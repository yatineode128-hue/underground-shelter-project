# EMP PROTECTION — QA/QC REPORT  ·  revision EM1

**Underground CBRN-hardened protective structure — Pune** · GEOMETRY REV F + M1
EMP Protection package **EM1** · 10.09.2026 · **FOR REVIEW — NOT FOR CONSTRUCTION**
**Sentry post excluded.** Main staircase unchanged.

> **What this report is.** A record of what was actually checked and what the check returned.
> Where a thing could not be verified, it says so and says why. **No check below is claimed
> that was not run.**

---

## 1  The check this package exists to pass

Master **K.3** records, as a **`[CONFIRMED]`** item:

> *"EMP rebar cage **0 dB @ 1 GHz** — **say it before a reviewer does**. Zone 2 welded steel
> room is the answer."*

That figure is stated in the master with no derivation anywhere in the project. This package
re-derives it from the one confirmed input — the **150 mm bar spacing**, master A.5.

| | |
|---|---|
| Model | Thin conducting screen, square aperture array: `SE = 20 log₁₀(λ / 2s)` |
| Input | `s` = **150 mm** `[C]` — the only input used |
| **SE at 1 GHz** | **0.000 dB** |
| Master K.3 says | **0 dB** |
| **Result** | **PASS — the project's own figure is reproduced, not assumed** `[R]` |

**Why this matters more than it looks.** The model was not chosen because it is convenient; it
was chosen because **it is the model that recovers the project's own number.** Every other cage
figure in this package — the 20 dB/decade slope, the 99.93 kHz crossing, the 999.31 MHz cutoff
— comes from that same validated model.

**Secondary check, unprompted by any project figure:** `2s` = 300 mm and λ at 1 GHz =
**299.79 mm**. The mesh cutoff, `c/2s` = **999.31 MHz**, lands **0.07 % below the top of the
MIL-STD-188-125-1 band**. That is arithmetic, not design, and it is stated on EM-001 and EM-201.

---

## 2  Checks executed

### 2.1 Source traceability — every input read from a confirmed document

| # | Check | Result | Basis |
|---|---|---|---|
| T1 | Bar spacing 150, both curtains | **PASS** | master A.5 |
| T2 | Five blast valves — tag, bore, position, host wall | **PASS** | `HVAC/Schedules/DAMPER_AND_VALVE_SCHEDULE.md`, all `[C]` |
| T3 | Service entry plate X 11398–12198, north wall, 800 wide | **PASS** | `MEP_AND_FINISHES_COORDINATION.md` CO-1 |
| T4 | Service entry plate **level and size** | **`[N]` — carried, not invented** | CO-1 records it is nowhere in the project |
| T5 | PD-05 DN50 rising main through the plate | **PASS** | `Drainage/Schedules/PIPE_SCHEDULE.md` |
| T6 | PD-05 **material** | **`[N]` — no pipe material is specified for ANY run** | searched the whole Drainage package: zero hits |
| T7 | Escape shafts 1400 bore, 250 collar, heads +0.150 / +0.700 | **PASS** | master A.4.5 |
| T8 | Escape shaft collar reinforcement 5-T25 each side/face/direction | **PASS** | master F.1 |
| T9 | Stair void 2800 × 3160 in the 900 slab | **PASS** | master A.4.4 |
| T10 | Void free edge thickened 900 → 1200, 6-T25 top and bottom | **PASS** | master F.1 |
| T11 | Bay 3 internal 3500 × 5000 × 3200; W8 door gaps Y 2500–3400 | **PASS** | master A.3 |
| T12 | `W-04` = EMP Zone 2 lining, `[C]` requirement / `[N]` specification | **PASS** | `Schedule of Finishes/Schedules/FINISH_LEGEND.md` |
| T13 | MIL-STD-188-125-1 sections and IEEE Std 299 | **PASS — only register entries cited** | master Part G |
| T14 | Deccan basalt 10³–10⁴ Ω·m; ≤ 5 Ω target | **PASS** | master K.3 and Part G |

### 2.2 Independent geometric re-check — EMP Zone 2 in bay 3

Re-computed from `em_proj.Z2` against master A.3, not read off a drawing.

| Clearance | Value | Rule | Result |
|---|---|---|---|
| West, to the bay face X 5520 | **300** | ≥ 300 survey gap | **PASS** |
| East, to the bay face X 9020 | **800** | ≥ 300 | **PASS** |
| South, to the circulation edge Y 3400 | **300** | ≥ 300 | **PASS** |
| North, to the wall face Y 5600 | **300** | ≥ 300 | **PASS** |
| Head, to the roof soffit (3200 clear) | **1 000** | ≥ 150 | **PASS** |
| Clear above the 150 HVAC duct zone `[C]` HV1 | **850** | > 0 | **PASS** |
| Overlap with the Y 2500–3400 circulation band | **0 mm** | zero | **PASS — entirely clear** |

**A 300 mm gap is held on every free face for a reason**: an IEEE Std 299 survey has to reach
every seam. **A shielded room you cannot walk around cannot be tested.**

### 2.3 Drawings

| # | Check | Result |
|---|---|---|
| D1 | `Drainage/Scripts/mep_validate.py` — 11 checks × 6 sheets | **0 errors, 0 warnings** |
| D2 | `DRAWING QAQC/Scripts/dxfqa.py` — text-on-text overlaps | **0** |
| D3 | Entities outside the A1 sheet border | **0** |
| D4 | Text past the right-hand sheet edge | **0** |
| D5 | Entities intruding into the title block | **0** |
| D6 | Title block present | **6 of 6** |
| D7 | Scope-exclusion note present | **6 of 6** |
| D8 | DXF version AC1024, `$INSUNITS` = 4 | **6 of 6** |
| D9 | Every entity on a declared layer | **6 of 6** |
| D10 | Zero-length / degenerate entities | **0** |

> **One reported item is a false positive and is recorded as such.** `dxfqa.py` reports
> `into_titleblock: 20` on every EMP sheet. That tool whitelists only the `S-TITLE` layer, and
> the MEP-family title block draws on `M-TITLE`. **The issued HVAC sheet `M-101` returns the
> identical count of 20.** The EMP sheets are at parity with the issued set; check D5 above is
> the corrected reading.

### 2.4 Schedules

| # | Check | Result |
|---|---|---|
| S1 | All five CSVs parse, no ragged rows | **PASS — 3 / 10 / 5 / 3 / 12 rows** |
| S2 | Every schedule figure imported from `em_proj` / `em_calc`, none typed | **PASS** |
| S3 | Penetration register row count = `em_proj.PENETRATIONS` | **PASS — 10** |
| S4 | Schedule figures agree with the drawings | **PASS by construction** — both import the same module |

### 2.5 Non-interference — the check that matters to the rest of the project

| # | Check | Result |
|---|---|---|
| N1 | Any shared library modified (`sc_dxflib.py`, `mep_dxf.py`, `mep_proj.py`, `mep_views.py`, `mep_validate.py`) | **NONE — `git status` clean on all five Scripts directories** |
| N2 | Any existing design, drawing, model, schedule or bill file modified | **NONE** |
| N3 | New penetration of the envelope created | **NONE — the ten are the project's own** |
| N4 | Main staircase touched | **NO — frozen, annotated only** |
| N5 | Sentry post touched | **NO — excluded, and said so on every sheet** |
| N6 | Existing `[ASSUMED]` / `[UNRESOLVED]` / `[NOT AVAILABLE]` tag converted or deleted | **NONE** |
| N7 | Clause cited that is not in master Part G | **NONE** |

**N1 is verified directly**: the EMP package subclasses the shared sheet library rather than
editing it, so Drainage, HVAC and Schedule of Finishes regenerate byte-identically whether this
package exists or not.

---

## 3  What could NOT be verified, and why

| | |
|---|---|
| **The cage figure itself** | **EMP Zone 1 cannot be surveyed to IEEE Std 299.** A buried box under 2 m of engineered cover has no accessible exterior to place a transmitter on. §0 of the design basis is a **calculation and will stay a calculation.** Any statement that the box gives 80 dB is unsupportable and is not made anywhere in this package. |
| **The direction of the error** | Every cage figure is an **UPPER BOUND**. The `−10 log₁₀(n)` array correction is not applied (it would make them worse); the crossings are **tied, not welded**, and **no statement of which exists anywhere in the project** `[N]` although it materially changes the result; no concrete absorption is credited `[N]`, which is in the safe direction. **A measured cage will be worse than the table.** |
| **Zone 2's size** | `[A]` at every dimension. No equipment schedule exists because **no electrical design exists** — the project's largest gap. The dimensions were checked to **fit**; they were not **derived**. **EM-V2.** |
| **Every vendor performance figure** | Shielded door, PCI residual, honeycomb blast rating, blast door RF performance — all `[N]`. **No number is invented for any of them.** The PCI residual is deliberately left blank: MIL-STD-188-125-1 specifies it *by pulse test* and the project's register carries the section number only. |
| **The threat** | No incident field, waveform or E1/E2/E3 decomposition. **U2** and **U3** remain open in master K.1b. The package is designed against the **80 dB performance requirement**, which needs none of them — that is a deliberate choice, not an omission. |
| **Whether bay 8 is inside the boundary** | `[U]`. **No EMP boundary has ever been drawn.** §2 of the design basis proposes one; only the client can adopt it. **EM-V3.** |

---

## 4  Findings raised — six

`EM-F1` stair void · `EM-F2` cage meets one decade of five · `EM-F3` Zone 2 named for four
revisions with no Zone 1 and no specification · `EM-F4` BV-4/BV-5 the only double failure ·
`EM-F5` 5 Ω unachievable and not an EMP number · `EM-F6` no communications design exists.

Full statements in `Documentation/EMP_PROTECTION_DESIGN_BASIS.md` §7 and on sheet **EM-001**.

## 5  Open items raised — six, none resolved

`EM-V1` … `EM-V6`. **Raising six open items is deliberate.** A package that quietly filled them
in would be inventing a specification, which is the one thing this project's rules forbid
absolutely.

---

## 6  Status

**FOR REVIEW — NOT FOR CONSTRUCTION.**

This is a design basis and a set of coordination drawings. It is **not construction-ready**:
EM-V1 (adopt the zone model) and EM-V2 (the equipment schedule) both gate it, and EM-V2 waits
on the project's missing electrical design. **The findings, however, do not wait on anything** —
they are arithmetic on confirmed geometry and they are true today.
