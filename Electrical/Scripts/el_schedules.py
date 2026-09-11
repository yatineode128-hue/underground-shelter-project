"""el_schedules.py  --  the two EL1 schedules, as Markdown and CSV."""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import el_proj as P                                        # noqa: E402
import el_calc as K                                        # noqa: E402

SCH = os.path.abspath(os.path.join(_HERE, "..", "Schedules"))

HEAD = (
    "**Underground CBRN-hardened protective structure — Pune** · "
    f"{P.GEOM_REV}\n"
    f"Electrical and Power package revision **{P.REV}** · {P.PACKAGE_DATE} · "
    f"**{P.STATUS}**\n"
    "**Sentry post excluded.** Evidence class: `[C]` confirmed · "
    "`[R]` reconstructed · `[D]` derived here · `[A]` assumed by this "
    "package · `[U]` unresolved · `[N]` not available — DATA REQUIRED\n\n"
    "> **A BASIC PACKAGE, ON PURPOSE.** It stops at **board level**. No "
    "circuit schedule, no cable sizing, no luminaire or socket layout — "
    "**EL-V5**.\n"
)


def write(name, title, header, rows, notes=(), pre=()):
    md = [f"# {title}", "", HEAD] + list(pre)
    md.append("| " + " | ".join(header) + " |")
    md.append("|" + "|".join("---" for _ in header) + "|")
    for r in rows:
        md.append("| " + " | ".join(str(c) for c in r) + " |")
    if notes:
        md.append("")
        md += list(notes)
    md.append("")
    open(os.path.join(SCH, name + ".md"), "w").write("\n".join(md))

    def esc(s):
        s = str(s).replace('"', '""').replace("**", "").replace("`", "")
        return f'"{s}"' if ("," in s or '"' in s) else s
    with open(os.path.join(SCH, name + ".csv"), "w") as fh:
        fh.write(",".join(esc(h) for h in header) + "\n")
        for r in rows:
            fh.write(",".join(esc(c) for c in r) + "\n")
    print(f"  {name}.md / .csv   {len(rows)} rows")


def load_schedule():
    rows = [[f"**{t}**", d, b, f"{kw:.3f}", f"`{c}`", n]
            for t, d, b, kw, c, n in K.rows()]
    tot = K.connected_kw()
    kva = tot / P.PF_SYSTEM
    write("LOAD_SCHEDULE", "ELECTRICAL LOAD SCHEDULE",
          ["TAG", "LOAD", "BOARD", "kW", "CLASS", "NOTES"], rows,
          pre=["**Standby units are not counted twice.** FAN-2, PU-02 and "
               "PU-05 are standby to FAN-1, PU-01 and PU-04 and never run "
               "simultaneously with them `[C]`. The schedule carries the "
               "**duty unit only**.\n"],
          notes=[
              f"| | |", "|---|---|",
              f"| **Connected load** | **{tot:.3f} kW** |",
              f"| at power factor {P.PF_SYSTEM} | **{kva:.3f} kVA** |",
              f"| **GEN-1 rating** `[C]` master A.3 | **{P.GEN_KVA:.1f} kVA** |",
              f"| **Utilisation** | **{kva/P.GEN_KVA*100:.1f} %** |",
              f"| Spare | {P.GEN_KVA - kva:.3f} kVA |",
              "",
              "### The 15 kVA is right, and needs no change `[D]`",
              "",
              f"It is **about twice the connected demand**, and **{kva/P.GEN_KVA*100:.0f} %** sits "
              "in the healthy loading band for a diesel set — high enough to "
              "avoid wet-stacking, low enough to carry growth. The largest "
              f"motor is the filter fan at **{K.fan_kw():.3f} kW**; even a "
              f"direct-on-line start is about **{K.fan_kw()*6/P.PF_SYSTEM:.1f} kVA**. "
              "**There is no starting problem.**",
              "",
              "**Derived figures.** Fan `P = Q·Δp/(η_fan·η_motor)` at "
              f"{P.Q_FAN_M3H:.0f} m³/h `[C]` and {P.DP_FAN_PA:.0f} Pa `[A]` "
              "*dirty* filter — HV1 records that only **161 Pa** of the loss "
              "build-up is derivable and five of eight components are vendor "
              "data `[N]`. Pumps `P = ρgQH/(η_pump·η_motor)` at the confirmed "
              "duties and assumed heads. Lighting "
              f"{P.FLOOR_AREA_M2:.0f} m² `[C]` × {P.LIGHT_W_M2:.0f} W/m² `[A]`.",
          ])


def distribution_schedule():
    rows = []
    for tag, name, bay, pos, note in P.BOARDS:
        fed = {"DB-M": "**MAINS** (meter panel) **+ GEN-1 15 kVA**, with changeover",
               "DB-E": "**DB-M**, and from the **battery inverter** on loss of both sources",
               "DB-Z2": "**DB-E through the PCI** on the EMP Zone 2 boundary"}[tag]
        rows.append([f"**{tag}**", name, f"Bay {bay}", pos, fed, note])
    ess = K.essential_kw()
    ah_a, kwh_a = K.battery_ah(P.CASE_A_H)
    ah_b, kwh_b = K.battery_ah(P.CASE_B_H)
    write("DISTRIBUTION_AND_ESSENTIAL_SCHEDULE",
          "DISTRIBUTION, ESSENTIAL SERVICES AND BATTERY SCHEDULE",
          ["BOARD", "NAME", "BAY", "POSITION", "FED FROM", "NOTES"], rows,
          pre=["**Three boards, and one cable entry.** Every conductor crossing "
               "the protective envelope uses the **service entry plate** — the "
               "project's single services penetration `[C]` — with a **PCI on "
               "power** and **fibre for signal**, as EM1 PoE-3 / PoE-4 require. "
               "**This package creates no new penetration.**\n"],
          notes=[
              "### Essential services — what stays live with no generator and no mains",
              "",
              "| Load | kW | |",
              "|---|---|---|",
          ] + [
              f"| `{t}` | {(K.pump_kw(P.Q_PU01_LS, P.H_PU01_M)*P.SUMP_DUTY_FRACTION if kw is None else kw):.3f} | {n} |"
              for t, kw, n in P.ESSENTIAL
          ] + [
              f"| **TOTAL** | **{ess:.3f}** | |",
              "",
              "**Groundwater does not stop because the shelter is sealed.** The "
              "clean sump pump stays powered through Mode 3, and the project's "
              "third line — **hand pump PU-03** `[C]` — is what covers it if "
              "the battery fails. Both filter fans also keep their **hand "
              "crank** `[C]`. **No electrical design should obscure those two.**",
              "",
              "### The battery — and the question that sizes it",
              "",
              f"{P.V_DC:.0f} V DC · depth of discharge {P.DOD:.2f} `[A]` · "
              f"inverter efficiency {P.ETA_INV:.2f} `[A]`",
              "",
              "| | Hours | Delivered kWh | Rated kWh | Ah at 48 V | Mass kg | Min floor m² |",
              "|---|---|---|---|---|---|---|",
              f"| **CASE A** — generator restartable after the shock | {P.CASE_A_H:.0f} | "
              f"{ess*P.CASE_A_H:.2f} | {kwh_a:.2f} | **{ah_a:.0f}** | {kwh_a*1000/P.WH_PER_KG:.0f} | "
              f"{kwh_a*1000/P.WH_PER_KG*P.G/1000/P.FLOOR_LL_KPA:.2f} |",
              f"| **CASE B** — no generator for the whole of Mode 3 | {P.CASE_B_H:.0f} | "
              f"{ess*P.CASE_B_H:.2f} | {kwh_b:.2f} | **{ah_b:.0f}** | {kwh_b*1000/P.WH_PER_KG:.0f} | "
              f"{kwh_b*1000/P.WH_PER_KG*P.G/1000/P.FLOOR_LL_KPA:.2f} |",
              "",
              f"> **Case A is a cabinet. Case B is a room.** They are "
              f"**{ah_b/ah_a:.0f}× apart**. Case B is **"
              f"{kwh_b*1000/P.WH_PER_KG/1000:.1f} tonnes** of lead-acid needing at least "
              f"**{kwh_b*1000/P.WH_PER_KG*P.G/1000/P.FLOOR_LL_KPA:.1f} m²** of floor merely to stay "
              f"inside the **{P.FLOOR_LL_KPA:.0f} kPa** floor live load `[C]` A.7.2 — "
              "and **Bay 5 is already 80 % occupied as drawn** (MEP "
              "coordination **CO-3**). **There is nowhere to put it.**",
              "",
              f"**Adopted: CASE A, {P.CASE_A_H:.0f} h, {ah_a:.0f} Ah at {P.V_DC:.0f} V** `[A]` — "
              "because it is the reading **the project's own document implies**: "
              "the mode schedule calls Mode 5 *\"power **or battery "
              "charging**\"* and says it is *\"independent of modes 1–4\"*, "
              "which only makes sense if the set can run while the clean zone "
              "is closed. **If Case B is right this battery is twelve times "
              "too small — EL-V1.**",
          ])


if __name__ == "__main__":
    print("EL1 schedules:")
    load_schedule()
    distribution_schedule()
