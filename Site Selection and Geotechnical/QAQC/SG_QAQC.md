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

---

# SG2 QA/QC — SITE LAYOUT AND EXTERNAL WORKS

**Revision SG2** · 11.09.2026 · **FOR REVIEW — NOT FOR CONSTRUCTION**

## 1. What was checked, and how

| # | Check | Method | Result |
|---|---|---|---|
| 1 | **Every siting clearance** | Computed from the positions in `sg_site.py` against the rule it must meet — `SG2_SITE_CALC_OUTPUT` §S.3, §S.4 | **PASS. 28 of 28 checks.** Tightest: foul group to excavation **15.49 m** (≥ 15 adopted), pit wall to pit wall **4.20 m** (≥ 4 adopted), soak pit to septic tank **5.40 m** (≥ 5 `[C]`) |
| 2 | **The 50 m envelope holds everything** | Furthest point of every element measured from the pin — §S.2 | **PASS. Worst case 42.5 m of 50 m.** The binding element is the **sentry post**, whose position is `[ASSUMED]` (U4) |
| 3 | **No pipe run crosses the engineered cover** | Every leg of every polyline checked against the box footprint X 0–22000, Y 0–6200 | **PASS.** Runs use the side **backfill** corridor (Y 6200–7200), which is not the cover |
| 4 | **No pipe run crosses an excavation it should not** | `PD-11` was re-routed **west** for exactly this reason — it would otherwise cross the stairwell excavation | **PASS, by re-routing** |
| 5 | **Drawings validate** | `mep_validate.py` | **PASS. 5 files, 0 errors, 0 warnings** |
| 6 | **No text-on-text overlap** | `dxfqa.py` | **PASS. 0 overlaps on all five sheets** — *two were found on `SG-102` on the first pass (the common-trench caption against `SK-02`'s label, and the `PD-16` caption against `IC-02`'s) and both were moved; recorded rather than silently passed* |
| 7 | **Sheet identity is consistent** | Every title block read back from the DXF | **PASS.** All five read rev **SG2**, sheets **1–5 OF 5** |
| 8 | **Nothing outside this package changed** | `git status` across every other package directory | **PASS** |
| 9 | **The drainage design is unchanged** | `SK-01` diameter, effective depth, side area and required area all read from the DR1/RC1 values and reproduced | **PASS — 2.200 dia × 3.500 eff, 24.19 m² vs 22.50, unchanged** |
| 10 | **Every other package still regenerates byte-identically** | All seven re-run | **PASS** — only timestamps, GUIDs and CLASS order differ |

## 2. What was **not** checked, and cannot be

| Item | Why |
|---|---|
| **The ≥ 15 m offset to any well** | **No well position exists anywhere in this project.** Not fudged, not assumed met — `SG2-V1` |
| **Any absolute level in the reserve** | No benchmark exists and the site fall is itself disputed (`SG-V4`). Pit levels are therefore set **relative to local grade**, which is also how a soak pit is built |
| **Whether the percolation rate is 20 L/m²/day** | The test has not been done. `SG2-F1` is deliberately an argument that **does not depend on it** — it is geometry against a stated water level, plus the measured stratum thicknesses |
| **`PD-14`'s route** | It cannot be routed. `GY-11`'s outlet is inside the pressure slab — `SG2-F5`, referred to drainage and structures |
| **The distance to the perimeter fence** | Never dimensioned anywhere — `SG2-V2`. The layout is built to be immune: every offset is relative |
| **Whether the pin is the box centre** | An **adopted convention** `[A]`, stated as one. If it is not, the layout translates rigidly |

## 3. Declared deviations

| Item | Position |
|---|---|
| Four clearance rules are `[A]`, adopted by this package | No pit-to-pit, foul-to-clean or excavation-offset rule is recorded in this project or on S-06. Each is stated **with its reasoning** in `SITING_CLEARANCE_SCHEDULE`, and the pit-to-pit one is explicitly **referred to the geotechnical engineer** |
| `SK-03` and `SK-04` are **reserved, not designed** | Neither is sized anywhere in the project (`[C]`/`[N]` in DR1). Their footprints are reserved to the SK-01/SK-02 detail |
| The three SG1 sheets were **re-issued at SG2** | Content unchanged; only the revision and sheet-count fields move. The SG1 *documents* stay at SG1 — that revision happened and Part H preserves it (`M.11`) |
| `SG2-F1` states a conclusion about SK-01 **without changing it** | The percolation test governs the final size and form — master `A7`, and RC1 said so too. SG2 quantifies and reserves; it does not redesign |

## 4. Status

**NOT CONSTRUCTION-READY.** Five new open items `SG2-V1`…`SG2-V5`; ten SG1
items, of which one is closed (`SG-V9`), one ruled (`SG-V3`) and one amended
(`SG-V5`).

The single item to act on first:

> **`SG2-F1` — the soak pit's problem is depth, not arithmetic.** At this site
> a 3.5 m deep pit is **21–43 % above the design water table** and its only
> demonstrably permeable horizon is **0.2–0.5 m thick**. The percolation test
> (`PT-1` and `PT-2`, positions fixed in §S.8) should be taken at **both** the
> pit invert and the trench invert — or the fallback is undesigned the day the
> pit is abandoned.
