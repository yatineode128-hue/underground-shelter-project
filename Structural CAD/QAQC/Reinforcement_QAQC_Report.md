# REINFORCEMENT QA/QC REPORT
## Structural CAD reinforcement package · revision **SC1** · 4 September 2026

**Scope: the underground shelter only. The sentry post is excluded from this package entirely.**

**Status key — nothing is forced:**
**PASS** — checked and satisfied from information actually held ·
**REVIEW** — satisfied, but a qualified structural engineer must look at it before construction ·
**NOT DETERMINABLE** — cannot be decided from the information held, and is not guessed.

---

## 0 — THE THREE FACTS THAT FRAME EVERY ROW BELOW

1. **NO STAAD RESULT EXISTS.** A scan of `current/staad/` for `*.anl`, `*.out`, `*.txt`, `*.rea`
   returns nothing, and master D.3.5 states it explicitly. **Every design action in this package
   is `MANUAL CALCULATION — NOT DIRECT STAAD OUTPUT`.** The five `.std` files supply the geometry,
   thicknesses, material, supports, load register and combination register — the *definition* of
   the demand, not its magnitude.
2. **NO CODE DOCUMENT EXISTS IN THE WORKSPACE.** Clause numbers are cited only from the verified
   register in master Part G. Anything else is reported **CLAUSE NOT VERIFIABLE**.
3. **BLAST CAPACITY IS NOT DEMONSTRATED.** Support rotation / ductility (μ = 5) needs a
   non-linear SDOF check — **Phase 3**. A quasi-static analysis gives *demand*. It is not, and is
   nowhere presented as, proof of blast resistance.

**Independent verification performed for this package:** all 212 master Part B values used here
were recomputed from first principles (`Scripts/verify_partB.py`). **211 agree; 1 differs** — and
that difference is raised as new conflict **C17**, not resolved away.

---

## 1 — ELEMENT-BY-ELEMENT QA/QC

### 1.1 MAT FOUNDATION — 600 thk

| Item | Record |
|---|---|
| **Geometry** | 600 thk, 22 000 × 6 200 footprint, u/s (−)6.700, top (−)6.100 = the internal floor. 100 M15 blinding to (−)6.800. **No separate base slab exists.** |
| **Design basis** | Master B.3, recomputed. Elastic foundation on Deccan basalt, `ELASTIC MAT DIRECT Y SUBGRADE 100000` |
| **Governing load case** | **COMB 103 BLAST, soft/red-bole band** — not bearing (12.5 % of SBC), not uplift (nominal) |
| **Design action** | 3.0 m band removed at the worst position, q = 404.9 kPa → **M = qL²/12 = 303.7 kNm/m**; V at d = **398.0 kN/m** |
| **A_st required** | 1 115 mm²/m (d = 517, f_ck,dyn 43.75, f_y,dyn 625) |
| **A_st provided** | **T16 @ 150 EF EW = 1 340 mm²/m/face** (`F01`–`F04`) |
| **Minimum** | IS 456 Cl. 26.5.2.1 → 720; IS 3370 Pt 2 surface zone → 875/face. Both satisfied |
| **Max / spacing** | 150 EMP cap; Cl. 26.5.2.2 D/8 = 75 ≥ T16 |
| **Anchorage** | L_d 640 (T16); wall starters `F07` 900 leg + 800 lap above a 150 kicker |
| **Lap / splice** | 800 (50 φ) staggered ≤ 50 % at a section; long runs split into 2 pieces of 11 350 |
| **IS 456** | Flexure ✔ · one-way shear ✔ (links `F05` 1.810 vs 0.908 required) · punching **NOT APPLICABLE, declared** · minimum steel ✔ · cover ✔ |
| **IS 13920** | **NOT APPLICABLE** — no frame member; Cl. 10.4 not triggered |
| **Utilisation** | **84 % — the second tightest element in the package** |
| **STATUS** | **PASS** — with **REVIEW** flags: k_s second bound never run (**NOT DETERMINABLE**); SBC and GWT are **[ASSUMED]**; flotation FoS 0.33 at the mat-only stage requires the mandatory mitigation on R-101 |

### 1.2 PERIMETER WALLS W1–W4 — 600 thk

| Item | Record |
|---|---|
| **Geometry** | 600 thk, clear height 3 200, total run 54 000 |
| **Support** | Propped by the mat and the pressure slab; idealised fixed-fixed vertical strip |
| **Governing load case** | **COMB 103 BLAST** — 383 kPa vs 83.2 kPa static earth+water → **blast governs 4.6 : 1** |
| **Design action** | **M_p = wL_n²/16 = 245.1 kNm/m**; V at d = 414.8 kN/m; N = 1 168 kN/m |
| **A_st required** | 894 mm²/m |
| **A_st provided** | **T16 @ 150 EF EW = 1 340** (`W01`–`W04`), links **T12 closed @ 200** (`W05`) |
| **Minimum** | Cl. 32.5(a) 720 · **Cl. 32.5(b) 1 200 — GOVERNS** · Cl. 32.5(c) two curtains ✔ · IS 3370 875/face ✔ |
| **Max / spacing** | 150 EMP; link spacing limit min(0.75 d = 388, 300) = 300, provided 200 |
| **Anchorage / lap** | L_d 640; lap 800 staggered; verticals carried 825 into the 900 slab |
| **IS 456** | Flexure 68 % ✔ · shear ✔ · axial f = 1.95 = 11 % of 0.4 f_ck,dyn ✔ · crack (surface steel) ✔ |
| **IS 13920** | Cl. 10.4 **checked, not triggered** (τ_seismic = 0.063 N/mm²) |
| **STATUS** | **PASS** |

### 1.3 WALLS W6 / W7 — 400 thk (MODIFICATION M1)

| Item | Record |
|---|---|
| **Geometry** | W6 X 14 800–15 200; W7 X 18 000–18 400; both 400 thk, 5 000 long, 3 200 clear. **Post-M1 — confirmed from the plan DXF and the 0.4 m shell group in the `.std`** |
| **Governing load case** | **COMB 103 BLAST via LOAD 11 `BL3 BLAST IN THE STAIR SHAFT ON W6 AND W7 383 KN/M2`** |
| **Design action** | **Finding F1** — the shaft fills in 0.094 s vs t_d 0.13–1.33 s, so it **equalises to full p_so**. **M_p = 245.1 kNm/m**; V at d = **481.8 kN/m** |
| **Why 200 was impossible** | At 200 thk, M_u,lim = **138.0** < demand 245.1. **No steel ratio works.** Two-way action checked before rejection (yield line ≈ 172, still above 138) |
| **A_st required / provided** | 1 400 → **T20 @ 150 EF EW = 2 094** (`W07`–`W10`); links **T12 4L @ 200** (`W11`) |
| **Minimum** | Cl. 32.5(a) 480, Cl. 32.5(b) 800 — both far exceeded |
| **Anchorage / lap** | L_d 800; lap 1 000 staggered; starters `F08` 900 leg + 1 000 lap |
| **IS 456** | Flexure 69 %, x/d 0.211 ✔ · shear (limit 257 governs, provided 200) ✔ |
| **IS 13920** | Cl. 10.4 not triggered |
| **STATUS** | **PASS** |

### 1.4 BLAST-DOOR OPENINGS AND HEADERS

| Item | Record |
|---|---|
| **Geometry** | 2 No. 1 200 × 2 100 at Y 600–1 800, in W6 and W7 |
| **Design action** | Interrupted steel 2 094 × 1.2 = 2 513 mm²/face → **1 256 per jamb**. Header w 402 kN/m, M 48.2 kNm, V 241 kN, τ 0.578 |
| **Provided** | `W13` **4-T20 each jamb each face = 1 257 mm²**; `W14` jamb links; `W15` reveal U-bars; `B01`/`B02` header 4-T20 T+B; `B03` T12 4L @ 150 |
| **Provided vs required** | **1 257 vs 1 256 — the arrangement is EXACT, not generous. Recorded as such.** |
| **Anchorage** | L_d 800 beyond the opening in both directions |
| **STATUS** | **PASS** on the RC. **NOT DETERMINABLE** on the door, frame section, anchor spacing and rebound rating — **vendor data [NOT AVAILABLE]**. No proprietary requirement is invented |

### 1.5 PRESSURE (ROOF) SLAB — 900 thk — **THE GOVERNING ELEMENT**

| Item | Record |
|---|---|
| **Geometry** | 900 thk, top (−)2.000, soffit (−)2.900, spanning the **5 000 internal clear width**, 22 000 long |
| **Design basis** | One-way is **forced, not chosen**: aspect 4.2, and Table 26 is tabulated only to 2.0 |
| **Governing load case** | **COMB 103 BLAST, w = 448.15 kPa**; no live load (IS 4991 Cl. 11.2); blast governs static 3.51 : 1 |
| **Design action** | **M_p = 700.2 kNm/m**; V at support face 1 120, at d **756.3 kN/m**; T = 13.4 ms → quasi-static |
| **A_st required / provided** | 1 632 → **T25 @ 150 EF EW = 3 272** (`S01`–`S04`) |
| **Minimum** | Cl. 26.5.2.1 → 1 080 ✔; Cl. 26.5.2.2 max bar D/8 = 112 ≥ 25 ✔ |
| **Links** | `S05` T12 4L @ 250 in the end 1 500 each side; `S06` T12 2L @ 300 mid. **Cl. 26.5.1.5 limit 300 governs the 409 the shear would allow** |
| **Anchorage / lap** | L_d 1 000; lap 1 250 staggered; long runs in 2 pieces |
| **IS 456** | Flexure 51 %, **x_u/d = 0.139** ✔ · shear ✔ · minimum ✔ · spacing ✔ |
| **Direct shear** | 0.16 f_ck,dyn b d = 5 688 kN/m vs 1 120 = 19.7 % — **cited to UFC 3-340-02 §4-30 as US criteria, not as IS** |
| **STATUS** | **PASS** — with **C17** flagged (cover load 40.65 held vs a 39.15 column sum; **no bar changes**) |

### 1.6 ROOF OPENINGS — ESCAPE SHAFTS, STAIR VOID, CANTILEVER PAD

| Item | Record |
|---|---|
| **ESC 1 / ESC 2** | 1 400 dia at (2 050, 2 050) and (**19 900**, 2 050) — **confirmed from the plan DXF**. Interrupted steel 4 581 mm²/face/direction; trimmers 2 291 required, **5-T25 = 2 454 provided** (`S08`), L_d 1 000 beyond. Collar 250 RC, hoops `S09`, radials `S10`, thickening 900→1 200 with links `S11`. **PASS** |
| **750 mm clearance rule** | Opening edge to wall face ≥ 750 → a bay must be ≥ 2 900 wide. **Satisfied; this is why M1 could not shorten Bay 8.** **PASS** |
| **Stair void 2 800 × 3 160** | Leaves an **1 840 cantilever**: **M(root) = 758.6 kNm/m — EXCEEDS the 700.2 mid-span M_p (Finding F2)**. A_st,req top 1 772 < 3 272 provided → **56 %**. V(root) 824.6 → `S07` T12 4L @ 250 **throughout the pad** (a new requirement). **PASS** |
| **Free edge / bands / corners** | `S12` thickening 900→1 200 with 6-T25 T+B, `S13` links @ 150; `S14` 6-T25 each face T+B in a 900 band over W6/W7; `S15` 4-T25 each face at 45° at **both** re-entrant corners. **PASS** |
| **HW3 band** | `S16` 4-T25 T+B in a 1 200 band, lapped 1 250. Slab strip check 26 % (two-way) / 41 % (one-way bound). **PASS**, with b_eff = 2.5 m **[ASSUMED — A11]** |

### 1.7 HEADHOUSE ROOF — 500 thk — **UTILISATION 90 %**

| Item | Record |
|---|---|
| **Geometry** | 500 thk, panel 4 000 × 5 000 clear, monolithic with the 400 walls on four sides, no earth cover |
| **Governing load case** | **COMB 103 BLAST, w = 396.5 kPa** |
| **Design action** | Three analyses run; **the most conservative adopted**: one-way strip **396.5 kNm/m** (vs Table 26 285.5, yield line 162.2). V at d **628.4 kN/m** |
| **A_st required / provided** | 1 879 → **T20 @ 150 EF EW = 2 094** (`H01A`–`H01D`) |
| **Links** | `H02` T12 4L @ 175 end 1 200 each side; `H03` @ 250 elsewhere. **Shear is NEW AND MANDATORY — it was not in the Phase 1 report (conflict C2)** |
| **IS 456** | Flexure **90 %**, x/d 0.174 ✔ · shear ✔ · minimum 600 ✔ · corner torsion (Annex D-1.8) **not required — all four edges carry full hogging steel** ✔ |
| **STATUS** | **REVIEW** — the tightest element in the package. 90 % on the adopted one-way basis leaves little reserve, and the element already moved once (C2) when the geometry changed under a carried-forward calculation |

### 1.8 HEADHOUSE WALLS HW1–HW4 — 400 thk

| Item | Record |
|---|---|
| **Governing load case** | **COMB 103 BLAST, 383 kPa acting on EITHER FACE** (conflict C10 resolved to the upper bound) |
| **Design action** | M_p **137.9 kNm/m**; V at d 328.6 kN/m; worst axial N = 822 kN/m → 12 % of 0.4 f_ck,dyn |
| **A_st required / provided** | 766 → **T16 @ 150 EF EW = 1 340** (`H04A`, `H04B`); **Cl. 32.5(b) minimum 800 still governs the requirement** |
| **Links** | `H05` T12 4L @ 250 throughout all four walls; **Cl. 26.5.1.5 limit 256 governs** |
| **Why the upper bound** | The berm transmits pressure and K_a for dry compacted fill is **[ASSUMED — A6]**. Designing to 383 kPa costs **one link cage** and **removes the assumption from the critical path**. Utilisation 17 % → 59 % |
| **Symmetry** | **Reinforced symmetrically for 383 kPa either way — a stated requirement.** The security door is not blast rated and the stairwell is expendable, so the headhouse fills and the walls are pushed outwards |
| **HW3** | Has **no wall beneath it** — detailed as a line load on the slab, not as a support (§1.6) |
| **STATUS** | **PASS** |

### 1.9 MAIN STAIRCASE — **GEOMETRY FROZEN**

| Item | Record |
|---|---|
| **Geometry** | **24 R @ 170.8333 · tread 280 · 3 flights × 8 · rise 4 100 · width 1 200 · well 200 · waist 200 · headroom 2 533.** Re-extracted from the plan DXF and **confirmed unchanged** |
| **Status** | **Inside the protective envelope but NOT a blast element.** Designed to IS 456 with normal partial factors, **not** with IS 4991 dynamic strengths |
| **Flight** | w_u 21.0 kPa; L_eff 3 160 (Cl. 33.1(b)); M 26.2 kNm/m; A_st,req 380 → **T12 @ 150 = 754**, **52 %**. Deflection L/d 19.3 vs 38 permissible ✔. Shear τ_v 0.202 < 0.575 → no links ✔ |
| **Landings** | w 44.20 kPa; L_eff 3 000 (Cl. 22.2(a)); M 49.7 kNm/m; A_st,req 745. **T12 @ 150 would give 754 = 100 % — too tight.** **T12 @ 125 = 905 adopted, 84 %.** Deflection ✔, shear ✔ |
| **NBC 2016 Pt 4** | riser ✔ · going ✔ · width ✔ · risers/flight ✔ · headroom ✔ · total rise closes exactly ✔ |
| **STATUS** | **PASS.** Geometry confirmed unchanged |

### 1.10 ENTRY (APPROACH) STAIRWELL

| Item | Record |
|---|---|
| **Status** | **OUTSIDE the protective boundary, NOT blast rated, DECLARED EXPENDABLE.** IS 456, normal factors |
| **Flight** | 12 R @ 166.6667/300, waist 250; w_u 22.85 kPa; L_eff 4 800; M 65.8 kNm/m; A_st,req 744 → **T16 @ 200 = 1 005, 75 %**. Deflection ✔, shear ✔ |
| **Side walls / roof / landings / platform / headwall / raft** | **Minimum steel governs everywhere** — T12 @ 200 EF EW; utilisations 20–41 % |
| **Opening corner** | **The detail most often got wrong.** At the top of the flight the tension face turns through 209°; a bar bent round it spalls the cover and loses anchorage. **Main bars are NOT bent round it** — continued straight, crossed, anchored L_d 640 into the opposite face, plus a U-bar `E12`. **SP 34 Cl. 5.5.** **PASS** |
| **Movement joint** | One only, at the raft/headhouse interface — **outside the protective envelope** |
| **STATUS** | **PASS**, with **C16 OPEN** — see §3 |

### 1.11 BEAM-TYPE ELEMENTS · COLUMNS · BEAM–COLUMN JOINTS

| Item | Record |
|---|---|
| **Framed beams** | **DO NOT EXIST** in the underground shelter |
| **RC columns** | **DO NOT EXIST.** Master B.3 declares punching NOT APPLICABLE because no column or pedestal bears on the mat |
| **Beam–column joints** | **DO NOT EXIST** — no beam, no column |
| **What does exist** | Three local bands: blast-door headers ×2 (`B01`–`B03`), headhouse door-head edge band (`H08`, `H09`), entry-door lintel (`E10`, `E11`) — detailed on R-401/R-402 |
| **Drawings** | **No R-501 / R-502 / R-503 and no joint detail are produced.** Drawing an element that does not exist would be fabrication |
| **STATUS** | **PASS — determination declared with evidence, not an omission** |

---

## 2 — PACKAGE-LEVEL QA/QC

| # | Check | Method | Result | Status |
|---|---|---|---|---|
| 2.1 | Master Part B recomputed independently | `verify_partB.py`, 212 values | 211 agree, 1 differs (**C17**) | **PASS** |
| 2.2 | IS 456 Table 19 τ_c column corroborated | 8 independent master values reproduced to ≤ 0.1 % | agrees | **PASS** |
| 2.3 | Geometry re-extracted from the primary DXF | `ezdxf` parse of `1_Underground_Level_Plan.dxf` | **all 14 controlling coordinates agree with master A.3/A.4** | **PASS** |
| 2.4 | Load register cross-checked against the `.std` | parse of all 4 underground models + the stairwell model | 11 primary loads and 5 combinations match verbatim | **PASS** |
| 2.5 | Every bar mark on a drawing has exactly one schedule entry | `qa_crosscheck.py` reads the DXFs back | **0 orphans** | **PASS** |
| 2.6 | No duplicate bar marks | assertion in `rebar_data.build_marks()` | **92 unique** | **PASS** |
| 2.7 | Every scheduled mark is drawn somewhere | `qa_crosscheck.py` | **all 92 + 1 fabric carry a balloon** | **PASS** |
| 2.8 | Every drawing cross-reference resolves | `qa_crosscheck.py` | **0 broken** | **PASS** |
| 2.9 | DXF structural validation, 30 files | `validate_dxf.py` | **0 errors, 0 review items** | **PASS** |
| 2.10 | Native editable entities present | validator entity census | LINE, LWPOLYLINE, ARC, CIRCLE, TEXT, MTEXT, **DIMENSION**, **LEADER**, **HATCH**, **INSERT** | **PASS** |
| 2.11 | Units, layers, extents | validator | mm, S-* layers declared, **all geometry inside 0..841 × 0..594** | **PASS** |
| 2.12 | Zero-length / degenerate geometry | validator | **none** | **PASS** |
| 2.13 | Unintended duplicate geometry | validator | **none** | **PASS** |
| 2.14 | Dimensions read model millimetres | `dimlfac` set to the view scale on every dimension | verified on R-101 | **PASS** |
| 2.15 | Title block completeness | every sheet | project, title, number, scale, date, revision, status, designed/checked/approved (**placeholders — no name is invented**), sheet number | **PASS** |
| 2.16 | Main staircase unchanged | re-extraction + comparison | **24R @ 170.8333 / 280, 3 × 8, rise 4 100, landings, 1 200 widths, 200 well — CONFIRMED UNCHANGED** | **PASS** |
| 2.17 | Sentry post excluded | grep of every deliverable | **no sentry design, detail, drawing, schedule, quantity or folder** | **PASS** |

---

## 3 — OPEN ITEMS. NONE OF THESE IS CLOSED BY THIS PACKAGE

| Ref | Item | Effect on this package | Status |
|---|---|---|---|
| **C16** | **Roof / platform junction.** A.4.7 says the roof over the platform becomes the 500 headhouse roof; B.6 / A.7.6 / F.2 design, load and register **250**, and the headhouse footprint does not overlap the platform | **Detailed at 250** (master rule M.2; the STAAD model is built at 250). **Flagged on R-603, R-702, R-703, R-803, R-804.** The A.4.7 clause is **not edited** | **UNRESOLVED — user ruling required** |
| **C17** | **NEW, raised by this package.** Master A.7.3 states the engineered cover as **40.65 kPa**; its own column sums to **39.15 kPa** — a 1.50 kPa difference | **40.65 HELD** (larger, and the value in Part A, Part L and every `.std`). At 39.15 the roof total is 446.65, M_p 697.9, utilisation 51.2 % vs 51.4 %. **NO BAR CHANGES.** Flagged on R-001, R-301, R-302 | **UNRESOLVED — user ruling required** |
| **C18** | **NEW, raised by this package.** Sump pit: master F.1 gives walls 300 / base 400, and the levels ((−)7.600 invert to (−)8.000 base) support **400**; the text on sheet S-06 says **300** for both | **400 held.** Flagged on R-101, R-102 | **UNRESOLVED — user ruling required** |
| **M-1** | **No STAAD result of any kind** | Every design action is a hand calculation | **NOT DETERMINABLE** |
| **M-2** | **No code document** | Clause citation restricted to master Part G | **NOT DETERMINABLE** |
| **M-3** | **IS 2502 named in the brief, not held, not in Part G** | Bar bending uses declared project rule **PBR-1** instead | **NOT DETERMINABLE** |
| **M-4 / A4** | **k_s second bound (500 000) never run** | Mat moment distribution not bounded on the stiff side | **NOT DETERMINABLE** |
| **M-5** | **No `.rvt` Revit model** — only 6 Dynamo scripts | Model-consistency check done against the scripts | **REVIEW** |
| **M-6** | **DXF toolchain for S-01…S-08 absent** | Those sheets are **not regenerated and not fabricated**; a new R-series is issued instead | **declared** |
| **M-7** | **Blast-door vendor data** | Frame shown cast in and welded only | **NOT DETERMINABLE** |
| **M-8 / P3** | **Non-linear SDOF support rotation** | **Blast capacity not demonstrated** | **NOT DETERMINABLE — Phase 3** |
| **A2** | **Design GWT (−)2.000 [ASSUMED]** | Two-thirds of the lateral load and all of the uplift | **REVIEW — monsoon monitoring required** |
| **U2 / U3** | Direct-hit requirement; DBT yield | Cover depth and burster design | **UNRESOLVED — client / military sign-off** |
| **Openings 10–12** | Blast valves ×5, service-entry plate, CBRN duct penetrations | **No structural basis exists. NOT fabricated.** A generic trimming rule is issued on R-003 D2 and each item is listed as requiring a designed detail | **NOT DETERMINABLE** |

---

## 4 — DECLARED DEVIATIONS FROM THE EXISTING PROJECT STANDARD

| # | Item | Master standard | This package | Why |
|---|---|---|---|---|
| **X1** | Output DXF format | E.3.1: **AutoCAD R12 ASCII** | **AutoCAD 2010 (AC1024) ASCII** | R12 does not carry usable DIMENSION / MTEXT / HATCH / LEADER entities, which the brief §25 requires. **S-06 and the ten input drawings are untouched** |
| **X2** | Layer naming | E.3.2: 22-layer table (`CONC`, `REINF-MAIN`, …) | brief §26 **`S-*`** system | Required by the brief. **A one-to-one mapping table is issued** in `Documentation/02_CAD_STANDARDS.md` and printed on **R-002**, so the two sets remain reconcilable |
| **X4** | Bar bending standard | Part G names BS 8666 + SP 34 | **project rule PBR-1** | Neither document is in the workspace, and IS 2502 is not held either. Only the four unambiguous BS 8666 shape codes (00, 11, 21, 51) are used; everything else is coded **99 — dimensioned sketch** |
| **X5** | Title-block size | E.3.1: 180 × 62 | **180 × 100**, same position | The brief §31 requires more fields than 62 mm can hold legibly |

---

## 5 — ITEMS REQUIRING REVIEW BY A QUALIFIED STRUCTURAL ENGINEER

**Before any drawing in this package is treated as construction-ready.**

| # | Item |
|---|---|
| **R-1** | **Every design action is a hand calculation. No STAAD result exists.** The section forces are closed-form idealisations (fixed-fixed strip, cantilever, soft band). A plate analysis may redistribute them |
| **R-2** | **Blast capacity is not demonstrated.** Support rotation / ductility needs the Phase 3 non-linear SDOF check |
| **R-3** | **C16 is open** and affects R-603, R-702, R-703, R-803, R-804 |
| **R-4** | **Clause numbers could not be verified at source** — no code document is held |
| **R-5** | **Mat k_s sensitivity not demonstrated** — the 500 000 bound has never been run |
| **R-6** | **Headhouse roof 90 % and mat 84 %** — the two tightest elements. Little reserve |
| **R-7** | **Flotation FoS 0.33 at the mat-only stage.** Dewatering, relief plugs, programme and symmetrical backfill are **mandatory design outputs** |
| **R-8** | **Bar bending is to project rule PBR-1, not to IS 2502 or BS 8666 Table 3.** Quantities are for tender and estimating and must be re-measured on the approved schedule |
| **R-9** | **Congestion** at the roof/wall haunch, the ESC collars and the void free edge has been checked geometrically for bar fit but **not physically mocked up** |
| **R-10** | **Blast-door leaf, frame and anchorage** are vendor items and are not designed here |
| **R-11** | **Crack width to IS 3370 Pt 2 is satisfied by the surface-zone steel rule, not by calculation** |
| **R-12** | **C17 and C18** are new conflicts raised by this package and are not resolved |
| **R-13** | **Blast valves, the service-entry plate and CBRN duct penetrations have no designed detail.** The generic rule on R-003 D2 is not a substitute |

---

## 6 — WHAT THIS PACKAGE DOES AND DOES NOT CLAIM

**It does claim:**
* A complete, internally consistent reinforcement design and detailing package for every in-scope
  element, traceable to master Parts A, B and F and **independently recomputed**.
* 30 genuine, editable, validated DXF sheets whose bar marks reconcile exactly with the schedules.
* 92 bar marks, 70.46 tonnes, every quantity derived from stated geometry.

**It does NOT claim:**
* **"Fully code compliant."** Twelve items are REVIEW and eleven are NOT DETERMINABLE, and no code
  document was available against which to verify a single clause number.
* **"Construction ready."** Section 5 lists thirteen items requiring engineering review, three
  unresolved conflicts and a missing Phase 3 analysis.
* **Any STAAD result.** There are none.
