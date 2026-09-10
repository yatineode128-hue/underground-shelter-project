"""
wm_quantities.py — quantity derivation for the Works Management BOQ.

Underground CBRN-hardened blast-resistant protective structure + sentry post, Pune.
Works Management package revision WM1.

Every quantity produced here is derived from a value that already exists in the
project record.  The source of each input is named in the SOURCES table below and
repeated in the printed working, so that any figure in the BOQ can be traced back
to the master project state file, the Rev F drawings or an existing discipline
package.

Evidence classes follow the master project state file:
    [C] CONFIRMED      taken directly from the project record
    [D] DERIVED        computed here from [C] inputs, arithmetic shown
    [A] ASSUMED        adopted by this package because the project does not state it
    [N] NOT AVAILABLE  cannot be determined from the project record

No value is invented.  Where a quantity cannot be derived the item is carried
into the BOQ as "To be verified from final measurement".

Run:  python3 wm_quantities.py > ../Schedules/BOQ_QUANTITY_DERIVATION.txt
"""

import math
from collections import OrderedDict

MM = 1000.0  # mm -> m

# ---------------------------------------------------------------------------
# SOURCES — every input value used below, with its provenance
# ---------------------------------------------------------------------------
SOURCES = [
    ("Box external 22000 x 6200", "master A.4.2 / L", "[C]"),
    ("Box internal 20800 x 5000", "master A.4.2 / L", "[C]"),
    ("Perimeter wall 600, roof 900, mat 600, PCC 100 M15", "master A.4.2", "[C]"),
    ("Internal clear height 3200", "master A.4.2", "[C]"),
    ("Levels: grade 0.000, T/slab -2.000, soffit -2.900, floor -6.100, "
     "u/s mat -6.700, formation -6.800", "master A.4.3", "[C]"),
    ("W5 200 @ 12600-12800; W6 400 @ 14800-15200; W7 400 @ 18000-18400",
     "master A.3", "[C]"),
    ("W8 partitions x4 @ 110, each with a 900 door gap at Y 2500-3400",
     "master A.3 / F.1", "[C]"),
    ("Stair void 15200-18000 x 600-3760; pad 3760-5600", "master A.4.4", "[C]"),
    ("ESC 1 (2050,2050), ESC 2 (19900,2050); 1400 dia clear, 250 collar, OD 1900",
     "master A.4.5", "[C]"),
    ("ESC head levels +0.150 (ESC 1) and +0.700 (ESC 2)", "master QUICK_STATE / A.4.3", "[C]"),
    ("Roof locally thickened 900->1200 over a 600 annulus at each shaft, and over "
     "600 at the stair-void free edge", "master F.1", "[C]"),
    ("Headhouse external 13600-18400 x 200-6000; internal 14000-18000 x 600-5600; "
     "walls 400; roof 500; soffit +0.400; top +0.900; no earth cover",
     "master A.4.6", "[C]"),
    ("Covered entry stairwell external 9250-16050 x 5750-7750; internal "
     "9500-15800 x 6000-7500; walls 250; raft 300; roof 250 raking",
     "master A.4.7", "[C]"),
    ("Entry stairwell 12R @ 166.6667, going 300, waist 250; platform 1500 x 1500 "
     "at -2.000; top landing 9500-11000 at 0.000", "master A.4.7", "[C]"),
    ("Main staircase FROZEN: 24R @ 170.8333, tread 280, 3 flights x 8, waist 200, "
     "flights 1200 wide, total rise 4100", "master A.4.4; frozen by project instruction", "[C]"),
    ("Engineered cover 2000 layered = 40.65 kPa, six layers", "master A.7.3", "[C]"),
    ("Burster slab M30 200 thk, T12 @ 150 B/W, inside the cover", "master A.7.3", "[C]"),
    ("Sump SU-01 1500 x 1500 x 1500; invert -7.600; base slab -8.000; "
     "walls 300 / base 400 (C18 CLOSED by RC1 - ruled at 400)", "Drainage DR1 sump schedule / master F.1", "[C]"),
    ("Concrete volumes: mat 81.8, roof net 112.0, perimeter walls 103.7, W6/W7 12.8, "
     "W5 3.2, headhouse 32.7, main stair 3.0, entry stairwell 19.9 = 369.2 m3",
     "Structural CAD SC1, REINFORCEMENT_SUMMARY.md", "[C]"),
    ("Reinforcement 70.457 t total; T12 20.318 t, T16 23.707 t, T20 10.923 t, "
     "T25 15.439 t, T10 0.063 t, T8 0.006 t", "Structural CAD SC1 BBS_MASTER", "[C]"),
    ("Sentry post external 4000 x 5000, internal 3600 x 4600; grid 3650 x 4650 c/c; "
     "C1 350 x 350 x4; B1/B2 250 x 450; S1 150; PB 250 x 400 at +0.450; "
     "F1 1500 x 1500 x 600 at -2.000", "master A.4.8 / L", "[C]"),
    ("Sentry levels +0.450 GF, +3.650 first floor, +6.700 roof, +7.000 parapet",
     "master A.4.3", "[C]"),
    ("Sentry roof 300 projection with 300 high parapet over",
     "Rev F drawing 4 text", "[C]"),
    ("Sentry openings: D1 900 in the west wall at Y 1000-1900 both floors; "
     "W1 1200 in the east wall at Y 1900-3100 (ground); eight armoured vision "
     "panels 1200 wide, two per face (first floor)",
     "Rev F drawings 3 and 4, parsed", "[C]"),
    ("Sentry infill height 2600 (0.200 x 2.600 x 25 = 13.000 kN/m)",
     "master A.7.7 / Rev F drawing 6", "[C]"),
    ("Sentry reinforcement: S1 T8@150 B/W + T8@300 edge + T8@200 torsion 700sq x4 "
     "corners; B1 4-T16/2-T16; B2 3-T20/2-T20; hoops T8@100 over 2d / @150; "
     "C1 8-T16 with T10 hoops+cross-ties @85 over 500 and T8@150 elsewhere; "
     "PB 3-T12+3-T12; F1 T12@150 B/W", "master F.4", "[C]"),
    ("Sentry cover 30 beams+slabs, 40 columns, 50 footings; M30; Ld 46 phi",
     "master A.5", "[C]"),
    ("Rockhead -1.500 to -2.000", "master A.6", "[A] in the master"),
    ("Design GWT -2.000 (monsoon)", "master A.6", "[A] in the master"),
]

lines = []


def w(s=""):
    lines.append(s)


def hdr(t):
    w()
    w("=" * 78)
    w(t)
    w("=" * 78)


def sub(t):
    w()
    w("-" * 78)
    w(t)
    w("-" * 78)


Q = OrderedDict()          # code -> (description, unit, quantity, class, note)


def rec(code, desc, unit, qty, cls, note=""):
    Q[code] = (desc, unit, qty, cls, note)
    return qty


# ===========================================================================
w("QUANTITY DERIVATION FOR THE WORKS MANAGEMENT BILL OF QUANTITIES")
w("Underground CBRN-hardened blast-resistant protective structure + sentry post")
w("Pune, Maharashtra.  Works Management package revision WM1.")
w("Geometry: architectural Rev F, structural Phase 2 Rev A + M1.")
w()
w("Evidence classes:  [C] confirmed   [D] derived here   [A] assumed by this")
w("package   [N] not available from the project record.")
w()
w("ALL DIMENSIONS IN METRES UNLESS STATED.  Origin, axes and levels are those of")
w("master A.4.1: X east 0-22.000, Y north 0-6.200, levels relative to grade 0.000.")

hdr("0.  INPUTS AND THEIR SOURCES")
for i, (val, src, cls) in enumerate(SOURCES, 1):
    w("%2d.  %-8s %s" % (i, cls, val))
    w("     source: %s" % src)

# ===========================================================================
hdr("1.  EARTHWORK")

sub("1.1  Working space and excavation envelope")
BOX_L, BOX_W = 22.000, 6.200
WORK_SPACE = 1.000
w("Box external footprint                       = %.3f x %.3f = %.2f m2  [C]"
  % (BOX_L, BOX_W, BOX_L * BOX_W))
w("Working space outside the external wall face = %.3f m each side       [A]" % WORK_SPACE)
w("  Basis: the external wall face carries a formed finish (50 cover, master A.5)")
w("  and a continuous external tanking membrane WP-01 with a protection layer")
w("  (Schedule of Finishes FN1).  Both are applied from outside the structure, so")
w("  the excavation cannot be taken to the wall face.  1.000 m is the minimum")
w("  practical working width for membrane application and inspection.")
EXC_L = BOX_L + 2 * WORK_SPACE
EXC_W = BOX_W + 2 * WORK_SPACE
EXC_A = EXC_L * EXC_W
w("Excavation plan                              = %.3f x %.3f = %.2f m2  [D]"
  % (EXC_L, EXC_W, EXC_A))
w()
w("Faces are taken VERTICAL, unbenched.  Basis: master A.6 records the ground as")
w("Deccan basalt with rockhead at (-)1.500 to (-)2.000, i.e. only the top ~1.75 m")
w("is soil.  The rock face stands unsupported; the soil face above it is battered")
w("or supported as temporary works (WBS 2.2).  No batter volume is added, so the")
w("figure is a LOWER BOUND on bulk excavation.  [A]")

sub("1.2  Bulk excavation, main shelter")
DEPTH = 6.800
w("Formation (-)6.800, grade 0.000  ->  depth = %.3f m  [C]" % DEPTH)
V_EXC = EXC_A * DEPTH
w("Total bulk excavation = %.2f x %.3f = %.1f m3  [D]" % (EXC_A, DEPTH, V_EXC))
rec("E-02", "Bulk excavation, main shelter, 0.000 to (-)6.800, all strata",
    "m3", V_EXC, "[D]")
w()
w("Split by stratum — the rockhead is [A] in the master at (-)1.500 to (-)2.000,")
w("so the split is given at BOTH bounds and at the mean.  The total is unaffected.")
w()
w("  rockhead      soil m3        rock m3")
for rh in (1.500, 1.750, 2.000):
    w("  (-)%.3f     %8.1f       %8.1f%s"
      % (rh, EXC_A * rh, EXC_A * (DEPTH - rh),
         "   <- mean adopted" if rh == 1.750 else ""))
RH = 1.750
V_SOIL = EXC_A * RH
V_ROCK = EXC_A * (DEPTH - RH)
rec("E-02a", "  of which excavation in soil / weathered overburden", "m3", V_SOIL, "[D]",
    "rockhead (-)1.750 mean; range 295.2-393.6")
rec("E-02b", "  of which excavation in rock (Deccan basalt)", "m3", V_ROCK, "[D]",
    "rockhead (-)1.750 mean; range 944.6-1043.0")

sub("1.3  Site clearance and stripping")
CLEAR_MARGIN = 5.000
CLEAR_A = (BOX_L + 2 * (WORK_SPACE + CLEAR_MARGIN)) * (BOX_W + 2 * (WORK_SPACE + CLEAR_MARGIN))
w("Cleared area = excavation envelope + %.1f m working margin all round  [A]" % CLEAR_MARGIN)
w("             = %.3f x %.3f = %.1f m2" % (EXC_L + 2 * CLEAR_MARGIN, EXC_W + 2 * CLEAR_MARGIN, CLEAR_A))
w("Excludes the sentry post compound and the access route: NO SITE PLAN EXISTS in")
w("the project (Drainage DR1 open item D3), so the true cleared area is [N].")
rec("E-01", "Site clearance, grubbing and stripping topsoil 150 thk, shelter area",
    "m2", CLEAR_A, "[A]", "no site plan exists - re-measure")
rec("E-01a", "  topsoil stripped and stockpiled for re-use in the concealment layer",
    "m3", CLEAR_A * 0.150, "[A]")

sub("1.4  Sump pit SU-01, additional excavation below formation")
SUMP_CL = 1.500
SUMP_WALL = 0.300
SUMP_BASE_T = 0.400
sump_ext = SUMP_CL + 2 * SUMP_WALL
sump_exc_side = sump_ext + 2 * 0.300
sump_depth = 8.100 - 6.800
w("Pit clear 1.500 x 1.500 x 1.500; invert (-)7.600; base slab (-)8.000  [C]")
w("Walls 300 / base 400 (master F.1; C18 CLOSED by RC1 - ruled at 400)     [C]")
w("Pit external = 1.500 + 2 x 0.300 = %.3f m square" % sump_ext)
w("Excavation with 0.300 working space = %.3f m square                    [A]" % sump_exc_side)
w("Depth below the main formation = (-)8.100 (u/s blinding) - (-)6.800 = %.3f m" % sump_depth)
V_SUMP_EXC = sump_exc_side ** 2 * sump_depth
w("Volume = %.3f^2 x %.3f = %.2f m3 in rock  [D]" % (sump_exc_side, sump_depth, V_SUMP_EXC))
rec("E-03", "Excavation in rock for sump pit SU-01, below general formation",
    "m3", V_SUMP_EXC, "[D]")

sub("1.5  Covered entry stairwell — excavation outside the box envelope")
w("Stairwell external 9250-16050 (X) x 5750-7750 (Y)  [C]")
w("The box excavation envelope already extends to Y = 6.200 + 1.000 = 7.200.")
w("Additional strip = Y 7.200 to 7.750 = 0.550 wide, plus 1.000 working space")
strip_w = (7.750 - 7.200) + WORK_SPACE
strip_l = 16.050 - 9.250 + 2 * WORK_SPACE
w("            = %.3f wide x %.3f long" % (strip_w, strip_l))
w("Mean depth: the raft steps from 0.000 at the head to (-)2.000 at the platform;")
w("u/s of the 300 raft on 100 blinding -> (-)0.400 to (-)2.400.  Mean %.3f m  [A]" % 1.400)
V_STAIRWELL_EXC = strip_w * strip_l * 1.400
w("Volume = %.3f x %.3f x %.3f = %.1f m3  [D]" % (strip_w, strip_l, 1.400, V_STAIRWELL_EXC))
w("Plus the stepped excavation WITHIN the box envelope, which is part of E-02.")
rec("E-04", "Excavation for the covered entry stairwell, outside the box envelope",
    "m3", V_STAIRWELL_EXC, "[D]")

sub("1.6  Sentry post — excavation")
F1_L, F1_T = 1.500, 0.600
f1_exc_side = F1_L + 2 * 0.300
f1_depth = 2.100
w("F1 1500 x 1500 x 600, 4 No., founded on in-situ basalt at (-)2.000  [C]")
w("Excavation to u/s of 100 blinding = (-)2.100; site grade taken as 0.000  [A]")
w("  (no sentry-post site level exists in the project; +0.450 GF FFL implies a")
w("   plinth of 450 above the surrounding ground - master A.4.3)")
w("Pit %.3f square (0.300 working space) x %.3f deep, 4 No." % (f1_exc_side, f1_depth))
V_F1_EXC = 4 * f1_exc_side ** 2 * f1_depth
w("Volume = 4 x %.3f^2 x %.3f = %.2f m3  [D]" % (f1_exc_side, f1_depth, V_F1_EXC))
rec("E-05", "Excavation for sentry post footings F1, 4 No., in soil and rock",
    "m3", V_F1_EXC, "[D]")
sen_fill_a = 3.600 * 4.600
V_SEN_FILL = sen_fill_a * 0.450
w()
w("Filling under the sentry post ground floor: internal 3.600 x 4.600 = %.2f m2"
  % sen_fill_a)
w("from grade 0.000 to FFL +0.450 = %.3f m3  [D]" % V_SEN_FILL)
rec("E-06", "Filling in compacted granular fill under the sentry post ground floor",
    "m3", V_SEN_FILL, "[D]")

sub("1.7  Backfill and disposal")
side_area = EXC_A - BOX_L * BOX_W
w("Side working-space plan area = %.2f - %.2f = %.2f m2  [D]"
  % (EXC_A, BOX_L * BOX_W, side_area))
V_SIDE_BF = side_area * (6.800 - 2.000)
w("Side backfill, formation (-)6.800 to top of slab (-)2.000, depth 4.800 m")
w("           = %.2f x 4.800 = %.1f m3  [D]" % (side_area, V_SIDE_BF))
w("Above (-)2.000 the side zone merges into the engineered cover and the berm and")
w("is measured in section 5.")
rec("E-07", "Side backfill in selected granular fill, 250 layers to 95 % MDD",
    "m3", V_SIDE_BF, "[D]")
V_DISPOSAL = V_EXC + V_SUMP_EXC + V_STAIRWELL_EXC + V_F1_EXC - V_SIDE_BF
w()
w("Surplus for disposal / re-use:")
w("  total excavated  = %.1f + %.1f + %.1f + %.1f = %.1f m3"
  % (V_EXC, V_SUMP_EXC, V_STAIRWELL_EXC, V_F1_EXC,
     V_EXC + V_SUMP_EXC + V_STAIRWELL_EXC + V_F1_EXC))
w("  less side backfill                             = %.1f m3" % V_SIDE_BF)
w("  gross surplus (bank measure, no bulking)       = %.1f m3  [D]" % V_DISPOSAL)
w("Bulking on rock excavation is typically 40-60 %; the loose volume to be handled")
w("is therefore materially larger.  Bulking factor not applied - [A] not stated in")
w("the project.  Excavated basalt is a DESIGNATED SOURCE for the 500 crushed")
w("rubble layer of the engineered cover (section 5) - see the methodology note.")
rec("E-08", "Surplus excavated material - re-use on site as engineered fill / "
    "crushed rubble, remainder to spoil", "m3", V_DISPOSAL, "[D]",
    "bank measure; bulking not applied")

# ===========================================================================
hdr("2.  CONCRETE — MAIN SHELTER AND ENTRY STRUCTURES")

sub("2.1  Structural concrete volumes carried forward from Structural CAD SC1")
w("The following are taken verbatim from Structural CAD/Schedules/")
w("REINFORCEMENT_SUMMARY.md (package SC1, 4 Sep 2026) and are re-derived here as")
w("an arithmetic check only.  They are NOT re-designed.")
w()
SC1 = OrderedDict([
    ("Mat 600 (M35)", 81.8),
    ("Pressure slab 900, net of openings (M35)", 112.0),
    ("Perimeter walls 600 (M35)", 103.7),
    ("Walls W6 / W7 400 (M35)", 12.8),
    ("Wall W5 200 (M35)", 3.2),
    ("Headhouse walls 400 + roof 500 (M35)", 32.7),
    ("Main staircase, waist and landings (M35)", 3.0),
    ("Entry stairwell: walls, roof, raft, flight, landings (M35)", 19.9),
])
checks = {
    "Mat 600 (M35)":
        ("22.000 x 6.200 x 0.600", 22.0 * 6.2 * 0.6),
    "Pressure slab 900, net of openings (M35)":
        ("22.000 x 6.200 x 0.900 - void 2.800 x 3.160 x 0.900 - 2 x pi/4 x 1.400^2 x 0.900",
         22.0 * 6.2 * 0.9 - 2.8 * 3.16 * 0.9 - 2 * math.pi / 4 * 1.4 ** 2 * 0.9),
    "Perimeter walls 600 (M35)":
        ("(22.000 x 6.200 - 20.800 x 5.000) x 3.200",
         (22.0 * 6.2 - 20.8 * 5.0) * 3.2),
    "Walls W6 / W7 400 (M35)":
        ("2 x 0.400 x 5.000 x 3.200", 2 * 0.4 * 5.0 * 3.2),
    "Wall W5 200 (M35)":
        ("0.200 x 5.000 x 3.200", 0.2 * 5.0 * 3.2),
    "Headhouse walls 400 + roof 500 (M35)":
        ("(4.800 x 5.800 - 4.000 x 5.000) x 2.400 + 4.800 x 5.800 x 0.500",
         (4.8 * 5.8 - 4.0 * 5.0) * 2.4 + 4.8 * 5.8 * 0.5),
}
tot_sc1 = 0.0
for k, v in SC1.items():
    tot_sc1 += v
    if k in checks:
        expr, val = checks[k]
        flag = "OK" if abs(val - v) < 0.15 else "*** CHECK ***"
        w("  %-52s %7.1f m3   check %s = %.2f  %s" % (k, v, expr, val, flag))
    else:
        w("  %-52s %7.1f m3   (composite - accepted from SC1)" % (k, v))
w("  %-52s %7.1f m3" % ("TOTAL, SC1 in-scope", tot_sc1))
w()
w("Six of the eight lines reproduce exactly.  The main staircase and the entry")
w("stairwell are composite figures that SC1 built element by element; they are")
w("accepted as they stand and are not re-derived here.")
for k, v in SC1.items():
    code = "C-%02d" % (list(SC1).index(k) + 1)
    rec(code, k, "m3", v, "[C]", "Structural CAD SC1")

sub("2.2  Concrete NOT in the SC1 figure — derived here")
w("SC1 explicitly excludes the blinding, the sump pit, the burster slab, the")
w("escape-shaft collars, the local roof thickenings and the sentry post.")
w()
V_PCC_BOX = (BOX_L + 0.2) * (BOX_W + 0.2) * 0.100
w("Blinding M15 100 thk under the mat, projecting 100 all round:")
w("  = %.3f x %.3f x 0.100 = %.2f m3  [D]" % (BOX_L + 0.2, BOX_W + 0.2, V_PCC_BOX))
rec("C-09", "Blinding / PCC M15, 100 thk under the mat", "m3", V_PCC_BOX, "[D]")

V_PCC_SUMP = (sump_ext + 0.2) ** 2 * 0.100
V_PCC_F1 = 4 * (F1_L + 0.2) ** 2 * 0.100
V_PCC_SW = (16.050 - 9.250) * (7.750 - 5.750) * 0.100
w("Blinding M15 under the sump pit    = %.3f^2 x 0.100 = %.2f m3  [D]"
  % (sump_ext + 0.2, V_PCC_SUMP))
w("Blinding M15 under F1, 4 No.       = 4 x %.3f^2 x 0.100 = %.2f m3  [D]"
  % (F1_L + 0.2, V_PCC_F1))
w("Blinding M15 under the stairwell raft = %.3f x %.3f x 0.100 = %.2f m3  [D]"
  % (16.050 - 9.250, 7.750 - 5.750, V_PCC_SW))
rec("C-10", "Blinding / PCC M15, 100 thk, sump pit, footings F1 and stairwell raft",
    "m3", V_PCC_SUMP + V_PCC_F1 + V_PCC_SW, "[D]")

w()
V_SUMP_WALLS = (sump_ext ** 2 - SUMP_CL ** 2) * (7.600 - 6.700)
V_SUMP_BASE = sump_ext ** 2 * SUMP_BASE_T
w("Sump pit SU-01, below the mat soffit (-)6.700:")
w("  walls 300, (-)6.700 to (-)7.600 = (%.3f^2 - %.3f^2) x 0.900 = %.2f m3"
  % (sump_ext, SUMP_CL, V_SUMP_WALLS))
w("  base slab 400, (-)8.000 to (-)7.600 = %.3f^2 x 0.400 = %.2f m3"
  % (sump_ext, V_SUMP_BASE))
w("  total = %.2f m3 M35  [D]" % (V_SUMP_WALLS + V_SUMP_BASE))
w("NOTE: the 81.8 m3 mat volume is NOT reduced for the 1.500 x 1.500 pit opening")
w("through the 600 mat (1.35 m3).  SC1 measured the mat gross; that convention is")
w("kept, so the BOQ is conservative by 1.35 m3.  DECLARED, not hidden.")
rec("C-11", "Sump pit SU-01 walls 300 and base 400 below the mat soffit (M35)",
    "m3", V_SUMP_WALLS + V_SUMP_BASE, "[D]")

w()
collar_area = math.pi / 4 * (1.900 ** 2 - 1.400 ** 2)
h1, h2 = 2.000 + 0.150, 2.000 + 0.700
V_ESC = collar_area * (h1 + h2)
w("Escape shaft collars, 250 RC, OD 1900 / ID 1400:")
w("  annulus area = pi/4 x (1.900^2 - 1.400^2) = %.3f m2" % collar_area)
w("  ESC 1: top of roof slab (-)2.000 to head +0.150 = %.3f m" % h1)
w("  ESC 2: top of roof slab (-)2.000 to head +0.700 = %.3f m" % h2)
w("  volume = %.3f x (%.3f + %.3f) = %.2f m3 M35  [D]" % (collar_area, h1, h2, V_ESC))
rec("C-12", "Escape shaft collars ESC 1 and ESC 2, 250 RC, OD 1900 (M35)",
    "m3", V_ESC, "[D]")

w()
thick_annulus = math.pi * (1.550 ** 2 - 0.950 ** 2)
V_THICK_ESC = 2 * thick_annulus * 0.300
V_THICK_VOID = 2.800 * 0.600 * 0.300
w("Local roof thickenings 900 -> 1200 (master F.1):")
w("  at each shaft, over a 600 annulus: pi x (1.550^2 - 0.950^2) = %.3f m2"
  % thick_annulus)
w("    2 No. x %.3f x 0.300 extra = %.2f m3" % (thick_annulus, V_THICK_ESC))
w("  at the stair-void free edge, 2.800 long x 600 wide x 0.300 extra = %.2f m3"
  % V_THICK_VOID)
w("  total = %.2f m3 M35  [D]" % (V_THICK_ESC + V_THICK_VOID))
rec("C-13", "Local thickenings of the pressure slab 900->1200 at openings (M35)",
    "m3", V_THICK_ESC + V_THICK_VOID, "[D]")

w()
w8_len = 5.000
w8_gap_a = 0.900 * (3.400 - 2.500)
V_W8 = 4 * (0.110 * (w8_len * 3.200 - 0.900 * 2.100))
w("W8 partitions, 4 No. @ 110, 5.000 long x 3.200 high, each with a 900 door gap")
w("  door opening taken 900 wide x 2100 high  [A] - the master confirms the 900")
w("  gap at Y 2500-3400 but states no head height; 2100 is the project convention")
w("  for every other door (master A.2, A.4.6, A.4.7).")
w("  = 4 x 0.110 x (5.000 x 3.200 - 0.900 x 2.100) = %.2f m3" % V_W8)
w("  W8 is NON-STRUCTURAL, A252 mesh both faces (master F.1).  Material grade is")
w("  not stated - measured as M35 with the rest of the box.  [A]")
rec("C-14", "Internal partitions W8, 4 No., 110 thk, non-structural",
    "m3", V_W8, "[D]")

TOT_M35 = tot_sc1 + V_SUMP_WALLS + V_SUMP_BASE + V_ESC + V_THICK_ESC + V_THICK_VOID + V_W8
TOT_M15 = V_PCC_BOX + V_PCC_SUMP + V_PCC_F1 + V_PCC_SW
w()
w("TOTAL M35 STRUCTURAL CONCRETE, shelter + entry structures = %.1f m3  [D]" % TOT_M35)
w("TOTAL M15 BLINDING                                        = %.1f m3  [D]" % TOT_M15)

# ===========================================================================
hdr("3.  REINFORCEMENT")

sub("3.1  Shelter and entry structures — carried forward from SC1")
BBS = OrderedDict([("T8", 5.7), ("T10", 63.3), ("T12", 20318.3),
                   ("T16", 23707.1), ("T20", 10922.8), ("T25", 15439.4)])
for k, v in BBS.items():
    w("  %-5s %10.1f kg" % (k, v))
TOT_REBAR = sum(BBS.values())
w("  %-5s %10.1f kg = %.3f t  [C]" % ("TOTAL", TOT_REBAR, TOT_REBAR / 1000))
w()
w("Fe500D to IS 1786:2008.  SENTRY POST EXPLICITLY EXCLUDED from this figure.")
w("SC1 declares the basis: cut length = sum of scheduled legs with NO bend")
w("deduction, laps at 50 phi added, stock bar 12 000.  Conservative by about")
w("2 phi per 90 degree bend.  Bend deductions to BS 8666 Table 3 are the")
w("fabricator's on the approved schedule.")
for k, v in BBS.items():
    rec("R-%s" % k, "Reinforcement %s Fe500D, shelter and entry structures" % k,
        "t", v / 1000, "[C]", "Structural CAD SC1")

sub("3.2  Reinforcement NOT in the SC1 figure")
w("SC1 excludes: the burster slab, the sentry post, waterstops, EMP straps,")
w("spacers, chairs and tying wire.  The first two are derived below; the")
w("remainder are measured as separate items and are not reinforcement.")

# burster slab reinforcement
w()
w("BURSTER SLAB, M30, 200 thk, T12 @ 150 both ways (master A.7.3):")
# area computed in section 5; forward reference
HH_PLAN = 4.800 * 5.800
esc_head_area = 2 * math.pi / 4 * 1.900 ** 2
COVER_A = BOX_L * BOX_W - HH_PLAN - esc_head_area
w("  area = box footprint %.2f - headhouse %.2f - shaft heads %.2f = %.2f m2"
  % (BOX_L * BOX_W, HH_PLAN, esc_head_area, COVER_A))
w("  (the headhouse has NO earth cover - master A.4.6 - so the cover, and with it")
w("   the burster slab, stops at the headhouse walls)")
n_bars_x = COVER_A ** 0.5  # not used; explicit grid below
# T12 @ 150 both ways, both directions, one layer B/W as stated
grid_len_per_m2 = 2 * (1 / 0.150)          # m of bar per m2, both ways
burster_len = COVER_A * grid_len_per_m2
burster_kg = burster_len * 0.888
w("  bar length = %.2f m2 x 2 x (1 / 0.150) = %.0f m" % (COVER_A, burster_len))
w("  weight     = %.0f x 0.888 kg/m = %.0f kg = %.3f t  [D]"
  % (burster_len, burster_kg, burster_kg / 1000))
w("  laps and wastage NOT added - [A], add 5 % at procurement (section 3.4).")
rec("R-BS", "Reinforcement T12 Fe500 to the burster slab (M30)", "t",
    burster_kg / 1000, "[D]")

# ---------------------------------------------------------------------------
sub("3.3  Sentry post reinforcement — derived from master F.4")
w("The sentry post has never been quantified anywhere in the project.  The")
w("reinforcement below is derived from the CONFIRMED arrangement in master F.4.")
w("It is an ESTIMATING quantity for tender only and must be replaced by the")
w("fabricator's approved bar bending schedule.  [D]")
w()
UM = {8: 0.395, 10: 0.617, 12: 0.888, 16: 1.578, 20: 2.466, 25: 3.853}
sen = OrderedDict((d, 0.0) for d in UM)          # dia -> metres


def add(dia, metres, note):
    sen[dia] += metres
    w("    %-62s T%-2d %8.1f m" % (note, dia, metres))


w("  FOOTINGS F1, 4 No., 1500 x 1500 x 600, T12 @ 150 both ways bottom:")
n = int(1.500 / 0.150) + 1
add(12, 4 * 2 * n * (1.500 - 2 * 0.050), "4 footings x 2 ways x %d bars x 1.400 long" % n)

w("  COLUMNS C1, 4 No., 350 x 350, 8-T16 from footing top (-)1.400 to +6.700:")
col_h = 6.700 - (-1.400)
add(16, 4 * 8 * (col_h + 0.920), "4 col x 8 bars x (%.3f + one lap 46phi = 0.920)" % col_h)
w("    confining hoops T10 + 1 cross-tie each way @ 85 over 500 from every joint")
w("    face, top and bottom, and through the joint (master F.4):")
hoop_per = 2 * (0.350 - 2 * 0.040) + 2 * (0.350 - 2 * 0.040) + 2 * 10 * 0.010
tie_per = 2 * (0.350 - 2 * 0.040) + 2 * 10 * 0.010
n_conf_zones = 4 * (2 * 2 + 2)      # 4 columns: 2 storeys x (top+bottom) + 2 joints
n_hoops_zone = int(0.500 / 0.085) + 1
add(10, n_conf_zones * n_hoops_zone * (hoop_per + 2 * tie_per),
    "%d zones x %d hoops x (hoop %.3f + 2 ties %.3f)"
    % (n_conf_zones, n_hoops_zone, hoop_per, tie_per))
gen_tie_len = col_h - n_conf_zones / 4 * 0.500
n_gen = int(gen_tie_len / 0.150) + 1
add(8, 4 * n_gen * hoop_per, "general ties T8 @ 150 elsewhere, 4 col x %d" % n_gen)

w("  BEAMS B1 (3650 c/c, 2 No. per level) and B2 (4650 c/c, 2 No. per level),")
w("  250 x 450, at first floor and roof = 2 levels:")
add(16, 2 * 2 * 4 * (3.650 + 2 * 0.400), "B1 4-T16 top at supports, 2 lvl x 2 bm x 4")
add(16, 2 * 2 * 2 * (3.650 + 2 * 0.400), "B1 2-T16 bottom continuous, 2 lvl x 2 bm x 2")
add(20, 2 * 2 * 3 * (4.650 + 2 * 0.400), "B2 3-T20 top at supports, 2 lvl x 2 bm x 3")
add(20, 2 * 2 * 2 * (4.650 + 2 * 0.400), "B2 2-T20 bottom continuous, 2 lvl x 2 bm x 2")
bm_hoop = 2 * (0.250 - 2 * 0.030) + 2 * (0.450 - 2 * 0.030) + 2 * 10 * 0.008
n_h_dense = 2 * (int(0.810 / 0.100) + 1)
n_b1_mid = int((3.650 - 2 * 0.810) / 0.150) + 1
n_b2_mid = int((4.650 - 2 * 0.810) / 0.150) + 1
add(8, 2 * 2 * (n_h_dense + n_b1_mid) * bm_hoop,
    "B1 hoops @100 over 2d=810 each end, @150 mid, hoop %.3f" % bm_hoop)
add(8, 2 * 2 * (n_h_dense + n_b2_mid) * bm_hoop,
    "B2 hoops @100 over 2d=810 each end, @150 mid")

w("  PLINTH BEAM PB 250 x 400, 15.200 m clear total, 3-T12 top + 3-T12 bottom:")
add(12, 6 * 15.200, "PB 6 bars x 15.200")
pb_hoop = 2 * (0.250 - 2 * 0.030) + 2 * (0.400 - 2 * 0.030) + 2 * 10 * 0.008
add(8, (int(15.200 / 0.150) + 1) * pb_hoop, "PB hoops T8 @ 150")

w("  SLAB S1 150, two levels.  First floor 4.000 x 5.000; roof 4.600 x 5.600")
w("  (300 projection all round - Rev F drawing 4):")
for lvl, (a, b) in (("first floor", (4.000, 5.000)), ("roof", (4.600, 5.600))):
    nx = int(b / 0.150) + 1
    ny = int(a / 0.150) + 1
    add(8, nx * a + ny * b, "S1 %s bottom T8 @ 150 both ways" % lvl)
    add(8, 2 * (int(b / 0.300) + 1) * 0.400 + 2 * (int(a / 0.300) + 1) * 0.400,
        "S1 %s edge top T8 @ 300, 0.400 into the span, 4 edges" % lvl)
    n_t = int(0.700 / 0.200) + 1
    add(8, 4 * 4 * 2 * n_t * 0.700,
        "S1 %s torsion T8 @ 200, 4 layers, 700 sq, 4 corners" % lvl)

w("  PARAPET 300 high over the roof projection, perimeter 2 x (4.600 + 5.600):")
w("    reinforcement NOT DESIGNED anywhere in the project  [N]")
w("    nominal T8 @ 200 vertical + 2-T8 horizontal allowed for estimating  [A]")
par_p = 2 * (4.600 + 5.600)
add(8, (int(par_p / 0.200) + 1) * 0.600 + 2 * par_p, "parapet nominal [A]")

w()
w("  SENTRY POST REINFORCEMENT SUMMARY")
sen_kg = 0.0
for d, m in sen.items():
    if m > 0:
        kg = m * UM[d]
        sen_kg += kg
        w("    T%-2d  %9.1f m x %.3f kg/m = %8.1f kg" % (d, m, UM[d], kg))
        rec("R-S%d" % d, "Reinforcement T%d Fe500, sentry post" % d, "t",
            kg / 1000, "[D]")
w("    %-38s %8.1f kg = %.3f t  [D]" % ("TOTAL SENTRY POST", sen_kg, sen_kg / 1000))
w()
sen_conc = None  # set later
w("  Cut lengths are scheduled leg lengths with no bend deduction, the same")
w("  convention SC1 declares.  Laps are included only where explicitly noted.")
w()
w("  SANITY CHECK.  Sentry post frame concrete is derived in section 7.1 as")
w("  20.95 m3, giving a steel density of about %.0f kg/m3.  For a small two-storey"
  % (sen_kg / 20.95))
w("  RC frame with IS 13920 ductile detailing (T10 confining hoops at 85 c/c over")
w("  500 from every joint face) that is a plausible figure.  It is a SANITY CHECK,")
w("  NOT a design check.")

sub("3.4  Procurement allowance")
w("Rolling margin, offcuts and wastage on cut-and-bend reinforcement are")
w("conventionally 3-5 %.  5 % is adopted for ordering.  [A]")
order = (TOT_REBAR + burster_kg + sen_kg) * 1.05 / 1000
w("Order quantity = (%.0f + %.0f + %.0f) x 1.05 = %.2f t  [D]"
  % (TOT_REBAR, burster_kg, sen_kg, order))
rec("R-ORD", "Reinforcement ORDER quantity, all works, incl. 5 % wastage",
    "t", order, "[D]")

# ===========================================================================
hdr("4.  FORMWORK")
w("Measured to IS 1200 (Part 5) principles: contact area of shuttering.")
w("Rates of re-use are a contractor's matter and are not assumed here.")
w()
FW = OrderedDict()
FW["Mat 600 - edges only"] = 2 * (BOX_L + BOX_W) * 0.600
FW["Perimeter walls 600 - external face"] = 2 * (BOX_L + BOX_W) * 3.200
FW["Perimeter walls 600 - internal face"] = 2 * (20.800 + 5.000) * 3.200
FW["Wall W5 200 - both faces"] = 2 * 5.000 * 3.200
FW["Walls W6 / W7 400 - both faces"] = 2 * 2 * 5.000 * 3.200
FW["Pressure slab 900 - soffit (net of the stair void)"] = 20.800 * 5.000 - 2.800 * 3.160
FW["Pressure slab 900 - external edge"] = 2 * (BOX_L + BOX_W) * 0.900
FW["Pressure slab 900 - void and opening edges"] = (2 * (2.800 + 3.160) + 2 * math.pi * 0.700) * 0.900
FW["Headhouse walls 400 - both faces"] = (2 * (4.800 + 5.800) + 2 * (4.000 + 5.000)) * 2.400
FW["Headhouse roof 500 - soffit and edge"] = 4.000 * 5.000 + 2 * (4.800 + 5.800) * 0.500
FW["Escape shaft collars - internal and external"] = (math.pi * 1.400 + math.pi * 1.900) * (h1 + h2) / 2
FW["Sump pit SU-01"] = 4 * SUMP_CL * 1.500 + 4 * sump_ext * 0.900
_flight_going = 7 * 0.280
_flight_rise = 8 * 0.1708333
_waist_len = math.hypot(_flight_going, _flight_rise)
FW["Main staircase - waist soffit, 3 flights x 8R"] = 3 * _waist_len * 1.200
FW["Main staircase - risers"] = 24 * 1.200 * 0.1708333
FW["Main staircase - landing soffits L1 and L2"] = 2 * 2.800 * 1.200
FW["Entry stairwell - walls 250 both faces"] = (2 * (6.800 + 2.000) + 2 * (6.300 + 1.500)) * 2.500
FW["Entry stairwell - raking roof soffit and flight waist"] = 6.300 * 1.500 + 3.300 * 1.500 * 1.15
FW["Entry stairwell - risers, landings and raft edges"] = 12 * 1.500 * 0.1666667 + 2 * 1.500 * 1.500 + 2 * (6.800 + 2.000) * 0.300
FW["W8 partitions 110 - both faces"] = 4 * 2 * (5.000 * 3.200 - 0.900 * 2.100)
FW["Burster slab M30 - edge only"] = 2 * (BOX_L + BOX_W) * 0.200
tot_fw = 0.0
for k, v in FW.items():
    tot_fw += v
    w("  %-58s %8.1f m2" % (k, v))
w("  %-58s %8.1f m2  [D]" % ("TOTAL, shelter and entry structures", tot_fw))
rec("F-01", "Formwork, shelter and entry structures, contact area", "m2", tot_fw, "[D]")
w()
w("Falsework to the pressure slab soffit: %.0f m2 of deck at 3.200 m height, and"
  % (20.800 * 5.000))
w("IS 456 Table 11 requires the props to a slab spanning over 4.5 m (this one spans")
w("5.000 m clear) to stay in place 14 DAYS.  That is a programme driver, not just a")
w("quantity - see the schedule basis note.")
rec("F-02", "Falsework to the pressure slab soffit, 3.200 m height, props to remain "
    "14 days (IS 456 Table 11)", "m2", 20.800 * 5.000, "[D]")

# ===========================================================================
hdr("5.  ENGINEERED COVER, BACKFILL AND CONCEALMENT")
w("Build-up from master A.7.3, read from the TOP down; construction order is the")
w("reverse.  Total 2000 = 40.65 kPa  [C]")
w()
COVER = [("Topsoil / turf - concealment and erosion", 0.300, "concealment"),
         ("Granular filter", 0.150, "filter"),
         ("RC burster slab M30, T12 @ 150 B/W", 0.200, "burster"),
         ("Crushed basalt rubble 25-75 mm", 0.500, "rubble"),
         ("Compacted engineered fill @ 95 % MDD", 0.750, "fill"),
         ("Protection screed over the membrane", 0.100, "screed")]
w("Plan area of the cover:")
w("  box footprint                       %8.2f m2" % (BOX_L * BOX_W))
w("  less headhouse (no earth cover)     -%7.2f m2   master A.4.6" % HH_PLAN)
w("  less escape shaft heads, 2 x OD 1900 -%7.2f m2" % esc_head_area)
w("  cover area                          %8.2f m2  [D]" % COVER_A)
w()
tot_cover = 0.0
for name, t, code in COVER:
    v = COVER_A * t
    tot_cover += v
    w("  %-48s %5.3f m  %7.2f m3" % (name, t, v))
    rec("B-%s" % code, name, "m3", v, "[D]")
w("  %-48s %5.3f m  %7.2f m3  [D]" % ("TOTAL ENGINEERED COVER", 2.000, tot_cover))
w()
w("The 500 crushed basalt rubble layer (%.1f m3) is to be won from the rock"
  % (COVER_A * 0.500))
w("excavation (E-02b, %.0f m3 available) and crushed on site to 25-75 mm.  This is"
  % V_ROCK)
w("the single largest cost saving available on the job and it removes %.0f m3 of"
  % (COVER_A * 0.500))
w("import and the same volume of cart-away.")
w()
w("BERM: graded 1.5:1 against the headhouse and stairwell walls to +0.900, toe at")
w("grade over 1350 (master A.4.6 / A.4.7).  Its volume CANNOT be determined - no")
w("site plan or ground model exists in the project (Drainage DR1 open item D3).")
rec("B-berm", "Berm forming and grading, 1.5:1 to +0.900 against the headhouse and "
    "covered stairwell", "m3", None, "[N]", "no site plan exists")
rec("B-camo", "Camouflage and concealment measures beyond the 300 topsoil / turf "
    "layer", "item", None, "[N]",
    "no concealment specification exists in the project")

# ===========================================================================
hdr("6.  WATERPROOFING")
WP = OrderedDict()
WP["WP-01 tanking, horizontal on blinding under the mat"] = (BOX_L + 0.2) * (BOX_W + 0.2)
WP["WP-01 tanking, vertical to external wall faces, (-)6.700 to (-)2.000"] = \
    2 * (BOX_L + BOX_W) * (6.700 - 2.000)
_roof_net = BOX_L * BOX_W - 2.800 * 3.160 - esc_head_area
WP["WP-01 tanking, roof membrane, net of the void and shafts"] = _roof_net
WP["WP-01 upstands, fillets and dressing to openings and penetrations"] = \
    (2 * (2.800 + 3.160) + 2 * math.pi * 0.950 + 2 * (BOX_L + BOX_W)) * 0.500
WP["WP-02 protection screed 100 over the roof membrane (also cover layer 1)"] = COVER_A
WP["WP-06 headhouse and stairwell roofs, external grade + protection"] = \
    HH_PLAN + (16.050 - 9.250) * (7.750 - 5.750)
WP["WP-04 internal wet-area tanking - bays 2, 5 and 6, floor and walls to 2.000"] = None
tot_wp = 0.0
for k, v in WP.items():
    if v is None:
        w("  %-64s   [N] see below" % k)
    else:
        tot_wp += v
        w("  %-64s %8.1f m2" % (k, v))
        rec("W-%02d" % (list(WP).index(k) + 1), k, "m2", v, "[D]")
w("  %-64s %8.1f m2  [D]" % ("TOTAL (excluding WP-04)", tot_wp))
w()
_wet_floor = (1.800 * 2.000 + 1.800 * 3.000) + 1.560 * 5.000 + 2.000 * 5.000
_wet_wall = (2 * (1.800 + 5.000) + 2 * (1.560 + 5.000) + 2 * (2.000 + 5.000)) * 2.000
w("WP-04 wet areas are bay 2 (lavatory 1800 x 2000 + medical 1800 x 3000), bay 5")
w("(CBRN plant, 1560 wide) and bay 6 (decon airlock, 2000 wide) - master A.3 [C].")
w("  floor area = %.2f m2;  wall area to 2.000 high = %.2f m2  [D]"
  % (_wet_floor, _wet_wall))
w("Schedule of Finishes FN1 states WP-04 is 'turned up 150 and dressed to every")
w("gully and pipe sleeve'; the turn-up height for the full wall finish W-02 is")
w("'floor to soffit'.  2.000 m is adopted here for measurement only.  [A]")
rec("W-08", "WP-04 internal wet-area tanking, floors", "m2", _wet_floor, "[D]")
rec("W-09", "WP-04 internal wet-area tanking, walls, 2.000 high [A]", "m2", _wet_wall, "[A]")
rec("W-10", "Waterstops, 2 No. at every construction joint (WP-05), ~6 m centres",
    "m", 2 * (2 * (BOX_L + BOX_W) / 6.0) * 3.200 + 2 * (BOX_W * 4), "[A]",
    "joint positions not fixed in the project - re-measure")

# ===========================================================================
hdr("7.  SENTRY POST — CONCRETE, BRICK MASONRY AND FINISHES")
w("THE ONLY DESIGN CHANGE IN THIS PACKAGE: the sentry post walls are BRICK")
w("MASONRY, replacing the 200 RC ballistic infill panels of Rev F.  Reference SP-B1.")
w("Everything else in the sentry post is as the current project documentation.")

sub("7.1  Sentry post concrete (M30)")
SEN = OrderedDict()
SEN["Footings F1, 4 No., 1500 x 1500 x 600"] = 4 * F1_L * F1_L * F1_T
_colh = 6.700 - (-1.400)
SEN["Columns C1, 4 No., 350 x 350, (-)1.400 to +6.700"] = 4 * 0.350 * 0.350 * _colh
SEN["Plinth beam PB 250 x 400, 15.200 m clear"] = 15.200 * 0.250 * 0.400
SEN["Beams B1 / B2 250 x 450, rib below slab, 2 levels"] = 2 * 15.200 * 0.250 * (0.450 - 0.150)
SEN["Slab S1 150, first floor, 4.000 x 5.000"] = 4.000 * 5.000 * 0.150
SEN["Slab S1 150, roof, 4.600 x 5.600 incl. the 300 projection"] = 4.600 * 5.600 * 0.150
SEN["Parapet 300 high x 150 thk [A] over the roof projection"] = par_p * 0.300 * 0.150
sen_conc = 0.0
for k, v in SEN.items():
    sen_conc += v
    w("  %-58s %7.2f m3" % (k, v))
    rec("SC-%02d" % (list(SEN).index(k) + 1), "Sentry post: " + k, "m3", v, "[D]")
w("  %-58s %7.2f m3  [D]" % ("TOTAL M30, sentry post frame", sen_conc))
w()
w("Clear beam / plinth-beam length 15.200 m is derived once and used throughout:")
w("  B1 (grid A-B) 3.650 c/c - 0.350 column = 3.300, 2 No. = 6.600")
w("  B2 (grid 1-2) 4.650 c/c - 0.350 column = 4.300, 2 No. = 8.600")
w("  total clear run per level = 15.200 m  [D]")
w()
w("GROUND FLOOR SLAB ON GRADE: NOT DESIGNED anywhere in the project.  The member")
w("schedule on Rev F drawing 6 lists S1 at 'both levels', meaning the first floor")
w("and the roof only.  Carried as a provisional item.  [N]")
rec("SC-08", "Sentry post ground floor slab on grade - PROVISIONAL, not designed",
    "m2", sen_fill_a, "[N]", "thickness and specification to be confirmed")
rec("SC-09", "Sentry post: blinding / PCC M15 100 thk under F1, 4 No.",
    "m3", V_PCC_F1, "[D]")
rec("SC-10", "Sentry post: external spiral stair, 1000 R, 250 dia central pole",
    "item", 1, "[C]", "fabrication detail not in the project record")

sub("7.2  Sentry post BRICK MASONRY WALLS — reference SP-B1")
w("Wall run between columns, per storey (the same 15.200 m derived above):")
w("  north and south walls: 4.000 - 2 x 0.350 = 3.300 each, 2 No. = 6.600 m")
w("  east and west walls:   5.000 - 2 x 0.350 = 4.300 each, 2 No. = 8.600 m")
w("  total run per storey                                        = 15.200 m  [D]")
w()
INFILL_H = 2.600
w("Height of the masonry panel = %.3f m  [C]" % INFILL_H)
w("  This is the project's OWN confirmed figure: master A.7.7 gives the infill load")
w("  as 13.000 kN/m = 0.200 x 2.600 x 25, verified.  Rev F drawing 6 repeats")
w("  '200 x 2600 high'.")
w("  Geometric check, first storey: roof slab top +6.700 less 0.450 beam depth =")
w("  soffit +6.250; first floor +3.650; panel = 2.600 m  -> AGREES.")
w("  Geometric check, ground storey: first floor +3.650 less 0.450 = soffit +3.200;")
w("  GF FFL +0.450; panel = 2.750 m  -> 150 mm MORE than the project's own figure.")
w("  The project's confirmed 2.600 is used for BOTH storeys and the 150 mm")
w("  difference is carried as a verification item.  DECLARED, not resolved.  [U]")
w()
WALL_T = 0.190
w("Structural infill zone between the column faces = 0.200 m, unchanged from the")
w("Rev F infill.  [C]")
w("  The masonry is built as ONE-BRICK-THICK work in MODULAR bricks to IS 1077")
w("  (190 x 90 x 90), giving a 190 mm wall inside the 200 mm zone.  The residual")
w("  10 mm is taken up at the INTERNAL face and absorbed in the plaster, so the")
w("  external face stays flush with the column faces and the CONFIRMED 4000 x 5000")
w("  external envelope is preserved exactly.  [A]")
w("  Brickwork is therefore MEASURED at its actual 0.190 thickness (IS 1200 Pt 3),")
w("  not at the 200 zone width.")
w("  Conventional 230 x 110 x 75 bricks would give a 230 wall and would change the")
w("  external envelope - NOT PERMITTED without a further design change.")
w()
gross_per_storey = 15.200 * INFILL_H
w("Gross masonry area per storey = 15.200 x %.3f = %.2f m2  [D]"
  % (INFILL_H, gross_per_storey))
w()
w("GROUND STOREY deductions (Rev F drawing 3, parsed):")
DOOR_H, WIN_H = 2.100, 1.200
w("  D1 door   900 wide x %.3f high  [A height - project convention]  = %.2f m2"
  % (DOOR_H, 0.900 * DOOR_H))
w("  W1 window 1200 wide x %.3f high [A height - NOT STATED anywhere] = %.2f m2"
  % (WIN_H, 1.200 * WIN_H))
gf_ded = 0.900 * DOOR_H + 1.200 * WIN_H
gf_net = gross_per_storey - gf_ded
w("  net ground storey masonry = %.2f - %.2f = %.2f m2" % (gross_per_storey, gf_ded, gf_net))
w("  volume = %.2f x %.3f = %.2f m3  [D]" % (gf_net, WALL_T, gf_net * WALL_T))
w()
w("FIRST STOREY deductions (Rev F drawing 4, parsed):")
w("  8 No. armoured vision panels 1200 wide, 2 per face, height [A] %.3f" % WIN_H)
w("  1 No. D1 door 900 wide - it lies WITHIN the west panel at Y 1000-2200, so the")
w("    UNION is deducted once, not both.  The overlap is a source-drawing matter")
w("    and is carried as a verification item.  [U]")
ff_ded = 8 * 1.200 * WIN_H
ff_net = gross_per_storey - ff_ded
w("  deduction = 8 x 1.200 x %.3f = %.2f m2" % (WIN_H, ff_ded))
w("  net first storey masonry = %.2f - %.2f = %.2f m2" % (gross_per_storey, ff_ded, ff_net))
w("  volume = %.2f x %.3f = %.2f m3  [D]" % (ff_net, WALL_T, ff_net * WALL_T))
w()
bm_total = (gf_net + ff_net) * WALL_T
w("TOTAL BRICK MASONRY = %.2f + %.2f = %.2f m3  (%.2f m2 face area)  [D]"
  % (gf_net * WALL_T, ff_net * WALL_T, bm_total, gf_net + ff_net))
rec("SP-01", "Brick masonry, ground storey, 190 thk in a 200 zone, CM 1:6, incl. scaffolding",
    "m3", gf_net * WALL_T, "[D]")
rec("SP-02", "Brick masonry, first storey, 190 thk in a 200 zone, CM 1:6, incl. scaffolding",
    "m3", ff_net * WALL_T, "[D]")
w()
w("MATERIAL CONSTANTS for procurement (modular brick 190 x 90 x 90 laid with a")
w("10 mm joint -> nominal module 200 x 100 x 100):")
bricks_per_m3 = 1.0 / (0.200 * 0.100 * 0.100)
w("  nominal module (brick + 10 mm joint) = 0.200 x 0.100 x 0.100 = 0.002 m3")
w("  bricks per m3 of finished masonry = 1 / 0.002 = %.0f No." % bricks_per_m3)
w("  bricks per m2 of a 190 wall       = %.0f x 0.190 = %.0f No."
  % (bricks_per_m3, bricks_per_m3 * 0.190))
w("  add 5 %% breakage and wastage  [A]  -> %.0f No./m3" % (bricks_per_m3 * 1.05))
n_bricks = bm_total * bricks_per_m3 * 1.05
w("  ORDER = %.2f m3 x %.0f = %.0f bricks, say %d thousand  [D]"
  % (bm_total, bricks_per_m3 * 1.05, n_bricks, int(math.ceil(n_bricks / 1000.0))))
rec("SP-03", "Modular burnt clay bricks class 10 to IS 1077, delivered",
    "No.", n_bricks, "[D]", "incl. 5 % breakage")
mortar_frac = 1.0 - (0.190 * 0.090 * 0.090) / (0.200 * 0.100 * 0.100)
mortar_vol = bm_total * mortar_frac * 1.25
w()
w("  mortar fraction = 1 - (0.190 x 0.090 x 0.090)/(0.200 x 0.100 x 0.100) = %.3f"
  % mortar_frac)
w("    i.e. brick 0.001539 m3 in a 0.002 m3 module.  This is the conventional")
w("    23 % figure for modular brickwork and is slightly conservative for a")
w("    one-brick wall, where the thickness carries no joint.  [A]")
w("  wet mortar = %.2f x %.3f = %.2f m3;  x 1.25 for dry volume = %.2f m3  [D]"
  % (bm_total, mortar_frac, bm_total * mortar_frac, mortar_vol))
w("  CM 1:6 -> cement = %.2f / 7 x 1440 = %.0f kg = %.1f bags of 50 kg  [D]"
  % (mortar_vol, mortar_vol / 7 * 1440, mortar_vol / 7 * 1440 / 50))
w("            sand   = %.2f x 6 / 7 = %.2f m3  [D]" % (mortar_vol, mortar_vol * 6 / 7))
rec("SP-04", "Cement for masonry mortar CM 1:6", "bag", mortar_vol / 7 * 1440 / 50, "[D]")
rec("SP-05", "Sand for masonry mortar, to IS 2116", "m3", mortar_vol * 6 / 7, "[D]")

sub("7.3  Sentry post lintels, plaster, flooring and finishes")
w("LINTELS.  With brick masonry the openings need lintels; the Rev F RC infill")
w("panels did not.  This is a CONSEQUENCE of SP-B1 and is a NEW work item.")
w("  ground storey: D1 900 clear, W1 1200 clear")
w("  first storey:  8 vision panels 1200 clear, 1 door 900 clear (see the overlap)")
w("Bearing 200 each end  [A].  RC lintel 200 wide x 150 deep  [A].")
w("*** LINTEL DESIGN DOES NOT EXIST IN THE PROJECT.  Section, reinforcement and")
w("    bearing are to be designed by the structural discipline.  The dimensions")
w("    above are for ESTIMATING ONLY.  [N] ***")
lintel_len = (0.900 + 1.200) + 2 * 0.200 * 2 + 8 * (1.200 + 2 * 0.200) + (0.900 + 2 * 0.200)
lintel_vol = lintel_len * 0.200 * 0.150
w("  total lintel length = %.2f m;  volume = %.2f m3 M30  [D]" % (lintel_len, lintel_vol))
rec("SP-06", "RC lintels over openings, 200 x 150 PROVISIONAL - design required",
    "m3", lintel_vol, "[N]")

w()
plaster_int = 2 * gross_per_storey - gf_ded - ff_ded + \
    2 * (4.000 * 5.000)          # both storeys' soffits
plaster_ext = 2 * gross_per_storey - gf_ded - ff_ded
w("PLASTER.  12 mm internal sand-faced CM 1:4 [A]; 15 mm external two-coat CM 1:4/1:6 [A].")
w("  IS 1661 governs application; thicknesses are NOT stated in the project.")
w("  internal wall faces  = 2 storeys x %.2f net masonry     = %.2f m2"
  % ((gf_net + ff_net) / 2, gf_net + ff_net))
w("  soffits (S1 first floor and roof, 4.000 x 5.000 each)  = %.2f m2" % (2 * 20.0))
w("  columns and beams, both faces, allowance                = %.2f m2"
  % (2 * 15.200 * 0.450 + 8 * 0.350 * 2.600))
p_int = (gf_net + ff_net) + 2 * 20.0 + (2 * 15.200 * 0.450 + 8 * 0.350 * 2.600)
p_ext = (gf_net + ff_net) + 2 * 15.200 * 0.450 + 8 * 0.350 * 2.600 + par_p * 0.300 * 2
w("  INTERNAL PLASTER TOTAL                                  = %.2f m2  [D]" % p_int)
w("  EXTERNAL PLASTER TOTAL (incl. parapet both faces)       = %.2f m2  [D]" % p_ext)
rec("SP-07", "Internal cement plaster 12 mm, sand faced, CM 1:4 [A]", "m2", p_int, "[D]")
rec("SP-08", "External cement plaster 15 mm, two coat [A]", "m2", p_ext, "[D]")
rec("SP-09", "Flooring, ground and first floor, 3.600 x 4.600 each",
    "m2", 2 * sen_fill_a, "[D]", "specification not in the project - [N]")
rec("SP-10", "Painting, internal and external, to IS 2395 (Part 1)",
    "m2", p_int + p_ext, "[D]", "specification not in the project - [N]")
rec("SP-11", "Door D1 900 x 2100 [A height], 2 No. (ground and first floor)",
    "No.", 2, "[C]")
rec("SP-12", "Window W1 1200 wide, ground storey, 1 No.", "No.", 1, "[C]",
    "height not stated - [N]")
rec("SP-13", "Armoured vision panels 1200 wide, 8 No., first storey - SPECIALIST",
    "No.", 8, "[C]", "specification not in the project - [N]")

# ===========================================================================
hdr("8.  BUILDING SERVICES — QUANTITIES CARRIED FROM THE DISCIPLINE PACKAGES")
w("Drainage DR1, HVAC HV1 and Schedule of Finishes FN1 are existing packages.")
w("Their schedules are the quantity source; nothing is re-derived here.")
w()
w("DRAINAGE (Drainage/Schedules) - principal items:")
for t in [
    "SU-01 clean sump 1500 x 1500 x 1500 at (-)7.600, with PU-01/PU-02 submersible "
    "pumps 1.5 L/s duty+standby and PU-03 hand pump                            [C]",
    "SU-02 stairwell sump 1.0 m3 at (-)2.000 with PU-04/PU-05 2 L/s             [C]",
    "TK-01 decon effluent tank 1000 L, bay 8, tanker emptying only              [C]",
    "TK-02 potable water tank 1000 L, bay 1                                     [C]",
    "ST-01 septic tank 1.50 x 0.75 x 1.00 liquid, IS 2470 (Pt 1) Table 1        [C]",
    "SK-01 foul soak pit 2.0 dia x 3.5 effective - 2.3 % SHORT, conflict C19    [U]",
    "SK-02 storm soakaway 2.0 dia x 3.5 effective, position not fixed           [A]",
    "SK-03 / SK-04 stairwell and headhouse soakaways - NOT SIZED anywhere       [N]",
    "PD-01 to PD-16 drains DN100 / rising mains DN50 - several lengths NOT",
    "  DETERMINABLE because no site plan exists (open item D3)                  [N]",
    "PD-04 decon effluent route across the protective boundary - NOT DEFINED    [U]",
    "PD-07 bay 8 (zone 3) has NO drainage destination                           [N]",
]:
    w("   " + t)
w()
w("HVAC / CBRN (HVAC/Schedules) - principal items:")
for t in [
    "AHU-1 / AHU-2 NBC filter trains, 300 m3/h each, true N+1                   [C]",
    "  (duty RULED AT 300 m3/h by RC1 - C21 CLOSED, master A.3 corrected)      [C]",
    "FAN-1 / FAN-2 supply fans with electric drive AND HAND CRANK               [C]",
    "  fan static pressure NOT DERIVABLE - five of eight loss components are",
    "  vendor data (HVAC calc H.9)                                              [N]",
    "CO2-1 soda-lime scrubber 20 kg/day, 40 kg store = 48 h closed mode         [C]",
    "O2-1 oxygen store, 2 x 50 L at 150 bar = 15 m3 = 80 h                      [C]",
    "DH-1 dehumidifier - DUTY NOT STATED anywhere                               [N]",
    "GEN-1 generator 15 kVA, bay 8 grey zone, 2600 m3/h combustion+cooling air  [C]",
    "SH-1 fresh-air shaft 600 x 600 west; SH-2 generator air shaft 600 x 600 east [C]",
    "Blast valves - 5 No. on sheet S-06; sizes and sleeve details NOT in Part B [N]",
]:
    w("   " + t)
w()
w("ELECTRICAL AND EMP:")
w("   *** NO ELECTRICAL DESIGN PACKAGE EXISTS IN THIS PROJECT. ***")
w("   The scope is CONFIRMED by the master (EMP Zone 2 enclosure in bay 3, master")
w("   A.3; generator 15 kVA; earthing to IEEE 142 / IS 3043 with a 5 ohm target,")
w("   master G; MIL-STD-188-125-1 80 dB over 10 kHz - 1 GHz; IEEE Std 299")
w("   verification survey), but NO circuit, cable, luminaire, DB or earth-electrode")
w("   schedule exists.  Every electrical quantity is therefore:")
w("       To be verified from final measurement.  [N]")
w("   The Works Management programme, resources, procurement, QA/QC and safety")
w("   documents still cover the electrical WORKS, because the works are confirmed")
w("   even though the quantities are not.")
for c, d in [("EL-01", "Conduits, boxes and concealed work, cast into RC - builder's work"),
             ("EL-02", "Cabling, distribution board and final circuits"),
             ("EL-03", "EMP Zone 2 shielded enclosure, bay 3 - SPECIALIST"),
             ("EL-04", "Earthing installation, 5 ohm target, IS 3043"),
             ("EL-05", "Lighting, small power and emergency lighting"),
             ("EL-06", "Generator connection, changeover and protection"),
             ("EL-07", "EMP protection to every service penetration (power PCI, "
                       "waveguide-below-cutoff, fibre)")]:
    rec(c, d, "item", None, "[N]", "no electrical design package exists")

# ===========================================================================
hdr("9.  CEMENT, AGGREGATE AND WATER — INDICATIVE PROCUREMENT VOLUMES")
w("Mix proportions are NOT stated in the project.  IS 456 Table 5 fixes the")
w("MINIMUM cement content at 340 kg/m3 and w/c <= 0.45 for the M35 (very severe")
w("exposure) concrete - that IS confirmed (master A.5).  A trial mix to IS 10262")
w("must fix the actual proportions.  The figures below use the code MINIMUM and")
w("are therefore a LOWER BOUND on cement.  [A]")
w()
CEM_M35 = 400.0
CEM_M30 = 360.0
CEM_M15 = 240.0
w("  M35 assumed 400 kg/m3 (>= 340 minimum, allowing for the crystalline admixture")
w("      and the 0.45 w/c cap)                                          [A]")
w("  M30 assumed 360 kg/m3                                              [A]")
w("  M15 assumed 240 kg/m3                                              [A]")
w()
V_M30 = sen_conc + COVER_A * 0.200 + lintel_vol
w("  M35 total = %.1f m3  ->  %.1f t cement" % (TOT_M35, TOT_M35 * CEM_M35 / 1000))
w("  M30 total = %.1f m3 (sentry %.1f + burster %.1f + lintels %.1f)  ->  %.1f t"
  % (V_M30, sen_conc, COVER_A * 0.200, lintel_vol, V_M30 * CEM_M30 / 1000))
w("  M15 total = %.1f m3  ->  %.1f t cement" % (TOT_M15, TOT_M15 * CEM_M15 / 1000))
cem_conc = (TOT_M35 * CEM_M35 + V_M30 * CEM_M30 + TOT_M15 * CEM_M15) / 1000
cem_mort = mortar_vol / 7 * 1440 / 1000
cem_plas = (p_int * 0.012 + p_ext * 0.015) * 1.25 / 5 * 1440 / 1000
w("  cement in concrete            = %.1f t" % cem_conc)
w("  cement in masonry mortar      = %.1f t" % cem_mort)
w("  cement in plaster (CM 1:4)    = %.1f t" % cem_plas)
w("  screeds, bedding, grout, 10 pct = %.1f t  [A]" % (0.10 * (cem_conc + cem_mort + cem_plas)))
cem_tot = 1.10 * (cem_conc + cem_mort + cem_plas)
w("  ORDER, cement, all works      = %.0f t = %.0f bags of 50 kg  [D]"
  % (cem_tot, cem_tot * 1000 / 50))
rec("M-01", "Cement, OPC 43 grade to IS 269, all works", "t", cem_tot, "[D]")
w()
V_ALL_CONC = TOT_M35 + V_M30 + TOT_M15
w("  aggregate (coarse + fine) at ~1.85 t/m3 of concrete  [A]")
w("            = %.1f m3 x 1.85 = %.0f t  [D]" % (V_ALL_CONC, V_ALL_CONC * 1.85))
rec("M-02", "Coarse and fine aggregate to IS 383, all concrete", "t",
    V_ALL_CONC * 1.85, "[D]")
w("  water for concrete at w/c 0.45 on %.0f t cement = %.0f m3, plus curing water"
  % (cem_conc, cem_conc * 0.45))
w("  Curing water for %.0f m2 of exposed concrete over 14 days is the larger demand"
  % tot_fw)
w("  and drives the site water supply.  Quantity [A] - depends on the curing method.")
rec("M-03", "Water for concrete, mortar and curing - site supply", "item", None, "[A]")

# ===========================================================================
hdr("10.  SUMMARY BILL")
w("%-8s %-58s %-6s %12s %-5s" % ("CODE", "DESCRIPTION", "UNIT", "QUANTITY", "CLASS"))
w("-" * 95)
for code, (desc, unit, qty, cls, note) in Q.items():
    qs = "TBV" if qty is None else ("%.2f" % qty if qty < 1000 else "%.0f" % qty)
    w("%-8s %-58s %-6s %12s %-5s" % (code, desc[:58], unit, qs, cls))
    if note:
        w("%-8s   note: %s" % ("", note))
w("-" * 95)
w("TBV = To be verified from final measurement.")

hdr("11.  ITEMS THAT CANNOT BE QUANTIFIED — DECLARED")
for t in [
    "Berm volume, site regrading, access road and hardstanding - NO SITE PLAN OR",
    "  GROUND MODEL EXISTS (Drainage DR1 open item D3).                         [N]",
    "Camouflage and concealment beyond the 300 topsoil / turf layer - no",
    "  concealment specification exists in the project.                         [N]",
    "All electrical quantities - no electrical design package exists.           [N]",
    "Blast door leaves, frames and anchorage - vendor items, master F.1 declares",
    "  them NOT AVAILABLE.                                                      [N]",
    "Blast valves x5, sleeves and trimming - sizes not in master Part B.        [N]",
    "Service-entry plate at W2, X ~ 11800 - plate size NOT AVAILABLE.           [N]",
    "Ventilation and CBRN duct penetrations - no penetration schedule exists.   [N]",
    "EMP Zone 2 shielded enclosure - specification is [N] in FN1 (code W-04).   [N]",
    "Armoured vision panels - specification not in the project.                 [N]",
    "Sentry post ground floor slab on grade - not designed.                     [N]",
    "Sentry post lintel design - does not exist; a CONSEQUENCE of SP-B1.        [N]",
    "Finishes: FN1 states every finish is a PERFORMANCE REQUIREMENT with the",
    "  product deliberately left open.  Areas can be measured; rates cannot.    [N]",
    "Sentry post window and vision-panel HEIGHTS - not stated on any drawing.   [N]",
    "Drainage pipe lengths PD-06, PD-11, PD-13, PD-14, PD-16 - not determinable.[N]",
]:
    w("  " + t)

hdr("12.  VERIFICATION ITEMS RAISED BY THIS DERIVATION")
for t in [
    "WM-V1  Sentry post ground-storey masonry height: the project's confirmed",
    "       2.600 m (master A.7.7) against the 2.750 m implied by +0.450 FFL and",
    "       the +3.200 beam soffit.  2.600 used.  150 mm difference OPEN.",
    "WM-V2  First-floor west wall: the D1 door (Y 1000-1900) lies inside the",
    "       armoured vision panel (Y 1000-2200) on the Rev F drawing.  The union",
    "       is deducted once.  Source-drawing clash, OPEN.",
    "WM-V3  Sentry post window W1 and vision-panel heights are not stated",
    "       anywhere.  1200 assumed for measurement.  OPEN.",
    "WM-V4  Brick wall thickness: 190 modular brickwork inside the 200 structural",
    "       zone preserves the confirmed external envelope.  Needs the designer's",
    "       confirmation, or a formal change to accept 230 conventional brickwork.",
    "WM-V5  Lintels over the sentry post openings are a NEW requirement created by",
    "       SP-B1.  CLOSED by SP-B2, 10 Sep 2026 (master A.4.8 / Part H.12):",
    "       lintel L1, 190 x 150, M30 / Fe500, 2-T10 bottom, 2-T8 top, T6 links",
    "       @ 150, bearing 200, ONE TYPE over all eleven openings.  SP-06 below",
    "       still measures the SUPERSEDED provisional 200 x 150 and is NOT",
    "       re-measured here - 0.485 m3 at 190 against 0.510 m3 at 200.",
    "WM-V6  Seismic weight of the sentry post changes when 200 RC infill (13.000",
    "       kN/m, master A.7.7) becomes brick masonry.  Brickwork at 20 kN/m3 over",
    "       0.190 x 2.600 gives 9.88 kN/m, LIGHTER than 13.000, so the existing",
    "       V_b = 73.18 kN is conservative - BUT this is a STRUCTURAL matter and",
    "       must be re-checked by that discipline.  NOT resolved here.",
    "WM-V7  Ballistic performance.  The Rev F panels are described as '200 RC",
    "       BALLISTIC INFILL'.  Brick masonry does not give the same ballistic",
    "       protection.  This is a consequence of the instructed change and is",
    "       recorded so that the decision is visible, not buried.",
    "WM-V8  Mat volume measured gross, with no deduction for the 1.5 x 1.5 sump",
    "       opening (1.35 m3).  SC1's convention, kept.  Conservative.",
    "WM-V9  Working space of 1.000 m and vertical unbenched faces are assumptions",
    "       of this package.  A slope-stability assessment of the soil zone above",
    "       rockhead is required before excavation.",
    "WM-V10 Bulking on rock excavation is not applied.  Loose volumes for haulage",
    "       and stockpiling will be 40-60 % greater.",
]:
    w("  " + t)

w()
w("END OF QUANTITY DERIVATION.  Works Management package revision WM1.")
w("Nothing in this derivation was invented.  Every input is named in section 0.")

TEXT = "\n".join(lines)

if __name__ == "__main__":
    print(TEXT)
