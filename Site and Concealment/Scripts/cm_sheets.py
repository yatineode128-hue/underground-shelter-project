"""cm_sheets.py  --  C-101, the above-ground signature elevation.

    C-101  ABOVE-GROUND SIGNATURE ELEVATION

WHAT THIS SHEET IS.  A true elevation, equal scales both ways, of everything
that stands above finished grade, each element at its confirmed height.  It
exists to make the camouflage policy's central finding visible in one look:
THE SHELTER IS CONCEALED, THE INSTALLATION IS NOT.

WHAT IT IS NOT, AND CANNOT BE.  A concealment layout.  There is no site plan
anywhere in this project - master open item D3 - so no element's position on
the ground is known except relative to the box.  The sentry post is therefore
drawn BEYOND A BREAK, at its confirmed height and size and at no fixed
distance, and the two air shafts carry the same flag.  Nothing about nets,
screens, paint schemes, thermal treatment or detection criteria appears
anywhere on this sheet, because the project contains none of it.

The sheet standard, border, layers and title block are the project's existing
ones - mep_dxf.Sheet, which subclasses sc_dxflib.Sheet - so C-101 is the same
drawing standard as the issued D, M, A-6xx and F series.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.normpath(os.path.join(HERE, "..", "..",
                                                 "Drainage", "Scripts")))
import mep_dxf as X                                        # noqa: E402
import mep_proj as P                                       # noqa: E402
import cm_data as C                                        # noqa: E402

T = X.TXT
OUT = os.path.abspath(os.path.join(HERE, "..", "DXF"))
NOTE, LEAD = 2.4, 4.3
CA, WA = 14.0, 408.0
CB, WB = 430.0, 401.0

CM_LAYERS = {
    "C-SIGNATURE": (1, 50, "Above ground - what can be seen"),
    "C-BURIED":    (3, 35, "Below ground - what cannot"),
    "C-GRADE":     (2, 40, "Finished grade"),
}


class CSheet(X.Sheet):
    """An A1 site and concealment sheet.

    The sentry post IS in scope on this sheet - it is the tallest signature on
    the site - so the two inherited scope notes are replaced rather than
    carried, which would otherwise contradict the drawing.
    """

    DATE = C.DATE
    SCOPE_NOTE = "SENTRY POST INCLUDED - IT IS THE TALLEST SIGNATURE ON SITE"
    TB_SCOPE = "SENTRY POST INCLUDED ON THIS SHEET"

    def __init__(self, number, title, subtitle="", flags=(), of=""):
        super().__init__(number, title, subtitle, package=C.PACKAGE,
                         rev=C.REV, flags=list(flags), sheet_of=of)
        for name, (col, lw, desc) in CM_LAYERS.items():
            ly = self.doc.layers.add(name)
            ly.color = col
            ly.lineweight = lw
            ly.description = desc


# =====================================================================
def c101():
    sh = CSheet("C-101", "ABOVE-GROUND SIGNATURE ELEVATION",
                "EVERY ELEMENT THAT STANDS ABOVE FINISHED GRADE, AT ITS "
                "CONFIRMED HEIGHT",
                flags=("D3", "CAM-V2", "U2", "U3"), of="1 OF 1")

    sc = 60.0
    GRADE_Y = 395.0
    M = X.vw(sc, 90.0, GRADE_Y)          # model x in mm, model y = level in mm

    sh.view_title((20, 553), "V1", "ABOVE-GROUND SIGNATURE ELEVATION",
                  "SCALE 1:60, EQUAL BOTH WAYS   A TRUE ELEVATION, NOT A SITE "
                  "PLAN   LEVELS m   ALL OTHER DIMENSIONS mm")

    # ---- the buried structure, which is the point of the drawing ----
    B = P.BOX
    sh.dline(M(B["x0"], -6700), M(B["x1"], -6700), "C-BURIED")
    sh.dline(M(B["x0"], -2000), M(B["x1"], -2000), "C-BURIED")
    sh.dline(M(B["x0"], -6700), M(B["x0"], -2000), "C-BURIED")
    sh.dline(M(B["x1"], -6700), M(B["x1"], -2000), "C-BURIED")
    sh.text(f"THE SHELTER  -  {B['x1'] / 1000:.0f} m LONG, ENTIRELY BURIED "
            f"UNDER {C.COVER} OF ENGINEERED COVER.  NOTHING OF IT IS VISIBLE  [C]",
            M(11000, -4600), NOTE, "C-BURIED", "BC")
    sh.text("ROOF TOP (-2.000)", M(11000, -1750), 2.0, "C-BURIED", "BC")

    # the cover, and the grade over it
    sh.hatch_pat([M(B["x0"], -2000), M(B["x1"], -2000),
                  M(B["x1"], 0), M(B["x0"], 0)], "ANSI31", 1.4, 0.0,
                 layer="M-EXISTING")
    sh.line((14.0, GRADE_Y), (700.0, GRADE_Y), "C-GRADE")
    sh.text("GRADE 0.000", (62.0, GRADE_Y + 1.6), 2.0, "C-GRADE")
    sh.text("FINISHED GRADE IS CROWNED AND FALLS 1:50 AWAY (A.4.3).  THIS "
            "ELEVATION IS TAKEN AT THE CROWN  [C]",
            M(11000, -3600), NOTE, "C-GRADE", "BC")
    sh.text(f"FLOOR (-6.100)   MAT SOFFIT (-6.700)", M(1200, -6350), 2.0,
            "C-BURIED")

    # ---- what stands above it, in confirmed X where there is one ----
    def block(x0, x1, top_m, label, sub=None, layer="C-SIGNATURE", ly=0):
        p0, p1 = M(x0, 0), M(x1, top_m * 1000.0)
        sh.rect(p0[0], p0[1], p1[0], p1[1], layer)
        xm = (p0[0] + p1[0]) / 2.0
        sh.text(label, (xm, p1[1] + 6.0 + ly), 2.2, layer, "CENTER")
        if sub:
            sh.text(sub, (xm, p1[1] + 3.0 + ly), 1.9, layer, "CENTER")
        return p1[1]

    block(P.ESC[0][1] - P.ESC_COLLAR_OD / 2, P.ESC[0][1] + P.ESC_COLLAR_OD / 2,
          P.ESC[0][3], "ESC 1", "(+0.150)")
    block(P.ESC[1][1] - P.ESC_COLLAR_OD / 2, P.ESC[1][1] + P.ESC_COLLAR_OD / 2,
          P.ESC[1][3], "ESC 2", "(+0.700)")
    hh_top = M(P.HH["x1"], P.LVL["hh_top"] * 1000.0)
    sh.rect(*M(P.HH["x0"], 0), hh_top[0], hh_top[1], "C-SIGNATURE")
    sh.leader([(hh_top[0] - 6.0, hh_top[1]), (400.0, 420.0)], None)
    sh.text("HEADHOUSE", (400.0, 425.0), 2.2, "C-SIGNATURE", "CENTER")
    sh.text("(+0.900)  NO EARTH COVER", (400.0, 422.0), 1.9, "C-SIGNATURE",
            "CENTER")
    # the covered stairwell stands behind the headhouse in Y - hidden where
    # the two overlap in X, which is how an elevation shows it
    a0, a1 = P.ASW["x0"], P.ASW["x1"]
    p0, p1 = M(a0, 0), M(a1, P.LVL["asw_head"] * 1000.0)
    sh.line((p0[0], p0[1]), (p0[0], p1[1]), "C-SIGNATURE")
    sh.line((p0[0], p1[1]), (p1[0], p1[1]), "C-SIGNATURE")
    sh.dline((p1[0], p1[1]), (p1[0], p0[1]), "C-SIGNATURE")
    sh.text("COVERED ENTRY STAIRWELL", ((p0[0] + p1[0]) / 2.0, p1[1] + 6.0),
            2.2, "C-SIGNATURE", "CENTER")
    sh.text("(+2.450)  OUTSIDE THE PROTECTIVE BOUNDARY, DECLARED EXPENDABLE",
            ((p0[0] + p1[0]) / 2.0, p1[1] + 3.0), 1.9, "C-SIGNATURE", "CENTER")

    # ---- the two air shafts: heights recorded, positions not -------
    s0 = M(-2600, 0)
    s1 = M(-2000, 1500)
    sh.rect(s0[0], s0[1], s1[0], s1[1], "C-SIGNATURE")
    sh.text("SH-1", ((s0[0] + s1[0]) / 2.0, s1[1] + 5.6), 2.0,
            "C-SIGNATURE", "CENTER")
    sh.text("(+1.500)", ((s0[0] + s1[0]) / 2.0, s1[1] + 3.0), 1.7,
            "C-SIGNATURE", "CENTER")
    sh.text("POSITION", ((s0[0] + s1[0]) / 2.0, s0[1] - 4.0), 1.7,
            "M-FLAG", "CENTER")
    sh.text("NOT FIXED [N]", ((s0[0] + s1[0]) / 2.0, s0[1] - 6.6), 1.7,
            "M-FLAG", "CENTER")

    t0 = M(22800, 0)
    t1 = M(23400, 900)
    sh.rect(t0[0], t0[1], t1[0], t1[1], "C-SIGNATURE")
    sh.dline((t0[0], t1[1]), (t0[0], t1[1] + 14.0), "M-FLAG")
    sh.dline((t1[0], t1[1]), (t1[0], t1[1] + 14.0), "M-FLAG")
    sh.text("SH-2", ((t0[0] + t1[0]) / 2.0, t1[1] + 20.5), 2.0,
            "C-SIGNATURE", "CENTER")
    sh.text("HEAD LEVEL", ((t0[0] + t1[0]) / 2.0, t1[1] + 17.5), 1.7,
            "M-FLAG", "CENTER")
    sh.text("NOT RECORDED [N]", ((t0[0] + t1[0]) / 2.0, t0[1] - 4.0), 1.7,
            "M-FLAG", "CENTER")

    # ---- the break, and the sentry post beyond it ------------------
    BX = 495.0
    for dx in (0.0, 5.0):
        sh.pline([(BX + dx, GRADE_Y - 14.0), (BX + dx + 4.0, GRADE_Y + 6.0),
                  (BX + dx, GRADE_Y + 26.0)], "M-FLAG")
    sh.text(f"AT LEAST {C.SP['siting_min_m']:.0f} 000 CLEAR OF THE SHELTER "
            f"EXCAVATION  -  A SITING RULE, NOT A POSITION.",
            (BX + 12.0, GRADE_Y - 9.0), 2.0, "M-FLAG")
    sh.text("THERE IS NO SITE PLAN ANYWHERE IN THIS PROJECT, MASTER OPEN "
            "ITEM D3  [C] / [N]",
            (BX + 12.0, GRADE_Y - 13.0), 2.0, "M-FLAG")

    SPX0 = 580.0
    SPX1 = SPX0 + C.SP["w"] / sc
    sh.line((BX + 10.0, GRADE_Y), (700.0, GRADE_Y), "C-GRADE")
    sh.rect(SPX0, M(0, C.SP["ffl"] * 1000)[1], SPX1,
            M(0, C.SP["parapet"] * 1000)[1], "C-SIGNATURE")
    for lab, lvl in (("PARAPET", C.SP["parapet"]), ("ROOF", C.SP["roof"]),
                     ("FIRST FLOOR", C.SP["first"]), ("GF FFL", C.SP["ffl"])):
        yy = M(0, lvl * 1000)[1]
        sh.line((SPX0, yy), (SPX1, yy), "C-SIGNATURE")
        sh.text(f"({lvl:+.3f})  {lab}", (SPX1 + 2.5, yy - 0.8), 1.9, "M-LEVEL")
    sh.text("SENTRY POST", ((SPX0 + SPX1) / 2.0,
                            M(0, C.SP["parapet"] * 1000)[1] + 8.0), 2.6,
            "C-SIGNATURE", "CENTER")
    sh.text(f"{C.SP['w']} x {C.SP['d']}  -  THE TALLEST THING ON THE SITE BY "
            f"4.5 m", ((SPX0 + SPX1) / 2.0,
                       M(0, C.SP["parapet"] * 1000)[1] + 4.4), 2.0,
            "C-SIGNATURE", "CENTER")
    # the external spiral stair, to the roof
    sh.line((SPX1 + 1.5, GRADE_Y), (SPX1 + 1.5, M(0, C.SP["roof"] * 1000)[1]),
            "C-SIGNATURE")
    sh.text(f"SPIRAL STAIR, {C.SP['stair_r']} R, {C.SP['stair_pole']} DIA POLE",
            (SPX1 + 4.0, M(0, 2400)[1]), 1.9, "C-SIGNATURE")
    sh.dim_v((SPX0, GRADE_Y), (SPX0, M(0, C.SP["parapet"] * 1000)[1]),
             SPX0 - 14.0, sc=sc)

    # ---- the two dimensions that carry the finding ------------------
    sh.dim_v((M(B["x0"], -2000)[0], M(0, -2000)[1]),
             (M(B["x0"], 0)[0], GRADE_Y), M(B["x0"], 0)[0] - 12.0, sc=sc)
    sh.text("ENGINEERED", (M(B["x0"], 0)[0] - 38.0, 380.0), 1.8, "M-DIM")
    sh.text("COVER  [C]", (M(B["x0"], 0)[0] - 38.0, 377.0), 1.8, "M-DIM")
    # ---- the finding, stated where it cannot be missed --------------
    sh.text("THE SHELTER IS CONCEALED.  THE INSTALLATION IS NOT.",
            (20.0, 532.0), 4.6, "M-FLAG")
    sh.text("A 7 m SENTRY POST, A 4 800 x 5 800 HEADHOUSE WITH NO EARTH COVER, "
            "A 2 450 STAIRWELL HEAD AND A 1 500 GOOSENECK ARE NOT CONCEALED BY "
            "ANYTHING.", (20.0, 526.0), 2.2, "M-FLAG")

    sh.panel(CA, 518, 440, "WHAT THIS SHEET IS, AND WHAT IT IS NOT", [
        "IT IS A TRUE ELEVATION, equal scales both ways, of everything that "
        "stands above finished grade,",
        "   each element at its confirmed height.  Read across it: the "
        "22 m shelter under it is invisible,",
        "   and every one of the nine things above it is not.",
        "IT IS NOT A CONCEALMENT SPECIFICATION.  Bill item B-camo  -  "
        "concealment measures beyond the 300",
        "   topsoil / turf layer  -  is tagged [N], quantity to be verified "
        "from final measurement, note NO",
        "   CONCEALMENT.  No net, screen, paint scheme, thermal treatment or "
        "detection criterion exists",
        "   anywhere in this project, and none is invented here.",
        "IT IS NOT A SITE PLAN AND CANNOT BECOME ONE.  Horizontal positions "
        "are shown ONLY where the project",
        "   confirms them relative to the box.  The sentry post and both air "
        "shafts are flagged [N] and the",
        "   sentry post is drawn beyond a break  -  master open item D3.",
    ], h=2.0, lead=LEAD)

    # ================= schedules and panels =========================
    y = sh.table(CA, 275, [96, 40, 40, 262, 72],
                 [(e, ("NOT RECORDED" if t is None else f"{t:+.3f}"),
                   ("-" if w is None else str(int(w))), n, c)
                  for e, t, w, n, c in C.SIGNATURE],
                 header=["ELEMENT", "TOP LEVEL", "WIDTH", "NOTE", "EVIDENCE"],
                 h=2.0, rh=6.4, layer="M-TABLE", max_w=642.0)

    y3 = sh.panel(CA, y - 8, WA, "THE CONCEALMENT THE DESIGN ALREADY "
                  "PROVIDES  -  AND IT IS REAL", C.PROVIDED, h=2.0, lead=LEAD)

    sh.panel(CA, y3 - 8, WA, "POLICY  -  THE CLAUSES THAT ARE ABOUT THIS "
             "DRAWING", [
        "CAM-P1   THE TURF IS A CONTINUOUS SURFACE, NOT A PATCH.  The 300 "
        "topsoil / turf is laid to read as",
        "         the ground it replaces, using the site's own stripped turf.",
        "CAM-P3   THE BERM READS AS GROUND, NOT AS AN ENGINEERED LINE.  "
        "1.5:1 to +0.900.",
        "CAM-P4   SHAFT HEADS SIT AS LOW AS THEIR FUNCTION ALLOWS.  ESC 1 at "
        "+0.150 and ESC 2 at +0.700 are",
        "         already low; the +1.500 gooseneck is the one that is not, "
        "and its height is functional.",
        "CAM-P6   THERMAL AND ACOUSTIC SIGNATURE IS THE GENERATOR, AND IT IS "
        "UNQUANTIFIED  [N].",
        "CAM-P7   DO NOT ASSUME CONCEALMENT IS PRICED.  B-camo carries no "
        "quantity and no rate.  Anything",
        "         specified from this sheet is an ADDITION to the bill.",
    ], h=2.0, lead=LEAD)

    y2 = sh.panel(CB, y - 8, WB, "WHAT THIS DRAWING CANNOT SHOW, AND WHY  [N]", [
        "NO CONCEALMENT LAYOUT.  There is no site plan, boundary, contour, "
        "approach or tree line anywhere in",
        "   this project  -  master open item D3.  Nothing can be sited, no "
        "line of sight can be drawn and no",
        "   screening position can be proposed.  THE SENTRY POST IS THEREFORE "
        "SHOWN BEYOND A BREAK, at its",
        "   confirmed height and size and at no fixed distance.",
        "NO NET, SCREEN, PAINT SCHEME, THERMAL TREATMENT OR DETECTION "
        "CRITERION.  None exists anywhere in the",
        "   project.  Bill item B-camo  -  concealment measures beyond the 300 "
        "topsoil / turf layer  -  is tagged",
        "   [N], quantity to be verified from final measurement, note NO "
        "CONCEALMENT.  Nothing is invented here.",
        "NO CONCEALMENT REQUIREMENT AT ALL.  What has to be concealed, and "
        "from what, depends on two questions",
        "   the project has never answered  -  U2, whether a direct hit is a "
        "requirement, and U3, the design",
        "   basis threat yield.  Both are in master K.1b awaiting a client or "
        "military ruling.",
        "NO FINISH, COLOUR OR REFLECTIVITY for any shaft head, cover slab or "
        "gooseneck  -  CAM-V3.",
        "",
        "THIS SHEET STATES WHAT THE DESIGN ACHIEVES AND WHAT IT DOES NOT, AND "
        "STOPS THERE.",
    ], h=2.0, lead=LEAD)

    X.evidence_key(sh, CB, y2 - 8)

    sh.finish(scale="1:60", sheet_of="1 OF 1")
    return sh


# =====================================================================
def main():
    os.makedirs(OUT, exist_ok=True)
    sh = c101()
    p = sh.save(os.path.join(OUT, "C-101_Above_Ground_Signature_Elevation.dxf"))
    print("wrote", os.path.basename(p))


if __name__ == "__main__":
    main()
