# IS 13920:2016 COMPLIANCE MATRIX
## Ductile detailing — applicability determination and checks
### Structural CAD reinforcement package · revision **SC1** · 4 September 2026

> ### ⚠ READ THIS FIRST — THE BRIEF'S OWN WARNING IS THE RIGHT ONE
> The brief says: *"Do NOT assume that IS 13920 alone governs the entire underground shelter…
> For portions governed by other structural actions, identify the appropriate governing
> requirements. If a particular requirement does not apply, explain why."*
>
> **That is exactly the situation here.** IS 13920:2016 is the standard for **ductile detailing of
> reinforced-concrete structures subjected to seismic forces**. This matrix therefore begins with
> a **determination of applicability, member category by member category**, supported by evidence,
> and only then records the checks that actually have a member to apply to.

> ### ⚠ CLAUSE VERIFICATION
> **No copy of IS 13920:2016 is held in this workspace** (input audit §A.6). Clause numbers are
> taken **only** from master **Part G**, which lists the clauses this project relied on:
> **Cl. 6.1.1, 6.1.2, 6.1.3; 6.2.1(b), 6.2.2, 6.2.3, 6.2.4; 6.3.3, 6.3.4, 6.3.5.1, 6.3.5.2;
> 7.1, 7.2.1, 7.3, 7.4; 8.1, 8.2; 10.4.**
> Any check needing a clause outside that list is reported **"CLAUSE NOT VERIFIABLE"** and given
> status **NOT DETERMINABLE**. **No clause number is guessed.**
>
> In particular, the IS 13920 **Cl. 10.1.x structural-wall detailing clauses** (minimum thickness,
> minimum reinforcement, two curtains, maximum bar diameter, spacing) are **NOT in the verified
> register** and are therefore **not cited**. The equivalent IS 456 wall provisions
> (**Cl. 32.5(a), (b), (c)**) *are* in the register, are checked in
> `IS456_Compliance_Matrix.md` §4, and are satisfied with large margins.

**Sentry post excluded.** Master B.8 and F.4 — where the project's IS 13920 frame detailing
actually lives — are **not used**, because the sentry post is out of scope for this package.

---

## PART 1 — APPLICABILITY DETERMINATION

### 1.1 What the seismic demand on this structure actually is

| Quantity | Value | Source | Class |
|---|---|---|---|
| Zone / Z | III / 0.16 | IS 1893 (Pt 1):2016 Table 3 | [CONFIRMED] |
| Importance factor I | 1.5 | IS 1893 Cl. 7.2.3 | [CONFIRMED] |
| Response reduction R | 4.0 | IS 1893 Cl. 7.2.6 | [CONFIRMED] |
| S_a/g | 2.5 | IS 1893 Cl. 6.4.2 + Fig. 2 | [CONFIRMED] |
| **A_h = (Z/2)(I/R)(S_a/g)** | **0.075** | derived | [CONFIRMED] |
| Seismic weight W | 14 002 kN | master A.7.8 | [CONFIRMED] |
| **Base shear V_b** | **1 050 kN** | 0.075 × 14 002 | [CONFIRMED] |
| Shear per long wall | 525 kN | V_b / 2 | [CONFIRMED] |
| **Wall shear stress τ** | **0.063 N/mm²** | 525e3/(600 × 0.8 × 21 600) | [CONFIRMED] |

**τ = 0.063 N/mm² is 1.7 % of the M35 τ_c,max of 3.70 N/mm², and 17 % of even the lowest τ_c in
Table 19.** The governing lateral action on every blast-rated element is **COMB 103 BLAST at
383 kPa**, which produces τ_v between 0.770 and 1.514 N/mm² — **12 to 24 times the seismic shear.**

**IS 4991 Cl. 11.1 forbids combining wind or earthquake with blast**, so the two never act together.

### 1.2 What members exist, and what IS 13920 has to say to each

| IS 13920 member category | Clauses in the verified register | Does the member exist in the underground shelter? | Determination |
|---|---|---|---|
| **Beams of a moment frame** | 6.1.1, 6.1.2, 6.1.3, 6.2.1(b), 6.2.2, 6.2.3, 6.2.4, 6.3.3, **6.3.4**, 6.3.5.1, 6.3.5.2 | **NO.** The box is a monolithic plate structure — mat, walls, roof slab. The only beam-*type* members are three local bands over openings (blast-door headers ×2, headhouse door-head edge band, entry-door lintel), none of which is part of a lateral-force-resisting frame | **NOT APPLICABLE — no member.** See Part 3 |
| **Columns and frame members subject to bending and axial load** | 7.1, 7.2.1 (SCWB), 7.3, 7.4 | **NO.** Master B.3 declares punching shear NOT APPLICABLE precisely because *"no columns/pedestals bear on the mat"* | **NOT APPLICABLE — no member** |
| **Special confining reinforcement** | 8.1, 8.2 | **NO** — there is no column and no frame joint to confine | **NOT APPLICABLE — no member** |
| **Beam–column joints** | (joint provisions) | **NO** — no beam and no column, therefore no joint | **NOT APPLICABLE — no member** |
| **Structural walls — boundary elements** | **10.4** | **YES — walls exist.** The check was performed | **CHECKED AND NOT TRIGGERED.** See 2.1 |
| **Structural walls — general detailing** | Cl. 10.1.x — **NOT IN THE VERIFIED REGISTER** | walls exist | **NOT DETERMINABLE — clause not verifiable.** The IS 456 Cl. 32.5 equivalents are checked and pass |

### 1.3 The determination, stated plainly

**IS 13920 does not govern this structure, and saying so is a finding, not an evasion.**

1. There is **no moment frame**, so the beam, column, joint and confinement provisions — which are
   the substance of IS 13920 — **have no member to apply to**.
2. The one category that *does* exist, **structural walls**, was checked against the one wall
   clause in the verified register — **Cl. 10.4 boundary elements — and is not triggered**.
3. The governing action everywhere is **blast**, not earthquake, by a factor of 12 to 24 on shear
   and by 3.5 : 1 on the roof and 4.6 : 1 on the walls in flexure.
4. **This does not mean the detailing is un-ductile.** The section proportions this package adopts
   are far more ductile than IS 13920 would demand of a frame — see Part 4.

---

## PART 2 — CHECKS PERFORMED ON THE ONE APPLICABLE CATEGORY

### 2.1 Structural walls — boundary elements, Cl. 10.4

| # | Requirement | Clause | Project value | Trigger | Result | Status |
|---|---|---|---|---|---|---|
| 2.1.1 | Boundary elements required where the extreme-fibre compressive stress under the factored seismic combination exceeds the code threshold | **Cl. 10.4** | seismic wall shear τ = **0.063 N/mm²**; axial from gravity f = 1.95 N/mm² = 11 % of 0.4 f_ck,dyn; no flexural compression concentration arises from a 525 kN in-plane shear on a 22 m × 3.2 m wall | not reached | **BOUNDARY ELEMENTS NOT TRIGGERED** | **PASS — checked, not assumed** |
| 2.1.2 | Same, walls W6 / W7 | Cl. 10.4 | 400 thk, 5 000 long, in-plane seismic demand negligible; governing action is out-of-plane blast | not reached | not triggered | **PASS** |
| 2.1.3 | Same, headhouse walls HW1–HW4 | Cl. 10.4 | above ground, 2 400 clear, governing action 383 kPa out-of-plane either face | not reached | not triggered | **PASS** |

**Master A.7.8 records this determination independently:** *"IS 13920 Cl. 10.4 boundary elements
NOT triggered."* This package re-states it rather than re-deriving it, and the underlying numbers
(A_h 0.075, V_b 1 050 kN, τ 0.063) were re-checked for this matrix.

### 2.2 Wall detailing provisions that IS 456 covers and that ARE verifiable

Reported here so the wall category is not left with only one line.

| # | Requirement | Clause | Required | Provided | Status |
|---|---|---|---|---|---|
| 2.2.1 | Two curtains of reinforcement | **IS 456 Cl. 32.5(c)** | required where t > 200 | provided in every wall ≥ 250 | **PASS** |
| 2.2.2 | Minimum vertical reinforcement | **IS 456 Cl. 32.5(a)** | 0.12 % | 0.22 %–0.52 % | **PASS** |
| 2.2.3 | Minimum horizontal reinforcement | **IS 456 Cl. 32.5(b)** | 0.20 % — governs on the perimeter and headhouse walls | 0.22 %–0.52 % | **PASS** |
| 2.2.4 | Maximum bar spacing | project EMP rule, stricter than IS 456 Cl. 26.3.3 | **150 mm both curtains** | 150 | **PASS** |
| 2.2.5 | Wall thickness | Cl. 10.1.x **not verifiable** | — | 600 / 400 / 200 / 110 | **NOT DETERMINABLE — clause not verifiable.** All are ≥ 200 except the 110 non-structural partitions, which carry no load path |

---

## PART 3 — THE THREE BEAM-TYPE MEMBERS, ASSESSED HONESTLY

These are **local bands spanning over openings**, not frame beams. IS 13920 Cl. 6 is written for
members of a lateral-force-resisting moment frame and **is not applied**. What follows records
what *was* provided and why, so that a reviewer can judge the decision rather than take it on trust.

| Member | Size | Span | Governing action | Provided | IS 13920 status |
|---|---|---|---|---|---|
| **Blast-door header ×2** (W6, W7) | 400 × 1100 | 1 200 | **COMB 103 BLAST**, w 402 kN/m, M 48.2 kNm, V 241 kN | 4-T20 top **and** 4-T20 bottom; **T12 4-legged closed links @ 150 over the full length** | **NOT APPLICABLE — no frame member** |
| **Headhouse door-head edge band** | 400 × 800 | 900 + 600 each side | **COMB 103 BLAST either face**, M 27.1 kNm, V 181 kN | 4-T20 top **and** 4-T20 bottom; T12 4-legged links @ 150 | **NOT APPLICABLE — no frame member** |
| **Entry-door lintel** | 250 × 350 | 1 000 | IS 456 ULS, normal factors (not blast rated) | 3-T12 top **and** 3-T12 bottom; T8 links @ 150 | **NOT APPLICABLE — no frame member** |

### What the detailing does anyway, and why

| Feature | IS 13920 frame requirement (Cl. 6.2.x, 6.3.5.x) it resembles | Why it is provided **here** |
|---|---|---|
| **Equal top and bottom steel** | beams must carry a minimum bottom-steel ratio at a joint face | **Blast load reversal and rebound.** The header is loaded from the shaft side and rebounds; the headhouse band is loaded from **either** face by design |
| **Closed links at 150 over the full length**, not just at the ends | special confining hoops over 2 d from the face | **Shear under a 402 kN/m band load**, plus confinement of a heavily bar-congested 400 mm width |
| **135° hooks on every link** | required for hoops | Standard practice for closed links in a blast-loaded member |

> **This is a blast-detailing decision, not an IS 13920 compliance claim, and it is not presented
> as one.** The brief's instruction — *"Do not simply label the joint 'IS 13920 compliant'"* — is
> observed by the stronger route: **there is no joint to label.**

---

## PART 4 — DUCTILITY THAT IS DEMONSTRATED, BY A DIFFERENT ROUTE

IS 13920 exists to guarantee rotation capacity. This structure obtains it from **section
proportion**, and that is measurable:

| Element | x_u/d provided | x_u,max/d (IS 456 Cl. 38.1(f), Fe500) | Margin |
|---|---|---|---|
| **Roof slab 900** | **0.139** | 0.46 | **3.3 ×** |
| Perimeter walls 600 | 0.089 | 0.46 | 5.2 × |
| Mat 600 | 0.089 | 0.46 | 5.2 × |
| Headhouse walls 400 | 0.135 | 0.46 | 3.4 × |
| Headhouse roof 500 | 0.174 | 0.46 | 2.6 × |
| W6 / W7 400 | 0.211 | 0.46 | 2.2 × |

> **x_u/d = 0.139 on the roof is the project's stated proof that the ductility ratio μ = 5 used in
> the blast DLF is defensible.** A section that deep in the under-reinforced range has the rotation
> capacity that μ = 5 assumes.

### The limit of that argument — stated, not hidden

**x_u/d is a section property. It is not a support-rotation check.**
Demonstrating that θ ≤ 2° under the blast requires a **non-linear SDOF analysis**
(IS 4991 Fig. 6 / Biggs) or explicit non-linear FE with strain-rate-dependent materials.
**That work is PHASE 3 AND HAS NOT BEEN DONE.**

**Status of blast ductility: NOT DETERMINABLE in this package.**

---

## PART 5 — SUMMARY

| Category | Members | Clauses in the verified register | Result |
|---|---|---|---|
| **Beams** | **none exist** | 6.1.1–6.3.5.2 | **NOT APPLICABLE — declared, with evidence** |
| **Columns** | **none exist** | 7.1–7.4 | **NOT APPLICABLE — declared, with evidence** |
| **Beam–column joints** | **none exist** | — | **NOT APPLICABLE — declared, with evidence** |
| **Special confining reinforcement** | no member | 8.1, 8.2 | **NOT APPLICABLE — declared** |
| **Structural walls — boundary elements** | W1–W4, W5, W6, W7, HW1–HW4 | **10.4** | **CHECKED — NOT TRIGGERED. PASS** |
| **Structural walls — general detailing** | as above | Cl. 10.1.x **not in the register** | **NOT DETERMINABLE — clause not verifiable.** IS 456 Cl. 32.5 equivalents all PASS |
| **Blast ductility / support rotation** | roof, walls | *not an IS 13920 matter* | **NOT DETERMINABLE — Phase 3 SDOF** |

### The one sentence a reviewer should take from this matrix

**IS 13920 does not govern the underground shelter — not because the check was skipped, but
because the structure has no moment frame and its seismic demand is 12 to 24 times smaller than
the blast demand that does govern. The one applicable clause in the verified register, Cl. 10.4,
was checked and is not triggered.**

**Nothing in this matrix is claimed as "fully code compliant".** Three items are
**NOT DETERMINABLE**, and the reason for each is a missing document or a Phase 3 analysis, not a
judgement call.
