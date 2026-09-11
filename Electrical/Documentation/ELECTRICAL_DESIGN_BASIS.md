# ELECTRICAL AND POWER — DESIGN BASIS  ·  revision EL1
## Underground CBRN-hardened blast-resistant protective structure — Pune, Maharashtra

**Electrical and Power package revision EL1** · 11 September 2026
**Geometry:** Architectural Rev F · Structural Phase 2 Rev A + M1
**Services:** Drainage DR1 · HVAC HV1 · Finishes FN1 · Structural CAD SC1 · Works Management WM3 · Fire FS2 · Concealment CAM2 · **EMP EM1**
**Evidence classes:** `[C]` confirmed · `[R]` reconstructed · `[D]` derived here · `[A]` assumed by this package · `[U]` unresolved · `[N]` not available

> **A BASIC PACKAGE, ON PURPOSE.** It stops at **board level**: sources, a load schedule, three
> boards, the essential/battery system, one single-line diagram. **No circuit schedule, no cable
> sizing, no luminaire or socket layout, no protection study** — see §7 and **EL-V5**.

> **THIS PACKAGE CHANGES NO DESIGN.** No dimension, load, bar, wall, level, valve, duct, pipe or
> model is altered. It creates **no** penetration of the envelope. No BOQ quantity, rate, date or
> float changes — the owner's Works Management package governs. Main staircase untouched; sentry
> post excluded.

> Every figure here is produced by `Scripts/el_calc.py` and printed with its arithmetic in
> `Calculations/EL_CALC_OUTPUT.txt`.

---

## 0  Why this package exists

**"No electrical design package exists" has been the project's largest single gap** since WM1
(master H.10): *"the scope is confirmed — EMP Zone 2 enclosure, 15 kVA generator, earthing to
5 Ω, penetration protection — but no circuit, cable, luminaire, DB or earth-electrode schedule
does. Every electrical quantity reads 'to be verified from final measurement' and no electrical
enquiry can be issued."*

Three other packages are stuck behind it, by their own words:

| | |
|---|---|
| **FS-V2** (fire) | *"No fire detection, alarm, emergency lighting or suppression exists anywhere. **Follows the missing electrical design**"* |
| **EM-V2** (EMP) | Every EMP Zone 2 dimension is `[A]` pending an equipment schedule, **which waits on the electrical design** |
| **HVAC QA/QC P11** | *"Distribution, UPS and battery autonomy are an **electrical** scope item, **not designed here**"* |

This package is the minimum that unblocks them.

---

## 1  Sources — and one the master never recorded

| | | |
|---|---|---|
| **GEN-1** | 15 kVA standby set, Bay 8, the grey zone | `[C]` master A.3 |
| **MAINS** | via a **meter panel** | `[C]` — **but only in the owner's own programme** |
| **BATTERY** | **does not exist anywhere in the project** | `[N]` — §5 designs it |

**The mains supply is real and the master has never mentioned it.** The owner's master
construction schedule R0 — which **WM2 ruled governs** — carries activity **5 "Electricity
Provision"** and activity **123 "Electrical Wiring Works — Mains wire Pulling, Mater Panel
Fixing etc. (DB to Meter Panel)"**. A meter panel means a utility connection. So the shelter has
**two** sources, not one. But its **capacity, tariff and point of connection are `[N]`**, which
is why no fault level or discrimination study is possible here. **EL-V4.**

### And two sources that need no electricity at all — both already confirmed

- a **hand crank on both filter fans** `[C]` HVAC equipment schedule
- **hand pump PU-03** `[C]` drainage schedule and S-06

**These are the real last line, the project already has them, and no electrical design should be
allowed to obscure them.** `[D]`

---

## 2  Load schedule

Full schedule in `Schedules/LOAD_SCHEDULE.md`. Derived figures:
fan `P = Q·Δp/(η_fan·η_motor)`; pumps `P = ρgQH/(η_pump·η_motor)`; lighting by area.

| Tag | Load | Board | kW | Class |
|---|---|---|---|---|
| L-01 | General lighting, Bays 1–8, LED | DB-E | 0.520 | `[A]` |
| L-02 | Emergency lighting, maintained, DC | DB-E | 0.100 | `[A]` |
| P-01 | Small power, socket outlets | DB-M | 1.000 | `[A]` |
| F-01 | Filter train fan, **1 duty of 2** | DB-E | 0.379 | `[R]` |
| D-01 | Dehumidifier DH-1 | DB-E | 1.000 | `[A]` |
| U-01 | Clean sump pump PU-01, **1 duty of 2** | DB-E | 0.334 | `[R]` |
| U-02 | Stairwell pump PU-04, **1 duty of 2** | DB-M | 0.223 | `[R]` |
| Z-01 | **EMP Zone 2 ops / comms** | DB-Z2 | 1.500 | `[A]` |
| S-01 | Fire detection and alarm panel | DB-E | 0.100 | `[A]` |
| B-01 | Battery charger / inverter | DB-M | 0.800 | `[A]` |
| G-01 | Generator auxiliaries | DB-M | 0.300 | `[A]` |
| | **CONNECTED LOAD** | | **6.256 kW** | |
| | at power factor 0.85 | | **7.360 kVA** | |

**Standby units are not counted twice.** FAN-2, PU-02 and PU-05 are standby to FAN-1, PU-01 and
PU-04 and never run simultaneously with them `[C]`.

**The fan figure rests on an `[A]`.** HV1 records that only **161 Pa** of the fan's loss build-up
is derivable and **five of the eight components are vendor data** `[N]`. 2 000 Pa *dirty* is
assumed. The fan must be selected on dirty-filter figures, not clean.

---

## 3  Is the 15 kVA generator right? — yes, comfortably

| | |
|---|---|
| Connected load | 6.256 kW · **7.360 kVA** |
| **GEN-1 rating** `[C]` | **15.0 kVA** |
| **Utilisation** | **49.1 %** |
| Spare | 7.64 kVA |

**The confirmed 15 kVA is about twice the connected demand**, and 49 % sits in the healthy
loading band for a diesel set — high enough to avoid wet-stacking, low enough to carry growth.
The largest motor is the filter fan at **0.379 kW**; even a direct-on-line start is about
**2.7 kVA**. **There is no starting problem, and the project's own figure needs no change.** `[D]`

---

## 4  The question that decided the package — now ruled

> ### May the generator run during Mode 3 CLOSED?
>
> ### RULED YES — RC2, 11 September 2026 (master H.21) `[C]`
> **All five valves shut at the shock and hold 1.3 s; BV-4 and BV-5 are then reopened for generator operation.** Bay 8 is outside the gas-tight envelope, so the clean zone is unaffected — which is what the Mode 5 note always said. **HV1's Mode 3 row is amended to match. Case A is confirmed and EL-V1 is closed.**
>
> **No number in this package changes** — only the evidence class, from `[A]` to `[C]`. The question and its arithmetic are kept below, because the size of the consequence is why it was worth putting to the owner rather than assuming.

The project states **both** of these, in the **same confirmed schedule**:

| Mode | | |
|---|---|---|
| **3 CLOSED** | detonation to all-clear | ***"All five blast valves shut.*** Soda lime and O₂ only. **48 h limit**" |
| **5 GENERATOR RUNNING** | power **or battery charging** | ***"BV-4 and BV-5 open.*** Bay 8 only — does **not** touch the gas-tight envelope" — and *"Mode 5 is **independent** of modes 1–4"* |

**BV-4 and BV-5 are two of the five.** Mode 3 shuts them; Mode 5 needs them open. **The two
statements cannot both hold during Mode 3, and nothing in the project says which gives way.** `[U]`

Both readings are defensible:

- **Case A** — the valves shut at the shock, hold 1.3 s `[C]`, and BV-4/BV-5 are **reopened** once
  it has passed. Bay 8 is outside the gas-tight envelope, so the clean zone is untouched — which
  is exactly what the Mode 5 note says. The generator is available after a short outage.
- **Case B** — Mode 3 means *sealed*, all five, for the full **48 h**. The generator cannot run at
  all and the battery carries everything.

**The answer differs by a factor of twelve.**

---

## 5  The essential system and the battery

**Loads that stay live with no generator and no mains** — full list in
`Schedules/DISTRIBUTION_AND_ESSENTIAL_SCHEDULE.md`:

emergency lighting 0.100 · reduced general lighting 0.150 · fire detection 0.100 · EMP Zone 2 at
50 % 0.750 · clean sump pump intermittent 0.033 · CO₂ scrubber recirculation fan 0.100 `[A]` ·
instruments 0.050 → **1.283 kW**

> **Groundwater does not stop because the shelter is sealed.** The clean sump pump has to stay
> powered through Mode 3, and **hand pump PU-03** `[C]` is what covers it if the battery fails.

**48 V DC · depth of discharge 0.80 `[A]` · inverter efficiency 0.90 `[A]`**

| | Hours | Delivered | Rated | **Ah at 48 V** | Mass | Min floor |
|---|---|---|---|---|---|---|
| **Case A** | 4 | 5.13 kWh | 7.13 kWh | **149 Ah** | 204 kg | 0.40 m² |
| **Case B** | 48 | 61.61 kWh | 85.56 kWh | **1 783 Ah** | **2 445 kg** | **4.80 m²** |

> ### Case A is a cabinet. Case B is a room. They are 12× apart.

Case B is **2.4 tonnes** of lead-acid needing at least **4.8 m²** of floor merely to stay inside
the **5.0 kPa** floor live load `[C]` A.7.2 — **and Bay 5 is already 80 % occupied as drawn**
(MEP coordination **CO-3**). **There is nowhere to put it.**

**CONFIRMED: Case A, 4 h, 149 Ah at 48 V** `[C]` — **ruled, RC2.** EL1 had already adopted Case A
as `[A]`, reasoning that it is the reading **the project's own document implies**: the mode
schedule calls Mode 5 *"power **or battery charging**"* and says it is *"independent of
modes 1–4"*. **The ruling confirms that reading.**

> **No number changes. The battery stands at the size EL1 designed; only its evidence class
> moves. That is the best outcome a ruling can have — it confirms the design rather than
> replacing it. EL-V1 is CLOSED.**

> **One consequence, recorded not resolved.** Reopening BV-4 and BV-5 leaves **two DN350 bores
> open in the post-attack period** — the two EM1 showed **fail both EMP criteria** (cutoff
> 502 MHz, 54.8 dB). That **sharpens EM-V3** — whether Bay 8 is inside the EMP boundary —
> **without deciding it.** `[D]`

---

## 6  Distribution, cable entry and earthing

**Three boards, one cable entry.** Drawn on **E-001**.

| Board | Where | Fed from |
|---|---|---|
| **DB-M** main LV | Bay 8, grey zone, **outside** the gas-tight envelope | Mains + GEN-1, with changeover |
| **DB-E** essential | Bay 5, **inside** the gas-tight envelope | DB-M, and the **battery inverter** on loss of both sources |
| **DB-Z2** EMP Zone 2 sub-board | Bay 3, **inside the shielded enclosure** | DB-E **through the PCI** on the Zone 2 boundary |

**Every conductor crossing the protective envelope uses the service entry plate** — the project's
single services penetration `[C]` — with a **PCI on power** (MIL-STD-188-125-1 §5.7.2.1, EM1
**PoE-3**) and **fibre for signal** (§5.7.4.1, EM1 **PoE-4**). **This package creates no new
penetration.** The plate's level and size remain `[N]`.

**Earthing follows EM1's ruling and is not re-argued here.** `≤ 5 Ω` (IS 3043 / IEEE 142 `[C]`)
is **not achievable with rods in Deccan basalt** — 335 Ω per 3 m rod at the *low* resistivity
bound — **and is not an EMP number** in any case. **The mat and its cage are already a large
concrete-encased electrode at ≈ 38 Ω.** Bond to the structure; do not chase rods. See **EM-F5**.

---

## 7  What this package did not do

| | |
|---|---|
| **No circuit schedule, no cable sizing, no luminaire or socket layout** | It stops at board level on purpose. **EL-V5** |
| **No protection or discrimination study, no fault level** | All need the incoming supply capacity, which is `[N]`. **EL-V4** |
| **No equipment schedule for EMP Zone 2** | Z-01 is a **1.50 kW allowance**, a *basis* for EM-V2, not an answer to it. **EL-V3** |
| **No cooling load** | Because **no cooling plant exists anywhere in the project**. Referred to HVAC, not resolved here. **EL-V6** |
| **No BOQ change** | No quantity, rate, date or float. The owner's package governs |
| **Nothing resolved** | No existing `[ASSUMED]`, `[UNRESOLVED]` or `[NOT AVAILABLE]` tag is converted, downgraded or deleted |

**Codes used are only those already in the project's own references:** IS 732:2019 (wiring
installations), IS 3043:2018 and IEEE 142 (earthing), IS 694:2010 (final circuit cables),
IS 1554 Part 1:1988 (sub-mains and generator cabling), MIL-STD-188-125-1 §5.7.2.1 / §5.7.4.1
(via EM1). **No clause outside those is cited, and none is invented.**

---

## 8  What this package unblocks

| Item | Was | Now |
|---|---|---|
| **13 gaps — "no electrical design package exists"**, the largest | Nothing | **A basic design exists.** The detailed design still does not — **EL-V5**. **Advanced, not closed** |
| **FS-V2** — no detection, alarm or emergency lighting; *"follows the missing electrical design"* | Blocked | **S-01 and L-02 exist on the essential board, on the battery. The electrical blocker is gone.** Head layout and zoning remain fire engineering. **Advanced, not closed** |
| **EM-V2** — Zone 2 dimensions await an equipment schedule | Blocked | **Z-01 gives a 1.50 kW allowance and a sub-board**, so the enclosure has a basis instead of nothing. Still an allowance. **Advanced, not closed** |
| **HVAC P11** — *"distribution, UPS and battery autonomy … not designed here"* | Deferred | **Designed. Closed** |
| **FS-V4 / R-8** — generator fuel unspecified | No number | **First number: ≈ 210 L for a 96 h run** `[A]` (600.6 kWh at 0.35 L/kWh). A bounded estimate, not a specification. **Advanced, not closed** |
| **EM-F5** — earthing | Ruled by EM1 | **Adopted unchanged.** Not re-argued |

**Nothing above is claimed as closed except HVAC P11**, which was explicitly a deferral to this
scope.

---

## 9  Open items — EL-V1 to EL-V7

| | | Whose decision |
|---|---|---|
| **EL-V1** | ~~May the generator run during Mode 3 CLOSED?~~ **RULED YES — RC2, 11 September 2026 (master H.21). Case A confirmed at 149 Ah; HV1's Mode 3 row amended. CLOSED — and no number in this package changed.** | **Closed** |
| **EL-V2** | **Generator fuel type, quantity and storage.** ≈ 210 L for 96 h is derived here; nothing is specified. Same root as **FS-V4** and **R-8** | Client / vendor |
| **EL-V3** | **No equipment schedule for EMP Zone 2.** Z-01's 1.50 kW is an allowance | Client / ops |
| **EL-V4** | **Incoming mains capacity, tariff and point of connection.** Recorded only as *"DB to Meter Panel"* in the owner's programme; no capacity anywhere. Blocks any fault level or discrimination study | Utility / client |
| **EL-V5** | **No circuit, cable, luminaire or socket schedule.** Deliberate — this package stops at board level | Detailed design stage |
| **EL-V6** | **No cooling plant exists anywhere in the project**, so no cooling load appears in §2. A sealed 332.8 m³ box with 9 occupants and a dehumidifier has a heat balance nobody has computed | HVAC |
| **EL-V7** | **The CO₂ scrubber's air movement is not in any schedule.** 0.10 kW is assumed for a recirculation fan; soda lime needs air over it and no fan is specified | HVAC |

---

## 10  QA/QC

| # | Check | Result |
|---|---|---|
| Q1 | Every confirmed duty traced to its source document | **PASS** — GEN-1 to master A.3; FAN/AHU/DH-1 to the HVAC equipment schedule; PU-01/PU-04 to the drainage schedule; mains to the owner's programme activities 5 and 123 |
| Q2 | Standby plant not double-counted | **PASS** — FAN-2, PU-02, PU-05 excluded |
| Q3 | Generator adequacy | **PASS** — 49.1 % utilisation, 7.64 kVA spare |
| Q4 | Motor starting | **PASS** — largest 0.379 kW, DOL ≈ 2.7 kVA |
| Q5 | Battery arithmetic reproducible | **PASS** — both cases printed with inputs in `EL_CALC_OUTPUT.txt` |
| Q6 | E-001 validated | **PASS** — `mep_validate.py` **0 errors, 0 warnings**; `dxfqa.py` **0 text overlaps** |
| Q7 | No new envelope penetration | **PASS** — single cable entry via the existing service entry plate |
| Q8 | No shared library modified | **PASS** — `el_dxf.py` subclasses `mep_dxf.py` and uses the FS2/CAM2 hooks |
| Q9 | No existing evidence tag altered | **PASS** |
| Q10 | No BOQ quantity, rate, date or float changed | **PASS** |

**Could not be checked:** every `[A]` in §2 — the dehumidifier duty, the lighting density, the
small-power and ops allowances, the fan static pressure and both pump heads. **They are
allowances that let a load schedule exist at all, and each is flagged where it is used.**

---

*Electrical and Power package revision EL1 · 11 September 2026 · FOR REVIEW — NOT FOR CONSTRUCTION*
*Basic design, stops at board level · Sentry post excluded · Main staircase unchanged · No design value altered*
