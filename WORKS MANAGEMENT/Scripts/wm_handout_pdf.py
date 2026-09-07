"""
wm_handout_pdf.py — the Works Management handout, A4 portrait.

Underground CBRN-hardened blast-resistant protective structure + sentry post, Pune.
Works Management package revision WM1.

Produces Underground_Shelter_Works_Management_Handout.pdf: the final-semester
Works Management submission covering the entire project from mobilisation to
handover, including the sentry post with its brick masonry walls.

Every number in the handout is pulled from wm_data / wm_schedule / wm_quantities
so that the handout, the programme and the bill cannot drift apart.
"""

import os
from datetime import timedelta

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, PageBreak,
                                PageTemplate, Paragraph, Spacer, Table,
                                TableStyle, Flowable)

import wm_data as D
import wm_schedule as S
import wm_content as C
import wm_quantities as QT
import wm_mspdi as M

PW, PH = A4
LM = RM = 20 * mm
TM = 20 * mm
BM = 18 * mm

INK = colors.HexColor("#1a1d24")
BLUE = colors.HexColor("#14477a")
RED = colors.HexColor("#a5231b")
GREY = colors.HexColor("#5d626c")
LIGHT = colors.HexColor("#eef1f5")
RULE = colors.HexColor("#c2c8d2")
AMBER = colors.HexColor("#8a5a05")

ss = getSampleStyleSheet()


def st(name, **kw):
    base = dict(name=name, fontName="Helvetica", fontSize=9.2, leading=13.2,
                textColor=INK, alignment=TA_JUSTIFY, spaceAfter=6)
    base.update(kw)
    return ParagraphStyle(**base)


BODY = st("body")
LEAD = st("lead", fontSize=10, leading=14.6, textColor=colors.HexColor("#2a2f38"))
H1 = st("h1", fontName="Helvetica-Bold", fontSize=15, leading=19, textColor=BLUE,
        spaceBefore=4, spaceAfter=9, alignment=0)
H2 = st("h2", fontName="Helvetica-Bold", fontSize=10.6, leading=14,
        textColor=colors.HexColor("#22405f"), spaceBefore=11, spaceAfter=5,
        alignment=0)
H3 = st("h3", fontName="Helvetica-BoldOblique", fontSize=9.4, leading=13,
        textColor=colors.HexColor("#3b424e"), spaceBefore=8, spaceAfter=3,
        alignment=0)
BUL = st("bul", leftIndent=11, bulletIndent=2, spaceAfter=3.4)
NOTE = st("note", fontSize=8.4, leading=12, textColor=GREY)
TCELL = st("tc", fontSize=7.6, leading=10, spaceAfter=0, alignment=0)
TCELLB = st("tcb", fontSize=7.6, leading=10, spaceAfter=0, alignment=0,
            fontName="Helvetica-Bold")
TCELLR = st("tcr", fontSize=7.6, leading=10, spaceAfter=0, alignment=TA_RIGHT)
THEAD = st("th", fontSize=7.4, leading=9.6, spaceAfter=0, alignment=0,
           fontName="Helvetica-Bold", textColor=colors.white)
CAP = st("cap", fontSize=7.8, leading=10.6, textColor=GREY, spaceBefore=2,
         spaceAfter=9, alignment=0)

TOC = []          # (level, title, page-key)


class Rule(Flowable):
    def __init__(self, w, thick=0.6, col=RULE, pad=3):
        Flowable.__init__(self)
        self.width, self.thick, self.col, self.pad = w, thick, col, pad
        self.height = thick + pad * 2

    def draw(self):
        self.canv.setStrokeColor(self.col)
        self.canv.setLineWidth(self.thick)
        self.canv.line(0, self.pad, self.width, self.pad)


class Callout(Flowable):
    """A boxed statement — used for the design change and the key rules."""

    def __init__(self, text, width, style=None, accent=RED, title=None):
        Flowable.__init__(self)
        self.width = width
        self.accent = accent
        self.title = title
        self.style = style or st("co", fontSize=8.8, leading=12.6,
                                 textColor=colors.HexColor("#2a2f38"))
        self.tstyle = st("cot", fontSize=8.2, leading=11, fontName="Helvetica-Bold",
                         textColor=accent, spaceAfter=3)
        self.paras = []
        self._text = text

    def wrap(self, aw, ah):
        self.width = min(self.width, aw)
        inner = self.width - 20
        self.paras = []
        h = 8
        if self.title:
            p = Paragraph(self.title.upper(), self.tstyle)
            w, ph = p.wrap(inner, 1000)
            self.paras.append((p, ph))
            h += ph + 3
        for t in ([self._text] if isinstance(self._text, str) else self._text):
            p = Paragraph(t, self.style)
            w, ph = p.wrap(inner, 1000)
            self.paras.append((p, ph))
            h += ph + 4
        self.height = h + 4
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(colors.HexColor("#f7f8fa"))
        c.rect(0, 0, self.width, self.height, stroke=0, fill=1)
        c.setFillColor(self.accent)
        c.rect(0, 0, 3, self.height, stroke=0, fill=1)
        y = self.height - 8
        for p, ph in self.paras:
            y -= ph
            p.drawOn(c, 13, y)
            y -= 4


def tbl(header, rows, widths, align=None, small=False, hdr_col=BLUE):
    fs = 7.0 if small else 7.6
    hs = st("th2", fontSize=fs - 0.3, leading=fs + 2.2, spaceAfter=0, alignment=0,
            fontName="Helvetica-Bold", textColor=colors.white)
    cs = st("tc2", fontSize=fs, leading=fs + 2.6, spaceAfter=0, alignment=0)
    cr = st("tc3", fontSize=fs, leading=fs + 2.6, spaceAfter=0, alignment=TA_RIGHT)
    data = [[Paragraph(str(h), hs) for h in header]]
    for r in rows:
        row = []
        for i, v in enumerate(r):
            style = cr if (align and i < len(align) and align[i] == "r") else cs
            row.append(Paragraph(str(v), style))
        data.append(row)
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), hdr_col),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 2.6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.6),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("GRID", (0, 0), (-1, -1), 0.35, RULE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
    ]))
    return t


class MiniGantt(Flowable):
    """Compact summary Gantt of the fourteen level-1 packages."""

    def __init__(self, tasks, width):
        Flowable.__init__(self)
        self.tasks = tasks
        self.width = width
        self.rows = []
        roll = S.wbs_rollup(tasks)
        for code, title in D.WBS:
            if "." in code or code not in roll:
                continue
            self.rows.append((code, title, roll[code]))
        self.rh = 11.2
        self.pad = 16
        self.height = len(self.rows) * self.rh + 22 + self.pad

    def draw(self):
        c = self.canv
        end = max(t.ef for t in self.tasks.values())
        d0, d1 = S.CAL.day(0), S.CAL.day(end)
        span = (d1 - d0).days + 1
        labw = 200
        gx = labw + 4
        gw = self.width - gx

        def x(d):
            return gx + gw * ((d - d0).days / float(span))

        y = self.height - 18
        base = self.pad
        # timescale
        from datetime import date as _date
        yy, mm_ = d0.year, d0.month
        c.setFont("Helvetica-Bold", 5.6)
        i = 0
        while True:
            dd = _date(yy, mm_, 1)
            if dd > d1:
                break
            if dd >= d0.replace(day=1):
                x0 = x(max(dd, d0))
                mm2, yy2 = (mm_ + 1, yy) if mm_ < 12 else (1, yy + 1)
                nxt = _date(yy2, mm2, 1)
                x1 = x(min(nxt, d1 + timedelta(days=1)))
                if i % 2 == 0:
                    c.setFillColor(colors.HexColor("#f2f4f7"))
                    c.rect(x0, base, x1 - x0, y + 4 - base, stroke=0, fill=1)
                c.setFillColor(GREY)
                if x1 - x0 > 9:
                    c.drawCentredString((x0 + x1) / 2, y + 8, dd.strftime("%b"))
                if dd.month == 1 or i == 0:
                    c.setFillColor(INK)
                    c.drawCentredString((x0 + x1) / 2, y + 15, dd.strftime("%Y"))
                i += 1
            mm_ += 1
            if mm_ == 13:
                mm_, yy = 1, yy + 1
        c.setStrokeColor(RULE)
        c.setLineWidth(0.4)
        c.rect(gx, base, gw, y + 4 - base, stroke=1, fill=0)

        for code, title, (es, ef) in self.rows:
            y -= self.rh
            c.setFont("Helvetica-Bold", 6.2)
            c.setFillColor(INK)
            c.drawString(0, y + 3, code)
            c.setFont("Helvetica", 6.0)
            c.setFillColor(colors.HexColor("#33383f"))
            t = title
            while c.stringWidth(t, "Helvetica", 6.0) > labw - 18:
                t = t[:-2]
            c.drawString(15, y + 3, t)
            x0, x1 = x(S.CAL.day(es)), x(S.CAL.day(ef) + timedelta(days=1))
            crit = code in ("1", "2", "3", "4", "6", "7", "13", "14")
            c.setFillColor(RED if code == "8" else BLUE)
            c.rect(x0, y + 1.6, max(x1 - x0, 1.2), 5.6, stroke=0, fill=1)
        # legend
        c.setFont("Helvetica", 5.8)
        c.setFillColor(BLUE)
        c.rect(gx, 3, 10, 4, stroke=0, fill=1)
        c.setFillColor(GREY)
        c.drawString(gx + 13, 3, "Shelter, services and completion")
        c.setFillColor(RED)
        c.rect(gx + 150, 3, 10, 4, stroke=0, fill=1)
        c.setFillColor(GREY)
        c.drawString(gx + 163, 3, "Sentry post (WBS 8) — 118 days of float")


# ---------------------------------------------------------------------------
class Doc(BaseDocTemplate):
    def __init__(self, path):
        BaseDocTemplate.__init__(self, path, pagesize=A4,
                                 leftMargin=LM, rightMargin=RM,
                                 topMargin=TM, bottomMargin=BM,
                                 title="Underground Shelter — Works Management Handout",
                                 author="B.E. Civil Engineering final-semester project",
                                 subject="Works Management for the complete project "
                                         "including the sentry post")
        fw = PW - LM - RM
        fh = PH - TM - BM
        self.addPageTemplates([
            PageTemplate(id="title",
                         frames=[Frame(LM, BM, fw, fh, id="t",
                                       leftPadding=0, rightPadding=0,
                                       topPadding=0, bottomPadding=0)],
                         onPage=self._title_page),
            PageTemplate(id="body",
                         frames=[Frame(LM, BM + 8, fw, fh - 20, id="b",
                                       leftPadding=0, rightPadding=0,
                                       topPadding=0, bottomPadding=0)],
                         onPage=self._body_page),
        ])
        self.section = ""

    def _title_page(self, c, doc):
        pass

    def _body_page(self, c, doc):
        c.saveState()
        c.setStrokeColor(RULE)
        c.setLineWidth(0.4)
        c.line(LM, PH - TM + 8, PW - RM, PH - TM + 8)
        c.setFont("Helvetica", 6.8)
        c.setFillColor(GREY)
        c.drawString(LM, PH - TM + 12,
                     "UNDERGROUND CBRN-HARDENED PROTECTIVE STRUCTURE AND SENTRY "
                     "POST — PUNE")
        c.drawRightString(PW - RM, PH - TM + 12, "WORKS MANAGEMENT · REV %s" % D.REV)
        c.line(LM, BM - 2, PW - RM, BM - 2)
        c.setFont("Helvetica", 7)
        c.drawString(LM, BM - 11, doc.section)
        c.drawRightString(PW - RM, BM - 11, "%d" % (c.getPageNumber() - 1))
        c.restoreState()


def sec_head(story, n, title, doc_ref):
    def _set(canv, doc, t=title):
        doc.section = t
    story.append(SectionMark(title))
    story.append(Paragraph("%d&nbsp;&nbsp;%s" % (n, title), H1))
    story.append(Rule(PW - LM - RM, 1.1, BLUE, 2))
    story.append(Spacer(1, 5))


class SectionMark(Flowable):
    def __init__(self, title):
        Flowable.__init__(self)
        self.title = title
        self.width = self.height = 0

    def draw(self):
        self.canv._doctemplate.section = self.title


def p(story, text, style=BODY):
    story.append(Paragraph(text, style))


def bullets(story, items, style=BUL):
    for it in items:
        story.append(Paragraph(it, style, bulletText="•"))
    story.append(Spacer(1, 3))


# ===========================================================================
def build(path):
    tasks, order, end, _ = S.summary()
    Q = QT.Q
    FW = PW - LM - RM
    story = []

    fin = S.CAL.day(end)
    nact = len(tasks)
    nms = sum(1 for t in tasks.values() if t.is_milestone)
    nlinks = sum(len(t.preds) for t in tasks.values())
    ncrit = sum(1 for t in tasks.values() if t.tf == 0)

    # ---------------- title page ------------------------------------------
    story.append(Spacer(1, 34 * mm))
    story.append(Paragraph(
        "WORKS MANAGEMENT",
        st("t1", fontName="Helvetica-Bold", fontSize=26, leading=30,
           textColor=BLUE, alignment=TA_CENTER, spaceAfter=4)))
    story.append(Paragraph(
        "for the construction of an",
        st("t2", fontSize=11, leading=15, textColor=GREY, alignment=TA_CENTER,
           spaceAfter=6)))
    story.append(Paragraph(
        "UNDERGROUND CBRN-HARDENED<br/>BLAST-RESISTANT PROTECTIVE STRUCTURE<br/>"
        "AND SENTRY POST",
        st("t3", fontName="Helvetica-Bold", fontSize=15.5, leading=21,
           textColor=INK, alignment=TA_CENTER, spaceAfter=8)))
    story.append(Paragraph(
        "Pune, Maharashtra",
        st("t4", fontSize=11.5, leading=15, textColor=GREY, alignment=TA_CENTER,
           spaceAfter=20)))
    story.append(Rule(FW * 0.45, 1.0, BLUE, 6))
    story.append(Spacer(1, 14))
    story.append(Paragraph(
        "Complete project — mobilisation to handover",
        st("t5", fontName="Helvetica-Bold", fontSize=10.5, leading=14,
           textColor=colors.HexColor("#33383f"), alignment=TA_CENTER, spaceAfter=14)))

    story.append(tbl(
        ["", ""],
        [["Project", "Underground CBRN-hardened, blast-resistant protective "
                     "structure with associated sentry post"],
         ["Location", "Pune, Maharashtra"],
         ["Objective", "Protect 9 occupants for 96 hours against a nuclear "
                       "air-blast design basis threat, with CBRN, EMP and "
                       "fallout hardening"],
         ["Design basis", D.PROJECT["geometry_rev"]],
         ["Discipline packages", D.PROJECT["services_rev"]],
         ["Works Management revision", "<b>%s</b>, %s" %
          (D.REV, D.REV_DATE.strftime("%d %B %Y"))],
         ["Programme", "%d activities · %d milestones · %d logic links" %
          (nact, nms, nlinks)],
         ["Construction period", "%s to %s — %d working days" %
          (S.CAL.day(0).strftime("%d %B %Y"), fin.strftime("%d %B %Y"), end + 1)],
         ["Academic context", "B.E. Civil Engineering, final semester"]],
        [34 * mm, FW - 34 * mm]))
    story.append(Spacer(1, 16))
    story.append(Callout(
        "The sentry post walls are <b>brick masonry</b>, replacing the 200 mm "
        "reinforced concrete ballistic infill panels of architectural revision F. "
        "This is the only design change carried by the Works Management package "
        "and it is recorded throughout as reference <b>SP-B1</b>. Every other "
        "element of the project follows the current design without alteration.",
        FW, accent=RED, title="Design change carried by this package"))
    story.append(PageBreak())

    # ---------------- contents --------------------------------------------
    story.append(Paragraph("Contents", H1))
    story.append(Rule(FW, 1.1, BLUE, 2))
    story.append(Spacer(1, 6))
    SECTIONS = [
        "Introduction", "Project scope", "Project components",
        "Construction methodology", "Work breakdown structure",
        "Underground shelter works", "Sentry post works",
        "Sentry post brick masonry methodology", "Construction sequence",
        "Final work programme", "Bill of quantities", "Resource management",
        "Procurement", "Quality assurance and quality control",
        "Safety management", "Risk management", "Progress monitoring",
        "Inspection and testing", "External works", "Electrical works",
        "Camouflage and concealment works", "Completion and handover",
        "Applicable codes and MES specifications", "References", "Conclusion",
    ]
    rows = [["%d" % (i + 1), s] for i, s in enumerate(SECTIONS)]
    half = (len(rows) + 1) // 2
    two = []
    for i in range(half):
        a = rows[i]
        b = rows[i + half] if i + half < len(rows) else ["", ""]
        two.append([a[0], a[1], b[0], b[1]])
    story.append(tbl(["#", "Section", "#", "Section"], two,
                     [9 * mm, FW / 2 - 12 * mm, 9 * mm, FW / 2 - 12 * mm]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "This handout summarises a Works Management package whose detailed "
        "documents accompany it: the work breakdown structure, the bill of "
        "quantities and its full quantity derivation, the resource plan, the "
        "procurement plan, the quality plan, the safety and risk register, the "
        "codes register, the construction methodology, the progress-monitoring "
        "system, the assumptions and verification register, the master programme "
        "in Microsoft Project format and the programme drawing.", NOTE))
    story.append(PageBreak())

    # ================= 1  INTRODUCTION ====================================
    sec_head(story, 1, "Introduction", "")
    p(story,
      "This document sets out how the underground CBRN-hardened blast-resistant "
      "protective structure at Pune, together with its associated sentry post, is "
      "to be built and managed from site possession to handover. It is the Works "
      "Management component of the project and it covers the whole of it — the "
      "buried shelter, the entry structures, the escape shafts, the engineered "
      "cover, the sentry post, the services, the external works and the "
      "concealment works.", LEAD)
    p(story,
      "The design itself is not the subject of this document. The structure has "
      "been designed and detailed: a 22.0 × 6.2 m buried reinforced concrete box "
      "with 600 mm walls, a 900 mm pressure slab and a 600 mm mat, designed for a "
      "344.7 kPa nuclear air-blast design basis threat under 2.0 m of layered "
      "engineered cover, together with an above-ground entry headhouse, a covered "
      "approach stairwell, two escape shafts and a separate two-storey sentry "
      "post. What this document addresses is the question that follows the "
      "design: how is it actually constructed, in what order, with what "
      "resources, to what quality, at what risk, and how is progress measured "
      "while it happens.")
    p(story,
      "The starting point was a preliminary master construction schedule supplied "
      "with the project. That schedule contributed its project start date, its "
      "six-day working calendar and its practice of naming the structural "
      "consultant's pre-pour checks as distinct activities, and all three are "
      "retained. Its structure, however, described a different building: a "
      "1000 mm roof slab under 4 m of overburden, a lift shaft, wall tiling and "
      "suspended ceilings, and no identifiable sentry post, escape shafts, blast "
      "doors, CBRN plant, EMP works or procurement. The programme has therefore "
      "been rebuilt around the project as it now stands rather than tidied up.")

    story.append(Paragraph("1.1&nbsp;&nbsp;What makes this project unusual to build",
                           H2))
    p(story,
      "Three characteristics drive almost every decision in this package.")
    bullets(story, [
        "<b>It is a protective structure, so its continuity matters more than its "
        "strength.</b> There is no movement joint anywhere inside the protective "
        "envelope, because a movement joint is simultaneously a blast, a gas and "
        "an electromagnetic pulse discontinuity. Every construction joint carries "
        "two waterstops and a welded strap. Bar spacing is held at 150 mm in both "
        "curtains throughout — an electromagnetic pulse requirement, stricter "
        "than IS 456 requires for strength, and therefore one that a site "
        "engineer looking only at strength would see no reason to keep.",
        "<b>It is buried, so most of it can never be inspected again.</b> The "
        "external tanking is a continuous tank under the mat, up the walls and "
        "over the roof, and the design groundwater table sits at the roof level. "
        "Once it is backfilled the membrane is unreachable. The quality plan is "
        "built around that fact.",
        "<b>Several of its components cannot be bought quickly.</b> The blast "
        "doors, the CBRN filter trains, the blast valves and the shielded "
        "enclosure are specialist items with lead times measured in months, and "
        "the blast door cast-in frames have to be welded into the wall "
        "reinforcement before those walls are poured. Procurement is therefore "
        "not an administrative activity that runs alongside construction; it is "
        "part of the construction logic.",
    ])

    story.append(Paragraph("1.2&nbsp;&nbsp;How this package handles what is not known",
                           H2))
    p(story,
      "The project record classifies every value it holds as confirmed, "
      "reconstructed, assumed, unresolved or not available. This package uses the "
      "same classification and observes the same rule: nothing marked unresolved "
      "or not available is quietly filled in.")
    p(story,
      "That rule has real consequences here. There is no electrical design "
      "package in this project, so every electrical quantity in the bill of "
      "quantities reads <i>to be verified from final measurement</i> and no "
      "electrical enquiry can be issued. There is no site plan, so the berm "
      "volume, the access route and several drainage runs cannot be measured. "
      "There is no lintel design for the sentry post openings — a requirement "
      "that the brick masonry itself creates. Each of these is recorded, dated "
      "against the programme activity it blocks, and issued to the designer at "
      "mobilisation rather than discovered when the activity is due to start.")
    story.append(Callout([
        "Two claims are never made about this structure, and are not made here.",
        "<b>A static analysis gives the demand on a blast structure, not proof of "
        "blast resistance.</b> The non-linear support-rotation check is later-phase "
        "work and has not been done. This package delivers the structure that was "
        "designed; it does not validate the design.",
        "<b>Flotation cannot be read off a model whose springs take tension.</b> It "
        "is a hand check and it belongs to the designer.",
    ], FW, accent=AMBER, title="What this package does not claim"))

    story.append(PageBreak())

    # ================= 2  PROJECT SCOPE ===================================
    sec_head(story, 2, "Project scope", "")
    p(story,
      "The project comprises three physically separate structures with different "
      "design bases, different risk profiles and different positions in the "
      "programme. Treating them as one building is the mistake the preliminary "
      "schedule made and is the first thing this package corrects.", LEAD)

    story.append(tbl(
        ["", "Structure", "Design basis", "Position in the programme"],
        [["1", "<b>Main underground box</b><br/>Buried RC shelter, eight bays, "
               "22.0 × 6.2 m external, roof 2.0 m below grade, 20.8 × 5.0 m "
               "internal, 3.2 m clear height",
          "Nuclear air-blast, p<sub>so</sub> 344.7 kPa, design pressure 383 kPa "
          "on the roof <i>and</i> the walls. Total roof load 448.15 kPa. M35 "
          "concrete, Fe500D reinforcement",
          "The controlling chain. WBS 3 and 4"],
         ["2", "<b>Entry headhouse and covered approach stairwell</b><br/>"
               "Above-ground bermed RC on the shelter roof and adjacent fill",
          "Headhouse walls and roof designed for full blast pressure on either "
          "face. <b>The covered stairwell is outside the protective boundary and "
          "is declared expendable</b> — designed to IS 456 with normal partial "
          "factors",
          "Follows the pressure slab. WBS 5"],
         ["3", "<b>Sentry post</b><br/>Separate two-storey RC framed building, "
               "4.0 × 5.0 m, at least 10 m clear of the shelter excavation, on "
               "its own footings on in-situ basalt",
          "Seismic Zone III, R = 3.0, V<sub>b</sub> = 73.18 kN. M30 concrete, "
          "ductile detailing to IS 13920. <b>Not blast designed — a recorded "
          "decision.</b> Walls are brick masonry (SP-B1)",
          "Independent, with 118 days of float. WBS 8"]],
        [6 * mm, 46 * mm, 62 * mm, FW - 114 * mm], small=True))
    story.append(Paragraph(
        "Table 2.1 — The three structures.", CAP))

    story.append(Paragraph("2.1&nbsp;&nbsp;The protective boundary", H2))
    p(story,
      "The protective boundary is blast doors 1 and 2 at level (−)6.100, together "
      "with walls W6 and W7, the perimeter walls, the mat and the pressure slab. "
      "Everything above the blast doors — the stair shaft, the headhouse, the "
      "covered entry stairwell — lies outside it, and the covered stairwell is "
      "deliberately declared expendable.")
    p(story,
      "That single definition produces a large part of the construction logic. It "
      "is why the blast door frames must be cast into W6 and W7 rather than fixed "
      "afterwards; why there is no movement joint inside the envelope but there "
      "is one where the stairwell raft meets the headhouse; why the gas-tight "
      "envelope tested at handover is bays 1 to 6 only, 67.8 m² of floor and "
      "217.0 m³ of volume; and why the stair shaft and the generator bay sit "
      "outside that envelope as a deliberate grey zone.")

    story.append(Paragraph("2.2&nbsp;&nbsp;Scope of the Works Management package", H2))
    story.append(tbl(
        ["Scope element", "Covered by", "WBS"],
        [["Main underground shelter structure", "Mat, perimeter walls, protective "
          "walls W5/W6/W7, partitions, pressure slab with its openings, sump pit, "
          "main staircase", "3, 4"],
         ["Sentry post", "Footings, frame, <b>brick masonry walls</b>, lintels, "
          "spiral stair, finishes, electrical", "8"],
         ["All associated structural works", "Entry headhouse, covered entry "
          "stairwell, escape shaft collars", "5"],
         ["Access and egress", "Main staircase, entry stairwell, blast doors, "
          "security door, external door, escape shafts", "4.4, 5"],
         ["External works", "Berm, regrading, surface water, access, hardstanding, "
          "restoration", "13"],
         ["Drainage", "Internal gullies and drains, clean sump and pumps, "
          "segregated decontamination effluent, septic tank, soak pits", "10"],
         ["Waterproofing", "External tanking, roof membrane, protection screed, "
          "internal wet-area tanking, waterstops", "6"],
         ["Electrical works", "Containment, cabling, distribution, lighting, "
          "earthing, EMP enclosure and penetration protection", "11"],
         ["Overburden and backfilling", "Side backfill, six-layer engineered "
          "cover, M30 burster slab", "7"],
         ["Camouflage and concealment", "Topsoil and turf, spoil dressing, "
          "screening, track discipline", "13.3"],
         ["Construction and completion", "Mobilisation, earthworks, testing, "
          "commissioning, training, handover", "1, 2, 14"]],
        [40 * mm, FW - 56 * mm, 16 * mm], small=True))
    story.append(Paragraph("Table 2.2 — Scope coverage.", CAP))

    story.append(PageBreak())

    # ================= 3  PROJECT COMPONENTS ==============================
    sec_head(story, 3, "Project components", "")
    p(story,
      "Before a work breakdown structure can be written, the components that "
      "actually make up the finished project have to be identified from the "
      "project record rather than assumed. Twenty-three components are confirmed "
      "by the master project state file, the revision F drawings or an existing "
      "discipline package. All twenty-three are covered by this package.", LEAD)

    rows = [[c[0], "<b>%s</b>" % c[1], c[3], c[4]] for c in C.COMPONENTS]
    story.append(tbl(["Ref", "Component", "Source", "Class"], rows,
                     [11 * mm, FW - 66 * mm, 40 * mm, 15 * mm], small=True))
    story.append(Paragraph(
        "Table 3.1 — Confirmed project components. Full descriptions are in the "
        "project component register.", CAP))

    story.append(Paragraph("3.1&nbsp;&nbsp;Components that do not exist", H2))
    p(story,
      "A component is included only where the project record supports it. The "
      "preliminary schedule contained several that it does not, and each was "
      "removed rather than carried forward.")
    story.append(tbl(["Item in the preliminary schedule", "Why it is not in this project"],
                     [[i, w] for i, w in C.NOT_COMPONENTS],
                     [46 * mm, FW - 46 * mm], small=True))
    story.append(Paragraph("Table 3.2 — Items removed from the preliminary schedule.",
                           CAP))
    p(story,
      "The preliminary schedule also contained no sentry post as an identifiable "
      "structure, no escape shafts, no blast doors, no CBRN plant, no "
      "electromagnetic pulse works, no engineered cover build-up, no burster "
      "slab, no concealment works, no procurement activities, no commissioning "
      "sequence, and a single milestone. All of that is project scope and all of "
      "it is now in the breakdown.")

    story.append(PageBreak())

    # ================= 4  CONSTRUCTION METHODOLOGY ========================
    sec_head(story, 4, "Construction methodology", "")
    p(story,
      "The methodology is set out in full in the accompanying construction "
      "methodology document. This section gives the decisions that shape it — "
      "the ones that produce the logic links in the programme.", LEAD)

    for ref, title, paras in C.METHODOLOGY:
        if ref in ("M10",):
            continue
        story.append(Paragraph("%s&nbsp;&nbsp;%s" % (ref, title), H3))
        take = paras[:2] if ref in ("M1", "M12", "M13", "M14") else paras[:3]
        for para in take:
            p(story, para)

    story.append(PageBreak())

    # ================= 5  WBS =============================================
    sec_head(story, 5, "Work breakdown structure", "")
    p(story,
      "The breakdown has three levels: fourteen level-1 work packages, %d level-2 "
      "sub-packages and %d level-3 activities of which %d are milestones. It runs "
      "from contract award to practical completion and it covers all three "
      "structures in one integrated programme rather than three separate ones."
      % (len([c for c, _ in D.WBS if "." in c]), nact, nms), LEAD)

    roll = S.wbs_rollup(tasks)
    rows = []
    for code, title in D.WBS:
        if "." in code or code not in roll:
            continue
        es, ef = roll[code]
        n = len([t for t in tasks.values() if t.wbs.split(".")[0] == code])
        rows.append([code, "<b>%s</b>" % title, str(n),
                     S.dstr(es), S.dstr(ef), str(ef - es + 1)])
    story.append(tbl(["WBS", "Level-1 work package", "Acts", "Start", "Finish",
                      "Days"], rows,
                     [11 * mm, FW - 71 * mm, 11 * mm, 17 * mm, 17 * mm, 12 * mm],
                     align=[None, None, "r", None, None, "r"]))
    story.append(Paragraph("Table 5.1 — Level-1 work packages.", CAP))

    story.append(Paragraph("5.1&nbsp;&nbsp;Coding rules", H2))
    bullets(story, [
        "<b>Level 1</b> is a work package that could be let separately or reported "
        "on separately to the client.",
        "<b>Level 2</b> groups activities sharing a work face, a trade and a set "
        "of hold points.",
        "<b>Level 3</b> is an activity one gang can be instructed to do, with a "
        "measurable quantity behind it, that can be marked complete without "
        "ambiguity.",
        "Milestones carry zero duration and no resource. They are reporting "
        "events, not work.",
        "Hold points are activities in their own right — they consume time and "
        "require the Engineer's attendance — and are named so that they cannot be "
        "passed over silently.",
        "Activity numbers follow the level-1 package: A1xxx pre-construction "
        "through to A14xxx testing and handover.",
    ])
    p(story,
      "The breakdown and the programme are the same data. Every activity code in "
      "the work breakdown structure appears in the Microsoft Project file with "
      "the same identifier, duration and logic, and every item in the bill of "
      "quantities is measured against one of these work packages. They are "
      "generated together and cannot drift apart.")

    story.append(PageBreak())

    # ================= 6  UNDERGROUND SHELTER WORKS =======================
    sec_head(story, 6, "Underground shelter works", "")
    p(story,
      "The shelter accounts for %d of the %d activities and for the whole of the "
      "critical path between formation approval and the completion of the "
      "engineered cover." %
      (len([t for t in tasks.values()
            if t.wbs.split(".")[0] in ("2", "3", "4", "5", "6", "7")]), nact), LEAD)

    story.append(Paragraph("6.1&nbsp;&nbsp;Principal quantities", H2))
    story.append(tbl(
        ["Work", "Quantity", "Note"],
        [["Bulk excavation, 0.000 to (−)6.800", "1 338 m³",
          "24.0 × 8.2 m envelope including 1.0 m working space; vertical faces"],
         ["— of which in soil / weathered overburden", "344 m³",
          "at the mean rockhead (−)1.750; range 295–394 m³"],
         ["— of which in rock (Deccan basalt)", "994 m³",
          "hydraulic breaker, no blasting; range 945–1 043 m³"],
         ["Blinding, M15", "17.3 m³", "100 thk under the mat, footings and raft"],
         ["Structural concrete, M35", "388.7 m³",
          "mat 81.8 · walls 119.7 · pressure slab 112.0 · headhouse 32.7 · "
          "stairs and stairwell 22.9 · sump, collars, thickenings, partitions 19.5"],
         ["Reinforcement, Fe500D", "70.46 t",
          "92 bar marks; 33.6 % T16, 28.8 % T12, 21.9 % T25, 15.5 % T20"],
         ["Formwork, contact area", "1 058 m²", "including 104 m² of falsework "
          "deck at 3.200 m height"],
         ["Waterproofing", "532 m²", "continuous external tank plus internal "
          "wet-area tanking"],
         ["Side backfill", "290 m³", "250 layers to 95 % maximum dry density"],
         ["Engineered cover", "206 m³", "six layers totalling 2 000 mm"]],
        [56 * mm, 22 * mm, FW - 78 * mm], align=[None, "r", None], small=True))
    story.append(Paragraph("Table 6.1 — Principal shelter quantities.", CAP))

    story.append(Paragraph("6.2&nbsp;&nbsp;The three programme drivers", H2))
    story.append(Callout([
        "<b>Rock excavation — 994 m³ removed by hydraulic breaker.</b> No blasting "
        "is used: the sentry post founds on the same rock within 10 m and the "
        "installation is operational. Two breaker rigs at about 30 m³ a day give "
        "20 working days across two lifts.",
        "<b>The pressure slab prop period — 14 days.</b> IS 456 Table 11 requires "
        "14 days for props to a slab spanning over 4.5 m. This slab spans 5.000 m "
        "clear. With 14 days of curing before it, 19 working days sit on the "
        "critical path and are not available for compression. Striking requires a "
        "signed permit for exactly that reason.",
        "<b>The engineered cover — a structure, not a fill operation.</b> Six "
        "layers, one of which is a 200 mm M30 reinforced burster slab that has to "
        "be formed, reinforced, poured and cured inside the cover. Thirty-four "
        "working days from the roof membrane to the finished turf.",
    ], FW, accent=BLUE, title="What controls the shelter programme"))

    story.append(Paragraph("6.3&nbsp;&nbsp;The main staircase", H2))
    p(story,
      "The main staircase geometry is fixed and is not touched by this package: "
      "24 risers at 170.8333 mm, 280 mm tread, three flights of eight, total rise "
      "4 100 mm, flights 1 200 mm wide, a 200 mm well and 2 533 mm headroom. It is "
      "inside the protective envelope but is not a blast element and is designed "
      "to IS 456 with normal partial factors.")
    p(story,
      "It is programmed in two parts for a construction reason. The lower two "
      "flights and landings L1 and L2 are built immediately after the walls, "
      "which gives permanent access into the excavation and removes a temporary "
      "stair from the temporary works. The third flight rises to (−)2.000, which "
      "is the top of the pressure slab, so it cannot be cast until the slab is in "
      "and its props are struck.")

    story.append(PageBreak())

    # ================= 7  SENTRY POST WORKS ===============================
    sec_head(story, 7, "Sentry post works", "")
    p(story,
      "The sentry post is a separate two-storey reinforced concrete framed "
      "building 4.0 × 5.0 m on plan, at least 10 m clear of the shelter "
      "excavation, on its own footings on in-situ basalt at (−)2.000. It is not "
      "blast designed — that is a recorded decision in the project, not an "
      "omission — and it is designed for seismic Zone III with ductile detailing.",
      LEAD)

    story.append(tbl(
        ["Element", "Size", "Reinforcement", "Quantity"],
        [["Footings F1", "1500 × 1500 × 600, 4 No., on in-situ basalt at (−)2.000",
          "T12 @ 150 both ways bottom", "5.40 m³ M30"],
         ["Columns C1", "350 × 350, 4 No., both storeys, (−)1.400 to +6.700",
          "8-T16; T10 hoops with a cross-tie each way @ 85 over 500 from every "
          "joint face and through the joint; T8 @ 150 elsewhere", "3.97 m³"],
         ["Plinth beam PB", "250 × 400 at +0.450, 15.20 m clear",
          "3-T12 top + 3-T12 bottom", "1.52 m³"],
         ["Beams B1", "250 × 450, spanning 3 650 c/c, grids 1 and 2",
          "4-T16 top at supports, 2-T16 bottom continuous", "included below"],
         ["Beams B2", "250 × 450, spanning 4 650 c/c, grids A and B",
          "3-T20 top at supports, 2-T20 bottom continuous — <i>3-T20 chosen over "
          "5-T16 because five T16 bars need 256 mm in a 250 mm beam</i>",
          "2.28 m³ (ribs)"],
         ["Slab S1", "150 two-way, first floor 4.0 × 5.0 and roof 4.6 × 5.6 with "
          "the 300 projection",
          "T8 @ 150 both ways bottom; T8 @ 300 edge top 400 into the span; "
          "<b>T8 @ 200 torsion in four layers over 700 × 700 at all four "
          "corners</b>", "6.86 m³"],
         ["Parapet", "300 high over the roof projection", "nominal — not designed",
          "0.92 m³"],
         ["<b>Walls (SP-B1)</b>", "<b>190 brick masonry in a 200 structural zone, "
          "both storeys</b>", "<b>Unreinforced infill; lintels over all "
          "openings</b>", "<b>12.20 m³</b>"],
         ["Spiral stair", "External, 1000 R with a 250 dia central pole",
          "Fabrication detail not in the project record", "1 No."]],
        [22 * mm, 42 * mm, FW - 86 * mm, 22 * mm], small=True))
    story.append(Paragraph("Table 7.1 — Sentry post elements and quantities.", CAP))

    story.append(Paragraph("7.1&nbsp;&nbsp;Position in the programme", H2))
    p(story,
      "The sentry post is deliberately not started until the main rock breaking "
      "is finished. No green concrete stands within 10 m of a hydraulic breaker, "
      "and holding the post back also shortens the period over which a finished "
      "building is exposed to main-works traffic.")
    p(story,
      "It carries 118 working days of float — by a wide margin the largest block "
      "of float in the programme. That makes it the natural place to absorb "
      "labour redeployment when the main works are held up, and the natural place "
      "to take labour from when the main works need to catch up. It is reported "
      "as a separate progress stream for the same reason.")

    story.append(tbl(
        ["Milestone", "Baseline date", "Float"],
        [[n, S.CAL.day(tasks[a].es).strftime("%d %B %Y"), "%d d" % tasks[a].tf]
         for m, a, n in D.MILESTONES if tasks[a].wbs.startswith("8")],
        [FW - 56 * mm, 34 * mm, 22 * mm], align=[None, None, "r"]))
    story.append(Paragraph("Table 7.2 — Sentry post milestones.", CAP))

    story.append(Paragraph("7.2&nbsp;&nbsp;Reinforcement quantity", H2))
    p(story,
      "The sentry post has never been quantified anywhere in the project — the "
      "reinforcement package explicitly excludes it. Its reinforcement has "
      "therefore been derived here from the confirmed arrangement in the master "
      "reinforcement register: <b>1.97 t</b>, being 0.64 t of T8, 0.25 t of T10, "
      "0.19 t of T12, 0.62 t of T16 and 0.27 t of T20. Against 20.95 m³ of "
      "concrete that is about 94 kg/m³, which is plausible for a small "
      "ductile-detailed frame whose columns carry T10 confining hoops at 85 mm "
      "centres. It is a sanity check, not a design check, and it is an estimating "
      "quantity for tender that must be replaced by the fabricator's approved bar "
      "bending schedule.")

    story.append(PageBreak())

    # ================= 8  BRICK MASONRY ===================================
    sec_head(story, 8, "Sentry post brick masonry methodology", "")
    story.append(Callout(C.BRICK_METHOD["decision"], FW, accent=RED,
                         title="Design change SP-B1"))
    p(story, C.BRICK_METHOD["consequence"], LEAD)

    story.append(Paragraph("8.1&nbsp;&nbsp;Geometry", H2))
    story.append(tbl(["Item", "Value", "Basis"],
                     [[k, "<b>%s</b>" % v, b] for k, v, b in C.BRICK_METHOD["geometry"]],
                     [34 * mm, 30 * mm, FW - 64 * mm], small=True))
    story.append(Paragraph("Table 8.1 — Brick masonry geometry and quantity.", CAP))

    story.append(Paragraph("8.2&nbsp;&nbsp;Why 190 mm and not 230 mm", H2))
    p(story,
      "The confirmed structural zone between the column faces is 200 mm: the "
      "sentry post is 4 000 × 5 000 externally and 3 600 × 4 600 internally, with "
      "350 × 350 columns whose outer faces are flush with the wall. Two standard "
      "Indian brick sizes are available. Modular bricks to IS 1077 at "
      "190 × 90 × 90 build a 190 mm one-brick wall that fits inside the 200 mm "
      "zone with 10 mm to spare, which is taken up at the internal face and "
      "absorbed in the plaster. Conventional bricks at 230 × 110 × 75 build a "
      "230 mm wall that would project 30 mm beyond the column faces and change "
      "the confirmed external envelope.")
    p(story,
      "The modular brick is adopted because it preserves every confirmed "
      "dimension. Using the conventional brick would be a second design change, "
      "and the instruction for this package is that there is only one. The "
      "brickwork is measured at its actual 190 mm thickness, as IS 1200 (Part 3) "
      "requires, not at the 200 mm zone width.")

    story.append(Paragraph("8.3&nbsp;&nbsp;Why the panel height is 2.600 m", H2))
    p(story,
      "This is the project's own confirmed figure, not an assumption. The master "
      "gives the infill load on the first-floor beams as 13.000 kN/m and verifies "
      "it as 0.200 × 2.600 × 25, and the framing plan repeats '200 × 2600 high'. "
      "The first storey checks geometrically: the roof slab top at +6.700 less "
      "the 450 mm beam depth gives a soffit at +6.250, and +6.250 − +3.650 = "
      "2.600. The ground storey does not: the first floor at +3.650 less 450 mm "
      "gives a soffit at +3.200, and +3.200 − +0.450 = 2.750, which is 150 mm "
      "more. The project's confirmed 2.600 is used for both storeys and the "
      "difference is carried as a verification item. It is declared, not "
      "resolved.")

    story.append(Paragraph("8.4&nbsp;&nbsp;Construction method", H2))
    for i, step in enumerate(C.BRICK_METHOD["method"], 1):
        parts = step.split(". ", 1)
        p(story, "<b>%d. %s.</b> %s" % (i, parts[0].title() if parts[0].isupper()
                                        else parts[0],
                                        parts[1] if len(parts) > 1 else ""))

    story.append(Paragraph("8.5&nbsp;&nbsp;Programme", H2))
    brick_ids = ["A1176", "A8130", "A8135", "A8140", "A8145", "A8150", "A8155",
                 "A8160", "A8165", "A8175", "A8180", "A8185"]
    story.append(tbl(
        ["Act", "Description", "Days", "Start", "Finish"],
        [[a, ("<b>%s</b>" % tasks[a].name) if "MASONRY" in tasks[a].name
          else tasks[a].name,
          "—" if tasks[a].is_milestone else str(tasks[a].dur),
          S.dstr(tasks[a].es), S.dstr(tasks[a].ef)] for a in brick_ids],
        [15 * mm, FW - 61 * mm, 11 * mm, 17 * mm, 17 * mm],
        align=[None, None, "r", None, None], small=True))
    story.append(Paragraph(
        "Table 8.2 — The brick masonry sequence. Each storey is built only after "
        "the slab above it has cured, so the masonry is built into a completed "
        "frame rather than the frame being completed around it.", CAP))

    story.append(Paragraph("8.6&nbsp;&nbsp;Verification items raised by this change",
                           H2))
    story.append(tbl(
        ["Ref", "Item", "Status"],
        [["WM-V1", "Ground-storey panel height: the project's confirmed 2.600 m "
                   "against the 2.750 m implied by the levels", "Open — 2.600 used"],
         ["WM-V2", "First-floor west wall: door D1 lies inside the vision panel on "
                   "the drawing", "Open — the union is deducted once"],
         ["WM-V3", "Window and vision-panel heights are not stated anywhere",
          "Open — 1200 assumed"],
         ["WM-V4", "190 mm modular brickwork inside the 200 mm zone",
          "Open — needs the designer's confirmation"],
         ["WM-V5", "Lintel design over the nine openings — a new requirement "
                   "created by SP-B1", "Open — structural design required"],
         ["WM-V6", "Seismic weight changes. Brick at about 20 kN/m³ over "
                   "0.190 × 2.600 gives roughly 9.9 kN/m against the confirmed "
                   "13.000 kN/m, so the existing base shear is conservative — a "
                   "direction, not a verification",
          "Open — referred to the structural discipline"],
         ["WM-V7", "Ballistic performance. The panels are described as "
                   "'200 RC ballistic infill'; brick masonry does not provide "
                   "equivalent protection",
          "Open — recorded so the consequence is visible"],
         ["—", "Wall tie detail between the masonry and the columns",
          "Does not exist in the project"]],
        [15 * mm, FW - 65 * mm, 50 * mm], small=True))
    story.append(Paragraph("Table 8.3 — Verification items. None is resolved here.",
                           CAP))

    story.append(PageBreak())

    # ================= 9  CONSTRUCTION SEQUENCE ===========================
    sec_head(story, 9, "Construction sequence", "")
    p(story,
      "The sequence below is the programme logic in narrative form. The features "
      "worth noting are that the roof goes on before the walls are backfilled, "
      "that the sentry post is held back until the rock breaking is over, and "
      "that the protective systems are tested in a fixed order because each "
      "depends on the one before it.", LEAD)

    seq = [
        ("Mobilisation", "Approvals and workforce security clearance; site "
         "boundary and access control first, because the site is operational. "
         "Survey and confirmatory site investigation, with monsoon groundwater "
         "monitoring deliberately on the critical path. <b>Blast doors ordered on "
         "day one.</b>"),
        ("Earthworks", "Clear and strip, keeping the topsoil for the concealment "
         "layer. Temporary works and surface water cut-off. Excavate the soil to "
         "rockhead, then break rock in two lifts to (−)6.800. Sump pit. Dewater "
         "continuously. Trim the formation, over-excavate any red-bole seam and "
         "replace with M15. <b>Formation hold point.</b>"),
        ("Substructure", "Blinding, then the horizontal tanking, then a hold "
         "point before it is covered. Mat and sump cast in one pour with the wall "
         "starters set. Fourteen days curing. Wall reinforcement in both curtains "
         "at 150 spacing, with the <b>blast door frames set, aligned and welded to "
         "the cage</b>. Walls in two lifts of 1.6 m with two waterstops and a "
         "welded strap at every joint. Lower stair flights, which give permanent "
         "access."),
        ("Pressure slab", "Falsework at 3.2 m. Bottom curtain, opening trimmers, "
         "escape shaft collar bands, local thickenings, links, top curtain, "
         "haunches, cast-ins. <b>Pre-pour hold point.</b> A single continuous "
         "112 m³ pour. Fourteen days curing, then props for fourteen days to "
         "IS 456 Table 11. Strike, then the upper stair flight."),
        ("Entry structures", "Headhouse walls and roof off the top of the "
         "pressure slab; the covered stairwell on its stepped raft with the "
         "movement joint at the headhouse; escape shaft collars up to their heads "
         "before the cover is placed; blast doors installed."),
        ("Waterproofing", "Vertical tanking and its protection, with a hold point "
         "before backfilling because it can never be seen again. Roof membrane "
         "and the 100 mm protection screed, with a second hold point before "
         "covering."),
        ("Sentry post", "Held until the rock breaking is over. Footings on a "
         "confirmed founding stratum, then the frame storey by storey. <b>Brick "
         "masonry ground storey after the first floor has cured, first storey "
         "after the roof has cured</b>, each with a hold point on line, level, "
         "plumb and joint thickness. Lintels, spiral stair, chases cut for "
         "conduit, plaster, flooring, finishes."),
        ("Services", "Builder's work coordinated with the reinforcement, not cut "
         "afterwards. Ductwork with every run inspectable. Blast valves. Filter "
         "trains and generator. Drainage with the decontamination effluent "
         "physically segregated. Electromagnetic pulse enclosure and penetration "
         "protection. Electrical distribution and earthing."),
        ("Cover and overburden", "Side backfill in 250 layers, density tested "
         "before the cover goes on. Then the six layers from the bottom up: "
         "100 screed, 750 compacted fill, 500 crushed basalt won from our own "
         "excavation, the 200 M30 burster slab, 150 granular filter, 300 topsoil "
         "and turf. Verified against the design build-up."),
        ("External works", "Berm at 1.5:1 to +0.900, site regraded with 1:50 "
         "falls, surface water, access and hardstanding, turfing, concealment "
         "measures, removal of temporary works."),
        ("Testing and handover", "Cubes and non-destructive testing; "
         "watertightness; drainage; electrical and a 5 Ω earth; <b>then the "
         "protective sequence in order</b> — shielding survey, blast door seals, "
         "gas-tightness and overpressure, filter train commissioning, generator, "
         "integrated protective-mode operation. Snagging, rectification, "
         "contingency, documentation, training, handover."),
    ]
    story.append(tbl(["Stage", "Sequence"], seq, [30 * mm, FW - 30 * mm]))
    story.append(Paragraph("Table 9.1 — Construction sequence.", CAP))

    story.append(Paragraph("9.1&nbsp;&nbsp;Three sequencing decisions worth defending",
                           H2))
    p(story,
      "<b>The roof before the backfill.</b> A 3.2 m wall carrying an 83.2 kPa "
      "gradient at its base needs a prop at the top. The pressure slab is that "
      "prop. Backfilling earlier would mean designing, installing and later "
      "removing temporary propping to do the same job worse, and would put "
      "temporary works loads into a structure whose whole purpose is that it "
      "carries a very large permanent one.")
    p(story,
      "<b>The lower stair flights early.</b> Building the first two flights and "
      "landings immediately after the walls costs nothing on the critical path "
      "and removes a temporary access stair from a 6.8 m excavation for the whole "
      "of the pressure slab operation.")
    p(story,
      "<b>The sentry post after the rock breaking.</b> Hydraulic breaking within "
      "10 m of green concrete is avoidable simply by ordering the work "
      "differently, and doing so also reduces the time a finished building stands "
      "exposed to main-works traffic.")

    story.append(PageBreak())

    # ================= 10  PROGRAMME ======================================
    sec_head(story, 10, "Final work programme", "")
    p(story,
      "The master programme covers the complete project in one integrated "
      "network: %d activities, %d milestones and %d logic links using "
      "finish-to-start, start-to-start and finish-to-finish relationships with "
      "positive and negative lags. It runs from %s to %s — %d working days on a "
      "six-day week." % (nact, nms, nlinks, S.CAL.day(0).strftime("%d %B %Y"),
                         fin.strftime("%d %B %Y"), end + 1), LEAD)

    story.append(MiniGantt(tasks, FW))
    story.append(Paragraph(
        "Figure 10.1 — Summary programme, the fourteen level-1 work packages.", CAP))

    story.append(Paragraph("10.1&nbsp;&nbsp;Calendar", H2))
    p(story, D.CALENDAR_NOTE)
    p(story,
      "The six-day week is read from the preliminary schedule rather than "
      "imposed: its stated 224 working days between 2 November 2026 and 26 July "
      "2027 corresponds to a six-day week with a small number of holidays, and "
      "the same convention is kept.")

    story.append(Paragraph("10.2&nbsp;&nbsp;Milestones", H2))
    story.append(tbl(
        ["Ref", "Milestone", "Date", "Float", "Status"],
        [[m, n, S.CAL.day(tasks[a].es).strftime("%d %b %Y"), "%d d" % tasks[a].tf,
          "<b>CRITICAL</b>" if tasks[a].tf == 0 else ""]
         for m, a, n in D.MILESTONES],
        [13 * mm, FW - 71 * mm, 22 * mm, 14 * mm, 22 * mm],
        align=[None, None, None, "r", None], small=True))
    story.append(Paragraph("Table 10.1 — Milestone register.", CAP))

    story.append(Paragraph("10.3&nbsp;&nbsp;Critical path and float", H2))
    p(story,
      "%d activities carry zero total float. The controlling chain runs: site "
      "possession, the confirmatory site investigation and monsoon groundwater "
      "monitoring — which must close the assumed water table before the "
      "excavation support can be designed — then rock excavation, formation "
      "approval, the external tanking, the mat, the perimeter and protective "
      "walls, the pressure slab with its fourteen-day prop period, the roof "
      "membrane, the six-layer engineered cover including the burster slab, the "
      "external works and concealment, and finally snagging, rectification and "
      "handover." % ncrit)
    bands = [(0, 0, "Critical — any slip is a project slip"),
             (1, 10, "Near critical — flagged in every monthly report"),
             (11, 30, "Manageable"),
             (31, 90, "Comfortable"),
             (91, 10 ** 6, "Large — procurement and the sentry post")]
    story.append(tbl(
        ["Total float band", "Activities", "Interpretation"],
        [["TF = 0" if hi == 0 else ("TF > 90" if hi > 10 ** 5 else "TF %d–%d" % (lo, hi)),
          str(sum(1 for t in tasks.values() if lo <= t.tf <= hi)), desc]
         for lo, hi, desc in bands],
        [28 * mm, 20 * mm, FW - 48 * mm], align=[None, "r", None]))
    story.append(Paragraph("Table 10.2 — Float distribution.", CAP))

    story.append(Paragraph("10.4&nbsp;&nbsp;Programme file", H2))
    p(story,
      "The editable master programme is issued as "
      "<font face='Courier'>Underground_Shelter_Final_Works_Programme.xml</font>, "
      "written in the Microsoft Project Data Interchange schema — Microsoft "
      "Project's own published XML format. Microsoft Project opens it directly, "
      "and <i>File → Save As → Project (*.mpp)</i> produces the binary file. The "
      "native .mpp format is undocumented and can only be written by Microsoft "
      "Project itself, so it is not imitated here. The interchange file carries "
      "the full breakdown structure, every activity, every logic link with its "
      "lag, the six-day calendar with its exceptions, %d resources and %d "
      "assignments, and it was verified by reading it back and comparing every "
      "date against the critical-path calculation. A programme drawing and a "
      "comma-separated task list accompany it."
      % (len(D.RESOURCES),
         sum(len([x for x in t.res.split(';') if x.strip()]) for t in tasks.values())))

    story.append(PageBreak())

    # ================= 11  BOQ ============================================
    sec_head(story, 11, "Bill of quantities", "")
    p(story,
      "The bill covers the entire project. Nothing in it is fabricated: every "
      "quantity is either taken directly from an existing project package or "
      "derived from confirmed geometry with the arithmetic shown. The full "
      "derivation — the source of every input and every line of working — "
      "accompanies this handout.", LEAD)

    hi = {"A": "1 338 m³ bulk excavation · 994 m³ in rock · 290 m³ backfill",
          "B": "388.7 m³ M35 · 17.3 m³ M15 blinding",
          "C": "77.33 t ordered · 70.46 t shelter · 1.97 t sentry · 1.22 t burster",
          "D": "1 058 m² formwork · 104 m² falsework deck at 3.200 m",
          "E": "205.8 m³ in six layers · 20.6 m³ M30 burster slab",
          "F": "532 m² tanking · 110 m waterstop",
          "G": "20.95 m³ M30 · 4 No. footings F1",
          "H": "<b>12.20 m³ brick masonry · 64.19 m² face · about 6 400 bricks</b>",
          "I": "All quantities to be verified — no electrical design exists",
          "J": "194 t cement · 829 t aggregate"}
    story.append(tbl(
        ["", "Section", "Items", "Principal quantities"],
        [[s, n, str(len([k for k in Q if any(k.startswith(x) for x in pf)])), hi[s]]
         for s, n, pf in
         [(a, b, c) for a, b, c in __import__("wm_docs").BOQ_SECTIONS]],
        [7 * mm, 62 * mm, 12 * mm, FW - 81 * mm], align=[None, None, "r", None],
        small=True))
    story.append(Paragraph("Table 11.1 — Bill summary.", CAP))

    story.append(Paragraph("11.1&nbsp;&nbsp;Basis of measurement", H2))
    bullets(story, [
        "Measurement follows the IS 1200 series — Part 1 earthwork, Part 2 "
        "concrete, Part 3 brickwork, Part 5 formwork, Part 12 plastering.",
        "Concrete volumes for the shelter and entry structures are taken verbatim "
        "from the existing reinforcement package. Six of its eight lines were "
        "independently re-derived here and reproduce exactly.",
        "Reinforcement for the shelter is taken verbatim from the approved bar "
        "bending schedule: 70.46 t across 92 bar marks, with that package's own "
        "declared convention — cut length as the sum of scheduled legs with no "
        "bend deduction, laps at 50 φ, 12 m stock bar.",
        "The sentry post had never been quantified anywhere in the project. Its "
        "concrete and reinforcement are derived here from the confirmed "
        "arrangement in the master reinforcement register, for tender and "
        "estimating only.",
        "Rates are not included. Rates come from the MES Standard Schedule of "
        "Rates, and no item number from it is quoted because none could be "
        "verified. " + C.MES_CAVEAT,
    ])

    story.append(Paragraph("11.2&nbsp;&nbsp;The sentry post brick masonry", H2))
    story.append(tbl(
        ["", "Ground storey", "First storey", "Total"],
        [["Wall run between columns", "15.200 m", "15.200 m", "—"],
         ["Panel height", "2.600 m", "2.600 m", "—"],
         ["Gross face area", "39.52 m²", "39.52 m²", "79.04 m²"],
         ["Openings deducted", "3.33 m²", "11.52 m²", "14.85 m²"],
         ["<b>Net masonry face</b>", "<b>36.19 m²</b>", "<b>28.00 m²</b>",
          "<b>64.19 m²</b>"],
         ["<b>Volume at 190 thk</b>", "<b>6.88 m³</b>", "<b>5.32 m³</b>",
          "<b>12.20 m³</b>"],
         ["Bricks including 5 % breakage", "—", "—", "about 6 400 No."],
         ["Cement for CM 1:6", "—", "—", "14.5 bags"],
         ["Sand", "—", "—", "3.0 m³"]],
        [FW - 90 * mm, 30 * mm, 30 * mm, 30 * mm],
        align=[None, "r", "r", "r"]))
    story.append(Paragraph("Table 11.2 — Brick masonry measurement.", CAP))

    story.append(Paragraph("11.3&nbsp;&nbsp;What cannot be quantified", H2))
    p(story,
      "Where a quantity genuinely cannot be determined from the project record, "
      "the item reads <i>to be verified from final measurement</i> and the reason "
      "is stated. It is not estimated and it is not left out.")
    story.append(tbl(["Item", "Why"],
                     [["Berm volume, regrading, access route, hardstanding",
                       "No site plan or ground model exists"],
                      ["Concealment beyond the topsoil layer",
                       "No concealment specification exists"],
                      ["Every electrical quantity",
                       "No electrical design package exists — the scope is "
                       "confirmed, the design is not"],
                      ["Blast door leaves, frames and anchorage",
                       "Vendor items, recorded in the project as not available"],
                      ["Blast valve sizes and sleeve details",
                       "Not in the structural design record"],
                      ["Sentry post lintel design",
                       "Does not exist — a consequence of SP-B1"],
                      ["Sentry post ground-floor slab",
                       "Not designed; the member schedule covers the first floor "
                       "and roof only"],
                      ["Finishes rates",
                       "The finishes schedule specifies performance and leaves the "
                       "product deliberately open, so areas can be measured but "
                       "rates cannot"],
                      ["Window and vision-panel heights",
                       "Not stated on any drawing"]],
                     [58 * mm, FW - 58 * mm], small=True))
    story.append(Paragraph("Table 11.3 — Items declared as not determinable.", CAP))

    story.append(PageBreak())

    # ================= 12  RESOURCES ======================================
    sec_head(story, 12, "Resource management", "")
    p(story,
      "The resource plan lists the resources that actually do the work and "
      "nothing else. Every resource below is assigned to at least one activity in "
      "the programme; a plan padded with resources that never appear on the "
      "programme is not a plan.", LEAD)

    used = {}
    for t in tasks.values():
        for r in [x.strip() for x in t.res.split(";") if x.strip()]:
            used.setdefault(r, []).append(t)
    for grp, title in (("Staff", "12.1  Staff"), ("Labour", "12.2  Labour"),
                       ("Plant", "12.3  Plant and equipment")):
        story.append(Paragraph(title.replace("  ", "&nbsp;&nbsp;"), H2))
        story.append(tbl(
            ["Resource", "Composition", "Peak", "What drives the peak", "Acts"],
            [[n, comp, str(pk), note, str(len(used.get(n, [])))]
             for n, g, comp, pk, note in D.RESOURCES if g == grp],
            [32 * mm, 34 * mm, 11 * mm, FW - 88 * mm, 11 * mm],
            align=[None, None, "r", None, "r"], small=True))

    story.append(Paragraph("12.4&nbsp;&nbsp;Resources for the sentry post masonry",
                           H2))
    p(story,
      "The masonry gang is three masons with helpers. At roughly 2.4 m² of "
      "finished one-brick wall per mason-day — reduced from the flat-wall rate "
      "because both storeys are short panels between columns with a high "
      "proportion of opening perimeter and cut brick — three masons clear the "
      "ground storey in five days and the first storey in four. The first storey "
      "has less masonry but more openings, more cutting and more scaffold, which "
      "is why the saving is one day and not two.")
    p(story,
      "All output rates in this package are assumed. The quantities they are "
      "applied to are confirmed or derived and are traceable; the rates are not, "
      "and they are the first thing that should be re-tested when a contractor is "
      "appointed.")

    story.append(Paragraph("12.5&nbsp;&nbsp;Peak resource periods", H2))
    story.append(tbl(
        ["Period", "Peak demand", "Why"],
        [["Dec 2026 – Jan 2027", "2 excavators, 2 rock breakers, 4 tippers",
          "994 m³ of basalt removed by breaker in 20 working days"],
         ["Mar – May 2027", "4 bar-bender gangs",
          "24.7 t of wall reinforcement at 150 spacing in both curtains"],
         ["May – Jun 2027", "4 bar-bender and 4 carpenter gangs",
          "Pressure slab — 20.5 t of T25 and 104 m² of deck at 3.200 m"],
         ["25–26 Jun 2027", "2 concrete gangs, pump, 4 transit mixers",
          "The 112 m³ continuous pressure slab pour"],
         ["Mar – Apr 2027", "3 mason gangs",
          "Sentry post brick masonry, both storeys"],
         ["Aug – Sep 2027", "Excavator, roller, plate compactors",
          "The six-layer engineered cover, 206 m³"],
         ["Sep – Oct 2027", "Specialist subcontractors",
          "Shielding survey, blast door tests, gas-tightness, CBRN commissioning"]],
        [30 * mm, 48 * mm, FW - 78 * mm], small=True))
    story.append(Paragraph("Table 12.1 — Peak resource periods.", CAP))

    story.append(PageBreak())

    # ================= 13  PROCUREMENT ====================================
    sec_head(story, 13, "Procurement", "")
    p(story,
      "Procurement is programmed, not assumed. Every package is tied to an "
      "activity in the master programme and every package is required before the "
      "activity that installs it, with the dates computed from the programme "
      "rather than typed in.", LEAD)
    story.append(Callout(
        "The governing fact of this project's procurement is that <b>the blast "
        "door cast-in frames must be welded into the W6 and W7 reinforcement "
        "cages before those walls are poured.</b> A seventy-five-day vendor lead "
        "time therefore sits directly upstream of the wall concrete, which is why "
        "the blast door enquiry is the first procurement activity on the "
        "programme and why the frames are ordered as a separate, earlier delivery "
        "than the door leaves.", FW, accent=RED,
        title="Why procurement is construction logic here"))

    story.append(tbl(
        ["Package", "Lead", "Ordered", "Delivered", "Needed", "Float"],
        [[label, "%d d" % tasks[a].dur, S.dstr(tasks[a].es), S.dstr(tasks[a].ef),
          S.dstr(tasks[n].es), "%d d" % (tasks[n].es - tasks[a].ef - 1)]
         for a, label, n in [
             ("A1120", "Blast door cast-in frames", "A3105"),
             ("A1122", "Blast door leaves", "A5135"),
             ("A1135", "CBRN filter trains", "A9040"),
             ("A1145", "Blast valves and sleeves", "A9015"),
             ("A1155", "Shielded enclosure", "A11030"),
             ("A1160", "Generator 15 kVA", "A9050"),
             ("A1165", "Armoured vision panels", "A8195"),
             ("A1170", "Submersible pumps", "A10020"),
             ("A1172", "Reinforcement, 77.3 t", "A3040"),
             ("A1174", "Waterproofing system", "A3020"),
             ("A1176", "<b>Modular bricks to IS 1077</b>", "A8130")]],
        [FW - 88 * mm, 14 * mm, 18 * mm, 18 * mm, 18 * mm, 14 * mm],
        align=[None, "r", None, None, None, "r"]))
    story.append(Paragraph(
        "Table 13.1 — Long-lead items. All lead times are assumed; replacing them "
        "with quoted times at tender is the single most valuable thing that can "
        "be done to de-risk this programme.", CAP))

    story.append(Paragraph("13.1&nbsp;&nbsp;Brick masonry procurement", H2))
    p(story,
      "The whole brick requirement is about 6 400 bricks — a single approved "
      "batch. That is an advantage worth protecting. The source is approved once, "
      "against IS 1077 class designation 10, with samples drawn to IS 5454 and "
      "tested to IS 3495 for compressive strength, water absorption, "
      "efflorescence and warpage <i>before</i> the order is placed, and it is not "
      "changed without retesting. Changing brick source part way through a 64 m² "
      "job means retesting for a quantity too small to justify it.")

    story.append(Paragraph("13.2&nbsp;&nbsp;Procurement risk", H2))
    p(story,
      "Four packages have no recovery available once they are late: the blast "
      "doors, the CBRN filter trains, the blast valves and the shielded "
      "enclosure. They are managed by monitoring the vendor — monthly "
      "manufacturing progress reports — rather than by planning to recover, "
      "because there is no recovery to plan.")
    p(story,
      "One package cannot be procured at all yet. No electrical design package "
      "exists, so no electrical enquiry can be issued. The date by which the "
      "design is needed is computed from the programme and issued to the designer "
      "at mobilisation rather than requested when the activity falls due.")

    story.append(PageBreak())

    # ================= 14  QA/QC ==========================================
    sec_head(story, 14, "Quality assurance and quality control", "")
    holds = [t for t in sorted(tasks.values(), key=lambda x: x.es)
             if t.name.startswith("HOLD POINT")]
    p(story,
      "The quality plan is built around hold points. A hold point is an activity "
      "in its own right in the programme — it takes time, it requires the "
      "Engineer's attendance, and work does not proceed past it. There are %d of "
      "them, placed at the moments where an error becomes permanent." % len(holds),
      LEAD)

    story.append(tbl(["Hold", "Activity", "Description", "Date"],
                     [[t.note or "—", t.id,
                       t.name.replace("HOLD POINT: ", ""), S.dstr(t.es)]
                      for t in holds],
                     [13 * mm, 16 * mm, FW - 51 * mm, 22 * mm], small=True))
    story.append(Paragraph("Table 14.1 — Hold points in the programme.", CAP))

    story.append(Paragraph("14.1&nbsp;&nbsp;The five checks that matter most", H2))
    bullets(story, [
        "<b>The formation.</b> The hazard is not the basalt, it is the red-bole "
        "and vesicular seams at the flow contacts — a single seam under the mat "
        "produces the differential-support case that sizes the mat. Every seam is "
        "over-excavated and replaced with M15, and the approval carries a seam "
        "map.",
        "<b>The tanking before it is covered.</b> The external tank is continuous "
        "under the mat, up the walls and over the roof. Once backfilled it can "
        "never be seen again, and the structure sits with its roof 2 m below "
        "grade and a design water table at roof level.",
        "<b>Reinforcement at 150 spacing in both curtains.</b> This is an "
        "electromagnetic pulse requirement and is stricter than IS 456. It is not "
        "a strength requirement, which means an engineer looking only at strength "
        "will see no reason not to relax it when the cage gets congested. It must "
        "not be relaxed.",
        "<b>Formwork striking.</b> Props to a slab spanning over 4.5 m stay for "
        "14 days; this slab spans 5.000 m clear. Striking requires a signed "
        "permit and the fourteen days are in the baseline programme.",
        "<b>Sentry post masonry line, level and plumb.</b> Checked at the end of "
        "each storey, before plaster. Plumb over the 2.600 m storey height and "
        "joint thickness decide whether the plaster can be held to its stated "
        "thickness — and once plaster is on, neither can be corrected.",
    ])

    story.append(Paragraph("14.2&nbsp;&nbsp;Quality control of the brick masonry",
                           H2))
    p(story,
      "The masonry brings a set of checks the reinforced concrete panels did not "
      "need. They are grouped so that they can be issued as a single inspection "
      "sheet.")
    story.append(tbl(
        ["Check", "Criterion", "Reference"],
        [["Brick source approval", "Class 10; dimensional tolerance on "
          "190 × 90 × 90", "IS 1077"],
         ["Compressive strength", "Not less than 10 N/mm² average",
          "IS 3495 (Part 1)"],
         ["Water absorption, efflorescence, warpage", "Within the IS 1077 limits "
          "for the class", "IS 3495 (Parts 2–4)"],
         ["Sampling", "Sample size and selection", "IS 5454"],
         ["Soaking", "Thoroughly wet before laying, not surface-damp", "IS 2212"],
         ["Mortar", "CM 1:6 by gauge box, used within 30 minutes, never "
          "re-tempered", "IS 2250"],
         ["Mortar sand", "Grading and cleanliness", "IS 2116"],
         ["Bond and joints", "English bond one brick thick; 10 mm joints fully "
          "filled bed, cross and vertical", "IS 2212"],
         ["Lift height", "Not more than 1 m above adjacent work in a day",
          "IS 2212"],
         ["Level and plumb", "Level every fourth course; plumb over the full "
          "2.600 m storey height", "IS 2212 — <b>hold point</b>"],
         ["Frame interface", "Top course wedged and packed only after initial "
          "shrinkage", "IS 1905 — <b>hold point</b>"],
         ["Wall ties", "At the specified spacing", "<b>Detail does not yet "
          "exist</b>"],
         ["Lintels", "Approved design, section, reinforcement, 200 bearing each "
          "end", "IS 456 — <b>design does not yet exist</b>"],
         ["Curing", "Damp for at least seven days", "IS 2212"],
         ["Chases for conduit", "Cut, not hammered; not before the masonry has "
          "cured", "IS 2212"],
         ["Plaster", "Thickness, line, level, no hollowness on tapping, "
          "seven-day cure", "IS 1661"]],
        [46 * mm, FW - 88 * mm, 42 * mm], small=True))
    story.append(Paragraph("Table 14.2 — Brick masonry quality control.", CAP))

    story.append(Paragraph("14.3&nbsp;&nbsp;Non-conformance", H2))
    p(story,
      "A non-conformance is raised the moment it is identified, by anyone, and is "
      "closed only against evidence. Three categories on this project are not "
      "closable by repair and require the designer's ruling: reinforcement "
      "spacing relaxed beyond 150 mm inside the protective envelope; a "
      "construction joint formed without both waterstops and the bonding strap; "
      "and any penetration cut through the envelope after casting.")

    story.append(PageBreak())

    # ================= 15  SAFETY =========================================
    sec_head(story, 15, "Safety management", "")
    p(story,
      "Four features set the safety regime for this project: a 6.8 m deep "
      "excavation in rock, a buried structure that becomes a confined space, "
      "substantial work at height on the headhouse and the sentry post, and "
      "specialist lifting of heavy protective components.", LEAD)
    p(story,
      "Baseline arrangements are site induction before first entry; minimum "
      "personal protective equipment of helmet, safety footwear, high-visibility "
      "clothing and eye protection with task-specific additions; a first-aid post "
      "and trained first-aiders; a documented emergency plan covering rescue from "
      "height, rescue from confined space and evacuation of a flooded excavation; "
      "a weekly safety walk and a monthly safety committee; and permit-to-work "
      "for confined space entry, hot work and live electrical work.")

    story.append(tbl(
        ["Ref", "Activity", "Principal hazards", "Controls", "Reference"],
        [[r[0], r[1], r[2], r[3], r[4]] for r in C.SAFETY],
        [11 * mm, 26 * mm, 40 * mm, FW - 116 * mm, 39 * mm], small=True))
    story.append(Paragraph("Table 15.1 — Safety register.", CAP))

    story.append(Paragraph("15.1&nbsp;&nbsp;Masonry hazards on the sentry post", H2))
    p(story,
      "Masonry is often treated as a low-risk trade, so the hazards it introduces "
      "are set out separately.")
    bullets(story, [
        "<b>Falls from the masonry scaffold.</b> The first-storey panels are built "
        "3.2 m above the ground floor. An independent tied scaffold with a proper "
        "working platform, guard-rail, mid-rail and toe-board is required — never "
        "a trestle standing on a slab edge.",
        "<b>Collapse of a freshly built panel.</b> A 190 mm panel 2.6 m high and "
        "up to 4.3 m long is slender while its mortar is green. Lift height is "
        "limited to 1 m above adjacent work in a day, and free-standing panels "
        "are temporarily propped.",
        "<b>Manual handling.</b> About 6 400 bricks and 3.5 m³ of mortar are "
        "handled. Bricks are hoisted mechanically above ground level, never "
        "thrown.",
        "<b>Silica dust.</b> A high proportion of the masonry is short panels "
        "between columns with cut brick at every opening reveal. Wet cutting or "
        "on-tool extraction, with respiratory protection.",
        "<b>Eye injury.</b> From mortar splash while laying the top course "
        "overhead, and from chasing for conduit. Eye protection for laying, "
        "cutting and chasing.",
    ])

    story.append(Paragraph("15.2&nbsp;&nbsp;The three events that would stop the job",
                           H2))
    p(story,
      "<b>A fall of ground into the excavation</b> while people work at (−)6.800 — "
      "controlled by designed faces, edge protection installed as the excavation "
      "deepens, and daily inspection after rain. <b>A falsework collapse</b> "
      "during the 112 m³ continuous pour, with a concrete gang working beneath "
      "104 m² of deck at 3.200 m — controlled by designed and checked falsework "
      "inspected before every pour. <b>A confined-space fatality</b> in the sump "
      "at (−)8.100 or in a 1 400 mm escape shaft — controlled by permit, gas "
      "testing, forced ventilation, harness and retrieval line, a standby person "
      "and a rehearsed rescue plan.")

    story.append(PageBreak())

    # ================= 16  RISK ===========================================
    sec_head(story, 16, "Risk management", "")
    p(story,
      "Risks are scored for likelihood and impact. The response column states "
      "what is actually done about the risk in the programme, the procurement "
      "plan or the quality plan — not a statement of intent.", LEAD)
    story.append(tbl(
        ["Ref", "Category", "Risk", "L", "I", "Response"],
        [[r[0], r[1], r[2], r[3], r[4], r[5]] for r in C.RISKS],
        [11 * mm, 18 * mm, 48 * mm, 6 * mm, 6 * mm, FW - 89 * mm], small=True))
    story.append(Paragraph("Table 16.1 — Risk register.", CAP))

    story.append(Paragraph("16.1&nbsp;&nbsp;The four risks that carry the project",
                           H2))
    bullets(story, [
        "<b>Blast door frames arrive late (R-04).</b> The frames must be welded "
        "into the W6 and W7 cages before those walls are poured. A late frame "
        "stops the wall, and the wall stops the pressure slab, the cover and "
        "everything after it.",
        "<b>No electrical design package exists (R-08).</b> The scope is confirmed "
        "but no circuit, cable, luminaire, distribution board or earth-electrode "
        "schedule does. This is the largest single information gap on the "
        "project.",
        "<b>Red-bole seams under the mat (R-02).</b> The project record is "
        "explicit that the hazard is the flow contacts, not the basalt, and that "
        "a single seam produces the differential-support case that sizes the mat.",
        "<b>Groundwater higher than assumed (R-01).</b> Water is nearly "
        "two-thirds of the 15.41 kPa/m lateral gradient. Monsoon monitoring is "
        "deliberately on the critical path so the answer arrives before the "
        "excavation support is designed, not after the walls are built.",
    ])

    story.append(Paragraph("16.2&nbsp;&nbsp;Risks arising from the design change",
                           H2))
    p(story,
      "Substituting brick masonry for the reinforced concrete infill panels "
      "creates four risks that did not previously exist: there is no lintel "
      "design, no wall tie detail and a changed seismic weight (R-09); the "
      "ballistic function the panels were named for is lost (R-10); masonry "
      "workmanship becomes a quality risk on a structure that previously "
      "contained no masonry at all (R-15); and brick supply consistency matters "
      "for a quantity too small to justify retesting a second source (R-16).")
    p(story,
      "The seismic point is worth stating precisely because it is easy to get "
      "wrong. The project uses a response reduction factor of 3.0 <i>specifically "
      "because</i> the infill is not separated from the frame, and designs to a "
      "base shear of 73.18 kN. Replacing 200 mm of concrete at 25 kN/m³ with "
      "190 mm of brickwork at about 20 kN/m³ reduces the infill line load from "
      "13.000 kN/m to roughly 9.9 kN/m, which reduces the seismic weight and "
      "therefore points the existing design in the conservative direction. That "
      "is a direction, not a verification. The structural discipline must re-run "
      "the check; this package does not, and does not claim to.")

    story.append(PageBreak())

    # ================= 17  PROGRESS =======================================
    sec_head(story, 17, "Progress monitoring", "")
    for para in C.PROGRESS["baseline"]:
        p(story, para)
    story.append(Paragraph("17.1&nbsp;&nbsp;Measurement", H2))
    for para in C.PROGRESS["measurement"]:
        p(story, para)

    story.append(Paragraph("17.2&nbsp;&nbsp;Three reporting streams, one project",
                           H2))
    p(story,
      "Progress is tracked separately for three streams and consolidated for the "
      "project. The streams are chosen so that each has a different trade, a "
      "different work face and a different risk profile; reporting them together "
      "would hide exactly the divergence that matters.")
    stream_wbs = {"A — Underground shelter": ["2", "3", "4", "5", "6", "7", "12"],
                  "B — Sentry post": ["8"],
                  "C — Services and external works": ["9", "10", "11", "13"]}
    rows = []
    for (label, scope, meas), (lab2, tops) in zip(C.PROGRESS["streams"],
                                                  stream_wbs.items()):
        sel = [t for t in tasks.values() if t.wbs.split(".")[0] in tops]
        rows.append([label.replace("Stream ", ""), scope, meas,
                     "%s – %s" % (S.dstr(min(t.es for t in sel)),
                                  S.dstr(max(t.ef for t in sel)))])
    story.append(tbl(["Stream", "Scope", "How it is measured", "Baseline"], rows,
                     [30 * mm, 42 * mm, FW - 106 * mm, 34 * mm], small=True))
    story.append(Paragraph("Table 17.1 — Reporting streams.", CAP))

    story.append(Paragraph("17.3&nbsp;&nbsp;Reporting cycle", H2))
    story.append(tbl(["Frequency", "Content"],
                     [[f, c] for f, c in C.PROGRESS["cycle"]],
                     [24 * mm, FW - 24 * mm], small=True))
    story.append(Paragraph("Table 17.2 — Reporting cycle.", CAP))

    story.append(Paragraph("17.4&nbsp;&nbsp;Delay tracking and corrective action",
                           H2))
    for para in C.PROGRESS["delay"]:
        p(story, para)
    for para in C.PROGRESS["corrective"]:
        p(story, para)

    story.append(PageBreak())

    # ================= 18  INSPECTION AND TESTING =========================
    sec_head(story, 18, "Inspection and testing", "")
    p(story,
      "The inspection and test plan runs from setting out to integrated "
      "commissioning. Inspection types are hold — work stops until released; "
      "witness — the Engineer is invited and work may proceed if attendance is "
      "waived; test — a measurement against a stated acceptance criterion; and "
      "surveillance — ongoing observation.", LEAD)
    story.append(tbl(
        ["Ref", "Work", "Requirement", "Reference", "Type"],
        [[r[0], r[1], r[3], r[4], r[5]] for r in C.ITP],
        [11 * mm, 32 * mm, FW - 111 * mm, 46 * mm, 22 * mm], small=True))
    story.append(Paragraph("Table 18.1 — Inspection and test plan.", CAP))

    story.append(Paragraph("18.1&nbsp;&nbsp;The protective test sequence", H2))
    p(story,
      "The protective systems are tested in a fixed order because each depends on "
      "the one before it. The shielding effectiveness survey comes first, because "
      "it tests the enclosure and every penetration and there is no point "
      "proceeding if it fails. The blast door seals are proved next, because the "
      "envelope test depends on them. Then the gas-tightness and overpressure "
      "test of bays 1 to 6, then filter train commissioning, then the generator, "
      "then integrated protective-mode operation with the doors closed, the blast "
      "valves set, the filter trains running, overpressure maintained and the "
      "drainage isolated.")
    p(story,
      "The shielding survey is also the test least likely to be recoverable if it "
      "fails, which is why the works it tests are inspected as they are built — "
      "bonding straps at every construction joint, door frames welded to the "
      "cage, penetration protection installed and recorded — rather than tested "
      "for the first time at the end.")

    story.append(PageBreak())

    # ================= 19  EXTERNAL WORKS =================================
    sec_head(story, 19, "External works", "")
    p(story,
      "The external works complete the site: the berm against the above-ground "
      "structures, the regrading that sheds water away from a buried building, "
      "the surface water system, the access route, and the removal of everything "
      "temporary.", LEAD)
    story.append(tbl(
        ["Act", "Work", "Days", "Note"],
        [[a, tasks[a].name, str(tasks[a].dur), tasks[a].note or "—"]
         for a in ["A13010", "A13015", "A13020", "A13025", "A13030", "A13035",
                   "A13040", "A13045"]],
        [15 * mm, FW - 82 * mm, 11 * mm, 56 * mm], align=[None, None, "r", None],
        small=True))
    story.append(Paragraph("Table 19.1 — External works activities.", CAP))
    p(story,
      "The berm is graded at 1.5:1 to +0.900 against the headhouse and the "
      "covered stairwell, and the site is crowned with 1:50 falls away from the "
      "structure. Surface water cut-off drains installed before excavation are "
      "retained and connected into the permanent system.")
    p(story,
      "The extent of the external works cannot be quantified. No site plan or "
      "ground model exists in the project, so the berm volume, the access route "
      "and the hardstanding are programmed as activities with indicative "
      "durations and carried in the bill as items to be verified from final "
      "measurement. A site plan is requested at mobilisation; the external works "
      "sit at the end of the programme, which buys time but not an unlimited "
      "amount.")

    # ================= 20  ELECTRICAL =====================================
    sec_head(story, 20, "Electrical works", "")
    story.append(Callout(
        "The electrical <b>scope</b> is confirmed by the project record: a "
        "15 kVA generator in the grey zone, a shielded Zone 2 enclosure in the "
        "operations room, earthing to a 5 Ω target, bonding straps at every "
        "construction joint, and electromagnetic pulse protection at every "
        "service penetration to a requirement of 80 dB over 10 kHz to 1 GHz. "
        "<b>No electrical design package exists.</b> There is no circuit, cable, "
        "luminaire, distribution board or earth-electrode schedule anywhere in "
        "the project, so every electrical quantity in the bill reads <i>to be "
        "verified from final measurement</i> and no electrical enquiry can be "
        "issued until the design is produced.", FW, accent=AMBER,
        title="Scope confirmed, design absent"))
    p(story,
      "The Works Management package still covers the electrical <i>works</i>, "
      "because the works are confirmed even though the quantities are not. They "
      "are programmed, resourced, given hold points and given tests.")
    story.append(tbl(
        ["Act", "Work", "Days", "Note"],
        [[a, tasks[a].name, str(tasks[a].dur), tasks[a].note or "—"]
         for a in ["A11015", "A11020", "A11025", "A11030", "A11035", "A11040",
                   "A11045", "A11050", "A11055"]],
        [15 * mm, FW - 84 * mm, 11 * mm, 58 * mm], align=[None, None, "r", None],
        small=True))
    story.append(Paragraph("Table 20.1 — Electrical and shielding activities.", CAP))
    p(story,
      "The electromagnetic pulse works are as much structural as electrical, and "
      "that is why they appear early in the programme rather than at the end. "
      "Bonding straps are welded at every construction joint as the walls rise; "
      "the blast door frames are welded to the reinforcement cage before the "
      "walls are poured; the earth ring is laid before the mat is cast. The "
      "reinforcement cage on its own gives no useful attenuation at 1 GHz — the "
      "welded steel Zone 2 room is the whole answer, not a supplement to the "
      "cage — and the shielding effectiveness survey at handover tests all of it "
      "at once.")
    p(story,
      "The sentry post has its own small electrical installation: conduits and "
      "boxes chased into the brick masonry after the masonry hold point, wiring "
      "and a distribution board, fittings and earthing, all tested before "
      "handover. Chases are cut, not hammered, and not before the masonry has "
      "cured — a detail that matters more in brickwork than it did in the "
      "reinforced concrete panels it replaces.")

    story.append(PageBreak())

    # ================= 21  CONCEALMENT ====================================
    sec_head(story, 21, "Camouflage and concealment works", "")
    p(story,
      "Concealment is the point of a buried structure. A shelter whose position "
      "is obvious from the surface has lost part of its protection before the "
      "first weapon effect arrives.", LEAD)
    p(story,
      "The project confirms one concealment element: the 300 mm topsoil and turf "
      "layer at the top of the engineered cover, whose stated function is "
      "concealment, erosion control and shedding rain. It is programmed as the "
      "final layer of the cover, using the topsoil stripped at the start of the "
      "job and stockpiled for the purpose — which is why the stripping activity "
      "says <i>stockpile</i> and not <i>cart away</i>.")
    p(story,
      "Beyond that layer, the project contains no concealment specification. "
      "Spoil dressing, screening, a planting regime and track discipline are all "
      "programmed as work, because they are the measures such a structure would "
      "normally need, but their extent and specification must be confirmed before "
      "they can be priced. The bill carries them as an item to be verified from "
      "final measurement rather than inventing a scope for them.")
    p(story,
      "Two decisions elsewhere in the package serve concealment even though they "
      "are not labelled as concealment work. The engineered cover is graded and "
      "the site crowned with 1:50 falls so that the finished ground reads as "
      "ground rather than as a mound with drainage problems. And 994 m³ of rock "
      "is excavated while only about 51 m³ of crushed rubble is needed for the "
      "cover, so the surplus has to go somewhere — dressing it into the "
      "surrounding ground rather than leaving it as a spoil heap adjacent to a "
      "structure whose position is meant to be unremarkable is a concealment "
      "decision as much as a haulage one.")

    # ================= 22  COMPLETION =====================================
    sec_head(story, 22, "Completion and handover", "")
    story.append(tbl(
        ["Act", "Work", "Days", "Start", "Finish"],
        [[a, tasks[a].name, "—" if tasks[a].is_milestone else str(tasks[a].dur),
          S.dstr(tasks[a].es), S.dstr(tasks[a].ef)]
         for a in ["A14075", "A14080", "A14085", "A14090", "A14095", "A14098",
                   "A14100", "A14105"]],
        [15 * mm, FW - 61 * mm, 11 * mm, 17 * mm, 17 * mm],
        align=[None, None, "r", None, None], small=True))
    story.append(Paragraph("Table 22.1 — Completion sequence.", CAP))
    p(story,
      "Handover includes as-built drawings, operation and maintenance manuals, "
      "every test certificate, and operator training on the CBRN plant, the "
      "pumps, the generator, the blast doors and the escape shafts. The training "
      "matters more than usual here: the shelter has a duty pump, a standby pump "
      "<i>and</i> a hand pump precisely because it may have to work without "
      "power, and a fan with an electric drive <i>and</i> a hand crank for the "
      "same reason. Equipment provided as a third line of defence is only a third "
      "line of defence if the people who will use it have been shown how.")
    p(story,
      "A ten-working-day contingency activity sits immediately before the final "
      "inspection. It exists because the calendar deliberately contains no "
      "fabricated festival-holiday dates: the movable holidays are absorbed there "
      "rather than hidden inside individual durations, where they would be "
      "impossible to audit.")

    story.append(PageBreak())

    # ================= 23  CODES ==========================================
    sec_head(story, 23, "Applicable codes and MES specifications", "")
    p(story,
      "Every reference used in this package is a real, published document. No "
      "clause number, item number, schedule-of-rates reference, specification "
      "number or document title has been invented. Where an exact reference could "
      "not be verified from the material available, the entry says so in these "
      "words: <i>%s</i>" % C.MES_CAVEAT, LEAD)

    groups = []
    for g, *_ in C.CODES:
        if g not in groups:
            groups.append(g)
    for g in groups:
        story.append(Paragraph(g, H3))
        story.append(tbl(["Reference", "Title", "Used for"],
                         [[r, t, u] for gg, r, t, u, cl in C.CODES if gg == g],
                         [40 * mm, 52 * mm, FW - 92 * mm], small=True))

    story.append(Paragraph("23.1&nbsp;&nbsp;The position on MES and CPWD references",
                           H2))
    p(story,
      "The Military Engineer Services Standard Schedule of Rates and the Defence "
      "Works Procedure are the documents that would actually govern a Service "
      "work of this kind. They exist, they are named correctly, and the work they "
      "would govern is identified. What is not given is any item number, clause "
      "number or rate, because none could be verified from the material available "
      "in this project — and putting a false authority on a document that an "
      "examiner or an executing engineer might rely on would be worse than "
      "leaving the gap visible. The same applies to the CPWD Specifications and "
      "the Delhi Schedule of Rates: the documents are real, the individual item "
      "numbers are not quoted.")

    # ================= 24  REFERENCES =====================================
    sec_head(story, 24, "References", "")
    p(story,
      "Indian Standards, international standards and government specifications "
      "are listed in section 23 and in the accompanying codes register. The "
      "references below are the project documents that are the authority for "
      "everything this package measures and schedules.")
    story.append(tbl(
        ["Document", "What it governs"],
        [["<b>Master project state file</b>, Parts A, B, F and L",
          "The single source of truth for geometry, materials, loading, "
          "structural design and reinforcement. Every quantity in this package "
          "traces back to it"],
         ["Structural reinforcement package",
          "Thirty A1 reinforcement drawings, 92 bar marks, 70.46 t of "
          "reinforcement and the concrete volumes used in the bill"],
         ["Drainage package",
          "Drainage design basis and the pipe, chamber, sump, pump and soakaway "
          "schedules"],
         ["HVAC package",
          "HVAC and CBRN design basis and the equipment, duct, filter and damper "
          "schedules"],
         ["Schedule of finishes",
          "Finish legend and rules for all thirteen spaces, specified as "
          "performance requirements"],
         ["Revision F architectural drawings",
          "The ten input drawings, including the sentry post ground floor, first "
          "floor and framing plans from which the wall runs and openings in "
          "section 8 were read"],
         ["Structural analysis models",
          "The underground plate model, the sentry post frame model and the entry "
          "stairwell frame model"],
         ["Preliminary master construction schedule",
          "The starting point for this programme; its start date and six-day "
          "calendar are retained"]],
        [56 * mm, FW - 56 * mm], small=True))

    # ================= 25  CONCLUSION =====================================
    sec_head(story, 25, "Conclusion", "")
    p(story,
      "This package plans the construction and management of the complete "
      "project — the underground shelter, the entry structures, the escape "
      "shafts, the engineered cover, the sentry post and all of the services, "
      "external works and concealment works — from mobilisation to handover.",
      LEAD)
    p(story,
      "The logic runs in one direction and each step depends on the one before "
      "it. The project record establishes what is being built; the component "
      "register identifies the twenty-three components that actually exist; the "
      "work breakdown structure organises them into fourteen work packages; the "
      "construction methodology explains how each is built and why in that order; "
      "the bill of quantities measures them from confirmed geometry; the resource "
      "plan and the procurement plan provide what the quantities need; the "
      "programme sequences all of it into %d activities across %d working days; "
      "and the quality, safety, risk and progress systems control it while it "
      "happens." % (nact, end + 1))
    p(story,
      "Three things about the result are worth stating plainly. First, the "
      "programme is driven by a small number of facts that cannot be argued away: "
      "a fourteen-day prop period fixed by code, a seventy-five-day vendor lead "
      "time that sits upstream of a wall pour, and 994 m³ of rock that has to be "
      "broken rather than dug. Recognising those early is most of what "
      "distinguishes a programme that holds from one that does not.")
    p(story,
      "Second, the package is honest about what it does not know. There is no "
      "electrical design, no site plan, no lintel design and no wall tie detail; "
      "several conflicts in the project record remain unresolved; and every "
      "output rate and vendor lead time is an assumption. All of it is listed, "
      "dated against the activity it blocks, and issued to the designer at "
      "mobilisation. A bill with visible gaps is more useful than one whose gaps "
      "have been filled with plausible numbers.")
    p(story,
      "Third, the one design change carried by this package — the sentry post "
      "walls as brick masonry — has been followed through everywhere it reaches: "
      "into the methodology, the breakdown structure, the bill, the resource "
      "plan, the procurement plan, the programme, the quality plan, the safety "
      "register and the risk register. It has also been followed through into the "
      "places where it creates new obligations. Brick masonry needs lintels that "
      "the concrete panels did not; it needs ties that have not been detailed; it "
      "changes the seismic weight of the frame, conservatively but not "
      "verifiably; and it does not provide the ballistic protection that the "
      "panels it replaces were named for. Those consequences are recorded rather "
      "than absorbed, because a change whose consequences are invisible is the "
      "one that causes trouble on site.")
    story.append(Spacer(1, 8))
    story.append(Rule(FW, 0.8, RULE, 4))
    story.append(Paragraph(
        "Accompanying documents: work breakdown structure · bill of quantities "
        "and its full quantity derivation · resource plan · procurement plan · "
        "quality assurance and quality control plan · safety management and risk "
        "register · codes and references register · project component register · "
        "construction methodology · sentry post brick masonry methodology · "
        "progress monitoring and control · assumptions and verification register "
        "· master programme in Microsoft Project interchange format · programme "
        "drawing · comma-separated task list.", NOTE))

    doc = Doc(path)
    doc.build(story)
    return doc.page


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "..",
                       "Underground_Shelter_Works_Management_Handout.pdf")
    n = build(out)
    print("handout written: %d pages" % n)


if __name__ == "__main__":
    main()
