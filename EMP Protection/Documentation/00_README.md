# EMP PROTECTION — package README  ·  revision EM1

**Underground CBRN-hardened blast-resistant protective structure and sentry post — Pune**
10 September 2026 · Geometry **Rev F + M1** · **FOR REVIEW — NOT FOR CONSTRUCTION**

---

## Why this package exists

**The project has required EMP hardening since Rev F and has never had an EMP design.**

EMP appears in the master's objective (*"CBRN, EMP and fallout hardening"*), in the bay
schedule (*"EMP Zone 2 enclosure"* in bay 3), in the materials table (*"max bar spacing 150 —
an EMP requirement"*), in the code register (**MIL-STD-188-125-1**, **IEEE Std 299**), on
thirty-odd drawings and in eight bar-bending schedules. **It has never once been designed.**
Master **H.10** lists *"the EMP enclosure … specifications"* among the thirteen things the
project does not contain, and the finishes package carries `W-04` — the Zone 2 lining — as
**`[C]` requirement / `[N]` specification**.

This package supplies the design, and says plainly where it could not.

## The one-line finding

> **The concrete box is not an EMP shield and never could have been.** The reinforcement cage
> meets 80 dB over **one decade of the five** MIL-STD-188-125-1 requires, and gives **0.00 dB
> at 1 GHz** — which *reproduces the project's own confirmed figure in master K.3*.
> **So the 80 dB boundary must be the EMP Zone 2 enclosure, and it has never been specified.**

## What is here

| | |
|---|---|
| `Documentation/EMP_PROTECTION_DESIGN_BASIS.md` | **The main document.** Governing fact · what the design already does right · the zone model · every hole in the envelope · the Zone 2 enclosure · bonding and earthing · verification · six findings · six open items |
| `Documentation/EMP_DRAWING_INDEX.md` | The six drawings, their validation results, and the sheets deliberately not issued |
| `Calculations/EMP_CALC_OUTPUT.txt` | Every derivation, printed with its inputs, its formula and its arithmetic |
| `Schedules/` | Five schedules, each as `.md` and `.csv` — zones, envelope penetrations, points of entry, bonding and earthing, shielding effectiveness |
| `QAQC/EMP_QAQC.md` | What was verified, how, and what could not be |
| `DXF/` | Six A1 drawings, `EM-001` … `EM-302` |
| `Scripts/` | `em_proj.py` (constants) · `em_calc.py` (derivations) · `em_schedules.py` · `em_dxf.py` (sheet library) · `em_sheets.py` · `em_build_all.py` |

## Rebuild

```
python3 "EMP Protection/Scripts/em_build_all.py"
```

## What this package does NOT do

- **It changes no design.** No dimension, load, bar, wall, level, valve, duct, pipe, model or
  bill item is altered. It creates **no** penetration of the envelope and moves none.
- **The main staircase is untouched.** Frozen, and annotated only.
- **The sentry post is excluded**, as it is from every other services package. It is above
  ground, framed, brick-infilled and not blast designed; its EMP exposure is total and nothing
  here changes that.
- **It resolves nothing.** No existing `[ASSUMED]`, `[UNRESOLVED]` or `[NOT AVAILABLE]` tag is
  converted, downgraded or deleted. **Six new open items EM-V1 … EM-V6 are raised.**
- **It invents no clause.** Only the EMP entries already in master Part G are cited.
- **It quotes no PCI residual, no threat field and no vendor performance**, because the project
  contains none. Inventing a number would be worse than `[N]`.

## Read it in this order

1. **`EM-001`** — the whole position on one sheet.
2. **`EMP_PROTECTION_DESIGN_BASIS.md` §0** — the governing fact, with the K.3 check.
3. **`EM-201`** — the shielding-effectiveness chart. This is the sheet that settles the argument.
4. **`EM-102`** — the finding drawn: the entry path.
5. **`EM-301`** — what to build instead.
