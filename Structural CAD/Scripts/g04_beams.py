"""g04_beams.py  --  R-401, R-402.  BEAM-TYPE ELEMENTS ONLY.

THERE ARE NO FRAMED RC BEAMS AND NO RC COLUMNS IN THE UNDERGROUND SHELTER.
No R-501 / R-502 / R-503 column sheet is issued and no beam-column joint detail
is drawn, because no such element exists.  The three local band members that DO
exist are detailed here.
"""
import os, math
import sc_proj as P
import sc_dxflib as D
import sc_views as V
import rebar_data as R
from sc_dxflib import Sheet, vw, TXT

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "DXF", "Beams"))

NO_COLUMNS = [
    "*** THERE ARE NO RC COLUMNS, NO FRAMED BEAMS AND NO BEAM-COLUMN JOINTS",
    "    IN THE UNDERGROUND SHELTER. ***",
    "",
    "The box is a MONOLITHIC PLATE STRUCTURE - mat, walls and pressure slab.",
    "Master B.3 declares punching shear (IS 456 Cl. 31.6) NOT APPLICABLE for",
    "exactly this reason: no column or pedestal bears on the mat, and the",
    "headhouse walls bear on the ROOF, not on the foundation.",
    "",
    "CONSEQUENCES, STATED RATHER THAN LEFT IMPLICIT:",
    "  ·  NO R-501 / R-502 / R-503 COLUMN SHEET IS ISSUED.",
    "  ·  NO BEAM-COLUMN JOINT DETAIL IS DRAWN.",
    "  ·  BAR-MARK PREFIX C IS RESERVED AND DELIBERATELY UNUSED.",
    "  ·  IS 13920 Cl. 6 (beams), Cl. 7 (columns), Cl. 8 (confinement) and the",
    "     joint provisions HAVE NO MEMBER TO APPLY TO in this package.  This is",
    "     a determination, not an omission - see QAQC/IS13920_Compliance_Matrix.md.",
    "",
    "Drawing a column that does not exist would be fabrication.  It is not done.",
    "",
    "THREE LOCAL BAND MEMBERS DO EXIST AND ARE DETAILED ON THIS SHEET AND R-402:",
    "  B01-B03  BLAST-DOOR HEADER 400 x 1100, x2 (over Blast Doors 1 and 2)",
    "  H08-H09  HEADHOUSE DOOR-HEAD EDGE BAND 400 x 800",
    "  E10-E11  ENTRY-DOOR LINTEL 250 x 350",
    "",
    "They are LOCAL BANDS spanning over openings, not part of any lateral-force-",
    "resisting frame.  The governing action on the first two is BLAST, not seismic.",
]


def r401():
    sh = Sheet("R-401", "BEAM-TYPE ELEMENT LOCATION PLAN",
               "HEADERS · EDGE BANDS · LINTELS  -  NO FRAMED BEAM OR COLUMN EXISTS",
               flags=["NO COLUMNS EXIST"])
    sh.sheet_header()
    sc = 50
    Pm = vw(sc, 66, 400)
    V.box_plan(sh, Pm, sc, show_bays=True, show_openings=True, hatch_walls=True)
    for _, x0, x1, t in P.IW:
        if t == 400:
            sh.rect(*Pm(x0 - 200, P.BLAST_DOOR["y0"] - 300),
                    *Pm(x1 + 200, P.BLAST_DOOR["y1"] + 1400), "S-REBAR-SEC")
    sh.rect(*Pm(P.HH["x0"], P.HH["y0"]), *Pm(P.HH["x1"], P.HH["y1"]), "S-REFERENCE")
    sh.text("HEADHOUSE OVER", Pm(16000, 5900), TXT["small"], "S-REFERENCE", "CENTER")
    sh.rect(*Pm(14450, 5400), *Pm(15350, 6200), "S-REBAR-SEC")
    V.dim_box_plan(sh, Pm, sc)
    sh.north((560, 456))
    sh.leader([Pm(15000, 2400), (250, 540)], "B01-B03  BLAST-DOOR HEADER 400 x 1100 (x2)")
    # QA1: leader text used to sit on the W7 wall mark - dropped clear
    sh.leader([Pm(14900, 5800), (420, 514)], "H08-H09  HEADHOUSE DOOR-HEAD EDGE BAND")
    sh.view_title((66, 552), "V1", "BEAM-TYPE ELEMENT LOCATIONS - UNDERGROUND LEVEL",
                  "SCALE 1:50")
    sh.text("THE ONLY BEAM-TYPE ELEMENTS IN THE STRUCTURE ARE LOCAL BANDS OVER OPENINGS.",
            (66, 372), TXT["small"], "S-BLAST")
    V.loading_panel(sh, 66, 352, 300, NO_COLUMNS, TXT["small"], 3.05,
                    heading="WHY THERE IS NO COLUMN SHEET IN THIS PACKAGE")
    y = V.loading_panel(sh, 376, 352, 262, [
        "ELEMENT                        SIZE        SPAN   ACTION",
        "BLAST-DOOR HEADER x2        400 x 1100     1200   w 402 kN/m",
        "  M = w L2 / 12 = 48.2 kNm  ·  V = 241 kN  ·  tau 0.578 N/mm2",
        "  4-T20 TOP + 4-T20 BOTTOM · T12 4-LEGGED LINKS @ 150",
        "  GOVERNING: COMB 103 BLAST",
        "",
        "HEADHOUSE DOOR-HEAD BAND    400 x 800       900   w 402 kN/m",
        "  M = w L2 / 12 = 27.1 kNm  ·  V = 181 kN  ·  d 742 · tau_v 0.610",
        "  4-T20 TOP + 4-T20 BOTTOM · T12 4-LEGGED LINKS @ 150",
        "  over the opening AND 600 mm each side",
        "  GOVERNING: COMB 103 BLAST, acting on EITHER FACE",
        "",
        "  A GEOMETRIC TRAP, RECORDED RATHER THAN HIDDEN:  the door head is at",
        "  (-)2.000 + 2.100 = +0.100 and the roof soffit is at +0.400, leaving",
        "  ONLY 300 mm OF WALL ABOVE THE DOOR - too shallow for a lintel.  The",
        "  300 wall and the 500 roof are therefore detailed to act TOGETHER as",
        "  an 800 mm deep edge band.",
        "",
        "ENTRY-DOOR LINTEL           250 x 350      1000   nominal",
        "  3-T12 TOP + 3-T12 BOTTOM · T8 LINKS @ 150",
        "  GOVERNING: IS 456 ULS, normal partial factors.  The entry stairwell",
        "  is OUTSIDE the protective boundary and is NOT blast rated.",
        "",
        "MANUAL CALCULATION - NOT DIRECT STAAD OUTPUT.",
    ], TXT["small"], 3.05, heading="BEAM-TYPE ELEMENT SCHEDULE")
    V.bbs_extract(sh, 376, y - 8, ["B01", "B02", "B03", "H08", "H09", "E10", "E11"])
    V.materials_panel(sh, 648, 552, 183)
    sh.titleblock(scale="1:50", sheet_of="17 OF 30")
    return sh.save(os.path.join(OUT, "R-401_Beam_Type_Element_Location_Plan.dxf"))


def _beam_elev(sh, Pm, sc, L, h, b, cov, ntop, nbot, phi, phi_l, sl, ext=0):
    sh.rect(*Pm(-ext, 0), *Pm(L + ext, h), "S-CONCRETE")
    sh.concrete_hatch([Pm(-ext, 0), Pm(L + ext, 0), Pm(L + ext, h), Pm(-ext, h)])
    yt, yb = h - cov - phi / 2, cov + phi / 2
    sh.line(Pm(-ext + cov, yt), Pm(L + ext - cov, yt), "S-REBAR-MAIN")
    sh.line(Pm(-ext + cov, yb), Pm(L + ext - cov, yb), "S-REBAR-MAIN")
    x = -ext + cov + sl / 2
    while x < L + ext - cov:
        sh.line(Pm(x, cov), Pm(x, h - cov), "S-REBAR-STIRRUP")
        x += sl


def r402():
    sh = Sheet("R-402", "BEAM-TYPE ELEMENT REINFORCEMENT DETAILS",
               "BLAST-DOOR HEADER · HEADHOUSE EDGE BAND · ENTRY-DOOR LINTEL",
               flags=["NO COLUMNS EXIST"])
    sh.sheet_header()
    # V1 blast door header elevation 1:20
    sc = 20
    Pm = vw(sc, 70, 440)
    _beam_elev(sh, Pm, sc, 1200, 1100, 400, 40, 4, 4, 20, 12, 150, ext=800)
    sh.dim_h(Pm(0, 0), Pm(1200, 0), Pm(0, -400)[1], sc)
    sh.dim_h(Pm(-800, 0), Pm(0, 0), Pm(0, -900)[1], sc)
    sh.dim_v(Pm(2000, 0), Pm(2000, 1100), Pm(2300, 0)[0], sc)
    sh.text("Ld 800 BEYOND EACH FACE", Pm(1300, -1000), TXT["small"], "S-TEXT")
    V.balloon(sh, (58, 512), "B01", Pm(600, 1040))
    V.balloon(sh, (58, 436), "B02", Pm(600, 60))
    V.balloon(sh, (152, 476), "B03", Pm(1500, 550))
    sh.view_title((30, 552), "V1", "BLAST-DOOR HEADER 400 x 1100 - ELEVATION", "SCALE 1:20")

    # V2 header section 1:10
    sc2 = 10
    Pm2 = vw(sc2, 200, 430)
    sh.rect(*Pm2(0, 0), *Pm2(400, 1100), "S-CONCRETE")
    sh.concrete_hatch([Pm2(0, 0), Pm2(400, 0), Pm2(400, 1100), Pm2(0, 1100)])
    for x in (70, 180, 290, 330):
        pass
    for x in (66, 155, 245, 334):
        sh.bar_dot(Pm2(x, 1040), 1.2, "S-REBAR-MAIN")
        sh.bar_dot(Pm2(x, 60), 1.2, "S-REBAR-MAIN")
    sh.rect(*Pm2(40, 40), *Pm2(360, 1060), "S-REBAR-STIRRUP")
    sh.line(Pm2(155, 40), Pm2(155, 1060), "S-REBAR-STIRRUP")
    sh.line(Pm2(245, 40), Pm2(245, 1060), "S-REBAR-STIRRUP")
    sh.dim_h(Pm2(0, 0), Pm2(400, 0), Pm2(0, -200)[1], sc2)
    sh.dim_v(Pm2(400, 0), Pm2(400, 1100), Pm2(700, 0)[0], sc2)
    sh.text("4-T20 TOP", Pm2(460, 1000), TXT["small"], "S-TEXT")
    sh.text("4-T20 BOTTOM", Pm2(460, 20), TXT["small"], "S-TEXT")
    sh.text("T12 4-LEG LINKS @ 150", Pm2(460, 520), TXT["small"], "S-TEXT")
    sh.text("COVER 40", Pm2(0, -420), TXT["small"], "S-TEXT")
    sh.view_title((190, 552), "V2", "HEADER SECTION", "SCALE 1:10")

    # V3 headhouse edge band 1:20
    Pm3 = vw(sc, 300, 460)
    sh.rect(*Pm3(-600, 0), *Pm3(1500, 800), "S-CONCRETE")
    sh.concrete_hatch([Pm3(-600, 0), Pm3(1500, 0), Pm3(1500, 800), Pm3(-600, 800)])
    sh.dline(Pm3(-600, 300), Pm3(1500, 300), "S-HIDDEN")
    sh.text("WALL 300 / ROOF 500 ACT TOGETHER", Pm3(-560, 340), TXT["small"], "S-TEXT")
    for y in (740, 60):
        sh.line(Pm3(-560, y), Pm3(1460, y), "S-REBAR-MAIN")
    x = -540
    while x < 1460:
        sh.line(Pm3(x, 40), Pm3(x, 760), "S-REBAR-STIRRUP")
        x += 150
    sh.dim_h(Pm3(0, 0), Pm3(900, 0), Pm3(0, -300)[1], sc)
    sh.dim_h(Pm3(-600, 0), Pm3(0, 0), Pm3(0, -800)[1], sc)
    sh.dim_v(Pm3(1500, 0), Pm3(1500, 800), Pm3(1800, 0)[0], sc)
    V.balloon(sh, (286, 508), "H08", Pm3(450, 740))
    V.balloon(sh, (352, 486), "H09", Pm3(900, 400))
    sh.view_title((280, 552), "V3", "HEADHOUSE DOOR-HEAD EDGE BAND 400 x 800",
                  "SCALE 1:20")

    # V4 entry door lintel 1:20
    Pm4 = vw(sc, 440, 470)
    _beam_elev(sh, Pm4, sc, 1000, 350, 250, 30, 3, 3, 12, 8, 150, ext=480)
    sh.dim_h(Pm4(0, 0), Pm4(1000, 0), Pm4(0, -300)[1], sc)
    sh.dim_v(Pm4(1480, 0), Pm4(1480, 350), Pm4(1700, 0)[0], sc)
    V.balloon(sh, (426, 508), "E10", Pm4(500, 320))
    V.balloon(sh, (500, 500), "E11", Pm4(1200, 175))
    sh.view_title((420, 552), "V4", "ENTRY-DOOR LINTEL 250 x 350", "SCALE 1:20")
    sh.text("NOT BLAST RATED - THE ENTRY STAIRWELL IS OUTSIDE THE PROTECTIVE",
            (420, 424), TXT["small"], "S-TEXT")
    sh.text("BOUNDARY AND IS DECLARED EXPENDABLE.", (420, 419), TXT["small"], "S-TEXT")

    # QA1: dropped from 400 so the V1 extension dimension no longer sits in it
    y = V.loading_panel(sh, 30, 384, 300, [
        "BLAST-DOOR HEADER 400 x 1100 over a 1200 clear opening",
        "  w = 383 x 2.100 / 2                     =  402 kN/m",
        "  M = w L2 / 12                           =  48.2 kNm",
        "  V = w L / 2                             =  241 kN",
        "  tau = 0.578 N/mm2",
        "  ADOPTED  4-T20 TOP + 4-T20 BOTTOM, T12 4-LEGGED LINKS @ 150",
        "  Bars anchored Ld = 800 beyond each opening face.",
        "",
        "HEADHOUSE DOOR-HEAD EDGE BAND 400 x 800 over a 900 clear opening",
        "  w = 383 x 2.100 / 2                     =  402 kN/m",
        "  M = w L2 / 12                           =  27.1 kNm",
        "  V                                       =  181 kN",
        "  d = 800 - 40 - 8 - 10 = 742 ; tau_v     =  0.610 N/mm2",
        "  ADOPTED  4-T20 TOP + 4-T20 BOTTOM, T12 4-LEGGED LINKS @ 150,",
        "  OVER THE OPENING AND 600 mm EACH SIDE.",
        "",
        "ENTRY-DOOR LINTEL 250 x 350 over a 1000 clear opening",
        "  Nominal.  ADOPTED  3-T12 TOP + 3-T12 BOTTOM, T8 LINKS @ 150.",
        "",
        "MANUAL CALCULATION - NOT DIRECT STAAD OUTPUT.  No STAAD result exists.",
    ], TXT["small"], 3.05, heading="BEAM-TYPE ELEMENTS - DESIGN")
    V.bbs_extract(sh, 30, y - 8, ["B01", "B02", "B03", "H08", "H09", "E10", "E11"])
    sh.panel(340, 400, 298, "IS 13920 - APPLICABILITY TO THESE MEMBERS", [
        "IS 13920:2016 governs DUCTILE DETAILING OF RC STRUCTURES SUBJECTED TO",
        "SEISMIC FORCES.  Its beam provisions (Cl. 6.1.x geometry, Cl. 6.2.x",
        "longitudinal steel, Cl. 6.3.x capacity-design shear and hoops) apply to",
        "members of a lateral-force-resisting moment frame.",
        "",
        "THESE THREE MEMBERS ARE NOT SUCH MEMBERS.  They are local bands spanning",
        "over openings in a buried monolithic box.",
        "",
        "THE DETERMINATION, WITH ITS EVIDENCE:",
        "  ·  Box seismic:  Ah 0.075, Vb 1050 kN, wall shear tau = 0.063 N/mm2.",
        "     NEGLIGIBLE.  [master A.7.8]",
        "  ·  IS 13920 Cl. 10.4 boundary elements: CHECKED AND NOT TRIGGERED.",
        "  ·  Governing action on the two blast headers is COMB 103 BLAST, which",
        "     IS 4991 Cl. 11.1 FORBIDS combining with earthquake.",
        "  ·  There is no column, so Cl. 7 (columns), Cl. 8 (special confining",
        "     reinforcement) and the beam-column joint provisions have no member.",
        "",
        "WHAT IS NEVERTHELESS PROVIDED, AND WHY:",
        "  The headers and the edge band carry CLOSED 4-LEGGED LINKS AT 150 c/c",
        "  over their full length - closer than IS 456 alone would require - and",
        "  equal top and bottom steel.  That is a blast-detailing decision (load",
        "  reversal and rebound), not an IS 13920 compliance claim.",
        "",
        "FULL DETERMINATION: QAQC/IS13920_Compliance_Matrix.md",
    ], TXT["small"], 3.05)
    sh.titleblock(scale="1:20, 1:10", sheet_of="18 OF 30")
    return sh.save(os.path.join(OUT, "R-402_Beam_Type_Element_Details.dxf"))


def build():
    os.makedirs(OUT, exist_ok=True)
    return [r401(), r402()]


if __name__ == "__main__":
    for f in build():
        print("written", f)
