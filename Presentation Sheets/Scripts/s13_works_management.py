"""
s13_works_management.py  --  WMS013  WORKS MANAGEMENT: MASTER CONSTRUCTION
                             PROGRAMME AND BILL OF QUANTITIES

A SCHEDULE SHEET, in the layout and title block of the supplied Revit A2 set
(ARCH001..ARCH005), so that SHEET 13 reads as the next sheet of that series.
By instruction it carries NO CHARTS OR GRAPHS: the programme and the bill are
presented as they are issued, in tables.

    LEFT COLUMN    BILL OF QUANTITIES - MEASURED ITEMS
                   all 38 items under their five part headings
    RIGHT COLUMN   MASTER CONSTRUCTION PROGRAMME
                   COST SUMMARY
                   BILL OF QUANTITIES - PART SUMMARY
                   WHAT THE REVISED BILL CARRIES

WHICH REVISION.  This sheet presents **WM3**, the REVISED owner package of
master H.15, whose final project cost is **Rs 2,97,90,913** and whose programme
is the revised master construction schedule R1: 224 working days, 02-11-26 to
26-07-27.  It is NOT WM4, the later bill priced from the Maharashtra PWD State
Schedule of Rates 2022-23, which is a different total on a different basis.

Every amount, quantity, count, rate, date and duration on this sheet is read at
build time from the WM3 output files under `WORKS MANAGEMENT/`; nothing is
retyped and nothing is re-derived.  One line of the bill carries no rate, so it
is shown as NOT PRICED rather than as a figure this sheet has invented.

COLOUR: dark only, and mostly black.  ACI 7 black and 8 dark grey.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
for _p in ("Structural CAD", "Drainage", "Fire and Life Safety"):
    sys.path.insert(0, os.path.join(ROOT, _p, "Scripts"))

from a2_lib import A2Sheet                                    # noqa: E402
import ops_data as D                                          # noqa: E402

LCOL, LCOL_W = 44.0, 216.0        # the bill, in the drawing region
RCOL, RCOL_W = 282.0, 178.0       # the schedule column
TOP, BOT = 383.0, 35.5

s = A2Sheet(
    sheet_no="SHEET 13",
    drawing_no="WMS013",
    title_lines=["WORKS", "MANAGEMENT -", "MASTER PROGRAMME", "AND BILL OF",
                 "QUANTITIES"],
    project_lines=D.PROJECT_LINES,
    identity=D.IDENTITY,
    notes=[
        "ALL AMOUNTS ARE IN INDIAN RUPEES. ALL DURATIONS ARE IN WORKING DAYS. "
        "ALL DATES ARE dd-mm-yy.",
        "WRITTEN FIGURES TO BE FOLLOWED ONLY.",
        "THIS DRG IS TO BE READ IN CONJUNCTION WITH THE FULL BILL OF "
        "QUANTITIES, THE COST ESTIMATE AND THE MASTER CONSTRUCTION SCHEDULE.",
        f"FINAL PROJECT COST Rs {D.FINAL_COST}, BUILT UP FROM A TOTAL BASIC "
        f"COST OF Rs {D.BASIC_COST} IN 38 MEASURED ITEMS UNDER FIVE PARTS.",
        f"MASTER CONSTRUCTION PROGRAMME {D.PROG_DAYS.upper()}, "
        f"{D.PROG_START} TO {D.PROG_FINISH}, IN FOUR PHASES: INITIAL WORKS, "
        f"SUBSTRUCTURE, SUPERSTRUCTURE AND FINISHING. THE PROGRAMME TABLE "
        f"LISTS THE SUMMARY ACTIVITIES; THE FULL SCHEDULE CARRIES 130.",
        "THE BURSTER SLAB IS 200 THK M30 AND 38.40 CUM. THE SENTRY POST IS "
        "MEASURED AS AN RC FRAME WITH ITS BRICK INFILL MEASURED SEPARATELY "
        "AS BRICKWORK.",
        "THE TWO ESCAPE SHAFT COLLARS, 250 RC AT OD 1900, ARE MEASURED AS A "
        "LINE AT 6.285 CUM, AND THE 15 kVA GENERATOR IS A VISIBLE LINE.",
        "THE CONCRETE TOTAL IS 467.59 CUM, WHICH IS THE SUM OF ITS OWN LINES.",
        "AMOUNTS AND RATES ARE THE BILL'S OWN. A LINE SHOWN NOT PRICED "
        "CARRIES NO RATE IN THE BILL AND IS NOT INCLUDED IN ANY TOTAL ON "
        "THIS SHEET.",
        "ITEM DESCRIPTIONS ARE THE BILL'S OWN, TRIMMED TO THE COLUMN WHERE "
        "MARKED WITH AN ELLIPSIS. THE BILL GOVERNS.",
        "CONTRACTOR TO CHECK AND VERIFY THE FIGURES BEFORE TENDER.",
    ],
    date=D.DATE,
    drawn=D.DRAWN,
    checked=D.CHECKED,
    scale_note="Not to scale",
)

# =====================================================  LEFT COLUMN, THE BILL
yl = s.table_stack(LCOL, TOP, BOT, LCOL_W, [
    dict(rows=D.BOQ_ITEMS,
         title="BILL OF QUANTITIES - MEASURED ITEMS  (REVISED)",
         header=["No.", "ITEM", "UNIT", "QTY", "RATE  Rs", "AMOUNT  Rs"],
         align=["C", "L", "C", "R", "R", "R"], pad=2.2),
], gap=0.0, rh_max=8.0)
assert yl > BOT - 0.6, f"the bill overflows the frame: bottom at {yl:.1f}"

# ================================================  RIGHT COLUMN, THE SCHEDULES
yr = s.table_stack(RCOL, TOP, BOT, RCOL_W, [
    dict(rows=D.PROGRAMME_ROWS, title="MASTER CONSTRUCTION PROGRAMME",
         header=["ID", "ACTIVITY", "DAYS", "START", "FINISH"],
         align=["C", "L", "C", "C", "C"], pad=2.2),
    dict(rows=D.COST_SUMMARY, title="COST SUMMARY",
         header=["COST HEAD", "BASIS", "AMOUNT  Rs"],
         align=["L", "C", "R"], pad=2.2),
    dict(rows=D.PART_SUMMARY, title="BILL OF QUANTITIES - PART SUMMARY",
         header=["PART", "DESCRIPTION", "ITEMS", "AMOUNT  Rs"],
         align=["C", "L", "C", "R"], pad=2.2),
    dict(rows=D.WM3_APPLIED, title="WHAT THE REVISED BILL CARRIES",
         header=["ITEM", "AS MEASURED", "QUANTITY", "NOTES"],
         align=["L", "L", "C", "L"], pad=2.2),
], gap=5.0, rh_max=7.2)
assert yr > BOT - 0.6, f"the schedule stack overflows the frame: bottom at {yr:.1f}"


if __name__ == "__main__":
    out = os.path.join(ROOT, "Presentation Sheets", "DXF",
                       "WMS013_Works_Management_Master_Programme_and_Bill_of_"
                       "Quantities.dxf")
    s.save(out)
    print("written", out, "| bill bottom y =", round(yl, 1),
          "| schedule bottom y =", round(yr, 1))
