# EMP PROTECTION — DESIGN BASIS  ·  revision EM1
## Underground CBRN-hardened blast-resistant protective structure and sentry post — Pune, Maharashtra

**EMP Protection package revision EM1** · 10 September 2026
**Geometry:** Architectural Rev F · Structural Phase 2 Rev A + M1
**Services:** Drainage DR1 · HVAC HV1 · Finishes FN1 · Structural CAD SC1 · Works Management WM3
**Evidence classes:** `[C]` confirmed · `[R]` reconstructed · `[D]` derived by this package ·
`[A]` assumed by this package · `[U]` unresolved · `[N]` not available — data required

> **Every figure in this document is produced by `Scripts/em_calc.py` and printed with its
> arithmetic in `Calculations/EMP_CALC_OUTPUT.txt`.** Nothing is typed by hand and nothing is
> quoted from memory.

> **THIS PACKAGE CHANGES NO DESIGN.** No dimension, load, bar, wall, level, valve, duct, pipe
> or model is altered. It creates **no** penetration of the envelope and moves none. The main
> staircase is untouched. The sentry post is excluded, as it is from every other services
> package.

> **`EMP Zone` is not `zone`.** Drainage and finishes already use *zone 1 / 2 / 3* for
> **cleanliness**. The EMP zones defined here are a different scheme on the same building. The
> prefix **`EMP`** is mandatory on every drawing, schedule and note in this project.

---

## 0  The fact that governs everything else

**The concrete box is not an EMP shield, and it never could have been.**

The project's EMP requirement is confirmed and specific — master Part G, the code register:

> **MIL-STD-188-125-1 — 80 dB, 10 kHz to 1 GHz.**

That is **five decades**. Two independent pieces of arithmetic, both from confirmed geometry,
say the box does not deliver it.

**First, the reinforcement cage.** Bar spacing is **150 mm, both curtains, both ways** — master
A.5 records it as *"an EMP requirement, stricter than IS 456 Cl. 26.3.3"* `[C]`. Treated as what
it is, a conducting screen pierced by a square array of apertures:

| | |
|---|---|
| `SE = 20 log₁₀(λ / 2s)`, s = 150 mm | |
| SE at 10 kHz | **99.99 dB** |
| SE at 100 kHz | **79.99 dB** |
| SE at 1 MHz | **59.99 dB** |
| SE at 100 MHz | **19.99 dB** |
| **SE at 1 GHz** | **0.00 dB** |
| Mesh cutoff, `c/2s` | **999.31 MHz** |
| **Highest frequency at 80 dB** | **99.93 kHz** |
| **Fraction of the required band met** | **one decade of five — 20 %** |

**This reproduces the project's own number.** Master **K.3** already records, as a confirmed
item: *"EMP rebar cage 0 dB @ 1 GHz — **say it before a reviewer does**. Zone 2 welded steel room
is the answer."* The calculation reaches **0.000 dB at 1 GHz from the 150 mm spacing alone**.
K.3 was right, and this package is the arithmetic behind it. `[R]`

And a coincidence worth saying out loud: **2s = 300 mm; the wavelength at 1 GHz is 299.79 mm.**
The cage stops shielding at almost exactly the frequency at which MIL-STD-188-125-1 stops
asking. That is arithmetic, not design.

**Second, the holes.** A 900 mm pressure slab with a **2 800 × 3 160 stair void** in it —
**8.85 m²** — is not a shield at any frequency. Nor are two **1 400 mm** escape shafts. Section
3 takes every penetration one at a time.

**So the 80 dB boundary has to be the EMP Zone 2 enclosure, and EMP Zone 2 is the only EMP
shield this project has. It has never been specified.** Master A.3 has placed *"an EMP Zone 2
enclosure"* in bay 3 since Rev F; the finishes package carries it as `W-04`,
*"specialist — welded steel room, shielding effectiveness verified to IEEE Std 299"*, classed
**`[C]` requirement / `[N]` specification**. Four revisions, no specification.

---

## 1  What the design already does right

**Four real strengths, and not one of them had been written down as an EMP measure.**

**1.1 The 150 mm bar spacing is a deliberate EMP decision, and it was the right one.**
It is stricter than IS 456 Cl. 26.3.3 needs and it is recorded as an EMP requirement in the
master, in the Structural CAD package, in eight bar-bending schedules and on the drawings
themselves. It cannot make the box a MIL-STD boundary — but **99.99 dB at 10 kHz is not
nothing**, and E3 HEMP, the slow component that drives long conductors, lives at the bottom of
the band where the cage is strongest. **The cage earns its keep exactly where it can.**

**1.2 The cast-in frames are already specified as EMP bonds.** Master A.5 requires every blast
door frame to be *"cast in and **WELDED to the cage** (EMP)"* `[C]`, and B.7.2 requires it even
for the **non-blast-rated** headhouse door — *"because the EMP shield must be electrically
continuous."* The HVAC package carries the same rule for every duct crossing. **That is correct
EMP practice, correctly specified, four packages deep.**

**1.3 Every construction joint already carries a welded EMP strap.** Master F.1: joints at
roughly 6 m with *"reinforcement fully continuous, two waterstops **and a welded Cu/galvanised
EMP strap**"* `[C]`. A construction joint is where a cage loses continuity, and the project
already knew it.

**1.4 There are no movement joints inside the protective envelope, and the master says why.**
Part M: *"A movement joint is a guaranteed blast, gas **and EMP** discontinuity."* `[C]` A
designer who writes that sentence has understood the problem.

**None of this was ever collected into an EMP position.** That is what this package is.

---

## 2  The zone model — adopted by the project owner

**"EMP Zone 2" had been named since Rev F with nothing to be the second of.** There was no EMP
Zone 1 and no EMP Zone 0 anywhere in the project. All three below were **derived by EM1** and are
now:

> ### ADOPTED — RC2, 11 September 2026 (master H.21) `[C]`
> **The project owner has adopted the three-zone model and the standing-alone design rule. They
> are the project's EMP position, not this package's proposal. EM-V1 is closed.**
> **Nothing else in EM1 changes** — no figure, no finding, no other open item. The model was
> already what the package was built on; the ruling makes it the project's rather than this
> package's.

| Zone | What it is | Performance | Verification |
|---|---|---|---|
| **EMP ZONE 0** | Everything above grade — sentry post +7.000, headhouse +0.900 **with no earth cover**, covered stairwell +2.450 (**expendable**), shaft heads, burster slab | **None credited** | n/a |
| **EMP ZONE 1** | The buried box, **all eight bays**. The reinforcement cage | **99.99 dB at 10 kHz → 0 dB at 999 MHz**, pierced by a 8.85 m² stair void and two 1 400 shafts. **80 dB only below 99.93 kHz** | **Cannot be surveyed** — no accessible exterior under 2 m of cover |
| **EMP ZONE 2** | Welded steel enclosure, bay 3 (U-03), finish `W-04` | **80 dB, 10 kHz – 1 GHz, standing alone** | **IEEE Std 299 full survey — HOLD POINT** |

### The design rule, adopted with the model — the whole package in one line

> ### EMP Zone 2 is designed to the full 80 dB **standing alone**. **No attenuation from the concrete box is credited at any frequency.** — **ADOPTED, RC2** `[C]`

The cage is then **margin**, not design — which is the only defensible way to use a shield you
can never survey, buried under two metres of engineered cover. `[D]`

### What EMP protection is *for*, said plainly

The small enclosure invites the wrong reading, so: **HEMP is not a personnel hazard.** The
occupants are protected from blast, CBRN and fallout by the box. **EMP protection exists so the
shelter can still *function* afterwards.** Zone 2 protects **equipment**. It is correct that it
is an enclosure and not a room, and nobody should expect to shelter inside it. `[D]`

---

## 3  Every hole in the envelope

Ten penetrations. Every position, bore and wall thickness is read from a confirmed project
document — the HVAC damper and valve schedule, `MEP_AND_FINISHES_COORDINATION.md` CO-1, master
A.4.4 and A.4.5. Full register in `Schedules/ENVELOPE_PENETRATION_REGISTER.md`.

A depth (waveguide-below-cutoff) credit is taken **only where the bore is bounded by metal**.
Concrete is a lossy dielectric, not a waveguide wall.

| Tag | Bore | Wall | Bounded by | Cutoff | WBC | Verdict |
|---|---|---|---|---|---|---|
| **BV-1 / BV-2** | 100 ⌀ | 600 | steel | 1 757 MHz | **192 dB** | **PASS** |
| **BV-3** | 100 ⌀ | 400 | steel | 1 757 MHz | **128 dB** | **PASS** |
| **BV-4 / BV-5** | 350 ⌀ | 600 | steel | **502 MHz** | **54.8 dB** | **FAIL — both criteria** |
| **SEP** *(read as an open aperture — the wrong reading, see 3.4)* | 800 wide | 600 | steel | 187 MHz | 20.5 dB | see 3.4 |
| **PD-05** | 50 ⌀ | 600 | steel | 3 514 MHz | **384 dB** | **PASS** |
| **ESC 1 / ESC 2** | 1 400 ⌀ | 3 050 / 3 600 | **concrete** | **126 MHz** | **none** | **FAIL** |
| **STAIR VOID** | 3 160 | 900 | **concrete** | **47.4 MHz** | **none** | **FAIL** |

> **The three-figure numbers are theory, not performance.** No practical penetration achieves
> 250 or 380 dB. Real assemblies flatten out around 100–120 dB, and what limits them is
> **workmanship** — the bond at the frame, the gasket, the one sleeve nobody welded. Read a
> large number as *"the bore is not the problem here."* `[D]`

### 3.1 The stair void — the finding of this package

**2 800 × 3 160 through the 900 pressure slab. 8.85 m². The largest aperture in the envelope.**

| Frequency | SE |
|---|---|
| 10 kHz | 73.52 dB |
| 100 kHz | 53.52 dB |
| 1 MHz | 33.52 dB |
| 10 MHz | 13.52 dB |
| **above 47.4 MHz** | **0 dB — simply open** |

**It never reaches 80 dB anywhere in the band.** It is bounded by the thickened free edge,
900 → 1200 with **6-T25** top and bottom `[C]` F.1 — six bars, which is not a conducting
surface, so it earns no depth credit at all.

And it does not open into soil. **It opens into the headhouse**, which sits at **+0.900 with no
earth cover** `[C]` A.4.6, and thence to grade through a **covered stairwell that is declared
expendable** `[C]` A.2. **The entry route is an open electromagnetic path from grade to bay 7.**

**Blast Door 1, in W6, is the only thing between that path and the occupied bays** — and a blast
door is a mechanical and gas seal. Whether it is an *RF* seal is vendor data the project does
not have `[N]`. Its frame is already required to be cast in and welded to the cage `[C]`, which
is the right start and is not the same as a certified RF door.

**This is finding EM-F1.** It is not a criticism of the architecture: a shelter needs a
staircase, and the stair void is exactly where a staircase has to go. It is a statement that
**the protective boundary for blast and the protective boundary for EMP are not the same
surface, and the project has only ever drawn one of them.**

### 3.2 The escape shafts

Two 1 400 ⌀ bores, 250 RC collars, heads at +0.150 and +0.700 `[C]` A.4.5. The TE11 cutoff of a
1 400 bore is **125.5 MHz** — above that a 1 400 tube propagates, however it is treated.

A **fully conducting liner** would give **69.7 dB** on ESC 1 and **82.2 dB** on ESC 2 — one below
the requirement, one barely above it — and **both figures only hold below 125.5 MHz.** The
collars carry **5-T25 each side, face and direction** `[C]` F.1: five bars, not a conducting
tube, so as built they earn nothing.

**Lining the shafts does not fix them.** The treatment that works is a **bonded conducting hatch
at the head**, which *terminates* the shaft instead of trying to attenuate down it. **No hatch is
specified anywhere in the project.** `[N]`

### 3.3 The two DN350 generator bores — and the decision behind them

**BV-4 and BV-5 are the only penetrations that fail both criteria**: cutoff **502 MHz** (below
the 1 GHz top of the band) and **54.8 dB** (below the 80 dB required). Compare the DN100 valves
in the same 600 wall — cutoff **1 757 MHz**, attenuation **192 dB**. **The wall does the whole
job for a DN100 and cannot for a DN350.** Bore, not workmanship, decides it.

But the real question is not how to fix BV-4/BV-5. It is **whether bay 8 is inside the EMP
boundary at all** — and **no EMP boundary has ever been drawn** `[U]`. Bay 8 is outside the
*gas-tight envelope* `[C]` A.2, but that is a **CBRN** boundary and says nothing about EMP.

- **If bay 8 is IN** — both bores need a honeycomb WBC panel inboard of the valve.
- **If bay 8 is OUT** — the **15 kVA generator, its control panel and every cable in bay 8 are
  unprotected**, and the shelter loses power to the pulse.

**This is EM-V3, and it is a client decision, not a drafting one.**

### 3.4 The service entry plate

X 11398–12198 in the north wall, **800 wide**, **level `[N]`, size `[N]`**.
`MEP_AND_FINISHES_COORDINATION.md` CO-1 records that it must be at **high level** because PD-05
rises over the filter trains, and that **its level is not recorded anywhere in the project**.

**Read as an open aperture** it would be a catastrophe — cutoff 187 MHz, 20.5 dB. **Read
correctly it is not an aperture at all.** A MIL-STD-188-125-1 entry plate **is** the shield: a
solid welded plate, bonded **360°** to the cast-in frame, itself welded to the cage. Its
apertures are the individual sleeves, and each is treated on its own:

| Service | Treatment | § |
|---|---|---|
| **PD-05** DN50 bore | cutoff 3 514 MHz, **384 dB** — ample | 5.5 |
| **Power** | **PCI on every conductor**, mounted *on* the boundary | 5.7.2.1 |
| **Signal** | **FIBRE** — a dielectric penetration is not a penetration | 5.7.4.1 |

> **One warning. PD-05's material is not specified anywhere in the project** `[N]` — the drainage
> package names **no pipe material for any run**. It changes the treatment completely:
> a **metallic** pipe is bonded 360° to the plate and its exterior becomes shield — correct, and
> cheap. A **plastic** pipe is an aperture *and* a conducting water column through it, and needs
> a metallic spool piece at the plate that nobody has specified. **EM-V5.**

---

## 4  EMP Zone 2 — the enclosure

**Every dimension in this section is `[A]`.** The project confirms the enclosure is **required**
and contains **no specification for it**. There is no equipment schedule, because **no electrical
design exists** — the project's largest single gap `[C]` master H.10. What follows is a competent
placeholder that demonstrably fits, **not a derived size**. See **EM-V2**.

| | |
|---|---|
| Host | Bay 3 (U-03), internal 3 500 × 5 000 × 3 200 `[C]` A.3 |
| **External** | **2 400 × 1 600 × 2 200**, at X 5820–8220, Y 3700–5300 |
| Shielded panel | 50 |
| **Internal clear** | **2 300 × 1 500 × 2 100** |
| Internal floor / volume | 3.45 m² / 7.245 m³ |
| **Shielded envelope area** | **25.28 m²** — walls 17.60, roof 3.84, floor 3.84 |
| **Total seam length** | **24.80 m** |

### Why it is where it is

| Clearance | |
|---|---|
| North, to the wall face Y 5600 | **300** |
| South, to the circulation edge Y 3400 | **300** |
| West, to the bay face X 5520 | **300** |
| East, to the bay face X 9020 | 800 |
| Head, to the roof soffit (−)2.900 | 1 000 — **850 clear above the 150 HVAC duct zone** `[C]` HV1 |

The W8 partition door gaps are at **Y 2500–3400** `[C]` A.3, so the east–west circulation route
through bay 3 runs at Y 2500–3400. **The enclosure is entirely clear of it.**

**A 300 mm gap is held on every free face so an IEEE Std 299 survey can physically reach every
seam.** A shielded room you cannot walk around cannot be tested, and **an untested shield is a
claim, not a shield.**

> **The seam length is the risk, not the area.** Every one of those **24.8 metres** has to be
> continuously welded or continuously gasketed, and IEEE Std 299 will find the metre that is not.

### The five ways in

Full schedule in `Schedules/POE_PROTECTION_SCHEDULE.md`. Section numbers are only those already
in the project's own code register — **no clause not in master Part G is cited.**

| PoE | Treatment | Performance |
|---|---|---|
| **PoE-1 ACCESS** §5.4 | RF-gasketed or knife-edge shielded door | ≥ 80 dB · **type and vendor `[N]`** |
| **PoE-2 VENTILATION** §5.5 | Honeycomb, **6 mm cell × 25 mm deep** | cutoff **29.3 GHz** · **133 dB** (**+53 dB** margin) |
| **PoE-3 POWER** §5.7.2.1 | PCI on every conductor, mounted **on** the boundary | **`[N]` — no residual quoted** |
| **PoE-4 SIGNAL** §5.7.4.1 | **Fibre**, no metallic strength member or armour | **A dielectric is not a penetration** |
| **PoE-5 RF** §5.7.6 | — | **Nothing to apply it to — see EM-F6** |

**PoE-2 is mounted inboard of any blast device** — the valve takes the pressure, the honeycomb
takes the RF. Its own blast rating is `[N]`. **Two consequences are referred, not resolved
here:** honeycomb adds pressure drop that HV1 did not allow for, and the enclosure's equipment
heat goes into bay 3, which HV1 sized on **occupancy**. The load is `[N]` until an equipment
schedule exists.

**PoE-3 quotes no residual figure on purpose.** MIL-STD-188-125-1 specifies PCI performance **by
pulse test**, and the project's register carries the section number only. **Inventing a number
would be worse than `[N]`.**

**PoE-4 is the bargain of this package.** Fibre with no metallic member is not a penetration at
all. **It is the one place this project can buy perfect performance for almost nothing, and it
should take it.** `[D]`

---

## 5  Bonding and earthing

Full schedule in `Schedules/BONDING_AND_EARTHING_SCHEDULE.md`.

### Bonding is where EMP design actually lives

`L = 2×10⁻⁷·l·[ln(2l/(w+t)) + 0.5 + 0.2235(w+t)/l]` H

| Strap | L | X @ 1 MHz | X @ 10 MHz | **X @ 100 MHz** |
|---|---|---|---|---|
| 600 mm × 25 × 3 | 512.2 nH | 3.22 Ω | 32.2 Ω | **321.8 Ω** |
| **100 mm × 50 × 3** | **38.9 nH** | 0.24 Ω | 2.45 Ω | **24.5 Ω** |

**A 600 mm strap is 322 Ω at 100 MHz. That is not a bond. It is a resistor with a nice green
sleeve on it.** Shortening it to 100 mm and widening it to 50 takes the inductance from 512 nH to
39 nH — a factor of **13.2**.

**The rules that follow, and they are the ones that get built wrong** `[D]`:

1. **Every bond ≤ 100 mm long.**
2. **Width : length at least 5 : 1.**
3. **Flat strap only.** Never a round wire, never a pigtail, never *"loop it round to the
   nearest stud."*
4. **Clean bare metal both ends**, protected after making off.
5. **The shield bonds to the structure at ONE place.** A second bond is a loop, and a loop is an
   antenna.

### Earthing — and why 5 Ω is the wrong target to chase

| Electrode | ρ = 1 000 Ω·m | ρ = 10 000 Ω·m |
|---|---|---|
| One 3 m × 16 mm rod | **335 Ω** | **3 349 Ω** |
| Rods for 5 Ω, *ignoring interaction* | **67** | **670** |
| **The structure itself** — 136.4 m², r_eq 6.589 m, ρ/4r | **38 Ω** | **379 Ω** |

Deccan basalt is **1 000 – 10 000 Ω·m** `[C]` K.3, which already says *"test earth resistance
early."* **≤ 5 Ω is not achievable with rods.** Rods interact, a real group needs substantially
more than the ideal count, and there is nowhere on this site to put them.

**The mat and its cage are already a large concrete-encased electrode** — an order of magnitude
better than a rod, and costing nothing because it is already built. **Bond to the structure; do
not chase rods.** `[D]`

> **And ≤ 5 Ω is not an EMP number.** It is a power-safety and lightning requirement from
> IS 3043 / IEEE 142 `[C]`. It is real and it still applies. **It is not what makes an EMP shield
> work.** An EMP shield works by being **equipotential**, and equipotential is decided by
> **bonding inductance**, not by earth resistance. **EM-F5.**

---

## 6  Verification

**IEEE Std 299** is in the register `[C]` for a shielding effectiveness survey. Applied here:

**EMP ZONE 2 — SURVEY IT.** Full IEEE 299 survey, 10 kHz – 1 GHz, on the completed enclosure
with every penetration made off and every panel closed. Acceptance **80 dB**. **This is a HOLD
POINT: no equipment is installed before it passes**, because a failed survey means opening
seams.

**EMP ZONE 1 — DO NOT SURVEY IT, AND DO NOT CLAIM IT.** A buried box under 2 m of engineered
cover cannot be surveyed to IEEE 299 — there is no accessible exterior to put a transmitter on.
Section 0 is a calculation and it will stay a calculation. **Any statement that the box gives
80 dB is unsupportable and should not be made.** `[D]`

**What *can* be checked on site, cheaply, at the only moment it can be fixed:**

- **Continuity of the cage across every construction joint, before the pour.** Master F.1
  already requires the welded Cu/galvanised EMP strap `[C]`. **Measure it.**
- **Continuity of every cast-in frame to the cage, before the pour.**
- **Earth resistance, early**, as K.3 already demands `[C]`.
- **Bond resistance at every strap after making off.**

None of these prove shielding effectiveness. **All of them catch the mistakes that destroy it.**

---

## 7  Findings

| | |
|---|---|
| **EM-F1** | **The stair void is a 2 800 × 3 160 (8.85 m²) aperture that never reaches 80 dB anywhere in the band and is open above 47.4 MHz.** It opens into the headhouse (+0.900, **no earth cover**) and thence to grade. **The entry route is an open electromagnetic path from grade to bay 7**, and Blast Door 1 is the only thing across it — **its RF performance is vendor data the project does not have.** |
| **EM-F2** | **The reinforcement cage meets 80 dB over one decade of the five required, and gives 0.00 dB at 1 GHz.** This *reproduces* master K.3's own confirmed figure from the 150 mm bar spacing. The cage is a genuine low-frequency measure and **must not be described as a MIL-STD-188-125-1 boundary.** |
| **EM-F3** | **"EMP Zone 2" has been named since Rev F with no Zone 1 and no Zone 0 ever defined, and no specification for the enclosure itself** — finishes `W-04` carries it as `[C]` requirement / `[N]` specification. Four revisions, no shield. |
| **EM-F4** | **BV-4 and BV-5 (DN350) are the only penetrations failing both criteria** — cutoff 502 MHz and 54.8 dB. Behind them sits a question nobody has answered: **is bay 8 inside the EMP boundary?** No EMP boundary has ever been drawn. |
| **EM-F5** | **The ≤ 5 Ω earthing target is not achievable with rods in Deccan basalt** (335 Ω per rod at the *low* resistivity bound) **and is not an EMP requirement in any case.** The structure is already the better electrode. |
| **EM-F6** | **There is no antenna, mast, feeder or communications design anywhere in this project.** MIL-STD-188-125-1 §5.7.6 is in the register with nothing to apply it to. **An ops room that cannot transmit is an ops room in name only**, and an antenna is by definition a deliberate conductor from outside to inside — the hardest EMP penetration there is. |

---

## 8  Open items — EM-V1 to EM-V6

**Six open items were raised and none was resolved by this package. That was deliberate** — a package that quietly filled them in would be inventing a specification. **One, EM-V1, has since been ruled by the project owner (RC2, 11 September 2026). Five stand.**

| | | Whose decision |
|---|---|---|
| **EM-V1** | ~~Adopt or reject the three-zone EMP model and the "Zone 2 standing alone" design rule (§2).~~ **RULED — ADOPTED by the project owner, RC2, 11 September 2026 (master H.21). CLOSED.** Everything else in this package followed from it and is unchanged | **Closed** |
| **EM-V2** | **Every EMP Zone 2 dimension is `[A]`** pending an equipment schedule. **ADVANCED by EL1, 11 Sep 2026 (master H.20): `Z-01` gives a 1.50 kW ops/comms ALLOWANCE and a `DB-Z2` sub-board fed through the PoE-3 PCI**, so the enclosure now has a basis instead of nothing. **It is still an allowance, not a schedule, so this item stays open** | Waits on an equipment schedule — **EL-V3** |
| **EM-V3** | **Is bay 8 inside the EMP boundary?** Decides whether BV-4/BV-5 need honeycomb, and whether the 15 kVA generator survives the pulse. **SHARPENED by RC2, 11 September 2026: the generator may run in Mode 3, so BV-4 and BV-5 are reopened after the shock and the two bores that fail both EMP criteria are open through the post-attack period.** Still open | Client / military |
| **EM-V4** | **No communications design of any kind exists.** §5.7.6 cannot be applied, and the ops room's purpose is unmet | Client / military |
| **EM-V5** | **PD-05's pipe material is unspecified** — as is every pipe material in the project. Metallic and plastic need completely different treatments at the entry plate | Drainage / engineer |
| **EM-V6** | **No escape-shaft head hatch is specified, and no blast door RF data exists.** Both sit directly on the boundary | Vendor data required |

**These six add to, and do not disturb, the six items already open in master K.1b** (U2, U3, U8,
WM-V6, WM-V7, WM-V9) and the four CAM-V and six FS-V items. **Nothing in this package resolves,
downgrades or deletes any existing `[ASSUMED]`, `[UNRESOLVED]` or `[NOT AVAILABLE]` tag.**

---

## 9  What this package could not do

| | |
|---|---|
| **`[N]` Equipment** | No equipment schedule, because no electrical design exists. Zone 2's size, heat load, power and signal count are all unknown |
| **`[N]` Threat** | No incident field, waveform or E1/E2/E3 decomposition. **U2** and **U3** are open in K.1b. Designed against the **80 dB performance requirement** instead, which needs none of them |
| **`[N]` Communications** | No antenna, mast, feeder or comms design |
| **`[N]` Vendor data** | No shielded door, PCI, honeycomb, blast valve or blast door RF data |
| **`[N]` Materials** | No pipe material anywhere in the project; no concrete permittivity or conductivity; no statement anywhere of whether rebar crossings are **tied or welded** — which materially changes §0 |
| **`[U]` Boundary** | ~~§2 proposes a boundary; only the client can adopt it.~~ **§2's zone model is now ADOPTED (RC2).** But **whether bay 8 is inside the EMP boundary is still undecided — EM-V3** — and **RC2's other ruling sharpens it**: the generator may run in Mode 3, so **BV-4 and BV-5 reopen after the shock, leaving two DN350 bores open in the post-attack period** — the two that fail both EMP criteria |
| **Excluded** | **The sentry post**, consistent with every other services package. It is above ground, framed, brick-infilled and not blast designed. **Its EMP exposure is total and nothing here changes that** |

**Every cage figure in this package is an upper bound.** The classical `−10 log₁₀(n)` array
correction is not applied, the crossings are tied rather than welded, and no concrete absorption
is credited. **A measured cage will be worse than section 0.**

---

## 10  Codes

**Only the EMP entries already in master Part G are used. No clause not in that register is
cited, and none is invented.**

| Code | Used for | Sections relied on |
|---|---|---|
| **MIL-STD-188-125-1** | EMP | §5.4 access · §5.5 waveguide below cutoff · §5.7.2.1 power PCI · §5.7.4.1 fibre · §5.7.6 RF · **80 dB, 10 kHz – 1 GHz** |
| **IEEE Std 299** | EMP verification | Shielding effectiveness survey |
| **IEEE 142 / IS 3043** | Earthing | ≤ 5 Ω target |
| **IS 456:2000** | Bar spacing | Cl. 26.3.3 — **the project's 150 mm cap is stricter** |

---

## 11  Coordination with the other packages

| Package | Interface | Status |
|---|---|---|
| **Structural (SC1 / master A.5, F.1)** | 150 bar spacing · cast-in frames welded to the cage · welded EMP strap at every construction joint · no movement joints in the envelope | **All already correct.** This package changes nothing and adds the reason |
| **HVAC (HV1)** | Five blast valves. BV-1/2/3 need **no treatment**. BV-4/5 need honeycomb **if bay 8 is in** — **referred, EM-V3**. Honeycomb pressure drop and Zone 2 heat load **referred, not resolved** | **Referred** |
| **Drainage (DR1)** | PD-05 through the service entry plate. **Pipe material `[N]` — EM-V5** | **Referred** |
| **Finishes (FN1)** | `W-04` *"EMP Zone 2 shielded enclosure lining"* was raised as `[C]` requirement / `[N]` specification. **This package supplies the `[A]` specification it was waiting for** | **Answered, at `[A]`** |
| **Works Management (WM3)** | **No EMP bill item, quantity, rate, date or float is created or changed by this package.** The 25.28 m² enclosure area is stated for information only | **No change** |
| **Electrical (EL1)** | **EL1 supplies the load allowance EM-V2 was waiting for** (`Z-01`, 1.50 kW), the `DB-Z2` sub-board inside the enclosure, and the single cable entry that uses **PoE-3 (PCI on power)** and **PoE-4 (fibre on signal)**. EL1 also **adopts EM-F5's earthing ruling unchanged** — bond to the structure, do not chase rods | **Answered at `[A]`** |
| **Site and Concealment (CAM2)** | An antenna, if one is ever designed, is both an EMP penetration and a **concealment** signature. **And CAM2's new `CAM-V5` — the unrecorded head level of the generator air shaft SH-2 — is the same shaft that carries BV-4 / BV-5**, the two bores that fail both EMP criteria. **One shaft, two open questions: how tall is it (CAM-V5) and is it inside the EMP boundary (EM-V3)** | **Noted, EM-V4 · new link to CAM-V5** |
| **Fire and Life Safety (FS2)** | FS-5 records that every active fire measure waits on the missing electrical design. **EM-V2 waits on the same gap.** **And FS2's new `FS-V7` — how either escape shaft is actually climbed — lands on the same two shaft heads as `EM-V6`**, which asks what conducting hatch closes them. **Whatever is fitted at those heads has to satisfy both: climbable from below, and bonded** | **Same root cause · new link to FS-V7** |

---

*EMP Protection package revision EM1 · 10 September 2026 · FOR REVIEW — NOT FOR CONSTRUCTION*
*Sentry post excluded · Main staircase unchanged · No design value altered*
