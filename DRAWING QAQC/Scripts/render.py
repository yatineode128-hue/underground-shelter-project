import sys, os, glob, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import ezdxf
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from ezdxf.addons.drawing.config import Configuration, LineweightPolicy, ColorPolicy

def render(path, out, dpi=150, wide=16.0):
    doc = ezdxf.readfile(path)
    msp = doc.modelspace()
    ext = ezdxf.bbox.extents(msp, fast=False)
    x0,y0,x1,y1 = ext.extmin.x, ext.extmin.y, ext.extmax.x, ext.extmax.y
    w,h = x1-x0, y1-y0
    fig = plt.figure(figsize=(wide, wide*h/w), dpi=dpi)
    ax = fig.add_axes([0,0,1,1]); ax.set_axis_off()
    ctx = RenderContext(doc)
    cfg = Configuration(lineweight_policy=LineweightPolicy.RELATIVE_FIXED,
                        color_policy=ColorPolicy.BLACK,
                        background_policy=None if False else None)
    be = MatplotlibBackend(ax)
    Frontend(ctx, be, config=cfg).draw_layout(msp, finalize=False)
    m = 0.01*max(w,h)
    ax.set_xlim(x0-m, x1+m); ax.set_ylim(y0-m, y1+m)
    ax.set_aspect("equal")
    fig.savefig(out, dpi=dpi, facecolor="white")
    plt.close(fig)
    return (round(x0,1),round(y0,1),round(x1,1),round(y1,1))

if __name__ == "__main__":
    import json
    src, out = sys.argv[1], sys.argv[2]
    dpi = int(sys.argv[3]) if len(sys.argv)>3 else 150
    print(render(src, out, dpi))
