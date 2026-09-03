# STAAD model comparison — Phase 1 audit

Three primary STAAD models exist in `current/staad/` and represent three
different physical structures (confirmed from each file's own header, not
inferred):

| | Underground box | Sentry post | Entry stairwell |
|---|---|---|---|
| File | `Underground_Structure_WITH_LOADS_worked_example (4).STD` | `Sentry_Post_Framed_Seismic.std` | `Entry_Stairwell.std` |
| STAAD mode | SPACE, plate/shell elements | SPACE, beam frame | PLANE, 1 m strip frame |
| Represents | The buried shelter box: mat, 4 perimeter walls, W5/W6/W7, roof slab | The sentry post's 4-column, 2-storey RC moment frame | A 1 m transverse slice through the covered approach stairwell, at the platform end |
| Size | 2170 joints, 1138 shell elements | 12 joints, 16 members | 20 joints, 20 members |
| Geometry | 22.000 x 6.200 external, mid-surface plate model (see note below) | 4.000 x 5.000 external, column grid 3.650 x 4.650 c/c | wall span 2.650 c/c, roof span 1.750 c/c |
| Thickness / size | Mat 600, roof 900, ext. walls 600, W5 200, W6/W7 400 | Columns 350x350, beams 250x450 | Floor/wall/roof all 250 |
| Material | M35, Fe500D (Ec 29.580e6 kN/m2) | M30, Fe500 (Ec 27.386e6 kN/m2) | M35, Fe500D (Ec 29.580e6 kN/m2) — **see note** |
| Supports | `ELASTIC MAT` (ks = 100 000 kN/m3) under the mat, 4 corner joints hand-restated as `FIXED BUT ... KFY` | 4 joints `FIXED` (fully fixed base at GF FFL, +0.450) | Elastic vertical springs per floor joint (`FIXED BUT FX MZ KFY`), one joint also holds FX |
| Load cases | 11 (DL1-4, LL1-2, EP1 soil, HY1 uplift, BL1-3 blast) | 6 (DL, LL, EQ+-X, EQ+-Z) | 5 (DL, LL, EARTH, SURCHARGE, EARTH one-side) |
| Combinations | 5 (101/102/**103 BLAST**/104/105) | 15 (101-113, 201, 202) | 5 (101-104, 201) — **Master A.7.9 states 5 for the entry stairwell is not separately tabulated; this model's own combinations were read directly from the file, not assumed** |
| Design code basis | IS 4991 (blast) + IS 456, γ=1.0 on COMB 103 | IS 1893:2016 (seismic, R=3.0, Vb=73.18 kN) + IS 456 | IS 456 only — static, not blast rated |

## Cross-checks performed (file-level; STAAD.Pro was not run — see Limitations)

- **Underground box thickness/material groups** (`_MAT_600`, `_ROOF_900`,
  `_WALL_EXT_600`, `_WALL_INT_200`, `_WALL_W6_W7_400`, element ranges 1-270 /
  271-508 / 509-976 / 977-1030 / 1031-1138) match Master A.4.2/A.3 exactly:
  mat 600, roof 900, perimeter 600, W5 200, W6/W7 400.
- **M1 is present** in the underground box model: box header states
  "MOD M1: APPROVED. W6 and W7 200 -> 400 thk; box 21.600 -> 22.000; shaft
  15.200-18.000; ESC 2 X 19.500 -> 19.900" and the element/thickness data
  matches. `LOAD 11` (blast on W6/W7) is the M1-added case, present.
- **Blast load values** match Master A.7.1/A.7.4/A.7.5 exactly: 383 kN/m2 on
  roof and walls (`LOAD 8`, `LOAD 9`, `LOAD 11`), 40.65 kN/m2 cover (`LOAD 2`),
  5 kN/m2 floor live (`LOAD 4`), 2.947 kN/m2 staircase load on W6/W7
  (`LOAD 5`), 46.1 kN/m2 uplift (`LOAD 7`), earth+water gradient rows in
  `LOAD 6` (82.71 -> 32.0 kN/m2) reproduce Master A.7.2's 15.41 kPa/m
  gradient exactly (independently confirmed in
  `current/staad/MESH_SENSITIVITY_STUDY.md` Section 3, to 0.01 kPa).
- **Sentry post seismic values** match Master A.7.8 exactly: Ah=0.100,
  W=731.80 kN, Vb=73.18 kN, per-joint forces 13.8954 kN (roof) and 4.3996 kN
  (floor). All 15 combination factors match Master A.7.9's sentry table.
- **Sentry frame base level**: STAAD support joints are at Y=0.450, i.e. the
  frame model starts AT the GF FFL, not at the footing (Master B.8.7's F1
  footing is designed separately, "from the support reactions" — consistent).

## One material discrepancy found and already corrected in the file itself

`Entry_Stairwell.std`'s own header states: *"M35 / Fe500D... Was M30 in the
as-received model; corrected to M35 so that the Ld = 40 phi (T16 -> 640)
already detailed in Master B.6 / F.2 is valid. In M30 the same bar needs
46 phi = 736 and every stairwell lap would be 13% short."* This is already
resolved inside the `.std` file (its `DEFINE MATERIAL` block reads M35); it
is recorded here only so the correction is visible in this audit, not because
it is still open. Revit script `04_structural_entry_stairwell.py` uses M35,
consistent with the corrected file and with Master A.5.

## What each STAAD model contributes to the Revit structural model

| STAAD model | Revit script | What was carried over |
|---|---|---|
| Underground box | `02_structural_main_box.py` | Thicknesses, material grade, real (non-mid-surface) footprint, W6/W7 openings, roof openings |
| Sentry post | `06_structural_sentry_post.py` | Grid spacing (3.650 x 4.650 c/c), column/beam sizes, 2-storey levels, material grade |
| Entry stairwell | `04_structural_entry_stairwell.py` | Wall/floor/roof thickness (250), material grade (M35, corrected), governing retained height (2.9 m) used for the side-wall height simplification |

None of the STAAD *analysis* content (reactions, member forces, design
utilisation ratios) is imported into Revit — Revit does not run STAAD's
analysis and this audit does not claim otherwise. What transferred is
geometry, thickness, material grade and load-path labelling, all of which
were already finalised, hand-checked values in Master Part B before this
Phase 1 work began.

## Limitations of this comparison

- **STAAD.Pro was not executed.** Every statement above is a comparison of
  file *content* (joint coordinates, element/thickness tables, load and
  combination blocks, header comments) against the Master and against each
  other. No analysis was run, in this session or any prior one on record.
- The mesh-sensitivity study (`Underground_Shelter_Mesh_Coarse/Medium/Fine.std`)
  is a separate QA exercise (MS1, see `current/staad/MESH_SENSITIVITY_STUDY.md`)
  and is not one of the three primary models compared here; it re-meshes the
  same box model at 3 densities and its own results table is explicitly
  blank pending a real STAAD.Pro run.
