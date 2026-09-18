"""
s02_sentry_arch.py  --  ARCH002  SENTRY POST: GROUND FLOOR LEVEL, FIRST FLOOR
                        LEVEL PLAN AND SOUTH ELEVATION

A REDRAW of sheet 2 of the owner's Revit A2 set: the same views, in the same
frame and title block, with the plan sizes and every level brought to the
project's own authoritative data (master A.4.3, A.4.8 and the SP-B1 / SP-B2
rulings).

    1  GROUND FLOOR LEVEL                                          1 :  50
    2  FIRST FLOOR LEVEL                                           1 :  50
    3  SOUTH ELEVATION - SHELTER AND SENTRY POST                   1 : 125
    4  LINTEL L1, WALL TIES AND THE 200 INFILL ZONE                1 :  20

The elevation is the view the owner's set uses to carry the levels, so it is the
view that carries the corrections: the sentry post ground floor is +0.450 and
not 440, the entry stairwell roof head is +2.450 and not 3400, the post roof
slab and its parapet are two different levels (+6.700 and +7.000), and (-)6.100
is the internal floor and top of mat, not the foundation level.  The sentry post
is drawn at its TRUE relative X, X 32000 - 36000, with the 10 m gap broken.

Every corrected figure is registered in arch_data.CORRECTIONS and in master
Part H.  By instruction the sheet itself carries no revision or amendment text.

COLOUR: dark only, and mostly black - ACI 7, 8, 1, 5.
"""
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
RULE_TO, RULE_MID = 272.0, 140.0
SM, SMS = 1.9, 1.75

SC_PL = 50.0                                   # views 1 and 2
G1 = vw(SC_PL, 64.0, 276.0)                    # ground floor, model (0,0)
G2 = vw(SC_PL, 176.0, 276.0)                   # first floor
V12_TTL = 248.0

SC_EL = 150.0                                  # view 3
EL_X, EL_DATUM = 48.0, 160.0                   # model X 0 ; paper y of 0.000
EL_BREAK = 26000.0                             # the 10 m gap is broken here
EL_SHIFT = -9000.0                             # and the post pulled 9 m closer
V3_TTL = 102.0

SC_DT = 20.0                                   # view 4
DT = vw(SC_DT, 58.0, 52.0)
DT_H = 750.0                                   # height of the part elevation
V4_TTL = 40.0

EX, EY = D.SP_EXT_X, D.SP_EXT_Y                # 4000 x 5000
IZ = D.SP_INFILL                               # 200 structural infill zone
GA, GB, G_1, G_2 = D.SP_GRID_A, D.SP_GRID_B, D.SP_GRID_1, D.SP_GRID_2
CO = D.SP_COL                                  # 350
H = CO / 2.0


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


def floor_plan(P, first):
    """The frame, the infill zone and the openings, at one level."""
    s.rect(*P(0, 0), *P(EX, EY), "A-WALL")
    s.rect(*P(IZ, IZ), *P(EX - IZ, EY - IZ), "A-WALL")
    s.hatch_pat([P(0, 0), P(EX, 0), P(EX, EY), P(0, EY)], "ANSI31", 1.1, 0.0,
                "S-HATCH",
                holes=[[P(IZ, IZ), P(EX - IZ, IZ), P(EX - IZ, EY - IZ),
                        P(IZ, EY - IZ)]])
    for gx in (GA, GB):                                    # columns C1
        for gy in (G_1, G_2):
            s.conc_hatch([P(gx - H, gy - H), P(gx + H, gy - H),
                          P(gx + H, gy + H), P(gx - H, gy + H)], scale=0.5)
            s.rect(*P(gx - H, gy - H), *P(gx + H, gy + H), "A-WALL")
    for gx in (GA, GB):                                    # grid lines
        s.cline(P(gx, -400), P(gx, EY + 200), "S-CENTER")
    for gy in (G_1, G_2):
        s.cline(P(-580, gy), P(EX + 400, gy), "S-CENTER")
    for gx, lab in ((GA, "A"), (GB, "B")):
        s.circle(P(gx, EY + 300), 3.4 / 2.0, "S-GRID")
        s.text(lab, P(gx, EY + 300), SMS, "S-GRID", "C")
    for gy, lab in ((G_1, "1"), (G_2, "2")):
        s.circle(P(-700, gy), 3.4 / 2.0, "S-GRID")
        s.text(lab, P(-700, gy), SMS, "S-GRID", "C")

    # door D1, in the south face, and the openings
    s.line(P(IZ, 0), P(1100, 0), "A-WALL")
    s.line(P(1100 + D.SP_DOOR_W, 0), P(EX - IZ, 0), "A-WALL")
    s.arc(P(1100, 0), D.SP_DOOR_W / SC_PL, 0, 90, "A-OPEN")
    s.text("D1", P(1550, 470), SMS, "S-TEXT", "C")
    if first:
        for gy0, gy1 in ((900, 2100), (2900, 4100)):       # vision panels, E/W
            for gx in (0, EX - IZ):
                s.rect(*P(gx, gy0), *P(gx + IZ, gy1), "A-OPEN")
        for gx0, gx1 in ((1200, 2400),):                   # north face
            s.rect(*P(gx0, EY - IZ), *P(gx1, EY), "A-OPEN")
        s.text("W1 TYP", P(EX - 620, 1500), SMS, "S-TEXT", "C", rot=90.0)
        s.rect(*P(GA - 125, G_1 + H), *P(GA + 125, G_2 - H), "A-OVER")
    else:
        s.rect(*P(EX - IZ, 1600), *P(EX, 2800), "A-OPEN")   # W1 ground, east
        s.text("W1", P(EX - 620, 2200), SMS, "S-TEXT", "C", rot=90.0)
    # external spiral stair, 1000 R with a 250 dia central pole
    s.circle(P(-350, 1600), D.SP_SPIRAL_R / SC_PL, "A-WALL-IN")
    s.circle(P(-350, 1600), D.SP_SPIRAL_POLE / 2.0 / SC_PL, "A-WALL")
    for k in range(9):
        a = -70.0 + k * 22.0
        import math
        s.line(P(-350, 1600),
               P(-350 + D.SP_SPIRAL_R * math.cos(math.radians(a)),
                 1600 + D.SP_SPIRAL_R * math.sin(math.radians(a))),
               "A-WALL-IN")
    s.dim_chain_h([P(v, 0)[0] for v in (0, IZ, EX - IZ, EX)], P(0, 0)[1],
                  P(0, -800)[1], SC_PL, "A2-DIM-S")
    s.dim_v(P(EX, 0), P(EX, EY), P(EX + 700, 0)[0], SC_PL, "A2-DIM-S")


# =====================================================================  VIEW 1
floor_plan(G1, first=False)
s.text("+0.450", G1(EX / 2.0, 2500), SM, "S-TEXT", "C")
s.text("SPIRAL", G1(-350, 400), SMS, "S-TEXT", "C")
s.text("STAIR", G1(-350, 60), SMS, "S-TEXT", "C")
s.view_title(52.0, V12_TTL, "1", "GROUND FLOOR LEVEL",
             "1 : 50   FFL +0.450", RULE_MID)

# =====================================================================  VIEW 2
floor_plan(G2, first=True)
s.text("+3.650", G2(EX / 2.0, 2500), SM, "S-TEXT", "C")
s.text("SPIRAL", G2(-350, 400), SMS, "S-TEXT", "C")
s.text("STAIR", G2(-350, 60), SMS, "S-TEXT", "C")
s.view_title(164.0, V12_TTL, "2", "FIRST FLOOR LEVEL",
             "1 : 50   FFL +3.650", RULE_TO)

# =====================================================================  VIEW 3
# SOUTH ELEVATION, 1 : 125.  The shelter at true X, the post at true X across a
# break, and every level as master A.4.3.
B = D.BOX
s.hatch_pat([EL(-800, D.L_SLAB_TOP), EL(22800, D.L_SLAB_TOP),
             EL(22800, 0.0), EL(-800, 0.0)], "EARTH", 1.2, 0.0, "A-COVER")
s.line(EL(-800, 0.0), EL(22800, 0.0), "A-COVER")
s.line(EL(31000, 0.0), EL(37000, 0.0), "A-COVER")

# the buried box, in elevation behind the ground line
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
s.line(EL(SP["x0"], D.SP_L_ROOF), EL(SP["x0"], D.SP_L_PARAPET), "A-WALL")
for gx in (SP["x0"] + 1200, SP["x0"] + 2800):
    s.rect(*EL(gx - 600, D.SP_L_FF + 0.700),
           *EL(gx + 600, D.SP_L_FF + 1.900), "A-OPEN")
s.rect(*EL(SP["x0"] + 1100, D.SP_L_PLINTH),
       *EL(SP["x0"] + 2000, D.SP_L_PLINTH + 2.100), "A-OPEN")
s.text("SENTRY POST", EL(SP["x0"] + 2000, 3.90), SMS, "S-TEXT", "C")

# the break in the 10 m gap.  22275 is unshifted and 31725 is shifted, so the
# two lines land either side of the paper gap between the box and the post.
for bx in (22275.0, 31725.0):
    s.dline(EL(bx, -7.400), EL(bx, 7.600), "S-CENTER", 2.2, 1.5)
s.text("BREAK", EL(22500.0, -6.400), SMS, "S-TEXT", "C", rot=90.0)

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
    (D.L_FLOOR, "(-)6.100  FLOOR / TOP OF MAT", 1.4),
    (D.L_MAT_SOF, "(-)6.700  MAT SOFFIT", -1.4),
]
LX = EL(37500, 0.0)[0]
for lvl, lab, dy in LEVELS_EL:
    ly = EL(0, lvl)[1]
    s.line(EL(31400 if lvl > 0.0 else 22400, lvl), (LX, ly), "S-LEVEL")
    s.msp.add_blockref("A2-LEVEL", (LX, ly), dxfattribs={"layer": "S-LEVEL"})
    s.text(lab, (LX + 2.6, ly + 2.4 + dy), SMS, "S-LEVEL", "ML")
s.text("(-)6.800  FORMATION", EL(1000, -6.35), SMS, "S-TEXT", "ML")
s.text("(-)2.000  POST FOUNDING LEVEL, F1 ON IN-SITU BASALT",
       EL(8000, -6.35), SMS, "S-TEXT", "ML")
s.dim_v(EL(SP["x0"], D.SP_L_PLINTH), EL(SP["x0"], D.SP_L_FF),
        EL(SP["x0"] - 900, 0)[0], SC_EL, "A2-DIM-S")
s.dim_v(EL(SP["x0"], D.SP_L_FF), EL(SP["x0"], D.SP_L_ROOF),
        EL(SP["x0"] - 900, 0)[0], SC_EL, "A2-DIM-S")
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
s.text("190 BRICKWORK IN THE 200 ZONE", DT(800, 690), SMS,
       "S-TEXT", "C")
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
     "GRID A / B x 1 / 2"],
    ["B1  BEAM", "250 x 450", "SPANS A-B, 3650 c/c", "30", "ON GRIDS 1 AND 2"],
    ["B2  BEAM", "250 x 450", "SPANS 1-2, 4650 c/c", "30", "ON GRIDS A AND B"],
    ["S1  SLAB", "150 THK", "3650 x 4650 c/c, TWO-WAY", "30", "BOTH FLOORS"],
    ["PB  PLINTH BEAM", "250 x 400", "AT +0.450", "30", "TOP = GROUND FFL"],
    ["F1  ISOLATED FOOTING", "1500 x 1500 x 600", "4 No.", "50",
     "ON IN-SITU BASALT AT (-)2.000"],
    ["GROUND INFILL", "200 ZONE", "190 BRICKWORK IS 1077, CM 1:6", "-",
     "10 TAKEN UP IN THE INTERNAL PLASTER"],
    ["FIRST STOREY INFILL", "200 ZONE", "ARMOURED VISION PANELS 1200 WIDE",
     "-", "8 No. OPENINGS"],
    ["SPIRAL STAIR", "1000 R", "EXTERNAL", "-", "250 DIA CENTRAL POLE"],
    ["L1  LINTEL", "190 x 150", "OVER ALL 11 OPENINGS", "30",
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
    ["D1", "DOOR", "900 x 2100", "GROUND AND FIRST STOREY", "2 No."],
    ["W1", "ARMOURED VISION PANEL", "1200 WIDE", "GROUND STOREY", "1 No."],
    ["W1", "ARMOURED VISION PANEL", "1200 WIDE", "FIRST STOREY", "8 No."],
    "ELEVEN OPENINGS IN ALL, EVERY ONE WITH A LINTEL L1 OVER IT",
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
         header=["MARK", "TYPE", "SIZE", "STOREY", "No."],
         align=["C", "L", "C", "L", "C"], pad=2.2),
], gap=6.0, rh_max=7.2)
assert y > 35.0, f"the schedule stack overflows the frame: bottom at {y:.1f}"


if __name__ == "__main__":
    out = os.path.join(ROOT, "Presentation Sheets", "DXF",
                       "ARCH002_Sentry_Post_Floor_Plans_and_South_Elevation_"
                       "Redrawn_to_Project_Data.dxf")
    s.save(out)
    print("written", out, "| right column bottom y =", round(y, 1))
