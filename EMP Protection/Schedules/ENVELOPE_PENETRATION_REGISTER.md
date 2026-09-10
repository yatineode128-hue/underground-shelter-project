# ENVELOPE PENETRATION REGISTER — EMP

**Underground CBRN-hardened protective structure — Pune** · GEOMETRY REV F + M1
EMP Protection package revision **EM1** · 10.09.2026 · **FOR REVIEW - NOT FOR CONSTRUCTION**
**Sentry post excluded.** Evidence class: `[C]` confirmed · `[R]` reconstructed · `[D]` derived by this package · `[A]` assumed by this package · `[U]` unresolved · `[N]` not available — DATA REQUIRED

> **`EMP Zone` is not `zone`.** Drainage and finishes already use zones 1/2/3 for **cleanliness**. The EMP zones here are a different scheme on the same building; the `EMP` prefix is mandatory.

**Ten penetrations. Every position, bore and wall thickness is read from a confirmed project document** — the HVAC damper and valve schedule, `MEP_AND_FINISHES_COORDINATION.md` CO-1, master A.4.4 and A.4.5. **This register creates no penetration and moves none.**

**PASS** = below cutoff across the whole 10 kHz – 1 GHz band **and** at least 80 dB in band. A depth (waveguide) credit is taken **only where the bore is bounded by metal** — concrete is a lossy dielectric, not a waveguide wall.

| TAG | TYPE | LOCATION | BORE mm | DEPTH mm | BORE BOUNDED BY | CUTOFF MHz | WBC dB | SE @1 MHz dB | VERDICT | TREATMENT |
|---|---|---|---|---|---|---|---|---|---|---|
| **BV-1** | BLAST VALVE | W1 WEST WALL, BAY 1 | 100 ⌀ | 600 | steel | 1757.0 | 192 | 255 | **PASS** | **NONE REQUIRED.** The wall is the waveguide. Keep the bore metallic and the frame welded to the cage. |
| **BV-2** | BLAST VALVE | W1 WEST WALL, BAY 1 | 100 ⌀ | 600 | steel | 1757.0 | 192 | 255 | **PASS** | **NONE REQUIRED.** The wall is the waveguide. Keep the bore metallic and the frame welded to the cage. |
| **BV-3** | BLAST VALVE | W6, (14998, 4900) | 100 ⌀ | 400 | steel | 1757.0 | 128 | 191 | **PASS** | **NONE REQUIRED.** The wall is the waveguide. Keep the bore metallic and the frame welded to the cage. |
| **BV-4** | BLAST VALVE | EAST WALL, BAY 8 | 350 ⌀ | 600 | steel | 502.0 | 55 | 107 | **FAIL** | **HONEYCOMB WBC PANEL** inboard of the valve — *if* bay 8 is inside the EMP boundary. **EM-V3.** |
| **BV-5** | BLAST VALVE | EAST WALL, BAY 8 | 350 ⌀ | 600 | steel | 502.0 | 55 | 107 | **FAIL** | **HONEYCOMB WBC PANEL** inboard of the valve — *if* bay 8 is inside the EMP boundary. **EM-V3.** |
| **SEP** | SERVICE ENTRY PLATE | NORTH WALL, X 11398-12198 | 800 wide | 600 | steel | 187.4 | 20 | 66 | **FAIL** | **THE PLATE IS THE SHIELD.** Solid, welded, bonded 360° to the cast-in frame. Its apertures are the individual sleeves, treated one by one. |
| **PD-05** | RISING MAIN BORE | THROUGH THE SERVICE ENTRY PLATE | 50 ⌀ | 600 | steel | 3514.0 | 384 | 453 | **PASS** | Bond the pipe **360° to the plate** — *if it is metallic*. **No pipe material is specified anywhere in the project.** **EM-V5.** |
| **ESC1** | ESCAPE SHAFT | BAY 1, (2050, 2050) | 1400 ⌀ | 3050 | **concrete** | 125.5 | — | 41 | **FAIL** | **BONDED CONDUCTING HATCH AT THE HEAD.** Lining the shaft does not work — see notes. No hatch is specified. |
| **ESC2** | ESCAPE SHAFT | BAY 8, (19900, 2050) | 1400 ⌀ | 3600 | **concrete** | 125.5 | — | 41 | **FAIL** | **BONDED CONDUCTING HATCH AT THE HEAD.** Lining the shaft does not work — see notes. No hatch is specified. |
| **VOID** | STAIR VOID | PRESSURE SLAB, BAY 7 | 3160 wide | 900 | **concrete** | 47.4 | — | 34 | **FAIL** | **NO TREATMENT EXISTS OR IS PROPOSED.** It is the entry route. See notes — this is finding **EM-F1**. |

**Large dB figures are theory, not performance.** No practical penetration achieves 250 dB; real assemblies flatten out around 100–120 dB and are limited by **workmanship** — the bond at the frame, the gasket, the one sleeve nobody welded. Read a large number as *“the bore is not the problem here.”* `[D]`

**Why lining an escape shaft does not work.** A conducting liner would give 70 dB on ESC 1 and 82 dB on ESC 2 — but only below 126 MHz. Above that a 1400 bore propagates however well it is lined. The treatment that works is a **bonded conducting hatch at the head**, which terminates the shaft instead of trying to attenuate down it.

**The stair void is the finding.** 2 800 × 3 160 through the 900 pressure slab — **8.85 m², the largest aperture in the envelope.** It never reaches 80 dB anywhere in the band and above 47 MHz it is simply open. It opens into the headhouse (+0.900, **no earth cover**) and thence to grade through a stairwell that is **declared expendable**. Blast Door 1 is the only thing between that path and the occupied bays, and **its RF performance is vendor data the project does not have.** `[N]`
