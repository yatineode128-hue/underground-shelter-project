# Revit 2026 BIM build — workflow and status

**Revision identifier: BIM-P1** (Phase 1 — audit, Revit project setup, structural model).
Record this in `master/MASTER_PROJECT_STATE.md` Part H per rule M.10 before Phase 2 begins.

## Why there is no `.rvt` file here

This session runs in a headless Linux container. Revit 2026 is a Windows desktop
application and is not installed, and there is no way to invoke it, its API, or
Dynamo from this environment. **No `.rvt` file has been created, and none is
claimed to exist.** Editing these scripts is not running Revit, in the same sense
that CLAUDE.md already holds for STAAD: editing a `.std` file is not running an
analysis.

What *can* be done here, and what this folder contains: Python source for
**Dynamo Python Script nodes** that call the Revit API directly. You run these
**inside Revit 2026 on a Windows machine**, in the order below, against a project
you create there. The scripts are ordinary native-Revit-API calls (`Wall.Create`,
`Floor.Create`, `Level.Create`, `Grid.Create`, …) — every element they produce is
a genuine parametric Revit object, editable afterward exactly as if you had drawn
it by hand. There is no geometry import, no mesh, no DirectShape standing in for
a real wall or slab, with one stated exception (the main and entry stair flights
— see `05_structural_main_staircase.py` header).

## What you need on the Windows machine

- **Revit 2026**, structural discipline enabled.
- **Dynamo for Revit**, which ships with Revit — no separate install.
- The **Python Engine** for each Python Script node set to **CPython3** (Revit
  2026's Dynamo no longer ships IronPython2; CPython3 has full `clr`/RevitAPI
  access in current Dynamo builds). If your Dynamo build still offers IronPython2,
  that also works unchanged — the scripts use only the RevitAPI/RevitServices
  surface common to both.

## Step-by-step

1. **Create the project.** In Revit 2026: File → New → Project → pick a
   **Structural Template** (not Architectural — this model is structure-first
   per the task brief). Save it as `Revit/underground_shelter.rvt` in this
   repository checkout (create the file inside this `Revit/` folder, not a new
   one — there was no pre-existing Revit project in this repository to reuse;
   see the Phase 1 report for that finding).
2. **Set project units.** Structural templates default to sensible units, but
   confirm: Manage tab → Project Units → Length = **Millimeters** (matches
   every DXF and the Master's geometry, which is stated in mm; the Master's
   level table is in metres — the scripts convert both correctly via the
   Revit API's `UnitTypeId`, so this step is only about what the *UI* displays).
3. **Set project information.** Manage tab → Project Information: Project
   Name "Underground CBRN-Hardened Protective Structure + Sentry Post, Pune",
   Project Number per your own convention, Client/Status per Master A.1.
4. **Open Dynamo** (Manage tab → Dynamo). New blank graph. Add one
   **Python Script** node per file below, in order, paste the file's contents
   in, run it (each node prints a short confirmation string to its output).
   Run the scripts **in numeric order** — later scripts assume the levels
   and grids from `01` already exist and look them up by name.
5. **Save.** After each script (or after all of them), save the `.rvt`.

## Script inventory and what each one builds

| # | File | Builds | Master source |
|---|---|---|---|
| 01 | `01_levels_and_grids.py` | 12 Levels, 7 shelter-box Grids, 4 sentry-post Grids | A.4.1, A.4.3, A.4.8 |
| 02 | `02_structural_main_box.py` | PCC blinding, mat, 4 perimeter walls (W1–W4), internal walls W5/W6/W7 with the two blast-door openings, roof slab with the stair-void and two escape-shaft openings | A.4.2, A.4.4, A.4.5, B.1–B.4 |
| 03 | `03_structural_headhouse.py` | 4 headhouse walls (HW1–HW4), headhouse roof | A.4.6, B.7 |
| 04 | `04_structural_entry_stairwell.py` | Stepped raft, headwall, both side walls, top-landing slab, platform slab, raking roof, sloped flight waist slab | A.4.7, B.6 |
| 05 | `05_structural_main_staircase.py` | 3 flight waist slabs + 2 intermediate landings + arrival landing, inside the Bay 7 shaft | A.4.4, B.5 — **FROZEN geometry, see the file header** |
| 06 | `06_structural_sentry_post.py` | 4 footings, plinth beam, 4 columns/storey, 4 beams/storey ×2 storeys, 2 slabs, ground/first-storey ballistic infill panels | A.4.8, B.8 |

## What Phase 1 deliberately does not do

Per the Phase 1 instruction ("do not yet move to architecture"): no doors,
windows, furniture, MEP, finishes, rooms, schedules, sheets, or view templates
are created by these scripts. No reinforcement is modelled — Part B's bar
schedules exist and are unambiguous, but native Revit rebar is an architecture/
detailing-phase task, not a structural-envelope one, and modelling it before the
envelope is reviewed would be premature. See the Phase 1 report in the PR/commit
message and `master/MASTER_PROJECT_STATE.md` Part H for the full accounting of
what was built, what was assumed, and what remains open (in particular **C16**,
the roof/platform junction, and the sentry post's absolute site position, which
exists nowhere in the project files as a numeric coordinate).
