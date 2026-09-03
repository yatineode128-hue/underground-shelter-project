"""
Dynamo Python Script node — RUN SECOND, after 01_levels_and_grids.py.

Builds the main underground box structural envelope: PCC blinding, mat
foundation, the four perimeter walls (W1-W4), internal walls W5/W6/W7 (with
the two blast-door openings), and the roof (pressure) slab with its three
openings (the stair-shaft void and the two escape-shaft circles).

SOURCE OF TRUTH  master/MASTER_PROJECT_STATE.md A.4.2, A.4.3, A.4.4, A.4.5,
                 B.1, B.2, B.3, B.4, B.4.1 — cross-checked against
                 current/staad/Underground_Structure_WITH_LOADS_worked_example (4).STD
                 element groups _MAT_600, _ROOF_900, _WALL_EXT_600,
                 _WALL_INT_200, _WALL_W6_W7_400 and their THICKNESS lines.

REAL FOOTPRINT NOTE — the STAAD model above is a mid-surface plate model
(mat/roof plates run wall-centreline to wall-centreline, 119.84 sq m). This
script builds REAL geometry instead: mat and roof slab both span the full
22.000 x 6.200 external footprint (confirmed by the STAAD file's own comment,
"the REAL 22.000 x 6.200 = 136.40 m2 underside, not ... the mid-surface area
of 119.84 m2"), and walls sit on/under them at their true centrelines.

MATERIALS — Phase 1 assigns each type a placeholder Concrete material tagged
with its grade in the type name (e.g. "M35"). Physical/appearance material
properties are a later-stage task (see Revit/docs/00_README_WORKFLOW.md) and
are not authored here; do not read a grade in a type NAME as a verified
material definition.

REINFORCEMENT IS NOT MODELLED IN THIS SCRIPT — see B.1-B.4 for the bar
schedule; native Revit rebar is deferred to a later phase.
"""
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from Autodesk.Revit.DB import (
    XYZ, Line, Arc, CurveLoop, Wall, WallType, WallKind, Floor, FloorType,
    Level, UnitUtils, UnitTypeId, FilteredElementCollector, BuiltInParameter,
    StructuralType
)
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

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


def rect_loop(x0, y0, x1, y1, z_ft):
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


def circle_loop(cx, cy, dia_mm, z_ft):
    r = mm_to_ft(dia_mm) / 2.0
    c = XYZ(m_to_ft(cx), m_to_ft(cy), z_ft)
    p0 = c + XYZ(r, 0, 0)
    p1 = c + XYZ(-r, 0, 0)
    arc1 = Arc.Create(p0, p1, c + XYZ(0, r, 0))
    arc2 = Arc.Create(p1, p0, c + XYZ(0, -r, 0))
    loop = CurveLoop()
    loop.Append(arc1)
    loop.Append(arc2)
    return loop


def mark_structural(elem):
    p = elem.get_Parameter(BuiltInParameter.FLOOR_PARAM_IS_STRUCTURAL)
    if p and not p.IsReadOnly:
        p.Set(1)


created = []

TransactionManager.Instance.EnsureInTransaction(doc)

lvl_mat_top = get_level("02 Shelter Floor (Internal-T-O-Mat)")
lvl_us_mat = get_level("01 US Mat")
lvl_roof_top = get_level("06 Headhouse Floor (T-O-Roof Slab)")
lvl_roof_soffit = get_level("05 Roof Soffit")

# ------------------------------------------------------- PCC BLINDING -----
# 100 mm M15, real footprint assumed = mat footprint (extent beyond the mat
# edge is not stated in the Master) [ASSUMED — flagged in the Phase 1 report]
pcc_type = get_or_duplicate_floor_type("Slab - PCC Blinding 100mm (M15)", 100)
pcc_loop = rect_loop(0.0, 0.0, 22.000, 6.200, m_to_ft(-6.700))
pcc = Floor.Create(doc, [pcc_loop], pcc_type.Id, lvl_us_mat.Id)
mark_structural(pcc)
created.append("PCC blinding floor")

# ------------------------------------------------------------ MAT ---------
# 600 mm M35, real footprint 22.000 x 6.200 (Master B.3; "REAL 22.000 x 6.200
# = 136.40 m2 underside" per the STAAD file's own comment)
mat_type = get_or_duplicate_floor_type("Slab - Mat Foundation 600mm (M35)", 600)
mat_loop = rect_loop(0.0, 0.0, 22.000, 6.200, m_to_ft(-6.100))
mat = Floor.Create(doc, [mat_loop], mat_type.Id, lvl_mat_top.Id)
mark_structural(mat)
created.append("Mat foundation floor")

# ------------------------------------------------------ PERIMETER WALLS ---
# W1-W4, 600 mm thick, M35. Base = Shelter Floor (-6.100), height = 3.200 m
# to Roof Soffit (-2.900). Centrelines at wall-centreline X 0.300/21.700,
# Y 0.300/5.900 (Master A.4.2 external 22.000x6.200, internal 20800x5000).
perim_type = get_or_duplicate_wall_type("Structural Wall - CIP Concrete 600mm (M35)", 600)
wall_height = m_to_ft(3.200)

perimeter_segments = {
    "W1 - South Perimeter Wall": ((0.300, 0.300), (21.700, 0.300)),
    "W2 - North Perimeter Wall": ((0.300, 5.900), (21.700, 5.900)),
    "W3 - West Perimeter Wall":  ((0.300, 0.300), (0.300, 5.900)),
    "W4 - East Perimeter Wall":  ((21.700, 0.300), (21.700, 5.900)),
}
for mark, (p0, p1) in perimeter_segments.items():
    curve = Line.CreateBound(
        XYZ(m_to_ft(p0[0]), m_to_ft(p0[1]), 0.0),
        XYZ(m_to_ft(p1[0]), m_to_ft(p1[1]), 0.0),
    )
    w = Wall.Create(doc, curve, perim_type.Id, lvl_mat_top.Id, wall_height, 0.0, False, True)
    w.get_Parameter(BuiltInParameter.ALL_MODEL_MARK).Set(mark)
    created.append(mark)

# ------------------------------------------------------------- W5 ---------
# 200 mm, Bay 5/6 fire+gas seal only, no blast rating, no opening.
w5_type = get_or_duplicate_wall_type("Structural Wall - CIP Concrete 200mm (M35) - W5", 200)
curve = Line.CreateBound(
    XYZ(m_to_ft(12.700), m_to_ft(0.600), 0.0),
    XYZ(m_to_ft(12.700), m_to_ft(5.600), 0.0),
)
w5 = Wall.Create(doc, curve, w5_type.Id, lvl_mat_top.Id, wall_height, 0.0, False, True)
w5.get_Parameter(BuiltInParameter.ALL_MODEL_MARK).Set("W5 - Bay 5-6 Divider")
created.append("W5")

# ------------------------------------------------------- W6 / W7 ----------
# 400 mm (MOD M1), M35, protective boundary. Each carries a 1200 x 2100
# blast-door opening at Y 600-1800 (Master A.3, QUICK_STATE, B.2).
w67_type = get_or_duplicate_wall_type("Structural Wall - CIP Concrete 400mm (M35) - W6-W7", 400)

w67_segments = {
    "W6 - Blast Boundary (Bay 6-7)": 15.000,
    "W7 - Blast Boundary (Bay 7-8)": 18.200,
}
for mark, x in w67_segments.items():
    curve = Line.CreateBound(
        XYZ(m_to_ft(x), m_to_ft(0.600), 0.0),
        XYZ(m_to_ft(x), m_to_ft(5.600), 0.0),
    )
    w = Wall.Create(doc, curve, w67_type.Id, lvl_mat_top.Id, wall_height, 0.0, False, True)
    w.get_Parameter(BuiltInParameter.ALL_MODEL_MARK).Set(mark)
    created.append(mark)
    # Blast door opening: 1200 (Y 0.600-1.800) x 2100 high from floor (-6.100)
    op_pt1 = XYZ(m_to_ft(x), m_to_ft(0.600), m_to_ft(-6.100))
    op_pt2 = XYZ(m_to_ft(x), m_to_ft(1.800), m_to_ft(-4.000))
    doc.Create.NewOpening(w, op_pt1, op_pt2)
    created.append(mark + " blast-door opening 1200x2100")

# --------------------------------------------------------- ROOF SLAB ------
# 900 mm M35, real footprint 22.000 x 6.200, top at -2.000 (T/roof slab),
# bottom at -2.900 (roof soffit). Three openings: the stair-shaft void
# (2800 x 3160, X 15.200-18.000 / Y 0.600-3.760) and two 1400 dia escape
# shafts at (2.050, 2.050) and (19.900, 2.050) [M1: ESC2 shifted to 19.900].
roof_type = get_or_duplicate_floor_type("Slab - Roof (Pressure) Slab 900mm (M35)", 900)
z_roof_top = m_to_ft(-2.000)

outer = rect_loop(0.0, 0.0, 22.000, 6.200, z_roof_top)
stair_void = rect_loop(15.200, 0.600, 18.000, 3.760, z_roof_top)
esc1 = circle_loop(2.050, 2.050, 1400, z_roof_top)
esc2 = circle_loop(19.900, 2.050, 1400, z_roof_top)

roof = Floor.Create(doc, [outer, stair_void, esc1, esc2], roof_type.Id, lvl_roof_top.Id)
mark_structural(roof)
created.append("Roof slab with stair-void + 2 escape-shaft openings")

TransactionManager.Instance.TransactionTaskDone()

OUT = "Main box structural elements created:\n" + "\n".join(created)
