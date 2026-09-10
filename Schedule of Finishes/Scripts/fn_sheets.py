"""
fn_sheets.py  --  the Schedule of Finishes drawing set.

    A-601  Finish legend, notes, the four rules and typical junction details
    A-611  Entry level finish plan
    A-612  Underground level finish plan
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "Drainage",
                                                "Scripts")))
import mep_dxf as X
import mep_proj as P
import mep_views as V
import fn_data as F

T = X.TXT
OUT = os.path.abspath(os.path.join(HERE, "..", "DXF"))
NOTE, LEAD = 2.4, 4.3
CA, CB, CC = 14.0, 286.0, 558.0
WA, WB, WC = 264.0, 264.0, 268.0
TOP = 552.0


def sheet(num, title, sub, flags=(), of=""):
    return X.Sheet(num, title, sub, package="SCHEDULE OF FINISHES",
                   rev=P.REV["finishes"], flags=flags, sheet_of=of)


def fintag(sh, p, room, f, w, c, s, layer="A-FIN-TAG", th=None):
    """Four-part finish tag:  room / F  W / C  S."""
    th = th or 2.0
    # QA1: "W-01 + W-04" is wider than a 13 mm half-cell at 2.0 mm, so the wall
    # and ceiling halves ran into each other.  Tag widened, lower row sized to
    # the cell it sits in.
    bw, bh = 34.0, 11.0
    x, y = p
    sh.rect(x, y, x + bw, y + bh, layer)
    sh.line((x, y + bh / 2.0), (x + bw, y + bh / 2.0), layer)
    sh.line((x + bw / 2.0, y), (x + bw / 2.0, y + bh), layer)
    sh.text(room, (x + bw / 4.0, y + bh * 0.62), th, "A-FIN-TAG", "CENTER")
    sh.text(f, (x + bw * 0.75, y + bh * 0.62), th, "A-FIN-FLOOR", "CENTER")
    th2 = min(th, 1.75)
    sh.text(w, (x + bw / 4.0, y + bh * 0.14), th2, "A-FIN-WALL", "CENTER")
    sh.text(c + "/" + s, (x + bw * 0.75, y + bh * 0.14), th2, "A-FIN-CEIL",
            "CENTER")


# =====================================================================
def a601():
    sh = sheet("A-601", "FINISH LEGEND, NOTES AND TYPICAL JUNCTION DETAILS",
               "EVERY CODE IS A PERFORMANCE REQUIREMENT - THE PRODUCT IS "
               "LEFT OPEN",
               flags=("FN-D1", "FN-D2", "FN-U1", "C16"), of="1 OF 3")

    # ---------------- column A : the warning and the four rules
    y = sh.panel(CA, TOP, WA, "1   WHAT THIS SCHEDULE IS, AND WHAT IT IS NOT", [
        "*** NO FINISH SPECIFICATION EXISTS ANYWHERE IN THIS PROJECT. ***",
        "",
        "The master, the ten Rev F architectural drawings, sheet S-06 and the",
        "Structural CAD package between them fix concrete grade, cover,",
        "waterproofing, crack control and bar spacing.  They fix NOTHING about",
        "what a surface is finished with.",
        "",
        "THIS SCHEDULE THEREFORE DOES NOT REPORT FINISHES AS PROJECT FACTS.",
        "",
        "Every code on this sheet is a PERFORMANCE REQUIREMENT derived from",
        "something the project DOES confirm - the exposure class, the",
        "decontamination duty, the gas-tight envelope, the EMP requirement, the",
        "wet areas, the frozen stair geometry.  THE PRODUCT THAT SATISFIES IT",
        "IS LEFT OPEN.",
        "",
        "Wherever a thickness, a product, a colour or a manufacturer would",
        "normally appear, this set says PROVISIONAL - VERIFY or ENGINEER TO",
        "CONFIRM.  It does not invent one.  See panel 4.",
    ], h=NOTE, lead=LEAD)

    for ref, rule, why in F.RULES:
        lines = []
        for chunk in (rule, "", why):
            lines += _wrap(chunk, 74)
        y = sh.panel(CA, y - 6, WA, f"RULE {ref}", lines, h=NOTE, lead=LEAD)

    # ---------------- column B : the codes
    sh.text("2   FINISH CODES   -   every code defined", (CB, TOP - 3.4),
            T["panel_head"], "M-TITLE")
    rows = []
    for grp, src in (("FLOOR", F.FLOORS), ("SKIRTING", F.SKIRTINGS),
                     ("WALL", F.WALLS), ("CEILING", F.CEILINGS)):
        for code, desc, perf, why, cls in src:
            rows.append((code, desc[:44], cls))
    for code, desc, perf, why, cls in F.DOORS:
        rows.append((code, desc[:44], cls))
    for row in F.WATERPROOFING + [F.WP_EXTRA]:
        rows.append((row[0], row[1][:44], "[C]"))
    yB = sh.table(CB, TOP - 8, [26, 178, 56], rows,
                  header=["CODE", "DESCRIPTION", "CLASS"], h=2.1, rh=5.6,
                  layer="M-TABLE")

    # ---------------- column C : requirements and their source
    sh.text("3   WHERE EACH REQUIREMENT COMES FROM", (CC, TOP - 3.4),
            T["panel_head"], "M-TITLE")
    y = sh.table(CC, TOP - 8, [26, 216], [
        ("F-01", "Gas-tight CBRN envelope, bays 1-6  [C master A.2]"),
        ("F-02", "Wet areas.  Grout lines are a decontamination failure"),
        ("F-03", "Master A.5 designates the STAIR SHAFT FACES a WET / DIRTY"),
        ("", "     ZONE - it is why their cover is 30 and not 40  [C]"),
        ("F-04", "Bay 8 generator, the grey zone  [C master A.3]"),
        ("F-05", "Headhouse floor IS the top of the 900 pressure slab, with a"),
        ("", "     hose-down point and a confirmed 1:80 gully fall  [C]"),
        ("F-06", "Covered stairwell - outside the protective boundary and"),
        ("", "     DECLARED EXPENDABLE  [C master A.2]"),
        ("W-04", "Master A.3 places an EMP ZONE 2 enclosure in bay 3; K.3"),
        ("", "     records the rebar cage gives 0 dB at 1 GHz and 'a Zone 2"),
        ("", "     welded steel room is the answer'  [C]"),
        ("D-01", "Blast doors 1 and 2, the PROTECTIVE BOUNDARY  [C]"),
        ("D-05", "*** W5 IS CONFIRMED FIRE + GAS-TIGHT BUT NO DOOR IS"),
        ("", "     SCHEDULED IN IT ANYWHERE IN THE PROJECT, and the decon"),
        ("", "     airlock must have a clean-side exit.  FN-U1  ***"),
        ("WP-01", "R-805 - tanking membrane, a continuous tank  [C]"),
        ("WP-02", "R-805 / A.7.3 - 100 protection screed over the roof  [C]"),
        ("WP-03", "master A.5 - integral crystalline admixture  [C]"),
        ("WP-05", "R-804 - two waterstops at every construction joint  [C]"),
    ], header=["CODE", "SOURCE"], h=2.1, rh=5.6, layer="M-TABLE")

    sh.text("4   WHAT IS NOT SPECIFIED, AND WHY", (CC, y - 8),
            T["panel_head"], "M-TITLE")
    yC = sh.table(CC, y - 13, [110, 100, 32],
                  [(i[:52], r[:48], c) for i, r, c in F.NOT_SPECIFIED],
                  header=["ITEM", "REASON", "CLASS"], h=2.1, rh=6.4,
                  layer="M-TABLE")

    # ---------------- bottom band : typical junction details
    yy = min(y, yB, yC) - 10.0
    yy = min(yy, 250.0)
    sh.view_title((CA, yy), "D1", "COVED FLOOR / WALL JUNCTION  -  RULE R4",
                  "SCALE 1:10")
    M = X.vw(10.0, CA + 80, yy - 40.0)
    sh.rect(*M(-600, 0), *M(0, 900), "M-STRUCT")
    sh.concrete_hatch([M(-600, 0), M(0, 0), M(0, 900), M(-600, 900)])
    sh.rect(*M(0, -260), *M(1400, 0), "M-STRUCT")
    sh.concrete_hatch([M(0, -260), M(1400, -260), M(1400, 0), M(0, 0)])
    sh.pline([M(0, 750), M(0, 150), M(150, 0), M(1400, 0)], "A-FIN-WET")
    sh.text("F-02 / S-01 COVED IN ONE PIECE, 150 HIGH", M(220, 220), NOTE,
            "A-FIN-WET")
    sh.text("W-02 IMPERVIOUS TO FULL HEIGHT", M(220, 820), NOTE, "A-FIN-WALL")
    sh.text("WP-04 TANKING UNDER THE FINISH,", M(220, 500), NOTE,
            "M-WATERPROOF")
    sh.text("TURNED UP 150", M(220, 340), NOTE, "M-WATERPROOF")
    sh.text("*** NO BUTT JOINT AT THE FLOOR - IT IS THE ONE PLACE",
            M(-600, -600), NOTE, "M-FLAG")
    sh.text("    A HOSE CANNOT REACH ***", M(-600, -820), NOTE, "M-FLAG")

    sh.view_title((CB, yy), "D2", "CAST-IN FIXING  -  RULE R2", "SCALE 1:10")
    N = X.vw(10.0, CB + 90, yy - 34.0)
    sh.rect(*N(-700, -500), *N(700, 300), "M-STRUCT")
    sh.concrete_hatch([N(-700, -500), N(700, -500), N(700, 300), N(-700, 300)])
    sh.rect(*N(-120, 0), *N(120, 300), "M-STEELWORK" if False else "M-DAMPER")
    sh.line(N(-700, -100), N(700, -100), "A-FIN-TAG")
    sh.text("REINFORCEMENT - 40 COVER, 150 SPACING BOTH", N(-700, -280), NOTE,
            "A-FIN-TAG")
    sh.text("CURTAINS, AN EMP REQUIREMENT  [C]", N(-700, -440), NOTE,
            "A-FIN-TAG")
    sh.text("CAST-IN SOCKET", N(200, 200), NOTE, "M-DAMPER")
    # QA1: this flag block sat above the detail and ran through the D2 title
    sh.text("*** NO DRILLED ANCHOR ANYWHERE IN THE TANKED", N(-700, -700), NOTE,
            "M-FLAG")
    sh.text("    ENVELOPE.  IT RISKS THE 40 COVER, THE MEMBRANE", N(-700, -860),
            NOTE, "M-FLAG")
    sh.text("    AND THE EMP CAGE - ALL THREE ***", N(-700, -1020), NOTE,
            "M-FLAG")

    sh.panel(CC, yy, 242, "D3   FLOOR BUILD-UP  -  RULE R3", [
        "The floor finish is part of the DRAINAGE design, not a separate",
        "decision:",
        "",
        "    600 MAT, top at (-)6.100  -  a structural surface inside the tank.",
        "        Falls are NEVER cut into it.",
        "    SCREED to falls, 25 mm at the outlet rising to 78 mm at the far",
        "        corner.  Transverse 1:80 wet / 1:100 dry over 2500; the spine",
        "        falls 1:400 east to the sump.",
        "    F-01 / F-02 / F-03 / F-04 applied over.",
        "",
        "AREA-AVERAGE 52 mm  =  1.24 kPa  against a 1.0 kPa MAT SIDL ALLOWANCE.",
        "EXCESS 0.24 kPa = 25 kN over the 104 m2 floor - 1.2 % of the mat's own",
        "weight, 0.4 % of the 6289 kN uplift, and acting in the FAVOURABLE",
        "direction for flotation.",
        "",
        "*** REFERRED TO THE STRUCTURAL ENGINEER AS DRAINAGE FINDING DR-F4.",
        "    A HEAVIER FINISH SPENDS AN ALLOWANCE THAT IS ALREADY EXCEEDED. ***",
        "",
        "The finished clear height is therefore 3122 to 3175 mm against the",
        "3200 STRUCTURAL clear height (DR-F2).  A number quoted to a client",
        "must say which of the two it is.",
    ], h=NOTE, lead=LEAD)

    X.evidence_key(sh, CA, 100)
    V.scope_note(sh, CB, 100, WB)
    sh.finish(scale="1:10 / NTS", sheet_of="1 OF 3")
    return sh


def _wrap(s, n):
    if not s:
        return [""]
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


# =====================================================================
def a611():
    sh = sheet("A-611", "ENTRY LEVEL FINISH PLAN",
               "COVERED STAIRWELL 0.000 AND (-)2.000  -  HEADHOUSE (-)2.000",
               flags=("C16", "FN-D1"), of="2 OF 3")

    sc = 50.0
    M = X.vw(sc, 60.0, 380.0)
    sh.view_title((20, 553), "V1", "ENTRY LEVEL FINISH PLAN",
                  "SCALE 1:50   FINISH TAGS IN EVERY SPACE   "
                  "ROOM / FLOOR over WALL / CEILING-SKIRTING")
    V.ground_plan(sh, M, sc, box_below=True)

    tags = {"G-01": (10250, 6750), "G-02": (12650, 6750),
            "G-03": (15050, 6750), "G-04": (15600, 3000),
            "G-05": (16600, 2200)}
    for n, nm, l, a, f, s, w, c, d, wp, wet, sp, rm in F.ROOMS:
        if n in tags:
            x, yq = tags[n]
            px, py = M(x, yq)
            fintag(sh, (px - 13, py - 5), n, f, w, c, s)
    sh.text("G-01  TOP LANDING 0.000", M(10250, 8300), NOTE, "M-TEXT", "BC")
    sh.text("G-02  FLIGHT 12R @ 166.6667 / 300  -  F-06 NON-SLIP, CAST NOSING",
            M(12650, 8000), NOTE, "M-TEXT", "BC")
    sh.text("G-03  PLATFORM (-)2.000  -  WET", M(15050, 8300), NOTE,
            "A-FIN-WET", "BC")
    sh.text("G-04  HEADHOUSE (-)2.000  -  11.15 m2 USABLE  -  WET, "
            "HOSE-DOWN, FALL 1:80 CONFIRMED", M(15600, 1400), NOTE,
            "A-FIN-WET", "BC")
    sh.text("G-05  STAIR VOID EDGE  -  1100 GUARDING  [C]", M(16600, 800),
            NOTE, "M-FLAG", "BC")
    sh.text("*** C16 - ROOF OVER THE PLATFORM RULED AT 250, CLOSED RC1. "
            "THE FINISH DOES NOT DEPEND ON IT; THE DRIP AT THE JUNCTION DOES ***",
            M(9250, 9000), NOTE, "M-FLAG")
    sh.dim_h(M(P.ASW["x0"], 4800), M(P.ASW["x1"], 4800), M(0, 4200)[1], sc=sc)
    sh.dim_h(M(P.HH["x0"], 3400), M(P.HH["x1"], 3400), M(0, 2800)[1], sc=sc)
    V.north(sh, (620, 470))

    y = sh.panel(CA, 330, 620, "NOTES  -  ENTRY LEVEL FINISHES", [
        "1  THE HEADHOUSE FLOOR IS THE TOP OF THE 900 PRESSURE SLAB AT (-)2.000.  It is NOT a separate slab",
        "   (Rev F ground plan note 1).  F-05 is applied direct to it, to the CONFIRMED 1:80 fall to GY-11.",
        "   That gully discharges to an EXTERNAL SOAKAWAY and NEVER to the clean sump - a confirmed",
        "   instruction, not a preference: the headhouse is outside the gas-tight envelope.",
        "2  THE COVERED STAIRWELL IS OUTSIDE THE PROTECTIVE BOUNDARY AND IS DECLARED EXPENDABLE (master A.2).",
        "   Its finishes are an access and durability provision, not a protective one.  F-06 non-slip is",
        "   nevertheless the most important finish on this sheet - it is the only entry route.",
        "3  THE NOSING ON G-02 IS CAST IN, NOT APPLIED.  An applied strip changes the effective going.",
        "4  1100 GUARDING TO THE STAIR VOID EDGE is confirmed on the Rev F ground plan and required by",
        "   NBC 2016 Part 4.  Its finish is galvanised or coated steel; its HEIGHT is not a finish decision.",
        "5  THE 300 CHANNEL AND GRATING at the threshold, the flush threshold and the 50 weather bar are all",
        "   confirmed on Rev F section C-C and are shown on DRAINAGE D-103.  No finish crosses the channel.",
        "6  C16 - THE ROOF OVER THE PLATFORM IS RULED AT 250 AND CLOSED (RC1 10.09.26, master Part H.14).",
        "   A.4.7's clause that said 500 has been CORRECTED; the model, Part B, A.7.6, F.2 and this sheet all",
        "   said 250 already.  NO FINISH ON THIS SHEET EVER DEPENDED ON IT.  With the ruling at 250 there is",
        "   NO STEP in the soffit above G-03, so NO DRIP IS REQUIRED.",
        "7  ALL FINISHES ON THIS SHEET ARE PERFORMANCE REQUIREMENTS.  No product, thickness or colour is",
        "   specified anywhere in this package - see A-601 panel 4.",
    ], h=NOTE, lead=LEAD)

    sh.text("V2   ENTRY LEVEL ROOM FINISH SCHEDULE", (CA, y - 9),
            T["view_title"], "M-TITLE")
    yT = sh.table(CA, y - 17, [26, 74, 30, 26, 26, 26, 26, 26, 30, 26, 250],
                  [(n, nm[:26], ("-" if l is None else f"({l:+.3f})"),
                    ("-" if a is None else f"{a:.2f}"), f, s, w, c, d,
                    ("WET" if wet else "-"), rm[:88])
                   for n, nm, l, a, f, s, w, c, d, wp, wet, sp, rm in F.ROOMS
                   if n.startswith("G-")],
                  header=["ROOM", "NAME", "LEVEL", "AREA", "F", "S", "W", "C",
                          "DOOR", "WET", "REMARKS"], h=2.1, rh=6.2,
                  layer="M-TABLE")
    X.evidence_key(sh, CA, yT - 8)
    sh.finish(scale="1:50", sheet_of="2 OF 3")
    return sh


# =====================================================================
def a612():
    sh = sheet("A-612", "UNDERGROUND LEVEL FINISH PLAN",
               "LEVEL (-)6.100  -  WET AREAS, THE CLEAN ZONE AND THE GREY "
               "ZONE",
               flags=("FN-U1", "FN-D1", "DR-F4"), of="3 OF 3")

    sc = 45.0
    M = X.vw(sc, 40.0, 400.0)
    sh.view_title((20, 553), "V1", "UNDERGROUND LEVEL FINISH PLAN",
                  "SCALE 1:45   FLOOR (-)6.100   FINISH TAGS IN EVERY SPACE")
    V.underground_plan(sh, M, sc, bays=True, rooms=False, stair=True, esc=True)

    centres = {"U-01": 2050, "U-02": 4510, "U-03": 7270, "U-04": 10030,
               "U-05": 11820, "U-06": 13800, "U-07": 16600, "U-08": 19900}
    for n, nm, l, a, f, s, w, c, d, wp, wet, sp, rm in F.ROOMS:
        if n not in centres:
            continue
        px, py = M(centres[n], 3100)
        fintag(sh, (px - 13, py - 5), n, f, w, c, s)
        for i, part in enumerate(_wrap(nm, 18)):
            sh.text(part, M(centres[n], 4900 - i * 380), NOTE, "M-TEXT", "BC")
        if wet:
            sh.text("WET AREA", M(centres[n], 1500), NOTE, "A-FIN-WET", "BC")
            sh.text("WP-04 + F-02 + W-02", M(centres[n], 1100), NOTE,
                    "A-FIN-WET", "BC")
        sh.text(f"{a:.2f} m2", M(centres[n], 2100), NOTE, "M-TEXT", "BC")

    sh.text("ZONE 1  CLEAN  -  DECONTAMINABLE THROUGHOUT", M(6000, 5850),
            NOTE, "A-FIN-FLOOR", "BC")
    sh.text("ZONE 2  DECON", M(13800, 5850), NOTE, "A-FIN-WET", "BC")
    sh.text("ZONE 3  GREY", M(19700, 5850), NOTE, "M-FLAG", "BC")
    sh.text("W-04  EMP ZONE 2 ENCLOSURE - SPECIALIST", M(7270, 5450), NOTE,
            "M-FLAG", "BC")
    sh.text("MAIN STAIRCASE - GEOMETRY FROZEN.  24R @ 170.8333 / 280.",
            M(16600, 1600), NOTE, "M-FLAG", "BC")
    sh.text("F-03 TREADS, CAST-IN NOSING, NO BUILD-UP", M(16600, 1250), NOTE,
            "M-FLAG", "BC")
    sh.dim_h(M(0, -1400), M(22000, -1400), M(0, -2200)[1], sc=sc)

    y = sh.panel(CA, 358, 620, "NOTES  -  UNDERGROUND FINISHES", [
        "1  RULE R1 - NO SUSPENDED CEILING, NO DRY LINING, NO BOXING-IN AND NO CAVITY OF ANY KIND ANYWHERE IN",
        "   THE GAS-TIGHT ENVELOPE.  Three independent confirmed reasons: HVAC requires every duct inspectable",
        "   along its whole length, including the raw-air duct that is the only barrier between the clean zone",
        "   and unfiltered air (HV-F2); DRAINAGE requires the same of every pipe and trap; and a void is a",
        "   contamination trap that cannot be decontaminated.  EVERY FINISH IS APPLIED DIRECT TO THE CONCRETE.",
        "2  RULE R2 - NO FIXING IS DRILLED INTO THE TANKED ENVELOPE.  CAST-IN SOCKETS AND FRAMES ONLY.  The",
        "   internal cover is 40 and the bar spacing is 150 in both curtains as an EMP requirement; the",
        "   membrane and the crystalline admixture are the waterproofing; the cage is the EMP shield.  A",
        "   drilled anchor risks all three.  Bunks, handrails, trays, duct supports and door frames: CAST IN.",
        "3  RULE R3 - THE FLOOR FINISH IS PART OF THE DRAINAGE DESIGN.  Falls, screed thickness and the 25-78 mm",
        "   build-up are set in DRAINAGE calculation D.15 and are already constrained by the 1.0 kPa mat SIDL",
        "   allowance (finding DR-F4, referred to the structural engineer).  A heavier finish spends an",
        "   allowance that is already exceeded.  See A-601 detail D3.",
        "4  RULE R4 - EVERY JUNCTION IN A WET OR CLEAN AREA IS COVED, NOT BUTTED.  Floor to wall, wall to",
        "   soffit, and around every gully and pipe sleeve.  See A-601 detail D1.",
        "5  WET AREAS ARE U-02, U-05 AND U-06.  Each takes WP-04 tanking under F-02, W-02 to full height, a",
        "   coved S-01 skirting, and falls coordinated with DRAINAGE D-201.  U-06, the decon airlock, is the",
        "   dirtiest surface in the shelter and its gullies are SEGREGATED throughout.",
        "6  U-05 - THERE IS 110 mm CLEAR AT THE SIDES OF EACH FILTER TRAIN (1450 wide in a 1560 clear bay).",
        "   DO NOT THICKEN THE WALL FINISH IN THIS BAY.  HVAC finding HV-F3.",
        "7  U-07 - MASTER A.5 DESIGNATES THE STAIR SHAFT FACES A WET / DIRTY ZONE, which is why their cover is",
        "   30 and not 40.  F-03 non-slip decontaminable throughout.  THE STAIR GEOMETRY IS FROZEN: 24R @",
        "   170.8333 / 280, 3 flights x 8, rise 4100.  The nosing is CAST IN and the tread finish has NO",
        "   BUILD-UP - an applied nosing or a thick tread finish changes the going, and the going is frozen.",
        "8  U-03 - THE EMP ZONE 2 ENCLOSURE IS SPECIALIST.  Master K.3 confirms the requirement and that a",
        "   welded steel room is the answer; ITS SPECIFICATION IS NOT IN THE PROJECT.  Its finish is",
        "   subordinate to its shielding effectiveness, which is verified to IEEE Std 299, not by inspection.",
        "9  FN-U1 - W5 IS CONFIRMED AS FIRE AND GAS-TIGHT BUT NO DOOR IS SCHEDULED IN IT ANYWHERE IN THE",
        "   PROJECT, yet the decon airlock must have a clean-side exit.  D-05 is scheduled as a requirement",
        "   with NO SIZE AND NO POSITION.  ENGINEER TO CONFIRM.",
    ], h=NOTE, lead=LEAD)

    sh.text("V2   UNDERGROUND ROOM FINISH SCHEDULE", (CA, y - 9),
            T["view_title"], "M-TITLE")
    yT = sh.table(CA, y - 17, [26, 70, 30, 26, 24, 24, 30, 24, 30, 24, 258],
                  [(n, nm[:24], f"({l:+.3f})", f"{a:.2f}", f, s, w, c, d,
                    ("WET" if wet else "-"), rm[:92])
                   for n, nm, l, a, f, s, w, c, d, wp, wet, sp, rm in F.ROOMS
                   if n.startswith("U-")],
                  header=["ROOM", "NAME", "LEVEL", "AREA", "F", "S", "W", "C",
                          "DOOR", "WET", "REMARKS"], h=2.1, rh=6.2,
                  layer="M-TABLE")
    X.evidence_key(sh, CA, yT - 8)
    sh.finish(scale="1:45", sheet_of="3 OF 3")
    return sh


SHEETS = [(a601, "A-601_Finish_Legend_Notes_and_Typical_Details"),
          (a611, "A-611_Entry_Level_Finish_Plan"),
          (a612, "A-612_Underground_Level_Finish_Plan")]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, name in SHEETS:
        fn().save(os.path.join(OUT, name + ".dxf"))
        print("  ", name + ".dxf")
