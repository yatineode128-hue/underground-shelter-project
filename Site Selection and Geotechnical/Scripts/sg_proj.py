"""sg_proj.py  --  constants for the SITE SELECTION AND GEOTECHNICAL package
(revision SG1).

WHAT THIS PACKAGE IS.  The project has always carried its site and its ground
as ASSUMPTIONS.  Master A.6 tags every soil parameter [ASSUMED], K.2 lists six
of them (A1, A2, A4, A5, A7, A8) as things that must be confirmed before
construction, and Part J draws [SITE INVESTIGATION] as a root node with nothing
feeding it.  Two documents have now been supplied that feed it for the first
time:

  1. REPORT ON SUB-SOIL INVESTIGATION FOR CTW PH-III ACCN PROJECT AT CME PUNE
     Soil Engineering & Material Testing Wing, College of Military Engineering,
     Pune 411 031.  SEMT Code No. SEMT/67/15.  Raised on CTW's request, letter
     No 8722/Ph-III/CTW/116/Q dated 20 May 2015.  11 trial pits, 3 locations,
     Appendices A (classification), B (soil test result) and C (rock cores),
     Sketches P (trial pit location plan) and Q (trial pit details).

  2. The P1 presentation deck, "CONSTRUCTION OF CBRN HARDENED UNDERGROUND OPS
     ROOM", Team GROUNDZERO, 32 slides: site location, contour, watershed, road
     connectivity, pipelines, site recce, elevation profile, SWOT, wind,
     precipitation, temperature, seismic and soil slides.

WHAT THIS PACKAGE DOES NOT DO.  It resolves nothing.  Master rule M.6 and the
project CLAUDE.md both forbid converting an [ASSUMED] into a confirmed fact, and
nothing here does.  What it does is give every assumed soil parameter a
PROVENANCE for the first time, reproduce the two documents' own arithmetic, and
state precisely where they support the design, where they do not reach it, and
where they disagree with each other.

THE ONE FACT THAT GOVERNS THE PACKAGE.  The sub-soil investigation reached
about 1.5 m.  The structure founds at (-)6.800.  Everything the project holds
about the ground below (-)2.000 - rockhead continuity, red-bole seams, k_s,
the design groundwater table - is extrapolation, and the report cannot be read
as confirming any of it.

SENTRY POST: IN SCOPE for ground only.  Footing F1 bears on in-situ basalt at
(-)2.000 and that is a geotechnical statement, so it is checked here.  No
sentry post structural value is touched.
MAIN STAIRCASE: FROZEN.  Nothing in this package refers to it except to say so.
"""

PACKAGE = "SITE SELECTION AND GEOTECHNICAL"

# REV / PACKAGE_DATE identify the SG1 RECORD - the documents, schedules and
# calculation SG1 produced.  They are not bumped, because SG1 is a revision
# that happened and Part H preserves it (rule M.11).
REV = "SG1"
PACKAGE_DATE = "11.09.2026"

# PKG_REV is the CURRENT revision of the package, and it is what every DRAWING
# title block carries - a drawing always shows the revision it is issued at.
# At SG2 the three SG1 sheets were re-issued with NO CONTENT CHANGE beyond the
# revision and sheet-count fields; SG-102 and SG-202 are new.
PKG_REV = "SG2"
PKG_DATE = "11.09.2026"
SHEETS_TOTAL = 5
GEOM_REV = "GEOMETRY REV F + M1"
STATUS = "FOR REVIEW - NOT FOR CONSTRUCTION"

# --------------------------------------------------------------- evidence
EVIDENCE = [
    ("[C]", "CONFIRMED",
     "traceable to the master, to a Rev F drawing, to sheet S-06, or read "
     "verbatim off one of the two supplied documents"),
    ("[R]", "RECONSTRUCTED",
     "computed here from confirmed values; the arithmetic is shown in full"),
    ("[D]", "DERIVED",
     "an engineering result computed by THIS package"),
    ("[A]", "ASSUMED",
     "an engineering selection made by THIS package - confirm before "
     "construction"),
    ("[U]", "UNRESOLVED",
     "the two documents disagree, or they disagree with the master"),
    ("[N]", "NOT AVAILABLE",
     "no source exists anywhere in the project - DATA REQUIRED"),
]

# -------------------------------------------------------------- constants
KGCM2_KPA = 98.0665          # 1 kgf/cm2 in kPa, exact by definition of kgf
GCC_KNM3 = 9.81              # 1 g/cc in kN/m3
G_S = 2.75                   # specific gravity, basalt-derived murrum   [A]

# ----------------------------------------------- levels the package uses [C]
# master A.4.3 / A.6.  Project datum: finished grade = 0.000.
LVL_GRADE = 0.000
LVL_SLAB_TOP = -2.000
LVL_FLOOR = -6.100
LVL_MAT_SOFFIT = -6.700
LVL_FORMATION = -6.800
LVL_GWT_DESIGN = -2.000      # [A] master A.6 / K.2 A2
LVL_SUMP_BASE = -8.000
LVL_F1_FOUND = -2.000        # sentry footing F1, master B.8.7

ROCKHEAD_MASTER = (-1.500, -2.000)          # [A] master A.6
EXCAV_PLAN_AREA = 196.800    # m2, [R] back-figured from the WM1 BOQ, see calc

# ------------------------------------- bearing demands already in the master
Q_MAT_SERVICE = 58.4         # kPa, master B.3                            [C]
Q_MAT_BLAST = 404.9          # kPa, master B.3                            [C]
Q_F1_SERVICE = 157.6         # kPa, master B.8.7                          [C]
SBC_MASTER = 3240.0          # kPa, IS 1904:1986 Table 1 hard rock        [A]

# ------------------------------------------ soil parameters in master A.6 [A]
GAMMA_BULK = 20.0            # kN/m3
GAMMA_SAT = 21.0             # kN/m3
K0_MASTER = 0.50             # 1 - sin(phi), phi ~ 30 deg
GRADIENT_MASTER = 15.41      # kPa/m, K0*gamma' + gamma_w
COVER_FILL_GAMMA = 20.0      # kN/m3, the 750 compacted engineered fill
COVER_TOTAL_DESIGN = 40.65   # kPa, held by RC1 / C17
COVER_LAYER_SUM = 39.15      # kPa, the six layers as tabulated in A.7.3

# ------------------------------------------------- works management figures
WM_ROCK_M3 = 993.84          # BOQ E-02b at the mean rockhead (-)1.750    [C]
WM_ROCK_RANGE = (944.6, 1043.0)                                        # [C]
WM_ROCK_RATE_M3_DAY = 60.0   # WBS A2050                                  [C]

__all__ = [n for n in dir() if not n.startswith("_")]
