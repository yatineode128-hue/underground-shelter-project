"""
Dynamo Python Script node — DRAINAGE.  RUN AFTER 01 to 06.

Adds the drainage elements of package DR1 to the EXISTING Revit model that
`Revit/scripts/01_levels_and_grids.py` … `06_structural_sentry_post.py` build.

IT DOES NOT CREATE A PROJECT, A LEVEL, A GRID, A ROOM OR ANY STRUCTURE.
It reads the levels those scripts already made and adds drainage on top of
them.  There is exactly one Revit model in this project and this script
extends it.

SOURCE OF TRUTH  Drainage/Scripts/mep_proj.py and Drainage/Scripts/dr_data.py,
                 which come from master/MASTER_PROJECT_STATE.md and sheet S-06.
                 The tables below are transcribed from those two files; if they
                 ever disagree, the Python source in Scripts/ governs.

COORDINATE MAP   identical to scripts 01-06:
                 master X (east, 0-22000)  -> Revit X
                 master Y (north, 0-6200)  -> Revit Y
                 master LEVELS (grade 0.000) -> Revit Z

SENTRY POST      OUT OF SCOPE.  No sentry post element appears in this script.
MAIN STAIRCASE   FROZEN.  Nothing here touches it.

RERUN SAFETY     every element carries a unique Mark.  Before creating
                 anything the script reads the Marks already present and skips
                 any that exist, so a second run does not duplicate geometry.
                 Same guard pattern as scripts 02-06.

WHAT CAN AND CANNOT BE AUTOMATED
    CAN     pipe runs (Plumbing MEP curves or, if the template has no MEP
            system families loaded, model lines on a drainage subcategory),
            sump and tank volumes as generic-model extrusions, gully and
            chamber locations as reference points with Marks, and a set of
            shared parameters carrying invert level, gradient, bore and
            evidence class.
    CANNOT  automatically create the sump PIT as a structural void in the mat —
            the mat is a Floor created by script 02 and cutting a 1500 x 1500 x
            1500 recess into it is a structural change (builder's work BW-01
            and the C18 base-thickness question are both open).  THE PIT IS
            MODELLED AS A SEPARATE GENERIC MODEL SOLID SITTING IN THE MAT
            FOOTPRINT, NOT AS A CUT.  Cutting it is a manual step, listed at
            the end, and must wait for the structural ruling.

*** REVIT IS NOT EXECUTABLE IN THE ENVIRONMENT THIS SCRIPT WAS WRITTEN IN.
    THE SCRIPT HAS BEEN WRITTEN AND REVIEWED BUT HAS NOT BEEN RUN.  Treat the
    first run as a commissioning exercise, on a copy. ***
"""
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from Autodesk.Revit.DB import (
    XYZ, Line, Level, UnitUtils, UnitTypeId, FilteredElementCollector,
    BuiltInParameter, BuiltInCategory, Transform, DirectShape,
    ElementId, Solid, GeometryCreationUtilities, CurveLoop, Frame,
    SolidOptions, ModelCurve, SketchPlane, Plane
)
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

PACKAGE = "DR1"
PREFIX = "DR-"                     # every Mark this script writes starts here


# ------------------------------------------------------------------ units
def mm(v):
    return UnitUtils.ConvertToInternalUnits(v, UnitTypeId.Millimeters)


def m(v):
    return UnitUtils.ConvertToInternalUnits(v, UnitTypeId.Meters)


def get_level(name):
    for l in FilteredElementCollector(doc).OfClass(Level):
        if l.Name == name:
            return l
    raise Exception("Level not found - run 01_levels_and_grids.py first: "
                    + name)


def existing_marks():
    """Marks already on real elements, so a re-run skips finished work."""
    out = set()
    for bic in (BuiltInCategory.OST_GenericModel,
                BuiltInCategory.OST_PipeCurves,
                BuiltInCategory.OST_Lines,
                BuiltInCategory.OST_MechanicalEquipment):
        for e in FilteredElementCollector(doc).OfCategory(bic)\
                .WhereElementIsNotElementType():
            p = e.get_Parameter(BuiltInParameter.ALL_MODEL_MARK)
            if p and p.AsString():
                out.add(p.AsString())
    return out


# ------------------------------------------------------- the drainage data
# tag, x, y, level(m), description, evidence class
GULLIES = [
    ("GY-01", 2050, 3100, -6.100, "Trapped floor gully DN100, 75 deep seal", "A"),
    ("GY-02", 4510, 3100, -6.100, "Trapped floor gully DN100, lavatory", "A"),
    ("GY-03", 7270, 3100, -6.100, "Trapped floor gully DN100, ops room", "A"),
    ("GY-04", 10030, 3100, -6.100, "Trapped floor gully DN100, berthing", "A"),
    ("GY-05", 11820, 2600, -6.100, "Open fall to the sump, CBRN plant", "A"),
    ("GY-06", 13800, 4600, -6.100, "SEGREGATED gully, decon stage 1", "A"),
    ("GY-07", 13800, 2850, -6.100, "SEGREGATED gully, decon stage 2", "A"),
    ("GY-08", 13800, 1350, -6.100, "SEGREGATED gully, decon stage 3", "A"),
    ("GY-09", 19900, 3100, -6.100, "Generator bay - NO DESTINATION DEFINED", "U"),
    ("GY-10", 15050, 6750, -2.000, "Platform gully, entry stairwell", "C"),
    ("GY-11", 14700, 1960, -2.000, "Headhouse gully, fall 1:80", "C"),
]

# tag, x0, y0, x1, y1, top(m), bottom(m), description, class
VOLUMES = [
    ("SU-01", 11068, 900, 12568, 2400, -6.100, -7.600,
     "Clean sump 1500x1500x1500 = 3.375 m3", "C"),
    ("TK-01", 20198, 4400, 21398, 5600, -5.400, -6.100,
     "Decon effluent tank 1000 L - TANKER ONLY", "C"),
    ("PLATE", 11398, 5600, 12198, 6200, -3.000, -3.800,
     "Service entry plate - the ONLY envelope penetration", "C"),
]

# tag, [(x, y, level_m), ...], bore, gradient, description, class
RUNS = [
    ("PD-01", [(4510, 3100, -6.250), (11068, 3100, -6.316)], 100, "1:100",
     "Lavatory waste to the clean sump - BUILDER'S WORK BW-01, NOT ACCEPTED", "A"),
    ("PD-03", [(13800, 4600, -6.250), (13800, 3100, -6.275),
               (14500, 3100, -6.290)], 100, "1:100",
     "SEGREGATED decon effluent to CP-01", "A"),
    ("PD-05", [(11818, 1650, -7.300), (11818, 5600, -3.400)], 50, "PUMPED",
     "Rising main to the service entry plate", "C"),
    ("PD-12", [(15050, 6750, -2.150), (15500, 6400, -2.169)], 100, "1:80",
     "Platform gully to the stairwell sump", "C"),
    ("PD-14", [(14700, 1960, -2.150), (13000, 1300, -2.171)], 100, "1:80",
     "Headhouse gully to the EXTERNAL soakaway - never to the clean sump", "C"),
]

MANUAL_STEPS = [
    "1  CUT THE SUMP PIT INTO THE MAT.  SU-01 is modelled as a solid in the "
    "mat footprint, NOT as a void.  Cutting a 1500 x 1500 x 1500 recess into "
    "the 600 mat is a structural change and both BW-01 and C18 are open.  Do "
    "it by hand only after the structural ruling, with Modify > Cut.",
    "2  CUT THE PD-01 RECESS.  300 wide, 150 deep at GY-02 rising to 216 at "
    "the sump.  Same reason - BW-01 is REQUESTED, NOT ACCEPTED.",
    "3  SERVICE ENTRY PLATE OPENING.  The plate is modelled as a solid inside "
    "the north wall; the actual opening through the 600 wall is a Wall Opening "
    "and is a protective-design item, not a drainage one.",
    "4  ASSIGN MEP SYSTEMS.  If the template has Plumbing families loaded, "
    "replace the model curves with Pipes and set the Piping System to the "
    "matching system type (Sanitary / Storm / Other).  The script writes the "
    "system name into Comments so the mapping is unambiguous.",
    "5  EXTERNAL WORKS.  The septic tank ST-01, the soak pit SK-01, the storm "
    "soakaway SK-02, the stairwell soakaway SK-03 and the headhouse soakaway "
    "SK-04 are NOT modelled: no site plan, boundary or contour exists anywhere "
    "in the project (open item D3), so they cannot be positioned.",
    "6  ROUTE PD-04, decon effluent from bay 6 to TK-01 in bay 8, is NOT "
    "modelled.  It crosses the protective boundary at W6 and W7 and no route "
    "exists in the project.  It is a protective-design decision (DR-D4, DR-F5).",
]


# --------------------------------------------------------------- geometry
def box_solid(x0, y0, x1, y1, z_top, z_bot):
    pts = [XYZ(mm(x0), mm(y0), m(z_bot)), XYZ(mm(x1), mm(y0), m(z_bot)),
           XYZ(mm(x1), mm(y1), m(z_bot)), XYZ(mm(x0), mm(y1), m(z_bot))]
    loop = CurveLoop()
    for i in range(4):
        loop.Append(Line.CreateBound(pts[i], pts[(i + 1) % 4]))
    return GeometryCreationUtilities.CreateExtrusionGeometry(
        [loop], XYZ.BasisZ, m(z_top - z_bot))


def set_mark(el, mark, comment):
    p = el.get_Parameter(BuiltInParameter.ALL_MODEL_MARK)
    if p:
        p.Set(mark)
    c = el.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)
    if c:
        c.Set(comment)


# ------------------------------------------------------------------ build
made, skipped = [], []
have = existing_marks()

TransactionManager.Instance.EnsureInTransaction(doc)

# --- volumes: sump, tanks, service entry plate
for tag, x0, y0, x1, y1, ztop, zbot, desc, cls in VOLUMES:
    mark = PREFIX + tag
    if mark in have:
        skipped.append(mark)
        continue
    ds = DirectShape.CreateElement(
        doc, ElementId(int(BuiltInCategory.OST_GenericModel)))
    ds.ApplicationId = "DrainageDR1"
    ds.ApplicationDataId = tag
    ds.SetShape([box_solid(x0, y0, x1, y1, ztop, zbot)])
    set_mark(ds, mark, "[%s] %s  (package %s)" % (cls, desc, PACKAGE))
    made.append(mark)

# --- gullies: a small marker solid each, so the tag is selectable in 3D
for tag, x, y, lev, desc, cls in GULLIES:
    mark = PREFIX + tag
    if mark in have:
        skipped.append(mark)
        continue
    ds = DirectShape.CreateElement(
        doc, ElementId(int(BuiltInCategory.OST_GenericModel)))
    ds.ApplicationId = "DrainageDR1"
    ds.ApplicationDataId = tag
    ds.SetShape([box_solid(x - 150, y - 150, x + 150, y + 150,
                           lev, lev - 0.300)])
    set_mark(ds, mark, "[%s] %s  (package %s)" % (cls, desc, PACKAGE))
    made.append(mark)

# --- pipe runs as model curves on the drainage subcategory
for tag, pts, bore, grad, desc, cls in RUNS:
    mark = PREFIX + tag
    if mark in have:
        skipped.append(mark)
        continue
    for i in range(len(pts) - 1):
        a, b = pts[i], pts[i + 1]
        p1 = XYZ(mm(a[0]), mm(a[1]), m(a[2]))
        p2 = XYZ(mm(b[0]), mm(b[1]), m(b[2]))
        if p1.DistanceTo(p2) < mm(1.0):
            continue
        ln = Line.CreateBound(p1, p2)
        nrm = ln.Direction.CrossProduct(XYZ.BasisZ)
        if nrm.GetLength() < 1e-9:
            nrm = XYZ.BasisX
        sp = SketchPlane.Create(doc, Plane.CreateByNormalAndOrigin(
            nrm.Normalize(), p1))
        mc = doc.Create.NewModelCurve(ln, sp)
        set_mark(mc, mark + ("" if i == 0 else "-%d" % (i + 1)),
                 "[%s] DN%d at %s  -  %s  (package %s)"
                 % (cls, bore, grad, desc, PACKAGE))
    made.append(mark)

TransactionManager.Instance.TransactionTaskDone()

OUT = ("DRAINAGE %s added to the EXISTING model.\n"
       "  created : %d\n%s\n"
       "  skipped (Mark already present, no duplication): %d\n%s\n\n"
       "MANUAL STEPS STILL REQUIRED:\n%s"
       % (PACKAGE, len(made), "    " + ", ".join(made) if made else "    none",
          len(skipped), "    " + ", ".join(skipped) if skipped else "    none",
          "\n".join("  " + s for s in MANUAL_STEPS)))
