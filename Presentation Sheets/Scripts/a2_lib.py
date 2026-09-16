"""
a2_lib.py  --  A2 presentation-sheet library for the structural reinforcement
sheets STR006 and STR007.

SHEET STANDARD -- measured off the supplied Revit A2 set (ARCH001..ARCH005,
"Project1.pdf") so that STR006 / STR007 sit in the SAME SERIES and read with the
same layout and the same feel.  Every constant below was extracted from the
vector content of that PDF, not estimated:

    A2 landscape 594 x 420 mm, drawn in PAPER MILLIMETRES, plot 1:1
    outer border          27.0 , 19.1   ->  567.0 , 400.9
    inner frame           38.8 , 30.9   ->  555.2 , 389.1
    title-block divider   x = 464.3, full height of the inner frame
    title-block panels    x 467.0 .. 552.4, four stacked boxes
        A  314.5 .. 386.4   identity block, with a rule at 332.7 and the
                            "NOTES" caption under it
        B  193.4 .. 311.8   numbered general notes
        C  130.3 .. 190.6   drawing title, large bold, centred
        D   33.6 .. 128.2   project / sheet data, rules at
                            40.9  54.6  61.8  69.1  76.4  83.6  96.9
    drawing region        x 38.8 .. 464.3 , y 30.9 .. 389.1

COLOUR POLICY -- the whole package is deliberately DARK.  Only four ACI colours
are used and every one of them plots dark on white paper:
    7  black       all line work, text, dimensions, tables, title block
    8  dark grey   hatching, soil, and work beyond the cut plane
    1  dark red    MAIN reinforcement only
    5  dark blue   links, stirrups and distribution steel only
No yellow, no cyan, no bright green, no light grey appears anywhere.

SOURCE OF TRUTH for everything drawn:  master/MASTER_PROJECT_STATE.md
Parts A.3, A.4, A.5, A.7, B and F, and the bar marks in
"Structural CAD/Scripts/rebar_data.py".
"""
import math
import ezdxf
from ezdxf.enums import TextEntityAlignment
from ezdxf import const
from ezdxf.fonts import fonts as _fonts

DXFVERSION = "AC1024"                     # AutoCAD 2010 -- native DIMENSION etc.
FONT = "OpenSans-Regular.ttf"
STYLE = "OpenSans"

# ------------------------------------------------------------- sheet geometry
SHEET_W, SHEET_H = 594.0, 420.0
OUT = (27.0, 19.1, 567.0, 400.9)          # outer border
INN = (38.8, 30.9, 555.2, 389.1)          # inner frame
TB_DIV = 464.3                            # title-block column divider
TBL, TBR = 467.0, 552.4                   # title-block panel left / right
BOX_A = (314.5, 386.4)
A_RULE = 332.7
BOX_B = (193.4, 311.8)
BOX_C = (130.3, 190.6)
BOX_D = (33.6, 128.2)
D_RULES = (40.9, 54.6, 61.8, 69.1, 76.4, 83.6, 96.9)

# drawing region actually available to the views
DR = (INN[0] + 4.0, INN[1] + 4.0, TB_DIV - 4.0, INN[3] - 4.0)   # 42.8 .. 460.3

# ----------------------------------------------------------------- text sizes
TXT = dict(tb_big=7.0, tb_row=3.2, tb_note=2.9, tb_ident=2.9,
           view_title=5.4, view_scale=3.3,
           tbl_title=3.8, tbl_head=2.3, tbl_body=2.1,
           panel_head=2.8, panel_body=2.05,
           note=2.1, mark=2.0, dim=2.0, small=1.8)
MIN_TXT_H = 1.7                           # nothing smaller goes on the sheet

# ---------------------------------------------------------------- layer table
# name: (aci colour, lineweight 1/100 mm, description)
LAYERS = {
    "S-CONCRETE":      (7, 50, "Structural concrete, cut"),
    "S-CONCRETE-THIN": (7, 25, "Concrete outlines, uncut"),
    "S-HIDDEN":        (8, 18, "Concrete and features beyond / below"),
    "S-REBAR-MAIN":    (1, 35, "Main reinforcement"),
    "S-REBAR-DIST":    (5, 25, "Distribution reinforcement"),
    "S-REBAR-STIRRUP": (5, 25, "Links and stirrups"),
    "S-REBAR-SEC":     (1, 25, "Trimmers, jamb bars, starters, additional bars"),
    "S-DIM":           (7, 13, "Dimensions"),
    "S-TEXT":          (7, 18, "General annotation"),
    "S-NOTE":          (7, 18, "Note panels"),
    "S-CALLOUT":       (7, 18, "Bar-mark tags and leaders"),
    "S-SECTION":       (7, 35, "Section and detail markers"),
    "S-GRID":          (7, 13, "Grid lines and bubbles"),
    "S-CENTER":        (7, 13, "Centrelines and void diagonals"),
    "S-HATCH":         (8, 13, "Section hatch"),
    "S-TITLE":         (7, 35, "Border, title block, view titles"),
    "S-EXISTING":      (8, 13, "Soil, rock, fill and cover build-up"),
    "S-WATERPROOF":    (7, 25, "Tanking, waterstops, groundwater table"),
    "S-LEVEL":         (7, 18, "Level markers"),
    "S-TABLE":         (7, 18, "Tables and schedules"),
}

_FCACHE = {}


def tw(s, h, font=FONT):
    """Rendered width of `s` at height `h`, in paper millimetres."""
    if not s:
        return 0.0
    f = _FCACHE.get((font, h))
    if f is None:
        f = _FCACHE[(font, h)] = _fonts.make_font(font, h)
    return f.text_width(str(s))


def fit_h(strings, avail, h, floor=MIN_TXT_H):
    """Largest height <= h at which every string fits inside `avail` mm."""
    need = max([tw(s, h) for s in strings] or [0.0])
    if need <= avail or need <= 0:
        return h
    return max(floor, h * avail / need)


def vw(scale, ox, oy):
    """Return P(model_x, model_y) -> (paper_x, paper_y) for one view."""
    def P(mx, my):
        return (ox + mx / scale, oy + my / scale)
    return P


class A2Sheet:
    """One A2 structural presentation sheet in the ARCH001..ARCH005 series."""

    def __init__(self, sheet_no, drawing_no, title_lines, project_lines,
                 notes, identity, date, drawn, checked, scale_note,
                 rev_note=""):
        self.sheet_no = sheet_no            # "SHEET 06"
        self.drawing_no = drawing_no        # "STR006"
        self.title_lines = list(title_lines)
        self.project_lines = list(project_lines)
        self.notes = list(notes)
        self.identity = list(identity)
        self.date = date
        self.drawn = drawn
        self.checked = checked
        self.scale_note = scale_note
        self.rev_note = rev_note

        self.doc = ezdxf.new(DXFVERSION, setup=True)
        self.doc.header["$INSUNITS"] = 4     # millimetres
        self.doc.header["$LUNITS"] = 2
        self.doc.header["$MEASUREMENT"] = 1
        self.msp = self.doc.modelspace()
        self._layers()
        self._dimstyles()
        self._blocks()
        self.frame()
        self.titleblock()

    # ------------------------------------------------------------------ setup
    def _layers(self):
        for name, (col, lw, desc) in LAYERS.items():
            ly = self.doc.layers.add(name)
            ly.color = col
            ly.lineweight = lw
            ly.description = desc

    def _dimstyles(self):
        for nm, h, asz in (("A2-DIM", TXT["dim"], 1.4),
                           ("A2-DIM-S", TXT["small"], 1.1)):
            ds = (self.doc.dimstyles.get(nm) if nm in self.doc.dimstyles
                  else self.doc.dimstyles.add(nm))
            ds.dxf.dimtxt = h
            ds.dxf.dimasz = asz
            ds.dxf.dimexe = 1.1
            ds.dxf.dimexo = 1.0
            ds.dxf.dimgap = 0.7
            ds.dxf.dimtad = 1          # text above the dimension line
            ds.dxf.dimdec = 0          # whole millimetres
            ds.dxf.dimlwd = 13
            ds.dxf.dimlwe = 13
            ds.dxf.dimclrt = 7         # BLACK dimension text
            ds.dxf.dimclrd = 7         # BLACK dimension line
            ds.dxf.dimclre = 7         # BLACK extension lines
            ds.dxf.dimblk = "ARCHTICK"
            ds.dxf.dimtih = 0
            ds.dxf.dimtoh = 0
            ds.dxf.dimtxsty = STYLE

    def _blocks(self):
        if "A2-SECMARK" not in self.doc.blocks:
            b = self.doc.blocks.new("A2-SECMARK")
            b.add_circle((0, 0), 3.6, dxfattribs={"layer": "S-SECTION"})
        if "A2-LEVEL" not in self.doc.blocks:
            b = self.doc.blocks.new("A2-LEVEL")
            b.add_lwpolyline([(0, 0), (-1.9, 2.8), (1.9, 2.8)], close=True,
                             dxfattribs={"layer": "S-LEVEL"})
        if "A2-NORTH" not in self.doc.blocks:
            b = self.doc.blocks.new("A2-NORTH")
            b.add_circle((0, 0), 7.0, dxfattribs={"layer": "S-TITLE"})
            b.add_lwpolyline([(0, 6.0), (-2.2, -4.2), (0, -1.8), (2.2, -4.2)],
                             close=True, dxfattribs={"layer": "S-TITLE"})

    # ------------------------------------------------------------- primitives
    def line(self, p1, p2, layer="S-CONCRETE"):
        if math.dist(p1, p2) < 1e-9:
            return None
        return self.msp.add_line(p1, p2, dxfattribs={"layer": layer})

    def pline(self, pts, layer="S-CONCRETE", close=False):
        pts = [p for i, p in enumerate(pts)
               if i == 0 or math.dist(p, pts[i - 1]) > 1e-9]
        if len(pts) < 2:
            return None
        return self.msp.add_lwpolyline(pts, close=close, dxfattribs={"layer": layer})

    def rect(self, x0, y0, x1, y1, layer="S-CONCRETE"):
        return self.pline([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], layer, True)

    def circle(self, c, r, layer="S-CONCRETE"):
        if r <= 1e-9:
            return None
        return self.msp.add_circle(c, r, dxfattribs={"layer": layer})

    def arc(self, c, r, a0, a1, layer="S-CONCRETE"):
        return self.msp.add_arc(c, r, a0, a1, dxfattribs={"layer": layer})

    def dline(self, p1, p2, layer="S-HIDDEN", dash=1.8, gap=1.2):
        """Dashed line drawn as explicit segments -- plots identically anywhere."""
        L = math.dist(p1, p2)
        if L < 1e-9:
            return
        ux, uy = (p2[0] - p1[0]) / L, (p2[1] - p1[1]) / L
        t = 0.0
        while t < L:
            e = min(t + dash, L)
            self.line((p1[0] + ux * t, p1[1] + uy * t),
                      (p1[0] + ux * e, p1[1] + uy * e), layer)
            t = e + gap

    def cline(self, p1, p2, layer="S-CENTER"):
        """Long-dash / dot centreline."""
        L = math.dist(p1, p2)
        if L < 1e-9:
            return
        ux, uy = (p2[0] - p1[0]) / L, (p2[1] - p1[1]) / L
        t, long_ = 0.0, True
        while t < L:
            d = 4.0 if long_ else 0.6
            e = min(t + d, L)
            self.line((p1[0] + ux * t, p1[1] + uy * t),
                      (p1[0] + ux * e, p1[1] + uy * e), layer)
            t = e + 1.2
            long_ = not long_

    ALIGN = {"L": TextEntityAlignment.LEFT,
             "C": TextEntityAlignment.MIDDLE_CENTER,
             "R": TextEntityAlignment.RIGHT,
             "BC": TextEntityAlignment.BOTTOM_CENTER,
             "ML": TextEntityAlignment.MIDDLE_LEFT,
             "MR": TextEntityAlignment.MIDDLE_RIGHT}

    def text(self, s, p, h=None, layer="S-TEXT", align="L", rot=0.0):
        h = h or TXT["note"]
        t = self.msp.add_text(str(s), height=h, rotation=rot,
                              dxfattribs={"layer": layer, "style": STYLE})
        t.set_placement(p, align=self.ALIGN[align])
        return t

    # ------------------------------------------------------------- dimensions
    def dim_h(self, p1, p2, ybase, sc=1.0, style="A2-DIM", ov=None):
        """Horizontal dimension.  Geometry is in paper mm, so dimlfac = the view
        scale makes the text read MODEL millimetres."""
        o = {"dimlfac": float(sc)}
        o.update(ov or {})
        d = self.msp.add_linear_dim(base=(0, ybase), p1=p1, p2=p2, angle=0,
                                    dimstyle=style, override=o,
                                    dxfattribs={"layer": "S-DIM"})
        d.render()
        return d

    def dim_v(self, p1, p2, xbase, sc=1.0, style="A2-DIM", ov=None):
        o = {"dimlfac": float(sc)}
        o.update(ov or {})
        d = self.msp.add_linear_dim(base=(xbase, 0), p1=p1, p2=p2, angle=90,
                                    dimstyle=style, override=o,
                                    dxfattribs={"layer": "S-DIM"})
        d.render()
        return d

    def dim_chain_h(self, xs, y, ybase, sc=1.0, style="A2-DIM", minlen=3.0):
        for a, b in zip(xs[:-1], xs[1:]):
            if abs(b - a) >= minlen:
                self.dim_h((a, y), (b, y), ybase, sc, style)

    def dim_chain_v(self, ys, x, xbase, sc=1.0, style="A2-DIM", minlen=3.0):
        for a, b in zip(ys[:-1], ys[1:]):
            if abs(b - a) >= minlen:
                self.dim_v((x, a), (x, b), xbase, sc, style)

    # -------------------------------------------------------------- rebar aids
    def bar(self, pts, layer="S-REBAR-MAIN", close=False):
        return self.pline(pts, layer, close)

    def bar_dot(self, p, r=0.65, layer="S-REBAR-MAIN"):
        """A bar seen end-on: a solid dot."""
        self.circle(p, r, layer)
        h = self.msp.add_hatch(color=LAYERS[layer][0], dxfattribs={"layer": layer})
        h.paths.add_polyline_path(
            [(p[0] + r * math.cos(a * math.pi / 8),
              p[1] + r * math.sin(a * math.pi / 8)) for a in range(16)],
            is_closed=True)

    def bar_run(self, p1, p2, spacing_mm, scale, layer="S-REBAR-MAIN", r=0.6):
        """A row of bars seen end-on, at TRUE spacing, between p1 and p2."""
        L = math.dist(p1, p2)
        step = spacing_mm / scale
        if L < 1e-6 or step <= 0:
            return 0
        n = int(L / step) + 1
        for i in range(n):
            t = i * step
            self.bar_dot((p1[0] + (p2[0] - p1[0]) * t / L,
                          p1[1] + (p2[1] - p1[1]) * t / L), r, layer)
        return n

    def bar_lines(self, p1, p2, q1, q2, spacing_mm, scale, layer="S-REBAR-MAIN"):
        """A run of bars seen along their length: parallel lines at TRUE spacing.
        The run marches from edge p1->q1 to edge p2->q2."""
        L = math.dist(p1, p2)
        step = spacing_mm / scale
        if L < 1e-6 or step <= 0:
            return 0
        n = int(L / step) + 1
        for i in range(n):
            f = (i * step) / L
            a = (p1[0] + (p2[0] - p1[0]) * f, p1[1] + (p2[1] - p1[1]) * f)
            b = (q1[0] + (q2[0] - q1[0]) * f, q1[1] + (q2[1] - q1[1]) * f)
            self.line(a, b, layer)
        return n

    def link_rect(self, x0, y0, x1, y1, layer="S-REBAR-STIRRUP", hook=1.1):
        """A closed link with 135 degree hooks, seen in section."""
        self.rect(x0, y0, x1, y1, layer)
        self.line((x1, y1), (x1 - hook, y1 - hook), layer)
        self.line((x1 - 0.45, y1), (x1 - 0.45 - hook, y1 - hook), layer)

    def tag(self, p, mark, leader_from=None, rx=4.3, ry=2.5):
        """Bar-mark tag: the ellipse tag used by the ARCH sheets, with the mark
        inside.  Every mark used here exists in rebar_data.MARKS."""
        self.msp.add_ellipse(p, major_axis=(rx, 0), ratio=ry / rx,
                             dxfattribs={"layer": "S-CALLOUT"})
        self.text(mark, p, TXT["mark"], "S-CALLOUT", "C")
        if leader_from:
            dx = -rx if leader_from[0] < p[0] else rx
            self.line(leader_from, (p[0] + dx, p[1]), "S-CALLOUT")

    def note_leader(self, pt, elbow, txt, h=None, side=None):
        """Leader with a horizontal landing and text at the far end."""
        h = h or TXT["mark"]
        right = (elbow[0] >= pt[0]) if side is None else (side == "R")
        land = 2.6 if right else -2.6
        self.line(pt, elbow, "S-CALLOUT")
        self.line(elbow, (elbow[0] + land, elbow[1]), "S-CALLOUT")
        # the leader line is a call-out, but its text is general annotation:
        # this keeps "every TEXT on S-CALLOUT is a bar mark" exactly true
        self.text(txt, (elbow[0] + land + (0.8 if right else -0.8), elbow[1]),
                  h, "S-TEXT", "ML" if right else "MR")

    # ------------------------------------------------------------------ hatch
    def hatch_pat(self, pts, pattern="ANSI31", scale=1.6, angle=0.0,
                  layer="S-HATCH", holes=None):
        h = self.msp.add_hatch(dxfattribs={"layer": layer})
        h.set_pattern_fill(pattern, scale=scale, angle=angle)
        h.paths.add_polyline_path(pts, is_closed=True,
                                  flags=const.BOUNDARY_PATH_EXTERNAL)
        for hole in (holes or []):
            h.paths.add_polyline_path(hole, is_closed=True,
                                      flags=const.BOUNDARY_PATH_OUTERMOST)
        return h

    def conc_hatch(self, pts, holes=None, scale=1.3):
        return self.hatch_pat(pts, "ANSI31", scale, 0.0, "S-HATCH", holes)

    def soil_hatch(self, pts, scale=1.1):
        return self.hatch_pat(pts, "EARTH", scale, 0.0, "S-EXISTING")

    def rock_hatch(self, pts, scale=1.4):
        return self.hatch_pat(pts, "ANSI37", scale, 0.0, "S-EXISTING")

    # ------------------------------------------------------------- annotation
    def view_title(self, x, y, tag, title, scale_note, rule_to):
        """The ARCH-series view title: numbered bubble, title, rule, scale.
        QA: both lines are shrunk to the width actually available, so a title
        can never run out of its column and across the next one."""
        r = 4.0
        self.circle((x + r, y + 2.0), r, "S-TITLE")
        self.text(tag, (x + r, y + 2.0), TXT["view_title"] * 0.68, "S-TITLE", "C")
        tx = x + 2 * r + 4.2
        avail = rule_to - tx
        th = fit_h([title], avail, TXT["view_title"], floor=3.2)
        sh = fit_h([scale_note], avail, TXT["view_scale"], floor=2.2)
        self.text(title, (tx, y + 3.0), th, "S-TITLE")
        self.line((x + 2 * r + 1.6, y + 1.6), (rule_to, y + 1.6), "S-TITLE")
        self.text(scale_note, (tx, y - 4.6), sh, "S-TEXT")

    def secmark(self, p, label, direction="R", size=3.6):
        """Section mark: bubble, label, and a tail showing the view direction."""
        self.msp.add_blockref("A2-SECMARK", p, dxfattribs={"layer": "S-SECTION"})
        self.text(label, p, TXT["mark"], "S-SECTION", "C")
        d = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}[direction]
        self.line((p[0] + d[0] * size, p[1] + d[1] * size),
                  (p[0] + d[0] * (size + 2.6), p[1] + d[1] * (size + 2.6)),
                  "S-SECTION")

    def level(self, p, txt, side="R", dy=3.6):
        self.msp.add_blockref("A2-LEVEL", p, dxfattribs={"layer": "S-LEVEL"})
        dx = 2.6 if side == "R" else -2.6
        self.text(txt, (p[0] + dx, p[1] + dy), TXT["small"], "S-LEVEL",
                  "ML" if side == "R" else "MR")

    def north(self, p):
        self.msp.add_blockref("A2-NORTH", p, dxfattribs={"layer": "S-TITLE"})
        self.text("N", (p[0], p[1] + 9.6), TXT["small"], "S-TITLE", "BC")

    # ----------------------------------------------------------------- tables
    def table(self, x, y_top, total_w, rows, title=None, header=None,
              rh=4.0, hh=None, body_h=None, head_h=None, align=None):
        """Draw a ruled table that is GUARANTEED to fit `total_w`.

        Column widths are not guessed: every cell is measured with the same
        font metrics ezdxf places it with, the text height is reduced until the
        widest row fits, and the remaining width is shared out in proportion to
        what each column actually needs.  A row that is a bare string is a
        full-width sub-heading band.  Returns the y of the bottom rule.
        """
        body_h = body_h or TXT["tbl_body"]
        head_h = head_h or TXT["tbl_head"]
        data = [r for r in rows if not isinstance(r, str)]
        bands = [r for r in rows if isinstance(r, str)]
        ncol = len(header) if header else max(len(r) for r in data)
        align = align or (["L"] * ncol)
        hh = hh or rh

        def needs(bh, hd):
            out = []
            for j in range(ncol):
                w = max([tw(str(r[j]), bh) for r in data if j < len(r)] or [0.0])
                if header:
                    w = max(w, tw(str(header[j]), hd))
                out.append(w + 2.8)
            return out

        while True:
            n = needs(body_h, head_h)
            band_ok = all(tw(b, head_h) + 3.2 <= total_w for b in bands)
            if (sum(n) <= total_w and band_ok) or body_h <= MIN_TXT_H:
                break
            body_h = round(body_h - 0.05, 2)
            head_h = max(MIN_TXT_H, round(head_h - 0.05, 2))
        n = needs(body_h, head_h)
        colw = [v * total_w / sum(n) for v in n]

        W, y = total_w, y_top
        if title:
            th = fit_h([title], W - 3.0, TXT["tbl_title"])
            self.rect(x, y - th - 2.6, x + W, y, "S-TABLE")
            self.text(title, (x + W / 2, y - th / 2 - 1.3), th, "S-TABLE", "C")
            y -= th + 2.6

        if header:
            self.rect(x, y - hh, x + W, y, "S-TABLE")
            cx = x
            for j, w in enumerate(colw):
                if j:
                    self.line((cx, y - hh), (cx, y), "S-TABLE")
                self.text(str(header[j]), (cx + w / 2, y - hh / 2), head_h,
                          "S-TABLE", "C")
                cx += w
            y -= hh

        for r in rows:
            if isinstance(r, str):                      # full-width sub-heading
                self.rect(x, y - rh, x + W, y, "S-TABLE")
                self.text(r, (x + 1.6, y - rh / 2), head_h, "S-TABLE", "ML")
                y -= rh
                continue
            self.rect(x, y - rh, x + W, y, "S-TABLE")
            cx = x
            for j, w in enumerate(colw):
                if j:
                    self.line((cx, y - rh), (cx, y), "S-TABLE")
                sv = str(r[j]) if j < len(r) else ""
                if align[j] == "C":
                    self.text(sv, (cx + w / 2, y - rh / 2), body_h, "S-TABLE", "C")
                elif align[j] == "R":
                    self.text(sv, (cx + w - 1.4, y - rh / 2), body_h, "S-TABLE", "MR")
                else:
                    self.text(sv, (cx + 1.4, y - rh / 2), body_h, "S-TABLE", "ML")
                cx += w
            y -= rh
        return y

    def table_stack(self, x, y_top, y_bot, w, specs, gap=8.0, rh_max=8.0,
                    body_max=3.2):
        """Draw a stack of tables that fills `y_top` .. `y_bot` EXACTLY.

        Added at SR2A, when the two note panels were deleted from STR008 and
        STR009 and the schedules became the whole right-hand column.  The row
        height is solved for, not guessed: it is whatever makes the stack end on
        `y_bot`, capped at `rh_max` so a short stack cannot turn into a poster.
        Any height the cap leaves over is shared out between the tables as gap.
        Body text grows with the row and is then shrunk by `table()` until it
        fits its column, so a wider row can never push text out of a cell.
        """
        n = sum(len(sp["rows"]) + (1 if sp.get("header") else 0) for sp in specs)
        th = sum(fit_h([sp["title"]], w - 3.0, TXT["tbl_title"]) + 2.6
                 for sp in specs if sp.get("title"))
        ngap = max(len(specs) - 1, 0)
        span = y_top - y_bot
        rh = (span - th - gap * ngap) / max(n, 1)
        if rh > rh_max:
            rh = rh_max
            gap = (span - th - n * rh) / ngap if ngap else 0.0
        body_h = min(body_max, max(TXT["tbl_body"], rh * 0.40))
        y = y_top
        for i, sp in enumerate(specs):
            y = self.table(x, y, w, sp["rows"], title=sp.get("title"),
                           header=sp.get("header"), rh=rh,
                           body_h=sp.get("body_h", body_h),
                           head_h=sp.get("head_h", body_h + 0.2),
                           align=sp.get("align"))
            if i < len(specs) - 1:
                y -= gap
        return y

    def panel(self, x, y_top, w, heading, lines, lead=3.1, h=None, box=True,
              max_h=None):
        """A boxed note panel.  Returns the y of the bottom edge."""
        h = h or TXT["panel_body"]
        h = min(h, fit_h(lines, w - 4.0, h))
        hh = TXT["panel_head"]
        n = len(lines)
        if max_h:
            room = max_h - (4.4 + hh + 2.4)
            if n * lead > room:
                lead = max(1.9, room / max(n, 1))
                h = min(h, lead * 0.66)
        H = 4.4 + hh + 2.4 + n * lead
        if box:
            self.rect(x, y_top - H, x + w, y_top, "S-TABLE")
            self.line((x, y_top - hh - 3.6), (x + w, y_top - hh - 3.6), "S-TABLE")
        self.text(heading, (x + 2.0, y_top - hh - 1.4), hh, "S-TITLE", "L")
        y = y_top - hh - 3.6 - 3.0
        for ln in lines:
            self.text(ln, (x + 2.0, y), h, "S-NOTE", "L")
            y -= lead
        return y_top - H

    # ------------------------------------------------------ border + titleblock
    def frame(self):
        self.rect(*OUT, "S-TITLE")
        self.rect(*INN, "S-TITLE")
        self.line((TB_DIV, INN[1]), (TB_DIV, INN[3]), "S-TITLE")

    def titleblock(self):
        T = "S-TITLE"
        W = TBR - TBL
        cx = (TBL + TBR) / 2

        # --- box A : identity, with the NOTES caption under the rule
        self.rect(TBL, BOX_A[0], TBR, BOX_A[1], T)
        self.line((TBL, A_RULE), (TBR, A_RULE), T)
        ih = fit_h(self.identity, W - 6.0, TXT["tb_ident"])
        y = A_RULE + (BOX_A[1] - A_RULE) / 2 + (len(self.identity) - 1) * 2.2
        for ln in self.identity:
            self.text(ln, (cx, y), ih if ln.isupper() else ih * 0.92, T, "C")
            y -= 4.4
        self.text("NOTES", (cx, (A_RULE + BOX_A[0]) / 2), TXT["tb_note"] * 1.15,
                  T, "C")

        # --- box B : numbered general notes.  QA: the list is re-wrapped at a
        # smaller height until it FITS the box - it may never run out of it.
        self.rect(TBL, BOX_B[0], TBR, BOX_B[1], T)
        nx, tx = TBL + 8.0, TBL + 19.0
        avail = (BOX_B[1] - BOX_B[0]) - 9.0
        nh = TXT["tb_note"]
        while True:
            wrapped = []
            for i, note in enumerate(self.notes, 1):
                for k, ln in enumerate(self._wrap(note, TBR - tx - 3.0, nh)):
                    wrapped.append((f"{i}." if k == 0 else "", ln))
            lead = nh * 1.43
            if len(wrapped) * lead <= avail or nh <= MIN_TXT_H:
                break
            nh = round(nh - 0.05, 2)
        y = BOX_B[1] - 6.0
        for num, ln in wrapped:
            if num:
                self.text(num, (nx, y), nh, "S-NOTE", "L")
            self.text(ln, (tx, y), nh, "S-NOTE", "L")
            y -= lead

        # --- box C : drawing title
        self.rect(TBL, BOX_C[0], TBR, BOX_C[1], T)
        th = fit_h(self.title_lines, W - 5.0, TXT["tb_big"])
        th = min(th, (BOX_C[1] - BOX_C[0] - 6.0) / (len(self.title_lines) * 1.30))
        lead = th * 1.30
        y = (BOX_C[0] + BOX_C[1]) / 2 + (len(self.title_lines) - 1) * lead / 2
        for ln in self.title_lines:
            self.text(ln, (cx, y), th, T, "C")
            y -= lead

        # --- box D : project / sheet data
        self.rect(TBL, BOX_D[0], TBR, BOX_D[1], T)
        for yr in D_RULES:
            self.line((TBL, yr), (TBR, yr), T)

        ph = fit_h(self.project_lines, W - 5.0, TXT["tb_big"] * 0.94)
        ph = min(ph, (BOX_D[1] - D_RULES[6] - 5.0) / (len(self.project_lines) * 1.30))
        y = (D_RULES[6] + BOX_D[1]) / 2 + (len(self.project_lines) - 1) * ph * 0.65
        for ln in self.project_lines:
            self.text(ln, (cx, y), ph, T, "C")
            y -= ph * 1.30

        self.text(self.sheet_no, (cx, (D_RULES[5] + D_RULES[6]) / 2),
                  TXT["tb_big"], T, "C")
        self.text(self.drawing_no, (cx, (D_RULES[0] + D_RULES[1]) / 2),
                  TXT["tb_big"], T, "C")

        rows = [(D_RULES[4], D_RULES[5], "Project number", "01"),
                (D_RULES[3], D_RULES[4], "Date", self.date),
                (D_RULES[2], D_RULES[3], "Drawn by", self.drawn),
                (D_RULES[1], D_RULES[2], "Checked by", self.checked),
                (BOX_D[0], D_RULES[0], "Scale", self.scale_note)]
        rh = TXT["tb_row"]
        for y0, y1, lab, val in rows:
            ym = (y0 + y1) / 2
            self.text(lab, (TBL + 4.0, ym), rh, T, "ML")
            vh = min(rh, fit_h([val], W - 10.0 - tw(lab, rh), rh))
            self.text(val, (TBR - 4.0, ym), vh, T, "MR")

        # --- the rotated stamp the ARCH sheets carry outside the frame
        if self.rev_note:
            self.text(self.rev_note, (562.0, BOX_D[0]), TXT["tb_note"], T,
                      "L", rot=90.0)

    @staticmethod
    def _wrap(s, width, h):
        out, cur = [], ""
        for w in s.split():
            t = (cur + " " + w).strip()
            if tw(t, h) <= width or not cur:
                cur = t
            else:
                out.append(cur)
                cur = w
        if cur:
            out.append(cur)
        return out

    # ------------------------------------------------------------------- save
    def save(self, path):
        self.doc.saveas(path)
        return path
