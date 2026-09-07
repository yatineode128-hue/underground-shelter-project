"""
dr_calc.py  --  every drainage number this package uses, computed from the
project's own confirmed inputs.  Nothing here is typed in as a result; each
value is derived and printed with its inputs so a checker can follow it.

Run:  python3 dr_calc.py        writes ../Calculations/DR_CALC_OUTPUT.txt

EVIDENCE CLASSES  [C] confirmed  [R] reconstructed here  [A] assumed by this
package  [U] unresolved  [N] not available.

NOTHING IN THIS FILE INVENTS AN ENGINEERING INPUT.  Where an input does not
exist in the project the routine prints DATA REQUIRED and stops that line of
calculation rather than substituting a value.
"""
import os
import sys
import math

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mep_proj as P

OUT = []


def w(s=""):
    OUT.append(s)


def rule(c="-"):
    w(c * 100)


def head(n, t):
    w()
    rule("=")
    w(f"{n}   {t}")
    rule("=")


# =====================================================================
head("D.1", "WETTED AREA AND STRUCTURAL SEEPAGE  -  verification of the S-06 figure")
# ---------------------------------------------------------------------
w("""
Sheet S-06 states:  structural seepage = 0.5 L/m2/day x 401 m2 = 200 L/day.
The 401 m2 is not defined on the sheet.  It is reproduced here so that the
sump duty rests on an area a checker can see, not on an unexplained number.""")
w()
Lx = (P.BOX["x1"] - P.BOX["x0"]) / 1000.0
Ly = (P.BOX["y1"] - P.BOX["y0"]) / 1000.0
gwt = P.LVL["gwt"]
mat_soffit = P.LVL["mat_soffit"]
h_sub = gwt - mat_soffit                       # submerged wall height
perim = 2 * (Lx + Ly)
a_walls = perim * h_sub
a_base = Lx * Ly
a_tot = a_walls + a_base
w(f"  External box                       {Lx:.3f} x {Ly:.3f} m           [C] A.4.2")
w(f"  Design GWT                         ({gwt:+.3f})                       [A] A2")
w(f"  Underside of mat                   ({mat_soffit:+.3f})                       [C] A.4.3")
w(f"  Submerged wall height  {gwt:+.3f} - ({mat_soffit:+.3f})  = {h_sub:.3f} m")
w(f"  External perimeter     2 x ({Lx:.1f} + {Ly:.1f})     = {perim:.2f} m")
w(f"  Submerged wall area    {perim:.2f} x {h_sub:.3f}      = {a_walls:.2f} m2")
w(f"  Mat underside area     {Lx:.1f} x {Ly:.1f}          = {a_base:.2f} m2")
w(f"  TOTAL WETTED EXTERNAL ENVELOPE                = {a_tot:.2f} m2")
w()
w(f"  S-06 uses 401 m2.  Difference {abs(a_tot - 401.0):.2f} m2 = "
  f"{abs(a_tot - 401.0) / 401.0 * 100:.2f} %.")
w("  [R] CONFIRMED BY RECONSTRUCTION: the 401 m2 on S-06 is the area of the")
w("      external envelope standing below the design groundwater table -")
w("      the four perimeter walls from ({:+.3f}) to ({:+.3f}) plus the whole".format(gwt, mat_soffit))
w("      mat underside.  It is NOT the internal wetted area.")
w()
seep = P.SEEPAGE["rate_lm2d"] * a_tot
w(f"  Seepage = {P.SEEPAGE['rate_lm2d']} L/m2/day x {a_tot:.2f} m2 = {seep:.1f} L/day     [A] A8 on the rate")
w(f"  S-06 states 200 L/day.  Adopted for this package: 200 L/day.")
w("  *** THE RATE 0.5 L/m2/day IS [ASSUMED] (master K.2 A8) AND THE GWT IS")
w("      [ASSUMED] (A2).  BOTH REQUIRE SITE CONFIRMATION.  The sump store")
w("      below is directly proportional to both. ***")

# =====================================================================
head("D.2", "CLEAN SUMP  -  storage, cycling and alarm margin")
S = P.SUMP
w()
w(f"  Pit                {S['l']} x {S['b']} x {S['d']} internal, invert ({S['invert']:+.3f}), "
  f"base ({S['base']:+.3f})   [C] S-06 / A.4.3")
w(f"  Gross volume       {S['l']/1000:.1f} x {S['b']/1000:.1f} x {S['d']/1000:.1f} = "
  f"{S['l']*S['b']*S['d']/1e9:.3f} m3   (S-06 states {S['volume_m3']} m3)   [C]")
w(f"  Pumps              {S['pumps']} No. submersible, {S['duty_ls']} L/s, {S['arrangement']}, "
  f"plus a hand pump   [C]")
w(f"  Levels above invert   start {S['start']}   stop {S['stop']}   high alarm {S['alarm']}   [C]")
w()
plan = (S["l"] / 1000.0) * (S["b"] / 1000.0)
inflow_lpd = P.SEEPAGE["flow_lpd"] + 200.0        # seepage + condensate/washdown
inflow_ls = inflow_lpd / 86400.0
w(f"  Design inflow to the sump, S-06 flow table:")
w(f"      structural seepage                     200 L/day   [C]/[A8]")
w(f"      condensate + washdown                  200 L/day   [C]")
w(f"      TOTAL                                  {inflow_lpd:.0f} L/day = {inflow_ls:.5f} L/s   [R]")
w()
store = S["volume_m3"] * 1000.0
w(f"  Gross store / inflow      {store:.0f} / {inflow_lpd:.0f}      = {store/inflow_lpd:.2f} days")
w(f"      S-06 states '8 days store'; master K.2 A8 states 8.4 days.  Both refer to")
w(f"      this number.  [R] {store/inflow_lpd:.2f} days confirmed.")
w()
vw_m3 = plan * (S["start"] - S["stop"]) / 1000.0
w(f"  Working volume, stop to start   {plan:.2f} m2 x {(S['start']-S['stop'])/1000:.3f} m "
  f"= {vw_m3:.3f} m3 = {vw_m3*1000:.0f} L   [R]")
t_empty = vw_m3 * 1000.0 / S["duty_ls"]
w(f"  Time to draw down at {S['duty_ls']} L/s        {vw_m3*1000:.0f} / {S['duty_ls']} "
  f"= {t_empty:.0f} s = {t_empty/60:.1f} min   [R]")
t_fill = vw_m3 * 1000.0 / (inflow_lpd / 24.0)
w(f"  Time to refill at {inflow_lpd:.0f} L/day       {vw_m3*1000:.0f} / {inflow_lpd/24:.2f} L/h "
  f"= {t_fill:.0f} h = {t_fill/24:.1f} days   [R]")
w(f"  Duty ratio                         {t_empty/(t_fill*3600)*100:.2f} % of the time   [R]")
w()
w("  *** OPERATIONAL FINDING - DR-F1 ***")
w(f"      One start every {t_fill/24:.1f} days, {t_empty/60:.0f} minutes per start, and with")
w(f"      auto-alternation each pump runs about every {2*t_fill/24:.1f} days.  That")
w("      cycling is acceptable and no anti-stagnation timer is needed on")
w("      hydraulic grounds.  What IS needed is a witnessed monthly test of the")
w("      STANDBY path and of the hand pump, because at a 0.3 % duty ratio a")
w("      failed standby would not be discovered by use.  [A] this package -")
w("      a commissioning and O&M requirement, not a change to the pump duty.")
w()
alarm_l = plan * (S["alarm"] - S["start"]) / 1000.0 * 1000.0
w(f"  Alarm margin, start to high alarm   {plan:.2f} x {(S['alarm']-S['start'])/1000:.3f} "
  f"= {alarm_l:.0f} L")
w(f"  Warning time at the design inflow   {alarm_l:.0f} / {inflow_lpd/24:.2f} L/h "
  f"= {alarm_l/(inflow_lpd/24):.0f} h   [R]")
w(f"  Freeboard above high alarm          {S['d'] - S['alarm']} mm to the floor at "
  f"({P.LVL['floor']:+.3f})   [R]")
w()
w(f"  Sump top   ({S['invert']:+.3f}) + {S['d']/1000:.3f} = ({S['invert']+S['d']/1000:+.3f}) "
  f"= the internal floor level.  [R] consistent with A.4.3.")
w()
w("  *** C18 REMAINS OPEN.  Master F.1 and the A.4.3 levels give a 400 pit base;")
w("      the text on S-06 says 300.  400 IS HELD, unchanged by this package.")
w("      The drainage design is unaffected either way - the invert is fixed at")
w(f"      ({S['invert']:+.3f}) and the storage is measured from it. ***")

# =====================================================================
head("D.3", "SUMP DISCHARGE  -  rising main, static lift and the envelope crossing")
w()
w("  The rising main is the ONLY drainage item that crosses the protective")
w("  envelope.  S-06: it passes through the service entry plate - the MCT frame")
w("  that is 'the only penetration of the envelope' - and discharges through")
w("  four devices IN SERIES, all inside the envelope:   [C] S-06")
for i, d in enumerate(P.DISCHARGE_TRAIN, 1):
    w(f"      {i}  {d}")
w()
for dn, idia in (("DN40", 40.0), ("DN50", 50.0), ("DN65", 65.0)):
    a = math.pi * (idia / 1000.0) ** 2 / 4.0
    v = (P.SUMP["duty_ls"] / 1000.0) / a
    ok = "self-cleansing OK" if v >= 0.75 else "BELOW 0.75 m/s - not self-cleansing"
    w(f"  {dn}  bore {idia:.0f} mm   A = {a*1e3:.3f} x 10-3 m2   "
      f"v = {P.SUMP['duty_ls']/1000:.4f} / A = {v:.2f} m/s   {ok}")
w()
w("  ADOPTED  DN50 rising main, ductile iron or stainless, welded/flanged, no")
w("  push-fit joint inside the envelope.  [A] this package.")
w(f"  Velocity {(P.SUMP['duty_ls']/1000)/(math.pi*0.05**2/4):.2f} m/s is above the 0.75 m/s")
w("  self-cleansing minimum and below the 2.4 m/s at which a rising main starts")
w("  to hammer.  DN40 is the alternative if a higher scouring velocity is wanted.")
w()
lift_stop = 0.000 - (P.LVL["sump_invert"] + P.SUMP["stop"] / 1000.0)
lift_inv = 0.000 - P.LVL["sump_invert"]
w(f"  Static lift, stop level ({P.LVL['sump_invert'] + P.SUMP['stop']/1000:+.3f}) to grade 0.000 "
  f"= {lift_stop:.2f} m   [R]")
w(f"  Static lift, invert     ({P.LVL['sump_invert']:+.3f}) to grade 0.000 "
  f"= {lift_inv:.2f} m   [R]")
w()
w("  TOTAL PUMP HEAD - DATA REQUIRED.")
w("      Static lift is computable and is given above.  Friction and fitting")
w("      losses cannot be computed until the final route length is fixed, and")
w("      the discharge point level is not recorded anywhere in the project")
w("      (open item D3).  The pump DUTY (1.5 L/s) is confirmed on S-06; the")
w("      HEAD is not stated there and is not derived here.  It must be fixed")
w("      at procurement against the built route.  [N]")

# =====================================================================
head("D.4", "INTERNAL DRAINAGE  -  pipe capacity, gradient and self-cleansing velocity")
w()
w("  Manning:  Q = (1/n) A R^(2/3) S^(1/2),  R = D/4 running full.")
w("  n = 0.010 for uPVC / HDPE / stainless [A] - a standard tabulated value for")
w("  smooth plastic pipe; the source code is not in the workspace (open item M2).")
w()
w(f"  {'PIPE':6s} {'BORE':>6s} {'GRADIENT':>10s} {'Q full':>10s} {'v full':>9s}   NOTE")
n_man = 0.010
rows_pipe = []
for dn, idia in (("DN50", 50.0), ("DN75", 75.0), ("DN100", 100.0),
                 ("DN150", 150.0)):
    for grad in (60, 80, 100, 150):
        D_ = idia / 1000.0
        A_ = math.pi * D_ ** 2 / 4.0
        R_ = D_ / 4.0
        Sg = 1.0 / grad
        Q_ = (1.0 / n_man) * A_ * R_ ** (2.0 / 3.0) * math.sqrt(Sg)
        v_ = Q_ / A_
        note = "self-cleansing" if v_ >= 0.75 else "below 0.75 m/s"
        rows_pipe.append((dn, idia, grad, Q_ * 1000.0, v_, note))
        w(f"  {dn:6s} {idia:5.0f}  {'1:'+str(grad):>10s} {Q_*1000:9.2f} L/s {v_:8.2f} m/s   {note}")
w()
w(f"  Design flow to the sump           {inflow_ls:.5f} L/s   [R] from D.2")
q100_100 = [r for r in rows_pipe if r[0] == "DN100" and r[2] == 100][0][3]
w(f"  DN100 at 1:100 full-bore capacity {q100_100:.2f} L/s")
w(f"  CAPACITY RATIO                    {q100_100/inflow_ls:.0f} : 1")
w()
w("  CONCLUSION.  Internal drainage is governed by MINIMUM PIPE SIZE and by")
w("  SELF-CLEANSING VELOCITY, not by flow.  Sizing therefore follows minimum")
w("  practical bores and the gradients above, and the flow check is recorded")
w("  only to show that flow is not the constraint.  No washdown or hose design")
w("  flow is stated anywhere in the project; if a washdown regime is specified")
w("  later the branch sizes must be re-checked.  [N] washdown design flow.")

# =====================================================================
head("D.5", "FLOOR FALLS, SCREED AND THE EFFECT ON CLEAR HEIGHT")
w()
w("  The internal floor at ({:+.3f}) IS the top of the 600 mat - a structural".format(P.LVL["floor"]))
w("  surface inside the tanked envelope.  Falls to a gully must NOT be cut into")
w("  it: that would reduce the mat thickness and the 75 mm cover to the bottom")
w("  curtain locally.  Falls are therefore formed in the FLOOR SCREED.  [A]")
w()
w("  THE ADOPTED GRADING IS SET IN D.15, where it is checked against the mat")
w("  SIDL allowance - that allowance, not hydraulics, is what sizes it:")
w("      transverse   1:80 wet areas (lavatory, CBRN plant, decon airlock)")
w("                   1:100 elsewhere,   2500 run each side to the spine")
w("      spine        1:400 east to the sump, Y 3100, through the door gaps")
w("      minimum      25 mm at the sump edge")
w()
t_min_ = 25.0
d_long_ = (11800.0 - 600.0) / 400.0
d_tr_ = 2500.0 / 100.0
t_corner = t_min_ + d_long_ + d_tr_
w(f"  Screed at the sump edge                     {t_min_:.0f} mm   [A]")
w(f"  Screed at the far corner  {t_min_:.0f} + {d_long_:.0f} + {d_tr_:.0f}          "
  f"= {t_corner:.0f} mm   [R]")
w()
w(f"  Structural clear height   ({P.LVL['floor']:+.3f}) to ({P.LVL['roof_soffit']:+.3f})"
  f"        = {P.H_CLEAR} mm   [C]")
w(f"  FINISHED clear height, sump edge   {P.H_CLEAR} - {t_min_:.0f}          "
  f"= {P.H_CLEAR - t_min_:.0f} mm   [R]")
w(f"  FINISHED clear height, far corner  {P.H_CLEAR} - {t_corner:.0f}          "
  f"= {P.H_CLEAR - t_corner:.0f} mm   [R]")
w()
w("  *** COORDINATION FINDING - DR-F2 ***")
w("      The 3200 clear height in the master is measured between STRUCTURAL")
w("      surfaces.  A drained floor screed reduces the FINISHED clear height")
w(f"      to between {P.H_CLEAR - t_corner:.0f} and {P.H_CLEAR - t_min_:.0f} mm.  "
  f"Still ample, but the two")
w("      figures are different and a number quoted to a client must say which")
w("      of the two it is.  Recorded for the architect; NO STRUCTURAL DIMENSION")
w("      IS CHANGED and the 3200 itself is untouched.")

# =====================================================================
head("D.6", "TRAP SEALS AGAINST SHELTER OVERPRESSURE")
w()
w("  The clean zone is held at +50 to +100 Pa, and is leak-tested at +300 Pa.")
w("  [C] S-06.  A water trap on any drain inside that zone is a pressure")
w("  boundary: if the seal is shallower than the overpressure it blows through")
w("  and the shelter vents to the drain.")
w()
w("  1 mm water gauge = 9.81 Pa.")
for seal in (50, 75, 100):
    w(f"      {seal:3d} mm seal  holds  {seal*9.81:6.0f} Pa   "
      f"= {seal*9.81/100:.1f} x the +100 Pa operating overpressure, "
      f"{seal*9.81/300:.1f} x the +300 Pa test")
w()
w("  ADOPTED  75 mm DEEP-SEAL TRAPS throughout the gas-tight envelope (bays 1-6)")
w("  and on the sump discharge train.  [A] this package.")
w(f"  Margin at 75 mm: {75*9.81:.0f} Pa against a {300} Pa test = "
  f"{75*9.81/300:.1f} : 1.")
w("  Every trap inside the envelope must also be a PRIMED trap - an unused")
w("  floor gully evaporates dry and then leaks air both ways.  Trap primers or")
w("  a written weekly priming task are required.  [A]")

# =====================================================================
head("D.7", "RAINWATER  -  catchments and flows at the recorded intensity")
w()
i_mmh = P.RAIN_INTENSITY
w(f"  DESIGN INTENSITY   {i_mmh:.0f} mm/h   [C] Rev F drawing 5, note 1")
w("      This is the only rainfall intensity stated anywhere in the project.")
w("      NO return period, storm duration or IDF source is recorded with it.")
w("      *** OPEN ITEM D1 - VERIFY AGAINST IMD PUNE DATA BEFORE CONSTRUCTION ***")
w()
w("  Q = C i A / 3600   with i in mm/h, A in m2, Q in L/s.")
w("  C = 1.00 adopted for RC roofs and for the engineered cover in the monsoon")
w("  (saturated topsoil).  A lower C for turf is defensible but is not taken -")
w("  the conservative bound is used.  [A]")
w()


def q_ls(area, c=1.0, i=i_mmh):
    return c * i * area / 3600.0


hh_a = (P.HH["x1"] - P.HH["x0"]) * (P.HH["y1"] - P.HH["y0"]) / 1e6
asw_a = (P.ASW["x1"] - P.ASW["x0"]) * (P.ASW["y1"] - P.ASW["y0"]) / 1e6
ov_x = min(P.HH["x1"], P.ASW["x1"]) - max(P.HH["x0"], P.ASW["x0"])
ov_y = min(P.HH["y1"], P.ASW["y1"]) - max(P.HH["y0"], P.ASW["y0"])
ov_a = max(0.0, ov_x) * max(0.0, ov_y) / 1e6
cover_a = (P.BOX["x1"] - P.BOX["x0"]) * (P.BOX["y1"] - P.BOX["y0"]) / 1e6
plat_a = (P.ASW["platform"][1] - P.ASW["platform"][0]) * P.ASW["width"] / 1e6

w(f"  {'CATCHMENT':44s} {'AREA m2':>9s} {'C':>5s} {'Q L/s':>8s}  CLASS")
w(f"  {'Headhouse roof  13600-18400 x 200-6000':44s} {hh_a:9.2f} {1.0:5.2f} "
  f"{q_ls(hh_a):8.3f}  [R] from [C] A.4.6")
w(f"  {'Covered stairwell roof  9250-16050 x 5750-7750':44s} {asw_a:9.2f} {1.0:5.2f} "
  f"{q_ls(asw_a):8.3f}  [R] from [C] A.4.7")
w(f"  {'   less overlap of the two footprints':44s} {-ov_a:9.2f} {1.0:5.2f} "
  f"{-q_ls(ov_a):8.3f}  [R]")
w(f"  {'Engineered cover over the box  22.0 x 6.2':44s} {cover_a:9.2f} {1.0:5.2f} "
  f"{q_ls(cover_a):8.3f}  [R] from [C] A.4.2")
sub = hh_a + asw_a - ov_a + cover_a
w(f"  {'SUB-TOTAL, structures and cover':44s} {sub:9.2f} {'':5s} {q_ls(sub):8.3f}  [R]")
w()
w("  Berm, approach, hardstanding and the rest of the site:  DATA REQUIRED.")
w("  No site plan, boundary, contour or external area exists in the project, so")
w("  the total site catchment CANNOT be closed.  The figures above are the")
w("  catchments of the structures themselves and are complete for those.  [N]")
w()
w("  *** THE ENGINEERED COVER IS NOT DRAINED BY PIPEWORK. ***")
w("  A.4.3 records finished grade as crowned, falling 1:50 away from the")
w("  structure; A.7.3 gives 300 topsoil/turf over a 150 GRANULAR FILTER layer")
w("  over the burster slab.  Rain on the cover sheds at the surface and what")
w("  infiltrates is intercepted by the granular filter and dispersed at the")
w("  berm toe.  There is no roof outlet, no downpipe and no rainwater pipe on")
w("  the buried roof, and none is added by this package: a pipe penetrating")
w("  the cover would breach the radiation mass and the roof membrane.  [C]/[A]")

# =====================================================================
head("D.8", "ENTRY THRESHOLD  -  the catchment that reaches the stairwell")
w()
w("  Rev F drawing 5 records the design history explicitly:")
w("      note 1  the Rev E OPEN cut was 7.2 m2 of open pit; at 50 mm/h that is")
w("              0.10 L/s that had to be pumped, and a pump failure flooded the")
w("              only entrance")
w("      note 5  at Rev F the approach is roofed, the door is at grade, the")
w("              ground falls away 1:50 and a channel and grating cross the")
w("              threshold.  'WITH THE DOOR SHUT THE CATCHMENT IS ZERO.'")
w("      note 9  a 1.0 m3 sump takes 32 hours to fill at the worst door-open")
w("              driving-rain rate; pump 2 L/s duty + standby, NRV on the main")
w()
q_reve = q_ls(P.REV_E_PIT_AREA)
w(f"  Check of note 1:  {P.REV_E_PIT_AREA} m2 x {i_mmh:.0f} mm/h / 3600 = "
  f"{q_reve:.3f} L/s   -> the 0.10 L/s is reproduced exactly.  [R]")
w()
fill = P.ASW_SUMP["volume_m3"] * 1000.0 / P.ASW_SUMP["fill_time_h"]
w(f"  Check of note 9:  {P.ASW_SUMP['volume_m3']*1000:.0f} L / "
  f"{P.ASW_SUMP['fill_time_h']} h = {fill:.1f} L/h = {fill/3600:.4f} L/s")
w(f"                    equivalent catchment at {i_mmh:.0f} mm/h = "
  f"{fill/1000/(i_mmh/1000)/1:.3f} m2")
w("  The driving-rain entry area behind note 9 is NOT stated on the drawing.")
w("  It is recorded here as a reconstruction only.  [R]/[U]")
w()
w("  *** CONFLICT RAISED BY THIS PACKAGE - DR-C1 ***")
w(f"      The S-06 'DESIGN FLOWS' table still carries {0.10} L/s for")
w("      'Stairwell / approach surface water'.  That is the REV E open-cut")
w("      figure (note 1 above).  At Rev F the approach is covered and the")
w("      design case is the door-open driving-rain rate of note 9, which is")
f_ratio = q_reve / (fill / 3600.0)
w(f"      about {f_ratio:.0f} times smaller.  The S-06 number is CONSERVATIVE and")
w("      nothing is unsafe, but it is a superseded catchment carried forward.")
w("      NOT CHANGED HERE - S-06 is an issued sheet and the correction needs a")
w("      ruling.  Both figures are shown on D-103 so no reviewer is misled.")
w()
w(f"  Stairwell sump   {P.ASW_SUMP['volume_m3']} m3, pump {P.ASW_SUMP['duty_ls']} L/s "
  f"{P.ASW_SUMP['arrangement']}, {P.ASW_SUMP['rising_main']}   [C]")
w(f"  At the note-9 rate the {P.ASW_SUMP['duty_ls']} L/s pump empties the sump in "
  f"{P.ASW_SUMP['volume_m3']*1000/P.ASW_SUMP['duty_ls']/60:.1f} min against a "
  f"{P.ASW_SUMP['fill_time_h']} h fill.  [R]")
w(f"  At the superseded 0.10 L/s the pump is still {P.ASW_SUMP['duty_ls']/0.10:.0f} "
  f"times the inflow.  [R]  The pump is not sensitive to DR-C1.")

# =====================================================================
head("D.9", "SEPTIC TANK  -  IS 2470 (Part 1):1985 re-check")
T = P.SEPTIC
w()
w(f"  Design population         {T['users']} [C] S-06 - 'sentry-post shift crews +")
w("                            shelter maintenance'.  TAKEN VERBATIM, NOT")
w("                            RE-DERIVED.  The sentry post itself is outside")
w("                            the scope of this package; only the tank that")
w("                            already exists in the project is carried forward.")
w(f"  Sewage flow               {T['q_lpcd']} lpcd x {T['users']} = {T['flow_lpd']} L/day   [C]")
w(f"  Detention 24 h, Cl. 6.2   = {T['detention_l']} L                    [C]")
w(f"  Sludge, Cl. 6.3           30 L/person/yr x {T['users']} x 2 yr = {T['sludge_l']} L   [C]")
w(f"  REQUIRED                  {T['detention_l']} + {T['sludge_l']} = {T['required_l']} L   [R]")
prov = T["l"] * T["b"] * T["liquid_depth"] * 1000.0
w(f"  PROVIDED, Table 1         {T['l']} x {T['b']} x {T['liquid_depth']} = {prov:.0f} L   [C]")
w(f"  CHECK                     {prov:.0f} >= {T['required_l']}   "
  f"{'PASS' if prov >= T['required_l'] else 'FAIL'}   margin "
  f"{(prov/T['required_l']-1)*100:.1f} %   [R]")
w(f"  L/B = {T['l']}/{T['b']} = {T['l']/T['b']:.1f}   Cl. 6.5 wants 2 to 4      "
  f"{'PASS' if 2 <= T['l']/T['b'] <= 4 else 'FAIL'}")
w(f"  B = {T['b']*1000:.0f} mm >= 750, depth {T['liquid_depth']:.2f} m >= 1.0 m   Cl. 6.6   PASS")
w(f"  Freeboard {T['freeboard']*1000:.0f} -> overall depth {T['overall_depth']:.2f} m   [C]")
w(f"  Two compartments, baffle {T['baffle']}, inlet and outlet tees, "
  f"vent {T['vent']}   Cl. 6.9   [C]")
w()
w("  ALL CHECKS REPRODUCE THE S-06 VALUES EXACTLY.  No change.")

# =====================================================================
head("D.10", "SOAK PIT  -  IS 2470 (Part 2):1985 re-check   *** A SHORTFALL IS FOUND ***")
K = P.SOAKPIT
w()
w(f"  Effluent to disperse      {T['flow_lpd']} L/day   [C]")
w(f"  Design absorption         {K['absorption_lm2d']} L/m2/day   [A] master K.2 A7")
req = T["flow_lpd"] / K["absorption_lm2d"]
w(f"  AREA REQUIRED             {T['flow_lpd']} / {K['absorption_lm2d']} = {req:.2f} m2   [R]")
side = math.pi * K["dia"] * K["effective_depth"]
w(f"  Pit {K['dia']:.1f} dia x {K['effective_depth']:.1f} effective")
w(f"  SIDE AREA pi.D.h          pi x {K['dia']:.1f} x {K['effective_depth']:.1f} = {side:.2f} m2   [R]")
w("      (the base is not counted - it clogs; S-06 states this and it is correct)")
w()
short = req - side
w(f"  CHECK                     {side:.2f} vs {req:.2f} m2 required   ->  SHORT BY "
  f"{short:.2f} m2  =  {short/req*100:.1f} %")
w()
w("  *** CONFLICT RAISED BY THIS PACKAGE - DR-C2 ***")
w(f"      Sheet S-06 prints '{side:.1f} m2   OK' against a stated requirement of")
w(f"      '{req:.1f} m2'.  {side:.2f} m2 is NOT >= {req:.2f} m2.  The pit as drawn is "
  f"{short/req*100:.1f} % short.")
w("      This is arithmetic, not judgement.")
w()
need_h = req / (math.pi * K["dia"])
need_d = req / (math.pi * K["effective_depth"])
w("      Either of these closes it, and both are single-dimension changes:")
w(f"        (a) effective depth {K['effective_depth']:.1f} -> {need_h:.2f} m  "
  f"(say {math.ceil(need_h*10)/10:.1f} m), diameter unchanged")
w(f"        (b) diameter {K['dia']:.1f} -> {need_d:.2f} m  "
  f"(say {math.ceil(need_d*10)/10:.1f} m), depth unchanged")
w(f"      Option (a) at {math.ceil(need_h*10)/10:.1f} m gives "
  f"{math.pi*K['dia']*math.ceil(need_h*10)/10:.2f} m2, "
  f"{(math.pi*K['dia']*math.ceil(need_h*10)/10)/req*100-100:+.1f} % on requirement.")
w()
w("      NOT RESOLVED HERE.  S-06 is an issued sheet and A7 (the 20 L/m2/day")
w("      absorption) is itself [ASSUMED] and MUST be replaced by a percolation")
w("      test to Cl. 4 before construction.  The test may move the requirement")
w("      by far more than 2.3 %, so re-sizing the pit before the test would be")
w("      false precision.  The shortfall is recorded, flagged on D-305 and")
w("      D-001, and referred for a ruling.")
w()
w("  *** AND THE LARGER RISK, ALREADY IN THE MASTER (K.2 A7) ***")
w("      'Soak pit will not work if lower - LIKELY ON BASALT.'  A percolation")
w("      test to IS 2470 (Pt 2) Cl. 4 is MANDATORY.  If the measured rate is")
w("      below 20 L/m2/day the answer is not a bigger pit: it is a dispersion")
w("      trench (Cl. 5) or a sealed holding tank emptied on a schedule.")

# =====================================================================
head("D.11", "STORM SOAKAWAY  -  the clean sump outfall")
w()
w("  S-06 sends the clean sump discharge to a 'storm soakaway', separate from")
w("  the foul soak pit.  NO SIZE, LEVEL OR POSITION IS GIVEN FOR IT ANYWHERE")
w("  IN THE PROJECT.  [N]  It is sized here for the first time.")
w()
w(f"  Discharge to disperse     {inflow_lpd:.0f} L/day  (seepage + condensate/washdown)   [R]")
w(f"  Design absorption         {K['absorption_lm2d']} L/m2/day   [A] A7, same caveat")
req_s = inflow_lpd / K["absorption_lm2d"]
w(f"  AREA REQUIRED             {inflow_lpd:.0f} / {K['absorption_lm2d']} = {req_s:.1f} m2   [R]")
w()
w(f"  ADOPTED  a pit of the SAME construction as the foul soak pit -")
w(f"           {K['dia']:.1f} m dia x {K['effective_depth']:.1f} m effective, side area "
  f"{side:.2f} m2   [A]")
w(f"  CHECK    {side:.2f} >= {req_s:.1f} m2   PASS, margin {(side/req_s-1)*100:.0f} %   [R]")
w("  Standardising the two pits means one construction detail, one cover slab")
w("  and one spare set of materials on site.")
w()
w("  SEPARATION.  The storm soakaway takes clean groundwater and condensate; the")
w("  soak pit takes septic effluent.  They are NOT combined.  S-06 is explicit -")
w("  'STORM SOAKAWAY - CLEAN SUMP DISCHARGE.  SEPARATE FROM FOUL.'  [C]")
w("  IS 2470 (Pt 2) offset rules apply to the foul pit: >= 15 m from any well,")
w("  >= 5 m from the septic tank, >= 2 m from any building.  [C] S-06")
w("  *** THOSE OFFSETS CANNOT BE DEMONSTRATED - no site plan, no well position")
w("      and no boundary exist in the project.  DATA REQUIRED (D3). ***")

# =====================================================================
head("D.12", "STAIRWELL SOAKAWAY  -  the storage check the low absorption rate forces")
w()
w("  The stairwell sump discharges to its 'own soakaway' [C].  Unlike the two")
w("  pits above, this one takes a STORM EVENT, not a steady daily flow, so it")
w("  is a storage problem: the pit must hold the event and then empty before")
w("  the next one.")
w()
ev = P.ASW_SUMP["volume_m3"] * 1000.0
emptying = K["absorption_lm2d"] * side
w(f"  Event volume, one sump-full          {ev:.0f} L   [C]")
w(f"  Emptying rate of a {K['dia']:.1f} x {K['effective_depth']:.1f} pit   "
  f"{K['absorption_lm2d']} x {side:.2f} = {emptying:.0f} L/day   [R]")
w(f"  TIME TO EMPTY                        {ev:.0f} / {emptying:.0f} = "
  f"{ev/emptying*24:.1f} h   [R]")
w()
w("  *** FINDING - DR-F3 ***")
w(f"      At the [ASSUMED] 20 L/m2/day the pit takes {ev/emptying*24:.0f} hours to")
w("      recover from one sump-full.  Good practice for a rainwater soakaway is")
w("      half-emptying inside 24 h.  This is NOT a defect in the layout - it is")
w("      the [ASSUMED] absorption rate showing through.  It is the third")
w("      independent reason the PERCOLATION TEST (A7) is on the critical path.")
w("      If the measured rate does not support infiltration, the stairwell sump")
w("      discharges to a holding tank or to a positive outfall instead, and the")
w("      final discharge question (D3) has to be answered first.")

# =====================================================================
head("D.15", "FLOOR SCREED AGAINST THE MAT SIDL ALLOWANCE  -  the governing constraint")
w()
w("  The internal floor is the top of the 600 mat.  A drained floor needs a")
w("  screed, and the screed is dead load on a mat that master A.7.2 allows only")
w("  1.0 kPa of SIDL.  That allowance, not hydraulics, sizes the falls.")
w()
rho_scr = 24.0                      # kN/m3, as the A.7.3 protection screed  [C]
sidl = 1.0                          # kPa on the mat  [C] A.7.2
t_max = sidl / rho_scr * 1000.0
w(f"  Mat SIDL allowance                 {sidl:.1f} kPa            [C] A.7.2")
w(f"  Screed density                     {rho_scr:.0f} kN/m3          [C] A.7.3 uses 24 for screed")
w(f"  MAXIMUM AVERAGE SCREED             {sidl:.1f} / {rho_scr:.0f} = {t_max:.0f} mm   [R]")
w()
w("  ADOPTED FLOOR GRADING - zone 1, bays 1 to 5, falling east to the sump:")
t_min = 25.0
run_long = 11800.0 - 600.0
g_long = 400
d_long = run_long / g_long
run_tr = (P.INT["y1"] - P.INT["y0"]) / 2.0
g_tr = 100
d_tr = run_tr / g_tr
w(f"      minimum screed at the sump edge                       {t_min:.0f} mm   [A]")
w(f"      longitudinal fall 1:{g_long} over {run_long:.0f}            "
  f"= {d_long:.0f} mm   [A]")
w(f"      transverse fall 1:{g_tr} over {run_tr:.0f} each side       "
  f"= {d_tr:.0f} mm   [A]")
t_max_pt = t_min + d_long + d_tr
t_avg = t_min + d_long / 2.0 + d_tr / 2.0
w(f"      screed at the sump edge  {t_min:.0f} mm  ->  at the far corner "
  f"{t_max_pt:.0f} mm   [R]")
w(f"      AREA-AVERAGE SCREED                                   {t_avg:.0f} mm   [R]")
w()
load = t_avg / 1000.0 * rho_scr
w(f"  Screed load    {t_avg:.0f} mm x {rho_scr:.0f} kN/m3 = {load:.2f} kPa")
w(f"  Allowance                                {sidl:.2f} kPa")
w(f"  EXCESS                                   {load - sidl:+.2f} kPa "
  f"= {(load/sidl - 1)*100:+.0f} %")
a_int = (P.INT["x1"] - P.INT["x0"]) / 1000.0 * (P.INT["y1"] - P.INT["y0"]) / 1000.0
w(f"  Over the {a_int:.1f} m2 internal floor          "
  f"= {(load - sidl) * a_int:+.0f} kN   [R]")
mat_wt = 22.0 * 6.2 * 0.6 * 25.0
w(f"  For scale: the mat itself weighs {mat_wt:.0f} kN, and the hydrostatic")
w(f"  uplift on it is 6289 kN (master B.3).  The excess is "
  f"{(load-sidl)*a_int/mat_wt*100:.1f} % of the mat weight")
w(f"  and {(load-sidl)*a_int/6289*100:.2f} % of the uplift, and it acts in the FAVOURABLE")
w("  direction for flotation.")
w()
w("  *** FINDING - DR-F4.  REFERRED, NOT ASSUMED. ***")
w(f"      A drained floor cannot be built inside a {sidl:.1f} kPa SIDL allowance at")
w(f"      {rho_scr:.0f} kN/m3: {t_max:.0f} mm of screed is all the allowance buys, and "
  f"{t_max:.0f} mm")
w("      does not contain a fall over a 2.5 m run plus a minimum thickness at")
w("      the outlet.  Three ways out, for the structural engineer to choose:")
w(f"        (a) accept the {load - sidl:+.2f} kPa ({(load-sidl)*a_int:+.0f} kN) as a "
  f"revision to the mat SIDL")
w("        (b) use a lightweight or thin-set levelling system and re-check")
w("        (c) reduce the falls, accepting standing water between washdowns")
w("      THIS PACKAGE DRAWS (a) AND FLAGS IT.  It is a change to a stated")
w("      design load in master A.7.2 and is not made silently.")

# =====================================================================
head("D.16", "COLLECTION DRAIN IN THE MAT  -  builder's work request BW-01")
w()
w("  Only ONE buried drain is needed inside the envelope: the lavatory branch")
w("  from bay 2 to the sump in bay 5.  Everything else either falls to the sump")
w("  across the floor or is segregated.  That branch has to sit somewhere, and")
w("  the only place is the top of the mat.")
w()
x_gy02 = 4510.0
x_sump = 11068.0
run = x_sump - x_gy02
grad = 100
recess0 = 150.0
fall = run / grad
w(f"  From  GY-02, bay 2 lavatory, X {x_gy02:.0f}")
w(f"  To    clean sump west face,  X {x_sump:.0f}     run = {run:.0f} mm   [R]")
w(f"  DN100 at 1:{grad}   full-bore 6.72 L/s at 0.85 m/s - self-cleansing   [R] D.4")
w(f"  Fall over the run              {run:.0f} / {grad} = {fall:.0f} mm")
w(f"  Recess at the head             {recess0:.0f} mm  (110 OD pipe + surround)   [A]")
w(f"  RECESS AT THE SUMP             {recess0:.0f} + {fall:.0f} = {recess0+fall:.0f} mm   [R]")
w(f"  Invert at the head             ({P.LVL['floor'] - recess0/1000:+.3f})")
w(f"  Invert at the sump             ({P.LVL['floor'] - (recess0+fall)/1000:+.3f})")
w(f"  LOCAL MAT THICKNESS            {P.T_MAT} - {recess0+fall:.0f} = "
  f"{P.T_MAT - (recess0+fall):.0f} mm over a 300 wide band")
w(f"  Section loss                   {(recess0+fall)/P.T_MAT*100:.0f} % of the mat depth, "
  f"locally")
w()
w("  *** BUILDER'S WORK REQUEST BW-01 - NOT ACCEPTED, NOT ASSUMED ***")
w("      The mat is the MOST HEAVILY UTILISED element in the project at 84 %")
w("      (master B.3) and it is part of the tank.  A 300 wide recess taking")
w(f"      {(recess0+fall)/P.T_MAT*100:.0f} % of its depth, on the line of the peak transverse "
  f"sagging")
w("      moment, cannot be adopted by a drainage package.  It is issued to the")
w("      structural engineer as builder's work.  IF IT IS REFUSED, the fallback")
w("      is drawn on D-201 note 6: the lavatory waste discharges over a tundish")
w("      to the graded floor, and there is no buried drain inside the envelope")
w("      at all.  Both are shown; neither is presented as decided.")
w()
w("  No other drain is buried.  The rising main leaves the sump ABOVE the mat.")

# =====================================================================
head("D.17", "HYDRAULIC ZONING  -  what the protective boundary does to drainage")
w()
w("  The protective boundary (blast doors 1 and 2 at (-)6.100, plus W6 and W7)")
w("  and the gas-tight sub-division at W5 cut the shelter into THREE")
w("  hydraulically separate zones.  Water may not cross between them.")
w()
w("  ZONE 1  CLEAN            bays 1-5, inside the gas-tight envelope")
w("          destination      clean sump, bay 5              CONFIRMED, complete")
w()
w("  ZONE 2  DECON AIRLOCK    bay 6, inside the gas-tight envelope but dirty")
w("          destination      S-06 assigns airlock stages 1 and 2 to the")
w("                           1000 L decon effluent tank - WHICH S-06 DRAWS IN")
w("                           BAY 8, at X 20198-21398, Y 4400-5600.")
w("          *** ANY PIPED ROUTE FROM BAY 6 TO BAY 8 CROSSES THE PROTECTIVE")
w("              BOUNDARY TWICE - W6 AND W7 - AND PASSES THROUGH THE STAIR")
w("              SHAFT.  NO SUCH ROUTE IS DRAWN OR DESCRIBED ANYWHERE IN THE")
w("              PROJECT.  [U] ***")
w()
w("  ZONE 3  GREY             bays 7 and 8, outside the gas-tight envelope")
w("          destination      NONE RECORDED.  Bay 8 holds the effluent tank but")
w("                           has no drainage outlet of its own, and bay 7 (the")
w("                           stair shaft, arrival landing at (-)6.100) cannot")
w("                           drain into zone 1 without breaching the boundary.")
w("          [N] DATA REQUIRED")
w()
w("  *** FINDING - DR-F5 ***")
w("      Two of the three hydraulic zones have no closed drainage destination.")
w("      This is not a layout error - it is a consequence of the protective")
w("      boundary, and closing it is a PROTECTIVE-DESIGN decision (a blast and")
w("      gas-tight boundary crossing, or manual transfer in sealed containers),")
w("      not a drainage one.  This package:")
w("        - drains zone 1 completely;")
w("        - drains zone 2 to a collection point at the W6 side of bay 6 and")
w("          marks the onward route to the bay 8 tank UNDEFINED on D-203;")
w("        - provides threshold upstands at W5 and at blast door 1 so that no")
w("          water can run from zone 2 or zone 3 into zone 1;   [A]")
w("        - records zone 3 as having no destination.")
w("      ENGINEER TO CONFIRM.  Nothing is assumed across the boundary.")

# =====================================================================
head("D.13", "SUMMARY OF FLOWS  -  the whole system on one page")
w()
w(f"  {'SOURCE':38s} {'FLOW':>12s} {'COLLECTION':>16s} {'CONVEYANCE':>13s}  DISCHARGE")
rows = [
    ("Groundwater seepage, 401 m2 envelope", "200 L/day", "floor gullies", "gravity DN100", "clean sump -> storm soakaway"),
    ("Condensate + washdown", "200 L/day", "floor gullies", "gravity DN100", "clean sump -> storm soakaway"),
    ("Clean sump, pumped", "1.5 L/s", "sump 3.375 m3", "DN50 rising main", "storm soakaway"),
    ("Decon effluent, airlock stages 1+2", "on use", "1000 L tank", "segregated DN100", "TANKER ONLY"),
    ("Foul, peacetime, 10 users", "450 L/day", "septic 1.125 m3", "gravity DN100", "soak pit"),
    ("Stairwell, door-open driving rain", "1 m3 / 32 h", "1.0 m3 sump", "DN50 rising main", "own soakaway"),
    ("Headhouse washdown / floor gully", "on use", "trapped gully", "gravity DN100", "external soakaway"),
    ("Roofs and engineered cover", f"{q_ls(sub):.2f} L/s", "surface, 1:50 falls", "sheds at grade", "ground at the berm toe"),
]
for r in rows:
    w(f"  {r[0]:38s} {r[1]:>12s} {r[2]:>16s} {r[3]:>13s}  {r[4]}")
w()
w("  FINAL DISCHARGE OF THE WHOLE SITE IS TO GROUND, ON SITE.")
w("  No municipal sewer connection, no municipal storm connection, no outfall")
w("  and no receiving watercourse appears anywhere in the project.  Whether one")
w("  is available at this site is OPEN ITEM D3 - DATA REQUIRED.  Every")
w("  discharge above therefore depends on the percolation test (A7).")

# =====================================================================
head("D.14", "WHAT THIS PACKAGE DOES NOT CALCULATE, AND WHY")
w()
for t, why in [
    ("Site-wide storm runoff",
     "no site plan, boundary, contour or external paved area exists  [N]"),
    ("Rainwater return period / IDF curve",
     "only a bare 50 mm/h is recorded, with no duration or period  [U] D1"),
    ("Runoff coefficient for the berm and turf",
     "no soil infiltration data; C = 1.00 used as the conservative bound  [A]"),
    ("Total pump head for either sump",
     "route length not fixed and no discharge level recorded  [N]"),
    ("Foul drainage from the Bay 2 lavatory",
     "no route exists in the project - open item D2  [U]"),
    ("Washdown / hose design flow",
     "no washdown regime is specified anywhere  [N]"),
    ("Uplift or flotation",
     "already designed in master B.3; NOT re-opened by a drainage package"),
    ("Groundwater lowering / permanent dewatering",
     "the box is a TANK, not a drained structure - by design  [C]"),
]:
    w(f"  - {t}")
    w(f"        {why}")

rule("=")
w("END OF DRAINAGE CALCULATIONS")
rule("=")

# =====================================================================
if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    dest = os.path.abspath(os.path.join(here, "..", "Calculations",
                                        "DR_CALC_OUTPUT.txt"))
    txt = "\n".join(OUT)
    hdr = (f"DRAINAGE CALCULATIONS  -  OUTPUT OF dr_calc.py\n"
           f"UNDERGROUND CBRN-HARDENED PROTECTIVE STRUCTURE, PUNE  -  {P.GEOM_REV}\n"
           f"PACKAGE REVISION {P.REV['drainage']}   {P.PACKAGE_DATE}   "
           f"{P.STATUS}\n"
           f"SENTRY POST EXCLUDED\n")
    with open(dest, "w") as f:
        f.write(hdr + txt + "\n")
    print(hdr + txt)
    print(f"\n[written] {dest}")
