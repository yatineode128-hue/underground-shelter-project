"""
Dynamo Python Script node — RUN SIXTH (last), after 01-05.

Builds the sentry post frame: 4 isolated footings (F1), a plinth beam, 4
columns per storey (C1, 2 storeys), 4 beams per storey (B1 x2 + B2 x2, 2
storeys), 2 two-way slabs (S1, one per floor), and the ground-storey 200 mm
RC ballistic infill panels.

SOURCE OF TRUTH  master/MASTER_PROJECT_STATE.md A.4.8, B.8.1-B.8.7 —
                 cross-checked against current/staad/Sentry_Post_Framed_Seismic.std
                 (12 joints, 16 members, groups _COL_GF/_COL_FF/_BEAM_FF/_BEAM_RF,
                 fixed supports at Y=0.450 = GF FFL, confirming the STAAD frame
                 starts AT plinth level, not at the footing).

*** ASSUMED SITE PLACEMENT — see 01_levels_and_grids.py header ***. The
constants below (SENTRY_ORIGIN_X_M/Y_M/ROTATION_DEG) MUST be kept identical
to the ones in that script; change one, change both, or the frame will land
somewhere other than where the grids in script 01 say it is.

NOT MODELLED (flagged, not guessed):
  - First-storey infill ("armoured vision panels, 1200 wide", A.4.8) has no
    stated thickness anywhere in the Master or the Rev F DXFs, so it is
    NOT built here. [NOT AVAILABLE]
  - The column segment between the footing top and the plinth beam
    (-1.400 to +0.450) is not separately named or sized in the Master — the
    footing and the STAAD frame (which starts at +0.450) simply do not meet
    without one. This script adds a 350x350 stub there for structural
    continuity only; it is an inferred connector, not a Master value, and is
    reported as such in the Phase 1 QA list.
"""
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from Autodesk.Revit.DB import (
    XYZ, Line, CurveLoop, Wall, WallType, WallKind, Floor, FloorType,
    Level, FamilySymbol, BuiltInCategory, StructuralType, UnitUtils,
    UnitTypeId, FilteredElementCollector, BuiltInParameter
)
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
import math

doc = DocumentManager.Instance.CurrentDBDocument


def m_to_ft(v):
    return UnitUtils.ConvertToInternalUnits(v, UnitTypeId.Meters)


def mm_to_ft(v):
    return UnitUtils.ConvertToInternalUnits(v, UnitTypeId.Millimeters)


def get_level(name):
    for l in FilteredElementCollector(doc).OfClass(Level):
        if l.Name == name:
            return l
    raise Exception("Level not found, run 01_levels_and_grids.py first: " + name)


def get_or_duplicate_wall_type(name, thickness_mm):
    for wt in FilteredElementCollector(doc).OfClass(WallType):
        if wt.Name == name:
            return wt
    template = None
    for wt in FilteredElementCollector(doc).OfClass(WallType):
        if wt.Kind == WallKind.Basic:
            template = wt
            break
    new_type = template.Duplicate(name)
    cs = new_type.GetCompoundStructure()
    idx = cs.GetFirstCoreLayerIndex()
    cs.SetLayerWidth(idx, mm_to_ft(thickness_mm))
    new_type.SetCompoundStructure(cs)
    return new_type


def get_or_duplicate_floor_type(name, thickness_mm):
    for ft in FilteredElementCollector(doc).OfClass(FloorType):
        if ft.Name == name:
            return ft
    template = list(FilteredElementCollector(doc).OfClass(FloorType))[0]
    new_type = template.Duplicate(name)
    cs = new_type.GetCompoundStructure()
    idx = cs.GetFirstCoreLayerIndex()
    cs.SetLayerWidth(idx, mm_to_ft(thickness_mm))
    new_type.SetCompoundStructure(cs)
    return new_type


def rect_loop_xy(x0, y0, x1, y1, z_ft):
    p1, p2, p3, p4 = (
        XYZ(m_to_ft(x0), m_to_ft(y0), z_ft),
        XYZ(m_to_ft(x1), m_to_ft(y0), z_ft),
        XYZ(m_to_ft(x1), m_to_ft(y1), z_ft),
        XYZ(m_to_ft(x0), m_to_ft(y1), z_ft),
    )
    loop = CurveLoop()
    for a, b in [(p1, p2), (p2, p3), (p3, p4), (p4, p1)]:
        loop.Append(Line.CreateBound(a, b))
    return loop


def mark_structural(elem):
    p = elem.get_Parameter(BuiltInParameter.FLOOR_PARAM_IS_STRUCTURAL)
    if p and not p.IsReadOnly:
        p.Set(1)


def first_symbol(bic):
    syms = list(
        FilteredElementCollector(doc).OfClass(FamilySymbol)
        .OfCategory(bic)
    )
    if not syms:
        cat_name = {
            BuiltInCategory.OST_StructuralColumns: "Structural Columns -> a concrete rectangular column family (e.g. Concrete-Rectangular-Column.rfa)",
            BuiltInCategory.OST_StructuralFraming: "Structural Framing -> a concrete rectangular beam family (e.g. Concrete-Rectangular Beam.rfa)",
            BuiltInCategory.OST_StructuralFoundation: "Structural Foundation -> an isolated footing family (e.g. Footing-Rectangular.rfa)",
        }.get(bic, str(bic))
        raise Exception(
            "No family loaded in category {}. In Revit: Insert tab -> Load "
            "Family -> Structural Templates -> {} -- then re-run this script."
            .format(bic, cat_name)
        )
    sym = syms[0]
    if not sym.IsActive:
        sym.Activate()
    return sym


def set_param_try(elem, names, value):
    for n in names:
        p = elem.LookupParameter(n)
        if p and not p.IsReadOnly:
            p.Set(value)
            return True
    return False


# ------------------------------------------------------- SITE PLACEMENT ---
SENTRY_ORIGIN_X_M = 11.000
SENTRY_ORIGIN_Y_M = 17.750
SENTRY_ROTATION_DEG = 0.0


def loc(local_x_m, local_z_m):
    rad = math.radians(SENTRY_ROTATION_DEG)
    gx = SENTRY_ORIGIN_X_M + local_x_m * math.cos(rad) - local_z_m * math.sin(rad)
    gy = SENTRY_ORIGIN_Y_M + local_x_m * math.sin(rad) + local_z_m * math.cos(rad)
    return gx, gy


created = []

TransactionManager.Instance.EnsureInTransaction(doc)

lvl_gf = get_level("10 Sentry Post GF FFL")
lvl_ff = get_level("11 Sentry Post First Floor")
lvl_roof = get_level("12 Sentry Post Roof")

# --------------------------------------------------------- FOOTINGS F1 ----
# 1500 x 1500 x 600, 4 No., founded on basalt at -2.000 (bottom); top -1.400.
footing_type = get_or_duplicate_floor_type("Foundation - Sentry F1 1500x1500x600 (M30)", 600)
grid_points_local = {
    "A-1": (0.175, 0.175), "A-2": (0.175, 4.825),
    "B-1": (3.825, 0.175), "B-2": (3.825, 4.825),
}
FOOTING_TOP_Z = -1.400
for mark, (lx, lz) in grid_points_local.items():
    gx, gy = loc(lx, lz)
    loop = rect_loop_xy(gx - 0.750, gy - 0.750, gx + 0.750, gy + 0.750, m_to_ft(FOOTING_TOP_Z))
    f = Floor.Create(doc, [loop], footing_type.Id, lvl_gf.Id)
    mark_structural(f)
    f.get_Parameter(BuiltInParameter.ALL_MODEL_MARK).Set("F1 Footing " + mark)
    created.append("F1 Footing " + mark)

# --------------------------------------------------- COLUMNS + STUBS ------
col_sym = first_symbol(BuiltInCategory.OST_StructuralColumns)
col_type = col_sym.Duplicate("Sentry Column C1 350x350 (M30)")
set_param_try(col_type, ["b", "Width", "bF", "b/Diameter"], mm_to_ft(350))
set_param_try(col_type, ["h", "Depth", "hF"], mm_to_ft(350))

for mark, (lx, lz) in grid_points_local.items():
    gx, gy = loc(lx, lz)
    pt = XYZ(m_to_ft(gx), m_to_ft(gy), 0.0)
    # Stub: footing top (-1.400) to GF FFL (+0.450) -- inferred connector, see header
    stub = doc.Create.NewFamilyInstance(pt, col_type, lvl_gf, StructuralType.Column)
    set_param_try(stub, ["Base Level"], lvl_gf.Id)
    set_param_try(stub, ["Base Offset", "b Offset"], m_to_ft(FOOTING_TOP_Z) - lvl_gf.Elevation)
    set_param_try(stub, ["Top Level"], lvl_gf.Id)
    set_param_try(stub, ["Top Offset", "t Offset"], 0.0)
    created.append("Column stub (footing-to-plinth, inferred) " + mark)

    # Ground-storey column: GF FFL (+0.450) to First Floor (+3.650)
    col_gf = doc.Create.NewFamilyInstance(pt, col_type, lvl_gf, StructuralType.Column)
    set_param_try(col_gf, ["Top Level"], lvl_ff.Id)
    col_gf.get_Parameter(BuiltInParameter.ALL_MODEL_MARK).Set("C1 GF " + mark)
    created.append("Column C1 (ground storey) " + mark)

    # First-storey column: First Floor (+3.650) to Roof (+6.700)
    col_ff = doc.Create.NewFamilyInstance(pt, col_type, lvl_ff, StructuralType.Column)
    set_param_try(col_ff, ["Top Level"], lvl_roof.Id)
    col_ff.get_Parameter(BuiltInParameter.ALL_MODEL_MARK).Set("C1 FF " + mark)
    created.append("Column C1 (first storey) " + mark)

# -------------------------------------------------------------- BEAMS -----
beam_sym = first_symbol(BuiltInCategory.OST_StructuralFraming)
beam_type_b1 = beam_sym.Duplicate("Sentry Beam B1 250x450 (M30)")
set_param_try(beam_type_b1, ["b", "Width"], mm_to_ft(250))
set_param_try(beam_type_b1, ["h", "Depth"], mm_to_ft(450))
beam_type_b2 = beam_sym.Duplicate("Sentry Beam B2 250x450 (M30)")
set_param_try(beam_type_b2, ["b", "Width"], mm_to_ft(250))
set_param_try(beam_type_b2, ["h", "Depth"], mm_to_ft(450))

# B1 spans A-B (X, 3650 c/c) on grids 1 and 2 ; B2 spans 1-2 (Z, 4650 c/c) on grids A and B
beam_defs = [
    ("B1 @ Grid 1", beam_type_b1, (0.175, 0.175), (3.825, 0.175)),
    ("B1 @ Grid 2", beam_type_b1, (0.175, 4.825), (3.825, 4.825)),
    ("B2 @ Grid A", beam_type_b2, (0.175, 0.175), (0.175, 4.825)),
    ("B2 @ Grid B", beam_type_b2, (3.825, 0.175), (3.825, 4.825)),
]
for storey_mark, lvl in [("FF", lvl_ff), ("Roof", lvl_roof)]:
    for mark, btype, p0_local, p1_local in beam_defs:
        gx0, gy0 = loc(*p0_local)
        gx1, gy1 = loc(*p1_local)
        curve = Line.CreateBound(
            XYZ(m_to_ft(gx0), m_to_ft(gy0), lvl.Elevation),
            XYZ(m_to_ft(gx1), m_to_ft(gy1), lvl.Elevation),
        )
        b = doc.Create.NewFamilyInstance(curve, btype, lvl, StructuralType.Beam)
        b.get_Parameter(BuiltInParameter.ALL_MODEL_MARK).Set(mark + " " + storey_mark)
        created.append("Beam " + mark + " " + storey_mark)

# ------------------------------------------------------------- PLINTH -----
# PB 250 x 400 at +0.450, perimeter of the 4 columns.
plinth_type = get_or_duplicate_wall_type("Structural Beam-as-Wall - Plinth PB 250x400 (M30)", 250)
# Modelled as a shallow structural wall band at GF level for simplicity;
# true plinth BEAMS (250 wide x 400 deep) can be substituted with the same
# beam family used above if the user prefers a framing element here.
pb_corners_local = [(0.175, 0.175), (3.825, 0.175), (3.825, 4.825), (0.175, 4.825)]
pb_pts = [loc(x, z) for x, z in pb_corners_local]
for i in range(4):
    x0, y0 = pb_pts[i]
    x1, y1 = pb_pts[(i + 1) % 4]
    curve = Line.CreateBound(
        XYZ(m_to_ft(x0), m_to_ft(y0), 0.0),
        XYZ(m_to_ft(x1), m_to_ft(y1), 0.0),
    )
    w = Wall.Create(doc, curve, plinth_type.Id, lvl_gf.Id, mm_to_ft(400), 0.0, False, True)
    w.get_Parameter(BuiltInParameter.ALL_MODEL_MARK).Set("PB Plinth Beam")
created.append("Plinth beam (4 sides, modelled as structural wall band)")

# -------------------------------------------------------------- SLABS -----
# S1, 150 mm two-way, both floors, external footprint 4.000 x 5.000 local.
slab_type = get_or_duplicate_floor_type("Slab - Sentry S1 150mm (M30)", 150)
s1_corners_local = (0.0, 0.0, 4.000, 5.000)
for storey_mark, lvl in [("First Floor", lvl_ff), ("Roof", lvl_roof)]:
    x0, y0 = loc(s1_corners_local[0], s1_corners_local[1])
    x1, y1 = loc(s1_corners_local[2], s1_corners_local[3])
    loop = rect_loop_xy(min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1), lvl.Elevation)
    s = Floor.Create(doc, [loop], slab_type.Id, lvl.Id)
    mark_structural(s)
    created.append("Slab S1 - " + storey_mark)

# ------------------------------------------------- GROUND-STOREY INFILL ---
# 200 mm RC ballistic panels, non-structural (STAAD: "carried by the beam...
# as a UDL"), all 4 faces, GF FFL (+0.450) to First Floor (+3.650).
infill_type = get_or_duplicate_wall_type("Non-Bearing Wall - Sentry Ballistic Infill 200mm (M30)", 200)
for i in range(4):
    x0, y0 = pb_pts[i]
    x1, y1 = pb_pts[(i + 1) % 4]
    curve = Line.CreateBound(
        XYZ(m_to_ft(x0), m_to_ft(y0), 0.0),
        XYZ(m_to_ft(x1), m_to_ft(y1), 0.0),
    )
    w = Wall.Create(doc, curve, infill_type.Id, lvl_gf.Id, m_to_ft(3.200), 0.0, False, False)
    w.get_Parameter(BuiltInParameter.ALL_MODEL_MARK).Set("Ground-storey ballistic infill")
created.append("Ground-storey ballistic infill (4 faces, non-structural)")

TransactionManager.Instance.TransactionTaskDone()

OUT = "Sentry post structural elements created:\n" + "\n".join(created)
