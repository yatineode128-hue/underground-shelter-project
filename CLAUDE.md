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

## Current state

- Structural revision: **Phase 2 Rev A + M1**. Architectural Rev F. Report Rev D.
- **M1 is APPROVED and IMPLEMENTED** (3 Sep 2026, master H.4): W6 and W7 400 mm,
  box 22 000, shaft 15200–18000, ESC 2 at X 19 900, headhouse and covered stairwell +200.
- Open item **C16** (roof/platform junction) is *not* resolved — see QUICK_STATE.md.

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
