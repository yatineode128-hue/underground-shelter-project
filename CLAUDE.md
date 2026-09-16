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
- Latest revision: **AN1** (16 Sep 2026, master **H.42**) — **the project's FIRST animation**, the
  new package `Animation/`: one continuous 3D camera journey through the whole facility,
  **6 min 22 s**, 21 beats, rendered live in the browser from the project's own dimensions.
  **A single self-contained HTML file with ZERO external dependencies** — it plays from a USB
  stick in a hall with no internet. **No design value moved, no analysis was run, no tag
  converted, the main staircase untouched.** The load path is **conceptual only** because `D.3.5`
  records the underground model's results as `[NOT AVAILABLE — DO NOT INVENT]`: there is no
  contour, displacement, utilisation or failure mode in it anywhere. It names **no
  vulnerability** — `EM-F1`, `EM-V3` and `RC5-F2` are not drawn and not named. Rebuild with
  `python3 Animation/Scripts/an1_build.py`; `Animation/Output/` is a **build artefact, never
  edit it by hand**. Findings **`AN1-F1`** the owner's Revit set prints `ENTRY ROOF TOP 3400`
  and `GROUND FLOOR LEVEL 440` where `A.4.3` records **+2.450** and **+0.450** — the master
  governs, neither resolved, new item `AN1-V8` · **`AN1-F2`** *"cassette"* means two different
  things in this project (the HEPA/carbon **filter** cassette and the **SN-03 sealed-cassette
  chemical toilet**) and they were nearly conflated · **`AN1-F3`** nothing documents a walk of
  56 steps, so both endpoints were fixed to real features and the pace **derived** at 0.655 m ·
  **`AN1-F4`** the project holds no wind-direction data, so the blast azimuth is `[V]`, chosen
  as the only one that puts the sentry post **upwind** of the shelter. Eight open items
  `AN1-V1…V8`; **`K.1b` is unaffected.**
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
