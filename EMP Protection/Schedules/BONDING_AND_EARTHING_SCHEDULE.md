# BONDING AND EARTHING SCHEDULE — EMP

**Underground CBRN-hardened protective structure — Pune** · GEOMETRY REV F + M1
EMP Protection package revision **EM1** · 10.09.2026 · **FOR REVIEW - NOT FOR CONSTRUCTION**
**Sentry post excluded.** Evidence class: `[C]` confirmed · `[R]` reconstructed · `[D]` derived by this package · `[A]` assumed by this package · `[U]` unresolved · `[N]` not available — DATA REQUIRED

> **`EMP Zone` is not `zone`.** Drainage and finishes already use zones 1/2/3 for **cleanliness**. The EMP zones here are a different scheme on the same building; the `EMP` prefix is mandatory.

**This is where EMP design actually lives.** An EMP shield works by being **equipotential**, and equipotential is decided by **bonding inductance**, not by earth resistance. `L = 2×10⁻⁷·l·[ln(2l/(w+t)) + 0.5 + 0.2235(w+t)/l]` H

| STRAP | LENGTH mm | SECTION mm | w : l | L nH | X @1 MHz Ω | X @10 MHz Ω | X @100 MHz Ω | RULING |
|---|---|---|---|---|---|---|---|---|
| **Long Round-The-Corner Strap** | 600 | 25 × 3 | 0.04 : 1 | 512.2 | 3.22 | 32.2 | 322 | **REJECTED — 322 Ω at 100 MHz is not a bond** |
| **House Rule - Short Wide Strap** | 100 | 50 × 3 | 0.50 : 1 | 38.9 | 0.24 | 2.4 | 24 | **ADOPTED — the house rule** |
| **House Rule - Limit Case** | 150 | 50 × 3 | 0.33 : 1 | 69.4 | 0.44 | 4.4 | 44 | **REJECTED — 322 Ω at 100 MHz is not a bond** |

### The bonding rules `[D]`

1. **Every bond ≤ 100 mm long.**
2. **Width : length at least 5 : 1.**
3. **Flat strap only.** Never a round wire, never a pigtail, never *“loop it round to the nearest stud.”*
4. **Clean bare metal both ends**, protected after making off.
5. **The shield bonds to the structure at ONE place.** A second bond is a loop, and a loop is an antenna.

### Earthing — and why 5 Ω is the wrong target to chase

| Electrode | ρ = 1 000 Ω·m | ρ = 10 000 Ω·m | Class |
|---|---|---|---|
| One 3 m × 16 mm rod | **335 Ω** | **3349 Ω** | `[D]` |
| Rods needed for 5 Ω, *no interaction* | **67** | **670** | `[D]` |
| **The structure itself** (136.4 m², r_eq 6.589 m, ρ/4r) | **38 Ω** | **379 Ω** | `[D]` |

**≤ 5 Ω is not achievable with rods in Deccan basalt** (1 000 – 10 000 Ω·m, master K.3, which already says *“test earth resistance early”*). The **mat and its cage are already a large concrete-encased electrode**, an order of magnitude better than a rod and costing nothing. **Bond to the structure; do not chase rods.** `[D]`

**And ≤ 5 Ω is not an EMP number.** It is a power-safety and lightning requirement from IS 3043 / IEEE 142. It is real and it still applies. **It is not what makes the shield work.**

**The project already does this correctly in two places, without saying why:** master A.5 requires the blast door frames to be *cast in and **welded to the cage***, and B.7.2 requires it even for the **non-blast-rated** headhouse door. Those are EMP bonds. `[C]`
