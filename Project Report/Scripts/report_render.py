"""
report_render.py -- renders Documentation/MASTER_PROJECT_REPORT.md to
Project Report/MASTER_PROJECT_REPORT.pdf.

Underground CBRN-hardened blast-resistant protective structure + sentry post, Pune.
Project Report package, revision PR3.

The report SOURCE is the Markdown file.  This script is only the typesetter:
it adds no content, no number and no heading of its own beyond the cover page,
the running head/foot and the automatically paginated contents list -- plus,
from PR3, the College of Military Engineering front matter drawn by
report_frontmatter.py and the drawing index read from the QA tool's own
DRAWING QAQC/qa_index.json.  Edit the Markdown and re-run; never edit the PDF.

Page numbering (PR3): the hard cover and the title page carry no number; the
front matter from the certificate to the list of figures runs i, ii, iii ...
(the certificate's i is counted, not printed); Part 1 starts again at page 1.
The PDF's own page labels match what is printed.

    python3 "Project Report/Scripts/report_render.py"

Dependency: reportlab (already used by WORKS MANAGEMENT/Scripts/wm_programme_pdf.py
and wm_handout_pdf.py, so it is the project's established PDF toolchain).
Fonts: GNU FreeFont, which is the only family on this machine that carries every
glyph the report uses (Greek, sub/superscripts, maths and arrows) in all four
styles.  Any character missing from a face is substituted, never dropped -- see
SUBST and sanitize().

Markdown subset supported -- deliberately small, and the report is written to it:
    # ## ### ####      headings (# starts a new page and enters the contents)
    ---                horizontal rule
    > text             call-out box
    ``` ... ```        fixed-pitch calculation block
    | a | b |          table, with the |---|---| rule row
    - item / 1. item   lists
    **b** *i* `c`      inline bold, italic, fixed pitch
    <sub> <sup>        as written in the master
    <!-- PAGEBREAK --> forced page break
    <!-- FIG: name --> a drawn figure from report_figures.py, numbered and
                       captioned in document order
    <!-- LOF -->       the list of figures
    <!-- HARDCOVER -->   the black hard cover            (report_frontmatter)
    <!-- COVER -->       the title page
    <!-- FRONTMATTER --> certificate, approval sheet, declaration and
                         acknowledgement                 (report_frontmatter)
    <!-- DRAWING INDEX --> the drawing index, from DRAWING QAQC/qa_index.json
"""

import importlib.util
import json
import os
import re
import sys
import datetime

try:
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont, TTFontFile
    from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether,
                                    NextPageTemplate, PageBreak, PageTemplate,
                                    Paragraph,
                                    Spacer, Table, TableStyle)
    from reportlab.platypus.tableofcontents import TableOfContents
except ImportError:                                          # pragma: no cover
    sys.exit("reportlab is required.  python3 -m pip install reportlab")

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
try:
    import report_figures as FIGS
except ImportError:                                          # pragma: no cover
    sys.exit("report_figures.py must sit beside report_render.py")
try:
    import report_frontmatter as FRONT
except ImportError:                                          # pragma: no cover
    sys.exit("report_frontmatter.py must sit beside report_render.py")

PKG = os.path.abspath(os.path.join(HERE, ".."))
SRC = os.path.join(PKG, "Documentation", "MASTER_PROJECT_REPORT.md")
OUT = os.path.join(PKG, "MASTER_PROJECT_REPORT.pdf")
QAQC = os.path.abspath(os.path.join(PKG, "..", "DRAWING QAQC"))
QA_INDEX = os.path.join(QAQC, "qa_index.json")
MAKE_INDEX = os.path.join(QAQC, "Scripts", "make_index.py")

# ---------------------------------------------------------------- page setup
PW, PH = A4
LM, RM, TM, BM = 20 * mm, 16 * mm, 20 * mm, 18 * mm
BODY_W = PW - LM - RM
# the formal front-matter pages: a wider binding margin, no running head/foot
FL, FR, FT, FB = 28 * mm, 24 * mm, 24 * mm, 30 * mm
FRONT_W, FRONT_H = PW - FL - FR, PH - FT - FB

INK = colors.Color(0.09, 0.10, 0.13)
MID = colors.Color(0.36, 0.38, 0.43)
RULE = colors.Color(0.74, 0.76, 0.80)
HDRBG = colors.Color(0.925, 0.933, 0.945)
QUOTEBG = colors.Color(0.960, 0.966, 0.976)
QUOTEBAR = colors.Color(0.30, 0.42, 0.58)
CODEBG = colors.Color(0.972, 0.972, 0.965)
ACCENT = colors.Color(0.14, 0.28, 0.46)
BAND = colors.Color(0.977, 0.980, 0.986)

DOCREF = "UG-CBRN-PUNE / MASTER PROJECT REPORT / PR3"

# ------------------------------------------------------------------- fonts
FONTDIR = "/usr/share/fonts/truetype/freefont"
FACES = [("RepSans", "FreeSans.ttf"),
         ("RepSans-Bold", "FreeSansBold.ttf"),
         ("RepSans-Oblique", "FreeSansOblique.ttf"),
         ("RepSans-BoldOblique", "FreeSansBoldOblique.ttf"),
         ("RepMono", "FreeMono.ttf"),
         ("RepMono-Bold", "FreeMonoBold.ttf"),
         ("RepMono-Oblique", "FreeMonoOblique.ttf")]

# characters that at least one registered face cannot draw, and what to draw
# instead.  Nothing is silently dropped.
SUBST = {"✔": "✓", "✘": "x", "≪": "<<", "≫": ">>",
         "‑": "-", " ": " ", " ": " ", "⁠": ""}

_CMAPS = {}


def register_fonts():
    for name, fn in FACES:
        path = os.path.join(FONTDIR, fn)
        if not os.path.exists(path):
            sys.exit("font not found: " + path)
        pdfmetrics.registerFont(TTFont(name, path))
        _CMAPS[name] = TTFontFile(path).charToGlyph
    pdfmetrics.registerFontFamily("RepSans", normal="RepSans",
                                  bold="RepSans-Bold",
                                  italic="RepSans-Oblique",
                                  boldItalic="RepSans-BoldOblique")
    pdfmetrics.registerFontFamily("RepMono", normal="RepMono",
                                  bold="RepMono-Bold",
                                  italic="RepMono-Oblique",
                                  boldItalic="RepMono-Bold")


MISSING = {}


def sanitize(s):
    """Replace every character no registered face can draw.  Report what was
    replaced so a silent blank box can never reach the PDF."""
    out = []
    for ch in s:
        if ch in SUBST:
            out.append(SUBST[ch])
            continue
        if ord(ch) < 128 or ch in "\n\t":
            out.append(ch)
            continue
        drawable = all(ord(ch) in _CMAPS[n] for n, _ in FACES)
        if drawable:
            out.append(ch)
        else:
            MISSING[ch] = MISSING.get(ch, 0) + 1
            out.append("?")
    return "".join(out)


# ------------------------------------------------------------------ styles
def styles():
    s = {}
    s["body"] = ParagraphStyle("body", fontName="RepSans", fontSize=8.6,
                               leading=11.6, alignment=TA_JUSTIFY,
                               textColor=INK, spaceAfter=4.6)
    s["bodyc"] = ParagraphStyle("bodyc", parent=s["body"], alignment=TA_CENTER)
    s["h1"] = ParagraphStyle("h1", fontName="RepSans-Bold", fontSize=15.5,
                             leading=18.5, textColor=colors.white,
                             spaceBefore=0, spaceAfter=0, alignment=TA_LEFT)
    s["h2"] = ParagraphStyle("h2", fontName="RepSans-Bold", fontSize=11.6,
                             leading=14, textColor=ACCENT,
                             spaceBefore=11, spaceAfter=4)
    s["h3"] = ParagraphStyle("h3", fontName="RepSans-Bold", fontSize=9.6,
                             leading=12, textColor=INK,
                             spaceBefore=8, spaceAfter=3)
    s["h4"] = ParagraphStyle("h4", fontName="RepSans-BoldOblique", fontSize=8.8,
                             leading=11, textColor=MID,
                             spaceBefore=6.5, spaceAfter=2.5)
    s["li"] = ParagraphStyle("li", parent=s["body"], leftIndent=11,
                             bulletIndent=2, spaceAfter=2.4)
    s["quote"] = ParagraphStyle("quote", parent=s["body"], fontSize=8.4,
                                leading=11.2, alignment=TA_LEFT,
                                spaceAfter=0, spaceBefore=0)
    s["code"] = ParagraphStyle("code", fontName="RepMono", fontSize=7.3,
                               leading=9.1, textColor=INK, alignment=TA_LEFT,
                               spaceAfter=0, spaceBefore=0)
    s["th"] = ParagraphStyle("th", fontName="RepSans-Bold", fontSize=7.5,
                             leading=9.2, textColor=INK, alignment=TA_LEFT)
    s["td"] = ParagraphStyle("td", fontName="RepSans", fontSize=7.5,
                             leading=9.2, textColor=INK, alignment=TA_LEFT)
    s["cap"] = ParagraphStyle("cap", fontName="RepSans-Oblique", fontSize=7.4,
                              leading=9.4, textColor=MID, spaceAfter=6)
    s["figcap"] = ParagraphStyle("figcap", fontName="RepSans", fontSize=7.5,
                                 leading=9.6, textColor=MID,
                                 alignment=TA_LEFT, spaceBefore=2.6,
                                 spaceAfter=9)
    s["lof"] = ParagraphStyle("lof", fontName="RepSans", fontSize=8.0,
                              leading=11.0, textColor=INK, leftIndent=17,
                              firstLineIndent=-17)
    # cover
    s["cvt"] = ParagraphStyle("cvt", fontName="RepSans-Bold", fontSize=21,
                              leading=25, textColor=INK, alignment=TA_LEFT)
    s["cvs"] = ParagraphStyle("cvs", fontName="RepSans", fontSize=12.4,
                              leading=16, textColor=MID, alignment=TA_LEFT)
    s["cvn"] = ParagraphStyle("cvn", fontName="RepSans", fontSize=8.8,
                              leading=12.4, textColor=INK, alignment=TA_LEFT)
    # contents
    s["toc1"] = ParagraphStyle("toc1", fontName="RepSans-Bold", fontSize=9,
                               leading=13.5, textColor=INK, spaceBefore=5)
    s["toc2"] = ParagraphStyle("toc2", fontName="RepSans", fontSize=8.2,
                               leading=11.4, textColor=INK, leftIndent=13)
    return s


ST = styles()

# ------------------------------------------------------------------ inline
TAG = re.compile(r"</?(?:sub|sup|b|i|br\s*/?)>", re.I)


def inline(text):
    """Markdown inline -> reportlab mini-HTML.  Escapes everything, then puts
    back only the tags the report is allowed to use."""
    text = sanitize(text)
    holds = []

    def hold(m):
        holds.append(m.group(0))
        return "\x00%d\x00" % (len(holds) - 1)

    text = TAG.sub(hold, text)
    text = (text.replace("&", "&amp;").replace("<", "&lt;")
                .replace(">", "&gt;"))
    text = re.sub(r"`([^`]+)`",
                  lambda m: '<font face="RepMono" size="7.9">%s</font>'
                            % m.group(1), text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text, flags=re.S)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>",
                  text, flags=re.S)
    text = re.sub(r"~~(.+?)~~", r"\1", text, flags=re.S)
    text = re.sub(r"\x00(\d+)\x00", lambda m: holds[int(m.group(1))], text)
    return text


# ------------------------------------------------------------------ blocks
def para(text, style, **kw):
    """Paragraph, with a guard: if the inline markup produces tags the
    parser cannot balance, fall back to the same text with the markup
    stripped rather than failing the build silently or loudly."""
    try:
        return Paragraph(text, style, **kw)
    except Exception as exc:                                 # noqa: BLE001
        plain = re.sub(r"<[^>]+>", "", text)
        BADMARKUP.append((plain[:70], str(exc)[:70]))
        return Paragraph(plain, style, **kw)


BADMARKUP = []


class Rule(Spacer):
    def __init__(self, w, colour=RULE, th=0.55, gap=3.2):
        Spacer.__init__(self, w, th + 2 * gap)
        self.colour, self.th, self.gap = colour, th, gap

    def draw(self):
        self.canv.setStrokeColor(self.colour)
        self.canv.setLineWidth(self.th)
        self.canv.line(0, self.gap, self.width, self.gap)


def part_banner(text, key):
    p = Paragraph(inline(text), ST["h1"])
    t = Table([[p]], colWidths=[BODY_W], rowHeights=None)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ACCENT),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    t._tocEntry = (0, text, key)
    return t


def quote_box(lines):
    flows = []
    for kind, payload in lines:
        if kind == "p":
            flows.append(para(inline(payload), ST["quote"]))
            flows.append(Spacer(1, 3))
        elif kind == "code":
            flows.append(code_block(payload, width=BODY_W - 22))
        elif kind == "table":
            flows.append(make_table(payload, width=BODY_W - 22))
    if flows and isinstance(flows[-1], Spacer):
        flows.pop()
    t = Table([[flows]], colWidths=[BODY_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), QUOTEBG),
        ("LINEBEFORE", (0, 0), (0, -1), 2.2, QUOTEBAR),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
    return [t, Spacer(1, 6)]


def code_block(lines, width=None):
    """A fixed-pitch calculation block.  Built as ONE ROW PER LINE so that a
    long block splits across a page break instead of being pushed whole onto
    the next page and leaving half a page empty."""
    width = width or BODY_W
    rows = []
    for ln in lines:
        ln = sanitize(ln).replace("&", "&amp;").replace("<", "&lt;") \
                         .replace(">", "&gt;").replace(" ", "&nbsp;")
        rows.append([para(ln if ln.strip() else "&nbsp;", ST["code"])])
    if not rows:
        rows = [[para("&nbsp;", ST["code"])]]
    t = Table(rows, colWidths=[width])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CODEBG),
        ("BOX", (0, 0), (-1, -1), 0.5, RULE),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, 0), 5),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    return t


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", line)]


def col_widths(rows, width):
    n = max(len(r) for r in rows)
    rows = [r + [""] * (n - len(r)) for r in rows]
    # natural width: longest word sets the minimum, mean length sets the want
    want, mins = [], []
    for j in range(n):
        cells = [re.sub(r"[*`]", "", r[j]) for r in rows]
        longest_word = max([max([len(w) for w in c.split()] or [1])
                            for c in cells] or [1])
        mins.append(min(longest_word * 4.3 + 9, width * 0.36))
        want.append(max(len(c) for c in cells) * 3.55 + 9)
    tot = sum(want)
    if tot <= 0:
        return [width / n] * n
    scaled = [width * w / tot for w in want]
    # honour minimums, then take the difference off the widest columns
    out = [max(scaled[j], mins[j]) for j in range(n)]
    over = sum(out) - width
    guard = 0
    while over > 0.5 and guard < 200:
        guard += 1
        j = out.index(max(out))
        take = min(over, out[j] - mins[j]) if out[j] > mins[j] else 0
        if take <= 0:
            break
        out[j] -= take
        over -= take
    f = width / sum(out)
    return [w * f for w in out]


def make_table(rows, width=None):
    width = width or BODY_W
    n = max(len(r) for r in rows)
    rows = [r + [""] * (n - len(r)) for r in rows]
    cw = col_widths(rows, width)
    data = []
    for i, r in enumerate(rows):
        style = ST["th"] if i == 0 else ST["td"]
        data.append([para(inline(c.replace("\\|", "|")), style)
                     for c in r])
    t = Table(data, colWidths=cw, repeatRows=1)
    cmds = [("BACKGROUND", (0, 0), (-1, 0), HDRBG),
            ("LINEBELOW", (0, 0), (-1, 0), 0.7, MID),
            ("GRID", (0, 0), (-1, -1), 0.3, RULE),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 3.6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 3.6),
            ("TOPPADDING", (0, 0), (-1, -1), 2.9),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2.9)]
    for i in range(2, len(rows), 2):
        cmds.append(("BACKGROUND", (0, i), (-1, i), BAND))
    t.setStyle(TableStyle(cmds))
    return t


# ------------------------------------------------------------------- parser
def parse(md):
    """Markdown -> list of ('kind', payload) blocks."""
    lines = md.split("\n")
    blocks, i = [], 0
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()

        if s == "<!-- PAGEBREAK -->":
            blocks.append(("pagebreak", None)); i += 1; continue
        if s == "<!-- TOC -->":
            blocks.append(("toc", None)); i += 1; continue
        if s == "<!-- COVER -->":
            blocks.append(("cover", None)); i += 1; continue
        if s == "<!-- LOF -->":
            blocks.append(("lof", None)); i += 1; continue
        if s == "<!-- HARDCOVER -->":
            blocks.append(("hardcover", None)); i += 1; continue
        if s == "<!-- FRONTMATTER -->":
            blocks.append(("frontmatter", None)); i += 1; continue
        if s == "<!-- DRAWING INDEX -->":
            blocks.append(("drawindex", None)); i += 1; continue
        m = re.match(r"^<!--\s*FIG:\s*([A-Za-z0-9_]+)\s*-->$", s)
        if m:
            blocks.append(("fig", m.group(1))); i += 1; continue
        if s.startswith("<!--"):
            while i < len(lines) and "-->" not in lines[i]:
                i += 1
            i += 1; continue
        if not s:
            i += 1; continue
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", s):
            blocks.append(("hr", None)); i += 1; continue

        if s.startswith("```"):
            i += 1
            buf = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i].rstrip("\n")); i += 1
            i += 1
            blocks.append(("code", buf)); continue

        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            blocks.append(("h%d" % len(m.group(1)), m.group(2).strip()))
            i += 1; continue

        if s.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            blocks.append(("quote", parse_quote(buf))); continue

        if s.startswith("|") and i + 1 < len(lines) and \
           re.match(r"^\|[\s:|-]+\|?$", lines[i + 1].strip()):
            rows = [split_row(lines[i])]
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i])); i += 1
            blocks.append(("table", rows)); continue

        m = re.match(r"^([-*+]|\d+\.)\s+(.*)$", s)
        if m:
            items, ordered = [], bool(re.match(r"^\d+\.", m.group(1)))
            while i < len(lines):
                mm = re.match(r"^\s*([-*+]|\d+\.)\s+(.*)$", lines[i])
                if mm:
                    items.append(mm.group(2).strip()); i += 1
                elif lines[i].strip() and lines[i].startswith(("  ", "\t")):
                    items[-1] += " " + lines[i].strip(); i += 1
                else:
                    break
            blocks.append(("list", (ordered, items))); continue

        buf = []
        while i < len(lines) and lines[i].strip() and \
                not re.match(r"^\s*(#{1,4}\s|>|\||```|[-*+]\s|\d+\.\s|"
                             r"-{3,}$|<!--)", lines[i]):
            buf.append(lines[i].strip()); i += 1
        if buf:
            blocks.append(("p", " ".join(buf)))
        else:
            i += 1
    return blocks


def parse_quote(buf):
    """A call-out may hold paragraphs, one code block and tables."""
    out, i = [], 0
    while i < len(buf):
        s = buf[i].strip()
        if not s:
            i += 1; continue
        if s.startswith("```"):
            i += 1; code = []
            while i < len(buf) and not buf[i].strip().startswith("```"):
                code.append(buf[i]); i += 1
            i += 1
            out.append(("code", code)); continue
        if s.startswith("|") and i + 1 < len(buf) and \
           re.match(r"^\|[\s:|-]+\|?$", buf[i + 1].strip()):
            rows = [split_row(buf[i])]; i += 2
            while i < len(buf) and buf[i].strip().startswith("|"):
                rows.append(split_row(buf[i])); i += 1
            out.append(("table", rows)); continue
        para = []
        while i < len(buf) and buf[i].strip() and \
                not buf[i].strip().startswith(("|", "```")):
            para.append(buf[i].strip()); i += 1
        if para:
            out.append(("p", " ".join(para)))
    return out


# ------------------------------------------------------------------ heading
class FigureList(TableOfContents):
    """A contents list fed by FIGEntry notifications only."""

    def notify(self, kind, stuff):
        if kind == "FIGEntry":
            self.addEntry(*stuff)


class FigCaption(Paragraph):
    """The caption under a figure;  it is what registers the figure."""

    def __init__(self, num, caption, key):
        Paragraph.__init__(self,
                           inline("**Figure %d**   %s" % (num, caption)),
                           ST["figcap"])
        self._figEntry = (num, caption, key)


def figure_block(name, num, key):
    """A drawn figure and its caption, kept on one page."""
    drawing, caption = FIGS.figure(name)
    if drawing.width > BODY_W:                       # never overflow the page
        sc = BODY_W / float(drawing.width)
        drawing.scale(sc, sc)
        drawing.width *= sc
        drawing.height *= sc
    return KeepTogether([Spacer(1, 3), drawing,
                         FigCaption(num, caption, key)])


class Head(Paragraph):
    """A heading that registers itself with the contents list."""

    def __init__(self, text, style, level, key):
        Paragraph.__init__(self, inline(text), style)
        self._tocEntry = (level, text, key)

    def draw(self):
        Paragraph.draw(self)
        lvl, txt, key = self._tocEntry
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(sanitize(re.sub(r"[*`]", "", txt)),
                                  key, lvl, 0)


class PartHead(Table):
    pass


# ---------------------------------------------------------------- document
ROMAN = [(1000, "m"), (900, "cm"), (500, "d"), (400, "cd"), (100, "c"),
         (90, "xc"), (50, "l"), (40, "xl"), (10, "x"), (9, "ix"), (5, "v"),
         (4, "iv"), (1, "i")]


def roman(n):
    out = ""
    for v, r in ROMAN:
        while n >= v:
            out += r
            n -= v
    return out


class Report(BaseDocTemplate):
    def __init__(self, path, meta, first="cover"):
        BaseDocTemplate.__init__(self, path, pagesize=A4,
                                 leftMargin=LM, rightMargin=RM,
                                 topMargin=TM, bottomMargin=BM,
                                 title=meta["title"], author=meta["author"],
                                 subject=meta["subject"], creator=DOCREF)
        self.meta = meta
        pad = dict(leftPadding=0, rightPadding=0, topPadding=0,
                   bottomPadding=0)
        frame = Frame(LM, BM, BODY_W, PH - TM - BM, id="body", **pad)
        blank = Frame(LM, BM, BODY_W, PH - TM - BM, id="blank", **pad)
        board = Frame(0, 0, PW, PH, id="board", **pad)
        formal = Frame(FL, FB, FRONT_W, FRONT_H, id="formal", **pad)
        tpls = {"hardcover": PageTemplate(id="hardcover", frames=[board],
                                          onPageEnd=self.board_label),
                "cover": PageTemplate(id="cover", frames=[blank],
                                      onPage=self.cover_furniture),
                "front": PageTemplate(id="front", frames=[formal],
                                      onPageEnd=self.front_furniture),
                "main": PageTemplate(id="main", frames=[frame],
                                     onPageEnd=self.furniture)}
        # the first template in the list is the one page 1 is laid out on
        order = [first] + [k for k in tpls if k != first]
        self.addPageTemplates([tpls[k] for k in order])
        self.part = ""
        self.front_start = None
        self.body_start = None

    def beforeDocument(self):
        # multiBuild runs the story twice; the running head must not carry
        # the last part of the previous pass into the first pages of this one
        self.part = ""
        self.front_start = None
        self.body_start = None

    # ---- page numbering: covers unnumbered, front matter i, ii ..., body 1..
    def logical(self, page):
        """The number printed on a body page."""
        return page - self.body_start + 1 if self.body_start else page

    def _front_no(self, c):
        page = c.getPageNumber()
        if self.front_start is None:
            self.front_start = page
            c.addPageLabel(page - 1, style="ROMAN_LOWER", start=1)
        return page - self.front_start + 1

    def page_label(self, c):
        page = c.getPageNumber()
        if self.body_start and page >= self.body_start:
            return "Page %d" % self.logical(page)
        return "Page %s" % roman(self._front_no(c))

    def board_label(self, c, doc):
        c.addPageLabel(c.getPageNumber() - 1, prefix="Hard cover")

    def front_furniture(self, c, doc):
        n = self._front_no(c)
        if n > 1:                       # the certificate's i is not printed
            c.saveState()
            c.setFont("FMSerif", 11)
            c.setFillColor(INK)
            c.drawCentredString(PW / 2.0, 17 * mm, roman(n))
            c.restoreState()

    # running head / foot
    def furniture(self, c, doc):
        c.saveState()
        c.setFont("RepSans", 6.8)
        c.setFillColor(MID)
        c.drawString(LM, PH - TM + 7,
                     sanitize(self.part or self.meta["shorttitle"]))
        c.drawRightString(PW - RM, PH - TM + 7, DOCREF)
        c.setStrokeColor(RULE)
        c.setLineWidth(0.45)
        c.line(LM, PH - TM + 4, PW - RM, PH - TM + 4)
        c.line(LM, BM - 7, PW - RM, BM - 7)
        c.setFont("RepSans", 6.8)
        c.drawString(LM, BM - 15, sanitize(self.meta["footer"]))
        c.drawRightString(PW - RM, BM - 15, self.page_label(c))
        c.restoreState()

    def cover_furniture(self, c, doc):
        c.saveState()
        c.addPageLabel(c.getPageNumber() - 1, prefix="Title page")
        c.setFillColor(ACCENT)
        c.rect(0, PH - 34 * mm, PW, 34 * mm, stroke=0, fill=1)
        c.setFillColor(colors.Color(0.86, 0.66, 0.20))
        c.rect(0, PH - 36.6 * mm, PW, 2.6 * mm, stroke=0, fill=1)
        c.setFillColor(ACCENT)
        c.rect(0, 0, PW, 12 * mm, stroke=0, fill=1)
        c.restoreState()

    def afterFlowable(self, flowable):
        fig = getattr(flowable, "_figEntry", None)
        if fig is not None:
            num, cap, key = fig
            clean = sanitize(re.sub(r"[*`]", "", cap))
            self.canv.bookmarkPage(key)
            self.notify("FIGEntry",
                        (0, "Figure %d   %s" % (num, clean),
                         self.logical(self.page), key))
            return
        entry = getattr(flowable, "_tocEntry", None)
        if entry is None:
            return
        lvl, txt, key = entry
        clean = sanitize(re.sub(r"[*`]", "", txt))
        if lvl == 0:                                   # part banner
            if self.body_start is None:                # Part 1 is page 1
                self.body_start = self.page
                self.canv.addPageLabel(self.page - 1, style="ARABIC", start=1)
            self.part = clean
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(clean, key, 0, 0)
        if lvl <= 1:          # parts and sections only -- h3 stays a bookmark
            self.notify("TOCEntry",
                        (lvl, clean, self.logical(self.page), key))


# ------------------------------------------------------------ drawing index
def _index_order():
    """make_index.ORDER -- the QA tool's own discipline order, read from the
    tool rather than copied, so the report's index groups as the tool does."""
    spec = importlib.util.spec_from_file_location("make_index", MAKE_INDEX)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return list(mod.ORDER)


def _scale(s):
    t = s.strip().rstrip(".").strip()
    if t in ("-", ""):
        return "\u2014"
    if t.lower() == "not to scale":
        return "NOT TO SCALE"
    return t


INDEX_STATS = {}


def drawing_index():
    """The drawing index as a report table, read at build time from the QA
    tool's qa_index.json -- which the tool reads from the DXF files -- so the
    report's index cannot drift from the drawings.  A discipline missing from
    make_index.ORDER is NOT dropped (the H.25 failure): it is appended and
    reported."""
    with open(QA_INDEX, encoding="utf-8") as fh:
        rows = json.load(fh)
    order = _index_order()
    extra = sorted({r["discipline"] for r in rows} - set(order))
    groups = [(d, sorted([r for r in rows if r["discipline"] == d],
                         key=lambda r: r["number"]))
              for d in order + extra]
    groups = [(d, rs) for d, rs in groups if rs]
    sizes = {}
    for r in rows:
        sizes[r["size"]] = sizes.get(r["size"], 0) + 1
    listed = sum(len(rs) for _, rs in groups)
    INDEX_STATS.update(total=len(rows), listed=listed, groups=len(groups),
                       sizes=sizes, unregistered=extra)

    head = ["No.", "Drawing No.", "Title", "Scale", "Sheet size"]
    data = [[para(inline(h), ST["th"]) for h in head]]
    cmds = [("BACKGROUND", (0, 0), (-1, 0), HDRBG),
            ("LINEBELOW", (0, 0), (-1, 0), 0.7, MID),
            ("GRID", (0, 0), (-1, -1), 0.3, RULE),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 3.6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 3.6),
            ("TOPPADDING", (0, 0), (-1, -1), 2.4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2.4)]
    n = 0
    for disc, rs in groups:
        name = disc.replace(" - ", " \u2014 ")
        data.append([para(inline("**%s** (%d)" % (name, len(rs))), ST["th"]),
                     "", "", "", ""])
        i = len(data) - 1
        cmds += [("SPAN", (0, i), (-1, i)),
                 ("BACKGROUND", (0, i), (-1, i), BAND),
                 ("TOPPADDING", (0, i), (-1, i), 3.4)]
        for r in rs:
            n += 1
            data.append([para(str(n), ST["td"]),
                         para(inline("**%s**" % r["number"]), ST["td"]),
                         para(inline(r["title"]), ST["td"]),
                         para(inline(_scale(r["scale"])), ST["td"]),
                         para(r["size"], ST["td"])])
    cw = [10 * mm, 21 * mm, 0, 25 * mm, 18 * mm]
    cw[2] = BODY_W - sum(cw)
    t = Table(data, colWidths=cw, repeatRows=1)
    t.setStyle(TableStyle(cmds))

    size_txt = " · ".join("%d %s" % (k, s) for s, k in
                          sorted(sizes.items(), key=lambda kv: -kv[1]))
    intro = ("**%d drawings** · %s, in %d groups. Read at build time from "
             "`DRAWING QAQC/qa_index.json`, which the drawing QA tool "
             "generates from the DXF files themselves, so this index cannot "
             "drift from the drawings." % (len(rows), size_txt, len(groups)))
    note = ("\u2014 in the Scale column: no single scale is stated in the "
            "sheet's title block; see the sheet. Every scale is true at the "
            "sheet size given, **not** on the A3 page.")
    return [para(inline(intro), ST["body"]), Spacer(1, 2), t, Spacer(1, 4),
            para(inline(note), ST["cap"])]


NUMWORDS = ("zero one two three four five six seven eight nine ten eleven "
            "twelve thirteen fourteen fifteen sixteen seventeen eighteen "
            "nineteen").split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()


def words(n):
    if n < 20:
        return NUMWORDS[n]
    t, u = divmod(n, 10)
    return TENS[t] + ("-" + NUMWORDS[u] if u else "")


def counts(blocks):
    """Parts, appendices and figures, counted from the source -- the cover
    states them, and a stated count must follow the document it counts."""
    h1 = [p for k, p in blocks if k == "h1"]
    return (sum(1 for p in h1 if p.upper().startswith("PART ")),
            sum(1 for p in h1 if p.upper().startswith("APPENDIX ")),
            sum(1 for k, _ in blocks if k == "fig"))


def build(md, meta):
    register_fonts()
    FRONT.setup()
    blocks = parse(md)
    story = []
    nparts, napps, nfigs = counts(blocks)
    meta = dict(meta)
    meta["cover_notes"] = [n.replace("{COUNTS}", "%s parts, %s appendices and "
                                     "%s drawn figures" % (
                                         words(nparts).capitalize(),
                                         words(napps), words(nfigs)))
                           for n in meta["cover_notes"]]
    kinds = [k for k, _ in blocks]
    nkey = [0]

    def key():
        nkey[0] += 1
        return "h%04d" % nkey[0]

    toc = TableOfContents()
    toc.levelStyles = [ST["toc1"], ST["toc2"]]
    toc.dotsMinLevel = 0

    lof = FigureList()
    lof.levelStyles = [ST["lof"]]
    lof.dotsMinLevel = 1
    nfig = [0]

    def brk():
        """One page break, never two in a row (which leaves a blank page)."""
        if story and isinstance(story[-1], PageBreak):
            return
        story.append(PageBreak())

    for bi, (kind, payload) in enumerate(blocks):
        nxt = kinds[bi + 1] if bi + 1 < len(kinds) else None
        if kind == "hardcover":
            story.append(FRONT.HardCover(PW, PH))
            story.append(NextPageTemplate("cover" if nxt == "cover"
                                          else "main"))
            story.append(PageBreak())
        elif kind == "cover":
            story += cover_page(meta, "front" if nxt == "frontmatter"
                                else "main")
        elif kind == "frontmatter":
            sheets = FRONT.front_pages(FRONT_W, FRONT_H)
            for k, sh in enumerate(sheets):
                story.append(sh)
                if k == len(sheets) - 1:
                    story.append(NextPageTemplate("main"))
                story.append(PageBreak())
        elif kind == "drawindex":
            story += drawing_index()
        elif kind == "toc":
            story.append(Paragraph(inline("CONTENTS"), ST["h2"]))
            story.append(Rule(BODY_W))
            story.append(toc)
            brk()
        elif kind == "lof":
            story.append(Paragraph(inline("LIST OF FIGURES"), ST["h2"]))
            story.append(Rule(BODY_W))
            story.append(lof)
            brk()
        elif kind == "fig":
            nfig[0] += 1
            story.append(figure_block(payload, nfig[0], key()))
        elif kind == "pagebreak":
            brk()
        elif kind == "hr":
            story.append(Rule(BODY_W))
        elif kind == "h1":
            brk()
            story.append(part_banner(payload, key()))
            story.append(Spacer(1, 9))
        elif kind == "h2":
            story.append(KeepTogether([Head(payload, ST["h2"], 1, key()),
                                       Rule(BODY_W, RULE, 0.45, 1.6)]))
        elif kind == "h3":
            story.append(Head(payload, ST["h3"], 2, key()))
        elif kind == "h4":
            story.append(para(inline(payload), ST["h4"]))
        elif kind == "p":
            story.append(para(inline(payload), ST["body"]))
        elif kind == "list":
            ordered, items = payload
            for n, it in enumerate(items, 1):
                bullet = "%d." % n if ordered else "•"
                story.append(para(inline(it), ST["li"],
                                  bulletText=bullet))
            story.append(Spacer(1, 3))
        elif kind == "code":
            story.append(code_block(payload))
            story.append(Spacer(1, 6))
        elif kind == "table":
            story.append(make_table(payload))
            story.append(Spacer(1, 7))
        elif kind == "quote":
            story += quote_box(payload)

    doc = Report(OUT, meta, first=kinds[0] if kinds and kinds[0] in
                 ("hardcover", "cover") else "main")
    doc.multiBuild(story)
    return doc.page


def cover_page(meta, next_template="main"):
    out = [Spacer(1, 26 * mm)]
    out.append(Paragraph(inline(meta["title"]), ST["cvt"]))
    out.append(Spacer(1, 5))
    out.append(Paragraph(inline(meta["subtitle"]), ST["cvs"]))
    out.append(Spacer(1, 9 * mm))
    out.append(Rule(BODY_W, ACCENT, 1.1, 2))
    out.append(Spacer(1, 5 * mm))
    rows = meta["cover_rows"]
    t = make_table(rows)
    out.append(t)
    out.append(Spacer(1, 7 * mm))
    for para in meta["cover_notes"]:
        out.append(Paragraph(inline(para), ST["cvn"]))
        out.append(Spacer(1, 3.4))
    out.append(NextPageTemplate(next_template))
    out.append(PageBreak())
    return out


META = {
    "title": "UNDERGROUND CBRN-HARDENED BLAST-RESISTANT "
             "PROTECTIVE STRUCTURE, WITH SENTRY POST",
    "subtitle": "Pune, Maharashtra · Master project report",
    "author": "B.E. Civil Engineering capstone project",
    "subject": "Design basis, engineering science, calculations, drawings, "
               "services and works management",
    "shorttitle": "MASTER PROJECT REPORT \u00b7 FRONT MATTER",
    "footer": "Master project report · revision PR3 · "
              "FOR REVIEW — NOT FOR CONSTRUCTION",
    "cover_rows": [
        ["Item", "State"],
        ["Report revision", "**PR3** · 26 September 2026"],
        ["Architectural revision", "**Rev F**"],
        ["Structural revision", "**Phase 2 Rev A + M1**"],
        ["Design report revision (historical)", "Rev D"],
        ["Design content current to",
         "RC10 (package impact register) · DR-A2 (sump pit head), "
         "12 September 2026. **Later revisions — WM4, SR1/SR2, MEP1/MEP2 — "
         "are recorded in the master and are not yet carried into this "
         "report**, except the drawing index of Part 14"],
        ["Drawing index", "Read from the drawing QA tool at build time — "
         "current to **MEP2A**, 18 September 2026. **The drawings themselves "
         "are a separate spiral-bound book of A3 pages**"],
        ["Governing authority",
         "`master/MASTER_PROJECT_STATE.md` — Parts A, B, F and L"],
        ["Status", "**FOR REVIEW — NOT FOR CONSTRUCTION**"],
    ],
    "cover_notes": [
        "This report states the project once, in the order an engineer would "
        "need it to reproduce the design: the science first, then the site, "
        "then the loads, then the calculations, then the openings, then what "
        "is drawn, then the services, then how it is built — and then what is "
        "still open.",
        "**It is a statement of the design as it stands, not a history of how "
        "it got there.** Every value carries the evidence class the master "
        "gives it. Where the project does not hold a number, this report says "
        "so in the same sentence rather than filling it in.",
        "**{COUNTS}.** "
        "The figures are generated from the confirmed geometry in project "
        "coordinates. They are **not** the issued drawings and must never be "
        "used for setting out or fabrication.",
        "**Where this report and the master disagree, the master governs.**",
    ],
}


def main():
    if not os.path.exists(SRC):
        sys.exit("source not found: " + SRC)
    with open(SRC, encoding="utf-8") as fh:
        md = fh.read()
    pages = build(md, META)
    size = os.path.getsize(OUT)
    print("built   %s" % OUT)
    print("pages   %d" % pages)
    print("size    %.1f kB" % (size / 1024.0))
    print("source  %s (%d lines, %.1f kB)"
          % (os.path.basename(SRC), md.count("\n") + 1, len(md) / 1024.0))
    if BADMARKUP:
        print("MARKUP FALLBACK (%d) -- tags stripped, text kept:"
              % len(BADMARKUP))
        for txt, err in BADMARKUP:
            print("   %s | %s" % (txt, err))
    if INDEX_STATS:
        print("index   %d drawings in %d groups, %d listed%s"
              % (INDEX_STATS["total"], INDEX_STATS["groups"],
                 INDEX_STATS["listed"],
                 ("  -- NOT REGISTERED in make_index.ORDER, appended: "
                  + ", ".join(INDEX_STATS["unregistered"]))
                 if INDEX_STATS["unregistered"] else ""))
    if FRONT.OVERFLOW:
        for name, over in FRONT.OVERFLOW:
            print("FRONT MATTER OVERFLOW  %s by %.1f mm" % (name, over))
    if FRONT.PENDING:
        print("FRONT MATTER -- %d particulars still to be supplied "
              "(printed in red):" % len(FRONT.PENDING))
        for label in FRONT.PENDING:
            print("   [%s]" % label)
    else:
        print("front   every particular supplied")
    if MISSING:
        print("SUBSTITUTED (no face carries these): %s"
              % ", ".join("U+%04X x%d" % (ord(c), n)
                          for c, n in sorted(MISSING.items())))
    else:
        print("glyphs  every character drawn by a real glyph")
    print("built   %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))


if __name__ == "__main__":
    main()
