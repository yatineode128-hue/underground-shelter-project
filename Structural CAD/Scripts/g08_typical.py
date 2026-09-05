"""g08_typical.py  --  R-801 to R-805, typical details."""
import os, math
import sc_proj as P
import sc_dxflib as D
import sc_views as V
import rebar_data as R
from sc_dxflib import Sheet, vw, TXT

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "DXF",
                                   "Typical_Details"))
LD = [(8, 320, 256, 400), (10, 400, 320, 500), (12, 480, 384, 600),
      (16, 640, 512, 800), (20, 800, 640, 1000), (25, 1000, 800, 1250)]


def r801():
    sh = Sheet("R-801", "ANCHORAGE AND DEVELOPMENT",
               "Ld · HOOKS · ANCHORAGE AT SUPPORTS · TRIMMER ANCHORAGE")
    sh.sheet_header()
    sc = 10
    # D1 straight anchorage into a support
    Pm = vw(sc, 60, 380)
    sh.rect(*Pm(0, 0), *Pm(600, 1400), "S-CONCRETE")
    sh.rect(*Pm(600, 500), *Pm(2600, 1400), "S-CONCRETE")
    sh.concrete_hatch([Pm(0, 0), Pm(600, 0), Pm(600, 1400), Pm(0, 1400)])
    sh.concrete_hatch([Pm(600, 500), Pm(2600, 500), Pm(2600, 1400), Pm(600, 1400)])
    sh.pline([Pm(2550, 1310), Pm(90, 1310)], "S-REBAR-MAIN")
    sh.pline([Pm(2550, 590), Pm(400, 590)], "S-REBAR-MAIN")
    sh.dim_h(Pm(0, 1310), Pm(1000, 1310), Pm(0, 1900)[1], sc)
    sh.text("Ld MEASURED FROM THE SUPPORT FACE", Pm(0, 2050), TXT["small"], "S-TEXT")
    sh.dim_h(Pm(0, 0), Pm(600, 0), Pm(0, -300)[1], sc)
    sh.view_title((30, 552), "D1", "STRAIGHT ANCHORAGE OF TOP STEEL INTO A SUPPORT",
                  "SCALE 1:10")

    # D2 U-bar closing two curtains
    Pm2 = vw(sc, 240, 380)
    sh.rect(*Pm2(0, 0), *Pm2(600, 1400), "S-CONCRETE")
    sh.concrete_hatch([Pm2(0, 0), Pm2(600, 0), Pm2(600, 1400), Pm2(0, 1400)])
    for xo in (83, 517):
        sh.line(Pm2(xo, 100), Pm2(xo, 1350), "S-REBAR-MAIN")
    sh.pline([Pm2(83, 700), Pm2(83, 1310), Pm2(517, 1310), Pm2(517, 700)],
             "S-REBAR-SEC")
    sh.dim_v(Pm2(700, 700), Pm2(700, 1310), Pm2(900, 0)[0], sc)
    sh.text("LEG = Ld", Pm2(980, 950), TXT["small"], "S-TEXT")
    sh.view_title((215, 552), "D2", "U-BAR CLOSING TWO CURTAINS AT A FREE EDGE",
                  "SCALE 1:10")

    # D3 trimmer anchorage past an opening
    sc3 = 20
    Pm3 = vw(sc3, 400, 380)
    sh.rect(*Pm3(0, 0), *Pm3(3600, 1800), "S-CONCRETE")
    sh.rect(*Pm3(1200, 500), *Pm3(2400, 1300), "S-CONCRETE")
    sh.concrete_hatch([Pm3(0, 0), Pm3(3600, 0), Pm3(3600, 1800), Pm3(0, 1800)],
                      holes=[[Pm3(1200, 500), Pm3(2400, 500), Pm3(2400, 1300),
                              Pm3(1200, 1300)]])
    for o in (-120, -220):
        sh.line(Pm3(1200 + o, 100), Pm3(1200 + o, 1700), "S-REBAR-SEC")
        sh.line(Pm3(2400 - o, 100), Pm3(2400 - o, 1700), "S-REBAR-SEC")
    sh.dim_v(Pm3(980, 1300), Pm3(980, 1700), Pm3(700, 0)[0], sc3)
    sh.text("Ld BEYOND THE OPENING, BOTH DIRECTIONS", Pm3(0, -500),
            TXT["small"], "S-TEXT")
    sh.view_title((370, 552), "D3", "TRIMMER ANCHORAGE PAST AN OPENING", "SCALE 1:20")

    rows = [[f"T{d}", ld, ldc, lap, f"{40}", f"{50}"] for d, ld, ldc, lap in LD]
    sh.text("D4   DEVELOPMENT AND LAP LENGTHS - M35 / Fe500D", (30, 300),
            TXT["view_title"], "S-TITLE")
    sh.table(30, 292, [24, 34, 40, 34, 34, 34], rows,
             ["BAR", "Ld TENSION", "Ld COMPRESSION", "LAP", "Ld / phi", "LAP / phi"],
             TXT["table"], 5.0)
    y = V.loading_panel(sh, 230, 300, 250, [
        "Ld = phi x 0.87 fy / (4 tau_bd)             IS 456 Cl. 26.2.1",
        "tau_bd(M35) = 1.7, x1.6 for deformed bars in tension  =  2.72",
        "  ->  Ld TENSION = 40 phi",
        "Compression: tau_bd increased 25 %          IS 456 Cl. 26.2.1.1",
        "  ->  Ld COMPRESSION = 32 phi",
        "",
        "*** IS 4991 Cl. 10.3.1.1 PERMITS +25 % ON BOND FOR THE BLAST CASE,",
        "    WHICH WOULD GIVE 32 phi IN TENSION.  IT IS NOT TAKEN. ***",
        "    All detailing in this package uses the STATIC 40 phi.",
        "",
        "ANCHORAGE RULES USED THROUGHOUT",
        "  ·  Ld is measured FROM THE FACE OF THE SUPPORT, or from the face of",
        "     the opening for a trimmer.",
        "  ·  Slab and wall curtains are CONTINUOUS through supports wherever",
        "     the geometry allows; anchorage is the exception, not the rule.",
        "  ·  Trimmers are anchored Ld beyond an opening IN BOTH DIRECTIONS.",
        "  ·  U-bars close both curtains at every free edge.",
        "  ·  NO BAR RELIES ON A HOOK FOR ITS ANCHORAGE where a straight length",
        "     is available.",
    ], TXT["small"], 3.05, heading="THE RULE, AND THE ALLOWANCE NOT TAKEN")
    V.loading_panel(sh, 490, 300, 148, [
        "MAT / WALL STARTER        900 leg + 800 lap",
        "W6 / W7 STARTER           900 leg + 1000 lap",
        "SLAB TOP INTO A WALL      Ld 1000 (T25)",
        "WALL VERTICAL INTO SLAB   825 provided vs 640",
        "BLAST-DOOR JAMB           Ld 800 beyond",
        "ESC COLLAR TRIMMER        Ld 1000 beyond",
        "HW3 BAND                  lapped 1250 both ends",
        "STAIR FLIGHT TOP STEEL    800 + Ld 480",
        "STAIRWELL FLIGHT TOP      1200 + Ld 640",
        "OPENING-CORNER BAR        Ld 640 into the",
        "                          OPPOSITE face",
    ], TXT["small"], 3.05, heading="ANCHORAGE USED IN THIS PACKAGE")
    V.materials_panel(sh, 648, 552, 183)
    sh.titleblock(scale="1:10, 1:20", sheet_of="26 OF 30")
    return sh.save(os.path.join(OUT, "R-801_Anchorage_and_Development.dxf"))


def r802():
    sh = Sheet("R-802", "LAP AND SPLICE DETAILS",
               "50 phi STAGGERED · LAP ZONES · WHY NOT 40 phi")
    sh.sheet_header()
    sc = 20
    Pm = vw(sc, 60, 400)
    # staggered lap diagram
    sh.rect(*Pm(0, 0), *Pm(6000, 2400), "S-CONCRETE")
    sh.concrete_hatch([Pm(0, 0), Pm(6000, 0), Pm(6000, 2400), Pm(0, 2400)])
    for i, y in enumerate(range(200, 2400, 200)):
        sh.line(Pm(60, y), Pm(5940, y), "S-REBAR-MAIN")
        x0 = 1200 if i % 2 == 0 else 3600
        sh.line(Pm(x0, y + 40), Pm(x0 + 800, y + 40), "S-REBAR-SEC")
        sh.line(Pm(x0, y + 40), Pm(x0, y - 40), "S-REBAR-SEC")
        sh.line(Pm(x0 + 800, y + 40), Pm(x0 + 800, y - 40), "S-REBAR-SEC")
    sh.dim_h(Pm(1200, 0), Pm(2000, 0), Pm(0, -400)[1], sc)
    sh.text("LAP 50 phi", Pm(1220, -700), TXT["small"], "S-TEXT")
    sh.dim_h(Pm(1200, 2400), Pm(3600, 2400), Pm(0, 2800)[1], sc)
    sh.text("LAP ZONES STAGGERED - NOT MORE THAN 50 % SPLICED AT ANY SECTION",
            Pm(0, 3100), TXT["small"], "S-BLAST")
    sh.view_title((30, 552), "D1", "STAGGERED LAP ARRANGEMENT - TYPICAL", "SCALE 1:20")

    # D2 lap in a wall curtain, section
    sc2 = 10
    Pm2 = vw(sc2, 400, 400)
    sh.rect(*Pm2(0, 0), *Pm2(600, 1800), "S-CONCRETE")
    sh.concrete_hatch([Pm2(0, 0), Pm2(600, 0), Pm2(600, 1800), Pm2(0, 1800)])
    for xo in (83, 517):
        sh.line(Pm2(xo, 40), Pm2(xo, 1760), "S-REBAR-MAIN")
        sh.line(Pm2(xo + 26, 300), Pm2(xo + 26, 1100), "S-REBAR-SEC")
    sh.dim_v(Pm2(700, 300), Pm2(700, 1100), Pm2(900, 0)[0], sc2)
    sh.text("LAP 800 (T16)", Pm2(1000, 650), TXT["small"], "S-TEXT")
    sh.text("BARS IN CONTACT, TIED", Pm2(0, -350), TXT["small"], "S-TEXT")
    sh.view_title((370, 552), "D2", "LAP IN A WALL CURTAIN - SECTION", "SCALE 1:10")

    rows = [[f"T{d}", lap, f"{lap}", "STAGGERED"] for d, ld, ldc, lap in LD]
    sh.text("D3   LAP LENGTHS - M35 / Fe500D, 50 phi", (30, 300),
            TXT["view_title"], "S-TITLE")
    sh.table(30, 292, [24, 36, 36, 44], rows,
             ["BAR", "LAP mm", "= 50 phi", "ARRANGEMENT"], TXT["table"], 5.0)
    V.loading_panel(sh, 200, 300, 300, [
        "IS 456 Cl. 26.2.5.1(c) gives lap = Ld or 30 phi, whichever is GREATER.",
        "For M35 / Fe500D that is 40 phi.",
        "",
        "IS 456 Cl. 26.2.5.1 requires the lap to be INCREASED BY x1.4 IF MORE",
        "THAN 50 % OF THE BARS ARE LAPPED AT ONE SECTION.",
        "",
        "THIS PACKAGE DOES BOTH THINGS AT ONCE:",
        "  1  EVERY LAP IS STAGGERED so that not more than 50 % of the bars in",
        "     a curtain are spliced at any one section - so the x1.4 factor is",
        "     NOT TRIGGERED; and",
        "  2  THE LAP IS SPECIFIED AT 50 phi ANYWAY - 25 % above the 40 phi",
        "     requirement.",
        "",
        "The result is a 25 % margin on a splice length that already avoids the",
        "code penalty.  That margin is deliberate: laps in a blast-loaded",
        "member see LOAD REVERSAL AND REBOUND, which the static rule does not",
        "consider, and the SDOF support-rotation check that would quantify",
        "rebound is PHASE 3 WORK AND HAS NOT BEEN DONE.",
        "",
        "P-1 STOCK BAR 12 000 mm.  Any run longer than this is split into equal",
        "pieces with 50 phi laps added.  The bar bending schedule states the",
        "number of pieces for every such mark.",
        "",
        "MECHANICAL COUPLERS ARE NOT SPECIFIED anywhere in this package.  No",
        "coupler performance data exists in the project record.",
    ], TXT["small"], 3.05, heading="LAP POLICY - AND WHY IT IS 50 phi, NOT 40 phi")
    V.materials_panel(sh, 648, 552, 183)
    sh.titleblock(scale="1:20, 1:10", sheet_of="27 OF 30")
    return sh.save(os.path.join(OUT, "R-802_Lap_and_Splice_Details.dxf"))


def r803():
    sh = Sheet("R-803", "WALL / SLAB CONNECTIONS",
               "WALL-MAT · WALL-ROOF · HEADHOUSE WALL-SLAB · HAUNCH FAMILY",
               flags=["C16 OPEN"])
    sh.sheet_header()
    sc = 15
    # D1 wall / mat
    Pm = vw(sc, 60, 300)
    sh.rect(*Pm(0, 0), *Pm(2200, 600), "S-CONCRETE")
    sh.rect(*Pm(0, 600), *Pm(600, 2200), "S-CONCRETE")
    sh.pline([Pm(600, 600), Pm(1100, 600), Pm(600, 1100)], "S-CONCRETE")
    for pts in ([Pm(0, 0), Pm(2200, 0), Pm(2200, 600), Pm(0, 600)],
                [Pm(0, 600), Pm(600, 600), Pm(600, 2200), Pm(0, 2200)],
                [Pm(600, 600), Pm(1100, 600), Pm(600, 1100)]):
        sh.concrete_hatch(pts)
    for xo in (83, 517):
        sh.pline([Pm(xo + 900, 83), Pm(xo, 83), Pm(xo, 1550)], "S-REBAR-TIE")
        sh.line(Pm(xo, 750), Pm(xo, 2200), "S-REBAR-MAIN")
    sh.bar_run(Pm(150, 83), Pm(2150, 83), 150, sc, "S-REBAR-MAIN", 0.7)
    sh.bar_run(Pm(150, 552), Pm(2150, 552), 150, sc, "S-REBAR-MAIN", 0.7)
    for i in range(4):
        o = i * 150
        sh.line(Pm(600 + o, 540), Pm(540, 600 + o), "S-REBAR-SEC")
    sh.dline(Pm(0, 750), Pm(600, 750), "S-HIDDEN")
    sh.dim_h(Pm(600, 600), Pm(1100, 600), Pm(0, 2500)[1], sc)
    sh.view_title((30, 552), "D1", "WALL / MAT - STARTER, KICKER AND 500 HAUNCH",
                  "SCALE 1:15")
    V.balloon(sh, (36, 380), "F07", Pm(200, 1100))
    V.balloon(sh, (128, 350), "W06", Pm(800, 800))

    # D2 wall / roof
    Pm2 = vw(sc, 240, 300)
    sh.rect(*Pm2(0, 0), *Pm2(600, 1600), "S-CONCRETE")
    sh.rect(*Pm2(0, 1600), *Pm2(2200, 2500), "S-CONCRETE")
    sh.pline([Pm2(600, 1600), Pm2(1100, 1600), Pm2(600, 1100)], "S-CONCRETE")
    for pts in ([Pm2(0, 0), Pm2(600, 0), Pm2(600, 1600), Pm2(0, 1600)],
                [Pm2(0, 1600), Pm2(2200, 1600), Pm2(2200, 2500), Pm2(0, 2500)],
                [Pm2(600, 1600), Pm2(1100, 1600), Pm2(600, 1100)]):
        sh.concrete_hatch(pts)
    for xo in (83, 517):
        sh.line(Pm2(xo, 40), Pm2(xo, 2400), "S-REBAR-MAIN")
    sh.pline([Pm2(2150, 2413), Pm2(88, 2413)], "S-REBAR-MAIN")
    sh.pline([Pm2(2150, 1688), Pm2(400, 1688)], "S-REBAR-MAIN")
    for i in range(4):
        o = i * 150
        sh.line(Pm2(600 + o, 1660), Pm2(660, 1660 - o), "S-REBAR-SEC")
    sh.dim_h(Pm2(88, 2413), Pm2(1088, 2413), Pm2(0, 2900)[1], sc)
    sh.text("Ld 1000", Pm2(1200, 2860), TXT["small"], "S-TEXT")
    sh.view_title((215, 552), "D2", "WALL / ROOF - 500 HAUNCH AND TOP-STEEL ANCHORAGE",
                  "SCALE 1:15")
    V.balloon(sh, (300, 468), "S03A", Pm2(1400, 2413))
    V.balloon(sh, (232, 380), "W01", Pm2(83, 900))

    # D3 headhouse wall on the pressure slab
    Pm3 = vw(sc, 430, 300)
    sh.rect(*Pm3(-600, 0), *Pm3(2400, 900), "S-CONCRETE")
    sh.rect(*Pm3(0, 900), *Pm3(400, 2400), "S-CONCRETE")
    sh.concrete_hatch([Pm3(-600, 0), Pm3(2400, 0), Pm3(2400, 900), Pm3(-600, 900)])
    sh.concrete_hatch([Pm3(0, 900), Pm3(400, 900), Pm3(400, 2400), Pm3(0, 2400)])
    sh.dline(Pm3(0, 1050), Pm3(400, 1050), "S-HIDDEN")
    for xo in (58, 342):
        sh.pline([Pm3(xo - 600 if xo < 200 else xo + 600, 88), Pm3(xo, 88),
                  Pm3(xo, 1850)], "S-REBAR-TIE")
        sh.line(Pm3(xo, 1050), Pm3(xo, 2400), "S-REBAR-MAIN")
    sh.bar_run(Pm3(-500, 88), Pm3(2350, 88), 150, sc, "S-REBAR-MAIN", 0.6)
    sh.bar_run(Pm3(-500, 813), Pm3(2350, 813), 150, sc, "S-REBAR-MAIN", 0.6)
    sh.level(Pm3(1400, 900), "(-)2.000")
    sh.dim_v(Pm3(2400, 0), Pm3(2400, 900), Pm3(2800, 0)[0], sc)
    sh.view_title((400, 552), "D3", "HEADHOUSE WALL ON THE PRESSURE SLAB",
                  "SCALE 1:15")
    V.balloon(sh, (410, 380), "H10", Pm3(58, 1300))

    y = V.loading_panel(sh, 30, 260, 300, [
        "THE HAUNCH FAMILY",
        "  BOX, wall/mat and wall/roof     500 x 500, diagonal T20 @ 150",
        "  HEADHOUSE, wall/roof            300 x 300, diagonal T16 @ 150",
        "",
        "THE HAUNCH IS A LOAD-PATH ELEMENT, NOT A FILLET.  It shortens the shear",
        "span at the corner of the box and controls cracking at the re-entrant",
        "angle, which is where a monolithic box first distresses under an",
        "internal-to-external pressure reversal.",
        "",
        "THE STARTER FAMILY",
        "  W1-W4 from the mat     F07  T16 @ 150 EF, 900 leg,  lap  800",
        "  W6 / W7 from the mat   F08  T20 @ 150 EF, 900 leg,  lap 1000",
        "  W5 from the mat        F09  T12 @ 150 EF, 600 leg,  lap  600",
        "  HW1-HW4 from the slab  H10  T16 @ 150 EF, 600 leg,  lap  800",
        "  Every starter projects its lap length ABOVE A 150 KICKER.",
        "",
        "CONTINUITY RULE, APPLIED EVERYWHERE",
        "  NO REINFORCEMENT IS STOPPED AT A JUNCTION OR AT A CONSTRUCTION JOINT.",
        "  Anchorage is used only where the geometry genuinely terminates a bar.",
    ], TXT["small"], 3.05, heading="CONNECTION FAMILIES USED IN THIS PACKAGE")
    sh.panel(340, 260, 298, "*** C16 OPEN - AFFECTS THIS SHEET ***", [
        "The roof / platform junction of the entry stairwell is NOT resolved.",
        "Master A.4.7 says the roof over the platform becomes the 500 headhouse",
        "roof; master B.6 / A.7.6 / F.2 design, load and register a 250 roof, and",
        "the headhouse footprint does not overlap the platform.",
        "",
        "NO CONNECTION DETAIL BETWEEN THE STAIRWELL ROOF AND THE HEADHOUSE ROOF",
        "IS DRAWN ON THIS SHEET, because the two documents do not agree on what",
        "is being connected.",
        "",
        "WHAT IS FIXED AND NOT AFFECTED BY C16:",
        "  ·  the wall/mat and wall/roof haunches of the box,",
        "  ·  the headhouse wall on the pressure slab (D3 above),",
        "  ·  the movement joint at the stairwell raft (R-702, R-804).",
        "",
        "A USER RULING IS REQUIRED BEFORE THE JUNCTION CAN BE DETAILED.",
    ], TXT["small"], 3.05)
    V.bbs_extract(sh, 648, 552, ["F07", "F08", "F09", "H10", "W06", "W12", "H06"])
    sh.titleblock(scale="1:15", sheet_of="28 OF 30")
    return sh.save(os.path.join(OUT, "R-803_Wall_Slab_Connections.dxf"))


def r804():
    sh = Sheet("R-804", "CONSTRUCTION JOINTS",
               "FULL BAR CONTINUITY · TWO WATERSTOPS · WELDED EMP STRAP",
               flags=["C16 OPEN"])
    sh.sheet_header()
    sc = 10
    Pm = vw(sc, 70, 340)
    sh.rect(*Pm(0, 0), *Pm(600, 2400), "S-CONCRETE")
    sh.concrete_hatch([Pm(0, 0), Pm(600, 0), Pm(600, 1200), Pm(0, 1200)])
    sh.concrete_hatch([Pm(0, 1200), Pm(600, 1200), Pm(600, 2400), Pm(0, 2400)])
    sh.line(Pm(0, 1200), Pm(600, 1200), "S-CONCRETE")
    for x in range(0, 600, 60):
        sh.line(Pm(x, 1200), Pm(x + 30, 1240), "S-CONCRETE-THIN")
    for xo in (83, 517):
        sh.line(Pm(xo, 60), Pm(xo, 2340), "S-REBAR-MAIN")
    sh.bar_run(Pm(83, 150), Pm(83, 2300), 150, sc, "S-REBAR-MAIN", 0.9)
    sh.bar_run(Pm(517, 150), Pm(517, 2300), 150, sc, "S-REBAR-MAIN", 0.9)
    for y in (200, 400, 600, 800, 1000, 1400, 1600, 1800, 2000, 2200):
        sh.rect(*Pm(50, y - 55), *Pm(550, y + 55), "S-REBAR-STIRRUP")
    # waterstops
    sh.pline([Pm(140, 1120), Pm(140, 1280)], "S-WATERPROOF")
    sh.pline([Pm(90, 1120), Pm(190, 1120)], "S-WATERPROOF")
    sh.pline([Pm(90, 1280), Pm(190, 1280)], "S-WATERPROOF")
    sh.pline([Pm(460, 1120), Pm(460, 1280)], "S-WATERPROOF")
    sh.pline([Pm(410, 1120), Pm(510, 1120)], "S-WATERPROOF")
    sh.pline([Pm(410, 1280), Pm(510, 1280)], "S-WATERPROOF")
    # EMP strap
    sh.pline([Pm(200, 1200), Pm(400, 1200)], "S-STEELWORK")
    sh.circle(Pm(300, 1200), 0.9, "S-STEELWORK")
    sh.leader([Pm(300, 1200), (200, 420)], "WELDED Cu / GALV EMP STRAP")
    sh.leader([Pm(140, 1200), (200, 400)], "TWO WATERSTOPS - ONE EACH CURTAIN")
    sh.leader([Pm(83, 1600), (200, 380)], "REINFORCEMENT FULLY CONTINUOUS")
    sh.dim_h(Pm(0, 0), Pm(600, 0), Pm(0, -300)[1], sc)
    sh.view_title((30, 552), "D1", "CONSTRUCTION JOINT IN A 600 WALL - TYPICAL",
                  "SCALE 1:10")
    sh.text("JOINT SURFACE ROUGHENED TO EXPOSE THE COARSE AGGREGATE, CLEANED AND",
            (30, 300), TXT["small"], "S-TEXT")
    sh.text("SATURATED SURFACE-DRY BEFORE THE NEXT POUR.  IS 456 Cl. 13.4.",
            (30, 295), TXT["small"], "S-TEXT")

    # D2 movement joint - the only one
    sc2 = 20
    Pm2 = vw(sc2, 320, 340)
    sh.rect(*Pm2(0, 0), *Pm2(1400, 300), "S-CONCRETE")
    sh.rect(*Pm2(1500, 0), *Pm2(2900, 900), "S-CONCRETE")
    sh.concrete_hatch([Pm2(0, 0), Pm2(1400, 0), Pm2(1400, 300), Pm2(0, 300)])
    sh.concrete_hatch([Pm2(1500, 0), Pm2(2900, 0), Pm2(2900, 900), Pm2(1500, 900)])
    sh.rect(*Pm2(1400, -100), *Pm2(1500, 900), "S-BLAST")
    sh.bar_run(Pm2(100, 56), Pm2(1300, 56), 200, sc2, "S-REBAR-MAIN", 0.7)
    sh.bar_run(Pm2(1600, 56), Pm2(2800, 56), 150, sc2, "S-REBAR-MAIN", 0.7)
    sh.text("NO BAR CROSSES THE JOINT", Pm2(0, -700), TXT["small"], "S-BLAST")
    sh.dim_h(Pm2(1400, 900), Pm2(1500, 900), Pm2(0, 1300)[1], sc2)
    sh.view_title((300, 552), "D2", "MOVEMENT JOINT - STAIRWELL RAFT / HEADHOUSE",
                  "SCALE 1:20")
    sh.text("THE ONLY MOVEMENT JOINT ON THE PROJECT.", (300, 300), TXT["small"], "S-BLAST")

    y = V.loading_panel(sh, 30, 262, 300, [
        "CONSTRUCTION JOINTS - APPROXIMATELY 6 m CENTRES",
        "  1  REINFORCEMENT IS FULLY CONTINUOUS ACROSS EVERY CONSTRUCTION JOINT.",
        "     No bar is lapped at a joint unless the lap is separately staggered.",
        "  2  TWO WATERSTOPS - one in each curtain zone, centre-bulb type, on both",
        "     the earth face and the internal face of the section.",
        "  3  A WELDED Cu / GALVANISED EMP STRAP bridges the joint and is welded to",
        "     the cage on both sides, so that the reinforcement shield remains",
        "     electrically continuous across the pour break.",
        "  4  Joint surface roughened to expose the coarse aggregate, cleaned and",
        "     brought to a saturated surface-dry condition (IS 456 Cl. 13.4).",
        "  5  Joints are located AWAY from the blast-door openings, the escape-shaft",
        "     collars and the stair-void re-entrant corners.",
        "",
        "*** NO MOVEMENT JOINT ANYWHERE INSIDE THE PROTECTIVE ENVELOPE. ***",
        "A movement joint is a GUARANTEED BLAST, GAS AND EMP DISCONTINUITY.  The",
        "only movement joint on the project is where the entry-stairwell raft meets",
        "the headhouse - and that raft is OUTSIDE the protective boundary and is",
        "declared expendable.",
        "",
        "*** C16 OPEN ***  The roof / platform junction at that same location is not",
        "resolved.  The MOVEMENT JOINT IN THE RAFT is fixed and is not affected;",
        "the ROOF junction above it cannot be detailed until C16 is ruled on.",
    ], TXT["small"], 3.05, heading="JOINT POLICY")
    sh.panel(340, 262, 298, "WHY THE EMP STRAP MATTERS", [
        "The reinforcement cage is the primary EMP shield for the shelter, which",
        "is why the bar spacing is capped at 150 mm both curtains - a limit that",
        "is stricter than any IS 456 requirement and that governs the main steel",
        "spacing of every element in this package.",
        "",
        "A pour break is a discontinuity in that shield.  A welded strap restores",
        "it.  Reinforcement that is merely lapped across a joint is a structural",
        "connection but NOT a reliable electrical one.",
        "",
        "THE HONEST LIMIT, STATED BEFORE A REVIEWER FINDS IT:  a rebar cage at",
        "150 mm centres gives essentially 0 dB of attenuation at 1 GHz.  The",
        "answer in this project is the EMP Zone 2 welded steel room in Bay 3, not",
        "the cage.  The cage and its straps handle the low-frequency content and",
        "the bonding path; they are not the shield.",
        "",
        "The same reasoning is why every cast-in door frame is WELDED to the cage",
        "rather than simply embedded - R-703.",
    ], TXT["small"], 3.05)
    V.materials_panel(sh, 648, 552, 183)
    sh.titleblock(scale="1:10, 1:20", sheet_of="29 OF 30")
    return sh.save(os.path.join(OUT, "R-804_Construction_Joints.dxf"))


def r805():
    sh = Sheet("R-805", "WATERPROOFING / STRUCTURAL INTERFACE",
               "TANKING · WATERSTOPS · UPLIFT · THE INTERFACE THE STEEL DEPENDS ON",
               flags=["A2 GWT ASSUMED"])
    sh.sheet_header()
    sc = 20
    Pm = vw(sc, 70, 300)
    # mat / wall / membrane
    sh.rect(*Pm(-600, -100), *Pm(3000, 0), "S-CONCRETE-THIN")
    sh.hatch_pat([Pm(-600, -100), Pm(3000, -100), Pm(3000, 0), Pm(-600, 0)],
                 "ANSI31", 1.0, 45, "S-HATCH")
    sh.rect(*Pm(0, 0), *Pm(3000, 600), "S-CONCRETE")
    sh.concrete_hatch([Pm(0, 0), Pm(3000, 0), Pm(3000, 600), Pm(0, 600)])
    sh.rect(*Pm(0, 600), *Pm(600, 2600), "S-CONCRETE")
    sh.concrete_hatch([Pm(0, 600), Pm(600, 600), Pm(600, 2600), Pm(0, 2600)])
    sh.line(Pm(-600, -30), Pm(3000, -30), "S-WATERPROOF")
    sh.pline([Pm(0, -30), Pm(-100, -30), Pm(-100, 2600)], "S-WATERPROOF")
    sh.text("TANKING MEMBRANE ON THE BLINDING, TURNED UP THE EXTERNAL FACE",
            Pm(-600, -700), TXT["small"], "S-WATERPROOF")
    sh.text("100 M15 BLINDING", Pm(1200, -350), TXT["small"], "S-TEXT")
    # uplift arrows
    for x in range(300, 3000, 500):
        sh.pline([Pm(x, -900), Pm(x, -200)], "S-BLAST")
        sh.pline([Pm(x - 90, -450), Pm(x, -200), Pm(x + 90, -450)], "S-BLAST")
    sh.text("HYDROSTATIC UPLIFT 46.11 kPa  =  6289 kN OVER 136.4 m2",
            Pm(300, -1200), TXT["small"], "S-BLAST")
    # GWT
    sh.line(Pm(-800, 2450), Pm(3200, 2450), "S-WATERPROOF")
    sh.text("DESIGN GWT (-)2.000  [ASSUMED - A2]", Pm(1400, 2520),
            TXT["small"], "S-WATERPROOF")
    sh.bar_run(Pm(150, 83), Pm(2900, 83), 150, sc, "S-REBAR-MAIN", 0.6)
    sh.bar_run(Pm(150, 552), Pm(2900, 552), 150, sc, "S-REBAR-MAIN", 0.6)
    for xo in (83, 517):
        sh.line(Pm(xo, 700), Pm(xo, 2600), "S-REBAR-MAIN")
    sh.dim_v(Pm(3000, 0), Pm(3000, 600), Pm(3400, 0)[0], sc)
    sh.view_title((30, 552), "D1", "TANKING AT THE MAT / WALL / BLINDING INTERFACE",
                  "SCALE 1:20")

    # D2 roof waterproofing
    Pm2 = vw(sc, 400, 340)
    sh.rect(*Pm2(0, 0), *Pm2(2600, 900), "S-CONCRETE")
    sh.concrete_hatch([Pm2(0, 0), Pm2(2600, 0), Pm2(2600, 900), Pm2(0, 900)])
    sh.line(Pm2(0, 930), Pm2(2600, 930), "S-WATERPROOF")
    sh.rect(*Pm2(0, 930), *Pm2(2600, 1030), "S-CONCRETE-THIN")
    sh.line(Pm2(0, 1030), Pm2(2600, 1030), "S-EXISTING")
    sh.line(Pm2(0, 1780), Pm2(2600, 1780), "S-EXISTING")
    sh.hatch_pat([Pm2(0, 1030), Pm2(2600, 1030), Pm2(2600, 1780), Pm2(0, 1780)],
                 "EARTH", 1.0, 0, "S-EXISTING")
    sh.text("MEMBRANE ON THE SLAB", Pm2(2700, 900), TXT["small"], "S-WATERPROOF")
    sh.text("100 PROTECTION SCREED", Pm2(2700, 950), TXT["small"], "S-TEXT")
    sh.text("ENGINEERED COVER OVER - R-302", Pm2(2700, 1300), TXT["small"], "S-EXISTING")
    sh.bar_run(Pm2(150, 813), Pm2(2450, 813), 150, sc, "S-REBAR-MAIN", 0.6)
    sh.bar_run(Pm2(150, 88), Pm2(2450, 88), 150, sc, "S-REBAR-MAIN", 0.6)
    sh.dim_v(Pm2(0, 0), Pm2(0, 900), Pm2(-400, 0)[0], sc)
    sh.view_title((370, 552), "D2", "ROOF WATERPROOFING AND THE SCREED",
                  "SCALE 1:20")

    y = V.loading_panel(sh, 30, 240, 300, [
        "WHY A WATERPROOFING SHEET SITS IN A REINFORCEMENT PACKAGE",
        "",
        "THE WATER IS NOT AN ARCHITECTURAL PROBLEM HERE - IT IS THE LOAD.",
        "  ·  Of the 15.41 kPa/m lateral gradient on the walls, 9.81 IS WATER and",
        "     only 5.60 is soil.  WATER IS NEARLY TWO-THIRDS OF THE LATERAL LOAD.",
        "  ·  The whole 46.11 kPa uplift on the mat is water.",
        "  ·  Both depend entirely on A2: DESIGN GWT (-)2.000, WHICH IS [ASSUMED]",
        "     AND REQUIRES MONSOON-SEASON MONITORING.",
        "",
        "THE STEEL IN THIS PACKAGE IS SIZED ON THAT ASSUMPTION.  If the monsoon",
        "groundwater level is higher than (-)2.000, the wall moments, the mat",
        "case and the flotation factors all move.",
        "",
        "INTERFACE REQUIREMENTS",
        "  1  Tanking membrane on the blinding, turned up the external face and",
        "     lapped to the roof membrane - a continuous tank.",
        "  2  100 mm protection screed over the roof membrane; it is also the",
        "     first layer of the engineered cover.",
        "  3  TWO WATERSTOPS AT EVERY CONSTRUCTION JOINT - R-804.",
        "  4  INTEGRAL CRYSTALLINE WATERPROOFING ADMIXTURE in the concrete; the",
        "     membrane is not the only line of defence.",
        "  5  IS 3370 crack control: 0.2 mm limit, satisfied by the 0.35 % surface-",
        "     zone steel over a 250 mm zone, NOT BY CALCULATION - see QA/QC R-11.",
        "  6  NO COVER IS REDUCED FOR WATERPROOFING.  The membrane is outside the",
        "     structural section and adds nothing to the cover.",
    ], TXT["small"], 3.05, heading="THE INTERFACE THE REINFORCEMENT DEPENDS ON")
    sh.panel(340, 240, 298, "FLOTATION - THE CONSTRUCTION STAGE GOVERNS", [
        "STAGE                       WEIGHT  UPLIFT  FoS @(-)2.000  FLOODED",
        "1 mat cast only              2 009   6 175    0.33 FAIL     0.23 FAIL",
        "2 mat + walls, no roof       4 802   6 175    0.78 FAIL     0.55 FAIL",
        "3 box complete, no backfill  7 528   6 175    1.22 MARGINAL 0.86 FLOATS",
        "4 backfilled + cover        12 453   6 175    2.02 OK       1.41 OK",
        "",
        "MANDATORY MITIGATION - A DESIGN OUTPUT, NOT A CONTRACTOR'S PROBLEM",
        "  1  Continuous dewatering from the start of excavation until backfill",
        "     and cover are complete.",
        "  2  Temporary pressure-relief valves / knock-out plugs in the mat,",
        "     6 No., grouted up ONLY AFTER backfill.",
        "  3  Programme the sub-structure to complete before the monsoon, or bund",
        "     and positively drain with standby pumping and generator back-up.",
        "  4  Backfill SYMMETRICALLY, in layers.",
        "",
        "FLOTATION CANNOT BE READ OFF THE STAAD MODEL.  The elastic-mat springs",
        "TAKE TENSION, so the mat never lifts in the model.  It is a HAND CHECK",
        "on real dimensions and real weights.  Anyone who says the analysis shows",
        "no uplift has misunderstood their own model.",
    ], TXT["small"], 3.05)
    V.materials_panel(sh, 648, 552, 183)
    sh.titleblock(scale="1:20", sheet_of="30 OF 30")
    return sh.save(os.path.join(OUT, "R-805_Waterproofing_Structural_Interface.dxf"))


def build():
    os.makedirs(OUT, exist_ok=True)
    return [r801(), r802(), r803(), r804(), r805()]


if __name__ == "__main__":
    for f in build():
        print("written", f)
