"""
Dynamo Python Script node — SCHEDULE OF FINISHES.  RUN AFTER 01 to 06.

Writes the finish parameters of package FN1 onto the ROOMS that already exist
in the Revit model, and creates a Room Finish Schedule view.

IT CREATES NO ROOM, NO LEVEL, NO GRID, NO WALL AND NO MODEL.  If the rooms do
not exist yet it says so and stops - it does not invent them.  There is exactly
one Revit model in this project and this script annotates it.

*** THIS IS THE ONE PACKAGE WHERE REVIT IS THE RIGHT PLACE FOR THE DATA. ***
A room finish schedule is a Revit schedule: floor, base, wall and ceiling
finish are BUILT-IN room parameters.  Writing them onto the rooms means the
schedule in the model and the schedule in this package cannot drift apart.

SOURCE OF TRUTH  Schedule of Finishes/Scripts/fn_data.py.  The table below is
                 transcribed from it; if they disagree, fn_data.py governs.

SENTRY POST      OUT OF SCOPE.  No sentry post room appears here.
MAIN STAIRCASE   FROZEN.  This script writes finishes onto the shaft room; it
                 does not touch the stair.

RERUN SAFETY     the script OVERWRITES the finish parameters on a matching room
                 rather than creating anything, so re-running is safe by
                 construction.  It reports every room it wrote and every room
                 it could not find.

*** REVIT IS NOT EXECUTABLE IN THE ENVIRONMENT THIS SCRIPT WAS WRITTEN IN.
    IT HAS BEEN WRITTEN AND REVIEWED BUT HAS NOT BEEN RUN. ***
"""
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from Autodesk.Revit.DB import (
    FilteredElementCollector, BuiltInCategory, BuiltInParameter,
    ViewSchedule, ScheduleFieldType, SpecTypeId
)
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
PACKAGE = "FN1"

# room number, name, floor, base(skirting), wall, ceiling, wet, comment
FINISHES = [
    ("U-01", "EMERGENCY STORES / ESC 1", "F-01", "S-01", "W-01", "C-01", False,
     "Falls 1:100 to the spine.  Keep 750 clear of the ESC opening edge"),
    ("U-02", "LAVATORY + MEDICAL", "F-02", "S-01", "W-02", "C-01", True,
     "WET AREA.  WP-04 tanking under F-02.  Falls 1:80 to GY-02"),
    ("U-03", "OPS ROOM & HAZARD PLOTTING", "F-01", "S-01", "W-01 + W-04",
     "C-01", False,
     "W-04 EMP ZONE 2 ENCLOSURE - SPECIALIST.  Its finish is subordinate to "
     "its shielding, verified to IEEE Std 299"),
    ("U-04", "BERTHING - 9 BERTHS", "F-01", "S-01", "W-01", "C-01", False,
     "Bunk fixings CAST IN - rule R2, no drilled anchor in the envelope"),
    ("U-05", "CBRN PLANT + SUMP", "F-02", "S-01", "W-02", "C-01", True,
     "WET AREA.  110 mm clear at the sides of each filter train - do not "
     "thicken the wall finish here (HVAC HV-F3)"),
    ("U-06", "DECON AIRLOCK - 3 STAGE", "F-02", "S-01", "W-02", "C-01", True,
     "WET AREA and the dirtiest surface in the shelter.  Falls 1:80 to the "
     "SEGREGATED gullies.  50 upstand at W5 and at blast door 1"),
    ("U-07", "STAIR SHAFT", "F-03", "S-02", "W-03", "C-02", False,
     "Master A.5 designates these faces a WET / DIRTY ZONE.  MAIN STAIRCASE "
     "GEOMETRY IS FROZEN - cast-in nosing, no tread build-up"),
    ("U-08", "GENERATOR / SERVICES / ESC 2", "F-04", "S-02", "W-03", "C-02",
     False,
     "GREY ZONE.  Bunded plinth under the generator.  GY-09 has NO DRAINAGE "
     "DESTINATION DEFINED - drainage DR-F5"),
    ("G-01", "COVERED STAIRWELL - TOP LANDING", "F-06", "S-03", "W-05",
     "C-03", False, "EXTERNAL.  300 channel + grating at the threshold"),
    ("G-02", "COVERED STAIRWELL - FLIGHT", "F-06", "S-03", "W-05", "C-03",
     False, "EXTERNAL.  Non-slip is the most important finish here - it is "
     "the only entry route.  Cast nosing"),
    ("G-03", "COVERED STAIRWELL - PLATFORM", "F-06", "S-03", "W-05", "C-03",
     True, "C16 - the roof above is unresolved, 250 or 500.  The finish does "
     "not depend on it; the drip at the junction does"),
    ("G-04", "HEADHOUSE", "F-05", "S-02", "W-05", "C-02", True,
     "Floor IS the top of the 900 pressure slab.  Confirmed 1:80 fall to "
     "GY-11, which goes to an EXTERNAL soakaway and NEVER to the clean sump"),
    ("G-05", "HEADHOUSE - STAIR VOID EDGE", "F-05", "S-02", "W-05", "-",
     False, "1100 guarding to the void edge - NBC 2016 Part 4, not a finish "
     "decision"),
]

NOT_SPECIFIED = (
    "PRODUCT, THICKNESS, COLOUR AND MANUFACTURER ARE NOT SPECIFIED ANYWHERE "
    "IN THIS PROJECT.  Every code is a PERFORMANCE REQUIREMENT.  See "
    "Schedule of Finishes/Schedules/FINISHES_DATA_REQUIRED.md - nine items, "
    "all of which must be closed before anything is ordered.")


def rooms_by_number():
    out = {}
    for r in FilteredElementCollector(doc)\
            .OfCategory(BuiltInCategory.OST_Rooms)\
            .WhereElementIsNotElementType():
        p = r.get_Parameter(BuiltInParameter.ROOM_NUMBER)
        if p and p.AsString():
            out[p.AsString().strip()] = r
    return out


def set_param(el, bip, value):
    p = el.get_Parameter(bip)
    if p and not p.IsReadOnly:
        p.Set(value)
        return True
    return False


found = rooms_by_number()
written, missing = [], []

TransactionManager.Instance.EnsureInTransaction(doc)

for num, name, f, s, w, c, wet, note in FINISHES:
    r = found.get(num)
    if r is None:
        missing.append(num + "  " + name)
        continue
    set_param(r, BuiltInParameter.ROOM_FINISH_FLOOR, f)
    set_param(r, BuiltInParameter.ROOM_FINISH_BASE, s)
    set_param(r, BuiltInParameter.ROOM_FINISH_WALL, w)
    set_param(r, BuiltInParameter.ROOM_FINISH_CEILING, c)
    set_param(r, BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS,
              ("[%s] %s%s" % (PACKAGE, "WET AREA.  " if wet else "", note)))
    written.append(num)

# ---- the schedule view itself, created only if it does not already exist
SCHED = "ROOM FINISH SCHEDULE - %s" % PACKAGE
have_sched = any(v.Name == SCHED for v in
                 FilteredElementCollector(doc).OfClass(ViewSchedule))
if not have_sched:
    vs = ViewSchedule.CreateSchedule(
        doc, doc.Settings.Categories.get_Item(
            BuiltInCategory.OST_Rooms).Id)
    vs.Name = SCHED
    wanted = ("Number", "Name", "Level", "Area", "Floor Finish",
              "Base Finish", "Wall Finish", "Ceiling Finish", "Comments")
    defn = vs.Definition
    for fld in defn.GetSchedulableFields():
        try:
            nm = fld.GetName(doc)
        except Exception:
            continue
        if nm in wanted:
            defn.AddField(fld)

TransactionManager.Instance.TransactionTaskDone()

OUT = ("SCHEDULE OF FINISHES %s written onto the EXISTING rooms.\n"
       "  written : %d\n    %s\n"
       "  NOT FOUND IN THE MODEL : %d\n    %s\n\n"
       "  schedule view : %s\n\n"
       "*** %s ***\n\n"
       "IF ROOMS ARE MISSING: scripts 01-06 build the STRUCTURAL model and do "
       "not place rooms.  Place the rooms by hand, numbered exactly as above, "
       "then re-run this script.  IT WILL NOT CREATE THEM - a room is an "
       "architectural decision about enclosure, and inventing one here would "
       "put a boundary in the model that nobody drew."
       % (PACKAGE, len(written), ", ".join(written) if written else "none",
          len(missing), "\n    ".join(missing) if missing else "none",
          "created" if not have_sched else "already present",
          NOT_SPECIFIED))
