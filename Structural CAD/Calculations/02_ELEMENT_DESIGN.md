# 02 — ELEMENT-BY-ELEMENT REINFORCEMENT DESIGN
## Underground shelter · package revision **SC1** · Phase C deliverable · 4 September 2026

**Every design action below is `MANUAL CALCULATION — NOT DIRECT STAAD OUTPUT`.**
No STAAD result exists for any underground or entry-stairwell model (audit §A.3). Values are
recomputed for this package by `Scripts/rc_calc.py` and cross-checked against master Part B by
`Scripts/verify_partB.py` (212 values, 211 agree; the one difference is **C17**, §B.2 of the
design basis, and affects no bar).

**Sixteen-step format**, per the brief §8, applied to every element:
geometry · material · support · governing case · action · A_st required · minimum · maximum and
spacing · development · lap · seismic detailing · blast/underground provisions · practical
selection · provided vs required · detailing · design basis.

> **SENTRY POST — EXCLUDED.** No sentry element appears in this document.
> **MAIN STAIRCASE GEOMETRY — FROZEN.** 24 R @ 170.8333 · tread 280 · 3 flights × 8 · rise 4 100.

**Symbols:** EF = each face · EW = each way · 4L = four-legged link · B/W = both ways.

---

# PART 1 — FOUNDATIONS

## 1.1 MAT FOUNDATION — 600 thk · marks `F01`–`F09`

| | |
|---|---|
| **1 Geometry** | 600 thk, footprint 22 000 × 6 200 (external), u/s (−)6.700, top (−)6.100 = the internal floor. 100 M15 blinding beneath at (−)6.800. **There is no separate base slab** — the mat top *is* the floor |
| **2 Material** | M35 / Fe500D. Cover **75** cast against blinding, **50** top/formed |
| **3 Support** | Elastic foundation on Deccan basalt. `1 TO 310 ELASTIC MAT DIRECT Y SUBGRADE 100000` [CONFIRMED from all four `.std`]. **k_s = 100 000 kN/m³ only — the 500 000 bound required by master A.6/K.2-A4 has never been run (M-4)** |
| **4 Governing case** | **COMB 103 BLAST, soft/red-bole band.** Not bearing (12.5 % of SBC), not uplift (nominal) |
| **5 Design action** | 3.0 m band of red-bole/vesicular material removed at the worst position; q = 404.9 kPa blast bearing over a 3.0 m unsupported span. **M = qL²/12 = 404.9 × 9/12 = 303.7 kNm/m**. One-way shear V at d from the band edge = 404.9 × (1.500 − 0.517) = **398.0 kN/m** |
| | Alternative Case 1, net uplift COMB 102: u 46.11 − self 15.0 = 31.1 kPa up over 5 000 clear → M_p = 48.6 kNm/m — **nominal, does not govern** |
| **6 A_st required** | d = 600 − 75 − 8 = **517 mm**; f_ck,dyn 43.75, f_y,dyn 625 → **A_st,req = 1 115 mm²/m** |
| **7 Minimum** | IS 456 Cl. 26.5.2.1 → 0.12 % × 600 = 720 mm²/m. IS 3370 Pt 2 surface zone 0.35 % × 250 = 875 mm²/m/face |
| **8 Maximum / spacing** | **150 mm — EMP requirement**, governs over IS 456 Cl. 26.3.3. Max bar dia Cl. 26.5.2.2 D/8 = 75 ✔ |
| **9 Development** | L_d = 40 φ; T16 → **640 mm** |
| **10 Lap** | **50 φ = 800 mm**, staggered ≤ 50 % at a section |
| **11 Seismic** | IS 13920 **not applicable to the mat** — box τ = 0.063 N/mm², Cl. 10.4 boundary elements checked and not triggered (master A.7.8). See the IS 13920 matrix |
| **12 Blast / underground** | f_ck,dyn / f_y,dyn taken; **no dynamic increase on shear** (IS 4991 Cl. 10.3.1.1) — this is why the link grid exists. Flotation: **construction stage governs, FoS 0.33 at the mat-only stage** — mandatory mitigation is a design output, reproduced on R-101/R-102 |
| **13 Selected** | **`F01` T16 @ 150 BOTTOM, X direction · `F02` T16 @ 150 BOTTOM, Y · `F03` T16 @ 150 TOP, X · `F04` T16 @ 150 TOP, Y** — i.e. **T16 @ 150 EF EW = 1 340 mm²/m/face** |
| | **`F05` T12 closed links on a 250 × 250 grid throughout** — supplied A_sv/s_v = 4 × 113.1/250 = 1.810, **2.0 × the 0.908 required** |
| | **`F06` T16 @ 150 U-bars closing both curtains at every free mat edge** |
| | **`F07` T16 @ 150 EF wall starters, 900 mm horizontal leg into the mat**, lap 800 above a 150 kicker |
| | **`F08` T20 trimmers, 4 No. each face each side of the sump-pit opening**, L_d 800 beyond |
| | **`F09` T16 @ 150 EF EW to the sump pit walls (300) and base (400)** — nominal |
| **14 Provided vs required** | Flexure 1 340 > 1 115 → **M_u = 362.8 kNm/m vs 303.7 → UTILISATION 84 % — the tightest element in the box after the headhouse roof.** Shear A_sv/s_v 1.810 > 0.908 ✔. τ_v 0.770 < τ_c,max 3.70 ✔ |
| **15 Detailing** | Bottom curtain on 75 spacers off the blinding; link grid doubles as the curtain spacer system. Full continuity through all construction joints. Two waterstops + welded Cu/galv EMP strap at every joint |
| **16 Basis** | Master B.3, F.1. Recomputed ✔. **Punching (IS 456 Cl. 31.6) NOT APPLICABLE — declared, not ignored: no column or pedestal bears on the mat; the headhouse walls bear on the ROOF.** Sliding and overturning not credible mechanisms — reasoned, no spurious factor computed |

**Thickness study, reproduced:** 500 → A_st,req 1 407 = 105 % of provided **FAIL** · 600 → 1 115 = 84 % **ADOPTED** · 700 → 926 = 70 % · 800 → ≈ 57 %.

---

# PART 2 — UNDERGROUND WALLS

## 2.1 PERIMETER WALLS W1 (south), W2 (north), W3 (west), W4 (east) — 600 thk · marks `W01`–`W06`

| | |
|---|---|
| **1 Geometry** | 600 thk, clear height 3 200 ((−)6.100 to (−)2.900). W1 at Y 0–600, W2 at Y 5600–6200, W3 at X 0–600, W4 at X 21400–22000 |
| **2 Material** | M35 / Fe500D. Cover **75** (against blinding at the base) / **50** earth face / **40** internal face |
| **3 Support** | Propped top and bottom — monolithic with the 900 roof slab and the 600 mat. Idealised **fixed-fixed** vertical strip |
| **4 Governing case** | **COMB 103 BLAST.** Blast 383 kPa (K_a = 1.0, saturated) vs static earth+water 83.2 kPa at the base → **blast governs 4.6 : 1** |
| **5 Design action** | **M_p = w L_n²/16 = 383 × 3.200²/16 = 245.1 kNm/m**. V at d = 383 × (1.600 − 0.517) = **414.8 kN/m**. Axial N = 448.15 × 2.50 + 3.2 × 0.6 × 25 = **1 168 kN/m** |
| **6 A_st required** | d = 600 − 75 − 8 = **517 mm** → **894 mm²/m**. M_u,lim = 1 556 kNm/m ≫ 245.1 → singly reinforced ✔ |
| **7 Minimum** | Cl. 32.5(a) vertical 0.0012 × 600 = 720 · Cl. 32.5(b) horizontal 0.0020 × 600 = **1 200** · IS 3370 Pt 2 surface zone 875/face · Cl. 32.5(c) two curtains required (t > 200) ✔ |
| **8 Maximum / spacing** | **150 mm EMP maximum, both curtains** |
| **9 Development** | T16 L_d = **640**; T12 = 480 |
| **10 Lap** | **800 (50 φ)** staggered; starters lap 800 above a 150 kicker |
| **11 Seismic** | Per-wall seismic shear 525 kN → **τ = 0.063 N/mm², negligible**; IS 13920 Cl. 10.4 boundary elements **NOT TRIGGERED** [CONFIRMED master A.7.8] |
| **12 Blast / underground** | Dynamic strengths taken in flexure; **τ_c read at the STATIC M35 value**. Axial f = 1.95 N/mm² = 11 % of 0.4 f_ck,dyn → **P-M interaction not critical** |
| **13 Selected** | **`W01` T16 @ 150 vertical, outer face · `W02` T16 @ 150 vertical, inner face · `W03` T16 @ 150 horizontal, outer face · `W04` T16 @ 150 horizontal, inner face** = **T16 @ 150 EF EW, 1 340 mm²/m/face** |
| | **`W05` T12 closed links @ 200 c/c** (A_sv/s_v = 1.131 > 0.982 required; Cl. 26.5.1.5 limit min(0.75 d = 388, 300) = 300 ✔) |
| | **`W06` T20 @ 150 diagonal haunch bars — 500 × 500 haunch at EVERY wall–roof and wall–mat junction** |
| **14 Provided vs required** | 1 340 > 894 and > 1 200 horizontal minimum → **M_u = 362.8 kNm/m, UTILISATION 68 %**, x_u/d = 0.089 ≪ 0.46 ✔. Crack: surface steel 875 < 1 340 ✔ (IS 3370 Pt 2, 0.2 mm) |
| **15 Detailing** | Vertical bars continuous from mat starters to roof, lapped 800 staggered. Horizontal bars outside the verticals on the earth face. Closed links every 200 tie the two curtains |
| **16 Basis** | Master B.1, F.1. Recomputed ✔ |

> **Why 600 mm — stated honestly, reproduced from master B.1.** The wall is **not** strength-governed
> (68 %). 600 is set by (i) 75 mm cover, (ii) congestion — two curtains + closed links + waterstops
> + cast-in frames, (iii) IS 3370 crack control under sustained hydrostatic load, (iv) the EMP
> double curtain at 150, (v) the 1 168 kN/m axial path.

## 2.2 WALLS W6 (Bay 6/7) and W7 (Bay 7/8) — 400 thk · **MODIFICATION M1** · marks `W07`–`W12`

| | |
|---|---|
| **1 Geometry** | **W6 X 14 800–15 200, W7 X 18 000–18 400, both 400 thk**, clear height 3 200, full 6 200 width. **Post-M1 [CONFIRMED from `1_Underground_Level_Plan.dxf` and the 0.4 m shell group `1031 TO 1138` in the `.std`]** |
| **2 Material** | M35 / Fe500D. Cover **50** shaft face / **40** internal face |
| **3 Support** | Fixed top and bottom into the roof slab and the mat. The stair landings prop W6/W7 at (−)4.733 and (−)3.367 **but only over their 1 200 depth — the design does NOT rely on that prop** |
| **4 Governing case** | **COMB 103 BLAST, via `LOAD 11 BL3 BLAST IN THE STAIR SHAFT ON W6 AND W7 383 KN/M2`** [CONFIRMED, the load case M1 exists to carry] |
| **5 Design action** | **Finding F1:** the stair shaft is open to atmosphere through the 2 800 × 3 160 roof void, the headhouse and the entry stairwell. Fill time V/(A·c) = 105/(3.3 × 340) = **0.094 s vs t_d 0.13–1.33 s → the shaft equalises to full p_so.** W6/W7 sit in the **same plane as the 7-bar blast doors**, separating a pressurised shaft from Bay 6 / Bay 8 at ambient. **M_p = 383 × 3.200²/16 = 245.1 kNm/m**; V at d = 383 × (1.600 − 0.342) = **481.8 kN/m** |
| **6 A_st required** | d = 400 − 50 − 8 = **342 mm** → **1 400 mm²/m**. M_u,lim = 680.6 ≫ 245.1 ✔ |
| **7 Minimum** | Cl. 32.5(a) 480 · Cl. 32.5(b) 800 · Cl. 32.5(c) two curtains ✔ |
| **8 Maximum / spacing** | **150 EMP maximum** |
| **9 Development** | T20 L_d = **800** |
| **10 Lap** | **1 000 (50 φ)** staggered |
| **11 Seismic** | Not governing — see 2.1 item 11 |
| **12 Blast / underground** | **Why 200 mm was impossible, and it is not a detailing problem:** at 200 thk, d = 154, **M_u,lim = 0.133 × 43.75 × 1000 × 154² = 138.0 kNm/m < demand 245.1 — no steel ratio makes it work.** Two-way action was checked before rejection (3 200 × 3 800 panel, fixed 3 edges, yield line ≈ 0.7 × one-way = 172 kNm/m — still above 138). **This is the entire justification for M1** |
| **13 Selected** | **`W07`–`W10` T20 @ 150 EF EW = 2 094 mm²/m/face**; **`W11` T12 4-legged links @ 200 c/c** (Cl. 26.5.1.5 limit min(0.75 d = 257, 300) = 257 ✔); **`W12` T20 @ 150 haunch diagonals** at the roof and mat junctions |
| **14 Provided vs required** | 2 094 > 1 400 → **M_u = 355.3 kNm/m, UTILISATION 69 %**, x_u/d = 0.211 ✔. Shear: τ_v 1.409, τ_c 0.540 (pt 0.612 %), τ_c,max 3.70 ✔; V_us 297.2 → A_sv/s_v 1.998 → T12 4L at 226 → **adopted 200** ✔ |
| **15 Detailing** | Both faces identical — the wall is loaded from the shaft side but is detailed symmetrically. Continuous through the roof and mat haunches |
| **16 Basis** | Master B.2, F.1, Finding F1, M1-I3. Recomputed ✔ |

## 2.3 BLAST DOOR OPENINGS 1 200 × 2 100 in W6 and W7 · marks `W13`–`W16`, `B01`–`B03`

| | |
|---|---|
| **1 Geometry** | Two openings, **1 200 wide × 2 100 high at Y 600–1 800** [CONFIRMED from the plan DXF]. Blast Door 1 in W6 (into Bay 6), Blast Door 2 in W7 (into Bay 8). Doors proprietary, ≥ 7 bar, rebound-rated, gas-tight |
| **4 Governing case** | COMB 103 BLAST |
| **5 Design action** | **Interrupted steel** = 2 094 × 1.200 = **2 513 mm²/face → 1 256 mm² each jamb each face**. Header over the 1 200 clear opening: w = 383 × 2.100/2 = **402 kN/m**; M = wL²/12 = **48.2 kNm**; V = **241 kN**; τ = 0.578 N/mm² |
| **13 Selected** | **`W13` 4 No. T20 EACH JAMB, EACH FACE**, anchored **L_d 800 beyond the opening** in both directions |
| | **`W14` T12 closed links @ 150 to each jamb group** |
| | **`B01` header 400 × 1 100: 4-T20 TOP**, **`B02` 4-T20 BOTTOM**, **`B03` T12 4-legged links @ 150** |
| | **`W15` T16 @ 150 U-bars closing the reveal, both faces**; **`W16` cast-in steel door frame, anchored into and WELDED to the cage (EMP continuity)** |
| **14 Provided vs required** | 4-T20 = **1 257 mm² > 1 256** required ✔ (a 1 mm² margin — the arrangement is exact, not generous; recorded as such) |
| **16 Basis** | Master B.2, F.1. **No proprietary blast-door requirement is invented — vendor data is [NOT AVAILABLE] (M-7).** The frame is shown cast in and welded to the cage; the leaf, its anchorage and rebound rating are a vendor submittal |

## 2.4 WALL W5 (Bay 5/6) — 200 thk · mark `W17`

| | |
|---|---|
| **1 Geometry** | X 12 600–12 800, 200 thk, full height and width |
| **4 Governing case** | **None structural** — fire and gas-tight separation only, **no pressure differential** across it (both sides inside the envelope) |
| **5 Design action** | Nominal |
| **7 Minimum** | Cl. 32.5(a) 240 · Cl. 32.5(b) 400 |
| **13 Selected** | **`W17` T12 @ 150 EF EW = 754 mm²/m/face** |
| **14 Provided vs required** | 754 ≫ 400 → minimum governs, nominal ✔ |
| **16 Basis** | Master F.1 |

## 2.5 W8 PARTITIONS ×4 — 110 thk · mark `W18`

X 3500–3610, 5410–5520, 9020–9130, 10930–11040, each with a **900 door gap at Y 2 500–3 400**
[CONFIRMED from the plan DXF]. **NON-STRUCTURAL.** `W18` **A252 mesh both faces**.
No design action; no contribution assumed to any load path. Shown on drawings for completeness only.

---

# PART 3 — ROOF / PRESSURE SLAB — **THE GOVERNING ELEMENT**

## 3.1 PRESSURE SLAB — 900 thk · marks `S01`–`S06`

| | |
|---|---|
| **1 Geometry** | 900 thk, top (−)2.000, soffit (−)2.900, spanning the **5 000 mm internal clear width**, 22 000 long |
| **2 Material** | M35 / Fe500D. Cover **75** |
| **3 Support** | Monolithic with the 600 perimeter walls both sides; **fixed-fixed one-way strip** |
| **4 Governing case** | **COMB 103 BLAST, w = 448.15 kPa** (383 blast + 40.65 cover **[C17]** + 2.0 SIDL + 22.5 self). No live load — **IS 4991 Cl. 11.2** |
| **5 Design action** | **One-way is not a choice, it is forced:** aspect 20.8/5.0 = **4.2**, and IS 456 Table 26 is tabulated only to l_y/l_x = 2.0, so **two-way action CANNOT be claimed**. **M_p = w L_n²/16 = 448.15 × 25/16 = 700.2 kNm/m**. V at the support face = 1 120 kN/m; **V at d = 756.3 kN/m** |
| | **Natural period:** m = 3 250 kg/m²; 0.5 EI_g = 8.985e8 N·m²/m; f₁ = 74.9 Hz → **T = 13.4 ms**; t_d/T = 10–100 → **QUASI-STATIC**, which is what licenses the static analysis |
| **6 A_st required** | d = 900 − 75 − 12.5 = **812.5 mm** → **1 632 mm²/m**. M_u,lim = 3 841 ≫ 700.2 ✔ |
| **7 Minimum** | Cl. 26.5.2.1 → 0.12 % × 900 = **1 080 mm²/m** |
| **8 Maximum / spacing** | **150 EMP**; Cl. 26.5.2.2 max bar dia D/8 = 112 mm → T25 ✔ |
| **9 Development** | T25 L_d = **1 000** |
| **10 Lap** | **1 250 (50 φ)** staggered |
| **11 Seismic** | Not governing |
| **12 Blast / underground** | Dynamic strengths in flexure; **τ_c at the static M35 value**. **Direct shear** V_d,max = 0.16 f_ck,dyn b d = 5 688 kN/m vs 1 120 applied = **19.7 %** — cited to **UFC 3-340-02 §4-30 as US criteria, not as IS** |
| **13 Selected** | **`S01` T25 @ 150 BOTTOM, transverse (main, spanning the 5 000) · `S02` T25 @ 150 BOTTOM, longitudinal · `S03` T25 @ 150 TOP, transverse · `S04` T25 @ 150 TOP, longitudinal** = **T25 @ 150 EF EW = 3 272 mm²/m/face** |
| | **`S05` T12 4-legged links @ 250 in the END 1 500 each side**; **`S06` T12 2-legged links @ 300 elsewhere** |
| **14 Provided vs required** | 3 272 > 1 632 and > 1 080 → **M_u = 1 362.4 kNm/m, UTILISATION 51 %**. x_u = 113.0, **x_u/d = 0.139 ≪ 0.46** |
| | > **x/d = 0.139 IS THE PROOF THAT μ = 5 IS DEFENSIBLE** — a heavily under-reinforced section has the rotation capacity the ductility ratio assumes. |
| | Shear: τ_v 0.931, τ_c 0.450 (pt 0.403 %), τ_c,max 3.70 ✔; V_us 390.8 → A_sv/s_v 1.106 → T12 4L at 409, **but Cl. 26.5.1.5 limit 300 GOVERNS** → adopted 250 in the end zone |
| **15 Detailing** | Top steel continuous over every support and into the wall haunches, anchored L_d = 1 000. Bottom steel continuous, laps staggered at mid-span. Both curtains at 150 both ways — a welded EMP grid |
| **16 Basis** | Master B.4, F.1. Recomputed ✔ |

**Thickness study, reproduced:** 600 (d 512.5, A_st,req 2 673, τ_v 1.71 — links at 164, congested) ·
800 (1 868, 1.12 — structural optimum) · **900 (1 633, 0.93 — ADOPTED)** · 1 000 (1 453, 0.78, 11 % over).
900 was adopted for (a) reserve at the 1 400 collars, (b) headroom against a raised DBT while the
yield is **[UNRESOLVED — U3]**, (c) support rotation inside 2° without UFC lacing.

## 3.2 ESCAPE-SHAFT OPENINGS — 1 400 dia ×2 · marks `S07`–`S11`

| | |
|---|---|
| **1 Geometry** | **ESC 1 centre (2 050, 2 050); ESC 2 centre (19 900, 2 050)** [CONFIRMED — `CIRCLE r 700` + collar `r 950` in the plan DXF]. Clear 1 400 dia; collar 250 RC, OD 1 900 |
| **5 Design action** | **Interrupted steel** = 3 272 × 1.400 = **4 581 mm²/face/direction**; trimmers each side = **2 291 mm²** |
| **13 Selected** | **`S07` 5 No. T25 EACH SIDE, EACH FACE, EACH DIRECTION** (2 454 mm²), anchored **L_d = 1 000 beyond the opening** |
| | **`S08` collar 250 RC: T16 @ 150 hoops, 3 layers**; **`S09` T16 @ 150 radials** |
| | **`S10` slab thickened 900 → 1 200 over a 600 mm annulus**; **`S11` T12 closed links @ 150 in the thickening** |
| **14 Provided vs required** | 2 454 > 2 291 ✔ |
| **15 Detailing** | **Circular is the right shape: hoop action, NO re-entrant stress concentration.** This detail sets the **750 mm clearance rule** — opening edge to structural wall face ≥ 750 = 250 collar + ~400 trimmer band + 100 tolerance, so **a bay must be ≥ 2 900 wide to hold an escape shaft.** That rule is why M1 could not take 400 mm out of Bay 8 |
| **16 Basis** | Master B.4.1(a), A.4.5, F.1 |

## 3.3 STAIR VOID AND CANTILEVER PAD — **FINDING F2** · marks `S12`–`S17`

| | |
|---|---|
| **1 Geometry** | Void **X 15 200–18 000, Y 600–3 760 = 2 800 × 3 160**. Remaining **cantilever pad X 15 200–18 000, Y 3 760–5 600 = 2 800 × 1 840** |
| **4 Governing case** | COMB 103 BLAST at 448.15 kPa on a **1 840 mm cantilever** |
| **5 Design action** | **M(root) = wL²/2 = 448.15 × 1.840²/2 = 758.6 kNm/m.** |
| | > **THIS EXCEEDS THE 700.2 kNm/m MID-SPAN M_p. Finding F2 — not designed in the Phase 1 report.** |
| | V(root) = 448.15 × 1.840 = **824.6 kN/m**; τ_v 1.015 > τ_c 0.450; V_us 459.4 → A_sv/s_v 1.300 → T12 4L at 348, **Cl. 26.5.1.5 limit 300 governs** |
| **6 A_st required** | TOP steel **1 772 mm²/m** at d = 812.5 |
| **13 Selected** | **`S12` T25 @ 150 TOP continuous through the pad** (= `S03`/`S04` continued, 3 272 mm²/m) |
| | **`S13` T12 4-legged links @ 250 THROUGHOUT THE PAD** — a **new requirement** from F2 |
| | **`S14` free edge thickened 900 → 1 200 over 600, with 6-T25 TOP + 6-T25 BOTTOM** and **`S15` T12 closed links @ 150** |
| | **`S16` 6 No. T25 each face, top and bottom, in a 900 band over W6 and W7** |
| | **`S17` diagonal trimmers, 4 No. T25 each face at 45° at BOTH re-entrant corners, 2 000 long each way**, anchored L_d beyond |
| | **1 100 mm guarding to the free edge (NBC 2016 Pt 4)** — an architectural item shown for coordination |
| **14 Provided vs required** | 3 272 > 1 772 → **UTILISATION 56 %** ✔. Links 4L @ 250 > required 348 spacing ✔ |
| **15 Detailing** | **The re-entrant corners are the crack initiators** — the 45° diagonal trimmers are mandatory, not decorative. Top steel must be continuous from the pad through the band over W6/W7 into the main slab |
| **16 Basis** | Master B.4.1(b), Finding F2, F.1 |

## 3.4 BAND BENEATH HEADHOUSE WALL HW3 · mark `S18`

| | |
|---|---|
| **1 Geometry** | HW3 (west headhouse wall) runs in **Y over 5 000 and has NO wall beneath it** — it lands mid-slab in Bay 6 |
| **5 Design action** | The slab spans one-way in Y; HW3 runs **in** Y, so its load is carried by a slab strip acting as a beam. b_eff = 0.400 + 2 × 1.05 (45° spread through the 900 slab) = **2.5 m [ASSUMED — A11]** |
| | **Case 1** (two-way roof distribution, IS 456 Cl. 24.5 — correct): line load 476 + 29 self = 505 kN/m → equivalent UDL 226 kPa → **M = 354 kNm/m = 26 % of the slab's 1 362 capacity** ✔ |
| | **Case 2** (one-way bound): 793 + 29 = 822 kN/m → 353 kPa → **M = 552 kNm/m = 41 %** ✔ |
| **13 Selected** | **No slab change needed. Detailed as a LINE LOAD, not as a support.** Robustness: **`S18` 4 No. T25 ADDITIONAL TOP AND BOTTOM in a 1 200 mm band beneath HW3, lapped 1 250 (50 φ) into the main mesh** |
| **16 Basis** | Master B.7.3 |

---

# PART 4 — BEAM-TYPE ELEMENTS

> ### There are NO framed RC beams and NO RC columns in the underground shelter.
> The box is a monolithic plate structure: mat, walls, roof slab. Master B.3 declares punching
> shear **NOT APPLICABLE** precisely because *"no columns/pedestals bear on the mat."*
> **Therefore there are no beam–column joints, and no column or joint drawing is produced.**
> Brief §13 (columns), §14 (beam–column joints) and drawings R-501/R-502/R-503 are **deliberately
> not created** — see `QAQC/Reinforcement_QAQC_Report.md`. Creating them would mean inventing
> elements that do not exist.

Three **local band members** do exist and are detailed as beam-type elements on R-401 / R-402:

| Mark | Element | Size | Span | Action | Reinforcement |
|---|---|---|---|---|---|
| `B01`–`B03` | **Blast-door header ×2** (W6, W7) | 400 × 1 100 | 1 200 clear | w = 402 kN/m; **M = 48.2 kNm; V = 241 kN**; τ = 0.578 N/mm² | 4-T20 top, 4-T20 bottom, T12 4L links @ 150 |
| `H07`–`H09` | **Headhouse door-head edge band** (HW2) | 400 × 800 | 900 clear + 600 each side | w = 402 kN/m; **M = 27.1 kNm; V = 181 kN**; d = 742; τ_v = 0.610 | 4-T20 top, 4-T20 bottom, T12 4L links @ 150 |
| `E10`–`E11` | **Entry-door lintel** (stairwell headwall) | 250 × 350 | 1 000 clear | nominal | 3-T12 top, 3-T12 bottom, T8 links @ 150 |

**The headhouse door-head edge band is a geometric trap, recorded rather than hidden:** the door
head is at (−)2.000 + 2.100 = **+0.100** and the roof soffit is at **+0.400**, leaving **only 300 mm
of wall above the door — too shallow for a lintel.** The 300 wall and the 500 roof are therefore
detailed to act **together as an 800 mm deep edge band**.

**IS 13920 beam clauses (Cl. 6.1.1–6.1.3, 6.2.x, 6.3.x) — applicability:** these members are
**not** part of a lateral-force-resisting moment frame; they are local bands in a buried monolithic
box whose seismic demand is negligible (τ = 0.063 N/mm²) and whose governing action is blast.
Determination and the checks that *were* run are in `QAQC/IS13920_Compliance_Matrix.md`.

---

# PART 5 — MAIN STAIRCASE (BAY 7)

> ### GEOMETRY FROZEN — reproduced exactly, never altered.
> **24 R @ 170.8333 mm · tread 280 · 3 flights × 8 R · total rise 4 100 · flight width 1 200 ·
> well 200 · headroom 2 533.** Flight A (flights 1 and 3, stacked) X 15 300–16 500; well
> X 16 500–16 700; flight B X 16 700–17 900. Landings L1 (−)4.7333 (Y 3 760–4 960),
> L2 (−)3.3667 (Y 600–1 800), arrival (−)6.100 (Y 600–1 800). **All [CONFIRMED from the plan DXF.]**

**STATUS: INSIDE the protective envelope but NOT a blast element.** The shaft pressurises, but that
pressure acts on the shaft **walls** and the blast **doors** — not as a net load on a slab open on
both faces. **Designed to IS 456 with normal partial factors, NOT with IS 4991 dynamic strengths.**
This is stated on every stair drawing.

**NBC 2016 Part 4 geometry check:** riser 170.833 ≤ 190 ✔ · going 280 ≥ 250 ✔ · width 1 200 ≥ 1 000
✔ (stretcher-capable) · 8 risers/flight ≤ 12 ✔ · headroom 2 533 ≥ 2 200 ✔ · total rise
24 × 170.833 = 4 100 closes (−)6.100 → (−)2.000 **exactly** ✔

## 5.1 FLIGHT WAIST — 200 thk · marks `ST01`–`ST03`

| | |
|---|---|
| **1 Geometry** | Waist 200; θ = arctan(170.833/280) = **31.4°**, cos θ = 0.8535 |
| **2 Material** | M35 / Fe500D, cover **30** (stair-shaft face) |
| **3 Support** | Simply supported between landings; L_eff = going + min(landing/2, 1 000) each end (**IS 456 Cl. 33.1(b)**) = 1 960 + 600 + 600 = **3 160** |
| **4/5 Action** | waist self 5.858 + steps 2.135 (**Cl. 33.2**) + finishes 1.000 + live 5.000 (IS 875 Pt 2, plant + escape route) = 13.99 → **w_u = 21.0 kPa**; **M = w_u L_eff²/8 = 26.2 kNm/m**; V = 33.2 kN/m |
| **6/7** | d = 200 − 30 − 6 = **164**; A_st,req **380**; Cl. 26.5.2.1 min 240 |
| **13 Selected** | **`ST01` T12 @ 150 main** (754) · **`ST02` T10 @ 200 distribution** (393) · **`ST03` T12 @ 150 TOP for 0.25 L_eff = 800 into the flight**, anchored L_d 480 |
| **14** | M_u = **50.3 kNm/m → UTILISATION 52 %** ✔. **Deflection:** L/d = 19.3, basic 20, f_s = 0.58 × 500 × 380/754 = 146, p_t 0.46 % → MF ≈ 1.9 → permissible 38 ≫ 19.3 ✔. **Shear:** τ_v 0.202 < τ_c 0.479 × k 1.20 (**Cl. 40.2.1.1**, thin member) = 0.575 → **no links** ✔ |
| **16** | Master B.5, F.2 |

## 5.2 LANDINGS L1, L2 AND ARRIVAL — 200 thk · marks `ST04`–`ST06`

| | |
|---|---|
| **1/3 Geometry, support** | 200 thk, spanning **across the 2 800 shaft**; L_eff = 2 800 clear + 200 bearing (**Cl. 22.2(a)**) = **3 000** |
| **4/5 Action** | self 7.50 + finishes 1.50 + live 7.50 + **flight reaction 27.70** = **44.20 kPa**; **M = 49.7 kNm/m**; V = 66.3 kN/m |
| **6** | A_st,req **745**. **T12 @ 150 gives 754 = 100 % — TOO TIGHT** |
| **13 Selected** | **`ST04` T12 @ 125 BOTTOM** (905) · **`ST05` T12 @ 125 TOP for 900 from each support** · **`ST06` T10 @ 200 distribution** |
| **14** | M_u = 59.5 → **UTILISATION 84 %** ✔. Deflection 3 000/164 = 18.3, f_s 239, p_t 0.552 %, MF ≈ 1.35 → 27 > 18.3 ✔. Shear τ_v 0.404 < τ_c 0.519 × 1.20 = 0.622 ✔ |
| **15 Compatibility** | **The arrival landing at (−)6.100 IS the mat surface — there is no separate slab.** Flight 3 lands directly on the 900 pressure-slab pad at (−)2.000. The landings prop W6/W7 **but the 400 wall design does not rely on that prop** |
| **16** | Master B.5, F.2 |

---

# PART 6 — ENTRY (APPROACH) STAIRWELL

> **STATUS: OUTSIDE the protective boundary, NOT blast rated (Rev F drawing note 8).
> Expected to be LOST in the design event. Declared expendable.** Designed to IS 456 with normal
> partial factors. External **X 9 250–16 050 × Y 5 750–7 750**; internal **9 500–15 800 × 6 000–7 500**;
> walls 250; post-M1 (+200) [CONFIRMED].

| Element | Marks | Geometry | Action | Reinforcement | Util. |
|---|---|---|---|---|---|
| **Flight** 12 R @ 166.6667/300, waist 250, 1 500 wide, X 11 000–14 300 | `E01`–`E03` | θ 29.05°, L_eff = 3 300 + 750 + 750 = **4 800**, d = 214 | w_u **22.85 kPa**; **M = 65.8 kNm/m**; V 54.8; A_st,req 744 | **`E01` T16 @ 200 main** (1 005) · **`E02` T10 @ 200 distribution** · **`E03` T16 @ 200 TOP for 1 200 into the flight**, L_d 640 | **75 %** |
| **Side walls** 250, retained 2.9 m, propped by roof and raft | `E04` | d 194 | σ_h base **34 kPa**; M ≈ wL²/12 on an equivalent 20 kPa UDL = **14.0 kNm/m**; A_st,req 168 | **`E04` T12 @ 200 EF EW** (565/face) — **minimum steel governs** (Cl. 32.5(a) 300, (b) 500, (c) two curtains ✔) | 31 % |
| **Raking roof** 250, 1 500 clear | `E05` | d 204 | w_u **50.5 kPa** (incl. **20 kPa imposed for a stray vehicle on the berm**); M = wl²/12 = **9.5 kNm/m**; A_st,req 108, min 300 governs | **`E05` T12 @ 200 EF EW** | 20 % |
| **Top landing** 250 at 0.000, X 9 500–11 000 | `E06` | L_eff 1 750 | w_u **54.9 kPa**; **M = 21.0 kNm/m**; A_st,req 229 | **`E06` T12 @ 200 EF EW** (565) | 41 % |
| **Platform** 250 at (−)2.000, X 14 300–15 800, on fill | `E07` | 1 500 × 1 500 | nominal | **`E07` T12 @ 200 EF EW** | nominal |
| **Headwall** 250, X 9 250–9 500 | `E08` | — | nominal | **`E08` T12 @ 200 EF EW** | nominal |
| **Stepped raft** 300 on compacted fill | `E09` | — | nominal | **`E09` T12 @ 200 EF EW** | nominal |
| **Entry-door lintel** over 1 000 clear | `E10`, `E11` | 250 × 350 | nominal | **`E10` 3-T12 top + 3-T12 bottom · `E11` T8 links @ 150** | nominal |
| **Opening-corner U-bar** | `E12` | top of the flight | see below | **`E12` T16 @ 200 U-bar across the corner** | — |

## 6.1 THE OPENING CORNER — the detail most often got wrong

> At the **TOP** of the flight the tension face turns through **209°**. A bar bent round that corner
> has its bend resultant directed **OUT of the concrete**: it spalls the cover and the bar loses
> anchorage.
> **MAIN BARS SHALL NOT BE BENT ROUND IT.** Each layer is continued **straight, CROSSED, and
> anchored L_d = 640 into the OPPOSITE face**, plus a **U-bar T16 @ 200 across the corner**.
> **[SP 34:1987 Cl. 5.5 and standard detailing practice.]**
> At the **FOOT** of the flight the corner **CLOSES (151°)** — bars may turn normally.

This detail is drawn full size on **R-604** and on **R-702**.

## 6.2 Movement joint

**A movement joint is provided where the stepped raft meets the headhouse** — and **nowhere inside
the protective envelope**, because a movement joint is a guaranteed blast, gas and EMP
discontinuity (master M.17). Shown on R-702 and R-804.

## 6.3 ⚠ C16 — OPEN

**The roof/platform junction is NOT resolved.** Master A.4.7 says the roof *"over the platform
becomes the 500 headhouse roof"*; master B.6, A.7.6 and F.2 design, load and register a **250**
roof, and the headhouse footprint (Y 200–6 000) does not overlap the platform (Y 6 000–7 500).
**This package details 250** (master rule M.2 — Parts A, B, L primary — and the STAAD model is
built at 250) **and flags every affected drawing and detail: R-702, R-703, R-803, R-804.**
**The A.4.7 clause is not edited and C16 is not closed.**

---

# PART 7 — HEADHOUSE

External **X 13 600–18 400 × Y 200–6 000**; internal **14 000–18 000 × 600–5 600**; walls 400;
roof 500 (soffit +0.400, top +0.900, **no earth cover**); floor = the top of the 900 pressure slab
at (−)2.000; clear internal height 2 400. Post-M1 (+200) [CONFIRMED].

## 7.1 HEADHOUSE ROOF — 500 thk · marks `H01`–`H03` · **UTILISATION 90 %, THE TIGHTEST ELEMENT**

| | |
|---|---|
| **1/3 Geometry, support** | 500 thk, panel 4 000 × 5 000 clear, **monolithic with the 400 walls on all four sides**, l_y/l_x = 1.25 |
| **4 Governing case** | COMB 103 BLAST, **w = 396.5 kPa** = 383 + 12.5 self + 1.0 SIDL (IS 4991 Cl. 7.2 — flush at the berm crest) |
| **5 Design action** | **Three analyses run, the most conservative adopted:** |
| | 1 **One-way fixed-fixed strip, M_p = w L_n²/16 = 396.5 kNm/m** ← **ADOPTED** |
| | 2 IS 456 Table 26 Case 1, α_x⁻ = 0.045 at 1.25 → 285.5 kNm/m |
| | 3 Yield line, fixed 4 edges, isotropic → 162.2 kNm/m |
| | Yield-line validation: as b → ∞, 48/3 = 16 = the fixed-fixed strip wL²/16 ✔ (the 24-coefficient version gives 8 = simply supported wL²/8) |
| | V at d = 396.5 × (2.000 − 0.415) = **628.4 kN/m** |
| **6/7** | d = 500 − 75 − 10 = **415**; A_st,req **1 879**; M_u,lim 1 002 ✔; Cl. 26.5.2.1 min 600 |
| **13 Selected** | **`H01` T20 @ 150 EF EW** (2 094) · **`H02` T12 4-legged links @ 175 in the END 1 200 each side** · **`H03` T12 4-legged links @ 250 elsewhere** |
| **14** | M_u = 438.5 → **UTILISATION 90 % one-way / 65 % Table 26 / 37 % yield line**; x_u 72.3, x/d 0.174 ✔. **Shear — NEW AND MANDATORY, not in the Phase 1 report:** τ_v **1.514**, τ_c 0.502 (p_t 0.505 %, **read at the static M35 value — IS 4991 Cl. 10.3.1.1**), τ_c,max 3.70 ✔; V_us 420.0 → A_sv/s_v 2.327 → T12 4L at 194 → **adopted 175** ✔ |
| **15 Detailing** | **No opening in the headhouse roof** — the stair void is in the FLOOR. **Corner torsion steel (Cl. D-1.8) NOT required** — all four edges carry full T20 @ 150 hogging steel continuous into the walls. **Haunch 300 × 300 at all four wall–roof junctions, diagonal T16 @ 150** (`H06`). Top steel continuous over every support, anchored **L_d = 800** into the wall |
| **16** | Master B.7.1, F.3, conflict C2 (recomputed for the Rev F 4.0 m span and no cover). Recomputed ✔ |

## 7.2 HEADHOUSE WALLS HW1–HW4 — 400 thk · **CONFLICT C10 RESOLVED** · marks `H04`–`H06`

| | |
|---|---|
| **4 Governing case** | **COMB 103 BLAST, 383 kPa acting on EITHER FACE** |
| **5 Design action** | | CASE A (report, superseded) | **CASE B (ADOPTED)** | |
| | Lateral pressure | 113 kPa drag (C_d q = 0.4 × 282) | **383 kPa full envelope** |
| | M_p = w × 2.400²/16 | 40.7 kNm/m | **137.9 kNm/m** |
| | A_st,req | 221 | **766** |
| | V at d | 97.0 kN/m | **328.6 kN/m** |
| | τ_v | 0.283 | **0.961** |
| | Verdict | no links | **LINKS REQUIRED** |
| | **Why B:** the walls sit behind ~2.5 m of berm and **earth transmits pressure**. K_a for dry compacted fill is **[ASSUMED — A6]** and cannot be verified, so the walls take the full 383 kPa upper bound. **Cost of the upgrade: one link cage. Utilisation 17 % → 59 %.** The assumption is thereby removed from the critical path |
| **6/7** | d = 400 − 50 − 8 = **342**; M_u,lim 681 ✔; Cl. 32.5(a) min 480, **Cl. 32.5(b) min 800 — governs over the 766 required** |
| **13 Selected** | **`H04` T16 @ 150 EF EW** (1 340) · **`H05` T12 4-legged links @ 250 c/c THROUGHOUT ALL FOUR WALLS** (Cl. 26.5.1.5 limit min(0.75 d = 256, 300) = **256 governs**) · **`H06` T16 @ 150 haunch diagonals** |
| **14** | M_u 235.2 → **UTILISATION 59 %**, x/d 0.135 ✔. V_us 176.9 → A_sv/s_v 1.189 → T12 4L at 381, spacing limit 256 governs → adopted **250** ✔ |
| | **Axial:** roof reaction two-way (Cl. 24.5) HW3/HW4 trapezoid 476 kN/m, HW1/HW2 triangle 396 kN/m; one-way bound 793 kN/m; self 29 → **worst N = 822 kN/m → f = 2.06 N/mm² = 12 % of 0.4 f_ck,dyn** ✔ not critical |
| | Two-way, information only (fixed 4 edges): HW1/HW2 4 000 × 2 400 → 69.9 kNm/m; HW3/HW4 5 000 × 2 400 → 79.8 — both far below the 137.9 one-way strip adopted |
| **15 Detailing** | > **PRESSURE ACTS FROM INSIDE TOO.** The inner security door is not blast rated and the entry stairwell is expected to be lost, so the headhouse fills and the walls are pushed **OUTWARDS**. **THE WALLS ARE REINFORCED SYMMETRICALLY FOR 383 kPa EITHER WAY — a stated requirement, not an accident of detailing.** |
| **16** | Master B.7.2, F.3, conflict C10 |

## 7.3 HEADHOUSE LOAD PATH — recorded, because one wall has nothing under it

| Wall | Runs | Length | Sits over |
|---|---|---|---|
| HW1 south | X | 4 000 | Box south perimeter wall — direct ✔ |
| HW2 north | X | 4 000 | Box north perimeter wall — direct ✔ |
| **HW3 west** | Y | 5 000 | **Bay 6, mid-slab. NO WALL BELOW — line load on the pressure slab, 26 % / 41 %** — see §3.4, band `S18` |
| HW4 east | Y | 5 000 | **Wall W7 (18 000–18 400). M1 made these align exactly** ✔ |

## 7.4 INNER SECURITY DOOR 900 × 2 100 in HW2 · marks `H07`–`H09`

Opening **X 14 450–15 350**, **NOT blast rated**. Interrupted steel 1 340 × 0.900 = 1 206 mm²/face
→ **603 each jamb** → **`H07` 2 No. T20 EACH JAMB, EACH FACE** (628 mm² ✔), anchored **L_d 800 beyond**.
Head at **+0.100** vs roof soffit **+0.400** → only 300 mm of wall above the door → the
**400 × 800 edge band** `H08` **4-T20 top + 4-T20 bottom** with `H09` **T12 4L links @ 150**, over the
opening and **600 mm each side**. Door frame **cast in and WELDED to the cage (EMP)**, even though the
leaf is a security door and not blast rated.

---

# PART 8 — OPENINGS AND PENETRATIONS — COMPLETE REVIEW

Every significant opening in the in-scope structure, reviewed as required by brief §19.

| # | Opening | Location | Additional reinforcement | Status |
|---|---|---|---|---|
| 1 | **Blast Door 1** 1 200 × 2 100 | W6, Y 600–1 800 | `W13` 4-T20 each jamb each face + `B01`–`B03` header + `W15` U-bars | **DESIGNED** |
| 2 | **Blast Door 2** 1 200 × 2 100 | W7, Y 600–1 800 | as above | **DESIGNED** |
| 3 | **ESC 1** 1 400 dia | roof, (2 050, 2 050) | `S07`–`S11` | **DESIGNED** |
| 4 | **ESC 2** 1 400 dia | roof, (19 900, 2 050) | `S07`–`S11` | **DESIGNED** |
| 5 | **Stair void** 2 800 × 3 160 | roof, X 15 200–18 000 | `S12`–`S17` | **DESIGNED** (Finding F2) |
| 6 | **Inner security door** 900 × 2 100 | HW2, X 14 450–15 350 | `H07`–`H09` | **DESIGNED** |
| 7 | **Entry door** 1 000 × 2 100 | stairwell headwall | `E10`, `E11` | **DESIGNED** |
| 8 | **Sump-pit opening** | mat, Bay 5 | `F08` 4-T20 trimmers each face each side, L_d 800 | **DESIGNED** |
| 9 | **Partition door gaps ×4**, 900 wide | W8 partitions, Y 2 500–3 400 | **none required — W8 is 110 mm non-structural A252 mesh** | **N/A, declared** |
| 10 | **Blast valves ×5** | as located on sheet S-06 | **NOT DESIGNED — sizes, positions and sleeve details are on S-06 and not reproduced in Part B.** Trimming to be confirmed | **NOT DETERMINABLE — flagged** |
| 11 | **Service-entry plate**, W2 at X ≈ 11 800 | north perimeter wall | **NOT DESIGNED — plate size [NOT AVAILABLE] in Part B** | **NOT DETERMINABLE — flagged** |
| 12 | Ventilation / CBRN duct penetrations | Bay 5 plant room | **NOT DESIGNED — no penetration schedule exists in Part B** | **NOT DETERMINABLE — flagged** |

> **Items 10–12 are NOT fabricated.** Brief §19: *"Do not fabricate reinforcement where the
> structural design basis is insufficient."* A **generic trimming rule** is issued on **R-205** and
> **R-303** — *replace the interrupted steel each side of any penetration, anchored L_d beyond,
> minimum 2 bars of the parent diameter each face each side* — and each of these three items is
> listed as requiring a designed detail before construction.

---

# PART 9 — CONNECTIONS, JOINTS AND TYPICAL DETAILS

| Detail | Requirement | Ref |
|---|---|---|
| **Wall → mat** | `F07` T16 @ 150 EF starter bars with a **900 mm horizontal leg into the mat**, lap 800 (50 φ) above a 150 kicker. **500 × 500 haunch, diagonal T20 @ 150** | F.1 |
| **Wall → roof** | Wall verticals continuous into the slab, anchored L_d. **500 × 500 haunch, diagonal T20 @ 150** | F.1 |
| **W6/W7 → roof and mat** | As above with T20 haunch diagonals; top steel continuous through the `S16` band | F.1 |
| **Headhouse wall → roof** | **300 × 300 haunch, diagonal T16 @ 150**; roof top steel anchored L_d 800 into the wall | F.3 |
| **Construction joints (~6 m centres)** | **Reinforcement FULLY CONTINUOUS. Two waterstops + a welded Cu/galv EMP strap.** No reinforcement is stopped at a joint | F.1, IS 456 Cl. 13.4 |
| **Movement joints** | **NONE anywhere inside the protective envelope** — a movement joint is a guaranteed blast, gas and EMP discontinuity. One only, where the entry-stairwell raft meets the headhouse | M.17, A.4.7 |
| **Waterproofing interface** | Membrane below the mat over the blinding with a 100 protection screed; the cover build-up's screed protects the roof membrane. Waterstops at every joint. **Integral crystalline admixture** in the concrete | A.5, A.7.3 |
| **Mat free edges** | `F06` T16 @ 150 U-bars closing both curtains | F.1 |
| **Stair-void free edge** | `S14` thickened 900 → 1 200 over 600, 6-T25 top + 6-T25 bottom, `S15` T12 closed links @ 150 | B.4.1(b) |

---

# PART 10 — DESIGN SUMMARY

| Element | Thk | d | Governing action | A_st req | **A_st provided** | Links | Util. |
|---|---|---|---|---|---|---|---|
| Mat | 600 | 517 | 303.7 kNm/m | 1 115 | **T16 @ 150 EF EW = 1 340** | T12 @ 250 × 250 grid | **84 %** |
| W1–W4 | 600 | 517 | 245.1 kNm/m | 894 (min 1 200 horiz) | **T16 @ 150 EF EW = 1 340** | T12 closed @ 200 | 68 % |
| W5 | 200 | 154 | nominal | min 400 | **T12 @ 150 EF EW = 754** | — | nominal |
| **W6 / W7** | **400** | 342 | 245.1 kNm/m | 1 400 | **T20 @ 150 EF EW = 2 094** | T12 4L @ 200 | 69 % |
| W8 ×4 | 110 | — | none | — | **A252 mesh both faces** | — | n/s |
| **Roof slab** | **900** | 812.5 | **700.2 kNm/m** | 1 632 | **T25 @ 150 EF EW = 3 272** | T12 4L @ 250 end 1500 / 2L @ 300 mid | 51 % |
| Roof pad (cantilever) | 900 | 812.5 | **758.6 kNm/m** | 1 772 | **T25 @ 150 top continuous** | T12 4L @ 250 throughout | 56 % |
| **HH roof** | **500** | 415 | 396.5 kNm/m | 1 879 | **T20 @ 150 EF EW = 2 094** | T12 4L @ 175 end 1200 / @ 250 | **90 %** |
| HH walls | 400 | 342 | 137.9 kNm/m | 766 (min 800 horiz) | **T16 @ 150 EF EW = 1 340** | T12 4L @ 250 | 59 % |
| Main stair flight | 200 | 164 | 26.2 kNm/m | 380 | **T12 @ 150 = 754** | none required | 52 % |
| Main stair landings | 200 | 164 | 49.7 kNm/m | 745 | **T12 @ 125 = 905** | none required | **84 %** |
| Entry stairwell flight | 250 | 214 | 65.8 kNm/m | 744 | **T16 @ 200 = 1 005** | none required | 75 % |
| Entry stairwell walls/roof/landings | 250 | 194–214 | 9.5–21.0 kNm/m | min governs | **T12 @ 200 EF EW = 565** | none | 20–41 % |
| Sump pit | 300/400 | 244 | nominal | — | **T16 @ 150 EF EW** | — | nominal |

**Every provided arrangement equals or exceeds the required steel, the code minimum and the
150 mm EMP spacing rule. No arrangement in this package differs from a calculation.**

**Phase C is complete. Proceeding to Phase D — detailing and schedules.**
