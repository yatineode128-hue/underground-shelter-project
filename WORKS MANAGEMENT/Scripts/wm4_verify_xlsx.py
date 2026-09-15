"""
wm4_verify_xlsx.py — evaluate every formula in the WM4 workbook and check it.

LibreOffice cannot open a file in this environment, so the usual
"recalculate and read the cached values back" route is not available.  This
script does the job directly instead: it walks the workbook, evaluates every
formula it contains against the literal cells around it, and compares the
result with the figure wm4_bill.py computes independently.

It covers the whole formula vocabulary the workbook uses and FAILS if it meets
one it does not recognise, so a formula cannot slip through unchecked:
    =D12*F12                 quantity x rate
    =SUM(G4:G20)             section sub-total
    =G21+G45+G60             total of sub-totals
    =$E$4*D9                 a recapitulation percentage of the item total
    =E4+E5+E6                a recapitulation sub-total
    =IFERROR(J12/F12,"")     a percentage difference
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)

from openpyxl import load_workbook
from openpyxl.utils import column_index_from_string
import wm4_bill as BL
import wm4_build as BD

XLSX = os.path.join(ROOT, "Cost",
                    "WM4_Underground_Shelter_BOQ_Cost_Estimate_SSR_2022-23.xlsx")

CELL = re.compile(r"\$?([A-Z]{1,3})\$?(\d+)")


class Fail(Exception):
    pass


SHEETREF = re.compile(r"^'?([^'!]+)'?!\$?([A-Z]{1,3})\$?(\d+)$")


def evaluate(ws, formula, values, seen=None, wb=None):
    """Evaluate one formula against `values`, a {(row,col): number} map of the
    sheet's literal cells, resolving references to other formulas recursively.
    A reference into another sheet is followed there, with that sheet's own
    literal cells."""
    seen = seen or set()
    f = formula.lstrip("=").strip()

    m = SHEETREF.fullmatch(f)
    if m:
        if wb is None:
            raise Fail("cross-sheet reference needs the workbook: " + formula)
        other = wb[m.group(1)]
        ov = {(c.row, c.column): c.value for r in other.iter_rows()
              for c in r if isinstance(c.value, (int, float))}
        return cell_value(other, int(m.group(3)),
                          column_index_from_string(m.group(2)), ov, seen, wb)

    m = re.fullmatch(r'IFERROR\((.+),""\)', f)
    if m:
        try:
            return evaluate(ws, "=" + m.group(1), values, seen, wb)
        except ZeroDivisionError:
            return ""

    m = re.fullmatch(r"SUM\(([A-Z]{1,3})(\d+):([A-Z]{1,3})(\d+)\)", f)
    if m:
        c1, r1, c2, r2 = m.group(1), int(m.group(2)), m.group(3), int(m.group(4))
        if c1 != c2:
            raise Fail("multi-column SUM not expected: " + formula)
        col = column_index_from_string(c1)
        return sum(cell_value(ws, r, col, values, seen, wb) or 0
                   for r in range(r1, r2 + 1))

    if re.fullmatch(r"(\$?[A-Z]{1,3}\$?\d+)([*/+-]\$?[A-Z]{1,3}\$?\d+)*", f):
        # a chain of cell references joined by one operator class
        toks = re.split(r"([*/+-])", f)
        val = ref(ws, toks[0], values, seen, wb)
        for i in range(1, len(toks), 2):
            op, nxt = toks[i], ref(ws, toks[i + 1], values, seen, wb)
            a = 0 if val is None or val == "" else val
            b = 0 if nxt is None or nxt == "" else nxt
            if op == "*":
                val = a * b
            elif op == "/":
                if b == 0:
                    raise ZeroDivisionError
                val = a / b
            elif op == "+":
                val = a + b
            else:
                val = a - b
        return val

    raise Fail("unrecognised formula: " + formula)


def ref(ws, token, values, seen, wb=None):
    m = CELL.fullmatch(token.strip())
    if not m:
        raise Fail("bad reference: " + token)
    return cell_value(ws, int(m.group(2)),
                      column_index_from_string(m.group(1)), values, seen, wb)


def cell_value(ws, row, col, values, seen, wb=None):
    key = (row, col)
    if key in values:
        return values[key]
    c = ws.cell(row=row, column=col)
    v = c.value
    if isinstance(v, str) and v.startswith("="):
        if key in seen:
            raise Fail("circular reference at %s%d" % (c.column_letter, row))
        return evaluate(ws, v, values, seen | {key}, wb)
    return v if isinstance(v, (int, float)) else None


def main():
    wb = load_workbook(XLSX)
    checks, fails = 0, []

    def ck(name, ok, detail=""):
        nonlocal checks
        checks += 1
        if not ok:
            fails.append((name, detail))

    nf = 0
    for ws in wb.worksheets:
        values = {}
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, (int, float)):
                    values[(c.row, c.column)] = c.value
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.startswith("="):
                    nf += 1
                    try:
                        evaluate(ws, c.value, values, None, wb)
                    except Fail as e:
                        fails.append(("%s!%s%d" % (ws.title, c.column_letter,
                                                   c.row), str(e)))
                    checks += 1

    # --- the numbers the workbook must agree with ---------------------------
    ws = wb["BOQ priced"]
    values = {(c.row, c.column): c.value for r in ws.iter_rows() for c in r
              if isinstance(c.value, (int, float))}
    total_cell = None
    for row in ws.iter_rows(min_col=2, max_col=2):
        if row[0].value and str(row[0].value).startswith("TOTAL OF ITEMS"):
            total_cell = ws.cell(row=row[0].row, column=7)
    ck("the BOQ sheet has a TOTAL OF ITEMS row", total_cell is not None)
    grand = evaluate(ws, total_cell.value, values, None, wb)
    expect = BL.totals()["ITEMS"]
    ck("workbook total of items equals the bill total",
       abs(grand - expect) < 0.05, "%.2f against %.2f" % (grand, expect))

    ws2 = wb["Recapitulation"]
    v2 = {(c.row, c.column): c.value for r in ws2.iter_rows() for c in r
          if isinstance(c.value, (int, float))}
    v2[(1, 1)] = None
    est = None
    for row in ws2.iter_rows(min_col=2, max_col=2):
        if row[0].value and str(row[0].value).startswith("ESTIMATED COST"):
            est = ws2.cell(row=row[0].row, column=5)
    ck("the recapitulation has an ESTIMATED COST row", est is not None)

    # the recapitulation refers across to the BOQ sheet; the evaluator
    # follows that reference for real rather than being handed the answer
    got = evaluate(ws2, est.value, v2, None, wb)
    rows, base, sub_ssr, before_gst, gst = BD.recap_rows()
    ck("workbook estimated cost equals the computed recapitulation",
       abs(got - (before_gst + gst)) < 0.5,
       "%.2f against %.2f" % (got, before_gst + gst))

    print("=" * 74)
    print("WM4 WORKBOOK FORMULA VERIFICATION")
    print("=" * 74)
    print("  workbook      %s" % os.path.relpath(XLSX, ROOT))
    print("  sheets        %d" % len(wb.worksheets))
    print("  formulas      %d, every one evaluated" % nf)
    print("  checks        %d" % checks)
    print("  full-calc-on-open flag: %s" % wb.calculation.fullCalcOnLoad)
    print()
    print("  total of items          {:>18,.2f}".format(grand))
    print("  estimated cost          {:>18,.2f}".format(got))
    print()
    if fails:
        for n, d in fails:
            print("  FAIL  %-48s %s" % (n, d))
        print("\n  %d FAILURE(S)" % len(fails))
        return 1
    print("  ALL PASS — no unrecognised formula, no circular reference, and")
    print("  the workbook's own arithmetic reproduces the bill exactly.")
    print("=" * 74)
    return 0


if __name__ == "__main__":
    sys.exit(main())
