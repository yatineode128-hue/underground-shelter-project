"""
Dynamo Python Script node — RUN THIRD, after 01 and 02.

Builds the entry headhouse: walls HW1-HW4 (400 mm) and the headhouse roof
(500 mm), plus the inner security door opening in HW2. The headhouse floor is
the top of the main box roof slab already built by script 02 — no separate
floor element is created here (Master A.4.6: "Floor = the top of the 900
pressure slab, (-)2.000").

SOURCE OF TRUTH  master/MASTER_PROJECT_STATE.md A.4.6, B.7.1, B.7.2, B.7.3

NOTE — HW3 (west) bears on the mid-span of the box roof slab over Bay 6, not
on a wall (Master A.4.6, "NO wall below — line load on the pressure slab,
checked at 26% / 41%"). That is a load-path finding, not a drawing
difference: HW3 is still drawn as a normal 400 mm wall sitting on the roof
slab built in script 02, exactly like HW1/HW2/HW4. HW4 aligns exactly with
box wall W7's centreline (X 18.200) — Master A.4.6 states M1 made this
alignment exact; this script places HW4 at the same X and the coincidence is
a check, not a coding choice.
"""
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from Autodesk.Revit.DB import (
    XYZ, Line, CurveLoop, Wall, WallType, WallKind, Floor, FloorType,
    Level, UnitUtils, UnitTypeId, FilteredElementCollector, BuiltInParameter
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


def mark_structural(elem):
    p = elem.get_Parameter(BuiltInParameter.FLOOR_PARAM_IS_STRUCTURAL)
    if p and not p.IsReadOnly:
        p.Set(1)


created = []

TransactionManager.Instance.EnsureInTransaction(doc)

lvl_hh_floor = get_level("06 Headhouse Floor (T-O-Roof Slab)")
lvl_hh_soffit = get_level("08 Headhouse Roof Soffit")
lvl_hh_top = get_level("09 Headhouse Roof Top (Berm Crest)")

# ---------------------------------------------------------- HH WALLS ------
# 400 mm, M35. External 4800 x 5800 (X 13600-18400, Y 200-6000); internal
# 4000 x 5000 (X 14000-18000, Y 600-5600) -> centrelines X 13.800/18.200,
# Y 0.400/5.800 (Master A.4.6).
hh_wall_type = get_or_duplicate_wall_type("Structural Wall - CIP Concrete 400mm (M35) - Headhouse", 400)
wall_height = m_to_ft(2.400)

hh_segments = {
    "HW1 - Headhouse South Wall": ((13.800, 0.400), (18.200, 0.400)),
    "HW2 - Headhouse North Wall": ((13.800, 5.800), (18.200, 5.800)),
    "HW3 - Headhouse West Wall":  ((13.800, 0.400), (13.800, 5.800)),
    "HW4 - Headhouse East Wall":  ((18.200, 0.400), (18.200, 5.800)),
}
walls_by_mark = {}
for mark, (p0, p1) in hh_segments.items():
    curve = Line.CreateBound(
        XYZ(m_to_ft(p0[0]), m_to_ft(p0[1]), 0.0),
        XYZ(m_to_ft(p1[0]), m_to_ft(p1[1]), 0.0),
    )
    w = Wall.Create(doc, curve, hh_wall_type.Id, lvl_hh_floor.Id, wall_height, 0.0, False, True)
    w.get_Parameter(BuiltInParameter.ALL_MODEL_MARK).Set(mark)
    walls_by_mark[mark] = w
    created.append(mark)

# Inner security door opening, 900 x 2100, in HW2 at X 14450-15350, NOT blast
# rated (Master A.4.6). Sill at headhouse floor -2.000.
hw2 = walls_by_mark["HW2 - Headhouse North Wall"]
op_pt1 = XYZ(m_to_ft(14.450), m_to_ft(5.800), m_to_ft(-2.000))
op_pt2 = XYZ(m_to_ft(15.350), m_to_ft(5.800), m_to_ft(-2.000) + mm_to_ft(2100))
doc.Create.NewOpening(hw2, op_pt1, op_pt2)
created.append("HW2 inner security door opening 900x2100")

# ---------------------------------------------------------- HH ROOF -------
# 500 mm M35, external footprint 4800 x 5800 (bears on wall tops), top at
# +0.900 (berm crest), bottom at +0.400 (soffit). No openings (Master A.4.6).
hh_roof_type = get_or_duplicate_floor_type("Slab - Headhouse Roof 500mm (M35)", 500)
z_hh_roof_top = m_to_ft(0.900)
hh_roof_loop = rect_loop(13.600, 0.200, 18.400, 6.000, z_hh_roof_top)
hh_roof = Floor.Create(doc, [hh_roof_loop], hh_roof_type.Id, lvl_hh_top.Id)
mark_structural(hh_roof)
created.append("Headhouse roof slab")

TransactionManager.Instance.TransactionTaskDone()

OUT = "Headhouse structural elements created:\n" + "\n".join(created)
