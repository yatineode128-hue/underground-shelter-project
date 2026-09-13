"""
report_figures.py -- the drawn figures of the master project report.

Underground CBRN-hardened blast-resistant protective structure + sentry post, Pune.
Project Report package.

WHAT THESE ARE.  Report figures, drawn to scale FROM THE CONFIRMED GEOMETRY of
the master (Parts A.3 to A.4.9, A.7 and B) by the code below.  Nothing is
traced, nothing is measured off a picture, and every coordinate is a project
coordinate.

WHAT THESE ARE NOT.  They are NOT the project's issued drawings, and they are
NOT reconstructions of the seven S-series sheets that are absent from the
workspace.  They carry no title block, no revision box and no bar mark, they
are drawn at reading scale rather than at a plotting scale, and they must
never be used for setting out or for fabrication.  The issued package is the
80 DXF sheets listed in the drawing register.

Every figure is a reportlab Drawing, which is a Flowable, so it drops straight
into the report's story.  GEOM below holds the model coordinates; changing a
number there changes every figure that uses it.
"""

import math

from reportlab.graphics.shapes import (Circle, Drawing, Group, Line, PolyLine,
                                       Polygon, Rect, String)
from reportlab.lib import colors
from reportlab.lib.units import mm

# ------------------------------------------------------------------ palette
INK = colors.Color(0.09, 0.10, 0.13)
MID = colors.Color(0.36, 0.38, 0.43)
FAINT = colors.Color(0.62, 0.64, 0.68)
RULE = colors.Color(0.74, 0.76, 0.80)
ACCENT = colors.Color(0.14, 0.28, 0.46)
RED = colors.Color(0.74, 0.14, 0.14)
GOLD = colors.Color(0.78, 0.58, 0.12)
GREEN = colors.Color(0.13, 0.44, 0.30)
BLUE = colors.Color(0.18, 0.42, 0.66)
VIOLET = colors.Color(0.42, 0.26, 0.55)

CONC = colors.Color(0.845, 0.862, 0.884)      # concrete section
CONC2 = colors.Color(0.906, 0.918, 0.933)     # concrete beyond
SOIL = colors.Color(0.901, 0.866, 0.796)      # fill / soil
ROCK = colors.Color(0.792, 0.800, 0.792)      # basalt
RUB = colors.Color(0.855, 0.835, 0.792)       # rubble
TURF = colors.Color(0.808, 0.862, 0.780)      # topsoil / turf
WATER = colors.Color(0.792, 0.878, 0.933)
AIR = colors.Color(0.984, 0.988, 0.992)       # internal void
PLANT = colors.Color(0.906, 0.933, 0.949)
WARN = colors.Color(0.976, 0.925, 0.882)

F_REG = "RepSans"
F_BLD = "RepSans-Bold"
F_MON = "RepMono"

# ------------------------------------------------------------------ geometry
GEOM = dict(
    box=(0, 0, 22000, 6200),                  # external
    inner=(600, 600, 21400, 5600),            # internal clear
    bays=[("1", 600, 3500, "STORES / TANK / ESC 1"),
          ("2", 3610, 5410, "LAVATORY + MEDICAL"),
          ("3", 5520, 9020, "OPS ROOM  ·  EMP ZONE 2"),
          ("4", 9130, 10930, "BERTHING  9"),
          ("5", 11040, 12600, "CBRN PLANT"),
          ("6", 12800, 14800, "DECON AIRLOCK"),
          ("7", 15200, 18000, "STAIR SHAFT"),
          ("8", 18400, 21400, "GENERATOR  ·  ESC 2")],
    w8=[(3500, 3610), (5410, 5520), (9020, 9130), (10930, 11040)],
    w5=(12600, 12800), w6=(14800, 15200), w7=(18000, 18400),
    doorgap=(2500, 3400),
    esc1=(2050, 2050), esc2=(19900, 2050), esc_clear=700, esc_od=950,
    shaft=(15200, 600, 18000, 5600),
    void=(15200, 600, 18000, 3760),
    pad=(15200, 3760, 18000, 5600),
    fltA=(15300, 16500), well=(16500, 16700), fltB=(16700, 17900),
    L1=(3760, 4960), L2=(600, 1800), store=(4960, 5600),
    bd=(600, 1800),                            # blast door opening, in Y
    sump=(11068, 900, 12568, 2400),
    trainA=(11098, 3900, 12548, 5550),
    trainB=(11098, 2700, 12548, 3800),
    hh=(13600, 200, 18400, 6000), hhi=(14000, 600, 18000, 5600),
    hhdoor=(14450, 15350),
    asw=(9250, 5750, 16050, 7750), aswi=(9500, 6000, 15800, 7500),
    asw_top=(9500, 11000), asw_flt=(11000, 14300), asw_plat=(14300, 15800),
    channel=(8950, 9250),
    sentry=(32000, 600, 36000, 5600),
    reserve=(33000, 6500, 51000, 17500),
    exc=(-1000, -1000, 23000, 7200),
)

LEV = dict(grade=0, slab=-2000, soffit=-2900, floor=-6100, mat=-6700,
           form=-6800, gwt=-2000, hh_soffit=400, hh_top=900,
           asw_head=2450, asw_soffit=2200, sump_inv=-7600, sump_base=-8000,
           esc1_head=150, esc2_head=700, L1=-4733.3, L2=-3366.7,
           sp_gf=450, sp_ff=3650, sp_rf=6700, sp_par=7000)

COVER = [("TOPSOIL / TURF  300", 0, -300, TURF, "5.40"),
         ("GRANULAR FILTER  150", -300, -450, SOIL, "2.85"),
         ("RC BURSTER SLAB M30  200", -450, -650, CONC, "5.00"),
         ("CRUSHED BASALT RUBBLE  500", -650, -1150, RUB, "8.50"),
         ("COMPACTED ENGINEERED FILL  750", -1150, -1900, SOIL, "15.00"),
         ("PROTECTION SCREED  100", -1900, -2000, CONC2, "2.40")]


# ------------------------------------------------------------------- canvas
class V(object):
    """Model millimetres -> paper points."""

    def __init__(self, scale, ox, oy):
        self.s, self.ox, self.oy = float(scale), ox, oy

    def x(self, v):
        return self.ox + v / self.s * mm

    def y(self, v):
        return self.oy + v / self.s * mm

    def d(self, v):
        return v / self.s * mm


class Fig(Drawing):
    """A drawing with the small vocabulary the report's figures need."""

    def __init__(self, width, height):
        Drawing.__init__(self, width, height)

    # ---- primitives
    def line(self, x1, y1, x2, y2, c=INK, w=0.45, dash=None):
        ln = Line(x1, y1, x2, y2, strokeColor=c, strokeWidth=w)
        if dash:
            ln.strokeDashArray = dash
        self.add(ln)
        return ln

    def rect(self, x, y, w, h, fill=None, c=INK, sw=0.45, dash=None):
        r = Rect(x, y, w, h, fillColor=fill, strokeColor=c, strokeWidth=sw)
        if dash:
            r.strokeDashArray = dash
        self.add(r)
        return r

    def circ(self, cx, cy, r, fill=None, c=INK, sw=0.45, dash=None):
        o = Circle(cx, cy, r, fillColor=fill, strokeColor=c, strokeWidth=sw)
        if dash:
            o.strokeDashArray = dash
        self.add(o)
        return o

    def poly(self, pts, fill=None, c=INK, sw=0.45):
        self.add(Polygon(pts, fillColor=fill, strokeColor=c, strokeWidth=sw))

    def pline(self, pts, c=INK, w=0.45, dash=None):
        p = PolyLine(pts, strokeColor=c, strokeWidth=w)
        if dash:
            p.strokeDashArray = dash
        self.add(p)

    def txt(self, x, y, s, size=5.0, c=INK, anchor="start", bold=False,
            angle=0, font=None):
        st = String(x, y, s, fontName=font or (F_BLD if bold else F_REG),
                    fontSize=size, fillColor=c, textAnchor=anchor)
        if angle:
            g = Group(st)
            g.translate(x, y)
            g.rotate(angle)
            st.x = st.y = 0
            self.add(g)
        else:
            self.add(st)
        return st

    def para(self, x, y, s, size=4.1, c=MID, lead=None, width=None,
             bold=False):
        """Wrapped body text.  Returns the baseline of the last line."""
        font = F_BLD if bold else F_REG
        lead = lead or size * 1.34
        maxw = width if width is not None else self.width - x
        yy, line = y, ""
        for wd in s.split(" "):
            trial = (line + " " + wd) if line else wd
            if line and _strw(trial, font, size) > maxw:
                self.txt(x, yy, line, size, c, bold=bold)
                yy -= lead
                line = wd
            else:
                line = trial
        if line:
            self.txt(x, yy, line, size, c, bold=bold)
        return yy

    def note(self, x, y, head, body, hsize=4.4, bsize=4.1, hc=INK, bc=MID,
             gap=4.4, lead=None, width=None):
        """A bold lead-in line and a wrapped paragraph under it."""
        self.txt(x, y, head, hsize, hc, bold=True)
        return self.para(x, y - gap, body, bsize, bc, lead, width)

    def mono(self, x, y, s, size=4.6, c=INK, anchor="start"):
        return self.txt(x, y, s, size, c, anchor, font=F_MON)

    # ---- annotation
    def tick(self, x, y, ln=2.0, ang=45):
        a = math.radians(ang)
        dx, dy = ln * math.cos(a), ln * math.sin(a)
        self.line(x - dx, y - dy, x + dx, y + dy, MID, 0.4)

    def dimh(self, x1, x2, y, label, size=4.4, c=MID, off=0, ext=None):
        self.line(x1, y, x2, y, c, 0.35)
        self.tick(x1, y)
        self.tick(x2, y)
        if ext is not None:
            self.line(x1, y, x1, ext, FAINT, 0.25)
            self.line(x2, y, x2, ext, FAINT, 0.25)
        self.txt((x1 + x2) / 2.0, y + 1.6 + off, label, size, c, "middle")

    def dimv(self, y1, y2, x, label, size=4.4, c=MID, ext=None):
        self.line(x, y1, x, y2, c, 0.35)
        self.tick(x, y1, ang=-45)
        self.tick(x, y2, ang=-45)
        if ext is not None:
            self.line(x, y1, ext, y1, FAINT, 0.25)
            self.line(x, y2, ext, y2, FAINT, 0.25)
        self.txt(x - 1.8, (y1 + y2) / 2.0, label, size, c, "middle", angle=90)

    def level(self, x, y, label, size=4.4, c=ACCENT, side=1):
        s = 2.1
        self.poly([x, y, x - s * side, y + s, x + s * side, y + s],
                  fill=c, c=c, sw=0.2)
        self.txt(x + 3.4 * side, y + 1.4, label, size, c,
                 "start" if side > 0 else "end", bold=True)

    def leader(self, x1, y1, x2, y2, label, size=4.4, c=MID, anchor="start",
               dot=True):
        self.line(x1, y1, x2, y2, c, 0.3)
        if dot:
            self.circ(x1, y1, 0.7, fill=c, c=c, sw=0)
        dx = 1.6 if anchor == "start" else -1.6
        self.txt(x2 + dx, y2 - 1.4, label, size, c, anchor)

    def hatch(self, x, y, w, h, ang=45, sp=3.0, c=FAINT, lw=0.22):
        """Clipped 45-degree hatch inside a rectangle."""
        t = math.tan(math.radians(ang))
        start = -h / t if t else 0
        n = int((w - start) / sp) + 2
        for i in range(-2, n + 2):
            x0 = start + i * sp
            xa, ya = x0, 0.0
            xb, yb = x0 + h / t if t else x0, h
            # clip to [0,w]
            seg = _clip_seg(xa, ya, xb, yb, 0, 0, w, h)
            if seg:
                self.line(x + seg[0], y + seg[1], x + seg[2], y + seg[3],
                          c, lw)

    def rockface(self, x, y, w, h):
        self.rect(x, y, w, h, fill=ROCK, c=MID, sw=0.3)
        self.hatch(x, y, w, h, 45, 4.2, colors.Color(0.66, 0.68, 0.66), 0.2)

    def arrow(self, x1, y1, x2, y2, c=RED, w=0.7, head=2.6):
        self.line(x1, y1, x2, y2, c, w)
        a = math.atan2(y2 - y1, x2 - x1)
        for s in (+1, -1):
            b = a + s * math.radians(150)
            self.line(x2, y2, x2 + head * math.cos(b),
                      y2 + head * math.sin(b), c, w)

    def north(self, x, y, r=6.0):
        self.circ(x, y, r, fill=None, c=MID, sw=0.4)
        self.poly([x, y + r - 1.0, x - 2.0, y - r + 2.2, x, y - r + 3.6,
                   x + 2.0, y - r + 2.2], fill=INK, c=INK, sw=0.2)
        self.txt(x, y + r + 1.6, "N", 5.2, INK, "middle", bold=True)

    def scalebar(self, x, y, view, length_mm, label):
        w = view.d(length_mm)
        self.line(x, y, x + w, y, INK, 0.6)
        for f in (0.0, 0.5, 1.0):
            self.line(x + w * f, y - 1.4, x + w * f, y + 1.4, INK, 0.6)
        self.rect(x, y - 0.9, w / 2.0, 1.8, fill=INK, c=INK, sw=0)
        self.txt(x + w + 2.2, y - 1.5, label, 4.3, MID)

    def keybox(self, x, y, items, size=4.3, lead=5.4, sw=4.6):
        for i, (col, lab) in enumerate(items):
            yy = y - i * lead
            if col is None:
                self.txt(x, yy, lab, size, MID, bold=True)
            else:
                self.rect(x, yy - 0.4, sw, 3.2, fill=col, c=MID, sw=0.25)
                self.txt(x + sw + 2.2, yy, lab, size, INK)

    def keyrow(self, x, y, items, size=4.3, colw=42 * mm, sw=4.6):
        for i, (col, lab) in enumerate(items):
            xx = x + i * colw
            if col is not None:
                self.rect(xx, y - 0.4, sw, 3.2, fill=col, c=MID, sw=0.25)
                self.txt(xx + sw + 2.0, y, lab, size, INK)
            else:
                self.txt(xx, y, lab, size, MID, bold=True)

    def title(self, x, y, s, size=5.6):
        self.txt(x, y, s, size, INK, bold=True)


def _clip_seg(xa, ya, xb, yb, x0, y0, x1, y1):
    """Liang-Barsky clip of a segment to a rectangle."""
    dx, dy = xb - xa, yb - ya
    t0, t1 = 0.0, 1.0
    for p, q in ((-dx, xa - x0), (dx, x1 - xa), (-dy, ya - y0), (dy, y1 - ya)):
        if p == 0:
            if q < 0:
                return None
            continue
        r = q / float(p)
        if p < 0:
            if r > t1:
                return None
            if r > t0:
                t0 = r
        else:
            if r < t0:
                return None
            if r < t1:
                t1 = r
    return (xa + t0 * dx, ya + t0 * dy, xa + t1 * dx, ya + t1 * dy)


# ===========================================================================
#  CONFIGURATION FIGURES
# ===========================================================================

W = 174 * mm            # the report's text measure




# ===========================================================================
#  1  SITE AND GEOTECHNICS
# ===========================================================================

W = 174 * mm            # the report's text measure


def fig_site_plan():
    """Key plan -- everything on the plot, at true project X and Y."""
    d = Fig(W, 96 * mm)
    v = V(340, 11 * mm, 30 * mm)
    ex, ey, eX, eY = GEOM["exc"]
    rx, ry, rX, rY = GEOM["reserve"]
    sx, sy, sX, sY = GEOM["sentry"]

    d.rect(v.x(ex), v.y(ey), v.d(eX - ex), v.d(eY - ey), fill=SOIL,
           c=FAINT, sw=0.4, dash=[2, 2])
    d.rect(v.x(0), v.y(0), v.d(22000), v.d(6200), fill=CONC, c=INK, sw=0.7)
    d.rect(v.x(600), v.y(600), v.d(20800), v.d(5000), fill=AIR, c=MID, sw=0.3)
    d.txt(v.x(11000), v.y(3100) - 1.0, "UNDERGROUND BOX  22 000 x 6 200",
          4.8, INK, "middle", bold=True)

    hx, hy, hX, hY = GEOM["hh"]
    d.rect(v.x(hx), v.y(hy), v.d(hX - hx), v.d(hY - hy), fill=None,
           c=ACCENT, sw=0.5, dash=[2, 1.5])
    ax, ay, aX, aY = GEOM["asw"]
    d.rect(v.x(ax), v.y(ay), v.d(aX - ax), v.d(aY - ay), fill=CONC2,
           c=ACCENT, sw=0.5)
    d.txt(v.x(12650), v.y(6750) - 1.0, "C", 4.6, ACCENT, "middle", bold=True)
    d.txt(v.x(16000), v.y(7400), "B", 4.6, ACCENT, "middle", bold=True)
    d.line(v.x(16000), v.y(7200), v.x(16000), v.y(6000), ACCENT, 0.3)

    for (cx, cy), tag in ((GEOM["esc1"], "E1"), (GEOM["esc2"], "E2")):
        d.circ(v.x(cx), v.y(cy), v.d(GEOM["esc_od"]), fill=None, c=GREEN,
               sw=0.5)
        d.txt(v.x(cx), v.y(cy) - 1.0, tag, 3.8, GREEN, "middle", bold=True)

    d.rect(v.x(-2700), v.y(2800), v.d(600), v.d(600), fill=PLANT, c=BLUE,
           sw=0.5)
    d.txt(v.x(-2400), v.y(3800), "F", 4.4, BLUE, "middle", bold=True)
    d.rect(v.x(22598), v.y(2800), v.d(600), v.d(600), fill=PLANT, c=BLUE,
           sw=0.5, dash=[1.5, 1.5])
    d.txt(v.x(22898), v.y(3800), "G", 4.4, BLUE, "middle", bold=True)

    d.rect(v.x(sx), v.y(sy), v.d(sX - sx), v.d(sY - sy), fill=CONC,
           c=VIOLET, sw=0.7)
    d.txt(v.x((sx + sX) / 2), v.y(3100) - 1.0, "D", 5.0, VIOLET, "middle",
          bold=True)

    d.rect(v.x(rx), v.y(ry), v.d(rX - rx), v.d(rY - ry), fill=None,
           c=GREEN, sw=0.5, dash=[3, 2])
    d.txt(v.x(rx) + 2.0, v.y(rY) - 4.4,
          "E   EXTERNAL WORKS RESERVE  18.0 x 10.5", 4.5, GREEN, bold=True)
    for tag, cx, cy, r, dash in (("ST-01", 36750, 16000, 900, None),
                                 ("SK-01", 44000, 16000, 1100, None),
                                 ("SK-02", 35000, 8800, 1100, None),
                                 ("SK-03", 41400, 8500, 1100, [1.2, 1.2]),
                                 ("SK-04", 47800, 8500, 1100, [1.2, 1.2])):
        d.circ(v.x(cx), v.y(cy), v.d(r), fill=WATER, c=GREEN, sw=0.4,
               dash=dash)
        d.txt(v.x(cx), v.y(cy - 1900), tag, 3.8, GREEN, "middle")
    d.line(v.x(36750), v.y(16000), v.x(44000), v.y(16000), GREEN, 0.4)
    d.txt(v.x(40300), v.y(16000) + 1.2, "5.40 m  >= 5 m", 4.0, GREEN,
          "middle")

    d.line(v.x(23000), v.y(-3400), v.x(32000), v.y(-3400), RED, 0.5)
    d.tick(v.x(23000), v.y(-3400), ang=-45)
    d.tick(v.x(32000), v.y(-3400), ang=-45)
    d.txt(v.x(27500), v.y(-3400) + 1.4,
          "9.00 m to the EXCAVATION face", 4.2, RED, "middle", bold=True)
    d.line(v.x(22000), v.y(-6400), v.x(32000), v.y(-6400), MID, 0.4)
    d.tick(v.x(22000), v.y(-6400), ang=-45)
    d.tick(v.x(32000), v.y(-6400), ang=-45)
    d.txt(v.x(27000), v.y(-6400) + 1.4, "10.00 m to the BOX face", 4.2, MID,
          "middle")

    d.keybox(4 * mm, 90 * mm, [
        (None, "A  buried box, 8 bays, roof 2.0 m below grade"),
        (None, "B  entry headhouse, +0.900, no earth cover"),
        (None, "C  covered entry stairwell, head +2.450"),
        (None, "D  sentry post 4 000 x 5 000, parapet +7.000  [A]"),
        (None, "E  septic tank ST-01, soak pits SK-01 to SK-04"),
        (None, "F  SH-1 fresh-air intake, centred (-2 400, 3 100)"),
        (None, "G  SH-2 generator air, X 22 598 - 23 198;  Y not "
               "recorded  [N]")], 4.4, 4.6)
    d.north(W - 8 * mm, 88 * mm, 5.0)
    d.scalebar(4 * mm, 4 * mm, v, 10000, "10 m        1 : 340")
    d.txt(60 * mm, 4 * mm, "+X = EAST,  +Y = NORTH   [A].   "
          "Dashed: above, or not recorded.", 4.2, MID)
    return d


def fig_site_setting():
    """The plot in its setting, from the recorded description."""
    d = Fig(W, 74 * mm)
    d.rect(6 * mm, 6 * mm, W - 12 * mm, 62 * mm, fill=colors.white, c=RULE,
           sw=0.4)
    # campus schematic
    d.rect(14 * mm, 20 * mm, 30 * mm, 30 * mm, fill=CONC2, c=MID, sw=0.4)
    d.txt(29 * mm, 42 * mm, "CTW BLOCKS", 4.6, MID, "middle", bold=True)
    d.txt(29 * mm, 36 * mm, "G / H / MESS BUILDINGS", 4.0, MID, "middle")
    d.txt(29 * mm, 30 * mm, "TP-1 to TP-11", 4.0, RED, "middle", bold=True)
    d.txt(29 * mm, 25 * mm, "the investigated ground", 3.9, RED, "middle")

    d.rect(62 * mm, 22 * mm, 46 * mm, 26 * mm, fill=WARN, c=RED, sw=0.7)
    d.txt(85 * mm, 40 * mm, "THE PROJECT PLOT", 5.4, INK, "middle",
          bold=True)
    d.txt(85 * mm, 34 * mm, "undeveloped, east of the CTW blocks", 4.2, INK,
          "middle")
    d.txt(85 * mm, 28 * mm, "NO INVESTIGATION HAS EVER BEEN MADE HERE",
          4.4, RED, "middle", bold=True)

    d.rect(124 * mm, 10 * mm, 6 * mm, 54 * mm, fill=CONC2, c=MID, sw=0.35)
    d.txt(127 * mm, 36 * mm, "PERIMETER TRACK", 4.2, MID, "middle", angle=90)
    d.pline([136 * mm, 10 * mm, 139 * mm, 26 * mm, 135 * mm, 42 * mm,
             140 * mm, 58 * mm, 137 * mm, 64 * mm], BLUE, 0.8)
    d.txt(146 * mm, 36 * mm, "NULLAH LINE", 4.2, BLUE, "middle", angle=90)
    d.rect(62 * mm, 8 * mm, 46 * mm, 9 * mm, fill=CONC2, c=FAINT, sw=0.35)
    d.txt(85 * mm, 12 * mm, "CBRN LIVE TRAINING AREA", 4.2, MID, "middle")

    d.arrow(50 * mm, 35 * mm, 60 * mm, 35 * mm, MID, 0.5)
    d.txt(55 * mm, 37 * mm, "a few hundred", 3.8, MID, "middle")
    d.txt(55 * mm, 32 * mm, "metres  [A]", 3.8, MID, "middle")

    d.arrow(150 * mm, 22 * mm, 150 * mm, 14 * mm, MID, 0.5)
    d.txt(153 * mm, 24 * mm, "ground falls", 4.0, MID)
    d.txt(153 * mm, 19 * mm, "east / north-east", 4.0, MID)

    d.north(163 * mm, 58 * mm, 5.0)
    d.txt(6 * mm, 70 * mm, "SITE SETTING  -  SCHEMATIC, NOT TO SCALE",
          5.4, INK, bold=True)
    d.txt(6 * mm, 2.0 * mm, "Arrangement drawn from the recorded written "
          "description.  No dimensioned site plan, boundary, benchmark or "
          "coordinate exists  [N].", 4.2, MID)
    return d


def fig_trial_pit_logs():
    """The three investigated locations, and where this structure founds."""
    d = Fig(W, 126 * mm)
    v = V(100, 0, 104 * mm)                     # 1 : 100, depth downwards
    logs = [("G BUILDING", "TP-1 to TP-4", 16 * mm, 1500,
             [(0, 1000, TURF), (1000, 1200, SOIL), (1200, 1500, RUB),
              (1500, 8200, ROCK)]),
            ("H BUILDING", "TP-5 to TP-8", 44 * mm, 900,
             [(0, 180, TURF), (180, 700, SOIL), (700, 900, RUB),
              (900, 8200, ROCK)]),
            ("MESS BUILDING", "TP-9 to TP-11", 72 * mm, 1000,
             [(0, 200, SOIL), (200, 500, SOIL), (500, 1000, RUB),
              (1000, 8200, ROCK)])]

    d.rect(0, v.y(-8200), W, v.d(8200 - 1500), fill=WARN, c=None, sw=0)
    for name, pits, x0, rockhead, strata in logs:
        wp = 20 * mm
        for t, b, col in strata:
            d.rect(x0, v.y(-b), wp, v.d(b - t), fill=col, c=MID, sw=0.3)
        d.rect(x0, v.y(-1500), wp, v.d(1500), fill=None, c=INK, sw=0.6)
        d.line(x0, v.y(-rockhead), x0 + wp, v.y(-rockhead), RED, 0.9)
        d.txt(x0 + wp / 2, 110 * mm, name, 4.8, INK, "middle", bold=True)
        d.txt(x0 + wp / 2, 106.4 * mm, pits, 4.2, MID, "middle")
        d.txt(x0 + wp / 2, v.y(-rockhead) - 3.4,
              "rockhead %.1f m" % (rockhead / 1000.0), 4.0, RED, "middle",
              bold=True)
        d.txt(x0 + wp / 2, v.y(-8200) + 2.2, "NO DATA", 4.0, RED, "middle",
              bold=True)

    d.line(0, v.y(0), W, v.y(0), INK, 0.8)
    d.txt(2.0, v.y(0) + 1.8, "GROUND LEVEL", 4.2, INK, bold=True)
    d.line(0, v.y(-1500), W, v.y(-1500), RED, 0.7, [4, 2])
    d.txt(2.0, v.y(-1500) + 1.6,
          "DEEPEST STRATUM BOUNDARY ANYWHERE IN THE REPORT   (-)1.500",
          4.4, RED, bold=True)
    for lv, lab, col in ((-2000, "sentry footing F1 founds here   (-)2.000",
                          VIOLET),
                         (-6100, "shelter floor   (-)6.100", ACCENT),
                         (-6800, "FORMATION  -  the 600 mat bears here   "
                          "(-)6.800", ACCENT),
                         (-8000, "sump base   (-)8.000", BLUE)):
        d.line(96 * mm, v.y(lv), W, v.y(lv), col, 0.5,
               None if lv == -6800 else [3, 2])
        d.txt(W - 1.0, v.y(lv) + 1.4, lab, 4.2, col, "end",
              bold=(lv == -6800))
    d.txt(48 * mm, v.y(-4100), "5.3 m OF COMPLETELY UNLOGGED GROUND", 6.0,
          RED, "middle", bold=True)
    d.txt(48 * mm, v.y(-4700), "under the whole structure", 4.6, RED,
          "middle")
    d.txt(0, 120 * mm, "THE SUB-SOIL INVESTIGATION AGAINST THE STRUCTURE "
          "IT HAS TO SUPPORT   -   1 : 100", 5.4, INK, bold=True)
    d.keyrow(0, 9 * mm, [
        (TURF, "High plasticity CLAY, CH   FSI 60-65 %"),
        (SOIL, "MURRUM   GM / GP / SC"),
        (RUB, "BROKEN ROCK   980.7 kPa")], 4.3, 58 * mm)
    d.keyrow(0, 4 * mm, [
        (ROCK, "BASALT   1 961 - 2 059 kPa soaked"),
        (None, "RED LINE = rockhead, band 0.9 to 1.5 m"),
        (None, "The pits are on OTHER buildings")], 4.3, 58 * mm)
    return d


def fig_bearing_chart():
    """Bearing demand against the presumptive and the measured values."""
    d = Fig(W, 68 * mm)
    x0, y0, wbar = 40 * mm, 12 * mm, 100 * mm
    top = 3500.0
    d.line(x0, y0, x0 + wbar, y0, INK, 0.5)
    for q in (0, 1000, 2000, 3000):
        xx = x0 + wbar * q / top
        d.line(xx, y0, xx, y0 - 1.6, MID, 0.35)
        d.txt(xx, y0 - 5.6, str(q), 4.2, MID, "middle")
    d.txt(x0 + wbar / 2, y0 - 10.0, "kPa", 4.4, MID, "middle")

    rows = [("Mat, service", 58.4, MID),
            ("Mat, BLAST - the worst in the project", 404.9, RED),
            ("Sentry footing F1", 157.6, VIOLET)]
    for i, (lab, q, col) in enumerate(rows):
        yy = y0 + 30 * mm - i * 8 * mm
        d.rect(x0, yy, wbar * q / top, 5.0, fill=col, c=col, sw=0)
        d.txt(x0 - 2.0, yy + 1.2, lab, 4.4, INK, "end")
        d.txt(x0 + wbar * q / top + 2.0, yy + 1.2,
              "%.1f  =  %.1f %% of 1 961" % (q, q / 1961.0 * 100), 4.2, col)
    for val, lab, col, dash, hgt in (
            (1961, "MEASURED soaked basalt, lowest  1 961", INK, None,
             44 * mm),
            (2059, "measured soaked, highest  2 059", MID, [2, 2], 38 * mm),
            (3240, "IS 1904 presumptive  3 240  [A]", GOLD, [4, 2],
             44 * mm)):
        xx = x0 + wbar * val / top
        d.line(xx, y0, xx, y0 + hgt, col, 0.55, dash)
        d.txt(xx + 1.6, y0 + hgt + 1.2, lab, 4.2, col,
              "end" if val == 1961 else "start", bold=True)
    d.txt(0, 62 * mm, "BEARING  -  DEMAND AGAINST CAPACITY", 5.4, INK,
          bold=True)
    d.txt(0, 2.0 * mm, "The founding horizon is 4.8 m below the design water "
          "table, so the SOAKED value is the one that applies.  Worst "
          "utilisation 20.6 %; factor of 4.8 in hand.", 4.2, MID)
    return d


def fig_met_chart():
    """Monthly rainfall and temperature, as recorded."""
    d = Fig(W, 72 * mm)
    months = ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"]
    rain = [0.1, 3.0, 5.5, 3.9, 19.0, 137.8, 166.2, 120.8, 134.9, 139.8,
            22.7, 5.9]
    tmax = [29.8, 32.4, 35.5, 38.3, 37.8, 32.1, 28.5, 28.2, 29.7, 31.6,
            30.9, 29.6]
    tmin = [11.6, 13.7, 16.7, 20.2, 23.1, 23.1, 22.3, 21.6, 21.1, 19.7,
            15.2, 13.5]
    x0, y0 = 14 * mm, 14 * mm
    wcol = 11.5 * mm
    hmax = 34 * mm
    d.line(x0, y0, x0 + 12 * wcol, y0, INK, 0.5)
    for i, (mn, r) in enumerate(zip(months, rain)):
        xx = x0 + i * wcol
        h = hmax * r / 180.0
        col = BLUE if r > 100 else colors.Color(0.60, 0.76, 0.88)
        d.rect(xx + 1.5, y0, wcol - 3.0, h, fill=col, c=col, sw=0)
        d.txt(xx + wcol / 2, y0 - 5.0, mn, 4.4, INK, "middle", bold=True)
        d.txt(xx + wcol / 2, y0 + h + 1.2, "%.0f" % r, 3.8, BLUE, "middle")
    for q in (0, 50, 100, 150):
        yy = y0 + hmax * q / 180.0
        d.line(x0 - 1.6, yy, x0, yy, MID, 0.3)
        d.txt(x0 - 2.6, yy - 1.2, str(q), 4.0, MID, "end")
    d.txt(x0 - 2.6, y0 + hmax + 3.0, "mm", 4.2, BLUE, "end", bold=True)

    ty0, thi = y0 + 40 * mm, 16 * mm
    for series, col, lab in ((tmax, RED, "max"), (tmin, ACCENT, "min")):
        pts = []
        for i, t in enumerate(series):
            pts += [x0 + i * wcol + wcol / 2,
                    ty0 + thi * (t - 8) / 34.0]
        d.pline(pts, col, 0.8)
        d.txt(x0 + 11 * wcol + wcol / 2 + 2.0,
              ty0 + thi * (series[-1] - 8) / 34.0 - 1.2, lab, 4.2, col)
    d.txt(x0 - 2.6, ty0 + thi / 2, "degC", 4.2, RED, "end", bold=True)

    d.txt(0, 66 * mm, "RECORDED METEOROLOGY  -  MONTHLY MEANS", 5.4, INK,
          bold=True)
    d.txt(0, 2.0 * mm, "Rainfall total 759.6 mm against the soil report's "
          "500-600 mm  -  an unresolved conflict in the supplied documents.  "
          "October, at 139.8 mm, is the figure to go back and check:  the "
          "monsoon has withdrawn by then.", 4.2, MID)
    return d


# ===========================================================================
#  2  CONFIGURATION
# ===========================================================================

def fig_underground_plan():
    """The underground level at (-)6.100 -- bays, walls, openings, plant."""
    d = Fig(W, 84 * mm)
    v = V(150, 13 * mm, 25 * mm)
    d.rect(v.x(0), v.y(0), v.d(22000), v.d(6200), fill=CONC, c=INK, sw=0.7)
    d.rect(v.x(600), v.y(600), v.d(20800), v.d(5000), fill=AIR, c=MID,
           sw=0.35)

    for (a, b), col in ((GEOM["w5"], MID), (GEOM["w6"], RED),
                        (GEOM["w7"], RED)):
        d.rect(v.x(a), v.y(600), v.d(b - a), v.d(5000), fill=CONC, c=col,
               sw=0.55)
    for a, b in GEOM["w8"]:
        g0, g1 = GEOM["doorgap"]
        d.rect(v.x(a), v.y(600), v.d(b - a), v.d(g0 - 600), fill=CONC2,
               c=FAINT, sw=0.35)
        d.rect(v.x(a), v.y(g1), v.d(b - a), v.d(5600 - g1), fill=CONC2,
               c=FAINT, sw=0.35)

    for (a, b), tag in ((GEOM["w6"], "BD 1"), (GEOM["w7"], "BD 2")):
        y0, y1 = GEOM["bd"]
        d.rect(v.x(a), v.y(y0), v.d(b - a), v.d(y1 - y0), fill=RED, c=RED,
               sw=0.3)
        d.txt(v.x((a + b) / 2.0), v.y(y0) - 4.6, tag, 4.4, RED, "middle",
              bold=True)

    for (cx, cy), tag in ((GEOM["esc1"], "ESC 1"), (GEOM["esc2"], "ESC 2")):
        d.circ(v.x(cx), v.y(cy), v.d(GEOM["esc_od"]), fill=CONC2, c=GREEN,
               sw=0.45)
        d.circ(v.x(cx), v.y(cy), v.d(GEOM["esc_clear"]), fill=colors.white,
               c=GREEN, sw=0.55)
        d.txt(v.x(cx), v.y(cy) - 1.4, tag, 4.2, GREEN, "middle", bold=True)

    sx, sy, sX, sY = GEOM["shaft"]
    fa0, fa1 = GEOM["fltA"]
    fb0, fb1 = GEOM["fltB"]
    d.rect(v.x(sx), v.y(sy), v.d(sX - sx), v.d(sY - sy), fill=colors.white,
           c=MID, sw=0.35)
    for x0, x1 in ((fa0, fa1), (fb0, fb1)):
        d.rect(v.x(x0), v.y(1800), v.d(x1 - x0), v.d(1960), fill=CONC2,
               c=MID, sw=0.3)
        for i in range(1, 8):
            yy = 1800 + 1960 * i / 8.0
            d.line(v.x(x0), v.y(yy), v.x(x1), v.y(yy), FAINT, 0.25)
    d.rect(v.x(GEOM["well"][0]), v.y(1800), v.d(200), v.d(1960),
           fill=colors.white, c=FAINT, sw=0.25)
    d.rect(v.x(sx), v.y(GEOM["L1"][0]), v.d(sX - sx), v.d(1200), fill=CONC2,
           c=MID, sw=0.3)
    d.txt(v.x((sx + sX) / 2), v.y(4280), "L1", 4.2, MID, "middle")
    d.rect(v.x(sx), v.y(4960), v.d(sX - sx), v.d(640), fill=colors.white,
           c=FAINT, sw=0.25)
    d.txt(v.x((sx + sX) / 2), v.y(5200), "STORE", 3.8, FAINT, "middle")
    d.rect(v.x(sx), v.y(600), v.d(sX - sx), v.d(1200), fill=CONC2, c=MID,
           sw=0.3)
    d.txt(v.x((sx + sX) / 2), v.y(1120), "ARRIVAL", 3.8, MID, "middle")
    vx, vy, vX, vY = GEOM["void"]
    d.rect(v.x(vx), v.y(vy), v.d(vX - vx), v.d(vY - vy), fill=None, c=ACCENT,
           sw=0.45, dash=[2.5, 1.8])
    d.txt(v.x((vx + vX) / 2), v.y(2560), "VOID OVER  2 800 x 3 160", 4.0,
          ACCENT, "middle")

    sux, suy, suX, suY = GEOM["sump"]
    d.rect(v.x(sux), v.y(suy), v.d(suX - sux), v.d(suY - suy), fill=WATER,
           c=BLUE, sw=0.45)
    d.txt(v.x((sux + suX) / 2), v.y(1580), "SUMP", 3.9, BLUE, "middle")
    for (tx, ty, tX, tY), lab in ((GEOM["trainA"], "FILTER 1"),
                                  (GEOM["trainB"], "FILTER 2")):
        d.rect(v.x(tx), v.y(ty), v.d(tX - tx), v.d(tY - ty), fill=PLANT,
               c=BLUE, sw=0.4)
        d.txt(v.x((tx + tX) / 2), v.y((ty + tY) / 2) - 1.0, lab, 3.8, BLUE,
              "middle")

    for num, a, b, use in GEOM["bays"]:
        cx = (a + b) / 2.0
        d.circ(v.x(cx), v.y(6200) + 4.6, 3.4, fill=colors.white, c=INK,
               sw=0.45)
        d.txt(v.x(cx), v.y(6200) + 3.2, num, 5.0, INK, "middle", bold=True)
        d.txt(v.x(cx) + 1.4, v.y(760), use, 3.9, MID, "start", angle=90)
        d.dimh(v.x(a), v.x(b), v.y(0) - 5.2, str(b - a), 4.0)
    d.dimh(v.x(0), v.x(22000), v.y(0) - 12.0, "22 000 EXTERNAL", 4.6, INK)
    d.dimv(v.y(0), v.y(6200), v.x(0) - 5.0, "6 200", 4.2)
    d.dimv(v.y(600), v.y(5600), v.x(0) - 10.5, "5 000 CLEAR", 4.2)
    d.txt(v.x(0), v.y(6200) + 11.0, "UNDERGROUND LEVEL  (-)6.100", 5.4, INK,
          bold=True)
    d.north(W - 8 * mm, v.y(6200) + 4)
    d.scalebar(13 * mm, 3.0 * mm, v, 5000, "5 m        1 : 150")
    return d


def fig_long_section():
    """Longitudinal section on the box centreline."""
    d = Fig(W, 92 * mm)
    v = V(168, 15 * mm, 56 * mm)
    x0, x1 = -2000, 24200

    d.rect(v.x(x0), v.y(-8600), v.d(x1 - x0), v.d(8600), fill=SOIL, c=None,
           sw=0)
    d.rockface(v.x(x0), v.y(-8600), v.d(x1 - x0), v.d(8600 - 1500))
    d.line(v.x(x0), v.y(LEV["gwt"]), v.x(x1), v.y(LEV["gwt"]), BLUE, 0.5,
           [5, 2])
    d.txt(v.x(x0) + 1.2, v.y(LEV["gwt"]) + 1.4, "DESIGN GWT (-)2.000 [A]",
          4.0, BLUE, bold=True)

    for lab, t, b, col, load in COVER:
        d.rect(v.x(-500), v.y(b), v.d(23000), v.d(t - b), fill=col, c=MID,
               sw=0.25)
    d.txt(v.x(3000), v.y(-1000), "ENGINEERED COVER  2 000  =  40.65 kPa",
          4.6, INK, bold=True)

    d.rect(v.x(0), v.y(LEV["mat"]), v.d(22000), v.d(4700), fill=CONC, c=INK,
           sw=0.6)
    d.rect(v.x(600), v.y(LEV["floor"]), v.d(20800), v.d(3200), fill=AIR,
           c=MID, sw=0.3)
    d.rect(v.x(0), v.y(LEV["form"]), v.d(22000), v.d(100), fill=CONC2, c=MID,
           sw=0.25)
    for a, b in (GEOM["w5"], GEOM["w6"], GEOM["w7"]):
        d.rect(v.x(a), v.y(LEV["floor"]), v.d(b - a), v.d(3200), fill=CONC,
               c=MID, sw=0.4)
    for a, b in GEOM["w8"]:
        d.rect(v.x(a), v.y(LEV["floor"]), v.d(b - a), v.d(3200), fill=CONC2,
               c=FAINT, sw=0.3)

    # stair void and shaft
    d.rect(v.x(15200), v.y(LEV["slab"]) - v.d(900), v.d(2800), v.d(900),
           fill=colors.white, c=ACCENT, sw=0.5)
    d.txt(v.x(16600), v.y(-2500), "VOID", 4.0, ACCENT, "middle")
    d.pline([v.x(15300), v.y(LEV["floor"]), v.x(16500), v.y(LEV["L1"]),
             v.x(17900), v.y(LEV["L1"]), v.x(17900), v.y(LEV["L2"]),
             v.x(16500), v.y(LEV["L2"]), v.x(15300), v.y(LEV["slab"])],
            MID, 0.6)
    d.txt(v.x(16600), v.y(-4400), "MAIN STAIR", 4.0, MID, "middle")

    # escape shafts
    for cx, head, tag in ((2050, LEV["esc1_head"], "ESC 1"),
                          (19900, LEV["esc2_head"], "ESC 2")):
        d.rect(v.x(cx - 700), v.y(LEV["slab"]), v.d(1400), v.d(head + 2000),
               fill=colors.white, c=GREEN, sw=0.5)
        d.txt(v.x(cx), v.y(head) + 1.8, tag, 4.0, GREEN, "middle", bold=True)

    # headhouse and stairwell above
    hx, hy, hX, hY = GEOM["hh"]
    d.rect(v.x(hx), v.y(LEV["slab"]), v.d(hX - hx), v.d(2900), fill=None,
           c=ACCENT, sw=0.5)
    d.rect(v.x(hx), v.y(LEV["hh_soffit"]), v.d(hX - hx), v.d(500), fill=CONC,
           c=ACCENT, sw=0.5)
    d.txt(v.x(16000), v.y(-900), "HEADHOUSE", 4.4, ACCENT, "middle",
          bold=True)
    d.pline([v.x(9500), v.y(0), v.x(11000), v.y(0), v.x(14300),
             v.y(LEV["slab"]), v.x(15800), v.y(LEV["slab"])], ACCENT, 0.7)
    d.txt(v.x(12000), v.y(-1500), "COVERED ENTRY STAIRWELL", 4.2, ACCENT,
          "middle")

    for lv, lab in ((0, "0.000"), (LEV["slab"], "(-)2.000"),
                    (LEV["soffit"], "(-)2.900"), (LEV["floor"], "(-)6.100"),
                    (LEV["form"], "(-)6.800")):
        d.level(v.x(x0) + 3.0, v.y(lv), lab, 4.2, ACCENT, side=1)
    d.dimh(v.x(0), v.x(22000), v.y(-9200), "22 000", 4.6, INK)
    d.txt(0, 86 * mm, "LONGITUDINAL SECTION ON THE BOX CENTRELINE", 5.4,
          INK, bold=True)
    d.scalebar(15 * mm, 3.0 * mm, v, 5000, "5 m        1 : 168")
    return d


def fig_cross_section():
    """Transverse section -- the cover build-up, the box, the ground."""
    d = Fig(W, 156 * mm)
    v = V(72, 34 * mm, 126 * mm)
    gy0, gy1 = -800, 7000

    d.rect(v.x(gy0), v.y(-8600), v.d(gy1 - gy0), v.d(8600), fill=SOIL,
           c=None, sw=0)
    d.rockface(v.x(gy0), v.y(-8600), v.d(gy1 - gy0), v.d(8600 - 1500))
    d.line(v.x(gy0), v.y(-1500), v.x(gy1), v.y(-1500), MID, 0.35, [3, 2])
    d.line(v.x(gy0), v.y(LEV["gwt"]), v.x(gy1), v.y(LEV["gwt"]), BLUE, 0.55,
           [5, 2])

    for lab, t, b, col, load in COVER:
        d.rect(v.x(gy0), v.y(b), v.d(gy1 - gy0), v.d(t - b), fill=col, c=MID,
               sw=0.3)
        d.txt(v.x(gy1) + 2.0, v.y((t + b) / 2.0) - 1.0, lab, 4.0, INK)
        d.txt(W - 1.0, v.y((t + b) / 2.0) - 1.0, load, 4.0, MID, "end")
    d.txt(v.x(gy1) + 2.0, v.y(400), "ENGINEERED COVER  2 000", 4.6, INK,
          bold=True)
    d.txt(W - 1.0, v.y(400), "40.65", 4.6, INK, "end", bold=True)

    d.rect(v.x(0), v.y(LEV["mat"]), v.d(6200), v.d(4700), fill=CONC, c=INK,
           sw=0.7)
    d.rect(v.x(600), v.y(LEV["floor"]), v.d(5000), v.d(3200), fill=AIR,
           c=MID, sw=0.35)
    d.rect(v.x(0), v.y(LEV["form"]), v.d(6200), v.d(100), fill=CONC2, c=MID,
           sw=0.3)
    for hx, s in ((600, 500), (5600, -500)):
        d.poly([v.x(hx), v.y(LEV["soffit"]), v.x(hx + s), v.y(LEV["soffit"]),
                v.x(hx), v.y(LEV["soffit"] + 500)], fill=CONC, c=MID, sw=0.3)
        d.poly([v.x(hx), v.y(LEV["floor"]), v.x(hx + s), v.y(LEV["floor"]),
                v.x(hx), v.y(LEV["floor"] - 500)], fill=CONC, c=MID, sw=0.3)
    d.txt(v.x(3100), v.y(-4500), "5 000 x 3 200 CLEAR", 4.8, INK, "middle",
          bold=True)

    for lv, lab in ((0, "0.000 GRADE"), (LEV["slab"], "(-)2.000 T/SLAB"),
                    (LEV["soffit"], "(-)2.900 SOFFIT"),
                    (LEV["floor"], "(-)6.100 FLOOR"),
                    (LEV["mat"], "(-)6.700 U/S MAT"),
                    (LEV["form"], "(-)6.800 FORMATION")):
        d.level(v.x(gy0), v.y(lv), lab, 4.2, ACCENT, side=-1)
    d.txt(v.x(gy0) - 3.4, v.y(LEV["gwt"]) - 4.6, "DESIGN GWT [A]", 4.2, BLUE,
          "end", bold=True)

    for yy in (1200, 3100, 5000):
        d.arrow(v.x(yy), v.y(1500), v.x(yy), v.y(200), RED, 0.7)
    d.txt(v.x(3100), v.y(1800), "BLAST  383 kPa    K_a = 1.0", 4.8, RED,
          "middle", bold=True)
    for lv in (-3600, -5000):
        d.arrow(v.x(-700), v.y(lv), v.x(-60), v.y(lv), RED, 0.55)
        d.arrow(v.x(6900), v.y(lv), v.x(6260), v.y(lv), RED, 0.55)
    for yy in (1800, 4400):
        d.arrow(v.x(yy), v.y(-8200), v.x(yy), v.y(-6900), BLUE, 0.6)
    d.txt(v.x(3100), v.y(-8500), "UPLIFT 46.11 kPa = 6 289 kN", 4.4, BLUE,
          "middle", bold=True)

    d.dimv(v.y(LEV["soffit"]), v.y(LEV["slab"]), v.x(2400), "900", 4.0)
    d.dimv(v.y(LEV["mat"]), v.y(LEV["floor"]), v.x(2400), "600", 4.0)
    d.dimh(v.x(0), v.x(600), v.y(LEV["floor"]) - 4.2, "600", 3.9)
    d.dimh(v.x(5600), v.x(6200), v.y(LEV["floor"]) - 4.2, "600", 3.9)
    d.dimh(v.x(0), v.x(6200), v.y(LEV["form"]) - 5.4, "6 200", 4.4)
    d.dimv(v.y(LEV["floor"]), v.y(LEV["soffit"]), v.x(4600), "3 200", 4.0)
    d.txt(0, 150 * mm, "TRANSVERSE SECTION THROUGH THE BOX", 5.4, INK,
          bold=True)
    d.txt(v.x(gy1) + 2.0, 150 * mm, "kPa", 4.2, MID)
    d.scalebar(2 * mm, 4 * mm, v, 2000, "2 m      1 : 72")
    return d


# ===========================================================================
#  3  THE SCIENCE
# ===========================================================================

class Axes(object):
    """A minimal linear / logarithmic XY frame inside a Fig."""

    def __init__(self, d, x0, y0, w, h, xlim, ylim, xlog=False):
        self.d, self.x0, self.y0, self.w, self.h = d, x0, y0, w, h
        self.xa, self.xb = xlim
        self.ya, self.yb = ylim
        self.xlog = xlog
        d.line(x0, y0, x0 + w, y0, INK, 0.5)
        d.line(x0, y0, x0, y0 + h, INK, 0.5)

    def X(self, v):
        if self.xlog:
            return self.x0 + self.w * (math.log10(v) - math.log10(self.xa)) \
                / (math.log10(self.xb) - math.log10(self.xa))
        return self.x0 + self.w * (v - self.xa) / float(self.xb - self.xa)

    def Y(self, v):
        return self.y0 + self.h * (v - self.ya) / float(self.yb - self.ya)

    def xticks(self, vals, labels=None, size=4.2):
        for i, v in enumerate(vals):
            xx = self.X(v)
            self.d.line(xx, self.y0, xx, self.y0 - 1.6, MID, 0.35)
            lab = labels[i] if labels else str(v)
            self.d.txt(xx, self.y0 - 5.6, lab, size, MID, "middle")

    def yticks(self, vals, labels=None, size=4.2):
        for i, v in enumerate(vals):
            yy = self.Y(v)
            self.d.line(self.x0 - 1.6, yy, self.x0, yy, MID, 0.35)
            lab = labels[i] if labels else str(v)
            self.d.txt(self.x0 - 2.6, yy - 1.2, lab, size, MID, "end")

    def grid(self, xs=(), ys=()):
        for v in xs:
            self.d.line(self.X(v), self.y0, self.X(v), self.y0 + self.h,
                        RULE, 0.22)
        for v in ys:
            self.d.line(self.x0, self.Y(v), self.x0 + self.w, self.Y(v),
                        RULE, 0.22)

    def curve(self, pts, c=ACCENT, w=0.9, dash=None):
        out = []
        for x, y in pts:
            out += [self.X(x), self.Y(y)]
        self.d.pline(out, c, w, dash)

    def xlabel(self, s, size=4.4):
        self.d.txt(self.x0 + self.w / 2, self.y0 - 10.0, s, size, MID,
                   "middle")

    def ylabel(self, s, size=4.4):
        self.d.txt(self.x0 - 1.0, self.y0 + self.h + 3.2, s, size, MID,
                   "start", bold=True)


def fig_blast_wave():
    """The design pressure-time history at the structure."""
    d = Fig(W, 74 * mm)
    a = Axes(d, 22 * mm, 18 * mm, 128 * mm, 44 * mm, (-0.06, 1.55),
             (-90, 400))
    a.grid(ys=(0, 100, 200, 300))
    a.xticks([0, 0.13, 0.5, 1.0, 1.33],
             ["0", "0.13", "0.5", "1.0", "1.33"])
    a.yticks([0, 100, 200, 300, 344.7], ["0", "100", "200", "300", "344.7"])
    a.xlabel("time from arrival of the front,  seconds")
    a.ylabel("overpressure  kPa")

    td = 1.33
    pts = [(0.0, 0.0), (0.0, 344.7)]
    n = 60
    for i in range(n + 1):
        t = td * i / float(n)
        p = 344.7 * (1 - t / td) * math.exp(-1.8 * t / td)
        pts.append((t, p))
    for i in range(25):
        t = td + (0.14 * td) * i / 24.0
        p = -70.0 * math.sin(math.pi * (t - td) / (0.28 * td))
        pts.append((t, p))
    a.curve(pts, RED, 1.0)
    d.line(a.X(-0.06), a.Y(0), a.X(1.55), a.Y(0), INK, 0.4)

    d.line(a.X(0), a.Y(344.7), a.X(0.5), a.Y(344.7), MID, 0.3, [2, 2])
    d.txt(a.X(0.52), a.Y(344.7) - 1.2,
          "p_so = 344.7 kPa  (50 psi)  -  the DESIGN BASIS", 4.6, RED,
          bold=True)
    d.line(a.X(0.13), a.Y(-88), a.X(0.13), a.Y(120), MID, 0.3, [2, 2])
    d.dimh(a.X(0), a.X(1.33), a.Y(-82), "positive phase  t_d  =  0.13 to "
           "1.33 s", 4.4, MID)
    d.txt(a.X(1.36), a.Y(-45), "negative phase", 4.2, MID)
    d.txt(a.X(1.36), a.Y(-58), "not a separate load case", 4.0, MID)
    d.txt(a.X(0.30), a.Y(200), "IMPULSE  =  the area under the curve", 4.4,
          MID)
    d.txt(0, 68 * mm, "THE DESIGN BLAST WAVE", 5.4, INK, bold=True)
    d.txt(0, 2.0 * mm, "Shape indicative;  the DESIGN INPUTS are the peak "
          "and the duration, both confirmed.  The yield behind them is "
          "deliberately not stated  [N].", 4.2, MID)
    return d


def fig_dlf():
    """Dynamic load factor against ductility ratio."""
    d = Fig(W, 66 * mm)
    a = Axes(d, 24 * mm, 16 * mm, 84 * mm, 40 * mm, (0.9, 10.4), (0.9, 2.2))
    a.grid(ys=(1.0, 1.2, 1.4, 1.6, 1.8, 2.0))
    a.xticks([1, 2, 3, 4, 5, 6, 8, 10])
    a.yticks([1.0, 1.2, 1.4, 1.6, 1.8, 2.0],
             ["1.0", "1.2", "1.4", "1.6", "1.8", "2.0"])
    a.xlabel("ductility ratio  mu  =  maximum / yield displacement")
    a.ylabel("DLF")
    pts = [(1 + 9.4 * i / 120.0, (1 + 9.4 * i / 120.0) /
            ((1 + 9.4 * i / 120.0) - 0.5)) for i in range(121)]
    a.curve(pts, ACCENT, 1.1)
    for mu, lab, col in ((1.0, "mu = 1  ->  DLF 2.000\\nthe elastic step "
                          "load  -  the expression\\nreduces correctly at "
                          "its own limit", MID),
                         (5.0, "mu = 5  ->  DLF 1.111\\nADOPTED  -  moderate,"
                          " repairable damage", RED)):
        dlf = mu / (mu - 0.5)
        d.circ(a.X(mu), a.Y(dlf), 1.6, fill=col, c=col, sw=0)
        d.line(a.X(mu), a.Y(0.9), a.X(mu), a.Y(dlf), col, 0.35, [2, 2])
        for k, line in enumerate(lab.split("\\n")):
            d.txt(a.X(mu) + 3.0, a.Y(dlf) - 1.2 - k * 4.6, line,
                  4.3, col, bold=(k == 0))
    d.txt(116 * mm, 48 * mm, "DLF  =  mu / (mu - 0.5)", 5.0, INK, bold=True)
    d.txt(116 * mm, 42 * mm, "IS 4991 Cl. 10.3.3", 4.4, MID)
    d.txt(116 * mm, 34 * mm, "DESIGN PRESSURE", 4.6, RED, bold=True)
    d.txt(116 * mm, 28 * mm, "344.7 x 1.111  =  383 kPa", 4.6, RED)
    d.txt(116 * mm, 20 * mm, "A ductility ratio is a", 4.2, MID)
    d.txt(116 * mm, 15.6 * mm, "PROMISE ABOUT DETAILING,", 4.2, MID,
          bold=True)
    d.txt(116 * mm, 11.2 * mm, "not a discount.", 4.2, MID)
    d.txt(0, 60 * mm, "THE DYNAMIC LOAD FACTOR", 5.4, INK, bold=True)
    return d


def fig_regimes():
    """Where this structure sits on the t_d/T scale."""
    d = Fig(W, 52 * mm)
    x0, y0, w = 10 * mm, 22 * mm, 150 * mm
    bands = [(0.01, 0.1, "IMPULSIVE", colors.Color(0.93, 0.86, 0.86),
              "load over before the structure moves"),
             (0.1, 10.0, "DYNAMIC", colors.Color(0.93, 0.91, 0.84),
              "genuine transient interaction"),
             (10.0, 200.0, "QUASI-STATIC", colors.Color(0.86, 0.92, 0.87),
              "many cycles while the load is still on")]

    def X(v):
        return x0 + w * (math.log10(v) - math.log10(0.01)) / \
            (math.log10(200.0) - math.log10(0.01))

    for a, b, lab, col, note in bands:
        d.rect(X(a), y0, X(b) - X(a), 10 * mm, fill=col, c=MID, sw=0.35)
        d.txt((X(a) + X(b)) / 2, y0 + 6.2 * mm, lab, 5.0, INK, "middle",
              bold=True)
        d.txt((X(a) + X(b)) / 2, y0 + 2.4 * mm, note, 3.9, MID, "middle")
    for v in (0.01, 0.1, 1, 10, 100):
        d.line(X(v), y0, X(v), y0 - 1.8, MID, 0.35)
        d.txt(X(v), y0 - 5.8, str(v), 4.2, MID, "middle")
    d.txt(x0 + w / 2, y0 - 11.0, "t_d / T", 4.8, MID, "middle", bold=True)
    d.rect(X(10), y0 + 12 * mm, X(100) - X(10), 5.0, fill=RED, c=RED, sw=0)
    d.txt((X(10) + X(100)) / 2, y0 + 14.6 * mm,
          "THIS STRUCTURE   t_d/T  =  10 to 100", 4.8, colors.white,
          "middle", bold=True)
    d.txt(0, 46 * mm, "WHICH DYNAMIC REGIME THE STRUCTURE IS IN", 5.4, INK,
          bold=True)
    d.txt(0, 2.0 * mm, "Roof T = 13.4 ms against t_d 0.13-1.33 s.  A thick "
          "slab on a short span is very stiff, and a nuclear air blast is a "
          "long-duration load.  THAT is what makes a static analysis with a "
          "load factor an honest way to get the demand.", 4.2, MID)
    return d


def fig_cover():
    """The engineered cover, layer by layer, with what each one is for."""
    d = Fig(W, 104 * mm)
    v = V(34, 12 * mm, 94 * mm)
    reason = ["concealment, erosion, sheds rain",
              "stops fines clogging the drainage path",
              "BREAKS UP a penetrating item  -  it does not defeat one",
              "scatters burster energy",
              "RADIATION MASS  -  what the second metre buys",
              "protects the waterproofing membrane"]
    for i, (lab, t, b, col, load) in enumerate(COVER):
        yy, hh = v.y(b), v.d(t - b)
        d.rect(12 * mm, yy, 38 * mm, hh, fill=col, c=MID, sw=0.4)
        d.txt(52 * mm, yy + hh / 2 - 0.4, lab, 4.6, INK, bold=True)
        d.txt(52 * mm, yy + hh / 2 - 4.6, reason[i], 4.2, MID)
        d.txt(W - 1.0, yy + hh / 2 - 0.4, load + " kPa", 4.6, MID, "end")
    d.rect(12 * mm, v.y(-2900), 38 * mm, v.d(900), fill=CONC, c=INK, sw=0.6)
    d.txt(31 * mm, v.y(-2500), "900 PRESSURE SLAB", 4.4, INK, "middle",
          bold=True)
    d.dimv(v.y(-2000), v.y(0), 8 * mm, "2 000", 4.4)
    d.line(12 * mm, v.y(0), W, v.y(0), INK, 0.7)
    d.level(12 * mm, v.y(0), "0.000 GRADE", 4.4, ACCENT, side=1)

    ys = 27 * mm
    d.line(52 * mm, ys + 4.6, W, ys + 4.6, RULE, 0.35)
    d.txt(52 * mm, ys, "SUM OF THE SIX LAYERS", 4.6, INK, bold=True)
    d.txt(W - 1.0, ys, "39.15 kPa", 4.6, INK, "end", bold=True)
    d.txt(52 * mm, ys - 5.6, "declared allowance, held", 4.4, MID)
    d.txt(W - 1.0, ys - 5.6, "+   1.50", 4.4, MID, "end")
    d.line(52 * mm, ys - 8.6, W, ys - 8.6, INK, 0.5)
    d.txt(52 * mm, ys - 13.4, "DESIGN VALUE  -  DL2 in every model", 4.8,
          RED, bold=True)
    d.txt(W - 1.0, ys - 13.4, "40.65 kPa", 4.8, RED, "end", bold=True)

    d.txt(0, 99 * mm, "THE ENGINEERED COVER  -  2 000 mm IN SIX LAYERS",
          5.4, INK, bold=True)
    d.txt(0, 6.4 * mm, "The cover buys NO reduction in blast pressure:  "
          "K_a = 1.0 saturated, so a buried roof takes the full p_so.", 4.2,
          MID)
    d.txt(0, 2.4 * mm, "1.0 m already covers fallout at PF 2 200.  THE "
          "SECOND METRE IS BOUGHT ENTIRELY FOR PROMPT NEUTRON AND GAMMA "
          "ATTENUATION.", 4.2, MID)
    return d


def fig_lateral():
    """The lateral pressure diagram on a perimeter wall."""
    d = Fig(W, 104 * mm)
    v = V(80, 58 * mm, 94 * mm)
    sc = 0.30                                   # mm of paper per kPa

    d.rect(v.x(0), v.y(-6700), v.d(600), v.d(4700), fill=CONC, c=INK,
           sw=0.6)
    d.rect(v.x(-4000), v.y(-6700), v.d(4000), v.d(6700), fill=SOIL, c=None,
           sw=0)
    d.line(v.x(-4000), v.y(0), v.x(600), v.y(0), INK, 0.7)
    d.line(v.x(-4000), v.y(-2000), v.x(0), v.y(-2000), BLUE, 0.6, [4, 2])
    d.txt(v.x(-3900), v.y(-2000) + 1.6, "DESIGN GWT (-)2.000 [A]", 4.2,
          BLUE, bold=True)

    # static diagram, to the right of the wall
    xw = v.x(600) + 4.0
    p0, p1, p2 = 0.0, 20.0, 83.2
    d.poly([xw, v.y(0), xw + p1 * sc, v.y(-2000), xw + p2 * sc, v.y(-6100),
            xw, v.y(-6100)], fill=colors.Color(0.86, 0.90, 0.95), c=ACCENT,
           sw=0.5)
    d.txt(xw + p1 * sc + 2.0, v.y(-2000) - 1.2, "33.9 kPa at the soffit",
          4.2, ACCENT)
    d.txt(xw + p2 * sc + 2.0, v.y(-6100) - 1.2, "83.2 kPa at the floor",
          4.4, ACCENT, bold=True)
    d.txt(xw + 2.0, v.y(-3600), "EARTH + WATER", 4.4, ACCENT, bold=True)
    d.txt(xw + 2.0, v.y(-4100), "gradient 15.41 kPa/m", 4.2, ACCENT)
    d.txt(xw + 2.0, v.y(-4600), "of which WATER 9.81  (64 %)", 4.2, BLUE,
          bold=True)
    d.txt(xw + 2.0, v.y(-5100), "and soil only 5.60", 4.2, MID)

    # blast diagram, to the left
    xb = v.x(0) - 4.0
    d.poly([xb, v.y(-2900), xb - 383 * sc * 0.30, v.y(-2900),
            xb - 383 * sc * 0.30, v.y(-6100), xb, v.y(-6100)],
           fill=colors.Color(0.97, 0.88, 0.88), c=RED, sw=0.5)
    for lv in (-3300, -4200, -5100, -5900):
        d.arrow(xb - 383 * sc * 0.30 - 6.0, v.y(lv), xb - 1.0, v.y(lv),
                RED, 0.6)
    d.txt(xb - 383 * sc * 0.30 - 8.0, v.y(-4000), "BLAST  383 kPa", 4.8, RED,
          "end", bold=True)
    d.txt(xb - 383 * sc * 0.30 - 8.0, v.y(-4600), "UNIFORM over the height",
          4.2, RED, "end")
    d.txt(xb - 383 * sc * 0.30 - 8.0, v.y(-5200), "BLAST GOVERNS  4.6 : 1",
          4.4, RED, "end", bold=True)

    for lv, lab in ((0, "0.000"), (-2900, "(-)2.900"), (-6100, "(-)6.100"),
                    (-6700, "(-)6.700")):
        d.level(v.x(700), v.y(lv), lab, 4.2, MID, side=1)
    d.txt(0, 100 * mm, "LATERAL PRESSURE ON A PERIMETER WALL  -  THE TWO "
          "CASES COMPARED", 5.4, INK, bold=True)
    d.txt(0, 2.0 * mm, "The static case is a triangle that starts at the "
          "water table;  the blast case is a rectangle over the whole "
          "height, because K_a = 1.0 transmits it undiminished.", 4.2, MID)
    return d


def fig_flotation():
    """Weight against uplift at the four construction stages."""
    d = Fig(W, 84 * mm)
    x0, y0, w = 40 * mm, 20 * mm, 96 * mm
    top = 13000.0
    stages = [("1  mat cast only", 2009, 0.33),
              ("2  mat + walls, no roof", 4802, 0.78),
              ("3  box complete, no backfill", 7528, 1.22),
              ("4  backfilled and covered", 12453, 2.02)]
    d.line(x0, y0, x0 + w, y0, INK, 0.5)
    for q in (0, 4000, 8000, 12000):
        xx = x0 + w * q / top
        d.line(xx, y0, xx, y0 - 1.6, MID, 0.35)
        d.txt(xx, y0 - 5.6, "%d" % q, 4.2, MID, "middle")
    d.txt(x0 + w / 2, y0 - 10.4, "kN", 4.4, MID, "middle")
    for i, (lab, wt, fos) in enumerate(stages):
        yy = y0 + 46 * mm - i * 11 * mm
        ok = fos >= 1.2
        col = GREEN if ok else RED
        d.rect(x0, yy, w * wt / top, 6.0, fill=col, c=col, sw=0)
        d.txt(x0 - 2.0, yy + 1.6, lab, 4.4, INK, "end")
        d.txt(x0 + w * wt / top + 2.0, yy + 1.6, "%d kN" % wt, 4.2, col)
        d.txt(x0 + w + 16 * mm, yy + 1.6,
              "FoS %.2f   %s" % (fos, "OK" if ok else
                                 ("MARGINAL" if fos > 1.0 else "FAIL")),
              4.6, col, "end", bold=True)
    xu = x0 + w * 6175 / top
    d.line(xu, y0, xu, y0 + 54 * mm, BLUE, 0.8)
    d.txt(xu + 1.6, y0 + 55 * mm, "UPLIFT  6 175 kN  -  it does not change",
          4.4, BLUE, bold=True)
    d.txt(0, 78 * mm, "FLOTATION  -  THE CONSTRUCTION STAGE GOVERNS", 5.4,
          INK, bold=True)
    d.txt(0, 2.0 * mm, "Buoyancy competes with weight, and the weight "
          "arrives late.  Require FoS >= 1.2.  Figures at the pre-lengthening "
          "box;  both sides scale with length, so every factor is unchanged.",
          4.2, MID)
    return d


# ===========================================================================
#  4  ELEMENTS AND REINFORCEMENT
# ===========================================================================

def _bars(d, v, x0, x1, y, n, dia, col=RED, r=0.85):
    """A row of bar dots between two model x positions."""
    for i in range(n):
        xx = x0 + (x1 - x0) * (i + 0.5) / n
        d.circ(v.x(xx), v.y(y), r, fill=col, c=col, sw=0)


def fig_wall_section():
    """Typical perimeter wall, 600 thk, with its two curtains."""
    d = Fig(W, 84 * mm)
    v = V(15, 42 * mm, 14 * mm)
    t, h = 600, 1000
    d.rect(v.x(-400), v.y(0), v.d(400), v.d(h), fill=SOIL, c=None, sw=0)
    d.hatch(v.x(-400), v.y(0), v.d(400), v.d(h), 45, 3.4,
            colors.Color(0.76, 0.72, 0.64), 0.2)
    d.rect(v.x(0), v.y(0), v.d(t), v.d(h), fill=CONC, c=INK, sw=0.8)
    for cov in (75, t - 40):
        for k in range(9):
            yy = 60 + k * 150
            if yy > h - 50:
                break
            d.circ(v.x(cov), v.y(yy), 1.6, fill=RED, c=RED, sw=0)
        d.line(v.x(cov), v.y(35), v.x(cov), v.y(h - 35), RED, 0.6)
    for k in range(7):
        yy = 100 + k * 200
        if yy > h - 70:
            break
        d.rect(v.x(70), v.y(yy - 22), v.d(t - 140), v.d(44), fill=None,
               c=VIOLET, sw=0.6)
    d.dimh(v.x(0), v.x(600), v.y(0) - 6.0, "600", 4.8, INK)
    d.dimh(v.x(0), v.x(75), v.y(h) + 4.2, "75", 4.0)
    d.dimh(v.x(560), v.x(600), v.y(h) + 4.2, "40", 4.0)
    d.leader(v.x(75), v.y(510), v.x(84 * mm - 42 * mm + v.x(0), ),
             v.y(760), "", 4.0) if False else None
    d.leader(v.x(75), v.y(510), 92 * mm, 52 * mm,
             "T16 @ 150 EACH FACE EACH WAY  =  1 340 mm2/m per face",
             4.6, RED)
    d.leader(v.x(300), v.y(300), 92 * mm, 38 * mm,
             "T12 CLOSED LINKS @ 200   (Asv/sv 1.131 v. 0.982 required)",
             4.4, VIOLET)
    d.txt(v.x(-390), v.y(h) + 4.2, "EARTH FACE", 4.2, MID)
    d.txt(v.x(640), v.y(h) + 4.2, "INTERNAL", 4.2, MID)
    for lv in (180, 500, 820):
        d.arrow(v.x(-380), v.y(lv), v.x(-20), v.y(lv), RED, 0.6)
    d.txt(v.x(-390), v.y(-12 * 15), "", 4.0)
    d.txt(92 * mm, 68 * mm, "BLAST  383 kPa   -   GOVERNS 4.6 : 1 over the",
          4.6, RED, bold=True)
    d.txt(92 * mm, 63.6 * mm, "83.2 kPa static earth-and-water case", 4.6,
          RED)
    d.txt(92 * mm, 28 * mm, "600 IS NOT STRENGTH-GOVERNED  -  it is 68 %",
          4.4, INK, bold=True)
    for k, ln in enumerate(["75 mm cover against blinding and trimmed rock",
                            "congestion:  two curtains, closed links,",
                            "     waterstops and cast-in frames",
                            "IS 3370 crack control under sustained head",
                            "the EMP double curtain at 150",
                            "the 1 168 kN/m axial path from the roof"]):
        d.txt(92 * mm, 23 * mm - k * 4.4, ln, 4.2, MID)
    d.txt(0, 79 * mm, "PERIMETER WALL W1 - W4   600 thk   1 : 15", 5.4, INK,
          bold=True)
    return d


def fig_w6_and_door():
    """W6 / W7 section and the blast door opening elevation."""
    d = Fig(W, 106 * mm)
    v = V(16, 24 * mm, 18 * mm)
    t, h = 400, 900
    d.rect(v.x(0), v.y(0), v.d(t), v.d(h), fill=CONC, c=RED, sw=0.9)
    for cov in (50, t - 40):
        for k in range(7):
            yy = 70 + k * 150
            if yy > h - 50:
                break
            d.circ(v.x(cov), v.y(yy), 1.8, fill=RED, c=RED, sw=0)
        d.line(v.x(cov), v.y(35), v.x(cov), v.y(h - 35), RED, 0.6)
    for k in range(5):
        yy = 110 + k * 200
        if yy > h - 70:
            break
        d.rect(v.x(46), v.y(yy - 20), v.d(t - 92), v.d(40), fill=None,
               c=VIOLET, sw=0.6)
        d.line(v.x(t / 2.0), v.y(yy - 20), v.x(t / 2.0), v.y(yy + 20),
               VIOLET, 0.5)
    d.dimh(v.x(0), v.x(400), v.y(0) - 6.0, "400", 4.8, INK)
    d.txt(v.x(200), v.y(h) + 4.6, "W6 / W7", 5.0, RED, "middle", bold=True)
    d.txt(4 * mm, 48 * mm, "T20 @ 150 EF EW", 4.5, RED, bold=True)
    d.txt(4 * mm, 43.6 * mm, "2 094 mm2/m per face", 4.2, RED)
    d.txt(4 * mm, 37 * mm, "T12 4-LEG LINKS @ 200", 4.5, VIOLET, bold=True)
    for lv in (200, 480, 760):
        d.arrow(v.x(-240), v.y(lv), v.x(-15), v.y(lv), RED, 0.6)
    d.txt(4 * mm, 28 * mm, "383 kPa out of", 4.5, RED, bold=True)
    d.txt(4 * mm, 23.6 * mm, "the stair SHAFT", 4.5, RED, bold=True)
    d.txt(4 * mm, 16 * mm, "The shaft fills in", 4.2, MID)
    d.txt(4 * mm, 11.6 * mm, "0.094 s against a", 4.2, MID)
    d.txt(4 * mm, 7.2 * mm, "t_d of 0.13 s", 4.2, MID)

    ve = V(42, 66 * mm, 14 * mm)
    d.rect(ve.x(-900), ve.y(0), ve.d(3000), ve.d(3200), fill=CONC2, c=MID,
           sw=0.5)
    d.rect(ve.x(0), ve.y(0), ve.d(1200), ve.d(2100), fill=colors.white,
           c=RED, sw=0.9)
    d.txt(ve.x(600), ve.y(1250), "BLAST DOOR", 4.6, RED, "middle", bold=True)
    d.txt(ve.x(600), ve.y(950), "1 200 x 2 100", 4.4, RED, "middle")
    d.txt(ve.x(600), ve.y(650), ">= 7 bar", 4.2, RED, "middle")
    d.txt(ve.x(600), ve.y(380), "gas-tight, rebound-rated", 3.9, RED,
          "middle")
    for xx in (-130, 1330):
        for k in range(4):
            d.circ(ve.x(xx), ve.y(300 + k * 500), 1.6, fill=RED, c=RED, sw=0)
    d.rect(ve.x(-150), ve.y(2100), ve.d(1500), ve.d(1100), fill=CONC, c=INK,
           sw=0.7)
    d.txt(ve.x(600), ve.y(2700), "HEADER 400 x 1100", 4.4, INK, "middle",
          bold=True)
    d.txt(ve.x(600), ve.y(2380), "4-T20 top + 4-T20 bottom", 4.0, INK,
          "middle")
    d.txt(ve.x(600), ve.y(2160), "T12 4-leg links @ 150", 4.0, INK, "middle")
    d.dimh(ve.x(0), ve.x(1200), ve.y(0) - 5.0, "1 200", 4.4)
    d.txt(136 * mm, 74 * mm, "4-T20 EACH JAMB", 4.4, RED, bold=True)
    d.txt(136 * mm, 69.6 * mm, "EACH FACE", 4.4, RED, bold=True)
    d.txt(136 * mm, 65.2 * mm, "anchored L_d 800", 4.1, RED)
    d.txt(136 * mm, 60.8 * mm, "beyond the opening", 4.1, RED)
    d.txt(136 * mm, 52 * mm, "Cast-in steel frame,", 4.1, MID)
    d.txt(136 * mm, 47.6 * mm, "WELDED TO THE CAGE", 4.1, INK, bold=True)
    d.txt(136 * mm, 43.2 * mm, "-  the blast fixing AND", 4.1, MID)
    d.txt(136 * mm, 38.8 * mm, "the only EMP continuity", 4.1, MID)
    d.txt(136 * mm, 34.4 * mm, "the opening has", 4.1, MID)
    d.txt(66 * mm, 96 * mm, "BLAST DOOR OPENING  -  ELEVATION", 5.0, INK,
          bold=True)
    d.txt(0, 101 * mm, "W6 / W7   400 thk   -   THE PROTECTIVE BOUNDARY",
          5.4, INK, bold=True)
    d.txt(0, 2.0 * mm, "200 thk is IMPOSSIBLE here, not merely awkward:  "
          "Mu,lim = 138.0 kNm/m against a demand of 245.1 kNm/m.  No steel "
          "ratio closes that gap, so the GEOMETRY changed.", 4.2, MID)
    return d


def fig_roof_section():
    """Pressure slab section -- reinforcement and link zones."""
    d = Fig(W, 98 * mm)
    v = V(40, 26 * mm, 38 * mm)
    d.rect(v.x(0), v.y(0), v.d(5000), v.d(900), fill=CONC, c=INK, sw=0.9)
    d.rect(v.x(-600), v.y(-800), v.d(600), v.d(1700), fill=CONC, c=INK,
           sw=0.7)
    d.rect(v.x(5000), v.y(-800), v.d(600), v.d(1700), fill=CONC, c=INK,
           sw=0.7)
    for cov in (75, 825):
        for k in range(34):
            xx = 75 + k * 150
            if xx > 4930:
                break
            d.circ(v.x(xx), v.y(cov), 1.3, fill=RED, c=RED, sw=0)
        d.line(v.x(40), v.y(cov), v.x(4960), v.y(cov), RED, 0.6)
    for a0, b0, sp in ((0, 1500, 250), (1500, 3500, 300), (3500, 5000, 250)):
        k = a0 + 40
        while k < b0:
            d.rect(v.x(k), v.y(70), v.d(5), v.d(760), fill=None, c=VIOLET,
                   sw=0.5)
            k += sp
    d.rect(v.x(0), v.y(-3), v.d(1500), v.d(6), fill=VIOLET, c=VIOLET, sw=0)
    d.rect(v.x(3500), v.y(-3), v.d(1500), v.d(6), fill=VIOLET, c=VIOLET,
           sw=0)
    d.dimv(v.y(0), v.y(900), v.x(-900), "900", 4.6)
    d.dimh(v.x(0), v.x(5000), v.y(-1200), "5 000 CLEAR", 5.0, INK)
    d.dimh(v.x(0), v.x(1500), v.y(-400), "1 500", 4.2)
    d.dimh(v.x(3500), v.x(5000), v.y(-400), "1 500", 4.2)
    d.txt(v.x(2500), v.y(1150), "T25 @ 150 EF EW   =   3 272 mm2/m per face",
          4.8, RED, "middle", bold=True)
    d.txt(v.x(750), v.y(-700), "T12 4-LEG @ 250", 4.2, VIOLET, "middle",
          bold=True)
    d.txt(v.x(2500), v.y(-700), "T12 2-LEG @ 300", 4.2, VIOLET, "middle")
    d.txt(v.x(4250), v.y(-700), "T12 4-LEG @ 250", 4.2, VIOLET, "middle",
          bold=True)
    for xx in (800, 2500, 4200):
        d.arrow(v.x(xx), v.y(1850), v.x(xx), v.y(1000), RED, 0.9)
    d.txt(v.x(2500), v.y(2050), "w  =  448.15 kPa    COMB 103", 5.2, RED,
          "middle", bold=True)
    d.txt(0, 93 * mm, "PRESSURE SLAB   900 thk   -   THE GOVERNING ELEMENT   "
          "1 : 40", 5.4, INK, bold=True)
    d.txt(0, 2.0 * mm, "Aspect 20.8 / 5.0 = 4.2, so the slab spans ONE-WAY "
          "across the 5 m width and lengthening the box adds no roof moment. "
          " Mp 700.2 against Mu 1 362.4 kNm/m  -  51 % utilised, x_u/d = "
          "0.139.", 4.2, MID)
    return d


def fig_roof_openings():
    """Roof plan -- the void, the two shafts and their trimmers."""
    d = Fig(W, 80 * mm)
    v = V(150, 13 * mm, 24 * mm)
    d.rect(v.x(0), v.y(0), v.d(22000), v.d(6200), fill=CONC, c=INK, sw=0.7)
    vx, vy, vX, vY = GEOM["void"]
    d.rect(v.x(vx), v.y(vy), v.d(vX - vx), v.d(vY - vy), fill=colors.white,
           c=ACCENT, sw=0.8)
    d.rect(v.x(vx), v.y(vY), v.d(vX - vx), v.d(5600 - vY), fill=WARN, c=RED,
           sw=0.6)
    d.txt(v.x((vx + vX) / 2), v.y(4750), "CANTILEVER PAD", 4.2, RED,
          "middle", bold=True)
    d.txt(v.x((vx + vX) / 2), v.y(4250), "root M 758.6 kNm/m", 3.8, RED,
          "middle")
    d.txt(v.x((vx + vX) / 2), v.y(2300), "STAIR VOID", 4.2, ACCENT, "middle",
          bold=True)
    d.txt(v.x((vx + vX) / 2), v.y(1800), "2 800 x 3 160", 3.8, ACCENT,
          "middle")
    for cx, cy in (GEOM["esc1"], GEOM["esc2"]):
        d.circ(v.x(cx), v.y(cy), v.d(1300), fill=CONC2, c=MID, sw=0.4,
               dash=[2, 1.5])
        d.circ(v.x(cx), v.y(cy), v.d(950), fill=colors.white, c=GREEN,
               sw=0.6)
        d.circ(v.x(cx), v.y(cy), v.d(700), fill=colors.white, c=GREEN,
               sw=0.8)
        for ang in range(0, 360, 30):
            rr = math.radians(ang)
            d.line(v.x(cx + 700 * math.cos(rr)),
                   v.y(cy + 700 * math.sin(rr)),
                   v.x(cx + 950 * math.cos(rr)),
                   v.y(cy + 950 * math.sin(rr)), RED, 0.3)
    d.txt(3 * mm, 66 * mm, "5-T25 EACH SIDE / FACE / DIRECTION at the "
          "collars, L_d 1 000 beyond", 4.3, RED, bold=True)
    d.txt(3 * mm, 61.6 * mm, "collar 250 RC  ·  slab thickened 900 -> 1 200 "
          "over a 600 annulus", 4.2, MID)
    d.txt(3 * mm, 14 * mm, "4-T25 EACH FACE at 45 deg, 2 000 each way, at "
          "BOTH re-entrant corners", 4.3, RED, bold=True)
    d.txt(3 * mm, 9.6 * mm, "6-T25 top and bottom in the thickened free "
          "edge  ·  6-T25 band over W6 and W7", 4.2, MID)
    d.txt(3 * mm, 5.2 * mm, "T12 4-LEG LINKS @ 250 THROUGHOUT THE PAD  -  "
          "a requirement in its own right", 4.2, VIOLET, bold=True)
    d.dimh(v.x(vx), v.x(vX), v.y(0) - 5.0, "2 800", 4.2)
    d.dimv(v.y(vy), v.y(vY), v.x(vx) - 4.0, "3 160", 4.2)
    d.dimv(v.y(vY), v.y(5600), v.x(vX) + 4.0, "1 840", 4.2)
    d.txt(0, 74 * mm, "ROOF PLAN  -  OPENINGS AND TRIMMERS   1 : 150", 5.4,
          INK, bold=True)
    return d


def fig_mat_section():
    """The mat, and the soft-band case that sizes it."""
    d = Fig(W, 82 * mm)
    v = V(70, 12 * mm, 38 * mm)
    d.rect(v.x(0), v.y(-1600), v.d(9000), v.d(1500), fill=ROCK, c=None, sw=0)
    d.hatch(v.x(0), v.y(-1600), v.d(9000), v.d(1500), 45, 4.0,
            colors.Color(0.66, 0.68, 0.66), 0.2)
    d.rect(v.x(3000), v.y(-1600), v.d(3000), v.d(1500), fill=WARN, c=RED,
           sw=0.7, dash=[2.5, 2])
    d.txt(v.x(4500), v.y(-800), "RED-BOLE / VESICULAR SEAM", 4.6, RED,
          "middle", bold=True)
    d.txt(v.x(4500), v.y(-1200), "3.0 m of support REMOVED, worst position",
          4.2, RED, "middle")
    d.rect(v.x(0), v.y(-100), v.d(9000), v.d(100), fill=CONC2, c=MID,
           sw=0.35)
    d.rect(v.x(0), v.y(0), v.d(9000), v.d(600), fill=CONC, c=INK, sw=0.8)
    for cov in (75, 525):
        d.line(v.x(80), v.y(cov), v.x(8920), v.y(cov), RED, 0.6)
        for k in range(60):
            xx = 150 + k * 150
            if xx > 8880:
                break
            d.circ(v.x(xx), v.y(cov), 1.1, fill=RED, c=RED, sw=0)
    for k in range(36):
        xx = 125 + k * 250
        if xx > 8900:
            break
        d.rect(v.x(xx), v.y(60), v.d(4), v.d(480), fill=None, c=VIOLET,
               sw=0.45)
    for xx in (1500, 4500, 7500):
        d.arrow(v.x(xx), v.y(1900), v.x(xx), v.y(700), RED, 0.9)
    d.txt(v.x(4500), v.y(2150), "q  =  404.9 kPa   blast bearing", 5.0, RED,
          "middle", bold=True)
    d.dimh(v.x(3000), v.x(6000), v.y(-350), "3 000 unsupported", 4.4, RED)
    d.dimv(v.y(0), v.y(600), v.x(-420), "600", 4.4)
    d.txt(3 * mm, 11.0 * mm, "T16 @ 150 EF EW  =  1 340 mm2/m per face   ->   "
          "M 303.7 against Mu 362.8 kNm/m  =  84 %, the worst in the box",
          4.3, RED, bold=True)
    d.txt(3 * mm, 7.0 * mm, "T12 CLOSED LINKS ON A 250 x 250 GRID  -  twice "
          "the shear requirement, and it doubles as the spacer system "
          "between the curtains", 4.2, VIOLET)
    d.txt(3 * mm, 3.0 * mm, "Uplift case (net 31.1 kPa up over 5 000) gives "
          "only 48.6 kNm/m.  Bearing governs NOTHING  -  12.5 % of the "
          "presumptive value.", 4.2, MID)
    d.txt(0, 77 * mm, "MAT FOUNDATION   600 thk   -   THE CASE THAT SIZES "
          "IT   1 : 70", 5.4, INK, bold=True)
    return d


def fig_esc_head():
    """Escape shaft head -- the hatch, the collar and the ladder."""
    d = Fig(W, 124 * mm)
    v = V(40, 44 * mm, 90 * mm)
    top = 700
    for lab, t, b, col, load in COVER:
        d.rect(v.x(-1600), v.y(b), v.d(3200), v.d(t - b), fill=col, c=MID,
               sw=0.25)
    d.rect(v.x(-1600), v.y(-2900), v.d(650), v.d(900), fill=CONC, c=INK,
           sw=0.6)
    d.rect(v.x(950), v.y(-2900), v.d(650), v.d(900), fill=CONC, c=INK,
           sw=0.6)
    d.rect(v.x(-950), v.y(-2900), v.d(1900), v.d(3600), fill=CONC, c=INK,
           sw=0.7)
    d.rect(v.x(-700), v.y(-2900), v.d(1400), v.d(3600), fill=colors.white,
           c=GREEN, sw=0.8)
    d.rect(v.x(-800), v.y(top), v.d(1600), v.d(130),
           fill=colors.Color(0.72, 0.74, 0.78), c=INK, sw=0.9)
    for xx in range(-650, 700, 180):
        d.line(v.x(xx), v.y(top), v.x(xx), v.y(top - 170), INK, 0.5)
    d.rect(v.x(-800), v.y(top - 170), v.d(1600), v.d(170), fill=None, c=INK,
           sw=0.4)
    for k in range(9):
        yy = -2700 + k * 400
        if yy > top - 300:
            break
        d.line(v.x(-200), v.y(yy), v.x(200), v.y(yy), VIOLET, 0.8)
    d.line(v.x(-200), v.y(-2700), v.x(-200), v.y(top - 350), VIOLET, 0.5)
    d.line(v.x(200), v.y(-2700), v.x(200), v.y(top - 350), VIOLET, 0.5)
    d.arrow(v.x(-1300), v.y(1250), v.x(-1300), v.y(900), RED, 0.9)
    d.txt(v.x(-1400), v.y(1000), "383 kPa", 4.6, RED, "end", bold=True)
    d.level(v.x(-1560), v.y(top), "+0.700", 4.2, ACCENT, side=1)
    d.level(v.x(-1560), v.y(0), "0.000", 4.2, ACCENT, side=1)
    d.level(v.x(-1560), v.y(-2000), "(-)2.000", 4.2, ACCENT, side=1)
    d.dimh(v.x(-700), v.x(700), v.y(-3100), "1 400 CLEAR", 4.4, INK)
    d.txt(v.x(0), v.y(-3500), "250 RC COLLAR, OD 1 900", 4.2, MID, "middle")

    d.txt(92 * mm, 114 * mm, "THE HATCH  -  a structural closure", 4.8, INK,
          bold=True)
    for k, ln in enumerate([
            "589.6 kN on the leaf at 383 kPa",
            "M = w.a^2(3+nu)/16 = 38.71 kNm/m",
            "a flat Fe250 plate would be 32 mm",
            "      and 505 kg  -  UNLIFTABLE",
            "ADOPTED  ribbed steel weldment, 1 600 dia,",
            "12 mm face, 8 radial ribs 150 x 10,",
            "150 x 12 perimeter ring, seating ring",
            "CAST INTO the 250 collar, bearing 150",
            "FOUR QUARTER-TURN DOGS  -  it must",
            "resist UPLIFT too:  the negative phase",
            "and the rebound both lift it",
            "counterbalanced, openable from inside by",
            "one person without a key or a tool",
            "indicative leaf mass  ~ 322 kg"]):
        d.txt(92 * mm, 109 * mm - k * 4.4, ln, 4.1,
              INK if k in (4,) else MID)
    d.txt(92 * mm, 40 * mm, "THE LADDER", 4.8, VIOLET, bold=True)
    for k, ln in enumerate([
            "20 dia galvanised MS rungs, 400 clear,",
            "equal pitch  -  297.6 mm in ESC 1 over 21",
            "spaces, 295.7 in ESC 2 over 23",
            ">= 200 behind the rung, >= 750 in front",
            "grab rails 1 100 above the head",
            "NO fall-arrest.  NO rest platform.  And a",
            "vertical ladder cannot pass a stretcher."]):
        d.txt(92 * mm, 35 * mm - k * 4.4, ln, 4.1,
              RED if k >= 5 else MID)
    d.txt(0, 119 * mm, "ESCAPE SHAFT HEAD  -  A 1.54 m2 HOLE IN THE "
          "PROTECTIVE BOUNDARY   1 : 40", 5.4, INK, bold=True)
    return d


def fig_opening_corner():
    """The 209-degree corner at the top of the entry flight."""
    d = Fig(W, 78 * mm)
    for panel, x0, tag in ((0, 12 * mm, "TOP OF THE FLIGHT  -  THE TENSION "
                            "FACE TURNS 209 deg"),
                           (1, 96 * mm, "FOOT OF THE FLIGHT  -  THE CORNER "
                            "CLOSES, 151 deg")):
        v = V(30, x0, 22 * mm)
        if panel == 0:
            d.poly([v.x(0), v.y(0), v.x(1100), v.y(0), v.x(1100), v.y(250),
                    v.x(250), v.y(250), v.x(250), v.y(1200), v.x(0),
                    v.y(1200)], fill=CONC, c=INK, sw=0.7)
            d.pline([v.x(60), v.y(1200), v.x(60), v.y(60), v.x(1100),
                     v.y(60)], RED, 1.2)
            d.arrow(v.x(330), v.y(620), v.x(90), v.y(620), RED, 0.7)
            d.txt(v.x(350), v.y(620) - 1.4, "bend resultant pushes OUT",
                  4.2, RED)
            d.txt(v.x(350), v.y(380), "of the concrete", 4.2, RED)
            d.txt(x0, 12 * mm, "MAIN BARS SHALL NOT BE BENT ROUND IT.",
                  4.6, RED, bold=True)
            d.txt(x0, 7.6 * mm, "Each layer continued STRAIGHT, CROSSED,",
                  4.3, INK)
            d.txt(x0, 3.6 * mm, "anchored L_d = 640 into the OPPOSITE face,",
                  4.3, INK)
            d.txt(x0, -0.4 * mm + 1.0 * mm, "", 4.0)
        else:
            d.poly([v.x(0), v.y(0), v.x(1100), v.y(0), v.x(1100), v.y(1200),
                    v.x(850), v.y(1200), v.x(850), v.y(250), v.x(0),
                    v.y(250)], fill=CONC, c=INK, sw=0.7)
            d.pline([v.x(0), v.y(190), v.x(910), v.y(190), v.x(910),
                     v.y(1200)], GREEN, 1.2)
            d.txt(x0, 12 * mm, "BARS MAY TURN NORMALLY.", 4.6, GREEN,
                  bold=True)
            d.txt(x0, 7.6 * mm, "The bend resultant is directed INTO the",
                  4.3, INK)
            d.txt(x0, 3.6 * mm, "concrete, which is what a closing corner "
                  "does.", 4.3, INK)
        d.txt(x0, 66 * mm, tag, 4.6, INK, bold=True)
    d.txt(0, 73 * mm, "THE OPENING CORNER  -  THE DETAIL MOST OFTEN GOT "
          "WRONG        SP 34 Cl. 5.5", 5.4, INK, bold=True)
    d.txt(12 * mm, 16.5 * mm, "plus a U-bar T16 @ 200 across the corner.",
          4.3, INK)
    return d


# ===========================================================================
#  5  SERVICES -- HVAC AND CBRN
# ===========================================================================

def _box(d, x, y, w, h, title, lines=(), fill=PLANT, c=ACCENT, ts=4.6,
         ls=4.0, tc=INK, lc=MID, sw=0.6, dash=None):
    """A labelled schematic box.  Paper millimetres."""
    d.rect(x, y, w, h, fill=fill, c=c, sw=sw, dash=dash)
    d.txt(x + w / 2.0, y + h - 5.0, title, ts, tc, "middle", bold=True)
    for i, ln in enumerate(lines):
        d.txt(x + w / 2.0, y + h - 9.8 - i * 4.0, ln, ls, lc, "middle")
    return (x + w / 2.0, y + h / 2.0)


def _chain(d, x1, y1, x2, y2, c=ACCENT, w=0.8, label=None, size=4.0,
           above=1.8):
    d.arrow(x1, y1, x2, y2, c, w)
    if label:
        d.txt((x1 + x2) / 2.0, (y1 + y2) / 2.0 + above, label, size, c,
              "middle", bold=True)


def fig_filter_train():
    """The seven stages of the NBC filter train, in the order air meets them."""
    d = Fig(W, 76 * mm)
    stages = [
        ("WEATHER\nLOUVRE", "sand and", "debris trap", PLANT),
        ("BLAST\nVALVE", "< 2 ms close", "holds 1.3 s", WARN),
        ("PRE-FILTER", "G4 / F7", "protects the HEPA", PLANT),
        ("HEPA", "EN 1822 H14", "99.995 % at MPPS", PLANT),
        ("CARBON", "ASZM-TEDA", "300 000 mg.min/m3", WARN),
        ("FAN", "electric PLUS", "HAND CRANK", PLANT),
        ("PLENUM", "+50 to +100 Pa", "sets leak direction", PLANT)]
    n = len(stages)
    gap = 3.4 * mm
    bw = (W - (n - 1) * gap) / n
    y0, bh = 38 * mm, 22 * mm
    for i, (t1, l1, l2, col) in enumerate(stages):
        x = i * (bw + gap)
        d.rect(x, y0, bw, bh, fill=col, c=ACCENT, sw=0.6)
        head = t1.split("\n")
        for k, hl in enumerate(head):
            d.txt(x + bw / 2.0, y0 + bh - 5.4 - k * 4.6, hl, 4.8, INK,
                  "middle", bold=True)
        base = y0 + bh - 5.4 - len(head) * 4.6 - 1.4
        d.txt(x + bw / 2.0, base, l1, 3.9, MID, "middle")
        d.txt(x + bw / 2.0, base - 4.0, l2, 3.9, MID, "middle")
        d.txt(x + bw / 2.0, y0 - 4.6, str(i + 1), 4.4, FAINT, "middle",
              bold=True)
        if i < n - 1:
            d.arrow(x + bw + 0.6, y0 + bh / 2.0, x + bw + gap - 0.6,
                    y0 + bh / 2.0, ACCENT, 0.8, 2.2)
        # differential-pressure gauge on every stage
        d.circ(x + bw / 2.0, y0 + bh + 5.0, 2.4, fill=colors.white, c=MID,
               sw=0.4)
        d.txt(x + bw / 2.0, y0 + bh + 3.8, "dP", 3.4, MID, "middle")
        d.line(x + bw / 2.0, y0 + bh, x + bw / 2.0, y0 + bh + 2.6, MID, 0.3)
    d.txt(0, 68 * mm, "THE NBC FILTER TRAIN  -  SEVEN STAGES, IN THE ORDER "
          "THE AIR MEETS THEM", 5.4, INK, bold=True)
    d.txt(0, 63.4 * mm, "300 m3/h duty.  TWO IDENTICAL TRAINS, EACH ABLE TO "
          "CARRY THE WHOLE DUTY ALONE  -  true N+1, not 2 x 150.", 4.4, MID)
    d.txt(0, 32 * mm, "A DIFFERENTIAL-PRESSURE GAUGE ACROSS EVERY STAGE AND A "
          "FLOW METER ON THE TRAIN.", 4.4, ACCENT, bold=True)
    d.txt(0, 27.6 * mm, "They are the only way to know a filter is spent.  "
          "They turn a vendor's dirty-filter figure into a maintenance "
          "trigger.", 4.1, MID)
    d.txt(0, 21.0 * mm, "STAGE 5 IS THE ONLY STAGE WITH A FINITE, CONSUMABLE "
          "LIFE.", 4.4, RED, bold=True)
    d.txt(0, 16.6 * mm, "Its change-out interval needs a challenge "
          "concentration and vendor breakthrough data.  Neither exists  -  "
          "DATA REQUIRED  [N].", 4.1, MID)
    d.txt(0, 10.0 * mm, "FIVE OF THE EIGHT PRESSURE-LOSS COMPONENTS ARE "
          "VENDOR DATA.", 4.4, RED, bold=True)
    d.txt(0, 5.6 * mm, "Only 161 Pa  -  ductwork plus the 100 Pa plenum  -  "
          "is derivable.  The fan must be selected on the DIRTY figures.  A "
          "quoted total would be fabricated.", 4.1, MID)
    return d


def fig_hvac_schematic():
    """The whole air path -- intake, trains, distribution, cascade, exhaust."""
    d = Fig(W, 122 * mm)
    d.txt(0, 116 * mm, "THE AIR PATH  -  ONE WAY IN, ONE WAY OUT, AND A "
          "SEPARATE LOOP FOR THE GENERATOR", 5.4, INK, bold=True)

    # ---- intake
    d.txt(4 * mm, 108 * mm, "SH-1  FRESH-AIR SHAFT  600 x 600", 4.4, INK,
          bold=True)
    d.txt(4 * mm, 104 * mm, "gooseneck head at +1.500, 12.3 m from the "
          "intake to the entry against a >= 10 m rule", 4.0, MID)
    _box(d, 4 * mm, 84 * mm, 40 * mm, 15 * mm, "BV-1  /  BV-2",
         ["DN100 BLAST VALVES", "west wall of bay 1"], WARN, RED)
    _chain(d, 24 * mm, 103 * mm, 24 * mm, 99.6 * mm, ACCENT, 0.8)

    # ---- the raw-air run, which is the finding
    _chain(d, 44 * mm, 91.5 * mm, 62 * mm, 91.5 * mm, RED, 1.0)
    d.txt(53 * mm, 80.4 * mm, "RAW AIR  -  UNFILTERED", 4.2, RED, "middle",
          bold=True)
    d.txt(53 * mm, 76.4 * mm, "11.2 m through the", 4.0, RED, "middle")
    d.txt(53 * mm, 72.4 * mm, "clean zone", 4.0, RED, "middle")

    _box(d, 62 * mm, 84 * mm, 46 * mm, 15 * mm, "AHU-1  FILTER TRAIN  DUTY",
         ["bay 5  ·  300 m3/h  ·  full 7-stage set"], PLANT, ACCENT)
    _box(d, 62 * mm, 66 * mm, 46 * mm, 13 * mm, "AHU-2  STANDBY",
         ["identical  ·  carries the whole duty"], CONC2, MID)
    _chain(d, 85 * mm, 84 * mm, 85 * mm, 79.4 * mm, MID, 0.5)
    _box(d, 118 * mm, 84 * mm, 52 * mm, 15 * mm, "PLENUM  +50 to +100 Pa",
         ["the overpressure that sets every leak direction"], PLANT, ACCENT)
    _chain(d, 108 * mm, 91.5 * mm, 117.4 * mm, 91.5 * mm, ACCENT, 0.9,
           "300 m3/h")

    # ---- distribution
    d.line(144 * mm, 84 * mm, 144 * mm, 58 * mm, ACCENT, 0.8)
    d.line(8 * mm, 58 * mm, 144 * mm, 58 * mm, ACCENT, 0.8)
    rooms = [("U-01", "STORES / ESC 1", "30", "30"),
             ("U-02", "LAV + MEDICAL", "30", "30"),
             ("U-03", "OPS ROOM", "135", "45"),
             ("U-04", "BERTHING  9", "45", "135"),
             ("U-05", "CBRN PLANT", "60", "60")]
    bw, gap = 30 * mm, 3.5 * mm
    for i, (tag, nm, dayf, nightf) in enumerate(rooms):
        x = 4 * mm + i * (bw + gap)
        d.rect(x, 34 * mm, bw, 18 * mm, fill=AIR, c=ACCENT, sw=0.5)
        d.txt(x + bw / 2.0, 47.6 * mm, tag, 4.8, INK, "middle", bold=True)
        d.txt(x + bw / 2.0, 43.6 * mm, nm, 4.0, MID, "middle")
        d.txt(x + bw / 2.0, 38.4 * mm, "DAY " + dayf + "   NIGHT " + nightf,
              4.0, ACCENT, "middle", bold=True)
        d.txt(x + bw / 2.0, 35.0 * mm, "m3/h", 3.6, FAINT, "middle")
        d.arrow(x + bw / 2.0, 58 * mm, x + bw / 2.0, 52.4 * mm, ACCENT, 0.6,
                2.0)
    d.txt(4 * mm, 61.6 * mm, "VCD-1 / VCD-2 SWAP THE OPS AND BERTHING FLOWS  "
          "-  the occupied room of the pair always gets 135 m3/h = 15.0 "
          "m3/h per person", 4.1, ACCENT, bold=True)

    # ---- transfer to the airlock, then out
    d.line(19 * mm, 34 * mm, 19 * mm, 27 * mm, GREEN, 0.7)
    d.line(19 * mm, 27 * mm, 122 * mm, 27 * mm, GREEN, 0.7)
    for i in range(1, 5):
        x = 4 * mm + i * (bw + gap) + bw / 2.0
        d.line(x, 34 * mm, x, 27 * mm, GREEN, 0.5)
    _box(d, 122 * mm, 18 * mm, 48 * mm, 16 * mm, "U-06  DECON AIRLOCK",
         ["bay 6  ·  NOTHING IS SUPPLIED TO IT",
          "300 m3/h TRANSFER, three stages"], WARN, GREEN)
    d.arrow(122 * mm, 27 * mm, 121.4 * mm, 27 * mm, GREEN, 0.7)
    d.txt(70 * mm, 28.8 * mm, "TRANSFER AIR  -  the whole 300 m3/h, and it "
          "is what makes the cascade work", 4.1, GREEN, "middle", bold=True)
    d.arrow(146 * mm, 18 * mm, 146 * mm, 12 * mm, GREEN, 0.8)
    d.txt(148 * mm, 13.6 * mm, "BV-3  in W6", 4.2, GREEN, bold=True)
    d.txt(148 * mm, 9.6 * mm, "DN100, (14998, 4900)", 3.9, MID)

    # ---- the generator loop, deliberately drawn apart
    d.line(0, 5.6 * mm, W, 5.6 * mm, RULE, 0.4, dash=[2, 2])
    _box(d, 4 * mm, 12 * mm, 52 * mm, 12 * mm, "SH-2  GENERATOR AIR SHAFT",
         ["600 x 600, X 22598-23198"], CONC2, MID)
    _box(d, 62 * mm, 12 * mm, 34 * mm, 12 * mm, "BV-4  /  BV-5",
         ["DN350 blast valves"], WARN, RED)
    _box(d, 102 * mm, 12 * mm, 16 * mm, 12 * mm, "GEN-1", ["15 kVA"],
         CONC2, MID)
    _chain(d, 56 * mm, 18 * mm, 61.4 * mm, 18 * mm, MID, 0.8)
    _chain(d, 96 * mm, 18 * mm, 101.4 * mm, 18 * mm, MID, 0.8, "2 600 m3/h")
    d.txt(4 * mm, 1.4 * mm, "THE GENERATOR LOOP DOES NOT TOUCH THE GAS-TIGHT "
          "ENVELOPE.  Bay 8 is outside it, behind blast door 2 and W7, so "
          "running the set neither depressurises the clean zone nor spends "
          "carbon-bed life.", 4.0, MID)
    return d


def fig_cascade():
    """The overpressure cascade, and the airlock stages it maps onto."""
    d = Fig(W, 78 * mm)
    d.txt(0, 72 * mm, "THE OVERPRESSURE CASCADE  -  0 to +50 Pa IN FOUR "
          "STEPS, AND WHY THE AIRLOCK HAS THREE STAGES", 5.4, INK, bold=True)
    steps = [("OUTSIDE", "stair shaft, bay 7", 0, CONC2),
             ("STAGE 1", "airlock, dirty end", 10, WARN),
             ("STAGE 2", "airlock, middle", 20, WARN),
             ("STAGE 3", "airlock, clean end", 35, PLANT),
             ("CLEAN ZONE", "bays 1 to 5", 50, AIR)]
    bw, gap = 31 * mm, 4.2 * mm
    base = 20 * mm
    for i, (tag, nm, pa, col) in enumerate(steps):
        x = i * (bw + gap)
        h = 6 * mm + pa * 0.62 * mm
        d.rect(x, base, bw, h, fill=col, c=ACCENT, sw=0.6)
        d.txt(x + bw / 2.0, base + h + 4.4, "+" + str(pa) + " Pa" if pa
              else "0 Pa (atmospheric)", 5.0, ACCENT, "middle", bold=True)
        d.txt(x + bw / 2.0, base - 4.6, tag, 4.4, INK, "middle", bold=True)
        d.txt(x + bw / 2.0, base - 8.8, nm, 4.0, MID, "middle")
        if i:
            xa = x - gap + 0.8
            d.arrow(x - 0.8, base + 3.0 * mm, xa, base + 3.0 * mm, GREEN,
                    0.9, 2.2)
    d.txt(W / 2.0, base + 46 * mm, "AIR MOVES THIS WAY  -  from clean to "
          "dirty, always", 4.4, GREEN, "middle", bold=True)
    d.arrow(W / 2.0 + 44 * mm, base + 43.4 * mm, W / 2.0 - 44 * mm,
            base + 43.4 * mm, GREEN, 0.9)
    d.txt(0, 7.0 * mm, "THE CASCADE MAPS EXACTLY ONTO THE THREE AIRLOCK "
          "STAGES.", 4.4, ACCENT, bold=True)
    d.txt(0, 2.6 * mm, "The cascade values are confirmed; the mapping onto "
          "the stages is a reconstruction  [R]  -  the issued sheet does not "
          "state it.  Purge: 5 air changes of stage 1 = 12.8 min, so 4 to 5 "
          "persons an hour.", 4.0, MID)
    return d


# ===========================================================================
#  6  WATER, SEWAGE AND DRAINAGE
# ===========================================================================

def fig_drainage_schematic():
    """Three hydraulic zones, and where each one is allowed to go."""
    d = Fig(W, 128 * mm)
    d.txt(0, 122 * mm, "THE THREE HYDRAULIC ZONES  -  AND THE ONE THAT HAS "
          "NOWHERE TO GO", 5.4, INK, bold=True)
    d.txt(0, 117.4 * mm, "Water inside a sealed box is a protective problem "
          "before it is a plumbing problem:  every route out is a route in.",
          4.2, MID)

    # ---------------- Z1 CLEAN
    d.rect(0, 74 * mm, W, 38 * mm, fill=None, c=ACCENT, sw=0.5,
           dash=[3, 2])
    d.txt(3 * mm, 107 * mm, "ZONE Z1  -  CLEAN   bays 1 to 5, INSIDE the "
          "gas-tight envelope", 4.8, ACCENT, bold=True)
    _box(d, 3 * mm, 88 * mm, 40 * mm, 15 * mm, "STRUCTURAL SEEPAGE",
         ["0.5 L/m2/day x 401 m2", "= 200 L/day"], AIR, ACCENT)
    _box(d, 3 * mm, 76 * mm, 40 * mm, 10 * mm, "CONDENSATE + WASHDOWN",
         ["200 L/day"], AIR, ACCENT)
    _box(d, 56 * mm, 79 * mm, 44 * mm, 24 * mm, "SU-01  CLEAN SUMP",
         ["1500 x 1500 x 1500 = 3.375 m3", "invert (-)7.600, base (-)8.000",
          "= 8 DAYS OF STORE"], WATER, ACCENT)
    _chain(d, 43 * mm, 95.5 * mm, 55.4 * mm, 93 * mm, ACCENT, 0.8)
    _chain(d, 43 * mm, 81 * mm, 55.4 * mm, 87 * mm, ACCENT, 0.8)
    _box(d, 112 * mm, 90 * mm, 28 * mm, 13 * mm, "PU-01 duty",
         ["1.5 L/s"], PLANT, ACCENT)
    _box(d, 112 * mm, 76 * mm, 28 * mm, 13 * mm, "PU-02 standby",
         ["1.5 L/s, auto-alt."], CONC2, MID)
    _chain(d, 100 * mm, 96 * mm, 111.4 * mm, 96 * mm, ACCENT, 0.8)
    _chain(d, 100 * mm, 85 * mm, 111.4 * mm, 82 * mm, MID, 0.6)
    _box(d, 148 * mm, 83 * mm, 24 * mm, 13 * mm, "SK-02", ["storm", "soakaway"],
         SOIL, GREEN)
    _chain(d, 140 * mm, 96 * mm, 147.4 * mm, 90 * mm, ACCENT, 0.8)
    d.txt(3 * mm, 70.6 * mm, "PU-03  HAND PUMP  -  the third line, and the "
          "only one that does not need power.  Duty ratio of PU-01/02 is "
          "0.31 %:  one start every 3.4 days.", 4.1, RED, bold=True)
    d.txt(3 * mm, 66.6 * mm, "A failed standby would never be discovered by "
          "use, so a WITNESSED MONTHLY TEST of the standby path and the hand "
          "pump is a maintenance requirement, not an option.", 4.0, MID)

    # ---------------- Z2 DECON
    d.rect(0, 36 * mm, W, 26 * mm, fill=None, c=RED, sw=0.5, dash=[3, 2])
    d.txt(3 * mm, 57 * mm, "ZONE Z2  -  DECON   bay 6, inside the envelope "
          "but DIRTY", 4.8, RED, bold=True)
    _box(d, 3 * mm, 39 * mm, 44 * mm, 14 * mm, "DECON EFFLUENT",
         ["airlock stages 1 and 2", "on use"], WARN, RED)
    _box(d, 60 * mm, 39 * mm, 44 * mm, 14 * mm, "TK-01  1 000 L TANK",
         ["DRAWN IN BAY 8  -  across", "the gas-tight boundary"], WARN, RED)
    _chain(d, 47 * mm, 46 * mm, 59.4 * mm, 46 * mm, RED, 0.9)
    _box(d, 118 * mm, 39 * mm, 40 * mm, 14 * mm, "TANKER  -  OFF SITE",
         ["NEVER to the clean sump"], CONC2, RED)
    _chain(d, 104 * mm, 46 * mm, 117.4 * mm, 46 * mm, RED, 0.9)
    d.txt(3 * mm, 32.4 * mm, "THE ROUTE FROM BAY 6 TO A TANK IN BAY 8 CROSSES "
          "THE GAS-TIGHT BOUNDARY, AND NO ROUTE IS DEFINED  [U].  The "
          "emptying route is not defined either.", 4.1, RED, bold=True)

    # ---------------- Z3 GREY
    d.rect(0, 8 * mm, W, 20 * mm, fill=None, c=MID, sw=0.5, dash=[3, 2])
    d.txt(3 * mm, 23.4 * mm, "ZONE Z3  -  GREY   bays 7 and 8, OUTSIDE the "
          "gas-tight envelope", 4.8, MID, bold=True)
    _box(d, 3 * mm, 10 * mm, 52 * mm, 11 * mm, "GENERATOR BAY, STAIR SHAFT",
         ["spillage, washdown, tracked-in water"], CONC2, MID)
    d.txt(62 * mm, 16.4 * mm, "NO DESTINATION IS RECORDED ANYWHERE IN THE "
          "PROJECT  -  [N], DATA REQUIRED.", 4.6, RED, bold=True)
    d.txt(62 * mm, 12.0 * mm, "Zone 3 is not a small omission:  bay 8 holds "
          "the generator, its fuel and the main board.", 4.0, MID)
    d.txt(0, 2.6 * mm, "Separately:  the stairwell sump SU-02 (1.0 m3) with "
          "PU-04 / PU-05 at 2 L/s takes the approach and stairwell surface "
          "water to SK-03.  32 h to fill at the worst door-open driving-rain "
          "rate.", 4.0, MID)
    return d


def fig_sump_detail():
    """The clean sump -- a pit cast into the mat, and a hole in the tanking."""
    d = Fig(W, 118 * mm)
    v = V(34, 52 * mm, 98 * mm)
    d.txt(0, 112 * mm, "SU-01  CLEAN SUMP  -  A PIT IN THE MAT, AND "
          "THEREFORE A PENETRATION OF THE TANKING   1 : 34", 5.4, INK,
          bold=True)

    d.rect(v.x(-1400), v.y(-1900), v.d(4300), v.d(1900), fill=ROCK, c=None,
           sw=0)
    d.hatch(v.x(-1400), v.y(-1900), v.d(4300), v.d(1900), 45, 4.0,
            colors.Color(0.66, 0.68, 0.66), 0.2)
    d.rect(v.x(-1400), v.y(-600), v.d(4300), v.d(600), fill=CONC, c=INK,
           sw=0.8)
    d.rect(v.x(0), v.y(-1900), v.d(2300), v.d(1300), fill=CONC, c=INK, sw=0.8)
    d.rect(v.x(400), v.y(-1500), v.d(1500), v.d(1500), fill=colors.white,
           c=ACCENT, sw=0.7)
    d.rect(v.x(400), v.y(-1500), v.d(1500), v.d(900), fill=WATER, c=None,
           sw=0)
    d.pline([v.x(-1400), v.y(-620), v.x(-20), v.y(-620), v.x(-20),
             v.y(-1920), v.x(2320), v.y(-1920), v.x(2320), v.y(-620),
             v.x(2900), v.y(-620)], RED, 1.2)
    d.txt(v.x(2400), v.y(-380), "WP-01 TANKING", 4.2, RED)
    d.txt(v.x(2400), v.y(-680), "DRESSED AROUND THE PIT", 4.0, RED)
    d.txt(v.x(2400), v.y(-980), "no joint below the water", 4.0, MID)

    for lv, lab in ((0, "(-)6.100"), (-600, "(-)6.700")):
        d.level(v.x(-1360), v.y(lv), lab, 4.2, ACCENT, side=1)
    for lv, lab in ((-1500, "(-)7.600  invert"), (-1900, "(-)8.000  base")):
        d.line(v.x(2320), v.y(lv), v.x(2600), v.y(lv), ACCENT, 0.3,
               dash=[2, 1.5])
        d.txt(v.x(2640), v.y(lv) + 0.8, lab, 4.0, ACCENT)

    for lev, lab, col in ((-600, "HIGH ALARM  +1 200", RED),
                          (-900, "START  +900", ACCENT),
                          (-1200, "STOP  +300", GREEN)):
        d.line(v.x(420), v.y(lev), v.x(1880), v.y(lev), col, 0.5,
               dash=[2, 1.6])
        d.txt(v.x(1180), v.y(lev) + 1.4, lab, 4.0, col, "middle")
    for cx, tag in ((760, "PU-01"), (1540, "PU-02")):
        d.rect(v.x(cx - 130), v.y(-1460), v.d(260), v.d(300), fill=CONC2,
               c=INK, sw=0.5)
        d.txt(v.x(cx), v.y(-1760), tag, 4.0, INK, "middle", bold=True)
    d.dimh(v.x(400), v.x(1900), v.y(-2120), "1 500 internal", 4.4, INK)
    d.dimh(v.x(0), v.x(2300), v.y(-2460), "2 300 overall  -  400 walls, "
           "400 base", 4.4, MID)

    d.txt(0, 19.0 * mm, "CAST MONOLITHIC WITH THE MAT IN THE SAME CONTINUOUS "
          "POUR.  T16 @ 150 each face each way, 4-T20 trimmers each face "
          "and side.", 4.3, ACCENT, bold=True)
    d.txt(0, 14.6 * mm, "Wall and base thickness 300 / 400 was an open item;  "
          "400 is held.  A construction joint here would be a joint "
          "permanently below the water table.", 4.1, MID)
    d.txt(0, 8.6 * mm, "3 375 L OF STORE AGAINST 400 L/day  =  EIGHT DAYS "
          "WITH NO POWER AT ALL.", 4.3, GREEN, bold=True)
    d.txt(0, 4.2 * mm, "That store, the hand pump PU-03 and the 48-hour "
          "closed-mode limit are the three numbers a drill card needs.",
          4.1, MID)
    return d


def fig_septic_soakpit():
    """Foul drainage -- septic tank to IS 2470, and the soak pit."""
    d = Fig(W, 140 * mm)
    d.txt(0, 134 * mm, "FOUL DRAINAGE  -  SEPTIC TANK AND SOAK PIT TO "
          "IS 2470", 5.4, INK, bold=True)
    d.para(0, 129.4 * mm, "10 users at 45 lpcd = 450 L/day.  The tank is "
           "sized for the PEACETIME duty:  the shelter is not occupied "
           "continuously, and the sheltered case belongs to the airlock, "
           "not to the lavatory.", 4.2, MID)

    # ---------------- septic tank, section at 1 : 40
    v = V(40, 22 * mm, 66 * mm)
    d.txt(4 * mm, 122 * mm, "ST-01  SEPTIC TANK   1 : 40", 4.8, INK,
          bold=True)
    d.rect(v.x(0), v.y(0), v.d(1500), v.d(1300), fill=CONC, c=INK, sw=0.9)
    d.rect(v.x(120), v.y(120), v.d(1260), v.d(1060), fill=colors.white,
           c=MID, sw=0.4)
    d.rect(v.x(120), v.y(120), v.d(1260), v.d(1000), fill=WATER, c=None, sw=0)
    d.rect(v.x(960), v.y(120), v.d(90), v.d(820), fill=CONC, c=INK, sw=0.5)
    d.txt(v.x(1005), v.y(1000), "BAFFLE AT 2/3 L", 3.8, INK, "middle")
    d.pline([v.x(-350), v.y(1020), v.x(60), v.y(1020), v.x(60), v.y(760)],
            GREEN, 1.1)
    d.pline([v.x(1440), v.y(940), v.x(1440), v.y(700)], GREEN, 1.1)
    d.line(v.x(1440), v.y(940), v.x(1820), v.y(940), GREEN, 1.1)
    d.txt(v.x(-350), v.y(1420), "INLET TEE", 4.0, GREEN)
    d.txt(v.x(1120), v.y(1420), "OUTLET TEE", 4.0, GREEN)
    d.line(v.x(500), v.y(1300), v.x(500), v.y(2100), MID, 0.8)
    d.line(v.x(500), v.y(2100), v.x(620), v.y(2160), MID, 0.8)
    d.txt(v.x(680), v.y(2080), "50 COWLED VENT", 4.0, MID)
    d.txt(v.x(680), v.y(1800), ">= 2 m ABOVE GRADE", 4.0, MID)
    d.line(v.x(120), v.y(1120), v.x(1380), v.y(1120), BLUE, 0.5)
    d.txt(v.x(150), v.y(1170), "300 FREEBOARD", 3.8, BLUE)
    d.dimh(v.x(0), v.x(1500), v.y(-320), "1 500 long", 4.3, INK)
    d.dimv(v.y(0), v.y(1300), v.x(-150), "1 300 deep", 4.2)
    d.txt(v.x(750), v.y(-800), "1.50 x 0.75 x 1.00 liquid  =  1 125 L",
          4.6, INK, "middle", bold=True)
    d.txt(v.x(750), v.y(-1180), "1 050 L required by IS 2470 (Pt 1) "
          "Table 1  -  PASS", 4.2, GREEN, "middle", bold=True)
    d.txt(v.x(750), v.y(-1560), "two compartments  ·  inlet and outlet "
          "tees  ·  300 freeboard", 4.0, MID, "middle")

    # ---------------- soak pit, section at 1 : 55
    v2 = V(55, 130 * mm, 112 * mm)
    d.txt(100 * mm, 122 * mm, "SK-01 / SK-02  SOAK PIT   1 : 55", 4.8, INK,
          bold=True)
    d.rect(v2.x(-1600), v2.y(0), v2.d(3200), v2.d(400), fill=SOIL, c=None,
           sw=0)
    d.rect(v2.x(-1600), v2.y(-3600), v2.d(3200), v2.d(3600), fill=ROCK,
           c=None, sw=0)
    d.hatch(v2.x(-1600), v2.y(-3600), v2.d(3200), v2.d(3600), 45, 4.2,
            colors.Color(0.66, 0.68, 0.66), 0.2)
    d.rect(v2.x(-1100), v2.y(-3500), v2.d(2200), v2.d(3500), fill=RUB,
           c=INK, sw=0.7)
    d.rect(v2.x(-1100), v2.y(-300), v2.d(2200), v2.d(300), fill=SOIL, c=MID,
           sw=0.4)
    d.txt(v2.x(0), v2.y(-215), "300 SAND", 3.8, MID, "middle")
    d.rect(v2.x(-1300), v2.y(0), v2.d(2600), v2.d(150), fill=CONC, c=INK,
           sw=0.7)
    d.txt(v2.x(-1280), v2.y(260), "RC COVER SLAB", 4.0, INK)
    d.txt(v2.x(0), v2.y(-1500), "40-80 mm BRICKBAT", 4.0, INK, "middle")
    d.txt(v2.x(0), v2.y(-1900), "OR STONE FILL", 4.0, INK, "middle")
    d.line(v2.x(-1600), v2.y(-2000), v2.x(1600), v2.y(-2000), BLUE, 0.7,
           dash=[3, 2])
    d.txt(v2.x(160), v2.y(-2300), "DESIGN GWT  (-)2.000", 4.0, BLUE)
    d.dimv(v2.y(-3500), v2.y(0), v2.x(-1400), "3 500 effective", 4.2)
    d.dimh(v2.x(-1100), v2.x(1100), v2.y(-3900), "2 200 dia", 4.3, INK)
    d.txt(v2.x(0), v2.y(-4400), "side area 24.19 m2  -  the base is assumed "
          "blinded by silt", 4.2, INK, "middle", bold=True)

    y = d.note(0, 22 * mm, "WIDENED FROM 2.000 TO 2.200 DIAMETER, NOT "
               "DEEPENED.",
               "Deepening would drive the pit below the design groundwater "
               "table at (-)2.000, where a soak pit cannot soak.  Widening "
               "also keeps SK-01 and SK-02 one detail, one cover slab and "
               "one set of spare materials.")
    y = d.note(0, y - 5.0 * mm, "THE 20 L/m2/day ABSORPTION RATE IS ASSUMED "
               " [A], AND A PERCOLATION TEST TO IS 2470 (Pt 2) Cl. 4 IS "
               "MANDATORY.",
               "It, not this calculation, sets the final size.  SK-01 is "
               "2.3 % short of its own stated requirement  -  21.99 m2 "
               "against 22.5 m2  -  and that is recorded, not resized:  the "
               "test may move the requirement by far more than 2.3 %.",
               hc=RED)
    return d


def fig_water_balance():
    """Every litre in and every litre out, per day."""
    d = Fig(W, 88 * mm)
    d.txt(0, 82 * mm, "THE DAILY WATER BALANCE  -  WHAT ARRIVES, WHERE IT IS "
          "HELD, AND WHERE IT IS ALLOWED TO GO", 5.4, INK, bold=True)
    rows = [("STRUCTURAL SEEPAGE", "0.5 L/m2/day x 401 m2", "200 L/day",
             "CLEAN SUMP SU-01  3 375 L", "STORM SOAKAWAY SK-02", ACCENT),
            ("CONDENSATE + WASHDOWN", "DH-1 through a 75 deep-seal trap",
             "200 L/day", "CLEAN SUMP SU-01  3 375 L",
             "STORM SOAKAWAY SK-02", ACCENT),
            ("FOUL, PEACETIME", "10 users x 45 lpcd", "450 L/day",
             "SEPTIC TANK ST-01  1 125 L", "FOUL SOAK PIT SK-01", GREEN),
            ("DECON EFFLUENT", "airlock stages 1 and 2", "on use",
             "TK-01  1 000 L", "TANKER ONLY  -  OFF SITE", RED),
            ("STAIRWELL SURFACE WATER", "approach and stairwell",
             "0.10 L/s", "SU-02  1 000 L", "SK-03  -  NOT SIZED  [N]", MID)]
    y = 68 * mm
    colx = (0, 46 * mm, 78 * mm, 100 * mm, 140 * mm)
    hdr = ("SOURCE", "BASIS", "RATE", "HELD IN", "DISCHARGES TO")
    for i, h in enumerate(hdr):
        d.txt(colx[i], y + 5.0, h, 4.2, MID, bold=True)
    d.line(0, y + 2.6, W, y + 2.6, RULE, 0.5)
    for k, (src, bas, rate, hold, dest, col) in enumerate(rows):
        yy = y - 3.0 - k * 11.0
        d.txt(colx[0], yy, src, 4.4, col, bold=True)
        d.txt(colx[1], yy, bas, 4.0, MID)
        d.txt(colx[2], yy, rate, 4.4, INK, bold=True)
        d.txt(colx[3], yy, hold, 4.0, INK)
        d.txt(colx[4], yy, dest, 4.0, col)
        d.line(0, yy - 4.2, W, yy - 4.2, RULE, 0.25)
    d.txt(0, 14.6 * mm, "400 L/day INTO A 3 375 L SUMP  =  8 DAYS.  That is "
          "the number that matters:  it is longer than the 48-hour "
          "closed-mode limit set by the soda lime, by a factor of four.",
          4.3, GREEN, bold=True)
    d.txt(0, 9.6 * mm, "THE SEEPAGE RATE 0.5 L/m2/day IS A DESIGN ALLOWANCE "
          "FOR AN INTACT TANKED STRUCTURE.  It is not a measured figure and "
          "it is not a leak allowance for a defective one.", 4.2, RED,
          bold=True)
    d.txt(0, 4.4 * mm, "Groundwater does not stop because the shelter is "
          "sealed.  The clean sump pump stays on the essential board through "
          "closed mode, and the hand pump covers the battery failing.", 4.1,
          MID)
    return d


# ===========================================================================
#  7  EMP PROTECTION, ELECTRICAL AND FIRE
# ===========================================================================

def fig_emp_zones():
    """The three EMP zones, and what each one is actually worth."""
    d = Fig(W, 108 * mm)
    d.txt(0, 102 * mm, "THE THREE EMP ZONES  -  AND THE ONE THAT CARRIES "
          "THE REQUIREMENT", 5.4, INK, bold=True)
    d.txt(0, 97.4 * mm, "MIL-STD-188-125-1 asks for 80 dB from 10 kHz to "
          "1 GHz.  Only one of these three zones delivers it.", 4.2, MID)

    v = V(190, 8 * mm, 32 * mm)
    bx, by, bX, bY = GEOM["box"]

    # zone 0 -- everything above grade
    d.rect(0, 78 * mm, W, 14 * mm, fill=CONC2, c=MID, sw=0.5, dash=[3, 2])
    d.txt(3 * mm, 87.4 * mm, "EMP ZONE 0   everything above grade", 4.8, MID,
          bold=True)
    d.txt(3 * mm, 83.0 * mm, "sentry post +7.000  ·  headhouse +0.900 with "
          "no earth cover  ·  covered stairwell +2.450, expendable  ·  ESC "
          "heads  ·  burster slab", 4.0, MID)
    d.txt(150 * mm, 87.4 * mm, "0 dB", 6.0, RED, "middle", bold=True)
    d.txt(150 * mm, 82.6 * mm, "NOTHING CREDITED", 3.9, RED, "middle")

    # zone 1 -- the buried box, drawn in plan
    d.rect(0, 20 * mm, W, 54 * mm, fill=None, c=ACCENT, sw=0.5, dash=[3, 2])
    d.txt(3 * mm, 69.4 * mm, "EMP ZONE 1   the buried box, all eight bays  "
          "-  THE REINFORCEMENT CAGE IS THE SHIELD", 4.8, ACCENT, bold=True)
    d.rect(v.x(bx), v.y(by), v.d(bX - bx), v.d(bY - by), fill=CONC, c=INK,
           sw=0.7)
    d.rect(v.x(600), v.y(600), v.d(20800), v.d(5000), fill=AIR, c=MID,
           sw=0.35)
    for x0, x1 in GEOM["w8"] + [GEOM["w5"], GEOM["w6"], GEOM["w7"]]:
        d.rect(v.x(x0), v.y(600), v.d(x1 - x0), v.d(5000), fill=CONC, c=MID,
               sw=0.3)
    # the cage, indicated
    for k in range(1, 22):
        xx = k * 1000
        d.line(v.x(xx), v.y(0), v.x(xx), v.y(6200), RED, 0.18)
    for k in range(1, 7):
        yy = k * 900
        d.line(v.x(0), v.y(yy), v.x(22000), v.y(yy), RED, 0.18)
    d.txt(v.x(11000), v.y(3100) - 1.0, "600 WALLS  ·  900 ROOF  ·  600 MAT  "
          "·  W6 / W7 400", 4.4, INK, "middle", bold=True)
    # zone 2, marked in bay 3
    d.rect(v.x(5820), v.y(3700), v.d(2400), v.d(1600), fill=GOLD, c=INK,
           sw=0.7)
    d.txt(v.x(7020), v.y(4300) - 1.0, "ZONE 2", 4.2, colors.white, "middle",
          bold=True)
    d.para(3 * mm, 25.0 * mm, "Reinforcement at 150 in both curtains, "
           "cast-in frames welded to the cage, and a welded EMP strap at "
           "every construction joint.  Mesh shielding falls at 20 dB per "
           "decade, which is a property of any mesh and not of this one.",
           4.0, MID, width=W - 46 * mm)
    d.txt(150 * mm, 62.0 * mm, "80 dB ONLY", 5.4, RED, "middle", bold=True)
    d.txt(150 * mm, 57.4 * mm, "BELOW 99.9 kHz", 4.4, RED, "middle",
          bold=True)
    d.txt(150 * mm, 53.0 * mm, "1 decade of the 5", 3.9, RED, "middle")
    d.txt(150 * mm, 48.0 * mm, "CANNOT BE SURVEYED", 3.9, MID, "middle")
    d.txt(150 * mm, 44.0 * mm, "buried under 2 m of cover", 3.6, MID,
          "middle")

    # zone 2
    d.rect(0, 2 * mm, W, 16 * mm, fill=None, c=GOLD, sw=0.6, dash=[3, 2])
    d.txt(3 * mm, 13.4 * mm, "EMP ZONE 2   welded steel enclosure in bay 3, "
          "inside finish W-04", 4.8, GOLD, bold=True)
    d.txt(3 * mm, 9.0 * mm, "external 2 400 x 1 600 x 2 200  ·  panel 50  ·  "
          "internal 2 300 x 1 500 x 2 100  ·  solid welded steel, no "
          "aperture above the honeycomb cutoff", 4.0, MID)
    d.txt(3 * mm, 4.6 * mm, "IEEE Std 299 FULL SURVEY IS A HOLD POINT BEFORE "
          "ANY EQUIPMENT IS INSTALLED.  Every dimension of it is assumed  "
          "[A];  only the requirement is confirmed.", 4.0, ACCENT, bold=True)
    d.txt(150 * mm, 13.4 * mm, "80 dB", 6.0, GREEN, "middle", bold=True)
    d.txt(150 * mm, 8.4 * mm, "10 kHz - 1 GHz", 4.2, GREEN, "middle",
          bold=True)
    d.txt(150 * mm, 4.4 * mm, "STANDING ALONE", 3.9, GREEN, "middle")
    return d


def fig_emp_se():
    """Shielding effectiveness of the cage against the requirement."""
    d = Fig(W, 92 * mm)
    d.txt(0, 86 * mm, "SHIELDING EFFECTIVENESS OF THE REINFORCEMENT CAGE  -  "
          "20 dB PER DECADE AGAINST A FLAT 80 dB REQUIREMENT", 5.4, INK,
          bold=True)
    a = Axes(d, 22 * mm, 22 * mm, 122 * mm, 54 * mm, (1e4, 1e9), (-10, 110),
             xlog=True)
    a.grid(xs=(1e4, 1e5, 1e6, 1e7, 1e8, 1e9),
           ys=(0, 20, 40, 60, 80, 100))
    a.xticks([1e4, 1e5, 1e6, 1e7, 1e8, 1e9],
             ["10 kHz", "100 kHz", "1 MHz", "10 MHz", "100 MHz", "1 GHz"])
    a.yticks([0, 20, 40, 60, 80, 100])
    a.xlabel("frequency")
    a.ylabel("shielding effectiveness  dB")

    # SE = 20 log10(lambda / 2s), s = 150 mm
    pts = []
    f = 1e4
    while f <= 1e9 + 1:
        lam = 2.99792458e8 / f
        se = 20 * math.log10(lam / (2 * 0.150))
        pts.append((f, max(se, -10)))
        f *= 1.15
    a.curve(pts, ACCENT, 1.2)
    a.curve([(1e4, 80), (1e9, 80)], RED, 1.0, dash=[3, 2])
    d.txt(a.X(3e7), a.Y(84), "REQUIREMENT  80 dB", 4.4, RED, "middle",
          bold=True)
    d.txt(a.X(1.4e4), a.Y(96), "SE = 20 log10( lambda / 2s ),  s = 150 mm",
          4.4, ACCENT, bold=True)

    # the crossing
    d.circ(a.X(99.93e3), a.Y(80), 2.2, fill=None, c=RED, sw=0.9)
    d.line(a.X(99.93e3), a.Y(80), a.X(99.93e3), a.Y(-10), RED, 0.4,
           dash=[2, 2])
    d.txt(a.X(1.4e5), a.Y(64), "IT CROSSES AT 99.93 kHz", 4.6, RED,
          bold=True)
    d.txt(a.X(1.4e5), a.Y(55), "and reaches 0 dB at 999.31 MHz  -  where the "
          "half-spacing", 4.1, MID)
    d.txt(a.X(1.4e5), a.Y(47), "equals a half wavelength and the cage stops "
          "being a shield", 4.1, MID)

    d.txt(0, 10.6 * mm, "THE CAGE MEETS 80 dB OVER ONE DECADE OF THE FIVE "
          "THE STANDARD ASKS FOR.  IT IS NOT A SUBSTITUTE FOR ZONE 2.", 4.4,
          RED, bold=True)
    d.txt(0, 6.0 * mm, "This is a property of any mesh:  a 150 mm cage "
          "cannot do better, and closing the grid to reach 1 GHz would need "
          "a spacing of about 0.15 mm  -  a sheet, not a cage.", 4.1, MID)
    d.txt(0, 1.4 * mm, "It also cannot be surveyed.  The exterior is under "
          "two metres of engineered cover, so the figure above is a "
          "calculation and stays one.", 4.1, MID)
    return d


def fig_penetrations():
    """Every hole through the EMP boundary, and whether it passes."""
    d = Fig(W, 116 * mm)
    d.txt(0, 110 * mm, "EVERY PENETRATION OF THE PROTECTIVE BOUNDARY  -  AND "
          "WHETHER THE HOLE IS ITS OWN WAVEGUIDE", 5.4, INK, bold=True)
    d.txt(0, 105.4 * mm, "A bore through a conducting wall attenuates below "
          "its cutoff:  f_c = 1.8412 c / (pi d) for the TE11 mode, and about "
          "32 L/d dB of attenuation beyond it.", 4.2, MID)

    rows = [("BV-1 / BV-2", "blast valve, W1, bay 1", "100 dia", "600",
             "steel", "1 757", "192", "PASS", GREEN),
            ("BV-3", "blast valve, W6 at (14998, 4900)", "100 dia", "400",
             "steel", "1 757", "128", "PASS", GREEN),
            ("BV-4 / BV-5", "blast valve, east wall, bay 8", "350 dia",
             "600", "steel", "502", "55", "FAIL", RED),
            ("SEP", "service entry plate, north wall", "800 wide", "600",
             "steel", "187", "20", "FAIL", RED),
            ("PD-05", "rising main through the SEP", "50 dia", "600",
             "steel", "3 514", "384", "PASS", GREEN),
            ("ESC 1", "escape shaft, bay 1", "1 400 dia", "3 050",
             "CONCRETE", "126", "-", "FAIL", RED),
            ("ESC 2", "escape shaft, bay 8", "1 400 dia", "3 600",
             "CONCRETE", "126", "-", "FAIL", RED),
            ("VOID", "stair void through the roof, bay 7", "3 160 wide",
             "900", "CONCRETE", "47", "-", "FAIL", RED)]
    colx = (0, 24 * mm, 76 * mm, 96 * mm, 112 * mm, 132 * mm, 152 * mm,
            166 * mm)
    hdr = ("TAG", "WHAT AND WHERE", "BORE", "DEPTH", "BOUNDED BY",
           "CUTOFF MHz", "WBC dB", "")
    y = 96 * mm
    for i, h in enumerate(hdr):
        d.txt(colx[i], y, h, 4.0, MID, bold=True)
    d.line(0, y - 2.4, W, y - 2.4, RULE, 0.5)
    for k, r in enumerate(rows):
        yy = y - 7.0 - k * 6.6
        col = r[8]
        d.txt(colx[0], yy, r[0], 4.3, INK, bold=True)
        d.txt(colx[1], yy, r[1], 4.1, MID)
        d.txt(colx[2], yy, r[2], 4.1, INK)
        d.txt(colx[3], yy, r[3], 4.1, INK)
        d.txt(colx[4], yy, r[4], 4.1, RED if r[4] == "CONCRETE" else MID)
        d.txt(colx[5], yy, r[5], 4.1, INK)
        d.txt(colx[6], yy, r[6], 4.1, INK)
        d.txt(colx[7], yy, r[7], 4.3, col, bold=True)
        d.line(0, yy - 2.6, W, yy - 2.6, RULE, 0.2)

    d.txt(0, 38.0 * mm, "A CONCRETE BORE IS NOT A WAVEGUIDE.", 4.6, RED,
          bold=True)
    d.txt(0, 33.4 * mm, "The waveguide-below-cutoff formula needs conducting "
          "walls.  The two escape shafts and the stair void are concrete, so "
          "the cutoff column is what the bore WOULD give if it were "
          "metallic;  the real figure is the plain aperture value, about "
          "41 dB and 34 dB at 1 MHz.", 4.1, MID)
    d.txt(0, 26.4 * mm, "THE STAIR VOID IS THE FINDING.", 4.6, RED,
          bold=True)
    d.txt(0, 21.8 * mm, "It is 3.16 m wide through a 900 slab, it is the "
          "entry route, and NO TREATMENT FOR IT EXISTS OR IS PROPOSED "
          "ANYWHERE IN THE PROJECT.  A bonded conducting hatch works at the "
          "escape shafts;  nothing equivalent is specified here.", 4.1, MID)
    d.txt(0, 14.2 * mm, "AND THE GENERATOR VALVES REOPEN AFTER THE SHOCK.",
          4.6, RED, bold=True)
    d.txt(0, 9.6 * mm, "BV-4 and BV-5 are ruled to reopen for generator "
          "operation, which leaves two DN350 bores open through the "
          "post-attack period  -  the two bores that already fail both "
          "criteria.  That sharpens the open question of whether bay 8 is "
          "inside the EMP boundary at all.", 4.1, MID)
    d.txt(0, 2.8 * mm, "The service entry plate is treated as the shield "
          "itself:  solid, welded, bonded 360 degrees to its cast-in frame, "
          "with each sleeve through it treated one by one.", 4.1, MID)
    return d


def fig_single_line():
    """Three boards, one cable entry, and what survives losing both sources."""
    d = Fig(W, 118 * mm)
    d.txt(0, 112 * mm, "ELECTRICAL SINGLE LINE  -  THREE BOARDS, ONE CABLE "
          "ENTRY, AND WHAT STAYS LIVE WITH NOTHING RUNNING", 5.4, INK,
          bold=True)

    _box(d, 4 * mm, 94 * mm, 40 * mm, 12 * mm, "MAINS", ["meter panel"],
         CONC2, MID)
    _box(d, 52 * mm, 94 * mm, 40 * mm, 12 * mm, "GEN-1   15 kVA",
         ["bay 8, the grey zone"], CONC2, MID)
    _box(d, 4 * mm, 76 * mm, 88 * mm, 13 * mm, "DB-M   MAIN LV BOARD",
         ["bay 8  ·  changeover  ·  OUTSIDE the gas-tight envelope"],
         PLANT, MID)
    _chain(d, 24 * mm, 94 * mm, 24 * mm, 89.4 * mm, MID, 0.8)
    _chain(d, 72 * mm, 94 * mm, 72 * mm, 89.4 * mm, MID, 0.8)

    _box(d, 112 * mm, 76 * mm, 58 * mm, 13 * mm, "BATTERY + INVERTER",
         ["48 V DC  ·  149 Ah  ·  204 kg  ·  0.40 m2"], WARN, ACCENT)
    _chain(d, 92 * mm, 82.5 * mm, 111.4 * mm, 82.5 * mm, MID, 0.7)

    # the envelope
    d.rect(0, 14 * mm, W, 54 * mm, fill=None, c=RED, sw=0.7, dash=[3, 2])
    d.txt(3 * mm, 63.4 * mm, "THE GAS-TIGHT AND EMP ENVELOPE  -  every "
          "conductor crossing it uses the SERVICE ENTRY PLATE, the "
          "project's single services penetration", 4.2, RED, bold=True)
    d.rect(40 * mm, 68 * mm, 34 * mm, 5.4 * mm, fill=WARN, c=RED, sw=0.6)
    d.txt(57 * mm, 69.4 * mm, "SERVICE ENTRY PLATE", 4.0, RED, "middle",
          bold=True)
    _chain(d, 48 * mm, 76 * mm, 48 * mm, 73.8 * mm, MID, 0.7)
    _chain(d, 48 * mm, 68 * mm, 48 * mm, 61.4 * mm, MID, 0.7)
    d.txt(78 * mm, 70.4 * mm, "PCI ON POWER  ·  FIBRE FOR SIGNAL", 4.0, RED,
          bold=True)
    _chain(d, 141 * mm, 76 * mm, 141 * mm, 61.4 * mm, ACCENT, 0.7)
    d.txt(143 * mm, 67.0 * mm, "on loss of BOTH sources", 3.9, ACCENT)

    _box(d, 24 * mm, 48 * mm, 130 * mm, 13 * mm, "DB-E   ESSENTIAL BOARD",
         ["bay 5, the CBRN plant room  ·  INSIDE the envelope"], PLANT,
         ACCENT)
    _box(d, 56 * mm, 30 * mm, 62 * mm, 12 * mm, "DB-Z2   EMP ZONE 2 SUB-BOARD",
         ["bay 3, inside the shielded enclosure"], GOLD, INK)
    _chain(d, 87 * mm, 48 * mm, 87 * mm, 42.4 * mm, ACCENT, 0.7)
    d.rect(78 * mm, 43.4 * mm, 18 * mm, 4.4 * mm, fill=WARN, c=RED, sw=0.5)
    d.txt(87 * mm, 44.6 * mm, "PCI", 4.0, RED, "middle", bold=True)

    # essential list
    d.txt(3 * mm, 25.4 * mm, "WHAT STAYS LIVE WITH NO MAINS AND NO "
          "GENERATOR  -  1.283 kW for 4 hours", 4.4, ACCENT, bold=True)
    ess = [("0.100", "emergency lighting, maintained"),
           ("0.150", "reduced general lighting, 25 %"),
           ("0.100", "fire detection and alarm"),
           ("0.750", "EMP zone 2 at 50 % duty"),
           ("0.033", "clean sump pump, 10 % duty"),
           ("0.100", "CO2 scrubber recirculation fan"),
           ("0.050", "instruments and monitoring")]
    for i, (kw, nm) in enumerate(ess):
        x = 3 * mm + (i % 4) * 43 * mm
        yy = 20.8 * mm - (i // 4) * 4.4 * mm
        d.txt(x, yy, kw + " kW", 4.0, INK, bold=True)
        d.txt(x + 13 * mm, yy, nm, 4.0, MID)

    d.txt(0, 9.0 * mm, "CONNECTED LOAD 6.256 kW = 7.360 kVA AT pf 0.85.  "
          "GEN-1 AT 15 kVA IS 49.1 % UTILISED  -  high enough to avoid "
          "wet-stacking, low enough to carry growth.", 4.2, GREEN, bold=True)
    d.txt(0, 4.4 * mm, "The largest motor is the filter fan at 0.379 kW;  "
          "even direct-on-line it is about 2.7 kVA, so there is no starting "
          "problem.  THE PACKAGE STOPS AT BOARD LEVEL  -  no circuit "
          "schedule, no cable sizing, no luminaire layout.", 4.0, MID)
    d.txt(0, 0.2 * mm, "GROUNDWATER DOES NOT STOP BECAUSE THE SHELTER IS "
          "SEALED.  The hand pump PU-03 and the two hand cranks on the "
          "filter fans are what cover the battery failing;  no electrical "
          "design should obscure them.", 4.0, RED, bold=True)
    return d


# ===========================================================================
#  8  CONCRETE MIX DESIGN
# ===========================================================================

MIX = {
    "M35": dict(fck=35.0, s=5.0, X=6.5, wc_cap=0.45, cem_min=340.0,
                slump=100, wred=0.20, wc=0.40, water=158.0, cem=400.0,
                ca_frac=0.577, ca=1149.6, fa=786.4, adm=4.00, sgc=3.15,
                sgca=2.84, sgfa=2.65, air=0.010),
    "M30": dict(fck=30.0, s=5.0, X=6.5, wc_cap=0.45, cem_min=320.0,
                slump=75, wred=0.18, wc=0.44, water=157.0, cem=360.0,
                ca_frac=0.633, ca=1287.5, fa=696.5, adm=2.88, sgc=3.15,
                sgca=2.84, sgfa=2.65, air=0.010),
}


def fig_mix_proportions():
    """The two trial mixes, by mass and by absolute volume."""
    d = Fig(W, 96 * mm)
    d.txt(0, 90 * mm, "CONCRETE MIX DESIGN  -  M35 AND M30 TO THE IS 10262 "
          "METHOD, AS TRIAL MIXES", 5.4, INK, bold=True)
    d.txt(0, 85.4 * mm, "Every input marked  [A]  is assumed by this report.  "
          "NO MIX IS CONFIRMED ANYWHERE IN THE PROJECT, and none of this "
          "replaces a laboratory trial.", 4.2, RED, bold=True)

    for pane, (grade, x0, use) in enumerate((
            ("M35", 0.0, "shelter, stairs, headhouse  -  very severe, "
             "permanently below the design water table"),
            ("M30", 90 * mm, "sentry post and burster slab"))):
        m = MIX[grade]
        d.txt(x0, 77 * mm, grade, 7.0, ACCENT, bold=True)
        d.txt(x0 + 14 * mm, 77 * mm, use, 4.0, MID)
        tgt = max(m["fck"] + 1.65 * m["s"], m["fck"] + m["X"])
        lines = [
            ("characteristic strength  f_ck", "%.0f N/mm2" % m["fck"], "[C]"),
            ("standard deviation  s,  Table 2", "%.1f N/mm2" % m["s"], "[C]"),
            ("f_ck + 1.65 s", "%.2f N/mm2" % (m["fck"] + 1.65 * m["s"]), ""),
            ("f_ck + X,  Table 1", "%.2f N/mm2" % (m["fck"] + m["X"]), ""),
            ("TARGET MEAN STRENGTH", "%.2f N/mm2" % tgt, ""),
            ("", "", ""),
            ("free w/c cap,  IS 456 Table 5", "%.2f" % m["wc_cap"], "[C]"),
            ("minimum cement,  IS 456 Table 5", "%.0f kg/m3" % m["cem_min"],
             "[C]"),
            ("target slump", "%d mm" % m["slump"], "[A]"),
            ("water, Table 4 at 50 mm, 20 mm agg", "186 L/m3", ""),
            ("slump correction  +3 %% / 25 mm",
             "%.1f L/m3" % (186.0 * (1 + 0.03 * (m["slump"] - 50) / 25.0)),
             ""),
            ("superplasticiser reduction",
             "%.0f %%" % (m["wred"] * 100), "[A]"),
            ("WATER ADOPTED", "%.0f L/m3" % m["water"], ""),
            ("w/c adopted", "%.2f" % m["wc"], "[A]"),
            ("cement = water / (w/c)",
             "%.1f kg/m3" % (m["water"] / m["wc"]), ""),
            ("CEMENT ADOPTED", "%.0f kg/m3" % m["cem"], ""),
            ("resulting free w/c",
             "%.3f" % (m["water"] / m["cem"]), ""),
        ]
        y = 71 * mm
        for k, (lab, val, cls) in enumerate(lines):
            yy = y - k * 4.5
            if not lab:
                continue
            bold = lab.isupper()
            d.txt(x0, yy, lab, 4.0, INK if bold else MID, bold=bold)
            d.txt(x0 + 62 * mm, yy, val, 4.0, ACCENT if bold else INK,
                  "end", bold=bold)
            if cls:
                d.txt(x0 + 64 * mm, yy, cls, 3.6,
                      RED if cls == "[A]" else GREEN)
        d.line(x0, 71 * mm + 3.2, x0 + 70 * mm, 71 * mm + 3.2, RULE, 0.4)
        d.line(x0, y - 4 * 4.5 - 1.8, x0 + 70 * mm, y - 4 * 4.5 - 1.8,
               RULE, 0.3)
        d.line(x0, y - 16 * 4.5 - 1.8, x0 + 70 * mm, y - 16 * 4.5 - 1.8,
               RULE, 0.3)

        # --- the batch, as a stacked bar by absolute volume
        vols = [("CEMENT", m["cem"] / (m["sgc"] * 1000.0), CONC),
                ("WATER", m["water"] / 1000.0, WATER),
                ("FINE AGG", m["fa"] / (m["sgfa"] * 1000.0), SOIL),
                ("COARSE AGG", m["ca"] / (m["sgca"] * 1000.0), ROCK),
                ("AIR 1.0 %", m["air"], colors.white)]
        adm = m["adm"] / (1.145 * 1000.0)
        vols.insert(2, ("ADMIXTURE", adm, GOLD))
        bx, bw = x0, 70 * mm
        by, bh = 22 * mm, 9 * mm
        acc = 0.0
        for nm, vv, col in vols:
            wdt = bw * vv
            d.rect(bx + bw * acc, by, wdt, bh, fill=col, c=MID, sw=0.35)
            acc += vv
        d.txt(x0, by + bh + 7.2, "ONE CUBIC METRE BY ABSOLUTE VOLUME  -  "
              "total %.4f" % acc, 4.2, INK, bold=True)
        d.txt(x0, by + bh + 2.6, "cement %.4f  ·  water %.3f  ·  admixture "
              "%.4f  ·  aggregate %.4f  ·  air %.3f"
              % (vols[0][1], vols[1][1], adm, vols[3][1] + vols[4][1],
                 m["air"]), 3.8, MID)
        d.txt(x0, by - 4.4, "BY MASS   1 : %.3f : %.3f   at w/c %.3f"
              % (m["fa"] / m["cem"], m["ca"] / m["cem"],
                 m["water"] / m["cem"]), 4.6, ACCENT, bold=True)
        d.txt(x0, by - 9.0, "cement %.0f  ·  fine %.1f  ·  coarse %.1f  ·  "
              "water %.0f  ·  admixture %.2f kg/m3   =   %.0f kg/m3"
              % (m["cem"], m["fa"], m["ca"], m["water"], m["adm"],
                 m["cem"] + m["fa"] + m["ca"] + m["water"] + m["adm"]),
              3.9, MID)
    return d


def fig_mix_notes():
    """What the mix design rests on, and what it cannot settle."""
    d = Fig(W, 74 * mm)
    d.txt(0, 68 * mm, "THE MIX DESIGN IS A TRIAL MIX, AND IT IS NOT A "
          "CONFIRMED PROJECT VALUE", 5.4, INK, bold=True)
    rows = [
        ("CONFIRMED  [C]", GREEN,
         ["M35 for the shelter, stairs and headhouse;  M30 for the sentry "
          "post and the burster slab;  M15 blinding",
          "free water / cement ratio not greater than 0.45",
          "minimum cement content 340 kg/m3 for the M35",
          "Fe500D to IS 1786 in the shelter, Fe500 in the sentry post",
          "integral crystalline waterproofing admixture throughout"]),
        ("ASSUMED BY THIS REPORT  [A]", RED,
         ["target slump, and therefore the water content",
          "the superplasticiser and the water reduction credited to it",
          "specific gravities  -  cement 3.15, coarse 2.84, fine 2.65",
          "fine aggregate grading zone II, 20 mm nominal coarse aggregate",
          "the 10 % reduction in coarse aggregate volume for congestion"]),
        ("NOT AVAILABLE  [N]", MID,
         ["the site's actual aggregate  -  no source, no grading, no "
          "specific gravity, no water absorption",
          "the admixture  -  no product, no dosage, no compatibility data",
          "trial mix cube results at 7 and 28 days",
          "the standard deviation of the actual supplier, which is what "
          "Table 2 is a stand-in for"])]
    y = 60 * mm
    for head, col, items in rows:
        d.txt(0, y, head, 4.8, col, bold=True)
        for i, it in enumerate(items):
            d.txt(6 * mm, y - 4.8 - i * 4.2, "-  " + it, 4.0, MID)
        y -= 6.0 + len(items) * 4.2 + 2.4
    d.line(0, 8.6 * mm, W, 8.6 * mm, RULE, 0.5)
    d.txt(0, 4.8 * mm, "THE PROJECT'S OWN PROCUREMENT TAKE-OFF ASSUMES 400 "
          "kg/m3 FOR THE M35 AND 360 kg/m3 FOR THE M30.  This design lands "
          "on the same two figures, which is a consistency check and not a "
          "confirmation:", 4.1, ACCENT, bold=True)
    d.txt(0, 0.6 * mm, "both are assumptions, and both are replaced the day "
          "a laboratory trial to IS 10262 is run on the aggregate the site "
          "will actually receive.  QA/QC item Q-06 is the hold point.", 4.0,
          MID)
    return d


# ===========================================================================
#  9  WORKS MANAGEMENT
# ===========================================================================

PROG = [("1", "PRE-CONSTRUCTION AND ENABLING WORKS", 0, 183, False),
        ("2", "SITE PREPARATION AND EARTHWORKS", 24, 190, False),
        ("3", "MAIN SHELTER  -  SUBSTRUCTURE", 96, 204, False),
        ("4", "MAIN SHELTER  -  PRESSURE SLAB", 184, 297, False),
        ("5", "ENTRY STRUCTURES, ESCAPE SHAFTS AND DOORS", 238, 317, False),
        ("6", "WATERPROOFING", 184, 319, False),
        ("7", "BACKFILL, ENGINEERED COVER AND OVERBURDEN", 80, 312, False),
        ("8", "SENTRY POST", 80, 221, False),
        ("9", "MECHANICAL, CBRN AND HVAC SERVICES", 138, 297, False),
        ("10", "DRAINAGE AND SANITARY WORKS", 263, 318, False),
        ("11", "ELECTRICAL AND EMP WORKS", 133, 304, False),
        ("12", "INTERNAL FINISHES", 267, 320, False),
        ("13", "EXTERNAL WORKS, CONCEALMENT AND RESTORATION", 312, 350,
         True),
        ("14", "TESTING, COMMISSIONING AND HANDOVER", 276, 383, True)]

MILE = [("M-01", 5, "site possession", True),
        ("M-04", 96, "excavation complete, formation approved", True),
        ("M-05", 133, "mat cast", False),
        ("M-07", 238, "pressure slab cast", False),
        ("M-09", 312, "overburden complete  -  the structure is buried",
         True),
        ("M-17", 350, "external works and concealment complete", True),
        ("M-18", 383, "PRACTICAL COMPLETION AND HANDOVER", True)]


def fig_gantt():
    """The fourteen-group programme, and where the critical path runs."""
    d = Fig(W, 156 * mm)
    d.txt(0, 150 * mm, "THE CONSTRUCTION PROGRAMME  -  FOURTEEN WORK "
          "PACKAGES OVER 384 CALENDAR DAYS", 5.4, INK, bold=True)
    d.txt(0, 145.4 * mm, "Monday 2 November 2026 to Saturday 20 November "
          "2027.  326 working days, 279 activities, 18 milestones, and 75 "
          "activities at zero total float.", 4.2, MID)

    x0, xw = 62 * mm, 104 * mm
    y1, dy, bh = 136 * mm, 6.2 * mm, 3.6 * mm
    ybot = y1 - 13 * dy - 3 * mm
    total = 384.0

    def X(day):
        return x0 + xw * day / total

    months = [(0, "NOV 26"), (28, "DEC"), (59, "JAN 27"), (90, "FEB"),
              (118, "MAR"), (149, "APR"), (179, "MAY"), (210, "JUN"),
              (240, "JUL"), (271, "AUG"), (302, "SEP"), (332, "OCT"),
              (363, "NOV 27")]
    for dday, lab in months:
        d.line(X(dday), y1 + 1.6 * mm, X(dday), ybot, RULE, 0.22)
        d.txt(X(dday) + 1.0, y1 + 2.2 * mm, lab, 3.7, MID)
    d.line(x0, y1 + 1.4 * mm, x0 + xw, y1 + 1.4 * mm, INK, 0.5)

    for i, (num, nm, a, b, crit) in enumerate(PROG):
        yy = y1 - i * dy
        d.txt(0, yy - 1.0, num, 4.0, MID, bold=True)
        d.txt(5 * mm, yy - 1.0, nm, 4.0, INK)
        col = RED if crit else ACCENT
        d.rect(X(a), yy - bh / 2.0, X(b) - X(a), bh,
               fill=WARN if crit else PLANT, c=col, sw=0.5)

    ym = ybot - 2.4 * mm
    for tag, day, lab, crit in MILE:
        col = RED if crit else MID
        d.poly([X(day), ym + 2.4, X(day) - 2.0, ym, X(day), ym - 2.4,
                X(day) + 2.0, ym], fill=col, c=col, sw=0.3)
        d.line(X(day), ym + 2.4, X(day), y1 + 1.4 * mm, col, 0.22,
               dash=[1.5, 2])
    d.txt(0, ym - 1.0, "MILESTONES", 4.0, MID, bold=True)

    yl = ym - 8 * mm
    for k, (tag, day, lab, crit) in enumerate(MILE):
        x = 0 if k < 4 else 84 * mm
        yy = yl - (k % 4) * 4.8 * mm
        col = RED if crit else MID
        d.txt(x, yy, tag, 4.0, col, bold=True)
        d.txt(x + 11 * mm, yy, lab, 4.0, MID)

    d.keyrow(0, 24 * mm, [(WARN, "on the critical path"),
                          (PLANT, "has float"),
                          (None, "diamonds are milestones")],
             4.1, 44 * mm)
    y = d.note(0, 18 * mm, "THE CRITICAL PATH RUNS THROUGH THE GROUND, NOT "
               "THROUGH THE STRUCTURE.",
               "It goes site possession  ->  survey and confirmatory "
               "investigation  ->  MONSOON GROUNDWATER MONITORING  ->  "
               "excavation support design  ->  rock excavation  ->  "
               "formation approval, and only then into concrete.  The "
               "pressure slab has 26 days of float;  THE GROUNDWATER "
               "MONITORING HAS NONE.")
    d.note(0, y - 5.4 * mm, "AND THAT IS THE RIGHT ANSWER.",
           "The design groundwater table is an assumption and the flotation "
           "factor of safety is 1.22 before the cover goes on, so the "
           "programme is telling you where the risk is.  Ten days of "
           "contingency for festival holidays and weather sit immediately "
           "before handover, and they are on the critical path too.")
    return d


def fig_critical_path():
    """The critical chain, condensed to the decisions it contains."""
    d = Fig(W, 104 * mm)
    d.txt(0, 98 * mm, "THE CRITICAL PATH  -  SEVENTY-FIVE ACTIVITIES, AND "
          "THE SIX PLACES IT CAN ACTUALLY BE LOST", 5.4, INK, bold=True)
    chain = [
        ("GROUND", "02-11-26", "10-12-26",
         ["contract, possession, survey",
          "confirmatory boreholes  12 d",
          "MONSOON GWT MONITORING  20 d",
          "issue confirmed parameters"], RED),
        ("EXCAVATION", "11-12-26", "06-02-27",
         ["support and slope design  10 d",
          "soil to rockhead  4 d",
          "rock by breaker  20 d",
          "sump pit  ·  trim  ·  HOLD POINT"], RED),
        ("SUBSTRUCTURE", "06-02-27", "13-03-27",
         ["blinding  ·  tanking  ·  HOLD POINT",
          "mat steel both curtains  11 d",
          "cast-in items  ·  HOLD POINT",
          "MAT AND SUMP  -  ONE POUR"], ACCENT),
        ("WALLS", "18-03-27", "04-05-27",
         ["steel W1-W4 and W5-W7  18 d",
          "lift 1 form, HOLD, cast, cure",
          "lift 2 form, HOLD, cast, cure",
          "two lifts, 1 600 each"], ACCENT),
        ("PRESSURE SLAB", "05-05-27", "22-07-27",
         ["falsework 3.200 high  8 d",
          "T25 both curtains  12 d",
          "trimmers and collars  8 d",
          "HOLD  ·  ONE POUR 112 m3  ·  14 d CURE"], ACCENT),
        ("COVER", "23-07-27", "20-11-27",
         ["roof membrane  ·  HOLD POINT",
          "fill 750  ·  rubble 500  ·  burster",
          "filter 150  ·  topsoil 300  ·  turf",
          "berms  ·  concealment  ·  snagging",
          "HANDOVER"], RED)]
    n = len(chain)
    gap = 3.2 * mm
    bw = (W - (n - 1) * gap) / n
    y0, bh = 40 * mm, 44 * mm
    for i, (head, d1, d2, items, col) in enumerate(chain):
        x = i * (bw + gap)
        d.rect(x, y0, bw, bh, fill=WARN if col is RED else PLANT, c=col,
               sw=0.7)
        d.txt(x + bw / 2.0, y0 + bh - 6.0, head, 5.0, col, "middle",
              bold=True)
        d.txt(x + bw / 2.0, y0 + bh - 10.6, d1, 3.8, MID, "middle")
        d.txt(x + bw / 2.0, y0 + bh - 14.2, "to  " + d2, 3.8, MID, "middle")
        for k, it in enumerate(items):
            d.txt(x + 1.6 * mm, y0 + bh - 20.0 - k * 5.6, it, 3.7, INK)
        if i < n - 1:
            d.arrow(x + bw + 0.4, y0 + bh / 2.0, x + bw + gap - 0.4,
                    y0 + bh / 2.0, INK, 0.8, 2.0)
    d.txt(0, 34 * mm, "NINE HOLD POINTS SIT ON THE CRITICAL PATH.  Each one "
          "is a day the Engineer must be on site, and each one is a day the "
          "contractor cannot buy back.", 4.2, ACCENT, bold=True)
    d.txt(0, 28.0 * mm, "THE TWENTY DAYS OF MONSOON GROUNDWATER MONITORING "
          "ARE THE MOST IMPORTANT TWENTY DAYS IN THE PROGRAMME.", 4.6, RED,
          bold=True)
    d.para(0, 23.4 * mm, "The design groundwater table at (-)2.000 is an "
           "assumption.  Every uplift number, the whole staged construction "
           "sequence and the 1.22 factor of safety at the bare-box stage "
           "depend on it.  If the monitoring returns a higher table, the "
           "answer is found before a single cubic metre of concrete is "
           "placed  -  which is exactly where it should be found.", 4.1,
           MID)
    d.txt(0, 15.0 * mm, "THE OTHER FIVE PLACES IT CAN BE LOST", 4.6, INK,
          bold=True)
    for i, t in enumerate([
            "rock excavation, 20 days by breaker  -  no blasting is "
            "permitted, and the quantity carries a declared overrun band",
            "the two single continuous pours  -  81.8 m3 of mat and 112 m3 "
            "of pressure slab;  neither has a construction joint to fall "
            "back on",
            "the 14-day cure and the props that must stay 14 days after "
            "that  -  three weeks that cannot be compressed",
            "the roof membrane hold point  -  once it is covered it cannot "
            "be inspected again for the life of the structure",
            "the ten days of festival and weather contingency at the end, "
            "which are already spent in the programme as issued"]):
        d.txt(0, 10.4 * mm - i * 4.2, "-  " + t, 4.0, MID)
    return d


def fig_cost_split():
    """Where the money is, and what turns the basic cost into the final one."""
    d = Fig(W, 126 * mm)
    d.txt(0, 120 * mm, "THE COST ESTIMATE  -  FIVE PACKAGES OF BASIC COST, "
          "AND SEVEN ADDITIONS ON TOP OF THEM", 5.4, INK, bold=True)

    parts = [("I", "SURVEY, SITE CLEARANCE AND EXCAVATION", 1912726, SOIL),
             ("II", "SUBSTRUCTURE AND FOUNDATION WORKS", 1283471, CONC2),
             ("III", "SUPERSTRUCTURE AND STRUCTURAL RCC", 4145877, CONC),
             ("IV", "REINFORCEMENT STEEL AND SHIELDING", 6333152, WARN),
             ("V", "CBRN, EMP, CLOSURES AND ANCILLARY SERVICES", 10545028,
              PLANT)]
    tot = float(sum(p[2] for p in parts))
    x0, xw = 72 * mm, 72 * mm
    d.txt(0, 112 * mm, "BASIC COST, BY PACKAGE", 4.6, INK, bold=True)
    d.txt(x0, 112 * mm, "bar to scale", 3.8, FAINT)
    d.txt(150 * mm, 112 * mm, "Rs million", 3.8, FAINT)
    d.txt(W, 112 * mm, "share", 3.8, FAINT, "end")
    for i, (num, nm, amt, col) in enumerate(parts):
        yy = 105 * mm - i * 6.4 * mm
        d.txt(0, yy, num, 4.2, MID, bold=True)
        d.txt(6 * mm, yy, nm, 4.1, INK)
        d.rect(x0, yy - 1.2, xw * amt / tot, 4.6, fill=col, c=MID, sw=0.35)
        d.txt(150 * mm, yy, "%.2f" % (amt / 1e6), 4.2, ACCENT, bold=True)
        d.txt(W, yy, "%.1f %%" % (100.0 * amt / tot), 4.0, MID, "end")
    d.line(0, 71.4 * mm, W, 71.4 * mm, RULE, 0.5)
    d.txt(0, 67 * mm, "TOTAL BASIC COST", 4.8, INK, bold=True)
    d.txt(150 * mm, 67 * mm, "24.22", 4.8, ACCENT, bold=True)
    d.txt(x0, 67 * mm, "Rs 2 42 20 254", 4.8, ACCENT, bold=True)

    heads = [("Contingencies", "3.0 %", 726608),
             ("Water and electricity provisions", "1.0 %", 242203),
             ("Specialist CBRN / EMP and engineering consultant", "6.0 %",
              1453215),
             ("Site supervision and quality assurance", "2.0 %", 484405),
             ("Statutory clearances and liaisoning", "1.0 %", 242203),
             ("Contractor's overhead and profit", "10.0 %", 2422025)]
    d.txt(0, 58 * mm, "ON TOP OF THE BASIC COST  -  23.0 % IN SIX LINES",
          4.6, INK, bold=True)
    for i, (nm, pc, amt) in enumerate(heads):
        yy = 51 * mm - i * 5.2 * mm
        d.txt(6 * mm, yy, nm, 4.1, MID)
        d.txt(x0 + 6 * mm, yy, pc, 4.1, MID, "end")
        d.txt(W, yy, "Rs " + "{:,}".format(amt).replace(",", " "), 4.1, INK,
              "end")
    d.line(0, 17.4 * mm, W, 17.4 * mm, RULE, 0.5)
    d.txt(6 * mm, 13 * mm, "FINAL PROJECT COST", 5.2, INK, bold=True)
    d.txt(W, 13 * mm, "Rs 2 97 90 913", 5.2, ACCENT, "end", bold=True)

    y = d.note(0, 7 * mm, "PART V IS 43.5 % OF THE BASIC COST AND PART IV IS "
               "26.1 %  -  SEVENTY PER CENT OF THIS STRUCTURE IS ITS "
               "PROTECTIVE CONTENT AND ITS STEEL, NOT ITS CONCRETE.",
               "Rates are not verified against any published schedule of "
               "rates:  no DSR or state SoR reference exists in the "
               "project, the CBRN and EMP items are budgetary allowances, "
               "and several have no vendor quotation behind them.  The "
               "owner's own summary reaches Rs 3 00 33 306 from a basic "
               "cost of Rs 2 43 36 022, and its cost heads sum Rs 1 00 000 "
               "short of the total it states  -  a recorded conflict, "
               "reproduced here and not corrected.", 4.2, 4.0, RED)
    return d


def fig_boq_split():
    """The bill, by section, in the units each section is measured in."""
    d = Fig(W, 100 * mm)
    d.txt(0, 94 * mm, "THE BILL OF QUANTITIES  -  TEN SECTIONS, AND THE "
          "QUANTITY THAT DEFINES EACH ONE", 5.4, INK, bold=True)
    rows = [("A", "SITE PREPARATION AND EARTHWORKS", "1 338 m3 excavation, "
             "of which 994 m3 is rock", SOIL),
            ("B", "MAIN SHELTER  -  CONCRETE", "388.7 m3, all M35 except "
             "17.3 m3 of M15 blinding", CONC),
            ("C", "REINFORCEMENT  -  ALL WORKS", "77.33 t ordered, "
             "including 5 % wastage", WARN),
            ("D", "FORMWORK AND FALSEWORK", "1 058 m2, including 3.2 m "
             "high falsework to the pressure slab", CONC2),
            ("E", "ENGINEERED COVER AND OVERBURDEN", "205.8 m3 in six "
             "layers over 136.4 m2", RUB),
            ("F", "WATERPROOFING", "532 m2 of continuous tanking", WATER),
            ("G", "SENTRY POST  -  CONCRETE AND FRAME", "20.95 m3 M30, "
             "1.97 t of reinforcement", CONC),
            ("H", "SENTRY POST  -  BRICK MASONRY", "12.20 m3, 6 400 "
             "modular bricks to IS 1077", RUB),
            ("I", "ELECTRICAL AND EMP INSTALLATION", "EVERY LINE IS  [N]  "
             "-  no electrical design package exists", None),
            ("J", "PRINCIPAL MATERIALS", "194.2 t cement, 828.7 t "
             "aggregate", ROCK)]
    y = 84 * mm
    for i, (ltr, nm, q, col) in enumerate(rows):
        yy = y - i * 6.6
        d.rect(0, yy - 1.2, 4.2, 3.6, fill=col or colors.white,
               c=RED if col is None else MID, sw=0.4)
        d.txt(7 * mm, yy, ltr, 4.2, MID, bold=True)
        d.txt(12 * mm, yy, nm, 4.2, INK, bold=True)
        d.txt(78 * mm, yy, q, 4.1, RED if col is None else MID)
        d.line(0, yy - 2.8, W, yy - 2.8, RULE, 0.2)
    d.txt(0, 14.0 * mm, "THE QUANTITIES ARE TAKEN FROM THE STRUCTURAL CAD "
          "PACKAGE, NOT RE-MEASURED FROM THE DRAWINGS.", 4.4, ACCENT,
          bold=True)
    d.txt(0, 9.6 * mm, "Six of the eight concrete lines reproduce exactly "
          "from the stated geometry;  the main staircase and the entry "
          "stairwell are composite figures accepted as they stand.", 4.1,
          MID)
    d.txt(0, 5.0 * mm, "SECTION I IS NOT AN OMISSION  -  IT IS A DECLARED "
          "GAP.", 4.4, RED, bold=True)
    d.txt(0, 0.4 * mm, "Seven electrical and EMP lines are carried in the "
          "bill with no quantity against them, because no design exists to "
          "measure.  Pricing them would be inventing them.", 4.0, MID)
    return d


# ===========================================================================
#  10  OPENINGS, DOORS AND THE WAY IN
# ===========================================================================

def fig_openings_register():
    """Every opening through the protective boundary, on one page."""
    d = Fig(W, 108 * mm)
    d.txt(0, 102 * mm, "EVERY OPENING THROUGH THE PROTECTIVE BOUNDARY", 5.4,
          INK, bold=True)
    d.txt(0, 97.4 * mm, "A protective envelope is only as good as its "
          "weakest closure.  There are nine, and four of them are not blast "
          "rated because they are outside the boundary by design.", 4.2, MID)
    rows = [
        ("BLAST DOOR 1", "W6, 400 thk, opening Y 600-1800", "1 200 x 2 100",
         "(-)6.100", ">= 7 bar, gas-tight, rebound-rated", RED, True),
        ("BLAST DOOR 2", "W7, 400 thk, opening Y 600-1800", "1 200 x 2 100",
         "(-)6.100", ">= 7 bar", RED, True),
        ("D-05", "W5, the fire and gas-tight wall", "to be designed",
         "(-)6.100", "gas-tight;  escape route R1 crosses it", GOLD, True),
        ("ESC 1 HEAD", "bay 1, through the pressure slab", "1 400 dia bore",
         "+0.150", "ribbed steel weldment, 4 quarter-turn dogs", RED, True),
        ("ESC 2 HEAD", "bay 8, through the pressure slab", "1 400 dia bore",
         "+0.700", "as ESC 1;  6.800 m climb", RED, True),
        ("STAIR VOID", "pressure slab, bay 7", "2 800 x 3 160", "(-)2.000",
         "NOT A CLOSURE  -  it is the route in", MID, True),
        ("INNER SECURITY DOOR", "HW2, headhouse north wall", "900 x 2 100",
         "(-)2.000", "NOT blast rated", MID, False),
        ("ENTRY DOOR", "entry stairwell headwall, opens OUTWARD",
         "1 000 x 2 100", "0.000", "NOT blast rated  -  expendable", MID,
         False),
        ("W8 GAPS  x4", "internal partitions, 110 thk", "900 x 2 100 gap",
         "(-)6.100", "PERMANENTLY OPEN, no doors, by design", MID, False)]
    colx = (0, 34 * mm, 84 * mm, 110 * mm, 126 * mm)
    for i, h in enumerate(("MARK", "WHERE", "LEAF / BORE", "LEVEL",
                           "WHAT IT HAS TO DO")):
        d.txt(colx[i], 90 * mm, h, 4.0, MID, bold=True)
    d.line(0, 90 * mm - 2.4, W, 90 * mm - 2.4, RULE, 0.5)
    for k, (mk, wh, leaf, lv, duty, col, inside) in enumerate(rows):
        yy = 90 * mm - 7.2 - k * 6.6
        d.txt(colx[0], yy, mk, 4.2, col if inside else MID, bold=True)
        d.txt(colx[1], yy, wh, 4.0, MID)
        d.txt(colx[2], yy, leaf, 4.0, INK)
        d.txt(colx[3], yy, lv, 4.0, INK)
        d.txt(colx[4], yy, duty, 4.0, col)
        d.line(0, yy - 2.6, W, yy - 2.6, RULE, 0.2)
    d.txt(0, 27.0 * mm, "BOTH BLAST DOORS ARE THE PROTECTIVE BOUNDARY, NOT "
          "SOMETHING FITTED INTO IT.", 4.6, RED, bold=True)
    d.para(0, 22.4 * mm, "They sit in the same plane as W6 and W7, the "
           "shaft beyond them equalises to the full incident overpressure, "
           "and so the doors and the walls beside them take the same "
           "383 kPa.  Each frame is a cast-in steel frame anchored into and "
           "welded to the reinforcement cage  -  which is both the blast "
           "fixing and the only EMP continuity the opening has.", 4.1, MID)
    d.txt(0, 13.6 * mm, "THE DOORS THEMSELVES ARE VENDOR ITEMS AND ARE NOT "
          "DESIGNED HERE.", 4.6, RED, bold=True)
    d.para(0, 9.0 * mm, "The geometry, the level, the frame and the "
           "rating are the project's;  the leaf, the hinge, the seal, the "
           "latching and the rebound capacity are the manufacturer's, and "
           "no vendor data exists in the project  [N].", 4.1, MID)
    d.para(0, 3.0 * mm, "The four W8 gaps are deliberate:  the "
           "partitions are 110 mm and non-structural, they were never fire "
           "or blast barriers, and closing them would obstruct the escape "
           "spine.  The consequence  -  bays 1 to 6 are one smoke "
           "compartment 20.8 m long  -  is recorded, not designed away.",
           4.0, MID)
    return d


def fig_blast_door():
    """Blast door 1 -- what a closure in the boundary has to survive."""
    d = Fig(W, 140 * mm)
    STL = colors.Color(0.72, 0.74, 0.78)
    d.txt(0, 134 * mm, "BLAST DOOR 1  -  THE CLOSURE IN W6, AND THE FOUR "
          "THINGS IT HAS TO DO AT ONCE", 5.4, INK, bold=True)

    # ---------------- elevation from the stair shaft
    v = V(40, 22 * mm, 46 * mm)
    d.txt(4 * mm, 124 * mm, "ELEVATION FROM THE STAIR SHAFT   1 : 40", 4.6,
          INK, bold=True)
    d.rect(v.x(-700), v.y(-200), v.d(2600), v.d(2900), fill=CONC, c=INK,
           sw=0.8)
    d.hatch(v.x(-700), v.y(-200), v.d(2600), v.d(2900), 45, 5.0, FAINT, 0.22)
    d.rect(v.x(-150), v.y(-150), v.d(1500), v.d(2400), fill=CONC2, c=INK,
           sw=0.7)
    d.rect(v.x(0), v.y(0), v.d(1200), v.d(2100), fill=STL, c=INK, sw=1.0)
    for k in range(1, 4):
        d.line(v.x(0), v.y(k * 525), v.x(1200), v.y(k * 525), MID, 0.35)
    for cx, cy in ((150, 300), (150, 1800), (1050, 300), (1050, 1800)):
        d.circ(v.x(cx), v.y(cy), 2.2, fill=WARN, c=RED, sw=0.7)
    d.txt(v.x(600), v.y(1050) - 1.4, "1 200 x 2 100", 4.6, INK, "middle",
          bold=True)
    d.txt(v.x(600), v.y(700), "CLEAR OPENING", 4.0, MID, "middle")
    d.dimh(v.x(0), v.x(1200), v.y(-450), "1 200", 4.3, INK)
    d.dimv(v.y(0), v.y(2100), v.x(-400), "2 100", 4.3)
    d.txt(4 * mm, 30 * mm, "FOUR QUARTER-TURN DOGS, one per corner", 4.0,
          RED, bold=True)
    d.txt(4 * mm, 26 * mm, "CAST-IN STEEL FRAME, WELDED TO THE CAGE", 4.0,
          ACCENT, bold=True)

    # ---------------- plan section at the jamb
    v2 = V(26, 116 * mm, 74 * mm)
    d.txt(88 * mm, 124 * mm, "PLAN SECTION AT THE JAMB   1 : 26", 4.6, INK,
          bold=True)
    d.rect(v2.x(-900), v2.y(0), v2.d(900), v2.d(400), fill=CONC, c=INK,
           sw=0.9)
    d.hatch(v2.x(-900), v2.y(0), v2.d(900), v2.d(400), 45, 4.0, FAINT, 0.22)
    d.rect(v2.x(-180), v2.y(0), v2.d(180), v2.d(400), fill=STL, c=INK,
           sw=0.7)
    d.rect(v2.x(-180), v2.y(150), v2.d(1500), v2.d(40), fill=STL, c=INK,
           sw=0.5)
    d.rect(v2.x(-140), v2.y(190), v2.d(1400), v2.d(130),
           fill=colors.Color(0.62, 0.64, 0.70), c=INK, sw=0.9)
    d.txt(v2.x(600), v2.y(230), "LEAF", 4.4, colors.white, "middle",
          bold=True)
    d.circ(v2.x(-60), v2.y(190), 1.6, fill=WARN, c=RED, sw=0.6)
    d.txt(v2.x(-140), v2.y(-260), "SEAL  -  it seats on the FRAME,", 4.0,
          RED)
    d.txt(v2.x(-140), v2.y(-520), "never on the concrete", 4.0, RED)
    d.txt(v2.x(-880), v2.y(180), "W6  400", 4.2, INK, bold=True)
    d.txt(v2.x(-880), v2.y(560), "CAST-IN FRAME", 4.0, ACCENT, bold=True)
    d.dimv(v2.y(0), v2.y(400), v2.x(-1060), "400", 4.2)
    d.arrow(v2.x(600), v2.y(1150), v2.x(600), v2.y(440), RED, 1.0)
    d.txt(v2.x(700), v2.y(880), "383 kPa  IN", 4.4, RED, bold=True)
    d.txt(v2.x(700), v2.y(620), "from the stair shaft", 4.0, RED)
    d.arrow(v2.x(600), v2.y(-900), v2.x(600), v2.y(150), ACCENT, 1.0)
    d.txt(v2.x(700), v2.y(-860), "REBOUND AND", 4.4, ACCENT, bold=True)
    d.txt(v2.x(700), v2.y(-1120), "NEGATIVE PHASE  OUT", 4.4, ACCENT,
          bold=True)

    duties = [("1  TAKE THE LOAD IN", RED,
               "the shaft beyond it equalises to the full incident "
               "overpressure, so the leaf sees the same 383 kPa as the "
               "400 mm wall it sits in"),
              ("2  TAKE THE LOAD OUT", ACCENT,
               "the negative phase and the structural rebound both pull the "
               "leaf away from its frame;  a door detailed only for inward "
               "pressure comes off"),
              ("3  STAY GAS-TIGHT", GREEN,
               "it is part of the envelope tested at +300 Pa, and the "
               "overpressure cascade only works if it seals"),
              ("4  CARRY THE CAGE ACROSS", GOLD,
               "the frame is welded to the reinforcement cage, so the "
               "opening is the only EMP continuity the boundary has there")]
    for i, (head, col, txt) in enumerate(duties):
        yy = 20 * mm - i * 4.6 * mm
        d.txt(0, yy, head, 4.4, col, bold=True)
        d.txt(34 * mm, yy, txt, 3.9, MID)
    d.txt(0, 1.4 * mm, "THE LEAF, THE HINGE, THE SEAL AND THE LATCHING ARE "
          "VENDOR DATA  [N].  What the project fixes is the opening, the "
          "level, the frame, the rating and the four duties above.", 4.1,
          RED, bold=True)
    return d


def fig_entry_route():
    """The way in, stated once, from grade to the clean zone."""
    d = Fig(W, 96 * mm)
    d.txt(0, 90 * mm, "THE WAY IN  -  NINE STEPS FROM GRADE TO THE CLEAN "
          "ZONE, AND WHERE THE PROTECTIVE BOUNDARY ACTUALLY STARTS", 5.4,
          INK, bold=True)
    steps = [("ENTRY DOOR", "0.000", "1 000 x 2 100, opens OUTWARD",
              CONC2, MID),
             ("COVERED STAIRWELL", "0.000 to (-)2.000",
              "12 risers  ·  EXPENDABLE", CONC2, MID),
             ("HEADHOUSE", "(-)2.000", "500 roof, 400 walls, NO earth cover",
              CONC2, MID),
             ("INNER SECURITY DOOR", "(-)2.000",
              "900 x 2 100, NOT blast rated", CONC2, MID),
             ("MAIN STAIRCASE", "(-)2.000 to (-)6.100",
              "24R @ 170.8333, 3 flights of 8", PLANT, ACCENT),
             ("BAY 7  STAIR SHAFT", "(-)6.100", "the buried box begins",
              PLANT, ACCENT),
             ("BLAST DOOR 1", "(-)6.100", "THE BOUNDARY  -  1 200 x 2 100",
              WARN, RED),
             ("DECON AIRLOCK", "(-)6.100",
              "bay 6  ·  three stages  ·  +10, +20, +35 Pa", WARN, RED),
             ("CLEAN ZONE", "(-)6.100", "bays 1 to 5  ·  +50 Pa", AIR,
              GREEN)]
    n = len(steps)
    gap = 2.2 * mm
    bw = (W - (n - 1) * gap) / n
    y0, bh = 50 * mm, 26 * mm
    for i, (nm, lv, note, fill, col) in enumerate(steps):
        x = i * (bw + gap)
        d.rect(x, y0, bw, bh, fill=fill, c=col, sw=0.6)
        words = nm.split()
        for k, wd in enumerate(words):
            d.txt(x + bw / 2.0, y0 + bh - 5.0 - k * 4.2, wd, 4.2, col,
                  "middle", bold=True)
        d.txt(x + bw / 2.0, y0 + 8.2, lv, 3.8, INK, "middle", bold=True)
        nn = note.split("  ·  ")
        for k, wd in enumerate(nn[:2]):
            d.txt(x + bw / 2.0, y0 + 4.0 - k * 3.4, wd[:22], 3.4, MID,
                  "middle")
        if i < n - 1:
            d.arrow(x + bw + 0.3, y0 + bh / 2.0, x + bw + gap - 0.3,
                    y0 + bh / 2.0, INK, 0.7, 1.8)
        d.txt(x + bw / 2.0, y0 - 4.6, str(i + 1), 4.0, FAINT, "middle",
              bold=True)
    # the boundary
    xb = 6 * (bw + gap) - gap / 2.0
    d.line(xb, y0 - 9 * mm, xb, y0 + bh + 9 * mm, RED, 1.2, dash=[3, 2])
    d.txt(xb - 1.6, y0 + bh + 10.4, "OUTSIDE  -  expendable", 4.4, MID,
          "end", bold=True)
    d.txt(xb + 1.6, y0 + bh + 10.4, "INSIDE  -  the protective boundary",
          4.4, RED, bold=True)

    d.txt(0, 36 * mm, "EVERYTHING WEST OF THAT LINE IS DESIGNED TO BE LOST.",
          4.6, RED, bold=True)
    d.para(0, 31.4 * mm, "The covered stairwell is explicitly expendable "
           "and is not blast rated.  The headhouse has no earth cover.  The "
           "entry door opens outward so that blast cannot drive it into the "
           "stairwell, and it is not rated either.  None of that is an "
           "oversight:  the boundary is Blast Door 1 and the 400 mm wall it "
           "sits in, and the approach is a weather and security enclosure "
           "in front of it.", 4.1, MID)
    d.txt(0, 21.0 * mm, "WHICH IS WHY THE STAIR VOID IS THE EMP FINDING.",
          4.6, RED, bold=True)
    d.para(0, 16.4 * mm, "The same route that makes the shelter usable "
           "puts a 2 800 x 3 160 hole through a 900 mm pressure slab, and "
           "the reinforcement cage stops at its edge.  A bonded conducting "
           "hatch answers the escape shafts.  Nothing equivalent is "
           "specified here, and nothing is invented for it.", 4.1, MID)
    d.txt(0, 8.0 * mm, "AND IT IS ALSO THE ONLY ROUTE AN INJURED PERSON CAN "
          "USE.", 4.6, ACCENT, bold=True)
    d.txt(0, 3.4 * mm, "Routes R2 and R3 are 1 400 mm shafts with vertical "
          "ladders and a six-metre climb.  They are escape shafts, not "
          "exits.", 4.1, MID)
    return d


def fig_stair_section():
    """The main staircase, developed -- the frozen geometry."""
    d = Fig(W, 100 * mm)
    d.txt(0, 94 * mm, "MAIN STAIRCASE, BAY 7  -  DEVELOPED SECTION.  "
          "TWENTY-FOUR RISERS, THREE FLIGHTS OF EIGHT   1 : 70", 5.4, INK,
          bold=True)
    v = V(70, 16 * mm, 28 * mm)
    R, T, N = 170.8333, 280.0, 8
    x, y = 0.0, 0.0
    pts = [(x, y)]
    for f in range(3):
        x += 1200.0
        pts.append((x, y))
        for k in range(N):
            y += R
            pts.append((x, y))
            if k < N - 1:
                x += T
                pts.append((x, y))
    x += 1200.0
    pts.append((x, y))
    flat, flat2 = [], []
    for px, py in pts:
        flat += [v.x(px), v.y(py)]
        flat2 += [v.x(px), v.y(py - 280)]
    d.pline(flat2, MID, 0.7)
    d.pline(flat, INK, 1.2)
    for lab, yy in (("(-)6.100", 0.0), ("(-)4.733", 8 * R),
                    ("(-)3.367", 16 * R), ("(-)2.000", 24 * R)):
        d.line(v.x(0), v.y(yy), v.x(x), v.y(yy), RULE, 0.3, dash=[2, 2])
        d.level(v.x(-100), v.y(yy), lab, 4.2, ACCENT, side=-1)
    d.dimv(v.y(0), v.y(24 * R), v.x(10900), "RISE 4 100", 4.4)
    for f in range(3):
        x0 = f * (1200.0 + 7 * T) + 1200.0
        d.dimh(v.x(x0), v.x(x0 + 7 * T), v.y(f * 8 * R - 700),
               "8R @ 170.8333   going 7 x 280 = 1 960", 4.0, MID)
    d.txt(0, 12.0 * mm, "THIS GEOMETRY IS FROZEN.  24 risers at 170.8333 mm, "
          "280 mm tread, three flights of eight, total rise 4 100 mm, "
          "1 200 mm wide, 200 mm well, 200 mm waist, 2 533 mm headroom.",
          4.3, RED, bold=True)
    d.txt(0, 7.4 * mm, "24 x 170.8333 = 4 100.0 exactly, which is (-)6.100 "
          "to (-)2.000.  2R + T = 621.7, inside the 550 to 700 band.  "
          "R + T = 450.8.  R x T = 47 833  -  all three of the classical "
          "checks pass.", 4.1, MID)
    d.txt(0, 2.8 * mm, "It is also the only escape route usable by an "
          "injured person, which is why the width and the landings matter "
          "as much as the rise.", 4.1, MID)
    return d


def fig_excavation():
    """The excavation face -- a soil cap standing on rock."""
    d = Fig(W, 116 * mm)
    d.txt(0, 110 * mm, "THE EXCAVATION FACE  -  1.0 TO 1.5 m OF "
          "VERY-HIGH-SWELLING CLAY STANDING ON 5.3 TO 5.9 m OF BASALT   "
          "1 : 90", 5.4, INK, bold=True)
    v = V(90, 70 * mm, 96 * mm)
    d.rect(v.x(-6000), v.y(-1500), v.d(6000), v.d(1500), fill=SOIL, c=None,
           sw=0)
    d.rect(v.x(-6000), v.y(-6800), v.d(6000), v.d(5300), fill=ROCK, c=None,
           sw=0)
    d.hatch(v.x(-6000), v.y(-6800), v.d(6000), v.d(5300), 45, 4.6,
            colors.Color(0.66, 0.68, 0.66), 0.2)
    d.poly([v.x(-6000), v.y(0), v.x(-1500), v.y(0), v.x(0), v.y(-1500),
            v.x(0), v.y(-6800), v.x(-6000), v.y(-6800)], fill=None, c=RED,
           sw=1.2)
    d.line(v.x(-6000), v.y(-1500), v.x(0), v.y(-1500), INK, 0.7)
    d.txt(v.x(-5900), v.y(-1350), "ROCKHEAD  (-)0.900 to (-)1.500", 4.2, INK)
    d.txt(v.x(-5900), v.y(-700), "CH HORIZON, FSI 60 to 65 %", 4.4, RED,
          bold=True)
    d.txt(v.x(-5900), v.y(-2450), "DESIGN GWT  (-)2.000", 4.0, BLUE)
    d.txt(v.x(-5900), v.y(-4200), "SOUND BASALT  -  VERTICAL FACE RETAINED",
          4.4, INK, bold=True)
    d.txt(v.x(-5900), v.y(-4900), "the rock cut undercuts the soil cap "
          "above it", 4.0, MID)
    d.txt(v.x(-1450), v.y(-560), "1 : 1 MIN", 4.4, RED, bold=True)
    d.line(v.x(-6000), v.y(-2000), v.x(1400), v.y(-2000), BLUE, 0.7,
           dash=[3, 2])
    d.rect(v.x(0), v.y(-6800), v.d(1400), v.d(6800), fill=None, c=FAINT,
           sw=0.5, dash=[2, 2])
    d.txt(v.x(700), v.y(-3400), "STRUCTURE", 4.0, FAINT, "middle",
          angle=90)
    d.dimh(v.x(-1500), v.x(0), v.y(500), "1 500 offset at 1 : 1", 4.2, RED)
    d.dimv(v.y(-6800), v.y(0), v.x(1600), "6 800", 4.2)

    d.txt(92 * mm, 96 * mm, "WHAT THE BATTER COSTS", 4.8, INK, bold=True)
    for k, (a, off, q) in enumerate((("1 : 1", "1.500 m offset", "76.4 m3"),
                                     ("1.25 : 1", "1.875 m offset",
                                      "96.7 m3"),
                                     ("1.5 : 1", "2.250 m offset",
                                      "117.6 m3"),
                                     ("1.0 m bench", "at rockhead",
                                      "96.6 m3"))):
        yy = 90 * mm - k * 5.0
        d.txt(92 * mm, yy, a, 4.2, INK if k == 0 else MID, bold=(k == 0))
        d.txt(118 * mm, yy, off, 4.0, MID)
        d.txt(W, yy, q, 4.2, INK if k == 0 else MID, "end", bold=(k == 0))
    d.txt(92 * mm, 62 * mm, "AND WHAT ROCKHEAD COSTS", 4.8, INK, bold=True)
    d.txt(92 * mm, 56 * mm, "rockhead", 3.8, FAINT)
    d.txt(118 * mm, 56 * mm, "rock cut", 3.8, FAINT)
    d.txt(146 * mm, 56 * mm, "m3", 3.8, FAINT, "end")
    d.txt(W, 56 * mm, "vs the bill", 3.8, FAINT, "end")
    for k, (rh, dep, vol, vs) in enumerate((
            ("(-)0.900", "5.900 m", "1 161.12", "+118.12"),
            ("(-)1.000", "5.800 m", "1 141.44", "+98.44"),
            ("(-)1.500", "5.300 m", "1 043.04", "+0.04"),
            ("(-)1.750", "5.050 m", "993.84", "the bill"),
            ("(-)2.000", "4.800 m", "944.64", "-98.36"))):
        yy = 50 * mm - k * 5.0
        d.txt(92 * mm, yy, rh, 4.2, MID)
        d.txt(118 * mm, yy, dep, 4.0, MID)
        d.txt(146 * mm, yy, vol, 4.2, INK, "end")
        d.txt(W, yy, vs, 4.0, RED if vs.startswith("+") else MID, "end")

    d.txt(0, 14.0 * mm, "1 : 1 IS A MINIMUM, NOT THE ANSWER.", 4.6, RED,
          bold=True)
    d.para(0, 9.4 * mm, "A batter in clay at free-swell index 60 to 65 "
           "per cent, undercut by the rock cut below it and wetted across a "
           "monsoon, may need to be considerably flatter.  The angle and "
           "its seasonal variation belong to the geotechnical engineer, and "
           "the quantity moves with the angle.  The working space is "
           "unchanged  -  the 1.000 m is at formation, 5.3 m below the "
           "battered zone.  Total excavation does not change with rockhead "
           "either:  soil falls by the same volume as rock rises, so what "
           "is at stake is the RATE difference over about 118 m3, not a "
           "rock rate over 118 m3.", 4.0, MID)
    return d


def fig_fire_egress():
    """Three routes, one smoke compartment, and the rule that picks a route."""
    d = Fig(W, 118 * mm)
    d.txt(0, 112 * mm, "FIRE AND EGRESS  -  THREE ROUTES, ONE SMOKE "
          "COMPARTMENT 20.8 m LONG, AND A SHELTER THAT CANNOT BE VENTILATED "
          "OF SMOKE", 5.4, INK, bold=True)

    v = V(160, 8 * mm, 70 * mm)
    d.rect(v.x(0), v.y(0), v.d(22000), v.d(6200), fill=CONC, c=INK, sw=0.7)
    d.rect(v.x(600), v.y(600), v.d(20800), v.d(5000), fill=AIR, c=MID,
           sw=0.35)
    for x0, x1 in GEOM["w8"]:
        d.rect(v.x(x0), v.y(600), v.d(x1 - x0), v.d(1900), fill=CONC2,
               c=MID, sw=0.3)
        d.rect(v.x(x0), v.y(3400), v.d(x1 - x0), v.d(2200), fill=CONC2,
               c=MID, sw=0.3)
    for x0, x1, col in ((GEOM["w5"][0], GEOM["w5"][1], GOLD),
                        (GEOM["w6"][0], GEOM["w6"][1], RED),
                        (GEOM["w7"][0], GEOM["w7"][1], RED)):
        d.rect(v.x(x0), v.y(600), v.d(x1 - x0), v.d(5000), fill=col, c=INK,
               sw=0.4)
    # the one smoke compartment
    d.rect(v.x(600), v.y(600), v.d(14200), v.d(5000), fill=None, c=RED,
           sw=0.9, dash=[3, 2])
    d.txt(v.x(7700), v.y(6700), "ONE SMOKE COMPARTMENT  -  BAYS 1 TO 6, "
          "20.8 m, FOUR PERMANENTLY OPEN 900 GAPS", 4.4, RED, "middle",
          bold=True)
    # routes
    d.pline([v.x(1400), v.y(2050), v.x(14600), v.y(2050), v.x(15000),
             v.y(1200), v.x(16600), v.y(1200)], GREEN, 1.6)
    d.txt(v.x(8000), v.y(2500), "R1  PRIMARY  -  the spine, blast door 1, "
          "the stair shaft, 24 risers", 4.2, GREEN, bold=True)
    for (cx, cy), tag, lab in ((GEOM["esc1"], "R2", "ESC 1  +0.150"),
                               (GEOM["esc2"], "R3", "ESC 2  +0.700")):
        d.circ(v.x(cx), v.y(cy), v.d(950), fill=WARN, c=RED, sw=0.8)
        d.txt(v.x(cx), v.y(cy + 200), tag, 4.4, RED, "middle", bold=True)
        d.txt(v.x(cx), v.y(cy - 700), lab, 3.8, RED, "middle")
    # fire load
    for cx, lab in ((20000, "GENERATOR"), (11800, "CARBON BEDS")):
        d.circ(v.x(cx), v.y(4400), 3.2, fill=RED, c=RED, sw=0)
        d.txt(v.x(cx), v.y(5000), lab, 4.0, RED, "middle", bold=True)
    d.txt(v.x(16600), v.y(4600), "BAY 7", 4.2, MID, "middle")
    d.txt(v.x(16600), v.y(4100), "STAIR SHAFT", 3.8, MID, "middle")

    # the decision rule
    d.txt(0, 56 * mm, "WHERE THE FIRE IS DECIDES THE ROUTE", 4.8, INK,
          bold=True)
    rule = [("BAY 8  -  the generator", "R1, or R2 if the spine is smoke-"
             "logged", "BLAST DOOR 2 SHUT.  Bay 8 is separately ventilated "
             "at 2 600 m3/h.  R3 IS INSIDE THE FIRE COMPARTMENT  -  DO NOT "
             "USE IT", RED),
            ("BAYS 1 TO 6  -  occupied", "R1 if the route to bay 7 is clear;"
             " otherwise R2 from the west, R1 or R3 from the east",
             "bays 1 to 6 are ONE compartment  -  smoke starting in bay 1 "
             "reaches bay 6 unobstructed", ACCENT),
            ("BAY 7  -  the stair shaft", "R2 or R3",
             "the primary route IS the fire.  Both blast doors shut", RED),
            ("HEADHOUSE OR STAIRWELL", "R2 or R3",
             "R1's surface end is blocked;  both are outside the boundary "
             "and the stairwell is expendable", MID)]
    for i, (where, route, why, col) in enumerate(rule):
        yy = 50 * mm - i * 9.6
        d.txt(0, yy, where, 4.2, col, bold=True)
        d.txt(42 * mm, yy, route, 4.1, INK)
        d.txt(42 * mm, yy - 4.2, why, 4.0, MID)
        d.line(0, yy - 6.6, W, yy - 6.6, RULE, 0.2)

    d.txt(0, 18.0 * mm, "R1 IS THE ONLY ROUTE THAT DOES NOT REQUIRE "
          "CLIMBING A SHAFT, AND THE ONLY ONE USABLE BY AN INJURED PERSON.",
          4.4, GREEN, bold=True)
    d.txt(0, 13.2 * mm, "THE MOST LIKELY FIRE IN THE SHELTER DENIES ONE OF "
          "ITS THREE ESCAPE ROUTES.", 4.4, RED, bold=True)
    d.para(0, 9.0 * mm, "ESC 2 is in the same bay as the generator.  Both "
           "facts are confirmed and neither is wrong alone;  the coupling "
           "is what had never been stated, and it is why the rule above "
           "routes a bay 8 fire away from ESC 2.", 4.0, MID)
    d.para(0, 3.6 * mm, "A FIRE DURING THE CLOSED MODE CANNOT BE "
           "VENTILATED AT ALL, and clearing smoke means opening a blast "
           "valve  -  which breaks the protection the closed mode exists to "
           "provide.  No rule exists for which hazard takes precedence.  "
           "That belongs to the client, and it should be made before it is "
           "needed rather than during.", 4.0, RED, bold=True)
    return d


# ===========================================================================
#  CAPTION REGISTER  --  the report's <!-- FIG: name --> directive looks the
#  caption up here, and the renderer numbers the figures in document order.
# ===========================================================================

CAPTIONS = {
    "fig_site_plan":
        "Key plan. Everything on the plot at true project coordinates - the "
        "buried box, the headhouse, the covered entry stairwell, the two "
        "escape shafts, the sentry post and the reserve.",
    "fig_site_setting":
        "The site in its setting, and the three concealment decisions that "
        "follow from it.",
    "fig_trial_pit_logs":
        "The sub-soil investigation against the structure it has to support. "
        "Eleven trial pits on three OTHER buildings, none deeper than 1.5 m, "
        "against a formation at (-)6.800.",
    "fig_bearing_chart":
        "Bearing demand against capacity. The worst case in the project uses "
        "20.6 per cent of the lowest measured soaked strength.",
    "fig_met_chart":
        "The meteorological record used by the design, month by month.",
    "fig_underground_plan":
        "The underground box in plan - eight bays, the two escape shafts, "
        "the stair shaft and every internal wall.",
    "fig_long_section":
        "Longitudinal section on the spine, from the west end to the "
        "generator bay.",
    "fig_cross_section":
        "Transverse section through the box, with the full engineered cover "
        "build-up and the load that arrives from each direction.",
    "fig_blast_wave":
        "The design pressure-time history at the structure, and the "
        "idealised triangular pulse taken from it.",
    "fig_dlf":
        "The dynamic load factor against ductility ratio, and the value "
        "adopted.",
    "fig_regimes":
        "Impulsive, dynamic and quasi-static response - where this structure "
        "sits, and why.",
    "fig_cover":
        "The engineered cover, layer by layer: 2 000 mm and 40.65 kPa.",
    "fig_lateral":
        "Lateral pressure on a perimeter wall - the static case and the "
        "blast case compared.",
    "fig_flotation":
        "Flotation at each construction stage. The bare box is the stage "
        "that governs.",
    "fig_wall_section":
        "Perimeter wall W1 to W4, 600 thick - section and reinforcement.",
    "fig_w6_and_door":
        "Walls W6 and W7 at 400, and the blast door openings they carry.",
    "fig_roof_section":
        "The pressure slab, 900 thick - the governing element.",
    "fig_roof_openings":
        "The roof in plan: the stair void, the two escape shaft collars and "
        "their trimmers.",
    "fig_mat_section":
        "The mat foundation, 600 thick, and the soft-band case that sizes "
        "it.",
    "fig_esc_head":
        "Escape shaft head - a 1.54 m2 hole in the protective boundary, and "
        "the hatch that closes it.",
    "fig_opening_corner":
        "The opening corner - the detail most often got wrong.",
    "fig_stair_section":
        "The main staircase, developed. Twenty-four risers, three flights of "
        "eight - frozen geometry.",
    "fig_entry_route":
        "The way in, from grade to the clean zone, and where the protective "
        "boundary actually starts.",
    "fig_openings_register":
        "Every opening through the protective boundary, on one page.",
    "fig_blast_door":
        "Blast door 1 in W6 - elevation, jamb section, and the four things "
        "the closure has to do at once.",
    "fig_excavation":
        "The excavation face: a very-high-swelling clay cap standing on "
        "basalt, and what the batter and the rockhead band cost.",
    "fig_mix_proportions":
        "Concrete mix design - M35 and M30 to the IS 10262 method, as trial "
        "mixes.",
    "fig_mix_notes":
        "What the mix design rests on, and what it cannot settle.",
    "fig_filter_train":
        "The NBC filter train - seven stages, in the order the air meets "
        "them.",
    "fig_hvac_schematic":
        "The whole air path - intake, the two trains, distribution, the "
        "cascade, the exhaust, and the separate generator loop.",
    "fig_cascade":
        "The overpressure cascade, and the three airlock stages it maps "
        "onto.",
    "fig_drainage_schematic":
        "The three hydraulic zones, and the one that has nowhere to go.",
    "fig_sump_detail":
        "The clean sump SU-01 - a pit cast into the mat, and therefore a "
        "penetration of the tanking.",
    "fig_septic_soakpit":
        "Foul drainage - the septic tank and the soak pit, to IS 2470.",
    "fig_water_balance":
        "The daily water balance: what arrives, where it is held, and where "
        "it is allowed to go.",
    "fig_emp_zones":
        "The three EMP zones, and the one that carries the requirement.",
    "fig_emp_se":
        "Shielding effectiveness of the reinforcement cage against a flat "
        "80 dB requirement.",
    "fig_penetrations":
        "Every penetration of the protective boundary, and whether the hole "
        "is its own waveguide.",
    "fig_single_line":
        "Electrical single line - three boards, one cable entry, and what "
        "stays live with nothing running.",
    "fig_fire_egress":
        "Fire and egress - three routes, one smoke compartment 20.8 m long, "
        "and the rule that picks a route.",
    "fig_gantt":
        "The construction programme - fourteen work packages over 384 "
        "calendar days.",
    "fig_critical_path":
        "The critical path condensed to the six places it can actually be "
        "lost.",
    "fig_cost_split":
        "The cost estimate - five packages of basic cost, and the additions "
        "on top of them.",
    "fig_boq_split":
        "The bill of quantities - ten sections, and the quantity that "
        "defines each one.",
}


def figure(name):
    """Return (drawing, caption) for a registered figure name."""
    fn = globals().get(name)
    if fn is None or not name.startswith("fig_"):
        raise KeyError("no such figure: %s" % name)
    return fn(), CAPTIONS.get(name, "")


def check_captions():
    """Every drawn figure must have a caption, and vice versa."""
    drawn = set(n for n in globals() if n.startswith("fig_"))
    capped = set(CAPTIONS)
    return sorted(drawn - capped), sorted(capped - drawn)


# ===========================================================================
#  BOUNDS CHECK -- no figure may draw outside its own frame
# ===========================================================================

def _strw(text, font, size):
    """Width of a string, or 0 if the face is not registered yet."""
    try:
        from reportlab.pdfbase import pdfmetrics
        return pdfmetrics.stringWidth(text, font, size)
    except Exception:                                         # noqa: BLE001
        return 0.55 * size * len(text)


def bounds_report(fig, name, tol=0.6):
    """Return a list of primitives that fall outside the drawing."""
    bad = []

    def walk(node, dx=0.0, dy=0.0, rot=False):
        for el in getattr(node, "contents", []):
            cls = el.__class__.__name__
            if cls == "Group":
                t = getattr(el, "transform", (1, 0, 0, 1, 0, 0))
                walk(el, dx + t[4], dy + t[5],
                     rot or abs(t[1]) > 1e-6 or abs(t[2]) > 1e-6)
                continue
            pts = []
            if cls == "Line":
                pts = [(el.x1, el.y1), (el.x2, el.y2)]
            elif cls == "Rect":
                pts = [(el.x, el.y), (el.x + el.width, el.y + el.height)]
            elif cls == "Circle":
                pts = [(el.cx - el.r, el.cy - el.r),
                       (el.cx + el.r, el.cy + el.r)]
            elif cls == "String":
                wdt = 0.0 if rot else _strw(el.text, el.fontName,
                                            el.fontSize)
                anch = getattr(el, "textAnchor", "start")
                x0 = el.x - (wdt if anch == "end" else
                             wdt / 2.0 if anch == "middle" else 0.0)
                pts = [(x0, el.y), (x0 + wdt, el.y + el.fontSize)]
            elif cls in ("Polygon", "PolyLine"):
                p = el.points
                pts = [(p[i], p[i + 1]) for i in range(0, len(p), 2)]
            for px, py in pts:
                px += dx
                py += dy
                if px < -tol or px > fig.width + tol or py < -tol \
                        or py > fig.height + tol:
                    bad.append((name, cls, round(px, 1), round(py, 1)))
                    break
    walk(fig)
    return bad


def check_all():
    """Draw every figure and report anything outside its frame."""
    bad = []
    for nm in sorted(n for n in globals() if n.startswith("fig_")):
        try:
            bad += bounds_report(globals()[nm](), nm)
        except Exception as exc:                              # noqa: BLE001
            bad.append((nm, "EXCEPTION", str(exc)[:60], ""))
    return bad
