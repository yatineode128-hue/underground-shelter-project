# MASTER PROJECT STATE FILE
## Underground CBRN-Hardened Blast-Resistant Protective Structure + Sentry Post — Pune, Maharashtra
### Portable memory · Source of truth · Revision record · Reconstruction specification

**Document status:** MASTER STATE, issue 1
**Compiled:** 2 September 2026
**Compiled from:** Phase 1 Design Report Rev D (126 KB, 2000 lines), ten Rev F architectural DXF files, nineteen STAAD.Pro screen captures, and the full Phase 2 structural design work.
**Covers:** Phase 1 (architectural + basis of design, complete) and Phase 2 (structural design + drawings, substantially complete).
**Next phase:** Phase 3 — non-linear SDOF verification, site investigation close-out, sentry post drawing S-07 equivalent.

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
| 5 | 11040 – 12600 | 1560 | CBRN plant: 2 × 250 m³/h filters, CO₂/O₂, dehumidifier, **sump** |
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
Roof 250 RC raking, soffit 2200 above the flight; over the platform it becomes the 500 headhouse roof
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
```

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
| **TOTAL** | **2000** | | **40.65** | |

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
| Roof projection + parapet | 4.162 kN/m | [C] as drawn, not independently derived |
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

**Sentry post (15 combinations, matching the STAAD model) — [CONFIRMED from screenshots]**

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
            Uplift acts on the REAL 133.92 m² underside, not the plate mid-surface area.
            At the M1 geometry (22000) both uplift and resistance scale with length,
            so EVERY FoS IS UNCHANGED.

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

| Model | File name shown in the title bar | Status |
|---|---|---|
| Underground box | `Underground_Structure_WITH_LOADS_worked_example (4)` | [CONFIRMED] |
| Sentry post | `Sentry_Post_Framed_Seismic` | [CONFIRMED] |

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

> **The output DXFs were not hand-drafted. They are produced by a dependency-free Python toolchain built inside this project. `ezdxf` is NOT available in the environment and the network is disabled — the writer is hand-rolled.**

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
| **IS 12070** | Rock foundations | Cl. 6 (settlement on sound rock) |
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
| **C16** | Roof / platform junction — A.4.7 reads *"over the platform it becomes the 500 headhouse roof"*, while B.6 designs, A.7.6 loads and F.2 registers a **250** stairwell roof, and the headhouse footprint (Y 200–6000) does not overlap the platform (Y 6000–7500) | `Entry_Stairwell.std` | A.4.7 **vs** B.6 / A.7.6 / F.2 | **MODEL RESOLVED AT 250 on the authority of M.2 (Parts A, B, L primary). The A.4.7 clause is left exactly as written and the conflict is NOT closed — see below** |

> **C16 — what was decided and what was not.** The model keeps a 250 roof because Part B designs one, A.7.6 loads one and F.2 registers one, and because the headhouse roof of B.7.1 is a 396.5 kPa blast element on a footprint that does not extend over the platform. **The clause in A.4.7 has not been edited.** This is a genuine textual conflict inside this document and needs the user's ruling before the junction detail is drawn.

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
pre-study copy (`git diff` clean). The main staircase is not represented in this plate model
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

---

# PART I — PROJECT FILE MANIFEST

## I.1 CURRENT FILES — input (user-supplied)

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
| `Phase1_Design_Report_RevD.md` | Markdown, 126 KB | **D** | **Primary source for loads, materials, geotech** | **CURRENT for loads/materials; SUPERSEDED for the entrance (C1) and headhouse roof (C2)** |
| `SK02_Underground_Plan.png` | PNG | — | Coloured GA plan, presentation graphic | CURRENT |
| 19 STAAD screen captures | PNG | — | **The only evidence of the STAAD models** | CURRENT |

## I.2 CURRENT FILES — output (generated in this project)

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
                 │
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

## K.1 UNRESOLVED — do not guess

| # | Item | Competing values | What closes it |
|---|---|---|---|
| **U1** | **Sentry post base shear (C9)** | STAAD **73.18 kN** vs hand **59.3 kN** (23 % apart, not reverse-engineerable: 73.18/624.5 → A<sub>h</sub> ≈ 0.117, not 0.100) | Print the STAAD seismic-weight summary. **Design already uses the higher value.** |
| **U2** | **Is a direct hit a requirement?** | Not stated anywhere | **Military representative sign-off.** Changes cover depth and burster design entirely. |
| **U3** | **Design basis threat yield** | 50 psi / t<sub>d</sub> 0.13–1.33 s stated, but the yield behind it is not | Client confirmation. Drives prompt-radiation cover depth. |
| **U4** | STAAD analysis/design command blocks | Never shown | Upload the `.std` files |
| **U5** | Underground model plate table and support definition | Never shown | Upload the `.std` files |
| **U6** | Node 213, sentry post | Row visible, values cut off | Upload the `.std` file |
| **U7** | Beam 16 (211→212), sentry post | Not visible; required for a closed frame | Upload the `.std` file |
| **U8** | Roof projection + parapet 4.162 kN/m | Given on the framing plan, not independently derived | Recompute from the parapet detail |

> **Update, 3 September 2026 — the `.std` files are now in the workspace. No tag above has been changed.**
> **U4** and **U5** are answerable from them directly: both models end with `PERFORM ANALYSIS PRINT STATICS CHECK` and no P-Delta; the underground model has **1 138 shell elements** in four thickness groups (mat 600 / roof 900 / perimeter 600 / internal 200–400) on `ELASTIC MAT DIRECT Y SUBGRADE 100000`. Note that its closing `START CONCRETE DESIGN … DESIGN ELEMENT 509 TO 688 869 TO 922` block contradicts its own `NO DESIGN` header comment; it has been left in place.
> **U6** — the sentry model has **twelve joints. There is no node 213.**
> **U7** — beam `16 211 212` is present, exactly as reconstructed.
> **U1** — the sentry model does now print the seismic-weight summary the item asks for: roof 331.46 + floor 400.34 = **W 731.80 kN**, V<sub>b</sub> = 0.100 × 731.80 = 73.18 kN, so V<sub>b</sub>/W returns A<sub>h</sub> = 0.1000 exactly. **[DERIVED, requires the user's confirmation before U1 is closed]** rebuilding both storey weights from the model's own load blocks reproduces 331.46 and 400.34 exactly, and the 139.1 kN gap to the B.8 hand check resolves as (i) 107.9 kN — half the first-storey infill, which the B.8 floor line does not allocate — plus (ii) 31.1 kN, the model taking the full 450 beam depth in `SELFWEIGHT` while also applying the full slab pressure, where B.8 nets the beam to 300. **U1 remains open. U2, U3 and U8 are untouched.**

## K.2 ASSUMED — must be confirmed before construction

| # | Assumption | Impact if wrong | Verify by |
|---|---|---|---|
| A1 | Rockhead 1.5–2.0 m, competent below | Founding level, excavation cost | Site investigation |
| A2 | **GWT (−)2.000** | **Uplift, flotation, waterproofing class, wall design** | **Monsoon-season monitoring** |
| A3 | SBC 3240 kPa | Footing and mat sizing (both ≪ 13 % utilised) | Plate load / core testing |
| A4 | **k<sub>s</sub> 100 000–500 000 kN/m³** | **Mat moments — sensitive. Run both bounds** | Plate load test |
| A5 | K₀ = 0.50, γ 20/21 | Wall lateral load | Site investigation |
| A6 | K<sub>a</sub> = 1.0 saturated (used); K<sub>a</sub> ≈ 0.5 dry berm (**not relied on**) | Headhouse wall load — removed from the critical path by C10 | Would allow a reduction if measured |
| A7 | Soak-pit absorption 20 L/m²/day | **Soak pit will not work if lower — likely on basalt** | **Percolation test, IS 2470 Pt 2 Cl. 4 — MANDATORY** |
| A8 | Structural seepage 0.5 L/m²/day | Sump storage (currently 8.4 days) | Packer permeability tests |
| A9 | Sentry infill NOT separated → R = 3.0 | V<sub>b</sub> × 1.67 if separated | Architect's decision |
| A10 | k1 = 1.08 (100-yr wind life) | Wind (does not govern) | Client brief |
| A11 | b<sub>eff</sub> = 2.5 m for the HW3 line load | HW3 strip check (26 % / 41 %) | Refined FE if ever critical |
| A12 | Trapezoid factor 0.7946 used for both BM and FEM | ~2 % on B2 support moment | Frame model |
| A13 | Sentry post STAAD has no member releases | Frame moment distribution | Upload the `.std` file |
| A14 | Poisson's ratio 0.20 | Plate behaviour, minor | Standard |

## K.3 CONFIRMED but requiring attention

| # | Item |
|---|---|
| **F1** | Protective boundary was not continuous — **resolved by M1 — APPROVED AND IMPLEMENTED 3 Sep 2026, see H.4** |
| **F2** | Stair-void cantilever M(root) 758.6 > midspan 700.2 — **resolved, links added** |
| **ERR-1** | My own yield-line coefficient error, 324.4 → 162.2 — **corrected; no reinforcement change** |
| Flotation | FoS 0.33 at the mat-only stage — **a design output, mitigation is mandatory and on S-02** |
| **Deccan basalt resistivity** 10³–10⁴ Ω·m | **Test earth resistance early** — affects EMP and lightning protection |
| Airlock purge 13 min | **4–5 persons/hour — a manning constraint, must be on the drill card** |
| EMP rebar cage 0 dB @ 1 GHz | **Say it before a reviewer does.** Zone 2 welded steel room is the answer |

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
COMBINATIONS        Box 101/102/**103 BLAST**/104/105  ·  Sentry 101–113, 201, 202

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

STATUS      STAAD    2 models exist; .std NOT uploaded; screenshots only
            DXF      8 output sheets S-01…S-08, validated, + A1 PDFs
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
