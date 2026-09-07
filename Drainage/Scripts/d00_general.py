"""
d00_general.py  --  D-001 general notes / legend / design basis
                    D-002 symbols, pipe coding and abbreviations
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

CA, CB, CC = 14.0, 286.0, 558.0          # column origins
WA, WB, WC = 264.0, 264.0, 268.0         # column widths
TOP = 552.0
NOTE, LEAD = 2.4, 4.3


def sheet(num, title, sub, flags=(), of=""):
    return X.Sheet(num, title, sub, package="DRAINAGE",
                   rev=P.REV["drainage"], flags=flags, sheet_of=of)


def sbox(sh, x, y, w, h, lines, layer="P-EQUIP", th=None):
    """A schematic block: box with centred lines of text."""
    sh.rect(x, y - h, x + w, y, layer)
    th = th or T["small"]
    n = len(lines)
    for i, s in enumerate(lines):
        sh.text(s, (x + w / 2.0, y - h / 2.0 + (n - 1) * th * 0.85 / 2.0
                    - i * th * 1.7 + (-th * 0.4)), th, "M-TEXT", "CENTER")


def sarrow(sh, p1, p2, layer="P-FLOW", label=None):
    import math
    sh.line(p1, p2, layer)
    ang = math.degrees(math.atan2(p2[1] - p1[1], p2[0] - p1[0]))
    sh.flow(((p1[0] + p2[0]) / 2 - math.cos(math.radians(ang)) * 1.2,
             (p1[1] + p2[1]) / 2 - math.sin(math.radians(ang)) * 1.2),
            ang, 2.2, layer)
    if label:
        sh.text(label, ((p1[0] + p2[0]) / 2 + 2.0, (p1[1] + p2[1]) / 2),
                T["small"], "M-TEXT", "ML")


# =====================================================================
def d001():
    sh = sheet("D-001", "GENERAL DRAINAGE NOTES, LEGEND AND DESIGN BASIS",
               "TANKED ENVELOPE - THREE SEGREGATED STREAMS - ONE ENVELOPE "
               "PENETRATION",
               flags=("C16", "C18", "A2", "A7", "A8", "DR-C1", "DR-C2",
                      "DR-D1", "DR-D2", "DR-D3", "DR-D4", "DR-F4", "DR-F5"),
               of="1 OF 11")

    # ================================================== column A
    y = sh.panel(CA, TOP, WA, "1   DRAINAGE CONCEPT", [
        "THE STRUCTURE IS A TANKED BOX, NOT A DRAINED ONE.  That single decision",
        "sets the whole strategy, and every sheet in this set obeys four rules.",
        "",
        "1  NOTHING PENETRATES THE ROOF.  The 900 pressure slab carries 2.0 m of",
        "   engineered cover whose second metre is bought for prompt neutron and",
        "   gamma attenuation (master A.7.3).  A rainwater outlet, a vent stack or",
        "   a soil stack through that cover would breach both the radiation mass",
        "   and the roof membrane.  There is no downpipe on the buried roof and",
        "   none is added by this package.",
        "",
        "2  ONE ENVELOPE CROSSING.  Sheet S-06 records the service entry plate as",
        "   'the only penetration of the envelope'.  The sump rising main uses it.",
        "   No second drainage penetration is created.",
        "",
        "3  THREE STREAMS, NEVER COMBINED.  See the schematic below.",
        "",
        "4  DRAINAGE IS NOT IN THE SAFETY PATH.  Rev F drawing 5 note 9 states this",
        "   for the entry stairwell and it is held for the whole system: no",
        "   drainage failure may block egress, breach the envelope or flood an",
        "   entrance.",
    ], h=NOTE, lead=LEAD)

    # ---- drawn schematic
    sh.text("2   SYSTEM SCHEMATIC   -   SOURCE / COLLECTION / CONVEYANCE / DISCHARGE",
            (CA, y - 8), T["panel_head"], "M-TITLE")
    sy = y - 16
    xl, xm, xr = CA + 6, CA + 96, CA + 186
    bw, bh = 76, 17

    sbox(sh, xl, sy, bw, bh, ["RAIN  50 mm/h  [C]", "roofs 41.4 m2 + cover 136.4 m2"],
         "P-DRAIN-STORM")
    sbox(sh, xm, sy, bw, bh, ["GRADE 0.000 CROWNED", "FALLS 1:50 AWAY  [C]"],
         "P-DRAIN-STORM")
    sbox(sh, xr, sy, bw, bh, ["SHEDS AT THE SURFACE", "TO THE BERM TOE"],
         "P-DRAIN-STORM")
    sarrow(sh, (xl + bw, sy - bh / 2), (xm, sy - bh / 2), "P-DRAIN-STORM")
    sarrow(sh, (xm + bw, sy - bh / 2), (xr, sy - bh / 2), "P-DRAIN-STORM")

    sy -= 24
    sh.line((CA + 6, sy + 3), (CA + WA - 6, sy + 3), "M-WATERPROOF")
    sh.text("CONTINUOUS TANKING MEMBRANE  -  R-805  -  THE ENVELOPE",
            (CA + WA / 2, sy + 4.6), T["small"], "M-WATERPROOF", "BC")

    sy -= 8
    sbox(sh, xl, sy, bw, bh, ["SEEPAGE 200 L/d  [C]", "0.5 L/m2/d x 401 m2"],
         "P-DRAIN-SEEP")
    sbox(sh, xm, sy, bw, bh, ["FLOOR FALLS + GULLIES", "1:400 spine, 1:80 / 1:100"],
         "P-DRAIN-WASTE")
    sbox(sh, xr, sy, bw, bh, ["CLEAN SUMP  3.375 m3", "INVERT (-)7.600  [C]"],
         "P-EQUIP")
    sarrow(sh, (xl + bw, sy - bh / 2), (xm, sy - bh / 2), "P-DRAIN-SEEP")
    sarrow(sh, (xm + bw, sy - bh / 2), (xr, sy - bh / 2), "P-DRAIN-WASTE")

    sy -= 22
    sbox(sh, xl, sy, bw, bh, ["CONDENSATE + WASHDOWN", "200 L/d  [C]"],
         "P-DRAIN-WASTE")
    sarrow(sh, (xl + bw / 2, sy), (xl + bw / 2, sy + 7), "P-DRAIN-WASTE")
    sarrow(sh, (xr + bw / 2, sy + 22 - bh), (xr + bw / 2, sy - 3), "P-DRAIN-RISING")
    sbox(sh, xr, sy - 3, bw, bh,
         ["2 x 1.5 L/s + HAND PUMP", "ISOL / NRV / BCV / TRAP"], "P-EQUIP")

    sy -= 26
    sbox(sh, xr, sy, bw, bh, ["DN50 RISING MAIN", "SERVICE ENTRY PLATE"],
         "P-DRAIN-RISING")
    sy -= 22
    sarrow(sh, (xr + bw / 2, sy + 22 - bh), (xr + bw / 2, sy), "P-DRAIN-RISING")
    sbox(sh, xr, sy, bw, bh, ["STORM SOAKAWAY  SK-02", "21.99 m2  [A]  D3 OPEN"],
         "P-EQUIP")

    sbox(sh, xl, sy + 24, bw, bh, ["DECON EFFLUENT  [C]", "airlock stages 1 + 2"],
         "P-DRAIN-EFF")
    sbox(sh, xm, sy + 24, bw, bh, ["1000 L TANK TK-01", "*** ROUTE UNDEFINED ***"],
         "P-DRAIN-EFF")
    sarrow(sh, (xl + bw, sy + 24 - bh / 2), (xm, sy + 24 - bh / 2), "P-DRAIN-EFF")
    sh.text("TANKER ONLY  -  NEVER TO THE CLEAN SUMP",
            (xm + bw + 4, sy + 24 - bh / 2), T["small"], "M-FLAG", "ML")

    sbox(sh, xl, sy, bw, bh, ["FOUL, PEACETIME  [C]", "450 L/d, 10 users"],
         "P-DRAIN-SOIL")
    sbox(sh, xm, sy, bw, bh, ["SEPTIC TANK  1.125 m3", "IS 2470 Pt 1 Table 1"],
         "P-DRAIN-SOIL")
    sarrow(sh, (xl + bw, sy - bh / 2), (xm, sy - bh / 2), "P-DRAIN-SOIL")
    sy -= 22
    sbox(sh, xm, sy, bw, bh, ["SOAK PIT  SK-01", "*** 2.3 % SHORT - DR-C2 ***"],
         "M-FLAG")
    sarrow(sh, (xm + bw / 2, sy + 22 - bh), (xm + bw / 2, sy), "P-DRAIN-SOIL")

    sh.rect(CA, sy - 6, CA + WA, y - 12, "M-TITLE")

    yA = sh.panel(CA, sy - 10, WA, "3   FINAL DISCHARGE", [
        "*** THE FINAL DISCHARGE OF THE WHOLE SITE IS TO GROUND, ON SITE. ***",
        "No municipal sewer connection, no municipal storm connection, no outfall",
        "and no receiving watercourse appears anywhere in the project.  Whether",
        "any is available at this site is OPEN ITEM D3 - DATA REQUIRED.  Every",
        "discharge shown above therefore rests on the PERCOLATION TEST that",
        "master K.2 A7 already makes mandatory (IS 2470 Pt 2 Cl. 4).",
    ], h=NOTE, lead=LEAD)

    # ================================================== column B
    y = sh.panel(CB, TOP, WB, "5   GENERAL NOTES", [
        " 1  ALL DIMENSIONS IN MILLIMETRES.  ALL LEVELS IN METRES RELATIVE TO",
        "    FINISHED SITE GRADE 0.000, NEGATIVE DOWNWARDS.  The coordinate origin",
        "    is the south-west EXTERNAL corner of the underground box at grade",
        "    (master A.4.1);  X east 0-22000, Y north 0-6200.",
        " 2  READ WITH  master/MASTER_PROJECT_STATE.md,  sheet S-06,  the ten Rev F",
        "    architectural drawings, and R-805 waterproofing / structural interface.",
        " 3  DO NOT SCALE.  Work to figured dimensions and to the schedules.",
        " 4  EVERY VALUE ON THIS SET CARRIES AN EVIDENCE CLASS.  Nothing marked",
        "    [A], [U] or [N] may be built from without written confirmation.",
        " 5  THE 600 MAT AND THE 900 ROOF SLAB SHALL NOT BE CUT, CHASED OR CORED",
        "    for drainage.  The one exception requested is BW-01, note 12.",
        " 6  ALL TRAPS INSIDE THE GAS-TIGHT ENVELOPE: 75 mm DEEP SEAL, PRIMED.  An",
        "    evaporated seal is an envelope breach, not a smell.  Trap primers or",
        "    a written weekly priming task are mandatory.",
        " 7  THRESHOLD UPSTANDS 50 mm AT W5 AND AT BLAST DOOR 1.  No water may run",
        "    from the decon airlock or the stair shaft into the clean zone.",
        " 8  DECON EFFLUENT IS SEGREGATED THROUGHOUT and is never connected to the",
        "    clean sump or to any clean drain, anywhere, under any circumstance.",
        " 9  EVERY PIPE CROSSING THE TANK requires a puddle flange welded to the",
        "    sleeve with the membrane dressed and clamped to it - see D-304.",
        "10  RODDING ACCESS at every change of direction and at every gully.",
        "11  NO DRAINAGE ELEMENT IS PLACED IN THE MAIN STAIRCASE - not in the",
        "    flights, not in the well, not on the landings.  Its geometry is frozen.",
        "12  BUILDER'S WORK BW-01 - REQUESTED, NOT ACCEPTED.  PD-01 needs a 300 wide",
        "    recess in the top of the mat, 216 deep at the sump end, leaving 384 of",
        "    the 600 mat locally.  The mat is the most heavily utilised element in",
        "    the project at 84 % (master B.3).  STRUCTURAL ENGINEER TO ACCEPT OR",
        "    REFUSE.  If refused, D-201 note 6 applies and there is no buried drain",
        "    inside the envelope at all.",
    ], h=NOTE, lead=LEAD)

    y = sh.panel(CB, y - 6, WB, "6   TESTING AND COMMISSIONING", [
        "1  All gravity drains: water test before covering, and a rodding test",
        "   over the full length of every run.",
        "2  All rising mains: hydraulic test to 1.5 x the working pressure, held",
        "   for 30 minutes with no measurable drop.",
        "3  Every sleeve and puddle flange through the tank: witnessed by the",
        "   waterproofing installer BEFORE the membrane is dressed to it.  A",
        "   penetration that fails after tanking cannot be reworked from inside.",
        "4  Clean sump: prove level control, duty/standby auto-alternation, the",
        "   high-level alarm at +1200, AND the hand pump, each independently.",
        "5  Trap seals: fill, then re-check after the envelope leak test at",
        "   +300 Pa.  A trap that has blown is a failed envelope test, not a",
        "   drainage snag.",
        "6  Record the AS-BUILT invert of every drain.  The design inverts on",
        "   this set are calculated, not surveyed.",
    ], h=NOTE, lead=LEAD)

    y = sh.panel(CB, y - 6, WB, "7   OPERATION AND MAINTENANCE", [
        "WEEKLY   prime every trap inside the gas-tight envelope, or prove the",
        "         automatic primers.  An evaporated seal is an envelope breach.",
        "MONTHLY  witnessed test of the STANDBY pump path and of the hand pump.",
        "         At a 0.31 % duty ratio a failed standby is never discovered by",
        "         use (finding DR-F1).  Test the high-level alarm at the panel.",
        "QUARTERLY  empty the silt bucket in CP-10 and rod the threshold channel.",
        "ANNUAL   de-sludge the septic tank (IS 2470 Pt 1 Cl. 6.3 sizes it for a",
        "         2-year sludge interval; annual inspection, 2-yearly removal).",
        "         Inspect the soakaway and the soak pit for ponding - ponding is",
        "         the first sign that the absorption assumption A7 was optimistic.",
        "ON USE   decon effluent tank TK-01 is tankered out AFTER THE ALL-CLEAR.",
        "         It is never emptied to any drain on this site.",
    ], h=NOTE, lead=LEAD)

    y = sh.panel(CB, y - 6, WB, "8   CONSTRUCTION-STAGE DRAINAGE  -  master B.3 mitigation", [
        "The permanent drainage above does not operate during construction, and",
        "the flotation case governs then.  Master B.3 already makes these",
        "mandatory; they are repeated here because they are drainage work:",
        "  1  CONTINUOUS DEWATERING from the start of excavation until backfill",
        "     and cover are complete.  FoS against flotation is 0.33 at the",
        "     mat-only stage and 0.78 with the walls up.",
        "  2  SIX TEMPORARY PRESSURE-RELIEF VALVES / KNOCK-OUT PLUGS in the mat",
        "     (shown on S-02), GROUTED UP ONLY AFTER BACKFILL.",
        "  3  Programme the sub-structure to complete before the monsoon, or bund",
        "     and positively drain with standby pumping and generator back-up.",
        "  4  Backfill SYMMETRICALLY, in layers.",
        "The permanent sump and its pumps are NOT a construction dewatering",
        "system and shall not be used as one.",
    ], h=NOTE, lead=LEAD)

    yB = sh.panel(CB, y - 6, WB, "9   CODES AND STANDARDS", [
        "IN THE MASTER PART G REGISTER  -  clauses quoted:",
        "    IS 2470 (Pt 1):1985   septic tank - Cl. 6.2, 6.3, 6.5, 6.6, 6.9, Table 1",
        "    IS 2470 (Pt 2):1985   soak pit - Cl. 4 percolation test, Cl. 5 dispersion",
        "    IS 456:2000           RC, cover, construction joints",
        "    IS 3370 (Pts 1, 2)    crack control 0.2 mm, liquid-retaining",
        "    IS 4991:1968          Cl. 6.2.1 recessing, Cl. 7.2 buried surfaces",
        "    NBC 2016 Part 4       means of escape, guarding",
        "",
        "NOT IN THE REGISTER  -  cited BY TITLE ONLY, no clause quoted:",
        "    IS 1742  building drainage        IS 5329  sanitary pipework",
        "    NBC 2016 Part 9  plumbing services",
        "",
        "*** NO CODE DOCUMENT IS IN THE WORKSPACE (master open item M2).  No",
        "    clause number outside the Part G register appears on this set. ***",
    ], h=NOTE, lead=LEAD)

    # ================================================== column C
    sh.text("10   DESIGN FLOWS   -   reproduced from sheet S-06 for a line-by-line check",
            (CC, TOP - 3.4), T["panel_head"], "M-TITLE")
    y = sh.table(CC, TOP - 8, [110, 36, 44, 52],
                 [(a, b, c, d) for a, b, c, d in P.DESIGN_FLOWS],
                 header=["ITEM", "FLOW", "STORE", "DISCHARGES TO"],
                 h=2.1, rh=6.2, layer="M-TABLE")

    sh.text("11   DESIGN BASIS   -   the numbers and where they come from",
            (CC, y - 8), T["panel_head"], "M-TITLE")
    y = sh.table(CC, y - 13, [100, 62, 80], [
        ("DESIGN GROUNDWATER TABLE", "(-)2.000 monsoon", "[A]  master A2"),
        ("STRUCTURAL SEEPAGE RATE", "0.5 L/m2/day", "[A]  master A8"),
        ("WETTED EXTERNAL ENVELOPE", "401 m2", "[R]  verified, calc D.1"),
        ("   = 56.40 perim x 4.700 sub", "+ 136.40 mat", "[R]  = 401.48 m2"),
        ("SEEPAGE INFLOW", "200 L/day", "[C]  S-06"),
        ("CONDENSATE + WASHDOWN", "200 L/day", "[C]  S-06"),
        ("TOTAL TO THE CLEAN SUMP", "400 L/day = 0.00463 L/s", "[R]  calc D.2"),
        ("SUMP STORE", "3.375 m3 = 8.44 days", "[R]  calc D.2"),
        ("RAINFALL INTENSITY", "50 mm/h", "[C]  Rev F drg 5 note 1"),
        ("   no return period or IDF", "*** OPEN ITEM D1 ***", "[U]"),
        ("SOAK-PIT ABSORPTION", "20 L/m2/day", "[A]  master A7"),
        ("   percolation test", "*** MANDATORY ***", "IS 2470 Pt 2 Cl. 4"),
        ("FOUL, PEACETIME", "450 L/day, 10 x 45 lpcd", "[C]  S-06"),
        ("SHELTER OVERPRESSURE", "+50 to +100 Pa, test +300", "[C]  S-06"),
        ("TRAP SEAL ADOPTED", "75 mm = 736 Pa = 2.5 x test", "[A]  calc D.6"),
        ("MAT SIDL ALLOWANCE", "1.0 kPa = 42 mm of screed", "[C]  master A.7.2"),
        ("SCREED ADOPTED, AREA MEAN", "52 mm = 1.24 kPa", "[R]  DR-F4, referred"),
        ("PIPE CAPACITY DN100 1:100", "6.72 L/s at 0.85 m/s", "[R]  calc D.4"),
        ("CAPACITY RATIO ON DESIGN Q", "1450 : 1", "[R]  size is not flow-driven"),
    ], header=["PARAMETER", "VALUE", "CLASS AND SOURCE"], h=T["table"], rh=5.0,
        layer="M-TABLE")

    sh.text("12   OPEN ITEMS CARRIED ON THIS SET   -   none of them is resolved here",
            (CC, y - 8), T["panel_head"], "M-TITLE")
    yC = sh.table(CC, y - 13, [30, 212], [
        ("C16", "ROOF / PLATFORM JUNCTION, master, unresolved.  Affects only which roof a"),
        ("", "     2.25 m2 catchment belongs to; the TOTAL catchment is unchanged"),
        ("C18", "SUMP PIT BASE 300 vs 400, master, unresolved.  400 HELD.  No drainage"),
        ("", "     effect - the invert is fixed at (-)7.600 and storage is measured from it"),
        ("A2", "DESIGN GWT (-)2.000 [ASSUMED].  Sets the wetted area and the seepage"),
        ("A7", "SOAK-PIT ABSORPTION 20 L/m2/day [ASSUMED].  PERCOLATION TEST MANDATORY"),
        ("A8", "SEEPAGE 0.5 L/m2/day [ASSUMED].  Sets the 8.44-day sump store"),
        ("DR-C1", "S-06 carries the REV E open-cut catchment 0.10 L/s for the stairwell."),
        ("", "     Conservative and superseded.  NOT corrected here - ruling required"),
        ("DR-C2", "SOAK PIT 21.99 m2 against 22.50 m2 REQUIRED - SHORT BY 2.3 %."),
        ("", "     Arithmetic, not judgement.  NOT resized here - ruling required"),
        ("DR-D1", "RAINFALL 50 mm/h has no return period, duration or IDF source"),
        ("DR-D2", "PEACETIME FOUL ROUTE FROM THE BAY 2 LAVATORY IS UNDEFINED"),
        ("DR-D3", "NO SITE PLAN, BOUNDARY, CONTOUR, WELL OR OUTFALL EXISTS"),
        ("DR-D4", "DECON EFFLUENT TANK EMPTYING ROUTE IS UNDEFINED"),
        ("DR-F1", "Sump duty ratio 0.31 % - monthly witnessed standby test required"),
        ("DR-F2", "Screed reduces the FINISHED clear height 25-78 mm below the 3200"),
        ("DR-F3", "Stairwell soakaway needs 54.6 h to recover from one sump-full"),
        ("DR-F4", "SCREED EXCEEDS THE 1.0 kPa MAT SIDL BY 0.24 kPa - REFERRED"),
        ("DR-F5", "TWO OF THE THREE HYDRAULIC ZONES HAVE NO DRAINAGE DESTINATION"),
    ], header=["REF", "ITEM"], h=2.1, rh=5.8, layer="M-TABLE")

    # ---------------- column A, lower: key plan and exclusions

    sh.view_title((CA, yA - 8), "V1", "KEY PLAN  -  THE THREE STRUCTURES",
                  "SCALE 1:100    SENTRY POST IS NOT SHOWN - IT IS OUTSIDE THIS PACKAGE")
    M = X.vw(100.0, CA + 14, yA - 100.0)
    V.underground_plan(sh, M, 100.0, bays=True, rooms=False, stair=True, esc=True)
    V.ground_plan(sh, M, 100.0, box_below=False)
    for tag, x, y, l, ty, seal, sv, z, c in D.DRAINS:
        sh.sym("GULLY", M(x, y), scale=0.55)
    sh.rect(*M(*D.SUMP_RECT[:2]), *M(*D.SUMP_RECT[2:]), "P-EQUIP")
    sh.text("CLEAN SUMP", M(11800, 300), T["small"], "M-TEXT", "BC")
    sh.rect(*M(*D.SERVICE_PLATE[:2]), *M(*D.SERVICE_PLATE[2:]), "P-DRAIN-RISING")
    sh.text("SERVICE ENTRY PLATE - THE ONLY ENVELOPE PENETRATION",
            M(11800, 6600), T["small"], "M-FLAG", "BC")
    sh.rect(*M(*D.DECON_TANK[:2]), *M(*D.DECON_TANK[2:]), "P-DRAIN-EFF")
    sh.text("TK-01", M(20800, 4900), T["small"], "M-TEXT", "CENTER")
    sh.dim_h(M(0, -900), M(22000, -900), M(0, -1700)[1], sc=100.0)
    sh.text("D-201 / D-203  UNDERGROUND", M(4000, -3000), T["small"], "M-CALLOUT", "BC")
    sh.text("D-101 / D-102 / D-103  ABOVE GROUND AND ENTRY",
            M(13000, 8900), T["small"], "M-CALLOUT", "BC")

    yA2 = yA - 128.0
    sh.panel(CA, yA2, WA, "4   WHAT THIS PACKAGE DOES NOT CALCULATE, AND WHY", [
        "SITE-WIDE STORM RUNOFF         no site plan, boundary, contour or",
        "                               external paved area exists          [N]",
        "RETURN PERIOD / IDF CURVE      only a bare 50 mm/h is recorded      [U]",
        "RUNOFF COEFFICIENT FOR TURF    no infiltration data; C = 1.00 used",
        "                               as the conservative bound           [A]",
        "TOTAL PUMP HEAD, EITHER SUMP   route length not fixed and no",
        "                               discharge level recorded            [N]",
        "FOUL FROM THE BAY 2 LAVATORY   no route exists - open item D2       [U]",
        "WASHDOWN / HOSE DESIGN FLOW    no washdown regime is specified      [N]",
        "UPLIFT AND FLOTATION           already designed in master B.3.  A",
        "                               drainage package does not re-open it",
        "PERMANENT GROUNDWATER LOWERING the box is a TANK, not a drained",
        "                               structure - by design               [C]",
    ], h=NOTE, lead=LEAD)

    V.scope_note(sh, CC, yC - 8, 242)
    X.evidence_key(sh, CC, yC - 58)
    sh.finish(scale="NOT TO SCALE", sheet_of="1 OF 11")
    return sh


# =====================================================================
def d002():
    sh = sheet("D-002", "DRAINAGE SYMBOLS, PIPE CODING AND ABBREVIATIONS",
               "THE KEY TO EVERY OTHER SHEET IN THIS SET", of="2 OF 11")

    # ---------------- column A : symbols
    sh.view_title((CA, TOP), "V1", "GRAPHIC SYMBOLS", "NOT TO SCALE")
    yy = TOP - 16
    for blk, desc in [("GULLY", "TRAPPED FLOOR GULLY - 75 DEEP SEAL, PRIMED"),
                      ("CHAMBER", "INSPECTION CHAMBER / CATCHPIT"),
                      ("PUMP", "SUBMERSIBLE PUMP"),
                      ("CLEANOUT", "RODDING EYE / CLEANOUT"),
                      ("NRV", "NON-RETURN VALVE  (gas-tight where noted)"),
                      ("VALVE", "ISOLATION VALVE")]:
        sh.sym(blk, (CA + 12, yy))
        sh.text(desc, (CA + 26, yy - 1.2), NOTE, "M-TEXT")
        yy -= 13
    yy -= 3
    sh.line((CA, yy + 6), (CA + WA, yy + 6), "M-TITLE")
    for lay, desc in [("P-DRAIN-STORM", "STORM / SURFACE WATER"),
                      ("P-DRAIN-WASTE", "WASTE - WASTEWATER"),
                      ("P-DRAIN-SOIL", "SOIL - FOUL"),
                      ("P-DRAIN-EFF", "DECON EFFLUENT - CONTAMINATED, SEGREGATED"),
                      ("P-DRAIN-RISING", "PUMPED RISING MAIN"),
                      ("P-DRAIN-SEEP", "GROUNDWATER / SEEPAGE"),
                      ("M-WATERPROOF", "TANKING MEMBRANE / WATERSTOP"),
                      ("M-ARCH-HIDDEN", "STRUCTURE OR SERVICE BEYOND"),
                      ("M-FLAG", "OPEN ITEM, DATA REQUIRED OR WARNING")]:
        if lay == "M-ARCH-HIDDEN":
            sh.dline((CA + 4, yy), (CA + 22, yy), lay)
        else:
            sh.line((CA + 4, yy), (CA + 22, yy), lay)
        sh.text(desc, (CA + 26, yy - 1.2), NOTE, "M-TEXT")
        yy -= 9
    yy -= 3
    sh.flow((CA + 10, yy), 0, 3.2)
    sh.text("DIRECTION OF FLOW", (CA + 26, yy - 1.2), NOTE, "M-TEXT")
    yy -= 11
    sh.level((CA + 8, yy), "INVERT LEVEL / FLOOR LEVEL")
    yy -= 12
    sh.text("FF 1:80", (CA + 4, yy), NOTE, "M-TEXT")
    sh.text("DIRECTION AND GRADIENT OF FLOOR FALL", (CA + 26, yy), NOTE, "M-TEXT")
    yy -= 10
    sh.tag((CA + 4, yy - 2), "PD-01  DN100  1:100", "M-CALLOUT", NOTE)
    sh.text("PIPE TAG - id, bore, gradient", (CA + 80, yy), NOTE, "M-TEXT")
    yy -= 12
    sh.text("[C] [R] [A] [U] [N]", (CA + 4, yy), NOTE, "M-FLAG")
    sh.text("EVIDENCE CLASS - see the key on this sheet", (CA + 60, yy), NOTE,
            "M-TEXT")

    X.evidence_key(sh, CA, yy - 10)

    # ---------------- column B : pipe coding
    sh.view_title((CB, TOP), "V2", "PIPE CODING", "APPLIES TO EVERY TAG ON THE SET")
    y = sh.panel(CB, TOP - 12, WB, "HOW A TAG IS READ", [
        "                    PD - 01",
        "                    |     |",
        "                    |     +----  sequence within the package",
        "                    +----------  P  plumbing / drainage discipline",
        "                                 D  drainage",
        "",
        "SERIES ALLOCATION",
        "    PD-01 to PD-09    inside the protective envelope, level (-)6.100",
        "    PD-10 to PD-19    above ground and entry, levels 0.000 and (-)2.000",
        "    GY-nn  gully or floor drain          CH-nn  channel",
        "    CP-nn  catchpit / collection point   IC-nn  inspection chamber",
        "    RE-nn  rodding eye                   SU-nn  sump",
        "    PU-nn  pump                          TK-nn  tank",
        "    ST-nn  septic tank                   SK-nn  soakaway / soak pit",
        "    SN-nn  sanitary fixture              BW-nn  builder's work request",
        "",
        "SERVICE CODES used in the schedules and on the plans",
        "    STORM        surface and rainwater",
        "    WASTE        wastewater - basins, washdown, condensate, seepage",
        "    SOIL         foul - peacetime only, and only under case B of D2",
        "    EFFLUENT     decon airlock - CONTAMINATED, SEGREGATED THROUGHOUT",
        "    RISING MAIN  pumped, under pressure, non-gravity",
    ], h=NOTE, lead=LEAD)

    sh.text("V3   MATERIALS", (CB, y - 9), T["view_title"], "M-TITLE")
    y = sh.table(CB, y - 17, [56, 74, 134], [
        ("GRAVITY DRAINS", "uPVC or HDPE, DN100 min",
         "[A]  n = 0.010 in the capacity check, calc D.4"),
        ("RISING MAINS", "DUCTILE IRON or STAINLESS",
         "[A]  welded or flanged - NO push-fit joint inside the envelope"),
        ("TRAPS", "75 mm DEEP SEAL, PRIMED",
         "[A]  holds 736 Pa against the +300 Pa leak test"),
        ("SLEEVES", "CAST-IN, PUDDLE-FLANGED",
         "[A]  welded to the cage for EMP continuity - D-304"),
        ("CHANNEL + GRATING", "300 wide, full 1500 width",
         "[C]  Rev F, entry threshold X 8950-9250"),
        ("SOAKAWAY FILL", "40-80 mm BRICKBAT / STONE",
         "[C]  S-06.  300 sand at the top, RC cover slab"),
        ("SUMP AND PIT RC", "M35, T16 @ 150 EF EW",
         "[C]  master F.1.  4-T20 trimmers each face / side"),
        ("MEMBRANE", "AS R-805, DRESSED TO EVERY SLEEVE",
         "[C]  no cover is reduced for waterproofing"),
    ], header=["ITEM", "SPECIFICATION", "CLASS, SOURCE AND NOTE"],
        h=2.1, rh=6.4, layer="M-TABLE")

    sh.panel(CB, y - 8, WB, "SEGREGATION - THE RULE THAT OVERRIDES EVERY OTHER", [
        "NO CLEAN DRAIN, GULLY, TRAP OR CHANNEL MAY BE CONNECTED TO A DECON",
        "EFFLUENT DRAIN, ANYWHERE, UNDER ANY CIRCUMSTANCE.",
        "",
        "The two systems share no pipe, no chamber, no vent and no discharge",
        "point.  Decon effluent leaves the site BY TANKER ONLY.  This is not a",
        "preference - it is the reason the shelter has a decon airlock at all.",
        "",
        "S-06:  'DECON EFFLUENT NEVER ENTERS THE CLEAN SUMP - TANKERED OUT AFTER",
        "        THE ALL-CLEAR'",
        "S-06:  'STORM SOAKAWAY - CLEAN SUMP DISCHARGE.  SEPARATE FROM FOUL'",
    ], h=NOTE, lead=LEAD)

    # ---------------- column C : abbreviations + drawing register
    sh.text("V4   ABBREVIATIONS", (CC, TOP), T["view_title"], "M-TITLE")
    y = sh.table(CC, TOP - 8, [46, 196], [
        ("IL", "invert level"),
        ("FFL", "finished floor level"),
        ("CL", "cover level"),
        ("DN", "nominal diameter"),
        ("NRV", "non-return valve"),
        ("BCV", "blast check valve"),
        ("RE / IC", "rodding eye / inspection chamber"),
        ("GWT", "groundwater table"),
        ("SIDL", "superimposed dead load"),
        ("BW", "builder's work request - work required of another discipline"),
        ("MCT", "multi-cable transit - the service entry frame in the north wall"),
        ("OPRV", "overpressure relief valve"),
        ("BD1 / BD2", "blast door 1 / 2, 1200 x 2100, 7 bar - THE PROTECTIVE BOUNDARY"),
        ("W5", "bay 5/6 wall, 200 - fire and gas-tight, no pressure differential"),
        ("W6 / W7", "bay 6/7 and 7/8 walls, 400 - THE PROTECTIVE BOUNDARY"),
        ("W8", "110 partitions, each with a 900 door gap at Y 2500-3400"),
        ("ESC 1 / ESC 2", "escape shafts, 1400 dia clear, 250 RC collar"),
        ("Z1 / Z2 / Z3", "hydraulic zones - clean / decon / grey.  See D-201"),
    ], header=["ABBREVIATION", "MEANING"], h=2.1, rh=6.2, layer="M-TABLE")

    sh.text("V5   DRAWING REGISTER   -   this package", (CC, y - 9),
            T["view_title"], "M-TITLE")
    sh.table(CC, y - 17, [30, 150, 62], [
        ("D-001", "General drainage notes, legend and design basis", "NTS"),
        ("D-002", "Drainage symbols, pipe coding and abbreviations", "NTS"),
        ("D-101", "Above-ground / entry level drainage plan", "1:100"),
        ("D-102", "Rainwater catchment and surface-water plan", "1:100"),
        ("D-103", "Entry stairwell and headhouse drainage", "1:50"),
        ("D-201", "Underground drainage plan - falls, gullies, zones", "1:60"),
        ("D-203", "Underground wastewater and sanitary plan", "1:60"),
        ("D-204", "Sump and pumping - plan, section, discharge train", "1:25 / 1:20"),
        ("D-301", "Drainage sections - grade to discharge", "1:60 / 1:100"),
        ("D-304", "Pipe penetration and waterproofing details", "1:10"),
        ("D-305", "Septic tank, soak pit and chamber details", "1:25"),
        ("D-202", "NOT ISSUED - there is no rainwater below ground.", "-"),
        ("", "     The box is tanked and buried; groundwater is on D-201", ""),
        ("D-302", "MERGED INTO D-103 - one sheet is more useful than two", "-"),
        ("D-303", "MERGED INTO D-204 - sump plan, section and detail together", "-"),
    ], header=["SHEET", "TITLE", "SCALE"], h=2.1, rh=6.2, layer="M-TABLE")

    sh.finish(scale="NOT TO SCALE", sheet_of="2 OF 11")
    return sh


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, name in ((d001, "D-001_General_Drainage_Notes_Legend_Design_Basis"),
                     (d002, "D-002_Drainage_Symbols_and_Pipe_Coding")):
        s = fn()
        s.save(os.path.join(OUT, name + ".dxf"))
        print("  ", name + ".dxf")
