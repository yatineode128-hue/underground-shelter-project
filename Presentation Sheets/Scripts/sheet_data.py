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
# SR1A, by instruction: the "STRUCTURAL - PHASE 2 REV A + M1" revision line is
# DELETED from the identity block -- not edited, removed entirely.  The four
# site-description lines are unchanged.  See master Part H.41.
IDENTITY = [
    "UNDERGROUND CBRN-HARDENED",
    "BLAST-RESISTANT PROTECTIVE",
    "STRUCTURE + SENTRY POST",
    "PUNE, MAHARASHTRA",
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
    "Cl. 10.4 BOUNDARY ELEMENTS ARE NOT TRIGGERED - SEE MASTER PART A.7.8.",
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


# =====================================================================  SHEET 14
# HEADHOUSE.  Geometry sc_proj.HH / HH_DOOR / HH_BAND; design master B.7.1,
# B.7.2, B.7.3; detailing master F.3; loads A.7.5.  Bar marks H01A..H10 are read
# from rebar_data.py by headhouse_marks() -- nothing here re-types a bar.
def headhouse_marks():
    return _rows("HEADHOUSE")


def entrance_marks():
    return _rows("ENTRANCE / ENTRY STAIRWELL")


NOTES_14 = [
    "ALL DIMENSIONS ARE IN MM. ALL LEVELS ARE IN METRES RELATIVE TO FINISHED "
    "SITE GRADE 0.000, NEGATIVE DOWNWARDS.",
    "WRITTEN DIM TO BE FOLLOWED ONLY. DRG NOT TO BE SCALED.",
    "THIS DRG IS TO BE READ IN CONJUNCTION WITH ALL RELEVANT ARCH AND STR DRGS.",
    "CONCRETE M35, w/c NOT MORE THAN 0.45. REINFORCEMENT Fe500D TO IS 1786:2008. "
    "Ld 40 PHI, LAPS 50 PHI, ALL STAGGERED SO THAT NOT MORE THAN 50 % ARE "
    "SPLICED AT ONE SECTION.",
    "MAX BAR SPACING 150 IN BOTH CURTAINS - THIS IS AN EMP REQUIREMENT AND IS "
    "STRICTER THAN IS 456 Cl. 26.3.3.",
    "THE HEADHOUSE ROOF IS FLUSH WITH THE BERM CREST AT (+)0.900 AND CARRIES NO "
    "EARTH COVER. IT IS LOADED AT 396.5 kPa = 383 BLAST + 12.5 SELF + 1.0 SIDL.",
    "THE FOUR WALLS ARE REINFORCED SYMMETRICALLY FOR 383 kPa ACTING ON EITHER "
    "FACE - SEE THE CONSTRUCTION REQUIREMENTS PANEL. THIS IS A STATED "
    "REQUIREMENT, NOT AN ACCIDENT OF DETAILING.",
    "THE HEADHOUSE FLOOR IS THE TOP OF THE 900 PRESSURE SLAB AT (-)2.000. WALL "
    "STARTERS H10 ARE CAST WITH THAT SLAB - SEE SHEET 06.",
    "CONTRACTOR TO CHECK AND VERIFY THE DRG BEFORE EXECUTION.",
]

ELEMENT_ROWS_14 = [
    ["ROOF - END 1200 EACH SIDE", "500", "75", "415",
     "T20 @ 150 EF EW   (2094 mm2/m)", "T12 4L @ 175"],
    ["ROOF - MID ZONE", "500", "75", "415", "T20 @ 150 EF EW", "T12 4L @ 250"],
    ["WALLS HW1 - HW4", "400", "50 / 40", "342",
     "T16 @ 150 EF EW   (1340 mm2/m)", "T12 4L @ 250 THROUGHOUT"],
    ["DOOR JAMBS, HW2", "-", "40", "-",
     "2-T20 EACH JAMB, EACH FACE, Ld 800 BEYOND", "-"],
    ["DOOR-HEAD EDGE BAND", "400 x 800", "40", "742",
     "4-T20 TOP + 4-T20 BOTTOM", "T12 4L @ 150"],
    ["WALL / ROOF HAUNCH", "300 x 300", "-", "-", "DIAGONAL T16 @ 150", "-"],
    "THE WALLS ARE SYMMETRICAL FOR 383 kPa EITHER FACE.  ROOF SPANS 4000 CLEAR, WALLS 2400 CLEAR",
]

HH_CHECK = [
    ["ROOF 500 - ONE-WAY STRIP", "w Ln2 / 16", "396.5 kNm/m", "1879 mm2/m",
     "2094  (T20 @ 150 EF EW)", "90 %  *** ADOPTED ***"],
    ["ROOF 500 - IS 456 TABLE 26", "CASE 1, alpha x- 0.045", "285.5 kNm/m", "-",
     "as above", "65 %"],
    ["ROOF 500 - YIELD LINE", "FIXED 4 EDGES, ISOTROPIC", "162.2 kNm/m", "-",
     "as above", "37 %"],
    ["WALLS 400", "w Ln2 / 16 AT 383 kPa", "137.9 kNm/m",
     "766 ; Cl. 32.5(b) min 800", "1340  (T16 @ 150 EF EW)", "59 %"],
    "SHEAR - tau_c IS READ AT THE STATIC M35 VALUE.  IS 4991 Cl. 10.3.1.1 FORBIDS A DYNAMIC INCREASE ON SHEAR",
    ["ROOF SHEAR AT d", "V 628.4 kN/m", "tau_v 1.514", "tau_c 0.502",
     "T12 4L @ 175 / 250", "LINKS MANDATORY"],
    ["WALL SHEAR AT d", "V 328.6 kN/m", "tau_v 0.961", "tau_c 0.444",
     "T12 4L @ 250", "Cl. 26.5.1.5 256 GOVERNS"],
]

PANEL_14 = [
    "1  THE WALLS ARE REINFORCED SYMMETRICALLY FOR 383 kPa ACTING EITHER FACE.  The inner security",
    "   door is NOT blast rated and the entry stairwell is expected to be lost, so the headhouse",
    "   FILLS and the walls are pushed OUTWARDS.  A stated requirement, not an accident of detailing.",
    "2  HW3 HAS NO WALL UNDER IT.  It is carried as a LINE LOAD on the pressure slab, not as a",
    "   support - 26 % (two-way) / 41 % (one-way bound).  Robustness band: 4 No. T25 ADDITIONAL top",
    "   and bottom over a 1200 width beneath HW3, lapped 1250 (50 phi) - mark S16, SHEET 06.",
    "3  ROOF SHEAR LINKS ARE MANDATORY AND WERE NOT IN THE PHASE 1 REPORT.  tau_v 1.514 > tau_c",
    "   0.502, tau_c read at the STATIC M35 value because IS 4991 Cl. 10.3.1.1 forbids any dynamic",
    "   increase on shear.  T12 4-legged at 175 over the end 1200 each side, at 250 elsewhere.",
    "4  ONLY 300 mm OF WALL SITS ABOVE THE DOOR - too shallow for a lintel.  Door head (-)2.000 +",
    "   2.100 = (+)0.100; roof soffit (+)0.400.  The 300 wall and the 500 roof act TOGETHER as an",
    "   800 deep edge band, 4-T20 top + 4-T20 bottom, over the opening and 600 each side.",
    "5  THE DOOR FRAME IS CAST IN AND WELDED TO THE CAGE (EMP), even though the leaf is a security",
    "   door and is not blast rated.",
    "6  HAUNCH 300 x 300 AT ALL FOUR WALL / ROOF JUNCTIONS, diagonal T16 @ 150.  Top steel is",
    "   continuous over every support, anchored Ld 800 into the wall.  No opening occurs in the",
    "   headhouse roof - the stair void is in the FLOOR, not the roof.",
]

# =====================================================================  SHEET 15
# ENTRY (APPROACH) STAIRWELL.  Geometry sc_proj.ASW; design master B.6;
# detailing master F.2; loads A.7.6.  Bar marks E01..E12 from rebar_data.py.
NOTES_15 = [
    "ALL DIMENSIONS ARE IN MM. ALL LEVELS ARE IN METRES RELATIVE TO FINISHED "
    "SITE GRADE 0.000, NEGATIVE DOWNWARDS.",
    "WRITTEN DIM TO BE FOLLOWED ONLY. DRG NOT TO BE SCALED.",
    "THIS DRG IS TO BE READ IN CONJUNCTION WITH ALL RELEVANT ARCH AND STR DRGS.",
    "CONCRETE M35, w/c NOT MORE THAN 0.45. REINFORCEMENT Fe500D TO IS 1786:2008. "
    "Ld 40 PHI, LAPS 50 PHI, ALL STAGGERED SO THAT NOT MORE THAN 50 % ARE "
    "SPLICED AT ONE SECTION.",
    "*** THIS STRUCTURE IS OUTSIDE THE PROTECTIVE BOUNDARY AND IS NOT BLAST "
    "RATED (REV F DRAWING NOTE 8). IT IS EXPECTED TO BE LOST IN THE DESIGN "
    "EVENT. IT IS DESIGNED TO IS 456 WITH NORMAL PARTIAL FACTORS, NOT WITH "
    "IS 4991 DYNAMIC STRENGTHS. ***",
    "THE 150 EMP BAR-SPACING RULE DOES NOT APPLY HERE. IT IS A REQUIREMENT OF "
    "THE PROTECTIVE ENVELOPE, AND THIS STRUCTURE IS OUTSIDE IT; SPACING IS 200.",
    "THE OPENING CORNER AT THE TOP OF THE FLIGHT IS DETAILED TO SP 34:1987 "
    "Cl. 5.5 - MAIN BARS ARE NOT BENT ROUND IT. SEE DETAIL 3 AND THE "
    "CONSTRUCTION REQUIREMENTS PANEL.",
    "MOVEMENT JOINT WHERE THE STEPPED RAFT MEETS THE HEADHOUSE. THE RAFT BEARS "
    "ON COMPACTED FILL AND THE HEADHOUSE BEARS ON THE PRESSURE SLAB - THEY MUST "
    "NOT BE CAST MONOLITHIC.",
    "CONTRACTOR TO CHECK AND VERIFY THE DRG BEFORE EXECUTION.",
]

ELEMENT_ROWS_15 = [
    ["FLIGHT, WAIST 250", "250", "30", "214", "T16 @ 200  (1005)", "T10 @ 200",
     "T16 @ 200, 1200 INTO THE FLIGHT"],
    ["TOP LANDING   0.000", "250", "30", "214", "T12 @ 200 EF EW  (565)", "-", "-"],
    ["PLATFORM   (-)2.000", "250", "30", "214", "T12 @ 200 EF EW", "-", "ON FILL"],
    ["SIDE WALLS", "250", "50", "194", "T12 @ 200 EF EW", "-",
     "MIN STEEL GOVERNS"],
    ["RAKING ROOF", "250", "30", "204", "T12 @ 200 EF EW", "-",
     "MIN STEEL GOVERNS"],
    ["HEADWALL", "250", "30", "214", "T12 @ 200 EF EW", "-", "-"],
    ["DOOR LINTEL  1000 CLEAR", "250 x 350", "30", "306", "3-T12 T + 3-T12 B",
     "T8 @ 150", "-"],
    ["STEPPED RAFT", "300", "50", "244", "T12 @ 200 EF EW", "-",
     "ON COMPACTED FILL"],
    "OUTSIDE THE PROTECTIVE BOUNDARY.  NOT BLAST RATED.  DESIGNED TO IS 456, NOT TO IS 4991",
]

ASW_CHECK = [
    ["FLIGHT, WAIST 250", "wu 22.85 kPa", "Leff 4800 (Cl. 33.1(b))",
     "M 65.8 kNm/m", "Ast,req 744", "T16 @ 200  (1005)", "75 %"],
    ["SIDE WALLS 250", "34 kPa AT BASE", "RETAINED 2.9 m, PROPPED",
     "M 14.0 kNm/m", "168 ; min 500", "T12 @ 200 EF EW  (565)", "31 %"],
    ["RAKING ROOF 250", "wu 50.5 kPa", "1500 CLEAR", "M 9.5 kNm/m",
     "108 ; min 300", "T12 @ 200 EF EW", "20 %"],
    ["TOP LANDING 250", "wu 54.9 kPa", "Leff 1750", "M 21.0 kNm/m",
     "Ast,req 229", "T12 @ 200 EF EW  (565)", "41 %"],
    "THE RAKING ROOF CARRIES A 20 kPa IMPOSED LOAD, DELIBERATELY, FOR A STRAY VEHICLE ON THE BERM",
    "FLIGHT DEFLECTION  4800/214 = 22.4 ; basic 20 ; fs 215 ; pt 0.470 % ; MF about 1.5 -> 30.  SHEAR tau_v 0.256 < tau_c 0.484 x k 1.10 - NO LINKS",
]

PANEL_15 = [
    "1  THIS STRUCTURE IS OUTSIDE THE PROTECTIVE BOUNDARY AND IS NOT BLAST RATED.  It is expected",
    "   to be LOST in the design event.  Designed to IS 456 with normal partial factors - NOT with",
    "   IS 4991 dynamic strengths.  The blast boundary is the headhouse wall HW2 and its door.",
    "2  THE OPENING CORNER AT THE TOP OF THE FLIGHT IS THE DETAIL MOST OFTEN GOT WRONG.  There the",
    "   tension face turns through 209 deg, and a bar bent round that corner has its bend resultant",
    "   directed OUT of the concrete: it spalls the cover and the bar loses its anchorage.",
    "   *** MAIN BARS SHALL NOT BE BENT ROUND IT. ***  Each layer runs STRAIGHT, CROSSED, anchored",
    "   Ld = 640 into the OPPOSITE face, with a U-bar T16 @ 200 (mark E12) across the corner.",
    "   SP 34:1987 Cl. 5.5.  At the FOOT of the flight the corner CLOSES at 151 deg - bars turn",
    "   normally there.",
    "3  MOVEMENT JOINT WHERE THE STEPPED RAFT MEETS THE HEADHOUSE.  The raft bears on compacted",
    "   fill, the headhouse on the pressure slab.  Different supports, different settlement - they",
    "   must NOT be cast monolithic.",
    "4  300 mm CHANNEL AND GRATING THE FULL 1500 WIDTH at the door (X 8950 - 9250), and a 1.0 m3",
    "   external sump at the platform with its own soakaway.  The stairwell has no gravity outfall",
    "   to the shelter drainage and must not be allowed to discharge into it.",
    "5  BERM GRADED 1.5 : 1 AGAINST THE WALLS TO (+)0.900, toe at grade over 1350.  The 20 kPa roof",
    "   imposed load is what covers a stray vehicle on that berm.",
]
