"""g03_roof.py  --  R-301 to R-304, the pressure (roof) slab."""
import os, math
import sc_proj as P
import sc_dxflib as D
import sc_views as V
import rebar_data as R
from sc_dxflib import Sheet, vw, TXT

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "DXF", "Slabs"))

ROOF_BASIS = [
    "GOVERNING COMBINATION  103 BLAST,  w = 448.15 kPa",
    "  383.00 blast + 40.65 cover [C17] + 2.00 SIDL + 22.50 self",
    "  NO LIVE LOAD ON THE ROOF AT BLAST - IS 4991 Cl. 11.2",
    "  Static ULS 101 = 127.7 kPa  ->  BLAST GOVERNS 3.51 : 1",
    "",
    "ONE-WAY IS NOT A CHOICE, IT IS FORCED",
    "  aspect 20.8 / 5.0 = 4.2, and IS 456 Table 26 is tabulated only to",
    "  ly/lx = 2.0, so TWO-WAY ACTION CANNOT BE CLAIMED.  Mp depends only",
    "  on the 5000 clear width  ->  LENGTHENING THE BOX IS STRUCTURALLY",
    "  FREE (the basis of M1); WIDENING 5.0 -> 6.0 m would raise the roof",
    "  moment 44 %.",
    "",
    "NATURAL PERIOD   m 3250 kg/m2 ; 0.5 EIg 8.985e8 N.m2/m",
    "  f1 = 74.9 Hz  ->  T = 13.4 ms ;  td/T = 10 to 100  ->  QUASI-STATIC",
    "  This is what licenses a static analysis at all.",
    "",
    "FLEXURE   d = 900 - 75 - 12.5 = 812.5",
    "  Mp = w Ln2 / 16 = 448.15 x 25 / 16        =  700.2 kNm/m",
    "  Mu,lim = 3841 kNm/m  OK ;  Ast,req        =  1632 mm2/m",
    "  IS 456 Cl. 26.5.2.1 min 0.12 % x 900      =  1080 mm2/m",
    "  IS 456 Cl. 26.5.2.2 max bar dia D/8 = 112  ->  T25 OK",
    "  PROVIDED T25 @ 150 EF EW = 3272  ->  Mu 1362.4, UTILISATION 51 %",
    "  xu 113.0,  x/d = 0.139 << 0.46",
    "  *** x/d = 0.139 IS THE PROOF THAT mu = 5 IS DEFENSIBLE ***",
    "",
    "SHEAR   V at the support face 1120 kN/m ;  V at d 756.3 kN/m",
    "  tau_v 0.931 | tau_c 0.450 (pt 0.403 %, STATIC M35) | tau_c,max 3.70 OK",
    "  Vus 390.8 ; Asv/sv 1.106  ->  T12 4-leg at 409",
    "  IS 456 Cl. 26.5.1.5 LIMIT 300 GOVERNS",
    "  PROVIDED  T12 4-LEG @ 250 IN THE END 1500 EACH SIDE ; 2-LEG @ 300 MID",
    "",
    "DIRECT SHEAR   Vd,max = 0.16 fck,dyn b d = 5688 kN/m vs 1120 = 19.7 %",
    "  [UFC 3-340-02 section 4-30, cited AS US CRITERIA, NOT AS IS 456]",
    "",
    "MANUAL CALCULATION - NOT DIRECT STAAD OUTPUT.",
]

F2_PANEL = [
    "*** FINDING F2 - NOT DESIGNED IN THE PHASE 1 REPORT ***",
    "",
    "The 2800 x 3160 stair void leaves an 1840 mm CANTILEVER of 900 slab,",
    "2800 wide, carrying the full 448.15 kPa.",
    "",
    "  M(root) = w L2 / 2 = 448.15 x 1.840^2 / 2   =  758.6 kNm/m",
    "  *** THIS EXCEEDS THE 700.2 kNm/m MID-SPAN Mp ***",
    "  Ast,req TOP = 1772 mm2/m  <  3272 provided   ->  UTILISATION 56 %  OK",
    "",
    "  V(root) = 448.15 x 1.840                     =  824.6 kN/m",
    "  tau_v 1.015 > tau_c 0.450 ; Vus 459.4 ; Asv/sv 1.300",
    "  ->  T12 4-leg at 348 ; Cl. 26.5.1.5 limit 300",
    "  ADOPTED  T12 4-LEGGED LINKS @ 250 THROUGHOUT THE PAD  (NEW REQUIREMENT)",
    "",
    "PLUS   free edge thickened 900 -> 1200 over 600, with 6-T25 top +",
    "       6-T25 bottom and T12 closed links @ 150",
    "PLUS   6 No. T25 each face, top and bottom, in a 900 band over W6 and W7",
    "PLUS   diagonal trimmers 4 No. T25 each face at 45 deg at BOTH re-entrant",
    "       corners, 2000 long each way, anchored Ld beyond",
    "PLUS   1100 mm guarding to the free edge (NBC 2016 Part 4) - architectural,",
    "       shown for coordination only",
    "",
    "THE RE-ENTRANT CORNERS ARE THE CRACK INITIATORS.  The 45 deg diagonal",
    "trimmers are MANDATORY, not decorative.",
]


def r301():
    sh = Sheet("R-301", "ROOF / PRESSURE SLAB REINFORCEMENT PLAN",
               "900 THK · T25 @ 150 EF EW · THE GOVERNING ELEMENT",
               flags=["C17 COVER LOAD", "F2 CANTILEVER PAD"])
    sh.sheet_header()
    sc = 50
    Pm = vw(sc, 66, 400)
    sh.rect(*Pm(0, 0), *Pm(22000, 6200), "S-CONCRETE")
    sh.rect(*Pm(600, 600), *Pm(21400, 5600), "S-CONCRETE-THIN")
    for mk, x0, x1, t in P.IW:
        sh.dline(Pm(x0, 0), Pm(x0, 6200), "S-HIDDEN")
        sh.dline(Pm(x1, 0), Pm(x1, 6200), "S-HIDDEN")
        sh.text(mk, Pm((x0 + x1) / 2, 6500), TXT["small"], "S-TEXT", "CENTER")
    # main steel, diagrammatic outside the void
    for x in range(900, 22000, 1500):
        if not (15200 <= x <= 18000):
            sh.line(Pm(x, 75), Pm(x, 6125), "S-REBAR-MAIN")
    for y in range(600, 6200, 1200):
        sh.line(Pm(75, y), Pm(15200, y), "S-REBAR-MAIN")
        sh.line(Pm(18000, y), Pm(21925, y), "S-REBAR-MAIN")
    # void and pad
    Vd = P.VOID
    sh.rect(*Pm(Vd["x0"], Vd["y0"]), *Pm(Vd["x1"], Vd["y1"]), "S-CONCRETE")
    sh.line(Pm(Vd["x0"], Vd["y0"]), Pm(Vd["x1"], Vd["y1"]), "S-CENTER")
    sh.line(Pm(Vd["x0"], Vd["y1"]), Pm(Vd["x1"], Vd["y0"]), "S-CENTER")
    sh.text("STAIR VOID 2800 x 3160", Pm(16600, 2100), TXT["small"], "S-TEXT", "CENTER")
    Pd = P.PAD
    for x in range(15300, 18000, 150):
        sh.line(Pm(x, Pd["y0"] + 50), Pm(x, 6125), "S-REBAR-MAIN")
    sh.rect(*Pm(Pd["x0"], Pd["y0"]), *Pm(Pd["x1"], Pd["y1"]), "S-REFERENCE")
    sh.text("CANTILEVER PAD 2800 x 1840", Pm(16600, 4600), TXT["small"], "S-BLAST", "CENTER")
    # free edge thickening
    sh.rect(*Pm(Vd["x0"], Vd["y1"]), *Pm(Vd["x1"], Vd["y1"] + 600), "S-REBAR-SEC")
    # re-entrant corner diagonals
    for cx in (Vd["x0"], Vd["x1"]):
        s = 1 if cx == Vd["x0"] else -1
        for o in (0, 120, 240, 360):
            sh.line(Pm(cx + s * o, Vd["y1"] + 2000),
                    Pm(cx + s * (2000 + o), Vd["y1"]), "S-REBAR-SEC")
    # escape shafts
    for nm, cx, cy in P.ESC:
        sh.circle(Pm(cx, cy), 700 / sc, "S-CONCRETE")
        sh.circle(Pm(cx, cy), 950 / sc, "S-CONCRETE")
        sh.circle(Pm(cx, cy), 1250 / sc, "S-REBAR-SEC")
        sh.cline(Pm(cx - 1500, cy), Pm(cx + 1500, cy))
        sh.cline(Pm(cx, cy - 1500), Pm(cx, cy + 1500))
        for o in (-1150, -1050, -950, 950, 1050, 1150):
            sh.line(Pm(cx + o, cy - 1500), Pm(cx + o, cy + 1500), "S-REBAR-SEC")
            sh.line(Pm(cx - 1500, cy + o), Pm(cx + 1500, cy + o), "S-REBAR-SEC")
        sh.text(nm, Pm(cx, cy - 1750), TXT["small"], "S-TEXT", "CENTER")
    # HW3 band
    sh.rect(*Pm(13400, 600), *Pm(14600, 5600), "S-REBAR-SEC")
    sh.text("HW3 BAND", Pm(14000, 5750), TXT["small"], "S-REBAR-SEC", "CENTER")
    V.dim_box_plan(sh, Pm, sc)
    sh.dim_h(Pm(15200, 0), Pm(18000, 0), Pm(0, -1000)[1], sc)
    sh.dim_v(Pm(15200, 600), Pm(15200, 3760), Pm(14200, 0)[0], sc)
    sh.north((560, 456))
    V.balloon(sh, (110, 456), "S01A", Pm(2600, 3000))
    V.balloon(sh, (160, 510), "S02A", Pm(5000, 5400))
    V.balloon(sh, (398, 528), "S03B", Pm(16600, 5200))
    V.balloon(sh, (450, 470), "S08", Pm(19900, 3300))
    V.balloon(sh, (392, 486), "S12", Pm(16600, 3900))
    V.balloon(sh, (348, 486), "S15", Pm(15900, 4400))
    V.balloon(sh, (296, 512), "S16", Pm(14000, 5400))
    sh.view_title((66, 552), "V1", "PRESSURE SLAB PLAN - REINFORCEMENT AND OPENINGS",
                  "SCALE 1:50")
    sh.secmark((58, 424), "C")
    sh.secmark((520, 424), "C")
    sh.text("SECTION C-C  ->  R-302", (400, 380), TXT["small"], "S-SECTION", "CENTER")
    sh.text("TOP OF SLAB (-)2.000  ·  SOFFIT (-)2.900  ·  2000 ENGINEERED COVER OVER  ·  "
            "STEEL SHOWN DIAGRAMMATICALLY, ACTUAL SPACING 150 BOTH WAYS BOTH FACES",
            (66, 372), TXT["small"], "S-TEXT")

    yk = V.markkey(sh, 66, 352, ["S01A", "S01B", "S02A", "S02B", "S02C", "S03A",
                                 "S03B", "S03C", "S04A", "S04B", "S04C", "S05",
                                 "S06", "S07"], 240)
    # QA1: chained off the block above so the two can never collide
    V.markkey(sh, 66, yk - 8, ["S08", "S09", "S10", "S11", "S12", "S13", "S14",
                               "S15", "S16"], 240, "BAR MARK KEY - OPENINGS AND BANDS")
    yb = V.loading_panel(sh, 316, 352, 322, ROOF_BASIS, TXT["small"], 3.05,
                         heading="PRESSURE SLAB - DESIGN BASIS")
    V.bbs_extract(sh, 316, yb - 8, ["S01A", "S01B", "S02A", "S02B", "S02C", "S03A",
                                    "S03B", "S03C", "S04A", "S04B", "S04C", "S05",
                                    "S06", "S07"])
    sh.panel(648, 552, 183, "THICKNESS STUDY - WHY 900 AND NOT 800", [
        "t     d      Mp     Ast,req  tau_v  VERDICT",
        "600  512.5   689    2673     1.71   links at 164, congested",
        "800  712.5   696    1868     1.12   structural optimum",
        "900  812.5   700    1633     0.93   ADOPTED",
        "1000 912.5   704    1453     0.78   11 % over",
        "",
        "900 IS NOT THE STRUCTURAL OPTIMUM.  It is adopted for:",
        "(a)  reserve at the two 1400 dia collars",
        "(b)  headroom against a raised design basis threat while the",
        "     DBT YIELD IS [UNRESOLVED - U3]",
        "(c)  support rotation inside 2 deg without UFC lacing",
        "",
        "*** C17 RULED AND CLOSED - RC1, 10.09.26, master H.14 ***",
        "The engineered cover is stated as 40.65 kPa in A.7.3, A.7.4,",
        "Part L and every .std file, while the A.7.3 column itself sums",
        "to 39.15 kPa.  40.65 IS HELD, and A.7.3 now SHOWS why: the",
        "layer sum 39.15 PLUS A DECLARED ALLOWANCE OF 1.50.  The table",
        "no longer disagrees with itself and nothing downstream moves -",
        "COMB 103 stays 448.15 kPa and there are NO BAR CHANGES.",
    ], TXT["small"], 3.05)
    sh.panel(648, 380, 183, "ROOF OPENING REGISTER", [
        "ESC 1    1400 dia   centre (2 050, 2 050)",
        "ESC 2    1400 dia   centre (19 900, 2 050)  post-M1",
        "STAIR VOID  2800 x 3160   X 15200-18000, Y 600-3760",
        "  leaving a 2800 x 1840 CANTILEVER PAD",
        "NO OTHER OPENING PIERCES THE PRESSURE SLAB.",
        "",
        "THE 750 mm CLEARANCE RULE - opening edge to structural",
        "wall face:  250 collar + ~400 trimmer band + 100 tolerance.",
        "A BAY MUST THEREFORE BE AT LEAST 1400 + 2 x 750 = 2900 mm",
        "WIDE TO HOLD AN ESCAPE SHAFT.  This rule drove the Rev C",
        "lengthening and IS WHY MODIFICATION M1 COULD NOT TAKE",
        "400 mm OUT OF BAY 8.  M1 improved ESC 2 to headhouse",
        "clearance from 350 to 550.",
        "",
        "SERVICE PENETRATIONS - blast valves x5, the service-entry",
        "plate and the CBRN ducts - ARE NOT DESIGNED IN THE PROJECT",
        "RECORD and are NOT fabricated here.  Generic trimming rule",
        "on R-003 detail D2.  Reported NOT DETERMINABLE.",
    ], TXT["small"], 3.05)
    sh.panel(30, 126, 600, "PRESSURE SLAB - THE SINGLE MOST IMPORTANT STRUCTURAL FACT", [
        "THE ROOF SPANS ONE-WAY ACROSS THE 5 000 mm INTERNAL WIDTH.  The aspect ratio is",
        "20.8 / 5.0 = 4.2, and IS 456 Table 26 is tabulated only to ly/lx = 2.0, so two-way",
        "action cannot be claimed.  Mp therefore depends on the 5 000 width ALONE.",
        "",
        "CONSEQUENCE 1 - LENGTHENING THE BOX IS STRUCTURALLY FREE.  This is what made",
        "MODIFICATION M1 affordable: the box grew 21 600 -> 22 000 and not one bar in the",
        "roof changed.",
        "CONSEQUENCE 2 - WIDENING IS EXPENSIVE.  Going from 5.0 m to 6.0 m internal width",
        "would raise the roof moment by 44 % and would re-open the 900 mm thickness, the",
        "T25 @ 150 arrangement and the link zones together.",
        "",
        "PRESERVE THIS.  Any future request to widen the shelter is a request to redesign",
        "the pressure slab, the walls that carry it and the mat beneath it.",
    ], TXT["small"], 3.05)
    sh.titleblock(scale="1:50", sheet_of="13 OF 30")
    return sh.save(os.path.join(OUT, "R-301_Roof_Slab_Reinforcement_Plan.dxf"))


def r302():
    sh = Sheet("R-302", "ROOF SECTIONS",
               "SECTION C-C · TYPICAL SLAB SECTION · LINK ZONES",
               flags=["C17 COVER LOAD"])
    sh.sheet_header()
    sc = 40
    Pm = vw(sc, 60, 340)
    # walls and slab
    sh.rect(*Pm(0, 0), *Pm(600, 900), "S-CONCRETE")
    sh.rect(*Pm(5600, 0), *Pm(6200, 900), "S-CONCRETE")
    sh.rect(*Pm(0, 0), *Pm(6200, 900), "S-CONCRETE")
    sh.concrete_hatch([Pm(0, 0), Pm(6200, 0), Pm(6200, 900), Pm(0, 900)])
    sh.rect(*Pm(0, -1400), *Pm(600, 0), "S-CONCRETE")
    sh.rect(*Pm(5600, -1400), *Pm(6200, 0), "S-CONCRETE")
    sh.concrete_hatch([Pm(0, -1400), Pm(600, -1400), Pm(600, 0), Pm(0, 0)])
    sh.concrete_hatch([Pm(5600, -1400), Pm(6200, -1400), Pm(6200, 0), Pm(5600, 0)])
    # haunches
    sh.pline([Pm(600, 0), Pm(1100, 0), Pm(600, -500)], "S-CONCRETE")
    sh.pline([Pm(5600, 0), Pm(5100, 0), Pm(5600, -500)], "S-CONCRETE")
    # engineered cover
    # BS1: the burster slab and everything above it are laid to a 1:50 crossfall,
    # crowned on the box centreline (Y = 3100), parallel to the finished grade
    # (A.4.3).  The fall is taken up in the COMPACTED FILL, which is nominal 750
    # at the crown and thins to 688 at the box edge, so the cover load does not
    # increase anywhere.  Drawn as a real crown, not a note.
    CROWN_X, FALL = 3100.0, 1.0 / 50.0
    def crown(x):
        """Rise of the crowned layers above their box-edge level, at box Y = x."""
        return (CROWN_X - abs(x - CROWN_X)) * FALL

    # Only the protection screed is flat - it sits on the flat roof.  The top of
    # the compacted fill is CROWNED, because the fill is the layer that takes up
    # the fall; that same line is the underside of the crushed basalt.
    sh.line(Pm(-800, 1000), Pm(7000, 1000), "S-EXISTING")
    sh.text("PROTECTION SCREED 100", Pm(7100, 910), TXT["small"], "S-EXISTING")
    sh.text("COMPACTED FILL 750 CROWN / 688 EDGE", Pm(7100, 1330), TXT["small"], "S-EXISTING")

    sloped = [(1750, "CRUSHED BASALT 500"), (2250, "BURSTER SLAB M30 200 - LAID TO FALLS"),
              (2450, "GRANULAR FILTER 150 - DRAINS ON THE SLAB"),
              (2600, "TOPSOIL / TURF 300"), (2900, "FINISHED GRADE, CROWNED 1:50")]
    for lev, lab in sloped:
        pts = [Pm(x, lev + crown(x)) for x in (-800, 0, CROWN_X, 6200, 7000)]
        sh.pline(pts, "S-WATERPROOF" if "BURSTER" in lab else "S-EXISTING")
        sh.text(lab, Pm(7100, lev + crown(7000) - 40), TXT["small"], "S-EXISTING")
    # fall arrows on the filter layer, the layer that actually carries the seepage
    for x, d in ((1400, -1), (4800, +1)):
        sh.line(Pm(x, 2450 + crown(x) + 70), Pm(x + d * 700, 2450 + crown(x + d * 700) + 70),
                "S-BLAST")
        sh.text("1:50", Pm(x + d * 250, 2450 + crown(x) + 150), TXT["small"], "S-BLAST")
    sh.line(Pm(-800, 900), Pm(7000, 900), "S-WATERPROOF")
    # blast arrows
    for x in range(400, 6200, 800):
        sh.line(Pm(x, 3400), Pm(x, 2950), "S-BLAST")
        sh.pline([Pm(x - 90, 3100), Pm(x, 2950), Pm(x + 90, 3100)], "S-BLAST")
    sh.text("BLAST 383 kPa + COVER 40.65 + SIDL 2.0 + SELF 22.5  =  448.15 kPa",
            Pm(600, 3500), TXT["note"], "S-BLAST")
    # reinforcement
    sh.line(Pm(60, 813), Pm(6140, 813), "S-REBAR-MAIN")
    sh.line(Pm(60, 88), Pm(6140, 88), "S-REBAR-MAIN")
    sh.bar_run(Pm(150, 813), Pm(6050, 813), 150, sc, "S-REBAR-MAIN", 0.7)
    sh.bar_run(Pm(150, 88), Pm(6050, 88), 150, sc, "S-REBAR-MAIN", 0.7)
    for x in range(200, 1700, 250):
        sh.rect(*Pm(x - 60, 80), *Pm(x + 60, 820), "S-REBAR-STIRRUP")
        sh.rect(*Pm(6200 - x - 60, 80), *Pm(6200 - x + 60, 820), "S-REBAR-STIRRUP")
    for x in range(2200, 4200, 300):
        sh.rect(*Pm(x - 60, 80), *Pm(x + 60, 820), "S-REBAR-STIRRUP")
    sh.dim_h(Pm(600, 0), Pm(5600, 0), Pm(0, -2000)[1], sc)
    sh.dim_h(Pm(0, 0), Pm(6200, 0), Pm(0, -2600)[1], sc)
    sh.dim_v(Pm(6200, 0), Pm(6200, 900), Pm(7600, 0)[0], sc)
    sh.dim_h(Pm(600, 900), Pm(2100, 900), Pm(0, 3100)[1], sc)
    sh.text("END ZONE 1500 - T12 4-LEG @ 250", Pm(700, 3200), TXT["small"], "S-TEXT")
    sh.text("MID ZONE - T12 2-LEG @ 300", Pm(2600, 3200), TXT["small"], "S-TEXT")
    sh.level(Pm(3100, 900), "(-)2.000")
    sh.level(Pm(3100, 0), "(-)2.900")
    V.balloon(sh, (76, 396), "S03A", Pm(1200, 813))
    V.balloon(sh, (76, 348), "S01A", Pm(1200, 88))
    V.balloon(sh, (196, 372), "S05", Pm(1000, 450))
    V.balloon(sh, (140, 372), "S06", Pm(3100, 450))
    sh.view_title((60, 552), "V1", "SECTION C-C  -  PRESSURE SLAB, COVER AND SUPPORTS",
                  "SCALE 1:40")

    y = V.loading_panel(sh, 350, 552, 288, [
        "LAYER                       t     gamma   kPa   FUNCTION",
        "Topsoil / turf             300     18     5.40  concealment, erosion",
        "Granular filter            150     19     2.85  stops fines clogging",
        "RC burster slab M30        200     25     5.00  BREAKS UP A PENETRATOR",
        "                           LAID TO A 1:50 CROSSFALL - BS1, master A.7.3",
        "Crushed basalt 25-75       500     17     8.50  scatters burster energy",
        "Compacted fill 95 % MDD    750     20    15.00  RADIATION MASS",
        "Protection screed          100     24     2.40  protects the membrane",
        "TOTAL                     2000           39.15   <- COLUMN SUM",
        "STATED IN THE MASTER                     40.65   <- HELD  *** C17 ***",
        "",
        "WHY 2.0 m - NOT BLAST AND NOT FALLOUT.  A buried roof takes full p_so",
        "regardless (IS 4991 Cl. 7.2), and 1.0 m already gives a protection",
        "factor of about 2200 against a requirement of about 1000.  THE SECOND",
        "METRE IS BOUGHT ENTIRELY FOR PROMPT NEUTRON AND GAMMA ATTENUATION,",
        "which needs mass and needs it ABOVE the slab.",
        "Reducing 4.0 m to 2.0 m saved 2 m of rock excavation, 2 m of shaft,",
        "one stair flight and 2 m of headroom.",
    ], TXT["small"], 3.05, heading="ENGINEERED COVER BUILD-UP - AND CONFLICT C17")
    sh.panel(350, y - 6, 288, "SECTION NOTES", [
        "1  TOP AND BOTTOM CURTAINS T25 @ 150 BOTH WAYS, 75 COVER TO EACH FACE.",
        "2  TOP STEEL IS CONTINUOUS OVER EVERY SUPPORT and is anchored Ld = 1000",
        "   into the wall.  Bottom steel is continuous, laps staggered at mid-span.",
        "3  LINKS:  T12 4-LEGGED @ 250 IN THE END 1500 EACH SIDE, T12 2-LEGGED @ 300",
        "   ELSEWHERE.  The end-zone spacing is set by IS 456 Cl. 26.5.1.5 (limit 300),",
        "   not by the shear demand, which would allow 409.",
        "4  500 x 500 HAUNCH WITH T20 @ 150 DIAGONALS AT BOTH SUPPORTS - R-304.",
        "5  THE WATERPROOFING MEMBRANE SITS DIRECTLY ON THE SLAB and is protected by",
        "   the 100 screed, which is the first layer of the engineered cover - R-805.",
        "6  NO MOVEMENT JOINT ANYWHERE IN THE SLAB.",
    ], TXT["small"], 3.05)
    V.materials_panel(sh, 648, 552, 183)
    sh.titleblock(scale="1:40", sheet_of="14 OF 30")
    return sh.save(os.path.join(OUT, "R-302_Roof_Sections.dxf"))


def r303():
    sh = Sheet("R-303", "ROOF OPENING DETAILS",
               "ESCAPE-SHAFT COLLARS · STAIR VOID · CANTILEVER PAD · RE-ENTRANT CORNERS",
               flags=["F2 CANTILEVER PAD"])
    sh.sheet_header()
    # V1 escape shaft collar plan 1:25
    sc = 25
    Pm = vw(sc, 90, 400)
    sh.circle(Pm(0, 0), 700 / sc, "S-CONCRETE")
    sh.circle(Pm(0, 0), 950 / sc, "S-CONCRETE")
    sh.circle(Pm(0, 0), 1550 / sc, "S-REFERENCE")
    sh.cline(Pm(-1900, 0), Pm(1900, 0))
    sh.cline(Pm(0, -1900), Pm(0, 1900))
    for o in (1050, 1180, 1310, 1440, 1570):
        for s in (1, -1):
            sh.line(Pm(s * o, -1800), Pm(s * o, 1800), "S-REBAR-SEC")
            sh.line(Pm(-1800, s * o), Pm(1800, s * o), "S-REBAR-SEC")
    for r in (820, 950, 1080):
        sh.circle(Pm(0, 0), r / sc, "S-REBAR-MAIN")
    for i in range(24):
        a = i * math.pi / 12
        sh.line(Pm(700 * math.cos(a), 700 * math.sin(a)),
                Pm(1500 * math.cos(a), 1500 * math.sin(a)), "S-REBAR-DIST")
    sh.dim_h(Pm(-700, -1900), Pm(700, -1900), Pm(0, -2200)[1], sc)
    sh.dim_h(Pm(-950, -1900), Pm(950, -1900), Pm(0, -2700)[1], sc)
    V.balloon(sh, (150, 462), "S08", Pm(1180, 900))
    V.balloon(sh, (60, 440), "S09", Pm(-950, 200))
    V.balloon(sh, (60, 372), "S10", Pm(-800, -800))
    sh.view_title((30, 552), "V1", "ESCAPE-SHAFT COLLAR - PLAN ON THE ROOF SLAB",
                  "SCALE 1:25")
    sh.text("CIRCULAR IS THE RIGHT SHAPE: HOOP ACTION, NO RE-ENTRANT", (30, 322),
            TXT["small"], "S-TEXT")
    sh.text("STRESS CONCENTRATION.  THIS DETAIL SETS THE 750 mm CLEARANCE", (30, 317),
            TXT["small"], "S-TEXT")
    sh.text("RULE - A BAY MUST BE AT LEAST 2900 WIDE TO HOLD AN ESCAPE SHAFT.",
            (30, 312), TXT["small"], "S-BLAST")

    # V2 collar section 1:25
    Pm2 = vw(sc, 220, 400)
    sh.rect(*Pm2(-2600, 0), *Pm2(-700, 900), "S-CONCRETE")
    sh.rect(*Pm2(700, 0), *Pm2(2600, 900), "S-CONCRETE")
    sh.rect(*Pm2(-1300, -300), *Pm2(-700, 900), "S-CONCRETE")
    sh.rect(*Pm2(700, -300), *Pm2(1300, 900), "S-CONCRETE")
    for pts in ([Pm2(-2600, 0), Pm2(-700, 0), Pm2(-700, 900), Pm2(-2600, 900)],
                [Pm2(700, 0), Pm2(2600, 0), Pm2(2600, 900), Pm2(700, 900)],
                [Pm2(-1300, -300), Pm2(-700, -300), Pm2(-700, 0), Pm2(-1300, 0)],
                [Pm2(700, -300), Pm2(1300, -300), Pm2(1300, 0), Pm2(700, 0)]):
        sh.concrete_hatch(pts)
    sh.rect(*Pm2(-950, 900), *Pm2(-700, 2400), "S-CONCRETE")
    sh.rect(*Pm2(700, 900), *Pm2(950, 2400), "S-CONCRETE")
    sh.bar_run(Pm2(-2500, 813), Pm2(-800, 813), 150, sc, "S-REBAR-MAIN", 0.6)
    sh.bar_run(Pm2(800, 813), Pm2(2500, 813), 150, sc, "S-REBAR-MAIN", 0.6)
    sh.bar_run(Pm2(-2500, 88), Pm2(-800, 88), 150, sc, "S-REBAR-MAIN", 0.6)
    sh.bar_run(Pm2(800, 88), Pm2(2500, 88), 150, sc, "S-REBAR-MAIN", 0.6)
    for x in (-1250, -1100, -950, 950, 1100, 1250):
        sh.rect(*Pm2(x - 50, -220), *Pm2(x + 50, 820), "S-REBAR-STIRRUP")
    sh.dim_v(Pm2(2600, 0), Pm2(2600, 900), Pm2(3100, 0)[0], sc)
    sh.dim_v(Pm2(-2600, -300), Pm2(-2600, 900), Pm2(-3200, 0)[0], sc)
    sh.dim_h(Pm2(-700, -300), Pm2(700, -300), Pm2(0, -800)[1], sc)
    sh.text("SLAB THICKENED 900 -> 1200 OVER A 600 ANNULUS", Pm2(-2600, -1300),
            TXT["small"], "S-TEXT")
    V.balloon(sh, (206, 356), "S11", Pm2(-1100, 300))
    sh.view_title((174, 552), "V2", "ESCAPE-SHAFT COLLAR - SECTION", "SCALE 1:25")

    # V3 stair void free edge 1:25
    Pm3 = vw(sc, 350, 400)
    sh.rect(*Pm3(0, 0), *Pm3(2400, 900), "S-CONCRETE")
    sh.rect(*Pm3(0, -300), *Pm3(600, 900), "S-CONCRETE")
    sh.concrete_hatch([Pm3(0, -300), Pm3(600, -300), Pm3(600, 900), Pm3(0, 900)])
    sh.concrete_hatch([Pm3(600, 0), Pm3(2400, 0), Pm3(2400, 900), Pm3(600, 900)])
    for xo in (100, 200, 300, 400, 500):
        sh.bar_dot(Pm3(xo, 800), 1.0, "S-REBAR-SEC")
        sh.bar_dot(Pm3(xo, -200), 1.0, "S-REBAR-SEC")
    sh.bar_run(Pm3(700, 813), Pm3(2350, 813), 150, sc, "S-REBAR-MAIN", 0.7)
    sh.bar_run(Pm3(700, 88), Pm3(2350, 88), 150, sc, "S-REBAR-MAIN", 0.7)
    for x in range(75, 600, 150):
        sh.rect(*Pm3(x - 40, -240), *Pm3(x + 40, 840), "S-REBAR-STIRRUP")
    for x in range(750, 2400, 250):
        sh.rect(*Pm3(x - 50, 80), *Pm3(x + 50, 820), "S-REBAR-STIRRUP")
    sh.dim_v(Pm3(0, -300), Pm3(0, 900), Pm3(-500, 0)[0], sc)
    sh.dim_h(Pm3(0, -300), Pm3(600, -300), Pm3(0, -800)[1], sc)
    V.balloon(sh, (336, 458), "S12", Pm3(300, 800))
    V.balloon(sh, (336, 340), "S13", Pm3(300, 200))
    V.balloon(sh, (444, 450), "S07", Pm3(1600, 500))
    sh.view_title((320, 552), "V3", "STAIR-VOID FREE EDGE - SECTION THROUGH THE PAD",
                  "SCALE 1:25")
    sh.text("EDGE THICKENED 900 -> 1200 OVER 600", (320, 322), TXT["small"], "S-TEXT")
    sh.text("6-T25 TOP + 6-T25 BOTTOM, T12 CLOSED LINKS @ 150", (320, 317),
            TXT["small"], "S-TEXT")

    # V4 re-entrant corner 1:40
    sc4 = 40
    Pm4 = vw(sc4, 490, 400)
    sh.rect(*Pm4(-2500, -1500), *Pm4(2500, 2500), "S-CONCRETE")
    sh.rect(*Pm4(-2500, -1500), *Pm4(0, 0), "S-CONCRETE")
    sh.concrete_hatch([Pm4(-2500, 0), Pm4(2500, 0), Pm4(2500, 2500), Pm4(-2500, 2500)])
    sh.concrete_hatch([Pm4(0, -1500), Pm4(2500, -1500), Pm4(2500, 0), Pm4(0, 0)])
    for o in (0, 150, 300, 450):
        sh.line(Pm4(-2000 + o, 0), Pm4(0, 2000 - o), "S-REBAR-SEC")
        sh.line(Pm4(0 + o, -1400), Pm4(1400 + o, 0), "S-REBAR-SEC")
    sh.text("VOID", Pm4(-1400, -800), TXT["note"], "S-TEXT", "CENTER")
    sh.dim_h(Pm4(0, 2500), Pm4(2000, 2500), Pm4(0, 3000)[1], sc4)
    V.balloon(sh, (528, 466), "S15", Pm4(-900, 1100))
    sh.view_title((470, 552), "V4", "RE-ENTRANT CORNER TRIMMERS", "SCALE 1:40")
    sh.text("4-T25 EACH FACE AT 45 DEG, 2000 LONG EACH WAY,", (470, 322),
            TXT["small"], "S-TEXT")
    sh.text("ANCHORED Ld BEYOND.  BOTH CORNERS.  MANDATORY.", (470, 317),
            TXT["small"], "S-BLAST")

    V.loading_panel(sh, 30, 300, 300, F2_PANEL, TXT["small"], 3.05,
                    heading="FINDING F2 - THE CANTILEVER PAD")
    y = V.loading_panel(sh, 340, 300, 298, [
        "INTERRUPTED STEEL  3272 x 1.400          =  4581 mm2/face/direction",
        "TRIMMERS EACH SIDE                        =  2291 mm2",
        "PROVIDED  5 No. T25 EACH SIDE, EACH FACE, EACH DIRECTION = 2454 mm2  OK",
        "  ANCHORED Ld = 1000 BEYOND THE OPENING.",
        "COLLAR  250 RC, OD 1900 ;  T16 @ 150 HOOPS x3 LAYERS + T16 @ 150 RADIALS",
        "SLAB THICKENED 900 -> 1200 OVER A 600 ANNULUS, T12 CLOSED LINKS @ 150",
        "",
        "THE 750 mm CLEARANCE RULE - opening edge to structural wall face",
        "  750 = 250 collar + about 400 trimmer band + 100 tolerance",
        "  ->  A BAY MUST BE AT LEAST 1400 + 2 x 750 = 2900 mm WIDE.",
        "  This rule drove the Rev C lengthening and it is WHY MODIFICATION M1",
        "  COULD NOT TAKE 400 mm OUT OF BAY 8.",
        "  ESC 1 clearance 750 all round ; ESC 2 800 / 800 after M1.",
        "",
        "ESC 1 centre (2050, 2050)  ·  ESC 2 centre (19 900, 2050) after M1",
        "  [CONFIRMED - read directly from 1_Underground_Level_Plan.dxf]",
        "",
        "MANUAL CALCULATION - NOT DIRECT STAAD OUTPUT.",
    ], TXT["small"], 3.05, heading="ESCAPE-SHAFT OPENINGS - DESIGN")
    V.bbs_extract(sh, 340, y - 8, ["S07", "S08", "S09", "S10", "S11", "S12", "S13",
                                   "S14", "S15", "S16"])
    sh.titleblock(scale="1:25, 1:40", sheet_of="15 OF 30")
    return sh.save(os.path.join(OUT, "R-303_Roof_Opening_Details.dxf"))


def r304():
    sh = Sheet("R-304", "ROOF / WALL JUNCTION DETAILS",
               "HAUNCHES · ANCHORAGE OF TOP STEEL · HW3 LINE-LOAD BAND")
    sh.sheet_header()
    sc = 15
    Pm = vw(sc, 60, 232)
    sh.rect(*Pm(0, 0), *Pm(600, 1800), "S-CONCRETE")
    sh.rect(*Pm(0, 1800), *Pm(2600, 2700), "S-CONCRETE")
    sh.pline([Pm(600, 1800), Pm(1100, 1800), Pm(600, 1300)], "S-CONCRETE")
    for pts in ([Pm(0, 0), Pm(600, 0), Pm(600, 1800), Pm(0, 1800)],
                [Pm(0, 1800), Pm(2600, 1800), Pm(2600, 2700), Pm(0, 2700)],
                [Pm(600, 1800), Pm(1100, 1800), Pm(600, 1300)]):
        sh.concrete_hatch(pts)
    for xo in (58, 542):
        sh.line(Pm(xo, 40), Pm(xo, 1760), "S-REBAR-MAIN")
        sh.bar_run(Pm(xo, 150), Pm(xo, 1700), 150, sc, "S-REBAR-MAIN", 0.8)
    sh.pline([Pm(2550, 2613), Pm(88, 2613), Pm(88, 1500)], "S-REBAR-MAIN")
    sh.pline([Pm(2550, 1888), Pm(400, 1888), Pm(400, 1300)], "S-REBAR-MAIN")
    for i in range(4):
        o = i * 150
        sh.line(Pm(600 + o, 1760), Pm(660, 1760 - o), "S-REBAR-SEC")
    for yy in range(150, 1800, 200):
        sh.rect(*Pm(50, yy - 50), *Pm(550, yy + 50), "S-REBAR-STIRRUP")
    for x in range(700, 2600, 250):
        sh.rect(*Pm(x - 55, 1875), *Pm(x + 55, 2625), "S-REBAR-STIRRUP")
    sh.dim_v(Pm(2600, 1800), Pm(2600, 2700), Pm(3000, 0)[0], sc)
    sh.dim_h(Pm(0, 0), Pm(600, 0), Pm(0, -300)[1], sc)
    sh.dim_h(Pm(600, 1800), Pm(1100, 1800), Pm(0, 3100)[1], sc)
    sh.dim_h(Pm(88, 2613), Pm(1088, 2613), Pm(0, 3800)[1], sc)
    sh.text("Ld = 1000 (T25)", Pm(1200, 3720), TXT["small"], "S-TEXT")
    sh.level(Pm(1700, 2700), "(-)2.000")
    sh.level(Pm(1700, 1800), "(-)2.900")
    V.balloon(sh, (252, 408), "S03A", Pm(1500, 2613))
    V.balloon(sh, (252, 368), "S01A", Pm(1500, 1888))
    V.balloon(sh, (140, 330), "W06", Pm(830, 1600))
    V.balloon(sh, (34, 300), "W01", Pm(58, 900))
    sh.view_title((30, 500), "V1", "ROOF / PERIMETER WALL JUNCTION - 500 x 500 HAUNCH",
                  "SCALE 1:15")

    # V2 HW3 band
    sc2 = 25
    Pm2 = vw(sc2, 330, 340)
    sh.rect(*Pm2(0, 0), *Pm2(5000, 900), "S-CONCRETE")
    sh.concrete_hatch([Pm2(0, 0), Pm2(5000, 0), Pm2(5000, 900), Pm2(0, 900)])
    sh.rect(*Pm2(2300, 900), *Pm2(2700, 3300), "S-CONCRETE")
    sh.concrete_hatch([Pm2(2300, 900), Pm2(2700, 900), Pm2(2700, 3300), Pm2(2300, 3300)])
    sh.rect(*Pm2(1900, 0), *Pm2(3100, 900), "S-REBAR-SEC")
    for xo in (2050, 2350, 2650, 2950):
        sh.bar_dot(Pm2(xo, 813), 1.1, "S-REBAR-SEC")
        sh.bar_dot(Pm2(xo, 88), 1.1, "S-REBAR-SEC")
    sh.bar_run(Pm2(100, 813), Pm2(4900, 813), 150, sc2, "S-REBAR-MAIN", 0.6)
    sh.bar_run(Pm2(100, 88), Pm2(4900, 88), 150, sc2, "S-REBAR-MAIN", 0.6)
    sh.dim_h(Pm2(1900, 0), Pm2(3100, 0), Pm2(0, -500)[1], sc2)
    sh.dim_h(Pm2(2300, 3300), Pm2(2700, 3300), Pm2(0, 3800)[1], sc2)
    sh.pline([Pm2(2500, 4600), Pm2(2500, 3400)], "S-BLAST")
    sh.pline([Pm2(2380, 3700), Pm2(2500, 3400), Pm2(2620, 3700)], "S-BLAST")
    sh.text("HW3 LINE LOAD 505 kN/m (two-way) / 822 kN/m (one-way bound)",
            Pm2(-400, 4800), TXT["small"], "S-BLAST")
    V.balloon(sh, (420, 400), "S16", Pm2(2350, 813))
    sh.view_title((330, 552), "V2", "BAND BENEATH HEADHOUSE WALL HW3", "SCALE 1:25")

    y = sh.panel(30, 214, 300, "JUNCTION AND ANCHORAGE RULES", [
        "1  500 x 500 HAUNCH WITH T20 @ 150 DIAGONALS at every wall/roof and",
        "   wall/mat junction of the box.  300 x 300 with T16 @ 150 at the",
        "   headhouse - R-701.",
        "2  SLAB TOP STEEL IS CONTINUOUS OVER EVERY SUPPORT and is anchored",
        "   Ld = 1000 (T25) into the wall, measured from the support face.",
        "3  WALL VERTICALS CONTINUE INTO THE SLAB and terminate 75 below the",
        "   slab top - an anchorage of 825 against Ld = 640 required for T16.",
        "4  THE HAUNCH IS A LOAD-PATH ELEMENT, not a fillet.  It reduces the",
        "   shear span and controls cracking at the re-entrant corner of the box.",
        "5  NO REINFORCEMENT IS STOPPED AT A JUNCTION AND NO JUNCTION CONTAINS",
        "   A MOVEMENT JOINT.",
    ], TXT["small"], 3.05)
    V.bbs_extract(sh, 30, y - 8, ["S01A", "S03A", "W01", "W06", "S16"])
    V.loading_panel(sh, 340, 300, 298, [
        "The pressure slab spans ONE-WAY in Y over 5000 clear.  HW3 runs IN the Y",
        "direction, so its load is carried by a slab strip acting as a beam.",
        "  b_eff = 0.400 + 2 x 1.05 (45 deg spread through the 900 slab) = 2.5 m",
        "  [ASSUMED - master K.2 item A11]",
        "",
        "CASE 1 - two-way roof distribution (IS 456 Cl. 24.5, correct)",
        "  line load 476 (trapezoid) + 29 (self)        =  505 kN/m",
        "  equivalent UDL = 505/2.5 + 22.5 + 2.0        =  226 kPa",
        "  M = w Ln2 / 16                               =  354 kNm/m",
        "  against the slab's 1362 kNm/m capacity       =  26 %   OK",
        "",
        "CASE 2 - one-way roof bound",
        "  line load 793 + 29 = 822 kN/m  ->  353 kPa   ->  M = 552 kNm/m = 41 %  OK",
        "",
        "ADOPTED  NO SLAB CHANGE.  DETAILED AS A LINE LOAD, NOT AS A SUPPORT.",
        "ROBUSTNESS  4 No. T25 ADDITIONAL TOP AND BOTTOM IN A 1200 BAND BENEATH",
        "HW3, LAPPED 1250 (50 phi) INTO THE MAIN MESH.",
        "",
        "HW1 and HW2 sit directly over the box perimeter walls; HW4 sits over W7",
        "(M1 made these align exactly).  HW3 IS THE ONLY HEADHOUSE WALL WITH",
        "NOTHING UNDER IT.",
    ], TXT["small"], 3.05, heading="HW3 - THE WALL THAT HAS NOTHING UNDER IT")
    sh.titleblock(scale="1:10, 1:25", sheet_of="16 OF 30")
    return sh.save(os.path.join(OUT, "R-304_Roof_Wall_Junction_Details.dxf"))


def build():
    os.makedirs(OUT, exist_ok=True)
    return [r301(), r302(), r303(), r304()]


if __name__ == "__main__":
    for f in build():
        print("written", f)
