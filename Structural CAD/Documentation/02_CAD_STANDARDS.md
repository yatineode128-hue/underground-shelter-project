# CAD STANDARDS
## Structural CAD reinforcement package · revision **SC1** · 4 September 2026

---

## 1 — SHEET STANDARD

```
SHEET SIZE        A1, 841 x 594 mm, DRAWN IN PAPER MILLIMETRES, PLOT 1:1
DXF FORMAT        AutoCAD 2010 (AC1024) ASCII
UNITS             $INSUNITS = 4 (millimetres), $LUNITS = 2, $MEASUREMENT = 1
BORDER            outer 0,0 - 841,594   inner 10,10 - 831,584
TITLE BLOCK       180 x 100 mm, bottom right, at x0 = 651, y0 = 10
HEADER STRIP      y >= 562: package identity, sheet number and title, scope exclusion,
                  the "no STAAD result" statement, and the sheet's open-item flags
VIEW MAPPING      paper = view_origin + model / scale.  Every view has its own origin and
                  scale and carries a scale note beneath its title.
DIMENSIONS        geometry is drawn in paper mm, so every DIMENSION carries dimlfac = the
                  view scale.  DIMENSION TEXT THEREFORE READS MODEL MILLIMETRES.
```

### Standard layout grid

| Zone | Extent (paper mm) | Use |
|---|---|---|
| Header strip | y 562 – 584 | identity, exclusions, flags |
| Drawing band | y 300 – 560, x 16 – 640 | principal views |
| Second band | y 120 – 350, x 16 – 640 | secondary views and panels |
| Right column | x 648 – 831, y 118 – 556 | note panels, tables |
| Bottom band | x 16 – 643, y 14 – 112 | wide panels, schedule extracts |
| Title block | x 651 – 831, y 10 – 110 | title block |

---

## 2 — LAYER SYSTEM AND MAPPING

### Declared deviation **X2**

The brief §26 requires an `S-*` layer system. Master E.3.2 fixes a different 22-layer table
(`CONC`, `REINF-MAIN`, …) used by output sheets S-01…S-08.

**Resolution: the R-series uses the brief's `S-*` system, and the mapping below is issued so the
two sets remain reconcilable. Sheets S-01…S-08 and the ten Rev F input drawings are untouched.**

The mapping is also **printed on drawing R-002**, so it travels with the drawings.

| `S-*` layer (this package) | ACI | Lineweight mm | Purpose | Master E.3.2 equivalent |
|---|---|---|---|---|
| `S-CONCRETE` | 7 | **0.50** | Structural concrete outlines (cut) | `CONC` |
| `S-CONCRETE-THIN` | 7 | 0.25 | Concrete beyond the cut plane | `CONC` |
| `S-HIDDEN` | 8 | 0.18 | Concrete / features beyond, hidden | `CONC-HIDDEN` |
| `S-REBAR-MAIN` | 1 | 0.35 | Main reinforcement | `REINF-MAIN` |
| `S-REBAR-DIST` | 3 | 0.25 | Distribution reinforcement | `REINF-DIST` |
| `S-REBAR-STIRRUP` | 6 | 0.25 | Links and stirrups | `REINF-LINK` |
| `S-REBAR-TIE` | 6 | 0.25 | Ties, cross-ties, starters | `REINF-LINK` |
| `S-REBAR-SEC` | 4 | 0.25 | Trimmers, secondary and additional bars | `REINF-SEC` |
| `S-DIM` | 4 | 0.13 | Dimensions | `DIM` |
| `S-TEXT` | 7 | 0.18 | General annotation | `TEXT` |
| `S-NOTE` | 7 | 0.18 | Note panels | `NOTES` |
| `S-CALLOUT` | 2 | 0.18 | Bar-mark balloons and leaders | `DIM` |
| `S-SECTION` | 1 | 0.35 | Section and detail markers | `DIM` |
| `S-GRID` | 5 | 0.13 | Grid lines and bubbles | `GRID` |
| `S-CENTER` | 6 | 0.13 | Centrelines | `CENTRELINE` |
| `S-HATCH` | 8 | 0.13 | Section hatch | `HATCH` |
| `S-TITLE` | 7 | 0.35 | Border, title block, view titles | `TITLEBLOCK` |
| `S-EXISTING` | 8 | 0.13 | Soil, rock, berm, cover layers | `SOIL` |
| `S-REFERENCE` | 8 | 0.13 | Reference geometry, extents | `CONC-HIDDEN` |
| `S-WATERPROOF` | 30 | 0.25 | Membranes, waterstops, GWT | `WATERPROOF` |
| `S-STEELWORK` | 2 | 0.25 | Cast-in frames, EMP straps, steel items | `STEELWORK` |
| `S-LEVEL` | 4 | 0.18 | Level markers | `LEVELS` |
| `S-TABLE` | 7 | 0.18 | Tables and schedules | `TABLE` |
| `S-BLAST` | 1 | 0.35 | Blast arrows, findings, warnings | `BLAST` |

**24 layers, declared identically in every sheet.** All are on, thawed and unlocked, linetype
`CONTINUOUS`. **Dashed and chain lines are drawn as explicit segments**, not by linetype — the
same compatibility decision the master's own output set made.

---

## 3 — GRAPHIC HIERARCHY

Heaviest to lightest, so that reinforcement can never disappear into a concrete outline:

```
0.50   S-CONCRETE                       structural concrete, cut
0.35   S-REBAR-MAIN  S-SECTION  S-BLAST  S-TITLE
0.25   S-CONCRETE-THIN  S-REBAR-DIST  S-REBAR-STIRRUP  S-REBAR-TIE
       S-REBAR-SEC  S-WATERPROOF  S-STEELWORK
0.18   S-TEXT  S-NOTE  S-CALLOUT  S-LEVEL  S-TABLE  S-HIDDEN
0.13   S-DIM  S-GRID  S-CENTER  S-HATCH  S-EXISTING  S-REFERENCE
```

**The separation is doubly redundant: reinforcement is both lighter in weight and in colour,
while concrete is monochrome. The distinction therefore survives a monochrome plot.**

---

## 4 — TEXT STANDARDS

Defined once in `Scripts/sc_dxflib.py` as `TXT`, printed on **R-002**.

| Use | Height mm |
|---|---|
| Sheet title | 5.0 |
| View / section title | 3.5 |
| Panel heading | 2.5 |
| Detail label, drawing title in the title block | 2.4 |
| General note, bar mark | 2.0 |
| Reinforcement label, dimension | 1.8 |
| Schedule / table body | 1.6 |
| Small annotation, panel body | 1.4 |

Text style `OpenSans` throughout (created by `ezdxf.new(setup=True)`).
**No text is below 1.4 mm.** Where content would not fit, the panel was moved or split.

---

## 5 — DIMENSION STYLES

| Style | Text | Arrow | Use |
|---|---|---|---|
| `SC-DIM` | 1.8 | 1.6 | all normal dimensioning |
| `SC-DIM-S` | 1.4 | 1.2 | small sketches (R-003 bar shapes) |

Common settings: `dimtad = 1` (text above the line), `dimdec = 0` (whole millimetres),
`dimblk = ARCHTICK`, extension 1.2 beyond / 1.0 offset, gap 0.8, colour ACI 4,
`dimtih = dimtoh = 0` (text aligned with the dimension line).

> **`dimlfac` is set on every dimension to the view scale.** Because geometry is drawn in paper
> millimetres, a dimension between two paper points would otherwise report the *paper* distance.
> With `dimlfac = 50` on a 1:50 view, the 440 mm paper measurement reads **22000**. This was
> caught by the visual QA pass and is now enforced through the `sc` argument on every dimension
> helper.

---

## 6 — SYMBOL BLOCKS

Defined once per sheet in `Sheet._blocks()` and inserted as `INSERT` references:

| Block | Geometry | Use |
|---|---|---|
| `BARMARK` | circle r 3.2 | bar-mark balloon |
| `SECMARK` | circle r 4.0 + diameter line | section / detail marker |
| `LEVELMK` | filled triangle | level marker |
| `NORTH` | arrow in a circle r 12 | north point |

**154 block references across the package.**

---

## 7 — BAR-MARK SYSTEM

**Prefixes** (brief §22, extended and documented):

| Prefix | Element group | Marks |
|---|---|---|
| **F** | Foundations — mat, starters, sump pit | F01 – F13 |
| **W** | Walls — perimeter, W5, W6/W7, openings, partitions | W01 – W18 |
| **S** | Slab — pressure slab and its openings | S01A – S16 |
| **B** | Beam-type elements — headers | B01 – B03 |
| **ST** | Main staircase | ST01 – ST06 |
| **H** | Headhouse | H01A – H10 |
| **E** | Entrance / covered entry stairwell | E01 – E12 |
| **C** | **RESERVED AND DELIBERATELY UNUSED — no RC column exists** | — |
| **T** | **RESERVED AND UNUSED** | — |

**Suffix letters** (`S01A`, `S01B`, `H04A`, `E04B`…) are used where one bar *type* occurs at more
than one **cut length**, so that the rule **"one mark = one schedule row = one (diameter, shape,
cut length)"** holds without exception.

**92 unique marks + 1 fabric item.** Uniqueness is asserted in code
(`rebar_data.build_marks()`), and both directions are machine-verified by
`Scripts/qa_crosscheck.py` against the finished DXFs:

* **no mark drawn without a schedule entry** — 0 orphans;
* **no scheduled mark undrawn** — all 92 + 1 carry a balloon.

---

## 8 — BAR SHAPE CODES

Only the four **unambiguous** BS 8666 codes are used. Everything else is coded **99 — other,
fully dimensioned sketch**, because no copy of BS 8666, SP 34 or IS 2502 is held in the workspace
and a shape code will not be guessed.

| Code | Description | Cut length |
|---|---|---|
| **00** | Straight | A |
| **11** | One 90° bend (L-bar) | A + B |
| **21** | Two 90° bends (U / crank) | A + B + C |
| **51** | Closed link, 135° hooks | 2(A + B) + 2 × 10 φ |
| **99** | Other — dimensioned sketch on the drawing | Σ legs |

---

## 9 — DECLARED PROJECT RULES

| # | Rule | Status |
|---|---|---|
| **PBR-1** | Cut length = Σ scheduled leg dimensions, **no bend deduction**; links add 2 × 10 φ for 135° hooks. Conservative by ≈ 2 φ per 90° bend. Bend deductions to BS 8666 Table 3 to be applied by the fabricator on the approved schedule | **[ASSUMED]** — no bar-bending standard is in the workspace |
| **PBR-2** | A "4-legged link @ s" is scheduled as **two** closed links per node on an s × s grid; a "2-legged link @ s" as **one** | project convention |
| **PBR-3** | Openings (stair void, escape shafts) are **deducted zone by zone**, not by a blanket percentage | project convention |
| **P-1** | Stock bar **12 000 mm**; longer runs split into equal pieces with 50 φ laps added, staggered | **[ASSUMED]** |
| **P-3** | Bar-mark prefixes as §7; **C and T reserved and unused** | project convention |
| **P-4** | Where master Part F gives an arrangement but not an extent, the extent is the full element between support faces plus anchorage L_d | project convention |

---

## 10 — DECLARED DEVIATIONS FROM THE MASTER STANDARD

| # | Item | Master | This package | Reason |
|---|---|---|---|---|
| **X1** | DXF format | E.3.1 **R12 ASCII** | **AC1024** | R12 does not carry usable DIMENSION / MTEXT / HATCH / LEADER entities, which brief §25 requires |
| **X2** | Layer names | E.3.2 22-layer table | brief's **`S-*`** system | required by brief §26; **mapping issued above and on R-002** |
| **X4** | Bar bending standard | Part G names BS 8666 + SP 34 | **PBR-1** | neither document, nor IS 2502, is in the workspace |
| **X5** | Title-block size | E.3.1 180 × 62 | **180 × 100**, same position | brief §31 requires more fields than 62 mm holds legibly |

**Sheets S-01…S-08 and the ten Rev F input drawings are not modified by this package.**

---

## 11 — REGENERATION

The DXFs are **build artefacts**. Edit the source, never the DXF (master rule M.12).

```
python3 "Structural CAD/Scripts/build_all.py"
```

runs, in order: `verify_partB.py` → `make_schedules.py` → `g00`…`g08` →
`qa_crosscheck.py` → `validate_dxf.py`.

| To change | Edit |
|---|---|
| A dimension, level, thickness or load | `Scripts/sc_proj.py` |
| A bar diameter, spacing, count or mark | `Scripts/rebar_data.py` |
| A layer, lineweight, text height or the title block | `Scripts/sc_dxflib.py` |
| A shared view (box plan, wall section, panels) | `Scripts/sc_views.py` |
| One sheet's content | the matching `gNN_*.py` |
| A design equation | `Scripts/rc_calc.py` |

**Because the schedules and the drawing annotation are both generated from `rebar_data.py`,
they cannot drift apart.**

**Dependency:** `ezdxf` (`pip install ezdxf`). `matplotlib` is needed only for the optional
visual QA renderer `render_qa.py`. Both were installed into this session; **neither is vendored
into the repository.**
