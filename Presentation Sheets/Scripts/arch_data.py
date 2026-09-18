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
     "SENTRY POST WEST WALL, Y 1000-1900, BOTH STOREYS",
     "LINTEL L1 190 x 150 OVER"],
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
     "1 No. EAST WALL GROUND; FIRST STOREY ALL FOUR FACES. LINTEL L1 OVER"],
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


# ==================================================== READ FROM THE Rev F CAD
# Everything in this block is transcribed from the Rev F DXFs in `current/cad/`,
# PARSED rather than remembered, so that the two redraws depict what the
# drawings actually depict.  The Rev F files carry a Y offset; it is removed
# here and every value below is in project coordinates.
#   1_Underground_Level_Plan.dxf       project_Y = dxf_Y + 5807.9
#   2_Ground_Plan_Headhouse_Berm.dxf   project_Y = dxf_Y + 5857.2
#   3_ / 4_Sentry_Post_*_Plan.dxf      local_Y   = dxf_Y + 8180.8
#
# WHERE THE DRAWING AND THE MASTER DISAGREE THE MASTER GOVERNS (CLAUDE.md).
# Every such case is listed in CAD_FINDINGS at the foot of this file, and none
# is silently resolved.

# --- the four W8 partitions ------------------------------------------------
# The Rev F plan draws a 900 DOOR SWING in each of the four 900 gaps.  The
# master does not: A.3 records the gap as PERMANENT, A.4.9 schedules no door in
# a W8 partition anywhere in the project, and the fire plan's single-smoke-
# compartment finding C1 depends on the four gaps being open.  NO W8 DOOR IS
# DRAWN.  MEP3-F1.
W8_GAP = PART_DOOR_Y                          # 2500 - 3400, permanent, open

# --- W5 (200, bay 5/6) and the gas-tight fire door D-05 --------------------
# The Rev F plan draws an 800 opening at Y 4400 - 5200 with a door swinging
# EAST into bay 6.  Master RC4 (K.1e, 11 Sep 2026) RULED D-05 at 900 x 2100,
# gas-tight, opening EAST into bay 6.  The ruled 900 leaf governs; the
# drawing's position is kept, so the opening is Y 4400 - 5300.  MEP3-F2.
W5_DOOR_Y = (4400.0, 5300.0)
W5_DOOR_W = 900.0
W5_SEGMENTS = [(12600.0, 600.0, 12800.0, W5_DOOR_Y[0]),
               (12600.0, W5_DOOR_Y[1], 12800.0, 5600.0)]
W5_SWING = (12800.0, W5_DOOR_Y[0], W5_DOOR_W, 0.0, 90.0)   # cx, cy, r, a0, a1

# --- bay 6, the three-stage decon airlock ----------------------------------
# Two 110 partitions run EAST-WEST across bay 6, each in two pieces with an 800
# opening between them and a door hinged on the WEST jamb opening NORTH.  Clear
# depths 2000 / 1390 / 1390 south to north; with the two 110 partitions that is
# master A.3's 2000 / 1500 / 1500 module exactly.  STAGE 1 is the 2000 bay at
# the SOUTH, at blast door 1 - the dirty end.  2.0 x 2.0 x 3.2 = 12.8 m3
# reproduces mep_proj.VENT["purge_stage_m3"] exactly, which fixes the order.
DECON_BAY = (12800.0, 14800.0)
DECON_PARTITIONS = [(2600.0, 2710.0), (4100.0, 4210.0)]
DECON_SEGMENTS = [(12800.0, 13100.0), (13900.0, 14800.0)]
DECON_SWINGS = [(13100.0, 2600.0, 800.0, 0.0, 90.0),
                (13100.0, 4100.0, 800.0, 0.0, 90.0)]
DECON_STAGE_LABELS = [("STAGE 1", 1600.0), ("STAGE 2", 3405.0),
                      ("STAGE 3", 4905.0)]

# --- the two blast doors swing in OPPOSITE directions ----------------------
# BD1 hinges on the WEST face of W6 and opens WEST into bay 6; BD2 hinges on
# the EAST face of W7 and opens EAST into bay 8.  Both hinge on the south jamb
# of the 1200 opening at Y 600 - 1800, and the wall itself starts at Y 1800.
BD1_SWING = (14800.0, 600.0, 1200.0, 90.0, 180.0)
BD2_SWING = (18400.0, 600.0, 1200.0, 0.0, 90.0)
W6_W7_BASE = 1800.0                            # wall starts above the opening

# --- the main staircase, exactly as the Rev F plan draws it ----------------
# FROZEN geometry, read from mep_proj.STAIR and confirmed against the DXF: both
# flights span Y 1800 - 3760 = 7 goings at 280, i.e. EIGHT RISERS each.
FLIGHT_Y = (1800.0, 3760.0)
FLIGHT_RISERS = [2080.0, 2360.0, 2640.0, 2920.0, 3200.0, 3480.0]
LANDING_L1 = (15200.0, 3760.0, 18000.0, 4960.0)
ARRIVAL = (15200.0, 600.0, 18000.0, 1800.0)
UP_ARROW = ((15900.0, 3510.0), (15900.0, 2050.0))

# --- bay numbering and room names, verbatim from the Rev F plan ------------
# The Rev F plan numbers the bays in bubbles above the box and names the rooms
# inside them; it does not use the U-01 .. U-08 room references at all.  Both
# are kept: the bubbles and names on the drawing, the references in the ROOM
# SCHEDULE.
BAY_BUBBLE_Y = 6760.0
BAY_BUBBLE_R = 260.0
BAY_BUBBLES = [(2050.0, "1"), (4510.0, "2"), (7270.0, "3"), (10030.0, "4"),
               (11820.0, "5"), (13800.0, "6"), (16600.0, "7"), (19900.0, "8")]
ROOM_NAMES = [
    (2050.0, 5100.0, 0.0, "ESC 1 / STORES"),
    (4510.0, 3050.0, 90.0, "LAV / MEDICAL"),
    (7270.0, 3050.0, 0.0, "OPS ROOM & HAZARD PLOTTING"),
    (10030.0, 3050.0, 90.0, "BERTHING"),
    (11820.0, 2200.0, 90.0, "CBRN PLANT"),
    (16600.0, 5250.0, 0.0, "STAIR SHAFT 2800 x 5000"),
    (19900.0, 5100.0, 0.0, "GENERATOR / SERVICES"),
]

# --- entry level (-)2.000: the two doors, and both open OUTWARD ------------
# Rev F calls the headhouse door the OUTER security door and the master calls
# the same leaf the INNER security door; same 900 x 2100 leaf, same wall, same
# X range.  The master's name is used.  MEP3-F4.
HH_DOOR_OPENING = (14450.0, 15350.0)               # through HW2, Y 5600 - 6000
HH_DOOR_SWING = (14450.0, 6000.0, 900.0, 0.0, 90.0)       # outer face, opens N
ENTRY_DOOR_OPENING = (6250.0, 7250.0)          # through the headwall X 9250-9500
ENTRY_DOOR_SWING = (9250.0, 6250.0, 1000.0, 90.0, 180.0)  # outer face, opens W
APPROACH_RISERS = [11000.0 + 300.0 * k for k in range(1, 11)]
L2_BELOW = (15200.0, 600.0, 18000.0, 1800.0)
FLIGHT2_BELOW = (16700.0, 1800.0, 17900.0, 3760.0)
UP_ARROW_HH = ((15900.0, 2050.0), (15900.0, 3510.0))
ESC2_TO_HH = 550.0                             # collar OD to the headhouse face

# --- grade 0.000: the berm, 1.5:1 with a 1350 toe run ----------------------
BERM_TOE = 1350.0
# The Rev F plan draws the headhouse toe and the stairwell toe as two separate
# outlines that cross; merged here into ONE toe line, which is the same set of
# lines with the two internal segments dropped.  The diagonals at the stairwell
# west end are the drawing's own: the berm does NOT wrap the headwall, because
# the ground has to fall to grade there for the entry door.
BERM_TOE_LINE = [(9250.0, 5750.0), (10600.0, 4400.0), (12250.0, 4400.0),
                 (12250.0, -1150.0), (19750.0, -1150.0), (19750.0, 7350.0),
                 (17400.0, 7350.0), (17400.0, 9100.0), (10600.0, 9100.0),
                 (9250.0, 7750.0)]
DOOR_CLEAR_RUN = 1350.0          # earth falls +0.900 to grade over the last 1350

# --- the excavation line: NOT DRAWN.  MEP3-F3 ------------------------------
# The Rev F plan draws it 1500 clear all round, X (-)1500 - 23500, Y (-)1500 -
# 7700.  The project's MEASURED basis is 1.000 m of working space AT FORMATION
# (master WM-V9), and RC6 (H.30) then ruled a 1 : 1 MINIMUM batter over the
# soil cap with the angle left to the geotechnical engineer - so the TOP of the
# excavation has no single value anywhere in this project.  Neither offset is
# asserted: no excavation line is drawn on either sheet.
EXCAVATION_REVF = (-1500.0, -1500.0, 23500.0, 7700.0)

# --- sentry post, from drawings 3 and 4 ------------------------------------
# D1 is in the WEST wall on BOTH floors, hinged on the inner face at the south
# jamb and opening EAST into the room.  It is reached off the spiral stair,
# which stands OUTSIDE the west wall on its own landing.
SP_D1_OPENING = (1000.0, 1900.0)
SP_D1_SWING = (200.0, 1000.0, 900.0, 0.0, 90.0)
SP_W1_GROUND = (3800.0, 1900.0, 4000.0, 3100.0)          # east wall, 1200 panel
SP_COL_SQUARES = [(0.0, 0.0), (0.0, 4650.0), (3650.0, 0.0), (3650.0, 4650.0)]
SP_SPIRAL_C = (-1150.0, 1450.0)
SP_SPIRAL_LANDING = (-150.0, 1000.0, 0.0, 1900.0)
SP_STAIR_ARROW = ((-1150.0, 900.0), (-1150.0, 2000.0))
SP_TREADS = 12
# First floor: the Rev F plan draws EIGHT 1200 vision panels, two per face.  Its
# lower WEST panel is at Y 1000 - 2200, which is where D1 is - the two overlap
# on the drawing.  SEVEN are drawn, the clashing one is not.  MEP3-F5.
SP_PANELS_FF = [
    (0.0, 2800.0, 200.0, 4000.0), (3800.0, 1000.0, 4000.0, 2200.0),
    (3800.0, 2800.0, 4000.0, 4000.0),
    (650.0, 0.0, 1850.0, 200.0), (2150.0, 0.0, 3350.0, 200.0),
    (650.0, 4800.0, 1850.0, 5000.0), (2150.0, 4800.0, 3350.0, 5000.0),
]
SP_PANELS_REVF = 8
# The first floor projects 300 all round with a 300 high PARDI over it - the
# Rev F first-floor plan says so on its face and draws the 300 offset as a
# hidden line.  This is the FIRST FLOOR.  The SENTRY POST ROOF projection is a
# different dimension and it is [NOT AVAILABLE] (master U8-F1); nothing here
# resolves it and no roof projection is drawn to a figure.  MEP3-F6.
SP_PROJECTION = 300.0
SP_PARDI_H = 300.0
SP_PARDI_T = 150.0                       # = the A.7.7 parapet, 300 x 150 [C]
SP_PROJ_OUTLINE = (-300.0, -300.0, 4300.0, 5300.0)
SP_BEAM_BANDS_X = [(50.0, 300.0), (3700.0, 3950.0)]      # B2 on grids A and B
SP_BEAM_BANDS_Y = [(50.0, 300.0), (4700.0, 4950.0)]      # B1 on grids 1 and 2

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

# ===================================== Rev F CAD vs the master - MEP3 register
# (mark, where, what the Rev F drawing shows, what governs, what was drawn)
# Recorded here and in master Part H.  NOT printed on the sheets.
CAD_FINDINGS = [
    ("MEP3-F1", "ARCH001 view 1, the four W8 partitions",
     "a 900 door swing drawn in each of the four permanent gaps",
     "A.3 / A.4.9 - the gap is permanent and NO door is scheduled in a W8 "
     "partition anywhere in the project; fire compartment C1 depends on it",
     "the four gaps drawn open, no leaf and no swing"),
    ("MEP3-F2", "ARCH001 view 1, W5 door D-05",
     "an 800 opening at Y 4400 - 5200 with the leaf opening EAST",
     "master RC4 (K.1e) RULED D-05 at 900 x 2100 gas-tight, opening EAST "
     "into bay 6",
     "900 leaf at the drawing's position, opening Y 4400 - 5300, opening EAST"),
    ("MEP3-F2a", "FLS012 (SHEET 12) escape route R1",
     "R1 crosses W5 on the spine at Y 2950",
     "the only W5 opening in the Rev F drawing is at Y 4400 - 5200, and the "
     "south decon partition lands on W5's east face at Y 2600 - 2710",
     "ARCH001 draws D-05 where the drawing puts it; FLS012 is NOT altered "
     "and the two sheets disagree on where R1 crosses W5"),
    ("MEP3-F3", "ARCH001 view 3, the excavation line",
     "drawn 1500 clear all round, X (-)1500 - 23500, Y (-)1500 - 7700",
     "WM-V9 measures 1.000 m of working space AT FORMATION, and RC6 (H.30) "
     "rules a 1:1 MINIMUM batter over the soil cap with the angle left to "
     "the geotechnical engineer - so the top of the excavation has no value",
     "no excavation line drawn; neither offset asserted"),
    ("MEP3-F4", "ARCH001 view 2, the headhouse door",
     "OUTER SECURITY DOOR 900 x 2100, NOT BLAST RATED",
     "A.4.9 calls the same leaf the INNER security door - same size, same "
     "wall HW2, same X 14450 - 15350",
     "the master's name used; the drawing's swing used - hinged on the "
     "OUTER face at the west jamb, opening NORTH"),
    ("MEP3-F5", "ARCH002 view 2, first-storey vision panels",
     "EIGHT 1200 panels, two per face; the lower WEST panel at Y 1000 - 2200 "
     "overlaps door D1 at Y 1000 - 1900",
     "A.4.8 says 'armoured vision panels, 1200 wide' and gives no count or "
     "position; D1 is in the west wall on both floors",
     "SEVEN panels drawn, the clashing one omitted; the schedule states 8"),
    ("MEP3-F6", "ARCH002, the 300 projection and pardi",
     "'300 PROJECTION WITH 300 HIGH PARDI OVER' on the FIRST FLOOR plan, "
     "with the 300 offset drawn as a hidden line",
     "A.7.7 confirms the PARAPET at 300 x 150; master U8-F1 records that the "
     "SENTRY POST ROOF projection dimension is [NOT AVAILABLE]",
     "the FIRST FLOOR projection and pardi drawn at 300; NO roof projection "
     "drawn to any figure and U8 left open"),
]
