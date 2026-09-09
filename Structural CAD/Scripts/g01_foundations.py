"""g01_foundations.py  --  R-101, R-102, R-103."""
import os, math
import sc_proj as P
import sc_dxflib as D
import sc_views as V
import rebar_data as R
from sc_dxflib import Sheet, vw, TXT

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "DXF", "Foundations"))

MAT_LOADS = [
    "GOVERNING COMBINATION   103 BLAST   (gamma = 1.0, IS 4991 Cl. 10.3.1)",
    "",
    "CASE 2 - SOFT / RED-BOLE ZONE   *** GOVERNS ***",
    "  a 3.0 m band of red-bole or vesicular material removed, worst position",
    "  q = 404.9 kPa blast bearing over a 3.0 m unsupported span",
    "  M = q L2 / 12 = 404.9 x 9 / 12          =  303.7 kNm/m",
    "  d = 600 - 75 - 8                        =  517 mm",
    "  Ast,req (fck,dyn 43.75 / fy,dyn 625)    =  1115 mm2/m",
    "  PROVIDED T16 @ 150 EF EW = 1340         ->  Mu 362.8, UTILISATION 84 %",
    "",
    "CASE 1 - NET UPLIFT (COMB 102)   uplift 46.11 - self 15.0 = 31.1 kPa UP",
    "  Mp = 31.1 x 5.0^2 / 16 = 48.6 kNm/m     NOMINAL, DOES NOT GOVERN",
    "",
    "ONE-WAY SHEAR  V at d from the band edge = 404.9 (1.500 - 0.517) = 398.0 kN/m",
    "  tau_v 0.770  |  tau_c 0.375 (pt 0.259 %, STATIC M35 - IS 4991 Cl. 10.3.1.1)",
    "  tau_c,max 3.70 OK   Vus 204.2   Asv/sv 0.908",
    "  PROVIDED T12 @ 250 x 250 GRID -> 1.810 = 2.0 x REQUIRED",
    "",
    "BEARING  service 58.4 kPa (1.8 % of SBC) · blast 404.9 kPa (12.5 %)",
    "         BEARING GOVERNS NOTHING.",
    "PUNCHING  IS 456 Cl. 31.6 NOT APPLICABLE - no column or pedestal bears on",
    "          the mat; the headhouse walls bear on the ROOF.  DECLARED, NOT IGNORED.",
    "SLIDING / OVERTURNING  not credible mechanisms - reasoned, no spurious factor.",
    "",
    "THICKNESS STUDY  500 -> Ast,req 1407 = 105 % of provided  FAIL",
    "                 600 -> 1115 = 84 %   ADOPTED",
    "                 700 ->  926 = 70 %   ·  800 -> approx 57 %",
    "",
    "MANUAL CALCULATION - NOT DIRECT STAAD OUTPUT.  No STAAD result exists.",
]

FLOTATION = [
    "*** THE CONSTRUCTION STAGE GOVERNS.  THIS IS A DESIGN OUTPUT, NOT A",
    "    CONTRACTOR'S PROBLEM. ***",
    "",
    "STAGE                        WEIGHT   UPLIFT   FoS @(-)2.000  FLOODED TO GL",
    "1 mat cast only              2 009    6 175       0.33 FAIL      0.23 FAIL",
    "2 mat + walls, no roof       4 802    6 175       0.78 FAIL      0.55 FAIL",
    "3 box complete, no backfill  7 528    6 175       1.22 MARGINAL  0.86 FLOATS",
    "4 backfilled + cover        12 453    6 175       2.02 OK        1.41 OK",
    "REQUIRE FoS >= 1.2.   ULS COMB 102 = 0.9 x 12453 /(1.5 x 6175) = 1.21",
    "",
    "MANDATORY MITIGATION",
    "1  CONTINUOUS DEWATERING from the start of excavation until backfill and",
    "   cover are complete.",
    "2  TEMPORARY PRESSURE-RELIEF VALVES / KNOCK-OUT PLUGS IN THE MAT, 6 No.",
    "   as sheet S-02, GROUTED UP ONLY AFTER BACKFILL.",
    "3  PROGRAMME the sub-structure to complete before the monsoon, or bund and",
    "   positively drain with standby pumping and generator back-up.",
    "4  BACKFILL SYMMETRICALLY, IN LAYERS.",
    "",
    "FLOTATION CANNOT BE READ OFF THE STAAD MODEL.  The elastic-mat springs take",
    "TENSION, so the mat never lifts in the model.  This is a HAND CHECK on real",
    "dimensions and real weights.  Anyone who says the analysis shows no uplift",
    "has misunderstood their own model.",
]


def r101():
    sh = Sheet("R-101", "MAT FOUNDATION REINFORCEMENT PLAN",
               "MAT 600 THK · T16 @ 150 EF EW · T12 @ 250 x 250 LINK GRID",
               flags=["A2 GWT ASSUMED", "A4 ks SECOND BOUND NOT RUN", "C17", "C18"])
    sh.sheet_header()
    sc = 50
    Pm = vw(sc, 66, 400)
    sh.rect(*Pm(0, 0), *Pm(22000, 6200), "S-CONCRETE")
    V.box_plan(sh, Pm, sc, show_bays=True, show_openings=False, hatch_walls=False)
    # representative curtain, drawn sparse and declared as diagrammatic
    for x in range(1200, 22000, 1800):
        sh.line(Pm(x, 60), Pm(x, 6140), "S-REBAR-MAIN")
    for y in range(600, 6200, 1400):
        sh.line(Pm(60, y), Pm(21940, y), "S-REBAR-MAIN")
    # true-density patch in Bay 3 so the real spacing is visible
    for x in range(6000, 7801, 150):
        sh.line(Pm(x, 3400), Pm(x, 5200), "S-REBAR-MAIN")
    for y in range(3400, 5201, 150):
        sh.line(Pm(6000, y), Pm(7800, y), "S-REBAR-MAIN")
    sh.rect(*Pm(6000, 3400), *Pm(7800, 5200), "S-REFERENCE")
    sh.leader([Pm(7800, 5200), (250, 534)],
              "TRUE DENSITY PATCH - T16 @ 150 BOTH WAYS, BOTH FACES")
    # sump pit opening
    sh.rect(*Pm(11070, 900), *Pm(12570, 2400), "S-CONCRETE")
    sh.hatch_pat([Pm(11070, 900), Pm(12570, 900), Pm(12570, 2400), Pm(11070, 2400)],
                 "ANSI37", 1.0, 0.0, "S-HATCH")
    for o in (150, 240):
        sh.line(Pm(11070 - o, 700), Pm(11070 - o, 2600), "S-REBAR-SEC")
        sh.line(Pm(12570 + o, 700), Pm(12570 + o, 2600), "S-REBAR-SEC")
    # escape shafts above - reference only
    for nm, cx, cy in P.ESC:
        sh.circle(Pm(cx, cy), P.ESC_CLEAR_D / 2 / sc, "S-REFERENCE")
        sh.text(nm + " OVER", Pm(cx, cy - 1250), TXT["small"], "S-REFERENCE", "CENTER")
    V.dim_box_plan(sh, Pm, sc)
    sh.north((560, 456))
    V.balloon(sh, (108, 446), "F01", Pm(2600, 2600))
    V.balloon(sh, (152, 414), "F02", Pm(4600, 1200))
    V.balloon(sh, (432, 446), "F05", Pm(18600, 2600))
    V.balloon(sh, (474, 522), "F06", Pm(20600, 6140))
    V.balloon(sh, (246, 534), "F07", Pm(9200, 5900))
    V.balloon(sh, (352, 534), "F08", Pm(15000, 5900))
    V.balloon(sh, (330, 452), "F10", Pm(11900, 1700))
    sh.view_title((66, 552), "V1", "MAT FOUNDATION PLAN - REINFORCEMENT", "SCALE 1:50")
    sh.secmark((58, 424), "A")
    sh.secmark((520, 424), "A")
    sh.text("SECTION A-A  ->  R-102", (64, 416), TXT["small"], "S-SECTION")

    # enlarged sump part plan, 1:25, origin shifted so the pit sits at x = 66
    sc2 = 25
    Pm2 = vw(sc2, 66 - 10770 / sc2, 250 - 600 / sc2)
    sh.rect(*Pm2(10770, 600), *Pm2(12870, 2700), "S-CONCRETE")
    sh.rect(*Pm2(11070, 900), *Pm2(12570, 2400), "S-CONCRETE")
    sh.concrete_hatch([Pm2(10770, 600), Pm2(12870, 600), Pm2(12870, 2700), Pm2(10770, 2700)],
                      holes=[[Pm2(11070, 900), Pm2(12570, 900), Pm2(12570, 2400),
                              Pm2(11070, 2400)]])
    for i in range(4):
        o = 130 + i * 80
        sh.line(Pm2(11070 - o, 760), Pm2(11070 - o, 2540), "S-REBAR-SEC")
        sh.line(Pm2(12570 + o, 760), Pm2(12570 + o, 2540), "S-REBAR-SEC")
        sh.line(Pm2(10940, 900 - o), Pm2(12700, 900 - o), "S-REBAR-SEC")
        sh.line(Pm2(10940, 2400 + o), Pm2(12700, 2400 + o), "S-REBAR-SEC")
    sh.dim_h(Pm2(11070, 900), Pm2(12570, 900), Pm2(0, 200)[1], sc2)
    sh.dim_v(Pm2(11070, 900), Pm2(11070, 2400), Pm2(10600, 0)[0], sc2)
    V.balloon(sh, (166, 322), "F10", Pm2(12760, 2480))
    sh.view_title((66, 352), "V2", "SUMP-PIT OPENING IN THE MAT - PART PLAN", "SCALE 1:25")
    sh.text("CLEAN SUMP 1500 x 1500 x 1500 at X 11 070 - 12 570, Y 900 - 2 400",
            (66, 228), TXT["small"], "S-TEXT")
    sh.text("[CONFIRMED from sheet S-06]", (66, 224), TXT["small"], "S-TEXT")

    # QA1: the bar-mark key is 13 marks deep and used to run straight over the
    # bar-schedule extract, which was pinned at a fixed y = 282.  Both blocks
    # are now CHAINED off the height the key actually consumes, so they cannot
    # collide however many marks a sheet nominates.
    ymk = V.markkey(sh, 200, 348, ["F01", "F02", "F03", "F04", "F05", "F06", "F07",
                                   "F08", "F09", "F10", "F11", "F12", "F13"], 235)
    V.loading_panel(sh, 445, 348, 195, MAT_LOADS, TXT["small"], 3.05,
                    heading="MAT - DESIGN BASIS")
    ybs = V.bbs_extract(sh, 200, ymk - 8,
                        ["F01", "F02", "F03", "F04", "F05", "F06", "F07", "F08",
                         "F09", "F10"])
    y = sh.panel(648, 556, 183, "OPEN ITEMS AFFECTING THIS SHEET", [
        "A2  DESIGN GWT (-)2.000 IS [ASSUMED].  Water is two-thirds of",
        "    the lateral load and ALL of the 46.11 kPa uplift.  Monsoon",
        "    monitoring is required before construction.",
        "A4  SUBGRADE MODULUS ks.  The master requires BOTH 100 000 and",
        "    500 000 kN/m3.  ONLY 100 000 EXISTS in any model.  The mat",
        "    steel comes from the soft-band hand case, which does not",
        "    depend on ks - but the ks SENSITIVITY IS NOT DEMONSTRATED.",
        "C17 ENGINEERED COVER 40.65 kPa stated vs 39.15 kPa column sum.",
        "    40.65 HELD.  No effect on mat reinforcement.  NOT CLOSED.",
        "C18 SUMP PIT BASE - master F.1 gives 300 walls / 400 base and",
        "    the levels ((-)7.600 invert to (-)8.000 base) support 400.",
        "    Sheet S-06 text says 300 for both.  400 HELD.  NOT CLOSED.",
        "M1  NO STAAD RESULT EXISTS.  Every action on this sheet is a",
        "    hand calculation.  A plate analysis may redistribute it.",
    ], TXT["small"], 3.05)
    V.loading_panel(sh, 648, y - 6, 183, FLOTATION, TXT["small"], 3.05,
                    heading="FLOTATION - MANDATORY MITIGATION")
    # chained below the schedule extract and stretched to fill the bottom band
    sh.panel_column(200, ybs - 8, 22, 440, [
        ("MAT - CONSTRUCTION REQUIREMENTS THAT ARE DESIGN OUTPUTS", [
        "1  THE HAZARD IS NOT THE BASALT - IT IS THE FLOW CONTACTS.  A single red-bole or",
        "   vesicular seam under the mat produces the differential-support case that SIZES",
        "   the mat.  OVER-EXCAVATE ANY RED-BOLE OR VESICULAR SEAM AT FOUNDING LEVEL AND",
        "   REPLACE WITH M15 LEAN CONCRETE.  This is a requirement, not an option.",
        "2  100 mm M15 BLINDING to (-)6.800 before any reinforcement is placed.  Tanking",
        "   membrane on the blinding, with a protection screed - see R-805.",
        "3  75 mm COVER TO THE BLINDING on cementitious spacers.  No plastic spacer against",
        "   an earth or blinding face.",
        "4  CHAIRS AT NOT MORE THAN 1000 c/c BOTH WAYS to the top curtain.  The T12 link",
        "   grid F05 is structural AND is the curtain spacer system - it is not optional.",
        "5  CONSTRUCTION JOINTS AT APPROXIMATELY 6 m.  REINFORCEMENT FULLY CONTINUOUS.",
        "   Two waterstops and a welded Cu/galv EMP strap at every joint - R-804.",
        "6  DEWATERING, PRESSURE-RELIEF PLUGS, PROGRAMME AND SYMMETRICAL BACKFILL ARE",
        "   MANDATORY - see the flotation panel.  FoS IS 0.33 AT THE MAT-ONLY STAGE.",
        "7  NO BAR MAY BE DISPLACED TO CLEAR A SERVICE.  Any clash is an RFI.",
        ]),
    ])
    sh.titleblock(scale="1:50, 1:25", sheet_of="5 OF 30")
    return sh.save(os.path.join(OUT, "R-101_Mat_Foundation_Reinforcement_Plan.dxf"))


def _mat_wall_section(sh, Pm, sc, with_wall=True):
    """Mat 600 with the wall above, both curtains, link grid, haunch, starters."""
    # blinding + mat
    sh.rect(*Pm(-300, -100), *Pm(3000, 0), "S-CONCRETE-THIN")
    sh.hatch_pat([Pm(-300, -100), Pm(3000, -100), Pm(3000, 0), Pm(-300, 0)],
                 "ANSI31", 1.0, 45, "S-HATCH")
    sh.rect(*Pm(0, 0), *Pm(3000, 600), "S-CONCRETE")
    sh.concrete_hatch([Pm(0, 0), Pm(3000, 0), Pm(3000, 600), Pm(0, 600)])
    # mat curtains
    sh.bar_run(Pm(150, 83), Pm(2900, 83), 150, sc, "S-REBAR-MAIN", 0.7)
    sh.bar_run(Pm(150, 552), Pm(2900, 552), 150, sc, "S-REBAR-MAIN", 0.7)
    sh.line(Pm(75, 83), Pm(2950, 83), "S-REBAR-MAIN")
    sh.line(Pm(75, 552), Pm(2950, 552), "S-REBAR-MAIN")
    # link grid
    for x in range(200, 3000, 250):
        sh.rect(*Pm(x - 60, 75), *Pm(x + 60, 560), "S-REBAR-STIRRUP")
    if with_wall:
        sh.rect(*Pm(0, 600), *Pm(600, 1900), "S-CONCRETE")
        sh.concrete_hatch([Pm(0, 600), Pm(600, 600), Pm(600, 1900), Pm(0, 1900)])
        # haunch 500 x 500
        sh.pline([Pm(600, 600), Pm(1100, 600), Pm(600, 1100)], "S-CONCRETE")
        sh.concrete_hatch([Pm(600, 600), Pm(1100, 600), Pm(600, 1100)])
        # kicker
        sh.dline(Pm(0, 750), Pm(600, 750), "S-HIDDEN")
        sh.text("150 KICKER", Pm(640, 730), TXT["small"], "S-TEXT")
        # starters: 900 leg in the mat, turned up
        for xo in (83, 517):
            sh.pline([Pm(xo + 900, 83 if xo < 300 else 83), Pm(xo, 83), Pm(xo, 1550)],
                     "S-REBAR-TIE")
        # wall verticals
        for xo in (83, 517):
            sh.line(Pm(xo, 750), Pm(xo, 1900), "S-REBAR-MAIN")
        # wall horizontals in section
        sh.bar_run(Pm(83, 800), Pm(83, 1880), 150, sc, "S-REBAR-MAIN", 0.6)
        sh.bar_run(Pm(517, 800), Pm(517, 1880), 150, sc, "S-REBAR-MAIN", 0.6)
        # wall links
        for yy in range(850, 1900, 200):
            sh.rect(*Pm(50, yy - 45), *Pm(550, yy + 45), "S-REBAR-STIRRUP")
        # haunch diagonals
        for i in range(4):
            o = i * 150
            sh.line(Pm(600 + o, 600), Pm(600, 600 + o), "S-REBAR-SEC")
        # waterproofing
        sh.line(Pm(-300, -20), Pm(3000, -20), "S-WATERPROOF")
        sh.text("TANKING MEMBRANE ON 100 M15 BLINDING", Pm(1200, -180),
                TXT["small"], "S-WATERPROOF")


def r102():
    sh = Sheet("R-102", "MAT FOUNDATION SECTIONS",
               "SECTION A-A · MAT EDGE · SUMP PIT · TYPICAL MAT SECTION",
               flags=["A2 GWT ASSUMED"])
    sh.sheet_header()
    sc = 20
    Pm = vw(sc, 60, 380)
    _mat_wall_section(sh, Pm, sc)
    sh.dim_v(Pm(0, 0), Pm(0, 600), Pm(-500, 0)[0], sc)
    sh.dim_v(Pm(0, 600), Pm(0, 1900), Pm(-500, 0)[0], sc)
    sh.dim_h(Pm(0, 0), Pm(600, 0), Pm(0, -400)[1], sc)
    sh.level(Pm(1800, 600), "(-)6.100  MAT TOP / INTERNAL FLOOR")
    sh.level(Pm(2400, 0), "(-)6.700  MAT SOFFIT")
    sh.leader([Pm(1400, 83), (222, 392)], "F01 / F02  T16 @ 150 BOTTOM EW")
    sh.leader([Pm(1400, 552), (222, 412)], "F03 / F04  T16 @ 150 TOP EW")
    sh.leader([Pm(950, 300), (222, 402)], "F05  T12 CLOSED LINKS @ 250 x 250")
    sh.leader([Pm(84, 1100), (222, 462)], "F07  T16 @ 150 EF STARTERS, 900 LEG")
    sh.leader([Pm(830, 830), (222, 442)], "W06  T20 @ 150 HAUNCH DIAGONALS, 500 x 500")
    sh.leader([Pm(84, 1600), (222, 472)], "W01 / W02  T16 @ 150 EF VERTICAL")
    sh.view_title((60, 548), "V1", "SECTION A-A  -  MAT / PERIMETER WALL JUNCTION", "SCALE 1:20")

    # V2 mat edge at 1:10
    sc2 = 10
    Pm2 = vw(sc2, 300, 400)
    sh.rect(*Pm2(0, 0), *Pm2(900, 600), "S-CONCRETE")
    sh.concrete_hatch([Pm2(0, 0), Pm2(900, 0), Pm2(900, 600), Pm2(0, 600)])
    sh.rect(*Pm2(-200, -100), *Pm2(900, 0), "S-CONCRETE-THIN")
    sh.bar_run(Pm2(150, 83), Pm2(850, 83), 150, sc2, "S-REBAR-MAIN", 0.8)
    sh.bar_run(Pm2(150, 552), Pm2(850, 552), 150, sc2, "S-REBAR-MAIN", 0.8)
    sh.pline([Pm2(690, 83), Pm2(50, 83), Pm2(50, 552), Pm2(690, 552)], "S-REBAR-SEC")
    sh.line(Pm2(-200, -20), Pm2(900, -20), "S-WATERPROOF")
    sh.pline([Pm2(0, 0), Pm2(0, 600)], "S-WATERPROOF")
    sh.dim_v(Pm2(0, 0), Pm2(0, 600), Pm2(-350, 0)[0], sc2)
    sh.leader([Pm2(120, 320), (312, 480)], "F06  T16 @ 150 U-BAR CLOSING BOTH CURTAINS")
    sh.leader([Pm2(500, -20), (352, 356)], "TANKING MEMBRANE, TURNED UP THE EDGE")
    sh.text("50 COVER TO THE FORMED EDGE   ·   75 TO THE BLINDING",
            Pm2(0, -260), TXT["small"], "S-TEXT")
    sh.view_title((300, 548), "V2", "MAT EDGE AND WATERPROOFING INTERFACE", "SCALE 1:10")

    # V3 sump pit section 1:25
    sc3 = 25
    Pm3 = vw(sc3, 460, 300)
    sh.rect(*Pm3(0, 0), *Pm3(2100, 400), "S-CONCRETE")
    sh.rect(*Pm3(0, 400), *Pm3(300, 1900), "S-CONCRETE")
    sh.rect(*Pm3(1800, 400), *Pm3(2100, 1900), "S-CONCRETE")
    for pts in ([Pm3(0, 0), Pm3(2100, 0), Pm3(2100, 400), Pm3(0, 400)],
                [Pm3(0, 400), Pm3(300, 400), Pm3(300, 1900), Pm3(0, 1900)],
                [Pm3(1800, 400), Pm3(2100, 400), Pm3(2100, 1900), Pm3(1800, 1900)]):
        sh.concrete_hatch(pts)
    sh.rect(*Pm3(-900, 1900), *Pm3(0, 2500), "S-CONCRETE")
    sh.rect(*Pm3(2100, 1900), *Pm3(3000, 2500), "S-CONCRETE")
    sh.concrete_hatch([Pm3(-900, 1900), Pm3(0, 1900), Pm3(0, 2500), Pm3(-900, 2500)])
    sh.concrete_hatch([Pm3(2100, 1900), Pm3(3000, 1900), Pm3(3000, 2500), Pm3(2100, 2500)])
    for xo in (50, 250):
        sh.line(Pm3(xo, 450), Pm3(xo, 1900), "S-REBAR-MAIN")
        sh.line(Pm3(2100 - xo, 450), Pm3(2100 - xo, 1900), "S-REBAR-MAIN")
    sh.bar_run(Pm3(150, 50), Pm3(1950, 50), 150, sc3, "S-REBAR-MAIN", 0.6)
    sh.bar_run(Pm3(150, 350), Pm3(1950, 350), 150, sc3, "S-REBAR-MAIN", 0.6)
    sh.level(Pm3(1050, 1900), "(-)6.100")
    sh.level(Pm3(1050, 400), "(-)7.600 INVERT")
    sh.level(Pm3(1050, 0), "(-)8.000 BASE")
    sh.dim_v(Pm3(2100, 0), Pm3(2100, 400), Pm3(3200, 0)[0], sc3)
    sh.dim_v(Pm3(2100, 400), Pm3(2100, 1900), Pm3(3200, 0)[0], sc3)
    sh.dim_h(Pm3(300, 0), Pm3(1800, 0), Pm3(0, -400)[1], sc3)
    sh.leader([Pm3(150, 1200), (476, 348)], "F11 / F12  T16 @ 150 EF EW PIT WALLS")
    sh.leader([Pm3(1000, 200), (476, 258)], "F13  T16 @ 150 EF EW PIT BASE")
    sh.view_title((460, 400), "V3", "SUMP-PIT SECTION", "SCALE 1:25")
    sh.text("*** C18 OPEN: master F.1 gives walls 300 / base 400 and the levels support 400;",
            (460, 250), TXT["small"], "S-BLAST")
    sh.text("    sheet S-06 text says 300 for both.  400 HELD.  NOT CLOSED. ***",
            (460, 246), TXT["small"], "S-BLAST")

    y = V.materials_panel(sh, 648, 548, 183)
    V.bbs_extract(sh, 648, y - 8, ["F01", "F02", "F03", "F04", "F05", "F06",
                                   "F11", "F12", "F13"])
    sh.panel(60, 210, 380, "MAT SECTION - WHAT THE SECTION MUST SHOW", [
        "1  BOTH CURTAINS AT 150 BOTH WAYS.  The 150 spacing is the EMP maximum,",
        "   not a strength requirement - it is stricter than every code minimum.",
        "2  THE T12 @ 250 x 250 CLOSED-LINK GRID IS STRUCTURAL.  It comes from the",
        "   one-way shear check at the soft-band edge (tau_v 0.770 > tau_c 0.375),",
        "   which the Phase 1 report did not carry out (conflict C6).  It also",
        "   doubles as the spacer system between the curtains.",
        "3  WALL STARTERS F07 HAVE A 900 mm HORIZONTAL LEG IN THE BOTTOM CURTAIN,",
        "   turned up and lapped 800 (50 phi) above a 150 kicker.",
        "4  500 x 500 HAUNCH WITH T20 @ 150 DIAGONALS AT EVERY WALL / MAT JUNCTION.",
        "5  REINFORCEMENT IS FULLY CONTINUOUS THROUGH EVERY CONSTRUCTION JOINT.",
        "   Two waterstops and a welded Cu/galv EMP strap at every joint - R-804.",
        "6  75 COVER TO THE BLINDING, 50 TO A FORMED EDGE, 40 INTERNAL.  The 5 mm",
        "   reduction IS 456 Table 16 permits for M35 IS DELIBERATELY NOT TAKEN.",
    ], TXT["small"], 3.1)
    sh.titleblock(scale="1:20, 1:10, 1:25", sheet_of="6 OF 30")
    return sh.save(os.path.join(OUT, "R-102_Mat_Foundation_Sections.dxf"))


def r103():
    sh = Sheet("R-103", "FOUNDATION / WALL JUNCTION DETAILS",
               "STARTERS · HAUNCHES · EDGE U-BARS · SUMP TRIMMERS")
    sh.sheet_header()

    # D1 perimeter wall starter, 1:10
    sc = 10
    Pm = vw(sc, 55, 330)
    sh.rect(*Pm(0, 0), *Pm(1800, 600), "S-CONCRETE")
    sh.concrete_hatch([Pm(0, 0), Pm(1800, 0), Pm(1800, 600), Pm(0, 600)])
    sh.rect(*Pm(0, 600), *Pm(600, 1800), "S-CONCRETE")
    sh.concrete_hatch([Pm(0, 600), Pm(600, 600), Pm(600, 1800), Pm(0, 1800)])
    sh.dline(Pm(0, 750), Pm(600, 750), "S-HIDDEN")
    for xo in (83, 517):
        sh.pline([Pm(xo + 900, 83), Pm(xo, 83), Pm(xo, 1550)], "S-REBAR-TIE")
        sh.line(Pm(xo, 750), Pm(xo, 1800), "S-REBAR-MAIN")
    sh.bar_run(Pm(150, 83), Pm(1750, 83), 150, sc, "S-REBAR-MAIN", 0.8)
    sh.bar_run(Pm(150, 552), Pm(1750, 552), 150, sc, "S-REBAR-MAIN", 0.8)
    sh.dim_h(Pm(83, 83), Pm(983, 83), Pm(0, -180)[1], sc)
    sh.text("900 HORIZONTAL LEG", Pm(200, -320), TXT["small"], "S-TEXT")
    sh.dim_v(Pm(600, 750), Pm(600, 1550), Pm(1000, 0)[0], sc)
    sh.text("LAP 800 = 50 phi", Pm(1100, 1100), TXT["small"], "S-TEXT")
    sh.text("150 KICKER", Pm(700, 660), TXT["small"], "S-TEXT")
    sh.barmark((150, 300), "F07", "T16 @ 150 EACH FACE", leader_from=Pm(300, 900))
    sh.view_title((55, 548), "D1", "PERIMETER WALL STARTER AND KICKER", "SCALE 1:10")

    # D2 haunch detail 1:10
    Pm2 = vw(sc, 250, 330)
    sh.rect(*Pm2(0, 0), *Pm2(1600, 600), "S-CONCRETE")
    sh.rect(*Pm2(0, 600), *Pm2(600, 1800), "S-CONCRETE")
    sh.pline([Pm2(600, 600), Pm2(1100, 600), Pm2(600, 1100)], "S-CONCRETE")
    for pts in ([Pm2(0, 0), Pm2(1600, 0), Pm2(1600, 600), Pm2(0, 600)],
                [Pm2(0, 600), Pm2(600, 600), Pm2(600, 1800), Pm2(0, 1800)],
                [Pm2(600, 600), Pm2(1100, 600), Pm2(600, 1100)]):
        sh.concrete_hatch(pts)
    for i in range(4):
        o = i * 150
        sh.line(Pm2(600 + o, 600 - 60), Pm2(600 - 60, 600 + o), "S-REBAR-SEC")
    sh.bar_run(Pm2(150, 552), Pm2(1550, 552), 150, sc, "S-REBAR-MAIN", 0.8)
    sh.line(Pm2(83, 700), Pm2(83, 1800), "S-REBAR-MAIN")
    sh.line(Pm2(517, 700), Pm2(517, 1800), "S-REBAR-MAIN")
    sh.dim_h(Pm2(600, 600), Pm2(1100, 600), Pm2(0, -180)[1], sc)
    sh.dim_v(Pm2(1300, 600), Pm2(1300, 1100), Pm2(1400, 0)[0], sc)
    sh.barmark((330, 300), "W06", "T20 @ 150 DIAGONALS", leader_from=Pm2(800, 800))
    sh.view_title((250, 548), "D2", "500 x 500 HAUNCH - WALL / MAT AND WALL / ROOF",
                  "SCALE 1:10")

    # D3 W6/W7 starter
    Pm3 = vw(sc, 440, 330)
    sh.rect(*Pm3(0, 0), *Pm3(1600, 600), "S-CONCRETE")
    sh.rect(*Pm3(500, 600), *Pm3(900, 1800), "S-CONCRETE")
    sh.concrete_hatch([Pm3(0, 0), Pm3(1600, 0), Pm3(1600, 600), Pm3(0, 600)])
    sh.concrete_hatch([Pm3(500, 600), Pm3(900, 600), Pm3(900, 1800), Pm3(500, 1800)])
    for xo in (558, 842):
        sh.pline([Pm3(xo - 900 if xo < 700 else xo + 900, 83), Pm3(xo, 83),
                  Pm3(xo, 1750)], "S-REBAR-TIE")
        sh.line(Pm3(xo, 750), Pm3(xo, 1800), "S-REBAR-MAIN")
    sh.bar_run(Pm3(150, 83), Pm3(1550, 83), 150, sc, "S-REBAR-MAIN", 0.8)
    sh.bar_run(Pm3(150, 552), Pm3(1550, 552), 150, sc, "S-REBAR-MAIN", 0.8)
    sh.dim_h(Pm3(500, 600), Pm3(900, 600), Pm3(0, 900)[1], sc)
    sh.text("400 - MOD M1", Pm3(950, 900), TXT["small"], "S-BLAST")
    sh.barmark((520, 300), "F08", "T20 @ 150 EF, LAP 1000", leader_from=Pm3(600, 1000))
    sh.view_title((440, 548), "D3", "STARTER TO WALLS W6 / W7 (400, MOD M1)", "SCALE 1:10")

    y = sh.panel(55, 290, 380, "JUNCTION DETAILING RULES", [
        "1  EVERY WALL SPRINGS FROM A STARTER CAST INTO THE MAT.  The starter's",
        "   horizontal leg lies IN THE BOTTOM CURTAIN, 900 long (600 for W5), and",
        "   is turned up to project 800 (50 phi) above a 150 kicker.",
        "2  THE LAP IS 50 phi, NOT 40 phi.  IS 456 Cl. 26.2.5.1(c) requires Ld or",
        "   30 phi, whichever is greater = 40 phi; Cl. 26.2.5.1 requires x1.4 if",
        "   more than 50 % of bars are lapped at one section.  ALL LAPS ARE",
        "   STAGGERED so that <= 50 % are spliced at any section, AND the lap is",
        "   specified at 50 phi - 25 % above requirement.  The x1.4 factor is",
        "   therefore not triggered.",
        "3  IS 4991 Cl. 10.3.1.1 PERMITS +25 % ON BOND FOR THE BLAST CASE",
        "   (Ld -> 32 phi).  IT IS NOT TAKEN.  All detailing uses the static 40 phi.",
        "4  A 500 x 500 HAUNCH WITH T20 @ 150 DIAGONALS IS PROVIDED AT EVERY",
        "   WALL / MAT AND WALL / ROOF JUNCTION OF THE BOX (300 x 300 with",
        "   T16 @ 150 at the headhouse - R-304).",
        "5  NO REINFORCEMENT IS STOPPED AT A CONSTRUCTION JOINT.",
    ], TXT["small"], 3.1)
    sh.panel(55, y - 6, 380, "WHY THE MAT IS 600 AND THE WALLS ARE 600", [
        "The perimeter wall is NOT strength-governed - it is 68 % utilised.  600 mm",
        "is set by (i) 75 mm cover, (ii) CONGESTION - two curtains plus closed links",
        "plus waterstops plus cast-in frames, (iii) IS 3370 crack control under",
        "sustained hydrostatic load, (iv) the EMP double curtain at 150 centres, and",
        "(v) the 1 168 kN/m axial path.  Stated honestly rather than presented as a",
        "strength result.",
        "",
        "The mat at 600 IS strength-governed - 84 % on the soft-band case.  At 500 mm",
        "the required steel is 105 % of that provided: it FAILS.",
    ], TXT["small"], 3.1)
    V.bbs_extract(sh, 448, 300, ["F07", "F08", "F09", "F06", "F10", "W06"])
    sh.panel(648, 548, 183, "THE HAZARD IS NOT THE BASALT - IT IS THE FLOW CONTACTS", [
        "A single red-bole or vesicular seam under the mat produces the",
        "DIFFERENTIAL-SUPPORT CASE THAT SIZES THE MAT.",
        "",
        "OVER-EXCAVATE ANY RED-BOLE OR VESICULAR SEAM AT FOUNDING LEVEL",
        "AND REPLACE WITH M15 LEAN CONCRETE.",
        "",
        "This is a construction requirement of the design, not an option.",
        "The 3.0 m unsupported band assumed in the mat design is the",
        "worst-position idealisation of exactly this condition.",
        "",
        "GROUND, ROCKHEAD, SBC, K0 AND ks ARE ALL [ASSUMED].  A site",
        "investigation is required before construction.",
    ], TXT["small"], 3.1)
    sh.titleblock(scale="1:10", sheet_of="7 OF 30")
    return sh.save(os.path.join(OUT, "R-103_Foundation_Wall_Details.dxf"))


def build():
    os.makedirs(OUT, exist_ok=True)
    return [r101(), r102(), r103()]


if __name__ == "__main__":
    for f in build():
        print("written", f)
