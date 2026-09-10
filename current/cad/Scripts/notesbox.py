"""notesbox.py - move a drawing's loose bottom notes into a proper notes box.

On the Rev F drawings the general notes are loose lines sitting immediately
under the drawing, which leaves the bottom third of the sheet empty and gives
the notes no boundary.  This moves that block, unchanged, to the bottom left of
the drawing area and rules a box round it with a NOTES heading.
"""
import sys
import ezdxf, ezdxf.bbox

FRAME_LAYER = "SHEET-BORDER"
SHEET_LAYERS = {"SHEET-BORDER", "SHEET-TITLEBLOCK", "SHEET-TEXT"}
MARGIN, TB_W, TB_H = 10.0, 180.0, 100.0

def bb(e):
    b = ezdxf.bbox.extents([e], fast=False)
    return (b.extmin.x, b.extmin.y, b.extmax.x, b.extmax.y) if b.has_data else None

def frame_of(msp):
    xs, ys = [], []
    for e in msp.query(f'LINE[layer=="{FRAME_LAYER}"]'):
        xs += [e.dxf.start.x, e.dxf.end.x]; ys += [e.dxf.start.y, e.dxf.end.y]
    return (min(xs), min(ys), max(xs), max(ys)) if xs else None

def run(path, sheet_w=841.0, verbose=True):
    doc = ezdxf.readfile(path); msp = doc.modelspace()
    fr = frame_of(msp)
    if not fr: 
        if verbose: print(f"{path.split('/')[-1]:<50} no frame - skipped")
        return
    fx0, fy0, fx1, fy1 = fr
    s = (fx1 - fx0) / sheet_w                       # model units per paper mm
    def P(px, py): return (fx0 + px * s, fy0 + py * s)

    geo_min_y = None
    for e in msp:
        if e.dxftype() == "TEXT" or e.dxf.layer in SHEET_LAYERS: continue
        b = bb(e)
        if b: geo_min_y = b[1] if geo_min_y is None else min(geo_min_y, b[1])
    if geo_min_y is None: return

    # A note line sits WELL below the drawing.  Anything hugging the drawing is
    # a drawing annotation (a second line of a two-line callout, say) and must
    # stay with it - an earlier version swept those into the notes box.
    cand = []
    for e in msp.query("TEXT"):
        if e.dxf.layer in SHEET_LAYERS: continue
        b = bb(e)
        if b and b[3] < geo_min_y + 1e-6:
            cand.append((e, b, e.dxf.height))
    if not cand:
        if verbose: print(f"{path.split('/')[-1]:<50} no loose notes block")
        return
    hmed = sorted(t[2] for t in cand)[len(cand)//2]
    cut = geo_min_y - 3.0 * hmed
    # a drawing whose own title sits BELOW the drawing (A-102 does) must not
    # have that title swept into the notes box - it is a title, not a note
    notes = [(e, b) for e, b, h in cand if b[3] < cut and h <= 1.6 * hmed]
    if len(notes) < 2:
        if verbose: print(f"{path.split('/')[-1]:<50} no loose notes block")
        return
    nx0 = min(b[0] for _, b in notes); ny0 = min(b[1] for _, b in notes)
    nx1 = max(b[2] for _, b in notes); ny1 = max(b[3] for _, b in notes)
    nw, nh = (nx1-nx0)/s, (ny1-ny0)/s               # paper mm

    pad = 3.0
    tx = MARGIN + 6
    ty = MARGIN + 8                                  # clear of the revision strip
    # keep the box clear of the title block
    if tx + nw + 2*pad > sheet_w - MARGIN - TB_W - 4:
        ty = max(ty, MARGIN + TB_H + 6)
    tgt = P(tx + pad, ty + pad)
    dx, dy = tgt[0] - nx0, tgt[1] - ny0
    for e, _ in notes: e.translate(dx, dy, 0)

    bx0, by0 = P(tx, ty)
    bx1, by1 = P(tx + nw + 2*pad, ty + nh + 2*pad + 6.0)
    for a, b in (((bx0,by0),(bx1,by0)), ((bx1,by0),(bx1,by1)),
                 ((bx1,by1),(bx0,by1)), ((bx0,by1),(bx0,by0))):
        msp.add_line(a, b, dxfattribs={"layer": "SHEET-BORDER"})
    h = msp.add_text("NOTES", height=2.6*s, dxfattribs={"layer": "SHEET-TEXT"})
    h.set_placement(P(tx + pad, ty + nh + 2*pad + 0.6))

    # balance: the drawing was top-aligned, so all the spare paper collected in
    # one band between it and the notes.  Share it above and below the drawing.
    note_set = {id(e) for e, _ in notes}
    block, bmin, bmax = [], None, None
    for e in msp:
        if e.dxf.layer in SHEET_LAYERS or id(e) in note_set: continue
        b = bb(e)
        if not b: continue
        block.append(e)
        bmin = b[1] if bmin is None else min(bmin, b[1])
        bmax = b[3] if bmax is None else max(bmax, b[3])
    if block and bmin is not None:
        top_free = (fy1 - fy0) / s - MARGIN - 16.0 - (bmax - fy0) / s
        bot_free = (bmin - fy0) / s - (ty + nh + 2*pad + 6.0) - 6.0
        shift = (bot_free - top_free) / 2.0
        if shift > 2.0:
            for e in block: e.translate(0, -shift * s, 0)
    doc.saveas(path)
    if verbose:
        print(f"{path.split('/')[-1]:<50} notes block {nw:5.1f} x {nh:5.1f} mm -> ({tx:.0f},{ty:.0f}) boxed")

if __name__ == "__main__":
    for p in sys.argv[1:]: run(p)
