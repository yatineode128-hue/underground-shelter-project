"""dxfqa.py - inventory + automated drafting QA for the project DXF package."""
import sys, os, math, json, glob
from collections import Counter, defaultdict
import ezdxf, ezdxf.bbox

SHEET = (0.0, 0.0, 841.0, 594.0)          # A1 default; overridden per-file by frame detect
INNER = (10.0, 10.0, 831.0, 584.0)
TB    = (651.0, 10.0, 831.0, 110.0)

def bb_of(e):
    try:
        b = ezdxf.bbox.extents([e], fast=False)
        if not b.has_data: return None
        return (b.extmin.x, b.extmin.y, b.extmax.x, b.extmax.y)
    except Exception:
        return None

def overlap(a, b, tol=0.0):
    ox = min(a[2], b[2]) - max(a[0], b[0]) - tol
    oy = min(a[3], b[3]) - max(a[1], b[1]) - tol
    if ox > 0 and oy > 0:
        return ox * oy
    return 0.0

def area(a):
    return max(0.0, a[2]-a[0]) * max(0.0, a[3]-a[1])

def plain(e):
    t = e.dxftype()
    if t == "TEXT": return e.dxf.text
    if t == "MTEXT": return e.plain_text()
    if t == "ATTRIB": return e.dxf.text
    return ""

def detect_frame(msp):
    """Find the outer sheet rectangle from closed LWPOLYLINEs."""
    best = None
    for e in msp.query("LWPOLYLINE"):
        pts = [(p[0], p[1]) for p in e.get_points()]
        if len(pts) != 4: continue
        xs = sorted(set(round(p[0],3) for p in pts)); ys = sorted(set(round(p[1],3) for p in pts))
        if len(xs) != 2 or len(ys) != 2: continue
        r = (xs[0], ys[0], xs[1], ys[1])
        if best is None or area(r) > area(best): best = r
    return best

def audit(path):
    doc = ezdxf.readfile(path)
    msp = doc.modelspace()
    ents = list(msp)
    types = Counter(e.dxftype() for e in ents)
    frame = detect_frame(msp) or SHEET
    W, H = frame[2]-frame[0], frame[3]-frame[1]
    inner = (frame[0]+10, frame[1]+10, frame[2]-10, frame[3]-10)

    texts = []
    for e in ents:
        if e.dxftype() not in ("TEXT", "MTEXT"): continue
        s = plain(e).strip()
        if not s: continue
        b = bb_of(e)
        if b is None: continue
        h = e.dxf.height if e.dxftype()=="TEXT" else e.dxf.char_height
        texts.append(dict(e=e, s=s, bb=b, h=h, layer=e.dxf.layer, t=e.dxftype()))

    # --- checks
    issues = defaultdict(list)
    # 1 text height range
    for t in texts:
        if t["h"] < 1.3: issues["tiny_text"].append((round(t["h"],2), t["s"][:50], (round(t["bb"][0]),round(t["bb"][1]))))
        if t["h"] > 8.0: issues["huge_text"].append((round(t["h"],2), t["s"][:50], (round(t["bb"][0]),round(t["bb"][1]))))
    # 2 outside inner border
    for t in texts:
        b = t["bb"]
        if b[0] < inner[0]-0.6 or b[1] < inner[1]-0.6 or b[2] > inner[2]+0.6 or b[3] > inner[3]+0.6:
            issues["outside_inner"].append((t["s"][:50], tuple(round(v,1) for v in b), t["layer"]))
    # 3 outside sheet entirely
    for e in ents:
        b = bb_of(e)
        if b is None: continue
        if b[0] < frame[0]-0.5 or b[1] < frame[1]-0.5 or b[2] > frame[2]+0.5 or b[3] > frame[3]+0.5:
            issues["outside_sheet"].append((e.dxftype(), e.dxf.layer, tuple(round(v,1) for v in b)))
    # 4 text-text overlap
    ts = sorted(texts, key=lambda t: t["bb"][0])
    n = len(ts)
    for i in range(n):
        a = ts[i]
        for j in range(i+1, n):
            b = ts[j]
            if b["bb"][0] > a["bb"][2]: break
            ov = overlap(a["bb"], b["bb"], tol=0.0)
            if ov <= 0: continue
            frac = ov / max(1e-9, min(area(a["bb"]), area(b["bb"])))
            if frac > 0.12:
                issues["text_overlap"].append((round(frac,2), a["s"][:38], b["s"][:38],
                                               tuple(round(v,1) for v in a["bb"]),
                                               tuple(round(v,1) for v in b["bb"]),
                                               a["layer"], b["layer"]))
    # 5 duplicate text at same spot
    seen = defaultdict(int)
    for t in texts:
        k = (t["s"], round(t["bb"][0],1), round(t["bb"][1],1))
        seen[k] += 1
    for k,v in seen.items():
        if v > 1: issues["duplicate_text"].append((k[0][:50], k[1], k[2], v))
    # 6 non-title text intruding into title block
    for t in texts:
        if t["layer"] in ("S-TITLE",): continue
        if overlap(t["bb"], TB) > 0.2 * area(t["bb"]):
            issues["into_titleblock"].append((t["s"][:50], tuple(round(v,1) for v in t["bb"]), t["layer"]))

    heights = Counter(round(t["h"],2) for t in texts)
    return dict(path=path, frame=tuple(round(v,1) for v in frame), size=(round(W,1), round(H,1)),
                types=dict(types), n_text=len(texts), heights=dict(sorted(heights.items())),
                issues={k: v for k, v in issues.items()},
                counts={k: len(v) for k, v in issues.items()})

if __name__ == "__main__":
    files = sys.argv[1:]
    out = []
    for f in files:
        try:
            out.append(audit(f))
        except Exception as ex:
            out.append(dict(path=f, error=str(ex)))
    print(json.dumps(out, indent=None))
