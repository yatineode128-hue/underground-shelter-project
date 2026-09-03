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

*** ASSUMED SITE PLACEMENT — derived LIVE from the model, not hardcoded ***
The sentry post's absolute site position does not exist anywhere in the
project (Master A.2/A.4.8 and every Rev F sentry DXF state only "sited
>=10 m clear of the shelter excavation"). At Phase 1B this script stopped
duplicating the SENTRY_ORIGIN_X_M/Y_M/ROTATION_DEG constants that
01_levels_and_grids.py defines: instead it reads the ACTUAL "SA" and "S1"
Grid elements that script already placed in this document, and derives the
frame's origin and orientation from their real geometry. There is now
exactly ONE place the assumed position lives — the constants inside
01_levels_and_grids.py (or the 4 sentry grids, if you drag them by hand in
Revit) — and this script will always follow whatever they say on its next
run. If the grids are missing, this script stops with a clear error rather
than inventing a position.

NOT MODELLED (flagged, not guessed):
  - First-storey infill ("armoured vision panels, 1200 wide", A.4.8) has no
    stated thickness anywhere in the Master or the Rev F DXFs, so it is
    NOT built here. [NOT AVAILABLE]
  - The column segment between the footing top and the plinth beam
    (-1.400 to +0.450) is not separately named or sized in the Master — the
    footing and the STAAD frame (which starts at +0.450) simply do not meet
    without one. This script adds a 350x350 stub there for structural
    continuity only; it is an inferred connector, not a Master value, and is
    reported as such in the Phase 1 QA list. FOOTING_TOP_Z / GF_ELEV_M below
    are where that inference lives.

RERUN SAFETY — every element carries a unique Mark; re-running skips marks
already present in the relevant category (Walls / Floors / Structural
Columns / Structural Framing) in the document. Family TYPES are looked up by
name before duplicating (get_or_duplicate_symbol), so re-running does not
error out on "type already exists" either.

ROBUSTNESS NOTE ON FAMILY CONTENT — this script needs a rectangular concrete
column family loaded in Structural Columns and a rectangular concrete beam
family loaded in Structural Framing (both are standard Revit content, e.g.
"Concrete-Rectangular-Column.rfa" / "Concrete-Rectangular Beam.rfa", usually
preloaded by a Structural Template). It picks the loaded symbol whose family
name best matches "concrete"/"rectangular"; if nothing loaded matches those
words at all, it still proceeds (with whatever IS loaded) and says so in OUT
-- check that message. If NOTHING is loaded in a category, it stops with an
exact Insert-tab instruction rather than failing silently.
"""
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from Autodesk.Revit.DB import (
    XYZ, Line, CurveLoop, Wall, WallType, WallKind, Floor, FloorType,
    Level, Grid, FamilySymbol, BuiltInCategory, StructuralType, UnitUtils,
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


def get_grid(name):
    for g in FilteredElementCollector(doc).OfClass(Grid):
        if g.Name == name:
            return g
    raise Exception(
        "Sentry grid '{}' not found -- run 01_levels_and_grids.py first. This "
        "script derives the sentry post's position from the SA/S1 grids that "
        "script creates; it does not hardcode a site position.".format(name)
    )


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


def get_or_duplicate_symbol(base_symbol, name):
    """Idempotent FamilySymbol duplication -- looked up by name first, so a
    second run reuses the type instead of throwing 'name already in use'."""
    for sym in FilteredElementCollector(doc).OfClass(FamilySymbol):
        if sym.Name == name:
            if not sym.IsActive:
                sym.Activate()
            return sym
    new_sym = base_symbol.Duplicate(name)
    if not new_sym.IsActive:
        new_sym.Activate()
    return new_sym


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


def existing_marks(bic):
    result = set()
    for el in FilteredElementCollector(doc).OfCategory(bic).WhereElementIsNotElementType():
        p = el.get_Parameter(BuiltInParameter.ALL_MODEL_MARK)
        if p:
            v = p.AsString()
            if v:
                result.add(v)
    return result


def set_mark(elem, mark):
    p = elem.get_Parameter(BuiltInParameter.ALL_MODEL_MARK)
    if p and not p.IsReadOnly:
        p.Set(mark)


def set_param_builtin_or_name(elem, builtin_param, fallback_names, value):
    p = None
    if builtin_param is not None:
        p = elem.get_Parameter(builtin_param)
        if p and p.IsReadOnly:
            p = None
    if not p:
        for n in fallback_names:
            p2 = elem.LookupParameter(n)
            if p2 and not p2.IsReadOnly:
                p = p2
                break
    if p:
        p.Set(value)
        return True
    return False


def best_symbol(bic, hints, warnings_list, label):
    syms = list(FilteredElementCollector(doc).OfClass(FamilySymbol).OfCategory(bic))
    if not syms:
        cat_name = {
            BuiltInCategory.OST_StructuralColumns: "Structural Columns -> a concrete rectangular column family (e.g. Concrete-Rectangular-Column.rfa)",
            BuiltInCategory.OST_StructuralFraming: "Structural Framing -> a concrete rectangular beam family (e.g. Concrete-Rectangular Beam.rfa)",
        }.get(bic, str(bic))
        raise Exception(
            "No family loaded in category {}. In Revit: Insert tab -> Load "
            "Family -> Structural Templates -> {} -- then re-run this script."
            .format(bic, cat_name)
        )

    def score(s):
        name = (s.Family.Name + " " + s.Name).lower()
        return sum(1 for h in hints if h in name)

    syms.sort(key=score, reverse=True)
    chosen = syms[0]
    if score(chosen) == 0:
        warnings_list.append(
            "No loaded {} family name matched {} -- used '{}' ({}) instead. "
            "Verify this is a plain rectangular concrete section before trusting "
            "sizes/quantities.".format(label, hints, chosen.Family.Name, chosen.Name)
        )
    if not chosen.IsActive:
        chosen.Activate()
    return chosen


def unit_xy(vec):
    length = math.sqrt(vec.X * vec.X + vec.Y * vec.Y)
    if length < 1e-9:
        raise Exception("Degenerate grid direction vector -- check grids SA/S1 in the model.")
    return XYZ(vec.X / length, vec.Y / length, 0.0)


def line_intersection_xy(p1, p2, p3, p4):
    x1, y1, x2, y2 = p1.X, p1.Y, p2.X, p2.Y
    x3, y3, x4, y4 = p3.X, p3.Y, p4.X, p4.Y
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(denom) < 1e-9:
        raise Exception("Sentry grids SA and S1 are parallel in this document -- cannot derive the frame origin.")
    a = x1 * y2 - y1 * x2
    b = x3 * y4 - y3 * x4
    px = (a * (x3 - x4) - (x1 - x2) * b) / denom
    py = (a * (y3 - y4) - (y1 - y2) * b) / denom
    return XYZ(px, py, 0.0)


created = []
skipped = []
warnings = []

TransactionManager.Instance.EnsureInTransaction(doc)

lvl_gf = get_level("10 Sentry Post GF FFL")
lvl_ff = get_level("11 Sentry Post First Floor")
lvl_roof = get_level("12 Sentry Post Roof")
GF_ELEV_M = 0.450  # matches "10 Sentry Post GF FFL" -- Master A.4.3

# ------------------------------------------------- SITE PLACEMENT (LIVE) --
# See the module docstring. Derived from the actual SA/S1 grids, not from a
# duplicated constant.
grid_SA = get_grid("SA")
grid_S1 = get_grid("S1")
c_SA = grid_SA.Curve
c_S1 = grid_S1.Curve
x_dir = unit_xy(c_S1.GetEndPoint(1).Subtract(c_S1.GetEndPoint(0)))  # local-X, in global XY
z_dir = unit_xy(c_SA.GetEndPoint(1).Subtract(c_SA.GetEndPoint(0)))  # local-Z, in global XY
grid_a1_pt = line_intersection_xy(
    c_SA.GetEndPoint(0), c_SA.GetEndPoint(1), c_S1.GetEndPoint(0), c_S1.GetEndPoint(1)
)
# grid_a1_pt is grid A/1's intersection = local (0.175, 0.175); back out local (0,0)
sentry_origin = grid_a1_pt.Subtract(x_dir.Multiply(mm_to_ft(175))).Subtract(z_dir.Multiply(mm_to_ft(175)))


def sentry_point(local_x_m, local_z_m):
    """Local (x along grid SA->SB, z along grid S1->S2), metres -> global XYZ, feet, Z=0."""
    return sentry_origin.Add(x_dir.Multiply(m_to_ft(local_x_m))).Add(z_dir.Multiply(m_to_ft(local_z_m)))


def rect_loop_local(center_pt, half_x_m, half_z_m, z_ft):
    """Rectangle aligned to the sentry post's own local axes (x_dir/z_dir),
    not necessarily global X/Y -- correct even if SENTRY_ROTATION_DEG != 0."""
    hx = x_dir.Multiply(m_to_ft(half_x_m))
    hz = z_dir.Multiply(m_to_ft(half_z_m))
    base = XYZ(center_pt.X, center_pt.Y, z_ft)
    p1 = base.Subtract(hx).Subtract(hz)
    p2 = base.Add(hx).Subtract(hz)
    p3 = base.Add(hx).Add(hz)
    p4 = base.Subtract(hx).Add(hz)
    loop = CurveLoop()
    for a, b in [(p1, p2), (p2, p3), (p3, p4), (p4, p1)]:
        loop.Append(Line.CreateBound(a, b))
    return loop


wall_marks = existing_marks(BuiltInCategory.OST_Walls)
floor_marks = existing_marks(BuiltInCategory.OST_Floors)
col_marks = existing_marks(BuiltInCategory.OST_StructuralColumns)
beam_marks = existing_marks(BuiltInCategory.OST_StructuralFraming)

# --------------------------------------------------------- FOOTINGS F1 ----
# 1500 x 1500 x 600, 4 No., founded on basalt at -2.000 (bottom); top -1.400.
# FOOTING_TOP_Z is the inferred founding assumption -- see module docstring.
FOOTING_TOP_Z = -1.400
grid_points_local = {
    "A-1": (0.175, 0.175), "A-2": (0.175, 4.825),
    "B-1": (3.825, 0.175), "B-2": (3.825, 4.825),
}
for mark, (lx, lz) in grid_points_local.items():
    full_mark = "F1 Footing " + mark
    if full_mark in floor_marks:
        skipped.append(full_mark)
        continue
    footing_type = get_or_duplicate_floor_type("Foundation - Sentry F1 1500x1500x600 (M30)", 600)
    center = sentry_point(lx, lz)
    loop = rect_loop_local(center, 0.750, 0.750, m_to_ft(FOOTING_TOP_Z))
    f = Floor.Create(doc, [loop], footing_type.Id, lvl_gf.Id)
    mark_structural(f)
    set_mark(f, full_mark)
    floor_marks.add(full_mark)
    created.append(full_mark)

# --------------------------------------------------- COLUMNS + STUBS ------
col_base_sym = best_symbol(BuiltInCategory.OST_StructuralColumns, ["concrete", "rectangular"], warnings, "column")
col_type = get_or_duplicate_symbol(col_base_sym, "Sentry Column C1 350x350 (M30)")
if not set_param_builtin_or_name(col_type, None, ["b", "Width", "bF"], mm_to_ft(350)):
    warnings.append("Could not set column width (b) on 'Sentry Column C1 350x350 (M30)' -- check its type parameters by hand.")
if not set_param_builtin_or_name(col_type, None, ["h", "Depth", "hF"], mm_to_ft(350)):
    warnings.append("Could not set column depth (h) on 'Sentry Column C1 350x350 (M30)' -- check its type parameters by hand.")


def place_column(local_x_m, local_z_m, base_level, base_offset_m, top_level, top_offset_m, mark):
    if mark in col_marks:
        skipped.append(mark)
        return None
    p = sentry_point(local_x_m, local_z_m)
    pt = XYZ(p.X, p.Y, base_level.Elevation)
    inst = doc.Create.NewFamilyInstance(pt, col_type, base_level, StructuralType.Column)
    set_param_builtin_or_name(inst, BuiltInParameter.FAMILY_BASE_LEVEL_PARAM, ["Base Level"], base_level.Id)
    set_param_builtin_or_name(inst, BuiltInParameter.FAMILY_BASE_LEVEL_OFFSET_PARAM, ["Base Offset"], m_to_ft(base_offset_m))
    set_param_builtin_or_name(inst, BuiltInParameter.FAMILY_TOP_LEVEL_PARAM, ["Top Level"], top_level.Id)
    set_param_builtin_or_name(inst, BuiltInParameter.FAMILY_TOP_LEVEL_OFFSET_PARAM, ["Top Offset"], m_to_ft(top_offset_m))
    set_mark(inst, mark)
    col_marks.add(mark)
    created.append(mark)
    return inst


for grid_mark, (lx, lz) in grid_points_local.items():
    # Stub: footing top (-1.400) to GF FFL (+0.450) -- inferred connector, see header.
    place_column(lx, lz, lvl_gf, FOOTING_TOP_Z - GF_ELEV_M, lvl_gf, 0.0,
                 "Column stub (footing-to-plinth, inferred) " + grid_mark)
    # Ground-storey column: GF FFL (+0.450) to First Floor (+3.650).
    place_column(lx, lz, lvl_gf, 0.0, lvl_ff, 0.0, "C1 GF " + grid_mark)
    # First-storey column: First Floor (+3.650) to Roof (+6.700).
    place_column(lx, lz, lvl_ff, 0.0, lvl_roof, 0.0, "C1 FF " + grid_mark)

# -------------------------------------------------------------- BEAMS -----
beam_base_sym = best_symbol(BuiltInCategory.OST_StructuralFraming, ["concrete", "rectangular"], warnings, "beam")
beam_type_b1 = get_or_duplicate_symbol(beam_base_sym, "Sentry Beam B1 250x450 (M30)")
set_param_builtin_or_name(beam_type_b1, None, ["b", "Width"], mm_to_ft(250))
set_param_builtin_or_name(beam_type_b1, None, ["h", "Depth"], mm_to_ft(450))
beam_type_b2 = get_or_duplicate_symbol(beam_base_sym, "Sentry Beam B2 250x450 (M30)")
set_param_builtin_or_name(beam_type_b2, None, ["b", "Width"], mm_to_ft(250))
set_param_builtin_or_name(beam_type_b2, None, ["h", "Depth"], mm_to_ft(450))

# B1 spans A-B (X, 3650 c/c) on grids 1 and 2 ; B2 spans 1-2 (Z, 4650 c/c) on grids A and B
beam_defs = [
    ("B1 @ Grid 1", beam_type_b1, (0.175, 0.175), (3.825, 0.175)),
    ("B1 @ Grid 2", beam_type_b1, (0.175, 4.825), (3.825, 4.825)),
    ("B2 @ Grid A", beam_type_b2, (0.175, 0.175), (0.175, 4.825)),
    ("B2 @ Grid B", beam_type_b2, (3.825, 0.175), (3.825, 4.825)),
]
for storey_mark, lvl in [("FF", lvl_ff), ("Roof", lvl_roof)]:
    for mark, btype, p0_local, p1_local in beam_defs:
        full_mark = "Beam " + mark + " " + storey_mark
        if full_mark in beam_marks:
            skipped.append(full_mark)
            continue
        p0 = sentry_point(*p0_local)
        p1 = sentry_point(*p1_local)
        curve = Line.CreateBound(
            XYZ(p0.X, p0.Y, lvl.Elevation),
            XYZ(p1.X, p1.Y, lvl.Elevation),
        )
        b = doc.Create.NewFamilyInstance(curve, btype, lvl, StructuralType.Beam)
        set_mark(b, full_mark)
        beam_marks.add(full_mark)
        created.append(full_mark)

# ------------------------------------------------------------- PLINTH -----
# PB 250 x 400 at +0.450, perimeter of the 4 columns. Modelled as a shallow
# structural wall band at GF level for simplicity; true plinth BEAMS (250
# wide x 400 deep) can be substituted with the beam family used above if you
# prefer a framing element here.
pb_corners_local = [(0.175, 0.175), (3.825, 0.175), (3.825, 4.825), (0.175, 4.825)]
pb_pts = [sentry_point(x, z) for x, z in pb_corners_local]
pb_marks = ["PB Plinth Beam " + s for s in ["A-1 to B-1", "B-1 to B-2", "B-2 to A-2", "A-2 to A-1"]]
for i in range(4):
    mark = pb_marks[i]
    if mark in wall_marks:
        skipped.append(mark)
        continue
    plinth_type = get_or_duplicate_wall_type("Structural Beam-as-Wall - Plinth PB 250x400 (M30)", 250)
    p0, p1 = pb_pts[i], pb_pts[(i + 1) % 4]
    curve = Line.CreateBound(XYZ(p0.X, p0.Y, 0.0), XYZ(p1.X, p1.Y, 0.0))
    w = Wall.Create(doc, curve, plinth_type.Id, lvl_gf.Id, mm_to_ft(400), 0.0, False, True)
    set_mark(w, mark)
    wall_marks.add(mark)
    created.append(mark)

# -------------------------------------------------------------- SLABS -----
# S1, 150 mm two-way, both floors, external footprint 4.000 x 5.000 local
# (centre at local 2.000, 2.500).
s1_center_local = (2.000, 2.500)
for storey_mark, lvl in [("First Floor", lvl_ff), ("Roof", lvl_roof)]:
    full_mark = "Slab S1 - " + storey_mark
    if full_mark in floor_marks:
        skipped.append(full_mark)
        continue
    slab_type = get_or_duplicate_floor_type("Slab - Sentry S1 150mm (M30)", 150)
    center = sentry_point(*s1_center_local)
    loop = rect_loop_local(center, 2.000, 2.500, lvl.Elevation)
    s = Floor.Create(doc, [loop], slab_type.Id, lvl.Id)
    mark_structural(s)
    set_mark(s, full_mark)
    floor_marks.add(full_mark)
    created.append(full_mark)

# ------------------------------------------------- GROUND-STOREY INFILL ---
# 200 mm RC ballistic panels, non-structural (STAAD: "carried by the beam...
# as a UDL"), all 4 faces, GF FFL (+0.450) to First Floor (+3.650).
infill_marks = ["Ground-storey ballistic infill " + s for s in ["A-1 to B-1", "B-1 to B-2", "B-2 to A-2", "A-2 to A-1"]]
for i in range(4):
    mark = infill_marks[i]
    if mark in wall_marks:
        skipped.append(mark)
        continue
    infill_type = get_or_duplicate_wall_type("Non-Bearing Wall - Sentry Ballistic Infill 200mm (M30)", 200)
    p0, p1 = pb_pts[i], pb_pts[(i + 1) % 4]
    curve = Line.CreateBound(XYZ(p0.X, p0.Y, 0.0), XYZ(p1.X, p1.Y, 0.0))
    w = Wall.Create(doc, curve, infill_type.Id, lvl_gf.Id, m_to_ft(3.200), 0.0, False, False)
    set_mark(w, mark)
    wall_marks.add(mark)
    created.append(mark)

TransactionManager.Instance.TransactionTaskDone()

OUT = (
    "Sentry post structural elements created:\n" + "\n".join(created) +
    "\n\nSkipped (already present):\n" + "\n".join(skipped) +
    ("\n\nWARNINGS:\n" + "\n".join(warnings) if warnings else "")
)
