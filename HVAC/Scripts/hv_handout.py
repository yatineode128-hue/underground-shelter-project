"""
hv_handout.py  --  the HVAC two-page handout.  EXACTLY TWO A4 LANDSCAPE PAGES.
    page 1  UNDERGROUND HVAC - NORMAL OPERATION
    page 2  UNDERGROUND HVAC - EMERGENCY / PROTECTIVE OPERATION
"""
import os
import sys
import math

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "Drainage",
                                                "Scripts")))
import mep_dxf as X
import mep_proj as P
import mep_views as V
import hv_data as H

T = X.TXT
OUT = os.path.abspath(os.path.join(HERE, "..", "Handout"))


def box(sh, x, y, w, h, lines, layer="M-EQUIP", th=1.9):
    sh.rect(x, y - h, x + w, y, layer)
    n = len(lines)
    for i, s in enumerate(lines):
        sh.text(s, (x + w / 2.0, y - h / 2.0 + (n - 1) * th * 0.8
                    - i * th * 1.6 - th * 0.4), th, "M-TEXT", "CENTER")


def arrow(sh, p1, p2, layer="M-AIRFLOW"):
    sh.line(p1, p2, layer)
    ang = math.degrees(math.atan2(p2[1] - p1[1], p2[0] - p1[0]))
    sh.flow(((p1[0] + p2[0]) / 2 - math.cos(math.radians(ang)) * 1.0,
             (p1[1] + p2[1]) / 2 - math.sin(math.radians(ang)) * 1.0),
            ang, 1.8, layer)


def page1():
    sh = X.A4Sheet("HV-H1", "UNDERGROUND HVAC  -  NORMAL OPERATION",
                   "FRESH AIR  ·  SUPPLY  ·  CASCADE  ·  EXHAUST  ·  "
                   "DAY AND NIGHT BALANCE", package="HVAC",
                   rev=P.REV["hvac"], page="1 OF 2")

    sc = 150.0
    M = X.vw(sc, 24.0, 128.0)
    sh.text("UNDERGROUND PLAN  (-)6.100   1:150", (12, 176), 2.6, "M-TITLE")
    V.underground_plan(sh, M, sc, bays=True, rooms=False, stair=False,
                       esc=True)
    sh.rect(*M(*H.FILTER_T1[:2]), *M(*H.FILTER_T1[2:]), "M-EQUIP")
    sh.rect(*M(*H.FILTER_T2[:2]), *M(*H.FILTER_T2[2:]), "M-EQUIP")
    # QA1: at 1:150 there is no room between the box and the bubbles, so this
    # caption reads under the plan instead of over it.
    sh.text("AHU-1 / AHU-2   2 x 300 m3/h   TRUE N+1", M(11800, -1900), 1.8,
            "M-EQUIP", "BC")
    for tag, x, yq in H.BLAST_VALVE_PTS[:3]:
        sh.sym("BVALVE", M(x, yq), scale=0.5)
        sh.text(tag, M(x, yq - 900), 1.8, "M-DAMPER", "BC")
    sh.duct(M(598, 2200), M(11098, 2200), 1.6, "M-FLAG", "RAW AIR 11.2 m")
    sh.duct(M(11098, 4200), M(2600, 4200), 1.6, "M-DUCT-SUPPLY", "SUPPLY 300")
    for x, lab in ((2050, "30"), (4510, "30"), (7270, "135/45"),
                   (10030, "45/135"), (11820, "60")):
        sh.sym("DIFFUSER", M(x, 3400), scale=0.35)
        sh.text(lab, M(x, 2700), 1.8, "M-TERMINAL", "BC")
    for xg in (12700, 13600, 14400):
        sh.flow(M(xg, 1400), 0, 2.2, "M-AIRFLOW")
    sh.text("CASCADE 300 m3/h", M(13600, 800), 1.8, "M-DUCT-RETURN", "BC")

    sh.text("AIR PATH", (12, 118), 2.6, "M-TITLE")
    bx, by, bw, bh = 12.0, 112.0, 41.0, 13.0
    for i, (a, b) in enumerate([
            ("SH-1 SHAFT", "600 x 600, +1.500 [C]"),
            ("BV-1 / BV-2", "DN100, 10.6 m/s [C]"),
            ("RAW DUCT 11.2 m", "*** HV-F2 ***"),
            ("AHU  G4/F7 H14 CARBON", "2 x 300, TRUE N+1 [C]"),
            ("FAN + HAND CRANK", "300 m3/h [C]"),
            ("PLENUM +50 to +100 Pa", "every leak outward [C]")]):
        box(sh, bx, by, bw, bh, [a, b],
            "M-FLAG" if i == 2 else "M-DUCT-FRESH")
        if i:
            arrow(sh, (bx - 5, by - bh / 2), (bx - 0.5, by - bh / 2))
        bx += 46
    bx, by = 12.0, 94.0
    for i, (a, b) in enumerate([
            ("BAYS 1 TO 5", "240/195/60/30 m3/h"),
            ("VCD-1 / VCD-2", "day / night 135 / 45"),
            ("AIRLOCK CASCADE", "+50/+35/+20/+10 Pa"),
            ("BV-3 + OPRV IN W6", "exhaust to bay 7 [C]"),
            ("LAVATORY EXTRACT", "45 m3/h, kept negative"),
            ("LEAKAGE 32.5 m3/h", "11 % of one train [R]")]):
        box(sh, bx, by, bw, bh, [a, b], "M-DUCT-SUPPLY" if i < 2
            else "M-DUCT-RETURN")
        if i:
            arrow(sh, (bx - 5, by - bh / 2), (bx - 0.5, by - bh / 2))
        bx += 46

    sh.text("KEY PARAMETERS", (12, 76), 2.6, "M-TITLE")
    sh.table(12, 72, [46, 30, 34], [
        ("Occupancy / endurance", "9 / 96 h", "[C] S-06"),
        ("Design flow", "300 m3/h", "[C] S-06"),
        ("Configuration", "2 x 300, N+1", "[C] S-06"),
        ("Per person", "33.3 m3/h", "[R] 2.2 x working"),
        ("ACH, clean zone", "1.62", "[R]"),
        ("Envelope / clean zone", "217.0 / 185.0 m3", "[R] = S-06"),
    ], header=["PARAMETER", "VALUE", "CLASS"], h=1.8, rh=4.4, layer="M-TABLE")
    sh.table(128, 72, [42, 30, 34], [
        ("Leakage", "32.5 m3/h", "[R] = S-06"),
        ("Overpressure", "+50 to +100 Pa", "[C] S-06"),
        ("Ductwork + plenum loss", "161 Pa", "[R] calc H.9"),
        ("Total fan duty", "VENDOR DATA", "[N] 5 of 8"),
        ("Cooling load", "NOT CALCULATED", "[N] 8 inputs"),
        ("Noise criterion", "NONE EXISTS", "[N]"),
    ], header=["ITEM", "VALUE", "CLASS"], h=1.8, rh=4.4, layer="M-TABLE")
    sh.panel(238, 72, 47, "ROOM AIRFLOW", [
        "U-01 stores      30 / 30",
        "U-02 lav + med   30 / 30",
        "U-03 ops        135 / 45",
        "U-04 berthing    45 / 135",
        "U-05 plant       60 / 60",
        "U-06 airlock    300 transfer",
        "TOTAL           300 / 300",
        "day / night, m3/h  [A]",
        "The occupied room of the",
        "pair gets 15.0 m3/h/person",
        "- criterion 2 exactly.",
    ], h=1.8, lead=2.9)
    sh.finish()
    return sh


def page2():
    sh = X.A4Sheet("HV-H2", "UNDERGROUND HVAC  -  EMERGENCY AND PROTECTIVE "
                   "OPERATION",
                   "FIVE MODES  ·  BLAST VALVES  ·  FILTRATION  ·  CLOSED "
                   "MODE  ·  WHAT RUNS OUT FIRST", package="HVAC",
                   rev=P.REV["hvac"], page="2 OF 2")

    sh.text("THE PRESSURE CASCADE   -   WHY EVERY LEAK GOES OUTWARD",
            (12, 176), 2.6, "M-TITLE")
    bx, by, bw, bh = 12.0, 170.0, 52.0, 17.0
    for i, (nm, pr) in enumerate([("CLEAN ZONE BAYS 1-5", "+50 Pa"),
                                  ("AIRLOCK STAGE 3", "+35 Pa"),
                                  ("AIRLOCK STAGE 2", "+20 Pa"),
                                  ("AIRLOCK STAGE 1", "+10 Pa"),
                                  ("BAY 7 / OUTSIDE", "0 Pa")]):
        box(sh, bx, by, bw, bh, [nm, pr],
            "M-EQUIP" if i == 0 else ("M-DUCT-EXH" if i == 4
                                      else "M-DUCT-RETURN"))
        if i:
            arrow(sh, (bx - 4.5, by - bh / 2), (bx - 0.5, by - bh / 2))
        bx += 56
    sh.text("300 m3/h TRANSFERS THROUGH THE WHOLE CHAIN.  THE AIRLOCK IS THE "
            "EXHAUST PATH, NOT A DEAD END.  [C]", (12, 150), 2.0, "M-TEXT")

    sh.text("FILTER TRAIN   -   THE ORDER IS NOT INTERCHANGEABLE",
            (12, 142), 2.6, "M-TITLE")
    bx = 12.0
    for stage, spec, fn, cls in H.FILTERS:
        box(sh, bx, 136, 37, 15, [stage, spec], "M-EQUIP", th=1.5)
        if bx > 12:
            arrow(sh, (bx - 3.5, 128.5), (bx - 0.5, 128.5))
        bx += 40
    sh.text("A FLOW METER AND A DIFFERENTIAL-PRESSURE GAUGE ACROSS EVERY STAGE "
            "-  THE ONLY WAY TO KNOW A FILTER IS SPENT  [C] S-06",
            (12, 116), 2.0, "M-FLAG")

    # QA1: every cell in this table used to be hard-sliced ("NO FILTER BYPASS
    # IS SHO", "bay 8 not pressuri"), which lost information on a sheet meant
    # to be read in an emergency.  Full text now, with the table fitting its
    # own columns inside the printable width.
    sh.text("OPERATING MODES", (12, 112), 2.6, "M-TITLE")
    sh.table(12, 108, [8, 34, 50, 78, 20, 30],
             [(m, n, wh, wt, f, p) for m, n, wh, wt, f, p in H.MODES],
             header=["#", "MODE", "WHEN", "WHAT RUNS", "FLOW", "PRESSURE"],
             h=1.8, rh=4.4, layer="M-TABLE", max_w=273)

    sh.text("CLOSED MODE   -   WHAT RUNS OUT FIRST", (12, 76), 2.6, "M-TITLE")
    sh.table(12, 72, [56, 22, 24, 76], [
        ("Unscrubbed, CO2 to 1.0 %", "9.9 h", "[R]",
         "(0.0096 x 185) / 0.18.  Reproduces S-06"),
        ("Soda lime, 40 kg", "48 h", "[C]", "*** THE GOVERNING CONSUMABLE ***"),
        ("Oxygen, 15 m3", "80 h", "[R]", "2 x 50 L at 150 bar"),
        ("Design endurance", "96 h", "[C]",
         "Closed covers 48; the rest needs filtration"),
    ], header=["CONSUMABLE", "ENDURANCE", "CLASS", "NOTE"], h=1.8, rh=4.4,
        layer="M-TABLE")

    sh.panel(196, 62, 89, "EMERGENCY PROVISIONS", [
        "SECOND TRAIN      TRUE N+1  [C]",
        "HAND CRANK        survives power loss  [C]",
        "MANUAL DAMPERS    inboard of all 5 valves  [C]",
        "BLAST VALVES      automatic, < 2 ms  [C]",
        "OPRV WITH BV-3    relieves without opening  [C]",
        "SODA LIME + O2    48 h with no air movement",
        "GENERATOR BAY 8   outside the envelope  [C]",
        "",
        "EMERGENCY POWER IS NOT DESIGNED HERE.  The",
        "15 kVA set is confirmed; the distribution, the",
        "UPS and the battery autonomy are an ELECTRICAL",
        "scope item.  [N]",
    ], h=1.8, lead=2.9)

    # QA1: this panel used to bottom out at y = 6, inside the A4 footer strip
    sh.panel(12, 48, 178, "OPERATING SEQUENCE", [
        "1  WARNING - mode 2, filtered.  Confirm +50 Pa and the cascade at every stage.",
        "2  DETONATION - the five valves shut in under 2 ms and hold.  NO CREW ACTION IS POSSIBLE.  Mode 3.",
        "3  CLOSED - soda lime and oxygen, 48 h.  LOG THE SODA LIME, NOT THE OXYGEN.",
        "4  HAZARD ALLOWS - back to mode 2.  Confirm the cascade before standing down the scrubbant.",
        "5  ENTRY, any time in mode 2 - purge stage 1, 12.8 min, 4-5 persons per hour.  DO NOT SHORTEN IT.",
        "6  ALL-CLEAR - mode 1 or 2 by decision.  Change filters in mode 3.",
    ], h=1.7, lead=2.6)
    sh.finish()
    return sh


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    files = []
    for fn, name in ((page1, "HV-H1_HVAC_Normal_Operation"),
                     (page2, "HV-H2_HVAC_Emergency_Protective_Operation")):
        p = os.path.join(OUT, name + ".dxf")
        fn().save(p)
        files.append(p)
        print("  ", name + ".dxf")
    try:
        sys.path.insert(0, os.path.abspath(os.path.join(
            HERE, "..", "..", "Drainage", "Scripts")))
        import mep_render
        from matplotlib.backends.backend_pdf import PdfPages
        import matplotlib.pyplot as plt
        pdf = os.path.join(OUT, "HVAC_HANDOUT.pdf")
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
        print("   HVAC_HANDOUT.pdf   (2 pages, rendered from the DXF)")
    except Exception as exc:
        print("   PDF render skipped:", exc)
