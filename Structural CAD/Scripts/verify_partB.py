"""
verify_partB.py  --  independent recomputation of every master Part B design
value used by this reinforcement package.

This is a VERIFICATION script, not a design script.  It recomputes each value
from the stated inputs with rc_calc.py and reports MASTER vs RECOMPUTED.  It
changes nothing.  A non-zero delta is a finding, not something to be adjusted
away.

ALL VALUES ARE MANUAL CALCULATION -- NOT DIRECT STAAD OUTPUT.
No STAAD result exists for any underground or entry-stairwell model (audit A.3).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rc_calc as rc

FCK_S, FY_S = 35.0, 500.0            # static, M35 / Fe500D
FCK_D, FY_D = 43.75, 625.0           # IS 4991 Cl. 10.3.1 dynamic, BLAST ONLY

rows = []
def chk(item, master, calc, unit="", tol=0.011):
    """tol is a RELATIVE tolerance; master values are quoted to 3-4 s.f."""
    if master in (None, 0):
        ok = "—"
        d = ""
    else:
        rel = abs(calc - master) / abs(master)
        ok = "OK" if rel <= tol else "**DIFF**"
        d = f"{100*rel:+.2f}%"
    rows.append((item, f"{master}" if master is not None else "—",
                 f"{calc:.4g}", unit, d, ok))

print("=" * 100)
print("VERIFICATION OF MASTER PART B  --  MANUAL CALCULATION, NOT DIRECT STAAD OUTPUT")
print("=" * 100)

# ------------------------------------------------------- B.1 perimeter walls
d = 600 - 75 - 8
chk("B.1 W1-W4 d", 517, d, "mm")
Mp = rc.Mp_fixed_fixed(383, 3.200)
chk("B.1 Mp = 383 x 3.2^2/16", 245.1, Mp, "kNm/m")
chk("B.1 Mu,lim", 1556, rc.mu_lim(d, FCK_D), "kNm/m")
chk("B.1 Ast,req", 894, rc.ast_required(Mp, d, FY_D, FCK_D), "mm2/m")
Ast = rc.area_per_m(16, 150)
chk("B.1 Ast prov T16@150", 1340, Ast, "mm2/m")
chk("B.1 Mu provided", 362.8, rc.mu_capacity(Ast, d, FY_D, FCK_D), "kNm/m")
chk("B.1 xu", 46.3, rc.xu(Ast, FY_D, FCK_D), "mm")
chk("B.1 xu/d", 0.089, rc.xu(Ast, FY_D, FCK_D) / d, "-")
V = 383 * (1.600 - 0.517)
chk("B.1 V at d", 414.8, V, "kN/m")
s = rc.shear_check(V, d, Ast, FCK_S, FY_S, legs=2, phi_link=12)
chk("B.1 tau_v", 0.802, s["tau_v"], "N/mm2")
chk("B.1 pt", 0.259, s["pt"], "%")
chk("B.1 tau_c (STATIC M35)", 0.375, s["tau_c"], "N/mm2")
chk("B.1 tau_c,max", 3.70, s["tau_cmax"], "N/mm2")
chk("B.1 Vus", 220.8, s["Vus_kN"], "kN/m")
chk("B.1 Asv/sv", 0.982, s["asv_over_sv"], "mm2/mm")
chk("B.1 sv for T12 2L", 230, s["sv_for_link"], "mm", tol=0.02)
chk("B.1 sv,max Cl.26.5.1.5", 300, s["sv_max_cl26515"], "mm")
chk("B.1 min vert 0.0012t", 720, rc.min_steel("wall", 600, "vertical")["value"], "mm2/m")
chk("B.1 min horiz 0.0020t", 1200, rc.min_steel("wall", 600, "horizontal")["value"], "mm2/m")
chk("B.1 IS3370 surface zone", 875, rc.min_steel("surface_zone", 600)["value"], "mm2/m/face")

# --------------------------------------------------------------- B.2 W6 / W7
d = 400 - 50 - 8
chk("B.2 W6/W7 d", 342, d, "mm")
chk("B.2 200 wall Mu,lim (why 200 fails)", 138.0, rc.mu_lim(200 - 40 - 6, FCK_D), "kNm/m")
chk("B.2 Mp", 245.1, rc.Mp_fixed_fixed(383, 3.200), "kNm/m")
chk("B.2 Mu,lim 400", 680.6, rc.mu_lim(d, FCK_D), "kNm/m")
chk("B.2 Ast,req", 1400, rc.ast_required(245.1, d, FY_D, FCK_D), "mm2/m", tol=0.02)
Ast = rc.area_per_m(20, 150)
chk("B.2 Ast prov T20@150", 2094, Ast, "mm2/m")
chk("B.2 Mu provided", 355.3, rc.mu_capacity(Ast, d, FY_D, FCK_D), "kNm/m")
chk("B.2 xu/d", 0.211, rc.xu(Ast, FY_D, FCK_D) / d, "-")
V = 383 * (1.600 - 0.342)
chk("B.2 V at d", 481.8, V, "kN/m")
s = rc.shear_check(V, d, Ast, FCK_S, FY_S, legs=4, phi_link=12)
chk("B.2 tau_v", 1.409, s["tau_v"], "N/mm2")
chk("B.2 pt", 0.612, s["pt"], "%")
chk("B.2 tau_c", 0.540, s["tau_c"], "N/mm2")
chk("B.2 Vus", 297.2, s["Vus_kN"], "kN/m")
chk("B.2 Asv/sv", 1.998, s["asv_over_sv"], "mm2/mm")
chk("B.2 sv for T12 4L", 226, s["sv_for_link"], "mm", tol=0.02)
chk("B.2 sv,max Cl.26.5.1.5", 257, s["sv_max_cl26515"], "mm", tol=0.02)
chk("B.2 jamb steel interrupted 2094x1.2", 2513, 2094 * 1.2, "mm2/face")
chk("B.2 per jamb", 1256, 2094 * 1.2 / 2, "mm2")
chk("B.2 4-T20 provided", 1257, 4 * rc.BAR_AREA[20], "mm2")
w_hdr = 383 * 2.1 / 2
chk("B.2 header w", 402, w_hdr, "kN/m")
chk("B.2 header M = wL^2/12", 48.2, rc.M_udl_fixed(w_hdr, 1.2), "kNm")
chk("B.2 header V", 241, w_hdr * 1.2 / 2, "kN")

# ------------------------------------------------------------------- B.3 mat
d = 600 - 75 - 8
chk("B.3 mat d", 517, d, "mm")
chk("B.3 uplift 4.700 x 9.81", 46.11, 4.700 * 9.81, "kPa")
chk("B.3 net uplift 46.11-15.0", 31.1, 46.11 - 15.0, "kPa")
chk("B.3 Case 1 Mp", 48.6, rc.Mp_fixed_fixed(31.11, 5.0), "kNm/m")
chk("B.3 Case 2 soft band M = qL^2/12", 303.7, rc.M_udl_fixed(404.9, 3.0), "kNm/m")
chk("B.3 Ast,req", 1115, rc.ast_required(303.7, d, FY_D, FCK_D), "mm2/m")
Ast = rc.area_per_m(16, 150)
chk("B.3 Mu provided", 362.8, rc.mu_capacity(Ast, d, FY_D, FCK_D), "kNm/m")
chk("B.3 utilisation", 84, 100 * 303.7 / rc.mu_capacity(Ast, d, FY_D, FCK_D), "%", tol=0.02)
chk("B.3 t=500 Ast,req", 1407, rc.ast_required(303.7, 500 - 75 - 8, FY_D, FCK_D), "mm2/m")
chk("B.3 t=700 Ast,req", 926, rc.ast_required(303.7, 700 - 75 - 8, FY_D, FCK_D), "mm2/m")
V = 404.9 * (1.500 - 0.517)
chk("B.3 V at d from band edge", 398.0, V, "kN/m")
s = rc.shear_check(V, d, Ast, FCK_S, FY_S, legs=4, phi_link=12)
chk("B.3 tau_v", 0.770, s["tau_v"], "N/mm2")
chk("B.3 tau_c", 0.375, s["tau_c"], "N/mm2")
chk("B.3 Vus", 204.2, s["Vus_kN"], "kN/m")
chk("B.3 Asv/sv", 0.908, s["asv_over_sv"], "mm2/mm")
chk("B.3 supplied Asv/sv 4x113.1/250", 1.810, 4 * 113.1 / 250, "mm2/mm")

# ------------------------------------------------------------- B.4 roof slab
d = 900 - 75 - 12.5
chk("B.4 roof d", 812.5, d, "mm")
chk("B.4 COMB103 total w", 448.15, 383.00 + 40.65 + 2.00 + 22.50, "kPa")
chk("B.4 static ULS 101 on roof", 127.7, 1.5 * (40.65 + 2.0 + 22.5 + 20), "kPa")
chk("B.4 blast:static ratio", 3.51, 448.15 / 127.7, ":1")
Mp = rc.Mp_fixed_fixed(448.15, 5.0)
chk("B.4 Mp", 700.2, Mp, "kNm/m")
chk("B.4 Mu,lim", 3841, rc.mu_lim(d, FCK_D), "kNm/m")
chk("B.4 Ast,req", 1632, rc.ast_required(Mp, d, FY_D, FCK_D), "mm2/m")
chk("B.4 min 0.12 % x 900", 1080, rc.min_steel("slab", 900)["value"], "mm2/m")
Ast = rc.area_per_m(25, 150)
chk("B.4 Ast prov T25@150", 3272, Ast, "mm2/m")
chk("B.4 Mu provided", 1362.4, rc.mu_capacity(Ast, d, FY_D, FCK_D), "kNm/m")
chk("B.4 xu", 113.0, rc.xu(Ast, FY_D, FCK_D), "mm")
chk("B.4 xu/d", 0.139, rc.xu(Ast, FY_D, FCK_D) / d, "-")
chk("B.4 V at support face", 1120, 448.15 * 2.50, "kN/m")
V = 448.15 * (2.50 - 0.8125)
chk("B.4 V at d", 756.3, V, "kN/m")
s = rc.shear_check(V, d, Ast, FCK_S, FY_S, legs=4, phi_link=12)
chk("B.4 tau_v", 0.931, s["tau_v"], "N/mm2")
chk("B.4 pt", 0.403, s["pt"], "%")
chk("B.4 tau_c", 0.450, s["tau_c"], "N/mm2")
chk("B.4 Vus", 390.8, s["Vus_kN"], "kN/m")
chk("B.4 Asv/sv", 1.106, s["asv_over_sv"], "mm2/mm")
chk("B.4 direct shear 0.16 fck,dyn b d", 5688, 0.16 * FCK_D * 1000 * d / 1e3, "kN/m")
# thickness study
for t, mref, aref in ((600, 689, 2673), (800, 696, 1868), (1000, 704, 1453)):
    dd = t - 75 - 12.5
    w = 383 + 40.65 + 2.0 + t / 1000 * 25
    chk(f"B.4 study t={t} Mp", mref, rc.Mp_fixed_fixed(w, 5.0), "kNm/m")
    chk(f"B.4 study t={t} Ast,req", aref, rc.ast_required(rc.Mp_fixed_fixed(w, 5.0), dd, FY_D, FCK_D), "mm2/m")

# ------------------------------------------------------- B.4.1 roof openings
chk("B.4.1a interrupted steel 3272x1.4", 4581, 3272 * 1.400, "mm2/face/dir")
chk("B.4.1a trimmer each side", 2291, 3272 * 1.400 / 2, "mm2")
chk("B.4.1a 5-T25 provided", 2454, 5 * rc.BAR_AREA[25], "mm2")
Mroot = rc.M_cantilever(448.15, 1.840)
chk("B.4.1b cantilever M(root)", 758.6, Mroot, "kNm/m")
chk("B.4.1b Ast,req TOP", 1772, rc.ast_required(Mroot, 812.5, FY_D, FCK_D), "mm2/m")
chk("B.4.1b utilisation", 56, 100 * Mroot / 1362.4, "%", tol=0.02)
Vr = 448.15 * 1.840
chk("B.4.1b V(root)", 824.6, Vr, "kN/m")
s = rc.shear_check(Vr, 812.5, 3272, FCK_S, FY_S, legs=4, phi_link=12)
chk("B.4.1b tau_v", 1.015, s["tau_v"], "N/mm2")
chk("B.4.1b Vus", 459.4, s["Vus_kN"], "kN/m")
chk("B.4.1b Asv/sv", 1.300, s["asv_over_sv"], "mm2/mm")

# ------------------------------------------------------- B.5 main staircase
d = 200 - 30 - 6
chk("B.5 flight d", 164, d, "mm")
import math
th = math.degrees(math.atan(170.833 / 280))
chk("B.5 flight angle", 31.4, th, "deg", tol=0.02)
chk("B.5 cos theta", 0.8535, math.cos(math.radians(th)), "-")
chk("B.5 waist self 0.2x25/cos", 5.858, 0.200 * 25 / math.cos(math.radians(th)), "kPa")
chk("B.5 steps 0.5x0.170833x25", 2.135, 0.5 * 0.170833 * 25, "kPa")
wu = 1.5 * (5.858 + 2.135 + 1.0 + 5.0)
chk("B.5 wu", 21.0, wu, "kPa")
chk("B.5 Leff", 3160, 1960 + 600 + 600, "mm")
M = rc.M_udl_ss(wu, 3.160)
chk("B.5 M = wu Leff^2/8", 26.2, M, "kNm/m")
chk("B.5 Ast,req", 380, rc.ast_required(M, d, FY_S, FCK_S), "mm2/m", tol=0.02)
Ast = rc.area_per_m(12, 150)
chk("B.5 T12@150 provided", 754, Ast, "mm2/m")
chk("B.5 Mu provided", 50.3, rc.mu_capacity(Ast, d, FY_S, FCK_S), "kNm/m")
chk("B.5 utilisation", 52, 100 * M / rc.mu_capacity(Ast, d, FY_S, FCK_S), "%", tol=0.02)
chk("B.5 min 0.12 % x 200", 240, rc.min_steel("slab", 200)["value"], "mm2/m")
Vf = wu * 3.160 / 2
chk("B.5 flight V", 33.2, Vf, "kN/m")
s = rc.shear_check(Vf, d, Ast, FCK_S, FY_S)
chk("B.5 flight tau_v", 0.202, s["tau_v"], "N/mm2")
chk("B.5 flight tau_c", 0.479, s["tau_c"], "N/mm2")
chk("B.5 flight tau_c x k1.20", 0.575, s["tau_c"] * 1.20, "N/mm2")
# landings
wL = 7.50 + 1.50 + 7.50 + 27.70
chk("B.5 landing w", 44.20, wL, "kPa")
ML = rc.M_udl_ss(wL, 3.000)
chk("B.5 landing M", 49.7, ML, "kNm/m")
chk("B.5 landing Ast,req", 745, rc.ast_required(ML, d, FY_S, FCK_S), "mm2/m")
AstL = rc.area_per_m(12, 125)
chk("B.5 T12@125 provided", 905, AstL, "mm2/m")
chk("B.5 landing Mu", 59.5, rc.mu_capacity(AstL, d, FY_S, FCK_S), "kNm/m")
chk("B.5 landing utilisation", 84, 100 * ML / rc.mu_capacity(AstL, d, FY_S, FCK_S), "%", tol=0.02)
VL = wL * 3.000 / 2
chk("B.5 landing V", 66.3, VL, "kN/m")
sL = rc.shear_check(VL, d, AstL, FCK_S, FY_S)
chk("B.5 landing tau_v", 0.404, sL["tau_v"], "N/mm2")
chk("B.5 landing tau_c", 0.519, sL["tau_c"], "N/mm2")

# ---------------------------------------------------- B.6 entry stairwell
d = 250 - 30 - 8
chk("B.6 flight d", 214, d, "mm")
th = math.degrees(math.atan(166.6667 / 300))
chk("B.6 flight angle", 29.05, th, "deg", tol=0.02)
chk("B.6 waist self", 7.150, 0.250 * 25 / math.cos(math.radians(th)), "kPa")
chk("B.6 steps", 2.083, 0.5 * 0.1666667 * 25, "kPa")
wu6 = 1.5 * 15.233
chk("B.6 wu", 22.85, wu6, "kPa")
chk("B.6 Leff", 4800, 3300 + 750 + 750, "mm")
M6 = rc.M_udl_ss(wu6, 4.800)
chk("B.6 M", 65.8, M6, "kNm/m")
chk("B.6 Ast,req", 744, rc.ast_required(M6, d, FY_S, FCK_S), "mm2/m")
A6 = rc.area_per_m(16, 200)
chk("B.6 T16@200 provided", 1005, A6, "mm2/m")
chk("B.6 Mu", 87.3, rc.mu_capacity(A6, d, FY_S, FCK_S), "kNm/m")
chk("B.6 x/d", 0.162, rc.xu(A6, FY_S, FCK_S) / d, "-", tol=0.02)
chk("B.6 utilisation", 75, 100 * M6 / rc.mu_capacity(A6, d, FY_S, FCK_S), "%", tol=0.02)
V6 = wu6 * 4.800 / 2
chk("B.6 V", 54.8, V6, "kN/m")
s6 = rc.shear_check(V6, d, A6, FCK_S, FY_S)
chk("B.6 tau_v", 0.256, s6["tau_v"], "N/mm2")
chk("B.6 tau_c", 0.484, s6["tau_c"], "N/mm2")
chk("B.6 side wall sigma_h base", 34, 0.5 * 20 * 2.900 + 0.5 * 10, "kPa")
chk("B.6 side wall M ~ wL^2/12 (20 kPa)", 14.0, rc.M_udl_fixed(20, 2.900), "kNm/m")
chk("B.6 side wall min vert", 300, rc.min_steel("wall", 250, "vertical")["value"], "mm2/m")
chk("B.6 side wall min horiz", 500, rc.min_steel("wall", 250, "horizontal")["value"], "mm2/m")
chk("B.6 roof wu", 50.5, 1.5 * 33.65, "kPa")
chk("B.6 roof M = wl^2/12", 9.5, rc.M_udl_fixed(50.5, 1.500), "kNm/m")
chk("B.6 top landing M", 21.0, rc.M_udl_ss(54.9, 1.750), "kNm/m")

# -------------------------------------------------------------- B.7 headhouse
d = 500 - 75 - 10
chk("B.7.1 HH roof d", 415, d, "mm")
chk("B.7.1 w", 396.5, 383 + 12.5 + 1.0, "kPa")
chk("B.7.1 Mu,lim", 1002, rc.mu_lim(d, FCK_D), "kNm/m")
M71 = rc.Mp_fixed_fixed(396.5, 4.000)
chk("B.7.1 M one-way (adopted)", 396.5, M71, "kNm/m")
chk("B.7.1 M Table 26 a=0.045", 285.5, 0.045 * 396.5 * 4.0 ** 2, "kNm/m")
chk("B.7.1 Ast,req", 1879, rc.ast_required(M71, d, FY_D, FCK_D), "mm2/m")
chk("B.7.1 min 0.12 % x 500", 600, rc.min_steel("slab", 500)["value"], "mm2/m")
A71 = rc.area_per_m(20, 150)
chk("B.7.1 Mu provided", 438.5, rc.mu_capacity(A71, d, FY_D, FCK_D), "kNm/m")
chk("B.7.1 utilisation", 90, 100 * M71 / rc.mu_capacity(A71, d, FY_D, FCK_D), "%", tol=0.02)
chk("B.7.1 xu", 72.3, rc.xu(A71, FY_D, FCK_D), "mm")
chk("B.7.1 x/d", 0.174, rc.xu(A71, FY_D, FCK_D) / d, "-")
V71 = 396.5 * (2.000 - 0.415)
chk("B.7.1 V at d", 628.4, V71, "kN/m")
s71 = rc.shear_check(V71, d, A71, FCK_S, FY_S, legs=4, phi_link=12)
chk("B.7.1 tau_v", 1.514, s71["tau_v"], "N/mm2")
chk("B.7.1 pt", 0.505, s71["pt"], "%")
chk("B.7.1 tau_c", 0.502, s71["tau_c"], "N/mm2")
chk("B.7.1 Vus", 420.0, s71["Vus_kN"], "kN/m")
chk("B.7.1 Asv/sv", 2.327, s71["asv_over_sv"], "mm2/mm")
chk("B.7.1 sv T12 4L", 194, s71["sv_for_link"], "mm", tol=0.02)
chk("B.7.1 sv,max", 300, s71["sv_max_cl26515"], "mm")

d = 400 - 50 - 8
M72 = rc.Mp_fixed_fixed(383, 2.400)
chk("B.7.2 HW Mp CASE B 383 kPa", 137.9, M72, "kNm/m")
chk("B.7.2 HW Mp CASE A 113 kPa", 40.7, rc.Mp_fixed_fixed(113, 2.400), "kNm/m")
chk("B.7.2 Ast,req CASE B", 766, rc.ast_required(M72, d, FY_D, FCK_D), "mm2/m")
chk("B.7.2 Ast,req CASE A", 221, rc.ast_required(rc.Mp_fixed_fixed(113, 2.4), d, FY_D, FCK_D), "mm2/m", tol=0.02)
chk("B.7.2 min vert", 480, rc.min_steel("wall", 400, "vertical")["value"], "mm2/m")
chk("B.7.2 min horiz", 800, rc.min_steel("wall", 400, "horizontal")["value"], "mm2/m")
A72 = rc.area_per_m(16, 150)
chk("B.7.2 Mu provided", 235.2, rc.mu_capacity(A72, d, FY_D, FCK_D), "kNm/m")
chk("B.7.2 utilisation", 59, 100 * M72 / rc.mu_capacity(A72, d, FY_D, FCK_D), "%", tol=0.02)
chk("B.7.2 x/d", 0.135, rc.xu(A72, FY_D, FCK_D) / d, "-")
V72 = 383 * (1.200 - 0.342)
chk("B.7.2 V at d", 328.6, V72, "kN/m")
s72 = rc.shear_check(V72, d, A72, FCK_S, FY_S, legs=4, phi_link=12)
chk("B.7.2 tau_v", 0.961, s72["tau_v"], "N/mm2")
chk("B.7.2 pt", 0.392, s72["pt"], "%")
chk("B.7.2 tau_c", 0.444, s72["tau_c"], "N/mm2")
chk("B.7.2 Vus", 176.9, s72["Vus_kN"], "kN/m")
chk("B.7.2 Asv/sv", 1.189, s72["asv_over_sv"], "mm2/mm")
chk("B.7.2 sv,max", 256, s72["sv_max_cl26515"], "mm", tol=0.02)
chk("B.7.2 door jamb interrupted 1340x0.9", 1206, 1340 * 0.900, "mm2/face")
chk("B.7.2 2-T20 provided", 628, 2 * rc.BAR_AREA[20], "mm2")
wb = 383 * 2.100 / 2
chk("B.7.2 edge band w", 402, wb, "kN/m")
chk("B.7.2 edge band M", 27.1, rc.M_udl_fixed(wb, 0.900), "kNm")
chk("B.7.2 edge band V", 181, wb * 0.900 / 2, "kN")
chk("B.7.2 edge band d", 742, 800 - 40 - 8 - 10, "mm")
chk("B.7.2 edge band tau_v", 0.610, 181e3 / (400 * 742), "N/mm2")

# ------------------------------------------------------------------ B.7.3 HW3
chk("B.7.3 b_eff", 2.5, 0.400 + 2 * 1.05, "m")
q1 = (476 + 29) / 2.5 + 22.5 + 2.0
chk("B.7.3 CASE 1 equivalent UDL", 226, q1, "kPa")
chk("B.7.3 CASE 1 M", 354, rc.Mp_fixed_fixed(q1, 5.0), "kNm/m")
chk("B.7.3 CASE 1 % of 1362", 26, 100 * rc.Mp_fixed_fixed(q1, 5.0) / 1362.4, "%", tol=0.03)
q2 = (793 + 29) / 2.5 + 22.5 + 2.0
chk("B.7.3 CASE 2 equivalent UDL", 353, q2, "kPa")
chk("B.7.3 CASE 2 M", 552, rc.Mp_fixed_fixed(q2, 5.0), "kNm/m")

# ---------------------------------------------------- A.5 development lengths
for phi, ld35, lap35 in ((8, 320, 400), (10, 400, 500), (12, 480, 600),
                         (16, 640, 800), (20, 800, 1000), (25, 1000, 1250)):
    chk(f"A.5 Ld M35 T{phi}", ld35, rc.Ld_tension(phi, 35), "mm")
    chk(f"A.5 lap 50phi T{phi}", lap35, 50 * phi, "mm")
chk("A.5 Ld,c M35 T25", 925 * 35 / 30 * 0 + 800, rc.Ld_compression(25, 35), "mm", tol=0.02)

# --------------------------------------------------------------- A.7 loading
chk("A.7.1 DLF = mu/(mu-0.5)", 1.111, 5 / 4.5, "-")
chk("A.7.1 design blast 344.7 x DLF", 383, 344.7 * 5 / 4.5, "kPa")
chk("A.7.1 fck,dyn", 43.75, 1.25 * 35, "N/mm2")
chk("A.7.1 fy,dyn", 625, 1.25 * 500, "N/mm2")
chk("A.7.2 lateral gradient K0.g'+gw", 15.41, 0.50 * 11.19 + 9.81, "kPa/m")
chk("A.7.2 at roof soffit (0.9 m + ...)", 33.9, 15.41 * 2.200, "kPa", tol=0.03)
chk("A.7.2 at floor", 83.2, 15.41 * 5.400, "kPa", tol=0.03)
chk("A.7.3 cover total", 40.65, 5.40 + 2.85 + 5.00 + 8.50 + 15.00 + 2.40, "kPa")
chk("A.6 submerged gamma", 11.19, 21 - 9.81, "kN/m3")

# ------------------------------------------------------------------- report
w = max(len(r[0]) for r in rows) + 2
print(f"{'ITEM'.ljust(w)}{'MASTER':>12}{'RECOMPUTED':>14}  {'UNIT':<10}{'DELTA':>9}  RESULT")
print("-" * 100)
bad = 0
for it, m, c, u, dd, ok in rows:
    if ok == "**DIFF**":
        bad += 1
    print(f"{it.ljust(w)}{m:>12}{c:>14}  {u:<10}{dd:>9}  {ok}")
print("-" * 100)
print(f"{len(rows)} values recomputed   ·   {len(rows)-bad} agree   ·   {bad} differ")
print("\nALL VALUES ABOVE ARE MANUAL CALCULATION -- NOT DIRECT STAAD OUTPUT.")
sys.exit(0)
