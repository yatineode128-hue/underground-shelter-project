# DRAINAGE PACKAGE — README

Revision **DR1**, 5 September 2026. Geometry **Rev F + M1**. **Sentry post excluded.**
Status: **FOR REVIEW — NOT FOR CONSTRUCTION.** Developed for project coordination; design basis
established; pending engineering verification.

## Read in this order

1. `Documentation/DRAINAGE_DESIGN_BASIS.md` — what the system is and why.
2. `Calculations/DR_CALC_OUTPUT.txt` — every number, with its inputs.
3. `DXF/D-001` and `DXF/D-002` — notes, legend, symbols and pipe coding.
4. The plans and details, D-101 → D-305.
5. `QAQC/DRAINAGE_QAQC.md` — what was checked, what passed, what is still open.

## Rebuild

```
cd Drainage/Scripts
python3 dr_build_all.py
```

That regenerates the calculations, all seven schedules, all 11 A1 sheets and both handout pages,
then validates every DXF. It needs `ezdxf` (and `matplotlib` only for the handout PDF and the
visual-QA renderer). Nothing else.

Every number on every sheet comes from `mep_proj.py` or `dr_data.py`, so a tag on a drawing and a
row in a schedule cannot disagree. **Edit the generator, not the DXF.**

## Evidence discipline

Every value carries a class: `[C]` confirmed · `[R]` reconstructed here · `[A]` assumed by this
package · `[U]` unresolved · `[N]` not available — DATA REQUIRED. Nothing marked `[A]`, `[U]` or
`[N]` may be built from without written confirmation.

## What this package changed elsewhere in the project

**Nothing.** No existing file was edited by the drainage work. Sheet S-06, the Rev F architectural
drawings, the STAAD models, the master design values and the Structural CAD package are untouched.
Two conflicts found in S-06 (DR-C1, DR-C2) are **recorded, not corrected** — they need a ruling.

## Open items this package raises

`DR-C1` `DR-C2` `DR-D1` `DR-D2` `DR-D3` `DR-D4` `DR-F1` `DR-F2` `DR-F3` `DR-F4` `DR-F5` `BW-01` —
all listed with their evidence on D-001 and in `QAQC/DRAINAGE_QAQC.md`.

Master items **C16**, **C18**, **A2**, **A7** and **A8** are carried and flagged. **None is resolved
by this package.**
