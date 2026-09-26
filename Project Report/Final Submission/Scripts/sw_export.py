"""
sw_export.py -- exports the report, as sw_render.py sets it, to a JSON layout
file and a folder of figure images, from which sw_docx.js builds the editable
Word document.

    python3 "Project Report/Final Submission/Scripts/sw_export.py" OUTDIR

Everything the PDF decides -- paragraph numbers, sentence-case titles, table
and figure numbers, table column widths and sizes, figure sizes, and the page
labels of the contents lists -- is decided here by the same code, so the two
outputs cannot drift apart.  Nothing is retyped.
"""

import json
import os
import re
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sw_render as R                                          # noqa: E402
import sw_figures as SF                                        # noqa: E402
from sw_case import sentence                                   # noqa: E402

MM = 72.0 / 25.4


# ---------------------------------------------------------------- inline
def runs(text):
    """Source inline markup to a list of runs {t, b, i, sub, sup, br}."""
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    out, st = [], {"b": 0, "i": 0, "sub": 0, "sup": 0, "u": 0}
    for tok in re.split(r"(</?(?:b|i|sub|sup|u)>|<br/?>)", t):
        if not tok:
            continue
        m = re.match(r"<(/?)(b|i|sub|sup|u)>", tok)
        if m:
            st[m.group(2)] += -1 if m.group(1) else 1
            continue
        if re.match(r"<br/?>", tok):
            out.append({"br": True})
            continue
        out.append({"t": tok, "b": st["b"] > 0, "i": st["i"] > 0,
                    "sub": st["sub"] > 0, "sup": st["sup"] > 0,
                    "u": st["u"] > 0})
    return out


def bold(text):
    return [dict(r, b=True) if "t" in r else r for r in runs(text)]


# ---------------------------------------------------------------- images
class Images:
    def __init__(self, outdir):
        self.dir = os.path.join(outdir, "img")
        os.makedirs(self.dir, exist_ok=True)
        self.n = 0

    def drawing(self, d, maxw_pt):
        """A reportlab drawing to PNG at 220 dpi; returns (path, w_mm, h_mm)."""
        from reportlab.graphics import renderPDF
        import pymupdf
        sc = min(1.0, maxw_pt / float(d.width))
        self.n += 1
        pdf = os.path.join(self.dir, "fig%03d.pdf" % self.n)
        png = os.path.join(self.dir, "fig%03d.png" % self.n)
        renderPDF.drawToFile(d, pdf)
        doc = pymupdf.open(pdf)
        doc[0].get_pixmap(dpi=220).save(png)
        doc.close()
        os.remove(pdf)
        return png, d.width * sc / MM, d.height * sc / MM

    def photo(self, name):
        buf, (pw, ph) = SF.photo(name)
        maxh = SF.PHOTO_MAXH.get(name, 86) * R.mm
        sc = min(R.TXT_W / float(pw), maxh / float(ph))
        self.n += 1
        path = os.path.join(self.dir, "photo%03d.jpg" % self.n)
        with open(path, "wb") as f:
            f.write(buf.read())
        return path, pw * sc / MM, ph * sc / MM


# ---------------------------------------------------------------- page labels
def page_entries():
    """Run the PDF build to a scratch file and return its TOC / LOF / LOT
    entries with their page labels."""
    out = R.OUT
    R.OUT = os.path.join(tempfile.mkdtemp(), "labels.pdf")
    try:
        entries = []
        for _ in range(4):
            doc = R.build(entries)
            new = doc.entries
            if new == entries:
                break
            entries = new
    finally:
        R.OUT = out
    return entries


# ---------------------------------------------------------------- walk
def table_item(cap, rows, widths, align, header):
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    if widths:
        tot = float(sum(widths))
        cw = [R.TXT_W * w / tot for w in widths]
    else:
        cw = [R.TXT_W / ncol] * ncol
    if header:
        rows = [[sentence(c) for c in rows[0]]] + rows[1:]
    font, cw = R.fit_table(rows, cw, header)
    align = align or ["L"] * ncol
    groups, cells = [], []
    for ri, r in enumerate(rows):
        if ri and r[0].strip().startswith("==") and \
                not any(x.strip() for x in r[1:]):
            groups.append(ri)
            cells.append([bold(r[0].strip()[2:].strip())])
            continue
        cells.append([runs(c.strip()) for c in r])
    return {"t": "table", "caption": cap, "font": font,
            "widths": [w / MM for w in cw], "align": align,
            "header": header, "groups": groups, "rows": cells}


def export(outdir):
    R.register_fonts()
    blocks = R.parse()
    entries = page_entries()
    img = Images(outdir)
    items = []
    chap = None
    nums = [0, 0, 0]
    tcount = fcount = 0
    last_level = 0
    first_front = True
    in_main = False

    # the first page, read from the flowables sw_render.cover() builds
    cover = []
    for f in R.cover():
        cls = f.__class__.__name__
        if cls == "Paragraph":
            cover.append({"k": "line", "runs": runs(f.text),
                          "size": f.style.fontSize,
                          "bold": "Bold" in f.style.fontName})
        elif cls == "Spacer":
            cover.append({"k": "space", "mm": f.height / MM})
        elif cls == "FigBox":
            path, w, h = img.drawing(f.d, R.TXT_W)
            cover.append({"k": "figure", "path": path, "w": w, "h": h})
        elif cls == "Table":
            cols = list(zip(*f._cellvalues))
            cover.append({"k": "names", "cols": [
                [c.text for c in col if hasattr(c, "text")] for col in cols]})
    items.append({"t": "cover", "parts": cover})

    for b in blocks:
        k = b["k"]
        if k in ("front", "plainfront"):
            title = b["arg"].strip()
            toc = None
            if title not in ("CONTENTS",):
                toc = sentence(R.fix_case(title.title())) \
                    if title.isupper() else title
            items.append({"t": "front", "title": title, "toc": toc,
                          "first": first_front})
            first_front = False
            chap = None
            continue
        if k in ("chapter", "appendix"):
            parts = [x.strip() for x in b["arg"].split("|")]
            if k == "chapter":
                chap = (chap + 1) if isinstance(chap, int) else 1
                label = "CHAPTER %d" % chap
                title, sub = parts[0], (parts[1] if len(parts) > 1 else "")
                toc = "Chapter %d : %s" % (
                    chap, sentence(R.fix_case(title.title())))
            else:
                chap = parts[0]
                label = "APPENDIX %s" % parts[0]
                title, sub = parts[1], (parts[2] if len(parts) > 2 else "")
                toc = "Appendix %s : %s" % (
                    parts[0], sentence(R.fix_case(title.title())))
            items.append({"t": "chapter", "label": label, "title": title,
                          "sub": sub, "toc": toc, "first": not in_main})
            in_main = True
            nums = [0, 0, 0]
            tcount = fcount = 0
            continue
        if k == "head":
            items.append({"t": "head", "runs": runs(sentence(b["arg"]))})
            continue
        if k in ("toc", "lof", "lot"):
            kind = {"toc": ("toc",), "lof": ("lof",), "lot": ("lot",)}[k]
            items.append({"t": k, "entries": [
                {"level": lv, "text": R.inline_plain(tx), "page": pg}
                for kd, lv, tx, pg in entries if kd in kind]})
            continue
        if k == "pagebreak":
            items.append({"t": "pagebreak"})
            continue
        if k == "vspace":
            items.append({"t": "vspace", "mm": float(b["arg"])})
            continue
        if k == "crest":
            from PIL import Image as PImage
            fn = os.path.join(R.PKG, "Images", "CME_crest_colour.png")
            w, h = PImage.open(fn).size
            hh = float(b["arg"] or 30)
            items.append({"t": "image", "path": fn, "w": hh * w / float(h),
                          "h": hh, "align": "C"})
            continue
        if k == "cols":
            cols = [[x.strip() for x in part.split("|")]
                    for part in b["arg"].split("||")]
            items.append({"t": "cols", "cols": [
                [bold(c[0])] + [runs(x) for x in c[1:]] for c in cols]})
            continue
        if k == "right":
            lines = [x.strip() for x in b["arg"].split("|")]
            rule = bool(lines) and lines[0] == "-"
            items.append({"t": "right", "rule": rule,
                          "lines": [runs(x) for x in
                                    (lines[1:] if rule else lines)]})
            continue
        if k == "sigs":
            slots = [[x.strip() for x in part.split("|")]
                     for part in b["arg"].split("||")]
            items.append({"t": "sigs", "slots": slots})
            continue
        if k == "examiners":
            items.append({"t": "examiners"})
            continue
        if k == "cond":
            continue
        if k == "p":
            lev = b["lev"]
            if lev:
                nums[lev - 1] += 1
                for j in range(lev, 3):
                    nums[j] = 0
                number = ".".join([str(chap)] +
                                  [str(n) for n in nums[:lev]])
                last_level = lev
                ind, tab = R.TAB[lev]
                items.append({"t": "para", "level": lev, "num": number,
                              "title": sentence(b["title"]) if b["title"]
                              else "", "runs": runs(b["text"]),
                              "ind": ind / MM, "tab": tab / MM})
            else:
                ind = R.TAB[last_level][0] if last_level else 0
                items.append({"t": "text", "centre": bool(b.get("centre")),
                              "ind": ind / MM, "runs": runs(b["text"])})
            continue
        if k == "table":
            tcount += 1
            num = "%s.%d" % (chap, tcount) if chap else str(tcount)
            rows, capt = b["rows"], b["cap"]
            m = re.match(r"^@(\w+)\s*(.*)$", capt)
            if m:
                rows = R.SPECIAL[m.group(1)]()
                capt = m.group(2)
            if capt.strip() == "-":
                tcount -= 1
                cap = ""
            else:
                cap = "Table %s : %s" % (num, sentence(capt))
            items.append(table_item(cap, rows, b["widths"], b["align"],
                                    not b["nohead"]))
            continue
        if k == "calc":
            ind = R.TAB[max(last_level, 1)][1]
            rows = []
            for ln in b["rows"]:
                bb = ln.startswith("!")
                ln = ln[1:] if bb else ln
                a, c = (ln.split(";;", 1) + [""])[:2]
                rows.append({"a": runs(a.strip()), "b": runs(c.strip()),
                             "bold": bb})
            items.append({"t": "calc", "ind": ind / MM, "rows": rows})
            continue
        if k in ("fig", "photo", "grid"):
            name, cap = [x.strip() for x in b["arg"].split("|", 1)]
            fcount += 1
            num = "%s.%d" % (chap, fcount) if chap else str(fcount)
            capt = "Fig %s : %s" % (num, sentence(cap))
            if k == "grid":
                cols, panels = SF.GRIDS[name]
                from PIL import Image as PImage
                cells = []
                for fn, lab in panels:
                    path = os.path.join(SF.IMG_DIR, "STAAD", fn + ".png")
                    cells.append({"path": path, "label": lab,
                                  "dims": list(PImage.open(path).size)})
                items.append({"t": "grid", "caption": capt, "cols": cols,
                              "cells": cells})
            else:
                if k == "fig":
                    path, w, h = img.drawing(SF.figure(name), R.TXT_W)
                else:
                    path, w, h = img.photo(name)
                items.append({"t": "figure", "caption": capt, "path": path,
                              "w": w, "h": h})
            continue
        raise ValueError("unknown directive %r" % k)

    page = {"text_w": R.TXT_W / MM, "left": R.TXT_L / MM, "right": 25.0,
            "top": 25.0, "bottom": 25.0, "body_pt": R.BODY_SIZE,
            "head_bg": "E6E6E8", "group_bg": "F0F0F1"}
    with open(os.path.join(outdir, "report.json"), "w") as f:
        json.dump({"page": page, "items": items}, f, ensure_ascii=False)
    print("exported", len(items), "items,", img.n, "images, to", outdir)


if __name__ == "__main__":
    export(os.path.abspath(sys.argv[1]))
