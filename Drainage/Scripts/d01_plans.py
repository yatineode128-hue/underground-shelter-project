"""
d01_plans.py  --  the drainage plans.

    D-101  above-ground / entry level drainage plan
    D-102  rainwater catchment and surface-water plan
    D-103  entry stairwell and headhouse drainage - plan, section, threshold
    D-201  underground drainage plan - falls, gullies, zones
    D-203  underground wastewater and sanitary plan
"""
import os
import sys
import math

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mep_dxf as X
import mep_proj as P
import mep_views as V
import dr_data as D

T = X.TXT
OUT = os.path.abspath(os.path.join(HERE, "..", "DXF"))
NOTE, LEAD = 2.4, 4.3
CA, CB, CC = 14.0, 286.0, 558.0
WA, WB = 264.0, 264.0
TOP = 552.0


def sheet(num, title, sub, flags=(), of=""):
    return X.Sheet(num, title, sub, package="DRAINAGE",
                   rev=P.REV["drainage"], flags=flags, sheet_of=of)


# =====================================================================
def d101():
    sh = sheet("D-101", "ABOVE-GROUND AND ENTRY LEVEL DRAINAGE PLAN",
               "HEADHOUSE (-)2.000 - COVERED STAIRWELL - THRESHOLD - EXTERNAL "
               "DISPOSAL",
               flags=("C16", "DR-C1", "DR-D3", "DR-D4"), of="3 OF 11")

    sc = 60.0
    M = X.vw(sc, 40.0, 300.0)
    sh.view_title((20, 548), "V1", "ENTRY LEVEL DRAINAGE PLAN",
                  "SCALE 1:60   LEVELS 0.000 AND (-)2.000   ALL DIMENSIONS mm")
    V.ground_plan(sh, M, sc, box_below=True)
    V.underground_plan(sh, M, sc, bays=True, rooms=False, stair=True, esc=False,
                       layer="M-ARCH-HIDDEN", struct="M-ARCH-HIDDEN")

    # threshold channel and its catchpit
    c0, c1 = P.ASW["channel"]
    sh.text("CH-10  300 CHANNEL + GRATING, FULL 1500 WIDTH  [C]",
            M((c0 + c1) / 2 - 300, 8100), NOTE, "P-DRAIN-STORM", "BC")
    sh.leader([M(c0 + 150, 7500), M(c0 - 400, 8000)], None)
    sh.sym("CHAMBER", M(8300, 5200), scale=0.9)
    sh.text("CP-10  TRAPPED CATCHPIT, SILT BUCKET  [A]", M(8300, 4400), NOTE,
            "P-EQUIP", "BC")
    sh.pipe([M(9100, 6000), M(9100, 5400), M(8300, 5200)], "P-DRAIN-STORM",
            "PD-10  DN100  1:100")
    sh.pipe([M(8300, 4900), M(6200, 3600)], "P-DRAIN-STORM", "PD-11 DN100")
    sh.text("TO SK-02 STORM SOAKAWAY - POSITION NOT FIXED, D3  [N]",
            M(5600, 3100), NOTE, "M-FLAG", "BC")

    # platform gully + stairwell sump
    sh.sym("GULLY", M(15050, 6750), scale=0.9)
    sh.text("GY-10", M(15050, 7050), NOTE, "P-EQUIP", "BC")
    sh.sym("PUMP", M(15500, 6400), scale=0.9)
    sh.text("SU-02  1.0 m3 SUMP + 2 x 2 L/s, NRV ON THE RISING MAIN  [C]",
            M(16200, 6250), NOTE, "P-EQUIP", "ML")
    sh.pipe([M(15050, 6750), M(15500, 6400)], "P-DRAIN-STORM", "PD-12 1:80")
    sh.pipe([M(15600, 6100), M(17400, 5000)], "P-DRAIN-RISING", "PD-13")
    sh.text("TO SK-03, THE STAIRWELL'S OWN SOAKAWAY  [C] / SIZE [N]",
            M(17600, 4700), NOTE, "M-FLAG", "ML")

    # headhouse gully
    sh.sym("GULLY", M(14700, 1960), scale=0.9)
    sh.text("GY-11  FALL 1:80  [C]", M(14700, 1500), NOTE, "P-EQUIP", "BC")
    sh.text("HOSE-DOWN POINT  [C]", M(14700, 2560), NOTE, "M-TEXT", "BC")
    sh.pipe([M(14700, 1960), M(13000, 1300)], "P-DRAIN-WASTE", "PD-14 DN100 1:80")
    sh.text("TRAPPED GULLY -> EXTERNAL SOAKAWAY SK-04.",
            M(12800, 900), NOTE, "M-FLAG", "RIGHT")
    sh.text("*** NEVER TO THE CLEAN SUMP ***  [C]", M(12800, 500), NOTE,
            "M-FLAG", "RIGHT")

    # service entry plate
    sh.rect(*M(*D.SERVICE_PLATE[:2]), *M(*D.SERVICE_PLATE[2:]), "P-DRAIN-RISING")
    sh.text("SERVICE ENTRY PLATE - THE ONLY ENVELOPE PENETRATION  [C]",
            M(11800, 6500), NOTE, "M-FLAG", "BC")

    sh.dim_h(M(P.ASW["x0"], 4600), M(P.ASW["x1"], 4600), M(0, 4000)[1], sc=sc)
    sh.dim_h(M(P.HH["x0"], 3200), M(P.HH["x1"], 3200), M(0, 2600)[1], sc=sc)
    V.north(sh, (600, 470))

    y = sh.panel(CA, 268, 396, "NOTES  -  ABOVE GROUND AND ENTRY", [
        "1  THE ENTRY THRESHOLD IS PROTECTED BY THREE INDEPENDENT MEASURES ALREADY IN THE ARCHITECTURE:",
        "   the door is at grade rather than at the foot of a pit; the ground falls away 1:50 for 2000; and a",
        "   300 channel with grating crosses the full 1500 width.  Rev F drawing 5 note 5: 'WITH THE DOOR SHUT",
        "   THE CATCHMENT IS ZERO'.  CH-10 is an INTERCEPTION, not a collection - it discharges AWAY from the",
        "   entry, never into the stairwell.",
        "2  THE HEADHOUSE FLOOR GULLY GY-11 DISCHARGES TO AN EXTERNAL SOAKAWAY AND NEVER TO THE CLEAN SUMP.",
        "   This is a confirmed instruction on the Rev F ground plan, not a preference: the headhouse is outside",
        "   the gas-tight envelope and its washdown water is not clean-zone water.",
        "3  SK-02, SK-03 and SK-04 EXIST IN THE PROJECT BUT NONE OF THEM IS POSITIONED.  There is no site plan,",
        "   boundary or contour anywhere in the project (open item D3).  Their pipe runs are therefore shown",
        "   with direction and gradient but WITHOUT length - the schedules record 'not determinable'.",
        "4  IS 2470 (Pt 2) OFFSETS FOR THE FOUL SOAK PIT - at least 15 m from any well, 5 m from the septic tank",
        "   and 2 m from any building - CANNOT BE DEMONSTRATED for the same reason.  DATA REQUIRED.",
        "5  C16 - THE ROOF / PLATFORM JUNCTION IS UNRESOLVED.  It is shown at 250 to match the model and the",
        "   structural register.  It does not change any flow, pipe or pit on this sheet - see D-102 note 3.",
    ], h=NOTE, lead=LEAD)

    sh.table(CA, y - 8, [34, 108, 40, 214], [
        (t, it, ("-" if l is None else f"({l:+.3f})"), n)
        for t, it, l, n in [
            ("CH-10", "300 CHANNEL + GRATING", 0.000,
             "Full 1500 width, X 8950-9250.  Confirmed Rev F  [C]"),
            ("CP-10", "TRAPPED CATCHPIT 450 x 450", 0.000,
             "75 deep seal + silt bucket.  Position by this package  [A]"),
            ("GY-10", "TRAPPED GULLY DN100", -2.000,
             "Platform 1500 x 1500.  Confirmed Rev F drawing 5  [C]"),
            ("GY-11", "TRAPPED GULLY DN100, FALL 1:80", -2.000,
             "Headhouse hose-down point.  Confirmed Rev F ground plan  [C]"),
            ("SU-02", "STAIRWELL SUMP 1.0 m3", -2.000,
             "2 x 2 L/s duty + standby, NRV on the rising main  [C]"),
            ("SK-02", "STORM SOAKAWAY", None,
             "2.0 dia x 3.5 effective, 21.99 m2.  POSITION NOT FIXED  [A]/[N]"),
            ("SK-03", "STAIRWELL SOAKAWAY", None,
             "Exists in the project; SIZE AND POSITION NOT RECORDED  [C]/[N]"),
            ("SK-04", "HEADHOUSE EXTERNAL SOAKAWAY", None,
             "Exists on the Rev F ground plan; NOT SIZED  [C]/[N]"),
        ]], header=["TAG", "ITEM", "LEVEL", "NOTE AND EVIDENCE CLASS"],
        h=2.1, rh=6.2, layer="M-TABLE")

    X.evidence_key(sh, CA, 84)
    sh.finish(scale="1:60", sheet_of="3 OF 11")
    return sh


# =====================================================================
def d102():
    sh = sheet("D-102", "RAINWATER CATCHMENT AND SURFACE-WATER PLAN",
               "CATCHMENT AREAS, FALLS AND FLOWS AT THE RECORDED 50 mm/h",
               flags=("C16", "DR-D1", "DR-D3"), of="4 OF 11")

    sc = 60.0
    M = X.vw(sc, 40.0, 330.0)
    sh.view_title((20, 548), "V1", "CATCHMENT PLAN",
                  "SCALE 1:60   CATCHMENT BOUNDARIES HEAVY   AREAS IN m2")
    V.ground_plan(sh, M, sc, box_below=True)

    # catchment outlines
    sh.rect(*M(P.HH["x0"], P.HH["y0"]), *M(P.HH["x1"], P.HH["y1"]),
            "P-DRAIN-STORM")
    sh.text("C1  HEADHOUSE ROOF  4800 x 5800 = 27.84 m2   0.387 L/s",
            M((P.HH["x0"] + P.HH["x1"]) / 2, 3000), NOTE, "P-DRAIN-STORM", "BC")
    sh.rect(*M(P.ASW["x0"], P.ASW["y0"]), *M(P.ASW["x1"], P.ASW["y1"]),
            "P-DRAIN-STORM")
    sh.text("C2  COVERED STAIRWELL ROOF  6800 x 2000 = 13.60 m2   0.189 L/s",
            M(11000, 8200), NOTE, "P-DRAIN-STORM", "BC")
    sh.rect(*M(P.BOX["x0"], P.BOX["y0"]), *M(P.BOX["x1"], P.BOX["y1"]),
            "P-DRAIN-SEEP")
    sh.text("C3  ENGINEERED COVER OVER THE BOX  22.0 x 6.2 = 136.40 m2   1.894 L/s",
            M(11000, -1400), NOTE, "P-DRAIN-SEEP", "BC")

    # falls
    for x in range(2000, 21000, 3000):
        sh.flow(M(x, -300), -90, 2.6, "P-FLOW")
        sh.flow(M(x, 6500), 90, 2.6, "P-FLOW")
    sh.text("GRADE CROWNED, FALLS 1:50 AWAY FROM THE STRUCTURE  [C] A.4.3",
            M(11000, -2600), NOTE, "M-TEXT", "BC")

    # C16 flag at the junction
    px0, px1 = P.ASW["platform"]
    sh.rect(*M(px0, P.ASW["iy0"]), *M(px1, P.ASW["iy1"]), "M-FLAG")
    sh.text("C16 UNRESOLVED - 250 OR 500 ROOF OVER THE PLATFORM.",
            M(px1 + 400, 7200), NOTE, "M-FLAG", "ML")
    sh.text("2.25 m2 OF CATCHMENT MOVES BETWEEN C1 AND C2;",
            M(px1 + 400, 6800), NOTE, "M-FLAG", "ML")
    sh.text("THE TOTAL IS UNCHANGED.  NO PIPE OR PIT DEPENDS ON IT.",
            M(px1 + 400, 6400), NOTE, "M-FLAG", "ML")

    sh.dim_h(M(P.HH["x0"], -600), M(P.HH["x1"], -600), M(0, -1300)[1], sc=sc)
    sh.dim_h(M(P.ASW["x0"], 8600), M(P.ASW["x1"], 8600), M(0, 9200)[1], sc=sc)
    sh.dim_v(M(P.BOX["x1"] + 900, P.BOX["y0"]), M(P.BOX["x1"] + 900, P.BOX["y1"]),
             M(P.BOX["x1"] + 1600, 0)[0], sc=sc)
    V.north(sh, (600, 480))

    sh.text("V2   CATCHMENT SCHEDULE   -   Q = C i A / 3600,  i = 50 mm/h,  C = 1.00",
            (CA, 296), T["view_title"], "M-TITLE")
    y = sh.table(CA, 288, [26, 150, 40, 26, 34, 120], [
        ("C1", "Headhouse roof  X 13600-18400, Y 200-6000", "27.84", "1.00",
         "0.387", "[R] from [C] master A.4.6"),
        ("C2", "Covered stairwell roof  X 9250-16050, Y 5750-7750", "13.60",
         "1.00", "0.189", "[R] from [C] master A.4.7"),
        ("", "   less the overlap of the two footprints", "-0.61", "1.00",
         "-0.009", "[R]  2450 x 250"),
        ("C3", "Engineered cover over the box  22.0 x 6.2", "136.40", "1.00",
         "1.894", "[R] from [C] master A.4.2"),
        ("", "TOTAL - STRUCTURES AND COVER", "177.23", "", "2.461", "[R]"),
        ("", "Berm, approach, hardstanding, rest of the site",
         "DATA REQUIRED", "-", "-", "[N]  no site plan exists - D3"),
    ], header=["REF", "CATCHMENT", "AREA m2", "C", "Q L/s", "CLASS AND SOURCE"],
        h=2.1, rh=6.2, layer="M-TABLE")

    sh.panel(CA, y - 8, 396, "NOTES  -  RAINWATER", [
        "1  50 mm/h IS THE ONLY RAINFALL INTENSITY STATED ANYWHERE IN THE PROJECT (Rev F drawing 5, note 1).",
        "   NO return period, storm duration or IDF source is recorded with it.  OPEN ITEM D1 - VERIFY AGAINST",
        "   IMD PUNE DATA BEFORE CONSTRUCTION.  Every flow on this sheet scales directly with it.",
        "2  C = 1.00 is used for the RC roofs AND for the engineered cover.  A lower coefficient for turf is",
        "   defensible but is not taken: in a monsoon the 300 topsoil is saturated and the conservative bound",
        "   costs nothing here, because none of these flows is piped.",
        "3  THE ENGINEERED COVER IS NOT DRAINED BY PIPEWORK, AND MUST NOT BE.  Master A.4.3 records finished",
        "   grade as crowned, falling 1:50 away; A.7.3 gives 300 topsoil over a 150 GRANULAR FILTER over the",
        "   burster slab.  Rain sheds at the surface and what infiltrates is intercepted by the filter layer and",
        "   dispersed at the berm toe.  A pipe through the cover would breach the radiation mass and the roof",
        "   membrane - see D-001 note 1.",
        "4  THE SITE-WIDE CATCHMENT CANNOT BE CLOSED.  The table above is complete for the structures and for",
        "   nothing else.  Berm, approach and hardstanding areas do not exist as dimensioned information.",
        "5  DR-C1 - the S-06 design-flow table still carries 0.10 L/s for 'stairwell / approach surface water'.",
        "   That is the REV E OPEN-CUT figure (7.2 m2 of open pit at 50 mm/h, reproduced exactly in calculation",
        "   D.8).  At Rev F the approach is covered.  Conservative, superseded, and NOT corrected here.",
    ], h=NOTE, lead=LEAD)

    X.evidence_key(sh, CA, 92)
    sh.finish(scale="1:60", sheet_of="4 OF 11")
    return sh


# =====================================================================
def d103():
    sh = sheet("D-103", "ENTRY STAIRWELL AND HEADHOUSE DRAINAGE",
               "PLAN, LONGITUDINAL SECTION AND THRESHOLD DETAIL",
               flags=("C16", "DR-C1"), of="5 OF 11")

    # ---- V1 plan 1:50
    sc = 50.0
    M = X.vw(sc, 30.0, 400.0)
    sh.view_title((20, 548), "V1", "STAIRWELL AND HEADHOUSE - DRAINAGE PLAN",
                  "SCALE 1:50")
    V.ground_plan(sh, M, sc, box_below=False)
    sh.sym("GULLY", M(15050, 6750), scale=0.9)
    sh.text("GY-10", M(15050, 7100), NOTE, "P-EQUIP", "BC")
    sh.sym("GULLY", M(14700, 1960), scale=0.9)
    sh.text("GY-11  1:80", M(14700, 1500), NOTE, "P-EQUIP", "BC")
    c0, c1 = P.ASW["channel"]
    sh.text("CH-10", M((c0 + c1) / 2, 5300), NOTE, "P-DRAIN-STORM", "BC")
    sh.dim_h(M(P.ASW["x0"], 5200), M(P.ASW["x1"], 5200), M(0, 4600)[1], sc=sc)

    # ---- V2 section 1:50
    sc2 = 50.0
    M2 = X.vw(sc2, 30.0, 300.0)      # model y = level in mm
    sh.view_title((20, 330), "V2", "SECTION C-C  -  DRAINAGE ON THE ENTRY ROUTE",
                  "SCALE 1:50   ON Z = 6750, LOOKING SOUTH   LEVELS m")
    A = P.ASW
    # ground line and structure
    sh.line(M2(A["x0"] - 2600, 0), M2(A["x0"] - 200, 0), "M-EXISTING")
    sh.text("GROUND FALLS AWAY 1:50 FOR 2000  [C]", M2(A["x0"] - 2500, 260),
            NOTE, "M-TEXT")
    sh.rect(*M2(c0, -300), *M2(c1, 0), "P-DRAIN-STORM")
    sh.text("CH-10  300 CHANNEL + GRATING", M2(c0 - 200, -700), NOTE,
            "P-DRAIN-STORM")
    sh.line(M2(A["x0"], 0), M2(A["top_landing"][1], 0), "M-STRUCT")
    # flight
    x, z = A["flight"][0], 0.0
    for i in range(A["risers"]):
        sh.line(M2(x, z), M2(x, z - A["riser"]), "M-STRUCT")
        z -= A["riser"]
        sh.line(M2(x, z), M2(x + A["going"], z), "M-STRUCT")
        x += A["going"]
    sh.line(M2(A["platform"][0], -2000), M2(A["platform"][1], -2000), "M-STRUCT")
    sh.line(M2(A["platform"][1], -2000), M2(18400, -2000), "M-STRUCT")
    # roof
    sh.line(M2(A["x0"], 2450), M2(A["flight"][0], 2450), "M-STRUCT")
    sh.line(M2(A["flight"][0], 2450), M2(A["platform"][0], 400), "M-STRUCT")
    sh.line(M2(A["platform"][0], 400), M2(18400, 400), "M-STRUCT")
    sh.text("C16 - ROOF OVER THE PLATFORM SHOWN AT 250, UNRESOLVED",
            M2(A["platform"][0], 700), NOTE, "M-FLAG")
    # sump and gullies
    sh.sym("GULLY", M2(15050, -2000), scale=0.8)
    sh.rect(*M2(15300, -3000), *M2(16300, -2000), "P-EQUIP")
    sh.sym("PUMP", M2(15800, -2500), scale=0.9)
    sh.text("SU-02  1.0 m3  +  2 x 2 L/s, NRV  [C]", M2(16500, -2500), NOTE,
            "P-EQUIP", "ML")
    sh.pipe([M2(16300, -2400), M2(18000, -1600)], "P-DRAIN-RISING", "PD-13")
    V.section_datum(sh, M2, A["x0"] - 2600, 18600, 0.000, "GRADE = THRESHOLD")
    V.section_datum(sh, M2, A["x0"] - 2600, 18600, -2.000,
                    "PLATFORM = HEADHOUSE FLOOR = TOP OF THE 900 SLAB")

    # ---- V3 threshold detail 1:10
    M3 = X.vw(10.0, 470.0, 350.0)
    sh.view_title((464, 330), "V3", "THRESHOLD DETAIL", "SCALE 1:10")
    sh.rect(*M3(-700, -400), *M3(-300, 0), "M-STRUCT")
    sh.rect(*M3(-300, -400), *M3(0, -50), "P-DRAIN-STORM")
    sh.line(M3(0, 0), M3(700, 0), "M-STRUCT")
    sh.line(M3(-1400, 28), M3(-700, 0), "M-EXISTING")
    sh.text("GROUND FALLS AWAY 1:50", M3(-1400, 120), NOTE, "M-TEXT")
    sh.text("300 CHANNEL + REMOVABLE GRATING", M3(-300, -620), NOTE,
            "P-DRAIN-STORM")
    sh.text("50 WEATHER BAR, THRESHOLD FLUSH  [C]", M3(60, 200), NOTE, "M-TEXT")
    sh.text("ENTRY DOOR 1000 x 2100, OPENS OUTWARD  [C]", M3(60, 420), NOTE,
            "M-TEXT")
    sh.line(M3(0, 0), M3(0, 900), "M-ARCH")

    y = sh.panel(CA, 268, 396, "NOTES  -  ENTRY DRAINAGE", [
        "1  DR-C1 - THE TWO CATCHMENT FIGURES IN THE PROJECT ARE BOTH SHOWN, DELIBERATELY:",
        "      0.10 L/s   Rev E OPEN-CUT figure, still carried in the S-06 design-flow table.  7.2 m2 of open",
        "                 pit at 50 mm/h.  SUPERSEDED at Rev F but CONSERVATIVE.",
        "      1 m3/32 h  Rev F drawing 5 note 9, the worst DOOR-OPEN driving-rain rate = 0.0087 L/s.",
        "   The 2 L/s pump is 20 times the superseded figure and 230 times the current one, so the pump",
        "   selection is not sensitive to the conflict.  NOT CORRECTED HERE - S-06 is an issued sheet.",
        "2  CH-10 DISCHARGES AWAY FROM THE ENTRY, to CP-10 and then to SK-02.  It never discharges into the",
        "   stairwell.  With the door shut the catchment reaching the threshold is zero (Rev F drg 5 note 5).",
        "3  THE STAIRWELL IS OUTSIDE THE PROTECTIVE BOUNDARY and is declared expendable (master A.2).  Its",
        "   drainage is a comfort and access provision, not a protective one - which is the point of Rev F",
        "   note 9: 'DRAINAGE IS NO LONGER IN THE SAFETY PATH'.",
        "4  DR-F3 - AT THE ASSUMED 20 L/m2/day ABSORPTION, SK-03 NEEDS 54.6 h TO RECOVER FROM ONE SUMP-FULL.",
        "   That is poor for a rainwater soakaway.  It is not a defect in this layout; it is the [ASSUMED]",
        "   absorption rate showing through, and it is one of three independent reasons the PERCOLATION TEST",
        "   (master A7, IS 2470 Pt 2 Cl. 4) is on the critical path.",
        "5  C16 affects the roof over the platform, directly above GY-10.  A 250/500 step at the junction",
        "   changes where water is delivered and whether a drip is needed.  SHOWN AT 250 - NOT RESOLVED.",
    ], h=NOTE, lead=LEAD)

    X.evidence_key(sh, CA, y - 10)
    sh.finish(scale="1:50 / 1:10", sheet_of="5 OF 11")
    return sh


# =====================================================================
def _zone_shading(sh, M):
    """Label the three hydraulic zones on an underground plan."""
    sh.text("ZONE 1  CLEAN  -  BAYS 1 TO 5  ->  CLEAN SUMP", M(6000, 5850),
            NOTE, "P-DRAIN-WASTE", "BC")
    sh.text("ZONE 2  DECON", M(13800, 5850), NOTE, "P-DRAIN-EFF", "BC")
    sh.text("ZONE 3  GREY  -  NO DESTINATION", M(19700, 5850), NOTE,
            "M-FLAG", "BC")
    for x in (P.IW[0][1], P.IW[1][1], P.IW[2][1]):
        sh.line(M(x, -200), M(x, 6250), "M-FLAG")


def d201():
    sh = sheet("D-201", "UNDERGROUND DRAINAGE PLAN",
               "FLOOR FALLS - GULLIES - COLLECTION - HYDRAULIC ZONES - "
               "LEVEL (-)6.100",
               flags=("C18", "A2", "A8", "BW-01", "DR-F4", "DR-F5"),
               of="6 OF 11")

    sc = 45.0
    M = X.vw(sc, 40.0, 400.0)
    sh.view_title((20, 548), "V1", "UNDERGROUND DRAINAGE PLAN",
                  "SCALE 1:45   FLOOR (-)6.100   FALLS, GULLIES AND COLLECTION")
    V.underground_plan(sh, M, sc, bays=True, rooms=True, stair=True, esc=True)
    V.bay_room_labels(sh, M, y=4850, h=NOTE)
    _zone_shading(sh, M)

    # sump, pumps, filter trains, service plate
    sh.rect(*M(*D.SUMP_RECT[:2]), *M(*D.SUMP_RECT[2:]), "P-EQUIP")
    sh.text("SU-01  1500 x 1500 x 1500", M(11818, 2560), NOTE, "P-EQUIP", "BC")
    sh.text("3.375 m3  IL (-)7.600  [C]", M(11818, 2250), NOTE, "P-EQUIP", "BC")
    for i, (px, py) in enumerate(D.SUMP_PUMPS, 1):
        sh.sym("PUMP", M(px, py), scale=0.9)
        sh.text(f"PU-0{i}", M(px, py - 600), NOTE, "P-EQUIP", "BC")
    sh.rect(*M(*D.SERVICE_PLATE[:2]), *M(*D.SERVICE_PLATE[2:]), "P-DRAIN-RISING")
    sh.pipe([M(11800, 2400), M(11800, 5600)], "P-DRAIN-RISING",
            "PD-05  DN50 RISING MAIN")
    sh.text("SERVICE ENTRY PLATE - THE ONLY ENVELOPE PENETRATION  [C]",
            M(11800, 6450), NOTE, "M-FLAG", "BC")

    # gullies and the spine
    for tag, x, y, l, ty, seal, sv, z, c in D.DRAINS:
        if z in ("Z1", "Z2", "Z3"):
            sh.sym("GULLY", M(x, y), scale=0.9)
            sh.text(tag, M(x, y + 460), NOTE, "P-EQUIP", "BC")
    sh.pipe([M(4510, 3100), M(11068, 3100), M(11068, 2400)], "P-DRAIN-WASTE",
            "PD-01  DN100  1:100  BW-01")

    # falls
    for no, x0, x1, cw, rno, rname in P.BAYS[:5]:
        xm = (x0 + x1) / 2.0
        sh.flow(M(xm, 5000), -90, 2.8, "P-FLOW")
        sh.flow(M(xm, 1200), 90, 2.8, "P-FLOW")
        g = 80 if no in (2, 5) else 100
        sh.text(f"FF 1:{g}", M(xm, 3900), NOTE, "M-TEXT", "BC")
    sh.flow(M(8000, 3100), 0, 3.4, "P-FLOW")
    sh.text("SPINE FALLS 1:400 EAST TO THE SUMP  [A]", M(7600, 2300), NOTE,
            "M-TEXT", "BC")
    # upstands
    for xu, lab in ((12700, "50 UPSTAND AT W5"), (15000, "50 UPSTAND AT BD1")):
        sh.line(M(xu, 600), M(xu, 5600), "M-FLAG")
        sh.text(lab, M(xu, -700), NOTE, "M-FLAG", "BC")

    sh.dim_h(M(0, -1400), M(22000, -1400), M(0, -2200)[1], sc=sc)

    # ---- V2  transverse section through bay 5
    s2 = 25.0
    N = X.vw(s2, 548.0, 640.0)      # model x = plan Y, model y = level in mm
    sh.view_title((550, 548), "V2", "TRANSVERSE SECTION  -  BAY 5 ON THE SUMP",
                  "SCALE 1:25   FLOOR FALLS, SCREED AND THE MAT")
    # structure
    sh.rect(*N(0, -6700), *N(600, -2900), "M-STRUCT")          # south wall
    sh.rect(*N(5600, -6700), *N(6200, -2900), "M-STRUCT")      # north wall
    sh.rect(*N(0, -6700), *N(6200, -6100), "M-STRUCT")         # mat
    sh.rect(*N(0, -6800), *N(6200, -6700), "M-EXISTING")       # blinding
    sh.line(N(600, -2900), N(5600, -2900), "M-STRUCT")         # roof soffit
    sh.text("600 MAT  -  NOT CUT, NOT CHASED", N(3100, -6420), NOTE,
            "M-STRUCT", "CENTER")
    sh.text("100 M15 BLINDING", N(3100, -6770), 2.0, "M-EXISTING", "CENTER")
    # tanking membrane
    sh.line(N(0, -6800), N(6200, -6800), "M-WATERPROOF")
    sh.line(N(0, -6800), N(0, -2900), "M-WATERPROOF")
    sh.line(N(6200, -6800), N(6200, -2900), "M-WATERPROOF")
    sh.text("CONTINUOUS TANKING MEMBRANE  -  R-805", N(3100, -2700), NOTE,
            "M-WATERPROOF", "CENTER")
    # sump
    sh.rect(*N(900, -7600), *N(2400, -6100), "P-EQUIP")
    sh.rect(*N(900, -8000), *N(2400, -7600), "M-STRUCT")
    sh.sym("PUMP", N(1650, -7200), scale=0.9)
    sh.text("SU-01", N(1650, -6900), NOTE, "P-EQUIP", "CENTER")
    sh.text("IL (-)7.600", N(1650, -7750), 2.0, "M-LEVEL", "CENTER")
    sh.text("400 BASE - C18 OPEN, 400 HELD", N(2600, -7900), 2.0, "M-FLAG", "ML")
    # screed with falls, exaggerated
    sh.pline([N(600, -6100), N(600, -6022), N(3100, -6075), N(5600, -6022),
              N(5600, -6100)], "A-FIN-WET")
    sh.text("SCREED 25 AT THE SPINE  ->  78 AT THE WALL", N(3100, -5900),
            NOTE, "A-FIN-WET", "CENTER")
    sh.text("AREA-AVERAGE 52 mm = 1.24 kPa  vs  1.0 kPa SIDL  -  DR-F4",
            N(3100, -5650), NOTE, "M-FLAG", "CENTER")
    sh.sym("GULLY", N(3100, -6075), scale=0.8)
    sh.flow(N(1800, -5960), 0, 2.6, "P-FLOW")
    sh.flow(N(4400, -5960), 180, 2.6, "P-FLOW")
    # PD-01 recess
    sh.rect(*N(2950, -6316), *N(3250, -6100), "M-FLAG")
    sh.text("PD-01 RECESS  -  BW-01, NOT ACCEPTED", N(3400, -6250), NOTE,
            "M-FLAG", "ML")
    sh.dim_v(N(0, -6700), N(0, -6100), N(-500, 0)[0], sc=s2)
    sh.dim_v(N(6200, -6100), N(6200, -2900), N(6500, 0)[0], sc=s2)
    V.section_datum(sh, N, -900, 6200, -6.100, "FLOOR / TOP OF MAT")
    V.section_datum(sh, N, -900, 6200, -2.900, "ROOF SOFFIT")

    sh.text("V3   FLOOR GRADING SCHEDULE   -   zone 1", (550, 300),
            T["view_title"], "M-TITLE")
    sh.table(550, 292, [26, 66, 34, 30, 30, 84], [
        ("U-01", "EMERGENCY STORES", "2900", "1:100", "25 mm", "GY-01, then the spine"),
        ("U-02", "LAVATORY + MEDICAL", "1800", "1:80", "31 mm", "GY-02 -> PD-01, wet area"),
        ("U-03", "OPS ROOM", "3500", "1:100", "25 mm", "GY-03, then the spine"),
        ("U-04", "BERTHING", "1800", "1:100", "25 mm", "GY-04, then the spine"),
        ("U-05", "CBRN PLANT + SUMP", "1560", "1:80", "31 mm", "Direct fall to SU-01, wet area"),
        ("U-06", "DECON AIRLOCK", "2000", "1:80", "31 mm", "ZONE 2 - SEGREGATED, see D-203"),
        ("", "spine, X 600 to the sump", "11200", "1:400", "28 mm", "Y 3100, through the door gaps"),
    ], header=["ROOM", "SPACE", "RUN", "FALL", "DROP", "OUTLET"], h=2.1, rh=6.0,
        layer="M-TABLE")

    y = sh.panel(CA, 258, 396, "NOTES  -  UNDERGROUND DRAINAGE", [
        "1  FALLS ARE FORMED IN THE FLOOR SCREED, NEVER CUT INTO THE 600 MAT.  The mat is part of the tank and",
        "   is the most heavily utilised element in the project (84 %, master B.3).  Cutting falls into it would",
        "   reduce the section and the 75 cover to the bottom curtain.",
        "2  ADOPTED GRADING, ZONE 1:  transverse 1:80 in wet areas and 1:100 elsewhere over a 2500 run to the",
        "   spine at Y 3100; the spine then falls 1:400 east to the sump.  Screed 25 at the sump edge rising to",
        "   78 at the far corner, AREA-AVERAGE 52 mm.",
        "3  DR-F4 - REFERRED, NOT ASSUMED.  The mat SIDL allowance is 1.0 kPa, which at 24 kN/m3 buys only 42 mm",
        "   of screed.  The 52 mm area-average is 1.24 kPa: an EXCESS OF 0.24 kPa = 25 kN over the 104 m2 floor.",
        "   That is 1.2 % of the mat's own weight and 0.4 % of the 6289 kN uplift, and it acts in the FAVOURABLE",
        "   direction for flotation - but it is a change to a stated design load in master A.7.2 and it is not",
        "   made silently.  STRUCTURAL ENGINEER TO ACCEPT, or reduce the falls.",
        "4  BW-01 - REQUESTED, NOT ACCEPTED.  PD-01 is the ONLY buried drain inside the envelope.  It needs a 300",
        "   wide recess in the top of the mat, 150 deep at GY-02 rising to 216 at the sump, leaving 384 of the",
        "   600 mat locally, on the line of the peak transverse sagging moment.  STRUCTURAL ENGINEER TO ACCEPT",
        "   OR REFUSE.",
        "5  IF BW-01 IS REFUSED (FALLBACK):  the Bay 2 basin wastes discharge over a tundish to the graded floor,",
        "   the floor carries the water to the sump along the spine, and THERE IS NO BURIED DRAIN INSIDE THE",
        "   ENVELOPE AT ALL.  Gullies GY-01 to GY-04 then become washdown and rodding points only.  Both",
        "   arrangements work hydraulically - 400 L/day is 1/1450 of a DN100 pipe's capacity.",
        "6  DR-F5 - HYDRAULIC ZONING.  The protective boundary cuts the shelter into three zones and water may",
        "   not cross between them.  ZONE 1 (bays 1-5) drains to the clean sump - complete.  ZONE 2 (bay 6",
        "   decon) is segregated and its recorded destination, tank TK-01, is drawn in BAY 8, across the",
        "   boundary - ROUTE UNDEFINED, see D-203.  ZONE 3 (bays 7 and 8) HAS NO DRAINAGE DESTINATION AT ALL.",
        "   50 UPSTANDS AT W5 AND AT BLAST DOOR 1 keep zone 2 and zone 3 water out of zone 1.",
        "7  ALL TRAPS 75 mm DEEP SEAL, PRIMED.  See D-001 note 6.",
    ], h=NOTE, lead=LEAD)

    X.evidence_key(sh, CA, y - 8)
    sh.finish(scale="1:45", sheet_of="6 OF 11")
    return sh


# =====================================================================
def d203():
    sh = sheet("D-203", "UNDERGROUND WASTEWATER AND SANITARY PLAN",
               "SEGREGATED DECON EFFLUENT - FIXTURES - THE UNDEFINED ROUTES",
               flags=("DR-D2", "DR-D4", "DR-F5"), of="7 OF 11")

    sc = 45.0
    M = X.vw(sc, 40.0, 400.0)
    sh.view_title((20, 548), "V1", "WASTEWATER AND SANITARY PLAN",
                  "SCALE 1:45   FLOOR (-)6.100")
    V.underground_plan(sh, M, sc, bays=True, rooms=True, stair=True, esc=True)
    V.bay_room_labels(sh, M, y=4850, h=NOTE)
    _zone_shading(sh, M)

    # Bay 2 fixtures
    sh.sym("GULLY", M(4510, 3100), scale=0.9)
    sh.text("GY-02", M(4510, 3600), NOTE, "P-EQUIP", "BC")
    sh.text("SN-01 BASIN + SN-02 MEDICAL WASH-UP", M(4510, 2300), NOTE,
            "M-TEXT", "BC")
    sh.text("DN40 WASTES OVER THE GRATING, AIR GAP  [A]", M(4510, 1900), NOTE,
            "M-TEXT", "BC")
    sh.text("SN-03 SEALED-CASSETTE CHEMICAL TOILET  [C]", M(4510, 1500), NOTE,
            "M-TEXT", "BC")
    sh.text("NOTHING IS DISCHARGED IN PROTECTIVE MODE", M(4510, 1100), NOTE,
            "M-FLAG", "BC")
    sh.pipe([M(4510, 3100), M(11068, 3100), M(11068, 2400)], "P-DRAIN-WASTE",
            "PD-01  DN100  1:100")

    # case B provisional
    sh.dline(M(4510, 3500), M(4510, 5800), "M-FLAG")
    sh.dline(M(4510, 5800), M(9000, 5800), "M-FLAG")
    sh.text("PD-15  CASE B ONLY - PROVISIONAL, NOT ADOPTED", M(6800, 6000),
            NOTE, "M-FLAG", "BC")

    # Bay 6 decon
    sh.rect(*M(12800, 600), *M(14800, 5600), "P-DRAIN-EFF")
    ys = 600
    for tag, dx, dy in P.DECON_STAGES:
        sh.line(M(12800, ys + dy), M(14800, ys + dy), "P-DRAIN-EFF")
        ys += dy
    for tag, x, y, l, ty, seal, sv, z, c in D.DRAINS:
        if z == "Z2":
            sh.sym("GULLY", M(x, y), scale=0.9)
            sh.text(tag, M(x, y + 460), NOTE, "P-DRAIN-EFF", "BC")
    sh.sym("CHAMBER", M(14500, 3100), scale=0.9)
    sh.text("CP-01  SEALED", M(14500, 3600), NOTE, "P-DRAIN-EFF", "BC")
    sh.pipe([M(13800, 4600), M(13800, 3100), M(14500, 3100)], "P-DRAIN-EFF",
            "PD-03  DN100  SEGREGATED")

    # the undefined route to TK-01
    sh.rect(*M(*D.DECON_TANK[:2]), *M(*D.DECON_TANK[2:]), "P-DRAIN-EFF")
    sh.text("TK-01  1000 L DECON EFFLUENT TANK", M(20800, 4200), NOTE,
            "P-DRAIN-EFF", "BC")
    sh.text("DRAWN IN BAY 8 ON S-06  [C]", M(20800, 3800), NOTE,
            "P-DRAIN-EFF", "BC")
    sh.text("TANKER ONLY", M(20800, 3400), NOTE, "M-FLAG", "BC")
    sh.dline(M(14700, 3100), M(20198, 4900), "M-FLAG")
    sh.text("PD-04  *** ROUTE NOT DEFINED ***", M(17400, 4400), NOTE,
            "M-FLAG", "BC")
    sh.text("CROSSES W6 AND W7 - THE PROTECTIVE BOUNDARY", M(17400, 4000), NOTE,
            "M-FLAG", "BC")

    # Bay 8
    sh.sym("GULLY", M(19900, 3100), scale=0.9)
    sh.text("GY-09  NO DESTINATION  [N]", M(19900, 2500), NOTE, "M-FLAG", "BC")

    sh.dim_h(M(0, -1400), M(22000, -1400), M(0, -2200)[1], sc=sc)

    sh.text("V2   WASTEWATER ROUTES AND THEIR STATUS", (550, 548),
            T["view_title"], "M-TITLE")
    sh.table(550, 538, [30, 74, 60, 106], [
        ("PD-01", "GY-02 -> clean sump", "DN100 1:100", "ADOPTED.  BW-01 recess - not accepted"),
        ("PD-02", "GY-01/03/04 -> floor", "no pipe", "ADOPTED.  Bays 1, 3, 4 fall to the spine"),
        ("PD-03", "GY-06/07/08 -> CP-01", "DN100 1:100", "ADOPTED.  SEGREGATED throughout"),
        ("PD-04", "CP-01 -> TK-01 bay 8", "-", "*** ROUTE NOT DEFINED - crosses W6 and W7 ***"),
        ("PD-07", "GY-09 bay 8", "-", "*** NO DESTINATION IN ZONE 3 ***"),
        ("PD-15", "lavatory -> septic", "PUMPED", "*** CASE B ONLY - provisional, not adopted ***"),
        ("SN-01", "wash basin, U-02", "DN40", "Over the GY-02 grating, air gap"),
        ("SN-02", "medical wash-up, U-02", "DN40", "Over the GY-02 grating, air gap"),
        ("SN-03", "cassette toilet, U-02", "NO DISCHARGE", "Protective mode - nothing is discharged  [C]"),
        ("SN-04", "decon shower, stage 2", "to GY-07", "SEGREGATED.  Shower count not recorded  [N]"),
        ("SN-06", "WC, peacetime", "DN100", "*** CASE B ONLY - not specified, not sized ***"),
    ], header=["ID", "FROM / TO", "SIZE", "STATUS"], h=2.1, rh=6.2,
        layer="M-TABLE")

    y = sh.panel(CA, 258, 396, "NOTES  -  WASTEWATER AND SANITARY", [
        "1  SEGREGATION IS ABSOLUTE.  No clean drain, gully, trap or channel is connected to a decon effluent",
        "   drain, anywhere.  The two systems share no pipe, no chamber, no vent and no discharge point.",
        "   S-06: 'DECON EFFLUENT NEVER ENTERS THE CLEAN SUMP - TANKERED OUT AFTER THE ALL-CLEAR'.",
        "2  DR-D2 - THE PEACETIME FOUL ROUTE FROM THE BAY 2 LAVATORY IS NOT DEFINED ANYWHERE IN THE PROJECT.",
        "   S-06 records sealed-cassette chemical toilets in protective mode ('nothing is discharged') and a",
        "   peacetime septic tank sized for 10 users, but no connection between the two.  TWO READINGS:",
        "      CASE A  cassette in all modes - DRAWN.  No soil stack, no soil branch, no foul rising main below",
        "              ground.  The 450 L/day is entirely above ground.  Cassette handling is an O&M task.",
        "      CASE B  plumbed lavatory in peacetime - SHOWN DASHED AS PD-15, PROVISIONAL, NOT ADOPTED.  Needs",
        "              a macerator or packaged pumping unit AND A SECOND PENETRATION OF THE PROTECTIVE",
        "              ENVELOPE.  That is a protective-design decision, not a drainage one.",
        "   NO PUMP, MACERATOR, RISING MAIN SIZE OR PENETRATION IS SPECIFIED FOR CASE B.  ENGINEER TO CONFIRM.",
        "3  DR-D4 / DR-F5 - S-06 DRAWS TANK TK-01 IN BAY 8, at X 20198-21398, Y 4400-5600, and assigns airlock",
        "   stages 1 and 2 to it.  Bay 6 is inside the gas-tight envelope; bay 8 is outside the protective",
        "   boundary.  ANY PIPED ROUTE BETWEEN THEM CROSSES W6 AND W7 AND PASSES THROUGH THE STAIR SHAFT.  No",
        "   such route is drawn or described anywhere in the project.  Both ends are shown at their recorded",
        "   positions and the connection is shown DASHED AND UNDEFINED.  The alternatives are (a) two blast and",
        "   gas-tight boundary crossings, or (b) manual transfer in sealed containers after the all-clear.",
        "   BOTH ARE PROTECTIVE-DESIGN DECISIONS.  ENGINEER TO CONFIRM.  Nothing is assumed across the boundary.",
        "4  GY-09 IN BAY 8 HAS NO DRAINAGE DESTINATION.  Zone 3 cannot drain into zone 1 without breaching the",
        "   boundary, and no grey-zone outlet is recorded.  DATA REQUIRED.",
        "5  FIXTURE COUNTS, POSITIONS AND RIM HEIGHTS ARE NOT RECORDED ANYWHERE IN THE PROJECT.  The fixtures",
        "   shown are those the project's own text implies - master A.3 (lavatory + medical), S-06 (cassette",
        "   toilets, decon airlock) and the Rev F ground plan (hose-down point).  DATA REQUIRED for the rest.",
    ], h=NOTE, lead=LEAD)

    X.evidence_key(sh, CA, y - 8)
    sh.finish(scale="1:45", sheet_of="7 OF 11")
    return sh


SHEETS = [(d101, "D-101_Above_Ground_Entry_Level_Drainage_Plan"),
          (d102, "D-102_Rainwater_Catchment_and_Surface_Water_Plan"),
          (d103, "D-103_Entry_Stairwell_and_Headhouse_Drainage"),
          (d201, "D-201_Underground_Drainage_Plan"),
          (d203, "D-203_Underground_Wastewater_and_Sanitary_Plan")]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, name in SHEETS:
        fn().save(os.path.join(OUT, name + ".dxf"))
        print("  ", name + ".dxf")
