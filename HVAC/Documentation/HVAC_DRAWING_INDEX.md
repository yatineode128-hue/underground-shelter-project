# HVAC — DRAWING AND FILE INDEX

**Underground CBRN-hardened blast-resistant protective structure — Pune**
Package **HVAC**, revision **HV1** · 5 September 2026 · geometry **Rev F + M1**
Status of every item: **FOR REVIEW — NOT FOR CONSTRUCTION**. **Sentry post excluded.**

All DXF: AutoCAD 2010 (**AC1024**) ASCII, A1 841 × 594 mm (handout A4 297 × 210),
`$INSUNITS = 4` (millimetres), drawn in paper millimetres, plot 1:1. Real editable entities only.

## Drawings

| No. | Title | File | Format | Scale | Rev | Status |
|---|---|---|---|---|---|---|
| M-001 | HVAC general notes, design basis and legend | `DXF/M-001_HVAC_General_Notes_and_Design_Basis.dxf` | DXF AC1024, A1 | NTS | HV1 | For review |
| M-101 | Underground HVAC and ventilation plan | `DXF/M-101_Underground_HVAC_Ventilation_Plan.dxf` | DXF AC1024, A1 | 1:45 / 1:25 | HV1 | For review |
| M-102 | Fresh air and exhaust plan | `DXF/M-102_Fresh_Air_and_Exhaust_Plan.dxf` | DXF AC1024, A1 | 1:55 | HV1 | For review |
| M-201 | HVAC sections | `DXF/M-201_HVAC_Sections.dxf` | DXF AC1024, A1 | 1:55 / 1:25 | HV1 | For review |
| M-202 | Duct and equipment details | `DXF/M-202_Duct_and_Equipment_Details.dxf` | DXF AC1024, A1 | 1:20 / 1:10 / 1:5 | HV1 | For review |
| M-203 | Emergency and protective ventilation schematic | `DXF/M-203_Emergency_Protective_Ventilation_Schematic.dxf` | DXF AC1024, A1 | NTS | HV1 | For review |

**6 A1 sheets issued.**

## Calculations

| File | Contents |
|---|---|
| `Calculations/HV_CALC_OUTPUT.txt` | H.1–H.14: room volumes and the two envelope figures, fresh air against the three criteria, leakage and overpressure, closed mode, airlock purge, room-by-room airflow, duct sizing, duct pressure loss, fan duty, cooling/heating/humidity (not calculated, with the reason), protective ventilation, the raw-air duct, operating modes, exclusions |
| `Scripts/hv_calc.py` | The generator. **Eleven S-06 figures are reproduced from first principles** — see the design basis §2. `python3 hv_calc.py` regenerates the output. |

## Schedules

| File | Rows | Contents |
|---|---|---|
| `Schedules/AIRFLOW_SCHEDULE.md` / `.csv` | 6 | Room airflow, day and night modes, ACH, occupancy |
| `Schedules/HVAC_EQUIPMENT_SCHEDULE.md` / `.csv` | 10 | Trains, fans, CO₂/O₂ plant, dehumidifier, generator, shafts |
| `Schedules/DUCT_SCHEDULE.md` / `.csv` | 12 | Every duct: service, route, flow, size, velocity |
| `Schedules/TERMINAL_SCHEDULE.md` / `.csv` | 9 | Diffusers, grilles, transfer grilles |
| `Schedules/DAMPER_AND_VALVE_SCHEDULE.md` / `.csv` | 14 | Five blast valves, five gas-tight dampers, VCDs, OPRV |
| `Schedules/FILTER_TRAIN_SCHEDULE.md` / `.csv` | 7 | The seven stages, in order |
| `Schedules/OPERATING_MODE_SCHEDULE.md` / `.csv` | 5 | Normal, filtered, closed, purge, generator |

## Handout

| File | Format | Contents |
|---|---|---|
| `Handout/HV-H1_HVAC_Normal_Operation.dxf` | DXF AC1024, **A4 landscape** | Page 1 — fresh air, supply, cascade, exhaust, day/night balance |
| `Handout/HV-H2_HVAC_Emergency_Protective_Operation.dxf` | DXF AC1024, **A4 landscape** | Page 2 — five modes, blast valves, filtration, closed mode, sequence |
| `Handout/HVAC_HANDOUT.pdf` | PDF, **exactly 2 pages** | Print copy, rendered from the two DXF pages |

## Documentation, QA/QC and scripts

| File | Contents |
|---|---|
| `Documentation/HVAC_DESIGN_BASIS.md` | Design basis, the reproduction of all eleven S-06 figures, room airflow, duct sizing, fan duty, why no cooling load, protective ventilation, findings, coordination |
| `Documentation/HVAC_DRAWING_INDEX.md` | This file |
| `Documentation/00_README.md` | How to rebuild |
| `QAQC/HVAC_QAQC.md` | PASS / REVIEW / DATA REQUIRED / NOT DETERMINABLE |
| `QAQC/DXF_VALIDATION_REPORT.txt` | Machine output of `mep_validate.py` for all 8 DXF |
| `Scripts/hv_data.py` | The system: equipment, ducts, terminals, dampers, filters, modes |
| `Scripts/hv_calc.py` · `hv_schedules.py` · `hv_sheets.py` · `hv_handout.py` | Generators |
| `Scripts/hv_build_all.py` | **Rebuilds the entire package** and validates it |
| `Revit/08_hvac_model.py` · `Revit/README.md` | Extends the existing Revit model; does not duplicate it |

> The shared modules — `mep_proj.py`, `mep_dxf.py`, `mep_views.py`, `mep_validate.py`,
> `mep_render.py` — live in `Drainage/Scripts/` and are put on `sys.path` by the HVAC generators.
> One definition, three packages.

> **Note, 10 September 2026 (master H.18).** It is **five** now. The shared modules above
> are also used by the **FIRE AND LIFE SAFETY** package (`F-101`, `F-102`) and the
> **SITE AND CONCEALMENT** package (`C-101`). `mep_dxf.py` and `mep_validate.py` were
> changed to serve them and **both changes are output-neutral** — no HVAC sheet altered,
> and none was regenerated. The rest of this index is the HV1 record as issued on
> 5 September and is unchanged.
