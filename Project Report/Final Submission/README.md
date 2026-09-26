# Final Submission Report — revision PR3, amended PR3A / PR3B / PR3C / PR3D (master Part H.44)

`CBRN_Hardened_Underground_Ops_Room_Project_Report.pdf` — the project report in the owner's
service-writing layout: red double-rule frame, page number on the bottom rule, decimal paragraph
numbering 1 / 1.1 / 1.1.1 restarting in each chapter, Arial 12, black text, no running header.
120 A4 pages, 18 chapters, appendices A (reinforcement), B (bill of quantities, WM3),
C (drawing index — the fifteen sheets 01 to 15; the drawings themselves are a separate spiral-bound
A3 book), D (references). The front pages (certificate, approval sheet, declaration, acknowledgement)
follow a CME sample and carry no border.
Chapter 2 carries the five P1-deck site slides (Figs 2.1–2.5). The cover names Syndicate 01 and its
five guides; the guide is spelt *Dr I R Chaudhuri* by owner ruling (master H.44.10).

**It is a presentation of the design, not a change to it.** By instruction it leaves out the
evidence tags, revision history, findings and open-item register. **Nothing in master K.1b or
K.2 is closed by it** — master H.44.2 lists what a reader of this report will not see.
`master/MASTER_PROJECT_STATE.md` governs; PR2 (`../MASTER_PROJECT_REPORT.pdf`) remains the full
technical record.

`Hard_Cover_Report_A4.pdf` and `Hard_Cover_Drawings_A3_Landscape.pdf` are the black-and-gold hard
covers for the binder (`Scripts/sw_covers.py`).

## Rebuild

```
python3 "Project Report/Final Submission/Scripts/sw_render.py"
```

- `Source/*.txt` — the report text, read in file-name order. Markup is described at the top of
  `sw_render.py` (`P1` / `P2` / `P3` numbered paragraphs, `#table`, `#calc`, `#fig`, ...).
- `@concrete`, `@steel`, `@parts`, `@cost`, `@boq`, `@programme` tables are read at build time
  from the WM3 files in `WORKS MANAGEMENT/Cost/REVISED_*_RC1.csv` and
  `WORKS MANAGEMENT/Programme/REVISED_MASTER_CONSTRUCTION_SCHEDULE_R1.csv`. Nothing is retyped.
  Appendix C is a fixed table in `Source/19_appendices.txt` (the `@drawings` reader of
  `DRAWING QAQC/qa_index.json` is kept but no longer used).
- `Images/STAAD/*.png` — STAAD.Pro captures cut from the owner's screenshots of the analysis
  deck; `#grid` prints them in labelled panels (`sw_figures.GRIDS`). See master H.44.12.
- `Images/CME_crest_*.png` — the crest, cut from the owner's photographs and cleaned by
  `Scripts/sw_crest.py`; `python3 Scripts/sw_covers.py` rebuilds the two covers.
- `Images/P1_*.jpg` — the five P1-deck slides exactly as supplied. `#photo` prints them;
  `sw_figures.PHOTOS` crops the slide's edge and title bar at build time, nothing else.
- Figures come from `../Scripts/report_figures.py` through `Scripts/sw_figures.py`, which restates
  or drops review-style annotation and blackens lettering; geometry is untouched.
- Needs `reportlab` and `pillow` (the slide crops and the one-pixel spacer image). Uses Arial from
  `/usr/share/fonts/truetype/msttcorefonts/` if installed, otherwise Liberation Sans
  (metric-identical). The Arial files are not in the repository.

Main staircase unchanged: 24R @ 170.8333, 280 tread, 3 flights × 8, total rise 4 100.
