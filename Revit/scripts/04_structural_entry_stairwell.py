"""
Dynamo Python Script node — RUN FOURTH, after 01-03.

Builds the covered entry stairwell: stepped RC raft, headwall, both side
walls, east wall, top-landing slab, the sloped flight waist slab, the
platform slab, and the raking roof (as 3 pieces: flat over the top landing,
sloped over the flight, flat starter piece over the platform).

SOURCE OF TRUTH  master/MASTER_PROJECT_STATE.md A.4.7, B.6 — cross-checked
                 against current/staad/Entry_Stairwell.std (1 m transverse
                 strip model; confirms wall span 2.650 c/c, roof span 1.750
                 c/c, floor/wall/roof all 250, M35).

STATUS  OUTSIDE the protective boundary, NOT blast rated, "expected to be
LOST in the design event" (Master B.6). This is deliberately the lowest-
fidelity structure in the Phase 1 model — see the two simplifications below,
both flagged, neither silently resolved:

SIMPLIFICATION 1 — side/head/east walls. The Master gives the GOVERNING
retained height (2.9 m, B.6) and the floor levels at each end, but not a
stepped/raking wall profile. All four perimeter walls are therefore drawn as
single straight vertical walls at one uniform height each (see the per-wall
comments for which levels were used and why), not as the true stepped
retaining profile visible in the Rev F sections
(current/cad/2_Side_Section_with_Stairs.dxf,
current/cad/5_Entry_Headhouse_Stair_Section.dxf). Refine from those DXFs in
the architecture phase.

SIMPLIFICATION 2 / C16 — the roof/platform junction is an OPEN CONFLICT in
the Master itself (A.4.7 says the roof "becomes the 500 headhouse roof" over
the platform; B.6, A.7.6 and F.2 design, load and register a 250 mm roof
there instead; QUICK_STATE ref C16, unresolved, needs the user's ruling).
This script follows B.6/A.7.6/F.2 (250 mm, matching current/staad/
Entry_Stairwell.std) and does NOT extend or reconcile it with the headhouse
roof built in script 03. Do not treat the small resulting gap/overlap as a
modelling error — it is the geometric expression of C16, left open on
purpose pending your ruling. C16 does NOT block the rest of the structural
model: every other element in this script (raft, walls, landing, flight,
platform) is fully determined by the Master independently of how C16 is
eventually resolved — see Revit/docs/02_QAQC_and_discrepancies.md.

ASSUMPTION [ASSUMED] — RAFT_TOP_OFFSET_M below. "Stepped RC raft 300 thk on
compacted fill" (A.4.7) has no stated founding level anywhere in the Master.
This script assumes the raft's TOP sits flush with the UNDERSIDE of the
250 mm slab it carries at each end (offset = 0.250 m, the slab thickness;
no additional gap between raft and slab). Edit RAFT_TOP_OFFSET_M if you have
a real founding level — it is the one place this assumption lives.

RERUN SAFETY — every element carries a unique Mark; re-running skips marks
already present on a Wall/Floor in the document.
"""
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from Autodesk.Revit.DB import (
    XYZ, Line, CurveLoop, Wall, WallType, WallKind, Floor, FloorType,
    Level, UnitUtils, UnitTypeId, FilteredElementCollector, BuiltInParameter,
    BuiltInCategory
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


def sloped_rect_loop(x0, z0, x1, z1, y0, y1):
    """4-corner planar quad, sloped in X (constant per Y), for the raking roof
    and the flight waist slab."""
    p1 = XYZ(m_to_ft(x0), m_to_ft(y0), m_to_ft(z0))
    p2 = XYZ(m_to_ft(x1), m_to_ft(y0), m_to_ft(z1))
    p3 = XYZ(m_to_ft(x1), m_to_ft(y1), m_to_ft(z1))
    p4 = XYZ(m_to_ft(x0), m_to_ft(y1), m_to_ft(z0))
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


created = []
skipped = []

TransactionManager.Instance.EnsureInTransaction(doc)

lvl_grade = get_level("07 Site Grade")
lvl_hh_floor = get_level("06 Headhouse Floor (T-O-Roof Slab)")
lvl_hh_soffit = get_level("08 Headhouse Roof Soffit")
lvl_hh_top = get_level("09 Headhouse Roof Top (Berm Crest)")

wall_marks = existing_marks(BuiltInCategory.OST_Walls)
floor_marks = existing_marks(BuiltInCategory.OST_Floors)

RAFT_TOP_OFFSET_M = 0.250  # [ASSUMED] -- slab thickness, see module docstring


def make_wall(mark, p0, p1, base_level, height_m):
    if mark in wall_marks:
        skipped.append(mark)
        return None
    wall_type = get_or_duplicate_wall_type("Structural Wall - CIP Concrete 250mm (M35) - Entry Stairwell", 250)
    curve = Line.CreateBound(
        XYZ(m_to_ft(p0[0]), m_to_ft(p0[1]), 0.0),
        XYZ(m_to_ft(p1[0]), m_to_ft(p1[1]), 0.0),
    )
    w = Wall.Create(doc, curve, wall_type.Id, base_level.Id, m_to_ft(height_m), 0.0, False, True)
    set_mark(w, mark)
    wall_marks.add(mark)
    created.append(mark)
    return w


def make_floor(mark, loop, floor_type, base_level):
    if mark in floor_marks:
        skipped.append(mark)
        return None
    f = Floor.Create(doc, [loop], floor_type.Id, base_level.Id)
    mark_structural(f)
    set_mark(f, mark)
    floor_marks.add(mark)
    created.append(mark)
    return f


# Side walls (both long walls): base = platform level -2.000, top = berm
# crest +0.900 -> height 2.900 m, exactly the GOVERNING retained height in
# B.6. See SIMPLIFICATION 1 above.
make_wall("Stairwell South Side Wall", (9.375, 5.875), (15.925, 5.875), lvl_hh_floor, 2.900)
make_wall("Stairwell North Side Wall", (9.375, 7.625), (15.925, 7.625), lvl_hh_floor, 2.900)

# Headwall: base site grade (top landing level 0.000), height 2.200 m
# (Master A.4.7: "roof soffit 2200 above the flight").
headwall = make_wall("Stairwell Headwall", (9.375, 5.875), (9.375, 7.625), lvl_grade, 2.200)
if headwall is not None:
    # Entry door opening, 1000 x 2100, centred on the headwall, sill at grade.
    op_pt1 = XYZ(m_to_ft(9.375), m_to_ft(6.400), 0.0)
    op_pt2 = XYZ(m_to_ft(9.375), m_to_ft(7.400), mm_to_ft(2100))
    doc.Create.NewOpening(headwall, op_pt1, op_pt2)
    created.append("Headwall entry door opening 1000x2100")

# East wall (at the platform, movement joint against the headhouse): base
# platform -2.000, height 2.400 m (top = headhouse roof soffit +0.400).
make_wall("Stairwell East Wall (movement joint to headhouse)", (15.925, 5.875), (15.925, 7.625), lvl_hh_floor, 2.400)

# --------------------------------------------------------- FLOOR SLABS ----
slab250 = get_or_duplicate_floor_type("Slab - Entry Stairwell 250mm (M35)", 250)

# Top landing, X 9500-11000, external Y 5750-7750, flat at 0.000
make_floor("Top Landing Slab", rect_loop_xy(9.500, 5.750, 11.000, 7.750, m_to_ft(0.000)), slab250, lvl_grade)

# Platform, X 14300-15800, external Y 5750-7750, flat at -2.000, 1500x1500 clear
make_floor("Platform Slab", rect_loop_xy(14.300, 5.750, 15.800, 7.750, m_to_ft(-2.000)), slab250, lvl_hh_floor)

# Flight waist, sloped, X 11000 (Z 0.000) to X 14300 (Z -2.000), full width.
# 12R @ 166.6667 over 11 goings x 300 = 3300 run, total rise 2.000 m --
# matches 0.000 (top landing) to -2.000 (platform) exactly.
make_floor(
    "Flight Waist Slab (sloped, 12R @ 166.6667-300)",
    sloped_rect_loop(11.000, 0.000, 14.300, -2.000, 5.750, 7.750),
    slab250, lvl_hh_floor,
)

# ------------------------------------------------------- RAKING ROOF ------
# 3 pieces: flat over the top landing, sloped over the flight (soffit 2.200
# above the flight, i.e. flight Z + 2.200), flat starter piece over the
# platform. See SIMPLIFICATION 2 / C16 above -- NOT reconciled with the
# headhouse roof.
make_floor(
    "Stairwell Roof over Top Landing (flat)",
    rect_loop_xy(9.250, 5.750, 11.000, 7.750, m_to_ft(2.200)),
    slab250, lvl_hh_floor,
)
make_floor(
    "Stairwell Roof over Flight (sloped, soffit +2.200 above flight)",
    sloped_rect_loop(11.000, 2.200, 14.300, 0.200, 5.750, 7.750),
    slab250, lvl_hh_floor,
)
make_floor(
    "Stairwell Roof over Platform (flat starter piece -- C16 NOT resolved)",
    rect_loop_xy(14.300, 5.750, 15.800, 7.750, m_to_ft(0.200)),
    slab250, lvl_hh_floor,
)

# ------------------------------------------------------------- RAFT -------
# Stepped RC raft, 300 mm, on compacted fill (Master A.4.7). Founding level
# ASSUMED via RAFT_TOP_OFFSET_M -- see module docstring.
raft300 = get_or_duplicate_floor_type("Slab - Entry Stairwell Raft 300mm", 300)

make_floor(
    "Raft under Top Landing [ASSUMED founding level]",
    rect_loop_xy(9.250, 5.750, 11.000, 7.750, m_to_ft(0.000 - RAFT_TOP_OFFSET_M)),
    raft300, lvl_grade,
)
make_floor(
    "Raft under Platform [ASSUMED founding level]",
    rect_loop_xy(14.300, 5.750, 16.050, 7.750, m_to_ft(-2.000 - RAFT_TOP_OFFSET_M)),
    raft300, lvl_hh_floor,
)

TransactionManager.Instance.TransactionTaskDone()

OUT = (
    "Entry stairwell structural elements created:\n" + "\n".join(created) +
    "\n\nSkipped (already present):\n" + "\n".join(skipped)
)
