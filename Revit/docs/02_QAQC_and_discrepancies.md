# Phase 1 / 1B QA/QC — structural model checks and open items

**Revision identifiers: BIM-P1** (original build) **and BIM-P1B** (script
review + execution-preparation pass — idempotency hardening, grid-derived
sentry siting, this document's expanded sections below). This is a review of
the *scripts* in `Revit/scripts/` against `master/MASTER_PROJECT_STATE.md`
and the three primary STAAD models — **the scripts have still not been
executed inside Revit** (see `00_README_WORKFLOW.md`), so this remains a
source-level QA pass, not a model audit of a built `.rvt`. Do not read
anything below as evidence the scripts have been run — they have not. Re-run
this checklist against the actual model after you run the scripts in Revit,
since geometry that looks correct on paper can still fail to join, host, or
close in the real engine.

## Phase 1B — script review: order, dependencies, robustness

Full detail and the beginner run-through are in `00_README_WORKFLOW.md`
("Script order and dependencies", "Does this require Dynamo specifically").
Summary of what was checked and what changed:

- **Script order.** Confirmed correct: 01 Levels+Grids → 02 Main Box →
  03 Headhouse → 04 Entry Stairwell → 05 Main Staircase → 06 Sentry Post.
  Verified by reading each script's actual `get_level(...)`/`get_grid(...)`
  calls, not by assuming the filenames are right — 02-05 depend on Levels
  from 01; 06 depends on Levels AND (new at Phase 1B) Grids from 01; 03
  logically follows 02 (headhouse floor = box roof slab top) though Revit
  would not error if run out of order, it would just be geometrically wrong.
- **Required Revit API functionality.** `Level.Create`, `Grid.Create`,
  `Wall.Create` (both the curve+height overload and, nowhere used, the
  profile overload), `Floor.Create` (the modern `IList<CurveLoop>` overload,
  used throughout for slabs with holes), `Document.Create.NewOpening`,
  `Document.Create.NewFamilyInstance` (columns/beams) — all standard,
  documented Revit API since well before 2022, still current in 2026.
- **Operates on the current document, correctly.** Every script gets its
  document via `DocumentManager.Instance.CurrentDBDocument` (Dynamo's
  standard accessor for "the Revit document this graph is running in") —
  none of them open, create, or reference a different document. This is
  correct for the intended workflow (paste into a Python Script node inside
  a Dynamo graph open against your saved `.rvt`) and is exactly why they
  require Dynamo (or an equivalent Revit Python host) rather than being
  runnable standalone — see "Does this require Dynamo" in the README.
- **Native, editable Revit elements.** Confirmed: `Wall`, `Floor`, and
  (script 06) `FamilyInstance` columns/beams are genuine hosted Revit
  categories with their own parameters, schedulable and editable afterward
  exactly as if drawn by hand. Nothing is a `DirectShape`, imported mesh, or
  detail line standing in for real geometry, with the one stated exception
  (stair flights modelled as sloped structural Floors, not the Stairs tool —
  see script 05's header for why).
- **Transactions.** Each script wraps its entire body in exactly one
  `TransactionManager.Instance.EnsureInTransaction(doc)` /
  `.TransactionTaskDone()` pair — the correct, standard Dynamo pattern for a
  single Python Script node. No nested or nested-looking transactions, no
  transaction left open on an exception path (if a script raises before
  reaching `TransactionTaskDone()`, Dynamo's own execution model rolls the
  node back — this is Dynamo's behavior, not something the script itself
  needs to handle).
- **Duplication on re-run.** This was the main finding at Phase 1B: as
  originally written (BIM-P1), scripts 02-06 had NO guard against re-running
  — every wall/floor/column/beam would be created a second time, on top of
  the first, on a second run. **Fixed.** See "Duplication safety" below.
- **Dynamo requirement.** Confirmed the scripts are Dynamo-specific as
  written (they import `RevitServices`), and documented the exact,
  mechanical swap needed to run them under pyRevit/RPS/a compiled add-in
  instead — see the README section "Does this require Dynamo specifically."

## Duplication safety — what changed and how it works now

**Before Phase 1B:** only script 01 (Levels/Grids) was idempotent — it
checked existing names before creating. Scripts 02-06 created every wall,
floor, column, and beam unconditionally on every run.

**After Phase 1B:** every element created by scripts 02-06 is given a unique
value in its **Mark** parameter (Identity Data — chosen because Mark exists
as a standard instance parameter on Wall, Floor, and structural
FamilyInstance categories alike, so one mechanism covers every element type
these scripts create). Before creating anything, each script collects the
Marks already present in the relevant category
(`OST_Walls`/`OST_Floors`/`OST_StructuralColumns`/`OST_StructuralFraming`)
via `FilteredElementCollector`, and skips creating (and, for W6/W7/HW2/the
headwall, skips re-cutting the associated opening) anything whose Mark is
already there. Both the created list and the skipped list are reported in
each script's `OUT` string.

This was deliberately implemented with Marks rather than, say, checking
geometry/location (comparing curve endpoints or bounding boxes) — Marks are
exact, fast to query, human-readable in schedules, and every element already
needed a distinguishing label for traceability regardless (e.g. "W6 - Blast
Boundary (Bay 6-7)"), so the rerun-safety mechanism and the
documentation/schedule mechanism are the same parameter, not two competing
systems.

**What this does not protect against:** manual edits that put the model in a
state the scripts don't expect (renaming a Mark, deleting one element out of
a pair, etc.) — re-running in that case does what a fresh run for the
missing item would do, which is usually what you want, but is worth knowing
going in.

## Checks performed and passed

- **Levels.** All 14 elevations in the script trace directly to Master
  A.4.3's level table (Formation through Sentry Parapet); none invented.
  Entry-stairwell roof soffit/head (+2.200/+2.450) and sump invert (-7.600/
  -8.000) were deliberately NOT made whole-project Levels — they are local
  features, not floor-to-floor references — and are handled as explicit
  offsets in script 04's raking-roof geometry instead. GWT (-2.000) and
  rockhead (-1.5/-2.0) are geotechnical, not structural, levels; correctly
  excluded.
- **Grids vs wall centrelines.** Every box grid (1-5, A-B) sits exactly on a
  perimeter or W5/W6/W7 centreline computed from Master A.4.2/A.3, not on a
  rounded or eyeballed value. Re-derivation: external 22.000 x 6.200, wall
  600 thick -> centreline offset 0.300 from each external face; internal
  20.800 x 5.000 = external minus 2 x 600 exactly. Confirmed against the
  STAAD box model's own joint coordinates (wall centrelines at X 0.300/21.700,
  Z 0.300/5.900) — exact match.
- **W6/W7 alignment with HW4.** Master A.4.6 states M1 made HW4 (headhouse
  east wall) align exactly with W7. Script 03 places HW4 at X 18.200 and
  script 02 places W7 at the same X 18.200 — the coincidence was checked
  after independently deriving each from its own external/internal pair, not
  copied from one script to the other.
- **Stair rise/run closure.** Main staircase: 3 x 8 x 170.8333 = 4100.0 mm,
  exactly closing -6.100 to -2.000 (Master A.2's stated arrival-to-headhouse
  run). Per-flight run checked against going x count: flights 1/2/3 each run
  1.960 m = 7 x 280 mm, matching the Y-extents given in A.4.4 to the
  millimetre. Entry stairwell flight: 12R x 166.6667 = 2000.0 mm, exactly
  closing 0.000 (top landing) to -2.000 (platform) — also exact.
- **Wall heights self-consistent with level table**, not independently
  chosen: main box walls 3.200 m = -2.900 - (-6.100), matches A.4.2's stated
  clear height 3200 directly. Headhouse walls 2.400 m = +0.400 - (-2.000),
  matches A.4.6's stated clear height 2400 directly.
- **Material/thickness groups** in script 02 were checked one-for-one against
  the STAAD box model's `_MAT_600`/`_ROOF_900`/`_WALL_EXT_600`/
  `_WALL_INT_200`/`_WALL_W6_W7_400` groups and THICKNESS lines — see
  `01_STAAD_comparison.md`.
- **No silent resolution of tagged items.** Every `[ASSUMED]`/`[UNRESOLVED]`
  value touched by the scripts is carried through with its tag intact (grep
  the scripts for "ASSUMED" / "C16" / "NOT AVAILABLE" to find all of them);
  none was quietly turned into a hard number.

## Open items — not resolved, listed for the user

| # | Item | Where | Why it's open |
|---|---|---|---|
| 1 | **Sentry post absolute site position** | `01_levels_and_grids.py` (assumption lives here only, since Phase 1B); `06_structural_sentry_post.py` (derives live from the SA/S1 grids, no longer duplicates the constants) | No coordinate exists anywhere in the project — Master A.2/A.4.8 and all four Rev F sentry DXF sheets state only "≥10 m clear of the shelter excavation." Script places it at an ASSUMED (11.000, 17.750) m, exactly the 10 m minimum north of the entry stairwell. **This needs your confirmation or a real site plan before Phase 2.** Relocating it is now a single, documented procedure (see the README's "Assumption control" table) instead of editing two files by hand and hoping they match. |
| 2 | **C16 — roof/platform junction** | `04_structural_entry_stairwell.py` | Already flagged UNRESOLVED in `QUICK_STATE.md`; reviewed again at Phase 1B and deliberately NOT resolved (see the dedicated "C16" section in `00_README_WORKFLOW.md`). Master A.4.7 text says the stairwell roof "becomes the 500 headhouse roof" over the platform; B.6/A.7.6/F.2 design a 250 roof there instead, and the two headhouse and stairwell roof pieces built in scripts 03/04 are geometrically NOT reconciled (small step at the junction, by design). **Determination: this does NOT block the rest of the structural model** — every other element in scripts 02-06 is fully determined by the Master independent of how C16 resolves; only the single Floor marked "... C16 NOT resolved" in script 04 is provisional. **RULED AT 250 AND CLOSED by RC1, 10 September 2026** (master Part H.14): A.4.7's clause has been corrected, so the stairwell roof is 250 over the platform and the provisional Floor in script 04 can be finalised at 250. **The Revit model followed 250 all along and needs no change.** |
| 3 | **Entry stairwell side-wall profile** | `04_structural_entry_stairwell.py` | Simplified to single straight vertical walls at one height each (side walls 2.900 m, headwall 2.200 m, east wall 2.400 m), not the true stepped/raking retaining profile. The Master gives only the governing retained height (2.9 m) and end levels, not a stepped section. Refine from `current/cad/2_Side_Section_with_Stairs.dxf` / `5_Entry_Headhouse_Stair_Section.dxf` in the architecture phase. |
| 4 | **Footing-to-plinth column stub (sentry post)** | `06_structural_sentry_post.py`, constant `FOOTING_TOP_Z` | The Master's STAAD frame starts at +0.450 (GF FFL) and F1 footings found at -2.000/-1.400; nothing in Master or DXFs sizes the connector between them. Script adds a 350x350 stub (Mark: "Column stub (footing-to-plinth, inferred) ...") as the only way to avoid a floating column — this is an inferred continuity element, not a Master value. Unchanged in substance at Phase 1B; now named as a single constant per the "Assumption control" table rather than an inline literal. |
| 5 | **First-storey sentry infill** | not modelled | "Armoured vision panels, 1200 wide" (A.4.8) has no stated thickness anywhere. Left out rather than guessed — ground-storey 200 mm infill (which IS given) was modelled. |
| 6 | **PCC blinding plan extent** | `02_structural_main_box.py`, constant `PCC_EXTENT_M` | Master gives 100 mm thickness only, not a plan extent beyond the mat. Script assumes the same 22.000 x 6.200 footprint as the mat; real practice usually oversizes blinding ~100-150 mm each side, which is not in the Master. Promoted to a named constant at Phase 1B for easy editing. |
| 7 | **Entry stairwell raft founding levels** | `04_structural_entry_stairwell.py`, constant `RAFT_TOP_OFFSET_M` | "Stepped RC raft 300 thk on compacted fill" has no stated founding RL. Script assumes the raft TOP sits flush with the underside of the 250 mm slab it carries at each end (offset = 0.250 m, the slab thickness; no extra gap) — this is unchanged from the original BIM-P1 geometry, just promoted to a named, documented constant at Phase 1B (the docstring wording was corrected too — it previously said "300 mm below the underside," which did not match what the code actually did). Not a Master value either way. |
| 8 | **Roof local thickening at the void edge** | not modelled | Master B.4.1(b): the roof slab's free edge at the stair-void boundary (Y 3760) thickens 900 -> 1200 mm over a 600 mm band, plus diagonal corner trimmers. The roof slab built in script 02 is uniform 900 mm; this local refinement is not yet modelled. |
| 9 | **Reinforcement** | not modelled | Deferred by design — see `00_README_WORKFLOW.md`. Master Part B's bar schedules are complete and unambiguous; native Revit rebar is a documentation-phase task. |
| 10 | **Material physical/appearance properties** | not modelled | Types are named with their grade (M35/M30) for traceability; Revit Material objects with real IS-456 strength/appearance/thermal data are not authored in Phase 1 (see Section 5 of the original brief, explicitly a later stage). |

## Model integrity — one coherent project, or six disconnected models?

Reviewed at Phase 1B specifically to answer this. **Intended and, on
source-level review, actually achieved: one coherent project.** All six
scripts write into the SAME current document (`DocumentManager.Instance.
CurrentDBDocument` — see "Operates on the current document" above), share
the SAME 14 Levels and 11 Grids from script 01, and every element's
elevation was cross-derived from that one shared level table rather than
each script inventing its own — see "Checks performed and passed" above for
the specific closure checks (wall heights, stair rise/run, HW4/W7
alignment). Risk-by-risk:

| Risk | Assessment |
|---|---|
| **Incorrect levels** | Low. All 14 traced individually to Master A.4.3; no script defines its own competing level. |
| **Incorrect coordinates** | Low for the shelter/headhouse/stairwell/staircase (all in one shared global X/Y/Z system per script 01's coordinate map). Medium-then-resolved for the sentry post: at BIM-P1 it used a SEPARATELY hardcoded copy of the site-position constants (a real coherence risk — the two copies could have drifted). **Fixed at Phase 1B** — script 06 now derives its coordinates live from the Grid elements script 01 placed, so there is structurally only one source, not two that happen to agree today. |
| **Misaligned grids** | Low. Box grids sit on independently-derived wall centrelines that were then checked to coincide (not assumed); sentry grids and sentry geometry are now the same read, by construction, not two independent derivations. |
| **Duplicate elements** | Was HIGH before Phase 1B (no rerun guard at all on 02-06). **Fixed** — see "Duplication safety" above. |
| **Incorrect wall joins** | Not verifiable without Revit itself — Revit auto-joins walls that share endpoints, and the perimeter/internal wall segments were drawn to share exact centreline endpoints (e.g. all four perimeter walls meet at (0.300,0.300)/(21.700,0.300)/etc.), which is what auto-join needs, but whether Revit's join engine actually produces clean corners can only be confirmed by opening the model. Listed here as a check to perform after running, not claimed as passed. |
| **Incorrect slab elevations** | Low. Every Floor's level + z-coordinate was derived from the same shared level table and cross-checked (e.g. roof slab top -2.000 = headhouse floor level, by construction, not coincidence). |
| **Incorrect stair connections** | Low for the main staircase (full rise/run closure re-derived and checked, see above). Medium for the entry stairwell roof, where C16 leaves one piece geometrically provisional (see the C16 entry above) — contained to that one element. |
| **Incorrect openings** | Low. Blast door and security door openings are cut only on walls the script itself just created (guarded by the same Mark check, so a skip doesn't attempt to re-cut on a non-existent reference) — verifiable in Revit, not yet verified. |
| **Disconnected geometry** | Low by design (shared levels/coordinate system) but two DELIBERATE exceptions exist and are documented, not accidental: (1) the entry stairwell roof/headhouse roof junction (C16, contained to one Floor); (2) the sentry post is intentionally physically separate from the shelter (Master: "≥10 m clear," a real design requirement, not a modelling gap). |

## Why there is no existing Revit folder being reused

The task brief said to use the existing/current `Revit` folder and not
create a new one. A full repository scan at the start of this session found
no `Revit/` directory, no `.rvt`, no Dynamo `.dyn`, and no Revit-related
Python/family files anywhere in the repository (only `current/cad` DXFs,
`current/staad` STAAD files, and `master/`). This folder was therefore
created fresh, per the task's own fallback instruction ("If a suitable
existing Revit project already exists, use it. If not, determine the correct
way to create a new Revit 2026 project"). Flagging this explicitly rather
than silently creating the folder, since it contradicts the brief's stated
premise.

## Limitations — state these, do not paper over them

- **No Revit 2026 instance is available in this environment, still.** The
  scripts in `Revit/scripts/` have been authored and then reviewed a second
  time at Phase 1B to correct, idiomatic Revit 2026/Dynamo API usage to the
  best of available knowledge, but **have not been executed against a real
  Revit document, at either phase.** Treat them as a strong, carefully
  cross-checked starting point, not as verified working code — the first
  real run inside Revit is the actual test. The single most likely failure
  point remains parameter-name matching on the sentry post's column/beam
  family (script 06): it now tries the correct `BuiltInParameter` enums
  first for column base/top level and offset (`FAMILY_BASE_LEVEL_PARAM` etc.
  — more robust than guessing display-name strings, since those can be
  renamed/localized) and falls back to name-guessing (`set_param_builtin_or_
  name` helper) only for the width/depth (`b`/`h`/`Width`/`Depth`) parameters,
  which don't have a stable BuiltInParameter across arbitrary column
  families. It also now picks the loaded family/type whose name best matches
  "concrete"/"rectangular" (`best_symbol` helper) instead of blindly taking
  the first one Revit happens to list, and reports a `WARNINGS:` line in
  `OUT` if nothing loaded matched well — read that line if it appears.
- **No `.rvt` file exists or is claimed to exist.** See
  `00_README_WORKFLOW.md`.
- This QA pass, at both phases, is a **source-level review against the
  Master and the STAAD files**, not a QA pass on a built model (schedules,
  view coordination, clash detection, whether Revit's wall-join engine
  actually produces clean corners) — those checks require the scripts to
  actually be run in Revit first, and are listed as such in "Model
  integrity" above rather than claimed as already passed.
