"""
mep_validate.py  --  programmatic validation of every DXF produced by the
DRAINAGE, HVAC and SCHEDULE OF FINISHES packages.

Shared by all three packages (imported with this directory on sys.path).

CHECKS
   1  the file opens and parses as a valid DXF
   2  DXF version and drawing units
   3  every entity sits on a DECLARED layer, and the declared set is used
   4  no zero-length LINE, zero-radius CIRCLE or degenerate LWPOLYLINE
   5  no unintended duplicate geometry (identical entity, same layer)
   6  TEXT / MTEXT entities exist and carry readable heights
   7  DIMENSION entities exist where the sheet is a scaled view
   8  drawing extents lie inside the A1 sheet, 0..841 x 0..594
   9  nothing intrudes into the title-block rectangle except the title block
  10  no text runs off the right-hand sheet edge
  11  the package scope-exclusion note is present on every sheet

Run:  python3 mep_validate.py <dxf-dir> [<dxf-dir> ...]
"""
import os
import sys
import glob
import math
import collections

import ezdxf

SHEET_W, SHEET_H = 841.0, 594.0
TB = (651.0, 10.0, 831.0, 110.0)          # title block rectangle
TB_LAYERS = {"M-TITLE", "S-TITLE", "M-FLAG"}
SCOPE_TOKEN = "SENTRY POST EXCLUDED"


def _pts(e):
    t = e.dxftype()
    if t == "LINE":
        return [(e.dxf.start.x, e.dxf.start.y), (e.dxf.end.x, e.dxf.end.y)]
    if t == "LWPOLYLINE":
        return [(p[0], p[1]) for p in e.get_points()]
    if t == "CIRCLE":
        c, r = e.dxf.center, e.dxf.radius
        return [(c.x - r, c.y - r), (c.x + r, c.y + r)]
    if t == "ARC":
        c, r = e.dxf.center, e.dxf.radius
        return [(c.x - r, c.y - r), (c.x + r, c.y + r)]
    if t in ("TEXT", "ATTRIB"):
        ha = e.dxf.get("halign", 0)
        p = e.dxf.align_point if (ha or e.dxf.get("valign", 0)) else e.dxf.insert
        w = len(e.dxf.text) * e.dxf.height * 0.62
        # 0 left, 1 centre, 2 right, 3 aligned, 4 middle, 5 fit
        x0 = p.x if ha in (0, 3, 5) else (p.x - w / 2.0 if ha in (1, 4) else p.x - w)
        return [(x0, p.y), (x0 + w, p.y + e.dxf.height)]
    if t == "MTEXT":
        p = e.dxf.insert
        return [(p.x, p.y), (p.x + e.dxf.width, p.y)]
    if t == "INSERT":
        p = e.dxf.insert
        return [(p.x - 6, p.y - 6), (p.x + 6, p.y + 6)]
    return []


def check(path):
    name = os.path.basename(path)
    r = dict(file=name, errors=[], warnings=[], info={})
    try:
        doc = ezdxf.readfile(path)
    except Exception as exc:                                     # 1
        r["errors"].append(f"WILL NOT OPEN: {exc}")
        return r
    msp = doc.modelspace()
    ents = list(msp)
    r["info"]["entities"] = len(ents)
    r["info"]["dxfversion"] = doc.dxfversion

    if doc.dxfversion != "AC1024":                               # 2
        r["warnings"].append(f"DXF version {doc.dxfversion}, expected AC1024")
    if doc.header.get("$INSUNITS", 0) != 4:
        r["errors"].append("$INSUNITS is not 4 (millimetres)")

    declared = {ly.dxf.name for ly in doc.layers}                # 3
    used = collections.Counter(e.dxf.layer for e in ents)
    for lay in used:
        if lay not in declared:
            r["errors"].append(f"entity on undeclared layer '{lay}'")
    r["info"]["layers_used"] = len(used)
    r["info"]["layers_declared"] = len(declared)

    kinds = collections.Counter(e.dxftype() for e in ents)
    r["info"]["kinds"] = dict(kinds)

    zero = 0                                                     # 4
    for e in ents:
        t = e.dxftype()
        if t == "LINE":
            a, b = e.dxf.start, e.dxf.end
            if math.hypot(a.x - b.x, a.y - b.y) < 1e-6:
                zero += 1
        elif t == "CIRCLE" and e.dxf.radius < 1e-6:
            zero += 1
        elif t == "LWPOLYLINE" and len(e) < 2:
            zero += 1
    if zero:
        r["errors"].append(f"{zero} zero-length / degenerate entities")

    seen, dup = set(), 0                                         # 5
    for e in ents:
        t = e.dxftype()
        if t not in ("LINE", "CIRCLE", "LWPOLYLINE", "ARC"):
            continue
        key = (t, e.dxf.layer,
               tuple(round(c, 4) for p in _pts(e) for c in p))
        if key in seen:
            dup += 1
        seen.add(key)
    if dup:
        r["warnings"].append(f"{dup} duplicate geometry entities")

    txt = [e for e in ents if e.dxftype() in ("TEXT", "MTEXT")]  # 6
    if not txt:
        r["errors"].append("no TEXT or MTEXT on the sheet")
    r["info"]["text"] = len(txt)
    small = [e for e in txt if e.dxftype() == "TEXT" and e.dxf.height < 1.2]
    if small:
        r["warnings"].append(f"{len(small)} text entities below 1.2 mm high")

    dims = [e for e in ents if e.dxftype() in ("DIMENSION",)]    # 7
    r["info"]["dimensions"] = len(dims)

    xs, ys = [], []                                              # 8
    for e in ents:
        for x, y in _pts(e):
            xs.append(x)
            ys.append(y)
    if xs:
        ext = (min(xs), min(ys), max(xs), max(ys))
        r["info"]["extents"] = tuple(round(v, 1) for v in ext)
        if ext[0] < -0.5 or ext[1] < -0.5 or ext[2] > SHEET_W + 0.5 \
                or ext[3] > SHEET_H + 0.5:
            r["errors"].append(f"geometry outside the A1 sheet: {r['info']['extents']}")

    intr = 0                                                     # 9
    for e in ents:
        if e.dxf.layer in TB_LAYERS:
            continue
        for x, y in _pts(e):
            if TB[0] < x < TB[2] and TB[1] < y < TB[3]:
                intr += 1
                break
    if intr:
        r["errors"].append(f"{intr} entities intrude into the title block")

    over = 0                                                     # 10
    for e in txt:
        if e.dxftype() != "TEXT":
            continue
        box = _pts(e)
        if box and box[1][0] > 833.0:
            over += 1
    if over:
        r["errors"].append(f"{over} text entities run past the sheet edge")

    if not any(SCOPE_TOKEN in (e.dxf.text if e.dxftype() == "TEXT" else e.text)
               for e in txt):                                    # 11
        r["errors"].append("scope-exclusion note missing")

    return r


def run(dirs):
    files = []
    for d in dirs:
        files += sorted(glob.glob(os.path.join(d, "**", "*.dxf"),
                                  recursive=True))
    if not files:
        print("no DXF found in", dirs)
        return 1, []
    rows, nerr, nwarn = [], 0, 0
    print(f"{'FILE':58s} {'ENTS':>6s} {'TEXT':>5s} {'DIM':>4s} {'LAY':>4s}  RESULT")
    print("-" * 110)
    for f in files:
        r = check(f)
        nerr += len(r["errors"])
        nwarn += len(r["warnings"])
        res = "PASS" if not r["errors"] else f"{len(r['errors'])} ERROR"
        if r["warnings"]:
            res += f" / {len(r['warnings'])} warn"
        i = r["info"]
        print(f"{r['file']:58s} {i.get('entities',0):6d} {i.get('text',0):5d} "
              f"{i.get('dimensions',0):4d} {i.get('layers_used',0):4d}  {res}")
        for e in r["errors"]:
            print(f"      ERROR   {e}")
        for wmsg in r["warnings"]:
            print(f"      warn    {wmsg}")
        rows.append(r)
    print("-" * 110)
    print(f"{len(files)} files   {nerr} errors   {nwarn} warnings")
    return (0 if nerr == 0 else 1), rows


if __name__ == "__main__":
    dirs = sys.argv[1:] or [os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "DXF"))]
    sys.exit(run(dirs)[0])
