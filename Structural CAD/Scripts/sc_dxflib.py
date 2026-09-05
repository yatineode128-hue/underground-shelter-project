"""
sc_dxflib.py  --  professional structural-CAD sheet library for the R-series
reinforcement drawings.

Built on ezdxf, writing AutoCAD 2010 (AC1024) ASCII DXF so that the sheets carry
NATIVE editable entities: LINE, LWPOLYLINE, ARC, CIRCLE, TEXT, MTEXT, DIMENSION,
LEADER, HATCH and BLOCK / INSERT.  Nothing is rasterised, flattened or faked.

DECLARED DEVIATION X1: master E.3.1 fixes AutoCAD R12 ASCII for output sheets
S-01..S-08.  Those sheets are NOT touched by this package.  The R-series needs
real DIMENSION / MTEXT / HATCH / LEADER entities (brief section 25), which R12
does not carry usefully, so the R-series is written at AC1024.  Recorded in
Documentation/02_CAD_STANDARDS.md and in the QA/QC report.

DECLARED DEVIATION X2: layer names follow the brief's S-* system.  A one-to-one
mapping to the master's 22-layer table is in Documentation/02_CAD_STANDARDS.md.

SHEET STANDARD
    A1, 841 x 594 mm, drawn in PAPER MILLIMETRES, plot 1:1
    border outer 0,0-841,594  ;  inner 10,10-831,584
    title block 180 x 100 at x0 = 651, y0 = 10
    every view carries its own scale note; paper = origin + model / scale
"""
import math
import ezdxf
from ezdxf.enums import TextEntityAlignment
from ezdxf import const

DXFVERSION = "AC1024"          # AutoCAD 2010

SHEET_W, SHEET_H = 841.0, 594.0
IN_L, IN_B, IN_R, IN_T = 10.0, 10.0, 831.0, 584.0
TB_X, TB_Y, TB_W, TB_H = 651.0, 10.0, 180.0, 100.0

# ------------------------------------------------------------------- text sizes
TXT = dict(sheet_title=5.0, view_title=3.5, panel_head=2.5, detail_label=2.4,
           note=2.0, bar_mark=2.0, rebar=1.8, dim=1.8, table=1.6, small=1.4)

# ------------------------------------------------------- layers  (brief sect 26)
# name: (aci colour, lineweight 1/100 mm, description, master 22-layer equivalent)
LAYERS = {
    "S-CONCRETE":      (7,  50, "Structural concrete outlines (cut)",      "CONC"),
    "S-CONCRETE-THIN": (7,  25, "Concrete beyond the cut plane",           "CONC"),
    "S-HIDDEN":        (8,  18, "Concrete / features beyond, hidden",      "CONC-HIDDEN"),
    "S-REBAR-MAIN":    (1,  35, "Main reinforcement",                      "REINF-MAIN"),
    "S-REBAR-DIST":    (3,  25, "Distribution reinforcement",              "REINF-DIST"),
    "S-REBAR-STIRRUP": (6,  25, "Links and stirrups",                      "REINF-LINK"),
    "S-REBAR-TIE":     (6,  25, "Ties, cross-ties, starters",              "REINF-LINK"),
    "S-REBAR-SEC":     (4,  25, "Trimmers, secondary and additional bars",  "REINF-SEC"),
    "S-DIM":           (4,  13, "Dimensions",                              "DIM"),
    "S-TEXT":          (7,  18, "General annotation",                      "TEXT"),
    "S-NOTE":          (7,  18, "Note panels",                             "NOTES"),
    "S-CALLOUT":       (2,  18, "Bar-mark balloons and leaders",           "DIM"),
    "S-SECTION":       (1,  35, "Section and detail markers",              "DIM"),
    "S-GRID":          (5,  13, "Grid lines and bubbles",                  "GRID"),
    "S-CENTER":        (6,  13, "Centrelines",                             "CENTRELINE"),
    "S-HATCH":         (8,  13, "Section hatch",                           "HATCH"),
    "S-TITLE":         (7,  35, "Border, title block, view titles",        "TITLEBLOCK"),
    "S-EXISTING":      (8,  13, "Soil, rock, berm, cover layers",          "SOIL"),
    "S-REFERENCE":     (8,  13, "Reference geometry, extents",             "CONC-HIDDEN"),
    "S-WATERPROOF":    (30, 25, "Membranes, waterstops, GWT",              "WATERPROOF"),
    "S-STEELWORK":     (2,  25, "Cast-in frames, EMP straps, steel items", "STEELWORK"),
    "S-LEVEL":         (4,  18, "Level markers",                           "LEVELS"),
    "S-TABLE":         (7,  18, "Tables and schedules",                    "TABLE"),
    "S-BLAST":         (1,  35, "Blast arrows, findings, warnings",        "BLAST"),
}

STYLES = {"ISOSTD": "isocp.shx", "ISOBOLD": "isocpeur.ttf"}


def vw(scale, ox, oy):
    """Return P(model_x, model_y) -> (paper_x, paper_y) for one view."""
    def P(mx, my):
        return (ox + mx / scale, oy + my / scale)
    return P


class Sheet:
    """One A1 reinforcement drawing."""

    def __init__(self, number, title, subtitle="", status="FOR REVIEW - NOT FOR CONSTRUCTION",
                 rev="SC1", flags=()):
        self.number = number
        self.title = title
        self.subtitle = subtitle
        self.status = status
        self.rev = rev
        self.flags = list(flags)
        self.doc = ezdxf.new(DXFVERSION, setup=True)
        self.doc.header["$INSUNITS"] = 4          # millimetres
        self.doc.header["$LUNITS"] = 2            # decimal
        self.doc.header["$MEASUREMENT"] = 1       # metric
        self.msp = self.doc.modelspace()
        self._layers()
        self._dimstyles()
        self._blocks()
        self.border()

    # ------------------------------------------------------------- setup
    def _layers(self):
        for name, (col, lw, desc, _master) in LAYERS.items():
            ly = self.doc.layers.add(name)
            ly.color = col
            ly.lineweight = lw
            ly.description = desc

    def _dimstyles(self):
        for nm, h, asz in (("SC-DIM", TXT["dim"], 1.6), ("SC-DIM-S", TXT["small"], 1.2)):
            if nm in self.doc.dimstyles:
                ds = self.doc.dimstyles.get(nm)
            else:
                ds = self.doc.dimstyles.add(nm)
            ds.dxf.dimtxt = h        # text height
            ds.dxf.dimasz = asz      # arrow size
            ds.dxf.dimexe = 1.2      # extension beyond dim line
            ds.dxf.dimexo = 1.0      # extension line offset from origin
            ds.dxf.dimgap = 0.8
            ds.dxf.dimtad = 1        # text above the dimension line
            ds.dxf.dimdec = 0        # whole millimetres
            ds.dxf.dimlwd = 13
            ds.dxf.dimlwe = 13
            ds.dxf.dimclrt = 4
            ds.dxf.dimclrd = 4
            ds.dxf.dimclre = 4
            ds.dxf.dimblk = "ARCHTICK"
            ds.dxf.dimtih = 0
            ds.dxf.dimtoh = 0

    def _blocks(self):
        """Reusable symbol blocks: bar-mark balloon, section mark, level, north."""
        if "BARMARK" not in self.doc.blocks:
            b = self.doc.blocks.new("BARMARK")
            b.add_circle((0, 0), 3.2, dxfattribs={"layer": "S-CALLOUT"})
        if "SECMARK" not in self.doc.blocks:
            b = self.doc.blocks.new("SECMARK")
            b.add_circle((0, 0), 4.0, dxfattribs={"layer": "S-SECTION"})
            b.add_line((-4, 0), (4, 0), dxfattribs={"layer": "S-SECTION"})
        if "LEVELMK" not in self.doc.blocks:
            b = self.doc.blocks.new("LEVELMK")
            b.add_lwpolyline([(0, 0), (-2.0, 3.0), (2.0, 3.0), (0, 0)],
                             close=True, dxfattribs={"layer": "S-LEVEL"})
        if "NORTH" not in self.doc.blocks:
            b = self.doc.blocks.new("NORTH")
            b.add_lwpolyline([(0, 10), (-3.2, -6), (0, -2.4), (3.2, -6), (0, 10)],
                             close=True, dxfattribs={"layer": "S-TITLE"})
            b.add_circle((0, 0), 12.0, dxfattribs={"layer": "S-TITLE"})

    # -------------------------------------------------------- primitives
    def line(self, p1, p2, layer="S-CONCRETE"):
        if abs(p1[0] - p2[0]) < 1e-9 and abs(p1[1] - p2[1]) < 1e-9:
            return None                     # never emit zero-length geometry
        return self.msp.add_line(p1, p2, dxfattribs={"layer": layer})

    def pline(self, pts, layer="S-CONCRETE", close=False):
        pts = [p for i, p in enumerate(pts)
               if i == 0 or math.dist(p, pts[i - 1]) > 1e-9]
        if len(pts) < 2:
            return None
        return self.msp.add_lwpolyline(pts, close=close, dxfattribs={"layer": layer})

    def rect(self, x0, y0, x1, y1, layer="S-CONCRETE"):
        return self.pline([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], layer, close=True)

    def circle(self, c, r, layer="S-CONCRETE"):
        if r <= 1e-9:
            return None
        return self.msp.add_circle(c, r, dxfattribs={"layer": layer})

    def arc(self, c, r, a0, a1, layer="S-CONCRETE"):
        return self.msp.add_arc(c, r, a0, a1, dxfattribs={"layer": layer})

    def dline(self, p1, p2, layer="S-HIDDEN", dash=2.0, gap=1.4):
        """Dashed line drawn as explicit segments - maximum viewer compatibility."""
        L = math.dist(p1, p2)
        if L < 1e-9:
            return
        ux, uy = (p2[0] - p1[0]) / L, (p2[1] - p1[1]) / L
        s = 0.0
        while s < L:
            e = min(s + dash, L)
            self.line((p1[0] + ux * s, p1[1] + uy * s),
                      (p1[0] + ux * e, p1[1] + uy * e), layer)
            s = e + gap

    def cline(self, p1, p2, layer="S-CENTER"):
        """Chain (centre) line: long-dash short-dash."""
        L = math.dist(p1, p2)
        if L < 1e-9:
            return
        ux, uy = (p2[0] - p1[0]) / L, (p2[1] - p1[1]) / L
        s, long_on = 0.0, True
        while s < L:
            seg = 6.0 if long_on else 1.0
            e = min(s + seg, L)
            self.line((p1[0] + ux * s, p1[1] + uy * s),
                      (p1[0] + ux * e, p1[1] + uy * e), layer)
            s = e + 1.6
            long_on = not long_on

    def text(self, s, p, h=None, layer="S-TEXT", align="LEFT", rot=0.0):
        h = h or TXT["note"]
        t = self.msp.add_text(s, height=h, rotation=rot,
                              dxfattribs={"layer": layer, "style": "OpenSans"})
        amap = {"LEFT": TextEntityAlignment.LEFT,
                "CENTER": TextEntityAlignment.MIDDLE_CENTER,
                "RIGHT": TextEntityAlignment.RIGHT,
                "BC": TextEntityAlignment.BOTTOM_CENTER,
                "ML": TextEntityAlignment.MIDDLE_LEFT}
        t.set_placement(p, align=amap[align])
        return t

    def mtext(self, s, p, w, h=None, layer="S-NOTE"):
        h = h or TXT["note"]
        m = self.msp.add_mtext(s, dxfattribs={"layer": layer, "char_height": h,
                                              "width": w, "style": "OpenSans"})
        m.set_location(p, attachment_point=1)     # top-left
        return m

    # ------------------------------------------------------- dimensions
    def dim_h(self, p1, p2, ybase, sc=1.0, style="SC-DIM", override=None):
        """Horizontal dimension.  `sc` is the VIEW SCALE: geometry is drawn in
        paper mm, so dimlfac = sc makes the text read MODEL millimetres."""
        ov = {"dimlfac": float(sc)}
        ov.update(override or {})
        d = self.msp.add_linear_dim(base=(0, ybase), p1=p1, p2=p2, angle=0,
                                    dimstyle=style, override=ov,
                                    dxfattribs={"layer": "S-DIM"})
        d.render()
        return d

    def dim_v(self, p1, p2, xbase, sc=1.0, style="SC-DIM", override=None):
        ov = {"dimlfac": float(sc)}
        ov.update(override or {})
        d = self.msp.add_linear_dim(base=(xbase, 0), p1=p1, p2=p2, angle=90,
                                    dimstyle=style, override=ov,
                                    dxfattribs={"layer": "S-DIM"})
        d.render()
        return d

    def dim_chain_h(self, xs, y, ybase, sc=1.0):
        for a, b in zip(xs[:-1], xs[1:]):
            if abs(b - a) > 2.0:
                self.dim_h((a, y), (b, y), ybase, sc)

    def dim_chain_v(self, ys, x, xbase, sc=1.0):
        for a, b in zip(ys[:-1], ys[1:]):
            if abs(b - a) > 2.0:
                self.dim_v((x, a), (x, b), xbase, sc)

    def leader(self, pts, text=None, h=None, layer="S-CALLOUT"):
        self.msp.add_leader(pts, dimstyle="SC-DIM", dxfattribs={"layer": layer})
        if text:
            end = pts[-1]
            dx = 1.6 if pts[-1][0] >= pts[0][0] else -1.6
            self.text(text, (end[0] + dx, end[1] - 0.6), h or TXT["rebar"],
                      layer, "LEFT" if dx > 0 else "RIGHT")

    # ------------------------------------------------------------ hatch
    def hatch_solid(self, pts, color=8, layer="S-HATCH"):
        h = self.msp.add_hatch(color=color, dxfattribs={"layer": layer})
        h.paths.add_polyline_path(pts, is_closed=True)
        return h

    def hatch_pat(self, pts, pattern="ANSI31", scale=2.0, angle=0.0,
                  layer="S-HATCH", holes=None):
        h = self.msp.add_hatch(dxfattribs={"layer": layer})
        h.set_pattern_fill(pattern, scale=scale, angle=angle)
        h.paths.add_polyline_path(pts, is_closed=True, flags=const.BOUNDARY_PATH_EXTERNAL)
        for hole in (holes or []):
            h.paths.add_polyline_path(hole, is_closed=True,
                                      flags=const.BOUNDARY_PATH_OUTERMOST)
        return h

    def concrete_hatch(self, pts, holes=None):
        return self.hatch_pat(pts, "ANSI31", 1.6, 0.0, "S-HATCH", holes)

    def soil_hatch(self, pts):
        return self.hatch_pat(pts, "EARTH", 1.2, 0.0, "S-EXISTING")

    # --------------------------------------------------------- rebar aids
    def rebar(self, pts, layer="S-REBAR-MAIN", close=False):
        return self.pline(pts, layer, close)

    def bar_dot(self, p, r=0.75, layer="S-REBAR-MAIN"):
        """A bar seen in section: a small filled circle."""
        self.circle(p, r, layer)
        h = self.msp.add_hatch(color=LAYERS[layer][0], dxfattribs={"layer": layer})
        h.paths.add_polyline_path(
            [(p[0] + r * math.cos(a), p[1] + r * math.sin(a))
             for a in [i * math.pi / 8 for i in range(16)]], is_closed=True)

    def bar_run(self, p1, p2, spacing_mm, scale, layer="S-REBAR-MAIN", r=0.7):
        """A row of bars seen in section between p1 and p2 at `spacing_mm`."""
        L = math.dist(p1, p2)
        if L < 1e-6:
            return 0
        step = spacing_mm / scale
        n = max(2, int(L / step) + 1)
        for i in range(n):
            t = i * step
            if t > L + 1e-6:
                break
            self.bar_dot((p1[0] + (p2[0] - p1[0]) * t / L,
                          p1[1] + (p2[1] - p1[1]) * t / L), r, layer)
        return n

    def barmark(self, p, mark, note=None, leader_from=None):
        """Bar-mark balloon.  `mark` MUST exist in rebar_data (checked by qa_crosscheck)."""
        self.msp.add_blockref("BARMARK", p, dxfattribs={"layer": "S-CALLOUT"})
        self.text(mark, p, TXT["bar_mark"], "S-CALLOUT", "CENTER")
        if leader_from:
            self.msp.add_leader([leader_from, p], dimstyle="SC-DIM",
                                dxfattribs={"layer": "S-CALLOUT"})
        if note:
            self.text(note, (p[0] + 4.6, p[1] - 0.7), TXT["rebar"], "S-CALLOUT")

    # --------------------------------------------------------- annotation
    def view_title(self, p, tag, title, scale_note):
        self.text(f"{tag}   {title}", p, TXT["view_title"], "S-TITLE")
        self.line((p[0], p[1] - 1.8), (p[0] + 4.2 * len(f"{tag}   {title}") * 0.55,
                                       p[1] - 1.8), "S-TITLE")
        self.text(scale_note, (p[0], p[1] - 7.2), TXT["note"], "S-TEXT")

    def secmark(self, p, label, direction="R"):
        self.msp.add_blockref("SECMARK", p, dxfattribs={"layer": "S-SECTION"})
        self.text(label, (p[0], p[1] + 1.4), TXT["note"], "S-SECTION", "CENTER")
        dx = 6.0 if direction == "R" else -6.0
        self.line((p[0] + (4 if dx > 0 else -4), p[1]), (p[0] + dx, p[1]), "S-SECTION")
        self.pline([(p[0] + dx, p[1] + 1.4), (p[0] + dx + (2.2 if dx > 0 else -2.2), p[1]),
                    (p[0] + dx, p[1] - 1.4)], "S-SECTION", close=True)

    def level(self, p, txt):
        self.msp.add_blockref("LEVELMK", p, dxfattribs={"layer": "S-LEVEL"})
        self.text(txt, (p[0] + 3.0, p[1] + 3.2), TXT["rebar"], "S-LEVEL")

    def north(self, p):
        self.msp.add_blockref("NORTH", p, dxfattribs={"layer": "S-TITLE"})
        self.text("N", (p[0], p[1] + 14.0), TXT["note"], "S-TITLE", "CENTER")

    def panel(self, x, y, w, heading, lines, h=None, lead=3.0, box=True):
        """Text panel.  Returns the y of the bottom of the panel."""
        h = h or TXT["table"]
        yy = y
        self.text(heading, (x + 2.0, yy - 3.4), TXT["panel_head"], "S-TITLE")
        yy -= 7.4
        for ln in lines:
            self.text(ln, (x + 2.0, yy), h, "S-NOTE")
            yy -= lead
        yy -= 2.0
        if box:
            self.rect(x, yy, x + w, y, "S-TITLE")
        return yy

    def table(self, x, y, colw, rows, header=None, h=None, rh=4.4, layer="S-TABLE"):
        h = h or TXT["table"]
        W = sum(colw)
        yy = y
        if header:
            self.rect(x, yy - rh, x + W, yy, layer)
            cx = x
            for w, s in zip(colw, header):
                self.text(str(s), (cx + 1.4, yy - rh + 1.3), h, layer)
                cx += w
            yy -= rh
        for r in rows:
            cx = x
            for w, s in zip(colw, r):
                self.text(str(s), (cx + 1.4, yy - rh + 1.3), h, layer)
                cx += w
            self.line((x, yy - rh), (x + W, yy - rh), layer)
            yy -= rh
        self.line((x, y), (x + W, y), layer)
        cx = x
        for w in colw:
            self.line((cx, y), (cx, yy), layer)
            cx += w
        self.line((x + W, y), (x + W, yy), layer)
        return yy

    # ------------------------------------------------------------- sheet
    def border(self):
        self.rect(0, 0, SHEET_W, SHEET_H, "S-TITLE")
        self.rect(IN_L, IN_B, IN_R, IN_T, "S-TITLE")

    def titleblock(self, designed="[PLACEHOLDER]", checked="[PLACEHOLDER]",
                   approved="[PLACEHOLDER]", scale="AS NOTED", sheet_of=""):
        import sc_proj as P
        x, y, w, h = TB_X, TB_Y, TB_W, TB_H
        self.rect(x, y, x + w, y + h, "S-TITLE")
        for yy in (20, 32, 44, 56, 78):
            self.line((x, y + yy), (x + w, y + yy), "S-TITLE")
        # band 0-20  drawing number / revision / sheet
        self.line((x + 112, y), (x + 112, y + 20), "S-TITLE")
        self.line((x + 146, y), (x + 146, y + 20), "S-TITLE")
        self.text("DRAWING No.", (x + 2, y + 14.6), TXT["small"], "S-TITLE")
        self.text(self.number, (x + 22, y + 4.2), TXT["view_title"], "S-TITLE")
        self.text("REV", (x + 114, y + 14.6), TXT["small"], "S-TITLE")
        self.text(self.rev, (x + 118, y + 4.2), TXT["view_title"], "S-TITLE")
        self.text("SHEET", (x + 148, y + 14.6), TXT["small"], "S-TITLE")
        self.text(sheet_of or "-", (x + 148, y + 5.0), TXT["table"], "S-TITLE")
        # band 20-32  scale / date
        self.line((x + 96, y + 20), (x + 96, y + 32), "S-TITLE")
        self.text(f"SCALE   {scale}", (x + 2, y + 24.4), TXT["table"], "S-TITLE")
        self.text(f"DATE   {P.PACKAGE_DATE}", (x + 98, y + 24.4), TXT["table"], "S-TITLE")
        # band 32-44  signatures
        self.text(f"DESIGNED  {designed}", (x + 2, y + 36.4), TXT["small"], "S-TITLE")
        self.text(f"CHECKED  {checked}", (x + 62, y + 36.4), TXT["small"], "S-TITLE")
        self.text(f"APPROVED  {approved}", (x + 122, y + 36.4), TXT["small"], "S-TITLE")
        # band 44-56  status
        self.text("STATUS", (x + 2, y + 48.4), TXT["small"], "S-TITLE")
        self.text(self.status, (x + 22, y + 48.0), TXT["table"], "S-BLAST")
        # band 56-78  drawing title
        self.text("DRAWING TITLE", (x + 2, y + 73.4), TXT["small"], "S-TITLE")
        self.text(self.title, (x + 2, y + 65.4), TXT["detail_label"], "S-TITLE")
        if self.subtitle:
            self.text(self.subtitle[:74], (x + 2, y + 58.8), TXT["small"], "S-TITLE")
        # band 78-100  project
        self.text("PROJECT", (x + 2, y + 95.2), TXT["small"], "S-TITLE")
        self.text("UNDERGROUND CBRN-HARDENED BLAST-RESISTANT", (x + 2, y + 89.6),
                  TXT["table"], "S-TITLE")
        self.text("PROTECTIVE STRUCTURE  -  PUNE, MAHARASHTRA", (x + 2, y + 85.0),
                  TXT["table"], "S-TITLE")
        self.text(f"STRUCTURAL {P.STRUCT_REV}   ·   SENTRY POST NOT IN THIS PACKAGE",
                  (x + 2, y + 80.0), TXT["small"], "S-TITLE")

    def sheet_header(self, extra=None):
        """Top strip: package identity, scope exclusion and open-item flags."""
        self.text("STRUCTURAL CAD - REINFORCEMENT PACKAGE", (IN_L + 2, IN_T - 7.5),
                  TXT["sheet_title"], "S-TITLE")
        self.text(f"{self.number}   {self.title}", (IN_L + 2, IN_T - 14.5),
                  TXT["detail_label"], "S-TITLE")
        self.line((IN_L, IN_T - 17.5), (IN_R, IN_T - 17.5), "S-TITLE")
        self.text("SENTRY POST EXCLUDED FROM THIS PACKAGE", (IN_R - 2, IN_T - 7.0),
                  TXT["note"], "S-BLAST", "RIGHT")
        self.text("ALL DESIGN ACTIONS ARE MANUAL CALCULATION - NOT DIRECT STAAD OUTPUT",
                  (IN_R - 2, IN_T - 13.5), TXT["small"], "S-BLAST", "RIGHT")
        if self.flags:
            self.text("OPEN ITEMS ON THIS SHEET:  " + "  ".join(self.flags),
                      (IN_L + 2, IN_T - 22.5), TXT["small"], "S-BLAST")
        if extra:
            self.text(extra, (IN_L + 2, IN_T - 27.0), TXT["small"], "S-TEXT")

    def save(self, path):
        self.doc.saveas(path)
        return path
