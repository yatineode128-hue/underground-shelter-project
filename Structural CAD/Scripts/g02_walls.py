"""g02_walls.py  --  R-201 to R-205, underground walls."""
import os, math
import sc_proj as P
import sc_dxflib as D
import sc_views as V
import rebar_data as R
from sc_dxflib import Sheet, vw, TXT

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "DXF", "Walls"))

PERIM_BASIS = [
    "GOVERNING COMBINATION   103 BLAST",
    "Blast 383 kPa (Ka = 1.0, saturated) vs static earth + water 83.2 kPa at",
    "the base  ->  BLAST GOVERNS 4.6 : 1",
    "",
    "MECHANISM   fixed-fixed one-way vertical strip, Ln = 3200",
    "  Mp = w Ln2 / 16 = 383 x 3.200^2 / 16       =  245.1 kNm/m",
    "  d  = 600 - 75 - 8                          =  517 mm",
    "  Mu,lim = 0.133 x 43.75 x 1000 x 517^2      =  1556 kNm/m  SINGLY REINFORCED",
    "  Ast,req (fck,dyn 43.75 / fy,dyn 625)       =  894 mm2/m",
    "",
    "MINIMUM STEEL",
    "  IS 456 Cl. 32.5(a) vertical  0.0012 x 600  =  720 mm2/m",
    "  IS 456 Cl. 32.5(b) horizontal 0.0020 x 600 =  1200 mm2/m   GOVERNS",
    "  IS 3370 Pt 2 surface zone 0.35 % x 250     =  875 mm2/m/face",
    "  IS 456 Cl. 32.5(c) two curtains required (t > 200)   PROVIDED",
    "",
    "PROVIDED  T16 @ 150 EF EW = 1340 mm2/m/face",
    "  Mu = 362.8 kNm/m   ->  UTILISATION 68 %   ·  xu/d = 0.089 << 0.46",
    "",
    "SHEAR   V at d = 383 (1.600 - 0.517)         =  414.8 kN/m",
    "  tau_v 0.802 | tau_c 0.375 (pt 0.259 %, STATIC M35 - IS 4991 Cl. 10.3.1.1)",
    "  tau_c,max 3.70 OK   Vus 220.8   Asv/sv 0.982  ->  T12 2-leg at 230",
    "  IS 456 Cl. 26.5.1.5 limit min(0.75d 388, 300) = 300",
    "  PROVIDED  T12 CLOSED LINKS @ 200  (Asv/sv 1.131)",
    "",
    "AXIAL   N = 448.15 x 2.50 + 3.2 x 0.6 x 25   =  1168 kN/m",
    "  f = 1.95 N/mm2 = 11 % of 0.4 fck,dyn  ->  P-M NOT CRITICAL",
    "CRACK   IS 3370 Pt 2, 0.2 mm limit; surface steel 875 < 1340 provided  OK",
    "",
    "MANUAL CALCULATION - NOT DIRECT STAAD OUTPUT.",
]

W67_BASIS = [
    "GOVERNING COMBINATION  103 BLAST via LOAD 11",
    "`BL3 BLAST IN THE STAIR SHAFT ON W6 AND W7 383 KN/M2`",
    "  - the load case that MODIFICATION M1 EXISTS TO CARRY.",
    "",
    "FINDING F1   The stair shaft is open to atmosphere through the",
    "2800 x 3160 roof void, the headhouse and the entry stairwell.",
    "  Fill time V/(A c) = 105 /(3.3 x 340) = 0.094 s  vs  td 0.13-1.33 s",
    "  ->  THE SHAFT EQUALISES TO FULL p_so.",
    "W6 / W7 sit in the SAME PLANE as the 7-bar blast doors, separating a",
    "pressurised shaft from Bay 6 / Bay 8 at ambient.",
    "",
    "WHY 200 mm WAS IMPOSSIBLE - NOT A DETAILING PROBLEM",
    "  d = 200 - 40 - 6 = 154 ;  Mu,lim = 138.0 kNm/m",
    "  Demand Mp = 383 x 3.200^2/16 = 245.1 kNm/m",
    "  138 < 245  ->  NO STEEL RATIO MAKES IT WORK.",
    "  Two-way action was checked BEFORE rejection: 3200 x 3800 panel,",
    "  fixed 3 edges, yield line approx 0.7 x one-way = 172 - still above 138.",
    "",
    "DESIGN OF THE 400 WALL",
    "  d = 400 - 50 - 8 = 342 ;  Mu,lim 680.6 kNm/m  OK",
    "  Ast,req = 1400 mm2/m",
    "  PROVIDED T20 @ 150 EF EW = 2094  ->  Mu 355.3, UTIL 69 %, x/d 0.211",
    "SHEAR  V at d = 481.8 kN/m ; tau_v 1.409 | tau_c 0.540 | tau_c,max 3.70 OK",
    "  Vus 297.2 ; Asv/sv 1.998  ->  T12 4-leg at 226 ; Cl. 26.5.1.5 limit 257",
    "  PROVIDED  T12 4-LEGGED LINKS @ 200",
    "",
    "MANUAL CALCULATION - NOT DIRECT STAAD OUTPUT.",
]


def _wall_section(sh, Pm, sc, t, h, cover_out, cover_in, phi, sp, phi_l, sp_l,
                  legs=2, haunch=500):
    """Vertical section through a wall: thickness horizontal, height vertical."""
    sh.rect(*Pm(0, 0), *Pm(t, h), "S-CONCRETE")
    sh.concrete_hatch([Pm(0, 0), Pm(t, 0), Pm(t, h), Pm(0, h)])
    a = cover_out + phi / 2
    b = t - cover_in - phi / 2
    sh.line(Pm(a, 40), Pm(a, h - 40), "S-REBAR-MAIN")
    sh.line(Pm(b, 40), Pm(b, h - 40), "S-REBAR-MAIN")
    sh.bar_run(Pm(a, sp / 2), Pm(a, h - sp / 2), sp, sc, "S-REBAR-MAIN", 0.6)
    sh.bar_run(Pm(b, sp / 2), Pm(b, h - sp / 2), sp, sc, "S-REBAR-MAIN", 0.6)
    yy = sp_l / 2
    while yy < h:
        sh.rect(*Pm(cover_out, yy - sp_l * 0.22), *Pm(t - cover_in, yy + sp_l * 0.22),
                "S-REBAR-STIRRUP")
        if legs == 4:
            sh.line(Pm(t / 2, yy - sp_l * 0.22), Pm(t / 2, yy + sp_l * 0.22),
                    "S-REBAR-STIRRUP")
        yy += sp_l


def r201():
    sh = Sheet("R-201", "EXTERNAL WALL REINFORCEMENT",
               "PERIMETER WALLS W1-W4, 600 THK · T16 @ 150 EF EW · T12 CLOSED LINKS @ 200",
               flags=["A2 GWT ASSUMED"])
    sh.sheet_header()
    # V1 typical wall section, 1:20
    sc = 20
    Pm = vw(sc, 70, 356)
    _wall_section(sh, Pm, sc, 600, 3200, 50, 40, 16, 150, 12, 200, legs=2)
    # roof and mat stubs
    sh.rect(*Pm(-200, 3200), *Pm(800, 3600), "S-CONCRETE-THIN")
    sh.rect(*Pm(-200, -400), *Pm(800, 0), "S-CONCRETE-THIN")
    sh.pline([Pm(600, 0), Pm(1100, 0), Pm(600, 500)], "S-CONCRETE")
    sh.pline([Pm(600, 3200), Pm(1100, 3200), Pm(600, 2700)], "S-CONCRETE")
    for i in range(4):
        o = i * 150
        sh.line(Pm(600 + o, 60), Pm(660, 60 + o), "S-REBAR-SEC")
        sh.line(Pm(600 + o, 3140), Pm(660, 3140 - o), "S-REBAR-SEC")
    sh.dim_h(Pm(0, 0), Pm(600, 0), Pm(0, -900)[1], sc)
    sh.dim_v(Pm(0, 0), Pm(0, 3200), Pm(-700, 0)[0], sc)
    sh.level(Pm(-150, 3200), "(-)2.900")
    sh.level(Pm(-150, 0), "(-)6.100")
    sh.text("EARTH FACE", Pm(-120, 1600), TXT["small"], "S-TEXT", "CENTER", 90)
    sh.text("INTERNAL FACE", Pm(720, 1600), TXT["small"], "S-TEXT", "CENTER", 90)
    V.balloon(sh, (40, 470), "W01", Pm(58, 2400))
    V.balloon(sh, (120, 500), "W02", Pm(542, 2600))
    V.balloon(sh, (40, 410), "W05", Pm(300, 1000))
    V.balloon(sh, (128, 460), "W06", Pm(820, 2900))
    sh.view_title((70, 552), "V1", "TYPICAL PERIMETER WALL SECTION W1 - W4", "SCALE 1:20")
    sh.text("COVER  50 EARTH FACE  ·  40 INTERNAL FACE  ·  75 AT THE MAT",
            (30, 316), TXT["small"], "S-TEXT")
    sh.text("BOTH CURTAINS AT 150 BOTH WAYS - EMP MAXIMUM, NOT A STRENGTH SPACING",
            (30, 311), TXT["small"], "S-BLAST")

    # V2 horizontal section through the wall (plan cut), 1:20
    Pm2 = vw(sc, 190, 380)
    sh.rect(*Pm2(0, 0), *Pm2(600, 3000), "S-CONCRETE")
    sh.concrete_hatch([Pm2(0, 0), Pm2(600, 0), Pm2(600, 3000), Pm2(0, 3000)])
    sh.bar_run(Pm2(58, 75), Pm2(58, 2925), 150, sc, "S-REBAR-MAIN", 0.6)
    sh.bar_run(Pm2(542, 75), Pm2(542, 2925), 150, sc, "S-REBAR-MAIN", 0.6)
    sh.line(Pm2(83, 20), Pm2(83, 2980), "S-REBAR-MAIN")
    sh.line(Pm2(517, 20), Pm2(517, 2980), "S-REBAR-MAIN")
    for yy in range(100, 3000, 200):
        sh.rect(*Pm2(50, yy - 44), *Pm2(550, yy + 44), "S-REBAR-STIRRUP")
    sh.dim_h(Pm2(0, 0), Pm2(600, 0), Pm2(0, -400)[1], sc)
    sh.dim_v(Pm2(600, 900), Pm2(600, 1050), Pm2(760, 0)[0], sc)
    sh.text("150", Pm2(820, 975), TXT["small"], "S-TEXT")
    sh.view_title((190, 552), "V2", "HORIZONTAL SECTION - PLAN CUT ON THE WALL", "SCALE 1:20")

    y = V.loading_panel(sh, 300, 552, 200, PERIM_BASIS, TXT["small"], 3.05,
                        heading="PERIMETER WALLS - DESIGN BASIS")
    V.markkey(sh, 300, y - 6, ["W01", "W02", "W03", "W04", "W05", "W06"], 200)
    sh.panel(510, 552, 130, "WHY 600 mm - STATED HONESTLY", [
        "The wall is NOT strength-governed.",
        "It is 68 % utilised.  600 is set by:",
        "",
        "(i)   75 mm cover",
        "(ii)  CONGESTION - two curtains,",
        "      closed links, waterstops and",
        "      cast-in frames",
        "(iii) IS 3370 crack control under",
        "      sustained hydrostatic load",
        "(iv)  the EMP double curtain at 150",
        "(v)   the 1168 kN/m axial path",
        "",
        "Presenting 600 as a strength result",
        "would be false.  It is a detailing,",
        "durability and hardening thickness.",
    ], TXT["small"], 3.05)
    V.bbs_extract(sh, 510, 490, ["W01", "W02", "W03", "W04", "W05", "W06"])
    V.materials_panel(sh, 648, 552, 183)
    sh.panel(30, 296, 470, "PERIMETER WALL DETAILING", [
        "1  VERTICAL BARS W01 / W02 run continuously from the mat starters F07 to the",
        "   pressure slab, lapped 800 (50 phi) STAGGERED above a 150 kicker, and are",
        "   carried 825 into the 900 slab - more than the 640 Ld required.",
        "2  HORIZONTAL BARS lie OUTSIDE the verticals on the earth face.  W03 (long walls",
        "   W1 / W2) are full-length bars in 2 pieces of 11 350 with staggered 800 laps;",
        "   W04 (end walls W3 / W4) are U-bars whose 640 legs turn into W1 and W2 at",
        "   every corner, so the horizontal steel is continuous around the box.",
        "3  T12 CLOSED LINKS @ 200 BOTH WAYS tie the two curtains.  They are a SHEAR",
        "   requirement (Vus 220.8 kN/m), not a spacer.",
        "4  500 x 500 HAUNCH WITH T20 @ 150 DIAGONALS at the wall/mat and wall/roof",
        "   junctions - R-103 D2 and R-304.",
        "5  NO MOVEMENT JOINT.  Construction joints only, with full bar continuity, two",
        "   waterstops and a welded EMP strap - R-804.",
    ], TXT["small"], 3.05)
    sh.titleblock(scale="1:20", sheet_of="8 OF 30")
    return sh.save(os.path.join(OUT, "R-201_External_Wall_Reinforcement.dxf"))


def r202():
    sh = Sheet("R-202", "INTERNAL WALL REINFORCEMENT",
               "W6 / W7 400 THK (MOD M1) · W5 200 THK · W8 PARTITIONS 110",
               flags=["M1 NO STAAD RESULT"])
    sh.sheet_header()
    sc = 20
    Pm = vw(sc, 70, 356)
    _wall_section(sh, Pm, sc, 400, 3200, 50, 40, 20, 150, 12, 200, legs=4)
    sh.rect(*Pm(-300, 3200), *Pm(700, 3600), "S-CONCRETE-THIN")
    sh.rect(*Pm(-300, -400), *Pm(700, 0), "S-CONCRETE-THIN")
    sh.dim_h(Pm(0, 0), Pm(400, 0), Pm(0, -900)[1], sc)
    sh.dim_v(Pm(0, 0), Pm(0, 3200), Pm(-800, 0)[0], sc)
    sh.text("SHAFT FACE (BAY 7)", Pm(-180, 1600), TXT["small"], "S-BLAST", "CENTER", 90)
    sh.text("BAY 6 / BAY 8", Pm(560, 1600), TXT["small"], "S-TEXT", "CENTER", 90)
    sh.pline([Pm(-1400, 1600), Pm(-300, 1600)], "S-BLAST")
    sh.pline([Pm(-500, 1750), Pm(-300, 1600), Pm(-500, 1450)], "S-BLAST")
    sh.text("383 kPa", Pm(-1350, 1700), TXT["small"], "S-BLAST")
    V.balloon(sh, (40, 470), "W07", Pm(58, 2400))
    V.balloon(sh, (104, 500), "W08", Pm(342, 2600))
    V.balloon(sh, (40, 410), "W11", Pm(200, 1000))
    sh.view_title((70, 552), "V1", "WALLS W6 / W7 - 400 THK (MODIFICATION M1)", "SCALE 1:20")
    sh.text("COVER 50 SHAFT FACE / 40 ROOM FACE.  SYMMETRICAL - THE WALL IS",
            (24, 316), TXT["small"], "S-TEXT")
    sh.text("DETAILED THE SAME BOTH FACES EVEN THOUGH IT IS LOADED FROM THE",
            (24, 311), TXT["small"], "S-TEXT")
    sh.text("SHAFT SIDE ONLY.", (24, 306), TXT["small"], "S-TEXT")

    # V2 W5 200
    Pm2 = vw(sc, 175, 356)
    _wall_section(sh, Pm2, sc, 200, 3200, 40, 40, 12, 150, 12, 400, legs=2)
    sh.dim_h(Pm2(0, 0), Pm2(200, 0), Pm2(0, -900)[1], sc)
    V.balloon(sh, (166, 470), "W16", Pm2(46, 2400))
    sh.view_title((175, 552), "V2", "WALL W5 - 200 THK", "SCALE 1:20")
    sh.text("NO PRESSURE DIFFERENTIAL.  FIRE AND", (162, 316), TXT["small"], "S-TEXT")
    sh.text("GAS-TIGHT SEPARATION ONLY.  MINIMUM", (162, 311), TXT["small"], "S-TEXT")
    sh.text("STEEL GOVERNS - T12 @ 150 EF EW.", (162, 306), TXT["small"], "S-TEXT")

    # V3 W8 partition elevation
    sc3 = 50
    Pm3 = vw(sc3, 240, 400)
    sh.rect(*Pm3(0, 0), *Pm3(5000, 3200), "S-CONCRETE")
    sh.rect(*Pm3(1900, 0), *Pm3(2800, 2100), "S-CONCRETE")
    sh.concrete_hatch([Pm3(0, 0), Pm3(5000, 0), Pm3(5000, 3200), Pm3(0, 3200)],
                      holes=[[Pm3(1900, 0), Pm3(2800, 0), Pm3(2800, 2100), Pm3(1900, 2100)]])
    for x in range(200, 5000, 200):
        if not (1900 < x < 2800):
            sh.line(Pm3(x, 60), Pm3(x, 3140), "S-REBAR-DIST")
    for yy in range(200, 3200, 200):
        sh.line(Pm3(60, yy), Pm3(1900, yy), "S-REBAR-DIST")
        sh.line(Pm3(2800, yy), Pm3(4940, yy), "S-REBAR-DIST")
    sh.dim_h(Pm3(1900, 0), Pm3(2800, 0), Pm3(0, -500)[1], sc3)
    sh.dim_h(Pm3(0, 0), Pm3(5000, 0), Pm3(0, -1100)[1], sc3)
    sh.dim_v(Pm3(0, 0), Pm3(0, 3200), Pm3(-600, 0)[0], sc3)
    sh.leader([Pm3(3500, 1600), (330, 490)], "W18  A252 FABRIC BOTH FACES")
    sh.view_title((240, 552), "V3", "W8 PARTITION ELEVATION - 110 THK, TYPICAL x4",
                  "SCALE 1:50")
    sh.text("NON-STRUCTURAL.  NO LOAD PATH IS ASSUMED THROUGH A PARTITION.",
            (240, 316), TXT["small"], "S-BLAST")
    sh.text("NO TRIMMING IS REQUIRED TO THE 900 DOOR GAPS.", (240, 311),
            TXT["small"], "S-TEXT")

    y = V.loading_panel(sh, 380, 552, 258, W67_BASIS, TXT["small"], 3.05,
                        heading="WALLS W6 / W7 - DESIGN BASIS AND FINDING F1")
    yk = V.markkey(sh, 380, y - 6, ["W07", "W08", "W09", "W10", "W11", "W12", "W16",
                                    "W17"], 258)
    sh.rect(380, yk - 13.0, 638, yk - 2.0, "S-TITLE")
    sh.circle((387, yk - 7.0), 2.6, "S-CALLOUT")
    sh.text("W18", (387, yk - 7.0), TXT["small"], "S-CALLOUT", "CENTER")
    sh.text("FABRIC  A252 BOTH FACES - W8 PARTITIONS 110, NON-STRUCTURAL",
            (392, yk - 7.6), TXT["small"], "S-NOTE")
    V.bbs_extract(sh, 380, 232, ["W07", "W08", "W09", "W10", "W11", "W12", "W16", "W17"])
    sh.panel(648, 552, 183, "MODIFICATION M1 - WHAT CHANGED AND WHY", [
        "M1 WAS APPROVED AND IMPLEMENTED ON 3 SEPTEMBER 2026.",
        "",
        "W6 and W7   200  ->  400 mm",
        "Box length  21 600  ->  22 000",
        "Stair shaft ->  15 200 - 18 000",
        "ESC 2       ->  X 19 900",
        "Headhouse and covered stairwell  +200",
        "NOTHING WEST OF X 14 800 MOVED.",
        "",
        "M1 EXISTS BECAUSE THE PROTECTIVE BOUNDARY WAS NOT",
        "CONTINUOUS.  W6 / W7 are in the same plane as the two",
        "7-bar blast doors, and at 200 mm they could not carry",
        "the 245.1 kNm/m the pressurised shaft imposes -",
        "Mu,lim at 200 is only 138.0 kNm/m.",
        "",
        "LENGTHENING THE BOX IS STRUCTURALLY FREE: the roof spans",
        "ONE-WAY across the 5000 width, so Mp depends only on that",
        "width.  WIDENING 5.0 -> 6.0 m would raise the roof moment",
        "44 %.  That single fact is what made M1 affordable.",
        "",
        "M1 is NOT a uniform shift.  W6 / W7 thicken about their",
        "own faces; the shaft moves +200; Bay 8 and the east end",
        "+400; headhouse and stairwell +200 as whole structures.",
    ], TXT["small"], 3.05)
    sh.titleblock(scale="1:20, 1:50", sheet_of="9 OF 30")
    return sh.save(os.path.join(OUT, "R-202_Internal_Wall_Reinforcement.dxf"))


def r203():
    sh = Sheet("R-203", "WALL ELEVATIONS",
               "W1 SOUTH PERIMETER · W6 / W7 · BAR ARRANGEMENT AND LAP STAGGER")
    sh.sheet_header()
    sc = 60
    Pm = vw(sc, 40, 400)
    # W1 elevation, 22000 long x 3200 high
    sh.rect(*Pm(0, 0), *Pm(22000, 3200), "S-CONCRETE")
    sh.rect(*Pm(-0, 3200), *Pm(22000, 4100), "S-CONCRETE-THIN")
    sh.rect(*Pm(0, -600), *Pm(22000, 0), "S-CONCRETE-THIN")
    for x in range(300, 22000, 600):
        sh.line(Pm(x, 60), Pm(x, 3140), "S-REBAR-MAIN")
    for yy in range(150, 3200, 300):
        sh.line(Pm(100, yy), Pm(21900, yy), "S-REBAR-MAIN")
    # lap stagger diagram
    for i, yy in enumerate(range(300, 3200, 600)):
        x0 = 5000 if i % 2 == 0 else 11000
        sh.line(Pm(x0, yy), Pm(x0 + 800, yy), "S-REBAR-SEC")
        sh.text("LAP 800", Pm(x0 + 60, yy + 90), TXT["small"], "S-REBAR-SEC")
    for mk, x0, x1, t in P.IW:
        sh.dline(Pm(x0, 0), Pm(x0, 3200), "S-HIDDEN")
        sh.dline(Pm(x1, 0), Pm(x1, 3200), "S-HIDDEN")
        sh.text(mk, Pm((x0 + x1) / 2, 3300), TXT["small"], "S-TEXT", "CENTER")
    sh.dim_h(Pm(0, 0), Pm(22000, 0), Pm(0, -1400)[1], sc)
    sh.dim_v(Pm(0, 0), Pm(0, 3200), Pm(-900, 0)[0], sc)
    sh.level(Pm(-600, 3200), "(-)2.900")
    sh.level(Pm(-600, 0), "(-)6.100")
    V.balloon(sh, (60, 480), "W01", Pm(2400, 2400))
    V.balloon(sh, (200, 480), "W03", Pm(11000, 2550))
    sh.view_title((40, 552), "V1", "WALL W1 (SOUTH PERIMETER) - INTERNAL ELEVATION",
                  "SCALE 1:60")
    sh.text("VERTICAL BARS W01 / W02 AT 150 · HORIZONTAL BARS W03 AT 150 · "
            "LAPS 800 (50 phi) STAGGERED SO THAT NOT MORE THAN 50 % ARE SPLICED "
            "AT ANY ONE SECTION", (40, 364), TXT["small"], "S-TEXT")

    # W6 elevation with blast door
    sc2 = 30
    Pm2 = vw(sc2, 40, 175)
    sh.rect(*Pm2(0, 0), *Pm2(5000, 3200), "S-CONCRETE")
    sh.rect(*Pm2(0, 0), *Pm2(1200, 2100), "S-CONCRETE")
    sh.concrete_hatch([Pm2(0, 0), Pm2(5000, 0), Pm2(5000, 3200), Pm2(0, 3200)],
                      holes=[[Pm2(0, 0), Pm2(1200, 0), Pm2(1200, 2100), Pm2(0, 2100)]])
    for x in range(1350, 5000, 150):
        sh.line(Pm2(x, 60), Pm2(x, 3140), "S-REBAR-MAIN")
    for x in range(150, 1200, 150):
        sh.line(Pm2(x, 2200), Pm2(x, 3140), "S-REBAR-MAIN")
    for yy in range(150, 3200, 150):
        sh.line(Pm2(1300, yy), Pm2(4940, yy), "S-REBAR-MAIN")
    # jamb group
    for o in (60, 130, 200, 270):
        sh.line(Pm2(1200 + o, -600), Pm2(1200 + o, 2900), "S-REBAR-SEC")
    # header
    sh.rect(*Pm2(0, 2100), *Pm2(1200, 3200), "S-REBAR-SEC")
    sh.dim_h(Pm2(0, 0), Pm2(1200, 0), Pm2(0, -500)[1], sc2)
    sh.dim_v(Pm2(0, 0), Pm2(0, 2100), Pm2(-500, 0)[0], sc2)
    sh.dim_h(Pm2(0, 0), Pm2(5000, 0), Pm2(0, -1100)[1], sc2)
    V.balloon(sh, (105, 232), "W13", Pm2(1330, 1200))
    V.balloon(sh, (80, 288), "B01", Pm2(600, 3060))
    sh.view_title((40, 316), "V2", "WALL W6 - ELEVATION ON THE SHAFT FACE, BLAST DOOR 1",
                  "SCALE 1:30")
    sh.text("BLAST DOOR 1  1200 x 2100, 7 BAR, AT Y 600 - 1800.  BLAST DOOR 2 IN W7 IS "
            "HANDED, OTHERWISE IDENTICAL.", (40, 128), TXT["small"], "S-TEXT")

    y = sh.panel(300, 552, 340, "LAP AND SPLICE POLICY - WHY 50 phi AND NOT 40 phi", [
        "IS 456 Cl. 26.2.5.1(c) gives lap = Ld or 30 phi, whichever is greater = 40 phi.",
        "IS 456 Cl. 26.2.5.1 requires the lap to be increased by x1.4 if MORE THAN 50 %",
        "of the bars are lapped at one section.",
        "",
        "THIS PACKAGE STAGGERS EVERY LAP so that not more than 50 % are spliced at any",
        "one section, AND specifies the lap at 50 phi - 25 % above requirement.  The",
        "x1.4 factor is therefore not triggered and there is margin on top.",
        "",
        "IS 4991 Cl. 10.3.1.1 PERMITS A 25 % INCREASE ON BOND FOR THE BLAST CASE, which",
        "would reduce Ld to 32 phi.  IT IS NOT TAKEN.  All detailing uses the static 40 phi.",
        "",
        "LAP LENGTHS   T12 600  ·  T16 800  ·  T20 1000  ·  T25 1250",
        "Ld TENSION    T12 480  ·  T16 640  ·  T20  800  ·  T25 1000",
    ], TXT["small"], 3.05)
    V.markkey(sh, 300, y - 6, ["W01", "W02", "W03", "W04", "W07", "W08", "W09",
                               "W10", "W13"], 340)
    V.bbs_extract(sh, 300, 300, ["W01", "W02", "W03", "W04", "W07", "W08", "W09", "W10"])
    V.materials_panel(sh, 648, 552, 183)
    sh.titleblock(scale="1:60, 1:30", sheet_of="10 OF 30")
    return sh.save(os.path.join(OUT, "R-203_Wall_Elevations.dxf"))


def r204():
    sh = Sheet("R-204", "WALL SECTIONS",
               "PERIMETER 600 · W6 / W7 400 · W5 200 · LINK ARRANGEMENTS")
    sh.sheet_header()
    sc = 10
    # V1 perimeter wall enlarged section 1:10
    Pm = vw(sc, 50, 300)
    sh.rect(*Pm(0, 0), *Pm(600, 900), "S-CONCRETE")
    sh.concrete_hatch([Pm(0, 0), Pm(600, 0), Pm(600, 900), Pm(0, 900)])
    for xo in (58, 542):
        sh.bar_run(Pm(xo, 75), Pm(xo, 825), 150, sc, "S-REBAR-MAIN", 1.0)
    for xo in (83, 517):
        for yy in (75, 225, 375, 525, 675, 825):
            sh.bar_dot(Pm(xo, yy), 1.0, "S-REBAR-MAIN")
    for yy in (100, 300, 500, 700, 900):
        sh.rect(*Pm(50, yy - 100), *Pm(550, yy), "S-REBAR-STIRRUP")
    sh.dim_h(Pm(0, 0), Pm(600, 0), Pm(0, -220)[1], sc)
    sh.dim_h(Pm(0, 0), Pm(50, 0), Pm(0, -450)[1], sc)
    sh.dim_v(Pm(600, 75), Pm(600, 225), Pm(760, 0)[0], sc)
    sh.text("150", Pm(820, 140), TXT["small"], "S-TEXT")
    sh.text("50 COVER", Pm(-40, -560), TXT["small"], "S-TEXT")
    V.balloon(sh, (34, 404), "W01", Pm(83, 800))
    V.balloon(sh, (118, 404), "W02", Pm(517, 800))
    V.balloon(sh, (34, 268), "W05", Pm(300, 200))
    sh.view_title((50, 424), "V1", "PERIMETER WALL 600 - ENLARGED SECTION", "SCALE 1:10")

    # V2 W6/W7 400 enlarged
    Pm2 = vw(sc, 190, 300)
    sh.rect(*Pm2(0, 0), *Pm2(400, 900), "S-CONCRETE")
    sh.concrete_hatch([Pm2(0, 0), Pm2(400, 0), Pm2(400, 900), Pm2(0, 900)])
    for xo in (60, 340):
        for yy in (75, 225, 375, 525, 675, 825):
            sh.bar_dot(Pm2(xo, yy), 1.1, "S-REBAR-MAIN")
    for yy in (100, 300, 500, 700, 900):
        sh.rect(*Pm2(50, yy - 100), *Pm2(350, yy), "S-REBAR-STIRRUP")
        sh.line(Pm2(200, yy - 100), Pm2(200, yy), "S-REBAR-STIRRUP")
    sh.dim_h(Pm2(0, 0), Pm2(400, 0), Pm2(0, -220)[1], sc)
    sh.dim_v(Pm2(400, 75), Pm2(400, 225), Pm2(560, 0)[0], sc)
    sh.text("150", Pm2(620, 140), TXT["small"], "S-TEXT")
    V.balloon(sh, (174, 404), "W07", Pm2(60, 800))
    V.balloon(sh, (234, 404), "W08", Pm2(340, 800))
    V.balloon(sh, (174, 268), "W11", Pm2(200, 200))
    sh.view_title((190, 424), "V2", "WALLS W6 / W7 400 - ENLARGED SECTION", "SCALE 1:10")
    sh.text("4-LEGGED LINK = A CLOSED LINK PLUS AN", (190, 268), TXT["small"], "S-TEXT")
    sh.text("INTERNAL LEG EACH WAY (PBR-2).", (190, 263), TXT["small"], "S-TEXT")

    # V3 W5 200
    Pm3 = vw(sc, 300, 300)
    sh.rect(*Pm3(0, 0), *Pm3(200, 900), "S-CONCRETE")
    sh.concrete_hatch([Pm3(0, 0), Pm3(200, 0), Pm3(200, 900), Pm3(0, 900)])
    for xo in (46, 154):
        for yy in (75, 225, 375, 525, 675, 825):
            sh.bar_dot(Pm3(xo, yy), 0.9, "S-REBAR-MAIN")
    sh.dim_h(Pm3(0, 0), Pm3(200, 0), Pm3(0, -220)[1], sc)
    V.balloon(sh, (294, 404), "W16", Pm3(46, 800))
    sh.view_title((300, 424), "V3", "WALL W5 200", "SCALE 1:10")

    y = sh.panel(348, 552, 292, "LINK REQUIREMENTS - WHY THEY EXIST", [
        "IS 4991 Cl. 10.3.1.1 ALLOWS NO DYNAMIC INCREASE ON SHEAR.  tau_c and",
        "tau_c,max are therefore read at the STATIC M35 value while the flexural",
        "capacity uses fck,dyn 43.75 and fy,dyn 625.  This single rule is why the",
        "perimeter walls, W6/W7, the mat, the roof, the headhouse roof and the",
        "headhouse walls all carry links they would not otherwise need.",
        "",
        "ELEMENT            tau_v    tau_c    Vus      Asv/sv   PROVIDED",
        "Perimeter 600      0.802    0.375    220.8    0.982    T12 closed @ 200",
        "W6 / W7 400        1.409    0.540    297.2    1.998    T12 4-leg  @ 200",
        "Mat 600            0.770    0.375    204.2    0.908    T12 @ 250 x 250 grid",
        "Roof 900           0.931    0.450    390.8    1.106    T12 4-leg  @ 250 end",
        "Roof pad           1.015    0.450    459.4    1.300    T12 4-leg  @ 250",
        "Headhouse roof     1.514    0.502    420.0    2.327    T12 4-leg  @ 175 end",
        "Headhouse walls    0.961    0.444    176.9    1.189    T12 4-leg  @ 250",
        "",
        "IS 456 Cl. 26.5.1.5 limits link spacing to min(0.75 d, 300).  For the",
        "perimeter wall that is 300; for W6/W7 257; for the headhouse walls 256.",
        "In every case the SPACING LIMIT, not the shear demand, sets the final",
        "spacing adopted.",
        "",
        "tau_c,max (IS 456 Table 20, M35) = 3.70 N/mm2.  NO SECTION APPROACHES IT.",
    ], TXT["small"], 3.05)
    V.bbs_extract(sh, 348, y - 8, ["W05", "W11", "W14", "W15", "W17"])
    V.materials_panel(sh, 648, 552, 183)
    sh.titleblock(scale="1:10", sheet_of="11 OF 30")
    return sh.save(os.path.join(OUT, "R-204_Wall_Sections.dxf"))


def r205():
    sh = Sheet("R-205", "OPENING REINFORCEMENT DETAILS",
               "BLAST DOORS 1 AND 2 · JAMBS · HEADER · REVEAL",
               flags=["VENDOR DATA NOT AVAILABLE"])
    sh.sheet_header()
    sc = 20
    Pm = vw(sc, 96, 264)
    # elevation of the opening in a 400 wall
    sh.rect(*Pm(-1400, -600), *Pm(2600, 3400), "S-CONCRETE")
    sh.rect(*Pm(0, 0), *Pm(1200, 2100), "S-CONCRETE")
    sh.concrete_hatch([Pm(-1400, -600), Pm(2600, -600), Pm(2600, 3400), Pm(-1400, 3400)],
                      holes=[[Pm(0, 0), Pm(1200, 0), Pm(1200, 2100), Pm(0, 2100)]])
    for o in (70, 145, 220, 295):
        sh.line(Pm(-o, -520), Pm(-o, 2900), "S-REBAR-SEC")
        sh.line(Pm(1200 + o, -520), Pm(1200 + o, 2900), "S-REBAR-SEC")
    for yy in range(-450, 2900, 150):
        sh.line(Pm(-360, yy), Pm(-40, yy), "S-REBAR-STIRRUP")
        sh.line(Pm(1240, yy), Pm(1560, yy), "S-REBAR-STIRRUP")
    # header 400 x 1100
    sh.rect(*Pm(-600, 2100), *Pm(1800, 3200), "S-REBAR-SEC")
    for yy in (2200, 3100):
        sh.line(Pm(-560, yy), Pm(1760, yy), "S-REBAR-MAIN")
    for x in range(-500, 1800, 150):
        sh.line(Pm(x, 2180), Pm(x, 3120), "S-REBAR-STIRRUP")
    sh.dim_h(Pm(0, 0), Pm(1200, 0), Pm(0, -900)[1], sc)
    sh.dim_v(Pm(0, 0), Pm(0, 2100), Pm(-1700, 0)[0], sc)
    sh.dim_v(Pm(2100, 2100), Pm(2100, 3200), Pm(2800, 0)[0], sc)
    sh.dim_h(Pm(-295, 0), Pm(0, 0), Pm(0, -1500)[1], sc)
    V.balloon(sh, (36, 330), "W13", Pm(-180, 1400))
    V.balloon(sh, (36, 290), "W14", Pm(-200, 400))
    V.balloon(sh, (208, 424), "B01", Pm(1400, 3100))
    V.balloon(sh, (208, 400), "B02", Pm(1400, 2200))
    V.balloon(sh, (208, 412), "B03", Pm(1500, 2650))
    sh.view_title((24, 452), "V1", "BLAST DOOR OPENING 1200 x 2100 IN W6 / W7 - ELEVATION",
                  "SCALE 1:20")

    # V2 jamb section
    sc2 = 10
    Pm2 = vw(sc2, 250, 300)
    sh.rect(*Pm2(0, 0), *Pm2(400, 1000), "S-CONCRETE")
    sh.concrete_hatch([Pm2(0, 0), Pm2(400, 0), Pm2(400, 1000), Pm2(0, 1000)])
    for xo in (60, 340):
        for yy in (70, 150, 230, 310):
            sh.bar_dot(Pm2(xo, yy), 1.2, "S-REBAR-SEC")
        for yy in (500, 650, 800, 950):
            sh.bar_dot(Pm2(xo, yy), 1.1, "S-REBAR-MAIN")
    for yy in (80, 230, 380):
        sh.rect(*Pm2(50, yy - 60), *Pm2(350, yy + 60), "S-REBAR-STIRRUP")
    sh.line(Pm2(0, 0), Pm2(0, 400), "S-STEELWORK")
    sh.line(Pm2(-60, 0), Pm2(-60, 400), "S-STEELWORK")
    sh.line(Pm2(-60, 400), Pm2(0, 400), "S-STEELWORK")
    for yy in (100, 250):
        sh.line(Pm2(-60, yy), Pm2(200, yy), "S-STEELWORK")
    sh.dim_h(Pm2(0, 0), Pm2(400, 0), Pm2(0, -180)[1], sc2)
    sh.leader([Pm2(-30, 300), (250, 350)], "CAST-IN STEEL FRAME, WELDED TO THE CAGE (EMP)")
    V.balloon(sh, (240, 288), "W13", Pm2(60, 200))
    sh.view_title((250, 424), "V2", "JAMB SECTION - PLAN CUT", "SCALE 1:10")

    y = sh.panel(330, 552, 310, "BLAST DOOR OPENING - DESIGN", [
        "INTERRUPTED STEEL   2094 x 1.200 = 2513 mm2/face  ->  1256 mm2 EACH JAMB",
        "PROVIDED  4 No. T20 EACH JAMB EACH FACE = 1257 mm2",
        "  *** 1257 vs 1256 - THE ARRANGEMENT IS EXACT, NOT GENEROUS.  Recorded as",
        "      such rather than presented as a comfortable margin. ***",
        "  ANCHORED Ld = 800 BEYOND THE OPENING IN BOTH DIRECTIONS.",
        "",
        "HEADER over the 1200 clear opening, 400 x 1100",
        "  w = 383 x 2.100 / 2                       =  402 kN/m",
        "  M = w L2 / 12                             =  48.2 kNm",
        "  V = w L / 2                               =  241 kN",
        "  tau = 0.578 N/mm2",
        "  PROVIDED  4-T20 TOP + 4-T20 BOTTOM, T12 4-LEGGED LINKS @ 150",
        "",
        "REVEAL   T16 @ 150 U-BARS CLOSE THE REVEAL ON BOTH FACES, ALL ROUND.",
        "",
        "DOOR AND FRAME - WHAT IS AND IS NOT DESIGNED HERE",
        "  The cast-in steel frame is shown ANCHORED INTO AND WELDED TO THE CAGE, for",
        "  EMP continuity.  THE LEAF, ITS ANCHORAGE AND ITS REBOUND RATING ARE A VENDOR",
        "  SUBMITTAL AND ARE [NOT AVAILABLE].  NO PROPRIETARY BLAST-DOOR REQUIREMENT IS",
        "  INVENTED ON THIS SHEET.  Door: proprietary, >= 7 bar, rebound-rated, gas-tight.",
        "",
        "MANUAL CALCULATION - NOT DIRECT STAAD OUTPUT.",
    ], TXT["small"], 3.05)
    V.markkey(sh, 330, y - 6, ["W13", "W14", "W15", "B01", "B02", "B03"], 310)
    V.bbs_extract(sh, 330, 280, ["W13", "W14", "W15", "B01", "B02", "B03"])
    sh.panel(648, 552, 183, "OTHER OPENINGS AND WHERE THEY ARE DETAILED", [
        "ESCAPE SHAFTS ESC 1 / ESC 2, 1400 dia    R-303",
        "STAIR VOID 2800 x 3160                   R-303",
        "SECURITY DOOR 900 x 2100 in HW2          R-702 / R-703",
        "ENTRY DOOR 1000 x 2100                   R-702",
        "SUMP-PIT OPENING 1500 x 1500             R-101 / R-103",
        "PARTITION DOOR GAPS x4  - NO TRIMMING REQUIRED",
        "",
        "NOT DESIGNED - NO STRUCTURAL BASIS EXISTS.  REPORTED",
        "NOT DETERMINABLE, NOT FABRICATED:",
        "  ·  BLAST VALVES x5 - sizes and sleeve details are on",
        "     sheet S-06 and are not in the design register",
        "  ·  SERVICE-ENTRY PLATE, wall W2 at X approx 11 800 -",
        "     plate size [NOT AVAILABLE]",
        "  ·  VENTILATION / CBRN DUCT PENETRATIONS - no",
        "     penetration schedule exists",
        "",
        "A GENERIC TRIMMING RULE IS GIVEN ON R-003 DETAIL D2.",
        "IT IS NOT A SUBSTITUTE FOR A DESIGNED DETAIL.",
    ], TXT["small"], 3.05)
    sh.titleblock(scale="1:20, 1:10", sheet_of="12 OF 30")
    return sh.save(os.path.join(OUT, "R-205_Opening_Reinforcement_Details.dxf"))


def build():
    os.makedirs(OUT, exist_ok=True)
    return [r201(), r202(), r203(), r204(), r205()]


if __name__ == "__main__":
    for f in build():
        print("written", f)
