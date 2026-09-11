# DISTRIBUTION, ESSENTIAL SERVICES AND BATTERY SCHEDULE

**Underground CBRN-hardened protective structure — Pune** · GEOMETRY REV F + M1
Electrical and Power package revision **EL1** · 11.09.2026 · **FOR REVIEW - NOT FOR CONSTRUCTION**
**Sentry post excluded.** Evidence class: `[C]` confirmed · `[R]` reconstructed · `[D]` derived here · `[A]` assumed by this package · `[U]` unresolved · `[N]` not available — DATA REQUIRED

> **A BASIC PACKAGE, ON PURPOSE.** It stops at **board level**. No circuit schedule, no cable sizing, no luminaire or socket layout — **EL-V5**.

**Three boards, and one cable entry.** Every conductor crossing the protective envelope uses the **service entry plate** — the project's single services penetration `[C]` — with a **PCI on power** and **fibre for signal**, as EM1 PoE-3 / PoE-4 require. **This package creates no new penetration.**

| BOARD | NAME | BAY | POSITION | FED FROM | NOTES |
|---|---|---|---|---|---|
| **DB-M** | MAIN LV BOARD | Bay 8 | BAY 8 - GREY ZONE, WITH GEN-1 | **MAINS** (meter panel) **+ GEN-1 15 kVA**, with changeover | Mains + generator changeover.  OUTSIDE the gas-tight envelope |
| **DB-E** | ESSENTIAL BOARD | Bay 5 | BAY 5 - CBRN PLANT | **DB-M**, and from the **battery inverter** on loss of both sources | Fed from DB-M and from the inverter.  INSIDE the gas-tight envelope |
| **DB-Z2** | EMP ZONE 2 SUB-BOARD | Bay 3 | BAY 3 - INSIDE THE SHIELDED ENCLOSURE | **DB-E through the PCI** on the EMP Zone 2 boundary | Fed through the PCI on the Zone 2 boundary - EM1 PoE-3 |

### Essential services — what stays live with no generator and no mains

| Load | kW | |
|---|---|---|
| `L-02` | 0.100 | EMERGENCY LIGHTING - maintained |
| `L-01r` | 0.150 | REDUCED GENERAL LIGHTING, 25 % of L-01  [A] |
| `S-01` | 0.100 | FIRE DETECTION AND ALARM |
| `Z-01r` | 0.750 | EMP ZONE 2 AT 50 % DUTY  [A] |
| `U-01i` | 0.033 | CLEAN SUMP PUMP, INTERMITTENT AT 10 % DUTY  [A] |
| `R-01` | 0.100 | CO2 SCRUBBER RECIRCULATION FAN  [A] - NOT IN ANY SCHEDULE, EL-V7 |
| `I-01` | 0.050 | INSTRUMENTS AND MONITORING  [A] |
| **TOTAL** | **1.283** | |

**Groundwater does not stop because the shelter is sealed.** The clean sump pump stays powered through Mode 3, and the project's third line — **hand pump PU-03** `[C]` — is what covers it if the battery fails. Both filter fans also keep their **hand crank** `[C]`. **No electrical design should obscure those two.**

### The battery — and the question that sizes it

48 V DC · depth of discharge 0.80 `[A]` · inverter efficiency 0.90 `[A]`

| | Hours | Delivered kWh | Rated kWh | Ah at 48 V | Mass kg | Min floor m² |
|---|---|---|---|---|---|---|
| **CASE A** — generator restartable after the shock | 4 | 5.13 | 7.13 | **149** | 204 | 0.40 |
| **CASE B** — no generator for the whole of Mode 3 | 48 | 61.61 | 85.56 | **1783** | 2445 | 4.80 |

> **Case A is a cabinet. Case B is a room.** They are **12× apart**. Case B is **2.4 tonnes** of lead-acid needing at least **4.8 m²** of floor merely to stay inside the **5 kPa** floor live load `[C]` A.7.2 — and **Bay 5 is already 80 % occupied as drawn** (MEP coordination **CO-3**). **There is nowhere to put it.**

**Adopted: CASE A, 4 h, 149 Ah at 48 V** `[A]` — because it is the reading **the project's own document implies**: the mode schedule calls Mode 5 *"power **or battery charging**"* and says it is *"independent of modes 1–4"*, which only makes sense if the set can run while the clean zone is closed. **If Case B is right this battery is twelve times too small — EL-V1.**
