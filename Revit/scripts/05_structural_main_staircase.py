"""
Dynamo Python Script node — RUN FIFTH, after 01-04.

Builds the main dog-leg staircase inside the Bay 7 shaft: three 200 mm waist
slabs (flights 1-3) and the two intermediate landings L1/L2 (200 mm each).
The arrival landing at -6.100 is NOT a separate element -- it is the mat
foundation top, already built by script 02 (Master B.5 compatibility note:
"the arrival landing at (-)6.100 IS the mat surface, no separate slab").

*** FROZEN GEOMETRY -- CLAUDE.md ***
"Main staircase: 24 risers, 170.8333 mm riser, 280 mm tread, 3 flights x 8,
total rise 4100 mm... Never change any of this unless the user explicitly
asks again in a new request." Every number below is copied from Master A.4.4
and B.5 unchanged. If you are editing this file to change the stair, stop --
that requires a new, explicit user instruction, not a Phase-2 convenience.

ROUTING, re-derived and cross-checked against A.4.4/B.5 (shown here so the
logic is auditable, not just the numbers):
  Flight 1 (in the "Flight A" bay, X 15300-16500): arrival (Y 1800, -6.100)
    rising to L1 (Y 3760, -4.7333). Rise 1.3667 = 8 x 170.8333 ; run 1.960 =
    7 x 280 (Y 3760 - Y 1800). Both check exactly.
  Flight 2 (in the "Flight B" bay, X 16700-17900): L1 (Y 3760, -4.7333)
    rising to L2 (Y 1800, -3.3667), i.e. doubling back in Y. Same rise/run
    checks.
  Flight 3 (in the "Flight A" bay again, STACKED above flight 1, same X
    15300-16500): L2 (Y 1800, -3.3667) rising to the shaft top (Y 3760,
    -2.000 = headhouse floor level, where the roof VOID Master A.4.4 gives as
    Y 600-3760 opens the shaft through the roof). Same rise/run checks.
  Total rise 3 x 1.3667 = 4.100 = -6.100 to -2.000. Matches A.2's stated
  arrival-to-headhouse-floor stair run exactly.

NOT MODELLED (flagged, not silently dropped) — the free-edge roof
thickening 900 -> 1200 mm over a 600 mm band at the void's Y 3760 boundary,
and the diagonal corner trimmers, both from Master B.4.1(b). These are local
refinements to the uniform 900 mm roof slab script 02 already built; carry
them into the QA/QC list, do not add them here without re-touching script 02.
"""
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from Autodesk.Revit.DB import (
    XYZ, Line, CurveLoop, Floor, FloorType, Level,
    UnitUtils, UnitTypeId, FilteredElementCollector, BuiltInParameter
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


def sloped_rect_loop_y(x0, x1, y0, z0, y1, z1):
    """4-corner planar quad, sloped in Y (constant per X) -- for a flight."""
    p1 = XYZ(m_to_ft(x0), m_to_ft(y0), m_to_ft(z0))
    p2 = XYZ(m_to_ft(x1), m_to_ft(y0), m_to_ft(z0))
    p3 = XYZ(m_to_ft(x1), m_to_ft(y1), m_to_ft(z1))
    p4 = XYZ(m_to_ft(x0), m_to_ft(y1), m_to_ft(z1))
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

lvl_floor = get_level("02 Shelter Floor (Internal-T-O-Mat)")

waist200 = get_or_duplicate_floor_type("Slab - Main Stair Waist 200mm (M35)", 200)
landing200 = get_or_duplicate_floor_type("Slab - Main Stair Landing 200mm (M35)", 200)

# Flight 1 -- arrival (Y1.800, -6.100) to L1 (Y3.760, -4.7333)
f1_loop = sloped_rect_loop_y(15.300, 16.500, 1.800, -6.100, 3.760, -4.7333)
f1 = Floor.Create(doc, [f1_loop], waist200.Id, lvl_floor.Id)
mark_structural(f1)
created.append("Flight 1 waist slab (arrival to L1)")

# Flight 2 -- L1 (Y3.760, -4.7333) to L2 (Y1.800, -3.3667), doubles back
f2_loop = sloped_rect_loop_y(16.700, 17.900, 3.760, -4.7333, 1.800, -3.3667)
f2 = Floor.Create(doc, [f2_loop], waist200.Id, lvl_floor.Id)
mark_structural(f2)
created.append("Flight 2 waist slab (L1 to L2)")

# Flight 3 -- L2 (Y1.800, -3.3667) to shaft top (Y3.760, -2.000), stacked
# over flight 1's plan footprint
f3_loop = sloped_rect_loop_y(15.300, 16.500, 1.800, -3.3667, 3.760, -2.000)
f3 = Floor.Create(doc, [f3_loop], waist200.Id, lvl_floor.Id)
mark_structural(f3)
created.append("Flight 3 waist slab (L2 to shaft top)")

# Landing L1, full shaft width, Y 3760-4960, flat at -4.7333
l1_loop = rect_loop_xy(15.200, 3.760, 18.000, 4.960, m_to_ft(-4.7333))
l1 = Floor.Create(doc, [l1_loop], landing200.Id, lvl_floor.Id)
mark_structural(l1)
created.append("Landing L1")

# Landing L2, full shaft width, Y 600-1800, flat at -3.3667
l2_loop = rect_loop_xy(15.200, 0.600, 18.000, 1.800, m_to_ft(-3.3667))
l2 = Floor.Create(doc, [l2_loop], landing200.Id, lvl_floor.Id)
mark_structural(l2)
created.append("Landing L2")

TransactionManager.Instance.TransactionTaskDone()

OUT = "Main staircase elements created (FROZEN geometry, unchanged from Master):\n" + "\n".join(created)
