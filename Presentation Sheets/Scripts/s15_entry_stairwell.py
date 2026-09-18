"""
s15_entry_stairwell.py  --  STR015  STRUCTURAL REINFORCEMENT DETAILING
                            COVERED ENTRY (APPROACH) STAIRWELL

Four views, in the layout and title block of the supplied Revit A2 set
(ARCH001..ARCH005), so SHEET 15 reads as another sheet of that same series:

    1  ENTRY STAIRWELL - LONGITUDINAL SECTION B-B              1 : 50
    2  ENTRY STAIRWELL - PLAN                                  1 : 50
    3  THE OPENING CORNER AT THE TOP OF THE FLIGHT             1 : 20
    4  SECTIONS c-c, d-d, e-e, f-f                             1 : 10

Geometry is read from sc_proj.ASW; design from master B.6; detailing from
master F.2; loads from A.7.6.  EVERY BAR MARK E01..E12 IS READ FROM
Structural CAD/Scripts/rebar_data.py through sheet_data.entrance_marks(),
so a mark cannot appear on a view without a schedule entry.

*** THIS STRUCTURE IS OUTSIDE THE PROTECTIVE BOUNDARY AND IS NOT BLAST RATED
(Rev F drawing note 8).  It is expected to be LOST in the design event and is
designed to IS 456 with NORMAL partial factors, not with IS 4991 dynamic
strengths.  The 150 EMP bar-spacing rule is a requirement of the protective
envelope and does not reach here; spacing is 200 throughout. ***

VIEW 3 IS THE POINT OF THE SHEET.  At the top of the flight the tension face
turns through 209 degrees.  A bar bent round that corner has its bend
resultant directed OUT of the concrete: it spalls the cover and the bar loses
anchorage.  Master B.6 calls it "the detail most often got wrong".  Main bars
are NOT bent round it -- each layer runs straight, CROSSED, anchored Ld = 640
into the OPPOSITE face, with the U-bar E12 across the corner (SP 34 Cl. 5.5).
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

A = P.ASW
X0, X1, Y0, Y1 = A["x0"], A["x1"], A["y0"], A["y1"]          # 9250..16050, 5750..7750
IX0, IX1, IY0, IY1 = A["ix0"], A["ix1"], A["iy0"], A["iy1"]
TW, TR, TRA = A["t_wall"], A["t_roof"], A["t_raft"]          # 250, 250, 300
LAND0, LAND1 = A["top_landing"]                              # 9500, 11000
FL0, FL1 = A["flight"]                                       # 11000, 14300
PL0, PL1 = A["platform"]                                     # 14300, 15800
NR, RISE, GOING = A["risers"], A["riser"], A["going"]         # 12, 166.6667, 300
WAIST, WIDTH = A["waist"], A["width"]                        # 250, 1500
DOOR_W, DOOR_H = A["door"]                                   # 1000, 2100
L_TOP, L_PLAT = 0.000, -2.000                                # landing / platform
SOF = 2200.0                                                 # roof soffit over the flight
CV_I, CV_E = 30.0, 50.0

SC_B, B1X, D1, V1_TTL = 50.0, 62.0, 334.0, 250.0             # V1 long section
SC_P, P2X, P2Y, V2_TTL = 50.0, 62.0, 168.0, 152.0            # V2 plan
SC_C, C3X, C3D, V3_TTL = 20.0, 237.0, 294.0, 152.0           # V3 corner detail
SC_S, SEC_Y, V4_TTL = 10.0, 66.0, 42.0                       # V4 sections
SEC_X = (46.0, 113.0, 180.0, 247.0)


def BB(mx, lvl):
    """V1: model X and level in metres -> paper."""
    return (B1X + (mx - X0) / SC_B, D1 + lvl * 1000.0 / SC_B)


def PP(mx, my):
    return (P2X + (mx - X0) / SC_P, P2Y + (my - Y0) / SC_P)


def CC(mx, lvl):
    """V3: the opening corner, 1:20, model X and level -> paper."""
    return (C3X + (mx - FL1) / SC_C, C3D + lvl * 1000.0 / SC_C)


def step_top(mx):
    """Level of the flight's stepped top surface at model X."""
    if mx <= FL0:
        return L_TOP
    if mx >= FL1:
        return L_PLAT
    n = min(int((mx - FL0) / GOING) + 1, NR)
    return L_TOP - n * RISE / 1000.0


# AS1-F1: master B.6 designs the flight as a SPANNING slab (Leff 4800, IS 456
# Cl. 33.1(b)) and separately specifies a "stepped RC raft 300 on compacted
# fill".  It does NOT state the vertical relationship between the two.  Drawing
# them in contact would make the flight ground-bearing and contradict its own
# span; so the raft is drawn CLEAR of the flight soffit, on fill, and the gap is
# flagged.  The 400 shown is a drawing convention, not a master value.
RAFT_GAP = 0.400


def rake(mx):
    """Level of the flight's raking centre-line: straight, not stepped."""
    if mx <= FL0:
        return L_TOP
    if mx >= FL1:
        return L_PLAT
    return L_TOP + (L_PLAT - L_TOP) * (mx - FL0) / (FL1 - FL0)


def waist_line(mx):
    """Level of the flight soffit (the waist underside) at model X."""
    if mx <= FL0:
        return L_TOP - WAIST / 1000.0
    if mx >= FL1:
        return L_PLAT - WAIST / 1000.0
    t = (mx - FL0) / (FL1 - FL0)
    return (L_TOP - t * NR * RISE / 1000.0) - WAIST / 1000.0 * 1.144


s = A2Sheet(
    sheet_no="SHEET 15",
    drawing_no="STR015",
    title_lines=["STRUCTURAL", "REINFORCEMENT", "DETAILING -", "COVERED ENTRY",
                 "STAIRWELL"],
    project_lines=["CBRN HARDENED", "UG OPS ROOM"],
    identity=D.IDENTITY,
    notes=D.NOTES_15,
    date="18 SEP 2026",
    drawn="SYN 01",
    checked="DR IR CHAUDHARI",
    scale_note="As indicated",
    rev_note="AS1   18.09.2026",
)

# =====================================================================  VIEW 1
# ENTRY STAIRWELL - LONGITUDINAL SECTION B-B, 1 : 50
XS = [X0 + i * 25.0 for i in range(int((X1 - X0) / 25.0) + 1)]

# -- stepped raft 300 on compacted fill, and the ground each side
s.soil_hatch([BB(X0 - 700, 0.000), BB(X0, 0.000), BB(X0, L_PLAT - 0.600),
              BB(X0 - 700, L_PLAT - 0.600)], scale=0.9)
raft = [BB(mx, waist_line(mx) - RAFT_GAP - TRA / 1000.0) for mx in XS]
s.pline(raft + [BB(X1, L_PLAT - 0.750), BB(X0, L_PLAT - 0.750)],
        "S-EXISTING", True)
s.conc_hatch([BB(mx, waist_line(mx) - RAFT_GAP) for mx in XS]
             + [BB(mx, waist_line(mx) - RAFT_GAP - TRA / 1000.0)
                for mx in reversed(XS)], scale=1.0)
s.pline([BB(mx, waist_line(mx) - RAFT_GAP) for mx in XS]
        + [BB(mx, waist_line(mx) - RAFT_GAP - TRA / 1000.0)
           for mx in reversed(XS)], "S-CONCRETE", True)
s.soil_hatch([BB(mx, waist_line(mx)) for mx in XS]
             + [BB(mx, waist_line(mx) - RAFT_GAP) for mx in reversed(XS)],
             scale=0.7)

# -- the flight: stepped top surface over the raking waist
top = []
for mx in XS:
    top.append(BB(mx, step_top(mx)))
    if FL0 < mx < FL1:
        top.append(BB(mx, step_top(mx + 25.0)))
s.conc_hatch(top + [BB(mx, waist_line(mx)) for mx in reversed(XS)], scale=0.9)
s.pline(top + [BB(mx, waist_line(mx)) for mx in reversed(XS)],
        "S-CONCRETE", True)

# -- side wall beyond the cut, the raking roof, the headwall and the door
s.pline([BB(X0, L_TOP), BB(X0, L_TOP + (SOF + TR) / 1000.0),
         BB(IX0, L_TOP + (SOF + TR) / 1000.0), BB(IX0, L_TOP)],
        "S-CONCRETE", True)
s.conc_hatch([BB(X0, L_TOP), BB(IX0, L_TOP),
              BB(IX0, L_TOP + (SOF + TR) / 1000.0),
              BB(X0, L_TOP + (SOF + TR) / 1000.0)], scale=0.8)
s.rect(*BB(X0, L_TOP + DOOR_H / 1000.0), *BB(IX0, L_TOP), "S-HIDDEN")
s.conc_hatch([BB(mx, rake(mx) + SOF / 1000.0) for mx in XS]
             + [BB(mx, rake(mx) + (SOF + TR) / 1000.0) for mx in reversed(XS)],
             scale=0.9)
s.pline([BB(mx, rake(mx) + SOF / 1000.0) for mx in XS]
        + [BB(mx, rake(mx) + (SOF + TR) / 1000.0) for mx in reversed(XS)],
        "S-CONCRETE", True)

# -- reinforcement: E01 flight main, E03 top steel, E09 raft, E05 roof
s.bar([BB(FL0 - 750, L_TOP - (WAIST - CV_I) / 1000.0)]
      + [BB(mx, waist_line(mx) + CV_I / 1000.0) for mx in XS
         if FL0 <= mx <= FL1]
      + [BB(FL1 + 750, L_PLAT - (WAIST - CV_I) / 1000.0)], "S-REBAR-MAIN")
s.bar([BB(FL0 - 1200, L_TOP - CV_I / 1000.0)]
      + [BB(mx, step_top(mx) - CV_I / 1000.0) for mx in XS
         if FL0 <= mx <= FL0 + 1200], "S-REBAR-SEC")
s.bar([BB(FL1 - 1200, step_top(FL1 - 1200) - CV_I / 1000.0),
       BB(FL1, L_PLAT - CV_I / 1000.0), BB(FL1 + 1200, L_PLAT - CV_I / 1000.0)],
      "S-REBAR-SEC")
for o in (CV_E, TRA - CV_E):
    s.bar([BB(mx, waist_line(mx) - RAFT_GAP - o / 1000.0) for mx in XS],
          "S-REBAR-DIST")
for o in (CV_I, TR - CV_I):
    s.bar([BB(mx, rake(mx) + (SOF + o) / 1000.0) for mx in XS], "S-REBAR-DIST")

s.level(BB(9600, L_TOP), "0.000", "R", 2.6)
s.level(BB(15150, L_PLAT), "(-)2.000", "R", 2.6)
s.text("12 R @ 166.6667,  GOING 300,  WAIST 250", BB(12650, -0.230), SM,
       "S-TEXT", "C")
s.text("RAKING ROOF 250, SOFFIT 2200 OVER THE FLIGHT", BB(12950, 0.640), SM,
       "S-TEXT", "C")
s.text("STEPPED RAFT 300 ON COMPACTED FILL - CLEAR OF THE FLIGHT (AS1-F1)",
       BB(12650, -2.310), SM, "S-TEXT", "C")
s.text("ENTRY DOOR 1000 x 2100", BB(10450, 1.420), SM, "S-TEXT", "C")
s.text("PLATFORM", BB((PL0 + PL1) / 2, L_PLAT + 0.230), SM, "S-TEXT", "C")
s.text("TOP LANDING", BB(10400, L_TOP + 0.560), SM, "S-TEXT", "C")
s.text("MOVEMENT JOINT", BB(15450, -2.560), SM, "S-TEXT", "MR")
s.dline(BB(X1, L_PLAT + 0.400), BB(X1, L_PLAT - 0.750), "S-CENTER")

s.tag(BB(11750, -0.620), "E01", BB(12200, waist_line(12200) + 0.030))
s.tag(BB(9950, -1.780), "E09A", BB(11000, waist_line(11000) - 0.550))
s.tag(BB(10600, 0.900), "E05A", BB(11800, rake(11800) + 2.325))
s.tag(BB(14150, -1.530), "E03", BB(FL1 + 600, L_PLAT - 0.045))
s.secmark(BB(FL1, L_PLAT + 1.030), "3", "D", 3.0)

s.dim_h(BB(LAND0, L_PLAT), BB(FL0, L_PLAT), 268.0, SC_B, "A2-DIM-S")
s.dim_h(BB(FL0, L_PLAT), BB(FL1, L_PLAT), 268.0, SC_B, "A2-DIM-S")
s.dim_h(BB(FL1, L_PLAT), BB(PL1, L_PLAT), 268.0, SC_B, "A2-DIM-S")
s.dim_h(BB(X0, L_PLAT), BB(X1, L_PLAT), 261.0, SC_B)
s.view_title(44.0, V1_TTL, "1", "ENTRY STAIRWELL - LONGITUDINAL SECTION B-B",
             "1 : 50   CUT ON THE 1500 WIDTH CENTRELINE, LOOKING NORTH", 272.0)

# =====================================================================  VIEW 2
# ENTRY STAIRWELL - PLAN, 1 : 50
s.rect(*PP(X0, Y0), *PP(X1, Y1), "S-CONCRETE")
s.rect(*PP(IX0, IY0), *PP(IX1, IY1), "S-CONCRETE")
for wx0, wx1, wy0, wy1 in ((X0, X1, Y0, IY0), (X0, X1, IY1, Y1),
                           (X0, IX0, Y0, Y1), (IX1, X1, Y0, Y1)):
    s.conc_hatch([PP(wx0, wy0), PP(wx1, wy0), PP(wx1, wy1), PP(wx0, wy1)],
                 scale=0.5)
for mx in (LAND1, PL0):
    s.line(PP(mx, IY0), PP(mx, IY1), "S-CONCRETE")
for k in range(1, NR):                                       # the 11 goings
    s.line(PP(FL0 + k * GOING, IY0), PP(FL0 + k * GOING, IY1), "S-CONCRETE-THIN")
s.rect(*PP(X0 - 300, IY0), *PP(X0, IY1), "S-EXISTING")        # channel + grating
for k in range(6):
    s.line(PP(X0 - 300 + k * 60, IY0), PP(X0 - 300 + k * 60, IY1), "S-EXISTING")
s.dline(PP(X0, IY0 + 250), PP(X0, IY0 + 250 + DOOR_W), "S-HIDDEN")

mx = IX0 + 100.0
while mx <= IX1 - 100.0:                                     # E02 distribution
    s.bar([PP(mx, IY0 + CV_I), PP(mx, IY1 - CV_I)], "S-REBAR-DIST")
    mx += 200.0
for o in (CV_I, WIDTH - CV_I):                               # E01 main, along X
    s.bar([PP(IX0, IY0 + o), PP(IX1, IY0 + o)], "S-REBAR-MAIN")

s.text("FLIGHT  11 GOINGS @ 300 = 3300", (128.0, 213.0), SM, "S-TEXT", "C")
s.text("TOP LANDING", (82.0, 213.0), SM, "S-TEXT", "C")
s.text("PLATFORM", (174.0, 213.0), SM, "S-TEXT", "C")
s.text("CHANNEL + GRATING AT THE DOOR", (75.0, 229.0), SM, "S-TEXT", "C")
s.text("1500 CLEAR", PP(13000, 6750), SM, "S-TEXT", "C")
s.tag((118.0, 221.0), "E02", PP(12200, IY0 + 200))
s.tag((166.0, 221.0), "E01", PP(14300, IY0 + CV_I))
s.north((193.0, 228.0))
s.dim_h(PP(X0, Y0), PP(X1, Y0), 162.0, SC_P)
s.dim_v(PP(X0, Y0), PP(X0, Y1), 54.0, SC_P, "A2-DIM-S")
s.view_title(44.0, V2_TTL, "2", "ENTRY STAIRWELL - PLAN",
             "1 : 50   EXTERNAL 6800 x 2000, INTERNAL 6300 x 1500, WALLS 250",
             200.0)

# =====================================================================  VIEW 3
# THE OPENING CORNER AT THE TOP OF THE FLIGHT, 1 : 20
LP = L_PLAT
CW = 700.0
s.conc_hatch([CC(FL1 - CW, rake(FL1 - CW)), CC(FL1, LP), CC(FL1 + CW, LP),
              CC(FL1 + CW, LP - 0.250),
              CC(FL1 - CW, rake(FL1 - CW) - 0.286)], scale=0.6)
s.pline([CC(FL1 - CW, rake(FL1 - CW)), CC(FL1, LP), CC(FL1 + CW, LP),
         CC(FL1 + CW, LP - 0.250),
         CC(FL1 - CW, rake(FL1 - CW) - 0.286)], "S-CONCRETE", True)

# -- each layer runs STRAIGHT and CROSSED, anchored Ld 640 into the far face
s.bar([CC(FL1 - CW, rake(FL1 - CW) - 0.286 + CV_I / 1000.0),
       CC(FL1 + 640, LP - 0.250 + CV_I / 1000.0)], "S-REBAR-MAIN")
s.bar([CC(FL1 + CW, LP - CV_I / 1000.0),
       CC(FL1 - 640, rake(FL1 - 640) - CV_I / 1000.0)], "S-REBAR-MAIN")
s.bar([CC(FL1 - 260, LP - 0.260), CC(FL1 - 260, LP - 0.030),
       CC(FL1 + 260, LP - 0.030)], "S-REBAR-SEC")             # E12 U-bar
s.bar([CC(FL1 - 320, LP - 0.260), CC(FL1 - 320, LP - 0.090),
       CC(FL1 + 260, LP - 0.090)], "S-REBAR-SEC")

s.note_leader(CC(FL1, LP), (C3X - 2.0, 231.0),
              "209 deg - THE TENSION FACE OPENS HERE", SM, "L")
s.text("MAIN BARS ARE NOT BENT ROUND IT.  EACH", (C3X, 175.0), SM, "S-TEXT", "C")
s.text("LAYER RUNS STRAIGHT, CROSSED, AND IS", (C3X, 171.0), SM, "S-TEXT", "C")
s.text("ANCHORED Ld 640 INTO THE OPPOSITE FACE", (C3X, 167.0), SM, "S-TEXT", "C")
s.tag((C3X - 26.0, 224.0), "E01", CC(FL1 - 640, rake(FL1 - 640) - 0.030))
s.tag((C3X + 26.0, 224.0), "E12", CC(FL1 - 290, LP - 0.060))
s.view_title(206.0, V3_TTL, "3", "THE OPENING CORNER",
             "1 : 20   TOP OF THE FLIGHT, SP 34 Cl. 5.5", 272.0)

# =====================================================================  VIEW 4
# SECTIONS, all 1 : 10
def strip(x, ln, thk, cov, phi, spa, label, sub, extra):
    w, h = ln / SC_S, thk / SC_S
    y0 = SEC_Y
    s.conc_hatch([(x, y0), (x + w, y0), (x + w, y0 + h), (x, y0 + h)], scale=0.5)
    s.rect(x, y0, x + w, y0 + h, "S-CONCRETE")
    for lv in (y0 + h - (cov + phi / 2) / SC_S, y0 + (cov + phi / 2) / SC_S):
        s.line((x + cov / SC_S, lv), (x + w - cov / SC_S, lv), "S-REBAR-MAIN")
        u = cov + spa / 2
        while u <= ln - cov:
            s.bar_dot((x + u / SC_S, lv), phi / 2.0 / SC_S, "S-REBAR-DIST")
            u += spa
    s.dim_v((x + w, y0), (x + w, y0 + h), x + w + 4.5, SC_S, "A2-DIM-S")
    s.text(label, (x + w / 2, 57.5), TXT["mark"], "S-SECTION", "C")
    s.text(sub, (x + w / 2, 53.5), SM, "S-TEXT", "C")
    for i, t in enumerate(reversed([f"T{phi} @ {spa:.0f} EF EW", extra])):
        s.text(t, (x + w / 2, y0 + h + 2.6 + i * 3.0), SM, "S-TEXT", "C")


strip(SEC_X[0], 600, WAIST, CV_I, 16, 200, "c - c", "FLIGHT WAIST 250",
      "T10 @ 200 DISTRIBUTION")
strip(SEC_X[1], 600, TW, CV_E, 12, 200, "d - d", "SIDE WALL 250",
      "MIN STEEL GOVERNS, 31 %")
strip(SEC_X[2], 600, TR, CV_I, 12, 200, "e - e", "RAKING ROOF 250",
      "MIN STEEL GOVERNS, 20 %")

# -- f-f  the entry door lintel, 250 x 350
lx, lw, lh = SEC_X[3], 250 / SC_S, 350 / SC_S
s.conc_hatch([(lx, SEC_Y), (lx + lw, SEC_Y), (lx + lw, SEC_Y + lh),
              (lx, SEC_Y + lh)], scale=0.5)
s.rect(lx, SEC_Y, lx + lw, SEC_Y + lh, "S-CONCRETE")
s.link_rect(lx + CV_I / SC_S, SEC_Y + CV_I / SC_S, lx + lw - CV_I / SC_S,
            SEC_Y + lh - CV_I / SC_S, "S-REBAR-STIRRUP", 0.9)
for lv in (SEC_Y + lh - (CV_I + 14) / SC_S, SEC_Y + (CV_I + 14) / SC_S):
    for i in range(3):
        s.bar_dot((lx + (CV_I + 14 + i * 76.0) / SC_S, lv), 0.6)
s.dim_h((lx, SEC_Y), (lx + lw, SEC_Y), SEC_Y - 4.5, SC_S, "A2-DIM-S")
s.text("f - f", (lx + lw / 2, 57.5), TXT["mark"], "S-SECTION", "C")
s.text("ENTRY DOOR LINTEL", (lx + lw / 2, 53.5), SM, "S-TEXT", "C")
for i, t in enumerate(reversed(["3-T12 T + 3-T12 B", "T8 @ 150 LINKS"])):
    s.text(t, (lx + lw / 2, SEC_Y + lh + 2.6 + i * 3.0), SM, "S-TEXT", "C")
s.view_title(44.0, V4_TTL, "4", "SECTIONS - FLIGHT, WALL, ROOF AND LINTEL",
             "1 : 10   COVER 30 INTERNAL, 50 EARTH FACE", 272.0)

# =====================================================================  TABLES
y = s.table_stack(RCOL, 383.0, 96.0, RCOL_W, [
    dict(rows=D.ELEMENT_ROWS_15, title="ENTRY STAIRWELL - ELEMENT SCHEDULE",
         header=["ELEMENT", "THK", "COVER", "d", "MAIN", "DISTRIB.",
                 "TOP STEEL"],
         align=["L", "C", "C", "C", "L", "C", "L"], pad=2.4),
    dict(rows=D.entrance_marks(),
         title="BAR MARK SCHEDULE - COVERED ENTRY STAIRWELL",
         header=["MARK", "BAR", "SPACING", "LOCATION", "CUT mm", "No."],
         align=["C", "C", "C", "L", "C", "C"]),
    dict(rows=D.ASW_CHECK, title="ENTRY STAIRWELL - DESIGN SUMMARY",
         header=["ELEMENT", "LOAD", "SPAN / BASIS", "M", "Ast,req",
                 "PROVIDED", "UTIL"],
         align=["L", "C", "L", "C", "L", "L", "C"], pad=2.2),
], gap=9.0, rh_max=7.6)
y = s.panel(RCOL, y - 5.0, RCOL_W,
            "CONSTRUCTION REQUIREMENTS THAT ARE DESIGN OUTPUTS, NOT OPTIONS",
            D.PANEL_15, lead=2.45, h=1.88)
assert y > 35.0, f"the right column overflows the frame: bottom at {y:.1f}"

if __name__ == "__main__":
    out = os.path.join(ROOT, "Presentation Sheets", "DXF",
                       "STR015_Structural_Reinforcement_Detailing_"
                       "Covered_Entry_Stairwell.dxf")
    s.save(out)
    print("written", out, "| right column bottom y =", round(y, 1))
