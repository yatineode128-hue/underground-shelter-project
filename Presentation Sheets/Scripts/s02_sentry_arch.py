"""
s02_sentry_arch.py  --  ARCH002  SENTRY POST: GROUND FLOOR LEVEL, FIRST FLOOR
                        LEVEL PLAN AND SOUTH ELEVATION

A REDRAW of sheet 2 of the owner's Revit A2 set, in the same frame and title
block, with the plan sizes and every level brought to the project's own
authoritative data (master A.4.3, A.4.8, SP-B1 / SP-B2) AND with every element
drawn as Rev F drawings 3 and 4 draw it - both DXFs were parsed, not
remembered.

    1  GROUND FLOOR LEVEL                                          1 :  75
    2  FIRST FLOOR LEVEL                                           1 :  75
    3  SOUTH ELEVATION - SHELTER AND SENTRY POST                   1 : 150
    4  LINTEL L1, WALL TIES AND THE 200 INFILL ZONE                1 :  20

The two plans are at 1 : 75, not the owner's 1 : 50, because the external
spiral stair is now drawn - it stands 2150 clear of the west wall - and two
plans with their stairs and grid bubbles do not fit side by side on A2 at
1 : 50.

The elevation is the view the owner's set uses to carry the levels, so it is
the view that carries the corrections: the sentry post ground floor is +0.450
and not 440, the entry stairwell roof head is +2.450 and not 3400, the post
roof slab and its parapet are two different levels (+6.700 and +7.000), and
(-)6.100 is the internal floor and top of mat, not the foundation level.

Every corrected figure is registered in arch_data.CORRECTIONS, and every case
where the Rev F drawing and the master disagree in arch_data.CAD_FINDINGS.
Both are reproduced in master Part H.  By instruction neither is printed here.

COLOUR: dark only, and mostly black - ACI 7, 8, 1, 5.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
for _p in ("Structural CAD", "Drainage"):
    sys.path.insert(0, os.path.join(ROOT, _p, "Scripts"))

from a2_lib import A2Sheet, vw                                # noqa: E402
import arch_data as D                                         # noqa: E402

RCOL, RCOL_W, RTOP = 282.0, 178.0, 383.0
RULE_TO, RULE_MID = 272.0, 152.0
SM, SMS = 1.9, 1.75

SC_PL = 75.0                                   # views 1 and 2
G1 = vw(SC_PL, 80.0, 285.0)                    # ground floor, model (0,0)
G2 = vw(SC_PL, 198.0, 285.0)                   # first floor
V12_TTL = 255.0

SC_EL = 150.0                                  # view 3
EL_X, EL_DATUM = 48.0, 175.0                   # model X 0 ; paper y of 0.000
EL_BREAK = 26000.0                             # the 10 m gap is broken here
EL_SHIFT = -7500.0                             # and the post pulled 7.5 m closer
V3_TTL = 121.0

SC_DT = 20.0                                   # view 4
DT = vw(SC_DT, 58.0, 52.0)
DT_H = 750.0                                   # height of the part elevation
V4_TTL = 40.0

EX, EY = D.SP_EXT_X, D.SP_EXT_Y                # 4000 x 5000
IZ = D.SP_INFILL                               # 200 structural infill zone
GA, GB, G_1, G_2 = D.SP_GRID_A, D.SP_GRID_B, D.SP_GRID_1, D.SP_GRID_2
CO = D.SP_COL                                  # 350
DY0, DY1 = D.SP_D1_OPENING                     # 1000 - 1900, the D1 opening


def EL(mx, lvl):
    """V3: model X (mm, project frame) and a level in metres -> paper.
    Everything east of EL_BREAK is pulled EL_SHIFT closer, across a break."""
    x = mx + (EL_SHIFT if mx > EL_BREAK else 0.0)
    return (EL_X + x / SC_EL, EL_DATUM + lvl * 1000.0 / SC_EL)


s = A2Sheet(
    sheet_no="SHEET 02",
    drawing_no="ARCH002",
    title_lines=["SENTRY POST -", "GROUND FLOOR", "LEVEL, FIRST",
                 "FLOOR LEVEL PLAN,", "SOUTH ELEVATION"],
    project_lines=D.PROJECT_LINES,
    identity=D.IDENTITY,
    notes=[
        "ALL DIMENSIONS ARE IN MM. ALL LEVELS ARE IN METRES RELATIVE TO "
        "FINISHED SITE GRADE 0.000, NEGATIVE DOWNWARDS.",
        "WRITTEN DIM TO BE FOLLOWED ONLY. DRG NOT TO BE SCALED.",
        "THIS DRG IS TO BE READ IN CONJUNCTION WITH ALL RELEVANT ARCH, STR AND "
        "SERVICES DRGS.",
        "THE SENTRY POST IS AN ABOVE-GROUND FRAMED STRUCTURE WITH BRICK "
        "INFILL. IT IS NOT BLAST RATED AND IT IS NOT PART OF THE PROTECTIVE "
        "BOUNDARY.",
        "WALL POSITIONS ARE IDENTICAL ON BOTH FLOORS. DOOR D1 IS IN THE WEST "
        "WALL AT Y 1000 - 1900 ON BOTH STOREYS, HINGED ON THE SOUTH JAMB AND "
        "OPENING EAST INTO THE ROOM, OFF THE EXTERNAL SPIRAL STAIR LANDING.",
        "THE FIRST FLOOR PROJECTS 300 ALL ROUND WITH A 300 HIGH PARDI OVER "
        "THE PROJECTION.",
        "GROUND-STOREY INFILL IS 190 ONE-BRICK MODULAR BRICKWORK TO IS 1077 "
        "IN CM 1:6, BUILT INSIDE THE UNCHANGED 200 STRUCTURAL ZONE BETWEEN "
        "THE COLUMN FACES, THE RESIDUAL 10 TAKEN UP AT THE INTERNAL FACE IN "
        "THE PLASTER.",
        "THE TOP COURSE IS BUILT TIGHT TO THE BEAM SOFFIT AND THE LAST JOINT "
        "PACKED. THE INFILL IS NOT SEPARATED FROM THE FRAME.",
        "WALL TIES 6 DIA MS AT EVERY FIFTH COURSE, APPROXIMATELY 450, UP BOTH "
        "COLUMN FACES, PROJECTING 200 INTO THE BED JOINT AND ANCHORED BY A "
        "CAST-IN OR DRILLED-AND-GROUTED 10 DOWEL.",
        "LINTEL L1, ONE TYPE OVER EVERY OPENING: 190 WIDE x 150 DEEP, M30 / "
        "Fe500, COVER 30, BEARING 200 EACH END.",
        "THE SENTRY POST STANDS CLEAR OF THE SHELTER EXCAVATION. ITS SITE "
        "POSITION IS X 32000 - 36000, Y 600 - 5600.",
        "THIS DRG HAS BEEN PREPARED IN ACCORDANCE WITH EXISTING CODES, NBC OF "
        "INDIA 2016, SOA 2009 AND SEISMIC LOADS.",
        "CONTRACTOR TO CHECK AND VERIFY THE DRG BEFORE EXECUTION.",
    ],
    date=D.DATE,
    drawn=D.DRAWN,
    checked=D.CHECKED,
    scale_note="As indicated",
)

for _nm, _col, _lw, _desc in [
    ("A-WALL",    7, 35, "Frame and walls, cut"),
    ("A-WALL-IN", 7, 18, "Infill, stairs and non-structural"),
    ("A-OVER",    8, 18, "Over or below the cut plane"),
    ("A-OPEN",    1, 35, "Doors, vision panels and openings"),
    ("A-EQUIP",   5, 25, "Reinforcement and ties shown on the detail"),
    ("A-COVER",   8, 18, "Ground, fill and cover"),
]:
    _ly = s.doc.layers.add(_nm)
    _ly.color, _ly.lineweight, _ly.description = _col, _lw, _desc


def swing(P, cx, cy, r, a0, a1, sc, layer="A-OPEN"):
    """A door as the Rev F CAD draws one: the leaf shown open, the face of the
    opening, and the swing arc between them."""
    s.arc(P(cx, cy), r / sc, a0, a1, layer)
    for a in (a0, a1):
        s.line(P(cx, cy), P(cx + r * math.cos(math.radians(a)),
                            cy + r * math.sin(math.radians(a))), layer)


def dashed_rect(P, x0, y0, x1, y1, layer="A-OVER", dash=1.6, gap=1.1):
    for a, b in (((x0, y0), (x1, y0)), ((x1, y0), (x1, y1)),
                 ((x1, y1), (x0, y1)), ((x0, y1), (x0, y0))):
        s.dline(P(*a), P(*b), layer, dash, gap)


def floor_plan(P, first):
    """The frame, the 200 infill zone, D1 and the openings, at one level."""
    # the external envelope, and the walls in the pieces the Rev F plan uses -
    # the west wall is in two pieces because D1 passes through it on BOTH floors
    s.rect(*P(0, 0), *P(EX, EY), "A-WALL")
    for x0, y0, x1, y1 in ((0, 0, IZ, DY0), (0, DY1, IZ, EY),
                           (EX - IZ, 0, EX, EY), (0, 0, EX, IZ),
                           (0, EY - IZ, EX, EY)):
        s.rect(*P(x0, y0), *P(x1, y1), "A-WALL")

    for cx, cy in D.SP_COL_SQUARES:                        # columns C1
        s.rect(*P(cx, cy), *P(cx + CO, cy + CO), "A-WALL")
        s.line(P(cx, cy), P(cx + CO, cy + CO), "A-WALL")
        s.line(P(cx, cy + CO), P(cx + CO, cy), "A-WALL")

    for gx in (GA, GB):                                    # grid lines
        s.cline(P(gx, -900), P(gx, EY + 900), "S-CENTER")
    for gy in (G_1, G_2):
        s.cline(P(-2500, gy), P(EX + 900, gy), "S-CENTER")
    for gx, lab in ((GA, "A"), (GB, "B")):
        s.circle(P(gx, 6200), 3.4 / 2.0, "S-GRID")
        s.text(lab, P(gx, 6200), SMS, "S-GRID", "C")
    for gy, lab in ((G_1, "1"), (G_2, "2")):
        s.circle(P(-2800, gy), 3.4 / 2.0, "S-GRID")
        s.text(lab, P(-2800, gy), SMS, "S-GRID", "C")

    # door D1, in the WEST wall, opening EAST into the room
    swing(P, *D.SP_D1_SWING, SC_PL)
    s.text("D1  900", P(900, 700), SMS, "S-TEXT", "C")

    if first:
        for x0, y0, x1, y1 in D.SP_PANELS_FF:              # vision panels
            s.rect(*P(x0, y0), *P(x1, y1), "A-OPEN")
        dashed_rect(P, *D.SP_PROJ_OUTLINE, "A-OVER")       # 300 projection
        for x0, x1 in D.SP_BEAM_BANDS_X:                   # B2 over, on A / B
            for y in (x0, x1):
                s.dline(P(y, G_1), P(y, G_2), "A-OVER", 1.4, 1.0)
        for y0, y1 in D.SP_BEAM_BANDS_Y:                   # B1 over, on 1 / 2
            for y in (y0, y1):
                s.dline(P(GA, y), P(GB, y), "A-OVER", 1.4, 1.0)
    else:
        s.rect(*P(D.SP_W1_GROUND[0], D.SP_W1_GROUND[1]),
               *P(D.SP_W1_GROUND[2], D.SP_W1_GROUND[3]), "A-OPEN")   # W1 east
        s.text("W1", P(3900, 2500), SMS, "S-TEXT", "C", rot=90.0)

    # the external spiral stair, 1000 R on a 250 dia central pole
    cx, cy = D.SP_SPIRAL_C
    s.circle(P(cx, cy), D.SP_SPIRAL_R / SC_PL, "A-WALL-IN")
    s.circle(P(cx, cy), D.SP_SPIRAL_POLE / 2.0 / SC_PL, "A-WALL")
    for k in range(D.SP_TREADS):
        a = math.radians(k * 360.0 / D.SP_TREADS)
        s.line(P(cx + D.SP_SPIRAL_POLE / 2.0 * math.cos(a),
                 cy + D.SP_SPIRAL_POLE / 2.0 * math.sin(a)),
               P(cx + D.SP_SPIRAL_R * math.cos(a),
                 cy + D.SP_SPIRAL_R * math.sin(a)), "A-WALL-IN")
    s.rect(*P(D.SP_SPIRAL_LANDING[0], D.SP_SPIRAL_LANDING[1]),
           *P(D.SP_SPIRAL_LANDING[2], D.SP_SPIRAL_LANDING[3]), "A-WALL-IN")
    (ax, ay), (bx, by) = D.SP_STAIR_ARROW
    s.line(P(ax, ay), P(bx, by), "A-WALL-IN")
    for dx in (-90.0, 90.0):
        s.line(P(bx, by), P(bx + dx, by - 180.0), "A-WALL-IN")

    s.dim_chain_h([P(v, 0)[0] for v in (0, IZ, EX - IZ, EX)], P(0, 0)[1],
                  P(0, -1000)[1], SC_PL, "A2-DIM-S", minlen=2.0)
    s.dim_h(P(0, 0), P(EX, 0), P(0, -1600)[1], SC_PL, "A2-DIM-S")
    s.dim_chain_v([P(0, v)[1] for v in (0, IZ, EY - IZ, EY)], P(EX, 0)[0],
                  P(EX + 800, 0)[0], SC_PL, "A2-DIM-S", minlen=2.0)
    s.dim_v(P(EX, 0), P(EX, EY), P(EX + 1400, 0)[0], SC_PL, "A2-DIM-S")


# =====================================================================  VIEW 1
floor_plan(G1, first=False)
s.text("SENTRY POST", G1(2000, 2950), SM, "S-TEXT", "C")
s.text("GROUND FLOOR  FFL +0.450", G1(2000, 2500), SMS, "S-TEXT", "C")
s.text("190 BRICK MASONRY INFILL (SP-B1)", G1(2000, 2050), SMS, "S-TEXT", "C")
s.text("B1 / B2  250 x 450  FIRST FLOOR BEAMS OVER", G1(2000, 3500), SMS,
       "S-TEXT", "C")
s.text("SPIRAL STAIR 1000 R", G1(-1150, 5400), SMS, "S-TEXT", "C")
s.text("250 DIA CENTRAL POLE", G1(-1150, 4950), SMS, "S-TEXT", "C")
s.view_title(56.0, V12_TTL, "1", "GROUND FLOOR LEVEL",
             "1 : 75   FFL +0.450", RULE_MID)

# =====================================================================  VIEW 2
floor_plan(G2, first=True)
s.text("OBSERVATION POST", G2(2000, 2950), SM, "S-TEXT", "C")
s.text("FIRST FLOOR  FFL +3.650", G2(2000, 2500), SMS, "S-TEXT", "C")
s.text("ARMOURED VISION PANELS 1200 WIDE", G2(2000, 2050), SMS, "S-TEXT", "C")
s.text("B1 / B2  250 x 450  ROOF BEAMS OVER", G2(2000, 3500), SMS,
       "S-TEXT", "C")
s.text("300 PROJECTION WITH 300 HIGH PARDI OVER", G2(2000, 5700), SMS,
       "S-TEXT", "C")
s.text("SPIRAL STAIR 1000 R", G2(-1150, 5400), SMS, "S-TEXT", "C")
s.text("250 DIA CENTRAL POLE", G2(-1150, 4950), SMS, "S-TEXT", "C")
s.view_title(174.0, V12_TTL, "2", "FIRST FLOOR LEVEL",
             "1 : 75   FFL +3.650", RULE_TO)

# =====================================================================  VIEW 3
# SOUTH ELEVATION, 1 : 150.  The shelter at true X, the post at true X across a
# break, and every level as master A.4.3.
B = D.BOX
s.hatch_pat([EL(-800, D.L_SLAB_TOP), EL(22800, D.L_SLAB_TOP),
             EL(22800, 0.0), EL(-800, 0.0)], "EARTH", 2.6, 0.0, "A-COVER")
s.line(EL(-800, 0.0), EL(22800, 0.0), "A-COVER")
s.line(EL(31200, 0.0), EL(36800, 0.0), "A-COVER")

for lvl0, lvl1 in ((D.L_ROOF_SOF, D.L_SLAB_TOP), (D.L_MAT_SOF, D.L_FLOOR)):
    s.rect(*EL(B["x0"], lvl0), *EL(B["x1"], lvl1), "A-OVER")
s.rect(*EL(B["x0"], D.L_FLOOR), *EL(B["x1"], D.L_SLAB_TOP), "A-OVER")
s.line(EL(B["x0"], D.L_FORMATION), EL(B["x1"], D.L_FORMATION), "A-COVER")
s.text("BURIED BOX  22000 x 6200", EL(6000, -4.20), SMS, "S-TEXT", "C")

H_ = D.HH                                                  # headhouse
s.rect(*EL(H_["x0"], D.L_SLAB_TOP), *EL(H_["x1"], D.L_HH_TOP), "A-WALL")
s.text("HEADHOUSE", EL(16000, -0.80), SMS, "S-TEXT", "C")
A_ = D.ASW                                                 # entry stairwell
s.pline([EL(A_["x0"], 0.0), EL(A_["x0"], D.L_ASW_HEAD),
         EL(A_["x1"], D.L_ASW_HEAD), EL(A_["x1"], D.L_SLAB_TOP)], "A-WALL")
s.text("COVERED ENTRY STAIRWELL", EL(12000, 1.10), SMS, "S-TEXT", "C")
for name, cx, cy, head in D.ESC:                           # escape shaft heads
    s.rect(*EL(cx - 950, 0.0), *EL(cx + 950, head), "A-OPEN")

# the sentry post, at true X across the break
SP = D.SP_SITE
s.rect(*EL(SP["x0"], D.SP_L_FOUND), *EL(SP["x1"], D.SP_L_FOUND + 0.600),
       "A-WALL")
s.rect(*EL(SP["x0"], 0.0), *EL(SP["x1"], D.SP_L_PARAPET), "A-WALL")
for lvl in (D.SP_L_PLINTH, D.SP_L_FF, D.SP_L_ROOF):
    s.line(EL(SP["x0"], lvl), EL(SP["x1"], lvl), "A-WALL")
# the first floor projects 300 all round with a 300 high pardi over it
PJ0, PJ1 = SP["x0"] - D.SP_PROJECTION, SP["x1"] + D.SP_PROJECTION
s.rect(*EL(PJ0, D.SP_L_FF - 0.150), *EL(PJ1, D.SP_L_FF), "A-WALL")
s.rect(*EL(PJ0, D.SP_L_FF), *EL(PJ1, D.SP_L_FF + D.SP_PARDI_H / 1000.0),
       "A-WALL")
# the two SOUTH-face vision panels, at the local X the Rev F plan gives them.
# D1 is in the west wall and the ground-storey W1 is in the east wall, so the
# ground storey shows no opening at all in a south elevation.
for x0, y0, x1, y1 in D.SP_PANELS_FF:
    if y0 != 0.0:
        continue
    s.rect(*EL(SP["x0"] + x0, D.SP_L_FF + 1.100),
           *EL(SP["x0"] + x1, D.SP_L_FF + 2.300), "A-OPEN")
s.text("SENTRY POST", EL(SP["x0"] + 2000, 6.25), SMS, "S-TEXT", "C")

# the break in the 10 m gap.  22275 is unshifted and 31725 is shifted, so the
# two lines land either side of the paper gap between the box and the post.
for bx in (23400.0, 31500.0):
    s.dline(EL(bx, -7.400), EL(bx, 7.600), "S-CENTER", 2.2, 1.5)
s.text("BREAK", EL(23400.0, -5.100), SMS, "S-TEXT", "C", rot=90.0)

# (level, label, text offset in mm -- tightly spaced levels are staggered so
# that two labels 300 mm apart cannot touch at 1 : 150)
LEVELS_EL = [
    (D.SP_L_PARAPET, "+7.000  PARAPET TOP", 1.8),
    (D.SP_L_ROOF, "+6.700  POST ROOF SLAB", -1.8),
    (D.SP_L_FF, "+3.650  POST FIRST FLOOR", 0.0),
    (D.L_ASW_HEAD, "+2.450  STAIRWELL ROOF HEAD", 0.0),
    (D.L_HH_TOP, "+0.900  HEADHOUSE ROOF", 1.4),
    (D.SP_L_PLINTH, "+0.450  POST GROUND FFL", -1.4),
    (0.0, "0.000  FINISHED SITE GRADE", -3.6),
    (D.L_SLAB_TOP, "(-)2.000  PRESSURE SLAB TOP", 0.0),
    (D.L_ROOF_SOF, "(-)2.900  ROOF SOFFIT", 0.0),
    (D.L_FLOOR, "(-)6.100  FLOOR / MAT TOP", 1.4),
    (D.L_MAT_SOF, "(-)6.700  MAT SOFFIT", -1.4),
]
LX = EL(36900, 0.0)[0]
for lvl, lab, dy in LEVELS_EL:
    ly = EL(0, lvl)[1]
    s.line(EL(36000 if lvl > 0.0 else 22400, lvl), (LX, ly), "S-LEVEL")
    s.msp.add_blockref("A2-LEVEL", (LX, ly), dxfattribs={"layer": "S-LEVEL"})
    s.text(lab, (LX + 2.6, ly + 2.4 + dy), SMS, "S-LEVEL", "ML")
s.text("(-)6.800  FORMATION", EL(1000, -6.35), SMS, "S-TEXT", "ML")
s.text("(-)2.000  POST FOUNDING LEVEL, F1 ON IN-SITU BASALT",
       EL(7000, -6.35), SMS, "S-TEXT", "ML")
s.dim_v(EL(SP["x0"], D.SP_L_PLINTH), EL(SP["x0"], D.SP_L_FF),
        EL(SP["x0"] + 700, 0)[0], SC_EL, "A2-DIM-S")
s.dim_v(EL(SP["x0"], D.SP_L_FF), EL(SP["x0"], D.SP_L_ROOF),
        EL(SP["x0"] + 700, 0)[0], SC_EL, "A2-DIM-S")
s.view_title(44.0, V3_TTL, "3", "SOUTH ELEVATION - SHELTER AND SENTRY POST",
             "1 : 150   SENTRY POST AT TRUE X ACROSS A BREAK", RULE_TO)

# =====================================================================  VIEW 4
# LINTEL L1, WALL TIES AND THE 200 INFILL ZONE, 1 : 20
BR, LT_B, LT_D = D.SP_BRICK, 190.0, 150.0
s.rect(*DT(0, 0), *DT(1600, DT_H), "A-WALL-IN")
for k in range(1, 5):                                     # brick courses
    s.line(DT(0, k * 150.0), DT(1600, k * 150.0), "A-WALL-IN")
s.rect(*DT(-CO, 0), *DT(0, DT_H), "A-WALL")               # column C1 beyond
s.conc_hatch([DT(-CO, 0), DT(0, 0), DT(0, DT_H), DT(-CO, DT_H)], scale=0.5)
s.rect(*DT(200, 350), *DT(1400, 500), "A-OPEN")           # lintel L1
s.conc_hatch([DT(200, 350), DT(1400, 350), DT(1400, 500), DT(200, 500)],
             scale=0.5)
s.bar([DT(240, 385), DT(1360, 385)], "A-EQUIP")
s.bar([DT(240, 465), DT(1360, 465)], "A-EQUIP")
for k in range(9):
    x = 240.0 + k * 140.0
    s.bar([DT(x, 385), DT(x, 465)], "A-EQUIP")
for k in (1, 4):                                          # 6 dia ties @ 450
    s.bar([DT(-40, k * 150.0), DT(200, k * 150.0)], "A-EQUIP")
s.text("190 BRICKWORK IN THE 200 ZONE", DT(800, 690), SMS, "S-TEXT", "C")
s.text("LINTEL L1  190 x 150", DT(800, 560), SMS, "S-TEXT", "C")
s.text("2-T10 BOTTOM, 2-T8 TOP, T6 LINKS AT 150", DT(800, 200), SMS,
       "S-TEXT", "C")
s.text("C1", DT(-CO / 2, 620), SMS, "S-TEXT", "C", rot=90.0)
s.note_leader(DT(100, 600), (DT(1820, 690)[0], DT(0, 690)[1]),
              "6 DIA MS TIES AT EVERY FIFTH COURSE, 200 INTO THE BED JOINT",
              SMS, "R")
s.dim_h(DT(200, 350), DT(1400, 350), DT(0, 60)[1], SC_DT, "A2-DIM-S")
s.dim_v(DT(1400, 350), DT(1400, 500), DT(1560, 0)[0], SC_DT, "A2-DIM-S")
s.view_title(52.0, V4_TTL, "4", "LINTEL L1, WALL TIES AND THE 200 INFILL ZONE",
             "1 : 20   ONE LINTEL TYPE SERVES ALL ELEVEN OPENINGS", RULE_TO)

# =====================================================================  TABLES
ELEMENT_ROWS = [
    ["C1  COLUMN", "350 x 350", "4 No., BOTH STOREYS", "40",
     "AT THE FOUR CORNERS, OUTER FACES FLUSH"],
    ["B1  BEAM", "250 x 450", "SPANS A-B, 3650 c/c", "30", "ON GRIDS 1 AND 2"],
    ["B2  BEAM", "250 x 450", "SPANS 1-2, 4650 c/c", "30", "ON GRIDS A AND B"],
    ["S1  SLAB", "150 THK", "3650 x 4650 c/c, TWO-WAY", "30", "BOTH FLOORS"],
    ["PB  PLINTH BEAM", "250 x 400", "AT +0.450", "30", "TOP = GROUND FFL"],
    ["F1  ISOLATED FOOTING", "1500 x 1500 x 600", "4 No.", "50",
     "ON IN-SITU BASALT AT (-)2.000"],
    ["GROUND INFILL", "200 ZONE", "190 BRICKWORK IS 1077, CM 1:6", "-",
     "10 TAKEN UP IN THE INTERNAL PLASTER"],
    ["FIRST STOREY INFILL", "200 ZONE", "ARMOURED VISION PANELS 1200 WIDE",
     "-", "ALL FOUR FACES"],
    ["FIRST FLOOR PROJECTION", "300 WIDE", "ALL ROUND", "-",
     "300 HIGH PARDI OVER THE PROJECTION"],
    ["SPIRAL STAIR", "1000 R", "EXTERNAL, WEST OF THE POST", "-",
     "250 DIA CENTRAL POLE, 12 TREADS, LANDING AT D1"],
    ["L1  LINTEL", "190 x 150", "OVER EVERY OPENING", "30",
     "2-T10 BTM, 2-T8 TOP, T6 LINKS AT 150, BEARING 200"],
]
GRID_ROWS = [
    ["A", "X", "175", "3650 c/c TO GRID B"],
    ["B", "X", "3825", "-"],
    ["1", "Y", "175", "4650 c/c TO GRID 2"],
    ["2", "Y", "4825", "-"],
]
SP_LEVELS = [
    ["PARAPET TOP", "+7.000", "-"],
    ["ROOF SLAB", "+6.700", "FIRST STOREY HEIGHT 3050"],
    ["FIRST FLOOR", "+3.650", "GROUND STOREY HEIGHT 3200"],
    ["GROUND FLOOR FFL", "+0.450", "= TOP OF PLINTH BEAM PB"],
    ["PLINTH BEAM SOFFIT", "+0.050", "PB 250 x 400"],
    ["FINISHED SITE GRADE", "0.000", "-"],
    ["FOUNDING LEVEL", "(-)2.000", "F1 ON IN-SITU BASALT"],
]
OPEN_ROWS = [
    ["D1", "DOOR", "900 x 2100", "WEST WALL, Y 1000-1900, BOTH STOREYS",
     "OPENS EAST"],
    ["W1", "ARMOURED VISION PANEL", "1200 WIDE",
     "EAST WALL, Y 1900-3100, GROUND STOREY", "1 No."],
    ["W1", "ARMOURED VISION PANEL", "1200 WIDE",
     "FIRST STOREY, ALL FOUR FACES", "TWO PER FACE"],
    "EVERY OPENING HAS A LINTEL L1 190 x 150 OVER IT, BEARING 200 EACH END",
]

y = s.table_stack(RCOL, RTOP, 35.5, RCOL_W, [
    dict(rows=ELEMENT_ROWS, title="SENTRY POST ELEMENT SCHEDULE",
         header=["ELEMENT", "SIZE", "EXTENT", "COVER", "NOTES"],
         align=["L", "C", "L", "C", "L"], pad=2.2),
    dict(rows=GRID_ROWS, title="COLUMN GRID SCHEDULE",
         header=["GRID", "AXIS", "COORDINATE", "SPACING"],
         align=["C", "C", "C", "L"], pad=2.2),
    dict(rows=SP_LEVELS, title="SENTRY POST LEVEL SCHEDULE",
         header=["LEVEL", "VALUE", "NOTES"], align=["L", "C", "L"], pad=2.2),
    dict(rows=OPEN_ROWS, title="DOOR AND OPENING SCHEDULE",
         header=["MARK", "TYPE", "SIZE", "POSITION", "No."],
         align=["C", "L", "C", "L", "C"], pad=2.2),
], gap=6.0, rh_max=7.2)
assert y > 35.0, f"the schedule stack overflows the frame: bottom at {y:.1f}"


if __name__ == "__main__":
    out = os.path.join(ROOT, "Presentation Sheets", "DXF",
                       "ARCH002_Sentry_Post_Floor_Plans_and_South_Elevation_"
                       "Redrawn_to_Project_Data.dxf")
    s.save(out)
    print("written", out, "| right column bottom y =", round(y, 1))
