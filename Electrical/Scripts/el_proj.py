"""
el_proj.py  --  constants for the ELECTRICAL AND POWER package (revision EL1).

DELIBERATELY BASIC.  This package stops at BOARD LEVEL: sources, a load
schedule, three distribution boards, the essential/battery system, and the one
single-line diagram.  It does NOT produce circuit schedules, cable sizing,
luminaire layouts or a lighting calculation - see open item EL-V5.

Evidence classes, as everywhere in this project:
    [C] CONFIRMED      traceable to the master, a Rev F drawing, S-06, or the
                       owner's own Works Management documents (which govern)
    [R] RECONSTRUCTED  computed here from confirmed values, arithmetic shown
    [D] DERIVED        an engineering result computed by THIS package
    [A] ASSUMED        an engineering selection made by THIS package
    [U] UNRESOLVED     the project holds two positions, or none
    [N] NOT AVAILABLE  no source exists anywhere in the project

SOURCES, in order:
    master A.3 (bay schedule, GEN-1 15 kVA), Part G, K.3
    HVAC/Schedules/HVAC_EQUIPMENT_SCHEDULE.md      AHU-1/2, FAN-1/2, DH-1, GEN-1
    HVAC/Schedules/OPERATING_MODE_SCHEDULE.md      modes 1-5
    Drainage/Schedules/SUMP_AND_PUMP_SCHEDULE.md   PU-01..PU-05
    MEP_AND_FINISHES_COORDINATION.md  CO-1, CO-3   service entry plate, bay 5
    EMP Protection/  (EM1)                          PoE-3/4, EM-F5, EM-V2
    Fire and Life Safety/ (FS2)                     FS-V2
    WORKS MANAGEMENT/Programme/USER_MASTER_CONSTRUCTION_SCHEDULE_R0.md
        activity 5 "Electricity Provision" and activity 123 "Mains wire
        Pulling, Mater Panel Fixing etc. (DB to Meter Panel)" - the ONLY place
        in the whole project that records an incoming mains supply.

SENTRY POST: OUT OF SCOPE, as in every other services package.
MAIN STAIRCASE: FROZEN.  Annotated only.
"""

PACKAGE = "ELECTRICAL AND POWER"
REV = "EL1"
PACKAGE_DATE = "11.09.2026"
GEOM_REV = "GEOMETRY REV F + M1"
STATUS = "FOR REVIEW - NOT FOR CONSTRUCTION"

# ------------------------------------------------------- sources  [C]
GEN_KVA = 15.0              # master A.3, bay 8            [C]
GEN_PF = 0.8                # standard set rating basis    [A]
MAINS = "VIA METER PANEL"   # owner's programme activity 123 [C]

# ------------------------------------------------- efficiencies  [A]
ETA_FAN, ETA_PUMP, ETA_MOTOR = 0.55, 0.55, 0.80
PF_SYSTEM = 0.85
RHO_W, G = 1000.0, 9.81

# ------------------------------------------------ confirmed duties  [C]
Q_FAN_M3H = 300.0           # AHU-1 / AHU-2, one duty one standby
DP_FAN_PA = 2000.0          # [A] DIRTY filter.  HV1: only 161 Pa is derivable,
                            # five of eight loss components are vendor data [N]
Q_PU01_LS, H_PU01_M = 1.5, 10.0      # clean sump, [C] duty / [A] head
Q_PU04_LS, H_PU04_M = 2.0, 5.0       # stairwell,  [C] duty / [A] head

FLOOR_AREA_M2 = 104.0       # 20800 x 5000 internal        [C] A.4.2
LIGHT_W_M2 = 5.0            # LED general lighting         [A]

# --------------------------------------------------------- load schedule
# (tag, description, board, kW, class, note)
LOADS = [
    ("L-01", "GENERAL LIGHTING, BAYS 1-8, LED", "DB-E", None, "[A]",
     f"{FLOOR_AREA_M2:.0f} m2 at {LIGHT_W_M2:.0f} W/m2. No luminaire schedule exists - EL-V5"),
    ("L-02", "EMERGENCY LIGHTING, MAINTAINED, DC", "DB-E", 0.10, "[A]",
     "On the battery at all times.  FS-V2 waits on this"),
    ("P-01", "SMALL POWER, SOCKET OUTLETS", "DB-M", 1.00, "[A]",
     "Allowance.  No socket schedule exists - EL-V5"),
    ("F-01", "FILTER TRAIN FAN, 1 DUTY OF 2", "DB-E", None, "[R]",
     "AHU-1 / AHU-2 [C].  FAN-2 is standby, NOT simultaneous"),
    ("D-01", "DEHUMIDIFIER DH-1", "DB-E", 1.00, "[A]",
     "DH-1 confirmed in master A.3; ITS DUTY IS [N] - allowance only"),
    ("U-01", "CLEAN SUMP PUMP PU-01, 1 DUTY OF 2", "DB-E", None, "[R]",
     "1.5 L/s [C].  PU-02 standby, auto-alternating, NOT simultaneous"),
    ("U-02", "STAIRWELL PUMP PU-04, 1 DUTY OF 2", "DB-M", None, "[R]",
     "2.0 L/s [C].  OUTSIDE the protective envelope"),
    ("Z-01", "EMP ZONE 2 OPS / COMMS EQUIPMENT", "DB-Z2", 1.50, "[A]",
     "ALLOWANCE, NOT A SCHEDULE.  This is the number EM-V2 was waiting for"),
    ("S-01", "FIRE DETECTION AND ALARM PANEL", "DB-E", 0.10, "[A]",
     "Panel and loop only.  Head layout is fire engineering - FS-V2"),
    ("B-01", "BATTERY CHARGER / INVERTER", "DB-M", 0.80, "[A]",
     "Sized with the battery, section E.5"),
    ("G-01", "GENERATOR AUXILIARIES", "DB-M", 0.30, "[A]",
     "Controls, block heater, starting.  Vendor data [N]"),
]

# loads that remain live with no generator and no mains  (tag, kW or None, note)
ESSENTIAL = [
    ("L-02", 0.10, "EMERGENCY LIGHTING - maintained"),
    ("L-01r", 0.15, "REDUCED GENERAL LIGHTING, 25 % of L-01  [A]"),
    ("S-01", 0.10, "FIRE DETECTION AND ALARM"),
    ("Z-01r", 0.75, "EMP ZONE 2 AT 50 % DUTY  [A]"),
    ("U-01i", None, "CLEAN SUMP PUMP, INTERMITTENT AT 10 % DUTY  [A]"),
    ("R-01", 0.10, "CO2 SCRUBBER RECIRCULATION FAN  [A] - NOT IN ANY SCHEDULE, EL-V7"),
    ("I-01", 0.05, "INSTRUMENTS AND MONITORING  [A]"),
]
SUMP_DUTY_FRACTION = 0.10

# ---------------------------------------------------------- battery  [A]
V_DC = 48.0
DOD = 0.80                  # depth of discharge, flooded / VRLA  [A]
ETA_INV = 0.90
WH_PER_KG = 35.0            # lead-acid, order of magnitude       [A]
# RULED - RC2, 11 Sep 2026 (master H.21).  The project owner has ruled that
# the generator MAY run during mode 3: all five valves shut at the shock, then
# BV-4 and BV-5 REOPEN for GEN-1.  Case A is therefore [C], not [A], and the
# battery stands at the size EL1 already designed.  Case B is retained below
# because the comparison is what made the question answerable - it is now
# HISTORICAL, not an alternative.
CASE_A_H = 4.0              # generator restartable after the shock  [C] RULED
CASE_B_H = 48.0             # HISTORICAL - the rejected reading      [C] 48 h

FLOOR_LL_KPA = 5.0          # master A.7.2 floor live load        [C]

# ------------------------------------------------------------- boards
BOARDS = [
    ("DB-M", "MAIN LV BOARD", 8, "BAY 8 - GREY ZONE, WITH GEN-1",
     "Mains + generator changeover.  OUTSIDE the gas-tight envelope"),
    ("DB-E", "ESSENTIAL BOARD", 5, "BAY 5 - CBRN PLANT",
     "Fed from DB-M and from the inverter.  INSIDE the gas-tight envelope"),
    ("DB-Z2", "EMP ZONE 2 SUB-BOARD", 3, "BAY 3 - INSIDE THE SHIELDED ENCLOSURE",
     "Fed through the PCI on the Zone 2 boundary - EM1 PoE-3"),
]

# generator fuel, for the endurance check
SFC_L_PER_KWH = 0.35        # small diesel at part load  [A], vendor data is [N]
MISSION_H = 96.0            # master A.1  [C]
