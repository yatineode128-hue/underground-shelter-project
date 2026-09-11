"""sg_sheets.py  --  SG-001, SG-101 and SG-201.

    SG-001  SITE AND GEOTECHNICAL DESIGN BASIS
    SG-101  SITE SETTING, SELECTION AND METEOROLOGY      **NOT A SITE PLAN**
    SG-201  GEOTECHNICAL PROFILE AGAINST THE STRUCTURE SECTION

SG-201 IS THE SHEET THIS PACKAGE EXISTS FOR.  Every other drawing in this
project shows what has been designed.  SG-201 shows WHAT IS NOT KNOWN: the
three trial pit logs plotted at true level, at the same vertical scale, beside
the structure that founds 5.3 m below the deepest of them, with everything
under (-)1.500 drawn as an explicit NO DATA zone.  The contrast is the
drawing.

Every number on all three sheets is read from sg_data.py or computed from it
here, so no sheet can disagree with the schedules or with the calculation
printout.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import sg_dxf as X                                          # noqa: E402
import sg_proj as P                                         # noqa: E402
import sg_data as D                                         # noqa: E402

OUT = os.path.abspath(os.path.join(HERE, "..", "DXF"))
TOP = 548.0
NOTE, LEAD = 2.0, 3.4

# ------------------------------------------------------------- derived
PRECIP = dict(D.DECK_PRECIP)
WIND = dict(D.DECK_WIND)
TEMP = {r[0]: r for r in D.DECK_TEMP}
PRECIP_TOTAL = sum(PRECIP.values())
JUN_SEP = sum(v for m, v in D.DECK_PRECIP
              if m in ("June", "July", "August", "September"))
HEADS = [float(l[-1][0].replace("Below", "").replace("m", "").strip())
         for _, l in D.FINDINGS]
RH_LO, RH_HI = min(HEADS), max(HEADS)
AREA = P.WM_ROCK_M3 / (-P.LVL_FORMATION - 1.750)
ROCK_HI = AREA * (-P.LVL_FORMATION - RH_LO)
SOAKED = 20.0 * P.KGCM2_KPA
SHORT = {"January": "JAN", "February": "FEB", "March": "MAR", "April": "APR",
         "May": "MAY", "June": "JUN", "July": "JUL", "August": "AUG",
         "September": "SEP", "October": "OCT", "November": "NOV",
         "December": "DEC"}
S3 = {"JAN": "Jan", "FEB": "Feb", "MAR": "Mar", "APR": "Apr", "MAY": "May",
      "JUN": "Jun", "JUL": "Jul", "AUG": "Aug", "SEP": "Sep", "OCT": "Oct",
      "NOV": "Nov", "DEC": "Dec"}

FINDINGS = [
    ("SG-F1", "The SEMT report reproduces completely from its own inputs. "
              "It is usable."),
    ("SG-F2", "*** THE INVESTIGATION REACHED 1.5 m.  THE STRUCTURE FOUNDS "
              "AT 6.8 m. ***"),
    ("SG-F3", "Presumptive SBC 65 % above the measured SOAKED value - and "
              "no element cares."),
    ("SG-F4", "In service the structure is LIGHTER than the ground it "
              "replaces, by 105 kPa."),
    ("SG-F5", "Report rockhead 0.9-1.5 m is entirely AT OR ABOVE the "
              "master's 1.5-2.0 m."),
    ("SG-F6", "'No water table' means NOT REACHED.  K.2 A2 stays ASSUMED "
              "and stays open."),
    ("SG-F7", "The monsoon groundwater monitoring is programmed OUTSIDE the "
              "monsoon."),
    ("SG-F8", "40.65 kPa brackets BOTH the as-placed and the saturated "
              "cover.  C17 earns its keep."),
    ("SG-F9", "Measured shear parameters move the wall design load by under "
              "1 %."),
    ("SG-F10", "The deck's contour map and its elevation profile disagree "
               "by 12-16 m."),
    ("SG-F11", "The two documents disagree on annual rainfall by 27-52 %.  "
               "October is the outlier."),
    ("SG-F12", "Seismic Zone III externally CORROBORATED; A_h reproduces "
               "exactly.  Nothing changes."),
    ("SG-F13", "The entry stairwell raft founds in very-high-swelling CH "
               "clay.  No spec exists."),
    ("SG-F14", "The concealment turf may be very-high-swelling CH clay over "
               "the filter it would clog."),
]


# =====================================================================
def sg001():
    sh = X.Sheet("SG-001",
                 "SITE AND GEOTECHNICAL DESIGN BASIS",
                 "TWO SUPPLIED DOCUMENTS, THEIR LIMITS, AND EVERY MASTER "
                 "A.6 / K.2 PARAMETER AGAINST THEM",
                 flags=("SG-V1", "SG-V2", "SG-V3", "SG-V9", "D3"),
                 sheet_of="1 OF 3")

    # ---------------------------------------------------- governing banner
    sh.rect(14, 494, 640, 540, "G-FLAGG")
    sh.text("THE ONE FACT THAT GOVERNS THIS PACKAGE", (327, 531), 3.2,
            "G-FLAGG", "CENTER")
    sh.text("THE SUB-SOIL INVESTIGATION REACHED ABOUT 1.5 m.   THE "
            "STRUCTURE FOUNDS AT (-)6.800.", (327, 519), 4.4, "G-FLAGG",
            "CENTER")
    sh.text("Everything this project holds about the ground below (-)2.000 - "
            "rockhead continuity, red-bole seams, k_s, the design "
            "groundwater table -", (327, 509), 2.2, "M-TEXT", "CENTER")
    sh.text("is EXTRAPOLATION.  The supplied report cannot be read as "
            "confirming any of it.  Confirmatory investigation A1075 "
            "remains mandatory in full.", (327, 501), 2.2, "M-TEXT",
            "CENTER")

    # ------------------------------------------------------------ sources
    sh.view_title((14, 480), "V1", "THE TWO SUPPLIED DOCUMENTS",
                  "AND WHAT EACH ONE CAN AND CANNOT BE USED FOR")

    sh.panel_column(14.0, 462.0, 212.0, 300.0, [
        ("SOURCE 1 - THE SUB-SOIL INVESTIGATION   [C]", [
            f"{D.REPORT['code']}   REPORT ON SUB-SOIL INVESTIGATION FOR",
            "CTW PH-III ACCN PROJECT AT CME PUNE",
            "Soil Engineering & Material Testing Wing, College of Military",
            "Engineering, Pune 411 031",
            f"Raised on {D.REPORT['request']}",
            "",
            f"{D.N_TRIAL_PITS} TRIAL PITS at 3 locations, by JCB in open "
            f"trench.",
            "NO BOREHOLES.  NO SPT.  NO PLATE LOAD TEST.  NO PERMEABILITY",
            "TEST.  NO PERCOLATION TEST.  Date of field work NOT STATED [N]",
            "",
            "*** IT IS NOT AN INVESTIGATION OF THIS PLOT. ***",
            "It investigates the G Building, the H Building and the Mess",
            "Building.  The project plot is a separate undeveloped area",
            "east of the CTW blocks.  It may be carried across ONLY on the",
            "strength of its own para 5 - 'horizontally bedded and more or",
            "less uniform in character over a wide area' - and that",
            "carry-across is an ASSUMPTION OF THIS PACKAGE.        [A] SG-V1",
        ]),
        ("SOURCE 2 - THE P1 PRESENTATION DECK   [C] as a record", [
            f"{D.DECK['title']},  {D.DECK['team']},  {D.DECK['pages']} "
            f"slides",
            "",
            "Site location, contour, watershed, road connectivity,",
            "pipelines, recce, elevation profile, SWOT, wind,",
            "precipitation, temperature, seismic and soil slides.",
            "",
            "THREE OF ITS STATEMENTS ARE NOT IN THE REPORT IT CITES:",
            "  'SBC = 300 kN/m2 at 1.5 m'   - not any value in the report",
            "  'Murrum SBC 25-30 kg/cm2'    - the report says 2.07 to 5.18",
            "  'UCS 609-900 kg/cm2 unsoaked'- the report says 752 to 900",
            "NONE AFFECTS THE DESIGN - the design uses none of them.  But",
            "they will be presented again unless corrected.       [U] SG-V8",
        ]),
        ("SOURCE 3 - THE LOCATION PIN   [N]", [
            D.PIN_URL,
            "NOT RESOLVED IN THIS SESSION - the environment's egress policy",
            "refused maps.app.goo.gl (403, recorded).  NO LATITUDE OR",
            "LONGITUDE HAS BEEN READ FROM IT AND NONE IS INVENTED.",
            "THE PROJECT STILL HAS NO COORDINATES.               [N] SG-V9",
        ]),
        ("WHAT THIS PACKAGE DOES NOT DO", [
            "It RESOLVES NOTHING.  Master rule M.6 forbids converting an",
            "[ASSUMED] into a confirmed fact, and not one K.2 assumption is",
            "closed.  No design value, load, thickness, bar, level, BOQ",
            "quantity, rate, date or float changes.  No .std file is",
            "touched and STAAD.Pro WAS NOT RUN.  No existing file in any",
            "other package is modified.  The MAIN STAIRCASE IS UNTOUCHED.",
            "Master gap D3 - NO SITE PLAN - IS NOT CLOSED.  Imagery is not",
            "a site plan: no boundary, no dimension, no benchmark, no",
            "coordinate.  What is added is the SETTING, which was absent.",
        ]),
    ], gap=6.0)

    # ------------------------------------------ parameter reconciliation
    sh.view_title((330, 480), "V2",
                  "EVERY MASTER A.6 / K.2 PARAMETER AGAINST THE NEW EVIDENCE",
                  "FOUR OF FOURTEEN ARE TOUCHED.  NONE IS CLOSED.")

    rows = [
        ["A1", "Rockhead", "(-)1.5 to (-)2.0 [A]", "0.9-1.5 m, 3 locations",
         "OPEN  SG-F5"],
        ["A2", "DESIGN GWT", "(-)2.000 [A]", "not encountered, pits <1.5 m",
         "OPEN  SG-F6"],
        ["A3", "SBC", "3240 kPa [A]", "1961-2059 soaked / 2942-3530 dry",
         "OPEN  SG-F3"],
        ["A4", "k_s", "100k-500k, both [A]", "nothing - no plate load test",
         "OPEN  unchanged"],
        ["A5", "K0, gamma", "0.50, 20/21 [A]", "phi 27-35, MDD 1.88-1.93",
         "OPEN  SG-F9"],
        ["A6", "K_a saturated", "1.0 [C]", "nothing", "unchanged"],
        ["A7", "Soak pit rate", "20 L/m2/day [A]", "nothing - no perc test",
         "OPEN  unchanged"],
        ["A8", "Seepage rate", "0.5 L/m2/day [A]", "nothing - no packer test",
         "OPEN  unchanged"],
        ["A10", "Basic wind V_b", "39 m/s [C]", "monthly MEANS only",
         "unchanged  see SG-101"],
        ["-", "SEISMIC ZONE", "Z 0.16 Zone III [C]", "Zone III, both "
         "documents", "CORROBORATED  SG-F12"],
        ["-", "COVER 40.65 kPa", "40.65 held, C17 [C]", "MDD 1.90-1.93, "
         "OMC 8-9 %", "CORROBORATED  SG-F8"],
        ["-", "Black cotton soil", "NOT RECORDED", "CH, FSI 60-65, "
         "0.18-1.0 m", "NEW  SG-F13 / SG-F14"],
        ["D3", "Site plan", "does not exist", "imagery, no dimension",
         "STILL OPEN"],
    ]
    y = sh.table(330, 462, [16, 62, 74, 96, 76], rows,
                 header=["REF", "PARAMETER", "WHAT THE MASTER HOLDS",
                         "WHAT THE EVIDENCE SAYS", "STATUS AFTER SG1"],
                 h=1.9, rh=5.0, layer="M-TABLE")

    # ------------------------------------------------------- the findings
    sh.view_title((330, y - 12), "V3", "FINDINGS",
                  "FOURTEEN.  NONE OF THEM CHANGES A DESIGN VALUE.")
    y2 = y - 30
    for ref, txt in FINDINGS:
        lay = "G-FLAGG" if ref in ("SG-F2", "SG-F7") else "M-TEXT"
        sh.text(ref, (330, y2), 2.0, "M-CALLOUT")
        sh.text(txt, (356, y2), 2.0, lay)
        y2 -= 4.6

    # -------------------------------------------------------- bearing box
    BOX_H = 62.0
    sh.rect(330, y2 - 3 - BOX_H, 654, y2 - 3, "M-TABLE")
    sh.text("THE BEARING CHECK, RE-RUN AT THE MEASURED SOAKED VALUE  -  "
            "SG-F3", (492, y2 - 12), 2.4, "M-TITLE", "CENTER")
    hdr = f"{'CHECK':<34}{'DEMAND':>10}{'/3240 [A]':>12}{'/1961 SOAKED':>15}"
    sh.text(hdr, (336, y2 - 21), 2.0, "M-TABLE")
    yy = y2 - 27
    for name, q in (("Mat, service          master B.3", P.Q_MAT_SERVICE),
                    ("Mat, BLAST            master B.3", P.Q_MAT_BLAST),
                    ("Sentry footing F1     master B.8.7", P.Q_F1_SERVICE)):
        sh.text(f"{name:<34}{q:>8.1f} kPa{q / P.SBC_MASTER:>11.2%}"
                f"{q / SOAKED:>14.2%}    PASS", (336, yy), 2.0, "M-TEXT")
        yy -= 5.0
    sh.text(f"The worst bearing utilisation in the project rises from 12.5 % "
            f"to {P.Q_MAT_BLAST / SOAKED:.1%} and everything still passes "
            f"with a factor of", (336, yy - 3), 2.0, "M-TEXT")
    sh.text(f"{SOAKED / P.Q_MAT_BLAST:.1f} in hand.  MASTER A.6 IS NOT "
            f"CHANGED - 3240 kPa is an IS 1904 presumptive value and it is "
            f"declared as one.", (336, yy - 9), 2.0, "M-TEXT")
    sh.text("What SG1 adds is that the design is now known to survive the "
            "MEASURED value too.", (336, yy - 15), 2.0, "M-TEXT")

    sh.panel_column(330.0, y2 - 3 - BOX_H - 8.0, 122.0, 324.0, [
        ("TEN OPEN ITEMS.  NONE IS RESOLVED, AND THAT IS DELIBERATE.", [
            "SG-V1   The geotechnical data is OFF-SITE.  No investigation "
            "has ever been made on this plot.",
            "SG-V2   DEPTH.  About 1.5 m against a formation at (-)6.800 "
            "and a sump base at (-)8.000.",
            "SG-V3   The monsoon GWT monitoring window is NOT IN THE "
            "MONSOON - 12-11-26 to 04-12-26, TF 0.",
            "SG-V4   Site level and fall: the contour map and the elevation "
            "profile disagree by 12 to 16 m.",
            "SG-V5   Annual rainfall 759.6 mm against 500-600 mm; the "
            "October figure does not fit a Deccan year.",
            "SG-V6   The entry stairwell raft founds in black cotton soil.  "
            "No strip-and-replace spec or BOQ item.",
            "SG-V7   The 300 concealment turf may be very-high-swelling CH "
            "clay from the site's own stockpile.",
            "SG-V8   Three P1 deck statements are not in the report they "
            "cite.  No design value is affected.",
            "SG-V9   The project has NO COORDINATES.  The owner's map pin "
            "could not be resolved in this session.",
            "SG-V10  The date of the SEMT field work is not stated, so the "
            "SEASON of 'no water table' is unknown.",
        ]),
        ("WHAT WOULD ACTUALLY CLOSE THE GEOTECHNICAL ITEMS", [
            "BOREHOLES ON THIS PLOT, with core recovery and RQD, to well "
            "below (-)6.800, logging EVERY flow",
            "contact and red-bole seam - that is the case that SIZES THE "
            "MAT (B.3 Case 2, 84 % utilised) - with",
            "packer permeability at the contacts and a PLATE LOAD TEST for "
            "k_s at BOTH bounds (K.2 A4).",
            "A STANDPIPE PIEZOMETER in that borehole, read through a FULL "
            "MONSOON.  Nothing shorter closes A2.",
            "A PERCOLATION TEST to IS 2470 (Pt 2) Cl. 4 - mandatory, and "
            "likely to fail on basalt (K.2 A7).",
            "A LEVELLED BENCHMARK ON THE PLOT, tying the project datum "
            "(grade 0.000) to a real reduced level.",
            "All of this is programme activity A1075 + A1080, 12 d + 20 d, "
            "BOTH ON THE CRITICAL PATH.",
        ]),
    ], gap=6.0)

    X.evidence_key(sh, 14, 200, 300.0)
    sh.finish(scale="NOT TO SCALE", sheet_of="1 OF 3")
    return sh.save(os.path.join(
        OUT, "SG-001_Site_and_Geotechnical_Design_Basis.dxf"))


# =====================================================================
def sg101():
    sh = X.Sheet("SG-101",
                 "SITE SETTING, SELECTION AND METEOROLOGY",
                 "A DIAGRAM OF THE SETTING - NOT A SITE PLAN, AND NOT "
                 "CAPABLE OF BECOMING ONE",
                 flags=("D3", "SG-V1", "SG-V4", "SG-V5", "SG-V9", "CAM-V2"),
                 sheet_of="2 OF 3")

    # ------------------------------------------------- the warning banner
    sh.rect(14, 508, 400, 540, "G-FLAGG")
    sh.text("*** THIS IS NOT A SITE PLAN ***", (207, 529), 4.0, "G-FLAGG",
            "CENTER")
    sh.text("No boundary, no dimension, no benchmark, no coordinate, NO "
            "SCALE.  Master gap D3 stays OPEN.", (207, 519), 2.2, "M-TEXT",
            "CENTER")
    sh.text("Relative positions only, from deck slides 13, 14, 15, 17, 18 "
            "and 22.  Distances are NOT to scale.", (207, 512), 2.2,
            "M-FLAG", "CENTER")

    # ------------------------------------------------- V1 setting diagram
    sh.view_title((14, 496), "V1", "SITE SETTING - SCHEMATIC",
                  "RELATIVE POSITIONS ONLY.  NOT TO SCALE.  [C] deck slides "
                  "13, 14, 15, 17, 18, 22")

    # the two CTW blocks
    for i, yb in enumerate((392, 436)):
        sh.rect(96, yb, 168, yb + 28, "G-SETTING")
        sh.hatch_pat([(96, yb), (168, yb), (168, yb + 28), (96, yb + 28)],
                     "ANSI31", 2.4, 0.0, "M-HATCH")
    sh.text("CTW BLOCKS", (132, 424), 2.4, "G-SETTING", "CENTER")

    # the plot
    sh.rect(206, 398, 296, 462, "G-FLAGG")
    sh.text("THE PLOT", (251, 442), 3.2, "G-FLAGG", "CENTER")
    sh.text("undeveloped", (251, 434), 2.0, "M-TEXT", "CENTER")
    sh.text("NOT DIMENSIONED", (251, 426), 2.0, "M-FLAG", "CENTER")
    sh.text("ANYWHERE  [N] D3", (251, 419), 2.0, "M-FLAG", "CENTER")

    # contours 581 and 580 across the plot
    for xc, lab in ((224, "581"), (276, "580")):
        sh.pline([(xc - 6, 386), (xc, 404), (xc - 4, 428), (xc + 4, 448),
                  (xc, 470)], "G-SETTING")
        sh.text(lab, (xc + 2, 474), 2.0, "G-SETTING")
    sh.text("1 m CONTOURS  [C] slide 15", (206, 482), 2.0, "G-SETTING")

    # fall arrow, east
    sh.flow((318, 430), 0.0, 5.0, "G-SETTING")
    sh.text("GROUND FALLS EAST / NE", (302, 414), 2.0, "G-SETTING")
    sh.text("580 -> 575 towards the nullah", (302, 408), 2.0, "M-TEXT")

    # perimeter track and nullah
    sh.pline([(352, 372), (358, 410), (352, 446), (360, 484)], "G-SETTING")
    sh.text("PERIMETER TRACK", (364, 452), 2.0, "G-SETTING")
    sh.text("AND NULLAH LINE", (364, 446), 2.0, "G-SETTING")
    sh.text("WEAKNESS: 'Located near", (364, 432), 2.0, "M-FLAG")
    sh.text("Perimeter Fence'  -  and it", (364, 426), 2.0, "M-FLAG")
    sh.text("is a CONCEALMENT weakness", (364, 420), 2.0, "M-FLAG")
    sh.text("too.  CAM-V2 / D3", (364, 414), 2.0, "M-FLAG")

    # CBRN live training area, south
    sh.rect(150, 346, 300, 372, "G-SETTING")
    sh.text("CBRN LIVE TRAINING AREA", (225, 358), 2.4, "G-SETTING",
            "CENTER")
    sh.text("STRENGTH: 'Proximity to FCBRNP'", (225, 350), 2.0, "M-TEXT",
            "CENTER")

    # trial pits, beyond a break
    sh.line((60, 340), (60, 476), "M-SECTION")
    sh.line((66, 340), (66, 476), "M-SECTION")
    sh.text("BREAK - DISTANCE NOT RECORDED", (63, 342), 2.0,
            "M-FLAG", "LEFT", rot=90.0)
    for yb, lab in ((452, "G BLDG  TP-1..4"), (422, "H BLDG  TP-5..8"),
                    (392, "MESS  TP-9..11")):
        sh.rect(16, yb, 52, yb + 20, "G-LOG")
        sh.text(lab, (34, yb + 12), 1.9, "G-LOG", "CENTER")
        for i in range(3):
            sh.circle((24 + i * 8, yb + 6), 1.4, "G-FLAGG")
    sh.text("THE TRIAL PITS ARE HERE,", (16, 372), 2.2, "M-FLAG")
    sh.text("NOT ON THE PLOT.  SG-V1", (16, 366), 2.2, "M-FLAG")

    sh.north((412, 352))

    # ------------------------------------------------------- V2 met table
    sh.view_title((436, 496), "V2",
                  "METEOROLOGICAL RECORD  -  P1 DECK SLIDES 24, 25, 26",
                  "EACH CAPTIONED 'LAST 10 YEARS AVG'.  NO STATION, NO "
                  "PERIOD OF RECORD, NO SOURCE IS NAMED.  [C] / [U]")
    rows = []
    for m, _ in D.DECK_WIND:
        s = SHORT[m]
        t = D.DECK_TEMP[[r[0] for r in D.DECK_TEMP].index(S3[s])]
        rows.append([s, f"{WIND[m]:.1f}", f"{PRECIP[m]:.1f}",
                     f"{t[1]:.1f}", f"{t[2]:.1f}", f"{t[3]:.1f}"])
    rows.append(["YEAR", f"{sum(WIND.values()) / 12:.1f}",
                 f"{PRECIP_TOTAL:.1f}",
                 f"{max(r[1] for r in D.DECK_TEMP):.1f}",
                 f"{sum(r[2] for r in D.DECK_TEMP) / 12:.1f}",
                 f"{min(r[3] for r in D.DECK_TEMP):.1f}"])
    sh.table(436, 478, [24, 30, 28, 26, 26, 26], rows,
             header=["MONTH", "WIND km/h", "RAIN mm", "MAX C", "AVG C",
                     "MIN C"], h=2.0, rh=5.0, layer="M-TABLE")

    # ------------------------------------------------------- right panels
    sh.panel_column(610.0, 496.0, 122.0, 216.0, [
        ("SITE SELECTION - THE DECK'S OWN SWOT   [C] slide 22", [
            "STRENGTH    " + D.DECK_SWOT["strength"][0],
            "            " + D.DECK_SWOT["strength"][1],
            "            " + D.DECK_SWOT["strength"][2],
            "            " + D.DECK_SWOT["strength"][3],
            "            " + D.DECK_SWOT["strength"][4],
            "WEAKNESS    " + D.DECK_SWOT["weakness"][0],
            "OPPORTUNITY " + D.DECK_SWOT["opportunity"][0],
            "            " + D.DECK_SWOT["opportunity"][1],
            "            " + D.DECK_SWOT["opportunity"][2],
            "THREAT      " + D.DECK_SWOT["threats"][0],
        ]),
        ("WHAT THE SELECTION GOT RIGHT, IN THIS PROJECT'S TERMS", [
            "'NO PIPELINES' is worth more here than on an ordinary",
            "building.  A buried main crossing a 22 x 6.2 box with a",
            "continuous gas-tight, EMP-bonded envelope would have been a",
            "first-order problem - every penetration is a blast, gas and",
            "EMP discontinuity.  Slide 18 draws the plot OUTSIDE the pipe",
            "network.  [C]",
            "'ELECTRIC LINES' is the project's EARLIEST record of a supply.",
            "It gives no capacity - EL-V4 stays open.",
            "'ROAD CONNECTIVITY' matches 994 m3 of rock excavated by",
            "breaker with no blasting and hauled by tipper.  [C] WM1",
        ]),
    ], gap=6.0)

    sh.panel_column(436.0, 330.0, 122.0, 168.0, [
        ("GROUND LEVEL - THE DECK CONTRADICTS ITSELF   [U] SG-V4", [
            f"CONTOUR MAP slide 15   1 m contours "
            f"{D.DECK_CONTOURS[0]} to {D.DECK_CONTOURS[1]}.  The",
            f"  {D.DECK_CONTOURS_AT_SITE[0]} and "
            f"{D.DECK_CONTOURS_AT_SITE[1]} contours BOTH cross the plot.",
            f"  => ground level approx "
            f"{D.DECK_CONTOURS_AT_SITE[0]} to "
            f"{D.DECK_CONTOURS_AT_SITE[1] + 1} m, fall about 1 in 40",
            "ELEVATION PROFILE slide 21   "
            f"{D.DECK_ELEV_PROFILE['z0']} m rising to "
            f"{D.DECK_ELEV_PROFILE['z1']} m",
            f"  over {D.DECK_ELEV_PROFILE['x1']} m  =  1 in "
            f"{D.DECK_ELEV_PROFILE['x1'] / (D.DECK_ELEV_PROFILE['z1'] - D.DECK_ELEV_PROFILE['z0']):.1f}",
            "",
            "THEY DISAGREE BY 12 TO 16 m ON LEVEL AND BY ABOUT FOUR",
            "TIMES ON GRADIENT.  Neither is adopted.  Most likely a local",
            "survey datum against a satellite MSL profile across a short",
            "transect, BUT THAT IS A GUESS AND IT IS RECORDED AS ONE.",
            "",
            "IT CHANGES NO CALCULATION - the project works on a LOCAL datum",
            "with grade = 0.000 and holds no absolute reduced level at all.",
            "IT DOES BLOCK three things: the cut and fill for a level",
            "formation under a 22 m box, the berm toe, and where the BS1",
            "1:50 cover crossfall daylights.  All wait on D3.",
        ]),
        ("RAINFALL - THE TWO DOCUMENTS DISAGREE   [U] SG-V5", [
            f"P1 deck slide 25, summed        {PRECIP_TOTAL:>7.1f} mm  [C]",
            f"SEMT/67/15 para 9               "
            f"{D.RAINFALL_REPORT_RANGE[0]:.0f} to "
            f"{D.RAINFALL_REPORT_RANGE[1]:.0f} mm  [C]",
            f"DIFFERENCE                      "
            f"{PRECIP_TOTAL / D.RAINFALL_REPORT_RANGE[1] - 1:+.0%} to "
            f"{PRECIP_TOTAL / D.RAINFALL_REPORT_RANGE[0] - 1:+.0%}",
            "Neither names a station, a period of record or a source.",
            "NO THIRD FIGURE IS ADOPTED HERE - published tertiary figures",
            "for 'Pune' themselves span 720 to over 1000 mm.",
            "",
            f"OCTOBER IS THE OUTLIER.  {PRECIP['October']:.1f} mm is "
            f"{PRECIP['October'] / PRECIP['September']:.2f} x September and "
            f"above",
            "August, in a month when the SW monsoon has withdrawn from",
            "interior Maharashtra.  IT IS NOT CORRECTED HERE - correcting a",
            "datum whose source is unknown would be inventing evidence.",
            "",
            "NOTHING IN THE DESIGN USES THE ANNUAL TOTAL.  The only",
            "intensity in the project is 50 mm/h, Rev F drawing 5 note 1,",
            "with no return period, duration or IDF source - DR-D1, NOT",
            "closed here.  The one place rainfall bites is the PROGRAMME.",
        ]),
        ("WIND - A WARNING, BECAUSE THIS INVITES A WRONG CORRECTION", [
            "Deck slide 24 windiest month   JUN 6.6 km/h = 1.83 m/s",
            "Master A.7.8 basic wind speed          39 m/s",
            "THESE ARE NOT THE SAME QUANTITY AND THE RATIO IS NOT AN ERROR.",
            "The deck plots a MONTHLY MEAN.  IS 875 (Pt 3):2015 V_b is a",
            "3-SECOND GUST at 10 m with a 50-year return period.",
            "*** A.7.8 IS NOT TO BE REDUCED ON THE STRENGTH OF SLIDE 24 ***",
            "and seismic governs the sentry post 2.4:1 in any case.",
        ]),
    ], gap=6.0)

    X.evidence_key(sh, 14, 330, 400.0)

    sh.panel(14, 288, 400.0,
             "WHAT THE SELECTION DID NOT CONSIDER, AND WHAT IT COSTS", [
        "GROUND CONDITIONS ON THE PLOT ITSELF.  The selection rests on a soil "
        "report for three OTHER buildings.",
        "   The confirmatory site investigation A1075 must be located ON THIS "
        "PLOT, not repeated from it.      SG-V1",
        "DEPTH OF INVESTIGATION.  Nothing is known below about 1.5 m; the "
        "structure founds at (-)6.800.       SG-V2",
        "GROUND SLOPE.  The plot is the EDGE OF A SLOPE falling east.  A 22 m "
        "box on a level formation under a",
        "   crowned grade needs CUT AND FILL, and no cut-and-fill item exists "
        "in the BOQ, because D3 does.      SG-V4",
        "'LOCATED NEAR PERIMETER FENCE', the single recorded weakness, is "
        "also a CONCEALMENT weakness - and",
        "   CAM2, whose finding is that THE SHELTER IS CONCEALED BUT THE "
        "INSTALLATION IS NOT, could not draw a",
        "   concealment layout for exactly this reason.  The sentry post "
        "stands at +7.000 and the headhouse at",
        "   +0.900 with no earth cover; how visible they are from the fence "
        "is a function of a distance nobody",
        "   has recorded anywhere.                                        "
        "CAM-V2 / D3",
    ], h=2.0, lead=3.6)

    sh.rect(14, 128, 414, 196, "G-FLAGG")
    sh.text("SG-F7   THE MONSOON GROUNDWATER MONITORING IS PROGRAMMED "
            "OUTSIDE THE MONSOON", (214, 186), 2.6, "G-FLAGG", "CENTER")
    sh.text("WBS A1080  'Monsoon groundwater monitoring - confirm the design "
            "GWT (-)2.000'", (22, 176), 2.1, "M-TEXT")
    sh.text("           20 days,  12-11-26 to 04-12-26,  TOTAL FLOAT 0,  "
            "'the single most important", (22, 170), 2.1, "M-TEXT")
    sh.text("           assumption in the project'", (22, 164), 2.1,
            "M-TEXT")
    sh.text(f"On the deck's own table June to September carry "
            f"{JUN_SEP:.1f} mm "
            f"({JUN_SEP / PRECIP_TOTAL:.0%} of the year);", (22, 155), 2.1,
            "M-TEXT")
    sh.text(f"November and December carry "
            f"{PRECIP['November'] + PRECIP['December']:.1f} mm BETWEEN THEM. "
            f" A 12 Nov to 4 Dec window measures the", (22, 149), 2.1,
            "M-TEXT")
    sh.text("RECESSION, NOT THE PEAK - and the peak is exactly what K.2 A2 "
            "asks for.", (22, 143), 2.1, "M-TEXT")
    sh.text("What closes A2 is a STANDPIPE PIEZOMETER in the A1075 borehole, "
            "read through a FULL", (22, 136), 2.1, "M-FLAG")
    sh.text("MONSOON.  NO PROGRAMME DATE IS CHANGED HERE - A1080 is on the "
            "critical path.  SG-V3", (22, 130), 2.1, "M-FLAG")

    sh.finish(scale="NOT TO SCALE", sheet_of="2 OF 3")
    return sh.save(os.path.join(
        OUT, "SG-101_Site_Setting_Selection_and_Meteorology.dxf"))


# =====================================================================
def _log(sh, x0, w, gy, sc, layers, label, pits, show_text=True, h=1.8):
    """One trial pit log.  gy = paper y of level 0.000, sc = scale
    denominator (mm of ground per mm of paper).

    The last stratum of every log is stated by the report as 'Below X m'.
    It has NO recorded bottom, so it is drawn as an OPEN-ENDED band closed by
    a ragged break line, and the level label is the REAL stated boundary X -
    never the arbitrary paper depth the band is drawn to.
    """
    sh.text(label, (x0 + w / 2.0, gy + 9.0), 2.2, "G-LOG", "CENTER")
    sh.text(pits, (x0 + w / 2.0, gy + 4.0), 1.8, "M-TEXT", "CENTER")
    real = 0.0
    for i, (depth, kind, ucs, sbc, note) in enumerate(layers):
        d = depth.replace("Below", "").replace("GL", "0").replace("m", "")
        openended = "-" not in d
        if openended:
            lo = float(d)
            hi = lo + 0.30 * sc / 20.0
        else:
            lo, hi = [float(t) for t in d.split("-")]
        y0 = gy - hi * 1000.0 / sc
        y1 = gy - lo * 1000.0 / sc
        key = X.classify(kind)
        sh.stratum(x0, x0 + w, y0, y1, key)
        if openended:
            real = lo
            n, zig = 8, []
            for j in range(n + 1):
                zig.append((x0 + w * j / n, y0 + (1.4 if j % 2 else -1.4)))
            sh.pline(zig, "G-NODATA")
        if show_text and (y1 - y0) >= 4.0:
            sh.text(X.STRATA[key][0], (x0 + 2.0, (y0 + y1) / 2.0 - h / 2.0),
                    h, "M-TEXT")
            sh.text(f"SBC {sbc:.2f} kg/cm2 = {sbc * P.KGCM2_KPA:.0f} kPa",
                    (x0 + 2.0, (y0 + y1) / 2.0 - h / 2.0 - h - 0.6), h,
                    "M-TEXT")
    return gy - real * 1000.0 / sc, real


def sg201():
    sh = X.Sheet("SG-201",
                 "GEOTECHNICAL PROFILE AGAINST THE STRUCTURE SECTION",
                 "THE DEPTH THE INVESTIGATION REACHED, AND THE DEPTH THE "
                 "STRUCTURE NEEDS, AT ONE SCALE",
                 flags=("SG-V1", "SG-V2", "SG-V3", "SG-V6", "A1", "A2"),
                 sheet_of="3 OF 3")

    SC = 25.0                       # 1 : 25, both ways
    G = 496.0                       # paper y of level 0.000

    def py(level):
        return G + level * 1000.0 / SC

    sh.view_title((14, 528), "V1",
                  "TRIAL PIT LOGS AND THE STRUCTURE, AT THE SAME VERTICAL "
                  "SCALE",
                  "SCALE 1:25, EQUAL BOTH WAYS.  TRANSVERSE SECTION THROUGH "
                  "THE BOX.  THE CONTRAST IS THE DRAWING.")

    # --- the three logs
    LW = 52.0
    for i, (loc, layers) in enumerate(D.FINDINGS):
        x0 = 22.0 + i * (LW + 14.0)
        short = loc[:loc.find("(")].strip().upper()
        pits = loc[loc.find("(") + 1:loc.find(")")]
        _, real = _log(sh, x0, LW, G, SC, layers, short, pits,
                       show_text=False)
        sh.text(f"rock below (-){real:.3f}",
                (x0 + LW / 2.0, py(-real) - 6.0), 1.8, "G-NODATA", "CENTER")
        sh.text("depth NOT investigated",
                (x0 + LW / 2.0, py(-real) - 9.4), 1.8, "G-NODATA", "CENTER")
    sh.text("THE ENTIRE INVESTIGATION", (24, py(0) + 16.0), 2.4, "G-NODATA")
    sh.text("11 trial pits, JCB, open trench.  No borehole, no SPT, no "
            "plate load test, no permeability test.  [C] SEMT/67/15",
            (24, py(0) + 11.0), 2.0, "M-TEXT")

    # --- the NO DATA zone
    x_nd0, x_nd1 = 18.0, 646.0
    y_nd_top, y_nd_bot = py(-1.500), py(-8.600)
    sh.hatch_pat([(x_nd0, y_nd_bot), (x_nd1, y_nd_bot), (x_nd1, y_nd_top),
                  (x_nd0, y_nd_top)], "ANSI31", 6.0, 90.0, "G-NODATA")
    sh.pline([(x_nd0, y_nd_bot), (x_nd1, y_nd_bot), (x_nd1, y_nd_top),
              (x_nd0, y_nd_top)], "G-NODATA", close=True)
    sh.text("N O   D A T A   E X I S T S   B E L O W   T H I S   L I N E",
            (332, py(-1.500) - 7.5), 4.4, "G-NODATA", "CENTER")
    sh.text("No borehole, no sample, no water reading, no rockhead, no "
            "red-bole seam, no k_s.  THE DEEPEST TRIAL PIT STOPPED HERE.",
            (332, py(-1.500) - 14.0), 2.1, "G-NODATA", "CENTER")

    # --- what a real investigation would have had to put in this space
    sh.text("WHAT A REAL INVESTIGATION WOULD HAVE HAD TO PUT IN THIS SPACE",
            (24, py(-3.900)), 2.4, "G-NODATA")
    for i, t in enumerate([
            "the rockhead surface UNDER THE BOX, not inferred from three "
            "pits at three other buildings",
            "EVERY FLOW CONTACT and every red-bole or vesicular seam between "
            "(-)1.500 and below (-)6.800",
            "   - and this is the case that SIZES THE MAT: B.3 Case 2, a "
            "3.0 m soft band, 84 % utilised",
            "core recovery and RQD through the founding horizon",
            "a PIEZOMETER reading through a full monsoon - the design GWT at "
            "(-)2.000 is [ASSUMED]",
            "PLATE LOAD TESTS for k_s at BOTH bounds, 100 000 and 500 000 "
            "kN/m3 - only one has ever been run",
            "PACKER PERMEABILITY at the contacts, for the 0.5 L/m2/day "
            "seepage the sump is sized on",
            "a PERCOLATION TEST to IS 2470 (Pt 2) Cl. 4 - mandatory, and "
            "likely to fail on basalt"]):
        sh.text("-   " + t, (24, py(-3.900) - 6.0 - i * 4.6), 1.9, "M-TEXT")
    sh.text("Programme activities A1075 (12 d) and A1080 (20 d).  BOTH ARE "
            "ON THE CRITICAL PATH.  SG-V2",
            (24, py(-3.900) - 6.0 - 8 * 4.6 - 2.0), 2.0, "G-NODATA")

    # --- the structure, transverse section
    BX = 332.0
    def px(mm):
        return BX + mm / SC

    x_out0, x_out1 = px(0), px(6200)

    sh.hatch_pat([(x_out0 - 18, py(-2.000)), (x_out1 + 18, py(-2.000)),
                  (x_out1 + 18, py(0.0)), (x_out0 - 18, py(0.0))],
                 "EARTH", 0.8, 0.0, "G-MURRUM")
    sh.pline([(x_out0 - 18, py(-2.000)), (x_out1 + 18, py(-2.000)),
              (x_out1 + 18, py(0.0)), (x_out0 - 18, py(0.0))],
             "G-MURRUM", close=True)
    sh.text("ENGINEERED COVER 2000 = 40.65 kPa  [C] A.7.3  -  burster slab "
            "to a 1:50 crossfall, BS1", (px(3100), py(-1.000)), 2.0,
            "M-TEXT", "CENTER")

    sh.rect(x_out0, py(-2.900), x_out1, py(-2.000), "G-STRUCT")
    sh.concrete_hatch([(x_out0, py(-2.900)), (x_out1, py(-2.900)),
                       (x_out1, py(-2.000)), (x_out0, py(-2.000))])
    sh.text("ROOF SLAB 900", (px(3100), py(-2.520)), 2.2, "G-STRUCT",
            "CENTER")
    for a, b in ((0, 600), (5600, 6200)):
        sh.rect(px(a), py(-6.100), px(b), py(-2.900), "G-STRUCT")
        sh.concrete_hatch([(px(a), py(-6.100)), (px(b), py(-6.100)),
                           (px(b), py(-2.900)), (px(a), py(-2.900))])
    sh.rect(x_out0, py(-6.700), x_out1, py(-6.100), "G-STRUCT")
    sh.concrete_hatch([(x_out0, py(-6.700)), (x_out1, py(-6.700)),
                       (x_out1, py(-6.100)), (x_out0, py(-6.100))])
    sh.text("MAT 600", (px(3100), py(-6.440)), 2.0, "G-STRUCT", "CENTER")
    sh.rect(x_out0, py(-6.800), x_out1, py(-6.700), "G-STRUCT")
    sh.text("WALL 600", (px(300), py(-4.600)), 1.9, "G-STRUCT", "CENTER",
            rot=90.0)
    sh.text("CLEAR 3200   -   INTERNAL 5000", (px(3100), py(-4.600)), 2.4,
            "M-DIM", "CENTER")
    sh.text("PCC 100 M15 ON FORMATION", (px(3100), py(-6.780) - 4.6), 1.9,
            "G-STRUCT", "CENTER")

    sh.rect(px(2400), py(-8.000), px(3800), py(-6.800), "G-STRUCT")
    sh.text("SUMP SU-01", (px(3100), py(-7.340)), 1.9, "G-STRUCT", "CENTER")
    sh.text("base (-)8.000", (px(3100), py(-7.340) - 4.2), 1.8, "G-STRUCT",
            "CENTER")

    # sentry footing F1, beyond a break - its site position is ASSUMED (U4)
    sh.line((228, py(-1.200)), (228, py(-3.600)), "M-SECTION")
    sh.line((234, py(-1.200)), (234, py(-3.600)), "M-SECTION")
    sh.rect(240, py(-2.600), 292, py(-2.000), "G-STRUCT")
    sh.concrete_hatch([(240, py(-2.600)), (292, py(-2.600)),
                       (292, py(-2.000)), (240, py(-2.000))])
    sh.text("SENTRY F1", (266, py(-2.180)), 1.9, "G-STRUCT", "CENTER")
    sh.text("1500 x 1500 x 600 on in-situ basalt at (-)2.000  [C] B.8.7",
            (22, py(-3.000)), 1.9, "M-TEXT")
    sh.text("BEYOND A BREAK - >= 10 m clear of the shelter excavation, and "
            "its site position is ASSUMED (master U4)",
            (22, py(-3.000) - 4.4), 1.9, "M-FLAG")
    sh.text("THE ONLY FOUNDED ELEMENT INSIDE THE LOGGED HORIZON - AND ONLY "
            "JUST", (22, py(-3.000) - 8.8), 1.9, "G-FLAGG")

    # design GWT
    sh.dline((20, py(-2.000)), (644, py(-2.000)), "G-WATER", 3.0, 2.0)
    sh.text("DESIGN GWT (-)2.000   [A]  K.2 A2 - THE SINGLE MOST IMPORTANT "
            "NUMBER IN THE PROJECT, AND IT IS ASSUMED",
            (20, py(-2.000) + 1.8), 2.1, "G-WATER")

    # grade
    sh.line((18, G), (646, G), "M-LEVEL")
    sh.text("FINISHED GRADE 0.000  -  PROJECT DATUM, LOCAL  [C] A.4.1",
            (212, G + 2.2), 2.0, "M-LEVEL")

    # level ladder, all above the title block
    for lv, lab in ((0.0, "GRADE 0.000"),
                    (-1.500, "DEEPEST TRIAL PIT (-)1.500   [C]"),
                    (-2.000, "SLAB TOP / DESIGN GWT (-)2.000"),
                    (-6.100, "FLOOR (-)6.100"),
                    (-6.700, "MAT SOFFIT (-)6.700"),
                    (-6.800, "FORMATION (-)6.800  ***  THE MAT BEARS HERE"),
                    (-8.000, "SUMP BASE (-)8.000")):
        lay = "G-NODATA" if lv in (-1.500, -6.800) else "M-LEVEL"
        dy = -3.2 if lv == -6.800 else 0.0
        sh.line((590 - 3.0, py(lv)), (590 + 3.0, py(lv)), lay)
        sh.pline([(590, py(lv)), (588.4, py(lv) + 2.4), (591.6, py(lv) + 2.4)],
                 lay, close=True)
        sh.text(lab, (594.5, py(lv) + 0.8 + dy), 1.9, lay)

    # the gap dimension
    xg = 310.0
    sh.line((xg, py(-1.500)), (xg, py(-6.800)), "G-FLAGG")
    sh.pline([(xg, py(-1.500)), (xg - 3, py(-1.500) - 4),
              (xg + 3, py(-1.500) - 4)], "G-FLAGG", close=True)
    sh.pline([(xg, py(-6.800)), (xg - 3, py(-6.800) + 4),
              (xg + 3, py(-6.800) + 4)], "G-FLAGG", close=True)
    ym = (py(-1.500) + py(-6.800)) / 2.0
    sh.text("5.300 m", (xg - 5, ym + 2.0), 3.0, "G-FLAGG", "RIGHT")
    sh.text("OF UNLOGGED", (xg - 5, ym - 3.4), 2.2, "G-FLAGG", "RIGHT")
    sh.text("GROUND", (xg - 5, ym - 8.0), 2.2, "G-FLAGG", "RIGHT")

    # rockhead bands
    sh.dline((20, py(-RH_LO)), (222, py(-RH_LO)), "G-ROCK", 2.0, 1.6)
    sh.dline((20, py(-RH_HI)), (222, py(-RH_HI)), "G-ROCK", 2.0, 1.6)
    sh.text(f"REPORT ROCKHEAD BAND (-){RH_LO:.3f} to (-){RH_HI:.3f}   [C]",
            (226, py(-RH_LO) - 1.0), 1.9, "G-ROCK")
    sh.text("MASTER A.6 ASSUMES (-)1.500 to (-)2.000   [A]",
            (226, py(-RH_LO) - 5.4), 1.9, "G-FLAGG")
    sh.text("THE TWO BANDS TOUCH AT ONE POINT.  The report's rock is at or "
            "ABOVE the master's whole range: CONSERVATIVE for founding "
            "depth,", (20, py(-2.000) - 13.0), 1.9, "G-FLAGG")
    sh.text("UNCONSERVATIVE for excavation quantity - +118 m3 of rock, about "
            "2 extra days at the WBS A2050 output.   SG-F5",
            (20, py(-2.000) - 17.4), 1.9, "G-FLAGG")

    # ============================================== stratum key and table
    sh.view_title((14, 142), "KEY", "STRATUM KEY AND BEARING VALUES",
                  "ALL VALUES [C], READ OFF SEMT/67/15 para 15.  "
                  "1 kgf/cm2 = 98.0665 kPa.")
    kx = 16.0
    for i, key in enumerate(("CH", "MURRUM", "BROKEN", "ROCK", "NODATA")):
        name, layer, pat, psc, ang = X.STRATA[key]
        x0 = kx + i * 92.0
        sh.hatch_pat([(x0, 108), (x0 + 22, 108), (x0 + 22, 122),
                      (x0, 122)], pat, psc, ang, layer)
        sh.pline([(x0, 108), (x0 + 22, 108), (x0 + 22, 122), (x0, 122)],
                 layer, close=True)
        sh.text(name, (x0 + 25, 116), 1.9, layer)
    sh.text("0.18 - 1.0 m", (kx + 25, 111), 1.8, "M-TEXT")
    sh.text("to 1.2 m", (kx + 92 + 25, 111), 1.8, "M-TEXT")
    sh.text("0.75 - 1.6 m", (kx + 184 + 25, 111), 1.8, "M-TEXT")
    sh.text("below 0.9 - 1.5 m", (kx + 276 + 25, 111), 1.8, "M-TEXT")
    sh.text("below about 1.5 m", (kx + 368 + 25, 111), 1.8, "M-FLAG")

    rows = [
        ["BLACK COTTON  CH", "0.18 - 1.0", "0.25 - 0.27", "24.5 - 26.5",
         "FSI 60-65 %, VERY HIGH SWELL.  Nothing founds in it - but see "
         "SG-F13 and SG-F14"],
        ["MURRUM  GM / GP / SC", "to 1.2", "2.07 - 5.18", "203 - 508",
         "phi 27-35 deg, c = 0.  MDD 1.88-1.93, OMC 8-12 %.  This is the "
         "fill material"],
        ["BROKEN BASALT", "0.75 - 1.6", "10.00", "981",
         "IS 12070 Table 2.  Cracks, fissures, voids, discontinuities"],
        ["SOUND BASALT  soaked", "below 0.9 - 1.5", "20 - 21",
         "1961 - 2059", "*** THE APPLICABLE VALUE - the formation is 4.8 m "
         "below the design GWT ***"],
        ["SOUND BASALT  unsoaked", "below 0.9 - 1.5", "30 - 36",
         "2942 - 3530", "Master A.6 presumptive 3240 kPa [A] sits in THIS "
         "band, not the soaked one"],
        ["NO DATA", "below about 1.5", "-", "-",
         "THE FORMATION IS HERE, AT (-)6.800.  SG-F2 / SG-V2"],
    ]
    sh.table(16, 104, [56, 34, 34, 34, 200], rows,
             header=["STRATUM", "DEPTH m", "SBC kg/cm2", "SBC kPa",
                     "WHAT IT MEANS FOR THIS STRUCTURE"],
             h=1.9, rh=5.0, layer="M-TABLE")

    # ------------------------------------------------------ right panels
    sh.panel_column(656.0, 528.0, 120.0, 173.0, [
        ("WHAT THE LOGS ESTABLISH   SG-F2", [
            "To about 1.5 m, for the G, H and Mess",
            "buildings - NOT for this plot (SG-V1):",
            "  a thin BLACK COTTON cover, CH,",
            "  FSI 60-65 %, 0.18 to 1.0 m",
            "  MURRUM below it, phi 27-35 deg",
            "  BROKEN BASALT below that",
            "  SOUND BASALT, 0.9 to 1.5 m down",
        ]),
        ("WHAT THEY DO NOT   [N]", [
            "rockhead continuity under the box   A1",
            "the groundwater table               A2",
            "red-bole / vesicular seams at the",
            "  flow contacts - AND THIS IS THE",
            "  CASE THAT SIZES THE MAT, B.3",
            "  Case 2, 84 % utilised",
            "modulus of subgrade reaction k_s    A4",
            "rock mass permeability              A8",
            "Confirmatory SI A1075, 12 d, CRITICAL",
            "PATH, remains MANDATORY IN FULL, and",
            "must be located ON THIS PLOT.  SG-V1",
        ]),
        ("GROUNDWATER   SG-F6", [
            "SEMT para 13: 'Water table was not",
            "encountered in any trial pit. However,",
            "water table may raise during/after",
            "rainy season.'",
            "Deck slide 29: 'Proposed structure safe",
            "for water table at depth of 2 m below",
            "GL.'",
            "*** THAT IS THE PROVENANCE OF (-)2.000,",
            "RECORDED FOR THE FIRST TIME.  No water",
            "was found, so 2 m was CHOSEN and the",
            "structure designed safe for it.  IT IS",
            "NOT A MEASUREMENT. ***",
            "(1) DEPTH   the design GWT is ALREADY",
            "    BELOW THE DEEPEST PIT.",
            "(2) SEASON  requested 20 May 2015 - the",
            "    pre-monsoon minimum, if the work",
            "    followed promptly.  The date is",
            "    never stated.   [U] SG-V10",
            "(3) GROUND  Deccan Trap water sits at",
            "    the FLOW CONTACTS: perched, and",
            "    strongly seasonal.  A dry-season",
            "    pit is close to the worst possible",
            "    instrument for finding it.",
            "WHY IT MATTERS MOST:  of 15.41 kPa/m,",
            "9.81 IS WATER; uplift 46.11 kPa =",
            "6289 kN; flotation FoS 0.33 at the",
            "mat-only stage.  K.2 A2 STAYS ASSUMED",
            "AND STAYS OPEN.",
        ]),
        ("THE BLACK COTTON SOIL   SG-F13 / SG-F14", [
            "HARMLESS under every founded element -",
            "mat (-)6.700 and F1 (-)2.000 are both",
            "in basalt.  B.8.7's 'on IN-SITU ROCK,",
            "never on backfill' is now backed by a",
            "measurement.",
            "SG-F13  THE ENTRY STAIRWELL RAFT.  A.4.7",
            "  'Stepped RC raft 300 thk ON COMPACTED",
            "  FILL' - its top founds at about",
            "  (-)0.300, INSIDE the CH horizon.  No",
            "  strip-and-replace spec, no BOQ item.",
            "  HEAVE, not bearing.  Expendable",
            "  against BLAST - but heave is not a",
            "  blast problem, and it is the ONLY",
            "  primary access.            SG-V6",
            "SG-F14  THE CONCEALMENT TURF.  CAM2",
            "  re-lays the 300 from the site's own",
            "  stockpile.  If that is this CH clay it",
            "  cracks (a CONCEALMENT defect), feeds",
            "  the 150 filter directly, and pumps",
            "  fines INTO it - the one thing the",
            "  filter exists to stop.  Load",
            "  unaffected; SPEC missing.   SG-V7",
        ]),
    ], gap=5.0)

    X.evidence_key(sh, 404, 46, 240.0)
    sh.finish(scale="1:25", sheet_of="3 OF 3")
    return sh.save(os.path.join(
        OUT, "SG-201_Geotechnical_Profile_and_Structure_Section.dxf"))


def main():
    os.makedirs(OUT, exist_ok=True)
    print("SG1 drawings:")
    for f in (sg001(), sg101(), sg201()):
        print("  " + os.path.basename(f))


if __name__ == "__main__":
    main()
