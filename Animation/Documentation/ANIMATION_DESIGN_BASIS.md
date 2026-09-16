# AN1 — CONTINUOUS 3D ENGINEERING ANIMATION: DESIGN BASIS

**Underground CBRN-hardened blast-resistant protective structure + sentry post, Pune**
B.E. Civil Engineering final-semester capstone · College of Military Engineering, Pune

| | |
|---|---|
| Revision | **AN1** |
| Date | 16 September 2026 |
| Deliverable | `Animation/Output/AN1_UNDERGROUND_CBRN_OPS_ROOM.html` |
| Running time | **6 min 22 s**, one continuous camera journey, 21 beats |
| Technique | Real-time WebGL 2, rendered live in the browser |
| Dependencies | **None.** One self-contained file, no CDN, no fonts, no network |
| Design values moved | **NONE.** No dimension, load, rate, quantity or tag changed |
| Analysis run | **NONE.** STAAD.Pro is not available in this environment |

---

## 1 What this is, and what it is not

**It is** a presentation instrument: a single continuous camera journey through the project
as an integrated protected facility, built procedurally from the project's own dimensions.

**It is not** an analysis, a result, a verification or a drawing. Nothing in it may be quoted
back into the engineering record. Where the animation needed a value the project does not
hold, it did **not** invent one — it either simplified the visualisation or declared the value
`[V]` and listed it in section 4.

### Why a real-time page rather than a rendered video file

The build environment has no Blender, no renderer and no GPU, so a pre-rendered film was not
available. A real-time page is in any case the better instrument for this use:

- it runs **offline from a USB stick** — the property that actually matters in a hall;
- it is **resolution-independent** and fills any projector without re-rendering;
- the presenter can **pause, scrub and jump to a chapter** while answering a question;
- it can be **screen-recorded** to a video file in one pass if a file is wanted (section 9).

---

## 2 Sources and the order of authority

Applied exactly as the brief set it out, and reconciled with `CLAUDE.md`, which makes the
master the single source of truth for this repository.

| Rank | Source | Used for |
|---|---|---|
| 1 | **`master/MASTER_PROJECT_STATE.md`** Parts A, B, F, L | Every dimension, level, load, material and system value |
| 2 | `CONSOLIDATED_PROJECT_REPORT.md` and `Project Report/Documentation/MASTER_PROJECT_REPORT.md` | HVAC/CBRN, drainage, electrical, EMP, sanitation, operating modes |
| 3 | Package documentation (`Drainage/`, `EMP Protection/`, `Electrical/`, `Site Selection and Geotechnical/`) | Detail the master summarises |
| 4 | **`Project1.pdf`** — the owner's Revit set, ARCH001–ARCH005 | Visual geometry, massing, the 3D and side-profile views, title-block language |
| 5 | **`Abstract_Project_Flier.pdf`** | Visual identity, colour language, bay legend, the tagline, the standing caveat |

The Revit set was parsed, not eyeballed: its five sheets are
`ARCH001` underground/headhouse/ground level plans · `ARCH002` sentry post plans and front
elevation · `ARCH003` sectional views · `ARCH004` isometric and front elevation ·
`ARCH005` side profile 3D of both structures. Its printed dimensions (22000, 6200, 2900,
3500, 2400, 1560, 1800, ø1400) and its level tags (FDN −6100, UG ROOF −2900, HEAD HOUSE
FLOOR −2000, GL 0, HEAD HOUSE ROOF 900) **agree with master Part A** everywhere except the two
items in finding `AN1-F1`.

---

## 3 Value register — every figure the animation puts on screen

Evidence classes are the master's own. **Nothing below was rounded, recomputed or restated.**

### 3.1 Geometry — master A.4

| On screen | Value | Class | Source |
|---|---|---|---|
| External | 22.0 × 6.2 m | `[C]` | A.4.2 |
| Roof (pressure) slab | 900 | `[C]` | A.4.2 / B.4 |
| Mat | 600 | `[C]` | A.4.2 / B.3 |
| Perimeter walls | 600 | `[C]` | A.4.2 / B.1 |
| W6 / W7 | 400 | `[C]` | A.3 — **Modification M1** |
| Internal clear height | 3 200 | `[C]` | A.4.2 |
| Engineered cover | 2 000 layered | `[C]` | A.4.2 / A.7.3 |
| Levels: grade 0.000 · slab top −2.000 · soffit −2.900 · floor −6.100 · mat u/s −6.700 · formation −6.800 | | `[C]` | A.4.3 |
| Escape shafts ESC 1 / ESC 2, ø1400, 250 collar, OD 1900 | | `[C]` | A.4.5 |
| Headhouse 4800 × 5800, walls 400, roof 500, top +0.900 | | `[C]` | A.4.6 |
| Entry stairwell 6800 × 2000, walls 250, roof 250 **including over the platform** | | `[C]` | A.4.7 — RC1 ruling C16 |
| Main stair 24R @ 170.8333, tread 280, 3 × 8, rise 4100 | | `[C]` | A.4.4 — **FROZEN, untouched** |
| Blast doors 1 and 2, 1200 × 2100, ≥ 7 bar | | `[C]` | A.2 / A.4.9 |
| Sentry post 4000 × 5000, C1 350², B1/B2 250 × 450, S1 150, F1 1500 × 1500 × 600 at (−)2.000 | | `[C]` | A.4.8 |

### 3.2 Loading — master A.7

| On screen | Value | Class |
|---|---|---|
| DBT, nuclear air-blast, p<sub>so</sub> | **344.7 kPa (50 psi)** | `[C]` |
| Ductility μ 5 → DLF 5/4.5 | **1.111** | `[C]` |
| **DESIGN BLAST PRESSURE** | **383 kPa**, roof **and** walls (K<sub>a</sub> = 1.0) | `[C]` |
| Engineered cover | **40.65 kPa** = 39.15 layers + 1.50 declared allowance | `[C]` — RC1 ruling C17 |
| Earth + water at floor | **83.2 kPa** (gradient 15.41 kPa/m, 9.81 of it water) | `[C]` |
| Hydrostatic uplift on mat | **46.11 kPa** | `[C]` |
| Fallout protection factor | **≈ 2 200** against a requirement of ~1 000 | `[C]` |

> The brief asked whether 383 kPa is the final value. **It is**, and the master states the
> arithmetic: `344.7 × 1.111 = 383`. It is not a draft figure.

### 3.3 The six cover layers — master A.7.3, drawn at true thickness

topsoil/turf 300 · granular filter 150 · **RC burster slab M30 200** · crushed basalt rubble
500 · compacted fill @ 95 % MDD 750 · protection screed 100 = **2 000**. All `[C]`.

### 3.4 Systems

| On screen | Value | Class | Source |
|---|---|---|---|
| Occupancy | **9 persons, 96 h** | `[C]` | A.1 |
| Gas-tight envelope | **Bays 1–6, 67.80 m², 216.96 m³** | `[C]` | report 9.1 |
| Filter trains | **2 × 300 m³/h**, HEPA H14 + activated carbon, true N+1 | `[C]` | RC1 ruling C21 |
| Envelope overpressure | **+50 to +100 Pa** | `[C]` | report 16.7.3 |
| Closed mode limit | **48 h — set by the soda lime, not by power** | `[C]` | RC2 / HV-F1 |
| Blast valves | five; all shut at the shock, BV-4/BV-5 reopen for GEN-1 | `[C]` | RC2 ruling 2 |
| Generator | **GEN-1, 15 kVA, Bay 8 — 7.360 kVA connected, 49 %** | `[C]` | report 17 |
| Essential load / battery | **1.283 kW / 149 Ah, 48 V** | `[C]` | EL1, confirmed by RC2 |
| Sanitation | **SN-03 sealed-cassette chemical toilet, NO DISCHARGE** | `[C]` | `SANITARY_FIXTURE_SCHEDULE.md`, from S-06 |
| EMP three-zone model | Zone 0 / Zone 1 / Zone 2 | `[D]` EM1, **adopted by owner ruling RC2** | report 19 |
| EMP Zone 2 | **80 dB, welded steel enclosure, Bay 3, designed standing alone** | `[C]` | EM1 design rule |
| Zone 2 enclosure size | 2400 × 1600 × 2200 external | `[A]` | EM1 — see `AN1-V4` |

### 3.5 Ground — master A.6 + SG1

Deccan basalt with red-bole / vesicular seams at flow contacts `[A]`; surface **black cotton,
CH, FSI 60–65 %** `[C]` (SG1); rockhead (−)1.500 to (−)2.000 `[A]`, against SG1's measured
0.9–1.5 m. **The animation draws the rockhead band and labels the founding stratum
"rockhead ASSUMED, not proved"** — it does not present the geology as surveyed.

---

## 4 The animation's own values — class `[V]`

These exist so the camera has somewhere to stand and the soldier somewhere to walk. **They
carry no engineering weight and must never be quoted back into the record.**

| Item | Value | Why |
|---|---|---|
| Walked route between the two real endpoints | a 9-point polyline | The project draws no site circulation anywhere. Both **endpoints are real**: D1 on the sentry post's east face (A.4.8) and the 1000 × 2100 entry door at grade at X 9250 (A.4.7) |
| **Route length** | **36.687 m** | Measured from that polyline |
| **Pace** | **0.655 m / footfall** | **DERIVED: 36.687 / 56.** Not chosen — see `AN1-F3` |
| Cadence | 0.75 s / footfall | An ordinary measured sentry's pace |
| Blast azimuth | **115° bearing to the burst** | See `AN1-F4`. Verified: front coordinate of the sentry post **−29.50** < the box **−8.66**, so the front crosses the post first |
| Blast range | 2 400 m | Far enough to read as a distant event. No yield is stated or implied |
| Blast front travel | **slowed for legibility, and the animation says so on screen** | See `AN1-V2` |
| Interior lighting, finishes, figure posture and activity | generic | Not specified anywhere in the project |
| Soundscape | synthesised | No acoustic data exists in the project |

---

## 5 Shot list — 21 beats, one camera, no cut

| # | Beat | In | Out | What it establishes |
|---|---|---|---|---|
| 1 | SITE | 0:00 | 0:20 | Plot, berm, headhouse, entry stairwell, sentry post, stand-off |
| 2 | SENTRY POST | 0:20 | 0:36 | The exposed outer element; not blast designed; footings on rock |
| 3 | **56 STEPS** | 0:36 | 1:25 | 56 individual footfalls, camera continuous, pace printed |
| 4 | BLAST | 1:25 | 1:40 | Flash, brief fireball, DBT stated |
| 5 | BLAST WAVE | 1:40 | 1:57 | Front crosses the plot: source → wave → project |
| 6 | STAND-OFF | 1:57 | 2:09 | Expendability by design — no failure analysis |
| 7 | CUTAWAY | 2:09 | 2:27 | Ground ghosts, then opens into one engineering section |
| 8 | ENGINEERED COVER | 2:27 | 2:42 | The six layers, each named and dimensioned |
| 9 | **LOAD PATH** | 2:42 | 3:07 | Blast → slab → wall → mat → founding stratum, plus the lateral case |
| 10 | PROTECTED VOLUME | 3:07 | 3:19 | Bays 1–6, the gas-tight envelope, the blast doors |
| 11 | INTERIOR | 3:19 | 3:36 | Camera passes through the boundary into the ops room |
| 12 | OCCUPANTS | 3:36 | 3:51 | Nine at work; the shock felt as a tremor and a light dip |
| 13 | **CBRN AIRFLOW** | 3:51 | 4:17 | Intake → blast valve → filtration → envelope at +50 Pa |
| 14 | CLOSED MODE | 4:17 | 4:30 | Sealed; 48 h; the limit named correctly |
| 15 | ESSENTIAL POWER | 4:30 | 4:47 | GEN-1, essential board, the loads it actually carries |
| 16 | SANITATION | 4:47 | 4:58 | SN-03 sealed cassette; nothing is discharged |
| 17 | EMP | 4:58 | 5:14 | A field, not an explosion; Zone 0 then Zone 1 |
| 18 | **EMP ZONE 2** | 5:14 | 5:30 | 80 dB, standing alone, bay 3 |
| 19 | INTEGRATION | 5:30 | 5:42 | Continuity of operations, everything running |
| 20 | RETURN | 5:42 | 6:00 | Reverse the journey out through the cover to grade |
| 21 | SITE, AFTER | 6:00 | 6:22 | Hero three-quarter matching ARCH005, dust settled, fade |

**Continuity.** Camera position and target come from **one** track, resampled at 30 Hz from
the keyframes and smoothed 26 times, which gives continuous velocity with no overshoot and no
stop-start at keys. The only override is the soldier-follow during beat 3, cross-faded in over
4.5 s and out over 5.5 s, so the track never jumps. **There is no cut anywhere in the file.**

### On the running time

6 min 22 s is 22 s over the brief's preferred 4–6 min. **The 56-step requirement is the whole
of the overrun**: beat 3 alone is 49 s (56 × 0.75 s plus lead-in and settle). Every other beat
was cut to what it needs. Shortening the walk would mean either skipping footfalls, which the
brief forbids, or a cadence fast enough to read as a march rather than a sentry's walk.

---

## 6 What is deliberately NOT shown

Brief sections 11, 24, 30 and 31, applied as hard rules in the code:

- **No failure analysis of the sentry post.** It is dimmed and lost in the blast environment.
  No cracking, no rebar, no collapse mechanic, no weak point, and the word "failure" appears
  nowhere. It is labelled **EXPENDABLE OUTER ELEMENT**.
- **No vulnerability information.** `EM-F1` (the stair void aperture), the two DN350 bores of
  `EM-V3`, the `RC5-F2` pressure-slab penetrations and every other open weakness in the record
  are **not drawn and not named**. This is a demonstration of the intended protection concept.
- **No fabricated analysis.** Master D.3.5 records the underground model's results as
  `[NOT AVAILABLE — DO NOT INVENT]`. There is therefore **no stress contour, no displacement,
  no utilisation, no safety factor and no failure mode** anywhere. The load path shows *where*
  the load goes and never *how much arrives*.
- **No unsupported claim.** Nothing implies zero damage, guaranteed survival, absolute
  immunity or unlimited continuity. The flier's own caveat — *IS 4991:1968 excludes nuclear
  explosions; used for its loading rules only* — stands on screen for the whole blast sequence.
- **No invented plant.** Every duct, valve, filter, tank, board and enclosure drawn is in the
  bay schedule or a package schedule.
- **No title cards, no slides, no full-screen captions.** Annotations are small, anchored in 3D,
  fade in and out, and never stop the camera.

---

## 7 Findings

| Ref | Finding |
|---|---|
| **AN1-F1** | **The Revit set and master Part A disagree on two levels.** `ARCH002`/`ARCH003` print **ENTRY ROOF TOP 3400** and **GROUND FLOOR LEVEL 440**; master A.4.3 records the entry stairwell roof at head **+2.450** and the sentry post GF FFL **+0.450**. Per `CLAUDE.md` the master governs and the animation follows it. **Neither is resolved here and no tag is converted.** New open item `AN1-V8` |
| **AN1-F2** | **"Cassette" means two different things in this project and they were nearly conflated.** Master 9.1 uses it for the **HEPA/carbon filter cassette**; the sanitation cassette is the separate, separately-confirmed **SN-03 SEALED-CASSETTE CHEMICAL TOILET** (`SANITARY_FIXTURE_SCHEDULE.md`, `[C]` from S-06). Both are drawn; only SN-03 is labelled as sanitation |
| **AN1-F3** | **No documented basis for 56 steps exists anywhere in the project.** It is the presenter's requirement. Rather than assume a pace and invent a distance, both endpoints were fixed to real features and the **pace derived**: 36.687 m / 56 = **0.655 m**, which is an ordinary walking pace. The route between the endpoints is `[V]` |
| **AN1-F4** | **The project holds no wind-direction data** — `SG2-V4`'s plume half is open precisely because a CBRN shelter with no wind data cannot state which way a release drifts. The blast azimuth is therefore `[V]`, chosen as the only family of azimuths that puts the sentry post upwind of the shelter, which is what the stand-off argument requires. Verified numerically in the build |
| **AN1-F5** | **No STAAD result exists for the underground model** (master D.3.5 `[N]`). The load path is conceptual only, by construction |
| **AN1-F6** | **`DR-A2-V1` is respected rather than papered over.** The mat's 1500 × 1500 sump opening has no specified cover, so `SU-01` is drawn **open**. No lid was invented |
| **AN1-F7** | **The sentry post position is `[ASSUMED]` and fails its own rule as written.** `U4` stays open and `RC4-F3` records 9.00 m to the excavation face against a "≥ 10 m clear of the excavation" rule. **Both readings are stated on screen**: *"10.00 m to the box face — 9.00 m to the excavation."* The animation does not quietly adopt the flattering one |

---

## 8 Open items

| Ref | Item |
|---|---|
| **AN1-V1** | The walked route between the two real endpoints is undetermined by the project — no site circulation, path or hardstanding is drawn anywhere. `[V]` |
| **AN1-V2** | Blast front travel is **slowed for legibility**. The master gives t<sub>d</sub> 0.13–1.33 s but no propagation model, so no velocity, arrival time or decay is implied. The slowing is stated on screen |
| **AN1-V3** | Occupant tasking, posture and activity are specified nowhere. Figures are generic, without identifiable likeness `[V]` |
| **AN1-V4** | The EMP Zone 2 enclosure is drawn at EM1's **2400 × 1600 × 2200** `[A]`, which `EM-V2` records as an allowance pending the equipment schedule. If that schedule changes the enclosure, this animation changes with it |
| **AN1-V5** | Interior finishes and lighting are `[V]`. `Schedule of Finishes/` exists and is **not** modelled — including `W-04`, the Zone 2 lining |
| **AN1-V6** | The soundscape is synthesised and illustrative. No acoustic data exists in the project |
| **AN1-V7** | **AN1 is not registered with the drawing QA tool**, because it produces no DXF sheet. If a future revision adds drawing sheets, master H.25's rule applies and `qa_report_data.py` / `make_index.py` must be updated |
| **AN1-V8** | **NEW, from `AN1-F1`:** two levels differ between the owner's Revit model and master A.4.3. Needs an owner ruling on which is the intended value |

---

## 9 Running it, and recording it

**Running.** Open `AN1_UNDERGROUND_CBRN_OPS_ROOM.html` in any current browser. Press **Begin**.
It needs WebGL 2 and nothing else — no internet, no install, no player.

| Key | |
|---|---|
| `Space` | play / pause |
| `←` `→` | 5 s |
| `0` | restart |
| `F` | full screen |
| **`H`** | **hide the interface — press this before recording** |
| `M` | sound on / off |

Chapter buttons jump to any of the 21 beats, which is what to use when an examiner asks to see
the load path or Zone 2 again.

**Recording to a video file.** Full-screen (`F`), hide the interface (`H`), restart (`0`), then
capture with OBS Studio, the Windows Game Bar (`Win`+`G`), or QuickTime on macOS. Record at
1920 × 1080 or better. Let it run the full 6 min 22 s; it fades to black on its own.

**Presenting.** Run it live rather than from a recording if the machine allows — pausing on the
load path or Zone 2 to answer a question is worth more than a fixed film.

---

## 10 Rebuilding it

```
python3 Animation/Scripts/an1_build.py
```

`Animation/Source/*.js` are the sources; `Animation/Output/*.html` is a **build artefact and
must never be edited by hand.** The build prints the beat table and the running time, both read
out of `40_timeline.js`, so the design basis and the animation cannot drift apart.

| File | |
|---|---|
| `00_data.js` | **Every project value, each with its evidence tag.** Change nothing else first |
| `10_engine.js` | WebGL 2 core: maths, shaders, meshes, particles, section clipping |
| `20_facility.js` | Terrain, berm, strata, cover, box, stairs, shafts, headhouse, entry, sentry post |
| `25_fitout.js` | Bay contents and the figure rig |
| `30_effects.js` | Blast front, dust, grass, load-path arrows, airflow, EMP |
| `40_timeline.js` | The beat table, the camera track, the state function, the annotations |
| `50_audio.js` | The synthesised soundscape |
| `60_app.js` | Render loop, annotation projection, presenter controls |

---

## 11 QA/QC — what was actually verified, and how

Run in headless Chromium (Playwright) against the built file, with frames captured across all
21 beats.

| Check | Result |
|---|---|
| WebGL 2 context acquired | **PASS** |
| Console and page errors across a full traverse | **NONE** |
| Duration and beat count read back from the running page | **382 s, 21 beats** |
| Meshes constructed | **20** |
| Annotations constructed | **39** |
| Walk length / derived pace read back from the running page | **36.687 m / 0.655 m** |
| **Blast ordering** — front coordinate of the sentry post vs the box | **−29.50 < −8.66 → the post is crossed first. PASS** |
| Camera continuity — speed sampled mid-journey | **1.003 and 0.604 m/s, continuous, no jump** |
| Frames rendered and inspected | 33 first pass, 16 second pass |
| Main staircase geometry | **UNCHANGED** — 24R @ 170.8333, tread 280, 3 × 8, rise 4100, and the animation reads it from `PROJ.stair`, which is a transcription of A.4.4 |

### What could not be made consistent

- **`AN1-F1`** — the two Revit/master level discrepancies. Not resolvable without an owner
  ruling; carried as `AN1-V8`.
- **`AN1-F7`** — the sentry post's `[ASSUMED]` position and its 9.00 m against the ≥ 10 m rule.
  Both readings are shown rather than one being adopted.
- **The load path cannot be quantified** because no STAAD result exists. It stays conceptual.
- **The blast front's speed is not physical.** It is slowed to be watchable and says so.
