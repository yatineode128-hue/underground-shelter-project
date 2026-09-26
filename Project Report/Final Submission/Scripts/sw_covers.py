"""
sw_covers.py -- the two black hard covers, in the layout of the owner's sample
(an earlier CME project report): gold lettering and a gold frame on black.

    python3 "Project Report/Final Submission/Scripts/sw_covers.py"

Writes, next to the report:
    Hard_Cover_Report_A4.pdf              the bound report, A4 portrait
    Hard_Cover_Drawings_A3_Landscape.pdf  the spiral-bound drawing book

The crest is Images/CME_crest_gold.png (see sw_crest.py).  Names are those
printed on the report's own first page (sw_render.MEMBERS / GUIDES).
"""

import os
import sys

from reportlab.lib import colors
from reportlab.lib.pagesizes import A3, A4, landscape
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sw_render as R                                          # noqa: E402

PKG = os.path.abspath(os.path.join(HERE, ".."))
CREST = os.path.join(PKG, "Images", "CME_crest_gold.png")
GOLD = colors.Color(212 / 255.0, 175 / 255.0, 55 / 255.0)
TITLE = "CBRN HARDENED UNDERGROUND OPS ROOM"
FONT = "Arial-Bold"


def ordered(names):
    """The two-column cover order of sw_render back to reading order."""
    half = (len(names) + 1) // 2
    out = []
    for i in range(half):
        out.append(names[i])
        if i + half < len(names):
            out.append(names[i + half])
    return out


MEMBERS = [n.upper() for n in ordered(R.MEMBERS)]
GUIDES = [n.upper() for n in R.GUIDES]


def text(c, x, y, s, size, centre=True, underline=False):
    w = stringWidth(s, FONT, size)
    x0 = x - w / 2.0 if centre else x
    c.setFont(FONT, size)
    c.drawString(x0, y, s)
    if underline:
        c.setLineWidth(max(0.8, size * 0.06))
        c.line(x0, y - size * 0.16, x0 + w, y - size * 0.16)


def frame(c, x, y, w, h):
    c.setStrokeColor(GOLD)
    c.setLineWidth(2.2)
    c.rect(x, y, w, h)
    c.setLineWidth(0.8)
    g = 2.2 * mm
    c.rect(x + g, y + g, w - 2 * g, h - 2 * g)


def crest(c, cx, y_top, height):
    img = ImageReader(CREST)
    iw, ih = img.getSize()
    w = height * iw / float(ih)
    c.drawImage(img, cx - w / 2.0, y_top - height, w, height, mask="auto")


def name_list(c, x, y, head, names, size, lead):
    text(c, x, y, head, size, centre=False, underline=True)
    for i, n in enumerate(names):
        text(c, x, y - (i + 1) * lead, n, size * 0.92, centre=False)


def background(c, pw, ph):
    c.setFillColor(colors.black)
    c.rect(0, 0, pw, ph, stroke=0, fill=1)
    c.setFillColor(GOLD)
    c.setStrokeColor(GOLD)


def report_cover(path):
    pw, ph = A4
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle("CBRN Hardened Underground Ops Room - Hard Cover")
    c.setAuthor("Syndicate 01")
    c.setProducer("Syndicate 01")
    background(c, pw, ph)
    fx, fy = 20 * mm, 22 * mm
    frame(c, fx, fy, pw - 2 * fx, ph - 2 * fy)
    c.setFillColor(GOLD)
    cx = pw / 2.0
    text(c, cx, ph - 48 * mm, "COLLEGE OF MILITARY ENGINEERING", 17,
         underline=True)
    crest(c, cx, ph - 62 * mm, 52 * mm)
    text(c, cx, ph - 136 * mm, "PROJECT REPORT", 20, underline=True)
    text(c, cx, ph - 162 * mm, TITLE, 16, underline=True)
    y = ph - 196 * mm
    name_list(c, fx + 14 * mm, y, "SYNDICATE 01", MEMBERS, 12.5, 8.4 * mm)
    name_list(c, cx + 8 * mm, y, "GUIDES", GUIDES, 12.5, 8.4 * mm)
    c.showPage()
    c.save()


def drawings_cover(path):
    pw, ph = landscape(A3)
    c = canvas.Canvas(path, pagesize=(pw, ph))
    c.setTitle("CBRN Hardened Underground Ops Room - Drawings - Cover")
    c.setAuthor("Syndicate 01")
    c.setProducer("Syndicate 01")
    background(c, pw, ph)
    fx, fy = 22 * mm, 20 * mm
    frame(c, fx, fy, pw - 2 * fx, ph - 2 * fy)
    c.setFillColor(GOLD)
    cx = pw / 2.0
    text(c, cx, ph - 46 * mm, "COLLEGE OF MILITARY ENGINEERING", 22,
         underline=True)
    crest(c, cx, ph - 58 * mm, 58 * mm)
    text(c, cx, ph - 136 * mm, "PROJECT DRAWINGS", 26, underline=True)
    text(c, cx, ph - 160 * mm, TITLE, 21, underline=True)
    text(c, cx, ph - 176 * mm, "DRAWING SHEETS 01 TO 15", 15)
    y = ph - 194 * mm
    name_list(c, fx + 62 * mm, y, "SYNDICATE 01", MEMBERS, 13, 7.6 * mm)
    name_list(c, cx + 36 * mm, y, "GUIDES", GUIDES, 13, 7.6 * mm)
    c.showPage()
    c.save()


def main():
    R.register_fonts()
    a = os.path.join(PKG, "Hard_Cover_Report_A4.pdf")
    b = os.path.join(PKG, "Hard_Cover_Drawings_A3_Landscape.pdf")
    report_cover(a)
    drawings_cover(b)
    print("written", a)
    print("written", b)


if __name__ == "__main__":
    main()
