# Presentation Sheets — A2 structural series, revision SR1

Two A2 structural reinforcement sheets drawn in the layout and title block of the
supplied Revit A2 architectural set (`ARCH001 … ARCH005`, `Project1.pdf`), so that they
read as the next two sheets of that same series.

| Sheet | Drawing No. | Title | Views |
|---|---|---|---|
| **SHEET 06** | **STR006** | STRUCTURAL REINFORCEMENT DETAILING — ROOF SLAB & MAT FOUNDATION | 1 roof slab reinforcement plan 1:100 · 2 roof slab longitudinal section A-A 1:100 · 3 mat foundation reinforcement plan 1:100 · 4 mat foundation longitudinal section B-B 1:100 |
| **SHEET 07** | **STR007** | STRUCTURAL REINFORCEMENT DETAILING — 600 SHEAR WALL & MAIN STAIRCASE | 1 600 shear wall vertical section 1:30 · 2 600 shear wall part plan / horizontal section 1:25 · 3 main staircase reinforcement plan 1:40 · 4 main staircase longitudinal section C-C 1:40 |

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
set. Those sheets are not touched by this package. STR006 / STR007 are written at
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

The request for these sheets asked for detailing *"as per IS 13920"*. What the sheets
carry is what the project's design actually is, and the title block says so:

* The box — mat, roof slab, 600 perimeter walls — is designed to **IS 456:2000** with
  **IS 4991:1968** blast actions and **IS 3370 (Pt 2)** crack control. Seismic actions are
  **IS 1893 (Pt 1):2016**.
* **IS 13920:2016 has been checked for the box and does not govern.** Master A.7.8:
  A<sub>h</sub> 0.075, V<sub>b</sub> 1050 kN, 525 kN per long wall → τ = **0.063 N/mm²**, so
  **Cl. 10.4 boundary elements are NOT triggered**, and no ductile-detailing clause changes
  any bar on either sheet.
* The **IS 13920 ductile detailing in this project is carried by the sentry post frame**
  (master B.8, F.4) — beams B1 / B2, column C1 with T10 confining hoops at 85, SCWB to
  Cl. 7.2.1. That frame is **not on these two sheets**.

## Build

```
cd "Presentation Sheets/Scripts"
python3 s06_roof_mat.py          # -> DXF/STR006_...dxf
python3 s07_wall_stair.py        # -> DXF/STR007_...dxf
python3 render_a2.py  ../DXF/STR00*.dxf     # visual QA PNG
python3 render_pdf.py ../DXF/STR00*.dxf     # true-size A2 vector PDF, 1:1
```

`a2_lib.py` is the sheet library (frame, title block, tables, panels, dimensions, rebar
aids). `sheet_data.py` holds every value both sheets print, so the two cannot disagree
with each other or with the project.

Tables and view titles are **measured, not guessed**: every cell and every title is sized
with the same font metrics `ezdxf` places it with, and shrunk until it fits its column.
That is why both sheets pass the drafting QA with **zero text overlaps**.

## Registration with the project QA tools

Done, per `CLAUDE.md`:

* `DRAWING QAQC/Scripts/qa_report_data.py` — `Presentation Sheets/DXF/` added to
  `DISCIPLINE`; `A2` added to `sheet_size()` (including the 540 × 381.8 inset Revit sheet
  frame this series uses); `STR006` / `STR007` titles added to `TITLE_OVERRIDE`, because
  the Revit-style title block stacks the title over five lines and there is no single
  text to read.
* `DRAWING QAQC/Scripts/make_index.py` — `STRUCTURAL - A2 presentation sheets` added to
  `ORDER`.
* Both re-run. `DRAWING_INDEX.md` and `qa_index.json` now carry 82 drawings; **STR006 and
  STR007 both report PASS**.

**Known cosmetic gap:** the index's `Scale` column shows `-` for both sheets. `scale_of()`
looks for the scale value inside the same text as the word "SCALE"; this series follows
the Revit title block, which puts the label `Scale` and the value `1 : 100` /
`As indicated` in two separate cells. The title block is right; the index reader cannot
see it. Not changed, because `scale_of()` is shared with the other 80 drawings.
