"""
wm_programme_pdf.py — the final works programme as an A3 landscape PDF.

Underground CBRN-hardened blast-resistant protective structure + sentry post, Pune.
Works Management package revision WM1.

Sheet 1  Programme basis, key dates and the milestone register
Sheet 2  Summary Gantt — WBS levels 1 and 2 on one page
Sheet 3+ Detailed Gantt — every activity, with the critical path in red

Generated from wm_data.py through wm_schedule.py.  No date on any sheet is
typed by hand.
"""

import os
from datetime import timedelta

from reportlab.lib.pagesizes import A3, landscape
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas as rl_canvas

import wm_data as D
import wm_schedule as S
import wm_mspdi as M

PW, PH = landscape(A3)                      # 1190.5 x 841.9 pt
LM, RM, TM, BM = 14 * mm, 12 * mm, 14 * mm, 12 * mm

COL = [("OUTLINE", 38), ("ID", 34), ("ACTIVITY", 236), ("DUR", 22),
       ("START", 40), ("FINISH", 40), ("TF", 20)]
TBL_W = sum(c[1] for c in COL)
GANTT_X = LM + TBL_W + 6
GANTT_W = PW - RM - GANTT_X

ROW_H = 9.4
HDR_H = 26

CRIT = (0.78, 0.10, 0.10)
NORM = (0.24, 0.42, 0.62)
SUMM = (0.16, 0.18, 0.22)
MSTONE = (0.85, 0.55, 0.05)
GRID = (0.86, 0.86, 0.88)
BAND = (0.955, 0.960, 0.968)


def month_starts(d0, d1):
    out, y, m = [], d0.year, d0.month
    while True:
        from datetime import date
        d = date(y, m, 1)
        if d > d1:
            break
        if d >= d0.replace(day=1):
            out.append(d)
        m += 1
        if m == 13:
            m, y = 1, y + 1
    return out


class Sheet:
    def __init__(self, path, tasks, rows, end):
        self.c = rl_canvas.Canvas(path, pagesize=landscape(A3))
        self.tasks, self.rows, self.end = tasks, rows, end
        self.d0 = S.CAL.day(0)
        self.d1 = S.CAL.day(end)
        self.span = (self.d1 - self.d0).days + 1
        self.page = 0
        self.total_pages = 0

    # ---- helpers ---------------------------------------------------------
    def x_of(self, d):
        return GANTT_X + GANTT_W * ((d - self.d0).days / float(self.span))

    def title_block(self, sheet_no, sheet_title):
        c = self.c
        c.setFillColorRGB(0.10, 0.12, 0.16)
        c.rect(LM, PH - TM - 20, PW - LM - RM, 20, stroke=0, fill=1)
        c.setFillColorRGB(1, 1, 1)
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(LM + 6, PH - TM - 14,
                     "UNDERGROUND CBRN-HARDENED BLAST-RESISTANT PROTECTIVE "
                     "STRUCTURE AND SENTRY POST — PUNE, MAHARASHTRA")
        c.setFont("Helvetica", 8)
        c.drawRightString(PW - RM - 6, PH - TM - 14,
                          "FINAL WORKS PROGRAMME · Rev %s · %s"
                          % (D.REV, D.REV_DATE.strftime("%d.%m.%Y")))
        c.setFillColorRGB(0.20, 0.24, 0.30)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(LM, PH - TM - 32, sheet_title.upper())
        c.setFont("Helvetica", 7)
        c.drawRightString(PW - RM, PH - TM - 32,
                          "Geometry: %s   ·   Sheet %d"
                          % (D.PROJECT["geometry_rev"], sheet_no))
        c.setStrokeColorRGB(0.6, 0.6, 0.65)
        c.setLineWidth(0.4)
        c.line(LM, PH - TM - 36, PW - RM, PH - TM - 36)

    def footer(self, note=""):
        c = self.c
        c.setStrokeColorRGB(0.6, 0.6, 0.65)
        c.setLineWidth(0.4)
        c.line(LM, BM + 12, PW - RM, BM + 12)
        c.setFont("Helvetica", 6.4)
        c.setFillColorRGB(0.35, 0.35, 0.40)
        c.drawString(LM, BM + 4,
                     "Six-day working week (Mon–Sat); Sunday non-working; five "
                     "date-certain national holidays non-working.  Durations in "
                     "working days.  Critical path = total float 0.")
        c.drawRightString(PW - RM, BM + 4, note)

    def timescale(self, y_top, height):
        """Month grid across the Gantt area; returns nothing."""
        c = self.c
        ms = month_starts(self.d0, self.d1)
        c.setFont("Helvetica-Bold", 6.2)
        for i, d in enumerate(ms):
            x = self.x_of(d)
            nxt = ms[i + 1] if i + 1 < len(ms) else self.d1 + timedelta(days=1)
            xn = self.x_of(nxt)
            if i % 2 == 0:
                c.setFillColorRGB(*BAND)
                c.rect(x, y_top - height, xn - x, height, stroke=0, fill=1)
            c.setStrokeColorRGB(*GRID)
            c.setLineWidth(0.35)
            c.line(x, y_top - height, x, y_top)
            c.setFillColorRGB(0.30, 0.32, 0.38)
            if xn - x > 12:
                c.drawCentredString((x + xn) / 2.0, y_top + 3,
                                    d.strftime("%b"))
            if d.month == 1 or i == 0:
                c.setFont("Helvetica-Bold", 6.2)
                c.drawCentredString((x + xn) / 2.0, y_top + 11, d.strftime("%Y"))
                c.setFont("Helvetica-Bold", 6.2)
        c.setStrokeColorRGB(0.45, 0.45, 0.5)
        c.setLineWidth(0.5)
        c.rect(GANTT_X, y_top - height, GANTT_W, height, stroke=1, fill=0)

    def col_header(self, y):
        c = self.c
        x = LM
        c.setFillColorRGB(0.88, 0.90, 0.93)
        c.rect(LM, y - 12, TBL_W, 12, stroke=0, fill=1)
        c.setFillColorRGB(0.15, 0.17, 0.22)
        c.setFont("Helvetica-Bold", 6.2)
        for name, w in COL:
            c.drawString(x + 2, y - 8.5, name)
            x += w
        c.setStrokeColorRGB(*GRID)
        c.setLineWidth(0.35)
        x = LM
        for _, w in COL:
            c.line(x, y - 12, x, y)
            x += w
        c.line(LM, y - 12, LM + TBL_W, y - 12)

    def row(self, r, y, rh=None):
        rh = rh or ROW_H
        c = self.c
        summary = r["kind"] == "summary"
        t = r.get("task")
        ms = (not summary) and t.is_milestone
        crit = (not summary) and t.tf == 0

        if summary:
            c.setFillColorRGB(0.90, 0.92, 0.95) if r["level"] == 1 else \
                c.setFillColorRGB(0.955, 0.965, 0.975)
            c.rect(LM, y - rh + 1.4, TBL_W + 6 + GANTT_W, rh,
                   stroke=0, fill=1)

        # -- text columns
        vals = [r["outline"],
                "" if summary else t.id,
                ("    " * (r["level"] - 1)) + r["name"],
                "" if summary else ("" if ms else str(t.dur)),
                S.dstr(r["es"]),
                S.dstr(r["es"] if ms else r["ef"]),
                "" if summary else str(t.tf)]
        if summary:
            c.setFont("Helvetica-Bold", 6.0 if r["level"] > 1 else 6.4)
            c.setFillColorRGB(*SUMM)
        elif ms:
            c.setFont("Helvetica-Bold", 5.9)
            c.setFillColorRGB(0.55, 0.35, 0.0)
        else:
            c.setFont("Helvetica", 5.9)
            c.setFillColorRGB(*(CRIT if crit else (0.15, 0.15, 0.18)))
        x = LM
        for (name, w), v in zip(COL, vals):
            txt = v
            if name == "ACTIVITY":
                while c.stringWidth(txt, c._fontname, c._fontsize) > w - 4 and len(txt) > 4:
                    txt = txt[:-2]
            if name in ("DUR", "TF"):
                c.drawRightString(x + w - 3, y - rh + 4, txt)
            else:
                c.drawString(x + 2, y - rh + 4, txt)
            x += w

        # -- bar
        bx0, bx1 = self.x_of(S.CAL.day(r["es"])), self.x_of(S.CAL.day(r["ef"]) + timedelta(days=1))
        by = y - rh + 2.6
        h = rh - 4.6
        if ms:
            cx = self.x_of(S.CAL.day(r["es"]))
            s = min(3.4, h * 0.55)
            c.setFillColorRGB(*MSTONE)
            p = c.beginPath()
            p.moveTo(cx, by + h / 2 + s)
            p.lineTo(cx + s, by + h / 2)
            p.lineTo(cx, by + h / 2 - s)
            p.lineTo(cx - s, by + h / 2)
            p.close()
            c.drawPath(p, stroke=0, fill=1)
        elif summary:
            c.setFillColorRGB(*SUMM)
            c.rect(bx0, by + h * 0.30, max(bx1 - bx0, 1.0), max(h * 0.40, 1.8), stroke=0, fill=1)
            for xx in (bx0, bx1):
                p = c.beginPath()
                p.moveTo(xx, by + h * 0.68)
                p.lineTo(xx + (2.4 if xx == bx0 else -2.4), by + h * 0.68)
                p.lineTo(xx, by + h * 0.1)
                p.close()
                c.drawPath(p, stroke=0, fill=1)
        else:
            c.setFillColorRGB(*(CRIT if crit else NORM))
            c.rect(bx0, by, max(bx1 - bx0, 1.0), h, stroke=0, fill=1)
            if t.tf > 0 and t.tf < 400:
                fx = self.x_of(S.CAL.day(min(t.ef + t.tf, self.end)) + timedelta(days=1))
                c.setStrokeColorRGB(0.62, 0.66, 0.72)
                c.setLineWidth(0.35)
                c.setDash(1, 1.6)
                c.line(bx1, by + h / 2, fx, by + h / 2)
                c.setDash()

    # ---- sheets ----------------------------------------------------------
    def sheet_basis(self):
        c = self.c
        self.page += 1
        self.title_block(self.page, "Programme basis, key dates and milestone register")
        y = PH - TM - 52

        def h2(txt, yy):
            c.setFont("Helvetica-Bold", 8)
            c.setFillColorRGB(0.10, 0.30, 0.50)
            c.drawString(LM, yy, txt)
            c.setStrokeColorRGB(0.10, 0.30, 0.50)
            c.setLineWidth(0.5)
            c.line(LM, yy - 2.5, LM + 250, yy - 2.5)

        def kv(k, v, yy, xx=LM, kw=118):
            c.setFont("Helvetica-Bold", 6.8)
            c.setFillColorRGB(0.30, 0.32, 0.38)
            c.drawString(xx, yy, k)
            c.setFont("Helvetica", 6.8)
            c.setFillColorRGB(0.10, 0.10, 0.14)
            c.drawString(xx + kw, yy, v)

        # --- left column: basis
        h2("1  PROGRAMME BASIS", y)
        y -= 12
        for k, v in [
            ("Project", D.PROJECT["title"]),
            ("Location", D.PROJECT["location"]),
            ("Design basis", D.PROJECT["geometry_rev"]),
            ("Services packages", D.PROJECT["services_rev"]),
            ("Programme revision", "WM1 — the R0 master construction schedule, rebuilt"),
            ("Data date / start", S.CAL.day(0).strftime("%A %d %B %Y")),
            ("Completion", S.CAL.day(self.end).strftime("%A %d %B %Y")),
            ("Duration", "%d working days  (%d calendar days, %.1f months)"
             % (self.end + 1, self.span, self.span / 30.44)),
            ("Activities", "%d, of which %d milestones, in a %d-level WBS"
             % (len(self.tasks),
                sum(1 for t in self.tasks.values() if t.is_milestone), 3)),
            ("Logic links", "%d finish-to-start, start-to-start, finish-to-finish "
             "and finish-to-finish links with lags"
             % sum(len(t.preds) for t in self.tasks.values())),
            ("Critical activities", "%d activities at total float 0"
             % sum(1 for t in self.tasks.values() if t.tf == 0)),
            ("Calendar", "Six-day week, Mon–Sat, 08:00–17:00 with a one-hour break"),
        ]:
            kv(k, v, y)
            y -= 9.4
        y -= 4
        c.setFont("Helvetica", 6.4)
        c.setFillColorRGB(0.30, 0.30, 0.36)
        tw = c.beginText(LM, y)
        for ln in _wrap(D.CALENDAR_NOTE, 150):
            tw.textLine(ln)
            y -= 8
        c.drawText(tw)

        y -= 8
        h2("2  THE SIX DECISIONS THAT SHAPE THIS PROGRAMME", y)
        y -= 12
        for n, txt in enumerate([
            "Blast doors are ordered on day 1.  The cast-in frames must be welded "
            "into the W6 and W7 cages before those walls are poured, so a 75-day "
            "frame lead time sits directly upstream of the wall concrete.",
            "The pressure slab props stay for 14 days.  IS 456 Table 11 requires "
            "14 days for props to a slab spanning over 4.5 m; this one spans "
            "5.000 m clear.  Fourteen days of curing plus five of striking sit "
            "on the critical path and cannot be compressed.",
            "The roof is cast before the walls are backfilled.  Backfilling "
            "against a 3.2 m unpropped wall is what the 15.41 kPa/m lateral "
            "gradient forbids; the roof provides the prop.",
            "The engineered cover is a six-layer structure, not a fill operation. "
            "It contains a 200 mm M30 burster slab that must be formed, "
            "reinforced, poured and cured inside the cover.",
            "The sentry post starts only after the rock breaking finishes.  No "
            "green concrete stands within 10 m of a hydraulic breaker, and the "
            "post carries 118 days of float, which makes it the natural place to "
            "absorb delay and redeploy labour.",
            "Nothing is programmed against a fabricated festival-holiday date. "
            "The calendar carries only date-certain national holidays; a 10-day "
            "contingency activity before handover absorbs the movable ones.",
        ], 1):
            c.setFont("Helvetica-Bold", 6.6)
            c.setFillColorRGB(0.10, 0.30, 0.50)
            c.drawString(LM, y, "%d" % n)
            c.setFont("Helvetica", 6.4)
            c.setFillColorRGB(0.15, 0.15, 0.18)
            for ln in _wrap(txt, 118):
                c.drawString(LM + 10, y, ln)
                y -= 7.6
            y -= 2.6

        # --- right column: milestones
        xr = LM + 470
        y2 = PH - TM - 52
        h2c = xr
        c.setFont("Helvetica-Bold", 8)
        c.setFillColorRGB(0.10, 0.30, 0.50)
        c.drawString(h2c, y2, "3  MILESTONE REGISTER")
        c.setStrokeColorRGB(0.10, 0.30, 0.50)
        c.line(h2c, y2 - 2.5, h2c + 250, y2 - 2.5)
        y2 -= 14
        c.setFillColorRGB(0.88, 0.90, 0.93)
        c.rect(xr, y2 - 2, 600, 11, stroke=0, fill=1)
        c.setFillColorRGB(0.15, 0.17, 0.22)
        c.setFont("Helvetica-Bold", 6.2)
        for lbl, dx in (("REF", 0), ("ACT", 26), ("MILESTONE", 62),
                        ("DATE", 400), ("FLOAT", 452), ("STATUS", 500)):
            c.drawString(xr + dx, y2 + 1.5, lbl)
        y2 -= 11
        for mid, aid, name in D.MILESTONES:
            t = self.tasks[aid]
            crit = t.tf == 0
            c.setFont("Helvetica-Bold" if crit else "Helvetica", 6.2)
            c.setFillColorRGB(*(CRIT if crit else (0.15, 0.15, 0.18)))
            c.drawString(xr, y2, mid)
            c.drawString(xr + 26, y2, aid)
            c.drawString(xr + 62, y2, name[:82])
            c.drawString(xr + 400, y2, S.CAL.day(t.es).strftime("%d %b %y"))
            c.drawRightString(xr + 484, y2, "%d d" % t.tf)
            c.drawString(xr + 500, y2, "CRITICAL" if crit else "")
            y2 -= 9.2

        y2 -= 8
        c.setFont("Helvetica-Bold", 8)
        c.setFillColorRGB(0.10, 0.30, 0.50)
        c.drawString(xr, y2, "4  CRITICAL PATH — THE CONTROLLING CHAIN")
        c.line(xr, y2 - 2.5, xr + 250, y2 - 2.5)
        y2 -= 13
        c.setFont("Helvetica", 6.3)
        c.setFillColorRGB(0.15, 0.15, 0.18)
        chain = sorted((t for t in self.tasks.values() if t.tf == 0),
                       key=lambda x: (x.es, x.uid))
        groups, seen = [], set()
        for t in chain:
            top = t.wbs.split(".")[0]
            if top not in seen:
                seen.add(top)
                groups.append((top, t))
        wbsname = dict(D.WBS)
        for top, t in groups:
            c.setFont("Helvetica-Bold", 6.3)
            c.setFillColorRGB(*CRIT)
            c.drawString(xr, y2, "%s" % top)
            c.setFont("Helvetica", 6.3)
            c.setFillColorRGB(0.15, 0.15, 0.18)
            c.drawString(xr + 16, y2, "%s — enters the path at %s on %s"
                         % (wbsname[top][:56], t.id, S.CAL.day(t.es).strftime("%d %b %y")))
            y2 -= 8.4

        y2 -= 6
        c.setFont("Helvetica-Oblique", 6.2)
        c.setFillColorRGB(0.35, 0.35, 0.40)
        for ln in _wrap(
            "The controlling chain is: site possession and the confirmatory site "
            "investigation, which must close the ASSUMED groundwater level before "
            "the excavation support can be designed; rock excavation; formation "
            "approval; the external tanking; the mat; the perimeter and protective "
            "walls; the pressure slab with its 14-day prop period; the roof "
            "membrane; the six-layer engineered cover including the burster slab; "
            "the external works and concealment; and finally snagging, "
            "rectification and handover.  Every one of the eighteen milestones is "
            "either on that chain or hangs from it.", 150):
            c.drawString(xr, y2, ln)
            y2 -= 7.6

        # --- lower band: assumptions, resources, file format
        ylo = min(y, y2) - 16
        c.setFont("Helvetica-Bold", 8)
        c.setFillColorRGB(0.10, 0.30, 0.50)
        c.drawString(LM, ylo, "5  WHAT THIS PROGRAMME ASSUMES, AND WHAT MUST BE "
                              "CONFIRMED BEFORE IT CAN BE RELIED ON")
        c.setStrokeColorRGB(0.10, 0.30, 0.50)
        c.line(LM, ylo - 2.5, LM + 420, ylo - 2.5)
        ylo -= 13
        ya = ylo
        for ref, txt in PROG_ASSUMPTIONS:
            c.setFont("Helvetica-Bold", 6.3)
            c.setFillColorRGB(0.55, 0.20, 0.10)
            c.drawString(LM, ya, ref)
            c.setFont("Helvetica", 6.3)
            c.setFillColorRGB(0.15, 0.15, 0.18)
            for ln in _wrap(txt, 105):
                c.drawString(LM + 34, ya, ln)
                ya -= 7.4
            ya -= 1.6

        xr2 = LM + 470
        yb = ylo
        c.setFont("Helvetica-Bold", 8)
        c.setFillColorRGB(0.10, 0.30, 0.50)
        c.drawString(xr2, yb + 13, "6  PEAK RESOURCE REQUIREMENT AND FILE FORMAT")
        c.setStrokeColorRGB(0.10, 0.30, 0.50)
        c.line(xr2, yb + 10.5, xr2 + 300, yb + 10.5)
        c.setFillColorRGB(0.88, 0.90, 0.93)
        c.rect(xr2, yb - 2, 600, 10, stroke=0, fill=1)
        c.setFillColorRGB(0.15, 0.17, 0.22)
        c.setFont("Helvetica-Bold", 6.2)
        for lbl, dx in (("GROUP", 0), ("RESOURCE", 46), ("COMPOSITION", 180),
                        ("PEAK", 320), ("DRIVEN BY", 350)):
            c.drawString(xr2 + dx, yb + 0.8, lbl)
        yb -= 10
        for name, group, comp, peak, note in D.RESOURCES:
            if group == "Staff":
                continue
            c.setFont("Helvetica", 6.1)
            c.setFillColorRGB(0.15, 0.15, 0.18)
            c.drawString(xr2, yb, group)
            c.drawString(xr2 + 46, yb, name[:38])
            c.drawString(xr2 + 180, yb, comp[:34])
            c.drawRightString(xr2 + 340, yb, str(peak))
            c.drawString(xr2 + 350, yb, note[:64])
            yb -= 7.4
        yb -= 6
        c.setFont("Helvetica-Bold", 6.4)
        c.setFillColorRGB(0.55, 0.20, 0.10)
        c.drawString(xr2, yb, "PROGRAMME FILE FORMAT")
        yb -= 8
        c.setFont("Helvetica", 6.2)
        c.setFillColorRGB(0.15, 0.15, 0.18)
        for ln in _wrap(
            "The editable master programme accompanying this PDF is "
            "Underground_Shelter_Final_Works_Programme.xml, written in MSPDI — "
            "Microsoft Project's own published XML schema.  Microsoft Project "
            "opens it directly and File > Save As > Project (*.mpp) produces the "
            "binary .mpp.  The native .mpp format is undocumented and can only be "
            "written by Microsoft Project itself, so it is not produced here "
            "rather than being imitated.  The XML carries the full WBS, all 279 "
            "activities, all 404 logic links with their lags, the six-day "
            "calendar with its exceptions, 33 resources and 426 assignments; it "
            "was verified by reading it back with MPXJ and comparing every date "
            "against the critical-path calculation.", 118):
            c.drawString(xr2, yb, ln)
            yb -= 7.4

        self.footer("Sheet 1 of %d" % self.total_pages)
        c.showPage()

    def sheet_summary_gantt(self):
        c = self.c
        self.page += 1
        self.title_block(self.page, "Summary programme — WBS levels 1 and 2")
        rows = [r for r in self.rows if r["kind"] == "summary"]
        y_top = PH - TM - 56
        avail = y_top - (BM + 30)
        rh = min(14.0, avail / float(len(rows)))
        h = len(rows) * rh + 4
        self.timescale(y_top, h)
        self.col_header(y_top + 14)
        y = y_top
        for r in rows:
            self.row(dict(r), y, rh)
            y -= rh
        self.legend(y - 12)
        self.footer("Sheet 2 of %d" % self.total_pages)
        c.showPage()

    def legend(self, y):
        c = self.c
        c.setFont("Helvetica-Bold", 6.4)
        c.setFillColorRGB(0.15, 0.17, 0.22)
        c.drawString(LM, y, "LEGEND")
        x = LM + 42
        items = [(SUMM, "WBS summary"), (NORM, "Activity"), (CRIT, "Critical (TF = 0)"),
                 (MSTONE, "Milestone")]
        for col, lbl in items:
            c.setFillColorRGB(*col)
            c.rect(x, y - 1, 14, 5, stroke=0, fill=1)
            c.setFillColorRGB(0.15, 0.17, 0.22)
            c.setFont("Helvetica", 6.2)
            c.drawString(x + 18, y, lbl)
            x += 18 + c.stringWidth(lbl, "Helvetica", 6.2) + 16
        c.setStrokeColorRGB(0.62, 0.66, 0.72)
        c.setLineWidth(0.4)
        c.setDash(1, 1.6)
        c.line(x, y + 1.5, x + 14, y + 1.5)
        c.setDash()
        c.setFillColorRGB(0.15, 0.17, 0.22)
        c.drawString(x + 18, y, "Total float")

    def sheet_detail(self, chunk, n, total):
        c = self.c
        self.page += 1
        self.title_block(self.page, "Detailed works programme (%d of %d)" % (n, total))
        y_top = PH - TM - 56
        h = len(chunk) * ROW_H + 4
        self.timescale(y_top, h)
        self.col_header(y_top + 14)
        y = y_top
        for r in chunk:
            self.row(r, y)
            y -= ROW_H
        self.legend(y - 12)
        self.footer("Sheet %d of %d" % (self.page, self.total_pages))
        c.showPage()

    def build(self):
        rows_per_page = int((PH - TM - BM - 96) / ROW_H)
        detail = self.rows
        chunks = [detail[i:i + rows_per_page]
                  for i in range(0, len(detail), rows_per_page)]
        self.total_pages = 2 + len(chunks)
        self.sheet_basis()
        self.sheet_summary_gantt()
        for i, ch in enumerate(chunks, 1):
            self.sheet_detail(ch, i, len(chunks))
        self.c.save()
        return self.total_pages


PROG_ASSUMPTIONS = [
    ("WM-P1", "Project start Monday 2 November 2026 is carried over from the "
     "supplied R0 master construction schedule.  It is a planning date, not a "
     "contractual one."),
    ("WM-P2", "Durations are built from the quantities derived in the BOQ and "
     "from output rates typical of Indian sites; they are ASSUMED and must be "
     "re-tested against the appointed contractor's resources."),
    ("WM-P3", "The rockhead is ASSUMED in the master at (-)1.500 to (-)2.000. "
     "Rock excavation is programmed at the mean, 994 m3.  At the shallow bound "
     "it rises to 1043 m3 and the excavation lengthens by about a day."),
    ("WM-P4", "The design groundwater table (-)2.000 is ASSUMED.  A1080 puts "
     "monsoon monitoring on the critical path deliberately: if the water is "
     "higher, the dewatering, the tanking and the flotation check all change."),
    ("WM-P5", "No blasting is assumed.  Rock is removed by hydraulic breaker "
     "because the sentry post founds on the same rock within 10 m."),
    ("WM-P6", "Vendor lead times for the blast doors, filter trains, blast "
     "valves and the EMP enclosure are ASSUMED.  They are the longest single "
     "risk in the programme and must be replaced by quoted times at tender."),
    ("WM-P7", "Festival holidays are not in the calendar; A14098 carries ten "
     "working days of contingency in their place."),
    ("WM-P8", "The berm, the access route and the concealment works have no "
     "site plan behind them, so their durations are indicative only."),
]


def _wrap(text, n):
    words, out, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > n:
            out.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        out.append(cur)
    return out


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "..", "Programme")
    tasks, order, end, _ = S.summary()
    rows = M.outline_numbers(M.build_outline(tasks))
    path = os.path.join(out, "Underground_Shelter_Final_Works_Programme.pdf")
    n = Sheet(path, tasks, rows, end).build()
    print("programme PDF written: %d sheets" % n)


if __name__ == "__main__":
    main()
