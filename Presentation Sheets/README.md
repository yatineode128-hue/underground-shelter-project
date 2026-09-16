# Presentation Sheets — A2 structural series, revisions SR1 through SR2A

Four A2 structural reinforcement sheets drawn in the layout and title block of the
supplied Revit A2 architectural set (`ARCH001 … ARCH005`, `Project1.pdf`), so that they
read as the next four sheets of that same series.

**SR1 — the underground structure**

| Sheet | Drawing No. | Title | Views |
|---|---|---|---|
| **SHEET 06** | **STR006** | STRUCTURAL REINFORCEMENT DETAILING — ROOF SLAB & MAT FOUNDATION | 1 roof slab reinforcement plan 1:100 · 2 roof slab longitudinal section A-A 1:100 · 3 mat foundation reinforcement plan 1:100 · 4 mat foundation longitudinal section B-B 1:100 |
| **SHEET 07** | **STR007** | STRUCTURAL REINFORCEMENT DETAILING — 600 SHEAR WALL & MAIN STAIRCASE | 1 600 shear wall vertical section 1:30 · 2 600 shear wall part plan / horizontal section 1:25 · 3 main staircase reinforcement plan 1:40 · 4 main staircase longitudinal section C-C 1:40 |

> **SR1A, by instruction, on the owner's own copies of these two sheets.** The
> *DESIGN BASIS* panel is **deleted from both**, and **the whole revision line**
> (`STRUCTURAL - PHASE 2 REV A + M1`) is **deleted from the header** — asked directly which
> reading was meant (drop just `REV A`, or the whole line) and the whole line was the answer,
> so `sheet_data.IDENTITY` now carries only the four site-description lines and no revision
> text at all. **No view, scale, dimension, bar or count changed.** The freed column fills
> with `table_stack()`, same as SR2A below. Fixing this exposed and fixed **a real bug** in
> `a2_lib.A2Sheet.table()`: its row-height shrink loop could quantise one 0.05 mm step below
> `MIN_TXT_H` when the starting height wasn't grid-aligned — a `pad` parameter and a post-loop
> floor clamp fix it, verified **not** to change STR008 / STR009 (byte-identical rebuild,
> diffed with timestamps stripped). **This also CLOSES `SR2-F2`** — see below. Master **H.41**.

**SR2 — the sentry post.  This is the project's IS 13920:2016 sheet pair.**

> **SR2A, same day, by instruction.** STR008 and STR009 were re-issued with the
> *DESIGN BASIS* and *DECLARED DETAILING DECISIONS AND OPEN ITEMS* panels **deleted**, and
> **`REV A` removed** from the title-block identity line (`STRUCTURAL - PHASE 2 + M1`).
> **No view, scale, dimension, bar or count changed.** The schedules now fill the whole
> right-hand column via `a2_lib.A2Sheet.table_stack()`, which solves for the row height that
> ends the stack exactly on the frame — so the sheets have no void and the tables are
> noticeably more legible. The decisions and open items **still exist**; their authority is
> now master **H.40.4** and **H.40.5**, and title-block note 7 (STR008) / note 9 (STR009)
> points there. **`sheet_data.IDENTITY` and `sentry_data.IDENTITY` are now independent lists**
> (SR1A gave STR006 / STR007 no revision line at all; STR008 / STR009 keep `STRUCTURAL -
> PHASE 2 + M1`), sharing only their four site-description lines, enforced by an assertion.

| Sheet | Drawing No. | Title | Views |
|---|---|---|---|
| **SHEET 08** | **STR008** | STRUCTURAL REINFORCEMENT DETAILING OF SENTRY POST — BEAMS & COLUMN | 1 first-floor framing plan 1:50 · 2 beam B1 longitudinal section 1:40 · 3 beam B2 longitudinal section 1:40 · 4 sections a-a/b-b (B1), c-c/d-d (B2), 3-3 (C1 confining zone), 4-4 (C1 general) 1:10 · 5 column C1 vertical section, full height, 1:25 |
| **SHEET 09** | **STR009** | STRUCTURAL REINFORCEMENT DETAILING OF SENTRY POST — FOOTING & SLAB | 1 slab S1 bottom reinforcement plan 1:40 · 2 slab S1 top reinforcement plan (400 edge bands + 700 × 700 corner torsion mats) 1:40 · 3 slab S1 longitudinal section 2-2 1:25 · 4 isolated footing F1 reinforcement plan 1:20 · 5 isolated footing F1 section 1-1 1:20 |

## Sheet standard

Measured off the vector content of the supplied Revit PDF — not estimated — so the two
sheets sit on the same frame as `ARCH001 … ARCH005`:

```
A2 landscape 594 x 420 mm, drawn in PAPER MILLIMETRES, plotted 1:1
outer border          27.0 , 19.1   ->  567.0 , 400.9
inner frame           38.8 , 30.9   ->  555.2 , 389.1
title-block divider   x = 464.3, full height of the inner frame
title-block panels    x 467.0 .. 552.4, four stacked boxes
    A  314.5 .. 386.4   identity, rule at 332.7, "NOTES" caption under it
    B  193.4 .. 311.8   numbered general notes
    C  130.3 .. 190.6   drawing title, large, centred
    D   33.6 .. 128.2   project / sheet data, rules at
                        40.9  54.6  61.8  69.1  76.4  83.6  96.9
DXF FORMAT            AutoCAD 2010 ASCII (AC1024) - native LINE, LWPOLYLINE,
                      CIRCLE, ARC, ELLIPSE, TEXT, HATCH, DIMENSION, INSERT
```

**Declared deviation:** master E.3.1 fixes AutoCAD R12 ASCII for the S-01…S-08 output
set. Those sheets are not touched by this package. STR006 … STR009 are written at
AC1024 so they carry real `DIMENSION` and `HATCH` entities, exactly as the
`Structural CAD` R-series does (its own declared deviation X1).

## Colour

Dark only, and mostly black. Four ACI colours, every one of them dark on white paper:

| ACI | Used for |
|---|---|
| **7 black** | all line work, text, dimensions, tables, title block |
| **8 dark grey** | hatching, soil and rock, work beyond the cut plane |
| **1 dark red** | main reinforcement, trimmers, starters |
| **5 dark blue** | links, stirrups and distribution steel |

No yellow, no cyan, no bright green, no light grey appears anywhere.

## Where the data comes from

Nothing on either sheet is invented.

* **Geometry, levels, thicknesses, loads, capacities** — `master/MASTER_PROJECT_STATE.md`
  Parts A.3, A.4, A.5, A.6, A.7.3, A.7.8, B.1, B.3, B.4, B.4.1, B.5 and F.1 / F.2, read
  through `Structural CAD/Scripts/sc_proj.py`.
* **Every bar mark** — `Structural CAD/Scripts/rebar_data.py`. Both bar-mark schedules are
  generated from it, and the tags on the views quote nothing else, so **a mark cannot
  appear on a view without a schedule entry**.
* **The main staircase is frozen** — 24R at 170.8333 / 280, 3 flights × 8, total rise 4100,
  well 200, waist 200, headroom 2533. Read from `sc_proj.STAIR`; unchanged by this package.

## Code basis — read this before quoting the sheets

The request for SR1 asked for detailing *"as per IS 13920"*. What the sheets carry is what
the project's design actually is, and the title blocks say so:

* The box — mat, roof slab, 600 perimeter walls — is designed to **IS 456:2000** with
  **IS 4991:1968** blast actions and **IS 3370 (Pt 2)** crack control. Seismic actions are
  **IS 1893 (Pt 1):2016**.
* **IS 13920:2016 has been checked for the box and does not govern.** Master A.7.8:
  A<sub>h</sub> 0.075, V<sub>b</sub> 1050 kN, 525 kN per long wall → τ = **0.063 N/mm²**, so
  **Cl. 10.4 boundary elements are NOT triggered**, and no ductile-detailing clause changes
  any bar on STR006 or STR007. That is finding **`SR1-F1`**.
* **The IS 13920 ductile detailing in this project is carried by the sentry post frame**
  (master B.8, F.4) — and **that frame is STR008 / STR009**, added by SR2. STR008 carries a
  14-clause IS 13920 compliance table: Cl. 6.1 geometry, Cl. 6.2 beam steel, Cl. 6.3.3 /
  **6.3.4** capacity-design shear with τ<sub>c</sub> taken as zero, Cl. 6.3.5 hoop spacing,
  Cl. 7.2.1 strong-column–weak-beam, Cl. 7.4 ties, Cl. 8.1 / 8.2 special confining
  reinforcement.

## Sentry post — the four declared detailing decisions, and `SR2-F1`

The master does not settle four things the sentry post sheets had to draw. All four are
**declared in a panel on the face of the sheet** and in master H.40.4: **D1** top steel
detailed continuous (F.4 gives no curtailment point) · **D2** exterior-joint anchorage, a
90° leg of L<sub>d</sub> − 300 = 425 for T16 and 625 for T20 · **D3** column verticals
splice-free, one 8 724 mm bar inside the 12 000 stock length, so no lap is invented ·
**D4** slab bottom steel, 50 % full length and the remainder cut at 0.25 L.
**Since SR2A these are recorded in the master only** — the sheets carry the `(D1)…(D4)`
tags and a title-block note that points at master H.40.4, not the panel.

**`SR2-F1` is open and it blocks work.** Master B.8.6 evaluates the **roof** joint with
**B2 = 2-T20** (1.4 ΣM<sub>b</sub> = 138.5 ≤ ΣM<sub>c</sub> 101, "marginal"); master F.4
schedules **3-T20 top at supports** for B2 and does not distinguish level. With 3-T20 at
the roof, 1.4 ΣM<sub>b</sub> = **195.7 > ΣM<sub>c</sub> = 101** and **Cl. 7.2.1 fails**.
Both statements cannot be true, so **STR008 details the FIRST-FLOOR frame only** and the
roof frame is cross-referenced, not drawn. It needs a ruling, not a drafting decision.

**The sentry post is excluded from `rebar_data.py`** — that file says so in its own header
and SR2 does not change it. `sentry_data.py` is a **separate** bar-mark register for the
sentry post, built to the same rule (a mark cannot appear on a view without a schedule
entry; uniqueness asserted), importing `rebar_data.cut_length` and `rc_calc` rather than
re-deriving them.

## Build

```
cd "Presentation Sheets/Scripts"
python3 s06_roof_mat.py               # -> DXF/STR006_...dxf
python3 s07_wall_stair.py             # -> DXF/STR007_...dxf
python3 s08_sentry_beam_col.py        # -> DXF/STR008_...dxf
python3 s09_sentry_footing_slab.py    # -> DXF/STR009_...dxf
python3 qa_overlap.py ../DXF/STR00*.dxf     # drafting QA, exits non-zero on a defect
python3 render_a2.py  ../DXF/STR00*.dxf     # visual QA PNG
python3 render_pdf.py ../DXF/STR00*.dxf     # true-size A2 vector PDF, 1:1
```

Each generator writes its own DXF; they take no arguments and the save path is at the
bottom of each script's run (see master H.40.7).

`a2_lib.py` is the sheet library (frame, title block, tables, panels, dimensions, rebar
aids). `sheet_data.py` holds every value STR006 / STR007 print and `sentry_data.py` every
value STR008 / STR009 print, so no two sheets can disagree with each other or with the
project.

`qa_overlap.py` measures text with the **same `ezdxf.bbox` call** the project auditor
`DRAWING QAQC/Scripts/dxfqa.py` uses, so the two cannot disagree about what fits, and adds
three tests `dxfqa` does not make: near-touches at 2 % instead of 12 %, text below
`MIN_TXT_H`, and a non-dark-layer census. It reads the MTEXT inside rendered `DIMENSION`
blocks as well, so a dimension value colliding with a label is caught.

Tables and view titles are **measured, not guessed**: every cell and every title is sized
with the same font metrics `ezdxf` places it with, and shrunk until it fits its column.
That is why all four sheets pass the drafting QA with **zero text overlaps**.

**`SR2-F2`, open:** `qa_overlap.py` reports that **STR007's two note panels are set at
1.49 mm**, below the 1.70 mm `MIN_TXT_H` this package declares in `a2_lib.py` — 53 lines.
STR006, STR008 and STR009 are clean. **STR007 is deliberately NOT changed**: SR1 is a
released revision and the instruction that commissioned SR2 does not cover it. Recorded in
master H.40.5, not acted on.

## Registration with the project QA tools

Done, per `CLAUDE.md`:

* `DRAWING QAQC/Scripts/qa_report_data.py` — `Presentation Sheets/DXF/` added to
  `DISCIPLINE`; `A2` added to `sheet_size()` (including the 540 × 381.8 inset Revit sheet
  frame this series uses); `STR006`, `STR007`, `STR008` and `STR009` titles added to
  `TITLE_OVERRIDE`, because the Revit-style title block stacks the title over five lines
  and there is no single text to read.
* `DRAWING QAQC/Scripts/make_index.py` — `STRUCTURAL - A2 presentation sheets` added to
  `ORDER` (done at SR1; unchanged by SR2).
* Both re-run. `DRAWING_INDEX.md` and `qa_index.json` now carry **84 drawings, 78 PASS**;
  **STR006, STR007, STR008 and STR009 all report PASS**.

### `SR2-F2` — CLOSED at SR1A

Recorded at SR2A: `qa_overlap.py` found STR007's two note panels rendering at **1.49 mm**,
below the package's own 1.70 mm floor, and it was **deliberately left unfixed** because STR007
was outside that instruction's scope. STR007 is directly in scope at SR1A. The offending panel
is deleted outright, and the `WALL SCHEDULE` table that shares its column — the one table on
the whole four-sheet set that was genuinely too wide for its column — is verified fitting at
**exactly 1.70 mm with 2.1 mm of real margin** (`pad=2.4`, see H.41.2). **There is no longer
any sub-floor text anywhere in this package.**

**Known cosmetic gap:** the index's `Scale` column shows `-` for all four sheets. `scale_of()`
looks for the scale value inside the same text as the word "SCALE"; this series follows
the Revit title block, which puts the label `Scale` and the value `1 : 100` /
`As indicated` in two separate cells. The title block is right; the index reader cannot
see it. Not changed, because `scale_of()` is shared with the other 80 drawings.
