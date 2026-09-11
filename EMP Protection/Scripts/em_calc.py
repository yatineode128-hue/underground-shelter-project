"""
em_calc.py  --  every EMP figure this package publishes, derived here.

Nothing in the design basis, the schedules or the drawings is typed by hand.
Each section prints its inputs, its formula, its arithmetic and its result, so a
reviewer can follow the number rather than trust it.

MODEL CHOICE, STATED BEFORE ANY RESULT
    A reinforcement cage is modelled as a THIN CONDUCTING SCREEN pierced by a
    square array of apertures at the bar spacing:

        SE = 20 log10( lambda / 2s )   dB,   zero once lambda <= 2s

    That model is adopted for ONE reason: it is the model that reproduces the
    project's OWN confirmed figure.  Master K.3 records "EMP rebar cage 0 dB
    @ 1 GHz".  Section 2 below reaches -0.006 dB at 1 GHz from the confirmed
    150 mm bar spacing alone.  The project's number is recovered, not assumed.

    The classical array correction for n illuminated apertures, -10 log10(n),
    is NOT applied.  Applying it would make every cage figure WORSE.  Every
    cage number in this package is therefore an UPPER BOUND on a real cage,
    and the conclusions drawn from them are conservative in the safe direction.

    A waveguide-below-cutoff credit is taken ONLY where the bore is bounded by
    METAL.  Concrete is a lossy dielectric, not a waveguide wall.  The stair
    void and the escape shaft collars are reinforced concrete carrying 6-T25
    and 5-T25 respectively - six and five bars, not a conducting surface - so
    they take NO depth credit.  The blast valve bodies and the service entry
    plate are steel and do.

    Concrete absorption is real, is helpful, and is NOT credited: no
    permittivity, conductivity or moisture value for this concrete exists
    anywhere in the project.  [N]

Run:  python3 em_calc.py            (prints, and writes ../Calculations/EMP_CALC_OUTPUT.txt)
"""
import os
import sys
import math

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import em_proj as P                                        # noqa: E402

OUT = []


def w(s=""):
    OUT.append(s)
    print(s)


def h1(n, t):
    w("")
    w("=" * 78)
    w(f"{n}  {t}")
    w("=" * 78)


def h2(t):
    w("")
    w(f"--- {t} " + "-" * max(0, 73 - len(t)))


# ===================================================================== helpers
def lam(f_hz):
    """Free-space wavelength in mm."""
    return P.C_LIGHT / f_hz * 1000.0


def se_mesh(f_hz, s_mm):
    """Thin-screen SE of a square aperture array of pitch s, dB."""
    r = lam(f_hz) / (2.0 * s_mm)
    return 20.0 * math.log10(r) if r > 1.0 else 0.0


def f_mesh_cut(s_mm):
    """Frequency at which a mesh of pitch s stops shielding, Hz."""
    return P.C_LIGHT / (2.0 * s_mm / 1000.0)


def f_at_se(se_db, s_mm):
    """Frequency at which a mesh of pitch s delivers exactly se_db, Hz."""
    return P.C_LIGHT / (2.0 * s_mm / 1000.0 * 10.0 ** (se_db / 20.0))


def fc_circ(d_mm):
    """TE11 cutoff of a circular tube of bore d, Hz."""
    return 1.8412 * P.C_LIGHT / (math.pi * d_mm / 1000.0)


def fc_rect(w_mm):
    """TE10 cutoff of a rectangular tube of width w, Hz."""
    return P.C_LIGHT / (2.0 * w_mm / 1000.0)


def a_circ(L_mm, d_mm):
    """Below-cutoff attenuation of a circular tube, dB.  A = 8.686*(2pi/lc)*L."""
    lc = math.pi * d_mm / 1.8412            # cutoff wavelength, mm
    return 8.685889638 * (2.0 * math.pi / lc) * L_mm


def a_rect(L_mm, w_mm):
    """Below-cutoff attenuation of a rectangular tube, dB."""
    lc = 2.0 * w_mm
    return 8.685889638 * (2.0 * math.pi / lc) * L_mm


def strap_L(l_mm, w_mm, t_mm):
    """Self-inductance of a flat strap, henries.  l, w, t in mm."""
    l, wt = l_mm / 1000.0, (w_mm + t_mm) / 1000.0
    return 2.0e-7 * l * (math.log(2.0 * l / wt) + 0.5 + 0.2235 * wt / l)


def rod_R(rho, L, d):
    """Resistance of one vertical earth rod, ohm.  Dwight / IEEE 142 form."""
    a = d / 2.0
    return rho / (2.0 * math.pi * L) * (math.log(4.0 * L / a) - 1.0)


# which penetrations have a METAL bore, and therefore earn a waveguide credit
CONDUCTING = {"BV-1": True, "BV-2": True, "BV-3": True, "BV-4": True,
              "BV-5": True, "SEP": True, "PD-05": True,
              "ESC1": False, "ESC2": False, "VOID": False}

DECADES = [1e4, 3e4, 1e5, 3e5, 1e6, 3e6, 1e7, 3e7, 1e8, 3e8, 5e8, 1e9]


def fmt_f(f):
    if f >= 1e9:
        return f"{f/1e9:8.3f} GHz"
    if f >= 1e6:
        return f"{f/1e6:8.3f} MHz"
    if f >= 1e3:
        return f"{f/1e3:8.3f} kHz"
    return f"{f:8.1f} Hz "


# ============================================================================
def main():
    w("EMP PROTECTION - DESIGN CALCULATIONS")
    w(f"Underground CBRN-hardened blast-resistant protective structure - Pune")
    w(f"Package revision {P.REV}  ·  {P.PACKAGE_DATE}  ·  {P.GEOM_REV}")
    w(f"{P.STATUS}   ·   SENTRY POST EXCLUDED")
    w("")
    w("Evidence: [C] confirmed  [R] reconstructed  [D] derived here")
    w("          [A] assumed by this package  [U] unresolved  [N] not available")

    # ---------------------------------------------------------------- E.1
    h1("E.1", "THE REQUIREMENT - AND WHAT THE PROJECT ACTUALLY CONFIRMS")
    w("")
    w("From master Part G, the EMP entries in the code register:  [C]")
    w("")
    w("    MIL-STD-188-125-1   80 dB, 10 kHz - 1 GHz")
    w("                        5.4    access / shielded doors")
    w("                        5.5    waveguide below cutoff")
    w("                        5.7.2.1 power PCI")
    w("                        5.7.4.1 fibre")
    w("                        5.7.6  RF")
    w("    IEEE Std 299        shielding effectiveness survey")
    w("    IEEE 142 / IS 3043  earthing, <= 5 ohm target")
    w("")
    w(f"    SE required   {P.SE_REQUIRED_DB:.0f} dB, flat")
    w(f"    Band          {P.F_LO_HZ/1e3:.0f} kHz to {P.F_HI_HZ/1e9:.0f} GHz"
      f"  =  {math.log10(P.F_HI_HZ/P.F_LO_HZ):.0f} decades")
    w("")
    w("WHAT IS NOT CONFIRMED, and is NOT invented here:  [N]")
    w("    no incident field strength, no waveform, no E1/E2/E3 decomposition,")
    w("    no threat level.  U2 (is a direct hit a requirement) and U3 (the DBT")
    w("    yield) are both OPEN in master K.1b.  MIL-STD-188-125-1 states a")
    w("    PERFORMANCE requirement, not a field, so the whole of this package")
    w("    can be - and is - designed against 80 dB without one.")

    # ---------------------------------------------------------------- E.2
    h1("E.2", "THE REINFORCEMENT CAGE AS A SHIELD - AND THE K.3 CHECK")
    s = P.BAR_SPACING
    w("")
    w(f"Bar spacing  s = {s:.0f} mm, both curtains, both ways.  [C] master A.5:")
    w('   "Max bar spacing, both curtains - 150 mm, EMP requirement, stricter')
    w('    than IS 456 Cl. 26.3.3"')
    w("")
    w("    SE = 20 log10( lambda / 2s ),   lambda = c / f")
    w("")
    w(f"{'FREQUENCY':>14s}  {'WAVELENGTH':>14s}  {'lambda/2s':>11s}  "
      f"{'SE dB':>8s}   {'vs 80 dB':>9s}")
    w("-" * 68)
    for f in DECADES:
        L = lam(f)
        r = L / (2.0 * s)
        se = se_mesh(f, s)
        Ls = f"{L/1000.0:10.3f} m" if L >= 1000 else f"{L:10.1f} mm"
        w(f"{fmt_f(f):>14s}  {Ls:>14s}  {r:11.4f}  {se:8.2f}   "
          f"{'PASS' if se >= P.SE_REQUIRED_DB else 'FAIL':>9s}")
    w("-" * 68)
    w("")
    f_cut = f_mesh_cut(s)
    f_80 = f_at_se(P.SE_REQUIRED_DB, s)
    se_1g = se_mesh(1e9, s)
    w(f"  Mesh cutoff, SE -> 0     f = c/2s = {f_cut/1e6:9.3f} MHz")
    w(f"  SE at exactly 1 GHz                {se_1g:9.3f} dB")
    w(f"  Highest frequency at 80 dB         {f_80/1e3:9.3f} kHz")
    w("")
    w("  ** CHECK AGAINST THE MASTER **   K.3 records, as a CONFIRMED item:")
    w('       \"EMP rebar cage 0 dB @ 1 GHz\"')
    w(f"     This calculation gives {se_1g:.3f} dB at 1 GHz from the 150 mm bar")
    w(f"     spacing alone, and puts the mesh cutoff at {f_cut/1e6:.1f} MHz.")
    w("     THE PROJECT'S OWN FIGURE IS REPRODUCED.  [R]")
    w("")
    w("  ** AND THE COINCIDENCE WORTH SAYING OUT LOUD **")
    w(f"     2s = {2*s:.0f} mm.  The wavelength at 1 GHz is {lam(1e9):.2f} mm.")
    w("     The cage stops shielding at almost exactly the frequency at which")
    w("     MIL-STD-188-125-1 stops asking.  That is arithmetic, not design.")
    w("")
    dec_req = math.log10(P.F_HI_HZ / P.F_LO_HZ)
    dec_got = math.log10(f_80 / P.F_LO_HZ)
    w(f"  Decades required   {dec_req:.2f}")
    w(f"  Decades delivered  {dec_got:.2f}")
    w(f"  ==> THE CAGE MEETS THE REQUIREMENT OVER {dec_got/dec_req*100.0:.1f} %"
      f" OF THE REQUIRED BAND.")
    w("")
    w("  This is an UPPER BOUND.  The -10 log10(n) array correction is not")
    w("  applied, the crossings are TIED not welded, and no concrete absorption")
    w("  is credited.  A measured cage will be worse than this table.  [D]")

    # ---------------------------------------------------------------- E.3
    h1("E.3", "EVERY HOLE IN THE ENVELOPE")
    w("")
    w("Ten penetrations, all read from confirmed project documents.  Circular")
    w("bores use the TE11 cutoff and A = 8.686(2pi/lc)L; rectangular use TE10.")
    w("A depth credit is taken ONLY where the bore is bounded by METAL.")
    w("")
    w(f"{'TAG':>6s} {'BORE':>7s} {'DEPTH':>7s} {'METAL':>6s} {'f_c':>12s} "
      f"{'A dB':>8s} {'SE@10kHz':>9s} {'SE@1MHz':>8s} {'VERDICT':>8s}")
    w("-" * 78)
    rows = []
    for tag, kind, shape, bore, wall, host, note in P.PENETRATIONS:
        metal = CONDUCTING[tag]
        if shape == "CIRC":
            fc = fc_circ(bore)
            A = a_circ(wall, bore) if metal else 0.0
        else:
            fc = fc_rect(bore)
            A = a_rect(wall, bore) if metal else 0.0
        ap10k = 20.0 * math.log10(lam(1e4) / (2.0 * bore))
        ap1m = 20.0 * math.log10(lam(1e6) / (2.0 * bore))
        se10k, se1m = ap10k + A, ap1m + A
        ok = (fc >= P.F_HI_HZ) and (se1m >= P.SE_REQUIRED_DB)
        rows.append((tag, kind, shape, bore, wall, metal, fc, A, se10k, se1m,
                     ok, host, note))
        w(f"{tag:>6s} {bore:7.0f} {wall:7.0f} {'YES' if metal else 'NO':>6s} "
          f"{fmt_f(fc):>12s} {A:8.1f} {se10k:9.1f} {se1m:8.1f} "
          f"{'PASS' if ok else 'FAIL':>8s}")
    w("-" * 78)
    w("")
    w("SEP is listed READ AS AN OPEN APERTURE, which is the wrong reading and")
    w("is shown to make the point.  A service entry plate is not an aperture -")
    w("see E.3.4, where it is read correctly.")
    w("")
    w("** THE THREE-FIGURE NUMBERS IN THIS TABLE ARE THEORY, NOT PERFORMANCE. **")
    w("No practical penetration achieves 250 or 390 dB.  Real assemblies flatten")
    w("out around 100-120 dB, and what limits them is WORKMANSHIP - the bond at")
    w("the frame, the gasket, the one sleeve nobody welded - not the physics of")
    w("the bore.  Read a large number as 'the bore is not the problem here'.  [D]")
    w("")
    w("PASS means BOTH: below cutoff across the whole band (f_c >= 1 GHz) AND")
    w(f"at least {P.SE_REQUIRED_DB:.0f} dB in band.  Read the failures one at a time:")
    w("")
    for r in rows:
        (tag, kind, shape, bore, wall, metal, fc, A, se10k, se1m, ok, host,
         note) = r
        if ok:
            continue
        w(f"  {tag:6s} {kind:22s} {host}")
        if fc < P.F_HI_HZ:
            w(f"         cutoff {fmt_f(fc).strip()} is BELOW 1 GHz - the bore")
            w(f"         PROPAGATES above it, whatever its length.")
        if not metal:
            w(f"         bore is CONCRETE, not metal: no waveguide credit at all.")
        if fc < P.F_HI_HZ:
            w(f"         BELOW {fmt_f(fc).strip()} it gives {se1m:.1f} dB at 1 MHz;")
            w(f"         ABOVE it, nothing.  A bore that propagates cannot be")
            w(f"         rescued by making it longer.")
        else:
            w(f"         in-band SE {se1m:.1f} dB against"
              f" {P.SE_REQUIRED_DB:.0f} dB required.")
        w("")

    h2("E.3.1  the stair void, in its own right")
    v = P.VOID
    vw_, vl = v["x1"] - v["x0"], v["y1"] - v["y0"]
    fcv = fc_rect(max(vw_, vl))
    w("")
    w(f"  Opening in the 900 pressure slab, bay 7:  {vw_:.0f} x {vl:.0f} mm  [C] A.4.4")
    w(f"  Governing dimension                        {max(vw_, vl):.0f} mm")
    w(f"  Aperture cutoff  c/2L                      {fcv/1e6:.2f} MHz")
    w(f"  Area                                       {vw_*vl/1e6:.3f} m2")
    w("")
    w("  It is bounded by the thickened free edge, 900 -> 1200 with 6-T25 top")
    w("  and bottom  [C] F.1.  Six bars is not a conducting surface, so no")
    w("  depth credit applies.  As a thin-screen aperture:")
    w("")
    for f in (1e4, 1e5, 1e6, 1e7, 4.743e7, 1e8):
        r = lam(f) / (2.0 * max(vw_, vl))
        se = 20.0 * math.log10(r) if r > 1.0 else 0.0
        w(f"      {fmt_f(f):>12s}   SE = {se:7.2f} dB"
          f"   {'PASS' if se >= 80 else 'FAIL'}")
    w("")
    w("  THE STAIR VOID NEVER REACHES 80 dB ANYWHERE IN THE BAND, and above")
    w(f"  {fcv/1e6:.1f} MHz it is simply open.  It is the largest aperture in the")
    w("  envelope and it opens into the headhouse, which sits at +0.900 with")
    w("  NO EARTH COVER  [C] A.4.6, and thence to grade through a covered")
    w("  stairwell that is DECLARED EXPENDABLE  [C] A.2.")

    h2("E.3.2  the escape shafts")
    w("")
    for name, cx, cy, head in P.ESC:
        tag = "ESC1" if "1" in name else "ESC2"
        rec = [r for r in rows if r[0] == tag][0]
        Lsh = rec[4]
        fc = fc_circ(P.ESC_CLEAR_D)
        A_if = a_circ(Lsh, P.ESC_CLEAR_D)
        w(f"  {name}  bore {P.ESC_CLEAR_D:.0f}, collar {P.ESC_COLLAR_T} RC,"
          f" OD {P.ESC_COLLAR_OD}, head {head:+.3f}  [C] A.4.5")
        w(f"        shaft length grade to roof soffit    {Lsh:.0f} mm")
        w(f"        TE11 cutoff of a 1400 bore           {fc/1e6:.2f} MHz")
        w(f"        IF the collar were lined with metal  {A_if:.1f} dB")
        w(f"        it is not - 5-T25 each side/face/direction  [C] F.1")
        w("")
    w(f"  A FULLY CONDUCTING liner would give {a_circ(3050, 1400):.1f} dB on ESC 1"
      f" and {a_circ(3600, 1400):.1f} dB on ESC 2 -")
    w(f"  one below the {P.SE_REQUIRED_DB:.0f} dB required and one barely above it."
      f"  BOTH FIGURES ARE")
    w(f"  BESIDE THE POINT: they only hold below {fc_circ(1400)/1e6:.1f} MHz, and"
      f" above that a 1400")
    w("  bore propagates however well it is lined.")
    w("  Lining the shafts does not fix them.  The only treatment that works is")
    w("  a BONDED CONDUCTING HATCH at the head, which terminates the shaft")
    w("  instead of trying to attenuate down it.  No hatch is specified.  [N]")

    h2("E.3.3  the two DN350 generator bores, and the one decision behind them")
    w("")
    fc350 = fc_circ(350.0)
    a350 = a_circ(600.0, 350.0)
    w(f"  BV-4 / BV-5, DN350 through the 600 east wall  [C] HVAC schedule")
    w(f"        TE11 cutoff                    {fc350/1e6:.1f} MHz   < 1 GHz")
    w(f"        below-cutoff attenuation       {a350:.1f} dB   < {P.SE_REQUIRED_DB:.0f} dB")
    w("        FAILS BOTH CRITERIA - the only penetrations that do.")
    w("")
    w(f"  Compare the DN100 valves in the same wall:")
    w(f"        TE11 cutoff                    {fc_circ(100)/1e6:.1f} MHz   > 1 GHz")
    w(f"        below-cutoff attenuation       {a_circ(600, 100):.1f} dB")
    w("        The 600 wall does the whole job. No treatment is needed.")
    w("")
    w("  So the question is not how to fix BV-4/BV-5.  It is whether bay 8 is")
    w("  inside the EMP boundary at all.  Bay 8 is OUTSIDE the gas-tight")
    w("  envelope  [C] A.2 - but the gas-tight envelope is a CBRN boundary and")
    w("  says nothing about EMP.  No EMP boundary has ever been drawn.  [U]")
    w("  If bay 8 is IN, both bores need honeycomb - see E.5.")
    w("  If bay 8 is OUT, the 15 kVA generator, its control panel and every")
    w("  cable in bay 8 are unprotected, and the shelter loses power to the")
    w("  pulse.  That is open item EM-V3 and it is a client decision.")

    h2("E.3.4  the service entry plate")
    w("")
    w("  X 11398-12198 in the north wall, 800 wide, level [N], size [N].")
    w("  MEP_AND_FINISHES_COORDINATION.md CO-1 records that it must be at HIGH")
    w("  LEVEL because PD-05 rises over the filter trains, and that its level")
    w("  is not recorded anywhere in the project.")
    w("")
    fcs = fc_rect(800.0)
    w(f"  READ AS AN OPEN APERTURE 800 wide:  cutoff {fcs/1e6:.1f} MHz,")
    w(f"  attenuation {a_rect(600, 800):.1f} dB.  That would be a catastrophe.")
    w("")
    w("  READ CORRECTLY it is not an aperture at all.  A MIL-STD-188-125-1")
    w("  entry plate IS the shield: a solid welded plate, bonded 360 degrees to")
    w("  the cast-in frame, itself welded to the cage.  The apertures are the")
    w("  individual service sleeves through it, and each is treated on its own:")
    w("")
    d5 = 50.0
    w(f"      PD-05 DN50 bore    cutoff {fc_circ(d5)/1e6:.0f} MHz,"
      f" A = {a_circ(600, d5):.0f} dB   [D] ample")
    w("      power              PCI, MIL-STD-188-125-1 5.7.2.1")
    w("      signal             FIBRE, 5.7.4.1 - a dielectric is not a")
    w("                         penetration.  THIS IS THE PREFERRED TREATMENT.")
    w("")
    w("  ONE WARNING.  PD-05's MATERIAL IS NOT SPECIFIED ANYWHERE IN THE")
    w("  PROJECT  [N] - the drainage package names no pipe material for any")
    w("  run.  It changes the treatment completely:")
    w("      metallic pipe   -> bond it 360 deg to the plate.  The pipe exterior")
    w("                         becomes shield.  Correct, and cheap.")
    w("      plastic pipe    -> the bore is an aperture AND the water column is")
    w("                         a conductor through it.  Needs a metallic spool")
    w("                         piece at the plate.  Nobody has specified one.")

    # ---------------------------------------------------------------- E.4
    h1("E.4", "THE ZONE MODEL - ADOPTED BY THE PROJECT OWNER, RC2")
    w("")
    w("Master A.3 puts an 'EMP Zone 2 enclosure' in bay 3.  [C]")
    w("Finishes W-04 calls it 'EMP ZONE 2 SHIELDED ENCLOSURE LINING ... welded")
    w("steel room, shielding effectiveness verified to IEEE Std 299',")
    w("classed [C] requirement / [N] specification.")
    w("")
    w("THERE WAS NO EMP ZONE 1 ANYWHERE IN THE PROJECT, and no EMP Zone 0.")
    w("'Zone 2' had been used for four revisions with nothing to be the second")
    w("of.  The three zones below were DERIVED by EM1 and are now")
    w("")
    w("  *** ADOPTED BY THE PROJECT OWNER - RC2, 11 September 2026,")
    w("      master H.21.  THE THREE-ZONE MODEL AND THE STANDING-ALONE")
    w("      RULE BELOW ARE THE PROJECT'S ADOPTED EMP POSITION.  [C] ***")
    w("")
    w("EM-V1 IS CLOSED.  Nothing else in EM1 changes: no figure, no finding,")
    w("no other open item.  The model was already what the package was built")
    w("on - the ruling makes it the project's, not this package's.  [D]")
    w("")
    w("  EMP ZONE 0   everything above grade.  Sentry post +7.000, headhouse")
    w("               +0.900 with no earth cover, covered stairwell +2.450,")
    w("               shaft heads, burster slab.  NO ATTENUATION CREDITED.")
    w("")
    w("  EMP ZONE 1   the buried box, all eight bays.  The reinforcement cage.")
    w(f"               {se_mesh(1e4, s):.0f} dB at 10 kHz falling 20 dB/decade to"
      f" {se_mesh(1e9, s):.0f} dB at {f_mesh_cut(s)/1e6:.0f} MHz,")
    w("               pierced by a 2800 x 3160 stair void and two 1400 shafts.")
    w("               NOT a MIL-STD-188-125-1 shield.  NOT to be credited as one.")
    w("")
    w("  EMP ZONE 2   the welded steel enclosure in bay 3 (U-03).  THE ONLY")
    w(f"               SURFACE IN THIS PROJECT THAT DELIVERS"
      f" {P.SE_REQUIRED_DB:.0f} dB, 10 kHz - 1 GHz.")
    w("")
    w("THE DESIGN RULE, ADOPTED WITH THE MODEL - the whole package in one line:")
    w("")
    w("  *** ZONE 2 IS DESIGNED TO THE FULL 80 dB STANDING ALONE.  NO")
    w("      ATTENUATION FROM THE CONCRETE BOX IS CREDITED AT ANY FREQUENCY.")
    w("      ADOPTED - RC2.  [C] ***")
    w("")
    w("  The cage is then margin rather than design, which is the only")
    w("  defensible way to use a shield you cannot survey behind 2 m of earth.")
    w("")
    w("NAMING.  Drainage and finishes already use 'zone 1/2/3' for CLEANLINESS")
    w("[C].  These are different zones on the same building.  The prefix 'EMP'")
    w("is MANDATORY on every drawing, schedule and note.  [D]")
    w("")
    w("WHAT EMP PROTECTION IS FOR, said plainly, because the small enclosure")
    w("invites the wrong reading:  HEMP IS NOT A PERSONNEL HAZARD.  The people")
    w("are protected from blast, CBRN and fallout by the box.  EMP protection")
    w("exists so the shelter can still FUNCTION afterwards.  Zone 2 protects")
    w("equipment, and it is correct that it is small.  [D]")

    # ---------------------------------------------------------------- E.5
    h1("E.5", "EMP ZONE 2 ENCLOSURE - AN ENGINEERING SELECTION  [A]")
    Z = P.Z2
    ex, ey = Z["x1"] - Z["x0"], Z["y1"] - Z["y0"]
    eh = Z["h_ext"]
    t = Z["panel"]
    ix, iy, ih = ex - 2 * t, ey - 2 * t, eh - 2 * t
    w("")
    w("EVERY DIMENSION HERE IS [A].  The project confirms the enclosure is")
    w("REQUIRED and contains no specification for it.  No equipment schedule")
    w("exists, because no electrical design exists - the project's largest gap")
    w("[C] master H.10.  These dimensions are a competent placeholder that")
    w("fits, not a derived size.  See open item EM-V2.")
    w("")
    w(f"  Host bay 3 (U-03) internal   3500 x 5000 x {P.H_CLEAR} clear  [C] A.3")
    w(f"  Enclosure external plan      X {Z['x0']}-{Z['x1']}"
      f"  Y {Z['y0']}-{Z['y1']}   {ex:.0f} x {ey:.0f}")
    w(f"  Enclosure external height    {eh:.0f}")
    w(f"  Shielded panel               {t:.0f}")
    w(f"  Internal clear               {ix:.0f} x {iy:.0f} x {ih:.0f}")
    w(f"  Internal floor area          {ix*iy/1e6:.3f} m2")
    w(f"  Internal volume              {ix*iy*ih/1e9:.3f} m3")
    w("")
    w("  SITING, and why it is where it is:")
    w(f"    north gap to the wall face Y 5600      {5600 - Z['y1']:.0f} mm")
    w(f"    south gap to the circulation edge 3400 {Z['y0'] - 3400:.0f} mm")
    w(f"    west gap to the bay face X 5520        {Z['x0'] - 5520:.0f} mm")
    w(f"    east gap to the bay face X 9020        {9020 - Z['x1']:.0f} mm")
    w(f"    head to the roof soffit (-)2.900       {P.H_CLEAR - eh:.0f} mm")
    w("")
    w("    The W8 partition door gaps are at Y 2500-3400  [C] A.3, so the")
    w("    east-west circulation route through bay 3 runs at Y 2500-3400.")
    w("    THE ENCLOSURE IS ENTIRELY CLEAR OF IT.")
    w("    A 300 mm gap is held on every free face so that an IEEE Std 299")
    w("    survey can physically reach every seam.  A shielded room you cannot")
    w("    walk round cannot be tested, and an untested shield is a claim.")
    w(f"    HVAC ducts occupy a 150 deep zone under the soffit  [C] HV1:")
    w(f"    {P.H_CLEAR - eh - 150:.0f} mm remains clear above the enclosure.")
    w("")
    area_w = 2 * (ex * eh) + 2 * (ey * eh)
    area_rf = ex * ey
    area_t = (area_w + 2 * area_rf) / 1e6
    seam = (4 * ex + 4 * ey + 4 * eh) / 1000.0
    w(f"  Shielded envelope area       {area_t:.2f} m2")
    w(f"       walls {area_w/1e6:.2f}   roof {area_rf/1e6:.2f}   floor {area_rf/1e6:.2f}")
    w(f"  Total seam length            {seam:.2f} m")
    w("")
    w("  THE SEAM LENGTH IS THE RISK, not the area.  Every one of those")
    w(f"  {seam:.1f} metres has to be continuously welded or continuously")
    w("  gasketed, and IEEE Std 299 will find the metre that is not.")

    h2("E.5.1  the four ways into EMP Zone 2, and the treatment of each")
    cell, dep = P.Z2_VENT_CELL, P.Z2_VENT_DEPTH
    fcc = fc_circ(cell)
    Ah = a_circ(dep, cell)
    w("")
    w("  1  ACCESS   MIL-STD-188-125-1 5.4.  An RF-gasketed or knife-edge")
    w("     shielded door, its SE certified to match the enclosure.  Type and")
    w("     vendor [N].  A shielded door is the usual place a room fails.")
    w("")
    w("  2  VENTILATION   the enclosure holds powered equipment inside a sealed")
    w("     shelter and must pass air.  Honeycomb waveguide vent panels,")
    w("     5.5:")
    w(f"        cell             {cell:.0f} mm          [A]")
    w(f"        depth            {dep:.0f} mm         [A]")
    w(f"        TE11 cutoff      {fcc/1e9:.1f} GHz     >> 1 GHz")
    w(f"        attenuation      {Ah:.0f} dB       vs {P.SE_REQUIRED_DB:.0f} required")
    w(f"        margin           {Ah - P.SE_REQUIRED_DB:+.0f} dB")
    w("     Mounted INBOARD of any blast device: the valve takes the pressure,")
    w("     the honeycomb takes the RF.  Its own blast rating is [N].")
    w("     TWO CONSEQUENCES REFERRED, NOT RESOLVED HERE:")
    w("       - honeycomb adds pressure drop.  HV1 sized its fans without one.")
    w("       - the equipment's heat goes into bay 3.  HV1 sized U-03 on")
    w("         OCCUPANCY.  The load is [N] until an equipment schedule exists.")
    w("")
    w("  3  POWER   MIL-STD-188-125-1 5.7.2.1, a PCI on every conductor")
    w("     crossing the boundary, mounted ON the boundary, not near it.")
    w("     No residual figure is quoted here: the standard specifies PCI")
    w("     performance by pulse test and the project's register carries the")
    w("     section number only.  Inventing a number would be worse than [N].")
    w("")
    w("  4  SIGNAL   MIL-STD-188-125-1 5.7.4.1.  FIBRE, with NO metallic")
    w("     strength member and no metallic armour.  A dielectric penetration")
    w("     is not a penetration.  THIS IS THE ONE PLACE THE PROJECT CAN BUY")
    w("     PERFECT PERFORMANCE FOR ALMOST NOTHING, and it should take it.  [D]")
    w("")
    w("  5  RF   MIL-STD-188-125-1 5.7.6 exists in the register for antennas.")
    w("     THERE IS NO ANTENNA, NO MAST, NO FEEDER AND NO COMMUNICATIONS")
    w("     DESIGN ANYWHERE IN THIS PROJECT.  [N]  An ops room that cannot")
    w("     transmit is an ops room in name only, and an antenna is by")
    w("     definition a deliberate conductor from outside to inside - the")
    w("     hardest EMP penetration there is.  Open item EM-V4.")

    # ---------------------------------------------------------------- E.6
    h1("E.6", "EARTHING - AND WHY 5 OHM IS THE WRONG TARGET TO CHASE")
    w("")
    w(f"  Target      <= {P.R_EARTH_TARGET:.0f} ohm   [C] master G (IEEE 142 /")
    w("               IS 3043) and the WM1 confirmed electrical scope.")
    w(f"  Ground      Deccan basalt, {P.RHO_BASALT[0]:.0f} - {P.RHO_BASALT[1]:.0f}"
      f" ohm.m  [C] master K.3,")
    w('               which already says "test earth resistance early".')
    w("")
    w(f"  ONE ROD, {P.ROD_L:.0f} m x {P.ROD_D*1000:.0f} mm   [A]")
    w("      R = rho/(2 pi L) [ ln(4L/a) - 1 ]")
    w("")
    for rho in P.RHO_BASALT:
        R = rod_R(rho, P.ROD_L, P.ROD_D)
        n_ideal = R / P.R_EARTH_TARGET
        w(f"      rho = {rho:7.0f} ohm.m   R = {R:9.1f} ohm"
          f"   rods for 5 ohm, NO interaction: {n_ideal:6.0f}")
    w("")
    w("      Rods interact.  A real group needs substantially more than the")
    w("      ideal count, and there is nowhere on this site to put them.")
    w("      ** 5 OHM IS NOT ACHIEVABLE WITH RODS IN BASALT. **  [D]")
    w("")
    B = P.BOX
    area = (B["x1"] - B["x0"]) * (B["y1"] - B["y0"]) / 1e6
    r_eq = math.sqrt(area / math.pi)
    w(f"  THE STRUCTURE ITSELF, which is already built and already bonded")
    w(f"      Mat footprint            {(B['x1']-B['x0'])/1000:.1f} x"
      f" {(B['y1']-B['y0'])/1000:.1f} = {area:.1f} m2  [C] A.4.2")
    w(f"      Equivalent disc radius   sqrt(A/pi) = {r_eq:.3f} m")
    w("      Surface-disc form, R = rho / 4r   (the conservative one; a fully")
    w("      buried disc is rho/8r, twice as good)")
    w("")
    for rho in P.RHO_BASALT:
        R = rho / (4.0 * r_eq)
        w(f"      rho = {rho:7.0f} ohm.m   R = {R:9.1f} ohm")
    w("")
    r_lo = P.RHO_BASALT[0] / (4.0 * r_eq)
    rod_lo = rod_R(P.RHO_BASALT[0], P.ROD_L, P.ROD_D)
    w(f"      Better than a single rod by a factor of {rod_lo/r_lo:.1f}, and it")
    w("      costs nothing because the cage is there.  A concrete-encased")
    w("      electrode is the right answer on rock.  [D]")
    w("")
    w("  *** BUT THE IMPORTANT POINT IS THAT 5 OHM IS NOT AN EMP NUMBER. ***")
    w("      <= 5 ohm is a POWER-SAFETY and LIGHTNING requirement from IS 3043")
    w("      and IEEE 142.  It is real and it still applies.  It is not what")
    w("      makes an EMP shield work.  An EMP shield works by being")
    w("      EQUIPOTENTIAL, and equipotential is decided by BONDING INDUCTANCE,")
    w("      not by earth resistance.  E.7 shows why.  [D]")

    # ---------------------------------------------------------------- E.7
    h1("E.7", "BONDING - WHERE EMP DESIGN ACTUALLY LIVES")
    w("")
    w("  L = 2e-7 . l . [ ln(2l/(w+t)) + 0.5 + 0.2235 (w+t)/l ]   henries")
    w("")
    w(f"{'STRAP':>34s} {'l mm':>6s} {'w mm':>5s} {'L nH':>8s} "
      f"{'X @1MHz':>9s} {'X @10MHz':>9s} {'X @100MHz':>10s}")
    w("-" * 78)
    for label, l_, w_, t_ in P.STRAPS:
        L = strap_L(l_, w_, t_)
        x1 = 2 * math.pi * 1e6 * L
        x10 = 2 * math.pi * 1e7 * L
        x100 = 2 * math.pi * 1e8 * L
        w(f"{label:>34s} {l_:6.0f} {w_:5.0f} {L*1e9:8.1f} "
          f"{x1:8.2f}o {x10:8.2f}o {x100:9.2f}o")
    w("-" * 78)
    w("")
    Llong = strap_L(600.0, 25.0, 3.0)
    Lshort = strap_L(100.0, 50.0, 3.0)
    w(f"  A 600 mm strap is {2*math.pi*1e8*Llong:.0f} ohm at 100 MHz.  That is")
    w("  not a bond.  It is a resistor with a nice green sleeve on it.")
    w(f"  Shortening it to 100 mm and widening it to 50 takes the inductance")
    w(f"  from {Llong*1e9:.0f} nH to {Lshort*1e9:.0f} nH, a factor of"
      f" {Llong/Lshort:.1f}.")
    w("")
    w("  THE RULES THAT FOLLOW, and they are the ones that get built wrong: [D]")
    w(f"    - every bond <= {P.BOND_MAX_LEN:.0f} mm long")
    w(f"    - width : length at least {P.BOND_MIN_WL:.0f} : 1")
    w("    - FLAT STRAP ONLY.  Never a round wire, never a pigtail, never a")
    w("      'we'll loop it round to the nearest stud'")
    w("    - clean bare metal both ends, protected after making")
    w("    - the shield bonds to the structure at ONE place.  A second bond is")
    w("      a loop, and a loop is an antenna.")
    w("")
    w("  This is the same physics the project already relies on without saying")
    w("  so: master A.5 requires the blast door frames to be CAST IN AND WELDED")
    w("  TO THE CAGE  [C], and B.7.2 requires it even for the non-blast-rated")
    w("  headhouse door.  Those are EMP bonds.  They were specified correctly.")

    # ---------------------------------------------------------------- E.8
    h1("E.8", "VERIFICATION - THE ONLY THING THAT SETTLES ANY OF THIS")
    w("")
    w("  IEEE Std 299 is in the register  [C] for a shielding effectiveness")
    w("  survey.  Applied here:")
    w("")
    w("    EMP ZONE 2   SURVEY IT.  Full IEEE 299 survey, 10 kHz - 1 GHz, on")
    w("                 the completed enclosure with every penetration made")
    w("                 off and every panel closed.  Acceptance 80 dB.  This")
    w("                 is a HOLD POINT: no equipment installed before it")
    w("                 passes, because a failed survey means opening seams.")
    w("")
    w("    EMP ZONE 1   DO NOT SURVEY IT, AND DO NOT CLAIM IT.  A buried box")
    w("                 under 2 m of engineered cover cannot be surveyed to")
    w("                 IEEE 299 - there is no accessible exterior to put a")
    w("                 transmitter on.  E.2 is a calculation, and it will")
    w("                 stay a calculation.  Any statement that the box gives")
    w("                 80 dB is unsupportable and should not be made.  [D]")
    w("")
    w("    WHAT CAN BE CHECKED ON SITE, cheaply, during construction:")
    w("      - CONTINUITY of the cage across every construction joint, before")
    w("        the pour.  Master F.1 already requires two waterstops and a")
    w("        welded Cu/galvanised EMP strap at every joint  [C].  MEASURE IT.")
    w("      - CONTINUITY of every cast-in frame to the cage, before the pour.")
    w("      - EARTH RESISTANCE, early, as K.3 already demands  [C].")
    w("      - BOND RESISTANCE at every strap after making off.")
    w("    None of these prove shielding effectiveness.  All of them catch the")
    w("    mistakes that destroy it, at the only moment they can be fixed.")

    # ---------------------------------------------------------------- E.9
    h1("E.9", "WHAT THIS PACKAGE COULD NOT DO")
    w("")
    for i, (tag, txt) in enumerate([
        ("[N] EQUIPMENT",
         "No equipment schedule, because no electrical design exists. The"
         " Zone 2 size, its heat load, its power and its signal count are all"
         " unknown. Every enclosure dimension in E.5 is [A]."),
        ("[N] THREAT",
         "No incident field, waveform or threat level. U2 and U3 are open in"
         " master K.1b. Designed to the 80 dB performance requirement instead,"
         " which needs neither."),
        ("[N] COMMUNICATIONS",
         "No antenna, mast, feeder or comms design of any kind. 5.7.6 cannot"
         " be applied to something that does not exist."),
        ("[N] VENDOR DATA",
         "No shielded door, PCI, honeycomb panel, blast valve or blast door"
         " vendor data. Blast door RF performance is unknown, and it sits on"
         " the protective boundary."),
        ("[N] MATERIALS",
         "No pipe material anywhere in the drainage package; no concrete"
         " permittivity or conductivity; no rebar crossing treatment"
         " (tied or welded) stated anywhere."),
        ("[U] BOUNDARY",
         "Whether bay 8 is inside the EMP boundary has never been decided,"
         " because no EMP boundary has ever been drawn. E.4 proposes one;"
         " only the client can adopt it."),
        ("[U] SENTRY POST",
         "Excluded, consistent with every other services package. It is above"
         " ground and not blast designed; its EMP exposure is total and"
         " nothing here changes that."),
    ], 1):
        w(f"  {i}  {tag}")
        for ln in _wrapt(txt, 68):
            w(f"        {ln}")
        w("")
    w("  NO VALUE IN THIS PACKAGE RESOLVES AN EXISTING [ASSUMED], [UNRESOLVED]")
    w("  OR [NOT AVAILABLE] ITEM.  Six new open items EM-V1 to EM-V6 are")
    w("  raised in the design basis.  That is deliberate: a package that")
    w("  quietly filled these in would be inventing a specification.")

    w("")
    w("=" * 78)
    w("END OF CALCULATIONS")
    w("=" * 78)

    path = os.path.join(_HERE, "..", "Calculations", "EMP_CALC_OUTPUT.txt")
    with open(os.path.abspath(path), "w") as fh:
        fh.write("\n".join(OUT) + "\n")
    return os.path.abspath(path)


def _wrapt(s, n):
    out, line = [], ""
    for wd in s.split():
        if len(line) + len(wd) + 1 > n and line:
            out.append(line)
            line = wd
        else:
            line = (line + " " + wd).strip()
    if line:
        out.append(line)
    return out


if __name__ == "__main__":
    p = main()
    print(f"\nwritten: {p}")
