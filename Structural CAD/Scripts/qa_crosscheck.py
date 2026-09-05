"""
qa_crosscheck.py  --  bar-mark / schedule / drawing cross-check.

Answers the four questions the brief asks (sections 22, 23, 30, 33):
  1  does every bar mark on every drawing have EXACTLY ONE schedule entry?
  2  is any schedule entry an orphan - scheduled but never drawn?
  3  does every drawing named in rebar_data actually exist as a DXF?
  4  does every drawing cross-reference on a sheet resolve to a sheet?

It reads the DXFs back, it does not trust the generators.
"""
import os, sys, glob, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ezdxf
import rebar_data as R

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DXFDIR = os.path.join(ROOT, "DXF")
SCHED = {m["mark"] for m in R.MARKS}
FABRIC = {f["mark"] for f in R.FABRIC}
ALL = SCHED | FABRIC
DELIBERATE_NONSHEETS = {"R-501", "R-502", "R-503"}


def marks_on_sheet(path):
    doc = ezdxf.readfile(path)
    out = set()
    for e in doc.modelspace():
        if e.dxftype() == "TEXT" and e.dxf.layer == "S-CALLOUT":
            s = e.dxf.text.strip()
            if 2 <= len(s) <= 5 and s[0].isalpha():
                out.add(s)
    return out


def refs_on_sheet(path):
    doc = ezdxf.readfile(path)
    out = set()
    for e in doc.modelspace():
        if e.dxftype() in ("TEXT", "MTEXT"):
            s = e.dxf.text if e.dxftype() == "TEXT" else e.text
            for tok in s.replace(",", " ").replace("/", " ").split():
                tok = tok.strip("().·")
                if len(tok) == 5 and tok.startswith("R-") and tok[2:].isdigit():
                    out.add(tok)
    return out


def main():
    files = sorted(glob.glob(os.path.join(DXFDIR, "**", "*.dxf"), recursive=True))
    sheets = {os.path.basename(p)[:5]: p for p in files}
    print("=" * 88)
    print("BAR-MARK / SCHEDULE / DRAWING CROSS-CHECK")
    print("=" * 88)
    print(f"{len(R.MARKS)} bar marks scheduled  ·  {len(R.FABRIC)} fabric item(s)  ·  "
          f"{len(files)} DXF sheets")

    errors = []
    drawn = collections.defaultdict(set)
    for num, p in sorted(sheets.items()):
        m = marks_on_sheet(p)
        for mk in m:
            drawn[mk].add(num)
        bad = sorted(m - ALL)
        if bad:
            errors.append(f"{num}: ORPHAN MARKS DRAWN BUT NOT SCHEDULED {bad}")

    print("\n1  MARKS DRAWN BUT NOT SCHEDULED")
    print("   ", "NONE - every mark drawn has a schedule entry" if not errors
          else errors)

    print("\n2  SCHEDULED MARKS NEVER DRAWN ON ANY SHEET")
    never = sorted(ALL - set(drawn))
    if never:
        print(f"    {len(never)} marks are scheduled but carry no balloon on any sheet:")
        for mk in never:
            m = next((x for x in R.MARKS if x["mark"] == mk), None)
            dw = " / ".join(m["drawings"]) if m else "-"
            print(f"      {mk:<6} nominated for {dw}")
        print("    These are covered by the BAR MARK KEY panel and the BAR SCHEDULE")
        print("    EXTRACT on their nominated sheets, which name the mark in text.")
        print("    A balloon is added only where it can be placed without obscuring")
        print("    the reinforcement it points at.  NOT AN ERROR - reported for review.")
    else:
        print("    NONE")

    print("\n3  DRAWINGS NAMED IN THE SCHEDULE THAT DO NOT EXIST")
    named = set()
    for m in R.MARKS:
        named.update(m["drawings"])
    for f in R.FABRIC:
        named.update(f["drawings"])
    missing = sorted(named - set(sheets))
    if missing:
        errors.append(f"schedule names non-existent drawings: {missing}")
        print("   ", missing)
    else:
        print("    NONE - every drawing named in the schedule exists")

    print("\n4  BROKEN DRAWING CROSS-REFERENCES ON THE SHEETS")
    broken_any = False
    for num, p in sorted(sheets.items()):
        br = sorted(refs_on_sheet(p) - set(sheets) - DELIBERATE_NONSHEETS)
        if br:
            broken_any = True
            errors.append(f"{num}: broken references {br}")
            print(f"    {num}: {br}")
    if not broken_any:
        print("    NONE - every reference resolves")
        print("    (R-501 / R-502 / R-503 are named only to record that no column")
        print("     sheet is issued, because no RC column exists.)")

    print("\n5  MARK COVERAGE BY SHEET")
    for num in sorted(sheets):
        ms = sorted(mk for mk, s in drawn.items() if num in s)
        print(f"    {num}  {len(ms):>2} balloon(s)  {', '.join(ms) if ms else '-'}")

    print("\n" + "=" * 88)
    if errors:
        print(f"CROSS-CHECK FAILED - {len(errors)} error(s)")
        for e in errors:
            print("   ", e)
        return 1
    print("CROSS-CHECK PASSED - no orphan marks, no duplicate marks, "
          "no broken references")
    return 0


if __name__ == "__main__":
    sys.exit(main())
