"""addsheet.py - give a model-space Rev F drawing a proper A1 sheet, IN PLACE.

The ten Rev F drawings are drawn in model millimetres with no border, no title
block and no notes box: they are drawings, not sheets.  This adds the sheet
around the existing drawing without moving one line of it:

    A1 841 x 594 at the drawing's OWN stated scale, drawn in model units
    outer border, inner border 10 mm, title block 180 x 100 bottom right
    revision strip recording this QA pass

Everything is LINE + TEXT so the R12 (AC1009) format the drawings already use
is preserved.  Nothing is rasterised and no existing entity is touched.
"""
import math, sys
import ezdxf, ezdxf.bbox

SHEET_W, SHEET_H = 841.0, 594.0
MARGIN = 10.0
TB_W, TB_H = 180.0, 100.0
FRAME_LAYER, TB_LAYER, TBTEXT_LAYER = "SHEET-BORDER", "SHEET-TITLEBLOCK", "SHEET-TEXT"

PROJECT_1 = "UNDERGROUND CBRN-HARDENED BLAST-RESISTANT"
PROJECT_2 = "PROTECTIVE STRUCTURE  -  PUNE, MAHARASHTRA"
PROJECT_3 = "ARCHITECTURAL REV F  +  MODIFICATION M1"
STATUS    = "FOR REVIEW - NOT FOR CONSTRUCTION"
REV       = "F + M1"
ISSUE     = "09.09.2026"
REVNOTE   = ("QA1  09.09.2026   DRAWING QA/QC - ANNOTATION POSITIONS, SHEET "
             "FRAME AND TITLE BLOCK.  NO GEOMETRY, DIMENSION OR VALUE CHANGED.")

def content_bbox(msp):
    b = ezdxf.bbox.extents(msp, fast=False)
    return (b.extmin.x, b.extmin.y, b.extmax.x, b.extmax.y)

def add_sheet(path, scale, number, title, subtitle, scale_note, sheet_of,
              sheet_w=SHEET_W, sheet_h=SHEET_H, verbose=True):
    doc = ezdxf.readfile(path); msp = doc.modelspace()
    for ly, col in ((FRAME_LAYER, 7), (TB_LAYER, 7), (TBTEXT_LAYER, 7)):
        if ly not in doc.layers: doc.layers.add(ly, color=col)
    # already framed?
    if len(msp.query(f'LINE[layer=="{FRAME_LAYER}"]')):
        if verbose: print(f"{path.split('/')[-1]:<50} already framed - skipped")
        return None

    SW, SH = float(sheet_w), float(sheet_h)
    s = float(scale)
    cx0, cy0, cx1, cy1 = content_bbox(msp)
    cw, ch = (cx1-cx0)/s, (cy1-cy0)/s                 # content size in PAPER mm

    # where the content sits on the sheet, in paper mm
    avail_l, avail_r = MARGIN + 5, SW - MARGIN - 5
    avail_b, avail_t = MARGIN + 5, SH - MARGIN - 5
    tb_left = SW - MARGIN - TB_W
    tb_top = MARGIN + TB_H                             # 110
    # top-aligned under the header strip, centred in the band that is clear of
    # the title block - the conventional way a sheet is composed, and it leaves
    # the spare paper where the title block already is.
    head = SH - MARGIN - 16.0
    if cw <= (tb_left - avail_l) - 4:                  # fits left of the title block
        px = avail_l + ((tb_left - 4) - avail_l - cw) / 2.0
        py = head - ch
    else:                                              # full width: keep clear above the TB
        px = avail_l + (avail_r - avail_l - cw) / 2.0
        py = max(tb_top + 6, head - ch)
    if py < avail_b:
        py = avail_b
    fits = (cw <= avail_r - avail_l + 1e-6) and (ch <= avail_t - avail_b + 1e-6)

    # frame origin in MODEL units: paper (0,0) of the sheet
    ox, oy = cx0 - px * s, cy0 - py * s
    def P(x, y): return (ox + x * s, oy + y * s)
    def line(a, b, layer=FRAME_LAYER): msp.add_line(P(*a), P(*b), dxfattribs={"layer": layer})
    def rect(x0, y0, x1, y1, layer=FRAME_LAYER):
        line((x0,y0),(x1,y0),layer); line((x1,y0),(x1,y1),layer)
        line((x1,y1),(x0,y1),layer); line((x0,y1),(x0,y0),layer)
    def txt(t, x, y, h, layer=TBTEXT_LAYER, align=None):
        e = msp.add_text(str(t), height=h*s, dxfattribs={"layer": layer})
        e.set_placement(P(x, y)); return e

    rect(0, 0, SW, SH)
    rect(MARGIN, MARGIN, SW-MARGIN, SH-MARGIN)
    x, y = tb_left, MARGIN
    rect(x, y, x+TB_W, y+TB_H, TB_LAYER)
    for yy in (20, 32, 44, 56, 78):
        line((x, y+yy), (x+TB_W, y+yy), TB_LAYER)
    line((x+112, y), (x+112, y+20), TB_LAYER)
    line((x+146, y), (x+146, y+20), TB_LAYER)
    line((x+96, y+20), (x+96, y+32), TB_LAYER)

    txt("DRAWING No.", x+2,  y+14.6, 1.4); txt(number, x+16, y+4.2, 4.4)
    txt("REV",         x+114, y+14.6, 1.4); txt(REV,   x+114, y+4.6, 2.8)
    txt("SHEET",       x+148, y+14.6, 1.4); txt(sheet_of, x+148, y+5.0, 1.9)
    txt(f"SCALE   {scale_note}", x+2,  y+24.4, 1.9)
    txt(f"DATE   {ISSUE}",       x+98, y+24.4, 1.9)
    txt("DRAWN  [PLACEHOLDER]",    x+2,  y+36.4, 1.5)
    txt("CHECKED  [PLACEHOLDER]", x+62, y+36.4, 1.5)
    txt("APPROVED  [PLACEHOLDER]",x+122,y+36.4, 1.5)
    txt("STATUS", x+2, y+48.4, 1.4); txt(STATUS, x+22, y+48.0, 1.9)
    txt("DRAWING TITLE", x+2, y+73.4, 1.4)
    txt(title[:46], x+2, y+65.4, 2.4)
    if subtitle: txt(subtitle[:62], x+2, y+58.8, 1.5)
    txt("PROJECT", x+2, y+95.2, 1.4)
    txt(PROJECT_1, x+2, y+89.6, 1.9)
    txt(PROJECT_2, x+2, y+85.0, 1.9)
    txt(PROJECT_3, x+2, y+80.2, 1.5)

    # top strip + revision strip, both inside the inner border
    txt(f"{number}   {title}", MARGIN+2, SH-MARGIN-7.5, 3.2)
    line((MARGIN, SH-MARGIN-10.5), (SW-MARGIN, SH-MARGIN-10.5))
    txt(REVNOTE, MARGIN+2, MARGIN+2.5, 1.5)
    if verbose:
        size = "A1" if (SW, SH) == (841.0, 594.0) else ("A0" if (SW, SH) == (1189.0, 841.0) else f"{SW:.0f}x{SH:.0f}")
        print(f"{path.split('/')[-1]:<50} {size} @1:{scale:g}  content {cw:6.1f} x {ch:6.1f} mm"
              f"  at ({px:5.1f},{py:5.1f})  {'OK' if fits else '*** DOES NOT FIT ***'}")
    doc.saveas(path)
    return fits
