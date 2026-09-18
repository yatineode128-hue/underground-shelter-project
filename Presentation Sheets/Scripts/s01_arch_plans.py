"""
s01_arch_plans.py  --  ARCH001  UNDERGROUND LEVEL PLAN, HEADHOUSE LEVEL PLAN,
                       GROUND LEVEL PLAN AND LONGITUDINAL SECTION

A REDRAW of sheet 1 of the owner's Revit A2 set: the same three plans, at the
same scales, in the same frame and title block, with every dimension brought to
the project's own authoritative data (master A.3, A.4.2 - A.4.9, A.7.3).  A
longitudinal section is added because three plans cannot show a level, and the
levels are one of the things the redraw corrects.

    1  UNDERGROUND LEVEL PLAN  (-)6.100                            1 : 100
    2  HEADHOUSE LEVEL PLAN    (-)2.000                            1 : 100
    3  GROUND LEVEL PLAN        0.000                               1 : 100

All three at the owner's own scale and all three spanning the full 22000 box, so
that both escape shafts appear on every level.  Every corrected figure is
registered in arch_data.CORRECTIONS and in master Part H.  By instruction the
sheet itself carries no revision or amendment text.

COLOUR: dark only, and mostly black - ACI 7, 8, 1, 5.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
for _p in ("Structural CAD", "Drainage"):
    sys.path.insert(0, os.path.join(ROOT, _p, "Scripts"))

from a2_lib import A2Sheet, vw                                # noqa: E402
import arch_data as D                                         # noqa: E402

SC = 100.0
RCOL, RCOL_W, RTOP = 282.0, 178.0, 383.0
RULE_TO, RULE_MID = 272.0, 150.0
SM, SMS = 1.9, 1.75

PX0, VDIM = 47.0, 42.5
V1_Y0, V1_DIM, V1_TTL = 306.0, 300.0, 282.0      # box 306 .. 368
V2_Y0, V2_DIM, V2_TTL = 190.0, 184.0, 172.0      # model Y 0 at 190
V3_Y0, V3_DIM, V3_TTL = 74.0, 68.0, 56.0         # model Y 0 at 74

P1 = vw(SC, PX0, V1_Y0)
P2 = vw(SC, PX0, V2_Y0)
P3 = vw(SC, PX0, V3_Y0)


s = A2Sheet(
    sheet_no="SHEET 01",
    drawing_no="ARCH001",
    title_lines=["UNDERGROUND", "LEVEL PLAN,", "HEADHOUSE LEVEL",
                 "PLAN & GROUND", "LEVEL PLAN"],
    project_lines=D.PROJECT_LINES,
    identity=D.IDENTITY,
    notes=[
        "ALL DIMENSIONS ARE IN MM. ALL LEVELS ARE IN METRES RELATIVE TO "
        "FINISHED SITE GRADE 0.000, NEGATIVE DOWNWARDS.",
        "WRITTEN DIM TO BE FOLLOWED ONLY. DRG NOT TO BE SCALED.",
        "THIS DRG IS TO BE READ IN CONJUNCTION WITH ALL RELEVANT ARCH, STR AND "
        "SERVICES DRGS.",
        "THE PROTECTIVE BOUNDARY IS THE 600 PERIMETER WALLS, THE 900 PRESSURE "
        "SLAB, THE 600 MAT AND WALLS W6 AND W7 AT 400 WITH THEIR TWO BLAST "
        "DOORS. THE HEADHOUSE, THE COVERED ENTRY STAIRWELL AND THE SENTRY "
        "POST ARE OUTSIDE IT AND ARE NOT BLAST RATED.",
        "THE FOUR W8 PARTITIONS ARE NON-STRUCTURAL AND CARRY A PERMANENT 900 "
        "GAP AT Y 2500 - 3400. NO DOOR IS SCHEDULED IN THEM.",
        "MAIN STAIRCASE: 24 RISERS AT 170.8333, TREAD 280, 3 FLIGHTS OF 8, "
        "TOTAL RISE 4100, FLIGHT WIDTH 1200, WELL 200, HEADROOM 2533.",
        "THE ENGINEERED COVER OVER THE PRESSURE SLAB IS 2000 THICK IN SIX "
        "LAYERS AND IS GRADED TO SHED AT GRADE. THERE IS NO ROOF OUTLET.",
        "THIS DRG HAS BEEN PREPARED IN ACCORDANCE WITH EXISTING CODES, NBC OF "
        "INDIA 2016, SOA 2009 AND SEISMIC LOADS.",
        "CONTRACTOR TO CHECK AND VERIFY THE DRG BEFORE EXECUTION.",
    ],
    date=D.DATE,
    drawn=D.DRAWN,
    checked=D.CHECKED,
    scale_note="1 : 100",
)

for _nm, _col, _lw, _desc in [
    ("A-WALL",    7, 35, "Walls, cut"),
    ("A-WALL-IN", 7, 18, "Internal and non-structural walls"),
    ("A-OVER",    8, 18, "Over or below the cut plane"),
    ("A-OPEN",    1, 35, "Doors, openings and shafts through the boundary"),
    ("A-EQUIP",   5, 25, "Fixed equipment and services"),
    ("A-COVER",   8, 18, "Engineered cover, berm and fill"),
]:
    _ly = s.doc.layers.add(_nm)
    _ly.color, _ly.lineweight, _ly.description = _col, _lw, _desc


# =====================================================================  VIEW 1
# UNDERGROUND LEVEL PLAN, 1 : 100
B, I = D.BOX, D.INTR
s.rect(*P1(B["x0"], B["y0"]), *P1(B["x1"], B["y1"]), "A-WALL")
s.rect(*P1(I["x0"], I["y0"]), *P1(I["x1"], I["y1"]), "A-WALL")

for x0, x1 in D.PARTITIONS:                            # W8, 900 gap retained
    for y0, y1 in ((I["y0"], D.PART_DOOR_Y[0]), (D.PART_DOOR_Y[1], I["y1"])):
        s.rect(*P1(x0, y0), *P1(x1, y1), "A-WALL-IN")
s.rect(*P1(D.IW[0][1], I["y0"]), *P1(D.IW[0][2], I["y1"]), "A-WALL-IN")   # W5
BD = D.BLAST_DOOR
for mark, x0, x1, t in D.IW[1:]:                       # W6 and W7, 400
    s.rect(*P1(x0, BD["y1"]), *P1(x1, I["y1"]), "A-WALL")
    s.line(P1(x0, BD["y0"]), P1(x0, BD["y1"]), "A-OPEN")
    s.line(P1(x1, BD["y0"]), P1(x1, BD["y1"]), "A-OPEN")
    s.line(P1(x0, I["y0"]), P1(x1, I["y0"]), "A-WALL")
    s.arc(P1(x1, BD["y0"]), BD["w"] / SC, 0, 90, "A-OPEN")
s.text("BD1", P1(15000, 2100), SMS, "S-TEXT", "C")
s.text("BD2", P1(18200, 2100), SMS, "S-TEXT", "C")

for name, cx, cy, head in D.ESC:                       # escape shafts
    s.circle(P1(cx, cy), D.ESC_CLEAR_D / 2.0 / SC, "A-OPEN")
    s.circle(P1(cx, cy), D.ESC_COLLAR_OD / 2.0 / SC, "A-WALL")
    s.cline(P1(cx - 1500, cy), P1(cx + 1500, cy), "S-CENTER")
    s.cline(P1(cx, cy - 1500), P1(cx, cy + 1500), "S-CENTER")
s.text("ESC 1", P1(D.ESC[0][1], 3400), SMS, "S-TEXT", "C")
s.text("ESC 2", P1(D.ESC[1][1], 3400), SMS, "S-TEXT", "C")

V, PA, ST = D.VOID, D.PAD, D.STAIR                     # bay 7 stair shaft
s.dline(P1(V["x0"], V["y1"]), P1(V["x1"], V["y1"]), "A-OVER")
s.rect(*P1(PA["x0"], PA["y0"]), *P1(PA["x1"], PA["y1"]), "A-OVER")
for fx0, fx1 in (ST["fltA"], ST["fltB"]):
    s.rect(*P1(fx0, ST["L2_y"][0]), *P1(fx1, ST["L1_y"][1]), "A-WALL-IN")
    for k in range(1, 8):
        y = ST["L2_y"][0] + k * (ST["L1_y"][1] - ST["L2_y"][0]) / 8.0
        s.line(P1(fx0, y), P1(fx1, y), "A-WALL-IN")
s.rect(*P1(ST["wellx"][0], ST["L2_y"][0]), *P1(ST["wellx"][1], ST["L1_y"][1]),
       "A-OVER")
s.text("STAIR SHAFT", P1(16600, 5100), SMS, "S-TEXT", "C")

SR = D.SUMP_RECT                                       # SU-01, below floor
for a, b in (((SR[0], SR[1]), (SR[2], SR[1])), ((SR[0], SR[3]), (SR[2], SR[3])),
             ((SR[0], SR[1]), (SR[0], SR[3])), ((SR[2], SR[1]), (SR[2], SR[3]))):
    s.dline(P1(*a), P1(*b), "A-OVER", 1.2, 0.9)
s.rect(*P1(11398, 5600), *P1(12198, 6200), "A-EQUIP")  # service entry plate

for nm, y0, y1 in (("1", 3600, 5600), ("2", 2100, 3600), ("3", 600, 2100)):
    s.line(P1(12800, y0), P1(14800, y0), "A-WALL-IN")
    s.text(nm, P1(13800, (y0 + y1) / 2.0 - 120), SMS, "S-TEXT", "C")
s.text("DECON", P1(13800, 5150), SMS, "S-TEXT", "C")

for n, x0, x1, w, room, name in D.BAYS:                # room references
    s.text(room, P1((x0 + x1) / 2.0, 800), SM, "S-TEXT", "C")
for mark, x0, x1, t in D.IW:                           # wall thickness labels
    s.text(f"{t:.0f}", P1((x0 + x1) / 2.0, 4550), SMS, "S-TEXT", "C", rot=90.0)
s.text("600", P1(300, 3100), SMS, "S-TEXT", "C", rot=90.0)
s.text("600", P1(21700, 3100), SMS, "S-TEXT", "C", rot=90.0)
s.text("110 TYP", P1(3555, 4400), SMS, "S-TEXT", "C", rot=90.0)

s.secmark(P1(-600, 2050), "A", "R")
s.secmark(P1(22600, 2050), "A", "L")
s.cline(P1(-300, 2050), P1(22300, 2050), "S-CENTER")
s.north((274.5, 350.0))

AB = V1_Y0 + B["y1"] / SC
s.note_leader(P1(11798, 6200), (PX0 + 40.0, AB + 11.0),
              "SERVICE ENTRY PLATE, W2 NORTH WALL, X 11398 - 12198", SM, "R")
s.note_leader(P1(16600, 3760), (PX0 + 132.0, AB + 5.5),
              "STAIR VOID OVER 2800 x 3160;  CANTILEVER PAD 2800 x 1840", SM,
              "R")

s.dim_chain_h([P1(v, 0)[0] for v in D.BAY_CHAIN], V1_Y0, V1_DIM, SC,
              "A2-DIM-S")
s.dim_h(P1(0, 0), P1(22000, 0), V1_DIM - 7.0, SC, "A2-DIM-S")
s.dim_v(P1(0, 0), P1(0, 6200), VDIM, SC, "A2-DIM-S")
s.dim_chain_v([P1(0, v)[1] for v in (600, 2500, 3400, 5600)], P1(22000, 0)[0],
              P1(23400, 0)[0], SC, "A2-DIM-S")
s.view_title(PX0 - 4.0, V1_TTL, "1", "UNDERGROUND LEVEL PLAN   (-)6.100",
             "1 : 100   EIGHT BAYS, 22000 x 6200 EXTERNAL", RULE_TO)

# =====================================================================  VIEW 2
# HEADHOUSE LEVEL PLAN, 1 : 100  -- the top of the 900 pressure slab, (-)2.000
def box_below(P):
    """The 22000 x 6200 box footprint, below the cut plane on views 2 and 3."""
    for a_, b_ in (((B["x0"], B["y0"]), (B["x1"], B["y0"])),
                   ((B["x0"], B["y1"]), (B["x1"], B["y1"])),
                   ((B["x0"], B["y0"]), (B["x0"], B["y1"])),
                   ((B["x1"], B["y0"]), (B["x1"], B["y1"]))):
        s.dline(P(*a_), P(*b_), "A-OVER", 1.8, 1.3)


H, A = D.HH, D.ASW
box_below(P2)
s.rect(*P2(H["x0"], H["y0"]), *P2(H["x1"], H["y1"]), "A-WALL")
s.rect(*P2(H["ix0"], H["iy0"]), *P2(H["ix1"], H["iy1"]), "A-WALL")
s.rect(*P2(A["x0"], A["y0"]), *P2(A["x1"], A["y1"]), "A-WALL")
s.rect(*P2(A["ix0"], A["iy0"]), *P2(A["ix1"], A["iy1"]), "A-WALL")
s.rect(*P2(V["x0"], V["y0"]), *P2(V["x1"], V["y1"]), "A-OPEN")
s.line(P2(V["x0"], V["y0"]), P2(V["x1"], V["y1"]), "S-CENTER")
s.line(P2(V["x0"], V["y1"]), P2(V["x1"], V["y0"]), "S-CENTER")
s.rect(*P2(PA["x0"], PA["y0"]), *P2(PA["x1"], PA["y1"]), "A-OVER")
s.line(P2(H["ix0"], H["iy1"]), P2(D.HH_DOOR["x0"], H["iy1"]), "A-WALL")
s.line(P2(D.HH_DOOR["x1"], H["iy1"]), P2(H["ix1"], H["iy1"]), "A-WALL")
s.arc(P2(D.HH_DOOR["x0"], H["iy1"]), D.HH_DOOR["w"] / SC, 0, 90, "A-OPEN")
s.line(P2(A["top_landing"][1], A["iy0"]), P2(A["top_landing"][1], A["iy1"]),
       "A-WALL-IN")
for k in range(1, 12):
    x = A["flight"][0] + k * (A["flight"][1] - A["flight"][0]) / 12.0
    s.line(P2(x, A["iy0"]), P2(x, A["iy1"]), "A-WALL-IN")
s.line(P2(A["platform"][0], A["iy0"]), P2(A["platform"][0], A["iy1"]),
       "A-WALL-IN")
s.rect(*P2(A["channel"][0], A["iy0"]), *P2(A["channel"][1], A["iy1"]),
       "A-EQUIP")
s.arc(P2(A["x0"], A["iy0"]), A["door"][0] / SC, 0, 90, "A-OPEN")
for name, cx, cy, head in D.ESC:
    s.circle(P2(cx, cy), D.ESC_CLEAR_D / 2.0 / SC, "A-OPEN")
    s.circle(P2(cx, cy), D.ESC_COLLAR_OD / 2.0 / SC, "A-WALL")
    s.text(name, P2(cx, cy - 1500), SMS, "S-TEXT", "C")
s.text("VOID", P2(16600, 2050), SMS, "S-TEXT", "C")
s.text("D1", P2(14900, 4700), SMS, "S-TEXT", "C")
s.text("D2", P2(9820, 6300), SMS, "S-TEXT", "C")
s.text("HEADHOUSE", P2(16000, 5150), SMS, "S-TEXT", "C")
s.text("PLATFORM  (-)2.000", P2(15050, 7150), SMS, "S-TEXT", "C")
s.text("12R AT 166.6667, GOING 300", P2(12650, 8100), SMS, "S-TEXT", "C")
s.text("TOP LANDING  0.000", P2(10250, 7150), SMS, "S-TEXT", "C")
s.text("ENGINEERED COVER OVER THE PRESSURE SLAB", P2(6000, 3100), SMS,
       "S-TEXT", "C")
s.dim_chain_h([P2(v, 0)[0] for v in (8950, 9250, 9500, 11000, 14300, 15800,
                                     16050)], P2(0, A["y0"])[1],
              P2(0, 4200)[1], SC, "A2-DIM-S")
s.dim_chain_h([P2(v, 0)[0] for v in (H["x0"], H["ix0"], H["ix1"], H["x1"])],
              P2(0, H["y0"])[1], P2(0, -600)[1], SC, "A2-DIM-S")
s.dim_v(P2(H["x1"], H["y0"]), P2(H["x1"], H["y1"]), P2(19100, 0)[0], SC,
        "A2-DIM-S")
s.dim_v(P2(A["x1"], A["y0"]), P2(A["x1"], A["y1"]), P2(16800, 0)[0], SC,
        "A2-DIM-S")
s.view_title(PX0 - 4.0, V2_TTL, "2", "HEADHOUSE LEVEL PLAN   (-)2.000",
             "1 : 100   HEADHOUSE 4800 x 5800;  ENTRY STAIRWELL 6800 x 2000",
             RULE_TO)

# =====================================================================  VIEW 3
# GROUND LEVEL PLAN, 0.000
box_below(P3)
s.rect(*P3(H["x0"], H["y0"]), *P3(H["x1"], H["y1"]), "A-WALL")
s.rect(*P3(A["x0"], A["y0"]), *P3(A["x1"], A["y1"]), "A-WALL")
s.dline(P3(A["x0"] - 1350, A["y0"]), P3(A["x0"] - 1350, A["y1"]), "A-COVER")
for name, cx, cy, head in D.ESC:
    s.circle(P3(cx, cy), D.ESC_CLEAR_D / 2.0 / SC, "A-OPEN")
    s.circle(P3(cx, cy), D.ESC_COLLAR_OD / 2.0 / SC, "A-WALL")
    s.cline(P3(cx - 1400, cy), P3(cx + 1400, cy), "S-CENTER")
    s.cline(P3(cx, cy - 1400), P3(cx, cy + 1400), "S-CENTER")
    s.text(f"{name} HEAD  {head:+.3f}", P3(cx, cy - 1750), SMS, "S-TEXT", "C")
    s.text("1400 DIA CLEAR", P3(cx, cy - 2150), SMS, "S-TEXT", "C")
s.text("HEADHOUSE ROOF  +0.900", P3(16000, 3100), SMS, "S-TEXT", "C")
s.text("STAIRWELL ROOF", P3(12600, 6750), SMS, "S-TEXT", "C")
s.text("BERM 1.5:1 TO +0.900", P3(8750, 5100), SMS, "S-TEXT", "C", rot=90.0)
s.text("ENGINEERED COVER 2000, GRADED TO SHED AT GRADE", P3(12500, 4300), SMS,
       "S-TEXT", "C")

# the sentry post, drawn OFF POSITION, exactly as the owner's sheet 1 does
SPX, SPY = 5000.0, 700.0
s.rect(*P3(SPX, SPY), *P3(SPX + D.SP_EXT_X, SPY + D.SP_EXT_Y), "A-WALL")
s.rect(*P3(SPX + D.SP_INFILL, SPY + D.SP_INFILL),
       *P3(SPX + D.SP_EXT_X - D.SP_INFILL, SPY + D.SP_EXT_Y - D.SP_INFILL),
       "A-WALL")
for gx in (D.SP_GRID_A, D.SP_GRID_B):
    for gy in (D.SP_GRID_1, D.SP_GRID_2):
        s.rect(*P3(SPX + gx - D.SP_COL / 2, SPY + gy - D.SP_COL / 2),
               *P3(SPX + gx + D.SP_COL / 2, SPY + gy + D.SP_COL / 2), "A-WALL")
s.circle(P3(SPX - 500, SPY + 1300), D.SP_SPIRAL_R / SC, "A-WALL-IN")
s.text("SENTRY POST", P3(SPX + D.SP_EXT_X / 2, SPY + 3000), SMS, "S-TEXT", "C")
s.text("4000 x 5000", P3(SPX + D.SP_EXT_X / 2, SPY + 2600), SMS, "S-TEXT", "C")
s.dline(P3(SPX - 1900, SPY - 400), P3(SPX - 1900, SPY + D.SP_EXT_Y + 400),
        "S-CENTER", 2.0, 1.4)
s.text("SENTRY POST DRAWN OFF POSITION", P3(SPX + 300, SPY + 5700), SMS,
       "S-TEXT", "C")
s.text("TRUE SITE POSITION X 32000 - 36000,", P3(SPX + 300, SPY + 5300), SMS,
       "S-TEXT", "C")
s.text("Y 600 - 5600.   SEE SHEET 02", P3(SPX + 300, SPY + 4900), SMS,
       "S-TEXT", "C")
s.dim_h(P3(SPX, SPY), P3(SPX + D.SP_EXT_X, SPY), P3(0, SPY - 500)[1], SC,
        "A2-DIM-S")
s.dim_v(P3(SPX, SPY), P3(SPX, SPY + D.SP_EXT_Y), P3(SPX - 2400, 0)[0], SC,
        "A2-DIM-S")

s.dim_h(P3(A["x0"], 0), P3(A["x1"], 0), P3(0, -600)[1], SC, "A2-DIM-S")
s.dim_h(P3(H["x0"], 0), P3(H["x1"], 0), P3(0, -1300)[1], SC, "A2-DIM-S")
s.dim_v(P3(H["x1"], H["y0"]), P3(H["x1"], H["y1"]), P3(19100, 0)[0], SC,
        "A2-DIM-S")
s.north((274.5, 118.0))
s.view_title(PX0 - 4.0, V3_TTL, "3", "GROUND LEVEL PLAN   0.000",
             "1 : 100   SENTRY POST DRAWN OFF POSITION", RULE_TO)

# =====================================================================  TABLES
y = s.table_stack(RCOL, RTOP, 35.5, RCOL_W, [
    dict(rows=D.ROOM_SCHEDULE, title="ROOM SCHEDULE",
         header=["ROOM", "BAY", "X RANGE", "CLEAR", "USE"],
         align=["C", "C", "C", "C", "L"], pad=2.2),
    dict(rows=D.DOOR_SCHEDULE, title="DOOR SCHEDULE",
         header=["MARK", "DOOR", "LEAF", "LEVEL", "POSITION", "RATING"],
         align=["C", "L", "C", "C", "L", "L"], pad=2.0),
    dict(rows=D.OPENING_SCHEDULE, title="OPENING SCHEDULE",
         header=["MARK", "OPENING", "SIZE", "POSITION", "NOTES"],
         align=["C", "L", "C", "L", "L"], pad=2.2),
    dict(rows=D.WALL_SCHEDULE, title="WALL SCHEDULE",
         header=["WALL", "THK", "LENGTH", "EXTENT", "NOTES"],
         align=["L", "C", "C", "C", "L"], pad=2.2),
    dict(rows=[[a, b, c] for a, b, c in D.LEVELS], title="LEVEL SCHEDULE",
         header=["LEVEL", "VALUE", "DESCRIPTION"],
         align=["L", "C", "L"], pad=2.2),
], gap=5.0, rh_max=7.2)
assert y > 35.0, f"the schedule stack overflows the frame: bottom at {y:.1f}"


if __name__ == "__main__":
    out = os.path.join(ROOT, "Presentation Sheets", "DXF",
                       "ARCH001_Underground_Headhouse_and_Ground_Level_Plans_"
                       "Redrawn_to_Project_Data.dxf")
    s.save(out)
    print("written", out, "| right column bottom y =", round(y, 1))
