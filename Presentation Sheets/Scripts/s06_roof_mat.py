"""
s06_roof_mat.py  --  STR006  STRUCTURAL REINFORCEMENT DETAILING
                     ROOF (PRESSURE) SLAB AND MAT FOUNDATION

Four views, all 1:100, in the layout and with the title block of the supplied
Revit A2 set (ARCH001..ARCH005):

    1  ROOF (PRESSURE) SLAB - REINFORCEMENT PLAN
    2  ROOF SLAB - LONGITUDINAL SECTION A-A   (cut at Y 2050, looking north)
    3  MAT FOUNDATION - REINFORCEMENT PLAN
    4  MAT FOUNDATION - LONGITUDINAL SECTION B-B   (cut at Y 2050, looking north)

Bars are called up by MARK ONLY, in the ellipse tag the ARCH series uses for its
room tags.  The two bar-mark schedules on the right carry the full description,
and both are generated from Structural CAD/Scripts/rebar_data.py, so a mark
cannot appear on this sheet without a schedule entry.

EVERY dimension, level, thickness, bar size, spacing and bar mark is taken from
master/MASTER_PROJECT_STATE.md Parts A.3, A.4, A.5, A.7.3, B.3, B.4, B.4.1 and
F.1.  Nothing is invented here.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "Structural CAD", "Scripts"))

from a2_lib import A2Sheet, vw, TXT                      # noqa: E402
import sheet_data as D                                   # noqa: E402

SC = 100.0                        # every view on this sheet is 1:100
PX0 = 51.0                        # common left edge of all four views
PW = 22000 / SC                   # 220.0 mm  ->  views span x 51 .. 271
RCOL, RCOL_W = 277.0, 183.0       # schedule column, x 277 .. 460
VDIM = 44.0                       # x base of the 6200 vertical dimensions
TDIM = 47.5                       # x base of the slab / mat thickness dimensions

V1_Y0 = 315.0                     # roof plan     315 .. 377
V1_DIM_TOP, V1_DIM_BOT, V1_TTL = 382.0, 308.5, 296.0
V2_DATUM, V2_TTL = 282.0, 229.5  # roof section, paper y of level 0.000
V3_Y0 = 152.0                     # mat plan      152 .. 214
V3_DIM_TOP, V3_DIM_BOT, V3_TTL = 219.0, 145.5, 134.0
V4_DATUM, V4_TTL = 176.0, 80.0    # mat section, paper y of level 0.000

P1 = vw(SC, PX0, V1_Y0)
P3 = vw(SC, PX0, V3_Y0)


def X2(mx):
    return PX0 + mx / SC


def L2(datum, lvl_m):
    """Level in metres -> paper y for a 1:100 section with `datum` at 0.000."""
    return datum + lvl_m * 1000.0 / SC


# =====================================================================  SHEET
s = A2Sheet(
    sheet_no="SHEET 06",
    drawing_no="STR006",
    title_lines=["STRUCTURAL", "REINFORCEMENT", "DETAILING -", "ROOF SLAB &",
                 "MAT FOUNDATION"],
    project_lines=["CBRN HARDENED", "UG OPS ROOM"],
    identity=D.IDENTITY,
    notes=D.NOTES_06,
    date="16 SEP 2026",
    drawn="SYN 01",
    checked="DR IR CHAUDHARI",
    scale_note="1 : 100",
    rev_note="SR1   16.09.2026",
)

VOID = (15200, 600, 18000, 3760)
PAD = (15200, 3760, 18000, 5600)

# =====================================================================  VIEW 1
# ROOF (PRESSURE) SLAB - REINFORCEMENT PLAN
s.rect(*P1(0, 0), *P1(22000, 6200), "S-CONCRETE")

for y in (600, 5600):                                     # walls below, dashed
    s.dline(P1(0, y), P1(22000, y), "S-HIDDEN")
for x in (600, 21400):
    s.dline(P1(x, 600), P1(x, 5600), "S-HIDDEN")
for x0, x1 in D.PARTITION_X:
    s.dline(P1(x0, 600), P1(x0, 5600), "S-HIDDEN")
    s.dline(P1(x1, 600), P1(x1, 5600), "S-HIDDEN")
for mark, x0, x1, t in D.IW:
    s.dline(P1(x0, 600), P1(x0, 5600), "S-HIDDEN")
    s.dline(P1(x1, 600), P1(x1, 5600), "S-HIDDEN")

# -- escape-shaft openings, 250 collars and the 600 thickened annulus
for name, cx, cy in D.ESC:
    s.circle(P1(cx, cy), 700 / SC, "S-CONCRETE")
    s.circle(P1(cx, cy), 950 / SC, "S-CONCRETE")
    s.circle(P1(cx, cy), 1550 / SC, "S-REBAR-SEC")
    s.cline(P1(cx - 1750, cy), P1(cx + 1750, cy), "S-CENTER")
    s.cline(P1(cx, cy - 1750), P1(cx, cy + 1750), "S-CENTER")
    for k in range(5):                                    # S08 trimmers
        o = 1700 + k * 150
        s.bar([P1(cx - o, cy - 1700), P1(cx - o, cy + 1700)], "S-REBAR-SEC")
        s.bar([P1(cx + o, cy - 1700), P1(cx + o, cy + 1700)], "S-REBAR-SEC")

# -- stair void, cantilever pad and its 600 free-edge thickening
s.rect(*P1(VOID[0], VOID[1]), *P1(VOID[2], VOID[3]), "S-CONCRETE")
s.line(P1(VOID[0], VOID[1]), P1(VOID[2], VOID[3]), "S-CENTER")
s.line(P1(VOID[0], VOID[3]), P1(VOID[2], VOID[1]), "S-CENTER")
s.dline(P1(PAD[0], 4360), P1(PAD[2], 4360), "S-REBAR-SEC")

# -- extra-bar bands (S14 over W6 / W7, S16 under headhouse wall HW3)
s.dline(P1(14550, 0), P1(14550, 6200), "S-REBAR-SEC")
s.dline(P1(15450, 3760), P1(15450, 6200), "S-REBAR-SEC")
s.dline(P1(15450, 0), P1(15450, 600), "S-REBAR-SEC")
s.dline(P1(17750, 3760), P1(17750, 6200), "S-REBAR-SEC")
s.dline(P1(18650, 0), P1(18650, 6200), "S-REBAR-SEC")
s.dline(P1(13200, 0), P1(13200, 6200), "S-REBAR-SEC")
s.dline(P1(14400, 0), P1(14400, 6200), "S-REBAR-SEC")

# -- S15, 4-T25 each face at 45 deg across both re-entrant corners of the void
for cx, sgn in ((15200, +1), (18000, -1)):
    s.bar([P1(cx - sgn * 1414, 3760 - 1414), P1(cx + sgn * 1414, 3760 + 1414)],
          "S-REBAR-SEC")

# -- sample runs of main steel, drawn at TRUE 150 spacing
s.bar_lines(P1(1200, 75), P1(1950, 75), P1(1200, 6125), P1(1950, 6125),
            150, SC, "S-REBAR-MAIN")                      # S01A / S03A
s.bar_lines(P1(75, 5000), P1(75, 5450), P1(21925, 5000), P1(21925, 5450),
            150, SC, "S-REBAR-MAIN")                      # S02A / S04A
s.bar_lines(P1(75, 1000), P1(75, 1450), P1(15125, 1000), P1(15125, 1450),
            150, SC, "S-REBAR-MAIN")                      # S02B, stops at the void
s.bar_lines(P1(18075, 1000), P1(18075, 1450), P1(21925, 1000), P1(21925, 1450),
            150, SC, "S-REBAR-MAIN")                      # S02C

# -- bar-mark tags
s.tag((86, 344), "S01A", (71.0, 344))
s.tag((110, 344), "S08", (94.5, 340))
s.tag((140, 335), "S02B", (140, 329.0))
s.tag((140, 358), "S02A", (140, 365.0))
s.tag((150, 358), "S16", (183.0, 355.0))
s.tag((188, 358), "S14", (196.5, 355.0))
s.tag((215, 362), "S12", (215, 358.6))
s.tag((250, 358), "S15", (240.0, 352.0))
s.north((167, 358))

# -- section line A-A and annotation
s.secmark((X2(700), V1_Y0 + 2050 / SC), "A", "R")
s.secmark((X2(21300), V1_Y0 + 2050 / SC), "A", "L")
s.cline(P1(700, 2050), P1(21300, 2050), "S-CENTER")
s.text("VOID  2800 x 3160", P1(16600, 2050), TXT["mark"], "S-TEXT", "C")
for mark, x0, x1, t in D.IW:
    s.text(mark, P1((x0 + x1) / 2, 6320), TXT["small"], "S-TEXT", "BC")

s.dim_h(P1(0, 6200), P1(22000, 6200), V1_DIM_TOP, SC)
s.dim_chain_h([X2(x) for x in D.BAY_CHAIN], V1_Y0, V1_DIM_BOT, SC)
s.dim_v(P1(0, 0), P1(0, 6200), VDIM, SC)

s.view_title(PX0, V1_TTL, "1", "ROOF (PRESSURE) SLAB - REINFORCEMENT PLAN",
             "1 : 100    SLAB 900 THK,  T25 @ 150 EF EW", PX0 + PW)

# =====================================================================  VIEW 2
# ROOF SLAB - LONGITUDINAL SECTION A-A
GRD = L2(V2_DATUM, 0.000)
TOP = L2(V2_DATUM, -2.000)
SOF = L2(V2_DATUM, -2.900)
STUB = L2(V2_DATUM, -3.800)

for hx0, hx1 in ((0, 3800), (18200, 22000)):      # hatch the ends only, so the
    s.soil_hatch([(X2(hx0), GRD), (X2(hx1), GRD),  # cover notes sit on clean paper
                  (X2(hx1), TOP), (X2(hx0), TOP)])
cy = GRD
for th, nm in D.COVER_LAYERS:                             # six layers, A.7.3
    cy -= th / SC
    s.line((X2(0), cy), (X2(22000), cy), "S-EXISTING")
s.line((X2(0), GRD), (X2(22000), GRD), "S-EXISTING")
s.rect(X2(0), L2(V2_DATUM, -0.650), X2(22000), L2(V2_DATUM, -0.450),
       "S-CONCRETE-THIN")                                 # 200 RC burster slab

for x0, x1 in ((0, 15200), (18000, 22000)):               # the slab itself
    s.rect(X2(x0), SOF, X2(x1), TOP, "S-CONCRETE")
for name, cx, cy_ in D.ESC:                               # openings + thickening
    s.rect(X2(cx - 700), SOF, X2(cx + 700), TOP, "S-CONCRETE")
    s.pline([(X2(cx - 1300), SOF), (X2(cx - 1300), SOF - 3.0),
             (X2(cx + 1300), SOF - 3.0), (X2(cx + 1300), SOF)], "S-CONCRETE")

for x0, x1 in D.WALLS_UNDER_ROOF:                         # walls below
    s.rect(X2(x0), STUB, X2(x1), SOF, "S-CONCRETE")
    s.conc_hatch([(X2(x0), STUB), (X2(x1), STUB), (X2(x1), SOF), (X2(x0), SOF)])
for x0, x1 in D.PARTITION_X:
    s.line((X2(x0), STUB), (X2(x0), SOF), "S-CONCRETE-THIN")
    s.line((X2(x1), STUB), (X2(x1), SOF), "S-CONCRETE-THIN")
for x0, x1 in D.WALLS_UNDER_ROOF:                         # 500 x 500 haunches
    if x0 > 0:
        s.line((X2(x0 - 500), SOF), (X2(x0), SOF - 5.0), "S-CONCRETE")
    if x1 < 22000:
        s.line((X2(x1 + 500), SOF), (X2(x1), SOF - 5.0), "S-CONCRETE")

# -- two curtains at 75 cover, T25 @ 150 EF EW, with the link zones
yb, yt = SOF + 87.5 / SC, TOP - 87.5 / SC
for x0, x1 in ((75, 15125), (18075, 21925)):
    s.line((X2(x0), yb), (X2(x1), yb), "S-REBAR-MAIN")
    s.line((X2(x0), yt), (X2(x1), yt), "S-REBAR-MAIN")
    s.bar_run((X2(x0), yb), (X2(x1), yb), 150, SC, "S-REBAR-MAIN", r=0.32)
    s.bar_run((X2(x0), yt), (X2(x1), yt), 150, SC, "S-REBAR-MAIN", r=0.32)
for x in list(range(200, 1700, 250)) + list(range(20400, 21900, 250)):
    s.line((X2(x), yb), (X2(x), yt), "S-REBAR-STIRRUP")   # S05  4-leg @ 250
for x in range(2100, 20400, 900):
    s.line((X2(x), yb), (X2(x), yt), "S-REBAR-STIRRUP")   # S06  2-leg @ 300

s.tag((115, 267), "S04A", (115, 261.5))
s.tag((135, 248), "S01A", (135, 254.0))
s.tag((66, 248), "S05", (60.0, 255.0))
s.tag((160, 248), "S06", (155.0, 257.5))

s.level((X2(2000), GRD), "+0.000   GRADE")
s.level((X2(2000), TOP), "(-)2.000   TOP OF SLAB")
s.level((X2(2000), SOF), "(-)2.900   SOFFIT", dy=-4.0)
s.note_leader((X2(6000), L2(V2_DATUM, -0.550)), (X2(8000), 279.5),
              "200 RC BURSTER SLAB M30, T12 @ 150 B/W, LAID TO 1:50 FALLS",
              h=TXT["small"], side="R")
s.text("2000 ENGINEERED COVER - 6 LAYERS - 40.65 kPa  (MASTER A.7.3)",
       (190, 270.5), TXT["small"], "S-TEXT", "C")
s.text("STAIR VOID 2800 - NO SLAB", (X2(16600), 257.5), TXT["small"],
       "S-TEXT", "C")
for mark, x0, x1, t in [("W3", 0, 600, 0)] + list(D.IW) + [("W4", 21400, 22000, 0)]:
    s.text(mark, (X2((x0 + x1) / 2), STUB - 3.2), TXT["small"], "S-TEXT", "C")
s.dim_v((X2(0), SOF), (X2(0), TOP), TDIM, SC, "A2-DIM-S")

s.view_title(PX0, V2_TTL, "2", "ROOF SLAB - LONGITUDINAL SECTION A-A",
             "1 : 100    CUT AT Y 2050, LOOKING NORTH", PX0 + PW)

# =====================================================================  VIEW 3
# MAT FOUNDATION - REINFORCEMENT PLAN
s.rect(*P3(0, 0), *P3(22000, 6200), "S-CONCRETE")
for y in (600, 5600):
    s.dline(P3(0, y), P3(22000, y), "S-HIDDEN")
for x in (600, 21400):
    s.dline(P3(x, 600), P3(x, 5600), "S-HIDDEN")
for x0, x1 in D.PARTITION_X:
    s.dline(P3(x0, 600), P3(x0, 5600), "S-HIDDEN")
    s.dline(P3(x1, 600), P3(x1, 5600), "S-HIDDEN")
for mark, x0, x1, t in D.IW:
    s.dline(P3(x0, 600), P3(x0, 5600), "S-HIDDEN")
    s.dline(P3(x1, 600), P3(x1, 5600), "S-HIDDEN")
    s.text(mark, P3((x0 + x1) / 2, 6320), TXT["small"], "S-TEXT", "BC")

SP = D.SUMP
s.rect(*P3(SP[0], SP[1]), *P3(SP[2], SP[3]), "S-CONCRETE")
s.line(P3(SP[0], SP[1]), P3(SP[2], SP[3]), "S-CENTER")
s.line(P3(SP[0], SP[3]), P3(SP[2], SP[1]), "S-CENTER")
for k in range(4):                                        # F10 trimmers
    s.bar([P3(SP[0] - 500 - k * 120, SP[1] - 800), P3(SP[0] - 500 - k * 120, SP[3] + 800)],
          "S-REBAR-SEC")
    s.bar([P3(SP[2] + 500 + k * 120, SP[1] - 800), P3(SP[2] + 500 + k * 120, SP[3] + 800)],
          "S-REBAR-SEC")

s.bar_lines(P3(1200, 50), P3(1950, 50), P3(1200, 6150), P3(1950, 6150),
            150, SC, "S-REBAR-MAIN")                      # F02 / F04
s.bar_lines(P3(50, 5000), P3(50, 5450), P3(21950, 5000), P3(21950, 5450),
            150, SC, "S-REBAR-MAIN")                      # F01 / F03
for i in range(9):                                        # F05 link-grid patch
    s.line(P3(5600 + i * 250, 2600), P3(5600 + i * 250, 4600), "S-REBAR-STIRRUP")
    s.line(P3(5600, 2600 + i * 250), P3(7600, 2600 + i * 250), "S-REBAR-STIRRUP")

s.tag((86, 190), "F02", (71.0, 190))
s.tag((140, 195), "F01", (140, 202.0))
s.tag((140, 180), "F05", (127.0, 188.0))
s.tag((240, 210), "F06", (263.0, 212.0))
s.tag((215, 166), "F07", (212.0, 158.0))
s.tag((150, 168), "F10", (161.0, 168.0))
s.north((167, 195))

s.secmark((X2(700), V3_Y0 + 2050 / SC), "B", "R")
s.secmark((X2(21300), V3_Y0 + 2050 / SC), "B", "L")
s.cline(P3(700, 2050), P3(21300, 2050), "S-CENTER")
s.text("SUMP PIT 1500 x 1500", P3(11820, 2900), TXT["small"], "S-TEXT", "C")

s.dim_h(P3(0, 6200), P3(22000, 6200), V3_DIM_TOP, SC)
s.dim_chain_h([X2(x) for x in D.BAY_CHAIN], V3_Y0, V3_DIM_BOT, SC)
s.dim_v(P3(0, 0), P3(0, 6200), VDIM, SC)

s.view_title(PX0, V3_TTL, "3", "MAT FOUNDATION - REINFORCEMENT PLAN",
             "1 : 100    MAT 600 THK,  T16 @ 150 EF EW", PX0 + PW)

# =====================================================================  VIEW 4
# MAT FOUNDATION - LONGITUDINAL SECTION B-B
MTOP = L2(V4_DATUM, -6.100)
MSOF = L2(V4_DATUM, -6.700)
PCC = L2(V4_DATUM, -6.800)
WTOP = L2(V4_DATUM, -5.200)
SPI = L2(V4_DATUM, -7.600)
SPB = L2(V4_DATUM, -8.000)

s.rock_hatch([(X2(0), PCC), (X2(22000), PCC), (X2(22000), PCC - 3.2),
              (X2(0), PCC - 3.2)])
s.rect(X2(-300), PCC, X2(22300), MSOF, "S-CONCRETE-THIN")      # 100 M15 blinding
for x0, x1 in ((0, SP[0]), (SP[2], 22000)):
    s.rect(X2(x0), MSOF, X2(x1), MTOP, "S-CONCRETE")
s.pline([(X2(SP[0]), MTOP), (X2(SP[0]), SPB), (X2(SP[2]), SPB),
         (X2(SP[2]), MTOP)], "S-CONCRETE")
s.line((X2(SP[0] + 300), MTOP), (X2(SP[0] + 300), SPI), "S-CONCRETE")
s.line((X2(SP[2] - 300), MTOP), (X2(SP[2] - 300), SPI), "S-CONCRETE")
s.line((X2(SP[0] + 300), SPI), (X2(SP[2] - 300), SPI), "S-CONCRETE")

for x0, x1 in D.WALLS_ON_MAT:
    s.rect(X2(x0), MTOP, X2(x1), WTOP, "S-CONCRETE")
    s.conc_hatch([(X2(x0), MTOP), (X2(x1), MTOP), (X2(x1), WTOP), (X2(x0), WTOP)])
for x0, x1 in D.PARTITION_X:
    s.line((X2(x0), MTOP), (X2(x0), WTOP), "S-CONCRETE-THIN")
    s.line((X2(x1), MTOP), (X2(x1), WTOP), "S-CONCRETE-THIN")
for x0, x1 in D.WALLS_ON_MAT:                             # 500 x 500 haunches
    if x0 > 0:
        s.line((X2(x0 - 500), MTOP), (X2(x0), MTOP + 5.0), "S-CONCRETE")
    if x1 < 22000:
        s.line((X2(x1 + 500), MTOP), (X2(x1), MTOP + 5.0), "S-CONCRETE")

yb, yt = MSOF + 83 / SC, MTOP - 83 / SC
for x0, x1 in ((50, SP[0] - 50), (SP[2] + 50, 21950)):
    s.line((X2(x0), yb), (X2(x1), yb), "S-REBAR-MAIN")
    s.line((X2(x0), yt), (X2(x1), yt), "S-REBAR-MAIN")
    s.bar_run((X2(x0), yb), (X2(x1), yb), 150, SC, "S-REBAR-MAIN", r=0.32)
    s.bar_run((X2(x0), yt), (X2(x1), yt), 150, SC, "S-REBAR-MAIN", r=0.32)
for x in range(300, 22000, 250):
    if SP[0] - 200 < x < SP[2] + 200:
        continue
    s.line((X2(x), yb), (X2(x), yt), "S-REBAR-STIRRUP")

for x0, x1 in D.WALLS_ON_MAT:                             # F07 / F08 / F09 starters
    a = x0 + 60 + (900 if x0 == 0 else -900)              # 900 leg, turned inboard
    b = x1 - 60 + (-900 if x1 == 22000 else 900)          # at the two end walls
    s.bar([(X2(a), yb), (X2(x0 + 60), yb), (X2(x0 + 60), WTOP)], "S-REBAR-SEC")
    s.bar([(X2(b), yb), (X2(x1 - 60), yb), (X2(x1 - 60), WTOP)], "S-REBAR-SEC")

s.tag((90, 121), "F03", (90, 114.0))
s.tag((118, 121), "F01", (118, 114.0))
s.tag((150, 121), "F05", (150, 114.5))
s.tag((215, 121), "F07", (212.0, 115.0))
s.tag((75, 101), "F04", (75, 107.5))
s.tag((125, 101), "F02", (125, 107.5))

s.level((X2(4000), MTOP), "(-)6.100   FLOOR")
s.level((X2(4000), MSOF), "(-)6.700", dy=-4.0)
s.level((X2(10800), SPB), "(-)8.000", side="L", dy=-4.0)
s.dline((X2(7000), MSOF - 1.6), (X2(10000), MSOF - 1.6), "S-REBAR-SEC")
s.note_leader((X2(8500), MSOF - 1.6), (X2(8500), 98.5),
              "DESIGN CASE 2 - 3.0 m SOFT / RED-BOLE BAND AT THE WORST "
              "POSITION - GOVERNS THE MAT", h=TXT["small"], side="R")
s.text("100 M15 BLINDING, TANKING OVER", (X2(17600), 103.2), TXT["small"],
       "S-TEXT", "L")
for mark, x0, x1, t in [("W3", 0, 600, 0)] + list(D.IW) + [("W4", 21400, 22000, 0)]:
    s.text(mark, (X2((x0 + x1) / 2), WTOP + 1.6), TXT["small"], "S-TEXT", "C")
s.dim_v((X2(0), MSOF), (X2(0), MTOP), TDIM, SC, "A2-DIM-S")

s.view_title(PX0, V4_TTL, "4", "MAT FOUNDATION - LONGITUDINAL SECTION B-B",
             "1 : 100    CUT AT Y 2050, LOOKING NORTH", PX0 + PW)

# =====================================================  left column, bottom panel
s.panel(PX0, 70.0, PW,
        "CONSTRUCTION REQUIREMENTS THAT ARE DESIGN OUTPUTS, NOT OPTIONS",
        D.PANEL_06, lead=3.05, max_h=34.0)

# ======================================================  right column, schedules
y = 383.0
y = s.table(RCOL, y, RCOL_W, D.ELEMENT_ROWS_06,
            title="ROOF SLAB AND MAT - ELEMENT SCHEDULE",
            header=["ELEMENT", "THK", "COVER", "d", "MAIN REINFORCEMENT", "LINKS"],
            rh=4.2, align=["L", "C", "C", "C", "L", "L"])

y = s.table(RCOL, y - 6.0, RCOL_W, D.roof_marks(),
            title="BAR MARK SCHEDULE - ROOF (PRESSURE) SLAB 900",
            header=["MARK", "BAR", "SPACING", "LOCATION", "CUT mm", "No."],
            rh=3.9, align=["C", "C", "C", "L", "C", "C"])

y = s.table(RCOL, y - 6.0, RCOL_W, D.mat_marks(),
            title="BAR MARK SCHEDULE - MAT FOUNDATION 600 AND SUMP PIT",
            header=["MARK", "BAR", "SPACING", "LOCATION", "CUT mm", "No."],
            rh=3.9, align=["C", "C", "C", "L", "C", "C"])

y = s.panel(RCOL, y - 6.0, RCOL_W, "DESIGN BASIS - THIS SHEET", D.BASIS_06,
            lead=3.05, max_h=y - 6.0 - 36.0)

if __name__ == "__main__":
    out = os.path.join(ROOT, "Presentation Sheets", "DXF",
                       "STR006_Structural_Reinforcement_Detailing_"
                       "Roof_Slab_and_Mat_Foundation.dxf")
    s.save(out)
    print("written", out, "| right column bottom y =", round(y, 1))
