# Site Selection and Geotechnical — revision SG1

**11.09.2026** · GEOMETRY REV F + M1 · **FOR REVIEW - NOT FOR CONSTRUCTION**

The project's first site selection and geotechnical section. Until this
revision, master Part J drew `[SITE INVESTIGATION]` as a root node with
**nothing feeding it**, and every parameter in master `A.6` was `[ASSUMED]`
with no source.

## The one fact that governs the package

**The sub-soil investigation reached about 1.5 m. The structure founds at
`(−)6.800`.** Everything the project holds about the ground below `(−)2.000`
— rockhead continuity, red-bole seams, k_s, the design groundwater table — is
extrapolation, and the supplied report cannot be read as confirming any of it.

## What is here

| | |
|---|---|
| `Documentation/SITE_SELECTION_AND_GEOTECHNICAL_REPORT.md` | **the section** — site selection, setting, geology, the investigation, bearing, rockhead, groundwater, seismicity, meteorology, the black cotton soil, 14 findings, 10 open items |
| `Documentation/SG_DRAWING_INDEX.md` | the three drawings and what each is for |
| `Schedules/TRIAL_PIT_SCHEDULE` | the stratum log, `.md` + `.csv` |
| `Schedules/SOIL_PROPERTY_SCHEDULE` | Appendices A and B |
| `Schedules/ROCK_STRENGTH_SCHEDULE` | Appendix C, soaked and unsoaked |
| `Schedules/METEOROLOGICAL_SCHEDULE` | wind, rainfall, temperature |
| `Schedules/GEOTECHNICAL_PARAMETER_RECONCILIATION` | every `A.6` / `K.2` item against the new evidence |
| `Calculations/SG_CALC_OUTPUT.txt` | G.1–G.14, every conversion and check with its arithmetic shown |
| `QAQC/SG_QAQC.md` · `QAQC/SG_DRAWING_VALIDATION.txt` | consistency checks and the DXF validator output |
| `DXF/` | `SG-001`, `SG-101`, `SG-201` — A1, AutoCAD 2010 ASCII |
| `Scripts/sg_build_all.py` | rebuilds the whole package |

## Sources

1. **SEMT/67/15** — *REPORT ON SUB-SOIL INVESTIGATION FOR CTW PH-III ACCN PROJECT AT CME PUNE*, Soil Engineering & Material Testing Wing, College of Military Engineering, Pune 411 031.
   Raised on CTW letter No 8722/Ph-III/CTW/116/Q dated 20 May 2015. **11 trial pits, 3
   locations, no boreholes, no in-situ testing.**
2. **P1 presentation deck** — *CONSTRUCTION OF CBRN HARDENED UNDERGROUND OPS ROOM*, TEAM GROUNDZERO,
   32 slides.
3. **Location pin** `https://maps.app.goo.gl/H2VjnrjS8X8SsXEr9` — **NOT RESOLVED - maps.app.goo.gl refused by the session egress policy (403). Coordinates [N]; supply lat/long to close.**

## What this package does NOT do

- It **resolves nothing**. Master rule `M.6` forbids converting an
  `[ASSUMED]` into a confirmed fact, and not one `K.2` assumption is closed.
- It **does not close master gap D3** (no site plan). Imagery is not a site
  plan.
- It **changes no design value, no `.std` file, no BOQ quantity, no rate, no
  date and no float**, and modifies **no existing file** in any other
  package. The only files outside this directory that change are
  `master/MASTER_PROJECT_STATE.md` (Part `H.22` and cross-references) and
  `master/QUICK_STATE.md`.
- **STAAD.Pro was not run.** Nothing here is an analysis.
- The **main staircase is untouched**.

## Rebuild

```
python3 Scripts/sg_build_all.py
```

Runs `sg_calc.py`, `sg_schedules.py`, `sg_docs.py` and `sg_sheets.py`, then
validates the drawings with the project's own shared validator
(`Drainage/Scripts/mep_validate.py`). `sg_dxf.py` subclasses the shared
`mep_dxf.py` and uses the `SCOPE_NOTE` / `TB_SCOPE` / `DATE` hooks that
CAM2/FS2 added — **no shared library is modified**, so Drainage, HVAC,
Schedule of Finishes, Fire and Life Safety, Site and Concealment, EMP
Protection and Electrical all regenerate byte-identically.
