# MASTER PROJECT REPORT — README

Package `Project Report/`, revision **PR1**, 13 September 2026.
Geometry **Rev F + M1** · current to **RC10** and **DR-A2**.
Status: **FOR REVIEW — NOT FOR CONSTRUCTION.**

## What this package is

`MASTER_PROJECT_REPORT.pdf` — **89 pages, 19 parts and 4 appendices.** The project stated once, in
the order an engineer would need it to reproduce the design: the physics first, then the ground,
then the loads, then the calculations, then what is drawn, then what is still open.

It is written to stand on its own. Everything needed to follow an element from a first-principles
load to a bar mark on a drawing is in it, with the clause of the Indian Standard that permits each
step named beside it.

**`master/MASTER_PROJECT_STATE.md` governs. Where the report and the master disagree, the master
is right.**

## What PR1 changed in the project

**Nothing.** No dimension, level, load, thickness, bar, quantity, rate, date or float. No `.std`
file was touched, STAAD.Pro was not run, no drawing was edited, no generator was re-run, and **no
`[C]` / `[R]` / `[A]` / `[U]` / `[N]` tag was converted, downgraded or deleted.** The main
staircase is untouched. See master Part **H.36**.

## Files

```
Project Report/
   MASTER_PROJECT_REPORT.pdf                     the deliverable
   Documentation/MASTER_PROJECT_REPORT.md        the report SOURCE -- edit this
   Documentation/00_README.md                    this file
   Scripts/report_render.py                      Markdown subset -> PDF
   Scripts/report_verify.py                      independent recomputation
   Calculations/REPORT_VERIFICATION_OUTPUT.txt   its output
```

## Rebuild

```
python3 "Project Report/Scripts/report_verify.py"     # 498 checks
python3 "Project Report/Scripts/report_render.py"     # rebuild the PDF
```

**Never edit the PDF.** Edit the Markdown and re-run the renderer. The renderer adds no content of
its own beyond the cover page, the running head and foot, and the automatically paginated contents
list.

**Dependency:** `reportlab`, which is already the project's PDF toolchain —
`WORKS MANAGEMENT/Scripts/wm_programme_pdf.py` and `wm_handout_pdf.py` both use it.
**Fonts:** GNU FreeFont, the only family on this machine carrying every glyph the report uses
(Greek, sub- and superscripts, mathematics and arrows) in all four styles. Any character a face
cannot draw is substituted and **reported**, never silently dropped.

## The verification pass

`report_verify.py` recomputes **498** of the figures the report reproduces, from their own inputs,
with the formulas written out again rather than copied.

```
PASS                            494
KNOWN / RECORDED difference       4
UNEXPLAINED FAIL                  0
```

> **A PASS means the printed number follows from the printed inputs.** It is **not** a design
> check and **not** an analysis. It does not re-derive engineering judgement, it cannot run STAAD,
> and it cannot tell you whether an assumption is true.

**Two new findings came out of it and NEITHER IS CORRECTED** — master rule M.11 forbids editing a
recorded value away:

| Ref | Where | Computed | Printed |
|---|---|---|---|
| **`PR1-F1`** | master `A.7.8`, box wall shear stress | **0.0506 N/mm²** | 0.063 N/mm² |
| **`PR1-F2`** | master `B.8.7`, footing F1 ULS e<sub>u</sub> and q<sub>u,max</sub> | **0.159 m**, **186.0 kPa** | 0.128 m, 190.0 kPa |

Both are figures quoted to show that something is negligible or non-governing, and **nothing
downstream is sensitive to either** — which is why both survived every previous pass. They are
offered to the project owner as a ruling item, not asserted as errors.

A third difference — the owner's cost summary, ₹ 1 00 000 — is **already recorded as `R-14`**
(master H.13). Reproducing a known finding independently is the outcome a check like this is for.

**`PR1-F3`:** `CONSOLIDATED_PROJECT_REPORT.md` (repository root) is now stale on the open-item and
assumption counts and predates RC4 to RC10 and DR-A2. **It is not edited** — it is an artefact of
exactly the class `RC10` exists to register.

## The main staircase

**24R @ 170.8333 · 280 tread · 3 flights × 8 · total rise 4 100 · 1 200 wide · 200 well · 200
waist · headroom 2 533.** This package reproduces it and **changes nothing.**
