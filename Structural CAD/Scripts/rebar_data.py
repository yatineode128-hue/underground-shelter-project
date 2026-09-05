"""
rebar_data.py  --  THE SINGLE SOURCE OF TRUTH FOR EVERY BAR MARK.

Both the bar bending schedules (Schedules/) and the bar-mark annotation on every
DXF drawing are generated from this one list.  A mark therefore CANNOT appear on
a drawing without a schedule entry, and cannot be duplicated: build_marks()
asserts uniqueness.

QUANTITY BASIS -- declared, not assumed
---------------------------------------
* Bar counts are computed from the geometry stated in each row, taken from
  master Parts A.3/A.4/B/F and re-verified against current/cad/1_Underground_
  Level_Plan.dxf and sheet S-06 (audit A.2).
* PBR-1  cut length = SUM of scheduled leg dimensions, NO bend deduction;
         links add 2 x 10 phi for 135 deg hooks.  Conservative by ~2 phi per
         90 deg bend.  [ASSUMED - no bar-bending standard is in the workspace.]
* P-1    stock bar 12 000 mm; longer runs are split into equal pieces with
         50 phi laps added, staggered so <= 50 % are spliced at a section.
* PBR-2  a "4-legged link @ s" is scheduled as TWO closed links per node on an
         s x s grid; a "2-legged link @ s" as ONE closed link per node.
* PBR-3  openings (stair void, escape shafts) are DEDUCTED zone by zone, not by
         a blanket percentage.
* Quantities are for tender and estimating.  They must be re-measured by the
  contractor on the approved bar bending schedule (QA/QC item R-8).

SENTRY POST: EXCLUDED.  No sentry bar appears in this file.
"""
import math
import sc_proj as P
from rc_calc import BAR_AREA, bar_kg_per_m

HOOK = 10          # 135 deg hook allowance, x phi, each end of a closed link


# ---------------------------------------------------------------- shape rules
def cut_length(shape, dims, phi):
    """PBR-1.  dims are the scheduled leg dimensions, mm."""
    if shape == "00":                       # straight
        return dims[0]
    if shape == "11":                       # one 90 deg bend, A + B
        return sum(dims[:2])
    if shape == "21":                       # two 90 deg bends, A + B + C
        return sum(dims[:3])
    if shape == "51":                       # closed link, 2(A+B) + 2 x 10 phi
        return 2 * (dims[0] + dims[1]) + 2 * HOOK * phi
    if shape == "99":                       # other - fully dimensioned sketch
        return sum(dims)
    raise ValueError(shape)


SHAPE_NAME = {
    "00": "STRAIGHT",
    "11": "L-BAR, ONE 90 BEND (A+B)",
    "21": "U / CRANK, TWO 90 BENDS (A+B+C)",
    "51": "CLOSED LINK, 135 HOOKS",
    "99": "OTHER - DIMENSIONED SKETCH",
}

MARKS = []


def bar(mark, element, location, phi, shape, dims, count, drawings,
        spacing=None, remarks="", pieces=1, group=""):
    cl = cut_length(shape, dims, phi)
    MARKS.append(dict(
        mark=mark, group=group, element=element, location=location, phi=phi,
        shape=shape, dims=list(dims), spacing=spacing, count=int(count),
        pieces=pieces, cut=cl, total_len=cl * int(count) / 1000.0,
        kg=cl * int(count) / 1000.0 * bar_kg_per_m(phi),
        drawings=drawings, remarks=remarks))


def links(mark, element, location, phi, a, b, count, drawings, spacing=None,
          remarks="", group=""):
    bar(mark, element, location, phi, "51", (a, b), count, drawings,
        spacing=spacing, remarks=remarks, group=group)


def split(run, phi):
    """P-1: split a run into pieces of <= 12 000 with 50 phi laps."""
    return P.split_bar(run, P.lap(phi))


# =====================================================================
# GROUP F -- FOUNDATIONS (mat, starters, sump)
# =====================================================================
G = "FOUNDATIONS"
MAT_X = P.BOX["x1"] - 2 * 50                     # 21 900  (50 side cover)
MAT_Y = P.BOX["y1"] - 2 * 50                     # 6 100
n, p = split(MAT_X, 16)                          # 2 x 11 350
bar("F01", "MAT 600", "BOTTOM, LONGITUDINAL (X)", 16, "00", (round(p),),
    P.n_bars(MAT_Y, 150) * n, ["R-101", "R-102"], 150,
    f"{P.n_bars(MAT_Y,150)} bars in {n} pieces, laps 800 staggered", pieces=n, group=G)
bar("F02", "MAT 600", "BOTTOM, TRANSVERSE (Y)", 16, "00", (MAT_Y,),
    P.n_bars(MAT_X, 150), ["R-101", "R-102"], 150, "single length", group=G)
bar("F03", "MAT 600", "TOP, LONGITUDINAL (X)", 16, "00", (round(p),),
    P.n_bars(MAT_Y, 150) * n, ["R-101", "R-102"], 150,
    f"{P.n_bars(MAT_Y,150)} bars in {n} pieces", pieces=n, group=G)
bar("F04", "MAT 600", "TOP, TRANSVERSE (Y)", 16, "00", (MAT_Y,),
    P.n_bars(MAT_X, 150), ["R-101", "R-102"], 150, "single length", group=G)
links("F05", "MAT 600", "LINK GRID 250 x 250 THROUGHOUT", 12,
      600 - 75 - 40, 250, (22000 // 250) * (6200 // 250), ["R-101", "R-102"], "250 x 250",
      "doubles as the curtain spacer system; supplied Asv/sv 1.810 = 2.0 x required", group=G)
bar("F06", "MAT 600", "EDGE U-BARS, ALL FREE EDGES", 16, "21", (640, 500, 640),
    int(2 * (22000 + 6200) // 150), ["R-101", "R-103"], 150,
    "closes both curtains at every free mat edge", group=G)
bar("F07", "MAT / PERIMETER WALLS", "WALL STARTERS W1-W4, EACH FACE", 16, "11",
    (900, 1435), 2 * int(54000 // 150), ["R-101", "R-103", "R-803"], 150,
    "900 horizontal leg into the mat; 150 kicker + 800 lap (50 phi)", group=G)
bar("F08", "MAT / WALLS W6-W7", "WALL STARTERS W6/W7, EACH FACE", 20, "11",
    (900, 1635), 2 * int(10000 // 150), ["R-101", "R-103", "R-803"], 150,
    "150 kicker + 1000 lap (50 phi)", group=G)
bar("F09", "MAT / WALL W5", "WALL STARTERS W5, EACH FACE", 12, "11",
    (600, 1235), 2 * int(5000 // 150), ["R-101", "R-103"], 150,
    "150 kicker + 600 lap (50 phi)", group=G)
bar("F10", "MAT 600", "SUMP-PIT OPENING TRIMMERS", 20, "00", (1500 + 2 * 800,),
    4 * 2 * 4, ["R-101", "R-103"], None,
    "4-T20 each face each side; Ld 800 beyond. Pit 1500x1500 at X 11070-12570, "
    "Y 900-2400 [CONFIRMED from sheet S-06]", group=G)
bar("F11", "SUMP PIT WALLS 300", "VERTICAL, EACH FACE", 16, "00", (1500 + 800,),
    2 * int(4 * 1800 // 150), ["R-101", "R-102"], 150,
    "pit invert (-)7.600, mat top (-)6.100", group=G)
bar("F12", "SUMP PIT WALLS 300", "HORIZONTAL RINGS, EACH FACE", 16, "00",
    (4 * 1800 + 800,), 2 * P.n_bars(1500, 150), ["R-101", "R-102"], 150, "", group=G)
bar("F13", "SUMP PIT BASE 400", "BOTH WAYS, EACH FACE", 16, "00", (2100 - 100,),
    2 * 2 * P.n_bars(2000, 150), ["R-102"], 150,
    "base 400 thk - SEE CONFLICT C18 (S-06 text says 300)", group=G)

# =====================================================================
# GROUP W -- WALLS
# =====================================================================
G = "WALLS"
WALL_RUN = 2 * 22000 + 2 * 5000                       # 54 000 perimeter run
H_VERT = 4100 - 150 - 75                              # 3 875 kicker top -> 75 below roof top
bar("W01", "PERIMETER WALLS 600", "VERTICAL, EARTH FACE", 16, "00", (H_VERT,),
    int(WALL_RUN // 150), ["R-201", "R-203", "R-204"], 150,
    "laps 800 staggered with starters F07", group=G)
bar("W02", "PERIMETER WALLS 600", "VERTICAL, INTERNAL FACE", 16, "00", (H_VERT,),
    int(WALL_RUN // 150), ["R-201", "R-203", "R-204"], 150, "", group=G)
n, p = split(21900, 16)
bar("W03", "PERIMETER WALLS W1 / W2", "HORIZONTAL, EACH FACE", 16, "00", (round(p),),
    P.n_bars(3200, 150) * 2 * 2 * n, ["R-201", "R-203"], 150,
    f"{P.n_bars(3200,150)} layers x 2 faces x 2 walls, in {n} pieces", pieces=n, group=G)
bar("W04", "PERIMETER WALLS W3 / W4", "HORIZONTAL, EACH FACE", 16, "21",
    (640, 6100, 640), P.n_bars(3200, 150) * 2 * 2, ["R-201", "R-203"], 150,
    "legs turn Ld 640 into W1 and W2 at every corner", group=G)
links("W05", "PERIMETER WALLS 600", "CLOSED LINKS, 200 x 200 GRID", 12,
      600 - 2 * 50, 150, int(WALL_RUN // 200) * (3200 // 200),
      ["R-201", "R-204"], "200 x 200", "ties the two curtains", group=G)
bar("W06", "PERIMETER WALLS 600", "HAUNCH DIAGONALS, WALL/ROOF + WALL/MAT", 20, "00",
    (round(math.hypot(500, 500)) + 2 * 800,), 2 * int(WALL_RUN // 150),
    ["R-103", "R-204", "R-304", "R-803"], 150, "500 x 500 haunch, both junctions", group=G)

bar("W07", "WALLS W6 / W7 400", "VERTICAL, SHAFT FACE", 20, "00", (H_VERT,),
    2 * int(5000 // 150), ["R-202", "R-204"], 150, "MOD M1", group=G)
bar("W08", "WALLS W6 / W7 400", "VERTICAL, ROOM FACE", 20, "00", (H_VERT,),
    2 * int(5000 // 150), ["R-202", "R-204"], 150, "MOD M1", group=G)
bar("W09", "WALLS W6 / W7 400", "HORIZONTAL, SHAFT FACE", 20, "21", (800, 5000, 800),
    P.n_bars(3200, 150) * 2, ["R-202", "R-203"], 150,
    "Ld 800 into W1 and W2", group=G)
bar("W10", "WALLS W6 / W7 400", "HORIZONTAL, ROOM FACE", 20, "21", (800, 5000, 800),
    P.n_bars(3200, 150) * 2, ["R-202", "R-203"], 150, "", group=G)
links("W11", "WALLS W6 / W7 400", "4-LEGGED LINKS @ 200 (2 CLOSED LINKS/NODE)", 12,
      400 - 2 * 50, 150, 2 * 2 * (5000 // 200) * (3200 // 200), ["R-202", "R-204"],
      "200 x 200", "PBR-2", group=G)
bar("W12", "WALLS W6 / W7 400", "HAUNCH DIAGONALS", 20, "00",
    (round(math.hypot(500, 500)) + 2 * 800,), 2 * 2 * int(5000 // 150),
    ["R-202", "R-304"], 150, "", group=G)

bar("W13", "BLAST DOORS 1 AND 2", "JAMB BARS, 4-T20 EACH JAMB EACH FACE", 20, "00",
    (2100 + 2 * 800,), 2 * 2 * 2 * 4, ["R-205", "R-703"], None,
    "1257 mm2 provided vs 1256 required - EXACT, not generous", group=G)
links("W14", "BLAST DOORS 1 AND 2", "JAMB LINKS @ 150", 12, 400 - 2 * 50, 200,
      2 * 2 * int(3700 // 150), ["R-205", "R-703"], 150, "", group=G)
bar("W15", "BLAST DOORS 1 AND 2", "REVEAL U-BARS, BOTH FACES", 16, "21",
    (640, 300, 640), 2 * int(2 * (1200 + 2100) // 150), ["R-205", "R-703"], 150,
    "closes the reveal around the full opening perimeter", group=G)
bar("W16", "WALL W5 200", "VERTICAL, EACH FACE", 12, "00", (H_VERT,),
    2 * int(5000 // 150), ["R-202"], 150, "minimum steel governs", group=G)
bar("W17", "WALL W5 200", "HORIZONTAL, EACH FACE", 12, "21", (480, 5000, 480),
    P.n_bars(3200, 150) * 2, ["R-202"], 150, "", group=G)

# =====================================================================
# GROUP S -- ROOF / PRESSURE SLAB
# =====================================================================
G = "ROOF SLAB"
ROOF_Y = 6200 - 2 * 75            # 6 050
ROOF_X = 22000 - 2 * 75           # 21 850
# transverse (spanning the 5 000 clear), main zones X 0-15200 and 18000-22000
nT_main = int(15200 // 150) + int(4000 // 150)
bar("S01A", "ROOF SLAB 900", "BOTTOM, TRANSVERSE (Y) - MAIN ZONES", 25, "00",
    (ROOF_Y,), nT_main, ["R-301", "R-302"], 150,
    "X 0-15200 and X 18000-22000; stair void deducted", group=G)
bar("S01B", "ROOF SLAB 900", "BOTTOM, TRANSVERSE - CANTILEVER PAD", 25, "00",
    (6200 - 3760 - 75,), int(2800 // 150), ["R-301", "R-302"], 150,
    "X 15200-18000, Y 3760-6200 only - the void interrupts the rest", group=G)
n, p = split(ROOF_X, 25)
bar("S02A", "ROOF SLAB 900", "BOTTOM, LONGITUDINAL (X) - FULL LENGTH BANDS", 25, "00",
    (round(p),), (int(600 // 150) + int(2440 // 150)) * n, ["R-301", "R-302"], 150,
    f"Y 0-600 and Y 3760-6200; {n} pieces, laps 1250 staggered", pieces=n, group=G)
n2, p2 = split(15200 - 75, 25)
bar("S02B", "ROOF SLAB 900", "BOTTOM, LONGITUDINAL - WEST OF THE VOID", 25, "00",
    (round(p2),), int(3160 // 150) * n2, ["R-301"], 150,
    f"Y 600-3760, X 0-15200; {n2} pieces", pieces=n2, group=G)
bar("S02C", "ROOF SLAB 900", "BOTTOM, LONGITUDINAL - EAST OF THE VOID", 25, "00",
    (4000 - 75,), int(3160 // 150), ["R-301"], 150, "Y 600-3760, X 18000-22000", group=G)
bar("S03A", "ROOF SLAB 900", "TOP, TRANSVERSE (Y) - MAIN ZONES", 25, "00",
    (ROOF_Y,), nT_main, ["R-301", "R-302"], 150, "continuous over both supports", group=G)
bar("S03B", "ROOF SLAB 900", "TOP, TRANSVERSE - CANTILEVER PAD", 25, "00",
    (6200 - 3760 - 75,), int(2800 // 150), ["R-301", "R-302", "R-303"], 150,
    "*** THE CANTILEVER STEEL - FINDING F2, M(root) 758.6 > midspan 700.2 ***", group=G)
bar("S03C", "ROOF SLAB 900", "TOP, TRANSVERSE - STRIP OVER W1 AT THE VOID", 25, "00",
    (600 - 75,), int(2800 // 150), ["R-301", "R-303"], 150, "continuity only", group=G)
n, p = split(ROOF_X, 25)
bar("S04A", "ROOF SLAB 900", "TOP, LONGITUDINAL (X) - FULL LENGTH BANDS", 25, "00",
    (round(p),), (int(600 // 150) + int(2440 // 150)) * n, ["R-301", "R-302"], 150,
    f"{n} pieces, laps 1250 staggered", pieces=n, group=G)
bar("S04B", "ROOF SLAB 900", "TOP, LONGITUDINAL - WEST OF THE VOID", 25, "00",
    (round(p2),), int(3160 // 150) * n2, ["R-301"], 150, f"{n2} pieces", pieces=n2, group=G)
bar("S04C", "ROOF SLAB 900", "TOP, LONGITUDINAL - EAST OF THE VOID", 25, "00",
    (4000 - 75,), int(3160 // 150), ["R-301"], 150, "", group=G)
# links: end zones 1500 each side, minus void and pad; mid zone 2000 wide
end_nodes = 2 * (22000 // 250) * (1500 // 250) - (2800 // 250) * (1500 // 250) \
            - (2800 // 250) * (1500 // 250)
links("S05", "ROOF SLAB 900", "4-LEGGED LINKS @ 250, END 1500 EACH SIDE", 12,
      900 - 2 * 75, 150, 2 * end_nodes, ["R-301", "R-302"], "250 x 250",
      "PBR-2; Cl. 26.5.1.5 limit 300 governs the 409 required", group=G)
mid_nodes = (22000 // 300) * (2000 // 300) - (2800 // 300) * (2000 // 300)
links("S06", "ROOF SLAB 900", "2-LEGGED LINKS @ 300, MID ZONE", 12,
      900 - 2 * 75, 150, mid_nodes, ["R-301", "R-302"], "300 x 300", "PBR-2", group=G)
links("S07", "ROOF CANTILEVER PAD", "4-LEGGED LINKS @ 250 THROUGHOUT THE PAD", 12,
      900 - 2 * 75, 150, 2 * (2800 // 250) * (1840 // 250), ["R-301", "R-303"],
      "250 x 250", "NEW REQUIREMENT FROM FINDING F2", group=G)
bar("S08", "ESCAPE SHAFT OPENINGS", "TRIMMERS, 5-T25 EACH SIDE/FACE/DIRECTION", 25, "00",
    (1400 + 2 * 1000,), 2 * 2 * 2 * 2 * 5, ["R-301", "R-303"], None,
    "2454 mm2 provided vs 2291 required; Ld 1000 beyond the opening", group=G)
bar("S09", "ESCAPE SHAFT COLLARS", "HOOPS, 3 LAYERS EACH FACE", 16, "00",
    (round(math.pi * 1650) + 800,), 2 * 6, ["R-303"], 150,
    "mean collar diameter 1650; lap 800", group=G)
bar("S10", "ESCAPE SHAFT COLLARS", "RADIAL BARS", 16, "00", (600 + 2 * 640,),
    2 * 2 * int(math.pi * 1650 // 150), ["R-303"], 150, "", group=G)
links("S11", "ESCAPE SHAFT THICKENING", "CLOSED LINKS @ 150 IN THE 1200 ANNULUS", 12,
      1200 - 2 * 75, 150, 2 * int(math.pi * 1650 // 150), ["R-303"], 150,
      "slab thickened 900 -> 1200 over a 600 annulus", group=G)
bar("S12", "STAIR VOID FREE EDGE", "6-T25 TOP + 6-T25 BOTTOM IN THE 1200 THICKENING", 25,
    "00", (2800 + 2 * 1000,), 12, ["R-301", "R-303"], None, "edge thickened 900 -> 1200", group=G)
links("S13", "STAIR VOID FREE EDGE", "CLOSED LINKS @ 150", 12, 1200 - 2 * 75, 500,
      int(2800 // 150), ["R-303"], 150, "", group=G)
bar("S14", "BAND OVER W6 AND W7", "6-T25 EACH FACE, TOP AND BOTTOM, 900 BAND", 25, "00",
    (ROOF_Y,), 2 * 12, ["R-301", "R-303"], None, "", group=G)
bar("S15", "STAIR VOID RE-ENTRANT CORNERS", "4-T25 EACH FACE AT 45 DEG", 25, "00",
    (2 * 2000,), 2 * 2 * 4, ["R-301", "R-303"], None,
    "2000 long each way; the crack initiators - mandatory, not decorative", group=G)
bar("S16", "BAND BENEATH HEADHOUSE WALL HW3", "4-T25 TOP AND BOTTOM, 1200 BAND", 25, "00",
    (5000 + 2 * 1250,), 8, ["R-301", "R-304", "R-701"], None,
    "HW3 has NO wall beneath it - detailed as a LINE LOAD, not a support", group=G)

# =====================================================================
# GROUP B -- BEAM-TYPE ELEMENTS  (there are NO framed beams or columns)
# =====================================================================
G = "BEAM-TYPE ELEMENTS"
bar("B01", "BLAST-DOOR HEADER 400 x 1100", "TOP, 4-T20 (x2 HEADERS)", 20, "00",
    (1200 + 2 * 800,), 2 * 4, ["R-401", "R-402", "R-703"], None,
    "M = 48.2 kNm, V = 241 kN", group=G)
bar("B02", "BLAST-DOOR HEADER 400 x 1100", "BOTTOM, 4-T20 (x2 HEADERS)", 20, "00",
    (1200 + 2 * 800,), 2 * 4, ["R-401", "R-402", "R-703"], None, "", group=G)
links("B03", "BLAST-DOOR HEADER 400 x 1100", "4-LEGGED LINKS @ 150", 12,
      1100 - 2 * 40, 400 - 2 * 40, 2 * 2 * int(2800 // 150), ["R-402", "R-703"], 150,
      "PBR-2", group=G)

# =====================================================================
# GROUP ST -- MAIN STAIRCASE  (GEOMETRY FROZEN)
# =====================================================================
G = "MAIN STAIRCASE"
cos31 = math.cos(math.radians(31.4))
SLOPE = round(1960 / cos31)                       # 2 296 on slope
bar("ST01", "MAIN STAIR FLIGHT, WAIST 200", "MAIN BARS (x3 FLIGHTS)", 12, "21",
    (600, SLOPE, 600), 3 * P.n_bars(1200 - 60, 150), ["R-601", "R-602"], 150,
    "FROZEN GEOMETRY 24R @ 170.8333 / 280, 3 flights x 8. Leff 3160, util 52 %", group=G)
bar("ST02", "MAIN STAIR FLIGHT, WAIST 200", "DISTRIBUTION (x3 FLIGHTS)", 10, "00",
    (1200 - 60,), 3 * P.n_bars(SLOPE, 200), ["R-601", "R-602"], 200, "", group=G)
bar("ST03", "MAIN STAIR FLIGHT, WAIST 200", "TOP STEEL, 800 INTO THE FLIGHT", 12, "00",
    (800 + 480,), 3 * 2 * P.n_bars(1200 - 60, 150), ["R-601", "R-602", "R-604"], 150,
    "0.25 Leff each end, anchored Ld 480", group=G)
bar("ST04", "MAIN STAIR LANDINGS L1 / L2, 200", "BOTTOM MAIN", 12, "00",
    (2800 + 2 * 200,), 2 * P.n_bars(1200, 125), ["R-601", "R-602"], 125,
    "T12 @ 150 gives exactly 100 % - TOO TIGHT; @ 125 adopted, util 84 %", group=G)
bar("ST05", "MAIN STAIR LANDINGS L1 / L2, 200", "TOP, 900 FROM EACH SUPPORT", 12, "00",
    (900 + 480,), 2 * 2 * P.n_bars(1200, 125), ["R-601", "R-602", "R-604"], 125, "", group=G)
bar("ST06", "MAIN STAIR LANDINGS L1 / L2, 200", "DISTRIBUTION", 10, "00", (1200 - 60,),
    2 * P.n_bars(2800, 200), ["R-601", "R-602"], 200, "", group=G)

# =====================================================================
# GROUP H -- HEADHOUSE
# =====================================================================
G = "HEADHOUSE"
HH_PERIM = 2 * (4400 + 5400)                      # 19 600 wall centre-line
bar("H01A", "HEADHOUSE ROOF 500", "BOTTOM, MAIN (SPANNING 4000 IN X)", 20, "00",
    (4800 - 2 * 75,), P.n_bars(5800 - 150, 150), ["R-701"], 150, "util 90 %", group=G)
bar("H01B", "HEADHOUSE ROOF 500", "BOTTOM, SECONDARY (Y)", 20, "00", (5800 - 150,),
    P.n_bars(4650, 150), ["R-701"], 150, "", group=G)
bar("H01C", "HEADHOUSE ROOF 500", "TOP, MAIN (X)", 20, "00", (4800 - 2 * 75,),
    P.n_bars(5800 - 150, 150), ["R-701"], 150, "continuous over every support, Ld 800", group=G)
bar("H01D", "HEADHOUSE ROOF 500", "TOP, SECONDARY (Y)", 20, "00", (5800 - 150,),
    P.n_bars(4650, 150), ["R-701"], 150, "", group=G)
links("H02", "HEADHOUSE ROOF 500", "4-LEGGED LINKS @ 175, END 1200 EACH SIDE", 12,
      500 - 2 * 75, 150, 2 * 2 * (1200 // 175) * (5000 // 175), ["R-701"], "175 x 175",
      "SHEAR NEW AND MANDATORY - not in the Phase 1 report", group=G)
links("H03", "HEADHOUSE ROOF 500", "4-LEGGED LINKS @ 250, MID ZONE", 12,
      500 - 2 * 75, 150, 2 * (1600 // 250) * (5000 // 250), ["R-701"], "250 x 250", "", group=G)
bar("H04A", "HEADHOUSE WALLS 400", "VERTICAL, EACH FACE", 16, "00", (3825,),
    2 * int(HH_PERIM // 150), ["R-701", "R-702"], 150,
    "SYMMETRICAL - 383 kPa acts on EITHER FACE (C10)", group=G)
n, p = split(HH_PERIM, 16)
bar("H04B", "HEADHOUSE WALLS 400", "HORIZONTAL RINGS, EACH FACE", 16, "00", (round(p),),
    P.n_bars(2400, 150) * 2 * n, ["R-701", "R-702"], 150, f"{n} pieces", pieces=n, group=G)
links("H05", "HEADHOUSE WALLS 400", "4-LEGGED LINKS @ 250, ALL FOUR WALLS", 12,
      400 - 2 * 50, 150, 2 * (HH_PERIM // 250) * (2400 // 250), ["R-701"], "250 x 250",
      "Cl. 26.5.1.5 limit 256 governs", group=G)
bar("H06", "HEADHOUSE WALL / ROOF", "HAUNCH DIAGONALS, 300 x 300", 16, "00",
    (round(math.hypot(300, 300)) + 2 * 640,), int(HH_PERIM // 150), ["R-701", "R-304"], 150,
    "", group=G)
bar("H07", "HEADHOUSE SECURITY DOOR 900 x 2100", "JAMB BARS, 2-T20 EACH JAMB EACH FACE",
    20, "00", (2100 + 2 * 800,), 2 * 2 * 2, ["R-702", "R-703"], None,
    "628 mm2 provided vs 603 required. NOT blast rated", group=G)
bar("H08", "HEADHOUSE DOOR-HEAD EDGE BAND 400 x 800", "4-T20 TOP + 4-T20 BOTTOM", 20,
    "00", (900 + 2 * 600 + 2 * 800,), 8, ["R-402", "R-702", "R-703"], None,
    "only 300 mm of wall above the door - the 300 wall and 500 roof act TOGETHER", group=G)
links("H09", "HEADHOUSE DOOR-HEAD EDGE BAND", "4-LEGGED LINKS @ 150", 12,
      800 - 2 * 40, 400 - 2 * 40, 2 * int(2100 // 150), ["R-402", "R-702"], 150, "PBR-2", group=G)
bar("H10", "PRESSURE SLAB / HEADHOUSE WALLS", "WALL STARTERS, EACH FACE", 16, "11",
    (600, 1735), 2 * int(HH_PERIM // 150), ["R-701", "R-803"], 150,
    "cast into the 900 pressure slab; 150 kicker + 800 lap", group=G)

# =====================================================================
# GROUP E -- ENTRANCE / COVERED ENTRY STAIRWELL  (NOT BLAST RATED)
# =====================================================================
G = "ENTRANCE / ENTRY STAIRWELL"
cos29 = math.cos(math.radians(29.05))
E_SLOPE = round(3300 / cos29)                     # 3 775 on slope
bar("E01", "ENTRY STAIRWELL FLIGHT, WAIST 250", "MAIN BARS", 16, "21",
    (750, E_SLOPE, 750), P.n_bars(1500 - 60, 200), ["R-603", "R-702"], 200,
    "12R @ 166.6667 / 300; Leff 4800; util 75 %", group=G)
bar("E02", "ENTRY STAIRWELL FLIGHT, WAIST 250", "DISTRIBUTION", 10, "00", (1500 - 60,),
    P.n_bars(E_SLOPE, 200), ["R-603"], 200, "", group=G)
bar("E03", "ENTRY STAIRWELL FLIGHT, WAIST 250", "TOP, 1200 INTO THE FLIGHT", 16, "00",
    (1200 + 640,), 2 * P.n_bars(1500 - 60, 200), ["R-603", "R-604"], 200,
    "anchored Ld 640", group=G)
bar("E04A", "ENTRY STAIRWELL SIDE WALLS 250", "VERTICAL, EACH FACE", 12, "00",
    (2900 + 600,), 2 * 2 * int(6800 // 200), ["R-603", "R-702"], 200,
    "MINIMUM STEEL GOVERNS - 31 % utilised", group=G)
bar("E04B", "ENTRY STAIRWELL SIDE WALLS 250", "HORIZONTAL, EACH FACE", 12, "00",
    (6800 - 100,), 2 * 2 * P.n_bars(2900, 200), ["R-603", "R-702"], 200, "", group=G)
bar("E05A", "ENTRY STAIRWELL RAKING ROOF 250", "TRANSVERSE, EACH FACE", 12, "00",
    (2000 - 100,), 2 * int(6800 // 200), ["R-603", "R-702"], 200,
    "20 kPa imposed taken deliberately - a stray vehicle on the berm", group=G)
bar("E05B", "ENTRY STAIRWELL RAKING ROOF 250", "LONGITUDINAL, EACH FACE", 12, "00",
    (6800 - 100,), 2 * P.n_bars(1900, 200), ["R-603", "R-702"], 200, "", group=G)
bar("E06", "ENTRY STAIRWELL TOP LANDING 250", "BOTH WAYS, EACH FACE", 12, "00", (1900,),
    2 * 2 * P.n_bars(1500, 200), ["R-603", "R-702"], 200, "1500 x 1500 at 0.000", group=G)
bar("E07", "ENTRY STAIRWELL PLATFORM 250", "BOTH WAYS, EACH FACE", 12, "00", (1900,),
    2 * 2 * P.n_bars(1500, 200), ["R-702"], 200,
    "*** C16 OPEN - roof/platform junction not resolved ***", group=G)
bar("E08A", "ENTRY STAIRWELL HEADWALL 250", "VERTICAL, EACH FACE", 12, "00", (2900 + 600,),
    2 * int(2000 // 200), ["R-702"], 200, "", group=G)
bar("E08B", "ENTRY STAIRWELL HEADWALL 250", "HORIZONTAL, EACH FACE", 12, "00", (1900,),
    2 * P.n_bars(2900, 200), ["R-702"], 200, "", group=G)
bar("E09A", "ENTRY STAIRWELL STEPPED RAFT 300", "LONGITUDINAL, EACH FACE", 12, "00",
    (6800 - 100,), 2 * P.n_bars(1900, 200), ["R-702", "R-804"], 200,
    "MOVEMENT JOINT where the raft meets the headhouse", group=G)
bar("E09B", "ENTRY STAIRWELL STEPPED RAFT 300", "TRANSVERSE, EACH FACE", 12, "00",
    (2000 - 100,), 2 * int(6700 // 200), ["R-702", "R-804"], 200, "", group=G)
bar("E10", "ENTRY DOOR LINTEL 250 x 350", "3-T12 TOP + 3-T12 BOTTOM", 12, "00",
    (1000 + 2 * 480,), 6, ["R-402", "R-702"], None, "over 1000 clear", group=G)
links("E11", "ENTRY DOOR LINTEL 250 x 350", "LINKS @ 150", 8, 350 - 2 * 30, 250 - 2 * 30,
      int(1960 // 150), ["R-402", "R-702"], 150, "", group=G)
bar("E12", "ENTRY STAIRWELL OPENING CORNER", "U-BAR ACROSS THE CORNER", 16, "21",
    (640, 500, 640), P.n_bars(1500, 200), ["R-604", "R-702"], 200,
    "SP 34 Cl. 5.5 - MAIN BARS SHALL NOT BE BENT ROUND THE 209 DEG CORNER", group=G)


# ------------------------------------------------------------------- fabric
FABRIC = [dict(mark="W18", element="W8 PARTITIONS 110 (x4)",
               location="A252 MESH BOTH FACES", spec="A252 FABRIC",
               area_m2=round(4 * 2 * ((5000 * 3200) - (900 * 2100)) / 1e6, 1),
               drawings=["R-202"],
               remarks="NON-STRUCTURAL. Shown for completeness; no load path assumed")]


# --------------------------------------------------------------- integrity
def build_marks():
    seen = {}
    for m in MARKS:
        assert m["mark"] not in seen, f"DUPLICATE BAR MARK {m['mark']}"
        seen[m["mark"]] = m
    for f in FABRIC:
        assert f["mark"] not in seen, f"DUPLICATE MARK {f['mark']}"
    return MARKS


def totals_by_dia():
    t = {}
    for m in MARKS:
        t.setdefault(m["phi"], [0, 0.0, 0.0])
        t[m["phi"]][0] += m["count"]
        t[m["phi"]][1] += m["total_len"]
        t[m["phi"]][2] += m["kg"]
    return t


def totals_by_group():
    t = {}
    for m in MARKS:
        t.setdefault(m["group"], 0.0)
        t[m["group"]] += m["kg"]
    return t


def all_drawings():
    d = set()
    for m in MARKS:
        d.update(m["drawings"])
    for f in FABRIC:
        d.update(f["drawings"])
    return sorted(d)


build_marks()

if __name__ == "__main__":
    print(f"{len(MARKS)} bar marks, {len(FABRIC)} fabric item(s) - all unique")
    tot = sum(m["kg"] for m in MARKS)
    print(f"TOTAL REINFORCEMENT {tot/1000:.2f} tonnes")
    for phi, (n, L, kg) in sorted(totals_by_dia().items()):
        print(f"  T{phi:<3} {n:>6} bars {L:>10.1f} m {kg/1000:>8.3f} t")
    print()
    for g, kg in totals_by_group().items():
        print(f"  {g:<32} {kg/1000:>8.3f} t")
    print()
    print("drawings referenced:", all_drawings())
