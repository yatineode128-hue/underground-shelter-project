"""
sc_views.py  --  reusable view builders shared by the R-series generators.
Geometry comes from sc_proj.py; bar marks come from rebar_data.py.
"""
import math
import sc_proj as P
import sc_dxflib as D
import rebar_data as R

MARK = {m["mark"]: m for m in R.MARKS}

# standard sheet layout zones (paper mm)
MAIN = dict(x0=16, x1=640, y0=118, y1=556)
RCOL = dict(x0=648, x1=831, y0=118, y1=556)
BOTL = dict(x0=16, x1=643, y0=14, y1=112)


def label(mark):
    """Annotation text for a bar mark, taken from the schedule - never typed twice."""
    m = MARK[mark]
    sp = f" @ {m['spacing']}" if m["spacing"] else ""
    return f"T{m['phi']}{sp}"


def note_for(mark):
    m = MARK[mark]
    sp = f" @ {m['spacing']}" if m["spacing"] else ""
    return f"{mark}  T{m['phi']}{sp}  {m['location']}"


# --------------------------------------------------------------- box outline
def box_plan(sh, Pm, scale, show_bays=True, show_openings=True, hatch_walls=True):
    """Plan of the underground box at the mapping Pm, in paper mm."""
    B, I = P.BOX, P.INT
    sh.rect(*Pm(B["x0"], B["y0"]), *Pm(B["x1"], B["y1"]), "S-CONCRETE")
    sh.rect(*Pm(I["x0"], I["y0"]), *Pm(I["x1"], I["y1"]), "S-CONCRETE")
    if hatch_walls:
        outer = [Pm(B["x0"], B["y0"]), Pm(B["x1"], B["y0"]),
                 Pm(B["x1"], B["y1"]), Pm(B["x0"], B["y1"])]
        inner = [Pm(I["x0"], I["y0"]), Pm(I["x1"], I["y0"]),
                 Pm(I["x1"], I["y1"]), Pm(I["x0"], I["y1"])]
        sh.concrete_hatch(outer, holes=[inner])
    # internal walls
    for mk, x0, x1, t in P.IW:
        sh.rect(*Pm(x0, I["y0"]), *Pm(x1, I["y1"]), "S-CONCRETE")
        if hatch_walls:
            sh.concrete_hatch([Pm(x0, I["y0"]), Pm(x1, I["y0"]),
                               Pm(x1, I["y1"]), Pm(x0, I["y1"])])
        sh.text(mk, Pm((x0 + x1) / 2, I["y1"] + 900), D.TXT["small"],
                "S-TEXT", "CENTER")
    # partitions
    for x0, x1 in P.PARTITIONS:
        sh.rect(*Pm(x0, I["y0"]), *Pm(x1, P.PART_DOOR_Y[0]), "S-CONCRETE-THIN")
        sh.rect(*Pm(x0, P.PART_DOOR_Y[1]), *Pm(x1, I["y1"]), "S-CONCRETE-THIN")
    if show_openings:
        for nm, cx, cy in P.ESC:
            sh.circle(Pm(cx, cy), P.ESC_CLEAR_D / 2 / scale, "S-CONCRETE")
            sh.circle(Pm(cx, cy), P.ESC_COLLAR_OD / 2 / scale, "S-HIDDEN")
            sh.cline(Pm(cx - 1300, cy), Pm(cx + 1300, cy))
            sh.cline(Pm(cx, cy - 1300), Pm(cx, cy + 1300))
        V = P.VOID
        sh.rect(*Pm(V["x0"], V["y0"]), *Pm(V["x1"], V["y1"]), "S-CONCRETE")
        sh.line(Pm(V["x0"], V["y0"]), Pm(V["x1"], V["y1"]), "S-CENTER")
        sh.line(Pm(V["x0"], V["y1"]), Pm(V["x1"], V["y0"]), "S-CENTER")
        for _, x0, x1, t in P.IW:
            if t == 400:
                sh.rect(*Pm(x0, P.BLAST_DOOR["y0"]), *Pm(x1, P.BLAST_DOOR["y1"]),
                        "S-STEELWORK")
    if show_bays:
        for n, x0, x1, use in P.BAYS:
            sh.text(str(n), Pm((x0 + x1) / 2, I["y0"] - 900), D.TXT["note"],
                    "S-GRID", "CENTER")
            sh.circle(Pm((x0 + x1) / 2, I["y0"] - 900), 2.6, "S-GRID")


def dim_box_plan(sh, Pm, scale, ybase_off=-2100, xbase_off=-1800):
    """Overall and bay dimensioning under a box plan."""
    B = P.BOX
    xs = [0, 600] + [v for _, x0, x1, _ in P.IW for v in (x0, x1)] + [21400, 22000]
    xs = sorted(set(xs))
    yb = Pm(0, B["y0"] + ybase_off)[1]
    sh.dim_chain_h([Pm(x, 0)[0] for x in xs], Pm(0, B["y0"])[1], yb, scale)
    sh.dim_h(Pm(B["x0"], 0), Pm(B["x1"], 0), yb - 9, scale)
    xb = Pm(B["x0"] + xbase_off, 0)[0]
    ys = [0, 600, 5600, 6200]
    sh.dim_chain_v([Pm(0, y)[1] for y in ys], Pm(B["x0"], 0)[0], xb, scale)
    sh.dim_v(Pm(0, B["y0"]), Pm(0, B["y1"]), xb - 9, scale)


# ------------------------------------------------------- typical wall section
def two_curtain_section(sh, Pm, scale, x0, x1, y0, y1, cover_a, cover_b,
                        phi_main, spacing, phi_link, link_spacing,
                        mark_main, mark_link, horiz=False, link_legs=2):
    """Draw a rectangular concrete section with two curtains and links.
    x0..x1 is the THICKNESS direction; y0..y1 the LENGTH direction."""
    sh.rect(*Pm(x0, y0), *Pm(x1, y1), "S-CONCRETE")
    sh.concrete_hatch([Pm(x0, y0), Pm(x1, y0), Pm(x1, y1), Pm(x0, y1)])
    ca, cb = x0 + cover_a + phi_main / 2, x1 - cover_b - phi_main / 2
    n = sh.bar_run(Pm(ca, y0 + spacing / 2), Pm(ca, y1 - spacing / 2),
                   spacing, scale, "S-REBAR-MAIN", 0.65)
    sh.bar_run(Pm(cb, y0 + spacing / 2), Pm(cb, y1 - spacing / 2),
               spacing, scale, "S-REBAR-MAIN", 0.65)
    # links
    yy = y0 + link_spacing / 2
    while yy < y1:
        sh.rect(*Pm(x0 + cover_a, yy - link_spacing * 0.28),
                *Pm(x1 - cover_b, yy + link_spacing * 0.28), "S-REBAR-STIRRUP")
        yy += link_spacing
    return n


def cover_note(sh, p, faces):
    sh.text("COVER:  " + "   ".join(f"{k} {v}" for k, v in faces), p,
            D.TXT["small"], "S-TEXT")


# ---------------------------------------------------------------- panels
def open_items_panel(sh, x, y, w, keys):
    lines = []
    for k in keys:
        t = P.OPEN_ITEMS[k]
        lines.append(f"{k}  {t[:78]}")
        rest = t[78:]
        while rest:
            lines.append("     " + rest[:78])
            rest = rest[78:]
    return sh.panel(x, y, w, "OPEN ITEMS - NOT RESOLVED, DO NOT CLOSE", lines,
                    D.TXT["small"], 3.0)


def materials_panel(sh, x, y, w):
    lines = [
        "CONCRETE          M35 to IS 456 Table 5.  w/c <= 0.45, cement >= 340 kg/m3.",
        "                  Integral crystalline waterproofing admixture.",
        "                  Blinding M15, 100 thk.",
        "REINFORCEMENT     Fe500D to IS 1786:2008.",
        "Ec = 5000 sqrt(fck) = 29 580 N/mm2   (IS 456 Cl. 6.2.3.1)",
        "gamma_m           1.5 concrete / 1.15 steel  (IS 456 Cl. 36.4.2)",
        "",
        "BLAST CASE ONLY   IS 4991 Cl. 10.3.1:  fck,dyn 43.75  ·  fy,dyn 625",
        "*** NO DYNAMIC INCREASE ON SHEAR - IS 4991 Cl. 10.3.1.1 ***",
        "tau_c and tau_c,max are read at the STATIC M35 value in every check.",
        "",
        "COVER   75 cast against blinding · 50 formed earth face",
        "        40 internal · 30 stair-shaft faces",
        "        The 5 mm reduction IS 456 Table 16 permits for M35 is NOT taken.",
        "",
        "Ld TENSION 40 phi  ·  Ld COMPRESSION 32 phi  ·  LAP 50 phi STAGGERED",
        "T8 320/400 · T10 400/500 · T12 480/600 · T16 640/800",
        "T20 800/1000 · T25 1000/1250        (Ld / lap, mm)",
        "The IS 4991 Cl. 10.3.1.1 +25 % blast bond allowance is NOT taken.",
        "",
        "*** MAXIMUM BAR SPACING 150 BOTH CURTAINS - EMP REQUIREMENT ***",
        "    stricter than IS 456 Cl. 26.3.3 and than every code minimum.",
    ]
    return sh.panel(x, y, w, "MATERIALS, COVER AND ANCHORAGE", lines,
                    D.TXT["small"], 3.0)


def loading_panel(sh, x, y, w, rows, h=None, lead=3.0,
                  heading="LOADING AND GOVERNING COMBINATION"):
    return sh.panel(x, y, w, heading, rows, h or D.TXT["small"], lead)


def bbs_extract(sh, x, y, marks, w=None, title="BAR SCHEDULE EXTRACT - THIS SHEET"):
    """Small BBS extract; every mark is looked up in rebar_data."""
    colw = [17, 13, 12, 15, 15, 17, 20]
    rows = []
    for mk in marks:
        m = MARK[mk]
        rows.append([m["mark"], f"T{m['phi']}", m["shape"],
                     m["spacing"] or "-", m["count"], round(m["cut"]),
                     f"{m['kg']:.0f}"])
    sh.text(title, (x, y + 3.0), D.TXT["panel_head"], "S-TITLE")
    yy = sh.table(x, y, colw, rows,
                  ["MARK", "DIA", "SHP", "SPAC", "No.", "CUT", "kg"],
                  D.TXT["small"], 4.2)
    tot = sum(MARK[mk]["kg"] for mk in marks)
    sh.text(f"SHEET SUB-TOTAL  {tot:,.0f} kg     FULL SCHEDULE: R-004 and "
            f"Structural CAD/Schedules/BBS_MASTER.md", (x, yy - 4.4),
            D.TXT["small"], "S-TABLE")
    return yy - 8


STD_NOTES = [
    "1  ALL DIMENSIONS IN MILLIMETRES, LEVELS IN METRES RELATIVE TO FINISHED SITE GRADE 0.000.",
    "2  DO NOT SCALE FROM THIS DRAWING.  WORK TO FIGURED DIMENSIONS ONLY.",
    "3  READ WITH THE FULL R-SERIES, THE BAR BENDING SCHEDULES AND THE QA/QC REPORT.",
    "4  CONCRETE M35, REINFORCEMENT Fe500D.  COVER AS THE MATERIALS PANEL.",
    "5  MAXIMUM BAR SPACING 150 BOTH CURTAINS - AN EMP REQUIREMENT, STRICTER THAN IS 456.",
    "6  ALL LAPS 50 phi, STAGGERED SO THAT NOT MORE THAN 50 % ARE SPLICED AT ANY SECTION.",
    "7  REINFORCEMENT IS FULLY CONTINUOUS THROUGH EVERY CONSTRUCTION JOINT.  TWO WATERSTOPS",
    "   AND A WELDED Cu/GALV EMP STRAP AT EVERY JOINT.",
    "8  NO MOVEMENT JOINT ANYWHERE INSIDE THE PROTECTIVE ENVELOPE.  A MOVEMENT JOINT IS A",
    "   GUARANTEED BLAST, GAS AND EMP DISCONTINUITY.",
    "9  IS 4991:1968 Cl. 1.1 EXPRESSLY EXCLUDES NUCLEAR EXPLOSIONS FROM ITS SCOPE.  IT IS",
    "   USED HERE ONLY FOR LOADING RULES AND DYNAMIC MATERIAL STRENGTHS, AS A DOCUMENTED",
    "   CONSERVATIVE EXTRAPOLATION.  EVERY CAPACITY IS COMPUTED TO IS 456.",
    "10 A STATIC ANALYSIS GIVES THE DEMAND.  IT IS NOT, AND MUST NOT BE PRESENTED AS, PROOF",
    "   OF BLAST RESISTANCE.  SUPPORT ROTATION / DUCTILITY IS A PHASE 3 SDOF CHECK.",
    "11 NO STAAD RESULT EXISTS FOR THIS STRUCTURE.  EVERY DESIGN ACTION SHOWN IS A MANUAL",
    "   CALCULATION - NOT DIRECT STAAD OUTPUT.",
    "12 THE SENTRY POST IS NOT PART OF THIS PACKAGE.",
]


def markkey(sh, x, y, marks, w=300, title="BAR MARK KEY - THIS SHEET"):
    """Keyed bar-mark list WITH A BALLOON PER MARK.  Every mark is looked up in
    rebar_data, so the key, the balloons on the drawing and the schedule cannot
    diverge - and every mark nominated for the sheet carries a balloon on it."""
    lead = 6.0
    sh.text(title, (x + 2.0, y - 3.4), D.TXT["panel_head"], "S-TITLE")
    yy = y - 10.5
    for mk in marks:
        m = MARK[mk]
        sp = f"@ {m['spacing']}" if m["spacing"] else "     "
        sh.circle((x + 7.0, yy + 0.6), 2.6, "S-CALLOUT")
        sh.text(mk, (x + 7.0, yy + 0.6), D.TXT["small"], "S-CALLOUT", "CENTER")
        sh.text(f"T{m['phi']:<3} {sp:<7} {m['location'][:56]}",
                (x + 12.0, yy), D.TXT["small"], "S-NOTE")
        yy -= lead
    yy -= 2.0
    sh.rect(x, yy, x + w, y, "S-TITLE")
    return yy


def balloon(sh, p, mark, leader_from=None):
    """Balloon only - the description lives in the key panel."""
    sh.barmark(p, mark, None, leader_from)
