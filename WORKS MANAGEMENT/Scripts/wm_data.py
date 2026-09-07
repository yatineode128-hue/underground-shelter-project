"""
wm_data.py — the single source of truth for the Works Management package.

Underground CBRN-hardened blast-resistant protective structure + sentry post, Pune.
Works Management package revision WM1.

Everything downstream — the WBS document, the MSPDI programme, the programme PDF,
the BOQ, the resource plan, the procurement plan, the QA/QC plan, the safety and
risk register and the handout — is generated from this file.  Edit here, re-run
wm_build_all.py, and every deliverable moves together.

Evidence classes follow the master project state file:
    [C] confirmed   [D] derived   [A] assumed by this package   [N] not available
    [U] unresolved

THE ONLY DESIGN CHANGE carried by this package is reference SP-B1:
    SENTRY POST WALLS ARE BRICK MASONRY, replacing the Rev F 200 RC ballistic
    infill panels.  Nothing else in the project is changed.
"""

from datetime import date

REV = "WM1"
REV_DATE = date(2026, 9, 7)

PROJECT = {
    "title": "Underground CBRN-Hardened Blast-Resistant Protective Structure "
             "and Sentry Post",
    "location": "Pune, Maharashtra",
    "programme_title": "Master Construction Programme — Complete Project",
    "revision": REV,
    "start": date(2026, 11, 2),          # Monday — carried from the supplied R0 .mpp
    "geometry_rev": "Architectural Rev F · Structural Phase 2 Rev A + M1",
    "services_rev": "Drainage DR1 · HVAC HV1 · Schedule of Finishes FN1 · "
                    "Structural CAD SC1",
}

# ---------------------------------------------------------------------------
# CALENDAR
# ---------------------------------------------------------------------------
# Six-day working week, Sunday non-working.  This is read from the supplied R0
# .mpp: 02-11-26 to 26-07-27 is 266 calendar days, of which 38 are Sundays,
# giving 228; the R0 file states 224 working days, i.e. six-day working with a
# handful of holidays.  The same convention is kept.  [D]
WORKING_DAYS = (0, 1, 2, 3, 4, 5)        # Mon..Sat  (Python weekday numbers)

# Only DATE-CERTAIN national holidays are entered.  Maharashtra festival
# holidays move year to year and are NOT invented here; the programme instead
# carries a stated contingency before handover.  [A]
FIXED_HOLIDAYS_MMDD = [
    (1, 26),    # Republic Day
    (5, 1),     # Maharashtra Day / Labour Day
    (8, 15),    # Independence Day
    (10, 2),    # Gandhi Jayanti
    (12, 25),   # Christmas Day
]
HOLIDAY_YEARS = (2026, 2027, 2028)

CALENDAR_NOTE = (
    "Six-day working week, Monday to Saturday; Sunday non-working.  Five "
    "date-certain national holidays are non-working.  Maharashtra festival "
    "holidays are NOT in the calendar because their dates move; the programme "
    "carries a stated contingency activity before handover to absorb them. "
    "Monsoon (June to September at Pune) is handled by productivity allowances "
    "inside the affected durations and by the sequencing rule that the deep "
    "excavation and the external tanking are kept out of the monsoon, not by "
    "making the calendar non-working."
)

# ---------------------------------------------------------------------------
# WBS
# ---------------------------------------------------------------------------
WBS = [
    ("1", "PRE-CONSTRUCTION AND ENABLING WORKS"),
    ("1.1", "Approvals, contract and site possession"),
    ("1.2", "Mobilisation and site establishment"),
    ("1.3", "Survey, setting out and design-parameter confirmation"),
    ("1.4", "Long-lead procurement — protective and specialist items"),

    ("2", "SITE PREPARATION AND EARTHWORKS"),
    ("2.1", "Site clearance and stripping"),
    ("2.2", "Temporary works and excavation protection"),
    ("2.3", "Bulk excavation — main shelter"),
    ("2.4", "Dewatering"),
    ("2.5", "Formation preparation and approval"),

    ("3", "MAIN UNDERGROUND SHELTER — SUBSTRUCTURE"),
    ("3.1", "Blinding and external tanking, horizontal"),
    ("3.2", "Mat foundation and sump pit"),
    ("3.3", "Perimeter walls W1–W4 and protective walls W5, W6, W7"),
    ("3.4", "Main staircase — lower flights (FROZEN geometry)"),

    ("4", "MAIN UNDERGROUND SHELTER — PRESSURE SLAB"),
    ("4.1", "Falsework and formwork"),
    ("4.2", "Reinforcement, openings and cast-in items"),
    ("4.3", "Concrete, curing and striking"),
    ("4.4", "Main staircase — upper flight and guarding"),
    ("4.5", "Internal partitions W8"),

    ("5", "ENTRY STRUCTURES, ESCAPE SHAFTS AND DOORS"),
    ("5.1", "Entry headhouse"),
    ("5.2", "Covered entry stairwell"),
    ("5.3", "Escape shafts ESC 1 and ESC 2"),
    ("5.4", "Blast doors, security door and external door"),

    ("6", "WATERPROOFING"),
    ("6.1", "External tanking, vertical"),
    ("6.2", "Roof waterproofing and protection"),
    ("6.3", "Above-ground roofs"),

    ("7", "BACKFILL, ENGINEERED COVER AND OVERBURDEN"),
    ("7.1", "Side backfill"),
    ("7.2", "Engineered cover build-up, 2000 layered"),
    ("7.3", "Burster slab M30"),
    ("7.4", "Verification of the cover"),

    ("8", "SENTRY POST"),
    ("8.1", "Setting out, excavation and footings F1"),
    ("8.2", "Frame — columns C1, plinth beam PB"),
    ("8.3", "Frame — first floor beams B1/B2 and slab S1"),
    ("8.4", "Frame — roof beams, slab, projection and parapet"),
    ("8.5", "BRICK MASONRY WALLS  (design change SP-B1)"),
    ("8.6", "Lintels and openings"),
    ("8.7", "Spiral stair"),
    ("8.8", "Plaster, flooring and finishes"),
    ("8.9", "Electrical installation"),

    ("9", "MECHANICAL, CBRN AND HVAC SERVICES"),
    ("9.1", "Builder's work, sleeves and penetrations"),
    ("9.2", "Shafts, ductwork and blast valves"),
    ("9.3", "CBRN plant and generator"),

    ("10", "DRAINAGE AND SANITARY WORKS"),
    ("10.1", "Internal drainage and the clean sump"),
    ("10.2", "Segregated decontamination effluent"),
    ("10.3", "Above-ground and external drainage"),

    ("11", "ELECTRICAL AND EMP WORKS"),
    ("11.1", "Concealed containment and earthing"),
    ("11.2", "EMP Zone 2 enclosure and penetration protection"),
    ("11.3", "Distribution, lighting and power"),

    ("12", "INTERNAL FINISHES"),
    ("12.1", "Substrate preparation and wet-area tanking"),
    ("12.2", "Floor finishes and skirtings"),
    ("12.3", "Wall and soffit finishes"),
    ("12.4", "Internal doors"),

    ("13", "EXTERNAL WORKS, CONCEALMENT AND RESTORATION"),
    ("13.1", "Berm, regrading and surface water"),
    ("13.2", "Access and hardstanding"),
    ("13.3", "Concealment and camouflage"),
    ("13.4", "Site restoration"),

    ("14", "TESTING, COMMISSIONING AND HANDOVER"),
    ("14.1", "Structural verification"),
    ("14.2", "Services testing"),
    ("14.3", "Protective-system testing"),
    ("14.4", "Commissioning"),
    ("14.5", "Completion and handover"),
]

# ---------------------------------------------------------------------------
# ACTIVITIES
# ---------------------------------------------------------------------------
# (id, wbs, name, duration_days, predecessors, resources, note)
#
# Predecessor syntax follows Microsoft Project:  "A3075", "A3090SS+6",
# "A3130FS-4", comma separated.  Duration 0 = milestone.
#
# "resources" is a semicolon-separated list of resource names defined in
# RESOURCES below.  Deliberately kept to the resources that actually do the
# work; the plan is not padded.

A = [
    # ================= 1  PRE-CONSTRUCTION =================================
    ("A1010", "1.1", "Contract award, signature and site possession", 5, "",
     "Project Manager", ""),
    ("A1015", "1.1", "Statutory and Service approvals; security clearance of the workforce",
     10, "A1010SS", "Project Manager", ""),
    ("A1020", "1.1", "Contractor's programme, method statements and quality plan — approval",
     10, "A1010", "Project Manager;Planning Engineer", ""),
    ("A1025", "1.1", "MILESTONE: Site possession and commencement", 0, "A1010",
     "", "M-01"),

    ("A1030", "1.2", "Site office, stores, labour accommodation and first-aid post", 8,
     "A1025", "Site Engineer (Civil);Unskilled gang", ""),
    ("A1035", "1.2", "Site boundary, security fencing, gate and access control", 6,
     "A1025", "Unskilled gang", "military site — access control is not optional"),
    ("A1040", "1.2", "Temporary water supply, storage and distribution", 5,
     "A1030SS+2", "Plumber gang", "curing demand governs, not domestic demand"),
    ("A1045", "1.2", "Temporary power supply and site distribution board", 5,
     "A1030SS+2", "Electrician gang", ""),
    ("A1050", "1.2", "Concrete supply arrangements and site testing laboratory", 8,
     "A1030", "Site Engineer (Civil);QA/QC Engineer", ""),
    ("A1055", "1.2", "Material stacking areas, reinforcement yard and bar-bending area",
     5, "A1030", "Unskilled gang;Bar bender gang", "stacking to IS 4082"),
    ("A1060", "1.2", "Plant mobilisation — excavator, breakers, crane, pumps, compactors",
     5, "A1035", "Site Engineer (Civil)", ""),
    ("A1065", "1.2", "MILESTONE: Mobilisation complete", 0,
     "A1030,A1035,A1040,A1045,A1050,A1055,A1060", "", "M-02"),

    ("A1070", "1.3", "Topographic survey, benchmarks and establishment of the site grid",
     4, "A1025", "Surveyor", "origin and axes to master A.4.1"),
    ("A1075", "1.3", "Confirmatory site investigation — boreholes, rockhead, red-bole seams",
     12, "A1070", "Site Engineer (Civil)",
     "rockhead (-)1.500/(-)2.000 is ASSUMED in the master"),
    ("A1080", "1.3", "Monsoon groundwater monitoring — confirm the design GWT (-)2.000",
     20, "A1075SS", "Site Engineer (Civil)",
     "the single most important assumption in the project"),
    ("A1085", "1.3", "Percolation test for the soak pits — IS 2470 (Part 2) Cl. 4", 5,
     "A1075", "Site Engineer (Civil)", "MANDATORY; likely to fail on basalt"),
    ("A1090", "1.3", "Issue confirmed geotechnical parameters to the designer", 5,
     "A1075,A1080,A1085", "Project Manager", "closes master K.2 assumptions"),
    ("A1095", "1.3", "Setting out — shelter box, headhouse and covered stairwell", 3,
     "A1070", "Surveyor", ""),
    ("A1100", "1.3", "Setting out — sentry post, not less than 10 m clear of the excavation",
     2, "A1095", "Surveyor", "master A.2 siting rule"),
    ("A1105", "1.3", "Setting-out check and independent verification", 2,
     "A1095,A1100", "Surveyor;QA/QC Engineer", ""),

    ("A1110", "1.4", "Blast doors 1 and 2 — specification, enquiry and technical evaluation",
     15, "A1020", "Project Manager", "1200 x 2100, 7 bar, gas-tight, rebound rated"),
    ("A1115", "1.4", "Blast doors — order placement", 5, "A1110", "Project Manager", ""),
    ("A1120", "1.4", "Blast door cast-in FRAMES — manufacture and delivery", 75,
     "A1115", "", "frames ship ahead of the leaves so they can be cast in"),
    ("A1122", "1.4", "Blast door LEAVES — manufacture, factory proof test and shipment",
     120, "A1115", "", "vendor item; master F.1 records it as NOT AVAILABLE"),
    ("A1130", "1.4", "CBRN filter trains AHU-1/AHU-2 — enquiry and order", 20,
     "A1020", "Project Manager", "duty 250 vs 300 m3/h is conflict C21, UNRESOLVED"),
    ("A1135", "1.4", "CBRN filter trains — manufacture and delivery", 100, "A1130",
     "", "EN 1822 H14 HEPA + ASZM-TEDA carbon"),
    ("A1140", "1.4", "Blast valves, 5 No. — enquiry and order", 20, "A1020",
     "Project Manager", "sizes not in master Part B — NOT AVAILABLE"),
    ("A1145", "1.4", "Blast valves and sleeves — manufacture and delivery", 100,
     "A1140", "", ""),
    ("A1150", "1.4", "EMP Zone 2 shielded enclosure — specialist enquiry and order", 25,
     "A1020", "Project Manager", "MIL-STD-188-125-1; 80 dB, 10 kHz–1 GHz"),
    ("A1155", "1.4", "EMP Zone 2 enclosure — manufacture and delivery", 80, "A1150",
     "", ""),
    ("A1160", "1.4", "Generator 15 kVA — enquiry, order and delivery", 60, "A1020",
     "Project Manager", ""),
    ("A1165", "1.4", "Armoured vision panels, 8 No. — enquiry, order and delivery", 80,
     "A1020", "Project Manager", "sentry post first storey; specification is [N]"),
    ("A1170", "1.4", "Submersible pumps and drainage plant — order and delivery", 45,
     "A1020", "Project Manager", ""),
    ("A1172", "1.4", "Reinforcement Fe500D — order, mill certificates and delivery", 30,
     "A1020", "Project Manager", "77.3 t including 5 % wastage"),
    ("A1174", "1.4", "Waterproofing system — approval of the proprietary system and order",
     30, "A1020", "Project Manager", "FN1 leaves the product deliberately open"),
    ("A1176", "1.4", "Modular bricks to IS 1077 — source approval, testing and order", 20,
     "A1020", "Project Manager", "SENTRY POST BRICK MASONRY — design change SP-B1"),
    ("A1175", "1.4", "MILESTONE: All long-lead protective items ordered", 0,
     "A1115,A1130,A1140,A1150,A1160,A1165,A1172,A1174,A1176", "", "M-03"),

    # ================= 2  EARTHWORKS =======================================
    ("A2010", "2.1", "Site clearance, grubbing and removal of plants and shrubs", 4,
     "A1065,A1105,A1015", "Excavator;Unskilled gang", ""),
    ("A2015", "2.1", "Strip topsoil 150 and stockpile for the concealment layer", 3,
     "A2010", "Excavator;Tipper", "93 m3 retained — do not cart away"),
    ("A2020", "2.1", "Site levelling, temporary haul road and hardstanding", 4,
     "A2015", "Excavator;Dozer/grader;Vibratory roller", ""),

    ("A2025", "2.2", "Design and approval of excavation support and slope treatment", 10,
     "A1090", "Site Engineer (Civil)", "soil zone above rockhead only"),
    ("A2030", "2.2", "Surface water cut-off drains and interceptor around the excavation",
     4, "A2020", "Unskilled gang", "keeps run-off out of a 6.8 m deep cut"),
    ("A2035", "2.2", "Excavation edge protection, barriers, signage and access ladders",
     3, "A2040SS+2", "Unskilled gang;Safety Officer", "IS 3764"),

    ("A2040", "2.3", "Excavation in soil and weathered overburden to rockhead", 4,
     "A2030,A2025", "Excavator;Tipper", "344 m3 at mean rockhead (-)1.750"),
    ("A2045", "2.3", "Rock excavation by hydraulic breaker, (-)1.750 to (-)4.000", 9,
     "A2040", "Excavator;Rock breaker;Tipper",
     "NO BLASTING — sentry post and existing works within influence"),
    ("A2050", "2.3", "Rock excavation by hydraulic breaker, (-)4.000 to (-)6.800", 11,
     "A2045", "Excavator;Rock breaker;Tipper", "994 m3 total rock at 60 m3/day"),
    ("A2055", "2.3", "Excavation for the covered entry stairwell approach", 5,
     "A2050SS+5", "Excavator;Tipper", ""),
    ("A2060", "2.3", "Excavation in rock for the sump pit, to (-)8.100", 3, "A2050",
     "Excavator;Rock breaker", ""),

    ("A2065", "2.4", "Install and commission the construction dewatering system", 3,
     "A2040", "Dewatering pumps;Plumber gang", ""),
    ("A2070", "2.4", "Dewatering — continuous through the substructure works", 110,
     "A2065", "Dewatering pumps",
     "level-of-effort activity; large float is correct, it is not a real slack"),

    ("A2075", "2.5", "Trim, dress and clean the formation; remove loose rock", 4,
     "A2050,A2060", "Unskilled gang;Excavator", ""),
    ("A2080", "2.5", "Inspect for red-bole and vesicular seams; over-excavate and "
     "replace with M15", 4, "A2075", "Site Engineer (Civil);Concrete gang",
     "master A.6 — a single red-bole seam sizes the mat"),
    ("A2085", "2.5", "HOLD POINT: formation inspection and approval by the Engineer", 2,
     "A2080,A2035", "QA/QC Engineer", "H-01"),
    ("A2090", "2.5", "MILESTONE: excavation complete, formation approved", 0, "A2085",
     "", "M-04"),

    # ================= 3  SUBSTRUCTURE =====================================
    ("A3010", "3.1", "Blinding PCC M15 100 thk under the mat", 3, "A2090",
     "Concrete gang", "14.2 m3"),
    ("A3015", "3.1", "Blinding PCC M15 to the sump pit", 1, "A2090", "Concrete gang", ""),
    ("A3020", "3.1", "External tanking WP-01 — horizontal, on the blinding", 5,
     "A3010,A3015,A1174", "Waterproofing gang", "the tank must be continuous"),
    ("A3025", "3.1", "Protection layer to the horizontal tanking", 2, "A3020",
     "Waterproofing gang", ""),
    ("A3030", "3.1", "HOLD POINT: tanking integrity inspection before covering", 1,
     "A3025", "QA/QC Engineer", "H-02"),

    ("A3035", "3.2", "Sump pit SU-01 — formwork and reinforcement below the mat", 4,
     "A3030", "Bar bender gang;Carpenter gang", ""),
    ("A3040", "3.2", "Mat reinforcement — bottom curtain T16 @ 150 each way", 4,
     "A3030,A1172", "Bar bender gang", "14.67 t in the mat group"),
    ("A3045", "3.2", "Wall starter bars, 900 leg into the mat; kickers set out", 3,
     "A3040", "Bar bender gang;Surveyor", "lap 800 = 50 phi above a 150 kicker"),
    ("A3050", "3.2", "Mat links T12 @ 250 x 250 grid, chairs and spacers", 3, "A3045",
     "Bar bender gang", ""),
    ("A3055", "3.2", "Mat reinforcement — top curtain T16 @ 150 each way", 4, "A3050",
     "Bar bender gang", ""),
    ("A3060", "3.2", "Mat edge formwork and U-bars; waterstops at the kicker", 3,
     "A3055", "Carpenter gang;Bar bender gang", ""),
    ("A3065", "3.2", "Cast-in items — drainage BW-01, sleeves, earth pits, EMP straps",
     3, "A3055", "Plumber gang;Electrician gang", ""),
    ("A3070", "3.2", "HOLD POINT: mat reinforcement, cover and cast-in inspection", 1,
     "A3060,A3065,A3035", "QA/QC Engineer;Structural Consultant", "H-03"),
    ("A3075", "3.2", "Concrete mat 600 M35 and sump pit — single continuous pour", 2,
     "A3070", "Concrete gang;Concrete pump;Transit mixer", "81.8 + 3.7 m3"),
    ("A3080", "3.2", "Curing of the mat — 14 days continuous", 14, "A3075",
     "Unskilled gang", "IS 456 Cl. 13.5; mass section"),
    ("A3085", "3.2", "MILESTONE: mat foundation cast", 0, "A3075", "", "M-05"),

    ("A3090", "3.3", "Wall reinforcement W1–W4 — both curtains T16 @ 150 each face, each way",
     12, "A3075FS+3", "Bar bender gang", "24.7 t in the wall group; 150 spacing is EMP-driven"),
    ("A3095", "3.3", "Wall reinforcement W5, W6, W7 incl. blast door jambs and header", 6,
     "A3090SS+6", "Bar bender gang", "4-T20 each jamb each face; header 400 x 1100"),
    ("A3100", "3.3", "Haunch reinforcement 500 x 500, diagonal T20 @ 150, wall/mat junction",
     3, "A3090SS+2", "Bar bender gang", ""),
    ("A3105", "3.3", "Set and align the BLAST DOOR FRAMES in W6 and W7; weld to the cage",
     4, "A3095,A1120", "Welding set;Site Engineer (Civil)",
     "EMP continuity — the frame is welded to the cage"),
    ("A3110", "3.3", "Concealed conduits, sleeves and penetrations cast into the walls", 5,
     "A3095", "Electrician gang;Plumber gang", ""),
    ("A3115", "3.3", "Wall formwork — lift 1, (-)6.100 to (-)4.500", 6, "A3095,A3100,A3080",
     "Carpenter gang", ""),
    ("A3120", "3.3", "HOLD POINT: wall reinforcement, frames and cover inspection — lift 1",
     1, "A3115,A3105,A3110,A9010", "QA/QC Engineer;Structural Consultant", "H-04"),
    ("A3125", "3.3", "Concrete walls — lift 1, M35", 2, "A3120",
     "Concrete gang;Concrete pump;Transit mixer", ""),
    ("A3130", "3.3", "Curing lift 1; strike vertical formwork after 24 h minimum", 7,
     "A3125", "Unskilled gang;Carpenter gang", "IS 456 Table 11"),
    ("A3135", "3.3", "Wall formwork — lift 2, (-)4.500 to (-)2.900", 6, "A3130FS-4",
     "Carpenter gang", ""),
    ("A3140", "3.3", "HOLD POINT: wall reinforcement and cover inspection — lift 2", 1,
     "A3135,A3155", "QA/QC Engineer", "H-05"),
    ("A3145", "3.3", "Concrete walls — lift 2, M35", 2, "A3140",
     "Concrete gang;Concrete pump;Transit mixer", ""),
    ("A3150", "3.3", "Curing lift 2 and strike wall formwork", 7, "A3145",
     "Unskilled gang;Carpenter gang", ""),
    ("A3155", "3.3", "Construction joint preparation — two waterstops and welded EMP strap",
     3, "A3125", "Waterproofing gang;Welding set",
     "joints at ~6 m; reinforcement fully continuous"),
    ("A3160", "3.3", "MILESTONE: perimeter and protective walls complete", 0, "A3150",
     "", "M-06"),

    ("A3165", "3.4", "Main staircase — formwork to flights 1 and 2 and landings L1, L2",
     5, "A3150", "Carpenter gang", "FROZEN: 24R @ 170.8333, tread 280, 3 flights x 8"),
    ("A3170", "3.4", "Main staircase — reinforcement, flights T12 @ 150, landings T12 @ 125",
     4, "A3165", "Bar bender gang", ""),
    ("A3175", "3.4", "Main staircase — concrete flights 1 and 2 and landings, M35", 2,
     "A3170", "Concrete gang", ""),
    ("A3180", "3.4", "Main staircase — curing and strike, lower flights", 7, "A3175",
     "Unskilled gang;Carpenter gang",
     "gives permanent access into the excavation, removing a temporary stair"),

    # ================= 4  PRESSURE SLAB ====================================
    ("A4010", "4.1", "Falsework and soffit deck to the pressure slab, 3.200 m height", 8,
     "A3150", "Carpenter gang;Scaffolding", "104 m2 of deck; IS 14687"),
    ("A4015", "4.1", "Edge formwork, stair void and escape shaft box-outs", 4, "A4010",
     "Carpenter gang", ""),

    ("A4020", "4.2", "Pressure slab — bottom curtain T25 @ 150 each way", 6, "A4015",
     "Bar bender gang", "20.5 t in the roof group; THE governing element"),
    ("A4025", "4.2", "Opening trimmers — stair void 6-T25 top and bottom; re-entrant "
     "corners 4-T25 at 45 degrees", 4, "A4020", "Bar bender gang", "UFC 3-340-02 §4-27"),
    ("A4030", "4.2", "Escape shaft collar trimmers 5-T25 each side/face/direction; hoops "
     "and radials", 4, "A4025", "Bar bender gang", ""),
    ("A4035", "4.2", "Local thickenings 900 to 1200 at the shafts and the void free edge",
     3, "A4030SS+1", "Carpenter gang;Bar bender gang", "3.3 m3 extra concrete"),
    ("A4040", "4.2", "Band beneath headhouse wall HW3 — 4-T25 extra top and bottom in a "
     "1200 band", 2, "A4025", "Bar bender gang", "HW3 has no wall below it"),
    ("A4045", "4.2", "Links T12 4-leg @ 250 in the end 1500; 2-leg @ 300 mid", 5,
     "A4030", "Bar bender gang", "IS 4991 Cl. 10.3.1.1 — no dynamic increase on shear"),
    ("A4050", "4.2", "Pressure slab — top curtain T25 @ 150 each way", 6, "A4045",
     "Bar bender gang", ""),
    ("A4055", "4.2", "Wall/roof haunches 500 x 500, diagonal T20 @ 150", 3, "A4050SS+2",
     "Bar bender gang", ""),
    ("A4060", "4.2", "Cast-in — blast valve sleeves, duct and pipe penetrations, EMP straps",
     5, "A4050", "Plumber gang;Electrician gang;Welding set", ""),
    ("A4065", "4.2", "Escape shaft collar starter bars", 2, "A4050", "Bar bender gang", ""),
    ("A4067", "4.2", "Concealed electrical conduits and boxes cast into the slab", 4,
     "A4045SS+2", "Electrician gang", ""),

    ("A4070", "4.3", "HOLD POINT: pressure slab pre-pour inspection — reinforcement, "
     "cover, cast-ins", 2, "A4055,A4060,A4065,A4035,A4040,A4067",
     "QA/QC Engineer;Structural Consultant", "H-06"),
    ("A4075", "4.3", "Concrete pressure slab 900 M35 — single continuous pour, 112 m3", 2,
     "A4070", "Concrete gang;Concrete pump;Transit mixer",
     "continuous pour preferred inside the protective envelope"),
    ("A4080", "4.3", "Curing of the pressure slab — 14 days continuous", 14, "A4075",
     "Unskilled gang", ""),
    ("A4085", "4.3", "MILESTONE: pressure slab cast — the key structural milestone", 0,
     "A4075", "", "M-07"),
    ("A4090", "4.3", "Strike soffit formwork and props — props to remain 14 days", 5,
     "A4080", "Carpenter gang", "IS 456 Table 11: slab spanning over 4.5 m"),
    ("A4095", "4.3", "Make good, hack and prepare the soffit", 3, "A4090",
     "Unskilled gang", ""),

    ("A4110", "4.4", "Main staircase — flight 3 to the top of the pressure slab (-)2.000",
     6, "A4090,A3180", "Carpenter gang;Bar bender gang;Concrete gang", ""),
    ("A4115", "4.4", "Main staircase — handrails and guarding 1100 high", 4, "A4110,A12035",
     "Welding set;Unskilled gang", "NBC 2016 Part 4"),

    ("A4100", "4.5", "Internal partitions W8, 4 No., 110 thk with A252 mesh both faces",
     6, "A4090", "Carpenter gang;Bar bender gang;Concrete gang",
     "non-structural; 900 door gap at Y 2500–3400"),

    # ================= 5  ENTRY STRUCTURES =================================
    ("A5010", "5.1", "Headhouse — wall starters, kicker and setting out on the pressure slab",
     3, "A4090", "Bar bender gang;Surveyor", ""),
    ("A5015", "5.1", "Headhouse wall reinforcement HW1–HW4, T16 @ 150 EF EW, T12 4L @ 250",
     6, "A5010", "Bar bender gang", "walls designed for 383 kPa either face — C10"),
    ("A5020", "5.1", "Inner security door frame in HW2 — cast in and welded to the cage",
     2, "A5015", "Welding set", "not blast rated, but EMP-continuous"),
    ("A5025", "5.1", "Headhouse wall formwork", 5, "A5015,A5020", "Carpenter gang", ""),
    ("A5030", "5.1", "HOLD POINT: headhouse wall inspection", 1, "A5025",
     "QA/QC Engineer", "H-07"),
    ("A5035", "5.1", "Concrete headhouse walls 400 M35", 1, "A5030",
     "Concrete gang;Concrete pump", ""),
    ("A5040", "5.1", "Curing and strike — headhouse walls", 5, "A5035",
     "Unskilled gang;Carpenter gang", ""),
    ("A5045", "5.1", "Headhouse roof falsework and formwork", 4, "A5040",
     "Carpenter gang;Scaffolding", ""),
    ("A5050", "5.1", "Headhouse roof reinforcement T20 @ 150 EF EW; T12 4L @ 175 / 250",
     5, "A5045", "Bar bender gang", "utilisation 90 % — the most highly worked element"),
    ("A5055", "5.1", "HOLD POINT: headhouse roof inspection", 1, "A5050",
     "QA/QC Engineer;Structural Consultant", "H-08"),
    ("A5060", "5.1", "Concrete headhouse roof 500 M35", 1, "A5055",
     "Concrete gang;Concrete pump", ""),
    ("A5065", "5.1", "Curing 14 days and strike — headhouse roof", 14, "A5060",
     "Unskilled gang;Carpenter gang", ""),

    ("A5070", "5.2", "Compacted fill and blinding to the stepped raft", 4, "A2055,A4085",
     "Unskilled gang;Plate compactor;Concrete gang", ""),
    ("A5075", "5.2", "Stepped raft 300 — reinforcement and concrete; movement joint at "
     "the headhouse", 5, "A5070", "Bar bender gang;Carpenter gang;Concrete gang",
     "the ONLY movement joint — outside the protective envelope"),
    ("A5080", "5.2", "Stairwell side walls and headwall — reinforcement and formwork", 6,
     "A5075", "Bar bender gang;Carpenter gang", ""),
    ("A5085", "5.2", "Concrete stairwell walls 250 M35", 1, "A5080",
     "Concrete gang;Concrete pump", ""),
    ("A5090", "5.2", "Entry flight 12R @ 166.667/300, waist 250; top landing and platform",
     6, "A5085FS+3", "Carpenter gang;Bar bender gang;Concrete gang", ""),
    ("A5095", "5.2", "Opening-corner U-bars at the head of the flight — bars crossed", 1,
     "A5090SS", "Bar bender gang", "SP 34 Cl. 5.5"),
    ("A5100", "5.2", "Entry door lintel 250 x 350 and headwall opening", 2, "A5090",
     "Bar bender gang;Concrete gang", ""),
    ("A5105", "5.2", "Stairwell raking roof 250 — falsework, reinforcement and concrete",
     6, "A5090,A5095", "Carpenter gang;Bar bender gang;Concrete gang", ""),
    ("A5110", "5.2", "Curing and strike — covered entry stairwell", 7, "A5105",
     "Unskilled gang;Carpenter gang", ""),
    ("A5115", "5.2", "Threshold channel 300 and grating at X 8950–9250", 2, "A5110",
     "Concrete gang;Unskilled gang", ""),

    ("A5120", "5.3", "ESC 1 collar 250 RC — reinforcement, formwork and concrete to +0.150",
     5, "A4090", "Bar bender gang;Carpenter gang;Concrete gang", ""),
    ("A5125", "5.3", "ESC 2 collar 250 RC — reinforcement, formwork and concrete to +0.700",
     5, "A5120", "Bar bender gang;Carpenter gang;Concrete gang", ""),
    ("A5130", "5.3", "Escape shaft covers, ladders and closure devices", 4, "A5125",
     "Welding set;Unskilled gang", ""),

    ("A5135", "5.4", "Install BLAST DOOR 1 in W6; align and test the seal", 4,
     "A1122,A4090", "Crane;Site Engineer (Civil);Welding set", ""),
    ("A5140", "5.4", "Install BLAST DOOR 2 in W7; align and test the seal", 4, "A5135",
     "Crane;Site Engineer (Civil);Welding set", ""),
    ("A5145", "5.4", "Inner security door 900 x 2100 in HW2", 2, "A5065",
     "Unskilled gang", ""),
    ("A5150", "5.4", "External entry door 1000 x 2100 in the stairwell headwall", 2,
     "A5110,A5100", "Unskilled gang", "opens outward; 50 weather bar"),

    # ================= 6  WATERPROOFING ====================================
    ("A6010", "6.1", "Prepare and repair the external wall faces; fillets at the mat junction",
     4, "A3150", "Waterproofing gang", ""),
    ("A6015", "6.1", "External tanking WP-01 — vertical to the wall faces, lapped to the "
     "horizontal", 8, "A6010,A1174", "Waterproofing gang", "265 m2"),
    ("A6020", "6.1", "Protection board or screed to the vertical tanking", 4, "A6015",
     "Waterproofing gang", ""),
    ("A6025", "6.1", "HOLD POINT: vertical tanking inspection before backfilling", 1,
     "A6020", "QA/QC Engineer", "H-09 — the last chance to see it"),

    ("A6030", "6.2", "Roof waterproofing WP-01 over the pressure slab; dress into openings",
     6, "A4095", "Waterproofing gang", "122 m2 net"),
    ("A6035", "6.2", "Protection screed 100 over the roof membrane — cover layer 1", 4,
     "A6030", "Concrete gang", "10.3 m3; also the first layer of the cover"),
    ("A6040", "6.2", "HOLD POINT: roof membrane integrity test before covering", 1,
     "A6035", "QA/QC Engineer", "H-10"),

    ("A6045", "6.3", "Headhouse and stairwell roof waterproofing WP-06 and protection", 4,
     "A5065,A5110", "Waterproofing gang", ""),
    ("A6055", "6.3", "MILESTONE: buried envelope watertight — tanking complete", 0, "A6025,A6040", "",
     "M-08"),

    # ================= 7  BACKFILL AND COVER ===============================
    ("A7010", "7.1", "Side backfill in selected fill — 250 layers compacted to 95 % MDD",
     10, "A6025,A4090,A2070FF", "Excavator;Plate compactor;Vibratory roller;Unskilled gang",
     "290 m3; never backfill against an unpropped wall before the roof is on"),
    ("A7015", "7.1", "In-situ density testing of the side backfill", 3, "A7010SS+3",
     "QA/QC Engineer", "IS 2720 (Part 28)"),

    ("A7020", "7.2", "Crush excavated basalt on site to 25–75 mm and stockpile", 8,
     "A2050", "Excavator;Rock breaker", "wins the 51 m3 rubble layer from the cut"),
    ("A7025", "7.2", "Compacted engineered fill 750 at 95 % MDD over the roof", 5,
     "A6040,A7010,A7015", "Excavator;Plate compactor;Unskilled gang", "77 m3 — radiation mass"),
    ("A7030", "7.2", "Crushed basalt rubble layer 500", 4, "A7025,A7020",
     "Excavator;Unskilled gang", "scatters burster energy"),

    ("A7035", "7.3", "Burster slab M30 200 thk — formwork and reinforcement T12 @ 150 B/W",
     5, "A7030", "Carpenter gang;Bar bender gang", "1.22 t of T12"),
    ("A7040", "7.3", "Concrete burster slab M30", 1, "A7035",
     "Concrete gang;Concrete pump", "20.6 m3"),
    ("A7045", "7.3", "Curing of the burster slab", 7, "A7040", "Unskilled gang", ""),

    ("A7050", "7.2", "Granular filter layer 150", 2, "A7045", "Unskilled gang",
     "stops fines clogging"),
    ("A7055", "7.2", "Topsoil 300 and turfing — the concealment layer", 4, "A7050",
     "Excavator;Unskilled gang", "uses the stripped topsoil from A2015"),
    ("A7060", "7.4", "Compaction test records and verification of the cover build-up", 3,
     "A7055", "QA/QC Engineer;Site Engineer (Civil)",
     "must reproduce the 2000 / 40.65 kPa build-up of master A.7.3"),
    ("A7065", "7.4", "MILESTONE: overburden complete — the structure is buried", 0,
     "A7060", "", "M-09"),

    # ================= 8  SENTRY POST ======================================
    ("A8010", "8.1", "Sentry post setting out — grids A–B and 1–2, level control", 2,
     "A1105,A1065,A2050", "Surveyor", "3650 x 4650 c/c; at least 10 m clear"),
    ("A8015", "8.1", "Excavation for footings F1, 4 No., to (-)2.100", 4, "A8010",
     "Excavator;Rock breaker", "37 m3"),
    ("A8020", "8.1", "HOLD POINT: founding stratum inspection — in-situ basalt at (-)2.000",
     1, "A8015", "QA/QC Engineer;Site Engineer (Civil)", "H-11"),
    ("A8025", "8.1", "Blinding PCC M15 100 under F1, 4 No.", 1, "A8020", "Concrete gang", ""),
    ("A8030", "8.1", "Footing F1 reinforcement T12 @ 150 both ways; column starters 8-T16",
     3, "A8025", "Bar bender gang", ""),
    ("A8035", "8.1", "HOLD POINT: footing reinforcement and starter inspection", 1,
     "A8030", "QA/QC Engineer", "H-12"),
    ("A8040", "8.1", "Concrete footings F1 M30", 1, "A8035", "Concrete gang", "5.4 m3"),
    ("A8045", "8.1", "Curing and backfill to the footings", 5, "A8040",
     "Unskilled gang;Plate compactor", ""),

    ("A8050", "8.2", "Columns C1 to plinth level — reinforcement, formwork, concrete", 5,
     "A8045", "Bar bender gang;Carpenter gang;Concrete gang", ""),
    ("A8055", "8.2", "Plinth beam PB 250 x 400 at +0.450 — reinforcement, formwork, concrete",
     4, "A8050", "Bar bender gang;Carpenter gang;Concrete gang",
     "PB carries the ground storey masonry"),
    ("A8060", "8.2", "Filling and compaction under the ground floor to +0.450", 3,
     "A8055", "Unskilled gang;Plate compactor", "7.5 m3"),
    ("A8065", "8.2", "Columns C1 — ground storey, to the first-floor beam soffit", 6,
     "A8055", "Bar bender gang;Carpenter gang;Concrete gang",
     "T10 confining hoops + cross-ties @ 85 over 500 from every joint face"),

    ("A8070", "8.3", "First floor beams B1/B2 and slab S1 150 — falsework and formwork", 5,
     "A8065", "Carpenter gang;Scaffolding", ""),
    ("A8075", "8.3", "First floor beam and slab reinforcement, incl. corner torsion steel",
     4, "A8070", "Bar bender gang",
     "T8 @ 200 torsion, four layers, 700 sq at all four corners — IS 456 D-1.8"),
    ("A8080", "8.3", "HOLD POINT: first floor reinforcement inspection — IS 13920 detailing",
     1, "A8075", "QA/QC Engineer;Structural Consultant", "H-13"),
    ("A8085", "8.3", "Concrete first floor beams and slab M30", 1, "A8080",
     "Concrete gang", ""),
    ("A8090", "8.3", "Curing 7 days; strike sides, props to remain", 7, "A8085",
     "Unskilled gang;Carpenter gang", "IS 456 Table 11"),

    ("A8095", "8.4", "Columns C1 — first storey, to the roof beam soffit", 6, "A8090",
     "Bar bender gang;Carpenter gang;Concrete gang", ""),
    ("A8100", "8.4", "Roof beams B1/B2 and slab S1 with the 300 projection — formwork "
     "and reinforcement", 6, "A8095", "Carpenter gang;Bar bender gang;Scaffolding", ""),
    ("A8105", "8.4", "HOLD POINT: sentry post roof reinforcement inspection", 1, "A8100",
     "QA/QC Engineer;Structural Consultant", "H-14"),
    ("A8110", "8.4", "Concrete sentry post roof M30", 1, "A8105", "Concrete gang", ""),
    ("A8115", "8.4", "Parapet 300 high over the roof projection", 3, "A8110FS+3",
     "Bar bender gang;Carpenter gang;Concrete gang", ""),
    ("A8120", "8.4", "Curing and strike — sentry post roof", 10, "A8110",
     "Unskilled gang;Carpenter gang", ""),
    ("A8125", "8.4", "MILESTONE: sentry post frame complete", 0, "A8120,A8115", "", "M-10"),

    ("A8130", "8.5", "Brick delivery, stacking, sampling and testing to IS 3495", 4,
     "A1176,A8085", "Storekeeper;QA/QC Engineer",
     "compressive strength, water absorption, efflorescence, warpage"),
    ("A8135", "8.5", "BRICK MASONRY WALLS — ground storey, 190 thk in CM 1:6", 5,
     "A8090,A8130", "Mason gang;Unskilled gang;Scaffolding",
     "DESIGN CHANGE SP-B1: brick masonry replaces the 200 RC ballistic infill"),
    ("A8145", "8.5", "HOLD POINT: masonry line, level, plumb and joint thickness — ground "
     "storey", 1, "A8135,A8140", "QA/QC Engineer", "H-15"),
    ("A8150", "8.5", "BRICK MASONRY WALLS — first storey, 190 thk in CM 1:6", 4,
     "A8120,A8145", "Mason gang;Unskilled gang;Scaffolding", ""),
    ("A8160", "8.5", "HOLD POINT: masonry inspection — first storey", 1, "A8150,A8155",
     "QA/QC Engineer", "H-16"),
    ("A8165", "8.5", "MILESTONE: sentry post brick masonry complete", 0, "A8160", "",
     "M-11"),

    ("A8140", "8.6", "RC lintels over the D1 and W1 openings — ground storey", 2, "A8135",
     "Bar bender gang;Carpenter gang;Concrete gang",
     "NEW work created by SP-B1; lintel design does not yet exist"),
    ("A8155", "8.6", "RC lintels over the vision panel and door openings — first storey",
     2, "A8150", "Bar bender gang;Carpenter gang;Concrete gang", ""),

    ("A8170", "8.7", "External spiral stair 1000 R, 250 dia central pole — fabrication "
     "and erection", 6, "A8120", "Welding set;Crane;Unskilled gang", ""),

    ("A8175", "8.9", "Sentry post electrical — conduits and boxes chased into the masonry",
     4, "A8160", "Electrician gang", "chases cut, not hammered — masonry rule"),
    ("A8180", "8.8", "Sentry post internal plaster 12 mm, sand faced, CM 1:4", 6,
     "A8175", "Plasterer gang;Unskilled gang", "IS 1661"),
    ("A8185", "8.8", "Sentry post external plaster 15 mm, two coat, with scaffolding", 6,
     "A8180", "Plasterer gang;Scaffolding", ""),
    ("A8190", "8.8", "Sentry post flooring — ground and first floor", 4, "A8180,A8060",
     "Mason gang", "33 m2; specification not in the project"),
    ("A8195", "8.8", "Door D1 (2 No.), window W1 and armoured vision panel installation",
     6, "A8185,A1165", "Unskilled gang;Welding set", ""),
    ("A8200", "8.9", "Sentry post electrical — wiring, distribution board, fittings, earthing",
     6, "A8190,A8195", "Electrician gang", ""),
    ("A8205", "8.8", "Sentry post painting — internal and external", 6, "A8200",
     "Painter gang;Scaffolding", "IS 2395 (Part 1)"),
    ("A8210", "8.8", "Sentry post testing and snagging", 3, "A8205",
     "QA/QC Engineer;Electrician gang", ""),
    ("A8215", "8.8", "MILESTONE: sentry post complete", 0, "A8210,A8170", "", "M-12"),

    # ================= 9  MECHANICAL / CBRN ================================
    ("A9010", "9.1", "Builder's work — sleeves, ducts and penetrations coordinated with "
     "the RC", 6, "A3090SS+2", "HVAC fitter;Site Engineer (Services)", ""),
    ("A9015", "9.2", "Install blast valve sleeves in the walls and roof", 4,
     "A1145,A4050", "HVAC fitter;Welding set", ""),
    ("A9020", "9.2", "Fresh-air shaft SH-1 600 x 600 and gooseneck head at +1.500", 5,
     "A4090", "HVAC fitter;Concrete gang", "12.3 m from the intake to the entry"),
    ("A9025", "9.2", "Generator air shaft SH-2 600 x 600", 4, "A4090",
     "HVAC fitter;Concrete gang", ""),
    ("A9030", "9.2", "Ductwork installation, bays 1–6 — every run inspectable along its "
     "length", 10, "A4095", "HVAC fitter", "no suspended ceiling anywhere — FN1 C-01"),
    ("A9035", "9.2", "Install blast valves BV-1 to BV-5", 5, "A9015,A9030,A9020",
     "HVAC fitter", ""),
    ("A9040", "9.3", "Install CBRN filter trains AHU-1 and AHU-2 in bay 5", 8,
     "A1135,A9030", "HVAC fitter;Crane", "true N+1 — either train carries the whole duty"),
    ("A9045", "9.3", "Install CO2 scrubber, oxygen store and dehumidifier", 5, "A9040",
     "HVAC fitter", "soda lime, not oxygen, limits closed mode"),
    ("A9050", "9.3", "Install generator GEN-1 15 kVA in bay 8 on a bunded plinth", 5,
     "A1160,A9025", "HVAC fitter;Crane;Electrician gang", ""),
    ("A9055", "9.3", "HVAC terminal devices, dampers and controls", 6, "A9045",
     "HVAC fitter", ""),
    ("A9060", "9.3", "MILESTONE: CBRN plant installed", 0, "A9055,A9050,A9035", "",
     "M-13"),

    # ================= 10  DRAINAGE ========================================
    ("A10010", "10.1", "Internal gullies GY-01 to GY-09; floor falls set out", 4, "A4095",
     "Plumber gang;Surveyor", "spine falls 1:400 east to the sump"),
    ("A10015", "10.1", "Waste and effluent drains PD-01 and PD-03 — laid and tested", 5,
     "A10010", "Plumber gang", ""),
    ("A10020", "10.1", "Clean sump SU-01 — fit out, pumps PU-01/PU-02 and hand pump PU-03",
     5, "A1170,A10015", "Plumber gang;Electrician gang", "duty, standby AND manual"),
    ("A10025", "10.1", "Rising main PD-05 — isolation valve, gas-tight NRV, blast check "
     "valve and deep-seal trap in series", 4, "A10020", "Plumber gang",
     "four devices in series; all inside the envelope"),
    ("A10030", "10.2", "Decontamination effluent segregation — CP-01 and tank TK-01 in bay 8",
     4, "A10015", "Plumber gang", "NEVER connected to the clean sump"),
    ("A10035", "10.3", "Stairwell sump SU-02 and pumps PU-04/PU-05", 4, "A5110,A1170",
     "Plumber gang;Electrician gang", ""),
    ("A10040", "10.3", "Headhouse gully GY-11 and trapped connection", 2, "A5065",
     "Plumber gang", "trapped gully to an external soakaway"),
    ("A10045", "10.3", "Threshold channel CH-10, catchpit CP-10 and connections", 3,
     "A5115", "Plumber gang", ""),
    ("A10050", "10.3", "Septic tank ST-01 — excavation, construction and testing", 8,
     "A1085,A7010", "Mason gang;Concrete gang", "IS 2470 (Part 1) Table 1"),
    ("A10055", "10.3", "Soak pits SK-01 and SK-02 — constructed after the percolation test",
     6, "A10050", "Mason gang;Unskilled gang",
     "SK-01 is 2.3 % short of its own requirement — conflict C19, UNRESOLVED"),
    ("A10060", "10.3", "External drainage connections and chambers", 6, "A10055",
     "Plumber gang;Mason gang", "several lengths NOT DETERMINABLE — no site plan"),
    ("A10065", "10.3", "MILESTONE: drainage installed", 0,
     "A10060,A10045,A10035,A10025,A10030,A10040", "", "M-14"),

    # ================= 11  ELECTRICAL AND EMP ==============================
    ("A11015", "11.1", "Earth pits, earth electrodes and the buried earth ring", 5,
     "A3075", "Electrician gang;Unskilled gang", "IS 3043; 5 ohm target"),
    ("A11020", "11.1", "EMP straps and bonding at every construction joint", 8,
     "A3125SS", "Welding set;Electrician gang",
     "welded Cu/galv strap at every joint — a joint is an EMP discontinuity"),
    ("A11025", "11.2", "Main cable route, service entry plate and EMP penetration protection",
     6, "A4095", "Electrician gang;Welding set",
     "power PCI, waveguide below cutoff, fibre — MIL-STD-188-125-1"),
    ("A11030", "11.2", "EMP Zone 2 shielded enclosure erection in bay 3 — SPECIALIST", 12,
     "A1155,A4095", "Specialist subcontractor;Crane",
     "the rebar cage gives 0 dB at 1 GHz; the welded steel room is the answer"),
    ("A11035", "11.3", "Distribution board, sub-mains and final circuit wiring", 12,
     "A11025", "Electrician gang", "IS 732"),
    ("A11040", "11.3", "Lighting, small power and emergency lighting installation", 10,
     "A11035", "Electrician gang", ""),
    ("A11045", "11.3", "Generator connection, changeover panel and protection", 5,
     "A9050,A11035", "Electrician gang", ""),
    ("A11050", "11.1", "Earthing conductors, bonding and connection to the electrode system",
     6, "A11015,A11035", "Electrician gang", ""),
    ("A11055", "11.3", "Power to pumps, fans, filter trains and controls", 6,
     "A11035,A9055", "Electrician gang", ""),
    ("A11060", "11.3", "MILESTONE: electrical installation complete", 0,
     "A11040,A11045,A11050,A11055,A11030", "", "M-15"),

    # ================= 12  INTERNAL FINISHES ===============================
    ("A12010", "12.1", "Substrate preparation — hack, make good, prepare soffits and walls",
     6, "A4095,A4100", "Unskilled gang;Plasterer gang", ""),
    ("A12015", "12.1", "Internal wet-area tanking WP-04 — bays 2, 5 and 6", 5, "A12010",
     "Waterproofing gang", "turned up 150 and dressed to every gully and sleeve"),
    ("A12020", "12.2", "Floor screeds laid to falls, bays 1–8", 8, "A10015,A12015",
     "Mason gang;Concrete gang", ""),
    ("A12025", "12.2", "Floor finish F-01 — sealed power-floated, bays 1, 3 and 4", 6,
     "A12020", "Mason gang", "decontaminable, joint-free within a room"),
    ("A12030", "12.2", "Floor finish F-02 — seamless coved wet-area, bays 2, 5 and 6", 5,
     "A12020", "Mason gang", "NO tiles, NO grout — grout lines fail decontamination"),
    ("A12035", "12.2", "Floor finish F-03 — non-slip, stair shaft, treads and landings", 4,
     "A12020", "Mason gang", ""),
    ("A12040", "12.2", "Floor finish F-04 — oil-resistant with a bunded plinth, bay 8", 3,
     "A12020", "Mason gang", ""),
    ("A12045", "12.2", "Floor finish F-05 headhouse and F-06 covered entry stairwell", 4,
     "A5065,A5110", "Mason gang", ""),
    ("A12050", "12.2", "Coved skirtings S-01 / S-02, integral with the floor", 5,
     "A12025,A12030", "Mason gang", "no separate section, no sealant joint"),
    ("A12055", "12.3", "Wall finishes W-01 / W-02 / W-03 — sealed washable coatings", 10,
     "A12050,A11040", "Painter gang", "applied direct to concrete; no cavity, no lining"),
    ("A12060", "12.3", "Soffit finishes C-01 / C-02 — exposed RC, sealed", 6, "A12055",
     "Painter gang", "no suspended ceiling and no boxing-in anywhere"),
    ("A12065", "12.4", "Internal doors D-04 in the W8 partitions; gas-tight door D-05 in W5",
     4, "A12055", "Unskilled gang",
     "D-05 is UNRESOLVED — no door is scheduled in W5 anywhere in the project"),
    ("A12070", "12.4", "MILESTONE: internal finishes complete", 0,
     "A12060,A12065,A12045,A12035,A12040", "", "M-16"),

    # ================= 13  EXTERNAL WORKS ==================================
    ("A13010", "13.1", "Berm forming and grading 1.5:1 to +0.900 against the headhouse "
     "and stairwell", 8, "A7065,A5110", "Excavator;Dozer/grader;Vibratory roller",
     "volume NOT DETERMINABLE — no site plan exists"),
    ("A13015", "13.1", "Site regrading — crown and falls 1:50 away from the structure", 5,
     "A13010", "Dozer/grader;Vibratory roller", ""),
    ("A13020", "13.1", "Surface water drainage, cut-off drains and outfalls", 5, "A13015",
     "Plumber gang;Unskilled gang", ""),
    ("A13025", "13.2", "Access route, hardstanding and turning area", 8, "A13015",
     "Dozer/grader;Vibratory roller;Unskilled gang", "extent not defined in the project"),
    ("A13030", "13.2", "Sentry post surround, apron and drainage", 4, "A8205,A13025",
     "Mason gang;Unskilled gang", ""),
    ("A13035", "13.3", "Turfing and planting over the cover — the concealment layer", 6,
     "A13015", "Unskilled gang", "the only concealment element the project confirms"),
    ("A13040", "13.3", "Camouflage and concealment — spoil dressing, track discipline, "
     "screening", 6, "A13035", "Unskilled gang",
     "no concealment specification exists — scope to be confirmed"),
    ("A13045", "13.4", "Removal of temporary works, site restoration and clearing", 6,
     "A13040,A13030,A13020", "Excavator;Unskilled gang", ""),
    ("A13050", "13.4", "MILESTONE: external works and concealment complete", 0, "A13045",
     "", "M-17"),

    # ================= 14  TESTING AND HANDOVER ============================
    ("A14010", "14.1", "Concrete cube results at 28 days, all pours — review and acceptance",
     5, "A7040", "QA/QC Engineer", "IS 516"),
    ("A14015", "14.1", "Non-destructive testing — ultrasonic pulse velocity and rebound "
     "hammer", 4, "A14010", "QA/QC Engineer", "IS 13311 (Parts 1 and 2)"),
    ("A14020", "14.1", "Dimensional and as-built survey of the completed structure", 5,
     "A7065", "Surveyor", ""),
    ("A14025", "14.1", "Watertightness inspection of the completed envelope", 5,
     "A12010,A7065,A6045", "QA/QC Engineer;Waterproofing gang", ""),
    ("A14030", "14.2", "Drainage testing — pipes, gullies, chambers, pump duty and standby",
     5, "A10065", "Plumber gang;QA/QC Engineer", ""),
    ("A14035", "14.2", "Electrical testing — insulation, continuity, polarity, protection",
     5, "A11060", "Electrician gang;QA/QC Engineer", "IS 732"),
    ("A14040", "14.2", "Earth resistance measurement — 5 ohm target", 2, "A11050",
     "Electrician gang;QA/QC Engineer", "IEEE 142 / IS 3043"),
    ("A14045", "14.3", "EMP shielding effectiveness survey — 80 dB, 10 kHz to 1 GHz", 8,
     "A11030,A11060,A12060,A11020", "Specialist subcontractor;QA/QC Engineer",
     "IEEE Std 299; MIL-STD-188-125-1"),
    ("A14050", "14.3", "Blast doors 1 and 2 — functional and seal testing", 4,
     "A5140,A12060", "Specialist subcontractor;Site Engineer (Civil)", ""),
    ("A14055", "14.3", "Escape shaft access and closure functional test", 2, "A5130",
     "Site Engineer (Civil);Safety Officer", ""),
    ("A14060", "14.4", "HVAC and CBRN filter train commissioning — airflow and overpressure",
     8, "A9060,A11055", "Specialist subcontractor;HVAC fitter", ""),
    ("A14065", "14.3", "Gas-tightness and overpressure test of the envelope, bays 1–6", 5,
     "A14060,A14050", "Specialist subcontractor;QA/QC Engineer",
     "67.8 m2 floor, 217.0 m3 volume"),
    ("A14070", "14.4", "Generator load test and changeover proving", 3, "A11045",
     "Electrician gang;Specialist subcontractor", ""),
    ("A14075", "14.4", "Integrated systems commissioning — protective mode operation", 6,
     "A14065,A14060,A14070,A14030,A14045", "Site Engineer (Services);Specialist subcontractor",
     ""),
    ("A14080", "14.5", "Snagging inspection and defects list", 5,
     "A14075,A13050,A8215,A14025,A14015,A14035,A14040,A14055,A14020,A4115,A5145,A5150",
     "QA/QC Engineer;Project Manager", ""),
    ("A14085", "14.5", "Rectification of defects", 10, "A14080",
     "Unskilled gang;Mason gang;Painter gang", ""),
    ("A14090", "14.5", "As-built drawings, O&M manuals and test certificates", 12,
     "A14075", "Project Manager;Planning Engineer", ""),
    ("A14095", "14.5", "Operator training — CBRN plant, pumps, generator, doors, escape shafts",
     5, "A14090", "Specialist subcontractor;Site Engineer (Services)", ""),
    ("A14098", "14.5", "Programme contingency — festival holidays and weather allowance",
     10, "A14085,A14095", "",
     "the calendar carries no festival holidays; this activity absorbs them"),
    ("A14100", "14.5", "Final inspection and handover documentation", 4, "A14098",
     "Project Manager;QA/QC Engineer", ""),
    ("A14105", "14.5", "MILESTONE: PRACTICAL COMPLETION AND HANDOVER", 0, "A14100", "",
     "M-18"),
]

# ---------------------------------------------------------------------------
# RESOURCES
# ---------------------------------------------------------------------------
# (name, group, unit/composition, peak No., note)
RESOURCES = [
    # --- staff -------------------------------------------------------------
    ("Project Manager", "Staff", "1 No.", 1,
     "Overall responsibility; MES/Service liaison; procurement of protective items"),
    ("Planning Engineer", "Staff", "1 No.", 1,
     "Programme, progress measurement, look-ahead, as-built records"),
    ("Site Engineer (Civil)", "Staff", "2 No.", 2,
     "Excavation, RC works, backfill, sentry post"),
    ("Site Engineer (Services)", "Staff", "1 No.", 1,
     "HVAC, CBRN, drainage, electrical coordination"),
    ("Surveyor", "Staff", "1 No. + chainman", 1,
     "Setting out to the master A.4.1 grid; level control; as-built survey"),
    ("QA/QC Engineer", "Staff", "1 No.", 1,
     "Inspection and test plan, hold points, records"),
    ("Safety Officer", "Staff", "1 No.", 1,
     "Deep excavation, confined space, work at height, lifting"),
    ("Storekeeper", "Staff", "1 No.", 1, "Material receipt, stacking to IS 4082, issue"),
    ("Structural Consultant", "Staff", "visiting", 1,
     "Attends the reinforcement hold points — carried from the R0 schedule"),
    # --- labour gangs ------------------------------------------------------
    ("Bar bender gang", "Labour", "1 gang = 1 fitter + 3 helpers", 4,
     "Peak on the pressure slab: 20.5 t of T25 at 150 both faces both ways"),
    ("Carpenter gang", "Labour", "1 gang = 1 carpenter + 2 helpers", 4,
     "Peak on the pressure slab falsework, 104 m2 of deck at 3.200 m"),
    ("Concrete gang", "Labour", "1 gang = 1 mason + 6 helpers", 2,
     "Continuous pours: mat 85 m3, pressure slab 112 m3"),
    ("Mason gang", "Labour", "1 gang = 1 mason + 2 helpers", 3,
     "SENTRY POST BRICK MASONRY; screeds; floor finishes; chambers"),
    ("Plasterer gang", "Labour", "1 gang = 1 plasterer + 1 helper", 2,
     "Sentry post internal and external plaster"),
    ("Painter gang", "Labour", "1 gang = 1 painter + 1 helper", 2,
     "Sealed washable coatings internally; sentry post painting"),
    ("Waterproofing gang", "Labour", "specialist, 1 gang = 4 No.", 4,
     "Tanking is a specialist trade — 532 m2 of continuous membrane"),
    ("Electrician gang", "Labour", "1 gang = 1 electrician + 1 helper", 3,
     "Conduits, cabling, earthing, EMP bonding"),
    ("Plumber gang", "Labour", "1 gang = 1 plumber + 1 helper", 2,
     "Drainage, sumps, rising mains"),
    ("HVAC fitter", "Labour", "1 gang = 1 fitter + 1 helper", 2,
     "Ductwork, blast valves, CBRN plant"),
    ("Unskilled gang", "Labour", "general labour", 20,
     "Curing, handling, backfill, cleaning"),
    ("Specialist subcontractor", "Labour", "as required", 1,
     "EMP enclosure, blast doors, CBRN commissioning, gas-tightness test"),
    # --- plant -------------------------------------------------------------
    ("Excavator", "Plant", "0.9 m3 tracked", 2, "Bulk excavation, backfill, cover"),
    ("Rock breaker", "Plant", "hydraulic, excavator mounted", 2,
     "994 m3 of basalt; NO BLASTING permitted near the sentry post"),
    ("Tipper", "Plant", "10 t", 4, "Spoil haulage; peak during rock excavation"),
    ("Dozer/grader", "Plant", "1 No.", 1, "Berm, regrading, access"),
    ("Vibratory roller", "Plant", "1 No.", 1, "Backfill and cover compaction to 95 % MDD"),
    ("Plate compactor", "Plant", "2 No.", 2, "Confined backfill in 250 layers"),
    ("Concrete pump", "Plant", "boom pump", 1,
     "112 m3 continuous pour to the pressure slab"),
    ("Transit mixer", "Plant", "6 m3", 4, "Peak on the pressure slab pour"),
    ("Crane", "Plant", "20 t mobile", 1,
     "Blast doors, filter trains, EMP enclosure, spiral stair"),
    ("Dewatering pumps", "Plant", "duty + standby", 2,
     "Continuous through the substructure; GWT (-)2.000 is ASSUMED"),
    ("Scaffolding", "Plant", "tube and fitting", 1,
     "Slab falsework, masonry, plaster; IS 3696 / IS 4014"),
    ("Welding set", "Plant", "2 No.", 2,
     "EMP straps and blast door frames welded to the reinforcement cage"),
]

# ---------------------------------------------------------------------------
# MILESTONES — external register (id used in the activity notes)
# ---------------------------------------------------------------------------
MILESTONES = [
    ("M-01", "A1025", "Site possession and commencement"),
    ("M-02", "A1065", "Mobilisation complete"),
    ("M-03", "A1175", "All long-lead protective items ordered"),
    ("M-04", "A2090", "Excavation complete, formation approved"),
    ("M-05", "A3085", "Mat foundation cast"),
    ("M-06", "A3160", "Perimeter and protective walls complete"),
    ("M-07", "A4085", "Pressure slab cast — key structural milestone"),
    ("M-08", "A6055", "Buried envelope watertight — tanking complete"),
    ("M-09", "A7065", "Overburden complete — structure buried"),
    ("M-10", "A8125", "Sentry post frame complete"),
    ("M-11", "A8165", "Sentry post brick masonry complete"),
    ("M-12", "A8215", "Sentry post complete"),
    ("M-13", "A9060", "CBRN plant installed"),
    ("M-14", "A10065", "Drainage installed"),
    ("M-15", "A11060", "Electrical installation complete"),
    ("M-16", "A12070", "Internal finishes complete"),
    ("M-17", "A13050", "External works and concealment complete"),
    ("M-18", "A14105", "PRACTICAL COMPLETION AND HANDOVER"),
]
