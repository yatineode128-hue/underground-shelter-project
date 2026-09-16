"""
sheet_data.py  --  every value that STR006 and STR007 draw or print.

ONE definition of each value, so the two sheets cannot disagree with each other
and neither can disagree with the project.

SOURCES, in order of authority
    master/MASTER_PROJECT_STATE.md   Parts A.3, A.4, A.5, A.6, A.7.3, A.7.8,
                                     B.1, B.3, B.4, B.4.1, B.5, F.1, F.2
    Structural CAD/Scripts/sc_proj.py      the reconciled geometric constants
    Structural CAD/Scripts/rebar_data.py   THE bar-mark register - every mark
                                           printed on these two sheets is read
                                           straight out of it, so a mark cannot
                                           appear here without a schedule entry.

MAIN STAIRCASE IS FROZEN: 24R @ 170.8333 / 280, 3 flights x 8, total rise 4100.
Nothing in this file changes it; the values are read from sc_proj.STAIR.
"""
import sc_proj as P
import rebar_data as RD

# ------------------------------------------------------------------- identity
IDENTITY = [
    "UNDERGROUND CBRN-HARDENED",
    "BLAST-RESISTANT PROTECTIVE",
    "STRUCTURE + SENTRY POST",
    "PUNE, MAHARASHTRA",
    "STRUCTURAL - PHASE 2 REV A + M1",
]

# --------------------------------------------------------------- box geometry
PARTITION_X = P.PARTITIONS                       # four 110 partitions
IW = P.IW                                        # W5 200, W6 400, W7 400
ESC = [(nm, cx, cy) for nm, cx, cy in P.ESC]     # ESC 1 / ESC 2, post-M1
SUMP = (11070, 900, 12570, 2400)                 # 1500 x 1500, Bay 5 [CONFIRMED, S-06]

# bottom dimension chain, chosen so that no two dimension texts can touch at 1:100
BAY_CHAIN = [0, 600, 3500, 5520, 9130, 11040, 12800, 15200, 18400, 21400, 22000]

# walls cut by a longitudinal section at Y 2050
WALLS_UNDER_ROOF = [(0, 600), (12600, 12800), (14800, 15200),
                    (18000, 18400), (21400, 22000)]
WALLS_ON_MAT = WALLS_UNDER_ROOF

# engineered cover build-up, from the top -- master A.7.3, 2000 total, 40.65 kPa
COVER_LAYERS = [(300, "TOPSOIL / TURF"),
                (150, "GRANULAR FILTER"),
                (200, "RC BURSTER SLAB M30"),
                (500, "CRUSHED BASALT RUBBLE 25-75"),
                (750, "COMPACTED ENGINEERED FILL"),
                (100, "PROTECTION SCREED")]

# ------------------------------------------------------- bar-mark table rows
def _rows(group, prefix=None):
    out = []
    for m in RD.MARKS:
        if m["group"] != group:
            continue
        if prefix and not m["mark"].startswith(prefix):
            continue
        out.append([m["mark"], f"T{m['phi']}",
                    str(m["spacing"]) if m["spacing"] else "-",
                    m["location"], f"{m['cut']:.0f}", str(m["count"])])
    return out


def roof_marks():
    return _rows("ROOF SLAB")


def mat_marks():
    return _rows("FOUNDATIONS")


def wall_marks():
    """The 600 perimeter shear walls W1-W4 only -- marks W01 to W06."""
    keep = {"W01", "W02", "W03", "W04", "W05", "W06"}
    return [r for r in _rows("WALLS") if r[0] in keep]


def stair_marks():
    return _rows("MAIN STAIRCASE")


# =====================================================================  SHEET 06
NOTES_06 = [
    "ALL DIMENSIONS ARE IN MM. ALL LEVELS ARE IN METRES RELATIVE TO FINISHED "
    "SITE GRADE 0.000, NEGATIVE DOWNWARDS.",
    "WRITTEN DIM TO BE FOLLOWED ONLY. DRG NOT TO BE SCALED.",
    "THIS DRG IS TO BE READ IN CONJUNCTION WITH ALL RELEVANT ARCH AND STR DRGS.",
    "CONCRETE M35, w/c NOT MORE THAN 0.45. REINFORCEMENT Fe500D TO IS 1786:2008. "
    "Ld 40 PHI, LAPS 50 PHI, ALL STAGGERED SO THAT NOT MORE THAN 50 % ARE "
    "SPLICED AT ONE SECTION.",
    "MAX BAR SPACING 150 IN BOTH CURTAINS - THIS IS AN EMP REQUIREMENT AND IS "
    "STRICTER THAN IS 456 Cl. 26.3.3.",
    "DESIGN IS TO IS 456:2000 WITH IS 4991:1968 BLAST ACTIONS AND IS 3370 (Pt 2) "
    "CRACK CONTROL; SEISMIC TO IS 1893 (Pt 1):2016. IS 13920:2016 IS CHECKED: "
    "Cl. 10.4 BOUNDARY ELEMENTS ARE NOT TRIGGERED - SEE THE DESIGN BASIS PANEL.",
    "CONTRACTOR TO CHECK AND VERIFY THE DRG BEFORE EXECUTION.",
]

ELEMENT_ROWS_06 = [
    ["ROOF SLAB - MIDSPAN", "900", "75", "812.5",
     "T25 @ 150 EF EW   (3272 mm2/m)", "T12 4L @ 250, END 1500 EACH SIDE"],
    ["ROOF SLAB - MID ZONE", "900", "75", "812.5",
     "T25 @ 150 EF EW", "T12 2L @ 300"],
    ["ROOF - CANTILEVER PAD", "900", "75", "812.5",
     "T25 @ 150 TOP, CONTINUOUS", "T12 4L @ 250 THROUGHOUT"],
    ["ROOF - 1200 THICKENINGS", "1200", "75", "-",
     "6-T25 TOP + 6-T25 BOTTOM", "T12 CLOSED @ 150"],
    ["MAT FOUNDATION", "600", "75 / 50", "517",
     "T16 @ 150 EF EW   (1340 mm2/m)", "T12 ON A 250 x 250 GRID"],
    ["SUMP PIT WALLS / BASE", "300 / 400", "50", "244",
     "T16 @ 150 EF EW", "-"],
]

PANEL_06 = [
    "1  THE HAZARD IS NOT THE BASALT - IT IS THE FLOW CONTACTS.  OVER-EXCAVATE ANY RED-BOLE OR VESICULAR SEAM AT FOUNDING LEVEL AND REPLACE WITH M15 LEAN",
    "   CONCRETE.  A single seam under the mat produces the 3.0 m differential-support case that SIZES the mat.  This is a requirement, not an option.",
    "2  100 mm M15 BLINDING TO (-)6.800 before any reinforcement is placed; tanking membrane on the blinding with a protection screed.  75 mm cover to the",
    "   blinding on CEMENTITIOUS spacers - no plastic spacer against an earth or blinding face.  Chairs at not more than 1000 c/c both ways to the top curtain.",
    "3  THE T12 LINK GRID F05 IS STRUCTURAL AND IS ALSO THE CURTAIN SPACER SYSTEM - it is not optional.  CONSTRUCTION JOINTS AT APPROXIMATELY 6 m WITH THE",
    "   REINFORCEMENT FULLY CONTINUOUS; two waterstops and a welded Cu / galvanised EMP strap at every joint.",
    "4  FLOTATION GOVERNS THE CONSTRUCTION STAGE, NOT THE FINISHED STRUCTURE.  FoS is 0.33 with the mat alone and 1.22 with the box complete and no backfill.",
    "   Continuous dewatering from the start of excavation until backfill and cover are complete; 6 No. temporary pressure-relief plugs in the mat, grouted",
    "   up ONLY after backfill; backfill SYMMETRICALLY in layers.   NO BAR MAY BE DISPLACED TO CLEAR A SERVICE - any clash is an RFI.",
]

BASIS_06 = [
    "GOVERNING COMBINATION   COMB 103 BLAST,  w = 448.15 kPa",
    "   383.00 blast (344.7 x 1.111 DLF) + 40.65 engineered cover + 2.00 SIDL + 22.50 self weight.",
    "   NO LIVE LOAD ON THE ROOF AT BLAST - IS 4991 Cl. 11.2.   Static ULS 101 = 127.7 kPa, so blast governs 3.51 : 1.",
    "",
    "ONE-WAY ACTION IS NOT A CHOICE, IT IS FORCED",
    "   Aspect 20.8 / 5.0 = 4.2 and IS 456 Table 26 is tabulated only to ly/lx = 2.0, so two-way action cannot be",
    "   claimed.  Mp depends on the 5000 clear width alone - which is why lengthening the box (M1) was structurally",
    "   free, and why widening 5.0 -> 6.0 m would raise the roof moment 44 %.",
    "",
    "ROOF (PRESSURE) SLAB 900   d = 900 - 75 - 12.5 = 812.5",
    "   Mp = w Ln2 / 16 = 448.15 x 25 / 16 = 700.2 kNm/m ;  Mu,lim = 3841 kNm/m ;  Ast,req = 1632 mm2/m",
    "   PROVIDED T25 @ 150 EF EW = 3272 mm2/m  ->  Mu 1362.4 kNm/m,  UTILISATION 51 %,  xu/d = 0.139 << 0.46",
    "   SHEAR  V at d = 756.3 kN/m ; tv 0.931 ; tc 0.450 ; tc,max 3.70  ->  T12 4L @ 250 end 1500, T12 2L @ 300 mid",
    "   NATURAL PERIOD  f1 = 74.9 Hz, T = 13.4 ms, td/T = 10 to 100  ->  QUASI-STATIC.  This is what licenses a",
    "   static analysis at all.",
    "",
    "CANTILEVER PAD 1840 (FINDING F2)   M(root) = 448.15 x 1.8402 / 2 = 758.6 kNm/m  -  MORE THAN THE MIDSPAN Mp",
    "   Ast,req TOP 1772 mm2/m < 3272 provided  ->  56 %.   V(root) 824.6 kN/m  ->  T12 4L @ 250 throughout the pad.",
    "",
    "MAT FOUNDATION 600   d = 600 - 75 - 8 = 517",
    "   CASE 1 net uplift 31.1 kPa over 5000  ->  Mp 48.6 kNm/m, nominal.",
    "   CASE 2 *** GOVERNS *** a 3.0 m red-bole band removed at the worst position, q = 404.9 kPa blast bearing",
    "   M = q L2 / 12 = 303.7 kNm/m ;  Ast,req 1115 mm2/m",
    "   PROVIDED T16 @ 150 EF EW = 1340 mm2/m  ->  Mu 362.8 kNm/m,  UTILISATION 84 %",
    "   ONE-WAY SHEAR  V at d = 398.0 kN/m ; tv 0.770 ; tc 0.375  ->  T12 closed links on a 250 x 250 grid",
    "   BEARING 404.9 kPa on a presumptive 3240 kPa (IS 1904 hard rock) = 12.5 %.  BEARING GOVERNS NOTHING.",
    "   PUNCHING IS 456 Cl. 31.6 NOT APPLICABLE - nothing bears on the mat; the headhouse walls bear on the ROOF.",
    "",
    "OPENINGS   2 No. 1400 dia escape shafts, collar 250 RC, slab thickened 900 -> 1200 over a 600 annulus.",
    "   Circular is the right shape: hoop action and NO re-entrant stress concentration.  This detail sets the",
    "   750 mm clearance rule, which is why a bay must be at least 2900 wide to hold an escape shaft.",
    "   1 No. 2800 x 3160 rectangular stair void - both re-entrant corners trimmed with S15 at 45 degrees.",
    "",
    "OPEN ITEMS AFFECTING THIS SHEET   A2 design GWT (-)2.000 is [ASSUMED] and carries two-thirds of the lateral",
    "   load and all of the uplift - monsoon monitoring required.   A4 subgrade modulus ks: the master requires",
    "   BOTH 100 000 and 500 000 kN/m3 and only 100 000 exists in any model.   M1 no STAAD result exists for any",
    "   underground model - every design action above is a hand calculation.   P3 blast capacity is not",
    "   demonstrated; support rotation needs a non-linear SDOF check (IS 4991 Fig. 6 / Biggs) - Phase 3.",
]

# =====================================================================  SHEET 07
NOTES_07 = [
    "ALL DIMENSIONS ARE IN MM. ALL LEVELS ARE IN METRES RELATIVE TO FINISHED "
    "SITE GRADE 0.000, NEGATIVE DOWNWARDS.",
    "WRITTEN DIM TO BE FOLLOWED ONLY. DRG NOT TO BE SCALED.",
    "THIS DRG IS TO BE READ IN CONJUNCTION WITH ALL RELEVANT ARCH AND STR DRGS.",
    "CONCRETE M35, w/c NOT MORE THAN 0.45. REINFORCEMENT Fe500D TO IS 1786:2008. "
    "Ld 40 PHI, LAPS 50 PHI, ALL STAGGERED SO THAT NOT MORE THAN 50 % ARE "
    "SPLICED AT ONE SECTION.",
    "THE 600 WALL IS NOT STRENGTH-GOVERNED (68 %). 600 IS SET BY COVER, "
    "CONGESTION, IS 3370 CRACK CONTROL, THE EMP DOUBLE CURTAIN AT 150 AND THE "
    "1168 kN/m AXIAL PATH.",
    "THE MAIN STAIRCASE IS INSIDE THE PROTECTIVE ENVELOPE AND IS NOT A BLAST "
    "ELEMENT. IT IS DESIGNED TO IS 456 WITH NORMAL PARTIAL FACTORS, NOT WITH "
    "IS 4991 DYNAMIC STRENGTHS.",
    "IS 13920:2016 HAS BEEN CHECKED FOR THE BOX: Cl. 10.4 BOUNDARY ELEMENTS ARE "
    "NOT TRIGGERED (WALL SHEAR 0.063 N/mm2) AND NO DUCTILE-DETAILING CLAUSE "
    "GOVERNS ANY BAR ON THIS SHEET.",
    "CONTRACTOR TO CHECK AND VERIFY THE DRG BEFORE EXECUTION.",
]

WALL_SCHEDULE_ROWS = [
    ["W1  SOUTH PERIMETER", "600", "22000", "75/50/40", "517",
     "T16 @ 150 EF EW", "T12 CLOSED @ 200"],
    ["W2  NORTH PERIMETER", "600", "22000", "75/50/40", "517",
     "T16 @ 150 EF EW", "T12 CLOSED @ 200"],
    ["W3  WEST END", "600", "6200", "75/50/40", "517",
     "T16 @ 150 EF EW", "T12 CLOSED @ 200"],
    ["W4  EAST END", "600", "6200", "75/50/40", "517",
     "T16 @ 150 EF EW", "T12 CLOSED @ 200"],
    "ALL FOUR 600 WALLS:  xu/d = 0.089,  UTILISATION 68 %,  BLAST GOVERNS 4.6 : 1",
    "OTHER WALLS - SCHEDULED HERE, DETAILED ELSEWHERE, NOT DRAWN ON THIS SHEET",
    ["W5  BAY 5 / 6", "200", "5000", "40", "154",
     "T12 @ 150 EF EW", "-  NOMINAL"],
    ["W6  BAY 6 / 7  (M1)", "400", "5000", "50/40", "342",
     "T20 @ 150 EF EW", "T12 4L @ 200"],
    ["W7  BAY 7 / 8  (M1)", "400", "5000", "50/40", "342",
     "T20 @ 150 EF EW", "T12 4L @ 200"],
    ["W8  PARTITIONS x 4", "110", "5000", "25", "-",
     "A252 MESH B/F", "-  NON-STRUCTURAL"],
]

STAIR_SCHEDULE = [
    ["FLIGHTS 1, 2, 3  (WAIST)", "200", "164",
     "T12 @ 150  (754)", "T10 @ 200", "T12 @ 150, 800 IN"],
    ["LANDING L1   (-)4.7333", "200", "164",
     "T12 @ 125 BTM  (905)", "T10 @ 200", "T12 @ 125, 900 EACH END"],
    ["LANDING L2   (-)3.3667", "200", "164",
     "T12 @ 125 BTM  (905)", "T10 @ 200", "T12 @ 125, 900 EACH END"],
    ["ARRIVAL LANDING (-)6.100", "-", "-",
     "= THE MAT SURFACE", "-", "NO SEPARATE SLAB"],
]

NBC_CHECK = [
    ["RISER", "170.8333 mm", "NOT MORE THAN 190", "PASS"],
    ["TREAD / GOING", "280 mm", "NOT LESS THAN 250", "PASS"],
    ["FLIGHT WIDTH", "1200 mm", "NOT LESS THAN 1000", "PASS - STRETCHER CAPABLE"],
    ["RISERS PER FLIGHT", "8", "12 PREFERRED MAX", "PASS"],
    ["HEADROOM", "2533 mm", "NOT LESS THAN 2200", "PASS"],
    ["TOTAL RISE", "4100 = 24 x 170.8333", "(-)6.100 TO (-)2.000", "CLOSES EXACTLY"],
]

FROZEN_07 = [
    "24 RISERS at 170.8333  |  TREAD 280  |  3 FLIGHTS x 8 RISERS  |  TOTAL RISE 4100",
    "FLIGHT WIDTH 1200  |  WELL 200  |  WAIST 200  |  HEADROOM 2533",
    "LANDING L1 (-)4.7333   L2 (-)3.3667   ARRIVAL (-)6.100 = THE MAT SURFACE",
    "TOTAL RISE CLOSES EXACTLY:  (-)6.100 TO (-)2.000 = 4100 = 24 x 170.8333",
    "NO RISER, TREAD, LANDING LEVEL, FLIGHT WIDTH, WELL OR HEADROOM ON THIS SHEET",
    "MAY BE ALTERED.  ANY CHANGE IS A NEW INSTRUCTION, NOT A DETAILING DECISION.",
]

PANEL_07 = [
    "1  WALL STARTERS F07: T16 @ 150 EACH FACE WITH A 900 mm HORIZONTAL LEG",
    "   INTO THE MAT, lapped 800 (50 phi) above a 150 kicker.  The starter, not",
    "   the wall bar, is what makes the mat / wall joint work.",
    "2  HAUNCHES 500 x 500 AT EVERY WALL / ROOF AND WALL / MAT JUNCTION, with",
    "   diagonal T20 @ 150 (mark W06).",
    "3  TWO WATERSTOPS AND A WELDED Cu / GALVANISED EMP STRAP AT EVERY",
    "   CONSTRUCTION JOINT (approximately 6 m centres).  Reinforcement is FULLY",
    "   CONTINUOUS through the joint - it is not a movement joint.",
    "4  COVER: 75 mm to a face cast against the blinding or trimmed rock; 50 mm",
    "   to a formed earth face; 40 mm internally; 30 mm in the stair shaft.",
    "   The 5 mm reduction IS 456 Table 16 permits for M35 and above is",
    "   DELIBERATELY NOT TAKEN.",
    "5  MAX BAR SPACING 150 IN BOTH CURTAINS - AN EMP REQUIREMENT, STRICTER",
    "   THAN IS 456 Cl. 26.3.3.  No bar may be displaced to clear a service;",
    "   any clash is an RFI.",
    "6  THE MAIN STAIRCASE IS DESIGNED TO IS 456 WITH NORMAL PARTIAL FACTORS.",
    "   It is inside the protective envelope and is NOT a blast element.",
    "7  STAIR FINISHES AND THE 1100 GUARDING TO THE VOID FREE EDGE (NBC 2016",
    "   Pt 4) ARE NOT SHOWN ON THIS SHEET - see the architectural package.",
]

BASIS_07 = [
    "600 PERIMETER SHEAR WALLS W1 - W4        d = 600 - 75 - 8 = 517",
    "   Blast 383 kPa (Ka 1.0) against static earth + water 83.2 kPa at",
    "   the base   ->   BLAST GOVERNS 4.6 : 1",
    "   Mp = w Ln2 / 16 = 383 x 3.2002 / 16            =  245.1 kNm/m",
    "   Mu,lim = 0.133 fck,dyn b d2                    =  1556 kNm/m  OK",
    "   Ast,req (fy,dyn 625, fck,dyn 43.75)            =  894 mm2/m",
    "   MINIMUM STEEL, ALL THREE CHECKED:",
    "     IS 456 Cl. 32.5(a) vertical 0.0012 x 600     =  720 mm2/m",
    "     IS 456 Cl. 32.5(b) horizontal 0.0020 x 600   =  1200 mm2/m",
    "     IS 3370 Pt 2 surface zone 0.35 % x 250/face  =  875 mm2/m/face",
    "   PROVIDED  T16 @ 150 EF EW = 1340 mm2/m",
    "     Mu 362.8 kNm/m,  UTILISATION 68 %,  xu/d = 0.089 << 0.46",
    "   SHEAR  V at d = 383 (1.600 - 0.517)            =  414.8 kN/m",
    "     tv 0.802 | tc 0.375 (pt 0.259 %) | tc,max 3.70  OK",
    "     Vus 220.8 kN/m ;  Asv/sv 0.982 ;  Cl. 26.5.1.5 limit 300",
    "     PROVIDED  T12 CLOSED LINKS @ 200   (Asv/sv 1.131)",
    "   AXIAL  N = 1168 kN/m ;  f 1.95 N/mm2 = 11 % of 0.4 fck,dyn",
    "     ->  P-M INTERACTION NOT CRITICAL",
    "   CRACK  IS 3370 Pt 2 limit 0.2 mm ; 875 required < 1340 provided",
    "   SEISMIC  Ah 0.075 ; Vb 1050 kN ; 525 kN per long wall",
    "     tau = 0.063 N/mm2, NEGLIGIBLE",
    "     IS 13920 Cl. 10.4 BOUNDARY ELEMENTS ARE NOT TRIGGERED",
    "",
    "WHY 600 - STATED HONESTLY.  The wall is NOT strength-governed at",
    "   68 %.  600 is set by (i) the 75 mm cover, (ii) congestion - two",
    "   curtains plus closed links plus waterstops plus cast-in frames,",
    "   (iii) IS 3370 crack control under sustained hydrostatic load,",
    "   (iv) the EMP double curtain at 150, (v) the 1168 kN/m axial path.",
    "",
    "MAIN STAIRCASE, BAY 7     INSIDE the protective envelope, and NOT a",
    "   blast element.  The shaft pressurises, but that pressure acts on",
    "   the shaft WALLS and on the blast DOORS - not as a net load on a",
    "   slab that is open on both faces.  Designed to IS 456 with normal",
    "   partial factors, NOT with IS 4991 dynamic strengths.",
    "",
    "FLIGHT, WAIST 200    theta = arctan(170.833 / 280) = 31.4 deg",
    "   waist self 5.858 + steps 2.135 (Cl. 33.2) + finishes 1.000",
    "   + live 5.000 = 13.99 kPa   ->   wu = 21.0 kPa",
    "   Leff = going 1960 + 600 + 600 = 3160   (IS 456 Cl. 33.1(b))",
    "   d = 200 - 30 - 6 = 164 ;  M = wu Leff2 / 8 = 26.2 kNm/m",
    "   Ast,req 380 ;  Cl. 26.5.2.1 min 0.12 % x 200 = 240",
    "   PROVIDED  T12 @ 150 (754)  ->  Mu 50.3 kNm/m,  UTILISATION 52 %",
    "   T10 @ 200 DISTRIBUTION ;  T12 @ 150 TOP, 800 in, Ld 480",
    "   DEFLECTION  Leff/d 19.3 ; fs 146 ; pt 0.46 % ; MF 1.9",
    "     ->  permissible 38 > 19.3",
    "   SHEAR  V 33.2 ; tv 0.202 < tc 0.479 x k 1.20 = 0.575  NO LINKS",
    "",
    "LANDINGS L1 / L2, 200 THK, SPANNING ACROSS THE SHAFT",
    "   self 7.50 + finishes 1.50 + live 7.50 + flight reaction 27.70",
    "   = 44.20 kPa ;  Leff = 2800 clear + 200 bearing = 3000 (Cl. 22.2(a))",
    "   M = 49.7 kNm/m ;  Ast,req 745",
    "   T12 @ 150 would give 754 = 100 % - TOO TIGHT.",
    "   PROVIDED  T12 @ 125 BOTTOM (905)  ->  Mu 59.5,  UTILISATION 84 %",
    "   DEFLECTION 3000 / 164 = 18.3 ; fs 239 ; pt 0.552 % ; MF 1.35 -> 27",
    "   SHEAR  V 66.3 kN/m ; tv 0.404 < tc 0.519 x 1.20 = 0.622",
    "",
    "THE LANDINGS PROP W6 AND W7 AT (-)4.733 AND (-)3.367, BUT ONLY OVER",
    "   THEIR 1200 DEPTH.  The 400 wall design does NOT rely on that prop.",
]
