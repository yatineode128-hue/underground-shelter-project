"""Find drawing geometry that has been drawn ON TOP OF a note panel / title block."""
import sys, glob
import ezdxf, ezdxf.bbox

PANEL_LAYERS = {"S-TITLE","M-TITLE"}
# layers that carry real drawing content (not annotation frames)
SKIP = {"S-TITLE","M-TITLE","S-NOTE","S-TABLE","M-TABLE","S-TEXT","M-TEXT","S-BLAST",
        "M-FLAG","S-CALLOUT","M-CALLOUT","S-DIM","M-DIM","A-FIN-TAG","M-LEVEL","S-LEVEL",
        "A-FIN-FLOOR","A-FIN-WALL","A-FIN-CEIL","P-EQUIP","M-EQUIP","M-DAMPER"}

def ov(a,b):
    ox=min(a[2],b[2])-max(a[0],b[0]); oy=min(a[3],b[3])-max(a[1],b[1])
    return ox*oy if ox>0 and oy>0 else 0.0
def ar(a): return max(0,a[2]-a[0])*max(0,a[3]-a[1])

def analyse(path):
    doc=ezdxf.readfile(path); msp=doc.modelspace()
    ext=ezdxf.bbox.extents(msp,fast=True); SH=ar((ext.extmin.x,ext.extmin.y,ext.extmax.x,ext.extmax.y))
    panels=[]
    for e in msp.query("LWPOLYLINE"):
        if e.dxf.layer not in PANEL_LAYERS: continue
        pts=[(p[0],p[1]) for p in e.get_points()]
        if len(pts)!=4: continue
        xs=sorted(set(round(p[0],3) for p in pts)); ys=sorted(set(round(p[1],3) for p in pts))
        if len(xs)!=2 or len(ys)!=2: continue
        r=(xs[0],ys[0],xs[1],ys[1])
        if 800 < ar(r) < 0.35*SH: panels.append(r)
    hits=[]
    for e in msp:
        ly=e.dxf.layer
        if ly in SKIP or e.dxftype() in ("TEXT","MTEXT","INSERT"): continue
        try:
            b=ezdxf.bbox.extents([e],fast=True)
            if not b.has_data: continue
        except Exception: continue
        eb=(b.extmin.x,b.extmin.y,b.extmax.x,b.extmax.y)
        if ar(eb) > 0.30*SH: continue
        for p in panels:
            o=ov(eb,p)
            if o > 0.55*max(ar(eb),1e-6) and o > 4.0:
                hits.append((e.dxftype(), ly, tuple(round(v,1) for v in eb),
                             tuple(round(v,1) for v in p)))
                break
    return panels, hits

if __name__=="__main__":
    tot=0
    for f in sorted(glob.glob("**/*.dxf",recursive=True)):
        if f.startswith(".git") or f.startswith("current/cad"): continue
        try: panels,hits=analyse(f)
        except Exception as e: print("ERR",f,e); continue
        if hits:
            tot+=len(hits)
            from collections import Counter
            c=Counter((h[1],h[3]) for h in hits)
            print(f"{f.split('/')[-1][:56]:<58} {len(hits):>4} entities inside a panel")
            for (ly,p),n in c.most_common(3): print(f"      {n:>4} x {ly:<18} inside panel {p}")
    print("\nTOTAL geometry-inside-panel entities:", tot)
