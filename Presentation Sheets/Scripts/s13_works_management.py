"""
s13_works_management.py  --  WMS013  WORKS MANAGEMENT: MASTER CONSTRUCTION
                             PROGRAMME AND BILL OF QUANTITIES SUMMARY

Two charts and five schedules, in the layout and with the title block of the
supplied Revit A2 set (ARCH001..ARCH005), so that SHEET 13 reads as the next
sheet of that series:

    1  MASTER CONSTRUCTION PROGRAMME - BAR CHART                    NTS
    2  COST DISTRIBUTION BY BILL PART                               NTS

WHICH REVISION.  This sheet presents **WM3**, the REVISED owner package of
master H.15, whose final project cost is **Rs 2,97,90,913** and whose programme
is the revised master construction schedule R1: 224 working days, 02-11-26 to
26-07-27.  It is NOT WM4, the later bill priced from the Maharashtra PWD State
Schedule of Rates 2022-23, which is a different total on a different basis.

Every amount, quantity, count, date and duration on this sheet is read at build
time from the WM3 output files under `WORKS MANAGEMENT/`; nothing is retyped and
nothing is re-derived.

COLOUR: dark only, and mostly black.  ACI 7 black, 8 dark grey, 1 dark red for
the four top-level programme phases and the largest bill part, 5 dark blue for
the sub-summaries.
"""
import datetime as _dt
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
for _p in ("Structural CAD", "Drainage", "Fire and Life Safety"):
    sys.path.insert(0, os.path.join(ROOT, _p, "Scripts"))

from a2_lib import A2Sheet, tw                                # noqa: E402
import ops_data as D                                          # noqa: E402

RCOL, RCOL_W, RTOP = 282.0, 178.0, 383.0
RULE_TO = 272.0
SM, SMS = 1.9, 1.75

GX0, GX1 = 47.0, 272.0            # view 1 extent
GLAB = 118.0                      # right edge of the task-name column
GY_TOP, GBAR = 350.0, 8.0         # first bar top, bar pitch
V1_TTL = 194.0

CX0, CX1 = 47.0, 272.0            # view 2 extent
CLAB = 128.0
CY_TOP, CBAR = 152.0, 18.0
V2_TTL = 44.0

s = A2Sheet(
    sheet_no="SHEET 13",
    drawing_no="WMS013",
    title_lines=["WORKS", "MANAGEMENT -", "MASTER PROGRAMME", "AND BILL OF",
                 "QUANTITIES"],
    project_lines=D.PROJECT_LINES,
    identity=D.IDENTITY,
    notes=[
        "ALL AMOUNTS ARE IN INDIAN RUPEES. ALL DURATIONS ARE IN WORKING DAYS.",
        "WRITTEN FIGURES TO BE FOLLOWED ONLY. THE BAR CHART IS NOT TO BE "
        "SCALED FOR A DATE.",
        "THIS DRG IS TO BE READ IN CONJUNCTION WITH THE FULL BILL OF "
        "QUANTITIES, THE COST ESTIMATE AND THE MASTER CONSTRUCTION SCHEDULE.",
        f"FINAL PROJECT COST Rs {D.FINAL_COST}, BUILT UP FROM A TOTAL BASIC "
        f"COST OF Rs {D.BASIC_COST} IN FIVE BILL PARTS.",
        f"MASTER CONSTRUCTION PROGRAMME {D.PROG_DAYS.upper()}, "
        f"{D.PROG_START} TO {D.PROG_FINISH}, IN FOUR PHASES: INITIAL WORKS, "
        f"SUBSTRUCTURE, SUPERSTRUCTURE AND FINISHING.",
        "THE BURSTER SLAB IS 200 THK M30 AND 38.40 CUM. THE SENTRY POST IS "
        "MEASURED AS AN RC FRAME WITH ITS BRICK INFILL MEASURED SEPARATELY "
        "AS BRICKWORK.",
        "THE TWO ESCAPE SHAFT COLLARS, 250 RC AT OD 1900, ARE MEASURED AS A "
        "LINE AT 6.285 CUM, AND THE 15 kVA GENERATOR IS A VISIBLE LINE.",
        "THE CONCRETE TOTAL IS 467.59 CUM, WHICH IS THE SUM OF ITS OWN LINES.",
        "AMOUNTS ARE FROM THE REVISED BILL OF QUANTITIES. A LINE SHOWN NIL IS "
        "NOT PRICED IN IT.",
        "CONTRACTOR TO CHECK AND VERIFY THE FIGURES BEFORE TENDER.",
    ],
    date=D.DATE,
    drawn=D.DRAWN,
    checked=D.CHECKED,
    scale_note="Not to scale",
)

for _nm, _col, _lw, _desc in [
    ("W-GRID",  8, 13, "Chart grid and time axis"),
    ("W-AXIS",  7, 25, "Chart axes and frames"),
    ("W-BAR",   7, 35, "Bars, sub-summary"),
    ("W-PHASE", 1, 50, "Bars, top-level phase"),
    ("W-SUB",   5, 35, "Bars, sub-summary"),
    ("W-TEXT",  7, 18, "Chart annotation"),
]:
    _ly = s.doc.layers.add(_nm)
    _ly.color, _ly.lineweight, _ly.description = _col, _lw, _desc


def hbar(x0, x1, y0, y1, layer, dense=True):
    """A solid-reading bar: outline plus a dark hatch."""
    s.rect(x0, y0, x1, y1, layer)
    if x1 - x0 > 0.6:
        s.hatch_pat([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], "ANSI31",
                    0.55 if dense else 1.3, 0.0, "S-HATCH")


# =====================================================================  VIEW 1
# MASTER CONSTRUCTION PROGRAMME - BAR CHART
def _d(s_):
    return _dt.datetime.strptime(s_, "%d-%m-%y").date()


T0, T1 = _d(D.PROG_START), _d(D.PROG_FINISH)
SPAN = (T1 - T0).days


def TX(day):
    return GLAB + 6.0 + (GX1 - GLAB - 6.0) * day / SPAN


# month grid across the top
m = _dt.date(T0.year, T0.month, 1)
AX = GY_TOP + 6.0
s.text(T0.strftime("%b %y").upper(), (GLAB + 6.8, AX - 1.2), SMS, "W-TEXT",
       "L")
while m <= T1:
    dd = (m - T0).days
    if 26 <= dd <= SPAN:
        s.line((TX(dd), GY_TOP + 3.0),
               (TX(dd), GY_TOP - len(D.GANTT) * GBAR - 1.0), "W-GRID")
        s.text(m.strftime("%b %y").upper(), (TX(dd) + 0.8, AX - 1.2), SMS,
               "W-TEXT", "L")
    m = _dt.date(m.year + (m.month // 12), m.month % 12 + 1, 1)
s.line((GLAB + 6.0, GY_TOP + 3.0), (GX1, GY_TOP + 3.0), "W-AXIS")
s.line((GX0, GY_TOP + 3.0), (GX0, GY_TOP - len(D.GANTT) * GBAR - 1.0),
       "W-AXIS")
s.line((GX0, GY_TOP - len(D.GANTT) * GBAR - 1.0),
       (GX1, GY_TOP - len(D.GANTT) * GBAR - 1.0), "W-AXIS")

PHASE_IDS = {"2", "6", "27", "86"}
for i, ((name, dur, st, fi), tid) in enumerate(zip(D.GANTT, D.GANTT_IDS)):
    yt = GY_TOP - i * GBAR
    yb = yt - GBAR
    top = tid in PHASE_IDS or tid == "1"
    lay = "W-PHASE" if top else "W-SUB"
    nm = ("MASTER CONSTRUCTION SCHEDULE" if tid == "1"
          else name if top else "   " + name)
    h = min(SMS, (RCOL_W and SMS))
    txt = nm
    while tw(txt, h) > GLAB - GX0 - 4.0 and len(txt) > 8:
        txt = txt[:-1]
    s.text(txt, (GX0 + 2.0, yt - GBAR / 2.0), h, "W-TEXT", "ML")
    a, b = (_d(st) - T0).days, (_d(fi) - T0).days
    hbar(TX(a), max(TX(b), TX(a) + 0.8), yb + 2.0, yt - 2.0, lay,
         dense=not top)
    s.text(dur.replace(" days", "d"), (max(TX(b), TX(a) + 0.8) + 1.4,
                                       yt - GBAR / 2.0), SMS, "W-TEXT", "ML")
    s.line((GX0, yb), (GX1, yb), "W-GRID")

s.text(f"{D.PROG_DAYS.upper()}   {D.PROG_START}  TO  {D.PROG_FINISH}",
       (GX0 + 2.0, GY_TOP + 9.0), SM, "S-TITLE", "L")
s.view_title(GX0 - 4.0, V1_TTL, "1",
             "MASTER CONSTRUCTION PROGRAMME - BAR CHART",
             f"NOT TO SCALE   {len(D.GANTT)} SUMMARY ACTIVITIES OF THE "
             f"130 IN THE REVISED SCHEDULE", RULE_TO)

# =====================================================================  VIEW 2
# COST DISTRIBUTION BY BILL PART
TOT = max(t for p, n, t in D.PART_TOTALS)
for i, (p, n, t) in enumerate(D.PART_TOTALS):
    yt = CY_TOP - i * CBAR
    yb = yt - CBAR
    lab = p.replace("PART ", "")
    part_no = lab.split(" - ")[0]
    rest = lab.split(" - ", 1)[1] if " - " in lab else ""
    s.text(f"PART {part_no}", (CX0 + 2.0, yt - 4.6), SM, "W-TEXT", "ML")
    txt = rest
    while tw(txt, SMS) > CLAB - CX0 - 4.0 and len(txt) > 8:
        txt = txt[:-1]
    s.text(txt, (CX0 + 2.0, yt - 9.4), SMS, "W-TEXT", "ML")
    w = (CX1 - CLAB - 34.0) * t / TOT
    hbar(CLAB, CLAB + w, yb + 3.0, yt - 3.0, "W-BAR" if i < 4 else "W-PHASE",
         dense=i < 4)
    s.text(f"Rs {D._money(t)}", (CLAB + w + 1.8, yt - CBAR / 2.0), SM,
           "W-TEXT", "ML")
    s.text(f"{n} ITEMS", (CLAB - 2.0, yt - CBAR / 2.0), SMS, "W-TEXT", "MR")
s.line((CX0, CY_TOP), (CX1, CY_TOP), "W-AXIS")
s.line((CX0, CY_TOP - len(D.PART_TOTALS) * CBAR),
       (CX1, CY_TOP - len(D.PART_TOTALS) * CBAR), "W-AXIS")
s.line((CLAB, CY_TOP), (CLAB, CY_TOP - len(D.PART_TOTALS) * CBAR), "W-AXIS")
s.text(f"TOTAL BASIC COST  Rs {D.BASIC_COST}   IN 38 MEASURED ITEMS",
       (CX0 + 2.0, CY_TOP + 4.6), SM, "S-TITLE", "L")
s.text(f"FINAL PROJECT COST  Rs {D.FINAL_COST}",
       (CX0 + 2.0, CY_TOP - len(D.PART_TOTALS) * CBAR - 5.6), SM, "S-TITLE",
       "L")
s.view_title(CX0 - 4.0, V2_TTL, "2", "COST DISTRIBUTION BY BILL PART",
             "NOT TO SCALE   BARS IN PROPORTION TO AMOUNT", RULE_TO)

# =====================================================================  TABLES
y = s.table_stack(RCOL, RTOP, 35.5, RCOL_W, [
    dict(rows=D.COST_SUMMARY, title="COST SUMMARY",
         header=["COST HEAD", "BASIS", "AMOUNT  Rs"],
         align=["L", "C", "R"], pad=2.2),
    dict(rows=D.PART_SUMMARY, title="BILL OF QUANTITIES - PART SUMMARY",
         header=["PART", "DESCRIPTION", "ITEMS", "AMOUNT  Rs"],
         align=["C", "L", "C", "R"], pad=2.2),
    dict(rows=D.PRINCIPAL_ITEMS, title="PRINCIPAL BILL ITEMS BY VALUE",
         header=["ITEM", "UNIT", "QTY", "AMOUNT  Rs"],
         align=["L", "C", "R", "R"], pad=2.2),
    dict(rows=D.MILESTONES, title="PROGRAMME PHASES",
         header=["PHASE", "DURATION", "START", "FINISH"],
         align=["L", "C", "C", "C"], pad=2.2),
    dict(rows=D.WM3_APPLIED, title="WHAT THE REVISED BILL CARRIES",
         header=["ITEM", "AS MEASURED", "QUANTITY", "NOTES"],
         align=["L", "L", "C", "L"], pad=2.2),
], gap=5.0, rh_max=7.2)
assert y > 35.0, f"the schedule stack overflows the frame: bottom at {y:.1f}"


if __name__ == "__main__":
    out = os.path.join(ROOT, "Presentation Sheets", "DXF",
                       "WMS013_Works_Management_Master_Programme_and_Bill_of_"
                       "Quantities.dxf")
    s.save(out)
    print("written", out, "| right column bottom y =", round(y, 1))
