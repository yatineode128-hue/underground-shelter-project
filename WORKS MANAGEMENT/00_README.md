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
| `WM_RECONCILIATION_REGISTER.md` | R-1 to R-14, the conflicts between the owner's package and the master, and how each was ruled |

> **TWO DOCUMENTS THAT USED TO BE HERE HAVE MOVED — 10 September 2026, master H.18.**
> `WM_CAMOUFLAGE_AND_CONCEALMENT_POLICY.md` is now
> **`Site and Concealment/Documentation/CAMOUFLAGE_AND_CONCEALMENT_POLICY.md`** (revision **CAM2**),
> and `WM_FIRE_SAFETY_AND_EVACUATION_PLAN.md` is now
> **`Fire and Life Safety/Documentation/FIRE_SAFETY_AND_EVACUATION_PLAN.md`** (revision **FS2**).
> Neither was ever a works-management document — they were generated here only because this
> package's generator happened to hold them. **Each now sits in its own discipline package with
> the drawings the move added** — `C-101` for concealment, `F-101` and `F-102` for escape. The
> text moved verbatim; each package's own revision note records the one finding its drawings
> raised. `Scripts/wm_audit.py` §15 fails if either document reappears here or goes missing there.

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

---

# REVISION WM2 — 10 September 2026

**The project owner's own Works Management package has been brought in, and it now
governs.** Four files were supplied — a BOQ and cost estimate workbook, an eight-page
BOQ / works-management report, and the master construction schedule **R0** as both a
Microsoft Project file and a Level-5 micro print. They are held unaltered in
`USER_SOURCE/`.

## Order of authority

1. **the owner's Works Management files** — `USER_SOURCE/`
2. actual project information
3. existing project documentation
4. **WM1**, the generated package above

Nothing of the owner's has been corrected, re-derived, rounded or rebuilt. **WM1 is not
overwritten either** — it is a preserved revision and stays exactly as issued.

## What WM2 adds

| | |
|---|---|
| `USER_SOURCE/` | the owner's four files, unaltered, with a README |
| `Cost/USER_BOQ_AND_COST_ESTIMATE.md` + three CSVs | **the project's cost document** — 42 priced items, every rate, ending at **₹3,00,33,306**. WM1 had no rate and no cost anywhere in it |
| `Programme/USER_MASTER_CONSTRUCTION_SCHEDULE_R0.md` / `.csv` | **the programme of record** — 130 activities, **224 working days, 02-11-2026 to 26-07-2027**, six-day week |
| `Documentation/WM_RECONCILIATION_REGISTER.md` | **fourteen conflicts, all open** — the owner's material against the project master |
| `Scripts/wm2_user_package.py` | reads `USER_SOURCE/` and writes the above. Nothing is retyped |

## The two packages are complementary

WM1 never carried a rate or a cost; the owner's estimate supplies them. The owner's R0
does not carry resources, procurement, long-lead manufacture, inspection and test points,
risk or codes; WM1 supplies those. Read together they cover the job. **They are not
alternatives and must not be read as such.**

## What WM2 did NOT do

- **No open item was closed by the reconciliation.** C17 and C21 stay open; WM-V3, WM-V6
  and WM-V7 stay open. WM-V5 and WM-V11 were closed by the **SP-B2 design** in master
  A.4.8, not by anything here.
- **No quantity, rate, cost, duration or date of the owner's was changed** — including
  two arithmetic slips found inside the owner's own files (a 10.00 m³ concrete total and
  a ₹1,00,000 final cost), which are **reported, not corrected**, as R-13 and R-14.
- **No WM1 document was rebuilt.** `SP-06`, the provisional lintel item, is left as it
  stands even though SP-B2 has now designed the real one — the supersession is recorded
  in the register instead.

**Recorded in master Part H.13.**

---

# REVISION WM3 — 10 September 2026 — the owner's package, revised

**The project owner's own BOQ, cost estimate and construction schedule, with the RC1
rulings applied** (master **Part H.14** and **K.1c**). Requested so the revised Works
Management sits alongside the files that were uploaded.

## Three versions now exist side by side, and that is deliberate

| | Where | What it is |
|---|---|---|
| **As uploaded** | `USER_SOURCE/` | The owner's four files, **byte-for-byte untouched.** Never edit anything in this folder |
| **As supplied, published** | `Cost/USER_BOQ_*`, `Programme/USER_MASTER_CONSTRUCTION_SCHEDULE_R0.*` | The same figures, read out of those files and rendered as CSV/Markdown |
| **REVISED — RC1 applied** | `Cost/REVISED_*`, `Programme/REVISED_MASTER_CONSTRUCTION_SCHEDULE_R1.csv` | **This revision.** Every difference from the as-supplied version is listed in `Cost/REVISED_BOQ_AND_COST_ESTIMATE_RC1.md` |

The revised estimate is issued as **`.xlsx`** as well as CSV and Markdown, so it opens in
the same tool the original came from.

## What the revision applies

| Ruling | Applied |
|---|---|
| **R-1** | Burster slab **300 mm M35 → 200 mm M30**; 57.60 → **38.40 m³**, and Part III falls from ₹5,10,210 to ₹3,40,140 |
| **R-6** | *"Sentry Post RCC Frame & Infill"* → **RC frame only**; the brick infill is measured as brickwork |
| **R-7** | **Escape shaft collars ESC 1 and ESC 2 ADDED** — 6.285 m³ of 250 RC, OD 1900. They were missing |
| **R-8** | **The 15 kVA generator ADDED as a visible line.** The bill priced the 2 600 m³/h combustion air path through BV-4/BV-5 but not the machine |
| **R-13** | Concrete total is now **the sum of its own lines**, 467.59 m³ |
| **R-14** | Final cost is now **the sum of its own cost heads** — this closes the ₹1,00,000 gap |
| **R-2 · R-3 · R-4 · R-5** | **13 programme activities reworded** — the 4 m cover → 2.0 m, the 1000 mm slab → 900 mm, the **lift that does not exist** → "Column & Staircase Shear Wall", and the pre-M1 box size in the title |

**Revised final project cost: ₹2,97,90,913** against the ₹3,00,33,306 stated.

## What the revision does NOT do

- **No rate is invented.** The generator is carried at **zero with DATA REQUIRED**
  against it, so the gap is visible in the bill rather than silent. **The revised total
  is therefore a LOWER BOUND until that line is priced.**
- **No labour figure is invented** for a line the project has no labour data for.
- **The burster-slab reinforcement is not silently changed.** T12 @ 150 both ways is
  11.84 kg/m² *whatever the slab thickness*, so the R-1 thickness ruling does not touch
  it. The owner's tonnage over their own plan area implies about 15 kg/m²; that is a
  separate question and is flagged **[REVIEW]**, not overwritten.
- **The owner's plan area for the cover is left alone.** RC1 ruled on thickness and
  grade, not on area.
- **`USER_SOURCE/` is untouched**, and the as-supplied publication is untouched.

Regenerate with `Scripts/wm3_revised_owner_package.py`. It reads `USER_SOURCE/` and
derives every figure — nothing is retyped.
