# HVAC — REVIT

**There is one Revit model in this project.** It is built by the six Dynamo scripts in
`Revit/scripts/` at the project root. This folder does **not** contain a second model, a second
project or a duplicate of anything in `Revit/scripts/`. It contains one script that **adds** the
HVAC package to that existing model.

| File | Purpose |
|---|---|
| `08_hvac_model.py` | Dynamo Python Script node. Adds the two NBC filter trains, the plenum, both shafts, all five blast valves and eight duct runs to the existing model. Run **after** `01`–`06` (and after `07` if the drainage package is being modelled too). |

## Before you run it

1. Open the model that `Revit/scripts/01`–`06` produced. **Work on a copy for the first run.**
2. The script reads the levels those scripts created and fails loudly if they are absent.
3. It is **rerun-safe**: every element carries an `HV-…` Mark and Marks already in the document are
   skipped. Same guard pattern as scripts `02`–`06`.

## What it will not do, and why

| Not automated | Reason |
|---|---|
| **Blast valve wall openings** | Each valve sits in a **recessed 250 RC valve chamber** through a 400 or 600 blast wall with a cast-in frame **welded to the reinforcement cage** for EMP continuity. That is structural and protective work, the openings do not exist in the model scripts `01`–`06` build, and creating them is a protective-design decision. |
| **MEP system assignment** | If the template has Mechanical families loaded, replace the model curves with Ducts and set the Duct System. The script writes the intended service, size, flow and evidence class into Comments so the mapping is unambiguous. |
| **Terminals** | Diffusers and grilles are scheduled but **not modelled**: no noise criterion exists anywhere in the project (**HV-D4**), so the selection cannot be closed, and modelling an unselected terminal would imply a decision nobody has made. |
| **Cooling / heating plant** | **No cooling load can be calculated** — eight inputs are missing (**HV-D3**). No coil, chiller or pipework is placed. DH-1 is confirmed but its duty is not stated (**HV-D5**) and it is a tagged marker only. |
| **Fresh-air shaft position** | Size (600 × 600) and head (+1.500) are confirmed, and so is the 12.3 m intake-to-entry separation, but **no plan coordinate exists**. SH-1 is placed at an assumed position — move it when the site position is confirmed. |

## Status

**REVIT IS NOT EXECUTABLE IN THE ENVIRONMENT THIS SCRIPT WAS WRITTEN IN.** It has been written and
reviewed against the API used by scripts `01`–`06`, and it parses, but **it has not been run in
Revit**. Treat the first run as a commissioning exercise. This is the same status the master records
for `Revit/scripts/01`–`06` (master H.6/H.7: *implemented, not yet run in Revit*).

No `.rvt` file exists in the project, and this package does not create one.
