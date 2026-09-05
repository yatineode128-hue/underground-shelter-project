# 00 — INPUT AUDIT
## Structural reinforcement design + CAD package, underground shelter
### Phase A deliverable · package revision **SC1** · 4 September 2026

**Scope of this package:** the **underground shelter only** — main box, mat, perimeter and
internal walls, pressure (roof) slab, main staircase, entry stairwell, headhouse, entrance
and all significant openings.

> ### ⛔ SENTRY POST — EXCLUDED
> The sentry post is **completely out of scope** for this package by instruction. No sentry-post
> design, detail, drawing, schedule, quantity or DXF is produced. `Structural CAD/DXF/Sentry_Post/`
> is **deliberately not created**. `Sentry_Post_Framed_Seismic.std`, `3_Sentry_Post_Ground_Floor_Plan.dxf`,
> `4_Sentry_Post_First_Floor_Plan.dxf` and `6_Sentry_Post_Framing_Plan.dxf` were opened **only** to
> confirm that they contain nothing the in-scope structures depend on. They do not: the sentry post is
> a physically separate building ≥ 10 m clear of the shelter excavation (master A.2, A.4.8).
> Master sections B.8 and F.4 (sentry design and reinforcement) were **not used**.

Evidence tags follow the master legend: **[CONFIRMED] · [RECONSTRUCTED] · [ASSUMED] ·
[UNRESOLVED] · [NOT AVAILABLE]**. Two additional package tags are used where the brief requires them:
**"STAAD RESULT REQUIRED"** and **"MANUAL CALCULATION — NOT DIRECT STAAD OUTPUT"**.

---

## A.1 Files inspected

Every file below was **parsed programmatically**, not read from a summary
(`Structural CAD/Scripts/audit_inputs.py`, read-only).

### A.1.1 Authority documents

| File | Used for | Class |
|---|---|---|
| `CLAUDE.md` | Operating rules, frozen items, evidence discipline | [CONFIRMED] |
| `master/MASTER_PROJECT_STATE.md` (2 110 lines) | **THE AUTHORITY.** Parts A, B, C, D, E, F, G, H, K, L read in full for this package | [CONFIRMED] |
| `master/QUICK_STATE.md` | Orientation digest only — **never** relied on for a value | orientation |
| `master/MASTER_PROJECT_STATE.pdf` | **Not used.** Master H.4 records it as a stale render of the pre-reconciliation `.md` | superseded |

### A.1.2 Architectural / civil input DXF set — Rev F (`current/cad/`)

All ten input drawings parsed. Layers in every input file: `0, BEYOND, CENTRE, DIM, GROUND,
HIDDEN, OPENINGS, STAIRS, TEXT, WALLS`. Units millimetres. Entities LINE / POLYLINE+VERTEX+SEQEND /
CIRCLE / ARC / TEXT (R12-era, no LWPOLYLINE, no MTEXT, no DIMENSION entities).

| File | Entities | Used in this package for |
|---|---|---|
| `1_Underground_Level_Plan.dxf` | 24 PL, 97 L, 9 A, 12 C, 51 T | **PRIMARY plan geometry** — box, bays, internal walls, escape shafts, stair shaft |
| `1_Staircase_Section.dxf` | 21 PL, 60 L, 43 T | Main staircase section geometry (**FROZEN** — read only) |
| `2_Side_Section_with_Stairs.dxf` | 42 PL, 88 L, 8 C, 64 T | Longitudinal section, levels |
| `2_Ground_Plan_Headhouse_Berm.dxf` | 20 PL, 115 L, 5 C, 2 A, 64 T | Headhouse and covered stairwell plan, berm |
| `3_Headhouse_Section_Cutaway.dxf` | 17 PL, 57 L, 35 T | Headhouse section at Z = 2800 |
| `5_Entry_Headhouse_Stair_Section.dxf` | 11 PL, 61 L, 1 C, 83 T | Entry stairwell Section C-C, 12R @ 166.667/300 |
| `5_Front_Elevation.dxf` | 25 PL, 81 L, 40 T | Levels only (sentry levels ignored) |
| `06_Underground_Plan_Services_Sump_BlastValves.dxf` | 587 L, 13 C, 295 T | **Output sheet S-06** — the only existing output sheet; used as the precedent for sheet size, title block and the 22-layer output standard |
| `3_Sentry_Post_Ground_Floor_Plan.dxf` · `4_Sentry_Post_First_Floor_Plan.dxf` · `6_Sentry_Post_Framing_Plan.dxf` | — | **EXCLUDED — sentry post. Opened only to confirm no in-scope dependency.** |

### A.1.3 STAAD models (`current/staad/`) — five `.std` in scope, one excluded

| File | Lines | Joints | Shells | Material | Analysis command | In scope |
|---|---|---|---|---|---|---|
| `Underground_Structure_WITH_LOADS_worked_example (4).STD` | 952 | 760 | **1 138** | M35, E 2.95804e7 kN/m² | `PERFORM ANALYSIS PRINT STATICS CHECK` | **YES — primary** |
| `Underground_Shelter_Mesh_Medium.std` | 968 | 760 | 1 138 | M35 | same | YES (mesh study MS1) |
| `Underground_Shelter_Mesh_Coarse.std` | 402 | 223 | 336 | M35 | same | YES (mesh study MS1) |
| `Underground_Shelter_Mesh_Fine.std` | 3 942 | 3 754 | 4 552 | M35 | same | YES (mesh study MS1) |
| `Entry_Stairwell.std` | 208 | 25 | — (frame) | M35, E 29 580 398 kN/m² | same | **YES** |
| `Sentry_Post_Framed_Seismic.std` | 261 | 21 | — | M30 | same | **NO — sentry post, excluded** |

**Underground model, verified by parse [CONFIRMED]:**

```
Shell thickness groups   1 TO 270    0.6 m   mat
                         271 TO 508  0.9 m   pressure (roof) slab
                         509 TO 976  0.6 m   perimeter walls
                         977 TO 1030 0.2 m   internal wall W5
                         1031 TO 1138 0.4 m  internal walls W6 / W7   <- MOD M1
Supports                 1 TO 310 ELASTIC MAT DIRECT Y SUBGRADE 100000
                         + 4 corner joints FIXED BUT FY MX MY MZ with KFY restated (C15)
Geometry                 MID-SURFACE.  Model Y = 0 is the UNDERSIDE of the mat.
                         Project level = model Y − 6.700
Primary load cases       11   (1-11, see A.4 below)
Load combinations        5    (101, 102, 103 BLAST, 104, 105)
Concrete design block    DESIGN ELEMENT 509 TO 688 869 TO 922   (walls only)
```

**Entry stairwell model, verified by parse [CONFIRMED]:** M35 (conflict C11 resolved),
5 primary load cases (DL+earth over roof; **LL 20 kPa on the berm** — C12 resolved; earth at rest
both walls; surcharge 10 kPa; earth one side — backfilling), 5 combinations (101–104, 201),
elastic vertical springs `FIXED BUT FX MZ KFY 29167 / 14583` on the raft joints.

---

## A.2 Geometry source

**Source of record: master Part A.4, cross-checked against the Rev F input DXFs.**
Every controlling coordinate below was **independently re-extracted from
`1_Underground_Level_Plan.dxf`** for this audit and **agrees with the master exactly**. [CONFIRMED]

| Item | Master A.3 / A.4 | Extracted from the DXF | Agree |
|---|---|---|---|
| Box external | 0 – 22 000 × 0 – 6 200 | X 0, 22 000 ; Y 0, 6 200 | ✔ |
| Box internal | 600 – 21 400 × 600 – 5 600 | X 600, 21 400 ; Y 600, 5 600 | ✔ |
| W8 partitions ×4 | 3500/3610, 5410/5520, 9020/9130, 10930/11040 | identical | ✔ |
| W5 200 thk | 12 600 – 12 800 | 12 600, 12 800 | ✔ |
| **W6 400 thk (M1)** | **14 800 – 15 200** | 14 800, 15 200 | ✔ |
| **W7 400 thk (M1)** | **18 000 – 18 400** | 18 000, 18 400 | ✔ |
| Flight A / well / flight B | 15300–16500 / 16500–16700 / 16700–17900 | identical | ✔ |
| Landing L1 | Y 3 760 – 4 960 | 3 760, 4 960 | ✔ |
| L2 / arrival landing | Y 600 – 1 800 | 600, 1 800 | ✔ |
| Store under L1 | Y 4 960 – 5 600 | 4 960, 5 600 | ✔ |
| Blast door openings | Y 600 – 1 800 in W6 and W7 | 600, 1 800 | ✔ |
| Partition door gaps | Y 2 500 – 3 400 | 2 500, 3 400 | ✔ |
| **ESC 1** | centre (2 050, 2 050), 1400 dia, collar OD 1900 | `CIRCLE (2050,2050) r 700` + `r 950` | ✔ |
| **ESC 2 (M1)** | centre (**19 900**, 2 050) | `CIRCLE (19900,2050) r 700` + `r 950` | ✔ |

Levels are taken from master A.4.3 and the sections; thicknesses from A.4.2 and confirmed against
the STAAD shell-thickness groups above.

**FROZEN GEOMETRY — reproduced, never altered:** main staircase 24 R @ **170.8333** mm riser,
**280** mm tread, **3 flights × 8**, total rise **4 100**, flight width 1 200, well 200,
headroom 2 533, landings L1 (−)4.7333 / L2 (−)3.3667 / arrival (−)6.100.

---

## A.3 Analysis source — **THE CENTRAL LIMITATION OF THIS PACKAGE**

> ### ⚠ NO STAAD RESULTS EXIST ANYWHERE IN THE WORKSPACE.
> A directory scan for `*.anl`, `*.out`, `*.txt`, `*.rea` in `current/staad/` returns **nothing**.
> There is **no** plate moment output, **no** support reaction table, **no** deflection, **no**
> design ratio and **no** analysis log for any underground model. Master **D.3.5** states this
> explicitly: *"No post-processing screenshot for the underground model was provided… Every
> underground design value in Part B was produced by hand calculation, not by STAAD output."*
> **STAAD.Pro is not available in this environment and no analysis was run for this package.**

**Consequence, applied throughout this package without exception:**

1. Every design action (moment, shear, axial) used to size reinforcement is labelled
   **"MANUAL CALCULATION — NOT DIRECT STAAD OUTPUT"**.
2. Nowhere in this package is any number presented as a STAAD result.
3. Where a plate-level or envelope result would refine or replace a hand value, the item is
   tagged **"STAAD RESULT REQUIRED"** and listed in `QAQC/Reinforcement_QAQC_Report.md`.

**What the STAAD models legitimately contribute** [CONFIRMED]: the geometry, thicknesses,
material, support idealisation, the **load register** and the **combination register** — all read
from the files. They establish the *demand definition*, not the demand *magnitude*.

**Governing analysis method actually used for every in-scope element:** closed-form hand
calculation from master Part B, **independently recomputed for this package** in
`Structural CAD/Scripts/rc_calc.py` (see `Calculations/`).

---

## A.4 Loading source

Master A.7, cross-checked line by line against the load-case titles in the underground `.std`. [CONFIRMED]

| # | STAAD title (verbatim from the file) | Value | Master ref |
|---|---|---|---|
| 1 | `DL1 SELF WEIGHT` | 25 kN/m³ | A.7.2 |
| 2 | `DL2 EARTH COVER ON ROOF 40.65 KN/M2` | 40.65 kPa | A.7.3 |
| 3 | `DL3 SIDL SERVICES AND FINISHES` | 2.0 kPa roof / 1.0 mat | A.7.2 |
| 4 | `LL1 LIVE LOAD ON INTERNAL FLOOR 5.0 KN/M2` | 5.0 kPa | A.7.2 |
| 5 | `DL4 STAIRCASE ON THE TWO SHAFT WALLS` | 2.947 kPa | A.7.2 |
| 6 | `EP1 EARTH + WATER ON EXTERNAL WALLS` | 33.9 → 83.2 kPa (15.41 kPa/m) | A.7.2 |
| 7 | `HY1 HYDROSTATIC UPLIFT ON MAT 46.1 KN/M2` | 46.11 kPa | A.7.2 |
| 8 | `BL1 BLAST ON ROOF 383 KN/M2` | 383 kPa | A.7.1 |
| 9 | `BL2 BLAST ON EXTERNAL WALLS 383 KN/M2` | 383 kPa | A.7.1 |
| 10 | `LL2 CONSTRUCTION SURCHARGE 20.0 KN/M2` | 20 kPa | A.7.2 |
| 11 | `BL3 BLAST IN THE STAIR SHAFT ON W6 AND W7 383 KN/M2` | 383 kPa | B.2 / Finding F1 / M1-I3 |

**Combinations [CONFIRMED from the file]:** 101 ULS static · 102 ULS uplift · **103 BLAST
(γ = 1.0)** · 104 SLS crack width · 105 construction.
**COMB 103 governs every blast-rated element.**

Non-blast elements (main staircase, entry stairwell) are loaded per master A.7.6 / B.5 / B.6 with
normal IS 456 partial factors — **not** with IS 4991 dynamic strengths.

---

## A.5 Material source

Master A.5, cross-checked against the `.std` material blocks. [CONFIRMED]

| Property | Value | Cross-check |
|---|---|---|
| Concrete, **all in-scope structures** | **M35** | `ISOTROPIC M35`, both underground and entry stairwell models ✔ |
| E_c | **29 580 N/mm²** (= 2.95804e7 kN/m²) | `E 2.95804e+07` / `E 29580398` ✔ |
| Reinforcement | **Fe500D** to IS 1786:2008 | master A.5 |
| Poisson's ratio | 0.20 | [ASSUMED — standard] |
| γ_m concrete / steel | 1.5 / 1.15 | IS 456 Cl. 36.4.2 |
| Blinding | M15, 100 thk | master A.5 |
| Burster slab (in the cover, not a package element) | M30, 200 thk | master A.7.3 |
| **Blast case only** | f_ck,dyn 43.75 · f_y,dyn **625** · **no dynamic increase on shear** | IS 4991 Cl. 10.3.1 / 10.3.1.1 |

**Cover** (master A.5): 75 cast against blinding/rock · 50 formed earth face · 40 internal ·
30 stair-shaft faces. The 5 mm reduction IS 456 Table 16 permits for M35 is **deliberately not taken**.

**Development / lap (M35, Fe500D):** L_d tension = **40 φ**, L_d compression = 32 φ,
**lap = 50 φ staggered** so ≤ 50 % spliced at any section.
The IS 4991 Cl. 10.3.1.1 +25 % blast bond allowance (→ 32 φ) is **not taken**.

**Bar spacing:** **150 mm maximum, both curtains — an EMP requirement**, stricter than IS 456
Cl. 26.3.3. This governs spacing over every code minimum in the blast-rated envelope.

---

## A.6 Design-code source — **A MATERIAL LIMITATION, STATED PLAINLY**

> ### ⚠ NO IS CODE DOCUMENT IS PRESENT IN THE WORKSPACE.
> The brief says *"use the actual code documents supplied with the project"* and *"where a code
> document is available, verify the actual clause before citing it."* **No code document — IS 456,
> IS 13920, IS 1786, IS 2502, IS 4991, IS 3370, SP 34, BS 8666 or any other — exists in this
> workspace.** A full-tree file listing returns only markdown, PDF (the stale master render),
> DXF, STD and Python files.

**Rule adopted for this package, and applied without exception:**

* A clause number is cited **only if it appears in master Part G**, which states:
  *"No clause number in this register was invented. Where a clause could not be confirmed from the
  material available it is not listed."* Part G is therefore the **only verified clause register**
  available, and it is treated as the authority for clause numbering.
* Any check that would need a clause **not** in Part G is reported as
  **"CLAUSE NOT VERIFIABLE — code document not in workspace"** and given status
  **NOT DETERMINABLE**. It is never given a guessed clause number.

**Clauses available for citation (master Part G, verbatim scope):**

| Code | Clauses in the verified register |
|---|---|
| **IS 456:2000** | 6.2.3.1; 13.4; 22.2(a); 23.2.1 + Fig. 4; 24.4, 24.5 + Fig. 7; 25.1.2; 25.4; 26.2.1, 26.2.1.1, 26.2.5.1; 26.3.3; 26.4.2, 26.4.2.1, 26.4.2.2 + Table 16; 26.5.1.1, 26.5.1.2, 26.5.1.5, 26.5.1.6; 26.5.2.1, 26.5.2.2; 26.5.3.1, 26.5.3.2; 31.6, 31.6.1, 31.6.3.1; 32.2, 32.5(a)(b)(c); 33.1(b), 33.2; 34.2.4.1; 36.4.2; 38.1, 38.1(c), 38.1(f); 39.1, 39.3, 39.6; 40.1, 40.2.1.1, 40.2.3, 40.4(a); Tables 3, 5, 16, 18, 19, 20, 26, 27, 28; Annex D; Annex G-1.1(b), G-1.1(c) |
| **IS 13920:2016** | 6.1.1, 6.1.2, 6.1.3; 6.2.1(b), 6.2.2, 6.2.3, 6.2.4; 6.3.3, 6.3.4, 6.3.5.1, 6.3.5.2; 7.1, 7.2.1, 7.3, 7.4; 8.1, 8.2; **10.4** |
| **IS 4991:1968** | **1.1 (excludes nuclear)**; 6.2.1; 7.2 + Table 3; 7.4; 10.3.1; **10.3.1.1**; 10.3.3; 11.1; 11.2; Fig. 6 |
| **IS 3370 (1,2):2021** | 0.2 mm crack limit; 0.35 % surface-zone steel over a 250 mm zone |
| **IS 1786:2008** | Fe500D grade |
| **IS 875 (1,2,3,5)** · **IS 1893 (1):2016** · **IS 1904** · **IS 2950(1)** · **IS 12070** | as listed in Part G |
| **SP 34:1987** | shape codes; **Cl. 5.5 (opening-corner detailing)** |
| **SP 16:1980** · **BS 8666** · **NBC 2016 Pt 4** · **UFC 3-340-02 §4-27, §4-30** | as listed in Part G |

**IS 2502 (bar bending schedules) is named in the brief but does NOT appear in master Part G and
no copy is in the workspace.** It is therefore **not cited** in this package. Bar bending and cut
lengths use a **declared project rule (PBR-1)** instead — see §A.10 and `Schedules/`.

**IS 13920 applicability — determined, not assumed.** IS 13920 is the ductile-detailing standard
for RC structures resisting seismic force. The in-scope structure is a buried RC box with **no
beams, no columns and no beam–column joints**. Master A.7.8 records box A_h = 0.075,
V_b = 1 050 kN, wall shear **τ = 0.063 N/mm² — negligible**, and **IS 13920 Cl. 10.4 boundary
elements checked and NOT triggered**. Governing action for every blast-rated element is
**COMB 103 blast at 383 kPa**, not seismic — blast governs the roof 3.51 : 1 and the walls 4.6 : 1.
Full member-by-member determination is in `QAQC/IS13920_Compliance_Matrix.md`.

---

## A.7 Existing reinforcement information

Master **Part F** is a complete reinforcement register for the in-scope structures and **Part B**
carries the calculation behind every line of it. This package **verifies and details** that
design; it does not replace it.

| Element | Master F register | Part B basis | Util. |
|---|---|---|---|
| W1–W4 perimeter, 600 | T16 @ 150 EF EW + T12 closed links @ 200 | B.1 | 68 % |
| W5, 200 | T12 @ 150 EF EW | F.1 (nominal) | — |
| **W6 / W7, 400 (M1)** | **T20 @ 150 EF EW + T12 4L @ 200** | B.2 | 69 % |
| W8 partitions, 110 | A252 mesh both faces | F.1 | non-structural |
| **Mat, 600** | **T16 @ 150 EF EW + T12 @ 250×250 link grid** | B.3 | **84 %** |
| **Roof, 900** | **T25 @ 150 EF EW** + T12 4L @ 250 end 1500 / 2L @ 300 mid | B.4 | 51 % |
| Roof cantilever pad | T25 @ 150 top continuous + T12 4L @ 250 throughout | B.4.1(b) | 56 % |
| Main stair flight / landings | T12 @ 150 / T12 @ 125 | B.5 | 52 % / 84 % |
| Entry stairwell flight | T16 @ 200 | B.6 | 75 % |
| **Headhouse roof, 500** | **T20 @ 150 EF EW** + T12 4L @ 175 / 250 | B.7.1 | **90 %** |
| Headhouse walls, 400 | T16 @ 150 EF EW + T12 4L @ 250 | B.7.2 | 59 % |
| Sump pit walls / base | T16 @ 150 EF EW | F.1 | nominal |

Plus the additional-bar register in F.1 (starters, haunches, jambs, headers, collars, void edge
and bands, HW3 band, construction joints) and F.2 (stairs, opening-corner U-bar).

**No reinforcement drawing exists for any of it.** Master E.3.3 registers eight output sheets
S-01…S-08, of which **only S-06 (services/drainage) is present in the workspace**; S-01…S-05,
S-07 and S-08 and their generator toolchain (`proj.py`, `dxflib.py`, `d01_wall.py`…`d08_sentryslab.py`)
are absent and, per `CLAUDE.md`, **must not be fabricated**. **This package therefore creates a new,
separately numbered R-series drawing set. It does not attempt to regenerate S-01…S-08.**

---

## A.8 In-scope structural element inventory

Prepared for this package. **"EXISTS" is a statement of fact about the design, not a wish list —
elements marked DOES NOT EXIST get no drawing, no schedule and no quantity.**

### Foundations

| Element | Status | Size | Ref |
|---|---|---|---|
| Mat / raft foundation | **EXISTS** | 600 thk, 22 000 × 6 200 footprint | A.4.2, B.3 |
| Base slab (internal floor) | **EXISTS — IS the mat top surface at (−)6.100.** No separate slab | — | B.5 note |
| Blinding / PCC | **EXISTS** | 100 thk M15 at (−)6.800 | A.4.2 |
| Sump pit | **EXISTS** | walls 300 / base 400, invert (−)7.600, base (−)8.000 | A.4.3, F.1 |
| Wall starter bars | **EXISTS** | T16 @ 150 EF, 900 leg into mat | F.1 |
| Isolated footings | **DOES NOT EXIST** in the shelter | — | — |
| Foundation beams | **DOES NOT EXIST** | — | — |
| Pedestals | **DOES NOT EXIST** | — | — |
| Pile caps | **DOES NOT EXIST** | — | — |
| Entry stairwell stepped raft | **EXISTS** (outside protective boundary) | 300 thk on compacted fill | A.4.7, B.6 |

### Underground box

| Element | Status | Size | Ref |
|---|---|---|---|
| W1 south perimeter | **EXISTS** | 600, blast-rated | B.1 |
| W2 north perimeter | **EXISTS** | 600, blast-rated | B.1 |
| W3 west end | **EXISTS** | 600, blast-rated | B.1 |
| W4 east end | **EXISTS** | 600, blast-rated | B.1 |
| W5 Bay 5/6 | **EXISTS** | 200, gas/fire only, no pressure differential | F.1 |
| **W6 Bay 6/7** | **EXISTS** | **400 (M1), protective boundary, Blast Door 1** | B.2 |
| **W7 Bay 7/8** | **EXISTS** | **400 (M1), protective boundary, Blast Door 2** | B.2 |
| W8 partitions ×4 | **EXISTS** | 110, non-structural, A252 mesh | F.1 |
| Pressure (roof) slab | **EXISTS** | 900, **the governing element** | B.4 |
| Roof cantilever pad | **EXISTS** | 900, 1 840 cantilever over the stair void | B.4.1(b) |
| RC beams in the box | **DOES NOT EXIST** — the box has no framed beams | — | — |
| RC columns in the box | **DOES NOT EXIST** — no column bears on the mat (B.3 declares punching NOT APPLICABLE) | — | — |
| Beam–column joints | **DOES NOT EXIST** — no beams and no columns | — | — |

> **Beam-type elements that DO exist** are local band members, not framed beams:
> blast-door header 400 × 1100 (×2, in W6 and W7), headhouse door-head edge band 400 × 800,
> entry-stairwell door lintel 250 × 350. These are detailed on R-401 / R-402.

### Entrance / headhouse

| Element | Status | Size | Ref |
|---|---|---|---|
| Headhouse walls HW1–HW4 | **EXISTS** | 400, blast-rated **either face** (C10) | B.7.2 |
| Headhouse roof | **EXISTS** | 500, 396.5 kPa, **90 % utilised** | B.7.1 |
| Headhouse floor | **EXISTS — IS the top of the 900 pressure slab** at (−)2.000 | — | A.4.6 |
| Headhouse foundation | **DOES NOT EXIST as a separate element** — HW1/HW2 bear on the box perimeter walls, HW4 on W7, **HW3 bears on the pressure slab as a line load** | — | A.4.6, B.7.3 |
| Headhouse beams / columns | **DOES NOT EXIST** | — | — |
| Covered entry stairwell walls | **EXISTS** | 250, **outside the protective boundary, expendable** | B.6 |
| Entry stairwell raking roof | **EXISTS** | 250 | B.6 |
| Entry stairwell top landing / platform / headwall | **EXISTS** | 250 each | B.6 |

### Stairs

| Element | Status | Ref |
|---|---|---|
| Main staircase flights ×3 | **EXISTS — GEOMETRY FROZEN**, waist 200 | B.5 |
| Main stair landings L1, L2, arrival | **EXISTS**, 200 (arrival = mat surface) | B.5 |
| Stairwell walls (Bay 7) | = W6, W7 and the perimeter walls — no separate element | B.5 |
| Entry stairwell flight | **EXISTS**, 12 R @ 166.6667/300, waist 250 | B.6 |

### Openings and penetrations

| Opening | Status | Size | Ref |
|---|---|---|---|
| Blast Door 1 (W6) | **EXISTS** | 1 200 × 2 100, 7 bar, Y 600–1800 | B.2 |
| Blast Door 2 (W7) | **EXISTS** | 1 200 × 2 100, Y 600–1800 | B.2 |
| Inner security door (HW2) | **EXISTS** | 900 × 2 100 at X 14450–15350, **not blast rated** | B.7.2 |
| Entry door (stairwell headwall) | **EXISTS** | 1 000 × 2 100 at grade | B.6 |
| ESC 1 roof opening + collar | **EXISTS** | 1 400 dia, collar 250 RC OD 1900, at (2050, 2050) | B.4.1(a) |
| ESC 2 roof opening + collar | **EXISTS** | 1 400 dia, at (**19 900**, 2 050) | B.4.1(a) |
| Stair void in the roof slab | **EXISTS** | 2 800 × 3 160, X 15200–18000, Y 600–3760 | B.4.1(b) |
| Partition door gaps ×4 | **EXISTS** | 900 wide, Y 2500–3400, in 110 partitions | A.3 |
| Sump pit opening in the mat | **EXISTS** | 4-T20 trimmers each face each side | F.1 |
| Blast valves ×5 | **EXISTS** as service penetrations | shown on S-06 | E.3.3 |
| Service-entry plate | **EXISTS**, north wall W2 at X ≈ 11 800 | H.3 |

---

## A.9 Missing information

| # | Missing | Consequence for this package | Action |
|---|---|---|---|
| **M-1** | **All STAAD output** — no plate moments, reactions, deflections, design ratios, for any underground or stairwell model | **Every design action is a hand calculation.** No result in this package is a STAAD output | Run the models; label every affected item **STAAD RESULT REQUIRED** |
| **M-2** | **All IS code documents** | No clause can be verified at source. Clause numbers restricted to master Part G; anything else is **NOT DETERMINABLE** | Supply IS 456, IS 13920, IS 1786, IS 2502, IS 4991, IS 3370, SP 34, BS 8666 |
| **M-3** | **IS 2502** (named in the brief, absent from Part G and the workspace) | Bar bending schedules cannot be certified to IS 2502. Project rule **PBR-1** used and declared instead | Supply IS 2502 |
| **M-4** | **Second k_s bound (500 000 kN/m³)** — master A.6/K.2-A4 require **both** bounds; only 100 000 exists in every `.std` | Mat moment distribution is unbounded on the stiff side. Mat steel is from the B.3 soft-band hand case, which does not depend on k_s — but the k_s sensitivity is **not demonstrated** | Run the mat at 500 000 |
| **M-5** | **`.rvt` Revit model** — only 6 Dynamo Python scripts exist, no model file | The Revit leg of the §35 model-consistency cross-check is done **against the scripts**, not against a built model | Build and supply the `.rvt` |
| **M-6** | **DXF generator toolchain** for S-01…S-08 (`proj.py`, `dxflib.py`, `d01_wall.py`…, `validate.py`, `render.py`) | S-01…S-05, S-07, S-08 **cannot be regenerated and are not fabricated**. A new independent R-series set is produced instead | Supply the toolchain if the S-series is to be reissued |
| **M-7** | **Blast-door vendor data** — leaf, frame anchorage, rebound rating | Door-frame interface is drawn as a **cast-in frame anchored and welded to the cage** only. No proprietary anchorage is invented | Vendor submittal |
| **M-8** | **Non-linear SDOF support-rotation check** (master C.1) | Blast **capacity** is not demonstrated — only demand and section capacity to IS 456 | Phase 3 |
| **M-9** | **Site investigation** — GWT, rockhead, SBC, k_s, K₀, percolation | All soil/water inputs remain **[ASSUMED]** | Site investigation |
| **M-10** | Crack-width **calculation** to IS 3370 Pt 2 (only the surface-zone steel rule is applied) | SLS crack width reported as **NOT DETERMINABLE** for elements where it is not computed in Part B | Compute, or supply IS 3370 |

---

## A.10 Conflicting information

| # | Conflict | Value A | Value B | Held by this package |
|---|---|---|---|---|
| **C16** | **Roof / platform junction — OPEN, master H.4** | A.4.7: *"over the platform it becomes the 500 headhouse roof"* | B.6 / A.7.6 / F.2 design, load and register a **250** roof; the headhouse footprint (Y 200–6000) does not overlap the platform (Y 6000–7500) | **NOT RESOLVED.** Detailing follows **250** (B/A/L primary, rule M.2, and the STAAD model is built at 250) and **every affected drawing and detail carries a C16 OPEN flag.** The A.4.7 clause is not edited |
| **C9 / U1** | Sentry base shear | STAAD 73.18 kN | hand 59.3 kN | **NOT APPLICABLE — sentry post excluded from this package** |
| **NEW — X1** | **Output DXF format standard** | Master E.3.1: **AutoCAD R12 ASCII** | The brief §25 requires native **DIMENSION**, **MTEXT**, **HATCH**, **LEADER** and **BLOCK** entities, which R12 ASCII does not carry usefully | **Declared deviation.** The R-series is written as **AutoCAD 2010 (AC1024) ASCII DXF**. Recorded in `Documentation/` and in `QAQC/Reinforcement_QAQC_Report.md`. **S-06 and the input set are untouched** |
| **NEW — X2** | **Layer naming** | Master E.3.2: 22-layer table (`CONC`, `REINF-MAIN`, …) used by S-01…S-08 | Brief §26 requires `S-CONCRETE`, `S-REBAR-MAIN`, … | **Declared deviation.** The R-series uses the brief's **`S-*`** system; a full **one-to-one mapping table to the master's 22 layers** is issued in `Documentation/02_CAD_STANDARDS.md` so the two sets remain reconcilable |
| **NEW — X3** | Sentry combination count | Master A.7.9 records **15** | `Sentry_Post_Framed_Seismic.std` has **16** (adds 203) | **NOT APPLICABLE — sentry post excluded.** Recorded here only so the audit is complete; master H.4 already records it |
| **NEW — X4** | Bar bending standard | Brief §4 names **IS 2502** | Master Part G names **BS 8666** + **SP 34** | Neither document is in the workspace. **Project rule PBR-1** declared; BS 8666 shape codes used **only** for the four shapes that are unambiguous (00, 11, 21, 51), everything else coded **99 — dimensioned sketch** |

**No conflict above has been silently resolved.** C16 remains open by instruction.

---

## A.11 Assumptions carried into this package

All are inherited from master K.2 and are **[ASSUMED]** — none is upgraded here.

| # | Assumption | Why it matters to reinforcement |
|---|---|---|
| A2 | **GWT (−)2.000** | Water is ⅔ of the 15.41 kPa/m lateral gradient and all of the 46.11 kPa uplift → wall and mat steel |
| A4 | **k_s 100 000–500 000 kN/m³** — only the lower bound modelled | Mat moment distribution |
| A1, A3, A5 | Rockhead 1.5–2.0 m; SBC 3 240 kPa; K₀ 0.50, γ 20/21 | Bearing (≪ 13 % used), wall lateral load |
| A6 | K_a = 1.0 saturated **used**; K_a ≈ 0.5 dry berm **not relied on** | Headhouse walls designed to the 383 kPa upper bound (C10) |
| A11 | b_eff = 2.5 m for the HW3 line load | HW3 band steel (4-T25 top and bottom in a 1 200 band) |
| A14 | Poisson's ratio 0.20 | Plate behaviour, minor |

**Package-specific assumptions declared here (new, tagged [ASSUMED] and listed in the QA/QC report):**

| # | Assumption | Basis |
|---|---|---|
| **P-1** | **Stock bar length 12 000 mm.** Bars longer than this are scheduled in lengths ≤ 12 000 with `ceil(L/12000) − 1` laps of 50 φ added, staggered | Indian market convention. **No code source in the workspace** |
| **P-2** | **PBR-1 cut-length rule:** cut length = Σ scheduled leg dimensions, **no bend deduction taken**; links add 2 × 10 φ for 135° hooks | Conservative by ≈ 2 φ per 90° bend. BS 8666 Table 3 deductions to be applied by the fabricator on the approved BBS |
| **P-3** | Bar mark prefixes **F / W / S / B / ST / H / E / T**; **C is reserved and unused** because no column exists | Brief §22 |
| **P-4** | Where master Part F gives an arrangement but not an extent, the extent is taken as the full element between the faces of its supports, plus anchorage L_d | Standard detailing practice |

---

## A.12 Items requiring engineering review

To be reviewed by a qualified structural engineer **before any drawing in this package is treated
as construction-ready.**

| # | Item | Why |
|---|---|---|
| **R-1** | **Every design action in this package is a hand calculation. No STAAD result exists.** | Section forces are closed-form idealisations (fixed-fixed strip, cantilever, soft-band). A plate analysis may redistribute them |
| **R-2** | **Blast capacity is not demonstrated** — support rotation / ductility (μ = 5) needs the non-linear SDOF check (IS 4991 Fig. 6 / Biggs). **Phase 3** | Master C.1. A static run gives demand, never proof of blast resistance |
| **R-3** | **C16 roof/platform junction is OPEN.** Affected: R-702, R-703 and the R-803 wall/slab connection family | Master H.4 — needs the user's ruling |
| **R-4** | **Clause numbers could not be verified at source** — no code document in the workspace | Every citation traces to master Part G only |
| **R-5** | **Mat k_s sensitivity not demonstrated** — second bound (500 000) never run | Master K.2-A4 requires both |
| **R-6** | **Headhouse roof at 90 % and mat at 84 % utilisation** — the two tightest elements | Little reserve; any load or geometry change re-opens them |
| **R-7** | **Flotation FoS = 0.33 at the mat-only construction stage.** Dewatering, pressure-relief plugs, programme and symmetrical backfill are **mandatory design outputs**, reproduced on R-101/R-102 | Master B.3 |
| **R-8** | **Bar bending schedule is to project rule PBR-1, not to IS 2502 or BS 8666 Table 3** | No standard in the workspace |
| **R-9** | **Congestion at the roof/wall haunch, the ESC collars and the void free edge** has been checked geometrically for bar fit but **not physically mocked up** | Two curtains of T25 @ 150 + 4-leg links + waterstops + cast-in frames |
| **R-10** | **Blast-door and frame anchorage** is shown as a cast-in frame welded to the cage only — no vendor data | Master M-7 above |
| **R-11** | **Crack width to IS 3370 Pt 2 is satisfied by the surface-zone steel rule, not by calculation** | 0.2 mm limit not computed |

---

## A.13 Phase A conclusion

The input set is **sufficient to produce a fully traceable reinforcement design and detailing
package**, because master Parts A, B and F carry a complete, internally consistent, hand-calculated
design for every in-scope element, and the geometry behind it has been re-verified against the
Rev F DXFs and the STAAD models in this audit.

The input set is **not sufficient to certify the package as construction-ready**, for the reasons
in §A.9 and §A.12 — principally the **total absence of STAAD results** and of **any code document**.

**Phase A is complete. Proceeding to Phase B — design basis.**
