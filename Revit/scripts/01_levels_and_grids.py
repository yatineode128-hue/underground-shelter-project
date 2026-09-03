"""
Dynamo Python Script node — RUN FIRST.

Creates the project Levels and Grids for the underground CBRN shelter, the
sentry post and the entry stairwell, from Master Parts A.4.1 / A.4.3 / A.4.5 /
A.4.8. Idempotent: re-running will not duplicate a Level or Grid that already
exists under the same name.

SOURCE OF TRUTH  master/MASTER_PROJECT_STATE.md Parts A.4.1, A.4.3, A.4.5, A.4.8
COORDINATE MAP   Master X (east, 0-22000) -> Revit X
                 Master "Y (plan)" (north, 0-6200) -> Revit Y
                 Master "LEVELS" (elevation, grade 0.000) -> Revit Z
                 This mapping is used consistently by every script in this set.

ASSUMPTION [ASSUMED] — the sentry post's absolute site position does not exist
anywhere in the project (Master A.2/A.4.8 and all four Rev F sentry-post DXF
sheets state only "sited >=10 m clear of the shelter excavation", no
coordinate). This script places its local grid origin at global
(11.000, 17.750) m — 10.000 m clear of the entry stairwell's north external
face (Y 7.750), the minimum the Master's rule allows, north of the approach it
would plausibly guard. CONFIRM THE REAL SITE POSITION AND ROTATION before this
is treated as final; both are single variables below (SENTRY_ORIGIN_X_M,
SENTRY_ORIGIN_Y_M, SENTRY_ROTATION_DEG) so relocating it later is a one-line
change, not a rebuild.

THIS IS THE ONLY PLACE THE ASSUMPTION LIVES. 06_structural_sentry_post.py does
NOT repeat these constants — it reads the actual "SA" and "S1" Grid elements
this script creates and derives every sentry post point from their real
geometry in the document, every time it runs.

HOW TO ACTUALLY RELOCATE IT (read this before assuming "just edit and
re-run" works — this script's own idempotency guard will NOT move a grid
that already exists under the same name, it will just skip it):
  (a) In Revit, delete the 4 sentry grids (SA, SB, S1, S2) -- Modify tab,
      select, Delete. Edit the three constants below. Re-run THIS script
      (creates the 4 grids fresh, at the new position/rotation). Re-run
      06_structural_sentry_post.py (rebuilds the frame from the new grids;
      anything 06 already built under the OLD position is not auto-deleted
      -- delete it by hand first if you don't want both).
  (b) Or skip the constants entirely: drag the 4 sentry grids to the
      correct position by hand in Revit, then just re-run
      06_structural_sentry_post.py. It reads whatever the grids say.
Either way there is exactly one source of truth (the grids in the model),
not two files that have to be kept in sync by hand.
"""
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from Autodesk.Revit.DB import (
    XYZ, Line, Level, Grid, UnitUtils, UnitTypeId,
    FilteredElementCollector, BuiltInCategory
)
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument


def m_to_ft(v):
    return UnitUtils.ConvertToInternalUnits(v, UnitTypeId.Meters)


def mm_to_ft(v):
    return UnitUtils.ConvertToInternalUnits(v, UnitTypeId.Millimeters)


# ---------------------------------------------------------------- LEVELS ---
# name -> elevation, metres, relative to Site Grade 0.000 (Master A.4.3)
LEVELS = [
    ("00 Formation (US PCC)",              -6.800),
    ("01 US Mat",                          -6.700),
    ("02 Shelter Floor (Internal-T-O-Mat)",-6.100),
    ("03 Stair Landing L1",                -4.7333),
    ("04 Stair Landing L2",                -3.3667),
    ("05 Roof Soffit",                     -2.900),
    ("06 Headhouse Floor (T-O-Roof Slab)", -2.000),
    ("07 Site Grade",                       0.000),
    ("08 Headhouse Roof Soffit",            0.400),
    ("09 Headhouse Roof Top (Berm Crest)",  0.900),
    ("10 Sentry Post GF FFL",               0.450),
    ("11 Sentry Post First Floor",          3.650),
    ("12 Sentry Post Roof",                 6.700),
    ("13 Sentry Post Parapet",              7.000),
]

# ----------------------------------------------------------------- GRIDS ---
# Shelter box (Master A.4.1-A.4.3): numbers along X at wall centrelines,
# letters along Y at the two perimeter wall centrelines. Only primary
# structural walls carry a grid; W8 partitions and bay boundaries do not
# (kept out to avoid over-cluttering a below-grade structural plan).
BOX_X_GRIDS = [
    ("1", 0.300),    # west perimeter wall centreline
    ("2", 12.700),   # W5 centreline
    ("3", 15.000),   # W6 centreline
    ("4", 18.200),   # W7 centreline
    ("5", 21.700),   # east perimeter wall centreline
]
BOX_Y_GRIDS = [
    ("A", 0.300),    # south perimeter wall centreline
    ("B", 5.900),    # north perimeter wall centreline
]
BOX_Y_EXTENT = (-1.0, 7.2)   # Y run of the X-grids, metres
BOX_X_EXTENT = (-1.0, 23.0)  # X run of the Y-grids, metres

# Sentry post (Master A.4.8) — local grid, see the ASSUMPTION note above.
SENTRY_ORIGIN_X_M = 11.000
SENTRY_ORIGIN_Y_M = 17.750
SENTRY_ROTATION_DEG = 0.0

SENTRY_X_GRIDS_LOCAL = [("SA", 0.175), ("SB", 3.825)]
SENTRY_Y_GRIDS_LOCAL = [("S1", 0.175), ("S2", 4.825)]
SENTRY_Y_EXTENT_LOCAL = (-1.0, 6.0)
SENTRY_X_EXTENT_LOCAL = (-1.0, 5.0)


def sentry_to_global(local_x_m, local_z_m):
    import math
    rad = math.radians(SENTRY_ROTATION_DEG)
    gx = SENTRY_ORIGIN_X_M + local_x_m * math.cos(rad) - local_z_m * math.sin(rad)
    gy = SENTRY_ORIGIN_Y_M + local_x_m * math.sin(rad) + local_z_m * math.cos(rad)
    return gx, gy


created_levels = []
skipped_levels = []
created_grids = []
skipped_grids = []

TransactionManager.Instance.EnsureInTransaction(doc)

existing_level_names = set(
    l.Name for l in FilteredElementCollector(doc).OfClass(Level)
)
for name, elev_m in LEVELS:
    if name in existing_level_names:
        skipped_levels.append(name)
        continue
    lvl = Level.Create(doc, m_to_ft(elev_m))
    lvl.Name = name
    created_levels.append(name)

existing_grid_names = set(
    g.Name for g in FilteredElementCollector(doc).OfClass(Grid)
)


def make_grid(name, p0_ft, p1_ft):
    if name in existing_grid_names:
        skipped_grids.append(name)
        return
    line = Line.CreateBound(p0_ft, p1_ft)
    g = Grid.Create(doc, line)
    g.Name = name
    created_grids.append(name)


for name, x_m in BOX_X_GRIDS:
    p0 = XYZ(m_to_ft(x_m), m_to_ft(BOX_Y_EXTENT[0]), 0.0)
    p1 = XYZ(m_to_ft(x_m), m_to_ft(BOX_Y_EXTENT[1]), 0.0)
    make_grid(name, p0, p1)

for name, y_m in BOX_Y_GRIDS:
    p0 = XYZ(m_to_ft(BOX_X_EXTENT[0]), m_to_ft(y_m), 0.0)
    p1 = XYZ(m_to_ft(BOX_X_EXTENT[1]), m_to_ft(y_m), 0.0)
    make_grid(name, p0, p1)

for name, lx_m in SENTRY_X_GRIDS_LOCAL:
    gx0, gy0 = sentry_to_global(lx_m, SENTRY_Y_EXTENT_LOCAL[0])
    gx1, gy1 = sentry_to_global(lx_m, SENTRY_Y_EXTENT_LOCAL[1])
    p0 = XYZ(m_to_ft(gx0), m_to_ft(gy0), 0.0)
    p1 = XYZ(m_to_ft(gx1), m_to_ft(gy1), 0.0)
    make_grid(name, p0, p1)

for name, lz_m in SENTRY_Y_GRIDS_LOCAL:
    gx0, gy0 = sentry_to_global(SENTRY_X_EXTENT_LOCAL[0], lz_m)
    gx1, gy1 = sentry_to_global(SENTRY_X_EXTENT_LOCAL[1], lz_m)
    p0 = XYZ(m_to_ft(gx0), m_to_ft(gy0), 0.0)
    p1 = XYZ(m_to_ft(gx1), m_to_ft(gy1), 0.0)
    make_grid(name, p0, p1)

TransactionManager.Instance.TransactionTaskDone()

OUT = (
    "Levels created: {}  |  already existed: {}\n"
    "Grids created: {}  |  already existed: {}\n"
    "SENTRY POST PLACEMENT IS ASSUMED at global ({}, {}) m, rotation {} deg — "
    "no coordinate exists in the source project; confirm before Phase 2."
).format(
    created_levels, skipped_levels, created_grids, skipped_grids,
    SENTRY_ORIGIN_X_M, SENTRY_ORIGIN_Y_M, SENTRY_ROTATION_DEG
)
