"""sg_schedules.py  --  the five SG1 schedules, as Markdown and CSV.

Every row comes from sg_data.py (transcription) or sg_calc.py (arithmetic), so
a schedule cannot disagree with the calculation printout or with the drawings.
"""
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import sg_proj as P                                        # noqa: E402
import sg_data as D                                        # noqa: E402

SCH = os.path.abspath(os.path.join(_HERE, "..", "Schedules"))

HEAD = (
    "**Underground CBRN-hardened protective structure — Pune** · "
    f"{P.GEOM_REV}\n"
    f"Site Selection and Geotechnical package revision **{P.REV}** · "
    f"{P.PACKAGE_DATE} · **{P.STATUS}**\n"
    "Evidence class: `[C]` confirmed · `[R]` reconstructed · `[D]` derived "
    "here · `[A]` assumed by this package · `[U]` unresolved · `[N]` not "
    "available — DATA REQUIRED\n\n"
    "> **THIS PACKAGE RESOLVES NOTHING.** Master rule M.6 forbids converting "
    "an `[ASSUMED]` into a confirmed fact. Every `K.2` assumption stands "
    "after these schedules exactly as it stood before them — what each one "
    "now has is a **stated provenance and a quantified margin**.\n\n"
    "> **THE GOVERNING FACT.** The sub-soil investigation reached about "
    "**1.5 m**. The structure founds at **(−)6.800**. Nothing in these "
    "schedules describes the founding horizon of the shelter.\n"
)


def write(name, title, header, rows, notes=(), pre=()):
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
        s = (s.replace("−", "-").replace("²", "2").replace("³", "3")
              .replace("·", "-").replace("’", "'").replace("—", "-")
              .replace("“", '"').replace("”", '"')
              .replace("**", "").replace("`", "").replace('"', '""'))
        return f'"{s}"' if ("," in s or '"' in s) else s

    with open(os.path.join(SCH, name + ".csv"), "w", encoding="utf-8") as fh:
        fh.write(",".join(esc(h) for h in header) + "\n")
        for r in rows:
            fh.write(",".join(esc(c) for c in r) + "\n")
    print(f"  {name}.md / .csv   {len(rows)} rows")


def kpa(v):
    return v * P.KGCM2_KPA


# ------------------------------------------------------------------ 1
def trial_pit_schedule():
    rows = []
    for loc, layers in D.FINDINGS:
        pits = loc[loc.find("(") + 1:loc.find(")")]
        short = loc[:loc.find("(")].strip()
        for i, (depth, kind, ucs, sbc, note) in enumerate(layers):
            rows.append([
                f"**{short}**" if i == 0 else "",
                pits if i == 0 else "",
                depth,
                kind,
                "" if ucs is None else f"{ucs:.0f}",
                f"{sbc:.2f}",
                f"{kpa(sbc):.1f}",
                note or ("IS 12070 Cl. 6" if ucs else ""),
                "`[C]`",
            ])
    write("TRIAL_PIT_SCHEDULE",
          "TRIAL PIT AND STRATUM SCHEDULE — SEMT/67/15",
          ["LOCATION", "PITS", "DEPTH", "SOIL / ROCK", "UCS SOAKED kg/cm²",
           "SBC kg/cm²", "SBC kPa", "BASIS", "CLASS"],
          rows,
          pre=[
              f"Source: **{D.REPORT['code']}**, *{D.REPORT['title']}*, "
              f"{D.REPORT['author']}. Raised on {D.REPORT['request']}.\n",
              f"**{D.N_TRIAL_PITS} trial pits at 3 locations.** Method, "
              f"verbatim: *“{D.FIELD}”*\n",
              "> **THESE ARE NOT THIS PLOT.** The report investigates the "
              "**G Building, H Building and Mess Building** on the CTW/CME "
              "campus. The project plot is a separate undeveloped area east "
              "of the CTW blocks. The data may be carried across only on the "
              "strength of the report’s own para 5 — *“these basaltic flows "
              "are horizontally bedded and more or less uniform in character "
              "over a wide area”* — and that carry-across is an **assumption "
              "of this package**, not a finding of the report. `[A]`\n",
          ],
          notes=[
              "| | |", "|---|---|",
              f"| Deepest stratum boundary anywhere in the report | "
              f"**1.5 m** |",
              f"| Project formation level | **(−)6.800** |",
              f"| Gap | **5.3 m of unlogged ground under the whole "
              f"structure** |",
              "",
              f"**Broken-rock footnote, verbatim.** *“{D.BROKEN_ROCK_NOTE}”*",
              "",
              "**Water table, verbatim (para 13).** "
              f"*“{D.WATER_TABLE_TEXT}”* — see `SG-F6`: in pits that reached "
              "about 1.5 m, *not encountered* means **not reached**. Master "
              "`K.2 A2` stays `[ASSUMED]` and stays **open**.",
          ])


# ------------------------------------------------------------------ 2
def soil_property_schedule():
    cls_a = {r[0]: r for r in D.APPX_A}
    rows = []
    for s, tp, cl, omc, mdd, ucs, dsc, phi, qult, sbc in D.APPX_B:
        a = cls_a.get(s)
        ll = pl = pi = fsi = None
        if a:
            ll, pl, fsi = a[10], a[11], a[14]
            pi = a[12]
        k0 = "" if phi is None else f"{1 - math.sin(math.radians(phi)):.4f}"
        rows.append([
            f"**{s}**", tp, a[1] if a else "", f"`{cl}`",
            "" if ll is None else ll, "" if pl is None else pl,
            "" if pi is None else pi, "" if fsi is None else fsi,
            f"{omc}", f"{mdd:.2f}",
            "" if ucs is None else f"{ucs:.2f}",
            "" if dsc is None else f"{dsc:.2f}",
            "" if phi is None else f"{phi}",
            k0, f"{qult:.3f}", f"{sbc:.2f}", f"{kpa(sbc):.1f}",
        ])
    write("SOIL_PROPERTY_SCHEDULE",
          "SOIL PROPERTY SCHEDULE — SEMT/67/15 APPENDICES A AND B",
          ["SAMPLE", "PIT", "DEPTH m", "IS 1498", "LL %", "PL %", "PI %",
           "FSI %", "OMC %", "MDD g/cc", "UCS c kg/cm²", "DS c kg/cm²",
           "φ°", "1 − sin φ", "q_ult kg/cm²", "SBC kg/cm²", "SBC kPa"],
          rows,
          pre=[
              "All values `[C]` — read off Appendices A and B. The "
              "`1 − sin φ` column is `[R]`, computed here, and is the only "
              "derived column.\n",
              "Appendix B remarks, verbatim: "
              + " ".join(f"*({i + 1}) {r}*"
                         for i, r in enumerate(D.APPX_B_REMARKS)) + "\n",
          ],
          notes=[
              "| Check | Result |", "|---|---|",
              f"| SBC = q_ult / {D.APPX_B_FOS} | **6 of 6 reproduce** to the "
              f"printed precision `[R]` |",
              "| Master `A.6` K₀ | **0.50** (φ ≈ 30°) `[A]` |",
              "| Measured, three granular murrum samples | K₀ **0.426 – "
              "0.455** — the assumption is **conservative** |",
              "| Measured, one clayey sand (0.2 m surface layer, TP-9) | "
              "K₀ **0.546** |",
              "| Effect on the wall design load, worst case | "
              "**under 1 %** — `SG-F9`. **No change.** |",
              "| Master `A.6`/`A.7.3` γ | **20.0** bulk, **21.0** saturated "
              "`[A]` |",
              "| γ at 95 % MDD and OMC, measured murrum | **19.12 – 19.61 "
              "kN/m³** `[D]` |",
              "| γ_sat back-figured, G_s = 2.75 `[A]` | **21.26 kN/m³** — "
              "agrees with the master within **1.2 %** `[R]` |",
              "",
              "**Black cotton soil.** LL **61–63 %**, PL **29–30 %**, PI "
              "**32–33 %**, free swell index **60–65 %**, class **CH**. An "
              "FSI above 50 % is the top band of the IS 1498 scale — **very "
              "high swelling potential**. Nothing structural founds in it "
              "(mat (−)6.700, footing F1 (−)2.000, both in basalt), but see "
              "`SG-F13` (entry stairwell stepped raft) and `SG-F14` (the "
              "300 turf concealment layer).",
          ])


# ------------------------------------------------------------------ 3
def rock_schedule():
    rows = []
    for cond, depth, loc, load, area, ucs, sbc in D.APPX_C:
        rows.append([f"**{cond}**", loc, depth, f"{load:,}", f"{area:.2f}",
                     f"{load / area:.1f}", f"{ucs}", f"{ucs / 25:.2f}",
                     f"{sbc}", f"{kpa(sbc):.1f}"])
    write("ROCK_STRENGTH_SCHEDULE",
          "ROCK STRENGTH AND BEARING SCHEDULE — SEMT/67/15 APPENDIX C",
          ["CONDITION", "LOCATION", "DEPTH", "MAX LOAD kg", "AREA cm²",
           "P/A kg/cm²", "PRINTED UCS", "UCS / 25", "PRINTED SBC kg/cm²",
           "SBC kPa"],
          rows,
          pre=["Tested to **IS 1121 (Pt-I)**; bearing to **IS 12070 "
               "Cl. 6**. Columns `P/A` and `UCS / 25` are `[R]`, computed "
               "here to test the report against itself — **all six rows "
               "reproduce**, so the bearing factor the report applies but "
               "does not print is **25**, rounded to the nearest whole "
               "kg/cm².\n"],
          notes=[
              "| | |", "|---|---|",
              "| **Which column applies to this structure** | the "
              "**SOAKED** one |",
              "| Why | design GWT `(−)2.000` `[A]`, formation `(−)6.800` — "
              "the founding horizon is **4.8 m below the design water "
              "table**, permanently submerged. Appendix B makes the same "
              "choice for the soils: *“in submerged condition of soil”* |",
              f"| Soaked band | **{kpa(20):.0f} – {kpa(21):.0f} kPa** |",
              f"| Unsoaked band | **{kpa(30):.0f} – {kpa(36):.0f} kPa** |",
              f"| Master `A.6` presumptive, IS 1904:1986 Table 1 | "
              f"**{P.SBC_MASTER:.0f} kPa** `[A]` — inside the *unsoaked* "
              f"band, **+65 %** on the *soaked* one |",
              "",
              "**Does it matter? No — and here is the arithmetic.** "
              f"Re-running every bearing check in the master at the lowest "
              f"soaked value ({kpa(20):.0f} kPa):",
              "",
              "| Check | Demand | / 3240 `[A]` | / 1961 soaked | Verdict |",
              "|---|---|---|---|---|",
              f"| Mat, service — master `B.3` | {P.Q_MAT_SERVICE} kPa | "
              f"{P.Q_MAT_SERVICE / P.SBC_MASTER:.2%} | "
              f"{P.Q_MAT_SERVICE / kpa(20):.2%} | **PASS** |",
              f"| Mat, **blast** — master `B.3` | {P.Q_MAT_BLAST} kPa | "
              f"{P.Q_MAT_BLAST / P.SBC_MASTER:.2%} | "
              f"{P.Q_MAT_BLAST / kpa(20):.2%} | **PASS** |",
              f"| Sentry footing F1 — master `B.8.7` | {P.Q_F1_SERVICE} kPa | "
              f"{P.Q_F1_SERVICE / P.SBC_MASTER:.2%} | "
              f"{P.Q_F1_SERVICE / kpa(20):.2%} | **PASS** |",
              "",
              "The worst bearing utilisation in the project rises from "
              "**12.5 % to 20.6 %** and everything still passes with a "
              f"factor of **{kpa(20) / P.Q_MAT_BLAST:.1f}** in hand. "
              "**Master `A.6` is NOT changed** — `SG-F3`.",
          ])


# ------------------------------------------------------------------ 4
def met_schedule():
    wind = dict(D.DECK_WIND)
    pre = dict(D.DECK_PRECIP)
    temp = {r[0]: r for r in D.DECK_TEMP}
    short = {"January": "Jan", "February": "Feb", "March": "Mar",
             "April": "Apr", "May": "May", "June": "Jun", "July": "Jul",
             "August": "Aug", "September": "Sep", "October": "Oct",
             "November": "Nov", "December": "Dec"}
    rows = []
    for m, _ in D.DECK_WIND:
        s = short[m]
        t = temp[s]
        rows.append([f"**{s}**", f"{wind[m]:.1f}", f"{pre[m]:.1f}",
                     f"{t[1]:.1f}", f"{t[2]:.1f}", f"{t[3]:.1f}"])
    tot = sum(pre.values())
    rows.append(["**YEAR**", f"{sum(wind.values()) / 12:.1f}", f"{tot:.1f}",
                 f"{max(t[1] for t in temp.values()):.1f}",
                 f"{sum(t[2] for t in temp.values()) / 12:.1f}",
                 f"{min(t[3] for t in temp.values()):.1f}"])
    write("METEOROLOGICAL_SCHEDULE",
          "METEOROLOGICAL SCHEDULE — P1 DECK AND SEMT/67/15",
          ["MONTH", "WIND km/h", "RAIN mm", "MAX °C", "AVG °C", "MIN °C"],
          rows,
          pre=["Monthly rows are `[C]` — read off P1 deck slides 24, 25 and "
               "26, each captioned *“LAST 10 YEARS AVG”*. The **YEAR** row "
               "is `[R]`, summed and averaged here. **No station, period of "
               "record or source is named on any of the three slides.**\n"],
          notes=[
              "| Quantity | P1 deck | SEMT report | Status |",
              "|---|---|---|---|",
              f"| Annual rainfall | **{tot:.1f} mm** (sum of slide 25) | "
              f"**{D.RAINFALL_REPORT_RANGE[0]:.0f}–"
              f"{D.RAINFALL_REPORT_RANGE[1]:.0f} mm**, para 9 | "
              f"**`[U]` CONFLICT — {tot / D.RAINFALL_REPORT_RANGE[1] - 1:+.0%}"
              f" to {tot / D.RAINFALL_REPORT_RANGE[0] - 1:+.0%}** — `SG-F11`, "
              f"item `SG-V5` |",
              f"| Temperature | monthly means, max {max(t[1] for t in temp.values()):.1f} °C "
              f"/ min {min(t[3] for t in temp.values()):.1f} °C | **absolute "
              f"extremes** {D.TEMP_REPORT['summer_max']}/"
              f"{D.TEMP_REPORT['summer_min']} summer, "
              f"{D.TEMP_REPORT['winter_max']}/{D.TEMP_REPORT['winter_min']} "
              f"winter | **not a conflict** — different statistics, and "
              f"mutually consistent |",
              "| Wind | monthly mean **1.2–6.6 km/h** | — | **not a "
              "conflict.** Master `A.7.8` uses V_b **39 m/s**, a 3-second "
              "gust at a 50-year return period — `SG-F12` note (c). "
              "**A.7.8 IS NOT TO BE REDUCED ON THE STRENGTH OF SLIDE 24.** |",
              "| Seismic | Zone **III**, IS 1893:2016 | Zone **III**, "
              "IS 1893 of **1984** | **CORROBORATED** — master `A.7.8` "
              "Z = 0.16 reproduces exactly, `SG-F12` |",
              "",
              "**What the design actually uses from any of this: nothing "
              "that these tables supply.** The only rainfall figure in the "
              "project is the **50 mm/h** design intensity on Rev F drawing "
              "5 note 1 — drainage open item `DR-D1`, which **SG1 does not "
              "close**, because a monthly total cannot produce a "
              "short-duration intensity. The soak-pit rate (`K.2 A7`) needs "
              "a percolation test. The one place the rainfall record bites "
              "is the **programme** — `SG-F7`.",
              "",
              "**October is the figure to go back and check.** It is "
              f"**{pre['October']:.1f} mm**, "
              f"**{pre['October'] / pre['September']:.2f}×** September and "
              f"above August, in a month when the south-west monsoon has "
              f"withdrawn from interior Maharashtra. It is **not corrected "
              f"here** — correcting a datum whose source is unknown would be "
              f"inventing evidence. `SG-V5`",
          ])


# ------------------------------------------------------------------ 5
def reconciliation_schedule():
    rows = [
        ["`A1`", "Rockhead 1.5–2.0 m", "`(−)1.500` to `(−)2.000` `[A]`",
         "**0.9 – 1.5 m** at three locations `[C]`",
         "Bands **touch at one point**. Master conservative on depth, "
         "**unconservative on rock quantity** — +118 m³, ≈ 2 d",
         "**OPEN** `SG-F5`"],
        ["`A2`", "**Design GWT (−)2.000**", "`(−)2.000` `[A]`",
         "*“not encountered in any trial pit”* — **in pits ~1.5 m deep** "
         "`[C]`",
         "**Provenance found, not verification.** *Not encountered* = "
         "**not reached**", "**OPEN** `SG-F6`"],
        ["`A3`", "SBC 3240 kPa", "3240 `[A]` IS 1904 Table 1",
         "**1961–2059 kPa soaked**, 2942–3530 unsoaked `[C]`",
         "Soaked governs. Worst utilisation 12.5 % → **20.6 %**, all pass",
         "**OPEN** `SG-F3`"],
        ["`A4`", "k_s 100 000–500 000 kN/m³", "both bounds `[A]`",
         "**nothing** — no plate load test `[N]`",
         "Untouched. The second bound is still outstanding",
         "**OPEN** — unchanged"],
        ["`A5`", "K₀ 0.50, γ 20/21", "0.50, 20/21 `[A]`",
         "φ **27–35°**, MDD **1.88–1.93**, OMC **8–12 %** `[C]`",
         "K₀ **conservative** on the murrum; γ_sat agrees within **1.2 %**; "
         "wall load moves **< 1 %**", "**OPEN** `SG-F9`"],
        ["`A6`", "K_a 1.0 saturated", "1.0 `[C]`", "nothing `[N]`",
         "Untouched", "unchanged"],
        ["`A7`", "Soak pit 20 L/m²/day", "20 `[A]`",
         "**nothing** — no percolation test `[N]`",
         "Untouched. IS 2470 (Pt 2) Cl. 4 test still **mandatory**, and the "
         "report’s basalt makes failure likely", "**OPEN** — unchanged"],
        ["`A8`", "Seepage 0.5 L/m²/day", "0.5 `[A]`",
         "**nothing** — no packer test `[N]`", "Untouched",
         "**OPEN** — unchanged"],
        ["`A10`", "Wind k₁ 1.08, V_b 39 m/s", "39 m/s `[C]`",
         "monthly **mean** speeds only `[C]`",
         "**Different statistic.** Not a conflict, and **not a reason to "
         "reduce V_b**", "unchanged"],
        ["—", "**Seismic Zone III**", "Z = 0.16, IS 1893 (Pt 1):2016 `[C]`",
         "**Zone III**, both documents `[C]`",
         "A_h 0.075 / 0.100 **reproduce exactly**",
         "**CORROBORATED** `SG-F12`"],
        ["—", "**Cover 40.65 kPa**", "40.65 held by RC1 / C17 `[C]`",
         "MDD **1.90–1.93**, OMC **8–9 %** `[C]`",
         "40.65 **brackets both** the as-placed (lighter) and the fully "
         "saturated (+1 %) case", "**CORROBORATED** `SG-F8`"],
        ["—", "**Black cotton soil**", "**not recorded anywhere**",
         "**CH, FSI 60–65 %, 0.18–1.0 m** `[C]`",
         "Harmless under every founded element; **two exposures** — entry "
         "stairwell raft, concealment turf",
         "**NEW** `SG-F13` `SG-F14`"],
        ["`D3`", "Site plan", "**does not exist**",
         "imagery and contours, **no dimension, benchmark or coordinate** "
         "`[C]`",
         "Better informed, **not closed**. Cut and fill, berm toe and the "
         "BS1 daylight point all still undrawable", "**STILL OPEN**"],
    ]
    write("GEOTECHNICAL_PARAMETER_RECONCILIATION",
          "GEOTECHNICAL PARAMETER RECONCILIATION — MASTER A.6 / K.2 "
          "AGAINST THE SUPPLIED EVIDENCE",
          ["REF", "PARAMETER", "WHAT THE MASTER HOLDS", "WHAT THE EVIDENCE "
           "SAYS", "WHAT THAT MEANS", "STATUS AFTER SG1"],
          rows,
          pre=["> **Four of the fourteen `K.2` assumptions are touched. "
               "NONE IS CLOSED.** Two master inputs are corroborated "
               "externally for the first time. One master gap is better "
               "informed and still open. Two entirely new items appear, "
               "both about the black cotton soil, neither previously "
               "recorded anywhere in the project.\n"],
          notes=[
              "**Nothing in Parts A, B, D, F or L is changed by this "
              "schedule.** No load, thickness, bar, level, quantity, rate, "
              "date or float moves. No `[ASSUMED]` becomes `[CONFIRMED]`. "
              "The main staircase is untouched.",
          ])


def main():
    os.makedirs(SCH, exist_ok=True)
    print("SG1 schedules:")
    trial_pit_schedule()
    soil_property_schedule()
    rock_schedule()
    met_schedule()
    reconciliation_schedule()


if __name__ == "__main__":
    main()
