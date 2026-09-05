# IS 456:2000 COMPLIANCE MATRIX
## Structural CAD reinforcement package · revision **SC1** · 4 September 2026

> ### ⚠ CLAUSE VERIFICATION — READ FIRST
> **No copy of IS 456:2000 is held in this workspace** (input audit §A.6). Clause numbers below
> are taken **only** from the project's verified clause register, master **Part G**, which states:
> *"No clause number in this register was invented. Where a clause could not be confirmed from the
> material available it is not listed."*
> A check that would need a clause **outside** that register is reported
> **"CLAUSE NOT VERIFIABLE"** and given status **NOT DETERMINABLE**. No clause number is guessed.
>
> **Every design action below is `MANUAL CALCULATION — NOT DIRECT STAAD OUTPUT`.**
> No STAAD result exists for any underground or entry-stairwell model.

**Status key:** **PASS** — checked and satisfied · **REVIEW** — satisfied but needs engineering
review · **NOT DETERMINABLE** — cannot be decided from the information held.

**Sentry post excluded throughout.**

---

## 1 — MATERIALS, DURABILITY AND COVER

| # | Requirement | Clause | Project value | Required | Provided | Status |
|---|---|---|---|---|---|---|
| 1.1 | Concrete grade for very severe exposure | Table 3, Table 5 | Buried, saturated, aggressive | **M35 min** | **M35** | **PASS** |
| 1.2 | Maximum w/c ratio | Table 5 | very severe | ≤ 0.45 | ≤ 0.45 specified | **PASS** |
| 1.3 | Minimum cement content | Table 5 | very severe | ≥ 340 kg/m³ | ≥ 340 specified | **PASS** |
| 1.4 | Modulus of elasticity E_c = 5000√f_ck | Cl. 6.2.3.1 | M35 | 29 580 N/mm² | 29 580 (`E 2.95804e7` in the `.std`) | **PASS** |
| 1.5 | Partial safety factors γ_m | Cl. 36.4.2 | — | 1.5 / 1.15 | 1.5 / 1.15 | **PASS** |
| 1.6 | Cover, cast against blinding / rock | Cl. 26.4.2.1, Table 16 | mat soffit, roof top | ≥ 50 (very severe 45+) | **75** | **PASS** |
| 1.7 | Cover, formed earth face | Cl. 26.4.2, Table 16 | external wall outer face | very severe | **50** | **PASS** |
| 1.8 | Cover, internal faces | Cl. 26.4.2, Table 16 | internal | — | **40** | **PASS** |
| 1.9 | Cover, stair-shaft faces | Cl. 26.4.2, Table 16 | wet/dirty zone | — | **30** | **PASS** |
| 1.10 | 5 mm cover reduction permitted for M35+ | Table 16 | permitted | — | **DELIBERATELY NOT TAKEN** | **PASS** |
| 1.11 | Cover ≥ bar diameter | Cl. 26.4.2 | max bar T25 | 25 | 30 min anywhere; 75 to T25 | **PASS** |

## 2 — FLEXURE AND SECTION CAPACITY

Equation used throughout: **M_u = 0.87 f_y A_st d [1 − A_st f_y /(b d f_ck)]** — Annex G-1.1(b);
**x_u = 0.87 f_y A_st /(0.36 f_ck b)** — Cl. 38.1; **x_u,max/d = 0.46 (Fe500)** — Cl. 38.1(f);
**M_u,lim = 0.133 f_ck b d²** — Annex G-1.1(c).

| # | Element | Clause | M demand kNm/m | M_u,lim | A_st req | A_st prov | M_u prov | x_u/d | Util. | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| 2.1 | **Mat 600** | G-1.1(b), 38.1(f) | 303.7 | 4 100 | 1 115 | **1 340** | 362.8 | 0.089 | **84 %** | **PASS** |
| 2.2 | **Perimeter walls 600** | G-1.1(b) | 245.1 | 1 556 | 894 | **1 340** | 362.8 | 0.089 | 68 % | **PASS** |
| 2.3 | **W6 / W7 400** | G-1.1(b) | 245.1 | 680.6 | 1 400 | **2 094** | 355.3 | 0.211 | 69 % | **PASS** |
| 2.4 | W5 200 | G-1.1(b) | nominal | 138.0 | — | 754 | — | — | nominal | **PASS** |
| 2.5 | **Roof slab 900** | G-1.1(b) | 700.2 | 3 841 | 1 632 | **3 272** | 1 362.4 | **0.139** | 51 % | **PASS** |
| 2.6 | Roof cantilever pad | G-1.1(b) | 758.6 | 3 841 | 1 772 | 3 272 | 1 362.4 | 0.139 | 56 % | **PASS** |
| 2.7 | **Headhouse roof 500** | G-1.1(b) | 396.5 | 1 002 | 1 879 | **2 094** | 438.5 | 0.174 | **90 %** | **REVIEW** |
| 2.8 | Headhouse walls 400 | G-1.1(b) | 137.9 | 681 | 766 | 1 340 | 235.2 | 0.135 | 59 % | **PASS** |
| 2.9 | Main stair flight 200 | G-1.1(b) | 26.2 | — | 380 | 754 | 50.3 | — | 52 % | **PASS** |
| 2.10 | Main stair landings 200 | G-1.1(b) | 49.7 | — | 745 | **905** | 59.5 | — | **84 %** | **PASS** |
| 2.11 | Entry stairwell flight 250 | G-1.1(b) | 65.8 | — | 744 | 1 005 | 87.3 | 0.162 | 75 % | **PASS** |
| 2.12 | Entry stairwell walls/roof/landings | G-1.1(b) | 9.5–21.0 | — | 108–229 | 565 | 48.2–50.6 | — | 20–41 % | **PASS** |

> **2.7 is REVIEW, not PASS-with-comfort:** 90 % on the one-way strip is the tightest element in
> the package, and it arrived there through conflict C2 (the report designed a 3.0 m span with
> 1.0 m of cover; Rev F is 4.0 m with none). Two-way and yield-line analyses give 65 % and 37 %,
> but the **one-way result is the one adopted**. Any load or geometry change re-opens it.

**Every section is under-reinforced (x_u/d ≤ 0.211 ≪ 0.46) and singly reinforced.** `PASS`

## 3 — SHEAR

τ_v = V_u/(bd) — Cl. 40.1 · τ_c from Table 19 · τ_c,max Table 20 · V_us = (τ_v − τ_c)bd and
A_sv/s_v = V_us/(0.87 f_y d) — Cl. 40.4(a) · s_v,max = min(0.75 d, 300) — Cl. 26.5.1.5.

> **IS 4991 Cl. 10.3.1.1 allows NO dynamic increase on shear.** τ_c and τ_c,max are read at the
> **static M35** value in every blast check. The calculation engine physically cannot be handed a
> dynamic grade for τ_c.

| # | Element | τ_v | τ_c | τ_c,max | V_us kN/m | A_sv/s_v req | s_v calc | s_v limit (26.5.1.5) | **Provided** | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| 3.1 | Mat 600 | 0.770 | 0.375 | 3.70 | 204.2 | 0.908 | — | 300 | **T12 @ 250×250 grid (1.810)** | **PASS** |
| 3.2 | Perimeter walls 600 | 0.802 | 0.375 | 3.70 | 220.8 | 0.982 | 230 | 300 | **T12 closed @ 200 (1.131)** | **PASS** |
| 3.3 | W6 / W7 400 | 1.409 | 0.540 | 3.70 | 297.2 | 1.998 | 226 | **257** | **T12 4L @ 200** | **PASS** |
| 3.4 | Roof slab 900 | 0.931 | 0.450 | 3.70 | 390.8 | 1.106 | 409 | **300 governs** | **T12 4L @ 250 end / 2L @ 300 mid** | **PASS** |
| 3.5 | Roof cantilever pad | 1.015 | 0.450 | 3.70 | 459.4 | 1.300 | 348 | **300 governs** | **T12 4L @ 250 throughout** | **PASS** |
| 3.6 | Headhouse roof 500 | 1.514 | 0.502 | 3.70 | 420.0 | 2.327 | 194 | 300 | **T12 4L @ 175 end / @ 250 mid** | **PASS** |
| 3.7 | Headhouse walls 400 | 0.961 | 0.444 | 3.70 | 176.9 | 1.189 | 381 | **256 governs** | **T12 4L @ 250** | **PASS** |
| 3.8 | Main stair flight | 0.202 | 0.479 × k 1.20 = 0.575 | 3.70 | 0 | — | — | — | **no links required** | **PASS** |
| 3.9 | Main stair landings | 0.404 | 0.519 × 1.20 = 0.622 | 3.70 | 0 | — | — | — | **no links required** | **PASS** |
| 3.10 | Entry stairwell flight | 0.256 | 0.484 × k 1.10 = 0.532 | 3.70 | 0 | — | — | — | **no links required** | **PASS** |
| 3.11 | τ_v ≤ τ_c,max everywhere | Cl. 40.2.3 | max τ_v = 1.514 | — | 3.70 | — | — | — | **41 % of the limit** | **PASS** |
| 3.12 | k factor for thin members | Cl. 40.2.1.1 | applied to the stairs only (200/250 thk) | — | — | — | — | — | k 1.10–1.20 | **PASS** |

**Punching shear, Cl. 31.6 / 31.6.1 / 31.6.3.1: NOT APPLICABLE — declared, not ignored.**
No column or pedestal bears on the mat; the headhouse walls bear on the roof slab. `PASS`

## 4 — MINIMUM AND MAXIMUM REINFORCEMENT

| # | Requirement | Clause | Element | Required | Provided | Status |
|---|---|---|---|---|---|---|
| 4.1 | Slab minimum 0.12 % (HYSD) | Cl. 26.5.2.1 | roof 900 | 1 080 | 3 272 | **PASS** |
| 4.2 | Slab minimum 0.12 % | Cl. 26.5.2.1 | HH roof 500 | 600 | 2 094 | **PASS** |
| 4.3 | Slab minimum 0.12 % | Cl. 26.5.2.1 | stair flight 200 | 240 | 754 | **PASS** |
| 4.4 | Max bar diameter in a slab, D/8 | Cl. 26.5.2.2 | roof 900 | ≤ 112 | T25 | **PASS** |
| 4.5 | Wall vertical minimum 0.12 % | Cl. 32.5(a) | perimeter 600 | 720 | 1 340 | **PASS** |
| 4.6 | Wall horizontal minimum 0.20 % | Cl. 32.5(b) | perimeter 600 | **1 200 — governs** | 1 340 | **PASS** |
| 4.7 | Wall horizontal minimum 0.20 % | Cl. 32.5(b) | HH walls 400 | **800 — governs the 766 required** | 1 340 | **PASS** |
| 4.8 | Wall vertical minimum 0.12 % | Cl. 32.5(a) | W6/W7 400 | 480 | 2 094 | **PASS** |
| 4.9 | Wall horizontal minimum | Cl. 32.5(b) | W5 200 | 400 | 754 | **PASS** |
| 4.10 | Two curtains where t > 200 | Cl. 32.5(c) | all walls ≥ 250 | required | provided everywhere | **PASS** |
| 4.11 | Wall slenderness / design method | Cl. 32.2 | walls braced top and bottom by mat and slab | — | walls designed in flexure, not as slender compression members | **PASS** |
| 4.12 | Maximum tension reinforcement 4 % | *not in the verified register* | max p_t provided 0.61 % | — | 0.61 % | **CLAUSE NOT VERIFIABLE — value is far below any credible limit** |
| 4.13 | Beam minimum / maximum steel and link limits | Cl. 26.5.1.1, 26.5.1.2, 26.5.1.6 | headers and edge bands | — | 4-T20 T/B, links @ 150 | **REVIEW** — clauses are in the register; the members are local bands, not beams as Cl. 26.5.1 contemplates |

## 5 — BAR SPACING

| # | Requirement | Clause | Value | Status |
|---|---|---|---|---|
| 5.1 | Maximum spacing of main bars | Cl. 26.3.3 | project cap **150 mm both curtains, all blast-rated elements — an EMP requirement, stricter than the code** | **PASS** |
| 5.2 | Maximum spacing, distribution steel | Cl. 26.3.3 | 200 (stairs), 150 elsewhere | **PASS** |
| 5.3 | Maximum link spacing | Cl. 26.5.1.5 | min(0.75 d, 300) — governs on 5 of 7 blast elements | **PASS** |
| 5.4 | Minimum clear bar spacing (aggregate + bar dia) | *not in the verified register* | worst case T25 @ 150 → 125 clear | **CLAUSE NOT VERIFIABLE — 125 mm clear is ample for a 20 mm aggregate** |

## 6 — DEVELOPMENT, ANCHORAGE AND LAPS

| # | Requirement | Clause | Value | Status |
|---|---|---|---|---|
| 6.1 | L_d = φ σ_s /(4 τ_bd) | Cl. 26.2.1 | **40 φ tension, 32 φ compression (M35)** | **PASS** |
| 6.2 | τ_bd for deformed bars, ×1.6 | Cl. 26.2.1.1 | 1.7 × 1.6 = 2.72 | **PASS** |
| 6.3 | Lap = L_d or 30 φ, whichever greater | Cl. 26.2.5.1(c) | 40 φ required | **PASS** |
| 6.4 | Lap ×1.4 if > 50 % spliced at one section | Cl. 26.2.5.1 | **all laps staggered ≤ 50 %; factor not triggered** | **PASS** |
| 6.5 | Lap actually specified | — | **50 φ — 25 % above requirement** | **PASS** |
| 6.6 | Anchorage of top steel into supports | Cl. 26.2.1 | L_d 1 000 (T25 roof), 800 (T16/T20 walls) | **PASS** |
| 6.7 | Trimmer anchorage past an opening | Cl. 26.2.1 + UFC 3-340-02 §4-27 (US criteria) | L_d beyond in both directions | **PASS** |
| 6.8 | Blast bond allowance +25 % (IS 4991 Cl. 10.3.1.1) | — | **NOT TAKEN — static 40 φ used** | **PASS** |
| 6.9 | Wall vertical anchorage into the 900 slab | Cl. 26.2.1 | 640 required (T16), **825 provided** | **PASS** |

## 7 — DEFLECTION AND SERVICEABILITY

| # | Element | Clause | L/d | Basic | f_s | p_t | MF | Permissible | Status |
|---|---|---|---|---|---|---|---|---|---|
| 7.1 | Main stair flight | Cl. 23.2.1 + Fig. 4 | 19.3 | 20 | 146 | 0.46 % | ≈1.9 | 38 | **PASS** |
| 7.2 | Main stair landings | Cl. 23.2.1 + Fig. 4 | 18.3 | — | 239 | 0.552 % | ≈1.35 | 27 | **PASS** |
| 7.3 | Entry stairwell flight | Cl. 23.2.1 + Fig. 4 | 22.4 | 20 | 215 | 0.470 % | ≈1.5 | 30 | **PASS** |
| 7.4 | Blast-rated elements | — | governed by strength, not deflection; blast deflection is a **support-rotation** question | — | — | — | — | — | **NOT DETERMINABLE — Phase 3 SDOF** |
| 7.5 | Crack width 0.2 mm | IS 3370 Pt 2 | satisfied by the **0.35 % surface-zone steel rule** (875 mm²/m/face required, 1 340 provided) — **not by calculation** | — | — | — | — | **REVIEW** |

## 8 — EFFECTIVE SPAN AND ANALYSIS

| # | Requirement | Clause | Application | Status |
|---|---|---|---|---|
| 8.1 | Effective span, monolithic | Cl. 22.2(a) | landings L_eff = 2 800 + 200 = 3 000 | **PASS** |
| 8.2 | Effective span of stairs | Cl. 33.1(b) | main 1 960 + 600 + 600 = 3 160; entry 3 300 + 750 + 750 = 4 800 | **PASS** |
| 8.3 | Stair step self weight | Cl. 33.2 | 0.5 × riser × 25 taken on both stairs | **PASS** |
| 8.4 | Two-way slab coefficients | Table 26 | **tabulated only to l_y/l_x = 2.0; roof aspect is 4.2, so two-way action CANNOT be claimed** — one-way adopted | **PASS** |
| 8.5 | Load transfer to supporting beams/walls | Cl. 24.5 + Fig. 7 | headhouse roof reactions to HW1–HW4 | **PASS** |
| 8.6 | Corner torsion steel | Annex D-1.8 | headhouse roof: **not required — all four edges carry full hogging steel continuous into the walls** | **PASS** |

## 9 — FOUNDATIONS

| # | Requirement | Clause | Value | Status |
|---|---|---|---|---|
| 9.1 | Bearing pressure vs capacity | IS 1904 Table 1 | service 58.4 kPa / blast 404.9 kPa vs SBC 3 240 **[ASSUMED]** = 1.8 % / 12.5 % | **REVIEW** — SBC is assumed |
| 9.2 | Mat flexure | Annex G-1.1(b) | soft-band case, 84 % | **PASS** |
| 9.3 | Mat one-way shear | Cl. 40.1, 40.4(a) | links required and provided | **PASS** |
| 9.4 | Punching | Cl. 31.6 | **NOT APPLICABLE — no column bears on the mat** | **PASS (declared)** |
| 9.5 | Footing shear | Cl. 34.2.4.1 | **NOT APPLICABLE — no isolated footing exists in the shelter** | **PASS (declared)** |
| 9.6 | Settlement | IS 12070 Cl. 6 | negligible on sound basalt **[ASSUMED]** | **REVIEW** |
| 9.7 | Flotation | *no IS clause in the register* | **FoS 0.33 at the mat-only construction stage — mandatory mitigation issued on R-101, R-102, R-805** | **REVIEW — a design output, not a pass** |
| 9.8 | Modulus of subgrade reaction | — | **k_s = 100 000 only; master A.6 / K.2-A4 require BOTH 100 000 and 500 000** | **NOT DETERMINABLE** |

## 10 — CONSTRUCTION JOINTS

| # | Requirement | Clause | Provision | Status |
|---|---|---|---|---|
| 10.1 | Construction joint location and preparation | Cl. 13.4 | ~6 m centres, roughened, cleaned, SSD; located away from openings and re-entrant corners | **PASS** |
| 10.2 | Reinforcement across a joint | Cl. 13.4 | **fully continuous — no bar stopped at a joint** | **PASS** |
| 10.3 | Water-tightness at joints | IS 3370 | two waterstops per joint | **PASS** |
| 10.4 | Movement joints | — | **none inside the protective envelope**; one only, at the expendable stairwell raft | **PASS** |

## 11 — COLUMNS AND BEAM-COLUMN JOINTS

| # | Requirement | Clause | Determination | Status |
|---|---|---|---|---|
| 11.1 | Column longitudinal steel 0.8–6 % | Cl. 26.5.3.1 | **NO RC COLUMN EXISTS IN THE UNDERGROUND SHELTER** | **NOT APPLICABLE — declared** |
| 11.2 | Column lateral ties | Cl. 26.5.3.2 | as above | **NOT APPLICABLE — declared** |
| 11.3 | Short column / slenderness | Cl. 25.1.2 | as above | **NOT APPLICABLE — declared** |
| 11.4 | Minimum eccentricity | Cl. 25.4 | as above | **NOT APPLICABLE — declared** |
| 11.5 | Axial and biaxial capacity | Cl. 39.1, 39.3, 39.6 | as above | **NOT APPLICABLE — declared** |
| 11.6 | Wall axial stress check | Cl. 32.2 (walls) | perimeter walls N = 1 168 kN/m → f = 1.95 N/mm² = 11 % of 0.4 f_ck,dyn; HH walls 822 kN/m → 12 % | **PASS** |

> The underground box is a **monolithic plate structure**. Master B.3 declares punching
> **NOT APPLICABLE** because *"no columns/pedestals bear on the mat."* Three local band members
> exist (blast-door headers ×2, headhouse door-head edge band, entry-door lintel) and are
> detailed on R-401 / R-402. **No column sheet and no beam–column joint detail is produced,
> because no such element exists.**

---

## 12 — SUMMARY

| Status | Count | Items |
|---|---|---|
| **PASS** | 60 | Material, cover, flexure, shear, minimum steel, spacing, development, laps, joints, deflection on the stairs, and the declared NOT-APPLICABLE determinations |
| **REVIEW** | 8 | 2.7 headhouse roof at 90 % · 4.13 band members against the beam clauses · 7.5 crack width by rule not calculation · 9.1 assumed SBC · 9.6 assumed settlement · 9.7 flotation mitigation · plus the two clause-not-verifiable items below |
| **NOT DETERMINABLE** | 4 | 4.12 and 5.4 (clause not in the verified register) · 7.4 blast deflection / support rotation (Phase 3) · 9.8 k_s second bound never run |

**No item has been forced to PASS.**

**The single largest limitation is not in this matrix at all:** every demand it checks against is a
**hand calculation**, because **no STAAD result exists**. A plate analysis could redistribute the
moments this matrix accepts.
