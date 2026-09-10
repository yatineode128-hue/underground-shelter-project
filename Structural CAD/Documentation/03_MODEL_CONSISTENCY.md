# MODEL CONSISTENCY CROSS-CHECK
## Structural CAD reinforcement package · revision **SC1** · 4 September 2026
### Brief §35 — MASTER ↕ STAAD ↕ REVIT ↕ CALCULATIONS ↕ REINFORCEMENT ↕ DXF

**Method: every value below was re-extracted from the file itself, not copied from a summary.**
DXFs were parsed with `ezdxf`; `.std` files were parsed for joint coordinates, element property
groups, supports, load cases and combinations; the Revit Dynamo scripts were read for their
geometry constants. Script: `Scripts/audit_inputs.py`.

> **Where a discrepancy exists, BOTH values are shown, the source of each is named, and the item
> is flagged. Nothing is silently chosen.**

---

## 1 — GEOMETRY

### 1.1 Controlling plan dimensions

| Item | **MASTER** A.3 / A.4 | **REV F DXF** `1_Underground_Level_Plan` | **STAAD** `.STD` (mid-surface) | **REVIT** `02_structural_main_box.py` | **THIS PACKAGE** `sc_proj.py` | Agree |
|---|---|---|---|---|---|---|
| Box external length | 22 000 | X 0 … 22 000 | grid to c/l 21.700 (= 22 000 ext) | `PCC_EXTENT_M` 0 … **22.000** | 22 000 | ✔ |
| Box external width | 6 200 | Y 0 … 6 200 | Z c/l 0.300 / 5.900 | `PCC_EXTENT_M` 0 … **6.200** | 6 200 | ✔ |
| Internal clear | 20 800 × 5 000 | X 600…21 400, Y 600…5 600 | implied by 600 walls | script comment states 20800 × 5000 | 20 800 × 5 000 | ✔ |
| Perimeter wall | 600 | 600 | shell group `509 TO 976 @ 0.6` | wall type **600 mm** | 600 | ✔ |
| Pressure slab | 900 | — | shell group `271 TO 508 @ 0.9` | roof slab **900** | 900 | ✔ |
| Mat | 600 | — | shell group `1 TO 270 @ 0.6` | mat **600** | 600 | ✔ |
| **W5** | 12 600 – 12 800, 200 | 12 600, 12 800 | shell group `977 TO 1030 @ 0.2` | c/l **12.700**, 200 | 12 600 – 12 800, 200 | ✔ |
| **W6 (M1)** | **14 800 – 15 200, 400** | 14 800, 15 200 | c/l **15.000**, group `1031 TO 1138 @ 0.4` | c/l **15.000**, type **400 mm** | 14 800 – 15 200, 400 | ✔ |
| **W7 (M1)** | **18 000 – 18 400, 400** | 18 000, 18 400 | c/l **18.200** | c/l **18.200**, type **400 mm** | 18 000 – 18 400, 400 | ✔ |
| W8 partitions ×4 | 3500/3610, 5410/5520, 9020/9130, 10930/11040 | identical | not modelled (non-structural) | modelled 110 | identical | ✔ |
| **ESC 1** | centre (2 050, 2 050) | `CIRCLE (2050,2050) r700` + `r950` | opening 1.4 sq at (2.050, 2.050) | (2.050, 2.050) | (2 050, 2 050) | ✔ |
| **ESC 2 (M1)** | centre (**19 900**, 2 050) | `CIRCLE (19900,2050) r700` + `r950` | opening at (**19.900**, 2.050) | **19.900** (script comment records the M1 shift) | (19 900, 2 050) | ✔ |
| Stair shaft (Bay 7) | 15 200 – 18 000 | 15 200, 18 000 | roof void X 15.000 – 18.200 (c/l to c/l) | — | 15 200 – 18 000 | ✔ |
| Stair void in the roof | 2 800 × 3 160, Y 600 – 3 760 | Y 600, 3 760 | opening to Z 0.300 – 4.010 | — | Y 600 – 3 760 | ✔ |
| Blast-door openings | Y 600 – 1 800 in W6, W7 | 600, 1 800 | — | — | Y 600 – 1 800 | ✔ |
| Headhouse external (M1) | 13 600 – 18 400 × 200 – 6 000 | `2_Ground_Plan` | — | `03_structural_headhouse.py` | 13 600 – 18 400 × 200 – 6 000 | ✔ |
| Entry stairwell external (M1) | 9 250 – 16 050 × 5 750 – 7 750 | `2_Ground_Plan` | — | `04_structural_entry_stairwell.py` | 9 250 – 16 050 × 5 750 – 7 750 | ✔ |

**All 18 controlling plan dimensions agree across every source. No discrepancy.**

### 1.2 Levels

| Level | Master A.4.3 | STAAD (model Y − 6.700) | This package | Agree |
|---|---|---|---|---|
| Grade | 0.000 | — | 0.000 | ✔ |
| Top of pressure slab | (−)2.000 | Y 4.700 → (−)2.000 | (−)2.000 | ✔ |
| Roof soffit | (−)2.900 | Y 3.800 → (−)2.900 | (−)2.900 | ✔ |
| Internal floor / top of mat | (−)6.100 | Y 0.600 → (−)6.100 | (−)6.100 | ✔ |
| Underside of mat | (−)6.700 | **Y 0.000** — the model datum | (−)6.700 | ✔ |
| Formation | (−)6.800 | — | (−)6.800 | ✔ |
| Design GWT | (−)2.000 **[ASSUMED]** | — | (−)2.000 **[ASSUMED]** | ✔ tag preserved |
| Stair L1 / L2 | (−)4.7333 / (−)3.3667 | — | (−)4.7333 / (−)3.3667 | ✔ |
| Headhouse soffit / top | +0.400 / +0.900 | — | +0.400 / +0.900 | ✔ |
| Sump invert / base | (−)7.600 / (−)8.000 | — | (−)7.600 / (−)8.000 | ✔ |

**The STAAD 6.700 m Y-offset (master M.13) was applied when comparing, not ignored.**

### 1.3 Main staircase — **FROZEN**

| Item | Master A.4.4 / B.5 | Rev F DXF | This package | Agree |
|---|---|---|---|---|
| Risers × rise | 24 @ **170.8333** | — | 24 @ 170.8333 | ✔ |
| Tread | 280 | — | 280 | ✔ |
| Flights | 3 × 8 | — | 3 × 8 | ✔ |
| Total rise | 4 100 | — | 4 100 | ✔ |
| Flight A / well / flight B | 15 300–16 500 / 16 500–16 700 / 16 700–17 900 | **15300, 16500, 16700, 17900** | identical | ✔ |
| Landing L1 | Y 3 760 – 4 960 | **3760, 4960** | identical | ✔ |
| L2 / arrival | Y 600 – 1 800 | **600, 1800** | identical | ✔ |
| Store under L1 | Y 4 960 – 5 600 | **4960, 5600** | identical | ✔ |
| Flight width / well | 1 200 / 200 | derived | 1 200 / 200 | ✔ |
| Headroom | 2 533 | — | 2 533 | ✔ |

> ### **THE MAIN STAIRCASE IS CONFIRMED UNCHANGED.**
> Every frozen value was re-extracted from `1_Underground_Level_Plan.dxf` and compared. Nothing
> in this package alters the staircase geometry.

---

## 2 — MATERIALS

| Property | Master A.5 | STAAD underground | STAAD entry stairwell | This package | Agree |
|---|---|---|---|---|---|
| Concrete | M35 | `ISOTROPIC M35` | `ISOTROPIC M35` (C11 resolved) | M35 | ✔ |
| E_c | 29 580 N/mm² | `E 2.95804e+07` kN/m² | `E 29580398` kN/m² | 29 580 | ✔ |
| Reinforcement | Fe500D | — | — | Fe500D | ✔ |
| Cover 75 / 50 / 40 / 30 | A.5 | — | — | identical | ✔ |
| L_d 40 φ, lap 50 φ | A.5 | — | — | identical, recomputed | ✔ |
| f_ck,dyn / f_y,dyn | 43.75 / 625 | — | — | 43.75 / 625 | ✔ |

---

## 3 — LOADING AND COMBINATIONS

| # | STAAD load case (verbatim from the file) | Master A.7 | This package | Agree |
|---|---|---|---|---|
| 1 | `DL1 SELF WEIGHT` | 25 kN/m³ | 25 | ✔ |
| 2 | `DL2 EARTH COVER ON ROOF 40.65 KN/M2` | 40.65 | **40.65 — but see C17** | ⚠ **C17** |
| 3 | `DL3 SIDL SERVICES AND FINISHES` | 2.0 / 1.0 | 2.0 / 1.0 | ✔ |
| 4 | `LL1 LIVE LOAD ON INTERNAL FLOOR 5.0 KN/M2` | 5.0 | 5.0 | ✔ |
| 5 | `DL4 STAIRCASE ON THE TWO SHAFT WALLS` | 2.947 | 2.947 | ✔ |
| 6 | `EP1 EARTH + WATER ON EXTERNAL WALLS` | 33.9 → 83.2 | 33.9 → 83.2 | ✔ |
| 7 | `HY1 HYDROSTATIC UPLIFT ON MAT 46.1 KN/M2` | 46.11 | 46.11 | ✔ |
| 8 | `BL1 BLAST ON ROOF 383 KN/M2` | 383 | 383 | ✔ |
| 9 | `BL2 BLAST ON EXTERNAL WALLS 383 KN/M2` | 383 | 383 | ✔ |
| 10 | `LL2 CONSTRUCTION SURCHARGE 20.0 KN` | 20.0 | 20.0 | ✔ |
| 11 | `BL3 BLAST IN THE STAIR SHAFT ON W6 AND W7 383 KN/M2` | B.2, Finding F1, M1-I3 | 383 on W6/W7 | ✔ |

| Comb | STAAD title | Master A.7.9 | This package | Agree |
|---|---|---|---|---|
| 101 | `ULS STATIC 1.5(DL+LL+EARTH+WATER)` | identical | identical | ✔ |
| 102 | `ULS UPLIFT 0.9DL + 1.5 HYDROSTATIC` | identical | identical | ✔ |
| **103** | `BLAST 1.0(DL + EARTH + WATER + BLAST) GAMMA = 1.0` | identical | **governs every blast element** | ✔ |
| 104 | `SLS 1.0(...) FOR CRACK WIDTH TO IS 3370` | identical | identical | ✔ |
| 105 | `CONSTRUCTION 1.5(...)` | identical | identical | ✔ |

**All four underground models (worked example, coarse, medium, fine) carry the identical
11-case / 5-combination register.** The mesh-study models differ only in mesh density
(336 / 1 138 / 1 138 / 4 552 shells) — verified by parse.

---

## 4 — ⚠ DISCREPANCIES FOUND. NONE IS SILENTLY RESOLVED

### 4.1 **C17 — engineered cover build-up does not sum** · NEW, raised by this package

| | Value A | Value B |
|---|---|---|
| **Source** | Master A.7.3 **total row**, A.7.4, Part L, and `DL2 EARTH COVER ON ROOF 40.65 KN/M2` in **all four** underground `.std` files | Master A.7.3 **column sum**: 5.40 + 2.85 + 5.00 + 8.50 + 15.00 + 2.40 |
| **Value** | **40.65 kPa** | **39.15 kPa** |

Every individual line of the A.7.3 table is arithmetically correct; the **total row is not the sum
of its own column**. The difference is exactly **1.50 kPa**.

**Held by this package: 40.65 kPa.** Reasons stated rather than assumed:
1. it is the value in Part A, Part L and **every STAAD model** — the design of record;
2. it is the **larger** value, so retaining it is conservative (roof COMB 103 stays 448.15 kPa
   rather than 446.65);
3. silently adopting 39.15 would *reduce* a design load, which is not permissible without a ruling.

**Effect on reinforcement: NONE.** At 39.15 the roof M_p would be 697.9 instead of 700.2 kNm/m
and utilisation 51.2 % instead of 51.4 %. **No bar, spacing or link changes.**

**Status: RULED AND CLOSED by RC1, 10 September 2026 (master Part H.14 / K.1 U9).** **40.65 kPa is held** and A.7.3 now shows why — the layer sum **39.15 plus a declared allowance of 1.50**, so the table no longer contradicts itself. 40.65 is the value in A.7.4, Part L and `DL2` in every underground `.std`, and it is the larger. **COMB 103 stays 448.15 kPa and nothing SC1 detailed changes.** Still flagged on R-001, R-101, R-301 and R-302, where the flag now reads as a recorded reconciliation rather than an open question.

### 4.2 **C18 — sump-pit base thickness** · NEW, raised by this package

| | Value A | Value B |
|---|---|---|
| **Source** | Master F.1 "Sump pit walls/base **300/400**", corroborated by master A.4.3 levels: invert (−)7.600 to base (−)8.000 = **400** | Text on sheet **S-06**: *"PIT WALLS / BASE 300 THK, T16 @ 150 EF EW"* |
| **Value** | walls 300, **base 400** | walls 300, **base 300** |

**Held: base 400** — the level difference is independent corroboration.
**Status: RULED AT 400 and CLOSED by RC1, 10 September 2026 (master Part H.14 / K.1 U10).** (−)8.000 − (−)7.600 = **0.400** is arithmetic, and master F.1 says 400 independently; sheet S-06's "300" is a transcription error and is superseded. **400 is what SC1 detailed, so nothing on R-101 or R-102 changes.**

*(The sump-pit plan position and size — 1 500 × 1 500 × 1 500 at X 11 070–12 570, Y 900–2 400 —
were extracted from the S-06 geometry itself and are [CONFIRMED]; only the base thickness is in
conflict.)*

### 4.3 **C16 — roof / platform junction** · pre-existing, carried forward

| | Value A | Value B |
|---|---|---|
| **Source** | Master A.4.7: *"over the platform it becomes the 500 headhouse roof"* | Master B.6 (design), A.7.6 (loading), F.2 (reinforcement register): a **250** stairwell roof; and `Entry_Stairwell.std` is built at 250 |
| **Value** | 500 | **250** |

The headhouse footprint (Y 200–6 000) **does not overlap** the platform (Y 6 000–7 500), so the
two statements cannot describe the same concrete.

**Detailed at 250** on the authority of master rule M.2 (Parts A, B, L primary) and because the
model is built at 250. **The A.4.7 clause is not edited.**
**Status: [UNRESOLVED]. Flagged on R-001, R-603, R-702, R-703, R-803, R-804.**

### 4.4 Items noted for completeness, not affecting this package

| Item | Note |
|---|---|
| Sentry post combination count | Master A.7.9 records 15; `Sentry_Post_Framed_Seismic.std` has 16. **Sentry post is out of scope**; master H.4 already records it |
| C9 / U1 sentry base shear | 73.18 (STAAD) vs 59.3 (hand). **Out of scope** |

---

## 5 — CHAIN CONSISTENCY: CALCULATIONS → REINFORCEMENT → SCHEDULE → DXF

This is the link the brief's chain most often breaks. It is closed **mechanically**, not by care.

```
sc_proj.py      one definition of every dimension, level, thickness and load
   |
rc_calc.py      the IS 456 equations, with tau_c forced to the STATIC grade
   |
verify_partB.py 212 master Part B values recomputed  ->  211 agree, 1 differs (C17)
   |
rebar_data.py   THE SINGLE SOURCE OF TRUTH: 92 bar marks, counts and cut lengths
   |            computed from the sc_proj geometry
   +---------------------------+
   |                           |
make_schedules.py          g00..g08 sheet generators
   |                           |
Schedules/*.md, *.csv      DXF/**/*.dxf  (bar-mark balloons, keys and
                                          schedule extracts all read rebar_data)
   |                           |
   +----------> qa_crosscheck.py <----------+
                reads the finished DXFs back and compares them to the schedule
```

| Consistency check | Method | Result |
|---|---|---|
| Master Part B ↔ this package's calculations | `verify_partB.py`, 212 values | **211 agree, 1 differs → C17 raised** |
| Calculations ↔ reinforcement | `rebar_data.py` imports `rc_calc` and `sc_proj` | single source |
| Reinforcement ↔ schedules | `make_schedules.py` reads `rebar_data` | cannot diverge |
| Reinforcement ↔ drawings | generators read `rebar_data`; `sc_views.markkey()` and `bbs_extract()` look every mark up | cannot diverge |
| Drawings ↔ schedules, **verified independently** | `qa_crosscheck.py` **re-reads the DXFs** | **0 orphan marks · all 92 + 1 drawn · 0 broken references** |
| Drawings ↔ sheet standard | `validate_dxf.py` | **30 files, 0 errors, 0 review items** |

> **No drawing in this package shows an arrangement that differs from a calculation** — the
> project's standing rule (master M.9) — and that is now enforced by construction, not by review.

---

## 6 — SOURCES THAT COULD NOT BE FULLY CROSS-CHECKED

| Source | Limitation | Consequence |
|---|---|---|
| **STAAD results** | **None exist.** No `*.anl`, `*.out`, `*.txt` or `*.rea` in `current/staad/` | The analysis→design link **cannot be checked at all**. Every design action is a hand calculation |
| **Revit model** | **No `.rvt` exists** — only 6 Dynamo Python scripts | The Revit leg was checked **against the scripts' geometry constants**, which agree (§1.1). A built model has not been compared |
| **k_s second bound** | Only 100 000 kN/m³ is modelled; master A.6 / K.2-A4 require **both** bounds | Mat moment distribution is not bounded on the stiff side |
| **Code documents** | None held | Clause numbers verifiable only against master Part G |
| **S-01…S-08** | Seven of the eight output sheets and the whole generator toolchain are absent | Not regenerated, not fabricated. This R-series is independent |

---

## 7 — CONCLUSION

**Geometry, materials, loading and combinations are consistent across the master, the Rev F
drawings, all five in-scope STAAD models, the Revit scripts and this package — 18 controlling
dimensions, 10 levels, 11 load cases and 5 combinations all agree, and the frozen staircase is
confirmed unchanged.**

**Three conflicts are open and none is resolved by this package: C16 (carried forward), and
C17 and C18 (both newly raised here).** None affects a single bar; all three need a ruling.

**The one link in the chain that cannot be checked is analysis → design, because no STAAD result
exists.**
