# SCHEDULE OF FINISHES — DRAWING AND FILE INDEX

**Underground CBRN-hardened blast-resistant protective structure — Pune**
Package **SCHEDULE OF FINISHES**, revision **FN1** · 5 September 2026 · geometry **Rev F + M1**
Status of every item: **FOR REVIEW — NOT FOR CONSTRUCTION**. **Sentry post excluded.**

> **NO FINISH SPECIFICATION EXISTS ANYWHERE IN THIS PROJECT.** Every code in this package is a
> **performance requirement** derived from something the project does confirm. The **product** that
> satisfies it is left open, and `Schedules/FINISHES_DATA_REQUIRED.md` lists exactly what is missing.

## Drawings

| No. | Title | File | Format | Scale | Rev | Status |
|---|---|---|---|---|---|---|
| A-601 | Finish legend, notes and typical junction details | `DXF/A-601_Finish_Legend_Notes_and_Typical_Details.dxf` | DXF AC1024, A1 | 1:10 / NTS | FN1 | For review |
| A-611 | Entry level finish plan | `DXF/A-611_Entry_Level_Finish_Plan.dxf` | DXF AC1024, A1 | 1:50 | FN1 | For review |
| A-612 | Underground level finish plan | `DXF/A-612_Underground_Level_Finish_Plan.dxf` | DXF AC1024, A1 | 1:45 | FN1 | For review |

**3 A1 sheets issued.** All AutoCAD 2010 (AC1024) ASCII, A1 841 × 594 mm, `$INSUNITS = 4`, drawn in
paper millimetres, plot 1:1, real editable entities only.

## Schedules

| File | Rows | Contents |
|---|---|---|
| `Schedules/FINISH_LEGEND.md` / `.csv` | 28 | **Every code defined** — F, S, W, C, D, WP — with its performance requirement and where that requirement comes from |
| `Schedules/ROOM_FINISH_SCHEDULE.md` / `.csv` | 13 | **Every space in the project except the sentry post**: number, name, level, area, floor, skirting, wall, ceiling, door, waterproofing, wet-area flag, special requirements, remarks |
| `Schedules/WET_AREA_SCHEDULE.md` / `.csv` | 5 | U-02, U-05, U-06, G-03, G-04 — floor, fall, outlet, wall, tanking, skirting, ceiling |
| `Schedules/STAIR_FINISH_SCHEDULE.md` / `.csv` | 10 | Tread, riser, nosing, landing, soffit/waist, stringer, wall, handrail, guarding — both stairs |
| `Schedules/FINISH_RULES.md` / `.csv` | 4 | The four rules that govern every finish here, each with its source |
| `Schedules/FINISHES_DATA_REQUIRED.md` / `.csv` | 9 | **What is not specified, and why** |

## Documentation, QA/QC and scripts

| File | Contents |
|---|---|
| `Documentation/FINISH_DRAWING_INDEX.md` | This file |
| `Documentation/00_README.md` | What the package is and how to rebuild it |
| `QAQC/FINISH_SCHEDULE_QAQC.md` | PASS / REVIEW / DATA REQUIRED / NOT DETERMINABLE |
| `QAQC/DXF_VALIDATION_REPORT.txt` | Machine output of `mep_validate.py` |
| `Scripts/fn_data.py` | The codes, the room schedule, the stair finishes, the four rules, and what is not specified |
| `Scripts/fn_schedules.py` · `fn_sheets.py` | Generators |
| `Scripts/fn_build_all.py` | **Rebuilds the package** and validates it |
| `Revit/09_room_finishes.py` · `Revit/README.md` | Writes finish parameters onto the **existing** Revit rooms; creates no room and no model |

> Shared modules — `mep_proj.py`, `mep_dxf.py`, `mep_views.py`, `mep_validate.py`, `mep_render.py` —
> live in `Drainage/Scripts/` and are put on `sys.path` by these generators.
