"""
audit_inputs.py  --  PHASE A input audit helper.

Parses every project input file that the Structural CAD reinforcement package
depends on and prints a factual inventory.  READ-ONLY: this script never writes
to any project file.

Run:  python3 "Structural CAD/Scripts/audit_inputs.py"
"""
import os, re, sys, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CAD  = os.path.join(ROOT, "current", "cad")
STD  = os.path.join(ROOT, "current", "staad")


# ----------------------------------------------------------------- DXF reader
def dxf_groups(path):
    """Yield (code, value) pairs from an ASCII DXF."""
    with open(path, "r", errors="replace") as f:
        lines = f.read().splitlines()
    for i in range(0, len(lines) - 1, 2):
        try:
            yield int(lines[i].strip()), lines[i + 1].strip()
        except ValueError:
            continue


def dxf_report(path):
    ents = collections.Counter()
    layers_tbl, layers_used = set(), collections.Counter()
    xs, ys = [], []
    section = None
    cur_ent = None
    in_tables = False
    tbl_kind = None
    pend_layer_name = None
    for code, val in dxf_groups(path):
        if code == 0:
            if val == "SECTION":
                section = "?"
            elif val == "ENDSEC":
                section = None
                in_tables = False
            elif val == "TABLE":
                in_tables = True
                tbl_kind = None
            elif val == "LAYER" and in_tables:
                tbl_kind = "LAYER"
                pend_layer_name = None
            elif val == "ENDTAB":
                tbl_kind = None
            elif section == "ENTITIES":
                cur_ent = val
                ents[val] += 1
            else:
                cur_ent = None
        elif code == 2 and section == "?":
            section = val
        elif code == 2 and tbl_kind == "LAYER":
            layers_tbl.add(val)
        elif code == 8 and section == "ENTITIES":
            layers_used[val] += 1
        elif section == "ENTITIES" and code in (10, 11, 12, 13):
            try:
                xs.append(float(val))
            except ValueError:
                pass
        elif section == "ENTITIES" and code in (20, 21, 22, 23):
            try:
                ys.append(float(val))
            except ValueError:
                pass
    return dict(entities=ents, layers_tbl=sorted(layers_tbl),
                layers_used=layers_used,
                extents=(min(xs) if xs else None, min(ys) if ys else None,
                         max(xs) if xs else None, max(ys) if ys else None))


def dxf_text(path):
    """Return all TEXT string values (code 1) in the file."""
    out = []
    for code, val in dxf_groups(path):
        if code == 1:
            out.append(val)
    return out


# --------------------------------------------------------------- STAAD reader
def std_report(path):
    txt = open(path, "r", errors="replace").read()
    lines = txt.splitlines()
    r = {}
    r["lines"] = len(lines)
    r["joints"] = len(re.findall(r"^\s*\d+\s+-?[\d.]+\s+-?[\d.]+\s+-?[\d.]+\s*;?",
                                 txt, re.M))
    r["elements"] = None
    m = re.search(r"ELEMENT INCIDENCES SHELL(.*?)(?=^[A-Z*])", txt, re.S | re.M)
    if m:
        r["elements"] = len(re.findall(r"\b(\d+)\s+\d+\s+\d+\s+\d+\s+\d+", m.group(1)))
    r["loads"] = re.findall(r"^LOAD\s+(\d+).*?TITLE\s+(.*)$", txt, re.M)
    r["combs"] = re.findall(r"^LOAD COMB\s+(\d+)\s+(.*)$", txt, re.M)
    r["props"] = re.findall(r"^\s*(.*?)\s+THICKNESS\s+([\d.]+)", txt, re.M)
    r["mats"] = re.findall(r"^ISOTROPIC\s+(\S+)", txt, re.M)
    r["E"] = re.findall(r"^E\s+([\d.e+E]+)", txt, re.M)
    r["supports"] = [l.strip() for l in lines
                     if "ELASTIC MAT" in l or "FIXED" in l or "PINNED" in l]
    r["perform"] = [l.strip() for l in lines if l.startswith("PERFORM")]
    r["design"] = [l.strip() for l in lines
                   if "CONCRETE DESIGN" in l or l.startswith("DESIGN ELEMENT")]
    return r


def main():
    print("=" * 78)
    print("PHASE A INPUT AUDIT  --  raw parse of every dependency")
    print("=" * 78)

    print("\n### INPUT DXF SET (current/cad)\n")
    for fn in sorted(os.listdir(CAD)):
        if not fn.lower().endswith(".dxf"):
            continue
        p = os.path.join(CAD, fn)
        rep = dxf_report(p)
        e = rep["extents"]
        print(f"- {fn}")
        print(f"    size {os.path.getsize(p):>8} B   entities "
              f"{dict(rep['entities'])}")
        print(f"    layers declared: {rep['layers_tbl']}")
        print(f"    extents X {e[0]} .. {e[2]}   Y {e[1]} .. {e[3]}")

    print("\n### STAAD MODELS (current/staad)\n")
    for fn in sorted(os.listdir(STD)):
        if not fn.lower().endswith((".std",)):
            continue
        p = os.path.join(STD, fn)
        r = std_report(p)
        print(f"- {fn}   ({r['lines']} lines)")
        print(f"    joints parsed  : {r['joints']}")
        print(f"    shell elements : {r['elements']}")
        print(f"    materials      : {r['mats']}   E = {r['E']}")
        print(f"    thicknesses    : {r['props']}")
        print(f"    supports       : {r['supports'][:6]}")
        print(f"    primary loads  : {len(r['loads'])}")
        for n, t in r["loads"]:
            print(f"        LOAD {n:>3}  {t}")
        print(f"    combinations   : {len(r['combs'])}")
        for n, t in r["combs"]:
            print(f"        COMB {n:>3}  {t}")
        print(f"    analysis       : {r['perform']}")
        print(f"    design block   : {r['design']}")
        print()

    print("### STAAD OUTPUT / RESULT FILES")
    outs = [f for f in os.listdir(STD)
            if f.lower().endswith((".anl", ".out", ".txt", ".rea"))]
    print("    ", outs if outs else "NONE PRESENT — no analysis output exists in the workspace")

    print("\n### REVIT")
    rv = os.path.join(ROOT, "Revit")
    for dirpath, _, files in os.walk(rv):
        for f in sorted(files):
            print("    ", os.path.relpath(os.path.join(dirpath, f), ROOT))
    print("    .rvt files:",
          [f for _, _, fs in os.walk(rv) for f in fs if f.endswith(".rvt")] or
          "NONE — no Revit model file exists in the workspace")


if __name__ == "__main__":
    main()
