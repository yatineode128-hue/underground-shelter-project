"""
sc_proj.py  --  every geometric and material constant the Structural CAD
reinforcement package uses.  ONE definition of each value; change it here and it
propagates to every calculation, schedule and drawing.

SOURCE OF TRUTH: master/MASTER_PROJECT_STATE.md Parts A.3, A.4, A.5, A.7, B, F, L.
CROSS-CHECKED against current/cad/1_Underground_Level_Plan.dxf (post-M1) and the
shell-thickness groups in the underground .STD (audit sections A.1.3, A.2).

Units: MILLIMETRES for geometry, METRES for level annotation, kPa / kNm / mm^2.

SENTRY POST: OUT OF SCOPE.  No sentry constant appears in this file.
MAIN STAIRCASE: FROZEN.  24R @ 170.8333 / 280, 3 flights x 8, rise 4100.
"""

PACKAGE_REV = "SC1"
PACKAGE_DATE = "04.09.2026"
PROJECT = "UNDERGROUND CBRN-HARDENED BLAST-RESISTANT PROTECTIVE STRUCTURE"
LOCATION = "PUNE, MAHARASHTRA"
CLIENT = "B.E. CIVIL CAPSTONE - FOR ACTUAL CONSTRUCTION"
STRUCT_REV = "PHASE 2 REV A + M1"

# ------------------------------------------------------------------ materials
FCK = 35.0                 # M35, all in-scope structures
FY = 500.0                 # Fe500D to IS 1786:2008
FCK_DYN = 43.75            # IS 4991 Cl. 10.3.1, BLAST CASE ONLY
FY_DYN = 625.0             # IS 4991 Cl. 10.3.1, BLAST CASE ONLY
EC = 29580.0               # N/mm^2, IS 456 Cl. 6.2.3.1
GAMMA_RC = 25.0            # kN/m^3

COVER = dict(blinding=75, earth=50, internal=40, shaft=30)
LD_FACTOR = 40             # Ld tension  = 40 phi   (M35, Fe500D)
LDC_FACTOR = 32            # Ld compression = 32 phi
LAP_FACTOR = 50            # lap = 50 phi, staggered <= 50 % at a section
MAX_SPACING = 150          # EMP requirement, stricter than IS 456 Cl. 26.3.3
STOCK_BAR = 12000          # [ASSUMED - P-1] stock length, mm

# --------------------------------------------------------------- box geometry
BOX = dict(x0=0, x1=22000, y0=0, y1=6200)                 # external
INT = dict(x0=600, x1=21400, y0=600, y1=5600)             # internal clear
T_WALL = 600               # perimeter walls W1-W4
T_ROOF = 900               # pressure slab
T_MAT = 600                # mat foundation
T_PCC = 100                # M15 blinding
H_CLEAR = 3200             # internal clear height

# levels, metres relative to finished site grade 0.000
LVL = dict(grade=0.000, slab_top=-2.000, roof_soffit=-2.900, floor=-6.100,
           mat_soffit=-6.700, formation=-6.800, gwt=-2.000,
           L1=-4.7333, L2=-3.3667, hh_soffit=+0.400, hh_top=+0.900,
           asw_head=+2.450, asw_soffit=+2.200,
           sump_invert=-7.600, sump_base=-8.000)

# internal walls: (mark, x_start, x_end, thickness)
IW = [("W5", 12600, 12800, 200),
      ("W6", 14800, 15200, 400),      # MOD M1  - protective boundary
      ("W7", 18000, 18400, 400)]      # MOD M1  - protective boundary
PARTITIONS = [(3500, 3610), (5410, 5520), (9020, 9130), (10930, 11040)]
T_PART = 110
PART_DOOR_Y = (2500, 3400)            # 900 door gap in each partition

BAYS = [(1, 600, 3500, "STORES / 1000 L TANK / ESC 1"),
        (2, 3610, 5410, "LAVATORY + MEDICAL"),
        (3, 5520, 9020, "OPS ROOM / EMP ZONE 2"),
        (4, 9130, 10930, "BERTHING 9 BERTHS"),
        (5, 11040, 12600, "CBRN PLANT / SUMP"),
        (6, 12800, 14800, "DECON AIRLOCK 3 STAGE"),
        (7, 15200, 18000, "STAIR SHAFT"),
        (8, 18400, 21400, "GENERATOR / ESC 2")]

# ------------------------------------------------------------------- openings
BLAST_DOOR = dict(w=1200, h=2100, y0=600, y1=1800)        # in W6 and W7, 7 bar
ESC = [("ESC 1", 2050, 2050), ("ESC 2", 19900, 2050)]     # centres, post-M1
ESC_CLEAR_D = 1400
ESC_COLLAR_T = 250
ESC_COLLAR_OD = 1900
ESC_THICKEN = dict(t_from=900, t_to=1200, annulus=600)
ESC_CLEARANCE_RULE = 750   # opening edge to wall face -> bay >= 2900 wide

VOID = dict(x0=15200, x1=18000, y0=600, y1=3760)          # 2800 x 3160
PAD = dict(x0=15200, x1=18000, y0=3760, y1=5600)          # 2800 x 1840 cantilever
PAD_EDGE_THICKEN = dict(t_from=900, t_to=1200, width=600)

SUMP = dict(bay=5, t_wall=300, t_base=400)

# ------------------------------------------------- main staircase  -- FROZEN
STAIR = dict(risers=24, riser=170.8333, tread=280, flights=3, per_flight=8,
             total_rise=4100, width=1200, well=200, waist=200, headroom=2533,
             fltA=(15300, 16500), wellx=(16500, 16700), fltB=(16700, 17900),
             L1_y=(3760, 4960), L2_y=(600, 1800), arrival_y=(600, 1800),
             store_y=(4960, 5600), shaft=(15200, 18000, 600, 5600))

# ---------------------------------------------------------------- headhouse
HH = dict(x0=13600, x1=18400, y0=200, y1=6000,            # external, post-M1
          ix0=14000, ix1=18000, iy0=600, iy1=5600,        # internal
          t_wall=400, t_roof=500, clear_h=2400)
HH_DOOR = dict(x0=14450, x1=15350, w=900, h=2100, wall="HW2")
HH_BAND = dict(b=400, d=800, ext=600)                     # door-head edge band

# --------------------------------------------------- covered entry stairwell
ASW = dict(x0=9250, x1=16050, y0=5750, y1=7750,           # external, post-M1
           ix0=9500, ix1=15800, iy0=6000, iy1=7500,       # internal
           t_wall=250, t_roof=250, t_raft=300,
           top_landing=(9500, 11000), flight=(11000, 14300),
           platform=(14300, 15800), risers=12, riser=166.6667, going=300,
           waist=250, width=1500, door=(1000, 2100))

# --------------------------------------------------------------------- loads
LOADS = dict(
    p_so=344.7, td_min=0.13, td_max=1.33, p_r=1366.0, q_dyn=282.0,
    mu=5.0, dlf=1.111, p_design=383.0,
    roof_cover=40.65,            # NOTE CONFLICT C17 - the A.7.3 column sums 39.15
    roof_sidl=2.0, roof_self=22.50, roof_total=448.15,
    mat_self=15.0, mat_sidl=1.0, floor_ll=5.0,
    lateral_gradient=15.41, lateral_top=33.9, lateral_base=83.2,
    uplift=46.11, uplift_total_kN=6289.0,
    surcharge_v=20.0, surcharge_h=10.0, stair_on_walls=2.947,
    hh_roof=396.5, hh_wall=383.0,
    asw_flight_wu=22.85, asw_wall_base=34.0, asw_roof_wu=50.5, asw_landing=54.9,
    stair_flight_wu=21.0, stair_landing_w=44.20,
    T_roof_ms=13.4, box_Ah=0.075, box_Vb=1050.0)

COMBS = [(101, "ULS STATIC", "1.5 (DL + SIDL + LL + SOIL + UPLIFT)"),
         (102, "ULS UPLIFT", "0.9 DL + 1.5 UPLIFT"),
         (103, "BLAST  *** GOVERNS ***", "1.0 (DL + SIDL + SOIL + UPLIFT + BLAST)"),
         (104, "SLS CRACK WIDTH", "1.0 (DL + SIDL + LL + SOIL + UPLIFT), IS 3370 Pt 2"),
         (105, "CONSTRUCTION", "1.5 (DL + SOIL + UPLIFT + SURCHARGE)")]

# ------------------------------------------------------------- open items
OPEN_ITEMS = {
    "C16": "ROOF / PLATFORM JUNCTION - UNRESOLVED. A.4.7 says the roof over the "
           "platform becomes the 500 headhouse roof; B.6 / A.7.6 / F.2 design, "
           "load and register 250. DETAILED AT 250. NOT CLOSED - user ruling required.",
    "C17": "ENGINEERED COVER - UNRESOLVED, RAISED BY THIS PACKAGE. A.7.3 states "
           "40.65 kPa; its own column sums to 39.15 kPa. 40.65 HELD (larger, and "
           "the value in every .std). No reinforcement effect. User ruling required.",
    "A2":  "DESIGN GWT (-)2.000 IS [ASSUMED]. Water is two-thirds of the lateral "
           "load and all of the uplift. Monsoon monitoring required.",
    "A4":  "SUBGRADE MODULUS ks - master requires BOTH 100 000 and 500 000 kN/m3. "
           "Only 100 000 exists in any model.",
    "M1":  "NO STAAD RESULT EXISTS for any underground or entry-stairwell model. "
           "Every design action in this package is a hand calculation.",
    "M2":  "NO CODE DOCUMENT is in the workspace. Clause numbers are cited only "
           "from the verified master Part G register.",
    "P3":  "BLAST CAPACITY IS NOT DEMONSTRATED. Support rotation / ductility needs "
           "a non-linear SDOF check (IS 4991 Fig. 6 / Biggs) - Phase 3.",
}

# ------------------------------------------------------------------ helpers
def Ld(phi):
    return LD_FACTOR * phi


def lap(phi):
    return LAP_FACTOR * phi


def n_bars(run_mm, spacing):
    """Number of bars at `spacing` centres over `run_mm`, ends inclusive."""
    return int(run_mm // spacing) + 1


def split_bar(total_len, lap_len, stock=STOCK_BAR):
    """Split a run longer than stock into equal pieces with `lap_len` laps.
    Returns (n_pieces, piece_length).  n pieces of p cover  n*p - (n-1)*lap."""
    n = 1
    while True:
        p = (total_len + (n - 1) * lap_len) / n
        if p <= stock:
            return n, p
        n += 1
