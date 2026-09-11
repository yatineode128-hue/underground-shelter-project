# UNDERGROUND CBRN-HARDENED BLAST-RESISTANT PROTECTIVE STRUCTURE, WITH SENTRY POST
## Pune, Maharashtra · Consolidated project report

**Issue 1 · 11 September 2026 · B.E. Civil Engineering capstone · designed for actual construction**

---

## How to read this document

This is the project stated once, at the state it is in, in the order you would need it to
reproduce it. It is a **statement of the design, not a history of it.** Where a number has a
reason, the reason is given; where it has a source, the source is named; where the project does
not have it, that is said in the same sentence rather than filled in.

The authority for every value here is `master/MASTER_PROJECT_STATE.md`, which also holds the
full revision record, the conflict register and the dependency map. **Where this report and the
master disagree, the master governs.** `master/QUICK_STATE.md` is a shorter orientation digest
and is not an authority.

Every value carries its evidence class, and **the classes are the point of the document:**

| Tag | Meaning | How to treat it |
|---|---|---|
| **`[C]` CONFIRMED** | Read from a project file, or computed here from confirmed inputs | Use as fact |
| **`[R]` RECONSTRUCTED** | Derived by back-calculation from partial evidence | Use, but state the derivation |
| **`[A]` ASSUMED** | Engineering assumption, no test or client confirmation | **Re-confirm before construction** |
| **`[U]` UNRESOLVED** | Conflicting values, insufficient evidence to choose | **Do not guess. Ask.** |
| **`[N]` NOT AVAILABLE** | The information does not exist in any project material | **Do not invent** |

There are **thirty-three open items** and **fourteen standing assumptions**. They are in §14 and
§15 and they are not decoration: four of them decide whether the structure floats.

---

## 1  What this is

A buried reinforced-concrete protective structure that keeps **nine occupants alive for 96
hours** against a **nuclear air-blast design basis threat**, with CBRN filtration, EMP
hardening and fallout shielding, plus a separate sentry post at the approach. `[C]`

**Three structures, and they are deliberately not equal:**

| # | Structure | Status |
|---|---|---|
| **1** | **Main underground box** — 8 bays, 22.0 × 6.2 m external, roof 2.0 m below grade | **Blast designed.** This is the protected volume |
| **2** | **Entry headhouse + covered approach stairwell** — above-ground bermed RC on the shelter roof and adjacent fill | Headhouse **blast designed**; the stairwell is **NOT**, and is **declared expendable** |
| **3** | **Sentry post** — two-storey RC framed building, **≥ 10 m clear** of the shelter excavation, on its own footings on in-situ rock | **NOT blast designed.** A recorded decision, not an omission |

### 1.1  The protective boundary — the single most important idea in the design

> **The protective boundary is Blast Doors 1 and 2 at level (−)6.100, together with walls W6
> and W7, the perimeter walls, the mat and the pressure slab.**
>
> **Everything above the blast doors — the stair shaft, the headhouse, the entry stairwell — is
> OUTSIDE it.** That is deliberate. The stair shaft is open to atmosphere through the roof void,
> and the design accepts that it fills with blast pressure rather than pretending it does not.

**Gas-tight envelope = Bays 1 to 6 only** — **67.80 m² floor, 216.96 m³** (stated as 67.8 / 217.0)
`[C]`. Bay 7 (stair shaft) and Bay 8 (generator) are **outside** it; Bay 8 is the "grey zone".

### 1.2  Access and egress

* **Primary** — grade → covered entry stairwell (12R @ 166.667/300) → platform (−)2.000 →
  inner security door → headhouse → stair void → main dog-leg stair (24R @ 170.8333/280,
  3 flights × 8) → arrival landing (−)6.100 → **Blast Door 1** into Bay 6.
* **Secondary** — **Blast Door 2**, stair shaft into Bay 8.
* **Emergency** — two **1400 mm dia** vertical escape shafts, **ESC 1** (Bay 1) and **ESC 2**
  (Bay 8), 250 mm RC collars.

---

## 2  Codes and standards

All design is to Indian Standards. The governing set:

| Code | Used for |
|---|---|
| **IS 456:2000** | All reinforced concrete |
| **IS 4991:1968** | **Blast loading rules and dynamic material strengths ONLY** |
| **IS 875 (Pts 1, 2, 3, 5)** | Dead, imposed, wind, combinations |
| **IS 1893 (Part 1):2016** | Seismic |
| **IS 13920:2016** | Ductile detailing — sentry post |
| **IS 3370 (Pts 1, 2):2021** | Crack width, liquid-retaining / water-excluding |
| **IS 1786:2008** · **IS 1904:1986** · **IS 2950** · **IS 12070** · **IS 1498** · **IS 2720** · **IS 1121** | Reinforcement, bearing, rafts, rock, soil classification and testing |
| **IS 2470 (Pts 1, 2):1985** | Septic tank, soak pit |
| **SP 16:1980** · **SP 34:1987** · **BS 8666** | Design aids, detailing, bar shape codes |
| **NBC 2016 Part 4** | Stairs, guarding, means of escape |
| **UFC 3-340-02** | Cited **as US criteria** — opening trimmers §4-27, direct shear §4-30 |
| **MIL-STD-188-125-1** · **IEEE 299** · **IEEE 142 / IS 3043** | EMP, shielding survey, earthing |
| **FEMA 453** · **EN 1822** | Shelter ventilation rate, HEPA classification |

> **IS 4991 Cl. 1.1 explicitly excludes nuclear effects.** The project uses it for **blast
> loading rules and dynamic material strengths only**, and says so in every deliverable. The
> weapons-effects data is from Glasstone & Dolan, unclassified and public. **No clause number in
> this project was invented** — where a clause could not be confirmed, it is not cited.

---

## 3  Design basis

### 3.1  Blast — the threat and what it becomes

```
Design basis threat        nuclear air-blast, p_so = 344.7 kPa (50 psi)       [C]
Positive phase td          0.13 to 1.33 s                                     [C]
Reflected pressure p_r     1366 kPa                                           [C]
Dynamic pressure q         282 kPa                                            [C]
Ductility ratio mu         5      moderate, repairable damage   IS 4991 Cl 10.3.3
DLF = mu/(mu - 0.5)        5/4.5 = 1.111
      validation:          mu = 1 -> DLF = 2.00 = the textbook step-load factor
DESIGN BLAST PRESSURE      344.7 x 1.111 = 383 kPa
                           applied to the ROOF AND THE WALLS (Ka = 1.0)
Roof natural period T      13.4 ms  ->  td/T = 10 to 100  ->  QUASI-STATIC
Dynamic material strengths, BLAST CASE ONLY, IS 4991 Cl 10.3.1:
      fck,dyn = 1.25 x 35 = 43.75 N/mm2     fy,dyn = 1.25 x 500 = 625 N/mm2
      NO dynamic increase on SHEAR -- IS 4991 Cl 10.3.1.1
```

> **The no-increase-on-shear rule is the most commonly mis-applied clause in blast design.** It
> is why several elements here carry links they would not otherwise need. Every τ<sub>c</sub> in
> this report is read at the **static** M35 value.

### 3.2  Ground and groundwater

| Parameter | Value | Class |
|---|---|---|
| Ground | Deccan basalt (trap), red-bole / vesicular seams at flow contacts | `[A]` |
| Rockhead | (−)1.500 to (−)2.000 | `[A]` — measured 0.9–1.5 m off-site |
| Presumptive SBC | **3240 kPa** (IS 1904 Table 1, hard rock) | `[A]` |
| γ bulk / γ<sub>sat</sub> | 20 / 21 kN/m³ | `[A]` |
| γ′ submerged | 11.19 kN/m³ | `[C]` derived |
| K₀ = 1 − sin φ | **0.50** (φ ≈ 30°) | `[A]` |
| **Design groundwater table** | **(−)2.000**, monsoon | **`[A]` — the single most important number in the project** |
| **Modulus of subgrade reaction k<sub>s</sub>** | **100 000 to 500 000 kN/m³** | **`[A]` — the mat must be run at BOTH bounds** |
| Soil-transmission factor K<sub>a</sub>, saturated | **1.0** (IS 4991 Cl. 7.2, Table 3) | `[C]` |
| K<sub>a</sub>, dry compacted berm fill | ≈ 0.5 | `[A]` — **deliberately not relied on** |

> **The hazard is not the basalt, it is the flow contacts.** A single red-bole seam under the mat
> produces the differential-support case that **sizes the mat**. Over-excavate any red-bole or
> vesicular seam at founding level and replace with M15 lean concrete.

> **The provenance of the design groundwater table, stated plainly.** The available sub-soil
> investigation (SEMT/67/15, for three other buildings at CME Pune — 11 trial pits, 3 locations,
> no boreholes, no in-situ testing) records *"water table was not encountered in any trial pit."*
> **The pits reached about 1.5 m. This structure founds at (−)6.800.** *Not encountered* here
> means **not reached** — so no water was found, and **2 m was chosen.** The investigation stops
> **5.3 m above the founding horizon** and is **not on this plot**. A confirmatory investigation
> on this site, and a standpipe piezometer read through a **full monsoon**, are mandatory.

> **The surface soil is BLACK COTTON, CH, free swell index 60–65 %** `[C]` — the top band of the
> IS 1498 scale. **Nothing structural founds in it:** the mat is at (−)6.700 and footing F1 at
> (−)2.000, both in basalt. Two elements are exposed anyway and **neither has a strip-and-replace
> specification**: the entry stairwell's stepped raft, and the 300 mm turf concealment layer.

> **The structure is lighter than the ground it replaces** — net pressure at formation ≈ **−105
> kPa**. That is *why* settlement is negligible, and it is the same fact that makes **flotation,
> not bearing, the governing foundation problem.**

### 3.3  Materials

| Item | Box / stairs / headhouse | Sentry post |
|---|---|---|
| Concrete | **M35** (IS 456 Table 3, very severe exposure) | **M30** |
| w/c ratio · cement content | ≤ 0.45 · ≥ 340 kg/m³ | — |
| Admixture | Integral crystalline waterproofing `[R]` | — |
| Blinding · burster slab | M15 100 thk · M30 200 thk | — |
| Reinforcement | **Fe500D** to IS 1786:2008 | Fe500 |
| E<sub>c</sub> = 5000√f<sub>ck</sub> | **29 580 N/mm²** | **27 386 N/mm²** |
| Poisson's ratio · unit weight · γ<sub>m</sub> | 0.20 `[A]` · 25 kN/m³ · 1.5 / 1.15 | same |

**Cover — IS 456 Cl. 26.4.2 / Table 16** `[C]`

| Face | Cover |
|---|---|
| Cast against blinding / trimmed rock | **75** |
| Formed earth face | **50** |
| Internal faces | **40** |
| Stair shaft faces | 30 |
| Sentry beams and slabs · columns · footings | **30** · **40** · **50** |
| **Maximum bar spacing, both curtains** | **150 — an EMP requirement**, stricter than IS 456 Cl. 26.3.3 |

> The 5 mm cover reduction IS 456 Table 16 permits for M35 and above is **deliberately not taken.**

**Development and lap lengths — IS 456 Cl. 26.2.1** `[C]`

```
Ld = phi x sigma_s / (4 tau_bd),  sigma_s = 0.87 fy = 435 N/mm2
tau_bd x 1.6 (deformed, tension):  M35 -> 2.72    M30 -> 2.40
            Ld tension             M35 -> 40 phi  M30 -> 46 phi
            Ld compression         M35 -> 32 phi  M30 -> 37 phi
```

| Bar | T8 | T10 | T12 | T16 | T20 | T25 |
|---|---|---|---|---|---|---|
| L<sub>d</sub> M35 | 320 | 400 | 480 | 640 | 800 | 1000 |
| Lap M35 | 400 | 500 | 600 | 800 | 1000 | 1250 |

**Lap policy:** all laps **staggered so ≤ 50 % are spliced at any section**, and lap specified at
**50 φ** — 25 % above the Cl. 26.2.5.1 requirement. **The +25 % bond bonus IS 4991 Cl. 10.3.1.1
permits for blast is NOT taken**; all detailing uses the static 40 φ.

### 3.4  Loads

| Load | Value | Applied to | Source |
|---|---|---|---|
| Self weight RC | 25 kN/m³ | all | IS 875 Pt 1 Table 1 |
| Roof self, 0.900 × 25 | 22.50 kPa | roof | |
| Mat self, 0.600 × 25 | 15.00 kPa | mat | |
| **Engineered cover, 2000 layered** | **40.65 kPa** | roof | `[C]` — §3.5 |
| SIDL services / finishes | 2.0 roof / 1.0 mat kPa | | `[R]` |
| Live load, internal floor | **5.0 kPa** — plant/storage, not 2.0 residential | floor | IS 875 Pt 2 |
| **Earth + water lateral gradient** | **K₀γ′ + γ<sub>w</sub> = 0.50 × 11.19 + 9.81 = 15.41 kPa/m** | walls | `[C]` derived |
| — at roof soffit (−)2.900 | 33.9 kPa | | |
| — at floor (−)6.100 | **83.2 kPa** | | |
| **Hydrostatic uplift on mat** | 4.700 × 9.81 = **46.11 kPa**; **6289 kN** over 136.4 m² | mat | `[C]` |
| Construction surcharge | 20 kPa vertical / 10 kPa lateral | | `[A]` |
| Staircase, smeared on the two shaft walls | 2.947 kPa | W6 / W7 | `[C]` |

> **Of the 15.41 kPa/m lateral gradient, 9.81 is water and only 5.60 is soil.** Water is nearly
> two-thirds of the lateral load on the walls. **That is why the groundwater level is the single
> assumption the site investigation most has to settle.**

### 3.5  The engineered cover — 2000 mm, 40.65 kPa `[C]`

| From the top | Thickness | γ | kPa | Function |
|---|---|---|---|---|
| Topsoil / turf | 300 | 18 | 5.40 | Concealment, erosion, sheds rain |
| Granular filter | 150 | 19 | 2.85 | Stops fines clogging |
| **RC burster slab, M30, T12 @ 150 B/W** | 200 | 25 | 5.00 | **Breaks up a penetrating item** |
| Crushed basalt rubble 25–75 mm | 500 | 17 | 8.50 | Scatters burster energy |
| Compacted engineered fill @ 95 % MDD | 750 | 20 | 15.00 | **Radiation mass** |
| Protection screed over the membrane | 100 | 24 | 2.40 | Protects the waterproofing |
| Sum of the six layers | **2000** | | **39.15** | |
| **Declared allowance, held** | — | | **+1.50** | Stated, not hidden |
| **TOTAL — DESIGN VALUE** | **2000** | | **40.65** | |

**The burster slab and everything above it is laid to a 1:50 crossfall**, crowned on the box
longitudinal centreline (Y = 3100) and falling each way to the box edges — **parallel to the
finished grade**, dropping 62 mm over the 3100 half-width. The granular filter sits directly on
the burster slab and the drainage design depends on infiltrating water being *intercepted by the
filter and dispersed at the berm toe*; **on a flat slab it cannot be — it ponds and finds the
construction joints.** The fall is taken up entirely in the compacted engineered fill, 750
nominal at the crown thinning to 688 at the edge, so **every other layer keeps its nominal
thickness and the cover load does not increase anywhere.** **No pipe is introduced into the
cover** — nothing may break the roof.

> **Why 2.0 m, and not more.** Not blast — a buried roof takes full p<sub>so</sub> regardless
> (IS 4991 Cl. 7.2). Not fallout — 1.0 m already gives a protection factor of ≈ 2200 against a
> requirement of ~1000. **The second metre is bought entirely for prompt neutron and gamma
> attenuation**, which needs mass and needs it above the slab. Coming down from 4.0 m saved 2 m
> of rock excavation, 2 m of shaft, one stair flight and 2 m of headroom.

### 3.6  Total roof load — the governing case

| Component | kPa |
|---|---|
| Blast, 344.7 × 1.111 | 383.00 |
| Engineered cover | 40.65 |
| SIDL | 2.00 |
| Self weight | 22.50 |
| **TOTAL w** | **448.15** |

**No live load on the roof at blast — IS 4991 Cl. 11.2.** Static ULS on the roof is
1.5 × (40.65 + 2.0 + 22.5 + 20) = 127.7 kPa, so **blast governs 3.51 : 1.**

**Headhouse roof 396.5 kPa** = 383 + 12.5 self + 1.0 SIDL. **Headhouse walls 383 kPa acting on
either face** — the walls sit behind ~2.5 m of berm and earth transmits pressure; K<sub>a</sub>
for dry compacted fill is an assumption that cannot be verified, so the walls take the full
upper bound. Cost of that decision: one link cage. Utilisation 17 % → 59 %.

### 3.7  Seismic and wind

```
UNDERGROUND BOX -- IS 1893 (Part 1):2016
   Z 0.16 (Zone III)   I 1.5   R 4.0   Sa/g 2.5
   Ah = (Z/2)(I/R)(Sa/g) = 0.075        W = 14 002 kN  ->  Vb = 1050 kN
   Per long wall 525 kN -> tau = 0.063 N/mm2   NEGLIGIBLE
   IS 13920 Cl 10.4 boundary elements checked -- NOT triggered

SENTRY POST -- IS 1893 (Part 1):2016
   Z 0.16   I 1.5   R 3.0   Sa/g 2.5   ->  Ah = 0.100
   R = 3.0 because the infill is NOT separated from the frame.
   R = 5.0 would require a special moment frame with positively separated infill.
   Ta:  bare frame 0.297 s  |  with infill 0.281 s (X), 0.252 s (Z)
        all three inside 0.10-0.40 s, so Sa/g = 2.5 regardless
   *** DESIGN BASE SHEAR  Vb = 73.18 kN  ***   (the analysis model's value)
        confirmed by the reactions: Fx 18.295 kN per column x 4 = 73.18
        hand check gives 59.3 kN -- the model is 23 % heavier, and 73.18 GOVERNS

WIND, sentry post only -- IS 875 (Part 3):2015
   Vb 39 m/s (Pune)  k1 1.08  k2 1.00  k3 = k4 = 1.00
   Vz 42.12 m/s   pz 1.065 kPa   pd 0.859 kPa   F = 29.9 kN
   SEISMIC 73.18 vs WIND 29.9  ->  SEISMIC GOVERNS 2.4 : 1
```

**Zone III is externally corroborated** and A<sub>h</sub> reproduces exactly from Z = 0.16. `[C]`

### 3.8  Load combinations

**Underground box — five, and 103 governs every element**

| No. | Title | Factors |
|---|---|---|
| 101 | ULS static | 1.5 (DL + SIDL + LL + SOIL + UPLIFT) |
| 102 | ULS uplift | 0.9 DL + 1.5 UPLIFT |
| **103** | **BLAST** | **1.0 (DL + SIDL + SOIL + UPLIFT + BLAST)** |
| 104 | SLS crack width | 1.0 (DL + SIDL + LL + SOIL + UPLIFT), IS 3370 Pt 2 |
| 105 | Construction | 1.5 (DL + SOIL + UPLIFT + SURCHARGE) |

> **γ = 1.0 on blast** because it is an extreme event checked against **ultimate** capacity using
> **dynamic** material strengths (IS 4991 Cl. 10.3.1). Applying 1.5 *and* taking the 25 %
> material bonus would be inconsistent. **Wind and earthquake are absent from 103 — IS 4991
> Cl. 11.1 forbids combining them with blast.**

**Sentry post — sixteen:** 101 (1.5 DL + 1.5 LL); 102–105 (1.2 DL + 1.2 LL ± 1.2 EQ, X and Z);
106–109 (1.5 DL ± 1.5 EQ); 110–113 (0.9 DL ± 1.5 EQ); 201 service; **202 and 203 drift checks**,
EQ+X and EQ+Z, IS 1893 Cl. 7.11. `[C]`

---

## 4  Geometry

### 4.1  Coordinate system and levels

```
ORIGIN    = south-west EXTERNAL corner of the underground box, at ground level
X         = east   along the length, 0 to 22000
Y (plan)  = north  across the width, 0 to 6200
LEVELS    = metres relative to finished site grade 0.000, negative downwards
UNITS     = millimetres in all DXF geometry; metres in all level annotation
SITE      = project +X is EAST, project +Y is NORTH
```

| Level | Value | What it is |
|---|---|---|
| Grade | **0.000** | Finished site level, crowned, falls 1:50 away |
| Top of pressure slab | **(−)2.000** | = headhouse floor level |
| Roof soffit | **(−)2.900** | 900 slab |
| Internal floor / top of mat | **(−)6.100** | 3200 clear height |
| Underside of mat | **(−)6.700** | 600 mat |
| Formation / underside of PCC | **(−)6.800** | 100 blinding |
| **Design groundwater table** | **(−)2.000** | monsoon `[A]` |
| Rockhead | (−)1.500 to (−)2.000 | `[A]` |
| Stair landing L1 · L2 | (−)4.7333 · (−)3.3667 | 8 · 16 risers up from floor |
| Headhouse roof soffit · top | **+0.400** · **+0.900** | 2400 clear; no earth cover |
| Entry stairwell roof at head | **+2.450** | soffit +2.200 |
| Sentry post GF · 1F · roof · parapet | **+0.450** · **+3.650** · **+6.700** · **+7.000** | |
| Sump pit invert · base slab | (−)7.600 · (−)8.000 | |

### 4.2  The main box

| Item | Value | Class |
|---|---|---|
| **External length × width** | **22 000 × 6 200** | `[C]` |
| **Internal length × width** | **20 800 × 5 000** | `[C]` |
| Perimeter wall · roof slab · mat · PCC | **600 · 900 · 600 · 100** (M15) | `[C]` |
| Internal clear height | **3 200** | `[C]` |
| Engineered cover | **2 000 layered = 40.65 kPa** | `[C]` |

> **The roof spans ONE WAY across the 5 000 mm width.** Aspect ratio 20.8 / 5.0 = 4.2, and
> IS 456 Table 26 is tabulated only to l<sub>y</sub>/l<sub>x</sub> = 2.0, so two-way action
> **cannot be claimed**. The consequence governs the whole layout: **lengthening the box is
> structurally free; widening it is expensive** — going 5.0 → 6.0 m would raise the roof moment
> **44 %**. **Do not widen the box.**

### 4.3  Bays and internal walls

| Bay | X range | Clear | Use |
|---|---|---|---|
| 1 | 600 – 3500 | 2900 | Emergency stores, 1000 L potable tank, **ESC 1** |
| 2 | 3610 – 5410 | 1800 | Lavatory (1800×2000) + medical (1800×3000) |
| 3 | 5520 – 9020 | 3500 | Ops room and hazard plotting; **EMP Zone 2 enclosure** |
| 4 | 9130 – 10930 | 1800 | Berthing, 3 × 3-tier bunks, 9 berths |
| 5 | 11040 – 12600 | 1560 | CBRN plant: **2 × 300 m³/h** filter trains, CO₂/O₂, dehumidifier, **sump** |
| 6 | 12800 – 14800 | 2000 | Decon airlock, 3 stages (2000×2000, 2000×1500, 2000×1500) |
| 7 | **15200 – 18000** | **2800** | **Stair shaft** |
| 8 | **18400 – 21400** | **3000** | Generator 15 kVA (grey zone), **ESC 2** at X 19900 |

| Mark | X range | Thk | Notes |
|---|---|---|---|
| W8 partitions ×4 | 3500–3610, 5410–5520, 9020–9130, 10930–11040 | 110 | Each with a **permanent 900 door gap** at Y 2500–3400 |
| **W5** | 12600 – 12800 | **200** | Bay 5/6. Fire and gas-tight only — **no pressure differential** |
| **W6** | **14800 – 15200** | **400** | Bay 6/7. **Protective boundary.** Blast Door 1, Y 600–1800 |
| **W7** | **18000 – 18400** | **400** | Bay 7/8. **Protective boundary.** Blast Door 2, Y 600–1800 |

### 4.4  Stair shaft, roof void and cantilever pad

```
Stair shaft (Bay 7) clear        X 15200 - 18000   Y  600 - 5600   = 2800 x 5000
Void in the pressure slab        X 15200 - 18000   Y  600 - 3760   = 2800 x 3160
Cantilever pad, remaining slab   X 15200 - 18000   Y 3760 - 5600   = 2800 x 1840
Flight A (flights 1 and 3, stacked)  X 15300 - 16500   1200 wide
Well                                 X 16500 - 16700   200
Flight B (flight 2)                  X 16700 - 17900   1200 wide
Landing L1 (-)4.7333   Y 3760 - 4960, full 2800 width
Landing L2 (-)3.3667   Y  600 - 1800, stacked over the arrival landing
Arrival landing (-)6.100 = the mat surface, Y 600 - 1800
Store under landing L1  Y 4960 - 5600
MAIN STAIR   24R @ 170.8333  ·  tread 280  ·  3 flights x 8  ·  total rise 4100
             waist 200  ·  headroom 2533
```

**The pad is the far end of the void kept as slab so that it forms the headhouse floor.**

### 4.5  Escape shafts

| | **ESC 1** | **ESC 2** |
|---|---|---|
| Centre | **(2050, 2050)** | **(19900, 2050)** |
| Clear opening | **1400 dia** | **1400 dia** |
| Collar | 250 RC, OD 1900 | 250 RC, OD 1900 |
| Clearance, opening edge to wall face | 750 all round | 800 / 800 |
| Head level · climb from (−)6.100 | **+0.150 · 6.250 m** | **+0.700 · 6.800 m** |

> **THE 750 mm CLEARANCE RULE.** Opening edge to structural wall face **≥ 750** = 250 collar +
> ~400 trimmer band + 100 tolerance. **A bay must therefore be at least 1400 + 2 × 750 = 2900 mm
> wide to hold an escape shaft.** This rule sets Bay 1's and Bay 8's widths and it is not
> negotiable without redesigning the collar.

### 4.6  Entry headhouse

```
External     X 13600 - 18400   Y  200 - 6000   = 4800 x 5800
Internal     X 14000 - 18000   Y  600 - 5600   = 4000 x 5000
Walls 400 thk  (HW1 south, HW2 north, HW3 west, HW4 east)
Roof  500 thk, soffit +0.400, top +0.900, NO earth cover
Floor = the top of the 900 pressure slab, (-)2.000.  Clear internal height 2400
Inner security door 900 x 2100 in HW2 at X 14450 - 15350.  NOT blast rated
Berm graded against all four walls to +0.900 at 1.5 : 1
```

**Load path of each headhouse wall** `[C]`

| Wall | Runs | Length | Sits over |
|---|---|---|---|
| HW1 south | X | 4000 | Box south perimeter wall — direct |
| HW2 north | X | 4000 | Box north perimeter wall — direct |
| **HW3 west** | Y | 5000 | **Bay 6, mid-slab. NOTHING below it** — a line load on the pressure slab, checked at **26 % two-way / 41 % one-way bound** |
| HW4 east | Y | 5000 | **Wall W7 — they align exactly** |

### 4.7  Covered entry stairwell

```
External     X  9250 - 16050   Y 5750 - 7750   = 6800 x 2000
Internal     X  9500 - 15800   Y 6000 - 7500   = 6300 x 1500
Walls 250 RC both sides, headwall and east wall
Top landing  X  9500 - 11000  at 0.000, 250 thk
Flight       X 11000 - 14300, 12R @ 166.6667, going 300, 11 x 300 = 3300, waist 250
Platform     X 14300 - 15800  at (-)2.000, 1500 x 1500, 250 thk
Roof 250 RC raking, soffit 2200 above the flight -- and it STAYS 250 over the platform
Entry door 1000 x 2100 at grade in the headwall (X 9250 - 9500), opens OUTWARD
300 mm channel + grating, full 1500 width, at X 8950 - 9250
Stepped RC raft 300 thk on compacted fill
MOVEMENT JOINT where the raft meets the headhouse
1.0 m3 external sump at the platform, with its own soakaway
Berm 1.5:1 against the walls to +0.900, toe at grade over 1350
```

> **Outside the protective boundary. Not blast rated. Declared expendable** — it is expected to
> be lost in the design event, and the design says so rather than implying otherwise.
>
> **The movement joint is here and nowhere inside the envelope.** There are **no movement joints
> anywhere inside the protective envelope** — one would be a guaranteed blast, gas and EMP
> discontinuity.

### 4.8  Sentry post

```
External plan        4000 x 5000        Internal 3600 x 4600
Column grid          A-B  3650 c/c (X)   ·   1-2  4650 c/c (Y)
Grid coordinates     A: x 175   B: x 3825   |   1: z 175   2: z 4825
Columns C1           350 x 350, 4 No., both storeys
Beams B1             250 x 450 spanning A-B (3650 c/c), on grids 1 and 2
Beams B2             250 x 450 spanning 1-2 (4650 c/c), on grids A and B
Slab S1              150 thk two-way, 3650 x 4650 c/c, both floors
Plinth beam PB       250 x 400 at +0.450
Footings F1          1500 x 1500 x 600, 4 No., on IN-SITU BASALT at (-)2.000
Ground storey infill 190 one-brick modular brickwork, IS 1077, in CM 1:6, built
                     inside the unchanged 200 structural zone between column faces;
                     the residual 10 mm taken up at the internal face in the plaster
First storey infill  armoured vision panels, 1200 wide -- openings, not construction
Spiral stair         external, 1000 R, 250 dia central pole
Door D1              900
Storey heights       ground 3200 (+0.450 -> +3.650), first 3050 (+3.650 -> +6.700)
Siting               >= 10 m clear of the shelter excavation
```

**Lintel L1 — one type over every opening**, eleven in all (ground D1 900 and W1 1200; first
storey D1 900 and the eight 1200-wide vision-panel openings):

```
190 wide x 150 deep, M30 / Fe500, cover 30, bearing 200 each end
2-T10 bottom  ·  2-T8 top (hangers)  ·  T6 two-legged links @ 150
Leff = min(clear + d, c/c bearings) = min(1315, 1400) = 1.315 m   IS 456 Cl 22.2
```

> **The opening HEIGHTS are not stated on any drawing** `[N]`. L1 is therefore designed to the
> bound that does not use one: masonry standing **just below** the 60° arching height
> (0.866 × 1.315 = 1.139 m), which is the heaviest case any opening height can produce — above
> it arching relieves the lintel, below it there is less masonry. **The design holds whatever
> the heights turn out to be.** w = 4.33 kN/m, M<sub>u</sub> = 1.403 against M<sub>u,lim</sub> =
> 10.03 kNm (**14 % utilised**); A<sub>st</sub> required 29.5 mm², **Cl. 26.5.1.1 minimum 37.1
> mm² governs**, 2-T10 = 157 provided. τ<sub>v</sub> 0.195 < τ<sub>c</sub> ≈ 0.56 → no shear
> steel; the T6 links are the Cl. 26.5.1.6 nominal minimum. **The lintel carries masonry only** —
> floor and roof go to B1 / B2, which is the whole point of the frame.

**Wall ties:** 6 mm dia MS ties at **every fifth course (≈ 450)** up both column faces,
projecting **200** into the bed joint, anchored by a cast-in or drilled-and-grouted 10 mm dowel.
**The top course is built tight to the beam soffit and the last joint packed**, because the
analysis takes **R = 3.0** — the infill is **not** separated from the frame and must not be.

> **Two consequences of masonry infill are open and are not closed here.** The seismic weight
> falls to ≈ 9.9 kN/m from the 13.000 kN/m modelled — **lighter, so V<sub>b</sub> = 73.18 kN
> stays conservative, but that is a direction, not a verification** and the check must be re-run.
> And **brick does not give the ballistic protection the original "200 RC ballistic panels" were
> named for.** That is a client / military decision, not a drafting one.

---

## 5  Exit hatches and blast doors

Every opening through the protective boundary, in one place.

**Doors**

| Mark | Where | Leaf | Level | Rating | Class |
|---|---|---|---|---|---|
| **Blast Door 1** | **W6** (400 thk), opening Y 600–1800 — stair shaft → Bay 6 | **1200 × 2100** | **(−)6.100** | **≥ 7 bar, gas-tight, rebound-rated** | `[C]` geometry · **`[V]` the door is proprietary** |
| **Blast Door 2** | **W7** (400 thk), opening Y 600–1800 — stair shaft → Bay 8 | **1200 × 2100** | **(−)6.100** | **≥ 7 bar** | `[C]` · **`[V]`** |
| Inner security door | **HW2**, headhouse north wall, X 14450–15350 | 900 × 2100 | (−)2.000 | **NOT blast rated** | `[C]` |
| Entry door | Entry stairwell headwall, X 9250–9500, **opens outward** | 1000 × 2100 | 0.000 | **NOT blast rated** — outside the boundary | `[C]` |
| **D-05**, the W5 gas-tight door | **W5** | — | (−)6.100 | — | **`[N]`. W5 is designated *fire and gas-tight* and no door exists in it anywhere in the project.** Escape route R1 has to cross it |
| W8 partition gaps ×4 | Bays 1/2, 2/3, 3/4, 4/5 | **permanent 900 gap**, Y 2500–3400 | (−)6.100 | **no doors, by design** | `[C]` |

**Both blast doors are the protective boundary**, and they sit in the same plane as W6 / W7.
That is why those walls are 400 thick: the shaft equalises to full p<sub>so</sub>, so the doors
and the walls beside them take the same 383 kPa. Opening reinforcement is **4-T20 each jamb each
face** anchored L<sub>d</sub> 800 beyond, over a **400 × 1100 header, 4-T20 top + 4-T20 bottom,
T12 4-leg links @ 150**. Each frame is a **cast-in steel frame anchored into and welded to the
cage** — that weld is both the blast fixing and the only EMP continuity the opening has.

**Escape shaft heads**

| | **ESC 1** | **ESC 2** |
|---|---|---|
| Bay / centre | Bay 1, **(2050, 2050)** | Bay 8, **(19900, 2050)** |
| Shaft | **1400 dia clear**, 250 RC collar, OD 1900 | as ESC 1 |
| Head level · climb from (−)6.100 | **+0.150 · 6.250 m** | **+0.700 · 6.800 m** |
| Escape route | **R2** | **R3** — **shares Bay 8 with the generator** |

> **Three things the project does not hold for these openings, and must not invent:**
>
> **1. No hatch on either shaft head.** No leaf, frame, fixing or bonding detail exists anywhere
> `[N]`. What it has to be is established — a **bonded conducting hatch at the head**, because a
> 1400 dia shaft propagates above **125.5 MHz** however well it is lined — but the specification
> itself is vendor data the project does not contain.
>
> **2. No way to climb either shaft.** No ladder, no rung, no fall-arrest is specified `[N]`.
> These are **6.250 m and 6.800 m vertical climbs** and they are two of the three escape routes.
> **This one needs a design, not a ruling.**
>
> **3. No blast-door vendor data of any kind**, RF performance included `[N]`. Blast Door 1 is
> the only thing across the entry path's open electromagnetic route from grade to Bay 7.

---

## 6  Structural design — element by element

Flexure throughout is **IS 456 Annex G-1.1(b)**:

```
Mu = 0.87 fy . Ast . d . [ 1 - (Ast.fy)/(b.d.fck) ]
xu = 0.87 fy Ast / (0.36 fck b)                       IS 456 Cl 38.1
xu,max/d = 0.46 for Fe500                             IS 456 Cl 38.1(f)
Mu,lim = 0.133 fck b d2                               IS 456 Annex G-1.1(c)
```

### 6.1  Perimeter walls W1–W4, 600 thk — 68 %

```
d = 600 - 75 - 8 = 517.  Blast 383 kPa (Ka 1.0) vs static earth+water 83.2 kPa at base
     -> BLAST GOVERNS 4.6 : 1
Mp = w.Ln2/16 = 383 x 3.2002/16                    = 245.1 kNm/m   (fixed-fixed plastic)
Mu,lim = 0.133 x 43.75 x 1000 x 5172                = 1556 kNm/m  -> singly reinforced
Ast,req (fy,dyn 625, fck,dyn 43.75)                 = 894 mm2/m
   IS 456 Cl 32.5(a) min vertical  0.0012 x 600     = 720
   IS 456 Cl 32.5(b) min horizontal 0.0020 x 600    = 1200
   IS 3370 Pt 2 surface zone 0.35 % x 250 each face = 875 mm2/m/face
ADOPTED  T16 @ 150 EACH FACE EACH WAY = 1340 mm2/m
         Mu 362.8 kNm/m  ->  UTILISATION 68 %   ·   xu/d = 0.089

SHEAR  V at d = 383 (1.600 - 0.517)                 = 414.8 kN/m
       tau_v 0.802 | tau_c 0.375 (pt 0.259 %) | tau_c,max 3.70   OK
       Vus 220.8 kN/m ; Asv/sv 0.982 -> T12 2-leg at 230
       Cl 26.5.1.5 limit min(0.75d 388, 300) = 300
ADOPTED  T12 CLOSED LINKS @ 200 c/c   (Asv/sv 1.131)

AXIAL  N = 448.15 x 2.50 + 3.2 x 0.6 x 25 = 1168 kN/m ; f = 1.95 N/mm2
       = 11 % of 0.4 fck,dyn  ->  P-M not critical
CRACK  IS 3370 Pt 2, 0.2 mm limit; surface steel 875 < 1340 provided
```

> **Why 600 mm, stated honestly.** The wall is **not** strength-governed at 68 %. 600 is set by
> (i) 75 mm cover, (ii) congestion — two curtains, closed links, waterstops and cast-in frames,
> (iii) IS 3370 crack control under sustained hydrostatic load, (iv) the EMP double curtain at
> 150, and (v) the 1168 kN/m axial path.

### 6.2  Walls W6 / W7, 400 thk — 69 % — and why 200 was impossible

> **The governing finding of the whole project.** The stair shaft is open to atmosphere through
> the 2800 × 3160 roof void, the headhouse and the entry stairwell. Fill time
> **V/(A·c) = 105/(3.3 × 340) = 0.094 s** against t<sub>d</sub> 0.13–1.33 s, so **the shaft
> equalises to full p<sub>so</sub>.** W6 and W7 stand in the same plane as the 7-bar blast doors,
> separating a pressurised shaft from Bay 6 / Bay 8 at ambient. **They are boundary elements and
> must be designed as such.**

```
WHY 200 CANNOT WORK -- not a detailing problem, an impossibility
     d = 200 - 40 - 6 = 154
     Mu,lim = 0.133 x 43.75 x 1000 x 1542           = 138.0 kNm/m
     Demand Mp = 383 x 3.2002/16                     = 245.1 kNm/m
     138 < 245  ->  NO STEEL RATIO MAKES IT WORK
     Two-way action checked BEFORE rejection: panel 3200 x 3800, fixed on 3 edges,
     yield line ~ 0.7 x one-way = 172 kNm/m -- still above 138.

DESIGN OF THE 400 WALL
     d = 400 - 50 (shaft face) - 8                   = 342
     Mp 245.1  |  Mu,lim 680.6 kNm/m  |  Ast,req     = 1400 mm2/m
ADOPTED   T20 @ 150 EF EW = 2094 mm2/m -> Mu 355.3, UTIL 69 %, xu/d 0.211

SHEAR  V at d = 383 (1.600 - 0.342) = 481.8 kN/m
       tau_v 1.409 | tau_c 0.540 (pt 0.612 %) | tau_c,max 3.70   OK
       Vus 297.2 ; Asv/sv 1.998 -> T12 4-leg at 226 ; Cl 26.5.1.5 limit 257
ADOPTED   T12 4-LEGGED LINKS @ 200 c/c
```

### 6.3  Mat foundation, 600 thk — 84 %, the most heavily worked element

```
BEARING    Service 58.4 kPa (1.8 % of 3240) ; Blast 404.9 kPa (12.5 %)
           BEARING GOVERNS NOTHING.

CASE 1 -- NET UPLIFT (COMB 102)
     u 46.11 kPa, self 15.0 -> net 31.1 kPa UP over the 5000 clear
     Mp = 31.1 x 5.02/16 = 48.6 kNm/m                NOMINAL

CASE 2 -- SOFT / RED-BOLE ZONE   *** GOVERNS ***
     A 3.0 m band of red-bole or vesicular material removed, in its worst position
     q 404.9 kPa over a 3.0 m unsupported span
     M = q.L2/12 = 404.9 x 9/12                      = 303.7 kNm/m
     d 517 ; Ast,req                                 = 1115 mm2/m
ADOPTED  T16 @ 150 EF EW = 1340 -> Mu 362.8, UTILISATION 84 %

THICKNESS STUDY   500 -> Ast,req 1407 = 105 % of provided   FAIL
                  600 -> 1115 = 84 %                        ADOPTED
                  700 ->  926 = 70 %   |   800 ~ 57 %, i.e. 33 % unused

ONE-WAY SHEAR
     V at d from the soft-band edge = 404.9 (1.500 - 0.517) = 398.0 kN/m
     tau_v 0.770 | tau_c 0.375 | tau_c,max 3.70    (no dynamic increase, Cl 10.3.1.1)
     Vus 204.2 ; Asv/sv 0.908
ADOPTED  T12 CLOSED LINKS ON A 250 x 250 GRID THROUGHOUT
         supplied Asv/sv = (4 x 113.1)/250 = 1.810 = 2.0 x required
         -- and it doubles as the spacer system between the two curtains.

PUNCHING     IS 456 Cl 31.6 -- no column or pedestal bears on the mat; the headhouse
             walls bear on the ROOF.  NOT APPLICABLE -- declared, not ignored.
SLIDING      Box socketed ~4.8 m into basalt, 300 annulus backfilled M15 lean.
             Not a credible mechanism -- reasoning stated, no spurious factor computed.
OVERTURNING  Buried box, symmetrical lateral load.  NOT APPLICABLE.
SETTLEMENT   Negligible on sound basalt (IS 12070 Cl 6).  The hazard is the flow contacts.
```

**FLOTATION — the construction stage governs, and it is a design output, not a contractor's
problem.**

| Stage | Weight | Uplift | FoS @ (−)2.000 | FoS flooded to GL |
|---|---:|---:|---:|---:|
| 1 · mat cast only | 2 009 kN | 6 175 kN | **0.33 FAIL** | 0.23 FAIL |
| 2 · mat + walls, no roof | 4 802 | 6 175 | **0.78 FAIL** | 0.55 FAIL |
| 3 · box complete, no backfill | 7 528 | 6 175 | **1.22 MARGINAL** | 0.86 **FLOATS** |
| 4 · backfilled + cover | 12 453 | 6 175 | **2.02 OK** | 1.41 OK |

Require FoS ≥ 1.2. ULS COMB 102 = **1.21**.

> **Read the absolute figures in that table at the 21.600 box scale**, which is where they were
> derived: 21.600 × 6.200 = **133.92 m²**, and 46.11 × 133.92 = **6 175 kN**. At the built
> 22.000 box the underside is **136.40 m²** and uplift is **6 289 kN**, and the weights scale by
> the same 22.0/21.6 = 1.01852 — so **every factor of safety is unchanged**: 0.325 / 0.778 /
> 1.219 / 2.017, and COMB 102 = 0.9 × 12 684 / (1.5 × 6 289) = **1.21**.
> **The hand check uses 136.40 m² and 6 289 kN**, which is the figure §3.4 carries. Uplift acts
> on the **real underside**, never on the plate model's mid-surface area.

**Mandatory mitigation — four items, all of them design requirements:**

1. **Continuous dewatering** from the start of excavation until backfill and cover are complete.
2. **Temporary pressure-relief valves / knock-out plugs in the mat** (6 No.), grouted up **only
   after** backfill.
3. Programme the sub-structure to complete **before the monsoon**, or bund and positively drain
   with standby pumping and generator back-up.
4. **Backfill symmetrically, in layers.**

> **Flotation can never be read off the analysis model.** The `ELASTIC MAT` springs take
> **tension**, so the model will never show the raft lifting off. **It is a hand check.**

### 6.4  Pressure (roof) slab, 900 thk — 51 % — THE GOVERNING ELEMENT

```
NATURAL PERIOD
     m = 0.900 x 2500 + 0.25 x 2.0 x 2000            = 3250 kg/m2
     0.5 EIg = 0.5 x 2.958e10 x 0.9003/12            = 8.985e8 N.m2/m
     f1 = (22.373/2pi).sqrt(EI/(m.Ln4))              = 74.9 Hz  ->  T = 13.4 ms
     td/T = 10 to 100  ->  QUASI-STATIC.  This is what licenses the DLF approach.

FLEXURE
     d = 900 - 75 - 12.5                             = 812.5
     Mp = w.Ln2/16 = 448.15 x 25/16                  = 700.2 kNm/m
     Mu,lim = 0.133 x 43.75 x 1000 x 812.52          = 3841 kNm/m
     Ast,req (pt 0.20 %)                             = 1632 mm2/m
     Cl 26.5.2.1 min 0.12 % x 900 = 1080  ·  Cl 26.5.2.2 max bar dia D/8 = 112  (T25 OK)
ADOPTED   T25 @ 150 EF EW = 3272 mm2/m
          Mu 1362.4 kNm/m  ->  UTILISATION 51 %   ·   xu = 113.0, xu/d = 0.139
          *** xu/d = 0.139 IS THE PROOF THAT mu = 5 IS DEFENSIBLE ***

SHEAR     V at support face = 448.15 x 2.50          = 1120 kN/m
          V at d from face                            = 756.3 kN/m
          tau_v 0.931 | tau_c 0.450 (pt 0.403 %) | tau_c,max 3.70   OK
          Vus 390.8 ; Asv/sv 1.106 -> T12 4-leg at 409 ; Cl 26.5.1.5 limit 300 GOVERNS
ADOPTED   T12 4-LEG @ 250 IN THE END 1500 EACH SIDE ; T12 2-LEG @ 300 ELSEWHERE

DIRECT SHEAR  Vd,max = 0.16 fck,dyn b d = 5688 kN/m vs 1120 applied = 19.7 %
              [UFC 3-340-02 §4-30, cited AS US criteria -- not an IS 456 check]

THICKNESS STUDY
   t     d      Mp     Ast,req   tau_v   verdict
   600   512.5  689    2673      1.71    links at 164, congested
   800   712.5  696    1868      1.12    structural optimum
   900   812.5  700    1633      0.93    ADOPTED
  1000   912.5  704    1453      0.78    11 % over
```

**900 is adopted over the 800 optimum for three stated reasons:** reserve at the 1400 dia
collars; headroom against a raised design threat while the yield is unconfirmed; and keeping
support rotation inside 2° without resorting to UFC lacing.

### 6.5  Roof openings

**(a) The two 1400 dia escape-shaft openings**

```
Interrupted steel = 3272 x 1.400                     = 4581 mm2/face/direction
Trimmers each side = 4581/2                          = 2291 mm2
ADOPTED  5 No. T25 EACH SIDE, EACH FACE, EACH DIRECTION (2454 mm2)
         anchored Ld = 1000 beyond the opening
         Collar 250 RC ; T16 @ 150 hoops (3 layers) + T16 @ 150 radials
         Slab thickened 900 -> 1200 over a 600 mm annulus
```

**Circular is the right shape** — hoop action, and **no re-entrant stress concentration**. This
detail is what sets the 750 mm clearance rule in §4.5.

**(b) The 2800 × 3160 rectangular stair void — the cantilever that exceeds midspan**

```
The void leaves an 1840 mm CANTILEVER of 900 slab, 2800 wide, at 448.15 kPa.
M(root) = 448.15 x 1.8402/2                          = 758.6 kNm/m
   *** THIS EXCEEDS THE 700.2 kNm/m MIDSPAN Mp ***
Ast,req TOP 1772 mm2/m  <  3272 provided  ->  UTILISATION 56 %
V(root) = 448.15 x 1.840                             = 824.6 kN/m
tau_v 1.015 > tau_c 0.450 ; Vus 459.4 ; Asv/sv 1.300 -> T12 4-leg at 348
Cl 26.5.1.5 limit 300
ADOPTED  T12 4-LEG LINKS @ 250 THROUGHOUT THE PAD
   plus  free edge thickened 900 -> 1200 over 600, with 6-T25 top + 6-T25 bottom
         and T12 closed links @ 150
   plus  6 No. T25 each face, top and bottom, in a 900 band over W6 and W7
   plus  diagonal trimmers 4 No. T25 each face at 45 deg at BOTH re-entrant corners,
         2000 long each way, anchored Ld beyond
   plus  1100 mm guarding to the free edge  (NBC 2016 Part 4)
```

### 6.6  Main staircase, Bay 7

> **Inside the protective envelope, but NOT a blast element.** The shaft pressurises, and that
> pressure acts on the shaft **walls** and the blast **doors** — not as a net load on a slab that
> is open on both faces. **Designed to IS 456 with normal partial factors, NOT with IS 4991
> dynamic strengths**, and that is stated on the drawing.

**Geometry against NBC 2016 Part 4**

| Item | Provided | Limit | |
|---|---|---|---|
| Riser | **170.8333** | ≤ 190 | ✔ |
| Tread / going | **280** | ≥ 250 | ✔ |
| Flight width | **1200** | ≥ 1000 | ✔ stretcher-capable |
| Risers per flight | **8** | ≤ 12 preferred | ✔ |
| Headroom | **2533** | ≥ 2200 | ✔ |
| Total rise | **4100 = 24 × 170.8333** | (−)6.100 → (−)2.000 | **closes exactly** |

```
FLIGHT -- waist 200
   theta = arctan(170.833/280) = 31.4 deg, cos = 0.8535
   waist self 5.858 + steps 2.135 (Cl 33.2) + finishes 1.000 + live 5.000 = 13.99
   wu = 1.5 x 13.99                                  = 21.0 kPa
   Leff = going + min(landing/2, 1000) each end  Cl 33.1(b)
        = 1960 + 600 + 600                           = 3160
   d = 200 - 30 - 6 = 164 ; M = wu.Leff2/8           = 26.2 kNm/m
   Ast,req 380 ; Cl 26.5.2.1 min 240
   ADOPTED  T12 @ 150 MAIN (754) -> Mu 50.3, UTIL 52 %  ;  T10 @ 200 DISTRIBUTION
   DEFLECTION  Leff/d 19.3 ; fs 146 ; pt 0.46 % ; MF ~1.9 -> permissible 38    OK
   SHEAR  tau_v 0.202 < tau_c 0.479 x k 1.20 = 0.575  ->  no links
   TOP STEEL  T12 @ 150 for 0.25 Leff = 800 into the flight, anchored Ld 480

LANDINGS L1 / L2 / ARRIVAL -- 200 thk, spanning ACROSS the shaft
   self 7.50 + finishes 1.50 + live 7.50 + flight reaction 27.70 = 44.20 kPa
   Leff = 2800 clear + 200 bearing  Cl 22.2(a)       = 3000
   M = 44.2 x 3.0002/8                               = 49.7 kNm/m
   Ast,req 745 ; T12 @ 150 gives 754 = 100 %  TOO TIGHT
   ADOPTED  T12 @ 125 BOTTOM (905) -> Mu 59.5, UTIL 84 %
            T12 @ 125 TOP for 900 from each support ; T10 @ 200 distribution
   DEFLECTION 18.3 < 27   ·   SHEAR tau_v 0.404 < 0.622    OK
```

**Compatibility:** the arrival landing at (−)6.100 **is** the mat surface — there is no separate
slab. Flight 3 lands directly on the 900 pressure-slab pad at (−)2.000. The landings prop W6 and
W7 at (−)4.733 and (−)3.367, **but only over their 1200 depth — and the 400 wall design in §6.2
does NOT rely on that prop.**

### 6.7  Entry (approach) stairwell

> **Outside the protective boundary, not blast rated, expected to be LOST in the design event.**
> Designed to IS 456 with normal partial factors.

```
FLIGHT -- 12R @ 166.6667 / 300, 1500 wide, waist 250
   theta 29.05 deg ; waist 7.150 + steps 2.083 + finishes 1.000 + live 5.000 = 15.233
   wu 22.85 kPa ; Leff = 3300 + 750 + 750            = 4800
   d = 250 - 30 - 8 = 214 ; M = 22.85 x 4.8002/8     = 65.8 kNm/m
   Ast,req 744 ; min 300
   ADOPTED  T16 @ 200 MAIN (1005) -> Mu 87.3, UTIL 75 %, xu/d 0.162
            T10 @ 200 DISTRIBUTION ; T16 @ 200 TOP for 1200 into the flight, Ld 640
   DEFLECTION 22.4 < 30  ·  SHEAR tau_v 0.256 < 0.532  ->  no links

SIDE WALLS 250 -- retained 2.9 m, propped by roof and raft
   sigma_h at base = 0.5 x 20 x 2.900 + 0.5 x 10     = 34 kPa
   M ~ w.L2/12 on an equivalent 20 kPa UDL           = 14.0 kNm/m ; Ast,req 168
   Cl 32.5(a) min 300 · Cl 32.5(b) 500 · Cl 32.5(c) two curtains required (t > 200)
   ADOPTED  T12 @ 200 EF EW -- MINIMUM STEEL GOVERNS, 31 % utilised

RAKING ROOF 250 -- 1500 clear
   self 6.25 + wp/screed 2.0 + earth lap 5.4 + IMPOSED 20 = 33.65 -> wu 50.5 kPa
   (20 kPa imposed deliberately, for a stray vehicle on the berm)
   M = w.l2/12 = 9.5 kNm/m ; Ast,req 108 ; min 300 GOVERNS
   ADOPTED  T12 @ 200 EF EW -> 20 % utilised

TOP LANDING 250 (0.000)  wu 54.9 kPa ; Leff 1750 ; M 21.0 ; ADOPTED T12 @ 200 EF EW, 41 %
PLATFORM 250 ((-)2.000, on fill) · HEADWALL 250 · STEPPED RAFT 300 on compacted fill
   ADOPTED  T12 @ 200 EF EW throughout
Door lintel over 1000 clear: 250 x 350, 3-T12 top + 3-T12 bottom, T8 @ 150
```

> **THE OPENING CORNER — the detail most often got wrong.** At the **top** of the flight the
> tension face turns through **209°**. A bar bent round that corner has its bend resultant
> directed **out of the concrete**: it spalls the cover and the bar loses anchorage.
> **MAIN BARS SHALL NOT BE BENT ROUND IT.** Each layer is continued straight, **crossed**, and
> anchored L<sub>d</sub> = 640 into the **opposite** face, with a **U-bar T16 @ 200** across the
> corner. (SP 34:1987 Cl. 5.5.) At the **foot** of the flight the corner **closes** (151°) and
> bars may turn normally.

### 6.8  Entry headhouse

**Roof, 500 thk — 90 %, the most heavily worked element in the project**

```
w = 383 blast + 12.5 self + 1.0 SIDL                  = 396.5 kPa
Panel 4000 x 5000 clear, monolithic with 400 walls on all four sides, ly/lx 1.25
d = 500 - 75 - 10 = 415 ; Mu,lim                      = 1002 kNm/m

THREE ANALYSES, MOST CONSERVATIVE ADOPTED
  1  One-way fixed-fixed strip, Mp = w.Ln2/16         = 396.5  <- ADOPTED
  2  IS 456 Table 26 Case 1, alpha_x- = 0.045 at 1.25 = 285.5
  3  Yield line, fixed 4 edges, isotropic             = 162.2
     wu = 48m / [a2(sqrt(3 + (a/b)2) - a/b)2]
     VALIDATION: as b -> infinity, 48/3 = 16 = the fixed-fixed strip w.L2/16

Ast,req (one-way basis) 1879 ; Cl 26.5.2.1 min 600
ADOPTED  T20 @ 150 EF EW = 2094 -> Mu 438.5 kNm/m
         UTILISATION 90 % one-way | 65 % Table 26 | 37 % yield line   ·   xu/d 0.174

SHEAR    V at d = 396.5 (2.000 - 0.415)               = 628.4 kN/m
         tau_v 1.514 | tau_c 0.502 | tau_c,max 3.70   (tau_c at the STATIC M35 value)
         Vus 420.0 ; Asv/sv 2.327 -> T12 4-leg at 194 ; Cl 26.5.1.5 limit 300
ADOPTED  T12 4-LEG @ 175 IN THE END 1200 EACH SIDE ; @ 250 ELSEWHERE
```

**No opening in the headhouse roof** — the stair void is in the **floor**. Corner torsion steel
(Cl. D-1.8) is **not** required: all four edges carry full T20 @ 150 hogging steel continuous
into the walls. **Haunch 300 × 300 at all four wall–roof junctions, diagonal T16 @ 150.**

**Walls HW1–HW4, 400 thk — 59 %** at the full 383 kPa either face, T16 @ 150 EF EW with
T12 4-leg links @ 250 throughout. **HW3 is the wall with nothing under it** — a line load on the
pressure slab, checked at 26 % (two-way) and 41 % (one-way bound), with **4-T25 extra top and
bottom in a 1200 band** beneath it, lapped 1250.

### 6.9  Sentry post

```
SEISMIC MEMBER FORCES -- portal method at Vb = 73.18 kN
SLAB S1, 150 thk two-way, 3650 x 4650 c/c
     wu floor = 1.5(4.75 + 3.00) = 11.625 kPa  GOVERNS  |  wu roof 10.125 kPa
     ADOPTED  T8 @ 150 BOTH WAYS bottom (335 mm2/m)  ->  69 %
              T8 @ 300 top at discontinuous edges, 400 (0.1 L) into the span, Cl D-1.6
              T8 @ 200 CORNER TORSION, FOUR LAYERS, 700 x 700 at all four corners, Cl D-1.8

LOAD PATH TO BEAMS -- IS 456 Cl 24.5, 45 deg yield lines
     Peak intensity on any beam = w x short span/2 = w x 1.825 m
     SHORT beams B1 (3650) -> TRIANGLE
     LONG  beams B2 (4650) -> TRAPEZOID, w_eq = w_peak x [1 - 1/(3r2)], r 1.274 -> 0.7946

BEAM B1  250 x 450, span 3650   ADOPTED  4-T16 top at supports ; 2-T16 bottom   84 %
BEAM B2  250 x 450, span 4650   ADOPTED  3-T20 top at supports ; 2-T20 bottom   89 %
    hoops both: T8 2-leg @ 100 over 2d = 810 from each face ; @ 150 elsewhere
COLUMN C1  350 x 350   ADOPTED  8-T16 (1608 mm2, p 1.31 %)   biaxial 0.819
    T10 hoops + one cross-tie each way @ 85 over 500 from every joint face, top and
    bottom AND THROUGH THE JOINT ; T8 @ 150 elsewhere
FOOTING F1  1500 x 1500 x 600 on IN-SITU BASALT at (-)2.000  ADOPTED T12 @ 150 B/W
```

> **3-T20 was chosen for B2 over 5-T16 because five T16 bars need 256 mm in a 250 mm wide beam.**
> That is exactly the check that becomes a site RFI if it is skipped.

> **F1 bears on in-situ rock, never on backfill.** The surface soil is black cotton at free swell
> index 60–65 %, and that instruction is now backed by a measurement rather than by caution.

---

## 7  Reinforcement register

Notation: `T16 @ 150 EF EW` = 16 mm Fe500D deformed bars at 150 centres, **E**ach **F**ace,
**E**ach **W**ay. `4L` = four-legged links. **Total 92 bar marks, 70.46 t.**

### 7.1  Underground box

| Element | Size | Cover | d | Main | Links | A<sub>st</sub> prov | x<sub>u</sub>/d | Util. |
|---|---|---|---|---|---|---|---|---|
| **W1–W4** perimeter | 600 | 75/50/40 | 517 | **T16 @ 150 EF EW** | T12 closed @ 200 | 1340/face | 0.089 | 68 % |
| **W5** Bay 5/6 | 200 | 40 | 154 | T12 @ 150 EF EW | — | 754/face | — | nominal |
| **W6 · W7** Bay 6/7, 7/8 | **400** | 50/40 | 342 | **T20 @ 150 EF EW** | **T12 4L @ 200** | 2094/face | 0.211 | 69 % |
| **W8** partitions ×4 | 110 | 25 | — | A252 mesh both faces | — | 252 | — | non-structural |
| **MAT** | 600 | 75/50 | 517 | **T16 @ 150 EF EW** | **T12 @ 250 × 250 grid** | 1340/face | 0.089 | **84 %** |
| **ROOF** midspan | 900 | 75 | 812.5 | **T25 @ 150 EF EW** | T12 4L @ 250 end 1500 / 2L @ 300 mid | 3272/face | 0.139 | 51 % |
| **ROOF** cantilever pad | 900 | 75 | 812.5 | T25 @ 150 top continuous | **T12 4L @ 250 throughout** | 3272 | 0.139 | 56 % |
| Sump pit walls / base | 300/400 | 50 | 244 | T16 @ 150 EF EW | — | 1340 | — | nominal |

**Additional bars — and none of these is optional**

| Location | Requirement |
|---|---|
| Wall starters | T16 @ 150 EF, **900 horizontal leg into the mat**, lap 800 (50 φ) above a 150 kicker |
| All wall–roof and wall–mat junctions | **Haunch 500 × 500, diagonal T20 @ 150** |
| Mat edge, all free edges | **T16 @ 150 U-bars** closing both curtains |
| Sump pit opening | **4-T20 trimmers each face each side**, L<sub>d</sub> 800 beyond |
| **Blast door jambs (W6, W7)** | **4-T20 each jamb each face**, L<sub>d</sub> 800 beyond |
| **Blast door header** | **400 × 1100: 4-T20 top + 4-T20 bottom, T12 4L @ 150** |
| **ESC 1 / ESC 2 collars** | Collar 250 RC; **5-T25 each side, each face, each direction**, L<sub>d</sub> 1000 beyond; **T16 @ 150 hoops ×3 layers + T16 @ 150 radials**; slab thickened 900→1200 over a 600 annulus |
| Stair void free edge | Thickened 900→1200 over 600; **6-T25 top + 6-T25 bottom, T12 closed @ 150** |
| Stair void side bands | **6-T25 each face, top and bottom, in a 900 band over W6 and W7** |
| Stair void re-entrant corners ×2 | **4-T25 each face at 45°, 2000 long each way**, anchored L<sub>d</sub> beyond |
| Band beneath headhouse wall HW3 | **4-T25 extra top and bottom in a 1200 band**, lapped 1250 |
| **Construction joints (~6 m)** | Reinforcement **fully continuous**; **two waterstops + a welded Cu/galv EMP strap** |

### 7.2  Stairs

| Element | Size | Cover | d | Main | Distribution | Top steel |
|---|---|---|---|---|---|---|
| Main stair flight waist | 200 | 30 | 164 | **T12 @ 150** (754) | T10 @ 200 | T12 @ 150 for 800 into the flight, L<sub>d</sub> 480 |
| Main stair landings L1/L2/arrival | 200 | 30 | 164 | **T12 @ 125 bottom** (905) | T10 @ 200 | T12 @ 125 for 900 from each support |
| Entry stairwell flight waist | 250 | 30 | 214 | **T16 @ 200** (1005) | T10 @ 200 | T16 @ 200 for 1200 into the flight, L<sub>d</sub> 640 |
| Entry stairwell top landing · platform · side walls · raking roof · headwall | 250 | 30/50 | 194–214 | **T12 @ 200 EF EW** (565) | — | minimum steel governs |
| Entry door lintel (1000 clear) | 250 × 350 | 30 | 306 | 3-T12 top + 3-T12 bottom | T8 @ 150 | — |
| Stepped raft | 300 | 50 | 244 | T12 @ 200 EF EW | — | on compacted fill |
| **Opening-corner U-bar** | — | — | — | **T16 @ 200 U-bar**, bars **CROSSED**, anchored L<sub>d</sub> 640 into the opposite face | | SP 34 Cl. 5.5 |

### 7.3  Headhouse

| Element | Size | Cover | d | Main | Links |
|---|---|---|---|---|---|
| **Roof** | 500 | 75 | 415 | **T20 @ 150 EF EW** (2094) | **T12 4L @ 175 in the end 1200 each side; @ 250 elsewhere** |
| **Walls HW1–HW4** | 400 | 50/40 | 342 | **T16 @ 150 EF EW** (1340) | **T12 4L @ 250 throughout** |
| Door jambs, HW2 | — | — | — | **2-T20 each jamb each face**, L<sub>d</sub> 800 beyond | — |
| Door head edge band | 400 × 800 | 40 | 742 | **4-T20 top + 4-T20 bottom** | T12 4L @ 150, over the opening + 600 each side |
| Wall–roof haunch | 300 × 300 | — | — | diagonal T16 @ 150 | — |

### 7.4  Sentry post

| Element | Size | Cover | d | Reinforcement |
|---|---|---|---|---|
| **Slab S1** bottom | 150 | 30 | 116/108 | **T8 @ 150 BOTH WAYS** (335 mm²/m) |
| S1 top, discontinuous edges | 150 | 30 | 116 | **T8 @ 300, 400 (0.1 L) into the span, all four edges** — Cl. D-1.6 |
| S1 corner torsion | — | — | — | **T8 @ 200, FOUR LAYERS, 700 × 700 at all four corners** — Cl. D-1.8 |
| **Beam B1** (3650) | 250 × 450 | 30 | 404 | **4-T16 top at supports; 2-T16 bottom continuous** |
| **Beam B2** (4650) | 250 × 450 | 30 | 404 | **3-T20 top at supports; 2-T20 bottom continuous** |
| Beam hoops, both | — | — | — | **T8 2-leg @ 100 over 2d = 810 from each face; @ 150 elsewhere**; first hoop ≤ 50 from the face |
| **Column C1** | 350 × 350 | 40 | d′ 56 | **8-T16** (1608 mm², p = 1.31 %) |
| Column confining hoops | — | — | — | **T10 hoops + 1 cross-tie each way @ 85 over 500 from every joint face, top and bottom, AND through the joint** |
| Column general ties | — | — | — | T8 @ 150 elsewhere |
| Plinth beam PB | 250 × 400 | 30 | 354 | 3-T12 top + 3-T12 bottom |
| **Footing F1** | 1500 × 1500 × 600 | 50 | 542 | **T12 @ 150 both ways bottom** (754 mm²/m) |
| **Lintel L1** ×11 | 190 × 150 | 30 | — | **2-T10 bottom · 2-T8 top · T6 2L @ 150** |

### 7.5  The six that matter

```
ROOF      T25 @ 150 EF EW  ·  T12 4L @ 250 end 1500 / 2L @ 300 mid      51 %
WALLS     T16 @ 150 EF EW  ·  T12 closed @ 200                          68 %
W6 / W7   T20 @ 150 EF EW  ·  T12 4L @ 200                              69 %
MAT       T16 @ 150 EF EW  ·  T12 @ 250 x 250 grid                      84 %
HH ROOF   T20 @ 150 EF EW  ·  T12 4L @ 175 / 250                        90 %
HH WALLS  T16 @ 150 EF EW  ·  T12 4L @ 250                              59 %
```

---

## 8  Analysis models

Six STAAD.Pro `.std` files, all in `current/staad/`, all validated as input files.

| Model | File | Form | Size |
|---|---|---|---|
| **Underground box — reference** | `Underground_Structure_WITH_LOADS_worked_example (4).STD` | Mid-surface plate model: mat, roof, four perimeter walls, W5, W6, W7 | 1 113 joints · 1 138 plates |
| **Sentry post** | `Sentry_Post_Framed_Seismic.std` | RC frame, IS 1893 seismic, 16 combinations | 12 joints · 16 members |
| **Entry stairwell** | `Entry_Stairwell.std` | Frame, **static only, not blast rated** | 20 joints · 20 members |
| Box — **COARSE** | `Underground_Shelter_Mesh_Coarse.std` | Mesh sensitivity variant | 324 joints · 336 plates |
| Box — **MEDIUM** | `Underground_Shelter_Mesh_Medium.std` | The reference mesh | 1 113 · 1 138 |
| Box — **FINE** | `Underground_Shelter_Mesh_Fine.std` | Exact h/2 refinement | 4 500 joints · 4 552 plates |

**Box model conventions** — metres and kilonewtons; STAAD global **Y is vertical**; **mid-surface
geometry with a 6.700 m Y-offset**, so model Y 0.300 = mat mid-surface = site (−)6.400, and model
Y 4.250 = roof mid-surface = site (−)2.450.

```
Joint numbering, all three box meshes:  n = (k-1).NI.NJ + (i-1).NJ + j
     i = X index, j = Z index, k = Y level  --  a structured grid, reproducible by hand
Supports   1 TO <all mat joints> ELASTIC MAT DIRECT Y SUBGRADE 100000
           plus KFY restated at the four mat corners, because a FIXED BUT line
           REPLACES the ELASTIC MAT entry there and they would otherwise have
           NO vertical restraint at all.  KFY = ks x 0.25 x dx_edge x dz_edge.
Loads      11 primary cases, ascending 1..11 ; 5 combinations 101..105
           EP1 earth+water applied as one uniform pressure per wall row, at that
           row's mid-height:  p = 15.4071 x depth - 10.8198 kPa, depth = 6.700 - Y
```

### 8.1  The mesh sensitivity study

Coarse, Medium and Fine are one structured grid at three densities. **Fine inserts a new grid
line at the exact midpoint of every reference interval** (uniform h/2, so it reproduces the
reference geometry exactly). **Coarse removes alternating reference grid lines, except any line
that defines the outer box, a W5 / W6 / W7 centreline or an opening edge** — those are always
kept. **Net roof area 104.048 m² and total opening area 15.792 m² are identical in all three**,
which is the check that no geometry drifted during re-meshing.

| Model | X spacing | Z spacing | Wall row | Joints | Plates |
|---|---|---|---|---|---|
| **Coarse** | 0.767–1.600 (avg 1.259) | 0.630–1.400 (avg 1.120) | 1.3167 | 324 | 336 |
| **Medium** | 0.525–1.000 (avg 0.713) | 0.525–0.700 (avg 0.622) | 0.6583 | 1 113 | 1 138 |
| **Fine** | 0.263–0.500 (avg 0.357) | 0.263–0.350 (avg 0.311) | 0.3292 | 4 500 | 4 552 |

> **The convergence table is empty, and it must stay empty until a real run fills it.** No
> moment, displacement, shear, reaction or design utilisation exists for any of the three
> models. See §13.

### 8.2  Before editing any `.std`

```
python3 current/staad/Scripts/validate_std.py
```

It reads each file **the way STAAD reads it** — truncated at the declared `INPUT WIDTH`, with
`-` continuations joined — and checks line width, ascending load case numbers, combination
references, element and member topology, planarity, duplicates, orphan joints, thickness and
property coverage, and **whether each self-equilibrating horizontal load case actually
balances.** All six models currently pass with **0 errors**.

**Two rules that are easy to break and silent when broken:**

1. **Every data line must fit `INPUT WIDTH 79`.** STAAD reads 79 columns and **discards the rest
   without complaining** — an 80-column pressure line becomes a *valid* number with its last
   digit gone. Split long element lists on the STAAD `-` continuation character.
2. **Primary load case numbers must ascend.**

---

## 9  Services

### 9.1  HVAC and CBRN filtration

**The envelope is the machine.** 216.96 m³ of gas-tight volume across Bays 1–6, held at
overpressure, with every opening either a blast valve or a blast door.

| Quantity | Value | Basis |
|---|---|---|
| Gas-tight envelope | **67.80 m² / 216.96 m³** | Bays 1–6 × 5.000 × 3.200 `[C]` |
| Clean zone (envelope less the 10.0 m² airlock) | **57.80 m² / 184.96 m³** | `[R]` |
| Filter trains | **2 × 300 m³/h**, HEPA H14 (EN 1822, ≥ 99.995 % at MPPS) + activated carbon | `[C]` |
| FEMA 453 requirement | 57.8 m² → **264.3 m³/h** | 0.25 cfm/ft² `[C]` |
| Envelope leakage | **32.5 m³/h** = 0.15 vol/h | **10.8 % of one train** `[R]` |
| Survival / working ventilation rates | 5 × 9 = **45** / 15 × 9 = **135 m³/h** | `[C]` |
| Time to 1.0 % CO₂, airlock shut | **9.9 h** | `[C]` |
| Airlock purge | **12.8 min** for 5 × 64 m³ at 300 m³/h | `[C]` |
| O₂ store | **15 m³** (2 × 50 L at 150 bar) = **80 h** at 4.5 m³/day | `[C]` |
| Blast valve throats | DN100 at **10.6 m/s**; DN350 at **7.5 m/s** | `[C]` |

> **The airlock purge is a manning constraint, not a plant figure.** 13 minutes per cycle means
> **4–5 persons per hour.** It belongs on the drill card.

> **Maintenance access is the tight dimension, not headroom.** Each train is 1450 wide in a 1560
> clear bay — **110 mm at the sides** — so all access is along the bay, and a HEPA or carbon
> cassette has to come in through **Blast Door 1 (1200 × 2100)** and along Bays 6 and 5.
> **Confirm the cassette dimensions against that route before the trains are ordered.**

**Five blast valves.** BV-4 and BV-5 (DN350) serve the generator in Bay 8. **All five shut at
the shock; BV-4 and BV-5 then reopen so the generator can run during the closed mode**, which is
legitimate because Bay 8 is outside the gas-tight envelope. **That leaves two DN350 bores open
through the post-attack period, and they fail both EMP criteria** — see §9.4.

### 9.2  Drainage

**No pipe anywhere in the cover.** Nothing may break the roof — no manhole, no gully, no
penetration. Water infiltrating the topsoil is intercepted by the granular filter and dispersed
at the berm toe, which is what the 1:50 burster-slab crossfall in §3.5 exists to make true.

| Item | Value |
|---|---|
| **SU-01** clean sump, Bay 5 | invert (−)7.600, base slab (−)8.000 — **400 deep** |
| Sump storage at assumed seepage | **8.4 days** |
| **TK-01** decon effluent tank | 1000 L, Bay 8 — **tanker only, never to the clean sump** |
| **ST-01** septic tank | IS 2470 Pt 1: 24 h detention, 30 L/person/yr sludge, L:B 2–4, vent |
| **SK-01** foul soak pit | **2.200 m dia × 3.500 m effective = 24.19 m²** against 22.50 required, **+7.5 %** |
| SK-02 · SK-03 · SK-04 | surface-water and stairwell soakaways |

> **The soak pit's problem is depth, not arithmetic.** Only **21–43 %** of its required area lies
> above the design water table, and its only permeable horizon is **0.2–0.5 m thick**. The form
> that fits this ground is **shallow and wide**. **SK-01 is deliberately NOT re-sized on that
> reasoning** — the mandatory percolation test (IS 2470 Pt 2 Cl. 4) governs the final size and
> form — and two **dispersion fields DF-1 / DF-2 are reserved** as the fallback, carrying both
> streams down to 26–34 % of the assumed absorption rate.
>
> **The percolation test is mandatory and failure is likely on basalt.** `[A]`

### 9.3  Electrical and power

**Deliberately basic — it stops at board level.** Sources, a load schedule, three boards, the
essential/battery system, one single-line diagram. **No circuit schedule, no cable schedule, no
luminaire schedule exists** `[N]`.

| Quantity | Value |
|---|---|
| Connected load | **6.256 kW · 7.360 kVA** at pf 0.85 |
| **GEN-1** standby set, Bay 8 | **15 kVA** `[C]` |
| Utilisation | **49 %** — the generator is amply sized and **needs no change** |
| Battery, essential services | **Case A, 4 h, 149 Ah at 48 V**, 204 kg, 0.40 m² `[C]` |
| Distribution | **Three boards, one cable entry** through the existing service entry plate |
| EMP treatment at entry | **PCI on power, fibre on signal** |

### 9.4  EMP protection

> **The concrete box is not an EMP shield and never could have been.** At the confirmed **150 mm
> bar spacing**, `SE = 20 log₁₀(λ/2s)` gives **99.99 dB at 10 kHz, falling 20 dB/decade to 0.00
> dB at 1 GHz**, with mesh cutoff **999.31 MHz**. Against the MIL-STD-188-125-1 requirement of
> **80 dB over 10 kHz–1 GHz**, the cage delivers it **only below 99.93 kHz — one decade of the
> five.**
>
> That figure is **an upper bound**: the −10 log₁₀(n) array correction is not applied, the bar
> crossings are **tied, not welded** (and nothing in the project says which), and no concrete
> absorption is credited. **A measured cage will be worse.**

**So the 80 dB boundary is EMP Zone 2 — a welded steel room**, and the project adopts a
**three-zone model** with the rule that **Zone 2 stands alone**: it does not rely on the cage
around it. The Zone 2 enclosure is designed at `[A]` — 2400 × 1600 × 2200 external, in Bay 3 at
X 5820–8220, Y 3700–5300 — **and every dimension of it is `[A]` pending an equipment schedule
that the detailed electrical design has not yet produced.**

**EMP Zone 1 cannot ever be surveyed, and the project does not claim it can.** A buried box
under 2 m of cover has no accessible exterior for an IEEE 299 transmitter. **The cage figures
are a calculation and will stay one.**

**Four things already right, now recorded as EMP measures:** the 150 mm double curtain; the
welded cast-in blast-door frames; the welded Cu/galv strap across every construction joint; and
a single service entry plate rather than scattered penetrations.

### 9.5  Fire and life safety

> **The governing fact: the shelter cannot be ventilated of smoke.** 332.8 m³ at 300 m³/h is
> **0.9 air changes per hour**, and in the closed protective mode it is **zero**.

| Route | What | Travel | Climb | Emerges at |
|---|---|---|---|---|
| **R1** | Main stair, Bay 7 | **14.6 m** | 6.100 m | Headhouse (−)2.000, then 12R to the entry door at grade |
| **R2** | **ESC 1**, Bay 1 | 1.45 m | **6.250 m** | Head +0.150 |
| **R3** | **ESC 2**, Bay 8 | 1.50 m | **6.800 m** | Head +0.700 |

**Blast Doors 1 and 2 are the only two real fire barriers in the shelter.** Bays 1–6 are **one
smoke compartment 20.8 m long** — the four W8 partitions are 110 mm non-structural with permanent
900 gaps and no doors. **W5 is designated fire and gas-tight and has no door** `[N]`, and R1 has
to cross it. **ESC 2 shares Bay 8 with the generator.** There is **no rule anywhere for a fire
during the closed protective mode** `[N]`, and **no ladder, rung or fall-arrest in either escape
shaft** `[N]`.

### 9.6  Finishes and concealment

Room finish, wet-area and stair-finish schedules cover every space; **no finish product is named
anywhere** `[N]` — the schedules specify performance and leave selection open.

> **The shelter is concealed. The installation is not.** Above finished grade there stand: the
> **sentry post at +7.000**, the **headhouse at +0.900 with no earth cover**, the **entry
> stairwell head at +2.450**, and a **gooseneck at +1.500**. The **300 mm turf is the
> concealment layer**, re-laid from the site's own stockpile. **No net, paint or screen is
> specified anywhere in the project, and none is invented.**

---

## 10  Site and external works

**Site orientation: project +X = EAST, project +Y = NORTH.** `[A]` The entry faces the campus,
drainage runs downgradient, and the fresh-air intake and exhaust end up at opposite ends of the
box.

**External works reserve: 18.0 × 10.5 m at X 33000–51000, Y 6500–17500** — 10 m clear of the
excavation, downgradient, using 42.5 m of the 50 m available.

| Item | Position | Item | Position |
|---|---|---|---|
| **ST-01** septic tank | (36750, 16000) | **SK-02** | (35000, 8500) |
| **SK-01** foul soak pit | (44000, 16000) | **SK-03** | (41400, 8500) |
| **IC-01** | (7500, 9800) | **SK-04** | (47800, 8500) |
| **IC-02** | (40200, 16000) | | |

**Four of five external pipe runs are fixed** — PD-16 **5.40 m**, PD-06 **27.00 m**,
PD-11 **32.35 m**, PD-13 **29.60 m**. **PD-14 cannot be routed** `[U]`. **Two of three IS 2470
offsets are demonstrated** (5.40 m to the tank, 10.97 m to any building); **the ≥ 15 m well
offset cannot be — no well position exists** `[N]`. **28 of 28 clearance checks pass.**

> **There is a site LAYOUT. There is no site SURVEY.** Still missing: a boundary, a benchmark and
> spot levels, the well, the perimeter fence distance, existing services, and a wind rose. Every
> one of those is a survey output — **and none of them moves anything the layout has fixed**,
> because the layout is dimensioned from confirmed structural geometry and every offset is
> relative.

---

## 11  Drawings

**80 DXF · 75 A1 · 4 A4 · 1 A0**, AutoCAD 2010 ASCII, all carrying a border and title block.
Index: `DRAWING QAQC/DRAWING_INDEX.md`, generated from the files themselves.

| Series | Package | Count |
|---|---|---|
| **A-101…A-301** + **S-06** | Architectural / general, and the services plan | 11 |
| **R-001…R-805** | Structural reinforcement | 30 |
| **D-001…D-305** (+2 handout) | Drainage | 13 |
| **M-001…M-203** (+2 handout) | HVAC | 8 |
| **EM-001…EM-302** | EMP protection | 6 |
| **SG-001…SG-202** | Site selection, geotechnical and site layout | 5 |
| **A-601 / 611 / 612** | Schedule of finishes | 3 |
| **F-101 / F-102** | Fire and life safety escape plans | 2 |
| **C-101** | Above-ground signature elevation | 1 |
| **E-001** | Electrical single line diagram | 1 |

**QA state: 74 PASS · 6 REVIEW REQUIRED · 2 text-on-text overlaps** (both on A-204) **· 10
annotations still crossing line work · 0 entities outside a sheet border.** Every REVIEW item is
a single annotation crossing a dimension or a wall line in a dense zone, each named individually
in `DRAWING QAQC/QAQC_REPORT.md` §5.1.

> **A-301 is A0, not A1, and that is a measurement statement rather than a preference:** at 1:50
> the front elevation is 880 mm wide against an A1 drawing area of 821 mm. Splitting it would
> break a continuous 44 m elevation.

> **Sheets S-01…S-05, S-07 and S-08 are NOT in this repository and cannot be regenerated here.**
> The generator toolchain that produced them (`proj.py`, `dxflib.py`, `d01_wall.py`…
> `d08_sentryslab.py`, `validate.py`, `render.py`) is absent. **S-06 is present.** **Do not
> invent them, and do not hand-edit a generated DXF** — edit the generator and re-run it.
> The sentry post's beams, columns and footings are **not yet drawn**; that sheet would be
> **S-09**.

---

## 12  Works management

| | |
|---|---|
| Programme | **224 working days**, 02-11-2026 → 26-07-2027, **six-day week**, 130 activities |
| Cost | **₹2,97,90,913** — **a LOWER BOUND.** The generator is deliberately unpriced, because no rate for it exists and none was invented |
| Deliverables | WBS · BOQ · Resource Plan · Procurement Plan · QA/QC Plan · Safety & Risk Register · Codes & References · a 44-page handout |
| Consistency checks | **65 of 65 passing** |

> **The programme stops dewatering on 11-05-27 but does not backfill until 20-07-27.** That spans
> the 2027 monsoon **at flotation FoS 1.22** — stage 3 in §6.3, the stage that floats if the
> excavation floods to ground level. **This is an open item, and it is the one on this list that
> could sink the structure.**

> **The confirmatory site investigation's monsoon monitoring window runs 12 Nov – 4 Dec, which is
> not in the monsoon.** The one measurement that would settle the project's most important
> assumption is scheduled when it cannot be taken.

---

## 13  What this design does NOT demonstrate

Stated here rather than left for a reviewer to find.

1. **No STAAD.Pro analysis has been run in this environment.** All six models are built,
   reconciled and validated **as input files**. **No moment, displacement, shear, reaction or
   design utilisation exists from any run performed here.** Editing and verifying a `.std` is
   **not** running an analysis and is never reported as one.
2. **A static run gives DEMAND, never proof of blast resistance.** The non-linear SDOF
   support-rotation check (IS 4991 Fig. 6, Biggs) is **Phase 3** and has not been done.
3. **Flotation cannot be read off the model.** The `ELASTIC MAT` springs take tension. It is a
   hand check on the real 136.40 m² underside — §6.3.
4. **The mesh convergence conclusion does not exist.** The table is a template with the result
   columns blank, and it must not be filled with reconstructed numbers.
5. **The second subgrade bound (k<sub>s</sub> = 500 000) has not been run.** The mat moments are
   sensitive to it and the master requires **both** bounds.
6. **EMP Zone 1 has not been and cannot be surveyed**, and the cage figure is an upper bound on
   an untested assumption about tied-versus-welded crossings.
7. **No blast door, blast valve or EMP vendor data exists** `[N]`. Ratings are specified;
   products are not selected.
8. Also not started: shock propagation down the entry shaft, transient soil–structure
   interaction, and blast-door vendor testing.

---

## 14  Assumptions to confirm before construction

| # | Assumption | Impact if wrong | Confirm by |
|---|---|---|---|
| **A1** | Rockhead 1.5–2.0 m, competent below | Founding level, excavation cost | Boreholes **on this plot** |
| **A2** | **GWT (−)2.000** | **Uplift, flotation, waterproofing class, wall design** | **Standpipe piezometer read through a FULL monsoon** |
| **A3** | SBC 3240 kPa | Mat and footing sizing (both ≤ 21 % utilised) | Plate load / core testing at the founding horizon |
| **A4** | **k<sub>s</sub> 100 000–500 000 kN/m³** | **Mat moments — sensitive. RUN BOTH BOUNDS** | Plate load test |
| **A5** | K₀ = 0.50, γ 20/21 | Wall lateral load (< 1 % — walls are blast-governed) | Site investigation |
| **A6** | K<sub>a</sub> = 1.0 saturated used; K<sub>a</sub> ≈ 0.5 dry berm **not relied on** | Headhouse wall load — deliberately off the critical path | Would permit a reduction if measured |
| **A7** | Soak-pit absorption 20 L/m²/day | **The soak pit will not work if lower — likely on basalt** | **Percolation test, IS 2470 Pt 2 Cl. 4 — MANDATORY** |
| **A8** | Structural seepage 0.5 L/m²/day | Sump storage (currently 8.4 days) | Packer permeability tests |
| **A9** | Sentry infill not separated → R = 3.0 | V<sub>b</sub> × 1.67 if separated | Architect's decision |
| **A10** | k1 = 1.08, 100-year wind life | Wind does not govern | Client brief |
| **A11** | b<sub>eff</sub> = 2.5 m for the HW3 line load | HW3 strip check (26 % / 41 %) | Refined FE if ever critical |
| **A12** | Trapezoid factor 0.7946 for both BM and FEM | ≈ 2 % on the B2 support moment | Frame model |
| **A13** | Sentry frame has no member releases | Frame moment distribution | The `.std` |
| **A14** | Poisson's ratio 0.20 | Plate behaviour, minor | Standard |

> **Not one of these is closed by anything currently in the project.** The available sub-soil
> investigation gives four of them a **provenance and a quantified margin — never a
> confirmation**, for the reason in §3.2: it reached about 1.5 m and this structure founds at
> (−)6.800.

---

## 15  Open items

**Thirty-three**, each a single position the project holds — or, in a few, one it does not hold
at all — that needs something from outside it. The register is master **K.1b**; the shape of it:

| Group | What is outstanding |
|---|---|
| **Threat** | Is a direct hit a requirement? · What is the design basis yield? — **military / client sign-off** |
| **Structural** | The sentry seismic re-check after the infill change (direction certain, favourable) · the ballistic requirement the brick infill no longer meets · the 4.162 kN/m parapet load, not independently reproducible |
| **Escape** | **How either escape shaft is climbed** — 6.250 m and 6.800 m with no ladder, rung or fall-arrest. **This needs a design, not a ruling** |
| **EMP** | Every Zone 2 dimension is `[A]` pending an equipment schedule · **is Bay 8 inside the EMP boundary?** — no EMP boundary has ever been drawn · no communications design of any kind · no escape-shaft head hatch and no blast-door RF data · **no pipe material is specified anywhere in the project** |
| **Electrical** | Generator fuel (≈ 210 L for 96 h derived, nothing specified) · incoming mains capacity, which **blocks any fault-level study** · no circuit / cable / luminaire schedule · **no cooling plant exists anywhere in the project** · the CO₂ scrubber's air movement is in no schedule |
| **Geotechnical** | The data is **off-site** and reached 1.5 m against a formation at (−)6.800 · no plate load test · no percolation test · **the monsoon monitoring window is not in the monsoon** · the entry stairwell raft and the concealment turf sit in very-high-swelling clay with no specification |
| **Site** | No well position, so the ≥ 15 m offset cannot be demonstrated · the perimeter fence distance has never been dimensioned · the fresh-air intake **SH-1 has no plan position** · SH-2 has **no recorded head level** · there is no wind rose · **the programme stops dewatering before backfill** |
| **Drawings / data** | Two different **assumed** sentry-post positions are held in the project · W5's gas-tight door D-05 does not exist · service-entry plate size · duct penetration schedule · vision panel specification · finish product selections |

> **None of these may be silently resolved.** An `[ASSUMED]`, `[UNRESOLVED]` or `[NOT AVAILABLE]`
> item stays what it is until someone supplies the information. **Do not convert a tag. Ask.**

---

## 16  Reproducing the project from this repository

Everything below runs with Python 3 alone, except where `ezdxf` is noted.

```
underground-shelter-project/
├── CLAUDE.md                          operating rules for this repository
├── CONSOLIDATED_PROJECT_REPORT.md     this document
├── master/
│   ├── MASTER_PROJECT_STATE.md        THE AUTHORITY -- design, revisions, conflicts
│   ├── MASTER_PROJECT_STATE.pdf       a STALE render; read the .md
│   └── QUICK_STATE.md                 orientation digest, not an authority
├── current/
│   ├── cad/       10 Rev F architectural DXF + S-06, and Scripts/
│   └── staad/     6 .std + the mesh study + Scripts/validate_std.py
├── Structural CAD/        30 reinforcement drawings, BBS, calcs, compliance matrices
├── Drainage/  HVAC/  Electrical/  EMP Protection/
├── Fire and Life Safety/  Schedule of Finishes/  Site and Concealment/
├── Site Selection and Geotechnical/
├── WORKS MANAGEMENT/      WBS, BOQ, programme, cost, QA/QC, risk
├── DRAWING QAQC/          package-wide drawing index and QA tooling
└── Revit/                 6 Dynamo scripts that build the structural envelope
```

**Rebuild each package from its own generators:**

| Package | Command |
|---|---|
| Structural CAD | `python3 "Structural CAD/Scripts/build_all.py"` |
| Drainage | `python3 Drainage/Scripts/dr_build_all.py` |
| HVAC | `python3 HVAC/Scripts/hv_build_all.py` |
| Electrical | `python3 Electrical/Scripts/el_build_all.py` |
| EMP protection | `python3 "EMP Protection/Scripts/em_build_all.py"` |
| Fire and life safety | `python3 "Fire and Life Safety/Scripts/fs_build_all.py"` |
| Schedule of finishes | `python3 "Schedule of Finishes/Scripts/fn_build_all.py"` |
| Site and concealment | `python3 "Site and Concealment/Scripts/cm_build_all.py"` |
| Site selection and geotechnical | `python3 "Site Selection and Geotechnical/Scripts/sg_build_all.py"` |
| Works management | `python3 "WORKS MANAGEMENT/Scripts/wm_build_all.py"` |

**Validate:**

| What | Command |
|---|---|
| STAAD input files | `python3 current/staad/Scripts/validate_std.py` |
| Services / finishes DXF | `python3 Drainage/Scripts/mep_validate.py <dir>` *(ezdxf)* |
| Reinforcement DXF | `python3 "Structural CAD/Scripts/validate_dxf.py"` *(ezdxf)* |
| Whole drawing package | `python3 "DRAWING QAQC/Scripts/qa_report_data.py" && python3 "DRAWING QAQC/Scripts/make_index.py"` *(ezdxf)* |

> **A new drawing package must register itself with the QA tool** — add its `DXF/` prefix to
> `DISCIPLINE` in `qa_report_data.py` and its name to `ORDER` in `make_index.py`, then re-run
> both. A package that skips this is **invisible** to the index, and the index will go on
> reporting a total that quietly excludes it.

**The shared sheet library is subclassed, never edited.** `Drainage/Scripts/mep_dxf.py` is the
base; EMP, Electrical and Site/Geotech subclass it and use its hooks. That is what keeps every
earlier package regenerating byte-identically when a later one is added.

**Not reproducible here, and not to be faked:**

* **Sheets S-01…S-05, S-07, S-08** — the generator toolchain is absent (§11).
* **The Revit model** — six Dynamo Python scripts exist and are rerun-safe, but **no `.rvt`
  exists and Revit is not executable in this environment.**
* **`MASTER_PROJECT_STATE.pdf`** — a stale render with no generator in the workspace.
* **Any STAAD result whatsoever** — STAAD.Pro is not installed here (§13).
* The **Phase 1 Rev D design report**, `SK02_Underground_Plan.png` and the 19 STAAD screen
  captures are **not in this repository.** Every value they support is already transcribed into
  this report and into the master, with its evidence tag.

---

## 17  The rules this project is held to

These are not style preferences. Each of them exists because breaking it produced a defect.

1. **`master/MASTER_PROJECT_STATE.md` governs.** If any file disagrees with it, the master is
   right and the file is wrong — say so rather than quietly adopting either.
2. **Never guess, and never silently resolve an `[ASSUMED]`, `[UNRESOLVED]` or `[NOT AVAILABLE]`
   item.** Ask. Do not convert a tag, and do not delete one.
3. **Inspect native files before modifying them.** Parse the DXF, read the `.std`. Never edit
   from memory or from a summary.
4. **Editing and verifying a `.std` is not running an analysis**, and must never be reported as
   one.
5. **To change a drawing, edit its generator and re-run it** — the DXF is a build artefact. The
   ten Rev F architectural drawings are the exception: they are source and may be edited
   directly.
6. **No drawing shows an arrangement that differs from a calculation.** If you change steel,
   change the drawing in the same turn.
7. **Cross-check in this order:** geometry → materials → loads → structural model → analysis →
   design calculations → reinforcement → drawings → revision number. **A change that stops at
   "reinforcement" and never reaches "drawings" is not finished.**
8. **Every significant change gets a revision identifier and a record**, and **no previous
   revision is overwritten** — corrections sit beside the record they correct.
9. **Say the weakness before the reviewer finds it.** That principle produced the two structural
   findings, the headhouse wall upgrade, the corrected yield-line coefficient and the flotation
   table — and it is the reason this package is defensible.

**And four design intentions that must survive any future change:**

* **The protective boundary is Blast Doors 1 and 2 at (−)6.100.** Everything above them is
  expendable, and that is deliberate.
* **The roof spans one way across the 5 000 mm width.** Lengthening the box is free; widening it
  is expensive. **Do not widen it.**
* **No movement joints anywhere inside the protective envelope.** One would be a guaranteed
  blast, gas and EMP discontinuity.
* **IS 4991 Cl. 10.3.1.1 — no dynamic increase on shear.**

### The frozen geometry

> **MAIN STAIRCASE — 24 risers, 170.8333 mm riser, 280 mm tread, 3 flights × 8, total rise
> 4100 mm.** The landing levels, the 1200 flight widths, the 200 well and the 2533 headroom go
> with it. **None of it changes unless it is explicitly asked for in a new request.**

---

*Underground CBRN-hardened blast-resistant protective structure with sentry post, Pune.
Architectural Rev F · design report Rev D · structural Phase 2 Rev A. Consolidated from the
complete project record, 11 September 2026. Every value in this document is tagged CONFIRMED,
RECONSTRUCTED, ASSUMED, UNRESOLVED or NOT AVAILABLE, or is stated in a section whose tag applies
throughout. **Nothing in this document was invented.***
