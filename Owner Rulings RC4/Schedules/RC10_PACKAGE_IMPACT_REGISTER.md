# RC10 — WHAT THE RULINGS LEFT STALE IN THE PACKAGES

**Revision RC10 · 12 September 2026 · master Part H.34**

Revisions **RC4 to RC9** ruled on thirty-two open items and recorded every ruling in the master.
**They did not touch the discipline packages.** Six artefacts therefore now say something the
master has settled — the same class of defect `RC9` corrected one level up, found by looking for
it rather than by waiting for it.

> **NOTHING IS SILENTLY EDITED HERE.** Every file below is a **build artefact**, regenerated from
> its package's `Scripts/`. The project's rule is to edit the generator and re-run, never the
> artefact — and the EM1, EL1, SG1 and SG2 records each verified that **every other package
> regenerates byte-identically**, which is a property worth not breaking casually. This register
> makes each contradiction **visible and actionable**; applying it is a package-by-package job
> with a regeneration check, and it has not been done.

---

## The six

### 1 · `EMP Protection/Schedules/ENVELOPE_PENETRATION_REGISTER` — BV-4 and BV-5

| | |
|---|---|
| **Says** | *"HONEYCOMB WBC PANEL inboard of the valve — **if** bay 8 is inside the EMP boundary. EM-V3."* |
| **The master now says** | **`EM-V3` IS RULED (RC4, H.28): BAY 8 IS INSIDE.** The conditional is settled |
| **Effect** | The honeycomb panels move from **conditional** to **required**. The verdict stays `FAIL` and the treatment is unchanged — what changes is that it is no longer optional |
| **Generator** | `EMP Protection/Scripts/em_schedules.py` |

> **And a consequence neither document yet states.** RC2 lets the generator run in the closed
> mode, with **BV-4 and BV-5 reopening after the shock**. So the two DN350 bores are **open,
> through the EMP boundary, during exactly the post-attack period the boundary exists for.**
> The honeycomb panels have to work **with the valves open**.

### 2 · Same register — ESC1 and ESC2

| | |
|---|---|
| **Says** | *"BONDED CONDUCTING HATCH AT THE HEAD … **No hatch is specified.**"* |
| **The master now says** | **`EM-V6` RULED AND SPLIT (RC5, H.29).** A hatch **is** specified structurally: 1600 dia ribbed steel weldment, 12 mm face, 8 radial ribs 150 × 10, 150 × 12 perimeter ring, on a steel seating ring cast into the 250 collar, **four quarter-turn dogs against uplift**, counterbalanced, openable from inside |
| **Effect** | *"No hatch is specified"* is **no longer true**. **The EMP half is still open** — the bonding is not designed — so the `FAIL` verdict stands |
| **Generator** | `EMP Protection/Scripts/em_schedules.py` |

> **The register should also carry `RC5-F2`**, which it is the natural home for: **these are 1400
> dia bores through the PRESSURE SLAB, which A.2 names as part of the protective boundary.**
> The register assesses them for EMP only. **Each head is also a 1.54 m² hole in the blast
> boundary**, and the hatch is designed to 383 kPa for that reason.

### 3 · `HVAC/Schedules/HVAC_EQUIPMENT_SCHEDULE` — SH-1

| | |
|---|---|
| **Says** | Location: *"West of the box"* |
| **The master now says** | **`SG2-V3` CLOSED (RC4, H.28): SH-1 is centred (−2400, 3100)**, 600 × 600 occupying X −2700 to −2100, Y 2800 to 3400 `[A]` |
| **Why it is not an invention** | The position was **recovered from the schedule's own note** — *"12.3 m from the intake to the entry"* — and reproduces it to **28 mm** |
| **Generator** | `HVAC/Scripts/hv_data.py` / `hv_schedules.py` |

### 4 · Same schedule — SH-2

| | |
|---|---|
| **Says** | *"East of the box, X 22598-23198"*, and **no head level** |
| **The master now says** | **`CAM-V5` CLOSED (RC4, H.28): head at +1.500**, the same gooseneck head as SH-1 `[A]` |
| **Generator** | `HVAC/Scripts/hv_data.py` / `hv_schedules.py` |

### 5 · `Fire and Life Safety/Schedules/FS_ESCAPE_ROUTE_SCHEDULE` — R2 and R3

| | |
|---|---|
| **Says** | Geometry for each shaft, climbs of **6.250 m** and **6.800 m**, and **no means of climbing** |
| **The master now says** | **`FS-V7` RULED (RC4, H.28): a ladder is designed** — 20 mm galvanised rungs, 400 clear width, equal pitch **297.6 mm (ESC 1, 21 spaces)** and **295.7 mm (ESC 2, 23 spaces)**, ≥ 200 behind the rung, ≥ 750 clear in front, grab rails 1100 above the head |
| **Effect** | Both routes become **demonstrably usable**, which they were not before |
| **AND WHAT THE SCHEDULE MUST STILL SAY** | **No fall-arrest. No rest platform. A vertical ladder cannot pass a stretcher.** `FS-V7` did **not** close — it changed |
| **Generator** | `Fire and Life Safety/Scripts/fs_data.py` / `fs_schedules.py` |

### 6 · `Site and Concealment/Documentation/CAMOUFLAGE_AND_CONCEALMENT_POLICY`

| | |
|---|---|
| **Says** | *"SH-2, whose head level is recorded nowhere in the project"*, and lists **`CAM-V5` as OPEN** |
| **The master now says** | **`CAM-V5` CLOSED at +1.500** (RC4, H.28) |
| **Effect** | The above-ground signature is **complete for the first time**: **+7.000** sentry post · **+2.450** stairwell head · **+1.500 both shaft heads** · **+0.900** headhouse. **`C-101` can draw SH-2 to scale instead of flagging its height `[N]`** |
| **Generator** | `Site and Concealment/Scripts/cm_docs.py`; the sheet from `cm_sheets.py` |

---

## What this register is not

**It is not a design change.** Every value in it is already ruled and already in the master —
Parts **A.4.8**, **A.4.9**, **H.28**, **H.29** and **K.1b**. **The master governs, and it is
right.** These six artefacts are simply behind it.

**It is not a defect list against the packages.** Each was correct when it was written. They went
stale because rulings landed in the master and nobody walked them downstream — **which is the
failure mode this project has now hit twice in two days**, once inside the master (`RC9`) and once
between the master and its packages (here).

> **THE LESSON, RECORDED BECAUSE IT WILL RECUR.** A ruling is not finished when the master
> records it. **Master rule M.14 already says so** — *"cross-check in this order: geometry →
> materials → loads → structural model → analysis → design calculations → reinforcement →
> drawings → revision number. A change that stops at 'reinforcement' and never reaches 'drawings'
> is not finished."* RC4 to RC9 stopped at the master. **This register is where they did not
> reach, written down so the next session can finish them.**
