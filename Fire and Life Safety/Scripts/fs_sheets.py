"""fs_sheets.py  --  the two escape plan drawings.

    F-101  underground level escape plan, level (-)6.100
    F-102  entry level escape plan and the vertical escape profile

The architectural background, the sheet standard, the A1 border and the title
block are the project's existing ones - mep_dxf.Sheet, which subclasses
sc_dxflib.Sheet - so these two sheets are the same drawing standard as the
issued D, M and A-6xx series.  Nothing about the building is redrawn here.

WHAT THESE SHEETS DO NOT DO.  They do not invent a door in W5, a ladder in an
escape shaft, a detector, an alarm, an extinguisher position, a muster point or
a fire compartment line.  None of those exists in the project.  Where the route
needs one, the drawing says so on its face and carries the [N] class.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.normpath(os.path.join(HERE, "..", "..",
                                                 "Drainage", "Scripts")))
import mep_dxf as X                                        # noqa: E402
import mep_proj as P                                       # noqa: E402
import mep_views as V                                      # noqa: E402
import fs_data as F                                        # noqa: E402

T = X.TXT
OUT = os.path.abspath(os.path.join(HERE, "..", "DXF"))
NOTE, LEAD = 2.4, 4.3
CA, WA = 14.0, 408.0                # left column below the plan
CB, WB = 430.0, 401.0               # right column

FIRE_LAYERS = {
    "F-ESCAPE":  (3, 50, "Escape route - primary, direction of travel"),
    "F-SHAFT":   (4, 40, "Escape shaft route - secondary"),
    "F-BARRIER": (1, 50, "Fire barrier - the blast doors, the only real ones"),
    "F-GAP":     (1, 40, "Route crosses something that does not exist"),
}


class FSheet(X.Sheet):
    """An A1 fire and life safety sheet."""

    DATE = F.DATE

    def __init__(self, number, title, subtitle="", flags=(), of=""):
        super().__init__(number, title, subtitle, package=F.PACKAGE,
                         rev=F.REV, flags=list(flags), sheet_of=of)
        for name, (col, lw, desc) in FIRE_LAYERS.items():
            ly = self.doc.layers.add(name)
            ly.color = col
            ly.lineweight = lw
            ly.description = desc

    def route(self, M, pts, layer="F-ESCAPE", every=34.0):
        """A walking line in model coordinates, with travel arrows on it."""
        pp = [M(*p) for p in pts]
        self.pline(pp, layer)
        for a, b in zip(pp, pp[1:]):
            dx, dy = b[0] - a[0], b[1] - a[1]
            L = (dx * dx + dy * dy) ** 0.5
            if L < 6.0:
                continue
            import math
            ang = math.degrees(math.atan2(dy, dx))
            n = max(1, int(L // every))
            for i in range(n):
                t = (i + 0.5) / n
                self.flow((a[0] + dx * t, a[1] + dy * t), ang, 2.8, layer)
        return pp


def sheet(num, title, sub, flags=(), of=""):
    return FSheet(num, title, sub, flags=flags, of=of)


# =====================================================================
def f101():
    sh = sheet("F-101", "UNDERGROUND LEVEL ESCAPE PLAN",
               "LEVEL (-)6.100  -  THREE ROUTES, TRAVEL DISTANCES, THE TWO "
               "FIRE BARRIERS",
               flags=("FS-1", "FS-2", "FS-3", "FS-6"), of="1 OF 2")

    sc = 33.0
    M = X.vw(sc, 40.0, 330.0)
    sh.view_title((20, 553), "V1", "UNDERGROUND LEVEL ESCAPE PLAN",
                  "SCALE 1:33   LEVEL (-)6.100   ALL DIMENSIONS mm   LEVELS m"
                  "   ROUTES ARE WALKING LINES, NOT SETTING OUT")
    V.underground_plan(sh, M, sc, bays=True, rooms=True, stair=True, esc=True)

    # ---- R1, the primary route -------------------------------------
    sh.route(M, F.R1_SPINE)
    sh.route(M, F.R1_TO_DOOR)
    sh.route(M, F.R1_STAIR)
    sh.route(M, F.R1_W5, "F-GAP", every=3.0)      # the crossing that is not there
    sh.text("R1  PRIMARY", M(7300, F.SPINE_Y + 260), NOTE, "F-ESCAPE", "BC")
    sh.text("UP", M(F.W6_X1 + 800, F.BDOOR_Y - 500), 2.8, "F-ESCAPE", "BC")

    # ---- R2 and R3, the two shafts ---------------------------------
    sh.route(M, F.R2, "F-SHAFT", every=8.0)
    sh.route(M, F.R3, "F-SHAFT", every=14.0)
    sh.route(M, F.R3_FROM_BD2, "F-SHAFT", every=14.0)
    sh.text("R2", M(F.ESC1_X, F.ESC1_Y + 1250), 2.8, "F-SHAFT", "BC")
    sh.text("R3", M(F.ESC2_X, F.ESC2_Y + 1250), 2.8, "F-SHAFT", "BC")

    # ---- the two real barriers -------------------------------------
    for mark, x0, x1 in (("BLAST DOOR 1", F.W6_X0, F.W6_X1),
                         ("BLAST DOOR 2", F.W7_X0, F.W7_X1)):
        sh.rect(*M(x0, P.BLAST_DOOR["y0"]), *M(x1, P.BLAST_DOOR["y1"]),
                "F-BARRIER")
        sh.leader([M((x0 + x1) / 2.0, P.BLAST_DOOR["y0"]),
                   M((x0 + x1) / 2.0, -350)], None)
        sh.text(mark, M((x0 + x1) / 2.0, -700), 2.2, "F-BARRIER", "BC")

    # ---- FS-1, the crossing the project does not contain ------------
    sh.leader([M(F.W5_X0, F.SPINE_Y), M(9020, 4150)], None)
    for i, ln in enumerate((
            "FS-1   W5 IS FIRE AND GAS-TIGHT AND HAS NO DOOR",
            "ANYWHERE IN THE PROJECT.  R1 HAS TO CROSS IT.",
            "THE CROSSING SHOWN IS INDICATIVE ONLY AND IS",
            "NOT A DESIGN   [N]")):
        sh.text(ln, M(7270, 4900 - i * 400), NOTE, "M-FLAG", "BC")

    # ---- FS-3, the coupling nobody had stated ----------------------
    sh.text("FS-3   ESC 2 SHARES BAY 8", M(F.ESC2_X, 4450), NOTE, "M-FLAG", "BC")
    sh.text("WITH THE GENERATOR  [C]", M(F.ESC2_X, 4030), NOTE, "M-FLAG", "BC")

    # ---- travel dimension and the two spine facts -------------------
    sh.dim_h(M(P.INT["x0"], 0), M(F.W6_X1, 0), M(0, -1400)[1], sc=sc)
    CX = M(11000, 0)[0]
    sh.text(f"LONGEST TRAVEL TO R1  =  {F.TRAVEL_R1:.1f} m  [D]  -  WEST "
            f"INTERNAL FACE OF BAY 1 TO THE BAY 7 FACE OF W6",
            (CX, 274.0), NOTE, "M-DIM", "BC")
    sh.text(f"SPINE  {F.SPINE_LEN:.1f} m INTERNAL.  BAYS 1 TO 6 ARE ONE SMOKE "
            f"COMPARTMENT, FS-2  [C]", (CX, 263.5), NOTE, "M-FLAG", "BC")
    sh.text("BLAST DOORS 1 AND 2 ARE THE ONLY TWO REAL FIRE BARRIERS IN THE "
            "SHELTER  [C]", (CX, 253.0), NOTE, "F-BARRIER", "BC")

    # ---- immediate actions, in the strip beside the plan ------------
    V.north(sh, (773, 522))
    sh.panel(715, 494, 116, "ROUTE KEY", [
        "R1   MAIN STAIR",
        f"     {F.TRAVEL_R1:.1f} m travel",
        f"     {F.CLIMB_R1:.3f} m climb",
        "R2   ESC 1 SHAFT",
        f"     {F.TRAVEL_R2:.2f} m travel",
        f"     {F.CLIMB_R2:.3f} m climb",
        "R3   ESC 2 SHAFT",
        f"     {F.TRAVEL_R3:.2f} m travel",
        f"     {F.CLIMB_R3:.3f} m climb",
        "",
        "R1 IS A STAIR.",
        "R2 AND R3 ARE",
        "SHAFTS, NOT EXITS.",
    ], h=2.0, lead=3.4)

    # ================= panels and schedules =========================
    y = sh.panel(CA, 242, WA, "FINDINGS THIS DRAWING IS OBLIGED TO SHOW  -  "
                 "IT DOES NOT RESOLVE ANY OF THEM",
                 [f"{k}   {v}" for k, v in F.FINDINGS],
                 h=2.0, lead=LEAD)

    y = sh.table(CA, y - 7, [13, 60, 128, 28, 28, 151],
                 [(r[0], r[1], r[2], r[3], r[4], r[5] + "   " + r[6])
                  for r in F.ROUTES],
                 header=["", "ROUTE", "GEOMETRY", "TRAVEL", "CLIMB",
                         "EMERGES AT / EVIDENCE"], h=2.0, rh=6.4,
                 layer="M-TABLE", max_w=WA)

    y = sh.table(CA, y - 7, [84, 94, 230], list(F.DECISION),
                 header=["FIRE IN", "ROUTE", "WHY  -  FROM THE PLAN 4.2"],
                 h=2.0, rh=6.4, layer="M-TABLE", max_w=WA)

    sh.panel(CA, y - 8, WA, "IMMEDIATE ACTIONS  -  FROM THE PLAN 4.3", [
        "1  RAISE THE ALARM BY VOICE.  There is no alarm system, and there is "
        "no electrical design for one to",
        "   come from.  In a 20.8 m shelter with 9 occupants and permanently "
        "open 900 partition gaps, voice carries.",
        "2  ATTACK IT ONLY WHILE IT IS SMALL, and only if the route behind you "
        "is clear.",
        "3  SHUT THE BLAST DOOR BETWEEN YOU AND THE FIRE  -  Blast Door 1 in "
        "W6 or Blast Door 2 in W7.  They are",
        "   the only real barriers in the shelter, and shutting one needs no "
        "system, no power and no design that",
        "   does not already exist.",
        "4  STOP THE GENERATOR if the fire is in Bay 8 or of unknown origin.",
        "5  EVACUATE BY THE ROUTE THE DECISION RULE GIVES.  Do not pass the "
        "fire to reach a preferred route.",
        "6  ROLL CALL: 9.  The occupancy is a confirmed project figure, so the "
        "count is unambiguous.",
        "   MUSTER POINT NOT DEFINED  -  no site plan exists, master open item "
        "D3  [N].",
    ], h=2.0, lead=LEAD)

    y = sh.panel(CB, 242, WB, "LEGEND, AND THE LIMITS OF THIS SHEET", [
        "ROUTE R1, PRIMARY  -  heavy line with travel arrows.  The only route "
        "that is a stair rather than a",
        "   shaft, and the only one usable by an injured or unconscious person.",
        "ROUTES R2 AND R3, THE ESCAPE SHAFTS  -  lighter line.  They are "
        "shafts, not exits.  Last resort.",
        "THE SHORT DENSE-ARROWED LEG THROUGH W5  -  THE ROUTE CROSSES "
        "SOMETHING THAT DOES NOT EXIST.  See FS-1.",
        "BLAST DOORS 1 AND 2  -  heavy, on F-BARRIER.  The only fire barriers "
        "in the shelter.",
        "TRAVEL DISTANCES are walking lines along the spine at the centre of "
        "the permanent 900 partition gaps,",
        "   measured from the internal faces of the box.  They are not setting "
        "out.  Class [D].",
        "",
        "NOT ON THIS SHEET, BECAUSE THE PROJECT DOES NOT CONTAIN IT  [N]:  "
        "fire detection, alarm, emergency",
        "lighting, extinguisher positions, suppression of any kind, smoke "
        "compartment lines other than the two",
        "blast doors, a muster point, or fire service access.  Detection, "
        "alarm and lighting all follow the",
        "missing electrical design (FS-5); the muster point and the access "
        "follow the missing site plan (D3).",
        "NOTHING IS INVENTED HERE TO FILL ANY OF IT.",
    ], h=2.0, lead=LEAD)

    sh.panel(CB, y - 7, WB, "POLICY CLAUSES THAT ARE ABOUT THIS DRAWING", [
        "THE BLAST DOORS ARE THE FIRE STRATEGY.  Shutting the door between the "
        "occupants and the fire is the",
        "   single most effective action available, and it needs no system, no "
        "power and no design that does",
        "   not already exist.",
        "W5 MUST BE GIVEN ITS DOOR.  Until it is, the fire separation between "
        "the CBRN plant bay and the decon",
        "   airlock does not exist, and R1 crosses an opening nobody has "
        "designed.",
        "ESC 2 IS NOT AN ESCAPE ROUTE FROM A GENERATOR FIRE.  It is in the "
        "fire compartment.",
    ], h=2.0, lead=LEAD)

    X.evidence_key(sh, CB, 128)

    sh.finish(scale="1:33", sheet_of="1 OF 2")
    return sh


# =====================================================================
def f102():
    sh = sheet("F-102", "ENTRY LEVEL ESCAPE PLAN AND VERTICAL PROFILE",
               "THE SURFACE END OF R1  -  THE TWO SHAFT HEADS  -  THE CLIMB "
               "EACH ROUTE ACTUALLY IS",
               flags=("FS-3", "FS-6", "D3"), of="2 OF 2")

    sc = 38.0
    M = X.vw(sc, 40.0, 300.0)
    sh.view_title((20, 553), "V1", "ENTRY LEVEL ESCAPE PLAN",
                  "SCALE 1:38   LEVELS 0.000 AND (-)2.000   THE BURIED BOX IS "
                  "SHOWN DASHED BELOW")
    V.ground_plan(sh, M, sc, box_below=True)

    # ---- R1 continues from F-101 -----------------------------------
    sh.rect(*M(P.VOID["x0"], P.VOID["y0"]), *M(P.VOID["x1"], P.VOID["y1"]),
            "M-ARCH-HIDDEN")
    sh.route(M, F.ENTRY_ROUTE, every=22.0)
    sh.text("MAIN STAIR ARRIVES (-2.000)", M(16600, 4550), NOTE,
            "F-ESCAPE", "BC")
    sh.text("FROM F-101", M(16600, 4150), NOTE, "F-ESCAPE", "BC")
    sh.text("R1  CONTINUED", M(10250, F.ASW_CL_Y + 500), NOTE, "F-ESCAPE", "BC")
    sh.leader([M(F.HH_DOOR_X, 5750), M(15900, 5250)], None)
    sh.text(f"INNER SECURITY DOOR IN HW2, {P.HH_DOOR['w']} x "
            f"{P.HH_DOOR['h']}  [C]", M(16750, 5100), NOTE, "M-FLAG", "BC")
    sh.text(f"ENTRY DOOR {P.ASW['door'][0]} x {P.ASW['door'][1]} AT GRADE  [C]",
            M(8600, 6750), NOTE, "F-ESCAPE", "RIGHT")

    # ---- the two shaft heads ---------------------------------------
    for name, cx, cy, head in P.ESC:
        sh.circle(M(cx, cy), P.ESC_CLEAR_D / 2.0 / sc, "F-SHAFT")
        sh.circle(M(cx, cy), P.ESC_COLLAR_OD / 2.0 / sc, "F-SHAFT")
        sh.text(f"{name} HEAD ({head:+.3f})", M(cx, cy + 1450), NOTE,
                "F-SHAFT", "BC")
        sh.text("EMERGES THROUGH THE 2 000 COVER  [C]", M(cx, cy - 1750),
                NOTE, "F-SHAFT", "BC")
    sh.text("FS-6   NO LADDER, RUNG OR FALL-ARREST IS SPECIFIED IN EITHER "
            "SHAFT  [N]", M(11000, 4600), NOTE, "M-FLAG", "BC")

    # ---- the covered stairwell run ---------------------------------
    sh.dim_h(M(P.ASW["top_landing"][0], P.ASW["y1"]),
             M(P.ASW["platform"][1], P.ASW["y1"]), M(0, 8000)[1], sc=sc)
    sh.text(f"COVERED STAIRWELL RUN  {F.ASW_RUN:.1f} m  -  LANDING, FLIGHT "
            f"AND PLATFORM  [C]", M(12650, 8400), NOTE, "M-DIM", "BC")

    # ---- the two facts about the surface end ------------------------
    sh.text("THE COVERED STAIRWELL AND THE HEADHOUSE ARE OUTSIDE THE "
            "PROTECTIVE BOUNDARY  [C]", M(300, 8700), NOTE, "M-TEXT")
    sh.text("MUSTER POINT NOT DEFINED  -  NO SITE PLAN EXISTS, MASTER OPEN "
            "ITEM D3  [N]", M(300, 8100), NOTE, "M-FLAG")

    # ================= V2, the vertical escape profile ==============
    sh.view_title((636, 553), "V2", "VERTICAL ESCAPE PROFILE",
                  "SCALE 1:75 VERTICAL   NOT A SECTION   WHAT EACH ROUTE "
                  "ACTUALLY ASKS OF THE PERSON USING IT")
    VS = 13.333                       # paper mm per metre  (1:75)
    Y0 = 415.0                        # paper y of level 0.000
    XL, XR = 640.0, 760.0

    def lv(level):
        return Y0 + level * VS

    for level, lab, dy in [(P.LVL["asw_head"], "COVERED STAIRWELL HEAD", 0.0),
                           (F.ESC2_HEAD, "ESC 2 HEAD", 0.0),
                           (F.ESC1_HEAD, "ESC 1 HEAD", 2.6),
                           (0.000, "GRADE  -  ENTRY DOOR", -3.0),
                           (P.LVL["slab_top"], "HEADHOUSE  -  STAIR ARRIVAL", 0.0),
                           (P.LVL["L2"], "LANDING L2", 0.0),
                           (P.LVL["L1"], "LANDING L1", 0.0),
                           (F.FLOOR, "SHELTER FLOOR", 0.0)]:
        sh.dline((XL, lv(level)), (XR, lv(level)), "M-LEVEL")
        sh.text(f"({level:+.3f})  {lab}", (XR + 3.0, lv(level) - 0.8 + dy),
                1.9, "M-LEVEL")

    for x, tag, top, col in ((664.0, "R1", 0.000, "F-ESCAPE"),
                             (700.0, "R2", F.ESC1_HEAD, "F-SHAFT"),
                             (736.0, "R3", F.ESC2_HEAD, "F-SHAFT")):
        sh.pline([(x, lv(F.FLOOR)), (x, lv(top))], col)
        for f in (0.28, 0.62, 0.88):
            sh.flow((x, lv(F.FLOOR) + (lv(top) - lv(F.FLOOR)) * f), 90.0,
                    2.8, col)
        sh.text(tag, (x, lv(F.FLOOR) - 6.4), 2.8, col, "CENTER")

    sh.text(f"{P.STAIR['risers']}R @ {P.STAIR['riser']:.4f}",
            (660.0, lv(-4.15)), 1.9, "F-ESCAPE", "RIGHT")
    sh.text(f"RISE {P.STAIR['total_rise']}, FROZEN", (660.0, lv(-4.50)),
            1.9, "F-ESCAPE", "RIGHT")
    sh.text(f"{P.ASW['risers']}R @ {P.ASW['riser']:.4f}", (660.0, lv(-0.85)),
            1.9, "F-ESCAPE", "RIGHT")
    sh.text("RISE 2000  [D]", (660.0, lv(-1.20)), 1.9, "F-ESCAPE", "RIGHT")
    sh.text(f"CLIMB {F.CLIMB_R2:.3f} m", (696.0, lv(-2.55)), 1.9, "F-SHAFT",
            "RIGHT")
    sh.text("NO LADDER  [N]", (696.0, lv(-2.90)), 1.9, "M-FLAG", "RIGHT")
    sh.text(f"CLIMB {F.CLIMB_R3:.3f} m", (732.0, lv(-5.30)), 1.9, "F-SHAFT",
            "RIGHT")
    sh.text("NO LADDER  [N]", (732.0, lv(-5.65)), 1.9, "M-FLAG", "RIGHT")
    sh.text("R1 IS THE ONLY ROUTE THAT IS A STAIR.", (XL, lv(-7.30)), 2.1,
            "M-TEXT")
    sh.text("R2 AND R3 ARE SHAFTS, AND THE PROJECT DOES NOT SAY HOW THEY ARE "
            "CLIMBED.", (XL, lv(-7.65)), 2.1, "M-FLAG")

    # ================= panels and schedules =========================
    y = sh.table(CA, 288, [13, 116, 52, 30, 161, 36], list(F.EMERGE),
                 header=["", "WHERE THE ROUTE ENDS", "OPENING", "LEVEL",
                         "WHAT THAT MEANS", "CLASS"],
                 h=2.0, rh=6.4, layer="M-TABLE", max_w=WA)

    y = sh.panel(CA, y - 7, WA, "THE SURFACE END OF THE PRIMARY ROUTE", [
        f"R1 REACHES GRADE IN TWO STAGES.  {P.STAIR['risers']}R @ "
        f"{P.STAIR['riser']:.4f} from the floor (-6.100) to the headhouse at "
        f"(-2.000)  -  the frozen main",
        f"   staircase, annotated and never altered  -  then "
        f"{P.ASW['risers']}R @ {P.ASW['riser']:.4f} up the covered stairwell "
        f"to the entry door at 0.000.",
        f"   {F.CLIMB_R1:.3f} m of climb in total  [C] / [D].",
        f"HORIZONTAL TRAVEL ON THIS LEVEL IS {F.TRAVEL_ENTRY:.1f} m  [D], "
        f"stair arrival to entry door, measured along the walking",
        "   line through the inner security door in HW2.",
        "BOTH SURFACE STRUCTURES ARE OUTSIDE THE PROTECTIVE BOUNDARY, and the "
        "covered stairwell is declared",
        "   EXPENDABLE in the project record.  A fire in either blocks R1's "
        "surface end and leaves only R2 and R3  -",
        "   which is why the decision rule on F-101 sends a headhouse or "
        "stairwell fire to the shafts.",
    ], h=2.0, lead=LEAD)

    sh.panel(CA, y - 7, WA, "ROUTE R1, STEP BY STEP  -  EVERY ELEMENT "
             "CONFIRMED UNLESS MARKED", [
        "1  ALONG THE SPINE to Bay 7, through the permanent 900 partition "
        "gaps at Y 2500-3400.",
        "2  THROUGH W5.  NO DOOR EXISTS IN W5 ANYWHERE IN THE PROJECT  [N].  "
        "See F-101 and FS-1.",
        "3  THROUGH BLAST DOOR 1 in W6, 1200 x 2100, 7 bar.  Shut it behind "
        "you if the fire is west of it.",
        f"4  UP THE MAIN STAIR, {P.STAIR['risers']}R @ "
        f"{P.STAIR['riser']:.4f}, {P.STAIR['flights']} flights of "
        f"{P.STAIR['per_flight']}, {P.STAIR['width']} wide, rise "
        f"{P.STAIR['total_rise']}, headroom {P.STAIR['headroom']}.",
        "      FROZEN GEOMETRY  -  annotated on these sheets and never altered.",
        f"5  INTO THE HEADHOUSE at ({P.LVL['slab_top']:+.3f}), then through "
        f"the inner security door in HW2, {P.HH_DOOR['w']} x "
        f"{P.HH_DOOR['h']}.",
        f"6  ACROSS THE PLATFORM and UP THE COVERED STAIRWELL, "
        f"{P.ASW['risers']}R @ {P.ASW['riser']:.4f}, {P.ASW['width']} wide, "
        f"rise 2000.",
        f"7  OUT THE ENTRY DOOR, {P.ASW['door'][0]} x {P.ASW['door'][1]}, at "
        f"grade.  MUSTER POINT NOT DEFINED  [N]  -  see D3.",
    ], h=2.0, lead=LEAD)

    X.evidence_key(sh, CA, 143)

    sh.panel(CB, 288, WB, "WHAT THIS SHEET CANNOT SHOW, AND WHY  [N]", [
        "NO MUSTER POINT.  There is no site plan, boundary or contour anywhere "
        "in this project  -  master open",
        "   item D3  -  so no assembly point can be placed and no distance "
        "from the structure can be stated.",
        "   The written plan records the same gap as FS-V5.  Nothing is "
        "invented here to fill it.",
        "NO FIRE SERVICE ACCESS, hardstanding, hydrant or rising main.  Same "
        "cause, same class.",
        "NO EXTERNAL SIGNAGE, EXIT SIGN OR EMERGENCY LIGHTING at either shaft "
        "head or at the entry door.",
        "   These follow the missing electrical design, FS-5.",
        "NO LADDER, RUNG OR FALL-ARREST IN EITHER ESCAPE SHAFT.  ESC 1 is a "
        f"{F.CLIMB_R2:.3f} m climb from the floor and",
        f"   ESC 2 is {F.CLIMB_R3:.3f} m.  Nothing in the project says how "
        "either climb is made, by whom, or whether an",
        "   injured person can make it at all.  THIS IS FS-6, AND DRAWING THE "
        "PROFILE IS WHAT FOUND IT  -  the written",
        "   plan had the two head levels and the floor level and never put "
        "them in the same picture.",
        "",
        "THE SENTRY POST IS NOT A REFUGE AND IS NOT SHOWN AS ONE.  It is "
        "outside this package and no fire",
        "   strategy for it exists anywhere in the project.",
    ], h=2.0, lead=LEAD)

    y = sh.table(CB, 214, [30, 262, 109], list(F.VERIF),
                 header=["ITEM", "WHAT IT IS", "STATUS"],
                 h=2.0, rh=6.4, layer="M-TABLE", max_w=WB)

    sh.panel(CB, y - 8, WB, "POLICY  -  THE CLAUSES THAT GOVERN THESE TWO "
             "SHEETS", [
        "FS-P3   BLAST DOORS ARE THE FIRE DOORS.  They are the only barriers "
        "that work.  Shutting the blast door",
        "        between the occupants and a fire is the FIRST structural "
        "action, not the last.",
        "FS-P4   W5 GETS ITS DOOR, OR ITS DESIGNATION IS WITHDRAWN.  One or "
        "the other.  A wall recorded as a fire",
        "        separation with a permanent hole in it is worse than a wall "
        "that claims nothing.",
        "FS-P5   ESC 2 IS NOT AN ESCAPE ROUTE FROM A GENERATOR FIRE.  The "
        "decision rule on F-101 is the rule.",
        "FS-P7   NO FIRE MEASURE IS ASSUMED TO BE PRICED.  Nothing on these "
        "sheets is in the bill, because nothing",
        "        on them exists yet.  Anything specified from them is an "
        "ADDITION to it.",
    ], h=2.0, lead=LEAD)

    sh.finish(scale="AS NOTED", sheet_of="2 OF 2")
    return sh


# =====================================================================
def main():
    os.makedirs(OUT, exist_ok=True)
    for fn, name in ((f101, "F-101_Underground_Level_Escape_Plan"),
                     (f102, "F-102_Entry_Level_Escape_Plan")):
        sh = fn()
        p = sh.save(os.path.join(OUT, name + ".dxf"))
        print("wrote", os.path.basename(p))


if __name__ == "__main__":
    main()
