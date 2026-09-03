# Phase 1 QA/QC — structural model checks and open items

**Revision identifier: BIM-P1.** This is a review of the *scripts* in
`Revit/scripts/` against `master/MASTER_PROJECT_STATE.md` and the three
primary STAAD models — the scripts have not been executed inside Revit (see
`00_README_WORKFLOW.md`), so this is a source-level QA pass, not a model
audit of a built `.rvt`. Re-run this checklist against the actual model
after the scripts are run in Revit, since geometry that looks correct on
paper can still fail to join, host, or close in the real engine.

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
| 1 | **Sentry post absolute site position** | `01_levels_and_grids.py`, `06_structural_sentry_post.py` | No coordinate exists anywhere in the project — Master A.2/A.4.8 and all four Rev F sentry DXF sheets state only "≥10 m clear of the shelter excavation." Script places it at an ASSUMED (11.000, 17.750) m, exactly the 10 m minimum north of the entry stairwell. **This needs your confirmation or a real site plan before Phase 2.** |
| 2 | **C16 — roof/platform junction** | `04_structural_entry_stairwell.py` | Already flagged UNRESOLVED in `QUICK_STATE.md`. Master A.4.7 text says the stairwell roof "becomes the 500 headhouse roof" over the platform; B.6/A.7.6/F.2 design a 250 roof there instead, and the two headhouse and stairwell roof pieces built in scripts 03/04 are geometrically NOT reconciled (small step at the junction, by design — see the script header). Needs your ruling before this is closed either way. |
| 3 | **Entry stairwell side-wall profile** | `04_structural_entry_stairwell.py` | Simplified to single straight vertical walls at one height each (side walls 2.900 m, headwall 2.200 m, east wall 2.400 m), not the true stepped/raking retaining profile. The Master gives only the governing retained height (2.9 m) and end levels, not a stepped section. Refine from `current/cad/2_Side_Section_with_Stairs.dxf` / `5_Entry_Headhouse_Stair_Section.dxf` in the architecture phase. |
| 4 | **Footing-to-plinth column stub (sentry post)** | `06_structural_sentry_post.py` | The Master's STAAD frame starts at +0.450 (GF FFL) and F1 footings found at -2.000/-1.400; nothing in Master or DXFs sizes the connector between them. Script adds a 350x350 stub as the only way to avoid a floating column — this is an inferred continuity element, not a Master value. |
| 5 | **First-storey sentry infill** | not modelled | "Armoured vision panels, 1200 wide" (A.4.8) has no stated thickness anywhere. Left out rather than guessed — ground-storey 200 mm infill (which IS given) was modelled. |
| 6 | **PCC blinding plan extent** | `02_structural_main_box.py` | Master gives 100 mm thickness only, not a plan extent beyond the mat. Script assumes the same 22.000 x 6.200 footprint as the mat; real practice usually oversizes blinding ~100-150 mm each side, which is not in the Master. |
| 7 | **Entry stairwell raft founding levels** | `04_structural_entry_stairwell.py` | "Stepped RC raft 300 thk on compacted fill" has no stated founding RL. Script assumes the raft top sits 300 mm below the slab it carries at each end (top landing and platform). Not a Master value. |
| 8 | **Roof local thickening at the void edge** | not modelled | Master B.4.1(b): the roof slab's free edge at the stair-void boundary (Y 3760) thickens 900 -> 1200 mm over a 600 mm band, plus diagonal corner trimmers. The roof slab built in script 02 is uniform 900 mm; this local refinement is not yet modelled. |
| 9 | **Reinforcement** | not modelled | Deferred by design — see `00_README_WORKFLOW.md`. Master Part B's bar schedules are complete and unambiguous; native Revit rebar is a documentation-phase task. |
| 10 | **Material physical/appearance properties** | not modelled | Types are named with their grade (M35/M30) for traceability; Revit Material objects with real IS-456 strength/appearance/thermal data are not authored in Phase 1 (see Section 5 of the original brief, explicitly a later stage). |

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

- **No Revit 2026 instance is available in this environment.** The scripts
  in `Revit/scripts/` have been authored to correct, idiomatic Revit
  2026/Dynamo API usage to the best of available knowledge, but **have not
  been executed against a real Revit document.** Treat them as a strong,
  fully-reasoned starting point, not as verified working code — the first
  real run inside Revit is the actual test, and small parameter-name
  mismatches (e.g. a column family's width/depth parameters not matching the
  guessed names `b`/`h`/`Width`/`Depth`) are the most likely failure point,
  called out in script 06's `set_param_try` helper and its docstring.
- **No `.rvt` file exists or is claimed to exist.** See
  `00_README_WORKFLOW.md`.
- This QA pass is a **source-level review against the Master and the STAAD
  files**, not a QA pass on a built model (schedules, view coordination,
  clash detection) — those checks require the scripts to actually be run in
  Revit first.
