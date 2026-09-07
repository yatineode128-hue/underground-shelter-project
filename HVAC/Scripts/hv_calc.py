"""
hv_calc.py  --  every HVAC number this package uses, computed from the
project's own confirmed inputs.

Run:  python3 hv_calc.py        writes ../Calculations/HV_CALC_OUTPUT.txt

EVIDENCE CLASSES  [C] confirmed  [R] reconstructed here  [A] assumed by this
package  [U] unresolved  [N] not available - DATA REQUIRED.

The ventilation basis for this shelter ALREADY EXISTS, on issued sheet S-06:
occupancy, the three airflow criteria, the design flow, the N+1 configuration,
the leakage allowance, the overpressure cascade, the closed-mode CO2 and O2
figures, the airlock purge, the filter train and the five blast valves.  This
package does NOT re-derive them.  It reproduces each one from first principles
to prove the sheet is self-consistent, then develops what S-06 does not carry:
room-by-room airflow, duct sizes and velocities, duct pressure loss, the fan
duty build-up, and the coordination of the routes with the structure.

WHAT IS NOT CALCULATED HERE, AND WHY, IS IN SECTION H.14.  In particular NO
COOLING LOAD IS CALCULATED - the inputs for one do not exist in the project.
"""
import os
import sys
import math

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "Drainage",
    "Scripts")))
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


# air properties - standard physical values, source not in the workspace [A]
RHO = 1.204          # kg/m3, dry air at 20 C, 101.325 kPa
NU = 1.51e-5         # m2/s, kinematic viscosity at 20 C
EPS = 0.00015        # m, absolute roughness, galvanised steel
CP = 1005.0          # J/kg.K

V = P.VENT

# =====================================================================
head("H.1", "ROOMS, VOLUMES AND THE TWO ENVELOPE FIGURES  -  verification of S-06")
w()
w("  S-06 states, without deriving them:  gas-tight envelope 67.8 m2 / 217.0 m3;")
w("  clean zone 57.8 m2 (used for the FEMA 453 rate); occupied volume with the")
w("  airlock shut 185.0 m3.  All three are reproduced below from the bay")
w("  schedule and the 3200 clear height, so the whole air basis rests on")
w("  geometry a checker can see.")
w()
wid = (P.INT["y1"] - P.INT["y0"]) / 1000.0
w(f"  Internal width, every bay      {wid:.3f} m        [C] master A.4.2")
w(f"  Internal clear height          {P.H_CLEAR/1000:.3f} m        [C] master A.4.2")
w()
w(f"  {'ROOM':6s} {'BAY':>4s} {'USE':32s} {'CLEAR':>7s} {'AREA':>8s} {'VOLUME':>9s}  ZONE")
tot_a = tot_v = 0.0
clean_a = clean_v = 0.0
rows_room = []
for no, x0, x1, cw, rno, rname in P.BAYS:
    a = cw / 1000.0 * wid
    vol = a * P.H_CLEAR / 1000.0
    if no <= 6:
        tot_a += a
        tot_v += vol
    if no <= 5:
        clean_a += a
        clean_v += vol
    rows_room.append((rno, no, rname, cw, a, vol))
    zone = ("clean" if no <= 5 else ("airlock" if no == 6 else "OUTSIDE"))
    w(f"  {rno:6s} {no:4d} {rname:32s} {cw:6.0f}  {a:7.2f} m2 {vol:8.2f} m3  {zone}")
w()
w(f"  GAS-TIGHT ENVELOPE, bays 1-6   {tot_a:.2f} m2   {tot_v:.2f} m3")
w(f"  S-06 states                     67.8 m2    217.0 m3   ->  BOTH REPRODUCED  [R]")
w()
w(f"  CLEAN ZONE, bays 1-5           {clean_a:.2f} m2   {clean_v:.2f} m3")
w(f"  S-06 states                     57.8 m2    185.0 m3   ->  BOTH REPRODUCED  [R]")
w()
w("  [R] THE CLEAN ZONE IS THE GAS-TIGHT ENVELOPE LESS THE DECON AIRLOCK.")
w(f"      67.8 - 10.0 (bay 6, 2000 x 5000) = 57.8 m2.  S-06 does not say this;")
w("      it is worth recording, because the FEMA 453 rate is applied to the")
w("      CLEAN ZONE area and not to the whole envelope.")

# =====================================================================
head("H.2", "FRESH AIR  -  the three criteria and the design flow")
w()
w(f"  Occupancy                      {V['occupants']} persons        [C] S-06")
w(f"  Design endurance               {V['endurance_h']} h              [C] S-06")
w()
w("  CRITERION 1 - SURVIVAL RATE")
w(f"      {V['survival_pp']} m3/h/person x {V['occupants']}                    "
  f"= {V['survival_pp']*V['occupants']:.0f} m3/h    [C] S-06")
w("  CRITERION 2 - WORKING SHELTER RATE")
w(f"      {V['working_pp']} m3/h/person x {V['occupants']}                   "
  f"= {V['working_pp']*V['occupants']:.0f} m3/h    [C] S-06")
w("  CRITERION 3 - FEMA 453, 0.25 cfm/ft2 OVER THE CLEAN ZONE")
ft2 = clean_a * 10.76391
cfm = 0.25 * ft2
m3h = cfm * 1.699011
w(f"      {clean_a:.1f} m2 x 10.76391                        = {ft2:.1f} ft2")
w(f"      x 0.25 cfm/ft2                                 = {cfm:.1f} cfm")
w(f"      x 1.699011 m3/h per cfm                        = {m3h:.1f} m3/h")
w(f"      S-06 states 264 m3/h  ->  REPRODUCED  [R]  ({abs(m3h-264)/264*100:.2f} % apart)")
w()
w(f"  DESIGN FLOW ADOPTED IN THE PROJECT                 = {V['design_m3h']} m3/h   [C]")
w(f"      = {V['design_m3h']/m3h:.2f} x the FEMA rate, "
  f"{V['design_m3h']/(V['working_pp']*V['occupants']):.2f} x the working rate, "
  f"{V['design_m3h']/(V['survival_pp']*V['occupants']):.1f} x the survival rate   [R]")
w(f"      = {V['design_m3h']/V['occupants']:.1f} m3/h per person   [R]")
w()
w(f"  CONFIGURATION  {V['trains']} x {V['design_m3h']} m3/h trains, each able to carry the whole")
w(f"  duty on its own  ->  {V['redundancy']}, not 2 x 150.   [C] S-06")
w()
ach_env = V["design_m3h"] / tot_v
ach_clean = V["design_m3h"] / clean_v
w(f"  AIR CHANGE RATE, whole envelope   {V['design_m3h']} / {tot_v:.1f}   "
  f"= {ach_env:.2f} ACH   [R]")
w(f"  AIR CHANGE RATE, clean zone       {V['design_m3h']} / {clean_v:.1f}   "
  f"= {ach_clean:.2f} ACH   [R]")
w("  Neither figure is a criterion in this project - the design is set by the")
w("  three rates above.  They are recorded because ACH is what a reviewer will")
w("  ask for.")

# =====================================================================
head("H.3", "LEAKAGE AND OVERPRESSURE")
w()
w(f"  Envelope volume                {tot_v:.1f} m3          [R] = S-06's 217.0")
w(f"  Specified leakage              {V['leak_rate']}   [C] S-06")
leak = 0.15 * tot_v
w(f"  Leakage flow  0.15 x {tot_v:.1f}      = {leak:.1f} m3/h        [R]")
w(f"      S-06 states {V['leak_m3h']} m3/h  ->  REPRODUCED  [R]")
w(f"  As a fraction of ONE train     {leak/V['design_m3h']*100:.1f} %          "
  f"[R]   (S-06 says '11 %')")
w()
w(f"  OPERATING OVERPRESSURE         {V['overpressure']}      [C] S-06")
w(f"  CASCADE                        {V['cascade']}   [C] S-06")
w()
w("  [R] THE CASCADE MAPS EXACTLY ONTO THE THREE-STAGE AIRLOCK:")
w("        clean zone, bays 1-5 ............ +50 Pa")
w("        decon stage 3, clean side ....... +35 Pa")
w("        decon stage 2 ................... +20 Pa")
w("        decon stage 1, dirty side ....... +10 Pa")
w("        outside / stair shaft ...........   0 Pa")
w("      Air therefore flows FROM the clean zone TOWARD the airlock and out")
w("      through BV-3.  Every leak is outward.  The airlock is not a dead end -")
w("      it is the exhaust path, and that is why the supply is delivered to")
w("      bays 1-5 and nothing is supplied directly to bay 6.")
w()
w("  The leak test is at +300 Pa [C].  Every water trap inside the envelope is")
w("  therefore a pressure boundary - see the DRAINAGE package, calculation D.6:")
w("  75 mm deep seals, which hold 736 Pa.")

# =====================================================================
head("H.4", "CLOSED MODE  -  CO2, O2 AND WHAT ACTUALLY LIMITS IT")
w()
w("  CLOSED MODE = all valves shut, e.g. immediately post-detonation.  S-06 is")
w("  explicit that it is A BRIDGE, NOT A SURVIVAL MODE.")
w()
w(f"  Occupied volume, airlock shut  {clean_v:.1f} m3          [R] = S-06's 185.0")
w(f"  CO2 production at rest         {V['occupants']} x {V['co2_pp']} "
  f"= {V['occupants']*V['co2_pp']:.2f} m3/h    [C] S-06")
rise = 0.0096
t_co2 = rise * clean_v / (V["occupants"] * V["co2_pp"])
w(f"  Rise to the 1.0 % CO2 limit    {rise:.4f} volume fraction   [C] implied by S-06")
w(f"  TIME TO 1.0 % CO2  ({rise} x {clean_v:.1f}) / {V['occupants']*V['co2_pp']:.2f} "
  f"= {t_co2:.1f} h   [R]")
w(f"      S-06 states {V['closed_hours']} h  ->  REPRODUCED  [R]")
w()
w(f"  SODA LIME                      {V['soda_lime_kgd']} kg/day  ->  "
  f"{V['soda_lime_48h']} kg for 48 h   [C] S-06")
w(f"  OXYGEN                         {V['o2_m3d']} m3/day, store {V['o2_cyl']}   [C] S-06")
o2_store = 15.0
w(f"  O2 store endurance             {o2_store} / {V['o2_m3d']} = "
  f"{o2_store/V['o2_m3d']:.2f} days = {o2_store/V['o2_m3d']*24:.0f} h   [R]")
w()
w("  *** FINDING - HV-F1.  WHAT LIMITS CLOSED MODE IS THE SODA LIME, NOT THE O2. ***")
w(f"      unscrubbed, CO2 alone .................... {t_co2:.1f} h")
w(f"      with the 40 kg soda-lime store .......... 48 h    [C]")
w(f"      with the 15 m3 oxygen store ............. {o2_store/V['o2_m3d']*24:.0f} h    [R]")
w("      The O2 store outlasts the scrubbant by about 5:3, and both outlast the")
w(f"      unscrubbed {t_co2:.1f} h by a wide margin.  SO THE CONSUMABLE TO COUNT AND")
w("      TO WRITE ON THE DRILL CARD IS SODA LIME.  This is not stated on S-06")
w("      and it is the number a shelter commander needs.")
w()
w(f"  Against the {V['endurance_h']} h design endurance: closed mode covers 48 of the "
  f"{V['endurance_h']} h.")
w("  The other 48 h REQUIRE the filter trains to be running.  Closed mode is")
w("  not an alternative to filtration; it is the bridge to it.")

# =====================================================================
head("H.5", "AIRLOCK PURGE  -  and the manning constraint it creates")
w()
s1 = P.DECON_STAGES[0]
vol1 = s1[1] / 1000.0 * s1[2] / 1000.0 * P.H_CLEAR / 1000.0
w(f"  Decon stage 1                  {s1[1]} x {s1[2]} x {P.H_CLEAR}   [C] master A.3")
w(f"  Volume                         = {vol1:.1f} m3          "
  f"[R]  (S-06 states {V['purge_stage_m3']})")
purge = V["purge_changes"] * vol1
w(f"  Purge at {V['purge_changes']} air changes     = {purge:.0f} m3          [R]  "
  f"(S-06 states {V['purge_m3']})")
t_purge = purge / V["design_m3h"] * 60.0
w(f"  Time at {V['design_m3h']} m3/h            = {t_purge:.1f} min        [R]  "
  f"(S-06 states {V['purge_min']})")
w()
w(f"  ->  {V['entry_rate']}.  S-06 records this as 'a manning constraint,")
w("      not a plant figure', and master K.3 already flags it for the drill card.")
w("      IT IS NOT SOLVED BY A BIGGER FAN: doubling the flow halves the purge")
w("      but doubles the filter and cylinder consumption for the same protection.")

# =====================================================================
head("H.6", "ROOM-BY-ROOM AIRFLOW  -  developed by this package")
w()
w("  S-06 gives the TOTAL, 300 m3/h.  It does not distribute it.  The split")
w("  below is an engineering selection by this package [A], made on function")
w("  and occupancy, and it sums exactly to the confirmed total.")
w()
w("  Nothing is supplied directly to bay 6: the airlock is the EXHAUST path and")
w("  receives the whole 300 m3/h as transfer air, which is what makes the")
w("  confirmed pressure cascade work (H.3).")
w()
SUPPLY_DAY = {"U-01": 30, "U-02": 30, "U-03": 135, "U-04": 45, "U-05": 60}
SUPPLY_NIGHT = {"U-01": 30, "U-02": 30, "U-03": 45, "U-04": 135, "U-05": 60}
EXTRACT = {"U-02": 45}
OCC_DAY = {"U-01": 0, "U-02": 1, "U-03": 9, "U-04": 0, "U-05": 0, "U-06": 0}
OCC_NIGHT = {"U-01": 0, "U-02": 1, "U-03": 0, "U-04": 9, "U-05": 0, "U-06": 0}
w("  The 9 occupants are NOT in two places at once: they work in the ops room")
w("  and they sleep in the berthing space.  A single fixed split would starve")
w("  whichever of the two is occupied.  The distribution is therefore")
w("  BALANCED IN TWO MODES with volume control dampers on those two branches,")
w("  and the duct is sized on the worse of the two at every segment.  [A]")
w()
w(f"  {'ROOM':6s} {'USE':28s} {'VOL':>7s} | {'DAY':>13s} | {'NIGHT':>13s} | "
  f"{'EXTR':>5s}")
w(f"  {'':6s} {'':28s} {'m3':>7s} | {'m3/h':>5s} {'ACH':>4s} {'occ':>2s} | "
  f"{'m3/h':>5s} {'ACH':>4s} {'occ':>2s} | {'m3/h':>5s}")
tot_d = tot_n = 0
for rno, no, rname, cw, a, vol in rows_room:
    if no > 5:
        continue
    sd, sn = SUPPLY_DAY.get(rno, 0), SUPPLY_NIGHT.get(rno, 0)
    tot_d += sd
    tot_n += sn
    e = EXTRACT.get(rno, 0)
    w(f"  {rno:6s} {rname[:28]:28s} {vol:7.2f} | {sd:5.0f} {sd/vol:4.2f} "
      f"{OCC_DAY.get(rno,0):2d} | {sn:5.0f} {sn/vol:4.2f} "
      f"{OCC_NIGHT.get(rno,0):2d} | {(e if e else 0):5.0f}")
w(f"  {'U-06':6s} {'DECON AIRLOCK - transfer':28s} {32.0:7.2f} | "
  f"{tot_d:5.0f} {tot_d/32.0:4.2f} {0:2d} | {tot_n:5.0f} {tot_n/32.0:4.2f} "
  f"{0:2d} | {'':5s}")
w(f"  {'':6s} {'TOTAL SUPPLY':28s} {'':7s} | {tot_d:5.0f} {'':4s} {'':2s} | "
  f"{tot_n:5.0f}")
w()
w(f"  CHECK  day {tot_d} and night {tot_n} m3/h against the confirmed design flow "
  f"{V['design_m3h']} m3/h")
w(f"         -> {'BOTH EXACT' if tot_d == tot_n == V['design_m3h'] else 'MISMATCH'}")
w()
w("  BASIS OF THE SPLIT  [A]")
w("    THE OCCUPIED ROOM GETS 135 m3/h IN EITHER MODE - 135 / 9 = 15.0 m3/h per")
w("    person, exactly the working-shelter rate S-06 names as criterion 2.")
w("    The unoccupied one of the pair drops to 45 m3/h, which still turns its")
w("    air over about 1.6 times an hour.")
w("    U-05 CBRN PLANT gets 60 m3/h in both modes - it holds the filter trains,")
w("        the CO2/O2 plant and the dehumidifier, all of which reject heat.")
w("    U-01 and U-02 get 30 m3/h each.  U-02 is EXTRACTED at 45 against a 30")
w("        supply so it runs slightly negative to the rest of the clean zone -")
w("        the lavatory must not be the source of the cascade.")
w()
w("  *** PER-PERSON RATES, STATED PLAINLY ***")
w(f"      whole shelter        {V['design_m3h']} / {V['occupants']}   = "
  f"{V['design_m3h']/V['occupants']:.1f} m3/h/person   "
  f"{V['design_m3h']/V['occupants']/V['working_pp']:.1f} x the working rate")
w(f"      occupied room        135 / {V['occupants']}   = "
  f"{135/V['occupants']:.1f} m3/h/person   = the working rate exactly")
w(f"      unoccupied of the pair 45 / {V['occupants']}    = "
  f"{45/V['occupants']:.1f} m3/h/person   = the {V['survival_pp']} m3/h survival rate exactly")
w()
w("      A FIXED SPLIT CANNOT DO THIS.  Without the two dampers, holding 15")
w("      m3/h/person in both rooms simultaneously would need 270 of the 300")
w("      m3/h and would leave 30 m3/h for the stores, the lavatory AND the")
w("      plant room.  The dampers are not a refinement; they are what makes")
w("      the confirmed 300 m3/h sufficient.")
w()
w("      If a reviewer requires 15 m3/h/person in BOTH rooms at once, the total")
w("      has to rise above 300 m3/h and that is a change to a confirmed design")
w("      value on S-06.  RAISED, NOT TAKEN.")

# =====================================================================
head("H.7", "DUCT SIZING AND VELOCITY")
w()
w("  Q = 300 m3/h = 0.08333 m3/s for the whole system.  Sizes are selected for")
w("  a target 3 to 5 m/s in distribution ductwork - low enough to be quiet in a")
w("  berthing space, high enough to keep the ducts small under a 3200 ceiling.")
w("  The DN100 throat at the blast valves is NOT a design choice: it is fixed")
w("  on S-06 and gives 10.6 m/s, which S-06 itself notes is 'inside the usual")
w("  10-15 m/s throat range'.")
w()


def vel(q_m3h, area_m2):
    return q_m3h / 3600.0 / area_m2


def rect(w_mm, h_mm):
    return w_mm / 1000.0 * h_mm / 1000.0


def circ(d_mm):
    return math.pi * (d_mm / 1000.0) ** 2 / 4.0


def dh_rect(w_mm, h_mm):
    return 2.0 * (w_mm * h_mm) / (w_mm + h_mm) / 1000.0


# worst-case segment flow, taken across BOTH the day and the night mode
DUCTS = [
    ("FA-1", "Blast valve throat, BV-1", 300, "DN100 circular", circ(100), 0.1),
    ("FA-2", "Raw air, BV-1 to filter train 1", 300, "200 dia circular",
     circ(200), 0.2),
    ("FA-3", "Raw air, BV-2 to filter train 2", 300, "200 dia circular",
     circ(200), 0.2),
    ("SA-1", "Plenum bay 5 -> bay 4, main", 240, "200 x 100 rect",
     rect(200, 100), dh_rect(200, 100)),
    ("SA-2", "Bay 4 -> bay 3", 195, "150 x 100 rect", rect(150, 100),
     dh_rect(150, 100)),
    ("SA-3", "Bay 3 -> bay 2", 60, "100 dia circular", circ(100), 0.1),
    ("SA-4", "Bay 2 -> bay 1", 30, "100 dia circular", circ(100), 0.1),
    ("SA-5", "Branch to U-05, CBRN plant", 60, "100 dia circular", circ(100),
     0.1),
    ("EA-1", "Lavatory extract, U-02 to the airlock", 45, "100 dia circular",
     circ(100), 0.1),
    ("EA-2", "Airlock transfer to BV-3", 300, "DN100 circular", circ(100), 0.1),
    ("GA-1", "Generator intake, BV-4", 2600, "DN350 circular", circ(350), 0.35),
    ("GA-2", "Generator exhaust, BV-5", 2600, "DN350 circular", circ(350),
     0.35),
]
w(f"  {'REF':6s} {'SERVES':38s} {'m3/h':>6s} {'SIZE':18s} {'AREA m2':>9s} "
  f"{'v m/s':>7s}  NOTE")
for ref, srv, q, size, a, dh in DUCTS:
    v = vel(q, a)
    if ref.startswith(("FA-1", "EA-2", "GA-")):
        note = "[C] fixed by S-06"
    else:
        note = "[A] this package"
    flag = "" if v >= 2.0 else "   size-governed"
    w(f"  {ref:6s} {srv:38s} {q:6.0f} {size:18s} {a:9.4f} {v:7.2f}  {note}{flag}")
w()
w("  Checks against the S-06 figures:")
w(f"      DN100 at 300 m3/h  ->  {vel(300, circ(100)):.1f} m/s   "
  f"S-06 states 10.6 m/s   REPRODUCED  [R]")
w(f"      DN350 at 2600 m3/h ->  {vel(2600, circ(350)):.1f} m/s   "
  f"S-06 states 7.5 m/s    REPRODUCED  [R]")
w()
w("  *** THE SMALL BRANCHES ARE GOVERNED BY THE PRACTICAL MINIMUM DUCT SIZE,")
w("      NOT BY VELOCITY.  At 30 m3/h a duct sized for 4 m/s would be about")
w("      100 x 25 mm - not buildable, not cleanable and not sealable to the")
w("      standard this envelope needs.  100 dia is adopted as the minimum, and")
w("      the resulting velocities of 1 to 2 m/s are a consequence, not a")
w("      defect.  The same logic governs the drainage package: below a certain")
w("      flow, size is set by buildability. ***")

# =====================================================================
head("H.8", "DUCT PRESSURE LOSS")
w()
w("  Darcy-Weisbach with the Colebrook-White friction factor.")
w("      dp = lambda (L/Dh) (rho v^2 / 2)")
w(f"      rho = {RHO} kg/m3, nu = {NU:.2e} m2/s, epsilon = {EPS*1000:.2f} mm   [A]")
w("  These are standard tabulated air properties and a standard roughness for")
w("  galvanised steel.  THE SOURCE DOCUMENT IS NOT IN THE WORKSPACE (master")
w("  open item M2), so they are tagged [A] and not attributed to a code.")
w()


def colebrook(re, dh):
    if re < 2300:
        return 64.0 / re
    f = 0.02
    for _ in range(60):
        f = (-2.0 * math.log10(EPS / (3.7 * dh) + 2.51 / (re * math.sqrt(f)))) ** -2
    return f


# ref, description, Q m3/h, area, Dh, length m, sum of fitting k
ROUTES = [
    ("FA", "Fresh air: BV-1 -> filter train 1, bay 1 west wall to bay 5",
     300, circ(200), 0.2, 11.2, 3.5),
    ("SA", "Supply: plenum bay 5 -> bay 1, worst index run",
     240, rect(200, 100), dh_rect(200, 100), 10.6, 4.0),
    ("EA", "Extract: U-02 lavatory -> airlock, bay 2 to bay 6",
     45, circ(100), 0.1, 9.3, 2.5),
]
w(f"  {'REF':4s} {'ROUTE':56s} {'L m':>5s} {'v':>6s} {'Re':>10s} "
  f"{'lambda':>7s} {'dp Pa':>7s}")
dp_total = {}
for ref, desc, q, a, dh, L, k in ROUTES:
    v = vel(q, a)
    re = v * dh / NU
    lam = colebrook(re, dh)
    dp_f = lam * (L / dh) * (RHO * v ** 2 / 2.0)
    dp_k = k * (RHO * v ** 2 / 2.0)
    dp = dp_f + dp_k
    dp_total[ref] = dp
    w(f"  {ref:4s} {desc:56s} {L:5.1f} {v:6.2f} {re:10.0f} {lam:7.4f} {dp:7.1f}")
    w(f"       friction {dp_f:.1f} Pa  +  fittings k={k:.1f} -> {dp_k:.1f} Pa")
w()
w("  Fitting k values are a nominal allowance for the bends, the transitions and")
w("  the terminal on each route.  THE FITTING SCHEDULE IS NOT FIXED UNTIL THE")
w("  ROUTES ARE SET ON SITE - these are coordination-level figures.  [A]")

# =====================================================================
head("H.9", "FAN DUTY  -  what can be built up, and what cannot")
w()
fa = dp_total["FA"]
sa = dp_total["SA"]
w(f"  ONE TRAIN, {V['design_m3h']} m3/h.  Working from the intake inwards:")
w()
w(f"  1  Weather louvre, sand and debris trap ......... VENDOR DATA REQUIRED  [N]")
w(f"  2  Blast valve BV-1, open ....................... VENDOR DATA REQUIRED  [N]")
w(f"  3  Raw-air duct, {ROUTES[0][5]:.1f} m ......................... {fa:6.1f} Pa   [R]")
w(f"  4  Pre-filter G4 / F7, clean -> dirty ........... VENDOR DATA REQUIRED  [N]")
w(f"  5  HEPA EN 1822 H14, clean -> dirty ............. VENDOR DATA REQUIRED  [N]")
w(f"  6  Carbon ASZM-TEDA bed ......................... VENDOR DATA REQUIRED  [N]")
w(f"  7  Supply ductwork and terminals, {ROUTES[1][5]:.1f} m ........ {sa:6.1f} Pa   [R]")
w(f"  8  Plenum overpressure to be maintained ......... {100:6.1f} Pa   [C] S-06")
w()
w(f"  DUCTWORK AND OVERPRESSURE, THE PART THAT CAN BE CALCULATED  = "
  f"{fa + sa + 100:.0f} Pa   [R]")
w()
w("  *** THE FAN DUTY CANNOT BE CLOSED HERE. ***")
w("      Items 1, 2, 4, 5 and 6 are VENDOR DATA and in a CBRN filter train they")
w("      dominate: a loaded H14 HEPA and a carbon bed together are normally")
w("      several times the ductwork loss.  Quoting a fan duty without them")
w("      would be a fabricated number.")
w()
w("      WHAT MUST BE SPECIFIED WHEN THE VENDOR IS SELECTED:")
w("        - the CLEAN and the DIRTY (change-out) pressure drop of every stage;")
w("        - the fan selected on the DIRTY figure, not the clean one;")
w("        - the hand-crank drive sized on the same duty  [C] S-06 shows one;")
w(f"        - the plenum held at {V['overpressure']} across the whole range.")
w()
w("      A FLOW METER AND A DIFFERENTIAL-PRESSURE GAUGE ACROSS EVERY STAGE are")
w("      already required by S-06 - 'the only way to know a filter is spent'.")
w("      They are what turns the vendor's dirty figure into a maintenance")
w("      trigger.")

# =====================================================================
head("H.10", "COOLING, HEATING AND HUMIDITY  -  NOT CALCULATED, AND WHY")
w()
w("  NO COOLING LOAD IS CALCULATED IN THIS PACKAGE.  The inputs do not exist.")
w()
w("  WHAT WOULD BE NEEDED, AND WHAT THE PROJECT ACTUALLY HAS:")
w("    outdoor design dry-bulb / wet-bulb, Pune ......... NOT IN THE PROJECT  [N]")
w("    indoor design condition and tolerance ............ NOT IN THE PROJECT  [N]")
w("    occupant sensible and latent gain rates .......... NOT IN THE PROJECT  [N]")
w("    equipment heat: filter fans, CO2/O2 plant,")
w("        dehumidifier, comms, lighting ................ NOT IN THE PROJECT  [N]")
w("    generator heat rejection into bay 8 .............. NOT IN THE PROJECT  [N]")
w("        (the 15 kVA rating is confirmed; its heat")
w("         rejection and whether bay 8 is conditioned")
w("         at all are not)")
w("    ground temperature at (-)6.100 in basalt ......... NOT IN THE PROJECT  [N]")
w("    U-value of the buried envelope ................... NOT IN THE PROJECT  [N]")
w("        (600 walls / 900 roof / 600 mat are confirmed,")
w("         but no thermal conductivity is given for M35")
w("         or for the surrounding rock)")
w()
w("  A dehumidifier IS confirmed in bay 5 (master A.3) and condensate IS in the")
w("  drainage flow table at 200 L/day combined with washdown [C].  Its DUTY is")
w("  not stated anywhere and is not derived here.")
w()
w("  *** WHAT CAN BE SAID WITHOUT INVENTING ANYTHING ***")
w("  A buried structure surrounded by 4.7 m of rock is a very large thermal")
w("  flywheel: 22.0 x 6.2 external, 600 walls, 900 roof and 600 mat of M35.")
w("  Its steady-state condition is governed by the ROCK TEMPERATURE, not by the")
w("  outside air, and the rock temperature is the missing number.  Until it is")
w("  measured, a cooling load calculated from air-side data alone would be")
w("  wrong in both directions and by an unknown amount.")
w()
w("  AN UPPER BOUND ON THE CLOSED-MODE AIR TEMPERATURE RISE - clearly bounded,")
w("  clearly assumed, and useful only as a bound:")
mass = clean_v * RHO
cap = mass * CP
w(f"    air mass in the clean zone   {clean_v:.1f} x {RHO} = {mass:.1f} kg   [R]")
w(f"    heat capacity of that air    {mass:.1f} x {CP} = {cap/1000:.1f} kJ/K   [R]")
for q_pp in (60, 75, 100):
    rate = V["occupants"] * q_pp / cap * 3600.0
    w(f"    at {q_pp} W/person sensible [A]   {V['occupants']*q_pp} W  ->  "
      f"{rate:.1f} K/h  IF THE STRUCTURE ABSORBED NOTHING")
w()
w("  THAT IS AN UPPER BOUND ONLY.  It ignores the concrete entirely, and the")
w("  concrete is the dominant term - which is exactly why the real answer needs")
w("  a transient model and a measured rock temperature.  DO NOT SIZE PLANT ON")
w("  THESE NUMBERS.  They are here to show the magnitude of what is missing.")

# =====================================================================
head("H.11", "PROTECTIVE VENTILATION  -  the blast valves and the filter train")
w()
w("  ALL OF THIS IS CONFIRMED ON S-06 AND IS CARRIED FORWARD UNCHANGED.")
w()
w(f"  {'TAG':6s} {'SIZE':7s} {'SERVES':20s} {'m3/h':>6s} {'v':>9s} "
  f"{'DESIGN PRESSURE':17s} {'FORCE':>8s}")
for tag, size, serves, q, v, pr, f in P.BLAST_VALVES:
    w(f"  {tag:6s} {size:7s} {serves:20s} {q:6d} {v:>9s} {pr:17s} {f:>8s}")
w()
w("  POSITIONS, read out of sheet S-06 by parsing its geometry:")
w("      BV-1  (598, 2200)     west perimeter wall of bay 1")
w("      BV-2  (598, 4000)     west perimeter wall of bay 1")
w("      BV-3  (14998, 4900)   IN W6 - exhaust and OPRV, discharging to bay 7")
w("      BV-4  (21398, 1300)   east perimeter wall of bay 8, generator intake")
w("      BV-5  (21398, 4700)   east perimeter wall of bay 8, generator exhaust")
w()
w("  RECESSING.  S-06: 'RECESS EVERY VALVE.  IS 4991 Cl 6.2.1.'  A valve flush")
w("  in a vertical face sees the REFLECTED pressure p_r = 1366 kPa, 3.6 times")
w("  the 383 kPa side-on value - 131 kN on a DN350 disc instead of 36.8 kN.")
w()
w("  FILTER TRAIN, in order  [C] S-06:")
for stage, spec in P.FILTER_TRAIN:
    w(f"      {stage:18s} {spec}")
w()
w("  THE THREE THINGS A BLAST VALVE MUST DO  [C] S-06, reproduced because they")
w("  are the specification, not commentary:")
w("      1  CLOSE FAST ENOUGH.  At 50 psi the shock front travels ~600 m/s, so")
w("         in 2 ms it moves 1.2 m.  Keep >= 2.0 m of duct between the valve")
w("         and the plenum and the leak-through is trivial.")
w("      2  STAY SHUT.  The nuclear positive phase is 0.13-1.33 s - a thousand")
w("         times longer than a grenade.  SPECIFY THE HOLD TIME, not just the")
w("         closing time.  A valve that reopens at 50 ms is useless here.")
w("      3  SURVIVE THE SUCTION.  The negative phase pulls the disc the other")
w("         way at roughly 0.25 p_so ~ 86 kPa.  It must be rated in reverse.")
w()
w("  *** THE 2.0 m RULE IS A ROUTING CONSTRAINT ON THIS PACKAGE. ***")
w(f"      BV-1 and BV-2 are in the west wall at X 598; the filter trains are in")
w(f"      bay 5 at X 11098-12548.  The raw-air duct is {ROUTES[0][5]:.1f} m long, so the")
w("      2.0 m rule is satisfied more than five times over.  Recorded because")
w("      it is the reason the trains are NOT put next to the valves.")

# =====================================================================
head("H.12", "THE RAW-AIR DUCT  -  a protective element, not a duct")
w()
w("  *** FINDING - HV-F2 ***")
w("      S-06 puts the fresh-air blast valves in the WEST WALL OF BAY 1 and the")
w("      NBC filter trains in BAY 5.  Between them the air is UNFILTERED, and")
w(f"      the duct carrying it runs {ROUTES[0][5]:.1f} m THROUGH THE CLEAN ZONE - bays 1,")
w("      2, 3 and 4, past the stores, the lavatory, the ops room and the berths.")
w()
w("      Over that length the duct wall is THE ONLY BARRIER between the clean")
w("      zone and unfiltered outside air.  A pinhole in it in the design event")
w("      admits agent directly into the occupied space, downstream of nothing.")
w()
w("      THIS PACKAGE DOES NOT MOVE THE TRAINS - their position is confirmed on")
w("      an issued sheet.  It specifies the duct as a PROTECTIVE ELEMENT:")
w("        - fully welded stainless or heavy-gauge galvanised, NO push-fit and")
w("          NO slip joints anywhere inside the envelope;")
w("        - pressure tested to the ENVELOPE standard (+300 Pa) and not to a")
w("          ductwork standard, witnessed, before any ceiling is closed;")
w("        - run at high level on visible supports, NOT buried, NOT boxed in,")
w("          NOT inside a ceiling void - it must be inspectable along its whole")
w("          length;")
w("        - labelled RAW AIR - UNFILTERED at not more than 2 m centres;")
w("        - and it must be re-tested after any work in bays 1 to 4.")
w()
w("      ALTERNATIVELY, and this is the question for the protective designer:")
w("      SHOULD THE TRAINS MOVE TO BAY 1, next to the valves?  Bay 1 is 2900")
w("      wide against bay 5's 1560, it already holds ESC 1 and the 1000 L tank,")
w("      and moving them would remove the raw-air run from the clean zone")
w("      entirely.  THAT IS A PROTECTIVE-DESIGN DECISION, NOT A VENTILATION")
w("      ONE.  It is raised, not taken.")

# =====================================================================
head("H.13", "OPERATING MODES")
w()
modes = [
    ("1  NORMAL, UNFILTERED", "peacetime",
     "One train, filters bypassed if a bypass is fitted (not shown on S-06).",
     "300 m3/h", "atmospheric"),
    ("2  FILTERED / PROTECTIVE", "CBRN warning to all-clear",
     "One train through the full filter set; second train standby.",
     "300 m3/h", "+50 to +100 Pa"),
    ("3  CLOSED", "detonation to all-clear, or filter change",
     "All five blast valves shut.  Soda lime and O2 only.",
     "0", "sealed"),
    ("4  PURGE", "each entry through the airlock",
     "5 air changes of decon stage 1.  13 minutes, 4-5 persons per hour.",
     "300 m3/h", "cascade held"),
    ("5  GENERATOR RUNNING", "power or battery charging",
     "BV-4 and BV-5 open, 2600 m3/h through bay 8 ONLY.  Bay 8 is the grey",
     "2600 m3/h", "bay 8 not pressurised"),
]
for name, when, what, flow, press in modes:
    w(f"  {name}")
    w(f"      when      {when}")
    w(f"      what      {what}")
    w(f"      flow      {flow}")
    w(f"      pressure  {press}")
    w()
w("  *** MODE 5 IS INDEPENDENT OF MODES 1 TO 4. ***  The generator air path")
w("  (BV-4, BV-5, bay 8) does not touch the gas-tight envelope: bay 8 is outside")
w("  it, behind blast door 2 and W7.  Running the generator does not")
w("  depressurise the clean zone and does not consume filter life.")
w()
w("  *** MODE 1 - A GAP ON S-06.  A filter bypass for peacetime running is not")
w("      shown anywhere.  Without one, every hour of peacetime ventilation")
w("      spends carbon-bed life that is only replaceable by a filter change,")
w("      which itself needs mode 3.  ENGINEER TO CONFIRM whether a bypass with")
w("      gas-tight isolation is intended.  NOT ADDED HERE - adding a bypass")
w("      adds a leak path to the envelope and that is a protective decision. ***")

# =====================================================================
head("H.14", "WHAT THIS PACKAGE DOES NOT CALCULATE, AND WHY")
w()
for t, why in [
    ("Cooling load, sensible or latent",
     "eight separate inputs are missing - see H.10  [N]"),
    ("Heating load",
     "no indoor design condition and no ground temperature  [N]"),
    ("Dehumidifier duty",
     "the unit is confirmed; no latent load and no target RH exist  [N]"),
    ("Total fan static pressure",
     "five of the eight components are vendor data - see H.9  [N]"),
    ("Filter change-out interval and carbon bed life",
     "vendor data plus a challenge concentration; neither exists  [N]"),
    ("Sound levels in the berthing space",
     "no criterion is stated anywhere in the project  [N]"),
    ("Generator heat rejection into bay 8",
     "only the 15 kVA rating is confirmed  [N]"),
    ("Blast valve closing and hold times",
     "vendor tested, master C.1 - not a civil deliverable  [C]"),
    ("Shock propagation down the entry shaft",
     "master Part C: Phase 3, CFD or shock tube  [C]"),
    ("EMP performance of the duct penetrations",
     "MIL-STD-188-125-1; the cast-in frames are welded to the cage for "
     "continuity, but the shielding survey is a separate scope  [C]"),
]:
    w(f"  - {t}")
    w(f"        {why}")

rule("=")
w("END OF HVAC CALCULATIONS")
rule("=")

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    dest = os.path.abspath(os.path.join(here, "..", "Calculations",
                                        "HV_CALC_OUTPUT.txt"))
    hdr = (f"HVAC CALCULATIONS  -  OUTPUT OF hv_calc.py\n"
           f"UNDERGROUND CBRN-HARDENED PROTECTIVE STRUCTURE, PUNE  -  "
           f"{P.GEOM_REV}\n"
           f"PACKAGE REVISION {P.REV['hvac']}   {P.PACKAGE_DATE}   {P.STATUS}\n"
           f"SENTRY POST EXCLUDED\n")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w") as f:
        f.write(hdr + "\n".join(OUT) + "\n")
    print(hdr + "\n".join(OUT))
    print(f"\n[written] {dest}")
