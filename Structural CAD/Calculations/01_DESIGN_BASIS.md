# 01 — DESIGN BASIS
## Structural reinforcement package, underground shelter · package revision **SC1**
### Phase B deliverable · 4 September 2026

**Authority:** `master/MASTER_PROJECT_STATE.md` Parts A, B, C, F, G, L.
**Nothing in this document is new design.** It restates the established basis, states the
methodology this package uses, and records the **one arithmetic discrepancy** found while
re-verifying it.

> **SENTRY POST — EXCLUDED.** Master B.8 and F.4 are not used. No sentry value appears anywhere.

---

## B.1 Verification performed for this package

Every design value in master Part B that this package relies on was **independently recomputed**
from first principles by `Structural CAD/Scripts/verify_partB.py` using the engine
`Structural CAD/Scripts/rc_calc.py`. Full output: `Calculations/00_PartB_verification_output.txt`.

```
212 values recomputed   ·   211 agree   ·   1 differs
```

**Every reinforcement-governing value agrees** — moments, required and provided steel, x_u/d,
τ_v, τ_c, V_us, A_sv/s_v, link spacings, minimum steel, development and lap lengths,
utilisations and the blast dynamic strengths.

**IS 456 Table 19 (τ_c) is self-validating in this project.** The τ_c column for M35 held in
`rc_calc.py` reproduces **eight** independent master values to ≤ 0.1 %:

| pt % | master τ_c | recomputed | element |
|---|---|---|---|
| 0.259 | 0.375 | 0.3748 | B.1 perimeter walls |
| 0.612 | 0.540 | 0.5403 | B.2 W6/W7 |
| 0.403 | 0.450 | 0.4496 | B.4 roof slab |
| 0.505 | 0.502 | 0.5017 | B.7.1 headhouse roof |
| 0.392 | 0.444 | 0.4438 | B.7.2 headhouse walls |
| 0.460 | 0.479 | 0.4792 | B.5 main stair flight |
| 0.552 | 0.519 | 0.5187 | B.5 stair landings |
| 0.470 | 0.484 | 0.4844 | B.6 entry stairwell flight |

This is **corroboration, not verification against the code.** No copy of IS 456 is in the
workspace (audit §A.6). It shows the table used here is the same table master Part B used.

---

## B.2 ⚠ NEW CONFLICT **C17** — engineered cover build-up does not sum

**Raised by this package. NOT resolved. Requires the user's ruling (CLAUDE.md, master rule M.5).**

Master A.7.3 tabulates the 2 000 mm engineered cover:

| Layer | Thickness | γ | Load |
|---|---|---|---|
| Topsoil / turf | 300 | 18 | 5.40 |
| Granular filter | 150 | 19 | 2.85 |
| RC burster slab M30 | 200 | 25 | 5.00 |
| Crushed basalt rubble | 500 | 17 | 8.50 |
| Compacted engineered fill | 750 | 20 | 15.00 |
| Protection screed | 100 | 24 | 2.40 |
| **Σ thickness** | **2 000 ✔** | | **Σ load = 39.15** |
| **Master's stated TOTAL** | | | **40.65** |

**The column sums to 39.15 kPa. The master states 40.65 kPa — a difference of exactly 1.50 kPa.**
Each individual line is arithmetically correct; the total row is not the sum of the column.

| | Value A | Value B |
|---|---|---|
| Source | Master A.7.3 **total row**, A.7.4, Part L, and `DL2 EARTH COVER ON ROOF 40.65 KN/M2` in all four underground `.std` files | Master A.7.3 **column sum** |
| Value | **40.65 kPa** | 39.15 kPa |

**Held by this package: 40.65 kPa.** Reasons, stated rather than assumed:

1. It is the value in **Part A, Part L and every STAAD model** — the design of record.
2. It is the **larger** value, so retaining it is **conservative**: roof COMB 103 stays at
   448.15 kPa rather than 446.65 kPa (−0.33 %). Roof M_p would fall 700.2 → 697.9 kNm/m and
   utilisation 51.4 % → 51.2 %. **No bar, spacing or link changes.**
3. Silently adopting 39.15 would *reduce* a design load — forbidden without a ruling.

**Status: [UNRESOLVED] — C17.** Every drawing produced by this package that states the roof
loading carries a **C17 note**. Impact on reinforcement: **none**. Impact on the load register:
**the master's own A.7.3 total row and its column disagree and one of them must be corrected.**

---

## B.3 Materials

| Property | Value | Source | Class |
|---|---|---|---|
| Concrete, **all in-scope elements** | **M35** | A.5; `ISOTROPIC M35` in both in-scope `.std` | [CONFIRMED] |
| w/c ≤ 0.45, cement ≥ 340 kg/m³ | IS 456 Table 5 | A.5 | [CONFIRMED] |
| Admixture | Integral crystalline waterproofing | A.5 | [RECONSTRUCTED] |
| Blinding | M15, 100 thk at (−)6.800 | A.5 | [CONFIRMED] |
| Reinforcement | **Fe500D to IS 1786:2008** | A.5 | [CONFIRMED] |
| E_c = 5000√f_ck | **29 580 N/mm²** | IS 456 Cl. 6.2.3.1; `E 2.95804e+07` kN/m² | [CONFIRMED] |
| Poisson's ratio | 0.20 | A.5 | [ASSUMED] |
| Unit weight RC | 25 kN/m³ | IS 875 (Pt 1) Table 1 | [CONFIRMED] |
| γ_m concrete / steel | 1.5 / 1.15 | IS 456 Cl. 36.4.2 | [CONFIRMED] |

**Blast case only — IS 4991 Cl. 10.3.1:** f_ck,dyn = 1.25 × 35 = **43.75 N/mm²**;
f_y,dyn = 1.25 × 500 = **625 N/mm²**.

> ### ⚠ IS 4991 Cl. 10.3.1.1 — NO DYNAMIC INCREASE ON SHEAR.
> τ_c and τ_c,max are read at the **static M35** values in every blast check in this package.
> `rc_calc.shear_check()` takes a separate `fck_static` argument and physically cannot be handed
> a dynamic grade for τ_c. This is the most commonly mis-applied rule in blast design (master M.17)
> and it is why the roof, W6/W7, the mat, the headhouse roof and the headhouse walls all carry
> links they would not otherwise need.

**IS 4991 scope, restated on every drawing:** *IS 4991:1968 Cl. 1.1 expressly EXCLUDES nuclear
explosions from its scope.* It is used here **only** for loading rules and dynamic material
strengths, as a documented conservative extrapolation. **Every capacity is computed to IS 456.**

---

## B.4 Cover, spacing, development and laps

### Cover — IS 456 Cl. 26.4.2 / Table 16 [CONFIRMED]

| Face | Cover |
|---|---|
| Cast against blinding / trimmed rock (mat bottom) | **75 mm** |
| Formed earth face (external wall outer face, roof top) | **50 mm** — **but see note** |
| Internal faces | **40 mm** |
| Stair-shaft faces (wet / dirty zone) | **30 mm** |

> **Note — the roof and mat use 75 mm.** Master B.3 and B.4 both take d from a **75 mm** cover
> (mat d = 600 − 75 − 8 = 517; roof d = 900 − 75 − 12.5 = 812.5). The 75 mm is applied to the
> roof top face and to the mat soffit. This package reproduces master Part B exactly and does
> **not** re-optimise cover.

> The 5 mm reduction IS 456 Table 16 permits for M35 and above is **deliberately not taken**.

### Bar spacing

**Maximum bar spacing = 150 mm, both curtains, every blast-rated element — an EMP requirement**,
stricter than IS 456 Cl. 26.3.3 and stricter than every code minimum. It, not strength, sets the
spacing of the main steel in the roof, the perimeter walls, W6/W7, the mat and the headhouse.

### Development and lap — IS 456 Cl. 26.2.1, 26.2.1.1, 26.2.5.1 [CONFIRMED, recomputed]

```
Ld = phi x 0.87 fy /(4 tau_bd) ;  tau_bd(M35) = 1.7 x 1.6 = 2.72  ->  Ld = 40 phi
Compression: tau_bd x 1.25                                        ->  Ld,c = 32 phi
```

| Bar | L_d tension (M35) | L_d compression | **Lap (50 φ, staggered)** |
|---|---|---|---|
| T8 | 320 | 256 | 400 |
| T10 | 400 | 320 | 500 |
| T12 | 480 | 384 | 600 |
| T16 | 640 | 512 | 800 |
| T20 | 800 | 640 | 1 000 |
| T25 | 1 000 | 800 | 1 250 |

**Lap policy.** IS 456 Cl. 26.2.5.1(c) gives lap = L_d or 30 φ, whichever greater = 40 φ.
Cl. 26.2.5.1 requires ×1.4 if more than 50 % of bars are lapped at one section. **All laps are
staggered so that ≤ 50 % are spliced at any one section, and the lap is specified at 50 φ** —
25 % above requirement, and the ×1.4 factor is therefore not triggered.

**Blast bond allowance NOT taken.** IS 4991 Cl. 10.3.1.1 permits +25 % on bond (→ 32 φ).
All detailing in this package uses the **static 40 φ**.

---

## B.5 Loading

### B.5.1 Blast — master A.7.1 [CONFIRMED, recomputed]

```
DBT                     nuclear air-blast, p_so = 344.7 kPa (50 psi)
Positive phase td       0.13 to 1.33 s
Reflected pressure p_r  1366 kPa      Dynamic pressure q  282 kPa
Ductility ratio mu      5  (moderate, repairable damage)      IS 4991 Cl. 10.3.3
DLF = mu/(mu - 0.5)     5/4.5 = 1.111    [validation: mu = 1 -> DLF 2.00 = step load]
DESIGN BLAST PRESSURE   344.7 x 1.111 = 383 kPa
                        on the ROOF **and** the WALLS  (Ka = 1.0, saturated soil)
Roof natural period T   13.4 ms  ->  td/T = 10 to 100  ->  QUASI-STATIC
```

### B.5.2 Gravity, soil and water — master A.7.2 [CONFIRMED, recomputed]

| Load | Value | Applies to |
|---|---|---|
| Roof self, 0.900 × 25 | 22.50 kPa | roof |
| Mat self, 0.600 × 25 | 15.00 kPa | mat |
| **Engineered cover** | **40.65 kPa** — **see C17 §B.2** | roof |
| SIDL | 2.0 kPa roof / 1.0 kPa mat | |
| Internal floor live | **5.0 kPa** (plant/storage) | floor |
| Earth + water lateral gradient, K₀γ′ + γ_w = 0.50 × 11.19 + 9.81 | **15.41 kPa/m** | external walls |
| — at roof soffit (−)2.900 | 33.9 kPa | |
| — at floor (−)6.100 | **83.2 kPa** | |
| Hydrostatic uplift on mat, 4.700 × 9.81 | **46.11 kPa** (6 289 kN over 136.4 m²) | mat |
| Construction surcharge | 20 vertical / 10 lateral | |
| Staircase smeared on the two shaft walls | 2.947 kPa | W6, W7 |

> Of the 15.41 kPa/m lateral gradient, **9.81 is water and only 5.60 is soil.**
> **A2 (GWT −2.000) is [ASSUMED] and is the single most important number in the design.**

### B.5.3 Roof total — COMB 103

| Component | kPa |
|---|---|
| Blast, 344.7 × 1.111 | 383.00 |
| Engineered cover (C17) | 40.65 |
| SIDL | 2.00 |
| Self weight | 22.50 |
| **TOTAL w** | **448.15** |

**Live load excluded — IS 4991 Cl. 11.2:** *"No live load shall be considered on roof at the time
of blast."* Static ULS 101 on the roof = 1.5 × (40.65 + 2.0 + 22.5 + 20) = 127.7 kPa
→ **blast governs 3.51 : 1**. Recomputed ✔

### B.5.4 Headhouse — master A.7.5

| Element | Load | Basis |
|---|---|---|
| Roof, 500 | **396.5 kPa** = 383 + 12.5 self + 1.0 SIDL | IS 4991 Cl. 7.2 |
| Walls HW1–HW4, 400 | **383 kPa acting on EITHER FACE** (conflict C10, resolved) | IS 4991 Cl. 7.2 |

> **The walls are reinforced symmetrically for 383 kPa either way — a stated requirement, not an
> accident of detailing.** The inner security door is not blast rated and the entry stairwell is
> expected to be lost, so the headhouse fills and the walls are pushed **outwards**.

### B.5.5 Entry stairwell — master A.7.6, **static only, NOT blast rated**

| Element | Load |
|---|---|
| Flight, waist 250 | 7.150 + 2.083 + 1.000 + LL 5.000 = 15.233 → **w_u = 22.85 kPa** |
| Side walls 250 | 0.5 × 20 × 2.9 + 0.5 × 10 = **34 kPa at base** |
| Raking roof 250 | 6.25 + 2.0 + 5.4 + **imposed 20** = 33.65 → **w_u = 50.5 kPa** |
| Top landing 250 | 18.4 + flight reaction 36.5 = **54.9 kPa** |

The 20 kPa roof imposed load is deliberate — a stray vehicle on the berm (C12/C13, resolved).

### B.5.6 Main staircase — master B.5, **inside the envelope, NOT a blast element**

The shaft pressurises, but that pressure acts on the shaft **walls** and the blast **doors**, not
as a net load on a slab open on both faces. **Designed to IS 456 with normal partial factors,
NOT with IS 4991 dynamic strengths.** Flight w_u = 21.0 kPa; landings 44.20 kPa.

### B.5.7 Seismic — master A.7.8

```
Underground box, IS 1893 (Part 1):2016
  Z 0.16 (Zone III) · I 1.5 · R 4.0 · Sa/g 2.5  ->  Ah = 0.075
  W 14 002 kN  ->  Vb = 1050 kN
  Per long wall 525 kN  ->  tau = 0.063 N/mm^2   NEGLIGIBLE
  IS 13920 Cl. 10.4 boundary elements  NOT TRIGGERED
```

**Blast governs every blast-rated element** (roof 3.51 : 1, walls 4.6 : 1). **Wind and earthquake
are absent from COMB 103 — IS 4991 Cl. 11.1 forbids combining them with blast.**

---

## B.6 Load combinations — master A.7.9, confirmed against the `.std`

**Underground box (5, matching all four underground models):**

| No. | Title (verbatim from the file) | Factors |
|---|---|---|
| 101 | `ULS STATIC 1.5(DL+LL+EARTH+WATER)` | 1.5 (DL + SIDL + LL + SOIL + UPLIFT) |
| 102 | `ULS UPLIFT 0.9DL + 1.5 HYDROSTATIC` | 0.9 DL + 1.5 UPLIFT |
| **103** | **`BLAST 1.0(DL + EARTH + WATER + BLAST) GAMMA = 1.0`** | **1.0 (DL + SIDL + SOIL + UPLIFT + BLAST)** |
| 104 | `SLS 1.0(DL+LL+EARTH+WATER) FOR CRACK WIDTH TO IS 3370` | 1.0 service |
| 105 | `CONSTRUCTION 1.5(DL + EARTH + WATER + SURCHARGE)` | 1.5 |

> γ = 1.0 on blast because it is an extreme event checked against **ultimate** capacity with
> **dynamic** material strengths (IS 4991 Cl. 10.3.1). Applying 1.5 while also taking the 25 %
> material bonus would be inconsistent.

**Entry stairwell (5, from `Entry_Stairwell.std`):** 101 (1.5 DL+LL+earth+surcharge) ·
102 (1.5, no roof LL) · 103 (0.9 DL + 1.5 earth + surcharge, minimum restraint) ·
104 (1.5 DL + 1.5 earth one side, construction) · 201 (1.0 service).

**COMB 103 governs the design of every blast-rated element in this package.**

---

## B.7 Governing action per element — the design basis table

**MANUAL CALCULATION — NOT DIRECT STAAD OUTPUT** for every row. No STAAD result exists (audit §A.3).

| Element | Governing combination | Mechanism / model | Design action |
|---|---|---|---|
| W1–W4, 600 | **103 BLAST** | fixed-fixed one-way strip, L_n 3.200 | M_p = w L_n²/16 = **245.1 kNm/m**; V at d = 414.8 kN/m; N = 1 168 kN/m |
| W5, 200 | — | no pressure differential | nominal, min steel |
| **W6 / W7, 400** | **103 BLAST (LOAD 11, BL3)** | fixed-fixed strip; shaft equalises to full p_so (Finding F1) | M_p = **245.1 kNm/m**; V at d = 481.8 kN/m |
| W8 partitions, 110 | — | non-structural | A252 mesh |
| **Mat, 600** | **103 BLAST, soft/red-bole band** | 3.0 m unsupported band, M = qL²/12 at q = 404.9 kPa | **303.7 kNm/m**; V = 398.0 kN/m |
| Mat, alternative | 102 UPLIFT | net 31.1 kPa up over 5.0 m | 48.6 kNm/m — **nominal, does not govern** |
| **Roof slab, 900** | **103 BLAST** | fixed-fixed one-way strip over the 5 000 clear width | **M_p = 700.2 kNm/m**; V at d = 756.3 kN/m |
| Roof cantilever pad | **103 BLAST** | 1 840 cantilever, M = wL²/2 | **758.6 kNm/m — exceeds the mid-span M_p** (Finding F2); V = 824.6 kN/m |
| ESC collars | 103 BLAST | interrupted-steel replacement, 3 272 × 1.400 | 4 581 mm²/face/direction to be trimmed |
| Blast-door jambs | 103 BLAST | interrupted-steel replacement, 2 094 × 1.2 | 2 513 mm²/face → 1 256 per jamb |
| Blast-door header | 103 BLAST | 400 × 1100 over 1 200 clear, w = 402 kN/m | M = wL²/12 = 48.2 kNm; V = 241 kN |
| **HH roof, 500** | **103 BLAST** | one-way fixed-fixed (most conservative of three) | **396.5 kNm/m**; V at d = 628.4 kN/m |
| HH walls, 400 | **103 BLAST, either face** | fixed-fixed strip, 2 400 clear | **137.9 kNm/m**; V at d = 328.6 kN/m |
| HH door edge band | 103 BLAST | 400 × 800 band, w = 402 kN/m over 900 | M = 27.1 kNm; V = 181 kN |
| HW3 line load | 103 BLAST | slab strip as a beam, b_eff 2.5 m | 354 kNm/m (two-way) / 552 (one-way bound) — **26 % / 41 %** |
| Main stair flight | IS 456 ULS, 1.5 | simply supported, L_eff 3 160 | 26.2 kNm/m |
| Main stair landings | IS 456 ULS, 1.5 | spanning across the shaft, L_eff 3 000 | 49.7 kNm/m |
| Entry stairwell flight | IS 456 ULS, 1.5 | simply supported, L_eff 4 800 | 65.8 kNm/m |
| Entry stairwell walls / roof / landings | IS 456 ULS, 1.5 | encastre strip | 14.0 / 9.5 / 21.0 kNm/m — **minimum steel governs** |

---

## B.8 Design methodology

**Flexure — IS 456 Annex G-1.1(b), Cl. 38.1, 38.1(f), Annex G-1.1(c):**
```
Mu     = 0.87 fy Ast d [1 - Ast fy /(b d fck)]
xu     = 0.87 fy Ast /(0.36 fck b)          xu,max/d = 0.46  (Fe500)
Mu,lim = 0.133 fck b d^2
```
**Shear — IS 456 Cl. 40.1, 40.2.1.1, 40.2.3, 40.4(a), 26.5.1.5:**
```
tau_v  = Vu /(b d)      tau_c = Table 19 (interpolated on pt)      tau_c,max = Table 20
Vus    = (tau_v - tau_c) b d       Asv/sv = Vus /(0.87 fy d)
sv,max = min(0.75 d, 300)
```
**Minimum steel:** slabs 0.12 % (Cl. 26.5.2.1); walls vertical 0.12 % (Cl. 32.5(a)), horizontal
0.20 % (Cl. 32.5(b)), two curtains where t > 200 (Cl. 32.5(c)); IS 3370 Pt 2 surface zone
0.35 % over 250 mm each face.
**Maximum bar diameter in slabs:** D/8 (Cl. 26.5.2.2) — 900/8 = 112 mm, T25 ✔.
**Effective span:** Cl. 22.2(a); stairs Cl. 33.1(b) and Cl. 33.2.
**Deflection:** Cl. 23.2.1 + Fig. 4 (stairs only — the blast elements are governed by strength).

**What is deliberately NOT claimed:**

1. **Support rotation / ductility for the blast case is NOT demonstrated.** θ ≤ 2° needs a
   non-linear SDOF check (IS 4991 Fig. 6 / Biggs) — **Phase 3**. A quasi-static analysis gives
   **demand**, never proof of blast resistance.
2. **Flotation cannot be shown by the elastic-mat model** — the springs take tension, so the mat
   never lifts in the model. It is a hand check on real dimensions (B.3), and the **construction
   stage governs at FoS 0.33**.
3. **Crack width to IS 3370 Pt 2 is satisfied by the surface-zone steel rule, not by calculation.**
4. **Shock propagation down the entry shaft, transient soil–structure interaction, and blast-door
   performance** are not civil deliverables of this package.

---

## B.9 Codes actually citable in this package

**No code document is in the workspace (audit §A.6).** Clause numbers are taken **only** from the
verified master Part G register. Any check requiring a clause outside that register is reported
**"CLAUSE NOT VERIFIABLE — code document not in workspace"** and given status **NOT DETERMINABLE**.

| Standard | Role in this package |
|---|---|
| **IS 456:2000** | **All capacity, detailing, minimum steel, cover, L_d, laps, spacing, shear.** Every capacity in the package is an IS 456 capacity |
| **IS 1786:2008** | Fe500D bar grade |
| **IS 3370 (1,2):2021** | 0.2 mm crack limit; 0.35 % surface-zone steel |
| **IS 875 (1,2,5)** | Dead, imposed, combination |
| **IS 1893 (Pt 1):2016** | Box seismic — established as **not governing** |
| **IS 13920:2016** | **Applicability determined element by element** — see `QAQC/IS13920_Compliance_Matrix.md`. Cl. 10.4 checked and **not triggered** |
| **IS 4991:1968** | **Blast loading rules and dynamic material strengths ONLY.** Cl. 1.1 excludes nuclear — quoted on every drawing |
| **IS 1904:1986 · IS 2950(1) · IS 12070** | Bearing, raft, rock settlement |
| **SP 34:1987** | Detailing; **Cl. 5.5 opening-corner rule** (entry stairwell) |
| **NBC 2016 Pt 4** | Stair geometry, 1 100 guarding |
| **SP 16:1980 · BS 8666 · UFC 3-340-02** | Design aids; shape codes; §4-27 opening trimmers, §4-30 direct shear — **cited as US criteria, not as IS** |
| **IS 2502** | **NAMED IN THE BRIEF BUT NOT IN PART G AND NOT IN THE WORKSPACE — NOT CITED.** Bar bending uses declared project rule **PBR-1** |

---

## B.10 Package conventions established here

| # | Convention | Value |
|---|---|---|
| **PBR-1** | Cut length = Σ scheduled leg dimensions, **no bend deduction**; links add 2 × 10 φ for 135° hooks. Conservative by ≈ 2 φ per 90° bend | [ASSUMED — no standard in the workspace] |
| **P-1** | Stock bar length **12 000 mm**; longer bars scheduled in ≤ 12 000 lengths with `ceil(L/12000) − 1` laps of 50 φ added, staggered | [ASSUMED] |
| **P-3** | Bar-mark prefixes **F** foundation · **W** wall · **S** slab · **B** beam-type · **ST** stair · **H** headhouse · **E** entrance/stairwell · **T** typical. **C reserved and unused — no column exists** | project |
| **X1** | DXF written as **AutoCAD 2010 (AC1024) ASCII** so that native DIMENSION / MTEXT / HATCH / LEADER / BLOCK entities are available (brief §25). Master E.3.1's R12 standard applies to S-01…S-08, which are untouched | declared deviation |
| **X2** | Layers use the brief's **`S-*`** system; a one-to-one mapping to the master's 22-layer table is issued in `Documentation/02_CAD_STANDARDS.md` | declared deviation |
| **Steel density** | 0.0061654 φ² kg/m (7 850 kg/m³) | standard |

---

## B.11 Open items carried forward, unresolved

| Ref | Item | Effect on this package |
|---|---|---|
| **C16** | Roof / platform junction — 500 headhouse roof (A.4.7) vs 250 stairwell roof (B.6 / A.7.6 / F.2) | **Detailing follows 250. Every affected sheet carries a C16 OPEN flag.** Not resolved |
| **C17** | Cover build-up 40.65 (stated) vs 39.15 (column sum) — **NEW, raised here** | **40.65 held.** No reinforcement effect. Flagged on the loading panel of every affected sheet |
| **A2** | GWT (−)2.000 [ASSUMED] | Governs uplift, lateral load, mat and wall steel |
| **A4** | k_s second bound (500 000) never run | Mat moment distribution not bounded on the stiff side |
| **M-1** | **No STAAD result of any kind** | Every action is a hand calculation, labelled as such |
| **M-2** | **No code document** | Clause citation restricted to master Part G |
| **U2 / U3** | Direct-hit requirement; DBT yield | Cover depth and burster design |
| **Phase 3** | SDOF support rotation | Blast **capacity** not demonstrated |

**Phase B is complete. Proceeding to Phase C — element-by-element reinforcement design.**
