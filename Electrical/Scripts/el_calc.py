"""
el_calc.py  --  every electrical figure this package publishes, derived here.

Deliberately short.  Six sections: sources, loads, the generator check, the
battery, the fuel check, and what could not be done.

Run:  python3 el_calc.py
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import el_proj as P                                        # noqa: E402

OUT = []


def w(s=""):
    OUT.append(s)
    print(s)


def h1(n, t):
    w("")
    w("=" * 76)
    w(f"{n}  {t}")
    w("=" * 76)


# ------------------------------------------------------------- primitives
def fan_kw(q_m3h=None, dp_pa=None):
    q = (q_m3h or P.Q_FAN_M3H) / 3600.0
    dp = dp_pa if dp_pa is not None else P.DP_FAN_PA
    return q * dp / (P.ETA_FAN * P.ETA_MOTOR) / 1000.0


def pump_kw(q_ls, h_m):
    return (P.RHO_W * P.G * (q_ls / 1000.0) * h_m
            / (P.ETA_PUMP * P.ETA_MOTOR)) / 1000.0


def light_kw():
    return P.FLOOR_AREA_M2 * P.LIGHT_W_M2 / 1000.0


def load_kw(tag):
    """kW for a schedule row, computing the [R] ones."""
    return {"L-01": light_kw(),
            "F-01": fan_kw(),
            "U-01": pump_kw(P.Q_PU01_LS, P.H_PU01_M),
            "U-02": pump_kw(P.Q_PU04_LS, P.H_PU04_M)}.get(tag)


def rows():
    out = []
    for tag, desc, board, kw, cls, note in P.LOADS:
        out.append((tag, desc, board, kw if kw is not None else load_kw(tag),
                    cls, note))
    return out


def connected_kw():
    return sum(r[3] for r in rows())


def essential_kw():
    t = 0.0
    for tag, kw, note in P.ESSENTIAL:
        t += (pump_kw(P.Q_PU01_LS, P.H_PU01_M) * P.SUMP_DUTY_FRACTION
              if kw is None else kw)
    return t


def battery_ah(hours):
    wh = essential_kw() * 1000.0 * hours
    rated = wh / (P.DOD * P.ETA_INV)
    return rated / P.V_DC, rated / 1000.0        # Ah, kWh


# =========================================================================
def main():
    w("ELECTRICAL AND POWER - DESIGN CALCULATIONS")
    w("Underground CBRN-hardened blast-resistant protective structure - Pune")
    w(f"Package revision {P.REV}  ·  {P.PACKAGE_DATE}  ·  {P.GEOM_REV}")
    w(f"{P.STATUS}   ·   SENTRY POST EXCLUDED")
    w("")
    w("A BASIC PACKAGE, ON PURPOSE.  It stops at BOARD LEVEL.  No circuit")
    w("schedule, no cable sizing, no luminaire layout - see E.6 and EL-V5.")

    # ------------------------------------------------------------- E.1
    h1("E.1", "SOURCES - AND ONE THE MASTER NEVER RECORDED")
    w("")
    w("  GEN-1    15 kVA standby set, bay 8, the grey zone     [C] master A.3")
    w("  MAINS    via a METER PANEL                            [C] but only in")
    w("           the OWNER'S OWN PROGRAMME - activity 123, 'Electrical Wiring")
    w("           Works - Mains wire Pulling, Mater Panel Fixing etc. (DB to")
    w("           Meter Panel)', and activity 5 'Electricity Provision'.")
    w("           WM2 ruled that the owner's package GOVERNS, so an incoming")
    w("           mains supply IS part of this project - but it appears")
    w("           NOWHERE in the master, and its capacity, tariff and point of")
    w("           connection are [N].  EL-V4.")
    w("  BATTERY  DOES NOT EXIST ANYWHERE IN THE PROJECT.  [N]")
    w("           HVAC QA/QC P11 says so explicitly: 'distribution, UPS and")
    w("           battery autonomy are an ELECTRICAL scope item, not designed")
    w("           here'.  E.5 designs it.")
    w("")
    w("  AND TWO SOURCES THAT NEED NO ELECTRICITY AT ALL, BOTH CONFIRMED:")
    w("    - a HAND CRANK on both filter fans      [C] HVAC equipment schedule")
    w("    - hand pump PU-03                       [C] drainage schedule, S-06")
    w("  These are the real last line, the project already has them, and no")
    w("  electrical design should be allowed to obscure them.  [D]")

    # ------------------------------------------------------------- E.2
    h1("E.2", "LOAD SCHEDULE")
    w("")
    w(f"  Fan       P = Q.dp / (eta_fan . eta_motor)")
    w(f"            Q = {P.Q_FAN_M3H:.0f} m3/h [C],  dp = {P.DP_FAN_PA:.0f} Pa [A] DIRTY filter")
    w(f"            -> {fan_kw():.3f} kW")
    w(f"  Pump      P = rho.g.Q.H / (eta_pump . eta_motor)")
    w(f"            PU-01 {P.Q_PU01_LS} L/s [C] at {P.H_PU01_M:.0f} m [A] -> {pump_kw(P.Q_PU01_LS, P.H_PU01_M):.3f} kW")
    w(f"            PU-04 {P.Q_PU04_LS} L/s [C] at {P.H_PU04_M:.0f} m [A] -> {pump_kw(P.Q_PU04_LS, P.H_PU04_M):.3f} kW")
    w(f"  Lighting  {P.FLOOR_AREA_M2:.0f} m2 [C] x {P.LIGHT_W_M2:.0f} W/m2 [A] -> {light_kw():.3f} kW")
    w("")
    w(f"{'TAG':>6s} {'DESCRIPTION':38s} {'BOARD':>6s} {'kW':>7s}  CLASS")
    w("-" * 76)
    for tag, desc, board, kw, cls, note in rows():
        w(f"{tag:>6s} {desc[:38]:38s} {board:>6s} {kw:7.3f}  {cls}")
    w("-" * 76)
    tot = connected_kw()
    kva = tot / P.PF_SYSTEM
    w(f"{'':6s} {'CONNECTED LOAD':38s} {'':6s} {tot:7.3f}  kW")
    w(f"{'':6s} {'at power factor ' + str(P.PF_SYSTEM):38s} {'':6s} {kva:7.3f}  kVA")
    w("")
    w("  STANDBY UNITS ARE NOT COUNTED TWICE.  FAN-2, PU-02 and PU-05 are")
    w("  standby to FAN-1, PU-01 and PU-04 and never run simultaneously with")
    w("  them  [C].  The schedule carries the duty unit only.")

    # ------------------------------------------------------------- E.3
    h1("E.3", "IS THE 15 kVA GENERATOR THE RIGHT SIZE?  -  YES, COMFORTABLY")
    w("")
    w(f"  Connected load                      {tot:8.3f} kW")
    w(f"  at PF {P.PF_SYSTEM}                          {kva:8.3f} kVA")
    w(f"  GEN-1 rating                        {P.GEN_KVA:8.3f} kVA   [C] master A.3")
    w(f"  UTILISATION                          {kva/P.GEN_KVA*100:7.1f} %")
    w(f"  SPARE                               {P.GEN_KVA - kva:8.3f} kVA")
    w("")
    w(f"  Largest motor: the filter fan at {fan_kw():.3f} kW.  Even a direct-on-line")
    w(f"  start at 6x full-load current is about {fan_kw()*6/P.PF_SYSTEM:.1f} kVA - trivial against")
    w(f"  a {P.GEN_KVA:.0f} kVA set.  THERE IS NO STARTING PROBLEM.  [D]")
    w("")
    w(f"  ** THE CONFIRMED 15 kVA IS ABOUT TWICE THE CONNECTED DEMAND, and at")
    w(f"     {kva/P.GEN_KVA*100:.0f} % it sits in the healthy loading band for a diesel set - high")
    w("     enough to avoid wet-stacking, low enough to carry growth.  The")
    w("     project's own figure needs no change.  [D] **")

    # ------------------------------------------------------------- E.4
    h1("E.4", "THE QUESTION THAT DECIDES THE WHOLE PACKAGE")
    w("")
    w("  MAY THE GENERATOR RUN DURING MODE 3 CLOSED?")
    w("")
    w("  The project states BOTH of these, in the SAME confirmed schedule:")
    w("")
    w("    MODE 3  CLOSED            'ALL FIVE BLAST VALVES SHUT.  48 h limit'")
    w("    MODE 5  GENERATOR RUNNING 'BV-4 AND BV-5 OPEN ... bay 8 only - does")
    w("                               NOT touch the gas-tight envelope'")
    w("            and, in the note, 'Mode 5 is INDEPENDENT of modes 1-4'")
    w("")
    w("  BV-4 and BV-5 are two of the five.  Mode 3 shuts them; mode 5 needs")
    w("  them open.  The two statements cannot both hold during mode 3, and")
    w("  NOTHING IN THE PROJECT SAYS WHICH GIVES WAY.  [U]")
    w("")
    w("  Both readings are defensible:")
    w("    CASE A  the valves shut at the shock, hold 1.3 s [C], and BV-4/BV-5")
    w("            are REOPENED once it has passed.  Bay 8 is outside the")
    w("            gas-tight envelope, so the clean zone is untouched - which")
    w("            is exactly what the mode 5 note says.  The generator is")
    w("            available after a short outage.")
    w("    CASE B  mode 3 means SEALED, all five, for the full 48 h.  The")
    w("            generator cannot run at all and the battery carries")
    w("            everything.")
    w("")
    w("  E.5 sizes both.  THE ANSWER DIFFERS BY A FACTOR OF TWELVE.")

    # ------------------------------------------------------------- E.5
    h1("E.5", "THE ESSENTIAL SYSTEM AND THE BATTERY")
    w("")
    w("  Loads that stay live with NO generator and NO mains:")
    w("")
    for tag, kw, note in P.ESSENTIAL:
        v = (pump_kw(P.Q_PU01_LS, P.H_PU01_M) * P.SUMP_DUTY_FRACTION
             if kw is None else kw)
        w(f"    {tag:>7s} {v:6.3f} kW   {note}")
    ess = essential_kw()
    w(f"    {'TOTAL':>7s} {ess:6.3f} kW")
    w("")
    w("  GROUNDWATER DOES NOT STOP BECAUSE THE SHELTER IS SEALED.  The clean")
    w("  sump pump has to stay powered through mode 3, and the project's third")
    w("  line - hand pump PU-03 [C] - is what covers it if the battery fails.")
    w("")
    w(f"  Battery:  {P.V_DC:.0f} V DC, depth of discharge {P.DOD:.2f} [A],")
    w(f"            inverter efficiency {P.ETA_INV:.2f} [A]")
    w("")
    w(f"{'':>10s} {'HOURS':>7s} {'DELIVERED':>11s} {'RATED':>10s} {'CAPACITY':>11s} {'MASS':>9s} {'FLOOR':>8s}")
    w(f"{'':>10s} {'':>7s} {'kWh':>11s} {'kWh':>10s} {'Ah at 48 V':>11s} {'kg':>9s} {'m2 min':>8s}")
    w("-" * 76)
    for label, hrs in (("CASE A", P.CASE_A_H), ("CASE B", P.CASE_B_H)):
        ah, rated = battery_ah(hrs)
        mass = rated * 1000.0 / P.WH_PER_KG
        area = mass * P.G / 1000.0 / P.FLOOR_LL_KPA
        w(f"{label:>10s} {hrs:7.1f} {ess*hrs:11.2f} {rated:10.2f} {ah:11.1f} "
          f"{mass:9.0f} {area:8.2f}")
    w("-" * 76)
    ah_a, kwh_a = battery_ah(P.CASE_A_H)
    ah_b, kwh_b = battery_ah(P.CASE_B_H)
    w("")
    w(f"  ** CASE A IS A CABINET.  CASE B IS A ROOM. **   {ah_b/ah_a:.0f}x apart.  [D]")
    w("")
    w(f"  CASE A   {ah_a:.0f} Ah, about {kwh_a*1000/P.WH_PER_KG:.0f} kg - one small battery cabinet,")
    w(f"           anywhere convenient.")
    w(f"  CASE B   {ah_b:.0f} Ah, about {kwh_b*1000/P.WH_PER_KG/1000:.1f} TONNES of lead-acid needing at least")
    w(f"           {kwh_b*1000/P.WH_PER_KG*P.G/1000/P.FLOOR_LL_KPA:.1f} m2 of floor just to stay inside the {P.FLOOR_LL_KPA:.0f} kPa floor live")
    w("           load  [C] A.7.2 - and BAY 5 IS ALREADY 80 % OCCUPIED as drawn")
    w("           (MEP coordination CO-3).  THERE IS NOWHERE TO PUT IT.")
    w("")
    w(f"  ADOPTED FOR THIS PACKAGE: CASE A, {P.CASE_A_H:.0f} h, {ah_a:.0f} Ah at {P.V_DC:.0f} V.  [A]")
    w("  Chosen because it is the reading THE PROJECT'S OWN DOCUMENT implies -")
    w("  the mode schedule calls mode 5 'power OR BATTERY CHARGING' and says it")
    w("  is 'independent of modes 1-4', which only makes sense if the set can")
    w("  run while the clean zone is closed.")
    w("")
    w("  ** IF CASE B IS RIGHT, THIS BATTERY IS TWELVE TIMES TOO SMALL AND THE")
    w("     SHELTER HAS NO ROOM FOR THE RIGHT ONE.  That is EL-V1, and it is")
    w("     the single most consequential open question in this package. **")

    # ------------------------------------------------------------- E.6
    h1("E.6", "FUEL - THE OTHER WAY THE 96 h MISSION CAN FAIL")
    w("")
    energy = tot * P.MISSION_H
    litres = energy * P.SFC_L_PER_KWH
    w(f"  If the generator is the sole source for the full mission:")
    w(f"    connected load        {tot:8.3f} kW      [D] E.2")
    w(f"    mission              {P.MISSION_H:8.1f} h       [C] master A.1")
    w(f"    energy               {energy:8.1f} kWh")
    w(f"    at {P.SFC_L_PER_KWH:.2f} L/kWh [A]     {litres:8.0f} L of fuel")
    w("")
    w(f"  ORDER 200-250 L, AND NO FUEL STORE IS SPECIFIED ANYWHERE.  [N]")
    w("  The fire plan already carries this as FS-V4 ('generator fuel type,")
    w("  quantity and storage arrangement are unspecified, so the bay 8 fire")
    w("  load cannot be quantified') and the Works Management reconciliation")
    w("  as R-8.  THIS PACKAGE PUTS A NUMBER ON IT for the first time - it is")
    w("  a bounded estimate, not a specification, and the specific fuel")
    w("  consumption behind it is vendor data.  EL-V2.")

    # ------------------------------------------------------------- E.7
    h1("E.7", "WHAT THIS PACKAGE DID NOT DO")
    w("")
    for i, t in enumerate([
        "NO CIRCUIT SCHEDULE, NO CABLE SIZING, NO LUMINAIRE OR SOCKET "
        "LAYOUT.  It stops at board level on purpose.  EL-V5.",
        "NO EQUIPMENT SCHEDULE FOR EMP ZONE 2.  Z-01 is a 1.50 kW ALLOWANCE, "
        "which is a basis for EM-V2, not an answer to it.  EL-V3.",
        "NO PROTECTION OR DISCRIMINATION STUDY, no fault level, no earth-loop "
        "impedance - all need the incoming supply capacity, which is [N].",
        "NO CHANGE TO ANY BOQ QUANTITY, RATE, DATE OR FLOAT.  The owner's "
        "Works Management package governs and is untouched.",
        "NO COOLING LOAD, because NO COOLING PLANT EXISTS anywhere in the "
        "project.  Referred to HVAC, not resolved here.  EL-V6.",
        "NOTHING RESOLVED.  No existing [ASSUMED], [UNRESOLVED] or [NOT "
        "AVAILABLE] tag is converted, downgraded or deleted.",
    ], 1):
        w(f"  {i}  {t}")
        w("")

    w("=" * 76)
    w("END OF CALCULATIONS")
    w("=" * 76)

    p = os.path.join(_HERE, "..", "Calculations", "EL_CALC_OUTPUT.txt")
    with open(os.path.abspath(p), "w") as fh:
        fh.write("\n".join(OUT) + "\n")
    return os.path.abspath(p)


if __name__ == "__main__":
    print(f"\nwritten: {main()}")
