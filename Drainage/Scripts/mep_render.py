"""
mep_render.py  --  visual QA renderer.  DXF -> PNG, for checking legibility and
clashes before a sheet is issued.  It is a CHECKING tool, not a deliverable:
the deliverable is the DXF.

Run:  python3 mep_render.py <dxf-dir> <png-dir>

Requires matplotlib.  If matplotlib is not installed, the DXFs are still valid
and mep_validate.py still runs - only the visual check is unavailable.
"""
import os
import sys
import glob
import math

import ezdxf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

ACI = {1: "#d02020", 2: "#c08000", 3: "#108010", 4: "#0090a0", 5: "#2040c0",
       6: "#a020a0", 7: "#101010", 8: "#909090", 30: "#e07000"}


def col(e, doc):
    c = e.dxf.color
    if c == 256 or c == 0:
        try:
            c = doc.layers.get(e.dxf.layer).color
        except Exception:
            c = 7
    return ACI.get(c, "#101010")


def render(path, out, dpi=150):
    doc = ezdxf.readfile(path)
    msp = doc.modelspace()
    fig, ax = plt.subplots(figsize=(841 / 25.4, 594 / 25.4))
    ax.set_xlim(-4, 845)
    ax.set_ylim(-4, 598)
    ax.set_aspect("equal")
    ax.axis("off")
    for e in msp:
        t = e.dxftype()
        c = col(e, doc)
        try:
            lw = max(0.25, doc.layers.get(e.dxf.layer).dxf.lineweight / 100.0 * 2.2)
        except Exception:
            lw = 0.3
        if t == "LINE":
            a, b = e.dxf.start, e.dxf.end
            ax.add_line(Line2D([a.x, b.x], [a.y, b.y], color=c, lw=lw))
        elif t == "LWPOLYLINE":
            pts = [(p[0], p[1]) for p in e.get_points()]
            if e.closed and pts:
                pts = pts + [pts[0]]
            ax.add_line(Line2D([p[0] for p in pts], [p[1] for p in pts],
                               color=c, lw=lw))
        elif t == "CIRCLE":
            ax.add_patch(plt.Circle((e.dxf.center.x, e.dxf.center.y),
                                    e.dxf.radius, fill=False, color=c, lw=lw))
        elif t == "ARC":
            a0, a1 = math.radians(e.dxf.start_angle), math.radians(e.dxf.end_angle)
            if a1 < a0:
                a1 += 2 * math.pi
            ts = [a0 + (a1 - a0) * i / 24.0 for i in range(25)]
            ax.add_line(Line2D(
                [e.dxf.center.x + e.dxf.radius * math.cos(t_) for t_ in ts],
                [e.dxf.center.y + e.dxf.radius * math.sin(t_) for t_ in ts],
                color=c, lw=lw))
        elif t == "TEXT":
            ha = e.dxf.get("halign", 0)
            p = e.dxf.align_point if (ha or e.dxf.get("valign", 0)) else e.dxf.insert
            hal = {0: "left", 1: "center", 2: "right", 4: "center"}.get(ha, "left")
            ax.text(p.x, p.y, e.dxf.text, fontsize=e.dxf.height * 2.05,
                    color=c, ha=hal, va="bottom",
                    rotation=e.dxf.rotation, family="monospace")
        elif t == "MTEXT":
            p = e.dxf.insert
            ax.text(p.x, p.y, e.text.replace("\\P", "\n"),
                    fontsize=e.dxf.char_height * 2.05, color=c,
                    ha="left", va="top", family="monospace")
        elif t == "INSERT":
            blk = doc.blocks.get(e.dxf.name)
            p = e.dxf.insert
            sx = e.dxf.get("xscale", 1.0) or 1.0
            for be in blk:
                bt = be.dxftype()
                if bt == "LINE":
                    a, b = be.dxf.start, be.dxf.end
                    ax.add_line(Line2D([p.x + a.x * sx, p.x + b.x * sx],
                                       [p.y + a.y * sx, p.y + b.y * sx],
                                       color=c, lw=0.4))
                elif bt == "CIRCLE":
                    ax.add_patch(plt.Circle(
                        (p.x + be.dxf.center.x * sx, p.y + be.dxf.center.y * sx),
                        be.dxf.radius * sx, fill=False, color=c, lw=0.4))
                elif bt == "LWPOLYLINE":
                    pts = [(p.x + q[0] * sx, p.y + q[1] * sx)
                           for q in be.get_points()]
                    pts = pts + [pts[0]]
                    ax.add_line(Line2D([q[0] for q in pts], [q[1] for q in pts],
                                       color=c, lw=0.4))
        elif t == "HATCH":
            pass
        elif t == "DIMENSION":
            pass
    fig.savefig(out, dpi=dpi, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return out


if __name__ == "__main__":
    src = sys.argv[1]
    dst = sys.argv[2]
    os.makedirs(dst, exist_ok=True)
    for f in sorted(glob.glob(os.path.join(src, "**", "*.dxf"), recursive=True)):
        o = os.path.join(dst, os.path.basename(f)[:-4] + ".png")
        render(f, o)
        print("  ", os.path.basename(o))
