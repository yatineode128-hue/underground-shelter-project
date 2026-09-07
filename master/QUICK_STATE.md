# QUICK_STATE — current implemented project state

**Orientation digest, not an authority.** `MASTER_PROJECT_STATE.md` governs. Where this file
and the master disagree, the master is right and this file is stale.
Compiled 3 Sep 2026 from the master (Parts A, B, F, L) plus the M1 reconciliation (Part H.4).
Updated 5 Sep 2026 for the DR1 / HV1 / FN1 packages (Part H.9).
Updated 7 Sep 2026 for the Works Management package WM1 (Part H.10).

---

## Identity and revisions

| | |
|---|---|
| Project | Underground CBRN-hardened, blast-resistant protective structure + sentry post, Pune |
| Objective | 9 occupants, 96 h, nuclear air-blast DBT, with CBRN / EMP / fallout hardening |
| Architectural | **Rev F** · Design report **Rev D** · Structural **Phase 2 Rev A + M1** |
| Services packages | Drainage **DR1** · HVAC **HV1** · Schedule of Finishes **FN1** (5 Sep 2026, master H.9) |
| Works Management | **WM1** (7 Sep 2026, master H.10) — whole project, mobilisation to handover |
| **SP-B1** | **SENTRY POST WALLS = BRICK MASONRY** — instructed design change, 7 Sep 2026. The only design change in WM1 |
| **M1** | **APPROVED and IMPLEMENTED 3 Sep 2026** (master H.4) |
| Deliverable | P2 (AutoCAD + STAAD + manual calculations) |

**M1 in one line:** W6 and W7 200 → **400 mm**; box 21 600 → **22 000**; shaft → 15200–18000;
ESC 2 → X 19 900; headhouse and covered stairwell **+200**. Nothing west of X 14 800 moved.

---

## Shelter — geometry

| Item | Value |
|---|---|
| External / internal | **22 000 × 6 200** / **20 800 × 5 000** |
| Perimeter wall · roof slab · mat · PCC | 600 · **900** · 600 · 100 (M15) |
| Internal clear height | 3 200 |
| Engineered cover | 2 000 layered = **40.65 kPa** |

**Bays (post-M1)** — clear widths unchanged by M1:

| Bay | X range | Clear | Use |
|---|---|---|---|
| 1 | 600–3500 | 2900 | Stores, 1000 L tank, **ESC 1** |
| 2 | 3610–5410 | 1800 | Lavatory + medical |
| 3 | 5520–9020 | 3500 | Ops room; EMP Zone 2 |
| 4 | 9130–10930 | 1800 | Berthing, 9 berths |
| 5 | 11040–12600 | 1560 | CBRN plant, **sump** |
| 6 | 12800–14800 | 2000 | Decon airlock, 3 stages |
| 7 | **15200–18000** | 2800 | **Stair shaft** |
| 8 | **18400–21400** | 3000 | Generator (grey zone), **ESC 2** |

**Internal walls:** W8 partitions ×4 @ 110 (900 door gap, Y 2500–3400) · W5 12600–12800 @ **200**
· **W6 14800–15200 @ 400** · **W7 18000–18400 @ 400**. W6/W7 carry Blast Doors 1 and 2
(1200 × 2100, 7 bar) at Y 600–1800 and **are the protective boundary**.

**Levels:** grade 0.000 · T/slab −2.000 · roof soffit −2.900 · floor −6.100 · u/s mat −6.700 ·
formation −6.800 · **GWT −2.000 [ASSUMED]** · L1 −4.7333 · L2 −3.3667 · sump invert −7.600
(base −8.000) · HH roof soffit +0.400 / top +0.900 · stairwell head +2.450 (soffit +2.200) ·
sentry +0.450 / +3.650 / +6.700 / parapet +7.000.

---

## Materials

| | Box / stairs / headhouse | Sentry post |
|---|---|---|
| Concrete | **M35** | **M30** |
| Reinforcement | **Fe500D** | Fe500 |
| E_c | 29 580 N/mm² | 27 386 N/mm² |
| L_d tension · lap | **40 φ** · 50 φ staggered | 46 φ |
| Cover | 75 blinding / 50 earth / 40 internal | 30 beams+slabs, 40 columns, 50 footings |

Max bar spacing **150 both curtains — EMP requirement**, stricter than IS 456.

---

## Design basis

**Blast** — p_so **344.7 kPa** (50 psi), t_d 0.13–1.33 s, μ 5, DLF 1.111 → **383 kPa on roof
AND walls** (K_a = 1.0). f_ck,dyn 43.75 · f_y,dyn 625 · **no dynamic increase on shear**.
T = 13.4 ms, t_d/T = 10–100 → quasi-static. Roof total COMB 103 = **448.15 kPa**.
Headhouse roof **396.5 kPa**; headhouse walls **383 kPa either face** (C10).

**Seismic** — box A_h 0.075, V_b 1050 kN (negligible). Sentry A_h 0.100, **R 3.0,
V_b = 73.18 kN** (STAAD value governs; hand check 59.3 kN — see U1). Wind 29.9 kN, seismic governs 2.4:1.

**Key loads** — SIDL 2.0 roof / 1.0 mat · floor LL 5.0 · earth+water gradient **15.41 kPa/m**
(33.9 at soffit, 83.2 at floor) · uplift **46.11 kPa = 6289 kN over 136.4 m²** ·
construction surcharge 20 vertical / 10 lateral · staircase on W6+W7 2.947 kPa.

**Combinations** — box 101 / 102 / **103 BLAST** / 104 / 105.
Sentry 101–113, 201, 202, **203** (the `.std` has 16; master A.7.9 records 15 — the master's count is short).

---

## Above-ground structures

**Headhouse** — external **13600–18400** × 200–6000 (4800 × 5800); internal **14000–18000** ×
600–5600 (4000 × 5000); walls 400, roof 500, top +0.900, **no earth cover**; floor = top of the
900 slab at −2.000; clear 2400. Inner security door 900 × 2100 in HW2 at **14450–15350**, not
blast rated. HW3 (west) has no wall under it — line load on the slab, 26 % / 41 %.

**Covered entry stairwell** — external **9250–16050** × 5750–7750 (6800 × 2000); internal
**9500–15800** × 6000–7500 (6300 × 1500); walls 250. Top landing 9500–11000 at 0.000 ·
flight **11000–14300**, 12R @ 166.6667 / 300 (11 goings × 300 = 3300), waist 250 · platform
**14300–15800** at −2.000. Roof 250 raking, soffit 2200 above the flight. Entry door 1000 × 2100
at grade; 300 channel + grating at 8950–9250. Stepped raft 300; **movement joint at the headhouse**.
**Outside the protective boundary, not blast rated, declared expendable.**

**Escape shafts** — **ESC 1 (2050, 2050)** head +0.150 · **ESC 2 (19900, 2050)** head +0.700.
Both 1400 dia clear, 250 RC collar, OD 1900. **750 mm clearance rule** (opening edge to wall
face) — a bay must be ≥ 2900 wide to hold one. M1 improved ESC 2 to headhouse clearance 350 → **550**.

---

## Main staircase — FROZEN, do not change

Bay 7. **24R @ 170.8333 · tread 280 · 3 flights × 8 · total rise 4100.**
Flight A (flights 1 and 3, stacked) **15300–16500** · well **16500–16700** (200) ·
flight B **16700–17900**. Both flights **1200** wide. Waist 200.
Landing L1 −4.7333 (Y 3760–4960) · L2 −3.3667 (Y 600–1800) · arrival −6.100 (Y 600–1800, = mat
surface) · store under L1 (Y 4960–5600). **Headroom 2533.** Inside the protective envelope,
**not** a blast element — designed to IS 456 with normal partial factors.

---

## Sentry post — unaffected by M1

4000 × 5000 external, 3600 × 4600 internal. Grid A–B **3650** c/c (A x 175, B x 3825),
1–2 **4650** c/c (1 z 175, 2 z 4825). C1 **350 × 350** ×4 · B1/B2 **250 × 450** · S1 **150**
two-way · PB 250 × 400 at +0.450 · F1 **1500 × 1500 × 600** on in-situ basalt at −2.000.
Ground storey 200 RC ballistic infill (**SUPERSEDED by SP-B1 — see below**);
first storey armoured vision panels 1200 wide.
Spiral stair 1000 R / 250 pole. **≥ 10 m clear of the shelter excavation. Not blast designed —
a recorded decision.**

**SP-B1 — sentry post walls are BRICK MASONRY** (7 Sep 2026, master H.10 / A.4.8 note).
190 one-brick modular brickwork to **IS 1077** in **CM 1:6**, inside the **unchanged 200
structural zone**; 10 mm taken up at the internal face in the plaster, so the confirmed
4000 × 5000 envelope and flush column faces are preserved. Panel height **2.600** (the
project's own confirmed figure, A.7.7). **12.20 m³ / 64.19 m² · ≈ 6 400 bricks.**
Openings: ground D1 900 + W1 1200; first storey 8 vision panels 1200 + D1 900.
**Nothing else in the sentry post changed. A.7.8, B.8 and F.4 are untouched.**
Four consequences, all OPEN: lintels now needed and **no lintel design exists** (WM-V5);
wall ties now needed and **no detail exists** (WM-V11); seismic weight falls to ≈ 9.9 kN/m
from 13.000, so V_b = 73.18 kN is **conservative — a direction, not a verification**
(WM-V6); **brick does not give the ballistic protection the Rev F panels were named for**
(WM-V7).

---

## Key reinforcement

| Element | Main | Links | Util. |
|---|---|---|---|
| **Roof slab** 900 | T25 @ 150 EF EW | T12 4L @ 250 end 1500 / 2L @ 300 mid | 51 % |
| **Perimeter walls** 600 | T16 @ 150 EF EW | T12 closed @ 200 | 68 % |
| **W6 / W7** 400 | T20 @ 150 EF EW | T12 4L @ 200 | 69 % |
| **Mat** 600 | T16 @ 150 EF EW | T12 @ 250 × 250 grid | **84 %** |
| **HH roof** 500 | T20 @ 150 EF EW | T12 4L @ 175 end 1200 / @ 250 | **90 %** |
| **HH walls** 400 | T16 @ 150 EF EW | T12 4L @ 250 | 59 % |
| Main stair flight / landings | T12 @ 150 / T12 @ 125 | — | 52 % / 84 % |
| Entry stairwell flight | T16 @ 200 | — | 75 % |
| Sentry S1 | T8 @ 150 B/W + T8 @ 300 edge top + **T8 @ 200 torsion, 4 layers, 700² at all 4 corners** | — | 69 % |
| Sentry B1 / B2 | 4-T16 / 2-T16 · 3-T20 / 2-T20 | T8 @ 100 over 2d, @ 150 elsewhere | 84 % / 89 % |
| Sentry C1 / F1 | 8-T16 · T12 @ 150 B/W | T10 hoops + cross-ties @ 85 over 500 | biaxial 0.819 |

Blast door jambs 4-T20 each jamb each face; ESC collars 5-T25 each side/face/direction;
stair-void free edge thickened 900 → 1200 with 6-T25 top + bottom.

---

## Current assumptions (all `[ASSUMED]` — confirm before construction)

- **GWT −2.000** — the single most important number; water is ⅔ of the lateral load. Needs monsoon monitoring.
- **k_s 100 000–500 000 kN/m³ — the master requires BOTH bounds be run. Only 100 000 exists.**
- Rockhead −1.5/−2.0 · SBC 3240 kPa · γ 20 / 21 · K₀ 0.50 · K_a 1.0 saturated.
- Soak-pit absorption 20 L/m²/day — **percolation test mandatory**, likely to fail on basalt.
- Sentry infill not separated from the frame → R = 3.0.

## Remaining unresolved

| Ref | Item |
|---|---|
| **C16** | **Roof / platform junction.** A.4.7 says "over the platform it becomes the 500 headhouse roof"; B.6, A.7.6 and F.2 design, load and register a **250** roof, and the headhouse (Y 200–6000) does not overlap the platform (Y 6000–7500). Model built at 250; **the A.4.7 clause is untouched and needs the user's ruling.** |
| U1 / C9 | Sentry V_b 73.18 (STAAD) vs 59.3 (hand). Design uses 73.18. The `.std` now prints W = 731.80 kN; gap traced but **not closed** — needs confirmation. |
| U2 · U3 | Is a direct hit a requirement? · DBT yield. Both need client / military sign-off. |
| U8 | Roof projection + parapet 4.162 kN/m not independently reproducible. |
| **C17** | **Engineered cover.** A.7.3 states **40.65 kPa**; its own column sums to **39.15**. 40.65 held (larger, and the value in every `.std`). **No reinforcement effect.** Raised by SC1 — needs a ruling. |
| **C18** | **Sump-pit base.** F.1 + the levels give **400**; sheet S-06 text says **300**. 400 held. Raised by SC1 — needs a ruling. |
| **C19** | **Soak pit 2.3 % short.** S-06 prints "22.0 m² OK" against its own "22.5 m² required"; π × 2.0 × 3.5 = **21.99**. Not resized — the percolation test may move it further. Raised by DR1 — needs a ruling. |
| **C20** | **S-06 carries the Rev E stairwell catchment** (0.10 L/s open cut). At Rev F the approach is covered and the catchment with the door shut is zero. Conservative. Raised by DR1 — needs a ruling. |
| **C21** | **Filter duty 250 vs 300 m³/h.** Master A.3 says "2 × 250"; S-06 states 300 in nine places, and **250 fails S-06's own 264 m³/h FEMA criterion**. HV1 uses 300. Raised by HV1 — **needs a ruling**. |
| **WM-V1…12** | **Twelve verification items raised by WM1, all OPEN.** Four from SP-B1 (WM-V5 lintel design, WM-V6 seismic weight, WM-V7 ballistic function, WM-V11 wall ties); eight on measurement. See `WORKS MANAGEMENT/Documentation/WM_ASSUMPTIONS_AND_VERIFICATION_REGISTER.md`. |
| **13 gaps** | **Information the project does not contain**, each dated against the WM1 programme. Largest: **no electrical design package exists** — scope confirmed, design absent, every electrical quantity 'to be verified from final measurement'. Also: no site plan, no sentry lintel or tie detail, blast door and blast valve vendor data, service-entry plate size, duct penetration schedule, EMP enclosure and vision panel specs, sentry GF slab, finish products, W5 door D-05. |

---

## File inventory

**`Revit/` — Phase 1 + 1B BIM build (BIM-P1/BIM-P1B, 3 Sep 2026, master H.6/H.7):**
6 Dynamo Python scripts (`Revit/scripts/`) that build the structural envelope
(levels, grids, main box, headhouse, entry stairwell, main staircase, sentry post
frame) when run inside Revit 2026 — **no `.rvt` exists, Revit is not executable in
this environment.** Rerun-safe since BIM-P1B (Mark-guarded, no duplication on a
second run). Sentry post site position is ASSUMED (no coordinate exists in the
project) and, since BIM-P1B, derived live from the SA/S1 grids by script 06 rather
than duplicated as a constant — see `Revit/docs/00_README_WORKFLOW.md` and
`Revit/docs/02_QAQC_and_discrepancies.md`. C16 reviewed and deliberately left open
(does not block the rest of the structural model).

**`current/cad/` — 11 DXF:** ten Rev F input drawings (directly editable) + `06_Underground_Plan_Services_Sump_BlastValves.dxf` = **sheet S-06**, the only output sheet present.
**`current/staad/` — 3 STD:** underground plate model, sentry frame, entry stairwell frame.

**`Structural CAD/` — reinforcement package, revision SC1 (4 Sep 2026, master H.8):**
**30 A1 DXF reinforcement drawings** (R-001…R-805, AutoCAD 2010 ASCII, validated 0 errors),
**92 bar marks / 70.46 t** of schedules, design basis and element-design calculations, an
independent recomputation of **212 Part B values** (211 agree), IS 456 and IS 13920 compliance
matrices, QA/QC and legibility reports, and 17 Python generators (`Scripts/build_all.py` rebuilds
everything). **Sentry post completely excluded. No column sheets — no RC column exists.**
Raised **C17** and **C18**; **C16 left open**. **Not construction-ready** — 13 items need
engineering review. **Design values in Parts A/B/F/L unchanged.**
**`Drainage/` `HVAC/` `Schedule of Finishes/` — services and finishes packages, revisions
DR1 / HV1 / FN1 (5 Sep 2026, master H.9):** **20 A1 DXF** (D-001…D-305, M-001…M-203, A-601/611/612)
plus **two two-page A4 handouts** — **24 DXF in all, AutoCAD 2010 ASCII, validated 0 errors**;
20 schedules; two calculation sets (17 and 14 sections); three QA/QC reports; three Revit scripts
that **extend the existing model** and create nothing; and `MEP_AND_FINISHES_COORDINATION.md`.
**S-06's ventilation and services basis was reproduced from first principles — twelve figures check,
one does not (C19).** Sentry post completely excluded. Main staircase untouched. **No existing design,
drawing or model file was modified** — only this file and master H.3 / H.9 / I.2 / K.1. Raised **C19, C20, C21**; **C16 left open**. **Not construction-ready.**
The shared sheet library subclasses `Structural CAD/Scripts/sc_dxflib.py`, so the sheet standard
matches the R-series.

**`WORKS MANAGEMENT/` — Works Management package, revision WM1 (7 Sep 2026, master H.10):**
the whole project from mobilisation to handover. **279 activities · 18 milestones · 404
logic links · 326 working days, 2 Nov 2026 → 20 Nov 2027 · six-day week.** Eight principal
deliverables (WBS · BOQ · Resource Plan · Procurement Plan · QA/QC Plan · Safety & Risk
Register · Codes & References · **44-page handout PDF**), the master programme in **MSPDI**
(`.xml`) plus a **7-sheet A3 programme drawing** and a `.csv` task list, five supporting
documents, ~800 lines of quantity derivation, and **65 executed consistency checks, all
passing**. `Scripts/wm_build_all.py` regenerates everything from two source files.
**No `.mpp`** — Microsoft Project's binary format is writable only by Microsoft Project
(verified against MPXJ 16.7.0); MSPDI is Microsoft's own schema and *Save As → .mpp* is one
step. **No design file was modified** — only this file and master H.3 / H.10 / I.2 / K.1
plus preserving notes at A.4.8 and A.7.7.

**`master/`** — `MASTER_PROJECT_STATE.md` (authority), `MASTER_PROJECT_STATE.pdf`, this file.

**Changed in the M1 reconciliation (9):**
`1_Underground_Level_Plan.dxf` · `2_Side_Section_with_Stairs.dxf` ·
`2_Ground_Plan_Headhouse_Berm.dxf` · `3_Headhouse_Section_Cutaway.dxf` ·
`5_Entry_Headhouse_Stair_Section.dxf` · `5_Front_Elevation.dxf` ·
`Underground_Structure_WITH_LOADS_worked_example (4).STD` · `Entry_Stairwell.std` ·
`MASTER_PROJECT_STATE.md`

**Intentionally untouched (7), byte-identical:**
`1_Staircase_Section.dxf` (staircase frozen) · `3_Sentry_Post_Ground_Floor_Plan.dxf` ·
`4_Sentry_Post_First_Floor_Plan.dxf` · `6_Sentry_Post_Framing_Plan.dxf` ·
`Sentry_Post_Framed_Seismic.std` (checked, already correct) ·
`06_Underground_Plan_Services_Sump_BlastValves.dxf` (already at M1) ·
`MASTER_PROJECT_STATE.pdf`

---

## Limitations — state these, do not paper over them

- **WM1 ran no analysis and changed no design.** Every output rate and vendor lead time in the programme is `[A]`. The main staircase is unchanged.
- **STAAD.Pro was NOT executed in Claude Code.** Both models were reconciled and verified
  *structurally and numerically against the master*. No analysis was run and no results exist.
- **Sheets S-01…S-05, S-07, S-08 cannot be regenerated** — the Part E.4 Python toolchain
  (`proj.py`, `dxflib.py`, `d01_wall.py`…`d08_sentryslab.py`, `validate.py`, `render.py`) is not
  in the workspace, and rule M.12 forbids editing a generated DXF directly.
- **`MASTER_PROJECT_STATE.pdf` is a stale render** of the pre-reconciliation `.md`.
- **Second k_s bound (500 000) outstanding.**
- **Phase 3 not started:** non-linear SDOF support rotation, shock propagation down the entry
  shaft, transient soil–structure interaction, blast-door vendor testing, sentry sheet S-09.
- A static STAAD run gives **demand**, never proof of blast resistance. Flotation can never be
  read off the model — the springs take tension; it is a hand check (master B.3).
