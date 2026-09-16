"""
s07_wall_stair.py  --  STR007  STRUCTURAL REINFORCEMENT DETAILING
                       600 PERIMETER SHEAR WALL AND MAIN STAIRCASE

Four views, in the layout and with the title block of the supplied Revit A2 set
(ARCH001..ARCH005):

    1  600 PERIMETER SHEAR WALL W1-W4 - VERTICAL SECTION          1 : 30
    2  600 PERIMETER SHEAR WALL W1-W4 - PART PLAN / HORIZONTAL SECTION  1 : 25
    3  MAIN STAIRCASE, BAY 7 - REINFORCEMENT PLAN                  1 : 40
    4  MAIN STAIRCASE, BAY 7 - LONGITUDINAL SECTION C-C            1 : 40

Only the 600 walls are detailed here.  W5 200 and the 400 walls W6 / W7 appear
in the wall schedule so the sheet cannot be misread, and are cross-referenced,
not drawn.

THE MAIN STAIRCASE GEOMETRY IS FROZEN - 24R at 170.8333 / 280, 3 flights x 8,
total rise 4100, well 200, headroom 2533.  Every stair value below is read from
sc_proj.STAIR through sheet_data; nothing here changes it.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "Structural CAD", "Scripts"))

from a2_lib import A2Sheet, TXT                           # noqa: E402
import sheet_data as D                                    # noqa: E402

# ------------------------------------------------------------------- columns
LX, LW = 47.0, 125.0              # wall views        x  47 .. 172
MX, MW = 180.0, 150.0             # staircase views   x 180 .. 330
RX, RW = 338.0, 122.0             # schedules         x 338 .. 460

# ------------------------------------------------------------- view set-out
SC1 = 30.0                        # V1  wall vertical section
V1_X, V1_D = 62.0, 440.667        # u = -400 at x 62 ; level 0.000 at y 440.667
V1_TTL = 202.0

SC2 = 25.0                        # V2  wall part plan
V2_X, V2_Y = 48.0, 158.0          # v = 0 at x 48 ; u = 0 (earth face) at y 158
V2_TTL = 134.0

SC3 = 40.0                        # V3  staircase plan
V3_X, V3_Y = 210.0, 245.0         # X 15200 at x 210 ; Y 600 at y 245
V3_TTL = 228.0

SC4 = 40.0                        # V4  staircase section C-C
V4_X, V4_D = 182.0, 267.5         # Y 200 at x 182 ; level 0.000 at y 267.5
V4_TTL = 88.0

# levels used by more than one view
L_ROOF_T, L_ROOF_S = -2.000, -2.900
L_FLOOR, L_MAT_S, L_PCC = -6.100, -6.700, -6.800
L_L1, L_L2 = -4.7333, -3.3667

RISER, TREAD = 170.8333, 280.0
FLT_A = (15300, 16500)            # flights 1 and 3, stacked
FLT_B = (16700, 17900)            # flight 2


def W1(u, lvl):
    """V1: u across the wall (0 = earth face), level in metres -> paper."""
    return (V1_X + (u + 400) / SC1, V1_D + lvl * 1000.0 / SC1)


def P2(v, u):
    """V2: v along the wall, u across it (0 = earth face) -> paper."""
    return (V2_X + v / SC2, V2_Y + u / SC2)


def P3(mx, my):
    """V3: project plan coordinates -> paper."""
    return (V3_X + (mx - 15200) / SC3, V3_Y + (my - 600) / SC3)


def S4(my, lvl):
    """V4: project Y and level in metres -> paper."""
    return (V4_X + (my - 200) / SC4, V4_D + lvl * 1000.0 / SC4)


# =====================================================================  SHEET
s = A2Sheet(
    sheet_no="SHEET 07",
    drawing_no="STR007",
    title_lines=["STRUCTURAL", "REINFORCEMENT", "DETAILING -", "600 SHEAR WALL",
                 "& MAIN STAIRCASE"],
    project_lines=["CBRN HARDENED", "UG OPS ROOM"],
    identity=D.IDENTITY,
    notes=D.NOTES_07,
    date="16 SEP 2026",
    drawn="SYN 01",
    checked="DR IR CHAUDHARI",
    scale_note="As indicated",
    rev_note="SR1   16.09.2026",
)

# =====================================================================  VIEW 1
# 600 PERIMETER SHEAR WALL - VERTICAL SECTION
UOUT, UIN = -400, 1600            # drawn extent across the wall

# -- retained ground and the 300 M15 lean annulus
s.soil_hatch([W1(UOUT, L_ROOF_T), W1(-300, L_ROOF_T),
              W1(-300, L_MAT_S), W1(UOUT, L_MAT_S)], scale=0.9)
s.rect(*W1(-300, L_MAT_S), *W1(0, L_ROOF_T), "S-CONCRETE-THIN")
s.rock_hatch([W1(UOUT, L_PCC), W1(UIN, L_PCC), W1(UIN, L_PCC - 0.120),
              W1(UOUT, L_PCC - 0.120)], scale=1.1)

# -- concrete
s.rect(*W1(-300, L_PCC), *W1(UIN, L_MAT_S), "S-CONCRETE-THIN")      # 100 blinding
s.rect(*W1(0, L_MAT_S), *W1(UIN, L_FLOOR), "S-CONCRETE")            # 600 mat
s.rect(*W1(0, L_FLOOR), *W1(600, L_ROOF_S), "S-CONCRETE")           # 600 wall
s.rect(*W1(0, L_ROOF_S), *W1(UIN, L_ROOF_T), "S-CONCRETE")          # 900 roof slab
s.line(W1(600, L_ROOF_S), W1(UIN, L_ROOF_S), "S-CONCRETE")
s.line(W1(600, L_FLOOR), W1(UIN, L_FLOOR), "S-CONCRETE")
s.line(W1(1100, L_ROOF_S), W1(600, L_ROOF_S - 0.500), "S-CONCRETE")   # haunches
s.line(W1(1100, L_FLOOR), W1(600, L_FLOOR + 0.500), "S-CONCRETE")


# -- tanking membrane on the retained face and under the mat
s.pline([W1(0, L_ROOF_T), W1(0, L_MAT_S), W1(UIN, L_MAT_S)], "S-WATERPROOF")

# -- reinforcement
UE, UI = 83.0, 552.0                                   # curtain centres
s.bar([W1(UE, -5.950), W1(UE, L_ROOF_S)], "S-REBAR-MAIN")           # W01 vertical
s.bar([W1(UI, -5.950), W1(UI, L_ROOF_S)], "S-REBAR-MAIN")           # W02 vertical
n = int((L_ROOF_S - L_FLOOR) * 1000 / 150) + 1
for i in range(n):                                                   # W03 / W04
    lv = L_FLOOR + 0.050 + i * 0.150
    if lv > L_ROOF_S - 0.030:
        break
    s.bar_dot(W1(UE + 24, lv), 0.5, "S-REBAR-MAIN")
    s.bar_dot(W1(UI - 24, lv), 0.5, "S-REBAR-MAIN")
for i in range(int((L_ROOF_S - L_FLOOR) * 1000 / 200) + 1):          # W05 links
    lv = L_FLOOR + 0.100 + i * 0.200
    if lv > L_ROOF_S - 0.060:
        break
    a, b = W1(50, lv), W1(550, lv)
    s.line(a, b, "S-REBAR-STIRRUP")
    s.line(a, (a[0] + 1.0, a[1] + 1.0), "S-REBAR-STIRRUP")
    s.line(b, (b[0] - 1.0, b[1] + 1.0), "S-REBAR-STIRRUP")
for k in range(3):                                                   # W06 haunch
    o = k * 0.150
    s.bar([W1(1050 - k * 150, L_ROOF_S), W1(600, L_ROOF_S - 0.450 + o)],
          "S-REBAR-SEC")
    s.bar([W1(1050 - k * 150, L_FLOOR), W1(600, L_FLOOR + 0.450 - o)],
          "S-REBAR-SEC")
for u in (UE, UI):                                                   # F07 starters
    s.bar([W1(u + 900, -6.550), W1(u, -6.550), W1(u, -5.150)], "S-REBAR-SEC")
for lv in (-6.617, -6.158):                                          # mat curtains
    s.bar([W1(0, lv), W1(UIN, lv)], "S-REBAR-MAIN")
    s.bar_run(W1(0, lv), W1(UIN, lv), 150, SC1, "S-REBAR-MAIN", r=0.5)
for lv in (-2.8125, -2.0875):                                        # roof curtains
    s.bar([W1(0, lv), W1(UIN, lv)], "S-REBAR-MAIN")
    s.bar_run(W1(0, lv), W1(UIN, lv), 150, SC1, "S-REBAR-MAIN", r=0.5)

# -- kicker and construction joint
s.line(W1(0, -5.950), W1(600, -5.950), "S-CONCRETE")
s.circle(W1(300, -5.950), 0.9, "S-WATERPROOF")

# -- annotation
s.level(W1(UIN, L_ROOF_T), "(-)2.000", side="L")
s.level(W1(UIN, L_ROOF_S), "(-)2.900", side="L", dy=-4.0)
s.level(W1(UIN, L_FLOOR), "(-)6.100", side="L")
s.level(W1(UIN, L_MAT_S), "(-)6.700", side="L", dy=-4.0)
s.tag((150, 356), "W01", W1(UE, -3.350))
s.tag((150, 346), "W02", W1(UI, -3.750))
s.tag((150, 336), "W03", W1(UE + 24, -4.250))
s.tag((150, 326), "W05", W1(550, -4.650))
s.tag((150, 316), "W06", W1(900, L_FLOOR + 0.250))
s.tag((150, 306), "F07", W1(UE + 700, -6.550))
s.text("M15 LEAN", W1(-150, -4.100), TXT["small"], "S-TEXT", "C", rot=90.0)
s.text("TANKING", W1(-55, -3.150), TXT["small"], "S-WATERPROOF", "C", rot=90.0)
s.text("150 KICKER + 800 LAP", (W1(680, -5.870)[0], W1(0, -5.870)[1]),
       TXT["small"], "S-TEXT", "L")
s.text("500 x 500 HAUNCH, T20 @ 150", (100.0, 333.0), TXT["small"], "S-TEXT", "L")

s.dim_h(W1(0, L_ROOF_T), W1(600, L_ROOF_T), 379.5, SC1, "A2-DIM-S")
s.dim_v(W1(0, L_FLOOR), W1(0, L_ROOF_S), 57.0, SC1, "A2-DIM-S")
s.dim_v(W1(0, L_ROOF_S), W1(0, L_ROOF_T), 51.0, SC1, "A2-DIM-S")
s.dim_v(W1(0, L_MAT_S), W1(0, L_FLOOR), 51.0, SC1, "A2-DIM-S")

s.view_title(LX, V1_TTL, "1", "600 SHEAR WALL - VERTICAL SECTION",
             "1 : 30   W1 / W2 / W3 / W4.  T16 @ 150 EF EW,  COVER 75 / 40", LX + LW)

# =====================================================================  VIEW 2
# 600 PERIMETER SHEAR WALL - PART PLAN (HORIZONTAL SECTION)
VL = 3000
s.rect(*P2(0, 0), *P2(VL, 600), "S-CONCRETE")
s.soil_hatch([P2(0, -160), P2(VL, -160), P2(VL, 0), P2(0, 0)], scale=0.9)
s.line(P2(0, 0), P2(VL, 0), "S-WATERPROOF")

for u in (83.0, 552.0):                                   # W03 / W04 horizontal
    s.bar([P2(0, u), P2(VL, u)], "S-REBAR-MAIN")
for u in (107.0, 528.0):                                  # W01 / W02 vertical bars
    s.bar_run(P2(0, u), P2(VL, u), 150, SC2, "S-REBAR-MAIN", r=0.75)
for i in range(int(VL / 200) + 1):                        # W05 closed links
    v = 50 + i * 200
    if v > VL - 50:
        break
    s.link_rect(*P2(v - 75, 50), *P2(v + 75, 550), "S-REBAR-STIRRUP", hook=0.9)

s.dline(P2(VL - 40, -160), P2(VL - 40, 600), "S-CONCRETE-THIN")
s.text("CJ", P2(VL - 150, 300), TXT["small"], "S-TEXT", "C")
s.text("RETAINED EARTH FACE", P2(120, -120), TXT["small"], "S-TEXT", "L")
s.text("INTERNAL FACE", P2(120, 625), TXT["small"], "S-TEXT", "L")
s.tag((58, 148.0), "W05", P2(250, 300))
s.tag((86, 148.0), "W01", P2(900, 107))
s.tag((114, 148.0), "W03", P2(1500, 83))
s.tag((142, 148.0), "W02", P2(2200, 528))

s.dim_h(P2(0, 600), P2(VL, 600), 189.0, SC2, "A2-DIM-S")
s.dim_v(P2(0, 0), P2(0, 600), 45.0, SC2, "A2-DIM-S")

s.view_title(LX, V2_TTL, "2", "600 SHEAR WALL - PART PLAN",
             "1 : 25   HORIZONTAL SECTION AT (-)4.500", LX + LW)

# =====================================================================  VIEW 3
# MAIN STAIRCASE, BAY 7 - REINFORCEMENT PLAN
s.rect(*P3(14800, 600), *P3(15200, 5600), "S-CONCRETE")      # W6
s.rect(*P3(18000, 600), *P3(18400, 5600), "S-CONCRETE")      # W7
s.conc_hatch([P3(14800, 600), P3(15200, 600), P3(15200, 5600), P3(14800, 5600)],
             scale=1.4)
s.conc_hatch([P3(18000, 600), P3(18400, 600), P3(18400, 5600), P3(18000, 5600)],
             scale=1.4)
s.rect(*P3(15200, 600), *P3(18000, 5600), "S-CONCRETE")      # shaft 2800 x 5000

# -- landings, well and store
s.line(P3(15200, 1800), P3(18000, 1800), "S-CONCRETE")       # L2 / arrival edge
s.line(P3(15200, 3760), P3(18000, 3760), "S-CONCRETE")       # L1 edge
s.line(P3(15200, 4960), P3(18000, 4960), "S-CONCRETE")       # store edge
s.rect(*P3(16500, 1800), *P3(16700, 3760), "S-CONCRETE")     # 200 well
s.line(P3(16500, 1800), P3(16700, 3760), "S-CENTER")
s.line(P3(16500, 3760), P3(16700, 1800), "S-CENTER")

# -- treads, flight A (flights 1 and 3 stacked) and flight B (flight 2)
for fx0, fx1 in (FLT_A, FLT_B):
    for k in range(1, 7):
        y = 1800 + k * TREAD
        s.line(P3(fx0, y), P3(fx1, y), "S-CONCRETE-THIN")
s.text("UP", P3(15900, 2100), TXT["small"], "S-TEXT", "C")
s.bar([P3(15900, 2250), P3(15900, 3550)], "S-CENTER")
s.bar([P3(15760, 3350), P3(15900, 3550), P3(16040, 3350)], "S-CENTER")

# -- reinforcement
for i in range(9):                                            # ST01 main, flights
    x = FLT_A[0] + i * 150
    s.bar([P3(x, 1800), P3(x, 3760)], "S-REBAR-MAIN")
    s.bar([P3(x + 1400, 1800), P3(x + 1400, 3760)], "S-REBAR-MAIN")
for i in range(11):                                           # ST02 distribution
    y = 1800 + i * 200
    s.bar([P3(FLT_A[0], y), P3(FLT_A[1], y)], "S-REBAR-DIST")
    s.bar([P3(FLT_B[0], y), P3(FLT_B[1], y)], "S-REBAR-DIST")
for j in range(10):                                           # ST04 landing bottom
    y = 3800 + j * 125
    s.bar([P3(15250, y), P3(17950, y)], "S-REBAR-MAIN")
    s.bar([P3(15250, y - 3150), P3(17950, y - 3150)], "S-REBAR-MAIN")
for i in range(6):                                            # ST06 distribution
    x = 15300 + i * 500
    s.bar([P3(x, 3800), P3(x, 4920)], "S-REBAR-DIST")

s.text("LANDING L1  (-)4.7333", P3(16600, 4400), TXT["small"], "S-TEXT", "C")
s.text("STORE", P3(16600, 5280), TXT["small"], "S-TEXT", "C")
s.text("LANDING L2  (-)3.3667", P3(16600, 1150), TXT["small"], "S-TEXT", "C")
s.text("ARRIVAL LANDING (-)6.100 = MAT", P3(16600, 800), TXT["small"], "S-TEXT", "C")
s.text("W6", P3(15000, 3100), TXT["small"], "S-TEXT", "C", rot=90.0)
s.text("W7", P3(18200, 3100), TXT["small"], "S-TEXT", "C", rot=90.0)
s.tag((294, 340), "ST04", P3(17950, 4200))
s.tag((294, 330), "ST01", P3(16400, 3000))
s.tag((294, 320), "ST02", P3(17700, 2600))
s.tag((294, 310), "ST06", P3(17300, 4300))
s.secmark(P3(15900, 400), "C", "U")
s.secmark(P3(15900, 5850), "C", "D")
s.cline(P3(15900, 400), P3(15900, 5850), "S-CENTER")

s.dim_chain_h([P3(x, 0)[0] for x in (15200, 16500, 16700, 18000)],
              V3_Y, 377.0, SC3, "A2-DIM-S")
s.dim_chain_v([P3(0, y)[1] for y in (600, 1800, 3760, 4960, 5600)],
              P3(15200, 0)[0], 202.0, SC3, "A2-DIM-S")

s.view_title(MX, V3_TTL, "3", "MAIN STAIRCASE - REINFORCEMENT PLAN",
             "1 : 40   BAY 7.  24R @ 170.8333 / 280, 3 FLIGHTS x 8", MX + MW)

# =====================================================================  VIEW 4
# MAIN STAIRCASE - LONGITUDINAL SECTION C-C
def flight(y0, lvl0, dash=False):
    """Step profile + 200 waist soffit for one 8-riser flight starting at
    (y0, lvl0) and rising 8 x 170.8333 over 7 x 280."""
    lay = "S-HIDDEN" if dash else "S-CONCRETE"
    pts = [S4(y0, lvl0)]
    y, lv = y0, lvl0
    for k in range(8):
        lv += RISER / 1000.0
        pts.append(S4(y, lv))
        if k < 7:
            y += TREAD
            pts.append(S4(y, lv))
    s.pline(pts, lay)
    sof0 = lvl0 - 0.2343
    sof1 = lvl0 + 8 * RISER / 1000.0 - 0.2343 - RISER / 1000.0
    s.line(S4(y0, max(sof0, lvl0)), S4(y0 + 7 * TREAD, sof1), lay)
    return y0 + 7 * TREAD, lvl0 + 8 * RISER / 1000.0


# -- box perimeter walls at each end of the shaft
for a, b in ((200, 600), (5600, 6000)):
    s.rect(*S4(a, L_FLOOR), *S4(b, L_ROOF_S), "S-CONCRETE")
    s.conc_hatch([S4(a, L_FLOOR), S4(b, L_FLOOR), S4(b, L_ROOF_S), S4(a, L_ROOF_S)],
                 scale=1.4)

# -- mat, and the roof slab: over W1, then over the cantilever pad and W2
s.rect(*S4(200, L_MAT_S), *S4(6000, L_FLOOR), "S-CONCRETE")
s.rect(*S4(200, L_ROOF_S), *S4(600, L_ROOF_T), "S-CONCRETE")
s.rect(*S4(3760, L_ROOF_S), *S4(6000, L_ROOF_T), "S-CONCRETE")
s.text("STAIR VOID 3160 - NO SLAB OVER", S4(2180, -2.430), TXT["small"],
       "S-TEXT", "C")
s.text("CANTILEVER PAD 1840", S4(4680, -2.430), TXT["small"], "S-TEXT", "C")

# -- landings
s.rect(*S4(600, L_L2 - 0.200), *S4(1800, L_L2), "S-CONCRETE")        # L2
s.rect(*S4(3760, L_L1 - 0.200), *S4(4960, L_L1), "S-CONCRETE")       # L1

# -- flight 2, beyond the cut plane (it is at X 16700-17900)
s.pline([S4(3760, L_L1), S4(3760, L_L1 + 0.100)], "S-HIDDEN")
y, lv = 3760, L_L1
pts = [S4(y, lv)]
for k in range(8):
    lv += RISER / 1000.0
    pts.append(S4(y, lv))
    if k < 7:
        y -= TREAD
        pts.append(S4(y, lv))
s.pline(pts, "S-HIDDEN")

# -- flights 1 and 3, in the cut plane
flight(1800, L_FLOOR)
flight(1800, L_L2)

# -- reinforcement
for y0, lvl0 in ((1800, L_FLOOR), (1800, L_L2)):                     # ST01 / ST03
    sof0, sof1 = lvl0 - 0.2343 + 0.036, lvl0 + 7 * RISER / 1000.0 - 0.2343 + 0.036
    s.bar([S4(y0 - 600, lvl0 - 0.034), S4(y0, max(sof0, lvl0 - 0.034)),
           S4(y0 + 7 * TREAD, sof1), S4(y0 + 7 * TREAD + 600, sof1 + 0.070)],
          "S-REBAR-MAIN")
    s.bar([S4(y0, lvl0 + 0.100), S4(y0 + 800, lvl0 + 0.100 + 0.488)],
          "S-REBAR-SEC")
for ly0, ly1, lv in ((600, 1800, L_L2), (3760, 4960, L_L1)):         # ST04 / ST05
    s.bar([S4(ly0 + 40, lv - 0.164), S4(ly1 - 40, lv - 0.164)], "S-REBAR-MAIN")
    s.bar([S4(ly0 + 40, lv - 0.036), S4(ly0 + 940, lv - 0.036)], "S-REBAR-SEC")
    s.bar([S4(ly1 - 940, lv - 0.036), S4(ly1 - 40, lv - 0.036)], "S-REBAR-SEC")
s.bar([S4(300, L_FLOOR - 0.036), S4(5900, L_FLOOR - 0.036)], "S-REBAR-MAIN")
s.bar([S4(300, L_MAT_S + 0.083), S4(5900, L_MAT_S + 0.083)], "S-REBAR-MAIN")

# -- annotation
s.level(S4(700, L_FLOOR), "(-)6.100")
s.level(S4(4400, L_L1), "(-)4.7333")
s.level(S4(1200, L_L2), "(-)3.3667")
s.level(S4(5000, L_ROOF_T), "(-)2.000")
s.tag((196, 205), "ST01", S4(2600, -5.55))
s.tag((196, 195), "ST03", S4(2300, -3.05))
s.tag((196, 185), "ST04", S4(1100, L_L2 - 0.164))
s.tag((196, 175), "ST05", S4(1500, L_L2 - 0.036))
s.text("STORE", S4(5280, -5.700), TXT["small"], "S-TEXT", "C")
s.text("HEADROOM 2533", S4(2900, -4.150), TXT["small"], "S-TEXT", "C")
s.dim_v(S4(0, L_L1), S4(0, L_ROOF_T), 186.0, SC4, "A2-DIM-S")
s.dim_v(S4(0, L_FLOOR), S4(0, L_L2), 191.0, SC4, "A2-DIM-S")
s.dim_chain_h([S4(y, 0)[0] for y in (600, 1800, 3760, 4960, 5600)],
              S4(0, L_MAT_S)[1], 96.0, SC4, "A2-DIM-S")

s.view_title(MX, V4_TTL, "4", "MAIN STAIRCASE - SECTION C-C",
             "1 : 40   CUT ON FLIGHT A AT X 15900, LOOKING EAST", MX + MW)

# ===============================================================  panels, tables
s.panel(LX, 126.0, LW, "WALL AND STAIR - CONSTRUCTION REQUIREMENTS", D.PANEL_07,
        lead=3.05, max_h=90.0)

s.panel(MX, 78.0, MW, "MAIN STAIRCASE - THE GEOMETRY IS FROZEN", D.FROZEN_07,
        lead=3.2, max_h=42.0)

# SR1A, by instruction: the DESIGN BASIS panel that used to close this column
# is DELETED (master H.41).  D.BASIS_07 is kept, unaltered, in sheet_data.py
# for the record, but is no longer printed on this sheet.  The five schedules
# now fill the whole column: table_stack() solves for the row height that ends
# the stack exactly on the frame, so the freed space is not left empty.
y = s.table_stack(RX, 383.0, 35.5, RW, [
    dict(rows=D.WALL_SCHEDULE_ROWS, title="WALL SCHEDULE",
         header=["WALL", "THK", "LENGTH", "COVER", "d", "MAIN BARS", "LINKS"],
         align=["L", "C", "C", "C", "C", "L", "L"],
         pad=2.4),  # 7 columns in 122 mm; the default 2.8 forces < MIN_TXT_H
    dict(rows=D.wall_marks(),
         title="BAR MARK SCHEDULE - 600 PERIMETER SHEAR WALLS",
         header=["MARK", "BAR", "SPACING", "LOCATION", "CUT mm", "No."],
         align=["C", "C", "C", "L", "C", "C"]),
    dict(rows=D.STAIR_SCHEDULE, title="MAIN STAIRCASE - ELEMENT SCHEDULE",
         header=["ELEMENT", "THK", "d", "MAIN", "DISTRIB.", "TOP STEEL"],
         align=["L", "C", "C", "L", "L", "L"]),
    dict(rows=D.stair_marks(), title="BAR MARK SCHEDULE - MAIN STAIRCASE",
         header=["MARK", "BAR", "SPACING", "LOCATION", "CUT mm", "No."],
         align=["C", "C", "C", "L", "C", "C"]),
    dict(rows=D.NBC_CHECK,
         title="MAIN STAIRCASE - NBC 2016 PART 4 GEOMETRY CHECK",
         header=["ITEM", "PROVIDED", "LIMIT", "VERDICT"],
         align=["L", "L", "L", "L"]),
], gap=9.0, rh_max=7.6)
assert y > 35.0, f"the schedule stack overflows the frame: bottom at {y:.1f}"

if __name__ == "__main__":
    out = os.path.join(ROOT, "Presentation Sheets", "DXF",
                       "STR007_Structural_Reinforcement_Detailing_"
                       "Shear_Wall_and_Main_Staircase.dxf")
    s.save(out)
    print("written", out, "| right column bottom y =", round(y, 1))
