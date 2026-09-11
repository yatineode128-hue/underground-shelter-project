# SG1 QA/QC REPORT

**Site Selection and Geotechnical package revision SG1** · 11.09.2026 ·
GEOMETRY REV F + M1 · **FOR REVIEW — NOT FOR CONSTRUCTION**

---

## 1. What was actually checked, and how

| # | Check | Method | Result |
|---|---|---|---|
| 1 | **The supplied report is internally consistent** | Both of its bearing chains recomputed from its own inputs in `sg_calc.py` §G.2 | **PASS.** Soil `SBC = q_ult / 2.5` — **6 of 6**. Rock `UCS = P/A` — **6 of 6**. Rock `SBC = UCS / 25` — **6 of 6** |
| 2 | **The master's BOQ rock quantity reproduces** | Plan area back-figured from `E-02b` at the mean rockhead, then checked against the BOQ's own stated range | **PASS.** 196.800 m² gives **1043.04** at `(−)1.500` vs the BOQ's stated **1043.0**, and **944.64** at `(−)2.000` vs **944.6** |
| 3 | **The master's seismic coefficients reproduce from Zone III** | `A_h = (Z/2)(I/R)(Sa/g)` with Z = 0.16 | **PASS.** Box **0.0750** vs 0.075; sentry **0.1000** vs 0.100 |
| 4 | **The master's bearing utilisations reproduce** | `q / 3240` for all three checks | **PASS.** 1.80 %, 12.50 %, 4.86 % — the master states 1.8 %, 12.5 %, 4.9 % |
| 5 | **γ_sat back-figured agrees with the master** | `e` from the measured MDD, then `(G_s + e)/(1 + e)·γ_w` | **PASS within 1.2 %** — 21.26 against the assumed 21.00 |
| 6 | **No evidence tag was converted** | `git diff` on `master/MASTER_PROJECT_STATE.md` reviewed line by line | **PASS.** No `[ASSUMED]` became `[CONFIRMED]`; none deleted or downgraded |
| 7 | **No design value moved** | `git status` across every other package directory | **PASS.** No file outside this package and the two `master/` files is modified |
| 8 | **Every other package regenerates byte-identically** | `dr_build_all`, `hv_build_all`, `cm_build_all`, `fs_build_all`, `em_build_all`, `el_build_all` re-run; geometry compared | **PASS** — see §4 |
| 9 | **Drawings validate** | `Drainage/Scripts/mep_validate.py` — the project's own validator | **PASS. 3 files, 0 errors, 0 warnings** |
| 10 | **No text-on-text overlap** | `DRAWING QAQC/Scripts/dxfqa.py` | **PASS. 0 overlaps on all three sheets** |
| 11 | **Nothing outside the sheet or in the title block** | same | **PASS.** See the note on `into_titleblock` in §3 |
| 12 | **Schedules, calculations, report and drawings cannot disagree** | All four read the same `sg_data.py` / `sg_proj.py`; no value is typed twice | **PASS by construction** |
| 13 | **The main staircase is unchanged** | `git diff` on every file containing `170.8333`, `24R`, `280` | **PASS.** Not one of those files is touched by SG1 |

## 2. What was **not** checked, and cannot be

| Item | Why |
|---|---|
| **Whether the SEMT data applies to this plot** | It is a report for three *other* buildings. The carry-across is an `[A]` of this package — `SG-V1` |
| **Anything below about 1.5 m** | No data exists. This is `SG-F2`, the governing finding, not an oversight |
| **The Google Maps pin** | The session's egress policy refused `maps.app.goo.gl` (403, recorded). No coordinate was read and **none was invented** — `SG-V9` |
| **Which annual rainfall figure is right** | The two documents disagree and neither names a station or period. Published tertiary figures for "Pune" span ~720 to >1 000 mm. **No third figure is adopted** — `SG-V5` |
| **Whether the October rainfall figure is wrong** | It does not fit a Deccan monsoon distribution, which is stated. **It is not corrected** — correcting a datum whose source is unknown would be inventing evidence |
| **The date of the SEMT field work** | Not stated anywhere in the report — `SG-V10`. The pre-monsoon inference is tagged `[U]`, not asserted |
| **Any structural re-analysis** | **STAAD.Pro was not run.** No `.std` file was opened or modified |

## 3. Declared deviations and known baseline flags

| Item | Position |
|---|---|
| `dxfqa.py` reports **`into_titleblock: 20`** on each SG sheet | **Not a defect, and not new.** The checker exempts only the `S-TITLE` layer; every sheet built on the shared `mep_dxf` library puts title-block text on `M-TITLE`. Verified against `EM-001` and `E-001`, which report **the same 20**. The flagged strings are the title block's own content (`DRAWING No.`, `SG-001`, `REV`, `SG1`, …) |
| `SG-101` carries a **NOT A SITE PLAN** banner | Deliberate. The setting diagram has **no scale, no boundary, no dimension and no coordinate**, and saying so on the sheet is the only honest way to draw it. Master gap **D3 stays open** |
| `SG-201` leaves the ground below `(−)1.500` **empty and hatched as NO DATA** | Deliberate, and it is the point of the sheet. The space carries a list of what a real investigation would have had to put there |
| The **sentry post is in scope** on these sheets | Ground only — footing F1 bears on in-situ basalt at `(−)2.000`, which is a geotechnical statement. **No sentry structural value is touched.** The `SCOPE_NOTE` and `TB_SCOPE` say so on every sheet |
| Sentry F1 is drawn **beyond a break** on `SG-201` | Its site position is `[ASSUMED]` — master **U4**, no coordinate exists — so no distance is implied. Same treatment `CAM2` gave it on `C-101` |
| Two γ values in `G.5` and three in `G.8` are `[A]` | Unit weights for the net-pressure and saturated-cover checks. Both are labelled on the line and neither changes a design value |

## 4. Byte-identity of the other packages

`sg_dxf.py` **subclasses** `Drainage/Scripts/mep_dxf.py` and uses only the
`SCOPE_NOTE` / `TB_SCOPE` / `DATE` class attributes that CAM2 / FS2 added.
No shared module was edited. Every other package's generators were re-run and
their outputs compared; the only differences are the DXF timestamp and GUID
fields ezdxf writes on every save.

| Package | Generators re-run | Geometry |
|---|---|---|
| Drainage · HVAC · Schedule of Finishes | `dr_build_all` · `hv_build_all` | **unchanged** |
| Fire and Life Safety · Site and Concealment | `fs_build_all` · `cm_build_all` | **unchanged** |
| EMP Protection · Electrical | `em_build_all` · `el_build_all` | **unchanged** |
| Structural CAD | not re-run — SG1 does not touch `sc_dxflib.py` | **unchanged** |

## 5. Status

**NOT CONSTRUCTION-READY**, and neither is the investigation it reports on.

Ten open items, `SG-V1` to `SG-V10`, are listed in
`Documentation/SITE_SELECTION_AND_GEOTECHNICAL_REPORT.md` §17 and in master
`K.1b`. **None is resolved, and that is deliberate** — each needs something
the project does not contain.

The single item that matters most:

> **The sub-soil investigation reached about 1.5 m. The structure founds at
> `(−)6.800`.** Programme activities `A1075` (confirmatory site investigation,
> 12 d) and `A1080` (groundwater monitoring, 20 d) are both on the **critical
> path** and both still have to happen — and `A1080`'s window, 12 November to
> 4 December, **is not in the monsoon** (`SG-F7` / `SG-V3`).
