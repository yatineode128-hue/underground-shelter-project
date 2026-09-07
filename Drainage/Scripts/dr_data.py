"""
dr_data.py  --  the drainage network itself: every gully, channel, pipe,
chamber and item of equipment, with one entry per item.

The schedules and the drawings are both generated from this file, so a tag on a
drawing and a row in a schedule cannot disagree.

CLASS column, throughout:
  [C] confirmed in the project   [R] reconstructed   [A] this package's selection
  [U] unresolved                 [N] not available - DATA REQUIRED

CONFIRMED POSITIONS read out of sheet S-06 by parsing its geometry
(view V1, scale 1:60, paper origin 92.03 / 420.00):
    clean sump          X 11068 - 12568   Y  900 - 2400   1500 x 1500
    sump pumps          (11468, 1650) and (12168, 1650), 420 dia
    service entry plate X 11398 - 12198   Y 5600 - 6200   in the north wall
    NBC filter train 2  X 11098 - 12548   Y 2700 - 3800
    NBC filter train 1  X 11098 - 12548   Y 3900 - 5550
    decon effluent tank X 20198 - 21398   Y 4400 - 5600   BAY 8
    generator air shaft X 22598 - 23198   Y 1750 - 2350   outside the box
    blast valves        (598, 2200) (598, 4000) (14998, 4900) (21398, 1300)
                        (21398, 4700)
"""

# ----------------------------------------------------------------- levels
FFL_SUMP_EDGE = -6.075          # [A] 25 screed on the mat at the sump edge
FFL_SPINE_W = -6.047            # [R] + 28 over 11200 at 1:400
SCREED_MIN = 25                 # [A]
FALL_LONG = 400                 # 1:400 along the spine, east to the sump  [A]
FALL_TR_DRY = 100               # 1:100 transverse, dry areas              [A]
FALL_TR_WET = 80                # 1:80 wet areas - matches the confirmed
                                # headhouse gully fall                     [A]
TRAP_SEAL = 75                  # mm deep seal, all traps in the envelope  [A]
UPSTAND = 50                    # mm threshold upstand at W5 and BD1       [A]

# confirmed positions, from S-06 (see the docstring)
SUMP_RECT = (11068, 900, 12568, 2400)
SUMP_PUMPS = [(11468, 1650), (12168, 1650)]
SERVICE_PLATE = (11398, 5600, 12198, 6200)
FILTER_T2 = (11098, 2700, 12548, 3800)
FILTER_T1 = (11098, 3900, 12548, 5550)
DECON_TANK = (20198, 4400, 21398, 5600)
GEN_SHAFT = (22598, 1750, 23198, 2350)
BLAST_VALVE_PTS = [("BV-1", 598, 2200), ("BV-2", 598, 4000),
                   ("BV-3", 14998, 4900), ("BV-4", 21398, 1300),
                   ("BV-5", 21398, 4700)]

# hydraulic zones created by the protective boundary  (finding DR-F5)
ZONES = [
    ("Z1", "CLEAN", "bays 1-5, inside the gas-tight envelope",
     "clean sump SU-01, bay 5", "COMPLETE", "[C]"),
    ("Z2", "DECON", "bay 6, inside the envelope but dirty",
     "1000 L tank TK-01 - DRAWN IN BAY 8, across the boundary",
     "ROUTE UNDEFINED", "[U]"),
    ("Z3", "GREY", "bays 7 and 8, outside the gas-tight envelope",
     "none recorded", "NO DESTINATION", "[N]"),
]

# ------------------------------------------------------------- drain points
# tag, x, y, level, type, seal, serves, zone, class
DRAINS = [
    ("GY-01", 2050, 3100, -6.100, "TRAPPED FLOOR GULLY DN100",
     TRAP_SEAL, "Bay 1 stores - washdown only", "Z1", "[A]"),
    ("GY-02", 4510, 3100, -6.100, "TRAPPED FLOOR GULLY DN100",
     TRAP_SEAL, "Bay 2 lavatory + medical, basin waste over the grating",
     "Z1", "[A]"),
    ("GY-03", 7270, 3100, -6.100, "TRAPPED FLOOR GULLY DN100",
     TRAP_SEAL, "Bay 3 ops room - washdown only", "Z1", "[A]"),
    ("GY-04", 10030, 3100, -6.100, "TRAPPED FLOOR GULLY DN100",
     TRAP_SEAL, "Bay 4 berthing - washdown only", "Z1", "[A]"),
    ("GY-05", 11820, 2600, -6.100, "OPEN FALL TO THE SUMP",
     0, "Bay 5 CBRN plant, dehumidifier and coil condensate", "Z1", "[A]"),
    ("GY-06", 13800, 4600, -6.100, "TRAPPED GULLY DN100 - SEGREGATED",
     TRAP_SEAL, "Decon airlock stage 1  (2000 x 2000)", "Z2", "[A]"),
    ("GY-07", 13800, 2850, -6.100, "TRAPPED GULLY DN100 - SEGREGATED",
     TRAP_SEAL, "Decon airlock stage 2  (2000 x 1500)", "Z2", "[A]"),
    ("GY-08", 13800, 1350, -6.100, "TRAPPED GULLY DN100 - SEGREGATED",
     TRAP_SEAL, "Decon airlock stage 3  (2000 x 1500) - dry side, "
     "gully for washdown only", "Z2", "[A]"),
    ("GY-09", 19900, 3100, -6.100, "TRAPPED GULLY DN100",
     TRAP_SEAL, "Bay 8 generator bay washdown - NO DESTINATION DEFINED",
     "Z3", "[U]"),
    ("GY-10", 15050, 6750, -2.000, "TRAPPED GULLY DN100",
     TRAP_SEAL, "Entry stairwell platform 1500 x 1500", "EXT", "[C]"),
    ("GY-11", 14700, 1960, -2.000, "TRAPPED GULLY DN100, FALL 1:80",
     TRAP_SEAL, "Headhouse floor, hose-down point - "
     "TO THE EXTERNAL SOAKAWAY, NEVER TO THE CLEAN SUMP", "EXT", "[C]"),
    ("CH-10", 9100, 6750, 0.000, "300 CHANNEL + GRATING, FULL 1500 WIDTH",
     0, "Entry threshold, X 8950-9250; ground falls away 1:50 for 2000",
     "EXT", "[C]"),
]

# ------------------------------------------------------------------- pipes
# id, service, from, to, DN, gradient, IL start, IL end, length m, notes, class
PIPES = [
    ("PD-01", "WASTE", "GY-02", "SU-01 clean sump", 100, "1:100",
     -6.250, -6.316, 6.56,
     "CAST IN THE TOP OF THE MAT - BUILDER'S WORK BW-01, 216 recess at the "
     "sump end, local mat 384. STRUCTURAL ACCEPTANCE REQUIRED", "[A]"),
    ("PD-02", "WASTE", "GY-01 / GY-03 / GY-04", "graded floor", 0, "-",
     None, None, 0.0,
     "NO PIPE. Bays 1, 3 and 4 fall to the spine and the spine falls 1:400 "
     "east to the sump. Gullies are rodding and washdown points only", "[A]"),
    ("PD-03", "EFFLUENT", "GY-06 / GY-07 / GY-08", "CP-01 bay 6", 100,
     "1:100", -6.250, -6.290, 4.00,
     "SEGREGATED. Never connected to PD-01 or to the clean sump", "[A]"),
    ("PD-04", "EFFLUENT", "CP-01 bay 6", "TK-01 decon tank, bay 8", 0, "-",
     None, None, 0.0,
     "*** ROUTE NOT DEFINED. Crosses the protective boundary at W6 and W7 "
     "and passes through the stair shaft. PROTECTIVE-DESIGN DECISION - "
     "ENGINEER TO CONFIRM ***", "[U]"),
    ("PD-05", "RISING MAIN", "SU-01 pumps", "service entry plate", 50, "-",
     -7.300, None, 3.20,
     "Isolation valve, gas-tight NRV, blast check valve, 75 deep-seal trap "
     "IN SERIES, all inside the envelope. v = 0.76 m/s at 1.5 L/s", "[C]/[A]"),
    ("PD-06", "RISING MAIN", "service entry plate", "SK-02 storm soakaway",
     50, "-", None, None, 0.0,
     "LENGTH NOT DETERMINABLE - no soakaway position exists in the project "
     "(open item D3)", "[N]"),
    ("PD-07", "WASTE", "GY-09 bay 8", "no destination", 100, "1:100",
     None, None, 0.0,
     "*** ZONE 3 HAS NO DRAINAGE DESTINATION. DATA REQUIRED ***", "[N]"),
    ("PD-10", "STORM", "CH-10 threshold channel", "CP-10 catchpit", 100,
     "1:100", -0.250, None, 2.00,
     "Discharges AWAY from the entry. Ground already falls away 1:50 for "
     "2000, so the channel is an interception, not a collection", "[A]"),
    ("PD-11", "STORM", "CP-10", "SK-02 storm soakaway", 100, "1:100",
     None, None, 0.0, "LENGTH NOT DETERMINABLE - open item D3", "[N]"),
    ("PD-12", "STORM", "GY-10 platform gully", "SU-02 stairwell sump", 100,
     "1:80", -2.150, -2.169, 1.50,
     "Platform (-)2.000, 1500 x 1500", "[C]/[A]"),
    ("PD-13", "RISING MAIN", "SU-02 pumps", "SK-03 own soakaway", 50, "-",
     None, None, 0.0,
     "NON-RETURN VALVE ON THE RISING MAIN [C]. Length not determinable",
     "[C]/[N]"),
    ("PD-14", "WASTE", "GY-11 headhouse gully", "SK-04 external soakaway",
     100, "1:80", -2.150, None, 0.0,
     "TRAPPED GULLY -> EXTERNAL SOAKAWAY, NEVER TO THE CLEAN SUMP [C]. "
     "Length not determinable", "[C]/[N]"),
    ("PD-15", "FOUL", "Bay 2 lavatory  (CASE B ONLY)", "ST-01 septic tank",
     100, "PUMPED", None, None, 0.0,
     "*** PROVISIONAL - CASE B OF OPEN ITEM D2 ONLY. Needs a macerator or "
     "packaged pumping unit AND A SECOND ENVELOPE PENETRATION. Not "
     "specified, not sized, not adopted ***", "[U]"),
    ("PD-16", "FOUL", "ST-01 septic tank", "SK-01 soak pit", 100, "1:100",
     None, None, 0.0,
     "Length not determinable - no site plan (open item D3)", "[C]/[N]"),
]

# -------------------------------------------------------------- chambers
# tag, type, size, cover level, invert, serves, class
CHAMBERS = [
    ("CP-01", "SEALED COLLECTION POINT", "600 x 600", -6.100, -6.290,
     "Decon effluent, bay 6, W6 side. SEALED AND GAS-TIGHT - it sits inside "
     "the gas-tight envelope", "[A]"),
    ("CP-10", "TRAPPED CATCHPIT", "450 x 450", 0.000, None,
     "Entry threshold channel CH-10. 75 deep seal, silt bucket", "[A]"),
    ("IC-01", "INSPECTION CHAMBER", "600 x 450", 0.000, None,
     "On PD-11 at the change of direction. Position not fixed - no site "
     "plan (D3)", "[A]/[N]"),
    ("IC-02", "INSPECTION CHAMBER", "600 x 450", 0.000, None,
     "On PD-16 upstream of SK-01, for septic tank de-sludging access. "
     "Position not fixed (D3)", "[A]/[N]"),
    ("RE-01", "RODDING EYE", "DN100", -6.100, -6.250,
     "Head of PD-01 at GY-02", "[A]"),
    ("RE-02", "RODDING EYE", "DN100", -6.100, -6.290,
     "Head of PD-03 at GY-06", "[A]"),
]

# ------------------------------------------------------------- equipment
# tag, item, duty / size, level, notes, class
EQUIPMENT = [
    ("SU-01", "CLEAN SUMP", "1500 x 1500 x 1500 = 3.375 m3", -7.600,
     "Invert (-)7.600, base slab (-)8.000. Walls/base 300/400 - C18 OPEN, "
     "400 held. T16 @ 150 EF EW, 4-T20 trimmers each face/side. Cast "
     "monolithic with the mat, membrane dressed around the pit", "[C]"),
    ("PU-01", "SUBMERSIBLE PUMP", "1.5 L/s", -7.600,
     "Duty. Auto-alternating with PU-02. Start +900, stop +300, high alarm "
     "+1200 above the invert. Position (11468, 1650) from S-06", "[C]"),
    ("PU-02", "SUBMERSIBLE PUMP", "1.5 L/s", -7.600,
     "Standby. Position (12168, 1650) from S-06. Monthly witnessed test "
     "required - finding DR-F1", "[C]"),
    ("PU-03", "HAND PUMP", "manual", -6.100,
     "Third line of defence, independent of power. Confirmed on S-06", "[C]"),
    ("SU-02", "STAIRWELL SUMP", "1.0 m3", -2.000,
     "At the platform. 32 h to fill at the worst door-open driving-rain "
     "rate (Rev F drawing 5 note 9)", "[C]"),
    ("PU-04", "STAIRWELL PUMP", "2 L/s", -2.000, "Duty", "[C]"),
    ("PU-05", "STAIRWELL PUMP", "2 L/s", -2.000,
     "Standby. NRV on the rising main", "[C]"),
    ("TK-01", "DECON EFFLUENT TANK", "1000 L", -6.100,
     "Bay 8, X 20198-21398, Y 4400-5600 as drawn on S-06. TANKER ONLY - "
     "never to the clean sump. Emptying route not defined (DR-D4)", "[C]"),
    ("TK-02", "POTABLE WATER TANK", "1000 L", -6.100,
     "Bay 1. Shown for coordination only - water supply is not in this "
     "package", "[C]"),
    ("ST-01", "SEPTIC TANK", "1.50 x 0.75 x 1.00 liquid = 1125 L", None,
     "IS 2470 (Pt 1) Table 1, up to 10 users. Two compartments, baffle at "
     "2/3 L, inlet and outlet tees, 50 cowled vent >= 2 m above grade. "
     "Freeboard 300, overall depth 1.30 m. Required 1050 L - PASS", "[C]"),
    ("SK-01", "FOUL SOAK PIT", "2.0 dia x 3.5 effective = 21.99 m2 side",
     None,
     "*** 22.5 m2 REQUIRED - SHORT BY 2.3 %, CONFLICT DR-C2. Fill 40-80 mm "
     "brickbat/stone, 300 sand at the top, RC cover slab. Side area only "
     "counted. PERCOLATION TEST MANDATORY - IS 2470 (Pt 2) Cl. 4 ***", "[C]"),
    ("SK-02", "STORM SOAKAWAY", "2.0 dia x 3.5 effective = 21.99 m2 side",
     None,
     "SIZED BY THIS PACKAGE. 20.0 m2 required for 400 L/day - PASS, 10 % "
     "margin. Same construction as SK-01. Position not fixed (D3)", "[A]"),
    ("SK-03", "STAIRWELL SOAKAWAY", "size not recorded", None,
     "Exists in the project ('own soakaway') but is not sized anywhere. "
     "54.6 h to recover from one sump-full at the assumed absorption rate "
     "- finding DR-F3", "[C]/[N]"),
    ("SK-04", "HEADHOUSE EXTERNAL SOAKAWAY", "size not recorded", None,
     "Exists on the Rev F ground plan ('trapped gully -> external "
     "soakaway'). Not sized anywhere", "[C]/[N]"),
]

# --------------------------------------------------- sanitary fixtures
# tag, fixture, room, discharge, trap, notes, class
FIXTURES = [
    ("SN-01", "WASH BASIN", "U-02 lavatory", "DN40 waste", "75 bottle trap",
     "Discharges over the GY-02 grating with an air gap - no buried "
     "connection inside the envelope", "[A]"),
    ("SN-02", "MEDICAL WASH-UP", "U-02 medical", "DN40 waste", "75 bottle trap",
     "As SN-01, over GY-02", "[A]"),
    ("SN-03", "SEALED-CASSETTE CHEMICAL TOILET", "U-02 lavatory",
     "NO DISCHARGE", "-",
     "PROTECTIVE MODE: 'the shelter is SEALED and uses sealed-cassette "
     "chemical toilets - nothing is discharged' [C] S-06. Cassette handling "
     "route is an O&M item, not a drainage item", "[C]"),
    ("SN-04", "DECON SHOWER, STAGE 2", "U-06 airlock stage 2",
     "to GY-07", "75 deep seal",
     "SEGREGATED - effluent to TK-01. Number of shower positions is not "
     "recorded anywhere in the project", "[C]/[N]"),
    ("SN-05", "HOSE-DOWN POINT", "Headhouse (-)2.000", "to GY-11",
     "75 deep seal", "Confirmed on the Rev F ground plan", "[C]"),
    ("SN-06", "WC, PEACETIME  (CASE B ONLY)", "U-02 lavatory",
     "DN100 soil - PROVISIONAL", "-",
     "*** ONLY IF CASE B OF OPEN ITEM D2 IS ADOPTED. Not specified, not "
     "sized, not adopted. Fixture count NOT RECORDED anywhere ***", "[U]"),
]
