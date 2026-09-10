# SHIELDING EFFECTIVENESS — THE REINFORCEMENT CAGE

**Underground CBRN-hardened protective structure — Pune** · GEOMETRY REV F + M1
EMP Protection package revision **EM1** · 10.09.2026 · **FOR REVIEW - NOT FOR CONSTRUCTION**
**Sentry post excluded.** Evidence class: `[C]` confirmed · `[R]` reconstructed · `[D]` derived by this package · `[A]` assumed by this package · `[U]` unresolved · `[N]` not available — DATA REQUIRED

> **`EMP Zone` is not `zone`.** Drainage and finishes already use zones 1/2/3 for **cleanliness**. The EMP zones here are a different scheme on the same building; the `EMP` prefix is mandatory.

Square aperture array at the confirmed bar spacing **s = 150 mm, both curtains, both ways** (master A.5 — *“an EMP requirement, stricter than IS 456 Cl. 26.3.3”*).

`SE = 20 log₁₀(λ / 2s)`, zero once `λ ≤ 2s`

| FREQUENCY | WAVELENGTH | SE dB | MARGIN dB | VERDICT | REQUIRED dB |
|---|---|---|---|---|---|
| 10.000 kHz | 29979.246 m | 99.99 | +19.99 | **PASS** | 80 |
| 30.000 kHz | 9993.082 m | 90.45 | +10.45 | **PASS** | 80 |
| 100.000 kHz | 2997.925 m | 79.99 | -0.01 | **FAIL** | 80 |
| 300.000 kHz | 999.308 m | 70.45 | -9.55 | **FAIL** | 80 |
| 1.000 MHz | 299.792 m | 59.99 | -20.01 | **FAIL** | 80 |
| 3.000 MHz | 99.931 m | 50.45 | -29.55 | **FAIL** | 80 |
| 10.000 MHz | 29.979 m | 39.99 | -40.01 | **FAIL** | 80 |
| 30.000 MHz | 9.993 m | 30.45 | -49.55 | **FAIL** | 80 |
| 100.000 MHz | 2.998 m | 19.99 | -60.01 | **FAIL** | 80 |
| 300.000 MHz | 999.3 mm | 10.45 | -69.55 | **FAIL** | 80 |
| 500.000 MHz | 599.6 mm | 6.01 | -73.99 | **FAIL** | 80 |
| 1.000 GHz | 299.8 mm | 0.00 | -80.00 | **FAIL** | 80 |

### The check that matters

Master **K.3** records, as a confirmed item: *“EMP rebar cage **0 dB @ 1 GHz**”*. This table reaches **0.000 dB at 1 GHz** from the 150 mm bar spacing alone, and puts the mesh cutoff at **999.3 MHz**. **The project's own figure is reproduced, not assumed.** `[R]`

**2s = 300 mm. The wavelength at 1 GHz is 299.79 mm.** The cage stops shielding at almost exactly the frequency at which MIL-STD-188-125-1 stops asking. That is arithmetic, not design.

| | |
|---|---|
| Highest frequency at 80 dB | **99.93 kHz** |
| Decades required | **5** |
| Decades delivered | **1.00** |
| **Fraction of the required band met** | **20 %** |

**These figures are an UPPER BOUND.** The classical array correction `−10 log₁₀(n)` for *n* illuminated apertures is **not applied** (it would make every figure worse); the crossings are **tied, not welded**; and no concrete absorption is credited, because no permittivity or conductivity for this concrete exists anywhere in the project `[N]`. **A measured cage will be worse than this table.** `[D]`
