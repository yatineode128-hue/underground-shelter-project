# `current/staad/` — the STAAD.Pro models

Six `.std` files and the mesh sensitivity study. Authority for every value in them is
`master/MASTER_PROJECT_STATE.md` — Parts **A** (geometry, loads), **B** (element design),
**D** (model specification) and **L** (final register). Where a file and the master
disagree, **the master is right.**

## The models

| File | What it is | Size | Master |
|---|---|---|---|
| `Underground_Structure_WITH_LOADS_worked_example (4).STD` | **The reference underground box model.** Reconciled Phase 2 Rev A + **M1**. Mid-surface plate model of mat, roof, four perimeter walls, W5, W6 and W7. **Every Part B box value is checked against this one** | 1 113 joints · 1 138 plates | D.3, H.4 |
| `Sentry_Post_Framed_Seismic.std` | Sentry post, two-storey RC frame, IS 1893 seismic. **16 combinations** — 101–113, 201, 202, 203 | 12 joints · 16 members | D.2, A.7.9 |
| `Entry_Stairwell.std` | Covered approach stairwell frame. **Static only — NOT blast rated**, and the structure it models is declared expendable | 20 joints · 20 members | B.6, A.7.6 |
| `Underground_Shelter_Mesh_Coarse.std` | Mesh sensitivity study **MS1** — coarse variant | 324 joints · 336 plates | H.5 |
| `Underground_Shelter_Mesh_Medium.std` | **MS1** reference mesh — an unmodified-in-substance copy of the box model above | 1 113 joints · 1 138 plates | H.5 |
| `Underground_Shelter_Mesh_Fine.std` | **MS1** — exact h/2 refinement of the reference mesh | 4 500 joints · 4 552 plates | H.5 |

`MESH_SENSITIVITY_STUDY.md` is the MS1 methodology, the panel-by-panel derivation and the
convergence table. **§5 of it is still blank and must stay blank** until a real STAAD.Pro run
fills it.

## The one thing this directory is not

**STAAD.Pro has never been run in this environment.** No moment, displacement, shear, reaction
or design utilisation exists for any of these six models from any run performed here. Editing
and verifying a `.std` is **not** running an analysis and must never be reported as one
(master rule M.13 and the project operating guide).

Two claims that can never be made from these files, whatever a run shows:

* that a **static** run proves blast resistance — it gives the *demand*; the non-linear SDOF
  support-rotation check is Phase 3; and
* that the box does not float — the `ELASTIC MAT` springs take **tension**, so the model will
  never show the raft lifting off. Flotation is a hand check on the real 136.40 m² underside
  (master B.3).

## Before you edit any of these files

Run the validator. It reads the file **the way STAAD reads it** — truncated at the declared
`INPUT WIDTH`, with `-` continuations joined — so a defect that only exists in STAAD's view of
the file is visible to it too.

```
python3 current/staad/Scripts/validate_std.py
```

It writes nothing; `STD_VALIDATION_REPORT.txt` in this directory is the last run's output.
**All six models currently pass with 0 errors.**

### The two rules that are easy to break

1. **Every data line must fit `INPUT WIDTH 79`.** STAAD reads 79 columns and silently discards
   the rest — it does not complain. An 80-column pressure line becomes a *valid* number with
   its last digit gone. Split long element lists on the STAAD `-` continuation character.
   This is exactly how `LOAD 6`'s south-wall pressures became −77.6 / −57.3 / −37.0 instead of
   −77.64 / −57.36 / −37.07 (master **H.26**, revision MS2).
2. **Primary load case numbers must ascend.** `LOAD 10` before `LOAD 11`, not after.

Both are checked, along with element and member topology, planarity, duplicate and orphan
detection, thickness and property coverage, combination references, and whether each
self-equilibrating horizontal load case actually balances — which is the check that catches a
truncated pressure by its effect rather than its cause.
