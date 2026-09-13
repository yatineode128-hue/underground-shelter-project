<!-- MASTER PROJECT REPORT -- source.  Rendered to PDF by Scripts/report_render.py.
     Underground CBRN-hardened blast-resistant protective structure + sentry post, Pune.
     Project Report package, revision PR1, 13 September 2026.
     AUTHORITY: master/MASTER_PROJECT_STATE.md.  Where this file and the master
     disagree, the master governs.  Edit this file and re-run the renderer;
     never edit the PDF. -->
<!-- COVER -->
<!-- TOC -->

# PART 1 — THE PROJECT AND THIS DOCUMENT

## 1.1 What this report is

This is the **master project report** for a buried reinforced-concrete protective structure at
Pune, Maharashtra, and for the separate sentry post that watches its approach. It states the
project once, in the order an engineer would need it to reproduce the design: the physics first,
then the ground, then the loads, then the calculations, then what is drawn, then what is still
open.

It is written to stand on its own. Everything needed to follow an element from a first-principles
load to a bar mark on a drawing is in here, with the clause of the Indian Standard that permits
each step named beside it.

**It is a statement of the design, not a history of it.** The revision history is summarised in
Appendix D and held in full in the master; this report gives the current position and says how it
was reached only where the reasoning is part of the design.

## 1.2 Authority, and what governs what

| Document | Role |
|---|---|
| `master/MASTER_PROJECT_STATE.md` | **The single source of truth.** Parts A, B, F and L are the authoritative current design. **Where this report and the master disagree, the master governs** |
| `master/QUICK_STATE.md` | Orientation digest only. **Not an authority** |
| **This report** | The project stated once, in full, for reading — design basis, science, calculations, services, works management, open items |
| Discipline packages | `Structural CAD/` · `Drainage/` · `HVAC/` · `Electrical/` · `EMP Protection/` · `Fire and Life Safety/` · `Schedule of Finishes/` · `Site Selection and Geotechnical/` · `Site and Concealment/` · `WORKS MANAGEMENT/` · `Owner Rulings RC4/` · `DRAWING QAQC/` |
| Drawings | 80 DXF. The ten Rev F architectural files are **source**, not build artefacts; the discipline sheets are generated and must be regenerated, never hand-edited |

> **This report changes no design value.** No dimension, level, load, thickness, bar, quantity,
> rate, date or float is altered by it, no `.std` file is touched, and **no evidence tag is
> converted, downgraded or deleted.** Where the project does not hold a number, this report says
> so in the same sentence rather than filling it in.

## 1.3 Evidence classes — and why they are the point of the document

Every value in this project carries a class. They are the master's own and they are used here
unchanged. A reader who ignores them will read an assumption as a measurement, which is the one
mistake this document set exists to prevent.

| Tag | Meaning | How to treat it |
|---|---|---|
| **`[C]` CONFIRMED** | Read directly from a project file, or computed in the project from confirmed inputs | Use as fact |
| **`[R]` RECONSTRUCTED** | Derived by back-calculation from partial evidence | Use, but state the derivation when relying on it |
| **`[A]` ASSUMED** | An engineering assumption. No test, no client confirmation | **Must be re-confirmed before construction** |
| **`[U]` UNRESOLVED** | Two or more conflicting values and insufficient evidence to choose | **Do not guess** |
| **`[N]` NOT AVAILABLE** | The information does not exist in any project material | **Do not invent** |

**The register is not decoration.** Seven assumptions remain open (Part 18.2) and **every one of
them is a physical test on this plot** — a borehole, a piezometer, a plate load test, a
percolation test, a packer test. Eighteen open items remain (Part 18.3), and **four of them are
the ones a reviewer should look at first**: an investigation that reached about 1.5 m against a
formation at (−)6.800; two 1 400 mm holes in the protective boundary whose bonding is still
undesigned; a CBRN shelter that cannot state which way a release drifts; and a sealed box with a
4 kW heat surplus and an unmodelled rejection path.

## 1.4 Project identity

| Field | Value | Class |
|---|---|---|
| Project title | Underground CBRN-hardened, blast-resistant protective structure with associated sentry post | `[C]` |
| Location | Pune, Maharashtra, India — CTW / College of Military Engineering campus | `[C]` |
| Project type | Buried reinforced-concrete protective structure, military-operational, **for actual construction** | `[C]` |
| Academic context | B.E. Civil Engineering, final semester, three-presentation capstone | `[C]` |
| Objective | Protect **9 occupants for 96 h** against a nuclear air-blast design basis threat, with CBRN, EMP and fallout hardening | `[C]` |
| Architectural revision | **Rev F** — the ten uploaded DXF files | `[C]` |
| Design report revision | **Rev D** — older than the drawings; the largest historical reconciliation issue, now closed (Part 18.4) | `[C]` |
| Structural revision | **Phase 2 Rev A**, incorporating **Modification M1** | `[C]` |
| Presentation status | P1 delivered. **P2 (AutoCAD + STAAD + manual calculations) is the active deliverable.** P3 not yet scoped | `[C]` |
| Software | STAAD.Pro (Bentley), AutoCAD/DXF, plus a purpose-built dependency-free Python DXF toolchain | `[C]` |

## 1.5 The three structures, and they are deliberately not equal

| # | Structure | Status |
|---|---|---|
| **1** | **Main underground box** — 8 bays, 22.0 × 6.2 m external, roof 2.0 m below grade | **Blast designed.** This is the protected volume |
| **2** | **Entry headhouse and covered approach stairwell** — above-ground bermed RC, sitting on the shelter roof and on adjacent fill | Headhouse **blast designed**; the stairwell is **NOT**, and is **declared expendable** |
| **3** | **Sentry post** — two-storey RC framed building, **≥ 10 m clear** of the shelter excavation, on its own footings on in-situ rock | **NOT blast designed.** A recorded decision, not an omission — Part 11.1 |

### 1.5.1 The protective boundary — the single most important idea in the design

> **The protective boundary is Blast Doors 1 and 2 at level (−)6.100, together with walls W6 and
> W7, the perimeter walls, the mat and the pressure slab.**
>
> **Everything above the blast doors — the stair shaft, the headhouse, the entry stairwell — is
> OUTSIDE it.** That is deliberate. The stair shaft is open to atmosphere through the roof void,
> and the design accepts that it fills with blast pressure rather than pretending it does not.
> That single admission is what produced **Finding F1** and **Modification M1** (Part 9.2), and
> it is the reason W6 and W7 are 400 mm thick instead of 200.

**Gas-tight envelope = Bays 1 to 6 only** — **67.80 m² floor, 216.96 m³** (stated on the issued
sheet as 67.8 / 217.0) `[C]`. Bay 7 (stair shaft) and Bay 8 (generator) are **outside** it; Bay 8
is the "grey zone".

> **The project holds TWO protective boundaries and they do not coincide.** The gas-tight
> boundary is bays 1–6. The **EMP boundary is bays 1–8** — ruled by the project owner at RC4,
> because otherwise the 15 kVA generator, its control panel and every cable in bay 8 would be
> unprotected against the pulse. **Only one of the two has ever been drawn.** Part 14.4.

### 1.5.2 Access and egress

| Route | Path |
|---|---|
| **Primary** | Grade → covered entry stairwell, **12R @ 166.667 / 300** → platform (−)2.000 → inner security door → headhouse → stair void → **main dog-leg stair, 24R @ 170.8333 / 280, 3 flights × 8** → arrival landing (−)6.100 → **Blast Door 1**, 1200 × 2100, ≥ 7 bar → Bay 6 |
| **Secondary** | **Blast Door 2**, 1200 × 2100, from the stair shaft into Bay 8 (generator / grey zone) |
| **Emergency** | Two 1 400 mm dia vertical escape shafts, **ESC 1** (Bay 1) and **ESC 2** (Bay 8), 250 mm RC collars, heads at +0.150 and +0.700 |

**R1, the main stair, is the only route that does not require climbing a shaft, and the only one
usable by an injured or unconscious person.** ESC 1 and ESC 2 are **6.250 m** and **6.800 m**
vertical climbs (Part 14.5).

## 1.6 The mission, in numbers

| | Value | Class |
|---|---|---|
| Occupancy | **9 persons** | `[C]` |
| Endurance | **96 hours** | `[C]` |
| Gas-tight floor area / volume | **67.80 m² / 216.96 m³** | `[C]` |
| Gross internal volume, bays 1–8 | 20.800 × 5.000 × 3.200 = **332.8 m³** | `[C]` |
| Design ventilation flow | **300 m³/h**, 2 × 300 trains, true N+1 | `[C]` |
| Air changes on the gross volume | **≈ 0.9 per hour** | `[R]` |
| Closed-mode CO₂ limit without scrubbing | **9.9 h** to 1.0 % | `[C]` |
| Closed-mode limit on the soda-lime store | **48 h** | `[C]` |
| Oxygen store | 2 × 50 L at 150 bar = 15 m³ = **80 h** at 4.5 m³/day | `[C]` |
| Standby power | **15 kVA** generator, bay 8; connected load **7.360 kVA = 49 %** | `[C]` / `[R]` |
| Battery autonomy, essential loads | **4 h**, 149 Ah at 48 V | `[C]` by ruling |
| Potable water | **1 000 L** tank, bay 1 = 27.8 L/person/day. **Not firefighting water** | `[C]` |

## 1.7 Working rules this project is held to

These are not general good practice — they are the specific disciplines this project adopted, and
several of them exist because something once went wrong.

1. **The master governs.** A digest is never an authority.
2. **Inspect native files before modifying them.** Parse the DXF; read the `.std`. Never edit from
   memory or from a summary.
3. **Never guess or silently resolve** an `[UNRESOLVED]`, `[ASSUMED]` or `[NOT AVAILABLE]` item.
   Do not convert one into a confirmed fact, and do not delete or downgrade a tag.
4. **Do not fabricate missing generator scripts or unavailable output drawings.**
5. **Distinguish file reconciliation from analysis.** STAAD.Pro is not available in this
   environment. **Editing and verifying a `.std` file is not running an analysis** and must never
   be reported as one.
6. **No drawing shows an arrangement that differs from a calculation.** If the steel changes, the
   drawing changes in the same turn.
7. **Every significant change gets a revision identifier** and is recorded; **no revision is
   overwritten without preserving it.**
8. **A new drawing package registers itself with the QA tool.** Twelve sheets were invisible to
   the drawing index for four revisions because this was not done (Part 13.3).
9. **A change that stops at "reinforcement" and never reaches "drawings" is not finished.**

### 1.7.1 Frozen geometry

> **The main staircase is frozen: 24 risers, 170.8333 mm riser, 280 mm tread, 3 flights × 8,
> total rise 4 100 mm.** The landing levels, the 1 200 flight widths, the 200 mm well and the
> 2 533 mm headroom go with it. **Nothing in this report changes any of it**, and no service,
> duct, pipe, drain or diffuser is placed in the flights, the well or the landings.

## 1.8 How this report is arranged

| Part | Contents |
|---|---|
| **1** | The project, the authority, the evidence classes, the rules |
| **2** | **The engineering science behind the design** — blast physics, structural dynamics, radiation attenuation, buoyancy, earth pressure, filtration, EMP coupling, seismic response |
| **3** | Codes and standards, clause by clause |
| **4** | Site selection and geotechnics |
| **5** | Geometry and configuration — the complete dimensional register |
| **6** | Materials, durability, cover, development and lap lengths |
| **7** | Loading — every load derived and every combination stated |
| **8** | Analysis models — what they are, what they prove, what they cannot |
| **9–11** | **Structural design calculations**, element by element: the box; the stairs, headhouse and appurtenances; the sentry post |
| **12** | Reinforcement register and quantities |
| **13** | Drawings and drawing quality |
| **14** | Services — HVAC and CBRN, drainage, electrical, EMP, fire |
| **15** | Site layout, external works, finishes and concealment |
| **16** | Works management — bill, cost, programme, procurement, QA/QC, risk |
| **17** | **What this design does not demonstrate** |
| **18** | Assumptions, open items and owner rulings |
| **19** | The verification performed for this report |
| **A–D** | Notation · IS clause index · reproducing the project · revision history |

# PART 2 — THE ENGINEERING SCIENCE BEHIND THE DESIGN

> **What this part is.** The design decisions in Parts 6 to 11 are only defensible if the physics
> underneath them is understood. This part sets out that physics: where the loads come from, why
> the code rules take the form they do, and which physical effect each dimension was bought for.
>
> **It introduces no project value.** Every number quoted here is carried from the project's own
> register and is cross-referenced to the Part where it is used. Where the physics would allow a
> quantity the project does not hold — a weapon yield, an ambient design temperature, a soil
> modulus — **the gap is named, not filled.**

## 2.1 The blast wave

### 2.1.1 What a shock front is

An explosion releases energy in a time far shorter than the time the surrounding air needs to move
out of the way. The air is compressed faster than an acoustic wave can carry the information
away, so the disturbance steepens into a **shock front**: a near-discontinuity across which
pressure, density, temperature and particle velocity all jump.

Across that front, conservation of mass, momentum and energy give the **Rankine–Hugoniot**
relations. For a strong shock in air the two consequences that matter to a structural engineer
are:

```
STATIC OVERPRESSURE  p_so   the rise in ambient pressure at the front.
                            It acts EQUALLY IN ALL DIRECTIONS, like any
                            pressure.  A buried roof, a buried wall and a
                            free-standing wall all feel it.

DYNAMIC PRESSURE     q      the kinetic pressure of the air actually moving
                            behind the front,  q = 0.5 rho u^2.
                            It acts ONLY in the direction of flow, and it is
                            what produces DRAG on an obstacle standing in it.
```

**They are different loads with different physics, and the design uses both.** The roof and walls
of the buried box are loaded by `p_so`; the drag term `q` is what the older Rev D calculation used
for the bermed headhouse walls before this project raised them to the full envelope (Part 7.5).

### 2.1.2 Reflection, and why the reflected pressure is not simply doubled

When a shock meets a rigid surface head-on, the air behind the front is brought to rest and its
momentum is converted into further compression. For a weak (acoustic) wave the reflected
pressure would be exactly twice the incident. For a strong shock in a gas that can be heated and
partially dissociated, the reflection coefficient rises well above 2 — for the design basis threat
of this project it is close to **4**:

```
p_so = 344.7 kPa (50 psi)          incident static overpressure      [C]
p_r  = 1366 kPa                    reflected pressure                [C]
q    = 282 kPa                     dynamic pressure                  [C]

reflection coefficient  p_r / p_so = 1366 / 344.7 = 3.96
```

That reflected value is not used on the buried box — a buried surface is not a free-standing
reflecting face — but it **is** the number that decides the sentry post. Part 11.1 computes the
reflected force on the sentry post's 4.0 × 6.7 m face as **36 600 kN, about 3 730 tonnes**, and
that single figure is why hardening it was rejected rather than attempted.

### 2.1.3 Positive phase duration and impulse

Behind the front, pressure decays back to ambient over the **positive phase duration** `t_d`, then
falls below ambient into a **negative phase** in which the flow reverses. The area under the
pressure–time curve is the **impulse**, and for short loading it is impulse rather than peak
pressure that damages a structure.

```
t_d = 0.13 to 1.33 s        the design basis positive phase duration  [C]
```

> **The yield behind those numbers is deliberately not stated.** `p_so` = 344.7 kPa and
> `t_d` = 0.13–1.33 s **are** the design inputs, and every load case in this project uses them.
> The weapon yield that would produce them is **`[N]`** and was **ruled to stay unstated rather
> than invented** — owner ruling 6, RC4 (Part 18.4). Nothing in the design requires it. The one
> thing it would change is the prompt-radiation cover depth, and that is said openly in 2.4.
>
> **The negative phase is also not designed for as a separate load case**, and that is recorded in
> Part 17. Where it matters it has been allowed for physically rather than numerically: the
> escape-shaft head hatches take **quarter-turn dogs so the leaf resists uplift as well as
> downward pressure**, because the negative phase and the rebound both lift it (Part 10.5).

### 2.1.4 Why a buried roof takes the full overpressure

A metre of soil is not a shield against overpressure. The wave in the air couples into the ground
and propagates as a stress wave; the soil is a medium that **transmits** pressure, it does not
absorb it in the way intuition suggests. Codified practice handles this with a **soil transmission
factor** `K_a` applied to the free-field overpressure:

```
design surface pressure on a buried element  =  K_a x p_so
IS 4991 Cl. 7.2 and Table 3
```

For **saturated** soil, `K_a = 1.0` — water is nearly incompressible and transmits the pressure
essentially undiminished. This project's founding horizon is permanently below the design water
table, and the governing case is therefore the saturated one:

| | Value | Class |
|---|---|---|
| `K_a`, saturated | **1.0** | `[C]` IS 4991 Cl. 7.2 / Table 3 |
| `K_a`, dry compacted berm fill | ≈ 0.5 | `[A]` — **deliberately not relied on** |

> **The single most consequential choice in the loading.** Because `K_a` = 1.0, **2.0 m of
> engineered cover buys no reduction in blast pressure at all.** The roof of the buried box is
> designed for the same 383 kPa a bare roof would take. Every metre of that cover was bought for
> something else — radiation attenuation — and 2.5 names the price.
>
> The same logic was applied to the headhouse walls, which stand behind ~2.5 m of berm. The
> earlier calculation credited the berm and used the drag pressure, 113 kPa. **Since `K_a` for a
> dry berm cannot be verified, this project designs those walls for the full 383 kPa envelope**
> (conflict C10, Part 7.5). The cost of that decision is one link cage; the utilisation goes from
> 17 % to 59 %.

## 2.2 From a pressure history to a design load: structural dynamics

### 2.2.1 The single-degree-of-freedom idealisation

A blast-loaded slab is a distributed system, but its response is dominated by its first mode. The
standard idealisation replaces it with a single-degree-of-freedom (SDOF) oscillator of equivalent
mass and stiffness carrying a time-varying force. The response then depends on **one ratio**: the
load duration to the natural period, `t_d / T`.

```
t_d / T  <  ~0.1      IMPULSIVE      the load is over before the structure
                                     has moved.  Only the IMPULSE matters.
~0.1 to ~10           DYNAMIC        genuine transient interaction; the full
                                     SDOF solution is needed.
t_d / T  >  ~10       QUASI-STATIC   the structure completes many cycles while
                                     the load is still applied.  The peak
                                     response approaches that of a step load.
```

### 2.2.2 Which regime this structure is in — and the calculation that settles it

The governing element is the 900 mm pressure slab spanning 5.0 m clear. Its fundamental frequency
is computed in Part 9.4 from the cracked flexural stiffness and the participating mass, including
a share of the soil cover:

```
m   = 0.900 x 2500 + 0.25 x 2.0 x 2000                  = 3250 kg/m2
0.5 EIg = 0.5 x 2.958e10 x 0.900^3 / 12                 = 8.985e8 N.m2/m
f1  = (22.373 / 2.pi) . sqrt( EI / (m . Ln^4) )         = 74.9 Hz
T   = 1 / f1                                            = 13.4 ms
t_d / T = 130 ms / 13.4 ms  to  1330 ms / 13.4 ms       = 10 to 100
```

> **`t_d / T` = 10 to 100 places this structure firmly in the QUASI-STATIC regime.** That is the
> single most important dynamic result in the project, and it is what makes a static analysis with
> a dynamic load factor an honest way to obtain the demand. It is not an approximation of
> convenience — it follows from a thick slab on a short span being extremely stiff, and a nuclear
> air blast being a comparatively long-duration load.
>
> The coefficient **22.373** is the first eigenvalue constant for a uniform beam **fixed at both
> ends** (`βL` = 4.730, `βL`² = 22.373). Using the fixed-fixed value is consistent with
> the plastic mechanism adopted for strength in 2.2.4.

### 2.2.3 The dynamic load factor, and the ductility it is bought with

For a perfectly elastic SDOF system under a **step load**, the classical result is a dynamic
amplification of exactly **2.0**: the mass overshoots the static deflection by as much again
before the restoring force brings it back.

A structure that is allowed to yield does not have to store that energy elastically. Equating the
work done by the load to the energy absorbed by an elastic–plastic resistance function, and
defining the **ductility ratio** `μ` as the ratio of maximum to yield displacement, gives the
form codified in IS 4991 Cl. 10.3.3:

```
DLF  =  mu / (mu - 0.5)

VALIDATION       mu = 1 (no ductility at all) -> DLF = 1/0.5 = 2.00
                 which is exactly the elastic step-load factor.  The
                 expression reduces correctly at its own limit.

ADOPTED          mu = 5   "moderate, repairable damage"   IS 4991 Cl. 10.3.3
                 DLF = 5 / 4.5                                    = 1.111

DESIGN BLAST PRESSURE = 344.7 x 1.111                             = 383 kPa
```

> **A ductility ratio is a promise about detailing, not a discount.** Taking `μ` = 5 asserts that
> the section can reach five times its yield rotation without losing capacity. That promise is
> kept in two places in this project and both are checkable:
>
> **First, the neutral axis depth.** For the roof slab the design gives `x_u/d` = **0.139**
> against the Fe500 limit of 0.46 (IS 456 Cl. 38.1(f)). A section with a neutral axis at 14 % of
> the effective depth is very lightly reinforced in flexural terms, the steel strain at failure is
> large, and the section is unambiguously under-reinforced and ductile. **That number is the
> proof that `μ` = 5 is defensible**, and it is why it is printed next to the result in Part 9.4.
>
> **Second, the shear detailing.** Shear failure is brittle, and a brittle failure mode makes a
> ductility claim meaningless. Every blast-governed element in this project carries designed
> shear links even where nominal steel would satisfy IS 456, and the mat's link grid was added
> for exactly this reason (conflict C6, Part 9.3).
>
> **What is NOT demonstrated** is the support rotation that `μ` = 5 implies — θ ≤ 2° corresponds
> to δ ≤ 87 mm = span/57 and requires a **non-linear SDOF check** (IS 4991 Fig. 6, or Biggs).
> **That is Phase 3 work and it is not claimed here.** See Part 17.

### 2.2.4 Why the plastic hinge mechanism, and why `wL²/16`

Flexural design of the blast-governed elements uses the plastic mechanism moment for a
fixed–fixed one-way strip:

```
Mp = w . Ln^2 / 16
```

This is the collapse mechanism value, not the elastic value. An elastic fixed-fixed strip carries
`wL²/12` at the supports and `wL²/24` at midspan. Once the support sections yield, they rotate
at constant moment and the span redistributes until the midspan section also reaches its capacity;
setting external work equal to internal work for the three-hinge mechanism gives a required
capacity of `wL²/16` at every hinge, which is **less than the elastic peak of `wL²/12`**.

> **This is only legitimate because the section is ductile enough to redistribute** — the same
> promise `μ` = 5 makes. The two are one assumption, checked once, and used consistently: the
> mechanism supplies the demand and `x_u/d` = 0.139 supplies the licence.

### 2.2.5 Strain-rate effects: why 25 % is added, and where it is not

Concrete and reinforcing steel are both **rate-sensitive**. Loaded in milliseconds rather than
minutes, both show higher apparent strength — concrete because micro-crack growth is a
time-dependent process that cannot keep pace, steel because dislocation motion at the yield plateau
is similarly rate-limited. IS 4991 Cl. 10.3.1 codifies this as a flat 25 % increase for the blast
case only:

```
BLAST CASE ONLY                IS 4991 Cl. 10.3.1
    fck,dyn = 1.25 x 35 = 43.75 N/mm2
    fy,dyn  = 1.25 x 500 = 625 N/mm2

NO DYNAMIC INCREASE ON SHEAR   IS 4991 Cl. 10.3.1.1
    every tau_c in this project is read at the STATIC M35 value
BOND  the clause permits +25 % (Ld 40phi -> 32phi).  NOT TAKEN.
    all detailing uses the static 40phi
```

> **Two deliberate refusals, and both are conservative.**
>
> **Shear gets no bonus, by the code's own rule.** Diagonal tension failure is brittle and
> aggregate-interlock dependent, and the rate sensitivity of that mechanism is not the same as
> that of the compression block. The consequence is real and visible: the mat's one-way shear
> check, run at the static `τ_c` for the first time in this project, is what produced the
> requirement for a **T12 link grid at 250 × 250 throughout the mat** (conflict C6).
>
> **The 25 % bond bonus is available and is refused.** Every development and lap length in this
> project is the static value. A 25 % shorter anchorage is not worth the argument at a
> construction joint that also has to be watertight and electrically continuous.

### 2.2.6 Why γ = 1.0 on the blast combination

Blast appears in combination 103 with a load factor of **1.0**, not 1.5. That is not a relaxation:

> The blast case is an **extreme event** checked against **ultimate** capacity computed with
> **dynamic** material strengths. Applying a 1.5 partial factor to the load *while also* taking
> the 25 % material bonus would double-count the same conservatism from both ends. The project
> takes the material bonus and drops the load factor, states so, and does not mix the two.
>
> IS 4991 Cl. 11.1 forbids combining wind or earthquake with blast, and Cl. 11.2 forbids live load
> on the roof at the time of blast. Both exclusions are applied (Part 7.9).

## 2.3 Ground shock, soil–structure interaction and arching

A buried structure and the soil around it are one system. Three effects matter, and this project's
position on each is stated rather than assumed away:

**Transmitted overpressure.** Handled by `K_a` (2.1.4), taken at the saturated upper bound of 1.0.

**Arching.** A buried structure stiffer than the surrounding soil attracts load; one more flexible
sheds it to the soil either side. Real buried boxes usually benefit from **positive arching**,
which would reduce the roof pressure below the free-field value. **This project takes no arching
credit at all.** That is conservative and it is declared, because the credit depends on the
relative stiffness and on the compaction actually achieved, neither of which is measurable in
advance.

**Transient soil–structure interaction** — participating mass, interface pressure ratios, the
phasing between the ground shock arriving at the roof and at the walls — is **not demonstrated**
and is listed in Part 17 as such. A static analysis with an SDOF-derived load factor gives the
correct *demand*; it is not a transient interaction analysis and is never presented as one.

## 2.4 Nuclear radiation, and what 2.0 m of cover actually buys

### 2.4.1 Two different radiation problems

| | Prompt radiation | Fallout |
|---|---|---|
| What it is | Gamma rays and **neutrons** emitted during the detonation itself | Gamma emission from activated debris deposited afterwards |
| When | Seconds | Hours to days |
| Spectrum | Hard; neutrons are the hard part to stop | Softer gamma |
| What stops it | **Mass**, and for neutrons **hydrogen** | Mass |

### 2.4.2 Attenuation is exponential in mass, not in thickness

For a narrow beam through a uniform absorber, intensity falls as

```
I = I0 . exp( -mu . x )          mu = linear attenuation coefficient
                                 x  = thickness

More useful in shielding practice, the same law written with MASS per unit
area, because it is areal density that does the work:

I = I0 . exp( -(mu/rho) . rho.x )

TENTH VALUE LAYER  TVL = ln(10) / mu   -- the thickness that cuts the dose
                                          by a factor of 10.
```

The practical consequence for a buried shelter is that **what protects the occupants is the mass
above them, and it has to be above the slab.** The same tonnage placed against a wall does
nothing for the roof.

For neutrons the mechanism is different and it matters: fast neutrons are slowed most efficiently
by **elastic collision with nuclei of similar mass**, which means hydrogen. Moisture in soil and
the chemically bound water in concrete are genuinely useful; dense dry rock is less effective
per unit mass against neutrons than against gamma.

### 2.4.3 Why 2.0 m, and what each metre is for

| Requirement | Does it need cover? | Verdict |
|---|---|---|
| **Blast** | **No.** A buried roof takes the full `p_so` regardless of depth — IS 4991 Cl. 7.2, `K_a` = 1.0 | Cover buys **nothing** here |
| **Fallout** | 1.0 m already gives a protection factor of ≈ 2 200 against a requirement of ~1 000 `[C]` | The **first** metre covers it, twice over |
| **Prompt neutron and gamma** | Needs mass, above the slab | **This is what the second metre is for** |

> **Stated plainly: the second metre of cover is bought entirely for prompt neutron and gamma
> attenuation.** Reducing the cover from 4.0 m to 2.0 m in an earlier revision saved 2 m of rock
> excavation, 2 m of shaft, one stair flight and 2 m of headroom, and cost nothing in blast
> capacity because there was nothing to lose.
>
> **And the honest caveat.** The prompt-radiation requirement scales with the yield, which is
> `[N]` and deliberately so (2.1.3). **If the design basis threat is ever stated and is larger,
> the cover depth is the dimension that changes** — along with the burster slab. The project
> records this rather than pretending the depth is threat-independent.

### 2.4.4 The burster slab

The 200 mm M30 slab inside the cover, reinforced T12 @ 150 both ways, is not there to stop
anything. It is there to **break up a penetrating item** so that its energy is dispersed in the
500 mm of crushed basalt rubble below it rather than delivered to the roof as a point load.

> **It breaks up a penetrating item; it does not defeat one.** **No direct hit is designed for**,
> and that is now an explicit owner ruling (ruling 5, RC4): *the design stands as it is.* If a
> direct hit ever becomes a requirement, both the cover depth and the burster design change.

## 2.5 Groundwater, buoyancy and the compensated foundation

### 2.5.1 Archimedes, applied to a buried box

A structure below the water table displaces water and is pushed up by the weight of the water it
displaces. The uplift is the water pressure at the underside integrated over the plan area:

```
u    = gamma_w x h_w = 9.81 x 4.700                        = 46.11 kPa
A    = 22.000 x 6.200                                      = 136.40 m2
U    = 46.11 x 136.40                                      = 6289 kN
```

Two points are easy to get wrong and are got right here:

1. **The uplift acts on the real underside, not on a model's mid-surface area.** A plate model of
   the mat has its elements at mid-depth; using that area under-states the force.
2. **Spring supports in a linear analysis take tension.** In the elastic-foundation model the mat
   therefore **never lifts, whatever the load case.** Flotation cannot be demonstrated — or
   refuted — by that model. It is a hand check on real dimensions and real weights (Part 9.3).

> **Anyone who says "the analysis shows no uplift" has misunderstood their own model.**

### 2.5.2 Why the construction stage governs

Buoyancy competes with weight, and the weight arrives late. Before the roof is on and the cover
is placed, the box is a light, closed vessel in a wet hole:

| Stage | Weight | Uplift | FoS at GWT (−)2.000 |
|---|---|---|---|
| 1 — mat cast only | 2 009 kN | 6 175 kN | **0.33 FAIL** |
| 2 — mat + walls, no roof | 4 802 kN | 6 175 kN | **0.78 FAIL** |
| 3 — box complete, no backfill | 7 528 kN | 6 175 kN | **1.22 MARGINAL** |
| 4 — backfilled and covered | 12 453 kN | 6 175 kN | **2.02 OK** |

*(The absolute figures are at the pre-M1 21.600 m box; both uplift and resistance scale with
length, so every factor of safety is unchanged. The hand check uses the current 136.40 m² /
6 289 kN — Part 9.3.)*

> **Flotation, not bearing and not settlement, is the governing foundation problem** — and it
> governs during construction, not in service. That is why the mitigation in Part 9.3 is a
> **design output** with four mandatory items, not a note passed to the contractor.

### 2.5.3 The compensated foundation, and why "settlement negligible" is true

The excavation removes more ground than the structure puts back:

```
overburden removed, 1.13 m soil at 19.5 kN/m3            =  22.10 kPa
overburden removed, 5.67 m basalt at 25.0 kN/m3          = 141.67 kPa
TOTAL GROSS PRESSURE REMOVED AT FORMATION                = 163.77 kPa
replaced by, in service                                  =  58.40 kPa
NET CHANGE IN PRESSURE AT FORMATION                      = -105.37 kPa
```

> **In service the structure is lighter than the ground it replaces, by about 105 kPa.** It is a
> fully compensated foundation and then some. **This is the physical reason "settlement
> negligible" is true rather than merely hoped for** — and it is the same fact, seen from the
> other side, that makes flotation the governing case. One physical observation explains both
> conclusions.

### 2.5.4 Effective stress, and why water is two-thirds of the wall load

Below the water table, soil and water carry the lateral load separately. The soil skeleton
transmits its share through grain contacts at the **submerged** unit weight; the water transmits
its own hydrostatic pressure, in full, in every direction:

```
gamma' = gamma_sat - gamma_w = 21 - 9.81                   = 11.19 kN/m3
K0     = 1 - sin(phi)   (Jaky), phi ~ 30 deg               = 0.50
lateral gradient = K0.gamma' + gamma_w
                 = 0.50 x 11.19 + 9.81                     = 15.41 kPa/m
   of which  SOIL  = 5.60 kPa/m       WATER = 9.81 kPa/m
```

> **Water is 64 % of the lateral gradient and soil is 36 %.** That single split is why the design
> groundwater table is called the most important number in the project, and why the master tags it
> `[ASSUMED]` in bold. `K₀` uses **Jaky's** relation for a normally consolidated soil at rest —
> at-rest, not active, because a stiff buried box does not move enough to mobilise active
> pressure.

## 2.6 The modulus of subgrade reaction, and why both bounds must be run

A mat on ground is modelled as a plate on a **Winkler** foundation: a bed of independent springs of
stiffness `k_s` (kN/m³ — pressure per unit settlement). It is a crude idealisation — real soil
couples adjacent points, which springs do not — but it is the standard one, and its weakness is
specific and known:

> **`k_s` does not change the total load; it changes how the load is distributed.** A soft bed
> lets the mat dish and drives moment into the span. A stiff bed concentrates reaction under the
> stiff lines — walls, corners — and drives moment there instead. **The two bounds do not
> bracket a small error; they can put the peak moment in different places.**

| | Value | Class |
|---|---|---|
| `k_s` | **100 000 to 500 000 kN/m³** | `[A]` — **run the mat model at BOTH bounds** |

The project has built the upper-bound model (`Underground_Shelter_ks500000.std`, differing from
the reference model **only** in the subgrade line and the four corner `KFY` values, verified by
diff). **Neither bound has been run, because STAAD.Pro is not available in this environment.**
`k_s` remains `[ASSUMED]` at both bounds, and a plate load test is the only thing that closes it.

## 2.7 CBRN: keeping the outside outside

### 2.7.1 Overpressure is the primary barrier

A gas-tight envelope leaks. The defence is not perfect sealing but **positive pressure**: hold the
inside above ambient, and any leak flows outward.

| | Value | Class |
|---|---|---|
| Operating overpressure | **+50 to +100 Pa** | `[C]` |
| Leak-test pressure | **+300 Pa** | `[C]` |
| Permitted leakage | ≤ **0.15 vol/h** at +300 Pa = 32.5 m³/h = **11 %** of one train | `[C]` / `[R]` |
| Cascade, clean to dirty | **0 → +10 → +20 → +35 → +50 Pa** | `[C]` |

**The cascade maps exactly onto the three decon airlock stages**, which is what makes a
three-stage airlock work: at every door, air moves from cleaner to dirtier and never the reverse.

> **A consequence that is easy to miss: every water trap inside the envelope is a pressure
> boundary.** A seal shallower than the overpressure blows through and the shelter vents to the
> drain. Part 14.2 shows the sizing — 75 mm deep seals hold **736 Pa**, which is **7.4 : 1**
> against the operating pressure and **2.5 : 1** against the test. **And an unused gully
> evaporates dry**, after which it leaks air in both directions; priming is therefore a written
> maintenance task, not a nicety.

### 2.7.2 Filtration: three different physical problems

| Threat | Physical form | What removes it |
|---|---|---|
| Radioactive particulate, biological agents | Aerosol, ~0.1–10 μm | **HEPA**, EN 1822 class **H14**, ≥ 99.995 % at MPPS |
| Chemical warfare agents | **Vapour** | **Impregnated activated carbon** (ASZM-TEDA) |
| Coarse dust, the blast pulse | — | Pre-filter; blast valves |

> **A HEPA filter does not remove a vapour and a carbon bed does not remove a particle.** They are
> in series because they solve different problems. HEPA performance is quoted at the **most
> penetrating particle size**, which is *not* the smallest: below about 0.3 μm, diffusion capture
> improves as particles get smaller, while above it interception and impaction take over. The
> minimum in between is the number the standard quotes, which is why an H14 rating is a stronger
> statement than "99.995 % of dust".

**Carbon beds self-heat.** Adsorption is exothermic and a loaded bed is a genuine fire hazard in a
protected ventilation system — which is why the filter bay appears in Part 14.5's fire-load
schedule rather than being treated as inert plant.

### 2.7.3 Blast valves: protecting the filters from the shock

The filter train cannot take 383 kPa. **Blast valves** are fast-acting closures on each envelope
penetration that shut on the pressure rise itself and reopen afterwards. This project carries
**five**, all confirmed on the issued services sheet, recessed to IS 4991 Cl. 6.2.1, each with a
manual quarter-turn gas-tight damper inboard of it, and with a **hand crank on each filter fan** so
that ventilation does not depend on electrical power at all.

### 2.7.4 Closed mode: the arithmetic of a sealed box

With every valve shut there is no fresh air. Two consumables then run the clock:

```
CO2 ACCUMULATION
    allowable rise 0.04 % -> 1.0 %          = 0.0096 volume fraction
    occupied volume, airlock shut           = 184.96 m3
    9 occupants x 0.020 m3/h/person         = 0.18 m3/h of CO2
    time to 1.0 %  = 0.0096 x 184.96 / 0.18 = 9.9 h          [C]
    over 96 h closed                        = 17.28 m3 of CO2

OXYGEN
    2 x 50 L at 150 bar = 15 m3 at 4.5 m3/day = 80 h         [C]

SODA LIME (CO2 scrubbing)   40 kg store                = 48 h [C]
```

> **HV-F1 — the soda lime, not the oxygen, limits closed mode.** Unscrubbed CO₂ gives 9.9 h; the
> soda-lime store gives 48 h; the oxygen store gives 80 h. **The binding consumable is the one to
> count and the one to write on the drill card.** Closed mode covers 48 of the 96 h endurance —
> **the other 48 h require filtration.**
>
> **And the scrubber is therefore not optional.** Without it the envelope reaches 1.0 % CO₂ in
> 9.9 hours against a 96-hour design occupancy. That ratio is the whole argument. Owner ruling 25
> (RC7) sized the recirculation loop at **75 m³/h** — chosen at the worst cell of the efficiency /
> target matrix because designing to it costs almost nothing (Part 14.3).

### 2.7.5 The decon airlock, and the manning constraint hiding in it

The three-stage airlock has to be purged between users:

```
volume         5 x (2.0 x 2.0 x 3.2)           = 64 m3
purge at the design flow 300 m3/h              = 12.8 min   [R]
                                        -> 4-5 persons per hour
```

> **That is an operational constraint, not a ventilation figure.** Four to five people per hour is
> the maximum rate at which anyone can enter the shelter through a working decon procedure, and it
> belongs on the drill card. The master carries it as a confirmed item *requiring attention* for
> exactly that reason.

## 2.8 EMP: why concrete and rebar are not a shield

### 2.8.1 What HEMP is, and what it is not

A high-altitude nuclear detonation produces three distinct electromagnetic components:

| Component | Time scale | What it couples to |
|---|---|---|
| **E1** | nanoseconds, very fast rise | Short conductors — cables, boxes, PCBs. The component that destroys electronics |
| **E2** | microseconds to milliseconds | Similar to lightning; conventional surge protection is relevant |
| **E3** | seconds | Long conductors — power lines, pipelines. Quasi-DC induced currents |

> **HEMP is not a personnel hazard.** The occupants are protected from blast, CBRN and fallout by
> the box. **EMP protection exists so that the shelter can still function afterwards.** It
> protects equipment. That is why the answer is an enclosure and not a room, and why nobody should
> expect to shelter inside it.

### 2.8.2 The requirement, and the aperture arithmetic that defeats the concrete

```
REQUIREMENT   MIL-STD-188-125-1:  80 dB, 10 kHz to 1 GHz    [C]
              that is FIVE DECADES of frequency
```

A conducting screen pierced by a regular array of apertures behaves as a high-pass filter. For
apertures of pitch `s` the classical single-aperture estimate is

```
SE = 20 . log10( lambda / 2s )          lambda = c / f
```

Applied to this project's reinforcement cage, whose bar spacing is **150 mm both curtains both
ways** — itself an EMP requirement, stricter than IS 456 Cl. 26.3.3 needs:

| Frequency | SE of the cage |
|---|---|
| 10 kHz | **99.99 dB** |
| 100 kHz | 79.99 dB |
| 1 MHz | 59.99 dB |
| 100 MHz | 19.99 dB |
| **1 GHz** | **0.00 dB** |
| Mesh cutoff `c / 2s` | **999.31 MHz** |
| **Highest frequency meeting 80 dB** | **99.93 kHz** |
| **Fraction of the required band met** | **one decade of five — 20 %** |

> **And a coincidence worth saying out loud: 2s = 300 mm, and the wavelength at 1 GHz is
> 299.79 mm.** The cage stops shielding at almost exactly the frequency at which the standard
> stops asking. That is arithmetic, not design.
>
> **So the cage is a genuine low-frequency measure and must never be described as a
> MIL-STD-188-125-1 boundary.** It earns its keep where it can: E3, the slow component that drives
> long conductors, lives at the bottom of the band where the cage is strongest, and 99.99 dB at
> 10 kHz is not nothing.

**The second, independent reason** is simply the holes: a 900 mm slab with a **2 800 × 3 160
stair void** in it — 8.85 m² — is not a shield at any frequency, and neither are two 1 400 mm
escape shafts.

### 2.8.3 Waveguide below cutoff — the one place geometry works for you

A conducting tube of diameter `d` will not propagate below its TE11 cutoff:

```
f_c(TE11) = 1.8412 . c / (pi . d)

and BELOW cutoff the attenuation is roughly
     A = 32 . L / d   dB          (L = tube length, d = diameter)
```

A penetration bounded by metal and long relative to its bore is therefore a very effective
attenuator. This is why a small pipe through a thick wall is not a problem and a large one is:

| Penetration | Bore | Wall | Bounded by | Cutoff | WBC | Verdict |
|---|---|---|---|---|---|---|
| **BV-1 / BV-2** | 100 ⌀ | 600 | steel | 1 757 MHz | **192 dB** | **PASS** |
| **BV-3** | 100 ⌀ | 400 | steel | 1 757 MHz | **128 dB** | **PASS** |
| **BV-4 / BV-5** | **350 ⌀** | 600 | steel | **502 MHz** | **54.8 dB** | **FAIL, both criteria** |
| **PD-05** | 50 ⌀ | 600 | steel | 3 514 MHz | **384 dB** | **PASS** |
| **ESC 1 / ESC 2** | **1 400 ⌀** | 3 050 / 3 600 | **concrete** | **126 MHz** | **none** | **FAIL** |
| **Stair void** | **3 160** | 900 | **concrete** | **47.4 MHz** | **none** | **FAIL** |

> **Read the three-figure numbers correctly.** No practical penetration achieves 192 or 384 dB.
> Real assemblies flatten out around 100–120 dB and what limits them is **workmanship** — the bond
> at the frame, the gasket, the one sleeve nobody welded. A large number means *"the bore is not
> the problem here."*
>
> **A depth credit is taken only where the bore is bounded by metal.** Concrete is a lossy
> dielectric, not a waveguide wall. The escape shafts' 250 mm collars carry five T25 bars each
> side — five bars is not a conducting tube, so as built they earn nothing.
>
> **Lining a 1 400 mm shaft does not fix it**: above 125.5 MHz it propagates however it is lined.
> The treatment that works is a **bonded conducting hatch at the head**, which *terminates* the
> shaft instead of trying to attenuate down it.

### 2.8.4 Bonding inductance — where EMP design actually lives

A bond strap is not a resistor; at EMP frequencies it is an inductor, and its impedance rises
linearly with frequency:

```
L = 2e-7 . l . [ ln(2l / (w+t)) + 0.5 + 0.2235(w+t)/l ]   henries
X = 2.pi.f.L
```

| Strap | L | X at 1 MHz | X at 10 MHz | **X at 100 MHz** |
|---|---|---|---|---|
| 600 mm × 25 × 3 | 512.2 nH | 3.22 Ω | 32.2 Ω | **321.8 Ω** |
| **100 mm × 50 × 3** | **38.9 nH** | 0.24 Ω | 2.45 Ω | **24.5 Ω** |

> **A 600 mm strap is 322 Ω at 100 MHz. That is not a bond; it is a resistor with a nice green
> sleeve on it.** Shortening it to 100 mm and widening it to 50 mm takes the inductance from
> 512 nH to 39 nH — a factor of **13.2** — and it costs nothing.
>
> **The five rules that follow are the ones that get built wrong:** every bond ≤ 100 mm long;
> width-to-length at least 5 : 1; **flat strap only** — never a round wire, never a pigtail, never
> *"loop it round to the nearest stud"*; clean bare metal both ends, protected after making off;
> and **the shield bonds to the structure at ONE place**, because a second bond is a loop and a
> loop is an antenna.

### 2.8.5 Earthing — and why 5 Ω is the wrong target to chase

| Electrode | ρ = 1 000 Ω·m | ρ = 10 000 Ω·m |
|---|---|---|
| One 3 m × 16 mm rod | **335 Ω** | **3 349 Ω** |
| Rods needed for 5 Ω, *ignoring interaction* | 67 | 670 |
| **The structure itself** — 136.4 m², r_eq 6.589 m, ρ/4r | **38 Ω** | 379 Ω |

Deccan basalt is **1 000 – 10 000 Ω·m** `[C]`.

> **≤ 5 Ω is not achievable with rods here, and it is not an EMP number in any case.** It is a
> power-safety and lightning requirement from IS 3043 / IEEE 142; it is real and it still applies.
> **But an EMP shield works by being equipotential, and equipotential is decided by bonding
> inductance, not by earth resistance.** The mat and its cage are already a large
> concrete-encased electrode, an order of magnitude better than a rod and costing nothing because
> it is already built. **Bond to the structure; do not chase rods.**

## 2.9 Seismic response, and why a buried box is the easy case

Seismic design force follows from a design spectrum reduced by a response reduction factor:

```
Ah = (Z/2) . (I/R) . (Sa/g)                 IS 1893 (Pt 1) Cl. 6.4.2
Vb = Ah . W                                 Cl. 7.6.3
```

| | Underground box | Sentry post |
|---|---|---|
| Zone factor `Z` (Zone III) | 0.16 | 0.16 |
| Importance `I` | 1.5 | 1.5 |
| Response reduction `R` | **4.0** | **3.0** |
| `Sa/g` | 2.5 | 2.5 |
| **`A_h`** | **0.075** | **0.100** |
| Seismic weight `W` | 14 002 kN | 731.80 kN (model) |
| **Base shear `V_b`** | **1 050 kN** | **73.18 kN** |

**For the buried box, seismic is negligible and the calculation says so numerically**, not by
assertion: 525 kN per long wall gives `τ` = 0.063 N/mm², and IS 13920 Cl. 10.4 boundary elements
are checked and **not triggered**. A buried box moves with the ground; there is no tall,
flexible mass to excite.

**For the sentry post seismic governs over wind by 2.4 : 1** (73.18 kN against 29.9 kN), and the
choice of `R` = 3.0 is the conservative one:

> `R` = 3.0 is taken **because the infill panels are not positively separated from the frame.**
> `R` = 5.0 would require a special moment-resisting frame with separated infill, which this
> project does not claim. The consequence is quantified: `R` = 5.0 would give `A_h` = 0.060
> against 0.100, so the design base shear of **73.18 kN is about 1.67 × what a separated SMRF
> would need.** Owner ruling 21 (RC6) keeps `R` = 3.0 on exactly that basis.

## 2.10 Fire in a volume that cannot be ventilated

Every conventional fire strategy assumes smoke can be got out. **Here it cannot.**

| | |
|---|---|
| Internal volume | **332.8 m³** gross |
| Design air supply | **300 m³/h** |
| Air changes | **≈ 0.9 per hour** |
| Smoke extract | **NONE — and there cannot be one.** Every opening in the envelope is a blast valve or a blast door; a smoke vent would be a hole in the protective boundary |

In **Mode 3 CLOSED** the shelter has **zero** air exchange, and opening a valve to clear smoke
breaks the protection the closed mode exists to provide.

> **So the strategy is not the usual one. It is: prevent, detect early, extinguish while it is
> small — and if it cannot be extinguished, LEAVE, because you cannot wait it out.** Part 14.5
> sets out the routes and the decision rule, and records the five findings a fire plan in this
> situation is obliged to raise.

## 2.11 The thermal problem of a sealed box

Nine people, lighting, plant and a dehumidifier in a sealed 332.8 m³ volume put heat in and have
nowhere to put it. The 96-hour balance was computed under owner ruling 10 (RC4):

```
electrical load dissipated INSIDE the envelope        = 5.733 kW
9 occupants at 70 W sensible                         = 0.630 kW
TOTAL SENSIBLE GAIN                                  = 6.363 kW
over 96 h  =  6.363 x 345600 s                       = 2.199 GJ

BOUND 1  adiabatic, AIR ONLY:  216.96 m3 x 1.2 x 1.005 = 261.7 kJ/K
         dT = 8404 K -- PHYSICALLY MEANINGLESS.
         THE AIR HOLDS NOTHING;  THE STRUCTURE IS THE ENTIRE STORY.
BOUND 2  air + the concrete the heat can REACH in 96 h
         thermal penetration sqrt(alpha.t) = sqrt(5.5e-7 x 345600) = 0.436 m
         414.38 m2 of wetted concrete surface, responding depth 0.30 m [A]
         124.3 m3 x 2500 x 0.88                      = 273 493 kJ/K
         dT                                          = 8.03 K
BOUND 3  the air-to-surface film,  h = 3.0 W/m2K [A]
         dT_film = 6363 / (3.0 x 414.38)             = 5.12 K

AIR TEMPERATURE RISE OVER 96 h  =  8.03 + 5.12        = 13.2 K
   from a ground temperature of 26 degC at 6 m depth [A]
   ->  about 39 degC by hour 96, AND STILL RISING, because nothing has
       reached equilibrium

COOLING DUTY TO HOLD 30 degC
   the structure can absorb 273 493 x 4 K            = 1.094 GJ
   heat to be rejected      2.199 - 1.094            = 1.105 GJ
   mean sensible duty       1 105 079 / 345 600      = 3.20 kW
   plus latent                                       = 0.405 kW
   TOTAL MEAN DUTY          3.60 kW = 1.02 TR
   ADOPT 4 kW (1.14 TR) as the closed-mode cooling duty [R]
```

Ruling 17 (RC5) then directed that the heat be rejected **to the ventilation air in open mode
only, adding no new penetration** — and the arithmetic of that ruling is the finding:

```
ventilation 300 m3/h  ->  0.1005 kW/K  ->  63.3 K needed to reject 6.363 kW
at a realistic 5 K difference, 300 m3/h ->  0.50 kW  =  7.9 % of the gain
```

> **`RC5-F1` — 300 m³/h is a CONTAMINANT rate, not a heat-rejection rate**, and it is about an
> order of magnitude short. The second train is standby, not simultaneous, so 600 m³/h is not a
> case the design contemplates. **And in Pune it can be worse than nothing**: whenever ambient
> exceeds the internal temperature, ventilating *adds* sensible heat. **No ambient design
> temperature exists anywhere in this project `[N]`**, so the number of hours cannot be stated —
> only the direction.
>
> **The ruling is therefore recorded as an acceptance of the ≈ 39 °C condition, not a solution to
> it.** The structure and the surrounding rock carry essentially the whole load in both modes.
> `RC4-V1` is narrowed, not closed: from *"no rejection path exists"* to **"the rejection path is
> the ground through the structure, and it has not been modelled."** A transient soil–structure
> **thermal** model is the missing piece — the sibling of the transient soil–structure
> **interaction** already deferred to Phase 3.

## 2.12 What the science section does not supply

| Not supplied | Why, and where it is recorded |
|---|---|
| Weapon yield | `[N]`, and **ruled to stay unstated** — the overpressure and duration are the design inputs. Ruling 6, RC4 |
| Negative-phase and rebound load case | Not designed as a separate case; handled physically at the hatches. Part 17 |
| Support rotation / non-linear SDOF | **Phase 3.** Part 17 |
| Shock propagation down the entry shaft, and the resulting door loading | Needs CFD or a shock tube. **Vendor / specialist.** Part 17 |
| Transient soil–structure interaction | Not demonstrated. Part 17 |
| Transient soil–structure **thermal** model | `RC4-V1`, open |
| Ambient design temperature | `[N]` — nowhere in the project |
| Incident EMP field, waveform, E1/E2/E3 decomposition | `[N]`. The EMP work is designed to the **80 dB performance requirement**, which needs none of them |
| Concrete permittivity / conductivity; whether rebar crossings are tied or welded | `[N]` — and the second materially changes 2.8.2 |

# PART 3 — CODES, STANDARDS AND REFERENCES

## 3.1 The governing caveat, stated before anything else

> **IS 4991:1968 Cl. 1.1 expressly EXCLUDES nuclear explosions from its scope.**
>
> It is used in this project **for its blast loading rules and its dynamic material strengths
> only**, as a documented and conservative extrapolation. **Every structural capacity in this
> project is computed to IS 456:2000**, with IS 13920:2016 for the ductile detailing of the sentry
> post frame.
>
> **A conventional static STAAD.Pro analysis gives the correct DEMAND. It is not, and must never
> be presented as, proof of blast resistance.**

This caveat appears on every deliverable in the project, and it appears here first because a
reader who does not have it cannot correctly weigh anything in Parts 7 to 11.

## 3.2 Code register — with the clauses actually relied upon

> **No clause number in this register was invented.** Where a clause could not be confirmed from
> the material available it is not listed. A code named **by title only** is one the project uses
> for its existence, not for a quotation; **no clause is ever quoted from a document that is not
> in the workspace.**

| Code / reference | Used for | Clauses relied upon |
|---|---|---|
| **IS 456:2000** | All reinforced concrete design | Cl. 6.2.3.1 (E<sub>c</sub>); Cl. 13.4 (construction joints); Cl. 22.2(a) (effective span); Cl. 23.2.1 + Fig. 4 (deflection); Cl. 24.4, 24.5 + Fig. 7 (two-way slabs, load to beams); Cl. 25.1.2 (short column); Cl. 25.4 (minimum eccentricity); Cl. 26.2.1, 26.2.1.1, 26.2.5.1 (L<sub>d</sub>, laps); Cl. 26.3.3 (bar spacing); Cl. 26.4.2, 26.4.2.1, 26.4.2.2 + Table 16 (cover); Cl. 26.5.1.1, 26.5.1.2, 26.5.1.5, 26.5.1.6 (beam steel, links); Cl. 26.5.2.1, 26.5.2.2 (slab steel); Cl. 26.5.3.1, 26.5.3.2 (column steel, ties); Cl. 31.6, 31.6.1, 31.6.3.1 (punching); Cl. 32.2, 32.5(a)(b)(c) (walls); Cl. 33.1(b), 33.2 (stairs); Cl. 34.2.4.1 (footing shear); Cl. 36.4.2 (γ<sub>m</sub>); Cl. 38.1, 38.1(c), 38.1(f) (limit state, stress block, x<sub>u,max</sub>); Cl. 39.1, 39.3, 39.6 (columns, biaxial); Cl. 40.1, 40.2.1.1, 40.2.3, 40.4(a) (shear); Tables 3, 5, 16, 18, 19, 20, 26, 27, 28; Annex D (D-1.1 to D-1.8, D-2); Annex G-1.1(b), G-1.1(c) |
| **IS 875 (Part 1):1987** | Dead loads, unit weights | Table 1 |
| **IS 875 (Part 2):1987** | Imposed loads | Plant / storage 5.0 kPa; office / observation post 3.0; accessible roof 1.5 |
| **IS 875 (Part 3):2015** | Wind — sentry post only | Cl. 6.3, 6.3.4, 7.2, 7.2.1, 7.3.3.13, 7.4; Tables 1, 2, 4, 26; Annex A (V<sub>b</sub> = 39 m/s) |
| **IS 875 (Part 5):1987** | Load combinations | with IS 456 Table 18 |
| **IS 1893 (Part 1):2016** | Seismic | Cl. 6.3.1.2, 6.3.2.2 (combinations, directional); Cl. 6.4.2 + Fig. 2 (A<sub>h</sub>, S<sub>a</sub>/g); Cl. 7.2.3 (I), 7.2.6 (R), 7.3.1, 7.3.2 (seismic weight); Cl. 7.6.1, 7.6.2, 7.6.2(c), 7.6.3 (period, base shear, distribution); Cl. 7.11.1 (drift); Table 3 (Z) |
| **IS 13920:2016** | Ductile detailing — sentry post | Cl. 6.1.1, 6.1.2, 6.1.3 (beam geometry); Cl. 6.2.1(b), 6.2.2, 6.2.3, 6.2.4 (beam steel); Cl. 6.3.3, **6.3.4**, 6.3.5.1, 6.3.5.2 (capacity-design shear, hoops); Cl. 7.1, 7.2.1 (strong column–weak beam), 7.3, 7.4 (columns); Cl. 8.1, 8.2 (special confining reinforcement); Cl. 10.4 (boundary elements — **checked, not triggered**) |
| **IS 3370 (Parts 1, 2):2021** | Crack width, surface-zone steel | 0.2 mm limit; 0.35 % surface-zone steel over a 250 mm zone |
| **IS 1786:2008** | Fe500D reinforcement | **D** grade — guaranteed minimum elongation |
| **IS 1904:1986** | Presumptive bearing capacity | Table 1 (hard rock, 3 240 kPa) |
| **IS 2950 (Part 1):1981** | Raft foundations | General provisions |
| **IS 12070** | Rock foundations | Cl. 6 (settlement on sound rock); Table 2 (broken bedrock, 10 kg/cm² — the SEMT report's own basis) |
| **IS 1498:1970** | Soil classification | CH, GM, GP, SC; free-swell-index bands — the SEMT report's classification basis |
| **IS 2720** Pts IV, VIII, X, XIII, XL | Soil testing | Classification (Pt IV); compaction, OMC–MDD (Pt VIII); UCS (Pt X); direct shear (Pt XIII); free swell (Pt XL) — **the SEMT report's own test methods, cited as it cites them** |
| **IS 2720 (Part 28)** | In-situ density | Backfill compaction testing, WBS `A7015` |
| **IS 1121 (Part I)** | Rock strength | Compressive strength of rock cores — the SEMT report's Appendix C basis. *(The report prints the year as "1874"; that is a typographical error, transcribed as printed, not corrected)* |
| **IS 2470 (Part 1):1985** | Septic tank | Cl. 6.2 (24 h detention), 6.3 (30 L/person/yr sludge), 6.5 (L:B 2–4), 6.6 (min width 750, min depth 1.0 m), 6.9 (vent); Table 1 (≤ 10 users: 1.5 × 0.75 × 1.0) |
| **IS 2470 (Part 2):1985** | Soak pit / dispersion | Cl. 4 (**percolation test — mandatory**), Cl. 5 (dispersion trench) |
| **IS 4991:1968** | **Blast loading rules and dynamic material strengths ONLY** | **Cl. 1.1 (EXCLUDES NUCLEAR — quoted in every deliverable)**; Cl. 6.2.1 (reflected pressure, recessing); Cl. 7.2 + Table 3 (buried roof / walls, K<sub>a</sub>); Cl. 7.4 (drag on bermed faces); Cl. 10.3.1 (dynamic f<sub>ck</sub>, f<sub>y</sub>); **Cl. 10.3.1.1 (no dynamic increase on shear; +25 % bond)**; Cl. 10.3.3 (DLF = μ/(μ−0.5)); Cl. 11.1 (no wind / EQ with blast); Cl. 11.2 (no live load on the roof at blast); Fig. 6 (SDOF — **Phase 3**) |
| **IS 1077** | Common burnt clay bricks | Sentry post masonry infill, 190 × 90 × 90 modular, SP-B1 |
| **IS 732:2019** | Electrical wiring installations | EL1 |
| **IS 3043:2018 / IEEE 142** | Earthing | ≤ 5 Ω target — **a power-safety and lightning number, not an EMP one** |
| **IS 694:2010 · IS 1554 (Pt 1):1988** | Cables | Final circuits; sub-mains and generator cabling |
| **IS 13416** | Construction-phase fire safety | In the register for exactly that |
| **SP 16:1980** | Design aids | Column interaction charts — **cross-checked only**; the P–M values in Part 11.5 were computed from first principles, not read off |
| **SP 34:1987** | Detailing | Shape codes; **Cl. 5.5 (opening-corner detailing)** |
| **NBC 2016 Part 4** | Fire and life safety | Stair geometry, 1 100 guarding, means of escape |
| **BS 8666** | Bar shape codes | Used alongside SP 34 in every bar bending schedule |
| **UFC 3-340-02** | US criteria, **cited as US criteria** | §4-27 (opening trimmers); §4-30 (direct shear) |
| **UFC 3-350-04AN** | US criteria | Referenced in the Phase 1 report |
| **MIL-STD-188-125-1** | EMP | §5.4 (access), §5.5 (waveguide below cutoff), §5.7.2.1 (power PCI), §5.7.4.1 (fibre), §5.7.6 (RF); **80 dB, 10 kHz – 1 GHz** |
| **IEEE Std 299** | EMP verification | Shielding effectiveness survey |
| **FEMA 453** | Shelter ventilation | 0.25 cfm/ft²; carbon adsorber performance |
| **EN 1822** | HEPA classification | H14, ≥ 99.995 % at MPPS |
| **Glasstone & Dolan** | Weapons effects | Unclassified, public — blast and radiation data only |
| **Biggs**, *Structural Dynamics* | SDOF method | Referenced for the **Phase 3** support-rotation check |

## 3.3 Codes named by title only

These are named because the work touches their subject, and **no clause is quoted from any of
them**, because no copy is in the workspace:

`IS 1742` · `IS 5329` · `NBC 2016 Part 9` (drainage) · `IS 3103` and the ISHRAE / ASHRAE
handbooks (ventilation) · `IS 3696 (Part 2)` (ladders) · `IS 3764` (excavation safety and slopes)
· `IS 2502` (bar bending — **explicitly NOT held and NOT cited**, which is why the schedules take
no bend deduction and say so).

## 3.4 The hierarchy used to resolve a conflict

Ten conflicts were closed in this project and a further set of rulings settled everything that
could be settled on the evidence. The precedence that produced those rulings is stated here
because it is itself part of the design record:

1. **A drawing beats an older document.** Precedent **C1**: the drawings are Rev F, the design
   report is Rev D; where they disagree, the drawing governs.
2. **Arithmetic beats a transcription.** Precedent **C18**: (−)8.000 − (−)7.600 = 0.400, so the
   sump base is 400 thick and the "300" in a sheet note is a transcription error.
3. **The `.std` file beats a screenshot of it.** Part D of the master was written from nineteen
   screen captures; six `.std` files are now in the workspace, and the files are primary.
4. **A value reproduced from independent lines beats a lone outlier.** Precedent **C21**: nine
   statements of 300 m³/h against one of 250, with 250 failing the sheet's own FEMA criterion.
5. **Where nothing in the project can decide it, it stays open.** No amount of choosing between
   recorded values supplies a datum, a test result or a client decision.

# PART 4 — SITE SELECTION AND GEOTECHNICS

## 4.1 The site, and what is and is not known about it

| Item | Value | Class |
|---|---|---|
| Installation | CTW / College of Military Engineering campus, Pune, Maharashtra | `[C]` |
| Plot | Undeveloped rectangle **east of the two CTW blocks**, west of the perimeter track and nullah line, **CBRN Live Training Area to the south** | `[C]` |
| Latitude / longitude | **NOT ESTABLISHED** | `[N]` |
| Plot boundary and area | **NOT DIMENSIONED ANYWHERE.** No scale bar, grid, boundary dimension or coordinate appears on any supplied site image | `[N]` — master gap **D3** |
| Site benchmark | **NONE.** Nothing ties any supplied level to the project datum | `[N]` |
| Project datum | **finished grade = 0.000**, local | `[C]` |
| Site orientation | **+X = EAST, +Y = NORTH** | `[A]` — fixed for the first time at SG2 |

> **"No site plan" is not closed and cannot be closed by imagery.** Until a boundary, a dimension,
> a benchmark and a coordinate exist, the berm, the hardstanding, the access, the five external
> drainage runs, the concealment layout and the cut-and-fill cannot be drawn. What the site
> package added is that the **setting** is now recorded, which it was not.

### 4.1.1 The selection, and what it got right

The site was chosen at the P1 stage. Its recorded SWOT, verbatim: **Strengths** — proximity to
FCBRNP · availability of electric lines · good road connectivity · good water supply · **no
pipelines**. **Weakness** — *located near perimeter fence*. **Opportunities** — training
value. **Threat** — interference with the CTW schedule.

Three of those strengths are load-bearing for the design that followed, and none had been written
down as such:

1. **"No pipelines."** For a 22 × 6.2 m box excavated to (−)6.800 with a continuous gas-tight,
   EMP-bonded envelope, a buried main crossing the footprint would have been a first-order
   problem: **every envelope penetration is a blast, gas and EMP discontinuity.** A clear plot is
   worth more here than on an ordinary building.
2. **"Availability of electric lines."** The only other record of an incoming mains supply anywhere
   in the project is a line in the owner's own construction schedule. This slide is earlier. It
   gives no capacity — `EL-V4` — but it confirms the supply exists.
3. **"Good road connectivity."** The works programme carries **994 m³ of rock excavation by
   hydraulic breaker with no blasting** and tipper haulage throughout. That is a haul-route
   requirement and the site meets it.

### 4.1.2 What the selection did not consider

| Not considered | What it costs, quantified |
|---|---|
| **Ground conditions on the plot itself** | The selection rests on a soil report for three *other* buildings. The confirmatory investigation `A1075` (12 d, **critical path**) must be located **on this plot** — `SG-V1` |
| **Depth of investigation** | Nothing is known below about 1.5 m; the structure founds at (−)6.800 — **`SG-V2`, the governing item** |
| **Ground slope** | The plot is on the edge of a slope falling east. **No cut-and-fill item exists in the bill** because no site plan exists |
| **"Near perimeter fence"** | It is also a **concealment** weakness, and the distance has never been dimensioned — `SG2-V2`, `CAM-V2` |

## 4.2 The sub-soil investigation, and the one fact that governs it

| # | Document | What it is | Class |
|---|---|---|---|
| 1 | **SEMT/67/15** — *Report on Sub-Soil Investigation for CTW Ph-III ACCN Project at CME Pune*, Soil Engineering & Material Testing Wing, College of Military Engineering. Raised on CTW letter 8722/Ph-III/CTW/116/Q dated 20 May 2015 | A real investigation: **11 trial pits at 3 locations**, Appendices A (classification), B (soil test results), C (rock cores) | `[C]` |
| 2 | **P1 presentation deck** — *Construction of CBRN Hardened Underground Ops Room*, 32 slides | The project's own first-phase presentation: location, contour, watershed, pipelines, elevation profile, SWOT, wind, precipitation, temperature, seismic, soil | `[C]` as a record of what was presented |

### 4.2.1 It is not an investigation of this plot

The SEMT report investigates **G Building (TP-1 to TP-4)**, **H Building (TP-5 to TP-8)** and the
**Mess Building (TP-9 to TP-11)**. The project plot is a separate undeveloped area east of the
CTW blocks. The report may be carried across only on the strength of its own paragraph 5:

> *"The area under investigation is underlain by the Deccan Trap formation. These are volcanic
> lava flows, which were poured out between the late cretaceous and early Eocene times. These
> basaltic flows are horizontally bedded and more or less uniform in character over a wide area."*

**That carry-across is an assumption `[A]`, not a finding of the report.** And the report itself
shows how much variation "uniform over a wide area" permits: across three locations a few hundred
metres apart, rockhead moved from **0.9 m to 1.5 m** and the surface stratum changed from a 1.0 m
high-plasticity clay to a 0.2 m clayey-sand murrum.

### 4.2.2 `SG-F2` — the governing finding

| | Level |
|---|---|
| **Deepest stratum boundary recorded anywhere in the report** | **(−)1.500** |
| Sentry footing F1, on in-situ basalt | (−)2.000 |
| Underground box, internal floor | (−)6.100 |
| Mat soffit | (−)6.700 |
| **FORMATION — what the mat actually bears on** | **(−)6.800** |
| Sump SU-01 base | (−)8.000 |

> **The investigation reached about 1.5 m. The structure founds at 6.8 m.**
>
> There are **5.3 m of completely unlogged ground** between the bottom of the deepest trial pit and
> the formation the 600 mm mat bears on, and **6.5 m** to the sump base. **Only the sentry post
> footing F1 at (−)2.000 lies inside the investigated horizon, and only just.**
>
> Nothing the report says about rockhead continuity, groundwater, jointing, red-bole seams or
> modulus of subgrade reaction can be read as covering the founding horizon of the shelter.
> **`SG-V2`, and it is the item a reviewer should look at first.**

### 4.2.3 The report is internally consistent, and that was checked before it was used

| Chain | Check | Result |
|---|---|---|
| Soil | `SBC = q_ult / 2.5`, the report's own stated factor of safety | **6 of 6 rows reproduce** |
| Rock, step 1 | `UCS = max load / specimen area` | **6 of 6 rows reproduce** |
| Rock, step 2 | `SBC = UCS / 25`, rounded — the factor the report applies but never prints | **6 of 6 rows reproduce** |

**`SG-F1`. The SEMT report is internally consistent and is usable.** That is worth establishing
before anything is built on it.

## 4.3 Ground parameters — the design set

| Parameter | Value | Class |
|---|---|---|
| Ground | Deccan basalt (trap), with red-bole / vesicular seams at flow contacts | `[A]` |
| Rockhead | (−)1.500 to (−)2.000 | `[A]` |
| Presumptive safe bearing capacity | **3 240 kPa** (IS 1904:1986 Table 1, hard rock) | `[A]` |
| Bulk unit weight γ | 20 kN/m³ | `[A]` |
| Saturated unit weight γ<sub>sat</sub> | 21 kN/m³ | `[A]` |
| Submerged γ′ = 21 − 9.81 | **11.19 kN/m³** | `[C]` derived |
| At-rest coefficient K₀ = 1 − sin φ | **0.50** (φ ≈ 30°) | `[A]` |
| **Design groundwater table** | **(−)2.000** (monsoon) | `[A]` — **the single most important number to confirm** |
| **Modulus of subgrade reaction k<sub>s</sub>** | **100 000 to 500 000 kN/m³** | `[A]` — **run the mat model at BOTH bounds** |
| Settlement | Negligible on sound basalt (IS 12070) | `[A]` |
| Soil transmission factor K<sub>a</sub>, saturated | **1.0** (IS 4991 Cl. 7.2 + Table 3) | `[C]` |
| K<sub>a</sub>, dry compacted berm fill | ≈ 0.5 | `[A]` — **deliberately not relied on** |

> **The hazard is not the basalt — it is the flow contacts.** A single red-bole seam under the mat
> produces the differential-support case that **SIZES the mat** (Part 9.3, Case 2, 84 % utilised).
> Horizontally bedded flows are precisely the geometry that produces flow contacts at intervals,
> and **the report neither finds nor excludes one, because it never reached the founding horizon.**
> Over-excavate any red-bole or vesicular seam at founding level and replace with M15 lean
> concrete.

### 4.3.1 What the evidence changed, and what it did not

**Not one parameter above is changed by the supplied documents.** What each gained is a stated
provenance and a quantified margin:

| Row | What the evidence says | Effect |
|---|---|---|
| Ground | Deccan Trap **confirmed** — *"horizontally bedded and more or less uniform"* | **Corroborated.** The flow-contact hazard is neither found nor excluded |
| Rockhead | **0.9–1.5 m** at three locations | The report's band is **entirely at or above** the assumed 1.5–2.0 m. **Conservative for founding depth, unconservative for rock excavation quantity: +118 m³, ≈ 2 days** (`SG-F5`) |
| **SBC 3 240** | Measured basalt **1 961–2 059 kPa soaked**, 2 942–3 530 unsoaked | The founding horizon is **4.8 m below the design GWT**, so **soaked governs**. Worst utilisation rises 12.5 % → **20.6 %**; every element still passes with a factor of **4.8** in hand. **3 240 stands — it is an IS 1904 presumptive value and is declared as one** (`SG-F3`) |
| γ 20 / γ<sub>sat</sub> 21 | 95 % MDD at OMC gives **19.12–19.61**; γ<sub>sat</sub> back-figures to **21.26** | Bulk 20 is **2–5 % conservative** for lateral load; γ<sub>sat</sub> agrees **within 1.2 %** |
| K₀ 0.50 | Measured φ **27–35°** → K₀ 0.426–0.546 | **Conservative** against all three granular murrum samples. Worst case moves the wall design load **under 1 %** — the walls are blast-governed (`SG-F9`) |
| **GWT (−)2.000** | *"Water table was not encountered in any trial pit"* — **in pits ~1.5 m deep** | **The provenance, recorded for the first time: no water was found, so 2 m was CHOSEN.** *Not encountered* here means **not reached** (`SG-F6`) |
| k<sub>s</sub> | **Nothing** — no plate load test | Untouched. **Both bounds still outstanding** |
| Settlement | Net pressure at formation ≈ **−105 kPa** | This is *why* "negligible" is true — and the same fact that makes **flotation** the governing problem (`SG-F4`) |

### 4.3.2 Bearing: it does not govern anything

| Check | Demand | / 3 240 `[A]` | / 1 961 soaked | Verdict |
|---|---|---|---|---|
| Mat, service | 58.4 kPa | 1.80 % | 2.98 % | **PASS** |
| Mat, **blast** | 404.9 kPa | 12.50 % | **20.64 %** | **PASS** |
| Sentry footing F1 | 157.6 kPa | 4.86 % | 8.04 % | **PASS** |

Even at the **broken** basalt value of 981 kPa — the horizon 5 m *above* the formation — the mat
under full blast would be at **41 %**. **The bearing case is nowhere near governing anything.**

## 4.4 Groundwater — the central question

> *"Water table was not encountered in any trial pit. However, water table may raise during/after
> rainy season."* — SEMT/67/15 para 13 `[C]`
>
> *"Proposed structure safe for water table at depth of 2 m below GL"* — P1 deck slide 29 `[C]`

**The provenance of (−)2.000, recorded for the first time: no water was found, so a depth of 2 m
below ground level was CHOSEN, and the structure was then designed to be safe for it.** That is
an assumption adopted in the absence of data. It is a defensible one — it puts the table near the
surface, which is the conservative direction for uplift and for lateral load. **It is not a
measurement, and nothing in this project turns it into one.**

Three reasons the observation does not reach the design question:

1. **Depth.** The pits reached about 1.5 m. The design GWT is at (−)2.000 — **already below the
   deepest pit** — and the founding horizon is at (−)6.800. **Here, *not encountered* means *not
   reached*.**
2. **Season.** The report itself says the table *"may raise during/after rainy season"*. The
   request is dated 20 May 2015; if the field work followed promptly it was the **pre-monsoon
   minimum**. The report nowhere states the field-work date, so this is inference and is tagged
   `[U]`, not asserted.
3. **Ground type.** Deccan Trap groundwater is not a simple water table in a porous medium. It
   sits in the vesicular and jointed zones **at the flow contacts** — the same feature that sizes
   the mat. Such water is commonly perched and strongly seasonal, and **an open trial pit in the
   dry season is close to the worst available instrument for finding it.**

> **And it is the number that matters most.** Of the 15.41 kPa/m lateral gradient, **9.81 is
> water**. The hydrostatic uplift on the mat is **46.11 kPa = 6 289 kN over 136.4 m²**. What
> closes it is a **standpipe piezometer read through a full monsoon** — and the programme's own
> monitoring window, 12 November to 4 December, **is not in the monsoon**.

## 4.5 Black cotton soil — confirmed, and it reaches two elements

**New, and recorded nowhere in this project before the site package: the surface soil is BLACK
COTTON, CH, free swell index 60–65 % — the top band of the IS 1498 scale.** `[C]`, by measurement,
from SEMT/67/15 Appendix A.

**Nothing structural founds in it.** The mat is at (−)6.700 and footing F1 at (−)2.000, both in
basalt — and Part 11.6's insistence that F1 bears *"on in-situ rock, never on backfill"* is now
backed by a measurement rather than by instinct. **Two elements are exposed anyway:**

| Element | Exposure | Status |
|---|---|---|
| **The covered entry stairwell's stepped raft** | Its top founds at about (−)0.300, **inside the 0.18–1.0 m CH horizon**. This is **heave**, not bearing — and the stairwell is expendable against *blast*, which heave is not | **RULED — strip and replace.** Ruling 12, RC4: strip the CH horizon to 1.000 m below existing ground over 4.410 × 4.000 m, replace with granular fill at **FSI ≤ 20 %** (IS 2720 Pt XL) in 200 mm layers to **≥ 95 % MDD**, extending **1.000 m beyond every raft edge**. **BOQ item added: 8 m³, rate `[A]`** |
| **The 300 mm turf concealment layer** | Re-laid *from the site's own stockpile* over the 150 mm granular filter. If the site's own topsoil is this CH clay it **cracks in the dry season** — a concealment defect — and the wet/dry cycles **pump fines into the filter, which is the one thing the filter exists to stop** | **LEFT OPEN by owner ruling 16 (RC4).** `SG-V7`. The load is unaffected: 300 at 18 kN/m³ = 5.40 kPa is right for a black cotton soil |

> **The two collide, and the collision is recorded rather than resolved.** The strip-and-replace
> ruling produces a stockpile of **exactly the material `SG-V7` warns against re-laying** — and
> the excavation-face ruling below produces 76–118 m³ more of it.

## 4.6 The excavation face — ruling 22 (RC6)

The project had measured **1.000 m working space and vertical unbenched faces for the full
6.800 m**. In basalt that is reasonable. But rockhead is at 0.9–1.5 m with a CH horizon at FSI
60–65 % on top of it:

> So the face is about **1.0–1.5 m of soil — including very-high-swelling clay — standing
> vertically on 5.3–5.9 m of rock, with the rock excavation undercutting it.** Under the
> flotation acceptance (Part 18.4) it also stands open **across a monsoon.** That soil cap is the
> one part of this excavation that has no business being vertical.

```
ADOPTED   batter 1 : 1 MINIMUM over the soil cap, grade to rockhead, all four
          sides;  VERTICAL FACE RETAINED IN ROCK below rockhead

          extra excavation    1 : 1     1.500 m offset       76.4 m3
                           1.25 : 1     1.875 m offset       96.7 m3
                            1.5 : 1     2.250 m offset      117.6 m3
          (a 1.000 m bench at rockhead instead would be    96.6 m3)

          WORKING SPACE UNCHANGED -- the 1.000 m is at FORMATION, 5.3 m below
          the battered zone, so no BOQ working-space quantity moves
```

> **1 : 1 is a MINIMUM, not the answer.** A batter in FSI 60–65 % clay, undercut and wetted across
> a monsoon, may need to be considerably flatter. `IS 3764` is named **by title only**.
> **The angle and its seasonal variation are the geotechnical engineer's, and the quantity moves
> with the angle** `[A]`. **`WM-V9` closes as a measurement basis** — the project now states a
> face treatment instead of an unexamined vertical — **but the slope-stability assessment it
> always asked for is still outstanding.**

## 4.7 Rockhead, and what it costs

| Location | Sound basalt below | On the project datum |
|---|---|---|
| G Building (TP-1 to TP-4) | 1.500 m | (−)1.500 |
| H Building (TP-5 to TP-8) | 0.900 m | (−)0.900 |
| Mess Building (TP-9 to TP-11) | 1.000 m | (−)1.000 |
| **Report band** | | **(−)0.900 to (−)1.500** `[C]` |
| **Assumed band** | | **(−)1.500 to (−)2.000** `[A]` |

**The two bands touch at exactly one point, (−)1.500.**

| Rockhead | Depth of rock cut | Rock volume m³ | vs BOQ |
|---|---|---|---|
| (−)0.900 | 5.900 m | 1 161.12 | **+118.12** |
| (−)1.000 | 5.800 m | 1 141.44 | +98.44 |
| (−)1.500 | 5.300 m | 1 043.04 | +0.04 |
| (−)1.750 ← BOQ `E-02b` | 5.050 m | 993.84 | −49.16 |
| (−)2.000 | 4.800 m | 944.64 | −98.36 |

**Overrun at the report's shallow rockhead: +118.1 m³ (+11.3 %), ≈ 2 extra days** at the
programme's 60 m³/day output. **Total excavation does not change** — soil falls by the same volume
as rock rises — so the money at stake is the **rate difference** over about 118 m³, not a rock rate
over 118 m³. **No BOQ quantity is changed**; the owner's own bill governs and its risk register
already carries the item, saying *"roughly one extra day"*. **What this adds is the number: it is
about two.**

One consequence is favourable and is recorded because it is free: the sliding argument rests on
the box being *"socketed ~4.8 m into basalt"*. On the report's band the socket is **5.3 m to
5.9 m**. **The argument gets stronger.**

# PART 5 — GEOMETRY AND CONFIGURATION

## 5.1 Coordinate system

```
ORIGIN      = south-west EXTERNAL corner of the underground box, at ground level
X           = EAST   (along the length, 0 to 22000)
Y (plan)    = NORTH  (across the width, 0 to 6200)
LEVELS      = metres relative to finished site grade 0.000, negative downwards
UNITS       = millimetres in all DXF geometry; metres in all level annotation
```

> **Site orientation `+X = EAST, +Y = NORTH` was fixed for the first time at SG2** and is `[A]`.
> Every drawing and every calculation in this project uses this system. **The STAAD underground
> model does not**: it is built on mid-surface geometry with its origin at the **underside of the
> mat**, so `project level = model Y − 6.700`. Part 8.2.

## 5.2 Level schedule

| Level | Value | Description |
|---|---|---|
| Grade | **0.000** | Finished site level, crowned, falls 1:50 away |
| Top of pressure slab | **(−)2.000** | = headhouse floor level |
| Roof soffit | **(−)2.900** | 900 mm slab |
| Internal floor / top of mat | **(−)6.100** | 3 200 mm clear height |
| Underside of mat | **(−)6.700** | 600 mm mat |
| Formation / underside of PCC | **(−)6.800** | 100 mm blinding |
| **Design groundwater table** | **(−)2.000** | monsoon `[A]` |
| Rockhead | (−)1.500 to (−)2.000 | `[A]` |
| Stair landing L1 | (−)4.7333 | 8 risers up from the floor |
| Stair landing L2 | (−)3.3667 | 16 risers up from the floor |
| Headhouse roof soffit | **+0.400** | 2 400 mm clear internally |
| Headhouse roof top | **+0.900** | no earth cover; berm graded to this level |
| Entry stairwell roof at head | **+2.450** | soffit +2.200 |
| Sentry post GF FFL | **+0.450** | = base of the STAAD model |
| Sentry post first floor | **+3.650** | storey height 3 200 |
| Sentry post roof | **+6.700** | storey height 3 050 |
| Sentry post parapet top | **+7.000** | |
| Sump pit invert | (−)7.600 | pit base slab (−)8.000 |

## 5.3 The main box

| Item | Value | Was | Class |
|---|---|---|---|
| **External length** | **22 000 mm** | 21 600 (pre-M1) | `[C]` |
| External width | 6 200 mm | unchanged | `[C]` |
| **Internal length** | **20 800 mm** | 20 400 | `[C]` |
| Internal width (clear span of the roof) | **5 000 mm** | unchanged — **do not widen** | `[C]` |
| Perimeter wall thickness | 600 mm | unchanged | `[C]` |
| Roof (pressure) slab | 900 mm | unchanged | `[C]` |
| Mat foundation | 600 mm | unchanged | `[C]` |
| Blinding / PCC | 100 mm M15 | unchanged | `[C]` |
| Internal clear height | 3 200 mm | unchanged | `[C]` |
| Engineered cover over roof | 2 000 mm layered | reduced from 4 000 in an earlier revision | `[C]` |

> **Why lengthening the box is structurally free, and widening it is not.** The roof aspect ratio
> is 20.8 / 5.0 = 4.2, and IS 456 Table 26 is tabulated only to l<sub>y</sub>/l<sub>x</sub> = 2.0,
> so **two-way action cannot be claimed**. The roof therefore spans one-way across the 5 m width,
> and its moment depends on that width alone. **Adding length adds no roof moment; widening
> 5.0 → 6.0 m would increase it by 44 %.** That single fact is the structural basis of
> Modification M1.

## 5.4 Bay schedule, and internal walls

| Bay | X range (mm) | Clear width | Use |
|---|---|---|---|
| 1 | 600 – 3500 | 2900 | Emergency stores, 1 000 L potable tank, **ESC 1** |
| 2 | 3610 – 5410 | 1800 | Lavatory (1800×2000) + medical (1800×3000) |
| 3 | 5520 – 9020 | 3500 | Ops room and hazard plotting; **EMP Zone 2 enclosure** |
| 4 | 9130 – 10930 | 1800 | Berthing, 3 × 3-tier bunks, 9 berths |
| 5 | 11040 – 12600 | **1560** | CBRN plant: **2 × 300 m³/h** filter trains, CO₂/O₂, dehumidifier, **clean sump** |
| 6 | 12800 – 14800 | 2000 | Decon airlock, 3 stages (2000×2000, 2000×1500, 2000×1500) |
| 7 | **15200 – 18000** | **2800** | **Stair shaft** (shifted +200 by M1) |
| 8 | **18400 – 21400** | **3000** | Generator 15 kVA (grey zone), **ESC 2** at X 19 900 |

| Mark | X range (mm) | Thickness | Notes |
|---|---|---|---|
| W8 partitions ×4 | 3500–3610, 5410–5520, 9020–9130, 10930–11040 | 110 | Each with a **permanent 900 mm gap at Y 2500–3400** |
| W5 | 12600 – 12800 | 200 | Bay 5/6, **fire and gas-tight only**, no pressure differential |
| **W6** | **14800 – 15200** | **400** | Bay 6/7 — **M1, was 200. Protective boundary.** Blast Door 1 opening Y 600–1800 |
| **W7** | **18000 – 18400** | **400** | Bay 7/8 — **M1, was 200. Protective boundary.** Blast Door 2 opening Y 600–1800 |

> **Modification M1 is not a uniform shift, and it must never be applied as one.** Nothing west of
> X 14 800 moves. W6 and W7 thicken **about their own faces**. The shaft moves +200; Bay 8 and the
> east end move +400; the headhouse and the covered stairwell move +200 **as whole structures**.
> **Re-derive per element, never translate wholesale.**

## 5.5 Stair shaft, roof void and cantilever pad

```
Stair shaft (Bay 7) clear       X 15200 - 18000   Y  600 - 5600   = 2800 x 5000
Void in the pressure slab       X 15200 - 18000   Y  600 - 3760   = 2800 x 3160
Cantilever pad (remaining slab) X 15200 - 18000   Y 3760 - 5600   = 2800 x 1840
Flight A (flights 1 and 3, stacked)  X 15300 - 16500   (1200 wide)
Well                                 X 16500 - 16700   (200)
Flight B (flight 2)                  X 16700 - 17900   (1200 wide)
Landing L1 (-)4.7333   Y 3760 - 4960, full 2800 width
Landing L2 (-)3.3667   Y  600 - 1800, full 2800 width (over the arrival landing)
Arrival landing (-)6.100 = the mat surface, Y 600 - 1800
Store under landing L1  Y 4960 - 5600
MAIN STAIR  24R @ 170.8333, tread 280, 3 flights x 8R, rise 4100, headroom 2533
```

## 5.6 Escape shafts, and the 750 mm rule

| | ESC 1 | ESC 2 |
|---|---|---|
| Centre | (2050, 2050) | **(19900, 2050)** — shifted +400 by M1 |
| Clear opening | 1 400 mm dia | 1 400 mm dia |
| Collar | 250 mm RC, OD 1 900 | 250 mm RC, OD 1 900 |
| Clearance, opening edge to wall face | 750 mm all round | 800 / 800 mm |
| Head level | **+0.150** | **+0.700** |
| Climb from (−)6.100 | **6.250 m** | **6.800 m** |
| Escape route | **R2** | **R3** — **shares Bay 8 with the generator** |

> **THE 750 mm CLEARANCE RULE.** Opening edge to structural wall face ≥ 750 mm = 250 collar +
> ~400 trimmer band + 100 tolerance. **A bay must therefore be at least 1 400 + 2 × 750 = 2 900 mm
> wide to hold an escape shaft.** That rule drove the Rev C lengthening, and **it is why
> Modification M1 could not take the 400 mm it needed out of Bay 8.**

## 5.7 Headhouse

```
External     X 13600 - 18400   Y  200 - 6000   = 4800 x 5800
Internal     X 14000 - 18000   Y  600 - 5600   = 4000 x 5000
Walls 400 thk (HW1 south, HW2 north, HW3 west, HW4 east)
Roof  500 thk, soffit +0.400, top +0.900, NO earth cover
Floor = the top of the 900 pressure slab, (-)2.000
Clear internal height 2400
Inner security door 900 x 2100 in HW2 (north), X 14450 - 15350.  NOT blast rated.
Berm graded against all four walls to +0.900 at 1.5 : 1
```

| Wall | Runs | Length | Sits over |
|---|---|---|---|
| HW1 south | in X | 4 000 | Box south perimeter wall — **direct** |
| HW2 north | in X | 4 000 | Box north perimeter wall — **direct** |
| **HW3 west** | in Y | 5 000 | **Bay 6, mid-slab. NO wall below** — a line load on the pressure slab, checked at **26 %** two-way / **41 %** on the one-way bound (Part 10.4) |
| HW4 east | in Y | 5 000 | **Wall W7 (18000–18400). M1 made these align exactly** |

## 5.8 Covered entry stairwell

```
External     X  9250 - 16050   Y 5750 - 7750   = 6800 x 2000
Internal     X  9500 - 15800   Y 6000 - 7500   = 6300 x 1500
Walls 250 RC (both sides, headwall, east wall)
Top landing   X  9500 - 11000  at 0.000, 250 thk
Flight        X 11000 - 14300, 12R @ 166.6667, going 300, 11 x 300 = 3300, waist 250
Platform      X 14300 - 15800  at (-)2.000, 1500 x 1500, 250 thk
Roof 250 RC raking, soffit 2200 above the flight; IT STAYS 250 OVER THE PLATFORM
Entry door 1000 x 2100 at grade in the headwall (X 9250 - 9500), opens OUTWARD
300 mm channel + grating, full 1500 width, at X 8950 - 9250
Stepped RC raft 300 thk on compacted fill; MOVEMENT JOINT where it meets the headhouse
1.0 m3 external sump at the platform, own soakaway
Berm 1.5:1 against the walls to +0.900, toe at grade over 1350
```

> **The roof stays 250 mm over the platform — conflict C16, ruled and closed.** The clause used to
> read *"over the platform it becomes the 500 headhouse roof"*, which **no other part of the
> project supported**: the structural design designs a 250 roof, the load register loads one, the
> reinforcement register registers one, and **the headhouse footprint Y 200–6000 does not reach the
> platform at Y 6000–7500 at all.** One clause was the only place in the project saying 500.

## 5.9 Sentry post

```
External plan          4000 x 5000        Internal 3600 x 4600
Column grid            A-B  3650 c/c (X)  .  1-2  4650 c/c (Y)
Grid coordinates       A: x = 175   B: x = 3825   |   1: z = 175   2: z = 4825
Columns C1             350 x 350, 4 No., both storeys
Beams B1               250 x 450, spanning A-B (3650 c/c), on grids 1 and 2
Beams B2               250 x 450, spanning 1-2 (4650 c/c), on grids A and B
Slab S1                150 thk two-way, 3650 x 4650 c/c, both floors
Plinth beam PB         250 x 400 at +0.450
Footings F1            1500 x 1500 x 600, 4 No., on in-situ basalt at (-)2.000
Ground storey infill   190 BRICK MASONRY in the 200 structural zone  (SP-B1)
First storey infill    armoured vision panels, 1200 wide
Spiral stair           external, 1000 R, 250 dia central pole
Door D1                900
Storey heights         ground 3200 (+0.450 -> +3.650), first 3050 (+3.650 -> +6.700)
Siting                 >= 10 m clear of the shelter excavation
Site position          X 32000 - 36000,  Y 600 - 5600     [A]  -- RC4, EAST ruling
```

### 5.9.1 SP-B1 — the walls are brick masonry, not RC ballistic panels

The Rev F drawings call the ground-storey infill *"200 RC ballistic panels"*. By instruction that
became **190 mm one-brick modular brickwork to IS 1077, laid in CM 1:6, built inside the unchanged
200 mm structural zone**, with the residual 10 mm taken up at the internal face in the plaster.

**190 and not 230** because 230 conventional brickwork would project 30 mm past the column faces
and change the confirmed 4 000 × 5 000 external envelope. **Every other value in the block above
is unchanged.** Quantity: **12.20 m³ / 64.19 m² face**, ≈ 6 400 bricks.

Four consequences were recorded rather than buried:

1. **Lintels became necessary.** The RC panels needed none. Designed at SP-B2 — Part 11.7.
2. **A wall tie detail became necessary.** None existed. Designed at SP-B2.
3. **The seismic weight falls.** Brick at ≈ 20 kN/m³ over 0.190 × 2.600 gives **≈ 9.88 kN/m**
   against the modelled **13.000 kN/m**, so `W` falls, `V_b` falls, and **every member designed to
   73.18 kN is over-designed.** *That is a direction, not a verification* — `WM-V6`, **left open by
   owner ruling 19 (RC5): wait for STAAD.** The modelled 13.000 kN/m is retained because it is
   conservative.
4. **The ballistic function is lost.** Brick masonry does not give the protection the Rev F panels
   were named for. **RULED — ruling 7 (RC4): ballistic protection is NOT required. Brick stands.**

### 5.9.2 The sentry post's position — one assumed position instead of two, and it still fails the rule as written

> **Ruling 8 (RC4): the EAST position is adopted.** The elevation's own note sets **X 32 000 –
> 36 000** — 4 000 wide, which is the post's actual external dimension. *(An earlier record of
> X 31 700 – 36 300 is 4 600 wide and matches nothing; the drawing is the primary source and is
> corrected.)* **An elevation cannot give a Y**, so **Y 600 – 5600, centred on the box
> longitudinal centreline Y 3100**, is set by the ruling.
>
> **`RC4-F3` — and it fails the rule as that rule is written.** *"≥ 10 m clear of the shelter
> EXCAVATION"*: X 32 000 is **10.00 m** clear of the **box face** at X 22 000, but the
> **excavation** face with its 1 000 mm working space is at X 23 000 — giving **9.00 m**. The
> drawing's note cites the excavation rule while applying the box face. Satisfying it as written
> moves the post to X 33 000 – 37 000, which passes every check. **BOTH readings are recorded and
> NEITHER is adopted over the other: the EAST position is a drawing convention, not a survey
> coordinate, and `U4` STAYS `[ASSUMED]`.**
>
> **And it costs the post its stated function.** One of the site package's five reasons for
> +X = east was *"the sentry post covers the approach from the north"*. With the post 10 m beyond
> the **far** end of the box it covers nothing — the approach is at the **west** end. **No stated
> rule fails, but a reviewer will ask.**

## 5.10 Every opening through the protective boundary

| Mark | Where | Leaf | Level | Rating | Class |
|---|---|---|---|---|---|
| **Blast Door 1** | **W6**, X 14800–15200 (400 thk), opening Y 600–1800 — stair shaft → Bay 6 | **1200 × 2100** | **(−)6.100** | **≥ 7 bar, gas-tight, rebound-rated** | `[C]` geometry · **the door itself is vendor data** |
| **Blast Door 2** | **W7**, X 18000–18400 (400 thk), opening Y 600–1800 — stair shaft → Bay 8 | **1200 × 2100** | **(−)6.100** | **≥ 7 bar** | `[C]` · vendor |
| Inner security door | **HW2**, headhouse north wall, X 14450–15350 | 900 × 2100 | (−)2.000 | **NOT blast rated** | `[C]` |
| Entry door | Entry stairwell headwall, X 9250–9500, **opens outward** | 1000 × 2100 | 0.000 | **NOT blast rated** — outside the boundary, expendable | `[C]` |
| **D-05, the W5 gas-tight door** | **W5**, X 12600–12800 | — | (−)6.100 | — | **RULED — ruling 9 (RC4): design it now.** W5 was designated *fire and gas-tight* with **no door anywhere in the project**, and escape route R1 has to cross it |
| W8 partition gaps ×4 | 3500–3610, 5410–5520, 9020–9130, 10930–11040 | **permanent 900 gap, Y 2500–3400** | (−)6.100 | **no doors, by design** | `[C]` |
| **ESC 1 / ESC 2 heads** | Bays 1 and 8, through the **pressure slab** | 1 400 dia bore | +0.150 / +0.700 | **1.54 m² hole in the protective boundary each** | See Part 10.5 |

> **Both blast doors ARE the protective boundary.** They sit in the same plane as W6/W7, and
> Finding F1 is why those walls are 400 thick: the shaft equalises to full `p_so`, so the doors and
> the walls beside them take the same **383 kPa**. Each frame is a **cast-in steel frame anchored
> into and welded to the cage**, which is both the blast fixing and the only EMP continuity the
> opening has.

# PART 6 — MATERIALS, DURABILITY AND DETAILING RULES

## 6.1 Concrete and reinforcement

| Item | Shelter / stairs / headhouse | Sentry post | Source |
|---|---|---|---|
| Concrete | **M35** | **M30** | IS 456 Table 5 — **M35 is the minimum for very severe exposure**, Table 3 |
| Free water / cement ratio | ≤ 0.45 | — | IS 456 Table 5 |
| Minimum cement content | ≥ 340 kg/m³ | — | IS 456 Table 5 |
| Admixture | Integral crystalline waterproofing | — | `[R]` |
| Blinding | M15, 100 thk | — | |
| Burster slab (in the cover) | M30, 200 thk | — | |
| Reinforcement | **Fe500D to IS 1786:2008** | Fe500 | |
| E<sub>c</sub> = 5000√f<sub>ck</sub> | **29 580 N/mm²** | **27 386 N/mm²** | IS 456 Cl. 6.2.3.1 |
| Poisson's ratio | 0.20 | 0.20 | `[A]` — standard; **closed by ruling 23 (RC6)** |
| Unit weight, reinforced concrete | 25 kN/m³ | 25 kN/m³ | IS 875 (Pt 1) Table 1 |
| γ<sub>m</sub> concrete / steel | 1.5 / 1.15 | same | IS 456 Cl. 36.4.2 |

> **Why Fe500D and not plain Fe500.** The **D** designation carries a guaranteed minimum
> elongation. A ductility ratio of 5 is claimed in the blast case (Part 2.2.3); claiming it on
> steel with no guaranteed elongation would be claiming it on nothing. The sentry post, which is
> not blast designed, uses Fe500.

## 6.2 Cover — IS 456 Cl. 26.4.2 / Table 16

| Face | Cover |
|---|---|
| Cast against blinding / trimmed rock | **75 mm** |
| Formed earth face | **50 mm** |
| Internal faces | **40 mm** |
| Stair shaft faces (wet / dirty zone) | 30 mm |
| Sentry post beams and slabs | **30 mm** |
| Sentry post columns | **40 mm** — Cl. 26.4.2.2, never less than 40 nor the bar diameter |
| Footings cast against earth | **50 mm** — Cl. 26.4.2.1 |
| **Maximum bar spacing, both curtains** | **150 mm — an EMP requirement**, stricter than IS 456 Cl. 26.3.3 |

> **The 5 mm cover reduction IS 456 Table 16 permits for M35 and above is deliberately not taken.**
> This structure is permanently below the design water table on a very severe exposure; 5 mm is not
> worth the argument.
>
> **And the 150 mm bar spacing is an EMP decision, recorded as one.** It is stricter than IS 456
> needs and it is carried in the master, in the structural CAD package, in eight bar bending
> schedules and on the drawings. Part 2.8.2 is the arithmetic behind it, and it is the reason the
> cage gives 99.99 dB at 10 kHz.

## 6.3 Development and lap lengths — IS 456 Cl. 26.2.1

```
Ld = phi . sigma_s / (4 . tau_bd),      sigma_s = 0.87 fy = 435 N/mm2
tau_bd  (Cl. 26.2.1.1):   M30 -> 1.5      M35 -> 1.7
         x 1.6 for deformed bars in tension
         / 0.8 (i.e. x 1.25) for bars in compression
```

| Grade | τ<sub>bd</sub> × 1.6 | **L<sub>d</sub> tension** | L<sub>d</sub> compression |
|---|---|---|---|
| M35 | 2.72 | **40 φ** | 32 φ |
| M30 | 2.40 | **46 φ** | 37 φ |

| Bar | L<sub>d</sub> M35 | Lap M35 | L<sub>d</sub> M30 | L<sub>d,c</sub> M30 |
|---|---|---|---|---|
| T8 | 320 | 400 | 368 | 296 |
| T10 | 400 | 500 | 460 | 370 |
| T12 | 480 | 600 | 552 | 444 |
| T16 | 640 | 800 | 736 | 592 |
| T20 | 800 | 1000 | 920 | 740 |
| T25 | 1000 | 1250 | 1150 | 925 |

**Lap policy.** IS 456 Cl. 26.2.5.1(c) gives lap = L<sub>d</sub> or 30 φ, whichever is greater
= 40 φ. Cl. 26.2.5.1 requires × 1.4 if more than 50 % of bars are lapped at one section.
**All laps are staggered so that ≤ 50 % are spliced at any section, and the lap is specified as
50 φ** — 25 % above requirement.

> **Blast bond bonus: refused.** IS 4991 Cl. 10.3.1.1 permits +25 % on bond, which would take
> L<sub>d</sub> to 32 φ. **Not taken. All detailing uses the static 40 φ** (Part 2.2.5).

## 6.4 Waterproofing and the tank

The structure is a **tanked box, not a drained one**. That single decision sets the entire water
strategy, and four rules follow from it:

1. **Nothing penetrates the roof.** No rainwater outlet, no vent stack, no soil stack through the
   2 000 mm cover — that would breach both the radiation mass and the roof membrane. **There is
   no downpipe on the buried roof and none is added.**
2. **One services envelope crossing.** The service entry plate. The sump rising main uses it; no
   second drainage penetration is created.
3. **Three streams, never combined.** Clean (seepage and condensate) → storm soakaway. Foul
   (peacetime) → septic tank → soak pit. Decon effluent → 1 000 L tank → **tanker only**.
4. **Drainage is not in the safety path.** No drainage failure may block egress, breach the
   envelope or flood an entrance.

| Element | Specification |
|---|---|
| Membrane | Continuous tank: on the blinding, turned up the external face, lapped to the roof membrane |
| Admixture | Integral crystalline waterproofing throughout |
| Construction joints (~6 m) | Reinforcement **fully continuous**, **two waterstops**, **and a welded Cu / galvanised EMP strap** |
| Movement joints | **NONE inside the protective envelope.** A movement joint is a guaranteed blast, gas **and EMP** discontinuity |
| Floor falls | Formed **in the screed, never cut into the 600 mm mat** — cutting them would reduce the section and the 75 mm cover to the bottom curtain |
| Pipe crossings | Puddle flange welded to the sleeve, membrane dressed and clamped to it |

> **The box is never drained to relieve groundwater.** A relief drain under the mat would defeat
> the tank and would not reduce uplift by design intent — the structure is held down by mass and
> by the staged construction sequence, not by pressure relief. **The only temporary relief
> permitted is the six construction-stage knock-out plugs**, grouted after backfill (Part 9.3).

# PART 7 — LOADING

## 7.1 Blast

```
DESIGN BASIS THREAT       nuclear air blast, p_so = 344.7 kPa (50 psi)       [C]
Positive phase duration   t_d = 0.13 to 1.33 s                               [C]
Reflected pressure        p_r = 1366 kPa                                     [C]
Dynamic pressure          q   = 282 kPa                                      [C]

Ductility ratio           mu = 5  (moderate, repairable damage)  IS 4991 Cl. 10.3.3
DLF = mu / (mu - 0.5)     5 / 4.5                                = 1.111
       validation: mu = 1 -> DLF = 2.00 = the elastic step-load factor

*** DESIGN BLAST PRESSURE   344.7 x 1.111                        = 383 kPa ***
       applied to the ROOF and to the WALLS   (K_a = 1.0, IS 4991 Cl. 7.2)

Roof natural period T     13.4 ms  ->  t_d/T = 10 to 100  ->  QUASI-STATIC

Dynamic material strengths, BLAST CASE ONLY   IS 4991 Cl. 10.3.1
       fck,dyn = 1.25 x 35 = 43.75 N/mm2     fy,dyn = 1.25 x 500 = 625 N/mm2
       NO dynamic increase on shear          IS 4991 Cl. 10.3.1.1
```

## 7.2 Gravity, soil and water

| Load | Value | Applied to | Source |
|---|---|---|---|
| Self weight, reinforced concrete | 25 kN/m³ | all | IS 875 (Pt 1) Table 1 |
| Roof self, 0.900 × 25 | **22.50 kPa** | roof | |
| Mat self, 0.600 × 25 | 15.00 kPa | mat | |
| **Engineered cover, 2 000 layered** | **40.65 kPa** | roof | `[C]` — Part 7.3 |
| Superimposed dead (services, finishes) | 2.0 kPa roof / 1.0 kPa mat | | `[R]` |
| Live load, internal floor | **5.0 kPa** — plant and storage, **not** 2.0 residential | floor | IS 875 (Pt 2) |
| Earth + water lateral gradient | K₀γ′ + γ<sub>w</sub> = 0.50 × 11.19 + 9.81 = **15.41 kPa/m** | walls | `[C]` derived |
| — at roof soffit (−)2.900 | 33.9 kPa | walls | |
| — at floor (−)6.100 | **83.2 kPa** | walls | |
| Hydrostatic uplift on the mat | 4.700 × 9.81 = **46.11 kPa**; total **6 289 kN** over 136.4 m² | mat | `[C]` |
| Construction surcharge | 20 kPa vertical / 10 kPa lateral | | `[A]` |
| Staircase, smeared on the two shaft walls | 2.947 kPa | W6 / W7 | `[C]` |

> Of the 15.41 kPa/m lateral gradient, **9.81 is water and only 5.60 is soil.** Water is nearly
> two-thirds of the lateral load. **This is why the groundwater level is the most important number
> the site investigation must confirm.**

## 7.3 The engineered cover — 2 000 mm, 40.65 kPa

| From the top | Thickness | Unit weight | Load kPa | Function |
|---|---|---|---|---|
| Topsoil / turf | 300 | 18 | 5.40 | **Concealment**, erosion, sheds rain |
| Granular filter | 150 | 19 | 2.85 | Stops fines clogging |
| **RC burster slab M30, T12 @ 150 B/W** | 200 | 25 | 5.00 | **Breaks up a penetrating item** |
| Crushed basalt rubble 25–75 mm | 500 | 17 | 8.50 | Scatters burster energy |
| Compacted engineered fill @ 95 % MDD | 750 | 20 | 15.00 | **Radiation mass** |
| Protection screed over the membrane | 100 | 24 | 2.40 | Protects the waterproofing |
| **Sum of the six layers** | **2 000** | | **39.15** | |
| **Declared allowance, held** | — | | **+1.50** | |
| **TOTAL — DESIGN VALUE** | **2 000** | | **40.65** | |

> **Conflict C17, ruled and closed.** The six layers sum to **39.15 kPa**; the table has always
> stated **40.65**, and the two never agreed. **40.65 is held as the design value** and the table
> now shows why: it is the layer sum **plus a declared allowance of 1.50 kPa**. That is the only
> choice that costs nothing and changes nothing — 40.65 is the number in the roof total, in the
> final register and in **`DL2` in every underground `.std` file**, it is the **larger** of the
> two, and adopting 39.15 instead would lighten the blast combination by 1.50 kPa and require a
> re-analysis that cannot be run here. **The allowance is not fabricated evidence: it is the
> difference the project has always carried, now stated instead of hidden.**

### 7.3.1 BS1 — the burster slab is laid to falls

By instruction the 200 mm burster slab is **no longer laid flat**. It is laid to a **1:50
crossfall, crowned on the box longitudinal centreline (Y = 3100) and falling each way to the box
edges** — that is, **parallel to the finished grade**, which is already recorded as *crowned,
falling 1:50 away*. Over the 3 100 mm half-width the slab drops **62 mm** from crown to box edge.

**Why.** The granular filter sits directly on the burster slab, and the drainage basis already
states that water infiltrating the topsoil is *"intercepted by the granular filter and dispersed
at the berm toe"*. **On a flat slab it cannot be** — it ponds on the slab and finds the
construction joints. The crossfall gives the filter layer the gradient that claim depends on.
**No pipe is introduced anywhere in the cover.**

**Thicknesses and load — unchanged.** The fall is taken up entirely in the **compacted engineered
fill** below the rubble, which is **750 nominal at the crown thinning to 688 at the box edge**.
Every other layer keeps its nominal thickness. **The cover therefore weighs exactly what it weighs
today at the crown, and less toward the edges: the cover load does not increase anywhere.**

## 7.4 Total roof load — combination 103

| Component | kPa |
|---|---|
| Blast, 344.7 × 1.111 | 383.00 |
| Engineered cover | 40.65 |
| Superimposed dead | 2.00 |
| Self weight | 22.50 |
| **TOTAL w** | **448.15** |

**Live load is excluded — IS 4991 Cl. 11.2**: *"No live load shall be considered on roof at the
time of blast."*

```
Static ULS on the roof (COMB 101)
   1.5 x (40.65 + 2.0 + 22.5 + 20) = 127.7 kPa

BLAST GOVERNS 448.15 / 127.7 = 3.51 : 1
```

## 7.5 Headhouse loads

| Element | Load | Basis |
|---|---|---|
| Roof (flush horizontal at the berm crest) | **396.5 kPa** = 383 blast + 12.5 self + 1.0 SIDL | IS 4991 Cl. 7.2 |
| **Walls — CURRENT** | **383 kPa, acting EITHER FACE** | **Conflict C10** |
| Walls — earlier basis (superseded) | 113 kPa = C<sub>d</sub>·q = 0.4 × 282 | IS 4991 Cl. 7.4 |

> **Conflict C10 and why the upgrade was taken.** The walls sit behind ~2.5 m of berm and **earth
> transmits pressure.** `K_a` for dry compacted fill is an assumption that cannot be verified, so
> the walls are designed for **the full 383 kPa upper bound.** **Cost of the upgrade: one link
> cage, T12 4-leg @ 250. Utilisation rises 17 % → 59 %.** That is what removing an unverifiable
> assumption from the critical path is worth, and it is cheap. Owner ruling 23 (RC6) confirms the
> choice and closes assumption `A6`.
>
> **And the pressure acts from inside too.** The inner security door is not blast rated and the
> entry stairwell is expected to be lost, so **the headhouse fills and the walls are pushed
> outwards.** They are reinforced symmetrically for 383 kPa either way — *a stated requirement,
> not an accident of detailing.*

## 7.6 Entry stairwell loads — static only, NOT blast rated

| Element | Load |
|---|---|
| Flight, waist 250 | waist 7.150 + steps 2.083 + finishes 1.000 + LL 5.000 = 15.233 → **w<sub>u</sub> = 22.85 kPa** |
| Side walls 250 | K₀ 0.50 × 20 × 2.9 + 0.5 × 10 surcharge = **34 kPa at base** |
| Raking roof 250 | self 6.25 + waterproofing 2.0 + earth lap 5.4 + **imposed 20** = 33.65 → **w<sub>u</sub> = 50.5 kPa** |
| Top landing 250 | 18.4 + flight reaction 36.5 = **54.9 kPa** |

> **The 20 kPa imposed load on the raking roof is deliberate: it is there for a stray vehicle on
> the berm.** It is not a code minimum and it is not an accident.

## 7.7 Sentry post loads

| Item | Value | Verification |
|---|---|---|
| Slab dead, first floor | 4.750 kPa | 0.150 × 25 + 1.0 finish |
| Slab dead, roof | 5.250 kPa | 3.75 + 1.5 screed / waterproofing |
| Imposed, first floor | 3.000 kPa | IS 875 (Pt 2), observation post |
| Imposed, roof | 1.500 kPa | IS 875 (Pt 2), accessible |
| Peak two-way intensity, DL floor | 8.669 kN/m | 4.75 × 1.825 |
| Peak two-way intensity, DL roof | 9.581 kN/m | 5.25 × 1.825 |
| Peak two-way intensity, LL floor | 5.475 kN/m | 3.00 × 1.825 |
| Peak two-way intensity, LL roof | 2.737 kN/m | 1.50 × 1.825 |
| Infill on the first-floor beams | **13.000 kN/m** | 0.200 × 2.600 × 25 — **retained after SP-B1 because brick is lighter (≈ 9.88) and the modelled value is therefore conservative** |
| Roof projection + parapet | 4.162 kN/m | `[C]` as drawn — **half re-derived, see below** |
| — parapet term, 0.300 × 0.150 × 25 | **1.125 kN/m** | **`[C]`, reproduces exactly** |
| — roof projection term | **3.037 kN/m** | **`[N]` — the projection dimension is recorded nowhere** |
| w<sub>u</sub> floor = 1.5(4.75 + 3.00) | **11.625 kPa** | **governs the slab** |
| w<sub>u</sub> roof = 1.5(5.25 + 1.50) | 10.125 kPa | |

> **`U8-F1` — the parapet confirmation is necessary but not sufficient.** Ruling 15 (RC4)
> confirmed the parapet at 300 × 150, and 0.300 × 0.150 × 25 = **1.125 kN/m** reproduces exactly.
> The residual **3.037 kN/m** is the roof projection, and **the projection dimension is recorded
> nowhere in this project.** Back-solving gives 810 mm (slab alone) or 578 mm (slab + finish);
> **neither is round, neither is drawn, neither is adopted. 4.162 continues to be used as given —
> no member force changes.**

**Load path to the beams — IS 456 Cl. 24.5, 45° yield lines:**

```
Peak intensity on any beam = w x short span / 2 = w x 3.650/2 = w x 1.825 m
SHORT beams B1 (3650 long) -> TRIANGLE
LONG  beams B2 (4650 long) -> TRAPEZOID
     w_eq = w_peak x [ 1 - 1/(3 r^2) ],   r = 4650/3650 = 1.2740
     1 - 1/(3 x 1.2740^2) = 0.79463  ->  0.7946 adopted
```

> The trapezoid factor **is exact**; using the same factor for both bending moment and fixed-end
> moment is the simplification, and it is worth **≈ 2 %** on B2's support moment, inside its 89 %
> utilisation. **Closed by owner ruling 24 (RC6), accepted on the margin** — assumption `A12`.

## 7.8 Seismic and wind

### 7.8.1 Underground box — IS 1893 (Part 1):2016

```
Z = 0.16 (Zone III)     I = 1.5     R = 4.0     Sa/g = 2.5
Ah = (Z/2)(I/R)(Sa/g) = 0.08 x 0.375 x 2.5                      = 0.075
W  = 14 002 kN   ->   Vb = 0.075 x 14 002                        = 1050 kN
Per long wall 525 kN
   tau = 525e3 / (600 x 0.8 x 21600)                             = 0.063 N/mm2
                                                        NEGLIGIBLE
IS 13920 Cl. 10.4 boundary elements CHECKED and NOT TRIGGERED
```

### 7.8.2 Sentry post — IS 1893 (Part 1):2016

```
Z = 0.16   I = 1.5   R = 3.0   Sa/g = 2.5  (rock, T on the plateau)
   R = 3.0 because the infill panels are NOT separated from the frame.
   R = 5.0 would require a special moment-resisting frame with positively
   separated infill, which this project does not claim.
Ah = 0.08 x 0.50 x 2.5                                           = 0.100

Fundamental period -- all three estimates land inside 0.10-0.40 s,
so Sa/g = 2.5 regardless of which is used:
   bare RC MRF, Cl 7.6.2       Ta = 0.075 h^0.75
                                  = 0.075 x 6.250^0.75           = 0.297 s
   with infill, Cl 7.6.2(c)    Ta = 0.09 h / sqrt(d)
                                  X 0.281 s        Z 0.252 s

HAND-CALCULATED seismic weight
   Roof  +6.700 : slab 89.1 + parapet/projection 69.1 + beams 31.1
                  + half-columns 18.7 + half first-storey infill 107.9  = 315.9 kN
   Floor +3.650 : slab 80.6 + beams 31.1 + columns 38.3
                  + half ground-storey infill 114.1 + 25 % LL 12.7      = 276.8 kN
   TOTAL W = 592.7 kN    ->   Vb,hand = 0.100 x 592.7                   = 59.3 kN

*** STAAD MODEL VALUE, WHICH GOVERNS DESIGN:  Vb = 73.18 kN ***
   stated in the load-case titles and CONFIRMED by the reactions:
   Fx = 18.295 kN per column x 4                                        = 73.18 kN
```

> **Conflict C9 — and it is now fully explained rather than merely adopted.** The model prints its
> own seismic-weight summary: roof 331.46 + floor 400.34 = **W = 731.80 kN**, and
> V<sub>b</sub> = 0.100 × 731.80 = 73.18 kN returns A<sub>h</sub> = **0.1000 exactly.** Rebuilding
> both storey weights from the model's own load blocks reproduces 331.46 and 400.34 to the
> kilonewton, **and the 139.1 kN gap to the hand check resolves completely**:
>
> - **107.9 kN** is half the first-storey infill, which the hand check's floor line does not
>   allocate;
> - **31.1 kN** is the model taking the full 450 mm beam depth in `SELFWEIGHT` while also applying
>   the full slab pressure, where the hand check nets the beam to 300 mm.
>
> **Nothing is unexplained, and every member is already designed to the higher value.**

### 7.8.3 Wind on the sentry post — IS 875 (Part 3):2015

```
Vb = 39 m/s (Pune)   k1 = 1.08 (100-yr, Table 1)   k2 = 1.00 (Cat 2, 10 m)
k3 = k4 = 1.00
Vz = 39 x 1.08                                                   = 42.12 m/s
pz = 0.6 Vz^2                                    Cl 7.2          = 1.065 kPa
pd = pz x Kd 0.90 x Ka 0.897 x Kc 1.0                            = 0.859 kPa
F  = Cf 1.3 x Ae (4.0 x 6.7 = 26.8 m2) x pd                      = 29.9 kN

SEISMIC 73.18 kN   vs   WIND 29.9 kN   ->   SEISMIC GOVERNS 2.4 : 1
```

> `k1` = 1.08 assumes a 100-year design life `[A]`. **Closed by owner ruling 23 (RC6), accepted:**
> a 100-year life on a load path that seismic already beats 2.4 : 1 costs nothing.

## 7.9 Load combinations

### 7.9.1 Underground box — five combinations, matching the STAAD model

| No. | Title | Factors |
|---|---|---|
| 101 | ULS static | 1.5 (DL + SIDL + LL + SOIL + UPLIFT) |
| 102 | ULS uplift | 0.9 DL + 1.5 UPLIFT |
| **103** | **BLAST** | **1.0 (DL + SIDL + SOIL + UPLIFT + BLAST)** ← **governs every element** |
| 104 | SLS crack width | 1.0 (DL + SIDL + LL + SOIL + UPLIFT), IS 3370 Pt 2 |
| 105 | Construction | 1.5 (DL + SOIL + UPLIFT + SURCHARGE) |

> **γ = 1.0 on blast** because it is an extreme event checked against **ultimate** capacity with
> **dynamic** material strengths (IS 4991 Cl. 10.3.1). Applying 1.5 while also taking the 25 %
> material bonus would be inconsistent (Part 2.2.6).
>
> **Wind and earthquake are absent from 103 — IS 4991 Cl. 11.1** forbids combining them with blast.

### 7.9.2 Sentry post — sixteen combinations, read from the `.std` file

| No. | Combination |
|---|---|
| 101 | 1.5 DL + 1.5 LL |
| 102–105 | 1.2 DL + 1.2 LL + 1.2 EQ (±X, ±Z) |
| 106–109 | 1.5 DL + 1.5 EQ (±X, ±Z) |
| 110–113 | 0.9 DL + 1.5 EQ (±X, ±Z) |
| 201 | 1.0 DL + 1.0 LL — SERVICE |
| **202 · 203** | 1.0 DL + 1.0 EQ+X · 1.0 DL + 1.0 EQ+Z — **DRIFT CHECK, IS 1893 Cl. 7.11** |

> **A correction worth recording.** This table used to read *"15 combinations"* and stopped at
> 202, on the authority of the screen captures. **The `.std` file itself carries sixteen
> `LOAD COMB` cases — 203, the second drift check, was missing from the master.** No combination
> factor, member force or bar changes: 203 is a serviceability drift check that was already in the
> model being designed to. **The file is primary; the screenshots were not.**

# PART 8 — ANALYSIS MODELS

## 8.1 What the models are, and what they are not

> **STAAD.Pro is not available in this environment. No analysis has been run in this project and
> no result — moment, displacement, shear or reaction — exists for the underground box or for the
> three mesh models.** Editing, reconciling and validating a `.std` file is **not** running an
> analysis and is never reported as one.
>
> **Every underground design value in Parts 9 and 10 was produced by hand calculation**, to
> IS 456 with IS 4991 loading rules. The model supplies the demand distribution and the visual
> check that loads are applied to the correct faces. **For the sentry post, only the *forces* were
> taken from the model** — the base shear and the seismic axial couples — and no STAAD concrete
> design output was relied upon anywhere.

## 8.2 Model inventory

| Model | File in `current/staad/` | Role | Status |
|---|---|---|---|
| **Underground box — reference** | `Underground_Structure_WITH_LOADS_worked_example (4).STD` | The reconciled Phase 2 Rev A + M1 plate model. **Every box value in Part 9 is checked against it** | `[C]` |
| **Sentry post** | `Sentry_Post_Framed_Seismic.std` | Two-storey RC frame, seismic | `[C]` |
| **Entry stairwell** | `Entry_Stairwell.std` | Covered approach stairwell, **static only, not blast rated** | `[C]` |
| Underground box — COARSE | `Underground_Shelter_Mesh_Coarse.std` | Mesh study — **324 joints, 336 plates** | `[C]` |
| Underground box — MEDIUM | `Underground_Shelter_Mesh_Medium.std` | Reference mesh — **1 113 joints, 1 138 plates** | `[C]` |
| Underground box — FINE | `Underground_Shelter_Mesh_Fine.std` | h/2 refinement — **4 500 joints, 4 552 plates** | `[C]` |
| Underground box — **k<sub>s</sub> upper bound** | `Underground_Shelter_ks500000.std` | The reference model at **k<sub>s</sub> = 500 000**; `ELASTIC MAT SUBGRADE` and the four corner `KFY` (× 5) are **the only lines that differ**, verified by diff | `[C]` |

**Units:** metres and kilonewtons throughout. **Coordinate system:** STAAD global — **Y is
vertical**, X and Z horizontal.

> **The underground model's datum is not the project datum.** It uses **mid-surface** geometry and
> its origin `Y = 0` is at the **underside of the mat**, real level (−)6.700.
>
> **`project level = model Y − 6.700`.** Apply the offset before comparing any model output to a
> drawing. Y = 0.300 is the mid-plane of the 600 mat; Z = 0.300 and Z = 5.900 are the mid-planes
> of the 600 perimeter walls; X = 0.300 is the mid-plane of the west end wall.

## 8.3 The underground box model

**Form.** A **plate + beam mid-surface model** of the whole box — mat, four perimeter walls,
internal walls and the pressure slab — meshed on a regular grid over the full 22 × 6.2 m
footprint, with support symbols at every mat node.

| | |
|---|---|
| Shell elements | **1 138**, in four thickness groups: mat 600 / roof 900 / perimeter 600 / internal 200–400 |
| Supports | `ELASTIC MAT DIRECT Y SUBGRADE 100000` — vertical springs on every mat node, generated from k<sub>s</sub> |
| Corner joints | Explicit `KFY` restated per corner from the post-M1 tributary areas: **6 891 / 8 269 / 7 219 / 8 663 kN/m** |
| Analysis command | `PERFORM ANALYSIS PRINT STATICS CHECK` — **no P-Delta** |

**Load cases, read verbatim from the file:**

| # | Title | Value |
|---|---|---|
| 1 | `DL1 SELF WEIGHT` (`SELFWEIGHT Y -1`) | auto |
| 2 | `DL2 EARTH COVER ON ROOF 40.65 KN/M2` | 40.65 kPa |
| 3 | `DL3 SIDL SERVICES AND FINISHES` | 2.0 kPa |
| 4 | `LL1 LIVE LOAD ON INTERNAL FLOOR` | 5.0 kPa |
| 5 | `DL4 STAIRCASE ON THE TWO SHAFT WALLS` | 2.947 kPa |
| 6 | `EP1 EARTH + WATER ON EXTERNAL WALLS` | 33.9 → 83.2 kPa |
| 7 | `HY1 HYDROSTATIC UPLIFT ON MAT` | 46.11 kPa |
| 8 | **`BL1 BLAST ON ROOF 383 KN/M2`** | **383 kPa** |
| 9 | **`BL2 BLAST ON EXTERNAL WALLS 383 KN/M2`** | **383 kPa** |
| 10 | `LL2 CONSTRUCTION SURCHARGE` | 20.0 kPa |
| **11** | **`BL3 BLAST IN THE STAIR SHAFT ON W6 AND W7 383 KN/M2`** | **383 kPa, acting out of the shaft on both faces** |

> **Load case 11 is Modification M1, expressed as a load.** The model previously applied blast to
> the **external** walls only. `BL3` is the demand Finding F1 identified — the stair shaft
> equalises to full `p_so` and therefore loads W6 and W7 from inside — and it is included in
> combination 103. **M1 exists to carry this case.**

### 8.3.1 The modelling warning that must not be lost

> **Spring supports in STAAD take tension unless explicitly declared compression-only.** In this
> model the mat therefore **never lifts**, in any load case. **The flotation check of Part 9.3
> cannot be performed in STAAD and is not.** It is a hand calculation on real dimensions and real
> weights. *Anyone who says "the analysis shows no uplift" has misunderstood their own model.*

## 8.4 The sentry post model

| | |
|---|---|
| Joints | **Twelve** — base 1, 2, 11, 12 at Y = +0.450; first floor +100; roof +200 |
| Members | **16** — 1–8 columns `PRIS YD 0.35 ZD 0.35`; 9–16 beams `PRIS YD 0.45 ZD 0.25` |
| Supports | `1 2 11 12 FIXED` — **all four column bases fully fixed** |
| **Member releases** | **NONE. The command appears nowhere in the file** — every beam–column joint is fully continuous, which is what a moment frame requires and what the portal-method forces in Part 11.1 assume |
| Infill | Modelled as **`MEMBER LOAD` only**, never as a strut |
| Slab S1 | **Not modelled as plates** — the slab load is applied to the beams as triangular / trapezoidal loading |
| Analysis command | `PERFORM ANALYSIS PRINT STATICS CHECK` — **no P-Delta** |

**Fixed bases are justified, not assumed:** the columns sit on isolated footings **on in-situ
rock**. Rotational restraint is real. **On backfill it would not be defensible** — which is
precisely why the post is sited ≥ 10 m clear of the shelter excavation.

**The statics check passes in every case** — difference between loads and reactions = 0.000.

| L/C | ΣF<sub>x</sub> | ΣF<sub>y</sub> | ΣF<sub>z</sub> | ΣM<sub>x</sub> | ΣM<sub>y</sub> |
|---|---|---|---|---|---|
| 1 (DL) | 0.000 | **−624.548** | 0.000 | 1561.369 | 0.000 |
| 2 (LL) | 0.000 | **−76.376** | 0.000 | 190.941 | 0.000 |
| 3 (EQ+X) | **73.180** | 0.000 | 0.000 | 0.000 | 182.950 |
| 5 (EQ+Z) | 0.000 | 0.000 | **73.180** | 436.631 | −146.360 |

**Two confirmations taken from the reaction table and used directly in design:**

```
1   Fx = 18.295 kN per column x 4 = 73.18 kN
    -- the portal-method distribution used in design is EXACTLY what the
       model produces.
2   Fy = +/- 36.127 kN (EQ+X)  and  +/- 27.891 kN (EQ+Z)
    -- these ARE the seismic axial couples used in the column design.
       They were READ from the model, not calculated by hand.
```

**And one difference, stated rather than smoothed over.** Back-calculating the model's own vertical
distribution from its load resultants gives Q<sub>roof</sub> = 55.57 kN and Q<sub>floor</sub> =
17.61 kN, against the hand `Wh²` distribution's 59.51 and 13.67. **The design used the hand
distribution at the model's total of 73.18 kN, which gives the LARGER ground-storey column moment.
Conservative, and recorded.**

## 8.5 Mesh sensitivity — MS1

Three mesh-density variants of the reconciled M1 model were built: **COARSE** (~1.9 × the
reference element size), **MEDIUM** (an unmodified copy of the reference mesh) and **FINE** (an
exact h/2 refinement).

Geometry — including every M1 value — thicknesses, materials, supports and soil springs, loads,
load cases and combinations are **identical in all three**; only the plate mesh density differs.
The opening boundaries and the footprint are pixel-identical across all three: **net roof area
104.048 m² and hole area 15.792 m² match exactly.** Corner spring `KFY` values and the `EP1`
earth-plus-water row pressures were **re-derived per mesh from the same physical formulas the
reference model itself encodes** —

```
KFY = k_s x A_trib
EP1 p = 15.4071 x depth - 10.8198  kN/m2,   depth = 6.700 - Y
      fitted from the reference model's own six data points, residual <= 0.01
```

— **not re-guessed.**

> **The convergence conclusion is OUTSTANDING.** The three models are built and validated;
> **STAAD.Pro is not available, so no result exists for any of them.** Saying the mesh converges
> would be inventing the study's conclusion.

## 8.6 MS2 — the input-file corrections, and why they matter

The project owner ran the COARSE model in STAAD.Pro — **the first time any model in this project
had been opened in STAAD** — and it reported errors. All four box models were then re-read line by
line.

| # | Defect | Fix |
|---|---|---|
| **MS2-1** | **Three `LOAD 6` south-wall lines were 80 columns against the file's own `INPUT WIDTH 79`.** STAAD reads 79 columns and discards the rest, so it read **−77.6 / −57.3 / −37.0** where the file says **−77.64 / −57.36 / −37.07**. The north wall (79 columns) was read correctly, so **`LOAD 6` no longer balanced** — 4 848.4 kN in +Z against 4 843.6 kN in −Z, an out-of-balance of **4.8 kN on a case that is self-equilibrating by construction**, and the file asks for exactly the statics check that reports it | Split on the STAAD `-` continuation character. **Every data line in all four box models is now ≤ 79 columns** |
| **MS2-2** | `LOAD 10` was defined **after** `LOAD 11` in all four models, so the primary case numbers ran 1…9, 11, 10 | Reordered. **Physically neutral** — combinations reference cases by number and 101–105 are byte-identical before and after |
| **MS2-3** | Corner spring `KFY` at joint 1 was **27 562** where the model's own formula gives **27 562.5** and the study documentation gives **27 563**, while the sibling half-value was rounded **up** | **27 563.** A 0.5 kN/m difference on one spring; the point is that the file now agrees with its own documentation |
| **MS2-4** | A load title and one `JOB CLIENT` line also exceeded 79 columns (titles only, no numeric consequence) | Shortened |

**Verified after the edits, on all four box models:** the 336 / 1 138 / 4 552-plate topology is
unchanged and clean — every element resolves to defined joints, no repeated node, no degenerate or
non-planar quadrilateral, no duplicate coordinate or element, no unused joint, no gap in the
numbering; every joint still satisfies the model's own numbering rule; and, **re-read as STAAD
reads them at 79 columns, COARSE, MEDIUM and FINE now produce identical panel-by-panel load
resultants for all eleven load cases** — mat, roof, each of the four external walls, W6 and W7 —
**which they did not before.**

> **MS2 changed no analysis model.** No geometry, thickness, material, support stiffness, load
> magnitude, load case number or combination factor moved. **It is a lesson about input files, and
> it is the kind of defect that only shows up when someone actually opens the model.**

## 8.7 What must be obtained before the STAAD work can be extended

1. **A STAAD.Pro run.** Everything below waits on it.
2. The underground model's **post-processing output** — plate M<sub>x</sub>/M<sub>y</sub>, support
   reactions, deflections.
3. The **mesh convergence table**, which is the conclusion MS1 exists to produce.
4. **Both k<sub>s</sub> bounds run** — the upper-bound model exists and has never been executed.
5. The **sentry post re-run after SP-B1** (`WM-V6`) — confirmation, not risk: brick is lighter than
   the modelled infill, so every member is over-designed.

# PART 9 — STRUCTURAL DESIGN CALCULATIONS: THE UNDERGROUND BOX

> **Every value in Parts 9 to 11 has been computed numerically in this project, and the drawings
> carry exactly this reinforcement. No drawing shows an arrangement that differs from these
> calculations.**

**The flexure equations used throughout — IS 456 Annex G-1.1(b) and Cl. 38.1:**

```
Mu     = 0.87 fy . Ast . d . [ 1 - (Ast . fy) / (b . d . fck) ]
xu     = 0.87 fy Ast / (0.36 fck b)                        IS 456 Cl. 38.1
xu,max / d = 0.46 for Fe500                                IS 456 Cl. 38.1(f)
Mu,lim = 0.133 fck b d^2                                   IS 456 Annex G-1.1(c)
```

**Notation:** `T16 @ 150 EF EW` = 16 mm Fe500D deformed bars at 150 mm centres, **E**ach **F**ace,
**E**ach **W**ay. `4L` = four-legged links.

## 9.1 Perimeter walls W1–W4 — 600 thk — 68 %

```
INPUTS      t 600, clear height 3200, cover 75 earth / 40 internal, T16
            d = 600 - 75 - 8                                     = 517 mm
            Blast 383 kPa (Ka 1.0); static earth+water 83.2 kPa at base
            -> BLAST GOVERNS 4.6 : 1

FORMULA     Mp = w . Ln^2 / 16       (fixed-fixed plastic mechanism)
SUBSTITUTE  Mp = 383 x 3.200^2 / 16
RESULT      Mp                                                   = 245.1 kNm/m

CHECK       Mu,lim = 0.133 x 43.75 x 1000 x 517^2                = 1556 kNm/m
                                                     -> singly reinforced  OK
            Ast,req  (fy,dyn 625, fck,dyn 43.75)                 = 894 mm2/m
            IS 456 Cl. 32.5(a) min vertical   0.0012 x 600       = 720 mm2/m
            IS 456 Cl. 32.5(b) min horizontal 0.0020 x 600       = 1200 mm2/m
            IS 3370 Pt 2 surface zone 0.35 % x 250 each face     = 875 mm2/m/face

ADOPTED     T16 @ 150 c/c EACH FACE EACH WAY                     = 1340 mm2/m
            Mu = 362.8 kNm/m   ->   UTILISATION 68 %
            xu = 46.3  ->  x/d = 0.089   <<  0.46

SHEAR       V at d  = 383 (1.600 - 0.517)                        = 414.8 kN/m
            tau_v = 414.8e3 / (1000 x 517)       Cl. 40.1        = 0.802 N/mm2
            pt = 0.259 %  ->  tau_c (Table 19, M35)              = 0.375 N/mm2
            tau_c,max (Table 20, M35) 3.70 > 0.802  OK           Cl. 40.2.3
            Vus = (0.802 - 0.375) x 517                          = 220.8 kN/m
            Asv/sv = 220800 / (0.87 x 500 x 517)  Cl. 40.4(a)    = 0.982 mm2/mm
              -> T12 2-leg at 230
            Cl. 26.5.1.5 limit min(0.75d = 388, 300)             = 300
ADOPTED     T12 CLOSED LINKS @ 200 c/c        (Asv/sv = 1.131  OK)

AXIAL       N = 448.15 x 2.50 + 3.2 x 0.6 x 25                   = 1168 kN/m
            f = 1.95 N/mm2 = 11 % of 0.4 fck,dyn (17.5)
                                              -> P-M not critical

CRACK       IS 3370 Pt 2, limit 0.2 mm; surface steel 875 < 1340   OK
```

> **Why 600 mm, stated honestly.** The wall is **not strength-governed** — it is 68 % utilised.
> 600 mm is set by five things at once, and none of them is bending:
>
> 1. **75 mm cover** against blinding and trimmed rock;
> 2. **congestion** — two curtains, closed links, waterstops and cast-in frames all in one section;
> 3. **IS 3370 crack control** under sustained hydrostatic load;
> 4. **the EMP double curtain at 150 mm** (Part 2.8.2);
> 5. **the 1 168 kN/m axial path** from the roof.
>
> Saying so matters: an optimiser who sees 68 % and thins the wall loses four of the five reasons
> it is that thick.

## 9.2 Walls W6 / W7 — 400 thk — Modification M1 — 69 %

### 9.2.1 Finding F1 — why these two walls are different

```
FINDING F1  The stair shaft is open to atmosphere through the 2800 x 3160 roof
            void, the headhouse and the entry stairwell.

            Fill time  V / (A . c) = 105 / (3.3 x 340)            = 0.094 s
            against the positive phase duration t_d  0.13 - 1.33 s

            -> THE SHAFT EQUALISES TO FULL p_so, and it does so in well under
               one t_d.

            W6 and W7 therefore sit in the SAME PLANE as the 7-bar blast doors,
            separating a PRESSURISED shaft from Bay 6 / Bay 8 at AMBIENT.
```

> **That is the whole of Modification M1 in one paragraph.** The protective boundary was not
> continuous: two 200 mm walls were standing where 7-bar doors stand. **The design does not
> pretend the shaft stays at ambient; it accepts that it fills and carries the consequence.**

### 9.2.2 Why 200 mm is impossible — not a detailing problem

```
            d = 200 - 40 - 6                                     = 154 mm
            Mu,lim = 0.133 x 43.75 x 1000 x 154^2                = 138.0 kNm/m
            Demand Mp = 383 x 3.200^2 / 16                       = 245.1 kNm/m

            138 < 245   ->   NO STEEL RATIO MAKES IT WORK

            Two-way action was CHECKED BEFORE REJECTION:
            panel 3200 x 3800, fixed on three edges, yield line
                 ~ 0.7 x one-way = 172 kNm/m   -- still above 138.
```

> **The section is over its singly-reinforced capacity before any steel is chosen.** This is the
> one place in the project where the answer was not "add bars" but "change the geometry" — and it
> is why M1 is a **modification**, not a detailing revision.
>
> **And the 400 mm could not be found anywhere convenient.** It could not come out of Bay 8,
> because the 750 mm escape-shaft clearance rule (Part 5.6) fixes Bay 8's minimum width at
> 2 900 mm. It could not come out of the shaft, because 2 800 = 2 × 1 200 flights + 200 well
> exactly. **So the box got 400 mm longer**, which the one-way roof makes structurally free
> (Part 5.3).

### 9.2.3 Design of the 400 mm wall

```
            d = 400 - 50 (shaft face) - 8                        = 342 mm
            Mp = 383 x 3.200^2 / 16                              = 245.1 kNm/m
            Mu,lim = 0.133 x 43.75 x 1000 x 342^2                = 680.6 kNm/m  OK
            Ast,req                                              = 1400 mm2/m

ADOPTED     T20 @ 150 EF EW                                      = 2094 mm2/m
            Mu = 355.3 kNm/m   ->   UTILISATION 69 %,  x/d = 0.211

SHEAR       V at d = 383 (1.600 - 0.342)                         = 481.8 kN/m
            tau_v 1.409  |  tau_c 0.540 (pt 0.612 %)  |  tau_c,max 3.70   OK
            Vus 297.2 kN/m ;  Asv/sv 1.998  ->  T12 4-leg at 226
            Cl. 26.5.1.5 limit min(0.75d = 257, 300)             = 257
ADOPTED     T12 4-LEGGED LINKS @ 200 c/c

BLAST DOOR OPENING  1200 x 2100
            Interrupted steel 2094 x 1.2 = 2513 mm2/face
                                       -> 1256 each jamb
ADOPTED     4 No. T20 EACH JAMB EACH FACE (1257 mm2), anchored Ld 800 beyond

HEADER      400 x 1100 over 1200 clear
            w = 383 x 2.1/2                                      = 402 kN/m
            M = w L^2 / 12                                       = 48.2 kNm
            V = 241 kN ;  tau = 0.578 N/mm2
ADOPTED     4-T20 TOP + 4-T20 BOTTOM, T12 4-leg links @ 150

FRAME       Cast-in steel frame anchored into and WELDED to the cage (EMP).
            Door: proprietary, >= 7 bar, rebound-rated, gas-tight   [vendor]
```

## 9.3 Mat foundation — 600 thk — 84 %, the most heavily worked element

### 9.3.1 Bearing governs nothing

```
BEARING     Service 58.4 kPa  = 1.8 % of 3240 kPa
            Blast  404.9 kPa  = 12.5 %          (20.6 % on the measured
                                                 soaked value -- Part 4.3.2)
            BEARING GOVERNS NOTHING.
```

### 9.3.2 Two flexural cases, and the second one sizes the mat

```
CASE 1 -- NET UPLIFT (COMB 102)
            u = 4.700 x 9.81                                     = 46.11 kPa
            self 0.600 x 25                                      = 15.00 kPa
            net 31.1 kPa UP over the 5000 clear span
            Mp = 31.1 x 5.0^2 / 16                               = 48.6 kNm/m
                                                                   NOMINAL

CASE 2 -- SOFT / RED-BOLE ZONE            *** GOVERNS ***
            A 3.0 m band of red-bole or vesicular material removed,
            at the WORST POSITION.
            q = 404.9 kPa (blast bearing) over a 3.0 m unsupported span
            M = q . L^2 / 12 = 404.9 x 9 / 12                    = 303.7 kNm/m
            d = 600 - 75 - 8                                     = 517 mm
            Ast,req                                              = 1115 mm2/m
ADOPTED     T16 @ 150 EF EW = 1340 mm2/m
            Mu = 362.8 kNm/m   ->   UTILISATION 84 %

THICKNESS STUDY
            500 -> Ast,req 1407 = 105 % of provided        FAIL
            600 -> 1115 =  84 %                            ADOPTED
            700 ->  926 =  70 %
            800 (as once drawn) ~ 57 %  =  33 % unused reserve
```

> **Case 2 is the geology, expressed as a load case.** The flow contacts in a Deccan Trap sequence
> are exactly where a soft seam sits, and a single red-bole band under the mat removes support over
> its width. **That case, not bearing and not uplift, is what sets the 600 mm mat and its
> T16 @ 150 EF EW.** It is also why Part 4.2.2's unlogged 5.3 m matters so much: **the case that
> sizes the mat is a case nobody has looked for at the founding horizon.**

### 9.3.3 One-way shear — conflict C6, and the link grid it produced

```
ONE-WAY SHEAR -- NOT CHECKED IN THE PHASE 1 REPORT (CONFLICT C6)
            V at d from the soft-band edge
              = 404.9 (1.500 - 0.517)                             = 398.0 kN/m
            tau_v 0.770 | tau_c 0.375 (pt 0.259 %) | tau_c,max 3.70   OK
            *** tau_c read at the STATIC M35 value --
                IS 4991 Cl. 10.3.1.1 gives NO dynamic increase on shear ***
            Vus = 204.2 kN/m ;  Asv/sv                            = 0.908 mm2/mm

ADOPTED     T12 CLOSED LINKS ON A 250 x 250 GRID THROUGHOUT
            supplied Asv/sv = (4 x 113.1) / 250 = 1.810 = 2.0 x required
            -- and the grid DOUBLES AS THE SPACER SYSTEM between the two curtains
```

### 9.3.4 The checks that do not apply, declared rather than ignored

| Check | Verdict |
|---|---|
| **Punching**, IS 456 Cl. 31.6 | **NOT APPLICABLE.** No column or pedestal bears on the mat; the headhouse walls bear on the **roof**. *Declared, not ignored* |
| **Sliding** | The box is socketed ~4.8 m into basalt (5.3–5.9 m on the measured rockhead) with the 300 mm annulus backfilled in M15 lean concrete. **Not a credible mechanism** — the reasoning is stated and **no spurious factor of safety is computed** |
| **Overturning** | Buried box 22.0 × 6.2 × 4.7 m under a symmetrical lateral load. **NOT APPLICABLE** |
| **Settlement** | Negligible on sound basalt, IS 12070 Cl. 6 — and Part 2.5.3 gives the physical reason. **The hazard is the flow contacts, not the settlement** |

### 9.3.5 Flotation — the construction stage governs

```
| Stage                        | Weight    | Uplift   | FoS @ (-)2.000 | FoS flooded |
| 1  mat cast only             |  2 009 kN | 6 175 kN | 0.33  FAIL     | 0.23 FAIL   |
| 2  mat + walls, no roof      |  4 802 kN | 6 175 kN | 0.78  FAIL     | 0.55 FAIL   |
| 3  box complete, no backfill |  7 528 kN | 6 175 kN | 1.22  MARGINAL | 0.86 FLOATS |
| 4  backfilled + cover        | 12 453 kN | 6 175 kN | 2.02  OK       | 1.41 OK     |

            Require FoS >= 1.2.
            ULS COMB 102 = 0.9 x 12453 / (1.5 x 6175)               = 1.21

            Uplift acts on the REAL UNDERSIDE, not on the plate model's
            mid-surface area.

*** THE ABSOLUTE FIGURES ABOVE ARE AT THE PRE-M1 21.600 BOX ***
            21.600 x 6.200 = 133.92 m2  ->  46.11 x 133.92 = 6175 kN (table)
            22.000 x 6.200 = 136.40 m2  ->  46.11 x 136.40 = 6289 kN (CURRENT)
            Both uplift and resistance scale with length (x 22.0/21.6),
            so EVERY FoS IS UNCHANGED:  0.325 / 0.778 / 1.219 / 2.017,
            and COMB 102 stays 0.9 x 12684 / (1.5 x 6289)            = 1.21
            THE HAND CHECK USES 136.40 m2 / 6289 kN.
```

**Mandatory mitigation — a design output, not a contractor's problem:**

1. **Continuous dewatering** from the start of excavation until backfill and cover are complete.
2. **Temporary pressure-relief valves / knock-out plugs in the mat**, 6 No., grouted up **only
   after backfill**.
3. **Programme the sub-structure to complete before the monsoon**, or bund and positively drain
   with standby pumping and generator back-up.
4. **Backfill SYMMETRICALLY, in layers.**

> **And mitigation 1 is NOT met by the current programme — the departure is recorded, in writing.**
> The owner's schedule ends dewatering on 11-05-27; side backfill runs 20-07-27 to 30-07-27 and the
> burster slab is not cast until 21-08-27. **The gap spans the whole 2027 monsoon with the box at
> stage 3 — FoS 1.22 at the design water table and 0.86 flooded to grade.**
>
> **Owner ruling 1 (RC4): the residual flotation risk is ACCEPTED IN WRITING. No date moves.**
> **B.3 mitigations 2, 3 and 4 stay mandatory.** This is a departure from mitigation 1, recorded
> as one — which is the only honest way to carry it.

## 9.4 Pressure (roof) slab — 900 thk — THE GOVERNING ELEMENT — 51 %

### 9.4.1 One-way, and why that is the licence for M1

```
ONE-WAY ARGUMENT   Aspect ratio 20.8 / 5.0                        = 4.2
                   IS 456 Table 26 is tabulated only to ly/lx = 2.0,
                   so TWO-WAY ACTION CANNOT BE CLAIMED.
                   -> Mp depends on Ln of the 5 m WIDTH only.
                   -> LENGTHENING THE BOX IS STRUCTURALLY FREE  (basis of M1)
                      Widening 5.0 -> 6.0 m would raise the roof moment 44 %.
```

### 9.4.2 Natural period — the calculation that puts this in the quasi-static regime

```
m       = 0.900 x 2500 + 0.25 x 2.0 x 2000                  = 3250 kg/m2
0.5 EIg = 0.5 x 2.958e10 x 0.900^3 / 12                     = 8.985e8 N.m2/m
f1      = (22.373 / 2 pi) . sqrt( EI / (m . Ln^4) )         = 74.9 Hz
T                                                           = 13.4 ms
t_d / T = 10 to 100    ->   QUASI-STATIC
```

### 9.4.3 Flexure

```
FLEXURE     d = 900 - 75 - 12.5                                   = 812.5 mm
            Mp = w . Ln^2 / 16 = 448.15 x 25 / 16                 = 700.2 kNm/m
            Mu,lim = 0.133 x 43.75 x 1000 x 812.5^2               = 3841 kNm/m  OK
            Ast,req (pt 0.20 %)                                   = 1632 mm2/m
            Cl. 26.5.2.1 minimum 0.12 % x 900                     = 1080 mm2/m
            Cl. 26.5.2.2 max bar dia D/8 = 112                    OK for T25

ADOPTED     T25 @ 150 EF EW                                       = 3272 mm2/m
            Mu = 1362.4 kNm/m   ->   UTILISATION 51 %
            xu = 113.0   ->   x/d = 0.139   <<  0.46

*** x/d = 0.139 IS THE PROOF THAT mu = 5 IS DEFENSIBLE ***
```

### 9.4.4 Shear, including the direct-shear check

```
SHEAR       V at the support face = 448.15 x 2.50                 = 1120 kN/m
            V at d from the face  = 448.15 x (2.50 - 0.8125)      = 756.3 kN/m
            tau_v 0.931 | tau_c 0.450 (pt 0.403 %) | tau_c,max 3.70   OK
            Vus 390.8 kN/m ; Asv/sv 1.106  ->  T12 4-leg at 409
            Cl. 26.5.1.5 limit 300 GOVERNS

ADOPTED     T12 4-LEG @ 250 IN THE END 1500 EACH SIDE
            T12 2-LEG @ 300 ELSEWHERE

DIRECT SHEAR   Vd,max = 0.16 fck,dyn b d                          = 5688 kN/m
               against 1120 applied                               = 19.7 %
               [UFC 3-340-02 Sec. 4-30, cited as US criteria, NOT IS 456]
```

> **Direct shear is a blast-specific failure mode that IS 456 does not address.** At a support,
> a very short, very high shear pulse can shear the section off cleanly before flexural response
> develops. It is checked here against a US criterion, **and the criterion is named as a US
> criterion** rather than blended into the Indian Standard work.

### 9.4.5 Why 900 mm and not 800

```
| t    | d     | Mp  | Ast,req | tau_v | verdict                     |
| 600  | 512.5 | 689 |  2673   | 1.71  | links at 164, congested     |
| 800  | 712.5 | 696 |  1868   | 1.12  | the STRUCTURAL OPTIMUM      |
| 900  | 812.5 | 700 |  1633   | 0.93  | ADOPTED                     |
| 1000 | 912.5 | 704 |  1453   | 0.78  | 11 % over                   |
```

**900 is adopted over the structural optimum of 800 for three stated reasons:**

1. **Reserve at the two 1 400 mm collars**, where the slab is locally interrupted;
2. **Headroom against a raised design basis threat while the yield is unconfirmed** — the honest
   consequence of Part 2.1.3's `[N]`;
3. **Support rotation kept inside 2° without resorting to UFC lacing reinforcement.**

## 9.5 Roof openings

### 9.5.1 The two 1 400 dia escape-shaft openings

```
Interrupted steel = 3272 x 1.400                        = 4581 mm2/face/direction
Trimmers each side = 4581 / 2                           = 2291 mm2

ADOPTED  5 No. T25 EACH SIDE, EACH FACE, EACH DIRECTION (2454 mm2)
         anchored Ld = 1000 beyond the opening
         Collar 250 RC; T16 @ 150 hoops (3 layers) + T16 @ 150 radials
         Slab thickened 900 -> 1200 over a 600 mm annulus
```

> **Circular is the right shape: hoop action, and no re-entrant stress concentration.** This
> detail is what SETS the 750 mm clearance rule (Part 5.6) — 250 collar + ~400 trimmer band +
> 100 tolerance — and that rule then propagates all the way back into the bay widths and into what
> Modification M1 was allowed to do.

### 9.5.2 The 2 800 × 3 160 stair void — Finding F2

```
The void leaves an 1840 mm CANTILEVER of 900 slab, 2800 wide, at 448.15 kPa.

M(root) = 448.15 x 1.840^2 / 2                          = 758.6 kNm/m
   *** THIS EXCEEDS THE 700.2 kNm/m MIDSPAN Mp ***

Ast,req TOP = 1772 mm2/m  <  3272 provided   ->  UTILISATION 56 %   OK
V(root) = 448.15 x 1.840                                = 824.6 kN/m
tau_v 1.015 > tau_c 0.450 ;  Vus 459.4 kN/m ;  Asv/sv 1.300
   -> T12 4-leg at 348 ;  Cl. 26.5.1.5 limit 300

ADOPTED  T12 4-LEG LINKS @ 250 THROUGHOUT THE PAD            (NEW requirement)
   plus  Free edge thickened 900 -> 1200 over 600, with 6-T25 top +
         6-T25 bottom and T12 closed links @ 150
   plus  6 No. T25 each face, top and bottom, in a 900 band over W6 and W7
   plus  Diagonal trimmers 4 No. T25 each face at 45 deg at BOTH re-entrant
         corners, 2000 long each way, anchored Ld beyond
   plus  1100 mm guarding to the free edge          (NBC 2016 Pt 4)
```

> **Finding F2: the cantilever root moment exceeds the midspan moment of the element it hangs
> off.** The flexural steel already provided happens to cover it at 56 % — but **the shear did
> not**, and the links through the pad are a new requirement that the Phase 1 report did not
> carry. **A 1.84 m cantilever of 900 mm slab at 448 kPa is not a detail; it is a structural
> element, and it is now designed as one.**

# PART 10 — STAIRS, HEADHOUSE AND APPURTENANCES

## 10.1 Main staircase, Bay 7 — FROZEN GEOMETRY

> **STATUS: INSIDE the protective envelope. NOT a blast element.** The shaft pressurises, but that
> pressure acts on the shaft **walls** and on the blast **doors** — **not as a net load on a slab
> that is open on both faces.** The stair is therefore designed to IS 456 with normal partial
> factors, **not** with IS 4991 dynamic strengths. That is stated explicitly on the drawing.

**Geometry check — NBC 2016 Part 4:**

| Item | Provided | Limit | Verdict |
|---|---|---|---|
| Riser | 170.833 mm | ≤ 190 | **OK** |
| Tread / going | 280 mm | ≥ 250 | **OK** |
| Flight width | 1 200 mm | ≥ 1 000 | **OK — stretcher-capable** |
| Risers per flight | 8 | ≤ 12 preferred | **OK** |
| Headroom | 2 533 mm | ≥ 2 200 | **OK** |
| Total rise | 4 100 = 24 × 170.833 | (−)6.100 → (−)2.000 | **closes exactly** |

```
FLIGHT -- waist 200
   theta = arctan(170.833 / 280) = 31.4 deg,  cos theta = 0.8535
   waist self   0.200 x 25 / 0.8535                     = 5.858 kPa
   steps        0.5 x 0.170833 x 25   IS 456 Cl. 33.2   = 2.135 kPa
   finishes                                              = 1.000 kPa
   live         IS 875 (Pt 2), plant + escape route      = 5.000 kPa
   total 13.99   ->   wu = 1.5 x 13.99                   = 21.0 kPa

   Leff = going + min(landing/2, 1000) each end   IS 456 Cl. 33.1(b)
        = 1960 + 600 + 600                                = 3160 mm
   d = 200 - 30 - 6                                       = 164 mm
   M = wu . Leff^2 / 8                                    = 26.2 kNm/m
   Ast,req 380 ;  Cl. 26.5.2.1 min 0.12 % x 200 = 240

   ADOPTED  T12 @ 150 MAIN (754)  ->  Mu 50.3,  UTILISATION 52 %
            T10 @ 200 DISTRIBUTION (393)

   DEFLECTION  Leff/d = 19.3 ; basic 20 ; fs = 0.58 x 500 x 380/754 = 146
               pt 0.46 % ; MF ~ 1.9 -> permissible 38 > 19.3      OK
   SHEAR  V = 33.2 kN/m ; tau_v 0.202 ;
          tau_c 0.479 x k 1.20 (Cl. 40.2.1.1)             = 0.575   OK, no links
   TOP STEEL  T12 @ 150 for 0.25 Leff = 800 into the flight, anchored Ld 480

LANDINGS L1 / L2 / ARRIVAL -- 200 thk, spanning ACROSS the shaft
   self 7.50 + finishes 1.50 + live 7.50 + flight reaction 27.70   = 44.20 kPa
   Leff = 2800 clear + 200 bearing      Cl. 22.2(a)                = 3000 mm
   M = 44.2 x 3.000^2 / 8                                          = 49.7 kNm/m
   Ast,req 745 ;  T12 @ 150 gives 754 = 100 %  -- TOO TIGHT

   ADOPTED  T12 @ 125 BOTTOM (905)  ->  Mu 59.5,  UTILISATION 84 %
            T12 @ 125 TOP for 900 from each support
            T10 @ 200 distribution

   DEFLECTION  3000/164 = 18.3 ; fs 239 ; pt 0.552 % ; MF ~ 1.35
               -> 27 > 18.3                                         OK
   SHEAR  V 66.3 kN/m ; tau_v 0.404 < tau_c 0.519 x 1.20 = 0.622     OK
```

> **T12 @ 150 on the landings gives exactly 100 % utilisation, and 100 % is not a design.** It was
> tightened to @ 125. That is the kind of decision that never appears in a summary and always
> appears in a site query.

**Compatibility notes.** The arrival landing at (−)6.100 **is** the mat surface — there is no
separate slab. Flight 3 lands directly on the 900 mm pressure-slab pad at (−)2.000. The landings
prop W6 and W7 at (−)4.733 and (−)3.367, **but only over their 1 200 mm depth — and the 400 mm
wall design in Part 9.2 does NOT rely on that prop.**

## 10.2 Entry (approach) stairwell

> **STATUS: OUTSIDE the protective boundary, NOT blast rated, and expected to be LOST in the
> design event.** Designed to IS 456 with normal partial factors.

```
FLIGHT -- 12R @ 166.6667 / 300, 1500 wide, waist 250
   theta = 29.05 deg,  cos theta = 0.8742
   waist 7.150 + steps 2.083 + finishes 1.000 + live 5.000 = 15.233
                                            ->  wu        = 22.85 kPa
   Leff = 3300 + 750 + 750       IS 456 Cl. 33.1(b)        = 4800 mm
   d = 250 - 30 - 8                                        = 214 mm
   M = 22.85 x 4.800^2 / 8                                 = 65.8 kNm/m
   Ast,req 744 ;  min 0.12 % x 250 = 300

   ADOPTED  T16 @ 200 MAIN (1005) -> Mu 87.3, UTIL 75 %, x/d 0.162
            T10 @ 200 DISTRIBUTION (393)
            T16 @ 200 TOP for 1200 into the flight, anchored Ld 640

   DEFLECTION  4800/214 = 22.4 ; basic 20 ; fs 215 ; pt 0.470 %
               MF ~ 1.5 -> 30                                  OK
   SHEAR  V 54.8 kN/m ; tau_v 0.256 ; tau_c 0.484 x k 1.10 = 0.532  OK

SIDE WALLS 250 -- retained 2.9 m, propped by the roof and the raft
   sigma_h at base = 0.5 x 20 x 2.900 + 0.5 x 10            = 34 kPa
   M ~ w L^2 / 12 on an equivalent 20 kPa UDL               = 14.0 kNm/m
   d = 250 - 50 - 6 = 194 ;  Ast,req 168
   Cl. 32.5(a) min 0.0012 x 250 = 300 ;  Cl. 32.5(b) 0.0020 x 250 = 500
   Cl. 32.5(c) two curtains required (t > 200)               OK
   ADOPTED  T12 @ 200 EF EW (565/face)
            -- MINIMUM STEEL GOVERNS, 31 % utilised
   SHEAR  V ~ 49 kN/m ; tau_v 0.253 < tau_c 0.484            OK

RAKING ROOF 250 -- 1500 clear
   self 6.25 + waterproofing/screed 2.0 + earth lap 5.4
   + IMPOSED 20                                             = 33.65
                                              ->  wu        = 50.5 kPa
   (20 kPa imposed taken DELIBERATELY, for a stray vehicle on the berm)
   M = w l^2 / 12                                           = 9.5 kNm/m
   d = 250 - 30 - 6 = 204 ;  Ast,req 108 ;  min 300 GOVERNS
   ADOPTED  T12 @ 200 EF EW  ->  Mu 48.2, 20 % utilised
   SHEAR  V 38 kN/m ; tau_v 0.186                            OK

TOP LANDING 250 (0.000)
   wu 54.9 kPa ; Leff 1750 ; M 21.0 kNm/m ; Ast,req 229
   ADOPTED  T12 @ 200 EF EW (565) -> Mu 50.6, 41 % utilised

PLATFORM 250 ((-)2.000, on fill)     ADOPTED  T12 @ 200 EF EW, nominal
HEADWALL 250                         ADOPTED  T12 @ 200 EF EW
   Door lintel over 1000 clear: 250 x 350, 3-T12 top + 3-T12 bottom, T8 @ 150
STEPPED RAFT 300 on compacted fill   ADOPTED  T12 @ 200 EF EW
```

### 10.2.1 The opening corner — the detail most often got wrong

```
At the TOP of the flight the tension face turns through 209 degrees.

A bar bent round that corner has its bend resultant directed OUT of the
concrete: it spalls the cover and the bar loses its anchorage.

MAIN BARS SHALL NOT BE BENT ROUND IT.
   Each layer is continued STRAIGHT, CROSSED, and anchored Ld = 640 into the
   OPPOSITE face, plus a U-bar T16 @ 200 across the corner.
   [SP 34:1987 Cl. 5.5 and standard detailing practice]

At the FOOT of the flight the corner CLOSES (151 degrees) -- bars may turn
normally.
```

> **This is a geometry problem, not a preference.** An obtuse re-entrant corner in a tension face
> puts the resultant of the bend into the cover, and the cover has nothing to push against. Two
> corners, two different answers, and the drawing shows both.

## 10.3 Entry headhouse — roof, 500 thk — 90 %, the highest utilisation in the project

```
w = 383 (blast) + 12.5 (self) + 1.0 (SIDL)                     = 396.5 kPa
Panel 4000 x 5000 clear, monolithic with 400 walls on all four
sides,  ly/lx = 1.25
d = 500 - 75 - 10                                              = 415 mm
Mu,lim = 0.133 x 43.75 x 1000 x 415^2                          = 1002 kNm/m

THREE ANALYSES, AND THE MOST CONSERVATIVE IS ADOPTED
| # | Method                                          | M       |
| 1 | One-way fixed-fixed strip,  Mp = w . Ln^2 / 16  | 396.5   <- ADOPTED
| 2 | IS 456 Table 26 Case 1, alpha_x- = 0.045 at 1.25| 285.5   |
| 3 | Yield line, FIXED on 4 edges, isotropic         | 162.2   |

  Method 3 formula:  wu = 48 m / [ a^2 ( sqrt(3 + (a/b)^2) - a/b )^2 ]
  VALIDATION: as b -> infinity, 48/3 = 16 = the fixed-fixed strip w L^2/16
              (the 24-coefficient version gives 8 = SIMPLY SUPPORTED w L^2/8)

Ast,req (one-way basis)                                        = 1879 mm2/m
Cl. 26.5.2.1 minimum 0.12 % x 500                              =  600 mm2/m

ADOPTED  T20 @ 150 EF EW = 2094 mm2/m   ->   Mu = 438.5 kNm/m
         UTILISATION  90 % one-way  |  65 % Table 26  |  37 % yield line
         xu 72.3  ->  x/d = 0.174   <<  0.46

SHEAR   *** NEW AND MANDATORY -- NOT IN THE PHASE 1 REPORT ***
   V at d = 396.5 (2.000 - 0.415)                              = 628.4 kN/m
   tau_v 1.514 | tau_c 0.502 (pt 0.505 %) | tau_c,max 3.70       OK
   (tau_c read at the STATIC M35 value -- IS 4991 Cl. 10.3.1.1)
   Vus 420.0 kN/m ; Asv/sv 2.327  ->  T12 4-leg at 194
   Cl. 26.5.1.5 limit min(0.75d = 311, 300)                     = 300
ADOPTED  T12 4-LEG @ 175 IN THE END 1200 EACH SIDE;  @ 250 ELSEWHERE

DETAILING
   No opening in the headhouse roof (the stair void is in the FLOOR).
   Corner torsion steel (Cl. D-1.8) NOT required -- all four edges carry
   full T20 @ 150 hogging steel continuous into the walls.
   Haunch 300 x 300 at all four wall-roof junctions, diagonal T16 @ 150.
   Top steel continuous over every support, anchored Ld = 800 into the wall.
```

> **Three analyses, and the reason the crudest one is adopted.** The one-way strip is the most
> conservative of the three by a factor of 2.4 against the yield-line value. A yield-line solution
> is only as good as the assumption that all four edges are genuinely fixed and that the panel can
> develop a full mechanism; under a blast load on a structure whose neighbour is expendable, that
> is not a bet worth taking for a saving of one bar size. **The project takes the strip, prints
> all three, and says which one it used.**
>
> **The corrected yield-line coefficient, recorded as an error.** The yield-line value was once
> computed as 324.4 kNm/m using the **simply-supported** coefficient 24 instead of the
> **fixed-four-edges** coefficient 48. It is **162.2**. The validation that catches it is in the
> formula itself: as `b → ∞`, 48/3 = 16 = `wL²/16`, which is the fixed-fixed strip. **No
> reinforcement changed, because the one-way value was the one adopted and nothing depended on the
> yield-line number** — but the error is recorded rather than quietly fixed.
>
> **And the shear is new.** τ<sub>v</sub> = 1.514 against τ<sub>c</sub> = 0.502 is a factor of
> three. The Phase 1 report did not check it. **This is conflict C2, and the links are mandatory.**

## 10.4 Headhouse walls HW1–HW4 — 400 thk — conflict C10 — 59 %

```
                              CASE A (report)        CASE B (ADOPTED)
Lateral pressure              113 kPa drag           383 kPa full envelope
Mp = w x 2.400^2 / 16         40.7 kNm/m             137.9 kNm/m
Ast,req                       221 mm2/m              766 mm2/m
Cl. 32.5(a) min vertical      480 mm2/m -- governs   480
Cl. 32.5(b) min horizontal    800 mm2/m -- governs   800
Utilisation on T16@150 EF EW  17 %                   59 %
Shear V at d                  97.0 kN/m              328.6 kN/m
tau_v                         0.283                  0.961
tau_c (pt 0.392 %)            0.444                  0.444
Verdict                       NO LINKS               LINKS REQUIRED

d = 400 - 50 - 8 = 342 ;  Mu,lim = 681 kNm/m
ADOPTED  T16 @ 150 EF EW = 1340 mm2/m -> Mu 235.2, UTIL 59 %, x/d 0.135
         Vus 176.9 kN/m ; Asv/sv 1.189 -> T12 4-leg at 381
         Cl. 26.5.1.5 limit min(0.75d = 256, 300) = 256 GOVERNS
ADOPTED  T12 4-LEGGED LINKS @ 250 c/c THROUGHOUT ALL FOUR WALLS

Two-way check (information only, fixed on 4 edges):
   HW1/HW2  4000 x 2400  ->  m = 69.9 kNm/m    (one-way strip 137.9)
   HW3/HW4  5000 x 2400  ->  m = 79.8 kNm/m    (one-way strip 137.9)

AXIAL  Roof reaction, two-way (Cl. 24.5):
          HW3/HW4 trapezoid 2379 kN / 5.0 m                 = 476 kN/m
          HW1/HW2 triangle  1586 kN / 4.0 m                 = 396 kN/m
       One-way bound: 396.5 x 2.0 = 793 kN/m ;  self 29 kN/m
       Worst N = 822 kN/m  ->  f = 2.06 N/mm2
                            = 12 % of 0.4 fck,dyn            OK

*** PRESSURE ACTS FROM INSIDE TOO.  The inner security door is NOT blast
    rated and the entry stairwell is expected to be lost, so the headhouse
    FILLS and the walls are pushed OUTWARDS.  THE WALLS ARE REINFORCED
    SYMMETRICALLY FOR 383 kPa EITHER WAY -- a stated requirement, not an
    accident of detailing. ***

DOOR OPENING 900 x 2100 IN HW2 -- and a geometric trap
   Interrupted steel 1340 x 0.900 = 1206 mm2/face  ->  603 each jamb
   ADOPTED  2 No. T20 EACH JAMB EACH FACE (628), anchored Ld 800 beyond

   Door head at (-)2.000 + 2.100 = +0.100 ;  roof soffit +0.400
   -> ONLY 300 mm OF WALL ABOVE THE DOOR -- too shallow for a lintel.

   The 300 wall and the 500 roof act TOGETHER as an 800 mm deep edge band:
   w = 383 x 2.100/2 = 402 kN/m ;  M = w L^2/12 = 27.1 kNm ;  V = 181 kN
   d = 800 - 40 - 8 - 10 = 742 ;  tau_v = 0.610 N/mm2
   ADOPTED  400 x 800 EDGE BAND: 4-T20 TOP + 4-T20 BOTTOM,
            T12 4-LEG @ 150, over the opening and 600 each side

   Door frame cast in and WELDED to the cage (EMP), even though the leaf is
   a security door and is not blast rated.
```

### 10.4.1 HW3 — the wall that has nothing under it

```
The pressure slab spans one-way in Y over 5000 clear.  HW3 runs IN the Y
direction, so its load is carried by a slab strip acting as a beam.

   b_eff = 0.400 + 2 x 1.05  (45 deg spread through the 900 slab)  = 2.5 m  [A]

CASE 1 -- two-way roof distribution (IS 456 Cl. 24.5, correct)
   Line load 476 (trapezoid) + 29 (self)                          = 505 kN/m
   Equivalent UDL = 505/2.5 + 22.5 + 2.0                          = 226 kPa
   M = w . Ln^2 / 16 = 226 x 25 / 16                              = 354 kNm/m
   Against the slab's 1362 kNm/m capacity                         = 26 %   OK

CASE 2 -- one-way roof bound
   Line load 793 + 29 = 822 kN/m -> 353 kPa -> M = 552 kNm/m      = 41 %   OK

ADOPTED  No slab change needed.  DETAILED AS A LINE LOAD, NOT AS A SUPPORT.
         Robustness: 4 No. T25 ADDITIONAL TOP AND BOTTOM in a 1200 mm band
         beneath HW3, lapped 1250 (50 phi) into the main mesh.
```

> **`b_eff` = 2.5 m is an assumption, and it is closed on the margin.** Owner ruling 24 (RC6)
> accepts it: the strip is at 26 % on the correct two-way distribution and 41 % on the conservative
> one-way bound, so **more than half the capacity is spare and `b_eff` would have to be badly wrong
> to matter** — assumption `A11`.

## 10.5 Escape shaft head hatches — `RC5-F2`, the finding nobody had asked for

> **The protective boundary is defined as the blast doors plus the perimeter walls, the mat and
> THE PRESSURE SLAB. ESC 1 and ESC 2 are 1 400 mm dia bores straight through the pressure slab.**
> They begin in bay 1 — **inside the gas-tight envelope** — and in bay 8, and they finish at grade.
>
> **Each shaft head is therefore a 1.54 m² hole in the protective boundary, and the only thing that
> can close it is a hatch that did not exist.** The EMP penetration register had listed both as
> FAIL and prescribed a bonded conducting hatch — **but it prescribed it for EMP. Nothing anywhere
> in this project stated what the head has to resist STRUCTURALLY.**
>
> The design was silent, so owner ruling 18 (RC5) took the only defensible reading: **the head is
> part of the boundary and takes the full 383 kPa design blast.**

```
total force on the leaf    383 x pi x 0.700^2                = 589.6 kN
M = w a^2 (3 + nu) / 16                                      =  38.71 kNm/m
V at the seating = w a / 2                                   = 134.1 kN/m

flat Fe250 plate   t = sqrt(6M / sigma) = 30.5  ->  say 32 mm
mass of a 1600 dia x 32 leaf                                 =  505 kg
```

> **505 kg is the point, not the thickness.** Half a tonne cannot be lifted by a person escaping
> up a 6.8 m ladder in the dark. **That is why the answer is not a flat plate.**

**ADOPTED: a ribbed steel weldment** — 1 600 dia, 12 mm face, 8 No. radial ribs 150 × 10 and a
150 × 12 perimeter ring — on a **steel seating ring cast into the 250 mm collar**, bearing 150 mm
all round, with **four quarter-turn dogs so the leaf resists UPLIFT as well as downward pressure**
(the negative phase and the rebound both lift it), and **counterbalanced or spring-assisted,
openable from inside by one person without a key or a tool.** Indicative leaf mass **≈ 322 kg —
still a mechanically assisted item.**

**Not designed and not invented `[N]`:** the rib proportioning (an orthotropic plate problem — the
flat-plate demand above is exact and is **the brief**), the counterbalance mechanism, and every
EMP figure.

> **And the consequence of splitting it the way the ruling splits it, stated plainly.** The EMP
> treatment for this opening is a **bonded conducting** hatch. Bonding is not a finish applied
> later — it is continuity between the leaf, the seating ring and the collar reinforcement, and it
> has to be designed **into** the weldment and the seat. **Ruling the structure and the bonding
> into different packages is exactly how these two shaft heads came to be undesigned for four
> revisions.** `EM-V6` stays open for its EMP half.

## 10.6 The escape shaft ladders

> **Owner ruling 2 (RC4): ladder only; fall-arrest deferred.** Before it, the project held **no
> position at all** on how either shaft was climbed — no ladder, no rung, no fall-arrest anywhere
> in any document, against a **6.250 m** climb out of Bay 1 and a **6.800 m** climb out of Bay 8.

**One ladder type serves both shafts:**

```
20 mm dia galvanised MS rungs, 400 clear width, EQUAL PITCH within each shaft
     ESC 1   297.6 mm over 21 spaces
     ESC 2   295.7 mm over 23 spaces
>= 200 behind the rung   .   >= 750 clear climbing space in front
2 No. 50 x 10 galvanised flat stringers
cast-in lugs to the 250 collar and the roof-slab bore,
expansion-anchored brackets at 1.5 m over the lower 3.200 m
grab rails 1100 above the head
```

`IS 3696 (Part 2)` and `NBC 2016 Part 4` are named **by title only** — neither is in the workspace
and no unconfirmed clause is cited.

> **`FS-V7` DOES NOT CLOSE. IT CHANGES** — and three things are still missing, and the ruling
> knows it:
>
> - **no fall-arrest** — deferred by the ruling;
> - **no rest platform** — a 1 400 mm bore cannot take one without blocking the escape;
> - **the injured-person question** — **a vertical ladder cannot pass a stretcher**, and whether a
>   casualty is expected to use a shaft at all is a client question.

# PART 11 — THE SENTRY POST

## 11.1 Why it is not blast designed, and what that decision cost

> **The sentry post is NOT designed for the blast, and that is a RECORDED decision, not an
> omission.**
>
> ```
> Reflected pressure on the 4.0 x 6.7 m face
>       p_r x Ae = 1366 kPa x 26.8 m2            = 36 600 kN  (about 3730 t)
> Hardening would need roughly 700 mm of RC on all four above-ground faces.
> ```
>
> **Not justified for a peacetime observation post.** The post is declared expendable, and the
> shelter's protection does not depend on it in any way.

**All member design uses the STAAD base shear V<sub>b</sub> = 73.18 kN, not the hand-calculated
59.3 kN** (Part 7.8.2).

### 11.1.1 Seismic member forces — portal method at V<sub>b</sub> = 73.18 kN

```
Q_roof  = 73.18 x (315.9 x 6.25^2) / Sigma                     = 59.51 kN
Q_floor = 73.18 x (276.8 x 3.20^2) / Sigma                     = 13.67 kN

Column shear, ground storey = 73.18 / 4   (= STAAD Fx 18.295)  = 18.30 kN
Column shear, first storey  = 59.51 / 4                        = 14.88 kN
Column moment, ground = 18.30 x 3.200 / 2                      = 29.27 kNm
Column moment, first  = 14.88 x 3.050 / 2                      = 22.69 kNm

Beam moment, first-floor joint (corner joint, one beam)
                             = 29.27 + 22.69                   = 51.96 kNm
Beam moment, roof joint                                        = 22.69 kNm

Axial from overturning -- READ DIRECTLY FROM THE STAAD REACTIONS:
   EQ+X  Fy = +/- 36.127 kN      EQ+Z  Fy = +/- 27.891 kN
                                 -> 36.127 GOVERNS
```

### 11.1.2 The frame analysis assumption, stated rather than hidden

```
Single-bay portal in each direction.  Beams are NOT fully fixed; the joint
rotates.  Slope-deflection with symmetric loading:

   I_beam = 250 x 450^3 / 12                              = 1.8984e9 mm4
   I_col  = 350^4 / 12                                    = 1.2505e9 mm4
   Kc (first-floor joint) = 4EI/3200 + 4EI/3050           = 3.203e6 . E
   M_support = -FEM + (2 E I_b / L_b) . theta,
      theta = FEM / (2 E I_b / L_b + Kc)

| Beam            | FEM   | 2EI/L      | Reduction | M_support | M_midspan |
| B1, 1.5(DL+LL)  | 39.49 | 1.040e6 E  |  x 0.755  |   29.81   |   30.90   |
| B1, DL only     | 22.53 |     --     |  x 0.755  |   17.01   |     --    |
| B2, 1.5(DL+LL)  | 70.60 | 0.8165e6 E |  x 0.797  |   56.26   |   49.64   |
| B2, DL only     | 39.21 |     --     |  x 0.797  |   31.25   |     --    |
```

## 11.2 Slab S1 — 150 thk two-way

```
Cover 30 (Table 16, moderate) ;  T8 bars
   dx = 150 - 30 - 4                                        = 116 mm
   dy = 150 - 30 - 8 - 4                                    = 108 mm
Clear spans 3400 and 4400

Effective span, IS 456 Cl. 22.2(a) -- the LESSER of clear + d, or c/c:
   lx = min(3400 + 116, 3650)                               = 3516
   ly = min(4400 + 108, 4650)                               = 4508
   ly / lx = 1.282  <  2   ->   TWO-WAY     Cl. 24.4 / Annex D

MOMENT COEFFICIENTS -- IS 456 Table 26 (Annex D-1.1) Case 9: four edges
   discontinuous but RESTRAINED, with corner torsion steel per Cl. D-1.8
   -> Table 26, NOT Table 27.
   alpha_x = 0.0777 (interpolated at 1.282)    alpha_y = 0.056

wu = 1.5 (4.750 + 3.000)                                    = 11.625 kPa
     (the FIRST FLOOR governs; the roof is 10.125)

   Mx = 0.0777 x 11.625 x 3.516^2                           = 11.17 kNm/m
   My = 0.0560 x 11.625 x 3.516^2                           =  8.05 kNm/m
   Ast,req  x 229  |  y 176
   Cl. 26.5.2.1 min 0.12 % x 150                            = 180 mm2/m
   Cl. 26.5.2.2 max bar dia D/8 = 18.75                     OK
   Cl. 26.3.3(b) max spacing 3d or 300                      OK

ADOPTED  T8 @ 150 c/c BOTH WAYS BOTTOM                      = 335 mm2/m
   Mu = 16.09 (x) / 14.92 (y) kNm/m  ->  UTILISATION 69 % / 54 %
   xu = 13.5  ->  x/d = 0.116 / 0.125

DEFLECTION  lx/dx = 3516/116 = 30.3 ;  basic taken as SIMPLY SUPPORTED = 20
   fs = 0.58 x 500 x 229/335 = 198 ;  pt = 0.289 % ;  MF (Fig. 4) ~ 1.68
   Permissible 20 x 1.68 = 33.6 > 30.3                       OK
   (as continuous, basic = 26 and the margin doubles -- it passes on the
    conservative assumption, so that assumption is the one used)

SHEAR  Vu ~ wu . lx / 3 = 13.6 kN/m ;  tau_v 0.117 ;
       tau_c 0.390 x k 1.30 (D <= 150)                       = 0.507  OK
```

**Detailing — IS 456 Annex D:**

| Clause | Requirement | Adopted |
|---|---|---|
| D-1.2 / D-1.3 | Middle strip = ¾ width, edge strips ⅛ each side; **Table 26 moments apply to MIDDLE STRIPS ONLY** | — |
| D-1.4 | 50 % of midspan bottom steel to within 0.1 L of a discontinuous edge; remainder curtailed at 0.25 L | — |
| **D-1.6** | At every discontinuous edge, top steel = 50 % of the midspan bottom steel, extending 0.1 L = 400 mm into the span | **T8 @ 300 TOP, 400 mm band, all four edges** |
| D-1.7 | Edge strips: minimum reinforcement only | — |
| **D-1.8** | **Torsion at corners** — both edges discontinuous at all four corners → steel = ¾ of the midspan area, in **four layers** (2 top + 2 bottom, each way), over l<sub>x</sub>/5 = 700 mm each way | **T8 @ 200, 4 LAYERS, 700 × 700 AT EACH CORNER** |

> **The torsion mats are a HOLD POINT for reinforcement inspection.** Table 26 is valid **only
> because they are provided.** Omit them and the slab must be reassessed on Table 27, which gives
> larger coefficients. **This is why the drawing carries a panel headed "why Table 26 and not Table
> 27".**

## 11.3 Beam B1 — 250 × 450, span 3 650

```
IS 13920:2016 section limits
   b >= 200                                   250       OK
   b/D = 0.556 >= 0.3                                   OK
   clear span / D = 3300/450 = 7.33 >= 4                 OK

d = 450 - 30 - 8 - 8                                     = 404 mm
Mu,lim = 0.133 x 30 x 250 x 404^2                        = 162.8 kNm

| Combination                                | M_support hogging |
| 1.5(DL + LL)                               |  29.8  |
| 1.2(DL + LL + EL) = 1.2(19.87 + 51.96)     |  86.2  |
| 1.5(DL + EL) = 1.5(17.01 + 51.96)          | 103.5  <- GOVERNS |
| 0.9 DL + 1.5 EL                            |  93.2  |

Mu = 103.5 < 162.8  ->  singly reinforced ;  Ast,req = 661 mm2
ADOPTED  4-T16 TOP AT SUPPORTS (804) -> Mu = 122.6 kNm, UTIL 84 %, x/d 0.321

BOTTOM
   Reversal 1.5(17.01 - 51.96) = -52.4 kNm sagging  ->  Ast,req 313
   IS 13920 Cl. 6.2.3: positive steel at the joint face >= 50 % of negative
        = 0.5 x 804 = 402 mm2                                 <- GOVERNS
   Midspan sagging 30.9 kNm  ->  Ast,req 181
   IS 13920 Cl. 6.2.1(b) rho_min = 0.24 sqrt(fck)/fy
        = 0.00263 x 250 x 404                                 = 266
   IS 456 Cl. 26.5.1.1 As,min = 0.85 b d / fy                 = 172
   IS 13920 Cl. 6.2.2 rho_max = 0.025                         = 2525   OK
   Cl. 6.2.4 top or bottom >= 25 % of max at the joint face   = 201     OK
ADOPTED  2-T16 BOTTOM CONTINUOUS (402) -> Mu = 66.0 kNm, x/d 0.160

SHEAR -- CAPACITY DESIGN, IS 13920 Cl. 6.3.3
   Vu = 1.2(D+L) . L/2  +/-  1.4 (Mu^As + Mu^Bh) / L
   Unfactored gravity total = 54.29 (UDL) + 25.81 (triangle)   = 80.1 kN
   1.2 x 80.1 / 2                                              = 48.1 kN
   1.4 x (122.6 + 66.0) / 3.650                                = 72.3 kN
   Vu                                                          = 120.4 kN
   tau_v = 1.192 N/mm2 ;  tau_c,max (Table 20, M30) 3.50        OK

   *** IS 13920 Cl. 6.3.4:  EQ share 72.3 / 120.4 = 60 % >= 50 %, no axial
       ->  tau_c TAKEN AS ZERO in the plastic hinge region ***

   Asv/sv = 120.4e3 / (0.87 x 500 x 404) = 0.685 -> T8 2-leg at 147
   Cl. 6.3.5.1 hinge region (2d = 810 from each face):
       sv <= min(d/4 = 101, 8 x 16 = 128), need not be < 100    -> 100 mm
   Cl. 6.3.5.2 elsewhere: sv <= d/2                             = 202 mm

ADOPTED  T8 2-LEGGED HOOPS @ 100 c/c OVER 2d = 810 FROM EACH FACE;
         T8 @ 150 c/c ELSEWHERE.  First hoop within 50 mm of the column face.

DEFLECTION  l/d = 3650 / 404 = 9.0  <<  20                      OK
```

> **Capacity design, in one sentence: the beam is designed for the shear that accompanies its own
> flexural failure, not for the shear from the analysis.** That is what `1.4(Mu^As + Mu^Bh)/L`
> means — the hinges form at over-strength and the shear follows. **And when the earthquake share
> exceeds half the total, IS 13920 Cl. 6.3.4 requires τ_c to be taken as zero**: a hinge that has
> cycled has lost its aggregate interlock, so the links carry everything.

## 11.4 Beam B2 — 250 × 450, span 4 650 — 89 %

```
| Combination                                | M_support hogging |
| 1.5(DL + LL)                               |  56.3  |
| 1.2(DL + LL + EL) = 1.2(37.51 + 51.96)     | 107.4  |
| 1.5(DL + EL) = 1.5(31.25 + 51.96)          | 124.8  <- GOVERNS |
| 0.9 DL + 1.5 EL                            | 106.1  |

Mu = 124.8 < 162.8   OK ;  Ast,req = 822 mm2
ADOPTED  3-T20 TOP AT SUPPORTS (942) -> Mu = 139.8 kNm, UTIL 89 %, x/d 0.376
   *** 3-T20 CHOSEN OVER 5-T16: five T16 bars need 256 mm in a 250 mm
       wide beam.  That is exactly the check that becomes a site RFI
       if it is skipped. ***

BOTTOM   Cl. 6.2.3 -> 0.5 x 942 = 471 ;  midspan 49.6 kNm -> Ast,req 297
ADOPTED  2-T20 BOTTOM CONTINUOUS (628) -> Mu = 98.9 kNm, 50 %, x/d 0.250

SHEAR    Unfactored gravity (UDL-equivalent) = 26.115 x 4.650  = 121.4 kN
   1.2 x 121.4 / 2                                             = 72.8 kN
   1.4 x (139.8 + 98.9) / 4.650                                = 71.9 kN
   Vu                                                          = 144.7 kN
   tau_v = 1.433 ;  tau_c,max 3.50                              OK

   EQ share 71.9 / 144.7 = 49.7 % -- a hair under the Cl. 6.3.4 trigger.
   *** TAKEN AS TRIGGERED (tau_c = 0).  A design must not turn on the
       third decimal place of a ratio. ***

   Asv/sv = 0.823 -> T8 2-leg at 122 ;  hinge spacing 100 governs
   Outside the hinge V falls to ~124 kN and tau_c = 0.641 (pt 0.933 %)
   may be used  ->  Asv/sv 0.337  ->  T8 at 298
ADOPTED  T8 @ 100 OVER 810 FROM EACH FACE ;  T8 @ 150 ELSEWHERE
DEFLECTION  l/d = 4650 / 404 = 11.5  <<  20                      OK
```

## 11.5 Column C1 — 350 × 350

```
SLENDERNESS
   clear height, ground = 3650 - 450 - 450 (beam depth)          = 2750 mm
   Effective length factor 1.2 (Table 28, unbraced, both ends restrained)
   lex = 3300 ;  lex/D = 9.43 < 12  ->  SHORT COLUMN   Cl. 25.1.2   OK

MINIMUM ECCENTRICITY    Cl. 25.4
   emin = l/500 + D/30 = 5.5 + 11.67 = 17.2, but >= 20            -> 20 mm
   Mmin = 276.8 x 0.020 = 5.5 kNm  <<  applied                     OK

AXIAL, per column, unfactored:  DL 148.4 kN, LL 19.1 kN,
                                EQ axial +/- 36.127 kN
   1.5(DL + LL)  = 251.3 kN
   1.5(DL + EL)  = 276.8 kN   <- max
   1.5(DL - EL)  = 168.4 kN   <- min

LONGITUDINAL STEEL   Cl. 26.5.3.1:  min 0.8 % = 980 ;  max 6 % = 7350
ADOPTED  8-T16 = 1608 mm2  ->  p = 1.31 %,  bars on all four faces
   Cover 40 (Cl. 26.4.2.2) ;  d' = 40 + 8 + 8 = 56 ;  d'/D = 0.16

UNIAXIAL CAPACITY -- computed from the IS 456 Cl. 38.1 stress block and the
Fe500 design curve (Fig. 23B), NOT read off a chart:
   | Pu (kN) | Mu1 (kNm) |
   | 168.4   | 105.8 |
   | 251.3   | 111.7 |
   | 276.8   | 112.9 |

BIAXIAL -- IS 456 Cl. 39.6
   Puz = 0.45 fck Ac + 0.75 fy Asc
       = 0.45 x 30 x 120892 + 0.75 x 500 x 1608                  = 2235 kN
   Pu / Puz = 276.8 / 2235 = 0.124 < 0.2   ->   alpha_n = 1.0
   Worst case, EQ in Z with 30 % in X    IS 1893 Cl. 6.3.2.2:
      Mux = 25.6 kNm ;  Muy = 66.8 kNm
      25.6/112.9 + 66.8/112.9 = 0.227 + 0.592 = 0.819  <=  1.0     OK

STRONG COLUMN - WEAK BEAM   IS 13920 Cl. 7.2.1,  Sigma Mc >= 1.4 Sigma Mb
   | Joint                     | SigmaMb | 1.4 SigmaMb | SigmaMc      | Verdict |
   | First floor, X (B1)       |  122.6  |   171.6     | 112.9+101=213.9 |  OK  |
   | First floor, Z (B2)       |  139.8  |   195.7     | 213.9        |  OK     |
   | Roof, Z (B2 roof, 2-T20)  |   98.9  |   138.5     | 101          |  OK, marginal |

TRANSVERSE REINFORCEMENT
   General, Cl. 26.5.3.2: tie dia >= max(6, phi/4) = 8 ;
        spacing <= min(350, 16 phi = 256, 300)                    = 256
   IS 13920 Cl. 7.4: hoops over the full length at <= half the least
        dimension                                                 = 175
ADOPTED  T8 HOOPS @ 150 c/c outside the confining zone

SPECIAL CONFINING REINFORCEMENT   IS 13920 Cl. 8.1
   lo >= max(350, clear height/6 = 458, 450)                      = 500 mm
   spacing <= 0.25 x 350 = 87.5, but 75 <= s <= 100               = 85 mm
   Ash = 0.18 s h (fck/fy) [ (Ag/Ak) - 1 ]
       h = 350 - 2 x 40 = 270 ;  Ag = 122500 ;  Ak = 270^2 = 72900
       = 0.18 x 85 x 270 x (30/500) x (1.680 - 1)                 = 168.5 mm2
   minimum = 0.05 x 85 x 270 x 30/500                             =  68.9 mm2
ADOPTED  T10 HOOPS + ONE CROSS-TIE EACH WAY @ 85 c/c
         (3 legs x 78.5 = 235.5 mm2   OK)
         over 500 mm from every joint face, top and bottom of every column,
         AND THROUGH THE JOINT                              Cl. 8.2

DRIFT -- IS 1893 Cl. 7.11.1
   limit 0.004 x storey height = 12.8 mm (ground), 12.2 mm (first)
   Calculated drift under 3 mm.       Not critical, but CHECKED.
```

> **The roof joint at 101 against 138.5 is marginal and is printed as marginal.** Strong
> column–weak beam is the mechanism check that keeps the hinges in the beams; at the roof, where
> only one column continues above, the margin is naturally smallest. It passes, and it is flagged
> so that nobody reduces the roof beam's bottom steel without re-running it.

## 11.6 Isolated footing F1 — 1 500 × 1 500 × 600 on in-situ basalt at (−)2.000

> **Founded on IN-SITU ROCK, never on backfill. This is the whole reason the sentry post was
> relocated ≥ 10 m clear of the shelter excavation** — and Part 4.5's measured black cotton soil,
> CH at FSI 60–65 %, is why that insistence is now backed by a measurement rather than by instinct.

```
SERVICE  P = 167.5 (column) + 36.1 (EQ axial) + 33.75 (footing self) = 237.4 kN
         M (base, EQ)                                                =  29.3 kNm
         e = 29.3 / 237.4 = 0.123 m  <  L/6 = 0.250  -> NO TENSION    OK
         qmax = P/A (1 + 6e/L) = 105.5 x 1.494                        = 157.6 kPa
         vs presumptive SBC 3240 kPa (IS 1904 Table 1) [A]            = 4.9 %  OK
         vs measured SOAKED basalt 1961 kPa                           = 8.0 %  OK

ULS      Governing 1.5(DL + EL):  Pu = 1.5(148.4 + 36.127)            = 276.8 kN
         Mu = 1.5 x 29.27                                             =  43.9 kNm
         eu = 0.128 ;  qu,max = 276.8/2.25 x (1 + 6 x 0.128/1.5)      = 190.0 kPa

FLEXURE  Cantilever from the column face = (1500 - 350)/2             = 575 mm
         Mu = 190.0 x 0.575^2 / 2                                     = 31.4 kNm/m
         d = 600 - 50 (Cl. 26.4.2.1) - 8                              = 542 mm
         Ast,req 136 ;  Cl. 26.5.2.1 min 0.12 % x 600 = 720   <- GOVERNS
ADOPTED  T12 @ 150 c/c BOTH WAYS BOTTOM (754 mm2/m),  x/d 0.056

ONE-WAY SHEAR   IS 456 Cl. 34.2.4.1, critical at d from the column face:
         575 - 542 = 33 mm from the edge ;  Vu = 6.3 kN/m ; tau_v = 0.012  OK

PUNCHING   IS 456 Cl. 31.6.1, critical perimeter at d/2:
         b0 = 4 x (350 + 542) = 3568 ;  Vu = 276.8 - 190.0 x 0.892^2  = 125.6 kN
         tau_v = 0.065 ;  ks = (0.5 + beta_c) <= 1.0 = 1.0 ;
         tau_c = 0.25 sqrt(30)          Cl. 31.6.3.1                  = 1.369
         1.369  >>  0.065                                              OK

ANCHORAGE  Column starters T16: Ld,compression = 37 x 16               = 592 mm
         Available 600 - 50 - 24 = 526 straight + 8 phi bend 128       = 654 mm  OK

*** THE 600 mm DEPTH IS GOVERNED BY THE ANCHORAGE OF THE COLUMN STARTERS,
    NOT BY BENDING AND NOT BY SHEAR -- stated so that nobody "optimises"
    it to 350. ***
```

## 11.7 Lintel L1 and the wall ties — SP-B2

SP-B1 made the sentry post walls masonry but left **no lintel design and no tie detail**, so the
walls as recorded **could not be built.** Both are now designed. **This adds nothing to the frame
and changes no frame member.**

```
LINTEL L1 -- ONE TYPE OVER EVERY OPENING IN THE SENTRY POST

   190 wide x 150 deep, M30 / Fe500, cover 30, bearing 200 each end
   2-T10 bottom  .  2-T8 top (hangers)  .  T6 two-legged links @ 150

Openings served -- ELEVEN in all:
   ground   D1 900  and  W1 1200
   first    D1 900  and  the EIGHT 1200-wide vision-panel openings
The 1200 opening governs;  one type covers all.
```

**Design basis — and the reason it does not depend on an unknown.**

```
Effective span = min(clear + d, c/c bearings) = min(1315, 1400)
                                      IS 456 Cl. 22.2           = 1.315 m

*** THE OPENING HEIGHTS ARE NOT STATED ON ANY DRAWING -- WM-V3, still open.
    L1 is deliberately designed to the bound that does not depend on the
    height at all: masonry standing JUST BELOW the 60 deg arching height,
       0.866 x 1.315                                            = 1.139 m
    which is the HEAVIEST case any opening height can produce.
    Above it, arching relieves the lintel;  below it, there is less
    masonry.  THE DESIGN THEREFORE HOLDS WHATEVER WM-V3 IS RULED TO BE. ***

w = 0.190 x 20 x 1.139                                          = 4.33 kN/m
M = 0.935 kNm ;  V = 2.85 kN
Mu = 1.403 kNm   against   Mu,lim = 0.133 fck b d^2 = 10.03 kNm
                                                    -> 14 % UTILISED
Ast required 29.5 mm2
   IS 456 Cl. 26.5.1.1 minimum 0.85 b d / fy = 37.1 mm2  <- GOVERNS
   2-T10 = 157 mm2 provided
tau_v = 0.195  against  tau_c ~ 0.56 (M30, pt 0.72 %)
                                          -> NO SHEAR STEEL REQUIRED
   the T6 @ 150 links are the Cl. 26.5.1.6 nominal minimum
   (maximum spacing 324)

*** THE LINTEL CARRIES MASONRY ONLY.  The floor and the roof go to beams
    B1/B2 at each level, which is the whole point of the frame. ***
```

**Wall ties.** 6 mm dia MS ties at **every fifth course (≈ 450 mm)** up both column faces,
projecting **200 mm** into the bed joint, anchored to the column by a cast-in or
drilled-and-grouted 10 mm dowel. **The top course is built tight to the beam soffit and the last
joint packed** — because the analysis takes **R = 3.0**, the infill is **not** separated from the
frame **and must not be.** Separating it would be the R = 5.0 special moment frame case, which
this project does not claim.

> **What SP-B2 does NOT change.** No frame member, no footing, no slab, no storey height, no
> envelope. **Infill on the first-floor beams stays at 13.000 kN/m**: brick gives ≈ 9.88 kN/m,
> which is lighter, so the modelled value stays conservative. **`WM-V6` is still open** — the
> structural discipline must re-run the seismic check, and nothing here is a substitute for that.

# PART 12 — REINFORCEMENT REGISTER AND QUANTITIES

## 12.1 Underground box

| Element | Size | Cover | d (mm) | Main reinforcement | Links | A<sub>st</sub> prov | x<sub>u</sub>/d | Util. |
|---|---|---|---|---|---|---|---|---|
| **W1** south perimeter | 600 | 75/50/40 | 517 | **T16 @ 150 EF EW** | T12 closed @ 200 | 1340/face | 0.089 | 68 % |
| **W2** north perimeter | 600 | 75/50/40 | 517 | T16 @ 150 EF EW | T12 closed @ 200 | 1340/face | 0.089 | 68 % |
| **W3** west end | 600 | 75/50/40 | 517 | T16 @ 150 EF EW | T12 closed @ 200 | 1340/face | 0.089 | 68 % |
| **W4** east end | 600 | 75/50/40 | 517 | T16 @ 150 EF EW | T12 closed @ 200 | 1340/face | 0.089 | 68 % |
| **W5** Bay 5/6 | 200 | 40 | 154 | T12 @ 150 EF EW | — | 754/face | — | nominal |
| **W6** Bay 6/7 (M1) | **400** | 50/40 | 342 | **T20 @ 150 EF EW** | **T12 4L @ 200** | 2094/face | 0.211 | 69 % |
| **W7** Bay 7/8 (M1) | **400** | 50/40 | 342 | T20 @ 150 EF EW | T12 4L @ 200 | 2094/face | 0.211 | 69 % |
| **W8** partitions ×4 | 110 | 25 | — | A252 mesh both faces | — | 252 | — | non-structural |
| **MAT** | 600 | 75/50 | 517 | **T16 @ 150 EF EW** | **T12 @ 250 × 250 grid** | 1340/face | 0.089 | **84 %** |
| **ROOF** midspan | 900 | 75 | 812.5 | **T25 @ 150 EF EW** | T12 4L @ 250 end 1500 / 2L @ 300 mid | 3272/face | 0.139 | 51 % |
| **ROOF** cantilever pad | 900 | 75 | 812.5 | T25 @ 150 top continuous | **T12 4L @ 250 throughout** | 3272 | 0.139 | 56 % |
| Sump pit walls / base | 300/400 | 50 | 244 | T16 @ 150 EF EW | — | 1340 | — | nominal |

**Additional bars — underground box**

| Location | Requirement |
|---|---|
| Wall starters | T16 @ 150 EF, **900 mm horizontal leg into the mat**, lap 800 (50 φ) above a 150 mm kicker |
| Haunches, all wall–roof and wall–mat junctions | **500 × 500**, diagonal **T20 @ 150** |
| Mat edge, all free edges | **T16 @ 150 U-bars** closing both curtains |
| Sump pit opening | **4-T20 trimmers each face, each side**, L<sub>d</sub> 800 beyond |
| Blast door jambs (W6, W7) | **4-T20 each jamb, each face**, L<sub>d</sub> 800 beyond |
| Blast door header | 400 × 1100: **4-T20 top + 4-T20 bottom, T12 4L @ 150** |
| ESC 1 / ESC 2 collars | Collar 250 RC; **5-T25 each side, each face, each direction**, L<sub>d</sub> 1000 beyond; **T16 @ 150 hoops × 3 layers + T16 @ 150 radials**; slab thickened 900 → 1200 over a 600 annulus |
| Stair void free edge | Thickened 900 → 1200 over 600; **6-T25 top + 6-T25 bottom, T12 closed @ 150** |
| Stair void side bands | **6-T25 each face, top and bottom, in a 900 band over W6 and W7** |
| Stair void re-entrant corners (×2) | **4-T25 each face at 45°, 2000 long each way**, anchored L<sub>d</sub> beyond |
| Band beneath headhouse wall HW3 | **4-T25 extra top and bottom in a 1200 band**, lapped 1250 |
| Construction joints (~6 m) | Reinforcement **fully continuous**; two waterstops + welded Cu / galvanised EMP strap |

## 12.2 Stairs

| Element | Size | Cover | d | Main | Distribution | Top steel |
|---|---|---|---|---|---|---|
| **Main stair flight** waist | 200 | 30 | 164 | **T12 @ 150** (754) | T10 @ 200 (393) | T12 @ 150 for 800 into the flight, L<sub>d</sub> 480 |
| **Main stair landings** L1/L2/arrival | 200 | 30 | 164 | **T12 @ 125 bottom** (905) | T10 @ 200 | T12 @ 125 for 900 from each support |
| **Entry stairwell flight** waist | 250 | 30 | 214 | **T16 @ 200** (1005) | T10 @ 200 | T16 @ 200 for 1200 into the flight, L<sub>d</sub> 640 |
| Entry stairwell top landing | 250 | 30 | 214 | T12 @ 200 EF EW (565) | — | — |
| Entry stairwell platform | 250 | 30 | 214 | T12 @ 200 EF EW | — | on fill |
| Entry stairwell side walls | 250 | 50 | 194 | T12 @ 200 EF EW | — | minimum steel governs |
| Entry stairwell raking roof | 250 | 30 | 204 | T12 @ 200 EF EW | — | minimum steel governs |
| Entry stairwell headwall | 250 | 30 | 214 | T12 @ 200 EF EW | — | — |
| Entry door lintel (1000 clear) | 250 × 350 | 30 | 306 | 3-T12 top + 3-T12 bottom | T8 @ 150 | — |
| Stepped raft | 300 | 50 | 244 | T12 @ 200 EF EW | — | on compacted fill |
| **Opening-corner U-bar** (top of entry flight) | — | — | — | **T16 @ 200 U-bar**, bars CROSSED and anchored L<sub>d</sub> 640 into the opposite face | | **SP 34 Cl. 5.5** |

## 12.3 Headhouse

| Element | Size | Cover | d | Main | Links |
|---|---|---|---|---|---|
| **Roof** | 500 | 75 | 415 | **T20 @ 150 EF EW** (2094) | **T12 4L @ 175 in the end 1200 each side; @ 250 elsewhere** |
| **Walls HW1–HW4** | 400 | 50/40 | 342 | **T16 @ 150 EF EW** (1340) | **T12 4L @ 250 throughout** |
| Door jambs, HW2 | — | — | — | **2-T20 each jamb, each face**, L<sub>d</sub> 800 beyond | — |
| Door head edge band | 400 × 800 | 40 | 742 | **4-T20 top + 4-T20 bottom** | T12 4L @ 150, over the opening + 600 each side |
| Wall–roof haunch | 300 × 300 | — | — | diagonal T16 @ 150 | — |

## 12.4 Sentry post

| Element | Size | Cover | d | Reinforcement |
|---|---|---|---|---|
| **Slab S1** bottom | 150 | 30 | 116/108 | **T8 @ 150 c/c BOTH WAYS** (335 mm²/m) |
| Slab S1 top, discontinuous edges | 150 | 30 | 116 | **T8 @ 300, 400 mm (0.1 L) into the span, all four edges** — Cl. D-1.6 |
| Slab S1 corner torsion | — | — | — | **T8 @ 200, FOUR LAYERS, 700 × 700 at all four corners** — Cl. D-1.8 |
| **Beam B1** (3650) | 250 × 450 | 30 | 404 | **4-T16 top at supports; 2-T16 bottom continuous** |
| **Beam B2** (4650) | 250 × 450 | 30 | 404 | **3-T20 top at supports; 2-T20 bottom continuous** |
| Beam hoops, both | — | — | — | **T8 2-leg @ 100 over 2d = 810 from each face; @ 150 elsewhere**; first hoop ≤ 50 from the face |
| **Column C1** | 350 × 350 | 40 | d′ 56 | **8-T16** (1608 mm², p = 1.31 %) |
| Column confining hoops | — | — | — | **T10 hoops + 1 cross-tie each way @ 85 c/c over 500 mm from every joint face, top and bottom, AND through the joint** |
| Column general ties | — | — | — | T8 @ 150 c/c elsewhere |
| Plinth beam PB | 250 × 400 | 30 | 354 | 3-T12 top + 3-T12 bottom |
| **Footing F1** | 1500 × 1500 × 600 | 50 | 542 | **T12 @ 150 both ways bottom** (754 mm²/m) |
| **Lintel L1** ×11 | 190 × 150 | 30 | — | **2-T10 bottom + 2-T8 top, T6 2-leg links @ 150**, bearing 200 each end |
| Wall ties | — | — | — | 6 mm MS at every 5th course (≈ 450), 200 into the bed joint, 10 mm dowel |

## 12.5 The six that matter

```
ROOF        T25 @ 150 EF EW  .  T12 4L @ 250 end 1500 / 2L @ 300 mid     51 %
WALLS       T16 @ 150 EF EW  .  T12 closed @ 200                         68 %
W6/W7       T20 @ 150 EF EW  .  T12 4L @ 200                             69 %
MAT         T16 @ 150 EF EW  .  T12 @ 250 x 250 grid                     84 %
HH ROOF     T20 @ 150 EF EW  .  T12 4L @ 175 / 250                       90 %
HH WALLS    T16 @ 150 EF EW  .  T12 4L @ 250                             59 %
```

## 12.6 Quantities — package SC1

> **Sentry post excluded** — no sentry post bar, quantity or weight appears in the structural CAD
> schedules.

| Bar | Unit mass kg/m | No. of bars | Total length m | Weight kg | % of total |
|---|---|---|---|---|---|
| T8 | 0.395 | 13 | 14.6 | 5.7 | 0.0 % |
| T10 | 0.617 | 85 | 102.6 | 63.3 | 0.1 % |
| **T12** | 0.888 | 13 814 | 22 885.7 | **20 318.3** | 28.8 % |
| **T16** | 1.578 | 3 698 | 15 020.2 | **23 707.1** | 33.6 % |
| **T20** | 2.466 | 1 440 | 4 429.1 | 10 922.8 | 15.5 % |
| **T25** | 3.853 | 654 | 4 006.7 | 15 439.4 | 21.9 % |
| | | **19 704** | **46 458.9** | **70 456.7** | 100 % |

| Element group | Weight kg | Weight t | % |
|---|---|---|---|
| FOUNDATIONS | 14 665.2 | 14.665 | 20.8 % |
| WALLS | 24 725.6 | 24.726 | 35.1 % |
| ROOF SLAB | 20 490.5 | 20.490 | 29.1 % |
| BEAM-TYPE ELEMENTS | 297.1 | 0.297 | 0.4 % |
| MAIN STAIRCASE | 281.3 | 0.281 | 0.4 % |
| HEADHOUSE | 8 364.2 | 8.364 | 11.9 % |
| ENTRANCE / ENTRY STAIRWELL | 1 632.8 | 1.633 | 2.3 % |
| **TOTAL** | **70 456.7** | **70.46** | 100 % |

**Concrete, in scope:** mat 81.8 + pressure slab 112.0 (net of openings) + perimeter walls 103.7
+ W6/W7 12.8 + W5 3.2 + headhouse 32.7 + main staircase 3.0 + entry stairwell 19.9 =
**369.2 m³**, excluding blinding and the sump pit.

> **Average steel density ≈ 191 kg/m³.** For a blast-hardened buried box whose bar spacing is set
> by the **150 mm EMP rule** rather than by strength, and whose sections are thick (900 roof,
> 600 walls and mat), that is a plausible figure. **It is a sanity check, not a design check.**

**Quantity basis — declared, not assumed:**

- **PBR-1** — cut length = Σ scheduled leg dimensions, **no bend deduction taken**; links add
  2 × 10 φ for 135° hooks. Conservative by ≈ 2 φ per 90° bend. Bend deductions to BS 8666 Table 3
  shall be applied by the fabricator on the approved schedule. **`[A]` — no bar-bending standard
  is in the workspace; IS 2502 is NOT held and NOT cited.**
- **P-1** — stock bar 12 000 mm; longer runs split into equal pieces with 50 φ laps added.
- **PBR-2** — a 4-legged link @ s is scheduled as **two** closed links per node on an s × s grid;
  a 2-legged link @ s as one.
- **PBR-3** — the stair void and the two escape openings are **deducted zone by zone**.
- Quantities are for **tender and estimating** and must be re-measured on the approved bar bending
  schedule.

**Not quantified, and declared as such:** the five blast valves with their sleeves and trimming
(sizes are on the services sheet, not in the structural design); the service entry plate (size
`[N]`); and the ventilation / CBRN duct penetrations (no penetration schedule exists).
**All three are NOT DETERMINABLE from the information the project holds, and none is fabricated.**

# PART 13 — DRAWINGS AND DRAWING QUALITY

## 13.1 Two distinct DXF sets — do not confuse them

| Set | Origin | Revision | Purpose |
|---|---|---|---|
| **Input set** (10 files) | Supplied by the project owner | **Rev F** | Architectural / civil geometry — **the primary geometry source.** Directly editable |
| **Output set** (S-01 … S-08) | Generated in this project | **Phase 2 Rev A** | Structural drawings with reinforcement. **Generated — edit the script, never the DXF** |
| Discipline sets | Generated in this project | per package | Structural CAD, drainage, HVAC, finishes, fire, concealment, EMP, electrical, site |

## 13.2 The package as it stands: 80 DXF, 74 PASS

| Discipline | Sheets |
|---|---|
| **Architectural / general — Rev F** | 11 (`A-101`…`A-301`, plus the services sheet `S-06`) |
| Architectural — finishes | 3 (`A-601`, `A-611`, `A-612`) |
| **Structural — reinforcement** | **30** (`R-001`…`R-805`) |
| Drainage | 11 (`D-001`…`D-305`) + 2 handout |
| HVAC | 6 (`M-001`…`M-203`) + 2 handout |
| Fire and life safety | 2 (`F-101`, `F-102`) |
| Site and concealment | 1 (`C-101`) |
| EMP protection | 6 (`EM-001`…`EM-302`) |
| Electrical | 1 (`E-001`) |
| Site selection and geotechnical | 5 (`SG-001`…`SG-202`) |
| **TOTAL** | **80 DXF · 75 A1 · 4 A4 · 1 A0** |

**The drawing index is generated from the DXF files themselves**, so it cannot drift from the
drawings. Filenames are deliberately unchanged — every document in the project cites the current
filenames — so the drawing number lives in the title block and the index carries both.

## 13.3 Drawing QA/QC — QA1 and QA2

**QA1 (9 September 2026)** inspected and corrected 65 DXF **in place**, at the same filename and
folder. Scope: drafting, annotation, sheet composition and title blocks only.

| Measure | Before | After |
|---|---|---|
| DXF inspected / edited in place | — | **65 / 65** |
| **Text-on-text overlaps, all 65 drawings** | **67** | **2** |
| · of which, the 54 generated sheets | 49 | **0** |
| · of which, the 11 Rev F drawings | 18 | **2** |
| Annotation crossing hard line work (Rev F sheets) | **50** | **10** |
| A view drawn on top of its own notes panel | 3 sheets | **0** |
| Entities outside the sheet border | 0 | **0** |
| Drawings with a border and title block | 54 of 65 | **65 of 65** |
| Panel / table body text below print size (1.4 mm on A1) | most of the package | **0** — floor is now 2.0 mm |
| Generated packages rebuilding clean | 54/54 | **54/54, 0 errors** |

> **No engineering value was changed anywhere by the QA pass.** No dimension, level, bar mark, bar
> size, spacing, load, material grade, thickness or room size was touched, and the frozen staircase
> geometry was not touched.

**QA2 (11 September 2026)** re-scanned the whole package at **80 DXF, 74 PASS**, after **twelve
sheets added by the EMP, electrical and site packages were found to be invisible to the index
tool**.

> **That is a process failure with a process fix, and it is recorded as a working rule.** A new
> drawing package **must register itself with the QA tool** — add its `DXF/` prefix to `DISCIPLINE`
> in `qa_report_data.py` and its name to `ORDER` in `make_index.py`, then re-run both. **Twelve
> sheets were invisible to the index for four revisions because this was not done.**

## 13.4 Sheet standard

```
SHEET SIZE     A1, 841 x 594 mm, DRAWN IN PAPER MILLIMETRES, PLOT 1:1
               (one A0 -- the front elevation, which is 880 mm at 1:50 and
                cannot fit A1;  four A4 handout sheets)
DXF FORMAT     AutoCAD R12 ASCII -- opens in AutoCAD, DraftSight, BricsCAD,
               LibreCAD and QCAD without translation
BORDER         outer 0,0-841,594 ;  inner 10,10-831,584
TITLE BLOCK    180 x 62 mm, bottom right, at x0 = 651, y0 = 10
VIEW SCALES    each view carries its own scale note;  views are mapped from
               model millimetres to paper millimetres by
                  paper = origin + model / scale
TEXT HEIGHTS   3.4 view titles | 2.4 panel headings | 2.0 scale notes
               1.6-1.7 general | 1.55-1.62 panel body | 1.4-1.5 small
VALIDATION     SECTION/ENDSEC balanced, EOF present, no undeclared layer,
               all geometry within the sheet extents
```

**22 layers, identical in every generated file** — `CONC`, `CONC-HIDDEN`, `REINF-MAIN` (red),
`REINF-DIST` (green), `REINF-LINK` (magenta), `REINF-SEC` (cyan), `DIM`, `TEXT`, `TEXT-TITLE`,
`HATCH`, `GRID`, `SOIL`, `CENTRELINE`, `TITLEBLOCK`, `WATERPROOF` (orange), `STEELWORK` (yellow),
`LEVELS`, `NOTES`, `TABLE`, `SERVICES`, `BLAST` (red), and `0`. **Dashed lines are drawn as
explicit segments, not by linetype**, for maximum compatibility.

## 13.5 Two rulings about the drawings that are worth reading

> **QA-1 — the front elevation cannot be plotted at 1:50 on A1, and A0 is the only answer.** The
> drawing is 880 mm wide at 1:50 against an A1 printable width of 821 mm. **The scale is a
> measurement statement and must not be changed to fit the paper**, and splitting the sentry post
> onto its own sheet would break a continuous 44 m elevation, which is the whole point of the
> drawing. **A0 keeps both the scale and the drawing intact.**
>
> **QA-2 — six sheets do not fill their paper, and that is accepted as drawn.** Six sheets share
> an empty strip. **Every one of them is correct, complete and legible; emptiness is not an
> error.** Re-scaling would make the stated scale a layout variable instead of a measurement
> statement — 1:20 is the right scale for a 400 mm wall section regardless of how much paper it
> leaves. Combining or renumbering would break cross-references, the index and the sheet numbering
> **for zero engineering benefit.** And reflowing the blocks **moves** the void, it does not remove
> it.

## 13.6 What cannot be regenerated, and is not invented

> **Seven of the eight S-series structural sheets are ABSENT and CANNOT be regenerated.** The
> Part E.4 toolchain — `proj.py`, `dxflib.py` and the eight sheet generators — is **not in the
> workspace**. `S-01` … `S-05`, `S-07` and `S-08` therefore cannot be rebuilt, and **they are not
> fabricated.** **`S-06` is present and is already at M1.**
>
> **Also not in this workspace and not invented:** the Phase 1 Rev D report, `SK02_Underground_Plan.png`,
> and the nineteen STAAD screen captures.
>
> **And the sentry post beams, columns and footings are not yet drawn.** A future sheet `S-09`
> would carry B1 4-T16 / 2-T16, B2 3-T20 / 2-T20, C1 8-T16 with T10 confining hoops @ 85, and F1
> 1500² × 600 with T12 @ 150 B/W. **Everything it needs is in Part 11; the sheet does not exist.**

## 13.7 The two most recent drawing changes

**DR-A1 and DR-A2** put the drainage items onto the Rev F architectural sheets — the sump pit on
the side section, the septic tank and soak pit on the front elevation beyond a break, and then at
DR-A2 the sump pit's **cover** at (−)6.100 and a **1:200 key plan** carrying the sump, the septic
tank and the soak pit at true project X **and** Y. **No design value changed in either.**

> **And DR-A2 found something the drawing could not avoid asking.** The mat is genuinely
> interrupted over the clean sump — the reinforcement register trims a **1 500 × 1 500 opening**
> with 4-T20 each face each side, the bar schedule calls it an opening, and the bill measures the
> mat gross by its 1.35 m³. **A 1 500 × 1 500 hole through the floor is what the project records,
> so that is what was drawn — and then Bay 5 is 1 560 mm clear and the pit is 1 500 of it.**
>
> **With the opening open there is no route past it** to the two filter trains, the CO₂/O₂ plant or
> the dehumidifier; and the room finish schedule falls that room **1:80 direct to the sump**, so
> whatever closes it has to pass water. **A cover is not optional here — and the project contains
> no cover: no type, no depth, no duty, no fixing, no lifting arrangement, in any schedule,
> drawing or document.** The cover is drawn as one diagrammatic line, tagged `[A]`, with its
> specification tagged `[N]`, and **`DR-A2-V1` was opened for it.** Nothing was converted.

# PART 14 — SERVICES, CBRN, EMP AND LIFE SAFETY

## 14.1 HVAC and CBRN filtration

### 14.1.1 The basis, and the eleven figures that reproduce

The ventilation basis existed on the issued services sheet before the HVAC package started. **That
package re-derived every figure from first principles rather than carrying them forward**, and all
eleven reproduce:

| Stated | Reproduced from | Result |
|---|---|---|
| Gas-tight envelope **67.8 m² / 217.0 m³** | Bay widths 2900+1800+3500+1800+1560+2000 × 5.000 × 3.200 | **67.80 / 216.96** |
| Clean zone **57.8 m²** | Envelope less the 10.0 m² decon airlock | **57.80** |
| Occupied volume, airlock shut **185.0 m³** | 57.80 × 3.200 | **184.96** |
| FEMA 453 rate **264 m³/h** | 57.8 m² = 622.2 ft² × 0.25 cfm/ft² | **264.3** (0.10 %) |
| Leakage **32.5 m³/h** | 0.15 vol/h × 216.96 | **32.5** = **10.8 %** of one train |
| Time to 1.0 % CO₂ **9.9 h** | (0.0096 × 184.96) / (9 × 0.02) | **9.9** |
| Airlock purge **13 min** | 5 × (2.0 × 2.0 × 3.2) = 64 m³ at 300 m³/h | **12.8 min** |
| DN100 throat **10.6 m/s** | 300 / 3600 / (π × 0.05²) | **10.61** |
| DN350 throat **7.5 m/s** | 2600 / 3600 / (π × 0.175²) | **7.51** |
| Survival / working rates | 5 × 9 = 45, 15 × 9 = 135 m³/h | **reproduces** |
| O₂ store **15 m³** | 2 × 50 L at 150 bar | **80 h** at 4.5 m³/day |

**Every figure reproduces. The sheet is internally consistent.**

### 14.1.2 Design basis

| Parameter | Value | Class |
|---|---|---|
| Occupancy / endurance | **9 persons / 96 h** | `[C]` |
| Design flow | **300 m³/h**, 2 × 300 trains, **true N+1** | `[C]` |
| — against the three criteria | 6.7 × survival · 2.2 × working · 1.14 × FEMA | `[R]` |
| — per person | **33.3 m³/h** | `[R]` |
| Air changes, whole envelope / clean zone | **1.38 / 1.62** | `[R]` |
| Leakage | ≤ 0.15 vol/h at +300 Pa = **32.5 m³/h**, 11 % of one train | `[C]`/`[R]` |
| Operating overpressure | **+50 to +100 Pa**, tested at +300 Pa | `[C]` |
| Cascade | **0 → +10 → +20 → +35 → +50 Pa** | `[C]` |
| Closed mode | CO₂ 0.18 m³/h; **9.9 h** unscrubbed, **48 h** on soda lime, **80 h** on O₂ | `[C]`/`[R]` |
| Airlock purge | 64 m³, **12.8 min**, **4–5 persons/hour** | `[R]` |
| Ductwork + plenum loss | **161 Pa** | `[R]` |
| **Total fan duty** | **VENDOR DATA REQUIRED** — 5 of 8 components | `[N]` |
| **Cooling load** | See Part 2.11 and `RC4-V1` | — |

**Room-by-room distribution — developed in this project.** The nine occupants are not in two
places at once: they work in the ops room and sleep in the berthing bay. A single fixed split
would starve whichever of the two is occupied, so the distribution is **balanced in two modes on
two volume control dampers**:

| Room | Use | Volume m³ | Day m³/h | Night m³/h | Extract |
|---|---|---|---|---|---|
| U-01 | Emergency stores / ESC 1 | 46.40 | 30 | 30 | — |
| U-02 | Lavatory + medical | 28.80 | 30 | 30 | **45** |
| U-03 | Ops room and hazard plotting | 56.00 | **135** | 45 | — |
| U-04 | Berthing, 9 berths | 28.80 | 45 | **135** | — |
| U-05 | CBRN plant + sump | 24.96 | 60 | 60 | — |
| U-06 | Decon airlock | 32.00 | *300 transfer* | *300 transfer* | *to BV-3* |
| | **TOTAL** | | **300** | **300** | |

> **The occupied room of the pair gets 135 m³/h = 15.0 m³/h per person — exactly the
> working-shelter rate the sheet names as its second criterion.** Holding that rate in *both* rooms
> at once would take 270 of the 300 m³/h and leave 30 for the stores, the lavatory *and* the plant
> room. **If a reviewer requires that, the total must rise above 300 m³/h — which is a change to a
> confirmed value. Raised, not taken.**
>
> **Nothing is supplied to Bay 6.** The airlock is the exhaust path: the whole 300 m³/h transfers
> through the three decon stages and out at BV-3, **which is what makes the confirmed cascade
> work.** The cascade maps exactly onto the three airlock stages.

### 14.1.3 Findings

| Ref | Finding |
|---|---|
| **HV-F1** | **The soda lime, not the oxygen, limits closed mode** — 9.9 h unscrubbed, 48 h on soda lime, 80 h on O₂. **The consumable to count, and the one to write on the drill card.** Closed mode covers 48 of the 96 h; **the other 48 h require filtration** |
| **HV-F2** | **The raw-air duct is a protective element, not a duct.** The fresh-air blast valves are in the west wall of Bay 1 and the filter trains are in Bay 5. **Between them the air is unfiltered, and the duct carries it 11.2 m through the clean zone.** Over that length the duct wall is the only barrier. Positions are not changed — they are confirmed on an issued sheet — but the duct is specified as protective: **fully welded, no push-fit or slip joint, tested to the +300 Pa envelope standard, run visible and never boxed in, labelled RAW AIR — UNFILTERED at ≤ 2 m centres, re-tested after any work in bays 1–4.** *Should the trains move to Bay 1? — raised, not taken* |
| **HV-F3** | **Maintenance access is the tight dimension, not headroom.** Each train is 1 450 wide in a 1 560 clear bay — **110 mm at the sides** — so all access is along the bay, and a HEPA or carbon cassette must come in through Blast Door 1 (1200 × 2100) and along bays 6 and 5. **Confirm the cassette dimensions against that route before the trains are ordered** |
| **HV-D1** | **No filter bypass for peacetime running.** Without one, every peacetime hour spends carbon-bed life replaceable only in closed mode. A bypass is a deliberate leak path around the filters — **a protective decision. Not added** |
| **HV-D2** | **BV-3 discharges into Bay 7**, and the onward path to atmosphere — up the stair shaft, out through the headhouse — **is not recorded anywhere.** A path exists; its resistance is unknown and it is in series with the relief valve |
| **HV-D4** | **No noise criterion exists anywhere in the project.** Terminal selection cannot be closed, and **a berthing space for nine is exactly where a noisy diffuser is felt** |
| **HV-D6** | **Fan static pressure — 5 of 8 loss components are vendor data.** The derivable part is 161 Pa. **Quoting a total without the vendor figures would be a fabricated number.** The fan must be selected on the **dirty** figure, and the hand crank sized on the same duty |

### 14.1.4 Operating modes

| Mode | Condition |
|---|---|
| 1 NORMAL | Peacetime, unfiltered or lightly filtered |
| 2 FILTERED / PROTECTIVE | Full seven-stage train, overpressure held |
| 3 **CLOSED** | Detonation to all-clear. **All five blast valves shut.** Soda lime and O₂ only. **48 h limit** |
| 4 PURGE | Airlock purge cycle |
| 5 GENERATOR RUNNING | **BV-4 and BV-5 open.** Bay 8 only — does **not** touch the gas-tight envelope. **Independent of modes 1–4** |

> **Modes 3 and 5 contradicted each other, and the contradiction was worth a factor of twelve.**
> Mode 3 shuts all five valves; Mode 5 needs two of them open. **RULED — RC2: the valves shut at
> the shock and hold 1.3 s, then BV-4 and BV-5 are REOPENED for generator operation.** Bay 8 is
> outside the gas-tight envelope, so the clean zone is unaffected, which is exactly what the Mode 5
> note always said. **The battery is therefore a 4 h cabinet (149 Ah) and not a 48 h room
> (1 783 Ah, 2.4 tonnes, 4.8 m² of floor) — and there is nowhere to put the latter.**
>
> **One consequence, recorded not resolved:** reopening BV-4 and BV-5 leaves **two DN350 bores open
> through the post-attack period** — the two that fail both EMP criteria (Part 2.8.3). That
> **sharpens** the EMP boundary question without deciding it.

## 14.2 Drainage

**Concept — a tanked box, not a drained one** (Part 6.4). Collected flow:

```
structural seepage                        200 L/day   [C]
condensate and washdown                   200 L/day   [C]
                                    TOTAL 400 L/day = 0.00463 L/s
```

**And the seepage figure's basis, reconstructed because the sheet did not state it:**

```
submerged wall height  (-)2.000 -> (-)6.700               = 4.700 m
external perimeter     2 x (22.0 + 6.2)                   = 56.40 m
submerged wall area    56.40 x 4.700                      = 265.08 m2
mat underside          22.0 x 6.2                         = 136.40 m2
                                                    TOTAL = 401.48 m2
0.5 L/m2/day x 401 m2                                     = 200 L/day
```

> **It is the external envelope standing below the design water table — not the internal wetted
> area.** Recording this matters: **if the water table is confirmed higher than (−)2.000, the
> wetted area, the seepage and the sump duty all move together**, and the relationship is now
> explicit.

| Item | Adopted | Class |
|---|---|---|
| Floor falls | transverse **1:80** in wet areas, **1:100** elsewhere; spine **1:400** east to the sump along Y 3100 | `[A]` |
| Fall formed in | **floor screed** — 25 mm minimum at the sump edge rising to 78 mm at the far corner; **area-average 52 mm** | `[A]`/`[R]` |
| Gravity drains | **DN100** minimum at 1:100 minimum | `[A]` |
| Capacity, DN100 at 1:100 | 6.72 L/s at 0.85 m/s — self-cleansing | `[R]` |
| **Capacity ratio against the design flow** | **1 450 : 1** | `[R]` |
| Traps | **75 mm deep seal** throughout, **primed** | `[A]` |
| Rising main | **DN50**, 0.76 m/s at 1.5 L/s; welded or flanged, **no push-fit joint inside the envelope** | `[A]` |
| Clean sump | **3.375 m³**, invert (−)7.600, base slab (−)8.000; 2 × 1.5 L/s submersible + **hand pump PU-03** | `[C]` |

> **Internal drainage is governed by minimum bore and self-cleansing velocity, not by flow** — the
> capacity ratio is three orders of magnitude. **Stated so that no reviewer looks for a hydraulic
> sizing calculation the flows do not justify.**

**Trap seals against shelter overpressure** (Part 2.7.1):

| Seal depth | Holds | vs +100 Pa operating | vs +300 Pa test |
|---|---|---|---|
| 50 mm | 491 Pa | 4.9 : 1 | 1.6 : 1 |
| **75 mm (adopted)** | **736 Pa** | **7.4 : 1** | **2.5 : 1** |
| 100 mm | 981 Pa | 9.8 : 1 | 3.3 : 1 |

**Sewage.** In protective mode the shelter is sealed and uses **sealed-cassette chemical toilets —
nothing is discharged.** The septic tank serves **peacetime use only**: design population 10,
45 lpcd = **450 L/day**, tank **1.5 × 0.75 × 1.0 m** liquid to IS 2470 (Pt 1) Table 1, two
compartments, baffle at ⅔ L, inlet and outlet tees, 50 mm cowled vent ≥ 2 m above grade. Every
IS 2470 (Pt 1) check reproduces: **450 L detention + 600 L sludge = 1 050 L required against
1 125 L provided (+7.1 %)**; L/B = 2.0; B = 750; depth 1.00 m; freeboard 300 → overall 1.30 m.
**PASS.**

**Findings.**

| Ref | Finding |
|---|---|
| **DR-C2, ruled and closed** | **The soak pit was 2.3 % short on its own stated requirement** — π × 2.0 × 3.5 = **21.99 m²** printed as "22.0 OK" against "22.5 required". **Arithmetic, not judgement. RULED: SK-01 is WIDENED, 2.0 → 2.200 m diameter, depth UNCHANGED at 3.500 m → 24.19 m², +7.5 %.** Widened rather than deepened because **deepening drives the pit further below the design water table, where it cannot soak at all.** The mandatory percolation test still governs the final size |
| **DR-C1, ruled and closed** | **A superseded catchment.** The 0.10 L/s for stairwell surface water is the **Rev E open-cut** figure — 7.2 m² of open pit at 50 mm/h. At Rev F the approach is covered, the door is at grade, and the sheet's own note states the catchment with the door shut is **zero**. **RULED: Rev F governs, and 0.10 L/s is RETAINED as a declared conservatism** — removing it changes no pump, pipe or pit (the stairwell pump is 20 × it) and **deleting a superseded number would hide the history.** Both figures are shown and labelled |
| **DR-F1** | The clean sump cycles **once every 3.4 days**, 15 min per start, **0.31 % duty ratio**. Cycling is fine — but **at that duty a failed standby would never be discovered by use.** A witnessed monthly test of the standby path and the hand pump is required |
| **DR-F2** | A drained screed reduces the **finished** clear height from the structural 3 200 to between **3 122** (far corner) and **3 175** (sump edge). **A client-facing number must say which one it is** |
| **DR-F4** | **A drained floor cannot be built inside the 1.0 kPa mat allowance.** At 24 kN/m³ that buys 42 mm of screed; the adopted grading averages **52 mm = 1.24 kPa**, an excess of **0.24 kPa = 25 kN** over the 104 m² floor — 1.2 % of the mat's own weight, 0.4 % of the uplift, and **acting in the FAVOURABLE direction for flotation.** Referred to the structural engineer, not assumed |
| **DR-F5** | **The protective boundary creates three hydraulic zones and two have no drainage destination.** Zone 1 (bays 1–5) → clean sump, complete. Zone 2 (bay 6 decon) → its tank, which the sheet draws in **bay 8, across the boundary** — route undefined. Zone 3 (bays 7–8) → **nothing recorded.** A protective-design decision |
| **BW-01** | **Builder's work, requested and not accepted.** The one buried drain inside the envelope needs a 300 wide recess in the top of the mat, 150 deep rising to 216, **leaving 384 of the 600 mat locally on the line of the peak transverse sagging moment.** Structural engineer to accept or refuse; a fallback with no buried drain at all is drawn |
| **DR-D1** | Rainfall intensity **50 mm/h** is the only intensity in the project. **No return period, duration or IDF source** |

## 14.3 Electrical and power

> **A basic package, on purpose. It stops at board level**: sources, a load schedule, three
> boards, the essential / battery system, one single-line diagram. **No circuit schedule, no cable
> sizing, no luminaire or socket layout, no protection study** — that is a **declared scope
> boundary**, not a gap.

| Tag | Load | Board | kW | Class |
|---|---|---|---|---|
| L-01 | General lighting, bays 1–8, LED | DB-E | 0.520 | `[A]` |
| L-02 | Emergency lighting, maintained, DC | DB-E | 0.100 | `[A]` |
| P-01 | Small power, socket outlets | DB-M | 1.000 | `[A]` |
| F-01 | Filter train fan, **1 duty of 2** | DB-E | 0.379 | `[R]` |
| D-01 | Dehumidifier | DB-E | 1.000 | `[A]` |
| U-01 | Clean sump pump, **1 duty of 2** | DB-E | 0.334 | `[R]` |
| U-02 | Stairwell pump, **1 duty of 2** | DB-M | 0.223 | `[R]` |
| Z-01 | **EMP Zone 2 ops / comms** | DB-Z2 | 1.500 | `[A]` |
| S-01 | Fire detection and alarm panel | DB-E | 0.100 | `[A]` |
| B-01 | Battery charger / inverter | DB-M | 0.800 | `[A]` |
| G-01 | Generator auxiliaries | DB-M | 0.300 | `[A]` |
| | **CONNECTED LOAD** | | **6.256 kW** | |
| | at power factor 0.85 | | **7.360 kVA** | |

**Standby units are not counted twice** — the standby fan and the two standby pumps never run
simultaneously with their duty partners.

```
GEN-1 rating                                            = 15.0 kVA   [C]
Connected load                                          =  7.360 kVA
UTILISATION                                             = 49.1 %
Spare                                                   =  7.64 kVA
Largest motor, the filter fan 0.379 kW;  DOL start      ~  2.7 kVA
```

> **The confirmed 15 kVA is about twice the connected demand, and 49 % sits in the healthy loading
> band for a diesel set** — high enough to avoid wet-stacking, low enough to carry growth. **There
> is no starting problem and the project's own figure needs no change.**

**Three boards, one cable entry:** `DB-M` main LV in Bay 8 (outside the gas-tight envelope, mains
+ generator with changeover); `DB-E` essential in Bay 5 (inside the envelope, fed from DB-M and
from the battery inverter on loss of both sources); `DB-Z2` inside the shielded enclosure in Bay 3,
fed from DB-E **through the PCI on the Zone 2 boundary**.

**The essential system** — emergency lighting 0.100 + reduced general lighting 0.150 + fire
detection 0.100 + EMP Zone 2 at 50 % 0.750 + clean sump pump intermittent 0.033 + CO₂ scrubber
recirculation fan 0.100 + instruments 0.050 = **1.283 kW**, carried for **4 h** on **149 Ah at
48 V** (depth of discharge 0.80, inverter efficiency 0.90).

> **Groundwater does not stop because the shelter is sealed.** The clean sump pump has to stay
> powered through the closed mode — and **hand pump PU-03 is what covers it if the battery fails.**
>
> **And two sources need no electricity at all, both already confirmed: a hand crank on both filter
> fans, and the hand pump. These are the real last line, the project already has them, and no
> electrical design should be allowed to obscure them.**

**The CO₂ scrubber, recovered from the project's own arithmetic** (owner ruling 25, RC7):

```
Q = production / (eta x C_target)

   target CO2      eta 0.50   eta 0.80   eta 0.95
      0.5 %           72.0       45.0       37.9   m3/h
      1.0 %           36.0       22.5       18.9   m3/h

ADOPTED   75 m3/h recirculation loop -- the worst cell, because designing to
          it costs almost nothing.

CHECK     a 75 m3/h fan at an assumed 250 Pa across a packed bed draws
          ~ 11.6 W against the 0.10 kW allowance  --  roughly 8 x margin.
          NO ELECTRICAL VALUE CHANGES;  the allowance is now CHECKED
          rather than assumed.
```

**Not designed, not invented `[N]`:** the absorber vessel, bed depth, face area, residence time;
the **soda lime charge** (17.28 m³ of CO₂ is the duty — converting it to a mass needs vendor
absorption capacity); the single-pass efficiency; and **where in Bay 5 the absorber stands**, the
tightest bay at 1 560 clear where the filter trains already leave 110 mm at the sides.

**The generator day tank** (owner ruling 20, RC5):

```
600.6 kWh over 96 h  x  0.35 L/kWh [A]                        = 210.2 L
ADOPTED   210 L usable  .  250 L nominal  .  275 L bund (110 %)
          BAY 8 -- outside the gas-tight envelope, INSIDE the EMP boundary
          welded steel, bunded, contents gauge, low-level alarm to the panel

THE FILL AND THE VENT ARE THE REAL DESIGN QUESTION, NOT THE TANK.
   Both cross the protective boundary, and bay 8 is inside the EMP boundary,
   so two new bores would each need blast, gas AND EMP treatment -- in the
   same wall where BV-4/BV-5 already FAIL the EMP criteria.

ADOPTED   route both up the EXISTING SH-2 bore and add NO NEW PENETRATION
          -- DN25 metallic fill with a lockable cap at the SH-2 head,
             DN25 metallic gooseneck vent, both bonded to the shaft earth.
```

> **Use what already crosses.** That instinct — never make a new hole in a protective boundary if
> an existing one can be shared — appears twice in the rulings, here and on the heat rejection.
> **It still needs an HVAC and EMP fit check: two DN25 lines sharing a 600 × 600 bore with two
> DN350 blast valves is a fit that has not been checked `[A]`.** Fuel type unconfirmed, the
> 0.35 L/kWh rate still `[A]`, no vendor set, no fuel polishing, no tank fire suppression.

## 14.4 EMP protection

### 14.4.1 The zone model — adopted by the project owner

| Zone | What it is | Performance | Verification |
|---|---|---|---|
| **EMP ZONE 0** | Everything above grade — sentry post +7.000, headhouse +0.900 **with no earth cover**, covered stairwell +2.450 (**expendable**), shaft heads, burster slab | **None credited** | n/a |
| **EMP ZONE 1** | The buried box, **all eight bays**. The reinforcement cage | **99.99 dB at 10 kHz → 0 dB at 999 MHz**, pierced by an 8.85 m² stair void and two 1 400 shafts. **80 dB only below 99.93 kHz** | **Cannot be surveyed** — no accessible exterior under 2 m of cover |
| **EMP ZONE 2** | Welded steel enclosure, Bay 3 | **80 dB, 10 kHz – 1 GHz, STANDING ALONE** | **IEEE Std 299 full survey — HOLD POINT** |

> ### The design rule, adopted with the model — the whole package in one line
>
> **EMP Zone 2 is designed to the full 80 dB standing alone. No attenuation from the concrete box
> is credited at any frequency.**
>
> The cage is then **margin, not design** — which is the only defensible way to use a shield you
> can never survey, buried under two metres of engineered cover.

### 14.4.2 What the design already does right — and none of it had been written down as EMP

1. **The 150 mm bar spacing is a deliberate EMP decision, and it was the right one.** Stricter than
   IS 456 Cl. 26.3.3 needs; recorded in the master, in the structural package, in eight bar
   schedules and on the drawings.
2. **The cast-in frames are already specified as EMP bonds** — every blast door frame *"cast in and
   welded to the cage"*, and the rule is applied even to the **non-blast-rated** headhouse door,
   because the shield must be electrically continuous.
3. **Every construction joint already carries a welded Cu / galvanised EMP strap.** A construction
   joint is where a cage loses continuity, and the project already knew it.
4. **There are no movement joints inside the protective envelope, and the reason is recorded:** *a
   movement joint is a guaranteed blast, gas and EMP discontinuity.*

### 14.4.3 EMP Zone 2 — the enclosure

**Every dimension in this section is `[A]`.** The project confirms the enclosure is **required** and
contains no specification for it.

| | |
|---|---|
| Host | Bay 3, internal 3 500 × 5 000 × 3 200 |
| **External** | **2 400 × 1 600 × 2 200**, at X 5820–8220, Y 3700–5300 |
| Shielded panel | 50 mm |
| **Internal clear** | 2 300 × 1 500 × 2 100 — 3.45 m² / 7.245 m³ |
| **Shielded envelope area** | **25.28 m²** — walls 17.60, roof 3.84, floor 3.84 |
| **Total seam length** | **24.80 m** |
| Clearances | 300 mm north, south and west; 800 east; **1 000 head — 850 clear above the 150 mm HVAC duct zone** |

**A 300 mm gap is held on every free face so an IEEE Std 299 survey can physically reach every
seam.** A shielded room you cannot walk around cannot be tested, and **an untested shield is a
claim, not a shield.** The enclosure is entirely clear of the Y 2500–3400 circulation route.

> **The seam length is the risk, not the area.** Every one of those **24.8 metres** has to be
> continuously welded or continuously gasketed, and IEEE Std 299 will find the metre that is not.

**The five ways in:**

| PoE | Treatment | Performance |
|---|---|---|
| **PoE-1 ACCESS** §5.4 | RF-gasketed or knife-edge shielded door | ≥ 80 dB · **type and vendor `[N]`** |
| **PoE-2 VENTILATION** §5.5 | Honeycomb, **6 mm cell × 25 mm deep** | cutoff **29.3 GHz** · **133 dB** (**+53 dB** margin) |
| **PoE-3 POWER** §5.7.2.1 | PCI on every conductor, mounted **on** the boundary | **`[N]` — no residual quoted, deliberately** |
| **PoE-4 SIGNAL** §5.7.4.1 | **Fibre**, no metallic strength member or armour | **A dielectric is not a penetration** |
| **PoE-5 RF** §5.7.6 | — | **Nothing to apply it to — EM-F6** |

> **PoE-3 quotes no residual figure on purpose.** MIL-STD-188-125-1 specifies pulse-current
> injection performance **by pulse test**, and the project's register carries the section number
> only. **Inventing a number would be worse than `[N]`.**
>
> **PoE-4 is the bargain of this package.** Fibre with no metallic member is **not a penetration at
> all**. It is the one place this project can buy perfect performance for almost nothing, and it
> should take it.

### 14.4.4 Findings

| Ref | Finding |
|---|---|
| **EM-F1** | **The stair void is a 2 800 × 3 160 (8.85 m²) aperture that never reaches 80 dB anywhere in the band and is simply open above 47.4 MHz.** It does not open into soil — **it opens into the headhouse, which is at +0.900 with no earth cover**, and thence to grade through a stairwell that is declared expendable. **The entry route is an open electromagnetic path from grade to Bay 7**, and Blast Door 1 is the only thing across it — **its RF performance is vendor data the project does not have.** *This is not a criticism of the architecture: a shelter needs a staircase, and the void is where a staircase has to go. It is a statement that the blast boundary and the EMP boundary are not the same surface, and the project has only ever drawn one of them* |
| **EM-F2** | **The cage meets 80 dB over one decade of the five required and gives 0.00 dB at 1 GHz.** A genuine low-frequency measure; **must not be described as a MIL-STD boundary** |
| **EM-F3** | **"EMP Zone 2" had been named since Rev F with no Zone 1 and no Zone 0 ever defined, and no specification for the enclosure itself.** Four revisions, no shield |
| **EM-F4** | **BV-4 and BV-5 (DN350) are the only penetrations failing both criteria** — cutoff 502 MHz, 54.8 dB. **RULED (ruling 3, RC4): bay 8 IS inside the EMP boundary, so the honeycomb panels move from conditional to REQUIRED** — and because the generator may run in closed mode, **the panels must work with the valves open** |
| **EM-F5** | **≤ 5 Ω is not achievable with rods in Deccan basalt** (335 Ω per rod at the *low* resistivity bound) **and is not an EMP requirement in any case.** The structure is already the better electrode |
| **EM-F6** | **There is no antenna, mast, feeder or communications design anywhere in this project.** §5.7.6 is in the register with nothing to apply it to. **An ops room that cannot transmit is an ops room in name only** — and an antenna is by definition a deliberate conductor from outside to inside, the hardest EMP penetration there is |

### 14.4.5 Verification, and what must not be claimed

**EMP ZONE 2 — SURVEY IT.** Full IEEE Std 299 survey, 10 kHz – 1 GHz, on the completed enclosure
with every penetration made off and every panel closed. Acceptance **80 dB**. **This is a HOLD
POINT: no equipment is installed before it passes**, because a failed survey means opening seams.

**EMP ZONE 1 — DO NOT SURVEY IT, AND DO NOT CLAIM IT.** A buried box under 2 m of engineered cover
**cannot** be surveyed to IEEE 299 — there is no accessible exterior to put a transmitter on.
**Any statement that the box gives 80 dB is unsupportable and should not be made.**

**What *can* be checked on site, cheaply, at the only moment it can be fixed:** continuity of the
cage across every construction joint **before the pour**; continuity of every cast-in frame to the
cage **before the pour**; **earth resistance, early**; and bond resistance at every strap after
making off. **None of these prove shielding effectiveness. All of them catch the mistakes that
destroy it.**

> **Every cage figure in this project is an upper bound.** The classical `−10 log₁₀(n)` array
> correction is not applied, the crossings are **tied rather than welded** — and whether they are
> tied or welded is itself `[N]` — and no concrete absorption is credited. **A measured cage will
> be worse than the calculation.**

## 14.5 Fire and life safety

**The governing fact is Part 2.10: this is a sealed shelter and it cannot be ventilated of smoke.**

### 14.5.1 What the design already does well

1. **The largest fire load is already compartmented away from the occupants.** The generator is in
   **Bay 8**, behind **Blast Door 2** in the 400 mm wall W7, and Bay 8 is separated from the
   occupied bays by **Bay 7, the stair shaft. Two barriers and a buffer between the fuel and the
   people.**
2. **Bay 8 has its own air path that never touches the gas-tight envelope** — 2 600 m³/h through
   BV-4/BV-5. **A generator fire is therefore ventilated, and ventilated away from the occupied
   zone.** The one part of this shelter that can be cleared of smoke is the one part most likely to
   produce it.
3. **The two dead-end bays are exactly the two bays with escape shafts.** Bay 1 has ESC 1; Bay 8
   has ESC 2. **No occupant is ever in a dead end without a way up out of it.**
4. **Travel distances are short** — the longest travel to a route is about **14.6 m**, and ESC 1 is
   1.5 m away in that same bay.

### 14.5.2 Where the fire load is

| Bay | Load | Comment |
|---|---|---|
| **8** | **Generator, fuel system, exhaust** | **The largest by far.** The set, its fuel system, exhaust and acoustic treatment are **not specified and not priced** |
| 5 | CBRN filter trains | **ASZM-TEDA activated carbon. Carbon beds self-heat; a filter fire is a known hazard in protected ventilation** |
| 1 | Stores | Combustible stores load not scheduled anywhere `[N]` |
| 3 | Ops room, EMP Zone 2 enclosure | Electronics and cabling |
| 4 | Berthing, 9 berths | Bedding and personal effects |
| all | **Cabling** | Cable type, route, containment and fire-stopping **are not specified anywhere** `[N]` |

### 14.5.3 The evacuation plan

| Route | Path | Emerges at |
|---|---|---|
| **R1 PRIMARY** | Any bay → spine → **Blast Door 1** → Bay 7 stair shaft → **24R @ 170.8333, 3 flights of 8, 1 200 wide** | **Headhouse** (−)2.000, then 12R up the covered stairwell to the entry door at grade |
| **R2** | **ESC 1**, Bay 1, 1 400 dia | Head **+0.150** — a **6.250 m** climb |
| **R3** | **ESC 2**, Bay 8, 1 400 dia | Head **+0.700** — a **6.800 m** climb |

> **R1 is the only route that does not require climbing a shaft, and the only one usable by an
> injured or unconscious person. R2 and R3 are escape shafts, not exits — treat them as the last
> resort they are.**

**Decision rule — where the fire is decides the route:**

| Fire in | Route | Why |
|---|---|---|
| **Bay 8, generator** | **R1**, or **R2** if the spine is smoke-logged | **Blast Door 2 SHUT.** Bay 8 is separately ventilated. **R3 / ESC 2 is inside the fire compartment — do not use it** |
| **Bays 1–6, occupied zone** | **R1** if the route to Bay 7 is clear; otherwise **R2** from the west end, **R1 or R3** from the east | Bays 1–6 are **one smoke compartment** |
| **Bay 7, stair shaft** | **R2 or R3** | The primary route **is** the fire. Both blast doors shut |
| **Headhouse or covered stairwell** | **R2 or R3** | R1's surface end is blocked; both are outside the boundary and the stairwell is expendable |

**Immediate actions.** Raise the alarm **by voice** — there is no alarm system, and in a 20.8 m
shelter with 9 occupants and permanently open 900 mm partition gaps, voice carries. Attack it only
while it is small and only if the route behind you is clear. **Shut the blast door between you and
the fire — they are the only real barriers in the shelter.** Stop the generator if the fire is in
Bay 8 or of unknown origin. Evacuate by the rule above; **do not pass the fire to reach a preferred
route.** **Roll call: 9** — the occupancy is a confirmed figure, so the count is unambiguous.
**Muster point — NOT DEFINED, because no site plan exists.**

**There is no fire team. With 9 occupants, everyone is the fire team.** No fire duty, warden role
or drill frequency is defined anywhere in the project `[N]`.

### 14.5.4 The findings a fire plan here is obliged to raise

| Ref | Finding |
|---|---|
| **FS-1** | **W5 was designated "fire and gas-tight" and no door existed in it anywhere in the project.** A fire separation with an unfilled opening in it is not a fire separation — and the compartment it protects contains the **activated-carbon filter trains**, while escape route R1 has to cross it. **RULED (ruling 9, RC4): design it now. FS-1 CLOSES** |
| **FS-2** | **Bays 1 to 6 are ONE smoke compartment, 20.8 m long.** The four W8 partitions are 110 mm, non-structural, with **permanent 900 mm gaps and no doors scheduled.** Smoke starting in Bay 1 reaches Bay 6 unobstructed. *Not a criticism of the partitions — they were never fire barriers* — but it means **the only real fire barriers in the shelter are Blast Doors 1 and 2, and W5 once it has its door** |
| **FS-3** | **ESC 2 is in the same bay as the generator.** Both facts are confirmed and neither is wrong alone. **The coupling had never been stated: the most likely fire in the shelter denies one of its three escape routes** — which is exactly why the decision rule routes a Bay 8 fire away from ESC 2 |
| **FS-4** | **A fire during the closed mode cannot be ventilated at all**, and clearing smoke means opening a blast valve, **which breaks the protection the closed mode exists to provide.** **No rule exists anywhere in the project for which hazard takes precedence.** That belongs to the client, **and it should be made before it is needed rather than during** |
| **FS-5** | **Every active fire measure followed the missing electrical design.** The electrical blocker is now gone — a detection and alarm panel and maintained emergency lighting exist on the essential board, on the battery. **What remains is fire engineering** — head layout, zoning, detector type, any suppression — **and none of it is invented here** |
| **FS-6 / FS-V7** | **The six-metre unequipped climb out of each escape shaft.** Raised **by the drawings, not by the text**: the written plan had all three numbers and never put them in the same picture; the escape-plan drawing's vertical profile put them side by side and the gap was immediate. **RULED — a ladder is now designed (Part 10.6), and it still has no fall-arrest, no rest platform, and no answer on the injured person** |

**What the plan cannot say, and does not invent:** extinguisher type, number and siting; fire
ratings of doors and finishes; cable type, containment and fire-stopping; generator fuel type and
quantity; muster point and fire service access; drill frequency and warden duties. **Codes beyond
NBC 2016 Part 4 and IS 13416 are not in the register, and their numbers are not invented.**

> **And one trade that must be a conscious decision, not an improvisation.** The 1 000 L tank in
> Bay 1 is the **96-hour potable supply** — 27.8 L/person/day. **It is not firefighting water.**
> Using it against a fire trades the shelter's endurance for its fire response, **and that is the
> commander's call.**

# PART 15 — SITE LAYOUT, FINISHES AND CONCEALMENT

## 15.1 External works — the reserve, and why everything is in it

An **external works reserve of 18.0 × 10.5 m at X 33 000 – 51 000, Y 6 500 – 17 500** —
**10.0 m clear of the main excavation's east face**, **downgradient**, and entirely inside the
owner's 50 m envelope (worst corner **42.5 m of 50 m**).

| Tag | What | Centre (X, Y) | Serves |
|---|---|---|---|
| **ST-01** | Septic tank 1.5 × 0.75 | (36 750, 16 000) | 10 users, 450 L/day |
| **SK-01** | **Foul soak pit** 2.2 dia | **(44 000, 16 000)** | Septic tank effluent — the furthest downgradient of everything |
| **SK-02** | Storm soakaway 2.2 dia | (35 000, 8 500) | Clean sump + entry channel. **Moved 300 mm north by RC4** to give 2.10 m to the sentry post against IS 2470's 2.0 m |
| **SK-03** | Stairwell soakaway — **footprint reserved** | (41 400, 8 500) | Stairwell sump. **Size recorded nowhere** `[N]` |
| **SK-04** | Headhouse soakaway — **footprint reserved** | (47 800, 8 500) | Headhouse gully. **Size recorded nowhere, and its pipe cannot be routed** |
| **IC-01 · IC-02** | Inspection chambers 600 × 450 | (7 500, 9 800) · (40 200, 16 000) | Change of direction; de-sludging |

**Everything in one reserve, on the downgradient side, for four stated reasons:**

1. **Nothing recharges the ground upslope or alongside a box that is flotation-critical at FoS 0.33
   in the mat-only stage** — and whose side backfill at 95 % MDD is **more permeable than the
   basalt around it**, so effluent released near it would run *into* the backfill and down the
   outside of the tanking.
2. **One percolation-test location, one keep-clear zone, one reserved fallback.**
3. **One trench** — three of the runs share a common services trench, and **where rockhead is
   0.9–1.5 m the cost *is* the trench.**
4. **Concealment** — four cover slabs and a 2 m septic vent, grouped 11–22 m away, **mark the
   drainage field, not the shelter.**

> **The layout is anchored to confirmed geometry only.** Nothing is dimensioned from the sentry
> post, so it survives the sentry position being resolved differently; and **every offset is
> relative**, so if the perimeter fence turns out to be closer than the reserve's east edge, **the
> whole reserve translates and not one offset changes.** That is why the fence distance —
> `SG2-V2` — could be closed: **the layout is immune to the answer.**

**The IS 2470 offsets — complete for the first time:**

```
foul soak pit to the SEPTIC TANK    >= 5 m      5.40 m    DEMONSTRATED
soak pit to any BUILDING            >= 2 m     10.97 m    DEMONSTRATED, 5.5x over
foul soak pit to any WELL           >= 15 m       --      OWNER RULING (RC7)
```

> **The caveat, and it matters.** The well clearance is an **owner ruling, not a survey result.**
> It is recorded as `[C] owner ruling` and **not** as `[C] surveyed`, and the distinction is
> deliberate: **if a well is later found within 15 m, the foul soak pit moves.** Foul effluent near
> a water source is the one clearance nobody should carry on an assumption, which is why it stayed
> open until the owner could answer it from knowledge of the plot.

**28 of 28 clearance checks pass**, and the five pipe runs are fixed except one:

| Run | Length | Status |
|---|---|---|
| Septic tank → foul soak pit, DN100 at 1:100 | **5.40 m** | FIXED |
| Service entry plate → storm soakaway, DN50 rising main | **27.00 m** | FIXED — its vertical leg waits on the entry plate's level, which is `[N]` |
| Entry channel → storm soakaway, DN100 at 1:100 | **32.35 m** | FIXED — **routed west first, because north would cross the stairwell excavation** |
| Stairwell sump → stairwell soakaway, DN50 rising main | **29.60 m** | FIXED |
| Headhouse gully → headhouse soakaway, DN100 at 1:80 | **`[U]`** | **CANNOT BE ROUTED** |

### 15.1.1 `SG2-F1` — the soak pit's problem is DEPTH, not arithmetic

The soak pit was widened rather than deepened when it was found 2.3 % short (Part 14.2). **The
reason that choice was forced, rather than merely preferred, is the finding:**

> **21–43 % of the pit's required side area is above the design water table, and its only
> permeable horizon is 0.2–0.5 m thick.** A pit driven deeper goes further below (−)2.000, **where
> it cannot soak at all.** So the fallback **dispersion field is reserved** rather than the pit
> being re-sized again — and **the mandatory percolation test governs the final size and form.**

### 15.1.2 Two more findings that the layout could not resolve

| Ref | Finding |
|---|---|
| **`SG2-F3`** | **The septic tank is sized for a building that no pipe connects to it.** It is sized for *"sentry-post shift crews + shelter maintenance"*, the drainage package **excludes the sentry post from scope**, and **there is no pipe from the sentry post to the tank anywhere in the project.** The layout positions the tank and leaves the connection to the drainage engineer; it does not prejudge it |
| **`SG2-F4` → closed** | **The fresh-air intake had no plan position.** The equipment schedule gave the generator shaft an X range and gave the intake only *"west of the box"* — **no X, no Y, no coordinate. The fresh-air intake of a CBRN shelter is not a minor fitting.** **RULED (ruling 14, RC4): SH-1 centred (−2 400, 3 100), RECOVERED from the project's own recorded 12.3 m to the entry, to within 28 mm.** SH-2's head level is **+1.500**, the same gooseneck head |

> **And the intake / exhaust separation was settled by geometry, not by meteorology.** SH-1 and
> SH-2 are **25.30 m apart at opposite ends of a 22 m box** — robust whatever the wind does, which
> is exactly why the site package justified its orientation on access, fall, noise and end-to-end
> separation and **explicitly not on prevailing wind.**
>
> **But the plume question stays open, and it must.** A CBRN shelter with no wind direction data
> **cannot state which way a release drifts**, and 25.30 m of separation says nothing about that.
> Closing both halves of that question on one argument is exactly the move the open-item register
> exists to prevent.

## 15.2 Finishes

> **No finish specification exists anywhere in this project.** The master, the Rev F drawings, the
> services sheet and the structural package fix concrete grade, cover, waterproofing, crack control
> and bar spacing — **and nothing about what a surface is finished with.**
>
> So the finishes package does **not** report finishes as project facts. **Every code is a
> performance requirement derived from something the project does confirm**, and the product that
> satisfies it is left open. **A schedule that filled them in would be inventing a specification.**

| Requirement | Derived from |
|---|---|
| Decontaminable, coved, joint-free finishes in bays 1–6 | The gas-tight CBRN envelope |
| Wet-area treatment in the lavatory, the plant bay and the airlock | The room uses |
| Non-slip decontaminable finish in the stair shaft | Those faces are designated a **wet / dirty zone** — it is why their cover is 30 and not 40 |
| Non-slip external finish in the covered stairwell | Outside the boundary, **declared expendable** |
| Hose-down finish and 1:80 fall in the headhouse | Confirmed on the Rev F ground plan |
| EMP Zone 2 enclosure in the ops room | **The finish is subordinate to the shielding** |
| **Cast-in fixings only** | 40 mm cover, 150 mm bar spacing as an EMP requirement, the membrane, the cage |
| **No suspended ceilings or cavities anywhere in the envelope** | Duct inspectability, drain inspectability, decontamination |
| Floor build-up limited | The 1.0 kPa mat allowance, and drainage finding DR-F4 |
| **Cast-in stair nosing, no tread build-up** | **The stair going is FROZEN.** An applied nosing or a thick tread finish would change the effective going |

**Thirteen spaces are scheduled**, each with its floor, skirting, wall, ceiling, door,
waterproofing, wet-area status and falls. Two entries carry findings rather than finishes:

- **The decon airlock is the dirtiest surface in the shelter** — wet area, falls 1:80 to
  **segregated** gullies, 50 mm upstand at W5 and at Blast Door 1.
- **The generator bay falls to a gully that has no destination defined** — drainage finding DR-F5.

**`FN-U1` / `D-05`** — the finishes schedule recorded the missing W5 door as a data gap; **the fire
plan made it a defect**, and it has since been ruled: *design it now.*

## 15.3 Concealment

> **The shelter is concealed. The installation is not.**

**What the design already achieves:**

| Measure | Value |
|---|---|
| Topsoil / turf over the whole buried roof | **300 mm**, 30.867 m³, the top layer of the cover — its function is named as *concealment, erosion, sheds rain* |
| Turf sourced from the site itself | **92.82 m³ stripped and stockpiled** for re-use — **the re-laid surface is the surface that was there before** |
| Finished grade | **crowned, falling 1:50 away** — a natural-looking shed, not a flat platform |
| Berm against the headhouse and covered stairwell | 1.5:1 to +0.900 |
| Surplus excavation | **1 113.937 m³ re-used on site** as engineered fill and crushed rubble |
| **Roof penetrations for drainage** | **NONE.** No roof outlet, no downpipe, no rainwater pipe anywhere on the buried roof |
| Burster slab | laid to a **1:50 crossfall** so infiltration disperses at the berm toe **without a pipe** |

> **Two of these matter more than the rest.** Re-using the site's own stripped turf means the
> restored surface is **not a different green from its surroundings**, which is what usually gives a
> buried structure away. And **because the cover is drained without a single pipe, there is no
> manhole, no gully and no outfall anywhere on the roof to break the surface.**

**The signature inventory — every element above ground:**

| Element | Above grade | Note |
|---|---|---|
| **Sentry post** | **+7.000** parapet | **The tallest thing on the site by 4.5 m** |
| Covered entry stairwell | **+2.450** head | Outside the boundary, **declared expendable** |
| Fresh-air shaft SH-1 | **+1.500** gooseneck | 600 × 600, west of the box |
| Generator air shaft SH-2 | **+1.500** gooseneck | 600 × 600, east of the box — **level ruled by RC4; the signature is now complete for the first time** |
| **Headhouse** | **+0.900** roof top | 4 800 × 5 800, **no earth cover. The largest above-ground mass** |
| Escape shaft ESC 2 | **+0.700** head | 1 400 dia clear, 1 900 OD collar |
| Escape shaft ESC 1 | **+0.150** head | as ESC 2 |
| Soak pit / soakaway covers | at grade | Positions fixed by the site layout |
| Sentry post spiral stair | external | 1 000 R, 250 dia pole |

> **The buried box under 2 m of graded, turfed cover is genuinely hard to see. But a 7 m sentry
> post 10 m away, a 4.8 × 5.8 m headhouse with no earth cover, a 2.45 m stairwell head and two
> 1.5 m goosenecks are not concealed by anything, and nothing in the project asks them to be.**
>
> **This is a statement of fact about the design as recorded, not a criticism of it** — the sentry
> post is a manned observation position and is *meant* to be seen, and the headhouse is the
> entrance. **But the distinction had never been written down, and a concealment policy that did
> not say it would be misleading.**

**Policy.** The turf is a **continuous surface, not a patch** — re-lay the stockpiled site turf; do
not import a different species or a different soil colour. **No new spoil heap** — all 1 113.937 m³
of surplus is re-used on site, because **a spoil mound is a permanent signature that outlasts the
works.** The berm should **read as ground, not as an engineered line.**

> **And what the policy cannot say.** The concealment bill item — *"camouflage and concealment
> measures beyond the 300 topsoil / turf layer"* — is tagged `[N]`, quantity *to be verified from
> final measurement*, note **"no concealment"**. **No net, screen, paint scheme, thermal treatment
> or detection criterion exists anywhere in this project, and none is invented.** Nor can a
> concealment **layout** be drawn: there is no site plan, so nothing's position on the ground is
> known except relative to the box.

# PART 16 — WORKS MANAGEMENT

## 16.1 What exists

| Deliverable | Contents |
|---|---|
| Works management handout | **44 pages, 25 sections**, covering the whole project |
| Master programme, MSPDI XML | Microsoft Project's own published schema, plus CSV for any other tool |
| Programme PDF | **7 A3 sheets** — basis and milestone register, summary Gantt, 5 sheets of detailed Gantt with the critical path |
| WBS | **279 activities, 18 milestones, 404 logic links**, 3-level, 14 level-1 packages |
| Bill of quantities | **90 items in 10 sections**, whole project |
| Resource plan | **33 resources, 426 assignments** |
| Procurement plan | 16 packages, all tied to programme activities; long-lead register |
| QA/QC plan | **42 ITP items, 16 hold points that are activities in the programme** |
| Safety and risk register | 15 hazard classes, **25 risks** |
| Codes and references | **78 references** |
| Quantity derivation | ~800 lines of working with the source of every input |
| Consistency audit | **65 executed checks, 65 pass** |

## 16.2 The programme

| | |
|---|---|
| Start | **Monday 2 November 2026** — carried from the owner's own R0 schedule `[A]` |
| Finish | **Saturday 20 November 2027** |
| Duration | **326 working days** (384 calendar days) against R0's 224 |
| Calendar | **Six-day week, Mon–Sat**, Sunday non-working, plus five date-certain national holidays. **Festival holidays are NOT fabricated** — a 10-day contingency activity absorbs them |
| **Critical path** | **75 activities at total float 0**: possession → site investigation and **monsoon groundwater monitoring** → excavation support design → rock excavation → formation → tanking → mat → walls → pressure slab (**14-day cure + 14-day props, IS 456 Table 11**) → roof membrane → the six-layer cover including the burster slab → external works → snagging → contingency → handover |

> **The site investigation is on the critical path, and so is the groundwater monitoring.** That is
> the correct answer to Part 4.4: the design's most important unknown is programmed as work, not as
> a hope. **And the monitoring window, 12 November to 4 December, is not in the monsoon** — which
> is what `SG-V3` says and what makes it worth saying.

## 16.3 Cost

Three versions are published side by side, deliberately: the project's own estimate, the project
owner's own estimate, and the owner's estimate with the rulings applied.

| Cost head | Basis | Owner's package | With rulings applied |
|---|---|---|---|
| Total basic cost | subtotal of packages | ₹ 24 336 022 | ₹ 24 220 254 |
| Contingencies | 3.0 % | 730 081 | 726 608 |
| Water and electricity provisions | 1.0 % | 243 360 | 242 203 |
| **Specialist CBRN / EMP and engineering consultant** | 6.0 % | 1 460 161 | 1 453 215 |
| Site supervision and quality assurance | 2.0 % | 486 720 | 484 405 |
| Statutory clearances and liaison | 1.0 % | 243 360 | 242 203 |
| Contractor's overhead and profit | 10.0 % | 2 433 602 | 2 422 025 |
| **FINAL PROJECT COST** | | **₹ 30 033 306** | **₹ 29 790 913** |

> **The total is a LOWER BOUND, and it says so.** Several items in the bill read *"to be verified
> from final measurement"* with no rate, because the project does not hold what they need:
> **the blast doors, the blast valves, the filter trains, the generator and its fuel system, the
> EMP Zone 2 enclosure, the escape-shaft hatches and ladders, and all concealment beyond the turf.**
> **Every one of those is a specialist or vendor item, and none of them is priced by guessing.**

## 16.4 The rules the works management package holds itself to

- **The project owner's own bill, estimate and schedule GOVERN.** The project's versions are
  published alongside, never in place of them.
- **Nothing is retyped.** The owner's documents are reproduced, not transcribed.
- **No quantity, rate, date or float is changed by any discipline package.** Every services and
  rulings revision in this project states that it changed none, and each states it separately so
  the claim can be checked.
- **One design change was instructed and is recorded as one** — the sentry post masonry (Part
  5.9.1). One bill item was added by a ruling — the 8 m³ strip-and-replace under the stairwell raft
  (Part 4.5), **at a rate tagged `[A]` rather than invented.**

## 16.5 Risks that are design outputs, not contractor problems

| Risk | Where it is answered |
|---|---|
| **Flotation during construction** | Part 9.3.5 — four mandatory mitigations, one of them **formally departed from in writing** |
| **Rock excavation quantity exceeds the estimate** | Part 4.7 — **+118 m³, about 2 extra days**, against a register entry that said "roughly one" |
| **The excavation face across a monsoon** | Part 4.6 — batter the soil cap; **the slope-stability assessment is still outstanding** |
| **Site investigation findings** | Part 4.2.2 — **5.3 m of unlogged ground under the whole structure** |
| **Specialist lead times** | The long-lead register: blast doors, blast valves, filter trains, the EMP enclosure |

# PART 17 — WHAT THIS DESIGN DOES NOT DEMONSTRATE

> **This part must be reproduced in every future revision. It is the boundary of the design's
> validity.**

## 17.1 What IS demonstrated

**Demonstrated to IS 456**, with IS 13920 for the sentry post frame: ultimate flexural capacity;
diagonal-tension shear; minimum and maximum steel; bar spacing; cover; development and anchorage;
deflection; crack-width provisions; biaxial column interaction; punching and one-way shear in the
footing; and ductile detailing to IS 13920.

## 17.2 What is NOT demonstrated, and NOT claimed

1. **Support rotation and ductility ratio for the blast case.** θ ≤ 2° corresponds to δ ≤ 87 mm =
   span/57 and requires a **non-linear SDOF check** (IS 4991 Fig. 6 / Biggs) or explicit non-linear
   FE with strain-rate-dependent materials. **Phase 3.**
2. **Shock-wave propagation down the entry shaft** and the resulting door loading — CFD or shock
   tube. **Specialist.**
3. **Transient soil–structure interaction** — participating mass, arching, interface pressure
   ratios.
4. **Transient soil–structure THERMAL behaviour** — the sibling of (3), and the missing piece of
   `RC4-V1`.
5. **Blast door, valve and hatch performance** — **vendor-tested, not a civil deliverable.**
6. **Global flotation cannot be shown by an elastic-mat model.** The springs take tension, so in the
   model the mat never lifts. It is a hand check on real dimensions (Part 9.3.5).
7. **The berm's actual pressure-transmission factor** — removed from the critical path by designing
   the headhouse walls to the upper bound.
8. **Any analysis result whatsoever.** STAAD.Pro has not been run in this project. No moment,
   displacement, shear or reaction exists for the underground box or for the three mesh models, and
   **the mesh convergence conclusion is outstanding.**
9. **The negative phase and rebound as a separate load case** — allowed for physically at the
   hatches, not analysed.
10. **EMP Zone 1 shielding effectiveness.** It is a calculation and it will stay a calculation; a
    buried box cannot be surveyed to IEEE 299.

> **A conventional static STAAD.Pro analysis gives the correct DEMAND. It is not, and must never be
> presented as, proof of blast resistance.**
>
> **IS 4991:1968 Cl. 1.1 expressly EXCLUDES nuclear explosions from its scope.** It is used here for
> its loading rules and dynamic material strengths only, as a documented conservative
> extrapolation. **Every structural capacity is computed to IS 456.**

# PART 18 — ASSUMPTIONS, OPEN ITEMS AND RULINGS

## 18.1 How to read this part

Three registers, and the distinction between them is the point:

| Register | What it holds |
|---|---|
| **18.2 Assumptions** | Values the design uses that have **no test and no client confirmation**. Seven are closed; **the seven that remain are exactly the site investigation** |
| **18.3 Open items** | Questions that need **information the project does not contain**. **Eighteen are open.** They are **not inconsistencies** — each is a single position the project holds, with nothing contradicting it |
| **18.4 Rulings** | **Thirty-two items ruled by the project owner across RC4 to RC9**, item by item, plus the two earlier RC2 rulings and the conflicts closed on the evidence |

## 18.2 Assumptions — seven closed, seven open

**CLOSED (7) — every one by judgement, and every one the conservative or immaterial choice:**

| # | Assumption | Ruling |
|---|---|---|
| **A6** | K<sub>a</sub> = 1.0 saturated used; dry berm ≈ 0.5 **not relied on** | **ACCEPTED as the conservative choice** — the full 383 kPa is taken rather than crediting unverifiable berm attenuation |
| **A9** | Sentry infill not separated → R = 3.0 | **KEPT.** R = 5.0 gives A<sub>h</sub> 0.060 against 0.100, so **73.18 kN is ≈ 1.67 × a separated SMRF's demand.** Separating would need an SMRF this project does not claim, and would undo the tie detail |
| **A10** | Wind k1 = 1.08, 100-year life | **ACCEPTED** — a 100-year life on a load path seismic beats **2.4 : 1** |
| **A11** | b<sub>eff</sub> = 2.5 m for the HW3 line load | **ACCEPTED ON THE MARGIN** — 41 % on the conservative one-way bound leaves more than half the capacity spare |
| **A12** | Trapezoid factor 0.7946 used for both BM and FEM | **ACCEPTED ON THE MARGIN.** The factor itself is exact; the simplification is worth ≈ 2 %, inside B2's 89 % |
| **A13** | Sentry frame has no member releases | **CLOSED ON THE EVIDENCE, and it needed no ruling.** The register asked for the `.std`; **the file had been in the workspace all along and nobody re-read it.** `MEMBER RELEASE` appears nowhere in it |
| **A14** | Poisson's ratio 0.20 | **ACCEPTED** as the standard value for concrete |

**STILL OPEN (7) — and every one needs a physical test on this plot:**

```
A1   rockhead 1.5-2.0 m                     boreholes
A2   DESIGN GWT (-)2.000                    piezometer, read through a FULL monsoon
A3   SBC 3240 kPa                           plate load / core testing
A4   ks 100 000 - 500 000 kN/m3             plate load test -- BOTH bounds
A5   K0 0.50, gamma 20/21                   site investigation
A7   soak-pit absorption 20 L/m2/day        PERCOLATION TEST, IS 2470 Pt 2 Cl. 4,
                                            MANDATORY
A8   structural seepage 0.5 L/m2/day        packer permeability tests
```

> **That is the sentence worth carrying into a viva.** The assumption register is no longer a mixed
> bag of judgement calls and missing data. **Everything a competent engineer could decide has been
> decided. What is left is precisely the site investigation the project has never had** — and the
> reason is Part 4.2.2: the only investigation available is **off-site** and **reached about 1.5 m
> against a formation at (−)6.800.**
>
> **A4 deserves one extra line.** The upper-bound model **now exists** and is verified by diff
> against the reference model. **It is still `[ASSUMED]` at both bounds, and neither has been run.**

## 18.3 Open items — eighteen

### 18.3.1 The four a reviewer should look at first

| Ref | Item |
|---|---|
| **`SG-V2`** | **The investigation reached about 1.5 m against a formation at (−)6.800.** 5.3 m of unlogged ground under the whole structure — **including the red-bole case that sizes the mat** |
| **`EM-V6`** | **Two 1 400 mm holes in the protective boundary whose bonding is still undesigned.** The structural half is now designed (Part 10.5); the EMP half is not |
| **`SG2-V4`** | **A CBRN shelter that cannot state which way a release drifts.** The intake/exhaust half is closed on geometry; **the plume half stays open, and must** |
| **`RC4-V1`** | **A sealed box with a 4 kW heat surplus and an unmodelled rejection path** (Part 2.11) |

### 18.3.2 Open, narrowed by a ruling (9)

| Ref | Where it stands now |
|---|---|
| **`U8`** | Parapet **confirmed at 300 × 150** and exact; **one dimension — the roof projection — is recorded nowhere.** 4.162 kN/m continues to be used as given; no member force changes |
| **`WM-V9`** | Excavation face **ruled** — batter the soil cap, vertical in rock. **The slope-stability assessment is still outstanding** |
| **`FS-V7`** | **Ladder designed** (Part 10.6). **No fall-arrest, no rest platform, and the injured-person question** |
| **`EM-V6`** | **Structural half designed, EMP half open** |
| **`EL-V2`** | **Day tank sized** at 250 L nominal in Bay 8, fill and vent up the existing shaft. **Fuel type, rate and vendor open**; the shared-bore fit is unchecked |
| **`EL-V7`** | **Duty computed** — 0.18 m³/h of CO₂, a 75 m³/h loop, 8 × margin on the fan allowance. **Absorber and soda-lime charge open** |
| **`SG-V6`** | Stairwell raft in black cotton soil — **specified and measured** (8 m³). **Rate `[A]`** |
| **`SG2-V4`** | **Intake/exhaust closed** at 25.30 m separation; **PLUME half open** |
| **`RC4-V1`** | **Narrowed** from *"no rejection path exists"* to *"the rejection path is the ground through the structure, and it has not been modelled"* |

### 18.3.3 Open, annotated but NOT narrowed (2) — and this pair is instructive

| Ref | The problem |
|---|---|
| **`EM-V2`** | Every EMP Zone 2 dimension is `[A]`, pending an equipment schedule |
| **`EL-V3`** | There is no equipment schedule for EMP Zone 2 — only a **1.50 kW allowance** |

> **These two are each holding the other's placeholder, and it is worth naming.** The enclosure is
> **sized to fit a bay**; the 1.50 kW load is **chosen to give the enclosure a basis**. **Neither is
> evidence.** They corroborate each other and neither corroborates anything. **What breaks the loop
> is an operational equipment list — a client input, not a calculation.**

### 18.3.4 Open, untouched (6)

| Ref | Item |
|---|---|
| **`WM-V6`** | Sentry seismic weight after the masonry change. **The direction is certain and favourable** — brick is lighter, so W falls, V<sub>b</sub> falls, and every member is over-designed. **Nothing is unsafe and nothing is inconsistent.** What is missing is a STAAD re-run to put a number on the margin — **confirmation, not risk** |
| **`EM-V4`** | **No communications design of any kind exists.** No antenna, mast or feeder, so MIL-STD §5.7.6 has nothing to apply to |
| **`EM-V5`** | **No pipe material is specified for any run in the project.** Metallic → bond it 360° to the entry plate and its exterior becomes shield. Plastic → the bore is an aperture *and* the water column is a conductor, needing a metallic spool piece nobody has specified |
| **`SG-V1`** | **The geotechnical data is off-site.** No investigation has ever been made on the project plot |
| **`SG-V2`** | **Depth of investigation** — the governing item |
| **`SG-V7`** | **The concealment turf may be an expansive clay.** If the site's own topsoil is the CH horizon, it cracks in the dry season and pumps fines into the granular filter, **which is the one thing the filter exists to stop.** The load is unaffected |

### 18.3.5 Open, new (1)

| Ref | Item |
|---|---|
| **`DR-A2-V1`** | **The clean sump has no cover, and Bay 5 cannot be crossed without one** (Part 13.7). Needs the cover itself: type, depth, **imposed load duty**, frame and rebate, fixing, and how it is lifted to withdraw the pumps |

### 18.3.6 A declared scope boundary — not a gap

| Ref | What does not exist | Where it was declared |
|---|---|---|
| **`EL-V5`** | **No circuit, cable, luminaire or socket schedules.** The electrical package stops at **board level** | The package's own opening paragraph. **It closes when a detailed electrical design is commissioned, not by any work in this project** |

> **This row was moved out of the open-item register on purpose**, so that a **declared decision is
> never counted as an outstanding problem** — which is what was happening.

## 18.4 Rulings and conflicts

### 18.4.1 The conflicts closed on the evidence

| # | Conflict | Resolution |
|---|---|---|
| **C1** | Drawings Rev F, report Rev D — the report describes a dog-leg open ramp; Rev F is a covered entry stairwell | **DXF governs.** The precedent for everything after it |
| **C2** | The report designs the headhouse roof for 3.0 m span + 1.0 m cover; Rev F is 4.0 m + no cover | **Recomputed.** T20 @ 150 survives at 90 %; **shear links new and mandatory** |
| **C3** | The report calls the stair-shaft walls 600 thk; the Rev F plan shows 200 | **DXF governs** → triggers **Finding F1** → **Modification M1** |
| **C4** | Blast door leaf: plan 1200, section 900 | **1200 × 2100 adopted** — agrees with the report's own 1 564 kN leaf force |
| **C5** | Plan dimension "7300 covered stairwell external" against 6 800 in the plotted geometry | **6 800 adopted** |
| **C6** | The report checks the mat in flexure only | **One-way shear checked → the T12 @ 250 × 250 link grid** |
| **C7 / C9** | The report uses W = 505 kN for the sentry post; the hand check gives 592.7 kN; STAAD gives 731.80 kN | **The STAAD value governs**, and Part 7.8.2 explains the gap to the kilonewton |
| **C8** | The report adopts a sentry post height of 6 850 mm; the elevation shows roof +6.700, parapet +7.000 | **Drawn levels adopted**; h = 6.250 m from the base at +0.450 |
| **C10** | The report designs the headhouse walls for 113 kPa drag only | **Raised to the full 383 kPa envelope** (Part 7.5) |
| **C11–C15** | Five defects in the entry stairwell and underground `.std` files — wrong concrete grade, missing roof imposed load, missing waterproofing load, wrong fill unit weight and berm level, and **four mat corner joints with no vertical restraint** | **All five resolved**, each by bringing the file to the master rather than the master to the file |
| **C16** | The roof/platform junction — one clause said the stairwell roof becomes the 500 headhouse roof over the platform | **RULED AT 250.** It was the only place in the project saying 500 (Part 5.8) |
| **C17** | Cover build-up: 40.65 stated, 39.15 summed | **RULED. 40.65 held, and the table made self-consistent** (Part 7.3) |
| **C18** | Sump pit base: the register says 400, a sheet note says 300 | **RULED AT 400.** (−)8.000 − (−)7.600 = 0.400 is arithmetic |
| **C19** | Soak pit 21.99 m² against its own stated 22.50 required | **RULED. Widened to 2.200 m dia → 24.19 m², +7.5 %** |
| **C20** | A superseded Rev E catchment on an issued sheet | **RULED. Rev F governs; the figure is retained as a declared conservatism and both are labelled** |
| **C21** | Filter duty: the master said 2 × 250 m³/h, the sheet said 300 in nine places | **RULED AT 300 m³/h, and the master was corrected.** 250 fails the sheet's own FEMA criterion, so it was **not the cautious option but a demonstrably inadequate one** |
| **ERR-1** | A yield-line coefficient computed with the simply-supported constant instead of the fixed-four-edges one — 324.4 against 162.2 | **Corrected, and recorded as an error rather than quietly fixed.** No reinforcement changed, because the one-way value was the one adopted (Part 10.3) |

### 18.4.2 The owner's rulings, revision by revision

| Revision | Rulings | Net effect on the open register |
|---|---|---|
| **RC2** (11 Sep) | 2 — the three-zone EMP model **adopted**; the generator **may** run in closed mode | **Neither changed a number** |
| **RC4** (11 Sep) | 16, item by item — **13 actioned, 3 deliberately left open** | 33 → **25** |
| **RC5** (12 Sep) | 4 — heat rejection, the hatches, the day tank, and one left open — plus `A13` closed on the evidence | 25, **three narrowed, none closed** |
| **RC6** (12 Sep) | The excavation face, and **six assumptions closed** | K.2 **14 → 7** |
| **RC7** (12 Sep) | 4 — the scrubber duty, the mains, four source defects, the well | 25 → **19** |
| **RC8** (12 Sep) | 3 — the fence, the EM/EL circularity named, one reclassified | 19 → **17** |
| **RC9** (12 Sep) | **None. It corrected a count** | 17, verifiable by reading |
| **DR-A2** (12 Sep) | **None. It drew two things and found one** | 17 → **18** |

> **Three of those deserve to be read as a set, because they are about the project's own
> discipline rather than about the design.**
>
> **`RC9` corrected a count this project got wrong.** Revisions RC4 to RC8 ruled faithfully and
> recorded every ruling — **but thirteen rows of the register itself were never annotated**, so a
> reader counting the table got 34 while the narratives claimed 21, then 15, then 13. **All three
> counts were wrong**, and the first was wrong arithmetically on its own terms. The fix was **not
> to restate the number but to make the register countable**: every row is now classified, and the
> totals can be verified by reading rather than by trusting a sentence.
>
> **`RC10` found the same failure mode one level down.** RC4 to RC9 ruled on thirty-two items and
> **did not touch the discipline packages**, so six artefacts still say something the master has
> settled — the EMP penetration register still calls the honeycomb panels conditional, the HVAC
> schedule still locates the intake as *"west of the box"*, the escape-route schedule still records
> two climbs with no means of climbing them. **Nothing was silently edited**: all six are build
> artefacts regenerated from their packages' scripts, and applying the register is a
> package-by-package job with a regeneration check that **has not been done.**
>
> **The lesson is one this project already wrote down: *a change that stops at "reinforcement" and
> never reaches "drawings" is not finished.* RC4 to RC9 stopped at the master.** The failure mode
> appeared twice in two days — once inside the master, once between the master and its packages —
> **and both times the fix was to make the thing countable rather than to trust a narrative.**

# PART 19 — VERIFICATION PERFORMED FOR THIS REPORT

## 19.1 What was checked, and how

This report reproduces several hundred numbers from the project record. **Every one of them was
independently recomputed from its own inputs before it was printed here**, by a script that is
part of this package:

```
Project Report/Scripts/report_verify.py
    -> Project Report/Calculations/REPORT_VERIFICATION_OUTPUT.txt

    python3 "Project Report/Scripts/report_verify.py"
```

Each check takes the **inputs** a value is derived from, does the arithmetic **independently** —
the formulas are written out again in the script, not copied — and compares the result with the
value the project prints.

> **What a PASS means, stated precisely.** *The printed number follows from the printed inputs.*
> **It is not a design check and it is not an analysis.** It does not re-derive the engineering
> judgement behind a value, it does not run STAAD, and it cannot tell you whether an assumption is
> true. What it does catch is the class of defect this project has already been bitten by twice: a
> number that no longer agrees with its own derivation.

## 19.2 The result

```
CHECKS EXECUTED                 498
PASS                            494
KNOWN / RECORDED difference       4
UNEXPLAINED FAIL                  0
```

**Coverage, by section of the script:**

| § | Subject | What it recomputes |
|---|---|---|
| 1 | Blast loading and structural dynamics | DLF and its limit case, the design pressure, the reflection coefficient, 50 psi in kPa, E<sub>c</sub>, the participating mass, the flexural stiffness, **the roof natural frequency and period, and t<sub>d</sub>/T at both ends of the duration band** |
| 2 | The engineered cover and the roof total | **All six layer loads, their sum, the declared allowance**, the total thickness, the crossfall drop, COMB 103, the static ULS case and the blast : static ratio |
| 3 | Soil, water and flotation | γ′, the lateral gradient and the water share, the pressures at soffit and floor, the uplift intensity and total at both box lengths, **all four flotation factors of safety**, the COMB 102 check at both lengths, the net pressure at formation, every bearing utilisation, **and the whole rock-excavation quantity table** |
| 4–8 | Element design, box and headhouse | Every d, M<sub>u,lim</sub>, A<sub>st</sub> provided, M<sub>u</sub>, utilisation, x<sub>u</sub>/d, shear force, τ<sub>v</sub>, p<sub>t</sub>, V<sub>us</sub>, A<sub>sv</sub>/s<sub>v</sub> and link spacing for W1–W4, W6/W7, the mat, the roof, the openings, the cantilever pad, the headhouse roof and walls, and HW3 — **plus the shaft fill time that produced Finding F1** |
| 9 | Stairs | Both pitch angles and their cosines, every load term, effective spans, moments, areas, capacities, utilisations, **the total-rise closure, and both opening-corner angles** |
| 10 | Escape shaft head hatches | The leaf force, the hole area, the plate moment and shear, **the flat-plate thickness and its 505 kg mass**, both climb heights and both rung pitches |
| 11 | Seismic and wind | Both A<sub>h</sub> values, both base shears, **the R = 3.0 conservatism factor**, the model-versus-hand weight gap **and its two explanations to the kilonewton**, all three period estimates, the full wind chain, and the portal distribution |
| 12 | Sentry post members | Effective spans and the two-way ratio, slab moments and capacities, both beams' governing combinations, capacities, capacity-design shears **and earthquake shares**, **the 5-T16 bar-fit check that forced 3-T20**, the column's slenderness, steel, P<sub>uz</sub>, biaxial sum and confinement, the footing in service and at ULS, punching, anchorage, **and the whole lintel design including the 60° arching bound** |
| 13 | Development, laps and cover | L<sub>d</sub>/φ for both grades in tension and compression, every tabulated L<sub>d</sub>, and the lap policy margin |
| 14 | CBRN ventilation | **All eleven figures the HVAC package reproduces**, plus the air-change rates, the scrubber matrix at six duty points and the recirculation fan power |
| 15 | Thermal balance | The load that is dissipated **inside** the envelope, the occupant gain, the 96-hour energy, **all three bounds — adiabatic, concrete and film — the 13.2 K rise, the cooling duty, and the ventilation rejection arithmetic** |
| 16 | EMP | Cage shielding effectiveness at five frequencies, the mesh cutoff, **the highest frequency meeting 80 dB**, the wavelength coincidence at 1 GHz, four TE11 cutoffs, six waveguide attenuations, the stair void, the honeycomb, **both bond-strap inductances and reactances**, the earth rod, the structure electrode, and the Zone 2 enclosure's area, seam length and volume |
| 17 | Drainage and external works | The wetted envelope and the seepage it produces, the sump storage, **all three trap-seal depths**, the soak pit before and after widening, the septic tank checks, and every catchment |
| 18 | Electrical | The connected load and its kVA, generator utilisation and spare, the essential load, **both battery cases and the factor of twelve between them**, and the fuel quantity |
| 19 | Quantities and cost | Every bar mass from its unit mass and length, both totals, the concrete take-off, the steel density, **and both cost summaries head by head** |
| 20 | Register arithmetic | **The open-item counts, the assumption counts and the drawing counts add up** |

## 19.3 The four differences found — reported, never corrected

> **Master rule M.11 and the project operating guide both forbid editing a recorded value away.**
> Every difference below is an **observation offered to the master**, not a change. **None of them
> moves a dimension, load, thickness, bar, quantity, rate, date or float.**

| # | Where | Computed | Printed | Assessment |
|---|---|---|---|---|
| **1** | **Underground box wall shear stress** — 525 × 10³ / (600 × 0.8 × 21600) | **0.0506 N/mm²** | 0.063 N/mm² | **Not previously recorded.** Both values are negligible **by two orders of magnitude**; the conclusion *"IS 13920 Cl. 10.4 boundary elements NOT triggered"* is unaffected and **no adopted value depends on it** |
| **2** | **Sentry footing F1, ULS eccentricity** — M<sub>u</sub>/P<sub>u</sub> = 43.9 / 276.8 | **0.159 m** | 0.128 m | **Not previously recorded.** The footing is governed by **IS 456 Cl. 26.5.2.1 minimum steel** (720 against 136 mm²/m required) and its depth by **starter anchorage**, so **no adopted bar, spacing or dimension moves** |
| **3** | **Sentry footing F1, q<sub>u,max</sub>** — the printed expression 276.8/2.25 × (1 + 6 × 0.128/1.5) | **186.0 kPa** | 190.0 kPa | Same item as 2. One-way shear at 0.012 and punching at 0.065 against τ<sub>c</sub> = 1.369 are unaffected on either figure |
| **4** | **The project owner's cost summary** — the seven heads against the printed final | **₹ 2 99 33 306** | ₹ 3 00 33 306 | **ALREADY RECORDED — conflict `R-14`**, exactly ₹ 1 00 000 apart, *"reported, not corrected"*. **The verification pass reproduced a known finding**, which is the outcome you want from a check like this. The revised estimate **reconciles to the rupee** and has no such difference |

> **Three observations about that result are worth making.**
>
> **The two footing items are one item.** An eccentricity and the bearing pressure computed from it
> are the same arithmetic seen twice, and both land on an element whose steel is set by a code
> minimum and whose depth is set by anchorage. **That is precisely why it survived four revisions
> without being caught: nothing downstream of it is sensitive to it.**
>
> **The wall shear item is the same shape.** A figure quoted to show that something is negligible
> is a figure nobody re-checks, because the conclusion is right either way.
>
> **And the fourth was already in the register.** Reproducing a recorded finding independently is
> the best evidence that the check is working — and reproducing it **from the owner's own published
> numbers** is what makes it safe to leave alone.

## 19.4 What this report could not verify, and did not attempt

| Not verified | Why |
|---|---|
| **Any analysis result** | STAAD.Pro is not available. **No result exists to check** |
| **The mesh convergence conclusion** | Same reason. The three models are built and validated; none has been run |
| **Every `[ASSUMED]` value** | An assumption is not an arithmetic error. **k<sub>s</sub>, the design water table, the safe bearing capacity, K₀, the soak-pit absorption rate, the seepage rate and the rockhead band are all tests, not sums** |
| **Vendor performance** | Blast doors, blast valves, filter trains, the shielded door, the PCI, the honeycomb, the escape hatches |
| **Anything tagged `[N]`** | There is nothing to check. **The projection dimension, the ambient design temperature, the opening heights, the pipe materials, the entry plate's level and size, the sump cover, the fan's five vendor loss components** |
| **The drawings themselves** | Checked by the drawing QA tool, not by this report — Part 13.3 |

## 19.5 Consistency checks made against the project record

Beyond the arithmetic, the following were checked by reading:

1. **Every reinforcement arrangement in Part 12 matches the calculation in Parts 9 to 11.** No bar
   size, spacing or count appears in the register that does not appear in a calculation.
2. **Every evidence tag is carried unchanged.** No `[ASSUMED]`, `[UNRESOLVED]` or `[NOT AVAILABLE]`
   item is converted, downgraded or deleted anywhere in this report.
3. **The open-item and assumption counts in Part 18 agree with their own tables** — 9 + 2 + 6 + 1 =
   18 open, 18 + 16 + 1 = 35 rows, 7 + 7 = 14 assumptions.
4. **The drawing counts in Part 13 sum to 80**, and the sheet sizes 75 A1 + 4 A4 + 1 A0 sum to 80.
5. **The frozen staircase geometry is reproduced exactly** — 24 risers, 170.8333 mm, 280 mm tread,
   3 flights × 8, total rise 4 100 mm — **and nothing in this report changes any of it.**
6. **Every code clause cited here appears in the project's own register.** No clause was added, and
   codes held by title only are named as such.

# APPENDIX A — NOTATION

| Symbol | Meaning |
|---|---|
| **p<sub>so</sub>** | Peak incident static overpressure of the blast wave |
| **p<sub>r</sub>** | Reflected overpressure on a surface normal to the wave |
| **q** | Dynamic (kinetic) pressure of the air flow behind the front |
| **t<sub>d</sub>** | Positive phase duration |
| **T**, **f<sub>1</sub>** | Fundamental natural period and frequency |
| **μ** | Ductility ratio — maximum displacement / yield displacement |
| **DLF** | Dynamic load factor, μ/(μ − 0.5) |
| **K<sub>a</sub>** | Soil transmission factor for a buried element |
| **K₀** | Coefficient of earth pressure at rest, 1 − sin φ |
| **γ, γ<sub>sat</sub>, γ′, γ<sub>w</sub>** | Bulk, saturated, submerged and water unit weights |
| **k<sub>s</sub>** | Modulus of subgrade reaction (kN/m³) |
| **f<sub>ck</sub>, f<sub>y</sub>** | Characteristic concrete and steel strengths |
| **f<sub>ck,dyn</sub>, f<sub>y,dyn</sub>** | The same, increased 25 % for the blast case only |
| **E<sub>c</sub>** | Modulus of elasticity of concrete, 5000√f<sub>ck</sub> |
| **d**, **d′** | Effective depth; cover to the centroid of compression steel |
| **A<sub>st</sub>, A<sub>sv</sub>/s<sub>v</sub>** | Tension steel area; shear link area per unit length |
| **M<sub>p</sub>, M<sub>u</sub>, M<sub>u,lim</sub>** | Plastic mechanism moment; design capacity; limiting singly-reinforced capacity |
| **x<sub>u</sub>, x<sub>u,max</sub>** | Neutral axis depth; its limiting value, 0.46 d for Fe500 |
| **τ<sub>v</sub>, τ<sub>c</sub>, τ<sub>c,max</sub>** | Nominal shear stress; permissible concrete shear stress; its maximum |
| **p<sub>t</sub>** | Tension steel percentage |
| **V<sub>us</sub>** | Shear to be carried by links |
| **L<sub>d</sub>, τ<sub>bd</sub>** | Development length; design bond stress |
| **A<sub>h</sub>, Z, I, R, S<sub>a</sub>/g** | Seismic design coefficient and its four inputs |
| **V<sub>b</sub>, W** | Seismic base shear; seismic weight |
| **P<sub>uz</sub>, α<sub>n</sub>** | Column pure-axial capacity; biaxial interaction exponent |
| **A<sub>sh</sub>, l<sub>o</sub>** | Special confining hoop area; confining length |
| **SE** | Shielding effectiveness, dB |
| **WBC** | Waveguide below cutoff |
| **T16 @ 150 EF EW** | 16 mm bars at 150 mm centres, **E**ach **F**ace, **E**ach **W**ay |
| **4L** | Four-legged links |

**Evidence classes** — `[C]` confirmed · `[R]` reconstructed · `[A]` assumed · `[U]` unresolved ·
`[N]` not available.

# APPENDIX B — WHERE EACH CODE CLAUSE IS USED

| Clause | Subject | Used in |
|---|---|---|
| IS 456 Cl. 6.2.3.1 | E<sub>c</sub> = 5000√f<sub>ck</sub> | Part 6.1 |
| IS 456 Cl. 13.4 | Construction joints | Part 6.4 |
| IS 456 Cl. 22.2(a) | Effective span | Parts 10.1, 11.2, 11.7 |
| IS 456 Cl. 23.2.1 + Fig. 4 | Deflection, modification factor | Parts 10.1, 10.2, 11.2 |
| IS 456 Cl. 24.4, 24.5 + Fig. 7 | Two-way slabs; load to beams | Parts 7.7, 10.4, 11.2 |
| IS 456 Cl. 25.1.2 | Short column | Part 11.5 |
| IS 456 Cl. 25.4 | Minimum eccentricity | Part 11.5 |
| IS 456 Cl. 26.2.1, 26.2.1.1, 26.2.5.1 | Development length, laps | Part 6.3 |
| IS 456 Cl. 26.3.3 | Bar spacing | Parts 6.2, 11.2 — **the project's 150 mm cap is stricter** |
| IS 456 Cl. 26.4.2, .1, .2 + Table 16 | Cover | Part 6.2 |
| IS 456 Cl. 26.5.1.1, .2, .5, .6 | Beam steel and links | Parts 9.1–9.4, 10.3, 11.3, 11.7 |
| IS 456 Cl. 26.5.2.1, .2 | Slab steel, maximum bar diameter | Parts 9.4, 10.1–10.3, 11.2, 11.6 |
| IS 456 Cl. 26.5.3.1, .2 | Column steel and ties | Part 11.5 |
| IS 456 Cl. 31.6, .1, .3.1 | Punching shear | Parts 9.3 (declared N/A), 11.6 |
| IS 456 Cl. 32.2, 32.5(a)(b)(c) | Walls — minimum steel, two curtains | Parts 9.1, 10.2, 10.4 |
| IS 456 Cl. 33.1(b), 33.2 | Stairs — effective span, step load | Parts 10.1, 10.2 |
| IS 456 Cl. 34.2.4.1 | Footing one-way shear | Part 11.6 |
| IS 456 Cl. 36.4.2 | Partial safety factors for materials | Part 6.1 |
| IS 456 Cl. 38.1, (c), (f) | Limit state, stress block, x<sub>u,max</sub> | Parts 9–11 throughout |
| IS 456 Cl. 39.1, 39.3, 39.6 | Columns, biaxial bending | Part 11.5 |
| IS 456 Cl. 40.1, 40.2.1.1, 40.2.3, 40.4(a) | Shear | Parts 9.1–9.4, 10.1–10.4 |
| IS 456 Tables 3, 5 | Exposure, mix requirements | Part 6.1 |
| IS 456 Tables 19, 20 | τ<sub>c</sub>, τ<sub>c,max</sub> | Parts 9–11 throughout |
| IS 456 Tables 26, 27 | Two-way slab coefficients | Parts 5.3, 10.3, 11.2 |
| IS 456 Table 28 | Effective length of columns | Part 11.5 |
| IS 456 Annex D, D-1.1 to D-1.8 | Two-way slab detailing, corner torsion | Part 11.2 |
| IS 456 Annex G-1.1(b), (c) | M<sub>u</sub>, M<sub>u,lim</sub> | Parts 9–11 throughout |
| IS 875 (Pt 1) Table 1 | Unit weights | Parts 6.1, 7.2 |
| IS 875 (Pt 2) | Imposed loads | Parts 7.2, 7.7, 10.1, 10.2 |
| IS 875 (Pt 3) Cl. 7.2 etc. | Wind | Part 7.8.3 |
| IS 1893 (Pt 1) Cl. 6.3.2.2 | Directional combination | Part 11.5 |
| IS 1893 (Pt 1) Cl. 6.4.2 | A<sub>h</sub> | Part 7.8 |
| IS 1893 (Pt 1) Cl. 7.6.2, (c) | Fundamental period | Part 7.8.2 |
| IS 1893 (Pt 1) Cl. 7.6.3 | Base shear and its distribution | Parts 7.8, 11.1 |
| IS 1893 (Pt 1) Cl. 7.11.1 | Storey drift | Part 11.5 |
| IS 13920 Cl. 6.1 | Beam section limits | Part 11.3 |
| IS 13920 Cl. 6.2.1(b), .2, .3, .4 | Beam steel limits | Part 11.3 |
| IS 13920 Cl. 6.3.3, **6.3.4**, 6.3.5.1, .2 | Capacity-design shear; **τ<sub>c</sub> = 0** | Parts 11.3, 11.4 |
| IS 13920 Cl. 7.2.1 | Strong column – weak beam | Part 11.5 |
| IS 13920 Cl. 7.4, 8.1, 8.2 | Column hoops, special confining reinforcement | Part 11.5 |
| IS 13920 Cl. 10.4 | Boundary elements — **checked, not triggered** | Part 7.8.1 |
| IS 3370 (Pts 1, 2) | Crack width 0.2 mm; 0.35 % surface-zone steel | Parts 6.1, 9.1 |
| IS 1904 Table 1 | Presumptive bearing capacity | Parts 4.3, 11.6 |
| IS 12070 Cl. 6, Table 2 | Settlement on rock; broken bedrock | Parts 4.3, 9.3 |
| IS 1498, IS 2720 Pts IV, VIII, X, XIII, XL, 28 | Soil classification and testing | Parts 4.2, 4.5 |
| IS 2470 (Pt 1) Cl. 6.2–6.9, Table 1 | Septic tank | Part 14.2 |
| IS 2470 (Pt 2) Cl. 4, 5 | **Percolation test — mandatory**; dispersion | Parts 14.2, 15.1, 18.2 |
| **IS 4991 Cl. 1.1** | **EXCLUDES NUCLEAR — quoted in every deliverable** | Parts 3.1, 17.2 |
| IS 4991 Cl. 6.2.1 | Reflected pressure, recessing of blast valves | Parts 2.7.3, 14.1.4 |
| IS 4991 Cl. 7.2 + Table 3 | Buried roof and walls, K<sub>a</sub> | Parts 2.1.4, 7.1, 7.5 |
| IS 4991 Cl. 7.4 | Drag on bermed faces | Part 7.5 (superseded basis) |
| IS 4991 Cl. 10.3.1 | Dynamic f<sub>ck</sub> and f<sub>y</sub> | Parts 2.2.5, 7.1 |
| **IS 4991 Cl. 10.3.1.1** | **No dynamic increase on shear; +25 % bond, refused** | Parts 2.2.5, 6.3, 9.3 |
| IS 4991 Cl. 10.3.3 | DLF = μ/(μ − 0.5) | Parts 2.2.3, 7.1 |
| IS 4991 Cl. 11.1, 11.2 | No wind/EQ with blast; no live load on the roof | Parts 7.4, 7.9 |
| IS 4991 Fig. 6 | SDOF support rotation — **Phase 3** | Parts 2.2.3, 17.2 |
| SP 34 Cl. 5.5 | Opening-corner detailing | Part 10.2.1 |
| NBC 2016 Part 4 | Stair geometry, 1 100 guarding, means of escape | Parts 9.5.2, 10.1, 14.5 |
| UFC 3-340-02 §4-27, §4-30 | Opening trimmers; **direct shear** | Part 9.4.4 |
| MIL-STD-188-125-1 §5.4–§5.7.6 | EMP — access, WBC, PCI, fibre, RF | Parts 2.8, 14.4 |
| IEEE Std 299 | Shielding effectiveness survey — **HOLD POINT** | Part 14.4.5 |
| IEEE 142 / IS 3043 | Earthing, ≤ 5 Ω | Parts 2.8.5, 14.3 |
| FEMA 453 | 0.25 cfm/ft² ventilation rate | Part 14.1 |
| EN 1822 | HEPA H14 at MPPS | Part 2.7.2 |
| IS 1077 | Sentry post brick masonry | Parts 5.9.1, 11.7 |
| IS 732, IS 694, IS 1554 (Pt 1) | Electrical installation and cables | Part 14.3 |
| IS 13416 | Construction-phase fire safety | Part 14.5 |
| BS 8666 | Bar shape codes | Part 12.6 |

# APPENDIX C — REPRODUCING THIS REPORT AND THE PROJECT

## C.1 This report

```
Project Report/
   Documentation/MASTER_PROJECT_REPORT.md      the report SOURCE -- edit this
   Scripts/report_render.py                    Markdown -> PDF typesetter
   Scripts/report_verify.py                    independent recomputation
   Calculations/REPORT_VERIFICATION_OUTPUT.txt its output
   MASTER_PROJECT_REPORT.pdf                   the deliverable

   python3 "Project Report/Scripts/report_verify.py"     run the checks
   python3 "Project Report/Scripts/report_render.py"     rebuild the PDF
```

**Never edit the PDF.** Edit the Markdown and re-run the renderer. The renderer adds no content of
its own beyond the cover, the running head and foot, and the automatically paginated contents
list.

## C.2 The project

| To rebuild | Do this |
|---|---|
| A discipline drawing package | `cd "<Package>/Scripts" && python3 <prefix>_build_all.py`. **Edit the generator, never the DXF** |
| The drawing index and QA report | Re-run `qa_report_data.py` then `make_index.py`. **A new package must first register its `DXF/` prefix in `DISCIPLINE` and its name in `ORDER`** |
| The works management package | `wm_build_all.py` regenerates everything from `wm_data.py` + `wm_content.py` |
| The S-series structural sheets | **Not possible.** The toolchain is not in the workspace (Part 13.6) and **must not be fabricated** |
| Any STAAD result | **Not possible.** STAAD.Pro is not available in this environment |

**The ten Rev F architectural DXFs are source, not build artefacts, and may be edited directly.**
Everything else generated in this project is a build artefact: **edit the generator and re-run.**

## C.3 The rule that makes regeneration safe

Every discipline package in this project has verified that it **regenerates byte-identically**.
That property is worth not breaking casually — it is what makes it possible to apply a change to a
generator and be certain that nothing else moved.

# APPENDIX D — REVISION HISTORY IN BRIEF

> The full record, with the reasoning for every change, is in the master's Part H. This is an index
> to it.

| Rev | Date | What it did |
|---|---|---|
| **A–C** | — | Architectural layout development. **Rev C lengthened the box** to give ESC 2 its 750 mm clearance |
| — | — | **Cover reduced 4.0 m → 2.0 m.** Saved 2 m of rock excavation, 2 m of shaft, one stair flight and 2 m of headroom |
| **D** | — | Design report issued — basis of design, loads, materials, geotechnics. **Current for loads and materials; superseded for the entrance and the headhouse roof** |
| **E–F** | — | **The approach was replaced**: a dog-leg open ramp became a covered entry stairwell entered at grade. The open cut had no gravity outfall, a 2 m pit collects dense CBRN agents, and lidding at grade gave zero headroom |
| **F** | — | **The ten architectural drawings issued. Current for all geometry** |
| **M1** | 3 Sep 2026 | **W6/W7 200 → 400; box 21 600 → 22 000.** Approved and implemented. Finding F1 |
| **MS1** | 3 Sep 2026 | Three mesh-density models built and validated |
| **BIM-P1 / P1B** | 3 Sep 2026 | Revit scripts authored — **not executed; Revit is not available** |
| **SC1** | 4 Sep 2026 | **30 reinforcement drawings**, 8 bar bending schedules, 70.46 t of steel |
| **DR1 · HV1 · FN1** | 5 Sep 2026 | Drainage, HVAC and the schedule of finishes |
| **WM1** | 7 Sep 2026 | Works management; **and SP-B1, the one instructed design change** |
| **QA1** | 9 Sep 2026 | 65 DXF inspected and corrected in place |
| **BS1 · SP-B2** | 10 Sep 2026 | Burster slab laid to falls; sentry post lintels and wall ties |
| **WM2 · WM3** | 10 Sep 2026 | The owner's own bill, estimate and schedule **adopted**, then revised alongside |
| **RC1** | 10 Sep 2026 | **Every inconsistency that could be ruled on the evidence, ruled** |
| **CAM1/2 · FS1/2** | 10 Sep 2026 | Concealment policy and fire plan — **neither existed before** — then relocated and drawn |
| **EM1** | 10 Sep 2026 | **The project's first EMP design** |
| **EL1** | 11 Sep 2026 | **The project's first electrical design**, deliberately basic |
| **RC2** | 11 Sep 2026 | Two owner rulings. **Neither changed a number** |
| **SG1 · SG2** | 11 Sep 2026 | **The project's first site and geotechnical section**, and its first site layout |
| **QA2 · MS2 · RC3** | 11 Sep 2026 | Drawing re-scan at 80 sheets; **the `.std` input-file corrections**; project-wide reconciliation |
| **DR-A1** | 11 Sep 2026 | Drainage items drawn on the Rev F architectural sheets |
| **RC4** | 11 Sep 2026 | **Sixteen owner rulings, item by item** |
| **RC5 · RC6 · RC7 · RC8** | 12 Sep 2026 | Sixteen more rulings; **K.2 falls from fourteen assumptions to seven** |
| **RC9** | 12 Sep 2026 | **A count this project got wrong, corrected — and made countable** |
| **RC10** | 12 Sep 2026 | **What the rulings left stale in the packages** — six artefacts, register raised, **not yet applied** |
| **DR-A2** | 12 Sep 2026 | The sump pit head and a key plan; **`DR-A2-V1` opened** |
| **PR1** | **13 Sep 2026** | **This report.** No design value changed; 498 checks executed; four differences reported and none corrected |

---

*Master project report, revision PR1 · 13 September 2026 · FOR REVIEW — NOT FOR CONSTRUCTION.*
*Authority: `master/MASTER_PROJECT_STATE.md`. Where this report and the master disagree, the
master governs. No design value, evidence tag, quantity, rate, date or float is changed by this
report, no `.std` file was touched, STAAD.Pro was not run, and the main staircase is unchanged —
24 risers, 170.8333 mm riser, 280 mm tread, 3 flights × 8, total rise 4 100 mm.*
