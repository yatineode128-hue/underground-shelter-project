"""
s09_sentry_footing_slab.py  --  STR009  STRUCTURAL REINFORCEMENT DETAILING
                                SENTRY POST - ISOLATED FOOTING F1 AND SLAB S1

Five views, in the layout and with the title block of the supplied Revit A2 set
(ARCH001..ARCH005), so that SHEET 09 reads as the next sheet of that series:

    1  SLAB S1 - BOTTOM REINFORCEMENT PLAN                      1 : 40
    2  SLAB S1 - TOP REINFORCEMENT PLAN (EDGES AND CORNERS)     1 : 40
    3  SLAB S1 - LONGITUDINAL SECTION 2-2                       1 : 25
    4  ISOLATED FOOTING F1 - REINFORCEMENT PLAN                 1 : 20
    5  ISOLATED FOOTING F1 - SECTION 1-1                        1 : 20

The slab is a two-way slab on IS 456 Table 26 (Annex D-1.1, Case 9).  Table 26
is valid ONLY because the corner torsion mats of Cl. D-1.8 are provided, so the
top plan carries them at full size and the sheet calls them a hold point.

Every dimension, level, size, bar and spacing comes from
master/MASTER_PROJECT_STATE.md Parts A.4.8, A.7.7, B.8.3, B.8.7 and F.4,
through sentry_data.py.  Nothing is invented; the detailing decisions the
master does not cover are DECLARED on the sheet and logged in Part H (SR2).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "Structural CAD", "Scripts"))

from a2_lib import A2Sheet, TXT                              # noqa: E402
import sentry_data as S                                      # noqa: E402

RCOL, RCOL_W = 277.0, 183.0
SM = 1.7

SC_SLAB = 40.0                       # V1 / V2 slab plans
S1X, S1Y = 58.0, 255.0               # model (0,0) of the bottom plan
S2X, S2Y = 168.0, 255.0              # model (0,0) of the top plan
V1_TTL, V2_TTL = 230.0, 230.0

SC_SEC = 25.0                        # V3 slab longitudinal section
L3X, L3TOP, V3_TTL = 52.0, 204.0, 151.0   # model Y 0 at x 52; slab top at 204

SC_FTG = 20.0                        # V4 / V5 footing views
F4X, F4Y, V4_TTL = 60.0, 66.0, 44.0       # footing plan, model (0,0)
F5X, F5B = 170.0, 66.0                    # footing section, base at y 66

H = S.COL / 2.0
HB = S.BM_B / 2.0
COLS = [(S.GRID_A, S.GRID_1), (S.GRID_B, S.GRID_1),
        (S.GRID_A, S.GRID_2), (S.GRID_B, S.GRID_2)]


def PL(ox, oy):
    def P(mx, my):
        return (ox + mx / SC_SLAB, oy + my / SC_SLAB)
    return P


P1, P2 = PL(S1X, S1Y), PL(S2X, S2Y)


def SEC(my, v):
    """V3: project Y (mm) and v DOWN from the top of slab -> paper."""
    return (L3X + my / SC_SEC, L3TOP - v / SC_SEC)


def FP(mx, my):
    return (F4X + mx / SC_FTG, F4Y + my / SC_FTG)


def FS(mx, v):
    """V5: x across the footing, v UP from the founding level -> paper."""
    return (F5X + mx / SC_FTG, F5B + v / SC_FTG)


# =====================================================================  SHEET
s = A2Sheet(
    sheet_no="SHEET 09",
    drawing_no="STR009",
    title_lines=["STRUCTURAL", "REINFORCEMENT", "DETAILING OF", "SENTRY POST -",
                 "FOOTING & SLAB"],
    project_lines=["CBRN HARDENED", "UG OPS ROOM"],
    identity=S.IDENTITY,
    notes=S.NOTES_09,
    date="16 SEP 2026",
    drawn="SYN 01",
    checked="DR IR CHAUDHARI",
    scale_note="As indicated",
    rev_note="SR2   16.09.2026",
)


def slab_shell(P):
    """The envelope, columns and beams that both slab plans stand on."""
    s.rect(*P(0, 0), *P(S.EXT_X, S.EXT_Y), "S-CONCRETE-THIN")
    for gy in (S.GRID_1, S.GRID_2):
        s.dline(P(S.GRID_A + H, gy - HB), P(S.GRID_B - H, gy - HB), "S-HIDDEN")
        s.dline(P(S.GRID_A + H, gy + HB), P(S.GRID_B - H, gy + HB), "S-HIDDEN")
    for gx in (S.GRID_A, S.GRID_B):
        s.dline(P(gx - HB, S.GRID_1 + H), P(gx - HB, S.GRID_2 - H), "S-HIDDEN")
        s.dline(P(gx + HB, S.GRID_1 + H), P(gx + HB, S.GRID_2 - H), "S-HIDDEN")
    for cx, cy in COLS:
        s.conc_hatch([P(cx - H, cy - H), P(cx + H, cy - H),
                      P(cx + H, cy + H), P(cx - H, cy + H)], scale=0.45)
        s.rect(*P(cx - H, cy - H), *P(cx + H, cy + H), "S-CONCRETE")


# =====================================================================  VIEW 1
# SLAB S1 - BOTTOM REINFORCEMENT PLAN, 1 : 40
slab_shell(P1)
X0, X1, Y0, Y1 = S.SL_X0, S.SL_X1, S.SL_Y0, S.SL_Y1
CXM, CYM = (S.GRID_A + S.GRID_B) / 2.0, (S.GRID_1 + S.GRID_2) / 2.0

for k in range(S.nb(S.CLR_SLAB_Y, 300)):                     # SS01 full length
    y = 300.0 + k * 300.0
    s.bar([P1(X0, y), P1(X1, y)], "S-REBAR-MAIN")
for k in range(S.nb(S.CLR_SLAB_Y, 300)):                     # SS02 curtailed
    y = 450.0 + k * 300.0
    s.bar([P1(CXM - S.CURT_X / 2.0, y), P1(CXM + S.CURT_X / 2.0, y)],
          "S-REBAR-MAIN")
for k in range(S.nb(S.CLR_SLAB_X, 300)):                     # SS03 full length
    x = 300.0 + k * 300.0
    s.bar([P1(x, Y0), P1(x, Y1)], "S-REBAR-DIST")
for k in range(S.nb(S.CLR_SLAB_X, 300)):                     # SS04 curtailed
    x = 450.0 + k * 300.0
    s.bar([P1(x, CYM - S.CURT_Y / 2.0), P1(x, CYM + S.CURT_Y / 2.0)],
          "S-REBAR-DIST")

s.tag(P1(700, 4350), "SS01", P1(1500, 4200))
s.tag(P1(700, 1050), "SS02", P1(1500, 1200))
s.tag(P1(3300, 4350), "SS03", P1(2600, 4200))
s.tag(P1(3300, 1050), "SS04", P1(2600, 1200))
s.text("SHORT SPAN (X) RED", P1(2000, 2750), SM, "S-TEXT", "C")
s.text("LONG SPAN (Y) BLUE", P1(2000, 2450), SM, "S-TEXT", "C")
s.text("BOTH ARE MAIN STEEL", P1(2000, 2150), SM, "S-TEXT", "C")
s.secmark(P1(2000, -320), "2", "U", 3.0)
s.secmark(P1(2000, S.EXT_Y + 320), "2", "D", 3.0)
s.cline(P1(2000, -260), P1(2000, S.EXT_Y + 260), "S-CENTER")

for gx, lab in ((S.GRID_A, "A"), (S.GRID_B, "B")):
    s.cline((P1(gx, 0)[0], P1(gx, 0)[1] - 4.0), P1(gx, S.EXT_Y), "S-CENTER")
    p = (P1(gx, 0)[0], P1(gx, 0)[1] - 8.0)
    s.circle(p, 4.0, "S-GRID")
    s.text(lab, p, TXT["mark"], "S-GRID", "C")
for gy, lab in ((S.GRID_1, "1"), (S.GRID_2, "2")):
    s.cline((P1(0, gy)[0] - 4.0, P1(0, gy)[1]), P1(S.EXT_X, gy), "S-CENTER")
    p = (P1(0, gy)[0] - 8.0, P1(0, gy)[1])
    s.circle(p, 4.0, "S-GRID")
    s.text(lab, p, TXT["mark"], "S-GRID", "C")

s.dim_h(P1(S.GRID_A, 0), P1(S.GRID_B, 0), 240.0, SC_SLAB)
s.dim_v(P1(S.EXT_X, S.GRID_1), P1(S.EXT_X, S.GRID_2), 163.0, SC_SLAB)
s.view_title(44.0, V1_TTL, "1", "SLAB S1 - BOTTOM REINFORCEMENT PLAN",
             "1 : 40   T8 @ 150 BOTH WAYS = 335 mm2/m,  COVER 30", 160.0)

# =====================================================================  VIEW 2
# SLAB S1 - TOP REINFORCEMENT PLAN, 1 : 40
slab_shell(P2)
BAND = S.EDGE_BAND
TOR = S.TORSION

# -- the 400 top edge bands, bars perpendicular to each edge at 300 c/c
for k in range(S.nb(S.CLR_SLAB_X, 300)):
    x = 300.0 + k * 300.0
    s.bar([P2(x, Y0), P2(x, S.GRID_1 + HB + BAND)], "S-REBAR-SEC")
    s.bar([P2(x, Y1), P2(x, S.GRID_2 - HB - BAND)], "S-REBAR-SEC")
for k in range(S.nb(S.CLR_SLAB_Y, 300)):
    y = 300.0 + k * 300.0
    s.bar([P2(X0, y), P2(S.GRID_A + HB + BAND, y)], "S-REBAR-SEC")
    s.bar([P2(X1, y), P2(S.GRID_B - HB - BAND, y)], "S-REBAR-SEC")
for gy in (S.GRID_1 + HB + BAND, S.GRID_2 - HB - BAND):
    s.dline(P2(X0, gy), P2(X1, gy), "S-HIDDEN")
for gx in (S.GRID_A + HB + BAND, S.GRID_B - HB - BAND):
    s.dline(P2(gx, Y0), P2(gx, Y1), "S-HIDDEN")

# -- the four corner torsion mats, 700 x 700, bars both ways at 200 c/c
for cx, cy in COLS:
    sx = 1 if cx < S.EXT_X / 2 else -1
    sy = 1 if cy < S.EXT_Y / 2 else -1
    x0, y0 = cx, cy
    s.rect(*P2(x0, y0), *P2(x0 + sx * TOR, y0 + sy * TOR), "S-REBAR-SEC")
    for k in range(S.nb(TOR, 200)):
        o = k * 200.0
        s.bar([P2(x0 - sx * (HB - S.CV_SLAB), y0 + sy * o),
               P2(x0 + sx * TOR, y0 + sy * o)], "S-REBAR-MAIN")
        s.bar([P2(x0 + sx * o, y0 - sy * (HB - S.CV_SLAB)),
               P2(x0 + sx * o, y0 + sy * TOR)], "S-REBAR-DIST")

s.tag(P2(2000, 4350), "SS05", P2(2000, S.GRID_2 - HB - BAND / 2.0))
s.tag(P2(1350, 850), "SS06", P2(S.GRID_A + TOR / 2.0, S.GRID_1 + TOR / 2.0))
s.text("TORSION MATS - 4 LAYERS,", P2(2000, 2750), SM, "S-TEXT", "C")
s.text("2 TOP + 2 BOTTOM EACH WAY,", P2(2000, 2450), SM, "S-TEXT", "C")
s.text("700 x 700 AT ALL 4 CORNERS", P2(2000, 2150), SM, "S-TEXT", "C")
s.text("Cl. D-1.8 - A HOLD POINT", P2(2000, 1850), SM, "S-TEXT", "C")

s.dim_v(P2(S.GRID_A + TOR, S.GRID_1), P2(S.GRID_A + TOR, S.GRID_1 + TOR),
        P2(S.GRID_A + TOR, 0)[0] + 9.0, SC_SLAB, "A2-DIM-S")
s.dim_v(P2(S.GRID_B, S.GRID_2 - HB - BAND), P2(S.GRID_B, S.GRID_2 - HB),
        P2(0, 0)[0] + 96.0, SC_SLAB, "A2-DIM-S")
s.view_title(164.0, V2_TTL, "2", "SLAB S1 - TOP REINFORCEMENT PLAN",
             "1 : 40   400 EDGE BANDS (Cl. D-1.6) + 700 x 700 CORNER MATS "
             "(Cl. D-1.8)", 272.0)

# =====================================================================  VIEW 3
# SLAB S1 - LONGITUDINAL SECTION 2-2, 1 : 25
s.conc_hatch([SEC(0, S.SLAB_T), SEC(S.EXT_Y, S.SLAB_T),
              SEC(S.EXT_Y, 0), SEC(0, 0)], scale=0.45)
s.rect(*SEC(0, S.SLAB_T), *SEC(S.EXT_Y, 0), "S-CONCRETE")
for gy in (S.GRID_1, S.GRID_2):                              # beams B1, cut
    s.conc_hatch([SEC(gy - HB, S.BM_D), SEC(gy + HB, S.BM_D),
                  SEC(gy + HB, S.SLAB_T), SEC(gy - HB, S.SLAB_T)], scale=0.45)
    s.rect(*SEC(gy - HB, S.BM_D), *SEC(gy + HB, S.SLAB_T), "S-CONCRETE")
    s.rect(*SEC(gy - H, S.BM_D + 420), *SEC(gy + H, S.BM_D), "S-CONCRETE")
    s.line(SEC(gy - HB, S.BM_D), SEC(gy + HB, S.BM_D), "S-CONCRETE")

VB = S.SLAB_T - S.CV_SLAB - 4.0                              # bottom bar, 116
VT = S.CV_SLAB + 4.0                                         # top bar, 34
s.bar([SEC(Y0, VB - 8.0), SEC(Y1, VB - 8.0)], "S-REBAR-DIST")   # SS03, dy 108
s.bar([SEC(CYM - S.CURT_Y / 2.0, VB - 8.0),
       SEC(CYM + S.CURT_Y / 2.0, VB - 8.0)], "S-REBAR-DIST")     # SS04
for k in range(S.nb(S.CLR_SLAB_Y, 300)):        # SS01 seen end-on, dx 116, BELOW
    s.bar_dot(SEC(300.0 + k * 300.0, VB), 0.5, "S-REBAR-MAIN")
for gy, sgn in ((S.GRID_1, 1), (S.GRID_2, -1)):              # SS05 edge bands
    s.bar([SEC(gy - sgn * (HB - S.CV_SLAB), VT + 100.0),
           SEC(gy - sgn * (HB - S.CV_SLAB), VT),
           SEC(gy + sgn * S.EDGE_BAND, VT)], "S-REBAR-SEC")
for gy in (S.GRID_1, S.GRID_2):                              # B1 hoops, cut
    for o in (-70, 0, 70):
        s.line(SEC(gy + o, S.CV_BEAM), SEC(gy + o, S.BM_D - S.CV_BEAM),
               "S-REBAR-STIRRUP")

s.tag(SEC(1450, -320), "SS01", SEC(1450, VB))
s.tag(SEC(2900, -320), "SS03", SEC(2900, VB - 8.0))
s.tag(SEC(700, -320), "SS05", SEC(S.GRID_1 + 300, VT - 40.0))
s.tag(SEC(4200, -320), "SS04", SEC(4200, VB - 8.0))
s.level(SEC(S.EXT_Y - 150.0, 0.0), "(+)3.650", "L", 2.6)
s.text("SLAB 150 THK", SEC(3600, S.SLAB_T + 260.0), SM, "S-TEXT", "C")
s.dim_h(SEC(S.GRID_1 + HB, 0), SEC(S.GRID_2 - HB, 0), 166.0, SC_SEC)
s.dim_h(SEC(0, 0), SEC(S.EXT_Y, 0), 161.0, SC_SEC)
s.view_title(44.0, V3_TTL, "3", "SLAB S1 - LONGITUDINAL SECTION 2-2",
             "1 : 25   TYPICAL AT FIRST FLOOR AND ROOF.  B1 250 x 450 AT "
             "EACH END - SEE SHEET 08", 272.0)

# =====================================================================  VIEW 4
# ISOLATED FOOTING F1 - REINFORCEMENT PLAN, 1 : 20
FL = S.FTG_L
s.rect(*FP(0, 0), *FP(FL, FL), "S-CONCRETE")
s.dline(FP(FL / 2 - H, FL / 2 - H), FP(FL / 2 + H, FL / 2 - H), "S-HIDDEN")
s.dline(FP(FL / 2 + H, FL / 2 - H), FP(FL / 2 + H, FL / 2 + H), "S-HIDDEN")
s.dline(FP(FL / 2 + H, FL / 2 + H), FP(FL / 2 - H, FL / 2 + H), "S-HIDDEN")
s.dline(FP(FL / 2 - H, FL / 2 + H), FP(FL / 2 - H, FL / 2 - H), "S-HIDDEN")
B0, B1_ = S.CV_FTG, FL - S.CV_FTG
for k in range(S.nb(S.FTG_BAR, 150)):
    o = B0 + k * 150.0
    s.bar([FP(B0, o), FP(B1_, o)], "S-REBAR-MAIN")
    s.bar([FP(o, B0), FP(o, B1_)], "S-REBAR-DIST")
UBC = H - S.CV_COL - 10 - 8
for i in range(3):
    for j in range(3):
        if not (i == 1 and j == 1):
            s.bar_dot(FP(FL / 2 - UBC + i * UBC, FL / 2 - UBC + j * UBC), 0.7)
s.cline(FP(FL / 2, -120), FP(FL / 2, FL + 120), "S-CENTER")
s.secmark(FP(FL / 2, -230), "1", "U", 3.0)
s.tag(FP(FL + 470, 1130), "SF01", FP(B1_, 1130))
s.tag(FP(FL + 470, 330), "SF02", FP(1350, 330))
s.text("C1 350 x 350 OVER", FP(FL / 2, FL / 2 + 430), SM, "S-TEXT", "C")
s.text("8-T16 SC01 THROUGH", FP(FL / 2, FL / 2 - 500), SM, "S-TEXT", "C")
s.dim_h(FP(0, 0), FP(FL, 0), 58.0, SC_FTG)
s.dim_v(FP(0, 0), FP(0, FL), 52.0, SC_FTG)
s.view_title(44.0, V4_TTL, "4", "ISOLATED FOOTING F1 - REINFORCEMENT PLAN",
             "1 : 20   T12 @ 150 BOTH WAYS BOTTOM (754 mm2/m),  COVER 50,"
             "  4 No.", 160.0)

# =====================================================================  VIEW 5
# ISOLATED FOOTING F1 - SECTION 1-1, 1 : 20
s.rock_hatch([FS(-220, -300), FS(FL + 220, -300), FS(FL + 220, 0), FS(-220, 0)],
             scale=1.0)
s.conc_hatch([FS(0, 0), FS(FL, 0), FS(FL, S.FTG_T), FS(0, S.FTG_T)], scale=0.45)
s.rect(*FS(0, 0), *FS(FL, S.FTG_T), "S-CONCRETE")
s.rect(*FS(FL / 2 - H, S.FTG_T), *FS(FL / 2 + H, S.FTG_T + 800), "S-CONCRETE")
s.line(FS(-220, 0), FS(FL + 220, 0), "S-EXISTING")

BOT = S.CV_FTG + 12.0                                        # SF01 centre, 62
for k in range(S.nb(S.FTG_BAR, 150)):                        # SF02, seen end-on
    s.bar_dot(FS(B0 + k * 150.0, BOT + 12.0), 0.6, "S-REBAR-DIST")
s.bar([FS(B0, BOT), FS(B1_, BOT)], "S-REBAR-MAIN")           # SF01 along its run
for sgn in (-1, 1):                                          # SC01, D3 anchorage
    x = FL / 2 + sgn * UBC
    s.bar([FS(x, S.FTG_T + 800), FS(x, S.CV_FTG + 24.0),
           FS(x - sgn * S.COL_BAR_BEND, S.CV_FTG + 24.0)], "S-REBAR-MAIN")

s.level(FS(FL + 40, S.FTG_T), "(-)1.400", "R", 2.6)
s.level(FS(FL + 40, 0.0), "(-)2.000", "R", 2.6)
s.text("IN-SITU BASALT - NEVER ON BACKFILL", FS(FL / 2, -240), SM,
       "S-TEXT", "C")
s.text("ANCHORAGE 526 + 128 BEND = 654 > Ld,comp 592",
       FS(FL / 2, S.FTG_T + 870), SM, "S-TEXT", "C")
s.tag(FS(FL + 340, S.FTG_T + 460), "SC01", FS(FL / 2 + UBC, S.FTG_T + 460))
s.tag(FS(-470, BOT), "SF01", FS(B0, BOT))
s.dim_h(FS(FL / 2 + H, S.FTG_T), FS(FL, S.FTG_T), 101.0, SC_FTG, "A2-DIM-S")
s.dim_v(FS(FL, 0), FS(FL, S.FTG_T), FS(FL, 0)[0] + 22.0, SC_FTG, "A2-DIM-S")
s.view_title(164.0, V4_TTL, "5", "ISOLATED FOOTING F1 - SECTION 1-1",
             "1 : 20   600 DEPTH SET BY STARTER ANCHORAGE, NOT BY BENDING "
             "OR SHEAR", 272.0)

# =====================================================================  TABLES
y = 383.0
y = s.table(RCOL, y, RCOL_W, S.FOOTING_SCHEDULE, title="FOOTING SCHEDULE",
            header=["MARK", "No.", "SIZE", "FOUNDING", "TOP", "COVER", "d",
                    "REINFORCEMENT"],
            rh=4.0, align=["C", "C", "C", "C", "C", "C", "C", "C"])
y = s.table(RCOL, y - 5.0, RCOL_W, S.SLAB_SCHEDULE,
            title="SLAB S1 - ELEMENT SCHEDULE",
            header=["ELEMENT", "THK", "COVER", "d x / d y", "REINFORCEMENT",
                    "BASIS"],
            rh=4.0, align=["L", "C", "C", "C", "C", "L"])
y = s.table(RCOL, y - 5.0, RCOL_W, S.rows("FOOTING F1", "SLAB S1"),
            title="BAR MARK SCHEDULE - FOOTING F1 AND SLAB S1",
            header=["MARK", "BAR", "SPACING", "LOCATION", "CUT mm", "No."],
            rh=4.0, align=["C", "C", "C", "L", "C", "C"])
y = s.table(RCOL, y - 5.0, RCOL_W, S.ANNEXD_CHECK,
            title="IS 456 ANNEX D - TWO-WAY SLAB DETAILING",
            header=["CLAUSE", "REQUIREMENT", "AS DETAILED"],
            rh=3.8, align=["L", "L", "L"])

y = s.panel(RCOL, y - 5.0, RCOL_W,
            "DECLARED DETAILING DECISIONS AND OPEN ITEMS", S.DECISIONS_09,
            lead=2.55, h=1.85)
y = s.panel(RCOL, y - 4.0, RCOL_W, "DESIGN BASIS - THIS SHEET", S.BASIS_09,
            lead=2.55, h=1.85)
assert y > 35.0, f"panels overflow the frame: bottom at {y:.1f}"


if __name__ == "__main__":
    out = os.path.join(ROOT, "Presentation Sheets", "DXF",
                       "STR009_Structural_Reinforcement_Detailing_"
                       "Sentry_Post_Footing_and_Slab.dxf")
    s.save(out)
    print("written", out, "| right column bottom y =", round(y, 1))
