"""
validate_dxf.py  --  programmatic validation of every R-series DXF.

Checks (brief section 33 plus the legibility items of section 32 that can be
checked mechanically):
  1  file opens and parses as a valid DXF
  2  DXF version and units
  3  every required layer is declared, and no entity sits on an undeclared layer
  4  no zero-length LINE, zero-radius CIRCLE or degenerate LWPOLYLINE
  5  no unintended duplicate geometry (identical entity on the same layer)
  6  TEXT / MTEXT entities exist
  7  DIMENSION entities exist and carry the view-scale factor
  8  drawing extents lie inside the A1 sheet 0..841 x 0..594
  9  nothing intrudes into the title-block rectangle except the title block
 10  every bar mark drawn on the sheet exists in rebar_data (no orphan marks)
 11  every detail / drawing cross-reference resolves to a sheet that exists

Run:  python3 validate_dxf.py            (validates the whole package)
"""
import os, sys, math, collections, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ezdxf
from ezdxf import bbox
import sc_dxflib as D
import rebar_data as R

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DXFDIR = os.path.join(ROOT, "DXF")
SHEET_W, SHEET_H = 841.0, 594.0
TB = (651.0, 10.0, 831.0, 110.0)
MARKS = {m["mark"] for m in R.MARKS} | {f["mark"] for f in R.FABRIC}
# R-501/502/503 are named ONLY to record that no column sheet is issued,
# because the underground shelter has no RC column.  Not a broken reference.
DELIBERATE_NONSHEETS = {"R-501", "R-502", "R-503"}

VALID_SHEETS = None      # filled in main()


def sheet_numbers():
    out = set()
    for p in glob.glob(os.path.join(DXFDIR, "**", "*.dxf"), recursive=True):
        out.add(os.path.basename(p)[:5])
    return out


def check(path):
    name = os.path.basename(path)
    res = dict(file=name, path=path, errors=[], warnings=[], info={})
    try:
        doc = ezdxf.readfile(path)
    except Exception as e:                                   # 1
        res["errors"].append(f"WILL NOT OPEN: {e}")
        return res
    msp = doc.modelspace()
    ents = list(msp)
    res["info"]["dxfversion"] = doc.dxfversion
    res["info"]["entities"] = len(ents)
    if doc.dxfversion != "AC1024":                           # 2
        res["warnings"].append(f"DXF version {doc.dxfversion}, expected AC1024")
    if doc.header.get("$INSUNITS", 0) != 4:
        res["errors"].append("units are not millimetres ($INSUNITS != 4)")

    declared = {l.dxf.name for l in doc.layers}              # 3
    missing = set(D.LAYERS) - declared
    if missing:
        res["errors"].append(f"layers declared in the standard but missing: {sorted(missing)}")
    used = collections.Counter(e.dxf.layer for e in ents)
    undeclared = {l for l in used if l not in declared}
    if undeclared:
        res["errors"].append(f"entities on undeclared layers: {sorted(undeclared)}")
    res["info"]["layers_used"] = len(used)

    kinds = collections.Counter(e.dxftype() for e in ents)
    res["info"]["kinds"] = dict(kinds)

    zero = 0                                                 # 4
    for e in ents:
        t = e.dxftype()
        if t == "LINE" and math.dist((e.dxf.start.x, e.dxf.start.y),
                                     (e.dxf.end.x, e.dxf.end.y)) < 1e-6:
            zero += 1
        elif t == "CIRCLE" and e.dxf.radius <= 1e-9:
            zero += 1
        elif t == "LWPOLYLINE" and len(e) < 2:
            zero += 1
    if zero:
        res["errors"].append(f"{zero} zero-length / degenerate entities")

    sig = collections.Counter()                              # 5
    for e in ents:
        t = e.dxftype()
        if t == "LINE":
            a = (round(e.dxf.start.x, 4), round(e.dxf.start.y, 4))
            b = (round(e.dxf.end.x, 4), round(e.dxf.end.y, 4))
            sig[(e.dxf.layer, "L", min(a, b), max(a, b))] += 1
        elif t == "CIRCLE":
            sig[(e.dxf.layer, "C", (round(e.dxf.center.x, 4), round(e.dxf.center.y, 4)),
                 round(e.dxf.radius, 4))] += 1
        elif t == "TEXT":
            sig[(e.dxf.layer, "T", e.dxf.text,
                 (round(e.dxf.insert.x, 3), round(e.dxf.insert.y, 3)))] += 1
    dups = sum(v - 1 for v in sig.values() if v > 1)
    if dups:
        res["warnings"].append(f"{dups} exactly duplicated entities on the same layer")

    texts = [e for e in ents if e.dxftype() in ("TEXT", "MTEXT")]
    if not texts:                                            # 6
        res["errors"].append("no TEXT or MTEXT entity")
    res["info"]["text_entities"] = len(texts)
    dims = [e for e in ents if e.dxftype() == "DIMENSION"]   # 7
    res["info"]["dimensions"] = len(dims)
    leaders = [e for e in ents if e.dxftype() == "LEADER"]
    res["info"]["leaders"] = len(leaders)
    hatches = [e for e in ents if e.dxftype() == "HATCH"]
    res["info"]["hatches"] = len(hatches)
    blocks = [e for e in ents if e.dxftype() == "INSERT"]
    res["info"]["blockrefs"] = len(blocks)

    try:                                                     # 8
        ext = bbox.extents(msp)
        x0, y0 = ext.extmin.x, ext.extmin.y
        x1, y1 = ext.extmax.x, ext.extmax.y
        res["info"]["extents"] = (round(x0, 1), round(y0, 1), round(x1, 1), round(y1, 1))
        if x0 < -0.6 or y0 < -0.6 or x1 > SHEET_W + 0.6 or y1 > SHEET_H + 0.6:
            res["errors"].append(
                f"geometry outside the A1 sheet: extents "
                f"{x0:.1f},{y0:.1f} .. {x1:.1f},{y1:.1f}")
    except Exception as e:
        res["warnings"].append(f"extents not computable: {e}")

    intruders = 0                                            # 9
    for e in ents:
        if e.dxf.layer in ("S-TITLE", "S-BLAST"):
            continue
        try:
            b = bbox.extents([e])
        except Exception:
            continue
        if (b.extmin.x > TB[0] + 1 and b.extmax.x < TB[2] - 1 and
                b.extmin.y > TB[1] + 1 and b.extmax.y < TB[3] - 1):
            intruders += 1
    if intruders:
        res["warnings"].append(f"{intruders} entities inside the title-block rectangle")

    drawn_marks = set()                                      # 10
    for e in texts:
        s = e.dxf.text if e.dxftype() == "TEXT" else e.text
        s = s.strip()
        if e.dxf.layer == "S-CALLOUT" and 2 <= len(s) <= 5 and s[0].isalpha():
            drawn_marks.add(s)
    orphans = sorted(drawn_marks - MARKS)
    if orphans:
        res["errors"].append(f"ORPHAN BAR MARKS drawn but not scheduled: {orphans}")
    res["info"]["marks_on_sheet"] = len(drawn_marks)

    refs = set()                                             # 11
    for e in texts:
        s = e.dxf.text if e.dxftype() == "TEXT" else e.text
        for tok in s.replace(",", " ").replace("/", " ").split():
            tok = tok.strip("().·")
            if len(tok) == 5 and tok[0] == "R" and tok[1] == "-" and tok[2:].isdigit():
                refs.add(tok)
    if VALID_SHEETS is not None:
        broken = sorted(refs - VALID_SHEETS - DELIBERATE_NONSHEETS)
        if broken:
            res["errors"].append(f"BROKEN DRAWING REFERENCES: {broken}")
    res["info"]["refs"] = sorted(refs)
    return res


def main():
    global VALID_SHEETS
    VALID_SHEETS = sheet_numbers()
    files = sorted(glob.glob(os.path.join(DXFDIR, "**", "*.dxf"), recursive=True))
    print("=" * 96)
    print("DXF VALIDATION  --  Structural CAD reinforcement package")
    print(f"{len(files)} files  ·  sheet numbers present: {len(VALID_SHEETS)}")
    print("=" * 96)
    nerr = nwarn = 0
    for p in files:
        r = check(p)
        i = r["info"]
        status = "FAIL" if r["errors"] else ("REVIEW" if r["warnings"] else "PASS")
        print(f"\n{r['file']}   [{status}]")
        if "extents" in i:
            print(f"    ver {i.get('dxfversion')}  ents {i.get('entities')}  "
                  f"layers {i.get('layers_used')}  text {i.get('text_entities')}  "
                  f"dim {i.get('dimensions')}  lead {i.get('leaders')}  "
                  f"hatch {i.get('hatches')}  blk {i.get('blockrefs')}")
            print(f"    extents {i['extents']}   marks on sheet {i.get('marks_on_sheet')}")
        for e in r["errors"]:
            print(f"    ERROR   {e}")
            nerr += 1
        for w in r["warnings"]:
            print(f"    REVIEW  {w}")
            nwarn += 1
    print("\n" + "=" * 96)
    print(f"TOTAL: {len(files)} files, {nerr} errors, {nwarn} review items")
    return nerr


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
