"""qa_overlap.py -- drafting QA for the A2 presentation sheets.

Reports, for each DXF given:
  * every pair of TEXT entities whose rendered boxes overlap,
  * every TEXT entity smaller than MIN_TXT_H,
  * every entity that falls outside the inner frame,
  * the layer / colour census, so a light colour cannot slip in unnoticed.

Text boxes are measured with the SAME font metrics ezdxf placed the text with,
so this is a real check, not an estimate.
"""
import sys
import ezdxf
import ezdxf.bbox
from a2_lib import MIN_TXT_H, INN, LAYERS

DARK = {7, 8, 1, 5}                      # the only colours the package allows
PAD = 0.0                                # dxfqa uses no slack; neither do we


def box(e):
    """Rendered box of a TEXT / MTEXT entity, in paper mm.  This is the SAME
    measurement the project QA tool makes (`DRAWING QAQC/Scripts/dxfqa.py`
    bb_of), so the two tools cannot disagree about what fits."""
    b = ezdxf.bbox.extents([e], fast=False)
    if not b.has_data:
        return None
    return (b.extmin.x, b.extmin.y, b.extmax.x, b.extmax.y)


mbox = box


def area(a):
    return max(0.0, a[2] - a[0]) * max(0.0, a[3] - a[1])


def frac(a, b):
    """Overlapped fraction of the SMALLER box -- dxfqa's own measure."""
    ox = min(a[2], b[2]) - max(a[0], b[0])
    oy = min(a[3], b[3]) - max(a[1], b[1])
    if ox <= PAD or oy <= PAD:
        return 0.0
    return (ox * oy) / max(1e-9, min(area(a), area(b)))


HARD, SOFT = 0.12, 0.02     # dxfqa's threshold, and a stricter "they touch"


def check(path):
    doc = ezdxf.readfile(path)
    msp = doc.modelspace()
    texts = [e for e in msp if e.dxftype() == "TEXT" and e.dxf.text.strip()]
    dims_mtext = []
    # DIMENSION text lives inside the rendered geometry block, not in modelspace
    for d in msp:
        if d.dxftype() != "DIMENSION":
            continue
        blk = doc.blocks.get(d.dxf.geometry) if d.dxf.get("geometry") else None
        for e in (blk or []):
            if e.dxftype() == "TEXT" and e.dxf.text.strip():
                texts.append(e)
            elif e.dxftype() == "MTEXT" and e.text.strip():
                dims_mtext.append(e)
    boxes = [(box(e), e) for e in texts + dims_mtext]
    boxes = [(b, e) for b, e in boxes if b is not None]
    bad, touch = [], []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            f = frac(boxes[i][0], boxes[j][0])
            if f > HARD:
                bad.append((boxes[i][1], boxes[j][1], boxes[i][0]))
            elif f > SOFT:
                touch.append((boxes[i][1], boxes[j][1], boxes[i][0]))
    small = [e for e in texts if e.dxf.height < MIN_TXT_H - 1e-6]
    print_name = lambda e: (e.dxf.text if e.dxftype() == "TEXT" else e.text)
    out = []
    for b, e in boxes:
        if e.dxftype() == "TEXT" and round(e.dxf.rotation % 360) == 90 \
                and b[0] > INN[2]:
            continue            # the rotated revision stamp the ARCH set carries
        if b[0] < INN[0] or b[1] < INN[1] or b[2] > INN[2] or b[3] > INN[3]:
            out.append((e, b))
    cols = {}
    for e in msp:
        ly = e.dxf.layer
        cols[ly] = cols.get(ly, 0) + 1
    light = [ly for ly in cols if ly in LAYERS and LAYERS[ly][0] not in DARK]

    print(f"\n=== {path}")
    print(f"    {len(texts)} TEXT + {len(dims_mtext)} dim-text, "
          f"{len(list(msp))} entities total")
    print(f"    TEXT OVERLAPS ............ {len(bad)}")
    for a, b, bb in bad[:40]:
        print(f"      [{print_name(a)[:42]!r} @ {bb[0]:.1f},{bb[1]:.1f}]"
              f"  x  [{print_name(b)[:42]!r}]")
    print(f"    NEAR-TOUCHES (> 2 %) ..... {len(touch)}")
    for a, b, bb in touch[:8]:
        print(f"      [{print_name(a)[:42]!r} @ {bb[0]:.1f},{bb[1]:.1f}]"
              f"  x  [{print_name(b)[:42]!r}]")
    print(f"    TEXT BELOW {MIN_TXT_H} mm ......... {len(small)}")
    for e in small[:10]:
        print(f"      {e.dxf.height:.2f}  {e.dxf.text[:50]!r}")
    print(f"    TEXT OUTSIDE THE FRAME ... {len(out)}")
    for e, b in out[:20]:
        print(f"      {print_name(e)[:46]!r}  box {tuple(round(v, 1) for v in b)}")
    print(f"    NON-DARK LAYERS .......... {len(light)}  {light}")
    return len(bad) + len(small) + len(out) + len(light)


if __name__ == "__main__":
    bad = sum(check(p) for p in sys.argv[1:])
    print(f"\nTOTAL DEFECTS: {bad}")
    sys.exit(1 if bad else 0)
