# DRAINAGE DESIGN BASIS

**Underground CBRN-hardened blast-resistant protective structure — Pune, Maharashtra**
Package **DRAINAGE**, revision **DR1** · 5 September 2026 · geometry **Rev F + M1**
Status: **DEVELOPED FOR PROJECT COORDINATION — PENDING ENGINEERING VERIFICATION**

**Sentry post is excluded from this package.** No sentry post drainage is designed, drawn,
scheduled or quantified here. Historical sentry post information elsewhere in the project is
untouched.

---

## 1 Authority and evidence

`master/MASTER_PROJECT_STATE.md` governs. Where a value already exists in the project it is
carried forward unchanged and cited; nothing is re-derived to suit this package. Evidence
classes are the master's own:

| Class | Meaning in this package |
|---|---|
| `[C]` CONFIRMED | traceable to the master, to a Rev F architectural drawing, or to issued sheet S-06 |
| `[R]` RECONSTRUCTED | computed here from confirmed values; the arithmetic is in `Calculations/DR_CALC_OUTPUT.txt` |
| `[A]` ASSUMED | an engineering selection made by this package — confirm before construction |
| `[U]` UNRESOLVED | competing values exist in the project |
| `[N]` NOT AVAILABLE | no source exists anywhere in the project — **DATA REQUIRED** |

Codes are cited only from the master Part G register (`IS 2470 Pt 1`, `IS 2470 Pt 2`,
`IS 456`, `IS 3370`, `IS 4991`, `NBC 2016 Pt 4`). Codes outside that register
(`IS 1742`, `IS 5329`, `NBC 2016 Pt 9`) are named **by title only** — no clause is quoted from
them, because no code document is in the workspace (master open item M2).

### Principal source — sheet S-06

`current/cad/06_Underground_Plan_Services_Sump_BlastValves.dxf`
*Underground plan — services and drainage · sump pit · blast valves · septic tank · soak pit*, Rev A.
It already carries the sump, the discharge train, the septic tank, the soak pit, the decon
effluent tank and a design-flow table. **This package develops the system around those decisions;
it does not replace them.** Two arithmetic/currency conflicts found in S-06 are recorded in §9 and
are **not** silently corrected.

---

## 2 Drainage concept

The structure is a **tanked box**, not a drained one. That single decision sets the whole strategy.

```
                              rain
                                |
   grade 0.000, crowned, falls 1:50 away  ────────────────────────────────
                                |                        |
                        sheds at the surface      infiltrates the 300 topsoil
                                |                        |
                        berm toe / ground          150 GRANULAR FILTER layer
                                                          |
                                                    disperses at the berm toe
   ──────────────────────────────────────────────────────────────────────
                        CONTINUOUS TANKING MEMBRANE  (R-805)
   ──────────────────────────────────────────────────────────────────────
                        residual seepage through the tank
                                |
                        floor gullies, falls in the screed
                                |
                        CLEAN SUMP  3.375 m³, invert (−)7.600
                                |
                        2 × 1.5 L/s submersible + hand pump
                                |
                 isolation valve → gas-tight NRV → blast check valve → deep-seal trap
                                |
                        DN50 rising main through the SERVICE ENTRY PLATE
                        (the only penetration of the protective envelope)
                                |
                        STORM SOAKAWAY   —   separate from foul
```

Four rules follow, and every drawing in the set obeys them:

1. **Nothing penetrates the roof.** The 900 pressure slab carries 2.0 m of engineered cover whose
   second metre is bought for prompt neutron and gamma attenuation (master A.7.3). A rainwater
   outlet, a vent stack or a soil stack through that cover would breach both the radiation mass
   and the roof membrane. There is no downpipe on the buried roof and none is added. `[C]/[A]`
2. **One envelope crossing.** S-06 records the service entry plate as *"the only penetration of the
   envelope"*. The sump rising main uses it. No second drainage penetration is created. `[C]`
3. **Three streams, never combined.** Clean (seepage/condensate) → storm soakaway. Foul
   (peacetime) → septic tank → soak pit. Decon effluent → 1000 L tank → **tanker only**. S-06 is
   explicit: *"DECON EFFLUENT NEVER ENTERS THE CLEAN SUMP"* and *"STORM SOAKAWAY — CLEAN SUMP
   DISCHARGE. SEPARATE FROM FOUL."* `[C]`
4. **Drainage is not in the safety path.** Rev F drawing 5 note 9 states this for the entry
   stairwell and it is held for the whole system: no drainage failure may block egress, breach the
   envelope or flood an entrance.

---

## 3 Above-ground and entry drainage

| Element | Basis |
|---|---|
| Finished grade | 0.000, crowned, **falls 1:50 away** from the structure `[C]` A.4.3 |
| Berm | 1.5:1 to +0.900, toe at grade over 1350, graded over ESC 2 `[C]` A.4.7 / ground plan |
| Headhouse roof | 4800 × 5800 = **27.84 m²**, top +0.900, no earth cover `[C]` A.4.6 |
| Covered stairwell roof | 6800 × 2000 = **13.60 m²**, 250 RC raking, soffit +2.200 at the head `[C]` A.4.7 |
| Threshold protection | **300 channel + grating** across the full 1500 width at X 8950–9250; ground falls away 1:50 for 2000 `[C]` |
| Entry door | 1000 × 2100 at grade, opens outward, **threshold flush with a 50 weather bar** `[C]` drawing 5 |
| Headhouse floor | −2.000 = top of the pressure slab, **floor gully, fall 1:80**, hose-down point `[C]` ground plan |
| Headhouse gully outfall | **trapped gully → external soakaway, NEVER to the clean sump** `[C]` ground plan |
| Platform | −2.000, 1500 × 1500, **gully to a 1.0 m³ sump** with its own soakaway `[C]` drawing 5 / A.4.7 |
| Stairwell sump | 1.0 m³, pump 2 L/s duty + standby, NRV on the rising main `[C]` drawing 5 note 9 |

**Rainwater strategy.** The roofs and the engineered cover shed at the surface; there is no piped
roof drainage anywhere on the project. Surface water is kept away from the entrance by three
independent measures already in the architecture — the door is at grade rather than at the foot of
a pit, the ground falls away 1:50 for 2000, and a channel and grating cross the threshold. Rev F
drawing 5 note 5: **"with the door shut the catchment is zero."**

Catchment flows at the recorded **50 mm/h** (`[C]` drawing 5 note 1), C = 1.00 conservative `[A]`:

| Catchment | Area m² | Q L/s |
|---|---|---|
| Headhouse roof | 27.84 | 0.387 |
| Covered stairwell roof | 13.60 | 0.189 |
| less overlap of the two footprints | −0.61 | −0.009 |
| Engineered cover over the box | 136.40 | 1.894 |
| **Sub-total — structures and cover** | **177.23** | **2.461** |

> **The site-wide catchment cannot be closed.** No site plan, boundary, contour, external paved
> area or hardstanding exists in the project. `[N]` The table above is complete for the structures
> themselves and for nothing else.

---

## 4 Groundwater and the water table

| Parameter | Value | Class |
|---|---|---|
| Design GWT | **(−)2.000** monsoon | `[A]` master A2 — *the single most important number in the project* |
| Ground | Deccan basalt with red-bole / vesicular seams at flow contacts | `[A]` A.6 |
| Rockhead | (−)1.500 to (−)2.000 | `[A]` A.6 |
| Structural seepage through the tank | **0.5 L/m²/day** | `[A]` master A8 |
| Wetted external envelope | **401 m²** — verified `[R]` | see below |
| Resulting seepage | **200 L/day** | `[C]` S-06 |

**Verification of the 401 m² (calculation D.1).** S-06 gives the seepage as
`0.5 L/m²/day × 401 m²` without saying what the 401 m² is. It reconstructs exactly as the external
envelope standing below the design GWT:

```
submerged wall height   (−)2.000 → (−)6.700              = 4.700 m
external perimeter      2 × (22.0 + 6.2)                 = 56.40 m
submerged wall area     56.40 × 4.700                    = 265.08 m²
mat underside           22.0 × 6.2                       = 136.40 m²
                                                   TOTAL = 401.48 m²   ✔ 0.12 % from 401
```

It is **not** the internal wetted area. Recording this matters: if the GWT is confirmed higher
than (−)2.000, the wetted area, the seepage and the sump duty all move together, and the
relationship is now explicit.

**Implications, assessed:**

| Element | Consequence |
|---|---|
| Underground floor | Mat is part of the tank. **Falls are formed in the screed, never cut into the 600 mat** — cutting them would reduce the section and the 75 mm cover to the bottom curtain. `[A]` |
| Retaining walls | Already designed for the full 15.41 kPa/m earth + water gradient (master A.7.2). Not re-opened. |
| Waterproofing | Continuous tank: membrane on the blinding, turned up the external face, lapped to the roof membrane; integral crystalline admixture; two waterstops at every construction joint. `[C]` R-805 |
| Wall/floor junction | Tanking is continuous through it; **no drainage channel is formed at the junction** — a perimeter channel here would sit exactly where the membrane lap is. `[A]` |
| Sump | Cast monolithic with the mat, membrane dressed around the pit, 4-T20 trimmers each face/side. `[C]` S-06 / F.1 |
| Uplift | **Not re-opened.** Master B.3 designs it: 46.11 kPa, 6289 kN, staged flotation, mandatory mitigation. A drainage package has no standing to revisit it, and there is no new data. |

> **The box is never drained to relieve groundwater.** A relief drain under the mat would defeat
> the tank and would not reduce uplift by design intent — the structure is held down by mass and
> by the staged construction sequence, not by pressure relief. The only temporary relief permitted
> is the six construction-stage knock-out plugs already specified on S-02, grouted after backfill.

---

## 5 Underground drainage

**Collected:** structural seepage 200 L/day `[C]` + condensate and washdown 200 L/day `[C]`
= **400 L/day = 0.00463 L/s** `[R]`.

| Item | Adopted | Class |
|---|---|---|
| Floor falls | transverse **1:80** wet areas (lavatory, CBRN plant, decon airlock), **1:100** elsewhere, 2500 run each side to the spine; spine **1:400** east to the sump along Y 3100 | `[A]` — 1:80 matches the confirmed headhouse gully fall |
| Fall formed in | **floor screed**, 25 mm minimum at the sump edge rising to 78 mm at the far corner; **area-average 52 mm** | `[A]` / `[R]` |
| Gravity drains | **DN100** minimum, laid at 1:100 minimum | `[A]` |
| Full-bore capacity, DN100 at 1:100 | 6.72 L/s at v = 0.85 m/s — self-cleansing | `[R]` |
| Capacity ratio against the design flow | **1450 : 1** | `[R]` |
| Traps | **75 mm deep seal** throughout, primed | `[A]` — see §6 |
| Rising main | **DN50**, v = 0.76 m/s at 1.5 L/s; welded or flanged, no push-fit joint inside the envelope | `[A]` |

Internal drainage is governed by **minimum bore and self-cleansing velocity, not by flow** — the
capacity ratio is three orders of magnitude. This is stated so that no reviewer looks for a
hydraulic sizing calculation that the flows do not justify. **No washdown or hose design flow is
specified anywhere in the project** `[N]`; if one is issued, branch sizes must be re-checked.

**Effect on clear height (finding DR-F2).** The 3200 clear height is measured between *structural*
surfaces, (−)6.100 to (−)2.900. A drained screed reduces the *finished* clear height to between
**3122 mm** (far corner) and **3175 mm** (sump edge). Ample, but the two figures are different and a
client-facing number must say which one it is. Recorded for the architect; no structural dimension
is changed.

---

## 6 Trap seals against shelter overpressure

The clean zone is held at **+50 to +100 Pa** and leak-tested at **+300 Pa** `[C]`. Any water trap
inside that zone is a pressure boundary — a seal shallower than the overpressure blows through and
the shelter vents to the drain.

| Seal depth | Holds | vs +100 Pa operating | vs +300 Pa test |
|---|---|---|---|
| 50 mm | 491 Pa | 4.9 : 1 | 1.6 : 1 |
| **75 mm (adopted)** | **736 Pa** | **7.4 : 1** | **2.5 : 1** |
| 100 mm | 981 Pa | 9.8 : 1 | 3.3 : 1 |

**75 mm deep-seal traps** are adopted throughout bays 1–6 and on the sump discharge train `[A]`.
Every trap inside the envelope must be **primed** — an unused floor gully evaporates dry and then
leaks air in both directions, which in a pressurised CBRN envelope is a breach, not a smell. Trap
primers, or a written weekly priming task on the O&M card, are mandatory.

---

## 7 Sewage and wastewater

### 7.1 What the project already decides

- **In protective mode the shelter is sealed and uses sealed-cassette chemical toilets — nothing is
  discharged.** `[C]` S-06
- The **septic tank serves peacetime use only**, design population **10** described on S-06 as
  *"sentry-post shift crews + shelter maintenance"*, 45 lpcd → **450 L/day**. `[C]`
- Septic tank **1.5 × 0.75 × 1.0 m liquid** to IS 2470 (Pt 1) Table 1; two compartments, baffle at
  ⅔ L, inlet and outlet tees, 50 mm cowled vent ≥ 2 m above grade. `[C]`
- **Soak pit 2.0 m dia × 3.5 m effective**, side area only counted, IS 2470 (Pt 2). `[C]`
- Decon effluent from airlock stages 1 and 2 → **1000 L tank, tankered out after the all-clear**. `[C]`

> **Scope note.** The 10-person septic design population is taken **verbatim** from S-06 and is not
> re-derived. It explicitly includes crews from the sentry post, which is outside this package's
> scope; only the tank that already exists in the project is carried forward, and no sentry post
> connection is designed, drawn or scheduled here.

### 7.2 Re-checks performed (calculations D.9, D.10)

Septic tank — **every IS 2470 (Pt 1) check reproduces the S-06 values exactly**:
450 L detention + 600 L sludge = 1050 L required against 1125 L provided (+7.1 %); L/B = 2.0;
B = 750; depth 1.00 m; freeboard 300 → overall 1.30 m. **PASS.**

Soak pit — **a shortfall is found**, see §9 conflict **DR-C2**.

### 7.3 The gap this package cannot close

**Open item D2 — the peacetime foul route from the Bay 2 lavatory is not defined anywhere in the
project.** `[U]` S-06 records cassette toilets in protective mode and a peacetime septic tank, but
no connection between the two. Bay 2 is at (−)6.100 and the septic tank is at grade, so any
peacetime soil discharge from the lavatory must be **pumped**. Two readings are possible:

| Case | Consequence |
|---|---|
| **A — cassette in all modes** (what S-06 implies) | No soil stack, no soil branch, no foul rising main below ground. The 450 L/day is entirely above-ground. Cassette handling route and a wash-down point are needed instead. |
| **B — plumbed lavatory in peacetime** | A macerator or packaged pumping unit, a foul rising main, and **a second penetration of the protective envelope** — a protective-design decision, not a drainage one. |

**Case A is drawn** as the recorded position, with case B shown as a provisional dashed route on
D-203 and clearly labelled. **ENGINEER TO CONFIRM.** No pump, macerator, rising main size or
penetration is specified for case B.

Wastewater sources identified: lavatory wash basin (Bay 2), medical wash-up (Bay 2), decon airlock
stages 1–2 (Bay 6, **segregated**), CBRN plant condensate and dehumidifier condensate (Bay 5),
generator bay washdown (Bay 8, outside the gas-tight envelope), headhouse hose-down point (−2.000).
Fixture counts and outlet positions beyond those recorded above are **`[N]` DATA REQUIRED** — no
sanitary fixture layout exists in the project.

---

## 8 Discharge strategy

| Stream | Flow | Store | Discharge | Class |
|---|---|---|---|---|
| Seepage + condensate/washdown | 400 L/day | clean sump 3.375 m³ (8.44 days) | **storm soakaway**, 2.0 dia × 3.5 eff., 20.0 m² required / 21.99 m² provided | `[C]` flows / `[A]` pit |
| Foul, peacetime | 450 L/day | septic 1.125 m³ | **soak pit**, 22.5 m² required / **24.19 m² provided, +7.5 %** — DR-C2 **CLOSED by RC1**, SK-01 widened 2.0 → 2.200 dia | `[C]` / `[R]` |
| Decon effluent | on use | 1000 L tank | **tanker only** | `[C]` |
| Stairwell surface water | 1 m³ / 32 h | 1.0 m³ sump | **own soakaway**, 54.6 h to empty — **DR-F3** | `[C]` / `[R]` |
| Headhouse washdown | on use | trapped gully | **external soakaway** | `[C]` |
| Roofs and cover | 2.46 L/s | none | sheds at grade to the berm toe | `[R]` |

> **FINAL DISCHARGE OF THE WHOLE SITE IS TO GROUND, ON SITE.** No municipal sewer connection, no
> municipal storm connection, no outfall and no receiving watercourse appears anywhere in the
> project. Whether any is available at this site is **open item D3 — DATA REQUIRED** `[N]`.
> Every discharge above therefore rests on the **percolation test**, which master A7 already makes
> mandatory and which is on the critical path for three independent reasons (§9).

---

## 9 Findings and conflicts raised by this package

| Ref | Item | Status |
|---|---|---|
| **DR-C1** | **S-06 carries a superseded catchment.** The design-flow table gives 0.10 L/s for "stairwell / approach surface water". That is the **Rev E open-cut** figure — 7.2 m² of open pit at 50 mm/h, reproduced exactly in calculation D.8. At Rev F the approach is covered, the door is at grade and note 5 states the catchment with the door shut is zero; the governing case is note 9's door-open driving-rain rate, ≈ 12 × smaller. **Conservative, nothing unsafe.** Not corrected here — S-06 is issued. **Both figures shown on D-103.** **RULED AND CLOSED by RC1**, 10 Sep 2026 (master Part H.14 / K.1 U12): **Rev F governs** (precedent C1 — the drawing governs), and the 0.10 L/s **stays as a declared conservatism** because removing it changes no pump, pipe or pit and deleting a superseded number would hide the history. |
| **DR-C2** | **Soak pit was 2.3 % short on its own stated requirement.** S-06 prints "22.0 m² OK" against "area required 22.5 m²". π × 2.0 × 3.5 = **21.99 m² < 22.50 m²**. Arithmetic, not judgement. **RULED AND CLOSED by RC1, 10 Sep 2026** (master Part H.14 / K.1 U11): **SK-01 is WIDENED, diameter 2.0 → 2.200 m, effective depth UNCHANGED at 3.500 m → π × 2.2 × 3.5 = 24.19 m² against 22.50 required, +7.5 %.** Widened rather than deepened because deepening drives the pit further below the design GWT at (−)2.000, where it cannot soak at all. SK-02 follows it so the two pits stay one construction detail. **The mandatory percolation test (A7) still governs the final size and form.** |
| **DR-F1** | Clean sump cycles once every **3.4 days**, 15 min per start, 0.31 % duty ratio. Cycling is fine; at that duty a failed standby would never be discovered by use. **Witnessed monthly test of the standby path and the hand pump** is required in O&M. |
| **DR-F2** | Drained floor screed reduces the **finished** clear height by 25–56 mm from the structural 3200. Recorded for the architect. No structural change. |
| **DR-F4** | **A drained floor cannot be built inside the 1.0 kPa mat SIDL allowance.** At 24 kN/m³ that allowance buys 42 mm of screed; the adopted grading averages **52 mm = 1.24 kPa**, an excess of **0.24 kPa = 25 kN** over the 104 m² floor — 1.2 % of the mat's own weight, 0.4 % of the 6289 kN uplift, and acting in the **favourable** direction for flotation. **Referred to the structural engineer, not assumed.** |
| **DR-F5** | **The protective boundary creates three hydraulic zones and two of them have no drainage destination.** Zone 1 (bays 1–5) → clean sump, complete. Zone 2 (bay 6 decon) → its recorded tank TK-01, which S-06 draws in **bay 8, across the boundary** — route undefined. Zone 3 (bays 7–8) → nothing recorded. A protective-design decision, not a drainage one. |
| **BW-01** | **Builder's work, requested and not accepted.** PD-01, the only buried drain inside the envelope, needs a 300 wide recess in the top of the mat, 150 deep rising to 216, leaving 384 of the 600 mat locally on the line of the peak transverse sagging moment. **Structural engineer to accept or refuse**; a fallback with no buried drain at all is drawn on D-201 note 5. |
| **DR-F3** | Stairwell soakaway needs **54.6 h** to recover from one sump-full at the assumed absorption rate — poor for a rainwater soakaway. Not a layout defect; it is the `[A]` absorption rate showing through. Third independent reason the percolation test is critical. |
| **DR-D1** | Rainfall intensity **50 mm/h** is the only intensity in the project. No return period, duration or IDF source. **VERIFY against IMD Pune data.** |
| **DR-D2** | Peacetime foul route from the Bay 2 lavatory undefined — §7.3. **ENGINEER TO CONFIRM.** |
| **DR-D3** | No site plan, boundary, contour, well position or municipal connection exists. IS 2470 (Pt 2) offsets (≥ 15 m from a well, ≥ 5 m from the septic tank, ≥ 2 m from a building) **cannot be demonstrated**. **DATA REQUIRED.** |
| **DR-D4** | Decon effluent tank emptying route is not defined. Emptying a 1000 L tank inside a gas-tight envelope either waits for the airlock to open or needs a second envelope penetration — **a protective-design decision, not a drainage one**. Flagged, not decided. |

**Carried, not resolved:** master **C16** (roof/platform junction), **C18** (sump pit base 300 vs
400 — 400 held), **A2** (GWT), **A7** (absorption), **A8** (seepage rate). None is resolved by this
package. See §10 and `QAQC/DRAINAGE_QAQC.md`.

---

## 10 C16 dependency — declared, not resolved

Master **C16** is open: A.4.7 says the stairwell roof *"over the platform becomes the 500 headhouse
roof"*, while B.6, A.7.6 and F.2 design, load and register a **250** roof, and the headhouse
footprint (Y 200–6000) does not overlap the platform (Y 6000–7500).

**Where drainage touches it:**

1. **Roof catchment allocation.** The 1500 × 1500 platform roof area (2.25 m²) belongs to the
   stairwell roof at 250 or to the headhouse roof at 500 depending on the ruling.
   **The total catchment is identical either way** — 177.23 m² — so no flow, pipe or pit in this
   package changes. Only the line on D-102 between the two catchments moves.
2. **Platform gully position.** The platform gully to the 1.0 m³ sump `[C]` sits directly under the
   junction. A 250/500 step in the roof soffit above it changes where water is delivered and
   whether a drip is needed at the step.

**Action taken:** the gully is drawn at its confirmed platform position; the roof above it is drawn
**at 250 to match the model and the structural register**, with the junction shown as an explicit
flag on D-102, D-103 and D-301. **C16 is now RULED AT 250 and CLOSED** (RC1, 10 Sep 2026,
master Part H.14): A.4.7's clause has been corrected, this package drew 250 already, and the
total catchment is unchanged at 177.23 m² either way. **No
irreversible assumption is made** and no drainage dimension depends on the outcome.

---

## 11 Coordination requirements

| Interface | Requirement |
|---|---|
| **Structure** | No drainage penetrates the 900 pressure slab, the 600 mat or the perimeter walls except the sump rising main through the service entry plate. Sump pit is monolithic with the mat. |
| **Waterproofing** | Every pipe crossing the tank needs a puddle flange welded to the sleeve and the membrane dressed and clamped to it — R-805 detail principles, D-304. |
| **Architecture** | Floor falls, screed thickness, gully positions and the finished floor level must be read together with the Schedule of Finishes package (FN1) — the same screed does both jobs. |
| **HVAC** | Dehumidifier and cooling-coil condensate (Bay 5) discharges to the clean sump through a 75 mm trapped connection with an air gap; duct routes and drain routes are coordinated on D-201 / M-101. |
| **Electrical** | Sump level control, high-level alarm, auto-alternation and the standby-test facility are an electrical scope item; the alarm must annunciate in the ops room (Bay 3). |
| **Blast / CBRN** | The gas-tight NRV, blast check valve and deep-seal trap on the sump discharge are protective components. Any change to the discharge train is a protective-design change. |
| **Frozen geometry** | Main staircase 24R @ 170.8333 / 280 — **no drainage element is placed in the flights, the well or the landings**, and nothing in this package alters the stair. |

---

## 12 What this package does not claim

- It is **not** construction ready and **not** a final design. Status is *for review*.
- No hydraulic model, no site survey and no percolation test has been performed.
- The pipe network is developed to a coordination level: routes, gradients, minimum sizes, invert
  levels at fixed points, and the capacity check that shows flow is not the constraint.
- Pump **heads**, fixture counts, external chamber positions and the site outfall are **not**
  determinable from the information in the project and are flagged, not filled in.

---

**Prepared under package revision DR1.** Calculations `Calculations/DR_CALC_OUTPUT.txt`
(reproducible: `python3 Scripts/dr_calc.py`). Drawing register
`Documentation/DRAINAGE_DRAWING_INDEX.md`. QA/QC `QAQC/DRAINAGE_QAQC.md`.
