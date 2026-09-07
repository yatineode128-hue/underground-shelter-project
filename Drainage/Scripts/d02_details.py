"""
d02_details.py  --  the drainage sections and details.

    D-204  sump and pumping - plan, section, discharge train, control
    D-301  drainage sections - grade to discharge
    D-304  pipe penetration and waterproofing details
    D-305  septic tank, soak pit and chamber details
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mep_dxf as X
import mep_proj as P
import mep_views as V
import dr_data as D

T = X.TXT
OUT = os.path.abspath(os.path.join(HERE, "..", "DXF"))
NOTE, LEAD = 2.4, 4.3
CA = 14.0


def sheet(num, title, sub, flags=(), of=""):
    return X.Sheet(num, title, sub, package="DRAINAGE",
                   rev=P.REV["drainage"], flags=flags, sheet_of=of)


# =====================================================================
def d204():
    sh = sheet("D-204", "SUMP AND PUMPING",
               "PLAN, SECTION, DISCHARGE TRAIN, CONTROL LEVELS AND THE "
               "ENVELOPE CROSSING",
               flags=("C18", "A8", "DR-F1"), of="8 OF 11")

    # ---- V1 sump plan 1:20
    s1 = 20.0
    M = X.vw(s1, 30.0, 380.0)
    sh.view_title((20, 548), "V1", "SUMP PLAN  -  BAY 5", "SCALE 1:20")
    x0, y0, x1, y1 = D.SUMP_RECT
    sh.rect(*M(x0 - 300, y0 - 300), *M(x1 + 300, y1 + 300), "M-STRUCT")
    sh.rect(*M(x0, y0), *M(x1, y1), "P-EQUIP")
    sh.concrete_hatch([M(x0 - 300, y0 - 300), M(x1 + 300, y0 - 300),
                       M(x1 + 300, y1 + 300), M(x0 - 300, y1 + 300)],
                      holes=[[M(x0, y0), M(x1, y0), M(x1, y1), M(x0, y1)]])
    for i, (px, py) in enumerate(D.SUMP_PUMPS, 1):
        sh.sym("PUMP", M(px, py), scale=1.4)
        sh.text(f"PU-0{i}", M(px, py - 420), NOTE, "P-EQUIP", "BC")
    sh.text("PU-01 DUTY", M(D.SUMP_PUMPS[0][0], y0 - 620), NOTE, "M-TEXT", "BC")
    sh.text("PU-02 STANDBY", M(D.SUMP_PUMPS[1][0], y0 - 620), NOTE, "M-TEXT", "BC")
    sh.text("AUTO-ALTERNATING", M((x0 + x1) / 2, y0 - 900), NOTE, "M-TEXT", "BC")
    sh.sym("CLEANOUT", M(x0 + 200, y1 - 200), scale=1.2)
    sh.text("PU-03 HAND PUMP", M(x0 + 200, y1 - 620), NOTE, "P-EQUIP", "BC")
    sh.text("300 PIT WALLS, T16 @ 150 EF EW, 4-T20 TRIMMERS  [C]",
            M((x0 + x1) / 2, y1 + 520), NOTE, "M-TEXT", "BC")
    sh.dim_h(M(x0, y0 - 500), M(x1, y0 - 500), M(0, y0 - 1200)[1], sc=s1)
    sh.dim_v(M(x1 + 500, y0), M(x1 + 500, y1), M(x1 + 1100, 0)[0], sc=s1)
    sh.pipe([M(x1, 1650), M(x1 + 900, 1650)], "P-DRAIN-RISING", "PD-05 DN50")

    # ---- V2 sump section 1:20
    N = X.vw(s1, 250.0, 700.0)
    sh.view_title((244, 548), "V2", "SUMP SECTION AND CONTROL LEVELS",
                  "SCALE 1:20   LEVELS m")
    sh.rect(*N(0, -8000), *N(2100, -6100), "M-STRUCT")
    sh.rect(*N(300, -7600), *N(1800, -6100), "P-EQUIP")
    sh.concrete_hatch([N(0, -8000), N(2100, -8000), N(2100, -6100), N(0, -6100)],
                      holes=[[N(300, -7600), N(1800, -7600), N(1800, -6100),
                              N(300, -6100)]])
    sh.line(N(-600, -6100), N(0, -6100), "M-STRUCT")
    sh.line(N(2100, -6100), N(2700, -6100), "M-STRUCT")
    sh.line(N(-600, -8000), N(0, -8000), "M-WATERPROOF")
    sh.text("MEMBRANE DRESSED AROUND THE PIT  [C]", N(-600, -8250), NOTE,
            "M-WATERPROOF")
    for lev, lab, lay in ((-6.100, "FLOOR / TOP OF PIT", "M-LEVEL"),
                          (-6.400, "HIGH ALARM   +1200", "M-FLAG"),
                          (-6.700, "PUMP START   +900", "P-EQUIP"),
                          (-7.300, "PUMP STOP    +300", "P-EQUIP"),
                          (-7.600, "INVERT", "M-LEVEL"),
                          (-8.000, "PIT BASE - 400, C18 OPEN", "M-FLAG")):
        sh.dline(N(300, lev * 1000), N(1800, lev * 1000), lay)
        sh.text(f"({lev:+.3f})  {lab}", N(1950, lev * 1000 - 60), NOTE, lay)
    sh.sym("PUMP", N(1050, -7450), scale=1.4)
    sh.pipe([N(1050, -7300), N(1050, -6300), N(2700, -6300)], "P-DRAIN-RISING",
            "PD-05")
    sh.dim_v(N(300, -7600), N(300, -6100), N(-300, 0)[0], sc=s1)

    # ---- V3 discharge train
    sh.view_title((20, 300), "V3", "SUMP DISCHARGE TRAIN  -  IN SERIES, ALL "
                  "INSIDE THE ENVELOPE", "NOT TO SCALE")
    bx = 24.0
    for i, (lab, sub) in enumerate([
            ("SUMP SU-01", "3.375 m3"),
            ("PU-01 / PU-02", "1.5 L/s duty / standby"),
            ("1  ISOLATION VALVE", "maintenance"),
            ("2  GAS-TIGHT NRV", "no backflow into the clean sump"),
            ("3  BLAST CHECK VALVE", "protective component"),
            ("4  DEEP-SEAL TRAP 75", "736 Pa vs the +300 Pa test"),
            ("SERVICE ENTRY PLATE", "the only envelope penetration"),
            ("SK-02 STORM SOAKAWAY", "position not fixed - D3")]):
        sh.rect(bx, 262, bx + 68, 282, "P-EQUIP" if i < 6 else "P-DRAIN-RISING")
        sh.text(lab, (bx + 34, 275), NOTE, "M-TEXT", "CENTER")
        sh.text(sub, (bx + 34, 266), 2.0, "M-TEXT", "CENTER")
        if i:
            sh.flow((bx - 4, 272), 0, 2.6, "P-FLOW")
        bx += 76
    sh.text("*** THE ORDER IS NOT INTERCHANGEABLE.  The gas-tight NRV and the blast check valve are PROTECTIVE "
            "components; the trap is the pressure seal.  Any change to this train is a protective-design change. ***",
            (24, 252), NOTE, "M-FLAG")

    y = sh.panel(CA, 242, 396, "NOTES  -  SUMP AND PUMPING", [
        "1  SUMP GEOMETRY, PUMP DUTY AND CONTROL LEVELS ARE ALL CONFIRMED ON SHEET S-06 and are carried forward",
        "   unchanged: 1500 x 1500 x 1500 = 3.375 m3, invert (-)7.600, 2 No. submersible at 1.5 L/s duty/standby",
        "   auto-alternating plus a hand pump, start +900, stop +300, high alarm +1200 above the invert.",
        "2  STORAGE.  400 L/day inflow against 3375 L gross = 8.44 DAYS.  Working volume between stop and start",
        "   is 2.25 m2 x 0.600 = 1350 L; the duty pump empties it in 15.0 minutes and it refills in 81 hours.",
        "3  DR-F1 - DUTY RATIO 0.31 %.  One start every 3.4 days, and with auto-alternation each pump runs about",
        "   every 6.8 days.  That cycling is fine, but AT THAT DUTY A FAILED STANDBY WOULD NEVER BE DISCOVERED",
        "   BY USE.  A WITNESSED MONTHLY TEST of the standby path AND of the hand pump is required in O&M.",
        "4  ALARM MARGIN.  Start to high alarm is 675 L = 40 HOURS of warning at the design inflow, and there is",
        "   a further 300 mm of freeboard from the alarm to the floor at (-)6.100.",
        "5  RISING MAIN DN50 gives 0.76 m/s at 1.5 L/s - above the 0.75 m/s self-cleansing minimum and below the",
        "   speed at which a rising main hammers.  DN40 (1.19 m/s) is the alternative if more scour is wanted.",
        "   DUCTILE IRON OR STAINLESS, welded or flanged; NO PUSH-FIT JOINT INSIDE THE ENVELOPE.",
        "6  TOTAL PUMP HEAD IS NOT DERIVED HERE.  Static lift is 7.30 m from stop level to grade.  Friction and",
        "   fitting losses need the built route length, and no discharge level is recorded anywhere in the",
        "   project (open item D3).  The DUTY is confirmed; the HEAD must be fixed at procurement.  [N]",
        "7  C18 REMAINS OPEN.  Master F.1 and the A.4.3 levels give a 400 pit base; the text on S-06 says 300.",
        "   400 IS HELD.  The drainage design is unaffected either way - the invert is fixed at (-)7.600 and the",
        "   storage is measured from it.",
        "8  THE PERMANENT SUMP IS NOT A CONSTRUCTION DEWATERING SYSTEM and shall not be used as one.  See",
        "   D-001 note 8 for the master B.3 construction-stage mitigation.",
    ], h=NOTE, lead=LEAD)

    X.evidence_key(sh, CA, y - 8)
    sh.finish(scale="1:20", sheet_of="8 OF 11")
    return sh


# =====================================================================
def d301():
    sh = sheet("D-301", "DRAINAGE SECTIONS  -  GRADE TO DISCHARGE",
               "LONGITUDINAL SECTION ON THE DRAINAGE ROUTE AND THE LEVEL "
               "RELATIONSHIPS",
               flags=("C16", "A2", "DR-D3"), of="9 OF 11")

    sc = 60.0
    M = X.vw(sc, 40.0, 530.0)
    sh.view_title((20, 548), "V1", "SECTION A-A  -  LONGITUDINAL, ON THE "
                  "DRAINAGE ROUTE", "SCALE 1:60   LEVELS m")

    B = P.BOX
    # cover build-up
    sh.rect(*M(B["x0"], -2000), *M(B["x1"], 0), "M-EXISTING")
    sh.soil_hatch([M(B["x0"], -2000), M(B["x1"], -2000), M(B["x1"], 0),
                   M(B["x0"], 0)])
    yy = 0
    for lab, t, g, kpa, fn in P.COVER_BUILDUP:
        sh.dline(M(B["x0"], yy - t), M(B["x1"], yy - t), "M-EXISTING")
        sh.text(f"{t}  {lab}", M(B["x0"] + 500, yy - t / 2 - 60), 2.0,
                "M-EXISTING")
        yy -= t
    sh.text("ENGINEERED COVER 2000 = 40.65 kPa  [C] master A.7.3   -   NOT DRAINED "
            "BY PIPEWORK", M(B["x0"] + 400, 400), NOTE, "M-EXISTING")
    # structure
    sh.rect(*M(B["x0"], -2900), *M(B["x1"], -2000), "M-STRUCT")
    sh.rect(*M(B["x0"], -6700), *M(B["x1"], -6100), "M-STRUCT")
    sh.line(M(B["x0"], -2900), M(B["x0"], -6100), "M-STRUCT")
    sh.line(M(B["x1"], -2900), M(B["x1"], -6100), "M-STRUCT")
    sh.rect(*M(B["x0"], -6800), *M(B["x1"], -6700), "M-EXISTING")
    sh.text("900 PRESSURE SLAB - NOTHING PENETRATES IT",
            M(B["x0"] + 400, -2500), NOTE, "M-STRUCT")
    sh.text("600 MAT", M(B["x0"] + 400, -6400), NOTE, "M-STRUCT")
    # GWT
    sh.dline(M(B["x0"] - 2000, -2000), M(B["x1"] + 800, -2000), "M-WATERPROOF")
    sh.text("DESIGN GWT (-)2.000  [ASSUMED - master A2]",
            M(B["x0"] - 1900, -1800), NOTE, "M-WATERPROOF")
    # tanking
    sh.line(M(B["x0"], -6800), M(B["x1"], -6800), "M-WATERPROOF")
    sh.line(M(B["x0"], -6800), M(B["x0"], -2000), "M-WATERPROOF")
    sh.line(M(B["x1"], -6800), M(B["x1"], -2000), "M-WATERPROOF")
    # floor grading and sump
    sh.pline([M(600, -6047), M(11068, -6075)], "A-FIN-WET")
    sh.text("SPINE FALLS 1:400 EAST  [A]", M(4000, -5900), NOTE, "A-FIN-WET")
    sh.rect(*M(11068, -7600), *M(12568, -6100), "P-EQUIP")
    sh.sym("PUMP", M(11818, -7200), scale=0.9)
    sh.text("SU-01", M(11818, -6900), NOTE, "P-EQUIP", "CENTER")
    sh.pipe([M(11818, -7000), M(11818, -3400)], "P-DRAIN-RISING", "PD-05")
    sh.text("PD-05 RISING MAIN TO THE SERVICE ENTRY PLATE", M(12100, -4200),
            NOTE, "P-DRAIN-RISING")
    sh.dim_v(M(B["x0"] - 700, -2000), M(B["x0"] - 700, 0), M(B["x0"] - 1500, 0)[0], sc=sc)
    sh.dim_v(M(B["x0"] - 700, -2900), M(B["x0"] - 700, -2000), M(B["x0"] - 1500, 0)[0], sc=sc)
    sh.dim_v(M(B["x0"] - 700, -6700), M(B["x0"] - 700, -6100), M(B["x0"] - 1500, 0)[0], sc=sc)
    sh.dim_h(M(B["x0"], -7400), M(B["x1"], -7400), M(0, -8100)[1], sc=sc)

    # levels
    for lev, lab in ((0.000, "FINISHED GRADE, CROWNED, FALLS 1:50 AWAY"),
                     (-2.000, "TOP OF SLAB = HEADHOUSE FLOOR = DESIGN GWT"),
                     (-2.900, "ROOF SOFFIT"),
                     (-6.100, "FLOOR / TOP OF MAT"),
                     (-6.700, "UNDERSIDE OF MAT"),
                     (-7.600, "SUMP INVERT"),
                     (-8.000, "SUMP BASE")):
        sh.level((M(B["x1"] + 900, lev * 1000)), f"({lev:+.3f})  {lab}")

    # ---- V2 discharge schematic in section
    sh.view_title((20, 268), "V2", "DISCHARGE ROUTE IN SECTION  -  WHY THE "
                  "SYSTEM IS PUMPED, NOT GRAVITY", "NOT TO SCALE")
    sh.line((28, 246), (620, 246), "M-EXISTING")
    sh.text("GRADE 0.000", (24, 248), NOTE, "M-EXISTING")
    sh.line((28, 172), (300, 172), "M-STRUCT")
    sh.text("SHELTER FLOOR (-)6.100", (24, 174), NOTE, "M-STRUCT")
    sh.rect(150, 152, 200, 172, "P-EQUIP")
    sh.text("SU-01 (-)7.600", (175, 146), NOTE, "P-EQUIP", "CENTER")
    sh.pipe([(175, 158), (175, 240), (420, 240)], "P-DRAIN-RISING",
            "PD-05 / PD-06  STATIC LIFT 7.30 m")
    sh.rect(420, 216, 480, 246, "P-EQUIP")
    sh.text("SK-02", (450, 230), NOTE, "P-EQUIP", "CENTER")
    sh.text("*** THERE IS NO GRAVITY OUTFALL FROM (-)7.600 ANYWHERE IN THE PROJECT.  Every drop of water that "
            "reaches the clean sump leaves it by pump. ***", (24, 200), NOTE, "M-FLAG")
    sh.text("The design GWT is (-)2.000, so the sump sits 5.6 m BELOW the water table.  This is why the discharge "
            "train carries a gas-tight NRV and a blast check valve", (24, 192), NOTE, "M-TEXT")
    sh.text("as well as an isolation valve: the rising main is a hole through the tank and through the protective "
            "envelope, and it must fail closed.", (24, 184), NOTE, "M-TEXT")

    y = sh.panel(CA, 132, 620, "NOTES  -  SECTIONS", [
        "1  THE STRUCTURE IS A TANK.  The membrane is continuous under the mat, up both external faces and lapped",
        "   to the roof membrane (R-805).  Nothing in this package interrupts it except the sump rising main,",
        "   which crosses at the service entry plate with a puddle-flanged sleeve - see D-304.",
        "2  THE ENGINEERED COVER IS NOT DRAINED BY PIPEWORK.  Surface water sheds at 1:50 and infiltration is",
        "   intercepted by the 150 granular filter layer within the cover and dispersed at the berm toe.",
        "3  THE SUMP SITS 5.6 m BELOW THE DESIGN GROUNDWATER TABLE.  The whole system is pumped; there is no",
        "   gravity outfall from (-)7.600 anywhere in the project and none can be created without a site survey.",
        "4  ALL LEVELS SHOWN ARE FROM master A.4.3 AND ARE CONFIRMED, except the design GWT which is [ASSUMED]",
        "   (master A2) and requires monsoon-season monitoring.",
    ], h=NOTE, lead=LEAD)
    X.evidence_key(sh, CA, y - 8)
    sh.finish(scale="1:60 / NTS", sheet_of="9 OF 11")
    return sh


# =====================================================================
def d304():
    sh = sheet("D-304", "PIPE PENETRATION AND WATERPROOFING DETAILS",
               "THE ONLY ENVELOPE CROSSING - SLEEVES, PUDDLE FLANGES AND "
               "TRAP SEALS",
               flags=("A2",), of="10 OF 11")

    # ---- D1 penetration through the tank
    M = X.vw(10.0, 96.0, 430.0)
    sh.view_title((20, 548), "D1", "PIPE PENETRATION THROUGH THE TANKED WALL",
                  "SCALE 1:10")
    sh.rect(*M(-300, -900), *M(300, 900), "M-STRUCT")
    sh.concrete_hatch([M(-300, -900), M(300, -900), M(300, 900), M(-300, 900)],
                      holes=[[M(-300, -90), M(300, -90), M(300, 90), M(-300, 90)]])
    sh.line(M(-700, 0), M(700, 0), "P-DRAIN-RISING")
    sh.rect(*M(-320, -110), *M(320, 110), "M-STEELWORK" if False else "M-DAMPER")
    sh.rect(*M(-40, -220), *M(40, 220), "M-DAMPER")
    sh.text("CAST-IN SLEEVE WITH A CENTRAL PUDDLE FLANGE", M(400, 300), NOTE,
            "M-DAMPER")
    sh.text("WELDED TO THE REINFORCEMENT CAGE FOR EMP CONTINUITY", M(400, 180),
            NOTE, "M-DAMPER")
    sh.line(M(-300, -900), M(-300, 900), "M-WATERPROOF")
    sh.text("TANKING MEMBRANE DRESSED AND CLAMPED TO THE FLANGE",
            M(-300, 1100), NOTE, "M-WATERPROOF")
    sh.leader([M(-300, 700), M(-260, 1040)], None)
    sh.text("*** WITNESSED BEFORE THE MEMBRANE IS DRESSED.  A PENETRATION THAT",
            M(-300, -1700), NOTE, "M-FLAG")
    sh.text("    FAILS AFTER TANKING CANNOT BE REWORKED FROM INSIDE ***",
            M(-300, -1840), NOTE, "M-FLAG")
    sh.text("PD-05 DN50 RISING MAIN", M(700, -140), NOTE, "P-DRAIN-RISING")
    sh.dim_h(M(-300, -1100), M(300, -1100), M(0, -1400)[1], sc=10.0)

    # ---- D2 service entry plate
    N = X.vw(10.0, 330.0, 430.0)
    sh.view_title((300, 548), "D2", "SERVICE ENTRY PLATE  -  THE ONLY "
                  "PENETRATION OF THE ENVELOPE", "SCALE 1:10")
    sh.rect(*N(-400, -600), *N(400, 600), "M-STRUCT")
    sh.rect(*N(-300, -500), *N(300, 500), "M-DAMPER")
    for r in range(3):
        for c in range(2):
            sh.circle(N(-150 + c * 300, -300 + r * 300), 60 / 10.0, "M-DAMPER")
    sh.text("MCT FRAME WITH EMP MODULES  [C] S-06", N(500, 400), NOTE,
            "M-DAMPER")
    sh.text("SLEEVED PIPES + THE SUMP RISING MAIN", N(500, 260), NOTE,
            "M-DAMPER")
    sh.text("800 x 600 IN THE NORTH WALL AT X 11398-12198  [C]", N(500, 120),
            NOTE, "M-TEXT")
    sh.text("*** THE ONLY PENETRATION OF THE ENVELOPE.", N(500, -120), NOTE,
            "M-FLAG")
    sh.text("    NO SECOND DRAINAGE PENETRATION IS CREATED ***", N(500, -260),
            NOTE, "M-FLAG")
    sh.dim_h(N(-300, -700), N(300, -700), N(0, -1000)[1], sc=10.0)

    # ---- D3 deep-seal trap
    Q = X.vw(5.0, 60.0, 210.0)
    sh.view_title((20, 300), "D3", "DEEP-SEAL TRAP  -  THE PRESSURE SEAL",
                  "SCALE 1:5")
    sh.pline([Q(-200, 300), Q(-200, -100), Q(-60, -240), Q(120, -240),
              Q(260, -100), Q(260, 240)], "P-DRAIN-WASTE")
    sh.pline([Q(-100, 300), Q(-100, -60), Q(-20, -140), Q(60, -140),
              Q(160, -60), Q(160, 240)], "P-DRAIN-WASTE")
    sh.line(Q(-200, 0), Q(260, 0), "M-WATERPROOF")
    sh.line(Q(-200, -75), Q(260, -75), "M-WATERPROOF")
    sh.dim_v(Q(320, -75), Q(320, 0), Q(420, 0)[0], sc=5.0)
    sh.text("75 DEEP SEAL", Q(460, -30), NOTE, "M-WATERPROOF")
    sh.text("HOLDS 736 Pa", Q(460, -160), NOTE, "M-WATERPROOF")

    sh.panel(300, 300, 334, "TRAP SEAL AGAINST SHELTER OVERPRESSURE", [
        "The clean zone is held at +50 to +100 Pa and is leak-tested at +300 Pa",
        "[C] S-06.  A trap inside that zone is a PRESSURE BOUNDARY: a seal",
        "shallower than the overpressure blows through and the shelter vents",
        "to the drain.  1 mm water gauge = 9.81 Pa.",
        "",
        "     50 mm seal   holds  491 Pa    4.9 x operating,  1.6 x test",
        "     75 mm seal   holds  736 Pa    7.4 x operating,  2.5 x test   ADOPTED",
        "    100 mm seal   holds  981 Pa    9.8 x operating,  3.3 x test",
        "",
        "EVERY TRAP INSIDE THE ENVELOPE MUST ALSO BE PRIMED.  An unused floor",
        "gully evaporates dry and then leaks air in both directions, which in a",
        "pressurised CBRN envelope is a breach, not a smell.  Trap primers, or a",
        "written weekly priming task on the O&M card, are mandatory.",
    ], h=NOTE, lead=LEAD)

    y = sh.panel(CA, 132, 620, "NOTES  -  PENETRATIONS AND WATERPROOFING", [
        "1  R-805 GOVERNS THE WATERPROOFING.  Its interface requirements are carried here unchanged: tanking",
        "   membrane on the blinding turned up the external face and lapped to the roof membrane as a continuous",
        "   tank; 100 protection screed over the roof membrane; TWO WATERSTOPS AT EVERY CONSTRUCTION JOINT;",
        "   integral crystalline admixture in the concrete; IS 3370 crack control at 0.2 mm.",
        "2  NO COVER IS REDUCED FOR WATERPROOFING.  The membrane is outside the structural section and adds",
        "   nothing to the cover (R-805).",
        "3  EVERY PIPE CROSSING THE TANK - and in this package there is only one, PD-05 - takes a cast-in sleeve",
        "   with a central puddle flange, welded to the reinforcement cage for EMP continuity, with the membrane",
        "   dressed and clamped to the flange.",
        "4  TEST BEFORE TANKING.  Every sleeve and puddle flange is witnessed by the waterproofing installer",
        "   BEFORE the membrane is dressed to it.  See D-001 note 3 under testing and commissioning.",
    ], h=NOTE, lead=LEAD)
    X.evidence_key(sh, CA, y - 8)
    sh.finish(scale="1:10 / 1:5", sheet_of="10 OF 11")
    return sh


# =====================================================================
def d305():
    sh = sheet("D-305", "SEPTIC TANK, SOAK PIT AND CHAMBER DETAILS",
               "IS 2470 (PARTS 1 AND 2):1985  -  AND THE 2.3 % SHORTFALL "
               "FOUND IN THE SOAK PIT",
               flags=("A7", "DR-C2", "DR-D3"), of="11 OF 11")

    # ---- D1 septic tank section 1:25
    M = X.vw(25.0, 40.0, 520.0)
    sh.view_title((20, 548), "D1", "SEPTIC TANK  -  SECTION", "SCALE 1:25")
    S = P.SEPTIC
    L, Bw, dep = S["l"] * 1000, S["b"] * 1000, S["liquid_depth"] * 1000
    fb = S["freeboard"] * 1000
    sh.rect(*M(-150, -dep - 150), *M(L + 150, fb), "M-STRUCT")
    sh.rect(*M(0, -dep), *M(L, fb), "P-DRAIN-SOIL")
    sh.concrete_hatch([M(-150, -dep - 150), M(L + 150, -dep - 150),
                       M(L + 150, fb), M(-150, fb)],
                      holes=[[M(0, -dep), M(L, -dep), M(L, fb), M(0, fb)]])
    sh.line(M(0, 0), M(L, 0), "M-WATERPROOF")
    sh.text("LIQUID LEVEL", M(L / 2, 60), NOTE, "M-WATERPROOF", "BC")
    bxx = L * 2.0 / 3.0
    sh.line(M(bxx, -dep), M(bxx, fb - 100), "M-STRUCT")
    sh.text("BAFFLE AT 2/3 L  [C] Cl. 6.5", M(bxx + 60, -dep / 2), NOTE,
            "M-TEXT")
    sh.line(M(-500, 0), M(0, 0), "P-DRAIN-SOIL")
    sh.line(M(L, 0), M(L + 500, 0), "P-DRAIN-SOIL")
    sh.text("INLET TEE", M(-500, 140), NOTE, "P-DRAIN-SOIL")
    sh.text("OUTLET TEE", M(L + 120, 140), NOTE, "P-DRAIN-SOIL")
    sh.line(M(L / 2, fb), M(L / 2, fb + 900), "P-DRAIN-VENT")
    sh.text("50 COWLED VENT, >= 2 m ABOVE GRADE  [C] Cl. 6.9",
            M(L / 2 + 80, fb + 700), NOTE, "P-DRAIN-VENT")
    sh.dim_h(M(0, -dep - 400), M(L, -dep - 400), M(0, -dep - 800)[1], sc=25.0)
    sh.dim_v(M(L + 400, -dep), M(L + 400, 0), M(L + 900, 0)[0], sc=25.0)

    # ---- D2 soak pit section 1:25
    N = X.vw(25.0, 250.0, 528.0)
    sh.view_title((244, 548), "D2", "SOAK PIT  -  SECTION", "SCALE 1:25")
    K = P.SOAKPIT
    dia, h = K["dia"] * 1000, K["effective_depth"] * 1000
    sh.rect(*N(0, -h), *N(dia, 0), "P-EQUIP")
    sh.soil_hatch([N(0, -h), N(dia, -h), N(dia, 0), N(0, 0)])
    sh.rect(*N(-150, 0), *N(dia + 150, 300), "M-STRUCT")
    sh.text("RC COVER SLAB  [C]", N(dia + 250, 150), NOTE, "M-STRUCT")
    sh.rect(*N(0, -300), *N(dia, 0), "M-EXISTING")
    sh.text("300 SAND AT THE TOP  [C]", N(dia + 250, -150), NOTE, "M-EXISTING")
    sh.text("40-80 mm BRICKBAT / STONE FILL  [C]", N(dia + 250, -h / 2), NOTE,
            "P-EQUIP")
    for lev in range(1, 4):
        sh.flow(N(-200, -h * lev / 4.0), 180, 2.4, "P-DRAIN-SEEP")
        sh.flow(N(dia + 200, -h * lev / 4.0), 0, 2.4, "P-DRAIN-SEEP")
    sh.text("SIDE AREA ONLY IS COUNTED  -  THE BASE CLOGS  [C]",
            N(-700, -h - 1600), NOTE, "M-TEXT")
    sh.dim_h(N(0, -h - 700), N(dia, -h - 700), N(0, -h - 1100)[1], sc=25.0)
    sh.dim_v(N(dia + 900, -h), N(dia + 900, 0), N(dia + 1400, 0)[0], sc=25.0)

    # ---- D3 inspection chamber 1:25
    Q = X.vw(25.0, 470.0, 520.0)
    sh.view_title((464, 548), "D3", "INSPECTION CHAMBER", "SCALE 1:25")
    sh.rect(*Q(-150, -1200), *Q(750, 150), "M-STRUCT")
    sh.rect(*Q(0, -1050), *Q(600, 0), "P-EQUIP")
    sh.concrete_hatch([Q(-150, -1200), Q(750, -1200), Q(750, 150), Q(-150, 150)],
                      holes=[[Q(0, -1050), Q(600, -1050), Q(600, 0), Q(0, 0)]])
    sh.line(Q(-600, -900), Q(0, -900), "P-DRAIN-STORM")
    sh.line(Q(600, -930), Q(1200, -930), "P-DRAIN-STORM")
    sh.text("600 x 450 IC", Q(300, -1400), NOTE, "M-TEXT", "CENTER")
    sh.text("BENCHING TO THE", Q(800, -700), NOTE, "M-TEXT")
    sh.text("CHANNEL INVERT", Q(800, -840), NOTE, "M-TEXT")
    sh.text("DUCTILE COVER", Q(800, 60), NOTE, "M-TEXT")
    sh.text("POSITION NOT FIXED - NO SITE PLAN  [N] D3", Q(-600, 600), NOTE,
            "M-FLAG")

    # ---- calculation panels
    y = sh.panel(CA, 300, 396, "SEPTIC TANK  -  IS 2470 (Pt 1):1985 RE-CHECK   [every value reproduces S-06 exactly]", [
        "Design population        10   [C] S-06 - 'sentry-post shift crews + shelter maintenance'.  TAKEN VERBATIM,",
        "                              NOT RE-DERIVED.  The sentry post itself is outside this package's scope;",
        "                              only the tank that already exists in the project is carried forward.",
        "Sewage flow              45 lpcd x 10                        =  450 L/day        [C]",
        "Detention 24 h, Cl. 6.2                                      =  450 L            [C]",
        "Sludge, Cl. 6.3          30 L/person/yr x 10 x 2 years        =  600 L            [C]",
        "REQUIRED                 450 + 600                           = 1050 L            [R]",
        "PROVIDED, Table 1        1.50 x 0.75 x 1.00 liquid           = 1125 L            [C]",
        "CHECK                    1125 >= 1050    PASS, margin 7.1 %                      [R]",
        "L/B = 1.50/0.75 = 2.0    Cl. 6.5 wants 2 to 4                  PASS",
        "B = 750 >= 750,  depth 1.00 >= 1.00 m    Cl. 6.6               PASS",
        "Freeboard 300  ->  overall depth 1.30 m.  Two compartments, baffle at 2/3 L, inlet and outlet tees,",
        "50 mm cowled vent >= 2 m above grade (Cl. 6.9).",
    ], h=NOTE, lead=LEAD)

    sh.panel(CA, y - 8, 396, "SOAK PIT  -  IS 2470 (Pt 2):1985 RE-CHECK   *** A SHORTFALL IS FOUND ***", [
        "Effluent to disperse     450 L/day                                                [C]",
        "Design absorption        20 L/m2/day                                              [A] master A7",
        "AREA REQUIRED            450 / 20                            = 22.50 m2           [R]",
        "SIDE AREA  pi.D.h        pi x 2.0 x 3.5                      = 21.99 m2           [R]",
        "CHECK                    21.99  vs  22.50  ->  SHORT BY 0.51 m2  =  2.3 %",
        "",
        "*** DR-C2.  Sheet S-06 prints '22.0 m2  OK' against its own stated requirement of '22.5 m2'.",
        "    21.99 is not >= 22.50.  THIS IS ARITHMETIC, NOT JUDGEMENT.  Either of these closes it:",
        "        (a)  effective depth 3.5 -> 3.6 m, diameter unchanged   ->  22.62 m2,  +0.5 %",
        "        (b)  diameter 2.0 -> 2.1 m, depth unchanged             ->  23.09 m2,  +2.6 %",
        "    NOT RESIZED HERE.  S-06 is an issued sheet and the 20 L/m2/day absorption is itself [ASSUMED].",
        "    A PERCOLATION TEST TO Cl. 4 IS MANDATORY BEFORE CONSTRUCTION and may move the requirement by far",
        "    more than 2.3 %, so re-sizing before the test would be false precision.  USER RULING REQUIRED. ***",
        "",
        "AND THE LARGER RISK, ALREADY IN THE MASTER (K.2 A7): 'Soak pit will not work if lower - LIKELY ON",
        "BASALT.'  If the measured rate is below 20 L/m2/day the answer is not a bigger pit: it is a DISPERSION",
        "TRENCH (Cl. 5) or a SEALED HOLDING TANK emptied on a schedule.  S-06 says the same thing.",
        "",
        "OFFSETS, Cl. 5 and S-06:  >= 15 m from any well,  >= 5 m from the septic tank,  >= 2 m from any",
        "building.  *** THESE CANNOT BE DEMONSTRATED - no site plan, no boundary and no well position exists",
        "anywhere in the project.  DATA REQUIRED (open item D3). ***",
    ], h=NOTE, lead=LEAD)

    sh.panel(430, 300, 204, "STORM SOAKAWAY SK-02  -  SIZED BY THIS PACKAGE", [
        "S-06 sends the clean sump discharge to a 'storm soakaway',",
        "separate from the foul soak pit, but NO SIZE, LEVEL OR",
        "POSITION IS GIVEN FOR IT ANYWHERE IN THE PROJECT.  [N]",
        "",
        "Discharge to disperse   400 L/day                 [R]",
        "Design absorption       20 L/m2/day               [A] A7",
        "AREA REQUIRED           400 / 20   = 20.0 m2      [R]",
        "ADOPTED  2.0 dia x 3.5 effective = 21.99 m2       [A]",
        "CHECK    21.99 >= 20.0   PASS, margin 10 %        [R]",
        "",
        "Same construction as SK-01 - one detail, one cover slab",
        "and one set of materials on site.",
        "",
        "SEPARATION IS ABSOLUTE.  SK-02 takes clean groundwater and",
        "condensate; SK-01 takes septic effluent.  They are never",
        "combined.  S-06: 'STORM SOAKAWAY - CLEAN SUMP DISCHARGE.",
        "SEPARATE FROM FOUL.'",
    ], h=NOTE, lead=LEAD)

    X.evidence_key(sh, 430, 168)
    sh.finish(scale="1:25", sheet_of="11 OF 11")
    return sh


SHEETS = [(d204, "D-204_Sump_and_Pumping"),
          (d301, "D-301_Drainage_Sections"),
          (d304, "D-304_Pipe_Penetration_and_Waterproofing_Details"),
          (d305, "D-305_Septic_Tank_Soak_Pit_and_Chamber_Details")]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, name in SHEETS:
        fn().save(os.path.join(OUT, name + ".dxf"))
        print("  ", name + ".dxf")
