"""
dr_schedules.py  --  writes every drainage schedule from dr_data.py.

Run:  python3 dr_schedules.py

One source, so a tag on a drawing and a row in a schedule cannot disagree.
Markdown for reading, CSV for take-off.
"""
import os
import sys
import csv

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mep_proj as P
import dr_data as D

DEST = os.path.abspath(os.path.join(HERE, "..", "Schedules"))
os.makedirs(DEST, exist_ok=True)

HDR = (f"**Underground CBRN-hardened protective structure — Pune** · "
       f"{P.GEOM_REV}\n"
       f"Drainage package revision **{P.REV['drainage']}** · {P.PACKAGE_DATE} · "
       f"**{P.STATUS}**\n"
       f"**Sentry post excluded.** Evidence class: "
       f"`[C]` confirmed · `[R]` reconstructed · `[A]` assumed by this package · "
       f"`[U]` unresolved · `[N]` not available — DATA REQUIRED\n")


def lvl(v):
    return "—" if v is None else f"({v:+.3f})"


def write(name, title, cols, rows, note=""):
    md = [f"# {title}", "", HDR, "", "| " + " | ".join(cols) + " |",
          "|" + "|".join(["---"] * len(cols)) + "|"]
    for r in rows:
        md.append("| " + " | ".join(str(c) for c in r) + " |")
    if note:
        md += ["", note]
    with open(os.path.join(DEST, name + ".md"), "w") as f:
        f.write("\n".join(md) + "\n")
    with open(os.path.join(DEST, name + ".csv"), "w", newline="") as f:
        wcsv = csv.writer(f)
        wcsv.writerow(cols)
        for r in rows:
            wcsv.writerow(r)
    print(f"  {name}.md / .csv   {len(rows)} rows")


# ---------------------------------------------------------------- 1 drains
write("DRAIN_SCHEDULE", "DRAIN AND GULLY SCHEDULE",
      ["TAG", "TYPE", "X", "Y", "LEVEL", "SEAL mm", "ZONE", "SERVES", "CLASS"],
      [(t, ty, f"{x}", f"{y}", lvl(l), (s or "—"), z, sv, c)
       for t, x, y, l, ty, s, sv, z, c in D.DRAINS],
      note=("**Seal depth 75 mm** throughout the gas-tight envelope — it holds "
            "736 Pa against the +50 to +100 Pa operating overpressure and the "
            "+300 Pa leak test (calculation D.6). Every trap inside the "
            "envelope must be **primed**; an evaporated seal is an envelope "
            "breach, not a smell.\n\n"
            "**Threshold upstands 50 mm** at W5 and at Blast Door 1 keep zone 2 "
            "and zone 3 water out of zone 1 (finding DR-F5)."))

# ----------------------------------------------------------------- 2 pipes
write("PIPE_SCHEDULE", "PIPE SCHEDULE",
      ["ID", "SERVICE", "FROM", "TO", "DN", "GRADIENT", "IL START", "IL END",
       "LENGTH m", "CLASS", "NOTES"],
      [(i, s, fr, to, (dn or "—"), g, lvl(a), lvl(b),
        (f"{L:.2f}" if L else "—"), c, n)
       for i, s, fr, to, dn, g, a, b, L, n, c in D.PIPES],
      note=("Full-bore capacity DN100 at 1:100 = **6.72 L/s at 0.85 m/s**; the "
            "design flow to the clean sump is **0.00463 L/s**, a capacity ratio "
            "of **1450 : 1**. Sizing is governed by minimum bore and "
            "self-cleansing velocity, not by flow (calculation D.4).\n\n"
            "At the design flow no practical gradient produces a self-cleansing "
            "velocity in service; the drains are cleansed by the periodic "
            "washdown the decontamination regime requires in any case. Rodding "
            "access is provided at every change of direction."))

# -------------------------------------------------------------- 3 chambers
write("CHAMBER_SCHEDULE", "CHAMBER, CATCHPIT AND ACCESS SCHEDULE",
      ["TAG", "TYPE", "SIZE", "COVER LEVEL", "INVERT", "CLASS", "SERVES"],
      [(t, ty, s, lvl(cl), lvl(iv), c, sv)
       for t, ty, s, cl, iv, sv, c in D.CHAMBERS],
      note=("No chamber position outside the structures can be fixed: no site "
            "plan, boundary or contour exists in the project (open item D3). "
            "External chambers are scheduled and detailed but **not "
            "positioned**."))

# ------------------------------------------------------- 4 sump and pumps
write("SUMP_AND_PUMP_SCHEDULE", "SUMP, PUMP, TANK AND SOAKAWAY SCHEDULE",
      ["TAG", "ITEM", "DUTY / SIZE", "LEVEL", "CLASS", "NOTES"],
      [(t, it, d, lvl(l), c, n) for t, it, d, l, n, c in D.EQUIPMENT],
      note=("**SK-01 is 2.3 % short of its own stated requirement** — "
            "21.99 m² provided against 22.5 m² required (conflict DR-C2). Not "
            "resized here: the 20 L/m²/day absorption rate is itself `[A]` and "
            "the mandatory percolation test may move the requirement by far "
            "more than 2.3 %.\n\n"
            "**PU-01/02 duty ratio 0.31 %** — one start every 3.4 days, 15 min "
            "per start. A failed standby would never be discovered by use, so a "
            "witnessed monthly test of the standby path and the hand pump is "
            "required in O&M (finding DR-F1)."))

# ----------------------------------------------------------- 5 fixtures
write("SANITARY_FIXTURE_SCHEDULE", "SANITARY FIXTURE DRAINAGE SCHEDULE",
      ["TAG", "FIXTURE", "ROOM", "DISCHARGE", "TRAP", "CLASS", "NOTES"],
      [(t, fx, rm, dg, tr, c, n) for t, fx, rm, dg, tr, n, c in D.FIXTURES],
      note=("**No sanitary fixture layout exists anywhere in the project.** "
            "The fixtures above are those the project's own text implies — the "
            "lavatory and medical spaces of Bay 2 (master A.3), the "
            "sealed-cassette toilets and decon airlock of S-06, and the "
            "headhouse hose-down point of the Rev F ground plan. Fixture "
            "counts, positions and rim heights are `[N]` **DATA REQUIRED**.\n\n"
            "**Open item D2** — the peacetime foul route from the Bay 2 "
            "lavatory is undefined. Case A (cassette in all modes, drawn) needs "
            "no soil drainage. Case B (plumbed WC) needs a pumping unit and a "
            "second penetration of the protective envelope, which is a "
            "protective-design decision. **ENGINEER TO CONFIRM.**"))

# ------------------------------------------------------------ 6 zones
write("HYDRAULIC_ZONE_SCHEDULE", "HYDRAULIC ZONE SCHEDULE",
      ["ZONE", "NAME", "EXTENT", "DESTINATION", "STATUS", "CLASS"],
      [(z, n, e, d, s, c) for z, n, e, d, s, c in D.ZONES],
      note=("**Finding DR-F5.** The protective boundary (Blast Doors 1 and 2, "
            "W6 and W7) and the gas-tight sub-division at W5 cut the shelter "
            "into three hydraulically separate zones. Water may not cross "
            "between them. **Two of the three have no closed drainage "
            "destination.** That is a consequence of the protective boundary, "
            "not a layout error, and closing it is a protective-design "
            "decision — a blast and gas-tight boundary crossing, or manual "
            "transfer in sealed containers. Nothing is assumed across the "
            "boundary."))

# ------------------------------------------------------- 7 design flows
write("DESIGN_FLOW_SCHEDULE", "DESIGN FLOW SCHEDULE",
      ["ITEM", "FLOW", "CAPACITY / STORE", "DISCHARGES TO", "SOURCE"],
      [(a, b, c, d, "S-06 `[C]`") for a, b, c, d in P.DESIGN_FLOWS],
      note=("Reproduced verbatim from sheet S-06 so that this package can be "
            "checked against it line by line.\n\n"
            "**Conflict DR-C1** — the 0.10 L/s against *stairwell / approach "
            "surface water* is the **Rev E open-cut** figure (7.2 m² of open "
            "pit at 50 mm/h, reproduced exactly in calculation D.8). At Rev F "
            "the approach is covered and the governing case is the door-open "
            "driving-rain rate of drawing 5 note 9, about 12 × smaller. "
            "Conservative, nothing unsafe. **RULED AND CLOSED by RC1**, "
            "10 Sep 2026 (master Part H.14 / K.1 U12): **Rev F governs** — "
            "precedent C1, the drawing governs — and the 0.10 L/s **stays as a "
            "declared conservatism**, because removing it changes no pump, no "
            "pipe and no pit (the stairwell pump is 20 × it) and deleting a "
            "superseded number would hide the history. Both figures are shown "
            "and labelled on D-103."))

print(f"\n[written to] {DEST}")
