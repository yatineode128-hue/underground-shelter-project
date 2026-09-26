# MASTER PROJECT REPORT — README

Package `Project Report/`, revision **PR3**, 26 September 2026 (master **H.44**).
Geometry **Rev F + M1** · design content current to **RC10** and **DR-A2** · drawing index current
to **MEP2A** (see `PR3-F2` below).
Status: **FOR REVIEW — NOT FOR CONSTRUCTION.**

## What this package is

`MASTER_PROJECT_REPORT.pdf` — **157 pages: the College of Military Engineering front matter, then
25 parts, 4 appendices and 56 drawn figures.** The drawings themselves are **not** bound into it:
**they are presented as a separate spiral-bound book of A3 pages**, and Part 14 carries their
index. The
project stated once, in the order an engineer would need it to reproduce the design: the physics
first, then the site and the ground, then the loads, then the calculations, then the openings, then
what is drawn, then the services, then how it is built — and then what is still open.

It is written to stand on its own. Everything needed to follow an element from a first-principles
load to a bar mark on a drawing is in it, with the clause of the Indian Standard that permits each
step named beside it.

**`master/MASTER_PROJECT_STATE.md` governs. Where the report and the master disagree, the master
is right.**

## What PR3 changed

**In the project: nothing.** No dimension, level, load, thickness, bar, quantity, rate, date or
float; no `.std`, no drawing, no QA output; no evidence tag. The main staircase is untouched.

**In the report:**

| | |
|---|---|
| **Front matter** | A black-and-gold **hard cover**, the existing **title page** (kept), then **certificate, approval sheet, declaration and acknowledgement**, drawn to the owner's photographs of a CME project report — `Scripts/report_frontmatter.py` |
| **Page numbers** | Covers unnumbered; certificate to list of figures **i, ii, iii …** (the certificate's *i* counted, not printed); **Part 1 is page 1**. The PDF's page labels match |
| **Part 14** | **Only the drawing index**, read at build time from `DRAWING QAQC/qa_index.json` (90 drawings, 17 groups), plus the statement that **the drawings are a separate spiral-bound book of A3 pages** and the caution that **every scale is true at the drawing's own sheet size, never on the A3 page** |
| **16.4.1** | The sump cover and `DR-A2-V1`, moved verbatim from the old 14.7 |
| **Counts** | The title page now counts its parts, appendices and figures from the source; the report's *"forty-four figures"* (PR2 actually had 57) now reads fifty-six |

### Filling in the front matter

**Every particular is in one block, `FM`, at the top of `Scripts/report_frontmatter.py`.** The
guides are the owner's. **These are NOT held and print as red bracketed placeholders — never
guessed:**

```
syndicate    the syndicate number                    e.g. "03"
members      rank and name of each member, in order  ["Capt ...", "Capt ...", ...]
leader       rank and name of the syndicate leader
leader_no    the leader's EODE number
date         month and year of submission            e.g. "Oct 2026"
degree_confirmed   True once the degree wording is ruled (PR3-F1)
```

The officials in the acknowledgement are thanked **by appointment**; add a name in `officials` to
print it. Then re-run the renderer — it lists every placeholder still on the pages.

**`PR3-F1` `[U]` — the degree.** Master A.1 says **"B.E. Civil Engineering"**; the CME pages
supplied as the model say **"Bachelor of Technology (Civil) … affiliated to the Jawaharlal Nehru
University, New Delhi"**. The pages print the CME wording **in red** until the owner rules.

**The crest** (`Assets/crest_gold.png`, `crest_colour.png`) is **traced from the owner's
photograph** by `Scripts/report_crest.py`; the colour version is a reconstruction. **Official
artwork is not held — drop it in under the same two filenames when available.**

## What PR2 changed in the project

**Nothing.** No dimension, level, load, thickness, bar, quantity, rate, date or float. No `.std`
file was touched, STAAD.Pro was not run, no drawing was edited, no generator was re-run, and **no
`[C]` / `[R]` / `[A]` / `[U]` / `[N]` tag was converted, downgraded or deleted.** The main
staircase is untouched. See master Part **H.37**.

## What PR2 changed in the report

**Voice.** PR1 told the project's story including its revision history. **PR2 states the design as
it stands, in the present tense, as though it had always been in this form.** Revision identifiers
are out of the narrative; every engineering *reason* is kept, because a reason is part of a design
and a revision number is not. The history is preserved in full in **Appendix D**, and the master's
Part H remains the ledger.

**Figures.** Fifty-seven, drawn by `Scripts/report_figures.py` from `GEOM` / `LEV` / `COVER`
constants in **project coordinates** — so a dimension changed there changes every figure that uses
it. Nothing is traced and no figure can drift from the geometry it is drawn from.

> **The figures are NOT the issued drawings.** No title block, no revision box, no bar mark; drawn
> at reading scale, not at a plotting scale; **never for setting out or fabrication.** They are
> also **not** reconstructions of the seven absent S-series sheets. The issued drawings are the 90
> DXF indexed in Part 14, bound separately as an A3 book.

**New and expanded parts.**

| Part | What |
|---|---|
| **4** | The full soil report — 11 trial pits, 6 soil samples, 6 rock cores, the meteorological record, and the site figures |
| **6.5** | **Concrete mix design, M35 and M30**, worked through the **IS 10262:2019 Annex A procedure step by step**, A-1 to A-11, as trial mixes |
| **12** | **Openings, blast doors, escape hatches and closures** — every hole through the protective boundary |
| **15–19** | HVAC and CBRN · water, sewage and drainage **with an operating procedure for peacetime, warning, closed mode and recovery** · electrical · **EMP protection, science and design** · fire, each a part in its own right |
| **21** | **Works management** — the bill, the cost estimate, the programme and the critical path, procurement, quality, resources and risk |
| **22** | **The environmental management plan** — derived from the project's own quantities, with every statutory gap named |

## Files

```
Project Report/
   MASTER_PROJECT_REPORT.pdf                     the deliverable
   Documentation/MASTER_PROJECT_REPORT.md        the report SOURCE -- edit this
   Documentation/00_README.md                    this file
   Scripts/report_render.py                      Markdown subset -> PDF
   Scripts/report_frontmatter.py                 hard cover + four formal pages;  FM
   Scripts/report_figures.py                     the drawn figures (56 used)
   Scripts/report_verify.py                      independent recomputation
   Scripts/report_crest.py                       one-off: crest images from the photo
   Assets/crest_source_photo.png                 the owner's photograph, cropped
   Assets/crest_gold.png, crest_colour.png       the crest as the pages use it
   Calculations/REPORT_VERIFICATION_OUTPUT.txt   its output
```

## Rebuild

```
python3 "Project Report/Scripts/report_verify.py"     # 565 checks
python3 "Project Report/Scripts/report_render.py"     # rebuild the PDF
python3 "Project Report/Scripts/report_crest.py"      # only to re-trace the crest
```

**Never edit the PDF.** Edit the Markdown (or `FM` for the front matter) and re-run the renderer.
The renderer adds no content of its own beyond the cover page, the running head and foot, the
automatically paginated contents list and the list of figures — and the front matter, and the
drawing index it reads from the QA tool.

Directives in the source:

```
<!-- FIG: fig_name -->     a numbered, captioned figure, in document order
<!-- LOF -->               the list of figures
<!-- PAGEBREAK -->         a forced page break
<!-- HARDCOVER -->         the black hard cover
<!-- COVER -->             the title page
<!-- FRONTMATTER -->       certificate, approval sheet, declaration, acknowledgement
<!-- DRAWING INDEX -->     the drawing index, from DRAWING QAQC/qa_index.json
```

**Dependency:** `reportlab` (plus Pillow, which reportlab installs), which is already the project's PDF toolchain —
`WORKS MANAGEMENT/Scripts/wm_programme_pdf.py` and `wm_handout_pdf.py` both use it.
**Fonts:** GNU FreeFont, the only family on this machine carrying every glyph the report uses
(Greek, sub- and superscripts, mathematics and arrows) in all four styles. Any character a face
cannot draw is substituted and **reported**, never silently dropped.

## The two gates

**Numbers.** `report_verify.py` recomputes **565** of the figures the report reproduces, from their
own inputs, with the formulas written out again rather than copied. PR3 replaced its two
hard-coded *"80 drawings"* checks with eight read from the QA tool's `qa_index.json`.

```
PASS                            559
KNOWN / RECORDED difference       6
UNEXPLAINED FAIL                  0
```

> **A PASS means the printed number follows from the printed inputs.** It is **not** a design
> check and **not** an analysis. It does not re-derive engineering judgement, it cannot run STAAD,
> and it cannot tell you whether an assumption is true.

**Figures.** `report_figures.check_all()` walks every drawing and reports any line, rectangle,
circle, polygon **or string** that falls outside its own frame or runs past the text measure —
because reportlab does not clip, so anything drawn outside a figure silently bleeds onto whatever
follows it.

```
python3 -c "import report_figures as R; print(len(R.check_all()))"   # 6 -- see PR3-F4
```

> **`PR3-F4`: the gate returns 6, not the 0 PR2 recorded** — six strings past the text measure in
> `fig_critical_path`, `fig_penetrations` and `fig_regimes`, on the unchanged `report_figures.py`,
> under reportlab 4.5.1 and 5.0.1 alike. **Nothing bleeds on the page**: each of the three is drawn
> wider than the measure and is scaled to the text width when placed. Recorded, not corrected.

## PR3's other findings — recorded, not corrected

| Ref | Finding |
|---|---|
| **`PR3-F2`** | **The report is not current beyond RC10 / DR-A2, except Part 14.** WM4, SR1/SR2, MEP1 and MEP2 post-date PR2 and are not in Parts 1–13 or 15–25 — the title page says so |
| **`PR3-F3`** | **Appendix B cites "Parts 14.1.4, 14.2, 14.3, 14.4, 14.5" for five services clauses** — PR1's numbering, never updated by PR2. They now point at the drawing index |

## The six differences — none corrected

Master rule M.11 forbids editing a recorded value away.

| Ref | Where | Computed | Printed |
|---|---|---|---|
| **`PR1-F1`** | master `A.7.8`, box wall shear stress | **0.0506 N/mm²** | 0.063 N/mm² |
| **`PR1-F2`** | master `B.8.7`, footing F1 ULS e<sub>u</sub> and q<sub>u,max</sub> | **0.159 m**, **186.0 kPa** | 0.128 m, 190.0 kPa |
| **`PR2-F1`** | the programme's working-day count | **325 days** | 326 days |
| **`PR2-F2`** | the honeycomb panel's margin, with the array counted | **+8.3 dB** | +53 dB |

`PR1-F1` and `PR1-F2` are figures quoted to show that something is negligible or non-governing,
and **nothing downstream is sensitive to either** — which is why both survived every previous
pass. `PR2-F1` is a single day and is far more likely a property of a scheduling tool's activity
calendar than an error; **no date, duration or float moves on it.** `PR2-F2` is the only one of
the four that changes what somebody has to do: 133 dB is the attenuation of **one** honeycomb cell,
a panel is tens of thousands of them in one screen, and the array correction takes the margin from
+53 dB to +8.3 dB. **The panel still passes; what changes is a procurement clause, not a design
value.** All four are offered to the project owner as ruling items, not asserted as errors.

A fourth difference — the owner's cost summary, ₹ 1 00 000 — is **already recorded as `R-14`**
(master H.13). Reproducing a known finding independently is the outcome a check like this is for.

**`PR1-F3`:** `CONSOLIDATED_PROJECT_REPORT.md` (repository root) is stale on the open-item and
assumption counts and predates RC4 to RC10 and DR-A2. **It is not edited** — it is an artefact of
exactly the class `RC10` exists to register.

## The main staircase

**24R @ 170.8333 · 280 tread · 3 flights × 8 · total rise 4 100 · 1 200 wide · 200 well · 200
waist · headroom 2 533.** This package reproduces it and **changes nothing.**
