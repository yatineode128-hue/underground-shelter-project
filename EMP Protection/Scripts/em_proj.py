"""
em_proj.py  --  shared constants for the EMP PROTECTION package (revision EM1).

ONE definition of each value, each carrying its source and its evidence class,
using the master's own legend:

    [C] CONFIRMED      traceable to the master, to a Rev F drawing or to S-06
    [R] RECONSTRUCTED  computed here from confirmed values, arithmetic shown
    [D] DERIVED        an engineering result computed by THIS package
    [A] ASSUMED        an engineering selection made by THIS package
    [U] UNRESOLVED     competing values exist, or the input does not exist
    [N] NOT AVAILABLE  no source exists anywhere in the project

SOURCE OF TRUTH, in order:
    master/MASTER_PROJECT_STATE.md   A.1, A.3, A.4, A.5, G, K.1b, K.3
    HVAC/Schedules/DAMPER_AND_VALVE_SCHEDULE.md     (the five blast valves)
    Drainage/Schedules/PIPE_SCHEDULE.md             (PD-05 rising main)
    MEP_AND_FINISHES_COORDINATION.md  CO-1 / CO-2   (service entry plate)
    Schedule of Finishes/Schedules/FINISH_LEGEND.md (W-04, the Zone 2 lining)

SENTRY POST: OUT OF SCOPE, consistent with every other services package.  It is
above ground, framed, brick-infilled and not blast designed; its EMP exposure is
total and nothing in this package changes that.  Stated once, then excluded.

MAIN STAIRCASE: FROZEN.  This package annotates it and changes nothing.

NAMING WARNING.  The drainage and finishes packages already use "zone 1/2/3" for
CLEANLINESS (clean / dirty / effluent).  The EMP zones defined here are a
DIFFERENT scheme on the same building, so the prefix "EMP" is MANDATORY on every
drawing, schedule and note.  "Zone 2" unqualified is ambiguous in this project.
"""

# --------------------------------------------------------------- identity
PACKAGE = "EMP PROTECTION"
REV = "EM1"
PACKAGE_DATE = "10.09.2026"
GEOM_REV = "GEOMETRY REV F + M1"
STATUS = "FOR REVIEW - NOT FOR CONSTRUCTION"

# ---------------------------------------------------- physical constants
C_LIGHT = 2.99792458e8          # m/s, exact by definition
MU0 = 4.0e-7 * 3.141592653589793

# ------------------------------------------------- the requirement  [C] G
# master Part G: MIL-STD-188-125-1 -- "80 dB, 10 kHz - 1 GHz", with sections
# 5.4 (access), 5.5 (waveguide below cutoff), 5.7.2.1 (power PCI),
# 5.7.4.1 (fibre), 5.7.6 (RF).  IEEE Std 299 -- shielding effectiveness survey.
SE_REQUIRED_DB = 80.0
F_LO_HZ = 1.0e4                 # 10 kHz
F_HI_HZ = 1.0e9                 # 1 GHz

# ------------------------------------------------------ geometry  [C] A.4
BOX = dict(x0=0, x1=22000, y0=0, y1=6200)
INT = dict(x0=600, x1=21400, y0=600, y1=5600)
T_WALL, T_ROOF, T_MAT = 600, 900, 600
T_W6 = T_W7 = 400
H_CLEAR = 3200
LVL = dict(grade=0.000, slab_top=-2.000, roof_soffit=-2.900, floor=-6.100,
           mat_soffit=-6.700, hh_top=+0.900,
           esc1_head=+0.150, esc2_head=+0.700)

# The single most important reinforcement value in this package.  [C] A.5:
# "Max bar spacing, both curtains -- 150 mm, EMP requirement, stricter than
# IS 456 Cl. 26.3.3".
BAR_SPACING = 150.0             # mm, both curtains, both ways

# stair void in the 900 pressure slab  [C] A.4.4 / mep_proj.VOID
VOID = dict(x0=15200, x1=18000, y0=600, y1=3760)

# escape shafts  [C] A.4.5
ESC = [("ESC 1", 2050, 2050, +0.150), ("ESC 2", 19900, 2050, +0.700)]
ESC_CLEAR_D = 1400              # mm clear bore
ESC_COLLAR_T, ESC_COLLAR_OD = 250, 1900

# bays  [C] A.3
BAYS = [(1, 600, 3500, "U-01", "EMERGENCY STORES / ESC 1"),
        (2, 3610, 5410, "U-02", "LAVATORY + MEDICAL"),
        (3, 5520, 9020, "U-03", "OPS ROOM - EMP ZONE 2 HOST BAY"),
        (4, 9130, 10930, "U-04", "BERTHING - 9 BERTHS"),
        (5, 11040, 12600, "U-05", "CBRN PLANT + SUMP"),
        (6, 12800, 14800, "U-06", "DECON AIRLOCK - 3 STAGE"),
        (7, 15200, 18000, "U-07", "STAIR SHAFT - STAIR VOID OVER"),
        (8, 18400, 21400, "U-08", "GENERATOR / ESC 2")]

# ------------------------------------------- envelope penetrations  [C]
# (tag, kind, shape, bore_mm, wall_mm, host, note)
# Blast valves: HVAC/Schedules/DAMPER_AND_VALVE_SCHEDULE.md, all [C].
# Service entry plate: MEP_AND_FINISHES_COORDINATION.md CO-1, [C] position,
#   [N] size and level.
PENETRATIONS = [
    ("BV-1", "BLAST VALVE", "CIRC", 100.0, 600.0, "W1 WEST WALL, BAY 1",
     "FRESH AIR TRAIN 1, (598, 2200)"),
    ("BV-2", "BLAST VALVE", "CIRC", 100.0, 600.0, "W1 WEST WALL, BAY 1",
     "FRESH AIR TRAIN 2, (598, 4000)"),
    ("BV-3", "BLAST VALVE", "CIRC", 100.0, 400.0, "W6, (14998, 4900)",
     "EXHAUST / OPRV, DISCHARGES INTO BAY 7"),
    ("BV-4", "BLAST VALVE", "CIRC", 350.0, 600.0, "EAST WALL, BAY 8",
     "GENERATOR INTAKE, (21398, 1300)"),
    ("BV-5", "BLAST VALVE", "CIRC", 350.0, 600.0, "EAST WALL, BAY 8",
     "GENERATOR EXHAUST, (21398, 4700)"),
    ("SEP", "SERVICE ENTRY PLATE", "RECT", 800.0, 600.0,
     "NORTH WALL, X 11398-12198", "PLATE APERTURE. LEVEL AND SIZE [N]"),
    ("PD-05", "RISING MAIN BORE", "CIRC", 50.0, 600.0,
     "THROUGH THE SERVICE ENTRY PLATE", "DN50 SUMP RISING MAIN, MATERIAL [N]"),
    ("ESC1", "ESCAPE SHAFT", "CIRC", 1400.0, 3050.0, "BAY 1, (2050, 2050)",
     "HEAD +0.150, SHAFT GRADE TO ROOF SOFFIT"),
    ("ESC2", "ESCAPE SHAFT", "CIRC", 1400.0, 3600.0, "BAY 8, (19900, 2050)",
     "HEAD +0.700, SHAFT GRADE TO ROOF SOFFIT"),
    ("VOID", "STAIR VOID", "RECT", 3160.0, 900.0, "PRESSURE SLAB, BAY 7",
     "2800 x 3160 OPENING. LARGEST APERTURE IN THE ENVELOPE"),
]

# --------------------------------------- EMP Zone 2 enclosure  [A] EM1
# An ENGINEERING SELECTION by this package.  The project confirms that a Zone 2
# enclosure is REQUIRED (master A.3, K.3, finishes W-04) and contains NO
# specification for it whatsoever.  Every dimension below is [A] and depends on
# an equipment schedule that does not exist -- see open item EM-V2.
#
# Placed in bay 3 (U-03) on the NORTH side, clear of the Y 2500-3400 circulation
# route through the W8 partition door gaps, with a 300 inspection gap on every
# free face so that the IEEE Std 299 survey can reach every seam.
Z2 = dict(x0=5820, x1=8220, y0=3700, y1=5300,      # external plan, mm
          h_ext=2200,                               # external height, mm
          panel=50,                                 # shielded panel thickness
          floor_level=-6.100,
          bay=3, room="U-03", finish="W-04")

Z2_VENT_CELL = 6.0              # mm honeycomb cell, [A]
Z2_VENT_DEPTH = 25.0            # mm honeycomb depth, [A]

# ----------------------------------------------- bonding  [D] EM1 / [C] G
# IEEE 142 / IS 3043 earthing target <= 5 ohm is CONFIRMED in master G and in
# the WM1 electrical scope.  K.3 records Deccan basalt at 1e3 - 1e4 ohm.m and
# says "test earth resistance early".
RHO_BASALT = (1.0e3, 1.0e4)     # ohm.m, [C] K.3
R_EARTH_TARGET = 5.0            # ohm, [C] G / WM1 scope
ROD_L, ROD_D = 3.0, 0.016       # m, a conventional 3 m x 16 mm rod, [A]

# bonding straps compared in the calculation  (label, length_mm, width_mm, t_mm)
STRAPS = [("LONG ROUND-THE-CORNER STRAP", 600.0, 25.0, 3.0),
          ("HOUSE RULE - SHORT WIDE STRAP", 100.0, 50.0, 3.0),
          ("HOUSE RULE - LIMIT CASE", 150.0, 50.0, 3.0)]
BOND_MAX_LEN = 100.0            # mm, [D] rule set by this package
BOND_MIN_WL = 5.0               # width : length ratio, [D]
