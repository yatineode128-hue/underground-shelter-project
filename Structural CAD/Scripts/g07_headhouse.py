"""g07_headhouse.py  --  R-701, R-702, R-703."""
import os, math
import sc_proj as P
import sc_dxflib as D
import sc_views as V
import rebar_data as R
from sc_dxflib import Sheet, vw, TXT

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "DXF", "Headhouse"))
OUTE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "DXF", "Entrance"))

HH_ROOF = [
    "GOVERNING COMBINATION  103 BLAST,  w = 396.5 kPa",
    "  = 383 blast + 12.5 self + 1.0 SIDL   (IS 4991 Cl. 7.2, flush at the",
    "  berm crest, NO earth cover on the headhouse roof)",
    "",
    "THREE ANALYSES RUN, THE MOST CONSERVATIVE ADOPTED",
    "  1  One-way fixed-fixed strip, Mp = w Ln2/16   =  396.5 kNm/m   <- ADOPTED",
    "  2  IS 456 Table 26 Case 1, ax- = 0.045 at 1.25 =  285.5 kNm/m",
    "  3  Yield line, fixed 4 edges, isotropic        =  162.2 kNm/m",
    "",
    "  Method 3 formula  wu = 48 m / [a2 (sqrt(3 + (a/b)2) - a/b)2]",
    "  VALIDATION: as b -> infinity, 48/3 = 16 = the fixed-fixed strip w L2/16.",
    "  (The 24-coefficient version gives 8 = SIMPLY SUPPORTED w L2/8.)",
    "  An earlier yield-line coefficient error (324.4 -> 162.2, ERR-1) was found",
    "  and corrected in the project record.  NO REINFORCEMENT CHANGED.",
    "",
    "FLEXURE   d = 500 - 75 - 10 = 415 ;  Mu,lim 1002 kNm/m  OK",
    "  Ast,req 1879 mm2/m ;  Cl. 26.5.2.1 min 0.12 % x 500 = 600",
    "  PROVIDED T20 @ 150 EF EW = 2094  ->  Mu 438.5 kNm/m",
    "  UTILISATION  90 % one-way  |  65 % Table 26  |  37 % yield line",
    "  xu 72.3, x/d 0.174 << 0.46",
    "  *** 90 % IS THE TIGHTEST ELEMENT IN THIS PACKAGE ***",
    "",
    "SHEAR  -  NEW AND MANDATORY, NOT IN THE PHASE 1 REPORT",
    "  V at d = 396.5 (2.000 - 0.415)             =  628.4 kN/m",
    "  tau_v 1.514 | tau_c 0.502 (pt 0.505 %, read at the STATIC M35 value -",
    "  IS 4991 Cl. 10.3.1.1) | tau_c,max 3.70  OK",
    "  Vus 420.0 ; Asv/sv 2.327  ->  T12 4-leg at 194 ; Cl. 26.5.1.5 limit 300",
    "  PROVIDED  T12 4-LEG @ 175 IN THE END 1200 EACH SIDE ; @ 250 ELSEWHERE",
    "",
    "DETAILING   NO OPENING IN THE HEADHOUSE ROOF - the stair void is in the",
    "FLOOR.  Corner torsion steel (Cl. D-1.8) NOT REQUIRED: all four edges carry",
    "full T20 @ 150 hogging steel continuous into the walls.  Haunch 300 x 300",
    "at all four wall-roof junctions, diagonal T16 @ 150.  Top steel continuous",
    "over every support, anchored Ld = 800 into the wall.",
    "",
    "CONFLICT C2 RESOLVED: the Phase 1 report designed this roof for a 3.0 m span",
    "with 1.0 m of cover.  Rev F is 4.0 m with NO cover.  RECOMPUTED - T20 @ 150",
    "survives at 90 %, but THE SHEAR LINKS ARE NEW AND MANDATORY.",
    "",
    "MANUAL CALCULATION - NOT DIRECT STAAD OUTPUT.",
]

HH_WALL = [
    "                              CASE A (report)     CASE B (ADOPTED)",
    "Lateral pressure              113 kPa drag        383 kPa full envelope",
    "Mp = w x 2.400^2 / 16         40.7 kNm/m          137.9 kNm/m",
    "Ast,req                       221 mm2/m           766 mm2/m",
    "Cl. 32.5(a) min vertical      480 - governs       480",
    "Cl. 32.5(b) min horizontal    800 - governs       800 - still governs",
    "Utilisation on T16@150 EF EW  17 %                59 %",
    "Shear V at d                  97.0 kN/m           328.6 kN/m",
    "tau_v                         0.283               0.961",
    "tau_c (pt 0.392 %)            0.444               0.444",
    "VERDICT                       NO LINKS            LINKS REQUIRED",
    "",
    "WHY CASE B - CONFLICT C10, RESOLVED",
    "The walls sit behind about 2.5 m of berm and EARTH TRANSMITS PRESSURE.",
    "Ka for dry compacted fill is [ASSUMED - master K.2 item A6] and cannot be",
    "verified, so the walls are designed for the FULL 383 kPa UPPER BOUND.",
    "COST OF THE UPGRADE: ONE LINK CAGE (T12 4-LEG @ 250).  Utilisation rises",
    "from 17 % to 59 %.  The assumption is thereby REMOVED FROM THE CRITICAL PATH.",
    "",
    "d = 400 - 50 - 8 = 342 ; Mu,lim 681 kNm/m",
    "ADOPTED  T16 @ 150 EF EW = 1340  ->  Mu 235.2, UTIL 59 %, x/d 0.135",
    "  Vus 176.9 ; Asv/sv 1.189 -> T12 4-leg at 381 ; Cl. 26.5.1.5 limit 256 GOVERNS",
    "ADOPTED  T12 4-LEGGED LINKS @ 250 THROUGHOUT ALL FOUR WALLS",
    "",
    "AXIAL  roof reaction two-way (Cl. 24.5): HW3/HW4 trapezoid 476 kN/m,",
    "  HW1/HW2 triangle 396 kN/m ; one-way bound 793 kN/m ; self 29 kN/m",
    "  worst N = 822 kN/m  ->  f = 2.06 N/mm2 = 12 % of 0.4 fck,dyn   NOT CRITICAL",
    "",
    "*** PRESSURE ACTS FROM INSIDE TOO. ***  The inner security door is NOT blast",
    "rated and the entry stairwell is expected to be lost, so the headhouse FILLS",
    "and the walls are pushed OUTWARDS.  THE WALLS ARE REINFORCED SYMMETRICALLY",
    "FOR 383 kPa EITHER WAY - A STATED REQUIREMENT, NOT AN ACCIDENT OF DETAILING.",
]


def r701():
    sh = Sheet("R-701", "HEADHOUSE REINFORCEMENT",
               "WALLS HW1-HW4 400 · ROOF 500 · UTILISATION 90 %",
               flags=["C10 RESOLVED - 383 kPa EITHER FACE"])
    sh.sheet_header()
    sc = 40
    Pm = vw(sc, 70, 380)
    H = P.HH
    sh.rect(*Pm(H["x0"], H["y0"]), *Pm(H["x1"], H["y1"]), "S-CONCRETE")
    sh.rect(*Pm(H["ix0"], H["iy0"]), *Pm(H["ix1"], H["iy1"]), "S-CONCRETE")
    sh.concrete_hatch([Pm(H["x0"], H["y0"]), Pm(H["x1"], H["y0"]),
                       Pm(H["x1"], H["y1"]), Pm(H["x0"], H["y1"])],
                      holes=[[Pm(H["ix0"], H["iy0"]), Pm(H["ix1"], H["iy0"]),
                              Pm(H["ix1"], H["iy1"]), Pm(H["ix0"], H["iy1"])]])
    for lab, x, y in [("HW1", 16000, 400), ("HW2", 16000, 5800),
                      ("HW3", 13800, 3100), ("HW4", 18200, 3100)]:
        sh.text(lab, Pm(x, y), TXT["small"], "S-TEXT", "CENTER")
    # security door in HW2
    sh.rect(*Pm(14450, 5600), *Pm(15350, 6000), "S-STEELWORK")
    sh.text("SECURITY DOOR 900 x 2100  NOT BLAST RATED", Pm(14000, 6250),
            TXT["small"], "S-TEXT")
    # roof steel diagrammatic
    for x in range(H["x0"] + 150, H["x1"], 450):
        sh.line(Pm(x, H["y0"] + 80), Pm(x, H["y1"] - 80), "S-REBAR-MAIN")
    for y in range(H["y0"] + 150, H["y1"], 450):
        sh.line(Pm(H["x0"] + 80, y), Pm(H["x1"] - 80, y), "S-REBAR-MAIN")
    # end link zones
    for x0, x1 in [(H["ix0"], H["ix0"] + 1200), (H["ix1"] - 1200, H["ix1"])]:
        sh.rect(*Pm(x0, H["iy0"]), *Pm(x1, H["iy1"]), "S-REBAR-STIRRUP")
    sh.text("END 1200 - T12 4-LEG @ 175", Pm(14050, 3100), TXT["small"],
            "S-REBAR-STIRRUP", "CENTER", 90)
    sh.text("MID - T12 4-LEG @ 250", Pm(16000, 3100), TXT["small"],
            "S-REBAR-STIRRUP", "CENTER")
    # HW3 band on the slab below
    sh.dline(Pm(13400, H["y0"]), Pm(13400, H["y1"]), "S-HIDDEN")
    sh.dline(Pm(14600, H["y0"]), Pm(14600, H["y1"]), "S-HIDDEN")
    sh.text("S16 BAND IN THE SLAB BELOW", Pm(13000, 2000), TXT["small"],
            "S-REBAR-SEC", "CENTER", 90)
    sh.dim_h(Pm(H["x0"], H["y0"]), Pm(H["x1"], H["y0"]), Pm(0, H["y0"] - 1400)[1], sc)
    sh.dim_h(Pm(H["ix0"], H["y0"]), Pm(H["ix1"], H["y0"]), Pm(0, H["y0"] - 800)[1], sc)
    sh.dim_v(Pm(H["x0"], H["y0"]), Pm(H["x0"], H["y1"]), Pm(H["x0"] - 1400, 0)[0], sc)
    sh.dim_v(Pm(H["x0"], H["iy0"]), Pm(H["x0"], H["iy1"]), Pm(H["x0"] - 800, 0)[0], sc)
    sh.north((560, 470))
    V.balloon(sh, (100, 500), "H01A", Pm(14600, 5400))
    V.balloon(sh, (240, 388), "H02", Pm(17600, 1200))
    V.balloon(sh, (176, 500), "H04A", Pm(16000, 5900))
    sh.secmark((56, 430), "D"); sh.secmark((300, 430), "D")
    sh.text("SECTION D-D  ->  BELOW", (180, 366), TXT["small"], "S-SECTION", "CENTER")
    sh.view_title((30, 552), "V1", "HEADHOUSE ROOF PLAN - REINFORCEMENT", "SCALE 1:40")
    sh.text("HEADHOUSE FLOOR = TOP OF THE 900 PRESSURE SLAB AT (-)2.000  ·  "
            "ROOF SOFFIT +0.400  ·  ROOF TOP +0.900  ·  NO EARTH COVER",
            (30, 358), TXT["small"], "S-TEXT")

    # V2 section D-D
    sc2 = 40
    Pm2 = vw(sc2, 70, 200)
    sh.rect(*Pm2(0, 0), *Pm2(400, 2400), "S-CONCRETE")
    sh.rect(*Pm2(4400, 0), *Pm2(4800, 2400), "S-CONCRETE")
    sh.rect(*Pm2(0, 2400), *Pm2(4800, 2900), "S-CONCRETE")
    sh.rect(*Pm2(-600, -900), *Pm2(5400, 0), "S-CONCRETE-THIN")
    for pts in ([Pm2(0, 0), Pm2(400, 0), Pm2(400, 2400), Pm2(0, 2400)],
                [Pm2(4400, 0), Pm2(4800, 0), Pm2(4800, 2400), Pm2(4400, 2400)],
                [Pm2(0, 2400), Pm2(4800, 2400), Pm2(4800, 2900), Pm2(0, 2900)]):
        sh.concrete_hatch(pts)
    sh.pline([Pm2(400, 2400), Pm2(700, 2400), Pm2(400, 2100)], "S-CONCRETE")
    sh.pline([Pm2(4400, 2400), Pm2(4100, 2400), Pm2(4400, 2100)], "S-CONCRETE")
    for xo in (58, 342):
        sh.line(Pm2(xo, 40), Pm2(xo, 2860), "S-REBAR-MAIN")
        sh.line(Pm2(4800 - xo, 40), Pm2(4800 - xo, 2860), "S-REBAR-MAIN")
    sh.line(Pm2(60, 2815), Pm2(4740, 2815), "S-REBAR-MAIN")
    sh.line(Pm2(60, 2485), Pm2(4740, 2485), "S-REBAR-MAIN")
    for yy in range(150, 2400, 250):
        sh.rect(*Pm2(50, yy - 60), *Pm2(350, yy + 60), "S-REBAR-STIRRUP")
        sh.rect(*Pm2(4450, yy - 60), *Pm2(4750, yy + 60), "S-REBAR-STIRRUP")
    for x in range(500, 1700, 175):
        sh.rect(*Pm2(x - 40, 2475), *Pm2(x + 40, 2825), "S-REBAR-STIRRUP")
        sh.rect(*Pm2(4800 - x - 40, 2475), *Pm2(4800 - x + 40, 2825), "S-REBAR-STIRRUP")
    for x in range(1900, 3000, 250):
        sh.rect(*Pm2(x - 40, 2475), *Pm2(x + 40, 2825), "S-REBAR-STIRRUP")
    # blast arrows both faces of a wall
    for y in range(300, 2400, 500):
        sh.pline([Pm2(-900, y), Pm2(-100, y)], "S-BLAST")
        sh.pline([Pm2(-300, y + 120), Pm2(-100, y), Pm2(-300, y - 120)], "S-BLAST")
        sh.pline([Pm2(1100, y), Pm2(500, y)], "S-BLAST")
        sh.pline([Pm2(700, y + 120), Pm2(500, y), Pm2(700, y - 120)], "S-BLAST")
    sh.text("383 kPa EITHER FACE", Pm2(-900, 2600), TXT["small"], "S-BLAST")
    sh.dim_h(Pm2(400, 0), Pm2(4400, 0), Pm2(0, -1500)[1], sc2)
    sh.dim_v(Pm2(4800, 0), Pm2(4800, 2400), Pm2(5600, 0)[0], sc2)
    sh.dim_v(Pm2(4800, 2400), Pm2(4800, 2900), Pm2(5600, 0)[0], sc2)
    sh.level(Pm2(2400, 2900), "+0.900")
    sh.level(Pm2(2400, 2400), "+0.400")
    sh.level(Pm2(2400, 0), "(-)2.000")
    V.balloon(sh, (48, 268), "H04A", Pm2(58, 1200))
    V.balloon(sh, (126, 288), "H05", Pm2(200, 900))
    V.balloon(sh, (110, 276), "H01C", Pm2(1600, 2815))
    V.balloon(sh, (94, 252), "H06", Pm2(560, 2280))
    sh.view_title((30, 340), "V2", "SECTION D-D  -  HEADHOUSE WALL AND ROOF", "SCALE 1:40")

    y = V.loading_panel(sh, 300, 552, 338, HH_ROOF, TXT["small"], 3.05,
                        heading="HEADHOUSE ROOF 500 - DESIGN BASIS")
    V.loading_panel(sh, 300, y - 6, 338, HH_WALL, TXT["small"], 3.05,
                    heading="HEADHOUSE WALLS 400 - CONFLICT C10")
    yk = V.markkey(sh, 648, 552, ["H01A", "H01B", "H01C", "H01D", "H02", "H03",
                                  "H04A", "H04B", "H05", "H06", "H07", "H08",
                                  "H09", "H10"], 183)
    # QA1: chained off the block above so the two can never collide
    ybb = V.bbs_extract(sh, 648, yk - 8, ["H01A", "H01B", "H01C", "H01D", "H02",
                                          "H03", "H04A", "H04B", "H05", "H06", "H10"])
    sh.panel(648, ybb - 6, 183, "HEADHOUSE LOAD PATH", [
        "HW1 south  runs in X, 4000, over the box south",
        "           perimeter wall - DIRECT",
        "HW2 north  runs in X, 4000, over the box north",
        "           perimeter wall - DIRECT",
        "HW3 west   runs in Y, 5000, over BAY 6, MID-SLAB.",
        "           *** NO WALL BELOW *** - a line load on",
        "           the pressure slab, 26 % (two-way) /",
        "           41 % (one-way bound).  Band S16 - R-304.",
        "HW4 east   runs in Y, 5000, over wall W7.",
        "           M1 MADE THESE ALIGN EXACTLY.",
        "",
        "THE HEADHOUSE HAS NO FOUNDATION OF ITS OWN.",
        "It bears entirely on the box roof and walls.",
    ], TXT["small"], 3.05)
    sh.titleblock(scale="1:40", sheet_of="23 OF 30")
    return sh.save(os.path.join(OUT, "R-701_Headhouse_Reinforcement.dxf"))


def r702():
    sh = Sheet("R-702", "ENTRANCE REINFORCEMENT",
               "COVERED ENTRY STAIRWELL · PLATFORM · HEADWALL · STEPPED RAFT",
               flags=["C16 OPEN", "NOT BLAST RATED"])
    sh.sheet_header()
    sc = 60
    Pm = vw(sc, 60, 400)
    A = P.ASW
    sh.rect(*Pm(A["x0"], A["y0"]), *Pm(A["x1"], A["y1"]), "S-CONCRETE")
    sh.rect(*Pm(A["ix0"], A["iy0"]), *Pm(A["ix1"], A["iy1"]), "S-CONCRETE")
    sh.concrete_hatch([Pm(A["x0"], A["y0"]), Pm(A["x1"], A["y0"]),
                       Pm(A["x1"], A["y1"]), Pm(A["x0"], A["y1"])],
                      holes=[[Pm(A["ix0"], A["iy0"]), Pm(A["ix1"], A["iy0"]),
                              Pm(A["ix1"], A["iy1"]), Pm(A["ix0"], A["iy1"])]])
    sh.rect(*Pm(9500, A["iy0"]), *Pm(11000, A["iy1"]), "S-CONCRETE-THIN")
    sh.text("TOP LANDING 0.000", Pm(10250, 6750), TXT["small"], "S-TEXT", "CENTER")
    for i in range(12):
        x = 11000 + i * 300
        sh.line(Pm(x, A["iy0"]), Pm(x, A["iy1"]), "S-CONCRETE-THIN")
    sh.text("FLIGHT 12R @ 166.6667 / 300", Pm(12650, 6750), TXT["small"], "S-TEXT", "CENTER")
    sh.rect(*Pm(14300, A["iy0"]), *Pm(15800, A["iy1"]), "S-CONCRETE-THIN")
    sh.text("PLATFORM (-)2.000", Pm(15050, 6750), TXT["small"], "S-TEXT", "CENTER")
    for x in range(9600, 15800, 200):
        sh.line(Pm(x, A["iy0"] + 60), Pm(x, A["iy1"] - 60), "S-REBAR-MAIN")
    # headhouse beyond
    sh.dline(Pm(P.HH["x0"], A["y0"]), Pm(P.HH["x0"], A["y0"] - 400), "S-HIDDEN")
    sh.rect(*Pm(P.HH["x0"], 200), *Pm(P.HH["x1"], 6000), "S-REFERENCE")
    sh.text("HEADHOUSE", Pm(16000, 3000), TXT["small"], "S-REFERENCE", "CENTER")
    # movement joint
    sh.line(Pm(16050, A["y0"] - 200), Pm(16050, A["y1"] + 200), "S-BLAST")
    sh.text("MOVEMENT JOINT AT THE HEADHOUSE - THE ONLY ONE ON THE PROJECT",
            Pm(11500, 8100), TXT["small"], "S-BLAST")
    sh.line(Pm(16050, 8050), Pm(16050, A["y1"] + 250), "S-BLAST")
    sh.dim_h(Pm(A["x0"], A["y0"]), Pm(A["x1"], A["y0"]), Pm(0, A["y0"] - 900)[1], sc)
    sh.dim_h(Pm(11000, A["y0"]), Pm(14300, A["y0"]), Pm(0, A["y0"] - 400)[1], sc)
    sh.dim_v(Pm(A["x0"], A["y0"]), Pm(A["x0"], A["y1"]), Pm(A["x0"] - 700, 0)[0], sc)
    sh.north((560, 460))
    V.balloon(sh, (140, 462), "E01", Pm(12500, 6750))
    V.balloon(sh, (74, 386), "E04A", Pm(9800, 5850))
    V.balloon(sh, (250, 462), "E07", Pm(15050, 6400))
    sh.view_title((30, 552), "V1", "COVERED ENTRY STAIRWELL - PLAN", "SCALE 1:60")
    sh.text("EXTERNAL 9250 - 16050 x 5750 - 7750  ·  INTERNAL 9500 - 15800 x 6000 - 7500  ·  "
            "WALLS 250  ·  POST-M1 (+200)  [CONFIRMED]", (30, 358), TXT["small"], "S-TEXT")

    # V2 headwall elevation
    sc2 = 30
    Pm2 = vw(sc2, 60, 200)
    sh.rect(*Pm2(0, 0), *Pm2(2000, 2900), "S-CONCRETE")
    sh.rect(*Pm2(500, 0), *Pm2(1500, 2100), "S-CONCRETE")
    sh.concrete_hatch([Pm2(0, 0), Pm2(2000, 0), Pm2(2000, 2900), Pm2(0, 2900)],
                      holes=[[Pm2(500, 0), Pm2(1500, 0), Pm2(1500, 2100), Pm2(500, 2100)]])
    sh.rect(*Pm2(300, 2100), *Pm2(1700, 2450), "S-REBAR-SEC")
    for x in range(100, 2000, 200):
        if not (500 < x < 1500):
            sh.line(Pm2(x, 60), Pm2(x, 2840), "S-REBAR-MAIN")
    for y in range(2500, 2900, 200):
        sh.line(Pm2(60, y), Pm2(1940, y), "S-REBAR-MAIN")
    sh.dim_h(Pm2(500, 0), Pm2(1500, 0), Pm2(0, -400)[1], sc2)
    sh.dim_v(Pm2(500, 0), Pm2(500, 2100), Pm2(-400, 0)[0], sc2)
    V.balloon(sh, (94, 288), "E08A", Pm2(300, 1400))
    V.balloon(sh, (128, 286), "E10", Pm2(1000, 2270))
    sh.view_title((30, 316), "V2", "HEADWALL ELEVATION AND ENTRY DOOR 1000 x 2100",
                  "SCALE 1:30")

    # V3 stepped raft / movement joint
    sc3 = 20
    Pm3 = vw(sc3, 200, 220)
    sh.rect(*Pm3(0, 0), *Pm3(1600, 300), "S-CONCRETE")
    sh.rect(*Pm3(1700, 0), *Pm3(3200, 900), "S-CONCRETE")
    sh.concrete_hatch([Pm3(0, 0), Pm3(1600, 0), Pm3(1600, 300), Pm3(0, 300)])
    sh.concrete_hatch([Pm3(1700, 0), Pm3(3200, 0), Pm3(3200, 900), Pm3(1700, 900)])
    sh.line(Pm3(1650, -200), Pm3(1650, 1100), "S-BLAST")
    sh.text("MOVEMENT JOINT", Pm3(1200, 1250), TXT["small"], "S-BLAST")
    sh.bar_run(Pm3(100, 56), Pm3(1500, 56), 200, sc3, "S-REBAR-MAIN", 0.7)
    sh.bar_run(Pm3(100, 244), Pm3(1500, 244), 200, sc3, "S-REBAR-MAIN", 0.7)
    sh.bar_run(Pm3(1800, 56), Pm3(3100, 56), 150, sc3, "S-REBAR-MAIN", 0.7)
    sh.text("STAIRWELL RAFT 300 ON COMPACTED FILL", Pm3(0, -700), TXT["small"], "S-TEXT")
    sh.text("HEADHOUSE / BOX - INDEPENDENT", Pm3(1750, -700), TXT["small"], "S-TEXT")
    sh.dim_v(Pm3(0, 0), Pm3(0, 300), Pm3(-400, 0)[0], sc3)
    V.balloon(sh, (216, 208), "E09A", Pm3(700, 56))
    sh.view_title((190, 316), "V3", "STEPPED RAFT AND MOVEMENT JOINT", "SCALE 1:20")

    y = sh.panel(370, 552, 268, "*** C16 - OPEN, NOT RESOLVED ***", [
        "THE ROOF / PLATFORM JUNCTION IS A GENUINE CONFLICT INSIDE THE PROJECT",
        "RECORD AND IS NOT CLOSED BY THIS PACKAGE.",
        "",
        "Master A.4.7 reads:  'over the platform it becomes the 500 headhouse roof'",
        "Master B.6 designs, A.7.6 loads and F.2 registers:  a 250 stairwell roof",
        "The headhouse footprint (Y 200 - 6000) DOES NOT OVERLAP the platform",
        "(Y 6000 - 7500), so the two statements cannot both be describing the same",
        "piece of concrete.",
        "",
        "THIS PACKAGE DETAILS 250, on the authority of master rule M.2 (Parts A, B",
        "and L are primary) and because the STAAD model is built at 250.",
        "THE A.4.7 CLAUSE IS NOT EDITED.  A USER RULING IS REQUIRED.",
        "",
        "AFFECTED DRAWINGS, ALL FLAGGED:  R-702  ·  R-703  ·  R-803  ·  R-804",
        "AND R-603.",
    ], TXT["small"], 3.05)
    V.loading_panel(sh, 370, y - 6, 268, [
        "STATUS: OUTSIDE THE PROTECTIVE BOUNDARY.  NOT BLAST RATED.",
        "DECLARED EXPENDABLE - expected to be LOST in the design event.",
        "Designed to IS 456 with NORMAL partial factors.",
        "",
        "THIS IS A DELIBERATE DESIGN DECISION, NOT AN OVERSIGHT.  The protective",
        "boundary is Blast Doors 1 and 2 at (-)6.100 together with walls W6/W7,",
        "the perimeter walls, the mat and the pressure slab.  EVERYTHING ABOVE THE",
        "BLAST DOORS IS OUTSIDE THE BOUNDARY.",
        "",
        "THE ONE MOVEMENT JOINT ON THE PROJECT is where the stairwell raft meets",
        "the headhouse.  There is NO movement joint anywhere inside the protective",
        "envelope, because a movement joint is a guaranteed blast, gas and EMP",
        "discontinuity.",
        "",
        "ROOF IMPOSED LOAD 20 kPa is taken DELIBERATELY, for a stray vehicle on",
        "the berm.  Conflicts C12, C13 and C14 (model imposed load, waterproofing",
        "and fill density) were resolved against master A.7.6 before this package.",
    ], TXT["small"], 3.05, heading="ENTRY STAIRWELL - STATUS")
    V.bbs_extract(sh, 648, 552, ["E04A", "E04B", "E05A", "E05B", "E06", "E07",
                                 "E08A", "E08B", "E09A", "E09B", "E10", "E11", "E12"])
    sh.titleblock(scale="1:60, 1:30, 1:20", sheet_of="24 OF 30")
    return sh.save(os.path.join(OUTE, "R-702_Entrance_Reinforcement.dxf"))


def r703():
    sh = Sheet("R-703", "BLAST-DOOR AND OPENING DETAILS",
               "BLAST DOORS 1 AND 2 · SECURITY DOOR · FRAME INTERFACE",
               flags=["VENDOR DATA NOT AVAILABLE", "C16 OPEN"])
    sh.sheet_header()
    # V1 blast door head detail
    sc = 10
    Pm = vw(sc, 90, 330)
    sh.rect(*Pm(0, 0), *Pm(400, 1600), "S-CONCRETE")
    sh.concrete_hatch([Pm(0, 0), Pm(400, 0), Pm(400, 1600), Pm(0, 1600)])
    sh.rect(*Pm(0, -900), *Pm(400, 0), "S-REFERENCE")
    for xo in (60, 340):
        for yy in range(80, 1600, 150):
            sh.bar_dot(Pm(xo, yy), 1.0, "S-REBAR-MAIN")
    for yy in range(150, 1600, 150):
        sh.rect(*Pm(50, yy - 55), *Pm(350, yy + 55), "S-REBAR-STIRRUP")
        sh.line(Pm(200, yy - 55), Pm(200, yy + 55), "S-REBAR-STIRRUP")
    sh.line(Pm(0, -900), Pm(0, 0), "S-STEELWORK")
    sh.line(Pm(-80, -900), Pm(-80, 0), "S-STEELWORK")
    sh.line(Pm(-80, 0), Pm(0, 0), "S-STEELWORK")
    for yy in (-750, -450, -150):
        sh.line(Pm(-80, yy), Pm(260, yy), "S-STEELWORK")
        sh.text("WELD", Pm(280, yy - 30), TXT["small"], "S-STEELWORK")
    sh.dim_h(Pm(0, 0), Pm(400, 0), Pm(0, 1900)[1], sc)
    sh.dim_v(Pm(400, 0), Pm(400, 1100), Pm(700, 0)[0], sc)
    sh.text("HEADER 400 x 1100", Pm(760, 500), TXT["small"], "S-TEXT")
    sh.text("OPENING 2100 HIGH BELOW", Pm(560, -1200), TXT["small"], "S-TEXT")
    V.balloon(sh, (74, 452), "B01", Pm(200, 1450))
    V.balloon(sh, (146, 420), "B03", Pm(300, 1000))
    sh.view_title((30, 552), "V1", "BLAST-DOOR HEAD AND CAST-IN FRAME", "SCALE 1:10")

    # V2 security door jamb in HW2
    Pm2 = vw(sc, 260, 330)
    sh.rect(*Pm2(0, 0), *Pm2(400, 1400), "S-CONCRETE")
    sh.concrete_hatch([Pm2(0, 0), Pm2(400, 0), Pm2(400, 1400), Pm2(0, 1400)])
    for xo in (58, 342):
        for yy in (70, 200):
            sh.bar_dot(Pm2(xo, yy), 1.2, "S-REBAR-SEC")
        for yy in range(400, 1400, 150):
            sh.bar_dot(Pm2(xo, yy), 1.0, "S-REBAR-MAIN")
    for yy in (100, 250):
        sh.rect(*Pm2(50, yy - 60), *Pm2(350, yy + 60), "S-REBAR-STIRRUP")
    sh.dim_h(Pm2(0, 0), Pm2(400, 0), Pm2(0, 1700)[1], sc)
    V.balloon(sh, (246, 348), "H07", Pm2(58, 140))
    sh.view_title((230, 552), "V2", "SECURITY DOOR JAMB IN HW2", "SCALE 1:10")
    sh.text("2-T20 EACH JAMB EACH FACE = 628 mm2", (230, 300), TXT["small"], "S-TEXT")
    sh.text("vs 603 REQUIRED.  NOT BLAST RATED.", (230, 295), TXT["small"], "S-TEXT")

    # V3 door head edge band
    Pm3 = vw(sc, 400, 330)
    sh.rect(*Pm3(0, 0), *Pm3(400, 300), "S-CONCRETE")
    sh.rect(*Pm3(0, 300), *Pm3(400, 800), "S-CONCRETE")
    sh.concrete_hatch([Pm3(0, 0), Pm3(400, 0), Pm3(400, 800), Pm3(0, 800)])
    sh.dline(Pm3(0, 300), Pm3(400, 300), "S-HIDDEN")
    for xo in (66, 155, 245, 334):
        sh.bar_dot(Pm3(xo, 742), 1.2, "S-REBAR-SEC")
        sh.bar_dot(Pm3(xo, 58), 1.2, "S-REBAR-SEC")
    sh.rect(*Pm3(40, 40), *Pm3(360, 760), "S-REBAR-STIRRUP")
    sh.line(Pm3(155, 40), Pm3(155, 760), "S-REBAR-STIRRUP")
    sh.line(Pm3(245, 40), Pm3(245, 760), "S-REBAR-STIRRUP")
    sh.dim_v(Pm3(400, 0), Pm3(400, 300), Pm3(700, 0)[0], sc)
    sh.dim_v(Pm3(400, 300), Pm3(400, 800), Pm3(700, 0)[0], sc)
    sh.text("WALL 300", Pm3(760, 120), TXT["small"], "S-TEXT")
    sh.text("ROOF 500", Pm3(760, 520), TXT["small"], "S-TEXT")
    V.balloon(sh, (386, 424), "H08", Pm3(155, 742))
    V.balloon(sh, (466, 396), "H09", Pm3(300, 400))
    sh.view_title((370, 552), "V3", "HEADHOUSE DOOR-HEAD EDGE BAND 400 x 800",
                  "SCALE 1:10")
    sh.text("ONLY 300 mm OF WALL ABOVE THE DOOR -", (370, 300), TXT["small"], "S-BLAST")
    sh.text("THE 300 WALL AND THE 500 ROOF ACT TOGETHER.", (370, 295),
            TXT["small"], "S-BLAST")

    y = V.loading_panel(sh, 30, 276, 300, [
        "WHAT IS DESIGNED HERE",
        "  ·  The RC opening reinforcement: jambs, header, edge band, reveal U-bars.",
        "  ·  The requirement that the cast-in frame be ANCHORED INTO AND WELDED TO",
        "     THE CAGE, for EMP continuity of the rebar shield.",
        "",
        "WHAT IS NOT DESIGNED HERE, AND IS NOT INVENTED",
        "  ·  THE DOOR LEAF.  Proprietary, >= 7 bar, rebound-rated, gas-tight.",
        "  ·  THE FRAME SECTION, ITS ANCHOR SPACING AND ITS EMBEDMENT.",
        "  ·  THE REBOUND RATING AND THE DYNAMIC REACTION ON THE FRAME.",
        "  ALL OF THESE ARE A VENDOR SUBMITTAL AND ARE [NOT AVAILABLE] IN THE",
        "  PROJECT RECORD.  NO PROPRIETARY BLAST-DOOR REQUIREMENT IS FABRICATED.",
        "",
        "THE INTERFACE THAT IS STRUCTURALLY REQUIRED",
        "  1  The frame shall be cast in, not drilled and fixed.",
        "  2  Frame anchors shall be WELDED to the wall cage, not merely embedded,",
        "     so that the reinforcement shield is electrically continuous",
        "     (MIL-STD-188-125-1 is the project's EMP reference).",
        "  3  Jamb bars W13 (4-T20 each jamb each face) are anchored Ld = 800",
        "     beyond the opening in BOTH directions and are NOT interrupted by the",
        "     frame or its anchors.",
        "  4  No frame fixing may displace a jamb bar.  Any clash is an RFI.",
        "",
        "THE SAME PRINCIPLE APPLIES TO THE SECURITY DOOR IN HW2: it is not blast",
        "rated, but its frame is still cast in and welded, because the EMP shield",
        "does not stop at the protective boundary.",
    ], TXT["small"], 3.05, heading="BLAST-DOOR INTERFACE - THE LIMIT OF THIS PACKAGE")
    yk = V.markkey(sh, 340, 276, ["W13", "W14", "W15", "B01", "B02", "B03", "H07",
                                  "H08", "H09"], 298)
    # QA1: chained off the block above so the two can never collide
    V.bbs_extract(sh, 340, yk - 8, ["W13", "W14", "W15", "B01", "B02", "B03",
                                    "H07", "H08", "H09"])
    V.materials_panel(sh, 648, 552, 183)
    sh.titleblock(scale="1:10", sheet_of="25 OF 30")
    return sh.save(os.path.join(OUTE, "R-703_Blast_Door_Opening_Details.dxf"))


def build():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(OUTE, exist_ok=True)
    return [r701(), r702(), r703()]


if __name__ == "__main__":
    for f in build():
        print("written", f)
