# CLAUDE.md — project operating guide

Underground CBRN-hardened blast-resistant protective structure + sentry post, Pune.
B.E. Civil capstone, designed for actual construction.

## Authority

- **`master/MASTER_PROJECT_STATE.md` is the single source of truth.** Parts A, B, F and L are
  the authoritative current design. If any file disagrees with it, the master governs.
- **`master/QUICK_STATE.md` is orientation only.** It is a compact digest to save you reading
  2 000 lines for a simple question. It is **not** an authority and never overrides the master.
  If the two disagree, the master is right and QUICK_STATE.md is stale — say so.
- **Read the relevant master sections before any engineering or design decision.** Quoting
  QUICK_STATE.md is not sufficient basis for changing a dimension, load, or bar.

## Evidence discipline

The master tags every value `[CONFIRMED]` / `[RECONSTRUCTED]` / `[ASSUMED]` /
`[UNRESOLVED]` / `[NOT AVAILABLE]`.

- **Never guess or silently resolve an `[UNRESOLVED]`, `[ASSUMED]` or `[NOT AVAILABLE]` item.**
  Ask. Do not convert one into a confirmed fact, and do not delete or downgrade a tag.
- Label anything you produce with the same classes.

## Rates

- **`SSR 22-23 MH (1).pdf` in the project root is the rate authority.** Maharashtra PWD
  State Schedule of Rates 2022-23, 624 pages, supplied by the owner. Every rate in the
  package is a published SSR item, or is derived from one **by a method the SSR itself
  prescribes** with the arithmetic recorded. **Never invent a rate.** If the schedule has
  no item, say so and leave the line NOT PRICED — the SSR's own instruction is that such
  rates are approved by the Superintending Engineer.
- **An SSR "completed rate" already contains 10 % overheads, 10 % contractor's profit,
  1 % labour cess, and — for concrete — its formwork and centering.** Never add any of
  them again. Reinforcement is the exception: it is explicitly excluded from the concrete
  rates and is billed at SSR 26.33.
- The rate library is `WORKS MANAGEMENT/Scripts/wm4_ssr_library.py`, the mapping is
  `wm4_bill.py`, and every output regenerates with `wm4_build.py`. **Read those before
  changing any rate**, and re-run `wm4_verify_xlsx.py` afterwards.

## Current state

- Structural revision: **Phase 2 Rev A + M1**. Architectural Rev F. Report Rev D.
- **M1 is APPROVED and IMPLEMENTED** (3 Sep 2026, master H.4): W6 and W7 400 mm,
  box 22 000, shaft 15200–18000, ESC 2 at X 19 900, headhouse and covered stairwell +200.
- **C16 (roof/platform junction) is CLOSED** — ruled at **250** by RC1, 10 Sep 2026
  (master H.3 / H.14 / K.1); A.4.7 carries the corrected clause. *This line previously read
  "is not resolved"; corrected by RC3, master H.27.* The open items that remain are the
  **thirty-three in master K.1b** — read that, not this line.
- Latest revision: **MEP3** (18 Sep 2026, master **H.44**) — **`ARCH001` and `ARCH002`
  corrected against the Rev F CAD.** The four Rev F DXFs they redraw were **parsed entity by
  entity**, and ten depiction errors on sheet 01 and nine on sheet 02 were fixed: **both blast
  doors now swing opposite ways** (BD1 west into bay 6, BD2 east into bay 8), the **W5 fire
  door D-05** is drawn, the **decon airlock** has its real 110 partitions with **STAGE 1 at
  the south**, the **main stair** is drawn as the plan draws it (flights Y 1800–3760, eight
  risers each — `mep_proj.STAIR`, unchanged), the **headhouse and entry doors open outward**
  through walls that are now broken at the opening, the **berm toe** is drawn, **sentry-post
  door D1 is in the WEST wall on both floors**, the **spiral stair** is at (−1150, 1450), and
  the **300 projection with its 300 high pardi** is drawn for the first time. **No design
  value moved, no analysis was run.** `ARCH001` view 3 is now **1 : 200** so the sentry post
  is drawn at its site position instead of off position; `ARCH002` views 1 and 2 are **1 : 75**
  so both plans fit beside their spiral stairs. **Read `arch_data.CAD_FINDINGS` (master H.44.4)
  before trusting either sheet against the Rev F CAD** — six places where the drawing and the
  master disagree, resolved in the master's favour and none of them silently: **no W8 door is
  drawn** (`MEP3-F1`, the gap is permanent), **D-05 is the ruled 900 not the drawn 800**
  (`MEP3-F2`), **no excavation line is drawn at all** (`MEP3-F3`, Rev F says 1500 and WM-V9 /
  RC6 measure 1000 at formation under a 1:1 batter), and **the roof projection stays
  `[NOT AVAILABLE]`** (`MEP3-F6`, U8-F1 — only the FIRST FLOOR projection is drawn).
  **`MEP3-F2a` is OPEN and unresolved: `FLS012` routes escape route R1 across W5 at Y 2950,
  where there is no opening.** FLS012 was not altered. Only nine files changed; `a2_lib.py`,
  `sheet_data.py`, `sentry_data.py`, `mep_data.py`, `ops_data.py` and STR006…STR009 / MEP010 /
  MEP011 / FLS012 / WMS013 are **untouched**. Index still **90 drawings, 84 PASS**.
  Before it: **MEP2** (18 Sep 2026, master **H.43**) — **four more A2 sheets; the
  presentation series is now TEN.** New: **`FLS012`** (SHEET 12, fire and life safety escape
  plan) and **`WMS013`** (SHEET 13, works management). **Redrawn: `ARCH001` and `ARCH002`**,
  the owner's own sheets 1 and 2, same views and scales, **every dimension and level brought
  to Part A** — the owner's `Project1.pdf` is preserved and untouched. **No design value
  moved, no analysis was run.** New data modules `arch_data.py` (sheets 01 / 02) and
  `ops_data.py` (sheets 12 / 13); `a2_lib.py`, `sheet_data.py`, `sentry_data.py`,
  `mep_data.py` and STR006…STR009 / MEP010 / MEP011 are **untouched**.
  **SHEET 13 presents `WM3`, NOT `WM4`** — the revised owner package of H.15, final project
  cost **Rs 2,97,90,913**, programme R1; WM4 is the later SSR-priced bill and both stand.
  **Read `arch_data.CORRECTIONS` (and master H.43.4) before trusting any figure on the
  owner's sheets 1 or 2** — fourteen are corrected, chiefly the **bay chain** (A.3) and the
  **sentry post 4000 × 5000** (A.4.8). Findings **`MEP2-F1`** (the owner's door schedule
  makes every door 900 × 2100; **both blast doors are 1200 × 2100**, A.4.9) and
  **`MEP2-F2`** (its *"FDN LEVEL −6100"* is the internal floor, not the foundation).
  **`FLS012` uses the RC4-ruled escape-shaft ladder, not `fs_data`'s superseded
  `FS-6`/`FS-V7` text.** Index now **90 drawings, 84 PASS**; the series is split across four
  QA disciplines by filename prefix.
  Amended the same day as **MEP2A** (master **H.43.12**), by instruction: **both charts
  DELETED from `WMS013`** — the programme bar chart and the cost distribution chart. **No
  figure changed.** The sheet is now purely tabular and carries **all 38 measured bill items**
  with unit, quantity, rate and amount, which the charted version had no room for. Long item
  descriptions are **trimmed to the column at a word break and marked with an ellipsis** (the
  bill governs), and the standby generator line, which carries no rate in WM3, prints as
  **NOT PRICED** and is in no total on the sheet. **Never invent a rate for it.**
  Before it: **MEP1** (16 Sep 2026, master **H.42**) — **two A2 SERVICES presentation
  sheets in the same `ARCH001…ARCH005` frame, `MEP010` (SHEET 10, HVAC + EMP zone layout plans)
  and `MEP011` (SHEET 11, septic tank, soak pit and sump pit in plan and cross-sectional
  elevation).** **No design value moved, no analysis was run.** Values are read from
  `hv_data.py`, `em_proj.py`, `dr_data.py`, `mep_proj.py` and `rebar_data.py` through the new
  `Presentation Sheets/Scripts/mep_data.py`; nothing is written back to those packages and
  **`a2_lib.py`, `sheet_data.py`, `sentry_data.py` and STR006…STR009 are untouched** (the
  services layers are added per-document, not to `a2_lib.LAYERS`). By instruction the sheets
  carry **no design-basis panel, no calculation table and no revision, phase or open-item
  text**; the gaps are therefore recorded in the master only, as **`MEP1-F1` … `MEP1-F7`**.
  **Read `MEP1-F2` before adding any bar to SHEET 11** — ST-01, the soak-pit cover slabs and
  the inspection chambers have **no reinforcement anywhere in this project**, so none is drawn
  or scheduled; only SU-01 (marks F10–F13) is detailed. **Read `MEP1-F7` before quoting
  SHEET 11's key plan** — it uses the **RC4 east** sentry-post placement, and `U4` is open.
  New QA discipline **`MEP - A2 presentation sheets`**; index now **86 drawings, 80 PASS**.
  Before it: **SR1A** (16 Sep 2026, master **H.41**) — by instruction, on the owner's own
  copies of `STR006` / `STR007`: the **DESIGN BASIS** panel deleted from both, and the entire
  revision line (`STRUCTURAL - PHASE 2 REV A + M1`) deleted from the header — asked directly
  which reading was meant (drop just `REV A`, or the whole line), and the whole line was the
  answer. **`sheet_data.IDENTITY` now has FOUR lines and no revision text at all.**
  `sentry_data.IDENTITY` (STR008 / STR009) is **decoupled** from it and keeps its own
  `STRUCTURAL - PHASE 2 + M1` line unchanged — **STR008 / STR009 are byte-identical to before
  this revision** (diffed with timestamps stripped). The freed column on STR006 / STR007 is
  filled with `table_stack()`, same as SR2A. **A real bug was found and fixed in `a2_lib.py`**:
  `table()`'s row-height shrink loop could quantise one 0.05 mm step below `MIN_TXT_H` when the
  starting height wasn't grid-aligned; fixed with a post-loop clamp, verified not to change
  STR008/STR009. **This CLOSES `SR2-F2`** (STR007's note panels were rendering below the 1.70 mm
  floor; that panel is now deleted and the table sharing its column fits with real margin).
  Before it: **SR2** (16 Sep 2026, master **H.40**) — **two A2 sentry-post reinforcement
  presentation sheets, `STR008` (SHEET 08, beams B1/B2 + column C1) and `STR009` (SHEET 09,
  isolated footing F1 + slab S1)**, in the same Revit A2 frame and title block. **No design
  value moved and no analysis was run.** The sentry post is excluded from `rebar_data.py`, so
  its bar-mark register is the separate `Presentation Sheets/Scripts/sentry_data.py` — keep it
  that way. Finding **`SR2-F1` is UNRESOLVED and blocks the roof beams**: master B.8.6 checks
  the roof joint with B2 = 2-T20 while F.4 schedules 3-T20 at supports, and 3-T20 there fails
  IS 13920 Cl. 7.2.1. **STR008 therefore details the FIRST-FLOOR frame only.** Six more open
  items `SR2-V1…V6`. Amended the same day as `SR2A` (master H.40.8): the design-basis
  and declared-decisions panels were DELETED from both sheets and `REV A` removed from their
  header. The decisions and open items live in the master ONLY — the drawing no longer states
  them, so the master must carry them forward.
  Before it: **SR1** (16 Sep 2026, master **H.39**) — **two A2 structural reinforcement
  presentation sheets, `STR006` (SHEET 06, roof slab + mat) and `STR007` (SHEET 07, 600 shear
  wall + main staircase)**, in the frame and title block of the owner's Revit A2 set.
  **No design value moved.** Finding `SR1-F1` — IS 13920 Cl. 10.4 is not triggered for the box.
  Before it: **WM4** (15 Sep 2026, master **H.38**) — **the Works Management bill priced
  from the Maharashtra PWD State Schedule of Rates 2022-23**, the 624-page `SSR 22-23 MH (1).pdf`
  the owner supplied. **No quantity moved.** Seven new open items **WM4-V1…V7**.
  Before it: **PR2** (master project report, H.37, 13 Sep) · **DR-A2** (H.35) · **RC10** (H.34)
  and the RC4…RC9 ruling series (H.28–H.33), 11–12 Sep · **MS2** (STAAD input files, H.26) ·
  **QA2** (drawing package re-scan, H.25) · **RC3** (project-wide reconciliation, H.27), 11 Sep 2026.

## Frozen — do not touch

**Main staircase: 24 risers, 170.8333 mm riser, 280 mm tread, 3 flights × 8, total rise 4100 mm.**
Landing levels, flight widths (1200), the 200 well and the 2533 headroom go with it.
**Never change any of this unless the user explicitly asks again in a new request.**

## Working rules

- **Inspect native files before modifying them.** Parse the DXF or read the `.std`; never edit
  from memory or from a summary.
- **Make only changes the master supports or the user has explicitly approved.** No scope
  widening, no opportunistic "improvements".
- **Supplied/input DXFs may be edited directly** — the ten Rev F architectural drawings are
  source, not build artefacts.
- **Do not fabricate missing generator scripts or unavailable output drawings.** `proj.py`,
  `dxflib.py` and `d01_wall.py`…`d08_sentryslab.py` are absent, so sheets S-01…S-05, S-07 and
  S-08 cannot be regenerated. Say so; do not invent them. (S-06 is present and already at M1.)
  The same applies to the files master I.1 lists as **NOT IN THIS WORKSPACE** — the Phase 1
  Rev D report, `SK02_Underground_Plan.png` and the 19 STAAD captures.
- **A new drawing package must register itself with the QA tool.** Add its `DXF/` prefix to
  `DISCIPLINE` in `DRAWING QAQC/Scripts/qa_report_data.py` and its name to `ORDER` in
  `make_index.py`, then re-run both. Twelve sheets were invisible to the index for four
  revisions because this was not done (H.25).
- **STAAD models must be checked against the master before modification** — geometry,
  materials, thicknesses, supports, loads, load cases and combinations.
- **Distinguish file reconciliation from STAAD.Pro execution.** STAAD.Pro is not available in
  this environment. Editing and verifying a `.std` file is *not* running an analysis, and must
  never be reported as one.
- M1 is not a uniform shift. Nothing west of X 14800 moves; W6/W7 thicken about their own
  faces; the shaft moves +200 and Bay 8 and the east end +400; the headhouse and covered
  stairwell move +200 as whole structures. Re-derive per element, never translate wholesale.

## Before you finish any modification

1. Run `git status` and `git diff`.
2. Report **exactly** which files changed, with a before → after summary for each.
3. State what you actually verified, and how.
4. State what you could not make consistent, and why.
5. Confirm the main staircase is unchanged.
6. Never claim a file is complete or verified unless you checked it.

Give any significant change a revision identifier and record it in master Part H (rule M.10).
Never overwrite a previous revision without preserving it (M.11).
