# SCHEDULE OF FINISHES — README

Revision **FN1**, 5 September 2026. Geometry **Rev F + M1**. **Sentry post excluded.**
Status: **FOR REVIEW — NOT FOR CONSTRUCTION.**

## What this package is

**No finish specification exists anywhere in this project.** The master, the ten Rev F drawings,
sheet S-06 and the Structural CAD package fix concrete grade, cover, waterproofing, crack control
and bar spacing — and nothing about what a surface is finished with.

So this package does **not** report finishes as project facts. Every code is a **performance
requirement** derived from something the project *does* confirm:

| Requirement | Comes from |
|---|---|
| Decontaminable, coved, joint-free finishes in bays 1–6 | The gas-tight CBRN envelope, master A.2 |
| Wet-area treatment in U-02, U-05, U-06 | Room uses, master A.3 |
| Non-slip decontaminable finish in the stair shaft | Master A.5 designates those faces a **wet/dirty zone** — it is why their cover is 30 and not 40 |
| Non-slip external finish in the covered stairwell | Outside the protective boundary, **declared expendable**, master A.2 |
| Hose-down finish and 1:80 fall in the headhouse | Confirmed on the Rev F ground plan |
| EMP Zone 2 enclosure in U-03 | Master A.3 and K.3 |
| Cast-in fixings only | 40 mm cover, 150 bar spacing as an EMP requirement, the membrane, the cage |
| No suspended ceilings or cavities anywhere in the envelope | HVAC HV-F2, drainage inspectability, decontamination |
| Floor build-up limited | The 1.0 kPa mat SIDL allowance, drainage finding DR-F4 |
| Cast-in stair nosing, no tread build-up | **The stair going is frozen** |

**The product that satisfies each requirement is left open.** `Schedules/FINISHES_DATA_REQUIRED.md`
lists all nine missing items. A schedule that filled them in would be inventing a specification.

## Read in this order

1. `DXF/A-601` — the four rules and what is *not* specified.
2. `Schedules/FINISH_LEGEND.md` — every code and where its requirement comes from.
3. `Schedules/ROOM_FINISH_SCHEDULE.md` — all 13 spaces.
4. `A-611`, `A-612` — the tagged plans.
5. `QAQC/FINISH_SCHEDULE_QAQC.md`.

## Rebuild

```
cd "Schedule of Finishes/Scripts"
python3 fn_build_all.py
```

## The main staircase

**24R @ 170.8333 · 280 tread · 3 flights × 8 · total rise 4100 · 1200 wide · 200 well · 200 waist ·
headroom 2533.** This package annotates and finishes it and **changes nothing**. The nosing is
specified **cast in, not applied**, and the tread finish carries **no build-up at the nosing** —
both because an applied nosing or a thick tread finish would change the effective going, and the
going is frozen.
