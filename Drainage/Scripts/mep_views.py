"""
mep_views.py  --  shared drawing backgrounds for the DRAINAGE, HVAC and
SCHEDULE OF FINISHES packages.

One definition of the architectural background means the same wall, the same
partition and the same bay label appear identically on a drainage plan, an HVAC
plan and a finish plan.  Geometry comes from mep_proj.py, which comes from the
master and the Rev F drawings.

Every function takes a Sheet and a mapping function P = vw(scale, ox, oy).
"""
import math
import mep_proj as P

NOTE_H = 2.4


# ------------------------------------------------------------------- plan
def underground_plan(sh, M, scale, bays=True, rooms=True, stair=True,
                     esc=True, layer="M-ARCH", struct="M-STRUCT"):
    """Underground level plan, level (-)6.100, at the given mapping."""
    B, I = P.BOX, P.INT
    # perimeter wall, drawn as a closed band
    sh.rect(*M(B["x0"], B["y0"]), *M(B["x1"], B["y1"]), struct)
    sh.rect(*M(I["x0"], I["y0"]), *M(I["x1"], I["y1"]), struct)
    # internal walls W5 / W6 / W7
    for mark, x0, x1, t in P.IW:
        sh.rect(*M(x0, I["y0"]), *M(x1, I["y1"]), struct)
        xm = (x0 + x1) / 2.0
        sh.text(mark, M(xm, I["y1"] + 150), NOTE_H, "M-TEXT", "BC")
    # 110 partitions with their 900 door gaps
    dy0, dy1 = P.PART_DOOR_Y
    for x0, x1 in P.PARTITIONS:
        sh.rect(*M(x0, I["y0"]), *M(x1, dy0), struct)
        sh.rect(*M(x0, dy1), *M(x1, I["y1"]), struct)
    # blast door openings in W6 and W7
    bd = P.BLAST_DOOR
    for mark, x0, x1, t in P.IW:
        if mark in ("W6", "W7"):
            sh.rect(*M(x0, bd["y0"]), *M(x1, bd["y1"]), "M-FLAG")
    # escape shafts
    if esc:
        for name, cx, cy, head in P.ESC:
            sh.circle(M(cx, cy), P.ESC_CLEAR_D / 2.0 / scale, layer)
            sh.circle(M(cx, cy), P.ESC_COLLAR_OD / 2.0 / scale, layer)
            sh.text(name, M(cx, cy - 1150), NOTE_H, "M-TEXT", "BC")
    # stair shaft, void edge and flights -- FROZEN GEOMETRY, annotated only
    if stair:
        S = P.STAIR
        sh.rect(*M(P.VOID["x0"], P.VOID["y0"]),
                *M(P.VOID["x1"], P.VOID["y1"]), "M-ARCH-HIDDEN")
        for (a, b) in (S["fltA"], S["fltB"]):
            sh.rect(*M(a, S["arrival_y"][0]), *M(b, S["L1_y"][1]), layer)
        sh.text("STAIR SHAFT - FROZEN GEOMETRY",
                M((P.VOID["x0"] + P.VOID["x1"]) / 2.0, 4150),
                NOTE_H, "M-TEXT", "BC")
    # bay division ticks and labels
    if bays:
        for no, x0, x1, cw, rno, rname in P.BAYS:
            xm = (x0 + x1) / 2.0
            # QA1: the bay bubbles used to sit 520 above the box, which put the
            # left-hand bubble straight through the "V1 ..." view title on every
            # plan sheet.  Moved below the box, matching the R-series convention.
            sh.circle(M(xm, B["y0"] - 900), 2.6, "M-GRID")
            sh.text(str(no), M(xm, B["y0"] - 900), NOTE_H,
                    "M-GRID", "CENTER")
            if rooms:
                sh.text(rno, M(xm, 5250), NOTE_H, "M-TEXT", "BC")
    return M


def bay_room_labels(sh, M, y=4800, h=None):
    for no, x0, x1, cw, rno, rname in P.BAYS:
        xm = (x0 + x1) / 2.0
        for i, part in enumerate(_wrap(rname, 16)):
            sh.text(part, M(xm, y - i * 380), h or NOTE_H,
                    "M-TEXT", "BC")


def _wrap(s, n):
    out, line = [], ""
    for wd in s.split():
        if len(line) + len(wd) + 1 > n and line:
            out.append(line)
            line = wd
        else:
            line = (line + " " + wd).strip()
    if line:
        out.append(line)
    return out


def ground_plan(sh, M, scale, box_below=True, layer="M-ARCH",
                struct="M-STRUCT"):
    """Ground / entry level plan: headhouse, covered stairwell, berm."""
    H, A, B = P.HH, P.ASW, P.BOX
    if box_below:
        sh.dline(M(B["x0"], B["y0"]), M(B["x1"], B["y0"]), "M-ARCH-HIDDEN")
        sh.dline(M(B["x1"], B["y0"]), M(B["x1"], B["y1"]), "M-ARCH-HIDDEN")
        sh.dline(M(B["x1"], B["y1"]), M(B["x0"], B["y1"]), "M-ARCH-HIDDEN")
        sh.dline(M(B["x0"], B["y1"]), M(B["x0"], B["y0"]), "M-ARCH-HIDDEN")
    # headhouse
    sh.rect(*M(H["x0"], H["y0"]), *M(H["x1"], H["y1"]), struct)
    sh.rect(*M(H["ix0"], H["iy0"]), *M(H["ix1"], H["iy1"]), struct)
    # covered entry stairwell
    sh.rect(*M(A["x0"], A["y0"]), *M(A["x1"], A["y1"]), struct)
    sh.rect(*M(A["ix0"], A["iy0"]), *M(A["ix1"], A["iy1"]), struct)
    # stair treads in the flight
    a, b = A["flight"]
    for i in range(1, A["risers"]):
        x = a + i * A["going"]
        if x < b:
            sh.line(M(x, A["iy0"]), M(x, A["iy1"]), layer)
    # top landing and platform
    sh.line(M(A["top_landing"][1], A["iy0"]), M(A["top_landing"][1], A["iy1"]),
            layer)
    sh.line(M(A["platform"][0], A["iy0"]), M(A["platform"][0], A["iy1"]), layer)
    # entry door
    sh.rect(*M(A["x0"], A["iy0"] + 250), *M(A["ix0"], A["iy0"] + 1250), "M-FLAG")
    # inner security door in HW2
    d = P.HH_DOOR
    sh.rect(*M(d["x0"], H["y1"] - 400), *M(d["x1"], H["y1"]), "M-FLAG")
    # threshold channel
    c0, c1 = P.ASW["channel"]
    sh.rect(*M(c0, A["iy0"]), *M(c1, A["iy1"]), "P-DRAIN-STORM")
    # berm toe, indicative
    t = P.BERM["toe_run"]
    sh.dline(M(A["x0"] - t, A["y0"] - t), M(A["x1"] + t, A["y0"] - t),
             "M-EXISTING")
    sh.dline(M(A["x0"] - t, A["y1"] + t), M(A["x1"] + t, A["y1"] + t),
             "M-EXISTING")
    return M


def levels_column(sh, x, y, entries, h=None, lead=3.4):
    """A level datum column: [(level, label), ...] top to bottom."""
    h = h or sh.TXTS["small"]
    yy = y
    for v, lab in entries:
        sh.line((x, yy), (x + 6, yy), "M-LEVEL")
        sh.text(f"({v:+.3f})  {lab}", (x + 8, yy - 0.8), h, "M-LEVEL")
        yy -= lead
    return yy


def section_datum(sh, M, x0, x1, level, label, layer="M-LEVEL", h=None):
    """A horizontal datum line across a section, with a level tag."""
    p1, p2 = M(x0, level * 1000.0), M(x1, level * 1000.0)
    sh.dline(p1, p2, layer)
    sh.text(f"({level:+.3f})  {label}", (p2[0] + 2.0, p2[1] - 0.8),
            h or sh.TXTS["small"], layer)


def north(sh, p):
    sh.sym("NORTH", p, "M-TITLE") if "NORTH" in sh.doc.blocks else None
    sh.text("N", (p[0], p[1] + 14.0), sh.TXTS["note"], "M-TITLE", "CENTER")


def scope_note(sh, x, y, w=168):
    return sh.panel(x, y, w, "SCOPE AND STATUS", [
        "SENTRY POST IS EXCLUDED from this package - no sentry post element is",
        "drawn, scheduled or quantified here.  Historical sentry post information",
        "elsewhere in the project is untouched.",
        "",
        "MAIN STAIRCASE GEOMETRY IS FROZEN.  24R @ 170.8333 / 280, 3 flights x 8,",
        "total rise 4100.  It is annotated on these sheets and never altered.",
        "",
        "DEVELOPED FOR PROJECT COORDINATION.  Design basis established.  Pending",
        "engineering verification.  NOT construction ready, NOT a final design.",
    ], h=2.0, lead=3.4)
