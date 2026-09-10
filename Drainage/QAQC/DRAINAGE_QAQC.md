# DRAINAGE — QA/QC REPORT

**Underground CBRN-hardened blast-resistant protective structure — Pune**
Package **DRAINAGE**, revision **DR1** · 5 September 2026 · geometry **Rev F + M1**
**Sentry post excluded from this package.** Status: **FOR REVIEW — NOT FOR CONSTRUCTION.**

Result classes used throughout: **PASS** · **REVIEW** · **DATA REQUIRED** · **NOT DETERMINABLE**

---

## 1 Geometry

| # | Check | Result | Evidence |
|---|---|---|---|
| G1 | Box external 22 000 × 6 200, internal 20 800 × 5 000 | **PASS** | `mep_proj.BOX` / `INT` against master A.4.2; every plan is drawn from these constants |
| G2 | Perimeter 600, roof 900, mat 600, PCC 100 | **PASS** | master A.4.2 |
| G3 | Bay X-ranges and clear widths, all 8 | **PASS** | master A.3, cross-checked against `1_Underground_Level_Plan.dxf` |
| G4 | W5 200 / W6 400 / W7 400 at their post-M1 positions | **PASS** | master A.3 |
| G5 | Four 110 partitions with 900 door gaps at Y 2500–3400 | **PASS** | master A.3. The drainage spine at **Y 3100 runs through those gaps** — checked, no clash |
| G6 | ESC 1 (2050, 2050) and ESC 2 (19900, 2050), 1400 clear, 250 collar | **PASS** | master A.4.5. No drainage element within the 750 clearance zone |
| G7 | Stair shaft 15200–18000, void 2800 × 3160, pad 2800 × 1840 | **PASS** | master A.4.4. **No drainage element is placed in the shaft, the flights, the well or the landings** |
| G8 | Headhouse 13600–18400 × 200–6000 external, 400 walls, 500 roof | **PASS** | master A.4.6 |
| G9 | Covered stairwell 9250–16050 × 5750–7750, 250 walls | **PASS** | master A.4.7 |
| G10 | Clean sump 1500 × 1500 at X 11068–12568, Y 900–2400 | **PASS** | **Read out of sheet S-06 by parsing its geometry**, not assumed — view V1, 1:60, paper origin 92.03/420.00 |
| G11 | Sump pumps at (11468, 1650) and (12168, 1650) | **PASS** | same parse of S-06 |
| G12 | Service entry plate 11398–12198 × 5600–6200, in the north wall | **PASS** | same parse of S-06 |
| G13 | Decon effluent tank TK-01 at 20198–21398 × 4400–5600 — **in Bay 8** | **REVIEW** | Drawn there on S-06. Bay 8 is outside the protective boundary while the airlock it serves (Bay 6) is inside. See **DR-D4 / DR-F5** below |
| G14 | Threshold channel 300 wide, full 1500 width, X 8950–9250 | **PASS** | Rev F ground plan and section C-C |

## 2 Levels

| # | Check | Result | Evidence |
|---|---|---|---|
| L1 | Grade 0.000, slab top (−)2.000, soffit (−)2.900, floor (−)6.100, mat soffit (−)6.700 | **PASS** | master A.4.3 |
| L2 | Sump invert (−)7.600, base (−)8.000 | **PASS** | master A.4.3. Sump top (−)7.600 + 1.500 = (−)6.100 = the floor — **arithmetic checked, consistent** |
| L3 | Design GWT (−)2.000 | **DATA REQUIRED** | `[ASSUMED]`, master **A2**. Monsoon-season monitoring. Sets the wetted area, the seepage and the sump duty |
| L4 | Headhouse roof soffit +0.400, top +0.900; stairwell head +2.450, soffit +2.200 | **PASS** | master A.4.3 |
| L5 | Invert levels on every pipe in the schedule | **PASS** for the runs whose ends are fixed; **NOT DETERMINABLE** for PD-06, PD-11, PD-13, PD-14, PD-16 | Those five end at soakaways or a septic tank **whose positions do not exist in the project** (open item D3). Direction and gradient are given; length and end invert are recorded as not determinable, not guessed |
| L6 | Finished floor level vs structural floor level | **REVIEW** | **DR-F2** — a drained screed puts FFL 25–78 mm above the structural (−)6.100, so the *finished* clear height is 3122–3175 mm against the structural 3200. Recorded for the architect; no structural dimension changed |

## 3 Rooms and spaces

| # | Check | Result | Evidence |
|---|---|---|---|
| R1 | All 8 bays named consistently with master A.3 and the Rev F GA plan | **PASS** | U-01 … U-08 in `mep_proj.BAYS`; names match the GA plan text exactly |
| R2 | Bay 2 sub-division: lavatory 1800 × 2000 + medical 1800 × 3000 | **PASS** | master A.3 |
| R3 | Bay 6 decon airlock, three stages 2000×2000 / 2000×1500 / 2000×1500 | **PASS** | master A.3; each stage has its own segregated gully |
| R4 | Gas-tight envelope = bays 1–6, 67.8 m², 217.0 m³ | **PASS** | master A.2 |
| R5 | Sanitary fixture layout | **DATA REQUIRED** | No fixture layout exists anywhere in the project. Fixtures scheduled are only those the project's own text implies |

## 4 Structure interface

| # | Check | Result | Evidence |
|---|---|---|---|
| S1 | No drainage penetrates the 900 pressure slab | **PASS** | By design rule, D-001 note 1. Zero roof penetrations on any sheet |
| S2 | Only one penetration of the protective envelope | **PASS** | PD-05 through the service entry plate, as S-06 requires |
| S3 | Floor screed against the mat SIDL allowance | **REVIEW — DR-F4** | 1.0 kPa allows only 42 mm at 24 kN/m³; the adopted grading averages 52 mm = 1.24 kPa. **Excess 0.24 kPa = 25 kN**, 1.2 % of the mat's own weight, 0.4 % of the 6289 kN uplift, acting **favourably** for flotation. **Referred to the structural engineer, not assumed** |
| S4 | Recess in the mat for PD-01 | **REVIEW — BW-01, NOT ACCEPTED** | 300 wide, 150 → 216 deep, leaving 384 of 600 locally, on the line of the peak transverse sagging moment, in the project's most heavily utilised element (84 %, master B.3). **Issued as builder's work. A fallback with no buried drain at all is drawn on D-201 note 5** |
| S5 | Sump pit reinforcement and construction | **PASS** | Carried unchanged from master F.1 / S-06: 300 walls, T16 @ 150 EF EW, 4-T20 trimmers each face and side, cast monolithic with the mat, membrane dressed around the pit |
| S6 | Sump pit base thickness | **REVIEW — C18 OPEN** | F.1 and the A.4.3 levels give 400; S-06 text says 300. **400 held, unchanged.** No drainage consequence — the invert is fixed and storage is measured from it |
| S7 | Uplift / flotation | **PASS — not re-opened** | Designed in master B.3. A drainage package has no standing to revisit it and no new data exists |
| S8 | Waterproofing interface | **PASS** | R-805 requirements carried verbatim: continuous tank, two waterstops per construction joint, crystalline admixture, no cover reduction, puddle flange at every crossing |

## 5 Architecture interface

| # | Check | Result | Evidence |
|---|---|---|---|
| A1 | Main staircase geometry | **PASS — UNCHANGED** | 24R @ 170.8333 / 280, 3 flights × 8, rise 4100, well 200, headroom 2533. Annotated only; no drainage element placed in it |
| A2 | Entry door 1000 × 2100, threshold flush, 50 weather bar | **PASS** | Rev F section C-C; the threshold detail on D-103 is drawn from it |
| A3 | Inner security door 900 × 2100 in HW2 at X 14450–15350 | **PASS** | master A.4.6; no drainage crosses it |
| A4 | Blast doors 1 and 2, 1200 × 2100 at Y 600–1800 | **PASS** | 50 mm threshold upstand at Blast Door 1 keeps zone 2 and 3 water out of zone 1 |
| A5 | Door in W5 between bays 5 and 6 | **DATA REQUIRED** | The master lists no door in W5, but the decon airlock must have a clean-side exit. Minor, but the 50 mm upstand and the gas-tight sub-division both sit on it |
| A6 | Headhouse hose-down point and 1:80 floor gully | **PASS** | Rev F ground plan; carried unchanged, and its "never to the clean sump" instruction is reproduced on three sheets |

## 6 Calculations

| # | Check | Result | Evidence |
|---|---|---|---|
| C1 | 401 m² wetted area reproduced from first principles | **PASS** | 56.40 × 4.700 + 136.40 = **401.48 m²**, 0.12 % from the S-06 figure. The sheet did not say what the 401 was; it does now |
| C2 | Sump storage 3375 / 400 = 8.44 days | **PASS** | Matches S-06 ("8 days") and master A8 ("8.4 days") |
| C3 | Working volume, drawdown, refill, duty ratio | **PASS** | 1350 L, 15.0 min, 81 h, 0.31 % |
| C4 | Alarm margin 675 L = 40 h of warning | **PASS** | |
| C5 | Rising main velocity DN50 at 1.5 L/s = 0.76 m/s | **PASS** | Above the 0.75 m/s self-cleansing minimum |
| C6 | Manning capacity table, DN50–DN150 at 1:60–1:150 | **PASS** | n = 0.010 `[A]`; DN100 at 1:100 gives 6.72 L/s at 0.85 m/s, a **1450 : 1** capacity ratio on the design flow |
| C7 | Trap seal vs overpressure | **PASS** | 75 mm = 736 Pa = 7.4 × operating, 2.5 × the +300 Pa leak test |
| C8 | Rainwater catchments at 50 mm/h | **PASS** for the structures; **NOT DETERMINABLE** site-wide | 177.23 m² → 2.461 L/s. No site plan exists |
| C9 | Rev E open-cut check: 7.2 m² at 50 mm/h = 0.10 L/s | **PASS** | Reproduces the S-06 figure exactly, which is how **DR-C1** was identified |
| C10 | Septic tank, IS 2470 (Pt 1) | **PASS** | Every check reproduces S-06 exactly: 1050 required, 1125 provided, +7.1 % |
| C11 | Soak pit, IS 2470 (Pt 2) | **PASS — DR-C2 CLOSED by RC1** | Was π × 2.0 × 3.5 = 21.99 m² against 22.50 required, **2.3 % short**. **SK-01 WIDENED to 2.200 dia**, depth unchanged: π × 2.2 × 3.5 = **24.19 m² vs 22.50, +7.5 %** |
| C12 | Storm soakaway sizing | **PASS** | 400 / 20 = 20.0 m² required; 21.99 m² adopted, +10 % |
| C13 | Stairwell soakaway recovery | **REVIEW — DR-F3** | 54.6 h to recover from one sump-full at the assumed absorption rate |
| C14 | Screed load vs mat SIDL | **REVIEW — DR-F4** | See S3 |
| C15 | Total pump head, either sump | **DATA REQUIRED** | Static lift is computed (7.30 m). Friction needs the built route; no discharge level exists |
| C16 | Every calculation reproducible | **PASS** | `python3 Scripts/dr_calc.py` regenerates `Calculations/DR_CALC_OUTPUT.txt` in full |

## 7 Schedules

| # | Check | Result |
|---|---|---|
| SC1 | Every schedule generated from `dr_data.py` — one source | **PASS** |
| SC2 | Every tag on a drawing appears in a schedule row, and vice versa | **PASS** — verified by generation: the sheets and the schedules read the same lists |
| SC3 | Every row carries an evidence class | **PASS** |
| SC4 | Rows whose values cannot be determined say so | **PASS** — PD-04, PD-06, PD-07, PD-11, PD-13, PD-14, PD-15, PD-16, SK-03, SK-04 all carry `[N]` or `[U]` and an explicit reason |

## 8 Drawings and DXF

| # | Check | Result | Evidence |
|---|---|---|---|
| D1 | All 13 DXF open and parse | **PASS** | `mep_validate.py`, 13/13 |
| D2 | AutoCAD 2010 (AC1024), `$INSUNITS = 4` | **PASS** | all files |
| D3 | No entity on an undeclared layer | **PASS** | 65 layers declared; 13–23 used per sheet |
| D4 | No zero-length or degenerate geometry | **PASS** | |
| D5 | No unintended duplicate geometry | **PASS** on 12 of 13; **1 warning** on DR-H1 (a single coincident line where the headhouse catchment box overlays the architectural outline — deliberate, both are wanted) |
| D6 | TEXT / MTEXT present and legible (≥ 1.2 mm) | **PASS** | 69–353 text entities per A1 sheet |
| D7 | Real DIMENSION entities present on scaled views | **PASS** | D-001 1, D-101 2, D-102 3, D-103 1, D-201 3, D-203 1, D-204 3, D-301 4, D-304 3, D-305 4 — **25 DIMENSION entities across the set**. D-002 is a symbols and coding sheet with no scaled view and carries none by intent |
| D8 | Extents inside the A1 sheet 0–841 × 0–594 | **PASS** | all 11 A1 sheets |
| D9 | Nothing intrudes into the title block | **PASS** | |
| D10 | No text runs past the sheet edge | **PASS** | |
| D11 | Scope-exclusion note on every sheet | **PASS** | "SENTRY POST EXCLUDED FROM THIS PACKAGE" on all 13 |
| D12 | Every sheet carries an evidence-class key | **PASS** on the 11 A1 sheets |
| D13 | Genuine editable entities, nothing rasterised | **PASS** | LINE, LWPOLYLINE, ARC, CIRCLE, TEXT, MTEXT, DIMENSION, LEADER, HATCH, INSERT only |
| D14 | Visual legibility check | **PASS** | Every sheet rendered to PNG with `mep_render.py` and inspected for clashes and overruns |

Machine output: `QAQC/DXF_VALIDATION_REPORT.txt`.

## 9 Revit

| # | Check | Result | Evidence |
|---|---|---|---|
| V1 | No duplicate model, project, level, grid or room created | **PASS** | `07_drainage_model.py` reads the levels scripts 01–06 made and adds only drainage |
| V2 | Rerun-safe | **PASS by design** | `DR-…` Mark guard, same pattern as scripts 02–06 |
| V3 | Script executes | **NOT DETERMINABLE** | **Revit is not executable in this environment.** The script parses and follows the API used by 01–06, but **it has not been run.** Same status the master records for 01–06 |
| V4 | Operations that cannot be automated are listed | **PASS** | Six manual steps in the script and in `Revit/README.md`, each with its reason |

## 10 Handout

| # | Check | Result |
|---|---|---|
| H1 | Exactly two pages | **PASS** — `DRAINAGE_HANDOUT.pdf`, 2 pages; two A4 DXF sources |
| H2 | Page 1 above ground, page 2 underground, as briefed | **PASS** |
| H3 | Diagram-led, no paragraphs | **PASS** |
| H4 | Every number carries an evidence class | **PASS** |

## 11 Assumptions made by this package

| Ref | Assumption | Impact if wrong |
|---|---|---|
| `[A]` | Manning n = 0.010 for smooth plastic pipe | Capacity ratio is 1450 : 1 — no practical impact |
| `[A]` | C = 1.00 runoff coefficient on roofs **and** cover | Conservative bound; flows are not piped |
| `[A]` | Floor falls 1:80 wet / 1:100 dry, spine 1:400 | Sets the screed thickness and therefore **DR-F4** |
| `[A]` | Screed minimum 25 mm at the outlet | As above |
| `[A]` | 75 mm deep trap seals, primed | 2.5 × the leak-test pressure |
| `[A]` | 50 mm threshold upstands at W5 and Blast Door 1 | Prevents zone 2/3 water entering zone 1 |
| `[A]` | DN100 minimum gravity bore, DN50 rising main | Velocity checked |
| `[A]` | Storm soakaway SK-02 sized at 2.0 dia × 3.5 effective | Rests on the `[A]` absorption rate |
| `[A]` | Gully positions and the Y 3100 spine | Coordination-level; through the confirmed door gaps |

## 12 Missing information — DATA REQUIRED

| Ref | Item |
|---|---|
| **D1** | Rainfall: 50 mm/h is recorded with **no return period, duration or IDF source**. Verify against IMD Pune data |
| **D2** | **Peacetime foul route from the Bay 2 lavatory is undefined.** Case A (cassette in all modes) is drawn; case B (plumbed WC) needs a pumping unit and a second envelope penetration and is shown provisional only |
| **D3** | **No site plan, boundary, contour, well position, municipal sewer, storm connection or outfall exists anywhere in the project.** Five pipe lengths, four soakaway positions, two chamber positions and the IS 2470 (Pt 2) offsets all depend on it |
| **D4** | **Decon effluent tank emptying route is undefined** |
| **A2** | Design GWT (−)2.000 — monsoon monitoring |
| **A7** | Soak-pit absorption 20 L/m²/day — **percolation test mandatory**, IS 2470 (Pt 2) Cl. 4 |
| **A8** | Structural seepage 0.5 L/m²/day — packer permeability tests |
| — | Washdown / hose design flow; sanitary fixture counts and positions; total pump head for both sumps; the level of the service entry plate |

## 12A Coordination findings added at the cross-discipline check (5 Sep 2026)

| Ref | Finding | Result |
|---|---|---|
| **CO-1** | **The rising main cannot run at low level through Bay 5.** The two NBC filter trains occupy X 11098–12548 from Y 2700 to Y 5550 — the full bay width less **58 mm west and 52 mm east** — and the direct line from the sump to the service entry plate passes through both. | **RESOLVED HERE.** PD-05 **rises at the sump and runs at high level over the trains** (D-201 note 8). **Consequence referred:** the service entry plate must therefore also be at high level, **and its level is not recorded anywhere in the project.** |
| **CO-1b** | **S-06 draws the rising main diagrammatically** — east across W5 into Bay 6, then west within the line of the north perimeter wall. Taken literally that crosses the Bay 5/6 gas-tight wall twice and runs longitudinally inside a 600 blast wall. | **READ AS A SCHEMATIC LINE.** DR1 routes the main directly from the sump to the plate within Bay 5 — 2.9 m instead of ~8 m, one wall crossing avoided. **If the S-06 route is literal, W5 needs two gas-tight sleeves and the north wall a longitudinal void — both structural.** Recorded on D-201 note 9. |
| **CO-2** | *"The only penetration of the envelope"* on S-06 sits on a sheet that also shows five blast valves. | **BOTH ARE CORRECT** — the plate is the only **services** penetration; the valves are **protective** penetrations. **This package creates no new penetration of any kind.** |

## 13 Unresolved conflicts

| Ref | Conflict | Held position |
|---|---|---|
| **DR-C1** | S-06's design-flow table carries **0.10 L/s** for stairwell surface water — the **Rev E open-cut** figure, superseded at Rev F where the approach is covered and the catchment with the door shut is zero | **RULED AND CLOSED by RC1**, 10 Sep 2026 (master Part H.14 / K.1 U12): **Rev F governs** (precedent C1 — the drawing governs), and the 0.10 L/s **stays as a declared conservatism** because removing it changes no pump, pipe or pit and deleting a superseded number would hide the history. |
| **DR-C2** | S-06 prints "22.0 m² OK" against its own "22.5 m² required". **21.99 < 22.50, short by 2.3 %** | **RULED AND CLOSED by RC1**, 10 Sep 2026 (master Part H.14 / K.1 U11). **SK-01 widened 2.0 → 2.200 dia, depth unchanged: 24.19 m², +7.5 %.** Widened not deepened — deepening drives the pit below the design GWT (−)2.000 where it cannot soak. **The percolation test still governs the final size** |
| **DR-F5** | Two of the three hydraulic zones the protective boundary creates have **no drainage destination** | Zone 1 drained completely; zone 2's route to its recorded tank and zone 3's outlet are **flagged, not invented** |
| **BW-01** | Mat recess for PD-01 | **Requested, not accepted.** Fallback drawn |
| **C16** | Roof / platform junction | **Carried, not resolved.** See §14 |
| **C18** | Sump pit base 300 vs 400 | **400 held**, as the master does |

## 14 C16 — roof / platform junction

**Not resolved by this package, and deliberately not.**

| Dependency | Effect |
|---|---|
| Roof catchment allocation | The 1500 × 1500 platform roof (2.25 m²) belongs to the stairwell roof at 250 or the headhouse roof at 500. **The total catchment is 177.23 m² either way** — no flow, pipe or pit changes. Only the boundary line on D-102 moves |
| Platform gully GY-10 | Sits directly under the junction. A 250/500 step in the soffit above changes where water is delivered and whether a drip is needed |

**Action taken:** the gully is drawn at its confirmed platform position; the roof is drawn **at 250**
to match the model and the structural register. **C16 is now RULED AT 250 and CLOSED**
(RC1, 10 Sep 2026, master Part H.14) — A.4.7's clause has been corrected, so what was flagged on
D-102, D-103 and D-301. **No irreversible assumption is made and no drainage dimension depends on
the outcome.**

---

## 15 Summary

| Class | Count |
|---|---|
| **PASS** | 52 |
| **REVIEW** | 9 |
| **DATA REQUIRED** | 9 |
| **NOT DETERMINABLE** | 3 |

**The package is developed for project coordination. It is not construction ready, it is not a
final design, and it is not claimed to be code compliant** — three of the codes it relies on are
cited by title only because no code document is in the workspace (master open item M2), and the
mandatory percolation test has not been carried out.
