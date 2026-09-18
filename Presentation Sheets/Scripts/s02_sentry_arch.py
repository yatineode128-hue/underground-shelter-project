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
EL_X, EL_DATUM = 46.0, 178.0                   # model X 0 ; paper y of 0.000
EL_BREAK = 26000.0                             # the 10 m gap is broken here
EL_SHIFT = -6150.0                             # and the post pulled 6.15 m closer
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
        "THE ROOF PROJECTS 300 ALL ROUND WITH A 300 HIGH PARDI OVER IT. THE "
        "FIRST FLOOR DOES NOT PROJECT; THE FIRST-FLOOR PLAN SHOWS THE ROOF "
        "PROJECTION HIDDEN, AS THE THING OVERHEAD.",
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
s.text("ROOF OVER -  300 PROJECTION WITH 300 HIGH PARDI", G2(2000, 5700),
       SMS, "S-TEXT", "C")
s.text("SPIRAL STAIR 1000 R", G2(-1150, 5400), SMS, "S-TEXT", "C")
s.text("250 DIA CENTRAL POLE", G2(-1150, 4950), SMS, "S-TEXT", "C")
s.view_title(174.0, V12_TTL, "2", "FIRST FLOOR LEVEL",
             "1 : 75   FFL +3.650", RULE_TO)

# =====================================================================  VIEW 3
# SOUTH ELEVATION, 1 : 150.  The shelter at true X, the sentry post and its
# spiral stair at true X across a break, the berm profile and the covered entry
# stairwell roof from section C-C, and the engineered cover called out.
B = D.BOX
H_, A_ = D.HH, D.ASW
GL = 0.0


def prof(pts, layer="A-COVER"):
    s.pline([EL(x, l) for x, l in pts], layer)


def rake(pts, dz=0.0):
    return [(x, l + dz) for x, l in pts]


# --- the ground: flat to the headwall, 1.5:1 up to the berm crest, down again
prof(D.BERM_PROFILE)
for x0, x1 in ((9250.0, 10600.0), (18400.0, 19750.0)):          # the two slopes
    lo, hi = (0.0, 0.900) if x0 == 9250.0 else (0.900, 0.0)
    s.hatch_pat([EL(x0, 0.0), EL(x1, 0.0), EL(x1, hi), EL(x0, lo)],
                "EARTH", 2.2, 0.0, "A-COVER")
s.hatch_pat([EL(10600, 0.0), EL(18400, 0.0), EL(18400, 0.900),
             EL(10600, 0.900)], "EARTH", 2.2, 0.0, "A-COVER")

# --- the engineered cover over the pressure slab: 2000 in six layers, A.7.3
lv, COV = 0.0, []
for th, name in D.COVER_LAYERS:
    COV.append((lv, lv - th / 1000.0, th, name))
    lv -= th / 1000.0
for _, bot, _, _ in COV[:-1]:
    s.line(EL(0, bot), EL(A_["x0"], bot), "A-COVER")
CX, CY = 52.0, 214.0
s.text("ENGINEERED COVER - 2000 IN SIX LAYERS", (CX, CY), SMS, "S-TEXT", "ML")
for k, (top, bot, th, name) in enumerate(COV):
    s.text(f"{th:.0f}  {name}", (CX + 3.0, CY - 3.2 * (k + 1)), SMS,
           "S-TEXT", "ML")
s.pline([(CX + 1.5, CY - 3.2 * len(COV) - 1.6), (CX + 1.5, EL(0, -1.0)[1]),
         EL(4200, -1.0)], "S-NOTE")

# --- the buried box, shown beyond the ground line
for lvl0, lvl1 in ((D.L_FORMATION, D.L_MAT_SOF), (D.L_MAT_SOF, D.L_FLOOR),
                   (D.L_ROOF_SOF, D.L_SLAB_TOP)):
    s.rect(*EL(B["x0"], lvl0), *EL(B["x1"], lvl1), "A-OVER")
for x0, x1 in ((B["x0"], D.INTR["x0"]), (D.INTR["x1"], B["x1"])):
    s.rect(*EL(x0, D.L_FLOOR), *EL(x1, D.L_ROOF_SOF), "A-OVER")
for x0, x1 in ((D.IW[1][1], D.IW[1][2]), (D.IW[2][1], D.IW[2][2])):
    s.dline(EL(x0, D.L_FLOOR), EL(x0, D.L_ROOF_SOF), "A-OVER", 1.4, 1.0)
    s.dline(EL(x1, D.L_FLOOR), EL(x1, D.L_ROOF_SOF), "A-OVER", 1.4, 1.0)
s.dline(EL(B["x0"], D.L_FLOOR), EL(B["x1"], D.L_FLOOR), "A-OVER", 1.6, 1.1)
s.text("BURIED BOX  22000 x 6200 EXTERNAL,  EIGHT BAYS", EL(7000, -4.30), SMS,
       "S-TEXT", "C")
s.text("900 PRESSURE SLAB", EL(5000, -2.48), SMS, "S-TEXT", "C")
s.text("600 MAT ON 100 PCC", EL(11000, -6.42), SMS, "S-TEXT", "C")
s.text("W6", EL(15000, -5.30), SMS, "S-TEXT", "C", rot=90.0)
s.text("W7", EL(18200, -5.30), SMS, "S-TEXT", "C", rot=90.0)

# --- the headhouse: entirely under the berm crest, so shown beyond
for a, b in (((H_["x0"], D.L_SLAB_TOP), (H_["x1"], D.L_SLAB_TOP)),
             ((H_["x0"], D.L_HH_TOP), (H_["x1"], D.L_HH_TOP)),
             ((H_["x0"], D.L_SLAB_TOP), (H_["x0"], D.L_HH_TOP)),
             ((H_["x1"], D.L_SLAB_TOP), (H_["x1"], D.L_HH_TOP)),
             ((H_["x0"], D.L_HH_SOF), (H_["x1"], D.L_HH_SOF))):
    s.dline(EL(*a), EL(*b), "A-OVER", 1.6, 1.1)
s.text("HEADHOUSE BEYOND  -  ROOF +0.900, NO EARTH COVER", EL(16000, -1.35),
       SMS, "S-TEXT", "C")

# --- the covered entry stairwell: the roof and the headwall stand proud
TOPS = rake(D.ASW_SOFFIT, D.ASW_ROOF_T / 1000.0)
XB = 11000.0 + (TOPS[1][1] - 0.900) * (14300.0 - 11000.0) / \
     (TOPS[1][1] - TOPS[2][1])                 # where the roof meets the crest
s.pline([EL(A_["x0"], GL)] + [EL(x, l) for x, l in TOPS[:2]] +
        [EL(XB, 0.900)], "A-WALL")
SB = D.ASW_SOFFIT[1][1] - (D.ASW_SOFFIT[1][1] - D.ASW_SOFFIT[2][1]) * \
     (XB - 11000.0) / (14300.0 - 11000.0)          # soffit level at the crest
s.pline([EL(A_["ix0"], D.ASW_SOFFIT[0][1]),
         EL(D.ASW_SOFFIT[1][0], D.ASW_SOFFIT[1][1]), EL(XB, SB)], "A-WALL")
s.dline(EL(XB, SB), EL(14300.0, D.ASW_SOFFIT[2][1]), "A-OVER", 1.6, 1.1)
s.dline(EL(14300.0, D.ASW_SOFFIT[2][1]), EL(15800.0, D.ASW_SOFFIT[3][1]),
        "A-OVER", 1.6, 1.1)
s.dline(EL(XB, 0.900), EL(14300.0, TOPS[2][1]), "A-OVER", 1.6, 1.1)
s.dline(EL(14300.0, TOPS[2][1]), EL(15800.0, TOPS[3][1]), "A-OVER", 1.6, 1.1)
s.line(EL(A_["x0"], GL), EL(A_["ix0"], GL), "A-WALL")
s.text("COVERED ENTRY STAIRWELL  -  250 RC ROOF,", EL(13800, 4.30), SMS,
       "S-TEXT", "C")
s.text("SOFFIT FOLLOWS THE FLIGHT AT 2200 CLEAR", EL(13800, 3.85), SMS,
       "S-TEXT", "C")
s.text("HEADWALL AND ROOF STAND PROUD OF THE BERM", EL(13800, 3.40), SMS,
       "S-TEXT", "C")

# --- the two escape shaft heads
for name, cx, cy, head in D.ESC:
    s.rect(*EL(cx - D.ESC_COLLAR_OD / 2.0, GL),
           *EL(cx + D.ESC_COLLAR_OD / 2.0, head), "A-OPEN")
    s.dline(EL(cx - D.ESC_CLEAR_D / 2.0, GL),
            EL(cx - D.ESC_CLEAR_D / 2.0, head), "A-OPEN", 1.2, 0.9)
    s.dline(EL(cx + D.ESC_CLEAR_D / 2.0, GL),
            EL(cx + D.ESC_CLEAR_D / 2.0, head), "A-OPEN", 1.2, 0.9)
s.text("ESC 1  HEAD +0.150", EL(2050, 0.75), SMS, "S-TEXT", "C")
s.text("ESC 2  HEAD +0.700", EL(19900, 2.10), SMS, "S-TEXT", "C")

# --- the break in the 10 m gap
for bx in (23025.0, 29625.0):
    s.dline(EL(bx, -7.300), EL(bx, 7.500), "S-CENTER", 2.2, 1.5)
s.text("BREAK", EL(23025.0, -4.700), SMS, "S-TEXT", "C", rot=90.0)

# --- the sentry post, at true X across the break, as A-301 draws it
SP = D.SP_SITE
X0, X1 = SP["x0"], SP["x1"]
PJ = D.SP_ROOF_PROJECTION
s.line(EL(X0 - 2400, GL), EL(X1 + 900, GL), "A-COVER")
for gx in (D.SP_GRID_A, D.SP_GRID_B):                      # F1 footings, buried
    s.dline(EL(X0 + gx - D.SP_FTG_L / 2, D.SP_L_FOUND),
            EL(X0 + gx + D.SP_FTG_L / 2, D.SP_L_FOUND), "A-OVER", 1.4, 1.0)
    s.dline(EL(X0 + gx - D.SP_FTG_L / 2, D.SP_L_FOUND + D.SP_FTG_T / 1000.0),
            EL(X0 + gx + D.SP_FTG_L / 2, D.SP_L_FOUND + D.SP_FTG_T / 1000.0),
            "A-OVER", 1.4, 1.0)
    for dx in (-D.SP_FTG_L / 2, D.SP_FTG_L / 2):
        s.dline(EL(X0 + gx + dx, D.SP_L_FOUND),
                EL(X0 + gx + dx, D.SP_L_FOUND + D.SP_FTG_T / 1000.0),
                "A-OVER", 1.4, 1.0)
    s.dline(EL(X0 + gx, D.SP_L_FOUND + D.SP_FTG_T / 1000.0), EL(X0 + gx, GL),
            "A-OVER", 1.4, 1.0)
s.rect(*EL(X0 - D.SP_PLINTH_PROJ, GL),
       *EL(X1 + D.SP_PLINTH_PROJ, D.SP_L_PLINTH), "A-WALL")   # plinth
s.rect(*EL(X0, D.SP_L_PLINTH), *EL(X1, D.SP_ROOF_SOFFIT), "A-WALL")
s.line(EL(X0, D.SP_L_FF), EL(X1, D.SP_L_FF), "A-WALL")
s.rect(*EL(X0 - PJ, D.SP_ROOF_SOFFIT), *EL(X1 + PJ, D.SP_L_ROOF), "A-WALL")
s.rect(*EL(X0 - PJ, D.SP_L_ROOF),
       *EL(X1 + PJ, D.SP_L_ROOF + D.SP_PARDI_H / 1000.0), "A-WALL")
for x0, y0, x1, y1 in D.SP_PANELS_FF:                      # the SOUTH face only
    if y0 == 0.0:
        s.rect(*EL(X0 + x0, D.SP_PANEL_SILL),
               *EL(X0 + x1, D.SP_PANEL_HEAD), "A-OPEN")
for c0, c1 in D.SP_FRAME_COLS:                             # the RC frame behind
    s.dline(EL(X0 + c0, D.SP_L_PLINTH), EL(X0 + c0, D.SP_L_ROOF),
            "A-OVER", 1.4, 1.0)
    s.dline(EL(X0 + c1, D.SP_L_PLINTH), EL(X0 + c1, D.SP_L_ROOF),
            "A-OVER", 1.4, 1.0)
FS0, FS1 = D.SP_FRAME_SPAN
for b0, b1 in D.SP_FRAME_BEAMS + [D.SP_FRAME_PLINTH]:
    for lv in (b0, b1):
        s.dline(EL(X0 + FS0, lv), EL(X0 + FS1, lv), "A-OVER", 1.4, 1.0)
ST_ = D.SP_STAIR_EL                                        # the spiral stair
SCX = (ST_["x0"] + ST_["x1"]) / 2.0                        # the pole centre
SR = (ST_["x1"] - ST_["x0"]) / 2.0                         # 1000 R
for px in ST_["pole"]:
    s.line(EL(X0 + px, GL), EL(X0 + px, ST_["top"]), "A-WALL-IN")
for k in range(1, ST_["risers"] + 1):
    lv = D.SP_L_PLINTH + k * ST_["rise"] / 1000.0          # the tread tip runs
    tip = SCX + SR * math.sin(math.radians(k * 30.0))      # round the pole
    if abs(tip - SCX) < 1.0:                               # edge-on, no line
        continue
    s.line(EL(X0 + SCX, lv), EL(X0 + tip, lv), "A-WALL-IN")
s.text("SENTRY POST", EL(X0 + 2000, 4.15), SMS, "S-TEXT", "C")
s.text("SENTRY POST: RC FRAME DASHED BEHIND THE 190 BRICK INFILL",
       (130.0, 221.0), SMS, "S-TEXT", "ML")
s.text("300 ROOF PROJECTION WITH A 300 HIGH PARDI OVER IT",
       (130.0, 217.5), SMS, "S-TEXT", "ML")
s.text("SPIRAL STAIR 1000 R", EL(X0 - 150, 5.30), SMS, "S-TEXT", "R")
s.text("250 DIA CENTRAL POLE", EL(X0 - 150, 4.85), SMS, "S-TEXT", "R")

# --- the levels.  Short labels: the LEVEL SCHEDULE carries the descriptions.
LEVELS_EL = [
    (D.SP_L_PARAPET, "+7.000  PARDI", 1.8),
    (D.SP_L_ROOF, "+6.700  ROOF", -1.8),
    (D.SP_L_FF, "+3.650  1ST FLOOR", 0.0),
    (D.L_ASW_HEAD, "+2.450  ASW HEAD", 0.0),
    (D.L_HH_TOP, "+0.900  BERM TOP", 1.4),
    (D.SP_L_PLINTH, "+0.450  POST FFL", -1.4),
    (0.0, "0.000  GRADE", -3.6),
    (D.L_SLAB_TOP, "(-)2.000  SLAB TOP", 0.0),
    (D.L_ROOF_SOF, "(-)2.900  ROOF SOFFIT", 0.0),
    (D.L_FLOOR, "(-)6.100  FLOOR", 1.4),
    (D.L_MAT_SOF, "(-)6.700  MAT SOFFIT", -1.4),
]
LX = 250.0
for lvl, lab, dy in LEVELS_EL:
    ly = EL(0, lvl)[1]
    s.line(EL(X1 + PJ if lvl > 0.0 else 22800.0, lvl), (LX, ly), "S-LEVEL")
    s.msp.add_blockref("A2-LEVEL", (LX, ly), dxfattribs={"layer": "S-LEVEL"})
    s.text(lab, (LX + 2.6, ly + 2.4 + dy), SMS, "S-LEVEL", "ML")
s.text("(-)6.800  FORMATION", EL(600, -6.40), SMS, "S-TEXT", "ML")
s.text("F1 FOUNDING LEVEL  (-)2.000", EL(X0 + 1200, -2.60), SMS,
       "S-TEXT", "C")
s.dim_v(EL(X0, D.SP_L_PLINTH), EL(X0, D.SP_L_FF), EL(X0 + 700, 0)[0], SC_EL,
        "A2-DIM-S")
s.dim_v(EL(X0, D.SP_L_FF), EL(X0, D.SP_L_ROOF), EL(X0 + 700, 0)[0], SC_EL,
        "A2-DIM-S")
s.view_title(44.0, V3_TTL, "3", "SOUTH ELEVATION - SHELTER AND SENTRY POST",
             "1 : 150   THE BURIED STRUCTURE IS SHOWN BEYOND THE GROUND LINE",
             RULE_TO)

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
    ["ROOF PROJECTION", "300 WIDE", "ALL ROUND, AT ROOF LEVEL", "-",
     "300 HIGH PARDI (PARAPET) 300 x 150 OVER IT"],
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
