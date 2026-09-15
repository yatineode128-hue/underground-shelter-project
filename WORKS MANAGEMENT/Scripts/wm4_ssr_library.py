"""
wm4_ssr_library.py — the SSR 2022-23 rate library, read out of the user's PDF.

Underground CBRN-hardened blast-resistant protective structure + sentry post, Pune.
Works Management package revision WM4.

SOURCE.  "SSR 22-23 MH (1).pdf" in the project root — Government of Maharashtra,
Public Works Department, STATE SCHEDULE OF RATES for the year 2022-23, approved by
Government Circular RADASU-2022/PR.KR.12/NIYOJAN-3 dated 25 July 2022, effective
from 25 July 2022.  624 pages.

EVERY rate below was read from that PDF and then re-verified against the raw page
text a second time, item by item — see QAQC/WM4_SSR_VERIFICATION.txt.  The three
that a first pass got wrong (21.40, 39.50) were corrected against the page.
NOTHING here is remembered, inferred or carried over from any other schedule.

Column meanings, from the SSR's own table head:
    completed  "Completed Rate for 2022-23 excluding GST, In Rs."
    labour     "Labour Rate for 2022-23 excluding GST, In Rs."
    page       printed page of the SSR (the PDF page is this + 7)
"""

# ---------------------------------------------------------------------------
# A.  COMPLETED ITEM RATES
# ---------------------------------------------------------------------------
# item -> dict(chapter, desc, unit, completed, labour, page)

SSR = {

    # ---- Chapter 21, Building Works: Excavation -----------------------------
    "21.02": dict(chapter="Excavation", unit="m3", completed=207, labour=116, page=153,
                  desc="Excavation for foundation in earth, soil of all types, sand, gravel "
                       "and soft murum, including removing the excavated material up to a "
                       "distance of 50 m beyond the building area and stacking and spreading "
                       "as directed, dewatering, preparing the bed for the foundation and "
                       "necessary back filling, ramming, watering including shoring and "
                       "strutting etc. complete. (Lift upto 1.5 m.) By Mechanical Means"),
    "21.04": dict(chapter="Excavation", unit="m3", completed=258, labour=144, page=153,
                  desc="Excavation for foundation in earth, soils of all types, sand, gravel "
                       "and soft murum ... (Lift from 1.5 m to 3.0 m) By Mechanical Means"),
    "21.20": dict(chapter="Excavation", unit="m3", completed=1307, labour=889, page=155,
                  desc="Excavation for foundation in Hard rock by chiselling, wedging, line "
                       "drilling, etc. including trimming and levelling the bed, removing the "
                       "excavated material upto a distance of 50 metres beyond the building "
                       "area, stacking as directed, dewatering and back filling with available "
                       "earth/murum, watering, ramming etc. complete. (Lift upto 1.5 m.) "
                       "By Mechanical Means"),
    "21.22": dict(chapter="Excavation", unit="m2", completed=107, labour=6, page=155,
                  desc="Providing preconstructional antitermite treatment as per IS 6313 "
                       "(Part-II) by treating the bottom surface and sides of excavation at "
                       "the rate of 5 litres of emulsion concentrate of 1.0 percent "
                       "chlorpyrifos per square metre etc. complete"),
    "21.33": dict(chapter="Excavation", unit="m2", completed=7, labour=7, page=157,
                  desc="Labour charges for removing grass, thorny shrubs, jungli shrub, "
                       "kubabul and alike grass, making the ground clean by shovel and "
                       "phavaras etc. complete"),
    "21.36": dict(chapter="Excavation", unit="m3", completed=120, labour=120, page=157,
                  desc="Filling in plinth and floors with approved excavated material in "
                       "15 cm to 20 cm layers including watering and compacting etc. complete"),
    "21.37": dict(chapter="Excavation", unit="m3", completed=599, labour=135, page=157,
                  desc="Filling in plinth and floors with contractor's material / brought from "
                       "outside and approved by Engineer in charge in layers of 15 cm to 20 cm "
                       "including watering and compaction etc. complete"),
    "21.38": dict(chapter="Excavation", unit="m3", completed=1382, labour=432, page=157,
                  desc="Providing dry / trap / granite / quartzite / gneiss rubble stone soling "
                       "15 cm to 20 cm thick including hand packing and compacting etc. complete"),
    "21.39": dict(chapter="Excavation", unit="m3", completed=2160, labour=120, page=157,
                  desc="Providing and filling in the foundation with sand of approved quality "
                       "including watering, compacting etc. complete. (To be executed with "
                       "prior approval of Superintending Engineer)"),
    "21.40": dict(chapter="Excavation", unit="m3", completed=1454, labour=436, page=157,
                  desc="Providing soling using 80 mm size trap metal in 15 cm layer including "
                       "filling voids with crushed sand / grit, ramming, watering etc. complete"),

    # ---- Chapter 24, Plain Cement Concrete ----------------------------------
    "24.01": dict(chapter="Plain Cement Concrete", unit="m3", completed=5830, labour=1616, page=175,
                  desc="Providing and laying cast in situ / ready mix cement concrete in M-10 of "
                       "trap / granite / quartzite / gneiss metal for foundation and bedding "
                       "including bailing out water, steel centering, formwork, laying / pumping, "
                       "compacting and curing etc. complete.  The SSR's own consumption table "
                       "gives nominal PCC 1:3:6 and M-10 the SAME 4.40 bags/m3, so 24.01 is the "
                       "published item for a 1:3:6 levelling bed"),
    "24.04": dict(chapter="Plain Cement Concrete", unit="m3", completed=6359, labour=1616, page=175,
                  desc="Providing and laying cast in situ / ready mix cement concrete in M15 of "
                       "trap / granite / quartzite / gneiss metal for foundation and bedding / "
                       "steps including steel centering, formwork, laying / pumping, compacting, "
                       "roughening them if special finish is to be provided, finishing uneven and "
                       "honeycombed surface and curing etc. complete. With fine aggregate "
                       "(Crushed sand VSI grade)"),

    # ---- Chapters 25 / 26, Reinforced Cement Concrete -----------------------
    "25.15": dict(chapter="Reinforced Cement Concrete", unit="m3", completed=7471, labour=2110, page=178,
                  desc="Providing and laying cast in situ / ready mix cement concrete M-30 of "
                       "trap / granite / quartzite / gneiss metal for R.C.C. work in foundations "
                       "like raft, strip foundations, grillage and footings of R.C.C. columns and "
                       "steel stanchions etc. ... including steel centering, formwork, cover "
                       "blocks, laying / pumping, compaction, finishing ... and curing etc. "
                       "complete, (EXCLUDING reinforcement and structural steel)"),
    "25.17": dict(chapter="Reinforced Cement Concrete", unit="m3", completed=7562, labour=2110, page=178,
                  desc="As 25.15 but grade M-35."),
    "25.35": dict(chapter="Reinforced Cement Concrete", unit="m3", completed=14150, labour=5252, page=180,
                  desc="Providing and laying cast in situ / ready mix cement concrete M-30 ... for "
                       "R.C.C. COLUMNS as per detailed designs and drawing ... including steel "
                       "centering, formwork, cover blocks ... (EXCLUDING reinforcement)"),
    "25.54": dict(chapter="Reinforced Cement Concrete", unit="m3", completed=12635, labour=5085, page=181,
                  desc="Providing and laying cast in situ / ready mix cement concrete M-30 ... for "
                       "R.C.C. BEAMS AND LINTELS ... including steel centering, formwork, cover "
                       "blocks ... (EXCLUDING reinforcement)"),
    "25.74": dict(chapter="Reinforced Cement Concrete", unit="m3", completed=14299, labour=5988, page=183,
                  desc="Providing and laying cast in situ / ready mix cement concrete M-30 ... for "
                       "R.C.C. SLABS AND LANDINGS ... including steel centering, formwork, cover "
                       "blocks ... (EXCLUDING reinforcement)"),
    "25.76": dict(chapter="Reinforced Cement Concrete", unit="m3", completed=14391, labour=5988, page=183,
                  desc="As 25.74 but grade M-35."),
    "26.19": dict(chapter="Reinforced Cement Concrete", unit="m3", completed=15750, labour=7338, page=185,
                  desc="Providing and laying cast in situ / ready mix cement concrete in M-25 ... "
                       "for R.C.C. PARDI (wall) of required thickness including steel centering, "
                       "formwork, cover blocks ... (EXCLUDING reinforcement).  M-25 is the HIGHEST "
                       "grade the SSR publishes for this item"),
    "26.26": dict(chapter="Reinforced Cement Concrete", unit="m3", completed=12244, labour=5219, page=186,
                  desc="Providing and laying cast in situ / ready mix cement concrete in M-25 ... "
                       "for R.C.C. WAIST SLAB AND STEPS OF STAIRCASES ... (EXCLUDING "
                       "reinforcement).  M-25 is the HIGHEST grade the SSR publishes for this item"),
    "26.33": dict(chapter="Reinforced Cement Concrete", unit="t", completed=89703, labour=11762, page=188,
                  desc="Providing and fixing in position TMT Fe-500 bar reinforcement of various "
                       "diameters for R.C.C. pile caps, footings, foundations, slabs, beams, "
                       "columns, canopies, staircase, newels, chajjas, lintels, pardis, copings, "
                       "fins, arches etc. as per detailed designs, drawings and schedules, "
                       "including cutting, bending, hooking the bars, binding with wires or tack "
                       "welding and supporting as required, complete"),

    # ---- Chapter 27, Brick Work --------------------------------------------
    "27.05": dict(chapter="Brick Work", unit="m3", completed=7994, labour=1705, page=197,
                  desc="Providing second class burnt brick masonry with conventional / IS type "
                       "bricks in cement mortar 1:6 in SUPERSTRUCTURE including striking joints, "
                       "raking out joints, watering and scaffolding etc. complete"),

    "27.06": dict(chapter="Brick Work", unit="m2", completed=1119, labour=203, page=197,
                  desc="Providing second class burnt brick masonry with conventional / IS type "
                       "bricks in cement mortar 1:4 in HALF BRICK THICK WALL including mild steel "
                       "longitudinal reinforcement of 2 bars of 6 mm dia / 2 hoop iron strips "
                       "25 x 1.6 mm at every third course, scaffolding etc. complete"),
    "27.08": dict(chapter="Brick Work", unit="m3", completed=9525, labour=2704, page=197,
                  desc="Providing FIRST class burnt brick masonry with conventional / IS type "
                       "bricks in cement mortar 1:4 including scaffolding, racking out joints, "
                       "pointing in CM 1:3 and watering etc. IN PILLARS of rectangular or square "
                       "shape.  NOTE: the SSR publishes NO first-class item for superstructure "
                       "WALLS — 27.08 and 27.09 are both pillar items"),

    # ---- Chapter 31 / 51, Water Proofing ------------------------------------
    "31.09": dict(chapter="Water Proofing", unit="m2", completed=615, labour=316, page=206,
                  desc="Providing and applying waterproofing treatment using acrylic polymer "
                       "modified cement based waterproofing coating with fibre glass mesh etc. "
                       "complete"),
    "31.12": dict(chapter="Water Proofing", unit="m2", completed=1286, labour=393, page=206,
                  desc="Providing and fixing 20 to 25 mm thick rough shahabad box type "
                       "waterproofing FOR BASEMENT OR UNDERGROUND FLOOR on a base of cement "
                       "concrete 1:3:6 ... with 7 years guarantee ... with ponding test etc. "
                       "complete (excluding cement concrete 1:3:6 base concrete)"),
    "31.13": dict(chapter="Water Proofing", unit="m2", completed=1338, labour=509, page=207,
                  desc="Providing and fixing 20 to 25 mm thick rough shahabad box type "
                       "waterproofing treatment TO VERTICAL OUTSIDE FACES OF REINFORCED CEMENT "
                       "CONCRETE WALLS OF BASEMENT or underground floor ... with 7 years "
                       "guarantee ... with ponding test etc. complete"),
    "51.114": dict(chapter="Water Proofing (new items 2019-20)", unit="m2", completed=678, labour=115, page=382,
                   desc="Providing and laying Hyperplas standard or equivalent POLYMERIC MULTIPLE "
                        "MONOLITHIC FIVE LAYER waterproofing flexible, pliable, high tensile "
                        "strength MEMBRANE (3 kg/m2) with a centre core of 90 micron thick high "
                        "molecular high density polyethylene film (HMHDPE) protected on both sides "
                        "with polymeric mix, applied by thermofusing after a primer, 10 cm "
                        "overlapping, with a 7 year guarantee.  (Prior written permission of the "
                        "Superintending Engineer is necessary before inclusion in an estimate)"),
    "51.115": dict(chapter="Water Proofing (new items 2019-20)", unit="m2", completed=390, labour=193, page=383,
                   desc="Providing and laying mechanical protective layer over waterproofing "
                        "membrane with cement screed plaster 1:5 after laying chicken mesh over "
                        "the membrane, 20 mm thick, including the cost of chicken mesh, curing, "
                        "and a 7 year guarantee"),

    # ---- Chapter 32, Plastering and Pointing --------------------------------
    "32.04": dict(chapter="Plastering and Pointing", unit="m2", completed=278, labour=204, page=209,
                  desc="Providing INTERNAL cement plaster 12 mm thick in single coat in cement "
                       "mortar 1:4 without neeru finish to concrete or brick surfaces, in all "
                       "positions, including scaffolding and curing etc. complete"),
    "32.11": dict(chapter="Plastering and Pointing", unit="m2", completed=639, labour=412, page=209,
                  desc="Providing SAND FACED plaster EXTERNALLY in cement mortar using approved "
                       "screened sand, in all positions, including base coat of 15 mm thick in "
                       "cement mortar 1:4 and a finishing coat, including scaffolding and curing "
                       "etc. complete"),

    "32.15": dict(chapter="Plastering and Pointing", unit="m2", completed=65, labour=56, page=210,
                  desc="Providing NEERU FINISH to plastered surfaces in all positions including "
                       "scaffolding and curing etc. complete"),

    # ---- Chapters 35 / 36, Oil Painting and Colouring -----------------------
    "35.25": dict(chapter="Oil Painting", unit="m2", completed=261, labour=172, page=226,
                  desc="Providing and applying two coats of EXTERIOR ACRYLIC EMULSION paint "
                       "conforming to the corresponding IS, of approved make, colour and shade, "
                       "including scaffolding and preparing the surface etc. complete"),
    "36.12": dict(chapter="Colouring", unit="m2", completed=80, labour=24, page=228,
                  desc="Providing and applying PLASTIC EMULSION paint of approved quality, colour "
                       "and shade to old and new surfaces in TWO coats including scaffolding and "
                       "preparing the surface etc. complete"),

    # ---- Chapter 33, Paving, Flooring and Dado (indicative only) ------------
    "33.24": dict(chapter="Paving, Flooring and Dado", unit="m2", completed=1182, labour=355, page=216,
                  desc="Providing and laying matt finish ceramic tiles 30 cm x 30 cm conforming "
                       "to IS 15622, on a bed of cement mortar, including cement float, filling "
                       "joints, curing etc. complete"),

    # ---- Chapter 39, Doors and Windows --------------------------------------
    "39.10": dict(chapter="Doors and Windows", unit="m2", completed=2913, labour=851, page=246,
                  desc="Providing and fixing solid core FLUSH DOOR SHUTTER, commercial, single "
                       "leaf, 32 mm thick, without ventilator, with necessary fixtures and "
                       "fastenings etc. complete.  SHUTTER ONLY — the frame is a separate item"),
    "39.50": dict(chapter="Doors and Windows", unit="m2", completed=5700, labour=1809, page=256,
                  desc="Providing and fixing in position ALUMINIUM OPENABLE WINDOW of any size as "
                       "per detailed drawing, with all necessary aluminium sections, fixtures and "
                       "fastenings, with 5 mm thick clear float glass etc. complete, with colour "
                       "anodising (section weight 6.90 kg/m2 considered)"),

    # ---- Chapter 40, Iron Work ---------------------------------------------
    "40.06": dict(chapter="Iron Work", unit="m", completed=1220, labour=286, page=264,
                  desc="Providing and fixing 40 mm diameter and 1.5 mm thick STAINLESS STEEL "
                       "HAND RAILING in SS 304 grade including fabrication, fixtures, erection "
                       "etc. complete"),
}


# ---------------------------------------------------------------------------
# B.  GENERAL MATERIAL RATES  (SSR "General Rates", printed page 541)
# ---------------------------------------------------------------------------
MATERIAL = {
    "Cement":                         (6000.0, "M.T."),
    "Structural Steel":              (62575.0, "M.T."),
    "TMT Fe-500":                    (61000.0, "M.T."),
    "HCRM / CRS reinforcement":      (63755.0, "M.T."),
    "Sand — natural / VSI artificial": (1670.0, "Cu.M."),
    "Sand — crushed":                 (1200.0, "Cu.M."),
    "Sand — natural screened (plaster only)": (1781.0, "Cu.M."),
    "Bricks — I class (red)":            (9.00, "No."),
    "Bricks — II class (red)":           (8.50, "No."),
    "Rubble stone (excluding royalty)": (653.0, "Cu.M."),
    "Aggregate 40 mm (hand broken, blasted, excl. royalty)": (900.0, "Cu.M."),
    "Aggregate 20 mm":                (1050.0, "Cu.M."),
    "Stone dust":                      (835.0, "Cu.M."),
    "Soft murum":                      (313.0, "Cu.M."),
    "Hard murum":                      (316.0, "Cu.M."),
    "Water":                           (213.0, "1000 litre"),
}

# ---------------------------------------------------------------------------
# C.  LABOUR RATES  (SSR "Labour Rates", printed page 545) — per day
# ---------------------------------------------------------------------------
LABOUR = {
    "Mason I class (skilled)": 677.0,
    "Carpenter I class (skilled)": 677.0,
    "Bar bender (skilled)": 677.0,
    "Vibrator operator (skilled)": 677.0,
    "Painter I class (skilled)": 677.0,
    "Welder (skilled)": 677.0,
    "Electrician": 677.0,
    "Maistry / supervisor / mate (skilled)": 677.0,
    "Jack hammer operator": 677.0,
    "Semi-skilled labour": 648.0,
    "Chiseler (semi-skilled)": 648.0,
    "Breaker (semi-skilled)": 648.0,
    "Bhisti, mixing / curing (semi-skilled)": 648.0,
    "Mukadam (semi-skilled)": 648.0,
    "Mazdoor — unskilled heavy": 615.0,
    "Helper — unskilled": 615.0,
    "Labour for excavation in hard rock (unblasted)": 615.0,
}

# ---------------------------------------------------------------------------
# D.  STANDARD CEMENT CONSUMPTION, bags of 50 kg per m3
#     SSR "Consumption of Material", printed pages 567-581
# ---------------------------------------------------------------------------
CEMENT_BAGS = {"M15": 6.00, "M20": 7.00, "M25": 7.50, "M30": 8.00,
               "M35": 8.25, "M40": 8.50}

# ---------------------------------------------------------------------------
# E.  GENERAL-NOTE FACTORS, Section B "Instructions for preparing estimate"
# ---------------------------------------------------------------------------
# Excavation for BUILDING works, increase on the basic rate of the item by depth
DEPTH_INCREASE = [
    (0.000, 3.000, 0.00,  "no increase"),
    (3.000, 4.500, 0.20,  "3.0 m to 4.50 m depth add 20 %"),
    (4.500, 6.000, 0.30,  "4.5 m to 6.0 m depth add 30 %"),
    (6.000, 99.99, None,  "Depth beyond 6.0 m — extra percent to be decided by "
                          "the concerned Superintending Engineer"),
]

# Floor lift, "For items of buildings having ground plus upper floors"
FLOOR_LIFT = {"ground": 0.00, "first": 0.01, "second": 0.02,
              "third": 0.03, "fourth": 0.04}

# Overheads and profit ALREADY inside every completed rate.  General Notes:
# "For labour amenities and all other overhead charges, 10% provision is
#  considered in Rate Abstract.  In addition, 10% provision for Contractor's
#  Profit is also considered separately."  Labour cess at 1% likewise.
OH_IN_RATE = 0.10
PROFIT_IN_RATE = 0.10
LABOUR_CESS_IN_RATE = 0.01

# The factor by which a change in material cost reaches the completed rate.
ON_COST = (1 + OH_IN_RATE) * (1 + PROFIT_IN_RATE) * (1 + LABOUR_CESS_IN_RATE)


def grade_uplift(base_grade, target_grade):
    """Rupees per m3 to be added to a published SSR concrete rate to carry it
    from base_grade to target_grade.

    The method is the SSR's own, General Notes Section B:
        "If higher Concrete grade is required for any specific work, the rate
         analysis of the same shall be derived by ADDING DIFFERENCE IN STANDARD
         CEMENT CONSUMPTION in relevant SSR item's rate and shall be got
         approved from the Superintending Engineer, PWD of concerned circle."

    Cement at the SSR general rate of Rs 6 000 / M.T. = Rs 6.00 / kg, a bag of
    50 kg, carried to the completed rate through the 10 % overheads, 10 %
    contractor's profit and 1 % labour cess that the rate abstract applies.

    The formula reproduces the SSR's own published inter-grade steps exactly:
    M20 -> M25 gives 183 against the 183/184 the SSR prints in four separate
    item families, and M30 -> M35 gives 92 against the SSR's 91/92.
    """
    d_bags = CEMENT_BAGS[target_grade] - CEMENT_BAGS[base_grade]
    return d_bags * 50.0 * (MATERIAL["Cement"][0] / 1000.0) * ON_COST
