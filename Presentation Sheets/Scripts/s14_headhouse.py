"""
s14_headhouse.py  --  STR014  STRUCTURAL REINFORCEMENT DETAILING
                      ENTRY HEADHOUSE - ROOF 500 AND WALLS HW1 - HW4 400

Five views, in the layout and title block of the supplied Revit A2 set
(ARCH001..ARCH005), so SHEET 14 reads as another sheet of that same series:

    1  HEADHOUSE - ROOF REINFORCEMENT PLAN                     1 : 50
    2  HEADHOUSE - SECTION A-A  (cut in X, looking north)      1 : 50
    3  WALL HW2 - INTERNAL ELEVATION AT THE SECURITY DOOR      1 : 50
    4  SECTIONS b-b, c-c, d-d, e-e                             1 : 20
    5  WALL / ROOF HAUNCH DETAIL                               1 : 20

Geometry is read from sc_proj.HH / HH_DOOR / HH_BAND; design from master
B.7.1 (roof), B.7.2 (walls, conflict C10) and B.7.3 (HW3); detailing from
master F.3; loads from A.7.5.  EVERY BAR MARK H01A..H10 IS READ FROM
Structural CAD/Scripts/rebar_data.py through sheet_data.headhouse_marks(),
so a mark cannot appear on a view without a schedule entry.

The headhouse is INSIDE the protective envelope: M35, Fe500D, 150 max bar
spacing in both curtains (EMP).  Its floor is the top of the 900 pressure
slab at (-)2.000 and its wall starters H10 are cast with that slab, SHEET 06.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "Structural CAD", "Scripts"))

from a2_lib import A2Sheet, TXT                              # noqa: E402
import sheet_data as D                                       # noqa: E402
import sc_proj as P                                          # noqa: E402

RCOL, RCOL_W = 277.0, 183.0
SM = 1.7

HH, DR, BD = P.HH, P.HH_DOOR, P.HH_BAND
X0, X1, Y0, Y1 = HH["x0"], HH["x1"], HH["y0"], HH["y1"]      # 13600..18400, 200..6000
IX0, IX1, IY0, IY1 = HH["ix0"], HH["ix1"], HH["iy0"], HH["iy1"]
TW, TR = HH["t_wall"], HH["t_roof"]                          # 400, 500
L_FLOOR, L_SOF, L_TOP = -2.000, 0.400, 0.900                 # A.4.6
L_SLAB_SOF = -2.900                                          # 900 pressure slab
CV_R, CV_E, CV_I = 75.0, 50.0, 40.0                          # roof / earth / internal
BERM_RUN = 1350.0                                            # 1.5 : 1 to (+)0.900

SC_P, SC_S, SC_E = 50.0, 50.0, 50.0
P1X, P1Y, V1_TTL = 62.0, 266.0, 250.0                        # V1 roof plan
S2X, D2, V2_TTL = 78.0, 210.0, 136.0                         # V2 section A-A
E3X, D3, V3_TTL = 176.0, 306.0, 250.0                        # V3 HW2 elevation
SC_SEC, SEC_Y, V4_TTL = 20.0, 66.0, 42.0                     # V4 sections
SEC_X = (46.0, 114.0, 182.0, 210.0)
SC_H, H5X, H5D = 20.0, 210.0, 183.0                          # V5 haunch detail


def PP(mx, my):
    return (P1X + (mx - X0) / SC_P, P1Y + (my - Y0) / SC_P)


def SA(mx, lvl):
    return (S2X + (mx - X0) / SC_S, D2 + lvl * 1000.0 / SC_S)


def EL(mx, lvl):
    return (E3X + (mx - X0) / SC_E, D3 + lvl * 1000.0 / SC_E)


def HD(mx, lvl):
    """V5: the haunch detail, 1:20, model X and level -> paper."""
    return (H5X + (mx - X0) / SC_H, H5D + lvl * 1000.0 / SC_H)


s = A2Sheet(
    sheet_no="SHEET 14",
    drawing_no="STR014",
    title_lines=["STRUCTURAL", "REINFORCEMENT", "DETAILING -", "ENTRY HEADHOUSE",
                 "ROOF & WALLS"],
    project_lines=["CBRN HARDENED", "UG OPS ROOM"],
    identity=D.IDENTITY,
    notes=D.NOTES_14,
    date="18 SEP 2026",
    drawn="SYN 01",
    checked="DR IR CHAUDHARI",
    scale_note="As indicated",
    rev_note="HH1   18.09.2026",
)

# =====================================================================  VIEW 1
# HEADHOUSE - ROOF REINFORCEMENT PLAN, 1 : 50
s.rect(*PP(X0, Y0), *PP(X1, Y1), "S-CONCRETE")               # roof edge
for gx in (IX0, IX1):                                        # walls below
    s.dline(PP(gx, Y0), PP(gx, Y1), "S-HIDDEN")
for gy in (IY0, IY1):
    s.dline(PP(X0, gy), PP(X1, gy), "S-HIDDEN")

# -- main steel: T20 @ 150 EF EW.  X bars span the 4000 clear and are MAIN
n = 0
my = Y0 + CV_R
while my <= Y1 - CV_R + 1e-6:
    s.bar([PP(X0 + CV_R, my), PP(X1 - CV_R, my)], "S-REBAR-MAIN")
    my += 150.0
    n += 1
mx = X0 + CV_R
while mx <= X1 - CV_R + 1e-6:
    s.bar([PP(mx, Y0 + CV_R), PP(mx, Y1 - CV_R)], "S-REBAR-DIST")
    mx += 150.0

# -- the 1200 end link zones (T12 4L @ 175); the middle is @ 250
for gx in (X0 + 1200, X1 - 1200):
    s.dline(PP(gx, Y0), PP(gx, Y1), "S-REBAR-SEC")
for gy in (Y0 + 1200, Y1 - 1200):
    s.dline(PP(X0, gy), PP(X1, gy), "S-REBAR-SEC")

s.dline(PP(DR["x0"], IY1), PP(DR["x0"], Y1), "S-HIDDEN")     # door below, in HW2
s.dline(PP(DR["x1"], IY1), PP(DR["x1"], Y1), "S-HIDDEN")

s.tag(PP(15200, 4700), "H01A", PP(16400, 4700))
s.tag(PP(15200, 3500), "H01B", PP(16400, 3500))
s.tag(PP(14700, 1150), "H02", PP(X0 + 600, 1150))
s.tag(PP(16200, 2350), "H03", PP(17200, 2350))
s.text("T20 @ 150 EF EW", PP(16100, 5350), SM, "S-TEXT", "C")
s.text("X BARS MAIN (RED), Y SECONDARY (BLUE)", PP(16100, 900), SM, "S-TEXT", "C")
s.text("LINK ZONE 1200", PP(X0 + 600, 3800), SM, "S-TEXT", "C", 90.0)
s.text("SECURITY DOOR BELOW, IN HW2", PP(14900, 5800), SM, "S-TEXT", "C")
s.north((PP(17700, 5300)))
s.secmark((PP(X0, 3100)[0] - 9.0, PP(X0, 3100)[1]), "A", "R")
s.secmark((PP(X1, 3100)[0] + 9.0, PP(X1, 3100)[1]), "A", "L")
s.cline(PP(X0 - 400, 3100), PP(X1 + 400, 3100), "S-CENTER")

s.dim_h(PP(X0, Y0), PP(X1, Y0), 260.0, SC_P)
s.dim_v(PP(X0, Y0), PP(X0, Y1), 47.0, SC_P)
s.view_title(44.0, V1_TTL, "1", "HEADHOUSE - ROOF REINFORCEMENT PLAN",
             "1 : 50   ROOF 500 THK, T20 @ 150 EF EW (2094 mm2/m), COVER 75",
             162.0)

# =====================================================================  VIEW 2
# HEADHOUSE - SECTION A-A, 1 : 50
s.soil_hatch([SA(X0 - BERM_RUN, 0.0), SA(X0, L_TOP), SA(X0, L_FLOOR),
              SA(X0 - BERM_RUN, L_FLOOR)], scale=0.9)
s.soil_hatch([SA(X1, L_TOP), SA(X1 + BERM_RUN, 0.0), SA(X1 + BERM_RUN, L_FLOOR),
              SA(X1, L_FLOOR)], scale=0.9)
s.conc_hatch([SA(X0 - BERM_RUN, L_FLOOR), SA(X1 + BERM_RUN, L_FLOOR),
              SA(X1 + BERM_RUN, L_SLAB_SOF), SA(X0 - BERM_RUN, L_SLAB_SOF)],
             scale=1.1)
s.rect(*SA(X0 - BERM_RUN, L_SLAB_SOF), *SA(X1 + BERM_RUN, L_FLOOR), "S-CONCRETE")
for wx0, wx1 in ((X0, IX0), (IX1, X1)):                      # HW3 west, HW4 east
    s.conc_hatch([SA(wx0, L_FLOOR), SA(wx1, L_FLOOR), SA(wx1, L_SOF),
                  SA(wx0, L_SOF)], scale=0.8)
    s.rect(*SA(wx0, L_FLOOR), *SA(wx1, L_SOF), "S-CONCRETE")
s.conc_hatch([SA(X0, L_SOF), SA(X1, L_SOF), SA(X1, L_TOP), SA(X0, L_TOP)],
             scale=0.8)
s.rect(*SA(X0, L_SOF), *SA(X1, L_TOP), "S-CONCRETE")
for hx, sgn in ((IX0, 1), (IX1, -1)):                        # 300 x 300 haunches
    s.pline([SA(hx, L_SOF), SA(hx + sgn * 300, L_SOF),
             SA(hx, L_SOF - 0.300)], "S-CONCRETE", True)

# -- roof steel, wall steel, haunch diagonals, starters
for lvl in (L_SOF + (CV_R + 10) / 1000.0, L_TOP - (CV_R + 10) / 1000.0):
    s.bar([SA(X0 + CV_R, lvl), SA(X1 - CV_R, lvl)], "S-REBAR-MAIN")
mx = X0 + 200.0
while mx <= X1 - 200.0 + 1e-6:                               # roof links
    end = mx <= X0 + 1200 or mx >= X1 - 1200
    s.line(SA(mx, L_SOF + CV_R / 1000.0), SA(mx, L_TOP - CV_R / 1000.0),
           "S-REBAR-STIRRUP")
    mx += 175.0 if end else 250.0
for wx0, wx1 in ((X0, IX0), (IX1, X1)):
    for u in (wx0 + CV_E, wx1 - CV_I):
        s.bar([SA(u, L_FLOOR - 0.150), SA(u, L_SOF)], "S-REBAR-MAIN")
    lv = L_FLOOR + 0.250
    while lv <= L_SOF - 0.100:
        s.line(SA(wx0 + CV_E, lv), SA(wx1 - CV_I, lv), "S-REBAR-STIRRUP")
        lv += 0.250
for hx, sgn in ((IX0, 1), (IX1, -1)):
    s.bar([SA(hx, L_SOF - 0.260), SA(hx + sgn * 260, L_SOF)], "S-REBAR-SEC")

s.level(SA(X1 + 700, L_TOP), "(+)0.900", "R", 2.6)
s.level(SA(X1 + 700, L_SOF), "(+)0.400", "R", 2.6)
s.level(SA(X1 + 700, L_FLOOR), "(-)2.000", "R", 2.6)
s.level(SA(X0 - 700, 0.0), "0.000 GRADE", "L", 2.6)
s.text("BERM 1.5 : 1", SA(X0 - 800, 0.330), SM, "S-TEXT", "C")
s.text("BERM 1.5 : 1", SA(X1 + 800, 0.330), SM, "S-TEXT", "C")
s.text("900 PRESSURE SLAB - SHEET 06", SA((X0 + X1) / 2, L_FLOOR - 0.430), SM,
       "S-TEXT", "C")
s.text("NO EARTH COVER ON THE HEADHOUSE ROOF", SA((X0 + X1) / 2, L_TOP + 0.330),
       SM, "S-TEXT", "C")
s.tag(SA(14600, 0.150), "H01C", SA(15400, L_TOP - 0.090))
s.tag(SA(17400, 0.150), "H02", SA(17000, L_SOF + 0.250))
s.tag(SA(14600, -0.700), "H04A", SA(IX0 - CV_I, -0.700))
s.tag(SA(17400, -0.700), "H06", SA(IX1 - 130, L_SOF - 0.130))
s.tag(SA(14600, -1.700), "H10", SA(IX0 - CV_I, L_FLOOR - 0.150))
s.dim_h(SA(X0, L_FLOOR), SA(X1, L_FLOOR), 146.0, SC_S)
s.dim_v(SA(X0, L_FLOOR), SA(X0, L_SOF), 60.0, SC_S, "A2-DIM-S")
s.view_title(44.0, V2_TTL, "2", "HEADHOUSE - SECTION A-A",
             "1 : 50   CUT IN X, LOOKING NORTH", 200.0)

# =====================================================================  VIEW 3
# WALL HW2 - INTERNAL ELEVATION AT THE SECURITY DOOR, 1 : 50
s.rect(*EL(X0, L_FLOOR), *EL(X1, L_TOP), "S-CONCRETE")
s.line(EL(X0, L_SOF), EL(X1, L_SOF), "S-CONCRETE")
dx0, dx1 = DR["x0"], DR["x1"]
dhead = L_FLOOR + DR["h"] / 1000.0                           # (-)2.000 + 2.100
s.rect(*EL(dx0, L_FLOOR), *EL(dx1, dhead), "S-CONCRETE")
s.line(EL(dx0, L_FLOOR), EL(dx1, dhead), "S-CENTER")
s.line(EL(dx0, dhead), EL(dx1, L_FLOOR), "S-CENTER")
s.rect(*EL(dx0 - BD["ext"], dhead), *EL(dx1 + BD["ext"], L_TOP), "S-REBAR-SEC")

mx = X0 + CV_I
while mx <= X1 - CV_I + 1e-6:                                # H04A verticals
    if not (dx0 - 40 < mx < dx1 + 40):
        s.bar([EL(mx, L_FLOOR), EL(mx, L_SOF)], "S-REBAR-MAIN")
    mx += 150.0
lv = L_FLOOR + 0.150
while lv <= L_SOF - 0.100:                                   # H04B horizontals
    s.bar([EL(X0 + CV_I, lv), EL(dx0, lv)], "S-REBAR-DIST")
    s.bar([EL(dx1, lv), EL(X1 - CV_I, lv)], "S-REBAR-DIST")
    lv += 0.150
for u in (dx0, dx1):                                         # H07 jamb bars
    for o in (-70, 70):
        s.bar([EL(u + o, L_FLOOR), EL(u + o, dhead + 0.800)], "S-REBAR-SEC")
for lvl in (dhead + 0.060, L_TOP - 0.060):                   # H08 edge band
    s.bar([EL(dx0 - BD["ext"], lvl), EL(dx1 + BD["ext"], lvl)], "S-REBAR-MAIN")
mx = dx0 - BD["ext"] + 75.0
while mx <= dx1 + BD["ext"] - 75.0 + 1e-6:                   # H09 links @ 150
    s.line(EL(mx, dhead + 0.040), EL(mx, L_TOP - 0.040), "S-REBAR-STIRRUP")
    mx += 150.0

s.text("SECURITY DOOR 900 x 2100 - NOT BLAST RATED",
       EL((dx0 + dx1) / 2, L_FLOOR + 0.900), SM, "S-TEXT", "C")
s.text("400 x 800 EDGE BAND, 600 EACH SIDE", EL(16900, dhead + 0.400), SM,
       "S-TEXT", "C")
s.tag((196.0, 334.0), "H08", EL(dx1 + BD["ext"], dhead + 0.060))
s.tag((214.0, 334.0), "H07", EL(dx0 - 70, -0.300))
s.tag((232.0, 334.0), "H04B", EL(X1 - CV_I, -0.300))
s.tag((250.0, 334.0), "H05", EL(17400, -1.360))
s.dim_h(EL(dx0, L_FLOOR), EL(dx1, L_FLOOR), 260.0, SC_E, "A2-DIM-S")
s.view_title(168.0, V3_TTL, "3", "WALL HW2 - INTERNAL ELEVATION",
             "1 : 50   400 THK, T16 @ 150 EF EW, AT THE SECURITY DOOR", 272.0)

# =====================================================================  VIEW 4
# SECTIONS, all 1 : 20
def strip(x, ln, thk, cov_t, cov_b, phi, spa, label, sub, link, nlink):
    """A slab / wall strip in section: bars along the cut drawn as lines, the
    perpendicular curtain seen end-on as dots, and the link cage."""
    w, h = ln / SC_SEC, thk / SC_SEC
    y0 = SEC_Y
    s.conc_hatch([(x, y0), (x + w, y0), (x + w, y0 + h), (x, y0 + h)], scale=0.45)
    s.rect(x, y0, x + w, y0 + h, "S-CONCRETE")
    for lv, cv in ((y0 + h - (cov_t + phi / 2) / SC_SEC, cov_t),
                   (y0 + (cov_b + phi / 2) / SC_SEC, cov_b)):
        s.line((x + cov_b / SC_SEC, lv), (x + w - cov_b / SC_SEC, lv),
               "S-REBAR-MAIN")
        u = cov_b + spa / 2
        while u <= ln - cov_b:
            s.bar_dot((x + u / SC_SEC, lv), phi / 2.0 / SC_SEC, "S-REBAR-DIST")
            u += spa
    u = cov_b + 60.0
    for _ in range(nlink):
        s.line((x + u / SC_SEC, y0 + cov_b / SC_SEC),
               (x + u / SC_SEC, y0 + h - cov_t / SC_SEC), "S-REBAR-STIRRUP")
        u += (ln - 2 * cov_b - 120.0) / max(nlink - 1, 1)
    s.dim_v((x + w, y0), (x + w, y0 + h), x + w + 4.5, SC_SEC, "A2-DIM-S")
    s.text(label, (x + w / 2, 57.5), TXT["mark"], "S-SECTION", "C")
    s.text(sub, (x + w / 2, 53.5), SM, "S-TEXT", "C")
    for i, t in enumerate(reversed([f"T{phi} @ {spa:.0f} EF EW", link])):
        s.text(t, (x + w / 2, y0 + h + 2.6 + i * 3.0), SM, "S-TEXT", "C")


strip(SEC_X[0], 1200, TR, CV_R, CV_R, 20, 150, "b - b", "ROOF 500",
      "T12 4L @ 175 / 250", 6)
strip(SEC_X[1], 1200, TW, CV_I, CV_E, 16, 150, "c - c", "WALLS HW1 - HW4 400",
      "T12 4L @ 250 THROUGHOUT", 5)

# -- d-d  the 400 x 800 door-head edge band
bx, bw, bh = SEC_X[2], BD["b"] / SC_SEC, BD["d"] / SC_SEC
s.conc_hatch([(bx, SEC_Y), (bx + bw, SEC_Y), (bx + bw, SEC_Y + bh),
              (bx, SEC_Y + bh)], scale=0.45)
s.rect(bx, SEC_Y, bx + bw, SEC_Y + bh, "S-CONCRETE")
s.link_rect(bx + CV_I / SC_SEC, SEC_Y + CV_I / SC_SEC,
            bx + bw - CV_I / SC_SEC, SEC_Y + bh - CV_I / SC_SEC,
            "S-REBAR-STIRRUP", 0.9)
for lv in (SEC_Y + bh - (CV_I + 22) / SC_SEC, SEC_Y + (CV_I + 22) / SC_SEC):
    for i in range(4):
        s.bar_dot((bx + (CV_I + 22 + i * 96.0) / SC_SEC, lv), 0.5)
s.dim_h((bx, SEC_Y), (bx + bw, SEC_Y), SEC_Y - 4.5, SC_SEC, "A2-DIM-S")
s.text("d - d", (bx + bw / 2, 57.5), TXT["mark"], "S-SECTION", "C")
s.text("DOOR-HEAD BAND", (bx + bw / 2, 53.5), SM, "S-TEXT", "C")
for i, t in enumerate(reversed(["4-T20 T + 4-T20 B", "T12 4L @ 150"])):
    s.text(t, (bx + bw / 2, SEC_Y + bh + 2.6 + i * 3.0), SM, "S-TEXT", "C")

# -- e-e  plan section through HW2 at a door jamb
jx, jw, jh = SEC_X[3], 1200 / SC_SEC, TW / SC_SEC
s.conc_hatch([(jx, SEC_Y), (jx + jw, SEC_Y), (jx + jw, SEC_Y + jh),
              (jx, SEC_Y + jh)], scale=0.45)
s.rect(jx, SEC_Y, jx + jw, SEC_Y + jh, "S-CONCRETE")
s.line((jx + 600 / SC_SEC, SEC_Y), (jx + 600 / SC_SEC, SEC_Y + jh), "S-CENTER")
for lv in (SEC_Y + (CV_E + 8) / SC_SEC, SEC_Y + jh - (CV_I + 8) / SC_SEC):
    for o in (70.0, 210.0):
        s.bar_dot((jx + (600 - o) / SC_SEC, lv), 0.5)
    u = 660.0
    while u <= 1200 - CV_E:
        s.bar_dot((jx + u / SC_SEC, lv), 0.4, "S-REBAR-DIST")
        u += 150.0
s.dim_v((jx + jw, SEC_Y), (jx + jw, SEC_Y + jh), jx + jw + 4.5, SC_SEC, "A2-DIM-S")
s.text("e - e", (jx + jw / 2, 57.5), TXT["mark"], "S-SECTION", "C")
s.text("DOOR JAMB IN HW2", (jx + jw / 2, 53.5), SM, "S-TEXT", "C")
for i, t in enumerate(reversed(["2-T20 EACH JAMB, EACH FACE", "Ld 800 BEYOND"])):
    s.text(t, (jx + jw / 2, SEC_Y + jh + 2.6 + i * 3.0), SM, "S-TEXT", "C")
s.view_title(44.0, V4_TTL, "4", "SECTIONS - ROOF, WALL, DOOR HEAD AND JAMB",
             "1 : 20   COVER 75 ROOF, 50 EARTH FACE, 40 INTERNAL", 270.0)

# =====================================================================  VIEW 5
# WALL / ROOF HAUNCH DETAIL, 1 : 20
HB, HT = L_SOF - 0.900, X0 + 900                             # break level, extent
s.conc_hatch([HD(X0, HB), HD(IX0, HB), HD(IX0, L_SOF), HD(X0, L_SOF)], scale=0.5)
s.conc_hatch([HD(X0, L_SOF), HD(HT, L_SOF), HD(HT, L_TOP), HD(X0, L_TOP)],
             scale=0.5)
s.conc_hatch([HD(IX0, L_SOF), HD(IX0 + 300, L_SOF), HD(IX0, L_SOF - 0.300)],
             scale=0.5)
s.pline([HD(X0, HB), HD(X0, L_TOP), HD(HT, L_TOP), HD(HT, L_SOF),
         HD(IX0 + 300, L_SOF), HD(IX0, L_SOF - 0.300), HD(IX0, HB)],
        "S-CONCRETE", True)
s.line(HD(X0, L_SOF), HD(IX0, L_SOF), "S-HIDDEN")            # soffit line, hidden
for u in (X0, IX0):                                          # break line at the cut
    s.dline(HD(u - 60, HB), HD(u + 60, HB), "S-CENTER", 1.2, 0.8)

for lvl in (L_SOF + (CV_R + 10) / 1000.0, L_TOP - (CV_R + 10) / 1000.0):
    s.bar([HD(X0 + CV_R, lvl), HD(HT, lvl)], "S-REBAR-MAIN")
for u in (X0 + CV_E, IX0 - CV_I):
    s.bar([HD(u, HB), HD(u, L_SOF + 0.030)], "S-REBAR-MAIN")
for k in range(3):                                           # H06 diagonals @ 150
    o = 40.0 + k * 150.0
    s.bar([HD(IX0 - 40, L_SOF - 0.300 + o / 1000.0),
           HD(IX0 + 300 - o, L_SOF - 0.040)], "S-REBAR-SEC")

s.dim_h(HD(IX0, L_SOF), HD(IX0 + 300, L_SOF), HD(0, L_SOF)[1] + 7.0, SC_H,
        "A2-DIM-S")
s.dim_v(HD(IX0, L_SOF - 0.300), HD(IX0, L_SOF), HD(IX0 + 300, 0)[0] + 7.0,
        SC_H, "A2-DIM-S")
s.tag((HD(X0, 0)[0] - 8.0, HD(0, L_SOF - 0.170)[1]), "H06",
      HD(IX0 + 120, L_SOF - 0.150))
s.text("300 x 300 HAUNCH, ALL 4 JUNCTIONS", HD(X0 + 450, L_TOP + 0.120), SM,
       "S-TEXT", "C")
s.text("TOP STEEL Ld 800 INTO THE WALL", (HD(X0 + 450, 0)[0], 152.0), SM,
       "S-TEXT", "C")
s.view_title(206.0, V2_TTL, "5", "WALL / ROOF HAUNCH",
             "1 : 20   DIAGONAL T16 @ 150", 272.0)

# =====================================================================  TABLES
y = s.table_stack(RCOL, 383.0, 92.0, RCOL_W, [
    dict(rows=D.ELEMENT_ROWS_14, title="HEADHOUSE - ELEMENT SCHEDULE",
         header=["ELEMENT", "THK", "COVER", "d", "MAIN REINFORCEMENT", "LINKS"],
         align=["L", "C", "C", "C", "L", "L"]),
    dict(rows=D.headhouse_marks(),
         title="BAR MARK SCHEDULE - HEADHOUSE ROOF 500 AND WALLS 400",
         header=["MARK", "BAR", "SPACING", "LOCATION", "CUT mm", "No."],
         align=["C", "C", "C", "L", "C", "C"]),
    dict(rows=D.HH_CHECK, title="HEADHOUSE - DESIGN SUMMARY",
         header=["ELEMENT", "BASIS", "M or V", "Ast,req / tau_c", "PROVIDED",
                 "UTILISATION"],
         align=["L", "L", "C", "L", "L", "C"], pad=2.4),
], gap=9.0, rh_max=7.6)
y = s.panel(RCOL, y - 5.0, RCOL_W,
            "CONSTRUCTION REQUIREMENTS THAT ARE DESIGN OUTPUTS, NOT OPTIONS",
            D.PANEL_14, lead=2.45, h=1.88)
assert y > 35.0, f"the right column overflows the frame: bottom at {y:.1f}"

if __name__ == "__main__":
    out = os.path.join(ROOT, "Presentation Sheets", "DXF",
                       "STR014_Structural_Reinforcement_Detailing_"
                       "Entry_Headhouse.dxf")
    s.save(out)
    print("written", out, "| right column bottom y =", round(y, 1))
