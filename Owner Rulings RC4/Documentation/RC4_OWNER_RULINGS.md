# RC4 — SIXTEEN RULINGS BY THE PROJECT OWNER

**Revision RC4 · 11 September 2026 · master Part H.28**

The project owner was taken through the open register item by item and ruled on sixteen of
them. **Thirteen are actioned here. Three were deliberately left open and stay open.**

Every ruling is `[C] owner ruling` — the same class RC2's two rulings carry. A ruling settles
what the project's position **is**; it does not manufacture evidence, and where a ruling
required a design or a calculation, that work is in
`Calculations/RC4_CALC_OUTPUT.txt` and `Calculations/RC4_SITING_OUTPUT.txt`
with its arithmetic shown.

> **RC4 ran no analysis. STAAD.Pro was not executed. The main staircase was not touched.**

---

## 1  The sixteen, in one table

| # | Item | Ruling | Effect |
|---|---|---|---|
| 1 | **SG2-V5** dewatering stops before backfill | **Accept the residual flotation risk in writing** | No date moves. §2.1 |
| 2 | **FS-V7** escape shafts uncllimbable | **Ladder only; fall-arrest deferred** | Ladder designed. §2.2 |
| 3 | **EM-V3** is Bay 8 inside the EMP boundary | **INSIDE — protect the generator** | §2.3 |
| 4 | **A4** second subgrade bound never run | **Build the k_s = 500 000 variant** | Model built. §2.4 |
| 5 | **U2** is a direct hit a requirement | **No — confirm as designed** | Nothing changes. **CLOSED** |
| 6 | **U3** design basis threat yield | **Hold 50 psi / t_d 0.13–1.33 s as the stated basis** | Nothing changes. **CLOSED** |
| 7 | **WM-V7** ballistic function | **Not required — brick stands** | Nothing changes. **CLOSED** |
| 8 | **U4 / DR-A1-V1** two sentry positions | **Adopt the EAST position** | §2.5 — three findings |
| 9 | **FS-1 / D-05** W5 has no door | **Design it now** | Designed. §2.6 |
| 10 | **EL-V6** no cooling anywhere | **Compute the heat balance** | Computed. §2.7 |
| 11 | **EM-V5** no pipe material specified | **LEAVE OPEN** | Unchanged, still open |
| 12 | **SG-V6** raft founds in expansive clay | **Specify strip-and-replace and price it** | Specified. §2.8 |
| 13 | **EM-V4** no communications design | **LEAVE OPEN** | Unchanged, still open |
| 14 | **CAM-V5 / SG2-V3** the two air shafts | **Fix both from the design's own logic** | Fixed. §2.9 |
| 15 | **U8** parapet load not re-derivable | **Confirm 300 × 150 and verify** | Verified — **half**. §2.10 |
| 16 | **SG-V7** concealment turf may be expansive | **LEAVE OPEN** | Unchanged, still open |

---

## 2  What each ruling actually produced

### 2.1  SG2-V5 — the flotation exposure is ACCEPTED, and here is exactly what is accepted

**Ruling: accept the residual risk in writing.** The programme is unchanged. `A2070`
dewatering still ends **11-05-27**; side backfill `A7010` still runs **20-07-27 → 30-07-27**;
the burster slab is still not cast until **21-08-27**. No date, float or logic link moves.

**What is being accepted, stated so that it cannot later be said it was not:**

| | |
|---|---|
| Exposure | **70 days**, 11-05-27 → 20-07-27, spanning the **whole 2027 monsoon** |
| State of the box | **Stage 3 — complete, not backfilled** (master B.3) |
| Flotation FoS at the design GWT (−)2.000 | **1.22 — marginal** |
| Flotation FoS if the excavation floods to ground level | **0.86 — THE BOX FLOATS** |
| What master B.3 mitigation 1 requires | dewatering **"until backfill and cover complete"** |

**This ruling is a departure from master B.3's own mandatory mitigation, and it is recorded as
one.** B.3 mitigation 1 is not advisory text — it is listed as *"a design output, not a
contractor's problem"*. The other three mitigations are unaffected and remain mandatory:
the mat pressure-relief plugs, the bund-and-pump fallback, and symmetric layered backfill.

> **The acceptance is only sound if dewatering in fact continues on site through the monsoon.**
> If it does, the programme is wrong and should say so. If it does not, the exposure is real.
> **RC4 does not resolve which — it records that the owner has accepted the position as
> programmed.** `[C] owner ruling`

### 2.2  FS-V7 — a ladder, and two things it does not have

**Ruling: ladder only. Fall-arrest deferred.** Full design in `RC4_CALC_OUTPUT.txt` §R.3.

```
One ladder type, both shafts.
  Rungs       20 dia MS, hot-dip galvanised, 400 clear width
  Pitch       ESC 1  6.250 m / 21 equal spaces = 297.6 mm  (20 intermediate rungs)
              ESC 2  6.800 m / 23 equal spaces = 295.7 mm  (22 intermediate rungs)
  Clearance   >= 200 behind the rung;  >= 750 clear climbing space in front
  Stringers   2 No. 50 x 10 MS flat, galvanised
  Fixing      cast-in lugs to the 250 collar and the roof-slab bore;
              expansion-anchored brackets at 1.5 m over the lower 3.200 m
  Head        top rung level with the head; grab rails 1100 above it
```

Equal pitch **within** each shaft, so there is no short step to trip on in the dark. Pitch held
in the 250–300 mm band. `IS 3696 (Part 2)` and `NBC 2016 Part 4` are named **by title only** —
no clause is quoted from either, because neither document is in this workspace and master
Part G forbids citing a clause that cannot be confirmed.

**Three things this design does not do, by ruling or by geometry:**

1. **NO FALL-ARREST.** Deferred. A 6.250 m and a 6.800 m unprotected vertical climb, in the
   dark, in an emergency, is the exact case a fall-arrest rail exists for.
2. **NO REST PLATFORM.** Both climbs exceed the height at which one is normally provided, and
   a 1400 dia bore cannot take one without blocking the escape it serves.
3. **THE INJURED-PERSON QUESTION IS UNANSWERED.** A vertical ladder cannot pass a stretcher.
   Whether a casualty is expected to leave by a shaft is a client question.

**FS-V7 does not close. It changes** — from *"the project holds no position at all"* to
*"a ladder is designed and two named things are missing from it"*.

### 2.3  EM-V3 — Bay 8 is INSIDE the EMP boundary

**Ruling: inside.** The 15 kVA generator, its control panel and every cable in Bay 8 are
within the protected volume.

**What follows, and it is not free:**

* **BV-4 and BV-5 (DN350) need honeycomb waveguide-below-cutoff panels.** EM1 established that
  both bores fail the EMP criteria as they stand; ruling Bay 8 in is what makes treating them
  mandatory rather than optional.
* **The EMP boundary is now a different surface from the gas-tight envelope.** Gas-tight is
  Bays 1–6; EMP is Bays 1–8. **The project now holds two protective boundaries that do not
  coincide, and only one of them has ever been drawn.**
* RC2 ruled that the generator **may run during the closed mode**, with BV-4/BV-5 reopening
  after the shock. Those two bores are therefore open, through the EMP boundary, during exactly
  the post-attack period the boundary exists for. **EM-V3's ruling sharpens that rather than
  removing it** — the honeycomb panels have to work with the valves open.

> The reasoning behind the ruling, recorded because it is the design intent: the premise of a
> 96-hour shelter is that power survives the event. The battery is **149 Ah for 4 hours**. A
> generator outside the EMP boundary is a generator that is not there when it is needed.

### 2.4  A4 — the upper subgrade bound now exists

`current/staad/Underground_Shelter_ks500000.std`, built from the reference model.

```
ELASTIC MAT SUBGRADE    100000  ->  500000
corner KFY, x5           6891 -> 34455    8269 -> 41345
                         7219 -> 36095    8663 -> 43315
```

**Verified by diff: the ONLY lines that differ from the reference model are the `JOB CLIENT`
line and the five support lines.** Geometry, thicknesses, materials, all eleven load cases and
all five combinations are byte-identical. Validates at **0 errors**.

**k_s stays `[ASSUMED]` at BOTH bounds.** No plate load test exists. What has changed is that
Part L's instruction *"RUN BOTH BOUNDS"* is now executable, not aspirational. **Neither has
been run — STAAD.Pro is not available here.**

### 2.5  U4 — the EAST position, and three findings it produced

**Ruling: adopt the EAST position.** Full re-run in `RC4_SITING_OUTPUT.txt`.

**First, the pin was recovered.** SG2 measures its 50 m envelope *"about the pin"* and never
says where the pin is. Solving from its own worst case — the reserve's far corner at 42.51 m —
gives **the box centre (11000, 3100)**, exactly. `[R]`

**`RC4-F1` — the master's X range is wrong.** DR-A1-V1 records A-301 as drawing the post at
**X 31700 – 36300**. A-301's own note 2 says **X 32000 – 36000**. That is **4000 wide, which is
the sentry post's actual external dimension**; 4600 matches nothing in the project. **The
drawing is the primary source and is self-consistent. Corrected to X 32000 – 36000.**

**An elevation cannot give a Y.** Y is therefore set here: **Y 600 – 5600, centred on Y 3100**,
the box longitudinal centreline. 5000 deep, which is the post's other external dimension. `[A]`

**`RC4-F2` — the clash the master predicted does not happen.** DR-A1-V1 reasoned that the
elevation's placement *"would put the sentry post inside the reserve"*. It would only do so if
the post's Y overlapped the reserve's Y 6500–17500 — and there was never a Y. With the post on
the box centreline:

```
reserve  X 33000 - 51000   Y 6500 - 17500
sentry   X 32000 - 36000   Y  600 -  5600
overlap in X, NONE in Y, clear gap 0.90 m
```

**The external works reserve does not have to move.** SG2's 28 checks stand.

**One check does fail, and it is new.** IS 2470 requires a soak pit ≥ 2.0 m from any building,
and the sentry post is a building. SG2 never ran it — its sentry post was 10 m north, nowhere
near SK-02.

| | |
|---|---|
| SK-02 as sited by SG2 | centre (35000, 8500), wall radius 1100 → Y 7400–9600 |
| Sentry north face | Y 5600 |
| Clear separation | **1.80 m against 2.00 m required — FAIL** |
| **Fix** | **move SK-02 300 mm north to (35000, 8800) → 2.10 m — PASS** |

Every check that move touches was re-run: **8 checks, all PASS**. Every check against the
sentry post — five pits and tanks — was run for the first time: **all PASS**.
**A 300 mm nudge is the whole cost of the EAST ruling in the layout.**

**`RC4-F3` — and the one that is not so easily fixed.** Master A.2 / A.4.8 say the sentry post
stands **"≥ 10 m clear of the shelter EXCAVATION"**. A-301 sets X 32000, which is exactly 10 m
clear of the **box face** at X 22000. The **excavation** face, with its 1000 mm working space,
is at X 23000.

```
SENTRY POST to the MAIN EXCAVATION face    9.00 m  vs  10.0 m [C]   *** FAIL ***
```

**A-301's own note cites the excavation rule while applying the box face.** Satisfying the rule
as written moves the post to **X 33000 – 37000**, which passes everything (excavation 10.00 m,
ST-01 10.03 m, SK-02 2.10 m, envelope 26.12 m).

> **Both readings are recorded and NEITHER is adopted over the other.** The ruling was "adopt
> the EAST position", and the EAST position is a **convention on a drawing, not a survey
> coordinate**. `U4` stays `[ASSUMED]` until a survey supplies a real one. What RC4 changes is
> that the project now holds **one** assumed position instead of two contradictory ones, and
> knows what that position costs.

**One consequence worth stating.** SG2's fifth reason for fixing +X = east was *"the sentry
post covers the approach from the north"*. With the post 10 m beyond the **far** end of the
box, it covers nothing — the approach is at the west end. **That is not a rule the project
states anywhere, so nothing fails; but the EAST position costs the sentry post its stated
function, and a reviewer will ask.**

### 2.6  FS-1 / D-05 — W5 now has a door

Full design in `RC4_CALC_OUTPUT.txt` §R.4.

```
OPENING     900 x 2100, sill at the floor (-)6.100, head (-)4.000
TRIM        interrupted vertical steel 754 x 0.900 = 679 mm2/face
            trimmer each jamb 339 mm2/face
            ADOPTED  2-T16 EACH JAMB EACH FACE = 402 mm2 (1.19 x required)
            anchored Ld = 40 phi = 640 mm beyond the opening
HEADER      60 deg arching height 0.779 m < 1.100 m of wall available
            -> THE WALL ARCHES.  Triangle only = 1.753 kN, M = 0.263 kNm
            against Mu,lim 20.4 kNm for a nominal 200 x 300 band = 1.3 %
            ADOPTED  200 x 300 band over the opening + 600 each side
                     2-T12 top + 2-T12 bottom, T8 2-leg links @ 150
```

**The door itself — performance specified, product `[V]`:**

| | |
|---|---|
| Size | 900 × 2100 clear |
| Function | **GAS-TIGHT and FIRE RATED. NOT blast rated** |
| Seal | full-perimeter compression gasket, cam-action latch on all four edges |
| Fire rating | **EI 120** `[A]` |
| **Opening direction** | **EAST, into Bay 6** — the direction of escape travel on route R1 |
| Hardware | escape-openable from the Bay 5 side without a key |

> **The rating is `[A]` and must stay `[A]`.** Nothing in this project states a required fire
> rating for W5 or for any element. There is no fire strategy with rated periods, and no head
> layout (FS-V2, open). **EI 120 is specified so the door can be procured — not derived.**

**W5 must not be represented as a blast element.** The blast boundary is Blast Doors 1 and 2 at
W6/W7. W5 carries no pressure differential, which is what makes a 200 wall adequate there.

**FS-1 closes:** route R1 now crosses an opening that exists.

### 2.7  EL-V6 — the heat balance, and what it found

Full calculation in `RC4_CALC_OUTPUT.txt` §R.2.

```
ELECTRICAL LOAD INSIDE THE GAS-TIGHT ENVELOPE      5.733 kW
  (the connected load less the stairwell pump and the generator
   auxiliaries, which are outside.  NO DIVERSITY -- an upper bound)
OCCUPANTS  9 x (70 W sensible + 45 W latent)       1.035 kW
TOTAL SENSIBLE GAIN                                6.363 kW
HEAT RELEASED OVER 96 h                            2.199 GJ

air alone            261.7 kJ/K        dT = 8404 K   -- meaningless
+ concrete the heat reaches (414.38 m2 wetted, 0.30 m effective)
                     273,755 kJ/K      dT = 8.03 K
+ air-to-surface film (h = 3 W/m2K)                 5.12 K
AIR TEMPERATURE RISE OVER 96 h                     13.2 K
   from a 6 m ground temperature of about 26 C  ->  about 39 C,
   AND STILL RISING -- nothing has reached equilibrium

COOLING DUTY TO HOLD 30 C   3.20 kW sensible + 0.405 latent = 3.60 kW
ADOPT 4 kW (1.14 TR)   [R]
```

**The dehumidifier makes the sensible problem worse, not better** — it returns the latent heat
plus its own 1.0 kW of motor work to the same air as sensible heat, and is counted as a
sensible source above.

> **`EL-V6-F1` — THE DUTY IS NOT THE PROBLEM. THE REJECTION PATH IS.**
>
> 4 kW is a small duty. But a **sealed** shelter has nowhere to put the heat. In closed mode
> there is no ventilation air to reject to, and every existing envelope penetration is a blast
> valve or a pipe already spoken for. The heat has to go to the ground — a ground loop — and
> therefore **a new penetration of the protective envelope that nobody has designed**, plus an
> EMP treatment for it, which is exactly EM-V5's case and EM-V5 has been left open.

**EL-V6 closes** as *"no cooling load had ever been computed"*. **It opens `RC4-V1` in its
place: a sealed shelter with a 4 kW heat surplus and no route out for it.**

### 2.8  SG-V6 — the raft strip-and-replace, specified and measured

Full derivation in `RC4_CALC_OUTPUT.txt` §R.5.

```
CH horizon, measured                    0.180 to 1.000 m depth   [C]
raft underside at the top landing end   (-)0.600
raft passes below the CH base at        X 11660
AFFECTED RAFT LENGTH  X 9250 -> 11660   = 2.410 m, width 2.000 m
STRIP EXTENT  1.000 m beyond every raft edge  [A]
              4.410 x 4.000 = 17.64 m2, x 0.400 m = 7.06 m3, say 8 m3
```

**Specification.** Strip the CH horizon to **1.000 m below existing ground level** over that
extent. Replace with free-draining granular fill, **free swell index ≤ 20 %** (IS 2720 Pt XL),
in 200 mm layers compacted to **≥ 95 % MDD** (IS 2720 Pt VIII), tested to IS 2720 Pt 28.
Blind with 50 mm sand before the raft blinding.

**The replacement extends 1.000 m beyond every raft edge** so the raft never bears partly on
replaced and partly on natural CH — **a differential heave line under the only primary access
is worse than uniform heave.**

**BOQ item added: 8 m³. RATE `[A]` — NOT INVENTED.**

> **And it collides with a ruling that was left open.** This work produces a stockpile of
> exactly the material **SG-V7** warns against re-laying as the cover's turf. SG-V7 was left
> open. **Recorded, not resolved.**

### 2.9  CAM-V5 / SG2-V3 — both air shafts, from the project's own arithmetic

The two gaps are complementary: SH-1 had a head level and no position; SH-2 had a position and
no head level.

**SH-1's position was RECOVERED, not chosen.** The project already records *"12.3 m from the
intake to the entry, against a ≥ 10 m rule"*. That figure could only have been computed from a
position — so the position is implied by the project's own arithmetic:

```
entry door centre (9375, 6750)
  SH-1 centred (-2100, 3100)  ->  12.04 m
  SH-1 centred (-2400, 3100)  ->  12.33 m   <-- reproduces the recorded 12.3 m to 28 mm
  SH-1 centred (-2700, 3100)  ->  12.61 m
```

**ADOPTED: SH-1 centred (−2400, 3100), 600 × 600 occupying X −2700 to −2100, Y 2800 to 3400.**
`[A]` West of the box ✔ · ≥ 10 m to the entry at 12.33 m ✔ · on the box centreline ✔ · 2100 mm
clear of the 1.000 m excavation working space ✔ · **25.30 m from SH-2**, the generator exhaust.

**ADOPTED: SH-2 head level +1.500** `[A]` — the same gooseneck head as SH-1. A consistency
argument, not a derivation: +1.500 is the only shaft head level the project contains, both
shafts are 600 × 600 blast-valved, and the **25.3 m intake-to-exhaust separation is what
protects the intake, not stack height**.

The above-ground signature now reads, complete for the first time: **+7.000** sentry post ·
**+2.450** stairwell head · **+1.500** both shaft heads · **+0.900** headhouse.

> Not a dispersion calculation. No plume analysis of the generator exhaust exists, and if one
> is ever done it may call for more height on SH-2. **C-101 can now draw SH-2 to scale instead
> of flagging it `[N]`.**

### 2.10  U8 — half re-derived, and the half that is missing

**Ruling: confirm the parapet at 300 × 150.** The 300 height was never really an assumption —
master A.4.3 records roof **+6.700** and parapet top **+7.000**, so it is `[C]` from the drawn
levels. Only the 150 thickness was `[A]`, and the ruling confirms it.

```
parapet   0.300 x 0.150 x 25            = 1.125 kN/m
stated total                            = 4.162 kN/m  [C]
residual, the roof projection           = 3.037 kN/m

projection implied, slab self only (3.750 kPa)   =  810 mm
projection implied, slab + finish (5.250 kPa)    =  578 mm
```

> **`U8-F1` — THE PARAPET CONFIRMATION IS NECESSARY BUT NOT SUFFICIENT.**
>
> The parapet accounts for 1.125 of the 4.162 and reproduces exactly. The remaining 3.037 kN/m
> is the roof projection, and **the projection dimension is recorded nowhere in this project** —
> the Rev F framing plan carries the lumped figure and no breakdown; no plan, section or
> elevation dimensions an overhang. Back-solving gives 810 mm or 578 mm depending on whether
> the projection carries a finish. **Neither is a round number, neither is drawn, and neither
> is adopted.**

**U8 moves from "cannot be re-derived at all" to "half re-derived":** the parapet term is now
`[C]` and exact; the projection term stays `[N]` pending **one dimension**. 4.162 kN/m
continues to be used as given, which is what the analysis already does. **No member force
changes.**

---

## 3  The three left open, and why that is a position

**EM-V4 — no communications design.** The ops room cannot communicate. MIL-STD-188-125-1
§5.7.6 still has nothing to apply to, and an antenna remains the hardest EMP penetration there
is as well as a concealment signature. **Unchanged.**

**EM-V5 — no pipe material, anywhere.** The drainage package names diameters, gradients,
lengths and levels for every run and a material for none. PD-05's EMP assessment cannot be
completed either way. **Unchanged — and §2.7 has now added a second boundary crossing that
will have the same problem.**

**SG-V7 — the concealment turf may be expansive clay.** **Unchanged — and §2.8 now produces a
stockpile of exactly that material.**

> Two of the three were sharpened by rulings elsewhere in RC4. That is worth seeing: leaving an
> item open is a decision with consequences, not a way of avoiding one.

---

## 4  What RC4 did NOT do

**No `[ASSUMED]`, `[UNRESOLVED]` or `[NOT AVAILABLE]` tag was converted by inference.** Where a
ruling settles a position, the position is tagged `[C] owner ruling` and the evidence behind it
is unchanged — `U4` is still `[A]`, `k_s` is still `[A]` at both bounds, `A2` and the GWT are
untouched, and the fire rating on D-05 is `[A]`.

**No analysis was run. STAAD.Pro was not executed.** The k_s upper-bound model is **built**, not
run; MESH_SENSITIVITY_STUDY §5 is still blank.

**No dimension, level, load, thickness or bar in Parts A, B, F or L changed**, except where a
ruling created something that did not exist before (the ladder, D-05 and its trim steel, the
raft replacement, SH-1's position, SH-2's head).

**One BOQ item was added** (8 m³, rate `[A]`). No existing quantity, rate, date or float moved.

**The main staircase is untouched** — 24 risers, 170.8333 mm, 280 mm tread, 3 flights × 8,
total rise 4100 mm.
