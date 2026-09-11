"""sg_data.py  --  the two supplied documents, transcribed.

EVERY VALUE IN THIS FILE IS READ OFF ONE OF THE TWO SUPPLIED DOCUMENTS AND IS
CLASSED [C].  Nothing is averaged, rounded, converted, corrected or completed
here.  Conversion and checking happen in sg_calc.py, where the arithmetic can
be shown.  Where a document is internally inconsistent the inconsistency is
transcribed as it stands and flagged; it is not tidied.

SOURCE 1  SEMT/67/15 - REPORT ON SUB-SOIL INVESTIGATION FOR CTW PH-III ACCN
          PROJECT AT CME PUNE.  Soil Engineering & Material Testing Wing,
          College of Military Engineering, Pune 411 031.  Requested by CTW
          letter No 8722/Ph-III/CTW/116/Q dated 20 May 2015.

SOURCE 2  P1 PRESENTATION DECK - "CONSTRUCTION OF CBRN HARDENED UNDERGROUND
          OPS ROOM", Team GROUNDZERO, 32 slides.

A NOTE ON WHOSE GROUND THIS IS.  The SEMT report investigates THREE NAMED
BUILDINGS on the CTW/CME campus - G Building, H Building and the Mess Building
- and not the project plot.  The project plot is an undeveloped area east of
the CTW blocks, near the perimeter fence (deck slides 13, 14, 22).  The report
may be extended to it only on the strength of the report's own paragraph 5,
which says the Deccan Trap flows "are horizontally bedded and more or less
uniform in character over a wide area."  That extension is an ASSUMPTION of
this package, not a finding of the report.
"""

# =====================================================================
# SOURCE 1  -  SEMT/67/15
# =====================================================================
REPORT = dict(
    title="REPORT ON SUB-SOIL INVESTIGATION FOR CTW PH-III ACCN PROJECT "
          "AT CME PUNE",
    author="Soil Engineering & Material Testing Wing, College of Military "
           "Engineering, Pune 411 031",
    code="SEMT/67/15",
    request="CTW letter No 8722/Ph-III/CTW/116/Q dated 20 May 2015",
    fieldwork_date=None,          # [N] the report nowhere states when the
                                  #     trial pits were actually dug
)

# para 5 - geology, verbatim
GEOLOGY = ("The area under investigation is underlain by the Deccan Trap "
           "formation. These are volcanic lava flows, which were poured out "
           "between the late cretaceous and early Eocene times. These "
           "basaltic flows are horizontally bedded and more or less uniform "
           "in character over a wide area.")

# para 6 - terrain, verbatim
TERRAIN = "The location for the proposed buildings is on fairly level ground."

# para 7 - seismic, verbatim
SEISMIC_REPORT = ("Pune falls under Seismic Zone III as per IS 1893 of 1984. "
                  "However, the earthquake activity in 1993 at Killari "
                  "(Latur, Maharastra) should be kept in mind while designing "
                  "the structure.")

# para 8 - meteorological data.  ABSOLUTE extremes, not design conditions.
TEMP_REPORT = dict(summer_max=40, summer_min=12, winter_max=26, winter_min=4)

# para 9 - rainfall, verbatim
RAINFALL_REPORT = ("The average annual rainfall in the region varies from "
                   "500-600 mm.")
RAINFALL_REPORT_RANGE = (500.0, 600.0)          # mm/year

# para 10 - field tests
FIELD = ("Excavation in open trench / trial pit by JCB was carried out and 11 "
         "trial pits were made.")
N_TRIAL_PITS = 11

# para 11 - laboratory tests, exactly as listed (the IS 1121 year is printed
# "1874" in the report; that is a typographical error for 1974 and is
# transcribed as printed - it is not silently corrected)
LAB_TESTS = [
    ("Soil Classification", "IS 2720 Pt IV-1975 & IS 1498-1970"),
    ("Free Swell test", "IS 2720 Pt XL-1977"),
    ("Soil compaction", "IS 2720 Part VIII-1983"),
    ("UCS test", "IS 2720 Pt X-1991"),
    ("Direct Shear Test", "IS 2720 Pt XIII-1986"),
    ("Compressive strength on Rock", "IS 1121 Pt I- 1874 [as printed]"),
]

# para 12 - soil profile, verbatim
PROFILE_TEXT = (
    "In the entire area under investigation, a thin soil (black cotton) cover "
    "of 0.18 m to 0.26 m is observed. However, at one or two locations the "
    "black cotton soil layer is found to be 0.5 m to 1.0 m deep. Murrum soil "
    "(Sand/Gravel soil) is encountered below the black cotton soil layer. "
    "This layer extends to an average depth of 0.18 to 1.2 m below GL. "
    "Disintegrated broken basalt rock is encountered below this murrum layer. "
    "In all trial pits, broken rock was encountered below a depth of 0.75 m "
    "to 1.6 m. Basalt rock is encountered below this murrum / broken rock, "
    "below a depth 0.9 m to 1.5 m.")

# para 13 - water table, verbatim.  THE SENTENCE THE WHOLE PACKAGE TURNS ON.
WATER_TABLE_TEXT = ("Water table was not encountered in any trial pit. "
                    "However, water table may raise during/after rainy "
                    "season.")

# para 14(a) - black cotton soil properties
BC_SOIL = dict(depth_m=(0.18, 1.0), LL=(61, 63), PL=(29, 30),
               free_swell=(60, 65), classification="CH")

# para 15 - findings of analysis.
# (location, [(layer description, soil/rock type, UCS soaked kg/cm2 or None,
#              SBC kg/cm2, note)])
FINDINGS = [
    ("G Building (TP-1 to TP-4)", [
        ("GL - 1.0 m", "High plasticity Clay (CH)", None, 0.27, ""),
        ("1.0 - 1.2 m", "Murrum (GM)", None, 4.27, ""),
        ("1.2 - 1.5 m", "Broken Rock", None, 10.0, "IS 12070 Table 2"),
        ("Below 1.5 m", "Basalt Rock", 509.0, 20.0, "soaked"),
    ]),
    ("H Building (TP-5 to TP-8)", [
        ("GL - 0.18 m", "High plasticity Clay (CH)", None, 0.25, ""),
        ("0.18 m - 0.7 m", "Murrum (GM)", None, 4.66, ""),
        ("0.7 m - 0.9 m", "Broken Rock", None, 10.0, "IS 12070 Table 2"),
        ("Below 0.9 m", "Basalt Rock", 513.0, 21.0, "soaked"),
    ]),
    ("Mess Bldg (TP-9 to TP-11)", [
        ("GL - 0.2 m", "Murrum (SC)", None, 2.07, ""),
        ("0.2 m - 0.5 m", "Murrum (GP)", None, 5.18, ""),
        ("0.5 m - 1.0 m", "Broken Rock", None, 10.0, "IS 12070 Table 2"),
        ("Below 1.0 m", "Basalt Rock", 529.0, 21.0, "soaked"),
    ]),
]

# the report's own footnote to the table, verbatim
BROKEN_ROCK_NOTE = (
    "The disintegrated broken basalt rock which is existing below murrum "
    "layer is having lot of cracks, fissures, voids and discontinuities. This "
    "layer is sandwiched between top murrum soil and basalt rock below. As "
    "per Table No 2 of para 2 of IS-12070-1987 the net safe bearing pressure "
    "is given as 10 Kg/cm2 for broken bedrock.")

# Appendix A - soil classification chart.  Location: CTW.
# (sample, depth, TP, gravel coarse, gravel fine, sand coarse, sand medium,
#  sand fine, silt, clay, LL, PL, PI, class, FSI)
APPX_A = [
    ("44/15", "GL-1.0",   "TP-1", None, 20, 4,  5,  4,  37, 30, 61, 29, 32,
     "CH", 60),
    ("45/15", "1.0-1.2",  "TP-1", 6,    51, 10, 7,  4,  20, 2,  None, None,
     None, "GM", None),
    ("46/15", "1.2-1.5",  "TP-1", None, None, None, None, None, None, None,
     None, None, None, "Broken Basalt Rocks", None),
    ("61/15", "GL-0.18",  "TP-8", None, 11, 5,  8,  6,  38, 32, 63, 30, 33,
     "CH", 65),
    ("62/15", "0.18-0.7", "TP-8", 14,   48, 8,  5,  2,  13, 10, None, None,
     None, "GM", None),
    ("63/15", "0.7-0.9",  "TP-8", None, None, None, None, None, None, None,
     None, None, None, "Broken Basalt Rocks", None),
    ("64/15", "GL-0.2",   "TP-9", 1,    10, 11, 20, 19, 31, 8,  30, 15, 15,
     "SC", None),
    ("65/15", "0.2-0.5",  "TP-9", 37,   50, 3,  2,  4,  3,  1,  None, None,
     None, "GP", None),
    ("66/15", "0.5-1.0",  "TP-9", None, None, None, None, None, None, None,
     None, None, None, "Broken Basalt Rocks", None),
]

# Appendix B - soil test result.  Location: CTW.
# (sample, TP, class, OMC %, MDD g/cc, UCS c kg/cm2, DS c kg/cm2, DS phi deg,
#  ultimate bearing kg/cm2, SBC kg/cm2)
APPX_B = [
    ("44/15", "TP-1", "CH", 10, 1.76, 0.13, None, None, 0.670, 0.27),
    ("45/15", "TP-1", "GM",  9, 1.93, None, 0.00, 33,   10.680, 4.27),
    ("61/15", "TP-8", "CH", 12, 1.78, 0.12, None, None, 0.617, 0.25),
    ("62/15", "TP-8", "GM",  8, 1.90, None, 0.00, 34,   11.650, 4.66),
    ("64/15", "TP-9", "SC", 10, 1.88, None, 0.01, 27,    5.170, 2.07),
    ("65/15", "TP-9", "GP",  8, 1.91, None, 0.00, 35,   12.950, 5.18),
]

# Appendix B remarks, verbatim
APPX_B_REMARKS = [
    "The soil sample is compacted to its maximum dry density and optimum "
    "moisture content.",
    "The recommended bearing capacity is calculated with factor of safety "
    "= 2.5 in submerged condition of soil.",
    "For SBC calculation the following value are assumed:- (a) Width of "
    "foundation (B) = 1200 mm.  (b) Depth of foundation (d) = 1500 mm.",
]
APPX_B_FOS = 2.5
APPX_B_B_MM = 1200
APPX_B_D_MM = 1500

# Appendix C - compressive strength & SBC of rock, IS 1121 (Pt-I) &
# IS 12070 Cl. 6.  (condition, depth, TP, max load kg, area cm2,
#                   compressive strength kg/cm2, SBC kg/cm2)
APPX_C = [
    ("UNSOAKED", "Below 1.5 m", "G- Building (TP-1)", 42356, 52.06, 814, 33),
    ("UNSOAKED", "Below 0.9 m", "H- Building (TP-8)", 21924, 29.15, 752, 30),
    ("UNSOAKED", "Below 1.0 m", "Mess Bldg (TP-9)",   57573, 63.96, 900, 36),
    ("SOAKED",   "Below 1.5 m", "G- Building (TP-1)", 24563, 48.30, 509, 20),
    ("SOAKED",   "Below 0.9 m", "H- Building (TP-8)", 14133, 27.56, 513, 21),
    ("SOAKED",   "Below 1.0 m", "Mess Bldg (TP-9)",   27033, 51.12, 529, 21),
]

DRAWINGS_REPORT = [
    ("Sketch 'P'", "Site Plan of CTW-III CME Pune Showing Location of trial "
                   "Pits"),
    ("Sketch 'Q'", "Trial Pit Details - Location CTW PH-III"),
]

# =====================================================================
# SOURCE 2  -  the P1 presentation deck
# =====================================================================
DECK = dict(
    title="CONSTRUCTION OF CBRN HARDENED UNDERGROUND OPS ROOM",
    team="TEAM GROUNDZERO",
    pages=32,
)

# slide 4 - operational pillars, verbatim
DECK_PILLARS = [
    "Kinteic Resilience : Survive 20 kT nuclear attack at 2.5 km from Ground "
    "Zero  [as printed]",
    "Electromagnetic Integrity : Total Volume Faraday Shielding",
    "Operational Autonomy : Self-sustaining life support and power generation",
]

# slide 7 - terms of reference, verbatim
DECK_TOR = [
    "Sustain Blast Pressure of 50 psi (345 kN/ sqm)",
    "EMP Shielding preferred",
    "Thermal insulation",
    "Able to accommodate 8-10 persons upto 96 Hrs",
    "Elevated Sentry Post (Double Storey)",
]

# slides 13, 14 - site location.  What the imagery shows, not measured.
DECK_SETTING = [
    "The plot is an undeveloped rectangle EAST of the two CTW blocks and WEST "
    "of the perimeter track and nullah line.",
    "CBRN LIVE TRG A lies to the SOUTH.",
    "North arrow shown; no scale bar, no grid, no boundary dimension, no "
    "coordinate.",
]

# slide 15 - contour map.  1 m contours, labelled 575 to 584.
DECK_CONTOURS = (575, 584)
DECK_CONTOURS_AT_SITE = (580, 581)   # the two that cross the plot
DECK_CONTOUR_FALL = "east / north-east, towards the track and nullah"

# slide 21 - elevation profile, read off the chart
DECK_ELEV_PROFILE = dict(x0=0.0, x1=26.8, z0=593.9, z1=596.2, zmid=595.0,
                         xmid=13.4)

# slide 22 - SWOT, verbatim
DECK_SWOT = dict(
    strength=["Proximity to FCBRNP", "Availability of electric lines",
              "Good road connectivity", "Good water supply", "No pipelines"],
    weakness=["Located near Perimeter Fence"],
    opportunity=["Enhanced trg opportunities",
                 "Live demo model to facilitate practical trg",
                 "Good connectivity"],
    threats=["Interference with CTW schedule"],
)

# slide 18 - pipelines sketch
DECK_PIPELINES = [
    "CTW LAKE to the north-west.",
    "PARADE GROUND 82.0 m x 82.0 m - the only dimensioned object on any "
    "supplied site sketch.",
    "RCC OH RESERVOIR, 15000 GLNS CAPACITY, 15 MTR STAGING, beside building "
    "527.",
    "SS-15 substation beside building 526.",
    "The SITE box is drawn OUTSIDE the pipe network - no main crosses it.",
]

# slide 24 - wind, monthly mean speed km/h, last 10 years average
DECK_WIND = [("January", 1.4), ("February", 2.1), ("March", 2.5),
             ("April", 3.6), ("May", 6.2), ("June", 6.6), ("July", 5.7),
             ("August", 5.2), ("September", 3.3), ("October", 1.6),
             ("November", 1.4), ("December", 1.2)]

# slide 25 - precipitation, monthly mm, last 10 years average
DECK_PRECIP = [("January", 0.1), ("February", 3.0), ("March", 5.5),
               ("April", 3.9), ("May", 19.0), ("June", 137.8),
               ("July", 166.2), ("August", 120.8), ("September", 134.9),
               ("October", 139.8), ("November", 22.7), ("December", 5.9)]

# slide 26 - temperature, monthly max / avg / min deg C, last 10 years average
DECK_TEMP = [("Jan", 29.8, 20.7, 11.6), ("Feb", 32.4, 23.2, 13.7),
             ("Mar", 35.5, 26.0, 16.7), ("Apr", 38.3, 29.3, 20.2),
             ("May", 37.8, 30.6, 23.1), ("Jun", 32.1, 27.6, 23.1),
             ("Jul", 28.5, 25.4, 22.3), ("Aug", 28.2, 24.8, 21.6),
             ("Sep", 29.7, 25.4, 21.1), ("Oct", 31.6, 25.6, 19.7),
             ("Nov", 30.9, 23.1, 15.2), ("Dec", 29.6, 21.7, 13.5)]

# slide 27 - seismic
DECK_SEISMIC_ZONE = "ZONE III"
DECK_SEISMIC_CODE = "IS 1893:2016"
DECK_SEISMIC_EVENTS = [
    ("28 Aug 1993", "Koyna area", 4.8),
    ("17 May 2004", "Katraj - Dive Ghats, Pune", 3.2),
    ("06 Jun 2007", "Katraj - Khadakwasla region, Pune", 2.6),
]

# slide 29 - soil investigation, verbatim.  Source line reads
# "Source : SEMT wing, CME PUNE".
DECK_SOIL_CLAIMS = [
    "Safe Bearing Capacity = 300 kN/m2 at 1.5 m depth from Top",
    "Ultimate Bearing Capacity = S.B.C x 2.5 = 750 kN/m2",
    "Water Table not encountered in any trial pit",
    "Might increase during monsoon",
    "Proposed structure safe for water table at depth of 2 m below GL",
]

# slide 30 - soil characteristics, verbatim
DECK_SOIL_CHAR = dict(
    bc=["Highly clayey soil.", "Contains about 60% of clay.",
        "During rain, it absorbs moisture and swells up.",
        "Contracts and produce cracks in dry season, 10 to 15 cm wide "
        "extending to maximum depth of 1m.",
        "Not suitable for foundation"],
    murrum=["It is reddish in color, Impervious in nature",
            "Product of disintegration of basalt rock",
            "Can be compacted easily.",
            "Good material for building path and huts.",
            "SBC of 25 - 30 kg/ cm2"],
    basalt=["Formed by volcanic lava flow poured out in late cretaceous time "
            "(about 145 ma ago)",
            "Compressive strength ranging from 609 - 900 kg/cm2 in unsoaked "
            "condition.",
            "Sufficient bearing capacity to support any engineering "
            "structure."],
)

# =====================================================================
# SOURCE 3  -  the Google Maps pin
# =====================================================================
# The project owner supplied https://maps.app.goo.gl/H2VjnrjS8X8SsXEr9 as the
# location of the project site.  The link could NOT be resolved in this
# session: the environment's egress policy refused maps.app.goo.gl (proxy 403,
# recorded).  No latitude, longitude or place name has therefore been read from
# it, and NONE IS INVENTED.  The link is recorded as the project's positional
# reference and the coordinates stay [N] until the owner supplies them.
PIN_URL = "https://maps.app.goo.gl/H2VjnrjS8X8SsXEr9"
PIN_LAT = None               # [N]
PIN_LON = None               # [N]
PIN_STATUS = ("NOT RESOLVED - maps.app.goo.gl refused by the session egress "
              "policy (403). Coordinates [N]; supply lat/long to close.")
