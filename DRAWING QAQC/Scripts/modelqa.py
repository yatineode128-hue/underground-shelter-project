"""Clash QA for model-space drawings: text over geometry, text over text."""
import sys, glob, json, math
import ezdxf, ezdxf.bbox

def seg_rect(p1, p2, r):
    """Does segment p1-p2 intersect axis-aligned rect r=(x0,y0,x1,y1)?"""
    x0,y0,x1,y1 = r
    ax,ay=p1; bx,by=p2
    if max(ax,bx)<x0 or min(ax,bx)>x1 or max(ay,by)<y0 or min(ay,by)>y1: return False
    if x0<=ax<=x1 and y0<=ay<=y1: return True
    if x0<=bx<=x1 and y0<=by<=y1: return True
    dx,dy=bx-ax,by-ay
    t0,t1=0.0,1.0
    for p,q in ((-dx,ax-x0),(dx,x1-ax),(-dy,ay-y0),(dy,y1-ay)):
        if abs(p)<1e-12:
            if q<0: return False
        else:
            t=q/p
            if p<0:
                if t>t1: return False
                t0=max(t0,t)
            else:
                if t<t0: return False
                t1=min(t1,t)
    return t0<=t1

def segments(e):
    t=e.dxftype()
    try:
        if t=="LINE": return [((e.dxf.start.x,e.dxf.start.y),(e.dxf.end.x,e.dxf.end.y))]
        if t=="LWPOLYLINE":
            pts=[(p[0],p[1]) for p in e.get_points()]
            segs=list(zip(pts[:-1],pts[1:]))
            if e.closed and len(pts)>2: segs.append((pts[-1],pts[0]))
            return segs
        if t=="POLYLINE":
            pts=[(v.dxf.location.x,v.dxf.location.y) for v in e.vertices]
            segs=list(zip(pts[:-1],pts[1:]))
            if e.is_closed and len(pts)>2: segs.append((pts[-1],pts[0]))
            return segs
        if t in ("ARC","CIRCLE"):
            c=e.dxf.center; r=e.dxf.radius
            if t=="CIRCLE": a0,a1=0.0,360.0
            else: a0,a1=e.dxf.start_angle,e.dxf.end_angle
            if a1<a0: a1+=360
            n=max(8,int((a1-a0)/15))
            pts=[(c.x+r*math.cos(math.radians(a0+(a1-a0)*i/n)),
                  c.y+r*math.sin(math.radians(a0+(a1-a0)*i/n))) for i in range(n+1)]
            return list(zip(pts[:-1],pts[1:]))
    except Exception: pass
    return []

def bb(e):
    try:
        b=ezdxf.bbox.extents([e],fast=False)
        return (b.extmin.x,b.extmin.y,b.extmax.x,b.extmax.y) if b.has_data else None
    except Exception: return None

def ov(a,b):
    ox=min(a[2],b[2])-max(a[0],b[0]); oy=min(a[3],b[3])-max(a[1],b[1])
    return ox*oy if ox>0 and oy>0 else 0.0
def ar(a): return max(0,a[2]-a[0])*max(0,a[3]-a[1])

def analyse(path, shrink=0.12):
    doc=ezdxf.readfile(path); msp=doc.modelspace()
    texts=[]; geo=[]
    for e in msp:
        t=e.dxftype()
        if t in ("TEXT","MTEXT"):
            s=(e.dxf.text if t=="TEXT" else e.plain_text()).strip()
            b=bb(e)
            if s and b: texts.append((s,b,e))
        else:
            for sg in segments(e): geo.append((sg,e.dxf.layer))
    clash=[]; over=[]
    for s,b,e in texts:
        # shrink the text box slightly so a line just grazing the edge is not a clash
        w,h=b[2]-b[0],b[3]-b[1]
        r=(b[0]+w*shrink,b[1]+h*shrink,b[2]-w*shrink,b[3]-h*shrink)
        hits=[ly for sg,ly in geo if seg_rect(sg[0],sg[1],r)]
        if hits: clash.append((s[:44], tuple(round(v) for v in b), len(hits), sorted(set(hits))[:3]))
    ts=sorted(texts,key=lambda t:t[1][0])
    for i in range(len(ts)):
        for j in range(i+1,len(ts)):
            if ts[j][1][0]>ts[i][1][2]: break
            o=ov(ts[i][1],ts[j][1])
            if o>0.12*min(ar(ts[i][1]),ar(ts[j][1])):
                over.append((ts[i][0][:34],ts[j][0][:34],round(o/min(ar(ts[i][1]),ar(ts[j][1])),2)))
    return dict(path=path, n_text=len(texts), text_over_geometry=clash, text_over_text=over)

if __name__=="__main__":
    for f in sys.argv[1:]:
        r=analyse(f)
        print(f"\n=== {f}   texts={r['n_text']}  overGeom={len(r['text_over_geometry'])}  overText={len(r['text_over_text'])}")
        for c in r["text_over_geometry"]: print("   GEO ", c)
        for c in r["text_over_text"]: print("   TXT ", c)
