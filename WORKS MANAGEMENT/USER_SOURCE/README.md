# USER_SOURCE — the project owner's own Works Management files

**These four files are the owner's, exactly as supplied. Nothing in this folder has
been edited, converted, re-derived or corrected, and nothing in it ever should be.**

Under the brief's order of authority for Works Management they come **first** — ahead of
the project master, ahead of the existing project documentation, and ahead of anything
Claude generated (the WM1 package). They are kept here in their original binary form so
that every published figure can be traced back to the file it came from.

| File | What it is |
|---|---|
| `Underground_CBRN_Ops_Room_BOQ_Estimate.xlsx` | **The bill of quantities and the cost estimate.** Three sheets: concrete and rebar take-off, the priced BOQ in five parts, and the cost summary ending at ₹3,00,33,306 |
| `BOQ_and_Works_Management_CBRN_Ops_Room.pdf` | The same estimate as an eight-page report, with the WBS overview, the milestone definitions and the working framework |
| `UG_CBRN_HDRND_OPS_ROOM_MCS_R0.mpp` | **The master construction schedule, revision R0** — the native Microsoft Project file |
| `UG_CBRN_HDRND_OPS_ROOM_MCS_R0_Lvl5Micro.pdf` | The Level-5 micro print of that schedule: 130 activities with durations, dates and logic |

## What is published from them

`Scripts/wm2_user_package.py` reads these files and writes:

| Output | From |
|---|---|
| `Cost/USER_BOQ_TAKEOFF.csv` · `USER_BOQ_PRICED.csv` · `USER_COST_SUMMARY.csv` | the workbook, cell by cell |
| `Cost/USER_BOQ_AND_COST_ESTIMATE.md` | the same three sheets, rendered |
| `Programme/USER_MASTER_CONSTRUCTION_SCHEDULE_R0.csv` / `.md` | the Level-5 print, decoded through its own font CMap |

**Nothing is retyped.** The `.mpp` cannot be parsed without Microsoft Project, so the
schedule is read from the owner's own print of it, which carries the same 130 activities.
If a figure in a generated file looks wrong, check it against the file here — there is no
transcription step in between that could have introduced the error.

## Where the disagreements are recorded

`Documentation/WM_RECONCILIATION_REGISTER.md` lists every point where this material and
the project master disagree — fourteen of them, **all left open for the owner to rule on.**
None has been silently reconciled in either direction.
