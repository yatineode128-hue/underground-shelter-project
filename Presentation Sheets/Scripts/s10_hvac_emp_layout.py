"""
s10_hvac_emp_layout.py  --  MEP010  HVAC AND EMP ZONE LAYOUT PLANS

Four views, in the layout and with the title block of the supplied Revit A2 set
(ARCH001..ARCH005), so that SHEET 10 reads as the next sheet of that series:

    1  HVAC SERVICES LAYOUT PLAN - UNDERGROUND LEVEL (-)6.100      1 : 100
    2  EMP ZONE LAYOUT PLAN - UNDERGROUND LEVEL (-)6.100           1 : 100
    3  EMP ZONE 2 ENCLOSURE - PLAN AND SECTION                     1 : 25
    4  PROTECTIVE VENTILATION SCHEMATIC - FILTER TRAIN AND CASCADE   NTS

The drainage structures are SHEET 11.  Every position, size, duty, tag and level
comes from the project's own discipline modules through mep_data.py; nothing is
invented.  SH-1, the fresh-air shaft, has no plan position in this project, so it
is shown as a direction arrow and never at a coordinate.

ANNOTATION RULE for this sheet.  Short tags go ON the view; the schedules on the
right carry the description, exactly as the ARCH series tags its doors 100..115
against a Door Schedule.  Only the few things a tag cannot say are leadered, and
those leaders all land in a reserved band ABOVE the view, so that nothing can
collide with a dimension chain or a view title.

COLOUR: dark only, and mostly black.  ACI 7 black, 8 dark grey, 1 dark red for
the protective devices and the foul line, 5 dark blue for the clean-air and
storm lines.  No light colour appears anywhere.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
for _p in ("Structural CAD", "HVAC", "EMP Protection", "Drainage"):
    sys.path.insert(0, os.path.join(ROOT, _p, "Scripts"))

from a2_lib import A2Sheet, vw                                # noqa: E402
import mep_data as D                                          # noqa: E402

SC = 100.0                        # V1 and V2
PX0 = 47.0                        # box west face -> x 47 .. 267
RCOL, RCOL_W = 282.0, 178.0       # schedule column, x 282 .. 460
RULE_TO = 272.0                   # right end of every view-title rule
SM, SMS = 1.9, 1.75               # annotation heights, both above the 1.70 floor

V1_Y0, V1_DIM, V1_TTL = 312.0, 306.0, 296.0     # box 312 .. 374
V2_Y0, V2_TTL = 214.0, 198.0                    # box 214 .. 276
V2_DIM = 42.5                                   # x base of the 6200 dimension
SC_Z2 = 30.0                                    # V3, the Zone 2 enclosure
Z2P_X, Z2P_Y = 54.0, 110.0                      # V3 plan,    model (0,0)
Z2S_X, Z2S_Y = 152.0, 110.0                      # V3 section, model (0,0)
V3_TTL = 96.0
V4_TTL = 40.0

P1 = vw(SC, PX0, V1_Y0)
P2 = vw(SC, PX0, V2_Y0)


ZP = vw(SC_Z2, Z2P_X, Z2P_Y)        # Zone 2 plan:    model (0,0) = SW corner
ZS = vw(SC_Z2, Z2S_X, Z2S_Y)        # Zone 2 section: model (0,0) = floor, west


# =====================================================================  SHEET
s = A2Sheet(
    sheet_no="SHEET 10",
    drawing_no="MEP010",
    title_lines=["HVAC & EMP ZONE", "LAYOUT PLANS -", "UNDERGROUND", "LEVEL"],
    project_lines=D.PROJECT_LINES,
    identity=D.IDENTITY,
    notes=D.NOTES_10,
    date=D.DATE,
    drawn=D.DRAWN,
    checked=D.CHECKED,
    scale_note="As indicated",
)

# ------------------------------------------------- services layers, all DARK
# Added to THIS document rather than to a2_lib.LAYERS, so that STR006...STR009
# are not disturbed.  Every colour is one of the four the package allows.
for _nm, _col, _lw, _desc in [
    ("M-EQUIP",        7, 35, "Services equipment"),
    ("M-DUCT-SUPPLY",  7, 25, "Filtered supply and transfer air"),
    ("M-DUCT-RAW",     1, 35, "RAW UNFILTERED air across the clean zone"),
    ("M-DUCT-EXTRACT", 5, 25, "Extract and exhaust air"),
    ("M-DUCT-GEN",     8, 35, "Generator air, outside the envelope"),
    ("M-VALVE",        1, 35, "Blast valves and gas-tight dampers"),
    ("M-EMP-Z1",       7, 35, "EMP Zone 1 boundary"),
    ("M-EMP-Z2",       1, 50, "EMP Zone 2 enclosure and envelope penetrations"),
    ("M-EMP-BOND",     5, 25, "Bonding, earthing and shield continuity"),
    ("M-PIPE-FOUL",    1, 35, "Foul drainage"),
    ("M-PIPE-STORM",   5, 25, "Storm and rising-main drainage"),
    ("M-SITE",         7, 25, "Site structures"),
    ("M-RESERVE",      8, 18, "Reserved footprints and land reserves"),
]:
    _ly = s.doc.layers.add(_nm)
    _ly.color, _ly.lineweight, _ly.description = _col, _lw, _desc


def solid_dot(p, r, layer, aci):
    """A filled dot on a layer this sheet adds itself.

    a2_lib.bar_dot() resolves its fill colour through a2_lib.LAYERS, which only
    knows the structural layer table, so the colour is passed explicitly here
    rather than by widening that shared table and disturbing STR006...STR009.
    """
    s.circle(p, r, layer)
    h = s.msp.add_hatch(color=aci, dxfattribs={"layer": layer})
    h.paths.add_polyline_path(
        [(p[0] + r * math.cos(a * math.pi / 8),
          p[1] + r * math.sin(a * math.pi / 8)) for a in range(16)],
        is_closed=True)


def shell(P, lay_out="S-CONCRETE", lay_in="S-CONCRETE-THIN"):
    """The 22000 x 6200 box: outer face, inner face, internal walls, shafts."""
    s.rect(*P(0, 0), *P(22000, 6200), lay_out)
    s.rect(*P(600, 600), *P(21400, 5600), lay_in)
    for x0, x1 in D.PARTITIONS:                         # 110 partitions
        s.line(P(x0, 600), P(x0, 5600), lay_in)
        s.line(P(x1, 600), P(x1, 5600), lay_in)
    for mark, x0, x1, t in D.IW:                        # W5 200, W6 / W7 400
        s.rect(*P(x0, 600), *P(x1, 5600), lay_in)
    for x0, x1 in ((14800, 15200), (18000, 18400)):     # 1200 blast doors
        s.line(P(x0, 600), P(x1, 600), "S-CENTER")
        s.line(P(x0, 1800), P(x1, 1800), "S-CENTER")
    for name, cx, cy, head in D.ESC:                    # escape shafts
        s.circle(P(cx, cy), D.ESC_CLEAR_D / 2.0 / SC, lay_in)
        s.circle(P(cx, cy), D.ESC_COLLAR_OD / 2.0 / SC, lay_in)
    for n, x0, x1, w, room, name in D.BAYS:             # room references
        s.text(room, P((x0 + x1) / 2.0, 800), SM, "S-TEXT", "C")


# =====================================================================  VIEW 1
# HVAC SERVICES LAYOUT PLAN, 1 : 100
shell(P1)
s.north((274.5, 358.0))

# -- the three decon airlock stages in bay 6
for nm, y0, y1 in D.DECON_STAGES:
    s.line(P1(12800, y0), P1(14800, y0), "S-CONCRETE-THIN")
    s.text(nm, P1(13800, (y0 + y1) / 2.0 - 90), SMS, "S-TEXT", "C")

# -- stair void over bay 7
s.dline(P1(D.VOID["x0"], D.VOID["y1"]), P1(D.VOID["x1"], D.VOID["y1"]),
        "S-HIDDEN")
s.text("STAIR VOID OVER", P1(16600, 3200), SMS, "S-TEXT", "C")

# -- clean sump SU-01 below floor, with the two submersibles
SR = D.SUMP_RECT
for a, b in ((0, 1), (2, 3)):
    pass
s.dline(P1(SR[0], SR[1]), P1(SR[2], SR[1]), "S-HIDDEN")
s.dline(P1(SR[0], SR[3]), P1(SR[2], SR[3]), "S-HIDDEN")
s.dline(P1(SR[0], SR[1]), P1(SR[0], SR[3]), "S-HIDDEN")
s.dline(P1(SR[2], SR[1]), P1(SR[2], SR[3]), "S-HIDDEN")
for px, py in D.SUMP_PUMPS:
    s.circle(P1(px, py), 210 / SC, "M-EQUIP")
s.text("SU-01", P1(11818, 2120), SMS, "S-TEXT", "C")

# -- the two NBC filter trains
for tag, rect in (("AHU-1", D.FILTER_T1), ("AHU-2", D.FILTER_T2)):
    s.rect(*P1(rect[0], rect[1]), *P1(rect[2], rect[3]), "M-EQUIP")
    s.text(tag, P1((rect[0] + rect[2]) / 2.0, (rect[1] + rect[3]) / 2.0 - 90),
           SM, "S-TEXT", "C")

# -- blast valves, drawn as a recessed valve body in the wall
for tag, bx, by in D.BLAST_VALVE_PTS:
    r = (D.BV_BORE[tag] + 240) / 2.0
    s.circle(P1(bx, by), r / SC, "M-VALVE")
    s.line(P1(bx - r, by - r), P1(bx + r, by + r), "M-VALVE")
    s.line(P1(bx - r, by + r), P1(bx + r, by - r), "M-VALVE")

# -- FA-2 / FA-3  RAW UNFILTERED AIR ACROSS THE CLEAN ZONE
s.pline([P1(598, 2200), P1(1100, 2200), P1(1100, 3000), P1(10600, 3000),
         P1(10600, 4725), P1(11098, 4725)], "M-DUCT-RAW")
s.pline([P1(598, 4000), P1(10200, 4000), P1(10200, 3250), P1(11098, 3250)],
        "M-DUCT-RAW")
s.text("FA-2 / FA-3  RAW UNFILTERED AIR, 11.2 m", P1(6000, 3220), SMS,
       "S-TEXT", "C")

# -- SA-1 .. SA-4 filtered supply, high level, west from the plenum
s.pline([P1(11098, 5100), P1(1500, 5100)], "M-DUCT-SUPPLY")
s.pline([P1(12100, 2700), P1(12100, 2550)], "M-DUCT-SUPPLY")        # SA-5
for tag, tx in [("SD-01", 2050), ("SD-02", 4510), ("SD-03", 6400),
                ("SD-03", 8100), ("SD-04", 9600), ("SD-04", 10500)]:
    s.rect(*P1(tx - 160, 4940), *P1(tx + 160, 5260), "M-DUCT-SUPPLY")
s.text("SA-1 .. SA-4  FILTERED SUPPLY, SD-01 .. SD-05 TERMINALS",
       P1(6000, 5320), SMS, "S-TEXT", "C")

# -- EA-1 extract low level, EA-2 exhaust to BV-3, transfer grilles
s.pline([P1(4510, 1200), P1(13000, 1200), P1(13000, 1350)], "M-DUCT-EXTRACT")
s.rect(*P1(4350, 1040), *P1(4670, 1360), "M-DUCT-EXTRACT")          # EG-01
s.pline([P1(13800, 4900), P1(14998, 4900)], "M-DUCT-EXTRACT")       # EA-2
for ty in (3600, 2100):                                             # TG-02/03
    s.rect(*P1(13500, ty - 90), *P1(14100, ty + 90), "M-DUCT-SUPPLY")
s.rect(*P1(12600, 3010), *P1(12800, 3190), "M-DUCT-SUPPLY")         # TG-01
s.text("EA-1 EXTRACT", P1(7000, 1380), SMS, "S-TEXT", "C")

# -- generator air:  SH-2 shaft outside the east wall, GA-1 / GA-2
GS = D.GEN_SHAFT
s.rect(*P1(GS[0], GS[1]), *P1(GS[2], GS[3]), "M-DUCT-GEN")
s.pline([P1(21398, 1300), P1(22350, 1300), P1(22350, 1750)], "M-DUCT-GEN")
s.pline([P1(21398, 4700), P1(22850, 4700), P1(22850, 2350)], "M-DUCT-GEN")
s.rect(*P1(19000, 2700), *P1(20600, 4300), "M-EQUIP")               # GEN-1
s.text("GEN-1", P1(19800, 3410), SM, "S-TEXT", "C")
s.rect(*P1(20198, 4400), *P1(21398, 5600), "M-EQUIP")               # TK-01
s.text("TK-01", P1(20798, 4910), SMS, "S-TEXT", "C")

# -- service entry plate in the north wall
SP_ = D.SERVICE_PLATE
s.rect(*P1(SP_[0], SP_[1]), *P1(SP_[2], SP_[3]), "M-EQUIP")

# -- blast-valve tags, placed where the plan is clear
s.text("BV-1", (PX0 - 1.2, P1(0, 2200)[1]), SM, "S-TEXT", "MR")
s.text("BV-2", (PX0 - 1.2, P1(0, 4000)[1]), SM, "S-TEXT", "MR")
s.text("BV-3", P1(16100, 4810), SM, "S-TEXT", "C")
s.text("BV-4", P1(20700, 1210), SM, "S-TEXT", "C")
s.text("BV-5", P1(19300, 4910), SM, "S-TEXT", "C")
s.text("CO2-1 / O2-1 / DH-1  BAY 5", P1(9700, 2460), SMS, "S-TEXT", "R")

# -- FA-1 arrives from a shaft the project does not position: direction only
s.line((PX0 - 5.4, P1(0, 3100)[1]), (PX0 - 0.4, P1(0, 3100)[1]), "M-DUCT-RAW")
s.pline([(PX0 - 2.0, P1(0, 3100)[1] + 0.9), (PX0 - 0.4, P1(0, 3100)[1]),
         (PX0 - 2.0, P1(0, 3100)[1] - 0.9)], "M-DUCT-RAW")

# -- the reserved leader band above the box
AB = V1_Y0 + 6200 / SC
s.note_leader(P1(11798, 6200), (PX0 + 50.0, AB + 12.0),
              "SEP  SERVICE ENTRY PLATE - PD-05 DN50 SUMP RISING MAIN", SM, "R")
s.note_leader(P1(11823, 5550), (PX0 + 118.0, AB + 7.2),
              "AHU-1 / AHU-2  NBC FILTER TRAINS 300 m3/h - EITHER TRAIN "
              "CARRIES THE WHOLE DUTY", SM, "R")
s.note_leader(P1(22898, 2350), (PX0 + 150.0, AB + 2.4),
              "SH-2 GENERATOR AIR SHAFT 600 x 600, EAST;   FA-1 ENTERS FROM "
              "THE SH-1 FRESH-AIR SHAFT, WEST OF THE BOX", SM, "L")

s.dim_chain_h([P1(v, 0)[0] for v in D.BAY_CHAIN], V1_Y0, V1_DIM, SC, "A2-DIM-S")
s.view_title(PX0 - 4.0, V1_TTL, "1",
             "HVAC SERVICES LAYOUT PLAN - UNDERGROUND LEVEL (-)6.100",
             "1 : 100   FIVE BLAST VALVES ARE THE ONLY AIR PATHS THROUGH THE "
             "PROTECTIVE BOUNDARY", RULE_TO)

# =====================================================================  VIEW 2
# EMP ZONE LAYOUT PLAN, 1 : 100
shell(P2, "M-EMP-Z1", "S-CONCRETE-THIN")
s.north((274.5, 258.0))

# -- EMP Zone 2 welded steel enclosure in bay 3
Z = D.Z2
s.rect(*P2(Z["x0"], Z["y0"]), *P2(Z["x1"], Z["y1"]), "M-EMP-Z2")
s.rect(*P2(Z["x0"] + 50, Z["y0"] + 50), *P2(Z["x1"] - 50, Z["y1"] - 50),
       "M-EMP-Z2")
s.conc_hatch(
    [P2(Z["x0"], Z["y0"]), P2(Z["x1"], Z["y0"]),
     P2(Z["x1"], Z["y1"]), P2(Z["x0"], Z["y1"])],
    holes=[[P2(Z["x0"] + 50, Z["y0"] + 50), P2(Z["x1"] - 50, Z["y0"] + 50),
            P2(Z["x1"] - 50, Z["y1"] - 50), P2(Z["x0"] + 50, Z["y1"] - 50)]],
    scale=0.5)
s.text("EMP ZONE 2", P2((Z["x0"] + Z["x1"]) / 2.0, 4390), SM, "S-TEXT", "C")

# -- the points of entry into Zone 2
s.line(P2(Z["x0"] + 700, Z["y0"]), P2(Z["x0"] + 1600, Z["y0"]), "M-EMP-BOND")
s.arc(P2(Z["x0"] + 700, Z["y0"]), 900 / SC, 0, 72, "M-EMP-BOND")
s.rect(*P2(Z["x1"] - 700, Z["y1"] - 50), *P2(Z["x1"] - 200, Z["y1"]),
       "M-EMP-BOND")
for dx in (120, 420):
    s.line(P2(Z["x0"] + dx, Z["y0"]), P2(Z["x0"] + dx, Z["y0"] - 500),
           "M-EMP-BOND")
s.text("PoE-1 .. PoE-5", P2((Z["x0"] + Z["x1"]) / 2.0, 3000), SMS, "S-TEXT",
       "C")

# -- every penetration of the Zone 1 envelope
PEN_PLAN = [("BV-1", 598, 2200), ("BV-2", 598, 4000), ("BV-3", 14998, 4900),
            ("BV-4", 21398, 1300), ("BV-5", 21398, 4700),
            ("SEP", 11798, 5900), ("ESC1", 2050, 2050), ("ESC2", 19900, 2050)]
for tag, px, py in PEN_PLAN:
    s.circle(P2(px, py), 1.15, "M-EMP-Z2")
    solid_dot(P2(px, py), 0.5, "M-EMP-Z2", 1)
s.rect(*P2(D.VOID["x0"], D.VOID["y0"]), *P2(D.VOID["x1"], D.VOID["y1"]),
       "M-EMP-Z2")
s.line(P2(D.VOID["x0"], D.VOID["y0"]), P2(D.VOID["x1"], D.VOID["y1"]),
       "S-CENTER")
s.line(P2(D.VOID["x0"], D.VOID["y1"]), P2(D.VOID["x1"], D.VOID["y0"]),
       "S-CENTER")

# -- welded EMP strap at every construction joint, about 6 m centres
for jx in (6000, 12000, 18000):
    s.dline(P2(jx, 0), P2(jx, 6200), "M-EMP-BOND", 1.2, 1.0)

# -- penetration tags
s.text("BV-1", (PX0 - 1.2, P2(0, 2200)[1]), SM, "S-TEXT", "MR")
s.text("BV-2", (PX0 - 1.2, P2(0, 4000)[1]), SM, "S-TEXT", "MR")
s.text("ESC1", P2(2050, 1150), SMS, "S-TEXT", "C")
s.text("ESC2", P2(19900, 1150), SMS, "S-TEXT", "C")
s.text("BV-3", P2(16100, 4810), SM, "S-TEXT", "C")
s.text("BV-4", P2(20900, 700), SM, "S-TEXT", "C")
s.text("BV-5", P2(20600, 5050), SM, "S-TEXT", "C")
s.text("VOID", P2(16600, 2100), SMS, "S-TEXT", "C")

AB2 = V2_Y0 + 6200 / SC
s.note_leader(P2(6000, 6200), (PX0 + 14.0, AB2 + 8.0),
              "EMP ZONE 1 - THE BURIED BOX, ALL EIGHT BAYS.  CAGE AT 150 IN "
              "BOTH CURTAINS;  WELDED Cu / GALVANISED EMP STRAP AT EVERY "
              "CONSTRUCTION JOINT", SM, "R")
s.note_leader(P2((Z["x0"] + Z["x1"]) / 2.0, Z["y1"]), (PX0 + 56.0, AB2 + 3.2),
              "EMP ZONE 2 - WELDED STEEL ENCLOSURE 2400 x 1600 x 2200, "
              "80 dB STANDING ALONE", SM, "R")
s.note_leader(P2(11798, 5900), (PX0 + 128.0, V2_Y0 - 6.0),
              "SEP MCT FRAME AND EVERY CAST-IN SLEEVE WELDED TO THE "
              "REINFORCEMENT CAGE", SM, "L")

s.dim_v(P2(0, 0), P2(0, 6200), V2_DIM, SC, "A2-DIM-S")
s.view_title(PX0 - 4.0, V2_TTL, "2",
             "EMP ZONE LAYOUT PLAN - UNDERGROUND LEVEL (-)6.100",
             "1 : 100   EMP ZONE IS NOT THE CLEANLINESS ZONE", RULE_TO)

# =====================================================================  VIEW 3
# EMP ZONE 2 ENCLOSURE - PLAN AND SECTION, 1 : 30
# The arrangement of the five points of entry follows the project's own EMP
# package (EM-301): the shielded door on the west face, the honeycomb vent on
# the east face, and a single-point bond at the base.
Z2W = Z["x1"] - Z["x0"]            # 2400 external
Z2D = Z["y1"] - Z["y0"]            # 1600 external
Z2H = Z["h_ext"]                   # 2200 external
PN = Z["panel"]                    # 50 welded shielded panel

# -- plan
s.rect(*ZP(0, 0), *ZP(Z2W, Z2D), "M-EMP-Z2")
s.rect(*ZP(PN, PN), *ZP(Z2W - PN, Z2D - PN), "M-EMP-Z2")
s.conc_hatch([ZP(0, 0), ZP(Z2W, 0), ZP(Z2W, Z2D), ZP(0, Z2D)],
             holes=[[ZP(PN, PN), ZP(Z2W - PN, PN), ZP(Z2W - PN, Z2D - PN),
                     ZP(PN, Z2D - PN)]], scale=0.55)
s.text("INTERNAL 2300 x 1500 x 2100", ZP(Z2W / 2.0, Z2D / 2.0 + 60), SMS,
       "S-TEXT", "C")
s.text("PANEL 50, WELDED THROUGHOUT", ZP(Z2W / 2.0, Z2D / 2.0 - 320), SMS,
       "S-TEXT", "C")
s.rect(*ZP(0, 250), *ZP(PN, 1150), "M-EMP-BOND")                 # PoE-1 door
s.text("PoE-1", ZP(330, 700), SMS, "S-TEXT", "C")
s.rect(*ZP(Z2W - PN, 500), *ZP(Z2W, 1100), "M-EMP-BOND")         # PoE-2 vent
s.text("PoE-2", ZP(Z2W - 340, 800), SMS, "S-TEXT", "C")
for px, lab in ((900, "PoE-3"), (1500, "PoE-4")):
    s.rect(*ZP(px - 110, 0), *ZP(px + 110, PN), "M-EMP-BOND")
    s.text(lab, ZP(px, 280), SMS, "S-TEXT", "C")
# the bay-3 faces the 300 inspection gap is measured to:  the W8 partition
# inner face at project X 5520 and the north wall inner face at project Y 5600
s.line(ZP(-300, -400), ZP(-300, 2000), "S-CONCRETE")
s.line(ZP(-420, 1900), ZP(2700, 1900), "S-CONCRETE")
s.hatch_pat([ZP(-420, 1900), ZP(2700, 1900), ZP(2700, 2060), ZP(-420, 2060)],
            "ANSI31", 0.7, 0.0, "S-HATCH")
s.hatch_pat([ZP(-460, -400), ZP(-300, -400), ZP(-300, 2060), ZP(-460, 2060)],
            "ANSI31", 0.7, 0.0, "S-HATCH")
s.text("BAY 3 NORTH WALL", ZP(1400, 1960), SMS, "S-TEXT", "C")
s.text("300 GAP", ZP(1150, 1750), SMS, "S-TEXT", "C")
s.text("300", ZP(-150, 950), SMS, "S-TEXT", "C", rot=90.0)
s.text("EXTERNAL 2400 x 1600 x 2200", ZP(Z2W / 2.0, Z2D / 2.0 + 480), SMS,
       "S-TEXT", "C")
s.text("PLAN", (Z2P_X + Z2W / 2.0 / SC_Z2, 106.5), SM, "S-TEXT", "C")

# -- section, cut along the 2400 length and looking north
s.rect(*ZS(0, 0), *ZS(Z2W, Z2H), "M-EMP-Z2")
s.rect(*ZS(PN, PN), *ZS(Z2W - PN, Z2H - PN), "M-EMP-Z2")
s.conc_hatch([ZS(0, 0), ZS(Z2W, 0), ZS(Z2W, Z2H), ZS(0, Z2H)],
             holes=[[ZS(PN, PN), ZS(Z2W - PN, PN), ZS(Z2W - PN, Z2H - PN),
                     ZS(PN, Z2H - PN)]], scale=0.55)
s.line(ZS(-400, 0), ZS(Z2W + 900, 0), "S-CONCRETE")
s.hatch_pat([ZS(-400, 0), ZS(Z2W + 900, 0), ZS(Z2W + 900, -220),
             ZS(-400, -220)], "ANSI31", 0.7, 0.0, "S-HATCH")
s.level(ZS(Z2W + 900, 0), "(-)6.100", "R", 2.6)
s.rect(*ZS(0, 200), *ZS(PN, 2000), "M-EMP-BOND")                 # PoE-1 door
s.text("PoE-1", ZS(360, 1100), SMS, "S-TEXT", "C")
s.rect(*ZS(Z2W - PN, 1300), *ZS(Z2W, 1900), "M-EMP-BOND")        # PoE-2 vent
for k in range(4):                                               # honeycomb
    s.line(ZS(Z2W - PN, 1300 + k * 200), ZS(Z2W, 1300 + k * 200), "M-EMP-BOND")
s.text("PoE-2  6 CELL", ZS(Z2W - 480, 1600), SMS, "S-TEXT", "C")
s.pline([ZS(1100, 0), ZS(1100, -420), ZS(1800, -420)], "M-EMP-BOND")
s.text("PoE-5  SINGLE-POINT BOND TO THE CAGE", ZS(1900, -420), SMS, "S-TEXT",
       "ML")
s.dim_v(ZS(Z2W, 0), ZS(Z2W, Z2H), ZS(Z2W + 700, 0)[0], SC_Z2, "A2-DIM-S")
s.text("SECTION", (Z2S_X + Z2W / 2.0 / SC_Z2, 106.5), SM, "S-TEXT", "C")

s.view_title(PX0 - 4.0, V3_TTL, "3",
             "EMP ZONE 2 ENCLOSURE - PLAN AND SECTION",
             "1 : 30   PANEL 50 WELDED THROUGHOUT", RULE_TO)

# =====================================================================  VIEW 4
# PROTECTIVE VENTILATION SCHEMATIC, NOT TO SCALE
SY, BOXW, BOXH, GAPX = 67.0, 23.2, 9.6, 3.6
X = PX0 + 11.0
TRAIN = [("WEATHER", "LOUVRE"), ("BLAST", "VALVE"), ("GAS-TIGHT", "DAMPER"),
         ("G4 / F7", "PRE-FILTER"), ("H14", "HEPA"), ("ASZM-TEDA", "CARBON"),
         ("FAN +", "HAND CRANK"), ("PLENUM", "+50 .. +100 Pa")]
for i, (a, b) in enumerate(TRAIN):
    x0 = X + i * (BOXW + GAPX)
    s.rect(x0, SY, x0 + BOXW, SY + BOXH, "M-EQUIP")
    s.text(a, (x0 + BOXW / 2.0, SY + BOXH - 3.2), SMS, "S-TEXT", "C")
    s.text(b, (x0 + BOXW / 2.0, SY + 2.4), SMS, "S-TEXT", "C")
    if i:
        s.line((x0 - GAPX, SY + BOXH / 2.0), (x0, SY + BOXH / 2.0),
               "M-DUCT-SUPPLY")
XEND = X + len(TRAIN) * (BOXW + GAPX) - GAPX
s.line((X - 8.0, SY + BOXH / 2.0), (X, SY + BOXH / 2.0), "M-DUCT-RAW")
s.text("SH-1", (X - 8.4, SY + BOXH / 2.0), SMS, "S-TEXT", "MR")

CASC = [("U-01 .. U-05 CLEAN ZONE", "+50 TO +100 Pa"),
        ("AIRLOCK STAGE 1", "+35 Pa"), ("AIRLOCK STAGE 2", "+20 Pa"),
        ("AIRLOCK STAGE 3", "+10 Pa"), ("BV-3 / OPRV-1", "TO BAY 7")]
CY = SY - 15.0
CW = (XEND - X - 4 * GAPX) / 5.0
for i, (lab, pr) in enumerate(CASC):
    x0 = X + i * (CW + GAPX)
    s.rect(x0, CY, x0 + CW, CY + BOXH, "M-EQUIP")
    s.text(lab, (x0 + CW / 2.0, CY + BOXH - 3.2), SMS, "S-TEXT", "C")
    s.text(pr, (x0 + CW / 2.0, CY + 2.4), SMS, "S-TEXT", "C")
    if i:
        s.line((x0 - GAPX, CY + BOXH / 2.0), (x0, CY + BOXH / 2.0),
               "M-DUCT-EXTRACT")
s.pline([(XEND, SY + BOXH / 2.0), (XEND + 3.2, SY + BOXH / 2.0),
         (XEND + 3.2, CY + BOXH + 2.4), (X + CW / 2.0, CY + BOXH + 2.4),
         (X + CW / 2.0, CY + BOXH)], "M-DUCT-SUPPLY")

s.view_title(PX0 - 4.0, V4_TTL, "4",
             "PROTECTIVE VENTILATION SCHEMATIC - FILTER TRAIN AND CASCADE",
             "SCHEMATIC ONLY   ONE TRAIN CARRIES THE WHOLE DUTY;  THE PLENUM "
             "OVERPRESSURE SETS THE DIRECTION OF EVERY LEAK", RULE_TO)

# =====================================================================  TABLES
y = s.table_stack(RCOL, 383.0, 35.5, RCOL_W, [
    dict(rows=D.HVAC_EQUIPMENT, title="HVAC EQUIPMENT SCHEDULE",
         header=["TAG", "ITEM", "DUTY", "POSITION", "NOTES"],
         align=["C", "L", "C", "L", "L"], pad=2.2),
    dict(rows=D.DAMPER_SCHEDULE,
         title="BLAST VALVE AND GAS-TIGHT DAMPER SCHEDULE",
         header=["TAG", "TYPE", "POSITION", "FUNCTION"],
         align=["C", "L", "L", "L"], pad=2.2),
    dict(rows=D.EMP_ZONE_SCHEDULE, title="EMP ZONE SCHEDULE",
         header=["ZONE", "WHAT IT IS", "SHIELDING MECHANISM", "PERFORMANCE"],
         align=["C", "L", "L", "L"], pad=2.2),
    dict(rows=D.penetration_rows(), title="ENVELOPE PENETRATION REGISTER",
         header=["TAG", "KIND", "BORE", "WALL", "HOST"],
         align=["C", "L", "C", "C", "L"], pad=2.2),
    dict(rows=D.POE_SCHEDULE, title="EMP ZONE 2 - POINT-OF-ENTRY SCHEDULE",
         header=["PoE", "KIND", "REF", "TREATMENT"],
         align=["C", "L", "C", "L"], pad=2.2),
], gap=6.0, rh_max=7.2)
assert y > 35.0, f"the schedule stack overflows the frame: bottom at {y:.1f}"


if __name__ == "__main__":
    out = os.path.join(ROOT, "Presentation Sheets", "DXF",
                       "MEP010_HVAC_and_EMP_Zone_Layout_Plans.dxf")
    s.save(out)
    print("written", out, "| right column bottom y =", round(y, 1))
