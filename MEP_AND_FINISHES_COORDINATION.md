# CROSS-DISCIPLINE COORDINATION REPORT

**Underground CBRN-hardened blast-resistant protective structure — Pune, Maharashtra**
Packages **DRAINAGE DR1**, **HVAC HV1** and **SCHEDULE OF FINISHES FN1** · 5 September 2026
Geometry **Rev F + M1** · **FOR REVIEW — NOT FOR CONSTRUCTION**

**Sentry post is excluded from all three packages.** This report covers only the underground box,
the headhouse and the covered entry stairwell.

> This report is a **coordination check performed across the three new packages and against the
> existing architecture, structure, calculations, DXF set and Revit scripts.** It records what was
> checked and what it found. **It resolves nothing that belongs to somebody else.**

---

## 1 How the check was made

The three packages are generated from **one shared set of constants** (`Drainage/Scripts/mep_proj.py`)
and **one shared set of architectural backgrounds** (`mep_views.py`). Geometry cannot drift between
them by construction: the same wall, the same bay and the same level appear identically on a drainage
plan, an HVAC plan and a finish plan because they are drawn from the same numbers.

That removes the ordinary class of coordination error and leaves the interesting one — **conflicts
between what the three packages need of each other and of the structure**. Those are below.

| Axis | Method |
|---|---|
| Architecture ↕ all | Backgrounds generated from master A.3 / A.4, cross-checked against `1_Underground_Level_Plan.dxf` and `2_Ground_Plan_Headhouse_Berm.dxf` |
| Structure ↕ all | Every penetration, recess and imposed load checked against master A.7, B.3 and R-805 |
| Drainage ↕ HVAC | Levels, routes, the shared Bay 5 plant room, condensate, trap seals |
| Drainage ↕ Finishes | Floor falls, screed thickness, the mat SIDL allowance, wet areas, coving |
| HVAC ↕ Finishes | Ceiling voids, plant clearances, duct inspectability |
| Calculations ↕ drawings | Every figure on a sheet is generated from the calculation module that produced it |
| DXF | 24 files, one validator, 11 checks each |
| Revit | Three scripts, one existing model, no duplication |

---

## 2 Coordination findings

### CO-1 — The sump rising main cannot run at low level through Bay 5 ✅ RESOLVED IN THIS PACKAGE

The clean sump SU-01 is at X 11068–12568, Y 900–2400. The service entry plate — the only services
penetration of the protective envelope — is at X 11398–12198 in the north wall, Y 5600–6200. The
direct line between them runs north at about X 11800.

**The two NBC filter trains occupy X 11098–12548 from Y 2700 to Y 5550.** That is the full width of
the bay less **58 mm at the west side and 52 mm at the east**. The direct rising-main route passes
straight through both trains, and there is no room beside them.

**Resolution, made here:** PD-05 **rises at the sump and runs at high level over the trains.**
Recorded on D-201 note 8 and annotated on the plan.

**Consequence, referred:** the **service entry plate must therefore also be at high level, and its
level is not recorded anywhere in the project.** That was already `[N]`; it now has a reason.

### CO-2 — "The only penetration of the envelope" needs reading carefully ✅ RECORDED

S-06 labels the service entry plate *"the only penetration of the envelope"*, and the same sheet
shows five blast valves through the same envelope. Both are correct: the plate is the only
**services** penetration (sleeved pipes, EMP-treated cables, the sump rising main), while the blast
valves are **protective** penetrations with their own recessed chambers and closure devices.

**Both packages have been written so that no reviewer has to reconcile that on their own:** drainage
creates **no** new penetration and HVAC creates **none beyond the five confirmed valves**. Total
envelope crossings across both packages: **six, all of them already in the project.**

### CO-3 — Bay 5 is 80 % occupied as drawn, and the plant master A.3 requires has no space ⚠ RAISED

| Item | Footprint | Area |
|---|---|---|
| Bay 5 clear floor, 1560 × 5000 | X 11040–12600, Y 600–5600 | **7.800 m²** |
| Clean sump SU-01 | 1500 × 1500 | 2.250 m² |
| NBC filter train 1 | 1450 × 1650 | 2.393 m² |
| NBC filter train 2 | 1450 × 1100 | 1.595 m² |
| **Occupied** | | **6.237 m² = 80 %** |
| **Free** | in **four strips**, the widest **300 mm** | 1.562 m² |

**Master A.3 also requires the CO₂/O₂ plant *and* the dehumidifier in this bay.** There is no space
shown for either.

**And Bay 5 is a through route.** The partition door gap into it is at Y 2500–3400 (confirmed,
master A.3); filter train 2 spans Y 2700–3800 across the full bay width. **That leaves 200 mm on the
door line.**

**Two readings, and this package does not choose between them:**

- the plant footprints on S-06 are **indicative zones**, not measured equipment — their X extents sit
  inside the bay by 42 and 52 mm, which is what a drawn-to-fit zone looks like; **or**
- the Bay 5 layout genuinely needs resolving.

**Raised, not resolved** — the plant positions are confirmed on an issued sheet. Recorded on M-101
note 11 and M-001. It also drives HVAC finding **HV-F3**: each train is 1450 wide in a 1560 bay, so
a HEPA and a carbon cassette must be carried in along the bay through Blast Door 1 (1200 × 2100), and
**the cassette dimensions must be checked against that route before the trains are ordered.**

### CO-4 / HV-C1 — The master and S-06 disagree on the filter train duty ⚠ USER RULING REQUIRED

| Source | States |
|---|---|
| **master A.3** (the authority) | Bay 5: **CORRECTED by RC1, 10 Sep 2026** to *"CBRN plant: **2 × 300 m³/h** filters…"*. It previously read **2 × 250**, and that was the single outlier in the project |
| **sheet S-06** (issued) | **300 m³/h** — in nine separate places: the design flow, the train label *"EACH 300 m³/h (TRUE N+1)"*, both train annotations, the blast-valve schedule (BV-1/2/3 at 300), the DN100 velocity sizing, the airlock purge and the closed-mode arithmetic |

**At 250 m³/h a single train would be below the 264 m³/h FEMA 453 rate that S-06 itself computes**,
so the "true N+1, not 2 × 150" claim would fail on the sheet's own criterion. Every other figure on
S-06 — the 10.6 m/s DN100 throat velocity, the 12.8-minute purge, the 11 % leakage fraction —
reproduces only at 300.

**This package uses 300 m³/h throughout**, because that is the only value consistent with the rest of
the confirmed basis, and it says so on every sheet that carries a flow.

**RULED AT 300 m³/h by RC1, 10 September 2026** (master Part H.14 / K.1 U13), on the user's
instruction to remove every inconsistency by choosing the best option available. **Master A.3 has
been CORRECTED from "2 × 250" to "2 × 300".** Four independent lines pointed to 300 and none to
250: S-06 states 300 in nine places; every other S-06 figure reproduces only at 300; **250 fails
S-06's own 264 m³/h FEMA 453 criterion**, so it was not the cautious option but a demonstrably
inadequate one; and the project owner's own cost estimate prices 2 × 300. **This package needed
no change — it used 300 all along. CLOSED.**

### CO-5 — The floor build-up is a shared constraint, not three separate decisions ✅ ALIGNED

The floor screed appears in all three packages and had to mean the same thing in each:

| Package | What it says |
|---|---|
| **Drainage D.15** | Sets the falls (1:80 wet, 1:100 dry, spine 1:400) and therefore the build-up: 25 mm at the outlet, 78 mm at the far corner, **area-average 52 mm** |
| **Drainage DR-F4** | 52 mm × 24 kN/m³ = **1.24 kPa against a 1.0 kPa mat SIDL allowance** — an excess of 0.24 kPa (25 kN). **Referred to the structural engineer, not assumed** |
| **Finishes R3** | States the same constraint as a rule: *"a heavier finish spends an allowance that is already exceeded"* |
| **Finishes / DR-F2** | The **finished** clear height is therefore 3122–3175 mm against the **structural** 3200 |

**Aligned. One number, three packages, one referral.**

### CO-6 — Ceiling zone ✅ ALIGNED

HVAC occupies a **150 mm deep zone tight under the (−)2.900 soffit**; drainage occupies the
**25–78 mm** at the floor; finishes **rule R1 forbids any ceiling void, dry lining or boxing-in**
anywhere in the gas-tight envelope. The three are consistent and mutually reinforcing: R1 exists
*because* HVAC (HV-F2) and drainage both need every service inspectable, and because a void cannot be
decontaminated. **2950 mm remains clear below the largest duct.**

### CO-7 — Condensate ✅ ALIGNED

Dehumidifier DH-1 and any cooling coil are in Bay 5; the clean sump is in the same bay. The
condensate run is the shortest possible and discharges through a **75 mm deep-seal trap** with an air
gap. Both packages quote the same seal depth and the same **736 Pa** capacity against the same
**+300 Pa** envelope leak test, from the same calculation (drainage D.6). **DH-1's duty is not stated
anywhere in the project** (HV-D5) — that does not change the route.

### CO-8 — Hydraulic and ventilation zoning agree ✅ ALIGNED

The protective boundary creates the same three zones for both disciplines:

| Zone | Drainage | HVAC | Finishes |
|---|---|---|---|
| Bays 1–5, clean | → clean sump, complete | supply, +50 Pa | F-01/F-02, decontaminable |
| Bay 6, decon airlock | **segregated**, route to TK-01 **undefined** (DR-F5) | the **exhaust path**, cascade to +10 Pa | F-02/W-02, the dirtiest surface |
| Bays 7–8, grey | **no destination** (DR-F5) | outside the envelope; the generator serves Bay 8 only | F-03/F-04, S-02 |

Both packages reached the same zoning independently from the same confirmed boundary, and both flag
the same two unresolved crossings. **The 50 mm threshold upstands at W5 and Blast Door 1 keep zone 2
and zone 3 water out of zone 1** and do not obstruct the air cascade, which is at high level.

### CO-9 — A door that is required but not scheduled ⚠ RAISED (FN-U1)

**W5 is confirmed as "fire + gas-tight" (master A.3) but no door is scheduled in it anywhere in the
project** — yet the decon airlock must have a clean-side exit, drainage needs a 50 mm upstand at that
threshold, HVAC needs the transfer grille TG-01 through it, and finishes need to know what the leaf
and frame are. **Three packages depend on a door nobody has drawn.** Scheduled as D-05, a requirement
with **no size and no position**. **Engineer to confirm.**

### CO-10 — C16, the roof/platform junction ✅ RULED AT 250 AND CLOSED

| Package | Dependency |
|---|---|
| **Drainage** | The 2.25 m² platform roof belongs to the stairwell roof at 250 or the headhouse roof at 500. **The total catchment, 177.23 m², is identical either way** — no flow, pipe or pit changes. Only the boundary line on D-102 moves. The platform gully GY-10 sits under the junction, so a 250/500 step changes where water is delivered |
| **HVAC** | **None.** No duct, plant item, terminal or penetration is at the junction; the nearest is BV-3 in W6, 1.5 m away and at a different level |
| **Finishes** | **None to the finish itself.** What depends on the ruling is whether a **drip** is needed at the step in the soffit above G-03 |

**Action taken:** drawn at **250** to match the model and the structural register, and flagged on
D-102, D-103, D-301 and A-611.

**RULED AT 250 AND CLOSED by RC1, 10 September 2026** (master Part H.14). A.4.7's *"over the
platform it becomes the 500 headhouse roof"* was one clause against Part B, A.7.6, F.2 **and the
geometry itself** — the headhouse occupies Y 200–6000 and the platform is at Y 6000–7500, so they
do not touch. **The A.4.7 clause has been corrected to 250.** All three packages drew the right
thing; nothing in any of them changes, and the platform gully GY-10 has no step to sit under.

---

## 3 Frozen and untouched

| Item | Status |
|---|---|
| **Main staircase** — 24R @ 170.8333 / 280, 3 flights × 8, rise 4100, 1200 wide, 200 well, 200 waist, headroom 2533, landings L1/L2 and the arrival landing | **UNCHANGED.** No drainage element, duct, diffuser or support is placed in the flights, the well or the landings. Finishes annotate it and specify the nosing **cast in** with **no tread build-up**, precisely so the going stays frozen |
| Every dimension in master Parts A, B, F and L | **UNCHANGED** |
| The ten Rev F architectural DXF | **UNCHANGED** |
| Sheet S-06 | **UNCHANGED.** Three conflicts found in it (DR-C1, DR-C2, HV-C1) are **recorded, not corrected** |
| The three STAAD models | **UNTOUCHED.** No analysis was run — STAAD.Pro is not available in this environment |
| The Structural CAD package (SC1) | **UNCHANGED.** Its `sc_dxflib.py` is *imported* by the new sheet library so the sheet standard matches; not one of its files is edited |
| `Revit/scripts/01`–`06` | **UNCHANGED.** The three new scripts extend that model; none creates a project, level, grid or room |

---

## 4 What the three packages ask of other disciplines

| Ref | Request | To |
|---|---|---|
| **BW-01** | Accept or refuse a 300 wide recess in the top of the mat, 150 → 216 deep, leaving 384 of 600 locally on the line of the peak transverse sagging moment, for the one buried drain. **A fallback with no buried drain at all is drawn.** | Structural |
| **DR-F4** | Accept +0.24 kPa (25 kN) on the mat SIDL for a drained floor screed, or reduce the falls | Structural |
| **CO-1** | Fix the level of the service entry plate — the rising main must cross it at high level | Protective / structural |
| **DR-D2** | Rule on the peacetime foul route from the Bay 2 lavatory. Case B needs a **second envelope penetration** | Protective |
| **DR-D4 / DR-F5** | Rule on the decon effluent route from Bay 6 to TK-01 in Bay 8 — **it crosses the protective boundary twice** — and on a drainage destination for zone 3 | Protective |
| **HV-F2** | Rule on whether the NBC trains should move to Bay 1, removing the 11.2 m unfiltered raw-air run from the clean zone | Protective |
| **HV-D1** | Rule on whether a peacetime filter bypass is intended — a bypass is a deliberate leak path | Protective |
| **CO-3** | Confirm whether the S-06 Bay 5 plant footprints are indicative or dimensional | Architectural / mechanical |
| **CO-4 / HV-C1** | **Rule on 250 vs 300 m³/h.** One of the two numbers must change | User / design authority |
| **CO-9 / FN-U1** | Schedule the door in W5 | Architectural |
| **DR-C1, DR-C2** | Rule on the superseded catchment and the 2.3 % soak-pit shortfall on S-06 | User / design authority |

---

## 5 DXF and calculation coordination

| Check | Result |
|---|---|
| Every DXF in the three packages validates | **24 files, 0 errors, 1 warning** (a deliberate coincident line on a handout diagram) |
| Every sheet carries the scope exclusion | **PASS** — "SENTRY POST EXCLUDED FROM THIS PACKAGE" on all 24 |
| Every A1 sheet carries an evidence-class key | **PASS** |
| Figures on sheets match the calculations | **PASS by construction** — both are generated from the same module |
| Schedules match drawing tags | **PASS by construction** — one data file per package |
| Sheet standard matches the issued R-series | **PASS** — the new library subclasses `Structural CAD/Scripts/sc_dxflib.py`; same A1 size, border, title-block position, text heights and dimension styles |

---

## 6 Conclusion

**The three packages are internally consistent, consistent with each other, and consistent with the
architecture and structure as recorded.** Every conflict found is between the *existing* project
documents, or between what a package needs and what another discipline must grant — **none is a
conflict this work created**, and none has been resolved by assumption.

**Ten coordination items are recorded. Four are aligned and closed. One was resolved inside the
drainage package (CO-1). Five are referred**, of which **CO-4 / HV-C1 (250 vs 300 m³/h) is the most
consequential**, because it is a disagreement between the master and an issued sheet about a number
that the whole ventilation design rests on.

**Developed for project coordination. Design basis established. Pending engineering verification.**
