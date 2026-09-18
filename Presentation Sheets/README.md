# Presentation Sheets — A2 series, revisions SR1 through MEP2

**Ten A2 sheets**, all in the layout and title block of the supplied Revit A2 architectural
set (`ARCH001 … ARCH005`, `Project1.pdf`):

| Sheets | Drawing Nos. | Discipline | Revision |
|---|---|---|---|
| **01 · 02** | `ARCH001` `ARCH002` | ARCHITECTURAL — **redraws of the owner's own sheets 1 and 2** | **MEP2**, corrected **MEP3** |
| 06 · 07 | `STR006` `STR007` | STRUCTURAL — the underground box | SR1 / SR1A |
| 08 · 09 | `STR008` `STR009` | STRUCTURAL — the sentry post | SR2 / SR2A |
| 10 · 11 | `MEP010` `MEP011` | MEP — HVAC, EMP and the drainage structures | MEP1 |
| **12** | `FLS012` | FIRE AND LIFE SAFETY — escape plan | **MEP2** |
| **13** | `WMS013` | WORKS MANAGEMENT — programme and bill | **MEP2** |

**MEP2 — the fire plan, the works management sheet and the two redraws.  No design value
moved and no analysis was run.**

* **`FLS012` SHEET 12** — 1 underground level escape plan 1:100 · 2 entry level escape plan
  1:100 · 3 escape shaft section and ladder 1:100 · 4 evacuation decision rule. Every route,
  travel distance and climb is **computed** in `Fire and Life Safety/Scripts/fs_data.py` from
  the confirmed geometry, so a figure on the sheet cannot disagree with the schedule.
  **The ladder drawn is the one RC4 RULED** (master A.4.9 / H.28) — ladder only, fall-arrest
  deferred — **not** `fs_data`'s superseded `FS-6` / `FS-V7` *"no ladder specified"* text.
* **`WMS013` SHEET 13** — a **pure schedule sheet, no charts or graphs**: the whole
  **BILL OF QUANTITIES, all 38 measured items** under their five part headings with unit,
  quantity, rate and amount, plus the **MASTER CONSTRUCTION PROGRAMME** (18 summary
  activities), the **COST SUMMARY**, the **PART SUMMARY** and **WHAT THE REVISED BILL
  CARRIES**. *(Issued first with a programme bar chart and a cost chart; both were deleted
  the same day at **MEP2A** by instruction, which freed the drawing region for the full bill.
  No figure changed — master H.43.12.)*
  Long item descriptions are the bill's own, **trimmed to the column at a word break and
  marked with an ellipsis**; the bill governs. The **standby generator line carries no rate
  in WM3** and prints as **NOT PRICED** — it is in no total on the sheet and no rate is
  invented for it.
  **It presents `WM3`, the REVISED owner package of master H.15, final project
  cost `Rs 2,97,90,913` and programme R1, 224 working days 02-11-26 to 26-07-27.**
  **It is NOT `WM4`**, the later bill priced from the Maharashtra SSR 2022-23; the two are
  different revisions on different bases and both stand. Every amount, quantity, count, date
  and duration is read at build time from `WORKS MANAGEMENT/Cost/REVISED_*_RC1.csv` and
  `WORKS MANAGEMENT/Programme/REVISED_MASTER_CONSTRUCTION_SCHEDULE_R1.csv`.
* **`ARCH001` SHEET 01** — the underground level plan and the headhouse level plan at the
  owner's 1:100, both spanning the full 22000 box so that both escape shafts appear at every
  level, and the **ground level plan at 1:200** so the **sentry post is drawn at its site
  position X 32000 – 36000** instead of off position; plus room, door, opening, wall and
  level schedules.
* **`ARCH002` SHEET 02** — the sentry post's two floor plans at **1:75** (the external
  spiral stair stands 2150 clear of the west wall, and two plans with their stairs do not fit
  on A2 at 1:50), the south elevation with the shelter at **1:150 and the post at its true X
  across a break**, and a 1:20 detail of lintel L1, the wall ties and the 200 infill zone.

> **MEP3, 18 September 2026 — both sheets corrected against the Rev F CAD.** The four Rev F
> DXFs the two sheets redraw (`1_Underground_Level_Plan`, `2_Ground_Plan_Headhouse_Berm`,
> `3_` / `4_Sentry_Post_*_Plan`) were **parsed entity by entity**, and ten depiction errors on
> sheet 01 and nine on sheet 02 were fixed — **the two blast doors swing opposite ways**, the
> W5 fire door **D-05** is drawn, the decon airlock has its real 110 partitions with **STAGE 1
> at the south**, the stair is drawn as the plan draws it (flights Y 1800 – 3760, eight risers
> each — unchanged), the headhouse and entry doors **open outward** through walls broken at the
> opening, the berm toe is drawn, sentry-post door **D1 is in the WEST wall on both floors**,
> the spiral stair is at **(−1150, 1450)**, and the **300 projection with its 300 high pardi**
> is drawn for the first time. **No design value moved and no analysis was run.**
> Six places where the Rev F drawing and the master disagree are registered in
> **`arch_data.CAD_FINDINGS`** and master **H.44.4** — including **`MEP3-F1`** (no W8
> partition door is drawn: the 900 gap is permanent), **`MEP3-F3`** (no excavation line is
> drawn at all) and **`MEP3-F6`** (the sentry post ROOF projection stays `[NOT AVAILABLE]`).
> **`MEP3-F2a` is open:** `FLS012` routes escape route R1 across W5 at Y 2950, where there is
> no opening; `FLS012` was not altered.

> **The redraws change what the owner's two sheets PRINT, not what the project IS.**
> All **fourteen** corrected figures already existed in master Part A and each is cited to
> it. The register is `arch_data.CORRECTIONS` and master **H.43.4**; by instruction it is
> **not printed on the sheets**. The owner's originals are preserved as the uploaded
> `Project1.pdf` and are not altered.
>
> The principal correction is the **bay clear-width chain**. The owner's underground level
> plan reads `2900 / 3500 / 1800 / 1560 / 2400` then `2800 / 3400` — it omits bay 2, reverses
> bays 3 and 4, and gives bay 6 as 2400 and bay 8 as 3400. Master **A.3** gives
> **`2900 / 1800 / 3500 / 1800 / 1560 / 2000 / 2800 / 3000`**. The 22000 × 6200 envelope was
> already right and is unchanged.
>
> Two findings the redraw raised:
>
> * **`MEP2-F1`** — the owner's shared **DOOR SCH** lists thirteen marks and makes **every
>   one 900 × 2100 × 45**. Master **A.4.9** has five distinct openings at four sizes, and
>   **a 900 leaf will not fit either blast door**, which are **1200 × 2100** in the
>   Y 600 – 1800 openings in W6 and W7. `ARCH001` carries a new schedule keyed
>   `BD1 / BD2 / D1 / D2 / D3`.
> * **`MEP2-F2`** — the elevation's lowest level, labelled **"FDN LEVEL −6100"**, is the
>   **internal floor and top of mat**. The mat soffit is **(−)6.700** and the formation
>   **(−)6.800**; the sentry post's own founding level, **(−)2.000**, was not shown at all.
>   Also corrected: post ground floor **+0.450** (not 440), entry stairwell roof head
>   **+2.450** (not 3400), and the single "POST ROOF 7000" split into the **+6.700** roof
>   slab and the **+7.000** parapet top.

`arch_data.py` is the single value source for sheets 01 and 02 and `ops_data.py` for sheets
12 and 13. Both read the discipline modules (`mep_proj`, `sentry_data`, `fs_data`, the WM3
CSVs) and **write nothing back**; `a2_lib.py`, `sheet_data.py`, `sentry_data.py`,
`mep_data.py` and STR006 … STR009 / MEP010 / MEP011 are **untouched** by MEP2.

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

**MEP1 — the services sheets.  No design value moved and no analysis was run.**

| Sheet | Drawing No. | Title | Views |
|---|---|---|---|
| **SHEET 10** | **MEP010** | HVAC & EMP ZONE LAYOUT PLANS — UNDERGROUND LEVEL | 1 HVAC services layout plan (−)6.100 1:100 · 2 EMP zone layout plan (−)6.100 1:100 · 3 EMP Zone 2 enclosure, plan and section, 1:30 · 4 protective ventilation schematic, filter train and cascade |
| **SHEET 11** | **MEP011** | SEPTIC TANK, SOAK PIT & SUMP PIT — PLANS, SECTIONS & SCHEDULES | 1 sump pit SU-01 reinforcement plan 1:35 · 2 sump pit SU-01 sectional elevation A-A 1:35 · 3 septic tank ST-01 plan 1:30 · 4 septic tank ST-01 sectional elevation 1:30 · 5 soak pit SK-01 plan 1:50 · 6 soak pit SK-01 sectional elevation 1:50 · 7 key plan, external works location, 1:500 |

Each of the three drainage structures is drawn **twice — once in plan and once as a
cross-sectional elevation** — and the key plan puts all three at true project X and Y, with
the septic tank and the soak pits **east of the shelter and 10 400 north of the sentry post**.

> **By instruction these two sheets carry no design-basis panel, no calculation table, and no
> revision, phase or open-item text.** The gaps the project genuinely has are therefore
> recorded in master **H.42.4 / H.42.5** as `MEP1-F1` … `MEP1-F7`, not on the drawing. Two of
> them govern how the sheets may be read:
>
> * **`MEP1-F2` — ST-01, the soak-pit cover slabs and the inspection chambers have NO
>   reinforcement anywhere in this project.** No bar is drawn in them and none is scheduled;
>   the element schedule and title-block note 8 call them to the structural engineer's detail.
>   **The only reinforcement detailed on SHEET 11 is SU-01**, whose marks `F10`, `F11`, `F12`
>   and `F13` are read straight out of `rebar_data.py`.
> * **`MEP1-F7` — SHEET 11's key plan uses the RC4 EAST sentry-post placement**
>   (X 32000–36000, Y 600–5600), the one DR-A2 drew. `U4` is still open and SG2's northern
>   placement would put the post and the external works on the *same* side.
>
> Three more things the project does not hold are handled by **not drawing them**: `SH-1`, the
> fresh-air shaft, has no plan position and is shown as a **direction arrow only**; `SK-03` and
> `SK-04` have a reserved footprint and no size, and are drawn **dashed**; `ST-01` has no
> recorded level, so its section is drawn to local finished grade and carries **no level at
> all**. `PD-06`, `PD-11` and `PD-13` have scheduled lengths but no fixed route, so they are
> **not drawn on the key plan** — only `PD-16`, whose two ends the project fixes.

`mep_data.py` is the single value source for both sheets. It imports `hv_data`, `em_proj`,
`dr_data`, `mep_proj` and `rebar_data` and **writes nothing back to them**; `a2_lib.py`,
`sheet_data.py`, `sentry_data.py` and STR006 … STR009 are **not touched** by MEP1 — the
nineteen services layers the two sheets need are added to each document at build time rather
than to the shared `a2_lib.LAYERS` table, precisely so the structural sheets cannot move.

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
python3 s10_hvac_emp_layout.py        # -> DXF/MEP010_...dxf
python3 s11_drainage_structures.py    # -> DXF/MEP011_...dxf
python3 s01_arch_plans.py             # -> DXF/ARCH001_...dxf
python3 s02_sentry_arch.py            # -> DXF/ARCH002_...dxf
python3 s12_fire_plan.py              # -> DXF/FLS012_...dxf
python3 s13_works_management.py       # -> DXF/WMS013_...dxf
python3 qa_overlap.py ../DXF/*.dxf          # drafting QA, exits non-zero on a defect
python3 render_a2.py  ../DXF/*.dxf          # visual QA PNG
python3 render_pdf.py ../DXF/*.dxf          # true-size A2 vector PDF, 1:1
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
That is why all ten sheets pass the drafting QA with **zero text overlaps**.

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
* **MEP1:** `Presentation Sheets/DXF/` maps to *"STRUCTURAL - A2 presentation sheets"*, which
  MEP010 / MEP011 are not, so a **filename-prefix** entry `("Presentation Sheets/DXF/MEP",
  "MEP - A2 presentation sheets")` was inserted **ahead** of it — the lookup takes the first
  match — and the same label added to `make_index.ORDER`. Both drawing numbers added to
  `TITLE_OVERRIDE`.
* **MEP2:** the series now spans **four disciplines in one folder**, so `DISCIPLINE` matches
  each by **filename prefix** ahead of the generic folder prefix — `…/DXF/MEP`,
  `…/DXF/ARCH`, `…/DXF/FLS`, `…/DXF/WMS`, with `…/DXF/` left as the structural fallback.
  The three new labels were added to `make_index.ORDER` and all four drawing numbers to
  `TITLE_OVERRIDE`.
* All re-run. `DRAWING_INDEX.md` and `qa_index.json` now carry **90 drawings, 84 PASS**;
  **all ten A2 sheets report PASS**.

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
