"""g06_stairs.py  --  R-601 to R-604, stairs.

MAIN STAIRCASE GEOMETRY IS FROZEN: 24R @ 170.8333 · tread 280 · 3 flights x 8 ·
total rise 4100 · flight width 1200 · well 200 · headroom 2533.  Reproduced
exactly, never altered.
"""
import os, math
import sc_proj as P
import sc_dxflib as D
import sc_views as V
import rebar_data as R
from sc_dxflib import Sheet, vw, TXT

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "DXF", "Stairs"))

FROZEN = [
    "*** MAIN STAIRCASE GEOMETRY IS FROZEN.  DO NOT ALTER. ***",
    "",
    "24 RISERS @ 170.8333  ·  TREAD 280  ·  3 FLIGHTS x 8 RISERS",
    "TOTAL RISE 4100  ·  FLIGHT WIDTH 1200  ·  WELL 200  ·  WAIST 200",
    "HEADROOM 2533",
    "Flight A (flights 1 and 3, stacked)  X 15 300 - 16 500",
    "Well                                 X 16 500 - 16 700",
    "Flight B (flight 2)                  X 16 700 - 17 900",
    "Landing L1  (-)4.7333   Y 3760 - 4960",
    "Landing L2  (-)3.3667   Y  600 - 1800",
    "Arrival     (-)6.100    Y  600 - 1800  = THE MAT SURFACE",
    "Store under L1          Y 4960 - 5600",
    "[ALL CONFIRMED - re-extracted from 1_Underground_Level_Plan.dxf]",
    "",
    "NBC 2016 PART 4 GEOMETRY CHECK",
    "  riser 170.833 <= 190                                OK",
    "  going 280 >= 250                                    OK",
    "  flight width 1200 >= 1000                           OK  stretcher-capable",
    "  risers per flight 8 <= 12                           OK",
    "  headroom 2533 >= 2200                               OK",
    "  total rise 24 x 170.833 = 4100 closes (-)6.100 to (-)2.000 EXACTLY",
]

NOT_BLAST = [
    "*** INSIDE THE PROTECTIVE ENVELOPE BUT NOT A BLAST ELEMENT ***",
    "",
    "The shaft pressurises - that is Finding F1 and the reason walls W6 and W7",
    "are 400 mm thick.  But that pressure acts on the shaft WALLS and on the",
    "blast DOORS.  It is NOT a net load on a slab that is open on both faces.",
    "",
    "THE STAIRCASE IS THEREFORE DESIGNED TO IS 456 WITH NORMAL PARTIAL FACTORS,",
    "NOT WITH IS 4991 DYNAMIC MATERIAL STRENGTHS.  fck 35 and fy 500 are used,",
    "not fck,dyn 43.75 and fy,dyn 625.  This is stated on every stair drawing.",
    "",
    "COMPATIBILITY, RECORDED:",
    "  ·  The arrival landing at (-)6.100 IS the mat surface.  There is no",
    "     separate slab there.",
    "  ·  Flight 3 lands directly on the 900 pressure-slab pad at (-)2.000.",
    "  ·  The landings prop W6 and W7 at (-)4.733 and (-)3.367, BUT ONLY OVER",
    "     THEIR 1200 DEPTH.  THE 400 WALL DESIGN DOES NOT RELY ON THAT PROP.",
]


def r601():
    sh = Sheet("R-601", "MAIN STAIRCASE REINFORCEMENT PLAN",
               "BAY 7 · WAIST 200 · GEOMETRY FROZEN",
               flags=["GEOMETRY FROZEN"])
    sh.sheet_header()
    sc = 25
    Pm = vw(sc, 90, 260)
    S = P.STAIR
    # shaft walls
    sh.rect(*Pm(14800, 0), *Pm(15200, 6200), "S-CONCRETE")
    sh.rect(*Pm(18000, 0), *Pm(18400, 6200), "S-CONCRETE")
    sh.rect(*Pm(14800, 0), *Pm(18400, 600), "S-CONCRETE")
    sh.rect(*Pm(14800, 5600), *Pm(18400, 6200), "S-CONCRETE")
    for pts in ([Pm(14800, 0), Pm(15200, 0), Pm(15200, 6200), Pm(14800, 6200)],
                [Pm(18000, 0), Pm(18400, 0), Pm(18400, 6200), Pm(18000, 6200)],
                [Pm(15200, 0), Pm(18000, 0), Pm(18000, 600), Pm(15200, 600)],
                [Pm(15200, 5600), Pm(18000, 5600), Pm(18000, 6200), Pm(15200, 6200)]):
        sh.concrete_hatch(pts)
    sh.text("W6", Pm(15000, 6350), TXT["small"], "S-TEXT", "CENTER")
    sh.text("W7", Pm(18200, 6350), TXT["small"], "S-TEXT", "CENTER")
    # flights
    for x0, x1, lab in [(S["fltA"][0], S["fltA"][1], "FLIGHT A (1 AND 3)"),
                        (S["fltB"][0], S["fltB"][1], "FLIGHT B (2)")]:
        sh.rect(*Pm(x0, 1800), *Pm(x1, 3760), "S-CONCRETE")
        for i in range(8):
            y = 1800 + i * 280
            sh.line(Pm(x0, y), Pm(x1, y), "S-CONCRETE-THIN")
        sh.text(lab, Pm((x0 + x1) / 2, 2780), TXT["small"], "S-TEXT", "CENTER", 90)
        for x in range(x0 + 60, x1, 150):
            sh.line(Pm(x, 1700), Pm(x, 3860), "S-REBAR-MAIN")
    sh.rect(*Pm(S["wellx"][0], 1800), *Pm(S["wellx"][1], 3760), "S-HIDDEN")
    # landings
    sh.rect(*Pm(15200, 3760), *Pm(18000, 4960), "S-CONCRETE")
    sh.rect(*Pm(15200, 600), *Pm(18000, 1800), "S-CONCRETE")
    sh.rect(*Pm(15200, 4960), *Pm(18000, 5600), "S-CONCRETE-THIN")
    sh.text("STORE UNDER L1", Pm(16600, 5220), TXT["small"], "S-TEXT", "CENTER")
    for x in range(15300, 18000, 125):
        sh.line(Pm(x, 3800), Pm(x, 4920), "S-REBAR-MAIN")
        sh.line(Pm(x, 640), Pm(x, 1760), "S-REBAR-MAIN")
    for y in range(3800, 4960, 200):
        sh.line(Pm(15260, y), Pm(17940, y), "S-REBAR-DIST")
    for y in range(640, 1800, 200):
        sh.line(Pm(15260, y), Pm(17940, y), "S-REBAR-DIST")
    sh.text("L1  (-)4.7333", Pm(16600, 4380), TXT["small"], "S-LEVEL", "CENTER")
    sh.text("L2  (-)3.3667  OVER  ·  ARRIVAL (-)6.100", Pm(16600, 1200),
            TXT["small"], "S-LEVEL", "CENTER")
    sh.dim_h(Pm(15200, 0), Pm(18000, 0), Pm(0, -700)[1], sc)
    sh.dim_h(Pm(15300, 0), Pm(16500, 0), Pm(0, -1400)[1], sc)
    sh.dim_h(Pm(16500, 0), Pm(16700, 0), Pm(0, -1400)[1], sc)
    sh.dim_h(Pm(16700, 0), Pm(17900, 0), Pm(0, -1400)[1], sc)
    sh.dim_v(Pm(14800, 1800), Pm(14800, 3760), Pm(14100, 0)[0], sc)
    sh.dim_v(Pm(14800, 3760), Pm(14800, 4960), Pm(14100, 0)[0], sc)
    sh.dim_v(Pm(14800, 600), Pm(14800, 1800), Pm(14100, 0)[0], sc)
    sh.north((560, 480))
    V.balloon(sh, (240, 380), "ST01", Pm(15900, 3000))
    V.balloon(sh, (240, 314), "ST04", Pm(16300, 1300))
    V.balloon(sh, (330, 452), "ST06", Pm(17200, 4400))
    sh.secmark((84, 340), "A"); sh.secmark((240, 340), "A")
    sh.text("SECTION A-A  ->  R-602", (160, 246), TXT["small"], "S-SECTION", "CENTER")
    sh.view_title((84, 552), "V1", "MAIN STAIRCASE PLAN - BAY 7", "SCALE 1:25")
    sh.text("BOTTOM STEEL SHOWN.  TOP STEEL ST03 / ST05 IS SHOWN ON R-602 AND R-604.",
            (84, 240), TXT["small"], "S-TEXT")

    V.loading_panel(sh, 340, 552, 298, FROZEN, TXT["small"], 3.05,
                    heading="FROZEN GEOMETRY AND NBC 2016 CHECK")
    y = V.loading_panel(sh, 340, 470, 298, NOT_BLAST, TXT["small"], 3.05,
                        heading="STATUS - NOT A BLAST ELEMENT")
    yk = V.markkey(sh, 340, y - 6, ["ST01", "ST02", "ST03", "ST04", "ST05", "ST06"], 298)
    # QA1: chained off the block above so the two can never collide
    V.bbs_extract(sh, 340, yk - 8, ["ST01", "ST02", "ST03", "ST04", "ST05", "ST06"])
    V.materials_panel(sh, 648, 552, 183)
    sh.titleblock(scale="1:25", sheet_of="19 OF 30")
    return sh.save(os.path.join(OUT, "R-601_Main_Staircase_Reinforcement_Plan.dxf"))


def r602():
    sh = Sheet("R-602", "MAIN STAIRCASE SECTIONS",
               "SECTION A-A LONGITUDINAL · FLIGHT CROSS-SECTION · LANDING SECTION",
               flags=["GEOMETRY FROZEN"])
    sh.sheet_header()
    sc = 25
    Pm = vw(sc, 90, 210)
    # longitudinal: x = plan Y direction, y = level
    # levels relative to (-)6.100 = 0
    lv = {"arr": 0, "L1": 1366.664, "L2": 2733.328, "top": 4100}
    # arrival landing / mat
    sh.rect(*Pm(600, -200), *Pm(1800, 0), "S-CONCRETE")
    sh.rect(*Pm(3760, lv["L1"] - 200), *Pm(4960, lv["L1"]), "S-CONCRETE")
    sh.rect(*Pm(600, lv["L2"] - 200), *Pm(1800, lv["L2"]), "S-CONCRETE")
    sh.rect(*Pm(3760, lv["top"] - 900), *Pm(5600, lv["top"]), "S-CONCRETE")
    for pts in ([Pm(600, -200), Pm(1800, -200), Pm(1800, 0), Pm(600, 0)],
                [Pm(3760, lv["L1"] - 200), Pm(4960, lv["L1"] - 200),
                 Pm(4960, lv["L1"]), Pm(3760, lv["L1"])],
                [Pm(600, lv["L2"] - 200), Pm(1800, lv["L2"] - 200),
                 Pm(1800, lv["L2"]), Pm(600, lv["L2"])],
                [Pm(3760, lv["top"] - 900), Pm(5600, lv["top"] - 900),
                 Pm(5600, lv["top"]), Pm(3760, lv["top"])]):
        sh.concrete_hatch(pts)
    # three flights
    for (y0, y1, l0, l1) in [(1800, 3760, 0, lv["L1"]),
                             (3760, 1800, lv["L1"], lv["L2"]),
                             (1800, 3760, lv["L2"], lv["top"])]:
        sh.pline([Pm(y0, l0), Pm(y1, l1), Pm(y1, l1 - 230), Pm(y0, l0 - 230)],
                 "S-CONCRETE", close=True)
        sh.concrete_hatch([Pm(y0, l0), Pm(y1, l1), Pm(y1, l1 - 230), Pm(y0, l0 - 230)])
        n = 8
        for i in range(n):
            t = i / n
            xx = y0 + (y1 - y0) * t
            yy = l0 + (l1 - l0) * t
            sh.line(Pm(xx, yy), Pm(xx, yy + 170.8333), "S-CONCRETE-THIN")
            sh.line(Pm(xx, yy + 170.8333),
                    Pm(xx + (280 if y1 > y0 else -280), yy + 170.8333),
                    "S-CONCRETE-THIN")
        # main bar on the underside
        sh.pline([Pm(y0, l0 - 130), Pm(y1, l1 - 130)], "S-REBAR-MAIN")
        # top bar for 800 into the flight
        d = 1 if y1 > y0 else -1
        sh.pline([Pm(y0, l0 - 40), Pm(y0 + d * 800, l0 + (l1 - l0) * 800 /
                                      abs(y1 - y0) - 40)], "S-REBAR-SEC")
        sh.pline([Pm(y1, l1 - 40), Pm(y1 - d * 800, l1 - (l1 - l0) * 800 /
                                      abs(y1 - y0) - 40)], "S-REBAR-SEC")
    for lab, y, l in [("(-)6.100 ARRIVAL", 1200, 0), ("(-)4.7333 L1", 4360, lv["L1"]),
                      ("(-)3.3667 L2", 1200, lv["L2"]), ("(-)2.000", 4600, lv["top"])]:
        sh.level(Pm(y, l), lab)
    sh.dim_v(Pm(600, 0), Pm(600, lv["L1"]), Pm(200, 0)[0], sc)
    sh.dim_v(Pm(600, lv["L1"]), Pm(600, lv["L2"]), Pm(200, 0)[0], sc)
    sh.dim_v(Pm(600, lv["L2"]), Pm(600, lv["top"]), Pm(200, 0)[0], sc)
    sh.dim_v(Pm(6000, 0), Pm(6000, lv["top"]), Pm(6400, 0)[0], sc)
    sh.dim_h(Pm(1800, -200), Pm(3760, -200), Pm(0, -900)[1], sc)
    sh.text("8R @ 170.8333 = 1366.664 PER FLIGHT   ·   TOTAL RISE 4100   ·   TREAD 280",
            Pm(600, -1600), TXT["small"], "S-TEXT")
    sh.text("HEADROOM 2533", Pm(2600, lv["L2"] + 700), TXT["small"], "S-TEXT")
    V.balloon(sh, (160, 300), "ST01", Pm(2600, lv["L1"] / 2 - 130))
    V.balloon(sh, (250, 420), "ST03", Pm(4200, lv["L2"] + 300))
    V.balloon(sh, (110, 268), "ST04", Pm(1200, -140))
    sh.view_title((84, 552), "V1", "SECTION A-A  -  MAIN STAIRCASE, LONGITUDINAL",
                  "SCALE 1:25")

    # V2 flight cross-section 1:10
    sc2 = 10
    Pm2 = vw(sc2, 380, 300)
    sh.pline([Pm2(0, 0), Pm2(1200, 0), Pm2(1200, 200), Pm2(0, 200)],
             "S-CONCRETE", close=True)
    sh.concrete_hatch([Pm2(0, 0), Pm2(1200, 0), Pm2(1200, 200), Pm2(0, 200)])
    for x in range(36, 1200, 150):
        sh.bar_dot(Pm2(x, 36), 1.1, "S-REBAR-MAIN")
    for x in range(100, 1200, 200):
        sh.bar_dot(Pm2(x, 164), 1.0, "S-REBAR-DIST")
    sh.dim_h(Pm2(0, 0), Pm2(1200, 0), Pm2(0, -200)[1], sc2)
    sh.dim_v(Pm2(1200, 0), Pm2(1200, 200), Pm2(1400, 0)[0], sc2)
    sh.text("T12 @ 150 MAIN", Pm2(1500, 20), TXT["small"], "S-TEXT")
    sh.text("T10 @ 200 DISTRIBUTION", Pm2(1500, 150), TXT["small"], "S-TEXT")
    sh.text("COVER 30", Pm2(0, -420), TXT["small"], "S-TEXT")
    V.balloon(sh, (370, 264), "ST01", Pm2(300, 36))
    V.balloon(sh, (370, 350), "ST02", Pm2(300, 164))
    sh.view_title((370, 552), "V2", "FLIGHT CROSS-SECTION - WAIST 200", "SCALE 1:10")

    # V3 landing section 1:20
    sc3 = 20
    Pm3 = vw(sc3, 380, 200)
    sh.rect(*Pm3(0, 0), *Pm3(400, 1200), "S-CONCRETE")
    sh.rect(*Pm3(3200, 0), *Pm3(3600, 1200), "S-CONCRETE")
    sh.rect(*Pm3(0, 1000), *Pm3(3600, 1200), "S-CONCRETE")
    for pts in ([Pm3(0, 0), Pm3(400, 0), Pm3(400, 1200), Pm3(0, 1200)],
                [Pm3(3200, 0), Pm3(3600, 0), Pm3(3600, 1200), Pm3(3200, 1200)],
                [Pm3(400, 1000), Pm3(3200, 1000), Pm3(3200, 1200), Pm3(400, 1200)]):
        sh.concrete_hatch(pts)
    sh.bar_run(Pm3(250, 1036), Pm3(3350, 1036), 125, sc3, "S-REBAR-MAIN", 0.6)
    sh.pline([Pm3(250, 1036), Pm3(3350, 1036)], "S-REBAR-MAIN")
    sh.pline([Pm3(150, 1164), Pm3(1300, 1164)], "S-REBAR-SEC")
    sh.pline([Pm3(2300, 1164), Pm3(3450, 1164)], "S-REBAR-SEC")
    sh.dim_h(Pm3(400, 1000), Pm3(3200, 1000), Pm3(0, 300)[1], sc3)
    sh.dim_h(Pm3(0, 0), Pm3(3600, 0), Pm3(0, -400)[1], sc3)
    sh.dim_v(Pm3(3600, 1000), Pm3(3600, 1200), Pm3(4000, 0)[0], sc3)
    sh.text("Leff = 2800 + 200 = 3000  (IS 456 Cl. 22.2(a))", Pm3(200, 1700),
            TXT["small"], "S-TEXT")
    V.balloon(sh, (450, 236), "ST04", Pm3(1800, 1036))
    V.balloon(sh, (400, 292), "ST05", Pm3(800, 1164))
    sh.view_title((370, 300), "V3", "LANDING SECTION - SPANNING ACROSS THE SHAFT",
                  "SCALE 1:20")

    y = V.loading_panel(sh, 30, 200, 330, [
        "FLIGHT - WAIST 200, IS 456 with NORMAL partial factors",
        "  theta = arctan(170.833/280) = 31.4 deg, cos theta = 0.8535",
        "  waist self 0.200 x 25 / 0.8535          =  5.858 kPa",
        "  steps 0.5 x 0.170833 x 25  (Cl. 33.2)   =  2.135 kPa",
        "  finishes                                 =  1.000 kPa",
        "  live, IS 875 Pt 2, plant + escape route  =  5.000 kPa",
        "  total 13.99  ->  wu = 1.5 x 13.99        =  21.0 kPa",
        "  Leff = going + min(landing/2, 1000) each end (Cl. 33.1(b))",
        "       = 1960 + 600 + 600                  =  3160 mm",
        "  d = 200 - 30 - 6 = 164 ; M = wu Leff2/8  =  26.2 kNm/m",
        "  Ast,req 380 ; Cl. 26.5.2.1 min 240",
        "  ADOPTED  T12 @ 150 MAIN (754)  ->  Mu 50.3, UTILISATION 52 %",
        "           T10 @ 200 DISTRIBUTION (393)",
        "           T12 @ 150 TOP for 0.25 Leff = 800 into the flight, Ld 480",
        "  DEFLECTION  Leff/d 19.3 ; basic 20 ; fs 146 ; pt 0.46 % ; MF ~1.9",
        "              permissible 38 >> 19.3   OK",
        "  SHEAR  V 33.2 kN/m ; tau_v 0.202 < tau_c 0.479 x k 1.20 (Cl. 40.2.1.1)",
        "         = 0.575   ->  NO LINKS REQUIRED",
        "",
        "LANDINGS L1 / L2 / ARRIVAL - 200, SPANNING ACROSS THE 2800 SHAFT",
        "  self 7.50 + finishes 1.50 + live 7.50 + flight reaction 27.70 = 44.20 kPa",
        "  Leff = 2800 + 200 bearing (Cl. 22.2(a))  =  3000 mm",
        "  M = 44.2 x 3.000^2 / 8                   =  49.7 kNm/m",
        "  Ast,req 745 ;  T12 @ 150 gives 754 = 100 %  -  TOO TIGHT",
        "  ADOPTED  T12 @ 125 BOTTOM (905)  ->  Mu 59.5, UTILISATION 84 %",
        "           T12 @ 125 TOP for 900 from each support ; T10 @ 200 distribution",
        "  DEFLECTION 3000/164 = 18.3 ; fs 239 ; pt 0.552 % ; MF ~1.35 -> 27 > 18.3 OK",
        "  SHEAR  V 66.3 kN/m ; tau_v 0.404 < tau_c 0.519 x 1.20 = 0.622   OK",
        "",
        "MANUAL CALCULATION - NOT DIRECT STAAD OUTPUT.",
    ], TXT["small"], 3.05, heading="MAIN STAIRCASE - DESIGN (IS 456, NOT IS 4991)")
    V.bbs_extract(sh, 648, 552, ["ST01", "ST02", "ST03", "ST04", "ST05", "ST06"])
    sh.panel(648, 470, 183, "WHY T12 @ 125 AND NOT @ 150", [
        "The landing needs 745 mm2/m.",
        "T12 @ 150 provides 754 mm2/m.",
        "",
        "That is 100.1 % of requirement - a margin of",
        "9 mm2/m, or about one per cent of one bar.",
        "",
        "IT IS TOO TIGHT TO BUILD TO.  A single bar",
        "displaced to clear a service, or a 10 mm",
        "setting-out error on the landing span, would",
        "put the section into deficit.",
        "",
        "T12 @ 125 gives 905 mm2/m and 84 % utilisation.",
        "The extra steel costs almost nothing; the RFI",
        "it avoids does not.",
    ], TXT["small"], 3.05)
    sh.titleblock(scale="1:25, 1:20, 1:10", sheet_of="20 OF 30")
    return sh.save(os.path.join(OUT, "R-602_Main_Staircase_Sections.dxf"))


def r603():
    sh = Sheet("R-603", "ENTRY STAIRWELL REINFORCEMENT",
               "12R @ 166.6667 / 300 · WAIST 250 · OUTSIDE THE PROTECTIVE BOUNDARY",
               flags=["C16 OPEN", "NOT BLAST RATED"])
    sh.sheet_header()
    sc = 40
    Pm = vw(sc, 60, 300)
    A = P.ASW
    # longitudinal section: x = project X, y = level x (-1) from grade
    sh.pline([Pm(9250, 0), Pm(9500, 0), Pm(9500, -2000), Pm(15800, -2000),
              Pm(16050, -2000), Pm(16050, 900), Pm(9250, 900)], "S-CONCRETE", close=True)
    sh.rect(*Pm(9500, 0), *Pm(11000, -250), "S-CONCRETE")
    sh.concrete_hatch([Pm(9500, 0), Pm(11000, 0), Pm(11000, -250), Pm(9500, -250)])
    sh.pline([Pm(11000, 0), Pm(14300, -2000), Pm(14300, -2250), Pm(11000, -250)],
             "S-CONCRETE", close=True)
    sh.concrete_hatch([Pm(11000, 0), Pm(14300, -2000), Pm(14300, -2250), Pm(11000, -250)])
    sh.rect(*Pm(14300, -2000), *Pm(15800, -2250), "S-CONCRETE")
    sh.concrete_hatch([Pm(14300, -2000), Pm(15800, -2000), Pm(15800, -2250),
                       Pm(14300, -2250)])
    for i in range(12):
        t = i / 12
        x = 11000 + 3300 * t
        y = -2000 * t
        sh.line(Pm(x, y), Pm(x, y - 166.6667), "S-CONCRETE-THIN")
        sh.line(Pm(x, y - 166.6667), Pm(x + 300, y - 166.6667), "S-CONCRETE-THIN")
    # roof
    sh.pline([Pm(9250, 2450), Pm(16050, 450), Pm(16050, 200), Pm(9250, 2200)],
             "S-CONCRETE", close=True)
    sh.concrete_hatch([Pm(9250, 2450), Pm(16050, 450), Pm(16050, 200), Pm(9250, 2200)])
    # main steel
    sh.pline([Pm(10250, -120), Pm(11000, -120), Pm(14300, -2120), Pm(15050, -2120)],
             "S-REBAR-MAIN")
    sh.pline([Pm(11000, -60), Pm(12200, -790)], "S-REBAR-SEC")
    sh.pline([Pm(14300, -2060), Pm(13100, -1330)], "S-REBAR-SEC")
    sh.level(Pm(10200, 0), "0.000 GRADE")
    sh.level(Pm(15000, -2000), "(-)2.000 PLATFORM")
    sh.level(Pm(9400, 2450), "+2.450")
    sh.dim_h(Pm(11000, -2250), Pm(14300, -2250), Pm(0, -2900)[1], sc)
    sh.dim_h(Pm(9500, -2250), Pm(11000, -2250), Pm(0, -2900)[1], sc)
    sh.dim_h(Pm(14300, -2250), Pm(15800, -2250), Pm(0, -2900)[1], sc)
    sh.dim_v(Pm(16050, -2000), Pm(16050, 0), Pm(16600, 0)[0], sc)
    V.balloon(sh, (334, 258), "E01", Pm(12600, -1500))
    V.balloon(sh, (250, 322), "E03", Pm(11700, -480))
    V.balloon(sh, (150, 400), "E05A", Pm(11000, 1700))
    V.balloon(sh, (110, 322), "E06", Pm(10200, -120))
    V.balloon(sh, (398, 258), "E07", Pm(15100, -2120))
    sh.view_title((30, 552), "V1", "ENTRY STAIRWELL - LONGITUDINAL SECTION", "SCALE 1:40")
    sh.text("*** C16 OPEN - THE ROOF / PLATFORM JUNCTION IS NOT RESOLVED.  DETAILED AT 250. ***",
            (30, 230), TXT["small"], "S-BLAST")

    # V2 transverse section
    sc2 = 25
    Pm2 = vw(sc2, 460, 300)
    sh.rect(*Pm2(0, 0), *Pm2(250, 2900), "S-CONCRETE")
    sh.rect(*Pm2(1750, 0), *Pm2(2000, 2900), "S-CONCRETE")
    sh.rect(*Pm2(0, 0), *Pm2(2000, -300), "S-CONCRETE")
    sh.rect(*Pm2(0, 2900), *Pm2(2000, 3150), "S-CONCRETE")
    for pts in ([Pm2(0, 0), Pm2(250, 0), Pm2(250, 2900), Pm2(0, 2900)],
                [Pm2(1750, 0), Pm2(2000, 0), Pm2(2000, 2900), Pm2(1750, 2900)],
                [Pm2(0, -300), Pm2(2000, -300), Pm2(2000, 0), Pm2(0, 0)],
                [Pm2(0, 2900), Pm2(2000, 2900), Pm2(2000, 3150), Pm2(0, 3150)]):
        sh.concrete_hatch(pts)
    for xo in (56, 194):
        sh.line(Pm2(xo, 40), Pm2(xo, 2860), "S-REBAR-MAIN")
        sh.line(Pm2(2000 - xo, 40), Pm2(2000 - xo, 2860), "S-REBAR-MAIN")
        sh.bar_run(Pm2(xo, 200), Pm2(xo, 2800), 200, sc2, "S-REBAR-MAIN", 0.6)
        sh.bar_run(Pm2(2000 - xo, 200), Pm2(2000 - xo, 2800), 200, sc2, "S-REBAR-MAIN", 0.6)
    sh.bar_run(Pm2(300, 2956), Pm2(1700, 2956), 200, sc2, "S-REBAR-MAIN", 0.6)
    sh.bar_run(Pm2(300, 3094), Pm2(1700, 3094), 200, sc2, "S-REBAR-MAIN", 0.6)
    sh.dim_h(Pm2(250, 0), Pm2(1750, 0), Pm2(0, -700)[1], sc2)
    sh.dim_h(Pm2(0, 0), Pm2(2000, 0), Pm2(0, -1300)[1], sc2)
    sh.dim_v(Pm2(2000, 0), Pm2(2000, 2900), Pm2(2500, 0)[0], sc2)
    V.balloon(sh, (450, 350), "E04A", Pm2(56, 1800))
    V.balloon(sh, (560, 424), "E05B", Pm2(1000, 3094))
    sh.view_title((440, 552), "V2", "TRANSVERSE SECTION", "SCALE 1:25")

    y = V.loading_panel(sh, 30, 224, 330, [
        "STATUS: OUTSIDE THE PROTECTIVE BOUNDARY, NOT BLAST RATED (Rev F note 8).",
        "EXPECTED TO BE LOST IN THE DESIGN EVENT.  DECLARED EXPENDABLE.",
        "Designed to IS 456 with NORMAL partial factors.",
        "",
        "FLIGHT  12R @ 166.6667 / 300, 1500 wide, waist 250",
        "  theta 29.05 deg ; waist 7.150 + steps 2.083 + finishes 1.000 + live 5.000",
        "  = 15.233  ->  wu = 22.85 kPa",
        "  Leff = 3300 + 750 + 750 (Cl. 33.1(b))    =  4800 mm ;  d = 214",
        "  M = 22.85 x 4.800^2 / 8                  =  65.8 kNm/m ; Ast,req 744",
        "  ADOPTED  T16 @ 200 MAIN (1005) -> Mu 87.3, UTIL 75 %, x/d 0.162",
        "           T10 @ 200 DISTRIBUTION ; T16 @ 200 TOP for 1200, Ld 640",
        "  DEFLECTION 4800/214 = 22.4 ; fs 215 ; pt 0.470 % ; MF ~1.5 -> 30  OK",
        "  SHEAR V 54.8 kN/m ; tau_v 0.256 < tau_c 0.484 x k 1.10 = 0.532  NO LINKS",
        "",
        "SIDE WALLS 250, retained 2.9 m, propped by the roof and the raft",
        "  sigma_h base = 0.5 x 20 x 2.900 + 0.5 x 10  =  34 kPa",
        "  M ~ w L2 / 12 on an equivalent 20 kPa UDL   =  14.0 kNm/m ; Ast,req 168",
        "  Cl. 32.5(a) 300 · Cl. 32.5(b) 500 · Cl. 32.5(c) two curtains  OK",
        "  ADOPTED  T12 @ 200 EF EW (565/face) - MINIMUM STEEL GOVERNS, 31 % used",
        "",
        "RAKING ROOF 250, 1500 clear",
        "  self 6.25 + wp/screed 2.0 + earth lap 5.4 + IMPOSED 20 = 33.65 -> wu 50.5",
        "  (20 kPa imposed taken DELIBERATELY, for a stray vehicle on the berm)",
        "  M = w l2 / 12 = 9.5 kNm/m ; Ast,req 108 ; min 300 GOVERNS",
        "  ADOPTED  T12 @ 200 EF EW  ->  20 % utilised",
        "",
        "TOP LANDING 250  wu 54.9 ; Leff 1750 ; M 21.0 kNm/m -> T12 @ 200 EF EW, 41 %",
        "PLATFORM · HEADWALL · STEPPED RAFT 300   T12 @ 200 EF EW, nominal",
        "",
        "MANUAL CALCULATION - NOT DIRECT STAAD OUTPUT.",
    ], TXT["small"], 3.05, heading="ENTRY STAIRWELL - DESIGN")
    V.markkey(sh, 370, 224, ["E01", "E02", "E03", "E04A", "E04B", "E05A", "E05B",
                             "E06", "E07", "E08A", "E08B", "E09A", "E09B", "E10",
                             "E11", "E12"], 268)
    V.bbs_extract(sh, 648, 552, ["E01", "E02", "E03", "E04A", "E04B", "E05A", "E05B",
                                 "E06", "E07"])
    sh.titleblock(scale="1:40, 1:25", sheet_of="21 OF 30")
    return sh.save(os.path.join(OUT, "R-603_Entry_Stairwell_Reinforcement.dxf"))


def r604():
    sh = Sheet("R-604", "STAIR CONNECTION DETAILS",
               "THE OPENING CORNER · FLIGHT / LANDING JUNCTIONS · SUPPORT STEEL",
               flags=["C16 OPEN"])
    sh.sheet_header()
    # V1 the opening corner at the TOP of the flight - 209 deg
    sc = 12
    Pm = vw(sc, 155, 480)
    sh.pline([Pm(-1500, 0), Pm(0, 0), Pm(1400, -800), Pm(1400, -1090),
              Pm(0, -290), Pm(-1500, -290)], "S-CONCRETE", close=True)
    sh.concrete_hatch([Pm(-1500, 0), Pm(0, 0), Pm(1400, -800), Pm(1400, -1090),
                       Pm(0, -290), Pm(-1500, -290)])
    # WRONG way shown crossed out
    sh.pline([Pm(-1400, -215), Pm(-40, -215), Pm(1300, -1015)], "S-REBAR-DIST")
    sh.text("BAR BENT ROUND THE CORNER - NOT PERMITTED", Pm(-1500, -1500),
            TXT["small"], "S-BLAST")
    sh.line(Pm(-1300, -1420), Pm(-500, -1560), "S-BLAST")
    sh.line(Pm(-1300, -1560), Pm(-500, -1420), "S-BLAST")
    # CORRECT: straight, crossed, anchored into the opposite face
    sh.pline([Pm(-1400, -215), Pm(700, -215)], "S-REBAR-MAIN")
    sh.pline([Pm(1300, -1015), Pm(-100, -215)], "S-REBAR-MAIN")
    sh.pline([Pm(-500, -60), Pm(0, -60), Pm(500, -350)], "S-REBAR-SEC")
    sh.dim_h(Pm(0, -290), Pm(640, -290), Pm(0, -700)[1], sc)
    sh.text("Ld 640 INTO THE OPPOSITE FACE", Pm(-1500, -900), TXT["small"], "S-TEXT")
    V.balloon(sh, (44, 452), "E01", Pm(-1000, -215))
    V.balloon(sh, (216, 466), "E12", Pm(200, -60))
    sh.view_title((25, 516), "V1", "THE OPENING CORNER - TOP OF THE ENTRY FLIGHT",
                  "SCALE 1:12")

    # V2 foot of the flight
    Pm2 = vw(sc, 425, 500)
    sh.pline([Pm2(-1400, -1000), Pm2(0, -200), Pm2(1500, -200), Pm2(1500, -490),
              Pm2(0, -490), Pm2(-1400, -1290)], "S-CONCRETE", close=True)
    sh.concrete_hatch([Pm2(-1400, -1000), Pm2(0, -200), Pm2(1500, -200),
                       Pm2(1500, -490), Pm2(0, -490), Pm2(-1400, -1290)])
    sh.pline([Pm2(-1300, -1215), Pm2(0, -415), Pm2(1400, -415)], "S-REBAR-MAIN")
    sh.pline([Pm2(-600, -1000), Pm2(0, -260), Pm2(1200, -260)], "S-REBAR-SEC")
    sh.text("CORNER CLOSES (151 deg) - BARS MAY TURN NORMALLY", Pm2(-1400, -1700),
            TXT["small"], "S-TEXT")
    V.balloon(sh, (318, 402), "E01", Pm2(-900, -1000))
    V.balloon(sh, (500, 448), "E03", Pm2(600, -260))
    sh.view_title((300, 516), "V2", "FOOT OF THE ENTRY FLIGHT", "SCALE 1:12")

    # V3 main stair flight / landing junction
    sc3 = 12
    Pm3 = vw(sc3, 40, 200)
    sh.rect(*Pm3(0, 0), *Pm3(1200, 200), "S-CONCRETE")
    sh.concrete_hatch([Pm3(0, 0), Pm3(1200, 0), Pm3(1200, 200), Pm3(0, 200)])
    sh.pline([Pm3(1200, 0), Pm3(2400, 732), Pm3(2400, 962), Pm3(1200, 230)],
             "S-CONCRETE", close=True)
    sh.concrete_hatch([Pm3(1200, 0), Pm3(2400, 732), Pm3(2400, 962), Pm3(1200, 230)])
    sh.pline([Pm3(80, 36), Pm3(1200, 36), Pm3(2350, 738)], "S-REBAR-MAIN")
    sh.pline([Pm3(80, 164), Pm3(1100, 164), Pm3(1900, 654)], "S-REBAR-SEC")
    sh.dim_h(Pm3(1200, 230), Pm3(2000, 230), Pm3(0, 1300)[1], sc3)
    sh.text("TOP STEEL 800 INTO THE FLIGHT, Ld 480 BEYOND", Pm3(0, 1500),
            TXT["small"], "S-TEXT")
    V.balloon(sh, (34, 186), "ST01", Pm3(600, 36))
    V.balloon(sh, (34, 226), "ST03", Pm3(600, 164))
    sh.view_title((25, 348), "V3", "MAIN STAIR - FLIGHT / LANDING JUNCTION",
                  "SCALE 1:12")

    y = V.loading_panel(sh, 300, 326, 338, [
        "*** THE DETAIL MOST OFTEN GOT WRONG ***",
        "",
        "At the TOP of the entry flight the tension face turns through 209 DEGREES.",
        "A bar bent round that corner has its BEND RESULTANT DIRECTED OUT OF THE",
        "CONCRETE: it spalls the cover and the bar loses its anchorage entirely.",
        "",
        "MAIN BARS SHALL NOT BE BENT ROUND IT.",
        "  ·  Each layer is continued STRAIGHT,",
        "  ·  CROSSED past the corner, and",
        "  ·  ANCHORED Ld = 640 INTO THE OPPOSITE FACE,",
        "  ·  plus a U-BAR T16 @ 200 ACROSS THE CORNER  (mark E12).",
        "[SP 34:1987 Cl. 5.5 and standard detailing practice]",
        "",
        "At the FOOT of the flight the corner CLOSES (151 deg) and bars may turn",
        "normally.  The two corners are NOT interchangeable.",
        "",
        "MAIN STAIRCASE JUNCTIONS",
        "  ·  Flight top steel ST03: T12 @ 150 for 0.25 Leff = 800 into the flight,",
        "     anchored Ld 480 into the landing.",
        "  ·  Landing top steel ST05: T12 @ 125 for 900 from each support.",
        "  ·  The arrival landing at (-)6.100 IS the mat surface - the flight bars",
        "     lap into the mat top curtain.",
        "  ·  Flight 3 lands on the 900 pressure-slab pad at (-)2.000 - the flight",
        "     bars lap into the pad top steel S03B.",
        "",
        "*** C16 OPEN ***  The roof / platform junction of the entry stairwell is",
        "NOT RESOLVED.  Master A.4.7 says the roof over the platform becomes the",
        "500 headhouse roof; B.6, A.7.6 and F.2 design, load and register a 250",
        "roof, and the headhouse footprint (Y 200-6000) does not overlap the",
        "platform (Y 6000-7500).  THIS PACKAGE DETAILS 250 and flags the junction.",
        "THE A.4.7 CLAUSE IS NOT EDITED.  A user ruling is required.",
    ], TXT["small"], 3.05, heading="THE OPENING CORNER - SP 34 Cl. 5.5")
    V.bbs_extract(sh, 300, y - 8, ["E01", "E03", "E12", "ST01", "ST03", "ST04", "ST05"])
    V.materials_panel(sh, 648, 552, 183)
    sh.titleblock(scale="1:12", sheet_of="22 OF 30")
    return sh.save(os.path.join(OUT, "R-604_Stair_Connection_Details.dxf"))


def build():
    os.makedirs(OUT, exist_ok=True)
    return [r601(), r602(), r603(), r604()]


if __name__ == "__main__":
    for f in build():
        print("written", f)
