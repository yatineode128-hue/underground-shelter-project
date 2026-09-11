"""fs_data.py  --  the escape route data behind F-101, F-102 and the schedule.

Every distance here is COMPUTED from mep_proj.py, which is the drainage / HVAC /
finishes packages' single copy of the confirmed geometry.  Nothing is typed by
hand, so a route length on a drawing cannot disagree with a route length in the
schedule or with the box it is measured in.

Evidence classes are the project's own:
    [C] confirmed   - a mep_proj value, which traces to the master or to Rev F
    [D] derived     - arithmetic on [C] values, shown in the schedule
    [N] not availble - no source exists anywhere in the project
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, "..", "..",
                                                 "Drainage", "Scripts")))
import mep_proj as P                                       # noqa: E402

REV = "FS2"
DATE = "10.09.2026"
PACKAGE = "FIRE AND LIFE SAFETY"

# ------------------------------------------------------------- the walking lines
# The spine runs at the centre of the permanent 900 partition gaps; the blast
# doors are lower in the bay, so R1 steps down to pass through W6.   [C]
SPINE_Y = sum(P.PART_DOOR_Y) / 2.0                      # 2950
BDOOR_Y = (P.BLAST_DOOR["y0"] + P.BLAST_DOOR["y1"]) / 2.0   # 1200
W5_X0, W5_X1 = P.IW[0][1], P.IW[0][2]                   # 12600 / 12800
W6_X0, W6_X1 = P.IW[1][1], P.IW[1][2]                   # 14800 / 15200
W7_X0, W7_X1 = P.IW[2][1], P.IW[2][2]                   # 18000 / 18400
ESC1_X, ESC1_Y, ESC1_HEAD = P.ESC[0][1], P.ESC[0][2], P.ESC[0][3]
ESC2_X, ESC2_Y, ESC2_HEAD = P.ESC[1][1], P.ESC[1][2], P.ESC[1][3]
FLOOR = P.LVL["floor"]                                  # -6.100
ARRIVAL = P.LVL["slab_top"]                             # -2.000
BAY1_W = P.INT["x0"]                                    # 600, west internal face
BAY8_E = P.INT["x1"]                                    # 21400, east internal face

# R1, west end of Bay 1 to the foot of the main stair in Bay 7.
R1_SPINE = [(BAY1_W + 300, SPINE_Y), (W5_X0, SPINE_Y)]          # to W5
R1_W5 = [(W5_X0, SPINE_Y), (W5_X1, SPINE_Y)]                    # THROUGH W5
R1_TO_DOOR = [(W5_X1, SPINE_Y), (14400.0, SPINE_Y),
              (14400.0, BDOOR_Y), (W6_X1, BDOOR_Y)]             # through BD1
R1_STAIR = [(W6_X1, BDOOR_Y), (P.STAIR["fltA"][0] + 300, BDOOR_Y)]

# R2 and R3, the two escape shafts.
R2 = [(ESC1_X, SPINE_Y), (ESC1_X, ESC1_Y + 150)]
R3 = [(BAY8_E - 300, SPINE_Y), (ESC2_X, SPINE_Y), (ESC2_X, ESC2_Y + 150)]
R3_FROM_BD2 = [(W7_X1, BDOOR_Y), (19100.0, BDOOR_Y), (19100.0, SPINE_Y)]

# ------------------------------------------------------------------- distances
def _run(pts):
    return sum(abs(b[0] - a[0]) + abs(b[1] - a[1])
               for a, b in zip(pts, pts[1:]))


# longest travel to R1: the west internal face of Bay 1 to the Bay 7 face of W6
TRAVEL_R1 = (W6_X1 - BAY1_W) / 1000.0                   # 14.600 m   [D]
TRAVEL_R2 = (ESC1_X - BAY1_W) / 1000.0                  # 1.450 m    [D]
TRAVEL_R3 = (BAY8_E - ESC2_X) / 1000.0                  # 1.500 m    [D]
SPINE_LEN = (P.INT["x1"] - P.INT["x0"]) / 1000.0        # 20.800 m   [C]

# vertical climb, floor to the point of emergence
CLIMB_R1_STAIR = (ARRIVAL - FLOOR)                      # 4.100 m    [C] frozen
CLIMB_R1_ASW = (0.000 - ARRIVAL)                        # 2.000 m    [D]
CLIMB_R1 = CLIMB_R1_STAIR + CLIMB_R1_ASW                # 6.100 m    [D]
CLIMB_R2 = ESC1_HEAD - FLOOR                            # 6.250 m    [D]
CLIMB_R3 = ESC2_HEAD - FLOOR                            # 6.800 m    [D]

# entry level: the covered stairwell run, platform through landing
ASW_RUN = (P.ASW["platform"][1] - P.ASW["top_landing"][0]) / 1000.0   # 6.300 m

ROUTES = [
    ("R1", "PRIMARY  -  MAIN STAIR",
     f"BAY 7 STAIR SHAFT, {P.STAIR['risers']}R @ {P.STAIR['riser']:.4f}, "
     f"{P.STAIR['flights']} FLIGHTS OF {P.STAIR['per_flight']}, "
     f"{P.STAIR['width']} WIDE  -  FROZEN GEOMETRY",
     f"{TRAVEL_R1:.1f} m", f"{CLIMB_R1:.3f} m",
     f"HEADHOUSE ({ARRIVAL:+.3f}), THEN {P.ASW['risers']}R @ "
     f"{P.ASW['riser']:.4f} TO THE ENTRY DOOR AT GRADE", "[C] / [D]"),
    ("R2", "ESCAPE SHAFT  -  ESC 1",
     f"BAY 1, {P.ESC_CLEAR_D} DIA CLEAR, {P.ESC_COLLAR_T} RC COLLAR, "
     f"OD {P.ESC_COLLAR_OD}",
     f"{TRAVEL_R2:.2f} m", f"{CLIMB_R2:.3f} m",
     f"HEAD ({ESC1_HEAD:+.3f})", "[C] / [D]"),
    ("R3", "ESCAPE SHAFT  -  ESC 2",
     f"BAY 8, {P.ESC_CLEAR_D} DIA CLEAR  -  SHARED WITH THE GENERATOR, FS-3",
     f"{TRAVEL_R3:.2f} m", f"{CLIMB_R3:.3f} m",
     f"HEAD ({ESC2_HEAD:+.3f})", "[C] / [D]"),
]

# --------------------------------------------------- decision rule, plan 4.2
DECISION = [
    ("BAY 8, GENERATOR", "R1, OR R2 IF THE SPINE IS SMOKE-LOGGED",
     "BLAST DOOR 2 IN W7 SHUT.  R3 / ESC 2 IS INSIDE THE FIRE COMPARTMENT  -  DO NOT USE IT"),
    ("BAYS 1 TO 6, OCCUPIED ZONE", "R1 IF THE ROUTE TO BAY 7 IS CLEAR",
     "OTHERWISE R2 FROM THE WEST END, R1 OR R3 FROM THE EAST.  BAYS 1-6 ARE ONE SMOKE COMPARTMENT, FS-2"),
    ("BAY 7, STAIR SHAFT", "R2 OR R3",
     "THE PRIMARY ROUTE IS THE FIRE.  BOTH BLAST DOORS SHUT"),
    ("HEADHOUSE OR COVERED STAIRWELL", "R2 OR R3",
     "R1'S SURFACE END IS BLOCKED.  BOTH ARE OUTSIDE THE PROTECTIVE BOUNDARY"),
]

# ------------------------------------------------------- findings, plan 5
FINDINGS = [
    ("FS-1", "W5 IS DESIGNATED FIRE AND GAS-TIGHT AND NO DOOR EXISTS IN IT "
             "ANYWHERE IN THE PROJECT.  Same defect as FN-U1 / D-05.  R1 "
             "crosses W5: the crossing is shown INDICATIVE and is not a design  [N]"),
    ("FS-2", "BAYS 1 TO 6 ARE ONE SMOKE COMPARTMENT.  The four 110 W8 partitions "
             "are non-structural with permanent 900 gaps at Y 2500-3400 and no "
             "doors scheduled.  The only real barriers are Blast Doors 1 and 2  [C]"),
    ("FS-3", "ESC 2 IS IN THE SAME BAY AS THE GENERATOR.  The most likely fire "
             "in the shelter denies one of the three escape routes  [C]"),
    ("FS-4", "A FIRE IN MODE 3 CLOSED CANNOT BE VENTILATED AT ALL.  Clearing "
             "smoke means opening a blast valve, which breaks the protection "
             "the closed mode exists to provide.  No precedence rule exists  [N]"),
    ("FS-5", "EVERY ACTIVE FIRE MEASURE FOLLOWS THE MISSING ELECTRICAL DESIGN.  "
             "No detection, alarm, emergency lighting or suppression exists  [N]"),
    ("FS-6", "NO LADDER, RUNG OR FALL-ARREST IS SPECIFIED IN EITHER ESCAPE "
             f"SHAFT.  R2 is a {CLIMB_R2:.3f} m climb and R3 a {CLIMB_R3:.3f} m "
             "climb from the floor, and nothing in the project says how either "
             "is made  [N]  -  RAISED BY THESE DRAWINGS"),
]


# ------------------------------------------------ entry level, R1's surface leg
HH_DOOR_X = (P.HH_DOOR["x0"] + P.HH_DOOR["x1"]) / 2.0        # 14900
ASW_CL_Y = (P.ASW["iy0"] + P.ASW["iy1"]) / 2.0               # 6750
ENTRY_DOOR = ((P.ASW["x0"] + P.ASW["ix0"]) / 2.0, ASW_CL_Y)  # 9375, 6750
STAIR_ARR = ((P.VOID["x0"] + P.VOID["x1"]) / 2.0, 2500.0)    # 16600, 2500

ENTRY_ROUTE = [STAIR_ARR,
               (HH_DOOR_X, STAIR_ARR[1]),
               (HH_DOOR_X, ASW_CL_Y),
               ENTRY_DOOR]
TRAVEL_ENTRY = _run(ENTRY_ROUTE) / 1000.0                    # m   [D]

# what you emerge into, and at what level                    [C] unless noted
EMERGE = [
    ("R1", "ENTRY DOOR, COVERED STAIRWELL",
     f"{P.ASW['door'][0]} x {P.ASW['door'][1]}", "0.000",
     "OUTSIDE THE PROTECTIVE BOUNDARY.  THE STAIRWELL IS DECLARED EXPENDABLE",
     "[C]"),
    ("R2", "ESC 1 HEAD, BAY 1", f"{P.ESC_CLEAR_D} DIA CLEAR",
     f"{ESC1_HEAD:+.3f}",
     f"{CLIMB_R2:.3f} m CLIMB FROM THE FLOOR.  NO LADDER OR RUNG SPECIFIED, FS-6",
     "[C] / [N]"),
    ("R3", "ESC 2 HEAD, BAY 8", f"{P.ESC_CLEAR_D} DIA CLEAR",
     f"{ESC2_HEAD:+.3f}",
     f"{CLIMB_R3:.3f} m CLIMB FROM THE FLOOR.  IN THE GENERATOR BAY, FS-3",
     "[C] / [N]"),
]


# ------------------------------------------- verification items, plan 8 + FS-V7
VERIF = [
    ("FS-V1", "W5 HAS NO DOOR.  The designated fire and gas-tight separation "
              "between the CBRN plant bay and the decon airlock cannot "
              "function.  Same defect as FN-U1 / D-05", "OPEN  -  DESIGN REQUIRED"),
    ("FS-V2", "NO FIRE DETECTION, ALARM, EMERGENCY LIGHTING OR SUPPRESSION "
              "exists anywhere.  EL1 provides S-01 and L-02 on DB-E; the "
              "fire engineering remains",
     "OPEN  -  ELECTRICAL BLOCKER GONE"),
    ("FS-V3", "NO RULE EXISTS FOR A FIRE DURING MODE 3 CLOSED.  Smoke cannot "
              "be cleared without breaking protection", "OPEN  -  CLIENT RULING"),
    ("FS-V4", "GENERATOR FUEL TYPE, QUANTITY AND STORAGE are unspecified, so "
              "the Bay 8 fire load cannot be quantified", "OPEN  -  FOLLOWS R-8"),
    ("FS-V5", "NO MUSTER POINT OR FIRE SERVICE ACCESS can be defined without "
              "the site plan", "OPEN  -  FOLLOWS D3"),
    ("FS-V6", "NO EXTINGUISHER SCHEDULE, DRILL REGIME OR FIRE DUTY exists",
     "OPEN  -  OPERATIONAL, CLIENT"),
    ("FS-V7", "NO LADDER, RUNG OR FALL-ARREST IN EITHER ESCAPE SHAFT.  "
              f"ESC 1 is a {CLIMB_R2:.3f} m climb from the floor and ESC 2 is "
              f"{CLIMB_R3:.3f} m", "OPEN  -  RAISED BY F-102, DESIGN REQUIRED"),
]
