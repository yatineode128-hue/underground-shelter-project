"""
s08_sentry_beam_col.py  --  STR008  STRUCTURAL REINFORCEMENT DETAILING
                            SENTRY POST - BEAMS B1 / B2 AND COLUMN C1

Five views, in the layout and with the title block of the supplied Revit A2 set
(ARCH001..ARCH005), so that SHEET 08 reads as the next sheet of that series:

    1  SENTRY POST - FIRST-FLOOR FRAMING PLAN                 1 : 50
    2  BEAM B1 250 x 450 - LONGITUDINAL SECTION               1 : 40
    3  BEAM B2 250 x 450 - LONGITUDINAL SECTION               1 : 40
    4  SECTIONS a-a, b-b, 3-3, 4-4                            1 : 10
    5  COLUMN C1 350 x 350 - VERTICAL SECTION, FULL HEIGHT    1 : 25

This is the IS 13920:2016 sheet of the project.  The underground box is NOT a
ductile-detailing element (Cl. 10.4 checked and not triggered, master A.7.8);
the sentry post frame is, and every bar on this sheet is set by a clause in the
master Part G register.

Every dimension, level, size, bar and spacing comes from
master/MASTER_PROJECT_STATE.md Parts A.4.8, A.7.7, A.7.8, B.8.1 to B.8.6 and
F.4, through sentry_data.py.  Nothing is invented; the three detailing decisions
the master does not cover are DECLARED on the sheet and logged in Part H (SR2).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "Structural CAD", "Scripts"))

from a2_lib import A2Sheet, TXT                              # noqa: E402
import sentry_data as S                                      # noqa: E402

# ------------------------------------------------------------------- regions
LX0, LX1 = 44.0, 188.0            # left drawing region
KX0, KX1 = 192.0, 272.0           # column strip
RCOL, RCOL_W = 277.0, 183.0       # schedules and panels

SM = 1.7                          # the small annotation height used throughout

# ------------------------------------------------------------- view set-out
SC_PLAN = 50.0                    # V1 framing plan
P1X, P1Y, V1_TTL = 62.0, 284.0, 256.0

SC_BM = 40.0                      # V2 / V3 beam longitudinal sections
BX = 48.0                         # common left edge (outer face of column A)
V2_TTL, V3_TTL = 192.0, 127.0     # B1 above, B2 below

SC_SEC = 10.0                     # V4 sections
SEC_Y, V4_TTL = 66.0, 42.0
SEC_X = (46.0, 82.0, 114.0, 152.0)

SC_COL = 25.0                     # V5 column vertical section
CX, CD, V5_TTL = 226.0, 114.0, 42.0


def PP(mx, my):
    """V1: sentry post plan coordinates (mm) -> paper."""
    return (P1X + mx / SC_PLAN, P1Y + my / SC_PLAN)


def CL(lvl):
    """V5: level in metres -> paper y."""
    return CD + lvl * 1000.0 / SC_COL


def CU(u):
    """V5: u across the column from its centreline (mm) -> paper x."""
    return CX + u / SC_COL


# =====================================================================  SHEET
s = A2Sheet(
    sheet_no="SHEET 08",
    drawing_no="STR008",
    title_lines=["STRUCTURAL", "REINFORCEMENT", "DETAILING OF", "SENTRY POST -",
                 "BEAMS & COLUMN"],
    project_lines=["CBRN HARDENED", "UG OPS ROOM"],
    identity=S.IDENTITY,
    notes=S.NOTES_08,
    date="16 SEP 2026",
    drawn="SYN 01",
    checked="DR IR CHAUDHARI",
    scale_note="As indicated",
    rev_note="SR2   16.09.2026",
)

COLS = [(S.GRID_A, S.GRID_1), (S.GRID_B, S.GRID_1),
        (S.GRID_A, S.GRID_2), (S.GRID_B, S.GRID_2)]
H = S.COL / 2.0                                  # 175
HB = S.BM_B / 2.0                                # 125
IN = HB - S.CV_BEAM - 8 - 8                      # 78, outer bar off the c/l

# =====================================================================  VIEW 1
# SENTRY POST - FIRST-FLOOR FRAMING PLAN, 1 : 50
s.rect(*PP(0, 0), *PP(S.EXT_X, S.EXT_Y), "S-CONCRETE-THIN")
for gy in (S.GRID_1, S.GRID_2):
    s.rect(*PP(S.GRID_A + H, gy - HB), *PP(S.GRID_B - H, gy + HB), "S-CONCRETE")
for gx in (S.GRID_A, S.GRID_B):
    s.rect(*PP(gx - HB, S.GRID_1 + H), *PP(gx + HB, S.GRID_2 - H), "S-CONCRETE")
for cx, cy in COLS:
    s.conc_hatch([PP(cx - H, cy - H), PP(cx + H, cy - H),
                  PP(cx + H, cy + H), PP(cx - H, cy + H)], scale=0.7)
    s.rect(*PP(cx - H, cy - H), *PP(cx + H, cy + H), "S-CONCRETE")

# -- grid centrelines, run out to the bubbles on the left and below
for gx in (S.GRID_A, S.GRID_B):
    s.cline((PP(gx, 0)[0], PP(gx, 0)[1] - 5.0), PP(gx, S.EXT_Y), "S-CENTER")
for gy in (S.GRID_1, S.GRID_2):
    s.cline((PP(0, gy)[0] - 5.0, PP(0, gy)[1]), PP(S.EXT_X, gy), "S-CENTER")

# -- top steel: the two outer bars of every beam, run through the joints (D1)
for gy in (S.GRID_1, S.GRID_2):
    for o in (-IN, IN):
        s.bar([PP(S.GRID_A - H + S.CV_COL + 10, gy + o),
               PP(S.GRID_B + H - S.CV_COL - 10, gy + o)], "S-REBAR-MAIN")
for gx in (S.GRID_A, S.GRID_B):
    for o in (-IN, IN):
        s.bar([PP(gx + o, S.GRID_1 - H + S.CV_COL + 10),
               PP(gx + o, S.GRID_2 + H - S.CV_COL - 10)], "S-REBAR-MAIN")

# -- marks
s.tag(PP(1050, 1150), "SB01", PP(1050, S.GRID_1 + IN))
s.tag(PP(1050, 3850), "SB01", PP(1050, S.GRID_2 - IN))
s.tag(PP(1150, 2500), "SB05", PP(S.GRID_A + IN, 2500))
s.tag(PP(2850, 2500), "SB05", PP(S.GRID_B - IN, 2500))
for cx, cy in COLS:
    s.text("C1", PP(cx, cy), SM, "S-TEXT", "C")
s.text("B1  250 x 450", PP(2600, S.GRID_1 + 330), SM, "S-TEXT", "C")
s.text("B1  250 x 450", PP(2600, S.GRID_2 - 330), SM, "S-TEXT", "C")
s.text("B2  250 x 450", PP(S.GRID_A + 330, 3400), SM, "S-TEXT", "C", 90.0)
s.text("B2  250 x 450", PP(S.GRID_B - 330, 3400), SM, "S-TEXT", "C", 90.0)
s.text("SLAB S1 150 THK", PP(2000, 1800), SM, "S-TEXT", "C")
s.text("SEE SHEET 09", PP(2000, 1500), SM, "S-TEXT", "C")
s.north((PP(3350, 4150)))

# -- grid bubbles
for gx, lab in ((S.GRID_A, "A"), (S.GRID_B, "B")):
    p = (PP(gx, 0)[0], PP(gx, 0)[1] - 7.0)
    s.circle(p, 4.0, "S-GRID")
    s.text(lab, p, TXT["mark"], "S-GRID", "C")
for gy, lab in ((S.GRID_1, "1"), (S.GRID_2, "2")):
    p = (PP(0, gy)[0] - 9.0, PP(0, gy)[1])
    s.circle(p, 4.0, "S-GRID")
    s.text(lab, p, TXT["mark"], "S-GRID", "C")

s.dim_h(PP(S.GRID_A, 0), PP(S.GRID_B, 0), 266.0, SC_PLAN)
s.dim_v(PP(S.EXT_X, S.GRID_1), PP(S.EXT_X, S.GRID_2), 150.0, SC_PLAN)
s.dim_v(PP(S.EXT_X, 0), PP(S.EXT_X, S.EXT_Y), 160.0, SC_PLAN)

s.view_title(LX0, V1_TTL, "1", "SENTRY POST - FIRST-FLOOR FRAMING PLAN",
             "1 : 50   EXTERNAL 4000 x 5000,  GRIDS A-B 3650 c/c,  1-2 4650 c/c",
             LX1)


# =============================================================  VIEWS 2 AND 3
def beam_view(name, clr, n_top, phi_top, n_bot, phi_bot, leg, marks, cuts,
              ttl_y, tag_no, title):
    """One beam longitudinal section at 1:40, outer column face to outer column
    face.  Every length is computed in sentry_data from the master values."""
    top = ttl_y + 41.0                              # paper y of the slab top
    L = clr + 2 * S.COL            # OUTER face of one column to OUTER face of
    assert abs(L - (clr + 2 * S.COL)) < 1e-9        # the other:  3300 -> 4000

    def B(u, v):
        return (BX + u / SC_BM, top - v / SC_BM)

    # -- columns above and below, and the beam with its slab
    for cu in (0.0, L - S.COL):
        s.conc_hatch([B(cu, S.BM_D), B(cu + S.COL, S.BM_D),
                      B(cu + S.COL, S.BM_D + 300), B(cu, S.BM_D + 300)],
                     scale=0.45)
        s.rect(*B(cu, S.BM_D + 300), *B(cu + S.COL, S.BM_D), "S-CONCRETE")
        s.rect(*B(cu, 0.0), *B(cu + S.COL, -180.0), "S-CONCRETE")
    s.rect(*B(0.0, S.BM_D), *B(L, 0.0), "S-CONCRETE")
    s.line(B(0.0, S.SLAB_T), B(L, S.SLAB_T), "S-CONCRETE-THIN")

    # -- main steel: D1 continuous, D2 90 deg legs into the column core
    u0, u1 = S.CV_COL + 10.0, L - S.CV_COL - 10.0
    vt = S.CV_BEAM + 8.0 + phi_top / 2.0
    vb = S.BM_D - S.CV_BEAM - 8.0 - phi_bot / 2.0
    s.bar([B(u0, vt + leg), B(u0, vt), B(u1, vt), B(u1, vt + leg)], "S-REBAR-MAIN")
    s.bar([B(u0, vb - leg), B(u0, vb), B(u1, vb), B(u1, vb - leg)], "S-REBAR-MAIN")

    # -- hoops at TRUE spacing: 100 over 2d = 810 from each face, 150 between
    face0, face1 = S.COL, L - S.COL
    pos, u = [], face0 + S.S_FIRST_HOOP
    for _ in range(S.N_HINGE):
        pos.append(u)
        u += S.S_HINGE
    last = pos[-1] - face0
    u = face0 + last + S.S_MID
    while u < face1 - last - 1e-6:
        pos.append(u)
        u += S.S_MID
    pos += [face1 - (p - face0) for p in pos[:S.N_HINGE]]
    for u in pos:
        s.line(B(u, S.CV_BEAM), B(u, S.BM_D - S.CV_BEAM), "S-REBAR-STIRRUP")

    # -- hinge-zone brackets ABOVE the beam, where the span is clear
    for cu, sgn in ((face0, 1), (face1, -1)):
        s.line(B(cu, -90.0), B(cu + sgn * S.HINGE, -90.0), "S-DIM")
        for uu in (cu, cu + sgn * S.HINGE):
            s.line(B(uu, -40.0), B(uu, -140.0), "S-DIM")
    for uu in (face0 + S.HINGE / 2.0, face1 - S.HINGE / 2.0):
        s.text("810 = 2d", B(uu, -160.0), SM, "S-TEXT", "C")
        s.text("T8 2L @ 100", B(uu, -285.0), SM, "S-TEXT", "C")
    s.text("T8 2L @ 150", B(L / 2.0, -285.0), SM, "S-TEXT", "C")
    s.text(f"90 DEG ANCHOR LEG {leg:.0f} (D2)",
           B(L - S.CV_COL - 10.0 - 80.0, S.BM_D + 120.0), SM, "S-TEXT", "MR")

    # -- section cut marks, in their own lane below the beam
    for uu, lab in cuts:
        s.secmark(B(uu, S.BM_D + 180.0), lab, "U", 3.0)

    # -- bar tags, on a clear line above everything else in the band
    ty = top + 12.5
    for mk, uu in marks:
        s.tag((BX + uu / SC_BM, ty), mk, (BX + uu / SC_BM, top + 10.0))

    # -- dimensions and the one level marker
    s.dim_h(B(S.COL, 0), B(L - S.COL, 0), ttl_y + 19.0, SC_BM)
    s.dim_h(B(0, 0), B(L, 0), ttl_y + 12.0, SC_BM)
    s.level(B(L + 60.0, 0.0), "(+)3.650", "R", 2.6)
    s.view_title(LX0, ttl_y, tag_no, title,
                 f"1 : 40   {name} 250 x 450,  CLEAR SPAN {clr:.0f},  d = 404,"
                 f"  {n_top}-T{phi_top} TOP + {n_bot}-T{phi_bot} BOTTOM (D1)",
                 LX1)


beam_view("B1", S.CLR_B1, 4, 16, 2, 16, S.LEG16,
          [("SB01", 900.0), ("SB03", 500.0), ("SB04", 2000.0), ("SB02", 3100.0)],
          [(800.0, "a"), (2000.0, "b")],
          V2_TTL, "2", "BEAM B1 - LONGITUDINAL SECTION  (GRIDS 1 AND 2)")
beam_view("B2", S.CLR_B2, 3, 20, 2, 20, S.LEG20,
          [("SB05", 1000.0), ("SB07", 500.0), ("SB08", 2500.0), ("SB06", 4000.0)],
          [(800.0, "c"), (2500.0, "d")],
          V3_TTL, "3", "BEAM B2 - LONGITUDINAL SECTION  (GRIDS A AND B)")

# =====================================================================  VIEW 4
# SECTIONS, all 1 : 10
def beam_section(x, label, sub, n_top, phi_top, n_bot, phi_bot, hoop):
    w, h = S.BM_B / SC_SEC, S.BM_D / SC_SEC
    y0 = SEC_Y
    s.conc_hatch([(x, y0), (x + w, y0), (x + w, y0 + h), (x, y0 + h)], scale=0.45)
    s.rect(x, y0, x + w, y0 + h, "S-CONCRETE")
    c = (S.CV_BEAM + 4.0) / SC_SEC
    s.link_rect(x + c, y0 + c, x + w - c, y0 + h - c, "S-REBAR-STIRRUP", 0.9)
    for n, phi, at_top in ((n_top, phi_top, True), (n_bot, phi_bot, False)):
        cb = (S.CV_BEAM + 8.0 + phi / 2.0) / SC_SEC
        for i in range(n):
            u = cb + i * (w - 2 * cb) / max(n - 1, 1)
            s.bar_dot((x + u, y0 + h - cb if at_top else y0 + cb),
                      phi / 2.0 / SC_SEC)
    s.dim_h((x, y0), (x + w, y0), y0 - 4.5, SC_SEC, "A2-DIM-S")
    if x == SEC_X[0]:
        s.dim_v((x + w, y0), (x + w, y0 + h), x + w + 4.5, SC_SEC, "A2-DIM-S")
    s.text(label, (x + w / 2.0, 57.5), TXT["mark"], "S-SECTION", "C")
    s.text(sub, (x + w / 2.0, 53.5), SM, "S-TEXT", "C")
    lines = [f"{n_top}-T{phi_top} TOP + {n_bot}-T{phi_bot} BTM", hoop]
    for i, t in enumerate(reversed(lines)):
        s.text(t, (x + w / 2.0, y0 + h + 2.6 + i * 3.0), SM, "S-TEXT", "C")


def col_section(x, label, sub, confining):
    w = S.COL / SC_SEC
    y0 = SEC_Y + 5.0
    s.conc_hatch([(x, y0), (x + w, y0), (x + w, y0 + w), (x, y0 + w)], scale=0.45)
    s.rect(x, y0, x + w, y0 + w, "S-CONCRETE")
    c = S.CV_COL / SC_SEC
    s.link_rect(x + c, y0 + c, x + w - c, y0 + w - c, "S-REBAR-STIRRUP", 1.0)
    if confining:                       # one cross-tie each way -- Cl. 8.1
        m = (S.CV_COL + 10.0) / SC_SEC
        s.line((x + m, y0 + w / 2.0), (x + w - m, y0 + w / 2.0), "S-REBAR-STIRRUP")
        s.line((x + w / 2.0, y0 + m), (x + w / 2.0, y0 + w - m), "S-REBAR-STIRRUP")
    cb = (S.CV_COL + 10.0 + 8.0) / SC_SEC
    for i in range(3):
        for j in range(3):
            if not (i == 1 and j == 1):
                s.bar_dot((x + cb + i * (w - 2 * cb) / 2.0,
                           y0 + cb + j * (w - 2 * cb) / 2.0), 0.8)
    s.dim_h((x, y0), (x + w, y0), y0 - 4.5, SC_SEC, "A2-DIM-S")
    s.text(label, (x + w / 2.0, 57.5), TXT["mark"], "S-SECTION", "C")
    s.text(sub, (x + w / 2.0, 53.5), SM, "S-TEXT", "C")
    lines = (["8-T16   (p = 1.31 %)", "T10 HOOP + 1 CROSS-TIE E/W @ 85"]
             if confining else ["8-T16   (p = 1.31 %)", "T8 HOOP @ 150"])
    for i, t in enumerate(reversed(lines)):
        s.text(t, (x + w / 2.0, y0 + w + 2.6 + i * 3.0), SM, "S-TEXT", "C")


beam_section(SEC_X[0], "a-a / b-b", "BEAM B1", 4, 16, 2, 16, "T8 2L HOOPS")
beam_section(SEC_X[1], "c-c / d-d", "BEAM B2", 3, 20, 2, 20, "T8 2L HOOPS")
col_section(SEC_X[2], "3 - 3", "C1 CONFINING ZONE", True)
col_section(SEC_X[3], "4 - 4", "C1 GENERAL", False)
s.view_title(LX0, V4_TTL, "4", "SECTIONS - BEAMS AND COLUMN",
             "1 : 10   COVER 30 TO BEAMS,  40 TO COLUMNS", LX1)

# =====================================================================  VIEW 5
# COLUMN C1 - VERTICAL SECTION, FULL HEIGHT, 1 : 25
HW = S.COL / 2.0
s.rect(CU(-HW), CL(S.L_FTG_TOP), CU(HW), CL(S.L_ROOF), "S-CONCRETE")
s.conc_hatch([(CU(-HW - 130), CL(S.L_FTG_TOP - 0.130)),
              (CU(HW + 130), CL(S.L_FTG_TOP - 0.130)),
              (CU(HW + 130), CL(S.L_FTG_TOP)),
              (CU(-HW - 130), CL(S.L_FTG_TOP))], scale=0.45)
s.line((CU(-HW - 130), CL(S.L_FTG_TOP)), (CU(HW + 130), CL(S.L_FTG_TOP)),
       "S-CONCRETE")
for lvl_top, lvl_sof in ((S.L_PLINTH, S.L_PB_SOF), (S.L_FF, S.L_FF_SOF),
                         (S.L_ROOF, S.L_ROOF_SOF)):
    for sgn in (-1, 1):
        s.rect(CU(sgn * HW), CL(lvl_sof), CU(sgn * (HW + 130)), CL(lvl_top),
               "S-CONCRETE")
for lvl in (S.L_FF, S.L_ROOF):
    for sgn in (-1, 1):
        s.line((CU(sgn * HW), CL(lvl - S.SLAB_T / 1000.0)),
               (CU(sgn * (HW + 130)), CL(lvl - S.SLAB_T / 1000.0)),
               "S-CONCRETE-THIN")

# -- the eight verticals read as two lines in elevation; splice-free (D3)
UB = HW - S.CV_COL - 10 - 8
for u in (-UB, UB):
    s.bar([(CU(u), CL(S.COL_BAR_TOP)), (CU(u), CL(S.COL_BAR_BOT)),
           (CU(u - (S.COL_BAR_BEND if u > 0 else -S.COL_BAR_BEND)),
            CL(S.COL_BAR_BOT))], "S-REBAR-MAIN")

# -- hoops, at TRUE spacing
inn = HW - S.CV_COL
for a, b in S.CONF_RUNS:
    for k in range(S.nb((b - a) * 1000.0, S.S_CONF)):
        y = CL(a + k * S.S_CONF / 1000.0)
        s.line((CU(-inn), y), (CU(inn), y), "S-REBAR-STIRRUP")
for a, b in S.TIE_ZONES:
    k = 1
    while a + k * S.S_TIE / 1000.0 < b - 1e-9:
        y = CL(a + k * S.S_TIE / 1000.0)
        s.line((CU(-inn), y), (CU(inn), y), "S-REBAR-STIRRUP")
        k += 1

# -- levels on the LEFT, kept short so they stay inside the strip
for lvl, lab in ((S.L_FTG_TOP, "(-)1.400"), (S.L_PLINTH, "(+)0.450"),
                 (S.L_FF, "(+)3.650"), (S.L_ROOF, "(+)6.700")):
    s.line((CU(-HW), CL(lvl)), (CU(-HW) - 5.0, CL(lvl)), "S-LEVEL")
    s.text(lab, (CU(-HW) - 6.0, CL(lvl) + 1.6), SM, "S-LEVEL", "MR")

# -- storey heights on the left, as short vertical labels
for a, b, lab in ((S.L_PLINTH, S.L_FF, "3200"), (S.L_FF, S.L_ROOF, "3050")):
    x = CU(-HW) - 22.0
    s.line((x, CL(a) + 1.0), (x, CL(b) - 1.0), "S-DIM")
    s.text(lab, (x - 1.2, (CL(a) + CL(b)) / 2.0), SM, "S-DIM", "C", 90.0)

# -- confining-zone brackets and labels on the RIGHT
XB = CU(HW) + 3.5
for a, b in S.CONF_RUNS:
    s.line((XB, CL(a)), (XB, CL(b)), "S-DIM")
    for lv in (a, b):
        s.line((XB - 1.2, CL(lv)), (XB + 1.2, CL(lv)), "S-DIM")

s.tag((CU(0) + 34.0, CL(2.150)), "SC01", (CU(UB), CL(2.150)))
s.tag((CU(0) + 34.0, CL(3.430)), "SC02", (XB, CL(3.430)))
s.tag((CU(0) + 34.0, CL(5.050)), "SC04", (XB, CL(5.050)))
s.tag((CU(0) + 34.0, CL(0.250)), "SC03", (XB, CL(0.250)))

s.secmark((CU(0), CL(6.000)), "3", "R", 3.0)
s.secmark((CU(0), CL(5.050)), "4", "R", 3.0)

s.text("PB 250 x 400", (CU(-HW) - 6.0, CL(0.140)), SM, "S-TEXT", "MR")
s.text("SR2-V1", (CU(-HW) - 6.0, CL(-0.080)), SM, "S-TEXT", "MR")
s.text("F1 - SHEET 09", (CU(-HW) - 6.0, CL(-1.490)), SM, "S-TEXT", "MR")
s.text("CONFINING ZONES", (XB + 2.0, CL(6.030)), SM, "S-TEXT", "ML")
s.text("lo = 500 (TYP)", (XB + 2.0, CL(5.830)), SM, "S-TEXT", "ML")
s.text("T10 + CROSS-TIES", (XB + 2.0, CL(4.500)), SM, "S-TEXT", "ML")
s.text("EACH WAY @ 85", (XB + 2.0, CL(4.300)), SM, "S-TEXT", "ML")
s.text("T8 @ 150 BETWEEN", (XB + 2.0, CL(1.600)), SM, "S-TEXT", "ML")
s.text("THROUGH THE JOINT", (XB + 2.0, CL(-0.700)), SM, "S-TEXT", "ML")
s.text("Cl. 8.2 (TYP)", (XB + 2.0, CL(-0.900)), SM, "S-TEXT", "ML")

s.view_title(KX0, V5_TTL, "5", "COLUMN C1",
             "1 : 25   VERTICAL SECTION, FULL HEIGHT", KX1)

# =====================================================================  TABLES
y = 383.0
y = s.table(RCOL, y, RCOL_W, S.BEAM_SCHEDULE,
            title="BEAM SCHEDULE - SENTRY POST FRAME",
            header=["BEAM", "SIZE", "SPAN c/c", "CLEAR", "COVER", "d",
                    "TOP AT SUPP.", "BOTTOM", "HOOPS"],
            rh=4.0, align=["L", "C", "C", "C", "C", "C", "C", "C", "C"])
y = s.table(RCOL, y - 5.0, RCOL_W, S.COLUMN_SCHEDULE,
            title="COLUMN SCHEDULE",
            header=["COL", "SIZE", "LEVELS", "COVER", "VERTICALS", "p",
                    "CONFINING (Cl. 8.1)", "GENERAL TIES"],
            rh=4.0, align=["C", "C", "C", "C", "C", "C", "C", "C"])
y = s.table(RCOL, y - 5.0, RCOL_W, S.rows("BEAM B1", "BEAM B2", "COLUMN C1"),
            title="BAR MARK SCHEDULE - BEAMS B1 / B2 AND COLUMN C1",
            header=["MARK", "BAR", "SPACING", "LOCATION", "CUT mm", "No."],
            rh=3.7, align=["C", "C", "C", "L", "C", "C"])
y = s.table(RCOL, y - 5.0, RCOL_W, S.IS13920_CHECK,
            title="IS 13920:2016 COMPLIANCE - SENTRY POST FRAME",
            header=["CLAUSE", "REQUIREMENT", "PROVIDED", "VERDICT"],
            rh=3.5, align=["L", "L", "L", "C"])

# ------------------------------------------------------------------- panels
y = s.panel(RCOL, y - 5.0, RCOL_W,
            "DECLARED DETAILING DECISIONS AND OPEN ITEMS", S.DECISIONS_08,
            lead=2.38, h=1.72)
y = s.panel(RCOL, y - 4.0, RCOL_W, "DESIGN BASIS - THIS SHEET", S.BASIS_08,
            lead=2.38, h=1.72)
assert y > 35.0, f"panels overflow the frame: bottom at {y:.1f}"


if __name__ == "__main__":
    out = os.path.join(ROOT, "Presentation Sheets", "DXF",
                       "STR008_Structural_Reinforcement_Detailing_"
                       "Sentry_Post_Beams_and_Column.dxf")
    s.save(out)
    print("written", out, "| right column bottom y =", round(y, 1))
