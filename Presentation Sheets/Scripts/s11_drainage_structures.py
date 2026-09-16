"""
s11_drainage_structures.py  --  MEP011  SEPTIC TANK, SOAK PIT AND SUMP PIT
                                PLANS, SECTIONAL ELEVATIONS AND SCHEDULES

Seven views, in the layout and with the title block of the supplied Revit A2 set
(ARCH001..ARCH005), so that SHEET 11 reads as the next sheet of that series.
Each of the three structures is drawn TWICE - once in plan and once as a
cross-sectional elevation - and the key plan puts all three in their real
positions on the site:

    1  SUMP PIT SU-01 - REINFORCEMENT PLAN                         1 : 35
    2  SUMP PIT SU-01 - SECTIONAL ELEVATION A-A                    1 : 35
    3  SEPTIC TANK ST-01 - PLAN                                    1 : 30
    4  SEPTIC TANK ST-01 - SECTIONAL ELEVATION                     1 : 30
    5  SOAK PIT SK-01 - PLAN                                       1 : 50
    6  SOAK PIT SK-01 - SECTIONAL ELEVATION                        1 : 50
    7  KEY PLAN - EXTERNAL WORKS LOCATION                          1 : 500

WHERE THE REINFORCEMENT COMES FROM.  SU-01 is a structural element of the box:
master F.1 schedules it and the bar-mark register carries its four marks, F10,
F11, F12 and F13.  They are drawn on views 1 and 2 and scheduled on the right,
read straight out of rebar_data.py, so a mark cannot appear here without a
schedule entry.  ST-01 and SK-01 are IS 2470 structures and the project holds no
bar for either of them; no bar is drawn in them and none is scheduled, and title
block note 8 calls them up to the structural engineer's detail.  Nothing is
invented.

ST-01 HAS NO RECORDED LEVEL, so view 4 is drawn relative to the local finished
grade at the external works reserve and carries no absolute level at all.

COLOUR: dark only, and mostly black.  ACI 7 black, 8 dark grey, 1 dark red for
main reinforcement and the foul line, 5 dark blue for rings, links and the storm
line.  No light colour appears anywhere.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
for _p in ("Structural CAD", "HVAC", "EMP Protection", "Drainage"):
    sys.path.insert(0, os.path.join(ROOT, _p, "Scripts"))

from a2_lib import A2Sheet, vw                                # noqa: E402
import mep_data as D                                          # noqa: E402

RULE_TO = 272.0
RULE_MID = 150.0                  # right end of every left-hand view title
SM, SMS = 1.9, 1.75

# ------------------------------------------------------------ row 1  SU-01
SC_SU = 35.0
SUP = vw(SC_SU, 74.0, 314.0)      # plan: model (0,0) = pit clear SW corner
SU_SX, SU_S0 = 172.0, 300.0       # section: x of the clear west face,
V12_TTL = 278.0                   #          y of level (-)8.300

# ------------------------------------------------------------ row 2  ST-01
SC_ST = 30.0
STP = vw(SC_ST, 64.0, 206.0)      # plan: model (0,0) = tank external SW corner
STS = vw(SC_ST, 166.0, 180.0)     # section: (0,0) = base underside, west face
V34_TTL = 158.0

# ------------------------------------------------------------ row 3  SK-01
SC_SK = 50.0
SKP = vw(SC_SK, 88.0, 100.0)      # plan: model (0,0) = pit centre
SK_CX, SK_G = 190.0, 144.0        # section: x of the centre, y of local grade
V56_TTL = 46.0

# --------------------------------------------------- right column, key plan
SC_SITE = 500.0
KP_X, KP_Y = 310.0, 340.0         # key plan: paper position of model (-2000,-2000)
V7_TTL = 328.0
RCOL, RCOL_W, RTOP = 282.0, 178.0, 315.0


def SU_S(mx, lvl):
    """V2: local x across the pit (mm) and an absolute level -> paper."""
    return (SU_SX + mx / SC_SU, SU_S0 + (lvl + 8.300) * 1000.0 / SC_SU)


def SK_S(mx, v):
    """V6: x from the pit centre, and v mm BELOW local finished grade."""
    return (SK_CX + mx / SC_SK, SK_G - v / SC_SK)


def P7(mx, my):
    """V7 key plan.  Model (-2000, -2000) sits at paper (KP_X, KP_Y)."""
    return (KP_X + (mx + 2000) / SC_SITE, KP_Y + (my + 2000) / SC_SITE)


# =====================================================================  SHEET
s = A2Sheet(
    sheet_no="SHEET 11",
    drawing_no="MEP011",
    title_lines=["SEPTIC TANK,", "SOAK PIT &", "SUMP PIT - PLANS,",
                 "SECTIONS &", "SCHEDULES"],
    project_lines=D.PROJECT_LINES,
    identity=D.IDENTITY,
    notes=D.NOTES_11,
    date=D.DATE,
    drawn=D.DRAWN,
    checked=D.CHECKED,
    scale_note="As indicated",
)

for _nm, _col, _lw, _desc in [
    ("M-EQUIP",       7, 35, "Services equipment"),
    ("M-PIPE-FOUL",   1, 35, "Foul drainage"),
    ("M-PIPE-STORM",  5, 25, "Storm and rising-main drainage"),
    ("M-SEEP",        8, 18, "Seepage and percolation"),
    ("M-SITE",        7, 25, "Site structures"),
    ("M-RESERVE",     8, 18, "Reserved footprints and land reserves"),
]:
    _ly = s.doc.layers.add(_nm)
    _ly.color, _ly.lineweight, _ly.description = _col, _lw, _desc

CL = 1500.0                       # sump clear
TW = float(D.SUMP_T_WALL)         # 300 pit walls
TB = float(D.SUMP_T_BASE)         # 400 pit base
CV = float(D.COVER_SUMP)          # 50 cover

# =====================================================================  VIEW 1
# SUMP PIT SU-01 - REINFORCEMENT PLAN, 1 : 35
# The mat opening IS the pit clear, 1500 x 1500; the 300 walls hang below it.
s.rect(*SUP(-500, -500), *SUP(2000, 2000), "S-CONCRETE-THIN")
s.conc_hatch([SUP(-500, -500), SUP(2000, -500), SUP(2000, 2000),
              SUP(-500, 2000)],
             holes=[[SUP(0, 0), SUP(CL, 0), SUP(CL, CL), SUP(0, CL)]],
             scale=0.45)
s.rect(*SUP(0, 0), *SUP(CL, CL), "S-CONCRETE")
for o in (-TW, CL + TW):                                  # pit walls below
    s.dline(SUP(o, -TW), SUP(o, CL + TW), "S-HIDDEN", 1.2, 0.9)
    s.dline(SUP(-TW, o), SUP(CL + TW, o), "S-HIDDEN", 1.2, 0.9)

for k in range(4):                                        # F10 trimmers
    o = 90.0 + k * 100.0
    s.bar([SUP(-500, -o), SUP(2000, -o)], "S-REBAR-SEC")
    s.bar([SUP(-500, CL + o), SUP(2000, CL + o)], "S-REBAR-SEC")
    s.bar([SUP(-o, -500), SUP(-o, 2000)], "S-REBAR-SEC")
    s.bar([SUP(CL + o, -500), SUP(CL + o, 2000)], "S-REBAR-SEC")

for o in (CV + 8.0, TW - CV - 8.0):                       # F12 rings
    s.bar([SUP(-o, -o), SUP(CL + o, -o), SUP(CL + o, CL + o),
           SUP(-o, CL + o)], "S-REBAR-DIST", close=True)

for o in (CV + 24.0, TW - CV - 24.0):                     # F11 verticals
    for t in range(int(CL / 150.0) + 1):
        v = t * 150.0
        for p in ((v, -o), (v, CL + o), (-o, v), (CL + o, v)):
            s.bar_dot(SUP(*p), 0.45, "S-REBAR-MAIN")

s.secmark(SUP(CL / 2.0, -420), "A", "U")
s.secmark(SUP(CL / 2.0, CL + 420), "A", "D")
s.line(SUP(CL / 2.0, -300), SUP(CL / 2.0, CL + 300), "S-SECTION")
s.tag(SUP(2450, 1350), "F10", SUP(CL + 390, 1350))
s.tag(SUP(2450, 460), "F12", SUP(CL + TW - CV - 8.0, 460))
s.tag(SUP(-1000, 1350), "F11", SUP(-CV - 24.0, 1350))
s.dim_chain_h([SUP(v, 0)[0] for v in (-TW, 0, CL, CL + TW)], SUP(0, -TW)[1],
              SUP(0, -700)[1], SC_SU, "A2-DIM-S")
s.dim_v(SUP(0, -TW), SUP(0, CL + TW), SUP(-700, 0)[0], SC_SU, "A2-DIM-S")
s.text("MAT 600 - OPENING 1500 x 1500", SUP(CL / 2.0, 2160), SMS, "S-TEXT",
       "C")
s.view_title(46.0, V12_TTL, "1", "SUMP PIT SU-01 - REINFORCEMENT PLAN",
             "1 : 35   BAY 5, X 11068 - 12568, Y 900 - 2400", RULE_MID)

# =====================================================================  VIEW 2
# SUMP PIT SU-01 - SECTIONAL ELEVATION A-A, 1 : 35
MT, MS = D.MAT_TOP, D.MAT_SOFFIT              # (-)6.100 / (-)6.700
BL, IN_, BS = D.BLINDING, D.SUMP_INVERT, D.SUMP_BASE
for x0, x1 in ((-500.0, -TW), (CL + TW, 2000.0)):         # mat beyond the pit
    s.conc_hatch([SU_S(x0, MS), SU_S(x1, MS), SU_S(x1, MT), SU_S(x0, MT)],
                 scale=0.45)
    s.rect(*SU_S(x0, MS), *SU_S(x1, MT), "S-CONCRETE")
    s.line(SU_S(x0, BL), SU_S(x1, BL), "S-EXISTING")
s.conc_hatch([SU_S(-TW, BS), SU_S(CL + TW, BS), SU_S(CL + TW, IN_),
              SU_S(-TW, IN_)], scale=0.45)                # base slab 400
s.rect(*SU_S(-TW, BS), *SU_S(CL + TW, IN_), "S-CONCRETE")
for x0, x1 in ((-TW, 0.0), (CL, CL + TW)):                # pit walls 300
    s.conc_hatch([SU_S(x0, IN_), SU_S(x1, IN_), SU_S(x1, MT), SU_S(x0, MT)],
                 scale=0.45)
    s.rect(*SU_S(x0, IN_), *SU_S(x1, MT), "S-CONCRETE")

s.pline([SU_S(-500, MS - 0.06), SU_S(-TW - 90, MS - 0.06),
         SU_S(-TW - 90, BS - 0.10), SU_S(CL + TW + 90, BS - 0.10),
         SU_S(CL + TW + 90, MS - 0.06), SU_S(2000, MS - 0.06)],
        "S-WATERPROOF")

s.line(SU_S(0, MT), SU_S(CL, MT), "M-EQUIP")              # the cover
s.text("SU-01 COVER", SU_S(CL / 2.0, MT + 0.13), SMS, "S-TEXT", "C")

for px in (430.0, 1070.0):                                # PU-01 / PU-02
    s.rect(*SU_S(px - 200, IN_), *SU_S(px + 200, IN_ + 0.40), "M-EQUIP")
s.pline([SU_S(430, IN_ + 0.40), SU_S(430, MT - 0.22),
         SU_S(-TW - 90, MT - 0.22)], "M-PIPE-STORM")
for lab, up in (("ALARM +1200", 1.200), ("START +900", 0.900),
                ("STOP +300", 0.300)):
    s.dline(SU_S(0, IN_ + up), SU_S(CL, IN_ + up), "M-PIPE-STORM", 1.2, 0.9)
    s.text(lab, SU_S(CL - 60, IN_ + up + 0.07), SMS, "S-TEXT", "MR")

for o in (CV + 24.0, TW - CV - 24.0):                     # F11 verticals
    for x in (-o, CL + o):
        s.bar([SU_S(x, IN_ + 0.05), SU_S(x, MT - 0.05)], "S-REBAR-MAIN")
for o in (CV + 8.0, TW - CV - 8.0):                       # F12 rings
    for x in (-o, CL + o):
        for k in range(int((MT - IN_) * 1000.0 / 150.0) + 1):
            s.bar_dot(SU_S(x, IN_ + 0.05 + k * 0.150), 0.4, "S-REBAR-DIST")
for lv in (BS + 0.062, IN_ - 0.062):                      # F13 base
    s.bar([SU_S(-TW + CV, lv), SU_S(CL + TW - CV, lv)], "S-REBAR-MAIN")
for k in range(4):                                        # F10 trimmers
    o = 90.0 + k * 100.0
    for lv in (MS + 0.075, MT - 0.075):
        s.bar_dot(SU_S(-o, lv), 0.45, "S-REBAR-SEC")
        s.bar_dot(SU_S(CL + o, lv), 0.45, "S-REBAR-SEC")

s.level(SU_S(2000, MT), "(-)6.100", "R", 2.6)
s.level(SU_S(2000, MS), "(-)6.700", "R", 2.6)
s.level(SU_S(CL + TW, IN_), "(-)7.600", "R", 2.6)
s.level(SU_S(CL + TW, BS), "(-)8.000", "R", 2.6)
s.tag(SU_S(2460, IN_ - 0.24), "F13", SU_S(CL + TW - CV, IN_ - 0.062))
s.tag(SU_S(-940, MS - 0.34), "F11", SU_S(-TW + CV + 24.0, MS - 0.34))
s.dim_v(SU_S(0, BS), SU_S(0, IN_), SU_S(-700, 0)[0], SC_SU, "A2-DIM-S")
s.dim_v(SU_S(0, IN_), SU_S(0, MT), SU_S(-700, 0)[0], SC_SU, "A2-DIM-S")
s.dim_chain_h([SU_S(v, 0)[0] for v in (-TW, 0, CL, CL + TW)],
              SU_S(0, BS)[1], SU_S(0, BS)[1] - 7.0, SC_SU, "A2-DIM-S")
s.text("CAST MONOLITHIC WITH THE MAT", SU_S(CL / 2.0, MT + 0.46), SMS,
       "S-TEXT", "C")
s.view_title(154.0, V12_TTL, "2", "SUMP PIT SU-01 - SECTIONAL ELEVATION A-A",
             "1 : 35   3.375 m3,  INVERT (-)7.600", RULE_TO)

# =====================================================================  VIEW 3
# SEPTIC TANK ST-01 - PLAN, 1 : 30
STL = int(D.SEPTIC["l"] * 1000)           # 1500 liquid length
STB = int(D.SEPTIC["b"] * 1000)           # 750 liquid width
TWA = float(D.ST_WALL)                    # 150 walls
EXL, EXB = STL + 2 * TWA, STB + 2 * TWA   # 1800 x 1050 external
BAF = TWA + STL * 2.0 / 3.0               # baffle at 2/3 L

s.rect(*STP(0, 0), *STP(EXL, EXB), "S-CONCRETE")
s.rect(*STP(TWA, TWA), *STP(EXL - TWA, EXB - TWA), "S-CONCRETE")
s.conc_hatch([STP(0, 0), STP(EXL, 0), STP(EXL, EXB), STP(0, EXB)],
             holes=[[STP(TWA, TWA), STP(EXL - TWA, TWA),
                     STP(EXL - TWA, EXB - TWA), STP(TWA, EXB - TWA)]],
             scale=0.45)
s.rect(*STP(BAF - 50, TWA), *STP(BAF + 50, EXB - TWA), "S-CONCRETE")
s.line(STP(-420, EXB / 2.0), STP(TWA, EXB / 2.0), "M-PIPE-FOUL")
s.line(STP(EXL - TWA, EXB / 2.0), STP(EXL + 420, EXB / 2.0), "M-PIPE-FOUL")
s.text("INLET", STP(-160, EXB / 2.0 + 230), SMS, "S-TEXT", "C")
s.text("PD-16 OUTLET", STP(EXL + 700, EXB / 2.0 + 230), SMS, "S-TEXT", "C")
s.circle(STP(EXL / 2.0, EXB - TWA / 2.0), 90 / SC_ST, "M-PIPE-FOUL")
s.text("50 VENT", STP(EXL / 2.0, EXB + 280), SMS, "S-TEXT", "C")
s.text("COMPT 1", STP(TWA + 500, EXB / 2.0), SMS, "S-TEXT", "C")
s.text("COMPT 2", STP(EXL - TWA - 250, EXB / 2.0), SMS, "S-TEXT", "C")
s.dim_chain_h([STP(v, 0)[0] for v in (0, TWA, BAF, EXL - TWA, EXL)],
              STP(0, 0)[1], STP(0, -600)[1], SC_ST, "A2-DIM-S")
s.dim_v(STP(EXL, 0), STP(EXL, EXB), STP(EXL + 480, 0)[0], SC_ST, "A2-DIM-S")
s.view_title(46.0, V34_TTL, "3", "SEPTIC TANK ST-01 - PLAN",
             "1 : 30   1500 x 750 LIQUID, 150 WALLS", RULE_MID)

# =====================================================================  VIEW 4
# SEPTIC TANK ST-01 - SECTIONAL ELEVATION, 1 : 30
# Local Y is measured UP from the underside of the base slab.  The project holds
# NO level for this tank, so none is printed; the cover slab is shown at the
# local finished grade, which is all the arrangement requires.
LIQ, FB = int(D.SEPTIC["liquid_depth"] * 1000), int(D.SEPTIC["freeboard"] * 1000)
BASE = COVER = int(TWA)
H_LIQ, H_TOP = BASE + LIQ, BASE + LIQ + FB
H_EXT = H_TOP + COVER

s.rect(*STS(0, 0), *STS(EXL, H_EXT), "S-CONCRETE")
s.rect(*STS(TWA, BASE), *STS(EXL - TWA, H_TOP), "S-CONCRETE")
s.conc_hatch([STS(0, 0), STS(EXL, 0), STS(EXL, H_EXT), STS(0, H_EXT)],
             holes=[[STS(TWA, BASE), STS(EXL - TWA, BASE),
                     STS(EXL - TWA, H_TOP), STS(TWA, H_TOP)]], scale=0.45)
s.line(STS(TWA, H_LIQ), STS(EXL - TWA, H_LIQ), "S-WATERPROOF")
s.text("LIQUID LEVEL", STS(EXL / 2.0, H_LIQ + 130), SMS, "S-TEXT", "C")
s.text("INLET TEE", STS(TWA + 330, H_LIQ - 470), SMS, "S-TEXT", "C")
s.text("OUTLET TEE", STS(EXL - TWA - 330, H_LIQ - 470), SMS, "S-TEXT", "C")
s.rect(*STS(BAF - 50, BASE), *STS(BAF + 50, H_TOP - 100), "S-CONCRETE")
s.text("BAFFLE AT 2/3 L", STS(BAF + 170, BASE + 380), SMS, "S-TEXT", "ML")
s.pline([STS(-420, H_LIQ + 60), STS(TWA + 120, H_LIQ + 60),
         STS(TWA + 120, H_LIQ - 300)], "M-PIPE-FOUL")
s.pline([STS(EXL - TWA - 120, H_LIQ - 300), STS(EXL - TWA - 120, H_LIQ + 60),
         STS(EXL + 420, H_LIQ + 60)], "M-PIPE-FOUL")
s.line(STS(-420, H_EXT), STS(-60, H_EXT), "S-EXISTING")
s.line(STS(EXL + 60, H_EXT), STS(EXL + 420, H_EXT), "S-EXISTING")
s.pline([STS(EXL / 2.0, H_EXT), STS(EXL / 2.0, H_EXT + 420)], "M-PIPE-FOUL")
s.line(STS(EXL / 2.0 - 90, H_EXT + 420), STS(EXL / 2.0 + 90, H_EXT + 420),
       "M-PIPE-FOUL")
s.note_leader(STS(EXL / 2.0, H_EXT + 380), (STS(EXL + 1500, H_EXT + 620)[0],
                                            STS(0, H_EXT + 620)[1]),
              "50 COWLED VENT, 2 m OR MORE ABOVE GRADE", SMS, "L")
s.text("LOCAL FINISHED GRADE", STS(EXL / 2.0, H_EXT + 230), SMS, "S-TEXT", "C")
s.dim_v(STS(EXL, BASE), STS(EXL, H_LIQ), STS(EXL + 1000, 0)[0], SC_ST,
        "A2-DIM-S")
s.dim_v(STS(EXL, H_LIQ), STS(EXL, H_TOP), STS(EXL + 1000, 0)[0], SC_ST,
        "A2-DIM-S")
s.text("1125 L CAPACITY, 10 USERS.  FREEBOARD 300, OVERALL DEPTH 1300",
       STS(EXL / 2.0, -320), SMS, "S-TEXT", "C")
s.view_title(154.0, V34_TTL, "4", "SEPTIC TANK ST-01 - SECTIONAL ELEVATION",
             "1 : 30   IS 2470 (Pt 1):1985", RULE_TO)

# =====================================================================  VIEW 5
# SOAK PIT SK-01 - PLAN, 1 : 50
DIA = int(D.SOAKPIT["dia"] * 1000)                 # 2200
EFF = int(D.SOAKPIT["effective_depth"] * 1000)     # 3500
SLB = float(D.SK_SLAB_BELOW_GRADE)                 # 600 to the u/s of the slab
CSL = float(D.SK_COVER_SLAB)                       # 300 cover slab
SND = float(D.SK_SAND)                             # 300 sand
BOT = SLB + SND + EFF                              # 4400 below local grade
HW = DIA / 2.0

s.circle(SKP(0, 0), (HW + 150) / SC_SK, "S-CONCRETE")
s.dline(SKP(-HW, 0), SKP(HW, 0), "S-HIDDEN", 1.2, 0.9)
s.circle(SKP(0, 0), HW / SC_SK, "M-SEEP")
s.cline(SKP(-HW - 600, 0), SKP(HW + 600, 0), "S-CENTER")
s.cline(SKP(0, -HW - 600), SKP(0, HW + 600), "S-CENTER")
s.line(SKP(-HW - 620, 0), SKP(-HW, 0), "M-PIPE-FOUL")
s.text("PD-16 DN100", SKP(-HW - 300, 340), SMS, "S-TEXT", "C")
s.text("2200 DIA BORE", SKP(0, -260), SMS, "S-TEXT", "C")
s.text("300 RC COVER SLAB OVER,", SKP(0, -700), SMS, "S-TEXT", "C")
s.text("150 BEARING ALL ROUND", SKP(0, -1040), SMS, "S-TEXT", "C")
s.dim_h(SKP(-HW, -HW), SKP(HW, -HW), SKP(0, -HW - 800)[1], SC_SK, "A2-DIM-S")
s.view_title(46.0, V56_TTL, "5", "SOAK PIT SK-01 - PLAN",
             "1 : 50   SK-02 IS IDENTICAL", RULE_MID)

# =====================================================================  VIEW 6
# SOAK PIT SK-01 - SECTIONAL ELEVATION, 1 : 50
s.hatch_pat([SK_S(-HW - 640, 0), SK_S(HW + 640, 0), SK_S(HW + 640, -180),
             SK_S(-HW - 640, -180)], "EARTH", 0.6, 0.0, "S-EXISTING")
s.line(SK_S(-HW - 640, 0), SK_S(HW + 640, 0), "S-EXISTING")

s.rect(*SK_S(-HW - 150, SLB - CSL), *SK_S(HW + 150, SLB), "S-CONCRETE")
s.conc_hatch([SK_S(-HW - 150, SLB), SK_S(HW + 150, SLB),
              SK_S(HW + 150, SLB - CSL), SK_S(-HW - 150, SLB - CSL)],
             scale=0.45)
s.rect(*SK_S(-HW, SLB), *SK_S(HW, SLB + SND), "S-EXISTING")
s.hatch_pat([SK_S(-HW, SLB), SK_S(HW, SLB), SK_S(HW, SLB + SND),
             SK_S(-HW, SLB + SND)], "ANSI31", 1.2, 0.0, "S-EXISTING")
s.rect(*SK_S(-HW, SLB + SND), *SK_S(HW, BOT), "M-SEEP")
s.rock_hatch([SK_S(-HW, SLB + SND), SK_S(HW, SLB + SND), SK_S(HW, BOT),
              SK_S(-HW, BOT)], 3.0)
for k in range(1, 5):                                   # percolation
    v = SLB + SND + EFF * k / 5.0
    for sgn in (-1, 1):
        s.line(SK_S(sgn * HW, v), SK_S(sgn * (HW + 420), v), "M-SEEP")
        s.pline([SK_S(sgn * (HW + 260), v + 110), SK_S(sgn * (HW + 420), v),
                 SK_S(sgn * (HW + 260), v - 110)], "M-SEEP")

GWT = 1300.0                                            # (-)2.000 below grade
s.dline(SK_S(-HW - 640, GWT), SK_S(HW + 640, GWT), "S-WATERPROOF", 2.0, 1.2)
s.pline([SK_S(-HW - 560, GWT), SK_S(-HW - 320, GWT),
         SK_S(-HW - 440, GWT + 190)], "S-WATERPROOF")
s.line(SK_S(-HW - 640, SLB + 80), SK_S(-HW, SLB + 80), "M-PIPE-FOUL")

# every note lands in the clear strip east of the pit and reads left to right,
# so no leader and no text can cross the fill
NX = SK_S(HW + 880, 0)[0]
for _pt, _ly, _txt in (
        ((HW + 150, SLB - CSL / 2.0), SLB - 620, "300 RC COVER SLAB"),
        ((HW, SLB + SND / 2.0), SLB + 120, "300 SAND AT THE TOP"),
        ((HW + 640, GWT), GWT + 380, "DESIGN GWT (-)2.000"),
        ((HW, SLB + SND + EFF * 0.50), SLB + SND + EFF * 0.50,
         "40-80 BRICKBAT FILL"),
        ((HW, BOT), BOT - 120, "SIDE AREA ONLY COUNTED")):
    s.note_leader(SK_S(*_pt), (NX, SK_S(0, _ly)[1]), _txt, SMS, "R")
s.text("PD-16", SK_S(-HW - 700, SLB + 300), SMS, "S-TEXT", "C")
s.dim_v(SK_S(-HW, BOT), SK_S(-HW, SLB + SND), SK_S(-HW - 960, 0)[0], SC_SK,
        "A2-DIM-S")
s.dim_v(SK_S(-HW, SLB), SK_S(-HW, 0), SK_S(-HW - 960, 0)[0], SC_SK,
        "A2-DIM-S")
s.view_title(154.0, V56_TTL, "6", "SOAK PIT SK-01 - SECTIONAL ELEVATION",
             "1 : 50   2200 DIA x 3500 EFFECTIVE, IS 2470 (Pt 2):1985",
             RULE_TO)

# =====================================================================  VIEW 7
# KEY PLAN - EXTERNAL WORKS LOCATION, 1 : 500, in the schedule column
R = D.RESERVE
s.rect(*P7(R["x0"], R["y0"]), *P7(R["x1"], R["y1"]), "M-RESERVE")
s.rect(*P7(0, 0), *P7(22000, 6200), "M-SITE")
s.dline(P7(D.EXCAV_FACE_X, -1400), P7(D.EXCAV_FACE_X, 7400), "S-HIDDEN")
SP = D.SENTRY
s.rect(*P7(SP["x0"], SP["y0"]), *P7(SP["x1"], SP["y1"]), "M-SITE")
s.text("SENTRY POST", P7((SP["x0"] + SP["x1"]) / 2.0, 3100), SMS, "S-TEXT",
       "C")
s.text("SHELTER 22000 x 6200", P7(11000, 3100), SMS, "S-TEXT", "C")
SR = D.SUMP_RECT
s.rect(*P7(SR[0], SR[1]), *P7(SR[2], SR[3]), "M-PIPE-STORM")
s.text("SU-01", P7(11818, -1300), SMS, "S-TEXT", "C")

K_OFF = {"ST-01": (0, 1600), "SK-01": (0, 1600), "SK-02": (0, -1800),
         "SK-03": (0, -1800), "SK-04": (0, -1800), "IC-01": (0, 1400),
         "IC-02": (0, -1800)}
for tag, kind, cx, cy, size, form in D.EXT_WORKS:
    if form == "CIRC":
        s.circle(P7(cx, cy), D.SOAK_DIA / 2.0 / SC_SITE, "M-PIPE-FOUL")
    elif form == "RESERVED":
        s.circle(P7(cx, cy), D.SOAK_DIA / 2.0 / SC_SITE, "M-RESERVE")
    elif tag.startswith("ST"):
        s.rect(*P7(cx - D.ST_L / 2.0, cy - D.ST_B / 2.0),
               *P7(cx + D.ST_L / 2.0, cy + D.ST_B / 2.0), "M-PIPE-FOUL")
    else:
        s.rect(*P7(cx - 600, cy - 450), *P7(cx + 600, cy + 450), "M-SITE")
    dx, dy = K_OFF[tag]
    s.text(tag, P7(cx + dx, cy + dy), SMS, "S-TEXT", "C")
s.line(P7(D.PD16["x0"], D.PD16["y"]), P7(D.PD16["x1"], D.PD16["y"]),
       "M-PIPE-FOUL")
s.dim_h(P7(22000, 16000), P7(36750, 16000), P7(0, 19400)[1], SC_SITE,
        "A2-DIM-S")
s.dim_h(P7(36750, 16000), P7(44000, 16000), P7(0, 19400)[1], SC_SITE,
        "A2-DIM-S")
s.dim_v(P7(53000, 6200), P7(53000, 16000), P7(54600, 0)[0], SC_SITE,
        "A2-DIM-S")
s.dim_v(P7(29800, 5600), P7(29800, 16000), P7(28400, 0)[0], SC_SITE,
        "A2-DIM-S")
s.view_title(RCOL - 4.0, V7_TTL, "7", "KEY PLAN - EXTERNAL WORKS LOCATION",
             "1 : 500   EAST OF THE SHELTER AND NORTH OF THE SENTRY POST",
             460.0)

# =====================================================================  TABLES
y = s.table_stack(RCOL, RTOP, 35.5, RCOL_W, [
    dict(rows=D.SUMP_PUMP_SCHEDULE, title="SUMP, PUMP AND TANK SCHEDULE",
         header=["TAG", "ITEM", "DUTY / SIZE", "LEVEL", "NOTES"],
         align=["C", "L", "L", "C", "L"], pad=2.2),
    dict(rows=D.ELEMENT_SCHEDULE_11, title="STRUCTURAL ELEMENT SCHEDULE",
         header=["ELEMENT", "THK", "SIZE", "COVER", "d", "REINFORCEMENT",
                 "NOTES"],
         align=["L", "C", "C", "C", "C", "L", "L"], pad=2.0),
    dict(rows=D.sump_marks(), title="BAR MARK SCHEDULE - SUMP PIT SU-01",
         header=["MARK", "BAR", "SPACING", "LOCATION", "CUT mm", "No."],
         align=["C", "C", "C", "L", "C", "C"], pad=2.2),
    dict(rows=D.EXT_STRUCTURE_SCHEDULE,
         title="EXTERNAL DRAINAGE STRUCTURE SCHEDULE",
         header=["TAG", "ITEM", "SIZE", "CENTRE (X, Y)", "NOTES"],
         align=["C", "L", "L", "C", "L"], pad=2.2),
    dict(rows=D.EXT_PIPE_SCHEDULE, title="EXTERNAL PIPE SCHEDULE",
         header=["REF", "SERVICE", "FROM  ->  TO", "DN", "GRADIENT", "LENGTH"],
         align=["C", "L", "L", "C", "C", "C"], pad=2.2),
], gap=5.0, rh_max=7.2)
assert y > 35.0, f"the schedule stack overflows the frame: bottom at {y:.1f}"


if __name__ == "__main__":
    out = os.path.join(ROOT, "Presentation Sheets", "DXF",
                       "MEP011_Septic_Tank_Soak_Pit_and_Sump_Pit_"
                       "Plans_Sections_and_Schedules.dxf")
    s.save(out)
    print("written", out, "| right column bottom y =", round(y, 1))
