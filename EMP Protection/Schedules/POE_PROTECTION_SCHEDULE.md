# POINT-OF-ENTRY (PoE) PROTECTION SCHEDULE — EMP ZONE 2

**Underground CBRN-hardened protective structure — Pune** · GEOMETRY REV F + M1
EMP Protection package revision **EM1** · 10.09.2026 · **FOR REVIEW - NOT FOR CONSTRUCTION**
**Sentry post excluded.** Evidence class: `[C]` confirmed · `[R]` reconstructed · `[D]` derived by this package · `[A]` assumed by this package · `[U]` unresolved · `[N]` not available — DATA REQUIRED

> **`EMP Zone` is not `zone`.** Drainage and finishes already use zones 1/2/3 for **cleanliness**. The EMP zones here are a different scheme on the same building; the `EMP` prefix is mandatory.

**Five ways into EMP Zone 2, and the treatment of each.** The section numbers are the ones already in the project's own code register (master Part G) — **no clause not in that register is cited.**

| PoE | KIND | MIL-STD-188-125-1 § | TREATMENT | PERFORMANCE | NOTES | CLASS |
|---|---|---|---|---|---|---|
| **PoE-1** | ACCESS — shielded door | 5.4 | RF-gasketed or knife-edge shielded door, SE certified to match the enclosure | ≥ 80 dB | **`[N]` type and vendor.** A shielded door is the usual place a room fails its survey | `[A]` / `[N]` |
| **PoE-2** | VENTILATION — honeycomb WBC | 5.5 | Honeycomb vent panel, **6 mm cell × 25 mm deep**, frame welded to the enclosure | cutoff **29.3 GHz** · **133 dB** (**+53 dB** margin) | Mounted **inboard** of any blast device — the valve takes the pressure, the honeycomb takes the RF. **Own blast rating `[N]`.** Adds pressure drop HV1 did not allow for | `[A]` |
| **PoE-3** | POWER — PCI | 5.7.2.1 | Protective device on **every** conductor crossing the boundary, mounted **on** the boundary, not near it | **`[N]` — no residual quoted** | MIL-STD-188-125-1 specifies PCI performance **by pulse test**; the project register carries the section number only. **Inventing a figure would be worse than `[N]`** | `[C]` method / `[N]` value |
| **PoE-4** | SIGNAL — fibre | 5.7.4.1 | Optical fibre, **no metallic strength member, no metallic armour** | **A dielectric penetration is not a penetration** | **The one place this project can buy perfect performance for almost nothing — and it should take it.** `[D]` | `[D]` |
| **PoE-5** | RF — antenna / feeder | 5.7.6 | **DOES NOT EXIST** | **`[N]`** | **There is no antenna, mast, feeder or communications design anywhere in this project.** An ops room that cannot transmit is an ops room in name only, and an antenna is by definition a deliberate conductor from outside to inside. **EM-V4** | `[N]` |

**A shield is only as good as its worst point of entry.** 133 dB of honeycomb is worth nothing behind a door that leaks, and a perfect door is worth nothing beside an unfiltered power conductor. **PoE-1 to PoE-5 are one system and are surveyed as one system.**
