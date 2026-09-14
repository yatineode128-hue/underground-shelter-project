# MASTER PROJECT REPORT — README

Package `Project Report/`, revision **PR2**, 13 September 2026.
Geometry **Rev F + M1** · current to **RC10** and **DR-A2**.
Status: **FOR REVIEW — NOT FOR CONSTRUCTION.**

## What this package is

`MASTER_PROJECT_REPORT.pdf` — **137 pages, 25 parts, 4 appendices and 44 drawn figures.** The
project stated once, in the order an engineer would need it to reproduce the design: the physics
first, then the site and the ground, then the loads, then the calculations, then the openings, then
what is drawn, then the services, then how it is built — and then what is still open.

It is written to stand on its own. Everything needed to follow an element from a first-principles
load to a bar mark on a drawing is in it, with the clause of the Indian Standard that permits each
step named beside it.

**`master/MASTER_PROJECT_STATE.md` governs. Where the report and the master disagree, the master
is right.**

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

**Figures.** Forty-four, drawn by `Scripts/report_figures.py` from `GEOM` / `LEV` / `COVER`
constants in **project coordinates** — so a dimension changed there changes every figure that uses
it. Nothing is traced and no figure can drift from the geometry it is drawn from.

> **The figures are NOT the issued drawings.** No title block, no revision box, no bar mark; drawn
> at reading scale, not at a plotting scale; **never for setting out or fabrication.** They are
> also **not** reconstructions of the seven absent S-series sheets. The issued package is the 80
> DXF of Part 14.

**New and expanded parts.**

| Part | What |
|---|---|
| **4** | The full soil report — 11 trial pits, 6 soil samples, 6 rock cores, the meteorological record, and the site figures |
| **6.5** | **Concrete mix design, M35 and M30**, to the IS 10262 method, as trial mixes |
| **12** | **Openings, blast doors, escape hatches and closures** — every hole through the protective boundary |
| **15–19** | HVAC and CBRN · water, sewage and drainage · electrical · EMP · fire, each a part in its own right |
| **21** | **Works management** — the bill, the cost estimate, the programme and the critical path, procurement, quality, resources and risk |
| **22** | **The environmental management plan** — derived from the project's own quantities, with every statutory gap named |

## Files

```
Project Report/
   MASTER_PROJECT_REPORT.pdf                     the deliverable
   Documentation/MASTER_PROJECT_REPORT.md        the report SOURCE -- edit this
   Documentation/00_README.md                    this file
   Scripts/report_render.py                      Markdown subset -> PDF
   Scripts/report_figures.py                     the 44 drawn figures
   Scripts/report_verify.py                      independent recomputation
   Calculations/REPORT_VERIFICATION_OUTPUT.txt   its output
```

## Rebuild

```
python3 "Project Report/Scripts/report_verify.py"     # 543 checks
python3 "Project Report/Scripts/report_render.py"     # rebuild the PDF
```

**Never edit the PDF.** Edit the Markdown and re-run the renderer. The renderer adds no content of
its own beyond the cover page, the running head and foot, the automatically paginated contents list
and the list of figures.

Three directives place figures and breaks in the source:

```
<!-- FIG: fig_name -->   a numbered, captioned figure, in document order
<!-- LOF -->             the list of figures
<!-- PAGEBREAK -->       a forced page break
```

**Dependency:** `reportlab`, which is already the project's PDF toolchain —
`WORKS MANAGEMENT/Scripts/wm_programme_pdf.py` and `wm_handout_pdf.py` both use it.
**Fonts:** GNU FreeFont, the only family on this machine carrying every glyph the report uses
(Greek, sub- and superscripts, mathematics and arrows) in all four styles. Any character a face
cannot draw is substituted and **reported**, never silently dropped.

## The two gates

**Numbers.** `report_verify.py` recomputes **543** of the figures the report reproduces, from their
own inputs, with the formulas written out again rather than copied.

```
PASS                            538
KNOWN / RECORDED difference       5
UNEXPLAINED FAIL                  0
```

> **A PASS means the printed number follows from the printed inputs.** It is **not** a design
> check and **not** an analysis. It does not re-derive engineering judgement, it cannot run STAAD,
> and it cannot tell you whether an assumption is true.

**Figures.** `report_figures.check_all()` walks every drawing and reports any line, rectangle,
circle, polygon **or string** that falls outside its own frame or runs past the text measure —
because reportlab does not clip, so anything drawn outside a figure silently bleeds onto whatever
follows it. **The gate is zero, and it is met.**

```
python3 -c "import report_figures as R; print(len(R.check_all()))"   # 0
```

## The five differences — none corrected

Master rule M.11 forbids editing a recorded value away.

| Ref | Where | Computed | Printed |
|---|---|---|---|
| **`PR1-F1`** | master `A.7.8`, box wall shear stress | **0.0506 N/mm²** | 0.063 N/mm² |
| **`PR1-F2`** | master `B.8.7`, footing F1 ULS e<sub>u</sub> and q<sub>u,max</sub> | **0.159 m**, **186.0 kPa** | 0.128 m, 190.0 kPa |
| **`PR2-F1`** | the programme's working-day count | **325 days** | 326 days |

`PR1-F1` and `PR1-F2` are figures quoted to show that something is negligible or non-governing,
and **nothing downstream is sensitive to either** — which is why both survived every previous
pass. `PR2-F1` is a single day and is far more likely a property of a scheduling tool's activity
calendar than an error; **no date, duration or float moves on it.** All three are offered to the
project owner as ruling items, not asserted as errors.

A fourth difference — the owner's cost summary, ₹ 1 00 000 — is **already recorded as `R-14`**
(master H.13). Reproducing a known finding independently is the outcome a check like this is for.

**`PR1-F3`:** `CONSOLIDATED_PROJECT_REPORT.md` (repository root) is stale on the open-item and
assumption counts and predates RC4 to RC10 and DR-A2. **It is not edited** — it is an artefact of
exactly the class `RC10` exists to register.

## The main staircase

**24R @ 170.8333 · 280 tread · 3 flights × 8 · total rise 4 100 · 1 200 wide · 200 well · 200
waist · headroom 2 533.** This package reproduces it and **changes nothing.**
