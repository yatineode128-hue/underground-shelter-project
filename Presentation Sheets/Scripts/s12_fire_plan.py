"""
s12_fire_plan.py  --  FLS012  FIRE AND LIFE SAFETY: ESCAPE PLAN

Four views, in the layout and with the title block of the supplied Revit A2 set
(ARCH001..ARCH005), so that SHEET 12 reads as the next sheet of that series:

    1  UNDERGROUND LEVEL ESCAPE PLAN  (-)6.100                     1 : 100
    2  ENTRY LEVEL ESCAPE PLAN         0.000 / (-)2.000            1 : 100
    3  ESCAPE SHAFT ESC 1 / ESC 2 - SECTION AND LADDER             1 : 100
    4  EVACUATION DECISION RULE                                     NTS

Every route, travel distance and climb is computed in
`Fire and Life Safety/Scripts/fs_data.py` from the confirmed geometry, so a
distance on this sheet cannot disagree with the escape-route schedule or with
the box it is measured in.  The escape-shaft ladder is the one RULED by RC4
(master A.4.9): ladder only, fall-arrest deferred.

COLOUR: dark only, and mostly black.  ACI 7 black, 8 dark grey, 1 dark red for
the primary route and the exits, 5 dark blue for the two shaft routes.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
for _p in ("Structural CAD", "Drainage", "Fire and Life Safety"):
    sys.path.insert(0, os.path.join(ROOT, _p, "Scripts"))

from a2_lib import A2Sheet, vw                                # noqa: E402
import ops_data as D                                          # noqa: E402

SC = 100.0
PX0, VDIM = 47.0, 42.5
RCOL, RCOL_W, RTOP = 282.0, 178.0, 383.0
RULE_TO, RULE_MID = 272.0, 116.0
SM, SMS = 1.9, 1.75

V1_Y0, V1_DIM, V1_TTL = 306.0, 300.0, 282.0
V2_Y0, V2_DIM, V2_TTL = 190.0, 184.0, 172.0
SC_SH = 100.0
SH_CX, SH_FL = 75.0, 70.0                        # shaft centre x, floor y
V34_TTL = 48.0

P1 = vw(SC, PX0, V1_Y0)
P2 = vw(SC, PX0, V2_Y0)


def SH(mx, lvl):
    """V3: x from the shaft centre, and a level in metres -> paper."""
    return (SH_CX + mx / SC_SH, SH_FL + (lvl + 6.100) * 1000.0 / SC_SH)


s = A2Sheet(
    sheet_no="SHEET 12",
    drawing_no="FLS012",
    title_lines=["FIRE AND LIFE", "SAFETY - ESCAPE", "PLAN, SHAFT",
                 "SECTION AND", "DECISION RULE"],
    project_lines=D.PROJECT_LINES,
    identity=D.IDENTITY,
    notes=[
        "ALL DIMENSIONS ARE IN MM. ALL LEVELS ARE IN METRES RELATIVE TO "
        "FINISHED SITE GRADE 0.000, NEGATIVE DOWNWARDS.",
        "WRITTEN DIM TO BE FOLLOWED ONLY. DRG NOT TO BE SCALED.",
        "THIS DRG IS TO BE READ IN CONJUNCTION WITH ALL RELEVANT ARCH, STR AND "
        "SERVICES DRGS.",
        "THERE ARE THREE ESCAPE ROUTES AND NO OTHERS. R1 IS THE MAIN STAIR IN "
        "BAY 7 TO THE HEADHOUSE AND OUT THROUGH THE COVERED ENTRY STAIRWELL; "
        "R2 AND R3 ARE THE TWO 1400 DIA ESCAPE SHAFTS.",
        "BAYS 1 TO 6 ARE ONE SMOKE COMPARTMENT. THE FOUR W8 PARTITIONS ARE "
        "NON-STRUCTURAL AND CARRY PERMANENT 900 GAPS, SO BLAST DOORS 1 AND 2 "
        "IN W6 AND W7 ARE THE ONLY REAL BARRIERS IN THE SHELTER.",
        "ESC 2 IS IN BAY 8 WITH THE GENERATOR. FOR A FIRE IN BAY 8, BLAST "
        "DOOR 2 IS SHUT AND R3 IS NOT USED - EVACUATE BY R1, OR BY R2 IF THE "
        "SPINE IS SMOKE-LOGGED.",
        "EACH SHAFT IS CLIMBED ON A FIXED LADDER: 20 DIA GALVANISED MS RUNGS "
        "AT 400 CLEAR WIDTH, EQUAL PITCH, 200 OR MORE BEHIND THE RUNG AND "
        "750 OR MORE CLIMBING SPACE IN FRONT, WITH GRAB RAILS 1100 ABOVE THE "
        "HEAD.",
        "THE MAIN STAIRCASE IS 24 RISERS AT 170.8333, TREAD 280, 3 FLIGHTS OF "
        "8, TOTAL RISE 4100, WIDTH 1200, HEADROOM 2533.",
        "KEEP EVERY ROUTE, EVERY DOOR SWING AND BOTH SHAFT BASES CLEAR AT ALL "
        "TIMES.",
        "CONTRACTOR TO CHECK AND VERIFY THE DRG BEFORE EXECUTION.",
    ],
    date=D.DATE,
    drawn=D.DRAWN,
    checked=D.CHECKED,
    scale_note="As indicated",
)

for _nm, _col, _lw, _desc in [
    ("F-WALL",     7, 35, "Walls, cut"),
    ("F-WALL-IN",  7, 18, "Internal and non-structural walls"),
    ("F-OVER",     8, 18, "Over or below the cut plane"),
    ("F-ROUTE-P",  1, 50, "Escape route R1, primary"),
    ("F-ROUTE-S",  5, 50, "Escape routes R2 and R3, the escape shafts"),
    ("F-EXIT",     1, 50, "Exits and points of emergence"),
    ("F-COMPT",    7, 35, "Fire and smoke compartment boundaries"),
    ("F-LADDER",   5, 35, "Escape shaft ladder"),
    ("F-BOX",      7, 25, "Decision-rule diagram"),
]:
    _ly = s.doc.layers.add(_nm)
    _ly.color, _ly.lineweight, _ly.description = _col, _lw, _desc

B, I = D.BOX, D.INTR


def route(P, pts, layer, arrows=True, step=2600.0):
    """A walking line, with arrowheads along it in the direction of travel."""
    s.pline([P(*p) for p in pts], layer)
    if not arrows:
        return
    for a, b in zip(pts, pts[1:]):
        L = math.dist(a, b)
        if L < step * 0.6:
            continue
        ux, uy = (b[0] - a[0]) / L, (b[1] - a[1]) / L
        n = max(int(L // step), 1)
        for k in range(1, n + 1):
            t = L * k / (n + 1)
            tip = (a[0] + ux * t, a[1] + uy * t)
            for sg in (1, -1):
                s.line(P(*tip), P(tip[0] - ux * 520 - sg * uy * 300,
                                  tip[1] - uy * 520 + sg * ux * 300), layer)


def exit_mark(P, p, lab):
    s.circle(P(*p), 2.6 / 2.0, "F-EXIT")
    s.text(lab, P(*p), SMS, "F-EXIT", "C")


# =====================================================================  VIEW 1
# UNDERGROUND LEVEL ESCAPE PLAN, 1 : 100
s.rect(*P1(B["x0"], B["y0"]), *P1(B["x1"], B["y1"]), "F-WALL")
s.rect(*P1(I["x0"], I["y0"]), *P1(I["x1"], I["y1"]), "F-WALL")
for x0, x1 in D.PARTITIONS:
    for y0, y1 in ((I["y0"], D.PART_DOOR_Y[0]), (D.PART_DOOR_Y[1], I["y1"])):
        s.rect(*P1(x0, y0), *P1(x1, y1), "F-WALL-IN")
s.rect(*P1(D.IW[0][1], I["y0"]), *P1(D.IW[0][2], I["y1"]), "F-WALL-IN")
BD = D.BLAST_DOOR
for mark, x0, x1, t in D.IW[1:]:
    s.rect(*P1(x0, BD["y1"]), *P1(x1, I["y1"]), "F-COMPT")
    s.line(P1(x0, I["y0"]), P1(x1, I["y0"]), "F-COMPT")
    s.arc(P1(x1, BD["y0"]), BD["w"] / SC, 0, 90, "F-EXIT")
for name, cx, cy, head in D.ESC:
    s.circle(P1(cx, cy), D.ESC_CLEAR_D / 2.0 / SC, "F-EXIT")
    s.circle(P1(cx, cy), D.ESC_COLLAR_OD / 2.0 / SC, "F-WALL")
V, ST = D.VOID, D.STAIR
s.dline(P1(V["x0"], V["y1"]), P1(V["x1"], V["y1"]), "F-OVER")
for fx0, fx1 in (ST["fltA"], ST["fltB"]):
    s.rect(*P1(fx0, ST["L2_y"][0]), *P1(fx1, ST["L1_y"][1]), "F-WALL-IN")
    for k in range(1, 8):
        y = ST["L2_y"][0] + k * (ST["L1_y"][1] - ST["L2_y"][0]) / 8.0
        s.line(P1(fx0, y), P1(fx1, y), "F-WALL-IN")

# the three routes
route(P1, D.R1, "F-ROUTE-P")
route(P1, D.R2, "F-ROUTE-S", step=900.0)
route(P1, D.R3, "F-ROUTE-S")
route(P1, D.R3_FROM_BD2, "F-ROUTE-S", step=1400.0)
exit_mark(P1, (D.ESC[0][1], D.ESC[0][2]), "R2")
exit_mark(P1, (D.ESC[1][1], D.ESC[1][2]), "R3")
exit_mark(P1, (ST["fltA"][0] + 400, D.BDOOR_Y), "R1")
s.text("R1", P1(6000, 3350), SM, "F-ROUTE-P", "C")
s.text("BD1", P1(15000, 2150), SMS, "S-TEXT", "C")
s.text("BD2", P1(18200, 2150), SMS, "S-TEXT", "C")
for n, x0, x1, w, room, name in D.BAYS:
    s.text(room, P1((x0 + x1) / 2.0, 800), SM, "S-TEXT", "C")
for lab, x in (("C1  BAYS 1 - 6, ONE SMOKE COMPARTMENT", 7300),
               ("C2", 16600), ("C3", 19900)):
    s.text(lab, P1(x, 4900), SMS, "F-COMPT", "C")

AB = V1_Y0 + B["y1"] / SC
s.note_leader(P1(2050, 3000), (PX0 + 6.0, AB + 11.0),
              f"R2  ESC 1, TRAVEL {D.TRAVEL_R2:.2f} m, CLIMB "
              f"{D.CLIMB_R2:.3f} m", SM, "R")
s.note_leader(P1(9000, D.SPINE_Y), (PX0 + 66.0, AB + 5.5),
              f"R1  SPINE THROUGH THE 900 PARTITION GAPS AT Y 2500 - 3400, "
              f"TRAVEL {D.TRAVEL_R1:.1f} m TO BAY 7, CLIMB "
              f"{D.CLIMB_R1:.3f} m", SM, "R")
s.note_leader(P1(19900, 3000), (PX0 + 180.0, AB + 11.0),
              f"R3  ESC 2, TRAVEL {D.TRAVEL_R3:.2f} m, CLIMB "
              f"{D.CLIMB_R3:.3f} m", SM, "R")
s.dim_h(P1(I["x0"], 0), P1(15200, 0), V1_DIM, SC, "A2-DIM-S")
s.dim_h(P1(15200, 0), P1(I["x1"], 0), V1_DIM, SC, "A2-DIM-S")
s.dim_v(P1(0, 0), P1(0, 6200), VDIM, SC, "A2-DIM-S")
s.north((274.5, 350.0))
s.view_title(PX0 - 4.0, V1_TTL, "1",
             "UNDERGROUND LEVEL ESCAPE PLAN   (-)6.100",
             f"1 : 100   SPINE {D.SPINE_LEN:.3f} m;  THREE ROUTES, R1 PRIMARY",
             RULE_TO)

# =====================================================================  VIEW 2
# ENTRY LEVEL ESCAPE PLAN, 1 : 100
H, A = D.HH, D.ASW
for a_, b_ in (((B["x0"], B["y0"]), (B["x1"], B["y0"])),
               ((B["x0"], B["y1"]), (B["x1"], B["y1"])),
               ((B["x0"], B["y0"]), (B["x0"], B["y1"])),
               ((B["x1"], B["y0"]), (B["x1"], B["y1"]))):
    s.dline(P2(*a_), P2(*b_), "F-OVER", 1.8, 1.3)
s.rect(*P2(H["x0"], H["y0"]), *P2(H["x1"], H["y1"]), "F-WALL")
s.rect(*P2(H["ix0"], H["iy0"]), *P2(H["ix1"], H["iy1"]), "F-WALL")
s.rect(*P2(A["x0"], A["y0"]), *P2(A["x1"], A["y1"]), "F-WALL")
s.rect(*P2(A["ix0"], A["iy0"]), *P2(A["ix1"], A["iy1"]), "F-WALL")
s.rect(*P2(V["x0"], V["y0"]), *P2(V["x1"], V["y1"]), "F-EXIT")
s.line(P2(V["x0"], V["y0"]), P2(V["x1"], V["y1"]), "S-CENTER")
s.line(P2(V["x0"], V["y1"]), P2(V["x1"], V["y0"]), "S-CENTER")
s.line(P2(H["ix0"], H["iy1"]), P2(D.HH_DOOR["x0"], H["iy1"]), "F-WALL")
s.line(P2(D.HH_DOOR["x1"], H["iy1"]), P2(H["ix1"], H["iy1"]), "F-WALL")
s.arc(P2(D.HH_DOOR["x0"], H["iy1"]), D.HH_DOOR["w"] / SC, 0, 90, "F-EXIT")
s.line(P2(A["top_landing"][1], A["iy0"]), P2(A["top_landing"][1], A["iy1"]),
       "F-WALL-IN")
for k in range(1, 12):
    x = A["flight"][0] + k * (A["flight"][1] - A["flight"][0]) / 12.0
    s.line(P2(x, A["iy0"]), P2(x, A["iy1"]), "F-WALL-IN")
s.line(P2(A["platform"][0], A["iy0"]), P2(A["platform"][0], A["iy1"]),
       "F-WALL-IN")
s.arc(P2(A["x0"], A["iy0"]), A["door"][0] / SC, 0, 90, "F-EXIT")
for name, cx, cy, head in D.ESC:
    s.circle(P2(cx, cy), D.ESC_CLEAR_D / 2.0 / SC, "F-EXIT")
    s.circle(P2(cx, cy), D.ESC_COLLAR_OD / 2.0 / SC, "F-WALL")
route(P2, D.ENTRY_ROUTE, "F-ROUTE-P", step=2200.0)
exit_mark(P2, (A["x0"] + 300, 6750), "R1")
exit_mark(P2, (D.ESC[0][1], D.ESC[0][2]), "R2")
exit_mark(P2, (D.ESC[1][1], D.ESC[1][2]), "R3")
s.text("STAIR ARRIVAL  (-)2.000", P2(16600, 2050), SMS, "S-TEXT", "C")
s.text("HEADHOUSE", P2(16000, 5150), SMS, "S-TEXT", "C")
s.text("ENTRY DOOR 1000 x 2100, OPENS OUTWARD", P2(12000, 8100), SMS,
       "S-TEXT", "C")
s.text("PLATFORM  (-)2.000", P2(15050, 7150), SMS, "S-TEXT", "C")
s.text("ESC 1 HEAD  +0.150", P2(2050, 300), SMS, "S-TEXT", "C")
s.text("ESC 2 HEAD  +0.700", P2(19900, 300), SMS, "S-TEXT", "C")
s.note_leader(P2(12650, 6750), (PX0 + 14.0, V2_Y0 - 6.0),
              f"R1 SURFACE LEG, TRAVEL {D.TRAVEL_ENTRY:.2f} m:  STAIR "
              f"ARRIVAL - HEADHOUSE - PLATFORM - ENTRY DOOR AT GRADE",
              SM, "R")
s.dim_h(P2(A["x0"], 0), P2(A["x1"], 0), P2(0, 4400)[1], SC, "A2-DIM-S")
s.dim_h(P2(H["x0"], 0), P2(H["x1"], 0), P2(0, -600)[1], SC, "A2-DIM-S")
s.view_title(PX0 - 4.0, V2_TTL, "2",
             "ENTRY LEVEL ESCAPE PLAN   (-)2.000 AND 0.000",
             "1 : 100   R1 EMERGES OUTSIDE THE PROTECTIVE BOUNDARY", RULE_TO)

# =====================================================================  VIEW 3
# ESCAPE SHAFT ESC 1 / ESC 2 - SECTION AND LADDER, 1 : 75
CL, CT = D.ESC_CLEAR_D / 2.0, D.ESC_COLLAR_OD / 2.0
s.hatch_pat([SH(-2600, 0.000), SH(2600, 0.000), SH(2600, -2.000),
             SH(-2600, -2.000)], "EARTH", 1.0, 0.0, "F-OVER")
for lv0, lv1 in ((-2.900, -2.000),):                        # 900 pressure slab
    s.conc_hatch([SH(-2600, lv0), SH(-CL, lv0), SH(-CL, lv1), SH(-2600, lv1)],
                 scale=0.5)
    s.conc_hatch([SH(CL, lv0), SH(2600, lv0), SH(2600, lv1), SH(CL, lv1)],
                 scale=0.5)
    s.rect(*SH(-2600, lv0), *SH(-CL, lv1), "F-WALL")
    s.rect(*SH(CL, lv0), *SH(2600, lv1), "F-WALL")
s.conc_hatch([SH(-2600, -6.700), SH(2600, -6.700), SH(2600, -6.100),
              SH(-2600, -6.100)], scale=0.5)
s.rect(*SH(-2600, -6.700), *SH(2600, -6.100), "F-WALL")     # 600 mat
for sg in (-1, 1):                                          # 250 RC collar
    s.rect(*SH(sg * CL, -2.000), *SH(sg * CT, 0.700), "F-WALL")
    s.conc_hatch([SH(sg * CL, -2.000), SH(sg * CT, -2.000),
                  SH(sg * CT, 0.700), SH(sg * CL, 0.700)], scale=0.5)
s.line(SH(-2600, 0.000), SH(-CT, 0.000), "F-OVER")
s.line(SH(CT, 0.000), SH(2600, 0.000), "F-OVER")

# the RC4 ladder: rungs at equal pitch, 2 stringers, brackets over the lower
# 3.200 m, grab rails 1100 above the head
NR = 22
for k in range(1, NR):
    v = -6.100 + k * (6.800 / NR)
    s.line(SH(-200, v), SH(200, v), "F-LADDER")
for sg in (-1, 1):
    s.line(SH(sg * 200, -6.100), SH(sg * 200, 0.700), "F-LADDER")
    s.line(SH(sg * 200, 0.700), SH(sg * 200, 1.800), "F-LADDER")
s.line(SH(-200, 1.800), SH(200, 1.800), "F-LADDER")
for k in range(3):
    s.line(SH(200, -6.100 + k * 1.600), SH(CL, -6.100 + k * 1.600), "F-LADDER")
s.text("GRAB RAILS 1100", SH(-1450, 1.500), SMS, "S-TEXT", "C")
for lvl, lab in ((0.700, "+0.700"), (0.150, "+0.150"), (-2.000, "(-)2.000"),
                 (-2.900, "(-)2.900"), (-6.100, "(-)6.100"),
                 (-6.700, "(-)6.700")):
    s.line(SH(2600, lvl), SH(3300, lvl), "S-LEVEL")
    s.msp.add_blockref("A2-LEVEL", SH(3300, lvl),
                       dxfattribs={"layer": "S-LEVEL"})
    s.text(lab, (SH(3300, lvl)[0] + 2.6, SH(0, lvl)[1] + 2.4), SMS, "S-LEVEL",
           "ML")
s.dim_h(SH(-CL, -6.100), SH(CL, -6.100), SH(0, -6.700)[1] - 5.0, SC_SH,
        "A2-DIM-S")
s.dim_v(SH(-CT, -6.100), SH(-CT, 0.700), SH(-3300, 0)[0], SC_SH, "A2-DIM-S")
s.text("400 RUNG", SH(-1300, -3.400), SMS, "S-TEXT", "C")

s.view_title(PX0 - 4.0, V34_TTL, "3", "ESCAPE SHAFT - SECTION",
             "1 : 100   ESC 1 AND ESC 2", RULE_MID)

# =====================================================================  VIEW 4
# EVACUATION DECISION RULE, not to scale
DX, DY, DW, DH, DG = 128.0, 138.0, 44.0, 13.0, 4.0
HEAD = ("WHERE THE FIRE IS", "ROUTE TO USE", "AND WHAT IS SHUT")
ROWS = [
    ("BAY 8, GENERATOR", "R1;  R2 IF THE SPINE IS SMOKE-LOGGED",
     "BLAST DOOR 2 SHUT.  DO NOT USE R3"),
    ("BAYS 1 TO 6, OCCUPIED", "R1 IF BAY 7 IS CLEAR",
     "OTHERWISE R2 FROM THE WEST, R3 FROM THE EAST"),
    ("BAY 7, STAIR SHAFT", "R2 OR R3",
     "BOTH BLAST DOORS SHUT.  R1 IS THE FIRE"),
    ("HEADHOUSE OR STAIRWELL", "R2 OR R3",
     "R1'S SURFACE END IS BLOCKED"),
]
for j, h in enumerate(HEAD):
    s.text(h, (DX + j * (DW + DG) + DW / 2.0, DY + 4.0), SM, "S-TITLE", "C")
s.line((DX, DY + 1.0), (DX + 3 * DW + 2 * DG, DY + 1.0), "F-BOX")
for i, row in enumerate(ROWS):
    y0 = DY - (i + 1) * (DH + DG)
    for j, cell in enumerate(row):
        x0 = DX + j * (DW + DG)
        s.rect(x0, y0, x0 + DW, y0 + DH, "F-BOX")
        for k, ln in enumerate(s._wrap(cell, DW - 3.0, SMS)[:3]):
            s.text(ln, (x0 + DW / 2.0, y0 + DH - 3.2 - k * 3.0), SMS,
                   "S-TEXT", "C")
        if j:
            lay = "F-ROUTE-P" if j == 1 else "F-BOX"
            s.line((x0 - DG, y0 + DH / 2.0), (x0, y0 + DH / 2.0), lay)
s.view_title(RULE_MID + 6.0, V34_TTL, "4", "EVACUATION DECISION RULE",
             "NOT TO SCALE", RULE_TO)

# =====================================================================  TABLES
y = s.table_stack(RCOL, RTOP, 35.5, RCOL_W, [
    dict(rows=D.ESCAPE_ROUTES, title="ESCAPE ROUTE SCHEDULE",
         header=["REF", "ROUTE", "TRAVEL", "CLIMB", "WHERE IT GOES"],
         align=["C", "L", "C", "C", "L"], pad=2.2),
    dict(rows=D.EMERGENCE, title="POINT OF EMERGENCE SCHEDULE",
         header=["REF", "EMERGES AT", "OPENING", "LEVEL", "NOTES"],
         align=["C", "L", "C", "C", "L"], pad=2.2),
    dict(rows=D.COMPARTMENTS, title="FIRE AND SMOKE COMPARTMENT SCHEDULE",
         header=["REF", "COMPARTMENT", "NOTES"],
         align=["C", "L", "L"], pad=2.2),
    dict(rows=D.LADDER, title="ESCAPE SHAFT LADDER SCHEDULE",
         header=["ITEM", "SPECIFICATION", "EXTENT", "NOTES"],
         align=["L", "L", "L", "L"], pad=2.2),
    dict(rows=D.DECISION, title="EVACUATION DECISION RULE",
         header=["WHERE THE FIRE IS", "ROUTE TO USE", "AND WHAT IS SHUT"],
         align=["L", "L", "L"], pad=2.2),
], gap=5.0, rh_max=7.2)
assert y > 35.0, f"the schedule stack overflows the frame: bottom at {y:.1f}"


if __name__ == "__main__":
    out = os.path.join(ROOT, "Presentation Sheets", "DXF",
                       "FLS012_Fire_and_Life_Safety_Escape_Plan_and_"
                       "Decision_Rule.dxf")
    s.save(out)
    print("written", out, "| right column bottom y =", round(y, 1))
