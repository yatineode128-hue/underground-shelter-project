"""
report_crest.py -- prepares the two crest images the front matter uses.

Underground CBRN-hardened blast-resistant protective structure + sentry post, Pune.
Project Report package, revision PR3.

    python3 "Project Report/Scripts/report_crest.py"

SOURCE.  `Assets/crest_source_photo.png` is a 380 x 405 px crop of the College
of Military Engineering crest, taken from the owner's own photograph of a CME
project report's hard cover (supplied 26 Sep 2026).  No official artwork file
of the crest is held in this project [NOT AVAILABLE].

WHAT THIS DOES.  It traces the photograph's line-work once -- a gold shield with
black line-work -- at 5x, and writes two images from that one trace:

    Assets/crest_gold.png     gold shield, line-work and surround transparent;
                              for the black hard cover, where the board shows
                              through the lines exactly as on the book
    Assets/crest_colour.png   navy over maroon field, gold gateway;  for the
                              certificate and approval sheet

The colour version is a RECONSTRUCTION.  The colour crest in the owner's
photographs is too small (about 205 px) to trace, so it is used only as the
reference for the field colours and the navy/maroon split: the towers keep the
gold masonry of the trace, and everything else is drawn as gold line-work on
the field, as it is on the printed colour crest.

**Replace both images with the official artwork when it is available** -- the
renderer reads only the two PNG files and needs nothing from this script.

Dependencies: numpy, scipy and Pillow.  They are needed ONLY to re-run this
preparation step;  report_render.py does not import this module.
"""

import os

import numpy as np
from PIL import Image
from scipy import ndimage as ndi

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.abspath(os.path.join(HERE, "..", "Assets"))
SRC = os.path.join(ASSETS, "crest_source_photo.png")
OUT_GOLD = os.path.join(ASSETS, "crest_gold.png")
OUT_COLOUR = os.path.join(ASSETS, "crest_colour.png")

UP = 5                  # trace resolution, times the photograph
OUT_W = 900             # published width, px  (about 500 dpi at 45 mm)

GOLD = (222, 178, 58)
NAVY = (31, 29, 64)
MAROON = (120, 27, 34)
LINE = (24, 20, 30)
SPLIT = 0.49            # navy/maroon boundary, fraction of the shield height,
                        # read off the colour crest in the owner's photograph


def trace():
    """The photograph -> (shield mask, line-work mask) at UP x resolution."""
    a = np.asarray(Image.open(SRC).convert("RGB")).astype(float)
    # gold is high in red and green and low in blue;  the board is none of them
    score = (a[..., 0] + a[..., 1]) / 2.0 - a[..., 2]
    score = ndi.zoom(score, UP, order=3)
    shield = ndi.binary_fill_holes(ndi.gaussian_filter(score, 2 * UP) > 70)
    inner = ndi.binary_erosion(shield, iterations=3 * UP)
    # the thin lines are blurred in the photograph, so a line is judged against
    # its neighbourhood, and anything plainly dark is a line regardless
    sm = ndi.gaussian_filter(score, 0.45 * UP)
    loc = ndi.gaussian_filter(score, 4 * UP)
    dark = ((sm < loc - 10) & (sm < 120)) | (sm < 55)
    dark = ndi.binary_opening(dark, iterations=1)
    dark = ndi.gaussian_filter(dark.astype(float), 0.5 * UP) > 0.5
    dark &= inner
    # keep the drawing, drop the photograph's specks: a component survives if
    # it is not tiny and it touches the gateway's own bounding box
    lab, n = ndi.label(dark)
    idx = np.arange(1, n + 1)
    sizes = ndi.sum(np.ones_like(lab), lab, idx)
    biggest = 1 + int(np.argmax(sizes))
    ys, xs = np.nonzero(lab == biggest)
    pad = 4 * UP
    y0, y1, x0, x1 = ys.min() - pad, ys.max() + pad, xs.min() - pad, xs.max() + pad
    keep = np.zeros(n + 1, bool)
    for k, sl in zip(idx, ndi.find_objects(lab)):
        cy = (sl[0].start + sl[0].stop) / 2.0
        cx = (sl[1].start + sl[1].stop) / 2.0
        if sizes[k - 1] > (2.2 * UP) ** 2 and y0 <= cy <= y1 and x0 <= cx <= x1:
            keep[k] = True
    lines = keep[lab]
    return shield, lines


def towers(shield, lines):
    """The two tower bodies: the gateway silhouette, in the columns where it
    rises above the parapet, from the parapet's top down."""
    sil = ndi.binary_fill_holes(lines)
    h, w = sil.shape
    top = np.where(sil.any(axis=0), sil.argmax(axis=0), h)
    parapet_top = int(np.median(top[int(w * 0.45):int(w * 0.55)]))
    cols = top < parapet_top - 6 * UP
    region = np.zeros_like(sil)
    region[parapet_top - 2 * UP:, :] = True
    return sil & region & cols[None, :]


def publish(rgba, path):
    img = Image.fromarray(rgba, "RGBA")
    ys, xs = np.nonzero(rgba[..., 3])
    img = img.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
    img = img.resize((OUT_W, round(img.height * OUT_W / img.width)),
                     Image.LANCZOS)
    img.save(path, optimize=True)
    return img.size


def main():
    shield, lines = trace()
    h, w = shield.shape

    gold = np.zeros((h, w, 4), np.uint8)
    gold[shield & ~lines] = GOLD + (255,)

    ys = np.nonzero(shield.any(axis=1))[0]
    split = int(ys.min() + SPLIT * (ys.max() - ys.min()))
    field = np.zeros((h, w, 3), np.uint8)
    field[:split] = NAVY
    field[split:] = MAROON
    tw = towers(shield, lines)
    colour = np.zeros((h, w, 4), np.uint8)
    colour[..., :3] = field
    colour[..., 3] = np.where(shield, 255, 0)
    colour[shield & lines & ~tw, :3] = GOLD          # line-work on the field
    colour[shield & tw & ~lines, :3] = GOLD          # the towers' masonry
    colour[shield & tw & lines, :3] = LINE

    print("crest_gold.png    %d x %d" % publish(gold, OUT_GOLD))
    print("crest_colour.png  %d x %d" % publish(colour, OUT_COLOUR))


if __name__ == "__main__":
    main()
