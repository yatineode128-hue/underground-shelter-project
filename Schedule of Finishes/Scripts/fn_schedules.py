"""
fn_schedules.py  --  writes every finishes schedule from fn_data.py.
Run:  python3 fn_schedules.py
"""
import os
import sys
import csv

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "Drainage",
                                                "Scripts")))
import mep_proj as P
import fn_data as F

DEST = os.path.abspath(os.path.join(HERE, "..", "Schedules"))
os.makedirs(DEST, exist_ok=True)

HDR = (f"**Underground CBRN-hardened protective structure — Pune** · "
       f"{P.GEOM_REV}\n"
       f"Schedule of Finishes revision **{P.REV['finishes']}** · "
       f"{P.PACKAGE_DATE} · **{P.STATUS}**\n"
       f"**Sentry post excluded.** Evidence class: `[C]` confirmed · "
       f"`[R]` reconstructed · `[A]` assumed by this package · "
       f"`[U]` unresolved · `[N]` not available — DATA REQUIRED\n")

WARN = ("> **NO FINISH SPECIFICATION EXISTS ANYWHERE IN THIS PROJECT.** Every "
        "code below is a **performance requirement** derived from something "
        "the project does confirm — the exposure class, the decontamination "
        "duty, the gas-tight envelope, the EMP requirement, the wet areas, "
        "the frozen stair geometry. **The product that satisfies it is left "
        "open.** Anywhere a thickness, product, colour or manufacturer would "
        "normally appear, this schedule says so rather than inventing one.\n")


def write(name, title, cols, rows, note=""):
    md = [f"# {title}", "", HDR, "", WARN, "",
          "| " + " | ".join(cols) + " |",
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


def lvl(v):
    return "—" if v is None else f"({v:+.3f})"


# ------------------------------------------------------------- 1 legend
legend = []
for grp, rows in (("FLOOR", F.FLOORS), ("SKIRTING", F.SKIRTINGS),
                  ("WALL", F.WALLS), ("CEILING / SOFFIT", F.CEILINGS)):
    for code, desc, perf, src, cls in rows:
        legend.append((code, grp, desc, perf, src, cls))
for code, desc, perf, src, cls in F.DOORS:
    legend.append((code, "DOOR", desc, perf, src, cls))
for row in F.WATERPROOFING + [F.WP_EXTRA]:
    code, desc, perf, src = row[0], row[1], row[2], row[3]
    legend.append((code, "WATERPROOFING", desc, perf, src, "[C]"))

write("FINISH_LEGEND", "FINISH LEGEND — EVERY CODE DEFINED",
      ["CODE", "GROUP", "DESCRIPTION", "PERFORMANCE REQUIREMENT",
       "WHERE THE REQUIREMENT COMES FROM", "CLASS"], legend,
      note=("Codes run `F-nn` floor · `S-nn` skirting · `W-nn` wall · "
            "`C-nn` ceiling/soffit · `D-nn` door · `WP-nn` waterproofing.\n\n"
            "**Every code is a requirement, not a product.** The column that "
            "would normally carry a manufacturer carries the reason the "
            "requirement exists instead."))

# --------------------------------------------------------- 2 room schedule
write("ROOM_FINISH_SCHEDULE", "ROOM FINISH SCHEDULE",
      ["ROOM", "NAME", "LEVEL", "AREA m²", "FLOOR", "SKIRTING", "WALL",
       "CEILING", "DOOR", "WATERPROOFING", "WET", "SPECIAL REQUIREMENTS",
       "REMARKS"],
      [(n, nm, lvl(l), ("—" if a is None else f"{a:.2f}"), f, s, w, c, d, wp,
        ("YES" if wet else "—"), sp, rm)
       for n, nm, l, a, f, s, w, c, d, wp, wet, sp, rm in F.ROOMS],
      note=("**13 spaces scheduled — every space in the project except the "
            "sentry post**, which is excluded from this package.\n\n"
            "Areas are computed from the confirmed bay widths × the 5.000 m "
            "internal width, except the headhouse (11.15 m² usable, confirmed "
            "on the Rev F ground plan) and the stairwell landings and "
            "platform (1500 × 1500 each, confirmed in master A.4.7). G-05 has "
            "no area — it is the guarded edge of the stair void, not a room.\n\n"
            "**Wet areas: U-02, U-05, U-06, G-03, G-04.** Each takes F-02 or "
            "F-05, W-02 or W-05, WP-04 or WP-06, a coved skirting, and falls "
            "coordinated with the DRAINAGE package."))

# ------------------------------------------------------------ 3 wet areas
write("WET_AREA_SCHEDULE", "WET AREA SCHEDULE",
      ["ROOM", "NAME", "FLOOR", "FALL", "OUTLET", "WALL", "TANKING",
       "SKIRTING", "CEILING", "NOTE"],
      [("U-02", "Lavatory + medical", "F-02", "1:80", "GY-02 → PD-01",
        "W-02", "WP-04", "S-01 coved 150", "C-01",
        "Basin wastes discharge over the gully grating with an air gap"),
       ("U-05", "CBRN plant + sump", "F-02", "1:80", "direct to SU-01",
        "W-02", "WP-04", "S-01 coved 150", "C-01",
        "110 mm clear at the sides of each filter train — do not thicken the "
        "wall finish here"),
       ("U-06", "Decon airlock, 3 stages", "F-02", "1:80",
        "GY-06/07/08 SEGREGATED", "W-02", "WP-04", "S-01 coved 150", "C-01",
        "**The dirtiest surface in the shelter.** 50 mm upstand at W5 and at "
        "Blast Door 1 so no water reaches the clean zone"),
       ("G-03", "Stairwell platform", "F-06", "to the gully", "GY-10 → SU-02",
        "W-05", "WP-06", "S-03", "C-03",
        "C16 — the roof above is unresolved, 250 or 500. The finish does not "
        "depend on it; the drip at the junction does"),
       ("G-04", "Headhouse", "F-05", "**1:80 confirmed**", "GY-11 → external "
        "soakaway", "W-05", "WP-06", "S-02", "C-02",
        "Hose-down point. **Never to the clean sump** — confirmed instruction "
        "on the Rev F ground plan")],
      note=("**The 1:80 headhouse fall is the only floor fall confirmed "
            "anywhere in the project** (Rev F ground plan). Every other fall "
            "in this schedule is set by DRAINAGE calculation D.15 and is "
            "`[A]`.\n\n"
            "**Falls are formed in the screed, never cut into the 600 mat.** "
            "The screed build-up is 25 mm at the outlet rising to 78 mm at "
            "the far corner, area-average 52 mm — which exceeds the 1.0 kPa "
            "mat SIDL allowance by 0.24 kPa and is **referred to the "
            "structural engineer as finding DR-F4**."))

# ----------------------------------------------------------- 4 stairs
write("STAIR_FINISH_SCHEDULE", "STAIR FINISH SCHEDULE",
      ["ELEMENT", "MAIN STAIRCASE — U-07", "COVERED ENTRY STAIRWELL — G-02",
       "CLASS"],
      [(e, a, b, c) for e, a, b, c in F.STAIRS],
      note=("### THE MAIN STAIRCASE GEOMETRY IS FROZEN\n\n"
            "**24 risers @ 170.8333 mm · 280 mm tread · 3 flights × 8 · total "
            "rise 4100 mm · 1200 wide · 200 well · 200 waist · headroom "
            "2533 mm.** Landing levels L1 (−)4.7333 and L2 (−)3.3667 and the "
            "arrival landing at (−)6.100 go with it.\n\n"
            "**Nothing in this schedule alters any of it.** In particular the "
            "nosing is specified **cast in, not applied** — an applied nosing "
            "strip changes the effective going, and the going is frozen. The "
            "tread finish is specified with **no build-up at the nosing** for "
            "the same reason.\n\n"
            "Handrail height and continuity are an **NBC 2016 Part 4** "
            "requirement, not a finish decision. The 1100 guarding to the "
            "stair void edge in the headhouse is confirmed on the Rev F "
            "ground plan."))

# -------------------------------------------------------- 5 the four rules
write("FINISH_RULES", "THE FOUR RULES THAT GOVERN EVERY FINISH HERE",
      ["REF", "RULE", "WHY — and where it comes from"],
      [(r, ru, why) for r, ru, why in F.RULES],
      note=("These are not preferences. Each one follows from something the "
            "project or another package confirms, and each one changes what "
            "may be specified."))

# ------------------------------------------------- 6 what is not specified
write("FINISHES_DATA_REQUIRED", "WHAT IS NOT SPECIFIED, AND WHY",
      ["ITEM", "REASON", "CLASS"],
      [(i, r, c) for i, r, c in F.NOT_SPECIFIED],
      note=("**This table is the honest half of the package.** A finishes "
            "schedule that filled these in would be inventing a "
            "specification, not recording one. Every row here must be closed "
            "by the architect, the specialist or the client before anything "
            "is ordered."))

print(f"\n[written to] {DEST}")
