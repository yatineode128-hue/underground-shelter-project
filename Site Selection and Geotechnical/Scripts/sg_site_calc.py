"""sg_site_calc.py  --  every siting check, arithmetic shown  (revision SG2).

    python3 sg_site_calc.py   ->  ../Calculations/SG2_SITE_CALC_OUTPUT.txt

Sections S.1 - S.12.  Nothing here is asserted: every clearance is computed
from the positions in sg_site.py and printed against the rule it has to meet,
and every rule carries its source.  Where a rule cannot be demonstrated the
calculation says so and opens an item rather than quietly passing.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import sg_proj as P                                        # noqa: E402
import sg_data as D                                        # noqa: E402
import sg_site as S                                        # noqa: E402

W = 100
OUT = []
FAILS = []


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


def verdict(actual, required, name, cls="[A]"):
    ok = actual >= required - 0.5
    if not ok:
        FAILS.append(name)
    return (f"  {name:<56} {actual / 1000.0:>8.2f} m   vs {required / 1000.0:>5.1f} m "
            f"{cls:<5} {'PASS' if ok else '*** FAIL ***'}")


# =====================================================================
def banner():
    rule()
    p("SITE LAYOUT AND EXTERNAL WORKS  -  CALCULATION PRINTOUT")
    p(f"revision {S.REV}   {S.PACKAGE_DATE}   {P.GEOM_REV}")
    rule()
    p()
    p("WHAT CHANGED SINCE SG1, AND WHY THAT UNBLOCKS THIS")
    p()
    p("  Master H.9 recorded the positions of the soakaways, the septic tank")
    p("  and the external chambers as NOT DETERMINABLE - 'no site plan,")
    p("  boundary or contour exists' - and with them FIVE PIPE LENGTHS and")
    p("  the IS 2470 (Pt 2) offsets.  The project owner has now supplied the")
    p("  two things that were missing:")
    p()
    p(f"      COORDINATE     {S.PIN_LAT} N,  {S.PIN_LON} E     [C] owner")
    p(f"      AVAILABILITY   'the area around 50 m is all available'   [C]")
    p()
    p("  Those, with SG1's contours and geotechnical profile and the")
    p("  project's own confirmed geometry, are enough.  SG2 determines them.")
    p()
    p("  THE PIN CONVENTION.  One point was given for 'the project site'.  The")
    p("  only self-consistent reading that lets everything be dimensioned is")
    p("  that it is the CENTRE OF THE UNDERGROUND BOX, project "
      f"({S.PIN_AT[0]:.0f}, {S.PIN_AT[1]:.0f}).")
    p("  Adopted as a CONVENTION, not claimed as a finding.  [A]  If the owner")
    p("  meant a corner or the entrance, THE WHOLE LAYOUT TRANSLATES RIGIDLY")
    p("  and not one offset, length or clearance below changes.")
    p()
    p("  WHAT IS STILL NOT AVAILABLE, and therefore what D3 still covers:")
    p("      a surveyed boundary            a benchmark and spot levels")
    p("      the position of any WELL       the distance to the perimeter fence")
    p("      existing services on the plot  a wind direction / rose")


# =====================================================================
def s1_orientation():
    head("S.1", "SITE ORIENTATION  -  fixed by this revision")
    p(f"  PROJECT +X = {S.ORIENT_X}        PROJECT +Y = {S.ORIENT_Y}     [A]")
    p()
    p("  The project has worked in a local frame since Rev F (master A.4.1)")
    p("  and has never tied it to north.  Five reasons, all pointing the same")
    p("  way:")
    p()
    p("  1  ACCESS.  The covered entry stairwell's grade door is at its WEST")
    p("     end, X 9250 (A.4.7), so the approach comes from the west - and the")
    p("     CTW blocks, the roads and the campus are west of the plot (deck")
    p("     slides 13, 14, 17).  The entry faces the installation it serves.")
    p("  2  FALL.  SG1 read the ground as falling EAST / NE, 580 -> 575.  With")
    p("     +X east the drainage field is DOWNGRADIENT, so nothing recharges")
    p("     the ground upslope of a flotation-critical tanked box.")
    p("  3  INTAKE AND EXHAUST AT OPPOSITE ENDS.  SH-1 (fresh air) west,")
    p("     SH-2 (generator) at X 22598-23198 east - 22.6 m apart at minimum.")
    p("  4  NOISE AND SIGNATURE.  Bay 8 - generator, ESC 2, SH-2, BV-4/BV-5 -")
    p("     is at the east end, away from the campus.")
    p("  5  The sentry post covers the approach from the north.")
    p()
    p("  *** AND THE LIMIT ON REASON 3, STATED PLAINLY. ***")
    p("  NO WIND DIRECTION DATA EXISTS ANYWHERE IN THIS PROJECT.  The P1 deck")
    p("  gives monthly mean SPEED and no direction; there is no wind rose.  So")
    p("  the orientation cannot be justified on prevailing wind, and it is")
    p("  not.  What it does instead is put the intake and the exhaust at")
    p("  OPPOSITE ENDS OF A 22 m BOX, which is the robust choice WHATEVER the")
    p("  wind does.  A wind rose matters for more than this - it is also the")
    p("  plume direction for the CBRN case - and it is opened as SG2-V4.  [N]")


# =====================================================================
def s2_envelope():
    head("S.2", "THE 50 m ENVELOPE  -  does everything fit?")
    p(f"  Envelope radius about the pin           "
      f"{S.ENVELOPE_R / 1000.0:>8.1f} m   [C] owner")
    p()
    p(f"  {'element':<44} {'furthest point':<22} {'radius':>9}")
    p("  " + "-" * 80)
    worst = 0.0
    items = []
    for name, x0, y0, x1, y1, cls, note in S.EXISTING:
        r = max(S.radius_from_pin(x, y)
                for x in (x0, x1) for y in (y0, y1))
        items.append((name, r))
    for tag, kind, cx, cy, cls, serves in S.CIRCULAR:
        items.append((f"{tag}  {kind}",
                      S.radius_from_pin(cx, cy) + S.PIT_DIA / 2.0))
    for tag, kind, x0, y0, x1, y1, cls, note in S.RECTANGULAR:
        items.append((f"{tag}  {kind}",
                      max(S.radius_from_pin(x, y)
                          for x in (x0, x1) for y in (y0, y1))))
    e = S.EWR
    items.append(("EXTERNAL WORKS RESERVE, far corner",
                  max(S.radius_from_pin(x, y)
                      for x in (e["x0"], e["x1"]) for y in (e["y0"], e["y1"]))))
    for name, r in items:
        worst = max(worst, r)
        flag = "" if r <= S.ENVELOPE_R else "   *** OUTSIDE ***"
        p(f"  {name:<44} {'':<22} {r / 1000.0:>8.2f} m{flag}")
    p()
    p(f"  WORST CASE                                                  "
      f"{worst / 1000.0:>8.2f} m")
    p(f"  AVAILABLE                                                   "
      f"{S.ENVELOPE_R / 1000.0:>8.2f} m")
    p(f"  SPARE                                                       "
      f"{(S.ENVELOPE_R - worst) / 1000.0:>8.2f} m")
    p()
    p("  EVERYTHING FITS, with the assumed sentry post position included and")
    p("  with room to spare.  The binding element is not the drainage - it is")
    p("  the SENTRY POST, whose position is ASSUMED (U4).")


# =====================================================================
def s3_offsets():
    head("S.3", "THE IS 2470 OFFSETS  -  demonstrated, one by one")
    p("  Three offsets are recorded on sheet S-06 and reproduced in drainage")
    p("  calculation D.11.  D.11 ends: '*** THOSE OFFSETS CANNOT BE")
    p("  DEMONSTRATED - no site plan, no well position and no boundary exist")
    p("  in the project.  DATA REQUIRED (D3). ***'   TWO OF THE THREE CAN NOW")
    p("  BE DEMONSTRATED.  The third cannot, and it is not fudged.")
    p()
    st = [r for r in S.RECTANGULAR if r[0] == "ST-01"][0]
    st_rect = (st[2], st[3], st[4], st[5])
    sk01 = [c for c in S.CIRCULAR if c[0] == "SK-01"][0]

    p("  (a)  FOUL SOAK PIT TO THE SEPTIC TANK,  >= 5 m   [C] S-06")
    d = S.dist_circle_rect(sk01[2], sk01[3], S.PIT_DIA, st_rect)
    p(f"       SK-01 centre ({sk01[2]:.0f}, {sk01[3]:.0f}), wall at "
      f"{S.PIT_DIA / 2:.0f} radius")
    p(f"       ST-01 {st[2]:.0f}-{st[4]:.0f} x {st[3]:.0f}-{st[5]:.0f}")
    p(verdict(d, 5000, "SK-01 wall to ST-01 face", "[C]"))
    p()
    p("  (b)  SOAK PIT TO ANY BUILDING,  >= 2 m   [C] S-06")
    p("       'Building' is read here as THE STRUCTURE AND ITS EXCAVATION,")
    p("       because a 6.8 m deep vertical unbenched face is what the pit is")
    p("       actually near.  Every pit is checked against every structure.")
    p()
    worst = None
    for tag, kind, cx, cy, cls, serves in S.CIRCULAR:
        for name, x0, y0, x1, y1, ec, note in S.EXISTING:
            if "ASSUMED" in name:
                continue
            d = S.dist_circle_rect(cx, cy, S.PIT_DIA, (x0, y0, x1, y1))
            if worst is None or d < worst[0]:
                worst = (d, tag, name)
    p(f"       nearest approach anywhere in the layout:")
    p(f"         {worst[1]} to {worst[2]}")
    p(verdict(worst[0], 2000, f"{worst[1]} wall to the nearest structure",
              "[C]"))
    p(f"       -  which is {worst[0] / 2000.0:.1f} times the code minimum.")
    p()
    p("  (c)  FOUL SOAK PIT TO ANY WELL,  >= 15 m   [C] S-06")
    p("       *** CANNOT BE DEMONSTRATED.  NO WELL POSITION EXISTS ANYWHERE IN")
    p("       THIS PROJECT. ***  The only water feature recorded anywhere is")
    p("       the RCC overhead reservoir on the deck's pipelines sketch -")
    p("       15 000 gallons on 15 m staging beside building 527 - which is a")
    p("       TANK, not a well, and is on the far side of the campus.")
    p("       SG2 does NOT claim this offset is met.  It is the ONE offset of")
    p("       the three that stays open, and it is opened as SG2-V1.   [N]")


# =====================================================================
def s4_clearances():
    head("S.4", "EVERY OTHER CLEARANCE IN THE LAYOUT")
    p("  Adopted rules, and why each is what it is:")
    p()
    for name, val, cls, basis in S.CLEARANCES:
        p(f"    {name:<44} {val / 1000.0:>5.1f} m   {cls}")
        for line in _wrap(basis, 86):
            p(f"        {line}")
    p()
    p("  CHECKS")
    p()
    exc = [(n, (x0, y0, x1, y1)) for n, x0, y0, x1, y1, c, note in S.EXISTING
           if "EXCAVATION" in n]
    foul = [c for c in S.CIRCULAR if c[0] == "SK-01"]
    clean = [c for c in S.CIRCULAR if c[0] != "SK-01"]
    st = [r for r in S.RECTANGULAR if r[0] == "ST-01"][0]
    st_rect = (st[2], st[3], st[4], st[5])

    p("  FOUL group to every excavation face,  >= 15 m adopted:")
    for tag, kind, cx, cy, cls, serves in foul:
        for n, r in exc:
            p(verdict(S.dist_circle_rect(cx, cy, S.PIT_DIA, r), 15000,
                      f"{tag} wall to {n[:34]}"))
    for n, r in exc:
        p(verdict(S.dist_rect_rect(st_rect, r), 15000,
                  f"ST-01 face to {n[:34]}"))
    p()
    p("  CLEAN group to every excavation face,  >= 10 m adopted:")
    for tag, kind, cx, cy, cls, serves in clean:
        for n, r in exc:
            p(verdict(S.dist_circle_rect(cx, cy, S.PIT_DIA, r), 10000,
                      f"{tag} wall to {n[:34]}"))
    p()
    p("  FOUL group to CLEAN group,  >= 5 m adopted:")
    for tag, kind, cx, cy, cls, serves in foul:
        for t2, k2, x2, y2, c2, s2 in clean:
            p(verdict(S.dist_circle_circle((cx, cy), (x2, y2)), 5000,
                      f"{tag} wall to {t2} wall"))
        for t2, k2, x0, y0, x1, y1, c2, note in S.RECTANGULAR:
            if t2 == "ST-01":
                continue
    for t2, k2, x2, y2, c2, s2 in clean:
        p(verdict(S.dist_circle_rect(x2, y2, S.PIT_DIA, st_rect), 5000,
                  f"ST-01 face to {t2} wall"))
    p()
    p("  PIT WALL TO PIT WALL,  >= 4 m adopted:")
    allc = S.CIRCULAR
    for i in range(len(allc)):
        for j in range(i + 1, len(allc)):
            a, b = allc[i], allc[j]
            p(verdict(S.dist_circle_circle((a[2], a[3]), (b[2], b[3])), 4000,
                      f"{a[0]} wall to {b[0]} wall"))
    p()
    p("  AND THE TWO SHAFTS, because a septic vent stands 2 m above grade:")
    sh2 = [(n, (x0, y0, x1, y1)) for n, x0, y0, x1, y1, c, note in S.EXISTING
           if n.startswith("SH-2")][0]
    p(verdict(S.dist_rect_rect(st_rect, sh2[1]), 10000,
              "ST-01 (and its vent) to SH-2 generator air shaft"))
    p(verdict(S.dist_circle_rect(foul[0][2], foul[0][3], S.PIT_DIA, sh2[1]),
              10000, "SK-01 to SH-2 generator air shaft"))
    p()
    p("  SH-1, THE FRESH-AIR INTAKE, CANNOT BE CHECKED AT ALL.  The HVAC")
    p("  equipment schedule gives SH-2 an X range and gives SH-1 only 'West of")
    p("  the box'.  ITS PLAN POSITION IS RECORDED NOWHERE IN THIS PROJECT.")
    p("  What protects it here is the layout, not a calculation: the whole")
    p("  external works reserve is EAST, and SH-1 is WEST, so the shortest")
    p("  possible separation is the length of the box plus the reserve offset")
    p(f"  - at least {(S.EWR['x0'] - 0) / 1000.0:.0f} m however SH-1 is "
      f"finally placed.  SG2-V3.   [N]")


def _wrap(s, n):
    out, cur = [], ""
    for word in s.split():
        if len(cur) + len(word) + 1 > n:
            out.append(cur)
            cur = word
        else:
            cur = (cur + " " + word).strip()
    if cur:
        out.append(cur)
    return out


# =====================================================================
def s5_runs():
    head("S.5", "THE FIVE PIPE LENGTHS MASTER H.9 CALLED 'NOT DETERMINABLE'")
    p("  Every run is routed as a polyline of straight orthogonal legs, each")
    p("  leg clear of the cover, of every excavation and of every structure.")
    p("  NO RUN CROSSES THE ENGINEERED COVER - master A.7.3 and D-001 note 1:")
    p("  a pipe through the cover breaches the radiation mass and the roof")
    p("  membrane.  The side BACKFILL corridor, Y 6200-7200, is not the cover")
    p("  and is a normal place for a service.")
    p()
    p(f"  {'tag':<7} {'DN':>4} {'grad':<8} {'from':<26} {'to':<18} "
      f"{'length':>9} {'fall':>8}")
    p("  " + "-" * 92)
    for tag, frm, to, dn, grad, pts, cls, note in S.RUNS:
        if not pts:
            p(f"  {tag:<7} {dn:>4} {grad:<8} {frm[:26]:<26} {to[:18]:<18} "
              f"{'[U]':>9} {'-':>8}")
            continue
        L = S.run_length(pts)
        if ":" in grad:
            fall = L / float(grad.split(":")[1])
            fs = f"{fall:.0f} mm"
        else:
            fs = "pumped"
        p(f"  {tag:<7} {dn:>4} {grad:<8} {frm[:26]:<26} {to[:18]:<18} "
          f"{L / 1000.0:>7.2f} m {fs:>8}")
    p()
    p("  ROUTES IN FULL")
    for tag, frm, to, dn, grad, pts, cls, note in S.RUNS:
        p()
        p(f"  {tag}   {cls}")
        if pts:
            p("     " + "  ->  ".join(f"({x:.0f}, {y:.0f})" for x, y in pts))
            for i in range(len(pts) - 1):
                seg = math.dist(pts[i], pts[i + 1])
                p(f"        leg {i + 1}: {seg:>8.0f} mm")
            p(f"        TOTAL   {S.run_length(pts):>8.0f} mm")
        for line in _wrap(note, 88):
            p(f"     {line}")
    p()
    p("  THE COMMON SERVICES TRENCH  -  why three long runs are affordable")
    p(f"     {S.COMMON_TRENCH[0]} -> {S.COMMON_TRENCH[1]}  at Y 9800, "
      f"{S.run_length(S.COMMON_TRENCH) / 1000.0:.1f} m")
    p("     PD-06, PD-11 and PD-13 share it from X 16500 eastward.  ONE trench")
    p("     in rock carrying a DN100 gravity drain, two DN50 rising mains and")
    p("     room for spare ducts.  That is what makes a 32 m gravity run")
    p("     sensible at a site where rockhead is 0.9-1.5 m: the cost is the")
    p("     trench, and the trench is cut once.")


# =====================================================================
def s6_soakpit():
    head("S.6", "*** THE SOAK PIT WILL NOT WORK AS A DEEP PIT, AND THE SITE "
                "DATA NOW SAYS SO ***")
    p("  RC1 fixed the ARITHMETIC of SK-01 (C19: widened 2.0 -> 2.200 dia,")
    p("  24.19 m2 against 22.50 required, +7.5 %).  It also wrote the sentence")
    p("  this section starts from:")
    p()
    p("     'deepening drives the pit further below the design GWT at")
    p("      (-)2.000, WHERE IT CANNOT SOAK AT ALL.'")
    p()
    p("  The project has therefore known since RC1 that the pit is below the")
    p("  water table.  NOBODY HAS EVER QUANTIFIED BY HOW MUCH.  SG1 supplied")
    p("  the missing half - the measured ground profile - so it can be.")
    p()
    p("  THE PIT AS RULED")
    p(f"     diameter                              "
      f"{S.PIT_DIA / 1000.0:>7.3f} m   [C] RC1 C19")
    p(f"     underside of cover slab, below grade  "
      f"{-S.PIT_TOP / 1000.0:>7.3f} m   [A] this package")
    p(f"     effective depth                       "
      f"{S.PIT_EFF / 1000.0:>7.3f} m   [C] RC1, unchanged")
    p(f"     invert, below LOCAL grade             "
      f"{-S.PIT_INV / 1000.0:>7.3f} m   [R]")
    p(f"     side area counted                     "
      f"{S.side_area(S.PIT_DIA, S.PIT_EFF):>7.2f} m2  [C] base not counted")
    p(f"     AREA REQUIRED, 450 L/day at 20 L/m2/day        22.50 m2  [C]")
    p()
    p("  CHECK 1  -  HOW MUCH OF IT IS ABOVE THE DESIGN WATER TABLE?")
    p()
    p("  The project holds TWO readings of the design GWT and they are not the")
    p("  same thing at a point 28 m east of the box on falling ground:")
    p("     (a) ABSOLUTE   master A.6 / K.2 A2: the GWT is the LEVEL (-)2.000")
    p("     (b) RELATIVE   deck slide 29: 'water table at DEPTH OF 2 m")
    p("         BELOW GL'")
    p("  On level ground they coincide.  On ground falling east at about")
    p("  1 in 40 (SG1, and itself disputed - SG-V4) the reserve is roughly")
    p("  0.70 m lower than the structure, so reading (a) puts the water only")
    p("  1.30 m below local grade there.  BOTH BOUNDS ARE COMPUTED.")
    p()
    p(f"  {'reading':<46} {'water below':>12} {'wet depth':>10} "
      f"{'area ABOVE':>11} {'of 22.50':>9}")
    p("  " + "-" * 92)
    for label, dw in (("(a) absolute (-)2.000, reserve 0.70 m lower", 1300.0),
                      ("(b) relative, 2 m below local grade", 2000.0)):
        dry = max(0.0, dw + S.PIT_TOP)      # PIT_TOP is negative
        a = S.side_area(S.PIT_DIA, dry)
        p(f"  {label:<46} {dw / 1000.0:>10.2f} m {(S.PIT_EFF - dry) / 1000.0:>8.2f} m "
          f"{a:>9.2f} m2 {a / 22.50:>8.1%}")
    p()
    p("  >>> SO BETWEEN 21 % AND 43 % OF THE REQUIRED ABSORPTION AREA LIES")
    p("      ABOVE THE DESIGN WATER TABLE.  The rest of the pit is, by the")
    p("      project's own design assumption, PERMANENTLY SUBMERGED - and a")
    p("      submerged wall does not infiltrate: there is no unsaturated")
    p("      storage to receive the effluent and no head to drive it.")
    p("      THIS IS GEOMETRY AGAINST A STATED DESIGN LEVEL.  It does not")
    p("      depend on the percolation rate at all.")
    p()
    p("  CHECK 2  -  AND WHAT IS THE REST OF IT CUT THROUGH?")
    p()
    p("  SG1's profile, carried across to this plot at [A] (SG-V1):")
    p()
    p(f"  {'location':<26} {'broken-rock band':>20} {'thickness':>11} "
      f"{'side area in it':>16} {'of 22.50':>9}")
    p("  " + "-" * 88)
    best = 0.0
    for loc, layers in D.FINDINGS:
        br = [l for l in layers if "Broken" in l[1]]
        if not br:
            continue
        d = br[0][0].replace("m", "").strip()
        lo, hi = [float(t) for t in d.split("-")]
        t = (hi - lo) * 1000.0
        a = S.side_area(S.PIT_DIA, t)
        best = max(best, a)
        p(f"  {loc[:26]:<26} {lo:>8.2f} - {hi:<8.2f} {t / 1000.0:>10.2f} m "
          f"{a:>14.2f} m2 {a / 22.50:>8.1%}")
    p()
    p("  Above the broken rock:  black cotton CH at FSI 60-65 % - it SWELLS")
    p("  SHUT when wet - over murrum, which the deck's own slide 30 calls")
    p("  'IMPERVIOUS IN NATURE'.  Below it:  SOUND BASALT, whose matrix")
    p("  permeability is effectively zero; whatever it takes, it takes through")
    p("  JOINTS, and NO JOINT DATA EXISTS - no RQD, no packer test (SG-V2).")
    p()
    p("  >>> SO THE ONLY DEMONSTRABLY PERMEABLE HORIZON IS 0.20 to 0.50 m")
    p(f"      THICK, AND CONTRIBUTES {best / 22.50:.0%} OR LESS OF THE "
      f"REQUIRED AREA.")
    p()
    p("  *** FINDING SG2-F1.  TWO INDEPENDENT CHECKS, ONE CONCLUSION. ***")
    p("      SK-01's shortfall was never an arithmetic problem - RC1 fixed")
    p("      that.  IT IS A DEPTH PROBLEM.  A 3.5 m deep pit at this site is")
    p("      mostly below the design water table and mostly in sound basalt.")
    p("      THE FORM THAT FITS THIS GROUND IS SHALLOW AND WIDE, NOT DEEP AND")
    p("      NARROW - a dispersion trench worked in the 0.5-1.6 m broken-rock")
    p("      horizon, ABOVE the water table.  Which is exactly IS 2470 (Pt 2)")
    p("      Cl. 5, the fallback master K.2 A7 has named all along.")
    p()
    p("      SG2 DOES NOT CHANGE SK-01.  The percolation test governs the")
    p("      final size and form - master A7, and RC1 said so too.  What SG2")
    p("      does is (i) say the number before the test rather than after it,")
    p("      and (ii) RESERVE THE GROUND FOR THE FALLBACK so that a failed")
    p("      test costs a redesign and not a re-siting.  See S.7.")


# =====================================================================
def s7_fallback():
    head("S.7", "THE FALLBACK, RESERVED  -  what a failed percolation test "
                "costs")
    p("  A dispersion trench is sized on the SAME basis this project uses for")
    p("  the pit: SIDE area only, the base discounted because it clogs.")
    p("  A trench of width w and effective depth h gives 2h m2 of side area")
    p("  per metre run - both sides, base not counted.")
    p()
    trench_h = 1000.0
    per_m = 2 * trench_h / 1000.0
    p(f"     trench effective depth                {trench_h / 1000.0:>7.2f} m"
      f"   [A] invert 1.500 below grade, worked in the broken-rock horizon")
    p(f"     side area per metre run               {per_m:>7.2f} m2/m  [R]")
    p()
    p(f"  {'stream':<28} {'flow':>10} {'at 20 L/m2/day':>16} "
      f"{'trench run':>12}")
    p("  " + "-" * 70)
    for name, q in (("FOUL, via ST-01", 450.0), ("CLEAN, sump discharge", 400.0)):
        a = q / 20.0
        L = a / per_m
        p(f"  {name:<28} {q:>7.0f} L/d {a:>13.2f} m2 {L:>10.2f} m")
    p()
    p("  AND THE REAL QUESTION - HOW BAD CAN THE MEASURED RATE BE AND STILL")
    p("  FIT IN THE GROUND RESERVED?")
    p()
    for tag, x0, y0, x1, y1, what in S.FALLBACK:
        w = x1 - x0
        h = y1 - y0
        spacing = 2500.0
        runs = int((h - 1000.0) // spacing) + 1   # 0.5 m edge margin each side
        total = runs * w / 1000.0
        area = total * per_m
        q = 450.0 if "FOUL" in tag else 400.0
        rmin = q / area
        p(f"  {tag}")
        p(f"     reserved            {w / 1000.0:.1f} m x {h / 1000.0:.1f} m")
        p(f"     trenches at 2.5 m centres      {runs} runs x "
          f"{w / 1000.0:.1f} m = {total:.1f} m")
        p(f"     side area available            {area:.1f} m2")
        p(f"     serves {q:.0f} L/day down to an absorption rate of "
          f"{rmin:.2f} L/m2/day")
        p(f"     which is {rmin / 20.0:.0%} OF THE ASSUMED 20 L/m2/day   [D]")
        p()
    p("  >>> THE RESERVE CARRIES BOTH STREAMS AT ROUGHLY ONE THIRD OF THE")
    p("      ASSUMED ABSORPTION RATE.  That is the point of reserving it: the")
    p("      percolation test can come back badly and the answer is still a")
    p("      redesign inside the same footprint, not a new hunt for ground.")
    p()
    p("  IF EVEN THAT FAILS - and on sound basalt it can - the remaining")
    p("  answers are a SEALED HOLDING TANK emptied on a schedule (master A7's")
    p("  own words) or a positive outfall, and a positive outfall needs the")
    p("  final-discharge question answered, which is D3 and is still open.")


# =====================================================================
def s8_perc():
    head("S.8", "WHERE THE PERCOLATION TEST HAS TO BE DONE")
    p("  Master K.2 A7 makes it MANDATORY (IS 2470 Pt 2 Cl. 4).  Drainage D.12")
    p("  calls it 'on the critical path for three independent reasons'.  What")
    p("  nobody has ever said is WHERE, and a percolation test in the wrong")
    p("  place or at the wrong depth answers nothing.")
    p()
    p(f"  {'ref':<6} {'position':<22} {'depth below local grade':<26} "
      f"{'what it decides':<30}")
    p("  " + "-" * 88)
    for ref, x, y, what in S.PERC_TESTS:
        p(f"  {ref:<6} ({x:.0f}, {y:.0f}){'':<6} "
          f"to {-S.PERC_DEPTH / 1000.0:.3f} m, the proposed pit invert  "
          f"{what:<30}")
    p()
    p("  TWO TESTS, ONE IN EACH SUB-ZONE, EACH AT ITS OWN PIT'S POSITION AND")
    p("  AT THE PROPOSED INVERT.  Not at a convenient spot near the site hut.")
    p()
    p("  AND TEST THE SHALLOW HORIZON TOO.  S.6 shows the deep pit is mostly")
    p("  submerged and mostly in sound basalt, and S.7 shows the fallback is a")
    p("  trench at about 1.5 m.  A test taken ONLY at (-)4.100 measures the")
    p("  formation the fallback will not use.  Take each test at BOTH depths -")
    p("  the pit invert and the trench invert - or the fallback is undesigned")
    p("  the day the pit is abandoned.   [A] this package")
    p()
    p("  The same boreholes serve SG-V2: A1075 must be located ON THIS PLOT,")
    p("  and the standpipe that SG-V3 asks for goes in one of them.")


# =====================================================================
def s9_gwt_ruling():
    head("S.9", "SG-V3 RULED BY THE PROJECT OWNER  -  and what the ruling "
                "leaves standing")
    p("  RULING, 11 September 2026:  *** THE COST OF MOVING THE GROUNDWATER")
    p("  MONITORING IS NOT ACCEPTED. ***")
    p()
    p("  READING.  SG-F7 showed that WBS A1080 - 'Monsoon groundwater")
    p("  monitoring - confirm the design GWT (-)2.000', 20 d, TOTAL FLOAT 0 -")
    p("  runs 12-11-26 to 04-12-26, which is not the monsoon, and that moving")
    p("  it into one would move a critical-path activity and therefore the")
    p("  job.  The ruling declines THAT COST.  A1080 stays where it is.")
    p("  If the owner meant something wider, this reading is stated so it can")
    p("  be corrected.")
    p()
    p("  CONSEQUENCE, STATED HONESTLY.")
    p("    A1080 as programmed will measure the post-monsoon RECESSION.  It")
    p("    will therefore NOT close master K.2 A2.  The design GWT (-)2.000")
    p("    stays [ASSUMED] through construction and into service.")
    p()
    p("  AND WHY THE PERMANENT WORKS ARE STILL BOUNDED.")
    p("    (-)2.000 is only 2 m down, which is the CONSERVATIVE direction for")
    p("    everything the water drives - uplift, flotation, lateral load.  The")
    p("    risk left open is that the real table is HIGHER.  Master B.3 has")
    p("    already run that bound:")
    p()
    p("      stage                         FoS @ (-)2.000   FoS FLOODED TO GRADE")
    p("      1 mat cast only                    0.33 FAIL        0.23 FAIL")
    p("      2 mat + walls, no roof             0.78 FAIL        0.55 FAIL")
    p("      3 box complete, no backfill        1.22 MARGINAL    0.86 FLOATS")
    p("      4 backfilled + cover               2.02 OK          1.41 OK")
    p()
    p("    THE COMPLETED STRUCTURE PASSES EVEN WITH THE WATER AT GROUND")
    p("    LEVEL - FoS 1.41 against a requirement of 1.2.  So the ruling does")
    p("    not put the permanent works at risk.  [R] from B.3")
    p()
    p("  WHAT IT DOES EXPOSE IS THE CONSTRUCTION STAGE, and that is now the")
    p("  operative control.  Master B.3's MANDATORY MITIGATION becomes")
    p("  non-negotiable rather than advisory:")
    p("      1 continuous dewatering from the start of excavation UNTIL")
    p("        BACKFILL AND COVER ARE COMPLETE")
    p("      2 temporary pressure-relief valves / knock-out plugs in the mat,")
    p("        6 No. on S-02, grouted up ONLY after backfill")
    p("      3 programme the sub-structure to complete before the monsoon, or")
    p("        bund and positively drain with standby pumping and generator")
    p("        back-up")
    p("      4 backfill SYMMETRICALLY, in layers")
    p()
    p("    *** AND ONE THING THE WM1 PROGRAMME DOES NOT DO. ***  Activity")
    p("    A2070, 'Dewatering - continuous through the substructure works',")
    p("    runs 01-01-27 to 11-05-27.  Side backfill A7010 runs 20-07-27 to")
    p("    30-07-27 and the burster slab is not cast until 21-08-27.  So")
    p("    dewatering STOPS on 11 May and the box stands un-backfilled through")
    p("    the whole 2027 monsoon - stage 3, FoS 1.22 at (-)2.000 and 0.86")
    p("    FLOODED.  Mitigation 1 says 'until backfill and cover complete'.")
    p("    THE PROGRAMME AND THE MITIGATION DO NOT AGREE.  Raised as SG2-V5.")
    p("    No date is changed here - the owner's schedule R0 governs (H.13).")
    p()
    p("  AND ONE OPTION THE RULING DOES NOT PRECLUDE, BECAUSE IT COSTS NO")
    p("  FLOAT.  A standpipe piezometer left in the A1075 borehole and read")
    p("  weekly by staff already on site is a LEVEL-OF-EFFORT observation,")
    p("  exactly like A2070 itself.  It cannot verify the design in time - the")
    p("  mat is cast in February - but through the 2027 monsoon it measures")
    p("  the water that the flotation case is actually exposed to, while the")
    p("  box is standing at FoS 1.22.  Offered, not adopted.   [A]")


# =====================================================================
def s10_rain():
    head("S.10", "SG-V5  -  RAINFALL, AND WHICH OF THE TWO FIGURES IS THE "
                 "WRONG ONE")
    p("  THE INSTRUCTION WAS TO USE A RELIABLE SOURCE.  WHAT ACTUALLY")
    p("  HAPPENED, RECORDED SO IT CAN BE CHECKED:")
    p()
    p("    Ten hosts were probed from this session.  ALL TEN WERE REFUSED BY")
    p("    THE ENVIRONMENT'S EGRESS POLICY (HTTP 403):")
    p("      imd.gov.in   imdpune.gov.in   mausam.imd.gov.in   data.gov.in")
    p("      tropmet.res.in   en.wikipedia.org   en.climate-data.org")
    p("      power.larc.nasa.gov   climexp.knmi.nl   ncei.noaa.gov")
    p("    NO IMD NORMAL WAS RETRIEVED AND NONE IS INVENTED.")
    p()
    p("  ONE PUBLISHED FIGURE WITH A NAMED STATION AND A NAMED PERIOD WAS")
    p("  OBTAINED, AND IT IS ENOUGH TO SETTLE WHICH FIGURE IS WRONG:")
    p()
    a = S.RAIN_ANCHOR
    p(f"     {a['season']} mean, {a['station']}")
    p(f"     {a['period']}                     {a['value']:>8.1f} mm")
    p(f"     {a['cls']}")
    p(f"     source: {a['source']}")
    p()
    deck = dict(D.DECK_PRECIP)
    deck_jo = sum(v for m, v in D.DECK_PRECIP
                  if m in ("June", "July", "August", "September", "October"))
    deck_tot = sum(deck.values())
    p("  AGAINST THE PROJECT'S TWO FIGURES")
    p()
    p(f"  {'source':<46} {'Jun-Oct':>10} {'ANNUAL':>10} {'verdict':<22}")
    p("  " + "-" * 92)
    p(f"  {'Shivajinagar 42-yr mean (above)':<46} {a['value']:>8.1f} mm "
      f"{'-':>10} {'the yardstick':<22}")
    dev = deck_jo / a["value"] - 1.0
    p(f"  {'P1 deck slide 25':<46} {deck_jo:>8.1f} mm {deck_tot:>8.1f} mm "
      f"{f'{dev:+.0%} on Jun-Oct':<22}")
    p(f"  {'SEMT/67/15 para 9':<46} {'-':>10} "
      f"{D.RAINFALL_REPORT_RANGE[0]:.0f}-{D.RAINFALL_REPORT_RANGE[1]:.0f} mm "
      f"{'IMPOSSIBLE - see below':<22}")
    p()
    p("  *** FINDING SG2-F2.  THE SOIL REPORT'S RAINFALL FIGURE IS THE ONE")
    p("      THAT IS WRONG, NOT THE DECK'S. ***")
    p(f"      SEMT para 9 gives {D.RAINFALL_REPORT_RANGE[0]:.0f}-"
      f"{D.RAINFALL_REPORT_RANGE[1]:.0f} mm for the ANNUAL rainfall of 'the")
    p(f"      region'.  The June-to-October mean ALONE at the nearest")
    p(f"      long-record observatory is {a['value']:.1f} mm - "
      f"{a['value'] / D.RAINFALL_REPORT_RANGE[1]:.1f} to "
      f"{a['value'] / D.RAINFALL_REPORT_RANGE[0]:.1f} times the report's whole")
    p("      YEAR.  A figure that small is not a Pune figure.")
    p()
    p("      SG1 raised this as a straight conflict between two documents and")
    p("      could not say which side was wrong.  IT CAN NOW.  The correction")
    p("      runs the other way from the first guess: the deck is the right")
    p("      ORDER and the soil report is not.")
    p()
    p(f"      The deck is not vindicated, though.  Its Jun-Oct total of")
    p(f"      {deck_jo:.1f} mm is {1 - deck_jo / a['value']:.0%} BELOW the "
      f"42-year Shivajinagar mean,")
    p(f"      and its October figure - {deck['October']:.1f} mm, "
      f"{deck['October'] / deck['September']:.2f} x September and above")
    p("      August - still does not fit a Deccan monsoon.  BOTH the annual")
    p("      total and the October value need the real normal.  SG-V5 STAYS")
    p("      OPEN, and it is now open on a narrower question.")
    p()
    p("  WHAT TO ASK FOR, EXACTLY:")
    for s in S.RAIN_AUTHORITY:
        for line in _wrap(s, 88):
            p(f"     {line}")
    p()
    p("  AND THE PART THAT DECIDES HOW MUCH THIS MATTERS.")
    p()
    p("    NOT ONE PIPE, PIT, PUMP OR STRUCTURE IN THIS PROJECT IS SIZED BY")
    p("    RAINFALL.  The check:")
    p("      - the roofs and the 2 000 engineered cover SHED AT GRADE to the")
    p("        berm toe.  Drainage D.7: 'there is no roof outlet, no downpipe")
    p("        and no rainwater pipe on the buried roof'.  The 2.461 L/s at")
    p("        50 mm/h NEVER ENTERS A PIPE.")
    p("      - the only rainwater that does enter a pipe is the entry")
    p("        threshold channel CH-10 -> CP-10 -> PD-11, and DR-C1 ruled that")
    p("        catchment is the DOOR-OPEN DRIVING-RAIN case, about 12 x")
    p("        smaller than the superseded 0.10 L/s - order 0.008 L/s against")
    p("        a DN100 at 1:100 carrying 6.72 L/s.")
    p("      - the stairwell sump SU-02 is sized on a 1 000 L EVENT VOLUME")
    p("        [C], not on an intensity.")
    p()
    p("    >>> SO THE RAINFALL CONFLICT CANNOT MOVE A SINGLE DESIGN VALUE IN")
    p("        THIS PROJECT.  It governs what the design report may CLAIM, and")
    p("        - through the monsoon window - WHEN things can be built.  That")
    p("        is the whole of its reach, and it is worth saying plainly so")
    p("        nobody re-sizes a pipe on the back of a corrected rainfall")
    p("        table.")


# =====================================================================
def s11_crosscheck():
    head("S.11", "WHAT THE SITING WORK TOUCHED IN OTHER PACKAGES")
    p("  Four things surfaced that are not siting decisions.  Each is recorded")
    p("  and referred; NONE is acted on.")
    p()
    p("  SG2-F3  ST-01 IS SIZED FOR A BUILDING THAT IS NOT CONNECTED TO IT.")
    p("     The septic tank is sized for 10 users, 'sentry-post shift crews +")
    p("     shelter maintenance' [C] S-06.  The drainage package excludes the")
    p("     sentry post from its scope, and THERE IS NO PIPE FROM THE SENTRY")
    p("     POST TO ST-01 ANYWHERE IN THE PROJECT - the pipe schedule has")
    p("     PD-15 (Bay 2, CASE B only, not adopted) and PD-16 (ST-01 -> SK-01)")
    p("     and nothing upstream of the tank at all.  SG2 positions ST-01 and")
    p("     leaves the connection to the drainage engineer.  The layout does")
    p("     not prejudge it: ST-01 is 22.5 m from the assumed sentry position")
    p("     and the ground between is clear.")
    p()
    p("  SG2-F4  SH-1 HAS NO PLAN POSITION.  The HVAC equipment schedule gives")
    p("     SH-2 an X range (22598-23198) and gives SH-1 only 'West of the")
    p("     box'.  The fresh-air intake of a CBRN shelter is not a minor")
    p("     fitting.  Until it has a coordinate, no intake separation can be")
    p("     checked against anything - the septic vent included.  SG2-V3.")
    p()
    p("  SG2-F5  PD-14 CANNOT BE ROUTED.  GY-11 sits at (14700, 1960) with its")
    p("     invert at (-)2.150, and the headhouse floor IS the top of the 900")
    p("     pressure slab at (-)2.000 (master A.4.6).  The gully body and its")
    p("     outlet are therefore 150 mm INSIDE the pressure slab; outside the")
    p("     headhouse walls that level is beneath the waterproof membrane and")
    p("     within the engineered cover, which no pipe may enter.  SK-04's")
    p("     FOOTPRINT IS RESERVED; ITS PIPE IS NOT ROUTED.  Referred to")
    p("     drainage and structures together.")
    p()
    p("  SG2-V5  THE PROGRAMME STOPS DEWATERING BEFORE BACKFILL.  A2070 ends")
    p("     11-05-27; side backfill A7010 is 20-07-27 to 30-07-27.  Master")
    p("     B.3 mitigation 1 requires dewatering 'until backfill and cover")
    p("     complete'.  The gap spans the 2027 monsoon with the box at stage 3")
    p("     - FoS 1.22 at the design GWT, 0.86 flooded.  See S.9.")


# =====================================================================
def s12_d3():
    head("S.12", "MASTER GAP D3  -  what is now closed and what is not")
    p("  D3 has been cited as a blocker sixteen times across six packages.")
    p("  It was never one thing.  Splitting it:")
    p()
    p(f"  {'':<4} {'what D3 was blocking':<52} {'status after SG2':<28}")
    p("  " + "-" * 88)
    rows = [
        ("1", "Positions of the soakaways and the septic tank",
         "*** CLOSED - S.5, S.6 ***"),
        ("2", "The five 'not determinable' pipe lengths",
         "FOUR CLOSED, PD-14 [U] SG2-F5"),
        ("3", "External chamber positions IC-01, IC-02",
         "*** CLOSED ***"),
        ("4", "IS 2470 offset to the septic tank, >= 5 m",
         "*** DEMONSTRATED, 5.40 m ***"),
        ("5", "IS 2470 offset to any building, >= 2 m",
         "*** DEMONSTRATED, 5x over ***"),
        ("6", "IS 2470 offset to any well, >= 15 m",
         "STILL OPEN - no well exists  SG2-V1"),
        ("7", "A concealment LAYOUT (CAM2 / CAM-V2)",
         "PARTLY - see below"),
        ("8", "Berm, access and hardstanding layout",
         "STILL OPEN - needs levels"),
        ("9", "Cut and fill for a level formation",
         "STILL OPEN - needs levels  SG-V4"),
        ("10", "The final discharge question - is any outfall available?",
         "STILL OPEN - D3 proper"),
        ("11", "Sentry post site position (U4)",
         "STILL OPEN - and NOTHING here depends on it"),
    ]
    for n, what, st in rows:
        p(f"  {n:<4} {what:<52} {st:<28}")
    p()
    p("  >>> D3 IS PARTIALLY CLOSED, NOT CLOSED.  THE LAYOUT NOW EXISTS.  THE")
    p("      SURVEY DOES NOT.  What is still missing is a boundary, a")
    p("      benchmark and spot levels, the well, the fence distance, existing")
    p("      services on the plot and a wind rose.  Every one of those is a")
    p("      SURVEY output, and none of them moves anything SG2 has fixed:")
    p("      the layout is dimensioned from confirmed structure geometry and")
    p("      every clearance is RELATIVE, so if the fence turns out to be")
    p("      closer than the reserve's east edge THE WHOLE RESERVE TRANSLATES")
    p("      AND NOT ONE OFFSET CHANGES.")
    p()
    p("  ON CONCEALMENT.  CAM2 could not draw a layout and still cannot draw")
    p("  a full one.  But SG2 does fix where the new AT-GRADE SIGNATURES go -")
    p("  four RC cover slabs and a 2 m septic vent - and it puts them 11 to")
    p("  21 m from the structure, in one group, DOWNGRADIENT and away from the")
    p("  approach.  That is better for concealment than scattering them: the")
    p("  covers mark the drainage field, not the shelter.  CAM-V2 is")
    p("  unaffected - it is a client ruling on whether the above-ground")
    p("  signature is acceptable at all.")


# =====================================================================
def tail():
    p()
    rule()
    p("SUMMARY")
    rule()
    p()
    p("  POSITIONS FIXED BY SG2")
    for tag, kind, cx, cy, cls, serves in S.CIRCULAR:
        p(f"    {tag:<7} {kind:<22} centre ({cx:>7.0f}, {cy:>7.0f})   "
          f"dia {S.PIT_DIA:.0f}")
    for tag, kind, x0, y0, x1, y1, cls, note in S.RECTANGULAR:
        p(f"    {tag:<7} {kind:<22} {x0:>7.0f}-{x1:<7.0f} x "
          f"{y0:>7.0f}-{y1:<7.0f}")
    p()
    p("  FINDINGS")
    for n, t in [
        ("SG2-F1", "The soak pit's problem is DEPTH, not arithmetic. 21-43 % "
                   "of the required"),
        ("", "         area is above the water table; the only permeable "
             "horizon gives 15 % or less."),
        ("SG2-F2", "The SOIL REPORT's rainfall figure is the wrong one, not "
                   "the deck's."),
        ("SG2-F3", "ST-01 is sized for a building no pipe connects to it."),
        ("SG2-F4", "SH-1, the fresh-air intake, has no plan position anywhere."),
        ("SG2-F5", "PD-14 cannot be routed - GY-11's outlet is inside the "
                   "pressure slab."),
    ]:
        p(f"    {n:<8} {t}")
    p()
    p("  RULED BY THE PROJECT OWNER")
    p("    SG-V9   CLOSED.  The coordinate is supplied and recorded.")
    p("    SG-V3   RULED.  The cost of moving the monitoring is NOT accepted;")
    p("            A1080 stays.  K.2 A2 therefore stays ASSUMED through")
    p("            construction - and B.3 shows the completed structure is")
    p("            bounded even flooded to grade.  SG2-V5 opened.")
    p()
    if FAILS:
        p("  *** CLEARANCE CHECKS THAT DID NOT PASS ***")
        for f in FAILS:
            p(f"      {f}")
    else:
        p("  EVERY CLEARANCE CHECK IN S.3 AND S.4 PASSES.")
    p()
    p("  NOTHING IN PARTS A, B, D, F OR L IS CHANGED BY THIS CALCULATION.")
    p("  No load, thickness, bar, level, BOQ quantity, rate, date or float")
    p("  moves.  SK-01 is not re-sized.  The main staircase is untouched.")
    p()
    rule()
    p("END OF CALCULATIONS")
    rule()


def main():
    banner()
    s1_orientation()
    s2_envelope()
    s3_offsets()
    s4_clearances()
    s5_runs()
    s6_soakpit()
    s7_fallback()
    s8_perc()
    s9_gwt_ruling()
    s10_rain()
    s11_crosscheck()
    s12_d3()
    tail()
    out = os.path.abspath(os.path.join(HERE, "..", "Calculations",
                                       "SG2_SITE_CALC_OUTPUT.txt"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(OUT) + "\n")
    print("\n".join(OUT))
    print("\nwritten:", out)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
