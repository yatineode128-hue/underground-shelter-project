# DRAINAGE — DRAWING AND FILE INDEX

**Underground CBRN-hardened blast-resistant protective structure — Pune**
Package **DRAINAGE**, revision **DR1** · 5 September 2026 · geometry **Rev F + M1**
Status of every item: **FOR REVIEW — NOT FOR CONSTRUCTION**. **Sentry post excluded.**

All DXF: AutoCAD 2010 (**AC1024**) ASCII, A1 841 × 594 mm, `$INSUNITS = 4` (millimetres),
drawn in paper millimetres, plot 1:1. Real editable entities only — LINE, LWPOLYLINE, ARC,
CIRCLE, TEXT, MTEXT, DIMENSION, LEADER, HATCH, INSERT. Nothing rasterised.

## Drawings

| No. | Title | File | Format | Scale | Rev | Status |
|---|---|---|---|---|---|---|
| D-001 | General drainage notes, legend and design basis | `DXF/D-001_General_Drainage_Notes_Legend_Design_Basis.dxf` | DXF AC1024, A1 | NTS | DR1 | For review |
| D-002 | Drainage symbols, pipe coding and abbreviations | `DXF/D-002_Drainage_Symbols_and_Pipe_Coding.dxf` | DXF AC1024, A1 | NTS | DR1 | For review |
| D-101 | Above-ground and entry level drainage plan | `DXF/D-101_Above_Ground_Entry_Level_Drainage_Plan.dxf` | DXF AC1024, A1 | 1:60 | DR1 | For review |
| D-102 | Rainwater catchment and surface-water plan | `DXF/D-102_Rainwater_Catchment_and_Surface_Water_Plan.dxf` | DXF AC1024, A1 | 1:60 | DR1 | For review |
| D-103 | Entry stairwell and headhouse drainage — plan, section, threshold | `DXF/D-103_Entry_Stairwell_and_Headhouse_Drainage.dxf` | DXF AC1024, A1 | 1:50 / 1:10 | DR1 | For review |
| D-201 | Underground drainage plan — falls, gullies, zones | `DXF/D-201_Underground_Drainage_Plan.dxf` | DXF AC1024, A1 | 1:45 / 1:25 | DR1 | For review |
| D-203 | Underground wastewater and sanitary plan | `DXF/D-203_Underground_Wastewater_and_Sanitary_Plan.dxf` | DXF AC1024, A1 | 1:45 | DR1 | For review |
| D-204 | Sump and pumping — plan, section, discharge train, control | `DXF/D-204_Sump_and_Pumping.dxf` | DXF AC1024, A1 | 1:20 | DR1 | For review |
| D-301 | Drainage sections — grade to discharge | `DXF/D-301_Drainage_Sections.dxf` | DXF AC1024, A1 | 1:60 / NTS | DR1 | For review |
| D-304 | Pipe penetration and waterproofing details | `DXF/D-304_Pipe_Penetration_and_Waterproofing_Details.dxf` | DXF AC1024, A1 | 1:10 / 1:5 | DR1 | For review |
| D-305 | Septic tank, soak pit and chamber details | `DXF/D-305_Septic_Tank_Soak_Pit_and_Chamber_Details.dxf` | DXF AC1024, A1 | 1:25 | DR1 | For review |

**11 A1 sheets issued.**

### Numbers deliberately not issued, and why

| No. | Decision |
|---|---|
| **D-202** | *Underground rainwater / stormwater plan* — **NOT ISSUED.** There is no rainwater below ground. The box is buried and fully tanked, no pipe penetrates the roof, and the only water arriving at the underground level is groundwater seepage, which is drawn on D-201 and detailed on D-304. Issuing an empty sheet would be misleading. |
| **D-302** | *Entry / stairwell drainage sections* — **MERGED INTO D-103.** The stairwell is 6800 × 2000; its plan, section and threshold detail read better on one sheet than across two. |
| **D-303** | *Sump / pump details* — **MERGED INTO D-204**, which carries the sump plan, section, control levels and the discharge train together. |

## Calculations

| File | Format | Contents |
|---|---|---|
| `Calculations/DR_CALC_OUTPUT.txt` | Text | D.1–D.17: wetted area, sump storage and cycling, rising main, pipe capacity, floor falls, trap seals, rainwater catchments, entry threshold, septic tank, soak pit, storm soakaway, stairwell soakaway, flow summary, exclusions, screed vs mat SIDL, builder's work BW-01, hydraulic zoning |
| `Scripts/dr_calc.py` | Python | The generator. Every number is derived, not typed in. `python3 dr_calc.py` reproduces the output file. |

## Schedules

| File | Rows | Contents |
|---|---|---|
| `Schedules/DRAIN_SCHEDULE.md` / `.csv` | 12 | Gullies, channels and floor drains |
| `Schedules/PIPE_SCHEDULE.md` / `.csv` | 14 | Every pipe: service, from/to, bore, gradient, invert levels, length, class |
| `Schedules/CHAMBER_SCHEDULE.md` / `.csv` | 6 | Chambers, catchpits, rodding eyes |
| `Schedules/SUMP_AND_PUMP_SCHEDULE.md` / `.csv` | 14 | Sumps, pumps, tanks, septic tank, soakaways |
| `Schedules/SANITARY_FIXTURE_SCHEDULE.md` / `.csv` | 6 | Fixture drainage |
| `Schedules/HYDRAULIC_ZONE_SCHEDULE.md` / `.csv` | 3 | The three zones the protective boundary creates |
| `Schedules/DESIGN_FLOW_SCHEDULE.md` / `.csv` | 5 | Reproduced verbatim from S-06 for line-by-line checking |

## Handout

| File | Format | Contents |
|---|---|---|
| `Handout/DR-H1_Drainage_Above_Ground.dxf` | DXF AC1024, **A4 landscape** | Page 1 — rainwater, surface runoff, entry threshold, external disposal |
| `Handout/DR-H2_Drainage_Underground.dxf` | DXF AC1024, **A4 landscape** | Page 2 — groundwater, wastewater, segregated effluent, sump and pumping |
| `Handout/DRAINAGE_HANDOUT.pdf` | PDF, **exactly 2 pages** | Print copy, rendered from the two DXF pages |

## Documentation and QA/QC

| File | Contents |
|---|---|
| `Documentation/DRAINAGE_DESIGN_BASIS.md` | Design basis, concept, groundwater, sewage, wastewater, discharge, findings, C16 dependency, coordination |
| `Documentation/DRAINAGE_DRAWING_INDEX.md` | This file |
| `Documentation/00_README.md` | How to rebuild the package |
| `QAQC/DRAINAGE_QAQC.md` | PASS / REVIEW / DATA REQUIRED / NOT DETERMINABLE against geometry, levels, rooms, structure, calculations, schedules, drawings, DXF, Revit, handout, annotations, assumptions |
| `QAQC/DXF_VALIDATION_REPORT.txt` | Machine output of `mep_validate.py` for all 13 DXF |

## Scripts

| File | Purpose |
|---|---|
| `Scripts/mep_proj.py` | **Shared** — every geometric, level and services constant, with its source and evidence class |
| `Scripts/mep_dxf.py` | **Shared** — A1 and A4 sheet library, subclassing `Structural CAD/Scripts/sc_dxflib.py` so the sheet standard is identical to the issued R-series |
| `Scripts/mep_views.py` | **Shared** — architectural backgrounds used by all three packages |
| `Scripts/mep_validate.py` | **Shared** — DXF validator, 11 checks |
| `Scripts/mep_render.py` | **Shared** — DXF → PNG visual QA renderer (a checking tool, not a deliverable) |
| `Scripts/dr_data.py` | The drainage network: every gully, pipe, chamber and item of equipment |
| `Scripts/dr_calc.py` | The calculations |
| `Scripts/dr_schedules.py` | Schedule generator |
| `Scripts/d00_general.py` · `d01_plans.py` · `d02_details.py` | Sheet generators |
| `Scripts/dr_handout.py` | Handout generator |
| `Scripts/dr_build_all.py` | **Rebuilds the entire package** and validates it |

> `mep_proj.py`, `mep_dxf.py`, `mep_views.py`, `mep_validate.py` and `mep_render.py` are **shared by
> all three packages** and live here because drainage is their largest consumer. The HVAC and
> Schedule of Finishes generators put this directory on `sys.path` rather than keeping a second copy.

## Revit

| File | Contents |
|---|---|
| `Revit/07_drainage_model.py` | Dynamo Python script that adds the drainage elements to the **existing** Revit model built by `Revit/scripts/01`–`06`. It does not create a project, a level, a grid or a room. |
| `Revit/README.md` | What the script does, what must be done by hand, and why |
