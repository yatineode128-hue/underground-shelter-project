# HVAC DESIGN BASIS

**Underground CBRN-hardened blast-resistant protective structure — Pune, Maharashtra**
Package **HVAC**, revision **HV1** · 5 September 2026 · geometry **Rev F + M1**
Status: **DEVELOPED FOR PROJECT COORDINATION — PENDING ENGINEERING VERIFICATION**

**Sentry post is excluded from this package.** No sentry post ventilation is designed, drawn,
scheduled or quantified here.

---

## 1 Authority, evidence and what this package did not do

`master/MASTER_PROJECT_STATE.md` governs. Evidence classes are the master's own — `[C]` confirmed,
`[R]` reconstructed here, `[A]` assumed by this package, `[U]` unresolved, `[N]` not available.

**The ventilation basis for this shelter already existed before this package started.** Issued sheet
S-06 carries the occupancy, the three airflow criteria, the design flow, the N+1 configuration, the
leakage allowance, the overpressure cascade, the closed-mode CO₂ and O₂ figures, the airlock purge,
the seven-stage filter train and all five blast valves with their sizes, flows, velocities and disc
forces.

**This package does not re-derive any of it.** What it does is:

1. **Reproduce every S-06 figure from first principles**, to prove the sheet is internally
   consistent and to make the basis checkable. All eleven reproduce — see §2.
2. **Develop what S-06 does not carry**: room-by-room airflow, duct sizes and velocities, duct
   pressure loss, the fan-duty build-up, terminal and damper schedules, duct routing coordinated
   against the structure, and the operating-mode set.
3. **Record what cannot be determined** rather than filling it in.

Codes are cited only from the master Part G register — `FEMA 453`, `EN 1822`, `IS 4991`,
`MIL-STD-188-125-1`, `IS 875 (Pt 2)`. `IS 3103` and the ISHRAE/ASHRAE handbooks are named **by title
only**; no clause is quoted from them, because no code document is in the workspace (master open
item **M2**). The air properties and duct roughness used in the pressure-loss calculation are
standard tabulated values whose source is likewise not in the workspace, and are tagged `[A]`.

---

## 2 Reproduction of the S-06 basis

| S-06 states | Reproduced from | Result |
|---|---|---|
| Gas-tight envelope **67.8 m² / 217.0 m³** | Bay widths 2900+1800+3500+1800+1560+2000 × 5.000 × 3.200 | **67.80 / 216.96** ✔ |
| Clean zone **57.8 m²** | Envelope less the 10.0 m² decon airlock | **57.80** ✔ — *S-06 does not say this; the FEMA rate is applied to the clean zone, not the envelope* |
| Occupied volume, airlock shut **185.0 m³** | 57.80 × 3.200 | **184.96** ✔ |
| FEMA 453 rate **264 m³/h** | 57.8 m² × 10.76391 = 622.2 ft² × 0.25 cfm/ft² × 1.699011 | **264.3** ✔ (0.10 %) |
| Leakage **32.5 m³/h** | 0.15 vol/h × 216.96 | **32.5** ✔ = **10.8 %** of one train (S-06: "11 %") |
| Time to 1.0 % CO₂ **9.9 h** | (0.0096 × 184.96) / (9 × 0.02) | **9.9** ✔ |
| Airlock purge **13 min** | 5 × (2.0 × 2.0 × 3.2) = 64 m³ at 300 m³/h | **12.8 min** ✔ |
| DN100 throat **10.6 m/s** | 300 / 3600 / (π × 0.05²) | **10.61** ✔ |
| DN350 throat **7.5 m/s** | 2600 / 3600 / (π × 0.175²) | **7.51** ✔ |
| Survival / working rates | 5 × 9 = 45, 15 × 9 = 135 m³/h | ✔ |
| O₂ store **15 m³** | 2 × 50 L at 150 bar | ✔ = **80 h** at 4.5 m³/day |

**Every figure on S-06 reproduces. The sheet is internally consistent.**

---

## 3 Design basis — the numbers

| Parameter | Value | Class |
|---|---|---|
| Occupancy / endurance | **9 persons / 96 h** | `[C]` |
| Design flow | **300 m³/h**, 2 × 300 trains, **true N+1** | `[C]` |
| — against the criteria | 6.7 × survival, 2.2 × working, 1.14 × FEMA | `[R]` |
| — per person | **33.3 m³/h** | `[R]` |
| ACH, whole envelope / clean zone | **1.38 / 1.62** | `[R]` |
| Leakage | ≤ 0.15 vol/h at +300 Pa = **32.5 m³/h**, 11 % of one train | `[C]`/`[R]` |
| Operating overpressure | **+50 to +100 Pa**, tested at +300 Pa | `[C]` |
| Cascade | **0 → +10 → +20 → +35 → +50 Pa** | `[C]` |
| Closed mode | CO₂ 0.18 m³/h; **9.9 h** unscrubbed, **48 h** on soda lime, **80 h** on O₂ | `[C]`/`[R]` |
| Airlock purge | 64 m³, **12.8 min**, **4–5 persons/hour** | `[R]` |
| Ductwork + plenum loss | **161 Pa** | `[R]` |
| Total fan duty | **VENDOR DATA REQUIRED** — 5 of 8 components | `[N]` |
| Cooling load | **NOT CALCULATED** — 8 inputs missing | `[N]` |

---

## 4 Room-by-room airflow — developed here

S-06 gives the total and does not distribute it. **The nine occupants are not in two places at
once**: they work in U-03 and sleep in U-04. A single fixed split would starve whichever of the two
is occupied, so the distribution is **balanced in two modes** on two volume control dampers.

| Room | Use | Volume m³ | Day m³/h | Night m³/h | Extract m³/h |
|---|---|---|---|---|---|
| U-01 | Emergency stores / ESC 1 | 46.40 | 30 | 30 | — |
| U-02 | Lavatory + medical | 28.80 | 30 | 30 | **45** |
| U-03 | Ops room & hazard plotting | 56.00 | **135** | 45 | — |
| U-04 | Berthing, 9 berths | 28.80 | 45 | **135** | — |
| U-05 | CBRN plant + sump | 24.96 | 60 | 60 | — |
| U-06 | Decon airlock | 32.00 | *300 transfer* | *300 transfer* | *to BV-3* |
| | **TOTAL** | | **300** | **300** | |

**The occupied room of the pair gets 135 m³/h = 15.0 m³/h per person — exactly the working-shelter
rate S-06 names as criterion 2.** The dampers are not a refinement: holding 15 m³/h/person in *both*
rooms at once would take 270 of the 300 m³/h and leave 30 m³/h for the stores, the lavatory *and* the
plant room. If a reviewer requires that, the total must rise above 300 m³/h — **a change to a
confirmed value on S-06. Raised, not taken.**

**Nothing is supplied to Bay 6.** The airlock is the exhaust path: the whole 300 m³/h transfers
through the three decon stages and out at BV-3, which is what makes the confirmed cascade work. The
cascade maps exactly onto the three airlock stages — a `[R]` observation S-06 does not state.

---

## 5 Duct sizing, velocity and pressure loss

Distribution ducts are selected for 3–5 m/s. **The small branches are governed by the practical
minimum duct size, not by velocity** — at 30 m³/h a duct sized for 4 m/s would be about 100 × 25 mm,
which is not buildable, not cleanable and not sealable to the standard this envelope needs.

Blast-valve throats are **not** a design choice: DN100 and DN350 are fixed on S-06.

Pressure loss by Darcy–Weisbach with Colebrook–White friction, ρ = 1.204 kg/m³, ν = 1.51 × 10⁻⁵ m²/s,
ε = 0.15 mm `[A]`:

| Route | L m | v m/s | Δp Pa |
|---|---|---|---|
| Raw air, BV-1 → AHU-1 | 11.2 | 2.65 | 20.7 |
| Supply, plenum → Bay 1, index run | 10.6 | 3.33 | 40.8 |
| Lavatory extract | 9.3 | 1.59 | 1.4 |

**Fan duty cannot be closed.** Five of the eight components — louvre, blast valve, pre-filter, HEPA
and carbon bed — are vendor data, and in a CBRN train they dominate. The part that can be
calculated is **161 Pa** (ductwork + the confirmed 100 Pa plenum). **Quoting a total without the
vendor figures would be a fabricated number.** What must be specified at procurement: the clean
*and* dirty pressure drop of every stage; the fan selected on the **dirty** figure; the hand crank
sized on the same duty; and the plenum held at +50 to +100 Pa across the whole range.

---

## 6 Cooling, heating and humidity — not calculated

**No cooling load is calculated in this package.** Eight inputs are missing: outdoor and indoor
design conditions, occupant sensible and latent rates, equipment heat, generator heat rejection,
ground temperature at (−)6.100, and the thermal properties of the buried envelope. `[N]`

A dehumidifier **is** confirmed in Bay 5 and its condensate **is** in the S-06 drainage flow table,
but **its duty is not stated anywhere** and no target humidity exists.

What can be said without inventing anything: a structure surrounded by 4.7 m of rock is a very large
thermal flywheel, and its steady state is governed by the **rock temperature**, which is the missing
number. A cooling load calculated from air-side data alone would be wrong in both directions by an
unknown amount. An upper bound on the closed-mode air temperature rise — **ignoring the concrete
entirely, which is why it is only a bound** — is tabulated in calculation H.10 at three assumed
occupant rates. **Do not size plant on it.**

---

## 7 Protective ventilation

All confirmed on S-06 and carried forward unchanged: five blast valves (positions parsed out of the
sheet's geometry), the seven-stage filter train, recessing to IS 4991 Cl. 6.2.1, the ≥ 2.0 m duct
rule, a manual quarter-turn gas-tight damper inboard of every valve, and the hand crank on each fan.

**Five operating modes** are defined here (M-203): normal, filtered/protective, closed, purge, and
generator running. **Mode 5 is independent of modes 1–4** — the generator air path serves Bay 8
only, outside the gas-tight envelope, so running it neither depressurises the clean zone nor
consumes filter life.

---

## 8 Findings and open items raised by this package

| Ref | Item | Status |
|---|---|---|
| **HV-F1** | **The soda lime, not the oxygen, limits closed mode.** Unscrubbed CO₂ gives 9.9 h; the 40 kg soda-lime store gives 48 h; the 15 m³ oxygen store gives 80 h. S-06 gives all three figures but does not draw the conclusion. **It is the consumable to count and the one to write on the drill card.** Closed mode covers 48 of the 96 h endurance; the other 48 h *require* filtration. |
| **HV-F2** | **The raw-air duct is a protective element, not a duct.** S-06 puts the fresh-air blast valves in the west wall of Bay 1 and the filter trains in Bay 5. Between them the air is **unfiltered**, and FA-2/FA-3 carry it **11.2 m through the clean zone**. Over that length the duct wall is the only barrier. **Positions not changed** — they are confirmed on an issued sheet — but the duct is specified as a protective element: fully welded, no push-fit or slip joints, **tested to the +300 Pa envelope standard**, run visible and never boxed in, labelled *RAW AIR — UNFILTERED* at ≤ 2 m centres, re-tested after any work in bays 1–4. **The question for the protective designer — should the trains move to Bay 1? — is raised, not taken.** |
| **HV-D1** | **No filter bypass for peacetime running is shown on S-06.** Without one, every peacetime hour spends carbon-bed life replaceable only in closed mode. A bypass is a deliberate leak path around the filters — a protective decision. **Not added. Engineer to confirm.** |
| **HV-D2** | **BV-3 discharges into Bay 7.** The onward path to atmosphere — up the stair shaft and out through the headhouse — **is not recorded anywhere**. A path exists (the shaft is not sealed) but its resistance is unknown and it is in series with the OPRV. |
| **HV-D3** | No cooling load can be calculated — §6. |
| **HV-D4** | **No noise criterion exists anywhere in the project.** Terminal selection cannot be closed. A berthing space for nine is exactly where a noisy diffuser is felt. |
| **HV-D5** | Dehumidifier duty not stated. |
| **HV-D6** | Fan static pressure — 5 of 8 loss components are vendor data. |
| **HV-F3** | **Maintenance access is the tight dimension, not headroom.** Each train is 1450 wide in a 1560 clear bay — 110 mm at the sides — so all access is along the bay. A HEPA and a carbon cassette must be carried in through Blast Door 1 (1200 × 2100), along bays 6 and 5. **Confirm the cassette dimensions against that route before the trains are ordered.** |

**Carried, not resolved:** master **C16** — *no HVAC dependency*: no duct, plant item or penetration
is at the roof/platform junction. **A2** (GWT) affects only the condensate route.

---

## 9 Coordination

| Interface | Requirement |
|---|---|
| **Structure** | No duct penetrates the 900 pressure slab or the 600 mat. Every envelope crossing is horizontal, through a wall, at a confirmed blast-valve position. Ducts occupy a 150 deep zone under the (−)2.900 soffit; 2950 clear remains. |
| **Drainage (DR1)** | Condensate from DH-1 and any coil discharges to the clean sump — in the same bay — through a **75 mm deep-seal trap** with an air gap. That trap is a pressure boundary at +300 Pa, sized in drainage calculation D.6. |
| **Architecture** | Terminals coordinated with the room layout; **no duct, diffuser or support is placed in the main staircase**, whose geometry is frozen. |
| **Electrical** | Fan starters, damper actuators, the high-level alarms and emergency power are an electrical scope item, **not designed here**. The hand crank makes ventilation independent of all of it. |
| **Blast / CBRN** | The blast valves, the gas-tight dampers, the OPRV and the raw-air duct are protective components. Any change to them is a protective-design change. |

---

**Prepared under package revision HV1.** Calculations `Calculations/HV_CALC_OUTPUT.txt`
(reproducible: `python3 Scripts/hv_calc.py`). Drawing register
`Documentation/HVAC_DRAWING_INDEX.md`. QA/QC `QAQC/HVAC_QAQC.md`.
