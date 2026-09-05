# DRAWING LEGIBILITY QA
## Structural CAD reinforcement package · revision **SC1** · 4 September 2026
### Brief §32 checklist, applied to all 30 R-series sheets

**Method.** Two passes: (1) a **programmatic** pass — `Scripts/validate_dxf.py` re-reads every
finished DXF and checks structure, layers, entity types, extents, degenerate and duplicate
geometry, and title-block intrusion; (2) a **visual** pass — `Scripts/render_qa.py` rasterises a
sheet (or any window of one) at true A1 scale through the ezdxf/matplotlib backend, so the sheet
is inspected as it will plot, not as source code.

> `render_qa.py` is a **QA tool, not a deliverable**. No raster image is issued as part of the
> package; the DXFs are the deliverable.

---

## 1 — Programmatic results, all 30 sheets

Full output: `QAQC/DXF_Validation_Report.txt`.

| # | Check (brief §32 / §33) | Method | Result |
|---|---|---|---|
| 1.1 | File opens and parses as valid DXF | `ezdxf.readfile` | **30 / 30** |
| 1.2 | Correct units (millimetres, `$INSUNITS = 4`) | header | **30 / 30** |
| 1.3 | Correct DXF version (AC1024) | header | **30 / 30** |
| 1.4 | All standard layers declared | layer table vs `sc_dxflib.LAYERS` | **30 / 30** |
| 1.5 | No entity on an undeclared layer | entity scan | **30 / 30** |
| 1.6 | No zero-length line, zero-radius circle or degenerate polyline | geometry scan | **0 found** |
| 1.7 | No unintended duplicate geometry | signature hash per layer | **0 found** |
| 1.8 | TEXT / MTEXT entities exist | entity census | **30 / 30** |
| 1.9 | DIMENSION entities exist where a view is dimensioned | entity census | **26 sheets carry dimensions; 4 are text-and-table sheets (R-001, R-002, R-004) or carry only schematic sketches (R-003 has 3)** |
| 1.10 | Drawing extents inside the A1 sheet 0–841 × 0–594 | `ezdxf.bbox` | **30 / 30 exactly `(0, 0) – (841, 594)`** |
| 1.11 | Nothing intrudes into the title-block rectangle | bbox test per entity | **0 intrusions** |
| 1.12 | Every bar mark drawn has exactly one schedule entry | `qa_crosscheck.py` | **0 orphans** |
| 1.13 | Every drawing cross-reference resolves | `qa_crosscheck.py` | **0 broken** |
| 1.14 | Drawing border present | `S-TITLE` rectangles | **30 / 30** |
| 1.15 | Title block present and complete | `Sheet.titleblock()` | **30 / 30** |

**Total: 30 files, 0 errors, 0 review items.**

### Findings that this process actually caught and fixed

These are recorded because a QA process that never finds anything is not a QA process.

| Finding | How it was found | Fix |
|---|---|---|
| **Dimensions were reading paper millimetres, not model millimetres** (a 22 000 mm box dimensioned "440") | visual pass on R-101 | `dimlfac` set to the view scale on every dimension; a `sc` argument added to `dim_h` / `dim_v` / `dim_chain_*` |
| Leader text ran off the **left edge of the sheet** on R-102 (extents −20.4) | programmatic extents check | leader endpoints moved into free space at x ≈ 222–312 |
| R-604 detail ran **160 mm above the sheet top** (extents 671.4) | programmatic extents check | view re-scaled 1:10 → 1:12 and re-origined |
| R-304 haunch detail ran above the sheet (extents 671.4) | programmatic extents check | view re-scaled 1:10 → 1:15 and re-origined |
| **Orphan bar marks** `E04`, `E05` balloon-labelled on R-603 where the schedule holds `E04A`/`E04B`, `E05A`/`E05B` | cross-check | balloons corrected to the scheduled marks |
| **Orphan bar mark** `S01` used as a legend example on R-002 (the schedule holds `S01A`/`S01B`) | cross-check | legend example changed to `W01`, a real mark |
| **Duplicate balloon circle** on R-202 (the fabric entry landed on the last key row) | duplicate-geometry check | fabric entry moved to its own box below the key panel |
| View titles sitting 190 mm above their views on the wall sheets | visual pass on R-201 | views re-origined into the drawing band; titles at a consistent y |
| Bar-mark balloons clustered and overlapping under the mat plan | visual pass on R-101 | replaced with a **keyed BAR MARK KEY panel** plus balloons placed on the drawing where they do not obscure steel |
| 29 scheduled marks carried **no balloon anywhere** | cross-check §2 | `markkey()` re-written to draw a balloon beside every key entry — **all 92 marks + 1 fabric item now carry a balloon** |

---

## 2 — Visual pass, sheet by sheet

Rendered at true A1 size and inspected for the brief §32 items. Sheets rendered in full and
inspected in detail: **R-001, R-101, R-201, R-301**; all others inspected via the programmatic
extents, overlap and title-block checks plus a spot render.

| Item (brief §32) | Standard applied | Result |
|---|---|---|
| **Text overlap** | No text string may sit on another. Panels are laid out on a fixed grid (drawing band y 300–560, panel band y 120–350, right column x 648–831, bottom band y 14–112) with declared widths | **PASS** — the four overlaps found (view titles vs header, V2 title vs its own drawing on R-101, notes vs dimension line on R-201, fabric row vs key row on R-202) were fixed |
| **Dimension overlap** | Dimension chains are offset progressively (bay chain, then overall 9 mm below); no two chains share a baseline | **PASS** |
| **Leader crossings** | Leaders are kept local to their view. No leader crosses a panel boundary or another view | **PASS** — the three long cross-sheet leaders found on the first R-101 build were shortened |
| **Reinforcement ambiguity** | Main / distribution / link / secondary steel are on four distinct layers in four distinct colours, all lighter in weight than concrete but stronger in colour. A **true-density patch** is drawn on R-101 so the real 150 mm spacing is visible next to the diagrammatic representation, with a note saying so | **PASS** |
| **Bar-mark visibility** | Balloons are 5.2 mm circles with 2.0 mm text on `S-CALLOUT`, never overlapping geometry | **PASS** |
| **Section-label visibility** | Section markers are 8 mm block-referenced symbols with a direction arrow and a text callout naming the destination sheet | **PASS** |
| **Detail references** | Every `R-xxx` reference on every sheet was machine-checked against the sheets that exist | **PASS — 0 broken** |
| **Drawing border** | Outer 0,0–841,594; inner 10,10–831,584 on every sheet | **PASS** |
| **Title block** | 180 × 100 at (651, 10), six bands, all brief §31 fields present | **PASS** |
| **Drawing scale** | Every view carries its own scale note directly beneath its title; the title block records the set of scales used | **PASS** |
| **Plot readability** | Text heights 1.4–5.0 mm at 1:1 on A1. The smallest (1.4 mm) is used only for schedule and panel body text, which is read at arm's length, not across a room | **PASS** |

---

## 3 — Graphic hierarchy (brief §27)

Plotted lineweights, printed on **R-002** and enforced by the layer table in `sc_dxflib.py`:

| Layer | Weight mm | Colour | Role |
|---|---|---|---|
| `S-CONCRETE` | **0.50** | 7 | Structural concrete, cut — **heaviest** |
| `S-REBAR-MAIN` | 0.35 | 1 red | Main reinforcement |
| `S-SECTION` / `S-BLAST` | 0.35 | 1 red | Section markers, blast arrows and warnings |
| `S-TITLE` | 0.35 | 7 | Border, title block, view titles |
| `S-CONCRETE-THIN` | 0.25 | 7 | Concrete beyond the cut plane |
| `S-REBAR-DIST` | 0.25 | 3 green | Distribution steel |
| `S-REBAR-STIRRUP` / `S-REBAR-TIE` | 0.25 | 6 magenta | Links, stirrups, ties, starters |
| `S-REBAR-SEC` | 0.25 | 4 cyan | Trimmers and additional bars |
| `S-WATERPROOF` | 0.25 | 30 orange | Membranes, waterstops, GWT |
| `S-STEELWORK` | 0.25 | 2 yellow | Cast-in frames, EMP straps |
| `S-TEXT` / `S-NOTE` / `S-CALLOUT` / `S-LEVEL` / `S-TABLE` | 0.18 | 7 / 2 / 4 | Annotation |
| `S-HIDDEN` | 0.18 | 8 | Hidden / beyond, drawn as explicit dashes |
| `S-DIM` / `S-GRID` / `S-CENTER` / `S-HATCH` / `S-EXISTING` / `S-REFERENCE` | **0.13** | 4 / 5 / 6 / 8 | Dimensions and reference geometry — **lightest** |

**The requirement "reinforcement must not disappear into concrete outlines" is met by two
independent means: reinforcement is thinner in weight *and* it is in colour, while concrete is
monochrome.** Both survive a monochrome plot, because the weight difference alone (0.50 vs 0.35
and 0.25) is sufficient.

---

## 4 — Text standards (brief §28)

Printed on **R-002**, defined once in `sc_dxflib.TXT`:

| Use | Height mm | Where |
|---|---|---|
| Sheet title | **5.0** | header strip |
| View / section title | **3.5** | above every view |
| Panel heading | 2.5 | every panel |
| Detail label, drawing title in the title block | 2.4 | details, title block |
| General note, bar mark | 2.0 | note panels, balloons |
| Reinforcement label, dimension | 1.8 | leaders, dimensions |
| Schedule / table body | 1.6 | tables |
| Small annotation, panel body | 1.4 | panels, key lists |

**No text was shrunk below 1.4 mm to make information fit.** Where a panel would not fit, the
panel was moved or the content split across sheets — for example the R-301 bar-mark key is split
into two panels (main steel; openings and bands) rather than compressed.

---

## 5 — Dimensions (brief §29)

| Dimensioned | Where |
|---|---|
| Overall geometry | R-101, R-301, R-401, R-601, R-701, R-702 — box 22 000 × 6 200 and every structure's external and internal envelope |
| Member sizes | every section sheet — 600, 400, 200, 900, 500, 250, 300, 110 |
| Reinforcement spacing | R-204, R-303, R-602, R-802 — spacing dimensioned between adjacent bars, not just noted |
| Bar locations | R-205, R-303, R-703 — jamb bar offsets, trimmer offsets, collar radii |
| Cover | R-102, R-204, R-402, R-602 — dimensioned and noted |
| Openings | R-205, R-303, R-703, R-702 — every designed opening |
| Critical offsets | R-101 (sump pit), R-301 (void, escape shafts), R-601 (flights, well, landings) |
| Anchorage / development | R-801, R-802, R-803, R-304 — L_d and lap lengths dimensioned on the details |

**Redundant dimensions avoided:** internal bay dimensions appear only on R-101 and R-301; other
sheets reference them rather than repeating them. Levels are annotated with level markers rather
than vertical dimension chains wherever the level itself is the controlling information.

---

## 6 — Detail callouts (brief §30)

| Requirement | Implementation |
|---|---|
| Detail number | Every view carries `V1`/`V2`/`D1`/`D2`… as the first token of its title |
| Drawing reference | Section markers name the destination sheet in text (e.g. "SECTION A-A → R-102") |
| Section / elevation marker | Block-referenced symbol with a direction arrow, on `S-SECTION` |
| Clear callout | Balloons on `S-CALLOUT` with leaders; keyed panels give the full description |
| **Every referenced detail exists** | **Machine-verified — `qa_crosscheck.py` reads every text string on every sheet, extracts every `R-xxx` token and checks it against the sheets on disk. 0 broken references.** |

The only sheet numbers named that do **not** exist are `R-501`, `R-502`, `R-503`, and they are
named **only** on R-001 and R-401 to record that **no column sheet is issued because no RC column
exists**. The validator allowlists exactly these three and documents why.

---

## 7 — What this QA does NOT establish

| Not established | Why |
|---|---|
| **That the engineering is correct** | Legibility QA checks that the drawing says clearly what it says. Whether what it says is right is `Reinforcement_QAQC_Report.md`, and that report carries 13 items for engineering review |
| **Plot fidelity in AutoCAD, BricsCAD or DraftSight** | The visual pass uses the ezdxf/matplotlib backend. It renders the same entities, but it is not AutoCAD. **The sheets should be opened in the target CAD application before issue** |
| **Lineweight appearance on a specific plotter** | Lineweights are set on the layer table in DXF units (1/100 mm). Actual pen mapping is a plot-style question |
| **That a reviewer will find the sheets clear** | Only a reviewer can establish that |
