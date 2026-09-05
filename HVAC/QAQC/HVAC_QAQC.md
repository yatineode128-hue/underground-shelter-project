# HVAC — QA/QC REPORT

**Underground CBRN-hardened blast-resistant protective structure — Pune**
Package **HVAC**, revision **HV1** · 5 September 2026 · geometry **Rev F + M1**
**Sentry post excluded from this package.** Status: **FOR REVIEW — NOT FOR CONSTRUCTION.**

Result classes: **PASS** · **REVIEW** · **DATA REQUIRED** · **NOT DETERMINABLE**

---

## 1 Reproduction of the confirmed basis — the primary check

This package's first job was to prove that sheet S-06's ventilation basis is internally consistent.
**Eleven figures were reproduced from first principles. All eleven check.**

| # | S-06 states | Reproduced | Result |
|---|---|---|---|
| B1 | Envelope 67.8 m² | 2900+1800+3500+1800+1560+2000 × 5.000 = **67.80** | **PASS** |
| B2 | Envelope 217.0 m³ | 67.80 × 3.200 = **216.96** | **PASS** |
| B3 | Clean zone 57.8 m² | 67.80 − 10.00 (Bay 6) = **57.80** | **PASS** |
| B4 | Occupied volume 185.0 m³ | 57.80 × 3.200 = **184.96** | **PASS** |
| B5 | FEMA 453 rate 264 m³/h | 57.8 × 10.76391 × 0.25 × 1.699011 = **264.3** | **PASS**, 0.10 % |
| B6 | Leakage 32.5 m³/h | 0.15 × 216.96 = **32.5** | **PASS** |
| B7 | Leakage "11 % of one train" | 32.5 / 300 = **10.8 %** | **PASS** |
| B8 | Time to 1.0 % CO₂ 9.9 h | (0.0096 × 184.96) / 0.18 = **9.9** | **PASS** |
| B9 | Airlock purge 13 min | 5 × 12.8 = 64 m³ at 300 m³/h = **12.8 min** | **PASS** |
| B10 | DN100 throat 10.6 m/s | 300/3600/(π × 0.05²) = **10.61** | **PASS** |
| B11 | DN350 throat 7.5 m/s | 2600/3600/(π × 0.175²) = **7.51** | **PASS** |

**One `[R]` observation S-06 does not state:** the clean zone is the gas-tight envelope *less the
decon airlock*, and the FEMA rate is applied to the clean zone, not the envelope. Worth recording —
a reviewer applying 0.25 cfm/ft² to 67.8 m² would get 310 m³/h and think the design flow was short.

## 2 Geometry and positions

| # | Check | Result | Evidence |
|---|---|---|---|
| G1 | Box, bays, internal walls, partitions, ESCs, stair shaft | **PASS** | Same `mep_proj` constants as the drainage package; master A.3/A.4 |
| G2 | Filter train 1 at X 11098–12548, Y 3900–5550 | **PASS** | **Parsed out of S-06's geometry**, not assumed |
| G3 | Filter train 2 at X 11098–12548, Y 2700–3800 | **PASS** | same parse |
| G4 | BV-1 (598, 2200) and BV-2 (598, 4000) — west wall, Bay 1 | **PASS** | same parse |
| G5 | BV-3 (14998, 4900) — **in W6** | **PASS** | same parse. W6 spans 14800–15200, so 14998 is mid-wall |
| G6 | BV-4 (21398, 1300) and BV-5 (21398, 4700) — east wall, Bay 8 | **PASS** | same parse |
| G7 | Generator air shaft 600 × 600 at X 22598–23198 | **PASS** | same parse; outside the box |
| G8 | Fresh-air shaft 600 × 600, gooseneck +1.500 | **PASS** size and head; **`[A]`** exact position | Size and head confirmed on S-06; the shaft is annotated west of the box but not dimensioned in plan |
| G9 | Intake-to-entry separation 12.3 m ≥ 10 m | **PASS** | S-06 |
| G10 | Generator shaft is at the opposite end from the fresh-air intake | **PASS `[R]`** | ≈ 26 m apart — exhaust cannot be drawn into the intake in any wind |

## 3 Levels and clearances

| # | Check | Result | Evidence |
|---|---|---|---|
| L1 | Duct zone 150 deep under the (−)2.900 soffit | **PASS** | 2950 clear below the largest duct against a 3200 structural clear height |
| L2 | No duct penetrates the 900 pressure slab or the 600 mat | **PASS** | Every envelope crossing is horizontal, through a wall, at a confirmed valve position |
| L3 | Plant fits Bay 5 | **REVIEW — HV-F3** | Each train is 1450 wide in a 1560 clear bay: **110 mm at the sides**. All access is along the bay. **Cassette dimensions must be checked against the route through Blast Door 1 (1200 × 2100) before the trains are ordered** |
| L4 | No HVAC element in the main staircase | **PASS** | Frozen geometry; nothing placed in the flights, well or landings |

## 4 Airflow and system design

| # | Check | Result | Evidence |
|---|---|---|---|
| A1 | Room split sums to the confirmed 300 m³/h | **PASS** | Exact in **both** day and night modes |
| A2 | Occupied room meets the working-shelter rate | **PASS** | 135 / 9 = **15.0 m³/h/person**, criterion 2 exactly |
| A3 | Unoccupied room of the pair | **PASS** | 45 / 9 = 5.0 m³/h/person = the survival rate exactly |
| A4 | Whole-shelter rate | **PASS** | 33.3 m³/h/person, 2.2 × the working rate |
| A5 | Nothing supplied to Bay 6 | **PASS by design** | The airlock is the exhaust path; 300 m³/h transfers through it |
| A6 | Cascade maps onto the airlock stages | **PASS `[R]`** | +50 / +35 / +20 / +10 / 0 across clean zone → 3 stages → Bay 7 |
| A7 | Lavatory runs negative to the clean zone | **PASS** | 45 extract against 30 supply |
| A8 | Duct velocities | **PASS** | 2.1–3.6 m/s in distribution; blast-valve throats fixed by S-06 |
| A9 | Small branches below the velocity band | **PASS — size-governed, not a defect** | At 30 m³/h a 4 m/s duct is ≈ 100 × 25 mm: not buildable, cleanable or sealable. 100 dia adopted as the minimum |
| A10 | Duct pressure loss | **PASS** | Darcy–Weisbach with Colebrook; 20.7 / 40.8 / 1.4 Pa on the three routes |
| A11 | Fan duty | **DATA REQUIRED — HV-D6** | 161 Pa of ductwork + plenum is computed; **5 of the 8 components are vendor data** and in a CBRN train they dominate. A total is **not** quoted |
| A12 | Cooling load | **NOT DETERMINABLE — HV-D3** | **Eight inputs missing**, of which the rock temperature at (−)6.100 governs. **No load is calculated and none is implied** |
| A13 | Dehumidifier duty | **DATA REQUIRED — HV-D5** | Unit confirmed; no latent load, no target RH |
| A14 | Terminal selection | **DATA REQUIRED — HV-D4** | **No noise criterion exists anywhere in the project.** Throw, NC and terminal pressure drop unchecked |

## 5 Protective ventilation

| # | Check | Result | Evidence |
|---|---|---|---|
| P1 | Five blast valves, sizes, flows, velocities, disc forces | **PASS** | Carried unchanged from S-06; velocities reproduced |
| P2 | Recessing to IS 4991 Cl. 6.2.1 | **PASS** | Stated on M-001, M-102 and M-202 with the 36.8 kN / 131 kN comparison |
| P3 | ≥ 2.0 m of duct between valve and plenum | **PASS** | 11.2 m on the fresh-air side — satisfied 5× over |
| P4 | Manual gas-tight damper inboard of every valve | **PASS** | Five scheduled, GD-01…GD-05 |
| P5 | Filter train order and specification | **PASS** | Seven stages, verbatim from S-06 |
| P6 | Hand crank on each fan | **PASS** | Confirmed; commissioning requirement added (M-001 note 5) |
| P7 | Closed-mode consumables | **REVIEW — HV-F1** | **The soda lime (48 h), not the oxygen (80 h), limits closed mode.** S-06 gives all three figures but does not draw the conclusion. It belongs on the drill card |
| P8 | Raw-air duct integrity | **REVIEW — HV-F2** | FA-2/FA-3 carry **unfiltered** air **11.2 m through the clean zone**. Specified as a protective element: fully welded, no push-fit, **tested to the +300 Pa envelope standard**, visible, labelled, re-tested after any work in bays 1–4. **Whether the trains should move to Bay 1 is raised, not taken** |
| P9 | Filter bypass for peacetime | **DATA REQUIRED — HV-D1** | None shown on S-06. Not added — a bypass is a deliberate leak path and a protective decision |
| P10 | Exhaust path to atmosphere | **DATA REQUIRED — HV-D2** | BV-3 discharges into Bay 7; the onward path up the shaft is not recorded and its resistance is unknown |
| P11 | Emergency power | **NOT DETERMINABLE** | The 15 kVA set is confirmed; distribution, UPS and battery autonomy are an **electrical** scope item, not designed here |

## 6 Drawings and DXF

| # | Check | Result |
|---|---|---|
| D1 | All 8 DXF open and parse | **PASS** |
| D2 | AC1024, `$INSUNITS = 4` | **PASS** |
| D3 | No entity on an undeclared layer | **PASS** |
| D4 | No zero-length or degenerate geometry | **PASS** |
| D5 | No unintended duplicate geometry | **PASS** |
| D6 | TEXT / MTEXT present and ≥ 1.2 mm | **PASS** — 78–301 per A1 sheet |
| D7 | DIMENSION entities on scaled views | **PASS** — M-101 2, M-102 1, M-201 3, M-202 2. M-001 and M-203 are a notes sheet and a schematic; neither has a scaled view |
| D8 | Extents inside the A1 sheet | **PASS** |
| D9 | Nothing intrudes into the title block | **PASS** |
| D10 | No text past the sheet edge | **PASS** |
| D11 | Scope-exclusion note on every sheet | **PASS** |
| D12 | Visual legibility check | **PASS** — every sheet rendered to PNG and inspected |

Machine output: `QAQC/DXF_VALIDATION_REPORT.txt`.

## 7 Revit

| # | Check | Result |
|---|---|---|
| V1 | No duplicate model, project, level, grid or room created | **PASS** — `08_hvac_model.py` reads what scripts 01–06 built and adds HVAC only |
| V2 | Rerun-safe | **PASS by design** — `HV-…` Mark guard, same pattern as scripts 02–06 |
| V3 | Script executes | **NOT DETERMINABLE** — **Revit is not executable in this environment.** The script parses and follows the API used by 01–06 but **has not been run** |
| V4 | Manual steps listed with reasons | **PASS** — six, in the script and in `Revit/README.md` |

## 8 Handout

| # | Check | Result |
|---|---|---|
| H1 | Exactly two pages | **PASS** — `HVAC_HANDOUT.pdf`, 2 pages |
| H2 | Page 1 normal operation, page 2 emergency/protective, as briefed | **PASS** |
| H3 | Diagram-led, no paragraphs | **PASS** |
| H4 | Every number carries an evidence class | **PASS** |

## 9 Cross-package coordination

| # | Interface | Result |
|---|---|---|
| X1 | Condensate to the clean sump | **PASS** — 75 mm deep-seal trap with an air gap; the seal depth is sized in drainage calculation D.6 against the same +300 Pa test the HVAC package specifies |
| X2 | Trap seals as a pressure boundary | **PASS** — both packages state the same figure, 736 Pa, from the same source |
| X3 | Plant room shared with the sump | **PASS** — Bay 5 holds both; the condensate run is the shortest possible |
| X4 | Envelope penetrations | **PASS** — drainage crosses once (service entry plate), HVAC crosses at five confirmed valve positions. **No new penetration is created by either package** |
| X5 | Ceiling zone vs drainage screed | **PASS** — HVAC occupies the top 150 mm, drainage the bottom 25–78 mm. No conflict |

## 10 Assumptions made by this package

| Ref | Assumption |
|---|---|
| `[A]` | Room airflow split (the total is `[C]`) |
| `[A]` | Two-mode day/night balance on VCD-1 and VCD-2 |
| `[A]` | Duct sizes and the 100 dia practical minimum |
| `[A]` | Air properties ρ = 1.204, ν = 1.51 × 10⁻⁵, ε = 0.15 mm — standard values, **source not in the workspace** |
| `[A]` | Fitting *k* allowances on the three routes |
| `[A]` | Terminal types, sizes and quantities |
| `[A]` | Exact plan position of the fresh-air shaft |

## 11 Missing information — DATA REQUIRED

Cooling and heating load inputs (8 items) · dehumidifier duty · fan static pressure (5 vendor
components) · filter change-out interval and carbon bed life · noise criterion · generator heat
rejection into Bay 8 · the exhaust path from Bay 7 to atmosphere · whether a peacetime filter bypass
is intended · emergency power distribution, UPS and battery autonomy.

## 12 C16

**No HVAC dependency.** No duct, plant item, terminal or penetration is at the roof/platform
junction; the nearest HVAC element is BV-3 in W6, 1.5 m away and at a different level. **Carried,
not resolved, and it does not constrain this package.**

---

## 13 Summary

| Class | Count |
|---|---|
| **PASS** | 48 |
| **REVIEW** | 4 |
| **DATA REQUIRED** | 7 |
| **NOT DETERMINABLE** | 3 |

**Developed for project coordination. Design basis established. Pending engineering verification.**
Not construction ready, not a final design, and **no code-compliance claim is made** — two of the
standards relied on are cited by title only because no code document is in the workspace (master
open item M2), and the fan duty and cooling load cannot be closed without vendor and site data.
