<!-- Works Management package, revision WM1. -->

# WORKS MANAGEMENT
## Underground CBRN-hardened blast-resistant protective structure and sentry post — Pune, Maharashtra

**Package revision WM1** · 7 September 2026
**Geometry:** Architectural Rev F · Structural Phase 2 Rev A + M1
**Discipline packages used:** Structural CAD SC1 · Drainage DR1 · HVAC HV1 · Schedule of Finishes FN1

> **THE ONLY DESIGN CHANGE in this package is reference SP-B1: the sentry post walls are
> BRICK MASONRY, replacing the Rev F 200 mm RC ballistic infill panels. No other element
> of the project is changed. No drawing, model, calculation or design file outside this
> folder was modified.**

---

## What this package is

A complete Works Management package for the **entire project** — the underground shelter,
the entry headhouse and covered stairwell, the escape shafts, the engineered cover, the
sentry post, the services, the external works and the concealment works — from mobilisation
to handover.

| | |
|---|---|
| Programme | **279 activities**, 18 milestones, 404 logic links, 3-level WBS |
| Duration | **326 working days**, 2 November 2026 to 20 November 2027 |
| Critical path | 75 activities at zero total float |
| Calendar | Six-day week (Mon–Sat), five date-certain national holidays |
| BOQ | 90 items across 10 sections, all traceable to the project record |
| Resources | 33 resources, 426 assignments — every one used on the programme |
| Quality | 42 inspection and test items, **16 hold points in the programme** |
| Safety / risk | 15 hazard classes, 25 risks |
| Codes | 78 references — **none invented** |
| Consistency audit | **65 checks, 65 pass** |

---

## Deliverables

### Principal documents (this folder)

| File | Contents |
|---|---|
| `Underground_Shelter_Works_Management_Handout.pdf` | **The handout** — 44 pages, 25 sections, the final-semester submission |
| `Underground_Shelter_WBS.md` / `.csv` | Complete work breakdown structure, every activity with dates, logic and float |
| `Underground_Shelter_BOQ.md` / `.csv` | Bill of quantities for the whole project |
| `Underground_Shelter_Resource_Plan.md` / `.csv` | Staff, labour and plant, with peaks and what drives them |
| `Underground_Shelter_Procurement_Plan.md` / `.csv` | Procurement tied to the programme; long-lead register |
| `Underground_Shelter_QA_QC_Plan.md` / `.csv` | Inspection and test plan, hold points, records |
| `Underground_Shelter_Safety_Risk_Register.md` / `.csv` | Safety management and the risk register |
| `Underground_Shelter_Codes_References.md` / `.csv` | Codes, standards and specifications |

### Programme (`Programme/`)

| File | Contents |
|---|---|
| `Underground_Shelter_Final_Works_Programme.xml` | **The master programme.** MSPDI — Microsoft Project's own published XML schema |
| `Underground_Shelter_Final_Works_Programme.pdf` | Programme drawing, 7 A3 sheets: basis, summary Gantt, detailed Gantt |
| `Underground_Shelter_Final_Works_Programme.csv` | Task list for import into any other planning tool |

> **On the `.mpp` file.** Microsoft Project's native `.mpp` is an undocumented binary
> (OLE2 compound document) format that can only be written by Microsoft Project itself.
> This was verified here against MPXJ 16.7.0, the industry-standard Project library:
> `org.mpxj.writer.FileFormat` offers JSON, MPX, MSPDI, Planner, PMXML, XER and SDEF —
> there is no MPP writer, in MPXJ or anywhere else outside Microsoft Project.
>
> The master programme is therefore issued as **MSPDI**, which is not a substitute or an
> approximation but Microsoft's own interchange format for Project. It carries the full
> WBS, all 279 activities, all 404 logic links with their lags, the six-day calendar with
> its exceptions, 33 resources, 426 assignments, milestones, float and notes.
>
> **To obtain the `.mpp`:** open the `.xml` in Microsoft Project
> (*File → Open*), then *File → Save As → Project (\*.mpp)*. One step, nothing lost, and
> the file remains fully editable.
>
> The file was verified by reading it back with MPXJ and comparing every task count, link
> count, calendar day type, calendar exception and date against the critical-path
> calculation that produced it.

### Supporting documentation (`Documentation/`)

| File | Contents |
|---|---|
| `WM_PROJECT_COMPONENT_REGISTER.md` | The 23 confirmed components, and what was removed from the supplied schedule |
| `WM_CONSTRUCTION_METHODOLOGY.md` | How each package is built and why in that order |
| `WM_SENTRY_POST_BRICK_MASONRY.md` | **Design change SP-B1** in full — geometry, method, programme, verification items |
| `WM_PROGRESS_MONITORING.md` | Baseline, three reporting streams, cycle, delay tracking, corrective action |
| `WM_ASSUMPTIONS_AND_VERIFICATION_REGISTER.md` | Everything assumed, everything missing, everything left open |

### Working files

| File | Contents |
|---|---|
| `Schedules/BOQ_QUANTITY_DERIVATION.txt` | ~800 lines of quantity working, with the source of every input |
| `Schedules/WM_CPM_OUTPUT.txt` | Critical-path calculation output and milestone dates |
| `QAQC/WM_CONSISTENCY_AUDIT.txt` | **65 executed consistency checks** with their evidence |

---

## Regenerating the package

Everything is generated from two source files, so the deliverables cannot drift apart.

```
Scripts/wm_data.py        programme, WBS, activities, logic, resources
Scripts/wm_content.py     methodology, ITP, safety, risk, procurement, codes
        |
        +-- wm_quantities.py    quantity derivation  -> BOQ
        +-- wm_schedule.py      calendar + CPM       -> all dates and float
        +-- wm_mspdi.py         Microsoft Project file + CSV
        +-- wm_programme_pdf.py programme drawing
        +-- wm_docs.py          every .md and .csv deliverable
        +-- wm_handout_pdf.py   the handout
        +-- wm_audit.py         final consistency audit

python3 Scripts/wm_build_all.py
```

No date, quantity or float in any deliverable is typed by hand.

---

## Evidence discipline

The package follows the project's own rule: **nothing marked unresolved or not available
is quietly filled in.** Every value carries a class — `[C]` confirmed, `[D]` derived here,
`[A]` assumed by this package, `[U]` unresolved, `[N]` not available.

**Twelve verification items** (`WM-V1` to `WM-V12`) are raised by this package and left
open. **Ten master conflicts** (`C16`–`C21`, `U1`, `U2`, `U3`, `U8`) are carried forward
untouched — none is resolved, downgraded or deleted.

**Thirteen pieces of information the project does not contain** are listed with the
activity each one blocks and the date it is needed, computed from the programme. The
largest is that **no electrical design package exists**: the scope is confirmed but no
circuit, cable, luminaire, distribution board or earth-electrode schedule does, so every
electrical quantity reads *to be verified from final measurement* and no electrical
enquiry can be issued.

## What this package did not do

* It did not run STAAD.Pro. STAAD.Pro is not available in this environment and no
  analysis was performed. Reading a `.std` file is not running an analysis.
* It did not modify any drawing, model, calculation or design file. The only files
  changed outside this folder are `master/MASTER_PROJECT_STATE.md` (Part H revision
  record) and `master/QUICK_STATE.md`.
* It did not change the main staircase. The frozen geometry — 24 risers at 170.8333,
  tread 280, three flights of eight, total rise 4100, flights 1200 wide, 200 well,
  2533 headroom — is reproduced in the programme exactly as it stands.
* It made only one design change, SP-B1, and made it because it was explicitly
  instructed.
