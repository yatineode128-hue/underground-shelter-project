# MASTER PROJECT STATE FILE
## Underground CBRN-Hardened Blast-Resistant Protective Structure + Sentry Post — Pune, Maharashtra
### Portable memory · Source of truth · Revision record · Reconstruction specification

**Document status:** MASTER STATE, issue 1
**Compiled:** 2 September 2026
**Compiled from:** Phase 1 Design Report Rev D (126 KB, 2000 lines), ten Rev F architectural DXF files, nineteen STAAD.Pro screen captures, and the full Phase 2 structural design work.
**Covers:** Phase 1 (architectural + basis of design, complete) and Phase 2 (structural design + drawings, substantially complete).
**Discipline packages:** Structural CAD **SC1** · Drainage **DR1** · HVAC **HV1** · Schedule of Finishes **FN1** · Works Management **WM1** (7 Sep 2026, Part H.10) + **WM2** (10 Sep 2026, Part H.13 — the owner's own BOQ, cost estimate and master construction schedule R0) + **WM4** (15 Sep 2026, Part **H.38** — **the bill priced from the Maharashtra PWD State Schedule of Rates 2022-23**, which the owner supplied).
**Drawing QA/QC:** **QA1** (9 Sep 2026, Part H.11) — all 65 DXF sanitised in place; **QA2** (11 Sep 2026, Part **H.25**) — the whole package re-scanned at **80 DXF, 74 PASS**, after the twelve sheets EM1 / EL1 / SG1 / SG2 added were found to be invisible to the index tool.
**Latest design changes:** **BS1** (burster slab laid to a 1:50 crossfall) and **SP-B2** (sentry post lintel L1 + wall ties) — 10 Sep 2026, Part H.12.
**Fire:** **FS1** (10 Sep 2026, Part H.17) — a fire safety and evacuation plan; there was none before.
**Concealment:** **CAM1** (10 Sep 2026, Part H.16) — a short camouflage and concealment policy; it did not exist before.
**Owner's package revised:** **WM3** (10 Sep 2026, Part H.15) — the RC1 rulings applied to the owner's own BOQ, estimate and schedule, published alongside the originals.
**Rates:** **WM4** (15 Sep 2026, Part **H.38**) — **the project's first bill priced from a published schedule of rates.** Maharashtra PWD **SSR 2022-23**, 624 pages, supplied by the owner. **No quantity moved**; WM1's measure is used as measured. **Total of items ₹ 15,283,278**, estimated cost **₹ 20,739,408** — **CIVIL WORKS ONLY and a declared lower bound**: the blast doors, hatches, valves, NBC trains, EMP enclosure, generator, sump pumps, commissioning and waterstops **have no SSR item** and are excluded, not estimated. The owner's own rates come out **31.6 % below schedule** on the 21 lines that can be compared. Seven new open items `WM4-V1…V7`.
**Inconsistency register:** **RC1** (10 Sep 2026, Part H.14) — **every conflict that could be decided on the evidence has been ruled**; six items that need information the project does not contain remain open in K.1b.
**EMP:** **EM1** (10 Sep 2026, Part H.19) — the project's first EMP design. **Electrical:** **EL1** (11 Sep 2026, Part H.20) — the project's first electrical design, deliberately basic. **Rulings:** **RC2** (11 Sep 2026, Part H.21).
**Site and ground:** **SG1** (11 Sep 2026, Part **H.22**) — **the project's first site selection and geotechnical section.** Two owner-supplied documents recorded, checked against each other and against this master. **It resolves nothing: not one `K.2` assumption is closed.** Its governing finding — **the sub-soil investigation reached about 1.5 m; the structure founds at (−)6.800** — and the first written **provenance of the design GWT (−)2.000**. Ten new open items `SG-V1…V10`.
**Drainage on the architectural sheets:** **DR-A1** (11 Sep 2026, Part **H.24**) — `SU-01` drawn on `A-202`, `ST-01` and `SK-01` drawn on `A-301` beyond a break. **No design value changed.** It raises **`DR-A1-V1`**: the project holds **two different assumed sentry-post positions**, and the elevation's would stand inside `SG2`'s external works reserve. · **DR-A2** (12 Sep 2026, Part **H.35**) — **`SU-01`'s cover** drawn on `A-202` at (−)6.100, and a **1:200 key plan** on `A-301` putting `SU-01`, `ST-01` and `SK-01` at true project X **and Y**. **No design value changed.** It raises **`DR-A2-V1`**: **the project records a 1500 × 1500 opening through the mat and nothing that closes it**, in a bay 1560 wide.
**Site layout:** **SG2** (11 Sep 2026, Part **H.23**) — **the project's first site layout plan.** On a coordinate and a 50 m envelope the owner supplied, master `H.9`'s *"not determinable"* external works positions, **four of five pipe lengths** and **two of three IS 2470 offsets** are **determined**. Site orientation fixed: **+X = EAST**. Principal finding **`SG2-F1` — the soak pit's problem is DEPTH, not arithmetic**: 21–43 % of its required area is above the design water table and its only permeable horizon is 0.2–0.5 m thick, so the fallback dispersion field is reserved rather than the pit re-sized. **`SG-V9` closed · `SG-V3` ruled · `SG-V5` amended · five new items `SG2-V1…V5` · master gap D3 PARTIALLY closed.**
**Master project report:** **PR2** (13 September 2026, Part **H.37**) — `Project Report/MASTER_PROJECT_REPORT.pdf`, **151 pages, 25 parts, 4 appendices and 57 drawn figures**, the project stated once and in full as a single as-built design, with the engineering science, the calculations, the citations, the soil report, the M35 and M30 mix designs, the openings and closures, the five services parts, works management and an environmental management plan. **It changes no design value**; its 559-check verification pass holds the two PR1 findings **`PR1-F1`** and **`PR1-F2`** and adds two, **`PR2-F1`** and **`PR2-F2`**, all **recorded and NOT corrected**. PR1 (89 pages, 19 parts) is at Part **H.36**.
**A2 presentation sheets:** **SR1** (16 Sep 2026, Part **H.39**) — **two A2 structural reinforcement sheets, `STR006` SHEET 06 (roof slab + mat foundation) and `STR007` SHEET 07 (600 shear wall + main staircase)**, drawn in the frame and title block of the owner's Revit A2 architectural set `ARCH001…ARCH005` so they read as the next two sheets of it. Every bar mark is read from `rebar_data.py`; **no design value, level, thickness, bar or spacing changed** and **the main staircase is untouched**. Finding **`SR1-F1`**: the request asked for IS 13920 detailing; **IS 13920 Cl. 10.4 was checked for the box and is NOT triggered** (τ = 0.063 N/mm²), the box is IS 456 + IS 4991 + IS 3370, and the project's IS 13920 detailing is the **sentry post frame**, which is not on these sheets. Both sheets **PASS** the drafting QA with **zero text overlaps**.
**A2 sentry-post sheets:** **SR2** (16 Sep 2026, Part **H.40**) — **two more A2 sheets in the same series, `STR008` SHEET 08 (sentry post beams B1 / B2 and column C1) and `STR009` SHEET 09 (isolated footing F1 and slab S1)**. **This is the project's IS 13920:2016 sheet pair** — the box is not a ductile-detailing element (Cl. 10.4 checked, not triggered) and the sentry post frame is, so STR008 carries a 14-clause IS 13920 compliance table. **No design value moved and no analysis was run.** Because the sentry post is EXCLUDED from `rebar_data.py`, SR2 builds a separate register `sentry_data.py` to the same rule. Principal finding **`SR2-F1` — the master contradicts itself on B2's top steel at the ROOF joint**: B.8.6 checks that joint with **2-T20** and passes it marginally, F.4 schedules **3-T20 at supports** without distinguishing level, and 3-T20 there makes IS 13920 Cl. 7.2.1 **FAIL** (1.4 ΣM<sub>b</sub> 195.7 > ΣM<sub>c</sub> 101). **Both cannot be true, so SHEET 08 details the FIRST-FLOOR frame only** and the roof frame is left undrawn until it is ruled on. Six further open items `SR2-V1…V6`, plus `SR2-F2` — a legibility finding on the existing sheet STR007, **recorded and NOT acted on**. Both new sheets **PASS** the drafting QA. **Amended the same day as `SR2A` (Part H.40.8), by instruction: the design-basis and declared-decisions panels DELETED from both sheets and `REV A` removed from their header — no view, scale, dimension, bar or count changed, and the schedules were grown to fill the freed column. The open items are unchanged and now live in the master only.**
**A2 header/panel cleanup:** **SR1A** (16 Sep 2026, master **H.41**) — by instruction, on the owner's own copies of `STR006` / `STR007`: the **DESIGN BASIS** panel deleted from both, and the entire revision line (**"STRUCTURAL - PHASE 2 REV A + M1"**) deleted from the header — asked directly which reading was meant, and the whole line was the answer. **No design value moved; STR008/STR009 are byte-identical to before.** The freed column is filled by the `table_stack()` helper SR2A introduced. Found and fixed a real bug in `a2_lib.py` along the way: `table()`'s row-height shrink loop could quantise one step below `MIN_TXT_H`; fixed with a floor clamp, verified not to change STR008/STR009. **This also CLOSES `SR2-F2`**, the STR007 legibility finding recorded and deliberately left unfixed at SR2A. `DRAWING_INDEX.md`: 84 drawings, 78 PASS.
**Next phase:** Phase 3 — non-linear SDOF verification, site investigation close-out, and a ruling on **`SR2-F1`** before the sentry post roof beams can be detailed.

---

## ⚠ EVIDENCE-CLASS LEGEND — APPLIED THROUGHOUT THIS DOCUMENT

| Tag | Meaning | How a future Claude must treat it |
|---|---|---|
| **[CONFIRMED]** | Read directly from an uploaded file, or computed in this project from confirmed inputs | Use as fact |
| **[RECONSTRUCTED]** | Derived by back-calculation from partial evidence (e.g. STAAD statics-check output) | Use, but state the derivation when relied on |
| **[ASSUMED]** | Engineering assumption, no test or client confirmation | Must be re-confirmed before construction |
| **[UNRESOLVED]** | Two or more conflicting values, insufficient evidence to choose | **DO NOT GUESS. Ask the user.** |
| **[NOT AVAILABLE]** | Information does not exist in any uploaded material | **DO NOT INVENT** |

---

# PART A — CURRENT AUTHORITATIVE PROJECT STATE

> **Everything in Part A is the LATEST VALID DESIGN. If any uploaded file disagrees with Part A, stop and raise the conflict before proceeding.**

## A.1 Project identity

| Field | Value | Class |
|---|---|---|
| Project title | Underground CBRN-hardened, blast-resistant protective structure with associated sentry post | [CONFIRMED] |
| Location | Pune, Maharashtra, India | [CONFIRMED] |
| Project type | Buried reinforced-concrete protective structure, military-operational, for actual construction | [CONFIRMED] |
| Academic context | B.E. Civil Engineering, final semester, three-presentation capstone | [CONFIRMED] |
| Objective | Protect 9 occupants for 96 h against a nuclear air-blast design basis threat with CBRN, EMP and fallout hardening | [CONFIRMED] |
| **Architectural revision** | **Rev F** (the ten uploaded DXF files) | [CONFIRMED] |
| **Design report revision** | **Rev D** (older than the drawings — this is the single largest reconciliation issue) | [CONFIRMED] |
| **Structural revision** | **Phase 2 Rev A**, incorporating **Modification M1** | [CONFIRMED] |
| Presentation status | P1 (preliminary/architectural) delivered. **P2 (AutoCAD + STAAD + manual calculations) is the active deliverable.** P3 not yet scoped | [CONFIRMED] |
| Software in use | STAAD.Pro (Bentley), AutoCAD/DXF, plus a purpose-built dependency-free Python DXF toolchain (see Part F) | [CONFIRMED] |
| Presentation window | ~90 minutes, mixed academic + military audience | [CONFIRMED] |

## A.2 Overall configuration

**Three separate structures:**

1. **Main underground box** — buried RC shelter, 8 bays, 22.0 × 6.2 m external, roof 2.0 m below grade.
2. **Entry headhouse + covered approach stairwell** — above-ground bermed RC, sitting on the shelter roof and on adjacent fill.
3. **Sentry post** — a separate two-storey RC framed building, **≥ 10 m clear** of the shelter excavation, on its own footings on in-situ rock. **Not blast designed** (declared expendable).

**Access / egress:**
- **Primary:** grade → covered entry stairwell (12R @ 166.667/300) → platform (−2.000) → inner security door → headhouse → stair void → main dog-leg stair (24R @ 170.833/280, 3 flights × 8) → arrival landing (−6.100) → **Blast Door 1** (1200 × 2100, 7 bar) into Bay 6.
- **Secondary:** **Blast Door 2** (1200 × 2100) from the stair shaft into Bay 8 (generator/grey zone).
- **Emergency:** two 1400 mm dia vertical escape shafts, **ESC 1** and **ESC 2**, with 250 mm RC collars, in Bays 1 and 8.

> **PROTECTIVE BOUNDARY = Blast Doors 1 and 2 at level (−)6.100, plus walls W6/W7, the perimeter walls, the mat and the pressure slab. Everything above the blast doors (stair shaft, headhouse, entry stairwell) is OUTSIDE the boundary and the entry stairwell is DECLARED EXPENDABLE.**

**Gas-tight envelope = Bays 1 to 6 only** — 67.8 m² floor, 217.0 m³ volume. Bays 7 (stair shaft) and 8 (generator, "grey zone") are outside it.

## A.3 Bay schedule — CURRENT (after Modification M1)

| Bay | X range (mm) | Clear width | Use |
|---|---|---|---|
| 1 | 600 – 3500 | 2900 | Emergency stores, 1000 L potable tank, **ESC 1** |
| 2 | 3610 – 5410 | 1800 | Lavatory (1800×2000) + medical (1800×3000) |
| 3 | 5520 – 9020 | 3500 | Ops room & hazard plotting; **EMP Zone 2 enclosure** |
| 4 | 9130 – 10930 | 1800 | Berthing, 3 × 3-tier bunks, 9 berths |
| 5 | 11040 – 12600 | 1560 | CBRN plant: **2 × 300 m³/h** filters (**RC1 ruling — was "2 × 250", see C21 / K.1 U13**), CO₂/O₂, dehumidifier, **sump** |
| 6 | 12800 – 14800 | 2000 | Decon airlock, 3 stages (2000×2000, 2000×1500, 2000×1500) |
| 7 | **15200 – 18000** | **2800** | **Stair shaft** (shifted +200 by M1) |
| 8 | **18400 – 21400** | **3000** | Generator 15 kVA (grey zone), **ESC 2** at X 19900 |

**Internal wall positions — CURRENT:**

| Mark | X range (mm) | Thickness | Notes |
|---|---|---|---|
| W8 partitions ×4 | 3500–3610, 5410–5520, 9020–9130, 10930–11040 | 110 | Each with a 900 door gap at Y 2500–3400 |
| W5 | 12600 – 12800 | 200 | Bay 5/6, fire + gas-tight only, no pressure differential |
| **W6** | **14800 – 15200** | **400** | **Bay 6/7 — MOD M1, was 200. Protective boundary.** Blast Door 1 opening Y 600–1800 |
| **W7** | **18000 – 18400** | **400** | **Bay 7/8 — MOD M1, was 200. Protective boundary.** Blast Door 2 opening Y 600–1800 |

## A.4 Geometry — CURRENT AUTHORITATIVE VALUES

### A.4.1 Coordinate system (used by every DXF and every calculation in this project)

```
ORIGIN      = south-west EXTERNAL corner of the underground box, at ground level
X           = east   (along the length, 0 to 22000)
Y (plan)    = north  (across the width, 0 to 6200)
LEVELS      = metres relative to finished site grade 0.000, negative downwards
UNITS       = millimetres in all DXF geometry; metres in all level annotation
```

### A.4.2 Main box

| Item | CURRENT value | Was | Class |
|---|---|---|---|
| **External length** | **22 000 mm** | 21 600 (pre-M1) | [CONFIRMED] |
| External width | 6 200 mm | unchanged | [CONFIRMED] |
| **Internal length** | **20 800 mm** | 20 400 | [CONFIRMED] |
| Internal width (clear span of the roof) | **5 000 mm** | unchanged — **do not widen** | [CONFIRMED] |
| Perimeter wall thickness | 600 mm | unchanged | [CONFIRMED] |
| Roof (pressure) slab | 900 mm | unchanged | [CONFIRMED] |
| Mat foundation | 600 mm | unchanged | [CONFIRMED] |
| Blinding / PCC | 100 mm M15 | unchanged | [CONFIRMED] |
| Internal clear height | 3 200 mm | unchanged | [CONFIRMED] |
| Engineered cover over roof | 2 000 mm layered | reduced from 4 000 in an earlier revision | [CONFIRMED] |

### A.4.3 Level schedule — CURRENT

| Level | Value | Description |
|---|---|---|
| Grade | **0.000** | Finished site level, crowned, falls 1:50 away |
| Top of pressure slab | **(−)2.000** | = headhouse floor level |
| Roof soffit | **(−)2.900** | 900 slab |
| Internal floor / top of mat | **(−)6.100** | 3200 clear height |
| Underside of mat | **(−)6.700** | 600 mat |
| Formation / underside of PCC | **(−)6.800** | 100 blinding |
| **Design groundwater table** | **(−)2.000** | monsoon [ASSUMED — requires monsoon monitoring] |
| Rockhead | (−)1.500 to (−)2.000 | [ASSUMED] |
| Stair landing L1 | (−)4.7333 | 8 risers up from floor |
| Stair landing L2 | (−)3.3667 | 16 risers up from floor |
| Headhouse roof soffit | **+0.400** | 2400 clear internally |
| Headhouse roof top | **+0.900** | no earth cover; berm graded to this level |
| Entry stairwell roof at head | **+2.450** | soffit +2.200 |
| Sentry post GF FFL | **+0.450** | = base of the STAAD model |
| Sentry post first floor | **+3.650** | storey height 3200 |
| Sentry post roof | **+6.700** | storey height 3050 |
| Sentry post parapet top | **+7.000** | |
| Sump pit invert | (−)7.600 | pit base slab (−)8.000 |

### A.4.4 Stair shaft, void and pad — CURRENT (post-M1)

```
Stair shaft (Bay 7) clear      X 15200 – 18000   Y  600 – 5600   = 2800 × 5000
Void in the pressure slab      X 15200 – 18000   Y  600 – 3760   = 2800 × 3160
Cantilever pad (remaining slab) X 15200 – 18000  Y 3760 – 5600   = 2800 × 1840
Flight A (flights 1 and 3, stacked) X 15300 – 16500   (1200 wide)
Well                                X 16500 – 16700   (200)
Flight B (flight 2)                 X 16700 – 17900   (1200 wide)
Landing L1 (−)4.7333   Y 3760 – 4960, full 2800 width
Landing L2 (−)3.3667   Y  600 – 1800, full 2800 width (stacked over the arrival landing)
Arrival landing (−)6.100 = the mat surface, Y 600 – 1800
Store under landing L1  Y 4960 – 5600
Main stair: 24R @ 170.8333, tread 280, 3 flights × 8R, total rise 4100, headroom 2533
```

### A.4.5 Escape shafts

| | ESC 1 | ESC 2 |
|---|---|---|
| Centre | (2050, 2050) | **(19900, 2050)** — shifted +400 by M1 |
| Clear opening | 1400 mm dia | 1400 mm dia |
| Collar | 250 mm RC, OD 1900 | 250 mm RC, OD 1900 |
| Clearance, opening edge to wall face | 750 mm all round | 800 / 800 mm |

> **THE 750 mm CLEARANCE RULE.** Opening edge to structural wall face ≥ 750 mm = 250 collar + ~400 trimmer band + 100 tolerance. **A bay must therefore be at least 1400 + 2 × 750 = 2900 mm wide to hold an escape shaft.** This rule drove the Rev C lengthening and it is why Modification M1 could not take 400 mm out of Bay 8.

### A.4.6 Headhouse — CURRENT (shifted +200 by M1)

```
External     X 13600 – 18400   Y  200 – 6000   = 4800 × 5800
Internal     X 14000 – 18000   Y  600 – 5600   = 4000 × 5000
Walls 400 thk (HW1 south, HW2 north, HW3 west, HW4 east)
Roof  500 thk, soffit +0.400, top +0.900, NO earth cover
Floor = the top of the 900 pressure slab, (−)2.000
Clear internal height 2400
Inner security door 900 × 2100 in HW2 (north), at X 14450 – 15350.  NOT blast rated.
Berm graded against all four walls to +0.900 at 1.5 : 1
```

**Load path of each headhouse wall — [CONFIRMED, checked in Phase 2]:**

| Wall | Runs | Length | Sits over |
|---|---|---|---|
| HW1 south | in X | 4000 | Box south perimeter wall — direct ✔ |
| HW2 north | in X | 4000 | Box north perimeter wall — direct ✔ |
| **HW3 west** | in Y | 5000 | **Bay 6, mid-slab. NO wall below — line load on the pressure slab, checked at 26 % (two-way) / 41 % (one-way bound)** |
| HW4 east | in Y | 5000 | **Wall W7 (18000–18400). M1 made these align exactly** ✔ |

### A.4.7 Covered entry stairwell — CURRENT (Rev F, shifted +200 by M1)

```
External     X  9250 – 16050   Y 5750 – 7750   = 6800 × 2000
Internal     X  9500 – 15800   Y 6000 – 7500   = 6300 × 1500
Walls 250 RC (both sides, headwall, east wall)
Top landing   X  9500 – 11000  at 0.000, 250 thk
Flight        X 11000 – 14300, 12R @ 166.6667, going 300, 11 goings × 300 = 3300, waist 250
Platform      X 14300 – 15800  at (−)2.000, 1500 × 1500, 250 thk
Roof 250 RC raking, soffit 2200 above the flight; **it stays 250 over the platform**
  (**RC1 ruling — C16. The clause used to read "over the platform it becomes the 500
  headhouse roof", which no other part of the project supported: B.6 designs a 250
  roof, A.7.6 loads one, F.2 registers one, and the headhouse footprint Y 200–6000
  does not reach the platform at Y 6000–7500 at all.**)
Entry door 1000 × 2100 at grade in the headwall (X 9250 – 9500), opens outward
300 mm channel + grating full 1500 width at X 8950 – 9250
Stepped RC raft 300 thk on compacted fill; MOVEMENT JOINT where it meets the headhouse
1.0 m³ external sump at the platform, own soakaway
Berm 1.5:1 against the walls to +0.900, toe at grade over 1350
```

### A.4.8 Sentry post — CURRENT [all CONFIRMED from the Rev F DXFs]

```
External plan          4000 × 5000        Internal 3600 × 4600
Column grid            A–B  3650 c/c (X)  ·  1–2  4650 c/c (Y)
Grid coordinates       A: x = 175   B: x = 3825   |   1: z = 175   2: z = 4825
Columns C1             350 × 350, 4 No., both storeys
Beams B1               250 × 450, spanning A–B (3650 c/c), on grids 1 and 2
Beams B2               250 × 450, spanning 1–2 (4650 c/c), on grids A and B
Slab S1                150 thk two-way, 3650 × 4650 c/c, both floors
Plinth beam PB         250 × 400 at +0.450
Footings F1            1500 × 1500 × 600, 4 No., on in-situ basalt at (−)2.000
Ground storey infill   200 RC ballistic panels
First storey infill    armoured vision panels, 1200 wide
Spiral stair           external, 1000 R, 250 dia central pole
Door D1                900
Storey heights         ground 3200 (+0.450 → +3.650), first 3050 (+3.650 → +6.700)
Siting                 >= 10 m clear of the shelter excavation
Site position          X 32000 - 36000,  Y 600 - 5600   [A] -- RC4, see below
```

> **U4 RULED — THE EAST POSITION IS ADOPTED, 11 September 2026 (RC4, Part H.28).** The project
> held **two** contradictory assumed positions; it now holds **one**. `A-301`'s own note 2 sets
> **X 32000 – 36000** — 4000 wide, which is the post's actual external dimension. (**`RC4-F1`:
> master DR-A1-V1 recorded this as X 31700 – 36300, which is 4600 and matches nothing. The
> drawing is the primary source and is corrected here.**) **An elevation cannot give a Y**, so
> **Y 600 – 5600, centred on the box longitudinal centreline Y 3100**, is set by RC4 — 5000
> deep, the post's other external dimension.
>
> **`RC4-F3` — AND IT FAILS THE RULE AS WRITTEN.** *"≥ 10 m clear of the shelter EXCAVATION"*:
> X 32000 is 10.00 m clear of the **box face** at X 22000, but the **excavation** face with its
> 1000 mm working space is at X 23000 — giving **9.00 m**. `A-301`'s note cites the excavation
> rule while applying the box face. Satisfying it as written moves the post to
> **X 33000 – 37000**, which passes every check. **BOTH readings are recorded and NEITHER is
> adopted over the other: the EAST position is a drawing convention, not a survey coordinate,
> and `U4` STAYS `[ASSUMED]`.**
>
> **Consequence.** SG2's fifth reason for +X = east was *"the sentry post covers the approach
> from the north"*. With the post 10 m beyond the **far** end of the box it covers nothing —
> the approach is at the **west** end. No stated rule fails, but **the EAST position costs the
> sentry post its stated function**, and a reviewer will ask. `[C] owner ruling / [A] position`

> **SP-B1 — WALLS CHANGED TO BRICK MASONRY, 7 September 2026 (Part H.10).** The Rev F text
> above is preserved unaltered. By instruction, the **ground storey "200 RC ballistic
> infill" is now 190 mm one-brick modular brickwork to IS 1077 laid in CM 1:6**, built
> inside the **unchanged 200 mm structural zone** between the column faces, with the
> residual 10 mm taken up at the internal face in the plaster. **Every other value in this
> block — the 4000 × 5000 external envelope, 3600 × 4600 internal, the A–B / 1–2 grid, C1,
> B1, B2, S1, PB, F1, the storey heights, the spiral stair and the siting rule — is
> UNCHANGED.** The armoured vision panels remain vision panels; they are openings in the
> wall, not wall construction. Consequences (lintels now required, ties now required,
> seismic weight reduced, ballistic function lost) are recorded in H.10 as **WM-V5, WM-V11,
> WM-V6 and WM-V7** and **none of them is resolved.** `[C] instruction / [A] 190-in-200`

> **SP-B2 — LINTELS AND WALL TIES FOR THE MASONRY INFILL, 10 September 2026 (Part H.12).**
> SP-B1 made the walls masonry but left **WM-V5 (no lintel design exists)** and
> **WM-V11 (no tie detail exists)** open, so the walls as recorded could not be built.
> Both are now designed. **This adds nothing to the frame and changes no frame member.**
>
> **Lintel L1 — one type over every opening in the sentry post**
> ```
> 190 wide x 150 deep, M30 / Fe500, cover 30, bearing 200 each end
> 2-T10 bottom  ·  2-T8 top (hangers)  ·  T6 two-legged links @ 150
> ```
> Openings served — **eleven in all**: ground **D1 900** and **W1 1200**; first storey
> **D1 900** and the **eight 1200-wide vision-panel openings**. The 1200 opening governs;
> one type covers all. (WM1's quantity `SP-06` already measures eleven lintels. The
> "nine openings" in the K.1 WM-V5 text counts only the nine *unstated-height* window and
> vision openings, matching WM-V3 — **a wording looseness in that block, flagged not
> silently edited; no quantity depends on it.**)
>
> **Design basis.** Effective span = min(clear + d, c/c bearings) = min(1315, 1400) =
> **1.315 m** (IS 456 Cl. 22.2). **The opening HEIGHTS are not stated on any drawing —
> WM-V3, still open.** WM1 assumed 1200 for *measurement only*, tagged `[A]`/`[N]`; **L1
> does not use that assumption and does not confirm it.** The lintel is deliberately
> designed to the bound that does not depend on the height at all: masonry standing *just
> below* the 60° arching height (0.866 × 1.315 = 1.139 m), which is the heaviest case any
> opening height can produce — above it, arching relieves the lintel; below it, there is
> less masonry. **The design therefore holds whatever WM-V3 is eventually ruled to be.**
>
> w = 0.190 × 20 × 1.139 = **4.33 kN/m**,
> M = 0.935 kNm, V = 2.85 kN → M<sub>u</sub> = **1.403 kNm** against
> M<sub>u,lim</sub> = 0.133 f<sub>ck</sub>bd² = **10.03 kNm**, **14 % utilised**.
> A<sub>st</sub> required 29.5 mm², **IS 456 Cl. 26.5.1.1 minimum 0.85bd/f<sub>y</sub> =
> 37.1 mm² GOVERNS**; 2-T10 = 157 mm² provided. τ<sub>v</sub> = 0.195 against
> τ<sub>c</sub> ≈ 0.56 for M30 at p<sub>t</sub> 0.72 % → **no shear steel required**;
> the T6 @ 150 links are the Cl. 26.5.1.6 nominal minimum (max spacing 324).
> **The lintel carries masonry only** — the floor and roof go to beams B1/B2 at each
> level, which is the whole point of the frame.
>
> **Wall ties.** 6 mm dia MS ties at **every fifth course (≈ 450 mm)** up both column
> faces, projecting **200 mm** into the bed joint, anchored to the column by a cast-in or
> drilled-and-grouted 10 mm dowel. The top course is **built tight to the beam soffit and
> the last joint packed**, because the analysis takes **R = 3.0** — the infill is NOT
> separated from the frame and must not be. Separating it would be the R = 5.0 special
> moment frame case, which this project does not claim.
>
> **What SP-B2 does NOT change.** No frame member, no footing, no slab, no storey height,
> no envelope. **Infill on the first-floor beams stays at 13.000 kN/m** in A.7.7 and in
> `Sentry_Post_Framed_Seismic.std`: brick gives ≈ 9.88 kN/m, which is lighter, so the
> modelled value stays conservative. **WM-V6 is still open** — the structural discipline
> must re-run the seismic check; nothing here is a substitute for that.
> **WM-V7 IS NOT CLOSED AND CANNOT BE CLOSED HERE: brick masonry does not give the
> ballistic protection the Rev F "200 RC ballistic panels" were named for.** That is a
> client / military decision, not a drafting one. `[C] instruction / [R] IS 456 design`

### A.4.9 Exit hatches and blast doors — every opening through the protective boundary

> **Added by RC3, 11 September 2026 (Part H.27).** Nothing here is new design. Every value is
> collected from A.2, A.3, A.4.6, A.4.7, B.2, B.6, F.1 and the FS2 escape-route schedule, so
> that the openings through the boundary can be read in one place instead of six.

**Doors**

| Mark | Where | Leaf | Level | Rating | Class |
|---|---|---|---|---|---|
| **Blast Door 1** | **W6**, X 14800–15200 (400 thk), opening Y 600–1800 — stair shaft → Bay 6 | **1200 × 2100** | **(−)6.100** | **≥ 7 bar, gas-tight, rebound-rated** | [C] geometry · **[V] the door itself is proprietary** |
| **Blast Door 2** | **W7**, X 18000–18400 (400 thk), opening Y 600–1800 — stair shaft → Bay 8 | **1200 × 2100** | **(−)6.100** | **≥ 7 bar** | [C] geometry · **[V]** |
| Inner security door | **HW2**, the headhouse north wall, X 14450–15350 | 900 × 2100 | (−)2.000 | **NOT blast rated** | [C] |
| Entry door | Entry stairwell headwall, X 9250–9500, **opens outward** | 1000 × 2100 | 0.000 | **NOT blast rated** — outside the boundary, declared expendable | [C] |
| **D-05, the W5 gas-tight door** | **W5, X 12600–12800** | — | (−)6.100 | — | **[NOT AVAILABLE].** W5 is designated *fire and gas-tight* and **no door exists in it anywhere in the project** (FS-1 / FN-U1). Escape route R1 has to cross it |
| W8 partition gaps ×4 | 3500–3610, 5410–5520, 9020–9130, 10930–11040 | **permanent 900 gap, Y 2500–3400** | (−)6.100 | **no doors, by design** | [C] |

**Both blast doors are the protective boundary.** They sit in the same plane as W6/W7, and
Finding F1 is why those walls are 400 thk: the shaft equalises to full p<sub>so</sub>, so the
doors and the walls beside them take the same 383 kPa. The opening reinforcement is in B.2 —
**4-T20 each jamb each face** anchored L<sub>d</sub> 800 beyond, and a **400 × 1100 header,
4-T20 top + 4-T20 bottom, T12 4-leg links @ 150.** Each frame is a **cast-in steel frame
anchored into and welded to the cage**, which is both the blast fixing and the only EMP
continuity the opening has.

**Escape shaft heads**

| | **ESC 1** | **ESC 2** |
|---|---|---|
| Bay / centre | Bay 1, **(2050, 2050)** | Bay 8, **(19900, 2050)** |
| Shaft | **1400 dia clear**, 250 RC collar, OD 1900 | as ESC 1 |
| Head level | **+0.150** | **+0.700** |
| Climb from (−)6.100 | **6.250 m** | **6.800 m** |
| Route | **R2** | **R3** — **shares Bay 8 with the generator (FS-3)** |

> **THE SHAFTS ARE NOW CLIMBABLE — RC4, 11 September 2026 (Part H.28).** `FS-V7` ruled:
> **ladder only, fall-arrest deferred.** One ladder type serves both shafts —
> **20 mm dia galvanised MS rungs, 400 clear width, equal pitch within each shaft**
> (ESC 1 297.6 mm over 21 spaces; ESC 2 295.7 mm over 23), **≥ 200 behind the rung and ≥ 750
> clear climbing space in front**, 2 No. 50 × 10 galvanised flat stringers, cast-in lugs to the
> 250 collar and the roof-slab bore with expansion-anchored brackets at 1.5 m over the lower
> 3.200 m, and **grab rails 1100 above the head**. `IS 3696 (Part 2)` and `NBC 2016 Part 4` are
> named **by title only** — neither is in the workspace and Part G forbids citing an
> unconfirmed clause. **`FS-V7` DOES NOT CLOSE. It CHANGES**, and three things are still
> missing: **no fall-arrest** (deferred by ruling), **no rest platform** (a 1400 bore cannot
> take one without blocking the escape), and **the injured-person question** — a vertical
> ladder cannot pass a stretcher, and whether a casualty is expected to use a shaft is a client
> question. `[C] owner ruling / [A] geometry`

> **What the project does not hold for these two heads — and must not be invented:**
> **(1) No hatch.** Neither shaft head has a leaf, a frame, a fixing or a bonding detail
> anywhere `[N]` (**EM-V6**). EM1 established what it has to be — a **bonded conducting hatch
> at the head**, because a 1400 dia shaft propagates above **125.5 MHz** however well it is
> lined — but the specification itself is vendor data the project does not contain.
> **(2) No way to climb either shaft.** There is no ladder, no rung and no fall-arrest
> specified in either `[N]` (**FS-V7**). These are **6.250 m and 6.800 m vertical climbs** and
> they are two of the three escape routes. **This one needs a design, not a ruling.**
> **(3) No blast-door vendor data of any kind**, RF performance included `[N]` (**EM-V6**, and
> one of the 13 gaps). Blast Door 1 is the only thing across the entry path's open
> electromagnetic route from grade to Bay 7 (**EM-F1**).

## A.5 Materials — CURRENT

| Item | Shelter / stairs / headhouse | Sentry post | Source |
|---|---|---|---|
| Concrete | **M35** | **M30** | IS 456 Table 5 (M35 = minimum for very severe exposure, Table 3) |
| w/c ratio | ≤ 0.45 | — | IS 456 Table 5 |
| Cement content | ≥ 340 kg/m³ | — | IS 456 Table 5 |
| Admixture | Integral crystalline waterproofing | — | [R] |
| Blinding | M15, 100 thk | — | |
| Burster slab (in the cover) | M30, 200 thk | — | |
| Reinforcement | **Fe500D** to IS 1786:2008 | Fe500 | |
| E<sub>c</sub> = 5000√f<sub>ck</sub> | **29 580 N/mm²** | **27 386 N/mm²** | IS 456 Cl. 6.2.3.1 |
| Poisson's ratio | 0.20 | 0.20 | [ASSUMED — standard] |
| Unit weight RC | 25 kN/m³ | 25 kN/m³ | IS 875 (Pt 1) Table 1 |
| γ<sub>m</sub> concrete / steel | 1.5 / 1.15 | same | IS 456 Cl. 36.4.2 |

### Cover — IS 456 Cl. 26.4.2 / Table 16 [CONFIRMED]

| Face | Cover |
|---|---|
| Cast against blinding / trimmed rock | **75 mm** |
| Formed earth face | **50 mm** |
| Internal faces | **40 mm** |
| Stair shaft faces (wet/dirty zone) | 30 mm |
| Sentry post beams and slabs | **30 mm** |
| Sentry post columns | **40 mm** (Cl. 26.4.2.2 — never less than 40 nor the bar dia) |
| Footings cast against earth | **50 mm** (Cl. 26.4.2.1) |
| **Max bar spacing, both curtains** | **150 mm — EMP requirement**, stricter than IS 456 Cl. 26.3.3 |

> The 5 mm cover reduction that IS 456 Table 16 permits for M35 and above is **deliberately not taken**.

### Development and lap lengths — IS 456 Cl. 26.2.1 [CONFIRMED]

```
Ld = φ σs /(4 τbd),  σs = 0.87 fy = 435 N/mm²
τbd (Cl. 26.2.1.1):  M30 → 1.5   M35 → 1.7   ; × 1.6 for deformed bars in tension
                     ÷ 0.8 (i.e. × 1.25) for bars in compression
```

| Grade | τ<sub>bd</sub>×1.6 | **L<sub>d</sub> tension** | L<sub>d</sub> compression |
|---|---|---|---|
| M35 | 2.72 | **40 φ** | 32 φ |
| M30 | 2.40 | **46 φ** | 37 φ |

| Bar | L<sub>d</sub> M35 | Lap M35 | L<sub>d</sub> M30 | L<sub>d,c</sub> M30 |
|---|---|---|---|---|
| T8 | 320 | 400 | 368 | 296 |
| T10 | 400 | 500 | 460 | 370 |
| T12 | 480 | 600 | 552 | 444 |
| T16 | 640 | 800 | 736 | 592 |
| T20 | 800 | 1000 | 920 | 740 |
| T25 | 1000 | 1250 | 1150 | 925 |

**Lap policy:** IS 456 Cl. 26.2.5.1(c) gives lap = L<sub>d</sub> or 30φ whichever greater = 40φ. Cl. 26.2.5.1 requires ×1.4 if more than 50 % of bars are lapped at one section. **All laps staggered so ≤ 50 % are spliced at any section, and lap specified as 50 φ** — 25 % above requirement.

**Blast bond:** IS 4991 Cl. 10.3.1.1 permits +25 % on bond (→ 32φ). **Not taken.** All detailing uses the static 40φ.

## A.6 Soil and foundation parameters — CURRENT

| Parameter | Value | Class |
|---|---|---|
| Ground | Deccan basalt (trap), with red-bole / vesicular seams at flow contacts | [ASSUMED] |
| Rockhead | (−)1.500 to (−)2.000 | [ASSUMED] |
| Presumptive SBC | **3240 kPa** (IS 1904:1986 Table 1, hard rock) | [ASSUMED] |
| Bulk unit weight γ | 20 kN/m³ | [ASSUMED] |
| Saturated unit weight γ<sub>sat</sub> | 21 kN/m³ | [ASSUMED] |
| Submerged γ′ = 21 − 9.81 | 11.19 kN/m³ | [CONFIRMED, derived] |
| At-rest coefficient K₀ = 1 − sin φ | **0.50** (φ ≈ 30°) | [ASSUMED] |
| **Design GWT** | **(−)2.000** (monsoon) | [ASSUMED — the single most important number to confirm] |
| **Modulus of subgrade reaction k<sub>s</sub>** | **100 000 to 500 000 kN/m³** | [ASSUMED] — **RUN THE MAT MODEL AT BOTH BOUNDS** |
| Settlement | Negligible on sound basalt (IS 12070) | [ASSUMED] |
| Soil-transmission factor K<sub>a</sub>, saturated | **1.0** (IS 4991 Cl. 7.2 + Table 3) | [CONFIRMED] |
| K<sub>a</sub>, dry compacted berm fill | ~0.5 | [ASSUMED — **deliberately not relied on**, see C10] |

> **The hazard is not the basalt — it is the flow contacts.** A single red-bole seam under the mat produces the differential-support case that SIZES the mat. Over-excavate any red-bole or vesicular seam at founding level and replace with M15 lean concrete.

> **SG1 — PROVENANCE, 11 September 2026 (Part H.22). NOT ONE VALUE OR TAG IN THE TABLE ABOVE
> IS CHANGED BY THIS NOTE.** Until SG1 every row above was `[ASSUMED]` with **no source
> recorded anywhere**. Two documents have now been supplied — the **SEMT/67/15** sub-soil
> investigation for the CTW PH-III ACCN project at CME Pune, and the **P1 presentation deck**
> — and the package `Site Selection and Geotechnical/` records what each row can and cannot
> draw from them.
>
> **The one fact that governs all of it: the investigation reached about 1.5 m; this structure
> founds at (−)6.800.** Only the sentry footing F1 at (−)2.000 lies inside the investigated
> horizon. **Rockhead continuity, groundwater, red-bole seams, k<sub>s</sub> and rock-mass
> permeability at the founding horizon are all still `[N]`**, and the programme's confirmatory
> site investigation `A1075` remains mandatory in full — and must be located **on this plot**,
> which the SEMT trial pits were not.
>
> | Row | What the new evidence says | Effect |
> |---|---|---|
> | Ground | Deccan Trap confirmed — *"horizontally bedded and more or less uniform in character over a wide area"* | **corroborated.** The flow-contact hazard is neither found nor excluded |
> | Rockhead | **0.9–1.5 m** at three locations | the report's band is **entirely at or above** the assumed 1.5–2.0. Conservative for founding depth, **unconservative for rock excavation quantity: +118 m³, ≈ 2 days** (`SG-F5`) |
> | **Presumptive SBC 3240** | measured basalt **1961–2059 kPa soaked**, 2942–3530 unsoaked | the founding horizon is **4.8 m below the design GWT**, so **soaked governs**. Worst utilisation rises 12.5 % → **20.6 %**; every element still passes with a factor of **4.8** in hand. **3240 stands — it is an IS 1904 presumptive value and is declared as one** (`SG-F3`) |
> | γ 20 / γ<sub>sat</sub> 21 | 95 % MDD at OMC gives **19.12–19.61**; γ<sub>sat</sub> back-figures to **21.26** | bulk 20 is **2–5 % conservative** for lateral load; γ<sub>sat</sub> **agrees within 1.2 %** |
> | K₀ 0.50 | measured φ **27–35°** → K₀ 0.426–0.546 | **conservative** against all three granular murrum samples. Worst case moves the wall design load **under 1 %** — the walls are blast-governed (`SG-F9`) |
> | **Design GWT (−)2.000** | *"Water table was not encountered in any trial pit"* — **in pits ~1.5 m deep** | **the provenance of (−)2.000, recorded for the first time: no water was found, so 2 m was CHOSEN.** *Not encountered* here means **not reached**. **`K.2 A2` stays `[ASSUMED]` and stays open** (`SG-F6`) |
> | k<sub>s</sub> | nothing — no plate load test | untouched. **Both bounds still outstanding** |
> | Settlement | net pressure at formation is **≈ −105 kPa** — the structure is **lighter than the ground it replaces** | this is *why* "negligible" is true, and the same fact that makes **flotation** the governing foundation problem (`SG-F4`) |
>
> **New, and recorded nowhere in this project before SG1: the surface soil is BLACK COTTON, CH,
> free swell index 60–65 % — the top band of the IS 1498 scale.** Nothing structural founds in
> it. Two elements are exposed anyway and **neither is changed here**: the covered entry
> stairwell's stepped raft (`SG-F13` / `SG-V6`) and the 300 turf concealment layer
> (`SG-F14` / `SG-V7`).

## A.7 Loading — CURRENT, complete register

### A.7.1 Blast

```
DBT                       nuclear air-blast, p_so = 344.7 kPa (50 psi)          [C]
Positive phase td         0.13 to 1.33 s                                        [C]
Reflected pressure p_r    1366 kPa                                              [CONFIRMED]
Dynamic pressure q        282 kPa                                               [CONFIRMED]
Ductility ratio μ         5   (moderate, repairable damage)   IS 4991 Cl 10.3.3
DLF = μ/(μ − 0.5)         5/4.5 = 1.111
                          validation: μ = 1 → DLF = 2.00 = the textbook step-load factor ✔
DESIGN BLAST PRESSURE     344.7 × 1.111 = 383 kPa
                          applied to the roof AND the walls (Ka = 1.0)
Roof natural period T     13.4 ms  → td/T = 10 to 100 → QUASI-STATIC
Dynamic material strengths (BLAST CASE ONLY, IS 4991 Cl 10.3.1):
     fck,dyn = 1.25 × 35 = 43.75 N/mm²      fy,dyn = 1.25 × 500 = 625 N/mm²
NO dynamic increase on shear — IS 4991 Cl 10.3.1.1
```

### A.7.2 Gravity, soil and water

| Load | Value | Applied to | Source |
|---|---|---|---|
| Self weight RC | 25 kN/m³ | all | IS 875 (Pt 1) Table 1 |
| Roof self, 0.900 × 25 | 22.50 kPa | roof | |
| Mat self, 0.600 × 25 | 15.00 kPa | mat | |
| **Engineered cover, 2000 layered** | **40.65 kPa** | roof | [CONFIRMED, see A.7.3] |
| SIDL services/finishes | 2.0 kPa roof / 1.0 kPa mat | | [R] |
| Live load, internal floor | **5.0 kPa** (plant/storage, not 2.0 residential) | floor | IS 875 (Pt 2) |
| Earth + water lateral gradient | K₀γ′ + γ<sub>w</sub> = 0.50 × 11.19 + 9.81 = **15.41 kPa/m** | walls | [CONFIRMED, derived] |
| — at roof soffit (−)2.900 | 33.9 kPa | walls | |
| — at floor (−)6.100 | **83.2 kPa** | walls | |
| Hydrostatic uplift on mat | 4.700 × 9.81 = **46.11 kPa**; total **6289 kN** over 136.4 m² | mat | [CONFIRMED] |
| Construction surcharge | 20 kPa vertical / 10 kPa lateral | | [ASSUMED] |
| Staircase, smeared on the two shaft walls | 2.947 kPa | W6/W7 | [CONFIRMED — report LC5] |

> Of the 15.41 kPa/m lateral gradient, **9.81 is water and only 5.60 is soil.** Water is nearly two-thirds of the lateral load. This is why the groundwater level is the most important number the site investigation must confirm.

### A.7.3 Engineered cover build-up — 40.65 kPa [CONFIRMED]

| From the top | Thickness | Unit weight | Load kPa | Function |
|---|---|---|---|---|
| Topsoil / turf | 300 | 18 | 5.40 | Concealment, erosion, sheds rain |
| Granular filter | 150 | 19 | 2.85 | Stops fines clogging |
| **RC burster slab M30, T12 @ 150 B/W** | 200 | 25 | 5.00 | **Breaks up a penetrating item** |
| Crushed basalt rubble 25–75 mm | 500 | 17 | 8.50 | Scatters burster energy |
| Compacted engineered fill @ 95 % MDD | 750 | 20 | 15.00 | **Radiation mass** |
| Protection screed over the membrane | 100 | 24 | 2.40 | Protects waterproofing |
| Sum of the six layers | 2000 | | 39.15 | |
| **Declared allowance, held** | — | | **+1.50** | **RC1 — see below** |
| **TOTAL — DESIGN VALUE** | **2000** | | **40.65** | |

> **RC1 — C17 IS RULED, 10 September 2026 (Part H.14).** The six layers sum to
> **39.15 kPa**; this table stated **40.65** and the two never agreed. **40.65 is held as
> the design value** and the table now shows why: it is the layer sum **plus a declared
> allowance of 1.50 kPa**. That is the only choice that costs nothing and changes nothing —
> 40.65 is the number in A.7.4, in Part L and in **every `.std` file**, it is the **larger**
> of the two, and adopting 39.15 instead would lighten COMB 103 by 1.50 kPa and require a
> re-analysis that cannot be run here. The allowance is **not fabricated evidence**: it is
> the difference the project has always carried, now stated instead of hidden. Nothing in
> Parts B, F or L moves, no `.std` file is touched, and **COMB 103 stays 448.15 kPa**.
> `[R] declared reconciliation of two recorded values`

> **BS1 — THE BURSTER SLAB IS LAID TO FALLS, 10 September 2026 (Part H.12).** By
> instruction, the **200 RC burster slab is no longer laid flat**. It is laid to a
> **1:50 crossfall, crowned on the box longitudinal centreline (Y = 3100) and falling
> each way to the box edges** — that is, **parallel to the finished grade**, which
> A.4.3 already records as *crowned, falling 1:50 away*. Over the 3100 half-width the
> slab drops **62 mm** from crown to box edge.
> **Why:** the granular filter sits directly on the burster slab, and D-201 note 3 and
> calculation D.7 already state that water infiltrating the topsoil is *"intercepted by
> the granular filter and dispersed at the berm toe."* **On a flat slab it cannot be** —
> it ponds on the slab and finds the construction joints. The crossfall gives the filter
> layer the gradient that claim depends on, so seepage runs sideways to the slab edge
> and daylights into the berm fill. **No pipe is introduced anywhere in the cover** —
> D-001 note 1 and D-201 note 3 still hold.
> **Thicknesses and load — UNCHANGED.** The fall is taken up entirely in the **compacted
> engineered fill** below the rubble, which is **750 (nominal) at the crown thinning to
> 688 at the box edge**. Every other layer keeps its nominal thickness. The cover
> therefore weighs **exactly what it weighs today at the crown**, and *less* toward the
> edges: **the cover load does not increase anywhere.** COMB 103 = 448.15 kPa, A.7.4,
> Part B, Part F, Part L and all three `.std` files are **untouched**. The slab's own
> M30 / T12 @ 150 B/W reinforcement is unchanged — it is a cover element, not a
> structural element of the box.
> **C17 is NOT resolved by this.** The column above still sums to 39.15 against the
> stated 40.65, at the crown exactly as before. `[C] instruction / [A] 1:50 to match A.4.3`

> **Why 2.0 m:** not blast (a buried roof takes full p<sub>so</sub> regardless — IS 4991 Cl. 7.2) and not fallout (1.0 m already gives PF ≈ 2200 against a requirement of ~1000). **The second metre is bought entirely for prompt neutron and gamma attenuation**, which needs mass and needs it above the slab. Reducing 4.0 m → 2.0 m saved 2 m of rock excavation, 2 m of shaft, one stair flight and 2 m of headroom.

### A.7.4 Total roof load — COMB 103

| Component | kPa |
|---|---|
| Blast, 344.7 × 1.111 | 383.00 |
| Engineered cover | 40.65 |
| SIDL | 2.00 |
| Self weight | 22.50 |
| **TOTAL w** | **448.15** |

Live load excluded — **IS 4991 Cl. 11.2**: *"No live load shall be considered on roof at the time of blast."*
Static ULS 101 on the roof = 1.5 × (40.65 + 2.0 + 22.5 + 20) = 127.7 kPa → **blast governs 3.51 : 1**.

### A.7.5 Headhouse loads

| Element | Load | Basis |
|---|---|---|
| Roof (flush horizontal at berm crest) | **396.5 kPa** = 383 blast + 12.5 self + 1.0 SIDL | IS 4991 Cl. 7.2 |
| **Walls — CURRENT** | **383 kPa, acting EITHER FACE** | **Conflict C10 — raised from the report's 113 kPa drag** |
| Walls — report basis (superseded) | 113 kPa = C<sub>d</sub>·q = 0.4 × 282 | IS 4991 Cl. 7.4 |

> The walls sit behind ~2.5 m of berm and **earth transmits pressure**. K<sub>a</sub> for dry compacted fill is an assumption we cannot verify, so the walls are designed for the full 383 kPa upper bound. **Cost of the upgrade: one link cage (T12 4-leg @ 250). Utilisation rises 17 % → 59 %.**

### A.7.6 Entry stairwell loads — static only, NOT blast rated

| Element | Load |
|---|---|
| Flight, waist 250 | waist 7.150 + steps 2.083 + finishes 1.000 + LL 5.000 = 15.233 → **w<sub>u</sub> = 22.85 kPa** |
| Side walls 250 | K₀ 0.50 × 20 × 2.9 + 0.5 × 10 surcharge = **34 kPa at base** |
| Raking roof 250 | self 6.25 + wp 2.0 + earth lap 5.4 + **imposed 20** = 33.65 → **w<sub>u</sub> = 50.5 kPa** |
| Top landing 250 | 18.4 + flight reaction 36.5 = **54.9 kPa** |

### A.7.7 Sentry post loads — [CONFIRMED from the Rev F framing plan, all verified]

| Item | Value | Verification |
|---|---|---|
| Slab dead, first floor | 4.750 kPa | 0.150 × 25 + 1.0 finish ✔ |
| Slab dead, roof | 5.250 kPa | 3.75 + 1.5 screed/wp ✔ |
| Imposed, first floor | 3.000 kPa | IS 875 (Pt 2), observation post ✔ |
| Imposed, roof | 1.500 kPa | IS 875 (Pt 2), accessible ✔ |
| Peak two-way intensity, DL floor | 8.669 kN/m | 4.75 × 1.825 ✔ |
| Peak two-way intensity, DL roof | 9.581 kN/m | 5.25 × 1.825 ✔ |
| Peak two-way intensity, LL floor | 5.475 kN/m | 3.00 × 1.825 ✔ |
| Peak two-way intensity, LL roof | 2.737 kN/m | 1.50 × 1.825 ✔ |
| Infill on first-floor beams | 13.000 kN/m | 0.200 × 2.600 × 25 ✔ |
| — SP-B1 note, 7 Sep 2026 | **13.000 kN/m STANDS** | Brick masonry at ≈ 20 kN/m³ over 0.190 × 2.600 gives ≈ 9.9 kN/m, i.e. **lighter**, so the design value and V<sub>b</sub> = 73.18 kN remain **conservative**. **A direction, not a verification — the structural discipline must re-run the check (WM-V6). NOT changed here.** |
| Roof projection + parapet | 4.162 kN/m | **[C] as drawn. HALF re-derived — see below** |
| — parapet term, 0.300 × 0.150 × 25 | **1.125 kN/m** | **[CONFIRMED, reproduces exactly]** |
| — roof projection term | **3.037 kN/m** | **[NOT AVAILABLE — the projection dimension is recorded nowhere]** |
| w<sub>u</sub> floor = 1.5(4.75 + 3.00) | **11.625 kPa** | governs the slab |
| w<sub>u</sub> roof = 1.5(5.25 + 1.50) | 10.125 kPa | |

**Load path to the beams — IS 456 Cl. 24.5, 45° yield lines:**
```
Peak intensity on any beam = w × short span/2 = w × 3.650/2 = w × 1.825 m
SHORT beams B1 (3650 long) → TRIANGLE
LONG  beams B2 (4650 long) → TRAPEZOID,  w_eq = w_peak × [1 − 1/(3r²)],  r = 1.274 → 0.7946
```

### A.7.8 Seismic

**Underground box — IS 1893 (Part 1):2016**
```
Z = 0.16 (Zone III)   I = 1.5   R = 4.0   Sa/g = 2.5
Ah = (Z/2)(I/R)(Sa/g) = 0.08 × 0.375 × 2.5 = 0.075
W  = 14 002 kN  →  Vb = 1050 kN
Per long wall 525 kN → τ = 525e3/(600 × 0.8 × 21600) = 0.063 N/mm²  NEGLIGIBLE
IS 13920 Cl. 10.4 boundary elements NOT triggered
```

**Sentry post — IS 1893 (Part 1):2016**
```
Z = 0.16   I = 1.5   R = 3.0   Sa/g = 2.5 (rock, T on the plateau)
   R = 3.0 because the 200 RC infill panels are NOT separated from the frame.
   R = 5.0 would require a special MRF with positively separated infill.
Ah = 0.08 × 0.50 × 2.5 = 0.100

Fundamental period (all three land inside 0.10–0.40 s → Sa/g = 2.5 regardless):
   bare RC MRF, Cl 7.6.2      Ta = 0.075 h^0.75 = 0.075 × 6.250^0.75 = 0.297 s
   with infill, Cl 7.6.2(c)   Ta = 0.09h/√d :  X 0.281 s   Z 0.252 s

HAND-CALCULATED seismic weight:
   Roof  +6.700 : slab 89.1 + parapet/proj 69.1 + beams 31.1 + half-cols 18.7
                  + half first-storey infill 107.9                    = 315.9 kN
   Floor +3.650 : slab 80.6 + beams 31.1 + cols 38.3
                  + half ground-storey infill 114.1 + 25 % LL 12.7    = 276.8 kN
   TOTAL W = 592.7 kN   →   Vb,hand = 0.100 × 592.7 = 59.3 kN

*** STAAD MODEL VALUE, WHICH GOVERNS DESIGN: Vb = 73.18 kN ***
   Stated in the load-case titles and CONFIRMED by the reactions:
   Fx = 18.295 kN per column × 4 = 73.18 kN
   The model is 23 % heavier than the hand check.  See CONFLICT C9.
```

**Wind on the sentry post — IS 875 (Part 3):2015**
```
Vb = 39 m/s (Pune)   k1 = 1.08 (100-yr, Table 1)   k2 = 1.00 (Cat 2, 10 m)   k3 = k4 = 1.00
Vz = 42.12 m/s ;  pz = 0.6 Vz² = 1.065 kPa   (Cl 7.2)
pd = pz × Kd 0.90 × Ka 0.897 × Kc 1.0 = 0.859 kPa
F = Cf 1.3 × Ae (4.0 × 6.7 = 26.8 m²) × pd = 29.9 kN

SEISMIC 73.18 kN vs WIND 29.9 kN  →  SEISMIC GOVERNS 2.4 : 1
```

### A.7.9 Load combinations — CURRENT

**Underground box (5 combinations, matching the STAAD model)**

| No. | Title | Factors |
|---|---|---|
| 101 | ULS static | 1.5 (DL + SIDL + LL + SOIL + UPLIFT) |
| 102 | ULS uplift | 0.9 DL + 1.5 UPLIFT |
| **103** | **BLAST** | **1.0 (DL + SIDL + SOIL + UPLIFT + BLAST)** ← governs every element |
| 104 | SLS crack width | 1.0 (DL + SIDL + LL + SOIL + UPLIFT), IS 3370 Pt 2 |
| 105 | Construction | 1.5 (DL + SOIL + UPLIFT + SURCHARGE) |

> γ = 1.0 on blast because it is an extreme event checked against ULTIMATE capacity with DYNAMIC material strengths (IS 4991 Cl. 10.3.1). Applying 1.5 while also taking the 25 % material bonus would be inconsistent.
> **Wind and earthquake are absent from 103 — IS 4991 Cl. 11.1** forbids combining them with blast.

**Sentry post (16 combinations, matching the STAAD model) — [CONFIRMED, read from `current/staad/Sentry_Post_Framed_Seismic.std`]**

| No. | Combination |
|---|---|
| 101 | 1.5 DL + 1.5 LL |
| 102 | 1.2 DL + 1.2 LL + 1.2 EQ+X |
| 103 | 1.2 DL + 1.2 LL + 1.2 EQ−X |
| 104 | 1.2 DL + 1.2 LL + 1.2 EQ+Z |
| 105 | 1.2 DL + 1.2 LL + 1.2 EQ−Z |
| 106 | 1.5 DL + 1.5 EQ+X |
| 107 | 1.5 DL + 1.5 EQ−X |
| 108 | 1.5 DL + 1.5 EQ+Z |
| 109 | 1.5 DL + 1.5 EQ−Z |
| 110 | 0.9 DL + 1.5 EQ+X |
| 111 | 0.9 DL + 1.5 EQ−X |
| 112 | 0.9 DL + 1.5 EQ+Z |
| 113 | 0.9 DL + 1.5 EQ−Z |
| 201 | 1.0 DL + 1.0 LL — SERVICE |
| 202 | 1.0 DL + 1.0 EQ+X — **DRIFT CHECK, IS 1893 Cl. 7.11** |
| 203 | 1.0 DL + 1.0 EQ+Z — **DRIFT CHECK, IS 1893 Cl. 7.11** |

> **RC3 correction, 11 September 2026 (Part H.27).** This table read *"15 combinations"* and stopped at 202, on the authority of the screen captures. The `.std` file itself carries **sixteen** `LOAD COMB` cases — **203, the second drift check, was missing here and in Part L.** `QUICK_STATE.md` had flagged the shortfall; the master had not been corrected. **No combination factor, member force or bar changes — 203 is a serviceability drift check that was already in the model being designed to.** `[C] read from the .std`

---

# PART B — STRUCTURAL DESIGN: FINAL ADOPTED VALUES

> **Every value in Part B has been computed numerically in this project. The DXF drawings carry exactly this reinforcement — no drawing shows an arrangement that differs from these calculations.**

**Flexure equation used throughout — IS 456 Annex G-1.1(b):**
```
Mu = 0.87 fy · Ast · d · [ 1 − (Ast · fy)/(b · d · fck) ]
xu = 0.87 fy Ast /(0.36 fck b)                              IS 456 Cl. 38.1
xu,max/d = 0.46 for Fe500                                   IS 456 Cl. 38.1(f)
Mu,lim = 0.133 fck b d²                                     IS 456 Annex G-1.1(c)
```

## B.1 Perimeter walls W1–W4 — 600 thk

```
INPUTS      t 600, clear height 3200, cover 75 earth / 40 internal, T16
            d = 600 − 75 − 8                                     = 517 mm
            Blast 383 kPa (Ka 1.0); static earth+water 83.2 kPa at base
            → BLAST GOVERNS 4.6 : 1
FORMULA     Mp = w·Ln²/16   (fixed-fixed plastic mechanism)
SUBSTITUTE  Mp = 383 × 3.200²/16
RESULT      Mp                                                   = 245.1 kNm/m
CHECK       Mu,lim = 0.133 × 43.75 × 1000 × 517²                 = 1556 kNm/m ✔ singly reinforced
            Ast,req (fy,dyn 625, fck,dyn 43.75)                  = 894 mm²/m
            IS 456 Cl. 32.5(a) min vertical 0.0012 × 600         = 720 mm²/m
            IS 456 Cl. 32.5(b) min horizontal 0.0020 × 600       = 1200 mm²/m
            IS 3370 Pt 2 surface zone 0.35 % × 250 each face     = 875 mm²/m/face
ADOPTED     T16 @ 150 c/c EACH FACE EACH WAY                     = 1340 mm²/m
            Mu = 362.8 kNm/m → UTILISATION 68 %
            xu = 46.3 → x/d = 0.089  ≪ 0.46

SHEAR       V at d = 383 (1.600 − 0.517)                         = 414.8 kN/m
            τv = 414.8e3/(1000 × 517)          Cl. 40.1          = 0.802 N/mm²
            pt = 0.259 % → τc (Table 19, M35)                    = 0.375 N/mm²
            τc,max (Table 20, M35) 3.70 > 0.802                  ✔ Cl. 40.2.3
            Vus = (0.802 − 0.375) × 517                          = 220.8 kN/m
            Asv/sv = 220800/(0.87 × 500 × 517)  Cl. 40.4(a)      = 0.982 mm²/mm
            → T12 2-leg at 230; Cl. 26.5.1.5 limit min(0.75d 388, 300) = 300
ADOPTED     T12 CLOSED LINKS @ 200 c/c   (Asv/sv = 1.131 ✔)

AXIAL       N = 448.15 × 2.50 + 3.2 × 0.6 × 25                   = 1168 kN/m
            f = 1.95 N/mm² = 11 % of 0.4 fck,dyn (17.5)          ✔ P-M not critical
CRACK       IS 3370 Pt 2, limit 0.2 mm; surface steel 875 < 1340 ✔
```

> **Why 600 mm — stated honestly.** The wall is NOT strength-governed (68 %). 600 is set by (i) 75 mm cover, (ii) congestion — two curtains + closed links + waterstops + cast-in frames, (iii) IS 3370 crack control under sustained hydrostatic load, (iv) the EMP double curtain at 150, (v) the 1168 kN/m axial path.

## B.2 Walls W6 / W7 — 400 thk (MODIFICATION M1)

```
FINDING F1  The stair shaft is open to atmosphere through the 2800 × 3160 roof void,
            the headhouse and the entry stairwell.
            Fill time V/(A·c) = 105/(3.3 × 340) = 0.094 s  vs  td 0.13–1.33 s
            → THE SHAFT EQUALISES TO FULL p_so.
            W6/W7 sit in the SAME PLANE as the 7-bar blast doors, separating a
            pressurised shaft from Bay 6 / Bay 8 at ambient.

WHY 200 IS IMPOSSIBLE (not a detailing problem)
            d = 200 − 40 − 6                                     = 154 mm
            Mu,lim = 0.133 × 43.75 × 1000 × 154²                 = 138.0 kNm/m
            Demand Mp = 383 × 3.200²/16                          = 245.1 kNm/m
            138 < 245 → NO STEEL RATIO MAKES IT WORK
            Two-way action checked before rejection: panel 3200 × 3800, fixed 3 edges,
            yield line ≈ 0.7 × one-way = 172 kNm/m — still above 138.

DESIGN OF THE 400 WALL
            d = 400 − 50 (shaft face) − 8                        = 342 mm
            Mp = 383 × 3.200²/16                                 = 245.1 kNm/m
            Mu,lim = 0.133 × 43.75 × 1000 × 342²                 = 680.6 kNm/m ✔
            Ast,req                                              = 1400 mm²/m
ADOPTED     T20 @ 150 EF EW = 2094 mm²/m → Mu = 355.3, UTIL 69 %, x/d = 0.211

SHEAR       V at d = 383 (1.600 − 0.342)                         = 481.8 kN/m
            τv 1.409 | τc 0.540 (pt 0.612 %) | τc,max 3.70       ✔
            Vus 297.2 kN/m; Asv/sv 1.998 → T12 4-leg at 226
            Cl. 26.5.1.5 limit min(0.75d 257, 300) = 257
ADOPTED     T12 4-LEGGED LINKS @ 200 c/c

BLAST DOOR OPENING 1200 × 2100
            Interrupted steel 2094 × 1.2 = 2513 mm²/face → 1256 each jamb
ADOPTED     4 No. T20 EACH JAMB EACH FACE (1257 mm²), anchored Ld 800 beyond
HEADER      400 × 1100 over 1200 clear; w = 383 × 2.1/2 = 402 kN/m
            M = wL²/12 = 48.2 kNm ; V = 241 kN ; τ = 0.578 N/mm²
ADOPTED     4-T20 top + 4-T20 bottom, T12 4-leg links @ 150
FRAME       Cast-in steel frame anchored into and WELDED to the cage (EMP).
            Door: proprietary, ≥ 7 bar, rebound-rated, gas-tight  [V]
```

## B.3 Mat foundation — 600 thk

```
BEARING     Service 58.4 kPa (1.8 % of 3240) ; Blast 404.9 kPa (12.5 %)   ✔
            Bearing governs NOTHING.

CASE 1 — NET UPLIFT (COMB 102)
            u = 4.700 × 9.81 = 46.11 kPa ; self 0.600 × 25 = 15.0
            net 31.1 kPa UP over 5000 clear
            Mp = 31.1 × 5.0²/16                                  = 48.6 kNm/m  NOMINAL

CASE 2 — SOFT / RED-BOLE ZONE   *** GOVERNS ***
            A 3.0 m band of red-bole or vesicular material removed, worst position
            q = 404.9 kPa (blast bearing) over a 3.0 m unsupported span
            M = q·L²/12 = 404.9 × 9/12                           = 303.7 kNm/m
            d = 600 − 75 − 8                                     = 517 mm
            Ast,req                                              = 1115 mm²/m
ADOPTED     T16 @ 150 EF EW = 1340 mm²/m → Mu = 362.8, UTILISATION 84 %

THICKNESS STUDY   500 → Ast,req 1407 = 105 % of provided   FAIL
                  600 → 1115 = 84 %                        ADOPTED
                  700 →  926 = 70 %  |  800 (as drawn) ~ 57 % = 33 % unused reserve

ONE-WAY SHEAR — NOT CHECKED IN THE REPORT (CONFLICT C6)
            V at d from the soft-band edge = 404.9 (1.500 − 0.517) = 398.0 kN/m
            τv 0.770 | τc 0.375 (pt 0.259 %) | τc,max 3.70        ✔
            (no dynamic increase — IS 4991 Cl. 10.3.1.1)
            Vus = 204.2 kN/m ; Asv/sv                             = 0.908 mm²/mm
ADOPTED     T12 CLOSED LINKS ON A 250 × 250 GRID THROUGHOUT
            supplied Asv/sv = (4 × 113.1)/250 = 1.810 = 2.0 × required ✔
            Doubles as the spacer system between the two curtains.

PUNCHING    IS 456 Cl. 31.6 — no columns/pedestals bear on the mat; headhouse walls
            bear on the ROOF. NOT APPLICABLE — declared, not ignored.
SLIDING     Box socketed ~4.8 m into basalt, 300 annulus backfilled M15 lean.
            Not a credible mechanism — reasoning stated, no spurious factor computed.
OVERTURNING Buried box 22.0 × 6.2 × 4.7, symmetrical lateral load. NOT APPLICABLE.
SETTLEMENT  Negligible on sound basalt (IS 12070 Cl. 6). Hazard = the flow contacts.

FLOTATION — THE CONSTRUCTION STAGE GOVERNS
| Stage                        | Weight   | Uplift   | FoS @ (−)2.000 | FoS flooded to GL |
| 1 mat cast only              | 2 009 kN | 6 175 kN | 0.33  FAIL     | 0.23  FAIL |
| 2 mat + walls, no roof       | 4 802 kN | 6 175 kN | 0.78  FAIL     | 0.55  FAIL |
| 3 box complete, no backfill  | 7 528 kN | 6 175 kN | 1.22  MARGINAL | 0.86  FLOATS |
| 4 backfilled + cover         | 12 453 kN| 6 175 kN | 2.02  OK       | 1.41  OK |
            Require FoS ≥ 1.2.  ULS COMB 102 = 0.9 × 12453/(1.5 × 6175) = 1.21
            Uplift acts on the REAL underside, not the plate model's mid-surface area.
            *** THE ABSOLUTE FIGURES IN THIS TABLE ARE AT THE PRE-M1 21.600 BOX ***
            21.600 × 6.200 = 133.92 m²  ->  46.11 × 133.92 = 6175 kN  (table)
            22.000 × 6.200 = 136.40 m²  ->  46.11 × 136.40 = 6289 kN  (A.7.2, CURRENT)
            Both uplift and resistance scale with length (× 22.0/21.6 = 1.01852), so
            EVERY FoS IS UNCHANGED: 0.325 / 0.778 / 1.219 / 2.017, and COMB 102 stays
            0.9 × 12684/(1.5 × 6289) = 1.21.  THE HAND CHECK USES 136.40 m² / 6289 kN.

MANDATORY MITIGATION — a design output, not a contractor's problem:
  1 Continuous dewatering from start of excavation until backfill and cover complete
  2 Temporary pressure-relief valves / knock-out plugs in the mat (6 No. on S-02),
    grouted up ONLY after backfill
  3 Programme the sub-structure to complete before the monsoon, or bund and
    positively drain with standby pumping and generator back-up
  4 Backfill SYMMETRICALLY, in layers
```

## B.4 Pressure (roof) slab — 900 thk — THE GOVERNING ELEMENT

```
ONE-WAY ARGUMENT   Aspect 20.8/5.0 = 4.2.  IS 456 Table 26 is tabulated only to
                   ly/lx = 2.0, so two-way action CANNOT be claimed.
                   → Mp ∝ Ln² of the 5 m width ONLY.
                   → LENGTHENING THE BOX IS STRUCTURALLY FREE (basis of M1).
                     Widening 5.0 → 6.0 m would increase the roof moment 44 %.

NATURAL PERIOD     m = 0.900 × 2500 + 0.25 × 2.0 × 2000          = 3250 kg/m²
                   0.5 EIg = 0.5 × 2.958e10 × 0.900³/12          = 8.985e8 N·m²/m
                   f1 = (22.373/2π)·√(EI/(m·Ln⁴))                = 74.9 Hz
                   T                                              = 13.4 ms
                   td/T = 10 to 100  →  QUASI-STATIC

FLEXURE            d = 900 − 75 − 12.5                            = 812.5 mm
                   Mp = w·Ln²/16 = 448.15 × 25/16                 = 700.2 kNm/m
                   Mu,lim = 0.133 × 43.75 × 1000 × 812.5²         = 3841 kNm/m ✔
                   Ast,req (pt 0.20 %)                            = 1632 mm²/m
                   Cl. 26.5.2.1 min 0.12 % × 900                  = 1080 mm²/m
                   Cl. 26.5.2.2 max bar dia D/8 = 112             ✔ (T25)
ADOPTED            T25 @ 150 EF EW = 3272 mm²/m
                   Mu = 1362.4 kNm/m → UTILISATION 51 %
                   xu = 113.0 → x/d = 0.139 ≪ 0.46
                   *** x/d = 0.139 IS THE PROOF THAT μ = 5 IS DEFENSIBLE ***

SHEAR              V at support face = 448.15 × 2.50              = 1120 kN/m
                   V at d from face  = 448.15 × (2.50 − 0.8125)   = 756.3 kN/m
                   τv 0.931 | τc 0.450 (pt 0.403 %) | τc,max 3.70 ✔
                   Vus 390.8 kN/m ; Asv/sv 1.106 → T12 4-leg at 409
                   Cl. 26.5.1.5 limit 300 GOVERNS
ADOPTED            T12 4-LEG @ 250 IN THE END 1500 EACH SIDE;
                   T12 2-LEG @ 300 ELSEWHERE

DIRECT SHEAR       Vd,max = 0.16 fck,dyn b d                      = 5688 kN/m
                   vs 1120 applied → 19.7 %   [UFC 3-340-02 §4-30, NOT IS 456]

THICKNESS STUDY    | t | d | Mp | Ast,req | τv | verdict |
                   | 600 | 512.5 | 689 | 2673 | 1.71 | links at 164, congested |
                   | 800 | 712.5 | 696 | 1868 | 1.12 | structural optimum |
                   | 900 | 812.5 | 700 | 1633 | 0.93 | ADOPTED |
                   | 1000| 912.5 | 704 | 1453 | 0.78 | 11 % over |
                   900 adopted for (a) reserve at the 1400 collars, (b) headroom
                   against a raised DBT while the yield is unconfirmed, (c) support
                   rotation inside 2° without UFC lacing.
```

### B.4.1 Roof openings

**(a) Two 1400 dia circular escape-shaft openings**
```
Interrupted steel = 3272 × 1.400              = 4581 mm²/face/direction
Trimmers each side = 4581/2                   = 2291 mm²
ADOPTED  5 No. T25 EACH SIDE, EACH FACE, EACH DIRECTION (2454 mm²)
         anchored Ld = 1000 beyond the opening
         Collar 250 RC; T16 @ 150 hoops (3 layers) + T16 @ 150 radials
         Slab thickened 900 → 1200 over a 600 mm annulus
Circular is the right shape: hoop action, NO re-entrant stress concentration.
This detail SETS the 750 mm clearance rule.
```

**(b) The 2800 × 3160 rectangular stair void — FINDING F2, not designed in the report**
```
The void leaves an 1840 mm CANTILEVER of 900 slab, 2800 wide, at 448.15 kPa.
M(root) = 448.15 × 1.840²/2                   = 758.6 kNm/m
   *** THIS EXCEEDS THE 700.2 kNm/m MIDSPAN Mp ***
Ast,req TOP = 1772 mm²/m  <  3272 provided    → UTILISATION 56 %  ✔
V(root) = 448.15 × 1.840                      = 824.6 kN/m
τv 1.015 > τc 0.450 ; Vus 459.4 kN/m ; Asv/sv 1.300 → T12 4-leg at 348
Cl. 26.5.1.5 limit 300
ADOPTED  T12 4-LEG LINKS @ 250 THROUGHOUT THE PAD          (NEW requirement)
   plus  Free edge thickened 900 → 1200 over 600, with 6-T25 top + 6-T25 bottom
         and T12 closed links @ 150
   plus  6 No. T25 each face, top and bottom, in a 900 band over W6 and W7
   plus  Diagonal trimmers 4 No. T25 each face at 45° at BOTH re-entrant corners,
         2000 long each way, anchored Ld beyond
   plus  1100 mm guarding to the free edge (NBC 2016 Pt 4)
```

## B.5 Main staircase — Bay 7

> **STATUS: INSIDE the protective envelope. NOT a blast element.** The shaft pressurises, but that pressure acts on the shaft WALLS and the blast DOORS — not as a net load on a slab open on both faces. **Designed to IS 456 with normal partial factors, NOT with IS 4991 dynamic strengths.** Stated explicitly on drawing S-04.

**Geometry check — NBC 2016 Part 4**

| Item | Provided | Limit | Verdict |
|---|---|---|---|
| Riser | 170.833 mm | ≤ 190 | ✔ |
| Tread / going | 280 mm | ≥ 250 | ✔ |
| Flight width | 1200 mm | ≥ 1000 | ✔ stretcher-capable |
| Risers per flight | 8 | ≤ 12 preferred | ✔ |
| Headroom | 2533 mm | ≥ 2200 | ✔ |
| Total rise | 4100 = 24 × 170.833 | (−)6.100 → (−)2.000 | closes exactly |

```
FLIGHT — waist 200
   θ = arctan(170.833/280) = 31.4°, cos θ = 0.8535
   waist self 0.200 × 25/0.8535                    = 5.858 kPa
   steps 0.5 × 0.170833 × 25   IS 456 Cl. 33.2     = 2.135 kPa
   finishes                                         = 1.000 kPa
   live IS 875 (Pt 2), plant + escape route         = 5.000 kPa
   total 13.99 → wu = 1.5 × 13.99                   = 21.0 kPa
   Leff = going + min(landing/2, 1000) each end     IS 456 Cl. 33.1(b)
        = 1960 + 600 + 600                          = 3160 mm
   d = 200 − 30 − 6                                 = 164 mm
   M = wu·Leff²/8                                   = 26.2 kNm/m
   Ast,req 380 ; Cl. 26.5.2.1 min 0.12 % × 200 = 240
   ADOPTED  T12 @ 150 MAIN (754) → Mu 50.3, UTIL 52 %  ; T10 @ 200 DISTRIBUTION (393)
   DEFLECTION  Leff/d = 19.3 ; basic 20 ; fs = 0.58 × 500 × 380/754 = 146 ; pt 0.46 %
               MF ≈ 1.9 → permissible 38 > 19.3     ✔
   SHEAR  V = 33.2 kN/m ; τv 0.202 ; τc 0.479 × k 1.20 (Cl. 40.2.1.1) = 0.575  ✔ no links
   TOP STEEL  T12 @ 150 for 0.25 Leff = 800 into the flight, anchored Ld 480

LANDINGS L1 / L2 / ARRIVAL — 200 thk, spanning ACROSS the shaft
   self 7.50 + finishes 1.50 + live 7.50 + flight reaction 27.70   = 44.20 kPa
   Leff = 2800 clear + 200 bearing   Cl. 22.2(a)                    = 3000 mm
   M = 44.2 × 3.000²/8                                              = 49.7 kNm/m
   Ast,req 745 ; T12 @ 150 gives 754 = 100 % TOO TIGHT
   ADOPTED  T12 @ 125 BOTTOM (905) → Mu 59.5, UTIL 84 %
            T12 @ 125 TOP for 900 from each support ; T10 @ 200 distribution
   DEFLECTION 3000/164 = 18.3 ; fs 239 ; pt 0.552 % ; MF ≈ 1.35 → 27 > 18.3  ✔
   SHEAR  V 66.3 kN/m ; τv 0.404 < τc 0.519 × 1.20 = 0.622  ✔
```

**Compatibility notes:** the arrival landing at (−)6.100 IS the mat surface, no separate slab. Flight 3 lands directly on the 900 pressure-slab pad at (−)2.000. The landings prop W6/W7 at (−)4.733 and (−)3.367 **but only over their 1200 depth — the 400 wall design in B.2 does NOT rely on that prop.**

## B.6 Entry (approach) stairwell

> **STATUS: OUTSIDE the protective boundary, NOT blast rated (Rev F drawing note 8). Expected to be LOST in the design event.** Designed to IS 456 with normal partial factors.

```
FLIGHT — 12R @ 166.6667 / 300, 1500 wide, waist 250
   θ = 29.05°, cos θ = 0.8742
   waist 7.150 + steps 2.083 + finishes 1.000 + live 5.000 = 15.233 → wu = 22.85 kPa
   Leff = 3300 + 750 + 750    IS 456 Cl. 33.1(b)              = 4800 mm
   d = 250 − 30 − 8                                            = 214 mm
   M = 22.85 × 4.800²/8                                        = 65.8 kNm/m
   Ast,req 744 ; min 0.12 % × 250 = 300
   ADOPTED  T16 @ 200 MAIN (1005) → Mu 87.3, UTIL 75 %, x/d 0.162
            T10 @ 200 DISTRIBUTION (393)
            T16 @ 200 TOP for 1200 into the flight, anchored Ld 640
   DEFLECTION  4800/214 = 22.4 ; basic 20 ; fs 215 ; pt 0.470 % ; MF ≈ 1.5 → 30 ✔
   SHEAR  V 54.8 kN/m ; τv 0.256 ; τc 0.484 × k 1.10 = 0.532  ✔ no links

SIDE WALLS 250 — retained 2.9 m, propped by roof and raft
   σh at base = 0.5 × 20 × 2.900 + 0.5 × 10                    = 34 kPa
   M ≈ w·L²/12 on an equivalent 20 kPa UDL                     = 14.0 kNm/m
   d = 250 − 50 − 6 = 194 ; Ast,req 168
   IS 456 Cl. 32.5(a) min 0.0012 × 250 = 300 ; Cl. 32.5(b) 0.0020 × 250 = 500
   Cl. 32.5(c) two curtains required (t > 200)                 ✔
   ADOPTED  T12 @ 200 EF EW (565/face) — MINIMUM STEEL GOVERNS, 31 % utilised
   SHEAR  V ≈ 49 kN/m ; τv 0.253 < τc 0.484  ✔

RAKING ROOF 250 — 1500 clear
   self 6.25 + wp/screed 2.0 + earth lap 5.4 + IMPOSED 20      = 33.65 → wu 50.5 kPa
   (20 kPa imposed deliberately, for a stray vehicle on the berm)
   M = w·l²/12                                                  = 9.5 kNm/m
   d = 250 − 30 − 6 = 204 ; Ast,req 108 ; min 300 GOVERNS
   ADOPTED  T12 @ 200 EF EW → Mu 48.2, 20 % utilised
   SHEAR  V 38 kN/m ; τv 0.186  ✔

TOP LANDING 250 (0.000)   wu 54.9 kPa ; Leff 1750 ; M 21.0 kNm/m ; Ast,req 229
   ADOPTED  T12 @ 200 EF EW (565) → Mu 50.6, 41 % utilised
PLATFORM 250 ((−)2.000, on fill)   ADOPTED T12 @ 200 EF EW, nominal
HEADWALL 250   ADOPTED T12 @ 200 EF EW
   Door lintel over 1000 clear: 250 × 350, 3-T12 top + 3-T12 bottom, T8 @ 150
STEPPED RAFT 300 on compacted fill  ADOPTED T12 @ 200 EF EW

DETAILING — THE OPENING CORNER (the detail most often got wrong)
   At the TOP of the flight the tension face turns through 209°.  A bar bent round
   that corner has its bend resultant directed OUT of the concrete: it spalls the
   cover and the bar loses anchorage.
   MAIN BARS SHALL NOT BE BENT ROUND IT.  Each layer continued straight, CROSSED,
   anchored Ld = 640 into the OPPOSITE face, plus a U-bar T16 @ 200 across the corner.
   [SP 34:1987 Cl. 5.5 and standard detailing practice]
   At the FOOT of the flight the corner CLOSES (151°) — bars may turn normally.
```

## B.7 Entry headhouse — walls and roof

### B.7.1 Roof, 500 thk — three analyses, most conservative adopted

```
w = 383 (blast) + 12.5 (self) + 1.0 (SIDL)                      = 396.5 kPa
Panel 4000 × 5000 clear, monolithic with 400 walls on all four sides, ly/lx = 1.25
d = 500 − 75 − 10                                                = 415 mm
Mu,lim = 0.133 × 43.75 × 1000 × 415²                             = 1002 kNm/m

| # | Method                                          | M          |
| 1 | One-way fixed-fixed strip, Mp = w·Ln²/16        | 396.5 ← ADOPTED |
| 2 | IS 456 Table 26 Case 1, αx⁻ = 0.045 at 1.25     | 285.5 |
| 3 | Yield line, FIXED 4 edges, isotropic            | 162.2 |

  Method 3 formula:  wu = 48m / [a²(√(3 + (a/b)²) − a/b)²]
  VALIDATION: as b → ∞, 48/3 = 16 = the fixed-fixed strip w·L²/16 ✔
              (the 24-coefficient version gives 8 = SIMPLY SUPPORTED w·L²/8)

Ast,req (one-way basis)                                          = 1879 mm²/m
Cl. 26.5.2.1 minimum 0.12 % × 500                                =  600 mm²/m
ADOPTED  T20 @ 150 EF EW = 2094 mm²/m  →  Mu = 438.5 kNm/m
         UTILISATION  90 % one-way | 65 % Table 26 | 37 % yield line
         xu 72.3 → x/d = 0.174  ≪ 0.46

SHEAR *** NEW AND MANDATORY — NOT IN THE PHASE 1 REPORT ***
   V at d = 396.5 (2.000 − 0.415)                                = 628.4 kN/m
   τv 1.514 | τc 0.502 (pt 0.505 %) | τc,max 3.70                ✔
   (τc read at the STATIC M35 value — IS 4991 Cl. 10.3.1.1)
   Vus 420.0 kN/m ; Asv/sv 2.327 → T12 4-leg at 194
   Cl. 26.5.1.5 limit min(0.75d 311, 300) = 300
ADOPTED  T12 4-LEG @ 175 IN THE END 1200 EACH SIDE; @ 250 ELSEWHERE

DETAILING  No opening in the headhouse roof (the stair void is in the FLOOR).
           Corner torsion steel (Cl. D-1.8) NOT required — all four edges carry
           full T20 @ 150 hogging steel continuous into the walls.
           Haunch 300 × 300 at all four wall-roof junctions, diagonal T16 @ 150.
           Top steel continuous over every support, anchored Ld = 800 into the wall.
```

### B.7.2 Walls HW1–HW4, 400 thk — CONFLICT C10

```
                              CASE A (report)        CASE B (ADOPTED)
Lateral pressure              113 kPa drag           383 kPa full envelope
Mp = w × 2.400²/16            40.7 kNm/m             137.9 kNm/m
Ast,req                       221 mm²/m              766 mm²/m
Cl. 32.5(a) min vertical      480 mm²/m — governs    480
Cl. 32.5(b) min horizontal    800 mm²/m — governs    800
Utilisation on T16@150 EF EW  17 %                   59 %
Shear V at d                  97.0 kN/m              328.6 kN/m
τv                            0.283                  0.961
τc (pt 0.392 %)               0.444                  0.444
Verdict                       NO LINKS               LINKS REQUIRED

d = 400 − 50 − 8 = 342 ; Mu,lim = 681 kNm/m
ADOPTED  T16 @ 150 EF EW = 1340 mm²/m → Mu 235.2, UTIL 59 %, x/d 0.135
         Vus 176.9 kN/m ; Asv/sv 1.189 → T12 4-leg at 381
         Cl. 26.5.1.5 limit min(0.75d 256, 300) = 256 GOVERNS
ADOPTED  T12 4-LEGGED LINKS @ 250 c/c THROUGHOUT ALL FOUR WALLS

Two-way (information only, fixed 4 edges):
   HW1/HW2  4000 × 2400 → m = 69.9 kNm/m   (one-way strip 137.9)
   HW3/HW4  5000 × 2400 → m = 79.8 kNm/m   (one-way strip 137.9)

AXIAL  Roof reaction, two-way (Cl. 24.5): HW3/HW4 trapezoid 2379 kN / 5.0 m = 476 kN/m
                                          HW1/HW2 triangle  1586 kN / 4.0 m = 396 kN/m
       One-way bound: 396.5 × 2.0 = 793 kN/m ; self 29 kN/m
       Worst N = 822 kN/m → f = 2.06 N/mm² = 12 % of 0.4 fck,dyn  ✔ not critical

PRESSURE ACTS FROM INSIDE TOO.  The inner security door is NOT blast rated and the
entry stairwell is expected to be lost, so the headhouse fills and the walls are
pushed OUTWARDS.  *** THE WALLS ARE REINFORCED SYMMETRICALLY FOR 383 kPa EITHER
WAY — a stated requirement, not an accident of detailing. ***

DOOR OPENING 900 × 2100 IN HW2 — and a geometric trap
   Interrupted steel 1340 × 0.900 = 1206 mm²/face → 603 each jamb
   ADOPTED  2 No. T20 EACH JAMB EACH FACE (628), anchored Ld 800 beyond
   Door head at (−)2.000 + 2.100 = +0.100 ; roof soffit +0.400
   → ONLY 300 mm OF WALL ABOVE THE DOOR — too shallow for a lintel.
   The 300 wall and the 500 roof act TOGETHER as an 800 mm deep edge band:
   w = 383 × 2.100/2 = 402 kN/m ; M = wL²/12 = 27.1 kNm ; V = 181 kN
   d = 800 − 40 − 8 − 10 = 742 ; τv = 0.610 N/mm²
   ADOPTED  400 × 800 EDGE BAND: 4-T20 TOP + 4-T20 BOTTOM, T12 4-LEG @ 150,
            over the opening and 600 each side
   Door frame cast in and WELDED to the cage (EMP), even though the leaf is a
   security door and not blast rated.
```

### B.7.3 HW3 — the wall that has nothing under it

```
The pressure slab spans one-way in Y over 5000 clear.  HW3 runs IN the Y direction,
so its load is carried by a slab strip acting as a beam.
   b_eff = 0.400 + 2 × 1.05 (45° spread through the 900 slab)     = 2.5 m  [R]

CASE 1 — two-way roof distribution (IS 456 Cl. 24.5, correct)
   Line load 476 (trapezoid) + 29 (self)                          = 505 kN/m
   Equivalent UDL = 505/2.5 + 22.5 + 2.0                          = 226 kPa
   M = w·Ln²/16 = 226 × 25/16                                     = 354 kNm/m
   Against the slab's 1362 kNm/m capacity                         = 26 %  ✔

CASE 2 — one-way roof bound
   Line load 793 + 29 = 822 kN/m → 353 kPa → M = 552 kNm/m       = 41 %  ✔

ADOPTED  No slab change needed.  Detailed as a LINE LOAD, not as a support.
         Robustness: 4 No. T25 ADDITIONAL TOP AND BOTTOM in a 1200 mm band
         beneath HW3, lapped 1250 (50φ) into the main mesh.
```

## B.8 Sentry post

> **NOT designed for the blast, and that is a RECORDED decision.** Reflected force on the 4.0 × 6.7 m face = 1366 kPa × 26.8 m² = **36 600 kN (≈ 3730 t)**. Hardening would need ~700 mm of RC on all four above-ground faces. Not justified for a peacetime observation post.
> **All member design uses the STAAD base shear V<sub>b</sub> = 73.18 kN, not the hand-calculated 59.3 kN.**

### B.8.1 Seismic member forces — portal method at V<sub>b</sub> = 73.18 kN

```
Q_roof  = 73.18 × (315.9 × 6.25²)/Σ                              = 59.51 kN
Q_floor = 73.18 × (276.8 × 3.20²)/Σ                              = 13.67 kN
Column shear, ground storey = 73.18/4  (= STAAD Fx 18.295) ✔      = 18.30 kN
Column shear, first storey  = 59.51/4                             = 14.88 kN
Column moment, ground = 18.30 × 3.200/2                           = 29.27 kNm
Column moment, first  = 14.88 × 3.050/2                           = 22.69 kNm
Beam moment, first-floor joint (corner joint, one beam) = 29.27 + 22.69 = 51.96 kNm
Beam moment, roof joint                                           = 22.69 kNm
Axial from overturning — READ DIRECTLY FROM THE STAAD REACTIONS:
   EQ+X  Fy = ± 36.127 kN      EQ+Z  Fy = ± 27.891 kN   → 36.127 governs
```

### B.8.2 Frame analysis assumption — stated, not hidden

```
Single-bay portal each direction.  Beams are NOT fully fixed; the joint rotates.
Slope-deflection with symmetric loading:
   I_beam = 250 × 450³/12 = 1.8984e9 mm⁴ ; I_col = 350⁴/12 = 1.2505e9 mm⁴
   Kc (first-floor joint) = 4EI/3200 + 4EI/3050 = 3.203e6·E
   M_support = −FEM + (2EI_b/L_b)·θ ,  θ = FEM/(2EI_b/L_b + Kc)

| Beam | FEM   | 2EI/L      | Reduction | M_support | M_midspan |
| B1, 1.5(DL+LL) | 39.49 | 1.040e6 E | ×0.755 | 29.81 | 30.90 |
| B1, DL only    | 22.53 | —         | ×0.755 | 17.01 | — |
| B2, 1.5(DL+LL) | 70.60 | 0.8165e6 E| ×0.797 | 56.26 | 49.64 |
| B2, DL only    | 39.21 | —         | ×0.797 | 31.25 | — |
```

### B.8.3 Slab S1 — 150 thk two-way

```
Cover 30 (Table 16, moderate) ; T8 bars
   dx = 150 − 30 − 4 = 116 mm      dy = 150 − 30 − 8 − 4 = 108 mm
Clear spans 3400 and 4400
Effective span, IS 456 Cl. 22.2(a) — lesser of clear + d, or c/c:
   lx = min(3400 + 116, 3650) = 3516     ly = min(4400 + 108, 4650) = 4508
   ly/lx = 1.282  < 2  → TWO-WAY   Cl. 24.4 / Annex D

MOMENT COEFFICIENTS — IS 456 Table 26 (Annex D-1.1) Case 9, four edges
   discontinuous but RESTRAINED, with corner torsion steel per Cl. D-1.8
   → Table 26, NOT Table 27.
   αx = 0.0777 (interpolated at 1.282)   αy = 0.056

wu = 1.5(4.750 + 3.000) = 11.625 kPa   (the FIRST FLOOR governs; roof = 10.125)
   Mx = 0.0777 × 11.625 × 3.516²                                 = 11.17 kNm/m
   My = 0.0560 × 11.625 × 3.516²                                 =  8.05 kNm/m
   Ast,req x = 229 ; y = 176 ; Cl. 26.5.2.1 min 0.12 % × 150     =  180 mm²/m
   Cl. 26.5.2.2 max bar dia D/8 = 18.75 ✔ ; Cl. 26.3.3(b) max spacing 3d or 300 ✔
ADOPTED  T8 @ 150 c/c BOTH WAYS BOTTOM = 335 mm²/m
   Mu = 16.09 (x) / 14.92 (y) kNm/m → UTILISATION 69 % / 54 %
   xu = 13.5 → x/d = 0.116 / 0.125

DEFLECTION  lx/dx = 3516/116 = 30.3 ; basic taken as SIMPLY SUPPORTED = 20
   fs = 0.58 × 500 × 229/335 = 198 ; pt = 0.289 % ; MF (Fig. 4) ≈ 1.68
   Permissible 20 × 1.68 = 33.6 > 30.3   ✔
   (as continuous, basic = 26 and the margin doubles — it passes on the
    conservative assumption, so that assumption is used)

SHEAR  Vu ≈ wu·lx/3 = 13.6 kN/m ; τv 0.117 ; τc 0.390 × k 1.30 (D ≤ 150) = 0.507 ✔

DETAILING — IS 456 ANNEX D
   Cl. D-1.2/D-1.3  middle strip = ¾ width, edge strips = ⅛ each side;
                    Table 26 moments apply to MIDDLE STRIPS ONLY
   Cl. D-1.4        50 % of midspan bottom steel extends to within 0.1 L of a
                    discontinuous edge; remainder curtailed at 0.25 L
   Cl. D-1.6        AT EVERY DISCONTINUOUS EDGE provide top steel = 50 % of the
                    midspan bottom steel, extending 0.1 L = 400 mm into the span
                    → ADOPTED  T8 @ 300 TOP, 400 wide band, all four edges
   Cl. D-1.7        edge strips: minimum reinforcement only
   Cl. D-1.8        TORSION AT CORNERS — both edges discontinuous at all four
                    corners → steel = ¾ of the midspan area, in FOUR layers
                    (2 top + 2 bottom, each way), over lx/5 = 700 mm each way
                    → ADOPTED  T8 @ 200, 4 LAYERS, 700 × 700 AT EACH CORNER
   *** THE TORSION MATS ARE A HOLD POINT FOR REINFORCEMENT INSPECTION.  Table 26
   is valid only because they are provided.  Omit them and the slab must be
   reassessed on Table 27. ***
```

### B.8.4 Beam B1 — 250 × 450, span 3650

```
IS 13920:2016 section limits:  b ≥ 200 ✔ (250) | b/D = 0.556 ≥ 0.3 ✔ |
                               clear span/D = 3300/450 = 7.33 ≥ 4 ✔
d = 450 − 30 − 8 − 8 = 404 ; Mu,lim = 0.133 × 30 × 250 × 404² = 162.8 kNm

| Combination                                | M_support hogging |
| 1.5(DL + LL)                               | 29.8  |
| 1.2(DL + LL + EL) = 1.2(19.87 + 51.96)     | 86.2  |
| 1.5(DL + EL) = 1.5(17.01 + 51.96)          | 103.5 ← GOVERNS |
| 0.9 DL + 1.5 EL                            | 93.2  |

Mu = 103.5 < 162.8 → singly reinforced ; Ast,req = 661 mm²
ADOPTED  4-T16 TOP AT SUPPORTS (804) → Mu = 122.6 kNm, UTIL 84 %, x/d 0.321

BOTTOM  Reversal 1.5(17.01 − 51.96) = −52.4 kNm sagging → Ast,req 313
        IS 13920 Cl. 6.2.3: positive steel at joint face ≥ 50 % of negative
           = 0.5 × 804 = 402 mm² ← GOVERNS
        Midspan sagging 30.9 kNm → Ast,req 181
        IS 13920 Cl. 6.2.1(b) ρmin = 0.24√fck/fy = 0.00263 × 250 × 404 = 266
        IS 456 Cl. 26.5.1.1 As,min = 0.85bd/fy = 172
        IS 13920 Cl. 6.2.2 ρmax = 0.025 → 2525 ✔
        Cl. 6.2.4 top or bottom ≥ 25 % of max at joint face = 201 ✔
ADOPTED  2-T16 BOTTOM CONTINUOUS (402) → Mu = 66.0 kNm, x/d 0.160

SHEAR — capacity design, IS 13920 Cl. 6.3.3
   Vu = 1.2(D+L)·L/2 ± 1.4(Mu^As + Mu^Bh)/L
   Unfactored gravity total = 54.29 (UDL) + 25.81 (triangle) = 80.1 kN
   1.2 × 80.1/2 = 48.1 ;  1.4 × (122.6 + 66.0)/3.650 = 72.3
   Vu = 120.4 kN ; τv = 1.192 N/mm² ; τc,max (Table 20, M30) 3.50 ✔
   *** IS 13920 Cl. 6.3.4: EQ share 72.3/120.4 = 60 % ≥ 50 %, no axial
       → τc TAKEN AS ZERO in the plastic hinge region ***
   Asv/sv = 120.4e3/(0.87 × 500 × 404) = 0.685 → T8 2-leg at 147
   Cl. 6.3.5.1 hinge region (2d = 810 from each face):
       sv ≤ min(d/4 = 101, 8 × 16 = 128), need not be < 100 → 100 mm
   Cl. 6.3.5.2 elsewhere: sv ≤ d/2 = 202
ADOPTED  T8 2-LEGGED HOOPS @ 100 c/c OVER 2d = 810 FROM EACH FACE;
         T8 @ 150 c/c ELSEWHERE.  First hoop within 50 mm of the column face.
DEFLECTION  l/d = 3650/404 = 9.0 ≪ 20 ✔
```

### B.8.5 Beam B2 — 250 × 450, span 4650

```
| Combination                                | M_support hogging |
| 1.5(DL + LL)                               | 56.3  |
| 1.2(DL + LL + EL) = 1.2(37.51 + 51.96)     | 107.4 |
| 1.5(DL + EL) = 1.5(31.25 + 51.96)          | 124.8 ← GOVERNS |
| 0.9 DL + 1.5 EL                            | 106.1 |

Mu = 124.8 < 162.8 ✔ ; Ast,req = 822 mm²
ADOPTED  3-T20 TOP AT SUPPORTS (942) → Mu = 139.8 kNm, UTIL 89 %, x/d 0.376
   *** 3-T20 chosen over 5-T16: five T16 need 256 mm in a 250 wide beam ***
BOTTOM   Cl. 6.2.3 → 0.5 × 942 = 471 ; midspan 49.6 kNm → Ast,req 297
ADOPTED  2-T20 BOTTOM CONTINUOUS (628) → Mu = 98.9 kNm, 50 % utilised, x/d 0.250

SHEAR    Unfactored gravity (UDL-equivalent) = 26.115 × 4.650 = 121.4 kN
   1.2 × 121.4/2 = 72.8 ; 1.4 × (139.8 + 98.9)/4.650 = 71.9
   Vu = 144.7 kN ; τv = 1.433 ; τc,max 3.50 ✔
   EQ share 71.9/144.7 = 49.7 % — a hair under the Cl. 6.3.4 50 % trigger.
   *** TAKEN AS TRIGGERED (τc = 0): a design must not turn on the third
       decimal place of a ratio. ***
   Asv/sv = 0.823 → T8 2-leg at 122 ; hinge spacing 100 governs
   Outside the hinge, V falls to ~124 kN and τc = 0.641 (pt 0.933 %) may be used
   → Asv/sv 0.337 → T8 at 298
ADOPTED  T8 @ 100 OVER 810 FROM EACH FACE ; T8 @ 150 ELSEWHERE
DEFLECTION  l/d = 4650/404 = 11.5 ≪ 20 ✔
```

### B.8.6 Column C1 — 350 × 350

```
SLENDERNESS  clear height ground = 3650 − 450 − 450 (beam depth) = 2750 mm
   Effective length factor 1.2 (Table 28, unbraced, both ends restrained)
   lex = 3300 ; lex/D = 9.43 < 12 → SHORT COLUMN   IS 456 Cl. 25.1.2 ✔
MIN ECCENTRICITY  emin = l/500 + D/30 = 5.5 + 11.67 = 17.2, but ≥ 20 → 20 mm
   Mmin = 276.8 × 0.020 = 5.5 kNm ≪ applied ✔   IS 456 Cl. 25.4

AXIAL   Per column unfactored: DL 148.4 kN, LL 19.1 kN ; EQ axial ± 36.127 kN
   1.5(DL + LL) = 251.3 ; 1.5(DL + EL) = 276.8 ← max ; 1.5(DL − EL) = 168.4 ← min

LONGITUDINAL STEEL   IS 456 Cl. 26.5.3.1: min 0.8 % = 980 ; max 6 % = 7350
ADOPTED  8-T16 = 1608 mm² → p = 1.31 %  ; bars on all four faces
   Cover 40 (Cl. 26.4.2.2) ; d′ = 40 + 8 + 8 = 56 ; d′/D = 0.16

UNIAXIAL CAPACITY — computed from the IS 456 Cl. 38.1 stress block and the Fe500
design curve (Fig. 23B), NOT read off a chart:
   | Pu (kN) | Mu1 (kNm) |
   | 168.4   | 105.8 |
   | 251.3   | 111.7 |
   | 276.8   | 112.9 |

BIAXIAL — IS 456 Cl. 39.6
   Puz = 0.45 fck Ac + 0.75 fy Asc = 0.45 × 30 × 120892 + 0.75 × 500 × 1608
       = 2235 kN
   Pu/Puz = 276.8/2235 = 0.124 < 0.2 → αn = 1.0
   Worst case, EQ in Z with 30 % in X (IS 1893 Cl. 6.3.2.2):
      Mux = 25.6 kNm ; Muy = 66.8 kNm
      25.6/112.9 + 66.8/112.9 = 0.227 + 0.592 = 0.819 ≤ 1.0  ✔

STRONG COLUMN – WEAK BEAM — IS 13920 Cl. 7.2.1, ΣMc ≥ 1.4 ΣMb
   | Joint                      | ΣMb   | 1.4 ΣMb | ΣMc            | Verdict |
   | First floor, X (B1)        | 122.6 | 171.6   | 112.9+101=213.9| ✔ |
   | First floor, Z (B2)        | 139.8 | 195.7   | 213.9          | ✔ |
   | Roof, Z (B2 roof, 2-T20)   |  98.9 | 138.5   | 101            | ✔ marginal |

TRANSVERSE REINFORCEMENT
   General, IS 456 Cl. 26.5.3.2: tie dia ≥ max(6, φ/4) = 8 ; spacing ≤
      min(350, 16φ = 256, 300) = 256
   IS 13920 Cl. 7.4: hoops over the full length at ≤ half the least dimension = 175
ADOPTED  T8 HOOPS @ 150 c/c outside the confining zone

   SPECIAL CONFINING REINFORCEMENT — IS 13920 Cl. 8.1
      lo ≥ max(350, clear height/6 = 458, 450)                    = 500 mm
      spacing ≤ ¼ × 350 = 87.5, but 75 ≤ s ≤ 100                  = 85 mm
      Ash = 0.18 s·h·(fck/fy)·[(Ag/Ak) − 1]
          h = 350 − 2 × 40 = 270 ; Ag = 122500 ; Ak = 270² = 72900
          = 0.18 × 85 × 270 × (30/500) × (1.680 − 1)              = 168.5 mm²
      minimum = 0.05 × 85 × 270 × 30/500                          =  68.9 mm²
ADOPTED  T10 HOOPS + ONE CROSS-TIE EACH WAY @ 85 c/c (3 legs × 78.5 = 235.5 ✔)
         over 500 mm from every joint face, top and bottom of every column,
         AND THROUGH THE JOINT (Cl. 8.2)

DRIFT — IS 1893 Cl. 7.11.1: limit 0.004 × storey height = 12.8 mm (ground),
        12.2 mm (first).  Calculated drift under 3 mm.  ✔ Not critical, but checked.
```

### B.8.7 Isolated footing F1 — 1500 × 1500 × 600 on in-situ basalt at (−)2.000

```
> Founded on IN-SITU ROCK, never on backfill.  This is the whole reason the sentry
> post was relocated ≥ 10 m clear of the shelter excavation.

SERVICE  P = 167.5 (col) + 36.1 (EQ axial) + 33.75 (footing self)  = 237.4 kN
         M (base, EQ)                                              = 29.3 kNm
         e = 29.3/237.4 = 0.123 m < L/6 = 0.250  → NO TENSION      ✔
         qmax = P/A(1 + 6e/L) = 105.5 × 1.494                      = 157.6 kPa
         vs presumptive SBC 3240 kPa (IS 1904 Table 1) [A]         = 4.9 %  ✔

ULS      Governing 1.5(DL + EL): Pu = 1.5(148.4 + 36.127)          = 276.8 kN
         Mu = 1.5 × 29.27                                          =  43.9 kNm
         eu = 0.128 ; qu,max = 276.8/2.25 × (1 + 6×0.128/1.5)      = 190.0 kPa

FLEXURE  Cantilever from the column face = (1500 − 350)/2          = 575 mm
         Mu = 190.0 × 0.575²/2                                     = 31.4 kNm/m
         d = 600 − 50 (Cl. 26.4.2.1) − 8                           = 542 mm
         Ast,req 136 ; Cl. 26.5.2.1 min 0.12 % × 600 = 720 ← GOVERNS
ADOPTED  T12 @ 150 c/c BOTH WAYS BOTTOM (754 mm²/m), x/d 0.056

ONE-WAY SHEAR  IS 456 Cl. 34.2.4.1, critical at d from the column face:
         575 − 542 = 33 mm from the edge ; Vu = 6.3 kN/m ; τv = 0.012 ✔
PUNCHING  IS 456 Cl. 31.6.1, critical perimeter at d/2:
         b0 = 4 × (350 + 542) = 3568 ; Vu = 276.8 − 190.0 × 0.892² = 125.6 kN
         τv = 0.065 ; ks = (0.5 + βc) ≤ 1.0 = 1.0 ;
         τc = 0.25√30 (Cl. 31.6.3.1) = 1.369  ≫ 0.065  ✔
ANCHORAGE  Column starters T16: Ld,compression = 37 × 16 = 592 mm
         Available 600 − 50 − 24 = 526 straight + 8φ bend 128 = 654  ✔
*** THE 600 mm DEPTH IS GOVERNED BY THE ANCHORAGE OF THE COLUMN STARTERS, NOT BY
    BENDING OR SHEAR — stated so that nobody "optimises" it to 350. ***
```

---

# PART C — WHAT IS NOT DEMONSTRATED

> **This section must be reproduced in every future revision. It is the boundary of the design's validity.**

**Demonstrated to IS 456:** ultimate flexural capacity, diagonal-tension shear, minimum and maximum steel, bar spacing, cover, development and anchorage, deflection, crack-width provisions, biaxial column interaction, punching and one-way shear in the footing, and ductile detailing to IS 13920 for the sentry post frame.

**NOT demonstrated, and NOT claimed:**

1. **Support rotation / ductility ratio for the blast case.** θ ≤ 2° corresponds to δ ≤ 87 mm = span/57 and requires a **non-linear SDOF check** (IS 4991 Fig. 6 / Biggs) or explicit non-linear FE with strain-rate-dependent materials. **Phase 3.**
2. **Shock-wave propagation down the entry shaft** and the resulting door loading — CFD or shock tube [V].
3. **Transient soil–structure interaction** — participating mass, arching, interface pressure ratios.
4. **Blast door, valve and hatch performance** — vendor-tested [V], not a civil deliverable.
5. **Global flotation cannot be shown by an elastic-mat model** — the springs take tension, so in the model the mat never lifts. It is a hand check on real dimensions (B.3). *Anyone who says "the analysis shows no uplift" has misunderstood their own model.*
6. **The berm's actual pressure-transmission factor K<sub>a</sub>** — removed from the critical path by designing the headhouse walls to the upper bound (C10).

> **A conventional static STAAD.Pro analysis gives the correct DEMAND. It is not, and must never be presented as, proof of blast resistance.**
> **IS 4991:1968 Cl. 1.1 expressly EXCLUDES nuclear explosions from its scope.** It is used here for its loading rules and dynamic material strengths only, as a documented conservative extrapolation. Every structural capacity is computed to IS 456.

---

# PART D — STAAD.PRO MASTER MODEL SPECIFICATION

> ## ⚠ CRITICAL LIMITATION — READ FIRST
> **⚠ UPDATED 3 September 2026 — the three `.std` files ARE now in the workspace** (`Underground_Structure_WITH_LOADS_worked_example (4).STD`, `Sentry_Post_Framed_Seismic.std`, and `Entry_Stairwell.std`, which is not registered anywhere else in this document). Part D below was written **before** they arrived and its evidence tags are left exactly as written. Everything in Part D was extracted from **nineteen screen captures** of the STAAD.Pro interface. Node tables, member tables, load-case titles and reaction tables were read directly from those images and are marked **[CONFIRMED]**. Anything derived by back-calculation is marked **[RECONSTRUCTED]**. Anything not visible in a screenshot is marked **[NOT AVAILABLE — DO NOT INVENT]**. Where Part D and a `.std` file now disagree, **the file is the primary evidence** — see the K.1 update note.
>
> **The `.std` files are now available, so a claim about the model must be checked against the file itself rather than against Part D.** Part D is retained as the screenshot-derived record and as the audit trail for what was known before 3 Sep 2026.

## D.1 Model inventory

| Model | File in `current/staad/` | Role | Status |
|---|---|---|---|
| Underground box — reference | `Underground_Structure_WITH_LOADS_worked_example (4).STD` | The reconciled Phase 2 Rev A + M1 plate model. **Every Part B box value is checked against this one** | [CONFIRMED] |
| Sentry post | `Sentry_Post_Framed_Seismic.std` | Two-storey RC frame, seismic | [CONFIRMED] |
| Entry stairwell | `Entry_Stairwell.std` | Covered approach stairwell, **static only, not blast rated** (Part B.6) | [CONFIRMED] |
| Underground box — COARSE | `Underground_Shelter_Mesh_Coarse.std` | Mesh sensitivity study **MS1** (Part H.5) — 324 joints, 336 plates | [CONFIRMED] |
| Underground box — MEDIUM | `Underground_Shelter_Mesh_Medium.std` | MS1 reference mesh, copy of the model above — 1 113 joints, 1 138 plates | [CONFIRMED] |
| Underground box — FINE | `Underground_Shelter_Mesh_Fine.std` | MS1 h/2 refinement — 4 500 joints, 4 552 plates | [CONFIRMED] |
| Underground box — **k<sub>s</sub> UPPER BOUND** | `Underground_Shelter_ks500000.std` | **RC4 (H.28).** The reference model at **k<sub>s</sub> = 500 000** — `ELASTIC MAT SUBGRADE` and the four corner `KFY` (×5) are **the only lines that differ**; verified by diff | [CONFIRMED] |

> **RC3 correction, 11 September 2026 (Part H.27).** This table listed **two** models, named
> from the STAAD screen captures, and Part L still read *"2 models exist; .std NOT uploaded;
> screenshots only."* **Six `.std` files are in the workspace and have been read, reconciled
> and edited in it** — the underground box and `Entry_Stairwell.std` at **M1** (H.4), the three
> mesh models built at **MS1** (H.5), and all four box models corrected at **MS2** (H.26).
> The screen captures are no longer the only evidence of anything. **No model value changes.**

**Units:** metres and kilonewtons throughout (node table headed "X m / Y m / Z m", reactions "kN", moments "kN-m"). [CONFIRMED]
**Coordinate system:** STAAD global — **Y is vertical**, X and Z horizontal. [CONFIRMED]

## D.2 SENTRY POST MODEL — `Sentry_Post_Framed_Seismic`

### D.2.1 Nodes — [CONFIRMED, read from the geometry table]

| Node | X (m) | Y (m) | Z (m) | Level |
|---|---|---|---|---|
| 1 | 0.175 | 0.450 | 0.175 | base, grid A-1 |
| 2 | 0.175 | 0.450 | 4.825 | base, grid A-2 |
| 11 | 3.825 | 0.450 | 0.175 | base, grid B-1 |
| 12 | 3.825 | 0.450 | 4.825 | base, grid B-2 |
| 101 | 0.175 | 3.650 | 0.175 | first floor, A-1 |
| 102 | 0.175 | 3.650 | 4.825 | first floor, A-2 |
| 111 | 3.825 | 3.650 | 0.175 | first floor, B-1 |
| 112 | 3.825 | 3.650 | 4.825 | first floor, B-2 |
| 201 | 0.175 | 6.700 | 0.175 | roof, A-1 |
| 202 | 0.175 | 6.700 | 4.825 | roof, A-2 |
| 211 | 3.825 | 6.700 | 0.175 | roof, B-1 |
| 212 | 3.825 | 6.700 | 4.825 | roof, B-2 |
| 213 | — | — | — | **[NOT AVAILABLE]** — row visible but values cut off by the scroll |

**Node numbering convention [RECONSTRUCTED]:** base = 1/2/11/12, first floor = +100, roof = +200; the second digit pair encodes the grid (01 = A-1, 02 = A-2, 11 = B-1, 12 = B-2).

### D.2.2 Members — [CONFIRMED, read from the beam table]

| Beam | Node A | Node B | Property ref | Interpretation |
|---|---|---|---|---|
| 1 | 1 | 101 | 1 | ground-storey column A-1 |
| 2 | 2 | 102 | 1 | ground-storey column A-2 |
| 3 | 11 | 111 | 1 | ground-storey column B-1 |
| 4 | 12 | 112 | 1 | ground-storey column B-2 |
| 5 | 101 | 201 | 1 | first-storey column A-1 |
| 6 | 102 | 202 | 1 | first-storey column A-2 |
| 7 | 111 | 211 | 1 | first-storey column B-1 |
| 8 | 112 | 212 | 1 | first-storey column B-2 |
| 9 | 101 | 111 | 2 | first-floor beam, grid 1, spans X (**B1**, 3650) |
| 10 | 102 | 112 | 2 | first-floor beam, grid 2, spans X (**B1**, 3650) |
| 11 | 101 | 102 | 2 | first-floor beam, grid A, spans Z (**B2**, 4650) |
| 12 | 111 | 112 | 2 | first-floor beam, grid B, spans Z (**B2**, 4650) |
| 13 | 201 | 211 | 2 | roof beam, grid 1 (**B1**) |
| 14 | 202 | 212 | 2 | roof beam, grid 2 (**B1**) |
| 15 | 201 | 202 | 2 | roof beam, grid A (**B2**) |
| 16 | 211 | 212 | 2 | roof beam, grid B (**B2**) — **[RECONSTRUCTED]**, row not visible but required for a closed frame |

**Property references [RECONSTRUCTED from the drawings, consistent with the member layout]:**
- **Property 1 = column, 350 × 350 rectangular**
- **Property 2 = beam, 250 × 450 rectangular**

**Member releases / offsets:** **[NOT AVAILABLE]** — no release or offset table was captured. The reaction pattern (all six components present at every base node, beam-end moments transferred to columns) is consistent with **no releases**, but this must be confirmed against the `.std` file.

**Slab S1 is NOT modelled as plates.** The slab load is applied to the beams as triangular/trapezoidal loading per the framing-plan schedule. [RECONSTRUCTED — no plate table appears in any sentry post screenshot, and the framing plan gives explicit peak beam intensities.]

### D.2.3 Supports — [CONFIRMED]

**Type: FIXED at all four base nodes (1, 2, 11, 12) at Y = +0.450.**
Evidence: the support-reaction table reports **all six components** (Fx, Fy, Fz, Mx, My, Mz) at every base node, and the plot symbols are the STAAD fixed-support hatched square.

**Justification [CONFIRMED, from the design]:** the columns sit on isolated footings on **in-situ rock**. Rotational restraint is real. On backfill it would not be defensible.

### D.2.4 Load cases — [CONFIRMED, load-case titles read verbatim]

| # | Title as it appears in STAAD |
|---|---|
| 1 | `DL SELFWEIGHT SLAB INFILL PARAP...` (truncated in the capture) |
| 2 | `LL AS PER IS 875 PART 2` |
| 3 | `EQ+X IS 1893 VB 73.18 KN` |
| 4 | `EQ-X IS 1893 VB 73.18 KN` |
| 5 | `EQ+Z IS 1893 VB 73.18 KN` |
| 6 | `EQ-Z IS 1893 VB 73.18 KN` |

**Applied load totals — [CONFIRMED, from the Statics Check Results table]:**

| L/C | ΣF<sub>x</sub> | ΣF<sub>y</sub> | ΣF<sub>z</sub> | ΣM<sub>x</sub> | ΣM<sub>y</sub> |
|---|---|---|---|---|---|
| 1 (DL) | 0.000 | **−624.548** | 0.000 | 1561.369 | 0.000 |
| 2 (LL) | 0.000 | **−76.376** | 0.000 | 190.941 | 0.000 |
| 3 (EQ+X) | **73.180** | 0.000 | 0.000 | 0.000 | 182.950 |
| 4 (EQ−X) | −73.180 | 0.000 | 0.000 | 0.000 | −182.950 |
| 5 (EQ+Z) | 0.000 | 0.000 | **73.180** | 436.631 | −146.360 |

Difference between Loads and Reactions = 0.000 in every case → **statics check passes**. [CONFIRMED]

**Back-calculated load geometry — [RECONSTRUCTED]:**
```
LC1  Mx/Fy = 1561.369/624.548 = 2.500 m  → Z-centroid of dead load = mid-width ✔
LC3  My/Fx =  182.950/73.180  = 2.500 m  → Z-centroid of the X seismic load ✔
LC5  My/Fz = −146.360/73.180  = 2.000 m  → X-centroid of the Z seismic load ✔
LC5  Mx/Fz =  436.631/73.180  = 5.967 m  → HEIGHT centroid above Y = 0

Solving the two-level distribution from the height centroid:
   Qr × 6.700 + Qf × 3.650 = 436.631   and   Qr + Qf = 73.180
   → Q_roof  = 55.57 kN at +6.700
   → Q_floor = 17.61 kN at +3.650
Compare the hand Wh² distribution: Q_roof 59.51, Q_floor 13.67.
→ THE MODEL'S VERTICAL DISTRIBUTION IS SLIGHTLY DIFFERENT FROM THE HAND CHECK.
  Design used the hand distribution at the STAAD total (73.18 kN), which gives a
  LARGER column moment at the ground storey.  Conservative.  See CONFLICT C9.
```

### D.2.5 Support reactions, node 1 — [CONFIRMED, read from the reaction table]

| L/C | F<sub>x</sub> kN | F<sub>y</sub> kN | F<sub>z</sub> kN | M<sub>x</sub> kNm | M<sub>y</sub> kNm |
|---|---|---|---|---|---|
| 1 DL SELFWEIGHT | 3.519 | 156.137 | 6.237 | 6.573 | 0.000 |
| 2 LL | 0.588 | 19.094 | 1.209 | 1.272 | −0.000 |
| 3 EQ+X | **−18.295** | **−36.127** | −0.000 | −0.000 | 0.000 |
| 4 EQ−X | 18.295 | 36.127 | 0.000 | 0.000 | −0.000 |
| 5 EQ+Z | −0.000 | **−27.891** | **−18.295** | **−36.078** | 0.000 |
| 6 EQ−Z | 0.000 | 27.891 | 18.295 | 36.078 | −0.000 |
| 101 1.5DL+1.5LL | 6.160 | 262.847 | 11.168 | 11.767 | 0.000 |
| 102 | −17.026 | 166.926 | 8.935 | 9.413 | −0.000 |
| 103 | 26.882 | 253.630 | 8.935 | 9.413 | −0.000 |
| 104 | 4.928 | 176.808 | −13.019 | −33.881 | 0.000 |
| 105 | 4.928 | 243.747 | 30.889 | 52.707 | 0.000 |
| 106 1.5DL+1.5EQ+X | −22.165 | 180.016 | 9.355 | 9.859 | 0.000 |
| 107 1.5DL+1.5EQ−X | 32.720 | 288.396 | 9.355 | 9.859 | 0.000 |

**Two key confirmations from this table:**
1. **F<sub>x</sub> = 18.295 kN per column × 4 = 73.18 kN** — the portal-method distribution used in design is exactly what the model produces. [CONFIRMED]
2. **F<sub>y</sub> = ± 36.127 kN (EQ+X) and ± 27.891 kN (EQ+Z)** — these ARE the seismic axial couples used in the column design. They were read from the model, not calculated by hand. [CONFIRMED]

### D.2.6 Analysis and design commands — **[NOT AVAILABLE — DO NOT INVENT]**

No screenshot shows the STAAD editor, the `PERFORM ANALYSIS` line, P-Delta settings, `DESIGN BEAM`/`DESIGN COLUMN` blocks, or any design parameter (`FYMAIN`, `FC`, `RATIO`, `TRACK`, `CLEAR`, etc.).
**A future Claude must not state what these are. Ask for the `.std` file.**

**What the design work in this project actually used instead:** hand calculations to IS 456 and IS 13920 (Part B.8), taking only the *forces* from the model. No STAAD concrete-design output was relied upon.

## D.3 UNDERGROUND MODEL — `Underground_Structure_WITH_LOADS_worked_example (4)`

### D.3.1 Model form — [CONFIRMED from the plots]

A **plate + beam mid-surface model** of the whole box: mat, four perimeter walls, internal walls and the pressure slab, meshed on a regular grid. The plots show a dense orthogonal mesh over the full 22 m × 6.2 m footprint with support symbols at every mat node.

**Beam table shows 1139 members.** [CONFIRMED]
**Plate table: [NOT AVAILABLE]** — the plate list was never displayed in any capture.

### D.3.2 Nodes — partial, [CONFIRMED for the rows visible]

| Node | X (m) | Y (m) | Z (m) |
|---|---|---|---|
| 1 | 0.300 | 0.300 | 0.3 |
| 2 | 0.300 | 0.300 | 0.8 |
| 3 | 0.300 | 0.300 | 1.3 |
| 4 | 0.300 | 0.300 | 2.0 |
| 5 | 0.300 | 0.300 | 2.7 |
| 6 | 0.300 | 0.300 | 3.3 |
| 7 | 0.300 | 0.300 | 4.0 |
| 8 | 0.300 | 0.300 | 4.6 |
| 9 | 0.300 | 0.300 | 5.2 |
| 10 | 0.300 | 0.300 | 5.9 |
| 11 | 0.825 | 0.300 | 0.3 |
| 12 | 0.825 | 0.300 | 0.8 |
| 13 | 0.825 | 0.300 | 1.3 |
| 14 | 0.825 | 0.300 | 2.0 |
| 15 | 0.825 | 0.300 | 2.7 |

**Interpretation [RECONSTRUCTED — important for anyone rebuilding this model]:**
```
The model uses MID-SURFACE geometry, and the model origin Y = 0 is at the
UNDERSIDE OF THE MAT, i.e. real level (−)6.700.
   Y = 0.300 = the mid-plane of the 600 mat                    ✔
   Z = 0.300 and Z = 5.900 = the mid-planes of the 600 perimeter walls
       (real Y-plan 0–600 → mid 300 ; 5600–6200 → mid 5900)    ✔
   X = 0.300 = the mid-plane of the 600 west end wall           ✔
   Mesh pitch in Z ≈ 0.5 to 0.7 m ; in X the second line is at 0.825
```
> **This means the model's Y-axis is offset from the project level datum by 6.700 m.**
> `Project level = model Y − 6.700`. A future Claude must apply this offset when comparing model output to the drawings.

**All other nodes: [NOT AVAILABLE]** — only rows 1–15 were captured.

### D.3.3 Supports — [RECONSTRUCTED]

The plots show support symbols at **every node of the mat**, and the design basis (Part A.6) specifies a modulus of subgrade reaction of 100 000–500 000 kN/m³. This is consistent with **elastic foundation (spring) supports, vertical only, on every mat node**, generated from k<sub>s</sub>.

**The actual STAAD command (`ELASTIC MAT`, `PLATE MAT`, or explicit `SPRING` entries) is [NOT AVAILABLE].**

> **⚠ MODELLING WARNING THAT MUST NOT BE LOST:** spring supports in STAAD **take tension** unless explicitly declared compression-only. In the model the mat therefore never lifts, and **the flotation check of Part B.3 CANNOT be performed in STAAD.** It is a hand calculation on real dimensions and real weights.

### D.3.4 Load cases — [CONFIRMED, titles read verbatim]

| # | Title as it appears in STAAD | Value |
|---|---|---|
| 1 | `DL1 SELF WEIGHT` (`SELFWEIGHT Y -1`) | auto |
| 2 | `DL2 EARTH COVER ON ROOF 40.65 KN/M2` | 40.65 kPa |
| 3 | `DL3 SIDL SERVICES AND FINISHES` | 2.0 kPa |
| 4 | `LL1 LIVE LOAD ON INTERNAL FLOOR 5.0 KN/...` | 5.0 kPa |
| 5 | `DL4 STAIRCASE ON THE TWO SHAFT WAL...` | 2.947 kPa |
| 6 | `EP1 EARTH + WATER ON EXTERNAL WAL...` | 33.9 → 83.2 kPa |
| 7 | `HY1 HYDROSTATIC UPLIFT ON MAT 46.1 KN...` | 46.11 kPa |
| 8 | **`BL1 BLAST ON ROOF 383 KN/M2`** | **383 kPa** |
| 9 | **`BL2 BLAST ON EXTERNAL WALLS 383 KN/...`** | **383 kPa** |
| 10 | `LL2 CONSTRUCTION SURCHARGE 20.0 KN` | 20.0 kPa |

**Load combinations — [CONFIRMED, titles read verbatim]**

| # | Title |
|---|---|
| 101 | `ULS STATIC 1.5(DL+LL+EARTH+WATE...` |
| 102 | `ULS UPLIFT 0.9DL + 1.5 HYDROSTATIC` |
| 103 | `BLAST 1.0(DL + EARTH + WATER + BLAST...` |
| 104 | `SLS 1.0(DL+LL+EARTH+WATER) FOR CR...` |
| 105 | `CONSTRUCTION 1.5(DL + EARTH + WATE...` |

A **Load Envelopes** entry exists in the tree but its contents were **[NOT AVAILABLE]**.

### D.3.5 Underground model results — **[NOT AVAILABLE — DO NOT INVENT]**

No post-processing screenshot for the underground model was provided: no plate moments, no reactions, no deflections, no design ratios, no warnings.

**Every underground design value in Part B was produced by hand calculation, not by STAAD output.** The model provides the demand distribution and the visual check that loads are applied to the correct faces.

## D.4 What a future Claude must obtain before extending the STAAD work

1. **The two `.std` files themselves** — everything above is screenshot-derived.
2. The **plate table** for the underground model (thicknesses, connectivity, material).
3. The **support definition** for the underground model, and whether the springs are compression-only.
4. The **analysis and design command blocks** for both models.
5. **The STAAD seismic-weight summary for the sentry post**, to close Conflict C9.
6. The underground model's **post-processing output** — plate M<sub>x</sub>/M<sub>y</sub>, support reactions, deflections.

---

# PART E — AUTOCAD / DXF MASTER SPECIFICATION

## E.1 Two distinct DXF sets — do not confuse them

| Set | Origin | Revision | Purpose |
|---|---|---|---|
| **Input set** (10 files) | Supplied by the user | **Rev F** | Architectural / civil geometry — the PRIMARY GEOMETRY SOURCE |
| **Output set** (8 files, S-01 to S-08) | Generated in this project | **Phase 2 Rev A** | Structural drawings with reinforcement |

## E.2 Input DXF set — Rev F — [CONFIRMED, all parsed]

| File | Content | Key extracted geometry |
|---|---|---|
| `1_Underground_Level_Plan.dxf` | **GA plan — PRIMARY** | Box 0–21600 × 0–6200; internal 600–21000 × 600–5600; partitions; internal walls; ESC circles r=700/r=950; stair shaft; blast door swings r=1200 |
| `1_Staircase_Section.dxf` | Section A-A, main stair | Landings 200 thk; waist 200 (from headroom 2533); flights; store under L1 |
| `2_Underground/Side_Section_with_Stairs.dxf` | Section X-X | **Contains the "REV F" marker and the covered-stairwell note** |
| `2_Ground_Plan_Headhouse_Berm.dxf` | Ground plan | Headhouse 13400–18200 × 200–6000; stairwell 9050–15850 × 5750–7750; berm; grating |
| `3_Headhouse_Section_Cutaway.dxf` | Section B-B at Z = 2800 | Shaft, Bay 6 and Bay 8 either side |
| `5_Entry_Headhouse_Stair_Section.dxf` | **Section C-C, Rev F** | 12R @ 166.667/300; raking roof 250; platform 250; entry door 1000×2100 |
| `5_Front_Elevation.dxf` | Front elevation | Sentry post levels +0.450 / +3.650 / +6.700 / +7.000 |
| `3_Sentry_Post_Ground_Floor_Plan.dxf` | Sentry GF | 4000 × 5000 external; 200 RC infill; D1 900 |
| `4_Sentry_Post_First_Floor_Plan.dxf` | Sentry FF | Armoured vision panels 1200 wide |
| `6_Sentry_Post_Framing_Plan.dxf` | **Sentry framing — PRIMARY for the frame** | Grid A-B 3650, 1-2 4650; C1 350×350; B1/B2 250×450; S1 150; PB 250×400; the full load schedule |

**Input set drawing conventions [CONFIRMED]:**
- Units: **millimetres**
- Origin: SW external corner of the box at (0, 0)
- Layers observed: `WALLS`, `STAIRS`, `OPENINGS`, `GROUND`, `CENTRE`, `DIM`, `TEXT`, `HATCH`
- Entities: LINE, POLYLINE + VERTEX + SEQEND, CIRCLE, ARC, TEXT
- **Sections use local coordinate systems** — e.g. in Section A-A the local x maps to the project plan Y (0 = box south external face)

## E.3 Output DXF set — S-01 to S-08 — [CONFIRMED, all generated in this project]

### E.3.1 Sheet standard — applies to every output sheet

```
SHEET SIZE        A1, 841 × 594 mm, DRAWN IN PAPER MILLIMETRES, PLOT 1:1
DXF FORMAT        AutoCAD R12 ASCII (maximum compatibility; opens in AutoCAD,
                  DraftSight, BricsCAD, LibreCAD, QCAD without translation)
BORDER            outer 0,0–841,594 ; inner 10,10–831,584
TITLE BLOCK       180 × 62 mm, bottom right, at x0 = 651, y0 = 10
VIEW SCALES       each view carries its own scale note; views are mapped from model
                  millimetres to paper millimetres by  paper = origin + model/scale
TEXT HEIGHTS      3.4 view titles | 2.4 panel headings | 2.0 scale notes
                  1.6–1.7 general | 1.55–1.62 panel body | 1.4–1.5 small annotation
VALIDATION        all eight files verified: SECTION/ENDSEC balanced, EOF present,
                  no undeclared layers, all geometry within 0..841 × 0..594
```

### E.3.2 Layer table — 22 layers, identical in every output file [CONFIRMED]

| Layer | Colour | Purpose |
|---|---|---|
| `0` | 7 | Default, unused |
| `CONC` | 7 | Concrete outlines |
| `CONC-HIDDEN` | 8 | Concrete beyond / hidden |
| `REINF-MAIN` | 1 (red) | Main reinforcement |
| `REINF-DIST` | 3 (green) | Distribution reinforcement |
| `REINF-LINK` | 6 (magenta) | Links, stirrups, torsion mats |
| `REINF-SEC` | 4 (cyan) | Secondary / trimmers / door frames |
| `DIM` | 4 | Dimensions and balloons |
| `TEXT` | 7 | General annotation |
| `TEXT-TITLE` | 7 | View titles, headings |
| `HATCH` | 8 | Section hatch |
| `GRID` | 5 | Grid lines |
| `SOIL` | 8 | Soil, rock, berm, cover layers |
| `CENTRELINE` | 6 | Centrelines, void diagonals |
| `TITLEBLOCK` | 7 | Border and title block |
| `WATERPROOF` | 30 (orange) | Membranes, waterstops, GWT |
| `STEELWORK` | 2 (yellow) | EMP straps, steel items |
| `LEVELS` | 4 | Level markers |
| `NOTES` | 7 | Panel body text |
| `TABLE` | 7 | Table rules and load diagrams |
| `SERVICES` | 2 | Sumps, tanks, ducts, drainage |
| `BLAST` | 1 (red) | Blast arrows, findings, warnings |

All layers: `70 = 0` (on, thawed, unlocked), linetype `CONTINUOUS`. Dashed lines are drawn as **explicit line segments**, not by linetype, for maximum compatibility.

### E.3.3 Output sheet register

| Sheet | File | Title | Key views |
|---|---|---|---|
| **S-01** | `01_Shear_Wall_Structural_Drawing.dxf` | Shear walls / retaining walls | V1 typical perimeter wall section 1:25 with 9-item balloon key; V2 W6/W7 400 section; V3 wall elevation 1:50; V4 haunch 1:10; V5 construction joint 1:5; V6 lateral load diagram; V7 wall layout key plan 1:200; wall schedule; BBS; 3 panels incl. **Finding F1** |
| **S-02** | `02_Mat_Foundation_Structural_Drawing.dxf` | Mat foundation | V1 mat plan 1:60; V2 section A-A mat/wall junction 1:20; V3 mat edge/drainage 1:10; V4 section B-B sump pit 1:25; bearing table; **staged flotation table**; mandatory mitigation; BBS; further checks |
| **S-03** | `03_Roof_Slab_Structural_Drawing.dxf` | Roof (pressure) slab | V1 roof plan 1:60; V2 section C-C 1:40; V3 1400 dia collar 1:30; V4 section D-D stair-void free edge 1:25; roof loading table; thickness study; BBS; **Finding F2** panel |
| **S-04** | `04_Main_Staircase_Structural_Drawing.dxf` | Main staircase, Bay 7 | V1 stair plan 1:35; V2 section A-A longitudinal 1:30; V3 flight/landing junction 1:20; V4 landing section 1:30; NBC geometry check; BBS |
| **S-05** | `05_Approach_Stairwell_Structural_Drawing.dxf` | Approach stairwell + headhouse | V1 plan 1:65; V2 section C-C 1:50; V3 section E-E transverse 1:40; V4 raft/headhouse movement joint 1:20; element schedule; BBS; **C2 + C10 headhouse panel** |
| **S-06** | `06_Underground_Plan_Services_Sump_BlastValves.dxf` | Services and drainage | V1 underground plan 1:60 with **5 blast valves marked**; V2 site drainage 1:300; V3 sump pit section 1:30; V4 septic tank + soak pit 1:40; V5 filter train schematic; blast valve schedule; drainage flows |
| **S-07** | `07_Entry_Stairwell_Flight_Reinforcement.dxf` | Entry stairwell flight | V1 longitudinal section 1:30; V2 plan on bottom steel 1:30; V3 section A-A 1:20; **V4 the opening corner 1:20**; V5 foot of flight 1:20; NBC geometry check; BBS |
| **S-08** | `08_Sentry_Post_Slab_Reinforcement.dxf` | Sentry post slab S1 | V1 bottom steel plan 1:30; V2 top + torsion plan 1:30; V3 section A-A slab/edge beam 1:10; V4 corner torsion mat 1:20; design summary; BBS; loads; **"why Table 26 not Table 27"** panel |

**Not yet drawn: sentry post beams, columns and footings.** A future sheet **S-09** would carry B1 4-T16/2-T16, B2 3-T20/2-T20, C1 8-T16 with T10 confining hoops @ 85, and F1 1500²×600 with T12 @ 150 B/W.

## E.4 The DXF generation toolchain — CRITICAL FOR REGENERATION

> **The output DXFs were not hand-drafted. They are produced by a dependency-free Python
> toolchain built inside this project — the S-01…S-08 writer below is hand-rolled and has no
> third-party dependency.**
>
> **RC3 correction, 11 September 2026 (Part H.27).** This paragraph used to end *"`ezdxf` is NOT
> available in the environment and the network is disabled."* That has not been true since
> **QA1** (Part H.11): `ezdxf` is installed and **sixteen scripts in the workspace import it** —
> the whole of `DRAWING QAQC/Scripts/`, `Drainage/Scripts/mep_render.py` and `mep_validate.py`,
> four scripts in `Structural CAD/Scripts/`, and all four in `current/cad/Scripts/`. The
> hand-rolled `dxflib.py` writer below is still the S-series toolchain's own writer, and it is
> still absent from the workspace. **Nothing about any drawing changes; this corrects a
> statement about the environment, not about the design.**

| File | Purpose |
|---|---|
| `dxflib.py` | AutoCAD R12 ASCII DXF writer. Class `Dxf` with methods: `line, circle, arc, text, rect, dline (dashed), cline, hatch45, soilhatch, tick, dimh, dimv, leader, level, secmark, table, notes, titleblock, save`. Holds the 22-layer table. |
| `proj.py` | **All reconciled project constants** — `PROJ, M1, S, L (levels), T (thicknesses), BOX, INT, PART_X, DOOR_Y, IW, SHAFT, VOID, PAD, FLTA, FLTB, BAY8, ESC1, ESC2, HH, HHI, ASW, ASWI, ASW_TOP, ASW_FLT, ASW_PLAT`, plus text blocks `MAT_NOTES, LOADS, CODES, CONFLICTS, MOD1, MOD2` and helpers `sheet, vw, vtitle, panel, balloon, keylist`. |
| `d01_wall.py` … `d08_sentryslab.py` | One generator per sheet |
| `parse.py` | DXF reader (`read`, `ents`) |
| `geo.py`, `txt.py` | Geometry / text extractors used to mine the input DXFs |
| `render.py` | Matplotlib visual-QA renderer, DXF → PNG |
| `render_pdf.py` | DXF → **true-size A1 vector PDF**, 1:1 |
| `validate.py` | Structural validation of every output DXF |
| `calc.py`, `colpm.py` | Numeric verification: flexure solver, τ<sub>c</sub> Table 19 interpolation, column P–M interaction |

**Key mapping helper — `vw(sc, ox, oy)`** returns a function `P(model_x, model_y) → (paper_x, paper_y)` where `paper = origin + model/scale`. Every view uses one.

> **A future Claude editing a drawing should edit the generator and re-run it, not edit the DXF.** The DXF is a build artefact.

---

# PART F — REINFORCEMENT MASTER REGISTER

> Notation: `T16 @ 150 EF EW` = 16 mm Fe500D deformed bars at 150 mm centres, **E**ach **F**ace, **E**ach **W**ay. `4L` = four-legged links.

## F.1 Underground box

| Element | Size | Cover | d (mm) | Main reinforcement | Links | A<sub>st</sub> prov | x<sub>u</sub>/d | Util. |
|---|---|---|---|---|---|---|---|---|
| **W1** south perimeter | 600 | 75/50/40 | 517 | **T16 @ 150 EF EW** | T12 closed @ 200 | 1340/face | 0.089 | 68 % |
| **W2** north perimeter | 600 | 75/50/40 | 517 | T16 @ 150 EF EW | T12 closed @ 200 | 1340/face | 0.089 | 68 % |
| **W3** west end | 600 | 75/50/40 | 517 | T16 @ 150 EF EW | T12 closed @ 200 | 1340/face | 0.089 | 68 % |
| **W4** east end | 600 | 75/50/40 | 517 | T16 @ 150 EF EW | T12 closed @ 200 | 1340/face | 0.089 | 68 % |
| **W5** Bay 5/6 | 200 | 40 | 154 | T12 @ 150 EF EW | — | 754/face | — | nominal |
| **W6** Bay 6/7 (M1) | **400** | 50/40 | 342 | **T20 @ 150 EF EW** | **T12 4L @ 200** | 2094/face | 0.211 | 69 % |
| **W7** Bay 7/8 (M1) | **400** | 50/40 | 342 | T20 @ 150 EF EW | T12 4L @ 200 | 2094/face | 0.211 | 69 % |
| **W8** partitions ×4 | 110 | 25 | — | A252 mesh both faces | — | 252 | — | non-structural |
| **MAT** | 600 | 75/50 | 517 | **T16 @ 150 EF EW** | **T12 @ 250 × 250 grid** | 1340/face | 0.089 | **84 %** |
| **ROOF** midspan | 900 | 75 | 812.5 | **T25 @ 150 EF EW** | T12 4L @ 250 end 1500 / 2L @ 300 mid | 3272/face | 0.139 | 51 % |
| **ROOF** cantilever pad | 900 | 75 | 812.5 | T25 @ 150 top continuous | **T12 4L @ 250 throughout** | 3272 | 0.139 | 56 % |
| Sump pit walls/base | 300/400 | 50 | 244 | T16 @ 150 EF EW | — | 1340 | — | nominal |

**Additional bars — underground box**

| Location | Requirement |
|---|---|
| Wall starters | T16 @ 150 EF, **900 mm horizontal leg into the mat**, lap 800 (50φ) above a 150 kicker |
| Haunches, all wall–roof and wall–mat junctions | **500 × 500**, diagonal **T20 @ 150** |
| Mat edge, all free edges | **T16 @ 150 U-bars** closing both curtains |
| Sump pit opening | **4-T20 trimmers each face, each side**, L<sub>d</sub> 800 beyond |
| Blast door jambs (W6, W7) | **4-T20 each jamb, each face**, L<sub>d</sub> 800 beyond |
| Blast door header | 400 × 1100: **4-T20 top + 4-T20 bottom, T12 4L @ 150** |
| ESC 1 / ESC 2 collars | Collar 250 RC; **5-T25 each side, each face, each direction**, L<sub>d</sub> 1000 beyond; **T16 @ 150 hoops ×3 layers + T16 @ 150 radials**; slab thickened 900→1200 over a 600 annulus |
| Stair void free edge | Thickened 900→1200 over 600; **6-T25 top + 6-T25 bottom, T12 closed @ 150** |
| Stair void side bands | **6-T25 each face, top and bottom, in a 900 band over W6 and W7** |
| Stair void re-entrant corners (×2) | **4-T25 each face at 45°, 2000 long each way**, anchored L<sub>d</sub> beyond |
| Band beneath headhouse wall HW3 | **4-T25 extra top and bottom in a 1200 band**, lapped 1250 |
| Construction joints (~6 m) | Reinforcement **fully continuous**; two waterstops + welded Cu/galv EMP strap |

## F.2 Stairs

| Element | Size | Cover | d | Main | Distribution | Top steel |
|---|---|---|---|---|---|---|
| **Main stair flight** waist | 200 | 30 | 164 | **T12 @ 150** (754) | T10 @ 200 (393) | T12 @ 150 for 800 into the flight, L<sub>d</sub> 480 |
| **Main stair landings** L1/L2/arrival | 200 | 30 | 164 | **T12 @ 125 bottom** (905) | T10 @ 200 | T12 @ 125 for 900 from each support |
| **Entry stairwell flight** waist | 250 | 30 | 214 | **T16 @ 200** (1005) | T10 @ 200 | T16 @ 200 for 1200 into the flight, L<sub>d</sub> 640 |
| Entry stairwell top landing | 250 | 30 | 214 | T12 @ 200 EF EW (565) | — | — |
| Entry stairwell platform | 250 | 30 | 214 | T12 @ 200 EF EW | — | on fill |
| Entry stairwell side walls | 250 | 50 | 194 | T12 @ 200 EF EW | — | min steel governs |
| Entry stairwell raking roof | 250 | 30 | 204 | T12 @ 200 EF EW | — | min steel governs |
| Entry stairwell headwall | 250 | 30 | 214 | T12 @ 200 EF EW | — | — |
| Entry door lintel (1000 clear) | 250 × 350 | 30 | 306 | 3-T12 top + 3-T12 bottom | T8 @ 150 | — |
| Stepped raft | 300 | 50 | 244 | T12 @ 200 EF EW | — | on compacted fill |
| **Opening-corner U-bar** (top of entry flight) | — | — | — | **T16 @ 200 U-bar**, bars CROSSED and anchored L<sub>d</sub> 640 into the opposite face | | **SP 34 Cl. 5.5** |

## F.3 Headhouse

| Element | Size | Cover | d | Main | Links |
|---|---|---|---|---|---|
| **Roof** | 500 | 75 | 415 | **T20 @ 150 EF EW** (2094) | **T12 4L @ 175 in the end 1200 each side; @ 250 elsewhere** |
| **Walls HW1–HW4** | 400 | 50/40 | 342 | **T16 @ 150 EF EW** (1340) | **T12 4L @ 250 throughout** |
| Door jambs, HW2 | — | — | — | **2-T20 each jamb, each face**, L<sub>d</sub> 800 beyond | — |
| Door head edge band | 400 × 800 | 40 | 742 | **4-T20 top + 4-T20 bottom** | T12 4L @ 150, over the opening + 600 each side |
| Wall–roof haunch | 300 × 300 | — | — | diagonal T16 @ 150 | — |

## F.4 Sentry post

| Element | Size | Cover | d | Reinforcement |
|---|---|---|---|---|
| **Slab S1** bottom | 150 | 30 | 116/108 | **T8 @ 150 c/c BOTH WAYS** (335 mm²/m) |
| Slab S1 top, discontinuous edges | 150 | 30 | 116 | **T8 @ 300, 400 mm (0.1 L) into the span, all four edges** — Cl. D-1.6 |
| Slab S1 corner torsion | — | — | — | **T8 @ 200, FOUR LAYERS, 700 × 700 at all four corners** — Cl. D-1.8 |
| **Beam B1** (3650) | 250 × 450 | 30 | 404 | **4-T16 top at supports; 2-T16 bottom continuous** |
| **Beam B2** (4650) | 250 × 450 | 30 | 404 | **3-T20 top at supports; 2-T20 bottom continuous** |
| Beam hoops, both | — | — | — | **T8 2-leg @ 100 over 2d = 810 from each face; @ 150 elsewhere**; first hoop ≤ 50 from the face |
| **Column C1** | 350 × 350 | 40 | d′ 56 | **8-T16** (1608 mm², p = 1.31 %) |
| Column confining hoops | — | — | — | **T10 hoops + 1 cross-tie each way @ 85 c/c over 500 mm from every joint face, top and bottom, AND through the joint** |
| Column general ties | — | — | — | T8 @ 150 c/c elsewhere |
| Plinth beam PB | 250 × 400 | 30 | 354 | 3-T12 top + 3-T12 bottom |
| **Footing F1** | 1500 × 1500 × 600 | 50 | 542 | **T12 @ 150 both ways bottom** (754 mm²/m) |

> **3-T20 was chosen for B2 over 5-T16 because five T16 bars require 256 mm in a 250 mm wide beam.** That is exactly the check that becomes a site RFI if skipped.

---

# PART G — CODES, STANDARDS AND REFERENCES

| Code / reference | Used for | Specific clauses relied upon |
|---|---|---|
| **IS 456:2000** | All RC design | Cl. 6.2.3.1 (E<sub>c</sub>); Cl. 13.4 (construction joints); Cl. 22.2(a) (effective span); Cl. 23.2.1 + Fig. 4 (deflection); Cl. 24.4, 24.5 + Fig. 7 (two-way slabs, loads to beams); Cl. 25.1.2 (short column); Cl. 25.4 (min eccentricity); Cl. 26.2.1, 26.2.1.1, 26.2.5.1 (L<sub>d</sub>, laps); Cl. 26.3.3 (bar spacing); Cl. 26.4.2, 26.4.2.1, 26.4.2.2 + Table 16 (cover); Cl. 26.5.1.1, 26.5.1.2, 26.5.1.5, 26.5.1.6 (beam steel, links); Cl. 26.5.2.1, 26.5.2.2 (slab steel); Cl. 26.5.3.1, 26.5.3.2 (column steel, ties); Cl. 31.6, 31.6.1, 31.6.3.1 (punching); Cl. 32.2, 32.5(a)(b)(c) (walls); Cl. 33.1(b), 33.2 (stairs); Cl. 34.2.4.1 (footing shear); Cl. 36.4.2 (γ<sub>m</sub>); Cl. 38.1, 38.1(c), 38.1(f) (limit state, stress block, x<sub>u,max</sub>); Cl. 39.1, 39.3, 39.6 (columns, biaxial); Cl. 40.1, 40.2.1.1, 40.2.3, 40.4(a) (shear); Table 3, 5, 16, 18, 19, 20, 26, 27, 28; Annex D (D-1.1 to D-1.8, D-2); Annex G-1.1(b), G-1.1(c) |
| **IS 875 (Part 1):1987** | Dead loads, unit weights | Table 1 |
| **IS 875 (Part 2):1987** | Imposed loads | Plant/storage 5.0 kPa; office/OP 3.0; accessible roof 1.5 |
| **IS 875 (Part 3):2015** | Wind, sentry post only | Cl. 6.3, 6.3.4, 7.2, 7.2.1, 7.3.3.13, 7.4; Tables 1, 2, 4, 26; Annex A (V<sub>b</sub> = 39 m/s) |
| **IS 875 (Part 5):1987** | Load combinations | with IS 456 Table 18 |
| **IS 1893 (Part 1):2016** | Seismic | Cl. 6.3.1.2, 6.3.2.2 (combinations, directional); Cl. 6.4.2 + Fig. 2 (A<sub>h</sub>, S<sub>a</sub>/g); Cl. 7.2.3 (I), Cl. 7.2.6 (R), Cl. 7.3.1, 7.3.2 (seismic weight); Cl. 7.6.1, 7.6.2, 7.6.2(c), 7.6.3 (period, base shear, distribution); Cl. 7.11.1 (drift); Table 3 (Z) |
| **IS 13920:2016** | Ductile detailing, sentry post | Cl. 6.1.1, 6.1.2, 6.1.3 (beam geometry); Cl. 6.2.1(b), 6.2.2, 6.2.3, 6.2.4 (beam steel); Cl. 6.3.3, **6.3.4**, 6.3.5.1, 6.3.5.2 (capacity-design shear, hoops); Cl. 7.1, 7.2.1 (SCWB), 7.3, 7.4 (columns); Cl. 8.1, 8.2 (special confining reinforcement); Cl. 10.4 (boundary elements — checked, not triggered) |
| **IS 3370 (Parts 1, 2):2021** | Crack width, surface-zone steel | 0.2 mm limit; 0.35 % surface-zone steel over a 250 mm zone |
| **IS 1786:2008** | Fe500D reinforcement | D grade — guaranteed minimum elongation |
| **IS 1904:1986** | Presumptive bearing capacity | Table 1 (hard rock, 3240 kPa) |
| **IS 2950 (Part 1):1981** | Raft foundations | General provisions |
| **IS 12070** | Rock foundations | Cl. 6 (settlement on sound rock); **Table 2 (broken bedrock, 10 kg/cm² — the SEMT report's own basis, SG1)** |
| **IS 1498:1970** | *(SG1)* Soil classification | CH, GM, GP, SC; free swell index bands — the SEMT report's classification basis |
| **IS 2720** Pts IV, VIII, X, XIII, XL | *(SG1)* Soil testing | Classification (Pt IV), compaction / OMC-MDD (Pt VIII), UCS (Pt X), direct shear (Pt XIII), free swell (Pt XL) — **the SEMT report's own test methods, cited as it cites them** |
| **IS 2720 (Part 28)** | *(SG1)* In-situ density | Backfill compaction testing, WBS `A7015` |
| **IS 1121 (Part I)** | *(SG1)* Rock strength | Compressive strength of rock cores — the SEMT report's Appendix C basis. *(The report prints the year as "1874"; that is a typographical error and is transcribed as printed, not corrected.)* |
| **IS 2470 (Part 1):1985** | Septic tank | Cl. 6.2 (24 h detention), Cl. 6.3 (30 L/person/yr sludge), Cl. 6.5 (L:B 2–4), Cl. 6.6 (min width 750, min depth 1.0 m), Cl. 6.9 (vent); **Table 1 (≤10 users: 1.5 × 0.75 × 1.0)** |
| **IS 2470 (Part 2):1985** | Soak pit / dispersion | Cl. 4 (**percolation test — mandatory**), Cl. 5 (dispersion trench) |
| **IS 4991:1968** | **Blast loading rules and dynamic material strengths ONLY** | **Cl. 1.1 (EXPLICITLY EXCLUDES NUCLEAR — quoted in every deliverable)**; Cl. 6.2.1 (reflected pressure, recessing); Cl. 7.2 + Table 3 (buried roof/walls, K<sub>a</sub>); Cl. 7.4 (drag on bermed faces); Cl. 10.3.1 (dynamic f<sub>ck</sub>, f<sub>y</sub>); **Cl. 10.3.1.1 (NO dynamic increase on shear; +25 % bond)**; Cl. 10.3.3 (DLF = μ/(μ−0.5)); Cl. 11.1 (no wind/EQ with blast); Cl. 11.2 (no live load on the roof at blast); Fig. 6 (SDOF — **Phase 3**) |
| **SP 16:1980** | Design aids | Column interaction charts (cross-checked; the P–M values in B.8.6 were computed from first principles, not read off) |
| **SP 34:1987** | Detailing | Shape codes; **Cl. 5.5 (opening-corner detailing)** |
| **NBC 2016 Part 4** | Fire and life safety | Stair geometry, guarding 1100, means of escape |
| **BS 8666** | Bar shape codes | Used alongside SP 34 in all BBS |
| **UFC 3-340-02** | US criteria, cited AS US criteria | §4-27 (opening trimmers); §4-30 (direct shear) |
| **UFC 3-350-04AN** | US criteria | Referenced in the Phase 1 report |
| **MIL-STD-188-125-1** | EMP | §5.4 (access), §5.5 (waveguide below cutoff), §5.7.2.1 (power PCI), §5.7.4.1 (fibre), §5.7.6 (RF); 80 dB, 10 kHz–1 GHz |
| **IEEE Std 299** | EMP verification | Shielding effectiveness survey |
| **IEEE 142 / IS 3043** | Earthing | ≤ 5 Ω target |
| **FEMA 453** | Shelter ventilation | 0.25 cfm/ft²; carbon adsorber performance |
| **EN 1822** | HEPA classification | H14, ≥ 99.995 % at MPPS |
| **Glasstone & Dolan** | Weapons effects | Unclassified, public — blast and radiation data only |
| **Biggs, *Structural Dynamics*** | SDOF method | Referenced for the **Phase 3** support-rotation check |

> **No clause number in this register was invented.** Where a clause could not be confirmed from the material available it is not listed. If a future Claude needs a clause not in this table, it must be verified against the code, not assumed.

---

# PART H — REVISION HISTORY

## H.1 Architectural / Phase 1 history (pre-dating this work)

| Rev | Change | Previous | New | Reason | Status |
|---|---|---|---|---|---|
| A–B | Initial layout development | — | — | — | **SUPERSEDED** |
| **C** | **Box lengthened** to give ESC 2 the 750 mm clearance | shorter box | 21 600 external | Escape-shaft opening edge was < 750 mm from a wall face | **SUPERSEDED by M1** |
| — | Cover reduced | 4 000 mm | **2 000 mm** | Prompt radiation needs 2 m; blast needs none; fallout needs 1 m. Saved 2 m excavation, 2 m shaft, one stair flight, 2 m headroom | **CURRENT** |
| **D** | Design report issued | — | — | Basis of design, loads, materials, geotech, calculations | **CURRENT for loads/materials; SUPERSEDED for the entrance and the headhouse roof** |
| D reg. item 11 | Headhouse resized | 3 000 × 4 000 | **4 000 × 5 000, no roof cover, +0.900** | — | **CURRENT** — but O.12 was never recomputed → **Conflict C2** |
| **E–F** | **Approach replaced** | dog-leg **open ramp** | **covered entry stairwell**, 12R @ 166.667/300, entered at grade | Open cut had no gravity outfall; a 2 m pit collects dense CBRN agents; lidding at grade gave zero headroom | **CURRENT — Conflict C1** |
| **F** | Drawing set issued | — | — | The ten uploaded DXFs | **CURRENT for all geometry** |

## H.2 Phase 2 structural history (this project)

| # | Change | Previous | New | Reason | Affected files | Status |
|---|---|---|---|---|---|---|
| **M1** | **Walls W6/W7 thickened; box lengthened** | 200 thk; box 21 600; shaft 15000–17800; Bay 8 18000–21000; ESC 2 at 19500 | **400 thk; box 22 000; shaft 15200–18000; Bay 8 18400–21400; ESC 2 at 19900** | **Finding F1** — 200 mm cannot carry 383 kPa (M<sub>u,lim</sub> 138 < 245 demand). 400 cannot come from Bay 8 (750 clearance) or the shaft (2800 = 2×1200+200) | ALL sheets; headhouse and stairwell shift +200 | **CURRENT — APPROVED AND IMPLEMENTED 3 Sep 2026, see H.4** |
| F2 | Stair-void cantilever pad designed | not designed | T25 @ 150 top (56 %) + **T12 4L @ 250 throughout the pad** + edge thickening + corner trimmers | M(root) 758.6 > midspan 700.2 | S-03 | **CURRENT** |
| C6 | Mat one-way shear checked | flexure only | **T12 @ 250 × 250 link grid** | IS 4991 Cl. 10.3.1.1 forbids dynamic increase on shear | S-02 | **CURRENT** |
| C2 | Headhouse roof recomputed | 3.0 m span, 1.0 m cover | **4.0 m span, no cover, w = 396.5 kPa** | Report O.12 stale vs Rev F | S-05 | **CURRENT** |
| C2 | Headhouse roof shear links added | none | **T12 4L @ 175 end 1200 / @ 250** | τ<sub>v</sub> 1.514 > τ<sub>c</sub> 0.502 | S-05 | **CURRENT** |
| **C10** | **Headhouse wall loading raised** | **113 kPa drag** (Cl. 7.4) | **383 kPa full envelope** | Berm transmits pressure; K<sub>a</sub> unverifiable. Cost = one link cage | S-05 | **CURRENT** |
| C10 | Headhouse wall links added | none | **T12 4L @ 250 all four walls** | consequence of the above | S-05 | **CURRENT** |
| **C9** | **Sentry post base shear** | hand calc **59.3 kN** (W = 592.7) | **STAAD 73.18 kN** — used for all design | Model 23 % heavier; reactions confirm F<sub>x</sub> = 18.295/column | Part B.8 | **CURRENT — gap to be closed in Phase 3** |
| C9 | Beam B1 top steel | 3-T16 (at 59.3 kN) | **4-T16** | consequence of C9 | Part B.8.4 | **CURRENT** |
| C9 | Beam B2 top/bottom | 4-T16 / 2-T16 | **3-T20 / 2-T20** | consequence of C9; 5-T16 will not fit a 250 wide beam | Part B.8.5 | **CURRENT** |
| C9 | Column biaxial ratio | 0.718 | **0.819** | consequence of C9 | Part B.8.6 | **CURRENT** |
| **ERR-1** | **Yield-line coefficient corrected** | **324.4 kNm/m** (used the simply-supported coefficient 24) | **162.2 kNm/m** (fixed-4-edges coefficient 48) | **My own arithmetic error.** Validation: as b→∞, 48/3 = 16 = w·L²/16 ✔ | Part B.7.1, S-05 | **CURRENT. No reinforcement change — the one-way value 396.5 was adopted, so nothing depended on it** |
| Sump relocated | outside the wall, below mat level | **inside, Bay 5, 1500³, invert (−)7.600** | Unprotected envelope breach below the water table, impossible to inspect | S-02, S-06 | **CURRENT** |
| Wall links | T12 @ 250 | **T12 @ 200** | Recalculated V<sub>us</sub> | S-01 | **CURRENT** |
| **SP-B1** | **Sentry post walls = BRICK MASONRY** — instructed design change, 7 Sep 2026 | RC 200 ballistic infill (Rev F) | **190 one-brick modular brickwork to IS 1077 in CM 1:6, inside the confirmed 200 structural zone** | Instructed by the user; the only design change in WM1. Preserves the confirmed 4000 × 5000 envelope. Creates a lintel requirement and a tie requirement that did not exist, reduces the infill line load 13.000 → ≈ 9.9 kN/m (conservative for V<sub>b</sub>, referred to the structural discipline, **not verified here**), and removes the ballistic function the Rev F panels were named for | Part H.10, `WORKS MANAGEMENT/` | **CURRENT** |
| **SP-B2** | **Sentry post lintels and wall ties** — completes SP-B1, 10 Sep 2026 | no lintel design, no tie detail existed (WM-V5, WM-V11) | **Lintel L1 190 × 150, M30/Fe500, 2-T10 bottom, 2-T8 top, T6 links @ 150, bearing 200 — one type over all eleven openings; 6 mm MS ties @ every 5th course (≈450) up both column faces, 200 into the bed joint, 10 mm dowel; top course tight to the beam soffit** | The walls as recorded could not be built without them. L1 designed to the 60° arching bound so it does not depend on the unstated opening heights (WM-V3). **No frame member, footing, slab, storey height or envelope changed; 13.000 kN/m infill retained; R = 3.0 unchanged** | Part H.12, A.4.8, A-105 | **CURRENT** |
| **BS1** | **RC burster slab laid to falls** — instructed design change, 10 Sep 2026 | burster slab and cover laid **flat** | **1:50 crossfall, crowned on the box centreline (Y 3100), falling 62 mm each way to the box edge — parallel to the crowned grade** | The granular filter bears directly on the slab; D-102 note 3 and calculation D.7 already claimed infiltration is *dispersed at the berm toe*, which a flat slab cannot do. Fall taken entirely in the compacted fill (750 crown → 688 edge). **Cover load unchanged at the crown and lighter toward the edges; COMB 103 = 448.15 kPa and all three `.std` untouched. C17 NOT resolved** | Part H.12, A.7.3, R-302, D-102, D-301 | **CURRENT** |

## H.3 Conflict register — full

| # | Conflict | Resolution | Status |
|---|---|---|---|
| **C1** | Drawings **Rev F**, report **Rev D**. Report describes a dog-leg open ramp; Rev F is a covered entry stairwell | **DXF governs.** Part 6 of the calculation report designs the Rev F arrangement | RESOLVED |
| **C2** | Report O.12 designs the headhouse roof for 3.0 m span + 1.0 m cover; Rev F is 4.0 m + no cover | **Recomputed.** T20 @ 150 survives at 90 %; **shear links new and mandatory** | RESOLVED |
| **C3** | Report G.2 / M-9 call the stair-shaft walls 600 thk; the Rev F plan shows 200 | **DXF governs** → triggers Finding F1 → Modification M1 | RESOLVED |
| **C4** | Blast door leaf: plan opening 1200, Section A-A shows 900 | **Adopted 1200 × 2100** — agrees with report F.5 (1564 kN leaf force) | RESOLVED |
| **C5** | Plan dim "7300 covered stairwell external" vs 6800 in the plotted geometry and Section C-C | **Adopted 6800** | RESOLVED |
| **C6** | Report O.9 checks the mat in flexure only | One-way shear checked → link grid required | RESOLVED |
| **C7** | Report O.14 uses W = 505 kN [A] for the sentry post | Computed as 592.7 kN from the drawn sizes → 59.3 kN. **Superseded by C9** | SUPERSEDED |
| **C8** | Report adopts sentry post height 6850 mm; the front elevation shows roof +6.700, parapet +7.000 | **Drawn levels adopted**; h = 6.250 m from the base at +0.450 | RESOLVED |
| **C9** | STAAD states V<sub>b</sub> = 73.18 kN; hand check gives 59.3 kN | **Design uses the higher STAAD value.** Print the STAAD seismic-weight summary in Phase 3 | **OPEN — documentation gap, not a safety gap** |
| **C10** | Report designs headhouse walls for 113 kPa drag only | **Raised to the full 383 kPa envelope.** Cost: T12 4L @ 250 in all four walls | RESOLVED |
| — | Report J.7 places the service-entry plate "between Bay 5 and Bay 8" — those bays are not adjacent | **Superseded.** Single plate placed in the north perimeter wall (W2) at Bay 5, X ≈ 11 800 | RESOLVED |
| **C17** | **Engineered cover build-up.** A.7.3 states a total of **40.65 kPa**; the same table's own column sums to **39.15 kPa**. Every individual line is arithmetically correct — the total row is not the sum of the column | **RULED — RC1, 10 Sep 2026 (H.14). 40.65 IS HELD as the design value, and the A.7.3 table has been made self-consistent**: it now shows the layer sum **39.15** plus a **declared allowance of +1.50**. 40.65 is the value in A.7.4, in Part L and in `DL2` in every underground `.std`, and it is the larger. Roof COMB 103 stays **448.15 kPa** and no bar, spacing or link changes | **CLOSED** |
| **C18** | **Sump-pit base thickness.** F.1 gives "walls/base **300/400**", and the A.4.3 levels ((−)7.600 invert to (−)8.000 base) independently give **400**; the text on sheet S-06 says **300** for both | **RULED AT 400 — RC1, 10 Sep 2026 (H.14).** (−)8.000 − (−)7.600 = **0.400** is arithmetic, and F.1 says 400 independently. S-06's "300" is a transcription error and is superseded | **CLOSED** |
| **C19** | **Soak pit capacity.** Sheet S-06 prints "22.0 m² OK" against its own stated requirement of "area required 22.5 m²". π × 2.0 × 3.5 = **21.99 m²**, which is **not** ≥ 22.50 m² — the pit as drawn was **2.3 % short** | **RULED — RC1, 10 Sep 2026 (H.14). SK-01 is WIDENED: diameter 2.0 → 2.200 m, effective depth UNCHANGED at 3.500 m.** π × 2.200 × 3.500 = **24.19 m²** against 22.50 required, **+7.5 %**. Widening was chosen over deepening because deepening drives the pit further below the design GWT at (−)2.000, where it cannot soak at all. The percolation test (A7) still governs the final size | **CLOSED** |
| **C20** | **Superseded catchment on S-06.** The design-flow table gives **0.10 L/s** for "stairwell / approach surface water". That is the **Rev E open-cut** figure — 7.2 m² of open pit at 50 mm/h, reproduced exactly by DR1. At Rev F the approach is covered, the door is at grade and drawing 5 note 5 states the catchment with the door shut is **zero**; the governing case is note 9's door-open driving-rain rate, ≈ 12 × smaller | **RULED — RC1, 10 Sep 2026 (H.14). REV F GOVERNS and 0.10 L/s is RETAINED as a declared conservatism, not as a live figure.** Precedent C1: where a drawing and an older document disagree, the drawing governs — so the catchment is Rev F's, and note 9's door-open rate is the design case. The 0.10 L/s stays in the S-06 table because removing it changes no pump, no pipe and no pit (the 2 L/s stairwell pump is 20 × it) and because deleting a superseded number hides the history. **Both figures are shown on D-103 and both are labelled** | **CLOSED** |
| **C21** | **Filter train duty — the master and S-06 disagree.** A.3 describes bay 5 as "2 × **250** m³/h filters". Sheet S-06 states **300 m³/h** in nine separate places: the design flow, the train label "EACH 300 m³/h (TRUE N+1)", both train annotations, the blast-valve schedule, the DN100 velocity sizing, the airlock purge and the closed-mode arithmetic. **At 250 m³/h one train is below the 264 m³/h FEMA 453 rate S-06 itself computes**, so the "true N+1, not 2 × 150" claim fails on the sheet's own criterion | **RULED AT 300 m³/h — RC1, 10 Sep 2026 (H.14). A.3 HAS BEEN CORRECTED from "2 × 250" to "2 × 300".** Four independent lines all point one way and none points the other: S-06 states 300 in **nine** places; every other S-06 figure reproduces **only** at 300; **250 fails S-06's own 264 m³/h FEMA 453 criterion**, so it is not merely the smaller option but a demonstrably inadequate one; and the project owner's own cost estimate independently prices **2 × 300 m³/h** trains. A.3's 250 was the single outlier | **CLOSED** |

## H.4 Implementation of Modification M1 — 3 September 2026

> **M1 was approved by the user on 3 September 2026 and has been implemented in the project files.** Parts A, B, F and L already carried the M1 values; **not one design value in them was changed.** This section records only that the CAD and STAAD files were brought into agreement with them.

| # | Change implemented | Files | Basis | Status |
|---|---|---|---|---|
| **M1-I1** | M1 geometry propagated into the six affected architectural DXFs — W6 14800–15200 (400), W7 18000–18400 (400), box 22 000, shaft 15200–18000, void 15200–18000, ESC 2 at X 19 900, headhouse 13600–18400, covered stairwell 9250–16050, and the dependent dimension text | `1_Underground_Level_Plan`, `2_Side_Section_with_Stairs`, `2_Ground_Plan_Headhouse_Berm`, `3_Headhouse_Section_Cutaway`, `5_Entry_Headhouse_Stair_Section`, `5_Front_Elevation` | A.3, A.4.2, A.4.4–A.4.7 | **IMPLEMENTED** |
| **M1-I2** | M1 geometry propagated into the underground plate model — X grid rebuilt on the post-M1 mid-surface (31 lines, W6 c/l 15.000, W7 c/l 18.200, east wall c/l 21.700, ESC 2 opening 19.2–20.6); internal wall thickness split **W5 200 / W6+W7 400** | `Underground_Structure_WITH_LOADS_worked_example (4).STD` | A.3, B.2, F.1 | **IMPLEMENTED** |
| **M1-I3** | **`LOAD 11 BL3 BLAST IN THE STAIR SHAFT ON W6 AND W7 383 KN/M2`** added, acting out of the shaft on both faces, and included in **COMB 103** — the demand Finding F1 identified and that M1 exists to carry. The model previously applied blast to the external walls only | same | A.7.1, B.2 (Finding F1) | **IMPLEMENTED** |
| **C11** | Entry stairwell concrete grade — model declared **M30**; A.5 places stairs in **M35** and B.6 / F.2 detail them at L<sub>d</sub> = 40 φ (T16 = 640 mm), the M35 value. In M30 the same bar needs 46 φ = 736 and every stairwell lap would be 13 % short | `Entry_Stairwell.std` | A.5, B.6, F.2 | **RESOLVED — M35, E<sub>c</sub> 29 580 N/mm² adopted** |
| **C12** | Entry stairwell roof imposed load — model applied **1.5 kPa**; A.7.6 / B.6 specify **20 kPa**, taken deliberately for a stray vehicle on the berm | `Entry_Stairwell.std` | A.7.6, B.6 | **RESOLVED — 20 kPa adopted** |
| **C13** | Entry stairwell roof waterproofing / screed **2.0 kPa** was absent from the model | `Entry_Stairwell.std` | A.7.6, B.6 | **RESOLVED — added; roof now 6.25 + 2.0 + 5.4 + 20.0 = 33.65 kPa, matching A.7.6 exactly** |
| **C14** | Entry stairwell fill — model used **γ = 18 kN/m³** to a +0.950 berm; A.6 gives **γ = 20** and A.4.7 a **+0.900** crest | `Entry_Stairwell.std` | A.6, A.4.7, B.6 | **RESOLVED — gradient 10.0 kPa/m gives 29.0 kPa at the platform and 34.0 kPa with surcharge, reproducing B.6** |
| **C15** | Underground model — mat corner joints 1, 10, 301, 310 carried `FIXED BUT FY MX MY MZ` with **no `KFY`**, leaving them with no vertical restraint, contrary to D.3.3. The file's own comment stated the value was required | `Underground_Structure_WITH_LOADS_worked_example (4).STD` | D.3.3 | **RESOLVED — KFY restated per corner from the post-M1 tributary areas (6891 / 8269 / 7219 / 8663 kN/m)** |
| **C16** | Roof / platform junction — A.4.7 read *"over the platform it becomes the 500 headhouse roof"*, while B.6 designs, A.7.6 loads and F.2 register a **250** stairwell roof, and the headhouse footprint (Y 200–6000) does not overlap the platform (Y 6000–7500) | `Entry_Stairwell.std` | A.4.7 **vs** B.6 / A.7.6 / F.2 | **RULED AT 250 — RC1, 10 Sep 2026 (H.14). The A.4.7 clause has been CORRECTED; it was the only place in the project that said 500. CLOSED** |

> **C16 — RULED AT 250, 10 September 2026 (RC1, Part H.14).** The model always kept a 250
> roof because Part B designs one, A.7.6 loads one and F.2 registers one, and because the
> headhouse roof of B.7.1 is a 396.5 kPa blast element on a footprint that **does not extend
> over the platform**: the headhouse occupies Y 200–6000 and the platform is at Y 6000–7500,
> so they do not touch. **A.4.7's "500 over the platform" was therefore not a competing
> design, it was a clerical error** — one clause against four parts of the project and
> against the geometry itself. **The clause is now corrected to read 250.** Nothing else
> moves: the model, the loads, the register and the drawings already said 250.
> **C16 IS CLOSED.**

**Verified after implementation:** every M1 control value in A.3 / A.4 / L was checked against the modified files; the main staircase (24R @ 170.8333 / 280, 3 flights × 8, rise 4100, landings, 1200 flight widths, 200 well) was confirmed **unchanged**; and `1_Staircase_Section.dxf` plus the three sentry post drawings were left **byte-identical**. `Sentry_Post_Framed_Seismic.std` was checked against A.4.8, A.5, A.7.7, A.7.8 and D.2.3 and **required no change**.

**Not implemented, and why:**

| Item | Reason |
|---|---|
| Output sheets **S-01 to S-08** | The Part E.4 Python toolchain (`proj.py`, `dxflib.py`, `d01_wall.py`…`d08_sentryslab.py`, `validate.py`, `render.py`) is **not in the workspace**, and M.12 forbids editing a generated DXF directly. **S-06 is the only output sheet present and already carries M1, so it was not touched.** The other seven cannot be regenerated until the toolchain is supplied. |
| Second k<sub>s</sub> bound | A.6 and K.2 **A4** require the mat model at **both** 100 000 and 500 000 kN/m³. Only the lower bound exists. k<sub>s</sub> stays **[ASSUMED]** and the second run is outstanding. |
| STAAD analysis run | STAAD.Pro is not available in this environment. The models were verified **structurally and numerically against this document**, not executed. |
| Sentry post combination count | A.7.9 records **15** combinations from a screen capture; the file has **16** (101–113, 201, 202 and **203**, a second drift check in Z). The file was **not** altered — deleting 203 would remove a directional check required by IS 1893 Cl. 6.3.2.2. A.7.9's count is the record that is short. |

## H.5 Mesh sensitivity / convergence study — 3 September 2026

> **MS1 is a verification/QA study, not a design change.** It does not alter M1, any Part A/B
> value, any load, or any support condition. It adds three auxiliary underground-box `.STD`
> models at coarser and finer mesh density than the reconciled M1 model, to demonstrate
> mesh-independence of the results for the capstone presentation. The reconciled model itself,
> `Underground_Structure_WITH_LOADS_worked_example (4).STD`, was verified **byte-identical /
> unchanged** after the study (see below).

| # | Change implemented | Files | Basis | Status |
|---|---|---|---|---|
| **MS1** | Three mesh-density variants of the reconciled M1 underground box model built: **COARSE** (~1.9× the reference element size), **MEDIUM** (unmodified copy of the reference mesh), **FINE** (exact h/2 refinement of the reference mesh). Geometry (incl. all M1 values), thicknesses, materials, supports/soil springs, loads, load cases and combinations are identical in all three; only plate mesh density differs. Roof/escape-shaft/stair-shaft opening boundaries, the 22 000×6 200 footprint and the W5/W6/W7 centrelines are pixel-identical across all three (verified: net roof area 104.048 m² and hole area 15.792 m² match exactly in all three). Corner mat-spring `KFY` values and the EP1 earth+water row pressures were re-derived per mesh from the same physical formulas the reference model itself encodes (KFY = k_s×A_trib; EP1 p = 15.4071×depth − 10.8198 kN/m², depth = 6.700−Y, fitted from the reference model's own 6 data points, residual ≤ 0.01 kN/m²) — not re-guessed. | `Underground_Shelter_Mesh_Coarse.std`, `Underground_Shelter_Mesh_Medium.std`, `Underground_Shelter_Mesh_Fine.std` (all in `current/staad/`); methodology in `current/staad/MESH_SENSITIVITY_STUDY.md` | A.3, A.4, B.2–B.4, D.3.3, H.4 (M1-I2, C15) | **MODELS BUILT AND VALIDATED. STAAD.Pro is not available in this environment — no analysis has been run and no result (moment, displacement, shear, reaction) exists yet for any of the three models. Results and the convergence conclusion are OUTSTANDING pending a STAAD.Pro run.** |

**Verified after build:** all three files terminate with `FINISH`; every element/joint reference
in `SUPPORTS`, `ELEMENT LOAD`, `DESIGN ELEMENT` and `PRINT SUPPORT REACTION LIST` resolves;
every plate has a `THICKNESS`; the reference `.STD` is confirmed byte-identical to its
pre-study copy (`git diff` clean) — **true of MS1; superseded by MS2, Part H.26, which
corrected all four box models as INPUT FILES while leaving every analysis value unchanged**. The main staircase is not represented in this plate model
(it is a separate `.std` and DXF set, per the Frozen section of `CLAUDE.md`) and was not
touched. `Entry_Stairwell.std` and `Sentry_Post_Framed_Seismic.std` were not touched.

**Not implemented, and why:**

| Item | Reason |
|---|---|
| Actual STAAD.Pro analysis results for COARSE/MEDIUM/FINE | STAAD.Pro is not available in this environment (same constraint as H.4). The three models are built and file/numerically validated but **not executed**. Running them and completing the convergence table is outstanding. |

## H.6 Revit 2026 BIM — Phase 1 (audit, project setup, structural model) — 3 September 2026

> **BIM-P1 is a new-format deliverable, not a design change.** It does not alter M1, any Part A/B
> value, any load, or any support condition. It translates the already-finalised geometry,
> thicknesses and materials of Parts A/B into native Revit 2026 elements via Dynamo Python
> scripts, since Revit is not executable in this environment (same constraint STAAD.Pro has had
> throughout — see H.4/H.5).

| # | Change implemented | Files | Basis | Status |
|---|---|---|---|---|
| **BIM-P1** | No pre-existing `Revit/` folder, `.rvt`, or Revit/Dynamo automation was found anywhere in the repository (full scan at session start) — this contradicts the task's premise of an existing folder to reuse; flagged rather than silently created. A new `Revit/` folder was created holding 6 Dynamo Python Script node files (`01_levels_and_grids.py` … `06_structural_sentry_post.py`) that build, when run inside Revit 2026: 14 Levels and 11 Grids (Master A.4.1/A.4.3/A.4.8); the main box structural envelope (PCC blinding, mat, perimeter walls W1-W4, W5/W6/W7 with the two blast-door openings, roof slab with the stair-void + 2 escape-shaft openings); the headhouse (HW1-HW4, roof, inner security door opening); the covered entry stairwell (raft, 4 walls, top landing, sloped flight, platform, 3-piece raking roof); the main staircase (3 flight waist slabs + L1/L2 landings, **FROZEN geometry, unchanged**); and the sentry post frame (4 footings, plinth beam, 4 columns × 2 storeys, 4 beams × 2 storeys, 2 slabs, ground-storey infill). Reinforcement and material physical properties are explicitly deferred (see `Revit/docs/00_README_WORKFLOW.md`). | `Revit/scripts/01…06*.py`, `Revit/docs/00_README_WORKFLOW.md`, `Revit/docs/01_STAAD_comparison.md`, `Revit/docs/02_QAQC_and_discrepancies.md` | A.4, A.5, B.1–B.8, D (STAAD cross-check) | **SCRIPTS AUTHORED. NOT EXECUTED — Revit 2026 is not available in this environment; editing/authoring these scripts is not running Revit, exactly as H.4 states for STAAD.Pro. No `.rvt` file exists.** |
| **U4 (new, open)** | **Sentry post absolute site position does not exist anywhere in the project** — Master A.2/A.4.8 and all four Rev F sentry DXF sheets state only "≥10 m clear of the shelter excavation," never a coordinate. BIM-P1 places it at an ASSUMED (11.000, 17.750) m — exactly the 10 m minimum, north of the entry stairwell — as a single, easily-relocated variable in the scripts. | `Revit/scripts/01_levels_and_grids.py`, `06_structural_sentry_post.py` | A.2, A.4.8 | **OPEN — needs the user's confirmation or a real site plan before Phase 2** |

**Verified after authoring:** every dimension used by the scripts was re-derived from Master A/B
(external/internal footprints, centreline offsets, level closures, stair rise/run) rather than
copied without checking — see `Revit/docs/02_QAQC_and_discrepancies.md` for the closure checks
performed. Main staircase geometry (24R @ 170.8333, 280 tread, 3 flights × 8, rise 4100, landings
L1/L2, 1200 flight widths, 200 well) is **unchanged** from Parts A.4.4/B.5, and the FROZEN clause
in `CLAUDE.md` was not touched.

**Not implemented, and why:**

| Item | Reason |
|---|---|
| The `.rvt` file itself | Revit 2026 cannot run in this (headless Linux) environment. See `Revit/docs/00_README_WORKFLOW.md`. |
| Reinforcement (native Revit rebar) | Explicitly deferred to a later phase — Part B's bar schedules are complete, but detailing them in Revit is documentation-phase work, not structural-envelope work. |
| Material physical/appearance properties | Types are named with their grade (M35/M30); IS-456 strength, appearance and thermal data are a later-stage task per the brief's own stage ordering. |
| C16 (roof/platform junction) | Still open (H.4). BIM-P1 follows B.6/A.7.6/F.2 (250 mm) without editing A.4.7 or reconciling the headhouse/stairwell roof geometry — see `Revit/docs/02_QAQC_and_discrepancies.md` item 2. |
| Architecture, rooms, finishes, schedules, sheets | Out of scope for this phase by the task's own instruction ("do not yet move to architecture"). |

## H.7 Revit 2026 BIM — Phase 1B (script review + execution preparation) — 3 September 2026

> **BIM-P1B is a review/hardening pass on the BIM-P1 scripts, not a design change or new
> geometry.** No dimension, level, thickness, material grade, or the FROZEN main-staircase
> geometry was touched. It fixes a real coherence risk found on review (duplicated sentry-siting
> constants) and adds rerun-safety that BIM-P1 lacked.

| # | Change implemented | Files | Basis | Status |
|---|---|---|---|---|
| **BIM-P1B-1** | **Rerun safety added.** BIM-P1's scripts 02-06 had no guard against re-running — every wall/floor/column/beam would duplicate on a second run (script 01 was already idempotent). Every element created by 02-06 now carries a unique Mark, checked against the document before creation; skips are reported separately from creates in each script's `OUT`. | `Revit/scripts/02…06*.py` | Phase 1B review, item 4 (duplication safety) | **IMPLEMENTED, NOT YET RUN IN REVIT** |
| **BIM-P1B-2** | **Sentry post siting de-duplicated.** BIM-P1 had the ASSUMED site-position constants (`SENTRY_ORIGIN_X_M/Y_M`, `SENTRY_ROTATION_DEG`) hardcoded separately in BOTH `01_levels_and_grids.py` and `06_structural_sentry_post.py` — a real risk that editing one without the other silently misplaces the frame relative to its own grids. Script 06 now derives the sentry post's origin and orientation live from the actual "SA"/"S1" Grid elements script 01 creates (line-intersection + direction-vector math on the real grid geometry), so there is structurally one source of truth, not two copies that happen to agree today. The [ASSUMED] (11.000, 17.750) m / 0° position itself is UNCHANGED — only how script 06 obtains it changed. | `Revit/scripts/01_levels_and_grids.py`, `06_structural_sentry_post.py` | Phase 1B review, item 5 (assumption control) | **IMPLEMENTED, NOT YET RUN IN REVIT — still OPEN pending the user's confirmation of the real site position, per U4 above** |
| **BIM-P1B-3** | **Column parameter setting made more robust.** Sentry column/beam base/top level and offset now set via the correct `BuiltInParameter` enums first (`FAMILY_BASE_LEVEL_PARAM` etc. — stable across localization/renaming) with name-guessing only as a fallback for width/depth, which has no stable enum. Family/type selection now prefers a loaded symbol whose name matches "concrete"/"rectangular" instead of blindly taking whichever one Revit lists first, and reports a warning in `OUT` when nothing loaded is a good match. | `Revit/scripts/06_structural_sentry_post.py` | Phase 1B review, item 1 (robustness) | **IMPLEMENTED, NOT YET RUN IN REVIT** |
| **BIM-P1B-4** | **Assumptions promoted to named constants.** PCC blinding extent (`PCC_EXTENT_M`) and the entry-stairwell raft founding offset (`RAFT_TOP_OFFSET_M`) were inline literals in BIM-P1; both are now single named constants near the top of their script, cross-referenced from a new "Assumption control" table in the README. The raft docstring's wording was also corrected — it previously said the raft sits "300 mm below the slab underside" while the code actually placed it flush with the underside (offset = slab thickness, 0.250 m); the geometry itself did not change, only the (previously inaccurate) description of it. | `Revit/scripts/02_structural_main_box.py`, `04_structural_entry_stairwell.py` | Phase 1B review, item 5 (assumption control) | **IMPLEMENTED, NOT YET RUN IN REVIT** |
| **BIM-P1B-5** | **C16 reviewed, deliberately left open.** Determination recorded: C16 does not block the rest of the structural model — every element in scripts 02-06 except one provisional Floor in script 04 is fully determined by the Master independent of C16's resolution. Not arbitrarily resolved; see the dedicated C16 section added to the README. | `Revit/docs/00_README_WORKFLOW.md` | Phase 1B review, item 6 | **STILL OPEN — needs the user's ruling, contained to one element** |
| **BIM-P1B-6** | Documentation rewritten: `00_README_WORKFLOW.md` gained a full beginner-exact "Run the scripts in Revit 2026" walkthrough (template choice, Dynamo access, per-script expected results, save procedure), a script order/dependency table, a Dynamo-vs-other-Revit-Python-environment note, an assumption-control table, and the C16 determination. `02_QAQC_and_discrepancies.md` gained script-review findings, a duplication-safety section, and a model-integrity/coherence risk table. | `Revit/docs/00_README_WORKFLOW.md`, `Revit/docs/02_QAQC_and_discrepancies.md` | Phase 1B review, items 2, 7, 8 | **IMPLEMENTED** |

**Verified after this pass:** all 6 scripts re-parsed as syntactically valid Python (`ast.parse`,
this environment's only available check — see Limitations). Every element-creation call site in
scripts 02-06 was re-read and confirmed wrapped in the new Mark-guard pattern; no creation call was
missed. The FROZEN main-staircase file (`05_structural_main_staircase.py`) had its rerun-safety
wrapper added but **zero dimension, level, or riser/tread value was touched** — confirmed by diff
against the BIM-P1 version.

**Not implemented, and why:**

| Item | Reason |
|---|---|
| Actually running the scripts in Revit 2026 | Still not available in this environment — see H.6. This remains a source-level review, not an execution. |
| Resolving C16 | Explicitly out of scope — "do NOT arbitrarily resolve C16" per this phase's own instructions. Left open, contained, documented. |
| New architectural elements | Explicitly out of scope — "do not create additional architectural elements yet" per this phase's own instructions. |
| Sentry post's real site position | Still genuinely unknown — the grid-derivation fix (BIM-P1B-2) makes the ASSUMED position consistent and easy to relocate, it does not supply the real one. |

---

## H.8 Structural CAD reinforcement package — revision SC1 — 4 September 2026

> **SC1 is a DELIVERABLE, not a design change. Not one value in Parts A, B, F or L was altered by
> it.** It takes the reinforcement design those parts already carry, verifies it independently,
> details it, schedules it and draws it. Three conflicts are raised (two of them new) and **none
> is resolved**.

**Scope:** the underground shelter only — mat, perimeter and internal walls, pressure slab, main
staircase, entry stairwell, headhouse, entrance and all significant openings.
**THE SENTRY POST IS COMPLETELY EXCLUDED** by the instruction that commissioned SC1. Parts B.8
and F.4 were not used and no sentry-post output exists in the package.

### What was produced — all under `Structural CAD/`

| # | Deliverable | Location | Extent |
|---|---|---|---|
| **SC1-D1** | Input audit | `QAQC/00_INPUT_AUDIT.md` | every dependency parsed; missing and conflicting information listed |
| **SC1-D2** | Design basis | `Calculations/01_DESIGN_BASIS.md` | materials, covers, L<sub>d</sub>, loads, combinations, methodology |
| **SC1-D3** | Element design | `Calculations/02_ELEMENT_DESIGN.md` | 16-step record for every in-scope element |
| **SC1-D4** | Independent verification | `Calculations/00_PartB_verification_output.txt` | **212 Part B values recomputed** |
| **SC1-D5** | Bar bending schedules | `Schedules/` | **92 marks + 1 fabric item, 70 457 kg** |
| **SC1-D6** | Drawings | `DXF/` | **30 A1 sheets**, AutoCAD 2010 ASCII |
| **SC1-D7** | Detail register | `Details/DETAIL_REGISTER.md` | every detail issued, and every detail deliberately not issued |
| **SC1-D8** | Generation scripts | `Scripts/` | 17 modules; `build_all.py` rebuilds the whole package |
| **SC1-D9** | QA/QC | `QAQC/` | main report, IS 456 matrix, IS 13920 matrix, legibility QA, DXF validation, bar-mark cross-check |
| **SC1-D10** | Documentation | `Documentation/` | README, drawing index, CAD standards, model consistency |

### Verification actually performed

| Check | Method | Result |
|---|---|---|
| Part B recomputed from first principles | `Scripts/verify_partB.py` | **212 values · 211 agree · 1 differs → C17** |
| IS 456 Table 19 τ<sub>c</sub> column corroborated | 8 independent Part B values reproduced | agrees to ≤ 0.1 % |
| Geometry re-extracted from the primary DXF | `ezdxf` parse of `1_Underground_Level_Plan.dxf` | **all 18 controlling dimensions agree with A.3 / A.4** |
| Load and combination register | parse of all four underground `.std` plus `Entry_Stairwell.std` | 11 cases and 5 combinations match verbatim |
| Revit leg | geometry constants read from the 6 Dynamo scripts | c/l 15.000 / 18.200, ESC 2 at 19.900, 22.000 × 6.200 — all agree |
| Bar mark ↔ schedule ↔ drawing | `Scripts/qa_crosscheck.py`, re-reading the finished DXFs | **0 orphans · all 92 + 1 drawn · 0 broken references** |
| DXF structural validation | `Scripts/validate_dxf.py`, 30 files | **0 errors, 0 review items** |
| **Main staircase** | frozen values re-extracted and compared | **CONFIRMED UNCHANGED** |

### Conflicts raised by SC1 — NONE RESOLVED

| # | Conflict | Held | Status |
|---|---|---|---|
| **C17** | **NEW.** The A.7.3 engineered-cover table states a total of **40.65 kPa**; its own column sums to **39.15 kPa** — a 1.50 kPa difference. Every individual line is arithmetically correct; the total row is not the sum of the column | **40.65 kPa held** — it is the value in A.7.3's total row, A.7.4, Part L and `DL2` in all four underground `.std`, and it is the larger value. At 39.15 the roof total would be 446.65 kPa, M<sub>p</sub> 697.9 and utilisation 51.2 % instead of 51.4 %. **No bar, spacing or link changes** | **RULED AND CLOSED — RC1, 10 Sep 2026 (H.14).** A.7.3 now shows the layer sum 39.15 **plus a declared allowance of +1.50** = 40.65, so the table no longer contradicts itself and nothing downstream moves |
| **C18** | Sump-pit base thickness: F.1 gives "walls/base 300/400" and the A.4.3 levels ((−)7.600 invert to (−)8.000 base) independently give **400**; the text on sheet S-06 says **300** for both | **RULED AT 400 — RC1, 10 Sep 2026 (H.14). (−)8.000 − (−)7.600 = 0.400 is arithmetic, not judgement, and F.1 agrees. S-06's text is a transcription error and is superseded** | **CLOSED** |
| **C16** | Roof / platform junction | **250 detailed**, on the authority of M.2. Flagged on R-001, R-603, R-702, R-703, R-803, R-804 | **RULED AT 250 AND CLOSED — RC1, 10 Sep 2026 (H.14). The A.4.7 clause has now been corrected; SC1 detailed the right thing all along** |

### Declared deviations from the Part E output standard

| # | Item | Part E standard | SC1 | Reason |
|---|---|---|---|---|
| **X1** | DXF format | E.3.1 R12 ASCII | **AC1024** | R12 does not carry usable DIMENSION / MTEXT / HATCH / LEADER entities, which the SC1 brief requires |
| **X2** | Layer names | E.3.2 22-layer table | **`S-*` system** | required by the SC1 brief; **a one-to-one mapping to the 22-layer table is issued** in `Documentation/02_CAD_STANDARDS.md` and printed on drawing R-002 |
| **X4** | Bar bending standard | Part G names BS 8666 + SP 34 | **project rule PBR-1** | neither document, nor IS 2502, is in the workspace. Only the four unambiguous BS 8666 shape codes are used; everything else is coded 99 |
| **X5** | Title block | E.3.1 180 × 62 | **180 × 100**, same position | more fields than 62 mm holds legibly |

**S-01…S-08 and the ten Rev F input drawings were NOT modified.** S-06 was read (it supplied the
sump-pit position and size, `[CONFIRMED]`) and left byte-identical. The seven missing output
sheets were **not regenerated and not fabricated** — their toolchain is still absent, per M.12
and the `CLAUDE.md` working rules.

### Not implemented, and why

| Item | Reason |
|---|---|
| Column, framed-beam and beam–column-joint drawings (R-501/502/503) | **No such element exists in the underground shelter.** B.3 already declares punching NOT APPLICABLE for the same reason. Drawing one would be fabrication. Recorded on R-001 and R-401 |
| Resolution of C16, C17 or C18 | All three are genuine conflicts inside the project record. M.5 and M.6 forbid silently choosing |
| Any STAAD analysis | STAAD.Pro is not available. **No result of any kind exists**, and every SC1 design action is labelled `MANUAL CALCULATION — NOT DIRECT STAAD OUTPUT` |
| Clause verification at source | **No code document is in the workspace.** SC1 cites clause numbers **only** from the Part G register and reports anything else as CLAUSE NOT VERIFIABLE |
| Second k<sub>s</sub> bound | Still outstanding — A.6 and K.2-A4 unchanged |
| Phase 3 SDOF support rotation | Unchanged. **Blast capacity remains not demonstrated** |
| Blast-valve, service-entry-plate and CBRN-penetration details | No structural design basis exists in the record. Reported NOT DETERMINABLE and **not fabricated**; a generic trimming rule is issued on R-003 and labelled as not a substitute for a designed detail |

### Status of the package

**NOT construction-ready.** `QAQC/Reinforcement_QAQC_Report.md` §5 lists **13 items requiring
review by a qualified structural engineer**. No part of SC1 claims "fully code compliant" — that
claim is not available while no code document is held.

---

## H.9 Drainage, HVAC and Schedule of Finishes packages — revisions DR1 / HV1 / FN1 — 5 September 2026

> **These three packages are DELIVERABLES, not design changes. Not one value in Parts A, B, F or L
> was altered by them.** They take what the project already decides — sheet S-06's services and
> ventilation basis, the Rev F architecture, the R-805 waterproofing interface — verify it
> independently, develop what is missing, and record what cannot be determined. **Four conflicts are
> raised (three of them new) and none is resolved.**

**Scope:** the underground box, the entry headhouse and the covered entry stairwell.
**THE SENTRY POST IS COMPLETELY EXCLUDED** by the instruction that commissioned this work. No sentry
post element appears in any drawing, schedule, calculation or script in the three packages.
**The main staircase geometry is untouched** — it is annotated and finished, never altered.

### What was produced

| Package | Rev | Contents |
|---|---|---|
| **`Drainage/`** | **DR1** | Design basis; **11 A1 sheets** D-001…D-305; 7 schedules; a 17-section calculation set; a **two-page A4 handout** (DXF + PDF); QA/QC; drawing index; one Revit script |
| **`HVAC/`** | **HV1** | Design basis; **6 A1 sheets** M-001…M-203; 7 schedules; a 14-section calculation set; a **two-page A4 handout** (DXF + PDF); QA/QC; drawing index; one Revit script |
| **`Schedule of Finishes/`** | **FN1** | **3 A1 sheets** A-601, A-611, A-612; 6 schedules covering **all 13 spaces**; QA/QC; drawing index; one Revit script |
| **`MEP_AND_FINISHES_COORDINATION.md`** | — | The cross-discipline check across all three, ten items |

**24 DXF, AutoCAD 2010 (AC1024) ASCII, all validated — 0 errors.** The sheet library subclasses
`Structural CAD/Scripts/sc_dxflib.py`, so the sheet standard is identical to the issued R-series.
Shared modules (`mep_proj.py`, `mep_dxf.py`, `mep_views.py`, `mep_validate.py`, `mep_render.py`) live
in `Drainage/Scripts/` and are used by all three packages — one definition, three consumers.

### Verification actually performed

**Sheet S-06's own basis was reproduced from first principles rather than quoted.**

| Reproduced | Result |
|---|---|
| Seepage wetted area **401 m²** — never defined on S-06 | 56.40 perimeter × 4.700 submerged + 136.40 mat = **401.48 m²**. It is the external envelope **below the design GWT**, not the internal area |
| Gas-tight envelope **67.8 m² / 217.0 m³** | **67.80 / 216.96** ✔ |
| Clean zone **57.8 m² / 185.0 m³** | **57.80 / 184.96** ✔ — and it is the envelope **less the decon airlock**, which S-06 does not state |
| FEMA 453 rate **264 m³/h** | **264.3** ✔ |
| Leakage **32.5 m³/h**, "11 %" | **32.5**, **10.8 %** ✔ |
| Time to 1.0 % CO₂ **9.9 h** | **9.9** ✔ |
| Airlock purge **13 min** | **12.8** ✔ |
| DN100 **10.6 m/s**, DN350 **7.5 m/s** | **10.61 / 7.51** ✔ |
| Septic tank, IS 2470 (Pt 1) | Every check reproduces exactly: 1050 required, 1125 provided |
| Rev E open-cut catchment 7.2 m² at 50 mm/h | **0.10 L/s** ✔ — which is how DR-C1 was identified |

**Twelve figures reproduce; one does not** — the soak pit, see C19.

### Conflicts raised — NONE RESOLVED

| Ref | Conflict |
|---|---|
| **C19** | **Soak pit is 2.3 % short of its own stated requirement.** S-06 prints "22.0 m² OK" against its own "area required 22.5 m²"; π × 2.0 × 3.5 = **21.99 m² < 22.50 m²**. Arithmetic, not judgement |
| **C20** | **S-06's design-flow table carries a superseded catchment.** 0.10 L/s for stairwell surface water is the **Rev E open-cut** figure; at Rev F the approach is covered and drawing 5 note 5 states the catchment with the door shut is zero. Conservative, so nothing is unsafe |
| **C21** | **The master and S-06 disagree on the filter train duty.** A.3 says "2 × **250** m³/h filters"; S-06 states **300 m³/h** in nine places. **At 250 one train is below the 264 m³/h FEMA rate S-06 itself computes**, so the "true N+1" claim fails on the sheet's own criterion |
| **C16** | Carried, **not** resolved. Drainage has a dependency (which roof a 2.25 m² catchment belongs to — the total is unchanged either way); HVAC has none; finishes only the drip at the step |

### Referred to other disciplines — decisions this work does not own

**BW-01** mat recess for the one buried drain, *requested not accepted*, with a no-buried-drain
fallback drawn · **DR-F4** floor screed exceeds the 1.0 kPa mat SIDL by 0.24 kPa (25 kN), acting
favourably for flotation · **DR-F5** two of the three hydraulic zones the protective boundary creates
have no drainage destination · **HV-F2** the raw-air duct runs 11.2 m unfiltered through the clean
zone; whether the trains should move to bay 1 is *raised not taken* · **CO-3** bay 5 is 80 % occupied
as drawn and the CO₂/O₂ plant and dehumidifier A.3 requires have no space · **FN-U1** no door is
scheduled in W5 anywhere in the project, yet the airlock needs a clean-side exit.

### Not implemented, and why

| Item | Reason |
|---|---|
| Sheet **D-202**, underground rainwater | **There is no rainwater below ground.** The box is buried and tanked. Issuing an empty sheet would mislead |
| Any **cooling or heating load** | **Eight inputs missing**, of which the rock temperature at (−)6.100 governs. No load is calculated and none is implied |
| **Total fan duty** | Five of eight loss components are vendor data. The 161 Pa that *can* be calculated is given; a total would be fabricated |
| **Finish products, thicknesses, colours** | **No finish specification exists anywhere in the project.** Every code is a performance requirement; nine missing items are listed |
| Positions of the **soakaways, septic tank and external chambers** | **No site plan, boundary or contour exists.** Five pipe lengths and the IS 2470 (Pt 2) offsets are recorded as not determinable |
| Resolution of **C16, C19, C20, C21** | M.5 and M.6 forbid silently choosing |
| Any **STAAD** work | Unchanged — STAAD.Pro is not available and no result exists |

### Status of the packages

**NOT construction-ready and NOT a final design.** Each carries its own QA/QC report using
PASS / REVIEW / DATA REQUIRED / NOT DETERMINABLE. **No code-compliance claim is made** — several
standards are cited by title only because no code document is held (M2), the **percolation test
(A7) is still mandatory and outstanding**, and the fan duty and cooling load cannot be closed
without vendor and site data.

---

## H.10 Works Management package — revision WM1 — 7 September 2026

**Scope.** A complete Works Management package for the **entire project** — the main
underground box, the entry headhouse and covered stairwell, the escape shafts, the
engineered cover, the **sentry post**, the services, the external works, the concealment
works and completion — from mobilisation to handover. Everything lives in a new
`WORKS MANAGEMENT/` folder.

**Inputs.** The user supplied a preliminary Microsoft Project schedule,
`UG CBRN HDRND OPS ROOM MCS — R0` (130 lines, 224 working days, 02.11.26 → 26.07.27) and
its two-page A3 PDF export. Both were parsed. The package also reads master Parts A, B, F,
G and L, the Rev F sentry-post drawings 3, 4 and 6, and the SC1, DR1, HV1 and FN1 schedules.

### THE ONE DESIGN CHANGE — reference SP-B1

| | |
|---|---|
| **Instruction** | **The sentry post walls shall be BRICK MASONRY WALLS** |
| Replaces | The "200 RC BALLISTIC INFILL PANELS" of Rev F (A.4.8, drawings 3, 4 and 6) |
| Adopted construction | **190 mm one-brick modular brickwork to IS 1077 (190 × 90 × 90) in CM 1:6**, built inside the **confirmed 200 mm structural zone**, the residual 10 mm taken up at the internal face in the plaster |
| Why 190 and not 230 | 230 conventional brickwork would project 30 mm past the column faces and change the **confirmed 4000 × 5000 external envelope**. 190 preserves every confirmed dimension. `[A]` — needs the designer's confirmation (WM-V4) |
| Panel height | **2.600 m** — the project's OWN confirmed figure (A.7.7: 13.000 kN/m = 0.200 × 2.600 × 25, verified; drawing 6 repeats "200 × 2600 high") |
| Quantity | **12.20 m³ / 64.19 m² face** — 6.88 m³ ground storey, 5.32 m³ first storey, net of openings. ≈ 6 400 bricks, 14.5 bags cement, 3.0 m³ sand |
| Openings | Read from the Rev F drawings: ground D1 900 + W1 1200; first storey 8 armoured vision panels 1200 wide + D1 900 |

**Consequences of SP-B1, recorded not buried:**

1. **Lintels are now required** over all nine openings. The RC panels needed none.
   **No lintel design exists anywhere in the project** — carried as WM-V5 and as
   provisional BOQ item `SP-06`.
2. **A wall tie detail is now required** between the masonry and the columns. None exists —
   WM-V11.
3. **The seismic weight of the frame changes.** Brickwork at ≈ 20 kN/m³ over 0.190 × 2.600
   gives ≈ 9.9 kN/m against the **confirmed 13.000 kN/m** of the 200 RC infill, so the
   seismic weight falls and the existing **V<sub>b</sub> = 73.18 kN is conservative**.
   **That is a direction, not a verification.** Referred to the structural discipline as
   WM-V6. **A.7.8, B.8 and F.4 are UNCHANGED by this package.**
4. **Ballistic performance.** Rev F names the panels "200 RC **BALLISTIC** INFILL". Brick
   masonry does not provide equivalent ballistic protection. The instructed change removes
   a stated protective function from a structure the project already declares **not blast
   designed and expendable**. Recorded as WM-V7 so the decision is visible.

### What was produced — all under `WORKS MANAGEMENT/`

| Deliverable | Contents |
|---|---|
| `Underground_Shelter_Works_Management_Handout.pdf` | **44 pages, 25 sections** — the final-semester handout, covering the whole project |
| `Programme/Underground_Shelter_Final_Works_Programme.xml` | **The master programme, MSPDI** — Microsoft Project's own published XML schema |
| `Programme/…_Programme.pdf` | **7 A3 sheets** — basis and milestone register, summary Gantt, 5 sheets of detailed Gantt with the critical path |
| `Programme/…_Programme.csv` | Task list for import into any other planning tool |
| `Underground_Shelter_WBS.md` / `.csv` | **279 activities, 18 milestones, 404 logic links**, 3-level WBS, 14 level-1 packages |
| `Underground_Shelter_BOQ.md` / `.csv` | **90 items in 10 sections**, whole project |
| `Underground_Shelter_Resource_Plan.md` / `.csv` | **33 resources, 426 assignments** — every resource used on the programme |
| `Underground_Shelter_Procurement_Plan.md` / `.csv` | 16 packages, all tied to programme activities; long-lead register |
| `Underground_Shelter_QA_QC_Plan.md` / `.csv` | **42 ITP items, 16 hold points that are activities in the programme** |
| `Underground_Shelter_Safety_Risk_Register.md` / `.csv` | 15 hazard classes, **25 risks** |
| `Underground_Shelter_Codes_References.md` / `.csv` | **78 references** |
| `Documentation/` (5 files) | Component register · construction methodology · **sentry post brick masonry (SP-B1)** · progress monitoring · assumptions and verification register |
| `Schedules/BOQ_QUANTITY_DERIVATION.txt` | ~800 lines of quantity working with the source of every input |
| `Schedules/WM_CPM_OUTPUT.txt` | Critical-path calculation and milestone dates |
| `QAQC/WM_CONSISTENCY_AUDIT.txt` | **65 executed consistency checks, 65 pass** |
| `Scripts/` (9 files) | `wm_build_all.py` regenerates the entire package from `wm_data.py` + `wm_content.py` |

### The programme

| | |
|---|---|
| Start | **Monday 2 November 2026** — carried from the supplied R0 schedule `[A]` |
| Finish | **Saturday 20 November 2027** |
| Duration | **326 working days** (384 calendar days) against R0's 224 |
| Calendar | **Six-day week, Mon–Sat**, Sunday non-working — *read from* R0 (266 calendar days − 38 Sundays ≈ its stated 224), plus five date-certain national holidays. **Festival holidays are NOT fabricated**; a 10-day contingency activity `A14098` absorbs them |
| Critical path | 75 activities at TF = 0: possession → SI and **monsoon GWT monitoring** → excavation support design → rock excavation → formation → tanking → mat → walls → pressure slab (**14-day cure + 14-day props, IS 456 Table 11**) → roof membrane → six-layer cover incl. burster slab → external works → snag → contingency → handover |
| Sentry post | Deliberately started only **after the rock breaking finishes** (no green concrete within 10 m of a hydraulic breaker). Carries **118 days of float** |

### Verification actually performed

* **65 consistency checks executed and passed** (`QAQC/WM_CONSISTENCY_AUDIT.txt`), covering
  component coverage, brick masonry consistency across all 12 documents, WBS ↔ programme
  identity, network integrity (acyclic, no open ends, no undefined or unused resources),
  18 sequencing rules, WBS ↔ BOQ, BOQ ↔ project record, procurement ↔ programme, QA/QC ↔
  activities, safety ↔ activities, codes, handout ↔ package, and that no file outside
  `WORKS MANAGEMENT/` and `master/` was modified.
* **Six SC1 concrete volumes independently re-derived and reproduce exactly** — mat 81.84,
  roof net 112.03, perimeter walls 103.68, W6/W7 12.80, W5 3.20, headhouse 32.74.
* **Reinforcement reconciled to the SC1 bar bending schedule**: 70.457 t.
* **The MSPDI file was read back with MPXJ 16.7.0** and every task count, summary count,
  milestone count, link count, resource count, assignment count, calendar day type,
  calendar exception and date compared against the CPM that produced it. All agree.
* **The engineered cover build-up reproduces A.7.3**: six layers summing to 2 000 mm.

### Conflicts raised by WM1 — NONE RESOLVED

Twelve verification items, **WM-V1 to WM-V12**, all left open. The ones that matter:
**WM-V1** ground-storey panel height, the project's confirmed 2.600 against the 2.750 the
levels imply (2.600 used); **WM-V2** the first-floor west wall, where D1 lies inside the
vision panel on the Rev F drawing; **WM-V3** window and vision-panel heights, stated
nowhere; **WM-V5** the missing lintel design; **WM-V6** the changed seismic weight;
**WM-V7** the lost ballistic function. Full list in
`Documentation/WM_ASSUMPTIONS_AND_VERIFICATION_REGISTER.md`.

### Master items carried forward untouched

**C16, C17, C18, C19, C20, C21, U1, U2, U3, U8** — all ten appear in the WM1 verification
register and **none is resolved, downgraded or deleted.** C21 (filter duty 250 vs 300 m³/h)
is flagged as needing a ruling **before the filter trains are ordered**, which is why the
programme puts the enquiry activity `A1130` ahead of the delivery `A1135`.

### Information the project does not contain — 13 items, each dated against the programme

The largest is that **no electrical design package exists**: the scope is confirmed
(EMP Zone 2 enclosure, 15 kVA generator, earthing to 5 Ω, penetration protection) but no
circuit, cable, luminaire, DB or earth-electrode schedule does. Every electrical quantity
reads *"To be verified from final measurement"* and no electrical enquiry can be issued.
Also missing: the site plan (blocks the berm, access, hardstanding and five drainage runs),
the sentry post lintel design and wall tie detail, blast door and blast valve vendor
details, the service-entry plate size, the duct penetration schedule, the EMP enclosure and
vision panel specifications, the sentry ground-floor slab design, the finish product
selections, and the W5 gas-tight door D-05.

### Not implemented, and why

| Item | Why |
|---|---|
| A native `.mpp` file | **Microsoft Project's `.mpp` is an undocumented binary (OLE2) format writable only by Microsoft Project itself.** Verified here against MPXJ 16.7.0 — `org.mpxj.writer.FileFormat` offers JSON, MPX, MSPDI, Planner, PMXML, XER and SDEF, and no MPP writer exists. The master programme is issued as **MSPDI**, Microsoft's own published XML schema for Project; *File → Open* then *File → Save As → Project (\*.mpp)* produces the binary in one step with nothing lost. **Not imitated, not renamed, not faked.** |
| Rates in the BOQ | **AS WM1 STOOD, and the reason it stood that way:** rates come from the **MES SSR**; no item number could be verified from the material available, and inventing one would put false authority on a document an executing engineer might rely on. **SUPERSEDED BY WM4, 15 September 2026 (H.38): the owner supplied the Maharashtra PWD State Schedule of Rates 2022-23 and the bill is now priced from it, item number by item number, each with the SSR page it was read from.** The MES SSR caveat still applies to MEASUREMENT and SPECIFICATION references, which is a different role, and to the lines WM4 leaves NOT PRICED because no schedule item exists for them. |
| Any change to A.7.8, B.8 or F.4 for the sentry post | The seismic re-check that SP-B1 implies is a **structural** matter. Direction noted (conservative), verification referred. |
| Resolution of any master conflict | M.5 and M.6 forbid silently choosing |
| Any STAAD work | **STAAD.Pro is not available and no analysis was run.** Reading a `.std` file is not running an analysis |
| Any change to a drawing, model, calculation or design file | Out of scope by instruction. **No design file was touched.** |

### Status of the package

**FOR REVIEW — not a construction issue.** Every output rate and vendor lead time is
`[A]` and must be re-tested against the appointed contractor. Twelve verification items and
thirteen information gaps are open. **The main staircase is unchanged** — 24R @ 170.8333,
tread 280, 3 flights × 8, total rise 4100, flights 1200 wide, 200 well, 2533 headroom,
reproduced in the programme exactly as frozen. **No design value in Parts A, B, F or L was
altered.**

---

## H.11 Drawing QA/QC pass — revision QA1 — 9 September 2026

**Scope.** A drafting, annotation, sheet-composition and title-block QA/QC pass over
**every DXF in the project — all 65 files**. Instructed by the user, whose brief was
explicit and repeated: each **existing** DXF is to be inspected, corrected and **saved
back at its own filename and location**; no parallel "clean" package, no duplicate
final versions. **QA1 changed no engineering design.** No dimension, level, bar mark,
bar size, spacing, load, material grade, thickness or room size was altered anywhere.
Parts A, B, F and L are untouched.

**Where the work was done.** The 54 generated sheets (R-001…R-805, D-001…D-305,
M-001…M-203, A-601/611/612 and the four A4 handouts) were fixed **in their generators**
and regenerated to the same filenames, so the generators and the DXF stay in agreement.
The eleven `current/cad` drawings have no generator in the workspace and were corrected
by a recorded, re-runnable pipeline, `current/cad/Scripts/qa1_build_sheets.py`.

**Measured result** (`DRAWING QAQC/Scripts/`, run over all 65 files):

| | before | after |
|---|---:|---:|
| Text-on-text overlaps, all 65 drawings | 67 | **2** |
| — the 54 generated sheets | 49 | **0** |
| — the 11 `current/cad` drawings | 18 | **2** |
| Annotation crossing hard line work — `current/cad` | 50 | **10** |
| Drawing geometry inside a notes panel — generated sheets | 46 | **35**, all legend panels and one section outline, which are meant to contain line work |
| A view drawn on top of its own notes panel | 3 sheets | **0** |
| Entities outside the sheet border | 0 | **0** |
| Drawings carrying a border and title block | 54 of 65 | **65 of 65** |
| Panel / table body text below print size on A1 | most of the package | **0** |

**Principal defects found and corrected.**

1. **`sc_dxflib.panel()` and `table()` sized their boxes by eye.** Both now measure
   their own content with the font metrics ezdxf uses to place it; a note line cannot
   cross its border and a cell cannot cross a column rule. Body text is lifted to a
   legible 2.0 mm wherever the box has room (it was all at the 1.4 mm library minimum).
2. **Blocks pinned under variable-height blocks.** A bar-mark key is as deep as the
   marks a sheet nominates; the schedule extract beneath it was pinned at a fixed *y*.
   On R-101 the key ran 25 mm through the schedule. Nine such pairs are now chained.
3. **Three views were drawn on top of their own notes panels**, found by plotting, not
   by any numeric check — **R-601** (stair plan over the MATERIALS panel and off the
   right border), **R-701** (headhouse roof plan through the roof design-basis panel),
   **M-201** (section B-B through the notes panel). All three view origins corrected.
4. **Pipe tags rotated along vertical runs** swept a tall box through every label beside
   the pipe (D-201 worst). Vertical runs now read horizontally, beside the run.
5. **HV-H2's operating-modes table hard-sliced every cell** — "NO FILTER BYPASS IS SHO",
   "bay 8 not pressuri" — losing information on a sheet meant to be read in an
   emergency. Full text restored, the table fits its own columns.
6. **The ten Rev F drawings were drawings, not sheets.** They now carry an A1 border,
   inner border, 180 × 100 title block, ruled NOTES box and revision strip, drawn in
   model units at each drawing's own stated scale, in LINE and TEXT only so the R12
   (AC1009) format is preserved. 93 labels were moved off the line work and 28 leaders
   added. **Where a drawing block was re-centred on its new sheet it moved as a PURE
   VERTICAL TRANSLATION** — verified entity by entity, so every dimension, level and
   geometric relationship is preserved.

**Drawing numbers.** The ten Rev F drawings were given numbers **A-101…A-105** (plans),
**A-201…A-204** (sections) and **A-301** (elevation). **Their filenames are deliberately
unchanged** — Part E.2, Part I.1 and every document in this project cite them, and the
brief requires each existing DXF to keep its own name. The number lives in the title
block; `DRAWING QAQC/DRAWING_INDEX.md` carries both.

**A-301 FRONT ELEVATION — a genuine drafting error found and corrected.** The drawing is
44 m long, which is **880 mm at 1:50**; the A1 drawing area is 821 mm wide. Its own note
read "SCALE 1:50 AT A1", which could never have been plotted. The scale governs
measurement and was kept; the **sheet size was corrected to A0** and the note now reads
"SCALE 1:50 AT A0". **This is the only text content changed anywhere in the package.**
A ruling is invited — see K.1 item **QA-1**.

**DECLARED DEVIATION FROM RULE M.12.** M.12 forbids editing a generated DXF directly.
**S-06 is a generated output sheet and its generator is not in the workspace**, so the
brief's instruction could be met only by editing it directly; 15 labels were moved on it
and nothing else was touched. Recorded here rather than hidden, and revertible from git.
**S-01…S-05, S-07 and S-08 remain absent and were not fabricated.**

**The frozen main staircase is unchanged** — 24R @ 170.8333, tread 280, three flights of
8, total rise 4100, flights 1200 wide, 200 well, 2533 headroom. Verified against the
pre-edit files.

**Open items C16…C21, U1–U3, U8 and WM-V1…12 were not resolved, closed, downgraded or
removed.** The panels that carry them are unchanged in content.

**New files.** `DRAWING QAQC/` (drawing index, QA/QC report, five inspection scripts)
and `current/cad/Scripts/` (the five-module pipeline that produced the current
`current/cad` state). No design file, calculation, schedule or STAAD model was modified.

## H.12 Burster slab laid to falls + sentry post masonry completed — revisions BS1 / SP-B2 — 10 September 2026

**Two instructed design changes, recorded together because they were carried through the
package in one pass.** Both are recorded in full at the point of design — **BS1 in A.7.3**,
**SP-B2 in A.4.8** — and this section is the change record, not a second authority. If the
two ever disagree, Part A governs.

---

### BS1 — the RC burster slab is laid to falls

**Instruction.** *"Make the RC burster slab sloping so that water seeps in moves
sideways."*

**What changed.** The 200 mm M30 burster slab, and every layer above it, is laid to a
**1:50 crossfall, crowned on the box longitudinal centreline (Y = 3100) and falling each
way to the box edge** — the same fall and the same direction as the finished grade, which
A.4.3 already records as *crowned, falling 1:50 away*. Over the 3100 half-width the slab
drops **62 mm** crown to edge.

**Why it was a real defect and not a preference.** D-102 note 3, D-001 note 1 and
calculation D.7 all state that infiltration through the cover is *"intercepted by the
granular filter and dispersed at the berm toe"*, and that no pipe penetrates the cover.
The granular filter bears **directly on the burster slab**. On a flat slab that sentence
cannot be true: the filter drains to a level surface, the water ponds on the slab and the
only path onward is the slab's own construction joints. The crossfall is what gives the
filter layer the gradient the drainage design already claimed it had.

**Load, thickness and analysis — UNCHANGED.**

| | |
|---|---|
| Layer thicknesses | Every layer keeps its **nominal** thickness. The fall is taken up entirely in the **compacted engineered fill** below the rubble: **750 at the crown, thinning to 688 at the box edge.** |
| Cover load | **40.65 kPa at the crown, exactly as before**; *less* toward the edges (≈ 1.24 kPa lighter at the box edge). **The cover load does not increase anywhere.** |
| COMB 103 | **448.15 kPa — untouched.** A.7.4, Part B, Part F and Part L are untouched. |
| STAAD | **All three `.std` files untouched.** No geometry, thickness, support, load case or combination was edited. |
| Burster slab reinforcement | **M30, T12 @ 150 B/W — unchanged.** It is a cover element, not a structural element of the box. |
| Measurement | Quantities are measured to the **nominal** 750 fill, which over-measures the fill by ≈ 4 % and is therefore conservative. **No WM quantity, rate or cost was changed by BS1.** |

**C17 IS NOT RESOLVED BY THIS.** The A.7.3 column still sums to 39.15 kPa against the
stated 40.65 — at the crown, exactly as it did before. BS1 does not touch that
discrepancy and must not be read as closing it.

**Files carrying BS1** (all edited in their generators, then regenerated to the same
filenames; the one `current/cad` drawing edited directly, per H.11):

| File | Before → after |
|---|---|
| `master/MASTER_PROJECT_STATE.md` A.7.3 | Cover table unchanged; **new BS1 block** beneath it |
| `Structural CAD/Scripts/g03_roof.py` → **R-302** | Cover build-up drawn as five flat lines → drawn as a **real 1:50 crown** (`CROWN_X = 3100`, `FALL = 1/50`); only the protection screed stays flat, because it sits on the flat roof; 1:50 fall arrows added on the filter layer; labels now read *"BURSTER SLAB M30 200 - LAID TO FALLS"*, *"GRANULAR FILTER 150 - DRAINS ON THE SLAB"*, *"COMPACTED FILL 750 CROWN / 688 EDGE"*, *"FINISHED GRADE, CROWNED 1:50"*; panel line *"LAID TO A 1:50 CROSSFALL - BS1, master A.7.3"* |
| `Drainage/Scripts/d01_plans.py` → **D-102** | Note 3 gains four continuation lines stating the crossfall, why the filter needs it, the 62 mm, and **"STILL NO PIPE ANYWHERE IN THE COVER"** |
| `Drainage/Scripts/d02_details.py` → **D-301** | Cover build-up section gains two lines: the fall is **across** this section, not along it, which is why the layers correctly read flat on a longitudinal section |
| `Drainage/Scripts/dr_calc.py` → `DR_CALC_OUTPUT.txt` D.7 | The "not drained by pipework" paragraph now states the crossfall **before** the sentence it makes true |
| `Drainage/Scripts/mep_proj.py` | Shared `COVER_BUILDUP` burster-slab function text → *"BREAKS UP A PENETRATING ITEM - LAID TO 1:50 CROSSFALL, BS1"* |
| `current/cad/2_Side_Section_with_Stairs.dxf` (**A-202**) | *"200 RC BURSTER SLAB"* → *"200 RC BURSTER SLAB - LAID TO 1:50 CROSSFALL (BS1)"* |

**A self-inflicted drafting error found by plotting and corrected.** The first R-302 crown
drew the compacted-fill top **both flat and crowned**. The fill is the layer that takes up
the fall, so it cannot be both; the spurious flat line was removed. Only the protection
screed is flat.

---

### SP-B2 — lintels and wall ties for the sentry post masonry infill

**Instruction.** *"Modify sentry post such that it has normal walls with beams and column
rather than RC walls. Make changes in all places."*

**Where this stood before.** The sentry post has been a **framed structure since Rev F** —
C1 350 × 350 columns, B1/B2 250 × 450 beams, S1 150 two-way slab, PB plinth beam, F1
footings — and **SP-B1** (7 Sep 2026, H.10) had already changed the walls from *200 RC
ballistic infill* to **190 one-brick modular brickwork to IS 1077 in CM 1:6**. So the frame
the user asked for already existed and the walls were already masonry **in the master** —
but SP-B1 left two things undone, and until they were done the walls as recorded **could
not be built**:

- **WM-V5** — no lintel design existed anywhere in the project.
- **WM-V11** — no wall-tie detail existed.

and the **drawings still said RC**. SP-B2 closes the first two and carries the change onto
the drawings. **No frame member changed. Nothing was added to the frame.**

**Lintel L1 — one type over every opening in the sentry post**

```
190 wide x 150 deep, M30 / Fe500, cover 30, bearing 200 each end
2-T10 bottom  -  2-T8 top (hangers)  -  T6 two-legged links @ 150
```

Openings served — **eleven in all**: ground **D1 900** and **W1 1200**; first storey
**D1 900** and the **eight 1200-wide vision-panel openings**. The 1200 opening governs, so
one type covers all.

**How a lintel was designed without inventing an opening height.** **The opening HEIGHTS
are not stated on any drawing** — this is the project's own open item **WM-V3**, and it
stays open. WM1 assumed **1200 for measurement only**, tagged `[A]`/`[N]`. Rather than lean
on that assumption, L1 is designed to the **bound that does not depend on the height at
all**: masonry standing *just below* the 60° arching height (0.866 × 1.315 = 1.139 m),
which is the heaviest load any opening height can produce. Above that height the masonry
arches and relieves the lintel; below it there is simply less masonry. **No opening height
has been invented, and WM-V3 is neither closed nor confirmed — L1 holds whatever it is
ruled to be.**

**A wording discrepancy found and flagged, not silently edited.** The K.1 **WM-V5** text
reads *"no lintel design exists for the **nine** sentry-post openings"*. Eleven openings
need a lintel; WM1's own quantity `SP-06` measures eleven, and the "nine" matches the nine
*unstated-height* window and vision openings of **WM-V3** rather than the lintel count.
**No quantity, rate or cost depends on the wording.** The K.1 block is left as written.

| Step | Value | Authority |
|---|---|---|
| Effective span | min(clear + d, c/c bearings) = min(1315, 1400) = **1.315 m** | IS 456 Cl. 22.2 |
| Masonry load | 0.190 × 20 × 1.139 = **4.33 kN/m** | arching bound, above |
| M, V | 0.935 kNm, 2.85 kN → M<sub>u</sub> = **1.403 kNm** | |
| Capacity | M<sub>u,lim</sub> = 0.133 f<sub>ck</sub>bd² = **10.03 kNm** → **14 % utilised** | IS 456 |
| Steel | A<sub>st</sub> req 29.5 mm²; **Cl. 26.5.1.1 minimum 0.85bd/f<sub>y</sub> = 37.1 mm² GOVERNS**; 2-T10 = 157 mm² | IS 456 Cl. 26.5.1.1 |
| Shear | τ<sub>v</sub> = 0.195 vs τ<sub>c</sub> ≈ 0.56 (M30, p<sub>t</sub> 0.72 %) → **no shear steel required** | IS 456 Table 19 |
| Links | T6 @ 150 = the **nominal minimum** (max spacing 324) | IS 456 Cl. 26.5.1.6 |

**The lintel carries masonry only.** The floor and the roof go to B1/B2 at each level —
that is the whole point of the frame.

**Wall ties.** 6 mm dia MS ties at **every fifth course (≈ 450 mm)** up both column faces,
projecting **200 mm** into the bed joint, anchored to the column by a cast-in or
drilled-and-grouted 10 mm dowel. The **top course is built tight to the beam soffit and the
last joint packed**, because the analysis takes **R = 3.0** — the infill is **not** separated
from the frame and must not be. Separating it is the R = 5.0 special-moment-frame case,
which this project does not claim.

**What SP-B2 does NOT change.** No frame member, no footing, no slab, no storey height, no
envelope, no grid. **Infill on the first-floor beams stays at 13.000 kN/m** in A.7.7 and in
`Sentry_Post_Framed_Seismic.std`. Brick gives ≈ 9.88 kN/m, which is **lighter**, so the
modelled value stays **conservative** — a direction, not a verification.

**Open items — what SP-B2 closes and what it does not.**

| Item | Status after SP-B2 |
|---|---|
| **WM-V5** — no lintel design exists; `SP-06` provisional; *"structural design required"* | **CLOSED by L1 above.** The design that did not exist now exists, to IS 456 with clause citations — `[R]` reconstructed engineering, not a confirmed project value. |
| **WM-V11** — no wall-tie detail exists | **CLOSED by the tie detail above** — `[R]`. |
| **WM-V3** — opening heights not stated on any drawing | **STILL OPEN, deliberately.** L1 is designed to a bound that does not use a height, so it neither needs nor confirms WM-V3's assumed 1200. |
| **WM-V6** — seismic re-check for the lighter masonry | **STILL OPEN.** The structural discipline must re-run it. Nothing here is a substitute. |
| **WM-V7** — the ballistic function of the Rev F panels | **NOT CLOSED AND CANNOT BE CLOSED HERE.** Brick masonry does not give the ballistic protection the Rev F *"200 RC ballistic panels"* were named for. That is a client / military decision, not a drafting one. |

**Files carrying SP-B2** (all four are `current/cad` Rev F drawings, edited directly and
in place, at the same filenames — the supplied-DXF rule, and H.11's recorded position):

| File | Before → after |
|---|---|
| `master/MASTER_PROJECT_STATE.md` A.4.8 | SP-B1 block unchanged; **new SP-B2 block** beneath it |
| `3_Sentry_Post_Ground_Floor_Plan.dxf` (**A-103**) | *"200 RC BALLISTIC INFILL PANELS"* → *"190 BRICK MASONRY INFILL (SP-B1)"*; *"200 RC BALLISTIC PANELS ARE INFILL - SEE THE FRAMING PLAN, DRAWING 6"* → *"190 BRICK INFILL IN THE RC FRAME - SEE THE FRAMING PLAN, DRAWING 6"* |
| `4_Sentry_Post_First_Floor_Plan.dxf` (**A-104**) | Same infill note → *"190 BRICK INFILL IN THE RC FRAME…"* |
| `5_Front_Elevation.dxf` (**A-301**) | *"FRAMED SCHEME - RC FRAME SHOWN DASHED BEHIND THE 200 INFILL"* → *"FRAMED SCHEME - RC FRAME DASHED BEHIND THE 190 BRICK INFILL"* |
| `6_Sentry_Post_Framing_Plan.dxf` (**A-105**) | Infill callout → *"190 BRICK MASONRY INFILL - NON STRUCTURAL (SP-B1)"*; the load-schedule line now reads *"13.000 kN/m RETAINED - see note below"*; the R = 3.0 / R = 5.0 note rewritten to say the infill is brick, is **not** separated, and that 9.88 < 13.000 keeps the model conservative, with **WM-V6 and WM-V7 named as still open**; **new SP-B2 panel** giving L1, its full design basis, the tie detail, and the WM-V7 warning |

**A-105 is the sentry post's framing plan and now carries the whole masonry design** —
lintel, ties, and the reason the infill must stay bonded to the frame — so a builder
reading one sheet has all of it.

**SP-B2 carried through the Works Management package, 10 September 2026.** The WM1
documents recorded, in **eleven places**, that no lintel design and no wall tie detail
existed in the project. That is no longer true, so the statements were corrected at
their generators and the package rebuilt.

| File | Before → after |
|---|---|
| `Scripts/wm_content.py` | The SP-B1 consequences paragraph now says both designs exist; **TIES TO THE COLUMNS** carries the designed 6 mm MS ties at every **fifth** course, **superseding the SP-B1 planning placeholder of every fourth course**; **LINTELS** carries L1 in full with its IS 456 clauses; risk `R-09` now names WM-V6 as the one part of it still open |
| `Scripts/wm_docs.py` | Shared document header gains an **AMENDED for SP-B2** banner; the masonry document's verification table and the package register mark **WM-V5 and WM-V11 CLOSED**; the BOQ narrative gains a superseded-by-SP-B2 note; the codes table cites the four IS 456 clauses L1 is designed to; the two lintel/tie rows in the **information-gap list are struck through as SUPPLIED** |
| `Scripts/wm_handout_pdf.py` | Table 8.3 and its caption, and the two narrative passages that listed the missing lintel and tie detail among the package's known gaps |
| `Scripts/wm_quantities.py` | The WM-V5 note in the quantity derivation, including the **0.485 m³ at 190 against `SP-06`'s 0.510 m³ at 200** |

**The tie spacing was a real contradiction and is now resolved in favour of the design.**
WM1 assumed ties *"at every fourth course"* as an explicit placeholder made when no
detail existed; SP-B2 designs them at **every fifth course (≈ 450)**. The placeholder is
superseded and is recorded as such rather than quietly dropped.

**NO QUANTITY, RATE, DURATION, DATE, FLOAT OR RESOURCE CHANGED.**
`Underground_Shelter_BOQ.csv`, `Underground_Shelter_WBS.csv` and
`Underground_Shelter_Final_Works_Programme.csv` are **byte-identical**. `SP-06` still
measures the superseded provisional 200 × 150 section — WM1 is a preserved revision and
26 litres of M30 changes nothing. The package's own consistency audit runs **65 checks,
65 pass**, including the handout-versus-package headline-figure check.

---

### Verification actually performed for BS1 + SP-B2

1. **Package QA re-run over all 65 DXF** after every edit — **2 text-on-text and 10
   annotation-crossing-line-work residuals, identical to the QA1 baseline in H.11.**
   Neither change regressed the drafting QA.
2. **A regression I introduced was found and fixed.** The longer A-103 label
   (32 characters against 30) ran into the *"W1 1200"* wall tag, taking that sheet from 0
   to 1 text-on-text. The note was **left-aligned onto the same x as the "B1 / B2 250 × 450"
   note directly above it** — which is better drafting than the centred position it had —
   and A-103 is back to **0 text-on-text, 0 hard-geometry**.
3. **A-105's NOTES box was rebuilt**, not overflowed. The SP-B2 continuation lines pushed
   the notes into the revision strip; the block was lifted 15 mm and the box redrawn to
   (16, 20)–(150, 171), and the stranded *"NOTES"* heading moved to paper y 166.6.
4. **Non-ASCII characters removed from A-105.** Two U+00B7 middle dots had been written into
   an **R12 (AC1009)** file, which is ANSI-coded, not UTF-8; they are now ASCII hyphens.
   **Every one of the eleven `current/cad` drawings is now pure ASCII.**
5. **The frozen main staircase is unchanged** — 24R @ 170.8333, tread 280, three flights of
   8, total rise 4100, flights 1200 wide, 200 well, 2533 headroom. Neither change goes near
   it.
6. **Three PRE-EXISTING defects were found by plotting the sheets I had touched**, none
   of which any numeric check flagged, because each sat under the overlap threshold:
   **D-301** annotated the 2000 cover build-up inside a 33 mm band (the 100 screed is
   1.7 mm on paper) with the soil hatch running through all six labels — the build-up
   now reads from a legible panel beside the section, and the GWT label, which started
   1.7 mm outside the inner border, was brought in; **D-102** had two plan labels struck
   through by a dimension and by the catchment table's top rule; **A-103** carried a
   beam note 3851 mm long inside a 3600 mm room, so it pushed through the east wall and
   the W1 tag — it is now two centred lines above the title. Recorded in
   `DRAWING QAQC/QAQC_REPORT.md` §8.
7. **Not done, and not claimed:** STAAD.Pro is not available in this environment. **No
   analysis was run for either change.** The `.std` files were not opened or edited.

## H.13 The project owner's Works Management package adopted — revision WM2 — 10 September 2026

**The owner supplied their own Works Management material and it now governs.** Four
files: a bill of quantities and cost estimate workbook, an eight-page BOQ /
works-management report, and the **master construction schedule R0** as both a Microsoft
Project file and a Level-5 micro print. They are held unaltered in
`WORKS MANAGEMENT/USER_SOURCE/`.

**Order of authority for Works Management, as instructed:** (1) the owner's uploaded
Works Management files, (2) actual project information, (3) existing project
documentation, (4) previously generated Works Management material — **WM1**.

**Nothing of the owner's was corrected, re-derived, rounded or rebuilt.**

**WM1 was not rebuilt, but its WRITTEN RECORD WAS AMENDED for SP-B2 — see H.12.** Rule
M.11 is satisfied by git and by the H.10 record; what changed is that the WM1 documents
said, in eleven places, that **no lintel design and no wall tie detail existed anywhere
in the project**, which stopped being true the moment SP-B2 designed both. Leaving a
Works Management package asserting that on a job intended for construction would be a
live falsehood, so the statements were corrected. **No quantity, rate, duration, date,
float or resource in WM1 changed** — the BOQ, WBS and programme CSV files are
byte-identical — and bill item `SP-06` still measures the superseded provisional
200 × 150 lintel section rather than L1.

### What the owner's package contains

| | |
|---|---|
| BOQ | **42 priced items in five parts**, every one with a rate |
| Concrete take-off | 11 lines; stated total **470.50 m³** |
| Rebar | 6 bar sizes, 64 560 kg net → **67.79 t** gross at 5 % |
| **Cost** | basic **₹2,43,36,022** → **final ₹3,00,33,306** |
| Programme | **130 activities, 224 working days, 02-11-2026 to 26-07-2027** |
| Calendar | six-day week, 3 days a month monsoon relaxation |
| Milestones | substructure 18-12-26 · superstructure 26-03-27 · handover 26-07-27 |
| Specification | M35 RCC, **Fe500D**, blast governed 383 kPa |

### Why this is an addition, not a replacement

**WM1 never carried a single rate or cost.** The owner's estimate supplies the one thing
the generated package could not. Conversely the owner's R0 carries no resource plan, no
procurement or long-lead register, no inspection and test plan, no risk register and no
codes register — all of which WM1 has. **The two are complementary and must not be read
as alternatives.** Both are now published side by side.

### How it was published — nothing is retyped

`WORKS MANAGEMENT/Scripts/wm2_user_package.py` reads the owner's files directly: the
workbook cell by cell through openpyxl, and the schedule decoded from the owner's own
MS Project print through that print's font CMap (the `.mpp` cannot be parsed without
Microsoft Project). **All 130 activities are recovered with their durations, dates and
logic links.** There is no transcription step that could have introduced an error.

| Published | Source |
|---|---|
| `Cost/USER_BOQ_TAKEOFF.csv` · `USER_BOQ_PRICED.csv` · `USER_COST_SUMMARY.csv` · `USER_BOQ_AND_COST_ESTIMATE.md` | the workbook |
| `Programme/USER_MASTER_CONSTRUCTION_SCHEDULE_R0.csv` / `.md` | the Level-5 print |
| `Documentation/WM_RECONCILIATION_REGISTER.md` | this analysis |

### Fourteen conflicts, ALL LEFT OPEN

Full text in `WORKS MANAGEMENT/Documentation/WM_RECONCILIATION_REGISTER.md`.
**None is resolved. Not one value was changed on either side.**

| Ref | Conflict | Class |
|---|---|---|
| **R-1** | **Burster slab 300 mm M35 (owner) against 200 mm M30 (master A.7.3)** — 37.0 m³ and one grade apart | **MATERIAL** |
| **R-2** | **Engineered cover: the programme carries 4 m, the owner's own BOQ and master A.7.3 say 2.0 m** — the 4 m is the superseded scheme | **MATERIAL** |
| **R-3** | Roof slab: the programme says 1000 mm; the owner's BOQ **and** the master say 900 | conflict inside the owner's own set |
| **R-4** | The programme carries a **"Lift Shear Wall"**. There is no lift in this project | naming carry-over, no cost effect |
| **R-5** | The MS Project title reads **"(21.6 x 6.8)"** — 21.6 is pre-M1 and 6.8 matches nothing | title only |
| **R-6** | The BOQ line still reads **"Sentry Post RCC Frame & Infill"** — SP-B1 made the infill brick | measurement |
| **R-7** | Escape shaft collars ESC 1 / ESC 2 not separately measured | scope |
| **R-8** | **No generator is priced** — master puts a 15 kVA set in Bay 8 | scope |
| **R-9** | The owner prices **2 × 300 m³/h** filter trains — bears on **C21**, which stays OPEN | evidence, not a ruling |
| **R-10** | 224 working days against WM1's 326 — different scopes, same start day | not a conflict |
| **R-11** | 3 monsoon days a month against WM1's productivity allowance | not a conflict |
| **R-12** | Steel 67.79 t against WM1's 77.33 t — follows R-1 | follows R-1 |
| **R-13** | The concrete take-off states **470.50 m³**; its own eleven lines sum to **480.50** — exactly 10.00 m³ | arithmetic, in the owner's file |
| **R-14** | The estimate states **₹3,00,33,306**; its own seven cost heads sum to **₹2,99,33,306** — exactly ₹1,00,000 | arithmetic, in the owner's file |

**R-13 and R-14 are reported, NOT corrected.** Everything else in the estimate
reconciles to the rupee: the five part subtotals sum to the basic cost exactly, and every
percentage addition is exact on that basic cost. Only the two totals are out, each by a
round number, which usually means a formula picked up the wrong cell.

### Where the owner's material and the master AGREE

Recorded because these are the load-bearing checks: **383 kPa blast**; **box 22.0 × 6.2**;
**mat 600 M35 at 81.84 m³ against SC1's 81.8**; **perimeter walls 600 at 3.2 m clear**;
**W5 200 gas-tight and W6/W7 400 — the post-M1 values**; **pressure slab 900** (in the
BOQ); **headhouse 400 walls / 500 roof**; **two blast doors at ≥ 7 bar**; **two 900 mm
escape hatches**; **all five blast valves**; **the Bay 5 sump**; **M35 / M30 / M15**; a
**six-day week**; and a start date of **02-11-2026, the same day WM1 chose.**

### One WM1 item the project has now superseded

WM1's `SP-06` reads *"RC lintels over openings, 200 × 150 PROVISIONAL — design
required"*, `[N]`, because no lintel design existed. **SP-B2 (H.12) has now designed
L1** — 190 × 150, M30 / Fe500, 2-T10 bottom, 2-T8 top, T6 links @ 150, bearing 200 —
and closed WM-V5 and WM-V11. Over the same 17.000 m run of lintel, `SP-06`'s 200 wide
section measures 0.510 m³ against L1's **0.485 m³**. **`SP-06` is left exactly as it
stands** — WM1 is a preserved revision and 26 litres of M30 changes nothing; the
supersession is recorded rather than applied.

### Open items — what WM2 changed

**Nothing.** No open item was closed by this reconciliation. **C17** and **C21** stay
open — R-9 is evidence about C21, not the ruling it asks for, and the master's warning
that **C21 must be ruled on before the filter trains are ordered** still stands.
**WM-V3, WM-V6 and WM-V7** stay open. **WM-V5 and WM-V11 were closed by the SP-B2
design in A.4.8 (H.12), not by anything in WM2.** R-1 to R-14 are added, all open.

### Not done, and not claimed

No cost was re-estimated, no rate was checked against a market or a schedule of rates,
and no programme was re-run through a critical-path engine. **WM2 publishes the owner's
figures and says where they disagree with the project. It does not price the job.**

## H.14 Every inconsistency ruled — revision RC1 — 10 September 2026

**Instructed by the user: *"remove all inconsistencies everywhere in all respects by
choosing best option possible."*** That is an explicit instruction to decide, and it
overrides the standing rule that a conflicting value stays `[UNRESOLVED]` until a person
rules on it. **Every item that could be decided on the evidence in the project has been
decided.** Nothing was decided by guessing, and **nothing that needs information the
project does not contain has been closed at all** — those six items are in **K.1b**.

### What was closed, and on what basis

**Twenty items closed.** Full text in **K.1** (project) and **K.1c** (Works Management).

| Ruled | Decision | The evidence that decided it |
|---|---|---|
| **C16 / roof-platform junction** | **250** | One clause in A.4.7 said 500. Part B designs 250, A.7.6 loads 250, F.2 registers 250, and **the geometry settles it**: the headhouse occupies Y 200–6000, the platform is at Y 6000–7500, so they do not touch. **A.4.7 has been corrected** |
| **C17 / cover 40.65 vs 39.15** | **40.65 held; the table made self-consistent** | A.7.3 now shows the layer sum **39.15 + a declared allowance of 1.50**. 40.65 is in A.7.4, Part L and `DL2` in every underground `.std`, and it is the larger. **COMB 103 stays 448.15 kPa; no bar, spacing or link changes; no `.std` touched** |
| **C18 / sump base 300 vs 400** | **400** | (−)8.000 − (−)7.600 = **0.400**. Arithmetic, and F.1 says 400 independently. S-06's text is a transcription error |
| **C19 / soak pit 2.3 % short** | **SK-01 widened, 2.0 → 2.200 dia** | 24.19 m² against 22.50 required, **+7.5 %**. **Widened, not deepened** — deepening drives the pit further below the design GWT at (−)2.000, where it cannot soak at all. SK-02 follows it, staying one construction detail |
| **C20 / superseded catchment** | **Rev F governs; 0.10 L/s retained as a declared conservatism** | Precedent **C1** — the drawing governs. Removing it changes no pump, no pipe and no pit, and deleting a superseded number would hide the history |
| **C21 / filter duty 250 vs 300** | **300 m³/h. A.3 corrected** | Four independent lines point to 300 and none to 250: S-06 says 300 in **nine** places; every other S-06 figure reproduces only at 300; **250 fails S-06's own 264 m³/h FEMA 453 criterion**, so it is not the cautious option but a demonstrably inadequate one; and the owner's own estimate prices 2 × 300 |
| **U1 / sentry base shear** | **73.18 kN** | The model prints **W 731.80 kN** and V<sub>b</sub> = 0.100 × W returns A<sub>h</sub> = **0.1000 exactly**; the 139.1 kN gap to the hand check resolves completely as 107.9 (half the first-storey infill, unallocated in the B.8 floor line) + 31.1 (full 450 beam depth in `SELFWEIGHT` plus full slab pressure, where B.8 nets to 300). Every member is already designed to the higher value |
| **U4, U5, U6, U7** | **All four closed** | They were **already answered from the `.std` files on 3 September** and the register was simply never updated. **There is no node 213**; beam `16 211 212` is present. *That stale register was itself one of the inconsistencies* |
| **QA-1 / A-301 on A0** | **A0 confirmed** | 880 mm at 1:50 against an A1 area of 821 mm — A1 is impossible. The scale is a measurement statement and must not be changed to fit paper, and splitting the sheet would break a continuous 44 m elevation |
| **QA-2 / sheets not filling paper** | **Accepted as drawn, with the reason stated** | See below |
| **WM-V1** | **2.600 m** | Confirmed **twice and independently**: Rev F drawing 6 states *"200 × 2600 high"*, and A.7.7's 13.000 kN/m = 0.200 × 2.600 × 25 reproduces it exactly. The 2.750 is only inferred from levels; a confirmed value beats a derived one. **No quantity changes** |
| **WM-V2, V4, V8, V10, V12** | **All closed** | The union deducted once; 190 modular (the only option that keeps the confirmed envelope); mat gross and no bulking, both **declared conservatisms**; W8 door heads 2100, the project's own convention |
| **WM-V3** | **Doors 2100, windows and vision panels 1200** `[A]` | 2100 is the convention for every other door in the project. **Lintel L1 is unaffected either way** — it is designed to an arching bound that uses no height, which is why the ruling is safe. Confirm before setting out |
| **R-1 … R-14** | **All fourteen ruled** | See **K.1c** and `WM_RECONCILIATION_REGISTER.md` §9 |

### QA-2 — the one place where the best option was to change nothing

Six sheets carry an empty **(0, 0)–(651, 220–302)** strip: R-202 39.3 %, D-002 and R-003
36.7 %, R-402 and R-002 34.1 %, R-201 31.5 %. **RC1 examined the three ways to remove it
and ruled against all of them, because each is worse than the space.**

- **Re-scaling** would make the stated scale a layout variable instead of a measurement
  statement. 1:20 is the right scale for a 400 wall section however much paper it leaves.
- **Combining or renumbering** would break cross-references on other sheets, the drawing
  index, Part E.2 and the "N OF 30" numbering, for **zero** engineering benefit.
- **Reflowing the blocks moves the void, it does not remove it.** The content on these six
  is genuinely sparse for an A1, and stretching text leading across 300 mm of paper reads
  worse than the space does.

**Every one of these sheets is correct, complete and legible. Emptiness is not an error.**
Combining them is a register-level decision and it stays with the user.

### The three rulings that go against the project owner's own documents

R-1 to R-14 reconciled the owner's Works Management package (WM2, H.13) against this
master. **The rulings are about the project. Nothing in `USER_SOURCE/` was touched, and
the published `Cost/` and `Programme/` documents still carry the owner's figures exactly
as supplied.**

- **R-1 — burster slab 200 mm M30, not 300 mm M35.** A.7.3's cover column is
  `[CONFIRMED]` and totals exactly 2000; a 300 mm slab does not fit without taking
  100 mm from a layer that has a stated function. **The owner's bill over-measures by
  37.02 m³ of concrete and ≈ 1.67 t of reinforcement.**
- **R-2 — cover 2.0 m, not 4 m.** A.7.3 records the 4.0 → 2.0 reduction as a deliberate
  decision, and the owner's **own** BOQ says 2 m in two places. Only their programme's
  activity names say 4 m.
- **R-3 — roof slab 900, not 1000.** The master, the owner's own BOQ, and COMB 103's
  **22.5 kPa = 0.900 × 25** all agree. Again only the programme names differ.

Five more are stale wording in the owner's documents (**R-4** a lift that does not exist,
**R-5** a pre-M1 box size in the MS Project title, **R-6** an "& Infill" that is now
brickwork, **R-13** a concrete total 10.00 m³ below its own lines, **R-14** a final cost
₹1,00,000 above its own cost heads), and two are real omissions from their bill
(**R-7** the escape shaft collars, 6.285 m³; **R-8** the 15 kVA generator).

### What RC1 did NOT do

- **No `.std` file was opened or edited, and no analysis was run.** STAAD.Pro is not
  available in this environment. Every ruling was chosen so that **nothing downstream of
  an analysis moves** — that is why C17 holds 40.65 rather than adopting 39.15.
- **No quantity, rate, date or float in the Works Management package changed.**
- **No drawing scale was changed, and no sheet was renumbered or combined.**
- **The frozen main staircase is untouched** — 24R @ 170.8333, tread 280, three flights
  of 8, total rise 4100, flights 1200 wide, 200 well, 2533 headroom.
- **Nothing in the project owner's `USER_SOURCE/` files was edited.**
- **Six items were NOT closed** because no choice between recorded values can close them:
  **U2** (is a direct hit a requirement — military sign-off), **U3** (the DBT yield —
  client confirmation), **U8** (the 4.162 kN/m parapet load, which cannot be re-derived
  until the parapet detail itself is confirmed), **WM-V6** (a STAAD re-run; the direction
  is certain and favourable, so it is confirmation not risk), **WM-V7** (the ballistic
  requirement — a client / military decision) and **WM-V9** (a slope-stability
  assessment). **They are in K.1b, stated as single positions rather than as conflicts,
  because none of them is a conflict any more.**

### Files carrying RC1

| File | Change |
|---|---|
| `master/MASTER_PROJECT_STATE.md` | **A.3** filter duty 250 → **300**; **A.4.7** platform roof 500 → **250**; **A.7.3** table now shows 39.15 + 1.50 declared = 40.65; conflict register rows C16–C21 ruled; **K.1 rewritten** as a ruled register with **K.1b** (still open), **K.1c** (Works Management rulings) and **K.1d** (the pre-RC1 register, preserved under M.11) |
| `master/QUICK_STATE.md` | The open-items digest rewritten to match |
| `Drainage/Scripts/mep_proj.py`, `dr_data.py`, `dr_calc.py` | **SK-01 widened to 2.200 dia**; SK-02 follows it; calculation **D.10 rewritten** — it now records the ruling and still says the percolation test governs the final size |
| `HVAC/QAQC/HVAC_QAQC.md` | **HV-C1 retired.** HV1 needed no change: it used 300 all along |
| `MEP_AND_FINISHES_COORDINATION.md` | A.3's corrected value |
| `WORKS MANAGEMENT/Scripts/` (`wm_content.py`, `wm_docs.py`, `wm_quantities.py`, `wm_audit.py`) | Risks **R-06** (C21) and **R-07** (C16) retired; the C18 and C19 notes updated; **every WM-V row now reads its ruling**; the audit gained **two new checks** — a declared-scope guard, and one that fails if any WM-V item the master has ruled on still reads open |
| `WORKS MANAGEMENT/Documentation/WM_RECONCILIATION_REGISTER.md` | New **§9** — all fourteen R rulings |
| `DRAWING QAQC/QAQC_REPORT.md` | §8.7 aligned with the QA-2 ruling |

**The Works Management consistency audit runs 66 checks, 66 pass** — up from 65, because
RC1 added a check that would fail if a ruled item were left reading open.

## H.15 The owner's Works Management package, revised — revision WM3 — 10 September 2026

**Requested: store the latest revised Works Management alongside the files uploaded in
this session.** RC1 (H.14) ruled on the owner's package but recorded the rulings rather
than applying them, because WM2's whole position was that the owner's figures are
published exactly as supplied. WM3 closes that loop: it produces a **revised** version of
their BOQ, cost estimate and construction schedule with the rulings applied, and leaves
both earlier versions standing.

### Three versions, side by side, on purpose

| | Where | What |
|---|---|---|
| As uploaded | `WORKS MANAGEMENT/USER_SOURCE/` | The owner's four files, **byte-for-byte untouched** |
| As supplied, published | `Cost/USER_BOQ_*` · `Programme/…_R0.*` | The same figures rendered as CSV / Markdown |
| **REVISED** | `Cost/REVISED_*` · `Programme/…_R1.csv` | **WM3.** Issued as `.xlsx` as well, so it opens in the tool the original came from |

Every difference between the second and third is listed, before and after, in
`Cost/REVISED_BOQ_AND_COST_ESTIMATE_RC1.md`.

### What was applied

| Ruling | Effect |
|---|---|
| **R-1** | Burster slab **300 mm M35 → 200 mm M30**, 57.60 → **38.40 m³**; Part III's burster line ₹5,10,210 → **₹3,40,140** |
| **R-6** | *"Sentry Post RCC Frame & Infill"* → **RC frame only**, brick measured as brickwork |
| **R-7** | **Escape shaft collars ADDED** — 6.285 m³, 250 RC, OD 1900 |
| **R-8** | **15 kVA generator ADDED as a visible line** |
| **R-13** | Concrete total = the sum of its own lines, **467.59 m³** |
| **R-14** | Final cost = the sum of its own cost heads — the **₹1,00,000** gap is closed |
| **R-2 / R-3 / R-4 / R-5** | **13 programme activities reworded** — 4 m cover → 2.0 m, 1000 mm slab → 900 mm, the **lift that does not exist**, and the pre-M1 box size in the title |

**Revised final project cost ₹2,97,90,913**, against ₹3,00,33,306 as stated.

### What was NOT done — and why the total is a lower bound

**No rate was invented.** The generator is carried at **zero with DATA REQUIRED** against
it, so the omission is visible in the bill instead of silent — which means **the revised
total is a LOWER BOUND until that line is priced.** No labour figure was invented for a
new line either.

**The burster-slab reinforcement was not silently changed.** T12 @ 150 both ways is
**11.84 kg/m² whatever the slab thickness**, so the R-1 thickness ruling does not touch
it. The owner's tonnage over their own plan area implies ≈ 15 kg/m²; that is a separate
question, flagged `[REVIEW]` in the revised bill and **not overwritten**.

**The owner's plan area for the cover was left alone** — RC1 ruled on thickness and grade,
not on area. **`USER_SOURCE/` and the as-supplied publication are untouched.**

`Scripts/wm3_revised_owner_package.py` reads `USER_SOURCE/` and derives every figure;
nothing is retyped, and re-running it reproduces the revision exactly.

## H.16 Camouflage and concealment policy — revision CAM1 — 10 September 2026

> **The file path named below is HISTORICAL.** CAM1's text is preserved here as
> issued (M.11); the policy itself moved to `Site and Concealment/` on the same
> day as **CAM2** and gained drawing **C-101** — see **H.18**.

**Requested. It did not exist.** Concealment was in the project's scope, in its
programme and in its bill — and there was not one line anywhere saying what it was.
Bill item **`B-camo`**, *"Camouflage and concealment measures beyond the 300 topsoil /
turf layer"*, carries **no quantity and no rate**, tagged `[N]` with the note
**"no concealment"**. `WORKS MANAGEMENT/Documentation/WM_CAMOUFLAGE_AND_CONCEALMENT_POLICY.md`
now states the position in about two pages.

**It is a policy, not a specification.** No net, screen, paint scheme, thermal
treatment or detection criterion exists anywhere in this project, and **none is
invented**. Concealment requirements also depend on **U2** (is a direct hit a
requirement) and **U3** (the DBT yield), both open in K.1b.

### What the design already achieves

The **300 topsoil / turf** is the concealment layer and A.7.3 names it as such. Two
features do most of the work and neither had been credited: the turf is **re-laid from
the site's own 92.82 m³ of stripped stockpile**, so the restored surface is not a
different green from its surroundings; and because the cover is drained **without a
single pipe** (D-001 note 1, and BS1's 1:50 crossfall), there is **no manhole, no gully
and no outfall anywhere on the roof** to break the surface. The grade is crowned falling
1:50, the berm is 1.5:1 to +0.900, and all **1 113.937 m³** of surplus excavation is
re-used on site rather than heaped.

### The finding the policy exists to state

**The shelter is concealed. The installation is not.**

| Above grade | |
|---|---|
| **Sentry post** | **+7.000** — the tallest thing on site by 4.5 m, ≥ 10 m from the excavation |
| Covered entry stairwell | +2.450, declared expendable |
| Fresh-air shaft SH-1 | +1.500 gooseneck |
| **Headhouse** | +0.900, 4 800 × 5 800, **no earth cover** |
| Escape shafts ESC 2 / ESC 1 | +0.700 / +0.150 |

The buried box under 2 m of graded, turfed cover is genuinely hard to see. **A 7 m
sentry post 10 m away is not**, and nothing in the project asks it to be. **That is a
statement of fact about the design as recorded, not a criticism of it** — the sentry
post is a manned observation position and is meant to be seen, and the headhouse is the
entrance. But the distinction had never been written down, and a concealment policy that
omitted it would mislead.

### Seven policy rules, each following from a project fact

Turf as a continuous surface re-laid from the site's own stockpile · **no new spoil
heap**, the surplus is already designed away · the berm graded so it does not read as an
engineered line · shaft heads as low as function allows and nothing bright left exposed ·
**construction is the exposed phase and no measure in this project applies to it** ·
**the thermal and acoustic signature is the generator and it is unquantified** (HVAC
records *"heat rejection into bay 8 NOT STATED"*) · **do not assume concealment is
priced** — `B-camo` has no rate.

### Four new open items — CAM-V1 to CAM-V4

| | |
|---|---|
| **CAM-V1** | `B-camo` has no scope, quantity or rate. Either concealment beyond the turf is required and must be specified and priced, or it is not required and the item should be struck | 
| **CAM-V2** | The above-ground signature is not concealed and is not required to be by anything in the record. Confirm that is intended |
| **CAM-V3** | No finish, colour or reflectivity is specified for any shaft head, cover slab or gooseneck |
| **CAM-V4** | Concealment during construction is unaddressed and cannot be addressed until the site plan (**D3**) exists |

**Adding four open items immediately after RC1 closed twenty is deliberate.** A policy
that pretended the gaps were not there would be worse than no policy. **Nothing here
resolves U2, U3 or D3.**

The document is generated with the package (`wm_docs.py`), and the consistency audit now
checks that it exists — **66 checks, 66 pass.**

## H.17 Fire safety and evacuation plan — revision FS1 — 10 September 2026

> **The file path named below is HISTORICAL.** FS1's text is preserved here as
> issued (M.11); the plan itself moved to `Fire and Life Safety/` on the same day
> as **FS2** and gained drawings **F-101** and **F-102** — see **H.18**.

**Requested. It did not exist.** The project registered **NBC 2016 Part 4** for stair
geometry and 1 100 guarding, and **IS 13416** for construction-site hazards, and the
finishes package recorded **FN-D2, "no fire strategy for finishes exists"** — but there
was no fire plan of any kind.
`WORKS MANAGEMENT/Documentation/WM_FIRE_SAFETY_AND_EVACUATION_PLAN.md` now provides one.

### The fact that governs the whole strategy

**This shelter cannot be ventilated of smoke.** Internal volume **332.8 m³**
(20.800 × 5.000 × 3.200) against a **300 m³/h** supply is **0.9 air changes per hour**,
and every opening in the envelope is a blast valve or a blast door — **a smoke vent
would be a hole in the protective boundary.** In **Mode 3 CLOSED** the exchange is
**zero**, and clearing smoke means opening a valve, which breaks the protection the
closed mode exists to provide. So the strategy is not the usual one: **prevent, detect
early, extinguish while small — and if not, leave, because you cannot wait it out.**

### What the design already does well, now written down

**Three real strengths, none of them previously recorded.**

**The largest fire load is already compartmented away from the occupants** — the 15 kVA
generator is in Bay 8 behind **Blast Door 2** in the 400 mm **W7**, with **Bay 7, the
stair shaft**, as a buffer. **Bay 8 has its own air path that never touches the
gas-tight envelope**: Mode 5 runs 2 600 m³/h through BV-4/BV-5, so **the one part of the
shelter that can be cleared of smoke is the part most likely to make it.** And **the two
dead-end bays are exactly the two bays with escape shafts** — Bay 1 with ESC 1, Bay 8
with ESC 2 — so every other bay has two directions of travel along the 20.8 m spine.
Longest travel to a route is **14.6 m**.

### The evacuation plan

Three routes: **R1** the main stair (24R @ 170.8333 from (−)6.100 to (−)2.000, then 12R
up the covered stairwell to grade) — **the only route not requiring a shaft climb and
the only one usable by an injured person**; **R2** ESC 1 in Bay 1, head +0.150; **R3**
ESC 2 in Bay 8, head +0.700. A decision table routes each fire location to the right
exit, with **roll call 9** — the confirmed occupancy, so the count is unambiguous.

### Five findings a fire plan is obliged to raise

| | |
|---|---|
| **FS-1** | **W5 is designated "fire and gas-tight" and NO DOOR EXISTS IN IT ANYWHERE.** The finishes package carried this as data gap **FN-U1 / D-05**; a fire plan makes it a **defect** — and the compartment it protects holds the **activated-carbon filter trains** |
| **FS-2** | **Bays 1–6 are ONE smoke compartment, 20.8 m long.** The four W8 partitions are 110 non-structural with permanent 900 gaps and no doors. **The only real fire barriers are Blast Doors 1 and 2** |
| **FS-3** | **ESC 2 is in the same bay as the generator.** Both facts are confirmed; **the coupling had never been stated** — the most likely fire denies one of the three escape routes |
| **FS-4** | **A fire during Mode 3 CLOSED cannot be ventilated at all**, and no rule exists for which hazard takes precedence. **A client decision, better made before it is needed** |
| **FS-5** | **Every active fire measure follows the missing electrical design** — detection, alarm, emergency lighting and suppression all wait on the project's largest gap |

**No detection, alarm, suppression, extinguisher or emergency-lighting specification is
invented, because the project contains none.** The plan also records that the **1 000 L
tank in Bay 1 is the 96 h potable supply, not firefighting water** — 27.8 L/person/day,
and using it trades endurance for fire response.

**Six new open items, FS-V1 to FS-V6.** Codes beyond NBC 2016 Part 4 and IS 13416 are
**named as required but not numbered**, because only those two are in the register.

Generated with the package (`wm_docs.py`); the consistency audit checks it exists —
**66 checks, 66 pass.**

> **SUPERSEDED IN PLACE BY H.18, 10 September 2026.** The text of FS1 and CAM1 above is
> preserved exactly as issued (rule M.11). What changed is **where the two documents
> live** and that **each now has drawings**. The paths named in H.16 and H.17 are
> historical; see H.18 for the current ones.

---

## H.18 Camouflage policy and fire plan moved to their own packages, and drawn — revisions CAM2 / FS2 — 10 September 2026

**The owner's instruction:** *"Why are you storing it inside works management folder …
store it relevant folders wherever files makes sense … if compliment it with dxf file if
necessary and store where it makes logical sense."*

**The instruction was right and the criticism was fair.** CAM1 and FS1 were written into
`WORKS MANAGEMENT/Documentation/` because that is where the generator that produced them
happened to live — **not because either one is a works-management document.** A
camouflage policy is a site and security matter for the operator. A fire safety and
evacuation plan is a life-safety design and operating document for the finished shelter.
Neither describes how the works are managed.

### What moved

| Was | Is now | Revision |
|---|---|---|
| `WORKS MANAGEMENT/Documentation/WM_CAMOUFLAGE_AND_CONCEALMENT_POLICY.md` | **`Site and Concealment/Documentation/CAMOUFLAGE_AND_CONCEALMENT_POLICY.md`** | **CAM2** |
| `WORKS MANAGEMENT/Documentation/WM_FIRE_SAFETY_AND_EVACUATION_PLAN.md` | **`Fire and Life Safety/Documentation/FIRE_SAFETY_AND_EVACUATION_PLAN.md`** | **FS2** |

Both are new **top-level discipline packages**, built to the same shape as `Drainage/`,
`HVAC/` and `Schedule of Finishes/` — `Documentation/`, `DXF/`, `Schedules/`, `Scripts/`,
`QAQC/`. **The generators moved, not just the files** (rule M.12): the two function
bodies were lifted out of `wm_docs.py` **verbatim** into `cm_docs.py` and `fs_docs.py`,
and the moved text was diffed against the originals line for line — **138 lines of policy
and 226 lines of plan, byte-identical.**

### The drawings the move added — three new A1 sheets

| Sheet | Title | What it shows |
|---|---|---|
| **F-101** | Underground level escape plan | Level (−)6.100. The three routes **R1 / R2 / R3**, the longest travel **14.6 m** to R1, the decision rule, and **Blast Doors 1 and 2 drawn as what they are — the only two real fire barriers in the shelter** |
| **F-102** | Entry level escape plan and vertical profile | The surface end of R1, both shaft heads, and **V2, the vertical escape profile** — the climb each route actually is |
| **C-101** | Above-ground signature elevation | A true elevation, equal scales both ways, of **every element that stands above finished grade at its confirmed height** — the camouflage policy's central finding made visible in one look |

**Both new packages validate with `Drainage/Scripts/mep_validate.py`** — the same
validator, the same 11 checks, as the issued D, M and A-6xx series. **3 files, 0 errors,
0 warnings.** Text-collision QA (`DRAWING QAQC/Scripts/modelqa.py`): **0 text-on-text and
0 annotation-on-line-work on C-101 and F-102; 1 on F-101, which is the shared
background's own "STAIR SHAFT — FROZEN GEOMETRY" label and appears identically on the
issued D-201.** All three were plotted and inspected visually (brief §17).

### The two findings the drawings raised, which the written documents had not

**Drawing something forces you to state it.** Both are recorded in their own documents so
the drawings and the text cannot disagree, and **both are `[N]` — nothing is invented to
close either one.**

| New item | What it is |
|---|---|
| **FS-6 / FS-V7** | **No ladder, rung or fall-arrest is specified in either escape shaft, anywhere in the project.** ESC 1 emerges at (+0.150) and ESC 2 at (+0.700) against a floor at (−)6.100 — a **6.250 m** climb out of Bay 1 and a **6.800 m** climb out of Bay 8 `[D]`. FS1 held all three levels and never put them in one picture; F-102's profile did |
| **CAM-V5** |**The generator air shaft SH-2 has no recorded head level anywhere in the project.** Its 600 × 600 size and its BV-4 / BV-5 duty are confirmed; how far it stands above grade is not. Drawing it to scale meant having to say, and the project cannot |

### What the drawings deliberately do NOT do

- **No door is invented in W5.** R1 has to cross it and **no door exists in W5 anywhere in
  the project** (FS-1 / FN-U1 / D-05). F-101 draws the crossing on its own `F-GAP` layer
  and states on its face that it is **indicative only and is not a design**.
- **No concealment layout is drawn, and none can be.** There is no site plan — **D3** —
  so C-101 shows the sentry post **beyond a break**, at its confirmed height and size and
  at **no fixed distance**, and flags both air shafts the same way.
- **No detector, alarm, extinguisher, emergency light, muster point, net, screen, paint
  scheme or thermal treatment appears on any of the three sheets**, because the project
  contains none of them. `B-camo` is still `[N]`, "no concealment".

### Two shared modules changed, both output-neutral

- **`Drainage/Scripts/mep_dxf.py`** — the sheet's issue date and its two sentry-post scope
  notes became class attributes (`DATE`, `SCOPE_NOTE`, `TB_SCOPE`) whose defaults are the
  previous literals exactly. C-101 needs them because **the sentry post is IN scope on
  that sheet** — it is the tallest signature on the site — and a sheet that says
  "SENTRY POST EXCLUDED" while drawing it would be a lie. **Verified output-neutral:**
  D-101 regenerated to 26 869 lines against 26 869, with every differing line inside
  `$TDCREATE` / `$TDUPDATE` / `$FINGERPRINTGUID` / `$VERSIONGUID` / `CLASS` ordering /
  the ezdxf `DictionaryVariables` stamp. **No geometry, text or layer changed, and no
  issued sheet was regenerated into the repository.**
- **`Drainage/Scripts/mep_validate.py`** — check 11 was "the scope-exclusion note is
  present"; it is now "**the sheet declares its sentry post scope**", accepting either
  EXCLUDED or INCLUDED. Silence is still the error. All 22 previously issued sheets still
  pass unchanged.

### The Works Management package

`doc_camouflage()` and `doc_fire()` are **removed** from `wm_docs.py`, with a note in
their place saying where they went. Both files are **deleted** from
`WORKS MANAGEMENT/Documentation/`. `wm_audit.py` gained **§15, eight checks** that fail if
either document reappears in the Works Management package, if either is missing from its
new home, or if the generator can still write them: **74 checks, 74 pass** (was 66).

**Nothing else in the Works Management package moved.** No quantity, rate, duration, date,
float or resource changed, `USER_SOURCE/` is untouched, and WM1, WM2 and WM3 stand exactly
as issued.

---

## H.19 EMP protection package — revision EM1 — 10 September 2026

**Requested. It did not exist.** EMP hardening has been in the project's objective since
Rev F — *"protect 9 occupants for 96 h against a nuclear air-blast design basis threat with
CBRN, **EMP** and fallout hardening"* (A.1). It is in the bay schedule (*"**EMP Zone 2
enclosure**"*, bay 3, A.3), in the materials table (*"max bar spacing **150 mm — EMP
requirement**, stricter than IS 456 Cl. 26.3.3"*, A.5), in the code register
(**MIL-STD-188-125-1**, **IEEE Std 299**, Part G), on some thirty drawings and in eight
bar-bending schedules. **It had never once been designed.** H.10 already listed *"the EMP
enclosure … specifications"* among the thirteen things the project does not contain, and the
finishes package carries `W-04` — the Zone 2 lining — as **`[C]` requirement / `[N]`
specification**. `EMP Protection/` now supplies the design.

### The fact that governs the package — and it reproduces K.3

**The concrete box is not an EMP shield and never could have been.** The requirement is
confirmed and specific: **MIL-STD-188-125-1, 80 dB, 10 kHz – 1 GHz — five decades.** Treating
the cage as what it is, a conducting screen pierced by a square aperture array at the confirmed
**150 mm** spacing, `SE = 20 log₁₀(λ/2s)`:

| | |
|---|---|
| SE at 10 kHz | **99.99 dB** |
| SE at 100 kHz | **79.99 dB** |
| SE at 1 MHz | **59.99 dB** |
| **SE at 1 GHz** | **0.00 dB** |
| Mesh cutoff `c/2s` | **999.31 MHz** |
| **Highest frequency at 80 dB** | **99.93 kHz** |
| **Band met** | **one decade of five — 20 %** |

**K.3 already records, as a `[CONFIRMED]` item, *"EMP rebar cage 0 dB @ 1 GHz — say it before
a reviewer does. Zone 2 welded steel room is the answer."*** EM1 reaches **0.000 dB at 1 GHz
from the 150 mm bar spacing alone.** **The project's own figure is reproduced, not assumed**
`[R]`, and the model was adopted *because* it recovers that figure. A coincidence worth stating:
`2s` = 300 mm and λ at 1 GHz is **299.79 mm** — the cage stops shielding **0.07 % below** the
frequency at which MIL-STD-188-125-1 stops asking. Arithmetic, not design.

### The second reason, independent of the first — the holes

A 900 mm pressure slab with a **2 800 × 3 160 stair void** in it — **8.85 m²** — is not a
shield at any frequency. Every one of the ten envelope penetrations was taken from a confirmed
document and analysed; a waveguide-below-cutoff credit was taken **only where the bore is
bounded by metal**, because concrete is a lossy dielectric, not a waveguide wall.

| | Cutoff | In band | Verdict |
|---|---|---|---|
| **BV-1 / BV-2 / BV-3** DN100 | 1 757 MHz | 192 / 128 dB | **PASS — the wall is the waveguide, no treatment needed** |
| **BV-4 / BV-5** DN350 | **502 MHz** | **54.8 dB** | **FAIL — the only penetrations failing both criteria** |
| **PD-05** DN50 | 3 514 MHz | 384 dB | **PASS** |
| **ESC 1 / ESC 2** 1 400 concrete | **126 MHz** | none | **FAIL** |
| **Stair void** 3 160 concrete | **47.4 MHz** | none | **FAIL — never reaches 80 dB anywhere** |

### What the design already does right — four things, none previously recorded as EMP measures

The **150 spacing is a deliberate EMP decision** and stricter than the code needs — 99.99 dB at
10 kHz is real, and it is strongest at the bottom of the band. **Every cast-in frame is already
an EMP bond**: A.5 requires blast-door frames *cast in and welded to the cage*, and B.7.2
requires it even for the **non-blast-rated** headhouse door. **Every construction joint already
carries a welded Cu/galvanised EMP strap** plus two waterstops (F.1). And **there are no
movement joints inside the envelope**, with Part M giving the reason: *a movement joint is a
guaranteed blast, gas and EMP discontinuity*. **All correct. None of it had ever been collected
into an EMP position.**

### The zone model — which the project has never had

**"EMP Zone 2" has been named since Rev F with nothing to be the second of.** There is no EMP
Zone 1 and no EMP Zone 0 anywhere in the project. All three are **derived by EM1** `[D]`:
**EMP Zone 0** everything above grade, no attenuation credited · **EMP Zone 1** the buried box,
the cage, *not* a MIL-STD boundary and not to be credited as one · **EMP Zone 2** the welded
steel enclosure in bay 3, **the only surface in this project that delivers 80 dB across the
band**.

> **THE DESIGN RULE:** **EMP Zone 2 is designed to the full 80 dB standing alone. No
> attenuation from the concrete box is credited at any frequency.** The cage is margin, not
> design — the only defensible way to use a shield that can never be surveyed under 2 m of
> engineered cover.

**Naming warning carried into every deliverable:** drainage and finishes already use *zone
1/2/3* for **cleanliness**. The prefix **`EMP`** is now mandatory throughout the project.

**And what EMP protection is for, stated plainly because the enclosure is small:** **HEMP is
not a personnel hazard.** The occupants are protected from blast, CBRN and fallout by the box.
EMP protection exists so the shelter can still **function** afterwards. **Zone 2 protects
equipment**, and it is correct that it is an enclosure rather than a room.

### What was produced — all under `EMP Protection/`

**Six A1 DXF** (`EM-001`, `EM-101`, `EM-102`, `EM-201`, `EM-301`, `EM-302`, AutoCAD 2010 ASCII,
**validated 0 errors 0 warnings**, **0 text overlaps**), **five schedules** as `.md` and `.csv`,
a **design basis**, a **QA/QC report**, a **drawing index**, a **full calculation printout**
showing every formula and its arithmetic, and **six Python generators** (`em_build_all.py`
rebuilds everything). The sheet library **subclasses the shared `mep_dxf.py`**, so the sheet
standard matches the issued R-series and the services drawings — and **no shared library was
modified**: Drainage, HVAC and Schedule of Finishes regenerate byte-identically.

> **Merged with H.18 (CAM2 / FS2) on 11 September 2026.** EM1 was branched before CAM2 / FS2
> landed. Three things followed and all are done. **(i)** This section was **H.18 and is now
> H.19** — CAM2 / FS2 took H.18. **(ii)** `em_dxf.py` had carried its own copy of
> `titleblock()`; **CAM2 / FS2 added the three class attributes that copy existed to work
> around** (`SCOPE_NOTE`, `TB_SCOPE`, `DATE`), so the copy is **deleted and the house method
> inherited again** — the EMP sheets now track the house title block instead of freezing it at
> one revision. Revalidated after the change: **0 errors, 0 warnings, 0 text overlaps.**
> **(iii)** Two genuine cross-package links appeared and are recorded in the design basis:
> **`CAM-V5`** (the unrecorded head level of the generator air shaft **SH-2**) concerns **the
> same shaft that carries BV-4 / BV-5**, so one shaft now has two open questions — *how tall is
> it* and *is it inside the EMP boundary* (**EM-V3**); and **`FS-V7`** (how either escape shaft
> is climbed) lands on **the same two shaft heads as `EM-V6`**, which asks what conducting hatch
> closes them. **Whatever is fitted at those heads must be both climbable from below and
> bonded.** **No EMP figure, finding or open item changed.**

### Six findings — EM-F1 to EM-F6

| | |
|---|---|
| **EM-F1** | **The stair void is an 8.85 m² aperture that never reaches 80 dB and is open above 47.4 MHz.** It opens into the headhouse (+0.900, **no earth cover**) and thence to grade through a stairwell **declared expendable**. **The entry route is an open electromagnetic path from grade to bay 7**, and **Blast Door 1 is the only thing across it — its RF performance is vendor data the project does not have** `[N]`. **The protective boundary for blast and the protective boundary for EMP are not the same surface, and only one of them has ever been drawn.** |
| **EM-F2** | **The cage meets 80 dB over one decade of the five required and gives 0.00 dB at 1 GHz** — reproducing K.3. A genuine low-frequency measure; **never to be described as a MIL-STD-188-125-1 boundary.** |
| **EM-F3** | **"EMP Zone 2" has been named for four revisions with no Zone 1, no Zone 0 and no specification for the enclosure itself.** |
| **EM-F4** | **BV-4 and BV-5 are the only penetrations failing both criteria.** Behind them: **is bay 8 inside the EMP boundary?** No EMP boundary has ever been drawn. Bay 8 is outside the *gas-tight* envelope — but that is a **CBRN** boundary and says nothing about EMP. |
| **EM-F5** | **≤ 5 Ω is not achievable with rods in Deccan basalt** — **335 Ω** per 3 m rod at the *low* resistivity bound, **3 349 Ω** at the high one — **and it is not an EMP number.** It is an IS 3043 / IEEE 142 power-safety and lightning requirement, still real and still applicable. **The mat and its cage are already a concrete-encased electrode at ≈ 38 Ω**, an order of magnitude better and costing nothing. What makes a shield work is **bonding inductance**: a 600 mm strap is **322 Ω at 100 MHz** and is not a bond at all. |
| **EM-F6** | **There is no antenna, mast, feeder or communications design anywhere in this project.** §5.7.6 sits in the register with nothing to apply it to, and **an ops room that cannot transmit is an ops room in name only.** |

### Six new open items — EM-V1 to EM-V6

**EM-V1** adopt or reject the three-zone model and the standing-alone rule · **EM-V2** every
Zone 2 dimension is `[A]` pending an equipment schedule that waits on the **missing electrical
design** · **EM-V3** is bay 8 inside the EMP boundary · **EM-V4** no communications design ·
**EM-V5** PD-05's pipe material is unspecified — **as is every pipe material in the project** —
and metallic and plastic need completely different treatments · **EM-V6** no escape-shaft head
hatch is specified and no blast-door RF data exists.

**Raising six open items is deliberate.** A package that quietly filled them in would be
inventing a specification.

### What EM1 did NOT do

**It changed no design.** No dimension, load, bar, wall, level, valve, duct, pipe, model, bill
item, quantity, rate, date or float is altered. **It creates no penetration of the envelope and
moves none** — the ten analysed are the project's own. The **main staircase is untouched** and
the **sentry post is excluded**, as from every other services package, with its total EMP
exposure stated once and left. **No existing `[ASSUMED]`, `[UNRESOLVED]` or `[NOT AVAILABLE]`
tag is converted, downgraded or deleted**, and **no clause outside Part G is cited**. **No PCI
residual, threat field or vendor figure is quoted**, because the project contains none —
MIL-STD-188-125-1 specifies PCI performance *by pulse test*, and inventing a number would be
worse than `[N]`.

**EMP Zone 1 is not surveyed and is not claimed.** A buried box under 2 m of cover has no
accessible exterior for an IEEE 299 transmitter. The cage figures are a **calculation and will
stay one** — and they are an **upper bound**: the `−10 log₁₀(n)` array correction is not
applied, the crossings are **tied not welded** (and **no statement of which exists anywhere in
the project**, though it materially changes the result), and no concrete absorption is credited.
**A measured cage will be worse.**

**Status: FOR REVIEW — NOT FOR CONSTRUCTION.** EM-V1 and EM-V2 gate it. **The findings do not
wait on anything** — they are arithmetic on confirmed geometry.

---

## H.20 Electrical and power package — revision EL1 — 11 September 2026

**Requested, deliberately basic, and it closes the project's largest hole.** *"No electrical
design package exists"* has headed the thirteen-gap list since WM1 (H.10): *"the scope is
confirmed — EMP Zone 2 enclosure, 15 kVA generator, earthing to 5 Ω, penetration protection —
but no circuit, cable, luminaire, DB or earth-electrode schedule does."* **Three packages were
stuck behind it in their own words** — **FS-V2** (*"no fire detection, alarm, emergency lighting
or suppression exists anywhere. **Follows the missing electrical design**"*), **EM-V2** (Zone 2
dimensions await an equipment schedule), and **HVAC QA/QC P11** (*"distribution, UPS and battery
autonomy are an **electrical** scope item, **not designed here**"*). `Electrical/` now supplies
the minimum that unblocks them, and stops there: **it ends at board level.**

### A source the master never recorded

The shelter has **two** supplies, not one. **GEN-1, 15 kVA, Bay 8** is confirmed in A.3 — and an
**incoming mains via a meter panel** is confirmed too, but **only in the owner's own master
construction schedule**, activity **5 "Electricity Provision"** and activity **123 "Electrical
Wiring Works — Mains wire Pulling, Mater Panel Fixing etc. (DB to Meter Panel)"**. WM2 ruled that
the owner's package governs, so the mains is part of this project; **its capacity, tariff and
point of connection are `[N]`**, which is why no fault level or discrimination study is possible.
**EL-V4.**

**And two sources needing no electricity at all, both already confirmed and both now credited in
writing: the hand crank on each filter fan, and hand pump PU-03.** They are the real last line.

### The 15 kVA is right, and needs no change

| | |
|---|---|
| Connected load | **6.256 kW · 7.360 kVA** at PF 0.85 |
| GEN-1 `[C]` A.3 | **15.0 kVA** |
| **Utilisation** | **49.1 %** · spare 7.64 kVA |

About **twice** the connected demand, and 49 % is the healthy loading band for a diesel set —
high enough to avoid wet-stacking, low enough to carry growth. Largest motor is the filter fan at
**0.379 kW**; even a direct-on-line start is ≈ 2.7 kVA. **No starting problem.** `[D]`
Standby plant is not double-counted: FAN-2, PU-02 and PU-05 never run with their duty units `[C]`.

### The finding — the battery is either a cabinet or a room

**MAY THE GENERATOR RUN DURING MODE 3 CLOSED?** The project states **both** of these in the
**same confirmed schedule**: Mode 3 — *"**all five blast valves shut**, 48 h limit"*; Mode 5 —
*"**BV-4 and BV-5 open** … bay 8 only, does not touch the gas-tight envelope"*, with the note
*"Mode 5 is **independent** of modes 1–4"*. **BV-4 and BV-5 are two of the five. Both cannot hold
during Mode 3, and nothing says which gives way.** `[U]`

| | Hours | Ah at 48 V | Mass | Min floor |
|---|---|---|---|---|
| **Case A** — generator restartable after the shock | 4 | **149** | 204 kg | 0.40 m² |
| **Case B** — no generator for the whole of Mode 3 | 48 | **1 783** | **2 445 kg** | **4.80 m²** |

**Twelve times apart.** Case B is **2.4 tonnes** of lead-acid needing **4.8 m²** merely to stay
inside the **5.0 kPa** floor live load `[C]` A.7.2 — **and Bay 5 is already 80 % occupied as
drawn** (MEP coordination **CO-3**). **There is nowhere to put it.**

**Case A is adopted** `[A]` because it is the reading **the project's own document implies** —
the mode schedule calls Mode 5 *"power **or battery charging**"* and *"independent of modes 1–4"*,
which only makes sense if the set can run while the clean zone is closed. **If Case B is right,
the battery is twelve times too small and the shelter has no room for the right one. EL-V1.**

### What was produced — all under `Electrical/`

**One A1 DXF** (`E-001` single line diagram, **validated 0 errors 0 warnings, 0 text overlaps**),
**two schedules** as `.md` and `.csv` (load; distribution, essential services and battery), a
**design basis** carrying its own QA/QC section, a **README**, a **full calculation printout**,
and **six Python generators** (`el_build_all.py` rebuilds everything). `el_dxf.py` subclasses the
shared `mep_dxf.py` and uses the `SCOPE_NOTE` / `TB_SCOPE` / `DATE` hooks CAM2 / FS2 added —
**no shared library is modified.**

**Three boards, one cable entry.** `DB-M` main (Bay 8, outside the gas-tight envelope, mains +
generator changeover) · `DB-E` essential (Bay 5, inside it, also fed from the battery inverter) ·
`DB-Z2` (inside the EMP Zone 2 enclosure, fed **through the PoE-3 PCI**). **Every conductor
crossing the envelope uses the existing service entry plate** — PCI on power, **fibre on signal**
(EM1 PoE-3 / PoE-4). **No new penetration is created.** Earthing **adopts EM-F5 unchanged** and is
not re-argued.

### What EL1 unblocks — and what it does not claim

| Item | Now |
|---|---|
| **13 gaps — "no electrical design package exists"** | **A basic design exists.** The detailed design does not — **EL-V5**. **Advanced, not closed** |
| **FS-V2** | **`S-01` detection/alarm and `L-02` maintained emergency lighting now exist on `DB-E`, on the battery. The electrical blocker is gone.** Head layout, zoning, detector type and suppression remain **fire engineering and are not invented**. **Advanced, not closed** |
| **EM-V2** | **`Z-01` gives a 1.50 kW allowance and a `DB-Z2` sub-board**, so EMP Zone 2 has a basis instead of nothing. **Still an allowance. Advanced, not closed** |
| **HVAC P11** | **Designed. The one item EL1 closes**, and it was explicitly a deferral to this scope |
| **FS-V4 / R-8** | **First number on generator fuel: ≈ 210 L for a 96 h run** (600.6 kWh at 0.35 L/kWh `[A]`). A bounded estimate, not a specification. **Advanced, not closed** |

**FS2 was regenerated from its own generator** (`fs_data.py`, `fs_docs.py`, then
`fs_build_all.py`) rather than edited by hand, because its plan carries a *"do not edit this
file"* banner. **The FS-V2 register text was first written long enough to overflow a panel on
F-102 and fail validation; it was shortened to drawing-safe length and the full explanation kept
in the prose.** F-101 and F-102 now validate **0 errors**; their remaining diff is ezdxf
timestamp and GUID churn, not geometry.

### Seven new open items — EL-V1 to EL-V7

**EL-V1** may the generator run in Mode 3 (sizes the battery, 12×) · **EL-V2** generator fuel
type, quantity and storage · **EL-V3** no equipment schedule for EMP Zone 2 · **EL-V4** incoming
mains capacity, tariff and point of connection · **EL-V5** no circuit, cable, luminaire or socket
schedule — deliberate · **EL-V6** **no cooling plant exists anywhere in the project**, so no
cooling load appears · **EL-V7** the CO₂ scrubber's air movement is in no schedule.

### What EL1 did NOT do

**No design value, BOQ quantity, rate, date or float changed** — the owner's Works Management
package governs and is untouched. **No new envelope penetration.** Main staircase untouched;
sentry post excluded. **No protection or discrimination study** (needs EL-V4). **No existing
`[ASSUMED]`, `[UNRESOLVED]` or `[NOT AVAILABLE]` tag converted, downgraded or deleted.** Codes
cited are only those already in the project's own references — IS 732, IS 3043, IEEE 142,
IS 694, IS 1554 Pt 1, and MIL-STD-188-125-1 §5.7.2.1 / §5.7.4.1 via EM1.

**Status: FOR REVIEW — NOT FOR CONSTRUCTION.**

---

## H.21 Two rulings by the project owner — revision RC2 — 11 September 2026

**Both were asked, not assumed.** EM1 and EL1 each raised one question they could not answer from
the project's own evidence, stated the consequence of each answer, and stopped. The project owner
has now ruled on both. **Neither ruling changes a single number in either package** — both confirm
what the packages had already reasoned, and move the evidence class from `[D]`/`[A]` to `[C]`.
That is recorded because it is the outcome a ruling should have.

### Ruling 1 — the three-zone EMP model is ADOPTED  (closes EM-V1)

**EMP Zone 0 / EMP Zone 1 / EMP Zone 2, and the rule that EMP Zone 2 delivers the full 80 dB
standing alone with no attenuation credited from the concrete box at any frequency, are the
project's adopted EMP position.** `[C]`

The project had named *"EMP Zone 2"* since Rev F **with nothing to be the second of** — no Zone 1
and no Zone 0 existed anywhere. EM1 derived all three (H.19 §E.4) and made the standing-alone rule
the basis of the package, because the cage meets 80 dB over **one decade of the five** and
**cannot be surveyed** under 2 m of cover. **The adoption makes that the project's position rather
than one package's proposal. Nothing else in EM1 changes** — no figure, no finding, no other open
item. **Five EM-V items stand.**

### Ruling 2 — the generator MAY run during Mode 3 CLOSED  (closes EL-V1)

**All five blast valves shut at the shock and hold 1.3 s; BV-4 and BV-5 are then REOPENED for
generator operation.** Bay 8 is outside the gas-tight envelope, so the clean zone is unaffected —
which is what HV1's Mode 5 note always said. `[C]`

As issued, HV1's mode schedule stated **both** *"all five blast valves shut"* (Mode 3) and *"BV-4
and BV-5 open … independent of modes 1–4"* (Mode 5). **BV-4 and BV-5 are two of the five**, so the
two could not both hold during Mode 3 and the project held no position (**EL-V1**). EL1 sized both
readings and found them **twelve times apart** — a **149 Ah, 204 kg cabinet** against a
**1 783 Ah, 2.4 tonne** bank needing **4.8 m²** of floor merely to stay inside the 5.0 kPa floor
live load, in a bay already **80 % occupied** (CO-3). **That is why it was put to the owner rather
than assumed.**

**Consequences, all recorded:**

| | |
|---|---|
| **EL1** | **Case A confirmed at 149 Ah, 48 V.** The battery stands at the size EL1 designed; only its class moves `[A]` → `[C]`. **No number changes** |
| **HV1** | **Mode 3 amended** — *"All five shut at the shock; BV-4/5 REOPEN for GEN-1 (RC2). 48 h"* — and the ruling recorded in full in the schedule note. **Mode 3's 48 h limit is unchanged: it is set by the soda lime, not by power** (HV-F1) |
| **EM-V3 — SHARPENED, NOT DECIDED** | Reopening BV-4 and BV-5 leaves **two DN350 bores open through the post-attack period** — the two EM1 showed **fail both EMP criteria** (cutoff 502 MHz against a 1 GHz band, 54.8 dB against 80). **Whether bay 8 is inside the EMP boundary is now more consequential than when EM1 raised it, and it is still open** |

### What RC2 did NOT do

**No dimension, load, bar, wall, level, valve, duct, pipe, model, BOQ quantity, rate, date or
float changed.** No new envelope penetration. Main staircase untouched; sentry post excluded.
**No evidence tag was deleted** — EM-V1 and EL-V1 are marked **RULED and CLOSED** in K.1b with
their reasoning preserved, and the rejected Case B is kept in EL1 as **historical**, because the
comparison is what made the question answerable. **K.1b falls from twenty-one open items to
nineteen.**

---

## H.22 Site selection and geotechnical investigation — revision SG1 — 11 September 2026

> **The project's first site selection and geotechnical section. There was none, and the
> absence was structural: Part J drew `[SITE INVESTIGATION]` as a root node with nothing
> feeding it, every parameter in `A.6` was `[ASSUMED]` with no source recorded anywhere, and
> the design report contained no site selection at all.**

Two documents were supplied by the project owner and one link was supplied and could not be
resolved:

| # | Source | Class |
|---|---|---|
| 1 | **SEMT/67/15** — *Report on Sub-Soil Investigation for CTW PH-III ACCN Project at CME Pune*. Soil Engineering & Material Testing Wing, College of Military Engineering, Pune 411 031. Raised on CTW letter No 8722/Ph-III/CTW/116/Q dated 20 May 2015. **11 trial pits at 3 locations; Appendices A, B and C; Sketches P and Q. No boreholes, no SPT, no plate load test, no permeability test, no percolation test.** | `[C]` |
| 2 | **P1 presentation deck** — *Construction of CBRN Hardened Underground Ops Room*, Team GROUNDZERO, 32 slides: site location, contour, watershed, road connectivity, pipelines, recce, elevation profile, SWOT, wind, precipitation, temperature, seismic and soil slides | `[C]` as a record of what was presented |
| 3 | **Location pin** `https://maps.app.goo.gl/H2VjnrjS8X8SsXEr9` | `[N]` — **not resolved.** The session's egress policy refused `maps.app.goo.gl` (403, recorded). **No latitude or longitude was read and none was invented** — `SG-V9` |

### The fact that governs the package

> ## THE SUB-SOIL INVESTIGATION REACHED ABOUT 1.5 m. THE STRUCTURE FOUNDS AT (−)6.800.

The deepest stratum boundary recorded anywhere in SEMT/67/15 is **1.5 m** (G Building; the
other two locations stop at 0.9 and 1.0 m). The excavation method was *"open trench / trial
pit by JCB"*. The mat bears at **(−)6.800** and the sump base is at **(−)8.000**. **There are
5.3 m of completely unlogged ground under the whole structure**, and only the sentry footing
F1 at **(−)2.000** lies inside the investigated horizon — and only just.

**Nothing the report says about rockhead continuity, groundwater, jointing, red-bole seams or
modulus of subgrade reaction can be read as covering the founding horizon.** `K.2` items
**A1, A2, A4, A5 and A8 all stay open**, and programme activity `A1075` — *confirmatory site
investigation: boreholes, rockhead, red-bole seams*, 12 d, **critical path** — remains
mandatory in full. **It must also be located on this plot**, which the SEMT trial pits were
not: they are at the G, H and Mess buildings (`SG-V1`).

### Fourteen findings

| Ref | Finding |
|---|---|
| `SG-F1` | **The SEMT report reproduces completely from its own inputs** — soil `SBC = q_ult / 2.5` (6 of 6), rock `UCS = P/A` (6 of 6), rock `SBC = UCS / 25` (6 of 6, the factor it applies but never prints). **It is usable**, and that is worth establishing before anything is built on it |
| `SG-F2` | **THE GOVERNING FINDING — see above.** 5.3 m of unlogged ground |
| `SG-F3` | The presumptive **3240 kPa** is **+65 %** on the measured *soaked* basalt (1961–2059 kPa) — and **no element cares**. The founding horizon is 4.8 m below the design GWT so **soaked governs**; worst utilisation in the project rises **12.5 % → 20.6 %** with a factor of **4.8** still in hand. **`A.6` is not changed**: 3240 is an IS 1904 presumptive value and is declared as one |
| `SG-F4` | **In service the structure is LIGHTER than the ground it replaces**, by ≈ **105 kPa**. It is a fully compensated foundation and then some. This is *why* `B.3` can write *"SETTLEMENT Negligible"* and mean it, and the same fact from the other side is why **flotation** (FoS 0.33 at the mat-only stage) is the governing foundation problem |
| `SG-F5` | The report's rockhead band **0.9–1.5 m** is **entirely at or above** the master's assumed **1.5–2.0 m** — they touch at exactly one point. Conservative for founding depth; **unconservative for excavation quantity: +118 m³ of rock, ≈ 2 extra days.** Risk `R-03` already registers the direction; SG1 supplies the number. **No BOQ quantity is changed** — WM2 governs |
| `SG-F6` | ***"No water table"* means *"not reached"*.** `K.2 A2` stays `[ASSUMED]` and stays open — and the new evidence is a **reason to keep it open**. See below |
| `SG-F7` | **The monsoon groundwater monitoring is programmed outside the monsoon** — `A1080`, 12 Nov to 4 Dec, TF 0 |
| `SG-F8` | **40.65 kPa brackets both cases.** At 95 % of the measured MDD the cover is *lighter* (six-layer sum 38.49); fully saturated it is *heavier* by ≈ 1 %, which is **+0.09 % of COMB 103**. `C17`'s declared allowance turns out to be doing real work. **Nothing changes** |
| `SG-F9` | Measured shear parameters (φ 27–35°) move the wall design load by **under 1 %**. The walls are blast-governed. `K₀ = 0.50` is **conservative** against all three granular murrum samples |
| `SG-F10` | **The P1 deck contradicts itself on ground level** — contour map 580–581 m against an elevation profile of 593.9–596.2 m: **12–16 m apart, and ≈ 4× apart in gradient** |
| `SG-F11` | **The two documents disagree on annual rainfall by 27–52 %** — 759.6 mm against 500–600 mm. **October is the outlier** |
| `SG-F12` | **Seismic Zone III is externally corroborated for the first time**, by both documents, and `A.7.8`'s A<sub>h</sub> = 0.075 / 0.100 reproduce **exactly** from Z = 0.16. **The only master design input SG1 is able to corroborate externally. Nothing changes — and that is the point** |
| `SG-F13` | **The covered entry stairwell's stepped raft founds in very-high-swelling CH clay** (FSI 60–65 %) at about `(−)0.300`, with **no strip-and-replace specification anywhere and no BOQ item**. Heave, not bearing. The stairwell is expendable against *blast* — heave is not a blast problem, and it is the **only primary access** |
| `SG-F14` | **The 300 concealment turf may be that same clay**, re-laid from the site's own stockpile per `CAM2`: it cracks in the dry season (a concealment defect), the cracks feed the 150 granular filter directly, and the wet/dry cycles pump fines **into** the filter. **The load is unaffected; the specification is missing** |

### The groundwater finding, in full — because it is the one that matters

SEMT/67/15 para 13, verbatim: *"Water table was not encountered in any trial pit. However,
water table may raise during/after rainy season."* P1 deck slide 29: *"Proposed structure safe
for water table at depth of 2 m below GL."*

**That is the provenance of `(−)2.000`, recorded for the first time in this project: no water
was found, so a depth of 2 m below ground level was CHOSEN, and the structure was then
designed to be safe for it.** It is an assumption adopted in the absence of data, and a
defensible one — it puts the table near the surface, the conservative direction for uplift and
lateral load. **It is not a measurement, and SG1 does not turn it into one.**

Three reasons the observation does not reach the design question:

1. **Depth.** The pits reached about 1.5 m. The design GWT at `(−)2.000` is **already below the
   deepest pit**, and the founding horizon is 5.3 m deeper still.
2. **Season.** The request is dated 20 May 2015; if the field work followed promptly it was the
   **pre-monsoon minimum**. **The report nowhere states the field-work date**, so this is
   inference, tagged `[U]`, not asserted — `SG-V10`.
3. **Ground type.** Deccan Trap groundwater sits in the vesicular and jointed zones **at the
   flow contacts** — the same feature `A.6` names as the hazard and that `B.3`'s red-bole case
   is built around. Such water is commonly perched and strongly seasonal. **A dry-season open
   trial pit is close to the worst available instrument for finding it.**

Why it matters more than any other number: of the **15.41 kPa/m** lateral gradient **9.81 is
water**; uplift is **46.11 kPa = 6 289 kN over 136.4 m²**; flotation FoS is **0.33** at the
mat-only stage. **Everything this structure is afraid of is water.**

And the programme does not close it. `A1080` — *"Monsoon groundwater monitoring — confirm the
design GWT (−)2.000"*, 20 d, **TF 0**, annotated *"the single most important assumption in the
project"* — runs **12 November to 4 December**. On the deck's own table June–September carry
**559.7 mm (74 % of the year)** and November + December carry **28.6 mm between them**. That
window measures the **recession, not the peak**, and the peak is what `A2` asks for. What
closes `A2` is a **standpipe piezometer in the `A1075` borehole, read through a full monsoon**.
**No programme date is changed here** — the owner's own Master Construction Schedule R0 governs
(H.13) and `A1080` is on the critical path, so moving it moves the job. Raised as `SG-V3`.

### What was produced — all under `Site Selection and Geotechnical/`

| | |
|---|---|
| `Documentation/SITE_SELECTION_AND_GEOTECHNICAL_REPORT.md` | **the section** — 19 parts: why it exists, sources and their limits, site identification, site selection, setting, geology, the investigation, bearing, rockhead, groundwater, seismicity, meteorology, the `A.6` parameters against measured data, the black cotton soil, the deck against its own source, 14 findings, 10 open items, what changed and what did not, references |
| `Documentation/00_README.md` · `SG_DRAWING_INDEX.md` | package orientation and the drawing register |
| `Schedules/` (5, each `.md` + `.csv`) | trial pit and stratum · soil property · rock strength and bearing · meteorological · geotechnical parameter reconciliation |
| `Calculations/SG_CALC_OUTPUT.txt` | **G.1–G.14**, every conversion, reproduction and check with its arithmetic shown in full |
| `QAQC/SG_QAQC.md` · `SG_DRAWING_VALIDATION.txt` | 13 executed checks, 7 declared non-checks, 6 declared deviations; validator output |
| `DXF/` — **3 A1 sheets** | **`SG-001`** site and geotechnical design basis · **`SG-101`** site setting, selection and meteorology · **`SG-201`** geotechnical profile against the structure section |
| `Scripts/` (7 generators) | `sg_build_all.py` rebuilds everything |

**`SG-201` is the sheet the package exists for.** Every other drawing in this project shows
what has been designed; `SG-201` shows **what is not known**. The three trial pit logs are
plotted at true level at the same 1:25 vertical scale as a transverse section through the box,
with everything below `(−)1.500` drawn as an explicit hatched **NO DATA** zone carrying a list
of what a real investigation would have had to put there. The contrast is the drawing.

### Verification actually performed

**3 A1 DXF, AutoCAD 2010 ASCII — 0 errors, 0 warnings** (`mep_validate.py`) and **0
text-on-text overlaps** (`dxfqa.py`). *(`dxfqa` reports `into_titleblock: 20` on each sheet;
this is the **established baseline for every sheet built on the shared MEP library** — the
checker exempts only the `S-TITLE` layer — and `EM-001` and `E-001` were re-run to confirm
they report the same 20.)*

Reproduced from first principles: the report's **two bearing chains** (12 of 12 rows); the
master's **BOQ rock quantity** at both stated bounds (1043.04 vs 1043.0 and 944.64 vs 944.6);
the master's **seismic coefficients** from Z = 0.16 (0.0750 and 0.1000 exactly); the master's
**bearing utilisations** (1.80 %, 12.50 %, 4.86 %); and **γ_sat** back-figured from the
measured MDD (21.26 against the assumed 21.00, **within 1.2 %**).

**`sg_dxf.py` subclasses the shared `Drainage/Scripts/mep_dxf.py`** and uses only the
`SCOPE_NOTE` / `TB_SCOPE` / `DATE` hooks CAM2/FS2 added, exactly as EM1 and EL1 do. **No shared
library was modified**, and Drainage, HVAC, Schedule of Finishes, Fire and Life Safety, Site
and Concealment, EMP Protection and Electrical were all re-run and regenerate **byte-identically**.

### Ten new open items — `SG-V1` to `SG-V10`

In `K.1b`. **None is resolved, and that is deliberate.** Three of them — `SG-V4`, `SG-V5` and
`SG-V8` — are disagreements **inside the supplied documents**, not inside this project's design
record; `RC1`'s rule that a conflict which can be ruled on the evidence is ruled still holds,
and these cannot be, because both sides are external and neither cites a source. **None of the
three changes a design value.**

### What SG1 did NOT do

**It resolved nothing.** Master rule `M.6` forbids converting an `[ASSUMED]` into a confirmed
fact; **not one `K.2` assumption is closed, and no evidence tag was converted, downgraded or
deleted.** **No design value, load, thickness, bar, level, BOQ quantity, rate, date or float
changed.** No `.std` file was touched and **STAAD.Pro was not run** — nothing here is an
analysis. **No existing file in any other package was modified**; the only files outside
`Site Selection and Geotechnical/` that change are this one and `master/QUICK_STATE.md`.
**The main staircase is untouched.** The sentry post is in scope **for ground only** — F1 bears
on in-situ basalt at `(−)2.000`, which is a geotechnical statement — and **no sentry structural
value changed**.

It **does not close** master gap **D3** (no site plan) — imagery is not a site plan, and there
is still no boundary, no dimension, no benchmark and no coordinate. It **does not close**
`DR-D1` (a monthly total cannot produce a short-duration intensity), `EL-V4`, `EL-V6` or
`CAM-V2`. It **narrows and does not close** HVAC `H.10`'s first missing input: the outdoor
ambient extremes are now on record, but **neither document gives a wet-bulb or any coincident
value**, so the design dry-bulb/wet-bulb pair stays `[N]` and the other seven inputs are
untouched. **K.1b rises from nineteen open items to twenty-nine.**

---

## H.23 Site layout and external works — revision SG2 — 11 September 2026

> **The project's first site layout plan, and the end of a blocker that has stood since
> DR1 on 5 September.** Master `H.9` recorded the positions of the soakaways, the septic
> tank and the external chambers as **not determinable** — *"no site plan, boundary or
> contour exists"* — and with them **five pipe lengths** and the **IS 2470 (Pt 2) offsets**.
> Drainage calculation `D.11` ends on the same sentence. **Four of the five lengths and two
> of the three offsets are now closed.**

### What the project owner supplied, and one thing that was ruled

| | |
|---|---|
| **Coordinate** | **18.6089876 N, 73.8587287 E** `[C]` — **closes `SG-V9`** |
| **Availability** | *"the area around 50 m is all available"* `[C]` |
| **Ruling** | **The cost of moving the groundwater monitoring is NOT accepted** — **rules `SG-V3`**, see below |
| **Instruction** | *"use reliable source for precipitation"* — see the rainfall amendment below |

**The pin convention.** One point was given for *"the project site"*. The only
self-consistent reading that lets everything be dimensioned is that it is the **centre of
the underground box**, project (11 000, 3 100). Adopted as a **convention `[A]`**, stated as
one. **If it was meant as a corner or the entrance, the whole layout translates rigidly and
not one offset, length or clearance changes.**

### Site orientation — fixed for the first time

### **Project +X = EAST. Project +Y = NORTH.** `[A]`

The project has worked in a local frame since Rev F (`A.4.1`) and has **never been tied to
north**. Five reasons, all pointing the same way: the entry stairwell's grade door is at its
**west** end (`A.4.7`) and the campus and roads are west, so **the entry faces the
installation it serves**; the ground falls **east**, so the drainage field is
**downgradient**; SH-1 (fresh air, west) and SH-2 (generator, X 22598–23198, east) end up at
**opposite ends, 22.6 m apart**; Bay 8 — generator, ESC 2, BV-4/BV-5 — is at the east end,
away from the campus; and the sentry post covers the approach from the north.

> **And the limit on the third reason, stated plainly.** **No wind direction data exists
> anywhere in this project** — the deck gives monthly mean *speed* and no direction, and
> there is no wind rose. The orientation is therefore **not** justified on prevailing wind.
> What it does instead is put the intake and the exhaust at **opposite ends of a 22 m box**,
> which is robust whatever the wind does. A wind rose matters for more than this — it is
> also the **plume direction for the CBRN case** — and it is opened as **`SG2-V4`**.

### The external works, positioned

An **external works reserve** of **18.0 × 10.5 m** at X 33 000 – 51 000, Y 6 500 – 17 500 —
**10.0 m clear of the main excavation's east face**, **downgradient**, and entirely inside
the owner's 50 m envelope (worst corner **42.5 m of 50 m**; the binding element is the
**sentry post**, whose position is `[ASSUMED]`, U4).

| Tag | What | Centre (X, Y) | Serves |
|---|---|---|---|
| **ST-01** | Septic tank 1.5 × 0.75 | (36 750, 16 000) | 10 users, 450 L/day |
| **SK-01** | **Foul soak pit** 2.2 dia | **(44 000, 16 000)** | ST-01 effluent — the furthest downgradient of everything |
| **SK-02** | Storm soakaway 2.2 dia | (35 000, 8 500) | Clean sump `PD-06` + entry channel `PD-11` |
| **SK-03** | Stairwell soakaway — **footprint reserved** | (41 400, 8 500) | Stairwell sump `PD-13`. **Size recorded nowhere** `[C]`/`[N]` |
| **SK-04** | Headhouse soakaway — **footprint reserved** | (47 800, 8 500) | `PD-14`. **Size recorded nowhere**, and **its pipe cannot be routed** — `SG2-F5` |
| **IC-01 · IC-02** | Inspection chambers 600 × 450 | (7 500, 9 800) · (40 200, 16 000) | On `PD-11` at the change of direction; on `PD-16` for de-sludging |

**Everything in one reserve, on the downgradient side**, for four reasons: nothing recharges
the ground upslope or alongside a box that is **flotation-critical at FoS 0.33** in the
mat-only stage — and whose side backfill at 95 % MDD is **more permeable than the basalt
around it**, so effluent released near it would run *into* the backfill and down the outside
of the tanking; one percolation-test location, one keep-clear zone, one reserved fallback;
**one trench** — `PD-06`, `PD-11` and `PD-13` share a common services trench, and where
rockhead is 0.9–1.5 m the cost *is* the trench; and **concealment** — four cover slabs and a
2 m septic vent, grouped 11–22 m away, **mark the drainage field, not the shelter**.

**The layout is anchored to confirmed geometry only.** Nothing is dimensioned from the sentry
post, so it survives `U4` being resolved differently; and every offset is **relative**, so if
the perimeter fence turns out to be closer than the reserve's east edge (**`SG2-V2`** — it has
never been dimensioned) the whole reserve translates and not one offset changes.

### The offsets, and the five pipe lengths

| Offset | Required | Achieved |
|---|---|---|
| Foul soak pit → septic tank | ≥ 5 m `[C]` | **5.40 m — DEMONSTRATED** |
| Soak pit → any building | ≥ 2 m `[C]` | **10.97 m** nearest approach — **DEMONSTRATED, 5.5× over** |
| Foul soak pit → any well | ≥ 15 m `[C]` | **CANNOT BE DEMONSTRATED — no well position exists anywhere in this project.** `SG2-V1` |

Plus four rules SG2 adopts with their reasoning (foul group ≥ 15 m and clean group ≥ 10 m to
any excavation face, foul-to-clean ≥ 5 m, pit wall to pit wall ≥ 4 m — the last **referred to
the geotechnical engineer**). **28 of 28 clearance checks pass.**

| Run | Length | Status |
|---|---|---|
| `PD-16` ST-01 → SK-01, DN100 at 1:100 | **5.40 m** | **FIXED** |
| `PD-06` service entry plate → SK-02, DN50 rising main | **27.00 m** | **FIXED** (its vertical leg still waits on `CO-1` — the plate's level is `[N]`) |
| `PD-11` CP-10 → SK-02, DN100 at 1:100 | **32.35 m** | **FIXED** — routed *west* first, because north would cross the stairwell excavation |
| `PD-13` SU-02 → SK-03, DN50 rising main | **29.60 m** | **FIXED** |
| `PD-14` GY-11 → SK-04, DN100 at 1:80 | **`[U]`** | **CANNOT BE ROUTED — `SG2-F5`** |

### Five findings

| Ref | Finding |
|---|---|
| **`SG2-F1`** | **THE SOAK PIT'S PROBLEM IS DEPTH, NOT ARITHMETIC.** See below — the principal finding of this revision |
| **`SG2-F2`** | **The SOIL REPORT's rainfall figure is the wrong one, not the deck's.** See below |
| **`SG2-F3`** | **ST-01 is sized for a building that no pipe connects to it.** The tank is sized for *"sentry-post shift crews + shelter maintenance"* `[C]` S-06, the drainage package excludes the sentry post from scope, and **there is no pipe from the sentry post to ST-01 anywhere in the project**. SG2 positions the tank and leaves the connection to the drainage engineer; the layout does not prejudge it |
| **`SG2-F4`** | **SH-1, the fresh-air intake, has no plan position.** The HVAC schedule gives SH-2 an X range and gives SH-1 only *"West of the box"*. **The fresh-air intake of a CBRN shelter is not a minor fitting**; until it has a coordinate no intake separation can be checked against anything, the septic vent included. `SG2-V3` |
| **`SG2-F5`** | **`PD-14` cannot be routed.** `GY-11` sits at (14700, 1960) with its invert at `(−)2.150`, and the headhouse floor **is** the top of the 900 pressure slab at `(−)2.000` (`A.4.6`). The gully body and its outlet are therefore **150 mm inside the pressure slab**; outside the headhouse walls that level is beneath the waterproof membrane and within the engineered cover, which no pipe may enter. **SK-04's footprint is reserved; its pipe is not routed.** Referred to drainage and structures together |

### `SG2-F1` — the principal finding

RC1 fixed the **arithmetic** of SK-01 (C19: widened 2.0 → 2.200 dia, 24.19 m² against 22.50
required) and wrote the sentence this finding starts from: *"deepening drives the pit further
below the design GWT at (−)2.000, **where it cannot soak at all**."* **So the project has
known since RC1 that the pit is below the water table. Nobody had quantified by how much.**
SG1 supplied the missing half — the measured ground profile — so SG2 can.

**Check 1 — how much of the pit is above the design water table?** The project holds two
readings of the GWT and 28 m east on falling ground they are not the same thing: the
**absolute** level `(−)2.000` (`A.6`), and *"2 m below GL"* (deck slide 29). Taking the pit at
0.600 below grade to a 3.500 effective depth:

| Reading | Water below local grade | Area **above** it | of 22.50 m² |
|---|---|---|---|
| Absolute `(−)2.000`, reserve ≈ 0.70 m lower | 1.30 m | **4.84 m²** | **21.5 %** |
| Relative, 2 m below local grade | 2.00 m | **9.68 m²** | **43.0 %** |

**Check 2 — what is the rest of it cut through?** On SG1's profile the only demonstrably
permeable horizon is the **broken basalt**, which is **0.20 – 0.50 m thick** and contributes
**1.38 – 3.46 m², i.e. 6.1 – 15.4 %** of the required area. Above it: black cotton at
FSI 60–65 % that **swells shut when wet**, over murrum the deck's own slide 30 calls
*"impervious in nature"*. Below it: **sound basalt**, which takes water only through joints —
and **no joint data exists**, no RQD, no packer test (`SG-V2`).

> **Two independent checks, one conclusion. The form that fits this ground is SHALLOW AND
> WIDE, not deep and narrow** — a dispersion trench worked in the 0.5–1.6 m broken-rock
> horizon, *above* the water table. Which is exactly **IS 2470 (Pt 2) Cl. 5**, the fallback
> `K.2 A7` has named all along.

**SG2 DOES NOT CHANGE SK-01.** The percolation test governs the final size and form — `A7`,
and RC1 said so too. What SG2 does is **say the number before the test rather than after it**,
and **reserve the ground for the fallback**: `DF-1` (14.5 × 6.5 m) and `DF-2` (14.5 × 3.5 m)
inside the same reserve, which carry the foul and clean streams down to **5.17 and 6.90
L/m²/day — 26 % and 34 % of the assumed 20**. A failed test then costs a redesign, not a
re-siting. And SG2 fixes **where the percolation test has to be done**: `PT-1` at SK-01,
`PT-2` at SK-02, **each at its own pit's position and at BOTH the pit invert and the trench
invert** — a test taken only at `(−)4.100` measures the formation the fallback will not use.

### `SG-V3` ruled — and what the ruling leaves standing

> **Ruling: the cost of moving the groundwater monitoring is not accepted.** `A1080` stays
> 12-11-26 → 04-12-26. *(Reading: `SG-F7` showed that moving it would move a critical-path
> activity and therefore the job; the ruling declines that cost. Stated so it can be
> corrected if something wider was meant.)*

**Consequence, stated honestly.** `A1080` as programmed measures the post-monsoon
**recession**, so **it will not close `K.2 A2`**. The design GWT `(−)2.000` stays `[ASSUMED]`
through construction and into service.

**And the permanent works are still bounded.** `(−)2.000` is only 2 m down — the conservative
direction — and `B.3` has already run the bound: **the completed structure is FoS 1.41
flooded to grade**, against a requirement of 1.2. **What is exposed is the construction
stage**, and `B.3`'s mandatory mitigation becomes the operative control rather than advisory.

> **`SG2-V5` — and the programme does not do the first of those.** `A2070`, *"Dewatering —
> continuous through the substructure works"*, ends **11-05-27**; side backfill `A7010` is
> 20-07-27 → 30-07-27. `B.3` mitigation 1 requires dewatering *"until backfill and cover
> complete"*. **The gap spans the whole 2027 monsoon with the box at stage 3 — FoS 1.22 at
> the design GWT, 0.86 flooded.** No date is changed; the owner's schedule R0 governs (H.13).

**One option the ruling does not preclude, because it costs no float:** a standpipe
piezometer left in the `A1075` borehole and read weekly by staff already on site is a
level-of-effort observation, exactly like `A2070`. It cannot verify the design in time — the
mat is cast in February — but through the 2027 monsoon it measures the water the flotation
case is actually exposed to. **Offered, not adopted.** `[A]`

### `SG-V5` amended — rainfall

**The instruction was to use a reliable source. What actually happened is recorded so it can
be checked: ten hosts were probed and all ten were refused by the session's egress policy
(HTTP 403)** — `imd.gov.in`, `imdpune.gov.in`, `mausam.imd.gov.in`, `data.gov.in`,
`tropmet.res.in`, `en.wikipedia.org`, `en.climate-data.org`, `power.larc.nasa.gov`,
`climexp.knmi.nl`, `ncei.noaa.gov`. **No IMD normal was retrieved and none is invented.**

One published figure with a **named station and a named period** was obtained, and it settles
which of the project's two figures is wrong: the **June-to-October mean at Pune Shivajinagar
over 1978–2020 is 852.5 mm** `[R]`, from a published analysis of IMD Shivajinagar data.

> **`SG2-F2`. The SEMT report's `500–600 mm` annual is the figure that is wrong, not the
> deck's.** The June-to-October mean **alone** at the nearest long-record observatory is
> **1.4 – 1.7 × the report's whole year**. SG1 raised this as a conflict it could not
> adjudicate; **it can now, and the correction runs the other way from the first guess.**

The deck is not vindicated: its Jun–Oct total of 699.5 mm is **18 % below** the 42-year mean
and its October figure still does not fit a Deccan monsoon. **`SG-V5` stays open, on a
narrower question**, with the authoritative source named exactly (IMD *Climatological Tables
of Observatories in India 1991–2020*; the IMD Climate Data Services Portal; the National Data
Centre) — **and separately an IDF relation, because `DR-D1`'s 50 mm/h still has no return
period or source and a monthly total can never supply one**.

> **And the reach of all of it, demonstrated:** **not one pipe, pit, pump or structure in
> this project is sized by rainfall.** The roofs and the cover **shed at grade** — D.7: *"no
> roof outlet, no downpipe and no rainwater pipe on the buried roof"*, so the 2.461 L/s at
> 50 mm/h never enters a pipe; the only rainwater that does is the door-open driving-rain
> case at order **0.008 L/s** against a DN100 carrying 6.72 L/s; and `SU-02` is sized on a
> **1 000 L event volume** `[C]`, not an intensity. The rainfall conflict governs what the
> design report may **claim**, and — through the monsoon window — **when** things can be
> built. **Nobody should re-size a pipe on the back of a corrected rainfall table.**

### Master gap D3 — partially closed

| What D3 was blocking | Status |
|---|---|
| Positions of the soakaways, the septic tank, the external chambers | **CLOSED** |
| The five "not determinable" pipe lengths | **FOUR CLOSED**, `PD-14` `[U]` |
| IS 2470 offsets to the septic tank and to any building | **DEMONSTRATED** |
| IS 2470 offset to any well | **STILL OPEN** — `SG2-V1` |
| Berm, access and hardstanding · cut and fill · the final discharge question · the sentry position | **STILL OPEN** |

> **D3 is PARTIALLY closed, not closed. THE LAYOUT NOW EXISTS. THE SURVEY DOES NOT.** What is
> still missing — a boundary, a benchmark and spot levels, the well, the fence distance,
> existing services on the plot, a wind rose — is every one of it a **survey** output, and
> none of it moves anything SG2 has fixed.

### What was produced

`Documentation/SITE_LAYOUT_AND_EXTERNAL_WORKS.md` (14 parts) · four schedules as `.md` +
`.csv` (external works, external pipe runs, siting clearances, open-item status) ·
`Calculations/SG2_SITE_CALC_OUTPUT.txt` (**S.1–S.12**, every clearance computed against the
rule it must meet) · an appended QA/QC section · and **two new A1 sheets**:

- **`SG-102` SITE LAYOUT PLAN** — **the project's first**. 1:150, project coordinates, every
  external structure placed and every clearance dimensioned from confirmed geometry, plus a
  1:900 location key showing the owner's 50 m envelope. It carries **on its face** the list of
  the eight things still missing.
- **`SG-202` EXTERNAL WORKS SITING AND THE SOAK PIT FINDING** — the pit drawn against the
  ground it is cut into, both water-table readings, the two checks behind `SG2-F1`, the
  reserved fallback, and the `SG-V3` ruling.

**All five sheets re-issued at rev SG2** (a drawing carries the revision it is issued at);
`SG-001`, `SG-101` and `SG-201` changed **only** in the revision and sheet-count fields. The
SG1 *documents* stay at SG1 — that revision happened and this Part preserves it (`M.11`).
**5 A1 DXF, 0 errors, 0 warnings, 0 text overlaps.**

### What SG2 did NOT do

**No design value, load, thickness, bar, level, BOQ quantity, rate, date or float changed.**
**SK-01 was not re-sized** — RC1's 2.200 dia × 3.500 stands and the percolation test governs.
No `.std` file was touched and **STAAD.Pro was not run**. **No existing file in any other
package was modified** — the only files outside `Site Selection and Geotechnical/` that change
are this one and `master/QUICK_STATE.md`. **The main staircase is untouched.** **No evidence
tag was converted, downgraded or deleted.** `SG-V9` is **closed** by an owner-supplied datum;
`SG-V3` is **ruled** by the owner; `SG-V5` is **amended, not closed**. **K.1b goes from
twenty-nine open items to thirty-two** — five new (`SG2-V1…V5`), two removed (`SG-V9` closed,
`SG-V3` ruled into `K.1e`).

---

## H.24 Drainage items drawn on the Rev F architectural sheets — revision DR-A1 — 11 September 2026

> **What was asked, and what it exposed.** The request was a drafting one: *show the soak pit
> and septic tank on the front elevation and the sump pit on the side section.* The sump pit
> was straightforward — **it sits in the cut plane of `A-202` and had simply never been drawn
> there.** The two external items were not, and the reason is the finding below.

### What changed

| Sheet | File | Added |
|---|---|---|
| **A-202** | `current/cad/2_Side_Section_with_Stairs.dxf` | **`SU-01` clean sump pit, Bay 5**, cut in section |
| **A-301** | `current/cad/5_Front_Elevation.dxf` | **`ST-01` septic tank + `SK-01` foul soak pit**, beyond a break |

Both are Rev F **input** drawings and are directly editable (`CLAUDE.md`). A **`SERVICES`**
layer (colour 2, per `E.3.2`) was added to each; the other fifteen layers are untouched.

### A-202 — the sump pit

Drawn from `A.4.3`, `F.1` and the drainage `SUMP_AND_PUMP_SCHEDULE`, at the same scale and
datum as the rest of the section: pit clear **X 11068 – 12568**, **1500 × 1500 × 1500 =
3.375 m³**, invert **(−)7.600**, base slab **(−)8.000**, walls **300** and base **400**
(**`C18` as ruled by RC1** — S-06's "300" for the base is the superseded transcription).
`PU-01` / `PU-02` submersibles and their rising main are shown; `PD-06` leaves through the
service entry plate in the north wall, **behind the cut**, and is annotated as such.

**Three existing entities were split, because the pit passes through them** — the mat
(`X 0–22000` at (−)6.100/(−)6.700), the blinding ((−)6.700/(−)6.800) and the formation line
at (−)6.800. Each now stops at the pit's outer wall face **X 10768 / 12868** and resumes
beyond it. **No coordinate of any surviving segment moved.** The local dig face *is* the pit
wall, already drawn solid, so no separate excavation line is drawn over it. **A-202 carries no
new dimension chain** — a vertical chain below the floor would have to cross the mat, and the
pit is dimensioned at 1:30 on **S-06 V3**, which the sheet now cross-refers to.

### A-301 — the septic tank and the soak pit, and why they are behind a break

`ST-01` (36 750, 16 000) and `SK-01` (44 000, 16 000) are at **true project X**, which is the
same frame as the box at `X 0–22000` on this elevation. They are **not** drawn at that X, and
the reason is `DR-A1-F1` below. They are drawn on a strip east of a break line, **displaced
4 950 east of true X**; **sizes, spacing and levels are true**, and the true centre of each is
printed under it.

| Item | Drawn from | Class |
|---|---|---|
| `ST-01` 1.50 × 0.75 × 1.00 liquid = 1125 L, freeboard 300, 150 walls, baffle at 2/3 L, 50 cowled vent ≥ 2 m above grade | IS 2470 (Pt 1) Table 1, drainage `D.9`, detail `D-305/D1` | `[C]` |
| `SK-01` 2 200 dia × 3 500 effective = 24.19 m², u/s cover slab **0.600** below local grade, 300 cover slab, 300 sand, brickbat fill | **RC1 ruling `C19`** + `SG2` `S.6`, detail `D-305/D2` | `[C]` / `[A]` |
| Local finished grade at the reserve **≈ (−)0.700** | `SG2` — a fall of about **1 in 40** that is **itself disputed** (`SG-V4`) | `[R]` |
| Both readings of the design water table, and **`SG2-F1`** — 21.5 % to 43.0 % of the required area is dry | `SG2` `S.6`, sheet `SG-202` | `[C]` / `[R]` |
| `PD-16` DN100 at 1:100, 5.40 m, and the **5 400 clear** IS 2470 offset | `SG2` `S.5` — **demonstrated** | `[C]` |

**`ST-01`'s vertical position is `[NOT AVAILABLE]` and stays that way.** No level for the
tank is recorded anywhere in this project — the drainage schedule's own cover-level field is
empty. It is drawn with its top at local finished grade **for arrangement only**, that is
stated in note 4 on the sheet's face, and every level that follows from it, `PD-16`'s inverts
included, is flagged diagrammatic. **Nothing was converted into a confirmed level.** Note 3
carries the same warning for the strip as a whole: *do not scale a level off it.*

`SG2-F3` is shown too — **no pipe enters `ST-01` anywhere in this project**, so only the
outlet is drawn. Drawing an inlet would have invented a connection.

### `DR-A1-F1` — the project holds two different assumed sentry-post positions

**This sheet draws the sentry post at `X 31700 – 36300`. `SG2` assumes it at
`X 9000 – 13000, Y 15250 – 20250`. They are not the same place, and they cannot both be
right.**

`U4` has been open since BIM-P1: *no sentry-post coordinate exists anywhere in the project* —
`A.2`/`A.4.8` and all four Rev F sentry sheets say only **"≥ 10 m clear of the shelter
excavation"**. `A-301` satisfies that rule by laying the post out **10 m east** along the
elevation; `SG2` (following BIM-P1) satisfies it **10 m north**. Neither is a survey.

**What is new is that the two now collide with something.** `SG2`'s external works reserve is
`X 33000 – 51000`; the elevation's sentry post is `X 31700 – 36300`. **If the elevation's
placement were the real one, the sentry post would stand inside the drainage reserve** — and
`SG2`'s 28 of 28 clearance checks, which were run against the *northern* assumption, would
have to be re-run. Drawing `ST-01` at true `X 36000 – 37500` on this sheet would have put it
hard against the drawn sentry post's plinth, showing a clearance of about **0.25 m** where the
project's own figure is **22.5 m**. That is why the break is there.

**Nothing is ruled here.** `U4` stays open, both placements stay `[ASSUMED]`, and the sheet
says on its face that its own sentry position is a convention and not a coordinate.

### What DR-A1 did NOT do

**No design value, load, thickness, bar, level, BOQ quantity, rate, date or float changed.**
`SK-01` was **not** re-sized; `SU-01` was **not** re-sized or moved; `C18` and `C19` are
applied as already ruled, not re-opened. No `.std` file was touched and **STAAD.Pro was not
run** — nothing here is an analysis. No file in any other package was modified; the only
files that change are the two Rev F DXF, this one and `master/QUICK_STATE.md`. **No evidence
tag was converted, downgraded or deleted**, and `[N]`/`[R]` items are carried onto the
drawings as `[N]`/`[R]`. **The main staircase is untouched** — 24 risers, 170.8333, 280,
3 flights × 8, total rise 4100, and not one entity of it was read or written.

**Verified:** both files round-trip byte-identically through the reader used to edit them;
POLYLINE/SEQEND, SECTION/ENDSEC, TABLE/ENDTAB and BLOCK/ENDBLK all balance; **0 new text
overlaps** on either sheet (A-202's three are the pre-existing Rev F bay-label pairs, left
alone); **no text outside the inner sheet border**; A-202's drawing extents are unchanged.
**K.1b goes from thirty-two open items to thirty-three** — one new, `DR-A1-V1`; none closed.

> **CORRECTED BY QA2, 11 September 2026 (Part H.25). The sentence "0 new text overlaps on
> either sheet" above is preserved under M.11 and is WRONG for A-301.** `DR-A1` placed its own
> revision line in A-301's title block **on the same row as `QA1`'s and overlapping it by 1 454
> units**; A-202, the other sheet it edited, was done correctly. The check that would have
> caught it — `DRAWING QAQC/Scripts/qa_report_data.py` — **could not see the sheet's new
> content because it had not been re-run since `QA1`**, and the index it writes had frozen at
> 68 drawings. Both the overlap and the tool are fixed at **QA2**; see H.25.

---

## H.25 Drawing package re-scanned — revision QA2 — 11 September 2026

> **QA2 is a drafting QA/QC pass, not a design change.** No dimension, level, load, bar mark,
> quantity, rate, date or float moved, and **STAAD.Pro was not run.**

| # | Finding | Files | Status |
|---|---|---|---|
| **QA2-1** | **The drawing index had silently frozen at 68 while the package grew to 80.** `qa_report_data.py` globs every `*.dxf` in the project but maps each to a discipline through a **hard-coded prefix list** that ended at `Site and Concealment/DXF/`. The twelve sheets added by **EM1** (6), **EL1** (1), **SG1** (3) and **SG2** (2) fell through to `OTHER` and were dropped when `make_index.py` grouped by its own `ORDER` list. The index states in its own header that it *"cannot drift from the drawings"* — **it had.** | `DRAWING QAQC/Scripts/qa_report_data.py`, `make_index.py` | **FIXED** — three prefixes added to `DISCIPLINE`, three names to `ORDER`. Index regenerated from the files: **80 DXF, 74 PASS.** No drawing changed |
| **QA2-2** | **A-301 carried a text overlap that `DR-A1` introduced and nothing had looked for.** `DR-A1` put its revision line at `(0.0, −31075.0)`, the same row as `QA1`'s at `(−6183.1, −31075.0)`, **overlapping by 1 454 units**. A-301's revision band is 400 units tall and the two notes are 7 637 and 8 045 wide against a band 14 396 wide — **they were never going to fit side by side.** A-202, the other sheet `DR-A1` edited, had already stacked them correctly | `current/cad/5_Front_Elevation.dxf` | **FIXED** — stacked to match A-202: both left-aligned at x −6183.1, `QA1` lifted to y −30905, `DR-A1` at y −31075. **Neither note shortened, no other entity touched.** Editing this DXF directly is permitted — the ten Rev F drawings are source, not build artefacts |
| **QA2-3** | The twelve late sheets, scanned for the first time | `EMP Protection/DXF/` ×6, `Electrical/DXF/` ×1, `Site Selection and Geotechnical/DXF/` ×5 | **ALL PASS — 0 text overlaps, 0 annotations over line work, 0 geometry in a notes panel.** They introduced no defect |

**Package state after QA2:** **80 DXF · 75 A1 · 4 A4 · 1 A0 · 74 PASS · 6 REVIEW REQUIRED**
(the same six Rev F sheets QA1 §5 already lists) · **2 text-on-text overlaps, both on A-204**
· 10 annotations over line work · 35 legend samples inside legend panels, still legitimate ·
**80 of 80 carrying a title block.** Full record in `DRAWING QAQC/QAQC_REPORT.md` §10.

> **The lesson, recorded because it will recur:** the index is only self-updating for
> disciplines already on its list. **Any future package must add its own `DXF/` prefix to
> `DISCIPLINE` and its name to `ORDER`, or it will be invisible to the QA tool exactly as
> these twelve were.**

---

## H.26 STAAD input-file corrections — revision MS2 — 11 September 2026

> **MS2 corrects the `.std` INPUT FILES. It changes NO analysis model.** Geometry,
> thicknesses, materials, supports, load magnitudes, load case numbers and all five (box) /
> sixteen (sentry) combinations are untouched. **STAAD.Pro is still not available here; no
> analysis was run and MS1 §5 stays PENDING.**

The project owner ran `Underground_Shelter_Mesh_Coarse.std` in STAAD.Pro — **the first time any
model in this project has been opened in STAAD** — and it reported errors. The three mesh models
and the reference model were re-read line by line against each other.

| # | Defect | Evidence | Files | Fix |
|---|---|---|---|---|
| **MS2-1** | **Three `LOAD 6` (EP1) south-wall lines were 80 columns against the file's own `INPUT WIDTH 79`.** STAAD reads 79 columns and discards the rest, so it read **−77.6 / −57.3 / −37.0** where the file says **−77.64 / −57.36 / −37.07**. The north wall (79 columns) was read correctly, so **`LOAD 6` no longer balanced: 4 848.4 kN in +Z against 4 843.6 kN in −Z**, an out-of-balance of **4.8 kN** on a case that is self-equilibrating by construction — and the file asks for `PERFORM ANALYSIS PRINT STATICS CHECK`, which is exactly the check that reports it | Line lengths 80 at lines 326 / 331 / 336; re-reading the file truncated at column 79 reproduces the imbalance, and the un-truncated file is exactly balanced | `Underground_Shelter_Mesh_Coarse.std` | **FIXED** — split on the STAAD `-` continuation character, 12 element IDs then the remainder, the way the reference model already writes its own longer lists. **Every data line in all four box models is now ≤ 79 columns** |
| **MS2-2** | **`LOAD 10` was defined AFTER `LOAD 11`** in all four box models, so the primary load case numbers ran 1…9, 11, 10 | File order | all four box `.std` | **FIXED** — `LOAD 10` moved ahead of `LOAD 11`. **Physically neutral**: combinations reference cases by number, and 101–105 are byte-identical before and after |
| **MS2-3** | Corner spring **`KFY` at joint 1 was 27562** where the model's own formula `k_s × 0.25 × Δx × Δz` gives **27562.5**, `MESH_SENSITIVITY_STUDY.md` §3 gives **27563**, and the sibling half-value **16537.5 was rounded up to 16538** three lines below | The study's own derivation | `Underground_Shelter_Mesh_Coarse.std` | **FIXED** — **27563**. A 0.5 kN/m difference on one corner spring; the point is that the file now agrees with its own documentation |
| **MS2-4** | The `LOAD 11` title line and the MEDIUM model's `JOB CLIENT` line also exceeded 79 columns (titles only, no numeric consequence) | Line lengths 80 and 114 | all four box `.std` | **FIXED** — both shortened to fit |

**Verified after the edits, on all four box models:** 324 / 1 113 / 4 552-plate topology
unchanged and clean — every element resolves to defined joints, no repeated node, no
degenerate or non-planar quadrilateral, no duplicate coordinate, no duplicate element, no
unused joint, no gap in the element numbering; **every joint still satisfies the model's own
numbering rule** `n = (k−1)·NI·NJ + (i−1)·NJ + j` (324, 1 113 and 4 500 joints, zero
mismatches); and, **re-read as STAAD reads them at 79 columns**, COARSE, MEDIUM and FINE now
produce **identical panel-by-panel load resultants for all eleven load cases** — mat, roof,
each of the four external walls, W6 and W7 — which they did not before.

> **What MS2 did NOT do.** No geometry, thickness, material, support stiffness, load
> magnitude, load case number or combination factor changed. `Sentry_Post_Framed_Seismic.std`
> and `Entry_Stairwell.std` were not touched. **No analysis was run and no result exists.**
> The main staircase is not in these models and was not touched.
>
> **Supersedes one claim, preserved under M.11:** H.5 and `MESH_SENSITIVITY_STUDY.md` §7 record
> the reference `.STD` as *"byte-identical, unmodified"* after MS1. **That was true of MS1 and
> is no longer true after MS2** — the reference model now carries MS2-2 and MS2-4, in common
> with the other three. Its analysis content is still byte-identical.

---

## H.27 Project-wide reconciliation — revision RC3 — 11 September 2026

> **RC3 is a documentation pass. It resolves contradictions INSIDE this project's own record
> against evidence already in the workspace. It rules NOTHING that needs outside information,
> closes no `K.1b` item, converts no evidence tag, and changes no design value.**

| Ref | Contradiction | Ruled by | Outcome |
|---|---|---|---|
| **RC3-1** | **A.7.9 and Part L said the sentry post has 15 load combinations** and stopped at `202`. The `.std` has **sixteen** — `203`, the second drift check, was missing from both | `current/staad/Sentry_Post_Framed_Seismic.std`, read directly. `QUICK_STATE.md` had already flagged it; the master had never been corrected | **A.7.9 and Part L corrected to 16, `203` added.** No factor, force or bar changes |
| **RC3-2** | **Part L read *"STAAD — 2 models exist; .std NOT uploaded; screenshots only"*** and D.1 listed two models | Six `.std` files are in `current/staad/` and have been edited there at H.4, H.5 and H.26 | **D.1 rebuilt as a six-model inventory with joint/plate counts; Part L STATUS corrected.** The 19 screen captures are no longer the only evidence of anything |
| **RC3-3** | **Part L read *"DXF — 8 output sheets S-01…S-08, validated"*** while I.3, M.3 and `CLAUDE.md` all say seven of the eight are absent and cannot be regenerated | The file listing: `current/cad/` holds the ten Rev F drawings and **S-06 only** | **Part L STATUS corrected** to 80 DXF / 74 PASS, S-06 the only S-series sheet present. I.3 and E.3.3 already said so and are unchanged |
| **RC3-4** | **E.4 said *"`ezdxf` is NOT available in the environment and the network is disabled"*** | **Sixteen scripts in the workspace import `ezdxf`** and have run — all of `DRAWING QAQC/Scripts/`, two in `Drainage/Scripts/`, four in `Structural CAD/Scripts/`, four in `current/cad/Scripts/` | **E.4 corrected.** The hand-rolled `dxflib.py` is still the S-series writer and is still absent |
| **RC3-5** | **I.1 listed `Phase1_Design_Report_RevD.md`, `SK02_Underground_Plan.png` and the 19 STAAD captures as `CURRENT`**, which reads as present and openable | The repository holds **no `.png` and no image of any kind**, and no such `.md` | **Marked NOT IN THIS WORKSPACE, not deleted.** They are the provenance of Part A and every value they support is already transcribed with its tag |
| **RC3-6** | **The document header said Phase 3 includes *"sentry post drawing S-07 equivalent"*** — but S-07 already exists (entry stairwell flight), and E.3.3 and Part L both name the sentry sheet **S-09** | E.3.3, Part L | **Header corrected to S-09** |
| **RC3-7** | **`CLAUDE.md` said *"Open item C16 (roof/platform junction) is not resolved"*** | H.3, H.14 and K.1 all record **C16 RULED AT 250 AND CLOSED** by RC1 on 10 Sep 2026, and A.4.7 carries the corrected clause | **`CLAUDE.md` corrected.** The stale instruction would have had a future session re-open a closed item |
| **RC3-8** | **`QUICK_STATE.md` said *"`current/staad/` — 3 STD"* and carried QA1's 65 / 68 drawing counts** | Six `.std`; 80 DXF | **`QUICK_STATE.md` refreshed** |
| **RC3-9** | **H.24 claimed *"0 new text overlaps on either sheet"* for `DR-A1`** | A-301 carries one, introduced by DR-A1 | **Flagged in place under M.11 and fixed at H.25 (QA2-2)** |
| **RC3-10** | **B.3's flotation table is computed on the PRE-M1 underside** — 21.600 × 6.200 = **133.92 m², uplift 6175 kN** — while A.7.2 and every other statement in the project use **136.40 m², 6289 kN**. B.3 also read *"uplift acts on the REAL 133.92 m² underside"*, which since M1 has not been the real underside | Arithmetic: 46.11 × 133.92 = 6175; 46.11 × 136.40 = 6289. Weights scale by 22.0/21.6 = 1.01852 | **B.3 annotated, table preserved.** **No FoS changes** — both uplift and resistance scale with length, so 0.33 / 0.78 / 1.22 / 2.02 and COMB 102 = 1.21 all stand exactly as recorded, which is what B.3 already claimed and is now shown. **The hand check must use 136.40 m² / 6289 kN** |

**Also produced by RC3:** master **A.4.9**, a single short register of **every opening through
the protective boundary** — both blast doors, the inner security door, the entry door, the
missing W5 door `D-05`, the four permanent W8 gaps and the two escape shaft heads — collected
from A.2, A.3, A.4.6, A.4.7, B.2, B.6, F.1 and the FS2 escape-route schedule. **It states no new
value.** It also states, in one place, the three things the project does **not** hold for those
openings and must not invent: **no escape-shaft head hatch** `[N]` (EM-V6), **no ladder, rung or
fall-arrest in either 6.250 m / 6.800 m shaft** `[N]` (FS-V7), and **no blast-door vendor data
of any kind**, RF performance included `[N]`.

And `CONSOLIDATED_PROJECT_REPORT.md` — the project stated once, at its current state, for
reproduction. See I.2.

> **What RC3 did NOT do.** **No `K.1b` item is closed and none is downgraded.** No `[ASSUMED]`,
> `[UNRESOLVED]` or `[NOT AVAILABLE]` tag was converted. No dimension, level, load, thickness,
> bar, quantity, rate, date or float changed. **STAAD.Pro was not run.** No superseded text was
> deleted — every correction above sits beside the record it corrects, per M.11. **The main
> staircase is untouched:** 24 risers, 170.8333 mm, 280 mm tread, 3 flights × 8, total rise
> 4100 mm.

---

## H.28 Sixteen rulings by the project owner — revision RC4 — 11 September 2026

> **The owner was taken through the open register item by item and ruled on sixteen.
> Thirteen are actioned; three were deliberately left open.** Every ruling is
> `[C] owner ruling`, the class RC2's two rulings carry. **RC4 ran no analysis, executed no
> STAAD.Pro, converted no evidence tag by inference, and did not touch the main staircase.**
> Full record: `Owner Rulings RC4/Documentation/RC4_OWNER_RULINGS.md`; arithmetic in
> `Owner Rulings RC4/Calculations/`.

| # | Item | Ruling | Outcome |
|---|---|---|---|
| 1 | **SG2-V5** | **Accept the residual flotation risk in writing** | **A DEPARTURE FROM B.3 MITIGATION 1, RECORDED AS ONE.** No date moves. 70 days of exposure, 11-05-27 → 20-07-27, spanning the 2027 monsoon at stage 3: **FoS 1.22 at the design GWT, 0.86 flooded to grade.** B.3's other three mitigations stay mandatory |
| 2 | **FS-V7** | **Ladder only; fall-arrest deferred** | Ladder designed, one type both shafts. **Does NOT close — it changes.** Three named gaps: no fall-arrest, no rest platform, and the injured-person question |
| 3 | **EM-V3** | **Bay 8 is INSIDE the EMP boundary** | **CLOSED.** BV-4/BV-5 now REQUIRE honeycomb WBC panels. **The project now holds two protective boundaries that do not coincide** — gas-tight is bays 1–6, EMP is bays 1–8 — **and only one has ever been drawn** |
| 4 | **A4** | **Build the k_s = 500 000 variant** | `Underground_Shelter_ks500000.std` built and validated. **k_s stays `[A]` at BOTH bounds; neither has been run** |
| 5 | **U2** | **No direct hit — as designed** | **CLOSED.** Nothing changes |
| 6 | **U3** | **Hold 50 psi / t<sub>d</sub> 0.13–1.33 s** | **CLOSED.** Nothing changes; the yield stays unstated rather than invented |
| 7 | **WM-V7** | **Ballistic protection not required** | **CLOSED.** Brick stands; nothing changes |
| 8 | **U4 / DR-A1-V1** | **Adopt the EAST position** | **Three findings — see below.** One assumed position instead of two. **`U4` stays `[A]`** |
| 9 | **FS-1 / D-05** | **Design it now** | **FS-1 CLOSES.** Route R1 crosses an opening that exists |
| 10 | **EL-V6** | **Compute the heat balance** | **CLOSED as computed; opens `RC4-V1`** |
| 11 | **EM-V5** | **LEAVE OPEN** | Unchanged. **Sharpened by rulings 10 and 12** |
| 12 | **SG-V6** | **Specify and price it** | Specified; **8 m³ BOQ item added, rate `[A]`** |
| 13 | **EM-V4** | **LEAVE OPEN** | Unchanged |
| 14 | **CAM-V5 / SG2-V3** | **Fix both from the design's own logic** | **BOTH CLOSED.** SH-1 **RECOVERED** from the project's own 12.3 m; SH-2 head **+1.500** |
| 15 | **U8** | **Confirm 300 × 150 and verify** | **HALF re-derived — see `U8-F1`** |
| 16 | **SG-V7** | **LEAVE OPEN** | Unchanged. **Sharpened by ruling 12** |

### The four findings RC4 produced

| Ref | Finding |
|---|---|
| **`RC4-F1`** | **DR-A1-V1's sentry X range is wrong.** It records A-301 as drawing the post at **X 31700–36300**. A-301's own note 2 says **X 32000–36000** — **4000 wide, which IS the post's external dimension**; 4600 matches nothing. The drawing is the primary source and is self-consistent. **Corrected.** An elevation gives no Y, so **Y 600–5600, centred on Y 3100**, is set by RC4 `[A]` |
| **`RC4-F2`** | **The clash DR-A1-V1 predicted does not happen — it rested on an assumed Y.** Reserve X 33000–51000 **Y 6500–17500**; sentry X 32000–36000 **Y 600–5600**. They overlap in X and **not at all in Y**, clear gap **0.90 m**. **The external works reserve does not move and SG2's 28 checks stand.** One NEW check fails: **SK-02 to the sentry post 1.80 m against IS 2470's 2.0 m** — SG2 never ran it because its post was 10 m north. **Fixed by moving SK-02 300 mm north to (35000, 8800) → 2.10 m.** All 8 checks that move touches, and all 5 against the post, re-run and PASS |
| **`RC4-F3`** | **The EAST position fails the ≥ 10 m rule as that rule is written.** A.2/A.4.8 say *"≥ 10 m clear of the shelter EXCAVATION"*. A-301's X 32000 is 10.00 m clear of the **box face** (X 22000); the **excavation** face with its 1000 working space is at X 23000, giving **9.00 m**. A-301's note cites the excavation rule while applying the box face. Satisfying it as written moves the post to **X 33000–37000**, which passes everything. **BOTH readings recorded; NEITHER adopted over the other — the EAST position is a drawing convention, not a survey coordinate** |
| **`U8-F1`** | **The parapet confirmation is necessary but not sufficient.** Parapet 0.300 × 0.150 × 25 = **1.125 kN/m**, exact. Residual **3.037 kN/m** is the roof projection, and **the projection dimension is recorded nowhere** — back-solving gives 810 mm (slab alone) or 578 mm (slab + finish). Neither is round, neither is drawn, **neither is adopted** |

> **Also recovered, and it was never written down: SG2's 50 m envelope pin is the box centre
> (11000, 3100).** Solving from SG2's own worst case — the reserve far corner at 42.51 m —
> reproduces it exactly. `[R]`

### `RC4-V1` — the one new open item

> **A SEALED SHELTER WITH A 4 kW HEAT SURPLUS AND NO ROUTE OUT FOR IT.** The 96-hour closed-mode
> balance is now computed: **6.363 kW sensible**, **2.199 GJ over 96 h**, air rising **13.2 K**
> to about **39 °C and still climbing**, and a mean duty of **3.60 kW (adopt 4 kW, 1.14 TR)** to
> hold 30 °C. The duty is small. **The rejection path does not exist** — in closed mode there is
> no ventilation air to reject to and every envelope penetration is already spoken for, so the
> heat has to go to the ground, which means **a new penetration of the protective envelope that
> nobody has designed** and an EMP treatment for it. **Referred, not solved.**

### What RC4 changed in Parts A–L

| Where | Change |
|---|---|
| **A.4.8** | Sentry post — the EAST position adopted at **X 32000–36000, Y 600–5600** `[A]`, with `RC4-F1` and `RC4-F3` recorded beside it |
| **A.4.9** | Exit hatches and blast doors — **the escape shaft ladder added**, with its three named gaps |
| **A.7.7** | `U8` note — the parapet term now `[C]` and exact; the projection term `[N]` |
| **A.7.2 / B.3** | Untouched. **The flotation ruling changes no number — it accepts the programme as written** |
| **D.1** | `Underground_Shelter_ks500000.std` added — seven `.std` files |
| **K.1b** | **Thirty-three → twenty-five.** ~~Thirty-three → twenty-one~~ — **corrected by RC9 (H.33); the original figure was wrong, and so were RC5's, RC7's and RC8's.** Closed by RC4 (9): `U2` `U3` `WM-V7` `CAM-V5` `EM-V3` `EL-V6` `SG2-V3` `SG2-V5` `DR-A1-V1`. (FS-1/D-05 was listed here in error — it is a finding, not a K.1b row.) Changed but open: `FS-V7` `U8` `SG-V6`. **New: `RC4-V1`** |
| **K.1e** | The RC4 rulings recorded alongside RC2's and SG2's |
| **K.2 A4** | The upper bound is now buildable and built. **Still `[ASSUMED]`, still unrun** |

> **What RC4 did NOT do.** No `[A]`/`[U]`/`[N]` tag converted by inference. No analysis run.
> No dimension, level, load, thickness or bar in A, B, F or L changed, except where a ruling
> created something that did not exist. One BOQ item added; no existing quantity, rate, date or
> float moved. **Main staircase untouched.**

---

## H.29 Four more rulings, and one assumption closed on the evidence — revision RC5 — 12 September 2026

> **Three rulings actioned, one left open, and `A13` closed WITHOUT a ruling — the first of
> K.2's fourteen assumptions to close.** RC5 ran no analysis and executed no STAAD.Pro.
> Calculations: `Owner Rulings RC4/Calculations/RC5_CALC_OUTPUT.txt` §R.7–R.9.

| # | Item | Ruling | Outcome |
|---|---|---|---|
| 17 | **RC4-V1** heat rejection | **Reject to the ventilation air in open mode only — NO new penetration** | **RULED AND NARROWED, not closed.** See `RC5-F1` |
| 18 | **EM-V6** shaft head hatches | **Design the hatch as a structural element only**; EMP bonding stays with the EMP package | Structural design done. **EM-V6 stays open for its EMP half.** See `RC5-F2` |
| 19 | **WM-V6** sentry seismic re-check | **LEAVE OPEN — wait for STAAD** | Unchanged. Nothing unsafe; every member over-designed, direction favourable, margin unquantified |
| 20 | **EL-V2** generator fuel | **Day tank inside, sized to the derived duty** | 250 L nominal / 210 L usable in bay 8. **RULED AND NARROWED** |
| — | **`A13`** sentry frame member releases | **NO RULING NEEDED — closed on the evidence** | K.2 asked for the `.std`; **the file has been in the workspace since H.4 and nobody re-read it.** See K.2 |

### `RC5-F1` — the ventilation air cannot reject this heat, and was never sized to

```
ventilation 300 m3/h -> 0.1005 kW/K  ->  63.3 K needed to reject 6.363 kW
ventilation 600 m3/h -> 0.2010 kW/K  ->  31.7 K needed

at a realistic difference:   5 K, 300 m3/h ->  0.50 kW =  7.9 % of the gain
                            10 K, 600 m3/h ->  2.01 kW = 31.6 % of the gain
```

**300 m³/h is a CONTAMINANT rate** — FEMA 453's 0.25 cfm/ft² over the clean zone, for CO₂ and
filtration — and it is about **an order of magnitude short of a heat-rejection rate**. The
second train is **standby, not simultaneous**, so 600 m³/h is not a case the design contemplates.

**And in Pune it can be worse than nothing.** The supply air is ambient; whenever ambient
exceeds the internal temperature, ventilating **adds** sensible heat. **No ambient design
temperature exists anywhere in this project** `[N]`, so the number of hours cannot be stated —
the direction can.

> **The ruling is therefore recorded as an ACCEPTANCE of the ~39 °C condition, not as a solution
> to it.** The structure and the rock carry essentially the whole load in both modes, and R.2's
> 96-hour answer — **13.2 K of rise, reaching about 39 °C and still climbing** — is unchanged.
> That is a habitability judgement and it is the owner's to make; what RC5 adds is the
> arithmetic, so it is accepted with the number in view. **`RC4-V1` is NARROWED, not closed:
> from "no rejection path exists" to "the rejection path is the ground through the structure,
> and it has not been modelled."** A transient soil–structure **thermal** model is the missing
> piece, and it is a sibling of the transient soil–structure **interaction** already in Part C.

### `RC5-F2` — TWO 1400 dia PENETRATIONS OF THE PROTECTIVE BOUNDARY HAVE NO SPECIFIED CLOSURE

> **This is the finding of the whole RC4/RC5 pass, and nobody had asked the question.**
>
> A.2 defines the protective boundary as Blast Doors 1 and 2 **plus the perimeter walls, the mat
> and THE PRESSURE SLAB**. **ESC 1 and ESC 2 are 1400 dia bores straight through the pressure
> slab.** They begin in bay 1 — **inside the gas-tight envelope** — and in bay 8, and they finish
> at grade.
>
> **Each shaft head is therefore a 1.54 m² hole in the protective boundary, and the only thing
> that can close it is a hatch that does not exist.** The envelope penetration register lists
> ESC1 and ESC2 as **FAIL** and prescribes a bonded conducting hatch — **but it prescribes it for
> EMP. Nothing anywhere in this project states what the head has to resist STRUCTURALLY.**
>
> The design is silent, so RC5 takes the only defensible reading: **the head is part of the
> boundary and takes the full 383 kPa design blast.**

**The structural demand, and why a flat plate is the wrong answer:**

```
total force on the leaf   383 x pi x 0.700^2              = 589.6 kN
M = w.a^2.(3+nu)/16                                       =  38.71 kNm/m
V at the seating = w.a/2                                  = 134.1 kN/m
flat Fe250 plate  t = sqrt(6M/sigma) = 30.5 -> say 32 mm
mass of a 1600 dia x 32 leaf                              =  505 kg
```

**505 kg is the point, not the thickness.** Half a tonne cannot be lifted by a person escaping up
a 6.8 m ladder in the dark. **Adopted instead: a ribbed steel weldment** — 1600 dia, 12 mm face,
8 No. radial ribs 150 × 10 and a 150 × 12 perimeter ring — on a **steel seating ring cast into
the 250 collar**, bearing 150 mm all round, with **four quarter-turn dogs so the leaf resists
UPLIFT as well as downward pressure** (the negative phase and the rebound both lift it), and
**counterbalanced or spring-assisted, openable from inside by one person without a key or a
tool.** Indicative leaf mass **≈ 322 kg — still a mechanically assisted item.**

**Not designed and not invented** `[N]`: the rib proportioning (an orthotropic plate problem —
the flat-plate demand above is exact and is the **brief**), the counterbalance mechanism, and
every EMP figure.

> **And the consequence of splitting it the way the ruling splits it, stated plainly.** The EMP
> treatment for this opening is a **bonded conducting** hatch. Bonding is not a finish applied
> later — it is continuity between the leaf, the seating ring and the collar reinforcement, and
> it has to be designed **into** the weldment and the seat. **Ruling the structure and the
> bonding into different packages is exactly how these two shaft heads came to be undesigned for
> four revisions.** `EM-V6` stays open for its EMP half.

### Ruling 20 — the day tank, and the penetrations it did NOT add

```
600.6 kWh over 96 h x 0.35 L/kWh [A]   =  210.2 L
ADOPTED   210 L usable  ·  250 L nominal  ·  275 L bund (110 %)
          BAY 8 -- outside the gas-tight envelope, INSIDE the EMP boundary (RC4)
          welded steel, bunded, contents gauge, low-level alarm to the S-01 panel
```

**The fill and the vent are the real design question, not the tank.** Both cross the protective
boundary, and RC4 has just ruled bay 8 inside the EMP boundary, so two new bores would each need
blast, gas and EMP treatment — in the same wall where **BV-4/BV-5 already FAIL** the EMP criteria.

**ADOPTED: route both up the existing SH-2 bore and add no new penetration** — DN25 metallic fill
with a lockable cap at the SH-2 head, DN25 metallic gooseneck vent, both bonded to the shaft
earth. **This is the same instinct the owner applied to RC4-V1: use what already crosses.**
It needs HVAC and EMP coordination — **two DN25 lines sharing a 600 × 600 bore with two DN350
blast valves is a fit that has not been checked here** `[A]`. Fuel type unconfirmed, the
0.35 L/kWh rate still `[A]`, no vendor set, no fuel polishing, no tank fire suppression, no rate.

> **What RC5 did NOT do.** No tag converted by inference. No analysis run. No dimension, level,
> load, thickness or bar in A, B, F or L changed. No BOQ quantity, rate, date or float moved.
> **Main staircase untouched.**

---

## H.30 Six assumptions closed, and the excavation face ruled — revision RC6 — 12 September 2026

> **K.2 GOES FROM FOURTEEN OPEN TO SEVEN, AND THE SEVEN THAT REMAIN ARE EXACTLY THE SITE
> INVESTIGATION.** Every assumption that could be closed by engineering judgement is now closed.
> Nothing left in K.2 can be settled by anyone in a room — each of the seven needs a borehole, a
> piezometer, a plate load test, a percolation test or a packer test. Calculation:
> `Owner Rulings RC4/Calculations/RC6_CALC_OUTPUT.txt` §R.10.

| # | Item | Ruling | Basis |
|---|---|---|---|
| 21 | **A9** sentry infill separation | **KEEP R = 3.0 — CLOSED** | The position in use is **the conservative one**: R = 5.0 would give A<sub>h</sub> 0.060 against 0.100, so **V<sub>b</sub> 73.18 kN is ≈ 1.67 × what a separated special moment frame would need.** Separating would require an SMRF and the IS 13920 detailing this project does not claim, and would undo SP-B2's tie detail. **Nothing changes** |
| 22 | **WM-V9** excavation face | **BATTER THE SOIL CAP; VERTICAL IN ROCK BELOW IT** | See below |
| 23 | **A6** K<sub>a</sub> | **ACCEPT — CLOSED** | K<sub>a</sub> = 1.0 saturated is **used**; the dry-berm ≈ 0.5 is **deliberately not relied on**. Taking the full 383 kPa on the headhouse walls rather than crediting unverifiable berm attenuation is the conservative choice, and C10 already took it off the critical path |
| 23 | **A10** wind k1 = 1.08 | **ACCEPT — CLOSED** | A 100-year life on a load path that **does not govern** — seismic beats wind **2.4 : 1** |
| 23 | **A14** Poisson 0.20 | **ACCEPT — CLOSED** | The standard value for concrete; plate behaviour, minor |
| 24 | **A11** b<sub>eff</sub> 2.5 m, HW3 | **ACCEPT — CLOSED** | The strip is at **26 % two-way / 41 % on the conservative one-way bound**. More than half the capacity is spare, so b<sub>eff</sub> would have to be badly wrong to matter |
| 24 | **A12** trapezoid factor 0.7946 | **ACCEPT — CLOSED** | ≈ **2 %** on B2's support moment, inside its 89 % utilisation. **The factor itself is exact**: 1 − 1/(3r²) at r = 1.2740 gives 0.79463. Using it for both BM and FEM is the simplification, and the margin swallows it |

### What K.2 now looks like — and why this is the useful result

```
CLOSED (7)   A6   Ka = 1.0 saturated, dry berm not relied on      conservative
             A9   sentry infill not separated, R = 3.0            conservative
             A10  wind k1 = 1.08, wind does not govern            standard
             A11  b_eff 2.5 m for HW3, strip at 26 % / 41 %       margin
             A12  trapezoid factor for both BM and FEM, ~2 %      margin
             A13  sentry frame has no member releases             READ FROM THE .std
             A14  Poisson's ratio 0.20                            standard

STILL OPEN (7) -- AND EVERY ONE NEEDS A PHYSICAL TEST ON THIS PLOT
             A1   rockhead 1.5-2.0 m                    boreholes
             A2   DESIGN GWT (-)2.000                   piezometer, FULL monsoon
             A3   SBC 3240 kPa                          plate load / core testing
             A4   ks 100 000 - 500 000 kN/m3            plate load test (BOTH bounds)
             A5   K0 0.50, gamma 20/21                  site investigation
             A7   soak-pit absorption 20 L/m2/day       PERCOLATION TEST, mandatory
             A8   structural seepage 0.5 L/m2/day       packer permeability tests
```

> **That is the sentence worth carrying into the viva.** The assumption register is no longer a
> mixed bag of judgement calls and missing data. **Everything a competent engineer could decide
> has been decided. What is left is precisely the site investigation the project has never
> had** — and `SG-V1`/`SG-V2` already say why: the only investigation available is **off-site**
> and **reached about 1.5 m against a formation at (−)6.800**.

### Ruling 22 — the excavation face

**The project measured 1.000 m working space and VERTICAL UNBENCHED faces for the full 6.800 m.**
In basalt that is reasonable. But SG1 measured what sits on top of the basalt: **rockhead at
0.9–1.5 m**, with a **black cotton CH horizon at FSI 60–65 %** in the top 0.18–1.0 m.

> So the face is about **1.0–1.5 m of soil — including very-high-swelling clay — standing
> vertically on 5.3–5.9 m of rock, with the rock excavation undercutting it.** Under the
> `SG2-V5` acceptance it also stands open **across a monsoon**. That soil cap is the one part of
> this excavation that has no business being vertical.

```
ADOPTED   batter 1 : 1 MINIMUM over the soil cap, grade to rockhead, all four
          sides; VERTICAL FACE RETAINED IN ROCK below rockhead

          extra excavation   1 : 1     1.500 m offset      76.4 m3
                          1.25 : 1     1.875 m offset      96.7 m3
                           1.5 : 1     2.250 m offset     117.6 m3
          (a 1.000 m bench at rockhead instead would be 96.6 m3)

          WORKING SPACE UNCHANGED -- the 1.000 m is at FORMATION, 5.3 m below
          the battered zone, so no BOQ working-space quantity moves
```

**1 : 1 is a MINIMUM, not the answer.** A batter in FSI 60–65 % clay, undercut and wetted across
a monsoon, may need to be considerably flatter. `IS 3764` is named **by title only** — it is not
in the workspace and Part G forbids citing an unconfirmed clause. **The angle and its seasonal
variation are the geotechnical engineer's, and the quantity moves with the angle** `[A]`.

> **The same collision `SG-V6` has, an order of magnitude bigger.** This produces **76–118 m³ of
> excavated CH clay** on top of the 8 m³ from the stairwell raft. **`SG-V7`, which the owner left
> open, warns against re-laying exactly that material as the cover's 300 turf over the granular
> filter.** Recorded, not resolved.

**`WM-V9` closes as a measurement basis** — the project now states a face treatment instead of an
unexamined vertical. **The slope-stability assessment it always asked for is still outstanding,
and still needed.**

> **What RC6 did NOT do.** No analysis run. No dimension, level, load, thickness or bar changed.
> **No BOQ quantity, rate, date or float moved** — the 76–118 m³ is derived and recorded, not
> priced. **Main staircase untouched.**

---

## H.31 Six more closed, and the IS 2470 offset set completed — revision RC7 — 12 September 2026

> **K.1b GOES FROM TWENTY-FIVE TO NINETEEN.** ~~twenty-one to fifteen~~ — **corrected by RC9 (H.33).** Calculation:
> `Owner Rulings RC4/Calculations/RC7_CALC_OUTPUT.txt` §R.11.

| # | Item | Ruling | Outcome |
|---|---|---|---|
| 25 | **EL-V7** CO₂ scrubber air movement | **Compute the airflow** | **RULED AND NARROWED.** Duty **0.18 m³/h of CO₂**, loop **75 m³/h**. See below |
| 26 | **EL-V4** incoming mains | **The mains does not gate the protective design — CLOSED** | See below |
| 27 | **SG-V4 · SG-V5 · SG-V8 · SG-V10** | **Source defects — ALL FOUR CLOSED** | They are defects in the **supplied documents**, not in this design record |
| 28 | **SG2-V1** foul soak pit to any well | **OWNER CONFIRMS THERE IS NO WELL WITHIN 15 m — CLOSED** | **The IS 2470 offset set is complete for the first time.** See the caveat |
| — | **SG2-V2** perimeter fence distance | **NOT ADDRESSED by the ruling — STAYS OPEN** | Recorded as still open, not assumed closed |

### Ruling 25 — the CO₂ scrubber duty, recovered from the project's own arithmetic

**The production rate did not have to be assumed. It was already embedded in the HVAC package's
own 9.9 h figure**, and reading that backwards gives every term:

```
time to 1.0 % CO2, airlock shut = (0.0096 x 184.96) / (9 x 0.02) = 9.9 h

   allowable rise 0.04 % -> 1.0 %        0.0096 fraction        [C]
   occupied volume, airlock shut         184.96 m3              [C]
   occupants x production                9 x 0.02 m3/h/person   [C]
   TOTAL CO2 PRODUCTION                  0.18 m3/h
   check 1.7756 / 0.18 = 9.86 h   -- reproduces the stated 9.9 h
   over 96 h closed                      17.28 m3 of CO2
```

> **The scrubber is a CLOSED-MODE device, and it is not optional.** In open mode the 300 m³/h
> flushes CO₂. In **Mode 3 CLOSED** there is no fresh air at all, and without a scrubber the
> envelope reaches 1.0 % in **9.9 hours against a 96-hour design occupancy**. That ratio is the
> whole argument.

```
Q = production / (eta x C_target)

   target CO2     eta 0.50   eta 0.80   eta 0.95
      0.5 %          72.0       45.0       37.9   m3/h
      1.0 %          36.0       22.5       18.9   m3/h

ADOPTED   75 m3/h recirculation loop  [R]  -- the worst cell, because
          designing to it costs almost nothing
```

**And it checks the only number the project already had.** A 75 m³/h fan at an assumed 250 Pa
across a packed bed draws **≈ 11.6 W** against EL1's **0.10 kW** allowance — **roughly 8 × margin**.
**So EL-V7 changes no electrical value**: the load schedule, the 6.256 kW connected load and the
15 kVA check at 49 % all stand. **What changes is that the allowance is now checked rather than
assumed.**

**Not designed, not invented** `[N]`: the absorber vessel, bed depth, face area and residence
time; the **soda lime charge** (17.28 m³ of CO₂ is the duty — converting it to a mass needs the
product's absorption capacity, which is vendor data); the single-pass efficiency, taken across a
range rather than from any product; and **where in bay 5 the absorber stands — bay 5 is the
tightest bay at 1560 clear, and HV-F3 already records that the filter trains leave 110 mm at the
sides.**

### Ruling 26 — the mains does not gate the protective design

**The shelter is designed to operate on GEN-1 alone for the full 96 hours.** RC2 allows the
generator to run in the closed mode, RC4 put it inside the EMP boundary, and the connected load
is **7.360 kVA against 15 kVA — 49 %**. The battery carries the essential services for 4 h if the
set is down.

> **So incoming mains capacity affects normal-mode operation and cost, and never the protected
> function.** `EL-V4` had been recorded as *blocking any fault level or discrimination study*; it
> still does — **for the normal-mode installation** — but it blocks nothing protective, and that
> is the distinction the register was missing. **No capacity figure is invented.**

### Ruling 27 — four source defects, closed

**None of the four is a defect in this design record**, and the project's position on every one
is already correct:

| | The defect, in the supplied document | This project's position |
|---|---|---|
| **SG-V4** |the P1 deck's contour map and its elevation profile disagree by **12–16 m in level** | **Neither is adopted.** The project works on a local datum with grade = 0.000 |
| **SG-V5** |the soil report's annual rainfall is **1.4–1.7 ×** too low against the 42-year Jun–Oct mean | **No figure was substituted and the suspect one was not corrected** — and SG2 established that **not one pipe, pit, pump or structure is sized by rainfall** |
| **SG-V8** |three deck statements are attributed to the SEMT report and **are not in it** | **All three are used nowhere in the design** |
| **SG-V10** |the SEMT field-work date is nowhere, so *"no water table"* is **season-unknown** | **Flagged as `[U]`, not asserted** — and `SG-V2` governs regardless |

> **These are corrections owed to the SOURCE documents before the next presentation, not open
> questions in this design.** Closed on that basis.

### Ruling 28 — the well, and what the ruling is and is not

**The project owner confirms there is no well within 15 m of the foul soak pit.** `[C] owner
ruling`

**The IS 2470 offset set is therefore complete for the first time in this project:**

```
foul soak pit to the SEPTIC TANK   >= 5 m     5.40 m      DEMONSTRATED  (SG2)
soak pit to any BUILDING           >= 2 m    10.97 m      DEMONSTRATED  (SG2)
foul soak pit to any WELL          >= 15 m      --        OWNER RULING  (RC7)
```

> **THE CAVEAT, AND IT MATTERS.** This is an **owner ruling, not a survey result.** It is recorded
> as `[C] owner ruling` and not as `[C] surveyed`, and the distinction is deliberate: **if a well
> is later found within 15 m, SK-01 moves.** Foul effluent near a water source is the one
> clearance nobody should carry on an assumption, which is why it stayed open through SG2 — and
> the ruling closes it on the owner's knowledge of the plot, which is evidence the project did
> not previously have.

> **`SG2-V2` — the perimeter fence distance — was NOT addressed by this ruling and STAYS OPEN.**
> It is recorded here so that it is not mistaken for closed. SG2's own reasoning still holds: the
> layout is dimensioned so every offset is relative, so a fence distance changes **where** the
> reserve sits, never **whether** it works.

> **What RC7 did NOT do.** No analysis run. No electrical value, dimension, level, load,
> thickness, bar, BOQ quantity, rate, date or float changed. **Main staircase untouched.**

---

## H.32 Two closed, one split, one reclassified — revision RC8 — 12 September 2026

> **K.1b GOES FROM NINETEEN TO SEVENTEEN**, and one long-standing entry leaves the register
> altogether because it was never a gap. ~~fifteen to thirteen~~ — **corrected by RC9 (H.33).**

| # | Item | Ruling | Outcome |
|---|---|---|---|
| 29 | **SG2-V2** perimeter fence distance | **CLOSED on the layout's immunity** | The layout was built so every offset is **relative to the structure**, never to a boundary. A fence distance changes **where** the reserve sits, never **whether** it works |
| 30 | **SG2-V4** no wind rose | **SPLIT — the intake/exhaust half CLOSED, the plume half STAYS OPEN** | See below |
| 31 | **EM-V2 + EL-V3** EMP Zone 2 | **Record the circularity; BOTH STAY OPEN** | See below |
| 32 | **EL-V5** electrical detail schedules | **RECLASSIFIED — a declared scope boundary, not a gap.** Moves to the new **K.1f** | It leaves K.1b |

### Ruling 30 — the wind rose, split in two because it is two questions

**(a) The intake / exhaust relationship — CLOSED.** SG2 justified the site orientation on
**access, fall, noise and end-to-end separation, and explicitly NOT on prevailing wind** — that
was a deliberate choice of geometry over meteorology. RC4 then fixed **SH-1 at (−2400, 3100) and
SH-2 at X 22598–23198**, putting intake and exhaust **25.30 m apart at opposite ends of a 22 m
box**. That separation is robust **whatever the wind does**, which is precisely why it was chosen.
**This half needs no wind rose and never did.**

**(b) The plume direction for the CBRN case — STAYS OPEN, and must.**

> **A CBRN shelter with no wind direction data cannot state which way a release drifts.** No
> argument from layout supplies that, and the 25.30 m separation — which settles (a) completely —
> says **nothing** about it. The event the whole structure exists to survive is the one this gap
> touches. **Closing both halves on one argument is exactly the move the register exists to
> prevent.**

### Ruling 31 — the circularity between EM-V2 and EL-V3, named

**Two packages are each holding the other's placeholder, and nobody had written that down.**

```
EM1 designs the EMP Zone 2 enclosure at 2400 x 1600 x 2200 external.
    Every dimension is [A].  It is a FIT TO BAY 3, not a derivation.
    What it waits on: AN EQUIPMENT SCHEDULE.

EL1 answers with Z-01, a 1.50 kW allowance.
    EL1's own words: "ALLOWANCE, NOT A SCHEDULE."
    Its stated justification: "This is the number EM-V2 was waiting for."
```

> **So the enclosure is sized to fit a bay, and the load is chosen to give the enclosure a basis.
> The two numbers corroborate each other and NEITHER IS EVIDENCE.** That is not a criticism of
> either package — both tagged their work `[A]` and both said what they were doing. It is a
> property of the pair that only shows up when you read them together, and **naming the loop is
> worth more than closing either half would be.**
>
> **BOTH STAY OPEN.** What breaks the loop is an **operational equipment list** — what actually
> goes in Zone 2 — which is a client input, not a calculation. Until it exists, **the 2400 × 1600
> × 2200 and the 1.50 kW must be read as a matched pair of placeholders, not as two independent
> confirmations.**

### Ruling 32 — EL-V5 was never a gap

EL1 says so in its own first paragraph: **"A BASIC PACKAGE, ON PURPOSE. It stops at board level."**
The absence of circuit, cable, luminaire and socket schedules is a **declared scope boundary**,
not an oversight — and carrying it in K.1b alongside genuine gaps **inflated the open count and
obscured what actually needs attention.**

**Moved to the new `K.1f`.** It remains true and visible that the schedules do not exist; it is
simply recorded as a stage that has not been commissioned rather than a problem to be solved.

> **What RC8 did NOT do.** No analysis run. No value, quantity, rate, date or float changed.
> **Main staircase untouched.**

---

## H.33 A count this session got wrong, corrected — revision RC9 — 12 September 2026

> **RC9 corrects an error revisions RC4 to RC8 introduced. It rules nothing, designs nothing and
> changes no design value.**

**What went wrong.** Each of RC4 to RC8 ruled on open items and recorded every ruling faithfully
in its own Part H narrative and in `K.1e`. **But thirteen of the rows in the `K.1b` table itself
were never annotated** — `U2` `U3` `WM-V7` `CAM-V5` `EM-V3` `EL-V6` `SG2-V3` `SG2-V5`
`DR-A1-V1` `SG-V4` `SG-V5` `SG-V8` `SG-V10` `SG2-V1`. A reader counting the table got **34**; the
narratives claimed **21**, then **15**, then **13**.

> **All three of those counts were wrong, and the first one was wrong arithmetically on its own
> terms**: H.28 listed eight closures and claimed a fall of twelve, and one of the eight
> (`FS-1 / D-05`) is a finding, not a `K.1b` row at all.

**What RC9 does.**

1. **Annotates all fourteen un-marked rows** with the ruling that settled them and the revision
   that made it, each keeping its original entry alongside under **M.11**.
2. **Adds `K.1b-INDEX`** at the head of the register — every row classified as still-open
   (narrowed), still-open (unchanged), closed, or moved, **with the totals stated so the count
   can be verified by reading rather than by trusting a sentence.**
3. **Corrects the figures in H.28, H.29, H.31 and H.32**, striking the wrong ones rather than
   deleting them.

**THE CORRECTED SEQUENCE:** 33 → **25** (RC4) → 25 (RC5, three narrowed, none closed) →
25 (RC6) → **19** (RC7) → **17** (RC8).

**`K.1b` HOLDS SEVENTEEN STILL-OPEN ITEMS** — nine narrowed by a ruling, eight unchanged — plus
sixteen closed rows and one moved to `K.1f`, all retained in the table.

> **Why this is recorded rather than quietly fixed.** The project's own discipline is that a
> register which disagrees with its own narrative is exactly the kind of defect this master
> exists to catch — `RC3-1` corrected the same class of error in A.7.9, and `H.24`'s *"0 new text
> overlaps"* was another. **This one was mine.** Rule M.11 applies to it in the same way: the
> wrong counts stay visible with the correction beside them.

> **What RC9 did NOT do.** No item was closed, opened, reclassified or re-ruled. No design value,
> quantity, rate, date or float changed. No analysis run. **Main staircase untouched.**

---

## H.34 What the rulings left stale in the packages — revision RC10 — 12 September 2026

> **RC4 to RC9 ruled on thirty-two items and recorded every ruling in this master. THEY DID NOT
> TOUCH THE DISCIPLINE PACKAGES.** Six artefacts therefore now say something the master has
> settled. **This is the same class of defect `RC9` corrected one level up** — and it was found by
> looking for it rather than by waiting for it. Register:
> `Owner Rulings RC4/Schedules/RC10_PACKAGE_IMPACT_REGISTER.md`.

| # | Artefact | What it still says | What the master has ruled |
|---|---|---|---|
| 1 | `EMP Protection/…/ENVELOPE_PENETRATION_REGISTER` — **BV-4, BV-5** | *"honeycomb WBC panel … **if** bay 8 is inside the EMP boundary"* | **`EM-V3` RULED: bay 8 IS inside.** The panels move from conditional to **required**. **And RC2 lets BV-4/BV-5 REOPEN in closed mode — so the panels must work with the valves open** |
| 2 | Same register — **ESC1, ESC2** | *"**No hatch is specified.**"* | **`EM-V6` RULED AND SPLIT: a hatch IS specified structurally** (1600 dia ribbed weldment, quarter-turn dogs against uplift, counterbalanced). **The EMP half is still open, so `FAIL` stands.** The register should also carry **`RC5-F2`** — these bores pierce the **pressure slab**, so each head is a **1.54 m² hole in the blast boundary**, not only an EMP aperture |
| 3 | `HVAC/…/HVAC_EQUIPMENT_SCHEDULE` — **SH-1** | Location *"West of the box"* | **`SG2-V3` CLOSED: centred (−2400, 3100)** — **recovered from this schedule's own "12.3 m to the entry" note, to within 28 mm** |
| 4 | Same schedule — **SH-2** | No head level | **`CAM-V5` CLOSED: +1.500** |
| 5 | `Fire and Life Safety/…/FS_ESCAPE_ROUTE_SCHEDULE` — **R2, R3** | 6.250 m and 6.800 m climbs, **no means of climbing** | **`FS-V7` RULED: a ladder is designed** (297.6 / 295.7 mm pitch). **And the schedule must still say there is NO fall-arrest, NO rest platform, and that a vertical ladder cannot pass a stretcher — `FS-V7` did not close, it changed** |
| 6 | `Site and Concealment/…/CAMOUFLAGE_AND_CONCEALMENT_POLICY` | *"SH-2, whose head level is recorded nowhere"*; **`CAM-V5` listed OPEN** | **`CAM-V5` CLOSED at +1.500.** The above-ground signature is **complete for the first time** — +7.000 · +2.450 · **+1.500 both shafts** · +0.900. **`C-101` can draw SH-2 to scale** |

> **NOTHING IS SILENTLY EDITED.** All six are **build artefacts** regenerated from their packages'
> `Scripts/`. The project's rule is to edit the generator and re-run, never the artefact — and
> EM1, EL1, SG1 and SG2 each verified that **every other package regenerates byte-identically**,
> a property worth not breaking casually. **Applying this register is a package-by-package job
> with a regeneration check, and it has NOT been done.**

> **THE LESSON, AND M.14 ALREADY STATES IT.** *"A change that stops at 'reinforcement' and never
> reaches 'drawings' is not finished."* **RC4 to RC9 stopped at this master.** This register is
> where they did not reach. **The failure mode has now appeared twice in two days** — once inside
> the master (`RC9`), once between the master and its packages (here) — and both times the fix was
> to make the thing countable rather than to trust a narrative.

> **What RC10 did NOT do.** No artefact edited, no generator run, no item closed or re-ruled, no
> design value, quantity, rate, date or float changed. **Main staircase untouched.**

---

## H.35 The sump pit head, and where the pits actually are — revision DR-A2 — 12 September 2026

> **What was asked.** *"You added the sump pit to the side section but it now shows no floor
> above the sump pit — correct it. Also make the front elevation indicate the soak pit and sump
> pit location relative to the project."* Both are drafting requests. **The first one is not a
> drafting error in `DR-A1` — the floor really was missing, and it was missing because the thing
> that closes the opening has never existed anywhere in this project.**

### What changed

| Sheet | File | Changed |
|---|---|---|
| **A-202** | `current/cad/2_Side_Section_with_Stairs.dxf` | **`SU-01`'s cover** drawn at floor level (−)6.100 across the 1500 clear opening; eight note lines; revision strip |
| **A-301** | `current/cad/5_Front_Elevation.dxf` | **`SU-01` drawn at true X** on the buried box; a **1:200 KEY PLAN** carrying `SU-01`, `ST-01` and `SK-01` at true project X **and Y**; note 7; note 2's displacement corrected; bottom dimension chain moved down 1200; revision strip |

Both are Rev F **input** drawings and are directly editable (`CLAUDE.md`). **No new layer was
added** — the work uses `SERVICES`, `HIDDEN`, `WALLS`, `CENTRE`, `DIM`, `LEADER`, `TEXT` and
`SHEET-TEXT`, all already present.

### A-202 — why there was no floor, and what now closes it

`DR-A1` drew the pit correctly. **The mat is genuinely interrupted over `SU-01`** — `F.1` bars a
*"sump pit opening"* with 4-T20 trimmers each face each side, `BBS_MASTER` line `F10` calls it an
opening 1500 × 1500 at X 11070–12570, Y 900–2400, and `WM-V8` measures the mat **gross by
1.35 m³ = 1.5 × 1.5 × 0.600** for it. **A 1500 × 1500 hole through the floor is what the project
records, so that is what `DR-A1` drew.**

**`DR-A2-F1` — but Bay 5 cannot be crossed like that, and no cover is recorded anywhere.**
Bay 5 is **1560** clear (`A.3`) and the pit is **1500** of it, so the opening runs effectively
the full width of the bay: with the pit open there is no way past it to the two filter trains,
the CO₂/O₂ plant or the dehumidifier. The `ROOM_FINISH_SCHEDULE` also falls room `U-05`
**1:80 direct to the sump**, so whatever closes the opening has to pass water. **A cover is not
optional here — and the project contains no cover: no type, no depth, no duty, no fixing, no
lifting arrangement, in any schedule, drawing or document.**

So the cover is drawn as **one line at (−)6.100 across the 1500 clear opening, on the `SERVICES`
layer because it is not structure**, tagged `SU-01 COVER [A]`, with eight note lines on the
sheet's face stating all of the above. **The line is diagrammatic and implies no thickness**;
the mat, the blinding and the formation stay interrupted exactly as `DR-A1` drew them, and the
rising main still passes through. **Nothing was converted into a confirmed element** — the cover
is `[A]`, its specification is `[N]`, and **`DR-A2-V1` is opened for it**.

> **`S-06` V3 has the same question the other way round, and it is left alone.** The 1:30 detail
> draws the mat as one rectangle **straight across** the pit while also drawing the void dashed
> **up to floor level** — the two cannot both be true, and it reads as a background rectangle
> that was never trimmed. **No change is made to `S-06`**: it is the dimensioned authority for
> the pit itself, that is not what is wrong with it, and it is a separate sheet from the two this
> request names. **Recorded here so the next reader finds it, not fixed here.**

### A-301 — the sump pit at true X, and a key plan because an elevation cannot show Y

`SU-01` is drawn inside the buried box **at true X 10768–12868 (clear 11068–12568)**, dashed like
the rest of the box, hanging from (−)6.100 to (−)8.000 with the clear void to the invert at
(−)7.600, leadered and labelled with its true position. It is the first time the sump appears on
this sheet.

**`SK-01` could not be handled the same way, and neither could `ST-01`.** They stand at plan
**Y 16000**, which is **9.8 m north of the box's north face** — an elevation has no way to show
that, and `DR-A1`'s break puts them at a displaced X as well. **So a 1:200 key plan was added**,
carrying at true project X *and* Y: the box `22000 × 6200`, the excavation face at X 23000, the
sentry post `X 32000–36000, Y 600–5600` `[ASSUMED]` (`U4`, east position per `RC4`), `SG2`'s
external works reserve `X 33000–51000, Y 6500–17500`, and `SU-01`, `ST-01` and `SK-01` in their
real positions. Dimensioned: **11068 and 1500** to the pit in X, **900 and 1500** in Y,
**14750 to `ST-01`** and **7250 on to `SK-01`** from the box east face, and **9800 north**.
**Every figure on it is transcribed from `A.3`/`A.4`, `SG2` and the drainage schedules; not one
is new.** Note 7 says why the plan is there and the key-plan notes carry `U4`, `RC4-F3`, the
displacement and the rest of the reserve's contents.

### Three findings — two fixed here, one recorded and left

| | |
|---|---|
| **`DR-A2-F2`** | **Note 2 said the east strip is displaced `5450`. It is displaced `4950`.** `ST-01` true centre X 36750 is drawn at 41700, `SK-01` true 44000 at 48950 — **4950 both times** — and `H.24` says 4950 too. **Corrected on the sheet to 4950.** Sizes, spacing and the 5400 offset were always right; only the sentence was wrong |
| **`DR-A2-F3`** | **`DR-A1`'s own revision line on A-202 sat BELOW the inner sheet border**, at y −24373 against a border at −24198, and `DR-A1` recorded *"no text outside the inner sheet border"*. **`QA2` (H.25 / report §10.3) had found and fixed the A-301 half of this and did not re-scan A-202.** All three revision lines on **both** sheets are now stacked evenly inside their own 400-tall band, and **A-202 now has 0 texts outside its inner border** |
| **`DR-A2-F4`** | **NOT FIXED, recorded only.** On A-301 the dimension text `3500 EFFECTIVE` (x 50860 → 52209) overruns the inner border at x 52166.889 by **42 units, 0.84 mm on paper**. It is `DR-A1`'s and it is still in the margin, not off the sheet. **Moving it ~120 left clears it**; that is not part of what was asked and it is left for the owner to call |

### What DR-A2 did NOT do

**No design value, load, thickness, level, bar, BOQ quantity, rate, date or float changed.**
`SU-01` was **not** re-sized or moved; `SK-01` and `ST-01` were **not** re-sized or moved; `C18`
and `C19` stand as ruled. **No evidence tag was converted, downgraded or deleted.** No `.std`
file was touched and **STAAD.Pro was not run.** `S-06` was **not** edited (see the note above).
**No discipline package was modified** — the only files that change outside the two DXF are this
one, `master/QUICK_STATE.md`, and `DRAWING QAQC/qa_index.json` + `DRAWING_INDEX.md`, both of which
are **regenerated output**: `qa_report_data.py` and `make_index.py` were re-run and the only
difference they produce is A-202's text count **104 → 114** and A-301's **113 → 143**. **The
main staircase is untouched** — 24 risers, 170.8333, 280, 3 flights × 8, total rise 4100, and its
44 entities on A-202 and 23 on A-301 are byte-identical to the previous revision.

**Verified — entity by entity, against the previous revision.** **A-202: 533 → 544**, 11 added,
and **exactly 2** pre-existing entities differ — the `QA1` and `DR-A1` revision-strip lines,
**Y only** (+156 and +337, the `DR-A2-F3` re-stack); **every other entity is byte-identical**.
**A-301: 502 → 625**, 123 added, and **exactly 21** differ, each intended: the **18** that make up
the bottom dimension chain, changed **only** in their Y (−1200 — **no dimension VALUE touched**,
`22000 SHELTER` / `10000 MIN CLEAR` / `4000 SENTRY POST` all unchanged); the two revision-strip
lines, **Y only** (−14 and +37); and note 2's string. Both files pass `ezdxf` audit with
**0 errors**.
`qa_report_data.py` and `make_index.py` were **re-run**: A-202 **114 texts, 0 overlaps, 2
annotations over line work (the same two as before)**; A-301 **143 texts, 0 overlaps, 0 over line
work**; sheet sizes still **A1** and **A0**, so **neither drawing's extents moved**; **the package
is still 80 drawings, 74 PASS.** **K.1b goes from seventeen open items to eighteen** — one new,
`DR-A2-V1`; none closed.

---

## H.36 The master project report — revision PR1 — 13 September 2026

> **PR1 is a DOCUMENT, not a design change.** It changes no dimension, level, load, thickness,
> bar, quantity, rate, date or float; it touches no `.std` file; STAAD.Pro was not run; the main
> staircase is untouched; and **no `[C]`, `[R]`, `[A]`, `[U]` or `[N]` tag is converted,
> downgraded or deleted anywhere in it.**

**What was asked.** A detailed, consistent project report that can act as a master document —
every section in full, with the basic science behind the design considerations, detailed
calculations, and correct citations and IS code references.

**What was produced — all under `Project Report/`.**

| Deliverable | Contents |
|---|---|
| `MASTER_PROJECT_REPORT.pdf` | **89 pages, A4, 19 parts and 4 appendices**, contents list with page numbers, PDF outline bookmarks, running head and foot |
| `Documentation/MASTER_PROJECT_REPORT.md` | **The report SOURCE.** Edit this and re-run the renderer; never edit the PDF |
| `Scripts/report_render.py` | The Markdown-subset typesetter. **It adds no content of its own** beyond the cover, the running head and foot and the paginated contents |
| `Scripts/report_verify.py` | **498 independent recomputations** of the figures the report reproduces |
| `Calculations/REPORT_VERIFICATION_OUTPUT.txt` | Their output, check by check |

**How it differs from `CONSOLIDATED_PROJECT_REPORT.md`** (H.25). That document states the project
once and remains valid as far as it goes. **PR1 adds three things it does not have**: a full
**Part 2 on the engineering science** behind every design decision — shock physics, the SDOF
regime, strain-rate effects, radiation attenuation, buoyancy and effective stress, Winkler
foundations, filtration and CO₂ kinetics, aperture and waveguide theory, bonding inductance;
the **calculations set out in full with every substitution and clause**; and **an executable
verification of its own arithmetic**. It is also current to **RC10 and DR-A2**, which the
consolidated report predates.

> **And that is itself a finding. `PR1-F3`: `CONSOLIDATED_PROJECT_REPORT.md` is now stale on
> three counts** — it states *"thirty-three open items"* against the current **eighteen**,
> *"fourteen standing assumptions"* against **seven still open**, and it predates RC4 to RC10 and
> DR-A2. **It is not edited here.** It is a build-level artefact of exactly the class `RC10`
> (H.34) exists to register, and the same rule applies: **record it, do not silently edit it.**

### The verification pass, and the two differences it found

**498 checks: 494 PASS, 4 differences, 0 unexplained.** Each check recomputes a value from its own
inputs — the formulas are written out again in `report_verify.py`, not copied — and compares the
result with the value the project prints. **A PASS means the printed number follows from the
printed inputs. It is not a design check and not an analysis.**

| Ref | Where | Computed | Printed | Assessment |
|---|---|---|---|---|
| **`PR1-F1`** | **`A.7.8`, underground box wall shear stress.** 525 × 10³ / (600 × 0.8 × 21600) | **0.0506 N/mm²** | **0.063 N/mm²** | **NOT previously recorded.** Both values are negligible **by two orders of magnitude**; *"IS 13920 Cl. 10.4 boundary elements NOT triggered"* holds on either, and **no adopted value depends on it** |
| **`PR1-F2`** | **`B.8.7`, sentry footing F1 at ULS.** e<sub>u</sub> = M<sub>u</sub>/P<sub>u</sub> = 43.9 / 276.8; and the printed expression 276.8/2.25 × (1 + 6 × 0.128/1.5) | **0.159 m** and **186.0 kPa** | **0.128 m** and **190.0 kPa** | **NOT previously recorded.** The footing's steel is governed by **IS 456 Cl. 26.5.2.1 minimum** (720 against 136 mm²/m required) and its depth by **starter anchorage**, so **no bar, spacing or dimension moves** on either figure. One-way shear 0.012 and punching 0.065 against τ<sub>c</sub> 1.369 are unaffected |
| — | The project owner's cost summary | ₹ 2 99 33 306 | ₹ 3 00 33 306 | **ALREADY RECORDED — `R-14` (H.13)**, exactly ₹ 1 00 000 apart. The pass **reproduced a known finding independently**, which is the outcome a check like this is for |

> **`PR1-F1` AND `PR1-F2` ARE RECORDED HERE AND ARE NOT CORRECTED.** Rule **M.11** forbids editing
> a recorded value away, and rule **M.6** forbids resolving anything by inference. `A.7.8` and
> `B.8.7` are left exactly as they stand.
>
> **Both have the same shape, and it is worth naming.** Each is a figure quoted to demonstrate
> that something is negligible or non-governing — a shear stress two orders of magnitude below any
> limit, and a bearing pressure on an element whose steel is a code minimum and whose depth is set
> by anchorage. **Nothing downstream is sensitive to either, which is precisely why both survived
> every previous pass.** They are offered to the owner as a ruling item, not asserted as errors:
> **whether to restate them, and to what, is the owner's call.**

### What PR1 did NOT do

**No design value, evidence tag, quantity, rate, date or float changed. No `.std` file touched and
no analysis run. No drawing edited and no generator re-run. No open item closed, opened,
narrowed or reclassified** — `K.1b` still holds **eighteen** open, `K.2` still holds **seven**.
**No package artefact edited**, including the six `RC10` registers and `CONSOLIDATED_PROJECT_REPORT.md`.
**The main staircase is untouched** — 24 risers, 170.8333 mm riser, 280 mm tread, 3 flights × 8,
total rise 4 100 mm.

## H.37 The master project report — revision PR2 — 13 September 2026

> **PR2 is a DOCUMENT, not a design change.** It changes no dimension, level, load, thickness,
> bar, quantity, rate, date or float; it touches no `.std` file; STAAD.Pro was not run; no drawing
> was edited and no generator re-run; the main staircase is untouched; and **no `[C]`, `[R]`,
> `[A]`, `[U]` or `[N]` tag is converted, downgraded or deleted anywhere in it.**

**What was asked.** Add drawings and layout wherever they aid understanding; **write the report as
though the project had always been in its latest form**; and cover in detail the bill of
quantities, the cost estimate, the programme and its critical path activities, works management,
water, sewage and drainage, the environmental management plan, the M35 and M30 mix design
calculations, HVAC, and a section on openings, escape hatches and blast doors — with the soil
report and the site maps included in site selection.

**What was produced — all under `Project Report/`.**

| | |
|---|---|
| `MASTER_PROJECT_REPORT.pdf` | **151 pages · 25 parts · 4 appendices · 57 figures · 916 kB** |
| `Documentation/MASTER_PROJECT_REPORT.md` | The report source — **6 720 lines, 398 kB** (PR1: 4 796 lines, 285 kB) |
| `Documentation/00_README.md` | Rewritten for PR2 |
| `Scripts/report_figures.py` | **NEW — the 57 drawn figures**, plus the bounds checker |
| `Scripts/report_render.py` | Gains `<!-- FIG: -->` and `<!-- LOF -->`, a figure register and a list of figures |
| `Scripts/report_verify.py` | **559 checks** (PR1: 498), including three new sections |
| `Calculations/REPORT_VERIFICATION_OUTPUT.txt` | **553 PASS · 6 recorded differences · 0 unexplained fail** |

### H.37.1 The voice

**PR1 told the project's story including its revision history. PR2 states the design as it stands,
in the present tense, as though it had always been in this form.** Revision identifiers — `M1`,
the `C`-series conflicts, `RC1`–`RC10`, `QA1`/`QA2`, `SP-B1`/`SP-B2`, `BS1`, `DR-A1`/`DR-A2`,
`MS1`/`MS2`, `ERR-1`, `WM1`–`WM3`, `FS1`/`FS2`, `CAM1`/`CAM2`, `EM1`, `EL1`, `SG1`/`SG2`, `HV1`,
`DR1` — are **out of the design narrative**.

**Every engineering reason is kept.** A reason is part of a design; a revision number is not. Where
a reader would otherwise ask *why is this wall 400 and not 200*, the answer is given as a reason,
in the present tense, as part of the design.

> **Nothing is lost, and the rule against overwriting a revision is not breached.** The full
> history moves to the report's **Appendix D — Traceability: decisions, conflicts and revision
> history**, which carries the conflict table, the ruling-by-ruling register and the revision list
> intact. **The master's Part H remains the ledger and is unchanged by PR2 except for this
> section.** Live register keys — `SG-V2`, `RC4-V1`, `EM-V3`, `DR-A2-V1`, `WM-V6` and the rest —
> are **kept in the narrative**, because an open item is part of the current state, not of the
> history.

### H.37.2 The figures

**Fifty-seven**, generated by `report_figures.py` from `GEOM`, `LEV` and `COVER` constants held in
**project coordinates**, so a dimension changed there changes every figure that uses it and no
figure can drift from the geometry it is drawn from. **Nothing is traced and nothing is measured
off a picture.**

> **They are NOT the issued drawings, and the module says so in its own docstring.** No title
> block, no revision box, no bar mark; drawn at reading scale rather than at a plotting scale;
> **never to be used for setting out or fabrication.** They are also **NOT** reconstructions of
> the seven S-series sheets absent from the workspace (`I.1`), and **no absent drawing is
> fabricated by PR2.**
>
> **No photograph, satellite image, contour sheet or survey drawing of the plot exists in this
> project, and PR2 creates none.** The site figures are schematic, drawn from the project's own
> coordinate system and from relationships the record states, and the report says so in Part 4.1
> before the first of them.

**A second gate was added alongside the numerical one.** `check_all()` walks every drawing and
reports any line, rectangle, circle, polygon **or string** falling outside its own frame or past
the 174 mm text measure — reportlab does not clip, so anything drawn outside a figure silently
bleeds onto the following flowable. **The gate is zero and it is met.**

### H.37.3 What PR2 added to the report

| Part | Content |
|---|---|
| **4** | The **full soil report** — 11 trial pits with every stratum and SBC, 6 soil samples with LL/PL/PI/FSI/OMC/MDD/φ, 6 rock cores soaked and unsoaked, the 12-month meteorological record, and the site figures |
| **6.5** | **Concrete mix design, M35 and M30**, to the IS 10262:2019 method — target mean strength, water content, w/c, absolute-volume proportioning, and the IS 456 Table 5 durability checks |
| **12** | **Openings, blast doors, escape hatches and closures** — the register, the four duties, both doors, D-05, both shaft heads, the stair void and the re-entrant corner |
| **2.8** | **EMP SCIENCE, deepened** — the Compton-current mechanism that makes a HEMP and why it puts energy to a gigahertz; the three coupling paths and why **conducted penetration** decides the answer; why the 10 kHz – 1 GHz band has that shape; and **Schelkunoff's A + R + B for a solid shield**, with the skin-depth arithmetic showing that **about 1 mm of steel is 80 dB at the hardest frequency in the band** |
| **18** | **EMP PROTECTION DESIGN, deepened** — a design basis table; the panel-versus-seam argument; **the honeycomb waveguide panel designed in full, with the array correction (`PR2-F2`)**; bonding inductance and the five bonding rules; earthing against 1 000–10 000 Ω·m basalt; and the IEEE Std 299 acceptance survey set out as a procedure with its hold point |
| **6.5** | **MIX DESIGN, rewritten as the IS 10262:2019 Annex A procedure** in the code's own step order, A-1 to A-11 — stipulations, test data, target strength, air content, w/c, water content, cement content, aggregate proportions, absolute-volume mix calculations, trial proportions with a **two-fraction coarse aggregate split and a batch-by-the-bag table**, and the **SSD / field-moisture correction stated as a procedure because both its terms are `[N]`** |
| **16.7** | **THE WATER, SEWAGE AND DRAINAGE OPERATING PROCEDURE — NEW.** What happens to every stream in each of the five operating modes, mode by mode: peacetime, the changeover on warning, closed mode and the order to work in if the sump rises with no power, the airlock purge, and the recovery sequence after the all-clear |
| **15–19** | HVAC and CBRN · water, sewage and drainage · electrical and power · EMP protection · fire and life safety, **each now a part in its own right** (PR1 carried them as five sections of one part) |
| **21** | **Works management** — the bill section by section, the cost estimate by package and by head, the programme, the critical path, the 18 milestones, procurement, the 16 hold points, resources and risk |
| **22** | **The environmental management plan — NEW.** No environmental management plan exists in this project; PR2 **derives** one from quantities and methods the project confirms, and names every statutory gap as `[N]` rather than inventing a consent condition |
| **Appendix D** | Retitled **Traceability**, and now carries the conflicts, the rulings and the revision history that left the narrative |

**Renumbering.** Parts 12→13, 13→14, 15→20, 17→23, 18→24, 19→25, with every cross-reference in the
source resolved. The old Part 14 (services) became Parts 15 to 19.

### H.37.4 The verification pass

```
CHECKS EXECUTED                 559        (PR1: 498)
PASS                            553
KNOWN / RECORDED difference       6
UNEXPLAINED FAIL                  0
```

Three sections are new: **§21 concrete mix design** — both target mean strengths and which branch of
IS 10262 Cl. 5.2 governs, the water content at each slump and after the admixture reduction, the
cement from the water/cement ratio, **the resulting free w/c against the IS 456 cap and the cement
against both the minimum and the shrinkage maximum**, the coarse aggregate fraction and its
congestion correction, the absolute-volume closure on 1.000 m³, both aggregate masses, both fresh
densities and both mixes by mass; and **§22 programme and cost** — the calendar span and the
Sundays in it, the six-day working count, the activity total, the basic cost re-summed from its
five priced parts, each part's share, and the final project cost re-derived from the seven
percentage heads; and **§23 EMP shielding physics** — skin depth in steel at three decades and the
thickness that alone gives 80 dB, the absorption of a 2 mm skin and the plane-wave reflection term,
the honeycomb TE11 cutoff and its 32 L/d attenuation, the cell area, **the number of cells in a
square metre and the array correction on them**, and the hatch leaf force and flat-plate moment at
ν = 0.30 for steel.

### H.37.5 `PR2-F1` — one new difference, recorded and NOT corrected

> **The programme states 384 calendar days, a six-day working week and five date-certain national
> holidays, and 326 working days.** A raw Monday-to-Saturday count of that span gives 330 days;
> less five holidays, **325**. The difference is **one day**.
>
> **It is far more likely a property of how a scheduling tool counts a finish milestone than an
> error**, and **no date, duration or float in this project depends on it.** It is recorded here
> because a one-day difference reported is worth more than a one-day difference rounded into
> agreement. **Offered to the project owner as a ruling item, not asserted as an error.**

### H.37.5a `PR2-F2` — the honeycomb margin, recorded and NOT corrected

> **The EMP package states a honeycomb waveguide panel margin of +53 dB.** That is the attenuation
> of **one** 6 mm × 25 mm cell — `32 L/d` = 133.3 dB against the 80 dB requirement — with **no
> array correction applied.**
>
> A panel is an array. A hexagonal 6 mm cell has an area of 31.18 mm², so **one square metre holds
> about 32 075 cells**, and the classical `−10 log₁₀(n)` correction for `n` identical apertures in
> one screen is **−45.1 dB**. The net is **88.3 dB**, and the margin is **+8.3 dB, not +53.**
>
> **The panel still PASSES.** What changes is **a procurement requirement, not a design value**:
> require a certified attenuation curve for the panel **as built**, not for one cell. Eight
> decibels is a margin a bad gasket eats; fifty-three is not.
>
> **Recorded, not corrected.** The project's +53 dB is reproduced in the report and the array term
> is offered alongside it. **No dimension, load, thickness, bar, quantity, rate, date or float
> moves on it.** Offered to the project owner as a ruling item.
>
> The same caveat already stood against the reinforcement cage figures, where the array correction
> is likewise not applied — H.37 records it there as one of three reasons every cage figure in
> this project is an upper bound.

**`PR1-F1` and `PR1-F2` stand unchanged** (H.36), and the owner's ₹ 1 00 000 cost-summary
difference is still reproduced on both sides as `R-14` (H.13).

### H.37.6 The mix design is a trial mix, and it is tagged as one

> **No mix proportion is confirmed anywhere in this project, and PR2 converts nothing.** What Part
> 6.5 produces is a **trial mix to the IS 10262 method**, with every assumed input tagged `[A]` —
> target slump, superplasticiser water reduction, specific gravities, grading zone, the congestion
> reduction — and every unavailable input tagged `[N]`: the aggregate source and its grading, the
> admixture products, the supplier's standard deviation, and the trial cubes.
>
> **The confirmed durability limits are the constraints it is checked against**, not results it
> produces: M35, free w/c ≤ 0.45, minimum cement 340 kg/m³, and both are satisfied at 0.395 and
> 400 kg/m³.
>
> **It lands independently on the same 400 and 360 kg/m³ the bill's procurement take-off already
> assumes** (`M-01`). That is a **consistency check, not a confirmation** — both remain `[A]`, and
> both are replaced the day a laboratory trial is run under QA/QC item `Q-06`.

### H.37.7 The environmental management plan is derived, not reported

> **No environmental management plan, environmental impact assessment, consent, clearance or
> monitoring schedule exists in this project.** Part 22 **derives** a plan from quantities and
> methods the project does confirm — 1 338 m³ of excavation, 994 m³ of rock broken without
> blasting, 1 113.937 m³ re-used on site, 194.2 t of cement, 450 L/day of foul effluent, a
> tanker-only decon stream, a 275 L bund — and **names every statutory gap rather than filling
> it.**
>
> **Nothing statutory is invented.** No consent condition, limit value, discharge standard, noise
> limit or receptor distance is stated, because none exists. The Part says so item by item, and
> ends by saying plainly that it **is not a substitute for a construction environmental management
> plan as a contract document.**
>
> One operational liability is raised there that the project had nowhere else: **spent CBRN
> filters are hazardous waste, produced for the life of the structure, and the project holds no
> change-out interval, no disposal route and no cost for them.**

### What PR2 did NOT do

**No design value, evidence tag, quantity, rate, date or float changed. No `.std` file touched and
no analysis run. No drawing edited and no generator re-run. No open item closed, opened, narrowed
or reclassified** — `K.1b` still holds **eighteen** open, `K.2` still holds **seven**. **No package
artefact edited**, including the six `RC10` registers and `CONSOLIDATED_PROJECT_REPORT.md`. **No
absent drawing or generator fabricated.** **The main staircase is untouched** — 24 risers,
170.8333 mm riser, 280 mm tread, 3 flights × 8, total rise 4 100 mm.

Evidence-tag counts in the report source moved **only upwards**, which is what adding content with
no deletion looks like: `[C]` 94 → 124, `[R]` 22 → 25, `[A]` 55 → 72, `[U]` 4 → 7, `[N]` 30 → 73.

---

## H.38 The bill priced from the Maharashtra SSR 2022-23 — revision WM4 — 15 September 2026

The project owner supplied **`SSR 22-23 MH (1).pdf`** — the Government of Maharashtra,
Public Works Department **State Schedule of Rates for 2022-23**, approved by Government
Circular RADASU-2022/PR.KR.12/NIYOJAN-3 dated 25 July 2022, effective from that date,
624 pages. **WM4 prices the Works Management bill from it.**

This closes a gap the project has carried since WM1. Part G's "not implemented" table
said it in as many words: *"Rates come from the MES SSR. No item number could be verified
from the material available, and inventing one would put false authority on a document an
executing engineer might rely on."* An item number can now be verified for every civil
line in the bill, so the bill is priced. **That line in Part G has been amended to say so.**

### H.38.1 What changed, and what did not

**NOT ONE QUANTITY MOVED.** WM1's 90 measured items are used exactly as measured. Where a
WM1 line had to be split to reach two different SSR items — the excavation by depth band,
the headhouse walls against its roof, the sentry beams across two levels, the painting
into internal and external — **the parts sum back to the WM1 figure exactly**, and the
audit checks each one. No design value, load, thickness, bar, level, date or float
changed. No `.std` file was opened and no analysis was run. **The main staircase is
untouched** — 24 risers, 170.8333 mm riser, 280 mm tread, 3 flights × 8, 4 100 mm rise.

### H.38.2 The result

| | Lines | Amount |
|---|---:|---:|
| Priced at a **published SSR item** | 53 | ₹ 13,823,328 |
| Priced on a **stated assumption** `[A]` | 21 | ₹ 1,459,950 |
| **Included** in another rate — measured, not payable twice | 15 | — |
| **NOT PRICED** — no specification, or no SSR item | 25 | — |
| **TOTAL OF ITEMS** | **114** | **₹ 15,283,278** |
| **ESTIMATED COST**, after the SSR and owner recapitulation heads and GST at 18 % `[A]` | | **₹ 20,739,408** |

**That figure is the CIVIL works only, and it is a declared lower bound.** The blast
doors, exit hatches, blast valves, NBC collective protection trains, EMP Zone 2
enclosure, standby generator, sump pumps and commissioning **have no SSR item**, and none
is invented. Neither do the waterstops, the spiral stair, the flooring, window W1, the
berm or the camouflage — each for a reason recorded on its own line.

### H.38.3 Four things the schedule itself settled

| | |
|---|---|
| **Overheads and profit are already in the rate** | SSR General Notes: *"For labour amenities and all other overhead charges, **10 % provision is considered in Rate Abstract**. In addition, **10 % provision for Contractor's Profit** is also considered separately"*, plus 1 % labour cess. The owner's own estimate adds 10 % OH&P **on top** of its rates; against SSR rates that is a double count, and WM4's recapitulation does not make it. The three heads are listed explicitly as **NOT ADDED**, with the clause |
| **Formwork is already in the concrete rate** | Every SSR concrete item reads *"including **steel centering, formwork**, cover blocks ... **(excluding reinforcement and structural steel)**"*. So `F-01` (1 057.743 m²) and `F-02` (104 m²) stay as measured control figures at **nil**, and reinforcement is billed separately at SSR **26.33**. The same logic retires the sentry masonry's bricks, cement and sand (inside 27.05), the cement and aggregate procurement volumes, and **`W-05`, which is the same protection screed as `B-screed` measured in m² instead of m³** — 102.889 × 0.100 = 10.289 |
| **A grade the schedule does not publish is derived by the schedule's own rule** | SSR pardi (wall) and staircase waist slab stop at M-25; the box is M-35. General Notes Section B: *"derived by **adding difference in standard cement consumption** in relevant SSR item's rate"*. Standard consumption M25 7.50 / M30 8.00 / M35 8.25 bags per m³, cement ₹6 000/M.T. **The formula was checked against the SSR's own published inter-grade steps in four item families before it was used** — it gives 183.32 where the SSR prints 183/184, and 91.66 where it prints 91/92. So the M-35 wall rate is ₹15,750 + ₹275 = **₹16,024.97/m³** |
| **Excavation below 3.0 m attracts a depth increase** | *"3.0 m to 4.50 m depth add 20 %; 4.5 m to 6.0 m depth add 30 %; depth beyond 6.0 m — extra percent to be decided by concerned Superintending Engineer."* The shelter goes to (−)6.800, so the bulk excavation is billed in **six depth bands** reproducing the WM1 quantities exactly: soil 295.20 + 49.20 = 344.40 against E-02a's 344.4; rock 246.00 + 295.20 + 295.20 + 157.44 = 993.84 against E-02b's 993.84 |

### H.38.4 The rock is broken, not blasted — and that decides the rate

`WM_CONSTRUCTION_METHODOLOGY.md` and risk `S-02` both say it: *"Rock is removed by
HYDRAULIC BREAKER, not by blasting ... controlled blasting would require a vibration
regime the project has not specified."* So **SSR 21.20** — hard rock by chiselling,
wedging and line drilling, ₹1 307 — governs, and the schedule's three blasting items
**21.17, 21.18 and 21.19** at ₹869, ₹1 033 and ₹1 322 **do not apply to this project at
all**. The project's own written methodology, not the estimator, picked the item.

### H.38.5 The owner's rates against the schedule

H.15 recorded of the owner's priced bill: *"No cost was re-estimated, no rate was checked
against a market or a schedule of rates."* WM4 is that check. **Nothing in their bill is
edited** — their quantities and their rates are reproduced as supplied, with the SSR rate
beside them.

Of 37 lines, **21** have an SSR item that can stand against them:

| | Amount |
|---|---:|
| Owner's rates, comparable lines | ₹ 10,986,464 |
| SSR 2022-23, the same lines | ₹ 14,454,895 |
| **Difference** | **₹ 3,468,431  (+31.6 %)** |

The gap is concentrated in three lines and each has a reason. **R.C.C. wall casting** is
the largest: the owner prices every grade at one blended ₹8 640/m³, which is close to the
SSR's **raft** rate and is being applied to **walls**, where the SSR charges ₹16 025
because wall formwork is what the item is dear for. **Rock excavation** is second: ₹850
blends murum and basalt and carries no depth increase. **Reinforcement** is third:
₹78 000/t against ₹89 703/t.

**A rate below schedule is a commercial position, not an error.** What did not exist
before was the comparison.

### H.38.6 Two RC4 items that were NOT PRICED now have a rate

`RC4-01` and `RC4-02`, the strip-and-replace of the expansive CH horizon under the entry
stairwell raft (8 m³ each), were recorded by the RC4 ruling as **"[A] NOT PRICED"**
because no rate existed. One exists now: SSR **21.02** at ₹207/m³ and **21.37** at
₹599/m³. **The ruling is untouched and the `[R]` quantity tag stays** — only the rate
column is filled. This is not the closure of an open item; it is the supply of a
schedule rate for a quantity the ruling already fixed.

### H.38.7 Seven new open items — `WM4-V1` to `WM4-V7`

None is closed here and none is guessed.

| Ref | What it is | What WM4 did |
|---|---|---|
| **`WM4-V1`** | Excavation below 6.0 m depth — the SSR sets no percentage | Priced at +30 % as a DECLARED LOWER BOUND, tagged [A].  Every extra 10 percentage points is about Rs 21 800 on these two lines. |
| **`WM4-V2`** | Brick class — SSR grading against IS 1077 | Priced at 27.05, second class in CM 1:6 in superstructure, which is the only published superstructure wall item and matches the specified mortar. |
| **`WM4-V3`** | Lintel SP-06 measures a superseded section | WM4 prices the quantity AS MEASURED and does not re-measure it.  The difference is 0.51 against 0.4845 m3, about 5 %, or Rs 322. |
| **`WM4-V4`** | No district cost index or circle variation applied | State rates are used exactly as published.  No index, uplift or discount is applied anywhere. |
| **`WM4-V5`** | GST rate is not fixed by the schedule | 18 % is used, tagged [A], as a single parameter cell in the workbook so another rate can be tested by changing one number. |
| **`WM4-V6`** | Tanking specification substituted | Priced at 51.114 because the MATERIAL matches — a five-layer polymeric membrane on a 90 micron HMHDPE core.  The shahabad alternative is carried in the workbook at Rs 1 286 / Rs 1 338 so the swap can be costed: it would add about Rs 400 000. |
| **`WM4-V7`** | The protective plant is outside the schedule entirely | Listed in bill section L at nil.  The owner's own bill prices them from vendor figures at about Rs 1.05 crore; those figures are NOT SSR rates and WM4 does not adopt them. |

`WM4-V1` is the one with money on it: 157.44 m³ of rock between (−)6.000 and (−)6.800
plus the 9.477 m³ sump pit below it sit past the SSR's last defined band, priced at the
4.5–6.0 m band's +30 % as a **declared lower bound**. Each further 10 percentage points
is about ₹21 800.

### H.38.8 What was verified, and how

* **18 automated consistency checks, 18 pass** — `WORKS MANAGEMENT/QAQC/WM4_SSR_VERIFICATION.txt`.
  They prove every split line sums back to its WM1 quantity, that the reinforcement net
  weight is exactly the WM1 order quantity ÷ 1.05 (73.647 against 73.648 t), that no line
  carries both a rate and an "included" marker, and that the main staircase quantity is
  unchanged.
* **Every rate re-read from the PDF a second time** against the raw text of its page.
  30 of 33 matched automatically; three were checked by hand and **two were corrected**
  (21.40 from a mis-read 7 695 to **1 454**; 39.50 from 5 716 to **5 700**). Neither
  correction touches a priced line.
* **All 203 workbook formulas evaluated** and shown to reproduce the bill —
  `Scripts/wm4_verify_xlsx.py`. LibreOffice cannot open a file in this environment, so
  the formulas were evaluated directly in Python rather than by recalculation, and the
  workbook carries `fullCalcOnLoad` so Excel computes them on open.

### H.38.9 What WM4 did NOT do

**No design value, load, thickness, bar, level, evidence tag, BOQ quantity, date or float
changed.** No drawing, model or `.std` file was touched and **no analysis was run** —
this is a rating exercise, and editing or reading a file is not running an analysis. **No
open item was closed, narrowed or reclassified**; seven were added. **No `[A]` or `[N]`
tag was upgraded.** **No rate was invented** — 25 lines are NOT PRICED and stay
that way. **No district cost index was applied** (`WM4-V4`). **The owner's bill and
`USER_SOURCE/` are untouched.** **WM1, WM2 and WM3 are preserved unaltered** under M.11.
**The main staircase is untouched.**

### H.38.10 Files

| File | What it is |
|---|---|
| `WORKS MANAGEMENT/Cost/WM4_Underground_Shelter_BOQ_Cost_Estimate_SSR_2022-23.xlsx` | **The workbook** — 11 sheets, every amount a live formula |
| `WORKS MANAGEMENT/Cost/WM4_BOQ_AND_COST_ESTIMATE_SSR.md` | The narrative |
| `WORKS MANAGEMENT/Cost/WM4_BOQ_PRICED_SSR_2022-23.csv` | The priced bill, 114 lines |
| `WORKS MANAGEMENT/Cost/WM4_SSR_RATE_LIBRARY.csv` | Every SSR item used, in the schedule's own wording, with its printed page |
| `WORKS MANAGEMENT/Cost/WM4_COST_SUMMARY.csv` · `WM4_OWNER_BILL_VS_SSR.csv` · `WM4_OPEN_ITEMS.csv` · `WM4_RATE_DERIVATION.txt` | Recapitulation · the owner's bill re-rated · the seven open items · every derived rate's arithmetic |
| `WORKS MANAGEMENT/QAQC/WM4_SSR_VERIFICATION.txt` | The 18 checks and the rate-extraction audit |
| `WORKS MANAGEMENT/Scripts/wm4_ssr_library.py` · `wm4_bill.py` · `wm4_owner_compare.py` · `wm4_build.py` · `wm4_doc.py` · `wm4_verify_xlsx.py` | The generators.  `wm_build_all.py` now runs the last two as steps 8 and 9 |

---

## H.39 A2 structural reinforcement presentation sheets — revision SR1 — 16 September 2026

The owner supplied a five-sheet **Revit A2 architectural set** (`ARCH001 … ARCH005`,
`Project1.pdf`) and asked for **two more sheets in the same series, numbered SHEET 06 and
SHEET 07**, carrying the structural reinforcement detailing of the underground structure.

**NOTHING IN PARTS A, B, D, E, F OR L CHANGES.** No dimension, level, thickness, load,
capacity, bar size, spacing or bar mark moved. No `.std` file was opened and no analysis
was run. **The main staircase is untouched** — 24 risers, 170.8333 mm riser, 280 mm tread,
3 flights × 8, 4 100 mm total rise, well 200, waist 200, headroom 2533. SR1 is a **drawing
production revision only**.

### H.39.1 What was produced — all under `Presentation Sheets/`

| Sheet | Drawing No. | Title | Views |
|---|---|---|---|
| **SHEET 06** | **STR006** | STRUCTURAL REINFORCEMENT DETAILING — ROOF SLAB & MAT FOUNDATION | V1 roof slab reinforcement plan 1:100 · V2 roof slab longitudinal section A-A 1:100 (cut Y 2050) · V3 mat foundation reinforcement plan 1:100 · V4 mat foundation longitudinal section B-B 1:100 (cut Y 2050) |
| **SHEET 07** | **STR007** | STRUCTURAL REINFORCEMENT DETAILING — 600 SHEAR WALL & MAIN STAIRCASE | V1 600 shear wall vertical section 1:30 · V2 600 shear wall part plan / horizontal section 1:25 · V3 main staircase reinforcement plan 1:40 · V4 main staircase longitudinal section C-C 1:40 (cut on flight A at X 15900) |

Tables carried: roof slab and mat element schedule · bar-mark schedule, roof slab 900
(23 marks) · bar-mark schedule, mat foundation 600 and sump pit (13 marks) · wall schedule
(W1–W4 detailed, W5 / W6 / W7 / W8 scheduled and cross-referenced) · bar-mark schedule,
600 perimeter shear walls (6 marks) · main staircase element schedule · bar-mark schedule,
main staircase (6 marks) · NBC 2016 Part 4 stair geometry check · design-basis and
construction-requirement panels on both sheets.

### H.39.2 The sheet standard — reverse-engineered, not estimated

Every frame constant was extracted from the **vector content** of the supplied Revit PDF,
so STR006 / STR007 sit on the same frame as ARCH001…ARCH005:

```
A2 landscape 594 x 420, drawn in PAPER MILLIMETRES, plotted 1:1
outer border 27.0, 19.1 -> 567.0, 400.9      inner frame 38.8, 30.9 -> 555.2, 389.1
title-block divider x = 464.3 ; panels x 467.0 .. 552.4, four stacked boxes
    A 314.5..386.4 (rule 332.7, "NOTES")   B 193.4..311.8 (notes)
    C 130.3..190.6 (title)                 D 33.6..128.2 (rules 40.9 54.6 61.8 69.1 76.4 83.6 96.9)
```

**Declared deviation SR1-X1.** Part E.3.1 fixes AutoCAD R12 ASCII for the S-01…S-08
output set. **Those sheets are not touched.** STR006 / STR007 are written at **AC1024**
so they carry native `DIMENSION`, `HATCH` and `ELLIPSE` entities — the same deviation the
`Structural CAD` R-series already declares as its X1.

**Colour, by instruction: dark only, mostly black.** Four ACI colours are used and no
others — **7 black** (all line work, text, dimensions, tables, title block), **8 dark
grey** (hatch, soil, work beyond), **1 dark red** (main reinforcement and trimmers),
**5 dark blue** (links and distribution). Verified: the colour set of every layer actually
used on both sheets is exactly `{1, 5, 7, 8}`.

### H.39.3 Provenance of every value drawn

* Geometry, levels, thicknesses, loads and capacities — **Parts A.3, A.4, A.5, A.6,
  A.7.3, A.7.8, B.1, B.3, B.4, B.4.1, B.5, F.1, F.2**, read through
  `Structural CAD/Scripts/sc_proj.py`.
* **Every bar mark is read from `Structural CAD/Scripts/rebar_data.py`.** Both bar-mark
  schedules are generated from it and the tags on the views quote nothing else, so a mark
  cannot appear on a view without a schedule entry. Marks used: `S01A…S16` (roof),
  `F01…F13` (mat and sump), `W01…W06` (600 walls), `ST01…ST06` (main staircase).
* Nothing is invented, and no `[UNRESOLVED]`, `[ASSUMED]` or `[NOT AVAILABLE]` item was
  resolved. STR006's design-basis panel names **A2** (design GWT), **A4** (k<sub>s</sub>
  at both bounds), **M1** (no STAAD result exists for any underground model) and **P3**
  (blast capacity not demonstrated) on the face of the drawing.

### H.39.4 SR1-F1 — the IS 13920 request, answered honestly on the drawing

**The request asked for the roof slab and mat to be detailed *"as per IS 13920"*. They are
not, and they should not be — so the sheets say what governs instead of implying a code
that does not.** Both title blocks carry note 6 / 7 and both design-basis panels repeat it:

* the box is designed to **IS 456:2000** with **IS 4991:1968** blast actions and
  **IS 3370 (Pt 2)** crack control; seismic to **IS 1893 (Pt 1):2016**;
* **IS 13920:2016 has been checked for the box and does not govern** — A.7.8 gives
  A<sub>h</sub> 0.075, V<sub>b</sub> 1050 kN, 525 kN per long wall, τ = **0.063 N/mm²**, so
  **Cl. 10.4 boundary elements are NOT triggered**, and no ductile-detailing clause changes
  any bar on either sheet;
* **the IS 13920 ductile detailing in this project is carried by the sentry post frame**
  (B.8, F.4) — B1 / B2, C1 with T10 confining hoops at 85, SCWB to Cl. 7.2.1 — **and that
  frame is not on these two sheets.** A future sheet **STR008** would carry it.

No bar was changed to chase the request, and no IS 13920 clause number was put on a bar it
does not govern. **`SR1-F1` is a finding, not an open item: nothing is outstanding.**

### H.39.5 Verification actually performed

| Check | Result |
|---|---|
| DXF structure — `ezdxf.readfile`, entity census, layer declaration | Both files open; **no undeclared layer** on either |
| Geometry inside the sheet | Both extents exactly `27.0, 19.1 → 567.0, 400.9` — the drawn frame. **Nothing outside the border** |
| Colour policy | Layer colours actually used = `{1, 5, 7, 8}` on both sheets. **No light colour anywhere** |
| Drafting QA — `DRAWING QAQC/Scripts/dxfqa.py` | **0 text overlaps on STR006, 0 on STR007.** One `outside_inner` item on each: the rotated date stamp outside the frame, which is where ARCH001…ARCH005 put theirs |
| Clash QA — `modelqa.py`, `panelclash.py` | 0 text-over-hard-geometry, 0 geometry-inside-panel on both |
| Project drawing index | Re-run. 82 drawings, **STR006 PASS, STR007 PASS** |
| True-size plot | Both export to a **594 × 420 mm** vector PDF at 1:1 |
| Bar-mark cross-check | Every mark tagged on a view exists in `rebar_data.MARKS` — both schedules are generated from it |
| Main staircase | **Unchanged.** 24R at 170.8333 / 280, 3 × 8, rise 4100, well 200, waist 200, headroom 2533, landings (−)4.7333 / (−)3.3667, arrival (−)6.100 = the mat surface |

**STAAD.Pro was not run, and no analysis was performed.** This revision drew two sheets.

### H.39.6 Registration with the QA tools — the H.25 rule, obeyed

`CLAUDE.md` requires a new drawing package to register itself. Done:

* `qa_report_data.py` — `("Presentation Sheets/DXF/", "STRUCTURAL - A2 presentation
  sheets")` added to `DISCIPLINE`; **`A2` added to `sheet_size()`**, including the
  540 × 381.8 inset Revit sheet frame this series uses; `STR006` / `STR007` added to
  `TITLE_OVERRIDE`, because the Revit title block stacks the title over five lines and
  there is no single text for `title_of()` to read.
* `make_index.py` — `STRUCTURAL - A2 presentation sheets` added to `ORDER`.
* Both re-run; `DRAWING_INDEX.md` and `qa_index.json` regenerated.

**One cosmetic gap, recorded not hidden:** the index's `Scale` column reads `-` for both
sheets. `scale_of()` only finds a scale when the value sits in the same text as the word
"SCALE"; this series follows the Revit title block, which puts the label `Scale` and the
value `1 : 100` / `As indicated` in two separate cells. The title block is correct; the
index reader cannot see it. `scale_of()` was **not** changed, because it is shared with
the other 80 drawings.

### H.39.7 Not implemented, and why

| | |
|---|---|
| **W5, W6 / W7 and W8 drawn** | The request was for **the 600 shear wall only**. W5 200, W6 / W7 400 and the W8 partitions are **scheduled** on STR007 so the sheet cannot be misread, and cross-referenced to `R-202`. They are not drawn |
| **Sentry post frame (the IS 13920 element)** | Out of the requested scope. Would be a new sheet **STR008** — B1 4-T16 / 2-T16, B2 3-T20 / 2-T20, C1 8-T16 with T10 confining hoops at 85, F1 1500² × 600 with T12 @ 150 B/W |
| **S-01 … S-08 regenerated** | `proj.py`, `dxflib.py` and `d01_wall.py`…`d08_sentryslab.py` are still absent. Those sheets **cannot** be regenerated and were not touched |
| **Pressure-relief plug positions** | Master B.3 requires 6 No. in the mat but records no positions. STR006 states the requirement in its construction-requirements panel and **draws no plug**, rather than inventing six locations |

### H.39.8 Files

| File | What it is |
|---|---|
| `Presentation Sheets/DXF/STR006_Structural_Reinforcement_Detailing_Roof_Slab_and_Mat_Foundation.dxf` | **SHEET 06** |
| `Presentation Sheets/DXF/STR007_Structural_Reinforcement_Detailing_Shear_Wall_and_Main_Staircase.dxf` | **SHEET 07** |
| `Presentation Sheets/Scripts/a2_lib.py` | The A2 sheet library — frame, Revit-style title block, measured tables and panels, dimensions, rebar aids |
| `Presentation Sheets/Scripts/sheet_data.py` | Every value the two sheets print, in one place, read from `sc_proj` and `rebar_data` |
| `Presentation Sheets/Scripts/s06_roof_mat.py` · `s07_wall_stair.py` | One generator per sheet |
| `Presentation Sheets/Scripts/render_a2.py` · `render_pdf.py` | Visual-QA PNG · true-size A2 vector PDF at 1:1 |
| `Presentation Sheets/README.md` | The package note, including the code-basis statement |

> **A future Claude editing either sheet should edit the generator and re-run it, not edit
> the DXF.** The DXF is a build artefact. `sheet_data.py` is the only place a printed value
> lives, and `rebar_data.py` is still the only place a bar mark lives.

---

## H.40 A2 sentry-post reinforcement presentation sheets — revision SR2 — 16 September 2026

Following SR1, the owner asked for **two more sheets in the same Revit A2 series, numbered
SHEET 08 and SHEET 09**, carrying the **structural reinforcement detailing of the SENTRY
POST** — beam plan / longitudinal section / cross section and column both views on the
first sheet; isolated footing plan and cross section, and slab plan and longitudinal
section, on the second.

**NOTHING IN PARTS A, B, D, E, F OR L CHANGES.** No dimension, level, thickness, load,
capacity, bar size or spacing moved. No `.std` file was opened and **no analysis was run**.
**The main staircase is untouched** — 24 risers, 170.8333 riser, 280 tread, 3 flights × 8,
4 100 total rise, well 200, waist 200, headroom 2533; it does not appear on either sheet.
SR2 is a **drawing production revision only**.

### H.40.1 What was produced — all under `Presentation Sheets/`

| Sheet | Drawing No. | Title | Views |
|---|---|---|---|
| **SHEET 08** | **STR008** | STRUCTURAL REINFORCEMENT DETAILING OF SENTRY POST — BEAMS & COLUMN | V1 first-floor framing plan 1:50 · V2 beam B1 longitudinal section 1:40 · V3 beam B2 longitudinal section 1:40 · V4 sections a-a/b-b (B1), c-c/d-d (B2), 3-3 (C1 confining zone), 4-4 (C1 general) 1:10 · V5 column C1 vertical section, full height (−)1.400 → (+)6.700, 1:25 |
| **SHEET 09** | **STR009** | STRUCTURAL REINFORCEMENT DETAILING OF SENTRY POST — FOOTING & SLAB | V1 slab S1 bottom reinforcement plan 1:40 · V2 slab S1 top reinforcement plan, 400 edge bands + 700 × 700 corner torsion mats, 1:40 · V3 slab S1 longitudinal section 2-2 1:25 · V4 isolated footing F1 reinforcement plan 1:20 · V5 isolated footing F1 section 1-1 1:20 |

Tables carried: beam schedule (B1, B2 detailed; PB scheduled, cross-referenced, not drawn)
· column schedule · bar-mark schedule, beams and column (12 marks) · **IS 13920:2016
compliance table, 14 clauses** · footing schedule · slab S1 element schedule · bar-mark
schedule, footing and slab (8 marks) · **IS 456 Annex D two-way-slab detailing table** ·
declared-detailing-decisions and design-basis panels on both sheets.

**This is the IS 13920 sheet pair of the project.** The box is not a ductile-detailing
element — A.7.8 checks Cl. 10.4 and it is not triggered (τ = 0.063 N/mm²). The sentry post
frame is, and SHEET 08 carries the clause-by-clause compliance table for it.

### H.40.2 Sheet standard and colour — unchanged from SR1

Same frame constants, same Revit-style title block, same AC1024 deviation (**SR2-X1**,
identical in substance to SR1-X1), same four dark ACI colours and no others:
**7 black · 8 dark grey · 1 dark red · 5 dark blue**. Verified on both sheets: the colour
set of every layer actually used is exactly `{1, 5, 7, 8}`.

### H.40.3 Provenance of every value drawn

* Geometry, levels, members, loads and capacities — **Parts A.4.8, A.7.7, A.7.8, B.8.1 to
  B.8.7 and F.4**, collected once in `Presentation Sheets/Scripts/sentry_data.py`.
* **The sentry post is EXCLUDED from `Structural CAD/Scripts/rebar_data.py`** — that file
  says so in its own header, and **it is not changed**. `sentry_data.py` is therefore a
  **separate bar-mark register for the sentry post only**, built to the same rule: a mark
  cannot appear on a view without a schedule entry, and uniqueness is asserted. It imports
  `rebar_data.cut_length` (the project's PBR-1 rule) and `rc_calc` (L<sub>d</sub>, bar
  areas) rather than re-deriving them. Marks: `SB01…SB08` (beams), `SC01…SC04` (column),
  `SF01 / SF02` (footing), `SS01…SS06` (slab).
* Nothing is invented, and **no `[UNRESOLVED]`, `[ASSUMED]` or `[NOT AVAILABLE]` item was
  resolved.** U4 (sentry-post site position, still `[ASSUMED]` after RC4) is named on both
  sheets; neither sheet depends on it — both are detail sheets in the post's own local
  coordinates.

### H.40.4 Declared detailing decisions — the master does not cover these

Four decisions were needed that no master value settles. They are **declared on the face
of both sheets**, in a panel headed *DECLARED DETAILING DECISIONS AND OPEN ITEMS*:

| # | Decision | Why it was needed |
|---|---|---|
| **D1** | **Beam top steel is detailed CONTINUOUS over the full span.** | F.4 schedules "4-T16 top at supports" / "3-T20 top at supports" and gives **no curtailment point anywhere**. Running the bars through is conservative under moment reversal and invents no cut-off. |
| **D2** | **Exterior-joint anchorage:** bars taken to the far face of the confined core (350 − 40 cover − 10 hoop = 300 from the near face) and turned 90° with a leg of L<sub>d</sub> − 300, i.e. **425 for T16 and 625 for T20**, L<sub>d</sub> being IS 456 Cl. 26.2.1 at M30/Fe500 (725 / 906) computed by `rc_calc.Ld_tension`. | The master states **no anchorage detail** for the beam bars. |
| **D3** | **Column verticals are SPLICE-FREE** — one 8 724 mm bar from the footing to the roof. | 8 724 < the 12 000 stock bar (`rebar_data` P-1), so **no lap is required and none is invented**. The bar is then its own starter, which is exactly how B.8.7 checks it: 526 straight + a 128 (8 φ) bend = 654 > L<sub>d,comp</sub> 592. |
| **D4** | **Slab bottom steel:** the 50 % that continues (SS01 / SS03) runs **full length** into the beams; the remainder (SS02 / SS04) stops **0.25 L** short of each support. | B.8.3's own reading of Cl. D-1.4. A bar that runs through certainly extends "to within 0.1 L of a discontinuous edge". |

### H.40.5 Findings and open items raised by SR2 — NONE of them is resolved here

| Ref | Item | Status |
|---|---|---|
| **`SR2-F1`** | **B2 top steel at the ROOF joint — the master contradicts itself.** B.8.6's strong-column-weak-beam table evaluates the **roof** joint with **B2 = 2-T20** (ΣM<sub>b</sub> 98.9, 1.4 × = 138.5 ≤ ΣM<sub>c</sub> 101, "marginal"). F.4 schedules **3-T20 top at supports** for B2 and **does not distinguish level**. With 3-T20 at the roof, 1.4 ΣM<sub>b</sub> = **195.7 > ΣM<sub>c</sub> = 101** and **IS 13920 Cl. 7.2.1 FAILS at that joint**. Both statements cannot be true. **Consequence: SHEET 08 details the FIRST-FLOOR frame only**, where B.8.5 and F.4 agree on 3-T20; the roof frame is cross-referenced and is **not detailed**. | **UNRESOLVED — ruling required** |
| **`SR2-V1`** | **Plinth beam PB has no link detail.** F.4 gives 250 × 400, cover 30, d 354, 3-T12 top + 3-T12 bottom. **No link size or spacing exists anywhere in the project.** PB is scheduled on STR008 and is **not detailed**. | **[NOT AVAILABLE]** |
| **`SR2-V2`** | Beam-bar anchorage — see **D2**. A declared detailing decision, not a master value. | OPEN, declared |
| **`SR2-V3`** | Beam top-steel curtailment — see **D1**. A declared detailing decision, not a master value. | OPEN, declared |
| **`SR2-V4`** | **Footing top level (−)1.400** is the founding level (−)2.000 plus the 600 thickness. The master states the **founding level only**. | **[RECONSTRUCTED]** — confirm against the setting-out before F1 is cast |
| **`SR2-V5`** | **No blinding or levelling course under F1** is stated anywhere in the master, and **none is drawn**. | **[NOT AVAILABLE]** |
| **`SR2-V6`** | **IS 13920 Cl. 8.1 also asks for confining reinforcement to continue INTO the footing.** F.4 states confining steel "500 from every joint face, top and bottom of every column, and through the joint" and stops there. The master's rule is applied **as written** and **no footing embedment is drawn**. | **UNRESOLVED — refer before the footings are cast** |
| **`SR2-F2`** | **QA finding on the EXISTING sheet STR007 (SR1), not on the new sheets.** Its two note panels are set at **1.49 mm** text, below the package's own `MIN_TXT_H` of 1.70 mm declared in `a2_lib.py`. 53 lines are affected. **STR007 is NOT changed by SR2** — the finding is recorded, not acted on, because SR1 is a released revision and the instruction that commissioned SR2 does not cover it. | **OPEN — reported, not fixed** |

> **`SR2-F1` is the significant one.** It is a **live IS 13920 Cl. 7.2.1 question about a
> real joint**, not a drafting matter, and it was found by trying to draw the frame. Until
> it is ruled on, the roof beams of the sentry post have **no detailed drawing**.

### H.40.6 What was verified, and how

* **Drafting QA — both sheets PASS.** `DRAWING QAQC/Scripts/dxfqa.py` (the project's own
  auditor, run through `qa_report_data.py`): **0 text overlaps, 0 text outside the inner
  border, 0 geometry in the title block** on STR008 and STR009.
* A second checker, **`Presentation Sheets/Scripts/qa_overlap.py`**, was written for this
  revision. It measures text with **the same `ezdxf.bbox` call `dxfqa.bb_of` uses**, so
  the two cannot disagree, and adds three tests `dxfqa` does not make: *near-touches* at a
  2 % threshold instead of 12 %, *text below `MIN_TXT_H`*, and a *non-dark-layer* census.
  Both sheets report **0 / 0 / 0 / 0**. It is this checker that found `SR2-F2` on STR007.
* **Dimension text is checked too.** `dxfqa` and the new checker both read the MTEXT
  inside each rendered `DIMENSION` block, so a dimension value colliding with a label is
  caught — it was, twice, during production, and both were fixed.
* **Registration with the project QA tools — done, per `CLAUDE.md`.** `STR008` and
  `STR009` added to `TITLE_OVERRIDE` in `qa_report_data.py` (the Revit title block stacks
  the title over five lines, so there is no single text to read). `Presentation Sheets/DXF/`
  was already in `DISCIPLINE` and the discipline was already in `make_index.py`'s `ORDER`
  from SR1. Both re-run: **`DRAWING_INDEX.md` now carries 84 drawings, 78 PASS**, and
  STR008 / STR009 both report **PASS**.
* **Arithmetic re-checked against the master, not retyped:** every span, clear span, cover,
  d, hinge length, confining length, hoop count and bar length on both sheets is computed
  in `sentry_data.py` from the A.4.8 / B.8 / F.4 values. One error was caught this way —
  the beam elevation was first drawn 3 650 long outer-face-to-outer-face instead of 4 000,
  which made the drawn bar run disagree with the scheduled 3 900 cut. Fixed and re-checked.
* **STAAD.Pro was NOT run.** No `.std` file was opened. Nothing on either sheet is an
  analysis result; the STAAD-derived quantities quoted (V<sub>b</sub> = 73.18 kN and the
  EQ axial 36.127 kN) are quoted **from Part B.8.1 as it already records them**.

**Known cosmetic gap, inherited from SR1 and unchanged:** the drawing index's `Scale`
column shows `-` for STR006…STR009. `scale_of()` looks for the scale value inside the same
text as the word "SCALE"; this series follows the Revit title block, which puts the label
`Scale` and the value in two separate cells. The title block is right; the index reader
cannot see it. Not changed, because `scale_of()` is shared with the other 80 drawings.

### H.40.7 Files added by SR2

| File | What it is |
|---|---|
| `Presentation Sheets/DXF/STR008_Structural_Reinforcement_Detailing_Sentry_Post_Beams_and_Column.dxf` | **SHEET 08** |
| `Presentation Sheets/DXF/STR009_Structural_Reinforcement_Detailing_Sentry_Post_Footing_and_Slab.dxf` | **SHEET 09** |
| `Presentation Sheets/PDF/STR008…pdf` · `STR009…pdf` | True-size A2 vector PDFs, plotted 1:1 |
| `Presentation Sheets/Scripts/sentry_data.py` | Every value the two sheets print, and the sentry-post bar-mark register |
| `Presentation Sheets/Scripts/s08_sentry_beam_col.py` · `s09_sentry_footing_slab.py` | One generator per sheet |
| `Presentation Sheets/Scripts/qa_overlap.py` | The drafting checker described in H.40.6 |

> **A future Claude editing either sheet should edit the generator and re-run it, not edit
> the DXF.** The DXF is a build artefact. `sentry_data.py` is the only place a printed
> value lives, and it is the only place a **sentry-post** bar mark lives —
> `rebar_data.py` still excludes the sentry post and must stay that way unless the
> exclusion is lifted by instruction.

### H.40.8 SR2A — the two note panels and the "REV A" header token deleted, 16 September 2026

**By instruction, the same day.** STR008 and STR009 were re-issued with three deletions and
nothing else. **No view, scale, dimension, level, bar, spacing, cut length or bar count
changed on either sheet**, and the drawings themselves are byte-for-byte the same geometry.

| Deleted | Was | Now |
|---|---|---|
| **DESIGN BASIS — THIS SHEET** panel | 36 lines (STR008) / 42 lines (STR009) of design narrative in the right-hand column | **gone from the sheets.** The text is `BASIS_08` / `BASIS_09` in `sentry_data.py`, kept unaltered under M.11 but **no longer printed**. The authority for the design basis is Part **B.8** |
| **DECLARED DETAILING DECISIONS AND OPEN ITEMS** panel | 19 lines (STR008) / 15 lines (STR009) | **gone from the sheets.** The authority is now **H.40.4** (decisions D1–D4) and **H.40.5** (findings `SR2-F1`, `SR2-F2` and open items `SR2-V1`…`SR2-V6`) |
| **"REV A"** in the title-block identity block | `STRUCTURAL - PHASE 2 REV A + M1` | `STRUCTURAL - PHASE 2 + M1` |

**Three consequences were handled, not left dangling:**

1. **The sheets still carry `(D1)`, `(D2)`, `(D3)`, `(D4)` and `SR2-` tags**, and the panel
   that explained them is gone. **Title-block note 7 on STR008 and note 9 on STR009 now say
   what those tags are and point at master H.40.4 / H.40.5.** A reader of the sheet alone
   can still find them.
2. **Deleting the panels left 144 mm (STR008) and 193 mm (STR009) of empty right-hand
   column.** The schedules now fill it: a new `a2_lib.A2Sheet.table_stack()` **solves for
   the row height that ends the stack exactly on the frame**, capped at 7.6 mm so a short
   stack cannot turn into a poster, sharing any surplus out as gap between tables. Body
   text grows with the row and is then shrunk by `table()` until it fits its column. The
   schedules are markedly more legible than at SR2 — this is the one visible gain.
3. **`sheet_data.IDENTITY` is NOT changed.** STR006 and STR007 are released sheets and keep
   the identity line they were issued with. `sentry_data.IDENTITY` derives its own copy with
   the `REV A` token removed and **asserts that the substitution actually happened**, so a
   future edit to `sheet_data` cannot silently put `REV A` back on these two sheets. The two
   lists are therefore allowed to differ, and that is the only difference between them.

**Not renumbered.** The sheets remain stamped **SR2**; SR2A is the name of this amendment in
the record, not a new margin stamp, so that nothing on the sheet reads like the `REV A` the
instruction removed. **If a distinct revision letter is wanted on the sheet, say so and it
becomes a one-line change.**

**Re-verified after the change.** `dxfqa` via `qa_report_data.py`: **STR008 and STR009 both
PASS** — 0 text overlaps, 0 text outside the inner border, 0 geometry in the title block.
`qa_overlap.py`: **0 / 0 / 0 / 0** on both, including the MTEXT inside rendered `DIMENSION`
blocks. It caught one real defect introduced by the change — with the schedule stack now
reaching the bottom of the frame, STR009's view-5 scale note overran x 272 into the table
column; the note was shortened. `DRAWING_INDEX.md` re-run: **84 drawings, 78 PASS**.

**The open items are unchanged and none is resolved.** `SR2-F1` still blocks the sentry-post
roof beams. Removing the panel removed the *statement* of the open items from the drawing,
**not the open items** — they now live only in H.40.5, so **the master, not the drawing, is
what must carry them into the next revision.**

---

## H.41 SR1A — design-basis panel and the revision line deleted from STR006 / STR007, 16 September 2026

**By instruction, given as a follow-up to SR2A** (H.40.8) but against the **owner's own copies
of the two SR1 sheets**, uploaded back into the session for the edit. Two deletions:

1. The **DESIGN BASIS — THIS SHEET** panel, deleted from **both** STR006 and STR007.
2. **"Phase 2 Rev A M1"** deleted from the header — and unlike SR2A, which kept
   `STRUCTURAL - PHASE 2 + M1` on STR008 / STR009 and removed only the `REV A` token, **the
   user was asked directly which was meant** (a chip question, since the two readings produce
   materially different title blocks) and **chose to delete the whole revision line**. The
   identity block on STR006 and STR007 now carries **only the four site-description lines** —
   `UNDERGROUND CBRN-HARDENED` / `BLAST-RESISTANT PROTECTIVE` / `STRUCTURE + SENTRY POST` /
   `PUNE, MAHARASHTRA` — with **no structural-revision text at all**.

**NOTHING IN PARTS A, B, D, E, F OR L CHANGES.** No dimension, level, bar, spacing, cut length
or bar count moved on either sheet. **The main staircase is untouched.** `STR008` and `STR009`
are **byte-identical** to before this revision except for their file creation timestamp
(diffed against the SR2A commit with timestamps and DXF handles stripped) — SR1A touches only
`sheet_data.py` (STR006 / STR007's own data module) and `s06_roof_mat.py` / `s07_wall_stair.py`
(their generators); `sentry_data.py` was edited only to **decouple** its own identity line from
`sheet_data.IDENTITY`'s now-different shape, not to change what it prints.

### H.41.1 The freed space — the same `table_stack()` treatment as SR2A

Deleting the panel left empty column on both sheets. Rather than leave it blank, the schedules
that used to sit above the panel now **fill the whole right-hand column**, using the
`a2_lib.A2Sheet.table_stack()` helper SR2A built for STR008 / STR009: it solves for the row
height that ends the stack exactly on the frame, capped so a short stack cannot become a
poster. `D.BASIS_06` and `D.BASIS_07` are **kept, unaltered, in `sheet_data.py`** under M.11 —
the design basis still exists as text, it is simply no longer printed on either sheet. Its
authority is Part **B** (the box design) directly.

### H.41.2 A real bug found and fixed in `a2_lib.py` — not cosmetic, a genuine defect

Building STR007 through `table_stack()` first produced **80 text-height defects at 1.69 mm**,
0.01 mm under the package's own `MIN_TXT_H` floor of 1.70. Diagnosis, not guesswork:

* **The `WALL SCHEDULE` table genuinely does not fit its 122 mm column at pad 2.8** — seven
  columns (`WALL`, `THK`, `LENGTH`, `COVER`, `d`, `MAIN BARS`, `LINKS`) need 122.7 mm of text
  at the 1.70 mm floor, 0.7 mm over budget. A new **`pad` parameter** was added to
  `A2Sheet.table()` (default 2.8, unchanged everywhere else) so a narrow, many-column table can
  buy back real width without shrinking text past the floor; STR007's wall schedule now passes
  `pad=2.4`, which needs only 119.9 mm — a genuine fit, not a narrower squeeze.
* **Independently, `table()`'s own shrink loop had a quantisation bug.** Body text height
  descends in fixed 0.05 mm steps from whatever height the caller started at; when that start
  is not aligned to `MIN_TXT_H`'s own grid, the step that first satisfies `body_h <= MIN_TXT_H`
  can land **one 0.05 mm step below it** (1.69 instead of 1.70) even when a genuine fit exists
  exactly at the floor. Fixed with a clamp immediately after the loop:
  `body_h = max(body_h, MIN_TXT_H)`. This is a **general library fix**: it can only ever raise
  a height that the loop pushed below the floor by quantisation, never lower one, so it cannot
  regress a table that was already passing.
* **Verified as backward-compatible, not asserted:** STR008 and STR009 rebuild **byte-identical**
  to their SR2A output (diffed with timestamps and DXF handles stripped) — neither the `pad`
  default nor the clamp changed anything either ever needed.

### H.41.3 `SR2-F2` — CLOSED by this revision

Master H.40.5 recorded **`SR2-F2`**: STR007's two note panels rendered at 1.49 mm, below the
package's own floor, found by `qa_overlap.py` and **deliberately left unfixed** at SR2A because
STR007 was a released sheet outside that instruction's scope. **STR007 is directly in scope
now.** The offending panel (`DESIGN BASIS`) is deleted outright by this revision, and the table
that shares its column is verified fitting at **exactly 1.70 mm with 2.1 mm of real margin**
(H.41.2). **`SR2-F2` is CLOSED — there is no longer any sub-floor text on STR007.**

### H.41.4 One dangling cross-reference caught and fixed

`NOTES_06` note 6 read *"...Cl. 10.4 BOUNDARY ELEMENTS ARE NOT TRIGGERED — SEE THE DESIGN BASIS
PANEL."* — a reference to the panel this revision deletes. Rewritten to point at **master Part
A.7.8** instead, so the sheet does not cite something that is no longer on it. No other such
reference was found (checked by grep for the panel's exact heading text across `sheet_data.py`).

### H.41.5 Verified after the change

* `dxfqa` via `qa_report_data.py`: **all four sheets — STR006, STR007, STR008, STR009 — PASS**,
  0 text overlaps, 0 text outside the inner border, 0 geometry in the title block.
* `qa_overlap.py` (measures with the same `ezdxf.bbox` call `dxfqa` uses, plus near-touch at
  2 %, minimum height, non-dark-colour, and the MTEXT inside rendered `DIMENSION` blocks):
  **0 / 0 / 0 / 0 on all four sheets.**
* `DRAWING_INDEX.md` re-run: **84 drawings, 78 PASS.**
* `sheet_data.IDENTITY` and `sentry_data.IDENTITY` printed and compared directly: STR006/007
  now read four lines with no revision text; STR008/009 read the same five lines as at SR2A,
  ending `STRUCTURAL - PHASE 2 + M1`.
* Main staircase constants re-read from `sc_proj.STAIR` after the rebuild: **24 R @ 170.8333 /
  280, 3 flights × 8, rise 4100, well 200, headroom 2533 — unchanged.**

**Nothing engineering moved.** This revision is drafting only: two panels deleted, one header
line deleted, the freed space filled, one dangling note reference fixed, and one real
text-sizing bug in the shared library fixed and verified not to regress the other two sheets.

---

## H.42 A2 services presentation sheets — revision MEP1 — 16 September 2026

> **Two more A2 sheets in the `ARCH001…ARCH005` series, the first of them for SERVICES rather
> than structure: `MEP010` SHEET 10 (HVAC and EMP zone layout plans) and `MEP011` SHEET 11
> (septic tank, soak pit and sump pit — plans, sectional elevations and schedules).**
> **NO DESIGN VALUE MOVED, NO ANALYSIS WAS RUN, AND STAAD.Pro WAS NOT OPENED.** MEP1 is a
> drawing package: it re-presents values the project already holds, in the owner's A2 frame.

### H.42.1 What was asked, and how the request was split

The instruction asked for A2 sheets *"with a similar layout as uploaded files… the same feel
and clarity"* (`Project1.pdf`, the five-sheet Revit A2 architectural set), carrying the HVAC
layout with the blast valves and the sump pit, an EMP zone layout with its schedules, and
cross-sectional elevations of the septic tank, soak pit and sump pit with schedules and
reinforcement — **dark colours only, mostly black; no design-basis panel; no calculation
tables; and nothing on the face about revisions, phases or open items.** Two clarifications
were given while the work was in progress and both are implemented as given:

1. *"Indicate the location of septic and sump pit in the layout scaled away from it towards
   opposite side of sentry post properly."* → the **key plan, view 7 of MEP011**, 1 : 500, at
   true project X and Y.
2. *"Make sheet 11 in which you can show plan and elevation of septic tank soak pit and sump
   pit… let sheet 10 only have hvac and EMP."* → the external works layout was **moved off
   SHEET 10 entirely**; SHEET 10 is HVAC and EMP, and each of the three structures on SHEET 11
   is drawn **twice — once in plan and once as a cross-sectional elevation.**

### H.42.2 What was produced — all under `Presentation Sheets/`

| Sheet | Drawing No. | Views |
|---|---|---|
| **SHEET 10** | **`MEP010`** | 1 HVAC services layout plan, underground level (−)6.100, 1 : 100 · 2 EMP zone layout plan, same level, 1 : 100 · 3 EMP Zone 2 enclosure, plan and section, 1 : 30 · 4 protective ventilation schematic, filter train and cascade |
| **SHEET 11** | **`MEP011`** | 1 sump pit SU-01 reinforcement plan 1 : 35 · 2 sump pit SU-01 sectional elevation A-A 1 : 35 · 3 septic tank ST-01 plan 1 : 30 · 4 septic tank ST-01 sectional elevation 1 : 30 · 5 soak pit SK-01 plan 1 : 50 · 6 soak pit SK-01 sectional elevation 1 : 50 · 7 key plan, external works location, 1 : 500 |

Schedules on MEP010: HVAC equipment · blast valve and gas-tight damper · EMP zone · envelope
penetration register · EMP Zone 2 point-of-entry. On MEP011: sump, pump and tank · structural
element · **bar-mark schedule for SU-01** · external drainage structure · external pipe.

New files: `Scripts/mep_data.py` (the single value source for both sheets),
`Scripts/s10_hvac_emp_layout.py`, `Scripts/s11_drainage_structures.py`, two `DXF/` and two
`PDF/`. **`a2_lib.py`, `sheet_data.py`, `sentry_data.py` and the four STR sheets are NOT
touched** — the two services layer tables are added to each new document at build time rather
than to `a2_lib.LAYERS`, precisely so that STR006…STR009 cannot move.

### H.42.3 Provenance — nothing on either sheet is invented

* **HVAC** — `HVAC/Scripts/hv_data.py`: the five blast valves at their parsed S-06 positions,
  the two NBC trains, the plenum, the generator air shaft, the ducts, terminals, dampers and
  the filter train.
* **EMP** — `EMP Protection/Scripts/em_proj.py`: the three-zone model (adopted at RC2), the
  Zone 2 enclosure, the envelope penetration register, the bonding rule and the PoE set.
* **Drainage** — `Drainage/Scripts/dr_data.py` and `mep_proj.py`: SU-01, the pumps and their
  control levels, ST-01, SK-01…SK-04, IC-01/IC-02 and the external pipe runs.
* **Geometry and levels** — Parts A.3, A.4, A.5, A.6 through `mep_proj`.
* **Reinforcement** — Part **F.1** and `Structural CAD/Scripts/rebar_data.py`. The four sump
  marks **F10, F11, F12 and F13** are read straight out of the register, so a mark cannot be
  tagged on a view without a schedule row.
* **The site layout** — Part **H.23** (SG2's positioned external works) and **H.35** (the
  A-301 key plan), transcribed, not re-derived.

### H.42.4 Six things the project does not hold, and what the sheets do instead

**No `[UNRESOLVED]`, `[ASSUMED]` or `[NOT AVAILABLE]` item was converted, and nothing was
guessed to fill a gap.** Because the instruction was that the sheets must not carry open-item
text, each gap is handled by **not drawing** the thing the project does not have, and is
recorded here instead:

| Ref | The gap | What MEP010 / MEP011 do |
|---|---|---|
| **`MEP1-F1`** | **SH-1, the fresh-air shaft, has no plan position** (`SG2-F4`). | Drawn as a **direction arrow only** at the west wall, with the note *"FA-1 ENTERS FROM THE SH-1 FRESH-AIR SHAFT, WEST OF THE BOX"*. **No coordinate is drawn for it.** |
| **`MEP1-F2`** | **ST-01, the SK cover slabs and the inspection chambers have NO reinforcement anywhere in this project.** | **No bar is drawn in them and none is scheduled.** The structural element schedule reads *"TO THE STR ENGINEER'S DETAIL"* and title-block note 8 says so on the face. Only SU-01, which Part F.1 does schedule, is detailed. |
| **`MEP1-F3`** | **ST-01 has no recorded level** (`H.24`). | View 4 is drawn **relative to local finished grade** and carries **no absolute level at all**. |
| **`MEP1-F4`** | **SK-03 and SK-04 have a reserved footprint and no recorded size** (`H.23`). | Drawn **dashed as reserved footprints** on the key plan; the size column reads `-`. |
| **`MEP1-F5`** | **FA-2 / FA-3 and PD-06 / PD-11 / PD-13 have lengths but no fixed route.** | FA-2 / FA-3 are drawn with a single dog-leg on MEP010 and labelled with the confirmed 11.2 m. **PD-06, PD-11 and PD-13 are NOT drawn on MEP011's key plan at all** — only `PD-16`, whose two ends the project fixes (X 37500 → 42900 on Y 16000 = the 5400 IS 2470 offset). They appear in the pipe schedule with their scheduled lengths. |
| **`MEP1-F6`** | **The SU-01 cover is `[ASSUMED]` and unspecified** (`DR-A2-V1`). | Drawn as **one diagrammatic line** at (−)6.100 across the 1500 opening, tagged `SU-01 COVER`, implying no thickness — exactly as A-202 draws it. Nothing is scheduled for it. |

### H.42.5 `MEP1-F7` — the key plan depends on which sentry-post assumption holds

The request was that the septic tank and the soak pits read as standing **away from the
shelter, on the opposite side from the sentry post**. **On the key plan they do** — the
external works reserve is at `Y 6500 – 17500` and ST-01 / SK-01 sit on `Y 16000`, **10 400
north of the sentry post's north face** — **but only because the key plan uses the EAST
sentry-post position, `X 32000 – 36000, Y 600 – 5600`**, the one RC4 ruled and DR-A2 drew on
the A-301 key plan (`H.35`).

**`U4` is still open and `DR-A1-F1` still stands:** SG2's own clearance run assumed the post
**north**, at `X 9000 – 13000, Y 15250 – 20250`. **If that placement turns out to be the real
one, the post and the external works are on the SAME side and this key plan's geometry is
wrong** — not the dimensions, which are transcribed, but the relationship the sheet is being
asked to show. **Recorded, not resolved. Neither placement is a survey and MEP1 does not rule
between them.**

### H.42.6 The colour and legibility rules the instruction set, and how they were met

*"Do not use light colours… use dark colours only… mostly black"* and *"neat without any
overwriting"* are both **measured, not asserted**:

* **Four ACI colours only — 7 black, 8 dark grey, 1 dark red, 5 dark blue** — on both sheets,
  including the thirteen services layers MEP010 adds and the six MEP011 adds. `qa_overlap.py`'s
  non-dark-layer census reports **0** on both.
* **0 text overlaps, 0 near-touches at 2 %, 0 text below the 1.70 mm floor, 0 text outside the
  inner frame** on both sheets, measured with the same `ezdxf.bbox` call the project auditor
  `dxfqa.py` uses. Every table is sized with the font metrics `ezdxf` places it with.
* **No design-basis panel, no calculation table, and no revision, phase or open-item text
  appears anywhere on either sheet.** `mep_data.IDENTITY` carries the same four
  site-description lines SR1A left on STR006 / STR007 and **no revision line**.

### H.42.7 Registration with the QA tools — the H.25 rule, obeyed

`Presentation Sheets/DXF/` was already in `qa_report_data.DISCIPLINE`, but it maps to
*"STRUCTURAL - A2 presentation sheets"*, which these two sheets are not. A **filename-prefix
entry** `("Presentation Sheets/DXF/MEP", "MEP - A2 presentation sheets")` was inserted **ahead**
of it — the lookup takes the first match — and the same label added to `make_index.ORDER`;
`MEP010` and `MEP011` were added to `TITLE_OVERRIDE` because the Revit-style title block stacks
the title over four or five lines and there is no single text to read. **Both tools re-run:
`DRAWING_INDEX.md` and `qa_index.json` now carry 86 drawings, 80 PASS — up from 84 / 78 — and
MEP010 and MEP011 both report PASS.** The four STR rows are byte-identical.

### H.42.8 Verified after the change, and how

* `qa_overlap.py` on both sheets: **0 / 0 / 0 / 0** — overlaps, near-touches, sub-floor text,
  text outside the frame — and **0 non-dark layers**.
* `qa_report_data.py` + `make_index.py` re-run: **86 drawings, 80 PASS**; **MEP010 383 texts,
  MEP011 342 texts**, both **A2**, both **PASS**.
* Both PDFs measured with `pdfinfo`: **1683.78 × 1190.55 pt — the same page box as
  `Project1.pdf` itself**, so they plot 1 : 1 on the owner's own sheet.
* **`git status` confirms STR006, STR007, STR008 and STR009 — DXF, PDF and their generators —
  are UNCHANGED**, as are `a2_lib.py`, `sheet_data.py` and `sentry_data.py`. The only edited
  files outside the new ones are `qa_report_data.py` and `make_index.py` (registration, five
  added lines) and the two regenerated QA outputs.
* **Main staircase: UNTOUCHED.** 24 risers at 170.8333, tread 280, 3 flights × 8, total rise
  4100, well 200, waist 200, headroom 2533. It is **not drawn on either sheet**, no file MEP1
  adds reads or writes `sc_proj.STAIR`, and `STR007`, which does detail it, is byte-identical.

### H.42.9 What MEP1 did NOT do

**No design value, load, duty, thickness, level, bar, spacing, quantity, rate, date or float
changed.** SU-01, ST-01, SK-01 and the Zone 2 enclosure were **not re-sized**. No `.std` file
was touched and **STAAD.Pro was not run** — nothing here is an analysis. **No evidence tag was
converted, downgraded or deleted**, and no `[U]` or `[N]` item was drawn as though it were
confirmed. The HVAC, EMP Protection and Drainage packages are **not modified** — MEP1 reads
their data modules and writes nothing back to them. **K.1b is not edited and no count is
restated**; MEP1's findings are `MEP1-F1` … `MEP1-F7` above, and they are findings, not new
information gaps — every gap they name is already recorded in Part K or in an earlier Part H.

---

## H.43 Fire plan, works management and two architectural sheets redrawn — revision MEP2 — 18 September 2026

> **Four more A2 sheets in the `ARCH001…ARCH005` series.** Two are NEW —
> **`FLS012` SHEET 12** (fire and life safety escape plan) and **`WMS013` SHEET 13**
> (works management) — and two are **REDRAWS of the owner's own sheets 1 and 2**,
> **`ARCH001`** and **`ARCH002`**, with the same views at the same scales and every
> dimension and level brought to the project's authoritative data.
> **NO DESIGN VALUE MOVED, NO ANALYSIS WAS RUN, AND STAAD.Pro WAS NOT OPENED.**

### H.43.1 What was asked

*"Make similar sheets 12 & 13 — 1) Fire plan, 2) works management not as per the latest
revision but the just previous one having an estimate of 2.98 cr one. Recreate sheets 1 & 2
with the same plans just correct the dimensions as per project data. Retain all other
instructions from the previous prompt."* The retained instructions are MEP1's (H.42): the
owner's A2 frame and title block, **dark colours only and mostly black**, **no design-basis
panel, no calculation table, and no revision, phase or open-item text on the face**, neat
with no overwriting, and schedules where they help.

### H.43.2 "The just previous one having an estimate of 2.98 cr" is WM3, not WM4

| Revision | Where | Total | Basis |
|---|---|---|---|
| **WM2** (H.13) | the owner's package as supplied | **Rs 3,00,33,306** as stated | the owner's own rates |
| **WM3** (H.15) | **the owner's package REVISED with the RC1 rulings applied** | **Rs 2,97,90,913** | the owner's own rates |
| WM4 (H.38) | priced from the Maharashtra PWD SSR 2022-23 | Rs 2,07,39,408 estimated cost | a published schedule |

**Rs 2,97,90,913 is Rs 2.98 crore, so SHEET 13 presents `WM3`** — the revised bill, the
revised cost summary and the revised master construction schedule **R1**. WM4 is the later
revision and is deliberately **not** the subject of this sheet. Every amount, quantity,
count, date and duration is read at build time from
`WORKS MANAGEMENT/Cost/REVISED_*_RC1.csv` and
`WORKS MANAGEMENT/Programme/REVISED_MASTER_CONSTRUCTION_SCHEDULE_R1.csv`; **nothing is
retyped and nothing is re-derived.**

### H.43.3 What was produced — all under `Presentation Sheets/`

| Sheet | Drawing No. | Views |
|---|---|---|
| **SHEET 01** | **`ARCH001`** | 1 underground level plan (−)6.100 1:100 · 2 headhouse level plan (−)2.000 1:100 · 3 ground level plan 0.000 1:100. All three span the full 22000 box so that both escape shafts appear at every level |
| **SHEET 02** | **`ARCH002`** | 1 sentry post ground floor level 1:50 · 2 first floor level 1:50 · 3 south elevation, shelter and sentry post, 1:150 · 4 lintel L1, wall ties and the 200 infill zone 1:20 |
| **SHEET 12** | **`FLS012`** | 1 underground level escape plan 1:100 · 2 entry level escape plan 1:100 · 3 escape shaft section and ladder 1:100 · 4 evacuation decision rule |
| **SHEET 13** | **`WMS013`** | 1 master construction programme bar chart, 18 summary activities of the 130 · 2 cost distribution by bill part |

New files: `Scripts/arch_data.py` (sheets 01 and 02), `Scripts/ops_data.py` (sheets 12 and
13), four generators `s01_arch_plans.py`, `s02_sentry_arch.py`, `s12_fire_plan.py`,
`s13_works_management.py`, four `DXF/` and four `PDF/`.

### H.43.4 The correction register — every figure the redraw changes

The owner's sheets 1 and 2 are preserved as the uploaded `Project1.pdf` and are **not
altered**. `arch_data.CORRECTIONS` is the machine-readable copy of this table; by
instruction it is **not printed on the sheets**.

| Sheet | View | Item | Owner's figure | Project figure | Authority |
|---|---|---|---|---|---|
| **01** | UNDERGROUND LEVEL PLAN | Bay clear-width chain | 2900 / 3500 / 1800 / 1560 / 2400 then 2800 / 3400 | **2900 / 1800 / 3500 / 1800 / 1560 / 2000 / 2800 / 3000** | `A.3` |
| **01** | UNDERGROUND LEVEL PLAN | Bay 6 decon airlock clear width | 2400 | **2000** | `A.3` |
| **01** | UNDERGROUND LEVEL PLAN | Bay 8 generator bay clear width | 3400 | **3000** | `A.3` |
| **01** | UNDERGROUND LEVEL PLAN | Bay 2 clear width | not dimensioned | **1800** | `A.3` |
| **01** | UNDERGROUND LEVEL PLAN | Internal walls W5 / W6 / W7 | not dimensioned | **200 / 400 / 400, W6 and W7 thickened by M1** | `A.3` |
| **01** | UNDERGROUND LEVEL PLAN | Blast door leaf, W6 and W7 | 900 x 2100 in the door schedule | **1200 x 2100** | `A.4.9` |
| **01** | HEADHOUSE LEVEL PLAN | Covered entry stairwell external length | 6550 | **6800  (X 9250 - 16050)** | `A.4.7` |
| **01** | GROUND LEVEL PLAN | Sentry post external plan | 3950 x 4950 | **4000 x 5000** | `A.4.8` |
| **02** | GROUND / FIRST FLOOR LEVEL | Sentry post external plan | 3950 x 4950 | **4000 x 5000** | `A.4.8` |
| **02** | SOUTH ELEVATION | Sentry post ground floor level | 440 | **+0.450** | `A.4.3` |
| **02** | SOUTH ELEVATION | Entry stairwell roof at head | 3400 | **+2.450  (soffit +2.200)** | `A.4.3 / A.4.7` |
| **02** | SOUTH ELEVATION | Sentry post roof | 7000, labelled POST ROOF | **+6.700 roof slab, +7.000 parapet top - two separate levels** | `A.4.3` |
| **02** | SOUTH ELEVATION | Lowest level shown | -6100, labelled FDN LEVEL | **(-)6.100 is the internal floor / top of mat; the mat soffit is (-)6.700 and the formation (-)6.800** | `A.4.3` |
| **02** | SOUTH ELEVATION | Sentry post founding level | not shown | **(-)2.000, F1 footings on in-situ basalt** | `A.4.8 / B.8.7` |

**The bay chain is the principal correction.** The owner's underground level plan reads
`2900 / 3500 / 1800 / 1560 / 2400` and then `2800 / 3400`: it omits bay 2 entirely, puts
bays 3 and 4 in the wrong order, and gives bay 6 as 2400 and bay 8 as 3400. Master **A.3**
gives **2900 / 1800 / 3500 / 1800 / 1560 / 2000 / 2800 / 3000**, and the redraw dimensions
every boundary in that schedule, with the 110 W8 partitions and the 200 / 400 internal walls
labelled. **The 22000 × 6200 external envelope and the 6200 depth were already right and are
unchanged.**

### H.43.5 `MEP2-F1` — the owner's door schedule is wrong for the two blast doors

The owner's sheets 1 and 2 share one **DOOR SCH** listing thirteen marks, `100`…`110`, `114`
and `115`, **every one of them 900 × 2100 × 45**. Master **A.4.9** records **five distinct
openings at four different sizes**: Blast Door 1 and Blast Door 2 are **1200 × 2100** and
are the protective boundary; the headhouse inner security door is 900 × 2100 and not blast
rated; the entry door is **1000 × 2100** and opens outward; the sentry post door is
900 × 2100. **A 900 leaf will not fit either blast door opening, which is dimensioned
Y 600 – 1800 in W6 and W7.** `ARCH001` therefore carries a **new DOOR SCHEDULE keyed
BD1 / BD2 / D1 / D2 / D3** against A.4.9, and a separate **OPENING SCHEDULE** for the two
escape shafts, the stair void, the service entry plate and the vision panels. The owner's
mark numbers are not carried forward, because nothing in the project maps them to openings.

### H.43.6 `MEP2-F2` — the elevation's "FDN LEVEL −6100" is the floor, not the foundation

On the owner's sheet 2 the lowest level is labelled **FDN LEVEL −6100**. Master A.4.3 makes
**(−)6.100 the internal floor and the top of the mat**; the **underside of the mat is
(−)6.700** and the **formation is (−)6.800**. The redraw labels all three, and adds the
sentry post's own founding level, **(−)2.000 on in-situ basalt**, which the owner's sheet
does not show at all. Two more levels on that elevation are corrected: the sentry post
ground floor is **+0.450** and not 440, and the entry stairwell roof at head is **+2.450**
and not 3400. The single **POST ROOF 7000** is split into the **+6.700 roof slab** and the
**+7.000 parapet top**, which are different levels in A.4.3.

### H.43.7 The fire sheet uses the RULED ladder, not the superseded finding

`Fire and Life Safety/Scripts/fs_data.py` still carries **`FS-6` / `FS-V7`** as *"no ladder,
rung or fall-arrest is specified in either escape shaft"*. **That was superseded by the RC4
ruling of 11 September 2026** (master A.4.9 and H.28): **ladder only, fall-arrest deferred.**
`FLS012` therefore draws and schedules the **ruled** ladder — 20 dia galvanised MS rungs at
400 clear width, equal pitch (ESC 1 297.6 over 21 spaces, ESC 2 295.7 over 23), 2 No.
50 × 10 galvanised flat stringers, cast-in lugs to the 250 collar and the roof-slab bore,
expansion-anchored brackets at 1.5 m over the lower 3.200 m, ≥ 200 behind the rung, ≥ 750
climbing space in front and grab rails 1100 above the head — and **does not reproduce the
superseded finding text**. **Fall-arrest, a rest platform and the injured-person question
remain outside this sheet and are unchanged in Part K.**

Every route, travel distance and climb is **computed** in `fs_data` from `mep_proj`, so a
figure on the sheet cannot disagree with the escape-route schedule: R1 travel **14.6 m**,
climb **6.100 m**; R2 **1.45 m** and **6.250 m**; R3 **1.50 m** and **6.800 m**; the spine
**20.800 m**; R1's surface leg **11.47 m**. The sheet states as fact the three things the
plan is built on — bays 1 to 6 are **one** smoke compartment, blast doors 1 and 2 are the
only real barriers, and **ESC 2 is in bay 8 with the generator, so R3 is not used for a fire
in bay 8** — as an operating instruction, not as an open item.

### H.43.8 What the two new sheets do NOT claim

**`WMS013` is a presentation of WM3, not a re-pricing.** No rate was touched, no quantity
re-measured and no total recomputed; the sheet's own note says that **a line shown nil is
not priced in the bill**, so the generator line that WM3 deliberately carries at zero cannot
be read as free. **`FLS012` designs nothing.** It draws the escape routes the project
already has and the ladder RC4 ruled; it adds no detection, no alarm, no emergency lighting
and no suppression, because the project contains none, and it does not pretend that the
three routes are four.

### H.43.9 Registration with the QA tools — the H.25 rule, obeyed

The A2 presentation series now spans **four disciplines in one folder**, so
`qa_report_data.DISCIPLINE` matches each by **filename prefix** ahead of the generic folder
prefix: `…/DXF/MEP`, `…/DXF/ARCH`, `…/DXF/FLS`, `…/DXF/WMS`, with `…/DXF/` left as the
structural fallback. The three new labels were added to `make_index.ORDER` and all four
drawing numbers to `TITLE_OVERRIDE`. **Both tools re-run: `DRAWING_INDEX.md` and
`qa_index.json` now carry 90 drawings, 84 PASS — up from 86 / 80 — and ARCH001, ARCH002,
FLS012 and WMS013 all report PASS.**

### H.43.10 Verified after the change, and how

* `qa_overlap.py` on **all ten** A2 sheets: **0 text overlaps, 0 near-touches at 2 %,
  0 text below the 1.70 mm floor, 0 text outside the inner frame, 0 non-dark layers.**
* `qa_report_data.py` + `make_index.py` re-run: **90 drawings, 84 PASS**; ARCH001 350 texts,
  ARCH002 250, FLS012 244, WMS013 298, all **A2**, all **PASS**.
* All four PDFs measured with `pdfinfo`: **1683.78 × 1190.55 pt — the same page box as
  `Project1.pdf`**, so they plot 1 : 1 on the owner's own sheet.
* **`git status` confirms STR006…STR009 and MEP010 / MEP011 — DXF, PDF and their generators
  — are UNCHANGED**, as are `a2_lib.py`, `sheet_data.py`, `sentry_data.py` and
  `mep_data.py`. The Fire and Life Safety, Drainage, HVAC, EMP and Works Management
  packages are **read and not written**. The only edited files outside the new ones are
  `qa_report_data.py` and `make_index.py` (registration) and the two regenerated QA outputs.
* **Main staircase: UNTOUCHED.** 24 risers at 170.8333, tread 280, 3 flights × 8, total rise
  4100, well 200, waist 200, headroom 2533 — re-read from `sc_proj.STAIR` after the build.
  It is drawn on `ARCH001` view 1 and used by escape route R1 on `FLS012`, and **not one of
  its values is altered**; both sheets print it from `mep_proj.STAIR`.

### H.43.11 What MEP2 did NOT do

**No design value, load, duty, thickness, level, bar, spacing, quantity, rate, date or float
changed.** The redraws correct what the owner's two sheets *print*; they do not change what
the project *is* — every corrected figure already existed in Part A and is cited to it. No
`.std` file was touched and **STAAD.Pro was not run**. **No evidence tag was converted,
downgraded or deleted**, and no `[U]` or `[N]` item was drawn as though it were confirmed:
the sentry post's site position is still `[ASSUMED]` under `U4` and is labelled a convention
on ARCH001, and WM3's own unpriced line is still unpriced. **K.1b is not edited and no count
is restated.** The owner's `Project1.pdf`, `USER_SOURCE/` and the as-supplied WM2
publication are untouched, and **WM4 is neither superseded nor altered** — WM3 and WM4 are
different revisions on different bases and both stand (M.11).

### H.43.12 MEP2A — the two charts deleted from SHEET 13, by instruction, 18 September 2026

> ***"No need to include graphs in works management."*** `WMS013` was re-issued the same day
> with **both charts deleted** — view 1, the master construction programme bar chart, and
> view 2, the cost distribution by bill part. **No figure changed.** The record above is
> preserved under M.11 and describes the sheet as first issued.

**What the sheet is now.** A pure schedule sheet, and a fuller one than the charts allowed:

| Where | Table | Rows |
|---|---|---|
| Drawing region, x 44 – 260 | **BILL OF QUANTITIES — MEASURED ITEMS (REVISED)** | **all 38 items** under their five part headings, each heading a full-width band carrying its own item count and total |
| Schedule column | **MASTER CONSTRUCTION PROGRAMME** | 18 summary activities, ID / activity / working days / start / finish |
| Schedule column | **COST SUMMARY** | 8 cost heads to the final project cost |
| Schedule column | **BILL OF QUANTITIES — PART SUMMARY** | the five parts |
| Schedule column | **WHAT THE REVISED BILL CARRIES** | the six WM3 changes |

**The bar chart carried 18 activities and no quantities; the tables carry the whole bill.**
Deleting the charts freed the entire drawing region, so the sheet now prints **every measured
item with its unit, quantity, rate and amount** — 491 texts against 298 before — which the
charted version could not do. The `PRINCIPAL BILL ITEMS BY VALUE` table is dropped as
redundant once the full bill is on the sheet, and `PROGRAMME PHASES` is dropped because the
programme table already contains the four phases. The two chart layers `W-GRID` / `W-BAR` /
`W-PHASE` / `W-SUB` / `W-AXIS` / `W-TEXT` are no longer created.

**Two honesty points the tabular sheet has to make, and does.** The bill's item descriptions
run to 293 characters, so they are **trimmed to the column at a word break and marked with an
ellipsis**, with title-block note 10 saying so and that the bill governs — no description is
reworded. And the **standby generator line carries no rate in WM3** (it is deliberately held
at `DATA REQUIRED` there, so the omission is visible rather than silent), so it prints as
**`NOT PRICED`** with a `-` rate, and title-block note 9 states that such a line is not
included in any total on the sheet. **No rate is invented, and the Rs 2,97,90,913 total is
WM3's own.**

**Verified after the change:** `qa_overlap.py` on all ten A2 sheets **0 / 0 / 0 / 0 / 0**;
`DRAWING_INDEX.md` re-run **90 drawings, 84 PASS**, `WMS013` **491 texts, A2, PASS**; the PDF
still **1683.78 × 1190.55 pt**. **No other sheet, script or data module was touched** — the
only files that change are `s13_works_management.py`, `ops_data.py` (which gains
`BOQ_ITEMS` and `PROGRAMME_ROWS` and keeps everything else), the `WMS013` DXF and PDF, the
two regenerated QA outputs and the documentation. **The main staircase is untouched and does
not appear on this sheet.**

---

# PART I — PROJECT FILE MANIFEST

## I.1 CURRENT FILES — input (user-supplied)

> **QA1, 9 Sep 2026 (H.11).** The ten Rev F DXF below were given a sheet frame, title
> block and NOTES box and had their annotation de-clashed, **in place, at the same
> filenames**. Their geometry is unchanged; where a drawing was re-centred on its new
> sheet it moved as a pure vertical translation. Drawing numbers **A-101…A-301** now
> appear in their title blocks — see `DRAWING QAQC/DRAWING_INDEX.md`.

| File | Type | Rev | Purpose | Status |
|---|---|---|---|---|
| `1_Underground_Level_Plan.dxf` | DXF | F | **Primary geometry source** | CURRENT |
| `1_Staircase_Section.dxf` | DXF | F | Section A-A, main stair | CURRENT |
| `2_Side_Section_with_Stairs.dxf` | DXF | F | Section X-X; carries the Rev F marker | CURRENT |
| `2_Ground_Plan_Headhouse_Berm.dxf` | DXF | F | Headhouse + stairwell plan, berm | CURRENT |
| `3_Headhouse_Section_Cutaway.dxf` | DXF | F | Section B-B | CURRENT |
| `5_Entry_Headhouse_Stair_Section.dxf` | DXF | F | **Section C-C, the Rev F entry stairwell** | CURRENT |
| `5_Front_Elevation.dxf` | DXF | F | Sentry post levels | CURRENT |
| `3_Sentry_Post_Ground_Floor_Plan.dxf` | DXF | F | Sentry GF | CURRENT |
| `4_Sentry_Post_First_Floor_Plan.dxf` | DXF | F | Sentry FF | CURRENT |
| `6_Sentry_Post_Framing_Plan.dxf` | DXF | F | **Primary source for the sentry frame + load schedule** | CURRENT |
| `Phase1_Design_Report_RevD.md` | Markdown, 126 KB | **D** | **Primary source for loads, materials, geotech** | **CURRENT for loads/materials; SUPERSEDED for the entrance (C1) and headhouse roof (C2). NOT IN THIS WORKSPACE — see note** |
| `SK02_Underground_Plan.png` | PNG | — | Coloured GA plan, presentation graphic | CURRENT. **NOT IN THIS WORKSPACE** |
| 19 STAAD screen captures | PNG | — | How the STAAD models were originally recorded | CURRENT. **NOT IN THIS WORKSPACE, and no longer the only evidence — the six `.std` files are (Part D.1)** |

> **RC3 correction, 11 September 2026 (Part H.27).** The three rows above were listed as
> `CURRENT` without qualification, which reads as *present and openable*. **They are not in the
> repository** — it holds no `.png`, no `.md` named `Phase1_Design_Report_RevD`, and no image of
> any kind. They were supplied to the project, this master was compiled from them, and **every
> value they support is already transcribed into Parts A, B, D and F with its evidence tag** —
> which is why nothing downstream depends on re-opening them. **Recorded as absent rather than
> deleted: they are the provenance of Part A, and M.11 forbids editing a record away.** Re-upload
> is required only to re-derive something Parts A–F do not already carry. `[C] file listing`

## I.2 CURRENT FILES — output (generated in this project)

> **Added by QA1, 9 Sep 2026 (H.11):** `DRAWING QAQC/DRAWING_INDEX.md` (the drawing
> index for all 65 DXF, generated from the files themselves), `DRAWING QAQC/QAQC_REPORT.md`,
> `DRAWING QAQC/Scripts/` (five inspection scripts: bounding-box, clash, panel, void and
> plot) and `current/cad/Scripts/` (the five-module pipeline that produced the current
> state of the eleven `current/cad` drawings). **No output DXF listed below was created
> or renamed by QA1** — the 54 generated sheets were regenerated to their own filenames
> after their generators were corrected.

| File | Type | Purpose |
|---|---|---|
| `01_Shear_Wall_Structural_Drawing.dxf` / `.pdf` | DXF + A1 PDF | S-01 |
| `02_Mat_Foundation_Structural_Drawing.dxf` / `.pdf` | DXF + A1 PDF | S-02 |
| `03_Roof_Slab_Structural_Drawing.dxf` / `.pdf` | DXF + A1 PDF | S-03 |
| `04_Main_Staircase_Structural_Drawing.dxf` / `.pdf` | DXF + A1 PDF | S-04 |
| `05_Approach_Stairwell_Structural_Drawing.dxf` / `.pdf` | DXF + A1 PDF | S-05 |
| `06_Underground_Plan_Services_Sump_BlastValves.dxf` / `.pdf` | DXF + A1 PDF | S-06 |
| `07_Entry_Stairwell_Flight_Reinforcement.dxf` / `.pdf` | DXF + A1 PDF | S-07 |
| `08_Sentry_Post_Slab_Reinforcement.dxf` / `.pdf` | DXF + A1 PDF | S-08 |
| `00_Drawing_Set_S01_to_S08.pdf` | PDF, 8 pages A1 | Combined drawing set |
| `Structural_Design_Calculations_IS456.md` / `.pdf` | 17 pp | **Full calculation report with clause citations** |
| `Headhouse_Walls_and_Slab_Design.md` / `.pdf` | 8 pp | Dedicated headhouse design + the ERR-1 correction |
| `Load_Calculations_Explained.md` / `.pdf` | 7 pp | Plain-language loads + STAAD modelling basis |
| `Services_Drainage_EMP_BlastValves.md` / `.pdf` | 7 pp | Drainage, EMP cage, blast valves, ventilation |
| `Consolidated_Member_Schedule.md` / `.pdf` | 5 pp | Every member, one table |
| `Presentation_Speaking_Notes.md` / `.pdf` | 7 pp | 90-minute run sheet + anticipated questions |
| `Phase1_Design_Report_RevD.pdf` | 33 pp | The Rev D report, rendered |
| Python toolchain (18 files) | `.py` | **DXF generators + verification scripts — see E.4** |

### Added by DR1 / HV1 / FN1, 5 September 2026 — see H.9

| Folder | Contents |
|---|---|
| `Drainage/` | **11 A1 DXF** D-001…D-305 · 7 schedules (`.md` + `.csv`) · `DR_CALC_OUTPUT.txt`, 17 sections · **two-page A4 handout**, 2 DXF + `DRAINAGE_HANDOUT.pdf` · design basis · drawing index · QA/QC + DXF validation report · 11 Python generators · `Revit/07_drainage_model.py` |
| `HVAC/` | **6 A1 DXF** M-001…M-203 · 7 schedules · `HV_CALC_OUTPUT.txt`, 14 sections · **two-page A4 handout**, 2 DXF + `HVAC_HANDOUT.pdf` · design basis · drawing index · QA/QC + validation report · 5 Python generators · `Revit/08_hvac_model.py` |
| `Schedule of Finishes/` | **3 A1 DXF** A-601, A-611, A-612 · 6 schedules covering **all 13 spaces** · drawing index · QA/QC + validation report · 3 Python generators · `Revit/09_room_finishes.py` |
| `MEP_AND_FINISHES_COORDINATION.md` | The cross-discipline check across all three — ten items, four aligned, one resolved, five referred |

### Added by WM1, 7 September 2026 — see H.10

| Folder | Contents |
|---|---|
| `WORKS MANAGEMENT/` | **8 principal deliverables** (`.md` + `.csv`): WBS · BOQ · Resource Plan · Procurement Plan · QA/QC Plan · Safety & Risk Register · Codes & References · **`Underground_Shelter_Works_Management_Handout.pdf`, 44 pages, 25 sections** |
| `WORKS MANAGEMENT/Programme/` | **`Underground_Shelter_Final_Works_Programme.xml`** — the master programme in **MSPDI**, Microsoft Project's own published XML schema (279 activities, 18 milestones, 404 links, 33 resources, 426 assignments, six-day calendar with 5 exceptions) · **`.pdf`, 7 A3 sheets** with the summary and detailed Gantt · `.csv` task list |
| `WORKS MANAGEMENT/Documentation/` | Project component register · construction methodology · **sentry post brick masonry, design change SP-B1** · progress monitoring · assumptions and verification register |
| `WORKS MANAGEMENT/Schedules/` | `BOQ_QUANTITY_DERIVATION.txt` (~800 lines, every input sourced) · `WM_CPM_OUTPUT.txt` |
| `WORKS MANAGEMENT/QAQC/` | `WM_CONSISTENCY_AUDIT.txt` — **65 executed checks, 65 pass** |
| `WORKS MANAGEMENT/Scripts/` | 9 Python files. `wm_build_all.py` regenerates the whole package from `wm_data.py` + `wm_content.py`; no date, quantity or float in any deliverable is typed by hand |

### Added by WM2, 10 September 2026 — see H.13

> **THE OWNER'S OWN WORKS MANAGEMENT MATERIAL. It governs.** Nothing in `USER_SOURCE/`
> has been edited, converted or corrected, and nothing generated from it is retyped.

| Folder / file | Contents |
|---|---|
| `SSR 22-23 MH (1).pdf` | **PDF, 624 pages, 8.3 MB — USER-SUPPLIED INPUT, 15 Sep 2026.** Government of Maharashtra PWD **State Schedule of Rates 2022-23**, approved by Circular RADASU-2022/PR.KR.12/NIYOJAN-3 dt. 25.07.2022, effective 25.07.2022. **The rate source for the priced bill (WM4, H.38).** Untouched; the rates read out of it are in `WORKS MANAGEMENT/Cost/WM4_SSR_RATE_LIBRARY.csv` with the SSR page for each |
| `WORKS MANAGEMENT/Cost/WM4_*` | **The SSR-priced bill (WM4, H.38)** — the workbook, the narrative, the priced bill, the rate library, the recapitulation, the owner's bill re-rated, the open items and every derived rate's arithmetic |
| `WORKS MANAGEMENT/USER_SOURCE/` | **The owner's four files, unaltered** — `Underground_CBRN_Ops_Room_BOQ_Estimate.xlsx` (BOQ, rates and the cost build-up to **₹3,00,33,306**) · `BOQ_and_Works_Management_CBRN_Ops_Room.pdf` (8-page report, WBS overview, milestones) · **`UG_CBRN_HDRND_OPS_ROOM_MCS_R0.mpp`** (master construction schedule R0) · its Level-5 micro print · `README.md` |
| `WORKS MANAGEMENT/Cost/` | **Three cost documents, side by side.** *(1)* The owner's, as supplied — `USER_BOQ_AND_COST_ESTIMATE.md` plus `USER_BOQ_TAKEOFF.csv`, `USER_BOQ_PRICED.csv`, `USER_COST_SUMMARY.csv`, read out of their workbook cell by cell. *(2)* The owner's with the RC1 rulings applied — `REVISED_BOQ_*_RC1`. *(3)* **WM4, the project's own bill priced from Maharashtra SSR 2022-23** — `WM4_Underground_Shelter_BOQ_Cost_Estimate_SSR_2022-23.xlsx` and its CSVs. **WM1 had no rate and no cost anywhere in it; WM4 is where the rates are** |
| `WORKS MANAGEMENT/Programme/USER_MASTER_CONSTRUCTION_SCHEDULE_R0.md` / `.csv` | **The programme of record** — all **130 activities**, ids 1–130 with no gaps, durations, dates and logic, decoded from the owner's own MS Project print. **224 working days, 02-11-2026 to 26-07-2027** |
| `WORKS MANAGEMENT/Documentation/WM_RECONCILIATION_REGISTER.md` | **R-1 to R-14 — fourteen conflicts against this master, ALL OPEN.** Nothing reconciled in either direction |
| `WORKS MANAGEMENT/QAQC/WM2_SOURCE_AUDIT.txt` | The owner's own arithmetic re-added. Rebar, the five part subtotals and every percentage cost head **tie up to the rupee**; the concrete total is out by **10.00 m³** and the final cost by **₹1,00,000** — R-13 and R-14, **reported not corrected** |
| `WORKS MANAGEMENT/Scripts/wm2_user_package.py` | Reads `USER_SOURCE/` and writes all of the above, including the audit. Re-runnable; nothing is typed by hand |

> **No `.mpp`.** Microsoft Project's native format is an undocumented binary writable only
> by Microsoft Project. MSPDI is Microsoft's own interchange schema and opens directly;
> *File → Save As → Project (\*.mpp)* produces the binary. Verified by reading the file back
> with MPXJ 16.7.0 and comparing every count and date against the CPM. See H.10.

> **Shared modules** — `mep_proj.py`, `mep_dxf.py`, `mep_views.py`, `mep_validate.py`,
> `mep_render.py` — live in `Drainage/Scripts/` and are used by all five packages. `mep_dxf.py`
> **subclasses `Structural CAD/Scripts/sc_dxflib.py`**, so the A1 sheet standard is identical to the
> issued R-series. **27 DXF, all validated, 0 errors.**

### Added by CAM2 / FS2, 10 September 2026 — see H.18

> **Two documents that were in `WORKS MANAGEMENT/Documentation/` are no longer there.**
> Neither was ever a works-management deliverable. Each is now its own discipline package,
> built to the same shape as `Drainage/` and `HVAC/`, with the drawings the move added.
> **The text moved verbatim and the generators moved with it** (M.12).

| Folder | Contents |
|---|---|
| `Fire and Life Safety/` | **2 A1 DXF** F-101, F-102 · `Documentation/FIRE_SAFETY_AND_EVACUATION_PLAN.md` — **FS2**, the FS1 text plus **FS-6 / FS-V7**, which the drawings raised · `Schedules/FS_ESCAPE_ROUTE_SCHEDULE.md` / `.csv` · `QAQC/FS_DRAWING_VALIDATION.txt` · **5 Python generators**; `fs_build_all.py` rebuilds the package, and every travel and climb figure is computed from `mep_proj.py`, not typed |
| `Site and Concealment/` | **1 A1 DXF** C-101 · `Documentation/CAMOUFLAGE_AND_CONCEALMENT_POLICY.md` — **CAM2**, the CAM1 text plus **CAM-V5**, which the drawing raised · `QAQC/CM_DRAWING_VALIDATION.txt` · **4 Python generators**; `cm_build_all.py` rebuilds the package |

> **`mep_dxf.py` and `mep_validate.py` changed, and both changes are output-neutral.** The
> sheet's issue date and its two sentry-post scope notes became overridable class
> attributes, and validator check 11 now asks that a sheet **DECLARE** its sentry post
> scope rather than that it **exclude** it — because on C-101 the sentry post is in scope,
> being the tallest signature on the site. Verified by regenerating D-101 line for line:
> **26 869 lines against 26 869**, every difference a timestamp, a GUID, CLASS ordering or
> the ezdxf stamp. **No issued sheet was regenerated into the repository.**

### Added by EM1, 10 September 2026 — see H.19

> **The project's first EMP design.** No design value is changed by it, no shared library is
> modified, and it creates no penetration of the envelope.

| Folder / file | Contents |
|---|---|
| `EMP Protection/Documentation/EMP_PROTECTION_DESIGN_BASIS.md` | **The main document.** The governing fact and the K.3 reproduction · what the design already does right · the three-zone model and the standing-alone design rule · every hole in the envelope · the Zone 2 enclosure · bonding and earthing · verification · **EM-F1…F6** and **EM-V1…V6** |
| `EMP Protection/Documentation/00_README.md` · `EMP_DRAWING_INDEX.md` | Package README; the six drawings, their validation results, and the four sheets deliberately **not** issued |
| `EMP Protection/Calculations/EMP_CALC_OUTPUT.txt` | Every derivation printed with its inputs, its formula and its arithmetic — E.1 the requirement · E.2 the cage and the K.3 check · E.3 all ten penetrations · E.4 the zone model · E.5 the enclosure · E.6 earthing · E.7 bonding · E.8 verification · E.9 what could not be done |
| `EMP Protection/Schedules/` | Five schedules as `.md` **and** `.csv` — `EMP_ZONE_SCHEDULE` · `ENVELOPE_PENETRATION_REGISTER` (10 rows) · `POE_PROTECTION_SCHEDULE` (5 points of entry) · `BONDING_AND_EARTHING_SCHEDULE` · `SHIELDING_EFFECTIVENESS_SCHEDULE` (12 rows) |
| `EMP Protection/QAQC/EMP_QAQC.md` | What was checked and what it returned, including the checks that **could not** be run and why. Records the one `dxfqa.py` false positive against the MEP title block |
| `EMP Protection/DXF/` | **Six A1 DXF**, AC1024 ASCII — `EM-001` design basis and zone key · `EM-101` EMP zone plan · `EM-102` **the entry path, EM-F1 drawn** · `EM-201` shielding effectiveness chart · `EM-301` EMP Zone 2 enclosure · `EM-302` penetration, bonding and earthing details. **0 errors, 0 warnings, 0 text overlaps** |
| `EMP Protection/Scripts/` | `em_proj.py` constants · `em_calc.py` derivations · `em_schedules.py` · `em_dxf.py` sheet library · `em_sheets.py` · `em_build_all.py` rebuilds everything |

> **`em_dxf.py` SUBCLASSES the shared `Drainage/Scripts/mep_dxf.py`** rather than editing it, so
> the EMP sheets carry the identical A1 standard to the R-series and the services drawings while
> **Drainage, HVAC and Schedule of Finishes regenerate byte-identically.** Verified: `git status`
> is clean on all five `Scripts/` directories.

### Added by EL1, 11 September 2026 — see H.20

> **The project's first electrical design. Deliberately basic — it stops at board level.**

| Folder / file | Contents |
|---|---|
| `Electrical/Documentation/ELECTRICAL_DESIGN_BASIS.md` | **The main document.** Sources (including the mains the master never recorded) · load schedule · the 15 kVA check · **EL-V1, the Mode 3 question** · the essential system and battery · distribution, cable entry and earthing · what it did not do · **what it unblocks** · **EL-V1…V7** · a QA/QC section |
| `Electrical/Documentation/00_README.md` | Package README |
| `Electrical/Calculations/EL_CALC_OUTPUT.txt` | Every figure with its inputs, formula and arithmetic — E.1 sources · E.2 loads · E.3 the generator check · E.4 the Mode 3 question · E.5 the battery, both cases · E.6 fuel · E.7 what it did not do |
| `Electrical/Schedules/` | `LOAD_SCHEDULE` (11 rows) and `DISTRIBUTION_AND_ESSENTIAL_SCHEDULE` (3 boards + the essential list and both battery cases), each `.md` and `.csv` |
| `Electrical/DXF/E-001_Single_Line_Diagram.dxf` | **One A1 sheet.** Mains + GEN-1 with changeover, `DB-M`, battery and inverter, `DB-E`, and `DB-Z2` inside the EMP Zone 2 enclosure through its PCI. **0 errors, 0 warnings, 0 text overlaps** |
| `Electrical/Scripts/` | `el_proj.py` · `el_calc.py` · `el_schedules.py` · `el_dxf.py` (subclasses `mep_dxf.py`, uses the CAM2/FS2 hooks) · `el_sheets.py` · `el_build_all.py` |

### Added by SG1, 11 September 2026 — see H.22

> **The project's first site selection and geotechnical section. It resolves nothing —
> what it supplies is provenance and quantified margin. The investigation it reports on
> reached about 1.5 m; the structure founds at (−)6.800.**

| Folder / file | Contents |
|---|---|
| `Site Selection and Geotechnical/Documentation/SITE_SELECTION_AND_GEOTECHNICAL_REPORT.md` | **The main document, 19 parts.** Why it exists and what it does not do · sources and the off-site limitation · site identification · **site selection and its SWOT, with what the selection got right and what it did not consider** · setting, level and the deck's self-contradiction · geology and the flow-contact hazard · **the investigation and the 5.3 m gap** · bearing, soaked vs unsoaked · rockhead and what it costs · **groundwater, the central question** · seismicity · meteorology · the `A.6` parameters against measured data · **the black cotton soil and its two exposures** · the deck against its own cited source · **14 findings** · **10 open items** · what changed and what did not · references |
| `…/Documentation/00_README.md` · `SG_DRAWING_INDEX.md` | Package README and the drawing register |
| `…/Calculations/SG_CALC_OUTPUT.txt` | **G.1 – G.14**, every conversion, reproduction and check with its arithmetic in full: units · reproducing the report's own arithmetic · the depth reached vs the depth needed · bearing · net pressure · rockhead and its cost · groundwater · the `A.6` parameters · the site · meteorology · seismic · the black cotton soil · the deck against its source · the parameter register |
| `…/Schedules/` | `TRIAL_PIT_SCHEDULE` · `SOIL_PROPERTY_SCHEDULE` · `ROCK_STRENGTH_SCHEDULE` · `METEOROLOGICAL_SCHEDULE` · `GEOTECHNICAL_PARAMETER_RECONCILIATION`, each `.md` and `.csv` |
| `…/QAQC/SG_QAQC.md` · `SG_DRAWING_VALIDATION.txt` | 13 executed checks · 7 declared non-checks · 6 declared deviations · byte-identity evidence for all seven other packages |
| `…/DXF/SG-001_Site_and_Geotechnical_Design_Basis.dxf` | The two sources and their limits · every `A.6` / `K.2` parameter against the evidence · all 14 findings · the bearing check at the measured value · the 10 open items |
| `…/DXF/SG-101_Site_Setting_Selection_and_Meteorology.dxf` | **Carries a NOT A SITE PLAN banner and means it.** Setting diagram (no scale) · SWOT · what the selection did not consider · the full meteorological record · the level conflict · the rainfall conflict · the wind warning · `SG-F7` |
| `…/DXF/SG-201_Geotechnical_Profile_and_Structure_Section.dxf` | **The sheet the package exists for.** Three trial pit logs at true level against a transverse section through the box, **1:25 both ways**, with everything below `(−)1.500` hatched as **NO DATA** and annotated with what a real investigation would have had to put there. **0 errors, 0 warnings, 0 text overlaps** |
| `…/Scripts/` | `sg_proj.py` · `sg_data.py` (both documents transcribed, nothing averaged or corrected) · `sg_calc.py` · `sg_schedules.py` · `sg_docs.py` · `sg_dxf.py` (subclasses `mep_dxf.py`, uses the CAM2/FS2 hooks) · `sg_sheets.py` · `sg_build_all.py` |

### Added by SG2, 11 September 2026 — see H.23

> **The project's first site layout plan.** Master `H.9`'s *"not determinable"* positions,
> five pipe lengths and the IS 2470 offsets — **determined**, on a coordinate and a 50 m
> envelope the project owner supplied.

| Folder / file | Contents |
|---|---|
| `Site Selection and Geotechnical/Documentation/SITE_LAYOUT_AND_EXTERNAL_WORKS.md` | **The SG2 document, 14 parts.** What changed and why it unblocks this · **site orientation fixed: +X = EAST** · the external works reserve · the positions · the offsets demonstrated · the five pipe lengths · **`SG2-F1`, the soak pit is a DEPTH problem** · the reserved fallback `DF-1`/`DF-2` · where the percolation test has to be done · **the `SG-V3` ruling and what it leaves standing** · **the `SG-V5` rainfall amendment** · what the siting work surfaced elsewhere · **`D3` partially closed** · what changed and what did not |
| `…/Calculations/SG2_SITE_CALC_OUTPUT.txt` | **S.1 – S.12.** Orientation · the 50 m envelope · the IS 2470 offsets one by one · **28 of 28 clearance checks, each against the rule it must meet** · the five pipe routes leg by leg · the soak pit against the water table and against the ground · the fallback sized · the percolation test located · the `SG-V3` ruling · rainfall · cross-package findings · the `D3` split |
| `…/Schedules/EXTERNAL_WORKS_SCHEDULE` | ST-01, SK-01…SK-04, IC-01, IC-02 — positions, sizes, levels, what each serves |
| `…/Schedules/EXTERNAL_PIPE_RUN_SCHEDULE` | The five runs, four with lengths and one `[U]` |
| `…/Schedules/SITING_CLEARANCE_SCHEDULE` | Seven rules — three `[C]` from S-06, four `[A]` adopted here, each with its reasoning |
| `…/Schedules/SG2_OPEN_ITEM_STATUS` | Every SG1 and SG2 item with what SG2 did to it |
| `…/DXF/SG-102_Site_Layout_Plan.dxf` | **THE PROJECT'S FIRST SITE LAYOUT PLAN.** 1:150 plan + 1:900 location key. Every external structure placed, every clearance dimensioned from confirmed geometry — and, on its face, **the eight things still missing** |
| `…/DXF/SG-202_External_Works_Siting_and_Soak_Pit_Finding.dxf` | The pit against the ground it is cut into · both water-table readings · the two checks behind `SG2-F1` · the reserved fallback · the percolation-test positions · the `SG-V3` ruling |
| `…/Scripts/sg_site.py` · `sg_site_calc.py` · `sg_site_docs.py` · `sg_site_sheets.py` | The SG2 generators. `sg_build_all.py` now runs SG1 then SG2 and validates all five sheets |

### Added by QA2 / MS2 / RC3, 11 September 2026 — see H.25, H.26, H.27

| Folder / file | Contents |
|---|---|
| **`CONSOLIDATED_PROJECT_REPORT.md`** (repository root) | **The project stated once, at its current state, in the order needed to reproduce it — 17 sections.** What it is and the protective boundary · codes · design basis (blast, ground, materials, loads, the cover, combinations) · geometry · **exit hatches and blast doors** · element-by-element design · the reinforcement register · the analysis models and how to validate them · services · site · drawings · works management · **what the design does not demonstrate** · the fourteen assumptions · the thirty-three open items · how to rebuild every package · the rules the project is held to. **It is a statement of the design, not a history of it — Part H remains the revision record and this master remains the authority.** It states no new value and resolves nothing |
| `current/staad/Scripts/validate_std.py` | **The `.std` validator the project did not have.** Reads each file the way STAAD reads it — truncated at the declared `INPUT WIDTH`, `-` continuations joined — and checks line width, ascending load case numbers, combination references, element and member topology, planarity, duplicates, orphan joints, thickness and property coverage, and **whether each self-equilibrating horizontal load case actually balances**. Re-run against the pre-MS2 coarse model it reports **all six defects H.26 lists**, including the 4.8 kN `LOAD 6` imbalance, from the file alone |
| `current/staad/00_README.md` | The six-model index, what each one is for, the two input-file rules that are silent when broken, and **the four things that can never be claimed from these files** |
| `current/staad/STD_VALIDATION_REPORT.txt` | Last validator run — **6 files, 0 errors** |
| `DRAWING QAQC/DRAWING_INDEX.md`, `qa_index.json` | Regenerated over **80 drawings** (was frozen at 68) |
| `DRAWING QAQC/QAQC_REPORT.md` **§10** | The QA2 addendum — why the index froze, the twelve sheets scanned for the first time, and the A-301 correction |

### Added by RC4, 11 September 2026 — see H.28

| Folder / file | Contents |
|---|---|
| `Owner Rulings RC4/Documentation/RC4_OWNER_RULINGS.md` | **The sixteen rulings and what each produced.** Thirteen actioned, three deliberately left open, four findings (`RC4-F1…F3`, `U8-F1`) and one new item (`RC4-V1`) |
| `…/Calculations/RC4_CALC_OUTPUT.txt` | **R.1–R.6 with every step shown** — the parapet re-derivation · the 96-hour heat balance across three bounds · the escape shaft ladder · D-05 and its trim steel · the raft strip-and-replace · both air shafts |
| `…/Calculations/RC4_SITING_OUTPUT.txt` | **T.1–T.7** — the 50 m envelope pin recovered from SG2's own arithmetic; the EAST sentry position re-run against every SG2 rule; the one check that fails and the 300 mm that fixes it |
| `…/Schedules/RC4_BOQ_ADDENDUM` | The two items the rulings added. **8 m³ each, rate `[A]`, NOT PRICED** — a second declared exclusion from WM3's lower bound |
| `…/Schedules/RC10_PACKAGE_IMPACT_REGISTER.md` | **RC10 (H.34) — the six package artefacts the rulings left stale**, each with what it says, what the master has ruled, and which generator would have to change. **Not applied** |
| `…/Calculations/RC5_CALC_OUTPUT.txt` | **R.7–R.9 (RC5, H.29)** — what the ventilation air can actually reject · the escape shaft head hatch as a protective closure · the generator day tank and the penetrations it avoids |
| `…/Calculations/RC6_CALC_OUTPUT.txt` | **R.10 (RC6, H.30)** — the excavation soil cap, three batter angles and a bench alternative costed in volume |
| `…/Calculations/RC7_CALC_OUTPUT.txt` | **R.11 (RC7, H.31)** — the CO₂ scrubber duty recovered from the project's own 9.9 h figure, and the fan check against EL1's allowance |
| `…/Scripts/rc4_calc.py` · `rc4_siting.py` · `rc5_calc.py` · `rc6_calc.py` · `rc7_calc.py` | The generators. Everything above is regenerated by running the five |
| `current/staad/Underground_Shelter_ks500000.std` | **The subgrade upper bound.** Identical to the reference model but for the `ELASTIC MAT` line and four `KFY` values — verified by diff |

### Added by PR1, 13 September 2026 — see H.36

| Folder / file | Contents |
|---|---|
| **`Project Report/MASTER_PROJECT_REPORT.pdf`** | **The master project report — 89 pages, 19 parts and 4 appendices.** The project stated once and in full: the engineering science behind every decision · codes clause by clause · site and geotechnics · the complete dimensional register · materials and detailing rules · every load derived · the analysis models and what they cannot prove · **element-by-element calculations with every substitution** · the reinforcement register and quantities · drawings and drawing quality · services, CBRN, EMP and life safety · site layout, finishes and concealment · works management · **what the design does not demonstrate** · the assumption and open-item registers · **the verification performed on its own arithmetic** · notation, a clause index, reproduction instructions and a revision index |
| `Project Report/Documentation/MASTER_PROJECT_REPORT.md` | **The report SOURCE.** Edit this, never the PDF |
| `Project Report/Scripts/report_render.py` | Markdown-subset → PDF typesetter. Adds no content of its own |
| **`Project Report/Scripts/report_figures.py`** | **Added by PR2 (H.37) — the 44 drawn report figures**, generated from `GEOM` / `LEV` / `COVER` in project coordinates, with the bounds checker. **NOT the issued drawings, and NOT reconstructions of the absent S-series sheets** |
| `Project Report/Scripts/report_verify.py` | **498 independent recomputations** of the figures the report reproduces |
| `Project Report/Calculations/REPORT_VERIFICATION_OUTPUT.txt` | Their output — **494 PASS, 4 differences, 0 unexplained** — and the two new findings `PR1-F1` and `PR1-F2`, **reported, not corrected** |

## I.3 SUPERSEDED / ARCHIVED

| Item | Superseded by | Note |
|---|---|---|
| Box length 21 600 | **22 000** (M1) | All pre-M1 dimensions east of X 14 800 |
| W6/W7 at 200 thk | **400 thk** (M1) | Finding F1 |
| ESC 2 at X 19 500 | **X 19 900** | M1 |
| Report Rev D approach ramp | Rev F covered stairwell | C1 |
| Report O.12 headhouse roof | Recomputed, B.7.1 | C2 |
| Sentry V<sub>b</sub> 50.5 kN (report) and 59.3 kN (hand) | **73.18 kN (STAAD)** | C7, C9 |
| Yield line 324.4 kNm/m | **162.2 kNm/m** | ERR-1 |
| Sump outside the wall | Inside, Bay 5 | — |
| Wall links T12 @ 250 | T12 @ 200 | — |
| B1 3-T16 / B2 4-T16 | **B1 4-T16 / B2 3-T20** | C9 |

> **⚠ SUPERSEDED 3 September 2026 — M1 is now implemented in the files.** This block previously read: *"There is no file in the uploaded set that reflects Modification M1. Every input DXF is at the pre-M1 geometry (box 21 600)."* That is **no longer true**. The six affected input DXFs and the underground `.std` were updated to the M1 geometry on 3 Sep 2026 (see H.4). Sheet S-06 already carried it. **Sheets S-01 to S-05, S-07 and S-08 are absent from the workspace and could not be regenerated — see H.4.**

---

# PART J — DEPENDENCY MAP

```
        [CLIENT INPUTS]  DBT · yield · standoff · occupancy · site
                 │
                 ▼
        [SITE INVESTIGATION]  rockhead · GWT · red-bole · k_s · SBC · percolation
                 │        ▲   SG2, 11.09.26 (H.23): the COORDINATE and a 50 m envelope
                 │        │   arrive, and the SITE LAYOUT follows - external works placed,
                 │        │   4 of 5 pipe lengths and 2 of 3 IS 2470 offsets closed.
                 │        │   D3 PARTIALLY closed: the LAYOUT exists, the SURVEY does not.
                 │        ▲
                 │        └── SG1, 11.09.26 (H.22): FED FOR THE FIRST TIME, and only to
                 │            ABOUT 1.5 m.  SEMT/67/15 + the P1 deck give rockhead, SBC,
                 │            phi, MDD/OMC, Zone III and the provenance of GWT (−)2.000.
                 │            BELOW 1.5 m THE NODE IS STILL EMPTY: red-bole, k_s, the
                 │            water table at (−)6.800 and rock-mass permeability are all
                 │            [N].  A1075 + A1080, both CRITICAL PATH, still to happen.
                 ▼
        [ARCHITECTURAL GEOMETRY — Rev F DXF]
                 │
                 ├──────────────► [MODIFICATION M1] ──────┐
                 ▼                                        │
        [LOADS]  blast 383 · cover 40.65 · earth+water · uplift · seismic
                 │
                 ▼
        [STAAD MODEL]  supports · k_s · plates · load cases · combinations
                 │
                 ▼
        [DEMAND]  moments · shears · axial · reactions
                 │
                 ▼
        [DESIGN CALCULATIONS — IS 456 / IS 13920]
                 │
                 ▼
        [REINFORCEMENT]
                 │
                 ▼
        [DXF GENERATORS (proj.py + dNN_*.py)] ◄── M1 enters here too
                 │
                 ▼
        [DRAWINGS S-01 … S-08]  →  [A1 PDFs]  →  [PRESENTATION]
```

## J.1 Change-propagation matrix — WHAT MUST BE UPDATED IF …

| If this changes | Then these MUST be revisited |
|---|---|
| **Any plan geometry** | `proj.py` constants → **all 8 DXF generators** → all drawings → STAAD node/plate geometry → every affected calculation → member schedule |
| **The 5 000 mm internal width** | **Roof M<sub>p</sub> ∝ L<sub>n</sub>²** → roof steel, roof links, thickness study, wall axial load, mat, flotation, quantities. **The most expensive single change in the project.** |
| **Box length only** | Nothing structural — the roof spans one-way across the width. Only quantities, uplift total, and drawing dimensions. **This is why M1 is cheap.** |
| **Any thickness** | d → A<sub>st,req</sub> → M<sub>u</sub> → utilisation → x/d → shear → links → cover check → BBS → DXF → self weight → seismic weight → flotation |
| **Blast p<sub>so</sub>, t<sub>d</sub>, or μ** | DLF → 383 kPa → **every element of the box** + headhouse roof + blast doors + blast valves + t<sub>d</sub>/T quasi-static justification |
| **Groundwater level** | Earth+water gradient → wall design → uplift → **flotation FoS at all 4 stages** → dewatering strategy → waterproofing class → sump duty |
| **k<sub>s</sub>** | Mat moments (sensitive) → mat steel → link grid. **Run both bounds.** |
| **SBC** | Bearing check only (currently 1.8 %/12.5 % — enormous margin) |
| **Material grade** | E<sub>c</sub> → period T → t<sub>d</sub>/T ; f<sub>ck,dyn</sub> → all A<sub>st,req</sub> ; τ<sub>c</sub> Table 19 → all links ; τ<sub>bd</sub> → **all L<sub>d</sub> and laps** → all BBS cut lengths |
| **Cover** | d → every flexural result; also EMP spacing and IS 3370 surface-zone steel |
| **Sentry post V<sub>b</sub> (C9)** | Column shears → beam moments → B1/B2 steel → capacity-design shear → hoop spacing → SCWB check → column biaxial → footing moment |
| **R factor (3.0 vs 5.0)** | V<sub>b</sub> ×0.6 → everything in the row above; **plus the infill would need out-of-plane restraint** |
| **Support conditions in STAAD** | Demand distribution → all design; **and note flotation can never be taken from the model** |
| **Reinforcement** | M<sub>u,prov</sub> → utilisation → x/d → p<sub>t</sub> → **τ<sub>c</sub> → links** → capacity-design shear (IS 13920) → SCWB → BBS → DXF |
| **Headhouse geometry** | Roof span → the three-method analysis → steel + links; wall load path; **HW3 line-load check on the pressure slab** |

---

# PART K — KNOWN ISSUES, ASSUMPTIONS AND UNCERTAINTIES

## K.1 RULED — revision RC1, 10 September 2026 (Part H.14)

> **Every item that could be closed by choosing the better-evidenced value HAS BEEN
> CLOSED, on the user's instruction of 10 September 2026 to remove all inconsistencies by
> choosing the best option available. Each ruling below states the basis it was decided
> on. Nothing was closed by guessing, and nothing that requires information the project
> does not contain has been closed at all — those items are in K.1b.**

| # | Item | Ruling | Basis |
|---|---|---|---|
| **U1** | Sentry post base shear (C9) — STAAD **73.18 kN** vs hand **59.3 kN** | **CLOSED. 73.18 kN governs** | The model now prints its own seismic-weight summary: roof 331.46 + floor 400.34 = **W 731.80 kN**, and V<sub>b</sub> = 0.100 × 731.80 = 73.18 returns A<sub>h</sub> = **0.1000 exactly**. Rebuilding both storey weights from the model's own load blocks reproduces 331.46 and 400.34 to the kN, and the 139.1 kN gap to the B.8 hand check resolves completely: **107.9 kN** is half the first-storey infill, which the B.8 floor line does not allocate, and **31.1 kN** is the model taking the full 450 beam depth in `SELFWEIGHT` while also applying the full slab pressure where B.8 nets the beam to 300. Nothing is unexplained, and **every member is already designed to the higher value** |
| **U4** | STAAD analysis / design command blocks | **CLOSED** | Answered from the `.std` files on 3 Sep 2026 — both models end `PERFORM ANALYSIS PRINT STATICS CHECK`, no P-Delta. **The table had simply never been updated; that was itself an inconsistency** |
| **U5** | Underground plate table and supports | **CLOSED** | Answered 3 Sep 2026 — **1 138 shell elements**, four thickness groups (mat 600 / roof 900 / perimeter 600 / internal 200–400), `ELASTIC MAT DIRECT Y SUBGRADE 100000` |
| **U6** | Node 213, sentry post | **CLOSED. There is no node 213** | The sentry model has **twelve joints**. The item was chasing a row that does not exist |
| **U7** | Beam 16 (211→212), sentry post | **CLOSED. Present** | `16 211 212` is in the model exactly as reconstructed |
| **U9** | Engineered cover (C17) — 40.65 stated vs 39.15 summed | **CLOSED. 40.65 held; A.7.3 made self-consistent** | The table now shows the layer sum **39.15** plus a **declared allowance of +1.50**. 40.65 is in A.7.4, Part L and `DL2` in every underground `.std`, and it is the larger. **COMB 103 stays 448.15 kPa; no bar, spacing or link changes.** Adopting 39.15 instead would lighten the roof and force a re-analysis that cannot be run here |
| **U10** | Sump-pit base (C18) — 400 vs S-06's 300 | **CLOSED. 400** | (−)8.000 − (−)7.600 = **0.400**. Arithmetic, and F.1 says 400 independently. S-06's text is a transcription error |
| **U11** | Soak pit (C19) — 21.99 m² against 22.50 required | **CLOSED. SK-01 widened: diameter 2.0 → 2.200 m, depth unchanged at 3.500 m → 24.19 m², +7.5 %** | Widening beats deepening: deepening drives the pit further below the design GWT at (−)2.000, where it cannot soak at all. A pit that fails its own stated requirement is not something to leave standing, and the fix costs one course of extra excavation. **The mandatory percolation test (A7) still governs the final size** |
| **U12** | Superseded stairwell catchment (C20) | **CLOSED. Rev F governs; the 0.10 L/s is retained as a declared conservatism** | Precedent **C1** — where a drawing and an older document disagree, the drawing governs. Removing 0.10 L/s changes no pump, no pipe and no pit (the stairwell pump is 20 × it), and deleting a superseded number would hide the history. Both figures are shown and labelled on D-103 |
| **U13** | Filter duty (C21) — 250 vs 300 m³/h | **CLOSED. 300 m³/h. A.3 has been CORRECTED from "2 × 250"** | Four independent lines point to 300 and none to 250: S-06 states 300 in **nine** places; every other S-06 figure reproduces only at 300; **250 fails S-06's own 264 m³/h FEMA 453 criterion**, so it is not the cautious option but a demonstrably inadequate one; and the owner's own cost estimate prices **2 × 300**. A.3 was the single outlier |
| **QA-1** | A-301 cannot be plotted at 1:50 on A1 | **CLOSED. A0 confirmed** | The scale is a measurement statement and must not be changed to fit paper; the drawing is 880 mm at 1:50 against an A1 area of 821 mm, so A1 is impossible. Splitting the sentry post onto its own sheet would break a continuous 44 m elevation, which is the whole point of the drawing. **A0 is the only option that keeps both the scale and the drawing intact** |
| **QA-2** | Sheets that do not fill their paper | **CLOSED — RULED: ACCEPTED AS DRAWN, and the reason is now stated instead of left as a question.** Six sheets (R-202 39.3 %, D-002 and R-003 36.7 %, R-402 and R-002 34.1 %, R-201 31.5 %) share an empty **(0, 0)–(651, 220–302)** strip. **No sheet was re-scaled, renumbered or combined** | The space is real, and every way of removing it is worse than it is. **Every one of these sheets is correct, complete and legible — emptiness is not an error.** (i) **Re-scaling** would make the stated scale a layout variable instead of a measurement statement, and 1:20 for a 400 wall section is the right scale for that detail regardless of how much paper it leaves. (ii) **Combining or renumbering** sheets would break cross-references on other sheets, the drawing index, Part E.2 and the "N OF 30" numbering, for **zero** engineering benefit. (iii) **Reflowing the blocks moves the void, it does not remove it** — the content on these six is genuinely sparse for an A1, and stretching text leading across 300 mm of paper reads worse than the space does. **If you want them combined, that is a register-level decision and it is yours to take — say so and it is a contained job** |

## K.1b STILL OPEN — these need information the project does not contain

### K.1b-INDEX — the live count, and how to verify it

> **ADDED BY RC9, 12 September 2026 (Part H.33), TO CORRECT AN ERROR THIS SESSION INTRODUCED.**
> Revisions RC4 to RC8 ruled on items and recorded each ruling in its Part H narrative and in
> `K.1e` — **but thirteen of the rows in the table below were never annotated**, so the table
> still read as thirty-four open items while the narratives claimed twenty-one, then fifteen,
> then thirteen. **All three of those counts were wrong.** Every row is now annotated, and this
> index exists so the count can be verified by reading rather than by trusting a sentence.
>
> **THE TABLE BELOW HAS 35 ROWS. EIGHTEEN ARE STILL OPEN** — nine narrowed by a ruling, two
> annotated but not narrowed, six untouched, one new.
>
> **Updated by DR-A2, 12 September 2026 (Part H.35):** one row added, `DR-A2-V1`. ~~34 rows,
> seventeen open~~ — preserved under M.11; the figures above are current.

| State | Count | Items |
|---|---:|---|
| **STILL OPEN — ruled, and NARROWED by the ruling** | **9** | `U8` (parapet half-derived; **one dimension missing**) · `WM-V9` (face ruled; **slope-stability assessment outstanding**) · `FS-V7` (ladder designed; **no fall-arrest, no rest platform, injured-person question**) · `EM-V6` (**structural half designed, EMP half open**) · `EL-V2` (day tank sized; fuel type, rate and vendor open) · `EL-V7` (duty computed; absorber and soda lime open) · `SG-V6` (specified and measured; **rate `[A]`**) · `SG2-V4` (**intake/exhaust closed, PLUME half open**) · `RC4-V1` (**rejection path narrowed to "the ground, unmodelled"**) |
| **STILL OPEN — annotated, but NOT narrowed** | **2** | `EM-V2` and `EL-V3` — RC8 documented the **circularity** between them (the enclosure is sized to fit a bay, the 1.50 kW is chosen to give the enclosure a basis, **and neither is evidence**). **Nothing about either was resolved** |
| **STILL OPEN — untouched** | **6** | `WM-V6` · `EM-V4` · `EM-V5` · `SG-V1` · `SG-V2` · `SG-V7` |
| **STILL OPEN — NEW, raised by `DR-A2` (H.35)** | **1** | `DR-A2-V1` — **`SU-01` has no cover, and Bay 5 is 1560 wide against a 1500 opening** |
| **CLOSED by ruling** | **16** | `U2` `U3` `WM-V7` `CAM-V5` `EM-V3` `EL-V4` `EL-V6` `SG-V4` `SG-V5` `SG-V8` `SG-V10` `SG2-V1` `SG2-V2` `SG2-V3` `SG2-V5` `DR-A1-V1` |
| **MOVED to `K.1f`** — a declared scope boundary, never a gap | **1** | `EL-V5` |
| | **35** | |

> **Closed and moved rows are KEPT IN THE TABLE under M.11**, each carrying its ruling in the
> first cell and its original entry beside it. **Nothing is deleted; the count is stated instead.**
>
> **Of the seventeen still open, four are the ones a reviewer should look at first:**
> **`SG-V2`** — the investigation reached about 1.5 m against a formation at (−)6.800 ·
> **`EM-V6`** — two 1400 dia holes in the protective boundary whose bonding is still undesigned ·
> **`SG2-V4`** — a CBRN shelter that cannot state which way a release drifts ·
> **`RC4-V1`** — a sealed box with a 4 kW surplus and an unmodelled rejection path.

> **RC4, 11 September 2026 (Part H.28) — THE OWNER RULED ON SIXTEEN OF THESE, ITEM BY ITEM.
> K.1b falls from thirty-three to twenty-one.**
>
> **CLOSED and moved to K.1e (8):** `U2` · `U3` · `WM-V7` · `EM-V3` · `EL-V6` · `CAM-V5` ·
> `SG2-V3` · `FS-1 / D-05`.
> **RULED AND CHANGED, but still open, and their rows below now say how (5):** `FS-V7` ·
> `U8` · `U4 / DR-A1-V1` · `SG-V6` · `A4` (K.2).
> **DELIBERATELY LEFT OPEN by the owner (3):** `EM-V4` · `EM-V5` · `SG-V7` — **and two of the
> three were SHARPENED by rulings elsewhere in RC4.** Leaving an item open is a decision with
> consequences, not a way of avoiding one.
> **NEW (1):** `RC4-V1`.
>
> **RC5, 12 September 2026 (Part H.29) — four more, and `A13` closed on the evidence.**
> **RULED AND NARROWED, still open (3):** `RC4-V1` · `EM-V6` (its EMP half) · `EL-V2`.
> **LEFT OPEN (1):** `WM-V6`. **K.1b holds at twenty-one** — nothing closed, three narrowed —
> **but two findings came out of it**, `RC5-F1` (the ventilation air cannot reject the heat and
> was never sized to) and **`RC5-F2` — two 1400 dia penetrations of the protective boundary have
> no specified closure.** **(K.1b held at twenty-five, not twenty-one — corrected by RC9, H.33.)**
> `A13` closed in K.2 without a ruling: the `.std` the register asked for
> has been in the workspace since H.4.
>
> **RC6, 12 September 2026 (H.30):** `WM-V9` **RULED** — batter the soil cap, vertical in rock.
> **K.2 falls from fourteen to seven, and the seven that remain are exactly the site
> investigation.**
>
> **RC7, 12 September 2026 (H.31) — K.1b GOES FROM TWENTY-ONE TO FIFTEEN.**
> **CLOSED (6):** `EL-V4` the mains does not gate the protective design · `SG-V4` `SG-V5` `SG-V8`
> `SG-V10` — **four defects in the SUPPLIED DOCUMENTS, not in this design record**, on which the
> project's position was already correct · **`SG2-V1` — the owner confirms no well within 15 m,
> so the IS 2470 offset set is COMPLETE for the first time.** **RULED AND NARROWED (1):**
> `EL-V7`, a 0.18 m³/h CO₂ duty and a 75 m³/h loop. **`SG2-V2` was NOT addressed and STAYS
> OPEN.**
>
> **RC8, 12 September 2026 (H.32) — K.1b GOES FROM FIFTEEN TO THIRTEEN.**
> **CLOSED (1):** `SG2-V2`, on the layout's immunity — every offset is relative to the structure,
> so a fence distance changes where the reserve sits, never whether it works.
> **SPLIT (1):** `SG2-V4` — **the intake/exhaust half is CLOSED** (25.30 m end-to-end, robust
> whatever the wind does, which is why SG2 chose geometry over meteorology); **the PLUME half
> stays open, and must.**
> **RECLASSIFIED (1):** `EL-V5` leaves this register for the new **`K.1f`** — it is a declared
> scope boundary, not a gap.
> **DOCUMENTED, BOTH STILL OPEN:** `EM-V2` and `EL-V3` are **each holding the other's
> placeholder** — the enclosure is sized to fit a bay, the 1.50 kW is chosen to give the
> enclosure a basis, **and neither is evidence.**

> **These are NOT inconsistencies.** Each is a single position the project holds, with
> nothing contradicting it. What they need is a decision, a datum or a design from
> outside this workspace, and no amount of choosing between recorded values can supply it. They are
> listed separately so that a closed conflict is never confused with an open question.
>
> **THREE EXCEPTIONS, ADDED BY SG1 (11 Sep 2026, H.22), AND THEY ARE MARKED AS SUCH.**
> `SG-V4`, `SG-V5` and `SG-V8` **are** disagreements — but they are disagreements **inside
> the supplied documents**, not inside this project's own design record. **RC1's rule still
> holds: a conflict that can be ruled on the evidence is ruled.** These cannot be, because
> both sides are external, neither cites a source, and choosing between them would be
> inventing evidence. **None of the three changes a design value.**

| # | Item | The project's position | What it actually needs |
|---|---|---|---|
| **U2** |**CLOSED — RC4 (H.28): NO DIRECT HIT IS A REQUIREMENT. The design stands as it is.** *Entry as it stood before the ruling, preserved under M.11:* Is a direct hit a requirement? | **No direct hit is designed for.** The 2.0 m cover is sized for prompt neutron and gamma attenuation (A.7.3), not for a penetrating hit; the burster slab breaks up a penetrating item, it does not defeat one. This is stated, consistent, and carried through every load case | **A military representative's sign-off.** If a direct hit becomes a requirement the cover depth and the burster design both change |
| **U3** |**CLOSED — RC4 (H.28): p_so 344.7 kPa and t_d 0.13–1.33 s ARE the stated basis; the yield stays unstated rather than invented.** *Entry as it stood before the ruling, preserved under M.11:* Design basis threat yield | **50 psi with t<sub>d</sub> 0.13–1.33 s is the stated basis and is what every load case uses.** The pressure and duration are the design inputs; the yield behind them is not needed to execute the design as recorded | Client confirmation. It would drive the prompt-radiation cover depth if it moved |
| **U8** | Roof projection + parapet, 4.162 kN/m. **RULED AND HALF-CLOSED — RC4 (H.28): the parapet is CONFIRMED at 300 × 150** | **The parapet term is now `[C]` and exact: 0.300 × 0.150 × 25 = 1.125 kN/m.** The residual **3.037 kN/m** is the roof projection | **ONE DIMENSION.** `U8-F1`: **the projection dimension is recorded nowhere in this project.** Back-solving gives 810 mm (slab alone) or 578 mm (slab + finish); neither is round, neither is drawn, **neither is adopted.** 4.162 continues to be used as given — no member force changes |
| **WM-V6** | Sentry seismic weight after SP-B1 | **The direction is certain and favourable.** Brick at 20 kN/m³ over 0.190 × 2.600 gives **9.88 kN/m** against the **13.000 kN/m** modelled, so W falls, V<sub>b</sub> falls, and every member designed to 73.18 kN is over-designed. **Nothing is unsafe and nothing is inconsistent** | A STAAD re-run to put a number on the margin. **STAAD.Pro is not available in this environment**, so it is confirmation, not risk |
| **WM-V7** |**CLOSED — RC4 (H.28): BALLISTIC PROTECTION IS NOT REQUIRED. Brick stands.** *Entry as it stood before the ruling, preserved under M.11:* Ballistic function of the Rev F panels | **Brick masonry does not give ballistic protection, and every drawing now says brick.** There is no longer any inconsistency — the drawings, the master and the Works Management package all agree | **A client / military decision** on whether that protection is required at all. No drafting or design work in this project can supply it |
| **WM-V9** | Excavation working space and face treatment. **RULED — RC6, 12 Sep 2026 (H.30): BATTER THE SOIL CAP, VERTICAL IN ROCK BELOW IT.** The project measured a vertical unbenched face for the full 6.800 m; SG1 then measured **rockhead at 0.9–1.5 m** with a **CH horizon at FSI 60–65 %** on top. **That is 1.0–1.5 m of very-high-swelling clay standing vertically on rock, undercut by the rock excavation, and open across a monsoon under the SG2-V5 acceptance.** Adopted: **1 : 1 minimum batter over the soil cap, grade to rockhead, all four sides; vertical retained in rock.** Extra excavation **76.4 m³ at 1:1, 117.6 m³ at 1.5:1** `[R]`; **the 1.000 m working space is at FORMATION and does not move.** **1 : 1 is a MINIMUM, not the answer — the angle is the geotechnical engineer's** `[A]` | **The slope-stability assessment is STILL OUTSTANDING.** What RC6 closes is the measurement basis: the project now states a face treatment instead of an unexamined vertical. **And it produces 76–118 m³ more CH clay, on top of SG-V6's 8 m³ — exactly the material `SG-V7` warns against re-laying as the cover turf** |
| **FS-V7** | **How is either escape shaft climbed?** Raised by drawing F-102, 10 Sep 2026 (H.18). **RULED AND CHANGED — RC4, 11 Sep 2026 (H.28): LADDER DESIGNED, FALL-ARREST DEFERRED.** A.4.9 carries the ladder. **Three things are still missing and the ruling knows it: no fall-arrest, no rest platform (a 1400 bore cannot take one without blocking the escape), and the injured-person question — a vertical ladder cannot pass a stretcher.** The row below is the position BEFORE the ruling, preserved under M.11 | **Was: nothing. The project held no position at all.** ESC 1 emerges at (+0.150) and ESC 2 at (+0.700) against a floor at (−)6.100 — a **6.250 m** and a **6.800 m** climb `[D]` — and **no ladder, rung or fall-arrest is specified in either shaft anywhere** | **A design.** Not a ruling between recorded values: there are no recorded values. It also needs an answer on whether an injured person is expected to use a shaft at all, which is a client question |
| **CAM-V5** |**CLOSED — RC4 (H.28): SH-2 head level +1.500, the same gooseneck head as SH-1 `[A]`.** *Entry as it stood before the ruling, preserved under M.11:* **Head level of the generator air shaft SH-2.** Raised by drawing C-101, 10 Sep 2026 (H.18) | Its **600 × 600** size and its **BV-4 / BV-5** duty are confirmed; **how far it stands above finished grade is recorded nowhere** | **A datum.** Until it exists SH-2 cannot be assessed as an above-ground signature, and C-101 draws it with its height flagged `[N]` rather than assumed |
| **EM-V2** | EMP Zone 2 dimensions. **CIRCULARITY DOCUMENTED — RC8 (H.32). STILL OPEN, and so is its partner `EL-V3`** | **Required and unspecified for four revisions; EM1 supplies a set that demonstrably fits bay 3** — 2 400 × 1 600 × 2 200 external, clear of the Y 2500–3400 circulation route, with a 300 survey gap on every free face. **Every dimension is `[A]`** | **An equipment schedule.** **AND THE ANSWER IT GOT IS ITS OWN PLACEHOLDER:** EL1's `Z-01` is *"an allowance, NOT a schedule"*, justified as *"the number EM-V2 was waiting for"*. **So the enclosure is sized to fit a bay, the load is chosen to give the enclosure a basis, and NEITHER IS EVIDENCE.** What breaks the loop is an **operational equipment list** — a client input, not a calculation. **Until it exists the 2400 × 1600 × 2200 and the 1.50 kW are a matched pair of placeholders, not two independent confirmations** |
| **EM-V3** |**CLOSED — RC4 (H.28): BAY 8 IS INSIDE THE EMP BOUNDARY. BV-4/BV-5 now REQUIRE honeycomb WBC panels.** *Entry as it stood before the ruling, preserved under M.11:* Is bay 8 inside the EMP boundary? | **No EMP boundary has ever been drawn.** Bay 8 is outside the *gas-tight envelope* (A.2) — but that is a **CBRN** boundary and says nothing about EMP | **A client decision.** If bay 8 is in, BV-4/BV-5 need honeycomb WBC panels; if it is out, the 15 kVA generator, its control panel and every cable in bay 8 are unprotected and **the shelter loses power to the pulse** |
| **EM-V4** | Communications | **There is none.** No antenna, mast, feeder or comms design exists anywhere in the project, so MIL-STD-188-125-1 §5.7.6 has nothing to apply to | **A communications design.** An antenna is by definition a deliberate conductor from outside to inside — the hardest EMP penetration there is — and it is also a concealment signature (CAM1) |
| **EM-V5** | PD-05's pipe material | **Unspecified — as is every pipe material in the project.** The drainage package names no material for any run | **A material.** Metallic → bond it 360° to the entry plate and its exterior becomes shield. Plastic → the bore is an aperture *and* the water column is a conductor, needing a metallic spool piece nobody has specified |
| **EM-V6** | Escape-shaft head hatch and blast-door RF performance. **RULED AND SPLIT — RC5, 12 Sep 2026 (H.29): the hatch is DESIGNED AS A STRUCTURAL ELEMENT; the EMP bonding stays with the EMP package, so THIS ROW STAYS OPEN FOR ITS EMP HALF.** And the design raised **`RC5-F2`: these are 1400 dia bores through the PRESSURE SLAB, which A.2 names as part of the protective boundary — so each head is a 1.54 m² hole in that boundary and nothing in the project had ever stated what it must resist structurally.** Designed to the full **383 kPa**: 589.6 kN on the leaf, M 38.71 kNm/m, a ribbed steel weldment on a cast-in seating ring with quarter-turn dogs against uplift, counterbalanced and openable from inside. **A flat plate would be 32 mm and 505 kg — unliftable, which is why it is not one.** The row below is the position before the ruling | **Was: neither exists.** Lining a 1 400 shaft does not work — it propagates above 125.5 MHz however well it is lined; the treatment is a **bonded conducting hatch at the head**. Blast Door 1's frame is already cast in and welded to the cage (A.5), which is the right start | **Vendor data.** Both sit directly on the protective boundary |
| **EL-V2** | Generator fuel type, quantity and storage. **RULED AND NARROWED — RC5 (H.29): a DAY TANK INSIDE.** 210 L usable / **250 L nominal** / 275 L bund, bay 8, welded steel, contents gauge and low-level alarm to the S-01 panel. **The fill and the vent are routed up the EXISTING SH-2 bore so NO new envelope penetration is created** — the same instinct the owner applied to RC4-V1. **Fuel type still unconfirmed, 0.35 L/kWh still `[A]`, no vendor set, no rate. Needs an HVAC/EMP fit check: two DN25 lines sharing a 600 × 600 bore with two DN350 blast valves.** The row below is the position before the ruling | **Was: none specified.** EL1 derives **≈ 210 L for a 96 h run** (600.6 kWh at 0.35 L/kWh `[A]`) — the first number anyone has put on it | Client / vendor. Same root as **FS-V4** and **R-8** |
| **EL-V3** | Equipment schedule for EMP Zone 2. **CIRCULARITY DOCUMENTED — RC8 (H.32). STILL OPEN, with `EM-V2`** | **`Z-01`, a 1.50 kW allowance.** It gives EM-V2 a basis, not an answer — **and EM-V2's own dimensions are a fit to bay 3, so the two corroborate each other and neither is evidence** | **An operational equipment list.** Client input, not a calculation |
| **EL-V4** | Incoming mains capacity. **CLOSED — RC7 (H.31): THE MAINS DOES NOT GATE THE PROTECTIVE DESIGN.** The shelter runs on **GEN-1 alone for the full 96 h** — RC2 allows it in closed mode, RC4 put it inside the EMP boundary, connected load **7.360 kVA against 15 kVA = 49 %**, battery 4 h if the set is down | **The supply is confirmed only by the owner's programme.** No capacity exists anywhere | **It still blocks a fault level and discrimination study FOR THE NORMAL-MODE INSTALLATION, and blocks nothing protective.** No capacity figure invented |
| **EL-V5** | ~~Circuit, cable, luminaire and socket schedules~~ — **MOVED OUT OF THIS REGISTER BY RC8, 12 Sep 2026 (H.32). It is a DECLARED SCOPE BOUNDARY, not a gap: EL1's own opening paragraph says *"A BASIC PACKAGE, ON PURPOSE. It stops at board level."* See `K.1f`** | **None — deliberately.** EL1 stops at board level | Detailed design stage. **It closes when that stage is commissioned, not by any work in this project** |
| **EL-V6** |**CLOSED — RC4 (H.28): the 96-hour heat balance is COMPUTED — 6.363 kW sensible, +13.2 K to about 39 °C, 4 kW to hold 30 °C. **It opened `RC4-V1` in its place**.** *Entry as it stood before the ruling, preserved under M.11:* Cooling | **No cooling plant exists anywhere in the project**, so no cooling load appears in the schedule. A sealed 332.8 m³ box with 9 occupants and a dehumidifier has a heat balance nobody has computed | **HVAC.** Referred, not resolved |
| **EL-V7** | CO₂ scrubber air movement. **RULED AND NARROWED — RC7 (H.31).** The production rate was already embedded in the HVAC package's own 9.9 h figure: **0.18 m³/h of CO₂**, 17.28 m³ over 96 h. **Adopted: a 75 m³/h recirculation loop.** A 75 m³/h fan draws **≈ 11.6 W against EL1's 100 W allowance — now CHECKED rather than assumed, and NO electrical value changes.** **A closed-mode device, and not optional: without it the envelope reaches 1.0 % in 9.9 h against a 96 h occupancy** | **Was: in no schedule** | **The absorber, bed, residence time, soda lime charge and single-pass efficiency are all `[N]`**, and **where in bay 5 it stands** — the tightest bay at 1560 clear, where HV-F3 already records 110 mm at the sides |
| **SG-V1** | **The geotechnical data is OFF-SITE** *(SG1, 11 Sep 2026, H.22)* | **SEMT/67/15 investigates the G Building, the H Building and the Mess Building.** The project plot is a separate undeveloped area east of the CTW blocks. The carry-across rests on the report's own para 5 — *"horizontally bedded and more or less uniform in character over a wide area"* — and is an **`[A]` of the SG1 package**, not a finding of the report. The report's own spread (rockhead 0.9 → 1.5 m over three locations) shows how much that uniformity permits | **The confirmatory site investigation `A1075` located ON THIS PLOT**, not repeated from the report. **No investigation has ever been made on the project plot** |
| **SG-V2** | **DEPTH OF INVESTIGATION — the governing item** *(SG1)* | **The pits reached about 1.5 m. The formation is at `(−)6.800` and the sump base at `(−)8.000`.** There are **5.3 m of completely unlogged ground** under the whole structure. Only sentry footing F1 at `(−)2.000` is inside the investigated horizon, and only just | **Boreholes with core recovery and RQD to well below `(−)6.800`, logging every flow contact and red-bole seam** — that is the case that **sizes the mat** (`B.3` Case 2, 84 % utilised) — with **packer permeability** at the contacts and a **plate load test** for k<sub>s</sub> at **both** bounds |
| **SG-V4** |**CLOSED — RC7 (H.31): a defect in the SUPPLIED DOCUMENT, not in this design record. **Neither level is adopted**.** *Entry as it stood before the ruling, preserved under M.11:* **Site level and fall** *(SG1)* | **The P1 deck contradicts itself.** Its contour map puts the plot between the **580 and 581 m** contours; its elevation profile reads **593.9 → 596.2 m** over 26.8 m. **They differ by 12–16 m in level and about four times in gradient**, and neither is tied to the project datum. Neither is adopted | **A levelled benchmark on the plot** and a spot-level survey. It changes **no calculation** — the project works on a local datum with grade `= 0.000` — but the **cut and fill**, the **berm toe** and the point where the `BS1` 1:50 crossfall daylights all wait on it, and on **D3** |
| **SG-V5** |**CLOSED — RC7 (H.31): a defect in the SUPPLIED DOCUMENT. **No figure was substituted, and no pipe, pit, pump or structure is sized by rainfall**.** *Entry as it stood before the ruling, preserved under M.11:* **Annual rainfall** *(SG1, **AMENDED by SG2**, H.23)* | **SG2 settled which side is wrong.** The **June-to-October mean alone** at Pune Shivajinagar over **1978–2020 is 852.5 mm** `[R]` — **1.4 to 1.7 times the SEMT report's whole YEAR** of 500–600 mm. **`SG2-F2`: the soil report's figure is the one that is wrong, not the deck's**, which is the opposite of SG1's first guess. The deck is not vindicated either: its Jun–Oct total is **18 % below** the 42-year mean and its **October figure still does not fit a Deccan monsoon**. **No IMD normal could be retrieved — ten meteorological hosts were probed and all ten were refused by the session's egress policy (403) — and none is invented.** | **A named IMD station normal**: the *Climatological Tables of Observatories in India 1991–2020*, or the IMD Climate Data Services Portal, or the National Data Centre — with the station index and period printed on it. **And separately an IDF relation** for `DR-D1`. **Note what this does NOT reach: not one pipe, pit, pump or structure in this project is sized by rainfall** (H.23), so no design value waits on it |
| **SG-V6** | **The entry stairwell raft founds in black cotton soil** *(SG1)*. **RULED — RC4 (H.28): STRIP AND REPLACE, SPECIFIED AND PRICED.** Strip the CH horizon to 1.000 m below existing ground over 4.410 × 4.000 m, replace with granular fill at **FSI ≤ 20 %** (IS 2720 Pt XL) in 200 layers to **≥ 95 % MDD**, extending **1.000 m beyond every raft edge** so the raft never bears partly on replaced and partly on natural CH. **BOQ item added: 8 m³, rate `[A]` — not invented.** **It collides with `SG-V7`, which the owner left open: this work produces a stockpile of exactly the material SG-V7 warns against re-laying as the cover turf.** The row below is the position before the ruling | `A.4.7` records a *"Stepped RC raft 300 thk **on compacted fill**"* from the top landing at `0.000` to the platform at `(−)2.000`; **its top founds at about `(−)0.300`, inside the 0.18–1.0 m CH horizon**, which is measured at **FSI 60–65 %** — very high swelling. *"On compacted fill"* implies a strip and replace, but **no specification says so and no BOQ item exists**. This is **heave**, not bearing | **A specification** for stripping and replacing the CH horizon under the raft, and the quantity priced. The stairwell is expendable against **blast** — **heave is not a blast problem, and this is the only primary access to the shelter** |
| **SG-V7** | **The concealment turf may be an expansive clay** *(SG1)* | `A.7.3` puts **300 topsoil / turf** at the top of the cover and `CAM2` makes it *the* concealment layer, **"re-laid from the site's own stockpile"**. If the site's own topsoil is this CH clay, the concealment layer **cracks in the dry season** (a concealment defect — `CAM2`'s whole subject), the cracks **feed the 150 granular filter directly**, and the wet/dry cycles **pump fines into** the filter, which is the one thing it exists to stop. **The load is unaffected** — 300 at 18 kN/m³ = 5.40 kPa is right for a black cotton soil | **A specification**: a swell limit on the stockpiled topsoil, or imported non-expansive topsoil, priced. A `CAM2` coordination decision. `BS1`'s crossfall still works and is unaffected |
| **SG-V8** |**CLOSED — RC7 (H.31): a defect in the SUPPLIED DOCUMENT. **All three mis-attributed statements are used nowhere**.** *Entry as it stood before the ruling, preserved under M.11:* **Three P1 deck statements are not in the report they cite** *(SG1)* | Slides 29 and 30 both read *"Source : SEMT wing, CME"*. **"SBC = 300 kN/m² at 1.5 m"** is not any value in the report; **"Murrum … SBC of 25–30 kg/cm²"** — the report says 2.07–5.18, and 25–30 is the *sound basalt* band; **"609–900 kg/cm² unsoaked"** — the report says 752–900, and 609 appears nowhere. **None affects the design**, which uses none of them | **Correction at source before the next presentation.** The deck's two other soil statements are right: *"Ultimate = SBC × 2.5"* is Appendix B's own relationship, and *"safe for water table at 2 m below GL"* is the **provenance of `(−)2.000`** |
| **SG-V10** |**CLOSED — RC7 (H.31): a defect in the SUPPLIED DOCUMENT. **Flagged `[U]`, not asserted; `SG-V2` governs regardless**.** *Entry as it stood before the ruling, preserved under M.11:* **The date of the SEMT field work is not stated** *(SG1)* | The report is raised on a letter of **20 May 2015** but **nowhere states when the trial pits were dug**. If the work followed promptly it was the **pre-monsoon minimum** — the one time of year a trial pit is least likely to find water. **That is inference and is tagged `[U]`, not asserted** | The field-work dates from the SEMT wing, or acceptance that the *"no water table"* observation is **season-unknown**. Either way `SG-V2` and `SG-V3` still govern |

| **SG2-V1** |**CLOSED — RC7 (H.31): THE OWNER CONFIRMS NO WELL WITHIN 15 m, so the IS 2470 offset set is COMPLETE for the first time. **`[C] owner ruling`, NOT a survey result — if a well is later found within 15 m, SK-01 moves**.** *Entry as it stood before the ruling, preserved under M.11:* **No well position exists anywhere in the project** *(SG2, 11 Sep 2026, H.23)* | **The IS 2470 (Pt 2) offset of ≥ 15 m from any well is the ONE of the three that SG2 cannot demonstrate.** The other two — ≥ 5 m to the septic tank and ≥ 2 m to any building — are now demonstrated at **5.40 m** and **10.97 m**. The only water feature recorded anywhere in the project is the RCC overhead reservoir on the deck's pipelines sketch, which is a **tank, not a well**, and is on the far side of the campus. **SG2 does not claim the offset is met** | **The position of every well within 15 m of the reserve, or confirmation that there is none.** A survey output, and the last thing standing between the foul soak pit and a complete offset set |
| **SG2-V2** | **CLOSED — RC8, 12 Sep 2026 (H.32): THE LAYOUT IS IMMUNE TO THE ANSWER.** Every offset in it is measured **relative to the structure**, never to a boundary, so a fence distance changes **where** the reserve sits and never **whether** it works. The concealment half of the question stays with `CAM-V2`. The row below is the position before the ruling | **Was:** | **It is the site's only recorded SWOT weakness** — *"Located near Perimeter Fence"* — and **no distance appears anywhere**. It bears on concealment (`CAM-V2`), on security, and on whether the external works reserve fits where SG2 puts it | **A dimension.** The layout is built to be immune to the answer: every offset in it is **relative**, so if the fence is closer than the reserve's east edge **the whole reserve translates and not one offset changes** |
| **SG2-V3** |**CLOSED — RC4 (H.28): SH-1 centred (−2400, 3100) — RECOVERED from the project’s own recorded 12.3 m, to within 28 mm.** *Entry as it stood before the ruling, preserved under M.11:* **SH-1, the fresh-air intake, has no plan position** *(SG2)* | The HVAC equipment schedule gives **SH-2** an X range (22 598 – 23 198) and gives **SH-1** only *"West of the box"*. **No X, no Y, no coordinate.** The fresh-air intake of a CBRN shelter is not a minor fitting: until it has one, **no intake separation can be checked against anything** — the septic vent, the generator exhaust, a surface plume. What protects it in SG2's layout is geometry, not a calculation: the reserve is **east**, SH-1 is **west**, so the separation is **at least 33 m however SH-1 is finally placed** | **A coordinate**, from HVAC. `SG2-F4` |
| **SG2-V4** | **SPLIT — RC8 (H.32). THE INTAKE/EXHAUST HALF IS CLOSED; THE PLUME HALF STAYS OPEN.** *Closed:* SG2 justified the orientation on access, fall, noise and end-to-end separation and **explicitly not on prevailing wind**, and RC4 then fixed SH-1 and SH-2 **25.30 m apart at opposite ends of a 22 m box** — robust whatever the wind does, which is why geometry was chosen over meteorology. ***Still open, and it must be:* a CBRN shelter with no wind direction data cannot state which way a release drifts, and the 25.30 m separation says NOTHING about that.** Closing both halves on one argument is the move this register exists to prevent | **Was:** | The P1 deck gives monthly mean **speed** and nothing else. It matters twice: for the **intake / exhaust** relationship, and as the **plume direction for the CBRN case** the whole shelter exists to survive. **SG2's orientation is therefore justified on access, fall, noise and end-to-end separation — explicitly NOT on prevailing wind** | **A wind rose** for the nearest long-record station. Until then the design's only protection is that intake and exhaust sit at opposite ends of a 22 m box |
| **SG2-V5** |**CLOSED — RC4 (H.28): THE RESIDUAL FLOTATION RISK IS ACCEPTED IN WRITING. No date moves. **A departure from B.3 mitigation 1, recorded as one** — 70 days at stage 3 across the 2027 monsoon, FoS 1.22 at the design GWT and 0.86 flooded.** *Entry as it stood before the ruling, preserved under M.11:* **The programme stops dewatering before backfill** *(SG2, sharpened by the `SG-V3` ruling)* | `A2070`, *"Dewatering — continuous through the substructure works"*, ends **11-05-27**. Side backfill `A7010` runs 20-07-27 → 30-07-27 and the burster slab is not cast until 21-08-27. Master `B.3` mitigation 1 requires dewatering **"until backfill and cover complete"**. **The gap spans the whole 2027 monsoon with the box at stage 3 — flotation FoS 1.22 at the design GWT and 0.86 flooded.** The `SG-V3` ruling makes this the operative control rather than a belt-and-braces note | **A project-owner decision on the programme.** No date is changed by SG2 — the owner's own Master Construction Schedule R0 governs (H.13). Either dewatering extends to 30-07-27, or the sub-structure sequence moves, or the residual flotation risk is accepted in writing |
| **DR-A1-V1** |**CLOSED — RC4 (H.28): THE EAST POSITION IS ADOPTED — one assumed position instead of two. **`U4` itself stays `[ASSUMED]`**.** *Entry as it stood before the ruling, preserved under M.11:* **RULED — RC4, 11 Sep 2026 (H.28): THE EAST POSITION IS ADOPTED.** One assumed position instead of two. **`RC4-F1`: the X range below is WRONG** — `A-301`'s own note 2 says **X 32000–36000** (4000 = the post's external dimension), not 31700–36300 (4600, matching nothing). **`RC4-F2`: the clash below DOES NOT HAPPEN** — it rested on an assumed Y, and with the post at **Y 600–5600** the reserve does not move and SG2's 28 checks stand. One NEW check failed — **SK-02 to the post at 1.80 m against IS 2470's 2.0 m** — fixed by moving **SK-02 300 mm north**. **`RC4-F3`: the EAST position gives 9.00 m to the EXCAVATION face against the ≥ 10 m rule as written**; both readings recorded, neither adopted. **`U4` STAYS `[ASSUMED]`.** The row below is preserved under M.11 | **Was:** `U4` records that **no sentry-post coordinate exists** — `A.2`/`A.4.8` and the four Rev F sentry sheets say only *"≥ 10 m clear of the shelter excavation"*. Two placements now satisfy that rule in different directions: **`A-301` draws the post at `X 31700 – 36300`, 10 m EAST**, and **BIM-P1 / `SG2` assume `X 9000 – 13000, Y 15250 – 20250`, 10 m NORTH**. `SG2`'s external works reserve is `X 33000 – 51000`, so **the elevation's placement would put the sentry post inside the reserve**, and `SG2`'s 28 of 28 clearance checks — run against the northern assumption, and giving `ST-01` **22.5 m** from the post — would have to be re-run. On the elevation's own placement the same gap measures about **0.25 m**. **Nothing is ruled: both stay `[ASSUMED]`, and `A-301` now says on its face that its sentry position is a convention, not a coordinate** | **The sentry post's real site position — `U4`.** Until it exists, `ST-01` and `SK-01` are drawn on `A-301` beyond a break rather than at true X, and no clearance between the sentry post and the external works can be stated |

| **RC4-V1** | **A SEALED SHELTER WITH A 4 kW HEAT SURPLUS AND NO ROUTE OUT FOR IT** *(RC4, 11 Sep 2026, H.28)*. **RULED AND NARROWED — RC5 (H.29): reject to the ventilation air in OPEN MODE ONLY, and add no new penetration.** | **The ruling's value is real — every penetration not made cannot fail.** But `RC5-F1`: **the ventilation air cannot reject this heat and was never sized to.** 300 m³/h is a *contaminant* rate (FEMA 0.25 cfm/ft²), about an order of magnitude short; it needs a **63.3 K** difference to reject 6.363 kW, and at a realistic 5 K removes **7.9 %**. **In Pune, whenever ambient exceeds the internal temperature, ventilating ADDS heat.** So the structure and the rock carry essentially the whole load in both modes, and the 96-hour answer stays **13.2 K of rise to about 39 °C, still climbing.** **The ruling is an ACCEPTANCE of that condition, not a solution to it** | **A transient soil–structure THERMAL model** — the sibling of the soil–structure *interaction* already deferred to Phase 3 — and **an ambient design temperature, which exists nowhere in this project** `[N]` |
| **DR-A2-V1** | **`SU-01` HAS NO COVER, AND BAY 5 CANNOT BE CROSSED WITHOUT ONE** *(DR-A2, 12 Sep 2026, H.35)*. The mat carries a **1500 × 1500 opening** over the clean sump — `F.1` trims it with 4-T20 each face each side, `BBS` line `F10` calls it an opening, `WM-V8` measures the mat gross by its 1.35 m³. **Nothing in this project says what closes it.** | **A cover is not optional.** Bay 5 is **1560** clear and the pit is **1500** of it, so with the opening open there is no route past it to the filter trains, the CO₂/O₂ plant or the dehumidifier; and `ROOM_FINISH_SCHEDULE` falls room `U-05` **1:80 direct to the sump**, so the cover has to pass water. **A-202 now draws a cover at (−)6.100 as `[A]` and says on its face that its specification is `[N]`.** Nothing was converted | **The cover itself:** type (open grating vs slotted vs solid with a gully), depth, **imposed load duty**, frame and rebate, fixing, and how it is lifted for withdrawal of `PU-01`/`PU-02` and use of the `PU-03` hand pump. **Until it exists the 1500 span is undesigned and the bay is not demonstrably passable.** `[N]` |

### K.1e RULED, CLOSED OR ANSWERED BY THE PROJECT OWNER — RC2 (H.21), SG2 (H.23) and RC4 (H.28)

> **RC4, 11 September 2026 (Part H.28) — EIGHT CLOSED BY OWNER RULING.**
>
> | Item | Ruling | What it cost |
> |---|---|---|
> | **U2** — is a direct hit a requirement? | **NO. The design stands as it is.** The 2.0 m cover is for prompt neutron and gamma attenuation, not to defeat a penetrating weapon, and the burster slab breaks up a penetrating item rather than stopping one | Nothing. The position was already consistent through every load case; it is now **ruled** rather than assumed |
> | **U3** — design basis threat yield | **HOLD p<sub>so</sub> 344.7 kPa (50 psi) and t<sub>d</sub> 0.13–1.33 s as THE stated basis.** The overpressure and duration ARE the design inputs | Nothing. **The yield stays unstated rather than invented** — the honest position, and the one every load case already uses |
> | **WM-V7** — ballistic function | **NOT REQUIRED. Brick stands.** | Nothing. The sentry post is already declared not blast designed and expendable |
> | **EM-V3** — is bay 8 inside the EMP boundary? | **INSIDE.** The generator, its panel and its cabling are protected | **BV-4/BV-5 now REQUIRE honeycomb WBC panels**, and **the project now holds two protective boundaries that do not coincide** — gas-tight bays 1–6, EMP bays 1–8 — **only one of which has ever been drawn.** RC2 lets the generator run in mode 3 with those two bores open, so the panels must work with the valves open |
> | **EL-V6** — cooling | **COMPUTE THE HEAT BALANCE.** Done: 6.363 kW sensible, 2.199 GJ over 96 h, air +13.2 K to ≈ 39 °C and still rising, duty **4 kW (1.14 TR)** to hold 30 °C | **Closed as computed — and it opens `RC4-V1`.** The duty is trivial; **the rejection path does not exist** |
> | **CAM-V5** — SH-2 head level | **+1.500**, the same gooseneck head as SH-1 `[A]` | A consistency argument, not a dispersion calculation. **C-101 can now draw SH-2 to scale** instead of flagging it `[N]` |
> | **SG2-V3** — SH-1 plan position | **CENTRED (−2400, 3100)**, 600 × 600 `[A]` | **RECOVERED, not chosen** — it reproduces the project's own recorded *"12.3 m from the intake to the entry"* to **28 mm**. 25.30 m from SH-2 |
> | **FS-1 / D-05** — W5 has no door | **DESIGN IT.** 900 × 2100 gas-tight fire door, **opening EAST into bay 6** in the direction of escape on R1; 2-T16 each jamb each face; 200 × 300 header band | **FS-1 CLOSES.** The **EI 120 rating is `[A]` and must stay `[A]`** — nothing in this project states a required fire rating for any element |
>
> **AND THREE THE OWNER DELIBERATELY LEFT OPEN:** `EM-V4` (no communications design),
> `EM-V5` (no pipe material anywhere) and `SG-V7` (the concealment turf may be expansive clay).
> **Two of the three were sharpened by other RC4 rulings** — the cooling ruling adds a second
> boundary crossing with EM-V5's problem, and the raft ruling produces a stockpile of exactly
> the material SG-V7 warns against. **They stay in K.1b, unchanged.**

### K.1e — earlier rulings: RC2 (Part H.21) and SG2 (Part H.23)

> **Every one of these was asked, not assumed.** Each package raised a question it could not
> answer from the project's own evidence, stated the consequence of each possible answer, and
> stopped. **Not one of the four rulings changed a number.**
>
> **RC2, 11 September 2026 (H.21)** — `EM-V1` and `EL-V1`, the two the EMP and electrical
> packages raised. **SG2, 11 September 2026 (H.23)** — `SG-V9`, closed by a datum the owner
> supplied, and `SG-V3`, ruled. **The SG2 rows are listed first because one of them unblocked
> a package.** Reasoning is preserved throughout; nothing is deleted.

| # | Question | Ruling | Effect |
|---|---|---|---|
| **SG-V9** | Where is the site? The project had **no coordinates** — the owner's map pin could not be resolved in the SG1 session (egress policy, 403) | **CLOSED, 11 Sep 2026 (H.23). 18.6089876 N, 73.8587287 E**, supplied directly, together with *"the area around 50 m is all available"* | **It unblocked the site layout.** With the coordinate, the envelope, SG1's contours and the project's confirmed geometry, master `H.9`'s *"not determinable"* positions became determinable. **The pin is taken as the centre of the box — an adopted convention `[A]`; if it meant a corner the whole layout translates rigidly and no offset changes** |
| **SG-V3** | The monsoon groundwater monitoring `A1080` runs 12-11-26 → 04-12-26, which is **not the monsoon**. Move it, at the cost of a critical-path activity? | **RULED, 11 Sep 2026 (H.23). NO — the cost is not accepted.** `A1080` stays where it is | **`A1080` will measure the recession, not the peak, so it will NOT close `K.2 A2`.** The design GWT `(−)2.000` stays `[ASSUMED]` through construction. **The permanent works are still bounded** — `B.3` gives the completed structure FoS **1.41 flooded to grade** against a requirement of 1.2. **What is exposed is the construction stage**, so `B.3`'s mandatory mitigation becomes the operative control — and **`SG2-V5`** records that the programme does not currently implement the first of it |
| **EM-V1** | Adopt or reject the three-zone EMP model and the *"EMP Zone 2 standing alone"* design rule | **ADOPTED.** EMP Zone 0 / 1 / 2, and the rule that Zone 2 delivers the full 80 dB with **no attenuation credited from the concrete box at any frequency**, are the project's EMP position `[C]` | **CLOSED.** Nothing else in EM1 changes — no figure, no finding, no other open item. Five EM-V items stand |
| **EL-V1** | May the generator run during Mode 3 CLOSED? HV1 stated both *"all five blast valves shut"* and *"BV-4 and BV-5 open … independent of modes 1–4"*, and BV-4/BV-5 are two of the five | **YES.** All five shut at the shock and hold 1.3 s; **BV-4 and BV-5 are then reopened for generator operation.** Bay 8 is outside the gas-tight envelope `[C]` | **CLOSED.** EL1's **Case A confirmed at 149 Ah** — the battery stands at the size already designed, only the class moves `[A]` → `[C]`. **HV1's Mode 3 row amended.** **EM-V3 is sharpened, not decided** |


### K.1c Works Management items — RULED by RC1

> The WM-V items came from WM1 and the R items from the WM2 reconciliation of the owner's
> own package. **Every one that could be decided on the evidence in the project has been
> decided.** WM-V6, WM-V7 and WM-V9 are in K.1b because they need something the project
> does not contain.

| # | Ruling | Basis |
|---|---|---|
| **WM-V1** ground-storey panel height | **CLOSED. 2.600 m governs** | 2.600 is confirmed **twice** and independently: Rev F drawing 6 states *"200 × 2600 high"*, and A.7.7's confirmed **13.000 kN/m = 0.200 × 2.600 × 25** reproduces it exactly. The 2.750 is only *inferred* from levels. A confirmed value beats a derived one. **The 150 mm difference is a setting-out item, not a design conflict**, and no quantity changes — WM1 already measured at 2.600 |
| **WM-V2** door / vision-panel overlap | **CLOSED. The union is deducted once** | Deducting both would remove 1.9 m² of masonry twice. Deducting the union once is the only measurement that is neither double-counted nor short |
| **WM-V3** opening heights not stated | **CLOSED for measurement. Doors 2100, windows and vision panels 1200** `[A]` | 2100 is the project's own convention for **every other door** in the project, so a door of a different height would be the anomaly. 1200 is WM1's measurement assumption and is retained. **Lintel L1 is unaffected either way** — it is designed to an arching bound that does not use a height at all, which is why the ruling is safe to make. **Confirm before the openings are set out** |
| **WM-V4** 190 in the 200 zone | **CLOSED. 190 modular brickwork confirmed** | It is the only option that preserves the **confirmed** 4000 × 5000 external envelope and flush column faces. 230 conventional brickwork would break a confirmed dimension. The residual 10 mm is taken up at the internal face in the plaster |
| **WM-V5** lintel design | **CLOSED by SP-B2** — lintel **L1**, master A.4.8 / H.12 | |
| **WM-V8** mat measured gross | **CLOSED as a declared conservatism** | +1.35 m³ for the 1.5 × 1.5 sump opening. SC1's convention, kept. It over-measures, which is the safe direction for a bill |
| **WM-V10** bulking not applied | **CLOSED as a declared conservatism** | The 1 114 m³ is a **bank** measure; loose volumes for haulage will be 40–60 % greater. Declared so no one plans haulage off the bank figure |
| **WM-V11** wall tie detail | **CLOSED by SP-B2** — 6 mm MS ties @ every 5th course, master A.4.8 / H.12 | |
| **WM-V12** W8 door head height | **CLOSED. 2100** `[A]` | Same basis as WM-V3: the project's own convention for every other door |
| **R-1** burster slab 300 M35 (owner) vs **200 M30** (A.7.3) | **RULED: 200 mm M30 governs** | A.7.3's cover column is `[CONFIRMED]` and totals exactly 2000; **a 300 mm slab does not fit it** without taking 100 mm from another layer, and every layer has a stated function. M30 is what A.7.3 specifies. COMB 103 is built on this column. **The owner's bill over-measures the burster slab by 37.02 m³ and its rebar by ≈ 1.67 t** — flagged for their estimate, not changed in their file |
| **R-2** cover 4 m (owner's programme) vs **2.0 m** | **RULED: 2.0 m governs** | A.7.3 records the **4.0 → 2.0 reduction as a deliberate design decision** with its reasons, and the owner's **own** BOQ says 2 m in two places. Only the programme *activity names* say 4 m, so this is stale wording in one document against agreement everywhere else |
| **R-3** roof slab 1000 (owner's programme) vs **900** | **RULED: 900 governs** | The master says 900, the owner's **own** BOQ says 900, and COMB 103's self weight **22.5 kPa = 0.900 × 25** confirms it arithmetically. Again only the programme activity names differ |
| **R-4** "Lift Shear Wall" in the programme | **RULED: a template carry-over. There is no lift** | Not in Rev F, not in the master, not on any drawing. It carries no quantity and no cost, so nothing is mispriced — **the activity names should be corrected to "Column & Staircase Shear Wall" before the programme is issued for construction** |
| **R-5** MS Project title "(21.6 x 6.8)" | **RULED: the title is stale. 22.0 × 6.2 governs** | 21.6 is the **pre-M1** box length; 6.8 matches nothing in the project at all. The owner's own BOQ says 22.0 × 6.2, as does A.4.2 post-M1. Title only — no quantity depends on it |
| **R-6** "Sentry Post RCC Frame & Infill" | **RULED: the line is the RC FRAME ONLY; the infill is brick and is measured as brickwork** | 18.60 m³ against WM1's frame-only 20.951 m³ is frame-sized, not frame-plus-infill; RC infill would add ≈ 7.9 m³ more. The owner's own programme carries brickwork activities (87–90), so the intent is already masonry |
| **R-7** escape shaft collars not measured | **RULED: they are a real item and are missing from the owner's bill** | ESC 1 and ESC 2, **250 RC, OD 1900, 6.285 m³** (WM1 `C-12`). The owner prices the hatches but not the shafts. To be added to their estimate |
| **R-8** no generator priced | **RULED: a genuine omission from the owner's bill** | The master puts a **15 kVA** set in Bay 8 and HV1 sizes 2 600 m³/h of combustion and cooling air through BV-4/BV-5 — which the owner **does** price, so the air path is there and the machine is not. The set, its fuel system, exhaust and acoustic treatment are to be added |
| **R-9** filter duty | **RULED: 300 m³/h — see U13. The owner's estimate agrees** | Now consistent everywhere |
| **R-10** 224 vs 326 working days | **NOT A CONFLICT — different scopes** | The owner's R0 is a 130-activity construction schedule; WM1's 279 activities also carry approvals, procurement, long-lead manufacture, commissioning and 16 quality hold points. **The owner's R0 is the programme of record**; WM1's logic stays as the cross-check on what R0 does not name |
| **R-11** monsoon: 3 days a month vs a productivity allowance | **NOT A CONFLICT — two conventions. The owner's governs** | Both are defensible ways to carry the same lost time |
| **R-12** steel 67.79 t vs 77.33 t | **RULED: follows R-1** | The gap tracks the burster slab difference plus the bar-by-bar derivation in `BOQ_QUANTITY_DERIVATION.txt`. With the burster slab at 200 M30 the owner's figure needs its burster line reduced by ≈ 1.67 t |
| **R-13** concrete total out by 10.00 m³ | **RULED: the eleven line items are right. The stated total should be 480.50 m³, not 470.50** | The lines are the primary data and each is separately priced, so **no cost is affected**. The owner's report reaches 470.50 only because its grouped "Sentry Post & Sump" row reads 19.80 where the workbook's equivalent lines come to 29.80 — the same 10.00 m³ |
| **R-14** final cost out by ₹1,00,000 | **RULED: the seven cost heads are right. The total should be ₹2,99,33,306, not ₹3,00,33,306** | Everything else reconciles **to the rupee**: the five part subtotals make the basic cost exactly, and every percentage addition is exact on it. Only the final line is out, by a round lakh — the signature of a formula picking up the wrong cell |

> **R-1 to R-14 are rulings about the PROJECT, not edits to the owner's files.** Nothing in
> `WORKS MANAGEMENT/USER_SOURCE/` has been touched, and the published `Cost/` and
> `Programme/` documents still carry the owner's figures exactly as supplied. The rulings
> say which value the **project** uses and what the owner should correct in their own
> documents.

### K.1d Historical record — the register as it stood before RC1

> **PRESERVED UNDER RULE M.11, SUPERSEDED BY RC1.** Everything below is the dated record
> of how these items were carried, in the words used at the time. **Where it says an item
> is open, unresolved, or awaiting a ruling, read K.1 and K.1b above instead** — RC1
> (10 September 2026, Part H.14) ruled on all of them. Three statements below are now
> specifically out of date and are corrected here rather than edited out of the history:
> **"U1 remains open"** — U1 is closed, 73.18 kN governs;
> **"C21 must be ruled on BEFORE the CBRN filter trains are ordered"** — C21 **has** been
> ruled: **300 m³/h**, and A.3 is corrected, so the enquiry can proceed;
> **"no item above has been closed"** in the WM1 and WM2 updates — true when written,
> not true now.

> **Update, 3 September 2026 — the `.std` files are now in the workspace. No tag above has been changed.**
> **U4** and **U5** are answerable from them directly: both models end with `PERFORM ANALYSIS PRINT STATICS CHECK` and no P-Delta; the underground model has **1 138 shell elements** in four thickness groups (mat 600 / roof 900 / perimeter 600 / internal 200–400) on `ELASTIC MAT DIRECT Y SUBGRADE 100000`. Note that its closing `START CONCRETE DESIGN … DESIGN ELEMENT 509 TO 688 869 TO 922` block contradicts its own `NO DESIGN` header comment; it has been left in place.
> **U6** — the sentry model has **twelve joints. There is no node 213.**
> **U7** — beam `16 211 212` is present, exactly as reconstructed.
> **U1** — the sentry model does now print the seismic-weight summary the item asks for: roof 331.46 + floor 400.34 = **W 731.80 kN**, V<sub>b</sub> = 0.100 × 731.80 = 73.18 kN, so V<sub>b</sub>/W returns A<sub>h</sub> = 0.1000 exactly. **[DERIVED, requires the user's confirmation before U1 is closed]** rebuilding both storey weights from the model's own load blocks reproduces 331.46 and 400.34 exactly, and the 139.1 kN gap to the B.8 hand check resolves as (i) 107.9 kN — half the first-storey infill, which the B.8 floor line does not allocate — plus (ii) 31.1 kN, the model taking the full 450 beam depth in `SELFWEIGHT` while also applying the full slab pressure, where B.8 nets the beam to 300. **U1 remains open. U2, U3 and U8 are untouched.**

> **Update, 7 September 2026 — Works Management package WM1 (H.10). No tag above has been
> changed and no item above has been closed.** WM1 carries all ten of C16–C21, U1, U2, U3
> and U8 forward into its own verification register untouched. It adds twelve items of its
> own, **WM-V1 to WM-V12**, all open, of which four arise directly from the instructed
> design change **SP-B1** (sentry post walls = brick masonry):
> **WM-V5** no lintel design exists for the nine sentry-post openings — a requirement the
> brick masonry creates and the RC panels did not have;
> **WM-V6** the sentry post seismic weight changes when 200 RC infill (13.000 kN/m,
> confirmed in A.7.8/A.7.7) becomes 190 brickwork (≈ 9.9 kN/m), which makes the existing
> **V<sub>b</sub> = 73.18 kN conservative — a direction, not a verification**, referred to the
> structural discipline and **not resolved**;
> **WM-V7** brick masonry does not provide the ballistic protection that the Rev F "200 RC
> BALLISTIC INFILL" panels were named for, so the instructed change removes a stated
> protective function from a structure already declared not blast designed;
> **WM-V11** no wall tie detail exists between the masonry and the columns.
> The remaining eight concern measurement: the ground-storey panel height (**WM-V1**, the
> project's confirmed 2.600 against the 2.750 the levels imply — 2.600 used), the
> door/vision-panel overlap on the Rev F first-floor plan (**WM-V2**), unstated opening
> heights (**WM-V3**), the 190-in-200 brickwork thickness (**WM-V4**), the gross mat measure
> (**WM-V8**), excavation working space and face treatment (**WM-V9**), bulking on rock
> (**WM-V10**) and the W8 door head height (**WM-V12**). Full text in
> `WORKS MANAGEMENT/Documentation/WM_ASSUMPTIONS_AND_VERIFICATION_REGISTER.md`.
> **C21 must be ruled on BEFORE the CBRN filter trains are ordered** — the WM1 programme
> places the enquiry activity ahead of the order for that reason.

> **Update, 10 September 2026 — revisions BS1 and SP-B2 (H.12). Two WM-V items are
> closed; nothing else above is changed, downgraded or removed.**
> **WM-V5 (no lintel design exists) is CLOSED** — lintel **L1** is designed in A.4.8 to
> IS 456 Cl. 22.2 / 26.5.1.1 / 26.5.1.6 and Table 19, tagged `[R]`.
> **WM-V11 (no wall tie detail exists) is CLOSED** — the tie detail is in A.4.8, tagged `[R]`.
> **WM-V6 and WM-V7 REMAIN OPEN and are not touched**: WM-V6 is a seismic re-check for the
> structural discipline, and WM-V7 — the ballistic function the Rev F panels were named
> for — is a client / military decision that cannot be closed by drafting or by design.
> **WM-V3 (opening heights not stated) REMAINS OPEN and is deliberately not used**: L1 is
> designed to an arching bound that does not depend on the height, so it neither needs nor
> confirms WM1's assumed 1200.
> **C16–C21, U1, U2, U3, U8 and the remaining WM-V items are untouched.** **C17 in
> particular is NOT resolved by BS1** — the A.7.3 column still sums to 39.15 against the
> stated 40.65, at the crown exactly as before.

> **Update, 10 September 2026 — Works Management revision WM2 (H.13). NOTHING above is
> closed, downgraded or removed. Fourteen NEW open items are added.**
> The project owner supplied their own BOQ, cost estimate and master construction
> schedule R0, which now govern Works Management. Reconciling them against this master
> raised **R-1 to R-14**, all open, full text in
> `WORKS MANAGEMENT/Documentation/WM_RECONCILIATION_REGISTER.md`. The two that bear on
> the engineering are:
> **R-1** — the owner's burster slab is **300 mm M35, 57.60 m³**, against A.7.3's
> **200 mm M30**: 37.0 m³ and one grade apart, and 300 mm does not fit the confirmed
> 2000 mm cover column without changing another layer;
> **R-2** — the owner's programme carries a **4 m** soil overburden (activities 51 and
> 52) while their own BOQ report and A.7.3 both say **2.0 m**; A.7.3 records the
> 4.0 → 2.0 reduction as a deliberate decision, so the programme appears to carry the
> superseded scheme.
> **C21 IS NOT CLOSED BY R-9.** The owner's estimate independently prices
> **2 × 300 m³/h** filter trains, which is evidence on the 300 side and nothing more.
> **C21 must still be ruled on BEFORE the filter trains are ordered.**
> **R-13 and R-14 are arithmetic slips inside the owner's own files** — a concrete total
> 10.00 m³ below the sum of its own lines, and a final cost ₹1,00,000 above the sum of
> its own cost heads. Both are **reported, not corrected.**

### K.1f DECLARED SCOPE BOUNDARIES — true, visible, and NOT gaps

> **Added by RC8, 12 September 2026 (Part H.32).** These are stages the project deliberately did
> not undertake and said so at the time. They are recorded here rather than in `K.1b` so that a
> declared decision is never counted as an outstanding problem — which is what was happening.

| Ref | What does not exist | Where it was declared |
|---|---|---|
| **EL-V5** | **No circuit, cable, luminaire or socket schedules.** The electrical package stops at **board level** — sources, a load schedule, three boards, the essential/battery system and one single-line diagram | EL1's own opening paragraph: *"A BASIC PACKAGE, ON PURPOSE. It stops at board level."* (H.20). **It closes when a detailed electrical design is commissioned, not by any work in this project** |

## K.2 ASSUMED — must be confirmed before construction

> **SEVEN OF THE FOURTEEN ARE CLOSED — RC5 and RC6, 12 September 2026 (Parts H.29, H.30).**
> **`A13`** closed on the evidence (the `.std` was in the workspace all along); **`A6` `A9` `A10`
> `A11` `A12` `A14`** closed by owner ruling, each either the conservative choice or a
> simplification the margin swallows. **The rows below are preserved unaltered under M.11** and
> each closed one is marked in its last column.
>
> **AND THE SEVEN THAT REMAIN ARE EXACTLY THE SITE INVESTIGATION.** `A1` boreholes · `A2` a
> piezometer read through a **full** monsoon · `A3` plate load / core testing · `A4` a plate load
> test at **both** bounds · `A5` site investigation · `A7` **the mandatory percolation test** ·
> `A8` packer permeability tests. **Nothing left in this register can be settled by anyone in a
> room.** `SG-V1` and `SG-V2` say why: the only investigation available is **off-site** and
> **reached about 1.5 m against a formation at (−)6.800.**

| # | Assumption | Impact if wrong | Verify by |
|---|---|---|---|
| A1 | Rockhead 1.5–2.0 m, competent below | Founding level, excavation cost | Site investigation |
| A2 | **GWT (−)2.000** | **Uplift, flotation, waterproofing class, wall design** | **Monsoon-season monitoring** |
| A3 | SBC 3240 kPa | Footing and mat sizing (both ≪ 13 % utilised) | Plate load / core testing |
| A4 | **k<sub>s</sub> 100 000–500 000 kN/m³** | **Mat moments — sensitive. Run both bounds** | Plate load test. **RC4 (H.28): the UPPER-BOUND MODEL NOW EXISTS** — `Underground_Shelter_ks500000.std`, identical to the reference model but for the subgrade line and the four corner `KFY`. **STILL `[ASSUMED]` AT BOTH BOUNDS, AND NEITHER HAS BEEN RUN** |
| A5 | K₀ = 0.50, γ 20/21 | Wall lateral load | Site investigation |
| A6 | K<sub>a</sub> = 1.0 saturated (used); K<sub>a</sub> ≈ 0.5 dry berm (**not relied on**) | Headhouse wall load — removed from the critical path by C10 | ~~Would allow a reduction if measured~~ — **CLOSED, RC6 (H.30). ACCEPTED AS THE CONSERVATIVE CHOICE:** the full 383 kPa is taken rather than crediting unverifiable berm attenuation |
| A7 | Soak-pit absorption 20 L/m²/day | **Soak pit will not work if lower — likely on basalt** | **Percolation test, IS 2470 Pt 2 Cl. 4 — MANDATORY** |
| A8 | Structural seepage 0.5 L/m²/day | Sump storage (currently 8.4 days) | Packer permeability tests |
| A9 | Sentry infill NOT separated → R = 3.0 | V<sub>b</sub> × 1.67 if separated | ~~Architect's decision~~ — **CLOSED, RC6 (H.30). R = 3.0 KEPT.** It is the conservative position: R = 5.0 gives A<sub>h</sub> 0.060 against 0.100, so 73.18 kN is ≈ 1.67 × a separated SMRF's demand. Separating would need an SMRF this project does not claim, and would undo SP-B2 |
| A10 | k1 = 1.08 (100-yr wind life) | Wind (does not govern) | ~~Client brief~~ — **CLOSED, RC6 (H.30). ACCEPTED:** a 100-year life on a load path seismic beats **2.4 : 1** |
| A11 | b<sub>eff</sub> = 2.5 m for the HW3 line load | HW3 strip check (26 % / 41 %) | ~~Refined FE if ever critical~~ — **CLOSED, RC6 (H.30). ACCEPTED ON THE MARGIN:** 41 % on the conservative one-way bound leaves more than half the capacity spare, so b<sub>eff</sub> would have to be badly wrong to matter |
| A12 | Trapezoid factor 0.7946 used for both BM and FEM | ~2 % on B2 support moment | ~~Frame model~~ — **CLOSED, RC6 (H.30). ACCEPTED ON THE MARGIN.** The factor itself is exact — 1 − 1/(3r²) at r = 1.2740 = 0.79463; using it for both BM and FEM is the simplification, and 2 % sits inside B2's 89 % |
| A13 | Sentry post STAAD has no member releases | Frame moment distribution | ~~Upload the `.std` file~~ — **DONE. `A13` IS CLOSED ON THE EVIDENCE, 12 Sep 2026 (RC5, Part H.29). The file is in the workspace and has been read: there is NO `MEMBER RELEASE` command anywhere in it.** See below |
| A14 | Poisson's ratio 0.20 | Plate behaviour, minor | ~~Standard~~ — **CLOSED, RC6 (H.30). ACCEPTED** as the standard value for concrete |

> **`A13` CLOSED ON THE EVIDENCE — 12 September 2026 (RC5, Part H.29). THE FIRST OF THE
> FOURTEEN TO CLOSE, AND IT NEEDED NO RULING.** K.2 asked for the `.std` file; the file has been
> in the workspace since H.4 and the register was never revisited. Reading it settles the row:
>
> | Read from `current/staad/Sentry_Post_Framed_Seismic.std` | |
> |---|---|
> | **`MEMBER RELEASE`** | **Absent. The command appears nowhere in the file.** Every beam–column joint is fully continuous — which is what a moment frame requires, and what the portal-method member forces in B.8.1 assume |
> | Supports | `1 2 11 12 FIXED` — **all four column bases fully fixed** |
> | Members | 1–8 columns `PRIS YD 0.35 ZD 0.35`; 9–16 beams `PRIS YD 0.45 ZD 0.25` — matching A.4.8 |
> | Infill | modelled as **`MEMBER LOAD` only**, never as a strut |
>
> **The assumption was right and is now CONFIRMED.** `[C] read from the .std`
>
> **One observation that follows, and it is not a defect.** The infill is carried as **load, not
> stiffness**. The frame is analysed bare, which is conservative for the frame's own moments and
> is normal practice at **R = 3.0** — and A.7.8 already takes the *with-infill* period formula
> (IS 1893 Cl. 7.6.2(c)), so the infill is credited where it shortens the period and not
> credited where it would attract force. **What a bare-frame model does not capture is the
> local effect of infill on individual columns.** Nothing in this project claims it does.

> **SG1 — 11 September 2026 (Part H.22). NOT ONE OF THE FOURTEEN IS CLOSED.** Four are
> touched by the evidence the SEMT/67/15 sub-soil investigation and the P1 deck supply.
> What each gains is a **provenance and a quantified margin**, never a confirmation —
> master rule `M.6` forbids that, and the governing reason is `SG-F2`: **the investigation
> reached about 1.5 m and this structure founds at (−)6.800.**
>
> | # | Provenance now on record | Margin now quantified | Still needs |
> |---|---|---|---|
> | **A1** | rockhead **0.9–1.5 m** at three locations `[C]` | the report's band is **entirely at or above** the assumed 1.5–2.0; **+118 m³ rock, ≈ 2 d** | boreholes **on this plot** — `A1075`, and **`SG-V1`, `SG-V2`** |
> | **A2** | *"not encountered in any trial pit"* — **in pits ~1.5 m deep**; the P1 deck's *"safe for water table at depth of 2 m below GL"* `[C]` | **none.** *Not encountered* = **not reached**; the design GWT is already below the deepest pit | a **standpipe piezometer read through a full monsoon**. `A1080`'s window, **12 Nov – 4 Dec, is not in the monsoon** — **`SG-V3`** |
> | **A3** | measured basalt **1961–2059 kPa soaked** / 2942–3530 unsoaked `[C]` | soaked governs; worst utilisation **12.5 % → 20.6 %**, factor **4.8** in hand | plate load / core testing at the founding horizon — **`SG-V2`** |
> | **A4** | **nothing** | — | plate load test. **The 500 000 bound is still outstanding** |
> | **A5** | φ **27–35°**, c ≈ 0, MDD **1.88–1.93**, OMC **8–12 %** `[C]` | K₀ 0.50 **conservative** on the murrum; γ<sub>sat</sub> agrees within **1.2 %**; wall load moves **< 1 %** | nothing further — the walls are blast-governed |
> | **A7** | **nothing** | — | **percolation test, IS 2470 (Pt 2) Cl. 4 — still MANDATORY**, and the report's basalt makes failure likely |
> | **A8** | **nothing** | — | packer permeability tests at the flow contacts |
> | **A10** | the deck's monthly **mean** wind speeds `[C]` | **not the same statistic.** V<sub>b</sub> = 39 m/s is a 3-second gust at a 50-year return period | nothing. **A.7.8 IS NOT TO BE REDUCED ON THE STRENGTH OF THE DECK'S WIND SLIDE** |
>
> **Externally corroborated for the first time, and unchanged:** **Seismic Zone III** — both
> documents say it, and A.7.8's A<sub>h</sub> = 0.075 / 0.100 reproduce exactly from Z = 0.16
> (`SG-F12`); and the **40.65 kPa cover**, which brackets both the as-placed (lighter) and the
> fully saturated (+1 %, = **+0.09 % of COMB 103**) case (`SG-F8`).

## K.3 CONFIRMED but requiring attention

| # | Item |
|---|---|
| **F1** | Protective boundary was not continuous — **resolved by M1 — APPROVED AND IMPLEMENTED 3 Sep 2026, see H.4** |
| **F2** | Stair-void cantilever M(root) 758.6 > midspan 700.2 — **resolved, links added** |
| **ERR-1** | My own yield-line coefficient error, 324.4 → 162.2 — **corrected; no reinforcement change** |
| Flotation | FoS 0.33 at the mat-only stage — **a design output, mitigation is mandatory and on S-02** |
| **Deccan basalt resistivity** 10³–10⁴ Ω·m | **Test earth resistance early** — affects EMP and lightning protection |
| Airlock purge 13 min | **4–5 persons/hour — a manning constraint, must be on the drill card** |
| **Black cotton soil, CH, free swell index 60–65 %** *(SG1, H.22)* | **CONFIRMED by measurement — SEMT/67/15 Appendix A — and recorded nowhere in this project before SG1.** An FSI above 50 % is the **top band of the IS 1498 scale**. Nothing structural founds in it: the mat is at (−)6.700 and footing F1 at (−)2.000, both in basalt, and **`B.8.7`'s insistence that F1 bears *"on IN-SITU ROCK, never on backfill"* is now backed by a measurement.** **Two elements are exposed anyway:** the covered entry stairwell's **stepped raft**, whose top founds at about (−)0.300 with no strip-and-replace specification anywhere (`SG-F13` / `SG-V6`), and the **300 turf concealment layer**, which `CAM2` re-lays from the site's own stockpile over the granular filter it would clog (`SG-F14` / `SG-V7`). **Neither is changed by SG1; both need a specification, not a calculation.** |
| **The founding horizon is permanently submerged** *(SG1, H.22)* | The formation at (−)6.800 is **4.8 m below the design GWT**, so the measured **soaked** basalt bearing value (1961–2059 kPa) is the applicable one, not the unsoaked (2942–3530). **The presumptive 3240 kPa in `A.6` is an IS 1904 value, is declared as one, and is not changed** — the worst bearing utilisation in the project rises **12.5 % → 20.6 %** and everything passes with a factor of **4.8** in hand. **Say it before a reviewer does** (`SG-F3`). |
| EMP rebar cage 0 dB @ 1 GHz | **Say it before a reviewer does.** Zone 2 welded steel room is the answer. — **EM1, 10 Sep 2026 (H.19): this figure has now been REPRODUCED from the 150 mm bar spacing alone (0.000 dB at 1 GHz, mesh cutoff 999.31 MHz), and the Zone 2 room it calls for is designed at `[A]`.** The item stands: the cage meets 80 dB only below **99.93 kHz**, one decade of the five |

---

# PART L — FINAL AUTHORITATIVE DESIGN REGISTER
### Quick reference for the next session

```
REVISION            Architectural Rev F  ·  Report Rev D  ·  Structural Phase 2 Rev A + M1

BOX                 22 000 × 6 200 external  ·  20 800 × 5 000 internal
                    walls 600  ·  roof 900  ·  mat 600  ·  PCC 100  ·  clear height 3 200
                    cover 2 000 layered = 40.65 kPa
LEVELS              grade 0.000 · T/slab (−)2.000 · soffit (−)2.900 · floor (−)6.100
                    u/s mat (−)6.700 · formation (−)6.800 · GWT (−)2.000
INTERNAL WALLS      W5 200 @ 12600–12800  ·  W6 400 @ 14800–15200  ·  W7 400 @ 18000–18400
SHAFT / VOID / PAD  15200–18000 × 600–5600 / × 600–3760 / × 3760–5600
ESCAPE SHAFTS       ESC 1 (2050, 2050)  ·  ESC 2 (19900, 2050)  ·  1400 dia, 250 collar
HEADHOUSE           14000–18000 × 600–5600 internal · walls 400 · roof 500 · top +0.900
ENTRY STAIRWELL     9500–15800 × 6000–7500 internal · 12R @ 166.667/300 · waist 250
SENTRY POST         4000 × 5000 · grid 3650 × 4650 · C1 350² · B1/B2 250 × 450 · S1 150
                    F1 1500² × 600 · levels +0.450 / +3.650 / +6.700 / +7.000
                    SITE POSITION X 32000–36000, Y 600–5600 [A] — RC4, EAST ruling
                    (9.00 m to the excavation face against the ≥10 m rule — RC4-F3)
AIR SHAFTS          SH-1 intake centred (−2400, 3100), head +1.500 [A] — RC4
                    SH-2 generator X 22598–23198, head +1.500 [A] — RC4

MATERIALS           Box M35 / Fe500D  ·  Sentry M30 / Fe500
                    Ec 29 580 / 27 386 N/mm²  ·  cover 75/50/40 (box), 30/40 (sentry)
                    Ld 40φ (M35) / 46φ (M30)  ·  lap 50φ staggered
SOIL                Basalt · SBC 3240 kPa [A] · K0 0.50 · γ 20/21 · GWT (−)2.000 [A]
                    ks 100 000–500 000 kN/m³ [A] — RUN BOTH BOUNDS

BLAST               p_so 344.7 kPa (50 psi) · td 0.13–1.33 s · μ 5 · DLF 1.111
                    DESIGN 383 kPa on roof AND walls (Ka 1.0)
                    fck,dyn 43.75 · fy,dyn 625 · NO dynamic increase on shear
                    T 13.4 ms · td/T = 10–100 → QUASI-STATIC
ROOF TOTAL          448.15 kPa (383 + 40.65 + 2.0 + 22.5), no live load (Cl. 11.2)
HEADHOUSE ROOF      396.5 kPa   ·   HEADHOUSE WALLS 383 kPa either face (C10)
SEISMIC             Box Ah 0.075, Vb 1050 kN (negligible)
                    Sentry Ah 0.100, R 3.0, **Vb 73.18 kN (STAAD)** vs wind 29.9 kN
COMBINATIONS        Box 101/102/**103 BLAST**/104/105  ·  Sentry 101–113, 201, 202, 203

REINFORCEMENT — THE SIX THAT MATTER
   ROOF        T25 @ 150 EF EW  ·  T12 4L @ 250 end 1500 / 2L @ 300 mid   51 %
   WALLS       T16 @ 150 EF EW  ·  T12 closed @ 200                       68 %
   W6/W7       T20 @ 150 EF EW  ·  T12 4L @ 200                           69 %
   MAT         T16 @ 150 EF EW  ·  T12 @ 250 × 250 grid                   84 %
   HH ROOF     T20 @ 150 EF EW  ·  T12 4L @ 175 / 250                     90 %
   HH WALLS    T16 @ 150 EF EW  ·  T12 4L @ 250                           59 %

SENTRY      S1 T8 @ 150 B/W + T8 @ 300 edge top + T8 @ 200 torsion 700² × 4 corners
            B1 4-T16 / 2-T16   ·   B2 3-T20 / 2-T20   ·   T8 @ 100 hinge / @ 150
            C1 8-T16 · T10 hoops + cross-ties @ 85 over 500 · biaxial 0.819
            F1 T12 @ 150 B/W

STATUS      STAAD    7 .std in current/staad/ — box (reference), sentry, entry
                     stairwell, MS1 coarse/medium/fine, + ks 500 000 upper bound.
                     ALL READ AND RECONCILED
                     IN THIS WORKSPACE.  **STAAD.Pro NOT RUN — no result exists**
            DXF      80 DXF, 74 PASS (QA2, H.25).  S-06 is the only S-series sheet
                     present; S-01…S-05, S-07, S-08 are ABSENT and cannot be
                     regenerated — the Part E.4 toolchain is not in the workspace
            CALCS    Complete to IS 456; SDOF support rotation NOT done (Phase 3)
            DRAWINGS Sentry beams/columns/footings NOT yet drawn (would be S-09)
```

---

# PART M — INSTRUCTIONS FOR CONTINUING THIS PROJECT IN A NEW CLAUDE SESSION

**1. Read this entire MASTER PROJECT STATE before touching anything.** Do not skim to the section that looks relevant. The conflicts and the dependency map matter more than any single value.

**2. Treat PART A (Current Authoritative Project State), PART B (Structural Design) and PART L (Final Register) as the primary source of truth.** Everything else supports them.

**3. Treat superseded revisions as historical only.** Part H tells you what was superseded and why. **Superseded 3 Sep 2026: the input DXFs are no longer pre-M1.** The six affected drawings and the underground `.std` were brought to the M1 geometry on that date (H.4), so a dimension east of X = 14 800 may now be read from them. The seven missing output sheets S-01–S-05, S-07 and S-08 remain unregenerated.

**4. When project files are uploaded, compare them against this document before using them.** Parse them; do not assume.

**5. If a file conflicts with this document, STOP and identify the conflict.** Present both values, say which this document holds, and ask. Do not silently adopt either.

**6. Never guess missing engineering information.** If something is marked **[NOT AVAILABLE]** or **[UNRESOLVED]**, it stays that way until the user supplies it. The correct response is to ask, not to fill the gap.

**7. Preserve the existing design unless a change is explicitly requested.** This design is the product of ten resolved conflicts, two structural findings and one corrected arithmetic error. Do not "improve" it casually.

**8. When changing one parameter, work the dependency map in Part J** and list every downstream item that must be updated. State that list before making the change.

**9. Maintain consistency across geometry, calculations, STAAD, DXF, reinforcement and drawings.** The rule this project has held throughout: **no drawing shows an arrangement that differs from a calculation.** If you change steel, change the drawing in the same turn.

**10. Give every significant change a revision identifier** (M2, M3…; C11, C12…; ERR-2…) and add it to the tables in Part H.

**11. Never overwrite a previous revision without preserving it.** Add rows to Part H; do not edit them away.

**12. To regenerate a drawing, edit the Python generator and re-run it — do not edit the DXF.** See Part E.4. `proj.py` holds every geometric constant; changing a dimension there propagates to all eight sheets. Always re-run `validate.py` and `render.py` afterwards and **look at the render** before delivering.

**13. When generating any new STAAD content, keep it consistent with Part A geometry and Part D conventions** — remembering the underground model's **6.700 m Y-offset** and its **mid-surface** geometry.

**14. Before finalising any revision, cross-check in this order:** geometry → materials → loads → structural model → analysis → design calculations → reinforcement → drawings → revision number. A change that stops at "reinforcement" and never reaches "drawings" is not finished.

**15. Label everything you produce** as newly calculated, reconstructed, assumed or unresolved, using the same tags as this document.

**16. Do not claim a design is verified merely because an earlier version existed.** Recompute. The C2 headhouse roof — a calculation carried forward for two revisions while the geometry changed underneath it — is exactly why.

**17. Preserve the design intent.** In particular:
- The **protective boundary is Blast Doors 1 and 2 at (−)6.100**. Everything above them is expendable, and that is deliberate.
- **The roof spans one-way across the 5 000 mm width.** Lengthening the box is free; widening it is expensive. This single fact underpins Modification M1.
- **No movement joints anywhere inside the protective envelope.** A movement joint is a guaranteed blast, gas and EMP discontinuity.
- **IS 4991 Cl. 10.3.1.1 — no dynamic increase on shear.** This is the most commonly mis-applied rule in blast design and it is why several elements have links they would not otherwise need.
- **Say the weakness before the reviewer finds it.** That principle produced F1, F2, C9, C10 and ERR-1, and it is the reason this package is defensible.

**18. Two things that must never be claimed:**
- that a static STAAD run proves blast resistance (it gives the *demand* — the support-rotation check is Phase 3); and
- that flotation is satisfied because the model shows no uplift (the springs take tension — it is a hand check).

---

*END OF MASTER PROJECT STATE FILE. Compiled 2 September 2026 from the complete Phase 1 and Phase 2 record. Every value is tagged CONFIRMED, RECONSTRUCTED, ASSUMED, UNRESOLVED or NOT AVAILABLE. Nothing in this document was invented.*
