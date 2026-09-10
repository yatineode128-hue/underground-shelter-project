# QUICK_STATE — current implemented project state

**Orientation digest, not an authority.** `MASTER_PROJECT_STATE.md` governs. Where this file
and the master disagree, the master is right and this file is stale.
Compiled 3 Sep 2026 from the master (Parts A, B, F, L) plus the M1 reconciliation (Part H.4).
Updated 5 Sep 2026 for the DR1 / HV1 / FN1 packages (Part H.9).
Updated 7 Sep 2026 for the Works Management package WM1 (Part H.10).
Updated 9 Sep 2026 for the drawing QA/QC pass QA1 (Part H.11).
Updated 10 Sep 2026 for revisions **BS1** and **SP-B2** (Part H.12) and for Works
Management **WM2** (Part H.13).
Updated 10 Sep 2026 for **RC1** (Part H.14) — **every inconsistency that could be ruled
on the evidence has been ruled**; six items needing outside information stay open in K.1b.

---

## Identity and revisions

| | |
|---|---|
| Project | Underground CBRN-hardened, blast-resistant protective structure + sentry post, Pune |
| Objective | 9 occupants, 96 h, nuclear air-blast DBT, with CBRN / EMP / fallout hardening |
| Architectural | **Rev F** · Design report **Rev D** · Structural **Phase 2 Rev A + M1** |
| Services packages | Drainage **DR1** · HVAC **HV1** · Schedule of Finishes **FN1** (5 Sep 2026, master H.9) |
| Works Management | **WM1** (7 Sep 2026, master H.10) — whole project, mobilisation to handover |
| **Works Management** | **WM2** (10 Sep 2026, master H.13) — **THE OWNER'S OWN BOQ, COST ESTIMATE AND MASTER CONSTRUCTION SCHEDULE R0 NOW GOVERN.** ₹3,00,33,306 · 130 activities · 224 working days · 02-11-2026 to 26-07-2027. WM1 is preserved, not overwritten |
| **Works Management — revised** | **WM3** (10 Sep 2026, master H.15) — the **RC1 rulings applied** to the owner's own BOQ, estimate and schedule and published alongside the originals as `.xlsx`/CSV/MD. Burster 300 M35 → **200 M30**; escape shaft collars and the 15 kVA generator **added**; 13 programme activities reworded. **Revised final cost ₹2,97,90,913** — a **LOWER BOUND**, the generator is deliberately unpriced (**no rate invented**). `USER_SOURCE/` untouched |
| **Concealment** | **CAM2** (10 Sep 2026, master **H.18**) — the CAM1 policy **moved out of `WORKS MANAGEMENT/` into its own package `Site and Concealment/`** and **drawn as `C-101`, the above-ground signature elevation**. Text unchanged. Its finding: **the shelter is concealed, the installation is not** — sentry post **+7.000**, headhouse **+0.900 with no earth cover**, stairwell **+2.450**, gooseneck **+1.500**. The 300 turf is the concealment layer, re-laid from the site's own stockpile, and the cover is drained with **no pipe, so no manhole or gully breaks the roof**. **No net, paint or screen is specified anywhere and none is invented**; `B-camo` has no rate. **No concealment LAYOUT can be drawn — there is no site plan (D3)**, so C-101 shows the sentry post beyond a break at no fixed distance. Open items **CAM-V1…V4**, plus **CAM-V5** which the drawing raised: **SH-2 has no recorded head level anywhere** |
| **Fire** | **FS2** (10 Sep 2026, master **H.18**) — the FS1 plan **moved out of `WORKS MANAGEMENT/` into its own package `Fire and Life Safety/`** and **drawn as `F-101` and `F-102`, the escape plans**. Governing fact: **the shelter cannot be ventilated of smoke** — 332.8 m³ at 300 m³/h is **0.9 ACH**, and in Mode 3 CLOSED it is **zero**. Three routes: **R1** main stair, longest travel **14.6 m**; **R2** ESC 1; **R3** ESC 2. Findings **FS-1** W5 has **no door** and R1 has to cross it · **FS-2** Bays 1–6 are **one smoke compartment** · **FS-3** **ESC 2 shares Bay 8 with the generator** · **FS-4** no rule for a fire in Mode 3 · **FS-5** all active measures wait on the **missing electrical design** · **FS-6**, which the drawings raised: **no ladder, rung or fall-arrest in either escape shaft**, and they are **6.250 m** and **6.800 m** climbs. **Blast Doors 1 and 2 are the only two real fire barriers.** Open items **FS-V1…V7** |
| **Drawings** | **QA1** (9 Sep 2026, master H.11) — drafting QA/QC over **all 65 DXF**. Annotation, sheet frames, title blocks. **No engineering design changed** |
| **SP-B1** | **SENTRY POST WALLS = BRICK MASONRY** — instructed design change, 7 Sep 2026. The only design change in WM1 |
| **SP-B2** | **SENTRY POST LINTELS + WALL TIES** — completes SP-B1, 10 Sep 2026 (master H.12 / A.4.8). Closes WM-V5 and WM-V11 |
| **BS1** | **RC BURSTER SLAB LAID TO A 1:50 CROSSFALL** — instructed design change, 10 Sep 2026 (master H.12 / A.7.3). **No load, thickness or `.std` change** |
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
| Engineered cover | 2 000 layered = **40.65 kPa** · **burster slab and everything over it laid to a 1:50 crossfall, crowned on Y 3100, 62 mm each way — BS1** |

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
**This has been a framed structure — columns, beams and infill walls — since Rev F.**
Spiral stair 1000 R / 250 pole. **≥ 10 m clear of the shelter excavation. Not blast designed —
a recorded decision.**

**SP-B1 — sentry post walls are BRICK MASONRY** (7 Sep 2026, master H.10 / A.4.8 note).
190 one-brick modular brickwork to **IS 1077** in **CM 1:6**, inside the **unchanged 200
structural zone**; 10 mm taken up at the internal face in the plaster, so the confirmed
4000 × 5000 envelope and flush column faces are preserved. Panel height **2.600** (the
project's own confirmed figure, A.7.7). **12.20 m³ / 64.19 m² · ≈ 6 400 bricks.**
Openings: ground D1 900 + W1 1200; first storey 8 vision panels 1200 + D1 900.
**Nothing else in the sentry post changed. A.7.8, B.8 and F.4 are untouched.**
Four consequences: lintels now needed (WM-V5) and wall ties now needed (WM-V11) —
**both now DESIGNED, see SP-B2 below**; seismic weight falls to ≈ 9.9 kN/m
from 13.000, so V_b = 73.18 kN is **conservative — a direction, not a verification**
(WM-V6, **STILL OPEN**); **brick does not give the ballistic protection the Rev F panels
were named for** (WM-V7, **STILL OPEN — a client decision, not a drafting one**).

**SP-B2 — lintels and wall ties** (10 Sep 2026, master H.12 / A.4.8). Without these the
walls as recorded **could not be built**.
**Lintel L1, one type over all eleven openings:** 190 × 150, M30 / Fe500, cover 30,
bearing 200 each end, **2-T10 bottom · 2-T8 top · T6 two-legged links @ 150**.
L_eff = min(1315, 1400) = **1.315 m** (IS 456 Cl. 22.2). **Opening heights are not stated
on any drawing (WM-V3, still open)**, so L1 is designed to the bound that does not use one —
masonry just below the 60° arching height 1.139 m, the heaviest case any height can give:
w = 4.33 kN/m, M_u = **1.403** vs M_u,lim **10.03 kNm** (14 % utilised); A_st req 29.5,
**Cl. 26.5.1.1 minimum 37.1 mm² GOVERNS**, 2-T10 = 157 provided; τ_v 0.195 < τ_c 0.56 →
no shear steel, links are the Cl. 26.5.1.6 nominal minimum. **The lintel carries masonry
only** — floor and roof go to B1/B2.
**Wall ties:** 6 mm MS at **every 5th course (≈ 450)** up both column faces, 200 into the
bed joint, 10 mm cast-in or drilled-and-grouted dowel; **top course tight to the beam
soffit, last joint packed — the infill is NOT separated, because the analysis takes
R = 3.0**, not the R = 5.0 special moment frame.
**Nothing else changed:** no frame member, footing, slab, storey height or envelope;
**13.000 kN/m infill retained** in A.7.7 and in `Sentry_Post_Framed_Seismic.std`.
**Carried through the Works Management package** — WM1 said in eleven places that no
lintel design and no tie detail existed; those statements are corrected and the WM1
placeholder of ties *every fourth course* is superseded by the designed **fifth**.
**No WM quantity, rate, date or float changed** (BOQ, WBS and programme CSV are
byte-identical); WM audit still **65/65**.

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
| **C16** | **RULED AT 250 AND CLOSED — RC1, 10 Sep 2026 (master H.14).** A.4.7 used to say "over the platform it becomes the 500 headhouse roof"; B.6, A.7.6 and F.2 design, load and register **250**, and the headhouse (Y 200–6000) does not overlap the platform (Y 6000–7500) at all. **The A.4.7 clause has been corrected.** Every model and drawing already said 250. |
| U1 / C9 | Sentry V_b 73.18 (STAAD) vs 59.3 (hand). Design uses 73.18. The `.std` now prints W = 731.80 kN; gap traced but **not closed** — needs confirmation. |
| U2 · U3 | Is a direct hit a requirement? · DBT yield. Both need client / military sign-off. |
| U8 | Roof projection + parapet 4.162 kN/m not independently reproducible. |
| **RULED BY RC1, 10 Sep 2026 (master H.14)** | **Every conflict that could be decided on the evidence has been decided.** Basis for each in master **K.1** and **K.1c**. |
| **C16** | **RULED AT 250.** A.4.7's "500 over the platform" was one clause against Part B, A.7.6, F.2 **and the geometry** (headhouse Y 200–6000, platform Y 6000–7500 — they do not touch). **A.4.7 corrected.** |
| **C17** | **RULED. 40.65 kPa held; A.7.3 now shows 39.15 layer sum + 1.50 declared allowance**, so the table no longer contradicts itself. COMB 103 stays 448.15 kPa, no `.std` touched, no bar changes. |
| **C18** | **RULED AT 400.** (−)8.000 − (−)7.600 = 0.400 — arithmetic, and F.1 agrees. S-06's "300" is a transcription error. |
| **C19** | **RULED. SK-01 WIDENED 2.0 → 2.200 dia**, depth unchanged: **24.19 m² vs 22.50 required, +7.5 %.** Widened not deepened — deepening drives the pit below the design GWT (−)2.000 where it cannot soak. Percolation test still governs the final size. |
| **C20** | **RULED. Rev F governs** (precedent C1); the 0.10 L/s stays as a **declared conservatism** — removing it changes no pump, pipe or pit. |
| **C21** | **RULED AT 300 m³/h. Master A.3 CORRECTED from "2 × 250".** S-06 says 300 in nine places, every other S-06 figure reproduces only at 300, **250 fails S-06's own 264 m³/h FEMA criterion**, and the owner's estimate prices 2 × 300. |
| **U1** | **CLOSED. 73.18 kN governs.** The model prints W 731.80 and A<sub>h</sub> = 0.1000 exactly; the 139.1 kN gap to the hand check is fully explained (107.9 + 31.1). |
| **U4 · U5 · U6 · U7** | **CLOSED — they were already answered from the `.std` files on 3 Sep and the register was never updated.** *That stale register was itself an inconsistency.* **There is no node 213.** |
| **WM-V1…12** | **Nine CLOSED** (V1 at **2.600**, confirmed twice; V2, V3, V4, V5, V8, V10, V11, V12). **V6, V7, V9 remain open — see below.** |
| **R-1…R-14** | **All fourteen RULED** — master **K.1c** and `WM_RECONCILIATION_REGISTER.md` §9. The three against the owner's documents: **R-1** burster **200 M30** not 300 M35; **R-2** cover **2.0 m** not 4 m; **R-3** roof slab **900** not 1000. |
| **QA-1 · QA-2** | **BOTH RULED.** **QA-1: A0 confirmed** — 880 mm at 1:50 against an A1 area of 821 mm makes A1 impossible, the scale is a measurement statement, and splitting would break a continuous 44 m elevation. **QA-2: accepted as drawn, with the reason stated** — six sheets carry an empty bottom strip, and re-scaling, renumbering and reflowing are each worse than the space. **Every sheet is correct, complete and legible. Combining them stays your call.** |
| **STILL OPEN — master K.1b** | **Eight items, none of them a conflict.** Each is a single position the project holds — or, in the last two, a position it does not hold at all — that needs something from outside: **U2** direct hit (military sign-off) · **U3** DBT yield (client) · **U8** the 4.162 kN/m parapet load (cannot be re-derived until the parapet detail is confirmed) · **WM-V6** seismic re-check (STAAD not available; direction certain and favourable) · **WM-V7** ballistic requirement (client / military decision) · **WM-V9** slope stability (geotech) · **FS-V7** *(new, FS2)* **how either escape shaft is climbed** — 6.250 m and 6.800 m with no ladder, rung or fall-arrest specified anywhere; this one needs a **design**, not a ruling · **CAM-V5** *(new, CAM2)* **SH-2's head level, recorded nowhere**. |
| **13 gaps** | **Information the project does not contain**, each dated against the WM1 programme. Largest: **no electrical design package exists** — scope confirmed, design absent, every electrical quantity 'to be verified from final measurement'. Also: no site plan, **the sentry lintel and tie detail is now SUPPLIED — SP-B2, master A.4.8, so this gap is closed**, blast door and blast valve vendor data, service-entry plate size, duct penetration schedule, EMP enclosure and vision panel specs, sentry GF slab, finish products, W5 door D-05. |

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
**At QA1 all eleven were de-clashed and the ten Rev F drawings were given an A1 (A-301: A0)
border, title block and NOTES box — filenames unchanged, geometry unchanged.** Drawing
numbers A-101…A-105, A-201…A-204, A-301 live in the title blocks; `current/cad/Scripts/`
holds the pipeline that produced this state.
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

**`DRAWING QAQC/` — drawing QA/QC, revision QA1 (9 Sep 2026, master H.11):** the drawing
index for all DXF in the project (**68** after CAM2 / FS2 — 63 A1 · 1 A0 · 4 A4), the QA/QC report, and five inspection
scripts. Package state after the pass: **0 text-on-text overlaps on the 54 generated
sheets, 12 residual items in `current/cad`, 0 entities outside a sheet border, 65 of 65
drawings carrying a title block.** Raised **QA-1** (A-301 cannot plot at 1:50 on A1 —
sheet corrected to A0, ruling invited) and **QA-2** (sheets that do not fill their paper).

**`Fire and Life Safety/` — revision FS2 (10 Sep 2026, master H.18):** **2 A1 DXF**
(**F-101** underground level escape plan, **F-102** entry level escape plan + vertical
escape profile), the **fire safety and evacuation plan**, the escape route schedule
(`.md` + `.csv`) and a DXF validation report (**0 errors**). Five Python generators;
`Scripts/fs_build_all.py` rebuilds the package, and **every travel and climb figure is
computed from `mep_proj.py`, not typed**, so the drawings, the schedule and the plan
cannot disagree. **The plan was in `WORKS MANAGEMENT/Documentation/` until this
revision** — it was never a works-management document. Text moved verbatim; the
drawings added **FS-6 / FS-V7**.

**`Site and Concealment/` — revision CAM2 (10 Sep 2026, master H.18):** **1 A1 DXF**
(**C-101** above-ground signature elevation — a true elevation, equal scales both ways,
of every element standing above finished grade at its confirmed height), the
**camouflage and concealment policy**, and a DXF validation report (**0 errors**). Four
Python generators; `Scripts/cm_build_all.py` rebuilds the package. **The policy was in
`WORKS MANAGEMENT/Documentation/` until this revision.** Text moved verbatim; the
drawing added **CAM-V5**. **No concealment layout is drawn and none can be — there is no
site plan (D3).**

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
- **`MASTER_PROJECT_STATE.pdf` is a stale render.** It is the user-supplied upload of
  **9 September 2026** and there is no generator for it in the workspace, so it cannot be
  refreshed here. It predates **H.12** (BS1 / SP-B2), **H.13** (WM2), **H.14** (RC1),
  **H.15** (WM3), **H.16 / H.17** (CAM1 / FS1) and **H.18** (CAM2 / FS2). **Read the `.md`.**
- **Second k_s bound (500 000) outstanding.**
- **Phase 3 not started:** non-linear SDOF support rotation, shock propagation down the entry
  shaft, transient soil–structure interaction, blast-door vendor testing, sentry sheet S-09.
- A static STAAD run gives **demand**, never proof of blast resistance. Flotation can never be
  read off the model — the springs take tension; it is a hand check (master B.3).
