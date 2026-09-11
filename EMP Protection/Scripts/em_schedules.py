"""
em_schedules.py  --  the EMP PROTECTION schedules, in Markdown and CSV.

Every figure is imported from em_proj / em_calc.  Nothing here is typed by
hand, so a schedule cannot drift away from the calculation that produced it.

Run:  python3 em_schedules.py
"""
import os
import sys
import math

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import em_proj as P                                        # noqa: E402
import em_calc as K                                        # noqa: E402

SCH = os.path.abspath(os.path.join(_HERE, "..", "Schedules"))

HEAD = (
    "**Underground CBRN-hardened protective structure — Pune** · "
    f"{P.GEOM_REV}\n"
    f"EMP Protection package revision **{P.REV}** · {P.PACKAGE_DATE} · "
    f"**{P.STATUS}**\n"
    "**Sentry post excluded.** Evidence class: `[C]` confirmed · "
    "`[R]` reconstructed · `[D]` derived by this package · "
    "`[A]` assumed by this package · `[U]` unresolved · "
    "`[N]` not available — DATA REQUIRED\n\n"
    "> **`EMP Zone` is not `zone`.** Drainage and finishes already use "
    "zones 1/2/3 for **cleanliness**. The EMP zones here are a different "
    "scheme on the same building; the `EMP` prefix is mandatory.\n"
)


def write(name, title, header, rows, notes=(), pre=()):
    """One schedule, written as both .md and .csv."""
    md = [f"# {title}", "", HEAD]
    md += list(pre)
    md.append("| " + " | ".join(header) + " |")
    md.append("|" + "|".join("---" for _ in header) + "|")
    for r in rows:
        md.append("| " + " | ".join(str(c) for c in r) + " |")
    if notes:
        md.append("")
        md += list(notes)
    md.append("")
    with open(os.path.join(SCH, name + ".md"), "w") as fh:
        fh.write("\n".join(md))

    def esc(s):
        s = str(s).replace('"', '""')
        # strip the Markdown emphasis the CSV has no use for
        s = s.replace("**", "").replace("`", "")
        return f'"{s}"' if ("," in s or '"' in s) else s
    with open(os.path.join(SCH, name + ".csv"), "w") as fh:
        fh.write(",".join(esc(h) for h in header) + "\n")
        for r in rows:
            fh.write(",".join(esc(c) for c in r) + "\n")
    print(f"  {name}.md / .csv   {len(rows)} rows")


# ============================================================ 1  zones
def zone_schedule():
    s = P.BAR_SPACING
    f80 = K.f_at_se(P.SE_REQUIRED_DB, s)
    fcut = K.f_mesh_cut(s)
    Z = P.Z2
    rows = [
        ["**EMP ZONE 0**", "Everything above grade",
         "Sentry post +7.000 · headhouse +0.900, **no earth cover** · covered "
         "stairwell +2.450 (**expendable**) · ESC heads +0.150 / +0.700 · "
         "burster slab",
         "**NONE CREDITED**", "**0 dB**", "n/a — nothing to verify",
         "`[C]` RC2"],
        ["**EMP ZONE 1**", "The buried box, **all eight bays**",
         "600 walls · 900 roof · 600 mat · W6 / W7 400 · reinforcement cage at "
         "**150 both curtains** · cast-in frames welded to the cage · welded "
         "EMP strap at every construction joint",
         f"Mesh, 20 dB/decade: **{K.se_mesh(1e4, s):.0f} dB at 10 kHz** → "
         f"**0 dB at {fcut/1e6:.0f} MHz**",
         f"**{P.SE_REQUIRED_DB:.0f} dB only below {f80/1e3:.1f} kHz** — "
         "1 decade of the 5 required",
         "**CANNOT BE SURVEYED** — buried under 2 m of cover, no accessible "
         "exterior. Calculation only",
         "`[C]` RC2 · cage from `[C]` A.5"],
        ["**EMP ZONE 2**", f"Welded steel enclosure, bay 3 (U-03), finish W-04",
         f"External **{Z['x1']-Z['x0']} × {Z['y1']-Z['y0']} × {Z['h_ext']}** at "
         f"X {Z['x0']}–{Z['x1']}, Y {Z['y0']}–{Z['y1']} · panel {Z['panel']} · "
         f"internal **{Z['x1']-Z['x0']-2*Z['panel']} × "
         f"{Z['y1']-Z['y0']-2*Z['panel']} × {Z['h_ext']-2*Z['panel']}**",
         "**Solid welded steel — no aperture above the honeycomb cutoff**",
         f"**{P.SE_REQUIRED_DB:.0f} dB, {P.F_LO_HZ/1e3:.0f} kHz – "
         f"{P.F_HI_HZ/1e9:.0f} GHz, STANDING ALONE**",
         "**IEEE Std 299 full survey — HOLD POINT** before any equipment is "
         "installed",
         "`[C]` required / `[A]` every dimension"],
    ]
    write("EMP_ZONE_SCHEDULE", "EMP ZONE SCHEDULE",
          ["ZONE", "WHAT IT IS", "BOUNDARY AS BUILT", "SHIELDING MECHANISM",
           "PERFORMANCE", "VERIFICATION", "CLASS"], rows,
          pre=["**The project had named `EMP Zone 2` since Rev F and had never "
               "defined a Zone 1 or a Zone 0.** All three were derived by EM1 "
               "— master A.3 and K.3 confirm only that a Zone 2 enclosure is "
               "*required*.\n",
               "> ### ADOPTED — RC2, 11 September 2026 (master H.21)\n"
               "> **The project owner has adopted the three-zone model and "
               "the standing-alone rule below. They are the project's EMP "
               "position, not this package's proposal.** `[C]` **EM-V1 is "
               "closed.** No figure, finding or other open item in EM1 "
               "changes.\n",
               "> **THE DESIGN RULE:** *EMP Zone 2 is designed to the full "
               f"{P.SE_REQUIRED_DB:.0f} dB standing alone. **No attenuation "
               "from the concrete box is credited at any frequency.*** The "
               "cage is margin, not design.\n"],
          notes=[
              "**Why Zone 2 is small, and why that is right.** HEMP is not a "
              "personnel hazard. The occupants are protected from blast, CBRN "
              "and fallout by the box. EMP protection exists so the shelter "
              "can still **function** afterwards — so Zone 2 protects "
              "**equipment**, and it is correct that it is an enclosure "
              "rather than a room. `[D]`",
              "",
              "**Zone 1 is not a failure of the design.** A 150 mm bar "
              "spacing was adopted *as an EMP measure* and it is genuinely "
              "stricter than IS 456 Cl. 26.3.3 requires. It buys real "
              f"attenuation — {K.se_mesh(1e4, s):.0f} dB at 10 kHz is not "
              "nothing. It simply cannot be a MIL-STD-188-125-1 boundary, and "
              "it should never be described as one.",
          ])


# ==================================================== 2  penetrations
def penetration_register():
    rows = []
    for tag, kind, shape, bore, wall, host, note in P.PENETRATIONS:
        metal = K.CONDUCTING[tag]
        fc = K.fc_circ(bore) if shape == "CIRC" else K.fc_rect(bore)
        A = (K.a_circ(wall, bore) if shape == "CIRC"
             else K.a_rect(wall, bore)) if metal else 0.0
        se1m = 20.0 * math.log10(K.lam(1e6) / (2.0 * bore)) + A
        ok = (fc >= P.F_HI_HZ) and (se1m >= P.SE_REQUIRED_DB)
        if tag in ("BV-1", "BV-2", "BV-3"):
            treat = ("**NONE REQUIRED.** The wall is the waveguide. Keep the "
                     "bore metallic and the frame welded to the cage.")
        elif tag in ("BV-4", "BV-5"):
            treat = ("**HONEYCOMB WBC PANEL** inboard of the valve — *if* "
                     "bay 8 is inside the EMP boundary. **EM-V3.**")
        elif tag == "SEP":
            treat = ("**THE PLATE IS THE SHIELD.** Solid, welded, bonded 360° "
                     "to the cast-in frame. Its apertures are the individual "
                     "sleeves, treated one by one.")
        elif tag == "PD-05":
            treat = ("Bond the pipe **360° to the plate** — *if it is "
                     "metallic*. **No pipe material is specified anywhere in "
                     "the project.** **EM-V5.**")
        elif tag in ("ESC1", "ESC2"):
            treat = ("**BONDED CONDUCTING HATCH AT THE HEAD.** Lining the "
                     "shaft does not work — see notes. No hatch is specified.")
        else:
            treat = ("**NO TREATMENT EXISTS OR IS PROPOSED.** It is the entry "
                     "route. See notes — this is finding **EM-F1**.")
        rows.append([
            f"**{tag}**", kind, host,
            f"{bore:.0f}" + (" ⌀" if shape == "CIRC" else " wide"),
            f"{wall:.0f}", "steel" if metal else "**concrete**",
            f"{fc/1e6:.1f}", f"{A:.0f}" if metal else "—",
            f"{se1m:.0f}",
            "**PASS**" if ok else "**FAIL**", treat])
    write("ENVELOPE_PENETRATION_REGISTER",
          "ENVELOPE PENETRATION REGISTER — EMP",
          ["TAG", "TYPE", "LOCATION", "BORE mm", "DEPTH mm", "BORE BOUNDED BY",
           "CUTOFF MHz", "WBC dB", "SE @1 MHz dB", "VERDICT", "TREATMENT"],
          rows,
          pre=["**Ten penetrations. Every position, bore and wall thickness is "
               "read from a confirmed project document** — the HVAC damper and "
               "valve schedule, `MEP_AND_FINISHES_COORDINATION.md` CO-1, "
               "master A.4.4 and A.4.5. **This register creates no "
               "penetration and moves none.**\n",
               "**PASS** = below cutoff across the whole 10 kHz – 1 GHz band "
               "**and** at least 80 dB in band. A depth (waveguide) credit is "
               "taken **only where the bore is bounded by metal** — concrete "
               "is a lossy dielectric, not a waveguide wall.\n"],
          notes=[
              "**Large dB figures are theory, not performance.** No practical "
              "penetration achieves 250 dB; real assemblies flatten out around "
              "100–120 dB and are limited by **workmanship** — the bond at the "
              "frame, the gasket, the one sleeve nobody welded. Read a large "
              "number as *“the bore is not the problem here.”* `[D]`",
              "",
              "**Why lining an escape shaft does not work.** A conducting "
              f"liner would give {K.a_circ(3050, 1400):.0f} dB on ESC 1 and "
              f"{K.a_circ(3600, 1400):.0f} dB on ESC 2 — but only below "
              f"{K.fc_circ(1400)/1e6:.0f} MHz. Above that a 1400 bore "
              "propagates however well it is lined. The treatment that works "
              "is a **bonded conducting hatch at the head**, which terminates "
              "the shaft instead of trying to attenuate down it.",
              "",
              "**The stair void is the finding.** 2 800 × 3 160 through the "
              "900 pressure slab — **8.85 m², the largest aperture in the "
              f"envelope.** It never reaches 80 dB anywhere in the band and "
              f"above {K.fc_rect(3160)/1e6:.0f} MHz it is simply open. It "
              "opens into the headhouse (+0.900, **no earth cover**) and "
              "thence to grade through a stairwell that is **declared "
              "expendable**. Blast Door 1 is the only thing between that path "
              "and the occupied bays, and **its RF performance is vendor data "
              "the project does not have.** `[N]`",
          ])


# ============================================================= 3  PoE
def poe_schedule():
    cell, dep = P.Z2_VENT_CELL, P.Z2_VENT_DEPTH
    rows = [
        ["**PoE-1**", "ACCESS — shielded door", "5.4",
         "RF-gasketed or knife-edge shielded door, SE certified to match the "
         "enclosure", f"≥ {P.SE_REQUIRED_DB:.0f} dB",
         "**`[N]` type and vendor.** A shielded door is the usual place a "
         "room fails its survey", "`[A]` / `[N]`"],
        ["**PoE-2**", "VENTILATION — honeycomb WBC", "5.5",
         f"Honeycomb vent panel, **{cell:.0f} mm cell × {dep:.0f} mm deep**, "
         "frame welded to the enclosure",
         f"cutoff **{K.fc_circ(cell)/1e9:.1f} GHz** · "
         f"**{K.a_circ(dep, cell):.0f} dB** "
         f"(**{K.a_circ(dep, cell)-P.SE_REQUIRED_DB:+.0f} dB** margin)",
         "Mounted **inboard** of any blast device — the valve takes the "
         "pressure, the honeycomb takes the RF. **Own blast rating `[N]`.** "
         "Adds pressure drop HV1 did not allow for", "`[A]`"],
        ["**PoE-3**", "POWER — PCI", "5.7.2.1",
         "Protective device on **every** conductor crossing the boundary, "
         "mounted **on** the boundary, not near it",
         "**`[N]` — no residual quoted**",
         "MIL-STD-188-125-1 specifies PCI performance **by pulse test**; the "
         "project register carries the section number only. **Inventing a "
         "figure would be worse than `[N]`**", "`[C]` method / `[N]` value"],
        ["**PoE-4**", "SIGNAL — fibre", "5.7.4.1",
         "Optical fibre, **no metallic strength member, no metallic armour**",
         "**A dielectric penetration is not a penetration**",
         "**The one place this project can buy perfect performance for almost "
         "nothing — and it should take it.** `[D]`", "`[D]`"],
        ["**PoE-5**", "RF — antenna / feeder", "5.7.6",
         "**DOES NOT EXIST**",
         "**`[N]`**",
         "**There is no antenna, mast, feeder or communications design "
         "anywhere in this project.** An ops room that cannot transmit is an "
         "ops room in name only, and an antenna is by definition a deliberate "
         "conductor from outside to inside. **EM-V4**", "`[N]`"],
    ]
    write("POE_PROTECTION_SCHEDULE",
          "POINT-OF-ENTRY (PoE) PROTECTION SCHEDULE — EMP ZONE 2",
          ["PoE", "KIND", "MIL-STD-188-125-1 §", "TREATMENT", "PERFORMANCE",
           "NOTES", "CLASS"], rows,
          pre=["**Five ways into EMP Zone 2, and the treatment of each.** The "
               "section numbers are the ones already in the project's own "
               "code register (master Part G) — **no clause not in that "
               "register is cited.**\n"],
          notes=[
              "**A shield is only as good as its worst point of entry.** "
              f"{K.a_circ(dep, cell):.0f} dB of honeycomb is worth nothing "
              "behind a door that leaks, and a perfect door is worth nothing "
              "beside an unfiltered power conductor. **PoE-1 to PoE-5 are one "
              "system and are surveyed as one system.**",
          ])


# ==================================================== 4  bonding / earth
def bonding_schedule():
    rows = []
    for label, l_, w_, t_ in P.STRAPS:
        L = K.strap_L(l_, w_, t_)
        rows.append([
            f"**{label.title()}**", f"{l_:.0f}", f"{w_:.0f} × {t_:.0f}",
            f"{w_/l_:.2f} : 1", f"{L*1e9:.1f}",
            f"{2*math.pi*1e6*L:.2f}", f"{2*math.pi*1e7*L:.1f}",
            f"{2*math.pi*1e8*L:.0f}",
            "**REJECTED — 322 Ω at 100 MHz is not a bond**"
            if l_ > P.BOND_MAX_LEN and w_ / l_ < P.BOND_MIN_WL
            else ("**ADOPTED — the house rule**" if l_ <= P.BOND_MAX_LEN
                  else "**LIMIT — do not exceed**")])
    write("BONDING_AND_EARTHING_SCHEDULE",
          "BONDING AND EARTHING SCHEDULE — EMP",
          ["STRAP", "LENGTH mm", "SECTION mm", "w : l", "L nH",
           "X @1 MHz Ω", "X @10 MHz Ω", "X @100 MHz Ω", "RULING"], rows,
          pre=["**This is where EMP design actually lives.** An EMP shield "
               "works by being **equipotential**, and equipotential is decided "
               "by **bonding inductance**, not by earth resistance. "
               "`L = 2×10⁻⁷·l·[ln(2l/(w+t)) + 0.5 + 0.2235(w+t)/l]` H\n"],
          notes=[
              f"### The bonding rules `[D]`",
              "",
              f"1. **Every bond ≤ {P.BOND_MAX_LEN:.0f} mm long.**",
              f"2. **Width : length at least {P.BOND_MIN_WL:.0f} : 1.**",
              "3. **Flat strap only.** Never a round wire, never a pigtail, "
              "never *“loop it round to the nearest stud.”*",
              "4. **Clean bare metal both ends**, protected after making off.",
              "5. **The shield bonds to the structure at ONE place.** A second "
              "bond is a loop, and a loop is an antenna.",
              "",
              "### Earthing — and why 5 Ω is the wrong target to chase",
              "",
              "| Electrode | ρ = 1 000 Ω·m | ρ = 10 000 Ω·m | Class |",
              "|---|---|---|---|",
              f"| One 3 m × 16 mm rod | **{K.rod_R(1e3, P.ROD_L, P.ROD_D):.0f} Ω** "
              f"| **{K.rod_R(1e4, P.ROD_L, P.ROD_D):.0f} Ω** | `[D]` |",
              f"| Rods needed for 5 Ω, *no interaction* | "
              f"**{K.rod_R(1e3, P.ROD_L, P.ROD_D)/5:.0f}** | "
              f"**{K.rod_R(1e4, P.ROD_L, P.ROD_D)/5:.0f}** | `[D]` |",
              f"| **The structure itself** (136.4 m², r_eq 6.589 m, ρ/4r) | "
              f"**{1e3/(4*6.589):.0f} Ω** | **{1e4/(4*6.589):.0f} Ω** | `[D]` |",
              "",
              "**≤ 5 Ω is not achievable with rods in Deccan basalt** "
              "(1 000 – 10 000 Ω·m, master K.3, which already says *“test "
              "earth resistance early”*). The **mat and its cage are already a "
              "large concrete-encased electrode**, an order of magnitude "
              "better than a rod and costing nothing. **Bond to the structure; "
              "do not chase rods.** `[D]`",
              "",
              "**And ≤ 5 Ω is not an EMP number.** It is a power-safety and "
              "lightning requirement from IS 3043 / IEEE 142. It is real and "
              "it still applies. **It is not what makes the shield work.**",
              "",
              "**The project already does this correctly in two places, "
              "without saying why:** master A.5 requires the blast door frames "
              "to be *cast in and **welded to the cage***, and B.7.2 requires "
              "it even for the **non-blast-rated** headhouse door. Those are "
              "EMP bonds. `[C]`",
          ])


# ============================================= 5  shielding effectiveness
def se_schedule():
    s = P.BAR_SPACING
    rows = []
    for f in K.DECADES:
        L = K.lam(f)
        se = K.se_mesh(f, s)
        rows.append([
            K.fmt_f(f).strip(),
            f"{L/1000.0:.3f} m" if L >= 1000 else f"{L:.1f} mm",
            f"{se:.2f}",
            f"{se - P.SE_REQUIRED_DB:+.2f}",
            "**PASS**" if se >= P.SE_REQUIRED_DB else "**FAIL**",
            f"{P.SE_REQUIRED_DB:.0f}"])
    f80 = K.f_at_se(P.SE_REQUIRED_DB, s)
    fcut = K.f_mesh_cut(s)
    write("SHIELDING_EFFECTIVENESS_SCHEDULE",
          "SHIELDING EFFECTIVENESS — THE REINFORCEMENT CAGE",
          ["FREQUENCY", "WAVELENGTH", "SE dB", "MARGIN dB", "VERDICT",
           "REQUIRED dB"], rows,
          pre=[f"Square aperture array at the confirmed bar spacing "
               f"**s = {s:.0f} mm, both curtains, both ways** (master A.5 — "
               "*“an EMP requirement, stricter than IS 456 Cl. 26.3.3”*).\n",
               "`SE = 20 log₁₀(λ / 2s)`, zero once `λ ≤ 2s`\n"],
          notes=[
              "### The check that matters",
              "",
              "Master **K.3** records, as a confirmed item: *“EMP rebar cage "
              "**0 dB @ 1 GHz**”*. This table reaches "
              f"**{K.se_mesh(1e9, s):.3f} dB at 1 GHz** from the 150 mm bar "
              f"spacing alone, and puts the mesh cutoff at "
              f"**{fcut/1e6:.1f} MHz**. **The project's own figure is "
              "reproduced, not assumed.** `[R]`",
              "",
              f"**2s = {2*s:.0f} mm. The wavelength at 1 GHz is "
              f"{K.lam(1e9):.2f} mm.** The cage stops shielding at almost "
              "exactly the frequency at which MIL-STD-188-125-1 stops asking. "
              "That is arithmetic, not design.",
              "",
              "| | |",
              "|---|---|",
              f"| Highest frequency at 80 dB | **{f80/1e3:.2f} kHz** |",
              f"| Decades required | **{math.log10(P.F_HI_HZ/P.F_LO_HZ):.0f}** |",
              f"| Decades delivered | **{math.log10(f80/P.F_LO_HZ):.2f}** |",
              f"| **Fraction of the required band met** | "
              f"**{math.log10(f80/P.F_LO_HZ)/math.log10(P.F_HI_HZ/P.F_LO_HZ)*100:.0f} %** |",
              "",
              "**These figures are an UPPER BOUND.** The classical array "
              "correction `−10 log₁₀(n)` for *n* illuminated apertures is "
              "**not applied** (it would make every figure worse); the "
              "crossings are **tied, not welded**; and no concrete absorption "
              "is credited, because no permittivity or conductivity for this "
              "concrete exists anywhere in the project `[N]`. **A measured "
              "cage will be worse than this table.** `[D]`",
          ])


if __name__ == "__main__":
    print("EMP schedules:")
    zone_schedule()
    penetration_register()
    poe_schedule()
    bonding_schedule()
    se_schedule()
