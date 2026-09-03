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
purpose pending your ruling. Raise C16 before Phase 2 closes it either way.
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


created = []

TransactionManager.Instance.EnsureInTransaction(doc)

lvl_grade = get_level("07 Site Grade")
lvl_hh_floor = get_level("06 Headhouse Floor (T-O-Roof Slab)")
lvl_hh_soffit = get_level("08 Headhouse Roof Soffit")
lvl_hh_top = get_level("09 Headhouse Roof Top (Berm Crest)")

wall_type = get_or_duplicate_wall_type("Structural Wall - CIP Concrete 250mm (M35) - Entry Stairwell", 250)

# Side walls (both long walls): base = platform level -2.000, top = berm
# crest +0.900 -> height 2.900 m, exactly the GOVERNING retained height in
# B.6. See SIMPLIFICATION 1 above.
side_h = m_to_ft(2.900)
for mark, y in [("Stairwell South Side Wall", 5.875), ("Stairwell North Side Wall", 7.625)]:
    curve = Line.CreateBound(
        XYZ(m_to_ft(9.375), m_to_ft(y), 0.0),
        XYZ(m_to_ft(15.925), m_to_ft(y), 0.0),
    )
    w = Wall.Create(doc, curve, wall_type.Id, lvl_hh_floor.Id, side_h, 0.0, False, True)
    w.get_Parameter(BuiltInParameter.ALL_MODEL_MARK).Set(mark)
    created.append(mark)

# Headwall: base site grade (top landing level 0.000), height 2.200 m
# (Master A.4.7: "roof soffit 2200 above the flight").
curve = Line.CreateBound(
    XYZ(m_to_ft(9.375), m_to_ft(5.875), 0.0),
    XYZ(m_to_ft(9.375), m_to_ft(7.625), 0.0),
)
headwall = Wall.Create(doc, curve, wall_type.Id, lvl_grade.Id, m_to_ft(2.200), 0.0, False, True)
headwall.get_Parameter(BuiltInParameter.ALL_MODEL_MARK).Set("Stairwell Headwall")
created.append("Stairwell Headwall")
# Entry door opening, 1000 x 2100, centred on the headwall, sill at grade.
op_pt1 = XYZ(m_to_ft(9.375), m_to_ft(6.400), 0.0)
op_pt2 = XYZ(m_to_ft(9.375), m_to_ft(7.400), mm_to_ft(2100))
doc.Create.NewOpening(headwall, op_pt1, op_pt2)
created.append("Headwall entry door opening 1000x2100")

# East wall (at the platform, movement joint against the headhouse): base
# platform -2.000, height 2.400 m (top = headhouse roof soffit +0.400).
curve = Line.CreateBound(
    XYZ(m_to_ft(15.925), m_to_ft(5.875), 0.0),
    XYZ(m_to_ft(15.925), m_to_ft(7.625), 0.0),
)
eastwall = Wall.Create(doc, curve, wall_type.Id, lvl_hh_floor.Id, m_to_ft(2.400), 0.0, False, True)
eastwall.get_Parameter(BuiltInParameter.ALL_MODEL_MARK).Set("Stairwell East Wall (movement joint to headhouse)")
created.append("Stairwell East Wall")

# --------------------------------------------------------- FLOOR SLABS ----
slab250 = get_or_duplicate_floor_type("Slab - Entry Stairwell 250mm (M35)", 250)

# Top landing, X 9500-11000, external Y 5750-7750, flat at 0.000
top_landing_loop = rect_loop_xy(9.500, 5.750, 11.000, 7.750, m_to_ft(0.000))
top_landing = Floor.Create(doc, [top_landing_loop], slab250.Id, lvl_grade.Id)
mark_structural(top_landing)
created.append("Top landing slab")

# Platform, X 14300-15800, external Y 5750-7750, flat at -2.000, 1500x1500 clear
platform_loop = rect_loop_xy(14.300, 5.750, 15.800, 7.750, m_to_ft(-2.000))
platform = Floor.Create(doc, [platform_loop], slab250.Id, lvl_hh_floor.Id)
mark_structural(platform)
created.append("Platform slab")

# Flight waist, sloped, X 11000 (Z 0.000) to X 14300 (Z -2.000), full width.
# 12R @ 166.6667 over 11 goings x 300 = 3300 run, total rise 2.000 m --
# matches 0.000 (top landing) to -2.000 (platform) exactly.
flight_loop = sloped_rect_loop(11.000, 0.000, 14.300, -2.000, 5.750, 7.750)
flight = Floor.Create(doc, [flight_loop], slab250.Id, lvl_hh_floor.Id)
mark_structural(flight)
created.append("Flight waist slab (sloped, 12R @ 166.6667/300)")

# ------------------------------------------------------- RAKING ROOF ------
# 3 pieces: flat over the top landing, sloped over the flight (soffit 2.200
# above the flight, i.e. flight Z + 2.200), flat starter piece over the
# platform. See SIMPLIFICATION 2 / C16 above -- NOT reconciled with the
# headhouse roof.
roof_top_landing_loop = rect_loop_xy(9.250, 5.750, 11.000, 7.750, m_to_ft(2.200))
roof_top_landing = Floor.Create(doc, [roof_top_landing_loop], slab250.Id, lvl_hh_floor.Id)
mark_structural(roof_top_landing)
created.append("Stairwell roof over top landing (flat)")

roof_flight_loop = sloped_rect_loop(11.000, 2.200, 14.300, 0.200, 5.750, 7.750)
roof_flight = Floor.Create(doc, [roof_flight_loop], slab250.Id, lvl_hh_floor.Id)
mark_structural(roof_flight)
created.append("Stairwell roof over flight (sloped, soffit +2.200 above flight)")

roof_platform_loop = rect_loop_xy(14.300, 5.750, 15.800, 7.750, m_to_ft(0.200))
roof_platform = Floor.Create(doc, [roof_platform_loop], slab250.Id, lvl_hh_floor.Id)
mark_structural(roof_platform)
created.append("Stairwell roof over platform (flat starter piece -- C16 NOT resolved)")

# ------------------------------------------------------------- RAFT -------
# Stepped RC raft, 300 mm, on compacted fill (Master A.4.7). Founding level
# is NOT stated in the Master beyond "on compacted fill"; this script
# ASSUMES the raft top sits 300 mm below the underside of the slab it
# carries at each end -- flag before relying on it for real bearing design.
raft300 = get_or_duplicate_floor_type("Slab - Entry Stairwell Raft 300mm", 300)

raft_top_landing_loop = rect_loop_xy(9.250, 5.750, 11.000, 7.750, m_to_ft(-0.250))
raft_top_landing = Floor.Create(doc, [raft_top_landing_loop], raft300.Id, lvl_grade.Id)
mark_structural(raft_top_landing)
created.append("Raft under top landing [ASSUMED founding level]")

raft_platform_loop = rect_loop_xy(14.300, 5.750, 16.050, 7.750, m_to_ft(-2.250))
raft_platform = Floor.Create(doc, [raft_platform_loop], raft300.Id, lvl_hh_floor.Id)
mark_structural(raft_platform)
created.append("Raft under platform [ASSUMED founding level]")

TransactionManager.Instance.TransactionTaskDone()

OUT = "Entry stairwell structural elements created:\n" + "\n".join(created)
