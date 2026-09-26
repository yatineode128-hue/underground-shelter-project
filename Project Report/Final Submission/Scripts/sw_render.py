"""
sw_render.py -- typesets the final-submission project report in service-writing
layout.

    python3 "Project Report/Final Submission/Scripts/sw_render.py"

Reads   Project Report/Final Submission/Source/report_text.txt
Writes  Project Report/Final Submission/CBRN_Hardened_Underground_Ops_Room_Project_Report.pdf

Page layout follows the service-writing pattern supplied by the owner: a red
double-rule frame with rounded corners, the running head outside the frame on
the outer side, the page number in a circle on the bottom rule and a red tab
at the outer bottom corner.  Paragraph numbering is decimal and restarts in
every chapter: 1. / 1.1 / 1.1.1.

Source markup (one directive per line; a paragraph continues on following lines
until a blank line or the next directive):

    #front  TITLE                         unnumbered front-matter page
    #plainfront TITLE                     the same, without the frame
    #chapter TITLE | (SUBTITLE)            new chapter, numbering restarts
    #appendix A | TITLE | (SUBTITLE)       new appendix, numbering restarts
    #head   Text                           unnumbered side heading
    P1 Title | text                        numbered paragraph, level 1
    P2 Title | text                        level 2  (1.1)
    P3 Title | text                        level 3  (1.1.1)   title may be empty
    T  text                                un-numbered text paragraph
    #table Caption                         table; first row is the header
    #widths 10,40,50                       column widths in per cent (optional)
    #align L,L,R                           column alignment (optional)
    a | b | c                              rows
    #end
    #calc                                  calculation block
    expression ;; result                   (result optional; '!' prefix = bold)
    #end
    #fig name | Caption                    drawn figure from sw_figures.py
    #photo name | Caption                  photograph / map (sw_figures.PHOTOS)
    #drawings                              drawing index, read from the QA index
    #toc  #lof  #lot                       lists
    #pagebreak
    C  text                                centred paragraph (front pages)
    #crest H                               CME crest, H mm high
    #cols Head | a | b || Head | c          side-by-side lists
    #right - | line | line                 right-hand signature block
    #examiners                             examiners' signature lines

Inline: **bold**, *italic*, <sub>..</sub>, <sup>..</sup>.
"""

import os
import re
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont, TTFontFile
from reportlab.platypus import (BaseDocTemplate, CondPageBreak, Flowable,
                                Frame, KeepTogether, NextPageTemplate,
                                PageBreak, PageTemplate, Paragraph, Spacer,
                                Table, TableStyle)

HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.abspath(os.path.join(HERE, ".."))
ROOT = os.path.abspath(os.path.join(PKG, "..", ".."))
SRC_DIR = os.path.join(PKG, "Source")
OUT = os.path.join(PKG, "CBRN_Hardened_Underground_Ops_Room_Project_Report.pdf")
sys.path.insert(0, HERE)

# ---------------------------------------------------------------- fonts
LIB = "/usr/share/fonts/truetype/liberation"
FREE = "/usr/share/fonts/truetype/freefont"
MS = "/usr/share/fonts/truetype/msttcorefonts"

# Arial where it is installed (msttcorefonts); otherwise Liberation Sans, which
# is metrically identical to Arial.
if os.path.exists(os.path.join(MS, "arial.ttf")):
    BODY_FACES = [(MS, "arial.ttf"), (MS, "arialbd.ttf"), (MS, "ariali.ttf"),
                  (MS, "arialbi.ttf")]
else:
    BODY_FACES = [(LIB, "LiberationSans-Regular.ttf"),
                  (LIB, "LiberationSans-Bold.ttf"),
                  (LIB, "LiberationSans-Italic.ttf"),
                  (LIB, "LiberationSans-BoldItalic.ttf")]


def register_fonts():
    faces = [("Arial",) + BODY_FACES[0], ("Arial-Bold",) + BODY_FACES[1],
             ("Arial-Italic",) + BODY_FACES[2],
             ("Arial-BoldItalic",) + BODY_FACES[3],
             # the drawn figures use these names
             ("RepSans", FREE, "FreeSans.ttf"),
             ("RepSans-Bold", FREE, "FreeSansBold.ttf"),
             ("RepSans-Oblique", FREE, "FreeSansOblique.ttf"),
             ("RepSans-BoldOblique", FREE, "FreeSansBoldOblique.ttf"),
             ("RepMono", FREE, "FreeMono.ttf"),
             ("RepMono-Bold", FREE, "FreeMonoBold.ttf")]
    for name, d, fn in faces:
        if name not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(name, os.path.join(d, fn)))
    pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold",
                                  italic="Arial-Italic",
                                  boldItalic="Arial-BoldItalic")
    pdfmetrics.registerFontFamily("RepSans", normal="RepSans",
                                  bold="RepSans-Bold",
                                  italic="RepSans-Oblique",
                                  boldItalic="RepSans-BoldOblique")


_CMAP = None


def missing_glyphs(text):
    global _CMAP
    if _CMAP is None:
        _CMAP = TTFontFile(os.path.join(*BODY_FACES[0])).charToGlyph
    return sorted(set(c for c in text if ord(c) > 126 and ord(c) not in _CMAP))


# ---------------------------------------------------------------- page
PW, PH = A4
FR_IN = 11 * mm            # frame inset from the paper edge
PAD = 7 * mm               # text inset from the frame
TXT_L = FR_IN + PAD
TXT_W = PW - 2 * TXT_L     # 174 mm
TXT_B = FR_IN + 10 * mm
TXT_T = PH - FR_IN - 8 * mm

RED = colors.Color(0.78, 0.09, 0.11)       # frame only -- all text is black
INK = colors.black
GREY = colors.black
RULE = colors.Color(0.25, 0.25, 0.25)
HEAD_BG = colors.Color(0.90, 0.90, 0.91)

ROMAN = ["", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x",
         "xi", "xii", "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "xix", "xx"]


def draw_frame(c, odd, with_number=None):
    """The red double rule, the running head, the tab and the page number."""
    c.saveState()
    r = 7 * mm
    x0, y0 = FR_IN, FR_IN
    w, h = PW - 2 * FR_IN, PH - 2 * FR_IN
    c.setStrokeColor(RED)
    c.setLineWidth(1.6)
    c.roundRect(x0, y0, w, h, r, stroke=1, fill=0)
    g = 1.3 * mm
    c.setLineWidth(0.55)
    c.roundRect(x0 + g, y0 + g, w - 2 * g, h - 2 * g, r - g, stroke=1,
                fill=0)
    # red tab at the outer bottom corner
    s = 7.5 * mm
    tx = (PW - FR_IN - s + 1.2 * mm) if odd else (FR_IN - 1.2 * mm)
    ty = FR_IN - 1.2 * mm
    c.setFillColor(RED)
    c.setStrokeColor(RED)
    c.rect(tx, ty, s, s, stroke=0, fill=1)
    c.setStrokeColor(colors.white)
    c.setLineWidth(0.6)
    c.rect(tx + 1.2 * mm, ty + 1.2 * mm, s - 2.4 * mm, s - 2.4 * mm,
           stroke=1, fill=0)
    c.setFillColor(colors.white)
    cx, cy = tx + s / 2.0, ty + s / 2.0
    k = 1.35 * mm
    p = c.beginPath()
    p.moveTo(cx, cy + k)
    p.lineTo(cx + k, cy)
    p.lineTo(cx, cy - k)
    p.lineTo(cx - k, cy)
    p.close()
    c.drawPath(p, stroke=0, fill=1)
    # page number in a circle on the bottom rule
    if with_number:
        cx, cy, rr = PW / 2.0, FR_IN + g / 2.0, 3.6 * mm
        c.setFillColor(colors.Color(0.78, 0.78, 0.80))
        c.circle(cx + 0.35 * mm, cy - 0.45 * mm, rr, stroke=0, fill=1)
        c.setFillColor(colors.white)
        c.setStrokeColor(colors.Color(0.62, 0.62, 0.64))
        c.setLineWidth(0.5)
        c.circle(cx, cy, rr, stroke=1, fill=1)
        c.setFillColor(INK)
        c.setFont("Arial", 9 if len(with_number) < 3 else 8)
        c.drawCentredString(cx, cy - 3.1, with_number)
    c.restoreState()


class Doc(BaseDocTemplate):
    def __init__(self, path, **kw):
        BaseDocTemplate.__init__(self, path, pagesize=A4, **kw)
        self.main_start = None
        self.front_start = None
        self.entries = []          # (kind, level, text, page string)
        fr = Frame(TXT_L, TXT_B, TXT_W, TXT_T - TXT_B, id="body",
                   leftPadding=0, rightPadding=0, topPadding=0,
                   bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[fr], onPageEnd=self._cover),
            PageTemplate(id="front", frames=[fr], onPageEnd=self._front),
            PageTemplate(id="plain", frames=[fr], onPageEnd=self._plain),
            PageTemplate(id="main", frames=[fr], onPageEnd=self._main)])

    def page_label(self):
        if self.main_start is not None and self.page >= self.main_start:
            return str(self.page - self.main_start + 1)
        if self.front_start is not None and self.page >= self.front_start:
            n = self.page - self.front_start + 1
            return ROMAN[n] if n < len(ROMAN) else str(n)
        return ""

    def _cover(self, c, d):
        if hasattr(c, "setProducer"):
            c.setProducer("Syndicate 01")
        draw_frame(c, True, None)

    def _front(self, c, d):
        draw_frame(c, self.page % 2 == 1, self.page_label())

    def _plain(self, c, d):
        """No frame: the page number alone, centred at the foot."""
        c.saveState()
        c.setFont("Arial", 11)
        c.setFillColor(INK)
        c.drawCentredString(PW / 2.0, 12 * mm, self.page_label())
        c.restoreState()

    def _main(self, c, d):
        draw_frame(c, self.page % 2 == 1, self.page_label())

    def afterFlowable(self, f):
        tag = getattr(f, "_entry", None)
        if tag:
            kind, level, text = tag
            self.entries.append((kind, level, text, self.page_label()))


class Marker(Flowable):
    """Zero-size flowable that records where front matter / main text start."""

    def __init__(self, which):
        Flowable.__init__(self)
        self.which = which

    def wrap(self, aw, ah):
        return 0, 0

    def draw(self):
        doc = self.canv._doctemplate
        if self.which == "front" and doc.front_start is None:
            doc.front_start = doc.page
        if self.which == "main" and doc.main_start is None:
            doc.main_start = doc.page


# ---------------------------------------------------------------- styles
BODY_SIZE, BODY_LEAD = 12.0, 16.2
TABLE_SIZE = 10.0


def styles():
    s = {}
    s["body"] = ParagraphStyle("body", fontName="Arial", fontSize=BODY_SIZE,
                               leading=BODY_LEAD, alignment=TA_JUSTIFY,
                               textColor=INK, spaceAfter=6.5)
    s["chap"] = ParagraphStyle("chap", fontName="Arial-Bold", fontSize=14,
                               leading=18, alignment=TA_CENTER,
                               textColor=INK, spaceAfter=1.5)
    s["sub"] = ParagraphStyle("sub", parent=s["chap"], fontSize=12,
                              leading=16, spaceAfter=12)
    s["head"] = ParagraphStyle("head", fontName="Arial-Bold", fontSize=12,
                               leading=16, textColor=INK, spaceBefore=6,
                               spaceAfter=6, keepWithNext=1)
    s["th"] = ParagraphStyle("th", fontName="Arial-Bold", fontSize=TABLE_SIZE,
                             leading=TABLE_SIZE * 1.2, textColor=INK)
    s["td"] = ParagraphStyle("td", fontName="Arial", fontSize=TABLE_SIZE,
                             leading=TABLE_SIZE * 1.2, textColor=INK)
    s["tcap"] = ParagraphStyle("tcap", fontName="Arial-Bold", fontSize=11,
                               leading=14, alignment=TA_CENTER,
                               textColor=INK, spaceBefore=4, spaceAfter=4,
                               keepWithNext=1)
    s["fcap"] = ParagraphStyle("fcap", fontName="Arial-Bold", fontSize=11,
                               leading=14, alignment=TA_CENTER,
                               textColor=INK, spaceBefore=3, spaceAfter=9)
    s["calc"] = ParagraphStyle("calc", fontName="Arial", fontSize=11,
                               leading=14, textColor=INK)
    s["calcr"] = ParagraphStyle("calcr", parent=s["calc"],
                                alignment=TA_RIGHT)
    s["toc1"] = ParagraphStyle("toc1", fontName="Arial-Bold", fontSize=12,
                               leading=15.5, textColor=INK)
    s["toc2"] = ParagraphStyle("toc2", fontName="Arial", fontSize=11,
                               leading=14, textColor=INK)
    s["tocr"] = ParagraphStyle("tocr", fontName="Arial", fontSize=11,
                               leading=14, alignment=TA_RIGHT)
    s["center"] = ParagraphStyle("center", parent=s["body"],
                                 alignment=TA_CENTER)
    return s


S = styles()

# ---------------------------------------------------------------- inline


def inline(t):
    t = t.replace("&", "&amp;")
    t = re.sub(r"<(?!/?(sub|sup|b|i|br/?)>)", "&lt;", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    return t


# paragraph number geometry: (number indent, text tab) for levels 1..3
TAB = {1: (0.0, 10.5 * mm), 2: (10.5 * mm, 24.5 * mm),
       3: (24.5 * mm, 41.5 * mm), 0: (0.0, 0.0)}

_BLANK = None


def _blank_png():
    global _BLANK
    if _BLANK is None:
        _BLANK = os.path.join(HERE, "_gap.png")
        if not os.path.exists(_BLANK):
            from PIL import Image
            Image.new("RGBA", (1, 1), (255, 255, 255, 0)).save(_BLANK)
    return _BLANK


def numbered(level, number, title, text):
    """A service-writing paragraph: number, bold title, full-width text."""
    ind, tab = TAB[level]
    st = ParagraphStyle("p%d" % level, parent=S["body"], leftIndent=ind)
    body = ""
    if number:
        nw = pdfmetrics.stringWidth(number, "Arial", BODY_SIZE)
        gap = max(tab - ind - nw, 2.2 * mm)
        body = '%s<img src="%s" width="%.2f" height="1"/>' % (
            number, _blank_png(), gap)
    if title:
        body += "<b>%s</b>. " % inline(title)
    body += inline(text)
    return Paragraph(body, st)


# ---------------------------------------------------------------- tables


def make_table(caption, rows, widths=None, align=None, font=TABLE_SIZE,
               header=True, repeat=True):
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    if widths:
        tot = float(sum(widths))
        cw = [TXT_W * w / tot for w in widths]
    else:
        cw = [TXT_W / ncol] * ncol
    align = align or ["L"] * ncol
    alm = {"L": TA_LEFT, "C": TA_CENTER, "R": TA_RIGHT}
    data = []
    for ri, r in enumerate(rows):
        line = []
        for ci, cell in enumerate(r):
            base = S["th"] if (header and ri == 0) else S["td"]
            st = ParagraphStyle("c", parent=base, fontSize=font,
                                leading=font * 1.2,
                                alignment=(TA_CENTER if header and ri == 0
                                           else alm[align[ci]]))
            line.append(Paragraph(inline(cell.strip()), st))
        data.append(line)
    # group rows: a row whose only content is in the first cell
    groups = []
    for ri, r in enumerate(rows):
        if ri and r[0].strip().startswith("==") and \
                not any(x.strip() for x in r[1:]):
            data[ri][0] = Paragraph("<b>%s</b>" % inline(
                r[0].strip()[2:].strip()), S["td"])
            groups.append(ri)
    t = Table(data, colWidths=cw, repeatRows=1 if (header and repeat) else 0,
              hAlign="CENTER")
    ts = [("GRID", (0, 0), (-1, -1), 0.45, RULE),
          ("VALIGN", (0, 0), (-1, -1), "TOP"),
          ("TOPPADDING", (0, 0), (-1, -1), 2.2),
          ("BOTTOMPADDING", (0, 0), (-1, -1), 2.6),
          ("LEFTPADDING", (0, 0), (-1, -1), 3.2),
          ("RIGHTPADDING", (0, 0), (-1, -1), 3.2)]
    if header:
        ts.append(("BACKGROUND", (0, 0), (-1, 0), HEAD_BG))
    for ri in groups:
        ts += [("SPAN", (0, ri), (-1, ri)),
               ("BACKGROUND", (0, ri), (-1, ri),
                colors.Color(0.94, 0.94, 0.945))]
    t.setStyle(TableStyle(ts))
    return t


def calc_block(lines, indent):
    data, ts = [], []
    for i, ln in enumerate(lines):
        bold = ln.startswith("!")
        if bold:
            ln = ln[1:]
        if ";;" in ln:
            a, b = ln.split(";;", 1)
        else:
            a, b = ln, ""
        a, b = inline(a.strip()), inline(b.strip())
        if bold:
            a = "<b>%s</b>" % a if a else a
            b = "<b>%s</b>" % b if b else b
        data.append([Paragraph(a, S["calc"]), Paragraph(b, S["calcr"])])
        if not b:
            ts.append(("SPAN", (0, i), (1, i)))
    w = TXT_W - indent
    t = Table(data, colWidths=[w * 0.74, w * 0.26], hAlign="RIGHT")
    ts += [("VALIGN", (0, 0), (-1, -1), "TOP"),
           ("TOPPADDING", (0, 0), (-1, -1), 0.6),
           ("BOTTOMPADDING", (0, 0), (-1, -1), 0.8),
           ("LEFTPADDING", (0, 0), (-1, -1), 0),
           ("RIGHTPADDING", (0, 0), (-1, -1), 0),
           ("LINEBEFORE", (0, 0), (0, -1), 0.8, colors.Color(0.7, 0.7, 0.72))]
    t.setStyle(TableStyle(ts))
    # a small left inset inside the rule
    t2 = Table([[t]], colWidths=[w], hAlign="RIGHT")
    t2.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                            ("TOPPADDING", (0, 0), (-1, -1), 1),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
    return t2


class Entry(Flowable):
    """Zero-height flowable carrying a TOC / LOF / LOT entry."""

    def __init__(self, kind, level, text):
        Flowable.__init__(self)
        self._entry = (kind, level, text)

    def wrap(self, aw, ah):
        return 0, 0

    def draw(self):
        pass


class FigBox(Flowable):
    """A figure drawing, scaled to the text measure and centred."""

    def __init__(self, drawing, maxw=TXT_W):
        Flowable.__init__(self)
        self.d = drawing
        self.sc = min(1.0, maxw / float(drawing.width))
        self.width = drawing.width * self.sc
        self.height = drawing.height * self.sc

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        from reportlab.graphics import renderPDF
        c = self.canv
        c.saveState()
        c.translate((TXT_W - self.width) / 2.0, 0)
        c.scale(self.sc, self.sc)
        renderPDF.draw(self.d, c, 0, 0)
        c.restoreState()


class PhotoBox(Flowable):
    """A photograph or map, scaled to the text measure and centred."""

    def __init__(self, buf, size, maxw=TXT_W, maxh=86 * mm):
        Flowable.__init__(self)
        from reportlab.lib.utils import ImageReader
        self.img = ImageReader(buf)
        pw, ph = size
        sc = min(maxw / float(pw), maxh / float(ph))
        self.width, self.height = pw * sc, ph * sc

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        self.canv.drawImage(self.img, (TXT_W - self.width) / 2.0, 0,
                            self.width, self.height)


# ---------------------------------------------------------------- lists


def list_table(entries, kinds, dots=True):
    rows, ts = [], []
    for kind, level, text, page in entries:
        if kind not in kinds:
            continue
        st = S["toc1"] if level == 1 else S["toc2"]
        ind = 0 if level == 1 else 8 * mm
        pst = ParagraphStyle("x", parent=st, leftIndent=ind)
        rows.append([Paragraph(inline(text), pst),
                     Paragraph(page, S["tocr"])])
    if not rows:
        rows = [[Paragraph("", S["toc2"]), Paragraph("", S["tocr"])]]
    t = Table(rows, colWidths=[TXT_W - 16 * mm, 16 * mm])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
                           ("TOPPADDING", (0, 0), (-1, -1), 1.4),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 1.4),
                           ("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    return t


# ---------------------------------------------------------------- drawings


def _csv(rel):
    import csv
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return list(csv.reader(f))


def _money(v):
    """Indian digit grouping: 29790913 -> 2,97,90,913."""
    v = int(round(float(v)))
    s = str(v)
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    grp = []
    while len(head) > 2:
        grp.insert(0, head[-2:])
        head = head[:-2]
    if head:
        grp.insert(0, head)
    return ",".join(grp) + "," + tail


BOQ_DESC = {
    ("I", "1"): "Confirmatory soil and rock core boreholes",
    ("I", "2"): "Site clearance, grubbing and setting out",
    ("I", "3"): "Mass excavation in basalt and murrum, depth about 6.8 m",
    ("I", "4"): "Surface dressing and anti-termite treatment",
    ("II", "1"): "Formwork for mat raft and bay 5 sump",
    ("II", "2"): "PCC levelling bed, 100 mm",
    ("II", "3"): "Monolithic mat raft, M35, single pour",
    ("II", "4"): "Pre-applied waterproofing membrane with protection screed",
    ("II", "5"): "Hydrophilic swelling waterstops at kickers",
    ("III", "1"): "Formwork for 600 mm walls, 3.2 m high",
    ("III", "2"): "600 mm perimeter and protective walls, M35",
    ("III", "3"): "Formwork and staging for 900 mm pressure slab",
    ("III", "4"): "900 mm pressure slab, M35, single pour",
    ("III", "5"): "Internal dog-leg staircase, RCC",
    ("III", "6"): "Headhouse, 400 mm walls and 500 mm roof, M35",
    ("III", "7"): "Covered entry stairwell, 250 mm RC",
    ("III", "8"): "Burster slab in the engineered cover, 200 mm, M30",
    ("III", "9"): "Sentry post RC frame",
    ("III", "10"): "110 mm internal partition walls",
    ("III", "11"): "Escape shaft collars ESC 1 and ESC 2, 250 mm RC, OD 1 900",
    ("IV", "1"): "Pressure slab reinforcement (T25 / T12)",
    ("IV", "2"): "Perimeter and protective wall reinforcement (T16 / T20)",
    ("IV", "3"): "Mat raft and haunch reinforcement",
    ("IV", "4"): "Headhouse, stairwell and staircase reinforcement",
    ("IV", "5"): "Burster slab mesh, T12 @ 150 both ways",
    ("IV", "6"): "Sentry post reinforcement",
    ("IV", "7"): "EMP continuity welding of the cage and bonding straps",
    ("V", "1"): "Blast doors 1 and 2, 7 bar, rebound rated",
    ("V", "2"): "Escape shaft head hatches, ESC 1 and ESC 2",
    ("V", "3"): "Fast-acting blast valves BV-1 to BV-3 (DN100)",
    ("V", "4"): "Generator blast valves BV-4 and BV-5 (DN350)",
    ("V", "5"): "NBC collective protection filter trains, 2 x 300 m\u00b3/h",
    ("V", "6"): "EMP Zone 2 welded steel shielded enclosure",
    ("V", "7"): "Layerwise engineered fill and basalt rubble",
    ("V", "8"): "Submersible sump pumps, effluent piping and septic tank",
    ("V", "9"): "Internal plaster, punning and painting",
    ("V", "10"): "Testing, commissioning and envelope leakage test",
}

TAKEOFF_DESC = {
    "1.1": "PCC levelling bed under the mat, 100 mm",
    "1.2": "Monolithic mat raft foundation, 600 mm",
    "1.3": "Perimeter walls W1 to W4, 600 mm",
    "1.4": "Internal walls W5 to W7",
    "1.5": "Pressure slab, 900 mm, net of the stair void",
    "1.6": "Main staircase flights and landings",
    "1.7": "Sump pit and equipment plinths",
    "1.8": "Entry headhouse, 400 mm walls and 500 mm roof",
    "1.9": "Covered entry stairwell, 250 mm walls and roof",
    "1.10": "Burster slab in the engineered cover, 200 mm",
    "1.11": "Sentry post RC frame (footings, plinth, columns, beams, slabs)",
    "1.12": "Escape shaft collars ESC 1 and ESC 2, 250 mm, OD 1 900",
}

STEEL_DESC = {
    "2.1": "8 mm bars (hoops, ties, sentry post)",
    "2.2": "10 mm bars (distribution steel, secondary links)",
    "2.3": "12 mm bars (shear links, burster slab, partitions)",
    "2.4": "16 mm bars (perimeter walls, mat)",
    "2.5": "20 mm bars (walls W6 / W7, headhouse, haunches)",
    "2.6": "25 mm bars (pressure slab, opening trimmers)",
}

PART_NAMES = {
    "I": "Survey, site clearance and excavation",
    "II": "Substructure and foundation works",
    "III": "Superstructure and structural RCC",
    "IV": "Reinforcement steel and shielding",
    "V": "CBRN, EMP, closures and ancillary services",
}


def _part_no(p):
    return p.replace("PART ", "").split(" - ")[0].strip()


def boq_rows():
    """Every measured and priced line of the revised owner bill (WM3)."""
    rows = [["S No", "Description", "Unit", "Qty", "Rate (Rs)",
             "Material (Rs)", "Labour (Rs)", "Amount (Rs)"]]
    data = _csv("WORKS MANAGEMENT/Cost/REVISED_BOQ_PRICED_RC1.csv")[1:]
    part = None
    for r in data:
        if len(r) < 9:
            continue
        if r[0] and not r[1]:
            part = _part_no(r[0])
            rows.append(["== Part %s : %s" % (part, PART_NAMES[part]),
                         "", "", "", "", "", "", ""])
            continue
        if r[7] == "SUBTOTAL":
            rows.append(["", "**Total, Part %s**" % part, "", "", "", "",
                         "", "**%s**" % _money(r[8])])
            continue
        if not r[1] or not r[8] or float(r[8] or 0) == 0:
            continue
        rate = r[5].strip()
        rate = _money(rate) if float(rate) >= 1000 else rate
        qty = r[4].strip()
        mat, tot = float(r[6]), float(r[8])
        lab = tot - mat
        rows.append(["%s.%s" % (part, r[1]), BOQ_DESC[(part, r[1])], r[3],
                     qty, rate, _money(mat),
                     _money(lab) if lab > 0.5 else "-", _money(tot)])
    return rows


def cost_rows():
    rows = [["S No", "Cost Head", "Basis", "Amount (Rs)"]]
    data = _csv("WORKS MANAGEMENT/Cost/REVISED_COST_SUMMARY_RC1.csv")[1:]
    for i, r in enumerate(data):
        name = r[0].replace("&", "and")
        basis = "Sum of Parts I to V" if r[1].startswith("Subtotal") else \
            ("-" if r[1] == "-" else r[1] + " of basic cost")
        if name.upper().startswith("FINAL"):
            rows.append(["", "**Final Project Cost**", "",
                         "**%s**" % _money(r[2])])
        else:
            rows.append([str(i + 1), name, basis, _money(r[2])])
    return rows


def part_rows():
    rows = [["Part", "Description", "Items", "Amount (Rs)"]]
    data = _csv("WORKS MANAGEMENT/Cost/REVISED_BOQ_PRICED_RC1.csv")[1:]
    part, n, tot = None, 0, 0
    names = {}
    for r in data:
        if len(r) < 9:
            continue
        if r[0] and not r[1]:
            part = r[0]
            names[part] = [0, 0.0]
        elif r[1] and r[8] and float(r[8] or 0) > 0:
            names[part][0] += 1
            names[part][1] += float(r[8])
    grand = 0.0
    for p, (cnt, amt) in names.items():
        num = _part_no(p)
        rows.append([num, PART_NAMES[num], str(cnt), _money(amt)])
        grand += amt
    rows.append(["", "**Total Basic Cost**", "", "**%s**" % _money(grand)])
    return rows


PROG_NAMES = {
    "2": "Initial works: site clearance, water and electricity",
    "6": "Substructure works",
    "11": "Centre line works and PCC under the mat",
    "14": "Mat raft and 600 mm perimeter walls to (-)3.2 m, waterproofing "
          "and side backfill",
    "27": "Superstructure RCC works and brickwork",
    "28": "First slab: walls and 900 mm pressure slab",
    "42": "Second slab: walls to ground level, waterproofing and backfill",
    "52": "2 m engineered cover and burster slab",
    "55": "Third slab (first floor slab) RCC works",
    "68": "Fourth slab (headhouse roof slab) RCC works",
    "81": "Deshuttering, cleaning and housekeeping",
    "86": "Finishing works",
    "87": "Brickwork and spiral staircase",
    "92": "Internal plaster, plumbing, drainage and waterproofing",
    "99": "External plaster",
    "108": "Vision panels and windows",
    "112": "Door works",
    "118": "External painting",
    "125": "Internal painting, final coat",
    "129": "Testing and commissioning of all services",
    "130": "Hand-over",
}


def programme_rows():
    data = _csv("WORKS MANAGEMENT/Programme/"
                "REVISED_MASTER_CONSTRUCTION_SCHEDULE_R1.csv")[1:]
    prog = {r[0]: r for r in data}
    ids = ["2", "6", "11", "14", "27", "28", "42", "52", "55", "68", "81",
           "86", "87", "92", "99", "108", "112", "118", "125", "129", "130"]
    rows = [["S No", "Activity", "Working Days", "Start", "Finish"]]
    for n, i in enumerate(ids, 1):
        r = prog[i]
        rows.append([str(n), PROG_NAMES[i],
                     r[2].replace(" days", "").replace(" day", ""),
                     r[3], r[4]])
    rows.append(["", "**Total duration**", "**%s**" % prog["1"][2].replace(
        " days", ""), "**%s**" % prog["1"][3], "**%s**" % prog["1"][4]])
    return rows


def quantity_rows():
    data = _csv("WORKS MANAGEMENT/Cost/REVISED_BOQ_TAKEOFF_RC1.csv")
    rows = [["S No", "Element", "Grade", "Quantity (m\u00b3)"]]
    for r in data:
        if r and r[0] in TAKEOFF_DESC:
            rows.append([r[0], TAKEOFF_DESC[r[0]], r[2], r[3]])
        elif r and not r[0] and len(r) > 1 and \
                r[1].startswith("TOTAL CONCRETE"):
            rows.append(["", "**Total concrete**", "", "**%s**" % r[3]])
    return rows


def steel_rows():
    data = _csv("WORKS MANAGEMENT/Cost/REVISED_BOQ_TAKEOFF_RC1.csv")
    rows = [["S No", "Bar Diameter and Application", "Net Weight (kg)",
             "Gross Weight incl. 5 % Wastage (t)"]]
    for r in data:
        if r and r[0] in STEEL_DESC:
            rows.append([r[0], STEEL_DESC[r[0]], _money(r[2]), r[4]])
        elif r and not r[0] and len(r) > 1 and \
                r[1].startswith("TOTAL REINFORCEMENT"):
            rows.append(["", "**Total reinforcement**",
                         "**%s**" % _money(r[2]), "**%s**" % r[4]])
    return rows


def drawing_index_rows():
    import json
    idx = json.load(open(os.path.join(ROOT, "DRAWING QAQC", "qa_index.json")))
    import sw_figures as SF
    groups = []
    for rec in (r for r in idx if SF.is_generated(r)):
        g = SF.drawing_group(rec)
        if g not in [x[0] for x in groups]:
            groups.append((g, []))
        dict(groups)[g].append(rec)
    order = SF.DRAWING_GROUP_ORDER
    groups.sort(key=lambda x: order.index(x[0][0]) if x[0][0] in order
                else 99)
    rows = [["S No", "Drawing No", "Title", "Scale", "Size"]]
    n = 0
    for (name, where), recs in groups:
        rows.append(["== %s   (Location : %s)" % (name, where), "", "", "",
                     ""])
        for rec in sorted(recs, key=lambda r: SF.sheet_key(r["number"])):
            n += 1
            rows.append([str(n), rec["number"], SF.clean_title(rec),
                         SF.clean_scale(rec.get("scale", "")),
                         rec.get("size", "")])
    return rows


SPECIAL = {"drawings": drawing_index_rows, "boq": boq_rows,
           "cost": cost_rows, "parts": part_rows,
           "programme": programme_rows, "concrete": quantity_rows,
           "steel": steel_rows}


# ---------------------------------------------------------------- parser


def source_text():
    parts = []
    for fn in sorted(os.listdir(SRC_DIR)):
        if fn.endswith(".txt"):
            parts.append(open(os.path.join(SRC_DIR, fn),
                              encoding="utf-8").read())
    return "\n\n".join(parts)


def parse():
    lines = source_text().split("\n")
    blocks = []
    i = 0
    cur = None

    def flush():
        nonlocal cur
        if cur:
            blocks.append(cur)
        cur = None

    while i < len(lines):
        ln = lines[i].rstrip()
        i += 1
        if ln.startswith("%%"):            # comment
            continue
        if not ln.strip():
            flush()
            continue
        if ln.startswith("#table") or ln.startswith("#calc"):
            flush()
            kind = "table" if ln.startswith("#table") else "calc"
            blk = {"k": kind, "cap": ln[len("#" + kind):].strip(),
                   "rows": [], "widths": None, "align": None,
                   "font": None, "nohead": False}
            while i < len(lines) and lines[i].strip() != "#end":
                r = lines[i].rstrip()
                i += 1
                if r.startswith("%%"):
                    continue
                if r.startswith("#widths"):
                    blk["widths"] = [float(x) for x in
                                     r.split(None, 1)[1].split(",")]
                elif r.startswith("#align"):
                    blk["align"] = [x.strip() for x in
                                    r.split(None, 1)[1].split(",")]
                elif r.startswith("#font"):
                    blk["font"] = float(r.split()[1])
                elif r.startswith("#nohead"):
                    blk["nohead"] = True
                elif kind == "table":
                    if r.strip():
                        blk["rows"].append([c for c in r.split("|")])
                else:
                    if r.strip():
                        blk["rows"].append(r.strip())
            i += 1
            blocks.append(blk)
            continue
        m = re.match(r"^(P1|P2|P3|T|C)\s(.*)$", ln)
        if ln.startswith("#"):
            flush()
            parts = ln.split(None, 1)
            blocks.append({"k": parts[0][1:],
                           "arg": parts[1] if len(parts) > 1 else ""})
            continue
        if m:
            flush()
            lev = {"P1": 1, "P2": 2, "P3": 3, "T": 0, "C": 0}[m.group(1)]
            rest = m.group(2)
            if lev and "|" in rest:
                title, text = rest.split("|", 1)
            else:
                title, text = "", rest
            cur = {"k": "p", "lev": lev, "title": title.strip(),
                   "text": text.strip(), "centre": m.group(1) == "C"}
            continue
        if cur is not None:
            cur["text"] += " " + ln.strip()
        else:
            cur = {"k": "p", "lev": 0, "title": "", "text": ln.strip()}
    flush()
    return blocks


# ---------------------------------------------------------------- build


def story(blocks, entries, cover_fn):
    import sw_figures as SF
    st = []
    st += cover_fn()
    chap = None
    nums = [0, 0, 0]
    tcount = fcount = 0
    first_front = True
    in_main = False
    last_level = 0
    for b in blocks:
        k = b["k"]
        if k in ("front", "plainfront", "chapter", "appendix"):
            if k in ("front", "plainfront"):
                # the pages modelled on the owner's sample carry no frame
                st.append(NextPageTemplate("plain" if k == "plainfront"
                                           else "front"))
                st.append(PageBreak())
                if first_front:
                    st.append(Marker("front"))
                first_front = False
                title = b["arg"].strip()
                st.append(Paragraph("<u>%s</u>" % inline(title), S["chap"]))
                st.append(Spacer(1, 8))
                if title not in ("CONTENTS",):
                    st.append(Entry("toc", 1, fix_case(title.title())
                                    if title.isupper() else title))
                chap = None
            else:
                if not in_main:
                    st.append(NextPageTemplate("main"))
                    st.append(PageBreak())
                    st.append(Marker("main"))
                    in_main = True
                else:
                    st.append(PageBreak())
                parts = [x.strip() for x in b["arg"].split("|")]
                if k == "chapter":
                    chap = (chap + 1) if isinstance(chap, int) else 1
                    label = "CHAPTER %d" % chap
                    title, sub = parts[0], (parts[1] if len(parts) > 1
                                            else "")
                    tocname = "Chapter %d : %s" % (chap, title.title())
                else:
                    chap = parts[0]
                    label = "APPENDIX %s" % parts[0]
                    title, sub = parts[1], (parts[2] if len(parts) > 2
                                            else "")
                    tocname = "Appendix %s : %s" % (parts[0], title.title())
                tocname = fix_case(tocname)
                st.append(Entry("toc", 1, tocname))
                st.append(Paragraph("%s : %s" % (label, inline(title)),
                                    S["chap"]))
                if sub:
                    st.append(Paragraph(inline(sub), S["sub"]))
                else:
                    st.append(Spacer(1, 10))
                nums = [0, 0, 0]
                tcount = fcount = 0
            continue
        if k == "head":
            st.append(CondPageBreak(40 * mm))
            st.append(Paragraph(inline(b["arg"]), S["head"]))
            continue
        if k == "pagebreak":
            st.append(PageBreak())
            continue
        if k == "cond":
            st.append(CondPageBreak(float(b["arg"]) * mm))
            continue
        if k == "toc":
            st.append(("TOC",))
            continue
        if k == "lof":
            st.append(("LOF",))
            continue
        if k == "lot":
            st.append(("LOT",))
            continue
        if k == "crest":
            st.append(crest_image(float(b["arg"] or 30)))
            continue
        if k == "cols":
            st.append(column_block(b["arg"]))
            continue
        if k == "right":
            st.append(right_block(b["arg"]))
            continue
        if k == "examiners":
            st.append(examiners_block())
            continue
        if k == "sign":
            st.append(signature_block(b["arg"]))
            continue
        if k == "vspace":
            st.append(Spacer(1, float(b["arg"]) * mm))
            continue
        if k == "p":
            lev = b["lev"]
            if lev:
                nums[lev - 1] += 1
                for j in range(lev, 3):
                    nums[j] = 0
                if lev == 1:
                    number = "%d." % nums[0]
                else:
                    number = ".".join(str(n) for n in nums[:lev])
                last_level = lev
                p = numbered(lev, number, b["title"], b["text"])
            else:
                ind = TAB[last_level][0] if last_level else 0
                if b.get("centre"):
                    p = Paragraph(inline(b["text"]), ParagraphStyle(
                        "tc", parent=S["body"], alignment=TA_CENTER))
                else:
                    p = Paragraph(inline(b["text"]),
                                  ParagraphStyle("t", parent=S["body"],
                                                 leftIndent=ind))
            st.append(p)
            continue
        if k == "table":
            tcount += 1
            num = "%s.%d" % (chap, tcount) if chap else str(tcount)
            cap = "Table %s : %s" % (num, b["cap"])
            rows = b["rows"]
            capt = b["cap"]
            m = re.match(r"^@(\w+)\s*(.*)$", capt)
            if m:
                rows = SPECIAL[m.group(1)]()
                capt = m.group(2)
                cap = "Table %s : %s" % (num, capt)
            if capt.strip() == "-":
                tcount -= 1
                t = make_table("", rows, b["widths"], b["align"],
                               b["font"] or TABLE_SIZE,
                               header=not b["nohead"])
                st += [t, Spacer(1, 7)]
                continue
            t = make_table(cap, rows, b["widths"], b["align"],
                           b["font"] or TABLE_SIZE, header=not b["nohead"])
            capp = Paragraph(inline(cap), S["tcap"])
            ent = Entry("lot", 2, inline_plain(cap))
            if len(rows) <= 14:
                st.append(KeepTogether([ent, capp, t, Spacer(1, 7)]))
            else:
                st += [CondPageBreak(45 * mm), ent, capp, t, Spacer(1, 7)]
            continue
        if k == "calc":
            ind = TAB[max(last_level, 1)][1]
            st.append(calc_block(b["rows"], ind))
            continue
        if k in ("fig", "photo"):
            name, cap = [x.strip() for x in b["arg"].split("|", 1)]
            fcount += 1
            num = "%s.%d" % (chap, fcount) if chap else str(fcount)
            box = FigBox(SF.figure(name)) if k == "fig" else \
                PhotoBox(*SF.photo(name),
                         maxh=SF.PHOTO_MAXH.get(name, 86) * mm)
            capt = "Fig %s : %s" % (num, cap)
            st.append(KeepTogether([Entry("lof", 2, capt), Spacer(1, 3),
                                    box,
                                    Paragraph(inline(capt), S["fcap"])]))
            continue
        raise ValueError("unknown directive %r" % k)
    return st


def fix_case(s):
    small = {"And", "Of", "The", "For", "To", "In", "On", "With", "A", "An",
             "At", "By"}
    words = s.split(" ")
    out = []
    for i, w in enumerate(words):
        if i and w in small and words[i - 1] != "Appendix":
            w = w.lower()
        for ab in ("Cbrn", "Emp", "Hvac", "Rc", "Ops", "Boq", "Is"):
            if w == ab:
                w = ab.upper()
        out.append(w)
    return " ".join(out)


def inline_plain(s):
    return re.sub(r"\*\*|\*", "", s)


def crest_image(height_mm):
    """The CME crest (Images/CME_crest_colour.png, see sw_crest.py)."""
    from reportlab.platypus import Image
    fn = os.path.join(PKG, "Images", "CME_crest_colour.png")
    from PIL import Image as PImage
    w, h = PImage.open(fn).size
    im = Image(fn, width=height_mm * mm * w / float(h), height=height_mm * mm,
               mask="auto")
    im.hAlign = "CENTER"
    return im


def column_block(arg):
    """Side-by-side lists: 'Head | line | line || Head | line'.  The first
    line of each column is bold."""
    cols = [[x.strip() for x in part.split("|")] for part in arg.split("||")]
    st = ParagraphStyle("cl", parent=S["body"], leading=18)
    cells = []
    for c in cols:
        txt = ["<b>%s</b>" % inline(c[0])] + [inline(x) for x in c[1:]]
        cells.append(Paragraph("<br/>".join(txt), st))
    t = Table([cells], colWidths=[TXT_W / len(cells)] * len(cells))
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 6)]))
    return t


def right_block(arg):
    """A signature block in the right half: '- | name | line ...'; a
    leading '-' draws the signature rule."""
    lines = [x.strip() for x in arg.split("|")]
    rule = lines and lines[0] == "-"
    if rule:
        lines = lines[1:]
    p = Paragraph("<br/>".join(inline(x) for x in lines),
                  ParagraphStyle("rb", parent=S["body"], leading=17))
    t = Table([[""], [p]] if rule else [[p]], colWidths=[TXT_W * 0.42],
              hAlign="RIGHT")
    ts = [("LEFTPADDING", (0, 0), (-1, -1), 0),
          ("TOPPADDING", (0, 0), (-1, -1), 2)]
    if rule:
        ts.append(("LINEABOVE", (0, 1), (0, 1), 0.8, INK))
    t.setStyle(TableStyle(ts))
    return t


def examiners_block():
    """Examiners, name and signature lines, as on the owner's sample."""
    b = ParagraphStyle("ex", parent=S["body"], leading=15)
    hb = ParagraphStyle("exh", parent=b, fontName="Arial-Bold")
    rows = [[Paragraph("Examiners", hb), Paragraph("Name", hb),
             Paragraph("Signatures", hb)],
            [Paragraph("1.&nbsp;&nbsp;&nbsp;External Examiner", b), "", ""],
            [Paragraph("2.&nbsp;&nbsp;&nbsp;Guide", b), "", ""]]
    t = Table(rows, colWidths=[TXT_W * 0.34, TXT_W * 0.36, TXT_W * 0.30],
              rowHeights=[9 * mm, 13 * mm, 13 * mm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("LINEBELOW", (1, 1), (-1, 1), 0.8, INK),
        ("LINEBELOW", (1, 2), (-1, 2), 0.8, INK)]))
    return t


def signature_block(arg):
    parts = [p.strip() for p in arg.split("||")]
    cells = []
    for p in parts:
        lines = [x.strip() for x in p.split("|")]
        txt = "<br/>".join(inline(x) for x in lines)
        cells.append(Paragraph(txt, ParagraphStyle(
            "sg", parent=S["body"], alignment=TA_CENTER, leading=15)))
    t = Table([cells], colWidths=[TXT_W / len(cells)] * len(cells))
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("TOPPADDING", (0, 0), (-1, -1), 0)]))
    return t


# Syndicate 01, in the order of the syndicate's own title slide (the left
# column is filled first)
MEMBERS = ["Maj Yatin", "Capt Sukender Singh", "Capt DV Ghanashyama",
           "Capt Sonu Sharma", "Capt Balbanka Tiwary", "Capt Siddharth Sinha"]
# the guides, in the order of the list supplied by the syndicate
GUIDES = ["Maj Ashish Dubey, FGS", "Dr I R Chaudhuri", "Dr Uttam Awari",
          "Lt Col APS Chauhan", "Sh Tilak Sharma, Jt Dir (C), FCM"]


def two_columns(names, style):
    """Names in two centred columns, the left column filled first."""
    cells = [Paragraph(n, style) for n in names]
    half = (len(cells) + 1) // 2
    t = Table([[cells[i], cells[i + half] if i + half < len(cells) else ""]
               for i in range(half)], colWidths=[TXT_W / 2.0] * 2)
    t.setStyle(TableStyle([("TOPPADDING", (0, 0), (-1, -1), 0),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
    return t


def cover():
    import sw_figures as SF
    out = []
    big = ParagraphStyle("big", fontName="Arial-Bold", fontSize=19,
                         leading=25, alignment=TA_CENTER, textColor=INK)
    mid = ParagraphStyle("mid", fontName="Arial-Bold", fontSize=13,
                         leading=17, alignment=TA_CENTER, textColor=INK)
    small = ParagraphStyle("sm", fontName="Arial", fontSize=11, leading=15,
                           alignment=TA_CENTER, textColor=INK)
    out.append(Spacer(1, 3 * mm))
    out.append(Paragraph("COLLEGE OF MILITARY ENGINEERING, PUNE", mid))
    out.append(Paragraph("FACULTY OF CIVIL ENGINEERING", small))
    out.append(Spacer(1, 8 * mm))
    out.append(Paragraph("PROJECT REPORT", mid))
    out.append(Spacer(1, 5 * mm))
    out.append(Paragraph("CBRN HARDENED UNDERGROUND OPS ROOM", big))
    out.append(Spacer(1, 3 * mm))
    out.append(Paragraph("(DESIGN OF A BLAST-RESISTANT, CBRN AND EMP "
                         "PROTECTED UNDERGROUND OPERATIONS ROOM WITH SENTRY "
                         "POST AT PUNE)", ParagraphStyle(
                             "s2", parent=mid, fontSize=11.2, leading=15)))
    out.append(Spacer(1, 6 * mm))
    out.append(FigBox(SF.cover_figure(), maxw=TXT_W))
    out.append(Spacer(1, 6 * mm))
    out.append(Paragraph("Submitted in partial fulfilment of the requirements "
                         "for the award of the degree of", small))
    out.append(Paragraph("<b>Bachelor of Technology (Civil)</b>",
                         small))
    out.append(Spacer(1, 6 * mm))
    out.append(Paragraph("Submitted by", small))
    out.append(Paragraph("<b>SYNDICATE 01</b>", mid))
    out.append(Spacer(1, 2 * mm))
    out.append(two_columns(MEMBERS, small))
    out.append(Spacer(1, 5 * mm))
    out.append(Paragraph("Under the guidance of", small))
    out.append(Spacer(1, 2 * mm))
    out.append(two_columns(GUIDES, small))
    out.append(Spacer(1, 7 * mm))
    out.append(Paragraph("SEPTEMBER 2026", mid))
    return out


def build(entries_in):
    blocks = parse()
    # glyph check over the whole source
    miss = missing_glyphs(source_text())
    if miss:
        print("WARNING: glyphs missing from Liberation Sans:", miss)
    raw = story(blocks, entries_in, cover)
    final = []
    for f in raw:
        if isinstance(f, tuple):
            kind = {"TOC": ("toc",), "LOF": ("lof",), "LOT": ("lot",)}[f[0]]
            final.append(list_table(entries_in, kind))
        else:
            final.append(f)
    doc = Doc(OUT, title="CBRN Hardened Underground Ops Room - Project Report",
              author="Syndicate 01", subject="Project Report",
              creator="Syndicate 01")
    doc.build(final)
    return doc


def main():
    register_fonts()
    entries = []
    # pass 1 with placeholder page labels of the right shape, then repeat
    for _ in range(4):
        doc = build(entries)
        new = doc.entries
        if [e[:3] for e in new] == [e[:3] for e in entries] and \
                [e[3] for e in new] == [e[3] for e in entries]:
            break
        entries = new
    print("written", OUT, "pages:", doc.page)


if __name__ == "__main__":
    main()
