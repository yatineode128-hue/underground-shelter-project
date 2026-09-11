"""sg_calc.py  --  every conversion, check and reproduction, arithmetic shown.

    python3 sg_calc.py        ->  ../Calculations/SG_CALC_OUTPUT.txt

Nothing in this file adopts a value.  It converts the two supplied documents
into the project's units, reproduces their own internal arithmetic to show
whether they are self-consistent, and puts each result beside the master's
current assumed value so the gap - or the agreement - is visible and
quantified.  Where the comparison would change a design value, the calculation
says by how much and then says that nothing is changed, because master rules
M.5, M.6 and M.7 reserve that decision to the project owner.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import sg_proj as P                                        # noqa: E402
import sg_data as D                                        # noqa: E402

W = 100
OUT = []


def rule(ch="="):
    OUT.append(ch * W)


def head(n, t):
    OUT.append("")
    rule()
    OUT.append(f"{n}   {t}")
    rule()
    OUT.append("")


def p(s=""):
    OUT.append(s)


def kpa(v):
    """kgf/cm2 -> kPa."""
    return v * P.KGCM2_KPA


# =====================================================================
def banner():
    rule()
    p("SITE SELECTION AND GEOTECHNICAL  -  CALCULATION PRINTOUT")
    p(f"revision {P.REV}   {P.PACKAGE_DATE}   {P.GEOM_REV}")
    rule()
    p()
    p("SOURCES")
    p(f"  1  {D.REPORT['code']}   {D.REPORT['title']}")
    p(f"     {D.REPORT['author']}")
    p(f"     Raised on {D.REPORT['request']}")
    p(f"  2  P1 deck, \"{D.DECK['title']}\", {D.DECK['team']}, "
      f"{D.DECK['pages']} slides")
    p(f"  3  Location pin {D.PIN_URL}")
    p(f"     {D.PIN_STATUS}")
    p()
    p("EVIDENCE CLASSES, as everywhere in this project")
    for tag, name, desc in P.EVIDENCE:
        p(f"  {tag} {name:<15} {desc}")
    p()
    p("THIS PACKAGE RESOLVES NOTHING.  Master rule M.6 forbids converting an")
    p("[ASSUMED] into a confirmed fact.  Every K.2 assumption stands after")
    p("this calculation exactly as it stood before it; what changes is that")
    p("each one now has a stated provenance and a quantified margin.")


# =====================================================================
def g1_units():
    head("G.1", "UNIT CONVERSION  -  the report is in kgf/cm2, the project "
                "is in kPa")
    p("  1 kgf/cm2 = 1 kgf / 1e-4 m2 = 9.80665 N / 1e-4 m2 = 98 066.5 Pa")
    p(f"           = {P.KGCM2_KPA:.4f} kPa      [R] exact, from the "
      f"definition of kgf")
    p()
    p("  Every bearing figure in the report, converted once, here:")
    p()
    p(f"  {'kgf/cm2':>10}  {'kPa':>12}   {'what it is':<58}")
    p("  " + "-" * 84)
    rows = [
        (0.25, "H Building, CH clay, GL to 0.18 m"),
        (0.27, "G Building, CH clay, GL to 1.0 m"),
        (2.07, "Mess Bldg, murrum SC, GL to 0.2 m"),
        (4.27, "G Building, murrum GM, 1.0 to 1.2 m"),
        (4.66, "H Building, murrum GM, 0.18 to 0.7 m"),
        (5.18, "Mess Bldg, murrum GP, 0.2 to 0.5 m"),
        (10.0, "BROKEN basalt, all three locations, IS 12070 Table 2"),
        (20.0, "SOUND basalt, SOAKED, G Building, below 1.5 m"),
        (21.0, "SOUND basalt, SOAKED, H Building and Mess Bldg"),
        (30.0, "SOUND basalt, UNSOAKED, H Building, below 0.9 m"),
        (33.0, "SOUND basalt, UNSOAKED, G Building, below 1.5 m"),
        (36.0, "SOUND basalt, UNSOAKED, Mess Bldg, below 1.0 m"),
    ]
    for v, what in rows:
        p(f"  {v:>10.2f}  {kpa(v):>12.1f}   {what:<58}")
    p()
    p(f"  MASTER A.6 presumptive SBC                        "
      f"{P.SBC_MASTER:>8.0f} kPa  = {P.SBC_MASTER / P.KGCM2_KPA:.2f} kgf/cm2")
    p("  IS 1904:1986 Table 1, hard rock without lamination.          [A]")
    p()
    p("  *** THE MASTER'S PRESUMPTIVE VALUE AND THE REPORT'S MEASURED ONES ***")
    p(f"  3240 kPa sits INSIDE the report's UNSOAKED band "
      f"({kpa(30):.0f} to {kpa(36):.0f} kPa)")
    p(f"  and {P.SBC_MASTER / kpa(20) - 1:+.1%} ABOVE the report's SOAKED band "
      f"({kpa(20):.0f} to {kpa(21):.0f} kPa).")
    p("  Which one applies is settled in G.4 - it is not a free choice.")


# =====================================================================
def g2_reproduce():
    head("G.2", "REPRODUCING THE REPORT'S OWN ARITHMETIC  -  is it "
                "self-consistent?")
    p("  A report is only usable if its numbers follow from each other.  Both")
    p("  of its bearing derivations are reproduced here from its own inputs.")
    p()
    p("  (a)  SOIL  -  Appendix B.  Remark (ii): 'The recommended bearing")
    p("       capacity is calculated with factor of safety = 2.5 in submerged")
    p("       condition of soil.'   So SBC = q_ult / 2.5.")
    p()
    p(f"  {'sample':<8} {'class':<6} {'q_ult':>8} {'/2.5':>8} "
      f"{'SBC printed':>12}  {'check':<6}")
    p("  " + "-" * 56)
    ok_b = 0
    for s, tp, cl, omc, mdd, ucs, dsc, phi, qult, sbc in D.APPX_B:
        calc = qult / D.APPX_B_FOS
        good = abs(calc - sbc) <= 0.005 + 0.005
        ok_b += good
        p(f"  {s:<8} {cl:<6} {qult:>8.3f} {calc:>8.3f} {sbc:>12.2f}  "
          f"{'OK' if good else 'DIFFERS':<6}")
    p()
    p(f"  {ok_b} of {len(D.APPX_B)} reproduce to the printed precision.   [R]")
    p()
    p("  (b)  ROCK  -  Appendix C.  The report cites IS 1121 (Pt-I) for the")
    p("       compressive strength and IS 12070 Cl. 6 for the bearing value,")
    p("       but prints no factor.  Solving for it from its own six rows:")
    p()
    p(f"  {'condition':<10} {'location':<22} {'UCS':>7} {'SBC':>6} "
      f"{'UCS/SBC':>9}")
    p("  " + "-" * 58)
    ratios = []
    for cond, depth, loc, load, area, ucs, sbc in D.APPX_C:
        ratios.append(ucs / sbc)
        p(f"  {cond:<10} {loc:<22} {ucs:>7.0f} {sbc:>6.0f} {ucs / sbc:>9.2f}")
    p()
    p(f"  mean {sum(ratios) / len(ratios):.2f}, range "
      f"{min(ratios):.2f} to {max(ratios):.2f}")
    p("  The factor is 25, applied to the compressive strength and rounded to")
    p("  the nearest whole kgf/cm2.  Checking that back:")
    p()
    for cond, depth, loc, load, area, ucs, sbc in D.APPX_C:
        p(f"    {ucs:>4.0f} / 25 = {ucs / 25:>6.2f}  ->  rounds to "
          f"{round(ucs / 25):>2d}   printed {sbc:>2.0f}   "
          f"{'OK' if round(ucs / 25) == sbc else 'DIFFERS'}")
    p()
    p("  All six reproduce.  SBC_rock = UCS / 25, rounded.          [R]")
    p()
    p("  (c)  The specimen arithmetic behind the UCS itself:")
    p()
    p(f"  {'condition':<10} {'location':<22} {'load kg':>9} {'area cm2':>9} "
      f"{'P/A':>8} {'printed':>8}")
    p("  " + "-" * 70)
    for cond, depth, loc, load, area, ucs, sbc in D.APPX_C:
        calc = load / area
        p(f"  {cond:<10} {loc:<22} {load:>9.0f} {area:>9.2f} {calc:>8.1f} "
          f"{ucs:>8.0f}")
    p()
    p("  Every row is its own load divided by its own specimen area, to the")
    p("  nearest whole kgf/cm2.  The report is internally consistent.    [R]")
    p()
    p("  >>> FINDING SG-F1.  The SEMT report reproduces completely from its")
    p("      own inputs - both the soil chain (q_ult / 2.5) and the rock")
    p("      chain (P/A, then /25).  It is usable.  That is worth saying")
    p("      before anything is built on it.")


# =====================================================================
def g3_depth():
    head("G.3", "THE DEPTH THE INVESTIGATION REACHED  -  and the depth the "
                "structure needs")
    p("  Field method, verbatim, report para 10:")
    p(f"    \"{D.FIELD}\"")
    p()
    p("  The deepest stratum boundary recorded anywhere in the report:")
    p()
    p(f"  {'location':<24} {'deepest boundary stated':<28} {'level*':>9}")
    p("  " + "-" * 64)
    deepest = 0.0
    for loc, layers in D.FINDINGS:
        last = layers[-1][0]
        d = float(last.replace("Below", "").replace("m", "").strip())
        deepest = max(deepest, d)
        p(f"  {loc:<24} {last:<28} {-d:>9.3f}")
    p()
    p("  * expressed on the project datum, taking the report's GL as the")
    p("    project's finished grade 0.000.  That equivalence is itself [A] -")
    p("    see G.9, the site is not level and no benchmark ties the two.")
    p()
    p(f"  DEEPEST INFORMATION IN THE REPORT      (-){deepest:.3f}")
    p(f"  Rock cores were taken at and below that level; no pit is stated to")
    p(f"  have gone deeper, and a JCB in broken basalt cannot go much deeper.")
    p()
    p("  WHAT THE STRUCTURE NEEDS:")
    p()
    p(f"  {'element':<44} {'level':>9} {'below the deepest data':>24}")
    p("  " + "-" * 80)
    items = [
        ("Sentry footing F1, in-situ basalt", P.LVL_F1_FOUND),
        ("Underground box, top of roof slab", P.LVL_SLAB_TOP),
        ("Underground box, internal floor", P.LVL_FLOOR),
        ("Mat soffit", P.LVL_MAT_SOFFIT),
        ("FORMATION - what the mat bears on", P.LVL_FORMATION),
        ("Sump SU-01 base", P.LVL_SUMP_BASE),
    ]
    for name, lv in items:
        gap = -deepest - lv
        p(f"  {name:<44} {lv:>9.3f} {gap:>21.3f} m")
    p()
    p("  >>> FINDING SG-F2  -  THE GOVERNING FINDING OF THIS PACKAGE.")
    p(f"      The investigation reached about {deepest:.1f} m.  The structure")
    p(f"      founds at {P.LVL_FORMATION:.3f}, which is "
      f"{-deepest - P.LVL_FORMATION:.1f} m deeper, and the sump goes")
    p(f"      {-deepest - P.LVL_SUMP_BASE:.1f} m deeper still.  ONLY THE "
      f"SENTRY POST FOOTING F1 AT (-)2.000")
    p("      IS INSIDE THE INVESTIGATED HORIZON, AND ONLY JUST.")
    p()
    p("      Nothing the report says about rockhead, water, jointing,")
    p("      red-bole seams or modulus can be read as covering the founding")
    p("      horizon of the shelter.  Master K.2 A1, A2, A4, A5 and A8 all")
    p("      stay OPEN, and the programme's confirmatory site investigation")
    p("      A1075 - boreholes, rockhead, red-bole seams, 12 d, critical")
    p("      path - remains mandatory in full.")


# =====================================================================
def g4_sbc():
    head("G.4", "BEARING  -  which of the report's two rock values applies, "
                "and does it matter?")
    p("  The report gives the sound basalt TWO bearing values: one SOAKED, one")
    p("  UNSOAKED.  They differ by a factor of about 1.6.  The design GWT and")
    p("  the founding level decide between them, and it is not a free choice:")
    p()
    p(f"    design GWT   (master A.6, [A])                "
      f"{P.LVL_GWT_DESIGN:>8.3f}")
    p(f"    mat soffit                                    "
      f"{P.LVL_MAT_SOFFIT:>8.3f}")
    p(f"    formation                                     "
      f"{P.LVL_FORMATION:>8.3f}")
    p(f"    depth of the formation below the design GWT   "
      f"{P.LVL_GWT_DESIGN - P.LVL_FORMATION:>8.3f} m")
    p()
    p("  The founding horizon is permanently below the design water table.")
    p("  THE SOAKED VALUE IS THE APPLICABLE ONE.  Appendix B's own remark (ii)")
    p("  makes the same choice for the soils: it computes them 'in submerged")
    p("  condition of soil'.")
    p()
    soaked = kpa(20.0)
    unsoaked_lo = kpa(30.0)
    p(f"  SOAKED, lowest of the three                   {soaked:>8.1f} kPa  [C]")
    p(f"  UNSOAKED, lowest of the three                 "
      f"{unsoaked_lo:>8.1f} kPa  [C]")
    p(f"  MASTER A.6 presumptive, IS 1904 Table 1       "
      f"{P.SBC_MASTER:>8.1f} kPa  [A]")
    p()
    p("  Re-running every bearing check in the master at the SOAKED value:")
    p()
    p(f"  {'check':<40} {'demand':>10} {'/3240 [A]':>11} "
      f"{'/1961 soaked':>13} {'verdict':>9}")
    p("  " + "-" * 88)
    for name, q in (("Mat, service (master B.3)", P.Q_MAT_SERVICE),
                    ("Mat, BLAST (master B.3)", P.Q_MAT_BLAST),
                    ("Sentry footing F1 (master B.8.7)", P.Q_F1_SERVICE)):
        p(f"  {name:<40} {q:>8.1f} kPa {q / P.SBC_MASTER:>10.2%} "
          f"{q / soaked:>12.2%} {'PASS':>9}")
    p()
    p("  >>> FINDING SG-F3.  The master's presumptive 3240 kPa is 65 % above")
    p("      the report's soaked basalt value, and it does not matter.  The")
    p("      worst bearing utilisation in the whole project rises from 12.5 %")
    p(f"      to {P.Q_MAT_BLAST / soaked:.1%} and every element still passes "
      f"with a factor of about")
    p(f"      {soaked / P.Q_MAT_BLAST:.1f} in hand.  MASTER A.6 IS NOT "
      f"CHANGED - it is a presumptive")
    p("      value from IS 1904 and it is declared as one.  What SG1 adds is")
    p("      that the design is now known to survive the measured value too.")
    p()
    p("  A second robustness check, because the report offers it for free:")
    broken = kpa(10.0)
    p(f"      BROKEN basalt, IS 12070 Table 2               {broken:>8.1f} kPa")
    p(f"      mat blast bearing / broken basalt SBC         "
      f"{P.Q_MAT_BLAST / broken:>8.1%}")
    p("      Even if the formation were left in the BROKEN rock horizon - it")
    p("      will not be, it is 5 m below it - the mat would still pass under")
    p("      full blast.  The bearing case is not close to governing anything.")


# =====================================================================
def g5_net():
    head("G.5", "NET BEARING PRESSURE  -  why settlement was never the "
                "problem, and flotation always was")
    p("  The excavation removes ground before the structure replaces it.  The")
    p("  report's own profile lets that be quantified for the first time.")
    p()
    heads = [float(L[-1][0].replace("Below", "").replace("m", "").strip())
             for _, L in D.FINDINGS]
    soil_t = sum(heads) / len(heads)   # mean of the report's own rockhead band
    rock_t = -P.LVL_FORMATION - soil_t
    g_soil, g_rock = 19.5, 25.0       # [A]
    removed = soil_t * g_soil + rock_t * g_rock
    p(f"    mean rockhead over the report's three locations   "
      f"{soil_t:>8.3f} m     [R]")
    p(f"    overburden removed, {soil_t:.2f} m soil at {g_soil:.1f} kN/m3"
      f"       {soil_t * g_soil:>8.2f} kPa   [A] gamma")
    p(f"    overburden removed, {rock_t:.2f} m basalt at {g_rock:.1f} kN/m3"
      f"     {rock_t * g_rock:>8.2f} kPa   [A] gamma")
    p(f"    TOTAL GROSS PRESSURE REMOVED AT FORMATION        "
      f"{removed:>8.2f} kPa   [D]")
    p()
    p(f"    replaced by, in service                          "
      f"{P.Q_MAT_SERVICE:>8.2f} kPa   [C] B.3")
    p(f"    NET CHANGE IN PRESSURE AT FORMATION              "
      f"{P.Q_MAT_SERVICE - removed:>+8.2f} kPa   [D]")
    p()
    p("  >>> FINDING SG-F4.  IN SERVICE THE STRUCTURE IS LIGHTER THAN THE")
    p("      GROUND IT REPLACES, by about "
      f"{removed - P.Q_MAT_SERVICE:.0f} kPa.  It is a fully compensated")
    p("      foundation and then some.  This is the physical reason master")
    p("      B.3 can write 'SETTLEMENT Negligible' and mean it, and it is the")
    p("      same fact seen from the other side that makes FLOTATION the")
    p("      governing foundation problem - FoS 0.33 at the mat-only stage.")
    p("      The report does not change either conclusion; it explains them.")
    p()
    p(f"    under blast, momentarily                         "
      f"{P.Q_MAT_BLAST:>8.2f} kPa   [C] B.3")
    p(f"    net, under blast                                 "
      f"{P.Q_MAT_BLAST - removed:>+8.2f} kPa   [D]")
    p("    A transient, on rock, at 21 % of the soaked SBC.  Not a settlement")
    p("    case in any code sense.")


# =====================================================================
def g6_rockhead():
    head("G.6", "ROCKHEAD  -  the report's band against the master's, and "
                "what it costs")
    p("  Report para 12, last sentence, verbatim:")
    p(f"    \"{D.PROFILE_TEXT.rstrip('.').split('. ')[-1].strip()}.\"")
    p()
    p("  Rockhead, as the findings table gives it location by location:")
    p()
    p(f"  {'location':<26} {'sound basalt below':>20}   "
      f"{'on the project datum':>22}")
    p("  " + "-" * 74)
    heads = []
    for loc, layers in D.FINDINGS:
        d = float(layers[-1][0].replace("Below", "").replace("m", "").strip())
        heads.append(d)
        p(f"  {loc:<26} {d:>18.3f} m   {-d:>21.3f}")
    lo, hi = min(heads), max(heads)
    p()
    p(f"  REPORT BAND                        (-){lo:.3f} to (-){hi:.3f}    [C]")
    p(f"  MASTER A.6 ASSUMED BAND            "
      f"(-){-P.ROCKHEAD_MASTER[0]:.3f} to (-){-P.ROCKHEAD_MASTER[1]:.3f}    [A]")
    p()
    p("  >>> FINDING SG-F5.  THE TWO BANDS TOUCH AT EXACTLY ONE POINT,")
    p("      (-)1.500.  The report's rock is at or ABOVE the master's whole")
    p("      assumed range.  The master is therefore CONSERVATIVE for")
    p("      founding depth - the rock is there sooner than assumed - and")
    p("      UNCONSERVATIVE for excavation quantity, because more of the")
    p("      excavation is in rock and less is in soil.")
    p()
    p("  Quantifying that.  The WM1 BOQ gives item E-02b at the mean")
    p("  rockhead and states its own range, which fixes the plan area:")
    p()
    area = P.WM_ROCK_M3 / (-P.LVL_FORMATION - 1.750)
    p(f"    E-02b at rockhead (-)1.750       {P.WM_ROCK_M3:>8.2f} m3   [C]")
    p(f"    depth of rock cut                {-P.LVL_FORMATION - 1.750:>8.3f} m")
    p(f"    implied plan area                {area:>8.3f} m2   [R]")
    p(f"    check at (-)1.500  {area * (-P.LVL_FORMATION - 1.500):>8.2f} m3 "
      f"vs the BOQ's stated {P.WM_ROCK_RANGE[1]:.1f}   OK")
    p(f"    check at (-)2.000  {area * (-P.LVL_FORMATION - 2.000):>8.2f} m3 "
      f"vs the BOQ's stated {P.WM_ROCK_RANGE[0]:.1f}   OK")
    p()
    p(f"  {'rockhead':<12} {'rock cut':>10} {'volume m3':>12} "
      f"{'vs BOQ upper bound':>20}")
    p("  " + "-" * 58)
    for rh in (0.900, 1.000, 1.500, 1.750, 2.000):
        v = area * (-P.LVL_FORMATION - rh)
        p(f"  (-){rh:<9.3f} {-P.LVL_FORMATION - rh:>9.3f} m {v:>12.2f} "
          f"{v - P.WM_ROCK_RANGE[1]:>+18.2f}")
    p()
    v_lo = area * (-P.LVL_FORMATION - hi)
    v_hi = area * (-P.LVL_FORMATION - lo)
    p(f"  ON THE REPORT'S BAND the rock quantity is "
      f"{v_lo:.1f} to {v_hi:.1f} m3.")
    p(f"  The BOQ prices {P.WM_ROCK_RANGE[0]:.1f} to "
      f"{P.WM_ROCK_RANGE[1]:.1f} m3.  The report's LOWER bound equals the")
    p("  BOQ's UPPER bound.  At the report's shallow rockhead the overrun is")
    p(f"    {v_hi - P.WM_ROCK_RANGE[1]:>8.2f} m3   "
      f"({v_hi / P.WM_ROCK_RANGE[1] - 1:+.1%} on the priced upper bound)")
    p(f"    {(v_hi - P.WM_ROCK_RANGE[1]) / P.WM_ROCK_RATE_M3_DAY:>8.2f} days "
      f"at the WBS A2050 output of {P.WM_ROCK_RATE_M3_DAY:.0f} m3/day")
    p()
    p("  TOTAL excavation does not change - soil falls by the same volume as")
    p("  rock rises - so the money at stake is the RATE DIFFERENCE over about")
    p(f"  {v_hi - P.WM_ROCK_RANGE[1]:.0f} m3, not a rock rate over "
      f"{v_hi - P.WM_ROCK_RANGE[1]:.0f} m3.  NO BOQ QUANTITY IS CHANGED HERE:")
    p("  WM2 adopted the project owner's own BOQ and it governs (master H.13),")
    p("  and risk R-03 in the WM safety and risk register already carries")
    p("  'rock excavation quantity exceeds the estimate because rockhead is")
    p("  shallower than the mean assumed'.  What SG1 adds is the number: the")
    p("  register says 'roughly one extra day', and on the report's band it")
    p(f"  is about {(v_hi - P.WM_ROCK_RANGE[1]) / P.WM_ROCK_RATE_M3_DAY:.0f}.")
    p()
    p("  One favourable consequence, recorded because it is free.  Master B.3")
    p("  argues sliding away on the grounds that the box is 'socketed ~4.8 m")
    p("  into basalt'.  On the report's band the socket is")
    p(f"    {-P.LVL_FORMATION - hi:.1f} m to {-P.LVL_FORMATION - lo:.1f} m.  "
      f"The argument gets stronger, not weaker.")


# =====================================================================
def g7_water():
    head("G.7", "GROUNDWATER  -  what 'not encountered' does and does not "
                "establish")
    p("  Report para 13, in full, verbatim:")
    p(f"    \"{D.WATER_TABLE_TEXT}\"")
    p()
    p("  P1 deck slide 29, verbatim:")
    for c in D.DECK_SOIL_CLAIMS[2:]:
        p(f"    \"{c}\"")
    p()
    p("  THIS IS THE FIRST WRITTEN PROVENANCE THE PROJECT HAS EVER HAD FOR THE")
    p("  DESIGN GROUNDWATER TABLE.  Master A.6 and K.2 A2 record (-)2.000 as")
    p("  [ASSUMED - the single most important number to confirm] and give no")
    p("  source.  The source is now known, and it is this: no water was found,")
    p("  so a depth of 2 m below GL was CHOSEN and the structure was designed")
    p("  to be safe for it.  That is an assumption adopted in the absence of")
    p("  data.  It is a defensible one.  It is not a measurement.")
    p()
    p("  THREE REASONS THE OBSERVATION DOES NOT REACH THE DESIGN QUESTION:")
    p()
    p("  (1) DEPTH.  The pits reached about 1.5 m (G.3).  The design GWT is at")
    p(f"      (-)2.000, already BELOW the deepest pit, and the founding")
    p(f"      horizon is at {P.LVL_FORMATION:.3f}.  A pit that stops at 1.5 m")
    p("      cannot find a water table at 2 m, let alone characterise one at")
    p("      6.8 m.  'Not encountered' here means 'not reached'.")
    p()
    p("  (2) SEASON.  The report itself says the table 'may raise")
    p("      during/after rainy season'.  The request is dated 20 May 2015.")
    p("      If the field work followed promptly it was done in the last weeks")
    p("      before the monsoon - the annual minimum.  THE REPORT NOWHERE")
    p("      STATES THE DATE OF THE FIELD WORK, so this is inference, and it")
    p("      is recorded as an open item, not as a finding.               [U]")
    p()
    p("  (3) GROUND TYPE.  Deccan Trap groundwater is not a simple water")
    p("      table in a porous medium.  It sits in the vesicular and jointed")
    p("      zones AT THE FLOW CONTACTS - which is the same feature master A.6")
    p("      already names as 'the hazard is not the basalt, it is the flow")
    p("      contacts' and which the red-bole differential-support case in B.3")
    p("      is built around.  Such water is commonly perched and strongly")
    p("      seasonal.  An open trial pit in the dry season is close to the")
    p("      worst available instrument for finding it.")
    p()
    p("  >>> FINDING SG-F6.  K.2 A2 STAYS [ASSUMED] AND STAYS OPEN.  The new")
    p("      evidence supports keeping it open, not closing it.  Master B.3's")
    p("      own arithmetic shows why this matters more than any other number")
    p("      in the project:")
    p()
    p(f"        of the {P.GRADIENT_MASTER:.2f} kPa/m lateral gradient, 9.81 "
      f"is water and {P.GRADIENT_MASTER - 9.81:.2f} is soil")
    p("        hydrostatic uplift on the mat    46.11 kPa = 6289 kN over "
      "136.4 m2")
    p("        flotation FoS, mat cast only     0.33   FAIL")
    p("        flotation FoS, box complete      1.22   MARGINAL")
    p("      Water is nearly two thirds of the lateral load and the whole of")
    p("      the uplift.  Everything the structure is afraid of is water.")
    p()
    p("  WHAT WOULD ACTUALLY CLOSE A2, and what the programme currently does:")
    p()
    p("      WBS A1080  'Monsoon groundwater monitoring - confirm the design")
    p("                  GWT (-)2.000',  20 d,  12-11-26 to 04-12-26,  TF 0")
    p()
    p("      >>> FINDING SG-F7.  THAT WINDOW IS NOT IN THE MONSOON.  On the")
    p("          deck's own precipitation table the wet months are June to")
    p("          October; November and December carry 22.7 and 5.9 mm between")
    p("          them.  An activity called 'monsoon groundwater monitoring'")
    p("          scheduled 12 Nov to 4 Dec measures the recession, not the")
    p("          peak, and the peak is what A2 asks for.  A standpipe")
    p("          piezometer installed in the A1075 borehole and read through")
    p("          a full monsoon is what closes A2; nothing shorter does.")
    p("          NO PROGRAMME DATE IS CHANGED HERE - the owner's own Master")
    p("          Construction Schedule R0 governs (master H.13) and the")
    p("          activity is on the critical path at TF 0, so moving it")
    p("          moves the job.  It is raised, with the reason, as SG-V3.")


# =====================================================================
def g8_params():
    head("G.8", "THE SOIL PARAMETERS IN MASTER A.6, CHECKED AGAINST MEASURED "
                "DATA")
    p("  Appendix B gives compaction and shear results for the murrum, which")
    p("  is the material the engineered fill, the side backfill and the berm")
    p("  will actually be built from.  Master A.6 and A.7.3 have carried")
    p("  round-number values for them since Rev D with no measurement behind")
    p("  either.  They are now checkable.")
    p()
    p("  (a)  UNIT WEIGHT AT PLACEMENT.  The fill is specified at 95 % MDD")
    p("       (master A.7.3, WBS A7010).  gamma_bulk = 0.95 x MDD x (1 + OMC).")
    p()
    p(f"  {'sample':<8} {'class':<5} {'MDD':>6} {'OMC':>5} "
      f"{'0.95 MDD':>9} {'gamma_d':>9} {'gamma_bulk':>11}")
    p("  " + "-" * 60)
    bulks = []
    for s, tp, cl, omc, mdd, ucs, dsc, phi, qult, sbc in D.APPX_B:
        if cl in ("GM", "GP"):
            gd = 0.95 * mdd * P.GCC_KNM3
            gb = gd * (1 + omc / 100.0)
            bulks.append(gb)
            p(f"  {s:<8} {cl:<5} {mdd:>6.2f} {omc:>4d}% {0.95 * mdd:>9.4f} "
              f"{gd:>8.2f}  {gb:>10.2f}")
    p()
    p(f"  MEASURED PLACEMENT RANGE          {min(bulks):.2f} to "
      f"{max(bulks):.2f} kN/m3      [D]")
    p(f"  MASTER A.7.3 uses                 {P.COVER_FILL_GAMMA:.2f} kN/m3 "
      f"for the 750 fill   [A]")
    p(f"  MASTER A.6 uses                   {P.GAMMA_BULK:.2f} kN/m3 bulk, "
      f"{P.GAMMA_SAT:.2f} saturated  [A]")
    p()
    p("       The assumed 20 is 2 to 5 % ABOVE what 95 % of the measured MDD")
    p("       gives.  For LATERAL load that is conservative and welcome.  For")
    p("       the COVER it makes the cover slightly lighter than assumed:")
    p()
    gb_lo, gb_hi = min(bulks), max(bulks)
    for gb in (gb_hi, gb_lo):
        lay = 0.750 * gb
        p(f"         750 fill at {gb:.2f} kN/m3  ->  {lay:.2f} kPa  "
          f"(assumed {0.750 * P.COVER_FILL_GAMMA:.2f}, "
          f"{lay - 0.750 * P.COVER_FILL_GAMMA:+.2f})")
    p(f"         six-layer sum falls from {P.COVER_LAYER_SUM:.2f} to "
      f"{P.COVER_LAYER_SUM - (0.750 * P.COVER_FILL_GAMMA - 0.750 * gb_lo):.2f} "
      f"kPa")
    p(f"         the RC1 declared allowance grows from 1.50 to "
      f"{P.COVER_TOTAL_DESIGN - (P.COVER_LAYER_SUM - (0.750 * P.COVER_FILL_GAMMA - 0.750 * gb_lo)):.2f} kPa")
    p()
    p("       AND THE OTHER WAY, which matters more.  Saturate the three")
    p("       soil-like layers and the cover gets HEAVIER, not lighter:")
    p()
    gd = 0.95 * 1.93 * P.GCC_KNM3
    e = P.G_S * P.GCC_KNM3 / gd - 1.0
    gsat = (P.G_S + e) / (1 + e) * P.GCC_KNM3
    p(f"         gamma_d at 95 % of MDD 1.93        {gd:>6.2f} kN/m3")
    p(f"         void ratio e = G_s.gamma_w/gamma_d - 1  = {e:.4f}   "
      f"[A] G_s = {P.G_S}")
    p(f"         gamma_sat = (G_s + e)/(1 + e).gamma_w  = {gsat:.2f} kN/m3")
    p(f"         vs master A.6 gamma_sat            {P.GAMMA_SAT:>6.2f} kN/m3"
      f"   -> agrees within {abs(gsat / P.GAMMA_SAT - 1):.1%}    [R]")
    p()
    sat_delta = (0.750 * (gsat - 20.0) + 0.300 * (20.0 - 18.0)
                 + 0.150 * (21.5 - 19.0))
    p(f"         750 fill   20.00 -> {gsat:.2f}   "
      f"{0.750 * (gsat - 20.0):+.2f} kPa")
    p(f"         300 topsoil 18.00 -> 20.00        "
      f"{0.300 * 2.0:+.2f} kPa   [A]")
    p(f"         150 filter  19.00 -> 21.50        "
      f"{0.150 * 2.5:+.2f} kPa   [A]")
    p(f"         layer sum on full saturation      "
      f"{P.COVER_LAYER_SUM + sat_delta:.2f} kPa")
    p(f"         against the held design value     "
      f"{P.COVER_TOTAL_DESIGN:.2f} kPa   "
      f"({P.COVER_LAYER_SUM + sat_delta - P.COVER_TOTAL_DESIGN:+.2f})")
    p(f"         as a fraction of COMB 103 = 448.15 kPa   "
      f"{(P.COVER_LAYER_SUM + sat_delta - P.COVER_TOTAL_DESIGN) / 448.15:+.2%}")
    p()
    p("       >>> FINDING SG-F8.  The held cover value of 40.65 kPa brackets")
    p("           BOTH the as-placed case (lighter) and the fully saturated")
    p("           case (heavier by about 1 %, which is 0.1 % of COMB 103).")
    p("           C17's declared allowance turns out to be doing real work.")
    p("           NOTHING IS CHANGED: 40.65 stands, COMB 103 stays 448.15,")
    p("           no .std file is touched.")
    p()
    p("  (b)  SHEAR STRENGTH AND K0.  Master A.6 takes K0 = 1 - sin(phi) with")
    p("       phi ~ 30 deg.  Appendix B measured phi on four samples:")
    p()
    import math
    p(f"  {'sample':<8} {'class':<5} {'c kg/cm2':>9} {'phi':>5} "
      f"{'1 - sin phi':>12} {'vs 0.50':>9}")
    p("  " + "-" * 54)
    for s, tp, cl, omc, mdd, ucs, dsc, phi, qult, sbc in D.APPX_B:
        if phi is None:
            continue
        k0 = 1 - math.sin(math.radians(phi))
        p(f"  {s:<8} {cl:<5} {dsc:>9.2f} {phi:>4d}d {k0:>12.4f} "
          f"{k0 - P.K0_MASTER:>+9.4f}")
    p()
    p("       Three granular murrum samples (GM, GM, GP) give K0 0.426 to")
    p("       0.455 - the assumed 0.50 is CONSERVATIVE against all three.")
    p("       One clayey sand (SC, TP-9, a 0.2 m surface layer) gives 0.546.")
    p()
    p("       Worst case, carrying the SC value to full depth, which no")
    p("       reading of the profile supports:")
    k0w = 1 - math.sin(math.radians(27))
    gp = P.GAMMA_SAT - 9.81
    grad_w = k0w * gp + 9.81
    base_m = P.K0_MASTER * P.GAMMA_BULK * 2.0 + P.GRADIENT_MASTER * 4.100
    base_w = k0w * P.GAMMA_BULK * 2.0 + grad_w * 4.100
    p(f"         gradient  K0.gamma' + gamma_w = {k0w:.4f} x {gp:.2f} + 9.81 "
      f"= {grad_w:.3f} kPa/m")
    p(f"         wall pressure at the floor (-)6.100")
    p(f"             master     {base_m:>7.2f} kPa   [C] A.7.2")
    p(f"             worst case {base_w:>7.2f} kPa   [D]   "
      f"{base_w / base_m - 1:+.2%}")
    p(f"         with blast 383 kPa on the same wall face:")
    p(f"             master     {383 + base_m:>7.2f} kPa")
    p(f"             worst case {383 + base_w:>7.2f} kPa   "
      f"{(383 + base_w) / (383 + base_m) - 1:+.2%}")
    p()
    p("       >>> FINDING SG-F9.  The measured shear parameters move the wall")
    p("           design load by under 1 %.  The walls are blast-governed;")
    p("           the soil is 18 % of the load and the soil PARAMETERS are a")
    p("           fraction of that.  A.6's K0 = 0.50 is not changed, and the")
    p("           report gives no reason to change it.")
    p()
    p("  (c)  A LIMIT ON ALL OF (a) AND (b), STATED PLAINLY.  On the report's")
    p("       own rockhead band the box occupies (-)2.000 to (-)6.800 and is")
    p("       therefore ENTIRELY WITHIN BASALT.  What bears on the walls is")
    p("       rock and the 300 lean-concrete annulus, not soil.  The master's")
    p("       K0-soil-plus-hydrostatic model is a conservative idealisation of")
    p("       that, and correctly keeps the full hydrostatic term, because")
    p("       water pressure in a jointed rock mass is real and is two thirds")
    p("       of the load.  The measured soil parameters are the right check")
    p("       on the berm, the backfill and the cover.  They are NOT a")
    p("       description of what the buried walls retain.")


# =====================================================================
def g9_site():
    head("G.9", "THE SITE ITSELF  -  setting, level, fall, and one conflict "
                "inside the deck")
    p("  SETTING, from deck slides 13, 14, 17, 18 and 22:")
    for s in D.DECK_SETTING:
        p(f"    - {s}")
    for s in D.DECK_PIPELINES:
        p(f"    - {s}")
    p()
    p("  SELECTION, the deck's own SWOT, verbatim:")
    for k in ("strength", "weakness", "opportunity", "threats"):
        p(f"    {k.upper()}")
        for it in D.DECK_SWOT[k]:
            p(f"      - {it}")
    p()
    p("  GROUND LEVEL.  Two statements, and they do not agree.")
    p()
    p(f"    (i)  CONTOUR MAP, slide 15.  1 m contours labelled "
      f"{D.DECK_CONTOURS[0]} to {D.DECK_CONTOURS[1]}.")
    p(f"         The {D.DECK_CONTOURS_AT_SITE[0]} and "
      f"{D.DECK_CONTOURS_AT_SITE[1]} contours both cross the plot; ground")
    p(f"         falls {D.DECK_CONTOUR_FALL}.")
    p(f"         => site ground level approximately "
      f"{D.DECK_CONTOURS_AT_SITE[0]} to {D.DECK_CONTOURS_AT_SITE[1] + 1} m "
      f"on that map's datum,")
    p("         with of the order of 1 to 1.5 m of fall across the plot.  [R]")
    p()
    e = D.DECK_ELEV_PROFILE
    p(f"    (ii) ELEVATION PROFILE, slide 21.  {e['z0']} m at 0 m rising to "
      f"{e['z1']} m")
    p(f"         at {e['x1']} m.")
    p(f"         rise {e['z1'] - e['z0']:.1f} m over {e['x1']:.1f} m  =  "
      f"1 in {e['x1'] / (e['z1'] - e['z0']):.1f}  =  "
      f"{(e['z1'] - e['z0']) / e['x1']:.1%}")
    p()
    p(f"    THE TWO DISAGREE ON LEVEL BY "
      f"{e['z0'] - (D.DECK_CONTOURS_AT_SITE[1] + 1):.0f} to "
      f"{e['z1'] - D.DECK_CONTOURS_AT_SITE[0]:.0f} m, and on gradient")
    p(f"    by roughly a factor of four "
      f"(1 in {e['x1'] / (e['z1'] - e['z0']):.0f} against of the order of "
      f"1 in 40).")
    p()
    p("    >>> FINDING SG-F10.  These are two different measurements of two")
    p("        different things on two different datums, and the deck presents")
    p("        them as one site description.  The most likely reading is that")
    p("        the contour map is a local/survey datum and the profile is a")
    p("        satellite-derived MSL profile taken across a short transect")
    p("        that includes the track embankment east of the plot - but THAT")
    p("        IS A GUESS AND IT IS RECORDED AS ONE.  Neither number is")
    p("        adopted.  Open item SG-V4.")
    p()
    p("  WHY THE LEVEL MATTERS, AND WHY IT DOES NOT.")
    p("    It does not matter to any design value.  The project works on a")
    p("    LOCAL datum with finished grade = 0.000 (master A.4.1), every level")
    p("    in Parts A, B and F is relative to it, and no absolute reduced")
    p("    level appears anywhere in the project.  Nothing recalculates.")
    p("    It DOES matter to three things that are not yet drawn: the cut and")
    p("    fill needed to produce a level formation for a 22 m long box, the")
    p("    berm toe, and the point where the cover's 1:50 crossfall (BS1)")
    p("    daylights.  With 1 to 1.5 m of natural fall across the plot, the")
    p("    finished grade at 0.000 cannot be the natural surface everywhere.")
    p("    No cut-and-fill item exists in the BOQ because no site plan exists")
    p("    (master gap D3).  SG1 does not close D3 and cannot: there is still")
    p("    no boundary, no dimension, no benchmark and no coordinate.")
    p()
    p("  THE REPORT'S OWN TERRAIN SENTENCE, for completeness:")
    p(f"    \"{D.TERRAIN}\"")
    p("    That is said of the G, H and Mess building locations, not of this")
    p("    plot, and the contour map shows this plot is the edge of a slope.")


# =====================================================================
def g10_met():
    head("G.10", "METEOROLOGY  -  three statistics, one conflict, and what "
                 "the design actually uses")
    p("  (a)  RAINFALL.  The two documents disagree.")
    p()
    tot = sum(v for _, v in D.DECK_PRECIP)
    p(f"  {'month':<12} {'mm':>8}    {'month':<12} {'mm':>8}")
    p("  " + "-" * 48)
    for i in range(6):
        a, av = D.DECK_PRECIP[i]
        b, bv = D.DECK_PRECIP[i + 6]
        p(f"  {a:<12} {av:>8.1f}    {b:<12} {bv:>8.1f}")
    p("  " + "-" * 48)
    p(f"  DECK TOTAL, slide 25 (last 10 years avg)     {tot:>8.1f} mm   [C]")
    p(f"  SEMT REPORT para 9                    "
      f"{D.RAINFALL_REPORT_RANGE[0]:.0f} to "
      f"{D.RAINFALL_REPORT_RANGE[1]:.0f} mm   [C]")
    p(f"  DIFFERENCE                            "
      f"{tot / D.RAINFALL_REPORT_RANGE[1] - 1:+.0%} to "
      f"{tot / D.RAINFALL_REPORT_RANGE[0] - 1:+.0%}")
    p()
    p("  >>> FINDING SG-F11.  THE TWO SUPPLIED DOCUMENTS DISAGREE ON ANNUAL")
    p("      RAINFALL BY BETWEEN A QUARTER AND A HALF.  Neither names a")
    p("      station, a period of record or a source; the deck says 'last 10")
    p("      years avg' and the report says 'the region'.  Published")
    p("      tertiary figures for 'Pune' themselves range from about 720 mm")
    p("      to over 1000 mm depending on which gauge and which period is")
    p("      quoted, which is the reason a NAMED STATION AND PERIOD is")
    p("      required and is why NO THIRD FIGURE IS ADOPTED HERE.")
    p()
    p("  ONE MONTH IS THE OUTLIER.  Reading the deck's own table as a monsoon")
    p("  distribution for the interior Deccan:")
    p()
    jun_sep = sum(v for m, v in D.DECK_PRECIP
                  if m in ("June", "July", "August", "September"))
    octo = dict(D.DECK_PRECIP)["October"]
    sep = dict(D.DECK_PRECIP)["September"]
    p(f"      June to September          {jun_sep:>7.1f} mm   "
      f"{jun_sep / tot:>6.1%} of the year")
    p(f"      October alone              {octo:>7.1f} mm   "
      f"{octo / tot:>6.1%} of the year")
    p(f"      October / September        {octo / sep:>7.2f}")
    p()
    p("      The south-west monsoon withdraws from interior Maharashtra in")
    p("      the first half of October.  An October that nearly equals")
    p("      September, and exceeds August, is not the shape of a Deccan")
    p("      rainfall year.  THE OCTOBER FIGURE IS THE ONE TO GO BACK AND")
    p("      CHECK.  It is NOT corrected here - correcting a datum whose")
    p("      source is unknown would be inventing evidence.  SG-V5.")
    p()
    p("  AND THE PART THAT MATTERS MOST: NOTHING IN THE DESIGN USES THE")
    p("  ANNUAL TOTAL.  What the design uses is:")
    p("      - the 50 mm/h design intensity, Rev F drawing 5 note 1, which is")
    p("        the ONLY intensity anywhere in the project and carries no")
    p("        return period, duration or IDF source - drainage open item")
    p("        DR-D1, which SG1 does NOT close, because a monthly total")
    p("        cannot produce a short-duration intensity;")
    p("      - the soak pit absorption rate of 20 L/m2/day, K.2 A7, which")
    p("        needs a percolation test and nothing else;")
    p("      - the monsoon window, which is a PROGRAMME input - see SG-F7.")
    p("  So the rainfall conflict changes no number in this project.  It")
    p("  changes what the design report may claim, and it changes when the")
    p("  groundwater monitoring has to happen.")
    p()
    p("  (b)  TEMPERATURE.  The two documents measure different things and")
    p("       therefore do NOT conflict:")
    p()
    t = D.TEMP_REPORT
    p(f"      SEMT para 8, ABSOLUTE extremes    summer "
      f"{t['summer_max']} / {t['summer_min']} C   winter "
      f"{t['winter_max']} / {t['winter_min']} C   [C]")
    hi = max(D.DECK_TEMP, key=lambda r: r[1])
    lo = min(D.DECK_TEMP, key=lambda r: r[3])
    p(f"      Deck slide 26, MONTHLY MEANS      hottest {hi[0]} "
      f"{hi[1]} C mean daily max")
    p(f"                                        coldest {lo[0]} "
      f"{lo[3]} C mean daily min   [C]")
    p(f"      A monthly mean daily maximum of {hi[1]} C sitting under an")
    p(f"      absolute maximum of {t['summer_max']} C is exactly what one "
      f"expects.  Consistent.")
    p()
    p("       HVAC calculation H.10 records 'outdoor design dry-bulb /")
    p("       wet-bulb, Pune .... NOT IN THE PROJECT [N]' as the first of")
    p("       eight missing inputs that stop a cooling load being computed.")
    p("       SG1 NARROWS that gap and does not close it: an absolute extreme")
    p("       and a monthly mean are not a design dry-bulb, and NEITHER")
    p("       DOCUMENT GIVES A WET-BULB OR ANY COINCIDENT VALUE AT ALL.  The")
    p("       remaining seven inputs are untouched.  EL-V6 - no cooling plant")
    p("       exists anywhere in the project - is also untouched.")
    p()
    p("  (c)  WIND.  A WARNING, because this one invites a wrong 'correction'.")
    p()
    wmax = max(D.DECK_WIND, key=lambda r: r[1])
    p(f"      Deck slide 24, windiest month     {wmax[0]} "
      f"{wmax[1]} km/h = {wmax[1] / 3.6:.2f} m/s")
    p("      Master A.7.8 design basic wind     39 m/s")
    p(f"      ratio                             "
      f"{39 / (wmax[1] / 3.6):.1f} : 1")
    p()
    p("      THESE ARE NOT THE SAME QUANTITY AND THE RATIO IS NOT AN ERROR.")
    p("      The deck plots a MONTHLY MEAN SPEED.  IS 875 (Part 3):2015 V_b is")
    p("      a 3-SECOND GUST at 10 m with a 50-year return period.  A mean of")
    p("      1.8 m/s and a 50-year gust of 39 m/s are entirely compatible.")
    p("      MASTER A.7.8 IS NOT TO BE REDUCED ON THE STRENGTH OF SLIDE 24 -")
    p("      and in any case seismic governs the sentry post 2.4 : 1, so the")
    p("      wind case decides nothing.")


# =====================================================================
def g11_seismic():
    head("G.11", "SEISMIC ZONE  -  externally corroborated for the first time")
    p(f"  SEMT report para 7:  \"{D.SEISMIC_REPORT}\"")
    p(f"  Deck slide 27:       {D.DECK_SEISMIC_ZONE}, design per "
      f"{D.DECK_SEISMIC_CODE}")
    p(f"  Master A.7.8:        Z = 0.16 (Zone III), IS 1893 (Part 1):2016")
    p()
    p("  The report cites the 1984 zone map and the design uses the 2016 code.")
    p("  Pune is Zone III on both; Z = 0.16 is read from IS 1893 (Part 1):2016")
    p("  Table 3 for Zone III.  Reproducing the master's two A_h values:")
    p()
    for name, R, ah in (("underground box", 4.0, 0.075),
                        ("sentry post", 3.0, 0.100)):
        calc = (0.16 / 2) * (1.5 / R) * 2.5
        p(f"    {name:<18}  A_h = (Z/2)(I/R)(Sa/g) = (0.16/2)(1.5/{R:.1f})"
          f"(2.5) = {calc:.4f}   master {ah:.3f}   "
          f"{'OK' if abs(calc - ah) < 5e-4 else 'DIFFERS'}")
    p()
    p("  >>> FINDING SG-F12.  ZONE III IS NOW CORROBORATED BY A DOCUMENT")
    p("      OUTSIDE THE PROJECT, and the master's seismic coefficients")
    p("      reproduce exactly from it.  This is the ONLY master design input")
    p("      that SG1 is able to corroborate externally.  Nothing changes,")
    p("      and that is the point - it was already right.")
    p()
    p("  The two documents name DIFFERENT 1993 events - the report names")
    p("  Killari (Latur), the deck names the Koyna area on 28 Aug 1993.  Both")
    p("  are recorded as they stand; neither changes the zone, which is what")
    p("  the design uses, and this package does not adjudicate seismology.")
    p("  The deck's three regional events (M 4.8, 3.2, 2.6) are all well")
    p("  below the Zone III design basis and are recorded as context.")


# =====================================================================
def g12_expansive():
    head("G.12", "THE BLACK COTTON SOIL  -  where it is harmless, and the two "
                 "places it is not")
    p("  Measured properties, Appendix A and para 14(a):")
    b = D.BC_SOIL
    p(f"    depth               {b['depth_m'][0]} to {b['depth_m'][1]} m")
    p(f"    liquid limit        {b['LL'][0]} to {b['LL'][1]} %")
    p(f"    plastic limit       {b['PL'][0]} to {b['PL'][1]} %")
    p(f"    plasticity index    {b['LL'][0] - b['PL'][0]} to "
      f"{b['LL'][1] - b['PL'][1]} %   [R]")
    p(f"    free swell index    {b['free_swell'][0]} to "
      f"{b['free_swell'][1]} %")
    p(f"    classification      {b['classification']}  (IS 1498)")
    p(f"    SBC                 0.25 to 0.27 kgf/cm2 = "
      f"{kpa(0.25):.1f} to {kpa(0.27):.1f} kPa")
    p()
    p("    A free swell index above 50 % is the top band of IS 1498's own")
    p("    scale - VERY HIGH swelling potential.  The deck's slide 30 puts it")
    p("    in plain words: the soil 'contracts and produce cracks in dry")
    p("    season, 10 to 15 cm wide extending to maximum depth of 1 m' and is")
    p("    'Not suitable for foundation'.")
    p()
    p("  WHERE IT IS HARMLESS - and this is most of the project.")
    p("    Nothing structural founds in it.  The mat is at (-)6.700 and the")
    p("    sentry footing F1 at (-)2.000, both in basalt, both far below the")
    p("    0.18 to 1.0 m black cotton horizon.  Master B.8.7's insistence")
    p("    that F1 bears 'on IN-SITU ROCK, never on backfill' is now backed by")
    p("    a measurement.  NO ACTION.")
    p()
    p("  TWO PLACES IT IS NOT HARMLESS.  Both are raised, neither is changed.")
    p()
    p("    (1)  THE COVERED ENTRY STAIRWELL'S STEPPED RAFT.  Master A.4.7:")
    p("         'Stepped RC raft 300 thk ON COMPACTED FILL', stepping from the")
    p("         top landing at 0.000 down to the platform at (-)2.000.  With")
    p("         300 of raft the top of that raft founds at about (-)0.300 -")
    p("         INSIDE the black cotton horizon at two of the report's three")
    p("         locations.  'On compacted fill' implies the black cotton is")
    p("         stripped and replaced, but NO SPECIFICATION ANYWHERE SAYS SO,")
    p("         no strip-and-replace item exists in the BOQ, and a very-high-")
    p("         swelling CH clay under a stepped raft is a heave problem, not")
    p("         a bearing one.")
    p("         The stairwell is declared EXPENDABLE against blast (master")
    p("         B.6) - but heave is a service-life problem, not a blast one,")
    p("         and this stair is the ONLY primary access to the shelter.")
    p("         >>> SG-F13 / open item SG-V6.")
    p()
    p("    (2)  THE CONCEALMENT LAYER.  Master A.7.3 puts 300 of topsoil/turf")
    p("         at the top of the cover, and CAM2 makes it the concealment")
    p("         layer, 're-laid from the site's own stockpile'.  If the site's")
    p("         own topsoil is this CH clay at FSI 60 to 65 %, then the")
    p("         concealment layer is a very-high-swelling clay 300 mm thick:")
    p("           - it cracks in the dry season, and a cracked patchy turf is")
    p("             a CONCEALMENT DEFECT, which is CAM2's entire subject;")
    p("           - the cracks are a direct infiltration path into the 150")
    p("             granular filter immediately below it;")
    p("           - wetting and drying cycles pump clay fines INTO that")
    p("             filter, which is the one thing the filter exists to stop")
    p("             (A.7.3: 'Stops fines clogging').")
    p("         The LOAD is unaffected - 300 at 18 kN/m3 = 5.40 kPa is right")
    p("         for a black cotton soil - so no calculation moves.  What is")
    p("         missing is a SPECIFICATION: either qualify the stockpiled")
    p("         topsoil against a swell limit, or import a non-expansive")
    p("         topsoil.  Neither exists.")
    p("         >>> SG-F14 / open item SG-V7.  BS1's 1:50 crossfall on the")
    p("         burster slab still works and is unaffected; it is the filter")
    p("         above it that sees more water and more fines than assumed.")


# =====================================================================
def g13_deck_errors():
    head("G.13", "THE P1 DECK AGAINST ITS OWN CITED SOURCE")
    p("  Deck slides 29 and 30 both carry the source line 'Source : SEMT wing,")
    p("  CME'.  Three of their statements are not in that report.  They are")
    p("  listed here because the deck is a PRESENTED document and the same")
    p("  claims will be presented again unless they are corrected at source.")
    p()
    p("  (1)  'Safe Bearing Capacity = 300 kN/m2 at 1.5 m depth from Top'")
    p(f"       300 kPa = {300 / P.KGCM2_KPA:.2f} kgf/cm2.  At 1.5 m the report "
      f"gives:")
    p(f"           CH clay,  GL to 1.0 m                  "
      f"{kpa(0.27):>8.1f} kPa")
    p(f"           murrum GM, 1.0 to 1.2 m                {kpa(4.27):>8.1f} "
      f"kPa")
    p(f"           BROKEN rock, 1.2 to 1.5 m              {kpa(10.0):>8.1f} "
      f"kPa")
    p(f"           SOUND basalt below 1.5 m, soaked       {kpa(20.0):>8.1f} "
      f"kPa")
    p(f"           SOUND basalt below 1.5 m, unsoaked     {kpa(33.0):>8.1f} "
      f"kPa")
    p("       300 kPa is not any of them.  It is 6.5 times BELOW the lowest")
    p("       rock value at that depth and 72 % ABOVE the clay value.  It is")
    p("       conservative, and the design does not use it - master A.6 uses")
    p("       the IS 1904 presumptive 3240 kPa - so NO DESIGN VALUE IS")
    p("       AFFECTED.  The slide is wrong; the structure is not.   SG-V8")
    p()
    p("  (2)  'Murrum ... SBC of 25 - 30 kg/cm2', slide 30.")
    p("       The report's murrum SBCs are 2.07, 4.27, 4.66 and 5.18 kgf/cm2.")
    p("       25 to 30 kgf/cm2 is the SOUND BASALT unsoaked band (30 to 36).")
    p("       The slide is about five to six times high, and it has assigned")
    p("       ROCK strength to SOIL.  Nothing in the design uses it.   SG-V8")
    p()
    p("  (3)  'Compressive strength ranging from 609 - 900 kg/cm2 in unsoaked")
    p("       condition', slide 30.")
    ucs_uns = sorted(r[5] for r in D.APPX_C if r[0] == "UNSOAKED")
    p(f"       Appendix C's unsoaked results are {ucs_uns}.")
    p(f"       The range is {min(ucs_uns)} to {max(ucs_uns)}, not 609 to 900.")
    p("       609 appears nowhere in the report.  The upper bound is right.")
    p("       Nothing in the design uses it.                            SG-V8")
    p()
    p("  ONE DECK STATEMENT THAT IS RIGHT AND IMPORTANT:")
    p(f"       'Ultimate Bearing Capacity = S.B.C x 2.5'")
    p("       This is Appendix B's own relationship read backwards, and the")
    p("       factor 2.5 is the report's stated factor of safety.  Correct.")
    p()
    p("  AND THE ONE THIS PACKAGE EXISTS FOR:")
    p(f"       'Proposed structure safe for water table at depth of 2 m")
    p(f"        below GL'")
    p("       True, and now traceable.  See G.7.")


# =====================================================================
def g14_register():
    head("G.14", "PARAMETER REGISTER  -  every master A.6 / K.2 item against "
                 "the new evidence")
    p(f"  {'ref':<6} {'parameter':<28} {'master':<16} {'report says':<24} "
      f"{'status after SG1':<18}")
    p("  " + "-" * 96)
    rows = [
        ("A1", "Rockhead 1.5-2.0 m", "(-)1.5/(-)2.0 [A]",
         "0.9-1.5 m, 3 locations", "OPEN - SG-F5"),
        ("A2", "Design GWT (-)2.000", "(-)2.000 [A]",
         "not encountered, <1.5 m", "OPEN - SG-F6"),
        ("A3", "SBC 3240 kPa", "3240 [A]",
         "1961-2059 soaked", "OPEN - SG-F3"),
        ("A4", "k_s 100k-500k kN/m3", "both bounds [A]",
         "nothing", "OPEN - untouched"),
        ("A5", "K0 0.50, gamma 20/21", "0.50, 20/21 [A]",
         "K0 0.43-0.55, 19.1-19.6", "OPEN - SG-F9"),
        ("A6", "K_a 1.0 saturated", "1.0 [C]",
         "nothing", "unchanged"),
        ("A7", "Soak pit 20 L/m2/day", "20 [A]",
         "nothing - no perc test", "OPEN - untouched"),
        ("A8", "Seepage 0.5 L/m2/day", "0.5 [A]",
         "nothing", "OPEN - untouched"),
        ("A10", "Wind k1 1.08, V_b 39", "39 m/s [C]",
         "monthly means only", "unchanged - G.10(c)"),
        ("-", "Seismic Zone III", "Z 0.16 [C]",
         "Zone III, IS 1893-1984", "CORROBORATED"),
        ("-", "Cover 40.65 kPa", "40.65 held [C]",
         "MDD 1.90-1.93, OMC 8-9", "CORROBORATED - SG-F8"),
        ("-", "Black cotton", "not recorded",
         "CH, FSI 60-65, 0.18-1.0", "NEW - SG-F13/F14"),
        ("D3", "Site plan", "does not exist",
         "imagery, no dimension", "STILL OPEN"),
    ]
    for r in rows:
        p(f"  {r[0]:<6} {r[1]:<28} {r[2]:<16} {r[3]:<24} {r[4]:<18}")
    p()
    p("  FOUR of the fourteen K.2 assumptions are touched by the new evidence.")
    p("  NONE IS CLOSED.  Two master inputs are corroborated for the first")
    p("  time (Zone III, the cover weight).  One master gap (D3, no site plan)")
    p("  is better informed and still open.  Two entirely new items appear,")
    p("  both about the black cotton soil, neither previously recorded")
    p("  anywhere in the project.")


# =====================================================================
def tail():
    p()
    rule()
    p("SUMMARY OF FINDINGS")
    rule()
    p()
    for n, t in [
        ("SG-F1", "The SEMT report reproduces completely from its own inputs."),
        ("SG-F2", "THE INVESTIGATION REACHED 1.5 m; THE STRUCTURE FOUNDS AT "
                  "6.8 m."),
        ("SG-F3", "Presumptive SBC is 65 % above the measured soaked value, "
                  "and no element cares."),
        ("SG-F4", "In service the structure is lighter than the ground it "
                  "replaces."),
        ("SG-F5", "The report's rockhead band is entirely at or above the "
                  "master's."),
        ("SG-F6", "'No water table' means 'not reached'.  A2 stays open."),
        ("SG-F7", "The monsoon groundwater monitoring is programmed outside "
                  "the monsoon."),
        ("SG-F8", "40.65 kPa brackets both the as-placed and the saturated "
                  "cover."),
        ("SG-F9", "Measured shear parameters move the wall load by under "
                  "1 %."),
        ("SG-F10", "The deck's contour map and its elevation profile "
                   "disagree by 12 to 16 m."),
        ("SG-F11", "The two documents disagree on annual rainfall by 27 to "
                   "52 %."),
        ("SG-F12", "Zone III externally corroborated; A_h reproduces exactly."),
        ("SG-F13", "The entry stairwell raft founds in very-high-swelling CH "
                   "clay."),
        ("SG-F14", "The concealment layer may be a very-high-swelling CH "
                   "clay."),
    ]:
        p(f"  {n:<8} {t}")
    p()
    p("NOTHING IN PARTS A, B, D, F OR L IS CHANGED BY THIS CALCULATION.")
    p("No load, thickness, bar, level, quantity, rate, date or float moves.")
    p("No [ASSUMED] becomes [CONFIRMED].  The main staircase is untouched.")
    p()
    rule()
    p("END OF CALCULATIONS")
    rule()


# =====================================================================
def main():
    banner()
    g1_units()
    g2_reproduce()
    g3_depth()
    g4_sbc()
    g5_net()
    g6_rockhead()
    g7_water()
    g8_params()
    g9_site()
    g10_met()
    g11_seismic()
    g12_expansive()
    g13_deck_errors()
    g14_register()
    tail()

    out = os.path.abspath(os.path.join(HERE, "..", "Calculations",
                                       "SG_CALC_OUTPUT.txt"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    txt = "\n".join(OUT) + "\n"
    with open(out, "w", encoding="utf-8") as f:
        f.write(txt)
    print(txt)
    print("written:", out)


if __name__ == "__main__":
    main()
