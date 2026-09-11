# SITE LAYOUT AND EXTERNAL WORKS
### Where the septic tank and the soak pits go, and why

**Package** `Site Selection and Geotechnical/` · **revision SG2** · **11.09.2026** · GEOMETRY REV F + M1
**Status — FOR REVIEW - NOT FOR CONSTRUCTION.**

**Evidence class:** `[C]` confirmed · `[R]` reconstructed · `[D]` derived here · `[A]` assumed by this package · `[U]` unresolved · `[N]` not available — DATA REQUIRED

---

## 1. What changed, and why that unblocks this

Master `H.9` recorded the positions of the soakaways, the septic tank and the external chambers as **not determinable** — *“no site plan, boundary or contour exists”* — and with them **five pipe lengths** and the **IS 2470 (Pt 2) offsets**. Drainage calculation `D.11` ends on the same sentence. That has been the position since DR1 on 5 September.

The project owner has now supplied the two things that were missing:

| | | |
|---|---|---|
| **Coordinate** | **18.6089876 N, 73.8587287 E** | `[C]` owner |
| **Availability** | *“the area around 50 m is all available”* | `[C]` owner |

With those, plus SG1's contours and geotechnical profile and the project's own confirmed geometry, **the positions can be determined**. This section determines them.

> ### The pin convention, stated so it can be corrected
> One point was given for *“the project site”*. The only self-consistent reading that lets everything be dimensioned is that it is the **centre of the underground box**, project `(11000, 3100)`. That is adopted as a **convention `[A]`**, not claimed as a finding. **If it was meant as a corner or the entrance, the whole layout translates rigidly and not one offset, length or clearance below changes.**

## 2. Site orientation — fixed by this revision

### Project **+X = EAST**, project **+Y = NORTH** `[A]`

The project has worked in a local frame since Rev F (master `A.4.1`) and has **never been tied to north**. Five reasons, all pointing the same way:

| # | Reason |
|---|---|
| 1 | **Access.** The covered entry stairwell's grade door is at its **west** end, X 9250 (`A.4.7`), so the approach comes from the west — and the CTW blocks, the roads and the campus are west of the plot (deck slides 13, 14, 17). **The entry faces the installation it serves.** |
| 2 | **Fall.** SG1 read the ground as falling **east / north-east**, 580 → 575. With +X east the drainage field is **downgradient**, so nothing recharges the ground upslope of a flotation-critical tanked box. |
| 3 | **Intake and exhaust at opposite ends.** SH-1, the fresh-air intake, is west of the box; SH-2, the generator air shaft, is at X 22598–23198, east. **22.6 m apart at minimum.** |
| 4 | **Noise and signature.** Bay 8 — the generator, ESC 2, SH-2, BV-4/BV-5 — is at the east end, away from the campus. |
| 5 | The **sentry post** covers the approach from the north. |

> **And the limit on reason 3, stated plainly.** **No wind direction data exists anywhere in this project.** The deck gives monthly mean *speed* and no direction; there is no wind rose. So the orientation is **not** justified on prevailing wind. What it does instead is put the intake and the exhaust at **opposite ends of a 22 m box**, which is the robust choice whatever the wind does. A wind rose matters for more than this — it is also the **plume direction for the CBRN case** — and it is opened as **`SG2-V4`**.

## 3. The external works reserve

**X 33000 → 51000, Y 6500 → 17500** — 18.0 m × 11.0 m = 198 m², **10.0 m clear of the main excavation's east face**, and entirely inside the 50 m envelope (worst corner 42.5 m).

**Everything in one reserve, on the downgradient side.** Four reasons:

1. **Nothing recharges the ground upslope or alongside the box.** The box is flotation-critical — FoS **0.33** at the mat-only stage — and its side backfill is selected granular fill at 95 % MDD, which is **more permeable than the basalt around it**. Effluent released near it would run preferentially *into* the backfill and down the outside of the tanking. That is the single worst thing this layout could do, and putting the whole field 11–22 m downgradient is what prevents it.
2. **One percolation-test location, one keep-clear zone, one reserved fallback.**
3. **One trench.** `PD-06`, `PD-11` and `PD-13` share a common services trench at Y 9800. Where rockhead is 0.9–1.5 m the cost is the trench, and the trench is cut once — which is what makes a 32 m gravity run sensible.
4. **Concealment.** Four RC cover slabs and a 2 m septic vent are new at-grade signatures. Grouped 11–22 m away and downgradient, **they mark the drainage field, not the shelter** — which is better for `CAM2` than scattering them around the structure.

> **The layout is anchored to confirmed geometry only.** Every position is dimensioned from the underground box, whose geometry is `[C]` throughout. **Nothing is dimensioned from the sentry post**, whose site position is `[ASSUMED]` (master `U4`) — so the layout survives U4 being resolved differently. And every offset is **relative**: if the perimeter fence turns out to be closer than the reserve's east edge, **the whole reserve translates and not one offset changes**.

## 4. The positions

| Tag | Type | Centre (X, Y) | Size | Serves |
|---|---|---|---|---|
| **SK-02** | STORM SOAKAWAY | (35000, 8500) | 2200 dia × 3500 eff | Clean sump rising main PD-06 + entry threshold channel PD-11 |
| **SK-03** | STAIRWELL SOAKAWAY | (41400, 8500) | 2200 dia × 3500 eff | Stairwell sump SU-02 rising main PD-13.  SIZE NOT RECORDED ANYWHERE in the project - the 2.2 dia footprint is RESERVED, not designed |
| **SK-04** | HEADHOUSE SOAKAWAY | (47800, 8500) | 2200 dia × 3500 eff | Headhouse gully GY-11 via PD-14.  SIZE NOT RECORDED ANYWHERE - footprint RESERVED.  PD-14's route is UNDETERMINED - SG2-F5 |
| **SK-01** | FOUL SOAK PIT | (44000, 16000) | 2200 dia × 3500 eff | Septic tank ST-01 effluent via PD-16, 450 L/day |
| **ST-01** | SEPTIC TANK | (36750, 16000) | 1500 × 750 | 1 |
| **IC-02** | INSPECTION CHAMBER | (40200, 16000) | 600 × 450 | 600 x 450 on PD-16, for septic tank de-sludging access |
| **IC-01** | INSPECTION CHAMBER | (7500, 9800) | 600 × 450 | 600 x 450 on PD-11 at the change of direction |

Pit levels, **relative to local finished grade at each pit** — there is no benchmark and the site fall is itself disputed (`SG-V4`), and this is how a soak pit is built anyway: underside of cover slab **600 mm** below grade, invert **4100 mm** below grade, effective depth **3500 mm** `[C]` unchanged from RC1.

**`SK-03` and `SK-04` are reserved, not designed.** Neither is sized anywhere in the project (`[C]`/`[N]` in the drainage package). Their 2.2 m footprints are reserved to the same construction detail as SK-01/SK-02, so whatever size is finally adopted fits.

## 5. The offsets, demonstrated

Drainage `D.11` records three offsets from S-06 and then says: *“**THOSE OFFSETS CANNOT BE DEMONSTRATED** — no site plan, no well position and no boundary exist in the project.”*

| Offset | Required | Achieved | Status |
|---|---|---|---|
| Foul soak pit → septic tank | ≥ 5 m `[C]` | **5.40 m** | **DEMONSTRATED** |
| Soak pit → any building | ≥ 2 m `[C]` | **10.97 m** (nearest approach anywhere) | **DEMONSTRATED**, 5.5× over |
| Foul soak pit → any well | ≥ 15 m `[C]` | — | **CANNOT BE DEMONSTRATED — no well position exists anywhere in this project.** `SG2-V1` |

Plus four rules this package adopts, each with its reason, and every check passing — see `SITING_CLEARANCE_SCHEDULE` and calculation §S.4. The tightest are **foul group to any excavation face 15.49 m** (adopted ≥ 15) and **pit wall to pit wall 4.20 m** (adopted ≥ 4).

## 6. The five pipe lengths

| Tag | From | To | DN | Gradient | **Length** | Fall |
|---|---|---|---|---|---|---|
| **PD-16** | ST-01 outlet | SK-01 inlet | DN100 | 1:100 | **5.40 m** | 54 mm |
| **PD-06** | SERVICE ENTRY PLATE | SK-02 | DN50 | PUMPED | **27.00 m** | pumped |
| **PD-11** | CP-10 entry catchpit | SK-02 | DN100 | 1:100 | **32.35 m** | 324 mm |
| **PD-13** | SU-02 stairwell sump | SK-03 | DN50 | PUMPED | **29.60 m** | pumped |
| **PD-14** | GY-11 headhouse gully | SK-04 | DN100 | 1:80 | **`[U]`** | — |

**Four of the five are determined. The fifth cannot be routed at all** — see `SG2-F5` below. No run crosses the engineered cover; the side backfill corridor at Y 6200–7200 is not the cover and is a normal place for a service.

## 7. `SG2-F1` — the soak pit will not work as a deep pit, and the site data now says so

RC1 fixed the **arithmetic** of SK-01 (C19: widened 2.0 → 2.200 dia, 24.19 m² against 22.50 required). It also wrote the sentence this section starts from:

> *“deepening drives the pit further below the design GWT at `(−)2.000`, **where it cannot soak at all**.”*

So the project has known since RC1 that the pit is below the water table. **Nobody has ever quantified by how much.** SG1 supplied the missing half — the measured ground profile — so it can be.

### Check 1 — how much of it is above the design water table?

The project holds **two readings** of the design GWT, and 28 m east on falling ground they are not the same thing: the **absolute** level `(−)2.000` (master `A.6`), and **“2 m below GL”** (deck slide 29). Both bounds are computed:

| Reading | Water below local grade | Wet depth | Area **above** | of 22.50 m² |
|---|---|---|---|---|
| Absolute `(−)2.000`, reserve ≈ 0.70 m lower | 1.30 m | 2.80 m | **4.84 m²** | **21.5%** |
| Relative, 2 m below local grade | 2.00 m | 2.10 m | **9.68 m²** | **43.0%** |

> **Between 21 % and 43 % of the required absorption area lies above the design water table.** The rest is, by the project's own design assumption, permanently submerged — and a submerged wall does not infiltrate: there is no unsaturated storage to receive the effluent and no head to drive it. **This is geometry against a stated design level. It does not depend on the percolation rate at all.**

### Check 2 — and what is the rest of it cut through?

| Location | Broken-rock band | Thickness | Side area in it | of 22.50 m² |
|---|---|---|---|---|
| G Building (TP-1 to TP-4) | 1.20 – 1.50 m | 0.30 m | **2.07 m²** | **9.2%** |
| H Building (TP-5 to TP-8) | 0.70 – 0.90 m | 0.20 m | **1.38 m²** | **6.1%** |
| Mess Bldg (TP-9 to TP-11) | 0.50 – 1.00 m | 0.50 m | **3.46 m²** | **15.4%** |

Above the broken rock: **black cotton CH at FSI 60–65 %** — it swells shut when wet — over **murrum, which the deck's own slide 30 calls *“impervious in nature”***. Below it: **sound basalt**, whose matrix permeability is effectively zero; whatever it takes, it takes through **joints**, and no joint data exists — no RQD, no packer test (`SG-V2`).

> **The only demonstrably permeable horizon is 0.2–0.5 m thick and contributes 15 % or less of the required area.**

### The conclusion

> **`SG2-F1`. SK-01's shortfall was never an arithmetic problem — RC1 fixed that. It is a DEPTH problem.** A 3.5 m deep pit at this site is mostly below the design water table and mostly in sound basalt. **The form that fits this ground is shallow and wide, not deep and narrow** — a dispersion trench worked in the 0.5–1.6 m broken-rock horizon, *above* the water table. Which is exactly **IS 2470 (Pt 2) Cl. 5**, the fallback master `K.2 A7` has named all along.

**SG2 does not change SK-01.** The percolation test governs the final size and form — master `A7`, and RC1 said so too. What SG2 does is **(i)** say the number *before* the test rather than after it, and **(ii)** reserve the ground for the fallback.

## 8. The fallback, reserved

A dispersion trench is sized on the **same basis this project uses for the pit**: side area only, base discounted because it clogs. A trench of effective depth *h* gives 2*h* m² per metre run.

| Field | Reserved | Trenches at 2.5 m centres | Side area | Serves its stream down to |
|---|---|---|---|---|
| **DF-1** FOUL DISPERSION FIELD | 14.5 × 6.5 m | 3 × 14.5 m = 43.5 m | 87 m² | **5.17 L/m²/day = 26% of the assumed 20** |
| **DF-2** CLEAN DISPERSION FIELD | 14.5 × 3.5 m | 2 × 14.5 m = 29.0 m | 58 m² | **6.90 L/m²/day = 34% of the assumed 20** |

> **The reserve carries both streams at roughly a quarter to a third of the assumed absorption rate.** That is the point of reserving it: the percolation test can come back badly and the answer is still a **redesign inside the same footprint**, not a new hunt for ground.

If even that fails — and on sound basalt it can — the remaining answers are a **sealed holding tank emptied on a schedule** (master `A7`'s own words) or a **positive outfall**, and a positive outfall needs the final-discharge question answered, which is `D3` and is still open.

## 9. Where the percolation test has to be done

Master `K.2 A7` makes it **mandatory** (IS 2470 Pt 2 Cl. 4). Drainage `D.12` calls it *“on the critical path for three independent reasons”*. **Nobody has ever said where**, and a percolation test in the wrong place or at the wrong depth answers nothing.

| Ref | Position | Depth | What it decides |
|---|---|---|---|
| **PT-1** | (44000, 16000) | to **4.100 m** below local grade, the proposed pit invert | AT SK-01, the foul pit position |
| **PT-2** | (35000, 8500) | to **4.100 m** below local grade, the proposed pit invert | AT SK-02, the clean pit position |

> **And test the shallow horizon too.** §7 shows the deep pit is mostly submerged and mostly in sound basalt, and §8 shows the fallback is a trench at about 1.5 m. A test taken **only** at `(−)4.100` measures the formation the fallback will not use. **Take each test at both depths** — the pit invert and the trench invert — or the fallback is undesigned the day the pit is abandoned. `[A]`

The same boreholes serve `SG-V2`: `A1075` must be located **on this plot**, and the standpipe `SG-V3` asks for goes in one of them.

## 10. `SG-V3` ruled — and what the ruling leaves standing

> **Ruling, 11 September 2026: the cost of moving the groundwater monitoring is not accepted.**

**Reading.** `SG-F7` showed that WBS `A1080` runs 12-11-26 → 04-12-26, which is not the monsoon, and that moving it would move a critical-path activity and therefore the job. The ruling declines **that cost**. `A1080` stays where it is. *If the owner meant something wider, this reading is stated so it can be corrected.*

**Consequence, stated honestly.** `A1080` as programmed will measure the post-monsoon **recession**. It will therefore **not close master `K.2 A2`**. The design GWT `(−)2.000` stays `[ASSUMED]` through construction and into service.

**And why the permanent works are still bounded.** `(−)2.000` is only 2 m down, which is the conservative direction for everything the water drives. The risk left open is that the real table is **higher** — and master `B.3` has already run that bound:

| Stage | FoS @ `(−)2.000` | FoS **flooded to grade** |
|---|---|---|
| 1 mat cast only | 0.33 FAIL | 0.23 FAIL |
| 2 mat + walls, no roof | 0.78 FAIL | 0.55 FAIL |
| 3 box complete, no backfill | 1.22 MARGINAL | **0.86 FLOATS** |
| 4 backfilled + cover | 2.02 OK | **1.41 OK** |

> **The completed structure passes even with the water at ground level** — FoS 1.41 against a requirement of 1.2. The ruling does not put the permanent works at risk.

**What it does expose is the construction stage**, and that is now the operative control. Master `B.3`'s mandatory mitigation becomes non-negotiable rather than advisory: continuous dewatering until backfill *and cover* are complete; the six pressure-relief plugs grouted only after backfill; sub-structure before the monsoon or a bunded, positively drained excavation with standby pumping; and symmetrical backfill.

> **`SG2-V5` — and the programme does not do the first of those.** `A2070`, *“Dewatering — continuous through the substructure works”*, runs 01-01-27 → **11-05-27**. Side backfill `A7010` runs 20-07-27 → 30-07-27 and the burster slab is not cast until 21-08-27. **So dewatering stops on 11 May and the box stands un-backfilled through the whole 2027 monsoon — stage 3, FoS 1.22 at the design GWT and 0.86 flooded.** No date is changed here; the owner's schedule R0 governs (master `H.13`).

**One option the ruling does not preclude, because it costs no float.** A standpipe piezometer left in the `A1075` borehole and read weekly by staff already on site is a **level-of-effort** observation, exactly like `A2070` itself. It cannot verify the design in time — the mat is cast in February — but through the 2027 monsoon it measures the water the flotation case is actually exposed to, **while the box is standing at FoS 1.22**. Offered, not adopted. `[A]`

## 11. `SG-V5` amended — rainfall, and which figure is the wrong one

**What actually happened, recorded so it can be checked.** Ten hosts were probed from this session and **all ten were refused by the environment's egress policy (HTTP 403)**: `imd.gov.in`, `imdpune.gov.in`, `mausam.imd.gov.in`, `data.gov.in`, `tropmet.res.in`, `en.wikipedia.org`, `en.climate-data.org`, `power.larc.nasa.gov`, `climexp.knmi.nl`, `ncei.noaa.gov`. **No IMD normal was retrieved and none is invented.**

One published figure with a **named station and a named period** was obtained, and it is enough to settle which of the project's two figures is wrong:

> **June to October mean at Pune, Shivajinagar observatory, 1978-2020, 42 years: 852.5 mm.** [R] published analysis of IMD station data - NOT an IMD normal
> Source: Mongabay India commentary, 'Long term rainfall patterns and flooding in Pune city' (2021), citing IMD Shivajinagar data.

| Source | Jun–Oct | Annual | Verdict |
|---|---|---|---|
| Shivajinagar 42-year mean | **852.5 mm** | — | the yardstick |
| P1 deck slide 25 | 699.5 mm | 759.6 mm | **-18%** on Jun–Oct |
| SEMT/67/15 para 9 | — | 500–600 mm | **untenable — see below** |

> **`SG2-F2`. The soil report's rainfall figure is the one that is wrong, not the deck's.** SEMT para 9 gives 500–600 mm for the **annual** rainfall of *“the region”*. The **June-to-October mean alone** at the nearest long-record observatory is **852.5 mm** — **1.4 to 1.7 times the report's whole year**. A figure that small is not a Pune figure.

SG1 raised this as a straight conflict between two documents and could not say which side was wrong. **It can now — and the correction runs the other way from the first guess:** the deck is the right *order*, and the soil report is not.

The deck is not vindicated, though. Its Jun–Oct total of 699.5 mm is **18% below** the 42-year Shivajinagar mean, and its October figure — 139.8 mm, 1.04× September and above August — still does not fit a Deccan monsoon. **Both the annual total and the October value still need the real normal. `SG-V5` stays open, on a narrower question.**

**What to ask for, exactly:**

- IMD Pune, 'Climatological Tables of Observatories in India 1991-2020' - imdpune.gov.in/library
- IMD Climate Data Services Portal - cdsp.imdpune.gov.in, and the Station Climatological Normals service at dsp.imdpune.gov.in
- IMD National Data Centre, Shivajinagar, Pune - ndc@imd.gov.in
- ASK FOR: the station normal for the observatory nearest CME Dapodi, monthly and annual, with the station index number and the period of record printed on it.  AND SEPARATELY, an IDF relation - the 50 mm/h in this project has no return period, duration or source (DR-D1), and a monthly total can never supply one.

### And the part that decides how much this matters

> **Not one pipe, pit, pump or structure in this project is sized by rainfall.**

- The roofs and the 2 000 engineered cover **shed at grade** to the berm toe. Drainage `D.7`: *“there is no roof outlet, no downpipe and no rainwater pipe on the buried roof”*. The 2.461 L/s at 50 mm/h **never enters a pipe**.
- The only rainwater that does enter a pipe is `CH-10 → CP-10 → PD-11`, and `DR-C1` ruled that catchment is the **door-open driving-rain** case, about 12× smaller than the superseded 0.10 L/s — order **0.008 L/s** against a DN100 at 1:100 carrying 6.72 L/s.
- The stairwell sump `SU-02` is sized on a **1 000 L event volume** `[C]`, not on an intensity.

So the rainfall conflict **governs what the design report may claim, and — through the monsoon window — when things can be built. That is the whole of its reach**, and it is worth saying plainly so nobody re-sizes a pipe on the back of a corrected rainfall table. The intensity question `DR-D1` is separate and is **not** closed: a monthly total can never supply a short-duration intensity.

## 12. What the siting work surfaced in other packages

Four things. Each is recorded and referred; **none is acted on.**

| Ref | Finding |
|---|---|
| **`SG2-F3`** | **ST-01 is sized for a building that is not connected to it.** The tank is sized for 10 users, *“sentry-post shift crews + shelter maintenance”* `[C]` S-06. The drainage package excludes the sentry post from its scope, and **there is no pipe from the sentry post to ST-01 anywhere in the project** — the schedule has `PD-15` (Bay 2, Case B only, not adopted) and `PD-16` (ST-01 → SK-01) and nothing upstream of the tank at all. SG2 positions ST-01 and leaves the connection to the drainage engineer; the layout does not prejudge it — ST-01 is 22.5 m from the assumed sentry position with clear ground between. |
| **`SG2-F4`** | **SH-1 has no plan position.** The HVAC equipment schedule gives SH-2 an X range (22598–23198) and gives SH-1 only *“West of the box”*. **The fresh-air intake of a CBRN shelter is not a minor fitting.** Until it has a coordinate, no intake separation can be checked against anything — the septic vent included. What protects it here is the layout, not a calculation: the reserve is **east** and SH-1 is **west**, so the separation is at least 33 m however SH-1 is finally placed. `SG2-V3` |
| **`SG2-F5`** | **`PD-14` cannot be routed.** `GY-11` sits at (14700, 1960) with its invert at `(−)2.150`, and the headhouse floor **is** the top of the 900 pressure slab at `(−)2.000` (master `A.4.6`). The gully body and its outlet are therefore **150 mm inside the pressure slab**; outside the headhouse walls that level is beneath the waterproof membrane and within the engineered cover, which no pipe may enter. **SK-04's footprint is reserved; its pipe is not routed.** Referred to drainage and structures together. |
| **`SG2-V5`** | **The programme stops dewatering before backfill** — see §10. |

## 13. Master gap `D3` — what is now closed and what is not

`D3` has been cited as a blocker across six packages. It was never one thing. Splitting it:

| # | What D3 was blocking | Status after SG2 |
|---|---|---|
| 1 | Positions of the soakaways and the septic tank | **CLOSED** |
| 2 | The five “not determinable” pipe lengths | **FOUR CLOSED**, `PD-14` `[U]` — `SG2-F5` |
| 3 | External chamber positions `IC-01`, `IC-02` | **CLOSED** |
| 4 | IS 2470 offset to the septic tank, ≥ 5 m | **DEMONSTRATED — 5.40 m** |
| 5 | IS 2470 offset to any building, ≥ 2 m | **DEMONSTRATED — 5.5× over** |
| 6 | IS 2470 offset to any well, ≥ 15 m | **STILL OPEN** — no well exists. `SG2-V1` |
| 7 | A concealment *layout* (`CAM2` / `CAM-V2`) | **PARTLY** |
| 8 | Berm, access and hardstanding layout | **STILL OPEN** — needs levels |
| 9 | Cut and fill for a level formation | **STILL OPEN** — needs levels, `SG-V4` |
| 10 | The final discharge question — is any outfall available? | **STILL OPEN** — D3 proper |
| 11 | Sentry post site position (`U4`) | **STILL OPEN** — and nothing here depends on it |

> **`D3` is PARTIALLY closed, not closed. The layout now exists. The survey does not.** What is still missing — a boundary, a benchmark and spot levels, the well, the fence distance, existing services on the plot, a wind rose — is every one of it a **survey** output, and none of it moves anything SG2 has fixed: the layout is dimensioned from confirmed structure geometry and every clearance is relative.

**On concealment.** `CAM2` could not draw a layout and still cannot draw a full one. But SG2 fixes where the new **at-grade signatures** go — four RC cover slabs and a 2 m septic vent — and puts them 11–22 m from the structure, in one group, downgradient and away from the approach. **The covers mark the drainage field, not the shelter.** `CAM-V2` is unaffected: it is a client ruling on whether the above-ground signature is acceptable at all.

## 14. What this revision changed, and what it did not

| | |
|---|---|
| Design values in Parts A, B, D, F, L | **untouched** |
| **SK-01's size** | **untouched** — RC1's 2.200 dia × 3.500 stands. The percolation test governs |
| BOQ quantities, rates, dates, floats | **untouched** — WM2 governs |
| `.std` models | **untouched — STAAD.Pro was not run** |
| Any file in any other package | **untouched** |
| **The main staircase** | **untouched — frozen** |
| Any `[ASSUMED]` tag | **not one converted, downgraded or deleted** |

**Added:** this section, four schedules, a calculation printout (§S.1–S.12), and two A1 drawings — `SG-102`, the project's **first true site layout plan**, and `SG-202`, the external works siting and the soak pit finding.

---

*Site Selection and Geotechnical package, revision **SG2**, 11.09.2026. Every value is tagged. The positions are fixed; the survey that would confirm them is not. Nothing that was assumed has been made confirmed.*
