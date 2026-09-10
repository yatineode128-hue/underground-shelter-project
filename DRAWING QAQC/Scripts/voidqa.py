"""Occupancy / void analysis of an A1 sheet: how much of the drawing area is used."""
import sys, glob, json
import numpy as np
import ezdxf, ezdxf.bbox

FRAME_LAYERS = {"S-TITLE","M-TITLE","P-TITLE","A-TITLE"}

def cells(path, nx=84, ny=59):
    doc=ezdxf.readfile(path); msp=doc.modelspace()
    ext=ezdxf.bbox.extents(msp,fast=False)
    X0,Y0,X1,Y1=ext.extmin.x,ext.extmin.y,ext.extmax.x,ext.extmax.y
    W,H=X1-X0,Y1-Y0
    grid=np.zeros((ny,nx),bool)
    for e in msp:
        try:
            b=ezdxf.bbox.extents([e],fast=True)
            if not b.has_data: continue
        except Exception: continue
        x0,y0,x1,y1=b.extmin.x,b.extmin.y,b.extmax.x,b.extmax.y
        # skip the sheet border / frame rectangles themselves (they span everything)
        if (x1-x0) > 0.9*W and (y1-y0) > 0.9*H: continue
        i0=max(0,int((x0-X0)/W*nx)); i1=min(nx-1,int((x1-X0)/W*nx))
        j0=max(0,int((y0-Y0)/H*ny)); j1=min(ny-1,int((y1-Y0)/H*ny))
        # a long thin panel rect should mark only its outline, not its interior
        if (x1-x0) > 0.25*W and (y1-y0) > 0.25*H and e.dxftype()=="LWPOLYLINE":
            grid[j0:j1+1,i0]=True; grid[j0:j1+1,i1]=True
            grid[j0,i0:i1+1]=True; grid[j1,i0:i1+1]=True
        else:
            grid[j0:j1+1,i0:i1+1]=True
    return grid,(X0,Y0,X1,Y1)

def largest_void(grid, min_side=6):
    """Largest all-empty axis-aligned rectangle (cells)."""
    ny,nx=grid.shape
    heights=np.zeros(nx,int); best=(0,None)
    for j in range(ny):
        for i in range(nx):
            heights[i]=0 if grid[j,i] else heights[i]+1
        stack=[]
        for i in range(nx+1):
            h=heights[i] if i<nx else 0
            start=i
            while stack and stack[-1][1]>=h:
                s,hh=stack.pop()
                a=hh*(i-s)
                if a>best[0] and hh>=min_side and (i-s)>=min_side:
                    best=(a,(s,j-hh+1,i-1,j))
                start=s
            stack.append((start,h))
    return best

def report(path):
    g,(X0,Y0,X1,Y1)=cells(path)
    ny,nx=g.shape
    occ=g.mean()
    a,rect=largest_void(g)
    out=dict(path=path, occupancy=round(float(occ),3), void_cells=int(a),
             void_frac=round(a/(nx*ny),3))
    if rect:
        i0,j0,i1,j1=rect
        out["void_mm"]=(round(X0+i0/nx*(X1-X0)), round(Y0+j0/ny*(Y1-Y0)),
                        round(X0+(i1+1)/nx*(X1-X0)), round(Y0+(j1+1)/ny*(Y1-Y0)))
    return out

if __name__=="__main__":
    files=[f for f in sorted(glob.glob("**/*.dxf",recursive=True)) if not f.startswith(".git")]
    rs=[]
    for f in files:
        try: rs.append(report(f))
        except Exception as e: print("ERR",f,repr(e))
    rs.sort(key=lambda r:-r["void_frac"])
    print(f"{'file':<60} {'occ':>6} {'void%':>7}  largest empty rect (paper mm)")
    for r in rs:
        print(f"{r['path'][-58:]:<60} {r['occupancy']:>6.2f} {r['void_frac']*100:>6.1f}%  {r.get('void_mm')}")
    json.dump(rs,open(sys.argv[1],"w"))
