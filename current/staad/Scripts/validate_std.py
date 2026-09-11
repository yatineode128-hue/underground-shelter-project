"""
validate_std.py  --  programmatic validation of every STAAD.Pro `.std` input
file in this project.

Every other artefact type here has a validator -- `Structural CAD/Scripts/
validate_dxf.py` for the R-series, `Drainage/Scripts/mep_validate.py` for the
services and finishes sheets, `DRAWING QAQC/Scripts/` for the package as a
whole.  The `.std` files had none, and that is exactly why the defects
revision MS2 corrected (master Part H.26) survived from 3 to 11 September
2026 without being seen: three 80-column LOAD 6 lines that STAAD silently
truncated at its own `INPUT WIDTH 79`, and load case 10 defined after case 11.

This validator reads the file the way STAAD reads it -- truncated at the
declared INPUT WIDTH, with `-` continuation lines joined -- so a defect that
only exists in STAAD's view of the file is visible here too.

IT IS A FILE CHECK, NOT AN ANALYSIS.  It does not run STAAD.Pro, it computes
no result, and passing it says nothing whatever about whether the structure
works.  Master rule: editing and verifying a `.std` is not running an
analysis and must never be reported as one.

CHECKS
   1  the file opens, is ASCII, and terminates with FINISH
   2  every data line fits the declared INPUT WIDTH  (MS2-1)
   3  primary load case numbers are unique and ascending  (MS2-2)
   4  every LOAD COMB references a load case that exists
   5  every ELEMENT and MEMBER incidence resolves to a defined joint
   6  no repeated node, no duplicate element or member, no duplicate joint,
      no zero-length member
   7  every quadrilateral is planar, non-degenerate and correctly ordered
   8  no joint is defined but unused
   9  every element has a THICKNESS and every member a MEMBER PROPERTY, and
      the assignments do not overlap
  10  every joint/element referenced by SUPPORTS, ELEMENT LOAD, DESIGN ELEMENT
      and PRINT ... LIST resolves
  11  element loads are self-equilibrating in X and Z where the model applies
      them to opposing faces  (this is what catches a truncated pressure)

Run:  python3 validate_std.py [<file-or-dir> ...]
      default: the `current/staad/` directory this script lives under
"""
import os
import sys
import glob
import math
import collections
import re

DEFAULT_WIDTH = 79


# ---------------------------------------------------------------- reading

def raw_lines(path, width):
    """Return (logical_line, first_physical_lineno) as STAAD sees them:
    truncated at `width` columns, `-` continuations joined, comments dropped."""
    out, buf, buf_no = [], None, None
    for no, raw in enumerate(open(path, encoding="utf-8", errors="replace"), 1):
        s = raw.rstrip("\n")
        if width:
            s = s[:width]
        s = s.rstrip()
        if s.lstrip().startswith("*"):
            continue
        if buf is not None:
            s = buf + " " + s.strip()
            no, buf = buf_no, None
        if s.endswith("-"):
            buf, buf_no = s[:-1], no
            continue
        if s.strip():
            out.append((s, no))
    return out


def declared_width(path):
    for raw in open(path, encoding="utf-8", errors="replace"):
        m = re.match(r"\s*INPUT\s+WIDTH\s+(\d+)", raw, re.I)
        if m:
            return int(m.group(1))
    return DEFAULT_WIDTH


def parse(path, width):
    joints, elems, members, thick, mprop = {}, {}, {}, {}, set()
    loads = []          # (case_no, physical_line)
    combs = []          # (comb_no, [referenced case numbers], physical_line)
    refs = []           # (what, [ids], kind 'J'|'E', physical_line)
    eloads = []         # (case_no, [ids], axis, value)
    section, case = None, None
    for s, no in raw_lines(path, width):
        u = s.strip().upper()
        if u.startswith("JOINT COORDINATES"):
            section = "J"; continue
        if u.startswith("ELEMENT INCIDENCES"):
            section = "E"; continue
        if u.startswith("MEMBER INCIDENCES"):
            section = "M"; continue
        if u.startswith("ELEMENT PROPERTY"):
            section = "T"; continue
        if u.startswith("MEMBER PROPERTY"):
            section = "P"; continue
        if u.startswith("ELEMENT LOAD"):
            section = "L"; continue
        if u.startswith(("START GROUP", "DEFINE MATERIAL", "CONSTANTS",
                         "SUPPORTS", "UNIT ", "INPUT ", "END ")):
            section = "S" if u.startswith("SUPPORTS") else None

        m = re.match(r"^LOAD\s+(\d+)\s", s.strip(), re.I)
        if m:
            case = int(m.group(1)); loads.append((case, no)); section = None; continue
        m = re.match(r"^LOAD\s+COMB\w*\s+(\d+)", s.strip(), re.I)
        if m:
            combs.append([int(m.group(1)), [], no]); case = None; section = None; continue
        if combs and case is None and re.match(r"^[\d.\s]+$", s.strip()) and section is None:
            t = s.split()
            combs[-1][1].extend(int(float(t[i])) for i in range(0, len(t) - 1, 2))
            continue
        m = re.match(r"^DESIGN ELEMENT\s+(.*)$", s.strip(), re.I)
        if m:
            refs.append(("DESIGN ELEMENT", expand(m.group(1)), "E", no)); continue
        m = re.match(r"^PRINT .*?LIST\s+(.*)$", s.strip(), re.I)
        if m:
            refs.append(("PRINT ... LIST", expand(m.group(1)), "J", no)); continue

        if section == "J":
            for item in s.split(";"):
                p = item.split()
                if len(p) == 4 and _num(p):
                    joints[int(p[0])] = tuple(float(x) for x in p[1:])
        elif section == "E":
            for item in s.split(";"):
                p = item.split()
                if len(p) >= 4 and all(x.lstrip("-").isdigit() for x in p):
                    elems[int(p[0])] = [int(x) for x in p[1:]]
        elif section == "M":
            for item in s.split(";"):
                p = item.split()
                if len(p) == 3 and all(x.isdigit() for x in p):
                    members[int(p[0])] = [int(p[1]), int(p[2])]
        elif section == "P":
            m = re.match(r"^([\d\sTO]+?)\s+(PRIS|TABLE|TAPERED)", s.strip(), re.I)
            if m:
                mprop.update(expand(m.group(1)))
        elif section == "T":
            m = re.match(r"^([\d\sTO]+?)\s+THICKNESS\s+([\d.]+)$", s.strip(), re.I)
            if m:
                for e in expand(m.group(1)):
                    thick.setdefault(e, []).append(float(m.group(2)))
        elif section == "S":
            m = re.match(r"^([\d\sTO]+?)\s+(ELASTIC|FIXED|PINNED|SUPPORT)", s.strip(), re.I)
            if m:
                refs.append(("SUPPORTS", expand(m.group(1)), "J", no))
        if section == "L" and case is not None:
            m = re.match(r"^(.*?)\s+PR\s+G([XYZ])\s+(-?[\d.]+)$", s.strip(), re.I)
            if m and re.fullmatch(r"[\dA-Za-z\s]+", m.group(1)):
                eloads.append((case, expand(m.group(1)), m.group(2).upper(),
                               float(m.group(3))))
    return joints, elems, members, thick, mprop, loads, combs, refs, eloads


def _num(p):
    try:
        [float(x) for x in p]; return True
    except ValueError:
        return False


def expand(text):
    """'1 TO 5 9' -> [1,2,3,4,5,9]."""
    tok, ids, i = text.split(), [], 0
    while i < len(tok):
        if tok[i].upper() == "TO" and ids and i + 1 < len(tok):
            ids.extend(range(ids[-1] + 1, int(tok[i + 1]) + 1)); i += 2
        elif tok[i].lstrip("-").isdigit():
            ids.append(int(tok[i])); i += 1
        else:
            i += 1
    return ids


# ---------------------------------------------------------------- geometry

def _sub(a, b): return (a[0] - b[0], a[1] - b[1], a[2] - b[2])
def _cross(a, b): return (a[1] * b[2] - a[2] * b[1],
                          a[2] * b[0] - a[0] * b[2],
                          a[0] * b[1] - a[1] * b[0])
def _norm(a): return math.sqrt(sum(x * x for x in a))


def area(pts):
    return 0.5 * (_norm(_cross(_sub(pts[1], pts[0]), _sub(pts[2], pts[0])))
                  + _norm(_cross(_sub(pts[2], pts[0]), _sub(pts[3], pts[0]))))


# ---------------------------------------------------------------- checking

def check(path):
    err, warn, info = [], [], {}
    text = open(path, encoding="utf-8", errors="replace").read()
    width = declared_width(path)
    info["input_width"] = width

    # 1  ASCII and terminated
    try:
        text.encode("ascii")
    except UnicodeEncodeError:
        err.append("file is not plain ASCII - STAAD input must be")
    if not re.search(r"^\s*FINISH\s*$", text, re.M | re.I):
        err.append("file does not terminate with FINISH")

    # 2  every DATA line fits the declared INPUT WIDTH          (MS2-1)
    over = [(n, len(l), l) for n, l in enumerate(text.split("\n"), 1)
            if len(l) > width and not l.lstrip().startswith("*")]
    for n, ln, l in over:
        err.append(f"line {n} is {ln} columns against INPUT WIDTH {width} - "
                   f"STAAD will read only '{l[:width][-28:]}'")
    info["over_width"] = len(over)

    (joints, elems, members, thick, mprop,
     loads, combs, refs, eloads) = parse(path, width)
    info["joints"], info["elements"] = len(joints), len(elems)
    info["members"] = len(members)
    if not elems and not members:
        err.append("the file defines neither ELEMENT nor MEMBER INCIDENCES")
    info["cases"], info["combs"] = len(loads), len(combs)

    # 3  load case numbers unique and ascending                 (MS2-2)
    seen, prev = set(), None
    for c, no in loads:
        if c in seen:
            err.append(f"line {no}: load case {c} is defined more than once")
        if prev is not None and c < prev:
            err.append(f"line {no}: load case {c} is defined after case {prev} "
                       f"- primary load case numbers must ascend")
        seen.add(c); prev = c

    # 4  combinations reference cases that exist
    for cno, cases, no in combs:
        for c in cases:
            if c not in seen:
                err.append(f"line {no}: LOAD COMB {cno} references "
                           f"load case {c}, which is not defined")

    # 5-7  element and member topology and geometry
    used = set()
    for mid, inc in sorted(members.items()):
        bad = [j for j in inc if j not in joints]
        if bad:
            err.append(f"member {mid} references undefined joint(s) {bad}")
            continue
        used.update(inc)
        if inc[0] == inc[1]:
            err.append(f"member {mid} starts and ends at joint {inc[0]}")
        elif _norm(_sub(joints[inc[0]], joints[inc[1]])) < 1e-9:
            err.append(f"member {mid} has zero length ({inc[0]}-{inc[1]})")
    dupm = {k: v for k, v in _group(members, frozenset).items() if len(v) > 1}
    for _, ms in list(dupm.items())[:10]:
        err.append(f"members {ms} connect the same two joints")
    for eid, inc in sorted(elems.items()):
        bad = [n for n in inc if n not in joints]
        if bad:
            err.append(f"element {eid} references undefined joint(s) {bad}")
            continue
        used.update(inc)
        if len(set(inc)) != len(inc):
            err.append(f"element {eid} repeats a node: {inc}")
            continue
        if len(inc) == 4:
            p = [joints[n] for n in inc]
            ns = [_cross(_sub(p[(i + 1) % 4], p[i]), _sub(p[(i - 1) % 4], p[i]))
                  for i in range(4)]
            if any(_norm(x) < 1e-9 for x in ns):
                err.append(f"element {eid} has a degenerate (zero-area) corner")
                continue
            u = [tuple(c / _norm(x) for c in x) for x in ns]
            for k in range(1, 4):
                if sum(u[0][t] * u[k][t] for t in range(3)) < 0.999:
                    err.append(f"element {eid} is non-planar or its nodes are "
                               f"not in order: {inc}")
                    break

    dup = {k: v for k, v in _group(joints, lambda c: tuple(round(x, 6) for x in c)).items()
           if len(v) > 1}
    for c, ns in list(dup.items())[:10]:
        err.append(f"joints {ns} share the coordinate {c}")
    dupe = {k: v for k, v in _group(elems, frozenset).items() if len(v) > 1}
    for _, es in list(dupe.items())[:10]:
        err.append(f"elements {es} have identical incidences")

    # 8  unused joints
    orphan = sorted(set(joints) - used)
    if orphan:
        err.append(f"{len(orphan)} joint(s) defined but used by no element: "
                   f"{orphan[:12]}{' ...' if len(orphan) > 12 else ''}")

    # 9  thickness coverage
    missing = sorted(set(elems) - set(thick))
    if missing:
        err.append(f"{len(missing)} element(s) have no THICKNESS: {missing[:12]}")
    nomp = sorted(set(members) - mprop)
    if nomp:
        err.append(f"{len(nomp)} member(s) have no MEMBER PROPERTY: {nomp[:12]}")
    for e, ts in thick.items():
        if len(ts) > 1:
            err.append(f"element {e} is given a THICKNESS {len(ts)} times: {ts}")
        if e not in elems:
            err.append(f"THICKNESS assigned to element {e}, which does not exist")

    # 10  every referenced id resolves
    for what, ids, kind, no in refs:
        pool = joints if kind == "J" else (elems or members)
        bad = [i for i in ids if i not in pool]
        if bad:
            err.append(f"line {no}: {what} references "
                       f"{'joint' if kind == 'J' else 'element'}(s) "
                       f"{bad[:10]} that do not exist")
    for c, ids, ax, v in eloads:
        bad = [i for i in ids if i not in elems]
        if bad:
            err.append(f"load case {c}: ELEMENT LOAD references element(s) "
                       f"{bad[:10]} that do not exist")

    # 11  horizontal element loads must balance                 (MS2-1's symptom)
    A = {e: area([joints[n] for n in inc]) for e, inc in elems.items()
         if all(n in joints for n in inc) and len(inc) == 4}
    per = collections.defaultdict(lambda: collections.defaultdict(float))
    for c, ids, ax, v in eloads:
        if ax == "Y":
            continue
        per[c][ax] += v * sum(A.get(i, 0.0) for i in ids)
    for c in sorted(per):
        for ax, tot in sorted(per[c].items()):
            scale = sum(abs(v) * sum(A.get(i, 0.0) for i in ids)
                        for cc, ids, a2, v in eloads if cc == c and a2 == ax)
            if scale and abs(tot) > max(1.0, 1e-4 * scale):
                err.append(f"load case {c}: G{ax} element loads do not balance - "
                           f"net {tot:+.1f} kN on {scale:.0f} kN applied. "
                           f"A self-equilibrating case that does not balance is "
                           f"usually a truncated or mistyped pressure")
    return dict(file=os.path.relpath(path), errors=err, warnings=warn, info=info)


def _group(d, key):
    g = collections.defaultdict(list)
    for k, v in d.items():
        g[key(v)].append(k)
    return g


def run(targets):
    files = []
    for t in targets:
        if os.path.isdir(t):
            files += sorted(glob.glob(os.path.join(t, "*.std")) +
                            glob.glob(os.path.join(t, "*.STD")))
        else:
            files.append(t)
    print("STAAD .std INPUT-FILE VALIDATION  -  file check only, NOT an analysis")
    print("=" * 100)
    print(f"{'file':52s} {'joints':>7s} {'elems':>6s} {'mbrs':>5s} "
          f"{'cases':>6s} {'comb':>5s}  result")
    print("-" * 100)
    nerr = 0
    for f in files:
        r = check(f)
        nerr += len(r["errors"])
        i = r["info"]
        res = "PASS" if not r["errors"] else f"{len(r['errors'])} ERROR"
        print(f"{os.path.basename(r['file']):52s} {i.get('joints',0):7d} "
              f"{i.get('elements',0):6d} {i.get('members',0):5d} "
              f"{i.get('cases',0):6d} {i.get('combs',0):5d}  {res}")
        for e in r["errors"]:
            print(f"      ERROR   {e}")
        for w in r["warnings"]:
            print(f"      warn    {w}")
    print("-" * 100)
    print(f"{len(files)} files   {nerr} errors")
    print()
    print("A PASS means the INPUT FILE is well formed and self-consistent.")
    print("It does NOT mean the structure has been analysed, and it says")
    print("nothing about whether the structure works.  STAAD.Pro has not been")
    print("run in this environment - see master Parts H.4, H.5 and H.26.")
    return 0 if nerr == 0 else 1


if __name__ == "__main__":
    sys.exit(run(sys.argv[1:] or
                 [os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))]))
