# Final Submission Report — revision PR3 (master Part H.44)

`CBRN_Hardened_Underground_Ops_Room_Project_Report.pdf` — the project report in the owner's
service-writing layout: red double-rule frame, page number on the bottom rule, decimal paragraph
numbering 1 / 1.1 / 1.1.1 restarting in each chapter, Arial 12, black text, no running header.
114 A4 pages, 18 chapters, appendices A (reinforcement), B (bill of quantities, WM3),
C (drawing index, 90 drawings), D (references).

**It is a presentation of the design, not a change to it.** By instruction it leaves out the
evidence tags, revision history, findings and open-item register. **Nothing in master K.1b or
K.2 is closed by it** — master H.44.2 lists what a reader of this report will not see.
`master/MASTER_PROJECT_STATE.md` governs; PR2 (`../MASTER_PROJECT_REPORT.pdf`) remains the full
technical record.

## Rebuild

```
python3 "Project Report/Final Submission/Scripts/sw_render.py"
```

- `Source/*.txt` — the report text, read in file-name order. Markup is described at the top of
  `sw_render.py` (`P1` / `P2` / `P3` numbered paragraphs, `#table`, `#calc`, `#fig`, ...).
- `@concrete`, `@steel`, `@parts`, `@cost`, `@boq`, `@programme` tables are read at build time
  from the WM3 files in `WORKS MANAGEMENT/Cost/REVISED_*_RC1.csv` and
  `WORKS MANAGEMENT/Programme/REVISED_MASTER_CONSTRUCTION_SCHEDULE_R1.csv`; `@drawings` from
  `DRAWING QAQC/qa_index.json`. Nothing is retyped.
- Figures come from `../Scripts/report_figures.py` through `Scripts/sw_figures.py`, which restates
  or drops review-style annotation and blackens lettering; geometry is untouched.
- Needs `reportlab` (and `pillow` for the one-pixel spacer image). Uses Arial from
  `/usr/share/fonts/truetype/msttcorefonts/` if installed, otherwise Liberation Sans
  (metric-identical). The Arial files are not in the repository.

Main staircase unchanged: 24R @ 170.8333, 280 tread, 3 flights × 8, total rise 4 100.
