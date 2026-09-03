# Revit 2026 BIM build — workflow and status

**Revision identifiers: BIM-P1** (Phase 1 — audit, Revit project setup, structural
model) **and BIM-P1B** (Phase 1B — script review + execution preparation, no new
geometry). Both are recorded in `master/MASTER_PROJECT_STATE.md` Part H per rule
M.10.

## Why there is no `.rvt` file here

This session runs in a headless Linux container. Revit 2026 is a Windows desktop
application and is not installed, and there is no way to invoke it, its API, or
Dynamo from this environment. **No `.rvt` file has been created, and none is
claimed to exist, and none will be claimed to exist until you have actually run
these scripts and told us the result.** Editing these scripts is not running
Revit, in the same sense that `CLAUDE.md` already holds for STAAD: editing a
`.std` file is not running an analysis.

What *can* be done here, and what this folder contains: Python source for
**Dynamo Python Script nodes** that call the Revit API directly. You run these
**inside Revit 2026 on a Windows machine**, in the order below, against a project
you create there. The scripts are ordinary native-Revit-API calls (`Wall.Create`,
`Floor.Create`, `Level.Create`, `Grid.Create`, `NewFamilyInstance`, …) — every
element they produce is a genuine parametric Revit object, editable afterward
exactly as if you had drawn it by hand. There is no geometry import, no mesh, no
DirectShape standing in for a real wall or slab, with one stated exception (the
main and entry stair flights are modelled as sloped structural Floors rather than
a Revit "Stairs" object — see `05_structural_main_staircase.py`'s header and
`02_QAQC_and_discrepancies.md`).

---

# Run the scripts in Revit 2026 — beginner walkthrough

This section assumes you have never used Dynamo before. Follow it in order; do
not skip steps. Each script prints a short report when it finishes (in the
"Preview" area under Dynamo's Python Script node, or in `OUT` if you inspect the
node's output) — read it before moving to the next script.

### Before you start

You need, on a **Windows machine with Revit 2026 installed**:

- Revit 2026 itself (Dynamo ships inside it — see step 4, no separate install).
- This repository checked out somewhere you can browse to from Windows (or just
  the six files in `Revit/scripts/` copied over — a USB stick, a synced folder,
  whatever gets them onto the Windows machine).

### Step 1 — What to open first

Open **Revit 2026** itself (not a specific file — you don't have one yet).

### Step 2 — Create a blank project (yes, a new one)

On Revit's start screen, click **New...** under Projects. This opens the **New
Project** dialog.

### Step 3 — Which template

In the New Project dialog, click **Browse** and pick a **Structural Template**
(it usually shows as something like `Structural Analysis-DefaultMetric.rte` or
similar wording on your install — the important word to look for is
**"Structural"**, not "Architectural" or "Construction"). This project is
structure-first per the task brief, and a structural template is far more
likely to already have a concrete rectangular column and beam family loaded
(needed for script 06 — see the troubleshooting note below). Click **OK**, then
**OK** again (Project, not Project template) to create the new project.

You now have an unsaved, empty Revit project open. That is correct — do not
close it.

### Step 4 — Save it into this repository

File → Save As → Project. Navigate to this repository's `Revit/` folder and
save as `underground_shelter.rvt` (so the final path is
`Revit/underground_shelter.rvt`). Saving now, before running anything, means
you have a real file to keep saving into as you go.

### Step 5 — Set project units (30 seconds, do this now)

Manage tab → **Project Units**. Set Length = **Millimeters**. This only changes
what the Revit *interface* displays — the scripts convert every value correctly
regardless — but millimetres matches every dimension in the Master and the DXFs,
so what you see on screen will match what you're checking it against.

### Step 6 — Set project information (optional but recommended)

Manage tab → **Project Information**. Fill in Project Name ("Underground
CBRN-Hardened Protective Structure + Sentry Post, Pune") and any project number
you use. This has no effect on the scripts; it's just good practice before you
start adding real content.

### Step 7 — Is Dynamo required? Yes. How to open it

Yes — these scripts are written as **Dynamo Python Script nodes**, which is the
standard, no-extra-install way to run custom Revit-API code without writing a
compiled add-in. Dynamo ships inside Revit 2026; you do not need to download or
install anything separately.

Open it: **Manage tab → Dynamo** (in the "Visual Programming" panel). Dynamo
opens in its own window. Click **File → New** to start a blank graph.

### Step 8 — Add a Python Script node

In Dynamo's node search box (usually on the left, or press the space bar to
open a search popup), type **"Python Script"** and drag the **Python Script**
node onto the canvas. A node appears with a small code-editor area inside it.

**Set its engine to CPython3**: right-click the node → there should be an
"Engine" or similar submenu — pick **CPython3**. (If your Dynamo build still
offers IronPython2 instead, that also works unchanged with these scripts — they
only use the RevitAPI/RevitServices surface common to both engines.)

Double-click the node's code area to edit it, **delete the placeholder text
inside**, and paste in the full contents of one script file (see the run order
below). Do this **fresh for each script** — don't try to reuse one node for all
six; add six nodes (or replace the contents of one node six times, running it
between each edit — either works, but six separate nodes on the canvas gives
you a visible record of what you ran).

### Step 9 — Run the scripts, in this exact order

**The order matters and is not arbitrary** — see "Script order and
dependencies" below for why. Run each one, **read its printed report**, then
move to the next. To run: click **Run** at the bottom of the Dynamo window (or
tick "Run Automatically" and any edit re-runs it — turn that off while you're
still pasting code in, so you don't run half-finished edits).

| Order | File | What you should see happen | Expected report / how to know it worked |
|---|---|---|---|
| 1 | `01_levels_and_grids.py` | Nothing visible in a plan view yet (levels show up in section/elevation views, not plan) — switch to a **South** or **East** elevation view after running to see 14 new Levels stacked up the height of the model. Grids appear immediately in plan. | `OUT` lists "Levels created: [...14 names...]" and "Grids created: [...11 names...]", both with an empty "already existed" list (first run). |
| 2 | `02_structural_main_box.py` | Switch to a plan view at "02 Shelter Floor" — you should see the 22.0 x 6.2 m box outline (4 perimeter walls) plus W5/W6/W7 as internal lines. Switch to "06 Headhouse Floor" to see the roof slab with 3 holes cut in it (a rectangle and two circles). | `OUT` lists ~10 created items (PCC, Mat, W1-W4, W5, W6+opening, W7+opening, Roof+openings), no skips on first run. |
| 3 | `03_structural_headhouse.py` | The small 4.8 x 5.8 m headhouse box appears sitting on top of the main roof slab, roughly in the middle-east portion of the plan. | `OUT` lists HW1-HW4, the door opening, and the headhouse roof — 6 items. |
| 4 | `04_structural_entry_stairwell.py` | A narrow 6.8 x 2.0 m structure appears north of the headhouse, with a visibly sloped roof/floor (view it in 3D — Quick Access Toolbar → Default 3D View — to actually see the slope; a 2D plan view will just show it as a flat rectangle). | `OUT` lists ~10 items: 3 walls + opening, 3 slab pieces, 3 roof pieces, 2 raft pieces. |
| 5 | `05_structural_main_staircase.py` | Inside the box, between W6 and W7 (the "Bay 7" shaft), three sloped slabs and two flat landings appear, forming a dog-leg. Best seen in 3D or in a **section view** cut through the shaft (Section tool, cut north-south through X≈16000). | `OUT` lists 5 items: Flight 1/2/3, Landing L1, Landing L2. |
| 6 | `06_structural_sentry_post.py` | A small separate 2-storey framed building appears well away from the main box (north of the entry stairwell). If this is the FIRST time you're running Revit content with structural columns/beams, this is the step most likely to need attention — see "Known issues" below before you run it. | `OUT` lists footings, columns (including the inferred stub), beams, plinth, slabs, infill — 20+ items, plus a `WARNINGS:` section if the column/beam family it picked wasn't a clear match — **read that section if present.** |

### Step 10 — Save the `.rvt`

**File → Save** (Ctrl+S) after each script, or at minimum after all six. There
is nothing script-specific about saving — it's a normal Revit save. Do this
before closing Revit so you don't lose the run.

### If something goes wrong partway through

- **An exception with a level/grid name in it** ("Level not found, run
  01_levels_and_grids.py first: ...") means an earlier script didn't actually
  run (or was run against a different, unsaved document). Re-run from script 01.
- **An exception naming a family/category** ("No family loaded in category
  Structural Columns...") — see "Known issues" below; load the named family
  and re-run just that script.
- **Anything else** — the transaction the failing script was in will have been
  rolled back or left partial depending on where it failed; check `Edit → Undo`
  history, undo back to a clean state, and re-run that script. Re-running an
  already-succeeded script is safe (see "Duplication safety" below) so when in
  doubt, undo further than you think you need to and just re-run from there.

---

## Script order and dependencies

The correct sequence **is** the one already used above, and it is not
arbitrary — each script after the first looks up Levels, Grids, or specific
named elements that an earlier script must have already created:

1. **`01_levels_and_grids.py`** — no dependencies. Must run first: every other
   script calls `get_level("...")` (and script 06 calls `get_grid("...")`) and
   raises an exception naming exactly what's missing if you skip this.
2. **`02_structural_main_box.py`** — depends on script 1's Levels (`02 Shelter
   Floor`, `01 US Mat`, `06 Headhouse Floor`, `05 Roof Soffit`). Does not depend
   on script 1's Grids (grids are reference geometry only, nothing hosts to
   them directly) but there is no reason to build the box before you have your
   reference grid up.
3. **`03_structural_headhouse.py`** — depends on script 1's Levels AND on
   script 2's roof slab existing to sit on/bear over (not a hard Revit
   dependency — Revit will let you build HW1-HW4 with no roof slab underneath —
   but the model would be geometrically wrong: the headhouse floor level *is*
   the top of that roof slab, so building the headhouse first would leave it
   floating over nothing).
4. **`04_structural_entry_stairwell.py`** — depends on script 1's Levels
   (`06 Headhouse Floor`, `07 Site Grade`, `08 Headhouse Roof Soffit`,
   `09 Headhouse Roof Top`). Independent of scripts 2/3's actual geometry, but
   logically follows the headhouse since it's the same access route.
5. **`05_structural_main_staircase.py`** — depends on script 1's Level
   `02 Shelter Floor`, and is inside the shaft void that script 2's roof slab
   cuts (Master A.4.4). Run after 2 so the void it sits inside already exists.
6. **`06_structural_sentry_post.py`** — depends on script 1's Levels (`10-13`)
   **and, since Phase 1B, on script 1's Grids `SA`/`S1`/`SB`/`S2` existing** —
   it derives the sentry post's entire position and orientation by reading
   those grids' actual geometry (see "Assumption control" below), so it will
   raise a clear exception if they're missing. Independent of scripts 2-5.

If your intended sequence was "1 Levels+Grids, 2 Main Box, 3 Headhouse, 4
Covered Entry Stairwell, 5 Main Staircase, 6 Sentry Post" — **that is exactly
the correct sequence**, confirmed against the actual `get_level`/`get_grid`
calls in each file, not just against the filenames.

## Does this require Dynamo specifically, or could it run another way?

**As written, yes, Dynamo specifically** — every script imports
`RevitServices.Persistence.DocumentManager` and
`RevitServices.Transactions.TransactionManager`, which are Dynamo-for-Revit
assemblies, not part of the core Revit API. That is what gets you the current
document (`DocumentManager.Instance.CurrentDBDocument`) and transaction
handling (`TransactionManager.Instance.EnsureInTransaction` /
`.TransactionTaskDone()`) without writing a full compiled add-in.

They would run under a different Revit Python environment (pyRevit, Revit
Python Shell, or a compiled C# add-in) with a small, mechanical change: swap
the two `RevitServices` calls for that environment's own document/transaction
access —
- **pyRevit**: `doc = __revit__.ActiveUIDocument.Document`, and wrap the body in
  `with Transaction(doc, "...") as t: t.Start(); ...; t.Commit()` (or use
  pyRevit's own `revit.Transaction` context manager) instead of the
  `TransactionManager` calls.
- **Revit Python Shell (RPS)**: same idea — RPS exposes `__revit__` the same
  way pyRevit does.
- **A compiled C# add-in**: the whole body maps almost line-for-line (this is
  literally IronPython/CPython syntax over the same `Autodesk.Revit.DB`
  classes a C# add-in would use); `doc` comes from the `ExternalCommandData`
  argument and transactions are the ordinary `Transaction` class.

Nothing else in the scripts is Dynamo-specific — all element creation
(`Wall.Create`, `Floor.Create`, `NewFamilyInstance`, etc.) is plain
`Autodesk.Revit.DB`. If you don't have Dynamo for some reason but do have
pyRevit, that swap is the only change needed.

## Duplication safety — is it safe to run a script twice?

**Yes, as of Phase 1B.** Every element these scripts create carries a unique
value in its **Mark** (Identity Data) parameter. Before creating anything, each
script reads the Marks already present on the relevant category (Walls,
Floors, Structural Columns, Structural Framing) in the current document and
skips any element whose Mark is already there — it does not re-create it, and
it does not re-cut openings tied to a wall it skipped. The `OUT` report always
lists what was actually created versus what was skipped as already-present, so
you can tell the difference between "nothing happened because it's already
built" and "nothing happened because something's wrong."

This does NOT protect you from renaming/deleting things by hand and then
re-running — if you rename a Mark, delete an element, or otherwise create a
state the scripts don't expect, re-running will do what a fresh run would do
(likely re-create what you deleted, under the same Mark, which is probably
what you want). Types (WallType, FloorType, FamilySymbol duplicates) were
already looked-up-by-name before Phase 1B and remain so — re-running does not
error out on "type name already in use."

## Assumption control — where every `[ASSUMED]` value actually lives

Reviewed at Phase 1B so that no assumption is buried inside geometry math
where you'd have to reverse-engineer it to find or change it:

| Assumption | Lives in | How to change it |
|---|---|---|
| **Sentry post site position + rotation** | `01_levels_and_grids.py`, constants `SENTRY_ORIGIN_X_M` / `SENTRY_ORIGIN_Y_M` / `SENTRY_ROTATION_DEG` | Since Phase 1B, `06_structural_sentry_post.py` does **not** duplicate these — it derives the sentry post's actual position and orientation by reading the "SA"/"S1" Grid elements script 01 created, live, every run. See the exact relocation procedure (it is NOT just "edit and re-run" — script 01's idempotency guard won't move existing grids) in that script's own docstring. |
| **PCC blinding plan extent** | `02_structural_main_box.py`, constant `PCC_EXTENT_M` | Edit that one tuple; currently assumed equal to the mat footprint (22.000 x 6.200), no oversize. |
| **Entry stairwell wall profile** (single straight walls, not the true stepped/raking retaining profile) | `04_structural_entry_stairwell.py`, the `make_wall(...)` calls under "SIMPLIFICATION 1" in the header | Not a single constant — it's a modelling-fidelity choice, documented in the header and in `02_QAQC_and_discrepancies.md`. Refine from the Rev F section DXFs in the architecture phase. |
| **Entry stairwell raft founding level** | `04_structural_entry_stairwell.py`, constant `RAFT_TOP_OFFSET_M` | Edit that one value (currently 0.250 m = the slab thickness, i.e. raft top flush with the slab underside above it). |
| **Sentry footing-to-plinth column stub** | `06_structural_sentry_post.py`, constant `FOOTING_TOP_Z` and the `"Column stub..."` call in the per-grid-point loop | The stub's existence and size (350x350, matching C1) is an inference, not a Master value — see the header. |
| **C16 — roof/platform junction** | Not resolved anywhere — see the dedicated section below. | N/A — needs your ruling, not a script edit. |

None of these were "hidden inside geometry": every one is either a named
constant near the top of its script, or (for the stairwell wall profile,
which isn't reducible to one number) a clearly labelled block with a
cross-reference to the QA doc.

## C16 — status, and whether it blocks anything

**Not arbitrarily resolved, and it does not need to be before you run these
six scripts.** Recapping what the Master itself already has on record
(`QUICK_STATE.md`, Master H.4 row C16): Master A.4.7 states the stairwell roof
"becomes the 500 headhouse roof" over the platform, while B.6, A.7.6 and F.2
all design, load and register a 250 mm stairwell roof there instead, on the
authority of Part L (the final register) — the model (and this script set)
follows the 250 mm value, but **the A.4.7 sentence has deliberately not been
edited**, so the textual conflict inside the Master stands, open, exactly as
H.4 already recorded it before this Revit work started.

**This script set can, and does, proceed with C16 open.** Reasoning: every
other element built by scripts 02-06 (the main box, the headhouse, the main
staircase, the sentry post, and every entry-stairwell element except the
roof-over-platform piece) is fully determined by the Master independent of how
C16 resolves. Only ONE floor object in the whole model —
`"Stairwell Roof over Platform (flat starter piece -- C16 NOT resolved)"` in
script 04 — is geometrically provisional, and it is named as such in its own
Mark so it is easy to find and replace once you rule on C16. Nothing else
would need to change. Leaving it open is therefore a **documented, contained,
open coordination item**, not a blocker on inspecting or continuing to build
out the rest of the structural model.

**To close it**, you (the user) need to decide: does the 250 mm stairwell roof
extend to meet the 500 mm headhouse roof at their actual footprint boundary
(and if so, how — a step, a taper, an overlap), or was A.4.7's sentence simply
never updated when the roof was finalised at 250 mm and should now be
corrected to match B.6/A.7.6/F.2? Either answer is a one-paragraph edit to
Master A.4.7 plus, if the geometry needs to change, a small edit to script 04
— it is not a re-design.

---

## Script inventory and what each one builds

| # | File | Builds | Master source |
|---|---|---|---|
| 01 | `01_levels_and_grids.py` | 14 Levels, 7 shelter-box Grids, 4 sentry-post Grids | A.4.1, A.4.3, A.4.8 |
| 02 | `02_structural_main_box.py` | PCC blinding, mat, 4 perimeter walls (W1–W4), internal walls W5/W6/W7 with the two blast-door openings, roof slab with the stair-void and two escape-shaft openings | A.4.2, A.4.4, A.4.5, B.1–B.4 |
| 03 | `03_structural_headhouse.py` | 4 headhouse walls (HW1–HW4), headhouse roof | A.4.6, B.7 |
| 04 | `04_structural_entry_stairwell.py` | Stepped raft, headwall, both side walls, top-landing slab, platform slab, raking roof, sloped flight waist slab | A.4.7, B.6 |
| 05 | `05_structural_main_staircase.py` | 3 flight waist slabs + 2 intermediate landings, inside the Bay 7 shaft | A.4.4, B.5 — **FROZEN geometry, see the file header** |
| 06 | `06_structural_sentry_post.py` | 4 footings, plinth beam, 4 columns/storey, 4 beams/storey ×2 storeys, 2 slabs, ground-storey ballistic infill panels | A.4.8, B.8 |

## What Phase 1 / 1B deliberately does not do

Per the Phase 1 instruction ("do not yet move to architecture") and the
Phase 1B instruction ("do not create additional architectural elements yet"):
no doors, windows, furniture, MEP, finishes, rooms, schedules, sheets, or view
templates are created by these scripts. No reinforcement is modelled — Part
B's bar schedules exist and are unambiguous, but native Revit rebar is an
architecture/detailing-phase task, not a structural-envelope one. See
`master/MASTER_PROJECT_STATE.md` Part H for the full accounting of what was
built, what was assumed, and what remains open.
