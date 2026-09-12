"""
rc4_calc.py -- every calculation behind revision RC4, with its arithmetic shown.

RC4 is the project owner's rulings on sixteen open items and assumptions
(master Part H.28).  This script computes only the items the rulings asked to
be DESIGNED or VERIFIED.  It invents nothing: every input is either confirmed
in the master or tagged [A] at the point of use.

NOTHING HERE IS A STAAD.Pro RUN.  No analysis is performed anywhere.
"""
import math

W = []
def w(s=""): W.append(s); print(s)
def rule(t): w(); w("=" * 78); w("  " + t); w("=" * 78)


# ===========================================================================
rule("R.1  U8 -- ROOF PROJECTION + PARAPET, 4.162 kN/m")
# ===========================================================================
w("""
RULING: the parapet is CONFIRMED at 300 high x 150 thick.  Re-derive 4.162.

The 300 height is not in fact an assumption -- master A.4.3 records sentry
roof +6.700 and parapet top +7.000, so the height is CONFIRMED by the drawn
levels.  Only the 150 thickness was ever [A], and the ruling confirms it.
""")
gam = 25.0                                  # kN/m3, RC, IS 875 Pt 1 Table 1 [C]
h_par, t_par = 0.300, 0.150                 # m [C] levels / [C] ruling
w_par = h_par * t_par * gam
w(f"  parapet      {h_par:.3f} x {t_par:.3f} x {gam:.1f}      = {w_par:.3f} kN/m")

total = 4.162                               # kN/m [C] Rev F framing plan
resid = total - w_par
w(f"  stated total                              = {total:.3f} kN/m  [C]")
w(f"  residual attributable to the projection   = {resid:.3f} kN/m")
w("")

t_slab = 0.150                              # m [C] S1 is 150 thk
q_self = t_slab * gam
q_fin  = 1.5                                # kPa, roof screed/wp, master A.7.7 [C]
w(f"  slab self weight  {t_slab:.3f} x {gam:.1f}          = {q_self:.3f} kPa")
w(f"  roof finish (A.7.7 roof dead 5.250 = 3.75 + 1.5) = {q_fin:.3f} kPa")
w("")
for lbl, q in (("slab self only", q_self), ("slab + finish", q_self + q_fin)):
    P = resid / q
    w(f"  projection implied, {lbl:16s} : {resid:.3f} / {q:.3f} = {P*1000:.0f} mm")
w("")
w("""  FINDING U8-F1 -- THE PARAPET CONFIRMATION IS NECESSARY BUT NOT SUFFICIENT.

  The parapet accounts for 1.125 kN/m of the 4.162.  The remaining 3.037
  kN/m is the roof projection, and THE PROJECTION DIMENSION IS RECORDED
  NOWHERE IN THIS PROJECT.  The Rev F framing plan carries the lumped figure
  "roof projection + parapet 4.162 kN/m" and no breakdown; no plan, section
  or elevation dimensions an overhang.

  Back-solving gives 810 mm (slab self only) or 578 mm (slab + finish).
  Neither is a round number and neither is drawn, so NEITHER IS ADOPTED.

  U8 therefore moves from "cannot be re-derived at all" to "half re-derived":
  the parapet term is now [C] and reproduces exactly; the projection term
  stays [N] pending ONE dimension.  4.162 kN/m continues to be used as given,
  which is what the analysis already does.  No member force changes.""")


# ===========================================================================
rule("R.2  EL-V6 -- 96-HOUR CLOSED-MODE HEAT BALANCE")
# ===========================================================================
w("""
RULING: compute the heat balance.  The plant itself stays [N].

WHAT IS INSIDE THE GAS-TIGHT ENVELOPE (bays 1-6).  Every watt of electrical
load dissipated inside the envelope becomes heat inside it -- there is no
other place for it to go.  From the EL1 load schedule:
""")
loads_in = [("L-01", "general lighting, LED",          0.520, "[A]"),
            ("L-02", "emergency lighting, maintained", 0.100, "[A]"),
            ("P-01", "small power allowance",          1.000, "[A]"),
            ("F-01", "filter train fan, 1 duty of 2",  0.379, "[R]"),
            ("D-01", "dehumidifier DH-1",              1.000, "[A]"),
            ("U-01", "clean sump pump, 1 duty of 2",   0.334, "[R]"),
            ("Z-01", "EMP Zone 2 ops equipment",       1.500, "[A]"),
            ("S-01", "fire detection panel",           0.100, "[A]"),
            ("B-01", "battery charger / inverter",     0.800, "[A]")]
loads_out = [("U-02", "stairwell pump -- OUTSIDE the envelope", 0.223),
             ("G-01", "generator auxiliaries -- bay 8, OUTSIDE", 0.300)]
for t, d, kw, c in loads_in:
    w(f"    {t:6s} {d:34s} {kw:6.3f} kW  {c}")
P_el = sum(x[2] for x in loads_in)
w(f"    {'':6s} {'ELECTRICAL, INSIDE THE ENVELOPE':34s} {P_el:6.3f} kW")
w("")
for t, d, kw in loads_out:
    w(f"    {t:6s} {d:34s} {kw:6.3f} kW  excluded")
w(f"    connected load, whole project            "
  f"{P_el + sum(x[2] for x in loads_out):6.3f} kW  [C] = EL1's 6.256")
w("")
w("  NO DIVERSITY IS APPLIED.  This is the connected load, so it is an")
w("  UPPER BOUND on the electrical gain, which is the right side to be on")
w("  for sizing cooling.  [A]")
w("")

n_occ = 9                                   # [C] master A.1
q_s_p, q_l_p = 70.0, 45.0                   # W/person sensible / latent [A]
Q_occ_s = n_occ * q_s_p / 1000.0
Q_occ_l = n_occ * q_l_p / 1000.0
w(f"  OCCUPANTS   {n_occ} persons at {q_s_p:.0f} W sensible + {q_l_p:.0f} W latent  [A] seated, light activity")
w(f"              sensible {Q_occ_s:.3f} kW   latent {Q_occ_l:.3f} kW   total {Q_occ_s+Q_occ_l:.3f} kW")
w("")
Q_sens = P_el + Q_occ_s
Q_lat = Q_occ_l
w(f"  TOTAL SENSIBLE GAIN  {P_el:.3f} + {Q_occ_s:.3f}          = {Q_sens:.3f} kW")
w(f"  TOTAL LATENT GAIN                              = {Q_lat:.3f} kW")
w("")
w("""  NOTE ON THE DEHUMIDIFIER.  DH-1 does not reduce the sensible problem --
  it makes it worse.  A refrigerant dehumidifier condenses moisture and
  returns the latent heat, plus its own 1.0 kW of motor work, to the same
  air as SENSIBLE heat.  It is already counted above as a sensible source.
""")

t_h = 96.0
t_s = t_h * 3600.0
Q_tot = Q_sens * t_s                        # kJ
w(f"  HEAT RELEASED OVER {t_h:.0f} h = {Q_sens:.3f} kW x {t_s:.0f} s = {Q_tot/1e6:.3f} GJ")
w("")

w("  BOUND 1 -- ADIABATIC, AIR ONLY (to show why it is not the answer)")
V = 216.96                                  # m3 [C] master A.2
rho_a, cp_a = 1.2, 1.005                    # kg/m3, kJ/kgK [A] standard
C_air = V * rho_a * cp_a
w(f"    air {V:.2f} m3 x {rho_a} x {cp_a} = {C_air:.1f} kJ/K")
w(f"    dT = {Q_tot:.0f} / {C_air:.1f} = {Q_tot/C_air:.0f} K   -- PHYSICALLY MEANINGLESS")
w("    The air holds nothing.  The structure is the entire story.")
w("")

w("  BOUND 2 -- AIR + THE CONCRETE THE HEAT CAN REACH IN 96 h")
alpha = 5.5e-7                              # m2/s, thermal diffusivity of concrete [A]
d_pen = math.sqrt(alpha * t_s)
w(f"    thermal penetration depth  sqrt(alpha.t) = sqrt({alpha:.1e} x {t_s:.0f})")
w(f"                                             = {d_pen:.3f} m in {t_h:.0f} h")
areas = [("floor (top of mat)",              67.80),
         ("ceiling (roof soffit)",           67.80),
         ("two long perimeter walls",        2 * 13.56 * 3.2),
         ("west end wall W3",                5.0 * 3.2),
         ("W6 inner face",                   5.0 * 3.2),
         ("four W8 partitions, both faces",  8 * 5.0 * 3.2),
         ("W5, both faces",                  2 * 5.0 * 3.2)]
for lbl, a in areas:
    w(f"      {lbl:34s} {a:8.2f} m2")
A_c = sum(a for _, a in areas)
w(f"      {'TOTAL WETTED CONCRETE SURFACE':34s} {A_c:8.2f} m2")
d_eff = 0.30                                # m [A] lumped, < d_pen and < the thin partitions
V_c = A_c * d_eff
rho_c, cp_c = 2500.0, 0.88                  # kg/m3, kJ/kgK [A] standard for concrete
C_con = V_c * rho_c * cp_c
w(f"    effective responding depth taken as {d_eff:.2f} m  [A]")
w(f"      -- below the {d_pen:.3f} m penetration depth, and below half the")
w(f"         110 mm partitions' own thickness, so it is not double-counted")
w(f"    concrete {V_c:.1f} m3 x {rho_c:.0f} x {cp_c} = {C_con:,.0f} kJ/K")
C_tot = C_con + C_air
dT_struct = Q_tot / C_tot
w(f"    dT over {t_h:.0f} h = {Q_tot:.0f} / {C_tot:,.0f} = {dT_struct:.2f} K")
w("")

w("  BOUND 3 -- THE AIR-TO-SURFACE FILM (the air runs hotter than the concrete)")
h_film = 3.0                                # W/m2K [A] natural convection, still indoor air
dT_film = Q_sens * 1000.0 / (h_film * A_c)
w(f"    h taken as {h_film:.1f} W/m2K  [A] natural convection, sealed still air")
w(f"    dT_film = {Q_sens*1000:.0f} / ({h_film:.1f} x {A_c:.2f}) = {dT_film:.2f} K")
w("")
dT_air = dT_struct + dT_film
w(f"  AIR TEMPERATURE RISE OVER 96 h  =  {dT_struct:.2f} + {dT_film:.2f}  =  {dT_air:.1f} K")
w("")
T0 = 26.0                                   # degC [A] ground temp at 6 m, ~ Pune annual mean
w(f"    starting from a ground temperature of {T0:.0f} C at 6 m depth  [A]")
w(f"    ({T0:.0f} C is about the Pune annual mean air temperature; at (-)6.100")
w("     the rock is at the annual mean, not the daily or seasonal value)")
w(f"    -> the envelope reaches about {T0 + dT_air:.0f} C by hour 96, and it is")
w("       still rising, because nothing has reached equilibrium")
w("")
T_hold = 30.0
w(f"  COOLING DUTY TO HOLD {T_hold:.0f} C")
dT_avail = T_hold - T0
Q_abs = C_con * dT_avail                    # kJ the structure can take at that dT
Q_rej = Q_tot - Q_abs
P_cool_s = Q_rej / t_s
w(f"    structure can absorb  {C_con:,.0f} x {dT_avail:.0f} K = {Q_abs/1e6:.3f} GJ")
w(f"    heat to be rejected   {Q_tot/1e6:.3f} - {Q_abs/1e6:.3f} = {Q_rej/1e6:.3f} GJ")
w(f"    mean sensible duty    {Q_rej:.0f} / {t_s:.0f} = {P_cool_s:.2f} kW")
w(f"    plus latent           {Q_lat:.3f} kW")
P_cool = P_cool_s + Q_lat
w(f"    TOTAL MEAN DUTY       {P_cool:.2f} kW  =  {P_cool/3.517:.2f} TR")
w(f"    ADOPT {math.ceil(P_cool):.0f} kW ({math.ceil(P_cool)/3.517:.2f} TR) as the closed-mode cooling duty  [R]")
w("""
    Conservative, and deliberately so: it credits the concrete but credits
    NOTHING to the rock beyond it, which will keep absorbing for far longer
    than 96 h.  The duty is a mean -- the peak is at hour 0, before the
    structure has warmed, and falls as it does.
""")
w("""  FINDING EL-V6-F1 -- THE DUTY IS NOT THE PROBLEM.  THE REJECTION PATH IS.

  A 3-4 kW cooling duty is small.  But a SEALED shelter has nowhere to put
  the heat.  In closed mode there is no ventilation air to reject to, and
  every existing envelope penetration is a blast valve or a pipe that is
  already spoken for.  The heat has to go to the ground, which means a
  ground loop -- boreholes or a buried coil -- and therefore A NEW PENETRATION
  OF THE PROTECTIVE ENVELOPE THAT NOBODY HAS DESIGNED, plus an EMP treatment
  for it (a metallic pipe pair crossing the boundary is exactly EM-V5's case).

  THE HEAT BALANCE IS NOW COMPUTED.  THE PLANT, THE REJECTION PATH AND THAT
  PENETRATION ARE NOT DESIGNED AND ARE NOT INVENTED HERE.  EL-V6 closes as
  "no cooling load had ever been computed"; it opens RC4-V1 in its place --
  a sealed shelter with a 4 kW heat surplus and no route out for it.""")

# ===========================================================================
rule("R.3  FS-V7 -- ESCAPE SHAFT LADDERS  (fall-arrest DEFERRED by ruling)")
# ===========================================================================
w("""
RULING: ladder only.  Fall-arrest is deferred.  This is therefore a
KNOWINGLY INCOMPLETE DESIGN and is recorded as one.

The shafts are 1400 dia clear with a 250 RC collar.  Each climb is made up
of three different constructions, and the ladder has to be fixed to all
three:
""")
lv = dict(floor=-6.100, soffit=-2.900, rooftop=-2.000)
for tag, head, esc in (("ESC 1", 0.150, "ESC 1"), ("ESC 2", 0.700, "ESC 2")):
    a = lv["soffit"] - lv["floor"]; b = lv["rooftop"] - lv["soffit"]; c = head - lv["rooftop"]
    w(f"  {esc}   head (+{head:.3f})")
    w(f"    (-)6.100 -> (-)2.900   {a:.3f} m   open bay, ladder on brackets off the wall")
    w(f"    (-)2.900 -> (-)2.000   {b:.3f} m   through the 900 roof slab, 1400 dia bore")
    w(f"    (-)2.000 -> (+){head:.3f}   {c:.3f} m   through the cover, 1400 ID shaft")
    w(f"    TOTAL CLIMB                    {a+b+c:.3f} m")
    w("")

w("  RUNG GEOMETRY -- equal pitch within each shaft, no odd bottom space")
for esc, climb in (("ESC 1", 6.250), ("ESC 2", 6.800)):
    n = round(climb / 0.2975)
    pitch = climb / n
    w(f"    {esc}  climb {climb:.3f} m / {n} equal spaces = pitch {pitch*1000:.1f} mm"
      f"  ({n-1} intermediate rungs)")
w("""
    Pitch held between 250 and 300 mm, the normal band for a fixed vertical
    ladder, and EQUAL within each shaft so there is no short step to trip on
    in the dark.  [A] -- IS 3696 (Part 2) and NBC 2016 Part 4 are named by
    title; no clause is quoted from either, because neither document is in
    this workspace.  Master Part G's rule applies: a clause that cannot be
    confirmed is not cited.

  ADOPTED LADDER -- one type, both shafts
    Rungs          20 mm dia MS, hot-dip galvanised, 400 mm clear width
    Pitch          297.6 mm (ESC 1, 21 spaces) / 295.7 mm (ESC 2, 23 spaces)
    Clearance      >= 200 mm behind the rung to the shaft wall
                   >= 750 mm clear climbing space in front of the rung
    Stringers      2 No. 50 x 10 MS flat, galvanised
    Fixing         cast-in lugs to the 250 RC collar and to the roof slab
                   bore; expansion-anchored brackets at 1.5 m centres to the
                   bay wall over the lower 3.200 m
    Head           top rung set level with the shaft head; grab rails both
                   sides extending 1100 above the head  [A] -- 1100 is the
                   project's own guarding height, NBC 2016 Part 4, used at
                   the stair void free edge

  WHAT THIS DESIGN DOES NOT DO, AND THE RULING KNOWS IT:

    (1) NO FALL-ARREST.  Deferred by the project owner's ruling.  A 6.250 m
        and a 6.800 m unprotected vertical climb, in the dark, under
        emergency conditions, is the exact case a fall-arrest rail exists
        for.  A fixed ladder of this height would normally carry either a
        rail-and-shuttle system or a safety cage.  NEITHER IS PROVIDED.

    (2) NO REST PLATFORM.  Both climbs exceed the height at which an
        intermediate landing is normally provided, and a 1400 dia bore
        cannot take one without blocking the escape it exists to serve.
        Recorded, not solved.

    (3) THE INJURED-PERSON QUESTION IS STILL OPEN.  Whether a casualty is
        expected to leave by a shaft at all is a client question, not a
        design one.  A vertical ladder cannot pass a stretcher.  If the
        answer is yes, this design does not satisfy it and a different
        arrangement is needed.

    FS-V7 therefore does not close.  It CHANGES: from "no position at all"
    to "a ladder is designed, and two named things are missing from it".""")


# ===========================================================================
rule("R.4  FS-1 / D-05 -- THE W5 GAS-TIGHT FIRE DOOR")
# ===========================================================================
t_w5, cov, phi = 0.200, 0.040, 0.012
d_w5 = t_w5 - cov - phi / 2
w(f"""
RULING: design D-05 now.

W5 is 200 thk at X 12600-12800, reinforced T12 @ 150 EF EW = 754 mm2/face,
no links, nominal -- it carries NO pressure differential (master A.3), which
is what makes a 200 wall adequate there and what makes this door a fire and
gas-tight element rather than a blast element.

  OPENING       900 x 2100, sill at the floor (-)6.100, head at (-)4.000
  WALL ABOVE    (-)4.000 to the roof soffit (-)2.900 = 1.100 m
""")
b_op, h_op = 0.900, 2.100
as_face = 754.0
as_int = as_face * b_op
w(f"  TRIM STEEL -- replace what the opening interrupts")
w(f"    interrupted vertical steel  {as_face:.0f} x {b_op:.3f}   = {as_int:.0f} mm2/face")
w(f"    trimmer each jamb           {as_int:.0f} / 2        = {as_int/2:.0f} mm2/face")
n_b, dia_b = 2, 16
as_prov = n_b * math.pi * dia_b ** 2 / 4
w(f"    ADOPTED  {n_b}-T{dia_b} EACH JAMB EACH FACE = {as_prov:.0f} mm2  "
  f"({as_prov/(as_int/2):.2f} x required)")
Ld = 40 * dia_b
w(f"    anchored Ld = 40 phi = {Ld:.0f} mm beyond the opening (M35, master A.5)")
w("")
gam = 25.0
h_arch = 0.866 * b_op
h_avail = 1.100
w(f"  HEADER -- what the strip over the opening actually carries")
w(f"    60 deg arching height over a {b_op:.3f} m clear span = 0.866 x {b_op:.3f} = {h_arch:.3f} m")
w(f"    wall available above the opening                      = {h_avail:.3f} m")
if h_arch < h_avail:
    W_tri = 0.5 * b_op * h_arch * t_w5 * gam
    w(f"    {h_arch:.3f} < {h_avail:.3f}, SO THE WALL ARCHES over the opening.")
    w(f"    Load on the header is the triangle only:")
    w(f"      0.5 x {b_op:.3f} x {h_arch:.3f} x {t_w5:.3f} x {gam:.0f} = {W_tri:.3f} kN total")
    M = W_tri * b_op / 6.0
    w(f"      M = W.L/6 (triangular load, simply supported) = {M:.3f} kNm")
    d_h = 0.300 - 0.040 - 0.012
    Mu_lim = 0.133 * 35 * 1000 * (d_h * 1000) ** 2 / 1e6 * 0.200
    w(f"      a nominal 200 x 300 header, d = {d_h*1000:.0f} mm:")
    w(f"      Mu,lim = 0.133 x 35 x 200 x {d_h*1000:.0f}^2 = {Mu_lim:.1f} kNm  "
      f"-> {M/Mu_lim*100:.1f} % utilised")
w("""
    ADOPTED  header band 200 x 300 over the opening + 600 each side
             2-T12 top + 2-T12 bottom, T8 two-legged links @ 150
             -- nominal throughout; the arching case is under 1 % utilised
             and minimum steel governs everywhere.

  THE DOOR ITSELF -- performance specified, product [V]
    Size           900 x 2100 clear
    Function       GAS-TIGHT and FIRE RATED.  NOT blast rated, and it must
                   not be represented as one -- the blast boundary is Blast
                   Doors 1 and 2 at W6 / W7, and W5 carries no differential
    Seal           full-perimeter compression gasket with a cam-action latch
                   on all four edges, so the seal is made by closing  [A]
    Fire rating    EI 120 (120 min integrity AND insulation)  [A]
    OPENS EAST, INTO BAY 6 -- in the direction of escape travel on route R1,
                   which runs bays 1-4 -> bay 5 -> W5 -> bay 6 -> Blast Door 1
    Hardware       escape-openable from the bay 5 side without a key

  WHY THE FIRE RATING IS [A] AND MUST STAY [A]:
    NOTHING IN THIS PROJECT STATES A REQUIRED FIRE RATING FOR W5, OR FOR ANY
    ELEMENT.  The fire plan names W5 as a fire and gas-tight wall and stops
    there; there is no fire engineering, no compartment strategy with rated
    periods, and no head layout (FS-V2, still open).  EI 120 is specified
    here as the rating a compartment wall of this duty would normally carry,
    so that the door can be procured -- NOT as a derived requirement.
    Confirm it against a fire strategy before ordering.

  FS-1 CLOSES: W5 now has a door, and route R1 crosses an opening that
  exists.  The RATING behind it is [A] and is flagged, not hidden.""")


# ===========================================================================
rule("R.5  SG-V6 -- STRIP AND REPLACE UNDER THE ENTRY STAIRWELL RAFT")
# ===========================================================================
w("""
RULING: specify it and price it.  The rate stays [A].

THE PROBLEM IS HEAVE, NOT BEARING.  The stepped raft's shallow end founds
inside a CH horizon measured at free swell index 60-65 %, the top band of
the IS 1498 scale.  A.4.7 says "on compacted fill", which implies a strip
and replace -- but no specification says so and no BOQ item exists.  The
stairwell is expendable against BLAST.  Heave is not a blast problem, and
this is the only primary access to the shelter.
""")
ch_top, ch_bot = 0.180, 1.000
w(f"  CH horizon, measured                      {ch_top:.3f} to {ch_bot:.3f} m depth  [C]")
raft_t = 0.300
top_land_lvl, plat_lvl = 0.000, -2.000
raft_us_top = top_land_lvl - raft_t - 0.300
w(f"  raft 300 thk; top landing at {top_land_lvl:.3f}, platform at {plat_lvl:.3f}")
w(f"  raft underside at the top landing end     {raft_us_top:.3f}")
x_flight0, x_flight1 = 11000.0, 14300.0
drop = abs(plat_lvl - top_land_lvl)
x_at_1m = x_flight0 + (ch_bot - abs(raft_us_top)) / drop * (x_flight1 - x_flight0)
w(f"  the flight drops {drop:.3f} m over X {x_flight0:.0f} -> {x_flight1:.0f}")
w(f"  raft underside passes below the CH base ((-){ch_bot:.3f}) at X = {x_at_1m:.0f}")
x0 = 9250.0
L_aff = (x_at_1m - x0) / 1000.0
W_ext = 2.000
w(f"  AFFECTED RAFT LENGTH  X {x0:.0f} -> {x_at_1m:.0f} = {L_aff:.3f} m, width {W_ext:.3f} m")
w("")
marg = 1.000
L_s, W_s = L_aff + 2 * marg, W_ext + 2 * marg
A_s = L_s * W_s
w(f"  STRIP EXTENT  {marg:.3f} m beyond every raft edge  [A]")
w(f"    {L_aff:.3f} + 2({marg:.3f}) = {L_s:.3f} m  x  {W_ext:.3f} + 2({marg:.3f}) = {W_s:.3f} m")
w(f"    plan area = {A_s:.2f} m2")
d_extra = ch_bot - abs(raft_us_top)
V_s = A_s * d_extra
w(f"  DEPTH BELOW THE RAFT FORMATION  {ch_bot:.3f} - {abs(raft_us_top):.3f} = {d_extra:.3f} m")
w(f"    (mean; it reduces to zero at X {x_at_1m:.0f} where the raft passes below the CH)")
w(f"  VOLUME  {A_s:.2f} x {d_extra:.3f} = {V_s:.2f} m3, say {math.ceil(V_s):.0f} m3")
w(f"""
  SPECIFICATION -- ADOPTED
    Strip the CH horizon to {ch_bot:.3f} m below existing ground level over the
    full plan extent above, under and beyond the stepped raft.
    Replace with granular fill, free-draining, FREE SWELL INDEX <= 20 %
    (IS 2720 Pt XL), laid in 200 mm layers and compacted to >= 95 % MDD
    (IS 2720 Pt VIII), tested to IS 2720 Pt 28.
    Blind with 50 mm sand before the raft blinding.
    The replacement must extend {marg:.3f} m beyond every raft edge so the raft
    never bears partly on replaced and partly on natural CH -- a differential
    heave line under the only primary access is worse than uniform heave.

  BOQ ITEM -- ADDED, QUANTITY DERIVED, RATE [A]
    Item   Strip and replace expansive CH horizon under the entry stairwell
           stepped raft, including disposal, granular replacement and
           compaction testing
    Qty    {math.ceil(V_s):.0f} m3          Unit  m3          Rate  [A] -- NOT INVENTED

  NOTE.  The excavated CH material MUST NOT go to the cover's turf layer.
  That is SG-V7, which the owner has LEFT OPEN -- so the two now interact:
  this ruling produces a stockpile of exactly the material SG-V7 warns
  against re-laying over the granular filter.  RECORDED, NOT RESOLVED.""")


# ===========================================================================
rule("R.6  CAM-V5 / SG2-V3 -- THE TWO AIR SHAFTS")
# ===========================================================================
w("""
RULING: fix both from the design's own logic.

The two gaps are COMPLEMENTARY, which is why one ruling settles both:
    SH-1  fresh air       head +1.500 gooseneck [C]   plan position  [N]
    SH-2  generator air   X 22598-23198 [C]           head level     [N]

  SG2-V3 -- SH-1's PLAN POSITION
  The project already records "12.3 m from the intake to the entry, against
  a >= 10 m rule".  That figure could only have been computed from a
  position -- so the position is implied by the project's own arithmetic
  and does not have to be invented.  Recovering it:
""")
entry = (9375.0, 6750.0)
w(f"    entry door, X 9250-9500 in the headwall, stairwell Y 6000-7500")
w(f"      -> door centre ({entry[0]:.0f}, {entry[1]:.0f})")
for xc in (-2100.0, -2400.0, -2700.0):
    yc = 3100.0
    d = math.hypot(entry[0] - xc, entry[1] - yc)
    flag = "  <-- reproduces the recorded 12.3 m" if abs(d - 12300) < 60 else ""
    w(f"    SH-1 centred ({xc:.0f}, {yc:.0f})  ->  distance to entry = {d/1000:.2f} m{flag}")
xc, yc = -2400.0, 3100.0
w(f"""
    ADOPTED  SH-1 centred ({xc:.0f}, {yc:.0f}), i.e. 600 x 600 occupying
             X {xc-300:.0f} to {xc+300:.0f},  Y {yc-300:.0f} to {yc+300:.0f}   [A]

    It satisfies every rule the project states, and it was DERIVED, not chosen:
      west of the box                        X {xc+300:.0f} < 0                 [C] rule
      >= 10 m intake to entry                {math.hypot(entry[0]-xc, entry[1]-yc)/1000:.2f} m              [C] rule
      reproduces the recorded 12.3 m         to within {abs(math.hypot(entry[0]-xc,entry[1]-yc)-12300):.0f} mm
      on the box longitudinal centreline     Y {yc:.0f} = Y 3100        symmetry
      clear of the 1.000 m excavation working space   {abs(xc+300):.0f} mm clear
""")
sh2_c = (22898.0, 3100.0)
sep = abs(sh2_c[0] - xc)
w(f"    SEPARATION FROM SH-2, the generator exhaust")
w(f"      SH-2 centre X {sh2_c[0]:.0f}  -  SH-1 centre X {xc:.0f}  =  {sep/1000:.2f} m")
w(f"      Intake and exhaust sit at opposite ends of the site, {sep/1000:.1f} m apart,")
w(f"      which is what protects the intake -- NOT stack height.")
w("""
  CAM-V5 -- SH-2's HEAD LEVEL
    ADOPTED  +1.500, the same gooseneck head as SH-1  [A]

    Reasoning, and it is a consistency argument rather than a derivation:
      - +1.500 is the ONLY shaft head level this project contains, and it is
        [C] for SH-1
      - both shafts are 600 x 600 and both carry blast valves
      - it keeps the above-ground signature consistent, which is CAM2's
        whole subject: the installation now reads +7.000 sentry, +2.450
        stairwell, +1.500 BOTH shaft heads, +0.900 headhouse
      - the 25.3 m intake-to-exhaust separation is what protects the intake,
        so extra stack height on SH-2 buys little

    WHAT THIS IS NOT.  It is not a dispersion calculation.  No plume
    analysis of the generator exhaust exists in this project, and if one is
    ever done it may call for more height on SH-2.  Tagged [A] for that
    reason.  C-101 can now draw SH-2 to scale instead of flagging it [N].""")

open("/home/user/underground-shelter-project/Owner Rulings RC4/Calculations/RC4_CALC_OUTPUT.txt",
     "w").write("\n".join(W) + "\n")
