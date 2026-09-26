"""
report_frontmatter.py -- the College of Military Engineering front matter.

Underground CBRN-hardened blast-resistant protective structure + sentry post, Pune.
Project Report package, revision PR3.

Drawn to the format of the CME project report the owner photographed and
supplied on 26 Sep 2026:

    HARD COVER        black board, gold lettering, gold frame and the crest
    CERTIFICATE       page i  (the number is counted, not printed)
    APPROVAL SHEET    page ii
    DECLARATION       page iii
    ACKNOWLEDGEMENT   page iv

report_render.py places them with the <!-- HARDCOVER --> and
<!-- FRONTMATTER --> directives.  This module holds WORDS AND LAYOUT ONLY: no
design value, no number from the master and nothing the renderer typesets
elsewhere.

EVERY PARTICULAR IS IN `FM` BELOW, AND ONLY THERE.  A particular the owner has
not supplied is None or an empty list, and it prints as a RED BRACKETED
PLACEHOLDER -- never as a guess -- so a page carrying one cannot be mistaken for
a finished page.  The renderer lists every placeholder still on the pages each
time it builds.  To finish the pages, fill in `FM` and re-run the renderer.
"""

import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Flowable, Paragraph, Table, TableStyle
from reportlab.platypus import Image as RLImage

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.abspath(os.path.join(HERE, "..", "Assets"))
CREST_GOLD = os.path.join(ASSETS, "crest_gold.png")
CREST_COLOUR = os.path.join(ASSETS, "crest_colour.png")

# =============================================================================
# THE PARTICULARS -- the only place any of them is written
# =============================================================================
FM = {
    "college": "College of Military Engineering",
    "college_place": "Pune",
    "college_short": "CME",
    "college_pin": "Pune-411031",
    "faculty": "Faculty of Civil Engineering",

    # The owner's registered project title is NOT held in the project.  This is
    # master A.1's confirmed title, set in the CME cover format
    # ("PLANNING AND DESIGN OF ...").  Change it here and every page follows.
    "title": "PLANNING AND DESIGN OF AN UNDERGROUND CBRN-HARDENED, "
             "BLAST-RESISTANT PROTECTIVE STRUCTURE WITH SENTRY POST AT PUNE",

    # --- supplied by the owner, 26 Sep 2026 -------------------------------
    "guides": ["Maj Ashish Dubey, FGS",
               "Dr IR Chaudhuri",
               "Dr Uttam Awari",
               "Lt Col APS Chauhan",
               "Sh Tilak Sharma, Jt Dir (C), FCM"],

    # --- NOT YET SUPPLIED -- each prints as a red placeholder --------------
    "syndicate": None,       # e.g. "03"
    "members": [],           # rank and name, in the order to be printed
    "leader": None,          # rank and name of the syndicate leader
    "leader_no": None,       # the leader's CME/EODE number, e.g. "128"
    "date": None,            # month and year of submission, e.g. "Oct 2026"

    # The degree as the owner's CME format states it.  Master A.1 records
    # "B.E. Civil Engineering" [CONFIRMED]; the CME pages supplied say
    # "Bachelor of Technology (Civil) ... affiliated to the Jawaharlal Nehru
    # University, New Delhi".  The two disagree, so until the owner confirms
    # which is right the wording prints in RED.  Set True once confirmed.
    "degree": "Bachelor of Technology (Civil)",
    "university": "Jawaharlal Nehru University",
    "university_place": "New Delhi",
    "degree_confirmed": False,

    # Thanked by appointment.  A name, when supplied, is printed in front of
    # the appointment; with no name the appointment stands alone, and that is
    # not a placeholder -- it is a complete sentence either way.
    "officials": [
        # (appointment, name or None, what they are thanked for)
        ("Commander, Faculty of Civil Engineering, CME, Pune", None,
         "for extending all the support during the course"),
        ("Dean and Deputy Commandant, CME, Pune", None,
         "for the constant inspiration and encouragement"),
        ("Commandant, CME, Pune", None,
         "for providing us, the student officers' fraternity, with constant "
         "support and the infrastructure that makes a conducive academic "
         "environment in which to complete this project"),
    ],
}

# =============================================================================
# colours and faces
# =============================================================================
BOARD = colors.Color(0.063, 0.063, 0.071)       # the black hard cover
GOLD = colors.Color(0.925, 0.757, 0.231)        # its lettering and frame
CME_RED = colors.Color(0.690, 0.110, 0.125)     # the red headings inside
INK = colors.Color(0.05, 0.05, 0.06)
PENDING_INK = "#C8102E"                          # a placeholder, inner pages
PENDING_ON_BOARD = "#FF7A6B"                     # a placeholder, on the board

SERIF_DIR = "/usr/share/fonts/truetype/liberation"
FACES = [("FMSerif", "LiberationSerif-Regular.ttf"),
         ("FMSerif-Bold", "LiberationSerif-Bold.ttf"),
         ("FMSerif-Italic", "LiberationSerif-Italic.ttf"),
         ("FMSerif-BoldItalic", "LiberationSerif-BoldItalic.ttf"),
         ("FMSans-Bold", "LiberationSans-Bold.ttf")]


def register_fonts():
    for name, fn in FACES:
        path = os.path.join(SERIF_DIR, fn)
        if not os.path.exists(path):
            raise SystemExit("font not found: " + path)
        pdfmetrics.registerFont(TTFont(name, path))
    pdfmetrics.registerFontFamily("FMSerif", normal="FMSerif",
                                  bold="FMSerif-Bold",
                                  italic="FMSerif-Italic",
                                  boldItalic="FMSerif-BoldItalic")


# =============================================================================
# placeholders -- recorded so the renderer can report what is still missing
# =============================================================================
PENDING = []


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def pending(label, ink=PENDING_INK):
    if label not in PENDING:
        PENDING.append(label)
    return '<font color="%s">[%s]</font>' % (ink, esc(label))


def val(key, label, ink=PENDING_INK):
    v = FM.get(key)
    return esc(v) if v else pending(label, ink)


def degree_text(s):
    """The degree wording, in red until the owner confirms it."""
    if FM["degree_confirmed"]:
        return esc(s)
    if "degree wording (B.Tech/JNU or B.E.)" not in PENDING:
        PENDING.append("degree wording (B.Tech/JNU or B.E.)")
    return '<font color="%s">%s</font>' % (PENDING_INK, esc(s))


WORDS = ["", "one", "two", "three", "four", "five", "six", "seven", "eight",
         "nine", "ten", "eleven", "twelve"]


# =============================================================================
# styles
# =============================================================================
def S(name, **kw):
    base = dict(fontName="FMSerif", fontSize=12.5, leading=17,
                textColor=INK, alignment=TA_CENTER)
    base.update(kw)
    return ParagraphStyle(name, **base)


ST = {}


def styles():
    ST["head"] = S("head", fontName="FMSerif-Bold", fontSize=15.5, leading=19)
    ST["red"] = S("red", fontName="FMSerif-Bold", fontSize=13,
                  leading=17, textColor=CME_RED)
    ST["redtitle"] = S("redtitle", fontName="FMSerif-Bold", fontSize=14,
                       leading=17.5, textColor=CME_RED)
    ST["c"] = S("c", fontSize=12.5, leading=16)
    ST["cloose"] = S("cloose", fontSize=12.5, leading=23)
    ST["just"] = S("just", fontSize=12.5, leading=25, alignment=TA_JUSTIFY)
    ST["ack"] = S("ack", fontSize=12, leading=23.5, alignment=TA_JUSTIFY,
                  firstLineIndent=12 * mm, spaceAfter=0)
    ST["colhead"] = S("colhead", fontName="FMSerif-Bold", fontSize=12,
                      leading=16, alignment=TA_LEFT)
    ST["colitem"] = S("colitem", fontName="FMSerif-Bold", fontSize=12,
                      leading=16.5, alignment=TA_LEFT)
    ST["l"] = S("l", fontSize=12.5, leading=17, alignment=TA_LEFT)
    ST["lb"] = S("lb", fontName="FMSerif-Bold", fontSize=12.5, leading=17,
                 alignment=TA_LEFT)
    ST["sig"] = S("sig", fontSize=12.5, leading=17.5, alignment=TA_LEFT)


# =============================================================================
# building blocks
# =============================================================================
class HLine(Flowable):
    """A rule of a given length -- a signature line."""

    def __init__(self, length, th=0.7):
        Flowable.__init__(self)
        self.length, self.th = length, th

    def wrap(self, aw, ah):
        return self.length, self.th + 1

    def draw(self):
        self.canv.setLineWidth(self.th)
        self.canv.setStrokeColor(INK)
        self.canv.line(0, 0.5, self.length, 0.5)


def crest(path, width):
    from PIL import Image as PILImage          # Pillow ships with reportlab
    w, h = PILImage.open(path).size
    img = RLImage(path, width=width, height=width * h / float(w),
                  mask="auto")
    return img


def two_columns(left, right, width, split=0.47):
    """Two column blocks side by side, each a list of flowables."""
    t = Table([[left, right]],
              colWidths=[width * split, width * (1 - split)])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return t


class Sheet(Flowable):
    """One whole formal page.  `items` are stacked top to bottom; the space
    left over is shared out among the gaps in proportion to each item's
    weight, so a longer list of names closes the gaps rather than pushing the
    date off the page.  An item is (flowable, gap_weight, align, min_gap)."""

    def __init__(self, width, height, items, name):
        Flowable.__init__(self)
        self.width, self.height, self.items, self.name = \
            width, height, items, name

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        placed = []
        for f, weight, align, mingap in self.items:
            w, h = f.wrapOn(c, self.width, self.height)
            placed.append((f, w, h, weight, align, mingap))
        used = sum(p[2] for p in placed) + sum(p[5] for p in placed)
        free = self.height - used
        if free < 0:
            OVERFLOW.append((self.name, -free / mm))
            free = 0
        wsum = sum(p[3] for p in placed) or 1
        y = self.height
        for f, w, h, weight, align, mingap in placed:
            y -= mingap + free * weight / wsum
            y -= h
            x = {"left": 0, "center": (self.width - w) / 2.0,
                 "right": self.width - w}[align]
            f.drawOn(c, x, y)


OVERFLOW = []


def P(markup, style):
    return Paragraph(markup, ST[style])


def it(f, weight=0.0, align="center", mingap=0.0):
    return (f, weight, align, mingap)


# =============================================================================
# the pages
# =============================================================================
def members_markup(numbered=True, ink=PENDING_INK):
    ms = FM["members"]
    if not ms:
        return [pending("syndicate members — rank and name", ink)]
    return [("%d. %s" % (i, esc(m)) if numbered else esc(m))
            for i, m in enumerate(ms, 1)]


def date_place(width, blank_day=False):
    d = ("_____ " if blank_day else "") + (esc(FM["date"]) if FM["date"]
                                           else pending("month and year"))
    rows = [[P("Date:", "lb"), P(d, "l")],
            [P("Place:", "lb"), P("%s %s" % (FM["college_short"],
                                             FM["college_place"]), "l")]]
    t = Table(rows, colWidths=[28 * mm, width - 28 * mm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10)]))
    return t


def certificate(W, H):
    syn = val("syndicate", "syndicate no.")
    n = len(FM["members"])
    count = WORDS[n] if 0 < n < len(WORDS) else (str(n) if n else
                                                  pending("number of officers"))
    body = (
        "This is to certify that the project entitled "
        "‘<b>%s</b>’ submitted by %s officers of Syndicate %s, in "
        "partial fulfilment of the requirements for the award of the degree "
        "of %s of the %s, %s, affiliated to the %s, %s, is a record of their "
        "own work."
        % (esc(FM["title"]), count, syn, degree_text(FM["degree"]),
           esc(FM["college"]), esc(FM["college_place"]),
           degree_text(FM["university"]), esc(FM["university_place"])))
    left = [P("SYNDICATE NO. %s" % syn, "colhead")]
    left += [P(m, "colitem") for m in members_markup()]
    right = [P("GUIDES :-", "colhead")]
    right += [P("%d. %s" % (i, esc(g)), "colitem")
              for i, g in enumerate(FM["guides"], 1)]
    items = [
        it(P("<u>CERTIFICATE</u>", "head"), 0, "center", 2 * mm),
        it(P("%s, %s" % (FM["college"].upper(), FM["college_place"].upper()),
             "red"), 0.6, "center", 5 * mm),
        it(crest(CREST_COLOUR, 30 * mm), 0.8, "center", 6 * mm),
        it(P(body, "just"), 1.4, "center", 10 * mm),
        it(two_columns(left, right, W - 8 * mm, 0.46), 1.6, "right",
           10 * mm),
        it(date_place(W * 0.6, blank_day=True), 1.6, "left", 10 * mm),
    ]
    return Sheet(W, H, items, "certificate")


def approval(W, H):
    syn = val("syndicate", "syndicate no.")
    ex = Table(
        [[P("Examiners", "lb"), P("Name", "lb"), P("Signatures", "lb")],
         [P("1.&nbsp;&nbsp;&nbsp;&nbsp;External Examiner", "l"),
          HLine(W * 0.62), ""],
         [P("2.&nbsp;&nbsp;&nbsp;&nbsp;Guide", "l"), HLine(W * 0.62), ""]],
        colWidths=[W * 0.36, W * 0.32, W * 0.32],
        rowHeights=[9 * mm, 12 * mm, 12 * mm])
    ex.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
        ("SPAN", (1, 1), (2, 1)), ("SPAN", (1, 2), (2, 2)),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
    members = "<br/>".join(members_markup())
    degree_block = "<br/>".join([
        "is Approved for the Degree of",
        degree_text(FM["degree"]),
        "of",
        degree_text(FM["university"]),
        "at",
        esc(FM["faculty"]),
        "%s, %s" % (esc(FM["college"]), esc(FM["college_place"]))])
    items = [
        it(P("<u>APPROVAL SHEET</u>", "head"), 0, "center", 2 * mm),
        it(crest(CREST_COLOUR, 27 * mm), 0.7, "center", 5 * mm),
        it(P("This Project Entitled", "c"), 0.7, "center", 5 * mm),
        it(P("“%s”" % esc(FM["title"]), "redtitle"), 0.4,
           "center", 3 * mm),
        it(P("by", "c"), 0.5, "center", 3 * mm),
        it(P("SYNDICATE NO. %s" % syn, "red"), 0.5, "center", 3 * mm),
        it(P(members, "c"), 0.4, "center", 2 * mm),
        it(P(degree_block, "cloose"), 0.9, "center", 5 * mm),
        it(ex, 1.2, "center", 6 * mm),
        it(date_place(W * 0.6), 1.0, "left", 8 * mm),
    ]
    return Sheet(W, H, items, "approval sheet")


DECLARATION = (
    "I declare that this written submission represents our ideas in our own "
    "words and where others' ideas or words have been included, I have "
    "adequately cited and referenced the original sources. I also declare "
    "that we have adhered to all principles of academic honesty and integrity "
    "and have not misrepresented or fabricated or falsified any "
    "idea/data/fact/source in our submission. I understand that any violation "
    "of the above will be cause for disciplinary action by the Institute and "
    "can also evoke penal action from the sources which have thus not been "
    "properly cited or from whom proper permission has not been taken when "
    "needed.")


def signature_block(lines, width, rule=True):
    fl = []
    if rule:
        fl.append(HLine(width * 0.95))
        fl.append(Spacer_(5 * mm))
    fl += [P(ln, "sig") for ln in lines]
    t = Table([[f] for f in fl], colWidths=[width])
    t.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return t


class Spacer_(Flowable):
    def __init__(self, h):
        Flowable.__init__(self)
        self.h = h

    def wrap(self, aw, ah):
        return 1, self.h

    def draw(self):
        pass


def declaration(W, H):
    syn = val("syndicate", "syndicate no.")
    sig = signature_block([
        val("leader", "syndicate leader — rank and name"),
        "CME/EODE %s" % val("leader_no", "leader's EODE No."),
        "Syndicate Leader",
        "(on behalf of Syndicate %s)" % syn], W * 0.5)
    items = [
        it(P("<u>DECLARATION</u>", "head"), 0, "center", 2 * mm),
        it(P(DECLARATION, "just"), 0.25, "center", 12 * mm),
        it(sig, 1.0, "right", 30 * mm),
        it(date_place(W * 0.6), 0.9, "left", 20 * mm),
        it(Spacer_(1), 0.7, "left", 0),
    ]
    return Sheet(W, H, items, "declaration")


def acknowledgement(W, H):
    syn = val("syndicate", "syndicate no.")
    gs = ["<b>%s</b>" % esc(g) for g in FM["guides"]]
    guides = (", ".join(gs[:-1]) + " and " + gs[-1]) if len(gs) > 1 else gs[0]
    paras = [
        "It is indeed difficult to express in words the gratitude we feel "
        "for the help we received from all those who stood by us like pillars "
        "in this endeavour. Nevertheless, we attempt here to record our "
        "heartfelt sense of gratitude.",
        "We sincerely express our deep sense of gratitude to our guides, %s, "
        "for their expert and valuable guidance, advice, encouragement, "
        "patience and help all through this project work." % guides,
    ]
    lead = ["We extend our sincere thanks to",
            "We are also thankful to",
            "We are grateful to"]
    for k, (post, name, why) in enumerate(FM["officials"]):
        who = ("<b>%s</b>, %s" % (esc(name), esc(post)) if name
               else "the <b>%s</b>" % esc(post))
        paras.append("%s %s, %s." % (lead[min(k, len(lead) - 1)], who,
                                     esc(why)))
    paras.append(
        "We are thankful to all the <b>Instructors</b> and <b>Professors</b> "
        "of the %s for sharing with us their invaluable knowledge and for "
        "shaping vague thoughts and ideas on the subject into a logical end. "
        "We would also like to thank the <b>library</b> and the "
        "<b>administrative staff</b> for their cordial support and the "
        "facilities that were of great help in preparing this report."
        % esc(FM["faculty"]))
    sig = signature_block([
        val("leader", "syndicate leader — rank and name"),
        "EODE-%s" % val("leader_no", "leader's EODE No."),
        "Syndicate Leader",
        "(On behalf of Syndicate %s)" % syn,
        "%s, %s" % (FM["college_short"], FM["college_pin"])], W * 0.5,
        rule=False)
    items = [it(P("<u>ACKNOWLEDGEMENT</u>", "head"), 0, "center", 2 * mm)]
    for i, p in enumerate(paras):
        items.append(it(P(p, "ack"), 0.15 if i else 0.3, "center",
                        (9 if i == 0 else 2) * mm))
    items.append(it(sig, 1.0, "right", 16 * mm))
    items.append(it(Spacer_(1), 0.25, "left", 0))
    return Sheet(W, H, items, "acknowledgement")


# =============================================================================
# the hard cover -- drawn straight onto the canvas, to the photographed board
# =============================================================================
def _fit(text, font, size, width, floor):
    while size > floor and pdfmetrics.stringWidth(text, font, size) > width:
        size -= 0.25
    return size


def _wrap(text, font, size, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if pdfmetrics.stringWidth(t, font, size) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def _gold_line(c, text, font, size, x, y, center=True, underline=True,
               ink=GOLD):
    c.setFont(font, size)
    c.setFillColor(ink)
    w = pdfmetrics.stringWidth(text, font, size)
    x0 = x - w / 2.0 if center else x
    c.drawString(x0, y, text)
    if underline:
        c.setStrokeColor(ink)
        c.setLineWidth(max(0.6, size * 0.06))
        c.line(x0, y - size * 0.14, x0 + w, y - size * 0.14)
    return w


def draw_hardcover(c, PW, PH):
    """The board.  Positions are taken off the owner's photograph of a CME
    hard cover:  gold frame inset about 23 mm at the sides, 40 mm at the head
    and 36 mm at the tail;  institution, crest, PROJECT REPORT, title, then the
    syndicate and the guides in two columns."""
    font = "FMSans-Bold"
    c.saveState()
    c.setFillColor(BOARD)
    c.rect(0, 0, PW, PH, stroke=0, fill=1)

    fx0, fx1 = 23 * mm, PW - 23 * mm
    fy0, fy1 = 36 * mm, PH - 40 * mm
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.8)
    c.rect(fx0, fy0, fx1 - fx0, fy1 - fy0, stroke=1, fill=0)
    c.setLineWidth(0.5)
    g = 1.6 * mm
    c.rect(fx0 + g, fy0 + g, fx1 - fx0 - 2 * g, fy1 - fy0 - 2 * g,
           stroke=1, fill=0)

    cx = PW / 2.0
    inner = fx1 - fx0 - 16 * mm
    head = FM["college"].upper()
    _gold_line(c, head, font, _fit(head, font, 17.5, inner, 12), cx,
               fy1 - 13 * mm)

    cw = 43 * mm
    from PIL import Image as PILImage
    iw, ih = PILImage.open(CREST_GOLD).size
    ch = cw * ih / float(iw)
    ctop = fy1 - 32 * mm
    c.drawImage(CREST_GOLD, cx - cw / 2.0, ctop - ch, cw, ch, mask="auto")

    y = ctop - ch - 15 * mm
    _gold_line(c, "PROJECT REPORT", font, 21, cx, y)

    tsize = 13.2
    lines = _wrap(FM["title"].upper(), font, tsize, inner)
    y -= 22 * mm
    for ln in lines:
        _gold_line(c, ln, font, tsize, cx, y)
        y -= 7.4 * mm

    # two columns: the syndicate at left, the guides at right
    y -= 9 * mm
    lx, rx = fx0 + 10 * mm, cx + 8 * mm
    colw_l, colw_r = cx - lx - 4 * mm, fx1 - 7 * mm - rx
    syn = FM["syndicate"]
    lhead = "SYNDICATE NO %s" % syn if syn else "SYNDICATE NO"
    _gold_line(c, lhead, font, 12.5, lx, y, center=False)
    if not syn:
        w = pdfmetrics.stringWidth(lhead + " ", font, 12.5)
        _pending_label(c, "syndicate no.", lx + w, y, 11)
    _gold_line(c, "GUIDES", font, 12.5, rx, y, center=False)

    names = [m.upper() for m in FM["members"]]
    guides = [g_.upper() for g_ in FM["guides"]]
    size = min(12.0,
               min([_fit(n, font, 12.0, colw_l, 8.5) for n in names] or [12]),
               min([_fit(n, font, 12.0, colw_r, 8.5) for n in guides] or [12]))
    rows = max(len(names) or 1, len(guides))
    pitch = min(8.2 * mm, (y - fy0 - 12 * mm) / float(rows))
    yy = y - 10 * mm
    for n in names:
        _gold_line(c, n, font, size, lx, yy, center=False, underline=False)
        yy -= pitch
    if not names:
        _pending_label(c, "syndicate members \u2014 rank and name", lx, yy,
                       10)
    yy = y - 10 * mm
    for n in guides:
        _gold_line(c, n, font, size, rx, yy, center=False, underline=False)
        yy -= pitch
    c.restoreState()


def _pending_label(c, label, x, y, size):
    pending(label)
    c.setFont("FMSans-Bold", size)
    c.setFillColor(colors.HexColor(PENDING_ON_BOARD))
    c.drawString(x, y, "[%s]" % label)


class HardCover(Flowable):
    """Fills its page-sized frame and draws the board on it."""

    def __init__(self, PW, PH):
        Flowable.__init__(self)
        self.PW, self.PH = PW, PH

    def wrap(self, aw, ah):
        return aw, ah

    def draw(self):
        c = self.canv
        c.saveState()
        # the frame has no margin, so the flowable origin is the page origin
        draw_hardcover(c, self.PW, self.PH)
        c.restoreState()


def front_pages(W, H):
    """The four formal pages, in order."""
    return [certificate(W, H), approval(W, H), declaration(W, H),
            acknowledgement(W, H)]


def setup():
    register_fonts()
    styles()
    del PENDING[:]
    del OVERFLOW[:]
