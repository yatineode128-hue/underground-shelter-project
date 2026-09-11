"""cm_data.py  --  the above-ground signature inventory behind C-101.

Every element that stands above finished grade, with its confirmed height and,
where the project records one, its confirmed position.  Sizes and levels come
from mep_proj.py (the shared confirmed geometry) or, for the sentry post, from
master A.4.1 and the A.4.3 level schedule, cited on each line.

TWO THINGS ARE NOT RECORDED ANYWHERE IN THE PROJECT and are not invented here:

  *  the POSITION of the sentry post.  The record gives a siting RULE - at
     least 10 m clear of the shelter excavation - and no coordinate.
  *  the POSITION of either air shaft, and the HEAD LEVEL of SH-2.

There is no site plan at all (master open item D3), so no element's position on
the ground is known except relative to the box.  C-101 says so on its face.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, "..", "..",
                                                 "Drainage", "Scripts")))
import mep_proj as P                                       # noqa: E402

REV = "CAM2"
DATE = "10.09.2026"
PACKAGE = "SITE AND CONCEALMENT"

# ---------------------------------------------------- sentry post, master A.4.1
SP = dict(w=4000, d=5000, ffl=+0.450, first=+3.650, roof=+6.700, parapet=+7.000,
          siting_min_m=10.0, stair_r=1000, stair_pole=250)

HH_W = P.HH["x1"] - P.HH["x0"]                             # 4800
HH_D = P.HH["y1"] - P.HH["y0"]                             # 5800
ASW_W = P.ASW["x1"] - P.ASW["x0"]                          # 6800
ASW_D = P.ASW["y1"] - P.ASW["y0"]                          # 2000
COVER = int((P.LVL["grade"] - P.LVL["slab_top"]) * 1000)    # 2000

# element, top level (m), width in X (mm), note, class
SIGNATURE = [
    ("SENTRY POST", SP["parapet"], SP["w"],
     f"{SP['w']} x {SP['d']}, two storeys, FFL {SP['ffl']:+.3f} / first "
     f"{SP['first']:+.3f} / roof {SP['roof']:+.3f}.  THE TALLEST THING ON THE "
     f"SITE BY 4.5 m", "[C] size and level  /  [N] position"),
    ("COVERED ENTRY STAIRWELL", P.LVL["asw_head"], ASW_W,
     f"{ASW_W} x {ASW_D}, soffit {P.LVL['asw_soffit']:+.3f}.  OUTSIDE THE "
     f"PROTECTIVE BOUNDARY, DECLARED EXPENDABLE", "[C]"),
    ("FRESH-AIR SHAFT SH-1", +1.500, 600,
     "600 x 600 gooseneck, west of the box", "[C] level  /  [N] position"),
    ("HEADHOUSE", P.LVL["hh_top"], HH_W,
     f"{HH_W} x {HH_D}, walls {P.HH['t_wall']}, roof {P.HH['t_roof']}, "
     f"NO EARTH COVER.  The largest above-ground mass", "[C]"),
    ("ESCAPE SHAFT ESC 2 HEAD", P.ESC[1][3], P.ESC_COLLAR_OD,
     f"{P.ESC_CLEAR_D} dia clear, {P.ESC_COLLAR_T} RC collar, OD "
     f"{P.ESC_COLLAR_OD}, at X {P.ESC[1][1]}", "[C]"),
    ("ESCAPE SHAFT ESC 1 HEAD", P.ESC[0][3], P.ESC_COLLAR_OD,
     f"{P.ESC_CLEAR_D} dia clear, {P.ESC_COLLAR_T} RC collar, OD "
     f"{P.ESC_COLLAR_OD}, at X {P.ESC[0][1]}", "[C]"),
    ("GENERATOR AIR SHAFT SH-2", None, 600,
     "600 x 600, east of the box, serves BV-4 / BV-5.  HEAD LEVEL NOT "
     "RECORDED ANYWHERE", "[C] size  /  [N] level and position"),
    ("SENTRY POST SPIRAL STAIR", SP["roof"], SP["stair_pole"],
     f"External, {SP['stair_r']} R, {SP['stair_pole']} dia central pole",
     "[C] with the post"),
    ("SOAK PIT AND SOAKAWAY COVER SLABS", 0.000, None,
     "SK-01 and SK-02 RC cover slabs, at grade.  POSITIONS NOT FIXED",
     "[C] existence  /  [N] position"),
]

# what the design already does, master A.7.3 / A.4.3 / BS1        [C] unless noted
PROVIDED = [
    f"TOPSOIL / TURF OVER THE WHOLE BURIED ROOF, 300 mm  -  the top layer of "
    f"the {COVER} engineered cover.",
    "   A.7.3 names its function as CONCEALMENT, EROSION, SHEDS RAIN.",
    "TURF SOURCED FROM THE SITE ITSELF  -  92.82 m3 stripped and stockpiled at "
    "E-01a for re-use  [A].",
    "   The re-laid surface is the surface that was there before, which is what "
    "usually gives a buried",
    "   structure away.",
    "FINISHED GRADE CROWNED, FALLING 1:50 AWAY (A.4.3)  -  a natural-looking "
    "shed, not a flat platform.",
    "BERM AGAINST THE HEADHOUSE AND COVERED STAIRWELL, 1.5:1 to +0.900  "
    "[C] / quantity [N].",
    f"NO ROOF PENETRATION FOR DRAINAGE ANYWHERE.  No outlet, no downpipe, no "
    f"rainwater pipe on the buried",
    "   roof - D-001 note 1.  The burster slab is laid to a 1:50 crossfall "
    "(BS1) so infiltration",
    "   disperses at the berm toe WITHOUT A PIPE, so there is no manhole, no "
    "gully and no outfall",
    "   anywhere on the roof to break the surface.",
    "SURPLUS EXCAVATION RE-USED ON SITE, 1 113.937 m3 as engineered fill and "
    "crushed rubble (E-08)  [D].",
]
