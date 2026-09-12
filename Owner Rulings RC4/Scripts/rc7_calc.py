"""rc7_calc.py -- revision RC7 (master Part H.31).  EL-V7, the CO2 scrubber duty."""
W=[]
def w(s=""): W.append(s); print(s)
w("="*78); w("  R.11  EL-V7 -- CO2 SCRUBBER AIR MOVEMENT"); w("="*78)
w("""
RULING: compute the airflow.  The absorber and the soda lime charge stay
[N] -- vendor data.

THE CO2 PRODUCTION RATE IS ALREADY IN THIS PROJECT.  It does not have to be
assumed: it is embedded in the HVAC package's own 9.9 h figure, which the
design basis reproduces as

      time to 1.0 % CO2, airlock shut = (0.0096 x 184.96) / (9 x 0.02) = 9.9 h

Reading that backwards gives every term:
""")
frac, V_occ, n, per = 0.0096, 184.96, 9, 0.02
V_co2 = frac*V_occ
prod = n*per
w(f"    allowable rise, 0.04 % ambient -> 1.0 %          = {frac:.4f} volume fraction  [C]")
w(f"    occupied volume, airlock shut                    = {V_occ:.2f} m3            [C]")
w(f"    CO2 that fills that rise  {frac:.4f} x {V_occ:.2f}        = {V_co2:.4f} m3")
w(f"    occupants                                        = {n}                   [C]")
w(f"    CO2 production per person                        = {per:.2f} m3/h/person  [C]")
w(f"    TOTAL CO2 PRODUCTION  {n} x {per:.2f}                    = {prod:.2f} m3/h")
w(f"    check: {V_co2:.4f} / {prod:.2f} = {V_co2/prod:.2f} h   -- reproduces the stated 9.9 h")
w("")
w(f"    over a 96 h closed occupancy:  {prod:.2f} x 96 = {prod*96:.2f} m3 of CO2")
w("""
  THE SCRUBBER IS A CLOSED-MODE DEVICE.  In open mode the 300 m3/h of fresh
  air flushes CO2 and the scrubber is not needed.  In Mode 3 CLOSED there is
  no fresh air at all, and without a scrubber the envelope reaches 1.0 % in
  9.9 hours against a 96 hour design occupancy.  THAT RATIO -- 9.9 AGAINST
  96 -- IS WHY THE SCRUBBER IS NOT OPTIONAL.

  REQUIRED RECIRCULATION AIRFLOW.  At steady state the scrubber must remove
  CO2 as fast as the occupants make it:

      Q x (C_in - C_out) = production
      with a single-pass removal efficiency eta,  C_out = C_in (1 - eta)
      so   Q = production / (eta x C_target)
""")
w(f"    {'target CO2':>12s}  {'eta 0.50':>10s} {'eta 0.80':>10s} {'eta 0.95':>10s}")
for C, lbl in ((0.005, "0.5 %"), (0.010, "1.0 %")):
    row = "    %12s" % lbl
    for eta in (0.50, 0.80, 0.95):
        row += "  %8.1f  " % (prod/(eta*C))
    w(row + "m3/h")
w("""
  ADOPTED -- DESIGN THE RECIRCULATION LOOP FOR 75 m3/h   [R]

    75 m3/h is the worst cell in the table above (hold 0.5 %, assume only
    50 % single-pass removal).  Designing to the worst cell costs almost
    nothing -- see the fan check below -- and it means the loop still works
    if the absorber underperforms or if the operating limit is tightened
    from 1.0 % to 0.5 %.

  CHECK AGAINST THE ONLY NUMBER THE PROJECT ALREADY HAD.  EL1 carries a
  0.10 kW allowance for a recirculation fan (no tag, an allowance).
""")
Q, dp, eff = 75.0, 250.0, 0.45
P = Q/3600.0*dp/eff
w(f"    Q {Q:.0f} m3/h at an assumed {dp:.0f} Pa total across a packed bed  [A]")
w(f"    fan power = Q.dp/eta = ({Q:.0f}/3600) x {dp:.0f} / {eff:.2f} = {P:.1f} W")
w(f"    against the EL1 allowance of 100 W  ->  THE ALLOWANCE IS ADEQUATE,")
w(f"    with roughly {100/P:.1f} x margin even on a pessimistic bed resistance.")
w("""
    *** SO EL-V7 DOES NOT CHANGE THE ELECTRICAL DESIGN. ***  The 0.10 kW in
    the load schedule stands, the 6.256 kW connected load stands, and the
    15 kVA generator check at 49 % stands.  What changes is that the
    allowance is now CHECKED rather than assumed.

  FOR SCALE: 75 m3/h is a quarter of the 300 m3/h ventilation rate, moving
  0.35 air changes an hour through a small duct and a packed bed.  This is
  a domestic-sized fan, and it was always going to be.

  WHAT IS NOT DESIGNED AND IS NOT INVENTED  [N]:
    - the absorber vessel, its bed depth, face area and residence time
    - the SODA LIME CHARGE for 96 h (the 17.28 m3 of CO2 above is the duty
      it must absorb; converting that to a mass needs the product's stated
      absorption capacity, which is vendor data)
    - the single-pass efficiency, assumed above across a range rather than
      taken from any product
    - the duct route, and where in bay 5 the absorber stands.  Bay 5 is the
      TIGHTEST bay in the shelter at 1560 clear, and HV-F3 already records
      that the filter trains leave 110 mm at the sides

  EL-V7 IS RULED AND NARROWED: from 'in no schedule' to a stated duty of
  0.18 m3/h of CO2 and a 75 m3/h recirculation loop, with the equipment
  still to be selected.""")
open("/home/user/underground-shelter-project/Owner Rulings RC4/Calculations/RC7_CALC_OUTPUT.txt",
     "w").write("\n".join(W)+"\n")
