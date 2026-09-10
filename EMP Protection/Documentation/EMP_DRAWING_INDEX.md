# EMP PROTECTION — DRAWING INDEX  ·  revision EM1

**Underground CBRN-hardened protective structure — Pune** · GEOMETRY REV F + M1
EMP Protection package revision **EM1** · 10.09.2026 · **FOR REVIEW — NOT FOR CONSTRUCTION**
**Sentry post excluded.** Main staircase unchanged. **No design value is altered by this package.**

**Six A1 sheets**, AutoCAD 2010 (AC1024) ASCII DXF, 841 × 594 mm, plot 1:1, `$INSUNITS` = 4.
Built on the project's own shared sheet library — `Drainage/Scripts/mep_dxf.py`, which
subclasses `Structural CAD/Scripts/sc_dxflib.py` — so these sheets carry the **same border,
title block, text heights, dimension styles and layer conventions** as the issued R-series
reinforcement drawings and the D / M / A-6xx services drawings. **Nothing in either shared
library was modified.**

| Sheet | Title | Content | Scale | Open items |
|---|---|---|---|---|
| **EM-001** | EMP protection — design basis and EMP zone key | The governing fact · the three EMP zones · the design rule · what the design already does right · all six findings · all six open items · codes | NTS | EM-F1, EM-F3, EM-V1, EM-V2 |
| **EM-101** | EMP zone plan — underground level (−)6.100 | EMP Zone 1 envelope · all ten penetrations with verdicts · EMP Zone 2 enclosure sited in bay 3 · the DN100 / DN350 comparison · the bay 8 decision | 1:50 | EM-F1, EM-F4, EM-V3 |
| **EM-102** | EMP boundary section — the entry path | **Finding EM-F1 drawn**: the open electromagnetic path from grade to bay 7 through the stair void · escape shaft head detail | 1:40 / 1:25 | EM-F1, EM-V6 |
| **EM-201** | Shielding effectiveness — cage and apertures | SE v frequency, 10 kHz – 1 GHz, four curves against the 80 dB requirement · **the master K.3 check** · the upper-bound declaration | NTS | EM-F2 |
| **EM-301** | EMP Zone 2 enclosure — plan, section and siting | The only EMP shield in the project · siting in bay 3 with the 300 survey gap · the five points of entry · verification hold point | 1:25 / 1:20 | EM-F3, EM-V2 |
| **EM-302** | EMP penetration, bonding and earthing details | D1 service entry plate · D2 honeycomb WBC vent panel · D3 blast valve bore · D4 bonding strap · D5 cage continuity at a construction joint · earthing | As noted | EM-F5, EM-V5, EM-V6 |

## Validation

Every sheet was checked with the project's own shared validator,
`Drainage/Scripts/mep_validate.py` — eleven checks per file — and with the QA1 drafting
inspector, `DRAWING QAQC/Scripts/dxfqa.py`.

| | Result |
|---|---|
| `mep_validate.py` — 11 checks × 6 sheets | **0 errors, 0 warnings** |
| `dxfqa.py` — text-on-text overlaps | **0** |
| `dxfqa.py` — entities outside the sheet border | **0** |
| `dxfqa.py` — text past the right-hand sheet edge | **0** |
| Title block on every sheet | **6 of 6** |
| Scope-exclusion note on every sheet | **6 of 6** |

> `dxfqa.py` also reports `into_titleblock: 20` on each sheet. **That is a known false
> positive of that tool against the MEP-family title block** — it whitelists only the `S-TITLE`
> layer, and the MEP title block draws on `M-TITLE`. The issued HVAC sheet `M-101` returns the
> identical count. **No entity outside the title block intrudes into it on any EMP sheet.**

## Regeneration

```
python3 "EMP Protection/Scripts/em_build_all.py"
```

Rebuilds the calculations, the five schedules and all six drawings from `em_proj.py`, then
runs the validator. **Every figure on every sheet is imported from `em_proj` / `em_calc`, so a
drawing cannot disagree with the calculation that produced it.**

## Not issued, and why

| Sheet that does not exist | Why |
|---|---|
| An **EMP Zone 2 fabrication drawing** | The enclosure is `[A]` at every dimension. Fabrication detail would need an equipment schedule, a shielded-door type and a panel system, all `[N]`. **EM-V2.** |
| An **earthing and bonding layout** | Needs the electrode positions, the site plan (`D3`, `[N]`) and the electrical design (`[N]`). EM-302 gives the rules and the arithmetic; the layout cannot be drawn. |
| An **antenna / feeder entry detail** | **There is no antenna, mast, feeder or communications design anywhere in this project.** `[N]` **EM-F6 / EM-V4.** |
| A **sentry post EMP sheet** | The sentry post is excluded from this package, as it is from every other services package. |

**No sheet is invented to fill a gap.** Where the project holds no information, this package
says so and stops.
