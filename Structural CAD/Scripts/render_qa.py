"""render_qa.py  --  visual QA renderer, DXF -> PNG.  QA ONLY, not a deliverable.

    python3 render_qa.py <file.dxf> <out.png> [x0 x1 y0 y1] [dpi]
"""
import sys, matplotlib
matplotlib.use("Agg")
import ezdxf, matplotlib.pyplot as plt
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend

path, out = sys.argv[1], sys.argv[2]
box = [float(v) for v in sys.argv[3:7]] if len(sys.argv) >= 7 else [0, 841, 0, 594]
dpi = int(sys.argv[7]) if len(sys.argv) > 7 else 110
x0, x1, y0, y1 = box
doc = ezdxf.readfile(path)
msp = doc.modelspace()
from ezdxf.addons.drawing.properties import LayoutProperties
ctx = RenderContext(doc)
lp = LayoutProperties.from_layout(msp)
lp.set_colors("#FFFFFF")            # paper white, so ACI 7 plots black
fig = plt.figure(figsize=((x1 - x0) / 25.4 * 1.5, (y1 - y0) / 25.4 * 1.5))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_axis_off()
Frontend(ctx, MatplotlibBackend(ax)).draw_layout(msp, finalize=False, layout_properties=lp)
ax.set_xlim(x0, x1); ax.set_ylim(y0, y1); ax.set_aspect("equal")
fig.savefig(out, dpi=dpi, facecolor="white")
print("rendered", out)
