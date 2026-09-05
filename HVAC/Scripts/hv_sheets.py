"""
hv_sheets.py  --  the HVAC drawing set.

    M-001  HVAC general notes, design basis and legend
    M-101  Underground HVAC / ventilation plan
    M-102  Fresh air and exhaust plan
    M-201  HVAC sections
    M-202  Duct and equipment details
    M-203  Emergency / protective ventilation schematic
"""
import os
import sys
import math

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "Drainage",
                                                "Scripts")))
import mep_dxf as X
import mep_proj as P
import mep_views as V
import hv_data as H

T = X.TXT
OUT = os.path.abspath(os.path.join(HERE, "..", "DXF"))
NOTE, LEAD = 2.4, 4.3
CA, CB, CC = 14.0, 286.0, 558.0
WA, WB, WC = 264.0, 264.0, 268.0
TOP = 552.0


def sheet(num, title, sub, flags=(), of=""):
    return X.Sheet(num, title, sub, package="HVAC", rev=P.REV["hvac"],
                   flags=flags, sheet_of=of)


def sbox(sh, x, y, w, h, lines, layer="M-EQUIP", th=None):
    sh.rect(x, y - h, x + w, y, layer)
    th = th or T["small"]
    n = len(lines)
    for i, s in enumerate(lines):
        sh.text(s, (x + w / 2.0, y - h / 2.0 + (n - 1) * th * 0.85 / 2.0
                    - i * th * 1.7 - th * 0.4), th, "M-TEXT", "CENTER")


def sarrow(sh, p1, p2, layer="M-AIRFLOW"):
    sh.line(p1, p2, layer)
    ang = math.degrees(math.atan2(p2[1] - p1[1], p2[0] - p1[0]))
    sh.flow(((p1[0] + p2[0]) / 2 - math.cos(math.radians(ang)) * 1.2,
             (p1[1] + p2[1]) / 2 - math.sin(math.radians(ang)) * 1.2),
            ang, 2.2, layer)


# =====================================================================
def m001():
    sh = sheet("M-001", "HVAC GENERAL NOTES, DESIGN BASIS AND LEGEND",
               "PROTECTED VENTILATION - 300 m3/h TRUE N+1 - FIVE OPERATING "
               "MODES",
               flags=("HV-F1", "HV-F2", "HV-D1", "HV-D2", "HV-D3", "HV-D4"),
               of="1 OF 6")

    # ---------------- column A
    y = sh.panel(CA, TOP, WA, "1   VENTILATION CONCEPT", [
        "THE SHELTER IS SEALED AND HELD ABOVE ATMOSPHERE.  Everything else",
        "follows from that.",
        "",
        "1  THE ENVELOPE IS THE MACHINE.  217.0 m3 of gas-tight volume across",
        "   bays 1 to 6, leaking no more than 0.15 vol/h at +300 Pa - 32.5 m3/h,",
        "   11 % of one train.  The plant does not have to fight the leakage;",
        "   it has to keep the leak flowing OUTWARD.",
        "",
        "2  TRUE N+1, NOT 2 x 150.  Two 300 m3/h trains, either of which can",
        "   carry the whole duty alone.  A failed train is a maintenance job,",
        "   not an evacuation.",
        "",
        "3  THE AIRLOCK IS THE EXHAUST PATH.  Nothing is supplied to bay 6.  The",
        "   whole 300 m3/h transfers from the clean zone through the three decon",
        "   stages and out through BV-3, which is what makes the confirmed",
        "   0 -> +10 -> +20 -> +35 -> +50 Pa cascade work.",
        "",
        "4  CLOSED MODE IS A BRIDGE, NOT A SURVIVAL MODE.  48 hours on soda",
        "   lime and oxygen against a 96 hour endurance.  The other 48 hours",
        "   REQUIRE the filter trains running.",
        "",
        "5  THE GENERATOR IS OUTSIDE THE ENVELOPE.  BV-4, BV-5 and 2600 m3/h",
        "   serve bay 8 only, behind blast door 2 and W7.  Running it does not",
        "   depressurise the clean zone and does not consume filter life.",
    ], h=NOTE, lead=LEAD)

    sh.text("2   AIR PATH   -   INTAKE / FILTRATION / DISTRIBUTION / CASCADE / EXHAUST",
            (CA, y - 8), T["panel_head"], "M-TITLE")
    sy = y - 16
    xl, xm, xr = CA + 6, CA + 96, CA + 186
    bw, bh = 76, 17
    sbox(sh, xl, sy, bw, bh, ["FRESH-AIR SHAFT SH-1", "600 x 600, GOOSENECK +1.500"],
         "M-DUCT-FRESH")
    sbox(sh, xm, sy, bw, bh, ["BV-1 / BV-2  DN100", "< 2 ms CLOSE, HOLDS 1.3 s"],
         "M-DAMPER")
    sbox(sh, xr, sy, bw, bh, ["RAW-AIR DUCT 200 dia", "*** 11.2 m THROUGH THE"],
         "M-FLAG")
    sh.text("CLEAN ZONE - HV-F2 ***", (xr + bw / 2, sy - bh + 2.0), T["small"],
            "M-FLAG", "CENTER")
    sarrow(sh, (xl + bw, sy - bh / 2), (xm, sy - bh / 2), "M-DUCT-FRESH")
    sarrow(sh, (xm + bw, sy - bh / 2), (xr, sy - bh / 2), "M-DUCT-FRESH")

    sy -= 24
    sbox(sh, xl, sy, bw, bh, ["AHU-1 / AHU-2  BAY 5", "G4/F7 - H14 - CARBON"],
         "M-EQUIP")
    sbox(sh, xm, sy, bw, bh, ["FAN + HAND CRANK", "300 m3/h EACH"], "M-EQUIP")
    sbox(sh, xr, sy, bw, bh, ["PLENUM  +50 to +100 Pa", "SETS EVERY LEAK OUTWARD"],
         "M-EQUIP")
    sarrow(sh, (xr + bw / 2, sy + 24 - bh), (xr + bw / 2, sy), "M-DUCT-FRESH")
    sarrow(sh, (xl + bw, sy - bh / 2), (xm, sy - bh / 2), "M-DUCT-SUPPLY")
    sarrow(sh, (xm + bw, sy - bh / 2), (xr, sy - bh / 2), "M-DUCT-SUPPLY")

    sy -= 24
    sbox(sh, xl, sy, bw, bh, ["SUPPLY TO BAYS 1 TO 5", "240 / 195 / 60 / 30 m3/h"],
         "M-DUCT-SUPPLY")
    sbox(sh, xm, sy, bw, bh, ["CASCADE THROUGH BAY 6", "+50 / +35 / +20 / +10 Pa"],
         "M-DUCT-RETURN")
    sbox(sh, xr, sy, bw, bh, ["BV-3 + OPRV  IN W6", "EXHAUST TO BAY 7"],
         "M-DUCT-EXH")
    sarrow(sh, (xl + bw / 2, sy + 24 - bh), (xl + bw / 2, sy), "M-DUCT-SUPPLY")
    sarrow(sh, (xl + bw, sy - bh / 2), (xm, sy - bh / 2), "M-DUCT-RETURN")
    sarrow(sh, (xm + bw, sy - bh / 2), (xr, sy - bh / 2), "M-DUCT-EXH")
    sh.rect(CA, sy - bh - 6, CA + WA, y - 12, "M-TITLE")

    yA = sh.panel(CA, sy - bh - 10, WA, "3   WHAT LIMITS CLOSED MODE  -  FINDING HV-F1", [
        "unscrubbed, CO2 alone .............................  9.9 h   [C]",
        "with the 40 kg soda-lime store ....................   48 h   [C]",
        "with the 15 m3 oxygen store .......................   80 h   [R]",
        "",
        "THE OXYGEN OUTLASTS THE SCRUBBANT.  THE CONSUMABLE TO COUNT, AND THE",
        "ONE TO WRITE ON THE DRILL CARD, IS SODA LIME.  S-06 does not say this.",
    ], h=NOTE, lead=LEAD)

    # ---------------- column B
    y = sh.panel(CB, TOP, WB, "4   GENERAL NOTES", [
        " 1  ALL DIMENSIONS IN MILLIMETRES, ALL LEVELS IN METRES relative to",
        "    finished site grade 0.000.  Coordinate origin per master A.4.1.",
        " 2  READ WITH  master/MASTER_PROJECT_STATE.md,  sheet S-06,  the Rev F",
        "    architectural set, and the DRAINAGE package (condensate, trap seals).",
        " 3  DO NOT SCALE.  Work to figured dimensions and to the schedules.",
        " 4  EVERY VALUE ON THIS SET CARRIES AN EVIDENCE CLASS.  Nothing marked",
        "    [A], [U] or [N] may be built from without written confirmation.",
        " 5  RECESS EVERY BLAST VALVE - IS 4991 Cl. 6.2.1.  A valve flush in a",
        "    vertical face sees p_r = 1366 kPa, 3.6 x the 383 kPa side-on value:",
        "    131 kN on a DN350 disc instead of 36.8 kN.",
        " 6  KEEP >= 2.0 m OF DUCT BETWEEN EVERY BLAST VALVE AND ITS PLENUM.  At",
        "    50 psi the shock front moves 1.2 m in the 2 ms the valve takes to",
        "    shut; beyond 2.0 m the leak-through is trivial.",
        " 7  A MANUAL QUARTER-TURN GAS-TIGHT DAMPER INBOARD OF EVERY BLAST VALVE,",
        "    operable from inside WITHOUT TOOLS.  It is the crew's last line if a",
        "    valve fails open.",
        " 8  SPECIFY THE HOLD TIME, NOT JUST THE CLOSING TIME.  The nuclear",
        "    positive phase is 0.13-1.33 s.  A valve that reopens at 50 ms is",
        "    useless here.  It must also be rated IN REVERSE for the negative",
        "    phase, about 0.25 p_so = 86 kPa.",
        " 9  EVERY DUCT CROSSING THE ENVELOPE takes a cast-in frame welded to the",
        "    reinforcement cage for EMP continuity, in a 250 RC valve chamber.",
        "10  NO DUCT PENETRATES THE 900 PRESSURE SLAB OR THE 600 MAT.  Every",
        "    crossing is through a wall, at a confirmed blast-valve position.",
        "11  NO DUCT, DIFFUSER OR SUPPORT IS PLACED IN THE MAIN STAIRCASE, its",
        "    flights, its well or its landings.  That geometry is frozen.",
        "12  CONDENSATE from DH-1 and from any cooling coil discharges to the",
        "    clean sump through a 75 mm DEEP-SEAL TRAP with an air gap - it is a",
        "    pressure boundary at +300 Pa.  See DRAINAGE calculation D.6.",
        "13  A FLOW METER AND A DIFFERENTIAL-PRESSURE GAUGE ACROSS EVERY FILTER",
        "    STAGE - 'the only way to know a filter is spent' (S-06).",
    ], h=NOTE, lead=LEAD)

    y = sh.panel(CB, y - 6, WB, "5   TESTING AND COMMISSIONING", [
        "1  Envelope leak test at +300 Pa BEFORE any ceiling or boxing is closed.",
        "   The raw-air duct FA-2 / FA-3 is tested to the SAME standard, not to a",
        "   ductwork standard - see note 6 of M-102.",
        "2  Prove the cascade with a manometer at every stage: +50 / +35 / +20 /",
        "   +10 / 0 Pa, with the airlock doors shut and then in sequence.",
        "3  Balance the two modes: 135 / 45 m3/h on VCD-1 and VCD-2, and record",
        "   BOTH settings on the damper and on the O&M card.",
        "4  Time a real purge of decon stage 1 against the 12.8 min calculation.",
        "   If it is slower, the entry rate of 4-5 persons per hour falls too.",
        "5  Run the hand crank at full duty for 15 minutes with one person, and",
        "   record what it actually takes.  It is a survival provision, not a",
        "   symbol.",
        "6  Record the CLEAN pressure drop of every filter stage at handover -",
        "   it is the datum the dirty reading is judged against.",
    ], h=NOTE, lead=LEAD)

    yB = sh.panel(CB, y - 6, WB, "6   CODES AND STANDARDS", [
        "IN THE MASTER PART G REGISTER  -  quoted:",
        "    FEMA 453           0.25 cfm/ft2; carbon adsorber performance",
        "    EN 1822            HEPA classification H14, 99.995 % at MPPS",
        "    IS 4991:1968       Cl. 6.2.1 reflected pressure and recessing",
        "    MIL-STD-188-125-1  EMP - penetration treatment",
        "    IS 875 (Pt 2)      imposed loads, for duct support reactions",
        "",
        "NOT IN THE REGISTER  -  cited BY TITLE ONLY, no clause quoted:",
        "    IS 3103  industrial ventilation",
        "    ISHRAE / ASHRAE handbooks  ventilation and duct design practice",
        "",
        "*** NO CODE DOCUMENT IS IN THE WORKSPACE (master open item M2).  Air",
        "    properties and the duct roughness used in calculation H.8 are",
        "    standard tabulated values whose source is not in the workspace;",
        "    they are tagged [A] and are NOT attributed to a code. ***",
    ], h=NOTE, lead=LEAD)

    # ---------------- column C
    sh.text("7   DESIGN BASIS   -   every figure reproduced from first principles",
            (CC, TOP - 3.4), T["panel_head"], "M-TITLE")
    y = sh.table(CC, TOP - 8, [104, 62, 76], [
        ("OCCUPANCY", "9 persons", "[C]  S-06"),
        ("DESIGN ENDURANCE", "96 h", "[C]  S-06"),
        ("GAS-TIGHT ENVELOPE", "67.80 m2 / 216.96 m3", "[R]  = S-06's 67.8 / 217.0"),
        ("CLEAN ZONE, bays 1-5", "57.80 m2 / 184.96 m3", "[R]  = S-06's 57.8 / 185.0"),
        ("   = envelope less the airlock", "67.8 - 10.0 = 57.8", "[R]  not stated on S-06"),
        ("SURVIVAL RATE", "5 x 9 = 45 m3/h", "[C]  S-06"),
        ("WORKING SHELTER RATE", "15 x 9 = 135 m3/h", "[C]  S-06"),
        ("FEMA 453, 0.25 cfm/ft2", "264.3 m3/h", "[R]  = S-06's 264"),
        ("DESIGN FLOW", "300 m3/h", "[C]  S-06"),
        ("   per person", "33.3 m3/h", "[R]  2.2 x the working rate"),
        ("CONFIGURATION", "2 x 300, TRUE N+1", "[C]  S-06"),
        ("ACH, whole envelope", "1.38", "[R]"),
        ("ACH, clean zone", "1.62", "[R]"),
        ("LEAKAGE", "0.15 vol/h = 32.5 m3/h", "[R]  = S-06's 32.5, 11 %"),
        ("OVERPRESSURE", "+50 to +100 Pa", "[C]  S-06"),
        ("CASCADE", "0/+10/+20/+35/+50 Pa", "[C]  S-06"),
        ("CO2 AT REST", "9 x 0.02 = 0.18 m3/h", "[C]  S-06"),
        ("TIME TO 1.0 % CO2", "9.9 h in 185 m3", "[R]  = S-06's 9.9"),
        ("SODA LIME", "20 kg/day, 40 kg = 48 h", "[C]  S-06"),
        ("OXYGEN", "4.5 m3/day, 15 m3 = 80 h", "[C] / [R]"),
        ("AIRLOCK PURGE", "5 x 12.8 = 64 m3, 12.8 min", "[R]  = S-06's 13 min"),
        ("ENTRY RATE", "4-5 PERSONS PER HOUR", "[C]  a manning constraint"),
        ("DUCTWORK + PLENUM LOSS", "161 Pa", "[R]  calc H.9"),
        ("TOTAL FAN DUTY", "*** VENDOR DATA REQUIRED ***", "[N]  5 of 8 components"),
        ("COOLING LOAD", "*** NOT CALCULATED ***", "[N]  8 inputs missing"),
    ], header=["PARAMETER", "VALUE", "CLASS AND SOURCE"], h=2.1, rh=6.2,
        layer="M-TABLE")

    sh.text("8   OPEN ITEMS CARRIED ON THIS SET   -   none of them is resolved here",
            (CC, y - 8), T["panel_head"], "M-TITLE")
    yC = sh.table(CC, y - 13, [30, 212], [
        ("HV-F1", "THE SODA LIME, NOT THE OXYGEN, LIMITS CLOSED MODE.  48 h against 80 h."),
        ("", "     Not stated on S-06.  It is the number a shelter commander needs"),
        ("HV-F2", "THE RAW-AIR DUCT RUNS 11.2 m UNFILTERED THROUGH THE CLEAN ZONE,"),
        ("", "     from the bay 1 blast valves to the bay 5 filter trains.  Over that"),
        ("", "     length the duct wall is the ONLY barrier.  Specified as a protective"),
        ("", "     element.  Should the trains move to bay 1?  RAISED, NOT TAKEN"),
        ("HV-D1", "NO FILTER BYPASS FOR PEACETIME RUNNING IS SHOWN ON S-06.  Without"),
        ("", "     one, every peacetime hour spends carbon-bed life.  A bypass adds a"),
        ("", "     leak path - a protective decision.  ENGINEER TO CONFIRM"),
        ("HV-D2", "BV-3 DISCHARGES INTO BAY 7.  The onward path to atmosphere, up the"),
        ("", "     stair shaft and out through the headhouse, is NOT RECORDED"),
        ("HV-D3", "NO COOLING LOAD CAN BE CALCULATED.  Eight inputs are missing, of"),
        ("", "     which the ground temperature at (-)6.100 is the one that governs"),
        ("HV-D4", "NO NOISE CRITERION EXISTS.  Terminal selection cannot be closed"),
        ("HV-D5", "DEHUMIDIFIER DUTY NOT STATED.  The unit is confirmed; the load is not"),
        ("HV-D6", "FAN STATIC PRESSURE - 5 of the 8 loss components are vendor data"),
        ("C16", "ROOF / PLATFORM JUNCTION, master, unresolved.  NO HVAC DEPENDENCY -"),
        ("", "     no duct, plant item or penetration is at that junction"),
        ("A2", "DESIGN GWT (-)2.000 [ASSUMED] - affects the condensate route only"),
    ], header=["REF", "ITEM"], h=2.1, rh=5.8, layer="M-TABLE")

    # ---------------- bottom band
    yy = min(yA, yB, yC) - 10.0
    sh.view_title((CA, yy), "V1", "KEY PLAN  -  PLANT, VALVES AND SHAFTS",
                  "SCALE 1:150   SENTRY POST IS NOT SHOWN - OUTSIDE THIS PACKAGE")
    M = X.vw(150.0, CA + 32, yy - 62.0)
    V.underground_plan(sh, M, 150.0, bays=True, rooms=False, stair=True,
                       esc=True)
    sh.rect(*M(*H.FILTER_T1[:2]), *M(*H.FILTER_T1[2:]), "M-EQUIP")
    sh.rect(*M(*H.FILTER_T2[:2]), *M(*H.FILTER_T2[2:]), "M-EQUIP")
    sh.text("AHU-1 / AHU-2", M(11800, 6600), T["small"], "M-EQUIP", "BC")
    for tag, x, y2 in H.BLAST_VALVE_PTS:
        sh.sym("BVALVE", M(x, y2), scale=0.5)
        sh.text(tag, M(x, y2 - 900), T["small"], "M-DAMPER", "BC")
    sh.rect(*M(*H.GEN_SHAFT[:2]), *M(*H.GEN_SHAFT[2:]), "M-DUCT-FRESH")
    sh.rect(*M(*H.FRESH_SHAFT[:2]), *M(*H.FRESH_SHAFT[2:]), "M-DUCT-FRESH")
    sh.text("SH-1", M(-3300, 900), T["small"], "M-DUCT-FRESH", "BC")
    sh.text("SH-2", M(22900, 900), T["small"], "M-DUCT-FRESH", "BC")
    sh.duct(M(598, 2200), M(11098, 2200), 2.0, "M-FLAG", "FA-2 RAW AIR 11.2 m")

    V.scope_note(sh, CB, yy, WB)
    X.evidence_key(sh, CC, yy)
    sh.finish(scale="NOT TO SCALE", sheet_of="1 OF 6")
    return sh


# =====================================================================
def _plant(sh, M):
    sh.rect(*M(*H.FILTER_T1[:2]), *M(*H.FILTER_T1[2:]), "M-EQUIP")
    sh.text("AHU-1  300 m3/h", M(11823, 5100), NOTE, "M-EQUIP", "BC")
    sh.rect(*M(*H.FILTER_T2[:2]), *M(*H.FILTER_T2[2:]), "M-EQUIP")
    sh.text("AHU-2  300 m3/h", M(11823, 3100), NOTE, "M-EQUIP", "BC")
    sh.text("TRUE N+1", M(11823, 2820), NOTE, "M-EQUIP", "BC")


def m101():
    sh = sheet("M-101", "UNDERGROUND HVAC AND VENTILATION PLAN",
               "SUPPLY - CASCADE - EXHAUST - DAY AND NIGHT BALANCE - "
               "LEVEL (-)6.100",
               flags=("HV-F2", "HV-D3", "HV-D4"), of="2 OF 6")

    sc = 45.0
    M = X.vw(sc, 40.0, 400.0)
    sh.view_title((20, 548), "V1", "UNDERGROUND HVAC PLAN",
                  "SCALE 1:45   DUCTS AT HIGH LEVEL, SOFFIT (-)2.900   "
                  "AIRFLOWS DAY / NIGHT m3/h")
    V.underground_plan(sh, M, sc, bays=True, rooms=True, stair=True, esc=True)
    V.bay_room_labels(sh, M, y=4850, h=NOTE)
    _plant(sh, M)

    # supply main west from the plenum, with branch flows
    sh.duct(M(11098, 4200), M(9800, 4200), 3.0, "M-DUCT-SUPPLY", "SA-1  240")
    sh.duct(M(9800, 4200), M(8000, 4200), 3.0, "M-DUCT-SUPPLY", "SA-2  195")
    sh.duct(M(8000, 4200), M(4900, 4200), 2.2, "M-DUCT-SUPPLY", "SA-3  60")
    sh.duct(M(4900, 4200), M(2600, 4200), 2.2, "M-DUCT-SUPPLY", "SA-4  30")

    term_pos = {"SD-01": (2050, 3600), "SD-02": (4510, 3600),
                "SD-03": (7270, 3600), "SD-04": (10030, 3600),
                "SD-05": (11823, 2200), "EG-01": (4510, 1400)}
    for tag, ty, room, d, n, size, note_, cls in H.TERMINALS:
        if tag in term_pos:
            x, yq = term_pos[tag]
            sh.sym("DIFFUSER" if ty.startswith("SUPPLY DIFF") else "GRILLE",
                   M(x, yq), scale=0.8)
            sh.text(f"{tag}  {d}/{n}", M(x, yq - 700), NOTE, "M-TERMINAL", "BC")
    sh.text("VCD-1", M(7270, 4600), NOTE, "M-DAMPER", "BC")
    sh.text("VCD-2", M(10030, 4600), NOTE, "M-DAMPER", "BC")

    # extract and cascade
    sh.duct(M(4510, 1400), M(12600, 1400), 2.0, "M-DUCT-RETURN", "EA-1  45")
    sh.text("TG-01", M(12700, 3300), NOTE, "M-TERMINAL", "BC")
    for xg in (12700, 13800, 14300):
        sh.flow(M(xg, 3100), 0, 3.0, "M-AIRFLOW")
    sh.text("CASCADE  +50 -> +35 -> +20 -> +10 Pa   300 m3/h TRANSFER",
            M(13800, 2400), NOTE, "M-DUCT-RETURN", "BC")
    sh.sym("BVALVE", M(14998, 4900), scale=0.9)
    sh.text("BV-3 + OPRV  ->  BAY 7", M(15400, 4900), NOTE, "M-DAMPER", "ML")

    sh.dim_h(M(0, -1400), M(22000, -1400), M(0, -2200)[1], sc=sc)

    # ---- V2 transverse section
    s2 = 25.0
    N = X.vw(s2, 548.0, 640.0)
    sh.view_title((550, 548), "V2", "TRANSVERSE SECTION  -  DUCT AT HIGH LEVEL",
                  "SCALE 1:25   BAY 3, LOOKING EAST")
    sh.rect(*N(0, -6700), *N(600, -2900), "M-STRUCT")
    sh.rect(*N(5600, -6700), *N(6200, -2900), "M-STRUCT")
    sh.rect(*N(0, -6700), *N(6200, -6100), "M-STRUCT")
    sh.line(N(600, -2900), N(5600, -2900), "M-STRUCT")
    sh.rect(*N(3500, -3150), *N(3700, -3050), "M-DUCT-SUPPLY")
    sh.text("SA-2  150 x 100", N(3800, -3100), NOTE, "M-DUCT-SUPPLY", "ML")
    sh.sym("DIFFUSER", N(3600, -3350), scale=0.8)
    sh.text("SD-03", N(3800, -3400), NOTE, "M-TERMINAL", "ML")
    sh.dim_v(N(600, -3150), N(600, -6100), N(200, 0)[0], sc=s2)
    sh.text("2950 CLEAR BELOW THE DUCT", N(900, -4600), NOTE, "M-TEXT")
    sh.text("HEADROOM IS NOT A CONSTRAINT: 3200 STRUCTURAL,", N(900, -5000),
            NOTE, "M-TEXT")
    sh.text("2950 UNDER THE DUCT, 2900 UNDER THE DIFFUSER", N(900, -5300),
            NOTE, "M-TEXT")
    V.section_datum(sh, N, -900, 6200, -2.900, "ROOF SOFFIT")
    V.section_datum(sh, N, -900, 6200, -6.100, "FLOOR / TOP OF MAT")

    sh.text("V3   ROOM AIRFLOW SCHEDULE", (550, 300), T["view_title"],
            "M-TITLE")
    sh.table(550, 292, [24, 62, 26, 26, 26, 26], [
        (r, u[:24], f"{v:.1f}", sd, sn, e)
        for r, u, v, sd, sn, e, od, on in H.AIRFLOW],
        header=["ROOM", "USE", "VOL m3", "DAY", "NIGHT", "EXTR"], h=2.1,
        rh=6.0, layer="M-TABLE")

    y = sh.panel(CA, 384, 396, "NOTES  -  UNDERGROUND HVAC", [
        "1  THE 9 OCCUPANTS ARE NOT IN TWO PLACES AT ONCE.  They work in U-03 and sleep in U-04, so the",
        "   distribution is BALANCED IN TWO MODES on VCD-1 and VCD-2: the occupied room of the pair gets",
        "   135 m3/h = 15.0 m3/h per person, EXACTLY the working-shelter rate S-06 names as criterion 2, and",
        "   the other drops to 45 m3/h.  Both modes total 300 m3/h, the confirmed design flow.",
        "2  THE DAMPERS ARE NOT A REFINEMENT.  Holding 15 m3/h/person in BOTH rooms at once would take 270 of",
        "   the 300 m3/h and leave 30 m3/h for the stores, the lavatory AND the plant room.  If a reviewer",
        "   requires that, the total must rise above 300 m3/h - a change to a confirmed value on S-06.",
        "   RAISED, NOT TAKEN.",
        "3  NOTHING IS SUPPLIED TO BAY 6.  The airlock is the exhaust path: the whole 300 m3/h transfers",
        "   through it and out at BV-3, which is what makes the confirmed pressure cascade work.",
        "4  U-02 IS EXTRACTED AT 45 m3/h AGAINST A 30 m3/h SUPPLY so the lavatory runs slightly negative to",
        "   the rest of the clean zone.  The lavatory must not be the source of the cascade.",
        "5  DUCTS RUN AT HIGH LEVEL, tight under the (-)2.900 soffit, on visible supports.  2950 clear remains",
        "   below the largest duct.  NO DUCT IS BOXED IN OR RUN IN A CEILING VOID - in this envelope every",
        "   duct must be inspectable along its whole length.",
        "6  NO DUCT PENETRATES THE 900 PRESSURE SLAB OR THE 600 MAT.  Every crossing of the envelope is",
        "   through a wall at a confirmed blast-valve position.",
        "7  NO DUCT, DIFFUSER OR SUPPORT IS PLACED IN THE MAIN STAIRCASE.  That geometry is frozen.",
        "8  TERMINAL SIZES AND QUANTITIES ARE AN ENGINEERING SELECTION.  NO NOISE CRITERION EXISTS ANYWHERE",
        "   IN THE PROJECT (HV-D4), so throw, NC and terminal pressure drop are not checked.  DATA REQUIRED",
        "   before terminals are ordered - a berthing space for 9 is exactly where a noisy diffuser is felt.",
        "9  CONDENSATE from DH-1 discharges to the clean sump through a 75 mm DEEP-SEAL TRAP with an air gap.",
        "   That trap is a pressure boundary at +300 Pa - see the DRAINAGE package, calculation D.6.",
    ], h=NOTE, lead=LEAD)
    sh.text("V4   DUCT SCHEDULE", (CA, y - 9), T["view_title"], "M-TITLE")
    yD = sh.table(CA, y - 17, [24, 44, 78, 26, 40, 34, 150], [
        (r, sv, ft[:34], q, sz, v, n[:52])
        for r, sv, ft, q, sz, v, n, c in H.DUCTS],
        header=["REF", "SERVICE", "FROM -> TO", "m3/h", "SIZE", "v", "NOTE"],
        h=2.1, rh=5.6, layer="M-TABLE")
    X.evidence_key(sh, CA, yD - 8)
    sh.finish(scale="1:45 / 1:25", sheet_of="2 OF 6")
    return sh


# =====================================================================
def m102():
    sh = sheet("M-102", "FRESH AIR AND EXHAUST PLAN",
               "SHAFTS - BLAST VALVES - THE RAW-AIR DUCT - GENERATOR AIR",
               flags=("HV-F2", "HV-D1", "HV-D2"), of="3 OF 6")

    sc = 55.0
    M = X.vw(sc, 90.0, 400.0)
    sh.view_title((20, 548), "V1", "FRESH AIR AND EXHAUST PLAN",
                  "SCALE 1:55   SHAFTS SHOWN OUTSIDE THE BOX   "
                  "AIRFLOWS IN m3/h")
    V.underground_plan(sh, M, sc, bays=True, rooms=True, stair=True, esc=True)
    _plant(sh, M)

    # shafts
    sh.rect(*M(*H.FRESH_SHAFT[:2]), *M(*H.FRESH_SHAFT[2:]), "M-DUCT-FRESH")
    sh.text("SH-1  600 x 600", M(-3300, 1300), NOTE, "M-DUCT-FRESH", "BC")
    sh.text("GOOSENECK +1.500  [C]", M(-3300, 900), NOTE, "M-DUCT-FRESH", "BC")
    sh.rect(*M(*H.GEN_SHAFT[:2]), *M(*H.GEN_SHAFT[2:]), "M-DUCT-FRESH")
    sh.text("SH-2  600 x 600  [C]", M(22900, 1300), NOTE, "M-DUCT-FRESH", "BC")

    # blast valves and raw air
    for tag, x, yq in H.BLAST_VALVE_PTS:
        sh.sym("BVALVE", M(x, yq), scale=1.0)
        sh.text(tag, M(x, yq + 620), NOTE, "M-DAMPER", "BC")
    sh.duct(M(-3000, 2200), M(598, 2200), 2.4, "M-DUCT-FRESH", "300")
    sh.duct(M(-3000, 4000), M(598, 4000), 2.4, "M-DUCT-FRESH", "300")
    sh.duct(M(598, 2200), M(11098, 2200), 2.6, "M-FLAG",
            "FA-2  RAW, UNFILTERED, 200 dia, 11.2 m  ***  HV-F2  ***")
    sh.duct(M(598, 4000), M(11098, 4000), 2.6, "M-FLAG",
            "FA-3  RAW, UNFILTERED, 200 dia, 11.2 m  ***  HV-F2  ***")
    sh.duct(M(14300, 4900), M(14998, 4900), 2.4, "M-DUCT-EXH", "EA-2  300")
    sh.duct(M(14998, 4900), M(16000, 4900), 2.4, "M-DUCT-EXH", "TO BAY 7")
    sh.duct(M(21398, 1300), M(22598, 1300), 3.0, "M-DUCT-FRESH", "GA-1  2600")
    sh.duct(M(20000, 4700), M(21398, 4700), 3.0, "M-DUCT-EXH", "GA-2  2600")

    sh.dim_h(M(-3600, -1400), M(0, -1400), M(0, -2200)[1], sc=sc)
    sh.text("12.3 m INTAKE TO ENTRY, AGAINST A >= 10 m RULE  [C] S-06",
            M(-3600, -3000), NOTE, "M-TEXT")

    y = sh.panel(CA, 330, 620, "NOTES  -  FRESH AIR AND EXHAUST", [
        "1  ALL FIVE BLAST VALVE POSITIONS ARE CONFIRMED.  They were read out of sheet S-06 by parsing its",
        "   geometry, not assumed:  BV-1 (598, 2200) and BV-2 (598, 4000) in the WEST wall of bay 1;",
        "   BV-3 (14998, 4900) IN W6;  BV-4 (21398, 1300) and BV-5 (21398, 4700) in the EAST wall of bay 8.",
        "2  INTAKE SEPARATION.  12.3 m from the fresh-air intake to the entry, against the >= 10 m rule S-06",
        "   states.  The generator shaft SH-2 is at the OPPOSITE END of the structure, 26 m from SH-1, so",
        "   generator exhaust cannot be drawn into the fresh-air intake in any wind.",
        "3  RECESS EVERY VALVE - IS 4991 Cl. 6.2.1.  Recessed, a DN350 disc sees 36.8 kN; flush in a vertical",
        "   face it sees the reflected 1366 kPa and 131 kN.  A 250 RC valve chamber at every position, with the",
        "   frame cast in and WELDED TO THE REINFORCEMENT CAGE for EMP continuity.",
        "4  >= 2.0 m OF DUCT BETWEEN EVERY VALVE AND ITS PLENUM.  Satisfied more than five times over on the",
        "   fresh-air side, which is the reason the trains are in bay 5 and not against the valves.",
        "5  *** HV-F2 - THE RAW-AIR DUCT IS A PROTECTIVE ELEMENT, NOT A DUCT. ***",
        "   S-06 puts the fresh-air blast valves in the west wall of bay 1 and the NBC filter trains in bay 5.",
        "   Between them the air is UNFILTERED, and FA-2 and FA-3 carry it 11.2 m THROUGH THE CLEAN ZONE - past",
        "   the stores, the lavatory, the ops room and the berths.  Over that length the duct wall is THE ONLY",
        "   BARRIER between the occupied space and unfiltered outside air.  A pinhole in the design event",
        "   admits agent directly into the shelter, downstream of nothing.",
        "   THE POSITIONS ARE NOT CHANGED HERE - they are confirmed on an issued sheet.  THE DUCT IS SPECIFIED",
        "   ACCORDINGLY:  fully welded stainless or heavy-gauge galvanised, NO push-fit and NO slip joints;",
        "   pressure tested to the ENVELOPE standard of +300 Pa and not to a ductwork standard, witnessed,",
        "   before any boxing is closed;  run at high level on visible supports, NOT buried, NOT boxed in, NOT",
        "   in a ceiling void;  labelled RAW AIR - UNFILTERED at not more than 2 m centres;  and re-tested",
        "   after any work in bays 1 to 4.",
        "   THE QUESTION FOR THE PROTECTIVE DESIGNER:  SHOULD THE TRAINS MOVE TO BAY 1, next to the valves?",
        "   Bay 1 is 2900 wide against bay 5's 1560 and already holds ESC 1 and the 1000 L tank.  Moving them",
        "   would remove the raw-air run from the clean zone entirely.  RAISED, NOT TAKEN.",
        "6  HV-D2 - BV-3 DISCHARGES INTO BAY 7, the stair shaft.  The onward path to atmosphere, up the shaft",
        "   and out through the headhouse and the covered stairwell, IS NOT RECORDED ANYWHERE IN THE PROJECT.",
        "   The shaft is not sealed at the top, so a path exists, but its resistance is unknown and it is in",
        "   series with the OPRV.  ENGINEER TO CONFIRM.",
        "7  HV-D1 - NO FILTER BYPASS for peacetime running is shown on S-06.  Without one, every peacetime hour",
        "   spends carbon-bed life that is only replaceable in closed mode.  NOT ADDED HERE: a bypass is a",
        "   deliberate leak path around the filters and that is a protective decision, not a ventilation one.",
    ], h=NOTE, lead=LEAD)
    X.evidence_key(sh, CA, y - 8)
    sh.finish(scale="1:55", sheet_of="3 OF 6")
    return sh


# =====================================================================
def m201():
    sh = sheet("M-201", "HVAC SECTIONS",
               "LONGITUDINAL AND TRANSVERSE - DUCT ZONE, CLEARANCES AND THE "
               "ENVELOPE CROSSINGS",
               flags=("HV-F2",), of="4 OF 6")

    sc = 55.0
    M = X.vw(sc, 40.0, 500.0)
    sh.view_title((20, 548), "V1", "SECTION A-A  -  LONGITUDINAL ON THE AIR PATH",
                  "SCALE 1:55   LEVELS m")
    B = P.BOX
    sh.rect(*M(B["x0"], -2900), *M(B["x1"], -2000), "M-STRUCT")
    sh.rect(*M(B["x0"], -6700), *M(B["x1"], -6100), "M-STRUCT")
    sh.line(M(B["x0"], -2900), M(B["x0"], -6100), "M-STRUCT")
    sh.line(M(B["x1"], -2900), M(B["x1"], -6100), "M-STRUCT")
    for mark, x0, x1, t in P.IW:
        sh.rect(*M(x0, -6100), *M(x1, -2900), "M-STRUCT")
        sh.text(mark, M((x0 + x1) / 2, -2700), NOTE, "M-TEXT", "BC")
    sh.rect(*M(B["x0"], -2000), *M(B["x1"], 0), "M-EXISTING")
    sh.soil_hatch([M(B["x0"], -2000), M(B["x1"], -2000), M(B["x1"], 0),
                   M(B["x0"], 0)])
    sh.text("ENGINEERED COVER 2000  -  NOT PENETRATED BY ANY DUCT",
            M(B["x0"] + 400, -900), NOTE, "M-EXISTING")

    # duct zone
    sh.rect(*M(1400, -3150), *M(11098, -3050), "M-DUCT-SUPPLY")
    sh.text("DUCT ZONE  -  150 DEEP, TIGHT UNDER THE (-)2.900 SOFFIT",
            M(3000, -2980), NOTE, "M-DUCT-SUPPLY")
    sh.rect(*M(598, -3300), *M(1400, -3000), "M-FLAG")
    sh.text("FA-2 RAW", M(700, -3480), NOTE, "M-FLAG")
    sh.rect(*M(11098, -6100), *M(12548, -3400), "M-EQUIP")
    sh.text("AHU-1 / AHU-2", M(11823, -3250), NOTE, "M-EQUIP", "BC")
    sh.sym("BVALVE", M(598, -3150), scale=0.9)
    sh.sym("BVALVE", M(14998, -3400), scale=0.9)
    sh.text("BV-3 IN W6", M(15400, -3400), NOTE, "M-DAMPER", "ML")
    for lev, lab in ((0.000, "GRADE"), (-2.000, "TOP OF SLAB"),
                     (-2.900, "ROOF SOFFIT"), (-6.100, "FLOOR")):
        sh.level(M(B["x1"] + 700, lev * 1000), f"({lev:+.3f})  {lab}")
    sh.dim_v(M(B["x0"] - 500, -3150), M(B["x0"] - 500, -6100),
             M(B["x0"] - 1400, 0)[0], sc=sc)

    # ---- V2 transverse through bay 5
    s2 = 25.0
    N = X.vw(s2, 96.0, 300.0)
    sh.view_title((20, 300), "V2", "SECTION B-B  -  BAY 5, THE PLANT ROOM",
                  "SCALE 1:25   LOOKING EAST")
    sh.rect(*N(0, -6700), *N(600, -2900), "M-STRUCT")
    sh.rect(*N(5600, -6700), *N(6200, -2900), "M-STRUCT")
    sh.rect(*N(0, -6700), *N(6200, -6100), "M-STRUCT")
    sh.line(N(600, -2900), N(5600, -2900), "M-STRUCT")
    sh.rect(*N(1300, -6100), *N(4700, -3600), "M-EQUIP")
    sh.text("AHU-1 ABOVE AHU-2", N(3000, -4800), NOTE, "M-EQUIP", "CENTER")
    sh.text("1450 x 1650 EACH  [C]", N(3000, -5100), NOTE, "M-EQUIP", "CENTER")
    sh.rect(*N(1300, -3400), *N(4700, -3050), "M-EQUIP")
    sh.text("PLENUM  +50 to +100 Pa", N(3000, -3220), NOTE, "M-EQUIP", "CENTER")
    sh.dim_v(N(5000, -3600), N(5000, -3050), N(5500, 0)[0], sc=s2)
    sh.dim_v(N(900, -6100), N(900, -3600), N(400, 0)[0], sc=s2)
    sh.text("*** MAINTENANCE ACCESS ***", N(6400, -3600), NOTE, "M-FLAG")
    sh.text("A FILTER CHANGE NEEDS 800 CLEAR IN FRONT OF EVERY", N(6400, -3900),
            NOTE, "M-FLAG")
    sh.text("CASSETTE FACE AND A CLEAR ROUTE TO BLAST DOOR 1.", N(6400, -4200),
            NOTE, "M-FLAG")
    sh.text("BAY 5 IS 1560 WIDE.  THE 1450 TRAIN LEAVES 110.", N(6400, -4500),
            NOTE, "M-FLAG")
    sh.text("THE ACCESS IS THEREFORE FROM THE 5000 DIRECTION,", N(6400, -4800),
            NOTE, "M-FLAG")
    sh.text("ALONG THE BAY - SEE NOTE 4.", N(6400, -5100), NOTE, "M-FLAG")
    V.section_datum(sh, N, -900, 6200, -2.900, "ROOF SOFFIT")
    V.section_datum(sh, N, -900, 6200, -6.100, "FLOOR")

    y = sh.panel(CA, 160, 620, "NOTES  -  SECTIONS AND CLEARANCES", [
        "1  DUCTS OCCUPY A 150 DEEP ZONE TIGHT UNDER THE (-)2.900 SOFFIT.  2950 clear remains below the",
        "   largest duct against a 3200 structural clear height.  Headroom is not a constraint in this shelter.",
        "2  NOTHING PENETRATES THE 900 PRESSURE SLAB OR THE 600 MAT.  Every envelope crossing is horizontal,",
        "   through a wall, at a confirmed blast-valve position.  This is the same rule the DRAINAGE package",
        "   obeys and for the same reason: the cover over the roof is radiation mass and the membrane over it",
        "   is the tank.",
        "3  DUCTS ARE NOT BOXED IN AND NOT RUN IN A CEILING VOID anywhere in the gas-tight envelope.  Every",
        "   duct, joint and support must be inspectable along its whole length - see M-102 note 5.",
        "4  *** MAINTENANCE ACCESS IS THE TIGHT DIMENSION, NOT HEADROOM. ***  Each NBC train is 1450 wide in a",
        "   bay that is 1560 clear, so there is 110 mm at the sides and the whole of the access has to come",
        "   from the 5000 direction, along the bay.  A HEPA and a carbon cassette have to be carried in through",
        "   blast door 1 (1200 x 2100), along bays 6 and 5, and offered up to the train.  CONFIRM THE CASSETTE",
        "   DIMENSIONS AGAINST THAT ROUTE BEFORE THE TRAINS ARE ORDERED - a filter that cannot be carried to",
        "   its housing is a filter that never gets changed.  [A] this package - a procurement constraint.",
        "5  A FILTER CHANGE IS A CLOSED-MODE OPERATION.  All five valves shut, the shelter on soda lime and",
        "   oxygen, 48 hours available.  That is ample for a change but it is not ample for a change that goes",
        "   wrong, which is the second reason the cassette route must be proved before order.",
        "6  CONDENSATE from the plant falls to the clean sump, which is in this same bay - the shortest",
        "   possible run, through a 75 mm deep-seal trap.  See DRAINAGE D-201 and D-204.",
    ], h=NOTE, lead=LEAD)
    X.evidence_key(sh, CA, y - 8)
    sh.finish(scale="1:55 / 1:25", sheet_of="4 OF 6")
    return sh


# =====================================================================
def m202():
    sh = sheet("M-202", "DUCT AND EQUIPMENT DETAILS",
               "FILTER TRAIN - BLAST VALVE CHAMBER - ENVELOPE CROSSING - "
               "CONDENSATE", of="5 OF 6")

    # ---- D1 filter train elevation
    M = X.vw(20.0, 24.0, 400.0)
    sh.view_title((20, 548), "D1", "NBC FILTER TRAIN  -  ELEVATION",
                  "SCALE 1:20   ONE OF TWO IDENTICAL TRAINS, EACH 300 m3/h")
    x = 0
    for stage, spec, fn, cls in H.FILTERS:
        wd = 420 if stage in ("HEPA", "CARBON") else 300
        sh.rect(*M(x, 0), *M(x + wd, 1400), "M-EQUIP")
        sh.text(stage, M(x + wd / 2, 1550), NOTE, "M-TITLE", "BC")
        sh.text(spec[:22], M(x + wd / 2, 700), T["small"], "M-TEXT", "CENTER")
        if x:
            sh.flow(M(x - 60, 700), 0, 2.4, "M-AIRFLOW")
        x += wd + 120
    sh.text("FLOW METER AND DIFFERENTIAL-PRESSURE GAUGE ACROSS EVERY STAGE  "
            "-  THE ONLY WAY TO KNOW A FILTER IS SPENT  [C] S-06",
            M(0, -400), NOTE, "M-FLAG")
    sh.text("MANUAL QUARTER-TURN GAS-TIGHT DAMPER INBOARD OF EVERY BLAST "
            "VALVE, OPERABLE FROM INSIDE WITHOUT TOOLS  [C] S-06",
            M(0, -800), NOTE, "M-FLAG")
    sh.dim_h(M(0, -1200), M(x - 120, -1200), M(0, -1700)[1], sc=20.0)

    # ---- D2 blast valve chamber
    N = X.vw(10.0, 96.0, 250.0)
    sh.view_title((20, 300), "D2", "BLAST VALVE CHAMBER  -  RECESSED",
                  "SCALE 1:10   IS 4991 Cl. 6.2.1")
    sh.rect(*N(-300, -900), *N(300, 900), "M-STRUCT")
    sh.concrete_hatch([N(-300, -900), N(300, -900), N(300, 900), N(-300, 900)],
                      holes=[[N(-300, -180), N(300, -180), N(300, 180),
                              N(-300, 180)]])
    sh.rect(*N(-560, -420), *N(-300, 420), "M-DAMPER")
    sh.text("250 RC VALVE CHAMBER  -  THE RECESS", N(-560, 560), NOTE,
            "M-DAMPER")
    sh.sym("BVALVE", N(-160, 0), scale=1.2)
    sh.text("BLAST VALVE", N(-160, -560), NOTE, "M-DAMPER", "CENTER")
    sh.sym("VALVE", N(180, 0), scale=1.2)
    sh.text("GAS-TIGHT DAMPER", N(400, 0), NOTE, "M-DAMPER", "ML")
    sh.line(N(300, 0), N(1400, 0), "M-DUCT-FRESH")
    sh.text(">= 2000 OF DUCT TO THE PLENUM", N(500, 240), NOTE,
            "M-DUCT-FRESH")
    sh.text("CAST-IN FRAME WELDED TO THE REINFORCEMENT", N(-560, -720), NOTE,
            "M-FLAG")
    sh.text("CAGE FOR EMP CONTINUITY  [C] S-06", N(-560, -900), NOTE, "M-FLAG")
    sh.dim_h(N(-300, -1100), N(300, -1100), N(0, -1500)[1], sc=10.0)

    sh.panel(300, 300, 190, "WHY THE VALVE IS RECESSED", [
        "RECESSED, the disc sees the SIDE-ON pressure:",
        "    383 kPa x 0.0962 m2  =  36.8 kN on a DN350 disc",
        "FLUSH in a vertical face, it sees the REFLECTED pressure:",
        "  1366 kPa x 0.0962 m2  =  131 kN on the same disc",
        "",
        "3.6 TIMES WORSE.  RECESSING IS NOT COSMETIC.",
        "IS 4991 Cl. 6.2.1.  [C] S-06, reproduced verbatim.",
        "",
        "THE THREE THINGS THE VALVE MUST DO:",
        "  1  CLOSE FAST ENOUGH - < 2 ms.  At 50 psi the front",
        "     moves 1.2 m in that time; keep >= 2.0 m of duct.",
        "  2  STAY SHUT - the positive phase is 0.13 to 1.33 s.",
        "     SPECIFY THE HOLD TIME, not just the closing time.",
        "  3  SURVIVE THE SUCTION - the negative phase pulls the",
        "     disc the other way at about 0.25 p_so = 86 kPa.",
        "     IT MUST BE RATED IN REVERSE.",
    ], h=NOTE, lead=LEAD)

    # ---- D3 condensate
    Q = X.vw(5.0, 530.0, 250.0)
    sh.view_title((524, 300), "D3", "CONDENSATE FROM DH-1", "SCALE 1:5")
    sh.rect(*Q(-300, 200), *Q(300, 700), "M-EQUIP")
    sh.text("DH-1", Q(0, 400), NOTE, "M-EQUIP", "CENTER")
    sh.line(Q(0, 200), Q(0, 40), "P-DRAIN-WASTE")
    sh.text("AIR GAP", Q(60, 100), NOTE, "M-FLAG")
    sh.pline([Q(-160, 40), Q(-160, -300), Q(-60, -400), Q(60, -400),
              Q(160, -300), Q(160, 40)], "P-DRAIN-WASTE")
    sh.line(Q(-160, -160), Q(160, -160), "M-WATERPROOF")
    sh.line(Q(-160, -235), Q(160, -235), "M-WATERPROOF")
    sh.text("75 DEEP SEAL  =  736 Pa", Q(240, -200), NOTE, "M-WATERPROOF", "ML")
    sh.text("2.5 x THE +300 Pa LEAK TEST", Q(240, -380), NOTE,
            "M-WATERPROOF", "ML")
    sh.text("TO THE CLEAN SUMP", Q(240, -560), NOTE, "P-DRAIN-WASTE", "ML")
    sh.text("SEE DRAINAGE D.6", Q(240, -740), NOTE, "P-DRAIN-WASTE", "ML")

    y = sh.panel(CA, 160, 620, "NOTES  -  DETAILS", [
        "1  THE FILTER TRAIN ORDER IS NOT INTERCHANGEABLE.  Louvre, blast valve, pre-filter, HEPA, carbon,",
        "   fan, plenum.  The pre-filter exists to protect the HEPA; the HEPA exists to protect the carbon from",
        "   particulate loading; the carbon is the only stage with a finite consumable life.  Reordering them",
        "   shortens the life of the most expensive one.",
        "2  THE FAN IS DOWNSTREAM OF THE FILTERS, so the filter housings run at negative pressure relative to",
        "   the room and any housing leak draws room air INTO the train, not filtered air out of it.",
        "3  THE HAND CRANK IS NOT A SYMBOL.  It must be sized on the same DIRTY-filter duty as the electric",
        "   drive, and it must be provable by one person for a sustained period.  Commission it - M-001 note 5.",
        "4  EVERY DUCT CROSSING THE ENVELOPE takes a cast-in frame WELDED TO THE REINFORCEMENT CAGE for EMP",
        "   continuity, in a 250 RC valve chamber, with a manual gas-tight damper inboard.  Confirmed on S-06.",
        "5  CONDENSATE.  DH-1 is confirmed in master A.3 but ITS DUTY IS NOT STATED ANYWHERE and no latent load",
        "   or target humidity exists - DATA REQUIRED (HV-D5).  What IS confirmed is that condensate and",
        "   washdown together are 200 L/day in the S-06 drainage flow table, and that they go to the clean",
        "   sump.  The trap on that connection is a PRESSURE BOUNDARY at +300 Pa, not a smell trap.",
        "6  FILTER CHANGE-OUT INTERVAL AND CARBON BED LIFE cannot be stated: they need vendor data AND a",
        "   challenge concentration, and neither exists in the project.  The differential-pressure gauges are",
        "   what make the interval observable rather than assumed.",
    ], h=NOTE, lead=LEAD)
    X.evidence_key(sh, CA, y - 8)
    sh.finish(scale="1:20 / 1:10 / 1:5", sheet_of="5 OF 6")
    return sh


# =====================================================================
def m203():
    sh = sheet("M-203", "EMERGENCY AND PROTECTIVE VENTILATION SCHEMATIC",
               "FIVE MODES - THE PRESSURE CASCADE - CLOSED-MODE CONSUMABLES",
               flags=("HV-F1", "HV-D1"), of="6 OF 6")

    # ---- V1 cascade diagram
    sh.view_title((20, 548), "V1", "THE PRESSURE CASCADE  -  WHY EVERY LEAK "
                  "GOES OUTWARD", "NOT TO SCALE")
    bx, by, bw, bh = 24.0, 520.0, 108.0, 26.0
    stages = [("CLEAN ZONE  BAYS 1-5", "+50 Pa", "184.96 m3  [R]"),
              ("AIRLOCK STAGE 3", "+35 Pa", "2000 x 1500"),
              ("AIRLOCK STAGE 2", "+20 Pa", "2000 x 1500"),
              ("AIRLOCK STAGE 1", "+10 Pa", "2000 x 2000, 12.8 m3"),
              ("BAY 7 / OUTSIDE", "0 Pa", "via BV-3 and the OPRV")]
    for i, (nm, pr, sub) in enumerate(stages):
        lay = "M-EQUIP" if i == 0 else ("M-DUCT-EXH" if i == 4
                                        else "M-DUCT-RETURN")
        sbox(sh, bx, by, bw, bh, [nm, pr, sub], lay, th=NOTE)
        if i:
            sarrow(sh, (bx - 8, by - bh / 2), (bx - 1, by - bh / 2),
                   "M-AIRFLOW")
        bx += bw + 8
    sh.text("300 m3/h TRANSFERS THROUGH THE WHOLE CHAIN.  THE AIRLOCK IS NOT A "
            "DEAD END - IT IS THE EXHAUST PATH.", (24, 484), NOTE, "M-TEXT")
    sh.text("PURGE OF STAGE 1:  5 air changes x 12.8 m3 = 64 m3 at 300 m3/h = "
            "12.8 MINUTES  ->  4-5 PERSONS PER HOUR.  A MANNING CONSTRAINT, "
            "NOT A PLANT FIGURE.", (24, 476), NOTE, "M-FLAG")

    # ---- V2 modes
    sh.text("V2   OPERATING MODES", (CA, 460), T["view_title"], "M-TITLE")
    y = sh.table(CA, 452, [16, 66, 74, 210, 40, 54],
                 [(m, n, wh, wt, f, p) for m, n, wh, wt, f, p in H.MODES],
                 header=["#", "MODE", "WHEN", "WHAT RUNS", "FLOW", "PRESSURE"],
                 h=2.1, rh=7.0, layer="M-TABLE")

    # ---- V3 closed mode consumables
    sh.text("V3   CLOSED MODE  -  WHAT ACTUALLY RUNS OUT FIRST", (CA, y - 9),
            T["view_title"], "M-TITLE")
    y2 = sh.table(CA, y - 17, [110, 46, 46, 160], [
        ("Unscrubbed - CO2 reaches 1.0 %", "9.9 h", "[R] = S-06",
         "(0.0096 x 184.96) / 0.18.  Reproduced exactly"),
        ("Soda lime, 40 kg at 20 kg/day", "48 h", "[C] S-06",
         "*** THE GOVERNING CONSUMABLE ***"),
        ("Oxygen, 15 m3 at 4.5 m3/day", "80 h", "[R]",
         "2 x 50 L at 150 bar.  Outlasts the scrubbant 5:3"),
        ("Design endurance", "96 h", "[C] S-06",
         "Closed mode covers 48 of the 96.  The other 48 REQUIRE filtration"),
    ], header=["CONSUMABLE", "ENDURANCE", "CLASS", "NOTE"], h=2.1, rh=6.4,
        layer="M-TABLE")

    # ---- V4 emergency provisions
    sh.text("V4   EMERGENCY PROVISIONS", (CC, 460), T["view_title"], "M-TITLE")
    sh.table(CC, 452, [96, 146], [
        ("SECOND FILTER TRAIN", "TRUE N+1 - either train carries the whole 300 m3/h  [C]"),
        ("HAND CRANK ON EACH FAN", "Ventilation survives a total power failure  [C]"),
        ("MANUAL GAS-TIGHT DAMPERS", "Inboard of all 5 valves, operable from inside without tools  [C]"),
        ("BLAST VALVES", "Automatic, < 2 ms, no crew action - they work with nobody watching  [C]"),
        ("OPRV WITH BV-3", "Relieves above +100 Pa without opening the envelope  [C]"),
        ("SODA LIME + OXYGEN", "48 h of closed mode with no air movement at all  [C]"),
        ("GENERATOR, BAY 8", "Outside the envelope.  Does not consume filter life  [C]"),
        ("EMERGENCY POWER", "*** NOT DEFINED IN THIS PACKAGE.  The 15 kVA generator is"),
        ("", "confirmed; the distribution, the UPS and the battery autonomy are"),
        ("", "an ELECTRICAL scope item and are not designed here  [N] ***"),
    ], header=["PROVISION", "WHAT IT COVERS"], h=2.1, rh=6.4, layer="M-TABLE")

    yS = sh.panel(CC, 374, 242, "OPERATING SEQUENCE  -  WARNING TO ALL-CLEAR", [
        "1  WARNING RECEIVED.  Switch to mode 2, filtered.  Confirm the plenum",
        "   reaches +50 Pa and the cascade holds at every stage.",
        "2  DETONATION.  The five blast valves shut automatically in under 2 ms",
        "   and hold for the whole positive phase.  NO CREW ACTION IS REQUIRED",
        "   AND NONE IS POSSIBLE.  The shelter is now in mode 3, closed.",
        "3  CLOSED.  Start the soda lime and the oxygen.  48 hours.  Log the",
        "   soda lime, not the oxygen - it is the one that runs out first.",
        "4  WHEN THE OUTSIDE HAZARD ALLOWS, return to mode 2.  The valves",
        "   reopen; confirm the cascade before standing down the scrubbant.",
        "5  ENTRY, at any time in mode 2: purge stage 1, 12.8 minutes per",
        "   cycle, 4-5 persons per hour.  Do not shorten it.",
        "6  ALL-CLEAR.  Mode 1 or 2 by decision.  Change the filters in mode 3.",
        "",
        "*** THIS SEQUENCE IS A COORDINATION DOCUMENT, NOT AN OPERATIONAL",
        "    ORDER.  The drill card is the shelter commander's, and it needs",
        "    the vendor's valve hold times and filter change-out figures, which",
        "    do not exist yet. ***",
    ], h=NOTE, lead=LEAD)

    # ---- V5 single-line schematic
    sh.text("V5   SINGLE-LINE SCHEMATIC  -  THE WHOLE SYSTEM ON ONE LINE",
            (CC, yS - 10), T["view_title"], "M-TITLE")
    bx2, by2 = CC + 4, yS - 22
    for i, (nm, sub, lay) in enumerate([
            ("SH-1 SHAFT", "600 x 600, +1.500", "M-DUCT-FRESH"),
            ("BV-1 / BV-2", "DN100, < 2 ms", "M-DAMPER"),
            ("RAW DUCT 11.2 m", "*** HV-F2 ***", "M-FLAG"),
            ("AHU-1 / AHU-2", "G4/F7 H14 CARBON", "M-EQUIP"),
            ("FAN + CRANK", "300 m3/h", "M-EQUIP"),
            ("PLENUM", "+50 to +100 Pa", "M-EQUIP"),
            ("BAYS 1 TO 5", "240/195/60/30", "M-DUCT-SUPPLY"),
            ("AIRLOCK CASCADE", "+35/+20/+10 Pa", "M-DUCT-RETURN"),
            ("BV-3 + OPRV", "-> BAY 7", "M-DUCT-EXH")]):
        col = i % 3
        row = i // 3
        px = bx2 + col * 80
        py = by2 - row * 22
        sbox(sh, px, py, 72, 16, [nm, sub], lay, th=T["small"])
        if col:
            sarrow(sh, (px - 7, py - 8), (px - 1, py - 8), "M-AIRFLOW")
        elif row:
            sarrow(sh, (bx2 + 2 * 80 + 36, py + 22 - 16), (px + 36, py),
                   "M-AIRFLOW")

    y = sh.panel(CA, y2 - 10, 396, "NOTES  -  EMERGENCY AND PROTECTIVE VENTILATION", [
        "1  HV-F1 - THE SODA LIME, NOT THE OXYGEN, LIMITS CLOSED MODE: 48 h against 80 h, both against an",
        "   unscrubbed 9.9 h.  S-06 gives all three figures but does not draw the conclusion.  IT IS THE NUMBER",
        "   A SHELTER COMMANDER NEEDS, and it belongs on the drill card.",
        "2  CLOSED MODE COVERS 48 OF THE 96 h DESIGN ENDURANCE.  The other 48 h REQUIRE the filter trains to be",
        "   running.  Closed mode is not an alternative to filtration; it is the bridge to it.",
        "3  MODE 5, THE GENERATOR, IS INDEPENDENT OF MODES 1 TO 4.  BV-4, BV-5 and 2600 m3/h serve bay 8 only,",
        "   which is outside the gas-tight envelope behind blast door 2 and W7.  Running the generator does not",
        "   depressurise the clean zone and does not consume filter life.",
        "4  HV-D1 - NO FILTER BYPASS FOR PEACETIME RUNNING IS SHOWN ANYWHERE ON S-06.  Without one, every hour",
        "   of peacetime ventilation spends carbon-bed life that can only be replaced in mode 3.  A bypass is a",
        "   deliberate leak path around the filters: it is a PROTECTIVE decision, not a ventilation one, and it",
        "   is NOT ADDED HERE.  ENGINEER TO CONFIRM.",
        "5  EMERGENCY POWER IS NOT DESIGNED IN THIS PACKAGE.  The 15 kVA generator is confirmed; the",
        "   distribution, the UPS and the battery autonomy behind the fans, the dampers and the alarms are an",
        "   ELECTRICAL scope item.  What this package DOES record is that the hand crank makes ventilation",
        "   independent of all of it.",
        "6  NO NBC OR CBRN EQUIPMENT IS SPECIFIED BEYOND WHAT S-06 ALREADY CARRIES.  The filter train, the five",
        "   blast valves, the CO2/O2 plant and the dehumidifier are all confirmed items.  Nothing has been",
        "   added to that list and no performance beyond the S-06 figures is claimed.",
    ], h=NOTE, lead=LEAD)
    X.evidence_key(sh, CA, y - 8)
    sh.finish(scale="NOT TO SCALE", sheet_of="6 OF 6")
    return sh


SHEETS = [(m001, "M-001_HVAC_General_Notes_and_Design_Basis"),
          (m101, "M-101_Underground_HVAC_Ventilation_Plan"),
          (m102, "M-102_Fresh_Air_and_Exhaust_Plan"),
          (m201, "M-201_HVAC_Sections"),
          (m202, "M-202_Duct_and_Equipment_Details"),
          (m203, "M-203_Emergency_Protective_Ventilation_Schematic")]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, name in SHEETS:
        fn().save(os.path.join(OUT, name + ".dxf"))
        print("  ", name + ".dxf")
