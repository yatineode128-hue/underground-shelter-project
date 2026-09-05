# DRAINAGE — REVIT

**There is one Revit model in this project.** It is built by the six Dynamo scripts in
`Revit/scripts/` (project root). This folder does **not** contain a second model, a second project
or a duplicate of anything in `Revit/scripts/`. It contains one script that **adds** the drainage
package to that existing model.

## Files

| File | Purpose |
|---|---|
| `07_drainage_model.py` | Dynamo Python Script node. Adds sump, tanks, service entry plate, 11 gullies and 5 pipe runs to the existing model. Run **after** `01`–`06`. |

## Before you run it

1. Open the model that `Revit/scripts/01`–`06` produced. **Work on a copy for the first run.**
2. Confirm the levels exist — the script reads them and fails loudly if `01_levels_and_grids.py`
   has not been run.
3. The script is **rerun-safe**: every element carries a `DR-…` Mark and any Mark already in the
   document is skipped, so a second run does not duplicate geometry. Same guard pattern as
   scripts `02`–`06`.

## What it will not do, and why

| Not automated | Reason |
|---|---|
| Cutting the **sump pit** into the mat | The mat is a Floor created by script `02`. Cutting a 1500 × 1500 × 1500 recess into a 600 mat is a **structural** change, and both **BW-01** and **C18** are open. SU-01 is modelled as a solid in the mat footprint, not as a void. Cut it by hand only after the structural ruling. |
| Cutting the **PD-01 recess** | Builder's work **BW-01** is *requested, not accepted* — 300 wide, 150 deep rising to 216, leaving 384 of the 600 mat locally. |
| The **service entry plate opening** | The plate is modelled as a solid inside the north wall. The opening through the 600 blast wall is a protective-design item, not a drainage one. |
| **MEP system assignment** | If the template has Plumbing families loaded, replace the model curves with Pipes and set the Piping System. The script writes the intended system into Comments so the mapping is unambiguous. |
| **External works** — septic tank, soak pit, storm soakaway, stairwell and headhouse soakaways | **They cannot be positioned.** No site plan, boundary or contour exists anywhere in the project (open item **D3**). |
| **PD-04**, decon effluent bay 6 → TK-01 in bay 8 | The route crosses the protective boundary at W6 and W7 and **does not exist in the project**. A protective-design decision (**DR-D4**, **DR-F5**), not a drainage one. |

## Status

**REVIT IS NOT EXECUTABLE IN THE ENVIRONMENT THIS SCRIPT WAS WRITTEN IN.** The script has been
written and reviewed against the API used by scripts `01`–`06`, and it parses, but **it has not
been run in Revit**. Treat the first run as a commissioning exercise. This is the same status the
master records for `Revit/scripts/01`–`06` (master H.6/H.7: *implemented, not yet run in Revit*).

No `.rvt` file exists in the project, and this package does not create one.
