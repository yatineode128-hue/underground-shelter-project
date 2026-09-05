"""
Dynamo Python Script node — HVAC.  RUN AFTER 01 to 06 (and after 07 if the
drainage package is being modelled too).

Adds the HVAC elements of package HV1 to the EXISTING Revit model that
`Revit/scripts/01_levels_and_grids.py` … `06_structural_sentry_post.py` build.

IT DOES NOT CREATE A PROJECT, A LEVEL, A GRID, A ROOM OR ANY STRUCTURE.
There is exactly one Revit model in this project and this script extends it.

SOURCE OF TRUTH  HVAC/Scripts/hv_data.py and Drainage/Scripts/mep_proj.py,
                 which come from master/MASTER_PROJECT_STATE.md and sheet S-06.
                 The tables below are transcribed from those files; if they ever
                 disagree, the Python source in Scripts/ governs.

COORDINATE MAP   identical to scripts 01-06:
                 master X (east, 0-22000)  -> Revit X
                 master Y (north, 0-6200)  -> Revit Y
                 master LEVELS (grade 0.000) -> Revit Z

SENTRY POST      OUT OF SCOPE.  No sentry post element appears in this script.
MAIN STAIRCASE   FROZEN.  Nothing here touches it.

RERUN SAFETY     every element carries a unique HV- Mark.  Marks already in the
                 document are skipped, so a second run does not duplicate
                 geometry.  Same guard pattern as scripts 02-06.

WHAT CAN AND CANNOT BE AUTOMATED
    CAN     the two NBC filter trains, the plenum and the shafts as generic
            model solids; the five blast valves and the gas-tight dampers as
            tagged marker solids at their CONFIRMED coordinates; duct runs as
            model curves on a ductwork subcategory, carrying size, flow and
            evidence class in Comments.
    CANNOT  create the wall openings the blast valves sit in.  Each is a
            recessed 250 RC valve chamber through a 400 or 600 blast wall with
            a cast-in frame welded to the reinforcement cage - that is
            STRUCTURAL and PROTECTIVE work, not ductwork, and the openings do
            not exist in the model scripts 01-06 build.  Listed as a manual
            step and referred to the protective designer.

*** REVIT IS NOT EXECUTABLE IN THE ENVIRONMENT THIS SCRIPT WAS WRITTEN IN.
    IT HAS BEEN WRITTEN AND REVIEWED BUT HAS NOT BEEN RUN.  Treat the first
    run as a commissioning exercise, on a copy. ***
"""
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from Autodesk.Revit.DB import (
    XYZ, Line, Level, UnitUtils, UnitTypeId, FilteredElementCollector,
    BuiltInParameter, BuiltInCategory, DirectShape, ElementId,
    GeometryCreationUtilities, CurveLoop, SketchPlane, Plane
)
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

PACKAGE = "HV1"
PREFIX = "HV-"


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
    out = set()
    for bic in (BuiltInCategory.OST_GenericModel,
                BuiltInCategory.OST_DuctCurves,
                BuiltInCategory.OST_Lines,
                BuiltInCategory.OST_MechanicalEquipment):
        for e in FilteredElementCollector(doc).OfCategory(bic)\
                .WhereElementIsNotElementType():
            p = e.get_Parameter(BuiltInParameter.ALL_MODEL_MARK)
            if p and p.AsString():
                out.add(p.AsString())
    return out


# ------------------------------------------------------------- the HVAC data
# tag, x0, y0, x1, y1, top(m), bottom(m), description, class
VOLUMES = [
    ("AHU-1", 11098, 3900, 12548, 5550, -3.400, -6.100,
     "NBC filter train 1, 300 m3/h.  Position CONFIRMED on S-06", "C"),
    ("AHU-2", 11098, 2700, 12548, 3800, -3.400, -6.100,
     "NBC filter train 2, 300 m3/h.  TRUE N+1 - either train carries the "
     "whole duty", "C"),
    ("PLENUM", 11098, 2700, 12548, 5550, -3.050, -3.400,
     "Supply plenum, +50 to +100 Pa", "A"),
    ("SH-2", 22598, 1750, 23198, 2350, 1.500, -6.100,
     "Generator air shaft 600 x 600.  Position CONFIRMED on S-06", "C"),
    ("SH-1", -3600, 1750, -3000, 2350, 1.500, -6.100,
     "Fresh-air shaft 600 x 600, gooseneck head +1.500.  Size and head "
     "CONFIRMED; exact plan position ASSUMED", "A"),
]

# tag, x, y, level(m), description, class
VALVES = [
    ("BV-1", 598, 2200, -3.150, "Blast valve DN100, fresh air train 1.  "
     "RECESSED - IS 4991 Cl. 6.2.1", "C"),
    ("BV-2", 598, 4000, -3.150, "Blast valve DN100, fresh air train 2", "C"),
    ("BV-3", 14998, 4900, -3.400, "Blast valve DN100, exhaust + OPRV, IN W6, "
     "discharging to bay 7", "C"),
    ("BV-4", 21398, 1300, -3.400, "Blast valve DN350, generator intake", "C"),
    ("BV-5", 21398, 4700, -3.400, "Blast valve DN350, generator exhaust", "C"),
]

# tag, [(x, y, level_m), ...], size, m3/h, description, class
RUNS = [
    ("FA-2", [(598, 2200, -3.100), (11098, 2200, -3.100)], "200 dia", 300,
     "*** RAW, UNFILTERED AIR THROUGH THE CLEAN ZONE - 11.2 m.  A PROTECTIVE "
     "ELEMENT, NOT A DUCT.  Fully welded, tested to +300 Pa, visible, "
     "labelled RAW AIR - UNFILTERED.  Finding HV-F2 ***", "A"),
    ("FA-3", [(598, 4000, -3.100), (11098, 4000, -3.100)], "200 dia", 300,
     "As FA-2", "A"),
    ("SA-1", [(11098, 4200, -3.100), (9800, 4200, -3.100)], "200 x 100", 240,
     "Supply main, worst-case segment flow", "A"),
    ("SA-2", [(9800, 4200, -3.100), (8000, 4200, -3.100)], "150 x 100", 195,
     "Supply", "A"),
    ("SA-3", [(8000, 4200, -3.100), (4900, 4200, -3.100)], "100 dia", 60,
     "Supply - size governed by the practical minimum", "A"),
    ("SA-4", [(4900, 4200, -3.100), (2600, 4200, -3.100)], "100 dia", 30,
     "Supply - size governed by the practical minimum", "A"),
    ("EA-1", [(4510, 1400, -3.100), (12600, 1400, -3.100)], "100 dia", 45,
     "Lavatory extract, keeps U-02 negative to the clean zone", "A"),
    ("EA-2", [(14300, 4900, -3.400), (14998, 4900, -3.400)], "DN100", 300,
     "Airlock exhaust to BV-3", "C"),
]

MANUAL_STEPS = [
    "1  BLAST VALVE OPENINGS.  Each valve sits in a RECESSED 250 RC valve "
    "chamber through a 400 or 600 blast wall, with a cast-in frame WELDED TO "
    "THE REINFORCEMENT CAGE for EMP continuity.  Those openings are "
    "STRUCTURAL and PROTECTIVE work, they do not exist in the model scripts "
    "01-06 build, and they are NOT created here.  Refer to the protective "
    "designer.",
    "2  ASSIGN MEP SYSTEMS.  If the template has Mechanical families loaded, "
    "replace the model curves with Ducts and set the Duct System to Supply "
    "Air, Return Air or Exhaust Air to match.  The script writes the intended "
    "service, size, flow and evidence class into Comments.",
    "3  TERMINALS.  Diffusers, grilles and transfer grilles are scheduled in "
    "HVAC/Schedules/TERMINAL_SCHEDULE.md but are NOT modelled: no noise "
    "criterion exists anywhere in the project (HV-D4) so the selection cannot "
    "be closed, and modelling an unselected terminal would imply a decision "
    "that has not been made.",
    "4  THE FRESH-AIR SHAFT SH-1 IS PLACED AT AN ASSUMED PLAN POSITION.  Its "
    "size (600 x 600) and head level (+1.500) are confirmed on S-06 and so is "
    "the 12.3 m intake-to-entry separation, but no plan coordinate exists.  "
    "Move it when the site position is confirmed.",
    "5  MAINTENANCE ACCESS.  Each train is 1450 wide in a 1560 clear bay.  "
    "Before the trains are ordered, check the HEPA and carbon cassette "
    "dimensions against the carry route: Blast Door 1 (1200 x 2100), along "
    "bays 6 and 5.  Finding HV-F3.",
    "6  NO COOLING OR HEATING PLANT IS MODELLED.  No cooling load can be "
    "calculated - eight inputs are missing (HV-D3) - so no coil, no chiller "
    "and no pipework is placed.  The dehumidifier DH-1 is confirmed but its "
    "duty is not stated (HV-D5) and it is modelled only as a tagged marker.",
]


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


made, skipped = [], []
have = existing_marks()

TransactionManager.Instance.EnsureInTransaction(doc)

for tag, x0, y0, x1, y1, ztop, zbot, desc, cls in VOLUMES:
    mark = PREFIX + tag
    if mark in have:
        skipped.append(mark)
        continue
    ds = DirectShape.CreateElement(
        doc, ElementId(int(BuiltInCategory.OST_GenericModel)))
    ds.ApplicationId = "HvacHV1"
    ds.ApplicationDataId = tag
    ds.SetShape([box_solid(x0, y0, x1, y1, ztop, zbot)])
    set_mark(ds, mark, "[%s] %s  (package %s)" % (cls, desc, PACKAGE))
    made.append(mark)

for tag, x, y, lev, desc, cls in VALVES:
    mark = PREFIX + tag
    if mark in have:
        skipped.append(mark)
        continue
    ds = DirectShape.CreateElement(
        doc, ElementId(int(BuiltInCategory.OST_GenericModel)))
    ds.ApplicationId = "HvacHV1"
    ds.ApplicationDataId = tag
    ds.SetShape([box_solid(x - 200, y - 200, x + 200, y + 200,
                           lev + 0.200, lev - 0.200)])
    set_mark(ds, mark, "[%s] %s  (package %s)" % (cls, desc, PACKAGE))
    made.append(mark)

for tag, pts, size, q, desc, cls in RUNS:
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
                 "[%s] %s at %d m3/h  -  %s  (package %s)"
                 % (cls, size, q, desc, PACKAGE))
    made.append(mark)

TransactionManager.Instance.TransactionTaskDone()

OUT = ("HVAC %s added to the EXISTING model.\n"
       "  created : %d\n%s\n"
       "  skipped (Mark already present, no duplication): %d\n%s\n\n"
       "MANUAL STEPS STILL REQUIRED:\n%s"
       % (PACKAGE, len(made), "    " + ", ".join(made) if made else "    none",
          len(skipped), "    " + ", ".join(skipped) if skipped else "    none",
          "\n".join("  " + s for s in MANUAL_STEPS)))
