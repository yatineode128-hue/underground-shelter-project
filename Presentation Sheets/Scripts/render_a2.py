"""render_a2.py -- visual QA: DXF -> PNG at true A2 proportions, black on white."""
import sys, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import ezdxf, ezdxf.bbox
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from ezdxf.addons.drawing.config import Configuration, LineweightPolicy


def render(path, out, dpi=200, wide=16.5):
    doc = ezdxf.readfile(path)
    msp = doc.modelspace()
    W, H = 594.0, 420.0
    fig = plt.figure(figsize=(wide, wide * H / W), dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_axis_off()
    cfg = Configuration(lineweight_policy=LineweightPolicy.RELATIVE_FIXED)
    ctx = RenderContext(doc)
    # white paper: ACI 7 must resolve to BLACK, not to the dark-background white.
    # set_current_layout() first, because draw_layout() would reset the colours.
    ctx.set_current_layout(msp)
    ctx.current_layout_properties.set_colors("#ffffff", "#000000")
    Frontend(ctx, MatplotlibBackend(ax), config=cfg).draw_entities(msp)
    ax.set_xlim(0, W); ax.set_ylim(0, H); ax.set_aspect("equal")
    fig.savefig(out, dpi=dpi, facecolor="white")
    plt.close(fig)
    ext = ezdxf.bbox.extents(msp, fast=True)
    return (round(ext.extmin.x, 1), round(ext.extmin.y, 1),
            round(ext.extmax.x, 1), round(ext.extmax.y, 1))


if __name__ == "__main__":
    for p in sys.argv[1:]:
        o = os.path.splitext(os.path.basename(p))[0] + ".png"
        o = os.path.join(os.environ.get("OUTDIR", "."), o)
        print(o, render(p, o))
