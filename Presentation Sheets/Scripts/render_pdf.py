"""render_pdf.py -- DXF -> TRUE-SIZE A2 vector PDF, plotted 1:1, black on white.

The sheets are drawn in paper millimetres, so the plot is a straight 1:1: the
PDF page is exactly 594 x 420 mm and every dimension on it measures true.
"""
import sys, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import ezdxf
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from ezdxf.addons.drawing.config import Configuration, LineweightPolicy

MM = 1 / 25.4
W, H = 594.0, 420.0


def to_pdf(path, out):
    doc = ezdxf.readfile(path)
    msp = doc.modelspace()
    fig = plt.figure(figsize=(W * MM, H * MM))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_axis_off()
    ctx = RenderContext(doc)
    ctx.set_current_layout(msp)
    ctx.current_layout_properties.set_colors("#ffffff", "#000000")
    cfg = Configuration(lineweight_policy=LineweightPolicy.RELATIVE_FIXED)
    Frontend(ctx, MatplotlibBackend(ax), config=cfg).draw_entities(msp)
    ax.set_xlim(0, W); ax.set_ylim(0, H); ax.set_aspect("equal")
    fig.savefig(out, format="pdf", facecolor="white")
    plt.close(fig)
    return out


if __name__ == "__main__":
    for p in sys.argv[1:]:
        o = os.path.join(os.environ.get("OUTDIR", "."),
                         os.path.splitext(os.path.basename(p))[0] + ".pdf")
        print(to_pdf(p, o))
