"""
hv_data.py  --  the HVAC system itself: equipment, ducts, terminals, dampers
and filters, one entry per item.  Schedules and drawings are both generated
from this file so a tag on a drawing and a row in a schedule cannot disagree.

CLASS  [C] confirmed  [R] reconstructed  [A] this package  [U] unresolved
       [N] not available - DATA REQUIRED

CONFIRMED POSITIONS parsed out of sheet S-06 (view V1, 1:60, paper origin
92.03 / 420.00):
    NBC filter train 1   X 11098 - 12548   Y 3900 - 5550
    NBC filter train 2   X 11098 - 12548   Y 2700 - 3800
    blast valves         BV-1 (598, 2200)  BV-2 (598, 4000)   west wall, bay 1
                         BV-3 (14998, 4900)                   IN W6
                         BV-4 (21398, 1300) BV-5 (21398, 4700) east wall, bay 8
    generator air shaft  X 22598 - 23198   Y 1750 - 2350   600 x 600, outside
    fresh-air shaft      west of the box, 600 x 600, gooseneck +1.500
"""
FILTER_T1 = (11098, 3900, 12548, 5550)
FILTER_T2 = (11098, 2700, 12548, 3800)
GEN_SHAFT = (22598, 1750, 23198, 2350)
FRESH_SHAFT = (-3600, 1750, -3000, 2350)          # [A] indicative, west of the box
BLAST_VALVE_PTS = [("BV-1", 598, 2200), ("BV-2", 598, 4000),
                   ("BV-3", 14998, 4900), ("BV-4", 21398, 1300),
                   ("BV-5", 21398, 4700)]

INTAKE_TO_ENTRY_M = 12.3       # [C] S-06, against a >= 10 m rule
PLENUM = (11098, 2700, 12548, 5550)   # the two trains discharge into one plenum

# --------------------------------------------------------------- airflow
# room, use, volume m3, supply DAY, supply NIGHT, extract, occ day, occ night
AIRFLOW = [
    ("U-01", "EMERGENCY STORES / ESC 1", 46.40, 30, 30, 0, 0, 0),
    ("U-02", "LAVATORY + MEDICAL", 28.80, 30, 30, 45, 1, 1),
    ("U-03", "OPS ROOM & HAZARD PLOTTING", 56.00, 135, 45, 0, 9, 0),
    ("U-04", "BERTHING - 9 BERTHS", 28.80, 45, 135, 0, 0, 9),
    ("U-05", "CBRN PLANT + SUMP", 24.96, 60, 60, 0, 0, 0),
    ("U-06", "DECON AIRLOCK - transfer + exhaust", 32.00, 0, 0, 300, 0, 0),
]

# ------------------------------------------------------------- equipment
# tag, item, duty, position, notes, class
EQUIPMENT = [
    ("AHU-1", "NBC FILTER TRAIN 1", "300 m3/h",
     "Bay 5, X 11098-12548, Y 3900-5550",
     "Louvre + blast valve + G4/F7 pre-filter + EN 1822 H14 HEPA + ASZM-TEDA "
     "carbon + fan with hand crank + plenum. Carries the WHOLE duty on its "
     "own - TRUE N+1", "[C]"),
    ("AHU-2", "NBC FILTER TRAIN 2", "300 m3/h",
     "Bay 5, X 11098-12548, Y 2700-3800",
     "Identical to AHU-1. Standby", "[C]"),
    ("FAN-1", "SUPPLY FAN, TRAIN 1", "300 m3/h",
     "Within AHU-1",
     "Electric drive PLUS HAND CRANK [C]. Static pressure NOT DERIVABLE - "
     "five of the eight loss components are vendor data (calc H.9)", "[C]/[N]"),
    ("FAN-2", "SUPPLY FAN, TRAIN 2", "300 m3/h", "Within AHU-2",
     "As FAN-1", "[C]/[N]"),
    ("CO2-1", "CO2 SCRUBBER, SODA LIME", "20 kg/day", "Bay 5",
     "40 kg store = 48 h of closed mode. THE SODA LIME, NOT THE O2, IS WHAT "
     "LIMITS CLOSED MODE - finding HV-F1", "[C]"),
    ("O2-1", "OXYGEN STORE", "4.5 m3/day", "Bay 5",
     "2 x 50 L cylinders at 150 bar = 15 m3 = 80 h", "[C]"),
    ("DH-1", "DEHUMIDIFIER", "DUTY NOT STATED", "Bay 5",
     "Confirmed in master A.3. No latent load and no target RH exist "
     "anywhere in the project - DATA REQUIRED. Condensate to the clean sump "
     "through a 75 deep-seal trap", "[C]/[N]"),
    ("GEN-1", "GENERATOR", "15 kVA", "Bay 8, the grey zone",
     "Combustion and cooling air 2600 m3/h through BV-4 / BV-5. Heat "
     "rejection into bay 8 NOT STATED", "[C]/[N]"),
    ("SH-1", "FRESH-AIR SHAFT", "600 x 600", "West of the box",
     "Gooseneck head at +1.500. 12.3 m from the intake to the entry, against "
     "a >= 10 m rule", "[C]"),
    ("SH-2", "GENERATOR AIR SHAFT", "600 x 600", "East of the box, X 22598-23198",
     "Serves BV-4 and BV-5", "[C]"),
]

# ------------------------------------------------------------ blast valves
# (reproduced from mep_proj.BLAST_VALVES with the parsed positions)

# ---------------------------------------------------------------- ducts
# ref, service, from -> to, m3/h, size, area m2, velocity, notes, class
DUCTS = [
    ("FA-1", "FRESH AIR", "SH-1 shaft -> BV-1", 300, "DN100 throat",
     "10.6 m/s", "Blast valve throat. RECESSED - IS 4991 Cl 6.2.1", "[C]"),
    ("FA-2", "FRESH AIR - RAW", "BV-1 -> AHU-1", 300, "200 dia", "2.65 m/s",
     "*** RAW, UNFILTERED, THROUGH THE CLEAN ZONE - 11.2 m. A PROTECTIVE "
     "ELEMENT, NOT A DUCT. See finding HV-F2 ***", "[A]"),
    ("FA-3", "FRESH AIR - RAW", "BV-2 -> AHU-2", 300, "200 dia", "2.65 m/s",
     "As FA-2", "[A]"),
    ("SA-1", "SUPPLY", "Plenum bay 5 -> bay 4", 240, "200 x 100", "3.33 m/s",
     "Worst-case segment flow across both modes", "[A]"),
    ("SA-2", "SUPPLY", "Bay 4 -> bay 3", 195, "150 x 100", "3.61 m/s",
     "Worst-case segment flow", "[A]"),
    ("SA-3", "SUPPLY", "Bay 3 -> bay 2", 60, "100 dia", "2.12 m/s",
     "Size governed by the practical minimum, not by velocity", "[A]"),
    ("SA-4", "SUPPLY", "Bay 2 -> bay 1", 30, "100 dia", "1.06 m/s",
     "Size governed by the practical minimum", "[A]"),
    ("SA-5", "SUPPLY", "Plenum -> U-05", 60, "100 dia", "2.12 m/s", "", "[A]"),
    ("EA-1", "EXTRACT", "U-02 lavatory -> airlock", 45, "100 dia", "1.59 m/s",
     "Keeps the lavatory slightly negative to the rest of the clean zone",
     "[A]"),
    ("EA-2", "EXHAUST", "Airlock -> BV-3 -> bay 7", 300, "DN100 throat",
     "10.6 m/s", "Exhaust AND overpressure relief. Discharges into the stair "
     "shaft; the onward path to atmosphere is NOT RECORDED - HV-D2", "[C]"),
    ("GA-1", "GENERATOR", "SH-2 -> BV-4 -> bay 8", 2600, "DN350 throat",
     "7.5 m/s", "Outside the gas-tight envelope", "[C]"),
    ("GA-2", "GENERATOR", "Bay 8 -> BV-5 -> SH-2", 2600, "DN350 throat",
     "7.5 m/s", "Outside the gas-tight envelope", "[C]"),
]

# ------------------------------------------------------------- terminals
# tag, type, room, m3/h day, m3/h night, size, notes, class
TERMINALS = [
    ("SD-01", "SUPPLY DIFFUSER", "U-01", 30, 30, "150 x 150", "1 No.", "[A]"),
    ("SD-02", "SUPPLY DIFFUSER", "U-02", 30, 30, "150 x 150", "1 No.", "[A]"),
    ("SD-03", "SUPPLY DIFFUSER", "U-03", 135, 45, "225 x 225",
     "2 No. at 67.5 / 22.5 m3/h each, spread over the 3500 bay", "[A]"),
    ("SD-04", "SUPPLY DIFFUSER", "U-04", 45, 135, "225 x 225",
     "2 No. at 22.5 / 67.5 m3/h each, one over each bunk stack", "[A]"),
    ("SD-05", "SUPPLY GRILLE", "U-05", 60, 60, "200 x 150",
     "1 No. Plant room - grille rather than diffuser, throw is irrelevant",
     "[A]"),
    ("EG-01", "EXTRACT GRILLE", "U-02", 45, 45, "200 x 150",
     "1 No. at low level - the lavatory extract", "[A]"),
    ("TG-01", "TRANSFER GRILLE", "U-05 / U-06 in W5", 300, 300, "300 x 200",
     "Cascade path, clean zone -> airlock. GAS-TIGHT SHUT-OFF DAMPER "
     "INTEGRAL", "[A]"),
    ("TG-02", "TRANSFER GRILLE", "airlock stage 3 -> 2", 300, 300, "300 x 200",
     "Cascade +35 -> +20 Pa", "[A]"),
    ("TG-03", "TRANSFER GRILLE", "airlock stage 2 -> 1", 300, 300, "300 x 200",
     "Cascade +20 -> +10 Pa", "[A]"),
]

# --------------------------------------------------------------- dampers
# tag, type, location, function, class
DAMPERS = [
    ("BV-1", "BLAST VALVE DN100", "West wall, bay 1, (598, 2200)",
     "Fresh air train 1. < 2 ms close, holds 1.3 s, 383 kPa recessed, "
     "3.0 kN on the disc", "[C]"),
    ("BV-2", "BLAST VALVE DN100", "West wall, bay 1, (598, 4000)",
     "Fresh air train 2. As BV-1", "[C]"),
    ("BV-3", "BLAST VALVE DN100", "IN W6, (14998, 4900)",
     "Exhaust and overpressure relief, discharging into bay 7", "[C]"),
    ("BV-4", "BLAST VALVE DN350", "East wall, bay 8, (21398, 1300)",
     "Generator intake. 36.8 kN on the disc recessed; 131 kN if flush", "[C]"),
    ("BV-5", "BLAST VALVE DN350", "East wall, bay 8, (21398, 4700)",
     "Generator exhaust. As BV-4", "[C]"),
    ("GD-01", "MANUAL GAS-TIGHT DAMPER", "Inboard of BV-1",
     "Quarter-turn, operable from inside WITHOUT TOOLS", "[C]"),
    ("GD-02", "MANUAL GAS-TIGHT DAMPER", "Inboard of BV-2", "As GD-01", "[C]"),
    ("GD-03", "MANUAL GAS-TIGHT DAMPER", "Inboard of BV-3", "As GD-01", "[C]"),
    ("GD-04", "MANUAL GAS-TIGHT DAMPER", "Inboard of BV-4", "As GD-01", "[C]"),
    ("GD-05", "MANUAL GAS-TIGHT DAMPER", "Inboard of BV-5", "As GD-01", "[C]"),
    ("VCD-1", "VOLUME CONTROL DAMPER", "SD-03 branch, ops room",
     "DAY / NIGHT balancing, 135 / 45 m3/h. Not a refinement - it is what "
     "makes the confirmed 300 m3/h sufficient (calc H.6)", "[A]"),
    ("VCD-2", "VOLUME CONTROL DAMPER", "SD-04 branch, berthing",
     "DAY / NIGHT balancing, 45 / 135 m3/h", "[A]"),
    ("VCD-3", "VOLUME CONTROL DAMPER", "Each remaining branch",
     "Commissioning balance only", "[A]"),
    ("OPRV-1", "OVERPRESSURE RELIEF VALVE", "With BV-3, in W6",
     "Holds the clean zone at +50 to +100 Pa and relieves above it", "[C]"),
]

# --------------------------------------------------------------- filters
# stage, spec, function, class
FILTERS = [
    ("WEATHER LOUVRE", "SAND + DEBRIS TRAP",
     "Keeps rain, dust and debris out of the shaft", "[C]"),
    ("BLAST VALVE", "< 2 ms CLOSE, HOLDS 1.3 s",
     "Not a damper and not crew-operated - it must work with nobody watching",
     "[C]"),
    ("PRE-FILTER", "G4 / F7",
     "Protects the HEPA from coarse dust and extends its life", "[C]"),
    ("HEPA", "EN 1822 H14, 99.995 % at MPPS",
     "Particulate: biological agent, radioactive dust, fallout", "[C]"),
    ("CARBON", "ASZM-TEDA, 300 000 mg.min/m3",
     "Chemical agent vapour. THE STAGE WITH A FINITE, CONSUMABLE LIFE", "[C]"),
    ("FAN", "ELECTRIC + HAND CRANK",
     "The hand crank is the reason ventilation survives a power failure",
     "[C]"),
    ("PLENUM", "+50 to +100 Pa",
     "Sets the overpressure and therefore the direction of every leak", "[C]"),
]

# ------------------------------------------------------- operating modes
MODES = [
    ("1", "NORMAL, UNFILTERED", "peacetime",
     "One train. NO FILTER BYPASS IS SHOWN ON S-06 - see HV-D1",
     "300 m3/h", "atmospheric"),
    ("2", "FILTERED / PROTECTIVE", "CBRN warning to all-clear",
     "One train through the full filter set, second train standby",
     "300 m3/h", "+50 to +100 Pa"),
    ("3", "CLOSED", "detonation to all-clear, or a filter change",
     "All five shut at the shock; BV-4/5 REOPEN for GEN-1 (RC2). 48 h",
     "0", "sealed"),
    ("4", "PURGE", "each entry through the airlock",
     "5 air changes of decon stage 1: 12.8 min, 4-5 persons per hour",
     "300 m3/h", "cascade held"),
    ("5", "GENERATOR RUNNING", "power or battery charging",
     "BV-4 and BV-5 open. Bay 8 only - does NOT touch the gas-tight envelope",
     "2600 m3/h", "bay 8 not pressurised"),
]
