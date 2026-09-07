# HVAC EQUIPMENT SCHEDULE

**Underground CBRN-hardened protective structure — Pune** · GEOMETRY REV F + M1
HVAC package revision **HV1** · 05.09.2026 · **FOR REVIEW - NOT FOR CONSTRUCTION**
**Sentry post excluded.** Evidence class: `[C]` confirmed · `[R]` reconstructed · `[A]` assumed by this package · `[U]` unresolved · `[N]` not available — DATA REQUIRED


| TAG | ITEM | DUTY | POSITION | CLASS | NOTES |
|---|---|---|---|---|---|
| AHU-1 | NBC FILTER TRAIN 1 | 300 m3/h | Bay 5, X 11098-12548, Y 3900-5550 | [C] | Louvre + blast valve + G4/F7 pre-filter + EN 1822 H14 HEPA + ASZM-TEDA carbon + fan with hand crank + plenum. Carries the WHOLE duty on its own - TRUE N+1 |
| AHU-2 | NBC FILTER TRAIN 2 | 300 m3/h | Bay 5, X 11098-12548, Y 2700-3800 | [C] | Identical to AHU-1. Standby |
| FAN-1 | SUPPLY FAN, TRAIN 1 | 300 m3/h | Within AHU-1 | [C]/[N] | Electric drive PLUS HAND CRANK [C]. Static pressure NOT DERIVABLE - five of the eight loss components are vendor data (calc H.9) |
| FAN-2 | SUPPLY FAN, TRAIN 2 | 300 m3/h | Within AHU-2 | [C]/[N] | As FAN-1 |
| CO2-1 | CO2 SCRUBBER, SODA LIME | 20 kg/day | Bay 5 | [C] | 40 kg store = 48 h of closed mode. THE SODA LIME, NOT THE O2, IS WHAT LIMITS CLOSED MODE - finding HV-F1 |
| O2-1 | OXYGEN STORE | 4.5 m3/day | Bay 5 | [C] | 2 x 50 L cylinders at 150 bar = 15 m3 = 80 h |
| DH-1 | DEHUMIDIFIER | DUTY NOT STATED | Bay 5 | [C]/[N] | Confirmed in master A.3. No latent load and no target RH exist anywhere in the project - DATA REQUIRED. Condensate to the clean sump through a 75 deep-seal trap |
| GEN-1 | GENERATOR | 15 kVA | Bay 8, the grey zone | [C]/[N] | Combustion and cooling air 2600 m3/h through BV-4 / BV-5. Heat rejection into bay 8 NOT STATED |
| SH-1 | FRESH-AIR SHAFT | 600 x 600 | West of the box | [C] | Gooseneck head at +1.500. 12.3 m from the intake to the entry, against a >= 10 m rule |
| SH-2 | GENERATOR AIR SHAFT | 600 x 600 | East of the box, X 22598-23198 | [C] | Serves BV-4 and BV-5 |

**Fan static pressure is not stated.** Five of the eight loss components in the build-up are vendor data (calculation H.9). The ductwork and overpressure part that *can* be calculated is **161 Pa**; a CBRN filter train's own losses normally dominate that. The fan must be selected on the **dirty** filter figures, not the clean ones.
