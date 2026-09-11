"""sg_docs.py  --  the SITE SELECTION AND GEOTECHNICAL section, the README and
the drawing index.

The report is written here rather than typed by hand so that every number in
it comes from sg_data.py (transcription) or is computed on the spot from it.
The document, the schedules, the calculation printout and the drawings cannot
disagree, because they all read the same module.
"""
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import sg_proj as P                                        # noqa: E402
import sg_data as D                                        # noqa: E402

DOC = os.path.abspath(os.path.join(_HERE, "..", "Documentation"))
L = []


def w(s=""):
    L.append(s)


def kpa(v):
    return v * P.KGCM2_KPA


# ---------------------------------------------------------------- derived
PRECIP_TOTAL = sum(v for _, v in D.DECK_PRECIP)
PRECIP = dict(D.DECK_PRECIP)
JUN_SEP = sum(v for m, v in D.DECK_PRECIP
              if m in ("June", "July", "August", "September"))
HEADS = [float(l[-1][0].replace("Below", "").replace("m", "").strip())
         for _, l in D.FINDINGS]
RH_LO, RH_HI = min(HEADS), max(HEADS)
DEEPEST = RH_HI
AREA = P.WM_ROCK_M3 / (-P.LVL_FORMATION - 1.750)
ROCK_LO = AREA * (-P.LVL_FORMATION - RH_HI)
ROCK_HI = AREA * (-P.LVL_FORMATION - RH_LO)
SOAKED = kpa(20.0)


def report():
    w("# SITE SELECTION AND GEOTECHNICAL INVESTIGATION")
    w("### Underground CBRN-hardened blast-resistant protective structure "
      "and sentry post — Pune, Maharashtra")
    w()
    w(f"**Package** `Site Selection and Geotechnical/` · **revision "
      f"{P.REV}** · **{P.PACKAGE_DATE}** · {P.GEOM_REV}")
    w(f"**Status — {P.STATUS}.**")
    w()
    w("**Evidence class, as everywhere in this project:** "
      "`[C]` confirmed · `[R]` reconstructed · `[D]` derived here · "
      "`[A]` assumed by this package · `[U]` unresolved · `[N]` not "
      "available — DATA REQUIRED")
    w()
    w("---")
    w()

    # ---------------------------------------------------------------- 1
    w("## 1. Why this section exists, and what it does not do")
    w()
    w("Until now this project has carried its site and its ground entirely "
      "as assumptions. Master `A.6` tags **every** soil parameter "
      "`[ASSUMED]`; `K.2` lists six of them as items that must be confirmed "
      "before construction; and the Part J dependency map draws "
      "`[SITE INVESTIGATION]` as a root node with **nothing feeding it**. "
      "The design report has never contained a site selection section at "
      "all.")
    w()
    w("Two documents have now been supplied that feed that node for the "
      "first time. This section records them, checks them against each "
      "other and against the master, and states exactly what they do and do "
      "not establish.")
    w()
    w("> ### It resolves nothing, deliberately.")
    w("> Master rule `M.6` and the project operating guide both forbid "
      "converting an `[ASSUMED]` into a confirmed fact. **Not one `K.2` "
      "assumption is closed by this section.** What each one now has, for "
      "the first time, is a **stated provenance and a quantified margin** — "
      "and in four cases, a reason to stay open that is stronger than "
      "before.")
    w()
    w("**No design value changes.** No load, thickness, bar, level, "
      "quantity, rate, date or float moves. No `.std` file is touched. The "
      "main staircase is untouched. The sentry post is in scope for **ground "
      "only** — footing F1 bears on in-situ basalt at `(−)2.000` and that is "
      "a geotechnical statement — and no sentry structural value is changed.")
    w()

    # ---------------------------------------------------------------- 2
    w("## 2. Sources")
    w()
    w("| # | Document | What it is | Class |")
    w("|---|---|---|---|")
    w(f"| **1** | **{D.REPORT['code']}** — *{D.REPORT['title']}*. "
      f"{D.REPORT['author']}. Raised on {D.REPORT['request']}. | "
      f"A real sub-soil investigation: **{D.N_TRIAL_PITS} trial pits at 3 "
      f"locations**, Appendices A (classification), B (soil test result) and "
      f"C (rock cores), Sketches P and Q. | `[C]` |")
    w(f"| **2** | **P1 presentation deck** — *{D.DECK['title']}*, "
      f"{D.DECK['team']}, {D.DECK['pages']} slides. | The project's own "
      f"first-phase presentation: site location, contour, watershed, road, "
      f"pipelines, recce, elevation profile, SWOT, wind, precipitation, "
      f"temperature, seismic and soil slides. | `[C]` as a record of what "
      f"was presented |")
    w(f"| **3** | Location pin `{D.PIN_URL}` | The project owner's own "
      f"positional reference. | `[N]` — **{D.PIN_STATUS}** |")
    w()
    w("### 2.1 A limitation that must be read before anything else")
    w()
    w("**The SEMT report is not an investigation of this plot.** It "
      "investigates three named buildings on the CTW/CME campus — "
      "**G Building (TP-1 to TP-4)**, **H Building (TP-5 to TP-8)** and the "
      "**Mess Building (TP-9 to TP-11)**. The project plot is a separate "
      "undeveloped area east of the CTW blocks, against the perimeter track "
      "(deck slides 13, 14 and 22).")
    w()
    w("The report may be carried across to this plot only on the strength of "
      "its own paragraph 5:")
    w()
    w(f"> *“{D.GEOLOGY}”*")
    w()
    w("That carry-across is an **assumption of this section, not a finding "
      "of the report** `[A]`. And the report itself shows how much variation "
      f"“uniform over a wide area” permits: across three locations a few "
      f"hundred metres apart, rockhead moved from "
      f"**{RH_LO:.1f} m to {RH_HI:.1f} m** and the surface stratum changed "
      f"from a 1.0 m high-plasticity clay to a 0.2 m clayey-sand murrum.")
    w()

    # ---------------------------------------------------------------- 3
    w("## 3. Site identification")
    w()
    w("| Item | Value | Class |")
    w("|---|---|---|")
    w("| Installation | CTW / College of Military Engineering campus, Pune, "
      "Maharashtra | `[C]` |")
    w("| Plot | Undeveloped rectangle **east of the two CTW blocks**, west "
      "of the perimeter track and nullah line, **CBRN Live Training Area to "
      "the south** | `[C]` deck slides 13, 14, 22 |")
    w(f"| Latitude / longitude | **NOT ESTABLISHED** — {D.PIN_STATUS} | "
      f"`[N]` |")
    w("| Plot boundary and area | **NOT DIMENSIONED ANYWHERE.** No scale "
      "bar, grid, boundary dimension or coordinate appears on any supplied "
      "site image | `[N]` — master gap **D3** |")
    w("| Site benchmark | **NONE.** Nothing ties any supplied level to the "
      "project datum | `[N]` |")
    w("| Project datum | **finished grade = 0.000**, local, master `A.4.1` | "
      "`[C]` |")
    w()
    w("> **Master gap D3 — “no site plan” — is NOT closed by this section "
      "and cannot be.** Imagery is not a site plan. Until a boundary, a "
      "dimension, a benchmark and a coordinate exist, the berm, the "
      "hardstanding, the access, the five external drainage runs, the "
      "concealment layout (`CAM2`) and the cut-and-fill cannot be drawn. "
      "What this section adds is that the *setting* is now recorded, which "
      "it was not.")
    w()

    # ---------------------------------------------------------------- 4
    w("## 4. Site selection")
    w()
    w("The selection was made at P1 and is recorded here for the first "
      "time. The deck's own SWOT, verbatim:")
    w()
    w("| | |")
    w("|---|---|")
    for k, label in (("strength", "**Strengths**"),
                     ("weakness", "**Weaknesses**"),
                     ("opportunity", "**Opportunities**"),
                     ("threats", "**Threats**")):
        w(f"| {label} | " + " · ".join(D.DECK_SWOT[k]) + " |")
    w()
    w("### 4.1 What the selection got right, in this project's own terms")
    w()
    w("Three of the recorded strengths are load-bearing for the design that "
      "followed, and none of them was written down as such at the time:")
    w()
    w("1. **“No pipelines.”** The pipelines sketch (slide 18) draws the site "
      "box **outside** the campus pipe network; the nearest services are the "
      "RCC overhead reservoir (15 000 gallons, 15 m staging) and substation "
      "SS-15 beside buildings 526/527. For a **22 m × 6.2 m box excavated "
      "to (−)6.800** with a **continuous gas-tight, EMP-bonded envelope**, a "
      "buried main crossing the footprint would have been a first-order "
      "problem: every envelope penetration is a blast, gas and EMP "
      "discontinuity, which is why the master forbids movement joints inside "
      "the protective envelope at all. A clear plot is worth more here than "
      "on an ordinary building.")
    w("2. **“Availability of electric lines.”** `EL1` found that the only "
      "record of an incoming mains supply anywhere in the project is a line "
      "in the owner's own construction schedule. Slide 22 is the second, and "
      "it is earlier. It does not give a capacity — `EL-V4`, which blocks "
      "any fault-level study, **stays open**.")
    w("3. **“Good road connectivity.”** The road connectivity slide shows "
      "the plot reached from the campus network without passing through the "
      "built-up core. The works management package programmes **994 m³ of "
      "rock excavation by hydraulic breaker with no blasting** and tipper "
      "haulage throughout; that is a haul-route requirement, and the site "
      "meets it.")
    w()
    w("### 4.2 What the selection did not consider, and what it costs")
    w()
    w("| Not considered | Consequence, now quantified |")
    w("|---|---|")
    w("| **Ground conditions on the plot itself** | The selection rests on a "
      "soil report for three *other* buildings. The confirmatory site "
      "investigation (WBS `A1075`, 12 d, **critical path**) has to be "
      "located **on this plot**, not repeated from the report. `SG-V1` |")
    w("| **Depth of investigation** | Nothing is known below about 1.5 m; "
      "the structure founds at `(−)6.800`. **`SG-V2` — the governing item "
      "of this section.** |")
    w("| **Ground slope** | The plot sits on the edge of a slope falling "
      "east. A 22 m box on a level formation under a crowned grade needs cut "
      "and fill; **no cut-and-fill item exists in the BOQ** because no site "
      "plan exists. `SG-V4` |")
    w("| **“Located near Perimeter Fence”**, recorded as the single "
      "weakness | It is also a **concealment** weakness, and `CAM2` — whose "
      "finding is that *the shelter is concealed, the installation is not* — "
      "could not draw a concealment layout for exactly this reason. The "
      "sentry post stands at **+7.000** and the headhouse at **+0.900 with "
      "no earth cover**; how visible those are from the fence line is a "
      "function of a distance nobody has recorded. `CAM-V2`, `D3` |")
    w()

    # ---------------------------------------------------------------- 5
    w("## 5. Site setting — topography, drainage and access")
    w()
    w("### 5.1 Level and fall — and a conflict inside the deck")
    w()
    w("Two slides describe the ground surface, and **they do not agree**:")
    w()
    e = D.DECK_ELEV_PROFILE
    w("| Source | What it says | Implied ground level | Implied fall |")
    w("|---|---|---|---|")
    w(f"| **Contour map**, slide 15 | 1 m contours labelled "
      f"**{D.DECK_CONTOURS[0]} to {D.DECK_CONTOURS[1]}**; the "
      f"**{D.DECK_CONTOURS_AT_SITE[0]}** and "
      f"**{D.DECK_CONTOURS_AT_SITE[1]}** contours both cross the plot; "
      f"ground falls {D.DECK_CONTOUR_FALL} | "
      f"**≈ {D.DECK_CONTOURS_AT_SITE[0]}–"
      f"{D.DECK_CONTOURS_AT_SITE[1] + 1} m** on that map's datum | "
      f"of the order of **1–1.5 m** across the plot, ≈ 1 in 40 |")
    w(f"| **Elevation profile**, slide 21 | **{e['z0']} m** at 0 m rising to "
      f"**{e['z1']} m** at **{e['x1']} m** | "
      f"**{e['z0']}–{e['z1']} m** | "
      f"**{e['z1'] - e['z0']:.1f} m over {e['x1']:.1f} m** = "
      f"**1 in {e['x1'] / (e['z1'] - e['z0']):.1f}** "
      f"({(e['z1'] - e['z0']) / e['x1']:.1%}) |")
    w()
    w(f"**They differ by {e['z0'] - (D.DECK_CONTOURS_AT_SITE[1] + 1):.0f} to "
      f"{e['z1'] - D.DECK_CONTOURS_AT_SITE[0]:.0f} m in level and by roughly "
      f"a factor of four in gradient.** `[U]` `SG-V4`")
    w()
    w("The most likely reading is that the contour map is on a local survey "
      "datum while the profile is a satellite-derived MSL profile taken "
      "across a short transect that includes the track embankment east of "
      "the plot — **but that is a guess and it is recorded as one.** Neither "
      "figure is adopted.")
    w()
    w("**Why it does not matter to any calculation.** The project works on a "
      "local datum with finished grade `= 0.000` (master `A.4.1`). Every "
      "level in Parts A, B and F is relative to it and **no absolute reduced "
      "level appears anywhere in the project**. Nothing recalculates.")
    w()
    w("**Why it matters anyway.** Three things that are not yet drawn depend "
      "on it: the **cut and fill** needed to give a 22 m box a level "
      "formation under a crowned grade; the **berm toe**; and the point "
      "where the cover's **1:50 crossfall** (`BS1`) daylights into the berm "
      "fill. With 1 to 1.5 m of natural fall across the plot, finished grade "
      "at 0.000 **cannot be the natural surface everywhere**.")
    w()
    w("The report's own terrain sentence — *“" + D.TERRAIN + "”* — is said "
      "of the G, H and Mess building locations. The contour map shows this "
      "plot is the edge of a slope.")
    w()
    w("### 5.2 Surface drainage")
    w()
    w("The watershed slide (16) shows the plot on the shoulder of a "
      "catchment draining east and south-east to the track and nullah line, "
      "with no channel crossing the plot itself. That is consistent with the "
      "contours and with the drainage package's position that **the "
      "engineered cover is not drained by pipework**: rain sheds at the "
      "surface, what infiltrates is intercepted by the 150 granular filter "
      "and dispersed at the berm toe (`D-201` note 3, calculation `D.7`, and "
      "`BS1`, which gave the burster slab the 1:50 crossfall that claim "
      "depends on).")
    w()
    w("**The site-wide catchment still cannot be closed.** Calculation `D.7` "
      "records the structures' own catchments as complete (177.23 m²) and "
      "the berm, approach and hardstanding as `[N]` for want of a site plan. "
      "Slide 16 does not supply a boundary, so that stays `[N]`.")
    w()

    # ---------------------------------------------------------------- 6
    w("## 6. Geology and regional setting")
    w()
    w(f"> *“{D.GEOLOGY}”* — SEMT/67/15 para 5 `[C]`")
    w()
    w("This is the Deccan Trap, and the master has assumed it since Rev D. "
      "The report confirms the formation. **What it does not confirm is the "
      "thing the master is actually afraid of:**")
    w()
    w("> **Master `A.6`:** *“The hazard is not the basalt — it is the flow "
      "contacts. A single red-bole seam under the mat produces the "
      "differential-support case that SIZES the mat.”*")
    w()
    w("That case — a 3.0 m band of red-bole or vesicular material removed at "
      "the worst position — is **what governs the 600 mat and its "
      "T16 @ 150 EF EW at 84 % utilisation** (master `B.3`, Case 2). "
      "Horizontally bedded flows are precisely the geometry that produces "
      "flow contacts at intervals. **The report neither finds nor excludes "
      "one, because it never reached the founding horizon.** The red-bole "
      "case stands exactly as designed, and the confirmatory investigation "
      "must look for seams **at and below (−)6.800**, not above it.")
    w()

    # ---------------------------------------------------------------- 7
    w("## 7. The sub-soil investigation")
    w()
    w("### 7.1 Scope and method")
    w()
    w("| Item | Record | Class |")
    w("|---|---|---|")
    w(f"| Method | *“{D.FIELD}”* | `[C]` |")
    w(f"| Pits | **{D.N_TRIAL_PITS}**, at 3 locations | `[C]` |")
    w("| Boreholes | **none** | `[C]` |")
    w("| In-situ testing | **none** — no SPT, no plate load test, no "
      "permeability test, no percolation test | `[C]` |")
    w("| Date of field work | **not stated anywhere in the report** | "
      "`[N]` `SG-V10` |")
    w("| Laboratory | " + " · ".join(f"{n} ({c})" for n, c in D.LAB_TESTS)
      + " | `[C]` |")
    w()
    w("### 7.2 The governing finding of this whole section")
    w()
    w("| | Level |")
    w("|---|---|")
    w(f"| **Deepest stratum boundary recorded anywhere in the report** | "
      f"**(−){DEEPEST:.3f}** |")
    w(f"| Sentry footing F1, on in-situ basalt | `{P.LVL_F1_FOUND:.3f}` |")
    w(f"| Underground box, internal floor | `{P.LVL_FLOOR:.3f}` |")
    w(f"| Mat soffit | `{P.LVL_MAT_SOFFIT:.3f}` |")
    w(f"| **FORMATION — what the mat actually bears on** | "
      f"**`{P.LVL_FORMATION:.3f}`** |")
    w(f"| Sump SU-01 base | `{P.LVL_SUMP_BASE:.3f}` |")
    w()
    w("> ## `SG-F2` — THE INVESTIGATION REACHED ABOUT 1.5 m. THE STRUCTURE "
      "FOUNDS AT 6.8 m.")
    w(f"> There are **{-DEEPEST - P.LVL_FORMATION:.1f} m of completely "
      f"unlogged ground** between the bottom of the deepest trial pit and "
      f"the formation the 600 mat bears on, and "
      f"**{-DEEPEST - P.LVL_SUMP_BASE:.1f} m** to the sump base. "
      f"**Only the sentry post footing F1 at `(−)2.000` lies inside the "
      f"investigated horizon, and only just.**")
    w("> ")
    w("> Nothing the report says about rockhead continuity, groundwater, "
      "jointing, red-bole seams or modulus of subgrade reaction can be read "
      "as covering the founding horizon of the shelter. Master `K.2` items "
      "**A1, A2, A4, A5 and A8 all stay open**, and the programme's "
      "confirmatory site investigation `A1075` — *boreholes, rockhead, "
      "red-bole seams*, 12 days, **total float 0** — remains mandatory in "
      "full. `SG-V2`")
    w()
    w("### 7.3 What the pits did find — and the check that it is usable")
    w()
    w("The full stratum log is in `Schedules/TRIAL_PIT_SCHEDULE.md`. In "
      "summary, at all three locations: a thin **black cotton (CH) cover**, "
      "**murrum** below it, **disintegrated broken basalt** below that, and "
      "**sound basalt** below that again.")
    w()
    w("Before using any of it, the report was tested against itself. "
      "**Every derived number in it reproduces from its own inputs** "
      "(calculation `G.2`):")
    w()
    w("| Chain | Check | Result |")
    w("|---|---|---|")
    w(f"| Soil | `SBC = q_ult / {D.APPX_B_FOS}`, the report's own stated "
      f"factor of safety | **6 of 6 rows reproduce** |")
    w("| Rock, step 1 | `UCS = max load / specimen area` | **6 of 6 rows "
      "reproduce** |")
    w("| Rock, step 2 | `SBC = UCS / 25`, rounded — the factor the report "
      "applies but never prints | **6 of 6 rows reproduce** |")
    w()
    w("> **`SG-F1`.** The SEMT report is internally consistent and is "
      "usable. That is worth establishing before anything is built on it.")
    w()

    # ---------------------------------------------------------------- 8
    w("## 8. Bearing capacity")
    w()
    w("### 8.1 Soaked or unsoaked? It is not a free choice")
    w()
    w("The report gives sound basalt **two** bearing values, and they differ "
      "by a factor of about 1.6:")
    w()
    w("| Condition | Band | Class |")
    w("|---|---|---|")
    w(f"| **Soaked** | **{kpa(20):.0f} – {kpa(21):.0f} kPa** (20–21 kg/cm²) "
      f"| `[C]` |")
    w(f"| Unsoaked | {kpa(30):.0f} – {kpa(36):.0f} kPa (30–36 kg/cm²) | "
      f"`[C]` |")
    w(f"| Master `A.6` presumptive, IS 1904:1986 Table 1, hard rock | "
      f"**{P.SBC_MASTER:.0f} kPa** | `[A]` |")
    w()
    w(f"The design groundwater table is at `{P.LVL_GWT_DESIGN:.3f}` and the "
      f"formation at `{P.LVL_FORMATION:.3f}` — "
      f"**{P.LVL_GWT_DESIGN - P.LVL_FORMATION:.1f} m below it**, "
      f"permanently submerged. **The soaked value is the applicable one.** "
      f"Appendix B makes the same choice for the soils in its own remark: "
      f"*“in submerged condition of soil”*.")
    w()
    w(f"The master's presumptive **{P.SBC_MASTER:.0f} kPa** sits inside the "
      f"*unsoaked* band and is **{P.SBC_MASTER / SOAKED - 1:+.0%}** on the "
      f"*soaked* one.")
    w()
    w("### 8.2 And it does not matter")
    w()
    w("Every bearing check in the master, re-run at the lowest soaked value:")
    w()
    w("| Check | Demand | / 3240 `[A]` | / 1961 soaked | Verdict |")
    w("|---|---|---|---|---|")
    for name, q in (("Mat, service — master `B.3`", P.Q_MAT_SERVICE),
                    ("Mat, **blast** — master `B.3`", P.Q_MAT_BLAST),
                    ("Sentry footing F1 — master `B.8.7`", P.Q_F1_SERVICE)):
        w(f"| {name} | {q} kPa | {q / P.SBC_MASTER:.2%} | "
          f"{q / SOAKED:.2%} | **PASS** |")
    w()
    w(f"> **`SG-F3`.** The worst bearing utilisation in the whole project "
      f"rises from **12.5 % to {P.Q_MAT_BLAST / SOAKED:.1%}** and everything "
      f"still passes with a factor of **{SOAKED / P.Q_MAT_BLAST:.1f}** in "
      f"hand. **Master `A.6` is not changed** — 3240 kPa is a presumptive "
      f"value from IS 1904 and it is declared as one. What this section adds "
      f"is that **the design is now known to survive the measured value "
      f"too.**")
    w()
    w("A second check the report offers for free: even at the **broken** "
      f"basalt value of {kpa(10):.0f} kPa — the horizon 5 m *above* the "
      f"formation — the mat under full blast would be at "
      f"**{P.Q_MAT_BLAST / kpa(10):.0%}**. The bearing case is nowhere near "
      f"governing anything.")
    w()
    w("### 8.3 The real foundation story: net pressure")
    w()
    w("The excavation removes ground before the structure replaces it. The "
      "report's profile lets that be quantified for the first time "
      "(calculation `G.5`, γ values `[A]`):")
    w()
    soil_t = sum(HEADS) / len(HEADS)
    rock_t = -P.LVL_FORMATION - soil_t
    removed = soil_t * 19.5 + rock_t * 25.0
    w("| | kPa |")
    w("|---|---|")
    w(f"| Overburden removed, {soil_t:.2f} m soil at 19.5 kN/m³ | "
      f"{soil_t * 19.5:.2f} |")
    w(f"| Overburden removed, {rock_t:.2f} m basalt at 25.0 kN/m³ | "
      f"{rock_t * 25.0:.2f} |")
    w(f"| **Total gross pressure removed at formation** | "
      f"**{removed:.2f}** |")
    w(f"| Replaced by, in service (master `B.3`) | {P.Q_MAT_SERVICE:.2f} |")
    w(f"| **Net change in pressure at formation** | "
      f"**{P.Q_MAT_SERVICE - removed:+.2f}** |")
    w()
    w(f"> **`SG-F4`.** **In service the structure is lighter than the ground "
      f"it replaces, by about {removed - P.Q_MAT_SERVICE:.0f} kPa.** It is a "
      f"fully compensated foundation and then some. This is the physical "
      f"reason master `B.3` can write *“SETTLEMENT Negligible”* and mean it "
      f"— and it is the same fact seen from the other side that makes "
      f"**flotation**, not bearing or settlement, the governing foundation "
      f"problem (FoS **0.33** at the mat-only stage). The report does not "
      f"change either conclusion. It explains them.")
    w()

    # ---------------------------------------------------------------- 9
    w("## 9. Rockhead — and what it costs")
    w()
    w(f"> *“{D.PROFILE_TEXT.rstrip('.').split('. ')[-1].strip()}.”* — "
      f"SEMT/67/15 para 12")
    w()
    w("| Location | Sound basalt below | On the project datum |")
    w("|---|---|---|")
    for (loc, layers), d in zip(D.FINDINGS, HEADS):
        w(f"| {loc} | {d:.3f} m | `(−){d:.3f}` |")
    w(f"| **Report band** | | **`(−){RH_LO:.3f}` to `(−){RH_HI:.3f}`** "
      f"`[C]` |")
    w(f"| **Master `A.6` assumed band** | | "
      f"**`(−){-P.ROCKHEAD_MASTER[0]:.3f}` to "
      f"`(−){-P.ROCKHEAD_MASTER[1]:.3f}`** `[A]` |")
    w()
    w("> **`SG-F5`. The two bands touch at exactly one point, `(−)1.500`.** "
      "The report's rock is at or **above** the master's whole assumed "
      "range. The master is therefore **conservative for founding depth** — "
      "the rock is there sooner than assumed — and **unconservative for "
      "excavation quantity**, because more of the cut is in rock and less is "
      "in soil.")
    w()
    w("Quantifying it. BOQ item `E-02b` at the mean rockhead, with its own "
      "stated range, fixes the excavation plan area:")
    w()
    w("| Rockhead | Depth of rock cut | Rock volume m³ | vs BOQ upper "
      "bound |")
    w("|---|---|---|---|")
    for rh in (0.900, 1.000, 1.500, 1.750, 2.000):
        v = AREA * (-P.LVL_FORMATION - rh)
        mark = ""
        if rh == 1.750:
            mark = " ← BOQ `E-02b`"
        w(f"| `(−){rh:.3f}`{mark} | {-P.LVL_FORMATION - rh:.3f} m | "
          f"{v:.2f} | {v - P.WM_ROCK_RANGE[1]:+.2f} |")
    w()
    w(f"| | |")
    w(f"|---|---|")
    w(f"| BOQ prices | **{P.WM_ROCK_RANGE[0]:.1f} – "
      f"{P.WM_ROCK_RANGE[1]:.1f} m³** |")
    w(f"| On the report's band | **{ROCK_LO:.1f} – {ROCK_HI:.1f} m³** |")
    w(f"| The report's **lower** bound equals the BOQ's **upper** bound | "
      f"`(−)1.500` → {ROCK_LO:.1f} m³ |")
    w(f"| Overrun at the report's shallow rockhead | "
      f"**+{ROCK_HI - P.WM_ROCK_RANGE[1]:.1f} m³** "
      f"(**{ROCK_HI / P.WM_ROCK_RANGE[1] - 1:+.1%}**) |")
    w(f"| At the WBS `A2050` output of {P.WM_ROCK_RATE_M3_DAY:.0f} m³/day | "
      f"**≈ {(ROCK_HI - P.WM_ROCK_RANGE[1]) / P.WM_ROCK_RATE_M3_DAY:.0f} "
      f"extra days** |")
    w()
    w("**Total excavation does not change** — soil falls by the same volume "
      f"as rock rises — so the money at stake is the **rate difference** "
      f"over about {ROCK_HI - P.WM_ROCK_RANGE[1]:.0f} m³, not a rock rate "
      f"over {ROCK_HI - P.WM_ROCK_RANGE[1]:.0f} m³.")
    w()
    w("**No BOQ quantity is changed here.** `WM2` adopted the project "
      "owner's own BOQ and it governs (master `H.13`), and risk `R-03` in "
      "the works management risk register already carries *“rock excavation "
      "quantity exceeds the estimate because rockhead is shallower than the "
      "mean assumed”*. What this section adds is **the number**: the "
      "register says *“roughly one extra day”*, and on the report's band it "
      f"is about **{(ROCK_HI - P.WM_ROCK_RANGE[1]) / P.WM_ROCK_RATE_M3_DAY:.0f}**.")
    w()
    w("One consequence is favourable and is recorded because it is free. "
      "Master `B.3` dismisses sliding on the grounds that the box is "
      "*“socketed ~4.8 m into basalt”*. On the report's band the socket is "
      f"**{-P.LVL_FORMATION - RH_HI:.1f} m to "
      f"{-P.LVL_FORMATION - RH_LO:.1f} m**. The argument gets stronger.")
    w()

    # --------------------------------------------------------------- 10
    w("## 10. Groundwater — the central question")
    w()
    w("> *“" + D.WATER_TABLE_TEXT + "”* — SEMT/67/15 para 13 `[C]`")
    w()
    w("> P1 deck slide 29, verbatim: *“Water Table not encountered in any "
      "trial pit”* · *“Might increase during monsoon”* · **“Proposed "
      "structure safe for water table at depth of 2 m below GL”** `[C]`")
    w()
    w("### 10.1 The provenance of `(−)2.000`, recorded for the first time")
    w()
    w("Master `A.6` and `K.2 A2` record the design groundwater table as "
      "**`(−)2.000` `[ASSUMED]` — the single most important number to "
      "confirm** — and give **no source**. The source is now known, and it "
      "is this:")
    w()
    w("> **No water was found in any trial pit, so a depth of 2 m below "
      "ground level was *chosen*, and the structure was then designed to be "
      "safe for it.**")
    w()
    w("That is an assumption adopted in the absence of data. It is a "
      "defensible one — it puts the water table near the surface, which is "
      "the conservative direction for uplift and for lateral load. "
      "**It is not a measurement, and this section does not turn it into "
      "one.**")
    w()
    w("### 10.2 Three reasons the observation does not reach the design "
      "question")
    w()
    w(f"**(1) Depth.** The pits reached about {DEEPEST:.1f} m. The design "
      f"GWT is at `{P.LVL_GWT_DESIGN:.3f}` — **already below the deepest "
      f"pit** — and the founding horizon is at `{P.LVL_FORMATION:.3f}`. "
      f"A pit that stops at 1.5 m cannot find a water table at 2 m, let "
      f"alone characterise one at 6.8 m. **Here, *“not encountered”* means "
      f"*“not reached”*.**")
    w()
    w("**(2) Season.** The report itself says the table *“may raise "
      "during/after rainy season”*. The request is dated **20 May 2015**; if "
      "the field work followed promptly it was done in the last weeks before "
      "the monsoon — the annual minimum. **The report nowhere states the "
      "date of the field work**, so this is inference and is recorded as an "
      "open item, not as a finding. `[U]` `SG-V10`")
    w()
    w("**(3) Ground type.** Deccan Trap groundwater is not a simple water "
      "table in a porous medium. It sits in the vesicular and jointed zones "
      "**at the flow contacts** — the same feature master `A.6` names as the "
      "hazard and that the red-bole differential-support case in `B.3` is "
      "built around. Such water is commonly perched and strongly seasonal. "
      "**An open trial pit in the dry season is close to the worst available "
      "instrument for finding it.**")
    w()
    w("### 10.3 Why this is the number that matters")
    w()
    w("| From master `A.7.2` and `B.3` | |")
    w("|---|---|")
    w(f"| Of the **{P.GRADIENT_MASTER} kPa/m** lateral gradient | **9.81 is "
      f"water**, only {P.GRADIENT_MASTER - 9.81:.2f} is soil |")
    w("| Hydrostatic uplift on the mat | **46.11 kPa = 6 289 kN over "
      "136.4 m²** |")
    w("| Flotation FoS, mat cast only | **0.33 — FAIL** |")
    w("| Flotation FoS, box complete, no backfill | **1.22 — MARGINAL** |")
    w("| Flotation FoS, box complete, flooded to grade | **0.86 — FLOATS** |")
    w()
    w("> **`SG-F6`. `K.2 A2` stays `[ASSUMED]` and stays open — and the new "
      "evidence is a reason to keep it open, not to close it.** Water is "
      "nearly two thirds of the lateral load and the whole of the uplift. "
      "Everything this structure is afraid of is water.")
    w()
    w("### 10.4 What would actually close it — and a programme problem")
    w()
    w("The works management programme carries the right activity:")
    w()
    w("> `A1080` — **“Monsoon groundwater monitoring — confirm the design "
      "GWT (−)2.000”**, 20 days, **12-11-26 to 04-12-26**, total float 0, "
      "noted *“the single most important assumption in the project”*.")
    w()
    w("> ## `SG-F7` — that window is not in the monsoon.")
    w(f"> On the deck's own precipitation table, June to September carry "
      f"**{JUN_SEP:.1f} mm ({JUN_SEP / PRECIP_TOTAL:.0%} of the year)**, "
      f"while **November and December carry "
      f"{PRECIP['November'] + PRECIP['December']:.1f} mm between them**. An "
      f"activity called *monsoon* groundwater monitoring scheduled "
      f"**12 November to 4 December** measures the **recession, not the "
      f"peak** — and the peak is exactly what `A2` asks for.")
    w("> ")
    w("> What closes `A2` is a **standpipe piezometer installed in the "
      "`A1075` borehole and read through a full monsoon**. Nothing shorter "
      "does. **No programme date is changed here**: the owner's own Master "
      "Construction Schedule R0 governs (master `H.13`) and `A1080` sits on "
      "the critical path at TF 0, so moving it moves the job. It is raised, "
      "with its reason and its cost, as **`SG-V3`** — a decision for the "
      "project owner.")
    w()

    # --------------------------------------------------------------- 11
    w("## 11. Seismicity")
    w()
    w("| Source | Statement |")
    w("|---|---|")
    w(f"| SEMT/67/15 para 7 | *“{D.SEISMIC_REPORT}”* |")
    w(f"| P1 deck slide 27 | **{D.DECK_SEISMIC_ZONE}**, design per "
      f"**{D.DECK_SEISMIC_CODE}** |")
    w("| Master `A.7.8` | **Z = 0.16 (Zone III)**, IS 1893 (Part 1):2016 |")
    w()
    w("The report cites the **1984** zone map and the design uses the "
      "**2016** code. Pune is Zone III on both, and Z = 0.16 is read from "
      "IS 1893 (Part 1):2016 Table 3. Reproducing the master's two seismic "
      "coefficients from it:")
    w()
    w("| Structure | R | A_h = (Z/2)(I/R)(Sa/g) | Master | |")
    w("|---|---|---|---|---|")
    for name, R, ah in (("Underground box", 4.0, 0.075),
                        ("Sentry post", 3.0, 0.100)):
        calc = (0.16 / 2) * (1.5 / R) * 2.5
        w(f"| {name} | {R:.1f} | (0.16/2)(1.5/{R:.1f})(2.5) = "
          f"**{calc:.4f}** | {ah:.3f} | **✔** |")
    w()
    w("> **`SG-F12`. Zone III is now corroborated by a document outside the "
      "project, and the master's seismic coefficients reproduce exactly from "
      "it.** This is the **only** master design input this section is able "
      "to corroborate externally. Nothing changes — and that is the point. "
      "It was already right.")
    w()
    w("The two documents name **different** 1993 events — the report names "
      "Killari (Latur), the deck names the Koyna area on 28 August 1993. "
      "Both are recorded as they stand; neither changes the zone, which is "
      "what the design uses, and this section does not adjudicate "
      "seismology. The deck's three regional events (M "
      + ", ".join(str(m) for _, _, m in D.DECK_SEISMIC_EVENTS) +
      ") are all well below the Zone III design basis and are recorded as "
      "context.")
    w()

    # --------------------------------------------------------------- 12
    w("## 12. Meteorology")
    w()
    w("The full monthly table is in "
      "`Schedules/METEOROLOGICAL_SCHEDULE.md`.")
    w()
    w("### 12.1 Rainfall — the two documents disagree")
    w()
    w("| Source | Annual rainfall | Class |")
    w("|---|---|---|")
    w(f"| P1 deck slide 25, summed | **{PRECIP_TOTAL:.1f} mm** | `[C]` |")
    w(f"| SEMT/67/15 para 9 | **{D.RAINFALL_REPORT_RANGE[0]:.0f} – "
      f"{D.RAINFALL_REPORT_RANGE[1]:.0f} mm** | `[C]` |")
    w(f"| Difference | "
      f"**{PRECIP_TOTAL / D.RAINFALL_REPORT_RANGE[1] - 1:+.0%} to "
      f"{PRECIP_TOTAL / D.RAINFALL_REPORT_RANGE[0] - 1:+.0%}** | `[U]` |")
    w()
    w("> **`SG-F11`. The two supplied documents disagree on annual rainfall "
      "by between a quarter and a half.** Neither names a station, a period "
      "of record or a source: the deck says *“last 10 years avg”* and the "
      "report says *“the region”*.")
    w()
    w("**No third figure is adopted here.** Published tertiary figures for "
      "“Pune” themselves range from about 720 mm to over 1 000 mm depending "
      "on which gauge and which period is quoted — which is the reason a "
      "**named station and period** is required, and the reason substituting "
      "a web figure for the deck's would be putting false authority on the "
      "design report. `SG-V5`")
    w()
    w("**One month is the outlier.** Read as a monsoon distribution for the "
      "interior Deccan:")
    w()
    w("| | |")
    w("|---|---|")
    w(f"| June to September | **{JUN_SEP:.1f} mm**, "
      f"{JUN_SEP / PRECIP_TOTAL:.0%} of the year |")
    w(f"| **October alone** | **{PRECIP['October']:.1f} mm**, "
      f"{PRECIP['October'] / PRECIP_TOTAL:.0%} of the year |")
    w(f"| October ÷ September | **{PRECIP['October'] / PRECIP['September']:.2f}** |")
    w(f"| October ÷ August | **{PRECIP['October'] / PRECIP['August']:.2f}** |")
    w()
    w("The south-west monsoon withdraws from interior Maharashtra in the "
      "first half of October. An October that nearly equals September **and "
      "exceeds August** is not the shape of a Deccan rainfall year. "
      "**The October figure is the one to go back and check** — and note "
      f"that removing it alone would bring the deck's total to "
      f"**{PRECIP_TOTAL - PRECIP['October']:.1f} mm**, still above the "
      f"report's range. **It is not corrected here**: correcting a datum "
      f"whose source is unknown would be inventing evidence. `SG-V5`")
    w()
    w("### 12.2 And the part that matters most — nothing in the design uses "
      "the annual total")
    w()
    w("| What the design actually uses | Status |")
    w("|---|---|")
    w("| **50 mm/h design intensity**, Rev F drawing 5 note 1 — the only "
      "rainfall intensity anywhere in the project, with **no return period, "
      "duration or IDF source** | drainage open item **`DR-D1`**, **NOT "
      "closed by this section** — a monthly total cannot produce a "
      "short-duration intensity |")
    w("| **Soak-pit absorption 20 L/m²/day** | `K.2 A7` — needs the "
      "IS 2470 (Pt 2) Cl. 4 **percolation test** and nothing else. The "
      "report's basalt makes failure likely, which the master already says |")
    w("| **The monsoon window** | a **programme** input — `SG-F7` above |")
    w()
    w("So the rainfall conflict **changes no number in this project**. It "
      "changes what the design report may claim, and it changes when the "
      "groundwater monitoring has to happen.")
    w()
    w("### 12.3 Temperature — not a conflict, and a gap narrowed")
    w()
    t = D.TEMP_REPORT
    hi = max(D.DECK_TEMP, key=lambda r: r[1])
    lo = min(D.DECK_TEMP, key=lambda r: r[3])
    w("| Source | Statistic | Values |")
    w("|---|---|---|")
    w(f"| SEMT/67/15 para 8 | **absolute extremes** | summer "
      f"{t['summer_max']} / {t['summer_min']} °C · winter "
      f"{t['winter_max']} / {t['winter_min']} °C |")
    w(f"| P1 deck slide 26 | **monthly means** | hottest {hi[0]} "
      f"{hi[1]} °C mean daily max · coldest {lo[0]} {lo[3]} °C mean daily "
      f"min |")
    w()
    w(f"A monthly mean daily maximum of {hi[1]} °C sitting under an absolute "
      f"maximum of {t['summer_max']} °C is exactly what one expects. "
      f"**These are different statistics and they are mutually consistent.**")
    w()
    w("HVAC calculation `H.10` records *“outdoor design dry-bulb / wet-bulb, "
      "Pune … NOT IN THE PROJECT `[N]`”* as the **first of eight missing "
      "inputs** that stop a cooling load being computed. This section "
      "**narrows that gap and does not close it**: an absolute extreme and a "
      "monthly mean are not a design dry-bulb, and **neither document gives "
      "a wet-bulb or any coincident value at all**. The remaining seven "
      "inputs are untouched, and `EL-V6` — *no cooling plant exists anywhere "
      "in the project* — is untouched.")
    w()
    w("### 12.4 Wind — a warning, because this one invites a wrong "
      "“correction”")
    w()
    wmax = max(D.DECK_WIND, key=lambda r: r[1])
    w("| | |")
    w("|---|---|")
    w(f"| Deck slide 24, windiest month | {wmax[0]} **{wmax[1]} km/h** = "
      f"{wmax[1] / 3.6:.2f} m/s |")
    w("| Master `A.7.8` design basic wind speed | **39 m/s** |")
    w(f"| Ratio | **{39 / (wmax[1] / 3.6):.1f} : 1** |")
    w()
    w("> **These are not the same quantity and the ratio is not an error.** "
      "The deck plots a **monthly mean speed**. IS 875 (Part 3):2015 `V_b` "
      "is a **3-second gust at 10 m with a 50-year return period**. A mean "
      "of 1.8 m/s and a 50-year gust of 39 m/s are entirely compatible. "
      "**Master `A.7.8` is not to be reduced on the strength of slide 24** — "
      "and in any case seismic governs the sentry post **2.4 : 1**, so the "
      "wind case decides nothing.")
    w()

    # --------------------------------------------------------------- 13
    w("## 13. The soil parameters in master `A.6`, checked against measured "
      "data")
    w()
    w("Appendix B gives compaction and shear results for the **murrum** — "
      "the material the engineered fill, the side backfill and the berm will "
      "actually be built from. Master `A.6` and `A.7.3` have carried round "
      "numbers for these since Rev D with no measurement behind either. The "
      "full arithmetic is in calculation `G.8`.")
    w()
    w("### 13.1 Unit weight")
    w()
    w("| | |")
    w("|---|---|")
    w("| Measured, 95 % MDD at OMC, three murrum samples | **19.12 – 19.61 "
      "kN/m³** `[D]` |")
    w(f"| Master `A.6` / `A.7.3` bulk | **{P.GAMMA_BULK:.2f} kN/m³** `[A]` — "
      f"**2–5 % high**, i.e. conservative for lateral load |")
    w("| γ_sat back-figured from the measured MDD, G_s = 2.75 `[A]` | "
      "**21.26 kN/m³** `[R]` |")
    w(f"| Master `A.6` γ_sat | **{P.GAMMA_SAT:.2f} kN/m³** — agrees within "
      f"**1.2 %** |")
    w()
    w("Applied to the **engineered cover**, whose total is held at "
      "**40.65 kPa** by `RC1` / `C17`:")
    w()
    w("| Case | Six-layer sum | vs the held 40.65 |")
    w("|---|---|---|")
    w("| As placed, at the **lowest** measured γ | **38.49 kPa** | "
      "−2.16 (the declared allowance grows from 1.50 to 2.16) |")
    w("| As tabulated in `A.7.3` | 39.15 kPa | −1.50 (the `C17` allowance) |")
    w("| **Fully saturated**, all three soil-like layers `[A]` | "
      "**41.07 kPa** | **+0.42**, which is **+0.09 % of COMB 103** |")
    w()
    w("> **`SG-F8`. The held value of 40.65 kPa brackets both the as-placed "
      "case (lighter) and the fully saturated case (heavier by about 1 %, "
      "which is one tenth of one percent of COMB 103).** `C17`'s declared "
      "allowance turns out to be doing real work. **Nothing changes**: 40.65 "
      "stands, COMB 103 stays **448.15 kPa**, no `.std` file is touched.")
    w()
    w("### 13.2 Shear strength and K₀")
    w()
    w("| Sample | Class | c kg/cm² | φ | 1 − sin φ | vs the assumed 0.50 |")
    w("|---|---|---|---|---|---|")
    for s, tp, cl, omc, mdd, ucs, dsc, phi, qult, sbc in D.APPX_B:
        if phi is None:
            continue
        k0 = 1 - math.sin(math.radians(phi))
        w(f"| {s} | `{cl}` | {dsc:.2f} | {phi}° | **{k0:.4f}** | "
          f"{k0 - P.K0_MASTER:+.4f} |")
    w()
    w("Three granular murrum samples give K₀ **0.426 – 0.455**: the assumed "
      "**0.50 is conservative against all three**. One clayey sand (`SC`, "
      "TP-9, a 0.2 m surface layer) gives 0.546. Carrying even that value to "
      "full depth — which no reading of the profile supports — moves the "
      "wall pressure at the floor from **83.18 to 87.11 kPa**, and against "
      "the 383 kPa blast on the same face that is **+0.84 % on the total**.")
    w()
    w("> **`SG-F9`. The measured shear parameters move the wall design load "
      "by under 1 %.** The walls are blast-governed. `A.6`'s K₀ = 0.50 is "
      "not changed, and the report gives no reason to change it.")
    w()
    w("### 13.3 A limit on all of the above, stated plainly")
    w()
    w("On the report's own rockhead band the box occupies `(−)2.000` to "
      "`(−)6.800` and is therefore **entirely within basalt**. What bears on "
      "the buried walls is rock and the 300 lean-concrete annulus, **not "
      "soil**. The master's *K₀ soil plus full hydrostatic* model is a "
      "conservative idealisation of that, and it is right to keep the whole "
      "hydrostatic term, because water pressure in a jointed rock mass is "
      "real and is two thirds of the load. **The measured soil parameters "
      "are the right check on the berm, the backfill and the cover. They are "
      "not a description of what the buried walls retain.**")
    w()

    # --------------------------------------------------------------- 14
    w("## 14. The black cotton soil — where it is harmless, and two places "
      "it is not")
    w()
    b = D.BC_SOIL
    w("| Property | Measured |")
    w("|---|---|")
    w(f"| Depth | **{b['depth_m'][0]} – {b['depth_m'][1]} m** |")
    w(f"| Liquid limit | {b['LL'][0]} – {b['LL'][1]} % |")
    w(f"| Plastic limit | {b['PL'][0]} – {b['PL'][1]} % |")
    w(f"| Plasticity index | {b['LL'][0] - b['PL'][0]} – "
      f"{b['LL'][1] - b['PL'][1]} % `[R]` |")
    w(f"| **Free swell index** | **{b['free_swell'][0]} – "
      f"{b['free_swell'][1]} %** |")
    w(f"| IS 1498 classification | **{b['classification']}** |")
    w(f"| SBC | 0.25 – 0.27 kg/cm² = **{kpa(0.25):.1f} – {kpa(0.27):.1f} "
      f"kPa** |")
    w()
    w("A free swell index above 50 % is the top band of the IS 1498 scale — "
      "**very high swelling potential**. Deck slide 30 puts it in plain "
      "words: the soil *“contracts and produce cracks in dry season, 10 to "
      "15 cm wide extending to maximum depth of 1 m”* and is *“Not suitable "
      "for foundation”*.")
    w()
    w("### 14.1 Where it is harmless — which is most of the project")
    w()
    w("**Nothing structural founds in it.** The mat is at `(−)6.700` and "
      "sentry footing F1 at `(−)2.000`, both in basalt, both far below the "
      "0.18–1.0 m black cotton horizon. Master `B.8.7`'s insistence that F1 "
      "bears *“on IN-SITU ROCK, never on backfill”* — and the decision to "
      "put the sentry post **≥ 10 m clear of the shelter excavation** — are "
      "now backed by a measurement. **No action.**")
    w()
    w("### 14.2 `SG-F13` — the covered entry stairwell's stepped raft")
    w()
    w("Master `A.4.7`: *“Stepped RC raft 300 thk **on compacted fill**”*, "
      "stepping from the top landing at `0.000` down to the platform at "
      "`(−)2.000`. With 300 of raft, **its top founds at about `(−)0.300` — "
      "inside the black cotton horizon at two of the report's three "
      "locations.**")
    w()
    w("*“On compacted fill”* implies the black cotton is stripped and "
      "replaced, but **no specification anywhere says so**, **no "
      "strip-and-replace item exists in the BOQ**, and a very-high-swelling "
      "CH clay under a stepped raft is a **heave** problem, not a bearing "
      "one — the SBC of 24.5 kPa is irrelevant; the 60–65 % free swell is "
      "not.")
    w()
    w("The stairwell is declared **expendable** against blast (master `B.6`, "
      "Rev F drawing note 8) — but **heave is a service-life problem, not a "
      "blast one, and this stair is the only primary access to the "
      "shelter**. `SG-V6`")
    w()
    w("### 14.3 `SG-F14` — the concealment layer")
    w()
    w("Master `A.7.3` puts **300 of topsoil / turf** at the top of the "
      "cover, and `CAM2` makes it *the concealment layer*, **“re-laid from "
      "the site's own stockpile.”** If the site's own topsoil is this CH clay "
      "at FSI 60–65 %, then the concealment layer is a very-high-swelling "
      "clay 300 mm thick:")
    w()
    w("- it **cracks in the dry season**, and a cracked, patchy turf is a "
      "**concealment defect** — which is `CAM2`'s entire subject;")
    w("- the cracks are a **direct infiltration path** into the 150 granular "
      "filter immediately below it;")
    w("- wetting and drying cycles **pump clay fines into that filter**, "
      "which is the one thing the filter exists to stop (`A.7.3`: *“Stops "
      "fines clogging”*).")
    w()
    w("**The load is unaffected** — 300 at 18 kN/m³ = 5.40 kPa is right for "
      "a black cotton soil — so **no calculation moves**. What is missing is "
      "a **specification**: either qualify the stockpiled topsoil against a "
      "swell limit, or import a non-expansive topsoil and price it. Neither "
      "exists. `BS1`'s 1:50 crossfall on the burster slab still works and is "
      "unaffected; it is the filter above it that would see more water and "
      "more fines than assumed. `SG-V7`")
    w()

    # --------------------------------------------------------------- 15
    w("## 15. The P1 deck against its own cited source")
    w()
    w("Deck slides 29 and 30 both carry the source line *“Source : SEMT "
      "wing, CME”*. **Three of their statements are not in that report.** "
      "They are listed because the deck is a **presented** document and the "
      "same claims will be presented again unless they are corrected at "
      "source. **None of them affects the design**, because the design does "
      "not use any of them.")
    w()
    ucs_uns = sorted(r[5] for r in D.APPX_C if r[0] == "UNSOAKED")
    w("| Deck statement | What the report actually says | Effect on the "
      "design |")
    w("|---|---|---|")
    w(f"| *“Safe Bearing Capacity = 300 kN/m² at 1.5 m depth from Top”* | "
      f"300 kPa = {300 / P.KGCM2_KPA:.2f} kg/cm², which is **not any value "
      f"in the report**. At 1.5 m it gives CH clay {kpa(0.27):.1f}, murrum "
      f"{kpa(4.27):.1f}, broken rock {kpa(10):.0f}, sound basalt "
      f"{kpa(20):.0f} soaked / {kpa(33):.0f} unsoaked kPa | **None.** It is "
      f"6.5× below the lowest rock value at that depth — conservative — and "
      f"master `A.6` uses the IS 1904 presumptive 3240 kPa instead |")
    w(f"| *“Murrum … SBC of 25 – 30 kg/cm²”* | the report's murrum SBCs are "
      f"**2.07, 4.27, 4.66 and 5.18 kg/cm²**. 25–30 is the **sound basalt "
      f"unsoaked** band | **None.** But it assigns **rock** strength to "
      f"**soil**, about 5–6× high |")
    w(f"| *“Compressive strength ranging from 609 – 900 kg/cm² in unsoaked "
      f"condition”* | Appendix C's unsoaked results are **{ucs_uns}** — a "
      f"range of **{min(ucs_uns)} to {max(ucs_uns)}**. **609 appears nowhere "
      f"in the report** | **None.** The upper bound is right |")
    w()
    w("Two deck statements are **right and important**:")
    w()
    w("- *“Ultimate Bearing Capacity = S.B.C × 2.5”* — this is Appendix B's "
      "own relationship read backwards, with the report's stated factor of "
      "safety. **Correct.**")
    w("- *“Proposed structure safe for water table at depth of 2 m below "
      "GL”* — **true, and now traceable**. It is the provenance of "
      "`(−)2.000`. See §10.")
    w()
    w("`SG-V8`")
    w()

    # --------------------------------------------------------------- 16
    w("## 16. Findings")
    w()
    w("| Ref | Finding |")
    w("|---|---|")
    for n, t in [
        ("`SG-F1`", "The SEMT report reproduces completely from its own "
                    "inputs — soil, rock strength and rock bearing. **It is "
                    "usable.**"),
        ("`SG-F2`", "**THE INVESTIGATION REACHED ABOUT 1.5 m; THE STRUCTURE "
                    "FOUNDS AT 6.8 m.** 5.3 m of unlogged ground under the "
                    "whole structure. **The governing finding.**"),
        ("`SG-F3`", "The presumptive SBC is 65 % above the measured *soaked* "
                    "value — and no element cares. Worst utilisation "
                    "12.5 % → 20.6 %."),
        ("`SG-F4`", "In service the structure is **lighter than the ground "
                    "it replaces**, by ≈ 105 kPa. Settlement was never the "
                    "problem; flotation always was."),
        ("`SG-F5`", "The report's rockhead band (0.9–1.5 m) is **entirely at "
                    "or above** the master's assumed band (1.5–2.0 m). "
                    "+118 m³ of rock, ≈ 2 days."),
        ("`SG-F6`", "*“No water table”* means **“not reached”**. `K.2 A2` "
                    "stays `[ASSUMED]` and stays open — the provenance of "
                    "`(−)2.000` is now recorded, its verification is not."),
        ("`SG-F7`", "**The monsoon groundwater monitoring is programmed "
                    "outside the monsoon** (12 Nov – 4 Dec), on the critical "
                    "path."),
        ("`SG-F8`", "The held cover value of 40.65 kPa **brackets both** the "
                    "as-placed and the fully saturated case. `C17`'s "
                    "declared allowance is doing real work."),
        ("`SG-F9`", "Measured shear parameters move the wall design load by "
                    "**under 1 %**. The walls are blast-governed."),
        ("`SG-F10`", "The deck's contour map and its elevation profile "
                     "disagree by **12–16 m** in level and ≈ 4× in gradient."),
        ("`SG-F11`", "The two supplied documents disagree on annual rainfall "
                     "by **27 – 52 %**. October is the outlier."),
        ("`SG-F12`", "**Seismic Zone III is externally corroborated** and "
                     "the master's A_h values reproduce exactly. The only "
                     "master input this section can corroborate."),
        ("`SG-F13`", "The **entry stairwell's stepped raft founds in "
                     "very-high-swelling CH clay** with no strip-and-replace "
                     "specification anywhere."),
        ("`SG-F14`", "**The concealment layer may be a very-high-swelling CH "
                     "clay** re-laid from the site's own stockpile, over the "
                     "filter it would clog."),
    ]:
        w(f"| {n} | {t} |")
    w()

    # --------------------------------------------------------------- 17
    w("## 17. Open items — `SG-V1` to `SG-V10`")
    w()
    w("**None of these is resolved, and that is deliberate.** Each needs "
      "something this project does not contain.")
    w()
    w("| Ref | Item | What would close it |")
    w("|---|---|---|")
    for n, item, close in [
        ("`SG-V1`", "**The geotechnical data is off-site.** The trial pits "
                    "are at the G, H and Mess buildings. **No investigation "
                    "has ever been made on the project plot.**",
                    "Locate WBS `A1075` **on this plot**"),
        ("`SG-V2`", "**Depth of investigation.** ≈ 1.5 m against a formation "
                    "at `(−)6.800` and a sump base at `(−)8.000`.",
                    "Boreholes with core recovery and RQD to well below "
                    "`(−)6.800`, logging **every flow contact and red-bole "
                    "seam**, with packer permeability at the contacts"),
        ("`SG-V3`", "**The monsoon GWT monitoring window is not in the "
                    "monsoon** (12-11-26 → 04-12-26, TF 0).",
                    "A project-owner decision: a standpipe piezometer in the "
                    "`A1075` borehole read through a **full monsoon**, and "
                    "the programme consequence accepted"),
        ("`SG-V4`", "**Site level and fall.** The contour map and the "
                    "elevation profile disagree by 12–16 m; nothing ties "
                    "either to the project datum.",
                    "A levelled **benchmark on the plot** and a spot-level "
                    "survey; then the cut-and-fill, berm toe and `BS1` "
                    "daylight point can be drawn"),
        ("`SG-V5`", "**Annual rainfall.** 759.6 mm against 500–600 mm; the "
                    "**October figure** does not fit a Deccan year.",
                    "A **named IMD station and period of record** — and "
                    "separately, an IDF source for the 50 mm/h intensity "
                    "(`DR-D1`)"),
        ("`SG-V6`", "**The entry stairwell raft founds in black cotton "
                    "soil.** No strip-and-replace specification or BOQ item.",
                    "A specification for stripping and replacing the CH "
                    "horizon under the stepped raft, and the quantity priced"),
        ("`SG-V7`", "**The 300 concealment turf may be very-high-swelling CH "
                    "clay** re-laid from the site's own stockpile.",
                    "A swell limit on the stockpiled topsoil, or imported "
                    "non-expansive topsoil, priced — a `CAM2` coordination "
                    "decision"),
        ("`SG-V8`", "**Three P1 deck statements are not in the report they "
                    "cite** (SBC 300 kN/m², murrum SBC 25–30 kg/cm², UCS "
                    "609–900 kg/cm²).",
                    "Correct them at source before the next presentation. "
                    "**No design value is affected**"),
        ("`SG-V9`", "**The project has no coordinates.** The owner's Google "
                    "Maps pin could not be resolved in this session "
                    "(egress 403).",
                    "The latitude and longitude, supplied directly"),
        ("`SG-V10`", "**The date of the SEMT field work is not stated**, so "
                     "the season in which *“no water table”* was observed "
                     "cannot be established.",
                     "The field-work dates from the SEMT wing, or acceptance "
                     "that the observation is season-unknown"),
    ]:
        w(f"| {n} | {item} | {close} |")
    w()

    # --------------------------------------------------------------- 18
    w("## 18. What this section changed, and what it did not")
    w()
    w("**Changed:** nothing in the design.")
    w()
    w("| | |")
    w("|---|---|")
    w("| Design values in Parts A, B, D, F, L | **untouched** |")
    w("| Loads, thicknesses, bars, levels | **untouched** |")
    w("| `.std` models | **untouched — and STAAD.Pro was not run** |")
    w("| Existing DXF, schedules, calculations | **untouched** |")
    w("| BOQ quantities, rates, dates, floats | **untouched** — `WM2` "
      "adopted the owner's own documents and they govern |")
    w("| **The main staircase** | **untouched — frozen, 24R @ 170.8333 / "
      "280, 3 flights × 8, total rise 4100** |")
    w("| Any `[ASSUMED]` tag | **not one converted, downgraded or deleted** |")
    w()
    w("**Added:** this section, five schedules, a calculation printout, "
      "three A1 drawings, a QA/QC report, and — in the master — Part `H.22`, "
      "provenance notes against `A.6` and `K.2`, ten new open items in "
      "`K.1b`, and the manifest entries.")
    w()
    w("### 18.1 What this section is still not")
    w()
    w("- It is **not a site investigation report**. It is a reading of "
      "somebody else's, for other buildings, that stopped 5.3 m above the "
      "founding horizon.")
    w("- It is **not a site plan**. Master gap **D3 stays open**: no "
      "boundary, no dimension, no benchmark, no coordinate.")
    w("- It **does not close `DR-D1`**, `EL-V4`, `EL-V6`, `CAM-V2`, or any "
      "`K.2` assumption.")
    w("- It is **not construction-ready**, and neither is the confirmatory "
      "investigation it calls for — that is `A1075` and `A1080` on the "
      "programme, both on the critical path, both still to happen.")
    w()
    w("---")
    w()
    w("## 19. References")
    w()
    w("| Code / document | Used for |")
    w("|---|---|")
    w("| **IS 1498:1970** | Classification and identification of soils — "
      "CH, GM, GP, SC, free swell index |")
    w("| **IS 2720** Pts IV, VIII, X, XIII, XL | Classification, compaction, "
      "UCS, direct shear, free swell — the report's own test methods |")
    w("| **IS 1121 (Pt I)** | Compressive strength of rock |")
    w("| **IS 12070:1987** | Design and construction of shallow foundations "
      "on rocks — Cl. 6 bearing, Table 2 broken bedrock |")
    w("| **IS 1904:1986** | Presumptive bearing capacity, Table 1, hard "
      "rock 3240 kPa — the master's `A.6` value |")
    w("| **IS 1893 (Part 1):2016** | Seismic zone and Z; the report cites "
      "the **1984** map |")
    w("| **IS 875 (Part 3):2015** | Basic wind speed — §12.4 |")
    w("| **IS 2470 (Part 2):1985** Cl. 4 | Percolation test — still "
      "mandatory, `K.2 A7` |")
    w("| **IS 2720 (Part 28)** | In-situ density testing of backfill, "
      "WBS `A7015` |")
    w(f"| **{D.REPORT['code']}** | The sub-soil investigation itself |")
    w("| **P1 presentation deck** | Site selection, setting and meteorology |")
    w()
    w("---")
    w()
    w(f"*Site Selection and Geotechnical package, revision **{P.REV}**, "
      f"{P.PACKAGE_DATE}. Compiled from the two supplied documents and the "
      f"master project state. Every value is tagged. Nothing in this "
      f"document was invented, and nothing that was assumed has been made "
      f"confirmed.*")
    w()


# =====================================================================
def readme():
    return f"""# Site Selection and Geotechnical — revisions {P.REV} and {P.PKG_REV}

**{P.PACKAGE_DATE}** · {P.GEOM_REV} · **{P.STATUS}**

The project's first site selection and geotechnical section. Until this
revision, master Part J drew `[SITE INVESTIGATION]` as a root node with
**nothing feeding it**, and every parameter in master `A.6` was `[ASSUMED]`
with no source.

## The one fact that governs the package

**The sub-soil investigation reached about 1.5 m. The structure founds at
`(−)6.800`.** Everything the project holds about the ground below `(−)2.000`
— rockhead continuity, red-bole seams, k_s, the design groundwater table — is
extrapolation, and the supplied report cannot be read as confirming any of it.

## What is here

| | |
|---|---|
| `Documentation/SITE_SELECTION_AND_GEOTECHNICAL_REPORT.md` | **the section** — site selection, setting, geology, the investigation, bearing, rockhead, groundwater, seismicity, meteorology, the black cotton soil, 14 findings, 10 open items |
| `Documentation/SG_DRAWING_INDEX.md` | the three drawings and what each is for |
| `Schedules/TRIAL_PIT_SCHEDULE` | the stratum log, `.md` + `.csv` |
| `Schedules/SOIL_PROPERTY_SCHEDULE` | Appendices A and B |
| `Schedules/ROCK_STRENGTH_SCHEDULE` | Appendix C, soaked and unsoaked |
| `Schedules/METEOROLOGICAL_SCHEDULE` | wind, rainfall, temperature |
| `Schedules/GEOTECHNICAL_PARAMETER_RECONCILIATION` | every `A.6` / `K.2` item against the new evidence |
| `Calculations/SG_CALC_OUTPUT.txt` | G.1–G.14, every conversion and check with its arithmetic shown |
| `QAQC/SG_QAQC.md` · `QAQC/SG_DRAWING_VALIDATION.txt` | consistency checks and the DXF validator output |
| `Documentation/SITE_LAYOUT_AND_EXTERNAL_WORKS.md` | **SG2** — where the septic tank and the soak pits go, and why. Orientation, the reserve, the positions, the offsets demonstrated, the five pipe lengths, **`SG2-F1`** (the soak pit is a depth problem), the reserved fallback, the percolation-test locations, the `SG-V3` ruling, the rainfall amendment, and what `D3` still covers |
| `Schedules/EXTERNAL_WORKS_SCHEDULE` · `EXTERNAL_PIPE_RUN_SCHEDULE` · `SITING_CLEARANCE_SCHEDULE` · `SG2_OPEN_ITEM_STATUS` | **SG2**, `.md` + `.csv` |
| `Calculations/SG2_SITE_CALC_OUTPUT.txt` | **SG2** — S.1–S.12, every clearance computed against the rule it has to meet |
| `DXF/` | `SG-001`, `SG-101`, **`SG-102`**, `SG-201`, **`SG-202`** — A1, AutoCAD 2010 ASCII, **0 errors** |
| `Scripts/sg_build_all.py` | rebuilds the whole package |

## Sources

1. **{D.REPORT['code']}** — *{D.REPORT['title']}*, {D.REPORT['author']}.
   Raised on {D.REPORT['request']}. **{D.N_TRIAL_PITS} trial pits, 3
   locations, no boreholes, no in-situ testing.**
2. **P1 presentation deck** — *{D.DECK['title']}*, {D.DECK['team']},
   {D.DECK['pages']} slides.
3. **Location pin** `{D.PIN_URL}` — **{D.PIN_STATUS}**

## What this package does NOT do

- It **resolves nothing**. Master rule `M.6` forbids converting an
  `[ASSUMED]` into a confirmed fact, and not one `K.2` assumption is closed.
- It **does not close master gap D3** (no site plan). Imagery is not a site
  plan.
- It **changes no design value, no `.std` file, no BOQ quantity, no rate, no
  date and no float**, and modifies **no existing file** in any other
  package. The only files outside this directory that change are
  `master/MASTER_PROJECT_STATE.md` (Part `H.22` and cross-references) and
  `master/QUICK_STATE.md`.
- **STAAD.Pro was not run.** Nothing here is an analysis.
- The **main staircase is untouched**.

## Rebuild

```
python3 Scripts/sg_build_all.py
```

Runs `sg_calc.py`, `sg_schedules.py`, `sg_docs.py` and `sg_sheets.py`, then
validates the drawings with the project's own shared validator
(`Drainage/Scripts/mep_validate.py`). `sg_dxf.py` subclasses the shared
`mep_dxf.py` and uses the `SCOPE_NOTE` / `TB_SCOPE` / `DATE` hooks that
CAM2/FS2 added — **no shared library is modified**, so Drainage, HVAC,
Schedule of Finishes, Fire and Life Safety, Site and Concealment, EMP
Protection and Electrical all regenerate byte-identically.
"""


def drawing_index():
    return f"""# SG DRAWING INDEX

**Site Selection and Geotechnical package** · current revision **{P.PKG_REV}** ·
{P.PKG_DATE} · {P.GEOM_REV} · **{P.STATUS}**

**Five A1 sheets**, AutoCAD 2010 ASCII DXF, drawn in paper millimetres, plotted
1:1, on the project's existing sheet standard (`mep_dxf.Sheet`, which
subclasses `sc_dxflib.Sheet` — the same standard as the issued R, D, M, A-6xx,
F, C, EM and E series). **Validated 0 errors, 0 warnings, 0 text overlaps.**

| Sheet | Rev | Title | What it is | What it is **not** |
|---|---|---|---|---|
| **SG-001** | SG1 | Site and geotechnical design basis | The evidence key, the two sources and their limits, the parameter reconciliation against master `A.6` / `K.2`, and all fourteen SG1 findings on one sheet | not a specification — it states positions, not instructions |
| **SG-101** | SG1 | Site setting, selection and meteorology | A **diagram** of the plot's setting, with the SWOT, the meteorological tables and the level conflict | **NOT A SITE PLAN.** No boundary, no dimension, no benchmark, no coordinate, no scale |
| **SG-102** | **SG2** | **Site layout plan** | **The project's first true site layout plan.** 1:150, project coordinates, **+X = EAST**, every external structure placed and every clearance dimensioned from confirmed geometry; plus a 1:900 location key showing the owner's 50 m envelope | **still not a survey.** It carries, on its face, the list of what is missing — boundary, benchmark, well, fence, services, wind rose |
| **SG-201** | SG1 | Geotechnical profile against the structure section | The three trial-pit logs at true level against the shelter section, 1:25 both ways, with everything below `(−)1.500` an explicit **NO DATA** zone | not a ground model — the ground below the logs is drawn as **unknown**, because it is |
| **SG-202** | **SG2** | **External works siting and the soak pit finding** | The pit drawn against the ground it is cut into, both water-table readings, the two independent checks behind **`SG2-F1`**, the reserved fallback, and the `SG-V3` ruling | **not a redesign of SK-01.** The percolation test governs; this sheet says the number *before* the test |

> **Sheet revision.** All five title blocks read **{P.PKG_REV}**, because a
> drawing carries the revision it is issued at. `SG-001`, `SG-101` and `SG-201`
> were re-issued at SG2 with **no content change** beyond the revision and
> sheet-count fields. The SG1 *documents* stay at SG1 — that revision happened
> and Part H preserves it (rule `M.11`).

## The point of SG-201 and SG-102

`SG-201` shows **what is not known**: below `(−)1.500` it carries no strata, no
rockhead line and no water line, only a hatched *NO DATA* zone through which
the mat, the sump and 5.3 m of excavation pass.

`SG-102` shows **what can now be fixed in spite of that** — and marks, in the
same breath, the eight things that still cannot be. Between them they are an
honest pair: the layout exists, the survey does not.

## Open items flagged on the sheets

`SG-V1`…`SG-V10` · `SG2-V1`…`SG2-V5` · and the master items they touch:
`A1` `A2` `A3` `A4` `A5` `A7` `A8` `D3` `U4` `DR-D1` `CAM-V2`
"""


def main():
    os.makedirs(DOC, exist_ok=True)
    del L[:]
    report()
    with open(os.path.join(DOC,
                           "SITE_SELECTION_AND_GEOTECHNICAL_REPORT.md"),
              "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    with open(os.path.join(DOC, "00_README.md"), "w", encoding="utf-8") as f:
        f.write(readme())
    with open(os.path.join(DOC, "SG_DRAWING_INDEX.md"), "w",
              encoding="utf-8") as f:
        f.write(drawing_index())
    print("SG1 documentation:")
    print(f"  SITE_SELECTION_AND_GEOTECHNICAL_REPORT.md   {len(L)} lines")
    print("  00_README.md")
    print("  SG_DRAWING_INDEX.md")


if __name__ == "__main__":
    main()
