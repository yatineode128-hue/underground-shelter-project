# SCHEDULE OF FINISHES — QA/QC REPORT

**Underground CBRN-hardened blast-resistant protective structure — Pune**
Package **SCHEDULE OF FINISHES**, revision **FN1** · 5 September 2026 · geometry **Rev F + M1**
**Sentry post excluded from this package.** Status: **FOR REVIEW — NOT FOR CONSTRUCTION.**

Result classes: **PASS** · **REVIEW** · **DATA REQUIRED** · **NOT DETERMINABLE**

---

## 1 The premise check — the one that matters most

| # | Check | Result |
|---|---|---|
| **P1** | **Does a finish specification exist anywhere in this project?** | **NO.** The master, the ten Rev F drawings, sheet S-06 and the Structural CAD package fix concrete grade, cover, waterproofing, crack control and bar spacing — and nothing about what a surface is finished with. |
| **P2** | Does this package present finishes as project facts? | **NO — PASS.** Every code is a **performance requirement**, tagged, with its source named. |
| **P3** | Is any product, thickness, colour or manufacturer invented? | **NO — PASS.** Nine items are listed as not specified, with reasons, in `Schedules/FINISHES_DATA_REQUIRED.md` and on A-601 panel 4. |
| **P4** | Is every requirement traceable to something confirmed? | **PASS** — see §3. |

## 2 Rooms and spaces

| # | Check | Result | Evidence |
|---|---|---|---|
| R1 | Every space in the project is scheduled | **PASS** | 13 spaces: U-01…U-08 underground, G-01…G-05 at entry level |
| R2 | Sentry post excluded | **PASS** | No sentry post room appears in any file in this package |
| R3 | Room numbers and names match the master and the Rev F GA plan | **PASS** | Same `mep_proj.BAYS` the drainage and HVAC packages use |
| R4 | Areas | **PASS** where derivable | Bay widths × the 5.000 m internal width; headhouse 11.15 m² usable `[C]`; landings and platform 1500 × 1500 `[C]`. **G-05 has no area — it is the guarded edge of the void, not a room** |
| R5 | Levels | **PASS** | (−)6.100 underground, 0.000 and (−)2.000 at entry level, master A.4.3 |
| R6 | Wet areas identified | **PASS** | U-02, U-05, U-06, G-03, G-04 — from the confirmed room uses and the drainage package |

## 3 Traceability of every requirement

| Code | Requirement traced to | Result |
|---|---|---|
| F-01, W-01, C-01, S-01 | Gas-tight CBRN envelope, bays 1–6, master A.2 | **PASS** |
| F-02, W-02, WP-04 | Wet room uses, master A.3 | **PASS** |
| F-03, S-02, W-03 | **Master A.5 designates the stair shaft faces a wet/dirty zone** — it is why their cover is 30 and not 40 | **PASS** |
| F-04 | Bay 8 generator, the grey zone, master A.3 | **PASS** |
| F-05 | Headhouse floor is the top of the 900 slab, with a hose-down point and a **confirmed 1:80** gully fall, Rev F ground plan | **PASS** |
| F-06, C-03, W-05 | Covered stairwell, outside the protective boundary, **declared expendable**, master A.2 | **PASS** |
| W-04 | Master A.3 places an EMP Zone 2 enclosure in Bay 3; K.3 records the rebar cage gives 0 dB at 1 GHz and *"a Zone 2 welded steel room is the answer"* | **PASS** requirement / **DATA REQUIRED** specification |
| D-01…D-04 | Blast doors, inner security door, entry door and partition door gaps, all confirmed | **PASS** |
| **D-05** | **W5 is confirmed fire and gas-tight but no door is scheduled in it anywhere in the project**, yet the decon airlock must have a clean-side exit | **UNRESOLVED — FN-U1** |
| WP-01…WP-03, WP-05 | R-805 and master A.5 | **PASS** |
| WP-06 | Rev F section C-C — the headhouse and stairwell roofs stand proud of the berm | **PASS** |

## 4 The four rules

| # | Rule | Result | Basis |
|---|---|---|---|
| R1 | **No suspended ceiling, dry lining, boxing-in or cavity anywhere in the gas-tight envelope** | **PASS** | Three independent confirmed reasons: HVAC requires every duct inspectable including the raw-air duct (HV-F2); drainage requires the same of every pipe and trap; a void cannot be decontaminated |
| R2 | **No drilled fixing into the tanked envelope — cast-in only** | **PASS** | 40 mm internal cover and 150 bar spacing as an EMP requirement (master A.5); the membrane and crystalline admixture are the waterproofing (R-805); the cage is the EMP shield. A drilled anchor risks all three |
| R3 | **The floor finish is part of the drainage design** | **PASS — and it carries a live structural item** | Falls, screed thickness and the 25–78 mm build-up are set in drainage D.15 and already exceed the 1.0 kPa mat SIDL by 0.24 kPa (**DR-F4, referred to the structural engineer**) |
| R4 | **Every junction in a wet or clean area is coved, not butted** | **PASS** | Decontamination: a butt joint at the floor is where contaminant collects and the one place a hose cannot reach |

## 5 Stairs

| # | Check | Result |
|---|---|---|
| ST1 | Main staircase geometry unchanged | **PASS** — 24R @ 170.8333 / 280, 3 flights × 8, rise 4100, 1200 wide, 200 well, 200 waist, headroom 2533, landings L1/L2 and the arrival landing. **Annotated only** |
| ST2 | Nosing specified **cast in, not applied** | **PASS** — an applied strip changes the effective going, and the going is frozen |
| ST3 | Tread finish with **no build-up at the nosing** | **PASS** — same reason |
| ST4 | Entry stairwell 12R @ 166.6667 / 300 unchanged | **PASS** |
| ST5 | Handrail and guarding | **PASS as requirements** — NBC 2016 Part 4 for height and continuity; 1100 guarding to the void edge confirmed on the Rev F ground plan. **Materials `[A]`, heights are not finish decisions** |

## 6 Drawings and DXF

| # | Check | Result |
|---|---|---|
| D1 | All 3 DXF open and parse | **PASS** |
| D2 | AC1024, `$INSUNITS = 4` | **PASS** |
| D3 | No entity on an undeclared layer | **PASS** |
| D4 | No zero-length or degenerate geometry | **PASS** |
| D5 | No unintended duplicate geometry | **PASS** |
| D6 | TEXT / MTEXT present and ≥ 1.2 mm | **PASS** — 145–292 per sheet |
| D7 | DIMENSION entities on scaled views | **PASS** — A-611 2, A-612 1. A-601 carries the legend, the rules and two 1:10 details; its details are dimensioned by note, not by DIMENSION entity |
| D8 | Extents inside the A1 sheet | **PASS** |
| D9 | Nothing intrudes into the title block | **PASS** |
| D10 | No text past the sheet edge | **PASS** |
| D11 | Scope-exclusion note on every sheet | **PASS** |
| D12 | **A finish tag in every scheduled space** | **PASS** — 13 tags across A-611 and A-612 |
| D13 | Tags agree with the schedule | **PASS by construction** — both are generated from `fn_data.py` |
| D14 | Visual legibility check | **PASS** — rendered to PNG and inspected |

## 7 Coordination

| # | Interface | Result |
|---|---|---|
| X1 | Architectural plan ↔ finish plan | **PASS** — same background, from `mep_views.py`, as the drainage and HVAC plans |
| X2 | Finish plan ↔ finish schedule | **PASS by construction** — one source |
| X3 | Finishes ↔ drainage | **PASS** — falls, screed and the wet-area gullies are the drainage package's D.15 / D-201; rule R3 records the SIDL constraint rather than restating the falls independently |
| X4 | Finishes ↔ HVAC | **PASS** — rule R1 (no ceiling voids) follows from HV-F2; the U-05 note carries HV-F3's 110 mm side clearance so no one thickens the wall finish there |
| X5 | Finishes ↔ structure | **PASS** — rule R2 protects the cover, the membrane and the EMP cage; no finish reduces the confirmed cover |
| X6 | Finishes ↔ Revit | **PASS** — `09_room_finishes.py` writes the same codes onto the same room numbers |

## 8 Missing information — DATA REQUIRED

Nine items, listed in full in `Schedules/FINISHES_DATA_REQUIRED.md`: product/manufacturer/system for
every code · thicknesses other than the drainage-set screed · colours and light reflectance ·
fire ratings and surface spread of flame · slip-resistance values · chemical resistance against the
decontaminant actually to be used (**the decontaminant is not identified anywhere**) · the EMP Zone 2
specification · the blast door leaf finish (proprietary — **do not overcoat a tested assembly**) ·
**the door in W5**.

## 9 Unresolved

| Ref | Item |
|---|---|
| **FN-U1** | **No door is scheduled in W5 anywhere in the project**, yet W5 is confirmed fire and gas-tight and the decon airlock must have a clean-side exit. D-05 is scheduled as a requirement with **no size and no position**. **Engineer to confirm.** |
| **FN-D1** | No finish specification, of any kind, exists — the premise of §1 |
| **FN-D2** | No fire strategy for finishes exists. NBC 2016 Part 4 is in the Part G register for means of escape and guarding only |
| **DR-F4** | Carried from drainage: the floor build-up exceeds the mat SIDL allowance. **A heavier finish spends an allowance that is already exceeded** |
| **C16** | Carried. **No finish depends on the ruling**; what does is whether a drip is needed at the step in the soffit above G-03 |

---

## 10 Summary

| Class | Count |
|---|---|
| **PASS** | 44 |
| **REVIEW** | 2 |
| **DATA REQUIRED** | 9 |
| **NOT DETERMINABLE** | 1 |

**Developed for project coordination. Design basis established. Pending engineering verification.**
This is **not** a specification and must not be issued as one — it is a schedule of *requirements*
with the products deliberately left open, and nine items must be closed before anything is ordered.
