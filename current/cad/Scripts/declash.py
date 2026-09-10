"""declash.py - move clashing annotation off geometry, IN PLACE, in a model-space DXF.

Only TEXT insertion points move.  No geometry, dimension, value or layer is
touched.  When a label has to travel more than ~2 text heights to find clear
space, a two-segment LINE leader is drawn back to where it started, so the
label stays tied to the thing it names.  LINE is used because these drawings
are AutoCAD R12 (AC1009), which has no LEADER or LWPOLYLINE entity.
"""
import math, sys
import ezdxf, ezdxf.bbox
from ezdxf.math import Vec3

# layers whose line work a label must not sit on
# HARD: line work a label must never sit on - the cut fabric of the drawing,
# its dimensions and its structured blocks.
# Everything else (GROUND, HIDDEN "below" lines, BEYOND, CENTRE, SOIL, HATCH)
# is background or reference; an annotation crossing it is normal drafting and
# is deliberately NOT treated as a clash - chasing those moves labels away from
# the objects they name for no gain.
SOLID = {"WALLS","STAIRS","OPENINGS","CONC","STRUCT","SERVICES",
         "REINF-MAIN","REINF-SEC","BLAST","DIM","TITLEBLOCK","TABLE",
         # once a sheet frame exists, a label may not cross it either
         "SHEET-BORDER","SHEET-TITLEBLOCK"}
# text on these layers is part of a structured block (title block, schedule,
# notes panel) or is a dimension value tied to its own line - never move it
PROTECTED = {"TITLEBLOCK", "TEXT-TITLE", "TABLE", "NOTES", "DIM"}
LEADER_LAYER = "LEADER"   # kept OUT of SOLID so a leader never pushes a label

def segments(e):
    t = e.dxftype()
    try:
        if t == "LINE":
            return [((e.dxf.start.x, e.dxf.start.y), (e.dxf.end.x, e.dxf.end.y))]
        if t == "LWPOLYLINE":
            pts = [(p[0], p[1]) for p in e.get_points()]
            sg = list(zip(pts[:-1], pts[1:]))
            if e.closed and len(pts) > 2: sg.append((pts[-1], pts[0]))
            return sg
        if t == "POLYLINE":
            pts = [(v.dxf.location.x, v.dxf.location.y) for v in e.vertices]
            sg = list(zip(pts[:-1], pts[1:]))
            if e.is_closed and len(pts) > 2: sg.append((pts[-1], pts[0]))
            return sg
        if t in ("ARC", "CIRCLE"):
            c, r = e.dxf.center, e.dxf.radius
            a0, a1 = (0.0, 360.0) if t == "CIRCLE" else (e.dxf.start_angle, e.dxf.end_angle)
            if a1 < a0: a1 += 360
            n = max(8, int((a1 - a0) / 15))
            pts = [(c.x + r*math.cos(math.radians(a0 + (a1-a0)*i/n)),
                    c.y + r*math.sin(math.radians(a0 + (a1-a0)*i/n))) for i in range(n+1)]
            return list(zip(pts[:-1], pts[1:]))
    except Exception:
        pass
    return []

def seg_rect(p1, p2, r):
    x0,y0,x1,y1 = r; ax,ay = p1; bx,by = p2
    if max(ax,bx) < x0 or min(ax,bx) > x1 or max(ay,by) < y0 or min(ay,by) > y1: return False
    if x0<=ax<=x1 and y0<=ay<=y1: return True
    if x0<=bx<=x1 and y0<=by<=y1: return True
    dx,dy = bx-ax, by-ay; t0,t1 = 0.0,1.0
    for p,q in ((-dx,ax-x0),(dx,x1-ax),(-dy,ay-y0),(dy,y1-ay)):
        if abs(p) < 1e-12:
            if q < 0: return False
        else:
            t = q/p
            if p < 0:
                if t > t1: return False
                t0 = max(t0,t)
            else:
                if t < t0: return False
                t1 = min(t1,t)
    return t0 <= t1

def bb(e):
    try:
        b = ezdxf.bbox.extents([e], fast=False)
        return (b.extmin.x,b.extmin.y,b.extmax.x,b.extmax.y) if b.has_data else None
    except Exception: return None

def inflate(r, m): return (r[0]-m, r[1]-m, r[2]+m, r[3]+m)
def shrink(r, f):
    w,h = r[2]-r[0], r[3]-r[1]
    return (r[0]+w*f, r[1]+h*f, r[2]-w*f, r[3]-h*f)
def ov(a,b):
    ox = min(a[2],b[2])-max(a[0],b[0]); oy = min(a[3],b[3])-max(a[1],b[1])
    return ox*oy if ox>0 and oy>0 else 0.0
def ar(a): return max(0,a[2]-a[0])*max(0,a[3]-a[1])

def declash(path, max_rings=22, verbose=True):
    doc = ezdxf.readfile(path); msp = doc.modelspace()
    # the printable area, if the drawing has already been given a sheet frame
    fxs, fys = [], []
    for e in msp.query('LINE[layer=="SHEET-BORDER"]'):
        fxs += [e.dxf.start.x, e.dxf.end.x]; fys += [e.dxf.start.y, e.dxf.end.y]
    if fxs:
        m = (max(fxs) - min(fxs)) * 12.0 / 841.0        # ~12 mm inside the border
        AREA = (min(fxs) + m, min(fys) + m, max(fxs) - m, max(fys) - m)
    else:
        AREA = None
    geo = []
    for e in msp:
        if e.dxftype() in ("TEXT","MTEXT"): continue
        if e.dxf.layer not in SOLID: continue
        for sg in segments(e): geo.append(sg)
    texts = []
    for e in msp:
        if e.dxftype() != "TEXT": continue
        s = e.dxf.text.strip()
        if not s: continue
        b = bb(e)
        if b: texts.append([e, s, b, e.dxf.height, e.dxf.layer not in PROTECTED])
    tboxes = [t[2] for t in texts]

    def clashes(rect, skip_idx):
        if AREA is not None and not (AREA[0] <= rect[0] and rect[2] <= AREA[2]
                                     and AREA[1] <= rect[1] and rect[3] <= AREA[3]):
            return True                                  # never leave the sheet
        r = shrink(rect, 0.12)
        for sg in geo:
            if seg_rect(sg[0], sg[1], r): return True
        for i, tb in enumerate(tboxes):
            if i == skip_idx: continue
            o = ov(rect, tb)
            if o > 0.12 * min(ar(rect), ar(tb)): return True
        return False

    origin = {i: t[2] for i, t in enumerate(texts)}     # where each label started
    moved_idx = set()
    for _pass in range(3):
        any_move = False
        for i, (e, s, b, h, movable) in enumerate(texts):
            if not movable: continue
            b = texts[i][2]
            if not clashes(b, i): continue
            step = max(h * 0.45, 1e-6)
            best = None
            for ring in range(1, max_rings+1):
                d = step * ring
                for ang in (90, 270, 0, 180, 45, 135, 315, 225,
                            22, 68, 112, 158, 202, 248, 292, 338):
                    dx, dy = d*math.cos(math.radians(ang)), d*math.sin(math.radians(ang))
                    cand = (b[0]+dx, b[1]+dy, b[2]+dx, b[3]+dy)
                    if not clashes(cand, i):
                        best = (dx, dy, cand); break
                if best: break
            if not best: continue
            dx, dy, cand = best
            e.translate(dx, dy, 0)
            tboxes[i] = cand; texts[i][2] = cand
            moved_idx.add(i); any_move = True
        if not any_move: break
    moved = len(moved_idx); leaders = 0
    for i in sorted(moved_idx):
        e, s, cand, h = texts[i][0], texts[i][1], texts[i][2], texts[i][3]
        b = origin[i]
        ax, ay = (b[0]+b[2])/2.0, (b[1]+b[3])/2.0
        cx, cy = (cand[0]+cand[2])/2.0, (cand[1]+cand[3])/2.0
        if math.hypot(cx-ax, cy-ay) <= 4.0 * h: continue
        ex = cand[0]-h*0.4 if cx > ax else cand[2]+h*0.4
        ey = cy
        knee = (ex + (ax-ex)*0.45, ey)
        legs = [((ex, ey), knee), (knee, (ax, ay))]
        # never route a leader through another label
        blocked = any(seg_rect(p, q, inflate(tb, h * 0.25))
                      for p, q in legs for j, tb in enumerate(tboxes) if j != i)
        if not blocked:
            # a leader that cuts across the drawing is worse than a label that
            # sits a little off; only draw one that runs through clear space
            blocked = sum(1 for p, q in legs for sg in geo
                          if seg_rect(sg[0], sg[1],
                                      (min(p[0],q[0])-1e-6, min(p[1],q[1])-1e-6,
                                       max(p[0],q[0])+1e-6, max(p[1],q[1])+1e-6))) > 6
        if blocked:
            continue
        for p, q in legs:
            msp.add_line(p, q, dxfattribs={"layer": LEADER_LAYER})
        leaders += 1
    if LEADER_LAYER not in doc.layers:
        doc.layers.add(LEADER_LAYER, color=7)
    doc.saveas(path)
    if verbose:
        print(f"{path.split('/')[-1]:<52} moved {moved:>3} labels, {leaders:>2} leaders added")
    return moved, leaders

if __name__ == "__main__":
    for p in sys.argv[1:]:
        declash(p)
