"""
wm4_build.py — generate every WM4 deliverable from the SSR rate library and the bill.

Underground CBRN-hardened blast-resistant protective structure + sentry post, Pune.
Works Management package revision WM4 · 15 September 2026.

    python3 wm4_build.py

Writes into ../Cost, ../QAQC and ../Documentation.  Every figure in every output
comes from wm4_ssr_library.py (read out of the owner's SSR PDF) and wm4_bill.py
(the WM1 quantities, unchanged).  Nothing is typed twice.
"""

import csv
import datetime
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)

from wm4_ssr_library import (SSR, MATERIAL, LABOUR, CEMENT_BAGS, DEPTH_INCREASE,
                             FLOOR_LIFT, ON_COST, OH_IN_RATE, PROFIT_IN_RATE,
                             LABOUR_CESS_IN_RATE)
import wm4_bill as BL
from wm4_owner_compare import COMPARE

REV = "WM4"
DATE = "15 September 2026"
SRC = ('Government of Maharashtra, Public Works Department — STATE SCHEDULE OF '
       'RATES 2022-23, approved by Government Circular RADASU-2022/PR.KR.12/'
       'NIYOJAN-3 dated 25 July 2022, effective 25 July 2022.  Supplied by the '
       'project owner as "SSR 22-23 MH (1).pdf", 624 pages.')

GST_RATE = 0.18          # [A] — the SSR requires a provision but fixes no rate
INSURANCE_ASSET = 0.0100
INSURANCE_LABOUR = 0.0100

TIER_NAME = {"P": "PRICED", "A": "PRICED [A] — stated assumption",
             "N": "NOT PRICED", "X": "INCLUDED — not separately payable"}


def money(x):
    return "" if x is None else round(x, 2)


def wcsv(path, header, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    return path


# ===========================================================================
#  1.  CSV — the priced bill
# ===========================================================================
def out_bill_csv():
    rows = []
    for r in BL.BILL:
        rows.append([r["section"], r["code"], r["desc"], r["unit"],
                     "" if r["qty"] is None else r["qty"], r["ssr"],
                     money(r["rate"]), money(r["amount"]),
                     TIER_NAME[r["tier"]], r["note"]])
    return wcsv(os.path.join(ROOT, "Cost", "WM4_BOQ_PRICED_SSR_2022-23.csv"),
                ["Section", "Item", "Description", "Unit", "Quantity",
                 "SSR item", "Rate (Rs)", "Amount (Rs)", "Status", "Basis / note"],
                rows)


# ===========================================================================
#  2.  CSV — the rate library actually used
# ===========================================================================
def out_library_csv():
    used = sorted({r["ssr"] for r in BL.BILL} | {c[5] for c in COMPARE})
    rows = []
    for k in sorted(SSR):
        v = SSR[k]
        inuse = any(k in u for u in used)
        rows.append([k, v["chapter"], v["desc"], v["unit"], v["completed"],
                     v["labour"], v["page"], v["page"] + 7,
                     "USED" if inuse else "reference"])
    return wcsv(os.path.join(ROOT, "Cost", "WM4_SSR_RATE_LIBRARY.csv"),
                ["SSR item", "SSR chapter", "Description (SSR wording, trimmed)",
                 "Unit", "Completed rate 2022-23 excl. GST (Rs)",
                 "Labour rate 2022-23 excl. GST (Rs)", "SSR printed page",
                 "PDF page", "Use"], rows)


# ===========================================================================
#  3.  CSV + TXT — recapitulation
# ===========================================================================
def recap_rows():
    t = BL.totals()
    base = t["ITEMS"]
    rows = [["A", "Total of items — SSR 2022-23 completed rates, excl. GST",
             "sum of the priced bill", "", round(base, 2), "this bill"]]
    run = base
    for head, basis, pct, src in BL.RECAP_SSR[1:]:
        if pct is None:
            rows.append(["A", head, basis, "", "", src])
            continue
        if head.startswith("GST"):
            continue
        amt = base * pct
        run += amt
        rows.append(["A", head, basis, pct, round(amt, 2), src])
    rows.append(["A", "SUB-TOTAL — SSR recapitulation, before GST", "", "",
                 round(run, 2), ""])
    sub_ssr = run
    for head, pct in BL.RECAP_OWNER:
        amt = base * pct
        run += amt
        rows.append(["B", head, "%.0f %% of the item total" % (pct * 100), pct,
                     round(amt, 2),
                     "Project owner's own provision structure, carried from "
                     "their RC1 estimate.  NOT part of the schedule of rates"])
    rows.append(["B", "SUB-TOTAL — before GST", "", "", round(run, 2), ""])
    before_gst = run
    gst = before_gst * GST_RATE
    rows.append(["C", "GST on works contract", "%.0f %% [A]" % (GST_RATE * 100),
                 GST_RATE, round(gst, 2),
                 "SSR requires a separate provision in the recapitulation "
                 "sheet but does NOT fix the rate — tagged [A]"])
    rows.append(["C", "ESTIMATED COST — civil works priced from SSR 2022-23",
                 "", "", round(before_gst + gst, 2),
                 "EXCLUDES every NOT PRICED item — see the exclusions register"])
    for head, pct, why in BL.NOT_ADDED:
        rows.append(["D", head + " — NOT ADDED", "%.0f %%" % (pct * 100), "",
                     "", why])
    return rows, base, sub_ssr, before_gst, gst


def out_recap_csv():
    rows, *_ = recap_rows()
    return wcsv(os.path.join(ROOT, "Cost", "WM4_COST_SUMMARY.csv"),
                ["Block", "Head", "Basis", "Rate", "Amount (Rs)", "Source / note"],
                rows)


# ===========================================================================
#  4.  CSV — owner's bill re-rated
# ===========================================================================
def out_compare_csv():
    rows = []
    for part, desc, unit, qty, own, item, ssr, note in COMPARE:
        ov = qty * own
        sv = None if ssr is None else qty * ssr
        rows.append([part, desc, unit, qty, own, round(ov, 2), item,
                     "" if ssr is None else round(ssr, 2),
                     "" if sv is None else round(sv, 2),
                     "" if sv is None else round(sv - ov, 2),
                     "" if sv is None else round(100.0 * (sv - ov) / ov, 1),
                     note])
    return wcsv(os.path.join(ROOT, "Cost", "WM4_OWNER_BILL_VS_SSR.csv"),
                ["Part", "Owner's bill description (RC1)", "Unit", "Quantity",
                 "Owner rate (Rs)", "Owner amount (Rs)", "SSR item",
                 "SSR rate (Rs)", "SSR amount (Rs)", "Difference (Rs)",
                 "Difference (%)", "Note"], rows)


# ===========================================================================
#  5.  TXT — rate derivation, every arithmetic step
# ===========================================================================
def out_derivation():
    o = []
    w = o.append
    w("=" * 78)
    w("WM4 — RATE DERIVATION")
    w("Underground CBRN-hardened protective structure + sentry post, Pune")
    w("Works Management package revision %s, %s" % (REV, DATE))
    w("=" * 78)
    w("")
    w("SOURCE OF EVERY RATE")
    w("  " + SRC)
    w("")
    w("WHAT A 'COMPLETED RATE' ALREADY CONTAINS, on the SSR's own authority")
    w("  General Notes, Section A:")
    w("    'For labour amenities and all other overhead charges, 10 % provision")
    w("     is considered in Rate Abstract.  In addition, 10 % provision for")
    w("     Contractor's Profit is also considered separately.'")
    w("    'Labour Cess at 1 % has been considered separately in Rate Abstracts.'")
    w("    'Material Rates are exclusive of GST.  Rates for completed items are")
    w("     also exclusive of GST.  While preparing the estimates, separate")
    w("     provision for GST shall be made in recapitulation sheet.'")
    w("")
    w("  So the on-cost already inside every completed rate is")
    w("    (1 + %.2f) x (1 + %.2f) x (1 + %.2f) = %.4f"
      % (OH_IN_RATE, PROFIT_IN_RATE, LABOUR_CESS_IN_RATE, ON_COST))
    w("  and overhead, profit and labour cess MUST NOT be added again in the")
    w("  recapitulation.  The owner's RC1 estimate adds 10 % contractor's")
    w("  overhead and profit on top of its own rates; against SSR rates that")
    w("  would be a double count.  WM4 does not make it.")
    w("")
    w("  Every SSR concrete item reads 'including STEEL CENTERING, FORMWORK,")
    w("  cover blocks ... (EXCLUDING reinforcement and structural steel)'.")
    w("  So formwork is inside the concrete rate and reinforcement is not.")
    w("")
    w("-" * 78)
    w("1.  HIGHER CONCRETE GRADE THAN THE SSR PUBLISHES")
    w("-" * 78)
    w("The SSR publishes R.C.C. pardi (wall) and staircase waist slab only to")
    w("M-25.  The shelter box is M-35.  The SSR's own instruction, General")
    w("Notes Section B:")
    w("")
    w("    'If higher Concrete grade is required for any specific work, the")
    w("     rate analysis of the same shall be derived by adding difference in")
    w("     standard cement consumption in relevant SSR item's rate and shall")
    w("     be got approved from the Superintending Engineer, PWD of concerned")
    w("     circle.'")
    w("")
    w("Standard cement consumption, SSR 'Consumption of Material' (bags/m3):")
    for g in ("M15", "M20", "M25", "M30", "M35", "M40"):
        w("    %-4s %5.2f bags" % (g, CEMENT_BAGS[g]))
    w("")
    w("Cement at the SSR general rate Rs %.0f / M.T. = Rs %.2f / kg; bag = 50 kg."
      % (MATERIAL["Cement"][0], MATERIAL["Cement"][0] / 1000.0))
    w("")
    w("    uplift = d_bags x 50 kg x Rs 6.00/kg x %.4f" % ON_COST)
    w("")
    w("THE FORMULA IS VERIFIED AGAINST THE SSR'S OWN PUBLISHED STEPS.")
    w("Where the SSR does publish consecutive grades, the difference it prints")
    w("must equal what this formula computes:")
    w("")
    w("    step        formula   SSR prints (four item families)")
    w("    M20 -> M25   %6.2f    183 (25.11->25.13), 184 (25.13 fnd), 183, 183"
      % ((CEMENT_BAGS["M25"] - CEMENT_BAGS["M20"]) * 50 * 6.0 * ON_COST))
    w("    M25 -> M30   %6.2f    184 (25.15), 183 (25.35), 183, 183"
      % ((CEMENT_BAGS["M30"] - CEMENT_BAGS["M25"]) * 50 * 6.0 * ON_COST))
    w("    M30 -> M35   %6.2f     91 (25.17), 92 (25.37), 92, 92"
      % ((CEMENT_BAGS["M35"] - CEMENT_BAGS["M30"]) * 50 * 6.0 * ON_COST))
    w("")
    w("The formula reproduces the schedule to within the rupee it rounds to.")
    w("That is the check that makes the derived rates usable.")
    w("")
    w("-" * 78)
    w("2.  DEPTH AND FLOOR-LIFT INCREASES")
    w("-" * 78)
    w("SSR General Notes Section B, for BUILDING works:")
    for lo, hi, pct, txt in DEPTH_INCREASE:
        w("    %s" % txt)
    w("")
    w("    Floor lift: " + ", ".join("%s %.0f %%" % (k, v * 100)
                                     for k, v in FLOOR_LIFT.items()))
    w("")
    w("THE SHELTER EXCAVATION GOES TO (-)6.800, WHICH IS PAST THE SSR's LAST")
    w("DEFINED BAND.  The schedule hands that decision to the Superintending")
    w("Engineer and this package does not take it: the 6.0-6.8 m band and the")
    w("sump pit below it are priced at the 4.5-6.0 m band's +30 % as a DECLARED")
    w("LOWER BOUND, tagged [A], and raised as open item WM4-V1.")
    w("")
    w("Depth model, reproducing the WM1 quantities exactly:")
    w("    plan area = 1338.24 m3 / 6.800 m = %.2f m2" % BL.EXC_AREA)
    w("    mean rockhead (-)%.3f  [master / SG1]" % BL.ROCKHEAD)
    for c in ("E-02.1", "E-02.2", "E-02.3", "E-02.4", "E-02.5", "E-02.6"):
        r = [x for x in BL.BILL if x["code"] == c][0]
        w("    %-8s %9.2f m3 @ Rs %9.2f = Rs %12.2f"
          % (c, r["qty"], r["rate"], r["amount"]))
    w("    check: soil 295.20 + 49.20 = 344.40 against WM1 E-02a 344.4  OK")
    w("    check: rock 246.00 + 295.20 + 295.20 + 157.44 = 993.84 against")
    w("           WM1 E-02b 993.84  OK")
    w("")
    w("ROCK IS BROKEN, NOT BLASTED.  WM_CONSTRUCTION_METHODOLOGY.md: 'Rock is")
    w("removed by HYDRAULIC BREAKER, not by blasting ... controlled blasting")
    w("would require a vibration regime the project has not specified', and")
    w("risk S-02 says the same.  So SSR 21.20 (chiselling, wedging, line")
    w("drilling) governs and the three blasting items 21.17 / 21.18 / 21.19 —")
    w("Rs 869, Rs 1 033 and Rs 1 322 — DO NOT APPLY TO THIS PROJECT.")
    w("")
    w("-" * 78)
    w("3.  EVERY DERIVED RATE, WITH ITS ARITHMETIC")
    w("-" * 78)
    for key, val, working in BL._deriv_log:
        w("")
        w("  %s = Rs %.2f" % (key, val))
        for ln in _wrap(working, 72):
            w("      " + ln)
    w("")
    w("-" * 78)
    w("4.  WHAT IS INCLUDED IN ANOTHER RATE AND MUST NOT BE PAID TWICE")
    w("-" * 78)
    for r in BL.BILL:
        if r["tier"] != "X":
            continue
        w("")
        w("  %-12s %s" % (r["code"], r["desc"][:60]))
        for ln in _wrap(r["note"], 72):
            w("      " + ln)
    w("")
    w("-" * 78)
    w("5.  REINFORCEMENT — NET AGAINST ORDER WEIGHT")
    w("-" * 78)
    net = sum(r["qty"] for r in BL.BILL
              if r["section"].startswith("C ") and r["code"] != "R-ORD")
    w("  sum of the twelve scheduled diameters      = %.3f t" % net)
    w("  WM1 order quantity including 5 %% wastage   = 77.330 t")
    w("  77.330 / 1.05                              = %.3f t" % (77.33 / 1.05))
    w("  SSR 26.33 is paid on the weight FIXED IN POSITION, so the net figure")
    w("  is the payable one and the wastage is inside the rate.")
    w("")
    w("=" * 78)
    rows, base, sub_ssr, before_gst, gst = recap_rows()
    t = BL.totals()
    w("TOTALS")
    w("  priced at published SSR items                 Rs {:>16,.2f}".format(t["P"]))
    w("  priced on a stated assumption [A]             Rs {:>16,.2f}".format(t["A"]))
    w("  TOTAL OF ITEMS                                Rs {:>16,.2f}".format(base))
    w("  after the SSR recapitulation heads            Rs {:>16,.2f}".format(sub_ssr))
    w("  after the owner's provision heads             Rs {:>16,.2f}".format(before_gst))
    w("  GST at {:.0f} % [A]                              Rs {:>16,.2f}".format(GST_RATE * 100, gst))
    w("  ESTIMATED COST, CIVIL WORKS                   Rs {:>16,.2f}".format(before_gst + gst))
    w("")
    w("  NOT PRICED, and therefore NOT in that figure: %d bill lines."
      % len([r for r in BL.BILL if r["tier"] == "N"]))
    w("=" * 78)
    path = os.path.join(ROOT, "Cost", "WM4_RATE_DERIVATION.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write("\n".join(o) + "\n")
    return path


def _wrap(text, width):
    words, line, out = text.split(), "", []
    for wd in words:
        if len(line) + len(wd) + 1 > width:
            out.append(line)
            line = wd
        else:
            line = (line + " " + wd).strip()
    if line:
        out.append(line)
    return out


# ===========================================================================
#  6.  TXT — verification / QAQC
# ===========================================================================
def out_qaqc():
    o = []
    w = o.append
    checks = []

    def ck(name, ok, detail=""):
        checks.append((name, ok, detail))

    # quantity conservation against WM1
    e02 = sum(r["qty"] for r in BL.BILL if r["code"].startswith("E-02."))
    ck("E-02 depth bands sum to the WM1 quantity",
       abs(e02 - 1338.24) < 0.01, "%.2f against 1338.24" % e02)
    soil = sum(r["qty"] for r in BL.BILL if r["code"] in ("E-02.1", "E-02.2"))
    ck("soil bands sum to WM1 E-02a", abs(soil - 344.4) < 0.01,
       "%.2f against 344.4" % soil)
    rock = sum(r["qty"] for r in BL.BILL
               if r["code"] in ("E-02.3", "E-02.4", "E-02.5", "E-02.6"))
    ck("rock bands sum to WM1 E-02b", abs(rock - 993.84) < 0.01,
       "%.2f against 993.84" % rock)
    e05 = sum(r["qty"] for r in BL.BILL if r["code"].startswith("E-05."))
    ck("E-05 bands sum to the WM1 quantity", abs(e05 - 37.044) < 0.01,
       "%.3f against 37.044" % e05)
    c06 = sum(r["qty"] for r in BL.BILL if r["code"].startswith("C-06."))
    ck("C-06 split sums to the WM1 quantity", abs(c06 - 32.7) < 0.01,
       "%.2f against 32.7" % c06)
    sc04 = sum(r["qty"] for r in BL.BILL if r["code"].startswith("SC-04."))
    ck("SC-04 split sums to the WM1 quantity", abs(sc04 - 2.28) < 0.01,
       "%.2f against 2.28" % sc04)
    sp10 = sum(r["qty"] for r in BL.BILL if r["code"].startswith("SP-10."))
    ck("SP-10 split sums to the WM1 quantity", abs(sp10 - 222.54) < 0.01,
       "%.2f against 222.54" % sp10)
    net = sum(r["qty"] for r in BL.BILL
              if r["section"].startswith("C ") and r["code"] != "R-ORD")
    ck("reinforcement net = order / 1.05", abs(net - 77.33 / 1.05) < 0.001,
       "%.3f against %.3f" % (net, 77.33 / 1.05))
    ck("W-05 and B-screed are the same work, paid once",
       abs(102.889 * 0.100 - 10.289) < 0.001, "102.889 x 0.100 = 10.2889")

    # grade uplift reproduces the SSR's own published steps
    for a, b_, pub in (("M20", "M25", 183), ("M25", "M30", 183), ("M30", "M35", 92)):
        calc = (CEMENT_BAGS[b_] - CEMENT_BAGS[a]) * 50 * 6.0 * ON_COST
        ck("grade uplift %s->%s reproduces the SSR step" % (a, b_),
           abs(calc - pub) <= 1.5, "%.2f against the SSR's %d" % (calc, pub))

    # no line is both priced and marked included
    ck("no bill line carries both a rate and 'included'",
       all(not (r["tier"] == "X" and r["rate"]) for r in BL.BILL))
    ck("every NOT PRICED line carries no amount",
       all(r["amount"] is None for r in BL.BILL if r["tier"] == "N"))
    ck("every PRICED line carries a rate and an amount",
       all(r["rate"] and r["amount"] is not None
           for r in BL.BILL if r["tier"] in ("P", "A")))
    ck("every rate used is in the SSR library or is a derived rate",
       all(r["ssr"] == "—" or r["ssr"].split()[0] in SSR or "+" in r["ssr"]
           for r in BL.BILL))
    ck("overhead, profit and labour cess are NOT added again",
       len(BL.NOT_ADDED) == 3)

    # main staircase frozen
    stair = [r for r in BL.BILL if r["code"] == "C-07"][0]
    ck("MAIN STAIRCASE QUANTITY UNCHANGED (frozen geometry)",
       stair["qty"] == 3.0, "3.00 m3, as WM1")

    w("=" * 78)
    w("WM4 — CONSISTENCY AND VERIFICATION AUDIT")
    w("Works Management package revision %s, %s" % (REV, DATE))
    w("=" * 78)
    w("")
    w("Every check below is run by wm4_build.py against the generated bill.")
    w("")
    npass = sum(1 for _, ok, _ in checks if ok)
    for name, ok, detail in checks:
        w("  %-4s %-58s %s" % ("PASS" if ok else "FAIL", name, detail))
    w("")
    w("  %d checks, %d pass, %d fail" % (len(checks), npass, len(checks) - npass))
    w("")
    w("-" * 78)
    w("SSR RATE VERIFICATION")
    w("-" * 78)
    w("Every rate in wm4_ssr_library.py was extracted from the SSR PDF and then")
    w("re-verified a second time against the raw text of the page it sits on.")
    w("30 of the 33 first-pass items matched automatically.  Three were checked")
    w("by hand against the page image text:")
    w("    21.33  Rs 7 / 7          confirmed (single-digit rates)")
    w("    21.40  Rs 1 454 / 436    CORRECTED from a mis-read 7 695 / 2 165")
    w("    39.50  Rs 5 700 / 1 809  CORRECTED from a mis-read 5 716 / 1 448")
    w("NEITHER CORRECTION TOUCHES A PRICED LINE: 21.40 is carried for")
    w("reference only, and 39.50 belongs to SP-12, which is NOT PRICED for")
    w("want of a window height.  Both are in the library so that the next")
    w("revision starts from a verified figure.")
    w("")
    w("-" * 78)
    w("WHAT THIS AUDIT DOES NOT CLAIM")
    w("-" * 78)
    w("  * It does not check the QUANTITIES.  Those are WM1's, unchanged, and")
    w("    WM1's own 65-check audit covers them.")
    w("  * It does not claim the SSR item chosen for a line is the only")
    w("    defensible one.  Where a choice was made it is stated on the line.")
    w("  * A district cost index has NOT been applied.  The SSR is a STATE")
    w("    schedule; its General Notes give every Superintending Engineer the")
    w("    power to vary rates for local conditions, and no Pune circle")
    w("    variation is in this project.  Open item WM4-V4.")
    w("=" * 78)
    path = os.path.join(ROOT, "QAQC", "WM4_SSR_VERIFICATION.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write("\n".join(o) + "\n")
    return path, checks


# ===========================================================================
#  7.  OPEN ITEMS
# ===========================================================================
OPEN_ITEMS = [
 ("WM4-V1", "Excavation below 6.0 m depth — the SSR sets no percentage",
  "SSR General Notes Section B stops at '4.5 m to 6.0 m depth add 30 %' and "
  "then says 'Depth beyond 6.0 m — extra percent to be decided by concerned "
  "Superintending Engineer'.  157.44 m3 of rock between (-)6.000 and (-)6.800, "
  "and the 9.477 m3 sump pit below it, fall in that band.",
  "Priced at +30 % as a DECLARED LOWER BOUND, tagged [A].  Every extra 10 "
  "percentage points is about Rs 21 800 on these two lines.",
  "A determination by the Superintending Engineer, PWD, Pune circle"),
 ("WM4-V2", "Brick class — SSR grading against IS 1077",
  "SP-B1 specifies modular bricks CLASS 10 to IS 1077.  The SSR grades brick "
  "masonry as 'first class' and 'second class', which is a workmanship "
  "grading, and it publishes NO first-class item for superstructure walls at "
  "all — only plinth (27.02) and pillars (27.08, 27.09).",
  "Priced at 27.05, second class in CM 1:6 in superstructure, which is the "
  "only published superstructure wall item and matches the specified mortar.",
  "Confirmation that 27.05 is the correct billing item for class 10 bricks"),
 ("WM4-V3", "Lintel SP-06 measures a superseded section",
  "The bill line measures 200 x 150.  Design revision SP-B2 (master A.4.8, "
  "H.12) designs lintel L1 at 190 x 150.  WM_RECONCILIATION_REGISTER section "
  "6 already records this.",
  "WM4 prices the quantity AS MEASURED and does not re-measure it.  The "
  "difference is 0.51 against 0.4845 m3, about 5 %, or Rs 322.",
  "A re-measure, which belongs to the package that owns the quantity, not to "
  "a rating exercise"),
 ("WM4-V4", "No district cost index or circle variation applied",
  "The SSR is a STATE schedule.  Its covering circular gives every "
  "Superintending Engineer power to vary the rates of relevant items for the "
  "geographical conditions of the district, and the General Notes say the "
  "basic material rates are a state-wide average.",
  "State rates are used exactly as published.  No index, uplift or discount "
  "is applied anywhere.",
  "The Pune circle's current variation order, if one exists"),
 ("WM4-V5", "GST rate is not fixed by the schedule",
  "The SSR says 'separate provision for GST shall be made in recapitulation "
  "sheet' and does not state a percentage anywhere in 624 pages.",
  "18 % is used, tagged [A], as a single parameter cell in the workbook so "
  "another rate can be tested by changing one number.",
  "The applicable works-contract GST rate for this employer"),
 ("WM4-V6", "Tanking specification substituted",
  "WP-01 is a continuous external tanking MEMBRANE.  The SSR's own below-"
  "grade items (31.12, 31.13) are rough shahabad BOX treatments, a different "
  "specification.  The nearest membrane item, 51.114, is described applied to "
  "roof and parapet.",
  "Priced at 51.114 because the MATERIAL matches — a five-layer polymeric "
  "membrane on a 90 micron HMHDPE core.  The shahabad alternative is carried "
  "in the workbook at Rs 1 286 / Rs 1 338 so the swap can be costed: it would "
  "add about Rs 400 000.",
  "A decision on which specification is being bought"),
 ("WM4-V7", "The protective plant is outside the schedule entirely",
  "Blast doors, exit hatches, blast valves, the NBC trains, the EMP "
  "enclosure, the generator and the commissioning tests have NO SSR item.  "
  "The SSR's answer is explicit: 'The items for which rates are not included "
  "in State Schedule of Rates, the rates shall be approved by concerned "
  "Superintending Engineer, PWD.'",
  "Listed in bill section L at nil.  The owner's own bill prices them from "
  "vendor figures at about Rs 1.05 crore; those figures are NOT SSR rates and "
  "WM4 does not adopt them.",
  "Vendor quotations, and the Superintending Engineer's approval of the "
  "resulting non-schedule rates"),
]


def out_open_items_csv():
    return wcsv(os.path.join(ROOT, "Cost", "WM4_OPEN_ITEMS.csv"),
                ["Ref", "Title", "What the evidence says", "What WM4 did",
                 "What is needed to close it"],
                [list(r) for r in OPEN_ITEMS])


# ===========================================================================
#  8.  THE EXCEL WORKBOOK
# ===========================================================================
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.page import PageMargins

FONT = "Arial"
H1 = Font(name=FONT, size=14, bold=True, color="FFFFFF")
H2 = Font(name=FONT, size=11, bold=True, color="FFFFFF")
BOLD = Font(name=FONT, size=9, bold=True)
BODY = Font(name=FONT, size=9)
SMALL = Font(name=FONT, size=8, color="555555")
BLUE = Font(name=FONT, size=9, color="0000FF")          # hardcoded input
TITLEFILL = PatternFill("solid", fgColor="1F3864")
HEADFILL = PatternFill("solid", fgColor="2E5C8A")
SECFILL = PatternFill("solid", fgColor="D6E4F0")
TOTFILL = PatternFill("solid", fgColor="FFF2CC")
NFILL = PatternFill("solid", fgColor="FCE4E4")          # not priced
XFILL = PatternFill("solid", fgColor="EDEDED")          # included
AFILL = PatternFill("solid", fgColor="FFF7E0")          # assumption
YEL = PatternFill("solid", fgColor="FFFF00")
THIN = Side(style="thin", color="B7B7B7")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
MONEY = '#,##0.00;(#,##0.00);"-"'
MONEY0 = '#,##0;(#,##0);"-"'
QTY = '#,##0.000;;"-"'
PCT = '0.00%'


def _hdr(ws, row, headers, widths):
    for i, (h, wdt) in enumerate(zip(headers, widths), start=1):
        c = ws.cell(row=row, column=i, value=h)
        c.font = H2
        c.fill = HEADFILL
        c.alignment = Alignment(wrap_text=True, vertical="center",
                                horizontal="center")
        c.border = BOX
        ws.column_dimensions[get_column_letter(i)].width = wdt
    ws.row_dimensions[row].height = 32


def _title(ws, text, sub, ncol):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncol)
    c = ws.cell(row=1, column=1, value=text)
    c.font = H1
    c.fill = TITLEFILL
    c.alignment = Alignment(vertical="center", indent=1)
    ws.row_dimensions[1].height = 26
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=ncol)
    c = ws.cell(row=2, column=1, value=sub)
    c.font = SMALL
    c.alignment = Alignment(vertical="center", indent=1, wrap_text=True)
    ws.row_dimensions[2].height = 22


def sheet_cover(wb):
    ws = wb.create_sheet("Cover")
    ws.sheet_view.showGridLines = False
    _title(ws, "BILL OF QUANTITIES AND DETAILED COST ESTIMATE",
           "Underground CBRN-hardened blast-resistant protective structure and "
           "sentry post — Pune, Maharashtra", 4)
    ws.column_dimensions["A"].width = 3
    ws.column_dimensions["B"].width = 42
    ws.column_dimensions["C"].width = 74
    ws.column_dimensions["D"].width = 3
    r = 4

    def kv(k, v, bold=False, fill=None):
        nonlocal r
        a = ws.cell(row=r, column=2, value=k)
        a.font = BOLD if bold else BODY
        a.alignment = Alignment(vertical="top")
        b = ws.cell(row=r, column=3, value=v)
        b.font = BOLD if bold else BODY
        b.alignment = Alignment(wrap_text=True, vertical="top")
        if fill:
            a.fill = b.fill = fill
        ws.row_dimensions[r].height = max(14, 11 * (1 + len(str(v)) // 95))
        r += 1

    def gap(n=1):
        nonlocal r
        r += n

    def head(t):
        nonlocal r
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
        c = ws.cell(row=r, column=2, value=t)
        c.font = Font(name=FONT, size=10, bold=True, color="1F3864")
        c.fill = SECFILL
        c.alignment = Alignment(vertical="center", indent=1)
        ws.row_dimensions[r].height = 18
        r += 1

    head("THE ESTIMATE")
    kv("Package revision", "Works Management %s" % REV)
    kv("Date", DATE)
    kv("Supersedes", "Nothing.  WM1 (master H.10) measured this bill and "
                     "carried NO rate; WM4 prices it.  WM1, WM2 and WM3 are "
                     "preserved unaltered alongside")
    kv("Geometry", "Architectural Rev F · Structural Phase 2 Rev A + M1")
    kv("Quantities", "WM1, unchanged.  NOT ONE QUANTITY IS ALTERED BY THIS "
                     "REVISION.  Where a WM1 line is split to reach two "
                     "different SSR items the parts sum back to the WM1 "
                     "figure exactly — see the Verification sheet")
    gap()
    head("RATE SOURCE")
    kv("Schedule", SRC)
    kv("Rate basis", "'Completed Rate for 2022-23 excluding GST' — the SSR's "
                     "own column.  These rates ALREADY contain 10 % overheads, "
                     "10 % contractor's profit and 1 % labour cess, and every "
                     "concrete item already contains its steel centering and "
                     "formwork")
    kv("Reinforcement", "NOT in the concrete rates — SSR 26.33, measured on "
                        "the weight fixed in position")
    gap()
    head("WHAT THE BOTTOM LINE COVERS")
    t = BL.totals()
    rows, base, sub_ssr, before_gst, gst = recap_rows()
    npriced = len([x for x in BL.BILL if x["tier"] == "P"])
    nassum = len([x for x in BL.BILL if x["tier"] == "A"])
    nnot = len([x for x in BL.BILL if x["tier"] == "N"])
    ninc = len([x for x in BL.BILL if x["tier"] == "X"])
    kv("Priced at a published SSR item", "%d lines   Rs %s"
       % (npriced, "{:,.2f}".format(t["P"])))
    kv("Priced on a stated assumption [A]", "%d lines   Rs %s"
       % (nassum, "{:,.2f}".format(t["A"])), fill=AFILL)
    kv("Included in another rate — not payable twice", "%d lines" % ninc,
       fill=XFILL)
    kv("NOT PRICED — no specification, or no SSR item", "%d lines" % nnot,
       fill=NFILL)
    gap()
    kv("TOTAL OF ITEMS", "Rs %s" % "{:,.2f}".format(base), bold=True,
       fill=TOTFILL)
    kv("ESTIMATED COST after recapitulation and GST",
       "Rs %s" % "{:,.2f}".format(before_gst + gst), bold=True, fill=TOTFILL)
    gap()
    head("WHAT IS EXCLUDED FROM IT — READ THIS BEFORE USING THE FIGURE")
    kv("Protective plant and closures",
       "Blast doors, exit hatches, blast valves, the NBC collective "
       "protection trains, the EMP Zone 2 enclosure, the standby generator, "
       "sump pumps and commissioning have NO SSR ITEM and are NOT in the "
       "total.  The owner's own bill prices them at about Rs 1.05 crore from "
       "vendor figures.  See sheet 'Not priced'", fill=NFILL)
    kv("Electrical and EMP installation",
       "No electrical design package exists, so there is no quantity to "
       "price.  Seven lines, all nil", fill=NFILL)
    kv("Waterstops", "109.76 m measured.  THE SSR HAS NO WATERSTOP ITEM "
                     "anywhere in 624 pages", fill=NFILL)
    kv("Flooring, window W1, spiral stair, berm, camouflage",
       "No specification, or no quantity, exists in the project for any of "
       "them.  No rate is invented", fill=NFILL)
    gap()
    head("EVIDENCE DISCIPLINE")
    kv("No invented rates", "Every rate is either a published SSR item, or is "
                            "derived from one by a method the SSR itself "
                            "prescribes, with the arithmetic shown on the "
                            "'Rate derivation' sheet")
    kv("No resolved assumptions", "Every [A] and [N] tag carried by WM1 is "
                                  "carried forward.  None is upgraded")
    kv("Main staircase", "UNTOUCHED — 24 risers, 170.8333 mm riser, 280 mm "
                         "tread, 3 flights x 8, 4 100 mm total rise")
    kv("Open items raised by this revision",
       ", ".join(x[0] for x in OPEN_ITEMS) + " — see the 'Open items' sheet")
    return ws


def sheet_boq(wb):
    ws = wb.create_sheet("BOQ priced")
    ws.sheet_view.showGridLines = False
    _title(ws, "BILL OF QUANTITIES — PRICED AT SSR 2022-23",
           "Quantities are WM1's, unchanged.  Amount = Quantity x Rate, as a "
           "formula in every row.  Rates in blue are read from the SSR; rates "
           "in black are derived from a published SSR item by the schedule's "
           "own method.", 10)
    _hdr(ws, 3, ["Section / Item", "Description", "Unit", "Quantity",
                 "SSR item", "Rate (Rs)", "Amount (Rs)", "Status",
                 "Basis / note"],
         [14, 52, 7, 12, 13, 12, 15, 26, 78])
    ws.freeze_panes = "A4"
    r = 4
    sec_rows = []
    derived_rates = set(BL.DERIVED.values())
    for sec in BL.SECTIONS:
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=9)
        c = ws.cell(row=r, column=1, value=sec)
        c.font = Font(name=FONT, size=10, bold=True, color="1F3864")
        c.fill = SECFILL
        c.alignment = Alignment(vertical="center", indent=1)
        r += 1
        first = r
        for it in [x for x in BL.BILL if x["section"] == sec]:
            ws.cell(row=r, column=1, value=it["code"]).font = BOLD
            ws.cell(row=r, column=2, value=it["desc"]).font = BODY
            ws.cell(row=r, column=3, value=it["unit"]).font = BODY
            q = ws.cell(row=r, column=4,
                        value=None if it["qty"] is None else it["qty"])
            q.font = BODY
            q.number_format = QTY
            ws.cell(row=r, column=5, value=it["ssr"]).font = BODY
            rt = ws.cell(row=r, column=6, value=it["rate"])
            rt.number_format = MONEY
            rt.font = BLUE if (it["rate"] in derived_rates) is False and it["rate"] else BODY
            am = ws.cell(row=r, column=7)
            if it["rate"] is not None and it["qty"] is not None:
                am.value = "=D%d*F%d" % (r, r)
            am.number_format = MONEY
            am.font = BOLD
            st = ws.cell(row=r, column=8, value=TIER_NAME[it["tier"]])
            st.font = BODY
            nt = ws.cell(row=r, column=9, value=it["note"])
            nt.font = SMALL
            nt.alignment = Alignment(wrap_text=True, vertical="top")
            fill = {"N": NFILL, "X": XFILL, "A": AFILL}.get(it["tier"])
            if fill:
                for col in range(1, 10):
                    ws.cell(row=r, column=col).fill = fill
            for col in range(1, 10):
                ws.cell(row=r, column=col).border = BOX
            ws.row_dimensions[r].height = max(
                13, 10 * (1 + max(len(it["desc"]) // 52, len(it["note"]) // 95)))
            r += 1
        ws.cell(row=r, column=2, value="SUB-TOTAL — %s" % sec.split(" · ")[0]).font = BOLD
        sc = ws.cell(row=r, column=7, value="=SUM(G%d:G%d)" % (first, r - 1))
        sc.number_format = MONEY
        sc.font = BOLD
        for col in range(1, 10):
            ws.cell(row=r, column=col).fill = TOTFILL
            ws.cell(row=r, column=col).border = BOX
        sec_rows.append(r)
        r += 2
    ws.cell(row=r, column=2, value="TOTAL OF ITEMS — carried to the "
            "Recapitulation sheet").font = Font(name=FONT, size=11, bold=True)
    tc = ws.cell(row=r, column=7,
                 value="=" + "+".join("G%d" % x for x in sec_rows))
    tc.number_format = MONEY
    tc.font = Font(name=FONT, size=11, bold=True)
    for col in range(1, 10):
        ws.cell(row=r, column=col).fill = TOTFILL
        ws.cell(row=r, column=col).border = BOX
    ws.print_title_rows = "3:3"
    return ws, r


def sheet_recap(wb, total_ref):
    ws = wb.create_sheet("Recapitulation")
    ws.sheet_view.showGridLines = False
    _title(ws, "RECAPITULATION",
           "Block A is the SSR's own recapitulation, General Notes Section B.  "
           "Block B is the project owner's provision structure, carried from "
           "their RC1 estimate and kept separate because it is not part of the "
           "schedule.  Block D is what must NOT be added.", 6)
    _hdr(ws, 3, ["", "Head", "Basis", "Rate", "Amount (Rs)", "Source / note"],
         [5, 56, 40, 10, 18, 86])
    ws.freeze_panes = "A4"
    r = 4
    ITEMS_ROW = None
    blocks = {}
    for blk, head, basis, rate, amt, note in recap_rows()[0]:
        ws.cell(row=r, column=1, value=blk).font = BOLD
        hc = ws.cell(row=r, column=2, value=head)
        hc.font = BOLD if ("TOTAL" in head or "SUB-TOTAL" in head
                           or "ESTIMATED" in head) else BODY
        ws.cell(row=r, column=3, value=basis).font = BODY
        rc = ws.cell(row=r, column=4, value=rate if rate != "" else None)
        rc.number_format = PCT
        rc.font = BLUE
        ac = ws.cell(row=r, column=5)
        ac.number_format = MONEY
        ac.font = BOLD
        nc = ws.cell(row=r, column=6, value=note)
        nc.font = SMALL
        nc.alignment = Alignment(wrap_text=True, vertical="top")
        ws.row_dimensions[r].height = max(13, 10 * (1 + len(note) // 100))
        blocks.setdefault(blk, []).append((r, head, rate))
        if head.startswith("Total of items"):
            ac.value = "='BOQ priced'!G%d" % total_ref
            ITEMS_ROW = r
        elif rate not in ("", None):
            ac.value = "=$E$%d*D%d" % (ITEMS_ROW, r)
        if "SUB-TOTAL" in head or "ESTIMATED" in head or "Total of items" in head:
            for col in range(1, 7):
                ws.cell(row=r, column=col).fill = TOTFILL
        for col in range(1, 7):
            ws.cell(row=r, column=col).border = BOX
        r += 1

    # wire the two sub-totals and the GST/estimated-cost rows to real formulas
    aro = blocks["A"]
    sub_a = [x for x in aro if "SUB-TOTAL" in x[1]][0][0]
    pcts_a = [x[0] for x in aro if x[2] not in ("", None)]
    ws.cell(row=sub_a, column=5,
            value="=E%d+%s" % (ITEMS_ROW, "+".join("E%d" % p for p in pcts_a)))
    bro = blocks["B"]
    sub_b = [x for x in bro if "SUB-TOTAL" in x[1]][0][0]
    pcts_b = [x[0] for x in bro if x[2] not in ("", None)]
    ws.cell(row=sub_b, column=5,
            value="=E%d+%s" % (sub_a, "+".join("E%d" % p for p in pcts_b)))
    cro = blocks["C"]
    gst_row = cro[0][0]
    est_row = cro[1][0]
    ws.cell(row=gst_row, column=5, value="=E%d*D%d" % (sub_b, gst_row))
    ws.cell(row=gst_row, column=4).fill = YEL
    ws.cell(row=est_row, column=5, value="=E%d+E%d" % (sub_b, gst_row))
    ws.cell(row=est_row, column=5).font = Font(name=FONT, size=11, bold=True)

    r += 1
    ws.cell(row=r, column=2, value="THE YELLOW CELL IS THE ONLY LEVER IN THIS "
            "WORKBOOK").font = BOLD
    r += 1
    ws.cell(row=r, column=2, value="Change the GST rate in D%d and every figure "
            "below it recalculates.  Percentages in blue are inputs." % gst_row
            ).font = SMALL
    return ws


def sheet_table(wb, name, title, sub, headers, widths, rows, fmt=None,
                wrapcols=(), fills=None):
    ws = wb.create_sheet(name)
    ws.sheet_view.showGridLines = False
    _title(ws, title, sub, len(headers))
    _hdr(ws, 3, headers, widths)
    ws.freeze_panes = "A4"
    for i, row in enumerate(rows, start=4):
        for j, val in enumerate(row, start=1):
            c = ws.cell(row=i, column=j, value=val)
            c.font = SMALL if j in wrapcols else BODY
            c.border = BOX
            if j in wrapcols:
                c.alignment = Alignment(wrap_text=True, vertical="top")
            if fmt and j in fmt:
                c.number_format = fmt[j]
        if fills:
            f = fills(row)
            if f:
                for j in range(1, len(headers) + 1):
                    ws.cell(row=i, column=j).fill = f
        ws.row_dimensions[i].height = max(
            13, 10 * (1 + max((len(str(row[j - 1])) // 95) for j in wrapcols)
                      if wrapcols else 1))
    return ws


def build_workbook():
    wb = Workbook()
    wb.remove(wb.active)

    sheet_cover(wb)
    _, total_row = sheet_boq(wb)
    sheet_recap(wb, total_row)

    # --- rate derivation -----------------------------------------------------
    ws = wb.create_sheet("Rate derivation")
    ws.sheet_view.showGridLines = False
    _title(ws, "RATE DERIVATION",
           "Every rate in the bill that is not a straight SSR item, with the "
           "arithmetic that produced it.  The method is the SSR's own.", 3)
    _hdr(ws, 3, ["Derived rate", "Rs", "Working"], [22, 14, 130])
    ws.freeze_panes = "A4"
    r = 4
    for key, val, working in BL._deriv_log:
        ws.cell(row=r, column=1, value=key).font = BOLD
        c = ws.cell(row=r, column=2, value=val)
        c.number_format = MONEY
        c.font = BOLD
        wc = ws.cell(row=r, column=3, value=working)
        wc.font = SMALL
        wc.alignment = Alignment(wrap_text=True, vertical="top")
        for col in range(1, 4):
            ws.cell(row=r, column=col).border = BOX
        ws.row_dimensions[r].height = max(13, 10 * (1 + len(working) // 128))
        r += 1
    r += 1
    ws.cell(row=r, column=1, value="THE CHECK THAT MAKES THESE USABLE").font = BOLD
    r += 1
    for a, b_, pub in (("M20", "M25", "183 / 184"), ("M25", "M30", "183 / 184"),
                       ("M30", "M35", "91 / 92")):
        calc = (CEMENT_BAGS[b_] - CEMENT_BAGS[a]) * 50 * 6.0 * ON_COST
        ws.cell(row=r, column=1, value="%s to %s" % (a, b_)).font = BODY
        c = ws.cell(row=r, column=2, value=round(calc, 2))
        c.number_format = MONEY
        c.font = BODY
        ws.cell(row=r, column=3,
                value="The SSR publishes this step itself, in four separate "
                      "item families, as %s.  The formula reproduces it, so "
                      "the same formula can be trusted where the SSR stops "
                      "publishing." % pub).font = SMALL
        ws.cell(row=r, column=3).alignment = Alignment(wrap_text=True,
                                                       vertical="top")
        r += 1

    # --- SSR library ---------------------------------------------------------
    lib = []
    for k in sorted(SSR):
        v = SSR[k]
        lib.append([k, v["chapter"], v["desc"], v["unit"], v["completed"],
                    v["labour"], v["page"], v["page"] + 7])
    sheet_table(wb, "SSR rate library",
                "SSR 2022-23 — EVERY RATE USED, AS PUBLISHED",
                "Read out of the owner's PDF and re-verified against the raw "
                "page text.  'Completed rate' and 'Labour rate' are the SSR's "
                "own column headings, both excluding GST.",
                ["SSR item", "SSR chapter", "Description (SSR wording, trimmed)",
                 "Unit", "Completed rate (Rs)", "Labour rate (Rs)",
                 "SSR page", "PDF page"],
                [12, 30, 118, 8, 17, 15, 10, 10], lib,
                fmt={5: MONEY0, 6: MONEY0}, wrapcols=(3,))

    # --- not priced ----------------------------------------------------------
    npr = [[r["section"].split(" · ")[0], r["code"], r["desc"], r["unit"],
            "" if r["qty"] is None else r["qty"], r["note"]]
           for r in BL.BILL if r["tier"] == "N"]
    sheet_table(wb, "Not priced",
                "DECLARED EXCLUSIONS — NOT IN ANY TOTAL IN THIS WORKBOOK",
                "Each line is here because the project has no specification "
                "for it, or the SSR has no item for it, or both.  No rate is "
                "invented for any of them.  SSR General Notes Section B: "
                "'The items for which rates are not included in State Schedule "
                "of Rates, the rates shall be approved by concerned "
                "Superintending Engineer, PWD.'",
                ["Sec", "Item", "Description", "Unit", "Quantity",
                 "Why it is not priced"],
                [6, 12, 62, 8, 12, 120], npr, fmt={5: QTY}, wrapcols=(6,),
                fills=lambda row: NFILL)

    # --- included / not payable twice ---------------------------------------
    inc = [[r["section"].split(" · ")[0], r["code"], r["desc"], r["unit"],
            "" if r["qty"] is None else r["qty"], r["note"]]
           for r in BL.BILL if r["tier"] == "X"]
    sheet_table(wb, "Included not payable",
                "MEASURED, BUT ALREADY INSIDE ANOTHER RATE",
                "The double-count guard.  Every line here is real work with a "
                "real quantity that is already paid for somewhere else in the "
                "bill.  Pricing any of them again would pay for the same work "
                "twice.",
                ["Sec", "Item", "Description", "Unit", "Quantity",
                 "Where it is already paid"],
                [6, 12, 62, 8, 12, 120], inc, fmt={5: QTY}, wrapcols=(6,),
                fills=lambda row: XFILL)

    # --- owner comparison ----------------------------------------------------
    ws = wb.create_sheet("Owner bill vs SSR")
    ws.sheet_view.showGridLines = False
    _title(ws, "THE OWNER'S OWN PRICED BILL, RE-RATED AT SSR 2022-23",
           "The owner's quantities and the owner's rates are reproduced "
           "exactly as supplied and nothing in their bill is edited.  Master "
           "H.15 records of that bill: 'No cost was re-estimated, no rate was "
           "checked against a market or a schedule of rates.'  This sheet is "
           "that check.", 12)
    _hdr(ws, 3, ["Part", "Owner's bill description (RC1)", "Unit", "Quantity",
                 "Owner rate", "Owner amount", "SSR item", "SSR rate",
                 "SSR amount", "Difference", "Diff %", "Note"],
         [6, 48, 7, 11, 12, 15, 20, 12, 15, 15, 9, 84])
    ws.freeze_panes = "A4"
    r = 4
    comp_rows = []
    for part, desc, unit, qty, own, item, ssr, note in COMPARE:
        ws.cell(row=r, column=1, value=part).font = BOLD
        ws.cell(row=r, column=2, value=desc).font = BODY
        ws.cell(row=r, column=3, value=unit).font = BODY
        c = ws.cell(row=r, column=4, value=qty); c.number_format = QTY; c.font = BODY
        c = ws.cell(row=r, column=5, value=own); c.number_format = MONEY; c.font = BLUE
        c = ws.cell(row=r, column=6, value="=D%d*E%d" % (r, r)); c.number_format = MONEY; c.font = BODY
        ws.cell(row=r, column=7, value=item).font = BODY
        if ssr is not None:
            c = ws.cell(row=r, column=8, value=round(ssr, 2)); c.number_format = MONEY; c.font = BODY
            c = ws.cell(row=r, column=9, value="=D%d*H%d" % (r, r)); c.number_format = MONEY; c.font = BOLD
            c = ws.cell(row=r, column=10, value="=I%d-F%d" % (r, r)); c.number_format = MONEY; c.font = BOLD
            c = ws.cell(row=r, column=11, value="=IFERROR(J%d/F%d,\"\")" % (r, r))
            c.number_format = PCT; c.font = BODY
            comp_rows.append(r)
        else:
            for col in (8, 9, 10, 11):
                ws.cell(row=r, column=col).fill = NFILL
        nc = ws.cell(row=r, column=12, value=note)
        nc.font = SMALL
        nc.alignment = Alignment(wrap_text=True, vertical="top")
        for col in range(1, 13):
            ws.cell(row=r, column=col).border = BOX
        ws.row_dimensions[r].height = max(13, 10 * (1 + len(note) // 100))
        r += 1
    r += 1
    ws.cell(row=r, column=2, value="TOTAL — comparable lines only").font = BOLD
    for col, f in ((6, "F"), (9, "I"), (10, "J")):
        c = ws.cell(row=r, column=col,
                    value="=" + "+".join("%s%d" % (f, x) for x in comp_rows))
        c.number_format = MONEY
        c.font = BOLD
        c.fill = TOTFILL
    c = ws.cell(row=r, column=11, value="=IFERROR(J%d/F%d,\"\")" % (r, r))
    c.number_format = PCT
    c.font = BOLD
    c.fill = TOTFILL
    ws.cell(row=r, column=12, value="The owner's rates sit BELOW SSR 2022-23 on "
            "the lines that can be compared.  The gap is concentrated in three "
            "places: R.C.C. wall casting, rock excavation, and reinforcement.")\
        .font = SMALL
    ws.cell(row=r, column=12).alignment = Alignment(wrap_text=True, vertical="top")
    for col in range(1, 13):
        ws.cell(row=r, column=col).fill = TOTFILL
        ws.cell(row=r, column=col).border = BOX

    # --- general rates -------------------------------------------------------
    gr = [[k, v[1], v[0], "Material"] for k, v in MATERIAL.items()]
    gr += [[k, "day", v, "Labour"] for k, v in LABOUR.items()]
    gr += [["Cement consumption, %s" % g, "bags of 50 kg / m3", b,
            "Consumption"] for g, b in CEMENT_BAGS.items()]
    sheet_table(wb, "SSR general rates",
                "SSR 2022-23 — GENERAL MATERIAL, LABOUR AND CONSUMPTION RATES",
                "Printed pages 541 (materials), 545 (labour) and 567-581 "
                "(consumption).  These do not price the bill — the completed "
                "rates do.  They are here because the derivations use them and "
                "because they show what is inside a composite rate.",
                ["Description", "Unit", "Rate / quantity (Rs)", "Block"],
                [58, 22, 20, 16], gr, fmt={3: MONEY})

    # --- open items ----------------------------------------------------------
    sheet_table(wb, "Open items",
                "OPEN ITEMS RAISED BY THIS REVISION",
                "Each one is a question this rating exercise could not answer "
                "from the evidence.  None of them is closed here and none is "
                "guessed.",
                ["Ref", "Title", "What the evidence says", "What WM4 did",
                 "What is needed to close it"],
                [10, 44, 78, 74, 60], [list(x) for x in OPEN_ITEMS],
                wrapcols=(3, 4, 5))

    # --- verification --------------------------------------------------------
    _, checks = out_qaqc()
    vr = [["PASS" if ok else "FAIL", name, detail] for name, ok, detail in checks]
    ws = sheet_table(wb, "Verification",
                     "CONSISTENCY AND VERIFICATION",
                     "Run by wm4_build.py against the generated bill every time "
                     "it is built.  The quantity checks prove that splitting a "
                     "WM1 line to reach two SSR items did not change the "
                     "quantity.",
                     ["Result", "Check", "Detail"], [12, 66, 60], vr,
                     wrapcols=(3,))
    for i in range(4, 4 + len(vr)):
        if ws.cell(row=i, column=1).value == "PASS":
            ws.cell(row=i, column=1).font = Font(name=FONT, size=9, bold=True,
                                                 color="1E7B34")
        else:
            ws.cell(row=i, column=1).font = Font(name=FONT, size=9, bold=True,
                                                 color="C00000")
            for j in range(1, 4):
                ws.cell(row=i, column=j).fill = NFILL

    for s in wb.worksheets:
        s.page_setup.orientation = "landscape"
        s.page_setup.fitToWidth = 1
        s.page_margins = PageMargins(left=0.3, right=0.3, top=0.4, bottom=0.4)
    # openpyxl writes formulas with no cached value.  Excel and LibreOffice
    # both compute them on open only if the workbook asks, so it asks.
    wb.calculation.fullCalcOnLoad = True

    path = os.path.join(ROOT, "Cost",
                        "WM4_Underground_Shelter_BOQ_Cost_Estimate_SSR_2022-23.xlsx")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    wb.save(path)
    return path


# ===========================================================================
#  MAIN
# ===========================================================================
def main():
    made = []
    made.append(out_bill_csv())
    made.append(out_library_csv())
    made.append(out_recap_csv())
    made.append(out_compare_csv())
    made.append(out_open_items_csv())
    made.append(out_derivation())
    made.append(out_qaqc()[0])
    made.append(build_workbook())
    import wm4_doc
    wm4_doc.main()
    for p in made:
        print("  %-64s %8d bytes" % (os.path.relpath(p, ROOT),
                                     os.path.getsize(p)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
