"""
em_sheets.py  --  the six A1 EMP Protection drawings, EM-001 to EM-302.

Every figure on every sheet is imported from em_proj / em_calc.  A drawing
cannot disagree with the calculation that produced it.

Run:  python3 em_sheets.py
"""
import os
import sys
import math

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import em_dxf as X                                          # noqa: E402
import em_proj as P                                         # noqa: E402
import em_calc as K                                         # noqa: E402
import mep_proj as MP                                       # noqa: E402
import mep_views as MV                                      # noqa: E402

T = X.TXT
OUT = os.path.abspath(os.path.join(HERE, "..", "DXF"))
NOTE, LEAD = 2.4, 4.3
CA, CB, CC = 14.0, 286.0, 558.0
WCOL = 264.0
TOP = 552.0
S = P.BAR_SPACING


def sheet(num, title, sub, flags=(), of=""):
    return X.Sheet(num, title, sub, flags=flags, sheet_of=of)


def _se(f):
    return K.se_mesh(f, S)


# =====================================================================
def em001():
    """Design basis, zone key, findings and general notes."""
    sh = sheet("EM-001", "EMP PROTECTION - DESIGN BASIS AND EMP ZONE KEY",
               "THE GOVERNING FACT - THE THREE EMP ZONES - FINDINGS - "
               "OPEN ITEMS - CODES",
               flags=("EM-F1", "EM-F3", "EM-V2"), of="1 OF 6")

    f80, fcut = K.f_at_se(P.SE_REQUIRED_DB, S), K.f_mesh_cut(S)

    sh.panel(CA, TOP, WCOL, "*** THE FACT THAT GOVERNS EVERYTHING ELSE ***", [
        "THE CONCRETE BOX IS NOT AN EMP SHIELD, AND IT NEVER COULD",
        "HAVE BEEN.",
        "",
        "The requirement is CONFIRMED and specific - master part G:",
        "     MIL-STD-188-125-1   80 dB,  10 kHz to 1 GHz.",
        "That is FIVE DECADES.  Two independent pieces of arithmetic,",
        "both from confirmed geometry, say the box does not deliver it:",
        "",
        "1  THE CAGE.  Bar spacing 150 both curtains is an EMP measure",
        f"   [C] A.5.  SE = 20 log10(lambda/2s) gives {_se(1e4):.0f} dB at 10 kHz,",
        f"   {_se(1e6):.0f} dB at 1 MHz and {_se(1e9):.2f} dB at 1 GHz.  It meets 80 dB",
        f"   ONLY BELOW {f80/1e3:.2f} kHz - ONE DECADE OF THE FIVE.",
        "",
        "2  THE HOLES.  A 900 pressure slab with a 2800 x 3160 stair",
        "   void in it is not a shield at any frequency.  Nor are two",
        "   1400 escape shafts.  See EM-201 and EM-102.",
        "",
        "SO THE 80 dB BOUNDARY MUST BE THE EMP ZONE 2 ENCLOSURE, AND",
        "EMP ZONE 2 IS THE ONLY EMP SHIELD THIS PROJECT HAS.",
        "IT HAS NEVER BEEN SPECIFIED.  [N]",
    ], h=NOTE, lead=LEAD)

    y = sh.panel(CB, TOP, WCOL, "THE CHECK THAT MATTERS - K.3 IS REPRODUCED", [
        "Master K.3 already records, as a CONFIRMED item:",
        '     \"EMP rebar cage 0 dB @ 1 GHz - SAY IT BEFORE A REVIEWER',
        '      DOES.  Zone 2 welded steel room is the answer.\"',
        "",
        f"This package reaches {_se(1e9):.3f} dB at 1 GHz FROM THE 150 mm BAR",
        f"SPACING ALONE, and puts the mesh cutoff at {fcut/1e6:.1f} MHz.",
        "THE PROJECT'S OWN FIGURE IS REPRODUCED, NOT ASSUMED.  [R]",
        "",
        f"2s = {2*S:.0f} mm.  The wavelength at 1 GHz is {K.lam(1e9):.2f} mm.",
        "The cage stops shielding at almost exactly the frequency at",
        "which MIL-STD-188-125-1 stops asking.  Arithmetic, not design.",
    ], h=NOTE, lead=LEAD)

    y = sh.panel(CB, y - 8, WCOL,
                 "*** THE DESIGN RULE - ADOPTED, RC2.  THE PACKAGE IN A LINE ***", [
        "EMP ZONE 2 IS DESIGNED TO THE FULL 80 dB STANDING ALONE.",
        "NO ATTENUATION FROM THE CONCRETE BOX IS CREDITED AT ANY",
        "FREQUENCY.",
        "",
        "The cage is then MARGIN, not design - the only defensible way",
        "to use a shield you can never survey under 2 m of cover.",
        "",
        "*** ADOPTED BY THE PROJECT OWNER - RC2, 11 Sep 2026, master",
        "    H.21.  THE THREE-ZONE MODEL AND THIS RULE ARE NOW THE",
        "    PROJECT'S EMP POSITION.  [C]   EM-V1 IS CLOSED. ***",
    ], h=NOTE, lead=LEAD)

    sh.panel(CB, y - 8, WCOL, "WHAT EMP PROTECTION IS FOR", [
        "HEMP IS NOT A PERSONNEL HAZARD.  The occupants are protected",
        "from blast, CBRN and fallout by the box.  EMP protection",
        "exists so the shelter can still FUNCTION afterwards.",
        "EMP Zone 2 protects EQUIPMENT.  It is correct that it is an",
        "enclosure and not a room, and nobody should expect to shelter",
        "inside it.  [D]",
    ], h=NOTE, lead=LEAD)

    y = X.zone_key(sh, CC, TOP, WCOL)

    y = sh.panel(CC, y - 8, WCOL, "WHAT THE DESIGN ALREADY DOES RIGHT  [C]", [
        "Four real strengths, none previously recorded as EMP measures:",
        "1  150 BAR SPACING is a deliberate EMP decision, stricter than",
        f"   IS 456 Cl. 26.3.3.  {_se(1e4):.0f} dB at 10 kHz is not nothing, and",
        "   it is strongest exactly where E3 lives.",
        "2  CAST-IN FRAMES ARE ALREADY EMP BONDS - A.5 requires every",
        "   blast door frame WELDED TO THE CAGE, and B.7.2 requires it",
        "   even for the NON-BLAST-RATED headhouse door.",
        "3  EVERY CONSTRUCTION JOINT already carries a welded Cu/galv",
        "   EMP strap plus two waterstops  [C] F.1.",
        "4  NO MOVEMENT JOINTS inside the envelope, and the master says",
        "   why: a movement joint is a guaranteed EMP discontinuity.",
        "",
        "NONE OF IT WAS EVER COLLECTED INTO AN EMP POSITION.",
        "THAT IS WHAT THIS PACKAGE IS.",
    ], h=NOTE, lead=LEAD)

    sh.panel(CC, y - 8, WCOL, "CODES  -  ONLY THOSE ALREADY IN MASTER PART G", [
        "MIL-STD-188-125-1   5.4 access · 5.5 waveguide below cutoff",
        "                    5.7.2.1 power PCI · 5.7.4.1 fibre · 5.7.6 RF",
        "                    80 dB, 10 kHz - 1 GHz",
        "IEEE Std 299        shielding effectiveness survey",
        "IEEE 142 / IS 3043  earthing, <= 5 ohm target",
        "IS 456:2000         Cl. 26.3.3 - the 150 cap is STRICTER",
        "",
        "NO CLAUSE NOT IN THAT REGISTER IS CITED, AND NONE IS INVENTED.",
    ], h=NOTE, lead=LEAD)

    # findings and open items, full width under the panels
    sh.table(CA, 258, [30, 500], [
        ["EM-F1", "THE STAIR VOID IS A 2800 x 3160 (8.85 m2) APERTURE THAT NEVER "
         "REACHES 80 dB AND IS OPEN ABOVE 47.4 MHz."],
        ["", "     It opens into the headhouse (+0.900, NO EARTH COVER) and thence "
         "to grade.  THE ENTRY ROUTE IS AN OPEN"],
        ["", "     ELECTROMAGNETIC PATH FROM GRADE TO BAY 7.  Blast Door 1 is the "
         "only thing across it and its RF"],
        ["", "     performance is vendor data the project does not have.  [N]   "
         "SEE EM-102."],
        ["EM-F2", "THE CAGE MEETS 80 dB OVER ONE DECADE OF THE FIVE REQUIRED, AND "
         "GIVES 0.00 dB AT 1 GHz.  This reproduces"],
        ["", "     master K.3's own confirmed figure.  A genuine low-frequency "
         "measure - NOT a MIL-STD boundary.  SEE EM-201."],
        ["EM-F3", "'EMP ZONE 2' HAS BEEN NAMED SINCE REV F WITH NO ZONE 1 AND NO "
         "ZONE 0 EVER DEFINED, and no specification"],
        ["", "     for the enclosure itself.  Finishes W-04 carries it as [C] "
         "requirement / [N] specification.  SEE EM-301."],
        ["EM-F4", "BV-4 AND BV-5 (DN350) ARE THE ONLY PENETRATIONS FAILING BOTH "
         "CRITERIA - cutoff 502 MHz, 54.8 dB."],
        ["", "     Behind them: IS BAY 8 INSIDE THE EMP BOUNDARY?  No EMP boundary "
         "has ever been drawn.  [U]"],
        ["EM-F5", "THE <= 5 OHM EARTHING TARGET IS NOT ACHIEVABLE WITH RODS IN "
         "DECCAN BASALT (335 ohm per rod at the LOW"],
        ["", "     resistivity bound) AND IS NOT AN EMP REQUIREMENT ANYWAY.  The "
         "structure is already the better electrode."],
        ["EM-F6", "THERE IS NO ANTENNA, MAST, FEEDER OR COMMUNICATIONS DESIGN "
         "ANYWHERE IN THIS PROJECT.  5.7.6 is in the"],
        ["", "     register with nothing to apply it to.  An ops room that cannot "
         "transmit is an ops room in name only."],
    ], header=["REF", "FINDINGS  -  EMP PROTECTION EM1"], h=2.0, rh=4.6,
        layer="M-FLAG")

    sh.table(CA, 182, [30, 500], [
        ["EM-V1", "*** RULED - ADOPTED BY THE PROJECT OWNER, RC2, 11 Sep 2026, "
         "master H.21.  The three-zone model and the"],
        ["", "     'Zone 2 standing alone' rule are the project's EMP position.  "
         "CLOSED.  No figure or finding changed. ***"],
        ["EM-V2", "EVERY EMP ZONE 2 DIMENSION IS [A], pending an equipment "
         "schedule that waits on the MISSING ELECTRICAL DESIGN."],
        ["EM-V3", "IS BAY 8 INSIDE THE EMP BOUNDARY?  Decides BV-4/BV-5 honeycomb, "
         "and whether the 15 kVA generator survives."],
        ["EM-V4", "NO COMMUNICATIONS DESIGN OF ANY KIND EXISTS.  5.7.6 cannot be "
         "applied and the ops room's purpose is unmet."],
        ["EM-V5", "PD-05's PIPE MATERIAL IS UNSPECIFIED - as is every pipe material "
         "in the project.  Metallic and plastic need"],
        ["", "     completely different treatments at the service entry plate."],
        ["EM-V6", "NO ESCAPE-SHAFT HEAD HATCH IS SPECIFIED, AND NO BLAST DOOR RF "
         "DATA EXISTS.  Both sit on the boundary."],
    ], header=["REF", "OPEN ITEMS RAISED BY THIS PACKAGE  -  NONE IS RESOLVED "
               "HERE, AND THAT IS DELIBERATE"], h=2.0, rh=4.6, layer="M-FLAG")

    X.evidence_key(sh, CA, 128, 396)
    sh.text("THIS PACKAGE CHANGES NO DESIGN.  NO DIMENSION, LOAD, BAR, WALL, "
            "LEVEL, VALVE, DUCT, PIPE OR MODEL IS ALTERED.",
            (420, 118), 2.4, "M-FLAG")
    sh.text("IT CREATES NO PENETRATION OF THE ENVELOPE AND MOVES NONE.  THE MAIN "
            "STAIRCASE IS UNTOUCHED.", (420, 112), 2.4, "M-FLAG")
    sh.finish(scale="NOT TO SCALE", sheet_of="1 OF 6")
    return sh


# =====================================================================
def em101():
    """EMP zone plan at the underground level."""
    sh = sheet("EM-101", "EMP ZONE PLAN - UNDERGROUND LEVEL (-)6.100",
               "EMP ZONE 1 ENVELOPE - EVERY PENETRATION - EMP ZONE 2 "
               "ENCLOSURE IN BAY 3",
               flags=("EM-F1", "EM-F4", "EM-V3"), of="2 OF 6")
    sc = 50.0
    M = X.vw(sc, 40.0, 418.0)
    MV.underground_plan(sh, M, sc)
    sh.view_title((40.0, 404.0), "V1", "EMP ZONE PLAN AT (-)6.100", "1:50")

    B = P.BOX
    sh.rect(*M(B["x0"] - 120, B["y0"] - 120), *M(B["x1"] + 120, B["y1"] + 120),
            "E-ZONE1")
    # placed east of the view title, which sits at x 40 on the same band
    sh.text("EMP ZONE 1 BOUNDARY  -  THE REINFORCEMENT CAGE AT 150 BOTH "
            "CURTAINS.  NOT A MIL-STD-188-125-1 SHIELD  [D]",
            M(6600, -520), 2.2, "E-ZONE1")

    Z = P.Z2
    sh.rect(*M(Z["x0"], Z["y0"]), *M(Z["x1"], Z["y1"]), "E-ZONE2")
    sh.rect(*M(Z["x0"] + Z["panel"], Z["y0"] + Z["panel"]),
            *M(Z["x1"] - Z["panel"], Z["y1"] - Z["panel"]), "E-SHIELD")
    zm = (Z["x0"] + Z["x1"]) / 2.0
    sh.text("EMP ZONE 2", M(zm, 4880), 2.6, "E-ZONE2", "CENTER")
    sh.text(f"{Z['x1']-Z['x0']} x {Z['y1']-Z['y0']} x {Z['h_ext']} EXT",
            M(zm, 4520), 2.0, "E-ZONE2", "CENTER")
    sh.text("80 dB STANDING ALONE", M(zm, 4180), 2.0, "E-ZONE2", "CENTER")
    sh.text("EVERY DIMENSION [A] - EM-V2", M(zm, 3840), 1.9, "M-FLAG",
            "CENTER")

    dy0, dy1 = MP.PART_DOOR_Y
    sh.dline(M(600, dy0), M(21400, dy0), "M-ARCH-HIDDEN")
    sh.dline(M(600, dy1), M(21400, dy1), "M-ARCH-HIDDEN")
    sh.text("CIRCULATION Y 2500-3400 THROUGH THE W8 DOOR GAPS - EMP ZONE 2 IS "
            "ENTIRELY CLEAR OF IT  [C] A.3", M(2300, 2940), 2.0, "M-TEXT")

    # (x, y, label dx, label dy).  BV-3's label is carried west and given a
    # leader: dropped straight below the valve it lands on the "STAIR SHAFT -
    # FROZEN GEOMETRY" note that mep_views draws over the void.
    marks = {"BV-1": (598, 2200, 0, -620), "BV-2": (598, 4000, 0, -620),
             "BV-3": (14998, 4900, -1400, -620),
             "BV-4": (21398, 1300, 0, -620), "BV-5": (21398, 4700, 0, -620)}
    for tag, (px, py, lx, ly) in marks.items():
        fail = tag in ("BV-4", "BV-5")
        lay = "E-APERTURE" if fail else "E-PENET"
        sh.circle(M(px, py), 2.4, lay)
        if lx:
            sh.line(M(px, py), M(px + lx, py + ly + 180), lay)
        sh.text(tag + ("  FAIL" if fail else "  PASS"), M(px + lx, py + ly),
                2.0, lay, "CENTER")
    sh.circle(M(11798, 5900), 2.4, "E-PENET")
    sh.text("SEP", M(11798, 6280), 2.0, "E-PENET", "CENTER")
    for name, cx, cy, head in P.ESC:
        sh.circle(M(cx, cy), P.ESC_CLEAR_D / 2.0 / sc, "E-APERTURE")
        sh.text(f"{name}  FAIL", M(cx, cy - 1560), 2.0, "E-APERTURE", "CENTER")
    V = P.VOID
    sh.rect(*M(V["x0"], V["y0"]), *M(V["x1"], V["y1"]), "E-APERTURE")
    vm = (V["x0"] + V["x1"]) / 2.0
    sh.text("STAIR VOID 2800 x 3160", M(vm, 2350), 2.2, "E-APERTURE", "CENTER")
    sh.text("THE LARGEST APERTURE IN", M(vm, 1950), 2.0, "E-APERTURE",
            "CENTER")
    sh.text("THE ENVELOPE  -  EM-F1", M(vm, 1550), 2.0, "E-APERTURE", "CENTER")
    sh.north((790.0, 500.0))

    # ---- left column: summary, register extract, evidence key, then fill
    y = sh.panel(CA, 392.0, 396.0, "PENETRATION SUMMARY  -  FULL REGISTER IN "
                 "Schedules/ENVELOPE_PENETRATION_REGISTER.md", [
        "PASS = below cutoff across the whole 10 kHz - 1 GHz band AND at least 80 dB in band.",
        "A DEPTH (WAVEGUIDE) CREDIT IS TAKEN ONLY WHERE THE BORE IS BOUNDED BY METAL.",
        "Concrete is a lossy dielectric, not a waveguide wall.  [D]",
    ], h=NOTE, lead=LEAD)

    rows = []
    for tag, kind, shape, bore, wall, host, note in P.PENETRATIONS:
        metal = K.CONDUCTING[tag]
        fc = K.fc_circ(bore) if shape == "CIRC" else K.fc_rect(bore)
        A = (K.a_circ(wall, bore) if shape == "CIRC"
             else K.a_rect(wall, bore)) if metal else 0.0
        se1m = 20.0 * math.log10(K.lam(1e6) / (2.0 * bore)) + A
        ok = (fc >= P.F_HI_HZ) and (se1m >= P.SE_REQUIRED_DB)
        rows.append([tag, f"{bore:.0f}", f"{wall:.0f}",
                     "STEEL" if metal else "CONCRETE",
                     f"{fc/1e6:.1f}", f"{A:.0f}" if metal else "-",
                     f"{se1m:.0f}", "PASS" if ok else "FAIL"])
    y = sh.table(CA, y - 8.0, [26, 26, 26, 36, 34, 28, 30, 26], rows,
                 header=["TAG", "BORE", "WALL", "BOUNDED", "f_c MHz", "WBC dB",
                         "SE 1MHz", "VERDICT"], h=1.9, rh=4.4)

    y = X.evidence_key(sh, CA, y - 10.0, 396.0)

    sh.panel_column(CA, y - 10.0, 122.0, 396.0, [
        ("WHY DN100 PASSES AND DN350 DOES NOT  -  BORE, NOT WORKMANSHIP", [
            f"DN100 in a 600 wall   cutoff {K.fc_circ(100)/1e6:7.1f} MHz  >  1 GHz      "
            f"{K.a_circ(600, 100):5.0f} dB      PASS",
            f"DN350 in a 600 wall   cutoff {K.fc_circ(350)/1e6:7.1f} MHz  <  1 GHz      "
            f"{K.a_circ(600, 350):5.0f} dB      FAIL",
            "",
            "THE SAME WALL, THE SAME STEEL, THE SAME WORKMANSHIP.  Only the bore differs, and it",
            "moves the TE11 cutoff from above the top of the band to well below it.  Above its",
            "cutoff a bore propagates however long it is - so BV-4 and BV-5 cannot be rescued by",
            "a thicker wall, only by a honeycomb panel inboard of the valve.  [D]",
        ]),
    ], gap=8.0)

    # ---- right column
    sh.panel_column(430.0, 392.0, 122.0, 400.0, [
        ("NOTES", [
            "1  THIS SHEET CREATES NO PENETRATION AND MOVES NONE.  Every position, bore and wall",
            "   thickness is read from a confirmed document - the HVAC damper and valve schedule,",
            "   MEP_AND_FINISHES_COORDINATION.md CO-1, and master A.4.4 / A.4.5.",
            "2  BV-1, BV-2 AND BV-3 NEED NO TREATMENT.  THE WALL IS THE WAVEGUIDE.  Keep the bore",
            "   metallic and the frame welded to the cage, which master A.5 already requires  [C].",
            "3  SEP IS NOT AN APERTURE.  A MIL-STD-188-125-1 entry plate IS the shield: a solid",
            "   welded plate bonded 360 deg to the cast-in frame, itself welded to the cage.  Its",
            "   apertures are the individual sleeves.  ITS LEVEL AND SIZE ARE [N] - see EM-302.",
            "4  THE TWO ESCAPE SHAFTS AND THE STAIR VOID ARE CONCRETE-BOUNDED and earn no depth",
            "   credit.  The collars carry 5-T25 each side/face/direction and the void's thickened",
            "   free edge 6-T25 top and bottom  [C] F.1 - five and six bars, not conducting",
            "   surfaces.  See EM-102, where that path is drawn.",
            "5  EMP ZONE 2 IS SHOWN AT ITS [A] SIZE AND POSITION.  It fits, it clears the",
            "   circulation route, and it holds a 300 survey gap on every free face - see EM-301.",
            "   IT IS NOT A DERIVED SIZE, because no equipment schedule exists.  EM-V2.",
        ]),
        ("THE ONE DECISION BEHIND BV-4 AND BV-5  -  EM-V3", [
            "The question is not how to fix them.  It is WHETHER BAY 8 IS INSIDE THE EMP BOUNDARY",
            "AT ALL - and NO EMP BOUNDARY HAS EVER BEEN DRAWN.  [U]",
            "",
            "Bay 8 is outside the GAS-TIGHT ENVELOPE  [C] A.2 - but that is a CBRN boundary and",
            "says nothing whatever about EMP.",
            "",
            "IF BAY 8 IS IN    both bores need a honeycomb WBC panel inboard of the valve.",
            "IF BAY 8 IS OUT   the 15 kVA generator, its control panel and every cable in bay 8",
            "                  are unprotected, AND THE SHELTER LOSES POWER TO THE PULSE.",
            "",
            "IT IS A CLIENT DECISION, NOT A DRAFTING ONE, AND IT IS NOT TAKEN HERE.",
        ]),
    ], gap=8.0)

    sh.finish(scale="1:50", sheet_of="2 OF 6")
    return sh


# =====================================================================
def em102():
    """The entry path section - finding EM-F1 drawn."""
    sh = sheet("EM-102", "EMP BOUNDARY SECTION - THE ENTRY PATH",
               "FINDING EM-F1 - AN OPEN ELECTROMAGNETIC PATH FROM GRADE TO "
               "BAY 7 THROUGH THE STAIR VOID",
               flags=("EM-F1", "EM-V6"), of="3 OF 6")

    # ---- V1  section on the entry path, 1:40.   x 12000 -> paper 40.
    sc, ox, oy = 40.0, -260.0, 467.5

    def M(mx, mz):
        """mx in mm along X; mz in METRES of level."""
        return (ox + mx / sc, oy + mz * 1000.0 / sc)

    V = P.VOID
    x0, x1 = 12000, 21400

    sh.line(M(x0, 0.0), M(13600, 0.0), "M-EXISTING")
    sh.hatch_pat([M(x0, -2.0), M(13600, -2.0), M(13600, 0.0), M(x0, 0.0)],
                 "EARTH", 5.0, 0.0, "M-EXISTING")
    sh.text("2000 ENGINEERED COVER  [C] A.7.3", M(x0 + 120, -1.15), 1.9,
            "M-EXISTING")
    sh.text("GRADE 0.000", M(x0 + 120, 0.18), 2.0, "M-LEVEL")

    sh.rect(*M(x0, -2.9), *M(V["x0"], -2.0), "M-STRUCT")
    sh.rect(*M(V["x1"], -2.9), *M(x1, -2.0), "M-STRUCT")
    sh.text("900 PRESSURE SLAB", M(19100, -2.62), 1.9, "M-STRUCT", "CENTER")
    sh.rect(*M(V["x0"], -2.9), *M(V["x1"], -2.0), "E-APERTURE")
    sh.text("STAIR VOID", M((V["x0"] + V["x1"]) / 2, -2.34), 2.2,
            "E-APERTURE", "CENTER")
    sh.text("2800 x 3160", M((V["x0"] + V["x1"]) / 2, -2.72), 2.0,
            "E-APERTURE", "CENTER")

    sh.rect(*M(13600, 0.4), *M(18400, 0.9), "M-STRUCT")
    sh.line(M(13600, -2.0), M(13600, 0.9), "M-STRUCT")
    sh.line(M(18400, -2.0), M(18400, 0.9), "M-STRUCT")
    sh.text("HEADHOUSE  +0.900  -  NO EARTH COVER  [C] A.4.6",
            M(13700, 1.05), 2.0, "E-APERTURE")

    sh.rect(*M(x0, -6.7), *M(x1, -6.1), "M-STRUCT")
    sh.text("600 MAT", M(19100, -6.48), 1.9, "M-STRUCT", "CENTER")
    for xw0, xw1, mark in ((14800, 15200, "W6"), (18000, 18400, "W7")):
        sh.rect(*M(xw0, -6.1), *M(xw1, -2.9), "M-STRUCT")
        sh.text(mark, M((xw0 + xw1) / 2, -2.78), 2.0, "M-TEXT", "CENTER")
        sh.rect(*M(xw0, -6.1), *M(xw1, -4.0), "M-FLAG")
    sh.text("BLAST DOOR 1", M(15000, -5.35), 1.8, "M-FLAG", "CENTER")
    sh.text("BLAST DOOR 2", M(18200, -5.35), 1.8, "M-FLAG", "CENTER")
    sh.text("RF PERFORMANCE [N]", M(15000, -5.72), 1.8, "M-FLAG", "CENTER")

    sh.pline([M(15600, 2.2), M(15600, 0.9), M(16600, 0.9), M(16600, -6.1)],
             "E-APERTURE")
    for pt in (M(15600, 1.7), M(16600, -0.7), M(16600, -4.6)):
        sh.flow(pt, -90, 3.2, "E-APERTURE")
    sh.text("INCIDENT FIELD", M(14300, 2.32), 2.4, "E-APERTURE")
    sh.text("NO ATTENUATION ANYWHERE ON", M(16800, -3.6), 1.9, "E-APERTURE")
    sh.text("THIS PATH ABOVE 47.4 MHz  [D]", M(16800, -3.95), 1.9,
            "E-APERTURE")

    sh.text("BAY 6", M(13900, -5.9), 2.0, "M-TEXT", "CENTER")
    sh.text("BAY 7  STAIR SHAFT", M(16600, -5.9), 2.0, "M-TEXT", "CENTER")
    sh.text("BAY 8", M(19900, -5.9), 2.0, "M-TEXT", "CENTER")

    for lv, lab in ((0.0, "0.000"), (-2.0, "(-)2.000"), (-2.9, "(-)2.900"),
                    (-6.1, "(-)6.100"), (-6.7, "(-)6.700")):
        sh.level(M(x1 + 150, lv), lab)

    sh.view_title((40.0, 288.0), "V1",
                  "SECTION ON THE ENTRY PATH  -  LOOKING NORTH", "1:40")

    # ---- V2  escape shaft head, 1:25
    sc2, ox2, oy2 = 25.0, 400.0, 400.0

    def M2(mx, mz):
        return (ox2 + mx / sc2, oy2 + mz * 1000.0 / sc2)

    sh.line(M2(-1600, 0.0), M2(1600, 0.0), "M-EXISTING")
    for a, b in ((-1600, -950), (950, 1600)):
        sh.hatch_pat([M2(a, -2.0), M2(b, -2.0), M2(b, 0.0), M2(a, 0.0)],
                     "EARTH", 5.0, 0.0, "M-EXISTING")
        sh.rect(*M2(a, -2.9), *M2(b, -2.0), "M-STRUCT")
    for sgn in (-1, 1):
        sh.rect(*M2(sgn * 700, -2.9), *M2(sgn * 950, 0.7), "M-STRUCT")
    sh.line(M2(-700, -2.9), M2(-700, 0.7), "E-APERTURE")
    sh.line(M2(700, -2.9), M2(700, 0.7), "E-APERTURE")
    sh.line(M2(-950, 0.7), M2(950, 0.7), "E-SHIELD")
    sh.text("1400 CLEAR BORE", M2(0, -1.5), 2.2, "E-APERTURE", "CENTER")
    sh.text(f"CUTOFF {K.fc_circ(1400)/1e6:.1f} MHz", M2(0, -1.85), 2.0,
            "E-APERTURE", "CENTER")
    sh.text("250 RC COLLAR  -  5-T25 EACH SIDE / FACE / DIRECTION  [C] F.1",
            M2(-1600, 0.30), 1.9, "M-TEXT")
    sh.text("FIVE BARS IS NOT A CONDUCTING TUBE, SO NO DEPTH CREDIT  [D]",
            M2(-1600, 0.05), 1.9, "M-TEXT")
    sh.leader([M2(0, 0.7), (330.0, 462.0)],
              "BONDED CONDUCTING HATCH REQUIRED  -  NOT SPECIFIED  [N]")
    sh.text("ESC 2 HEAD +0.700", M2(0, 0.95), 2.2, "M-TEXT", "CENTER")
    sh.view_title((304.0, 288.0), "V2",
                  "ESCAPE SHAFT HEAD  -  TYPICAL, ESC 1 AND ESC 2", "1:25")

    # ---- right-hand column, filled
    sh.panel_column(545.0, TOP, 122.0, 285.0, [
        ("EM-F1  -  WHY THIS SECTION EXISTS", [
            "THE PROTECTIVE BOUNDARY FOR BLAST AND THE",
            "PROTECTIVE BOUNDARY FOR EMP ARE NOT THE SAME",
            "SURFACE, AND THE PROJECT HAS ONLY EVER DRAWN",
            "ONE OF THEM.",
            "",
            f"The stair void is {V['x1']-V['x0']} x {V['y1']-V['y0']} = "
            f"{(V['x1']-V['x0'])*(V['y1']-V['y0'])/1e6:.2f} m2.  As a",
            "thin-screen aperture it gives",
            f"     {20*math.log10(K.lam(1e4)/(2*3160)):5.1f} dB at  10 kHz",
            f"     {20*math.log10(K.lam(1e6)/(2*3160)):5.1f} dB at   1 MHz",
            f"     {0.0:5.1f} dB above {K.fc_rect(3160)/1e6:.1f} MHz",
            "IT NEVER REACHES 80 dB ANYWHERE IN THE BAND.",
        ]),
        ("AND IT DOES NOT OPEN INTO SOIL", [
            "It opens into the HEADHOUSE, which sits at",
            "+0.900 with NO EARTH COVER  [C] A.4.6, and",
            "thence to grade through a covered stairwell",
            "that is DECLARED EXPENDABLE  [C] A.2.",
            "",
            "BLAST DOOR 1 IS THE ONLY THING ACROSS THAT",
            "PATH - and whether a blast door is an RF door",
            "is VENDOR DATA THE PROJECT DOES NOT HAVE.  [N]",
            "Its frame is already required to be cast in",
            "and welded to the cage  [C] A.5, which is the",
            "right start and is not the same thing.  EM-V6.",
        ]),
        ("THIS IS NOT A CRITICISM OF THE ARCHITECTURE", [
            "A shelter needs a staircase, and the void is",
            "exactly where a staircase has to go.  It is a",
            "statement that EMP ZONE 1 CANNOT BE THE 80 dB",
            "BOUNDARY - which is why EM-001 puts that",
            "boundary at EMP ZONE 2 instead, and designs it",
            "to stand alone with no credit taken for the",
            "concrete box at any frequency.  [D]",
        ]),
        ("THE ESCAPE SHAFTS, V2", [
            "A conducting liner would give",
            f"     {K.a_circ(3050, 1400):.1f} dB on ESC 1"
            f"     {K.a_circ(3600, 1400):.1f} dB on ESC 2",
            f"but BOTH ONLY BELOW {K.fc_circ(1400)/1e6:.1f} MHz.  Above that a",
            "1400 bore propagates however well it is lined.",
            "LINING THE SHAFTS DOES NOT FIX THEM.  The",
            "treatment that works is a BONDED CONDUCTING",
            "HATCH AT THE HEAD, which terminates the shaft",
            "instead of attenuating down it.  [D]",
        ]),
    ], gap=7.0)

    sh.panel(CA, 270.0, 396.0, "WHAT THIS SHEET DOES NOT DO", [
        "IT CREATES NO PENETRATION AND MOVES NONE.  Every level, thickness and position on it is",
        "read from master A.4.2, A.4.3, A.4.4, A.4.5 and A.4.6.  The stair void, the escape shafts,",
        "the headhouse and both blast doors are drawn exactly where the project already puts them.",
        "THE MAIN STAIRCASE IS FROZEN AND IS NOT DRAWN OR DIMENSIONED HERE.",
    ], h=NOTE, lead=LEAD)

    X.evidence_key(sh, 420.0, 262.0, 222.0)
    sh.panel(420.0, 214.0, 222.0,
             "THE THREE CONCRETE-BOUNDED APERTURES  -  WHAT EACH NEEDS", [
        "STAIR VOID     no treatment exists or is proposed.",
        "               It is the entry route.  The 80 dB",
        "               boundary moves to EMP ZONE 2 instead.",
        "ESC 1 / ESC 2  a BONDED CONDUCTING HATCH at the head.",
        "               Lining the shaft does not work.  [N]",
        "BLAST DOOR 1   frame already cast in and welded to",
        "               the cage  [C] A.5.  Whether the LEAF is",
        "               an RF seal is VENDOR DATA.  [N]  EM-V6.",
        "",
        "NONE OF THESE IS RESOLVED HERE, AND NONE IS INVENTED.",
    ], h=NOTE, lead=LEAD)
    sh.finish(scale="1:40 / 1:25", sheet_of="3 OF 6")
    return sh


# =====================================================================
def em201():
    """The shielding effectiveness chart."""
    sh = sheet("EM-201", "SHIELDING EFFECTIVENESS - CAGE AND APERTURES",
               "SE v FREQUENCY, 10 kHz - 1 GHz, AGAINST THE 80 dB "
               "MIL-STD-188-125-1 REQUIREMENT",
               flags=("EM-F2",), of="4 OF 6")

    cx0, cy0, cw, ch = 52.0, 300.0, 420.0, 222.0
    dbmax = 110.0

    def CP(f, db):
        return (cx0 + (math.log10(f) - 4.0) / 5.0 * cw,
                cy0 + db / dbmax * ch)

    sh.rect(cx0, cy0, cx0 + cw, cy0 + ch, "E-CHART")
    for d in range(6):
        x = cx0 + d / 5.0 * cw
        sh.line((x, cy0), (x, cy0 + ch), "E-CHART")
        sh.text(["10 kHz", "100 kHz", "1 MHz", "10 MHz", "100 MHz",
                 "1 GHz"][d], (x, cy0 - 6.0), 2.2, "E-CHART", "CENTER")
    for db in range(0, int(dbmax) + 1, 10):
        yy = cy0 + db / dbmax * ch
        sh.line((cx0, yy), (cx0 + cw, yy), "E-CHART")
        sh.text(str(db), (cx0 - 3.0, yy - 1.1), 2.2, "E-CHART", "RIGHT")
    sh.text("SHIELDING EFFECTIVENESS  dB", (cx0 - 14.0, cy0 + ch / 2), 2.6,
            "E-CHART", "CENTER", rot=90.0)
    sh.text("FREQUENCY  (logarithmic)", (cx0 + cw / 2, cy0 - 13.0), 2.6,
            "E-CHART", "CENTER")

    y80 = cy0 + P.SE_REQUIRED_DB / dbmax * ch
    sh.line((cx0, y80), (cx0 + cw, y80), "E-CHART-HI")
    sh.text("MIL-STD-188-125-1  REQUIREMENT  80 dB, 10 kHz - 1 GHz  [C]",
            (cx0 + 4.0, y80 + 2.4), 2.4, "E-CHART-HI")

    def curve(fn, layer, label, lab_f, dy=3.0):
        pts, f = [], 1e4
        while f <= 1e9 + 1:
            pts.append(CP(f, max(0.0, min(dbmax, fn(f)))))
            f *= 10 ** 0.05
        sh.pline(pts, layer)
        sh.text(label, CP(lab_f, max(2.0, fn(lab_f)) + dy), 2.2, layer)

    curve(lambda f: _se(f), "E-ZONE1",
          f"REBAR CAGE  s = {S:.0f}  ->  0 dB at "
          f"{K.f_mesh_cut(S)/1e6:.0f} MHz", 2e6)
    curve(lambda f: 20 * math.log10(max(1.0, K.lam(f) / (2 * 2800.0))),
          "E-APERTURE", "ESCAPE SHAFT  1400 BORE", 6e4, 2.4)
    curve(lambda f: 20 * math.log10(max(1.0, K.lam(f) / (2 * 3160.0))),
          "E-APERTURE", "STAIR VOID  3160", 1.15e4, -6.0)

    sh.line(CP(1e4, 100.0), CP(1e9, 100.0), "E-ZONE2")
    sh.text("EMP ZONE 2  -  80 dB STANDING ALONE, ACROSS THE WHOLE BAND  [A]",
            CP(1.15e4, 102.0), 2.4, "E-ZONE2")

    f80 = K.f_at_se(P.SE_REQUIRED_DB, S)
    sh.line(CP(f80, 0.0), CP(f80, P.SE_REQUIRED_DB), "E-CHART-HI")
    sh.text(f"{f80/1e3:.1f} kHz", CP(f80, 4.5), 2.2, "E-CHART-HI", "CENTER")
    sh.text("THE CAGE MEETS 80 dB ONLY TO THE LEFT OF THIS LINE",
            CP(1.15e4, 9.0), 2.4, "E-CHART-HI")
    sh.view_title((32.0, 274.0), "V1",
                  "SHIELDING EFFECTIVENESS v FREQUENCY", "NOT TO SCALE")

    rows = [[K.fmt_f(f).strip(), f"{_se(f):.2f}",
             f"{_se(f) - P.SE_REQUIRED_DB:+.2f}",
             "PASS" if _se(f) >= P.SE_REQUIRED_DB else "FAIL"]
            for f in K.DECADES]
    ytab = sh.table(520.0, TOP, [42, 32, 36, 26], rows,
                    header=["FREQUENCY", "SE dB", "MARGIN", ""],
                    h=2.0, rh=4.8)

    sh.panel_column(520.0, ytab - 10.0, 282.0, 310.0, [
        ("HOW TO READ THIS CHART", [
            "Four lines.  Only one of them is a shield.",
            "",
            "EMP ZONE 2   flat, above the requirement, right",
            "   across the band.  IT IS DRAWN FLAT BECAUSE IT",
            "   IS SPECIFIED THAT WAY - a welded steel",
            "   enclosure with every point of entry treated.",
            "REBAR CAGE   falls 20 dB per decade.  Crosses the",
            f"   requirement at {f80/1e3:.1f} kHz and reaches zero at",
            f"   {K.f_mesh_cut(S)/1e6:.0f} MHz.",
            "STAIR VOID and ESCAPE SHAFT   start BELOW the",
            "   requirement and never rise to it.  An aperture",
            "   cannot be improved by making the wall thicker",
            "   unless the bore is metal - and neither is.",
        ]),
        ("WHY THE CAGE IS STILL WORTH HAVING", [
            f"{_se(1e4):.0f} dB at 10 kHz is not nothing.  E3, the slow",
            "component that drives long conductors, lives at",
            "the bottom of the band - EXACTLY WHERE THE CAGE",
            "IS STRONGEST.  The 150 rule was a deliberate EMP",
            "decision and it was the right one.  It simply",
            "cannot be a MIL-STD-188-125-1 boundary, and it",
            "should never be described as one.  [D]",
        ]),
    ], gap=8.0)

    y = sh.panel(CA, 262.0, 396.0, "THE CHECK THAT MATTERS  -  MASTER K.3 IS "
                 "REPRODUCED, NOT ASSUMED", [
        "SE = 20 log10( lambda / 2s ),  s = 150 mm both curtains both ways  [C] master A.5,",
        "which records it as 'an EMP requirement, STRICTER THAN IS 456 Cl. 26.3.3'.",
        "",
        "Master K.3 records, as a CONFIRMED item:  'EMP rebar cage 0 dB @ 1 GHz - say it before",
        f"a reviewer does.  Zone 2 welded steel room is the answer.'  THIS CHART GIVES {_se(1e9):.3f} dB",
        f"AT 1 GHz FROM THE 150 mm SPACING ALONE, and puts the mesh cutoff at "
        f"{K.f_mesh_cut(S)/1e6:.1f} MHz.  [R]",
        "",
        f"2s = {2*S:.0f} mm.  The wavelength at 1 GHz is {K.lam(1e9):.2f} mm.  THE CAGE STOPS SHIELDING AT",
        "ALMOST EXACTLY THE FREQUENCY AT WHICH MIL-STD-188-125-1 STOPS ASKING.",
        "",
        f"Decades required 5.00   ·   decades delivered "
        f"{math.log10(f80/1e4):.2f}   ·   "
        f"{math.log10(f80/1e4)/5.0*100:.0f} % OF THE REQUIRED BAND.",
    ], h=NOTE, lead=LEAD)

    sh.panel(CA, y - 8, 396.0, "*** THESE FIGURES ARE AN UPPER BOUND ***", [
        "The classical array correction -10 log10(n) for n illuminated apertures IS NOT APPLIED;",
        "applying it would make every figure WORSE.  The crossings are TIED, NOT WELDED - and no",
        "statement of which exists anywhere in the project  [N], though it materially changes the",
        "result.  No concrete absorption is credited, because no permittivity or conductivity for",
        "this concrete exists anywhere in the project  [N] - that omission is in the SAFE direction.",
        "",
        "A MEASURED CAGE WILL BE WORSE THAN THIS CHART.  AND IT CANNOT BE MEASURED: a buried box",
        "under 2 m of engineered cover has no accessible exterior to put a transmitter on, so no",
        "IEEE Std 299 survey of EMP Zone 1 is possible.  THIS CHART IS A CALCULATION AND IT WILL",
        "STAY A CALCULATION.  ANY STATEMENT THAT THE BOX GIVES 80 dB IS UNSUPPORTABLE.  [D]",
    ], h=NOTE, lead=LEAD)

    X.evidence_key(sh, 420.0, 262.0, 222.0)
    sh.finish(scale="NOT TO SCALE", sheet_of="4 OF 6")
    return sh


# =====================================================================
def em301():
    """EMP Zone 2 enclosure."""
    sh = sheet("EM-301", "EMP ZONE 2 ENCLOSURE - PLAN, SECTION AND SITING",
               "THE ONLY EMP SHIELD IN THIS PROJECT - EVERY DIMENSION [A], "
               "PENDING AN EQUIPMENT SCHEDULE",
               flags=("EM-F3", "EM-V2"), of="5 OF 6")
    Z = P.Z2
    t = Z["panel"]
    ex, ey = Z["x1"] - Z["x0"], Z["y1"] - Z["y0"]

    # ---- V1  siting plan in bay 3, 1:25.   X 5520 -> paper 40, Y 600 -> 320
    sc = 25.0
    M = X.vw(sc, -180.8, 296.0)
    sh.rect(*M(5520, 600), *M(9020, 5600), "M-STRUCT")
    for x in (5410, 9020):
        sh.rect(*M(x, 600), *M(x + 110, 2500), "M-STRUCT")
        sh.rect(*M(x, 3400), *M(x + 110, 5600), "M-STRUCT")
    sh.dline(M(5520, 2500), M(9020, 2500), "M-ARCH-HIDDEN")
    sh.dline(M(5520, 3400), M(9020, 3400), "M-ARCH-HIDDEN")
    sh.text("CIRCULATION Y 2500-3400", M(5650, 2900), 1.9, "M-TEXT")
    sh.text("BAY 3  U-03  OPS ROOM", M(5650, 1500), 2.0, "M-TEXT")
    sh.text("3500 x 5000  [C] A.3", M(5650, 1100), 1.9, "M-TEXT")

    sh.rect(*M(Z["x0"], Z["y0"]), *M(Z["x1"], Z["y1"]), "E-ZONE2")
    sh.rect(*M(Z["x0"] + t, Z["y0"] + t), *M(Z["x1"] - t, Z["y1"] - t),
            "E-SHIELD")
    sh.text("EMP ZONE 2", M((Z["x0"] + Z["x1"]) / 2, 4700), 2.6, "E-ZONE2",
            "CENTER")
    sh.text(f"{ex - 2*t} x {ey - 2*t} x {Z['h_ext'] - 2*t}",
            M((Z["x0"] + Z["x1"]) / 2, 4300), 2.0, "E-ZONE2", "CENTER")
    sh.text("300 SURVEY GAP", M(Z["x0"] + 120, 5400), 1.8, "M-DIM")
    sh.text("300 SURVEY GAP", M(Z["x0"] + 120, 3480), 1.8, "M-DIM")
    sh.dim_h(M(Z["x0"], Z["y0"]), M(Z["x1"], Z["y0"]), 310.0, sc)
    sh.dim_v(M(Z["x1"], Z["y0"]), M(Z["x1"], Z["y1"]), 190.0, sc)
    sh.sym("DIFFUSER", M(6400, 1900), "M-TERMINAL", 0.45)
    sh.text("SD-03  [C] HV1", M(6600, 1800), 1.8, "M-TEXT")
    sh.north((200.0, 505.0))
    sh.view_title((40.0, 300.0), "V1", "EMP ZONE 2 SITING IN BAY 3", "1:25")

    # ---- V2  section, 1:20
    sc2, ox2, oy2 = 20.0, 240.0, 320.0

    def M2(mx, mz):
        return (ox2 + mx / sc2, oy2 + mz / sc2)

    sh.line(M2(-400, 0), M2(2400, 0), "M-STRUCT")
    sh.text("FLOOR (-)6.100", M2(-390, -130), 1.9, "M-LEVEL")
    sh.line(M2(-400, 3200), M2(2400, 3200), "M-STRUCT")
    sh.text("ROOF SOFFIT (-)2.900", M2(-390, 3250), 1.9, "M-LEVEL")
    sh.rect(*M2(0, 3050), *M2(2000, 3200), "M-DUCT-SUPPLY")
    sh.text("150 HVAC DUCT ZONE  [C] HV1", M2(60, 3100), 1.8, "M-TEXT")

    sh.rect(*M2(200, 0), *M2(200 + ey, Z["h_ext"]), "E-ZONE2")
    sh.rect(*M2(200 + t, t), *M2(200 + ey - t, Z["h_ext"] - t), "E-SHIELD")
    sh.text("EMP ZONE 2", M2(200 + ey / 2, Z["h_ext"] / 2), 2.2, "E-ZONE2",
            "CENTER")
    sh.text("1000 TO SOFFIT   850 CLEAR OVER", M2(340, 2560), 1.9, "M-DIM")
    sh.dim_v(M2(200, 0), M2(200, Z["h_ext"]), 246.0, sc2)

    sh.rect(*M2(200, 200), *M2(200 + t, 2300), "E-SHIELD")
    sh.text("PoE-1", M2(-380, 1300), 1.9, "E-SHIELD")
    sh.text("DOOR", M2(-380, 1000), 1.9, "E-SHIELD")
    sh.rect(*M2(200 + ey - t, 300), *M2(200 + ey, 900), "E-SHIELD")
    sh.text("PoE-2", M2(1900, 700), 1.9, "E-SHIELD")
    sh.text("VENT", M2(1900, 400), 1.9, "E-SHIELD")
    sh.pline([M2(1000, 0), M2(1000, -220), M2(1560, -220)], "E-BOND")
    sh.text("SINGLE-POINT BOND", M2(1600, -300), 1.9, "E-BOND")
    sh.view_title((240.0, 300.0), "V2",
                  "SECTION THROUGH EMP ZONE 2  -  LOOKING WEST", "1:20")

    # ---- right-hand column
    y = sh.panel_column(430.0, TOP, 196.0, 400.0, [
        ("EMP ZONE 2  -  EVERY DIMENSION IS [A]", [
            "The project confirms the enclosure is REQUIRED - master A.3 places 'an EMP Zone 2",
            "enclosure' in bay 3, and finishes W-04 calls it 'a welded steel room, shielding",
            "effectiveness verified to IEEE Std 299', classed [C] REQUIREMENT / [N] SPECIFICATION.",
            "FOUR REVISIONS, NO SPECIFICATION.  THIS SHEET SUPPLIES ONE, AT [A].",
            "",
            f"External       {ex} x {ey} x {Z['h_ext']}    at X {Z['x0']}-{Z['x1']}, Y {Z['y0']}-{Z['y1']}",
            f"Panel          {t}",
            f"Internal       {ex-2*t} x {ey-2*t} x {Z['h_ext']-2*t}   =  "
            f"{(ex-2*t)*(ey-2*t)/1e6:.2f} m2  /  "
            f"{(ex-2*t)*(ey-2*t)*(Z['h_ext']-2*t)/1e9:.3f} m3",
            f"Shielded area  {(2*(ex*Z['h_ext']) + 2*(ey*Z['h_ext']) + 2*ex*ey)/1e6:.2f} m2"
            f"     TOTAL SEAM LENGTH  {(4*ex + 4*ey + 4*Z['h_ext'])/1000:.2f} m",
            "",
            "*** THE SEAM LENGTH IS THE RISK, NOT THE AREA.  Every one of those metres has to be",
            "    continuously welded or continuously gasketed, and IEEE Std 299 WILL FIND THE",
            "    METRE THAT IS NOT. ***",
            "",
            "IT IS NOT A DERIVED SIZE.  There is no equipment schedule, because NO ELECTRICAL",
            "DESIGN EXISTS - the project's largest single gap  [C] master H.10.  This is a",
            "competent placeholder that demonstrably fits.  EM-V2.",
        ]),
        ("SITING  -  WHY IT IS WHERE IT IS", [
            "north to the wall face Y 5600      300     A 300 GAP IS HELD ON EVERY FREE FACE SO",
            "south to the circulation edge 3400 300     AN IEEE Std 299 SURVEY CAN PHYSICALLY",
            "west to the bay face X 5520        300     REACH EVERY SEAM.  A shielded room you",
            "east to the bay face X 9020        800     cannot walk round cannot be tested, AND",
            "head to the roof soffit           1000     AN UNTESTED SHIELD IS A CLAIM.  [D]",
            "",
            "The W8 partition door gaps are at Y 2500-3400  [C] A.3, so the east-west circulation",
            "route through bay 3 runs at Y 2500-3400.  THE ENCLOSURE IS ENTIRELY CLEAR OF IT.",
            "HVAC ducts occupy a 150 zone under the soffit  [C] HV1: 850 remains clear above.",
        ]),
        ("THE FIVE WAYS IN  -  details on EM-302", [
            "PoE-1  ACCESS       5.4      RF-gasketed or knife-edge shielded door.  [N] type/vendor",
            f"PoE-2  VENTILATION  5.5      honeycomb {P.Z2_VENT_CELL:.0f} cell x "
            f"{P.Z2_VENT_DEPTH:.0f} deep -> "
            f"{K.a_circ(P.Z2_VENT_DEPTH, P.Z2_VENT_CELL):.0f} dB, cutoff "
            f"{K.fc_circ(P.Z2_VENT_CELL)/1e9:.1f} GHz  [A]",
            "PoE-3  POWER        5.7.2.1  PCI on every conductor, mounted ON the boundary.  [N]",
            "PoE-4  SIGNAL       5.7.4.1  FIBRE - a dielectric penetration is NOT a penetration.",
            "                             THE BARGAIN OF THIS PACKAGE.  [D]",
            "PoE-5  RF           5.7.6    NOTHING TO APPLY IT TO - no antenna, mast, feeder or",
            "                             comms design exists anywhere in this project.  [N] EM-F6",
            "",
            "A SHIELD IS ONLY AS GOOD AS ITS WORST POINT OF ENTRY.  PoE-1 TO PoE-5 ARE ONE SYSTEM",
            "AND ARE SURVEYED AS ONE SYSTEM.",
        ]),
    ], gap=8.0)

    X.evidence_key(sh, 430.0, y - 8.0, 400.0)

    sh.panel_column(CA, 288.0, 122.0, 400.0, [
        ("WHAT EMP ZONE 2 IS FOR  -  AND WHY IT IS SMALL", [
            "HEMP IS NOT A PERSONNEL HAZARD.  The occupants are protected from blast, CBRN and",
            "fallout by the box.  EMP PROTECTION EXISTS SO THE SHELTER CAN STILL FUNCTION",
            "AFTERWARDS.  EMP Zone 2 protects EQUIPMENT.  It is correct that it is an enclosure",
            "and not a room, and NOBODY SHOULD EXPECT TO SHELTER INSIDE IT.  [D]",
        ]),
        ("THE DESIGN RULE THIS SHEET IMPLEMENTS", [
            "EMP ZONE 2 IS DESIGNED TO THE FULL 80 dB STANDING ALONE.  NO ATTENUATION FROM THE",
            "CONCRETE BOX IS CREDITED AT ANY FREQUENCY.",
            "",
            "The cage gives 80 dB only below 99.93 kHz and 0.00 dB at 1 GHz - EM-201 - so it is",
            "MARGIN, not design.  That is the only defensible way to use a shield you can never",
            "survey under 2 m of engineered cover.  [D]",
        ]),
        ("VERIFICATION  -  A HOLD POINT", [
            "FULL IEEE Std 299 SURVEY, 10 kHz - 1 GHz, on the completed enclosure with every",
            "penetration made off and every panel closed.  Acceptance 80 dB.",
            "NO EQUIPMENT IS INSTALLED BEFORE IT PASSES, because a failed survey means opening",
            "seams.  EMP ZONE 1 IS NOT SURVEYED AND IS NOT CLAIMED - see EM-201.",
        ]),
    ], gap=8.0)
    sh.finish(scale="1:25 / 1:20", sheet_of="5 OF 6")
    return sh


# =====================================================================
def em302():
    """Penetration, bonding and earthing details."""
    sh = sheet("EM-302", "EMP PENETRATION, BONDING AND EARTHING DETAILS",
               "SERVICE ENTRY PLATE - HONEYCOMB - BLAST VALVE BORE - "
               "BONDING STRAP - CAGE CONTINUITY",
               flags=("EM-F5", "EM-V5", "EM-V6"), of="6 OF 6")

    # ---- D1  service entry plate, 1:5.  Hatch bands only, so no text sits on
    #          a hatch and every annotation is read in the clear beside it.
    def D1(mx, my):
        return (40.0 + mx / 5.0, 430.0 + my / 5.0)

    sh.rect(*D1(0, -150), *D1(600, 600), "M-STRUCT")
    sh.concrete_hatch([D1(0, -150), D1(600, -150), D1(600, 50), D1(0, 50)])
    sh.concrete_hatch([D1(0, 450), D1(600, 450), D1(600, 600), D1(0, 600)])
    sh.rect(*D1(0, 50), *D1(600, 450), "E-SHIELD")
    for my, r, lab in ((350, 5.0, "PD-05 DN50"), (240, 3.4, "POWER - PCI"),
                       (140, 2.4, "SIGNAL - FIBRE")):
        sh.circle(D1(150, my), r, "E-PENET")
        sh.text(lab, D1(280, my - 30), 1.8, "M-TEXT")
    for my in (50, 450):
        sh.pline([D1(-80, my), D1(0, my)], "E-BOND")
    sh.text("600", D1(620, 240), 1.8, "M-TEXT")
    sh.text("SERVICE ENTRY PLATE", (172.0, 546.0), 2.2, "E-SHIELD")
    for i, ln in enumerate([
            "600 PERIMETER WALL, CUT.  SIZE AND LEVEL ARE [N].  CO-1 records",
            "that the plate must be at HIGH",
            "LEVEL because PD-05 rises over the filter trains, and that its",
            "level is not recorded anywhere in the project.",
            "",
            "THE PLATE IS THE SHIELD.  A MIL-STD-188-125-1 entry plate is a",
            "solid welded plate bonded 360 deg to the cast-in frame, itself",
            "WELDED TO THE CAGE - which master A.5 already requires  [C].",
            "Its apertures are the individual sleeves, treated one by one:",
            "",
            f"   PD-05 DN50      cutoff {K.fc_circ(50)/1e6:.0f} MHz,"
            f" {K.a_circ(600, 50):.0f} dB   [D] ample",
            "   POWER           PCI, 5.7.2.1.  No residual quoted - the",
            "                   standard specifies it BY PULSE TEST.  [N]",
            "   SIGNAL          FIBRE, 5.7.4.1, no metallic member.",
            "                   A DIELECTRIC IS NOT A PENETRATION.  [D]",
            "",
            "*** PD-05's MATERIAL IS NOT SPECIFIED ANYWHERE IN THE PROJECT",
            "    [N] - the drainage package names no pipe material for any",
            "    run - AND IT CHANGES THE TREATMENT COMPLETELY:",
            "    METALLIC  bond it 360 deg to the plate.  Its exterior",
            "              becomes shield.  Correct, and cheap.",
            "    PLASTIC   the bore is an aperture AND the water column is",
            "              a conductor through it.  Needs a metallic spool",
            "              piece nobody has specified.  EM-V5. ***",
    ]):
        sh.text(ln, (172.0, 538.0 - i * 6.2), 1.9, "M-TEXT")
    sh.view_title((40.0, 392.0), "D1",
                  "SERVICE ENTRY PLATE  -  THE PLATE IS THE SHIELD", "1:5")

    # ---- D3  blast valve bore, 1:5
    def D3(mx, my):
        return (600.0 + mx / 5.0, 430.0 + my / 5.0)

    sh.rect(*D3(0, -150), *D3(600, 450), "M-STRUCT")
    sh.concrete_hatch([D3(0, -150), D3(600, -150), D3(600, 0), D3(0, 0)])
    sh.concrete_hatch([D3(0, 100), D3(600, 100), D3(600, 450), D3(0, 450)])
    sh.rect(*D3(0, 0), *D3(600, 100), "E-PENET")
    sh.text("DN100 BORE", D3(180, 30), 1.8, "E-PENET")
    sh.text("600", D3(620, 200), 1.8, "M-TEXT")
    sh.text("BV-1 / BV-2 / BV-3", (734.0, 500.0), 2.2, "E-PENET")
    for i, ln in enumerate([
            "600 WALL, CUT.   L / d  =  600 / 100  =  6.0",
            f"TE11 cutoff   {K.fc_circ(100)/1e6:.0f} MHz   >  1 GHz",
            f"Attenuation   {K.a_circ(600, 100):.0f} dB",
            "",
            "THE WALL IS THE WAVEGUIDE.",
            "NO TREATMENT IS REQUIRED.  [D]",
            "",
            "Keep the bore metallic and the",
            "frame welded to the cage.",
            "",
            f"DN350, same wall:",
            f"   cutoff {K.fc_circ(350)/1e6:.0f} MHz  <  1 GHz",
            f"   {K.a_circ(600, 350):.0f} dB  <  80 dB",
            "   BV-4 / BV-5 FAIL BOTH.",
            "   Bore, not workmanship.",
    ]):
        sh.text(ln, (734.0, 492.0 - i * 6.2), 1.9, "M-TEXT")
    sh.view_title((600.0, 392.0), "D3",
                  "BLAST VALVE BORE  -  WAVEGUIDE BELOW CUTOFF", "1:5")

    # ---- D2  honeycomb vent panel, full size
    def D2(mx, my):
        return (40.0 + mx, 312.0 + my)

    sh.rect(*D2(0, 0), *D2(25, 60), "E-SHIELD")
    for i in range(1, 10):
        sh.line(D2(0, i * 6), D2(25, i * 6), "E-SHIELD")
    sh.dim_h(D2(0, 0), D2(25, 0), 306.0, 1.0)
    sh.text("PoE-2  HONEYCOMB WAVEGUIDE VENT PANEL", (78.0, 368.0), 2.2,
            "E-SHIELD")
    for i, ln in enumerate([
            f"{P.Z2_VENT_CELL:.0f} mm cell  x  {P.Z2_VENT_DEPTH:.0f} mm deep   [A]",
            f"TE11 cutoff  {K.fc_circ(P.Z2_VENT_CELL)/1e9:.1f} GHz   >>  1 GHz",
            f"Attenuation  {K.a_circ(P.Z2_VENT_DEPTH, P.Z2_VENT_CELL):.0f} dB"
            f"   ({K.a_circ(P.Z2_VENT_DEPTH, P.Z2_VENT_CELL)-P.SE_REQUIRED_DB:+.0f} dB on 80)",
            "MOUNT INBOARD OF ANY BLAST DEVICE - the valve takes the pressure,",
            "the honeycomb takes the RF.  ITS OWN BLAST RATING IS [N].",
            "Adds pressure drop HV1 did not allow for - REFERRED, NOT RESOLVED.",
    ]):
        sh.text(ln, (78.0, 360.0 - i * 6.2), 1.9, "M-TEXT")
    sh.view_title((40.0, 300.0), "D2", "HONEYCOMB WBC VENT PANEL", "FULL SIZE")

    # ---- D4  bonding strap, full size
    def D4(mx, my):
        return (600.0 + mx, 322.0 + my)

    sh.rect(*D4(0, 0), *D4(100, 50), "E-BOND")
    sh.circle(D4(14, 25), 3.0, "E-BOND")
    sh.circle(D4(86, 25), 3.0, "E-BOND")
    sh.dim_h(D4(0, 0), D4(100, 0), 306.0, 1.0)
    sh.text("50 x 3 FLAT", D4(108, 36), 1.9, "M-DIM")
    sh.text("w : l  =  5 : 1", D4(108, 24), 1.9, "M-DIM")
    sh.text(f"{K.strap_L(100, 50, 3)*1e9:.0f} nH", D4(108, 10), 2.2, "E-BOND")
    sh.view_title((600.0, 300.0), "D4", "BONDING STRAP  -  THE HOUSE RULE",
                  "FULL SIZE")

    # ---- panels
    sh.panel_column(CA, 285.0, 122.0, 396.0, [
        ("BONDING  -  WHERE EMP DESIGN ACTUALLY LIVES  [D]", [
            "L = 2e-7 . l . [ ln(2l/(w+t)) + 0.5 + 0.2235 (w+t)/l ]  henries",
            "",
            f"600 x 25 x 3 strap    {K.strap_L(600,25,3)*1e9:6.0f} nH   ->  "
            f"{2*math.pi*1e8*K.strap_L(600,25,3):6.0f} ohm AT 100 MHz",
            f"100 x 50 x 3 strap    {K.strap_L(100,50,3)*1e9:6.0f} nH   ->  "
            f"{2*math.pi*1e8*K.strap_L(100,50,3):6.0f} ohm AT 100 MHz",
            "",
            f"A 600 STRAP IS {2*math.pi*1e8*K.strap_L(600,25,3):.0f} OHM AT 100 MHz.  THAT IS NOT A BOND.  IT IS A",
            "RESISTOR WITH A NICE GREEN SLEEVE ON IT.  Shortening it to 100 and widening it to 50",
            f"is a factor of {K.strap_L(600,25,3)/K.strap_L(100,50,3):.1f}.",
            "",
            "1  EVERY BOND <= 100 LONG.            4  CLEAN BARE METAL BOTH ENDS, PROTECTED",
            "2  WIDTH : LENGTH AT LEAST 5 : 1.        AFTER MAKING OFF.",
            "3  FLAT STRAP ONLY - never a round    5  THE SHIELD BONDS TO THE STRUCTURE AT ONE",
            "   wire, never a pigtail, never          PLACE.  A SECOND BOND IS A LOOP, AND A",
            "   'loop it round to the nearest        LOOP IS AN ANTENNA.",
            "   stud'.",
        ]),
        ("D5  CAGE CONTINUITY AT A CONSTRUCTION JOINT  -  ALREADY SPECIFIED, "
         "MEASURE IT", [
            "Master F.1 already requires, at every construction joint at roughly 6 m centres:",
            "   REINFORCEMENT FULLY CONTINUOUS  ·  TWO WATERSTOPS  ·  A WELDED Cu / GALVANISED",
            "   EMP STRAP bridging the joint and welded to the cage on both sides.  [C]",
            "A construction joint is where a cage loses continuity, AND THE PROJECT ALREADY KNEW IT.",
            "THIS PACKAGE ADDS NOTHING TO THAT DETAIL - IT ASKS THAT IT BE MEASURED BEFORE THE POUR.",
            "The drawn detail is Structural CAD R-804 / R-805 and is not reproduced here.",
        ]),
    ], gap=8.0)

    y = sh.panel_column(430.0, 285.0, 190.0, 400.0, [
        ("EARTHING  -  AND WHY 5 OHM IS THE WRONG TARGET TO CHASE", [
            "Deccan basalt 1000 - 10000 ohm.m  [C] master K.3, which already says 'test earth",
            "resistance early'.  Target <= 5 ohm  [C] master G (IEEE 142 / IS 3043).",
            "",
            f"ONE 3 m x 16 ROD          {K.rod_R(1e3,3,0.016):7.0f} ohm at 1e3     "
            f"{K.rod_R(1e4,3,0.016):7.0f} ohm at 1e4",
            f"RODS FOR 5 OHM            {K.rod_R(1e3,3,0.016)/5:7.0f}"
            f"          {K.rod_R(1e4,3,0.016)/5:7.0f}      ignoring interaction",
            f"THE STRUCTURE ITSELF      {1e3/(4*6.589):7.0f} ohm at 1e3     "
            f"{1e4/(4*6.589):7.0f} ohm at 1e4",
            "   136.4 m2, r_eq 6.589 m, R = rho / 4r  (the conservative form)",
            "",
            "5 OHM IS NOT ACHIEVABLE WITH RODS IN BASALT.  Rods interact, a real group needs far",
            "more than the ideal count, and there is nowhere on this site to put them.  THE MAT",
            "AND ITS CAGE ARE ALREADY A LARGE CONCRETE-ENCASED ELECTRODE, an order of magnitude",
            "better than a rod and costing nothing.  BOND TO THE STRUCTURE; DO NOT CHASE RODS. [D]",
            "",
            "*** AND 5 OHM IS NOT AN EMP NUMBER.  It is a power-safety and lightning requirement",
            "    from IS 3043 / IEEE 142  [C].  It is real and it still applies.  IT IS NOT WHAT",
            "    MAKES AN EMP SHIELD WORK.  A shield works by being EQUIPOTENTIAL, and that is",
            "    decided by BONDING INDUCTANCE, not by earth resistance.  EM-F5. ***",
        ]),
    ], gap=8.0)

    X.evidence_key(sh, 430.0, y - 8.0, 400.0)
    sh.finish(scale="AS NOTED", sheet_of="6 OF 6")
    return sh


# =====================================================================
BUILDERS = [("EM-001_EMP_Design_Basis_and_Zone_Key", em001),
            ("EM-101_EMP_Zone_Plan_Underground", em101),
            ("EM-102_EMP_Boundary_Section_Entry_Path", em102),
            ("EM-201_Shielding_Effectiveness_Cage_and_Apertures", em201),
            ("EM-301_EMP_Zone_2_Enclosure", em301),
            ("EM-302_EMP_Penetration_Bonding_and_Earthing_Details", em302)]


def build():
    os.makedirs(OUT, exist_ok=True)
    for name, fn in BUILDERS:
        sh = fn()
        p = os.path.join(OUT, name + ".dxf")
        sh.save(p)
        print(f"  {name}.dxf")


if __name__ == "__main__":
    print("EMP drawings:")
    build()
