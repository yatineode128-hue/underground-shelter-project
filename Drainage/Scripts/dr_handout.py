"""
dr_handout.py  --  the DRAINAGE two-page handout.

EXACTLY TWO A4 LANDSCAPE PAGES.
    page 1  DRAINAGE SYSTEM - ABOVE GROUND AND ENTRY
    page 2  DRAINAGE SYSTEM - UNDERGROUND

Diagram-led.  No paragraphs.  Every number carries its evidence class.

Outputs   ../Handout/DR-H1_Drainage_Above_Ground.dxf
          ../Handout/DR-H2_Drainage_Underground.dxf
          ../Handout/DRAINAGE_HANDOUT.pdf     (2 pages, rendered from the DXF)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mep_dxf as X
import mep_proj as P
import mep_views as V
import dr_data as D

T = X.TXT
OUT = os.path.abspath(os.path.join(HERE, "..", "Handout"))
W, H = X.A4_W, X.A4_H
N1, L1 = 2.0, 3.4


def box(sh, x, y, w, h, lines, layer="P-EQUIP", th=1.9):
    sh.rect(x, y - h, x + w, y, layer)
    n = len(lines)
    for i, s in enumerate(lines):
        sh.text(s, (x + w / 2.0, y - h / 2.0 + (n - 1) * th * 0.8
                    - i * th * 1.6 - th * 0.4), th, "M-TEXT", "CENTER")


def arrow(sh, p1, p2, layer="P-FLOW"):
    import math
    sh.line(p1, p2, layer)
    ang = math.degrees(math.atan2(p2[1] - p1[1], p2[0] - p1[0]))
    sh.flow(((p1[0] + p2[0]) / 2 - math.cos(math.radians(ang)) * 1.0,
             (p1[1] + p2[1]) / 2 - math.sin(math.radians(ang)) * 1.0),
            ang, 1.8, layer)


# =====================================================================
def page1():
    sh = X.A4Sheet("DR-H1", "DRAINAGE  -  ABOVE GROUND AND ENTRY",
                   "RAINWATER  ·  SURFACE RUNOFF  ·  ENTRY THRESHOLD  ·  "
                   "EXTERNAL DISPOSAL", package="DRAINAGE",
                   rev=P.REV["drainage"], page="1 OF 2")

    # ---- site diagram
    sc = 200.0
    M = X.vw(sc, 20.0, 132.0)
    sh.text("SITE DIAGRAM   1:200", (12, 176), 2.6, "M-TITLE")
    V.ground_plan(sh, M, sc, box_below=True)
    sh.rect(*M(P.HH["x0"], P.HH["y0"]), *M(P.HH["x1"], P.HH["y1"]),
            "P-DRAIN-STORM")
    # QA1 site diagram: these captions were long enough to cross the headhouse
    # and stairwell outlines and each other.  Split, shortened and moved into
    # the clear areas of the diagram; nothing is lost.
    sh.text("HEADHOUSE ROOF 27.84 m2", M(16000, 500), 1.8, "P-DRAIN-STORM", "BC")
    sh.text("STAIRWELL ROOF 13.60 m2", M(12000, 7900), 1.8, "P-DRAIN-STORM", "BC")
    sh.text("ENGINEERED COVER 136.40 m2", M(2000, 4000), 1.8, "P-DRAIN-SEEP", "ML")
    sh.text("SHEDS AT THE SURFACE, NOT PIPED", M(2000, 3200), 1.8,
            "P-DRAIN-SEEP", "ML")
    for x in range(3000, 21000, 4000):
        sh.flow(M(x, -300), -90, 1.8, "P-FLOW")
    c0, c1 = P.ASW["channel"]
    sh.rect(*M(c0, P.ASW["iy0"]), *M(c1, P.ASW["iy1"]), "P-DRAIN-STORM")
    sh.text("CH-10  300 CHANNEL + GRATING", M(c0 - 4500, 7400), 1.8,
            "P-DRAIN-STORM", "BC")
    sh.sym("GULLY", M(15050, 6750), scale=0.5)
    sh.sym("PUMP", M(15900, 6400), scale=0.5)
    sh.text("SU-02  1.0 m3  +  2 x 2 L/s", M(17400, 6600), 1.8, "P-EQUIP", "ML")
    sh.sym("GULLY", M(14700, 1960), scale=0.5)
    sh.leader([M(14900, 1960), M(22600, 2400)], None)
    sh.text("GY-11 -> EXTERNAL SOAKAWAY", M(23000, 2400), 1.8, "P-EQUIP", "ML")
    sh.text("NEVER TO THE CLEAN SUMP", M(23000, 1600), 1.8, "M-FLAG", "ML")

    # ---- flow chain
    sh.text("FLOW PATH   -   SOURCE / COLLECTION / CONVEYANCE / DISCHARGE", (12, 123), 2.6, "M-TITLE")
    bx, by, bw, bh = 12.0, 117.0, 50.0, 12.0
    chain = [("RAIN  50 mm/h  [C]", "no return period - VERIFY"),
             ("ROOFS + COVER", "177.23 m2  ->  2.461 L/s  [R]"),
             ("SURFACE, FALLS 1:50 AWAY", "crowned grade  [C]"),
             ("GROUND AT THE BERM TOE", "no piped roof drainage")]
    for i, (a, b) in enumerate(chain):
        box(sh, bx, by, bw, bh, [a, b], "P-DRAIN-STORM")
        if i:
            arrow(sh, (bx - 5.5, by - bh / 2), (bx - 0.5, by - bh / 2))
        bx += 55.5
    bx, by = 12.0, 101.0
    chain2 = [("ENTRY THRESHOLD", "door at grade, falls away 1:50"),
              ("CH-10 CHANNEL", "full 1500 width  [C]"),
              ("CP-10 CATCHPIT", "trapped, silt bucket  [A]"),
              ("SK-02 STORM SOAKAWAY", "position not fixed  [N]")]
    for i, (a, b) in enumerate(chain2):
        box(sh, bx, by, bw, bh, [a, b], "P-DRAIN-STORM")
        if i:
            arrow(sh, (bx - 5.5, by - bh / 2), (bx - 0.5, by - bh / 2))
        bx += 55.5
    bx, by = 12.0, 85.0
    chain3 = [("DOOR OPEN, DRIVING RAIN", "1 m3 / 32 h  [C] drg 5 note 9"),
              ("GY-10 PLATFORM GULLY", "(-)2.000  [C]"),
              ("SU-02  1.0 m3", "2 L/s duty + standby, NRV  [C]"),
              ("SK-03 OWN SOAKAWAY", "54.6 h to recover  -  DR-F3")]
    for i, (a, b) in enumerate(chain3):
        box(sh, bx, by, bw, bh, [a, b],
            "M-FLAG" if i == 3 else "P-DRAIN-STORM")
        if i:
            arrow(sh, (bx - 5.5, by - bh / 2), (bx - 0.5, by - bh / 2))
        bx += 55.5

    # ---- key parameters
    sh.text("KEY PARAMETERS", (12, 64), 2.6, "M-TITLE")
    sh.table(12, 60, [46, 32, 40], [
        ("Rainfall intensity", "50 mm/h", "[C] Rev F drg 5 n1"),
        ("Runoff coefficient", "1.00", "[A] conservative"),
        ("Roof + cover catchment", "177.23 m2", "[R]"),
        ("Peak surface flow", "2.461 L/s", "[R]"),
    ], header=["PARAMETER", "VALUE", "CLASS"], h=1.8, rh=4.4, layer="M-TABLE")
    sh.table(126, 60, [42, 30, 34], [
        ("Threshold channel", "300 x 1500", "[C] Rev F"),
        ("Stairwell sump / pump", "1.0 m3 / 2 L/s", "[C] drg 5 n9"),
        ("Storm soakaway SK-02", "2.0 dia x 3.5", "[A] this package"),
        ("Foul soak pit SK-01", "21.99 m2", "[C] 2.3 % SHORT"),
    ], header=["ITEM", "VALUE", "CLASS"], h=1.8, rh=4.4, layer="M-TABLE")
    sh.panel(236, 60, 49, "OPEN ITEMS", [
        "D1  no return period",
        "    or IDF source",
        "D3  no site plan, no",
        "    boundary, no outfall",
        "DR-C1  S-06 carries the",
        "    Rev E catchment",
        "DR-C2  soak pit 2.3 %",
        "    short - ruling needed",
    ], h=1.8, lead=2.9)

    sh.finish()
    return sh


# =====================================================================
def page2():
    sh = X.A4Sheet("DR-H2", "DRAINAGE  -  UNDERGROUND",
                   "GROUNDWATER  ·  WASTEWATER  ·  SEGREGATED EFFLUENT  ·  "
                   "SUMP AND PUMPING", package="DRAINAGE",
                   rev=P.REV["drainage"], page="2 OF 2")

    # ---- underground plan
    sc = 150.0
    M = X.vw(sc, 16.0, 128.0)
    sh.text("UNDERGROUND PLAN  (-)6.100   1:150", (12, 176), 2.6, "M-TITLE")
    V.underground_plan(sh, M, sc, bays=True, rooms=False, stair=False, esc=True)
    sh.rect(*M(*D.SUMP_RECT[:2]), *M(*D.SUMP_RECT[2:]), "P-EQUIP")
    for px, py in D.SUMP_PUMPS:
        sh.sym("PUMP", M(px, py), scale=0.45)
    sh.text("SU-01  3.375 m3  IL (-)7.600", M(11818, 200), 1.8, "P-EQUIP", "BC")
    sh.rect(*M(*D.SERVICE_PLATE[:2]), *M(*D.SERVICE_PLATE[2:]),
            "P-DRAIN-RISING")
    # QA1: this flag used to sit on the "UNDERGROUND PLAN" view title
    sh.text("SERVICE ENTRY PLATE - THE ONLY ENVELOPE PENETRATION",
            M(13400, 7900), 1.8, "M-FLAG", "BC")
    for tag, x, y, l, ty, seal, sv, z, c in D.DRAINS:
        if z in ("Z1", "Z2", "Z3"):
            sh.sym("GULLY", M(x, y), scale=0.45)
    sh.pipe([M(4510, 3100), M(11068, 3100)], "P-DRAIN-WASTE", None)
    sh.rect(*M(*D.DECON_TANK[:2]), *M(*D.DECON_TANK[2:]), "P-DRAIN-EFF")
    sh.text("TK-01 1000 L", M(20800, 4000), 1.8, "P-DRAIN-EFF", "BC")
    sh.dline(M(14700, 3100), M(20198, 4900), "M-FLAG")
    sh.text("ROUTE NOT DEFINED", M(17400, 3600), 1.8, "M-FLAG", "BC")
    # QA1: the bay bubbles now sit at (-)900 and the concept strip is just
    # under the plan, so the zone strip moves ABOVE the box where it is clear.
    sh.text("Z1  CLEAN", M(6000, 6350), 1.9, "P-DRAIN-WASTE", "BC")
    sh.text("Z2  DECON", M(13800, 6350), 1.9, "P-DRAIN-EFF", "BC")
    sh.text("Z3  GREY - NO DESTINATION", M(19700, 6350), 1.9, "M-FLAG", "BC")

    # ---- concept strip
    sh.text("GROUNDWATER CONCEPT   -   THE BOX IS A TANK, NOT A DRAINED "
            "STRUCTURE", (12, 116), 2.6, "M-TITLE")
    sh.line((12, 110), (150, 110), "M-WATERPROOF")
    sh.text("CONTINUOUS TANKING MEMBRANE  -  R-805", (14, 111.5), 1.8,
            "M-WATERPROOF")
    sh.text("DESIGN GWT (-)2.000  [ASSUMED - master A2]", (14, 105.5), 1.8,
            "M-WATERPROOF")
    sh.text("SUBMERGED ENVELOPE  56.40 x 4.700 + 136.40  =  401 m2  [R]",
            (14, 101.5), 1.8, "M-TEXT")
    sh.text("SEEPAGE  0.5 L/m2/day x 401  =  200 L/day  [C] / [A8]",
            (14, 97.5), 1.8, "M-TEXT")
    sh.text("THE SUMP SITS 5.6 m BELOW THE WATER TABLE.  THERE IS NO GRAVITY "
            "OUTFALL.", (14, 92.5), 1.9, "M-FLAG")

    # ---- discharge chain
    bx, by, bw, bh = 12.0, 86.0, 40.0, 12.0
    for i, (a, b) in enumerate([
            ("SEEPAGE 200 L/d", "+ condensate 200 L/d"),
            ("FLOOR FALLS + GULLIES", "1:400 spine, 1:80 / 1:100"),
            ("SU-01  3.375 m3", "8.44 days of store  [R]"),
            ("2 x 1.5 L/s + HAND", "duty 0.31 %  -  DR-F1"),
            ("ISOL / NRV / BCV / TRAP", "in series, inside  [C]"),
            ("SK-02 STORM SOAKAWAY", "20.0 m2 required  [R]")]):
        box(sh, bx, by, bw, bh, [a, b], "P-EQUIP")
        if i:
            arrow(sh, (bx - 4.5, by - bh / 2), (bx - 0.5, by - bh / 2))
        bx += 44.5

    # ---- emergency / segregation
    sh.text("SEGREGATION AND EMERGENCY DRAINAGE", (12, 68), 2.6, "M-TITLE")
    sh.panel(12, 64, 134, "", [
        "DECON EFFLUENT is segregated throughout and shares no pipe, chamber, vent or",
        "discharge point with any clean drain.  It leaves the site BY TANKER ONLY.",
        "S-06: 'DECON EFFLUENT NEVER ENTERS THE CLEAN SUMP.'",
        "",
        "EMERGENCY:  hand pump PU-03, independent of power.  40 h of warning between the",
        "pump-start and high-alarm levels.  8.44 days of store with both pumps failed.",
        "",
        "DR-F5:  the protective boundary makes three hydraulic zones.  ZONE 1 drains to",
        "the sump - complete.  ZONE 2's recorded tank is across the boundary in bay 8 -",
        "ROUTE UNDEFINED.  ZONE 3 has no destination at all.  Protective-design decisions.",
    ], h=1.8, lead=2.9, box=True)

    sh.table(152, 64, [42, 30, 44], [
        ("Seepage + condensate", "400 L/day", "[C] S-06"),
        ("Sump store", "3.375 m3 / 8.44 d", "[R]"),
        ("Pump duty / standby", "1.5 L/s each", "[C]"),
        ("Rising main", "DN50, 0.76 m/s", "[A]"),
        ("Static lift", "7.30 m", "[R]"),
        ("Trap seal", "75 mm = 736 Pa", "[A]"),
        ("Shelter overpressure", "+50 to +100 Pa", "[C]"),
        ("Decon tank", "1000 L, tanker only", "[C]"),
        ("Total pump head", "DATA REQUIRED", "[N]"),
    ], header=["ITEM", "VALUE", "CLASS"], h=1.8, rh=4.4, layer="M-TABLE")

    sh.finish()
    return sh


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    files = []
    for fn, name in ((page1, "DR-H1_Drainage_Above_Ground"),
                     (page2, "DR-H2_Drainage_Underground")):
        p = os.path.join(OUT, name + ".dxf")
        fn().save(p)
        files.append(p)
        print("  ", name + ".dxf")
    try:
        import mep_render
        from matplotlib.backends.backend_pdf import PdfPages
        import matplotlib.pyplot as plt
        pdf = os.path.join(OUT, "DRAINAGE_HANDOUT.pdf")
        with PdfPages(pdf) as pp:
            for f in files:
                png = f[:-4] + ".png"
                mep_render.render(f, png, dpi=200)
                fig = plt.figure(figsize=(11.69, 8.27))
                ax = fig.add_axes([0, 0, 1, 1])
                ax.axis("off")
                ax.imshow(plt.imread(png))
                pp.savefig(fig)
                plt.close(fig)
                os.remove(png)
        print("   DRAINAGE_HANDOUT.pdf   (2 pages, rendered from the DXF)")
    except Exception as exc:
        print("   PDF render skipped:", exc)
