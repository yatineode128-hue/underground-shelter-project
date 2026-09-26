"""
sw_crest.py -- prepares the CME crest used on the front pages and covers.

The crest is not drawn: it is cut from the syndicate's own photographs of an
earlier CME project report (Images/CME_crest_photo_*.png, crest only).  This
script only cleans the background of those crops:

    CME_crest_colour.png  the colour crest, paper background made transparent
                          (certificate and approval sheet)
    CME_crest_gold.png    the gold crest reduced to one gold tone on a
                          transparent background (black hard covers)

    python3 "Project Report/Final Submission/Scripts/sw_crest.py"
"""

import os

from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.abspath(os.path.join(HERE, "..", "Images"))
GOLD = (212, 175, 55)


def colour():
    im = Image.open(os.path.join(IMG, "CME_crest_photo_colour.png"))
    im = im.convert("RGB").resize((im.width * 3, im.height * 3),
                                  Image.LANCZOS)
    w, h = im.size
    # flood the grey paper from every edge point with a white key colour
    key = (255, 0, 255)
    for x in range(0, w, 6):
        for y in (0, h - 1):
            if im.getpixel((x, y)) != key:
                ImageDraw.floodfill(im, (x, y), key, thresh=60)
    for y in range(0, h, 6):
        for x in (0, w - 1):
            if im.getpixel((x, y)) != key:
                ImageDraw.floodfill(im, (x, y), key, thresh=60)
    px = im.load()
    out = Image.new("RGBA", (w, h))
    po = out.load()
    for y in range(h):
        for x in range(w):
            p = px[x, y]
            po[x, y] = (0, 0, 0, 0) if p == key else p + (255,)
    alpha = out.getchannel("A").filter(ImageFilter.MinFilter(3))
    out.putalpha(alpha.filter(ImageFilter.GaussianBlur(1)))
    out = out.crop(out.getbbox())
    out.save(os.path.join(IMG, "CME_crest_colour.png"))
    return out.size


def gold():
    im = Image.open(os.path.join(IMG, "CME_crest_photo_gold.png"))
    im = im.convert("RGB").resize((im.width * 2, im.height * 2),
                                  Image.LANCZOS)
    im = im.filter(ImageFilter.MedianFilter(5))
    w, h = im.size
    px = im.load()
    mask = Image.new("L", (w, h), 0)
    pm = mask.load()
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            pm[x, y] = 255 if (r > 110 and g > 90 and r - b > 55) else 0
    mask = mask.filter(ImageFilter.MedianFilter(5))
    mask = mask.filter(ImageFilter.GaussianBlur(0.8))
    out = Image.new("RGBA", (w, h), GOLD + (0,))
    out.putalpha(mask)
    out = out.crop(mask.point(lambda v: 255 if v > 60 else 0).getbbox())
    out.save(os.path.join(IMG, "CME_crest_gold.png"))
    return out.size


if __name__ == "__main__":
    print("colour", colour())
    print("gold", gold())
