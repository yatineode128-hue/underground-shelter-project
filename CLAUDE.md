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
- Latest revision: **SR1** (16 Sep 2026, master **H.39**) — **two A2 structural reinforcement
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
