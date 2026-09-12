"""rc5_calc.py -- the calculations behind revision RC5 (master Part H.29).

Four more rulings by the project owner, 12 September 2026.  Three actioned,
one left open.  Nothing here is a STAAD.Pro run.
"""
import math
W=[]
def w(s=""): W.append(s); print(s)
def rule(t): w(); w("="*78); w("  "+t); w("="*78)

# =========================================================================
rule("R.7  RC4-V1 -- REJECT THE HEAT TO THE VENTILATION AIR, OPEN MODE ONLY")
# =========================================================================
w("""
RULING: no new envelope penetration.  Cool only when the shelter is
ventilating; ride out closed mode on thermal mass.

THE VALUE OF THIS RULING IS REAL AND SHOULD BE SAID FIRST: every penetration
you do not make is a penetration that cannot fail.  A ground loop would have
put TWO more metallic bores through a boundary that already has eleven
entries in the penetration register, two of which (BV-4/BV-5) already fail
the EMP criteria.  This ruling adds none.

WHAT IT BUYS, ARITHMETICALLY.
""")
rho,cp = 1.2, 1.005
Qs = 6.363                                  # kW sensible, from R.2
for V in (300.0, 600.0):
    C = V/3600.0*rho*cp
    w(f"  ventilation {V:.0f} m3/h  ->  thermal capacity {V:.0f}/3600 x {rho} x {cp} "
      f"= {C:.4f} kW/K")
    w(f"    temperature difference needed to reject {Qs:.3f} kW : {Qs/C:.1f} K")
w("")
w("  300 m3/h is the DUTY rate -- master A.3 and the EL1 load schedule are")
w("  explicit that the second filter train is STANDBY, NOT SIMULTANEOUS.")
w("  600 m3/h is both trains running, which the design does not contemplate.")
w("")
w("  AT A REALISTIC TEMPERATURE DIFFERENCE:")
for dT in (5.0, 10.0):
    for V in (300.0, 600.0):
        C = V/3600.0*rho*cp
        w(f"    dT {dT:4.1f} K, {V:.0f} m3/h  ->  {C*dT:5.2f} kW rejected "
          f"= {C*dT/Qs*100:4.1f} % of the {Qs:.3f} kW gain")
w("""
  *** FINDING RC5-F1.  THE VENTILATION AIR CANNOT REJECT THIS HEAT, AND IT
      WAS NEVER SIZED TO. ***

  The 300 m3/h is set by FEMA 453's 0.25 cfm/ft2 over the clean zone -- a
  CONTAMINANT rate, for CO2 and filtration.  It is about one order of
  magnitude short of a heat-rejection rate.  Even with BOTH trains running
  and a 10 K difference it removes about a third of the gain, and the design
  does not run both trains.

  AND IN PUNE IT CAN BE WORSE THAN NOTHING.  The supply air is ambient.
  Whenever ambient exceeds the internal temperature -- which in Pune is a
  large part of the year in the afternoon -- ventilating in open mode ADDS
  sensible heat rather than removing it.  No ambient design temperature
  exists anywhere in this project [N], so the number of hours cannot be
  stated; the direction can.

  WHAT THIS MEANS FOR THE RULING.  Taken literally the ruling rejects little
  heat in open mode and none in closed mode, so THE STRUCTURE AND THE ROCK
  CARRY ESSENTIALLY THE WHOLE LOAD IN BOTH MODES.  The 96 h closed-mode
  answer is therefore unchanged from R.2: about 13.2 K of rise, reaching
  roughly 39 C and still climbing.

  *** THE RULING IS THEREFORE RECORDED AS AN ACCEPTANCE OF THAT CONDITION,
      NOT AS A SOLUTION TO IT. ***  That is a habitability judgement and it
  is the owner's to make.  What RC5 adds is the arithmetic showing what is
  being accepted, so that it is accepted with the number in view.

  NOT DESIGNED, NOT INVENTED: no cooling plant, no coil, no ground loop and
  no ambient design condition.  RC4-V1 is NOT closed -- it is RULED AND
  NARROWED, from 'no rejection path exists' to 'the rejection path is the
  ground through the structure, and it has not been modelled'.  A transient
  soil-structure thermal model is the missing piece and it is a sibling of
  the transient soil-structure INTERACTION already listed for Phase 3.""")

# =========================================================================
rule("R.8  EM-V6 -- THE ESCAPE SHAFT HEAD HATCH, AS A STRUCTURAL ELEMENT")
# =========================================================================
w("""
RULING: design the hatch as a structural element only; EMP bonding stays
with the EMP package.

  *** BEFORE THE DESIGN, THE QUESTION NOBODY HAS ASKED. ***

  Master A.2: 'PROTECTIVE BOUNDARY = Blast Doors 1 and 2 at (-)6.100, plus
  walls W6/W7, THE PERIMETER WALLS, THE MAT AND THE PRESSURE SLAB.'

  ESC 1 and ESC 2 are 1400 dia bores THROUGH THE PRESSURE SLAB.  They start
  in bay 1 and bay 8 -- both inside the perimeter walls and under the slab --
  and they finish at grade.

  So each shaft head is a 1.54 m2 hole in the protective boundary, and the
  ONLY thing that can close it is a hatch that does not exist.  The envelope
  penetration register lists ESC1 and ESC2 as FAIL and prescribes a bonded
  conducting hatch -- but it prescribes it FOR EMP.  NOTHING ANYWHERE IN THIS
  PROJECT STATES WHAT THE HEAD HAS TO RESIST STRUCTURALLY.

  *** FINDING RC5-F2.  TWO 1400 dia PENETRATIONS OF THE PROTECTIVE BOUNDARY
      HAVE NO SPECIFIED CLOSURE.  If the head is only a weather cover, blast
      runs down a 1400 bore into bay 1 -- which is inside the gas-tight
      envelope -- and into bay 8.  The design is silent, so this design takes
      the only defensible reading: THE HEAD IS PART OF THE BOUNDARY AND TAKES
      THE FULL DESIGN BLAST. ***
""")
p = 383.0                                   # kPa, master A.7.1
a = 0.700                                   # m, clear radius
nu = 0.3
F = p*math.pi*a**2
w(f"  DEMAND, head at grade -- IS 4991: everything at grade takes p_so")
w(f"    design blast pressure                       = {p:.0f} kPa")
w(f"    clear opening 1400 dia, radius a            = {a:.3f} m")
w(f"    total force on the leaf  {p:.0f} x pi x {a:.3f}^2   = {F:.1f} kN")
M = p*a**2*(3+nu)/16.0
V = p*a/2.0
w(f"    simply-supported circular plate, UDL:")
w(f"      M = w.a^2.(3+nu)/16 = {p:.0f} x {a**2:.4f} x {3+nu:.1f}/16 = {M:.2f} kNm/m")
w(f"      V at the seating    = w.a/2 = {V:.1f} kN/m")
w("")
fy = 250.0
t_req = math.sqrt(6*M*1e3/fy)
w(f"  IF IT WERE A FLAT STEEL PLATE, Fe{fy:.0f}:")
w(f"    t = sqrt(6M/sigma) = sqrt(6 x {M*1e3:.0f} / {fy:.0f}) = {t_req:.1f} mm  -> say 32 mm")
d_leaf = 1.600
m_flat = math.pi*(d_leaf/2)**2*0.032*7850
w(f"    mass of a {d_leaf*1000:.0f} dia x 32 leaf = {m_flat:.0f} kg")
w(f"""
    *** {m_flat:.0f} kg IS THE POINT, NOT THE THICKNESS. ***
    Half a tonne cannot be lifted by a person escaping up a 6.8 m ladder in
    the dark.  A FLAT PLATE IS THE WRONG FORM, and the calculation is worth
    doing precisely because it shows why.
""")
w("""  ADOPTED -- RIBBED STEEL LEAF ON A CAST-IN SEATING RING

    Leaf        1600 dia, 12 mm face plate, 8 No. radial ribs 150 x 10 and a
                150 x 12 perimeter ring, all welded -- a weldment, not a plate
    Seating     continuous steel ring cast into the 250 RC collar, machined
                seat, with a compressible gasket for weather and gas
    Bearing     150 mm all round onto the collar, so the 1900 OD collar
                carries the 589.5 kN as a ring load
    Fixing      four quarter-turn dogs engaging the seating ring, so the leaf
                resists UPLIFT as well as downward pressure -- the negative
                phase and the rebound both lift it
    Operation   COUNTERBALANCED OR SPRING-ASSISTED, openable from INSIDE by
                one person without a key or a tool, and lockable from outside
    Drainage    the seat drains outward; no ponding on the gasket
""")
m_ribbed = (math.pi*(d_leaf/2)**2*0.012 + 8*a*0.150*0.010
            + math.pi*1.45*0.150*0.012)*7850
w(f"    indicative leaf mass  {m_ribbed:.0f} kg  -- still a mechanically assisted item")
w("""
  WHAT IS NOT DESIGNED HERE, AND IS NOT INVENTED:
    - THE RIB PROPORTIONING.  A ribbed circular leaf is an orthotropic plate
      problem; the flat-plate demand above is exact and is the BRIEF, but the
      weldment itself needs FE or a proprietary design.  [N]
    - THE COUNTERBALANCE MECHANISM.  Specialist. [N]
    - EVERY EMP FIGURE.  By ruling, bonding stays with the EMP package.

  *** AND THE CONSEQUENCE OF SPLITTING IT THAT WAY, STATED PLAINLY. ***
  The EMP treatment for this opening is a BONDED CONDUCTING hatch.  Bonding
  is not a finish applied later -- it is continuity between the leaf, the
  seating ring and the collar reinforcement, and it has to be designed into
  the weldment and the seat, not added to them.  Ruling the structure and the
  bonding into different packages is exactly how these two shaft heads came
  to be undesigned for four revisions.  EM-V6 STAYS OPEN for its EMP half.""")

# =========================================================================
rule("R.9  EL-V2 -- GENERATOR FUEL: A DAY TANK INSIDE")
# =========================================================================
kwh, rate = 600.6, 0.35
L = kwh*rate
w(f"""
RULING: specify a day tank inside, sized to the derived duty.

  DERIVATION, from EL1 and unchanged:
    generator energy over a 96 h run              = {kwh:.1f} kWh   [R]
    specific fuel consumption                     = {rate:.2f} L/kWh [A]
    fuel for 96 h  {kwh:.1f} x {rate:.2f}                  = {L:.1f} L
""")
usable = 210.0
nom = 250.0
bund = nom*1.10
w(f"  ADOPTED")
w(f"    usable volume                             = {usable:.0f} L  [R]")
w(f"    nominal tank                              = {nom:.0f} L  (ullage + draw-off allowance)")
w(f"    bund                                      = {bund:.0f} L  = 110 % of nominal")
w(f"""    location                                  = BAY 8, the grey zone
                                                 outside the gas-tight envelope,
                                                 INSIDE the EMP boundary (RC4)
    construction                              = welded steel, bunded, with a
                                                 contents gauge and a low-level
                                                 alarm to the S-01 fire panel
    fuel type                                 = [A] diesel assumed by the
                                                 0.35 L/kWh rate; NOT CONFIRMED

  *** THE FILL AND THE VENT ARE THE REAL DESIGN QUESTION, NOT THE TANK. ***

  A tank inside the structure needs a fill point outside it and a vent to
  atmosphere.  Both cross the protective boundary.  The project already
  carries eleven entries in its envelope penetration register, and RC4 has
  just ruled bay 8 INSIDE the EMP boundary -- so two new bores would each
  need blast, gas and EMP treatment, and BV-4/BV-5 in the same wall already
  FAIL the EMP criteria.

  ADOPTED -- ROUTE BOTH THROUGH THE EXISTING SH-2 BORE, AND ADD NO NEW
  PENETRATION.  SH-2 is the generator air shaft, 600 x 600, already crossing
  at X 22598-23198 with its head now fixed at +1.500 (RC4).  The fill line
  and the vent run up inside it.

    fill    DN25 metallic, lockable cap at the SH-2 head, bonded 360 deg
    vent    DN25 metallic gooseneck at the SH-2 head, discharging away from
            the SH-1 intake -- which RC4 placed 25.30 m away at the far end
    both    bonded to the same earth as the shaft; EMP treatment is the EMP
            package's, as EM-V6's ruling establishes for shaft penetrations

  This is the same instinct the owner applied to RC4-V1: USE WHAT ALREADY
  CROSSES.  It needs HVAC and EMP coordination, because SH-2 also carries
  BV-4 and BV-5, and two DN25 metallic lines sharing a 600 x 600 bore with
  two DN350 blast valves is a fit that has not been checked here.  [A]

  NOT DESIGNED, NOT INVENTED: fuel type unconfirmed; the 0.35 L/kWh rate is
  still [A]; no vendor set, no fuel polishing, no fire suppression for the
  tank, and no rate for any of it.  EL-V2 is RULED AND NARROWED, not closed.""")

open("/home/user/underground-shelter-project/Owner Rulings RC4/Calculations/RC5_CALC_OUTPUT.txt",
     "w").write("\n".join(W)+"\n")
