"""sg_site_sheets.py  --  SG-102 and SG-202  (revision SG2).

    SG-102  SITE LAYOUT PLAN        *** THE PROJECT'S FIRST ***
    SG-202  EXTERNAL WORKS SITING, SECTION AND THE SOAK PIT FINDING

SG-102 is the drawing master gap D3 has been blocking since DR1 on 5
September.  It is a TRUE PLAN, to scale, with the whole external works layout
dimensioned from confirmed structure geometry - and it carries, on its face,
the list of what is STILL missing, because the layout exists and the survey
does not.

Every position, length and clearance is read from sg_site.py and computed
here, so the sheets cannot disagree with the schedules or the calculation.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import sg_dxf as X                                          # noqa: E402
import sg_proj as P                                         # noqa: E402
import sg_data as D                                         # noqa: E402
import sg_site as S                                         # noqa: E402

OUT = os.path.abspath(os.path.join(HERE, "..", "DXF"))


def _wrap(s, n):
    out, cur = [], ""
    for wd in s.split():
        if len(cur) + len(wd) + 1 > n:
            out.append(cur)
            cur = wd
        else:
            cur = (cur + " " + wd).strip()
    if cur:
        out.append(cur)
    return out


# =====================================================================
def sg102():
    sh = X.Sheet("SG-102",
                 "SITE LAYOUT PLAN",
                 "THE PROJECT'S FIRST.  EXTERNAL WORKS FIXED, DIMENSIONED "
                 "FROM CONFIRMED GEOMETRY.  THE LAYOUT EXISTS - THE SURVEY "
                 "DOES NOT",
                 flags=("D3", "SG2-V1", "SG2-V2", "SG2-V3", "SG-V4", "U4"),
                 sheet_of="3 OF 5")

    SC = 150.0                       # 1 : 150
    OX, OY = 137.0, 300.0            # paper position of project (0, 0)

    def px(x):
        return OX + x / SC

    def py(y):
        return OY + y / SC

    sh.view_title((14, 512), "V1", "SITE LAYOUT PLAN",
                  "SCALE 1:150.  PROJECT COORDINATES, ORIGIN AT THE SW CORNER "
                  "OF THE BOX.  +X = EAST, +Y = NORTH  [A] SG2.  "
                  "NO SURVEYED BOUNDARY EXISTS - SEE THE RIGHT-HAND COLUMN")

    # ---------------------------------------------------- fall arrows
    for yy in (-3000, 3100, 9000):
        sh.dline((px(-15000), py(yy)), (px(-10000), py(yy)), "G-SETTING",
                 2.0, 1.6)
        sh.flow((px(-10000), py(yy)), 0.0, 2.6, "G-SETTING")
    sh.text("GROUND FALLS EAST", (px(-15500), py(11200)), 2.0, "G-SETTING")
    sh.text("580 -> 575 toward the track", (px(-15500), py(10000)), 1.8,
            "M-TEXT")
    sh.text("[R] SG1, deck slide 15", (px(-15500), py(8800)), 1.8, "M-TEXT")
    sh.north((px(-13000), py(17500)))

    # ---------------------------------------------------- existing works
    for name, x0, y0, x1, y1, cls, note in S.EXISTING:
        if "EXCAVATION" in name:
            for a, b in (((x0, y0), (x1, y0)), ((x1, y0), (x1, y1)),
                         ((x1, y1), (x0, y1)), ((x0, y1), (x0, y0))):
                sh.dline((px(a[0]), py(a[1])), (px(b[0]), py(b[1])),
                         "G-NODATA", 2.0, 1.6)
            continue
        lay = "G-FLAGG" if "ASSUMED" in name else "G-STRUCT"
        sh.rect(px(x0), py(y0), px(x1), py(y1), lay)

    sh.hatch_pat([(px(0), py(0)), (px(22000), py(0)),
                  (px(22000), py(6200)), (px(0), py(6200))],
                 "ANSI31", 1.6, 0.0, "M-HATCH")
    sh.text("UNDERGROUND BOX   22 000 x 6 200", (px(11000), py(4200)), 2.4,
            "G-STRUCT", "CENTER")
    sh.text("ROOF TOP (-)2.000 UNDER 2 000 OF ENGINEERED COVER",
            (px(11000), py(2900)), 1.9, "M-TEXT", "CENTER")
    sh.text("*** NO PIPE, PIT OR CHAMBER ON THE COVER ***",
            (px(11000), py(1600)), 1.9, "M-FLAG", "CENTER")
    sh.text("EXCAVATION + 1 000 WORKING SPACE", (px(-900), py(7500)), 1.8,
            "G-NODATA")
    sh.text("HEADHOUSE", (px(16000), py(5300)), 1.8, "G-STRUCT", "CENTER")
    sh.text("ENTRY STAIRWELL", (px(12650), py(6800)), 1.8, "G-STRUCT",
            "CENTER")
    sh.text("ENTRY, GRADE DOOR", (px(-1000), py(6600)), 1.8, "M-FLAG",
            "RIGHT")
    sh.flow((px(8700), py(6750)), 0.0, 2.6, "M-FLAG")
    sh.line((px(-800), py(6750)), (px(8500), py(6750)), "M-FLAG")
    sh.text("SH-2", (px(22898), py(3400)), 1.7, "G-STRUCT", "CENTER")
    sh.text("ESC 1", (px(2050), py(2050)), 1.7, "G-STRUCT", "CENTER")
    sh.text("ESC 2", (px(19900), py(2050)), 1.7, "G-STRUCT", "CENTER")
    sh.text("SENTRY POST", (px(11000), py(18400)), 2.0, "G-FLAGG", "CENTER")
    sh.text("POSITION ASSUMED - master U4", (px(11000), py(17200)), 1.8,
            "M-FLAG", "CENTER")
    sh.text("NOTHING HERE IS DIMENSIONED FROM IT", (px(11000), py(16200)),
            1.8, "M-FLAG", "CENTER")

    # SH-1, which has no position
    for a, b in (((-3400, 1400), (-1800, 1400)), ((-1800, 1400), (-1800, 2700)),
                 ((-1800, 2700), (-3400, 2700)), ((-3400, 2700), (-3400, 1400))):
        sh.dline((px(a[0]), py(a[1])), (px(b[0]), py(b[1])), "G-FLAGG",
                 2.0, 1.6)
    sh.text("SH-1 ?", (px(-2600), py(2050)), 1.7, "G-FLAGG", "CENTER")
    sh.text("SH-1 FRESH-AIR INTAKE.  'WEST OF THE BOX' IS THE WHOLE",
            (px(-15500), py(-1200)), 1.8, "M-FLAG")
    sh.text("OF WHAT THE PROJECT RECORDS.  NO X, NO Y.  SHOWN",
            (px(-15500), py(-2400)), 1.8, "M-FLAG")
    sh.text("INDICATIVELY ONLY.   SG2-V3", (px(-15500), py(-3600)), 1.8,
            "M-FLAG")

    # ---------------------------------------------------- the reserve
    e = S.EWR
    sh.pline([(px(e["x0"]), py(e["y0"])), (px(e["x1"]), py(e["y0"])),
              (px(e["x1"]), py(e["y1"])), (px(e["x0"]), py(e["y1"]))],
             "G-FLAGG", close=True)
    sh.text("EXTERNAL WORKS RESERVE", (px((e["x0"] + e["x1"]) / 2),
            py(e["y1"]) + 5.0), 2.4, "G-FLAGG", "CENTER")
    sh.text(f"{(e['x1'] - e['x0']) / 1000:.1f} x "
            f"{(e['y1'] - e['y0']) / 1000:.1f} m  -  DOWNGRADIENT, "
            f"{(e['x0'] - 23000) / 1000:.0f} m CLEAR OF THE EXCAVATION",
            (px((e["x0"] + e["x1"]) / 2), py(e["y1"]) + 1.8), 1.8, "M-TEXT",
            "CENTER")

    for tag, x0, y0, x1, y1, what in S.FALLBACK:
        for a, b in (((x0, y0), (x1, y0)), ((x1, y0), (x1, y1)),
                     ((x1, y1), (x0, y1)), ((x0, y1), (x0, y0))):
            sh.dline((px(a[0]), py(a[1])), (px(b[0]), py(b[1])),
                     "G-MURRUM", 2.2, 2.2)
        sh.text(tag.split()[0], (px(x0) + 1.6, py(y0) + 1.6), 1.8, "G-MURRUM")

    # ---------------------------------------------------- the works
    for tag, kind, ccx, ccy, cls, serves in S.CIRCULAR:
        lay = "G-FLAGG" if tag == "SK-01" else "G-STRUCT"
        sh.circle((px(ccx), py(ccy)), S.PIT_DIA / 2.0 / SC, lay)
        sh.circle((px(ccx), py(ccy)), 0.6, lay)
        sh.text(tag, (px(ccx), py(ccy) + S.PIT_DIA / 2.0 / SC + 1.2), 1.9,
                lay, "CENTER")
    for tag, kind, x0, y0, x1, y1, cls, note in S.RECTANGULAR:
        sh.rect(px(x0), py(y0), px(x1), py(y1), "G-STRUCT")
        sh.text(tag, (px((x0 + x1) / 2), py(y1) + 1.2), 1.9, "G-STRUCT",
                "CENTER")

    # ---------------------------------------------------- pipe runs
    for tag, frm, to, dn, grad, pts, cls, note in S.RUNS:
        if not pts:
            continue
        lay = "P-DRAIN-SOIL" if tag == "PD-16" else "P-DRAIN-STORM"
        sh.pline([(px(x), py(y)) for x, y in pts], lay)
    sh.text("PD-11  32.4 m", (px(24000), py(9800) + 1.4), 1.8,
            "P-DRAIN-STORM")
    sh.text("PD-16  5.4 m", (px(37600), py(16000) + 3.4), 1.8,
            "P-DRAIN-SOIL")
    sh.text("COMMON SERVICES TRENCH  -  PD-06 + PD-11 + PD-13 SHARE IT",
            (px(9000), py(9800) - 3.2), 1.8, "M-SECTION")

    for ref, x, y, what in S.PERC_TESTS:
        sh.line((px(x) - 2.6, py(y) - 2.6), (px(x) + 2.6, py(y) + 2.6),
                "G-NODATA")
        sh.line((px(x) - 2.6, py(y) + 2.6), (px(x) + 2.6, py(y) - 2.6),
                "G-NODATA")
        sh.text(ref, (px(x) + 3.4, py(y) - 2.6), 1.8, "G-NODATA")
    sh.text("PT-1 / PT-2  PERCOLATION TESTS, EACH AT ITS OWN PIT",
            (px(33500), py(5200)), 1.8, "G-NODATA")

    # ---------------------------------------------------- key dimension
    sh.dim_h((px(37500), py(16000)), (px(42900), py(16000)),
             py(16000) - 6.0, 1.0)
    sh.text("5.40 m  >= 5 m  IS 2470  PASS", (px(40200), py(16000) - 9.6),
            1.8, "G-FLAGG", "CENTER")

    # ================================================ V2 the key diagram
    KSC = 900.0
    KX, KY = 300.0, 200.0
    sh.view_title((14, 258), "V2", "LOCATION KEY  -  THE 50 m ENVELOPE",
                  "SCALE 1:900.  The envelope the owner has confirmed "
                  "available, with the whole layout inside it.")

    def kx(x):
        return KX + (x - S.PIN_AT[0]) / KSC

    def ky(y):
        return KY + (y - S.PIN_AT[1]) / KSC

    sh.circle((KX, KY), S.ENVELOPE_R / KSC, "G-SETTING")
    sh.circle((KX, KY), 1.8, "G-FLAGG")
    sh.line((KX - 3, KY), (KX + 3, KY), "G-FLAGG")
    sh.line((KX, KY - 3), (KX, KY + 3), "G-FLAGG")
    sh.dline((KX, KY), (KX + S.ENVELOPE_R / KSC, KY), "G-SETTING", 2.0, 1.6)
    sh.text("R 50 m  [C] OWNER", (KX + 6, KY + 2.0), 2.0, "G-SETTING")
    sh.rect(kx(0), ky(0), kx(22000), ky(6200), "G-STRUCT")
    sh.rect(kx(e["x0"]), ky(e["y0"]), kx(e["x1"]), ky(e["y1"]), "G-FLAGG")
    sh.rect(kx(9000), ky(15250), kx(13000), ky(20250), "G-FLAGG")
    sh.text("BOX", (kx(11000), ky(3100) - 0.8), 1.8, "G-STRUCT", "CENTER")
    sh.text("RESERVE", (kx(42000), ky(12000) - 0.8), 1.8, "G-FLAGG",
            "CENTER")
    sh.text("SENTRY [A]", (kx(11000), ky(22500)), 1.8, "G-FLAGG", "CENTER")
    sh.text(f"{S.PIN_LAT} N   {S.PIN_LON} E   [C] OWNER",
            (KX, KY - S.ENVELOPE_R / KSC - 6.0), 2.2, "G-FLAGG", "CENTER")
    sh.text("THE PIN IS TAKEN AS THE CENTRE OF THE BOX - AN ADOPTED "
            "CONVENTION [A].", (KX, KY - S.ENVELOPE_R / KSC - 10.0), 1.9,
            "M-FLAG", "CENTER")
    sh.text("If it was meant as a corner, THE WHOLE LAYOUT TRANSLATES "
            "RIGIDLY and no offset changes.",
            (KX, KY - S.ENVELOPE_R / KSC - 13.6), 1.9, "M-FLAG", "CENTER")
    sh.text("WORST CASE 42.5 m OF THE 50 m AVAILABLE  -  AND THE BINDING",
            (KX, KY - S.ENVELOPE_R / KSC - 18.6), 1.9, "M-TEXT", "CENTER")
    sh.text("ELEMENT IS THE SENTRY POST, WHOSE POSITION IS ASSUMED.",
            (KX, KY - S.ENVELOPE_R / KSC - 22.2), 1.9, "M-TEXT", "CENTER")

    # ---------------------------------------------------- right column
    sh.panel_column(662.0, 528.0, 120.0, 167.0, [
        ("WHAT THIS SHEET CLOSES", [
            "Master H.9 recorded the positions of the",
            "soakaways, the septic tank and the",
            "external chambers as NOT DETERMINABLE -",
            "'no site plan, boundary or contour",
            "exists' - and with them FIVE PIPE",
            "LENGTHS and the IS 2470 OFFSETS.",
            "Drainage D.11 ends on the same sentence.",
            "",
            "The owner has supplied the COORDINATE",
            "and a 50 m WORKING ENVELOPE.  With SG1's",
            "contours and ground profile and the",
            "project's own confirmed geometry, THE",
            "POSITIONS CAN BE DETERMINED.",
            "",
            "FOUR of the five pipe lengths: FIXED.",
            "TWO of the three offsets: DEMONSTRATED.",
            "SEVEN external structures: PLACED.",
        ]),
        ("WHAT IT DOES NOT CLOSE   [N]", [
            "a surveyed BOUNDARY",
            "a BENCHMARK and spot levels    SG-V4",
            "the position of any WELL       SG2-V1",
            "the distance to the FENCE      SG2-V2",
            "existing services on the plot",
            "a WIND ROSE                    SG2-V4",
            "the sentry post position       U4",
            "the final discharge question   D3",
            "",
            "EVERY ONE OF THOSE IS A SURVEY OUTPUT,",
            "and none of them moves anything fixed",
            "here: the layout is dimensioned from",
            "CONFIRMED structure geometry and every",
            "clearance is RELATIVE.  If the fence is",
            "closer than the reserve's east edge THE",
            "WHOLE RESERVE TRANSLATES AND NOT ONE",
            "OFFSET CHANGES.",
        ]),
        ("WHY EVERYTHING IS ON THE EAST SIDE", [
            "1  DOWNGRADIENT.  Nothing recharges the",
            "   ground upslope or alongside a box",
            "   that is flotation-critical at FoS",
            "   0.33 in the mat-only stage - and",
            "   whose side backfill, at 95 % MDD, is",
            "   MORE permeable than the basalt around",
            "   it, so effluent released near it",
            "   would run INTO the backfill and down",
            "   the outside of the tanking.",
            "2  ONE percolation-test location, ONE",
            "   keep-clear zone, ONE reserved",
            "   fallback.",
            "3  ONE TRENCH.  PD-06, PD-11 and PD-13",
            "   share it.  Where rockhead is 0.9-1.5",
            "   m the cost is the trench, and the",
            "   trench is cut once.",
            "4  CONCEALMENT.  Four cover slabs and a",
            "   2 m septic vent, grouped 11-22 m away",
            "   and downgradient, MARK THE DRAINAGE",
            "   FIELD, NOT THE SHELTER.",
        ]),
    ], gap=5.0)

    X.evidence_key(sh, 420, 150, 230.0)
    sh.finish(scale="1:150 AND 1:900", sheet_of="3 OF 5")
    return sh.save(os.path.join(OUT, "SG-102_Site_Layout_Plan.dxf"))


# =====================================================================
def sg202():
    sh = X.Sheet("SG-202",
                 "EXTERNAL WORKS SITING AND THE SOAK PIT FINDING",
                 "WHY A 3.5 m DEEP PIT DOES NOT FIT THIS GROUND, AND WHAT IS "
                 "RESERVED INSTEAD",
                 flags=("SG2-F1", "SG-V2", "SG-V3", "SG2-V1", "A2", "A7"),
                 sheet_of="5 OF 5")

    # ================================================ V1 the pit section
    SC = 25.0
    G = 452.0

    def py(l):
        return G + l / SC

    sh.view_title((14, 522), "V1",
                  "THE SOAK PIT AGAINST THE GROUND IT IS CUT INTO",
                  "SCALE 1:25 VERTICAL.  LEVELS RELATIVE TO LOCAL FINISHED "
                  "GRADE AT THE PIT - there is no benchmark, and the site "
                  "fall is itself disputed (SG-V4)")

    PX0, PW = 60.0, S.PIT_DIA / SC
    # strata, from SG1's profile
    strata = [(0.0, -250.0, "CH", "BLACK COTTON  CH,  FSI 60-65 %"),
              (-250.0, -1000.0, "MURRUM", "MURRUM  -  'IMPERVIOUS IN NATURE'"),
              (-1000.0, -1400.0, "BROKEN", "BROKEN BASALT  -  THE ONLY "
               "PERMEABLE HORIZON"),
              (-1400.0, -5200.0, "ROCK", "SOUND BASALT  -  matrix "
               "permeability effectively ZERO")]
    for top, bot, key, lab in strata:
        name, layer, pat, psc, ang = X.STRATA[key]
        pts = [(PX0 - 40, py(bot)), (PX0 + PW + 150, py(bot)),
               (PX0 + PW + 150, py(top)), (PX0 - 40, py(top))]
        sh.hatch_pat(pts, pat, psc, ang, layer)
        sh.pline(pts, layer, close=True)
        sh.text(lab, (PX0 + PW + 154, (py(top) + py(bot)) / 2.0 - 0.9), 1.9,
                layer)

    # the pit
    sh.rect(PX0, py(S.PIT_INV), PX0 + PW, py(S.PIT_TOP), "G-STRUCT")
    sh.hatch_pat([(PX0, py(S.PIT_INV)), (PX0 + PW, py(S.PIT_INV)),
                  (PX0 + PW, py(S.PIT_TOP)), (PX0, py(S.PIT_TOP))],
                 "GRAVEL", 0.4, 0.0, "G-STRUCT")
    sh.rect(PX0 - 6, py(S.PIT_TOP), PX0 + PW + 6, py(S.PIT_TOP) + 4.0,
            "G-STRUCT")
    sh.text("RC COVER SLAB", (PX0 + PW / 2, py(S.PIT_TOP) + 5.6), 1.9,
            "G-STRUCT", "CENTER")
    sh.text("SK-01 / SK-02", (PX0 + PW / 2, py(-2200)), 2.2, "G-STRUCT",
            "CENTER")
    sh.text("2 200 dia", (PX0 + PW / 2, py(-2600)), 1.9, "G-STRUCT", "CENTER")
    sh.text("3 500 eff", (PX0 + PW / 2, py(-2950)), 1.9, "G-STRUCT", "CENTER")
    sh.text("24.19 m2", (PX0 + PW / 2, py(-3300)), 1.9, "G-STRUCT", "CENTER")

    # grade line
    sh.line((PX0 - 44, G), (PX0 + PW + 150, G), "M-LEVEL")
    sh.text("LOCAL FINISHED GRADE", (PX0 - 44, G + 2.2), 2.0, "M-LEVEL")

    # the two water table readings
    for dw, lab, off in ((1300.0, "(a) DESIGN GWT (-)2.000 taken as a LEVEL, "
                          "reserve 0.70 m lower", 0.0),
                         (2000.0, "(b) 'water table at depth of 2 m below GL' "
                          "-  deck slide 29", -4.4)):
        yy = py(-dw)
        sh.dline((PX0 - 44, yy), (PX0 + PW + 148, yy), "G-WATER", 3.0, 2.0)
        sh.text(lab, (PX0 - 44, yy + 1.4 + off), 1.9, "G-WATER")
    sh.text("BETWEEN THESE TWO READINGS LIES THE WHOLE ANSWER  -  AND THE "
            "PROJECT HOLDS BOTH", (PX0 - 44, py(-1700) - 1.0), 2.0, "G-FLAGG")

    # the dry / wet split
    for dw, tag in ((1300.0, "(a)"), (2000.0, "(b)")):
        dry = max(0.0, dw + S.PIT_TOP)
        a = S.side_area(S.PIT_DIA, dry)
        xx = PX0 - 30 if tag == "(a)" else PX0 - 30
    sh.rect(14, 150, 300, 250, "G-FLAGG")
    sh.text("HOW MUCH OF THE PIT IS ABOVE THE WATER TABLE?", (157, 240), 2.4,
            "G-FLAGG", "CENTER")
    sh.text(f"{'reading':<34}{'water':>9}{'DRY':>8}{'area':>9}{'of 22.50':>10}",
            (20, 231), 2.0, "M-TABLE")
    yy = 224
    for label, dw in (("(a) absolute (-)2.000", 1300.0),
                      ("(b) 2 m below local grade", 2000.0)):
        dry = max(0.0, dw + S.PIT_TOP)
        a = S.side_area(S.PIT_DIA, dry)
        sh.text(f"{label:<34}{dw / 1000:>7.2f} m{dry / 1000:>7.2f}m"
                f"{a:>8.2f}m2{a / 22.50:>9.1%}", (20, yy), 2.0, "M-TEXT")
        yy -= 5.4
    sh.text("*** 21 % TO 43 % OF THE REQUIRED AREA IS ABOVE THE WATER. ***",
            (20, yy - 2), 2.1, "G-FLAGG")
    sh.text("The rest is PERMANENTLY SUBMERGED by the project's own design",
            (20, yy - 7), 2.0, "M-TEXT")
    sh.text("assumption, and a submerged wall does not infiltrate: no",
            (20, yy - 12), 2.0, "M-TEXT")
    sh.text("unsaturated storage to receive it, no head to drive it.",
            (20, yy - 17), 2.0, "M-TEXT")
    sh.text("THIS IS GEOMETRY AGAINST A STATED DESIGN LEVEL - it does not",
            (20, yy - 23), 2.0, "G-FLAGG")
    sh.text("depend on the percolation rate at all.", (20, yy - 28), 2.0,
            "G-FLAGG")

    # broken rock table
    sh.rect(312, 150, 644, 250, "G-FLAGG")
    sh.text("AND WHAT IS THE REST OF IT CUT THROUGH?", (478, 240), 2.4,
            "G-FLAGG", "CENTER")
    sh.text(f"{'location':<30}{'broken-rock band':>20}{'thk':>8}"
            f"{'side area':>12}{'of 22.50':>10}", (318, 231), 2.0, "M-TABLE")
    yy = 224
    for loc, layers in D.FINDINGS:
        br = [l for l in layers if "Broken" in l[1]]
        if not br:
            continue
        lo, hi = [float(t) for t in br[0][0].replace("m", "").split("-")]
        a = S.side_area(S.PIT_DIA, (hi - lo) * 1000.0)
        sh.text(f"{loc[:30]:<30}{lo:>9.2f} -{hi:>7.2f}{hi - lo:>7.2f}m"
                f"{a:>10.2f}m2{a / 22.50:>9.1%}", (318, yy), 2.0, "M-TEXT")
        yy -= 5.4
    sh.text("*** THE ONLY DEMONSTRABLY PERMEABLE HORIZON IS 0.2-0.5 m THICK "
            "***", (318, yy - 2), 2.1, "G-FLAGG")
    sh.text("and contributes 15 % or less of the required area.  Above it:",
            (318, yy - 7), 2.0, "M-TEXT")
    sh.text("black cotton that SWELLS SHUT when wet, over murrum the deck's",
            (318, yy - 12), 2.0, "M-TEXT")
    sh.text("own slide 30 calls IMPERVIOUS.  Below it: sound basalt, which",
            (318, yy - 17), 2.0, "M-TEXT")
    sh.text("takes water only through JOINTS - and no joint data exists.",
            (318, yy - 22), 2.0, "M-TEXT")
    sh.text("No RQD.  No packer test.  SG-V2.", (318, yy - 27), 2.0,
            "G-NODATA")

    # the conclusion band
    sh.rect(14, 96, 644, 144, "G-FLAGG")
    sh.text("SG2-F1   THE SHORTFALL WAS NEVER ARITHMETIC.  IT IS DEPTH.",
            (329, 134), 3.2, "G-FLAGG", "CENTER")
    sh.text("RC1 fixed the arithmetic (C19: 2.0 -> 2.200 dia, 24.19 m2 against "
            "22.50 required) and wrote the sentence this sheet starts from -",
            (329, 125), 2.0, "M-TEXT", "CENTER")
    sh.text("'deepening drives the pit further below the design GWT at "
            "(-)2.000, WHERE IT CANNOT SOAK AT ALL'.  Nobody had quantified "
            "it.", (329, 118), 2.0, "M-TEXT", "CENTER")
    sh.text("THE FORM THAT FITS THIS GROUND IS SHALLOW AND WIDE, NOT DEEP AND "
            "NARROW  -  a dispersion trench in the 0.5-1.6 m broken-rock",
            (329, 110), 2.2, "G-FLAGG", "CENTER")
    sh.text("horizon, ABOVE the water table.  IS 2470 (Pt 2) Cl. 5 - the "
            "fallback master K.2 A7 has named all along.  SK-01 IS NOT "
            "RE-SIZED HERE:", (329, 103), 2.0, "M-TEXT", "CENTER")
    sh.text("the percolation test governs.  What IS done is to RESERVE THE "
            "GROUND, so a failed test costs a redesign and not a re-siting.",
            (329, 98), 2.0, "M-TEXT", "CENTER")

    # ------------------------------------------------------ right column
    sh.panel_column(662.0, 528.0, 120.0, 167.0, [
        ("THE FALLBACK, RESERVED", [
            "A trench of effective depth h gives 2h",
            "m2 of side area per metre run - the same",
            "basis this project uses for the pit,",
            "base discounted because it clogs.",
            "",
            "DF-1  FOUL     14.5 x 6.5 m reserved",
            "      3 runs x 14.5 m = 43.5 m",
            "      87 m2  ->  serves 450 L/day down",
            "      to 5.17 L/m2/day = 26 % of the",
            "      assumed 20",
            "",
            "DF-2  CLEAN    14.5 x 3.5 m reserved",
            "      2 runs x 14.5 m = 29.0 m",
            "      58 m2  ->  serves 400 L/day down",
            "      to 6.90 L/m2/day = 34 %",
            "",
            "THE RESERVE CARRIES BOTH STREAMS AT",
            "ROUGHLY A QUARTER TO A THIRD OF THE",
            "ASSUMED RATE.  The percolation test can",
            "come back badly and the answer is still",
            "a redesign inside the same footprint.",
        ]),
        ("WHERE THE PERCOLATION TEST HAS TO BE DONE", [
            "Master K.2 A7 makes it MANDATORY.",
            "Drainage D.12 calls it 'on the critical",
            "path for three independent reasons'.",
            "NOBODY HAS EVER SAID WHERE.",
            "",
            "PT-1   (44000, 16000)  at SK-01",
            "PT-2   (35000,  8500)  at SK-02",
            "",
            "EACH AT ITS OWN PIT'S POSITION, not at a",
            "convenient spot near the site hut.",
            "",
            "AND AT BOTH DEPTHS.  A test taken only",
            "at (-)4.100 measures the formation the",
            "FALLBACK WILL NOT USE.  Take each at the",
            "pit invert AND at the trench invert",
            "(about 1.5 m), or the fallback is",
            "undesigned the day the pit is abandoned.",
        ]),
        ("SG-V3 RULED  -  AND WHAT IT LEAVES STANDING", [
            "THE OWNER DOES NOT ACCEPT THE COST OF",
            "MOVING THE GROUNDWATER MONITORING.",
            "A1080 stays 12-11-26 to 04-12-26.",
            "",
            "CONSEQUENCE:  it measures the RECESSION,",
            "so it will NOT close K.2 A2.  The design",
            "GWT (-)2.000 stays ASSUMED through",
            "construction and into service.",
            "",
            "AND THE PERMANENT WORKS ARE STILL",
            "BOUNDED.  B.3 already ran the flooded-",
            "to-grade case: the COMPLETED structure",
            "is FoS 1.41 against a requirement of",
            "1.2, WITH THE WATER AT GROUND LEVEL.",
            "",
            "WHAT IS EXPOSED IS THE CONSTRUCTION",
            "STAGE, and B.3's mandatory mitigation is",
            "now the operative control - continuous",
            "dewatering UNTIL BACKFILL AND COVER ARE",
            "COMPLETE, the six relief plugs, the",
            "monsoon sequence, symmetrical backfill.",
            "",
            "*** AND THE PROGRAMME DOES NOT DO THE",
            "FIRST OF THOSE.  A2070 ends 11-05-27;",
            "backfill A7010 is 20-07-27 to 30-07-27.",
            "The box stands un-backfilled through the",
            "2027 monsoon at FoS 1.22, 0.86 flooded.",
            "SG2-V5. ***",
        ]),
    ], gap=5.0)

    sh.finish(scale="1:25 AND NOT TO SCALE", sheet_of="5 OF 5")
    return sh.save(os.path.join(
        OUT, "SG-202_External_Works_Siting_and_Soak_Pit_Finding.dxf"))


def main():
    os.makedirs(OUT, exist_ok=True)
    print("SG2 drawings:")
    for f in (sg102(), sg202()):
        print("  " + os.path.basename(f))


if __name__ == "__main__":
    main()
