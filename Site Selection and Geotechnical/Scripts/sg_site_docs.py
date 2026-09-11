"""sg_site_docs.py  --  the SITE LAYOUT AND EXTERNAL WORKS section and its
schedules (revision SG2).

Everything is generated from sg_site.py, so the document, the schedules, the
calculation printout and the drawings all read the same positions and cannot
disagree.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import sg_proj as P                                        # noqa: E402
import sg_data as D                                        # noqa: E402
import sg_site as S                                        # noqa: E402

DOC = os.path.abspath(os.path.join(HERE, "..", "Documentation"))
SCH = os.path.abspath(os.path.join(HERE, "..", "Schedules"))
L = []


def w(s=""):
    L.append(s)


HEAD = (
    "**Underground CBRN-hardened protective structure — Pune** · "
    f"{P.GEOM_REV}\n"
    f"Site Selection and Geotechnical package revision **{S.REV}** · "
    f"{S.PACKAGE_DATE} · **{P.STATUS}**\n"
    "Evidence class: `[C]` confirmed · `[R]` reconstructed · `[D]` derived "
    "here · `[A]` assumed by this package · `[U]` unresolved · `[N]` not "
    "available — DATA REQUIRED\n"
)


def write_sched(name, title, header, rows, notes=(), pre=()):
    md = [f"# {title}", "", HEAD] + list(pre)
    md.append("| " + " | ".join(header) + " |")
    md.append("|" + "|".join("---" for _ in header) + "|")
    for r in rows:
        md.append("| " + " | ".join("" if c is None else str(c) for c in r)
                  + " |")
    if notes:
        md.append("")
        md += list(notes)
    md.append("")
    with open(os.path.join(SCH, name + ".md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))

    def esc(s):
        s = "" if s is None else str(s)
        for a, b in (("−", "-"), ("²", "2"), ("³", "3"), ("·", "-"),
                     ("—", "-"), ("’", "'"), ("“", '"'), ("”", '"'),
                     ("≥", ">="), ("×", "x"), ("**", ""), ("`", "")):
            s = s.replace(a, b)
        s = s.replace('"', '""')
        return f'"{s}"' if ("," in s or '"' in s) else s

    with open(os.path.join(SCH, name + ".csv"), "w", encoding="utf-8") as fh:
        fh.write(",".join(esc(h) for h in header) + "\n")
        for r in rows:
            fh.write(",".join(esc(c) for c in r) + "\n")
    print(f"  {name}.md / .csv   {len(rows)} rows")


# =====================================================================
def sched_external_works():
    rows = []
    for tag, kind, cx, cy, cls, serves in S.CIRCULAR:
        rows.append([f"**{tag}**", kind,
                     f"({cx:.0f}, {cy:.0f})",
                     f"{S.PIT_DIA:.0f} dia",
                     f"{-S.PIT_TOP:.0f} / {-S.PIT_INV:.0f}",
                     f"{S.side_area(S.PIT_DIA, S.PIT_EFF):.2f}",
                     f"`{cls}`", serves])
    for tag, kind, x0, y0, x1, y1, cls, note in S.RECTANGULAR:
        rows.append([f"**{tag}**", kind,
                     f"({(x0 + x1) / 2:.0f}, {(y0 + y1) / 2:.0f})",
                     f"{x1 - x0:.0f} × {y1 - y0:.0f}",
                     "—", "—", f"`{cls}`", note])
    write_sched("EXTERNAL_WORKS_SCHEDULE",
                "EXTERNAL WORKS SCHEDULE — POSITIONS FIXED BY SG2",
                ["TAG", "TYPE", "CENTRE (X, Y) mm", "SIZE mm",
                 "TOP / INVERT below local grade mm", "SIDE AREA m²",
                 "CLASS", "SERVES / NOTE"],
                rows,
                pre=["> Positions are in the **project coordinate system** "
                     "(master `A.4.1`), origin at the south-west corner of "
                     "the underground box, **+X = EAST, +Y = NORTH** "
                     "(orientation fixed by SG2). Master `H.9` recorded every "
                     "one of these as *“not determinable”*.\n",
                     "> **Pit levels are relative to LOCAL finished grade at "
                     "each pit**, not to the project datum — there is no "
                     "benchmark and the site fall is itself disputed "
                     "(`SG-V4`). That is also how a soak pit is actually "
                     "built.\n"],
                notes=[
                    "| | |", "|---|---|",
                    "| Foul group | **ST-01** septic tank → **SK-01** foul "
                    "soak pit. The furthest downgradient of everything |",
                    "| Clean group | **SK-02** storm · **SK-03** stairwell · "
                    "**SK-04** headhouse. Never combined with the foul — "
                    "S-06: *“STORM SOAKAWAY — CLEAN SUMP DISCHARGE. SEPARATE "
                    "FROM FOUL.”* |",
                    "| **SK-03 and SK-04 are RESERVED, not designed** | "
                    "Neither is sized anywhere in the project (`[C]`/`[N]`). "
                    "The 2.2 m footprint is reserved to the same construction "
                    "detail as SK-01/SK-02 so that whatever size is finally "
                    "adopted fits |",
                    "",
                    "**And the finding that matters more than any position "
                    "here — `SG2-F1`.** At this site a 3.5 m deep pit is "
                    "**21–43 % above the design water table** and its only "
                    "demonstrably permeable horizon is **0.2–0.5 m thick**. "
                    "The problem is **depth, not arithmetic**. SG2 does not "
                    "re-size SK-01 — the percolation test governs — but it "
                    "reserves **DF-1** and **DF-2** so the fallback needs a "
                    "redesign and not a re-siting. See `SG2_SITE_CALC_OUTPUT` "
                    "§S.6 and §S.7.",
                ])


def sched_pipes():
    rows = []
    for tag, frm, to, dn, grad, pts, cls, note in S.RUNS:
        if pts:
            Lr = S.run_length(pts)
            fall = (f"{Lr / float(grad.split(':')[1]):.0f} mm"
                    if ":" in grad else "pumped")
            rows.append([f"**{tag}**", frm, to, f"DN{dn}", grad,
                         f"**{Lr / 1000.0:.2f} m**", fall, f"`{cls}`",
                         f"{len(pts) - 1} legs"])
        else:
            rows.append([f"**{tag}**", frm, to, f"DN{dn}", grad,
                         "**`[U]`**", "—", f"`{cls}`",
                         "**ROUTE UNDETERMINED — `SG2-F5`**"])
    write_sched("EXTERNAL_PIPE_RUN_SCHEDULE",
                "EXTERNAL PIPE RUN SCHEDULE — THE FIVE LENGTHS MASTER H.9 "
                "CALLED “NOT DETERMINABLE”",
                ["TAG", "FROM", "TO", "DN", "GRADIENT", "LENGTH", "FALL",
                 "CLASS", "NOTE"],
                rows,
                pre=["> **Four of the five are now determined. The fifth "
                     "cannot be routed at all**, and the reason is a "
                     "coordination problem, not a siting one — `SG2-F5`.\n",
                     "> **No run crosses the engineered cover.** Master "
                     "`A.7.3` and `D-001` note 1: a pipe through the cover "
                     "breaches the radiation mass and the roof membrane. The "
                     "side **backfill** corridor, Y 6200–7200, is not the "
                     "cover and is a normal place for a service.\n"],
                notes=[
                    "**The common services trench.** `PD-06`, `PD-11` and "
                    "`PD-13` share one trench at Y 9800 from X 16500 "
                    "eastward — a DN100 gravity drain, two DN50 rising mains "
                    "and room for spare ducts. **That is what makes a 32 m "
                    "gravity run affordable where rockhead is 0.9–1.5 m: the "
                    "cost is the trench, and the trench is cut once.**",
                    "",
                    "**`PD-11` is routed WEST first**, to X 7500, because "
                    "going north from CP-10 would cross the stairwell "
                    "excavation (X 8250–16050). `IC-01` sits at that change "
                    "of direction, which is exactly what the chamber schedule "
                    "already says it is for.",
                ])


def sched_clearances():
    rows = []
    for name, val, cls, basis in S.CLEARANCES:
        rows.append([f"**{name}**", f"{val / 1000.0:.1f} m", f"`{cls}`",
                     basis])
    write_sched("SITING_CLEARANCE_SCHEDULE",
                "SITING CLEARANCE SCHEDULE — THE RULES, AND WHERE EACH COMES "
                "FROM",
                ["RULE", "VALUE", "CLASS", "BASIS"],
                rows,
                pre=["> Three rules are **`[C]`** — they are recorded on "
                     "sheet S-06 and reproduced in drainage calculation "
                     "`D.11`. Four are **`[A]`, adopted by this package**, "
                     "and each says why. Every check is computed in "
                     "`SG2_SITE_CALC_OUTPUT` §S.3 and §S.4 and **every one "
                     "passes**.\n"],
                notes=[
                    "**The one that cannot be demonstrated.** `D.11` ends "
                    "*“THOSE OFFSETS CANNOT BE DEMONSTRATED — no site plan, "
                    "no well position and no boundary exist in the project.”* "
                    "**Two of the three now can.** The third — **≥ 15 m from "
                    "any well** — cannot, because **no well position exists "
                    "anywhere in this project**. SG2 does not claim it is "
                    "met. `SG2-V1`",
                ])


def sched_openitems():
    rows = [
        ["`SG-V9`", "**CLOSED**", "The project has no coordinates",
         "**18.6089876 N, 73.8587287 E**, supplied by the project owner and "
         "recorded. The pin is taken as the **centre of the box** — an "
         "adopted convention `[A]`; if it meant a corner the layout "
         "translates rigidly and no offset changes"],
        ["`SG-V3`", "**RULED**", "The monsoon GWT monitoring is not in the "
         "monsoon",
         "**The owner does not accept the cost of moving it.** `A1080` stays "
         "12-11-26 → 04-12-26. **Consequence: it will not close `K.2 A2`**, "
         "and the design GWT `(−)2.000` stays `[ASSUMED]` through "
         "construction. Master `B.3` shows the **completed** structure passes "
         "even flooded to grade (FoS 1.41), so the permanent works are "
         "bounded; what is exposed is the **construction stage**, and B.3's "
         "mandatory mitigation becomes the operative control. `SG2-V5` opened"],
        ["`SG-V5`", "**AMENDED**", "Annual rainfall, 759.6 vs 500–600 mm",
         "**The SOIL REPORT is the figure that is wrong, not the deck's** — "
         "`SG2-F2`. Jun–Oct alone at Pune Shivajinagar averages **852.5 mm** "
         "over 42 years, which is 1.4–1.7× the report's whole *year*. The "
         "deck is the right order but its Jun–Oct total is 18 % low and its "
         "October figure still does not fit. **Stays open on a narrower "
         "question**; no IMD normal could be retrieved (all ten hosts refused "
         "by the session egress policy) and **none is invented**"],
        ["`SG-V1`", "unchanged", "The geotechnical data is off-site",
         "Still open. The layout's carry-across of the SEMT profile to this "
         "plot is `[A]` and is stated as such"],
        ["`SG-V2`", "unchanged", "Depth of investigation, ~1.5 m vs (−)6.800",
         "Still open — and **SG2 now says where the boreholes and the "
         "percolation tests have to go**, §S.8"],
        ["`SG-V4`", "unchanged", "Site level and fall disagree by 12–16 m",
         "Still open. It is why SG2 sets pit levels **relative to local "
         "grade** and not to the project datum"],
        ["`SG-V6`", "unchanged", "Entry stairwell raft in black cotton soil",
         "Still open"],
        ["`SG-V7`", "unchanged", "Concealment turf may be expansive clay",
         "Still open"],
        ["`SG-V8`", "unchanged", "Three deck statements not in the report",
         "Still open"],
        ["`SG-V10`", "unchanged", "Date of the SEMT field work not stated",
         "Still open"],
        ["`SG2-V1`", "**NEW**", "**No well position exists anywhere**",
         "The IS 2470 **≥ 15 m to any well** offset cannot be demonstrated. "
         "It is the one offset of the three that SG2 cannot close, and it is "
         "not fudged"],
        ["`SG2-V2`", "**NEW**", "**Distance to the perimeter fence**",
         "Recorded as the site's only SWOT weakness and **never dimensioned**. "
         "If the fence is closer than the reserve's east edge the whole "
         "reserve translates — no offset changes — but somebody has to say "
         "where it is"],
        ["`SG2-V3`", "**NEW**", "**SH-1, the fresh-air intake, has no plan "
         "position**",
         "The HVAC schedule gives SH-2 an X range and gives SH-1 only *“West "
         "of the box”*. **The fresh-air intake of a CBRN shelter is not a "
         "minor fitting**; until it has a coordinate no intake separation can "
         "be checked against anything, the septic vent included. `SG2-F4`"],
        ["`SG2-V4`", "**NEW**", "**No wind direction data anywhere — no wind "
         "rose**",
         "The deck gives monthly mean **speed** only. It matters for the "
         "intake/exhaust relationship **and** as the plume direction for the "
         "CBRN case. SG2's orientation is therefore justified on access, "
         "fall, noise and end-to-end separation — **not** on prevailing wind"],
        ["`SG2-V5`", "**NEW**", "**The programme stops dewatering before "
         "backfill**",
         "`A2070` ends 11-05-27; side backfill `A7010` is 20-07-27 → "
         "30-07-27. Master `B.3` mitigation 1 requires dewatering *“until "
         "backfill and cover complete”*. The gap spans the **2027 monsoon** "
         "with the box at stage 3 — FoS **1.22** at the design GWT, **0.86 "
         "flooded**. Sharpened by the `SG-V3` ruling. No date changed — the "
         "owner's schedule R0 governs"],
    ]
    write_sched("SG2_OPEN_ITEM_STATUS",
                "OPEN ITEM STATUS AFTER SG2",
                ["REF", "STATUS", "ITEM", "WHAT SG2 DID"],
                rows,
                pre=["> **Two closed or ruled by the project owner, one "
                     "amended, five new.** Everything else SG1 opened stands "
                     "exactly as it stood.\n"])


# =====================================================================
def report():
    e = S.EWR
    a = S.RAIN_ANCHOR
    deck = dict(D.DECK_PRECIP)
    deck_jo = sum(v for m, v in D.DECK_PRECIP
                  if m in ("June", "July", "August", "September", "October"))

    w("# SITE LAYOUT AND EXTERNAL WORKS")
    w("### Where the septic tank and the soak pits go, and why")
    w()
    w(f"**Package** `Site Selection and Geotechnical/` · **revision "
      f"{S.REV}** · **{S.PACKAGE_DATE}** · {P.GEOM_REV}")
    w(f"**Status — {P.STATUS}.**")
    w()
    w("**Evidence class:** `[C]` confirmed · `[R]` reconstructed · `[D]` "
      "derived here · `[A]` assumed by this package · `[U]` unresolved · "
      "`[N]` not available — DATA REQUIRED")
    w()
    w("---")
    w()
    w("## 1. What changed, and why that unblocks this")
    w()
    w("Master `H.9` recorded the positions of the soakaways, the septic tank "
      "and the external chambers as **not determinable** — *“no site plan, "
      "boundary or contour exists”* — and with them **five pipe lengths** and "
      "the **IS 2470 (Pt 2) offsets**. Drainage calculation `D.11` ends on "
      "the same sentence. That has been the position since DR1 on 5 September.")
    w()
    w("The project owner has now supplied the two things that were missing:")
    w()
    w("| | | |")
    w("|---|---|---|")
    w(f"| **Coordinate** | **{S.PIN_LAT} N, {S.PIN_LON} E** | `[C]` owner |")
    w("| **Availability** | *“the area around 50 m is all available”* | "
      "`[C]` owner |")
    w()
    w("With those, plus SG1's contours and geotechnical profile and the "
      "project's own confirmed geometry, **the positions can be determined**. "
      "This section determines them.")
    w()
    w("> ### The pin convention, stated so it can be corrected")
    w("> One point was given for *“the project site”*. The only "
      "self-consistent reading that lets everything be dimensioned is that it "
      f"is the **centre of the underground box**, project "
      f"`({S.PIN_AT[0]:.0f}, {S.PIN_AT[1]:.0f})`. That is adopted as a "
      "**convention `[A]`**, not claimed as a finding. **If it was meant as a "
      "corner or the entrance, the whole layout translates rigidly and not "
      "one offset, length or clearance below changes.**")
    w()

    # ------------------------------------------------------------- 2
    w("## 2. Site orientation — fixed by this revision")
    w()
    w(f"### Project **+X = {S.ORIENT_X}**, project **+Y = {S.ORIENT_Y}** `[A]`")
    w()
    w("The project has worked in a local frame since Rev F (master `A.4.1`) "
      "and has **never been tied to north**. Five reasons, all pointing the "
      "same way:")
    w()
    w("| # | Reason |")
    w("|---|---|")
    w("| 1 | **Access.** The covered entry stairwell's grade door is at its "
      "**west** end, X 9250 (`A.4.7`), so the approach comes from the west — "
      "and the CTW blocks, the roads and the campus are west of the plot "
      "(deck slides 13, 14, 17). **The entry faces the installation it "
      "serves.** |")
    w("| 2 | **Fall.** SG1 read the ground as falling **east / north-east**, "
      "580 → 575. With +X east the drainage field is **downgradient**, so "
      "nothing recharges the ground upslope of a flotation-critical tanked "
      "box. |")
    w("| 3 | **Intake and exhaust at opposite ends.** SH-1, the fresh-air "
      "intake, is west of the box; SH-2, the generator air shaft, is at "
      "X 22598–23198, east. **22.6 m apart at minimum.** |")
    w("| 4 | **Noise and signature.** Bay 8 — the generator, ESC 2, SH-2, "
      "BV-4/BV-5 — is at the east end, away from the campus. |")
    w("| 5 | The **sentry post** covers the approach from the north. |")
    w()
    w("> **And the limit on reason 3, stated plainly.** **No wind direction "
      "data exists anywhere in this project.** The deck gives monthly mean "
      "*speed* and no direction; there is no wind rose. So the orientation is "
      "**not** justified on prevailing wind. What it does instead is put the "
      "intake and the exhaust at **opposite ends of a 22 m box**, which is "
      "the robust choice whatever the wind does. A wind rose matters for more "
      "than this — it is also the **plume direction for the CBRN case** — and "
      "it is opened as **`SG2-V4`**.")
    w()

    # ------------------------------------------------------------- 3
    w("## 3. The external works reserve")
    w()
    w(f"**X {e['x0']:.0f} → {e['x1']:.0f}, Y {e['y0']:.0f} → {e['y1']:.0f}** "
      f"— {(e['x1'] - e['x0']) / 1000.0:.1f} m × "
      f"{(e['y1'] - e['y0']) / 1000.0:.1f} m = "
      f"{(e['x1'] - e['x0']) * (e['y1'] - e['y0']) / 1e6:.0f} m², "
      f"**{(e['x0'] - 23000) / 1000.0:.1f} m clear of the main excavation's "
      f"east face**, and entirely inside the 50 m envelope (worst corner "
      f"{max(S.radius_from_pin(x, y) for x in (e['x0'], e['x1']) for y in (e['y0'], e['y1'])) / 1000.0:.1f} m).")
    w()
    w("**Everything in one reserve, on the downgradient side.** Four reasons:")
    w()
    w("1. **Nothing recharges the ground upslope or alongside the box.** The "
      "box is flotation-critical — FoS **0.33** at the mat-only stage — and "
      "its side backfill is selected granular fill at 95 % MDD, which is "
      "**more permeable than the basalt around it**. Effluent released near "
      "it would run preferentially *into* the backfill and down the outside "
      "of the tanking. That is the single worst thing this layout could do, "
      "and putting the whole field 11–22 m downgradient is what prevents it.")
    w("2. **One percolation-test location, one keep-clear zone, one reserved "
      "fallback.**")
    w("3. **One trench.** `PD-06`, `PD-11` and `PD-13` share a common "
      "services trench at Y 9800. Where rockhead is 0.9–1.5 m the cost is the "
      "trench, and the trench is cut once — which is what makes a 32 m "
      "gravity run sensible.")
    w("4. **Concealment.** Four RC cover slabs and a 2 m septic vent are new "
      "at-grade signatures. Grouped 11–22 m away and downgradient, **they "
      "mark the drainage field, not the shelter** — which is better for "
      "`CAM2` than scattering them around the structure.")
    w()
    w("> **The layout is anchored to confirmed geometry only.** Every "
      "position is dimensioned from the underground box, whose geometry is "
      "`[C]` throughout. **Nothing is dimensioned from the sentry post**, "
      "whose site position is `[ASSUMED]` (master `U4`) — so the layout "
      "survives U4 being resolved differently. And every offset is "
      "**relative**: if the perimeter fence turns out to be closer than the "
      "reserve's east edge, **the whole reserve translates and not one offset "
      "changes**.")
    w()

    # ------------------------------------------------------------- 4
    w("## 4. The positions")
    w()
    w("| Tag | Type | Centre (X, Y) | Size | Serves |")
    w("|---|---|---|---|---|")
    for tag, kind, cx, cy, cls, serves in S.CIRCULAR:
        w(f"| **{tag}** | {kind} | ({cx:.0f}, {cy:.0f}) | "
          f"{S.PIT_DIA:.0f} dia × {S.PIT_EFF:.0f} eff | {serves} |")
    for tag, kind, x0, y0, x1, y1, cls, note in S.RECTANGULAR:
        w(f"| **{tag}** | {kind} | ({(x0 + x1) / 2:.0f}, "
          f"{(y0 + y1) / 2:.0f}) | {x1 - x0:.0f} × {y1 - y0:.0f} | "
          f"{note.split('.')[0]} |")
    w()
    w(f"Pit levels, **relative to local finished grade at each pit** — there "
      f"is no benchmark and the site fall is itself disputed (`SG-V4`), and "
      f"this is how a soak pit is built anyway: underside of cover slab "
      f"**{-S.PIT_TOP:.0f} mm** below grade, invert **{-S.PIT_INV:.0f} mm** "
      f"below grade, effective depth **{S.PIT_EFF:.0f} mm** `[C]` unchanged "
      f"from RC1.")
    w()
    w("**`SK-03` and `SK-04` are reserved, not designed.** Neither is sized "
      "anywhere in the project (`[C]`/`[N]` in the drainage package). Their "
      "2.2 m footprints are reserved to the same construction detail as "
      "SK-01/SK-02, so whatever size is finally adopted fits.")
    w()

    # ------------------------------------------------------------- 5
    w("## 5. The offsets, demonstrated")
    w()
    w("Drainage `D.11` records three offsets from S-06 and then says: "
      "*“**THOSE OFFSETS CANNOT BE DEMONSTRATED** — no site plan, no well "
      "position and no boundary exist in the project.”*")
    w()
    st = [r for r in S.RECTANGULAR if r[0] == "ST-01"][0]
    st_rect = (st[2], st[3], st[4], st[5])
    sk01 = [c for c in S.CIRCULAR if c[0] == "SK-01"][0]
    d_tank = S.dist_circle_rect(sk01[2], sk01[3], S.PIT_DIA, st_rect)
    w("| Offset | Required | Achieved | Status |")
    w("|---|---|---|---|")
    w(f"| Foul soak pit → septic tank | ≥ 5 m `[C]` | **{d_tank / 1000.0:.2f} "
      f"m** | **DEMONSTRATED** |")
    w("| Soak pit → any building | ≥ 2 m `[C]` | **10.97 m** (nearest "
      "approach anywhere) | **DEMONSTRATED**, 5.5× over |")
    w("| Foul soak pit → any well | ≥ 15 m `[C]` | — | **CANNOT BE "
      "DEMONSTRATED — no well position exists anywhere in this project.** "
      "`SG2-V1` |")
    w()
    w("Plus four rules this package adopts, each with its reason, and every "
      "check passing — see `SITING_CLEARANCE_SCHEDULE` and calculation §S.4. "
      "The tightest are **foul group to any excavation face 15.49 m** "
      "(adopted ≥ 15) and **pit wall to pit wall 4.20 m** (adopted ≥ 4).")
    w()

    # ------------------------------------------------------------- 6
    w("## 6. The five pipe lengths")
    w()
    w("| Tag | From | To | DN | Gradient | **Length** | Fall |")
    w("|---|---|---|---|---|---|---|")
    for tag, frm, to, dn, grad, pts, cls, note in S.RUNS:
        if pts:
            Lr = S.run_length(pts)
            fall = (f"{Lr / float(grad.split(':')[1]):.0f} mm"
                    if ":" in grad else "pumped")
            w(f"| **{tag}** | {frm} | {to} | DN{dn} | {grad} | "
              f"**{Lr / 1000.0:.2f} m** | {fall} |")
        else:
            w(f"| **{tag}** | {frm} | {to} | DN{dn} | {grad} | "
              f"**`[U]`** | — |")
    w()
    w("**Four of the five are determined. The fifth cannot be routed at "
      "all** — see `SG2-F5` below. No run crosses the engineered cover; the "
      "side backfill corridor at Y 6200–7200 is not the cover and is a normal "
      "place for a service.")
    w()

    # ------------------------------------------------------------- 7
    w("## 7. `SG2-F1` — the soak pit will not work as a deep pit, and the "
      "site data now says so")
    w()
    w("RC1 fixed the **arithmetic** of SK-01 (C19: widened 2.0 → 2.200 dia, "
      "24.19 m² against 22.50 required). It also wrote the sentence this "
      "section starts from:")
    w()
    w("> *“deepening drives the pit further below the design GWT at "
      "`(−)2.000`, **where it cannot soak at all**.”*")
    w()
    w("So the project has known since RC1 that the pit is below the water "
      "table. **Nobody has ever quantified by how much.** SG1 supplied the "
      "missing half — the measured ground profile — so it can be.")
    w()
    w("### Check 1 — how much of it is above the design water table?")
    w()
    w("The project holds **two readings** of the design GWT, and 28 m east on "
      "falling ground they are not the same thing: the **absolute** level "
      "`(−)2.000` (master `A.6`), and **“2 m below GL”** (deck slide 29). "
      "Both bounds are computed:")
    w()
    w("| Reading | Water below local grade | Wet depth | Area **above** | of "
      "22.50 m² |")
    w("|---|---|---|---|---|")
    for label, dw in (("Absolute `(−)2.000`, reserve ≈ 0.70 m lower", 1300.0),
                      ("Relative, 2 m below local grade", 2000.0)):
        dry = max(0.0, dw + S.PIT_TOP)
        ar = S.side_area(S.PIT_DIA, dry)
        w(f"| {label} | {dw / 1000.0:.2f} m | "
          f"{(S.PIT_EFF - dry) / 1000.0:.2f} m | **{ar:.2f} m²** | "
          f"**{ar / 22.50:.1%}** |")
    w()
    w("> **Between 21 % and 43 % of the required absorption area lies above "
      "the design water table.** The rest is, by the project's own design "
      "assumption, permanently submerged — and a submerged wall does not "
      "infiltrate: there is no unsaturated storage to receive the effluent "
      "and no head to drive it. **This is geometry against a stated design "
      "level. It does not depend on the percolation rate at all.**")
    w()
    w("### Check 2 — and what is the rest of it cut through?")
    w()
    w("| Location | Broken-rock band | Thickness | Side area in it | of "
      "22.50 m² |")
    w("|---|---|---|---|---|")
    for loc, layers in D.FINDINGS:
        br = [l for l in layers if "Broken" in l[1]]
        if not br:
            continue
        lo, hi = [float(t) for t in br[0][0].replace("m", "").split("-")]
        ar = S.side_area(S.PIT_DIA, (hi - lo) * 1000.0)
        w(f"| {loc} | {lo:.2f} – {hi:.2f} m | {hi - lo:.2f} m | "
          f"**{ar:.2f} m²** | **{ar / 22.50:.1%}** |")
    w()
    w("Above the broken rock: **black cotton CH at FSI 60–65 %** — it swells "
      "shut when wet — over **murrum, which the deck's own slide 30 calls "
      "*“impervious in nature”***. Below it: **sound basalt**, whose matrix "
      "permeability is effectively zero; whatever it takes, it takes through "
      "**joints**, and no joint data exists — no RQD, no packer test "
      "(`SG-V2`).")
    w()
    w("> **The only demonstrably permeable horizon is 0.2–0.5 m thick and "
      "contributes 15 % or less of the required area.**")
    w()
    w("### The conclusion")
    w()
    w("> **`SG2-F1`. SK-01's shortfall was never an arithmetic problem — RC1 "
      "fixed that. It is a DEPTH problem.** A 3.5 m deep pit at this site is "
      "mostly below the design water table and mostly in sound basalt. **The "
      "form that fits this ground is shallow and wide, not deep and narrow** "
      "— a dispersion trench worked in the 0.5–1.6 m broken-rock horizon, "
      "*above* the water table. Which is exactly **IS 2470 (Pt 2) Cl. 5**, "
      "the fallback master `K.2 A7` has named all along.")
    w()
    w("**SG2 does not change SK-01.** The percolation test governs the final "
      "size and form — master `A7`, and RC1 said so too. What SG2 does is "
      "**(i)** say the number *before* the test rather than after it, and "
      "**(ii)** reserve the ground for the fallback.")
    w()

    # ------------------------------------------------------------- 8
    w("## 8. The fallback, reserved")
    w()
    w("A dispersion trench is sized on the **same basis this project uses for "
      "the pit**: side area only, base discounted because it clogs. A trench "
      "of effective depth *h* gives 2*h* m² per metre run.")
    w()
    w("| Field | Reserved | Trenches at 2.5 m centres | Side area | Serves "
      "its stream down to |")
    w("|---|---|---|---|---|")
    per_m = 2.0
    for tag, x0, y0, x1, y1, what in S.FALLBACK:
        wd, ht = x1 - x0, y1 - y0
        runs = int((ht - 1000.0) // 2500.0) + 1
        total = runs * wd / 1000.0
        area = total * per_m
        q = 450.0 if "FOUL" in tag else 400.0
        w(f"| **{tag.split()[0]}** {tag.split(maxsplit=1)[1]} | "
          f"{wd / 1000.0:.1f} × {ht / 1000.0:.1f} m | {runs} × "
          f"{wd / 1000.0:.1f} m = {total:.1f} m | {area:.0f} m² | "
          f"**{q / area:.2f} L/m²/day = {q / area / 20.0:.0%} of the assumed "
          f"20** |")
    w()
    w("> **The reserve carries both streams at roughly a quarter to a third "
      "of the assumed absorption rate.** That is the point of reserving it: "
      "the percolation test can come back badly and the answer is still a "
      "**redesign inside the same footprint**, not a new hunt for ground.")
    w()
    w("If even that fails — and on sound basalt it can — the remaining "
      "answers are a **sealed holding tank emptied on a schedule** (master "
      "`A7`'s own words) or a **positive outfall**, and a positive outfall "
      "needs the final-discharge question answered, which is `D3` and is "
      "still open.")
    w()

    # ------------------------------------------------------------- 9
    w("## 9. Where the percolation test has to be done")
    w()
    w("Master `K.2 A7` makes it **mandatory** (IS 2470 Pt 2 Cl. 4). Drainage "
      "`D.12` calls it *“on the critical path for three independent "
      "reasons”*. **Nobody has ever said where**, and a percolation test in "
      "the wrong place or at the wrong depth answers nothing.")
    w()
    w("| Ref | Position | Depth | What it decides |")
    w("|---|---|---|---|")
    for ref, x, y, what in S.PERC_TESTS:
        w(f"| **{ref}** | ({x:.0f}, {y:.0f}) | to **{-S.PERC_DEPTH / 1000.0:.3f} "
          f"m** below local grade, the proposed pit invert | {what} |")
    w()
    w("> **And test the shallow horizon too.** §7 shows the deep pit is "
      "mostly submerged and mostly in sound basalt, and §8 shows the fallback "
      "is a trench at about 1.5 m. A test taken **only** at `(−)4.100` "
      "measures the formation the fallback will not use. **Take each test at "
      "both depths** — the pit invert and the trench invert — or the fallback "
      "is undesigned the day the pit is abandoned. `[A]`")
    w()
    w("The same boreholes serve `SG-V2`: `A1075` must be located **on this "
      "plot**, and the standpipe `SG-V3` asks for goes in one of them.")
    w()

    # ------------------------------------------------------------ 10
    w("## 10. `SG-V3` ruled — and what the ruling leaves standing")
    w()
    w("> **Ruling, 11 September 2026: the cost of moving the groundwater "
      "monitoring is not accepted.**")
    w()
    w("**Reading.** `SG-F7` showed that WBS `A1080` runs 12-11-26 → 04-12-26, "
      "which is not the monsoon, and that moving it would move a "
      "critical-path activity and therefore the job. The ruling declines "
      "**that cost**. `A1080` stays where it is. *If the owner meant "
      "something wider, this reading is stated so it can be corrected.*")
    w()
    w("**Consequence, stated honestly.** `A1080` as programmed will measure "
      "the post-monsoon **recession**. It will therefore **not close master "
      "`K.2 A2`**. The design GWT `(−)2.000` stays `[ASSUMED]` through "
      "construction and into service.")
    w()
    w("**And why the permanent works are still bounded.** `(−)2.000` is only "
      "2 m down, which is the conservative direction for everything the water "
      "drives. The risk left open is that the real table is **higher** — and "
      "master `B.3` has already run that bound:")
    w()
    w("| Stage | FoS @ `(−)2.000` | FoS **flooded to grade** |")
    w("|---|---|---|")
    w("| 1 mat cast only | 0.33 FAIL | 0.23 FAIL |")
    w("| 2 mat + walls, no roof | 0.78 FAIL | 0.55 FAIL |")
    w("| 3 box complete, no backfill | 1.22 MARGINAL | **0.86 FLOATS** |")
    w("| 4 backfilled + cover | 2.02 OK | **1.41 OK** |")
    w()
    w("> **The completed structure passes even with the water at ground "
      "level** — FoS 1.41 against a requirement of 1.2. The ruling does not "
      "put the permanent works at risk.")
    w()
    w("**What it does expose is the construction stage**, and that is now the "
      "operative control. Master `B.3`'s mandatory mitigation becomes "
      "non-negotiable rather than advisory: continuous dewatering until "
      "backfill *and cover* are complete; the six pressure-relief plugs "
      "grouted only after backfill; sub-structure before the monsoon or a "
      "bunded, positively drained excavation with standby pumping; and "
      "symmetrical backfill.")
    w()
    w("> **`SG2-V5` — and the programme does not do the first of those.** "
      "`A2070`, *“Dewatering — continuous through the substructure works”*, "
      "runs 01-01-27 → **11-05-27**. Side backfill `A7010` runs 20-07-27 → "
      "30-07-27 and the burster slab is not cast until 21-08-27. **So "
      "dewatering stops on 11 May and the box stands un-backfilled through "
      "the whole 2027 monsoon — stage 3, FoS 1.22 at the design GWT and 0.86 "
      "flooded.** No date is changed here; the owner's schedule R0 governs "
      "(master `H.13`).")
    w()
    w("**One option the ruling does not preclude, because it costs no "
      "float.** A standpipe piezometer left in the `A1075` borehole and read "
      "weekly by staff already on site is a **level-of-effort** observation, "
      "exactly like `A2070` itself. It cannot verify the design in time — the "
      "mat is cast in February — but through the 2027 monsoon it measures the "
      "water the flotation case is actually exposed to, **while the box is "
      "standing at FoS 1.22**. Offered, not adopted. `[A]`")
    w()

    # ------------------------------------------------------------ 11
    w("## 11. `SG-V5` amended — rainfall, and which figure is the wrong one")
    w()
    w("**What actually happened, recorded so it can be checked.** Ten hosts "
      "were probed from this session and **all ten were refused by the "
      "environment's egress policy (HTTP 403)**: `imd.gov.in`, "
      "`imdpune.gov.in`, `mausam.imd.gov.in`, `data.gov.in`, "
      "`tropmet.res.in`, `en.wikipedia.org`, `en.climate-data.org`, "
      "`power.larc.nasa.gov`, `climexp.knmi.nl`, `ncei.noaa.gov`. "
      "**No IMD normal was retrieved and none is invented.**")
    w()
    w("One published figure with a **named station and a named period** was "
      "obtained, and it is enough to settle which of the project's two "
      "figures is wrong:")
    w()
    w(f"> **{a['season']} mean at {a['station']}, {a['period']}: "
      f"{a['value']} mm.** {a['cls']}")
    w(f"> Source: {a['source']}.")
    w()
    w("| Source | Jun–Oct | Annual | Verdict |")
    w("|---|---|---|---|")
    w(f"| Shivajinagar 42-year mean | **{a['value']:.1f} mm** | — | the "
      f"yardstick |")
    w(f"| P1 deck slide 25 | {deck_jo:.1f} mm | {sum(deck.values()):.1f} mm | "
      f"**{deck_jo / a['value'] - 1:+.0%}** on Jun–Oct |")
    w(f"| SEMT/67/15 para 9 | — | "
      f"{D.RAINFALL_REPORT_RANGE[0]:.0f}–{D.RAINFALL_REPORT_RANGE[1]:.0f} mm "
      f"| **untenable — see below** |")
    w()
    w("> **`SG2-F2`. The soil report's rainfall figure is the one that is "
      "wrong, not the deck's.** SEMT para 9 gives "
      f"{D.RAINFALL_REPORT_RANGE[0]:.0f}–{D.RAINFALL_REPORT_RANGE[1]:.0f} mm "
      f"for the **annual** rainfall of *“the region”*. The **June-to-October "
      f"mean alone** at the nearest long-record observatory is "
      f"**{a['value']:.1f} mm** — "
      f"**{a['value'] / D.RAINFALL_REPORT_RANGE[1]:.1f} to "
      f"{a['value'] / D.RAINFALL_REPORT_RANGE[0]:.1f} times the report's "
      f"whole year**. A figure that small is not a Pune figure.")
    w()
    w("SG1 raised this as a straight conflict between two documents and could "
      "not say which side was wrong. **It can now — and the correction runs "
      "the other way from the first guess:** the deck is the right *order*, "
      "and the soil report is not.")
    w()
    w(f"The deck is not vindicated, though. Its Jun–Oct total of "
      f"{deck_jo:.1f} mm is **{1 - deck_jo / a['value']:.0%} below** the "
      f"42-year Shivajinagar mean, and its October figure — "
      f"{deck['October']:.1f} mm, {deck['October'] / deck['September']:.2f}× "
      f"September and above August — still does not fit a Deccan monsoon. "
      f"**Both the annual total and the October value still need the real "
      f"normal. `SG-V5` stays open, on a narrower question.**")
    w()
    w("**What to ask for, exactly:**")
    w()
    for s in S.RAIN_AUTHORITY:
        w(f"- {s}")
    w()
    w("### And the part that decides how much this matters")
    w()
    w("> **Not one pipe, pit, pump or structure in this project is sized by "
      "rainfall.**")
    w()
    w("- The roofs and the 2 000 engineered cover **shed at grade** to the "
      "berm toe. Drainage `D.7`: *“there is no roof outlet, no downpipe and "
      "no rainwater pipe on the buried roof”*. The 2.461 L/s at 50 mm/h "
      "**never enters a pipe**.")
    w("- The only rainwater that does enter a pipe is `CH-10 → CP-10 → "
      "PD-11`, and `DR-C1` ruled that catchment is the **door-open "
      "driving-rain** case, about 12× smaller than the superseded 0.10 L/s — "
      "order **0.008 L/s** against a DN100 at 1:100 carrying 6.72 L/s.")
    w("- The stairwell sump `SU-02` is sized on a **1 000 L event volume** "
      "`[C]`, not on an intensity.")
    w()
    w("So the rainfall conflict **governs what the design report may claim, "
      "and — through the monsoon window — when things can be built. That is "
      "the whole of its reach**, and it is worth saying plainly so nobody "
      "re-sizes a pipe on the back of a corrected rainfall table. The "
      "intensity question `DR-D1` is separate and is **not** closed: a "
      "monthly total can never supply a short-duration intensity.")
    w()

    # ------------------------------------------------------------ 12
    w("## 12. What the siting work surfaced in other packages")
    w()
    w("Four things. Each is recorded and referred; **none is acted on.**")
    w()
    w("| Ref | Finding |")
    w("|---|---|")
    w("| **`SG2-F3`** | **ST-01 is sized for a building that is not connected "
      "to it.** The tank is sized for 10 users, *“sentry-post shift crews + "
      "shelter maintenance”* `[C]` S-06. The drainage package excludes the "
      "sentry post from its scope, and **there is no pipe from the sentry "
      "post to ST-01 anywhere in the project** — the schedule has `PD-15` "
      "(Bay 2, Case B only, not adopted) and `PD-16` (ST-01 → SK-01) and "
      "nothing upstream of the tank at all. SG2 positions ST-01 and leaves "
      "the connection to the drainage engineer; the layout does not prejudge "
      "it — ST-01 is 22.5 m from the assumed sentry position with clear "
      "ground between. |")
    w("| **`SG2-F4`** | **SH-1 has no plan position.** The HVAC equipment "
      "schedule gives SH-2 an X range (22598–23198) and gives SH-1 only "
      "*“West of the box”*. **The fresh-air intake of a CBRN shelter is not a "
      "minor fitting.** Until it has a coordinate, no intake separation can "
      "be checked against anything — the septic vent included. What protects "
      "it here is the layout, not a calculation: the reserve is **east** and "
      "SH-1 is **west**, so the separation is at least 33 m however SH-1 is "
      "finally placed. `SG2-V3` |")
    w("| **`SG2-F5`** | **`PD-14` cannot be routed.** `GY-11` sits at "
      "(14700, 1960) with its invert at `(−)2.150`, and the headhouse floor "
      "**is** the top of the 900 pressure slab at `(−)2.000` (master "
      "`A.4.6`). The gully body and its outlet are therefore **150 mm inside "
      "the pressure slab**; outside the headhouse walls that level is beneath "
      "the waterproof membrane and within the engineered cover, which no pipe "
      "may enter. **SK-04's footprint is reserved; its pipe is not routed.** "
      "Referred to drainage and structures together. |")
    w("| **`SG2-V5`** | **The programme stops dewatering before backfill** — "
      "see §10. |")
    w()

    # ------------------------------------------------------------ 13
    w("## 13. Master gap `D3` — what is now closed and what is not")
    w()
    w("`D3` has been cited as a blocker across six packages. It was never one "
      "thing. Splitting it:")
    w()
    w("| # | What D3 was blocking | Status after SG2 |")
    w("|---|---|---|")
    for n, what, st in [
        ("1", "Positions of the soakaways and the septic tank",
         "**CLOSED**"),
        ("2", "The five “not determinable” pipe lengths",
         "**FOUR CLOSED**, `PD-14` `[U]` — `SG2-F5`"),
        ("3", "External chamber positions `IC-01`, `IC-02`", "**CLOSED**"),
        ("4", "IS 2470 offset to the septic tank, ≥ 5 m",
         "**DEMONSTRATED — 5.40 m**"),
        ("5", "IS 2470 offset to any building, ≥ 2 m",
         "**DEMONSTRATED — 5.5× over**"),
        ("6", "IS 2470 offset to any well, ≥ 15 m",
         "**STILL OPEN** — no well exists. `SG2-V1`"),
        ("7", "A concealment *layout* (`CAM2` / `CAM-V2`)", "**PARTLY**"),
        ("8", "Berm, access and hardstanding layout",
         "**STILL OPEN** — needs levels"),
        ("9", "Cut and fill for a level formation",
         "**STILL OPEN** — needs levels, `SG-V4`"),
        ("10", "The final discharge question — is any outfall available?",
         "**STILL OPEN** — D3 proper"),
        ("11", "Sentry post site position (`U4`)",
         "**STILL OPEN** — and nothing here depends on it"),
    ]:
        w(f"| {n} | {what} | {st} |")
    w()
    w("> **`D3` is PARTIALLY closed, not closed. The layout now exists. The "
      "survey does not.** What is still missing — a boundary, a benchmark and "
      "spot levels, the well, the fence distance, existing services on the "
      "plot, a wind rose — is every one of it a **survey** output, and none "
      "of it moves anything SG2 has fixed: the layout is dimensioned from "
      "confirmed structure geometry and every clearance is relative.")
    w()
    w("**On concealment.** `CAM2` could not draw a layout and still cannot "
      "draw a full one. But SG2 fixes where the new **at-grade signatures** "
      "go — four RC cover slabs and a 2 m septic vent — and puts them 11–22 m "
      "from the structure, in one group, downgradient and away from the "
      "approach. **The covers mark the drainage field, not the shelter.** "
      "`CAM-V2` is unaffected: it is a client ruling on whether the "
      "above-ground signature is acceptable at all.")
    w()

    # ------------------------------------------------------------ 14
    w("## 14. What this revision changed, and what it did not")
    w()
    w("| | |")
    w("|---|---|")
    w("| Design values in Parts A, B, D, F, L | **untouched** |")
    w("| **SK-01's size** | **untouched** — RC1's 2.200 dia × 3.500 stands. "
      "The percolation test governs |")
    w("| BOQ quantities, rates, dates, floats | **untouched** — WM2 governs |")
    w("| `.std` models | **untouched — STAAD.Pro was not run** |")
    w("| Any file in any other package | **untouched** |")
    w("| **The main staircase** | **untouched — frozen** |")
    w("| Any `[ASSUMED]` tag | **not one converted, downgraded or deleted** |")
    w()
    w("**Added:** this section, four schedules, a calculation printout "
      "(§S.1–S.12), and two A1 drawings — `SG-102`, the project's **first "
      "true site layout plan**, and `SG-202`, the external works siting and "
      "the soak pit finding.")
    w()
    w("---")
    w()
    w(f"*Site Selection and Geotechnical package, revision **{S.REV}**, "
      f"{S.PACKAGE_DATE}. Every value is tagged. The positions are fixed; the "
      f"survey that would confirm them is not. Nothing that was assumed has "
      f"been made confirmed.*")
    w()


def main():
    os.makedirs(DOC, exist_ok=True)
    os.makedirs(SCH, exist_ok=True)
    del L[:]
    report()
    with open(os.path.join(DOC, "SITE_LAYOUT_AND_EXTERNAL_WORKS.md"), "w",
              encoding="utf-8") as f:
        f.write("\n".join(L))
    print("SG2 documentation:")
    print(f"  SITE_LAYOUT_AND_EXTERNAL_WORKS.md   {len(L)} lines")
    print("SG2 schedules:")
    sched_external_works()
    sched_pipes()
    sched_clearances()
    sched_openitems()


if __name__ == "__main__":
    main()
