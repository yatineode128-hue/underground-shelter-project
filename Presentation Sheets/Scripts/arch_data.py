"""
arch_data.py  --  every value that ARCH001 (SHEET 01) and ARCH002 (SHEET 02)
draw or print.

WHY THESE TWO SHEETS EXIST.  They are REDRAWS of sheets 1 and 2 of the owner's
Revit A2 set, with the same views at the same scales, and with every dimension
and level brought to the project's own authoritative data.  The owner's
originals are preserved as the uploaded `Project1.pdf` and are not altered.

SOURCES, in order of authority
    master/MASTER_PROJECT_STATE.md   A.3 (bays and internal walls), A.4.2 (box),
                                     A.4.3 (levels), A.4.4 (stair shaft, void,
                                     pad), A.4.5 (escape shafts), A.4.6
                                     (headhouse), A.4.7 (covered stairwell),
                                     A.4.8 (sentry post), A.4.9 (every opening
                                     through the protective boundary), A.7.3
                                     (engineered cover)
    Drainage/Scripts/mep_proj.py            the reconciled MEP / architectural
                                            geometric constants
    Presentation Sheets/Scripts/sentry_data.py   the sentry post frame

CORRECTIONS.  `CORRECTIONS` below is the register of every figure that differs
from the owner's sheets 1 and 2, as `(sheet, view, item, owner, project,
authority)`.  It is the audit trail for the redraw and is reproduced in master
Part H.  It is NOT printed on the sheets -- by instruction they carry no
revision or amendment text.

MAIN STAIRCASE IS FROZEN: 24R @ 170.8333 / 280, 3 flights x 8, total rise 4100.
Read from mep_proj.STAIR; nothing here changes it.
"""
import mep_proj as P
import sentry_data as S

# ------------------------------------------------------------------- identity
IDENTITY = [
    "UNDERGROUND CBRN-HARDENED",
    "BLAST-RESISTANT PROTECTIVE",
    "STRUCTURE + SENTRY POST",
    "PUNE, MAHARASHTRA",
]
PROJECT_LINES = ["CBRN HARDENED", "UG OPS ROOM"]
DATE = "18 SEP 2026"
DRAWN = "SYN 01"
CHECKED = "DR IR CHAUDHARI"

# --------------------------------------------------------------- the main box
BOX = P.BOX                               # 0..22000 x 0..6200          A.4.2
INTR = P.INT                              # 600..21400 x 600..5600
T_WALL, T_ROOF, T_MAT = P.T_WALL, P.T_ROOF, P.T_MAT
BAYS = P.BAYS                             # eight bays, clear widths    A.3
IW = P.IW                                 # W5 200, W6 400, W7 400      A.3
PARTITIONS = P.PARTITIONS                 # four 110 W8 partitions       A.3
T_PART = P.T_PART
PART_DOOR_Y = P.PART_DOOR_Y               # 2500..3400, permanent 900 gap
BLAST_DOOR = P.BLAST_DOOR                 # 1200 x 2100, Y 600..1800    A.4.9
ESC = P.ESC                               # ESC 1 / ESC 2               A.4.5
ESC_CLEAR_D, ESC_COLLAR_T, ESC_COLLAR_OD = (P.ESC_CLEAR_D, P.ESC_COLLAR_T,
                                            P.ESC_COLLAR_OD)
VOID = P.VOID                             # 15200..18000 x 600..3760    A.4.4
PAD = P.PAD                               # 15200..18000 x 3760..5600
STAIR = P.STAIR                           # FROZEN
HH = P.HH                                 # headhouse                   A.4.6
HH_DOOR = P.HH_DOOR                       # 900 x 2100 in HW2
ASW = P.ASW                               # covered entry stairwell     A.4.7
BERM = P.BERM
SUMP_RECT = (11068, 900, 12568, 2400)     # clean sump SU-01, bay 5

# the bay dimension chain, corrected: every A.3 boundary in order
BAY_CHAIN = [0, 600]
for _n, _x0, _x1, _w, _rm, _nm in BAYS:
    BAY_CHAIN += [_x0, _x1]
BAY_CHAIN += [21400, 22000]
BAY_CHAIN = sorted(set(BAY_CHAIN))

# clear-width chain, the one the owner's sheet got wrong: bay faces only
CLEAR_CHAIN = [(x0, x1, w) for n, x0, x1, w, rm, nm in BAYS]

# ------------------------------------------------------------------- levels
# master A.4.3, verbatim.  Negative downwards from finished site grade 0.000.
LEVELS = [
    ("FINISHED SITE GRADE", "0.000", "CROWNED, FALLS 1:50 AWAY"),
    ("SENTRY POST PARAPET TOP", "+7.000", "SENTRY POST"),
    ("SENTRY POST ROOF", "+6.700", "STOREY HEIGHT 3050"),
    ("SENTRY POST FIRST FLOOR", "+3.650", "STOREY HEIGHT 3200"),
    ("ENTRY STAIRWELL ROOF AT HEAD", "+2.450", "SOFFIT +2.200"),
    ("SENTRY POST GROUND FLOOR FFL", "+0.450", "= TOP OF PLINTH BEAM PB"),
    ("HEADHOUSE ROOF TOP", "+0.900", "NO EARTH COVER; BERM GRADED TO THIS"),
    ("HEADHOUSE ROOF SOFFIT", "+0.400", "2400 CLEAR INTERNALLY"),
    ("ESC 2 HEAD", "+0.700", "1400 DIA CLEAR"),
    ("ESC 1 HEAD", "+0.150", "1400 DIA CLEAR"),
    ("TOP OF PRESSURE SLAB", "(-)2.000", "= HEADHOUSE FLOOR LEVEL"),
    ("ROOF SOFFIT", "(-)2.900", "900 PRESSURE SLAB"),
    ("INTERNAL FLOOR / TOP OF MAT", "(-)6.100", "3200 CLEAR HEIGHT"),
    ("UNDERSIDE OF MAT", "(-)6.700", "600 MAT"),
    ("FORMATION / UNDERSIDE OF PCC", "(-)6.800", "100 BLINDING"),
    ("SUMP PIT INVERT", "(-)7.600", "PIT BASE SLAB (-)8.000"),
    ("SENTRY POST FOUNDING LEVEL", "(-)2.000", "IN-SITU BASALT, F1 FOOTINGS"),
]

L_GRADE = 0.000
L_SLAB_TOP = -2.000
L_ROOF_SOF = -2.900
L_FLOOR = -6.100
L_MAT_SOF = -6.700
L_FORMATION = -6.800
L_HH_SOF = 0.400
L_HH_TOP = 0.900
L_ASW_HEAD = 2.450
L_ASW_SOF = 2.200
L_ESC1, L_ESC2 = 0.150, 0.700

# engineered cover build-up over the pressure slab -- A.7.3, 2000 total
COVER_LAYERS = [(300, "TOPSOIL / TURF"),
                (150, "GRANULAR FILTER"),
                (200, "RC BURSTER SLAB M30"),
                (500, "CRUSHED BASALT RUBBLE 25-75"),
                (750, "COMPACTED ENGINEERED FILL"),
                (100, "PROTECTION SCREED")]

# ---------------------------------------------------------- the sentry post
SP_EXT_X, SP_EXT_Y = S.EXT_X, S.EXT_Y     # 4000 x 5000                 A.4.8
SP_INT_X, SP_INT_Y = S.INT_X, S.INT_Y     # 3600 x 4600
SP_GRID_A, SP_GRID_B = S.GRID_A, S.GRID_B
SP_GRID_1, SP_GRID_2 = S.GRID_1, S.GRID_2
SP_COL = S.COL                            # 350 x 350
SP_BM_B, SP_BM_D = S.BM_B, S.BM_D
SP_SLAB_T = S.SLAB_T
SP_PB_B, SP_PB_D = S.PB_B, S.PB_D
SP_FTG_L, SP_FTG_T = S.FTG_L, S.FTG_T
SP_L_PLINTH, SP_L_FF, SP_L_ROOF = S.L_PLINTH, S.L_FF, S.L_ROOF
SP_L_PARAPET = 7.000
SP_L_FOUND = S.L_FOUND
SP_H_GROUND, SP_H_FIRST = S.H_GROUND, S.H_FIRST
SP_INFILL = 200.0                         # structural zone, 190 brick in it
SP_BRICK = 190.0                          # SP-B1
SP_DOOR_W = 900.0                         # D1
SP_WIN_W = 1200.0                         # W1 ground / vision panels first
SP_SPIRAL_R = 1000.0                      # external spiral stair
SP_SPIRAL_POLE = 250.0
SP_SITE = dict(x0=32000, x1=36000, y0=600, y1=5600)   # A.4.8, RC4

# ---------------------------------------------- doors and openings -- A.4.9
DOOR_SCHEDULE = [
    ["BD1", "BLAST DOOR 1", "1200 x 2100", "(-)6.100",
     "W6, X 14800-15200, OPENING Y 600-1800", "7 bar, GAS-TIGHT, REBOUND"],
    ["BD2", "BLAST DOOR 2", "1200 x 2100", "(-)6.100",
     "W7, X 18000-18400, OPENING Y 600-1800", "7 bar, GAS-TIGHT, REBOUND"],
    ["D1", "INNER SECURITY DOOR", "900 x 2100", "(-)2.000",
     "HW2 HEADHOUSE NORTH WALL, X 14450-15350", "NOT BLAST RATED"],
    ["D2", "ENTRY DOOR", "1000 x 2100", "0.000",
     "ENTRY STAIRWELL HEADWALL, X 9250-9500", "OPENS OUTWARD"],
    ["D3", "SENTRY POST DOOR", "900 x 2100", "+0.450",
     "SENTRY POST, BOTH STOREYS", "LINTEL L1 190 x 150 OVER"],
    "W8 PARTITIONS x 4 CARRY A PERMANENT 900 GAP AT Y 2500 - 3400 AND NO DOOR, "
    "BY DESIGN",
]

OPENING_SCHEDULE = [
    ["ESC 1", "ESCAPE SHAFT", "1400 DIA CLEAR", "BAY 1, (2050, 2050)",
     "250 RC COLLAR, OD 1900. HEAD +0.150"],
    ["ESC 2", "ESCAPE SHAFT", "1400 DIA CLEAR", "BAY 8, (19900, 2050)",
     "250 RC COLLAR, OD 1900. HEAD +0.700"],
    ["VOID", "STAIR VOID IN THE PRESSURE SLAB", "2800 x 3160",
     "BAY 7, X 15200-18000, Y 600-3760", "CANTILEVER PAD 2800 x 1840 BEYOND"],
    ["SEP", "SERVICE ENTRY PLATE", "800 WIDE", "W2 NORTH WALL, X 11398-12198",
     "CARRIES THE PD-05 DN50 SUMP RISING MAIN"],
    ["W1", "ARMOURED VISION PANEL", "1200 WIDE", "SENTRY POST, BOTH STOREYS",
     "1 No. GROUND, 8 No. FIRST STOREY. LINTEL L1 OVER"],
]

# ------------------------------------------------------------ room schedule
ROOM_SCHEDULE = [[rm, str(n), f"{x0} - {x1}", str(w), nm]
                 for n, x0, x1, w, rm, nm in BAYS]

# ------------------------------------------------------------ wall schedule
WALL_SCHEDULE = [
    ["W1 / W2 PERIMETER, S AND N", "600", "22000 EACH", "(-)6.100 TO (-)2.000",
     "PROTECTIVE BOUNDARY"],
    ["W3 / W4 PERIMETER, W AND E", "600", "6200 EACH", "(-)6.100 TO (-)2.000",
     "PROTECTIVE BOUNDARY"],
    ["W5  BAY 5 / 6", "200", "5000", "(-)6.100 TO (-)2.900",
     "FIRE AND GAS-TIGHT ONLY, NO PRESSURE DIFFERENTIAL"],
    ["W6  BAY 6 / 7", "400", "5000", "(-)6.100 TO (-)2.900",
     "PROTECTIVE BOUNDARY. BLAST DOOR 1"],
    ["W7  BAY 7 / 8", "400", "5000", "(-)6.100 TO (-)2.900",
     "PROTECTIVE BOUNDARY. BLAST DOOR 2"],
    ["W8  PARTITIONS x 4", "110", "5000 EACH", "(-)6.100 TO (-)2.900",
     "NON-STRUCTURAL. PERMANENT 900 GAP AT Y 2500-3400"],
    ["HW1 - HW4  HEADHOUSE", "400", "4000 / 5000", "(-)2.000 TO +0.900",
     "ROOF 500 THK, SOFFIT +0.400, TOP +0.900, NO EARTH COVER"],
    ["ENTRY STAIRWELL WALLS", "250", "6800 / 2000", "RAFT TO ROOF",
     "OUTSIDE THE PROTECTIVE BOUNDARY, NOT BLAST RATED"],
    ["SENTRY POST GROUND INFILL", "200 ZONE", "-", "+0.450 TO +3.650",
     "190 ONE-BRICK MODULAR BRICKWORK IS 1077 IN CM 1:6"],
]

# ================================================== the correction register
# (sheet, view, item, owner's figure, project figure, authority)
# Recorded here and in master Part H; deliberately NOT printed on the sheets.
CORRECTIONS = [
    ("01", "UNDERGROUND LEVEL PLAN", "Bay clear-width chain",
     "2900 / 3500 / 1800 / 1560 / 2400 then 2800 / 3400",
     "2900 / 1800 / 3500 / 1800 / 1560 / 2000 / 2800 / 3000", "A.3"),
    ("01", "UNDERGROUND LEVEL PLAN", "Bay 6 decon airlock clear width",
     "2400", "2000", "A.3"),
    ("01", "UNDERGROUND LEVEL PLAN", "Bay 8 generator bay clear width",
     "3400", "3000", "A.3"),
    ("01", "UNDERGROUND LEVEL PLAN", "Bay 2 clear width",
     "not dimensioned", "1800", "A.3"),
    ("01", "UNDERGROUND LEVEL PLAN", "Internal walls W5 / W6 / W7",
     "not dimensioned", "200 / 400 / 400, W6 and W7 thickened by M1", "A.3"),
    ("01", "UNDERGROUND LEVEL PLAN", "Blast door leaf, W6 and W7",
     "900 x 2100 in the door schedule", "1200 x 2100", "A.4.9"),
    ("01", "HEADHOUSE LEVEL PLAN", "Covered entry stairwell external length",
     "6550", "6800  (X 9250 - 16050)", "A.4.7"),
    ("01", "GROUND LEVEL PLAN", "Sentry post external plan",
     "3950 x 4950", "4000 x 5000", "A.4.8"),
    ("02", "GROUND / FIRST FLOOR LEVEL", "Sentry post external plan",
     "3950 x 4950", "4000 x 5000", "A.4.8"),
    ("02", "SOUTH ELEVATION", "Sentry post ground floor level",
     "440", "+0.450", "A.4.3"),
    ("02", "SOUTH ELEVATION", "Entry stairwell roof at head",
     "3400", "+2.450  (soffit +2.200)", "A.4.3 / A.4.7"),
    ("02", "SOUTH ELEVATION", "Sentry post roof",
     "7000, labelled POST ROOF",
     "+6.700 roof slab, +7.000 parapet top - two separate levels", "A.4.3"),
    ("02", "SOUTH ELEVATION", "Lowest level shown",
     "-6100, labelled FDN LEVEL",
     "(-)6.100 is the internal floor / top of mat; the mat soffit is "
     "(-)6.700 and the formation (-)6.800", "A.4.3"),
    ("02", "SOUTH ELEVATION", "Sentry post founding level",
     "not shown", "(-)2.000, F1 footings on in-situ basalt", "A.4.8 / B.8.7"),
]
