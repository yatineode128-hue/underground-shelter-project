"""
s01_arch_plans.py  --  ARCH001  UNDERGROUND LEVEL PLAN, HEADHOUSE LEVEL PLAN
                       AND GROUND LEVEL PLAN

A REDRAW of sheet 1 of the owner's Revit A2 set, in the same frame and title
block, with every dimension brought to the project's own authoritative data
(master A.3, A.4.2 - A.4.9) AND with every element drawn as the Rev F CAD draws
it - the four Rev F DXFs in `current/cad/` were parsed, not remembered.

    1  UNDERGROUND LEVEL PLAN  (-)6.100                            1 : 100
    2  HEADHOUSE LEVEL PLAN    (-)2.000                            1 : 100
    3  GROUND LEVEL PLAN AND SITE   0.000                          1 : 200

View 3 is at 1 : 200 so that the sentry post can be drawn at its TRUE site
position, X 32000 - 36000, instead of off position beside the box.

WHERE THE Rev F DRAWING AND THE MASTER DISAGREE THE MASTER GOVERNS.  The seven
cases are listed in arch_data.CAD_FINDINGS and in master Part H; by instruction
none of them is printed on the sheet.

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

SC, SC3 = 100.0, 200.0
RCOL, RCOL_W, RTOP = 282.0, 178.0, 383.0
RULE_TO = 272.0
SM, SMS = 1.9, 1.75

PX0, PX3 = 47.0, 60.0
V1_Y0, V1_TTL = 310.0, 282.0                     # model Y 0 at 310;  box 310-372
V2_Y0, V2_TTL = 190.0, 153.0                     # model Y 0 at 192
V3_Y0, V3_TTL = 88.0, 54.0                       # model Y 0 at  88, 1 : 200

P1 = vw(SC, PX0, V1_Y0)
P2 = vw(SC, PX0, V2_Y0)
P3 = vw(SC3, PX3, V3_Y0)


s = A2Sheet(
    sheet_no="SHEET 01",
    drawing_no="ARCH001",
    title_lines=["UNDERGROUND", "LEVEL PLAN,", "HEADHOUSE LEVEL",
                 "PLAN & GROUND", "LEVEL PLAN"],
    project_lines=D.PROJECT_LINES,
    identity=D.IDENTITY,
    notes=[
        "ALL DIMENSIONS ARE IN MM. ALL LEVELS ARE IN METRES RELATIVE TO "
        "FINISHED SITE GRADE 0.000, NEGATIVE DOWNWARDS.",
        "WRITTEN DIM TO BE FOLLOWED ONLY. DRG NOT TO BE SCALED.",
        "THIS DRG IS TO BE READ IN CONJUNCTION WITH ALL RELEVANT ARCH, STR AND "
        "SERVICES DRGS.",
        "THE PROTECTIVE BOUNDARY IS THE 600 PERIMETER WALLS, THE 900 PRESSURE "
        "SLAB, THE 600 MAT AND WALLS W6 AND W7 AT 400 WITH THEIR TWO BLAST "
        "DOORS. THE HEADHOUSE, THE COVERED ENTRY STAIRWELL AND THE SENTRY "
        "POST ARE OUTSIDE IT AND ARE NOT BLAST RATED.",
        "THE FOUR W8 PARTITIONS ARE NON-STRUCTURAL AND CARRY A PERMANENT 900 "
        "GAP AT Y 2500 - 3400. NO DOOR IS SCHEDULED IN THEM.",
        "BLAST DOOR 1 OPENS WEST INTO BAY 6 AND BLAST DOOR 2 OPENS EAST INTO "
        "BAY 8. BOTH ARE HINGED ON THE SOUTH JAMB OF THE 1200 OPENING.",
        "THE DECON AIRLOCK RUNS SOUTH TO NORTH: STAGE 1 AT BLAST DOOR 1, "
        "STAGE 3 AT THE W5 GAS-TIGHT FIRE DOOR INTO THE CBRN PLANT BAY. THE "
        "TWO INTERNAL PARTITIONS ARE 110 THICK WITH AN 800 DOOR IN EACH.",
        "MAIN STAIRCASE: 24 RISERS AT 170.8333, TREAD 280, 3 FLIGHTS OF 8, "
        "TOTAL RISE 4100, FLIGHT WIDTH 1200, WELL 200, HEADROOM 2533.",
        "THE ENGINEERED COVER OVER THE PRESSURE SLAB IS 2000 THICK IN SIX "
        "LAYERS AND IS GRADED TO SHED AT GRADE. THERE IS NO ROOF OUTLET.",
        "THE BERM IS GRADED 1.5:1 TO +0.900 WITH A 1350 TOE RUN, AND FALLS "
        "FROM +0.900 TO GRADE OVER THE LAST 1350 SO THE ENTRY DOOR IS CLEAR "
        "AT 0.000.",
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
    ("A-WALL",    7, 35, "Walls, cut"),
    ("A-WALL-IN", 7, 18, "Internal and non-structural walls"),
    ("A-OVER",    8, 18, "Over or below the cut plane"),
    ("A-OPEN",    1, 35, "Doors, openings and shafts through the boundary"),
    ("A-EQUIP",   5, 25, "Fixed equipment and services"),
    ("A-COVER",   8, 18, "Engineered cover, berm and fill"),
]:
    _ly = s.doc.layers.add(_nm)
    _ly.color, _ly.lineweight, _ly.description = _col, _lw, _desc


def swing(P, cx, cy, r, a0, a1, sc, layer="A-OPEN"):
    """A door exactly as the Rev F CAD draws one: the two extreme radii - the
    leaf shown open and the face of the opening - and the swing arc between."""
    s.arc(P(cx, cy), r / sc, a0, a1, layer)
    for a in (a0, a1):
        s.line(P(cx, cy), P(cx + r * math.cos(math.radians(a)),
                            cy + r * math.sin(math.radians(a))), layer)


def arrow(P, p0, p1, sc, layer="A-WALL-IN", head=180.0):
    """A direction-of-travel arrow, head at p1."""
    s.line(P(*p0), P(*p1), layer)
    ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    for d in (+0.42, -0.42):
        s.line(P(*p1), P(p1[0] - head * math.cos(ang + d) * 1.15,
                         p1[1] - head * math.sin(ang + d) * 1.15), layer)


def dashed_rect(P, x0, y0, x1, y1, layer="A-OVER", dash=1.8, gap=1.3):
    for a, b in (((x0, y0), (x1, y0)), ((x1, y0), (x1, y1)),
                 ((x1, y1), (x0, y1)), ((x0, y1), (x0, y0))):
        s.dline(P(*a), P(*b), layer, dash, gap)


# =====================================================================  VIEW 1
# UNDERGROUND LEVEL PLAN, (-)6.100, 1 : 100
B, I = D.BOX, D.INTR
s.rect(*P1(B["x0"], B["y0"]), *P1(B["x1"], B["y1"]), "A-WALL")
s.rect(*P1(I["x0"], I["y0"]), *P1(I["x1"], I["y1"]), "A-WALL")

# the four W8 partitions.  PERMANENT 900 GAP, NO DOOR  (MEP3-F1)
for x0, x1 in D.PARTITIONS:
    for y0, y1 in ((I["y0"], D.W8_GAP[0]), (D.W8_GAP[1], I["y1"])):
        s.rect(*P1(x0, y0), *P1(x1, y1), "A-WALL-IN")

# W5 200, in two pieces, with the ruled 900 gas-tight fire door D-05
for x0, y0, x1, y1 in D.W5_SEGMENTS:
    s.rect(*P1(x0, y0), *P1(x1, y1), "A-WALL-IN")
swing(P1, *D.W5_SWING, SC)
s.text("D-05", P1(12180, 4850), SMS, "S-TEXT", "C")

# W6 and W7 400, each starting above its 1200 blast-door opening
BD = D.BLAST_DOOR
for mark, x0, x1, t in D.IW[1:]:
    s.rect(*P1(x0, D.W6_W7_BASE), *P1(x1, I["y1"]), "A-WALL")
swing(P1, *D.BD1_SWING, SC)
swing(P1, *D.BD2_SWING, SC)
s.text("BD1", P1(14200, 1000), SMS, "S-TEXT", "C")
s.text("BD2", P1(19000, 1000), SMS, "S-TEXT", "C")

# bay 6, the three-stage decon airlock
for y0, y1 in D.DECON_PARTITIONS:
    for x0, x1 in D.DECON_SEGMENTS:
        s.rect(*P1(x0, y0), *P1(x1, y1), "A-WALL-IN")
for sw in D.DECON_SWINGS:
    swing(P1, *sw, SC)
for lab, y in D.DECON_STAGE_LABELS:
    s.text(lab, P1(13450 if lab == "STAGE 1" else 13800,
                   2100 if lab == "STAGE 1" else y), SMS, "S-TEXT", "C")
s.text("DECON AIRLOCK", P1(14450, 2800), SMS, "S-TEXT", "C", rot=90.0)

# the two escape shafts
for name, cx, cy, head in D.ESC:
    s.circle(P1(cx, cy), D.ESC_CLEAR_D / 2.0 / SC, "A-OPEN")
    s.circle(P1(cx, cy), D.ESC_COLLAR_OD / 2.0 / SC, "A-WALL")
    s.cline(P1(cx - 1500, cy), P1(cx + 1500, cy), "S-CENTER")
    s.cline(P1(cx, cy - 1500), P1(cx, cy + 1500), "S-CENTER")
    s.text(f"{name}  1400 DIA", P1(cx, cy + 1550), SMS, "S-TEXT", "C")
    s.text("COLLAR 250 OVER", P1(cx, cy + 1150), SMS, "S-TEXT", "C")

# bay 7, the stair shaft.  FROZEN geometry, as the Rev F plan draws it
V, PA, ST = D.VOID, D.PAD, D.STAIR
s.dline(P1(V["x0"], V["y1"]), P1(V["x1"], V["y1"]), "A-OVER")
s.rect(*P1(D.ARRIVAL[0], D.ARRIVAL[1]), *P1(D.ARRIVAL[2], D.ARRIVAL[3]),
       "A-WALL-IN")
s.rect(*P1(D.LANDING_L1[0], D.LANDING_L1[1]),
       *P1(D.LANDING_L1[2], D.LANDING_L1[3]), "A-WALL-IN")
for fx0, fx1 in (ST["fltA"], ST["fltB"]):
    s.rect(*P1(fx0, D.FLIGHT_Y[0]), *P1(fx1, D.FLIGHT_Y[1]), "A-WALL-IN")
    for y in D.FLIGHT_RISERS:
        s.line(P1(fx0, y), P1(fx1, y), "A-WALL-IN")
arrow(P1, *D.UP_ARROW, SC)
s.text("FLIGHTS 1 + 3 UP", P1(15150, 2780), SMS, "S-TEXT", "C", rot=90.0)
s.text("FLIGHT 2", P1(18130, 2780), SMS, "S-TEXT", "C", rot=90.0)
s.text("ARRIVAL  (-)6.100", P1(16600, 1000), SMS, "S-TEXT", "C")
s.text("LANDING L1  (-)4.733", P1(16600, 4350), SMS, "S-TEXT", "C")

SR = D.SUMP_RECT                                       # SU-01, below floor
dashed_rect(P1, *SR, "A-OVER", 1.2, 0.9)
s.rect(*P1(11398, 5600), *P1(12198, 6200), "A-EQUIP")  # service entry plate

# bay numbers and room names, verbatim from the Rev F plan
for bx, lab in D.BAY_BUBBLES:
    s.circle(P1(bx, D.BAY_BUBBLE_Y), D.BAY_BUBBLE_R / SC, "S-GRID")
    s.text(lab, P1(bx, D.BAY_BUBBLE_Y), SM, "S-GRID", "C")
for rx, ry, rot, nm in D.ROOM_NAMES:
    s.text(nm, P1(rx, ry), SM, "S-TEXT", "C", rot=rot)
for mark, x0, x1, t in D.IW:
    s.text(f"{t:.0f}", P1((x0 + x1) / 2.0, 250), SMS, "S-TEXT", "C", rot=90.0)
s.text("600", P1(300, 3100), SMS, "S-TEXT", "C", rot=90.0)
s.text("600", P1(21700, 3100), SMS, "S-TEXT", "C", rot=90.0)
s.text("110 TYP", P1(3555, 4500), SMS, "S-TEXT", "C", rot=90.0)

s.secmark(P1(-500, 2050), "A", "R")
s.secmark(P1(22500, 2050), "A", "L")
s.cline(P1(-200, 2050), P1(22200, 2050), "S-CENTER")
s.north((55.0, 374.0))

s.dim_chain_h([P1(v, 0)[0] for v in D.BAY_CHAIN], V1_Y0, 305.0, SC, "A2-DIM-S")
s.dim_h(P1(600, 0), P1(21400, 0), 299.0, SC, "A2-DIM-S")
s.dim_h(P1(0, 0), P1(22000, 0), 293.0, SC, "A2-DIM-S")
s.dim_v(P1(0, 0), P1(0, 6200), 42.5, SC, "A2-DIM-S")
s.dim_chain_v([P1(0, v)[1] for v in (600, 2500, 3400, 5600)],
              P1(22000, 0)[0], P1(23200, 0)[0], SC, "A2-DIM-S")
s.view_title(PX0 - 4.0, V1_TTL, "1", "UNDERGROUND LEVEL PLAN   (-)6.100",
             "1 : 100   EIGHT BAYS, 22000 x 6200 EXTERNAL", RULE_TO)

# =====================================================================  VIEW 2
# HEADHOUSE LEVEL PLAN, (-)2.000, 1 : 100 - the top of the 900 pressure slab
H, A = D.HH, D.ASW
DJ0, DJ1 = D.HH_DOOR_OPENING                     # the D1 opening through HW2
EJ0, EJ1 = D.ENTRY_DOOR_OPENING                  # the D2 opening in the headwall
dashed_rect(P2, B["x0"], B["y0"], B["x1"], B["y1"], "A-OVER")

# the headhouse, with the north wall broken for door D1 on both faces
for y in (H["y0"], H["iy0"]):
    s.line(P2(H["x0"] if y == H["y0"] else H["ix0"], y),
           P2(H["x1"] if y == H["y0"] else H["ix1"], y), "A-WALL")
for x in (H["x0"], H["x1"]):
    s.line(P2(x, H["y0"]), P2(x, H["y1"]), "A-WALL")
for x in (H["ix0"], H["ix1"]):
    s.line(P2(x, H["iy0"]), P2(x, H["iy1"]), "A-WALL")
s.line(P2(H["x0"], H["y1"]), P2(DJ0, H["y1"]), "A-WALL")
s.line(P2(DJ1, H["y1"]), P2(H["x1"], H["y1"]), "A-WALL")
s.line(P2(H["ix0"], H["iy1"]), P2(DJ0, H["iy1"]), "A-WALL")
s.line(P2(DJ1, H["iy1"]), P2(H["ix1"], H["iy1"]), "A-WALL")

# the covered entry stairwell, with the west headwall broken for door D2
s.line(P2(A["x0"], A["y1"]), P2(A["x1"], A["y1"]), "A-WALL")
for x0, x1 in ((A["x0"], DJ0), (DJ1, A["x1"])):       # broken at door D1
    s.line(P2(x0, A["y0"]), P2(x1, A["y0"]), "A-WALL")
s.line(P2(A["ix0"], A["iy1"]), P2(A["ix1"], A["iy1"]), "A-WALL")
for x0, x1 in ((A["ix0"], DJ0), (DJ1, A["ix1"])):     # broken at door D1
    s.line(P2(x0, A["iy0"]), P2(x1, A["iy0"]), "A-WALL")
s.line(P2(A["x1"], A["y0"]), P2(A["x1"], A["y1"]), "A-WALL")
s.line(P2(A["ix1"], A["iy0"]), P2(A["ix1"], A["iy1"]), "A-WALL")
for x in (A["x0"], A["ix0"]):
    s.line(P2(x, A["y0"] if x == A["x0"] else A["iy0"]), P2(x, EJ0), "A-WALL")
    s.line(P2(x, EJ1), P2(x, A["y1"] if x == A["x0"] else A["iy1"]), "A-WALL")

# the opening in the pressure slab, and the slab restored beyond it
s.rect(*P2(V["x0"], V["y0"]), *P2(V["x1"], V["y1"]), "A-OPEN")
s.rect(*P2(PA["x0"], PA["y0"]), *P2(PA["x1"], PA["y1"]), "A-OVER")
s.rect(*P2(ST["fltA"][0], D.FLIGHT_Y[0]), *P2(ST["fltA"][1], D.FLIGHT_Y[1]),
       "A-WALL-IN")
for y in D.FLIGHT_RISERS:
    s.line(P2(ST["fltA"][0], y), P2(ST["fltA"][1], y), "A-WALL-IN")
arrow(P2, *D.UP_ARROW_HH, SC)
dashed_rect(P2, *D.FLIGHT2_BELOW, "A-OVER", 1.2, 0.9)
dashed_rect(P2, *D.L2_BELOW, "A-OVER", 1.2, 0.9)

# the headhouse door: hinged on the OUTER face, opening NORTH  (MEP3-F4)
for x in (DJ0, DJ1):
    s.line(P2(x, H["iy1"]), P2(x, H["y1"]), "A-OPEN")
swing(P2, *D.HH_DOOR_SWING, SC)

# the approach steps, the top landing and the platform
s.rect(*P2(A["top_landing"][0], A["iy0"]), *P2(A["top_landing"][1], A["iy1"]),
       "A-WALL-IN")
s.rect(*P2(A["flight"][0], A["iy0"]), *P2(A["flight"][1], A["iy1"]),
       "A-WALL-IN")
for x in D.APPROACH_RISERS:
    s.line(P2(x, A["iy0"]), P2(x, A["iy1"]), "A-WALL-IN")
s.rect(*P2(A["platform"][0], A["iy0"]), *P2(A["platform"][1], A["iy1"]),
       "A-WALL-IN")

# the entry door: hinged on the OUTER face of the headwall, opening WEST
for yy in (EJ0, EJ1):
    s.line(P2(A["x0"], yy), P2(A["ix0"], yy), "A-OPEN")
swing(P2, *D.ENTRY_DOOR_SWING, SC)
s.rect(*P2(A["channel"][0], A["iy0"]), *P2(A["channel"][1], A["iy1"]),
       "A-EQUIP")

for name, cx, cy, head in D.ESC:
    s.circle(P2(cx, cy), D.ESC_CLEAR_D / 2.0 / SC, "A-OPEN")
    s.circle(P2(cx, cy), D.ESC_COLLAR_OD / 2.0 / SC, "A-WALL")
    s.text(name, P2(cx, cy - 1450), SMS, "S-TEXT", "C")
s.text("OPENING IN THE PRESSURE SLAB  2800 x 3160", P2(11000, 2700), SMS,
       "S-TEXT", "C")
s.text("FLIGHT 3 UP", P2(15900, 4350), SMS, "S-TEXT", "C")
s.text("LANDING L2 BELOW  (-)3.367", P2(16600, 1150), SMS, "S-TEXT", "C")
s.text("HEADHOUSE FLOOR  (-)2.000  =  TOP OF THE PRESSURE SLAB",
       P2(11000, 4900), SMS, "S-TEXT", "C")
s.text("11.15 m2 USABLE", P2(11000, 4450), SMS, "S-TEXT", "C")
s.text("D1  OUTER FACE, OPENS NORTH", P2(18600, 6900), SMS, "S-TEXT", "C")
s.text("D2  OPENS OUTWARD", P2(6400, 6900), SMS, "S-TEXT", "C")
s.text("300 CHANNEL AND GRATING", P2(6400, 6450), SMS, "S-TEXT", "C")
s.text("TOP LANDING  0.000", P2(10250, 7150), SMS, "S-TEXT", "C")
s.text("PLATFORM  (-)2.000", P2(15050, 7150), SMS, "S-TEXT", "C")
s.text("APPROACH STEPS  12R AT 166.6667, GOING 300, 1500 WIDE",
       P2(11000, 5300), SMS, "S-TEXT", "C")
s.text("550", P2(18580, 4150), SMS, "S-TEXT", "C")

s.dim_chain_h([P2(v, 0)[0] for v in (A["x0"], A["ix0"], A["top_landing"][1],
                                     A["flight"][1], A["platform"][1],
                                     A["x1"])],
              P2(0, A["y1"])[1], P2(0, 8100)[1], SC, "A2-DIM-S",
              minlen=2.0)
s.dim_chain_h([P2(v, 0)[0] for v in (H["x0"], H["ix0"], V["x0"], H["ix1"],
                                     H["x1"])], P2(0, H["y0"])[1],
              P2(0, -600)[1], SC, "A2-DIM-S")
s.dim_h(P2(H["x0"], 0), P2(H["x1"], 0), P2(0, -1300)[1], SC, "A2-DIM-S")
s.dim_v(P2(H["x1"], H["y0"]), P2(H["x1"], H["y1"]), P2(19200, 0)[0], SC,
        "A2-DIM-S")
s.dim_chain_v([P2(0, v)[1] for v in (V["y0"], V["y1"], PA["y1"])],
              P2(H["x1"], 0)[0], P2(21000, 0)[0], SC, "A2-DIM-S")
s.view_title(PX0 - 4.0, V2_TTL, "2", "HEADHOUSE LEVEL PLAN   (-)2.000",
             "1 : 100   HEADHOUSE 4800 x 5800;  COVERED ENTRY STAIRWELL "
             "6800 x 2000", RULE_TO)

# =====================================================================  VIEW 3
# GROUND LEVEL PLAN AND SITE, 0.000, 1 : 200
dashed_rect(P3, B["x0"], B["y0"], B["x1"], B["y1"], "A-OVER")
s.rect(*P3(H["x0"], H["y0"]), *P3(H["x1"], H["y1"]), "A-WALL")
s.rect(*P3(A["x0"], A["y0"]), *P3(A["x1"], A["y1"]), "A-WALL")
s.pline([P3(*p) for p in D.BERM_TOE_LINE], "A-COVER")
for name, cx, cy, head in D.ESC:
    s.circle(P3(cx, cy), D.ESC_CLEAR_D / 2.0 / SC3, "A-OPEN")
    s.circle(P3(cx, cy), D.ESC_COLLAR_OD / 2.0 / SC3, "A-WALL")
s.text("ESC 1  HEAD +0.150", P3(2050, -900), SMS, "S-TEXT", "C")
s.text("ESC 2  HEAD +0.700", P3(20600, -1900), SMS, "S-TEXT", "C")
s.text("ENGINEERED COVER 2000, GRADED TO SHED", P3(8200, 1500), SMS,
       "S-TEXT", "C")
s.text("HEADHOUSE ROOF  +0.900", P3(16000, 4300), SMS, "S-TEXT", "C")
s.text("NO EARTH COVER", P3(16000, 3500), SMS, "S-TEXT", "C")
s.text("STAIRWELL ROOF  +2.450", P3(12000, 6750), SMS, "S-TEXT", "C")
s.text("BERM 1.5:1, 1350 TOE RUN, TOE AT GRADE 0.000", P3(11000, -1900), SMS,
       "S-TEXT", "C")
s.text("ENTRY DOOR AT GRADE", P3(5200, 7900), SMS, "S-TEXT", "C")

# the sentry post, at its true site position
SP = D.SP_SITE
s.rect(*P3(SP["x0"], SP["y0"]), *P3(SP["x1"], SP["y1"]), "A-WALL")
s.rect(*P3(SP["x0"] + D.SP_INFILL, SP["y0"] + D.SP_INFILL),
       *P3(SP["x1"] - D.SP_INFILL, SP["y1"] - D.SP_INFILL), "A-WALL")
for gx in (D.SP_GRID_A, D.SP_GRID_B):
    for gy in (D.SP_GRID_1, D.SP_GRID_2):
        s.rect(*P3(SP["x0"] + gx - D.SP_COL / 2, SP["y0"] + gy - D.SP_COL / 2),
               *P3(SP["x0"] + gx + D.SP_COL / 2, SP["y0"] + gy + D.SP_COL / 2),
               "A-WALL")
s.circle(P3(SP["x0"] + D.SP_SPIRAL_C[0], SP["y0"] + D.SP_SPIRAL_C[1]),
         D.SP_SPIRAL_R / SC3, "A-WALL-IN")
s.text("SENTRY POST  4000 x 5000", P3(34000, 7600), SMS, "S-TEXT", "C")
s.text("SEE SHEET 02", P3(34000, 6800), SMS, "S-TEXT", "C")
s.cline(P3(-600, 3100), P3(37000, 3100), "S-CENTER")

s.dim_h(P3(B["x0"], 0), P3(B["x1"], 0), P3(0, -3400)[1], SC3, "A2-DIM-S")
s.dim_h(P3(B["x1"], 0), P3(SP["x0"], 0), P3(0, -3400)[1], SC3, "A2-DIM-S")
s.dim_h(P3(SP["x0"], 0), P3(SP["x1"], 0), P3(0, -3400)[1], SC3, "A2-DIM-S")
s.dim_v(P3(B["x0"], B["y0"]), P3(B["x0"], B["y1"]), P3(-2200, 0)[0], SC3,
        "A2-DIM-S")
s.north((262.0, 128.0))
s.view_title(PX0 - 4.0, V3_TTL, "3", "GROUND LEVEL PLAN AND SITE   0.000",
             "1 : 200   SENTRY POST AT ITS SITE POSITION, X 32000 - 36000",
             RULE_TO)

# =====================================================================  TABLES
y = s.table_stack(RCOL, RTOP, 35.5, RCOL_W, [
    dict(rows=D.ROOM_SCHEDULE, title="ROOM SCHEDULE",
         header=["ROOM", "BAY", "X RANGE", "CLEAR", "USE"],
         align=["C", "C", "C", "C", "L"], pad=2.2),
    dict(rows=D.DOOR_SCHEDULE, title="DOOR SCHEDULE",
         header=["MARK", "DOOR", "LEAF", "LEVEL", "POSITION", "RATING"],
         align=["C", "L", "C", "C", "L", "L"], pad=2.0),
    dict(rows=D.OPENING_SCHEDULE, title="OPENING SCHEDULE",
         header=["MARK", "OPENING", "SIZE", "POSITION", "NOTES"],
         align=["C", "L", "C", "L", "L"], pad=2.2),
    dict(rows=D.WALL_SCHEDULE, title="WALL SCHEDULE",
         header=["WALL", "THK", "LENGTH", "EXTENT", "NOTES"],
         align=["L", "C", "C", "C", "L"], pad=2.2),
    dict(rows=[[a, b, c] for a, b, c in D.LEVELS], title="LEVEL SCHEDULE",
         header=["LEVEL", "VALUE", "DESCRIPTION"],
         align=["L", "C", "L"], pad=2.2),
], gap=5.0, rh_max=7.2)
assert y > 35.0, f"the schedule stack overflows the frame: bottom at {y:.1f}"


if __name__ == "__main__":
    out = os.path.join(ROOT, "Presentation Sheets", "DXF",
                       "ARCH001_Underground_Headhouse_and_Ground_Level_Plans_"
                       "Redrawn_to_Project_Data.dxf")
    s.save(out)
    print("written", out, "| right column bottom y =", round(y, 1))
