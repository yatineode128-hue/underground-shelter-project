"""
hv_schedules.py  --  writes every HVAC schedule from hv_data.py.
Run:  python3 hv_schedules.py
"""
import os
import sys
import csv

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "Drainage",
                                                "Scripts")))
import mep_proj as P
import hv_data as H

DEST = os.path.abspath(os.path.join(HERE, "..", "Schedules"))
os.makedirs(DEST, exist_ok=True)

HDR = (f"**Underground CBRN-hardened protective structure — Pune** · "
       f"{P.GEOM_REV}\n"
       f"HVAC package revision **{P.REV['hvac']}** · {P.PACKAGE_DATE} · "
       f"**{P.STATUS}**\n"
       f"**Sentry post excluded.** Evidence class: `[C]` confirmed · "
       f"`[R]` reconstructed · `[A]` assumed by this package · "
       f"`[U]` unresolved · `[N]` not available — DATA REQUIRED\n")


def write(name, title, cols, rows, note=""):
    md = [f"# {title}", "", HDR, "", "| " + " | ".join(cols) + " |",
          "|" + "|".join(["---"] * len(cols)) + "|"]
    for r in rows:
        md.append("| " + " | ".join(str(c) for c in r) + " |")
    if note:
        md += ["", note]
    open(os.path.join(DEST, name + ".md"), "w").write("\n".join(md) + "\n")
    with open(os.path.join(DEST, name + ".csv"), "w", newline="") as f:
        wc = csv.writer(f)
        wc.writerow(cols)
        for r in rows:
            wc.writerow(r)
    print(f"  {name}.md / .csv   {len(rows)} rows")


write("AIRFLOW_SCHEDULE", "ROOM AIRFLOW SCHEDULE",
      ["ROOM", "USE", "VOLUME m³", "SUPPLY DAY m³/h", "ACH DAY",
       "SUPPLY NIGHT m³/h", "ACH NIGHT", "EXTRACT m³/h", "OCC DAY",
       "OCC NIGHT"],
      [(r, u, f"{v:.2f}", sd, f"{sd/v:.2f}", sn, f"{sn/v:.2f}", e, od, on)
       for r, u, v, sd, sn, e, od, on in H.AIRFLOW],
      note=("Total supply **300 m³/h in both modes** — the confirmed design "
            "flow on sheet S-06, exactly. The split is an engineering "
            "selection by this package `[A]`; the total is `[C]`.\n\n"
            "**The occupied room of the ops/berthing pair gets 135 m³/h in "
            "either mode = 15.0 m³/h per person, exactly the working-shelter "
            "rate S-06 names as criterion 2.** Two volume control dampers "
            "(VCD-1, VCD-2) make the swap. They are not a refinement: without "
            "them, holding 15 m³/h/person in both rooms at once would need 270 "
            "of the 300 m³/h and leave 30 m³/h for the stores, the lavatory "
            "and the plant room. See calculation H.6.\n\n"
            "**Nothing is supplied directly to Bay 6.** The airlock is the "
            "exhaust path and receives the whole 300 m³/h as transfer air — "
            "which is what makes the confirmed 0 → +10 → +20 → +35 → +50 Pa "
            "cascade work."))

write("HVAC_EQUIPMENT_SCHEDULE", "HVAC EQUIPMENT SCHEDULE",
      ["TAG", "ITEM", "DUTY", "POSITION", "CLASS", "NOTES"],
      [(t, i, d, p, c, n) for t, i, d, p, n, c in H.EQUIPMENT],
      note=("**Fan static pressure is not stated.** Five of the eight loss "
            "components in the build-up are vendor data (calculation H.9). "
            "The ductwork and overpressure part that *can* be calculated is "
            "**161 Pa**; a CBRN filter train's own losses normally dominate "
            "that. The fan must be selected on the **dirty** filter figures, "
            "not the clean ones."))

write("DUCT_SCHEDULE", "DUCT SCHEDULE",
      ["REF", "SERVICE", "FROM → TO", "m³/h", "SIZE", "VELOCITY", "CLASS",
       "NOTES"],
      [(r, s, ft, q, sz, v, c, n) for r, s, ft, q, sz, v, n, c in H.DUCTS],
      note=("Blast-valve throat sizes and their velocities are **confirmed on "
            "S-06** and reproduced exactly by calculation H.7 — DN100 at "
            "300 m³/h gives 10.61 m/s against the sheet's 10.6, DN350 at "
            "2600 m³/h gives 7.51 against 7.5.\n\n"
            "**The small branches are governed by the practical minimum duct "
            "size, not by velocity.** At 30 m³/h a duct sized for 4 m/s would "
            "be about 100 × 25 mm — not buildable, not cleanable and not "
            "sealable to the standard this envelope needs."))

write("TERMINAL_SCHEDULE", "DIFFUSER, GRILLE AND TRANSFER SCHEDULE",
      ["TAG", "TYPE", "ROOM", "m³/h DAY", "m³/h NIGHT", "SIZE", "CLASS",
       "NOTES"],
      [(t, ty, r, d, n_, s, c, nt) for t, ty, r, d, n_, s, nt, c
       in H.TERMINALS],
      note=("Terminal sizes and quantities are an engineering selection `[A]`. "
            "**No noise criterion exists anywhere in the project**, so throw, "
            "NC and terminal pressure drop are not checked — DATA REQUIRED "
            "before the terminals are ordered.\n\n"
            "**TG-01 carries a gas-tight shut-off damper**: it is the transfer "
            "from the clean zone into the airlock, and in closed mode it must "
            "seal."))

write("DAMPER_AND_VALVE_SCHEDULE", "DAMPER, BLAST VALVE AND OPRV SCHEDULE",
      ["TAG", "TYPE", "LOCATION", "FUNCTION", "CLASS"],
      [(t, ty, lo, fn, c) for t, ty, lo, fn, c in H.DAMPERS],
      note=("**RECESS EVERY BLAST VALVE — IS 4991 Cl. 6.2.1.** A valve flush "
            "in a vertical face sees the reflected pressure p_r = 1366 kPa, "
            "3.6 × the 383 kPa side-on value: **131 kN on a DN350 disc instead "
            "of 36.8 kN**.\n\n"
            "**A manual quarter-turn gas-tight damper is required inboard of "
            "every blast valve, operable from inside without tools** — "
            "confirmed on S-06. It is the crew's last line if a valve fails "
            "open."))

write("FILTER_TRAIN_SCHEDULE", "NBC FILTER TRAIN SCHEDULE",
      ["STAGE", "SPECIFICATION", "FUNCTION", "CLASS"],
      [(s, sp, f, c) for s, sp, f, c in H.FILTERS],
      note=("Two identical trains, **each able to carry the whole 300 m³/h "
            "duty on its own — TRUE N+1, not 2 × 150** `[C]`.\n\n"
            "**A flow meter and a differential-pressure gauge across every "
            "stage** are required by S-06 — *'the only way to know a filter is "
            "spent'*. They are what turns a vendor's dirty-filter figure into "
            "a maintenance trigger.\n\n"
            "**The carbon bed is the only stage with a finite consumable "
            "life.** Its change-out interval needs a challenge concentration "
            "and vendor data; neither exists — DATA REQUIRED."))

write("OPERATING_MODE_SCHEDULE", "OPERATING MODE SCHEDULE",
      ["MODE", "NAME", "WHEN", "WHAT RUNS", "FLOW", "PRESSURE"],
      [(m, n, wh, wt, f, p) for m, n, wh, wt, f, p in H.MODES],
      note=("**Mode 5 is independent of modes 1–4.** The generator air path "
            "(BV-4, BV-5, Bay 8) does not touch the gas-tight envelope — "
            "Bay 8 is outside it, behind Blast Door 2 and W7. Running the "
            "generator does not depressurise the clean zone and does not "
            "consume filter life.\n\n"
            "**Mode 3 is limited by the soda lime, not the oxygen** "
            "(finding HV-F1): unscrubbed CO₂ alone gives 9.9 h, the 40 kg "
            "soda-lime store gives 48 h, the 15 m³ oxygen store gives 80 h. "
            "**The consumable to count on the drill card is soda lime.**\n\n"
            "**Mode 1 is a gap on S-06** — no filter bypass for peacetime "
            "running is shown anywhere. Without one, every hour of peacetime "
            "ventilation spends carbon-bed life. **Not added here**: a bypass "
            "adds a leak path to the envelope and that is a protective "
            "decision (HV-D1)."))

print(f"\n[written to] {DEST}")
