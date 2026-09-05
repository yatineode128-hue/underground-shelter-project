"""
rc_calc.py  --  RC section calculation engine for the Structural CAD package.

Independent re-implementation of the design equations named in master Part B, so
that every reinforcement value used in this package can be RECOMPUTED rather than
copied.  Nothing here is read from a STAAD result: there are none (audit A.3).

Equations, all from master Part B / Part G verified clause register
------------------------------------------------------------------
  Mu      = 0.87 fy Ast d [1 - Ast fy /(b d fck)]      IS 456 Annex G-1.1(b)
  xu      = 0.87 fy Ast /(0.36 fck b)                  IS 456 Cl. 38.1
  xu,max/d= 0.46  (Fe500)                              IS 456 Cl. 38.1(f)
  Mu,lim  = 0.133 fck b d^2                            IS 456 Annex G-1.1(c)
  tau_v   = Vu /(b d)                                  IS 456 Cl. 40.1
  tau_c   = Table 19 (interpolated on pt)              IS 456 Table 19
  tau_cmax= Table 20                                   IS 456 Cl. 40.2.3
  Vus     = (tau_v - tau_c) b d                        IS 456 Cl. 40.4(a)
  Asv/sv  = Vus /(0.87 fy d)                           IS 456 Cl. 40.4(a)
  Ld      = phi * 0.87 fy /(4 tau_bd)                  IS 456 Cl. 26.2.1

BLAST CASE ONLY (IS 4991 Cl. 10.3.1):  fck,dyn = 1.25 fck, fy,dyn = 1.25 fy.
NO dynamic increase on shear (IS 4991 Cl. 10.3.1.1) -- tau_c and tau_c,max are
ALWAYS read at the STATIC grade.  This is enforced in shear_check(): it takes a
separate `fck_static` and ignores any dynamic value for tau_c.

Units: N, mm, N/mm^2.  Moments returned in kNm/m for a 1000 mm strip.
"""
import math

# --------------------------------------------------------------------- tables
# IS 456:2000 Table 19 -- design shear strength of concrete tau_c (N/mm^2).
# Verified against EIGHT independent master Part B values (see verify_partB.py):
# pt 0.259->0.375, 0.612->0.540, 0.403->0.450, 0.505->0.502, 0.392->0.444,
# 0.460->0.479, 0.552->0.519, 0.470->0.484 -- all M35, all reproduced exactly.
_PT = [0.15, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00]
TABLE19 = {
    20: [0.28, 0.36, 0.48, 0.56, 0.62, 0.67, 0.72, 0.75, 0.79, 0.81, 0.82, 0.82, 0.82],
    25: [0.29, 0.36, 0.49, 0.57, 0.64, 0.70, 0.74, 0.78, 0.82, 0.85, 0.88, 0.90, 0.92],
    30: [0.29, 0.37, 0.50, 0.59, 0.66, 0.71, 0.76, 0.80, 0.84, 0.88, 0.91, 0.93, 0.95],
    35: [0.29, 0.37, 0.50, 0.59, 0.67, 0.73, 0.78, 0.82, 0.86, 0.90, 0.93, 0.96, 0.99],
    40: [0.30, 0.38, 0.51, 0.60, 0.68, 0.74, 0.79, 0.84, 0.88, 0.92, 0.95, 0.98, 1.01],
}
# IS 456:2000 Table 20 -- tau_c,max
TABLE20 = {20: 2.8, 25: 3.1, 30: 3.5, 35: 3.7, 40: 4.0}

# IS 456 Cl. 26.2.1.1 -- design bond stress tau_bd for plain bars in tension,
# x1.6 for HYSD deformed bars (master A.5 reproduces M30 -> 2.40, M35 -> 2.72).
TAU_BD = {20: 1.2, 25: 1.4, 30: 1.5, 35: 1.7, 40: 1.9}

BAR_AREA = {6: 28.27, 8: 50.27, 10: 78.54, 12: 113.10, 16: 201.06,
            20: 314.16, 25: 490.87, 32: 804.25}
# unit mass kg/m = pi/4 d^2 * 7850e-9 * 1000 = 0.0061654 d^2
def bar_kg_per_m(phi):
    return 0.0061654 * phi * phi


def area_per_m(phi, spacing):
    """mm^2 per metre width for bars of diameter phi at `spacing` centres."""
    return BAR_AREA[phi] * 1000.0 / spacing


# ------------------------------------------------------------------- flexure
def mu_capacity(Ast, d, fy, fck, b=1000.0):
    """Ultimate moment capacity, kNm per `b` width.  IS 456 Annex G-1.1(b)."""
    return 0.87 * fy * Ast * d * (1.0 - Ast * fy / (b * d * fck)) / 1e6


def mu_lim(d, fck, b=1000.0):
    """Limiting singly-reinforced moment, kNm.  IS 456 Annex G-1.1(c)."""
    return 0.133 * fck * b * d * d / 1e6


def ast_required(Mu_kNm, d, fy, fck, b=1000.0):
    """Solve Annex G-1.1(b) for Ast.  Returns None if Mu > Mu,lim."""
    if Mu_kNm > mu_lim(d, fck, b):
        return None
    A = 0.87 * fy * fy / (b * fck)
    B = -0.87 * fy * d
    C = Mu_kNm * 1e6
    disc = B * B - 4 * A * C
    if disc < 0:
        return None
    return (-B - math.sqrt(disc)) / (2 * A)


def xu(Ast, fy, fck, b=1000.0):
    """Neutral axis depth, mm.  IS 456 Cl. 38.1."""
    return 0.87 * fy * Ast / (0.36 * fck * b)


# --------------------------------------------------------------------- shear
def tau_c(pt_percent, fck_static):
    """IS 456 Table 19, linear interpolation on pt.  fck_static ONLY --
    IS 4991 Cl. 10.3.1.1 forbids a dynamic increase on shear."""
    grade = min(TABLE19, key=lambda g: (abs(g - fck_static), g))
    col = TABLE19[grade]
    p = max(_PT[0], min(pt_percent, _PT[-1]))
    for i in range(len(_PT) - 1):
        if _PT[i] <= p <= _PT[i + 1]:
            f = (p - _PT[i]) / (_PT[i + 1] - _PT[i])
            return col[i] + f * (col[i + 1] - col[i])
    return col[-1]


def shear_check(Vu_kN, d, Ast, fck_static, fy_static, b=1000.0, legs=2, phi_link=12):
    """One-way shear to IS 456 Cl. 40.  Vu in kN per `b` width.

    Returns a dict.  fy_static is used for the links -- there is NO dynamic
    increase on shear (IS 4991 Cl. 10.3.1.1)."""
    tv = Vu_kN * 1e3 / (b * d)
    pt = 100.0 * Ast / (b * d)
    tc = tau_c(pt, fck_static)
    tcmax = TABLE20[min(TABLE20, key=lambda g: (abs(g - fck_static), g))]
    out = dict(tau_v=tv, pt=pt, tau_c=tc, tau_cmax=tcmax,
               tau_cmax_ok=tv <= tcmax, links_required=tv > tc)
    if tv > tc:
        Vus = (tv - tc) * b * d / 1e3                    # kN
        asv_sv = Vus * 1e3 / (0.87 * fy_static * d)      # mm^2/mm
        out["Vus_kN"] = Vus
        out["asv_over_sv"] = asv_sv
        out["sv_for_link"] = legs * BAR_AREA[phi_link] / asv_sv
    else:
        out["Vus_kN"] = 0.0
        out["asv_over_sv"] = 0.0
        out["sv_for_link"] = None
    # IS 456 Cl. 26.5.1.5 maximum link spacing
    out["sv_max_cl26515"] = min(0.75 * d, 300.0)
    return out


# ---------------------------------------------------------- development / lap
def Ld_tension(phi, fck, fy=500.0):
    """IS 456 Cl. 26.2.1 with Cl. 26.2.1.1 x1.6 for deformed bars in tension."""
    tbd = TAU_BD[min(TAU_BD, key=lambda g: (abs(g - fck), g))] * 1.6
    return phi * 0.87 * fy / (4.0 * tbd)


def Ld_compression(phi, fck, fy=500.0):
    """IS 456 Cl. 26.2.1.1 -- bond stress increased 25 % for compression."""
    return Ld_tension(phi, fck, fy) / 1.25


# ------------------------------------------------------------ minimum steel
def min_steel(element, thickness, direction=None):
    """Minimum reinforcement, mm^2/m.  Clause references are from the verified
    master Part G register only."""
    t = thickness
    if element == "slab":
        return dict(value=0.0012 * 1000 * t, clause="IS 456 Cl. 26.5.2.1 (0.12 % HYSD)")
    if element == "wall" and direction == "vertical":
        return dict(value=0.0012 * 1000 * t, clause="IS 456 Cl. 32.5(a)")
    if element == "wall" and direction == "horizontal":
        return dict(value=0.0020 * 1000 * t, clause="IS 456 Cl. 32.5(b)")
    if element == "surface_zone":          # IS 3370 Pt 2, 0.35 % over a 250 zone
        return dict(value=0.0035 * 1000 * 250, clause="IS 3370 Pt 2 (0.35 % over a 250 mm surface zone)")
    raise ValueError(element)


# ----------------------------------------------------------------- mechanisms
def Mp_fixed_fixed(w_kPa, Ln_m):
    """Plastic mechanism moment, fixed-fixed one-way strip:  w Ln^2 / 16."""
    return w_kPa * Ln_m ** 2 / 16.0


def M_udl_fixed(w_kPa, L_m):
    """Encastre elastic support moment w L^2 / 12."""
    return w_kPa * L_m ** 2 / 12.0


def M_udl_ss(w_kPa, L_m):
    """Simply supported mid-span moment w L^2 / 8."""
    return w_kPa * L_m ** 2 / 8.0


def M_cantilever(w_kPa, L_m):
    """Root moment of a UDL cantilever w L^2 / 2."""
    return w_kPa * L_m ** 2 / 2.0
