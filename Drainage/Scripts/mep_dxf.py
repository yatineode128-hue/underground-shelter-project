"""
mep_dxf.py  --  shared A1 sheet library for the DRAINAGE, HVAC and SCHEDULE OF
FINISHES packages.

It does NOT re-implement a DXF writer.  It subclasses the sheet class the
Structural CAD package already uses (`Structural CAD/Scripts/sc_dxflib.py`), so
the three new packages carry the SAME sheet size, border, text heights, dimension
styles and drawing conventions as the issued R-series reinforcement drawings.
Only the title block, the top strip and the layer set are re-cut for MEP /
architectural work.

    A1, 841 x 594 mm, drawn in PAPER MILLIMETRES, plot 1:1
    border outer 0,0-841,594 ; inner 10,10-831,584
    title block 180 x 100 at x0 = 651, y0 = 10
    AutoCAD 2010 (AC1024) ASCII DXF, $INSUNITS = 4 (millimetres)
    every view carries its own scale note;  paper = origin + model / scale

Real, editable entities only: LINE, LWPOLYLINE, ARC, CIRCLE, TEXT, MTEXT,
DIMENSION, LEADER, HATCH, INSERT.  Nothing is rasterised or flattened.

THIS MODULE IS SHARED.  It lives in Drainage/Scripts because drainage is the
largest consumer; the HVAC and Schedule of Finishes generators put this
directory on sys.path rather than keeping a second copy.  One definition, three
packages.
"""
import os
import sys
import math

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "Structural CAD", "Scripts"))

import sc_dxflib as S                      # noqa: E402  the house sheet library
import mep_proj as P                       # noqa: E402

vw = S.vw
TXT = S.TXT
SHEET_W, SHEET_H = S.SHEET_W, S.SHEET_H
IN_L, IN_B, IN_R, IN_T = S.IN_L, S.IN_B, S.IN_R, S.IN_T
TB_X, TB_Y, TB_W, TB_H = S.TB_X, S.TB_Y, S.TB_W, S.TB_H

# ------------------------------------------------------------------ layers
# name: (aci colour, lineweight 1/100 mm, description)
MEP_LAYERS = {
    # background / coordination
    "M-ARCH":          (8,  13, "Architectural background, walls and slabs"),
    "M-ARCH-HIDDEN":   (8,  13, "Structure and features beyond"),
    "M-STRUCT":        (7,  35, "Structure cut by the view"),
    "M-GRID":          (5,  13, "Grid and bay reference lines"),
    # drainage
    "P-DRAIN-SOIL":    (1,  35, "Soil drainage - foul"),
    "P-DRAIN-WASTE":   (3,  30, "Waste drainage - wastewater"),
    "P-DRAIN-STORM":   (5,  30, "Storm and surface water"),
    "P-DRAIN-SEEP":    (4,  25, "Groundwater, seepage and subsoil drainage"),
    "P-DRAIN-EFF":     (6,  30, "Decon effluent - contaminated, segregated"),
    "P-DRAIN-RISING":  (2,  35, "Pumped rising main"),
    "P-DRAIN-VENT":    (8,  25, "Drainage ventilation"),
    "P-EQUIP":         (2,  35, "Pumps, tanks, chambers, plant"),
    "P-FLOW":          (1,  18, "Flow arrows and direction"),
    # HVAC
    "M-DUCT-SUPPLY":   (5,  35, "Supply air ductwork"),
    "M-DUCT-RETURN":   (3,  30, "Return air ductwork"),
    "M-DUCT-FRESH":    (4,  35, "Fresh air ductwork"),
    "M-DUCT-EXH":      (1,  30, "Exhaust air ductwork"),
    "M-DUCT-CL":       (8,  13, "Duct centrelines"),
    "M-TERMINAL":      (2,  25, "Diffusers, grilles and terminals"),
    "M-EQUIP":         (2,  35, "HVAC plant and equipment"),
    "M-DAMPER":        (6,  30, "Dampers, valves and isolation devices"),
    "M-AIRFLOW":       (1,  18, "Airflow arrows and quantities"),
    # finishes
    "A-FIN-FLOOR":     (4,  18, "Floor finish zones and tags"),
    "A-FIN-WALL":      (3,  18, "Wall finish zones and tags"),
    "A-FIN-CEIL":      (5,  18, "Ceiling and soffit finish tags"),
    "A-FIN-WET":       (30, 25, "Wet areas, tanking and falls"),
    "A-FIN-TAG":       (7,  18, "Finish tag boxes and leaders"),
    # shared annotation
    "M-WATERPROOF":    (30, 25, "Membranes, waterstops, tanking"),
    "M-LEVEL":         (4,  18, "Level and invert markers"),
    "M-DIM":           (4,  13, "Dimensions"),
    "M-TEXT":          (7,  18, "General annotation"),
    "M-NOTE":          (7,  18, "Note panels"),
    "M-TABLE":         (7,  18, "Tables and schedules"),
    "M-CALLOUT":       (2,  18, "Tags, balloons and leaders"),
    "M-SECTION":       (1,  35, "Section and detail markers"),
    "M-TITLE":         (7,  35, "Border, title block, view titles"),
    "M-HATCH":         (8,  13, "Hatching"),
    "M-EXISTING":      (8,  13, "Soil, rock, berm, cover"),
    "M-FLAG":          (1,  35, "Open items, data-required flags, warnings"),
}


class Sheet(S.Sheet):
    """One A1 MEP / architectural sheet.

    The three class attributes below were literals until FS2/CAM2 (10.09.26)
    added the FIRE AND LIFE SAFETY and SITE AND CONCEALMENT packages, which
    need their own issue date, and - for C-101 - need the sentry post IN scope
    rather than excluded from it.  The defaults are the previous literals
    exactly, so every sheet in DRAINAGE, HVAC and SCHEDULE OF FINISHES
    regenerates byte for byte unchanged.
    """

    SCOPE_NOTE = "SENTRY POST EXCLUDED FROM THIS PACKAGE"
    TB_SCOPE = "SENTRY POST NOT IN THIS PACKAGE"
    DATE = P.PACKAGE_DATE

    def __init__(self, number, title, subtitle="", package="DRAINAGE",
                 rev="DR1", status=P.STATUS, flags=(), sheet_of=""):
        self.package = package
        self.sheet_of = sheet_of
        self.TXTS = TXT
        super().__init__(number, title, subtitle=subtitle, status=status,
                         rev=rev, flags=list(flags))
        for name, (col, lw, desc) in MEP_LAYERS.items():
            ly = self.doc.layers.add(name)
            ly.color = col
            ly.lineweight = lw
            ly.description = desc
        self._mep_blocks()

    # ------------------------------------------------------------ symbols
    def _mep_blocks(self):
        b = self.doc.blocks
        if "GULLY" not in b:                       # floor gully / trapped gully
            g = b.new("GULLY")
            g.add_lwpolyline([(-2.2, -2.2), (2.2, -2.2), (2.2, 2.2), (-2.2, 2.2)],
                             close=True, dxfattribs={"layer": "P-EQUIP"})
            g.add_line((-2.2, -2.2), (2.2, 2.2), dxfattribs={"layer": "P-EQUIP"})
            g.add_line((-2.2, 2.2), (2.2, -2.2), dxfattribs={"layer": "P-EQUIP"})
        if "CHAMBER" not in b:                     # inspection chamber
            c = b.new("CHAMBER")
            c.add_lwpolyline([(-3.0, -3.0), (3.0, -3.0), (3.0, 3.0), (-3.0, 3.0)],
                             close=True, dxfattribs={"layer": "P-EQUIP"})
            c.add_circle((0, 0), 1.9, dxfattribs={"layer": "P-EQUIP"})
        if "PUMP" not in b:
            p = b.new("PUMP")
            p.add_circle((0, 0), 2.6, dxfattribs={"layer": "P-EQUIP"})
            p.add_lwpolyline([(-1.5, -1.5), (1.9, 0), (-1.5, 1.5)], close=True,
                             dxfattribs={"layer": "P-EQUIP"})
        if "CLEANOUT" not in b:
            c = b.new("CLEANOUT")
            c.add_circle((0, 0), 1.6, dxfattribs={"layer": "P-EQUIP"})
            c.add_line((0, -1.6), (0, 1.6), dxfattribs={"layer": "P-EQUIP"})
        if "NRV" not in b:                         # non-return valve
            n = b.new("NRV")
            n.add_lwpolyline([(-2.0, -1.8), (-2.0, 1.8), (2.0, 0)], close=True,
                             dxfattribs={"layer": "M-DAMPER"})
            n.add_line((2.0, -1.8), (2.0, 1.8), dxfattribs={"layer": "M-DAMPER"})
        if "VALVE" not in b:
            v = b.new("VALVE")
            v.add_lwpolyline([(-2.0, -1.8), (-2.0, 1.8), (0, 0)], close=True,
                             dxfattribs={"layer": "M-DAMPER"})
            v.add_lwpolyline([(2.0, -1.8), (2.0, 1.8), (0, 0)], close=True,
                             dxfattribs={"layer": "M-DAMPER"})
        if "DIFFUSER" not in b:
            d = b.new("DIFFUSER")
            d.add_lwpolyline([(-4.0, -4.0), (4.0, -4.0), (4.0, 4.0), (-4.0, 4.0)],
                             close=True, dxfattribs={"layer": "M-TERMINAL"})
            d.add_lwpolyline([(-2.4, -2.4), (2.4, -2.4), (2.4, 2.4), (-2.4, 2.4)],
                             close=True, dxfattribs={"layer": "M-TERMINAL"})
            for a, c in ((-4, -4), (4, -4), (4, 4), (-4, 4)):
                d.add_line((a, c), (a * 0.6, c * 0.6),
                           dxfattribs={"layer": "M-TERMINAL"})
        if "GRILLE" not in b:
            g = b.new("GRILLE")
            g.add_lwpolyline([(-4.0, -2.4), (4.0, -2.4), (4.0, 2.4), (-4.0, 2.4)],
                             close=True, dxfattribs={"layer": "M-TERMINAL"})
            for i in (-2.0, 0.0, 2.0):
                g.add_line((i, -2.4), (i, 2.4), dxfattribs={"layer": "M-TERMINAL"})
        if "BVALVE" not in b:                      # blast valve
            v = b.new("BVALVE")
            v.add_circle((0, 0), 3.0, dxfattribs={"layer": "M-DAMPER"})
            v.add_line((-3.0, 0), (3.0, 0), dxfattribs={"layer": "M-DAMPER"})
            v.add_line((-2.1, -2.1), (2.1, 2.1), dxfattribs={"layer": "M-DAMPER"})
        if "FANSYM" not in b:
            f = b.new("FANSYM")
            f.add_circle((0, 0), 3.4, dxfattribs={"layer": "M-EQUIP"})
            f.add_lwpolyline([(-2.4, -1.2), (2.4, -1.2), (0, 2.6)], close=True,
                             dxfattribs={"layer": "M-EQUIP"})
        if "FINTAG" not in b:
            t = b.new("FINTAG")
            t.add_lwpolyline([(0, 0), (16.0, 0), (16.0, 5.0), (0, 5.0)],
                             close=True, dxfattribs={"layer": "A-FIN-TAG"})
            t.add_line((0, 2.5), (16.0, 2.5), dxfattribs={"layer": "A-FIN-TAG"})
            t.add_line((8.0, 0), (8.0, 5.0), dxfattribs={"layer": "A-FIN-TAG"})

    # ---------------------------------------------------------- insertion
    def sym(self, name, p, layer=None, scale=1.0, rot=0.0):
        att = {"xscale": scale, "yscale": scale, "rotation": rot}
        if layer:
            att["layer"] = layer
        return self.msp.add_blockref(name, p, dxfattribs=att)

    def flow(self, p, ang=0.0, size=3.0, layer="P-FLOW"):
        """Single flow arrow at p, pointing at `ang` degrees."""
        a = math.radians(ang)
        ux, uy = math.cos(a), math.sin(a)
        px, py = -uy, ux
        tip = (p[0] + ux * size, p[1] + uy * size)
        self.pline([tip,
                    (p[0] - ux * size * 0.4 + px * size * 0.45,
                     p[1] - uy * size * 0.4 + py * size * 0.45),
                    (p[0] - ux * size * 0.4 - px * size * 0.45,
                     p[1] - uy * size * 0.4 - py * size * 0.45)],
                   layer, close=True)

    def pipe(self, pts, layer="P-DRAIN-WASTE", tag=None, arrow_at=0.5,
             h=None):
        """Polyline pipe run with one flow arrow and an optional tag."""
        self.pline(pts, layer)
        if len(pts) >= 2 and arrow_at is not None:
            # place the arrow on the longest leg
            best, bl = 0, -1.0
            for i in range(len(pts) - 1):
                L = math.hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1])
                if L > bl:
                    bl, best = L, i
            a, b = pts[best], pts[best + 1]
            mx = a[0] + (b[0] - a[0]) * arrow_at
            my = a[1] + (b[1] - a[1]) * arrow_at
            ang = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
            self.flow((mx, my), ang, 2.4, "P-FLOW")
            if tag:
                # QA1: the tag was offset +1.8 in Y whatever the pipe direction.
                # On a VERTICAL run that pushes the label ALONG the pipe, so a
                # long tag lay across every label beside the run.  The offset is
                # now perpendicular to the run, so the tag always sits beside it.
                if abs(b[0] - a[0]) >= abs(b[1] - a[1]):
                    # mostly horizontal run - tag reads along it, just above
                    self.text(tag, (mx, my + 1.8), h or TXT["small"], "M-CALLOUT",
                              "BC", rot=(ang if abs(ang) < 90 else ang - 180))
                else:
                    # mostly VERTICAL run - a tag rotated along the pipe sweeps a
                    # tall narrow box through every label beside the run.  Read it
                    # horizontally, set off to the side, as a callout normally is.
                    self.text(tag, (mx + 2.2, my), h or TXT["small"], "M-CALLOUT",
                              "ML")

    def duct(self, p1, p2, width, layer="M-DUCT-SUPPLY", tag=None, h=None):
        """Double-line duct between two points, `width` in paper mm."""
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        L = math.hypot(dx, dy) or 1.0
        px, py = -dy / L * width / 2.0, dx / L * width / 2.0
        self.line((p1[0] + px, p1[1] + py), (p2[0] + px, p2[1] + py), layer)
        self.line((p1[0] - px, p1[1] - py), (p2[0] - px, p2[1] - py), layer)
        self.line((p1[0], p1[1]), (p2[0], p2[1]), "M-DUCT-CL")
        ang = math.degrees(math.atan2(dy, dx))
        self.flow(((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2), ang, 2.6, "M-AIRFLOW")
        if tag:
            self.text(tag, ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2 + width / 2 + 1.4),
                      h or TXT["small"], "M-CALLOUT", "BC",
                      rot=(ang if abs(ang) < 90 else ang - 180))

    def tag(self, p, txt, layer="M-CALLOUT", h=None, w=None):
        """Boxed tag."""
        h = h or TXT["small"]
        w = w or (len(txt) * h * 0.62 + 2.4)
        self.rect(p[0], p[1], p[0] + w, p[1] + h + 1.8, layer)
        self.text(txt, (p[0] + 1.2, p[1] + 1.4), h, layer)
        return w

    def flag(self, p, txt, h=None):
        """A data-required / open-item flag, always on M-FLAG."""
        self.text(txt, p, h or TXT["small"], "M-FLAG")

    # ------------------------------------------------------------- sheet
    def sheet_header(self, extra=None):
        self.text(f"{self.package} PACKAGE", (IN_L + 2, IN_T - 7.5),
                  TXT["sheet_title"], "M-TITLE")
        self.text(f"{self.number}   {self.title}", (IN_L + 2, IN_T - 14.5),
                  TXT["detail_label"], "M-TITLE")
        self.line((IN_L, IN_T - 17.5), (IN_R, IN_T - 17.5), "M-TITLE")
        self.text(self.SCOPE_NOTE, (IN_R - 2, IN_T - 7.0),
                  TXT["note"], "M-FLAG", "RIGHT")
        self.text("DEVELOPED FOR PROJECT COORDINATION - PENDING ENGINEERING VERIFICATION",
                  (IN_R - 2, IN_T - 13.5), TXT["small"], "M-FLAG", "RIGHT")
        if self.flags:
            self.text("OPEN ITEMS ON THIS SHEET:  " + "   ".join(self.flags),
                      (IN_L + 2, IN_T - 22.5), TXT["small"], "M-FLAG")
        if extra:
            self.text(extra, (IN_L + 2, IN_T - 27.0), TXT["small"], "M-TEXT")

    def titleblock(self, designed="[PLACEHOLDER]", checked="[PLACEHOLDER]",
                   approved="[PLACEHOLDER]", scale="AS NOTED", sheet_of=""):
        x, y, w, h = TB_X, TB_Y, TB_W, TB_H
        self.rect(x, y, x + w, y + h, "M-TITLE")
        for yy in (20, 32, 44, 56, 78):
            self.line((x, y + yy), (x + w, y + yy), "M-TITLE")
        self.line((x + 112, y), (x + 112, y + 20), "M-TITLE")
        self.line((x + 146, y), (x + 146, y + 20), "M-TITLE")
        self.text("DRAWING No.", (x + 2, y + 14.6), TXT["small"], "M-TITLE")
        self.text(self.number, (x + 20, y + 4.2), TXT["view_title"], "M-TITLE")
        self.text("REV", (x + 114, y + 14.6), TXT["small"], "M-TITLE")
        self.text(self.rev, (x + 118, y + 4.2), TXT["view_title"], "M-TITLE")
        self.text("SHEET", (x + 148, y + 14.6), TXT["small"], "M-TITLE")
        self.text(sheet_of or self.sheet_of or "-", (x + 148, y + 5.0),
                  TXT["table"], "M-TITLE")
        self.line((x + 96, y + 20), (x + 96, y + 32), "M-TITLE")
        self.text(f"SCALE   {scale}", (x + 2, y + 24.4), TXT["table"], "M-TITLE")
        self.text(f"DATE   {self.DATE}", (x + 98, y + 24.4), TXT["table"], "M-TITLE")
        self.text(f"DESIGNED  {designed}", (x + 2, y + 36.4), TXT["small"], "M-TITLE")
        self.text(f"CHECKED  {checked}", (x + 62, y + 36.4), TXT["small"], "M-TITLE")
        self.text(f"APPROVED  {approved}", (x + 122, y + 36.4), TXT["small"], "M-TITLE")
        self.text("STATUS", (x + 2, y + 48.4), TXT["small"], "M-TITLE")
        self.text(self.status, (x + 22, y + 48.0), TXT["table"], "M-FLAG")
        self.text("DRAWING TITLE", (x + 2, y + 73.4), TXT["small"], "M-TITLE")
        self.text(self.title[:52], (x + 2, y + 65.4), TXT["detail_label"], "M-TITLE")
        if self.subtitle:
            self.text(self.subtitle[:74], (x + 2, y + 58.8), TXT["small"], "M-TITLE")
        self.text("PROJECT", (x + 2, y + 95.2), TXT["small"], "M-TITLE")
        self.text("UNDERGROUND CBRN-HARDENED BLAST-RESISTANT", (x + 2, y + 89.6),
                  TXT["table"], "M-TITLE")
        self.text("PROTECTIVE STRUCTURE  -  PUNE, MAHARASHTRA", (x + 2, y + 85.0),
                  TXT["table"], "M-TITLE")
        self.text(f"{P.GEOM_REV}   -   {self.TB_SCOPE}",
                  (x + 2, y + 80.0), TXT["small"], "M-TITLE")

    def finish(self, scale="AS NOTED", sheet_of="", extra=None):
        """Header + title block, called last so nothing overdraws them."""
        self.sheet_header(extra)
        self.titleblock(scale=scale, sheet_of=sheet_of or self.sheet_of)


# ------------------------------------------------------------------ helpers
def evidence_key(sh, x, y):
    """The evidence-class key block used on every sheet in these packages."""
    return sh.panel(x, y, 168, "EVIDENCE CLASS - APPLIED TO EVERY VALUE ON THIS SHEET", [
        "[C] CONFIRMED       traceable to the master, to a Rev F drawing or to sheet S-06",
        "[R] RECONSTRUCTED   computed here from confirmed values; the arithmetic is shown",
        "[A] ASSUMED         an engineering selection made by this package - confirm before construction",
        "[U] UNRESOLVED      competing values exist in the project, or the input does not",
        "[N] NOT AVAILABLE   no source exists anywhere in the project - DATA REQUIRED",
    ], h=2.0, lead=3.4)


# ============================================================== A4 handout
A4_W, A4_H = 297.0, 210.0          # landscape


class A4Sheet(Sheet):
    """One A4 landscape handout page.

    Same library, same layers, same conventions as the A1 sheets - only the
    sheet size, border and footer strip differ.  Used for the two-page
    handouts, which must be exactly two pages.
    """

    def __init__(self, number, title, subtitle="", package="DRAINAGE",
                 rev="DR1", page="1 OF 2", status=P.STATUS):
        self.page = page
        super().__init__(number, title, subtitle, package=package, rev=rev,
                         status=status)

    def border(self):
        self.rect(0, 0, A4_W, A4_H, "M-TITLE")
        self.rect(8, 8, A4_W - 8, A4_H - 8, "M-TITLE")

    def sheet_header(self, extra=None):
        self.text(self.title, (12, A4_H - 18), 4.2, "M-TITLE")
        if self.subtitle:
            self.text(self.subtitle, (12, A4_H - 24.5), 2.2, "M-TEXT")
        self.line((8, A4_H - 27.5), (A4_W - 8, A4_H - 27.5), "M-TITLE")
        self.text(f"PAGE {self.page}", (A4_W - 12, A4_H - 18), 3.0,
                  "M-TITLE", "RIGHT")

    def titleblock(self, designed="", checked="", approved="", scale="",
                   sheet_of=""):
        self.line((8, 20), (A4_W - 8, 20), "M-TITLE")
        self.text("UNDERGROUND CBRN-HARDENED BLAST-RESISTANT PROTECTIVE "
                  "STRUCTURE  -  PUNE", (12, 14.5), 2.2, "M-TITLE")
        self.text(f"{self.package} PACKAGE  REV {self.rev}   "
                  f"{P.GEOM_REV}   {P.PACKAGE_DATE}", (12, 10.5), 2.0,
                  "M-TEXT")
        self.text("SENTRY POST EXCLUDED   -   " + self.status,
                  (A4_W - 12, 14.5), 2.0, "M-FLAG", "RIGHT")
        self.text("DEVELOPED FOR PROJECT COORDINATION - PENDING ENGINEERING "
                  "VERIFICATION", (A4_W - 12, 10.5), 2.0, "M-TEXT", "RIGHT")

    def finish(self, scale="", sheet_of="", extra=None):
        self.sheet_header(extra)
        self.titleblock()
