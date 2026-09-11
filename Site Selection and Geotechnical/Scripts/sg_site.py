"""sg_site.py  --  the SITE LAYOUT AND EXTERNAL WORKS data (revision SG2).

WHAT SG2 ADDS TO SG1.  SG1 recorded the site and the ground and resolved
nothing.  SG2 can resolve something, because the project owner has supplied
the two things that were missing:

    the coordinate      18.6089876 N,  73.8587287 E          [C] owner
    the availability    "the area around 50 m is all available"  [C] owner

With those, plus SG1's contours and geotechnical profile and the project's
own confirmed geometry, the positions that master H.9 recorded as *"not
determinable - no site plan, boundary or contour exists"* CAN be determined.
That is what this module holds.

WHAT IT STILL IS NOT.  A survey.  There is no boundary, no benchmark, no spot
level, no well position, no fence distance and no record of existing services
on the plot.  Master gap D3 is PARTIALLY closed - the LAYOUT now exists; the
SURVEY does not - and the residue is listed in the report.

THE LAYOUT IS ANCHORED TO CONFIRMED GEOMETRY ONLY.  Every position below is
dimensioned from the underground box, whose geometry is [C] throughout.
NOTHING is dimensioned from the sentry post, whose site position is [ASSUMED]
(master U4), so the layout survives U4 being resolved differently.  And every
offset is RELATIVE, so if the perimeter fence turns out to be closer than the
reserve's east edge, the whole reserve translates without any offset changing.
"""
import math

REV = "SG2"
PACKAGE_DATE = "11.09.2026"

# =====================================================================
# 1.  THE COORDINATE AND THE ENVELOPE                              [C]
# =====================================================================
PIN_LAT = 18.6089876
PIN_LON = 73.8587287
PIN_URL = "https://maps.app.goo.gl/H2VjnrjS8X8SsXEr9"
ENVELOPE_R = 50000.0          # mm, "the area around 50 m is all available"

# THE PIN CONVENTION.  The owner gave one point for "the project site".  The
# only self-consistent reading that lets everything be dimensioned is that it
# is the CENTRE OF THE UNDERGROUND BOX.  That is adopted here and stated as an
# adopted convention, not as a finding.  If the owner meant a corner or the
# entrance instead, THE WHOLE LAYOUT TRANSLATES RIGIDLY and not one offset,
# length or clearance below changes.                                      [A]
PIN_AT = (11000.0, 3100.0)    # project coordinates of the pin

# =====================================================================
# 2.  SITE ORIENTATION  -  fixed by SG2                            [A]
# =====================================================================
# Project +X = EAST.  Project +Y = NORTH.
#
# The project has always worked in a local frame (master A.4.1) and has never
# tied it to north.  SG2 fixes it, for five reasons that all point the same
# way:
#
#  1 ACCESS.  The covered entry stairwell's grade door is at its WEST end,
#    X 9250 (master A.4.7), so the approach comes from the west - and the CTW
#    blocks, the road network and the campus are west of the plot (deck slides
#    13, 14, 17).  Entry faces the installation it serves.            [C]
#  2 FALL.  SG1 read the ground as falling EAST / north-east, 580 -> 575
#    (deck slide 15).  With +X east, the drainage field is DOWNGRADIENT of the
#    structure and nothing recharges the ground upslope of a flotation-
#    critical tanked box.                                             [R]
#  3 SEPARATION OF INTAKE AND EXHAUST.  SH-1, the fresh-air intake, is west of
#    the box; SH-2, the generator air shaft, is at X 22598-23198, east.  The
#    orientation puts them at OPPOSITE ENDS, 22.6 m apart at minimum, whatever
#    the wind does - and no wind DIRECTION data exists anywhere in this
#    project (the deck gives speed only).  SG2-V4.                     [C]/[N]
#  4 NOISE AND SIGNATURE.  Bay 8 - the generator, ESC 2, SH-2, BV-4/BV-5 - is
#    at the east end, away from the campus.                            [C]
#  5 THE SENTRY POST covers the approach from the north (master U4's assumed
#    position), which is the side the approach is on.                  [A]
ORIENT_X = "EAST"
ORIENT_Y = "NORTH"

# =====================================================================
# 3.  WHAT IS ALREADY ON THE GROUND  -  all [C] unless marked
# =====================================================================
# name, x0, y0, x1, y1, class, note
EXISTING = [
    ("UNDERGROUND BOX, external", 0, 0, 22000, 6200, "[C]",
     "master A.4.2.  Roof top (-)2.000 under a 2000 engineered cover"),
    ("MAIN EXCAVATION + 1000 working space", -1000, -1000, 23000, 7200,
     "[C]/[A]", "WM1 BOQ derivation line 82; vertical unbenched faces, WM-V9"),
    ("COVERED ENTRY STAIRWELL", 9250, 5750, 16050, 7750, "[C]",
     "master A.4.7.  Grade door at the WEST end, X 9250"),
    ("STAIRWELL EXCAVATION + working space", 8250, 7200, 16050, 8750,
     "[C]/[A]", "WM1 BOQ derivation line 133"),
    ("ENTRY HEADHOUSE", 13600, 200, 18400, 6000, "[C]",
     "master A.4.6.  Top +0.900, NO EARTH COVER"),
    ("ENTRY THRESHOLD CHANNEL CH-10", 8950, 6000, 9250, 7500, "[C]",
     "300 channel + grating, master A.4.7.  Trapped catchpit CP-10"),
    ("SH-2 GENERATOR AIR SHAFT", 22598, 1750, 23198, 2350, "[C]",
     "HVAC equipment schedule.  600 x 600.  Head level NOT RECORDED - CAM-V5"),
    ("SERVICE ENTRY PLATE", 11398, 5600, 12198, 6200, "[C]",
     "NORTH wall.  The only services penetration of the envelope.  Its LEVEL "
     "is [N] - coordination item CO-1"),
    ("ESC 1 shaft collar, OD 1900", 1100, 1100, 3000, 3000, "[C]",
     "centre (2050, 2050), head +0.150"),
    ("ESC 2 shaft collar, OD 1900", 18950, 1100, 20850, 3000, "[C]",
     "centre (19900, 2050), head +0.700"),
    ("SENTRY POST  -  POSITION ASSUMED", 9000, 15250, 13000, 20250, "[A]",
     "master U4.  NO COORDINATE EXISTS.  Nothing in this layout is "
     "dimensioned from it"),
]

# SH-1 is deliberately NOT in the list above.  The HVAC equipment schedule
# gives SH-2 an X range and gives SH-1 only "West of the box".  Its plan
# position is recorded NOWHERE in the project.  SG2-V3.
SH1_NOTE = ("SH-1 FRESH-AIR SHAFT, 600 x 600, gooseneck head +1.500.  "
            "'West of the box' is the whole of what the project records.  "
            "NO X, NO Y, NO COORDINATE.  SG2-V3")

# =====================================================================
# 4.  THE EXTERNAL WORKS RESERVE                                   [A]
# =====================================================================
EWR = dict(x0=33000.0, y0=6500.0, x1=51000.0, y1=17500.0)

# Adopted clearances, and why each one is what it is.
# rule, value mm, class, basis
CLEARANCES = [
    ("Foul soak pit to any WELL", 15000, "[C]",
     "S-06, reproduced in drainage calculation D.11.  CANNOT BE DEMONSTRATED "
     "- no well position exists anywhere in the project.  SG2-V1"),
    ("Foul soak pit to the SEPTIC TANK", 5000, "[C]",
     "S-06, reproduced in drainage calculation D.11"),
    ("Soak pit to any BUILDING", 2000, "[C]",
     "S-06, reproduced in drainage calculation D.11"),
    ("FOUL group to any excavation face", 15000, "[A]",
     "THIS PACKAGE, and far beyond the 2 m code minimum.  Three reasons: the "
     "box is flotation-critical (FoS 0.33 at the mat-only stage); the side "
     "backfill is selected granular fill at 95 % MDD and is therefore MORE "
     "permeable than the basalt around it, so effluent would run preferen"
     "tially INTO the backfill and down the outside of the tanking; and a "
     "6.8 m deep vertical unbenched excavation has an influence zone the "
     "2 m rule was never written for"),
    ("CLEAN group to any excavation face", 10000, "[A]",
     "THIS PACKAGE.  Same reasoning, relaxed because the clean streams are "
     "groundwater and condensate - water that came out of the ground a few "
     "metres away - at 400 L/day"),
    ("FOUL group to CLEAN group", 5000, "[A]",
     "THIS PACKAGE.  S-06 requires the two to be SEPARATE and gives no "
     "distance; the septic-tank figure is borrowed as the nearest recorded "
     "analogue"),
    ("Pit wall to pit wall", 4000, "[A]",
     "THIS PACKAGE.  No pit-to-pit spacing rule is recorded in this project "
     "or cited on S-06.  4 m clear keeps the wetted zones of two 3.5 m deep "
     "pits from merging at the assumed absorption rate.  FOR THE GEOTECHNICAL "
     "ENGINEER TO CONFIRM"),
]

# =====================================================================
# 5.  THE EXTERNAL WORKS  -  positions fixed by SG2
# =====================================================================
# Pit levels are set RELATIVE TO LOCAL FINISHED GRADE at each pit, which is how
# a soak pit is built and the only way that is defensible here: there is no
# benchmark and the site fall is itself disputed (SG-V4).
PIT_DIA = 2200.0              # [C] RC1 ruling C19
PIT_TOP = -600.0              # mm below local grade, underside of cover slab
PIT_EFF = 3500.0              # [C] effective depth, RC1 kept it unchanged
PIT_INV = PIT_TOP - PIT_EFF   # -4100 below local grade

# tag, kind, centre x, centre y, class, serves
CIRCULAR = [
    ("SK-02", "STORM SOAKAWAY", 35000.0, 8500.0, "[A]",
     "Clean sump rising main PD-06 + entry threshold channel PD-11"),
    ("SK-03", "STAIRWELL SOAKAWAY", 41400.0, 8500.0, "[A]",
     "Stairwell sump SU-02 rising main PD-13.  SIZE NOT RECORDED ANYWHERE "
     "in the project - the 2.2 dia footprint is RESERVED, not designed"),
    ("SK-04", "HEADHOUSE SOAKAWAY", 47800.0, 8500.0, "[A]",
     "Headhouse gully GY-11 via PD-14.  SIZE NOT RECORDED ANYWHERE - "
     "footprint RESERVED.  PD-14's route is UNDETERMINED - SG2-F5"),
    ("SK-01", "FOUL SOAK PIT", 44000.0, 16000.0, "[A]",
     "Septic tank ST-01 effluent via PD-16, 450 L/day"),
]

# tag, kind, x0, y0, x1, y1, class, note
RECTANGULAR = [
    ("ST-01", "SEPTIC TANK", 36000.0, 15625.0, 37500.0, 16375.0, "[A]",
     "1.50 x 0.75 liquid, 1.00 deep + 300 freeboard = 1.30 overall.  "
     "IS 2470 (Pt 1) Table 1, up to 10 users.  50 cowled vent >= 2 m above "
     "grade, Cl. 6.9"),
    ("IC-02", "INSPECTION CHAMBER", 39900.0, 15775.0, 40500.0, 16225.0, "[A]",
     "600 x 450 on PD-16, for septic tank de-sludging access"),
    ("IC-01", "INSPECTION CHAMBER", 7200.0, 9575.0, 7800.0, 10025.0, "[A]",
     "600 x 450 on PD-11 at the change of direction"),
]

# The two sub-zones reserved for the FALLBACK, if the percolation test fails.
# tag, x0, y0, x1, y1, what
FALLBACK = [
    ("DF-1  FOUL DISPERSION FIELD", 33500.0, 10500.0, 48000.0, 17000.0,
     "IS 2470 (Pt 2) Cl. 5 dispersion trenches for the 450 L/day foul "
     "stream, IF the percolation test kills the deep pit"),
    ("DF-2  CLEAN DISPERSION FIELD", 33500.0, 6800.0, 48000.0, 10300.0,
     "The same, for the 400 L/day clean stream"),
]

# =====================================================================
# 6.  THE PIPE RUNS  -  the five lengths master H.9 called "not determinable"
# =====================================================================
# tag, from, to, DN, gradient, polyline of (x, y), class, note
RUNS = [
    ("PD-16", "ST-01 outlet", "SK-01 inlet", 100, "1:100",
     [(37500, 16000), (42900, 16000)], "[R]",
     "Straight, with IC-02 on it.  The shortest run in the layout and the "
     "one that matters most - it carries septic effluent"),
    ("PD-06", "SERVICE ENTRY PLATE", "SK-02", 50, "PUMPED",
     [(11798, 6200), (11798, 6700), (16500, 6700), (16500, 9800),
      (35000, 9800), (35000, 9600)], "[R]",
     "50 mm rising main.  Leaves the plate northward into the side backfill "
     "corridor (Y 6200-7200), runs EAST to clear the stairwell excavation at "
     "X 16050, then joins the COMMON SERVICES TRENCH at Y 9800.  Its VERTICAL "
     "leg is not determinable - the service entry plate's level is [N], "
     "coordination item CO-1"),
    ("PD-11", "CP-10 entry catchpit", "SK-02", 100, "1:100",
     [(9100, 6750), (7500, 6750), (7500, 9800), (35000, 9800),
      (35000, 9600)], "[R]",
     "Gravity DN100.  Routed WEST first, to X 7500, because going north from "
     "CP-10 would cross the stairwell excavation (X 8250-16050).  IC-01 sits "
     "at the change of direction, and from there it shares the COMMON "
     "SERVICES TRENCH with PD-06 and PD-13 - which is what makes a long run "
     "affordable in rock: one trench, three pipes"),
    ("PD-13", "SU-02 stairwell sump", "SK-03", 50, "PUMPED",
     [(15050, 6750), (16500, 6750), (16500, 9800), (41400, 9800),
      (41400, 9600)], "[R]",
     "50 mm rising main with a non-return valve [C].  Joins the common "
     "services trench at X 16500"),
    ("PD-14", "GY-11 headhouse gully", "SK-04", 100, "1:80",
     [], "[U]",
     "*** ROUTE UNDETERMINED - SG2-F5. *** GY-11 is at (14700, 1960) with "
     "its invert at (-)2.150, and the headhouse floor IS the top of the 900 "
     "pressure slab at (-)2.000.  The gully body and its outlet therefore "
     "sit 150 mm INSIDE the pressure slab, and outside the headhouse walls "
     "that level is beneath the waterproof membrane and inside the "
     "engineered cover, which no pipe may enter.  SK-04's footprint is "
     "RESERVED; its pipe cannot be routed until the outlet is resolved"),
]

COMMON_TRENCH = [(7500, 9800), (47800, 9800)]

# =====================================================================
# 7.  THE PERCOLATION TEST  -  where it has to be done
# =====================================================================
PERC_TESTS = [
    ("PT-1", 44000.0, 16000.0, "AT SK-01, the foul pit position"),
    ("PT-2", 35000.0, 8500.0, "AT SK-02, the clean pit position"),
]
PERC_DEPTH = PIT_INV          # test at the proposed pit invert

# =====================================================================
# 8.  RAINFALL  -  what SG2 can and cannot establish
# =====================================================================
# The session's egress policy refused EVERY meteorological host probed
# (imd.gov.in, imdpune.gov.in, mausam.imd.gov.in, data.gov.in, tropmet.res.in,
# en.wikipedia.org, climate-data.org, power.larc.nasa.gov, climexp.knmi.nl,
# ncei.noaa.gov - ten of ten, 403).  NO IMD NORMAL WAS RETRIEVED AND NONE IS
# INVENTED.  What follows is one published figure with a NAMED STATION and a
# NAMED PERIOD, which is enough to settle WHICH of the project's two
# conflicting figures is the wrong one - and no more than that.
RAIN_ANCHOR = dict(
    value=852.5, unit="mm", season="June to October",
    station="Pune, Shivajinagar observatory",
    period="1978-2020, 42 years",
    source="Mongabay India commentary, 'Long term rainfall patterns and "
           "flooding in Pune city' (2021), citing IMD Shivajinagar data",
    cls="[R] published analysis of IMD station data - NOT an IMD normal",
)
RAIN_AUTHORITY = [
    "IMD Pune, 'Climatological Tables of Observatories in India 1991-2020' - "
    "imdpune.gov.in/library",
    "IMD Climate Data Services Portal - cdsp.imdpune.gov.in, and the Station "
    "Climatological Normals service at dsp.imdpune.gov.in",
    "IMD National Data Centre, Shivajinagar, Pune - ndc@imd.gov.in",
    "ASK FOR: the station normal for the observatory nearest CME Dapodi, "
    "monthly and annual, with the station index number and the period of "
    "record printed on it.  AND SEPARATELY, an IDF relation - the 50 mm/h in "
    "this project has no return period, duration or source (DR-D1), and a "
    "monthly total can never supply one.",
]


# =====================================================================
# helpers
# =====================================================================
def dist_point_rect(px, py, r):
    """Clear distance from a point to an axis-aligned rectangle (0 if inside)."""
    x0, y0, x1, y1 = r
    dx = max(x0 - px, 0.0, px - x1)
    dy = max(y0 - py, 0.0, py - y1)
    return math.hypot(dx, dy)


def dist_circle_rect(cx, cy, dia, r):
    """Clear distance from a circle's WALL to a rectangle."""
    return dist_point_rect(cx, cy, r) - dia / 2.0


def dist_rect_rect(a, b):
    """Clear distance between two axis-aligned rectangles."""
    ax0, ay0, ax1, ay1 = a
    bx0, by0, bx1, by1 = b
    dx = max(bx0 - ax1, 0.0, ax0 - bx1)
    dy = max(by0 - ay1, 0.0, ay0 - by1)
    return math.hypot(dx, dy)


def dist_circle_circle(c1, c2, dia=PIT_DIA):
    return math.hypot(c1[0] - c2[0], c1[1] - c2[1]) - dia


def dist_circle_rect_named(cx, cy, rect, dia=PIT_DIA):
    return dist_circle_rect(cx, cy, dia, rect)


def run_length(pts):
    return sum(math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1))


def radius_from_pin(x, y):
    return math.hypot(x - PIN_AT[0], y - PIN_AT[1])


def side_area(dia, h):
    return math.pi * dia / 1000.0 * h / 1000.0
