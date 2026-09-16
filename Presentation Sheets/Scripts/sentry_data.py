"""
sentry_data.py  --  every value that STR008 and STR009 draw or print.

THE SENTRY POST IS NOT IN `Structural CAD/Scripts/rebar_data.py`.  That file
says so in its own header -- "SENTRY POST: EXCLUDED.  No sentry bar appears in
this file." -- and it is not changed by this package.  This module is therefore
a SEPARATE bar-mark register, for the sentry post only, built to exactly the
same rule: a mark cannot appear on a view without a schedule entry, and
build_marks() asserts uniqueness.

SOURCES, in order of authority
    master/MASTER_PROJECT_STATE.md
        A.4.8   sentry post geometry (external 4000 x 5000, grids, members)
        A.7.7   sentry post loads
        A.7.8   sentry post seismic  (Ah 0.100, R 3.0)
        B.8.1   seismic member forces, portal method at Vb = 73.18 kN
        B.8.2   frame analysis assumption (joint rotation, slope deflection)
        B.8.3   slab S1 150 two-way
        B.8.4   beam B1 250 x 450 span 3650
        B.8.5   beam B2 250 x 450 span 4650
        B.8.6   column C1 350 x 350
        B.8.7   isolated footing F1 1500 x 1500 x 600
        F.4     THE DETAILING TABLE -- sizes, covers, d, reinforcement
        G       the clause register.  NO clause is cited on either sheet that
                is not in that register.
    Structural CAD/Scripts/rc_calc.py     Ld, bar areas -- the project's own
                                          functions, not re-derived here
    Structural CAD/Scripts/rebar_data.py  cut_length() -- the project's own
                                          PBR-1 rule, imported not copied

DECLARED DETAILING DECISIONS  (the master does not state these; they are
recorded here, printed on the sheets, and logged in master Part H as SR2)

  D1  TOP STEEL IS DETAILED CONTINUOUS OVER THE FULL SPAN.  F.4 schedules
      "4-T16 top at supports" / "3-T20 top at supports" and gives NO curtailment
      point.  Running the bars through is conservative and invents no cut-off.
  D2  BEAM BAR ANCHORAGE AT THE EXTERIOR JOINT.  Bars are taken to the far face
      of the confined core (350 - 40 cover - 10 hoop = 300 from the near face)
      and turned 90 deg with a leg of  Ld - 300,  Ld being the IS 456 Cl. 26.2.1
      tension development length at M30 / Fe500 computed by rc_calc.Ld_tension.
      The master states no anchorage detail for the beam bars.
  D3  COLUMN VERTICALS ARE SPLICE-FREE.  The 8 704 mm cut length is inside the
      12 000 mm stock bar (rebar_data P-1), so no lap is required and none is
      invented.  This also makes the bar its own starter, which is how B.8.7
      checks it ("Column starters T16 ... 526 straight + 8 phi bend 128 = 654").
  D4  SLAB BOTTOM STEEL.  B.8.3 reads Cl. D-1.4 as "50 % of midspan bottom steel
      extends to within 0.1 L of a discontinuous edge; remainder curtailed at
      0.25 L".  The 50 % that continues is detailed FULL LENGTH into the beams
      (a bar that runs through certainly extends to within 0.1 L); the remainder
      stops 0.25 L short of each support.

OPEN ITEMS RAISED BY THIS PACKAGE -- none of them is resolved here
  SR2-F1  B2 top steel at the ROOF joint.  B.8.6 evaluates the roof joint with
          B2 = 2-T20 (sum Mb 98.9, 1.4 x = 138.5 <= sum Mc 101 "marginal");
          F.4 schedules 3-T20 top at supports for B2 without distinguishing
          level.  With 3-T20 at the roof, 1.4 sum Mb = 195.7 > sum Mc = 101 and
          the IS 13920 Cl. 7.2.1 strong-column-weak-beam check FAILS at the roof
          joint.  THE TWO STATEMENTS CANNOT BOTH BE TRUE.  These sheets detail
          the FIRST-FLOOR frame only; the roof frame is cross-referenced and NOT
          detailed.  [UNRESOLVED]
  SR2-V1  Plinth beam PB links.  F.4 gives 250 x 400, cover 30, d 354,
          3-T12 top + 3-T12 bottom.  No link size or spacing exists anywhere.
          PB is scheduled on STR008 and is NOT detailed.  [NOT AVAILABLE]
  SR2-V2  Beam bar anchorage -- see D2.  Declared, not taken from the master.
  SR2-V3  Top-steel curtailment -- see D1.  Declared, not taken from the master.
  SR2-V4  Footing top level (-)1.400 is founding level (-)2.000 + the 600
          thickness.  The master states the founding level only.  [RECONSTRUCTED]
  SR2-V5  No blinding / levelling course under F1 is stated anywhere.  None is
          drawn.  [NOT AVAILABLE]
  SR2-V6  IS 13920 Cl. 8.1 also asks for confining reinforcement to continue
          into the footing.  F.4 states "500 from every joint face, top and
          bottom of every column, and through the joint" and stops there.  The
          master's rule is applied literally; no footing embedment is drawn.
          [UNRESOLVED]
  SR2-V7  Sentry post SITE POSITION is still [ASSUMED] -- master U4 / RC4-F3.
          Nothing on these two sheets depends on it; both are detail sheets in
          the post's own local coordinates.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "Structural CAD", "Scripts"))

import rc_calc as RC                                        # noqa: E402
from rebar_data import cut_length, HOOK                      # noqa: E402
import sheet_data as _SD                                     # noqa: E402

# ------------------------------------------------------------------- identity
# SR2A, by instruction: STR008 / STR009's identity block carries its OWN
# revision line, "STRUCTURAL - PHASE 2 + M1", independent of whatever
# sheet_data.IDENTITY does with its own -- that decoupling matters now that
# SR1A (master H.41) has DELETED sheet_data's revision line entirely for
# STR006 / STR007.  The four site-description lines are still shared, so a
# future edit to the project name or site cannot drift between the two sheet
# pairs; the assertion below is what enforces that sharing.
assert len(_SD.IDENTITY) == 4, (
    "sheet_data.IDENTITY no longer has exactly four site-description lines -- "
    "re-check this derivation before trusting it")
IDENTITY = list(_SD.IDENTITY) + ["STRUCTURAL - PHASE 2 + M1"]

FCK = 30.0                       # M30 -- master F.4 / B.8.4 (Mu,lim 0.133 x 30)
FY = 500.0                       # Fe500 / Fe500D
STOCK = 12000.0                  # rebar_data P-1


def nb(run_mm, spacing):
    """Bars in a run, both ends included.  Same rule as sc_proj.n_bars."""
    return int(run_mm // spacing) + 1


# =========================================================== GEOMETRY  (A.4.8)
EXT_X, EXT_Y = 4000.0, 5000.0            # external plan
INT_X, INT_Y = 3600.0, 4600.0            # internal
GRID_A, GRID_B = 175.0, 3825.0           # X of grids A and B   (3650 c/c)
GRID_1, GRID_2 = 175.0, 4825.0           # Y of grids 1 and 2   (4650 c/c)
SPAN_B1 = GRID_B - GRID_A                # 3650  B1 spans A-B, on grids 1 and 2
SPAN_B2 = GRID_2 - GRID_1                # 4650  B2 spans 1-2, on grids A and B

COL = 350.0                              # C1 350 x 350
BM_B, BM_D = 250.0, 450.0                # B1 / B2 250 x 450
SLAB_T = 150.0                           # S1
PB_B, PB_D = 250.0, 400.0                # plinth beam
FTG_L, FTG_T = 1500.0, 600.0             # F1 1500 x 1500 x 600

CLR_B1 = SPAN_B1 - COL                   # 3300   -- B.8.4 "3300/450 = 7.33"
CLR_B2 = SPAN_B2 - COL                   # 4300
CLR_SLAB_X = SPAN_B1 - BM_B              # 3400   -- B.8.3 "clear spans 3400"
CLR_SLAB_Y = SPAN_B2 - BM_B              # 4400   -- B.8.3 "and 4400"

# covers -- F.4
CV_BEAM, CV_COL, CV_SLAB, CV_FTG = 30.0, 40.0, 30.0, 50.0
D_BEAM = BM_D - CV_BEAM - 8 - 8          # 404    -- B.8.4
D_COL_DASH = CV_COL + 8 + 8              # d' 56  -- B.8.6
D_SLAB_X = SLAB_T - CV_SLAB - 4          # 116    -- B.8.3
D_SLAB_Y = SLAB_T - CV_SLAB - 8 - 4      # 108
D_FTG = FTG_T - CV_FTG - 8               # 542    -- B.8.7

# levels, metres, negative downwards -- A.4.8
L_FOUND = -2.000                         # in-situ basalt, B.8.7
L_FTG_TOP = L_FOUND + FTG_T / 1000.0     # (-)1.400   [RECONSTRUCTED, SR2-V4]
L_PLINTH = 0.450                         # top of PB -- B.8.6 uses 3650-450-450
L_PB_SOF = L_PLINTH - PB_D / 1000.0      # +0.050
L_FF = 3.650                             # first floor
L_FF_SOF = L_FF - BM_D / 1000.0          # +3.200  beam soffit
L_ROOF = 6.700                           # post roof
L_ROOF_SOF = L_ROOF - BM_D / 1000.0      # +6.250
H_GROUND = (L_FF - L_PLINTH) * 1000.0    # 3200  -- A.4.8 storey heights
H_FIRST = (L_ROOF - L_FF) * 1000.0       # 3050
CLR_COL_G = (L_FF_SOF - L_PLINTH) * 1000.0     # 2750  -- B.8.6
CLR_COL_1 = (L_ROOF_SOF - L_FF) * 1000.0       # 2600  -- A.7.7 infill 2.600 m

# IS 13920 detailing lengths -- B.8.4 / B.8.5 / B.8.6, all stated in the master
HINGE = 2.0 * D_BEAM                     # 810  "2d = 810 from each face"
S_HINGE, S_MID = 100.0, 150.0            # beam hoops
S_FIRST_HOOP = 50.0                      # "first hoop within 50 mm of the face"
LO_CONF = 500.0                          # column confining zone, Cl. 8.1
S_CONF = 85.0                            # confining hoop pitch
S_TIE = 150.0                            # general column ties

# D2 -- anchorage
CORE_IN = COL - CV_COL - 10.0            # 300, near face to far face of core
LD_T = {p: RC.Ld_tension(p, FCK) for p in (8, 10, 12, 16, 20)}
LD_C16 = 592.0                           # B.8.7 states 37 x 16 = 592 -- quoted


def anchor_leg(phi):
    """D2:  90 deg leg = Ld - 300, rounded UP to the next 25 mm."""
    raw = LD_T[phi] - CORE_IN
    return max(10.0 * phi, 25.0 * -(-raw // 25.0))


LEG16, LEG20, LEG12 = anchor_leg(16), anchor_leg(20), anchor_leg(12)

# =================================================== COLUMN CONFINING ZONES
# F.4 / B.8.6:  "500 mm from every joint face, top and bottom of every column,
# AND THROUGH THE JOINT (Cl. 8.2)".  Applied literally, joint by joint.
CONF_ZONES = [
    (L_FTG_TOP, L_FTG_TOP + 0.500, "BASE OF COLUMN, OFF THE FOOTING"),
    (L_PB_SOF - 0.500, L_PB_SOF, "BELOW THE PLINTH BEAM"),
    (L_PB_SOF, L_PLINTH, "THROUGH THE PLINTH-BEAM JOINT"),
    (L_PLINTH, L_PLINTH + 0.500, "ABOVE THE PLINTH BEAM"),
    (L_FF_SOF - 0.500, L_FF_SOF, "BELOW THE FIRST-FLOOR BEAM"),
    (L_FF_SOF, L_FF, "THROUGH THE FIRST-FLOOR JOINT"),
    (L_FF, L_FF + 0.500, "ABOVE THE FIRST FLOOR"),
    (L_ROOF_SOF - 0.500, L_ROOF_SOF, "BELOW THE ROOF BEAM"),
    (L_ROOF_SOF, L_ROOF, "THROUGH THE ROOF JOINT"),
]
# contiguous zones merge into one run of hoops -- a shared boundary carries ONE
# hoop, not two, so the runs are merged before the hoops are counted
CONF_RUNS = []
for _a, _b, _ in sorted(CONF_ZONES):
    if CONF_RUNS and abs(_a - CONF_RUNS[-1][1]) < 1e-9:
        CONF_RUNS[-1] = (CONF_RUNS[-1][0], _b)
    else:
        CONF_RUNS.append((_a, _b))
N_CONF = sum(nb((b - a) * 1000.0, S_CONF) for a, b in CONF_RUNS)

# the plain-tie runs are the gaps between the confining runs; the ties sit
# strictly INSIDE the gap, because both ends already carry a confining hoop
TIE_ZONES = [(CONF_RUNS[i][1], CONF_RUNS[i + 1][0])
             for i in range(len(CONF_RUNS) - 1)]
N_TIE = sum(max(-(-(b - a) * 1000.0 // S_TIE) - 1, 0) for a, b in TIE_ZONES)
N_TIE = int(N_TIE)

# column vertical bar, D3
COL_BAR_BOT = L_FOUND + (CV_FTG + 12 + 12) / 1000.0        # sits on the F1 mat
COL_BAR_TOP = L_ROOF - CV_SLAB / 1000.0
COL_BAR_RUN = (COL_BAR_TOP - COL_BAR_BOT) * 1000.0
COL_BAR_BEND = 8 * 16.0                                    # B.8.7, 8 phi = 128

# =========================================================== BAR-MARK REGISTER
MARKS = []


def _bar(mark, group, element, location, phi, shape, dims, count,
         spacing=None, remarks=""):
    cl = cut_length(shape, dims, phi)
    MARKS.append(dict(mark=mark, group=group, element=element, location=location,
                      phi=phi, shape=shape, dims=[round(d) for d in dims],
                      spacing=spacing, count=int(count), cut=cl,
                      kg=cl * int(count) / 1000.0 * RC.bar_kg_per_m(phi),
                      remarks=remarks))


def _link(mark, group, element, location, phi, a, b, count, spacing=None,
          remarks=""):
    _bar(mark, group, element, location, phi, "51", (a, b), count, spacing,
         remarks)


# ------------------------------------------------- B1, first floor, 2 No.
G = "BEAM B1"
N_B1, N_B2 = 2, 2                       # per level; FIRST FLOOR ONLY -- SR2-F1
B1_RUN = CLR_B1 + 2 * CORE_IN           # 3900
B2_RUN = CLR_B2 + 2 * CORE_IN           # 4900
LINK_A, LINK_B = BM_D - 2 * CV_BEAM, BM_B - 2 * CV_BEAM     # 390 x 190

N_HINGE = nb(HINGE - S_FIRST_HOOP, S_HINGE)                 # hoops one end
_last = S_FIRST_HOOP + (N_HINGE - 1) * S_HINGE              # 750 from the face
N_MID_B1 = int(max(-(-(CLR_B1 - 2 * _last) // S_MID) - 1, 0))
N_MID_B2 = int(max(-(-(CLR_B2 - 2 * _last) // S_MID) - 1, 0))

_bar("SB01", G, "B1  250 x 450", "TOP, 4 BARS, FULL LENGTH (D1)", 16, "21",
     (LEG16, B1_RUN, LEG16), 4 * N_B1, None,
     "90 deg legs into the column core, D2")
_bar("SB02", G, "B1  250 x 450", "BOTTOM, 2 BARS CONTINUOUS", 16, "21",
     (LEG16, B1_RUN, LEG16), 2 * N_B1, None,
     "IS 13920 Cl. 6.2.3 - 50 % of the top steel at the joint face")
_link("SB03", G, "B1  250 x 450", "HOOPS, HINGE ZONE 810 = 2d EACH END", 8,
      LINK_A, LINK_B, 2 * N_HINGE * N_B1, 100,
      "IS 13920 Cl. 6.3.5.1; first hoop 50 from the column face")
_link("SB04", G, "B1  250 x 450", "HOOPS, CENTRAL ZONE", 8,
      LINK_A, LINK_B, N_MID_B1 * N_B1, 150, "IS 13920 Cl. 6.3.5.2, sv <= d/2")

# ------------------------------------------------- B2, first floor, 2 No.
G = "BEAM B2"
_bar("SB05", G, "B2  250 x 450", "TOP, 3 BARS, FULL LENGTH (D1)", 20, "21",
     (LEG20, B2_RUN, LEG20), 3 * N_B2, None,
     "3-T20 not 5-T16: five T16 need 256 in a 250 wide beam (F.4)")
_bar("SB06", G, "B2  250 x 450", "BOTTOM, 2 BARS CONTINUOUS", 20, "21",
     (LEG20, B2_RUN, LEG20), 2 * N_B2, None,
     "IS 13920 Cl. 6.2.3 - 0.5 x 942 = 471 governs over the 297 required")
_link("SB07", G, "B2  250 x 450", "HOOPS, HINGE ZONE 810 = 2d EACH END", 8,
      LINK_A, LINK_B, 2 * N_HINGE * N_B2, 100,
      "Cl. 6.3.4 taken as TRIGGERED at 49.7 %: tau_c = 0")
_link("SB08", G, "B2  250 x 450", "HOOPS, CENTRAL ZONE", 8,
      LINK_A, LINK_B, N_MID_B2 * N_B2, 150, "IS 13920 Cl. 6.3.5.2, sv <= d/2")

# ------------------------------------------------- C1, 4 No., full height
G = "COLUMN C1"
N_COL = 4
CORE = COL - 2 * CV_COL                                     # 270 -- B.8.6 h
_bar("SC01", G, "C1  350 x 350", "VERTICALS, 8 PER COLUMN, NO SPLICE (D3)", 16,
     "11", (COL_BAR_BEND, COL_BAR_RUN), 8 * N_COL, None,
     "one stock bar, footing to roof; 8 phi bend on the F1 mat, B.8.7")
_link("SC02", G, "C1  350 x 350", "CONFINING HOOPS, 9 ZONES (IS 13920 Cl. 8.1)",
      10, CORE, CORE, N_CONF * N_COL, 85,
      "lo 500; Ash 235.5 provided vs 168.5 required, B.8.6")
_bar("SC03", G, "C1  350 x 350", "CROSS-TIES, ONE EACH WAY WITH EVERY HOOP", 10,
     "99", (CORE, HOOK * 10, HOOK * 10), 2 * N_CONF * N_COL, 85,
     "the third leg that makes Ash = 3 x 78.5 = 235.5")
_link("SC04", G, "C1  350 x 350", "GENERAL TIES, OUTSIDE THE CONFINING ZONES", 8,
      CORE, CORE, N_TIE * N_COL, 150,
      "IS 456 Cl. 26.5.3.2 and IS 13920 Cl. 7.4 (<= 175) both satisfied")

# ------------------------------------------------- F1, 4 No.
G = "FOOTING F1"
N_FTG = 4
FTG_BAR = FTG_L - 2 * CV_FTG                                # 1400
_bar("SF01", G, "F1  1500 x 1500 x 600", "BOTTOM, BOTH WAYS - LAYER 1 (X)", 12,
     "00", (FTG_BAR,), nb(FTG_BAR, 150) * N_FTG, 150,
     "Cl. 26.5.2.1 min 0.12 % x 600 = 720 GOVERNS over the 136 required")
_bar("SF02", G, "F1  1500 x 1500 x 600", "BOTTOM, BOTH WAYS - LAYER 2 (Y)", 12,
     "00", (FTG_BAR,), nb(FTG_BAR, 150) * N_FTG, 150, "as SF01, laid over it")

# ------------------------------------------------- S1, 2 panels (both floors)
G = "SLAB S1"
N_SLAB = 2                                # A.4.8: "150 thk ... both floors"
SL_X0 = GRID_A - BM_B / 2 + CV_SLAB       # 80   -- 30 cover off the beam face
SL_X1 = GRID_B + BM_B / 2 - CV_SLAB       # 3920
SL_Y0 = GRID_1 - BM_B / 2 + CV_SLAB
SL_Y1 = GRID_2 + BM_B / 2 - CV_SLAB
LX_EFF, LY_EFF = 3516.0, 4508.0           # B.8.3 Cl. 22.2(a)
CURT_X = round(LX_EFF - 2 * 0.25 * LX_EFF, -1)      # 1760
CURT_Y = round(LY_EFF - 2 * 0.25 * LY_EFF, -1)      # 2250
EDGE_BAND = 400.0                         # 0.1 L -- B.8.3 Cl. D-1.6
TORSION = 700.0                           # lx/5 -- B.8.3 Cl. D-1.8

_bar("SS01", G, "S1  150 THK", "BOTTOM, SHORT SPAN (X), FULL LENGTH (D4)", 8,
     "00", (SL_X1 - SL_X0,), nb(CLR_SLAB_Y, 300) * N_SLAB, 300,
     "the 50 % that continues; with SS02 gives T8 @ 150 = 335 mm2/m")
_bar("SS02", G, "S1  150 THK", "BOTTOM, SHORT SPAN (X), CURTAILED AT 0.25 L", 8,
     "00", (CURT_X,), nb(CLR_SLAB_Y, 300) * N_SLAB, 300, "IS 456 Cl. D-1.4")
_bar("SS03", G, "S1  150 THK", "BOTTOM, LONG SPAN (Y), FULL LENGTH (D4)", 8,
     "00", (SL_Y1 - SL_Y0,), nb(CLR_SLAB_X, 300) * N_SLAB, 300,
     "laid over SS01, so dy = 108")
_bar("SS04", G, "S1  150 THK", "BOTTOM, LONG SPAN (Y), CURTAILED AT 0.25 L", 8,
     "00", (CURT_Y,), nb(CLR_SLAB_X, 300) * N_SLAB, 300, "IS 456 Cl. D-1.4")
_bar("SS05", G, "S1  150 THK", "TOP, 400 EDGE BAND, ALL FOUR EDGES", 8, "11",
     (100, BM_B - CV_SLAB + EDGE_BAND),
     (2 * nb(CLR_SLAB_X, 300) + 2 * nb(CLR_SLAB_Y, 300)) * N_SLAB, 300,
     "IS 456 Cl. D-1.6 - 50 % of the midspan steel, 0.1 L into the span")
_bar("SS06", G, "S1  150 THK", "CORNER TORSION MATS, 4 LAYERS, 700 x 700", 8,
     "00", (TORSION + BM_B / 2 - CV_SLAB,),
     4 * 4 * nb(TORSION, 200) * N_SLAB, 200,
     "IS 456 Cl. D-1.8 - A HOLD POINT.  Omit them and Table 26 is invalid")

_seen = set()
for _m in MARKS:
    assert _m["mark"] not in _seen, "duplicate mark " + _m["mark"]
    _seen.add(_m["mark"])


def rows(*groups):
    """Bar-mark schedule rows for the named groups."""
    out = []
    for m in MARKS:
        if m["group"] not in groups:
            continue
        out.append([m["mark"], f"T{m['phi']}",
                    str(int(m["spacing"])) if m["spacing"] else "-",
                    m["location"], f"{m['cut']:.0f}", str(m["count"])])
    return out


def total_kg(*groups):
    return sum(m["kg"] for m in MARKS if m["group"] in groups)


# ============================================================ TITLE-BLOCK NOTES
_N_COMMON = [
    "ALL DIMENSIONS ARE IN MM. ALL LEVELS ARE IN METRES RELATIVE TO FINISHED "
    "SITE GRADE 0.000, NEGATIVE DOWNWARDS.",
    "WRITTEN DIM TO BE FOLLOWED ONLY. DRG NOT TO BE SCALED.",
    "THIS DRG IS TO BE READ IN CONJUNCTION WITH ALL RELEVANT ARCH AND STR DRGS.",
    "SENTRY POST CONCRETE M30. REINFORCEMENT Fe500D TO IS 1786:2008. COVER 40 "
    "TO COLUMNS, 30 TO BEAMS AND SLABS, 50 TO FOOTINGS (IS 456 Cl. 26.4.2 / "
    "TABLE 16).",
]
_N_13920 = (
    "THE SENTRY POST FRAME IS THE IS 13920:2016 ELEMENT OF THIS PROJECT. IT IS "
    "A SPECIAL MOMENT-RESISTING FRAME, R = 3.0, Ah = 0.100, DESIGNED ON THE "
    "STAAD BASE SHEAR Vb = 73.18 kN.")
_N_NOTBLAST = (
    "THE SENTRY POST IS NOT DESIGNED FOR THE BLAST, AND THAT IS A RECORDED "
    "DECISION (MASTER B.8). REFLECTED FORCE ON THE 4.0 x 6.7 m FACE IS 36 600 "
    "kN; HARDENING WOULD NEED ABOUT 700 mm OF RC ON ALL FOUR ABOVE-GROUND "
    "FACES.")
_N_CHECK = "CONTRACTOR TO CHECK AND VERIFY THE DRG BEFORE EXECUTION."

NOTES_08 = _N_COMMON + [
    _N_13920,
    "DUCTILE DETAILING GOVERNS EVERY BAR ON THIS SHEET: Cl. 6.2.3 SETS THE "
    "BOTTOM STEEL, Cl. 6.3.3 / 6.3.4 SET THE HOOPS (tau_c TAKEN AS ZERO IN THE "
    "HINGE REGIONS), Cl. 6.3.5.1 SETS 100 c/c OVER 2d = 810, AND Cl. 8.1 / 8.2 "
    "SET THE COLUMN CONFINING STEEL.",
    "THE TAGS (D1), (D2) AND (D3) ON THIS SHEET ARE DECLARED DETAILING "
    "DECISIONS, AND EVERY 'SR2-' REFERENCE IS AN OPEN ITEM. BOTH ARE RECORDED "
    "IN MASTER PART H.40.4 AND H.40.5. D1: TOP STEEL IS DETAILED CONTINUOUS "
    "OVER THE FULL SPAN BECAUSE THE MASTER GIVES 'TOP AT SUPPORTS' AND NO "
    "CURTAILMENT POINT.",
    "THIS SHEET DETAILS THE FIRST-FLOOR FRAME ONLY. THE ROOF FRAME IS NOT "
    "DETAILED - SEE FINDING SR2-F1 IN MASTER PART H.40.5.",
    _N_NOTBLAST,
    _N_CHECK,
]

NOTES_09 = _N_COMMON + [
    "FOOTINGS ARE FOUNDED ON IN-SITU BASALT AT (-)2.000, NEVER ON BACKFILL. "
    "THAT IS THE WHOLE REASON THE SENTRY POST IS SITED AT LEAST 10 m CLEAR OF "
    "THE SHELTER EXCAVATION.",
    "THE 600 FOOTING DEPTH IS GOVERNED BY THE ANCHORAGE OF THE COLUMN STARTERS, "
    "NOT BY BENDING OR SHEAR. IT MUST NOT BE 'OPTIMISED' TO 350.",
    "SLAB S1 IS A TWO-WAY SLAB ON IS 456 TABLE 26 (ANNEX D-1.1, CASE 9). TABLE "
    "26 IS VALID ONLY BECAUSE THE CORNER TORSION MATS ARE PROVIDED. THE MATS "
    "ARE A HOLD POINT FOR REINFORCEMENT INSPECTION.",
    _N_13920,
    "THE TAGS (D3) AND (D4) IN THE BAR MARK SCHEDULE ARE DECLARED DETAILING "
    "DECISIONS, RECORDED IN MASTER PART H.40.4. THE OPEN ITEMS THAT AFFECT "
    "THIS SHEET - SR2-V4 THE FOOTING TOP LEVEL, SR2-V5 NO BLINDING UNDER F1, "
    "SR2-V6 CONFINING STEEL INTO THE FOOTING - ARE IN MASTER PART H.40.5.",
    _N_CHECK,
]

# =============================================================================
# SR2A -- DECISIONS_08 / DECISIONS_09 / BASIS_08 / BASIS_09 ARE NO LONGER
# PRINTED.  The two note panels they fed were deleted from both sheets by
# instruction.  The lists are kept here, unaltered, so the record stays with the
# data (rule M.11), but THE AUTHORITY IS NOW master H.40.4 (the four declared
# detailing decisions) and master H.40.5 (findings SR2-F1, SR2-F2 and open items
# SR2-V1 to SR2-V6).  A reader of the sheets alone will not see them, so the
# open items must be carried into the next revision by the master, not by the
# drawing.
# =============================================================================

# ================================================================= SHEET 08
BEAM_SCHEDULE = [
    ["B1  GRIDS 1 AND 2", "250 x 450", "3650", "3300", "30", "404",
     "4-T16", "2-T16", "T8 2L @ 100 / 150"],
    ["B2  GRIDS A AND B", "250 x 450", "4650", "4300", "30", "404",
     "3-T20", "2-T20", "T8 2L @ 100 / 150"],
    "IS 13920 Cl. 6.1:  b 250 >= 200 OK  |  b/D 0.556 >= 0.3 OK  |  Ln/D 7.33 >= 4 OK",
    "SCHEDULED HERE, DETAILED ELSEWHERE, NOT DRAWN ON THIS SHEET",
    ["PB  PLINTH BEAM", "250 x 400", "3650 / 4650", "-", "30", "354",
     "3-T12", "3-T12", "NOT STATED - SR2-V1"],
]

COLUMN_SCHEDULE = [
    ["C1", "350 x 350", "(-)1.400 TO +6.700", "40", "8-T16  (1608)", "1.31 %",
     "T10 + 1 CROSS-TIE E/W @ 85", "T8 @ 150"],
    "4 No. COLUMNS.  SHORT COLUMN: lex/D = 9.43 < 12 (IS 456 Cl. 25.1.2)",
    "CONFINING STEEL OVER lo = 500 FROM EVERY JOINT FACE AND THROUGH THE JOINT",
    "Ash PROVIDED 3 x 78.5 = 235.5 mm2  vs  168.5 REQUIRED (IS 13920 Cl. 8.1)",
]

IS13920_CHECK = [
    ["Cl. 6.1.1 / 6.1.2 / 6.1.3", "b >= 200,  b/D >= 0.3,  Ln/D >= 4",
     "250,  0.556,  7.33", "PASS"],
    ["Cl. 6.2.1(b) / 6.2.2", "rho,min 266 mm2  ;  rho,max 2525 mm2",
     "402 (2-T16)  ;  942 (3-T20) MAX", "PASS"],
    ["Cl. 6.2.3  positive at joint", ">= 50 % of the negative steel",
     "402 = 50 % of 804", "PASS"],
    ["Cl. 6.2.4  through the joint", ">= 25 % of the max = 201 mm2",
     "402 CONTINUOUS", "PASS"],
    ["Cl. 6.3.3  capacity shear", "Vu  B1 120.4  /  B2 144.7 kN",
     "T8 2-LEG @ 100", "PASS"],
    ["Cl. 6.3.4  tau_c = 0", "EQ share  B1 60 %  /  B2 49.7 %",
     "TAKEN AS TRIGGERED", "PASS"],
    ["Cl. 6.3.5.1 / 6.3.5.2", "hinge min(d/4=101, 8phi=128) ; else d/2=202",
     "100 OVER 2d = 810 ;  150", "PASS"],
    ["Cl. 7.2.1  SCWB, FIRST FLOOR", "1.4 sum Mb  171.6 (X)  /  195.7 (Z)",
     "sum Mc 213.9", "PASS"],
    ["Cl. 7.2.1  SCWB, ROOF", "1.4 sum Mb 138.5 AT 2-T20", "sum Mc 101",
     "MARGINAL - SR2-F1"],
    ["Cl. 7.4  ties, full length", "<= 0.5 x least dimension = 175", "150", "PASS"],
    ["Cl. 8.1  lo and spacing", "lo max(350, h/6=458, 450) ; 75 <= s <= 87.5",
     "500 ;  85", "PASS"],
    ["Cl. 8.1  Ash", "168.5 mm2  (minimum 68.9)", "235.5  (3 LEGS T10)", "PASS"],
    ["Cl. 8.2  through the joint", "CONFINING STEEL CONTINUED", "PROVIDED", "PASS"],
    ["Cl. 10.4  boundary elements", "CHECKED FOR THE BOX ONLY", "NOT TRIGGERED",
     "N/A HERE"],
]

DECISIONS_08 = [
    "D1  TOP STEEL IS DETAILED CONTINUOUS OVER THE FULL SPAN.  Master F.4 schedules '4-T16 top at supports' and",
    "    '3-T20 top at supports' and gives NO curtailment point anywhere.  Running the bars through is conservative",
    "    under moment reversal and invents no cut-off.   [SR2-V3]",
    "D2  ANCHORAGE AT THE EXTERIOR JOINT.  Bars are taken to the far face of the confined core - 350 - 40 cover -",
    "    10 hoop = 300 from the near face - and turned 90 deg with a leg of Ld - 300.  Ld is the IS 456 Cl. 26.2.1",
    "    tension value at M30 / Fe500:  T16 725,  T20 906,  so the legs are 425 and 625.  The master states no",
    "    anchorage detail for the beam bars.   [SR2-V2]",
    "D3  THE COLUMN VERTICALS ARE SPLICE-FREE.  The 8 724 mm cut length is inside the 12 000 mm stock bar, so no",
    "    lap is required and none is invented.  The bar is therefore its own starter, which is exactly how master",
    "    B.8.7 checks it:  526 straight in the footing + a 128 (8 phi) bend = 654 > Ld,comp 592.",
    "SR2-F1  *** OPEN, NOT RESOLVED ***  B2 TOP STEEL AT THE ROOF JOINT.  Master B.8.6 evaluates the roof joint",
    "    with B2 = 2-T20 (sum Mb 98.9, 1.4 x = 138.5 <= sum Mc 101, 'marginal').  Master F.4 schedules 3-T20 top",
    "    at supports for B2 and does NOT distinguish level.  With 3-T20 at the roof, 1.4 sum Mb = 195.7 > sum Mc",
    "    = 101 and IS 13920 Cl. 7.2.1 FAILS at that joint.  Both statements cannot be true.  THIS SHEET DETAILS",
    "    THE FIRST-FLOOR FRAME, where B.8.5 and F.4 agree on 3-T20.  The roof frame is cross-referenced only.",
    "SR2-V1  The plinth beam PB is scheduled (3-T12 top + 3-T12 bottom) but NO link size or spacing exists in the",
    "    master.  PB IS NOT DETAILED HERE.   SR2-V6  IS 13920 Cl. 8.1 also asks for confining steel to continue",
    "    INTO the footing; master F.4 stops at 'top and bottom of every column and through the joint'.  Applied",
    "    as written - no footing embedment is drawn.  Refer to the design authority before the footings are cast.",
]

BASIS_08 = [
    "SEISMIC BASIS   IS 1893 (Pt 1):2016,  Z 0.16 ZONE III,  I 1.5,  R 3.0,  Sa/g 2.5   ->   Ah = 0.100",
    "   R = 3.0 because the infill panels are NOT positively separated from the frame.  R = 5.0 would require that.",
    "   Ta 0.297 s (Cl. 7.6.2) - all three period estimates land inside 0.10 to 0.40 s, so Sa/g = 2.5 regardless.",
    "   ALL MEMBER DESIGN USES THE STAAD BASE SHEAR Vb = 73.18 kN, NOT THE HAND-CALCULATED 59.3 kN.",
    "",
    "PORTAL-METHOD MEMBER FORCES  (master B.8.1)",
    "   Q roof 59.51 kN ; Q floor 13.67 kN ; column shear 18.30 (ground) / 14.88 (first) kN",
    "   Column moment 29.27 / 22.69 kNm ; beam moment 51.96 at the first-floor joint, 22.69 at the roof",
    "   Axial from overturning READ FROM THE STAAD REACTIONS:  EQ+X 36.127 kN governs over EQ+Z 27.891 kN",
    "",
    "THE JOINT ROTATES - STATED, NOT HIDDEN  (master B.8.2).  Slope-deflection on a single-bay portal:",
    "   I,beam 1.8984e9, I,col 1.2505e9, Kc 3.203e6 E  ->  support moments x0.755 (B1) and x0.797 (B2).",
    "   Beams are NOT taken as fully fixed.",
    "",
    "BEAM B1  250 x 450, SPAN 3650, CLEAR 3300     d 404 ;  Mu,lim = 0.133 x 30 x 250 x 404^2 = 162.8 kNm",
    "   1.5(DL + EL) = 1.5(17.01 + 51.96) = 103.5 kNm  *** GOVERNS ***  over 86.2 and 93.2 ;  Ast,req 661",
    "   PROVIDED 4-T16 TOP (804) :  Mu 122.6 kNm,  UTILISATION 84 %,  x/d 0.321",
    "   BOTTOM  reversal -52.4 needs 313 ; Cl. 6.2.3 needs 0.5 x 804 = 402 *** GOVERNS ***  ->  2-T16, Mu 66.0",
    "   SHEAR  Vu = 1.2 x 80.1/2 + 1.4(122.6 + 66.0)/3.650 = 48.1 + 72.3 = 120.4 kN ; tau_v 1.192 < 3.50",
    "     EQ share 60 % >= 50 %, no axial  ->  Cl. 6.3.4:  tau_c TAKEN AS ZERO.  Asv/sv 0.685 -> T8 2L at 147",
    "   DEFLECTION  l/d = 9.0 << 20",
    "",
    "BEAM B2  250 x 450, SPAN 4650, CLEAR 4300",
    "   1.5(DL + EL) = 1.5(31.25 + 51.96) = 124.8 kNm  *** GOVERNS *** ;  Ast,req 822",
    "   PROVIDED 3-T20 TOP (942) :  Mu 139.8 kNm,  UTILISATION 89 %,  x/d 0.376",
    "     *** 3-T20 NOT 5-T16: five T16 need 256 mm in a 250 mm wide beam.  Skip that check and it is a site RFI.",
    "   BOTTOM  Cl. 6.2.3 -> 0.5 x 942 = 471 *** GOVERNS *** over the 297 midspan requirement  ->  2-T20, Mu 98.9",
    "   SHEAR  Vu = 72.8 + 71.9 = 144.7 kN ; tau_v 1.433 < 3.50.  EQ share 49.7 %, a hair under the trigger.",
    "     *** TAKEN AS TRIGGERED (tau_c = 0): a design must not turn on the third decimal place of a ratio. ***",
    "",
    "COLUMN C1  350 x 350   SHORT COLUMN lex 3300, lex/D 9.43 < 12 ;  e,min 20 -> M,min 5.5 kNm, far below applied",
    "   AXIAL per column  1.5(DL+LL) 251.3 ;  1.5(DL+EL) 276.8 MAX ;  1.5(DL-EL) 168.4 MIN",
    "   8-T16 = 1608 mm2, p = 1.31 % (min 0.8 % = 980, max 6 %), bars on all four faces, d'/D 0.16",
    "   UNIAXIAL CAPACITY computed from the Cl. 38.1 stress block and the Fe500 curve, NOT read off a chart:",
    "     Mu1 = 105.8 / 111.7 / 112.9 kNm.   BIAXIAL Cl. 39.6:  Puz 2235 ; Pu/Puz 0.124 < 0.2 -> alpha,n 1.0 ;",
    "     25.6/112.9 + 66.8/112.9 = 0.819 <= 1.0  OK.   DRIFT limit 12.8 / 12.2 mm ; calculated under 3 mm.",
]

# ================================================================= SHEET 09
FOOTING_SCHEDULE = [
    ["F1", "4", "1500 x 1500 x 600", "(-)2.000", "(-)1.400", "50", "542",
     "T12 @ 150 B/W BOTTOM  (754)"],
    "FOUNDED ON IN-SITU BASALT.  PRESUMPTIVE SBC 3240 kPa, IS 1904 TABLE 1 [ASSUMED]",
    "SERVICE q,max 157.6 kPa = 4.9 % OF SBC   |   e = 0.123 < L/6 = 0.250, NO TENSION",
    "THE 600 DEPTH IS SET BY STARTER ANCHORAGE, NOT BY BENDING OR SHEAR",
]

SLAB_SCHEDULE = [
    ["S1  BOTTOM, BOTH WAYS", "150", "30", "116 / 108", "T8 @ 150  (335 mm2/m)",
     "IS 456 Cl. 26.5.2.1 min 180"],
    ["S1  TOP, DISCONTINUOUS EDGES", "150", "30", "116", "T8 @ 300, 400 INTO THE SPAN",
     "Cl. D-1.6, all four edges"],
    ["S1  CORNER TORSION MATS", "150", "30", "-", "T8 @ 200, 4 LAYERS, 700 x 700",
     "Cl. D-1.8, all four corners"],
    "S1 OCCURS TWICE - FIRST FLOOR AND ROOF (MASTER A.4.8).  THE FIRST FLOOR GOVERNS.",
]

ANNEXD_CHECK = [
    ["D-1.1 / Table 26", "CASE 9, FOUR EDGES DISCONTINUOUS BUT RESTRAINED",
     "alpha x 0.0777, alpha y 0.056"],
    ["Cl. 24.4", "ly/lx = 4508/3516 = 1.282 < 2  ->  TWO-WAY", "CONFIRMED"],
    ["D-1.2 / D-1.3", "MIDDLE STRIP 3/4, EDGE STRIPS 1/8 EACH SIDE",
     "TABLE 26 MOMENTS APPLY TO THE MIDDLE STRIPS ONLY"],
    ["D-1.4", "50 % TO WITHIN 0.1 L OF A DISCONTINUOUS EDGE",
     "SS01 / SS03 FULL LENGTH, SS02 / SS04 CUT AT 0.25 L"],
    ["D-1.6", "TOP STEEL = 50 % OF MIDSPAN, 0.1 L = 400 INTO THE SPAN",
     "SS05  T8 @ 300, ALL FOUR EDGES"],
    ["D-1.7", "EDGE STRIPS - MINIMUM REINFORCEMENT ONLY", "T8 @ 150 THROUGHOUT COVERS IT"],
    ["D-1.8", "CORNER TORSION = 3/4 OF MIDSPAN, 4 LAYERS OVER lx/5 = 700",
     "SS06  T8 @ 200 - A HOLD POINT"],
    ["Cl. 26.5.2.2", "MAX BAR DIA D/8 = 18.75", "T8  OK"],
    ["Cl. 26.3.3(b)", "MAX SPACING 3d OR 300", "150 BOTTOM, 300 TOP  OK"],
]

DECISIONS_09 = [
    "D4  SLAB BOTTOM STEEL.  Master B.8.3 reads IS 456 Cl. D-1.4 as '50 % of midspan bottom steel extends to within",
    "    0.1 L of a discontinuous edge; remainder curtailed at 0.25 L'.  The 50 % that continues (SS01 / SS03) is",
    "    detailed FULL LENGTH into the beams - a bar that runs through certainly extends to within 0.1 L - and the",
    "    remainder (SS02 / SS04) stops 0.25 L short of each support.  Together they give T8 @ 150 both ways.",
    "D3  THE COLUMN VERTICALS SC01 ARE CONTINUOUS FROM THE FOOTING TO THE ROOF, ONE 8 724 mm STOCK BAR, NO SPLICE.",
    "    They are detailed on SHEET 08; only their anchorage inside F1 is drawn here.  Master B.8.7:  526 straight",
    "    + a 128 (8 phi) bend = 654 > Ld,comp 592 for T16 in M30.",
    "SR2-V4  The footing TOP level (-)1.400 is the founding level (-)2.000 plus the 600 thickness.  The master",
    "    states the founding level only.  [RECONSTRUCTED]  Confirm against the setting-out before F1 is cast.",
    "SR2-V5  NO blinding or levelling course under F1 is stated anywhere in the master, and none is drawn.",
    "    [NOT AVAILABLE]",
    "SR2-V6  IS 13920 Cl. 8.1 also asks for confining reinforcement to continue INTO the footing.  Master F.4",
    "    states confining steel '500 from every joint face, top and bottom of every column, and through the joint'",
    "    and stops there.  The rule is applied as written and NO footing embedment is drawn.  [UNRESOLVED - refer",
    "    to the design authority before the footings are cast.]",
]

BASIS_09 = [
    "ISOLATED FOOTING F1  1500 x 1500 x 600 ON IN-SITU BASALT AT (-)2.000      d = 600 - 50 - 8 = 542",
    "   *** FOUNDED ON IN-SITU ROCK, NEVER ON BACKFILL.  This is the whole reason the sentry post is sited at",
    "   least 10 m clear of the shelter excavation. ***",
    "   SERVICE  P = 167.5 (column) + 36.1 (EQ axial) + 33.75 (footing self) = 237.4 kN ;  M at the base 29.3 kNm",
    "     e = 29.3/237.4 = 0.123 m < L/6 = 0.250   ->   NO TENSION UNDER THE BASE",
    "     q,max = P/A (1 + 6e/L) = 105.5 x 1.494 = 157.6 kPa  vs  SBC 3240 kPa (IS 1904 Table 1) = 4.9 %",
    "   ULS  1.5(DL + EL):  Pu 276.8 kN ; Mu 43.9 kNm ; eu 0.128 ;  qu,max = 123.0 x 1.544 = 190.0 kPa",
    "   FLEXURE  cantilever from the column face = (1500 - 350)/2 = 575 ;  Mu = 190.0 x 0.575^2/2 = 31.4 kNm/m",
    "     Ast,req 136 ;  Cl. 26.5.2.1 MINIMUM 0.12 % x 600 = 720 mm2/m  *** GOVERNS ***",
    "     PROVIDED  T12 @ 150 BOTH WAYS (754),  x/d 0.056",
    "   ONE-WAY SHEAR  Cl. 34.2.4.1, critical at d from the face = 33 mm from the edge ; Vu 6.3 kN/m ; tau_v 0.012",
    "   PUNCHING  Cl. 31.6.1, perimeter at d/2 :  b0 = 4 x (350 + 542) = 3568 ; Vu = 276.8 - 190.0 x 0.892^2 = 125.6",
    "     tau_v 0.065 ; ks 1.0 ; tau_c = 0.25 sqrt(30) = 1.369   ->   NOT CRITICAL",
    "   ANCHORAGE  column starters T16, Ld,comp = 37 x 16 = 592.  Available 526 straight + 128 (8 phi) bend = 654",
    "   *** THE 600 DEPTH IS GOVERNED BY STARTER ANCHORAGE, NOT BY BENDING OR SHEAR - so nobody optimises it. ***",
    "",
    "SLAB S1  150 THK TWO-WAY, 3650 x 4650 c/c, BOTH FLOORS     dx = 116 ;  dy = 108",
    "   EFFECTIVE SPANS  Cl. 22.2(a), lesser of clear + d or c/c :  lx = min(3400+116, 3650) = 3516 ;",
    "     ly = min(4400+108, 4650) = 4508.   ly/lx = 1.282 < 2  ->  TWO-WAY, Cl. 24.4 and Annex D",
    "   MOMENT COEFFICIENTS  Table 26 (D-1.1) CASE 9, four edges discontinuous but RESTRAINED, with corner",
    "     torsion steel to Cl. D-1.8  ->  Table 26, NOT Table 27.   alpha x 0.0777 (at 1.282),  alpha y 0.056",
    "   wu = 1.5(4.750 + 3.000) = 11.625 kPa   THE FIRST FLOOR GOVERNS (the roof is 10.125)",
    "     Mx = 0.0777 x 11.625 x 3.516^2 = 11.17 kNm/m ;  My = 0.0560 x 11.625 x 3.516^2 = 8.05 kNm/m",
    "     Ast,req x 229, y 176 ;  Cl. 26.5.2.1 minimum 0.12 % x 150 = 180 mm2/m",
    "   PROVIDED  T8 @ 150 BOTH WAYS BOTTOM = 335 mm2/m  ->  Mu 16.09 / 14.92 kNm/m,  UTILISATION 69 % / 54 %",
    "   DEFLECTION  lx/dx = 30.3 ; basic taken as SIMPLY SUPPORTED = 20, the conservative assumption",
    "     fs 198 ; pt 0.289 % ; MF about 1.68  ->  permissible 33.6 > 30.3  OK",
    "   SHEAR  Vu about wu lx/3 = 13.6 kN/m ; tau_v 0.117 ; tau_c 0.390 x k 1.30 = 0.507  OK",
    "",
    "*** THE CORNER TORSION MATS ARE A HOLD POINT FOR REINFORCEMENT INSPECTION.  Table 26 is valid ONLY because",
    "    they are provided.  Omit them and the slab must be reassessed on Table 27. ***",
    "",
    "LOADS (A.7.7)  slab dead 4.750 (floor) / 5.250 (roof) kPa ;  imposed 3.000 (IS 875 Pt 2, OP) / 1.500 kPa",
    "   Load path to the beams, Cl. 24.5, 45 deg yield lines: peak intensity = w x 3.650/2 = w x 1.825 m",
    "   SHORT beams B1 -> TRIANGLE ;  LONG beams B2 -> TRAPEZOID, w,eq = w,peak x [1 - 1/(3 r^2)], r 1.274",
    "   Infill on the first-floor beams 13.000 kN/m.  SP-B1: brick at about 20 kN/m3 over 0.190 x 2.600 gives",
    "   about 9.9 kN/m, i.e. LIGHTER, so 13.000 and Vb = 73.18 kN stay conservative.  THAT IS A DIRECTION, NOT A",
    "   VERIFICATION - the re-run is open as WM-V6.",
    "",
    "OPEN ITEMS  SR2-V4 footing top level RECONSTRUCTED.  SR2-V5 no blinding stated.  SR2-V6 confining steel into",
    "   the footing not stated.  A.7.7 the roof projection term 3.037 kN/m is [NOT AVAILABLE].  U4 the sentry post",
    "   SITE POSITION is [ASSUMED] (RC4-F3).  Neither sheet depends on it.",
]
