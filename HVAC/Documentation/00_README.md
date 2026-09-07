# HVAC PACKAGE — README

Revision **HV1**, 5 September 2026. Geometry **Rev F + M1**. **Sentry post excluded.**
Status: **FOR REVIEW — NOT FOR CONSTRUCTION.**

## Read in this order

1. `Documentation/HVAC_DESIGN_BASIS.md` — what the system is, and §2, the reproduction of every
   figure sheet S-06 already carries.
2. `Calculations/HV_CALC_OUTPUT.txt` — every number with its inputs.
3. `DXF/M-001` — notes, design basis and legend.
4. `M-101` → `M-203`.
5. `QAQC/HVAC_QAQC.md`.

## Rebuild

```
cd HVAC/Scripts
python3 hv_build_all.py
```

Regenerates the calculations, all seven schedules, all six A1 sheets and both handout pages, then
validates every DXF. Needs `ezdxf` (and `matplotlib` only for the handout PDF).

## What this package did, and did not, do

**The ventilation basis already existed on issued sheet S-06.** This package does not re-derive it.
It **reproduces all eleven S-06 figures from first principles** — every one checks — and then
develops what S-06 does not carry: room-by-room airflow, duct sizes and velocities, duct pressure
loss, the fan-duty build-up, terminal and damper schedules, routing coordinated against the
structure, and the five operating modes.

**No existing project file was modified.**

## Open items this package raises

`HV-F1` soda lime, not oxygen, limits closed mode · `HV-F2` the raw-air duct is a protective element
· `HV-F3` maintenance access, not headroom, is the tight dimension · `HV-D1` no filter bypass shown
· `HV-D2` BV-3's onward path to atmosphere unrecorded · `HV-D3` no cooling load possible ·
`HV-D4` no noise criterion exists · `HV-D5` dehumidifier duty not stated · `HV-D6` fan static
pressure is vendor data.

Master **C16** is carried with **no HVAC dependency**. **A2** affects only the condensate route.
