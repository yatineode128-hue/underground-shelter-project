# ELECTRICAL AND POWER — package README  ·  revision EL1

**Underground CBRN-hardened blast-resistant protective structure — Pune**
11 September 2026 · Geometry **Rev F + M1** · **FOR REVIEW — NOT FOR CONSTRUCTION**

---

## Why this exists

**"No electrical design package exists" was the project's largest single gap** (master H.10), and
three packages were stuck behind it by their own words — **FS-V2** (no detection, alarm or
emergency lighting: *"follows the missing electrical design"*), **EM-V2** (EMP Zone 2 dimensions
await an equipment schedule), and **HVAC P11** (*"distribution, UPS and battery autonomy are an
electrical scope item, not designed here"*).

**This is the minimum that unblocks them — and no more.** It stops at **board level**.

## The two things worth knowing

1. **The 15 kVA generator is right.** Connected load **6.256 kW / 7.360 kVA** against 15 kVA is
   **49 % utilisation** — about twice the demand, in the healthy loading band for a diesel set.
   **The project's own figure needs no change.**

2. **The battery is either a cabinet or a room, and the project does not contain the sentence
   that decides which.** Mode 3 CLOSED says *"all five blast valves shut"*; Mode 5 says *"BV-4
   and BV-5 open"* and *"independent of modes 1–4"*. Both are confirmed, both are in the same
   schedule, and **BV-4/BV-5 are two of the five**. If the generator can restart after the shock
   the battery is **149 Ah**; if it cannot, it is **1 783 Ah and 2.4 tonnes**, needing 4.8 m² of
   floor in a bay that is already 80 % full. **12× apart. That is EL-V1.**

## What is here

| | |
|---|---|
| `Documentation/ELECTRICAL_DESIGN_BASIS.md` | **The main document** — sources · load schedule · the generator check · EL-V1 · the battery · distribution and cable entry · what it did not do · **what it unblocks** · EL-V1…V7 · QA/QC |
| `Calculations/EL_CALC_OUTPUT.txt` | Every figure with its inputs, formula and arithmetic |
| `Schedules/` | `LOAD_SCHEDULE` and `DISTRIBUTION_AND_ESSENTIAL_SCHEDULE`, each `.md` + `.csv` |
| `DXF/E-001_Single_Line_Diagram.dxf` | One A1 sheet. Sources, changeover, three boards, the battery, the EMP Zone 2 sub-board through its PCI |
| `Scripts/` | `el_proj.py` · `el_calc.py` · `el_schedules.py` · `el_dxf.py` · `el_sheets.py` · `el_build_all.py` |

## Rebuild

```
python3 "Electrical/Scripts/el_build_all.py"
```

## What it does NOT do

**No circuit schedule, no cable sizing, no luminaire or socket layout, no protection or
discrimination study** (a fault level needs the incoming supply capacity, which is `[N]`).
**No design value, BOQ quantity, rate, date or float is changed. No new envelope penetration.**
Main staircase untouched, sentry post excluded. **Nothing is resolved** — seven open items
**EL-V1…EL-V7** are raised.
