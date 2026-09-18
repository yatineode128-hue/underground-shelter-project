"""
mep_data.py  --  every value that MEP010 (SHEET 10) and MEP011 (SHEET 11) draw
or print.

ONE definition of each value, so the two sheets cannot disagree with each other
and neither can disagree with the project.  Nothing here is invented: each
constant is either imported from the discipline module that already owns it, or
transcribed from the master with the Part named beside it.

SOURCES, in order of authority
    master/MASTER_PROJECT_STATE.md  A.3, A.4, A.5, A.6, F.1, G, H.23, H.24,
                                    H.35, K.3
    Drainage/Scripts/mep_proj.py     the reconciled MEP geometric constants
    Drainage/Scripts/dr_data.py      drains, pipes, chambers, equipment
    HVAC/Scripts/hv_data.py          equipment, ducts, terminals, dampers
    EMP Protection/Scripts/em_proj.py  EMP zones, penetrations, bonding
    Structural CAD/Scripts/rebar_data.py   THE bar-mark register -- every mark
                                    printed on SHEET 11 is read straight out of
                                    it, so a mark cannot appear on the sheet
                                    without a schedule entry.

EVIDENCE.  The project tags every value [C]/[R]/[A]/[U]/[N].  Those tags are
kept HERE, in the comments beside each block, and are not printed on the face of
the presentation sheets -- exactly as STR006...STR009 do it.  Nothing tagged
[U] or [N] in a source module is drawn as though it were confirmed, and nothing
is promoted:

  * SH-1, the fresh-air shaft, HAS NO PLAN POSITION in this project.  It is
    annotated off the west end of the box with a direction arrow and is NOT
    drawn at a coordinate.
  * SK-03 and SK-04 have a reserved footprint and NO RECORDED SIZE.  They are
    drawn dashed as reserved footprints and their size column is "-".
  * ST-01 has NO RECORDED LEVEL.  Its section is drawn relative to local
    finished grade, and no absolute level is printed against it.
  * The septic tank and the soak-pit cover slab have NO RECORDED BAR.  No bar
    is drawn in them and no bar mark is scheduled for them; the sheet calls
    them up to the structural engineer's detail.
  * The sump pit SU-01 does have recorded bars -- F10, F11, F12 and F13 in
    rebar_data.py -- and they are drawn and scheduled in full.

MAIN STAIRCASE IS FROZEN: 24R @ 170.8333 / 280, 3 flights x 8, total rise 4100.
Nothing in this file touches it.  It is not drawn on either sheet.
"""
import dr_data as DR
import hv_data as HV
import em_proj as EM
import mep_proj as P
import rebar_data as RD

# ------------------------------------------------------------------- identity
# Four site-description lines and no revision text, matching sheet_data.IDENTITY.
IDENTITY = [
    "UNDERGROUND CBRN-HARDENED",
    "BLAST-RESISTANT PROTECTIVE",
    "STRUCTURE + SENTRY POST",
    "PUNE, MAHARASHTRA",
]

PROJECT_LINES = ["CBRN HARDENED", "UG OPS ROOM"]
DATE = "16 SEP 2026"
DRAWN = "SYN 01"
CHECKED = "DR IR CHAUDHARI"

# --------------------------------------------------------------- box geometry
BOX = P.BOX                                   # 0..22000 x 0..6200      [C] A.4.2
INTR = P.INT                                  # 600..21400 x 600..5600  [C]
BAYS = P.BAYS                                 # eight bays              [C] A.3
IW = P.IW                                     # W5 200, W6 400, W7 400  [C]
PARTITIONS = P.PARTITIONS                     # four 110 partitions     [C]
ESC = P.ESC                                   # ESC 1 / ESC 2           [C] A.4.5
ESC_CLEAR_D = P.ESC_CLEAR_D                   # 1400 clear bore
ESC_COLLAR_OD = P.ESC_COLLAR_OD               # 1900 collar OD
VOID = P.VOID                                 # stair void in the roof  [C] A.4.4
LVL = P.LVL

BAY_CHAIN = [0, 600, 3500, 5520, 9130, 11040, 12800, 15200, 18400, 21400, 22000]

# bay centre lines, used to place terminals and tags
BAY_CX = {n: (x0 + x1) / 2.0 for n, x0, x1, w, rm, nm in BAYS}

# bay 6 decon airlock, three stages stacked in Y.  Stage boundaries follow the
# confirmed gully positions GY-06 / GY-07 / GY-08 in dr_data.            [C]
DECON_STAGES = [("STAGE 1", 3600, 5600), ("STAGE 2", 2100, 3600),
                ("STAGE 3", 600, 2100)]

# ------------------------------------------------------------- HVAC geometry
FILTER_T1 = HV.FILTER_T1                      # X 11098-12548, Y 3900-5550  [C]
FILTER_T2 = HV.FILTER_T2                      # X 11098-12548, Y 2700-3800  [C]
PLENUM = HV.PLENUM
GEN_SHAFT = HV.GEN_SHAFT                      # X 22598-23198, Y 1750-2350  [C]
BLAST_VALVE_PTS = HV.BLAST_VALVE_PTS          # BV-1 .. BV-5                [C]
SERVICE_PLATE = DR.SERVICE_PLATE              # X 11398-12198 in W2         [C]
SUMP_RECT = DR.SUMP_RECT                      # X 11068-12568, Y 900-2400   [C]
SUMP_PUMPS = DR.SUMP_PUMPS                    # PU-01 / PU-02               [C]
DECON_TANK = DR.DECON_TANK                    # TK-01, bay 8                [C]

# bore of each blast valve, mm -- from the penetration register        [C]
BV_BORE = {t[0]: t[3] for t in EM.PENETRATIONS if t[1] == "BLAST VALVE"}

# equipment that stands on the floor of bay 5, drawn to size where the project
# gives one and as a labelled footprint where it does not.
# CO2-1, O2-1 and DH-1 are confirmed to be in bay 5 and have NO recorded
# footprint, so they are shown as tagged items on the bay-5 plant band, not as
# dimensioned rectangles.                                              [C]/[N]
BAY5_PLANT = ["CO2-1", "O2-1", "DH-1"]

# ---------------------------------------------------------- EMP Zone 2  [A]
Z2 = EM.Z2                                    # X 5820-8220, Y 3700-5300
Z2_VENT_CELL = EM.Z2_VENT_CELL
Z2_VENT_DEPTH = EM.Z2_VENT_DEPTH
SE_REQUIRED_DB = EM.SE_REQUIRED_DB
BAR_SPACING = EM.BAR_SPACING                  # 150, both curtains      [C] A.5
R_EARTH_TARGET = EM.R_EARTH_TARGET            # <= 5 ohm                [C] G
ROD_L, ROD_D = EM.ROD_L, EM.ROD_D             # 3.0 m x 16 mm rod       [A]
BOND_STRAP = "100 LONG x 50 WIDE x 3 THK"     # the adopted house rule  [D]

# ================================================================ SITE LAYOUT
# master H.23 (external works, positioned) and H.35 (the A-301 key plan).
# Project +X = EAST, +Y = NORTH.                                       [A] H.23
EXCAV_FACE_X = 23000                          # east face of the excavation [C]
HH = P.HH                                     # headhouse                   [C]
ASW = P.ASW                                   # covered entry stairwell     [C]

# Sentry post -- the EAST position, as ruled RC4 and drawn on the A-301 key
# plan (master H.35).  It is SOUTH of the external works reserve.       [A] U4
SENTRY = dict(x0=32000, x1=36000, y0=600, y1=5600)

# SG2's external works reserve, 18.0 x 10.5 m, 10.0 m clear of the east
# excavation face and downgradient.                                      [A]
RESERVE = dict(x0=33000, x1=51000, y0=6500, y1=17500)

# tag, kind, centre X, centre Y, size, drawn
EXT_WORKS = [
    ("ST-01", "SEPTIC TANK", 36750, 16000, "1500 x 750", "RECT"),
    ("SK-01", "FOUL SOAK PIT", 44000, 16000, "2200 DIA", "CIRC"),
    ("SK-02", "STORM SOAKAWAY", 35000, 8500, "2200 DIA", "CIRC"),
    ("SK-03", "STAIRWELL SOAKAWAY", 41400, 8500, "-", "RESERVED"),
    ("SK-04", "HEADHOUSE SOAKAWAY", 47800, 8500, "-", "RESERVED"),
    ("IC-01", "INSPECTION CHAMBER", 7500, 9800, "600 x 450", "RECT"),
    ("IC-02", "INSPECTION CHAMBER", 40200, 16000, "600 x 450", "RECT"),
]
ST_L, ST_B = 1500, 750                        # septic tank on plan        [C]
SOAK_DIA = 2200                               # SK-01 / SK-02 bore         [C]
IC_L, IC_B = 600, 450

# the one external run whose geometry the project fixes end to end:
# ST-01 outlet face X 37500 to SK-01 near face X 42900 on Y 16000 = 5400,
# which IS the IS 2470 (Pt 2) >= 5 m offset, demonstrated.              [C]
PD16 = dict(y=16000, x0=37500, x1=42900, dn=100, grad="1:100", clear=5400)

# the other three external runs share one common services trench.  The project
# fixes their LENGTHS but not their routes, so they are drawn diagrammatically
# and the sheet says so.                                        [C] length only
EXT_RUNS = [
    ("PD-16", "FOUL", "ST-01", "SK-01", "DN100", "1:100", "5.40 m"),
    ("PD-06", "RISING MAIN", "SERVICE ENTRY PLATE", "SK-02", "DN50", "PUMPED",
     "27.00 m"),
    ("PD-11", "STORM", "CP-10 CATCHPIT", "SK-02", "DN100", "1:100", "32.35 m"),
    ("PD-13", "RISING MAIN", "SU-02 STAIRWELL SUMP", "SK-03", "DN50", "PUMPED",
     "29.60 m"),
]

# IS 2470 (Pt 2) offsets that the layout demonstrates                   [C] H.23
OFFSETS = [
    ["FOUL SOAK PIT -> SEPTIC TANK", "NOT LESS THAN 5 m", "5.40 m", "PASS"],
    ["FOUL SOAK PIT -> ANY BUILDING", "NOT LESS THAN 2 m", "10.97 m", "PASS"],
    ["EXTERNAL WORKS -> EXCAVATION FACE", "NOT LESS THAN 10 m", "10.00 m",
     "PASS"],
]

# ================================================================== SHEET 10
NOTES_10 = [
    "ALL DIMENSIONS ARE IN MM. ALL LEVELS ARE IN METRES RELATIVE TO FINISHED "
    "SITE GRADE 0.000, NEGATIVE DOWNWARDS.",
    "WRITTEN DIM TO BE FOLLOWED ONLY. DRG NOT TO BE SCALED.",
    "THIS DRG IS TO BE READ IN CONJUNCTION WITH ALL RELEVANT ARCH, STR AND "
    "SERVICES DRGS.",
    "PROJECT +X IS EAST AND PROJECT +Y IS NORTH. THE EXTERNAL WORKS ARE EAST "
    "OF THE BOX AND DOWNGRADIENT, AND STAND NORTH OF THE SENTRY POST ON THE "
    "OPPOSITE SIDE OF IT FROM THE APPROACH.",
    "THE FIVE BLAST VALVES ARE THE ONLY AIR PATHS THROUGH THE PROTECTIVE "
    "BOUNDARY. EACH IS RECESSED TO IS 4991 Cl. 6.2.1 AND CARRIES A MANUAL "
    "GAS-TIGHT DAMPER INBOARD OF IT, OPERABLE FROM INSIDE WITHOUT TOOLS.",
    "FA-2 AND FA-3 CARRY RAW UNFILTERED AIR ACROSS THE CLEAN ZONE FROM BV-1 / "
    "BV-2 TO THE FILTER TRAINS. THEY ARE A PROTECTIVE ELEMENT, NOT A DUCT, "
    "AND ARE TO BE WELDED AND PRESSURE TESTED AS SUCH.",
    "EMP ZONE 2 IS DESIGNED TO 80 dB FROM 10 kHz TO 1 GHz TO "
    "MIL-STD-188-125-1, STANDING ALONE. NO ATTENUATION FROM THE CONCRETE BOX "
    "IS CREDITED AT ANY FREQUENCY.",
    "MAX BAR SPACING 150 IN BOTH CURTAINS IS AN EMP REQUIREMENT AND IS "
    "STRICTER THAN IS 456 Cl. 26.3.3. EVERY CAST-IN FRAME AND SLEEVE IS "
    "WELDED TO THE REINFORCEMENT CAGE FOR SHIELD CONTINUITY.",
    "CONTRACTOR TO CHECK AND VERIFY THE DRG BEFORE EXECUTION.",
]

# ---- HVAC equipment schedule, from hv_data.EQUIPMENT                   [C]
HVAC_EQUIPMENT = [
    ["AHU-1", "NBC FILTER TRAIN 1", "300 m3/h", "BAY 5",
     "LOUVRE + BLAST VALVE + G4/F7 + H14 HEPA + ASZM-TEDA CARBON + FAN"],
    ["AHU-2", "NBC FILTER TRAIN 2", "300 m3/h", "BAY 5",
     "IDENTICAL TO AHU-1, STANDBY. EITHER TRAIN CARRIES THE WHOLE DUTY"],
    ["FAN-1", "SUPPLY FAN, TRAIN 1", "300 m3/h", "WITHIN AHU-1",
     "ELECTRIC DRIVE PLUS HAND CRANK"],
    ["FAN-2", "SUPPLY FAN, TRAIN 2", "300 m3/h", "WITHIN AHU-2", "AS FAN-1"],
    ["CO2-1", "CO2 SCRUBBER, SODA LIME", "20 kg/day", "BAY 5",
     "40 kg STORE = 48 h OF CLOSED MODE"],
    ["O2-1", "OXYGEN STORE", "4.5 m3/day", "BAY 5",
     "2 No. 50 L CYLINDERS AT 150 bar = 15 m3"],
    ["DH-1", "DEHUMIDIFIER", "-", "BAY 5",
     "CONDENSATE TO THE CLEAN SUMP THROUGH A 75 DEEP-SEAL TRAP"],
    ["GEN-1", "GENERATOR", "15 kVA", "BAY 8",
     "COMBUSTION AND COOLING AIR 2600 m3/h THROUGH BV-4 / BV-5"],
    ["SH-1", "FRESH-AIR SHAFT", "600 x 600", "WEST OF THE BOX",
     "GOOSENECK HEAD +1.500. 12.3 m FROM THE INTAKE TO THE ENTRY"],
    ["SH-2", "GENERATOR AIR SHAFT", "600 x 600", "X 22598 - 23198",
     "SERVES BV-4 AND BV-5. OUTSIDE THE GAS-TIGHT ENVELOPE"],
]

# ---- blast valve and gas-tight damper schedule, from hv_data.DAMPERS   [C]
DAMPER_SCHEDULE = [
    ["BV-1", "BLAST VALVE DN100", "W1 WEST WALL, (598, 2200)",
     "FRESH AIR, TRAIN 1"],
    ["BV-2", "BLAST VALVE DN100", "W1 WEST WALL, (598, 4000)",
     "FRESH AIR, TRAIN 2"],
    ["BV-3", "BLAST VALVE DN100", "IN W6, (14998, 4900)",
     "EXHAUST AND OVERPRESSURE RELIEF, TO BAY 7"],
    ["BV-4", "BLAST VALVE DN350", "W4 EAST WALL, (21398, 1300)",
     "GENERATOR INTAKE"],
    ["BV-5", "BLAST VALVE DN350", "W4 EAST WALL, (21398, 4700)",
     "GENERATOR EXHAUST"],
    "ALL FIVE:  CLOSE IN UNDER 2 ms AND HOLD 1.3 s.  RECESSED, IS 4991 "
    "Cl. 6.2.1.  DN100 DISC 3.0 kN;  DN350 DISC 36.8 kN RECESSED",
    ["GD-01", "MANUAL GAS-TIGHT DAMPER", "INBOARD OF BV-1",
     "QUARTER-TURN, OPERABLE FROM INSIDE WITHOUT TOOLS"],
    ["GD-02", "MANUAL GAS-TIGHT DAMPER", "INBOARD OF BV-2", "AS GD-01"],
    ["GD-03", "MANUAL GAS-TIGHT DAMPER", "INBOARD OF BV-3", "AS GD-01"],
    ["GD-04", "MANUAL GAS-TIGHT DAMPER", "INBOARD OF BV-4", "AS GD-01"],
    ["GD-05", "MANUAL GAS-TIGHT DAMPER", "INBOARD OF BV-5", "AS GD-01"],
    ["OPRV-1", "OVERPRESSURE RELIEF VALVE", "WITH BV-3, IN W6",
     "HOLDS THE CLEAN ZONE AT +50 TO +100 Pa"],
]

# ---- EMP zone schedule, from EMP_ZONE_SCHEDULE.md                      [C]
EMP_ZONE_SCHEDULE = [
    ["EMP ZONE 0", "EVERYTHING ABOVE GRADE", "NONE CREDITED", "0 dB"],
    ["EMP ZONE 1", "THE BURIED BOX, ALL EIGHT BAYS",
     "REINFORCEMENT CAGE AT 150, BOTH CURTAINS", "100 dB AT 10 kHz"],
    ["EMP ZONE 2", "WELDED STEEL ENCLOSURE, BAY 3",
     "SOLID WELDED STEEL, PANEL 50", "80 dB, 10 kHz - 1 GHz"],
    "EMP ZONE 2 EXTERNAL 2400 x 1600 x 2200 AT X 5820-8220, Y 3700-5300, "
    "INTERNAL 2300 x 1500 x 2100",
    "EMP ZONE 2 IS VERIFIED BY A FULL IEEE Std 299 SURVEY - A HOLD POINT "
    "BEFORE ANY EQUIPMENT IS INSTALLED",
]

# ---- envelope penetration register, from em_proj.PENETRATIONS          [C]
def penetration_rows():
    out = []
    for tag, kind, shape, bore, wall, host, note in EM.PENETRATIONS:
        bore_s = (f"{bore:.0f} DIA" if shape == "CIRC" else f"{bore:.0f} WIDE")
        out.append([tag, kind, bore_s, f"{wall:.0f}", host])
    return out

# ---- EMP Zone 2 point-of-entry schedule, from POE_PROTECTION_SCHEDULE  [C]/[A]
POE_SCHEDULE = [
    ["PoE-1", "ACCESS - SHIELDED DOOR", "5.4",
     "RF-GASKETED OR KNIFE-EDGE SHIELDED DOOR, SE CERTIFIED TO THE ENCLOSURE"],
    ["PoE-2", "VENTILATION - HONEYCOMB", "5.5",
     "6 mm CELL x 25 mm DEEP WAVEGUIDE PANEL, FRAME WELDED TO THE ENCLOSURE"],
    ["PoE-3", "POWER - PCI", "5.7.2.1",
     "PROTECTIVE DEVICE ON EVERY CONDUCTOR, MOUNTED ON THE BOUNDARY"],
    ["PoE-4", "SIGNAL - FIBRE", "5.7.4.1",
     "OPTICAL FIBRE, NO METALLIC STRENGTH MEMBER AND NO METALLIC ARMOUR"],
    ["PoE-5", "BONDING AND EARTHING", "IS 3043",
     "100 x 50 x 3 STRAPS, 3.0 m x 16 mm RODS, EARTH RESISTANCE 5 ohm OR LESS"],
]

# ================================================================== SHEET 11
NOTES_11 = [
    "ALL DIMENSIONS ARE IN MM. ALL LEVELS ARE IN METRES RELATIVE TO FINISHED "
    "SITE GRADE 0.000, NEGATIVE DOWNWARDS.",
    "WRITTEN DIM TO BE FOLLOWED ONLY. DRG NOT TO BE SCALED.",
    "THIS DRG IS TO BE READ IN CONJUNCTION WITH ALL RELEVANT ARCH, STR AND "
    "SERVICES DRGS.",
    "SUMP PIT SU-01: CONCRETE M35, w/c NOT MORE THAN 0.45, CAST MONOLITHIC "
    "WITH THE MAT. REINFORCEMENT Fe500D TO IS 1786:2008, Ld 40 PHI, LAPS "
    "50 PHI STAGGERED SO THAT NOT MORE THAN 50 % ARE SPLICED AT ONE SECTION.",
    "THE TANKING MEMBRANE IS DRESSED AROUND SU-01 AND IS CONTINUOUS WITH THE "
    "MAT TANKING. NO BAR MAY BE DISPLACED TO CLEAR A SERVICE.",
    "THE SU-01 DISCHARGE CARRIES AN ISOLATION VALVE, A GAS-TIGHT NON-RETURN "
    "VALVE, A BLAST CHECK VALVE AND A 75 DEEP-SEAL TRAP IN SERIES, ALL INSIDE "
    "THE GAS-TIGHT ENVELOPE.",
    "SEPTIC TANK ST-01 TO IS 2470 (Pt 1):1985 AND SOAK PIT SK-01 TO IS 2470 "
    "(Pt 2):1985. THE SOAK PIT SIDE AREA ALONE IS COUNTED - THE BASE CLOGS.",
    "ST-01 AND SK-01 WALL, BASE AND COVER-SLAB REINFORCEMENT IS TO THE "
    "STRUCTURAL ENGINEER'S DETAIL AND IS NOT SCHEDULED ON THIS SHEET.",
    "A PERCOLATION TEST TO IS 2470 (Pt 2) Cl. 4 IS TO BE CARRIED OUT AT THE "
    "POSITION OF EACH PIT, AT BOTH THE PIT INVERT AND THE TRENCH INVERT, "
    "BEFORE THE PITS ARE BUILT.",
    "CONTRACTOR TO CHECK AND VERIFY THE DRG BEFORE EXECUTION.",
]

# ---- sump pit geometry, all confirmed                     [C] A.4.3, F.1, S-06
SUMP = P.SUMP                # 1500 cube clear, walls 300, base 400
SUMP_CLEAR = 1500
SUMP_T_WALL = 300
SUMP_T_BASE = 400
SUMP_INVERT = -7.600
SUMP_BASE = -8.000
MAT_TOP = -6.100
MAT_SOFFIT = -6.700
BLINDING = -6.800
PU_START, PU_STOP, PU_ALARM = 900, 300, 1200      # above the invert     [C]
COVER_SUMP = 50                                    # [C] F.1
D_SUMP = 244                                       # [C] F.1

# ---- septic tank ST-01, all confirmed                     [C] IS 2470 (Pt 1)
SEPTIC = P.SEPTIC
ST_WALL = 150                                      # [C] H.24
ST_BAFFLE = "AT 2/3 L"

# ---- soak pit SK-01, RC1's ruled size                              [C] / [R]
SOAKPIT = P.SOAKPIT
SK_COVER_SLAB = 300                                # RC cover slab     [C]
SK_SAND = 300                                      # sand at the top   [C]
SK_SLAB_BELOW_GRADE = 600                          # u/s of the slab   [C] H.24

# ---- element schedule for the structures drawn on SHEET 11
ELEMENT_SCHEDULE_11 = [
    ["SU-01 SUMP PIT WALLS", "300", "1500 x 1500 CLEAR", "50", "244",
     "T16 @ 150 EF EW", "CAST MONOLITHIC WITH THE MAT"],
    ["SU-01 SUMP PIT BASE", "400", "2100 x 2100", "50", "244",
     "T16 @ 150 EF EW", "BASE SLAB (-)8.000"],
    ["MAT OPENING OVER SU-01", "600", "1500 x 1500", "75 / 50", "517",
     "4-T20 TRIMMERS EF / SIDE", "Ld 800 BEYOND THE OPENING EACH WAY"],
    ["ST-01 SEPTIC TANK", "150", "1500 x 750 LIQUID", "-", "-",
     "TO THE STR ENGINEER'S DETAIL", "TWO COMPARTMENTS, BAFFLE AT 2/3 L"],
    ["SK-01 / SK-02 COVER SLAB", "300", "2500 DIA", "-", "-",
     "TO THE STR ENGINEER'S DETAIL", "U/S 600 BELOW LOCAL FINISHED GRADE"],
    ["IC-01 / IC-02 CHAMBER", "150", "600 x 450 CLEAR", "-", "-",
     "TO THE STR ENGINEER'S DETAIL", "BENCHED TO THE CHANNEL INVERT"],
]

# ---- sump, pump and tank schedule, from dr_data.EQUIPMENT              [C]
SUMP_PUMP_SCHEDULE = [
    ["SU-01", "CLEAN SUMP", "1500 x 1500 x 1500 = 3.375 m3", "(-)7.600",
     "BAY 5. WALLS 300, BASE 400, BASE SLAB (-)8.000"],
    ["PU-01", "SUBMERSIBLE PUMP", "1.5 L/s", "(-)7.600",
     "DUTY, AUTO-ALTERNATING WITH PU-02. AT (11468, 1650)"],
    ["PU-02", "SUBMERSIBLE PUMP", "1.5 L/s", "(-)7.600",
     "STANDBY. AT (12168, 1650)"],
    ["PU-03", "HAND PUMP", "MANUAL", "(-)6.100",
     "THIRD LINE OF DEFENCE, INDEPENDENT OF POWER"],
    "PUMP CONTROL, ABOVE THE INVERT:   START +900   STOP +300   "
    "HIGH-LEVEL ALARM +1200",
    ["SU-02", "STAIRWELL SUMP", "1.0 m3", "(-)2.000", "AT THE PLATFORM"],
    ["PU-04", "STAIRWELL PUMP", "2 L/s", "(-)2.000", "DUTY"],
    ["PU-05", "STAIRWELL PUMP", "2 L/s", "(-)2.000",
     "STANDBY. NON-RETURN VALVE ON THE RISING MAIN"],
    ["TK-01", "DECON EFFLUENT TANK", "1000 L", "(-)6.100",
     "BAY 8. TANKER ONLY - NEVER TO THE CLEAN SUMP"],
]

# ---- external drainage structure schedule                              [C]
EXT_STRUCTURE_SCHEDULE = [
    ["ST-01", "SEPTIC TANK", "1500 x 750 x 1000 LIQUID = 1125 L",
     "(36750, 16000)", "10 USERS AT 45 L/DAY. FREEBOARD 300, OVERALL 1300"],
    ["SK-01", "FOUL SOAK PIT", "2200 DIA x 3500 EFFECTIVE", "(44000, 16000)",
     "24.19 m2 SIDE AREA. TAKES THE ST-01 EFFLUENT"],
    ["SK-02", "STORM SOAKAWAY", "2200 DIA x 3500 EFFECTIVE", "(35000, 8500)",
     "TAKES THE CLEAN SUMP DISCHARGE AND THE ENTRY CHANNEL"],
    ["SK-03", "STAIRWELL SOAKAWAY", "-", "(41400, 8500)",
     "FOOTPRINT RESERVED. TAKES THE SU-02 RISING MAIN"],
    ["SK-04", "HEADHOUSE SOAKAWAY", "-", "(47800, 8500)",
     "FOOTPRINT RESERVED"],
    ["IC-01", "INSPECTION CHAMBER", "600 x 450", "(7500, 9800)",
     "ON PD-11 AT THE CHANGE OF DIRECTION"],
    ["IC-02", "INSPECTION CHAMBER", "600 x 450", "(40200, 16000)",
     "ON PD-16, FOR SEPTIC TANK DE-SLUDGING ACCESS"],
]

# ---- external pipe schedule                                            [C]
EXT_PIPE_SCHEDULE = [
    [r[0], r[1], f"{r[2]}  ->  {r[3]}", r[4], r[5], r[6]] for r in EXT_RUNS
]


# ------------------------------------------------------- bar-mark table rows
def sump_marks():
    """The four sump-pit bar marks in rebar_data.py -- F10 to F13.

    Read straight out of the register, so a mark cannot be tagged on a view of
    this sheet without a schedule entry here.
    """
    keep = ("F10", "F11", "F12", "F13")
    out = []
    for m in RD.MARKS:
        if m["mark"] not in keep:
            continue
        out.append([m["mark"], f"T{m['phi']}",
                    str(m["spacing"]) if m["spacing"] else "-",
                    m["location"], f"{m['cut']:.0f}", str(m["count"])])
    assert len(out) == len(keep), f"sump marks missing: {out}"
    return out


SUMP_MARK_LOCATION = {
    "F10": "MAT 600 - SUMP-PIT OPENING TRIMMERS",
    "F11": "PIT WALLS 300 - VERTICAL, EACH FACE",
    "F12": "PIT WALLS 300 - HORIZONTAL RINGS, EACH FACE",
    "F13": "PIT BASE 400 - BOTH WAYS, EACH FACE",
}
