# ELECTRICAL LOAD SCHEDULE

**Underground CBRN-hardened protective structure — Pune** · GEOMETRY REV F + M1
Electrical and Power package revision **EL1** · 11.09.2026 · **FOR REVIEW - NOT FOR CONSTRUCTION**
**Sentry post excluded.** Evidence class: `[C]` confirmed · `[R]` reconstructed · `[D]` derived here · `[A]` assumed by this package · `[U]` unresolved · `[N]` not available — DATA REQUIRED

> **A BASIC PACKAGE, ON PURPOSE.** It stops at **board level**. No circuit schedule, no cable sizing, no luminaire or socket layout — **EL-V5**.

**Standby units are not counted twice.** FAN-2, PU-02 and PU-05 are standby to FAN-1, PU-01 and PU-04 and never run simultaneously with them `[C]`. The schedule carries the **duty unit only**.

| TAG | LOAD | BOARD | kW | CLASS | NOTES |
|---|---|---|---|---|---|
| **L-01** | GENERAL LIGHTING, BAYS 1-8, LED | DB-E | 0.520 | `[A]` | 104 m2 at 5 W/m2. No luminaire schedule exists - EL-V5 |
| **L-02** | EMERGENCY LIGHTING, MAINTAINED, DC | DB-E | 0.100 | `[A]` | On the battery at all times.  FS-V2 waits on this |
| **P-01** | SMALL POWER, SOCKET OUTLETS | DB-M | 1.000 | `[A]` | Allowance.  No socket schedule exists - EL-V5 |
| **F-01** | FILTER TRAIN FAN, 1 DUTY OF 2 | DB-E | 0.379 | `[R]` | AHU-1 / AHU-2 [C].  FAN-2 is standby, NOT simultaneous |
| **D-01** | DEHUMIDIFIER DH-1 | DB-E | 1.000 | `[A]` | DH-1 confirmed in master A.3; ITS DUTY IS [N] - allowance only |
| **U-01** | CLEAN SUMP PUMP PU-01, 1 DUTY OF 2 | DB-E | 0.334 | `[R]` | 1.5 L/s [C].  PU-02 standby, auto-alternating, NOT simultaneous |
| **U-02** | STAIRWELL PUMP PU-04, 1 DUTY OF 2 | DB-M | 0.223 | `[R]` | 2.0 L/s [C].  OUTSIDE the protective envelope |
| **Z-01** | EMP ZONE 2 OPS / COMMS EQUIPMENT | DB-Z2 | 1.500 | `[A]` | ALLOWANCE, NOT A SCHEDULE.  This is the number EM-V2 was waiting for |
| **S-01** | FIRE DETECTION AND ALARM PANEL | DB-E | 0.100 | `[A]` | Panel and loop only.  Head layout is fire engineering - FS-V2 |
| **B-01** | BATTERY CHARGER / INVERTER | DB-M | 0.800 | `[A]` | Sized with the battery, section E.5 |
| **G-01** | GENERATOR AUXILIARIES | DB-M | 0.300 | `[A]` | Controls, block heater, starting.  Vendor data [N] |

| | |
|---|---|
| **Connected load** | **6.256 kW** |
| at power factor 0.85 | **7.360 kVA** |
| **GEN-1 rating** `[C]` master A.3 | **15.0 kVA** |
| **Utilisation** | **49.1 %** |
| Spare | 7.640 kVA |

### The 15 kVA is right, and needs no change `[D]`

It is **about twice the connected demand**, and **49 %** sits in the healthy loading band for a diesel set — high enough to avoid wet-stacking, low enough to carry growth. The largest motor is the filter fan at **0.379 kW**; even a direct-on-line start is about **2.7 kVA**. **There is no starting problem.**

**Derived figures.** Fan `P = Q·Δp/(η_fan·η_motor)` at 300 m³/h `[C]` and 2000 Pa `[A]` *dirty* filter — HV1 records that only **161 Pa** of the loss build-up is derivable and five of eight components are vendor data `[N]`. Pumps `P = ρgQH/(η_pump·η_motor)` at the confirmed duties and assumed heads. Lighting 104 m² `[C]` × 5 W/m² `[A]`.
