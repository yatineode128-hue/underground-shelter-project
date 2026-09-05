# SCHEDULE OF FINISHES — REVIT

**There is one Revit model in this project**, built by the six Dynamo scripts in `Revit/scripts/` at
the project root. This folder does **not** contain a second model or a duplicate of anything. It
contains one script that **writes finish data onto the rooms that already exist** in that model.

| File | Purpose |
|---|---|
| `09_room_finishes.py` | Dynamo Python Script node. Writes Floor / Base / Wall / Ceiling Finish and Comments onto all 13 rooms and creates a Room Finish Schedule view. Run **after** `01`–`06`. |

## Why Revit is the right place for this one

Floor, base, wall and ceiling finish are **built-in Revit room parameters**. Writing them onto the
rooms means the schedule inside the model and the schedule in this package **cannot drift apart** —
which is not true of a drawing-only finishes schedule.

## What it will not do, and why

| Not automated | Reason |
|---|---|
| **Creating rooms** | Scripts `01`–`06` build the **structural** model and do not place rooms. If a room is missing the script **reports it and moves on**. A room is an architectural decision about enclosure; inventing one here would put a boundary in the model that nobody drew. Place the rooms by hand, numbered exactly as scheduled, then re-run. |
| **Materials, thicknesses, colours** | **They do not exist in the project.** The script writes the *code* into the finish parameter and the *requirement* into Comments. It writes no product. |
| **The EMP Zone 2 enclosure** | Specialist. The requirement is confirmed (master A.3, K.3); the specification is not in the project. |
| **The stair** | Frozen geometry. The script writes finishes onto the shaft room (U-07) and does not touch the stair itself. |

**Re-running is safe by construction** — the script overwrites parameters on matching rooms rather
than creating anything, and reports every room written and every room not found.

## Status

**REVIT IS NOT EXECUTABLE IN THE ENVIRONMENT THIS SCRIPT WAS WRITTEN IN.** It has been written and
reviewed against the API used by scripts `01`–`06`, and it parses, but **it has not been run in
Revit** — the same status the master records for `Revit/scripts/01`–`06`.

No `.rvt` file exists in the project, and this package does not create one.
