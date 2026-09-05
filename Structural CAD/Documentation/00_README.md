# STRUCTURAL CAD — REINFORCEMENT PACKAGE
## Underground CBRN-hardened blast-resistant protective structure, Pune
### Package revision **SC1** · structural revision Phase 2 Rev A + M1 · 4 September 2026

> ## ⛔ SENTRY POST — COMPLETELY EXCLUDED
> No sentry-post design, detail, drawing, schedule, quantity, calculation or folder exists
> anywhere in this package. `DXF/Sentry_Post/` is **deliberately not created**. Master sections
> B.8 and F.4 (sentry design and reinforcement) were **not used**.

> ## ⚠ NO STAAD RESULT EXISTS
> `current/staad/` contains **five `.std` model files and no output of any kind** — no `.anl`,
> `.out`, `.txt` or `.rea`. Master D.3.5 states the same.
> **Every design action in this package is `MANUAL CALCULATION — NOT DIRECT STAAD OUTPUT`.**
> That statement is printed in the header strip of **all 30 drawings**.

> ## ⚠ THIS PACKAGE IS NOT CONSTRUCTION-READY
> `QAQC/Reinforcement_QAQC_Report.md` §5 lists **13 items requiring review by a qualified
> structural engineer**, **3 unresolved conflicts** and a **missing Phase 3 analysis**.
> Nothing here is claimed as "fully code compliant" — **no code document was available against
> which to verify a single clause number.**

---

## 1 — WHAT IS HERE

| Deliverable | Where | Extent |
|---|---|---|
| **Input audit** | `QAQC/00_INPUT_AUDIT.md` | every dependency parsed, missing and conflicting information listed |
| **Design basis** | `Calculations/01_DESIGN_BASIS.md` | materials, covers, L_d, loads, combinations, methodology, **conflict C17 raised** |
| **Element design** | `Calculations/02_ELEMENT_DESIGN.md` | 16-step design record for every in-scope element |
| **Independent verification** | `Calculations/00_PartB_verification_output.txt` | **212 master Part B values recomputed — 211 agree** |
| **Bar bending schedules** | `Schedules/` | master + 7 group schedules + CSV + summary. **92 marks, 70.46 t** |
| **Drawings** | `DXF/` | **30 A1 sheets**, AutoCAD 2010 ASCII, validated |
| **Detail register** | `Details/DETAIL_REGISTER.md` | index to every detail, and to every detail deliberately *not* drawn |
| **Generation scripts** | `Scripts/` | 17 Python modules; the whole package rebuilds with one command |
| **QA/QC** | `QAQC/` | main report, IS 456 matrix, IS 13920 matrix, legibility QA, DXF validation, bar-mark cross-check |
| **Documentation** | `Documentation/` | this file, drawing index, CAD standards, model consistency |

### Headline numbers

| | |
|---|---|
| Drawings | **30** sheets, 11 645 entities, ≈ 4.0 MB |
| Native DIMENSION / LEADER / HATCH / INSERT | **173 / 133 / 1 126 / 154** |
| Bar marks | **92** unique, + 1 fabric item |
| Reinforcement | **70 457 kg = 70.46 t** |
| DXF validation | **30 files, 0 errors, 0 review items** |
| Bar-mark cross-check | **0 orphans · all 92 drawn · 0 broken references** |
| Part B verification | **212 values, 211 agree, 1 differs → conflict C17 raised** |

---

## 2 — READ IN THIS ORDER

1. `QAQC/00_INPUT_AUDIT.md` — **what was available and what was not.** Start here.
2. `Calculations/01_DESIGN_BASIS.md` — materials, loads, combinations, and **C17**.
3. `Calculations/02_ELEMENT_DESIGN.md` — the design itself, element by element.
4. `Documentation/01_DRAWING_INDEX.md` → the drawings in `DXF/`.
5. `Schedules/BBS_MASTER.md` — the schedule the drawings reconcile to.
6. `QAQC/Reinforcement_QAQC_Report.md` — **what is PASS, REVIEW and NOT DETERMINABLE.**
7. `QAQC/IS456_Compliance_Matrix.md` and `QAQC/IS13920_Compliance_Matrix.md`.
8. `Documentation/03_MODEL_CONSISTENCY.md` — the master ↕ STAAD ↕ Revit ↕ DXF cross-check.

---

## 3 — FOLDER STRUCTURE

```
Structural CAD/
├── Calculations/     design basis, element design, verification output
├── DXF/
│   ├── General/          R-001 .. R-004
│   ├── Foundations/      R-101 .. R-103
│   ├── Walls/            R-201 .. R-205
│   ├── Slabs/            R-301 .. R-304        (roof / pressure slab)
│   ├── Beams/            R-401 .. R-402        (beam-TYPE elements only)
│   ├── Stairs/           R-601 .. R-604
│   ├── Headhouse/        R-701
│   ├── Entrance/         R-702 .. R-703
│   └── Typical_Details/  R-801 .. R-805
├── Schedules/        BBS master, per-group schedules, CSV, summary
├── Details/          detail register
├── Scripts/          the generators - EDIT THESE, NOT THE DXFs
├── QAQC/             audit, matrices, reports, validation output
└── Documentation/    this file, drawing index, CAD standards, consistency
```

**No `Columns/` folder and no `Sentry_Post/` folder — neither element exists in scope.**

---

## 4 — REGENERATING THE PACKAGE

The DXFs are **build artefacts**. Edit the source, never the DXF (master rule M.12).

```bash
pip install ezdxf                                    # required
python3 "Structural CAD/Scripts/build_all.py"        # rebuilds everything
```

`build_all.py` runs: `verify_partB` → `make_schedules` → `g00`…`g08` →
`qa_crosscheck` → `validate_dxf`, and reports any step that is not clean.

| To change | Edit |
|---|---|
| A dimension, level, thickness, load | `Scripts/sc_proj.py` |
| A bar diameter, spacing, count, mark | `Scripts/rebar_data.py` |
| A layer, lineweight, text height, title block | `Scripts/sc_dxflib.py` |
| A shared view or panel | `Scripts/sc_views.py` |
| One sheet | the matching `gNN_*.py` |
| A design equation | `Scripts/rc_calc.py` |

> **The schedules and the drawing annotation are both generated from `rebar_data.py`, so they
> cannot drift apart** — and `qa_crosscheck.py` re-reads the finished DXFs to prove it.

Optional visual QA (needs `matplotlib`):
```bash
python3 "Structural CAD/Scripts/render_qa.py" <file.dxf> <out.png> [x0 x1 y0 y1] [dpi]
```

---

## 5 — THE DESIGN IN ONE TABLE

| Element | Thk | Governing action (COMB 103 BLAST unless noted) | Provided | Util. |
|---|---|---|---|---|
| Mat | 600 | soft/red-bole band, M = qL²/12 = **303.7 kNm/m** | T16 @ 150 EF EW + T12 @ 250×250 links | **84 %** |
| Perimeter walls W1–W4 | 600 | M_p = wL_n²/16 = **245.1 kNm/m** | T16 @ 150 EF EW + T12 closed @ 200 | 68 % |
| W5 | 200 | none — gas/fire separation only | T12 @ 150 EF EW | nominal |
| **W6 / W7 (M1)** | **400** | shaft equalises to full p_so, **245.1 kNm/m** | T20 @ 150 EF EW + T12 4L @ 200 | 69 % |
| W8 partitions ×4 | 110 | non-structural | A252 fabric both faces | — |
| **Pressure slab** | **900** | **M_p = 700.2 kNm/m**, x_u/d = **0.139** | T25 @ 150 EF EW + T12 4L @ 250 / 2L @ 300 | 51 % |
| Roof cantilever pad | 900 | **M(root) = 758.6 > mid-span 700.2** (Finding F2) | T25 @ 150 top + T12 4L @ 250 throughout | 56 % |
| **Headhouse roof** | **500** | **396.5 kNm/m** — most conservative of three analyses | T20 @ 150 EF EW + T12 4L @ 175 / 250 | **90 %** |
| Headhouse walls | 400 | **383 kPa EITHER FACE** (C10), 137.9 kNm/m | T16 @ 150 EF EW + T12 4L @ 250 | 59 % |
| Main stair flight / landings | 200 | **IS 456, not blast** — 26.2 / 49.7 kNm/m | T12 @ 150 / **T12 @ 125** | 52 % / **84 %** |
| Entry stairwell flight | 250 | **IS 456, not blast** — 65.8 kNm/m | T16 @ 200 | 75 % |
| Entry stairwell walls/roof/landings | 250 | minimum steel governs | T12 @ 200 EF EW | 20–41 % |

**Maximum bar spacing 150 mm both curtains — an EMP requirement, stricter than IS 456
Cl. 26.3.3, and it is what sets the spacing of every main curtain in the blast envelope.**

---

## 6 — OPEN ITEMS. NONE IS CLOSED BY THIS PACKAGE

| Ref | Item | Status |
|---|---|---|
| **C16** | Roof / platform junction — A.4.7 (500) vs B.6 / A.7.6 / F.2 (**250**). **Detailed at 250; the A.4.7 clause is not edited** | **UNRESOLVED — user ruling required** |
| **C17** | **NEW.** Engineered cover **40.65 stated vs 39.15 column sum** in master A.7.3. **40.65 held. No bar changes** | **UNRESOLVED — user ruling required** |
| **C18** | **NEW.** Sump-pit base **400** (master F.1 + levels) vs **300** (S-06 text). **400 held** | **UNRESOLVED — user ruling required** |
| A2 | Design GWT (−)2.000 **[ASSUMED]** — two-thirds of the lateral load, all of the uplift | **REVIEW — monsoon monitoring** |
| A4 | k_s second bound (500 000) **never run** | **NOT DETERMINABLE** |
| M-1 | **No STAAD result of any kind** | **NOT DETERMINABLE** |
| M-2 | **No code document in the workspace** | **NOT DETERMINABLE** |
| Phase 3 | Non-linear SDOF support rotation — **blast capacity not demonstrated** | **NOT DETERMINABLE** |
| U2 / U3 | Direct-hit requirement; DBT yield | **UNRESOLVED — client / military** |
| Openings | Blast valves ×5, service-entry plate, CBRN penetrations — **no design basis, not fabricated** | **NOT DETERMINABLE** |

---

## 7 — WHAT WAS DELIBERATELY NOT DONE

| Not done | Why |
|---|---|
| **No sentry-post anything** | Out of scope by instruction |
| **No R-501 / R-502 / R-503 column sheets, no beam–column joint detail** | **No RC column, framed beam or beam–column joint exists.** Drawing one would be fabrication |
| **S-01…S-05, S-07, S-08 not regenerated** | Their generator toolchain is absent from the workspace; `CLAUDE.md` forbids inventing it. A separate R-series is issued instead |
| **S-06 and the ten Rev F input drawings not modified** | They are inputs, already at M1, and this package had no reason to touch them |
| **C16, C17, C18 not resolved** | The project record disagrees with itself in three places; resolving that is the user's ruling, not this package's |
| **Blast-door vendor requirements not invented** | Only the structural interface is drawn |
| **IS 2502 not cited** | Named in the brief, but not held and not in the project's verified clause register. Project rule **PBR-1** is declared in its place |

---

## 8 — DEPENDENCIES

| | |
|---|---|
| **ezdxf** | required to regenerate the DXFs (`pip install ezdxf`) |
| **matplotlib** | optional, for `render_qa.py` visual QA only |
| Python | 3.11 in the session used to build this package |

Neither library is vendored into the repository. The DXFs are plain ASCII and open in AutoCAD,
BricsCAD, DraftSight, LibreCAD and QCAD without either.
