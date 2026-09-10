"""g00_general.py  --  R-001 to R-004, the general sheets."""
import os, math
import sc_proj as P
import sc_dxflib as D
import sc_views as V
import rebar_data as R
from sc_dxflib import Sheet, vw, TXT

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "DXF", "General"))


def r001():
    sh = Sheet("R-001", "GENERAL REINFORCEMENT NOTES",
               "MATERIALS · COVER · ANCHORAGE · LOADING · LIMITATIONS",
               flags=["C16", "C17"])
    sh.sheet_header()
    # QA1 layout: the three note columns are laid out with panel_column so that
    # they FILL the sheet height.  Previously every panel was drawn at the
    # library minimum (1.4 mm text, 3.2 mm pitch), which left the bottom third
    # of the sheet empty and the body text below legible print size.
    sh.panel_column(16, 550, 16, 300, [
        ("GENERAL NOTES", V.STD_NOTES),
        ("DESIGN BASIS - GOVERNING ACTION PER ELEMENT", [
        "COMB 103 BLAST GOVERNS EVERY BLAST-RATED ELEMENT.",
        "",
        "MAT 600            soft / red-bole band, M = qL2/12 = 303.7 kNm/m     util 84 %",
        "PERIMETER WALLS    Mp = w Ln2/16 = 245.1 kNm/m                        util 68 %",
        "WALLS W6 / W7 400  Mp = 245.1 kNm/m  (shaft equalises to full p_so)   util 69 %",
        "ROOF SLAB 900      Mp = 700.2 kNm/m                                   util 51 %",
        "ROOF CANTILEVER    M(root) = 758.6 kNm/m  - EXCEEDS THE MIDSPAN Mp    util 56 %",
        "HEADHOUSE ROOF 500 Mp = 396.5 kNm/m                                   util 90 %",
        "HEADHOUSE WALLS    Mp = 137.9 kNm/m, 383 kPa EITHER FACE              util 59 %",
        "",
        "MAIN STAIRCASE and ENTRY STAIRWELL are NOT blast elements.  They are",
        "designed to IS 456 with NORMAL partial factors, NOT with IS 4991",
        "dynamic strengths.  The entry stairwell is OUTSIDE the protective",
        "boundary and is DECLARED EXPENDABLE.",
        "",
        "PROTECTIVE BOUNDARY = BLAST DOORS 1 AND 2 AT (-)6.100, WALLS W6/W7,",
        "THE PERIMETER WALLS, THE MAT AND THE PRESSURE SLAB.",
        ]),
        ("WHAT THIS PACKAGE DOES NOT DEMONSTRATE", [
        "1  SUPPORT ROTATION / DUCTILITY FOR THE BLAST CASE.  mu = 5 needs a",
        "   non-linear SDOF check (IS 4991 Fig. 6 / Biggs).  PHASE 3.",
        "2  SHOCK PROPAGATION DOWN THE ENTRY SHAFT and the resulting door loading.",
        "3  TRANSIENT SOIL-STRUCTURE INTERACTION.",
        "4  BLAST DOOR, VALVE AND HATCH PERFORMANCE - vendor-tested, not a civil item.",
        "5  GLOBAL FLOTATION cannot be shown by an elastic-mat model: the springs",
        "   take tension, so the mat never lifts in the model.  It is a HAND CHECK.",
        "   THE CONSTRUCTION STAGE GOVERNS - FoS 0.33 AT THE MAT-ONLY STAGE.",
        "6  CRACK WIDTH is satisfied by the IS 3370 surface-zone steel rule, not",
        "   by calculation.",
        "7  NO CODE DOCUMENT IS HELD.  Clause numbers are cited only from the",
        "   project's verified clause register (master Part G).",
        ]),
        ("CODES RELIED ON", [
        "IS 456:2000        all capacity, detailing, cover, Ld, laps, shear",
        "IS 1786:2008       Fe500D",
        "IS 3370 (1,2):2021 0.2 mm crack limit; 0.35 % surface-zone steel",
        "IS 875 (1,2,5)     dead, imposed, combination",
        "IS 1893 (Pt 1):2016 seismic - established as NOT governing",
        "IS 13920:2016      applicability determined element by element;",
        "                   Cl. 10.4 checked and NOT triggered",
        "IS 4991:1968       BLAST LOADING RULES AND DYNAMIC STRENGTHS ONLY",
        "IS 1904 · IS 2950(1) · IS 12070   bearing, raft, rock",
        "SP 34:1987         detailing; Cl. 5.5 opening corner",
        "NBC 2016 Part 4    stair geometry, 1100 guarding",
        "SP 16 · BS 8666 · UFC 3-340-02 (cited AS US criteria)",
        "",
        "IS 2502 IS NAMED IN THE BRIEF BUT IS NOT HELD AND IS NOT CITED.",
        "Bar bending uses declared project rule PBR-1 - see R-004.",
        ]),
    ])

    x = 324
    rows = [f"{n:<4} {t:<26} {f}" for n, t, f in P.COMBS]
    sh.panel_column(x, 550, 16, 300, [
        (V.MATERIALS_HEAD, V.materials_lines()),
        (V.LOADING_HEAD, [
        "BLAST   p_so 344.7 kPa (50 psi) · td 0.13-1.33 s · mu 5 · DLF 1.111",
        "        DESIGN 383 kPa ON THE ROOF AND ON THE WALLS  (Ka = 1.0)",
        "        Roof T = 13.4 ms, td/T = 10-100  ->  QUASI-STATIC",
        "",
        "ROOF COMB 103 TOTAL   383.00 blast + 40.65 cover + 2.00 SIDL",
        "                      + 22.50 self = 448.15 kPa",
        "        NO LIVE LOAD ON THE ROOF AT BLAST - IS 4991 Cl. 11.2",
        "        Static ULS 101 = 127.7 kPa -> BLAST GOVERNS 3.51 : 1",
        "",
        "EARTH + WATER   K0.gamma' + gamma_w = 15.41 kPa/m",
        "                33.9 at the soffit, 83.2 kPa at the floor",
        "UPLIFT          4.700 x 9.81 = 46.11 kPa = 6289 kN over 136.4 m2",
        "HEADHOUSE       roof 396.5 kPa · walls 383 kPa EITHER FACE (C10)",
        "SEISMIC         box Ah 0.075, Vb 1050 kN, wall tau 0.063 N/mm2",
        "                NEGLIGIBLE.  IS 13920 Cl. 10.4 NOT TRIGGERED.",
        "                WIND AND EARTHQUAKE ARE ABSENT FROM COMB 103",
        "                - IS 4991 Cl. 11.1 FORBIDS COMBINING THEM WITH BLAST.",
        "",
        "LOAD COMBINATIONS (as built into the STAAD models):",
        ] + rows),
        (V.OPEN_ITEMS_HEAD,
         V.open_items_lines(["C16", "C17", "A2", "A4", "M1", "M2", "P3"])),
    ])

    # right column stops at 118 so it never crowds the title block (y 10-110)
    x = 634
    sh.panel_column(x, 550, 118, 197, [
        ("BAR MARK SYSTEM", [
        "F   FOUNDATIONS - mat, starters, sump pit",
        "W   WALLS - perimeter, W5, W6/W7, openings",
        "S   SLAB - pressure (roof) slab and its openings",
        "B   BEAM-TYPE ELEMENTS - headers, bands, lintels",
        "ST  MAIN STAIRCASE",
        "H   HEADHOUSE",
        "E   ENTRANCE / COVERED ENTRY STAIRWELL",
        "",
        "C  IS RESERVED FOR COLUMNS AND IS DELIBERATELY UNUSED:",
        "T  IS RESERVED AND UNUSED.",
        "",
        "THERE ARE NO RC COLUMNS, NO FRAMED BEAMS AND NO BEAM-COLUMN",
        "JOINTS IN THE UNDERGROUND SHELTER.  The box is a monolithic",
        "plate structure - mat, walls, roof slab.  Master B.3 declares",
        "punching shear NOT APPLICABLE because no column or pedestal",
        "bears on the mat.  No column or joint drawing is produced.",
        ]),
        ("DRAWING INDEX - THIS PACKAGE", [
        "R-001 GENERAL REINFORCEMENT NOTES",
        "R-002 REINFORCEMENT LEGEND AND SYMBOLS",
        "R-003 TYPICAL REINFORCEMENT DETAILS AND BAR SHAPES",
        "R-004 REINFORCEMENT SCHEDULE",
        "R-101 MAT FOUNDATION REINFORCEMENT PLAN",
        "R-102 MAT FOUNDATION SECTIONS",
        "R-103 FOUNDATION / WALL JUNCTION DETAILS",
        "R-201 EXTERNAL WALL REINFORCEMENT",
        "R-202 INTERNAL WALL REINFORCEMENT",
        "R-203 WALL ELEVATIONS",
        "R-204 WALL SECTIONS",
        "R-205 OPENING REINFORCEMENT DETAILS",
        "R-301 ROOF / PRESSURE SLAB REINFORCEMENT PLAN",
        "R-302 ROOF SECTIONS",
        "R-303 ROOF OPENING DETAILS",
        "R-304 ROOF / WALL JUNCTION DETAILS",
        "R-401 BEAM-TYPE ELEMENT LOCATION PLAN",
        "R-402 BEAM-TYPE ELEMENT REINFORCEMENT DETAILS",
        "R-601 MAIN STAIRCASE REINFORCEMENT PLAN",
        "R-602 MAIN STAIRCASE SECTIONS",
        "R-603 ENTRY STAIRWELL REINFORCEMENT",
        "R-604 STAIR CONNECTION DETAILS",
        "R-701 HEADHOUSE REINFORCEMENT",
        "R-702 ENTRANCE REINFORCEMENT",
        "R-703 BLAST-DOOR AND OPENING DETAILS",
        "R-801 ANCHORAGE AND DEVELOPMENT",
        "R-802 LAP AND SPLICE DETAILS",
        "R-803 WALL / SLAB CONNECTIONS",
        "R-804 CONSTRUCTION JOINTS",
        "R-805 WATERPROOFING / STRUCTURAL INTERFACE",
        "",
        "NO R-501 / R-502 / R-503 (COLUMNS) - NO COLUMN EXISTS.",
        "NO SENTRY-POST DRAWING - OUT OF SCOPE.",
        ]),
    ])
    sh.titleblock(scale="NOT TO SCALE", sheet_of="1 OF 30")
    return sh.save(os.path.join(OUT, "R-001_General_Reinforcement_Notes.dxf"))


def r002():
    sh = Sheet("R-002", "REINFORCEMENT LEGEND AND SYMBOLS",
               "LAYERS · LINE HIERARCHY · BAR REPRESENTATION · TEXT STANDARDS")
    sh.sheet_header()

    # --- layer table
    sh.text("L1   CAD LAYER SYSTEM AND MAPPING TO THE PROJECT'S EXISTING 22-LAYER TABLE",
            (16, 548), TXT["view_title"], "S-TITLE")
    rows = [[k, str(v[0]), f"{v[1]/100:.2f}", v[2], v[3]] for k, v in D.LAYERS.items()]
    # QA1: row height opened from 4.2 to 6.8 - the sheet was 45 % empty
    y = sh.table(16, 540, [42, 14, 18, 108, 32], rows,
                 ["LAYER", "ACI", "LW mm", "PURPOSE", "MASTER E.3.2"], TXT["small"], 6.8)
    sh.text("DECLARED DEVIATION X2: the R-series uses the S-* layer system.  Sheets S-01..S-08 "
            "keep the master's 22-layer table and are NOT touched.", (16, y - 5),
            TXT["small"], "S-BLAST")

    # --- graphic hierarchy
    sh.text("L2   GRAPHIC HIERARCHY - LINEWEIGHTS AS PLOTTED", (16, y - 14),
            TXT["view_title"], "S-TITLE")
    yy = y - 24
    for lay, desc in [("S-CONCRETE", "STRUCTURAL CONCRETE, CUT - HEAVIEST"),
                      ("S-REBAR-MAIN", "MAIN REINFORCEMENT - RED, MEDIUM"),
                      ("S-REBAR-SEC", "TRIMMERS / ADDITIONAL BARS - CYAN"),
                      ("S-REBAR-DIST", "DISTRIBUTION REINFORCEMENT - GREEN"),
                      ("S-REBAR-STIRRUP", "LINKS AND STIRRUPS - MAGENTA"),
                      ("S-CONCRETE-THIN", "CONCRETE BEYOND THE CUT PLANE"),
                      ("S-HIDDEN", "HIDDEN / BEYOND - DASHED"),
                      ("S-CENTER", "CENTRELINE - CHAIN"),
                      ("S-DIM", "DIMENSIONS - LIGHTEST"),
                      ("S-SECTION", "SECTION AND DETAIL MARKERS")]:
        if lay == "S-HIDDEN":
            sh.dline((18, yy), (78, yy), lay)
        elif lay == "S-CENTER":
            sh.cline((18, yy), (78, yy))
        else:
            sh.line((18, yy), (78, yy), lay)
        sh.text(f"{lay:<18} {desc}", (84, yy - 0.8), 2.0, "S-TEXT")
        yy -= 7.5
    sh.text("REINFORCEMENT MUST NEVER DISAPPEAR INTO A CONCRETE OUTLINE.  Concrete is plotted "
            "heavier than steel; steel is plotted in colour.", (16, yy - 3),
            TXT["small"], "S-BLAST")

    # --- bar representation
    x = 330
    sh.text("L3   BAR REPRESENTATION", (x, 548), TXT["view_title"], "S-TITLE")
    yy = 532
    sh.line((x + 4, yy), (x + 54, yy), "S-REBAR-MAIN")
    sh.text("BAR IN ELEVATION / PLAN - CONTINUOUS LINE ON ITS OWN LAYER",
            (x + 60, yy - 0.8), 2.0, "S-TEXT")
    yy -= 14
    for i in range(6):
        sh.bar_dot((x + 6 + i * 9, yy), 0.9, "S-REBAR-MAIN")
    sh.text("BAR IN SECTION - FILLED DOT AT THE TRUE SPACING", (x + 60, yy - 0.8),
            2.0, "S-TEXT")
    yy -= 14
    sh.rect(x + 4, yy - 3, x + 26, yy + 3, "S-REBAR-STIRRUP")
    sh.text("CLOSED LINK / STIRRUP IN SECTION", (x + 60, yy - 0.8), 2.0, "S-TEXT")
    yy -= 18
    sh.msp.add_blockref("BARMARK", (x + 12, yy), dxfattribs={"layer": "S-CALLOUT"})
    sh.text("W01", (x + 12, yy), TXT["bar_mark"], "S-CALLOUT", "CENTER")
    sh.leader([(x + 4, yy - 8), (x + 9, yy - 3)], None)
    sh.text("BAR-MARK BALLOON WITH LEADER.  EVERY MARK ON EVERY DRAWING HAS",
            (x + 60, yy + 1.4), 2.0, "S-TEXT")
    sh.text("EXACTLY ONE SCHEDULE ENTRY - VERIFIED PROGRAMMATICALLY.",
            (x + 60, yy - 2.2), 2.0, "S-TEXT")
    yy -= 20
    sh.secmark((x + 12, yy), "A")
    sh.text("SECTION MARKER - LETTER ABOVE, DIRECTION OF VIEW ARROWED",
            (x + 60, yy - 0.8), 2.0, "S-TEXT")
    yy -= 20
    sh.level((x + 12, yy), "(-)6.100")
    sh.text("LEVEL MARKER - METRES RELATIVE TO FINISHED SITE GRADE 0.000",
            (x + 60, yy - 0.8), 2.0, "S-TEXT")

    yy -= 24
    sh.text("L4   TEXT STANDARDS - HEIGHTS AS PLOTTED AT 1:1 ON A1", (x, yy),
            TXT["view_title"], "S-TITLE")
    yy -= 12
    for k, h, use in [("sheet_title", TXT["sheet_title"], "SHEET TITLE"),
                      ("view_title", TXT["view_title"], "VIEW / SECTION TITLE"),
                      ("panel_head", TXT["panel_head"], "PANEL HEADING"),
                      ("detail_label", TXT["detail_label"], "DETAIL LABEL"),
                      ("note", TXT["note"], "GENERAL NOTE"),
                      ("bar_mark", TXT["bar_mark"], "BAR MARK"),
                      ("rebar", TXT["rebar"], "REINFORCEMENT LABEL"),
                      ("dim", TXT["dim"], "DIMENSION"),
                      ("table", TXT["table"], "SCHEDULE / TABLE"),
                      ("small", TXT["small"], "SMALL ANNOTATION")]:
        sh.text(f"{h:.1f} mm  {use}", (x + 4, yy), h, "S-TEXT")
        yy -= h + 7.0

    x = 636
    # QA1: this column stopped less than half way down the sheet; it now
    # fills the column and stops clear of the title block.
    sh.panel_column(x, 548, 118, 195, [
        ("ABBREVIATIONS", [
        "EF     EACH FACE                 B/W   BOTH WAYS",
        "EW     EACH WAY                  T/B   TOP AND BOTTOM",
        "4L     FOUR-LEGGED LINK          c/c   CENTRE TO CENTRE",
        "Ld     DEVELOPMENT LENGTH        THK   THICKNESS",
        "T25    25 mm Fe500D DEFORMED BAR CL    CLEAR",
        "ESC    ESCAPE SHAFT              HH    HEADHOUSE",
        "ASW    APPROACH (ENTRY) STAIRWELL GWT  GROUNDWATER TABLE",
        "COMB   LOAD COMBINATION          SIDL  SUPERIMPOSED DEAD LOAD",
        ]),
        ("BAR SIZES AND UNIT MASS - Fe500D", [
        "BAR     AREA mm2    MASS kg/m     Ld (M35)    LAP 50 phi",
        "T8       50.3        0.395          320          400",
        "T10      78.5        0.617          400          500",
        "T12     113.1        0.888          480          600",
        "T16     201.1        1.578          640          800",
        "T20     314.2        2.466          800         1000",
        "T25     490.9        3.853         1000         1250",
        ]),
        ("SPACING PROVIDED - AREA PER METRE (mm2/m)", [
        "SPACING    T12     T16     T20     T25",
        "125        905    1609    2513    3927",
        "150        754    1340    2094    3272",
        "175        646    1149    1795    2805",
        "200        565    1005    1571    2454",
        "250        452     804    1257    1964",
        "300        377     670    1047    1636",
        "",
        "THE 150 ROW IS THE ONE THAT MATTERS: IT IS THE EMP MAXIMUM AND",
        "IT SETS THE SPACING OF EVERY MAIN CURTAIN IN THE BLAST ENVELOPE.",
        ]),
    ])
    sh.titleblock(scale="NOT TO SCALE", sheet_of="2 OF 30")
    return sh.save(os.path.join(OUT, "R-002_Reinforcement_Legend_and_Symbols.dxf"))


def _shape_sketch(sh, x, y, code, name, dims, formula):
    """Small dimensioned bar-shape sketch."""
    sh.text(f"SHAPE {code}   {name}", (x, y), TXT["detail_label"], "S-TITLE")
    # QA1: the sketches rise up to 22 mm above yy (shape 51 is a full link box),
    # so an 8 mm drop put the bar outline and its A/B/C labels straight through
    # the shape title.  Dropped clear of the title and the cut-length lines
    # moved down to match.
    yy = y - 30
    if code == "00":
        sh.line((x + 4, yy), (x + 64, yy), "S-REBAR-MAIN")
        sh.dim_h((x + 4, yy), (x + 64, yy), yy - 8, 1.0, "SC-DIM-S")
        sh.text("A", (x + 34, yy + 2.2), TXT["small"], "S-TEXT", "CENTER")
    elif code == "11":
        sh.pline([(x + 4, yy + 18), (x + 4, yy), (x + 64, yy)], "S-REBAR-MAIN")
        sh.text("B", (x + 1.6, yy + 9), TXT["small"], "S-TEXT", "RIGHT")
        sh.text("A", (x + 34, yy - 3.4), TXT["small"], "S-TEXT", "CENTER")
    elif code == "21":
        sh.pline([(x + 4, yy + 16), (x + 4, yy), (x + 64, yy), (x + 64, yy + 16)],
                 "S-REBAR-MAIN")
        sh.text("A", (x + 1.6, yy + 8), TXT["small"], "S-TEXT", "RIGHT")
        sh.text("B", (x + 34, yy - 3.4), TXT["small"], "S-TEXT", "CENTER")
        sh.text("C", (x + 66, yy + 8), TXT["small"], "S-TEXT")
    elif code == "51":
        sh.rect(x + 4, yy, x + 54, yy + 22, "S-REBAR-STIRRUP")
        sh.line((x + 44, yy + 22), (x + 50, yy + 15), "S-REBAR-STIRRUP")
        sh.line((x + 44, yy + 22), (x + 38, yy + 15), "S-REBAR-STIRRUP")
        sh.text("A", (x + 29, yy - 3.4), TXT["small"], "S-TEXT", "CENTER")
        sh.text("B", (x + 1.6, yy + 11), TXT["small"], "S-TEXT", "RIGHT")
        sh.text("135 HOOKS 10 phi", (x + 58, yy + 16), TXT["small"], "S-TEXT")
    else:
        sh.pline([(x + 4, yy), (x + 24, yy + 16), (x + 46, yy + 16), (x + 64, yy)],
                 "S-REBAR-MAIN")
        sh.text("FULLY DIMENSIONED ON THE DETAIL", (x + 4, yy - 4), TXT["small"], "S-TEXT")
    sh.text(f"CUT LENGTH = {formula}", (x, y - 46), TXT["small"], "S-NOTE")
    sh.text(dims, (x, y - 49.6), TXT["small"], "S-NOTE")


def r003():
    sh = Sheet("R-003", "TYPICAL REINFORCEMENT DETAILS AND BAR SHAPES",
               "SHAPE CODES · CUT-LENGTH RULE · SPACERS · GENERIC OPENING TRIMMING")
    sh.sheet_header()
    sh.text("D1   BAR SHAPE CODES USED IN THIS PACKAGE", (16, 548),
            TXT["view_title"], "S-TITLE")
    for i, (code, name, formula) in enumerate([
            ("00", "STRAIGHT", "A"),
            ("11", "ONE 90 DEG BEND (L-BAR)", "A + B"),
            ("21", "TWO 90 DEG BENDS (U / CRANK)", "A + B + C"),
            ("51", "CLOSED LINK, 135 DEG HOOKS", "2 (A + B) + 2 x 10 phi"),
            ("99", "OTHER - DIMENSIONED SKETCH", "SUM OF THE SCHEDULED LEGS")]):
        _shape_sketch(sh, 16 + (i % 3) * 105, 536 - (i // 3) * 60, code, name,
                      "dimensions as scheduled", formula)

    y = 404
    y = sh.panel(16, y, 320, "PBR-1  CUT-LENGTH RULE - DECLARED, NOT TAKEN FROM A CODE", [
        "CUT LENGTH = THE SUM OF THE SCHEDULED LEG DIMENSIONS.",
        "NO BEND DEDUCTION IS TAKEN.  Links add 2 x 10 phi for the 135 deg hooks.",
        "",
        "The rule is CONSERVATIVE by approximately 2 phi per 90 deg bend.",
        "Bend deductions to BS 8666 Table 3 shall be applied by the fabricator",
        "on the APPROVED bar bending schedule.",
        "",
        "IS 2502 IS NAMED IN THE BRIEF BUT NO COPY IS HELD IN THE PROJECT, SO IT",
        "IS NOT CITED.  This rule replaces it and is declared as an ASSUMPTION.",
        "",
        "P-1  STOCK BAR 12 000 mm.  Runs longer than stock are split into equal",
        "     pieces with 50 phi laps added, staggered so that not more than 50 %",
        "     are spliced at any one section.",
        "PBR-2  A 4-LEGGED LINK @ s is scheduled as TWO closed links per node on",
        "       an s x s grid; a 2-legged link @ s as ONE.",
        "PBR-3  The stair void and the two escape openings are DEDUCTED zone by",
        "       zone, not by a blanket percentage.",
    ], TXT["small"], 3.2)
    sh.panel(16, y - 6, 320, "SPACERS, CHAIRS AND COVER CONTROL", [
        "1  COVER IS A DESIGN VALUE, NOT A TOLERANCE.  75 / 50 / 40 / 30 as noted.",
        "2  The mat link grid (F05, T12 @ 250 x 250) DOUBLES AS THE SPACER SYSTEM",
        "   between the two mat curtains.  It is a structural requirement from the",
        "   one-way shear check, not a detailing convenience.",
        "3  Cementitious spacer blocks of the specified cover against blinding and",
        "   against every formed earth face.  No plastic spacer on an earth face.",
        "4  Chairs at not more than 1000 c/c both ways to the top curtain of the",
        "   mat and the pressure slab.",
        "5  NO BAR MAY BE DISPLACED TO CLEAR A SERVICE.  Any clash is an RFI.",
    ], TXT["small"], 3.2)

    x = 348
    sh.text("D2   GENERIC OPENING / PENETRATION TRIMMING RULE", (x, 548),
            TXT["view_title"], "S-TITLE")
    Pm = vw(20, x + 20, 430)
    sh.rect(*Pm(0, 0), *Pm(2400, 1800), "S-CONCRETE")
    sh.rect(*Pm(900, 600), *Pm(1500, 1200), "S-CONCRETE")
    sh.concrete_hatch([Pm(0, 0), Pm(2400, 0), Pm(2400, 1800), Pm(0, 1800)],
                      holes=[[Pm(900, 600), Pm(1500, 600), Pm(1500, 1200), Pm(900, 1200)]])
    for dy in (-90, 90):
        sh.line(Pm(200, 900 + dy), Pm(2200, 900 + dy), "S-REBAR-SEC")
    for dx in (-90, 90):
        sh.line(Pm(1200 + dx, 200), Pm(1200 + dx, 1600), "S-REBAR-SEC")
    sh.leader([Pm(2100, 1000), (x + 132, 470)],
              "TRIMMERS EACH SIDE, EACH FACE, EACH DIRECTION")
    sh.dim_h(Pm(900, 600), Pm(1500, 600), Pm(0, 300)[1])
    sh.dim_v(Pm(900, 600), Pm(900, 1200), Pm(400, 0)[0])
    sh.view_title((x, 398), "D2", "GENERIC TRIMMING AT ANY PENETRATION", "SCALE 1:20")
    y = sh.panel(x, 388, 290, "RULE - APPLIES WHERE NO DESIGNED DETAIL EXISTS", [
        "REPLACE THE INTERRUPTED STEEL EACH SIDE OF THE OPENING, EACH FACE,",
        "EACH DIRECTION, ANCHORED Ld BEYOND THE OPENING IN BOTH DIRECTIONS.",
        "MINIMUM 2 BARS OF THE PARENT DIAMETER EACH FACE EACH SIDE.",
        "",
        "THIS RULE IS NOT A SUBSTITUTE FOR A DESIGNED DETAIL.  The following",
        "penetrations have NO structural design basis in the project record and",
        "are reported NOT DETERMINABLE - a designed detail is required before",
        "construction:",
        "   ·  BLAST VALVES x5 - sizes and sleeve details are on sheet S-06 and",
        "      are not in the design register",
        "   ·  SERVICE-ENTRY PLATE, wall W2 at X approx 11 800 - size NOT AVAILABLE",
        "   ·  VENTILATION / CBRN DUCT PENETRATIONS - no penetration schedule exists",
        "",
        "REINFORCEMENT IS NOT FABRICATED WHERE THE DESIGN BASIS IS INSUFFICIENT.",
    ], TXT["small"], 3.2)
    sh.panel(x, y - 6, 290, "DESIGNED OPENINGS - WHERE THE REAL DETAIL IS", [
        "BLAST DOORS 1 AND 2, 1200 x 2100 in W6 / W7        R-205, R-703",
        "ESCAPE SHAFTS ESC 1 / ESC 2, 1400 dia in the roof  R-303",
        "STAIR VOID 2800 x 3160 in the roof                 R-303",
        "SECURITY DOOR 900 x 2100 in HW2                    R-702, R-703",
        "ENTRY DOOR 1000 x 2100 in the stairwell headwall   R-702",
        "SUMP-PIT OPENING 1500 x 1500 in the mat            R-101, R-103",
        "PARTITION DOOR GAPS 900 x 4 - NO TRIMMING REQUIRED, the 110 partitions",
        "   are non-structural A252 fabric                  R-202",
    ], TXT["small"], 3.2)
    sh.titleblock(scale="AS NOTED", sheet_of="3 OF 30")
    return sh.save(os.path.join(OUT, "R-003_Typical_Reinforcement_Details.dxf"))


def r004():
    sh = Sheet("R-004", "REINFORCEMENT SCHEDULE",
               "COMPLETE BAR BENDING SCHEDULE - ALL 92 MARKS")
    sh.sheet_header()
    marks = R.MARKS
    half = (len(marks) + 1) // 2
    # QA1: row height 4.9 left the bottom 220 mm of this sheet empty.  The
    # schedule now uses the height it has; the text size is unchanged (the
    # table fits its own text) and every summary below follows from RH.
    RH = 7.6
    colw = [16, 11, 10, 13, 13, 16, 17, 18, 88]
    hdr = ["MARK", "DIA", "SHP", "SPAC", "No.", "CUT", "TOT m", "kg", "ELEMENT / LOCATION"]
    for col, chunk in enumerate((marks[:half], marks[half:])):
        x = 16 + col * 400
        rows = []
        for m in chunk:
            loc = f"{m['element']} - {m['location']}"
            rows.append([m["mark"], f"T{m['phi']}", m["shape"], m["spacing"] or "-",
                         m["count"], round(m["cut"]), round(m["total_len"], 1),
                         f"{m['kg']:.0f}", loc[:64]])
        sh.table(x, 544, colw, rows, hdr, TXT["small"], RH)

    tot = sum(m["kg"] for m in R.MARKS)
    y = 544 - RH * (half + 1) - 8
    sh.text(f"TOTAL BAR REINFORCEMENT   {tot:,.0f} kg  =  {tot/1000:.2f} TONNES     "
            f"(FABRIC W18 SCHEDULED SEPARATELY BY AREA)", (16, y),
            TXT["panel_head"], "S-BLAST")
    rows = [[f"T{phi}", f"{n:,}", f"{L:,.0f}", f"{kg:,.0f}", f"{100*kg/tot:.1f} %"]
            for phi, (n, L, kg) in sorted(R.totals_by_dia().items())]
    sh.text("SUMMARY BY DIAMETER", (16, y - 10), TXT["panel_head"], "S-TITLE")
    sh.table(16, y - 14, [22, 26, 32, 30, 24], rows,
             ["BAR", "No.", "LENGTH m", "WEIGHT kg", "%"], TXT["small"], 6.2)
    rows = [[g, f"{kg:,.0f}", f"{kg/1000:.3f}", f"{100*kg/tot:.1f} %"]
            for g, kg in R.totals_by_group().items()]
    sh.text("SUMMARY BY ELEMENT GROUP", (180, y - 10), TXT["panel_head"], "S-TITLE")
    sh.table(180, y - 14, [92, 30, 26, 22], rows,
             ["ELEMENT GROUP", "kg", "t", "%"], TXT["small"], 6.2)
    sh.panel(360, y - 4, 280, "SCHEDULE NOTES", [
        "PBR-1  cut length = SUM of the scheduled legs, NO bend deduction; links add",
        "       2 x 10 phi for 135 deg hooks.  See R-003.",
        "P-1    stock bar 12 000; longer runs split with 50 phi laps, staggered.",
        "PBR-2  4-legged link @ s = TWO closed links per node on an s x s grid.",
        "PBR-3  stair void and escape openings deducted zone by zone.",
        "QUANTITIES ARE FOR TENDER AND ESTIMATING and shall be re-measured by the",
        "contractor on the approved bar bending schedule.",
        "FABRIC W18: A252 both faces to the four 110 non-structural partitions,",
        f"       {R.FABRIC[0]['area_m2']} m2.  Not included in the bar tonnage.",
        "NOT QUANTIFIED - no design basis exists: blast valves and sleeves, the",
        "service-entry plate, CBRN duct penetrations, blast-door leaf and frame",
        "anchorage.  Reported NOT DETERMINABLE.  See R-003 detail D2.",
        "SENTRY POST EXCLUDED - no sentry bar, weight or quantity appears here.",
    ], TXT["small"], 3.2)
    sh.titleblock(scale="NOT TO SCALE", sheet_of="4 OF 30")
    return sh.save(os.path.join(OUT, "R-004_Reinforcement_Schedule.dxf"))


def build():
    os.makedirs(OUT, exist_ok=True)
    return [r001(), r002(), r003(), r004()]


if __name__ == "__main__":
    for f in build():
        print("written", f)
