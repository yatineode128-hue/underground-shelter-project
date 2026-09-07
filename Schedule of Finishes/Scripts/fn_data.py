"""
fn_data.py  --  the finish codes, the room finish schedule and the stair
finishes.  Schedules and drawings are both generated from this file.

*** READ THIS BEFORE READING THE SCHEDULE ***

NO FINISH SPECIFICATION EXISTS ANYWHERE IN THIS PROJECT.  The master, the ten
Rev F architectural drawings, sheet S-06 and the Structural CAD package between
them fix concrete grade, cover, waterproofing, crack control and bar spacing -
and nothing else about what a surface is finished with.

This package therefore does NOT report finishes as project facts.  Every code
below is a PERFORMANCE REQUIREMENT derived from something the project does
confirm - the exposure class, the decontamination duty, the gas-tight envelope,
the EMP requirement, the wet areas, the frozen stair geometry - and the PRODUCT
that satisfies it is left open.

    [C]  the requirement is confirmed in the project, and the source is named
    [R]  derived here from confirmed values
    [A]  an engineering selection made by this package - CONFIRM BEFORE ORDER
    [N]  not available anywhere in the project - DATA REQUIRED

Anywhere a thickness, a product, a colour or a manufacturer would normally
appear, this schedule says PROVISIONAL - VERIFY or ENGINEER TO CONFIRM.  It
does not invent one.

SENTRY POST IS EXCLUDED.  No sentry post room appears in this file.
MAIN STAIRCASE GEOMETRY IS FROZEN - 24R @ 170.8333 / 280, 3 flights x 8, total
rise 4100.  This package annotates and finishes it.  It does not alter it.
"""

# ============================================================ finish codes
# code, description, performance requirement, where it comes from, class
FLOORS = [
    ("F-01", "SEALED POWER-FLOATED SCREED",
     "Decontaminable, non-dusting, chemical- and washdown-resistant, laid to "
     "falls. Joint-free within a room; coved to the skirting.",
     "Gas-tight CBRN envelope, bays 1-6 [C master A.2]. Falls and screed "
     "thickness from DRAINAGE calc D.15 / D.5", "[A]"),
    ("F-02", "SEAMLESS COVED HEAVY-DUTY WET-AREA FINISH",
     "As F-01 plus fully impervious, coved 150 up every wall in one piece, "
     "resistant to decontaminant solution. NO joints, NO tiles, NO grout.",
     "Wet areas: lavatory/medical, CBRN plant, decon airlock. Grout lines are "
     "a decontamination failure", "[A]"),
    ("F-03", "NON-SLIP DECONTAMINABLE FLOOR AND TREAD FINISH",
     "Wet-slip resistant when contaminated, abrasion resistant, no loose "
     "aggregate. Applied to treads, landings and the shaft floor.",
     "Master A.5 designates the stair shaft faces a WET / DIRTY ZONE (30 mm "
     "cover) [C]", "[A]"),
    ("F-04", "ABRASION- AND OIL-RESISTANT FLOOR",
     "Fuel- and oil-resistant, abrasion resistant, laid to falls to GY-09, "
     "with a bunded plinth under the generator.",
     "Bay 8 generator, the grey zone [C master A.3]", "[A]"),
    ("F-05", "POWER-FLOATED NON-SLIP SLAB FINISH",
     "External-grade, non-slip when wet, laid to the confirmed 1:80 fall to "
     "the floor gully. Hose-down duty.",
     "Headhouse floor is the top of the 900 pressure slab at (-)2.000 with a "
     "hose-down point and a 1:80 gully [C Rev F ground plan]", "[A]"),
    ("F-06", "IN-SITU CONCRETE, NON-SLIP, WITH A CAST NOSING",
     "External-grade non-slip; nosing integral, not applied.",
     "Covered entry stairwell, outside the protective boundary and DECLARED "
     "EXPENDABLE [C master A.2]", "[A]"),
]

SKIRTINGS = [
    ("S-01", "COVED SKIRTING, 150 HIGH, INTEGRAL WITH THE FLOOR",
     "Formed in one piece with the floor finish. No separate section, no "
     "sealant joint at the floor.",
     "Decontamination: a butt skirting has a joint at the very place "
     "contaminant collects", "[A]"),
    ("S-02", "HARD SKIRTING, 100 HIGH",
     "Impact resistant, sealed to the wall and floor.",
     "Grey zone and stair shaft, where the decontamination duty does not "
     "apply but impact does", "[A]"),
    ("S-03", "NO SKIRTING",
     "Wall finish returned to the floor and sealed.",
     "External and semi-external areas", "[A]"),
]

WALLS = [
    ("W-01", "FAIR-FACE RC, SEALED WASHABLE COATING",
     "Non-dusting, washable, resistant to decontaminant solution, applied "
     "direct to the concrete. NO cavity, NO dry lining, NO battens.",
     "Gas-tight envelope. A lined cavity is a contamination trap that cannot "
     "be decontaminated or inspected", "[A]"),
    ("W-02", "AS W-01 PLUS IMPERVIOUS FINISH TO FULL HEIGHT",
     "Fully impervious floor-to-soffit, continuous with the F-02 cove.",
     "Wet areas: lavatory/medical, CBRN plant, decon airlock", "[A]"),
    ("W-03", "FAIR-FACE RC, SEALED",
     "Non-dusting, washable. Impact-resistant at handling routes.",
     "Grey zone, stair shaft", "[A]"),
    ("W-04", "EMP ZONE 2 SHIELDED ENCLOSURE LINING",
     "*** SPECIALIST. Welded steel room, shielding effectiveness verified to "
     "IEEE Std 299. Its finish is subordinate to its shielding. ***",
     "Master A.3 places an EMP Zone 2 enclosure in bay 3; K.3 records that the "
     "rebar cage gives 0 dB at 1 GHz and 'a Zone 2 welded steel room is the "
     "answer' [C]", "[C] requirement / [N] specification"),
    ("W-05", "FAIR-FACE RC, SEALED, EXTERNAL GRADE",
     "UV and weather resistant on exposed faces; washable internally.",
     "Headhouse and covered stairwell", "[A]"),
]

CEILINGS = [
    ("C-01", "EXPOSED RC SOFFIT, SEALED DECONTAMINABLE COATING",
     "Applied direct to the soffit. *** NO SUSPENDED CEILING AND NO BOXING-IN "
     "ANYWHERE IN THE GAS-TIGHT ENVELOPE. ***",
     "Three independent reasons, all confirmed: HVAC requires every duct "
     "inspectable along its length (HV-F2); DRAINAGE requires the same of "
     "every pipe; and a ceiling void is a contamination trap that cannot be "
     "decontaminated", "[A]"),
    ("C-02", "EXPOSED RC SOFFIT, SEALED",
     "As C-01 without the decontamination duty.",
     "Grey zone, stair shaft", "[A]"),
    ("C-03", "EXPOSED RC RAKING SOFFIT, SEALED, EXTERNAL GRADE",
     "Follows the flight at 2200 clear.",
     "Covered entry stairwell [C master A.4.7]", "[A]"),
]

DOORS = [
    ("D-01", "BLAST DOOR - PROPRIETARY",
     "1200 x 2100, >= 7 bar, rebound-rated, gas-tight. FINISH IS THE VENDOR'S "
     "AND IS SUBORDINATE TO THE RATING - do not overcoat a tested assembly.",
     "Blast doors 1 and 2 in W6 and W7, THE PROTECTIVE BOUNDARY [C master "
     "A.2 / B.2]", "[C] / [N] finish"),
    ("D-02", "INNER SECURITY DOOR - STEEL, NOT BLAST RATED",
     "900 x 2100. Frame cast in and WELDED TO THE CAGE for EMP continuity, "
     "even though the leaf is not blast rated.",
     "In HW2 at X 14450-15350 [C master A.4.6 / B.7.2]", "[C] / [A] finish"),
    ("D-03", "EXTERNAL ENTRY DOOR - STEEL",
     "1000 x 2100, opens outward, threshold flush with a 50 weather bar. "
     "External-grade coating.",
     "In the stairwell headwall at grade [C Rev F section C-C]",
     "[C] / [A] finish"),
    ("D-04", "INTERNAL DOOR IN A 110 PARTITION",
     "900 clear in the confirmed door gap. Light, washable, no cavity.",
     "Four W8 partitions, door gap at Y 2500-3400 [C master A.3]", "[A]"),
    ("D-05", "GAS-TIGHT DOOR IN W5",
     "Clean-side exit from the decon airlock. Gas-tight, not blast rated.",
     "*** W5 IS CONFIRMED AS 'FIRE + GAS-TIGHT' BUT NO DOOR IS SCHEDULED IN "
     "IT ANYWHERE IN THE PROJECT. The airlock must have a clean-side exit. "
     "ENGINEER TO CONFIRM SIZE AND POSITION ***", "[U]"),
]

WATERPROOFING = [
    ("WP-01", "TANKING MEMBRANE - EXTERNAL, CONTINUOUS",
     "On the blinding, turned up the external face, lapped to the roof "
     "membrane. A CONTINUOUS TANK.", "R-805 [C]"),
    ("WP-02", "100 PROTECTION SCREED OVER THE ROOF MEMBRANE",
     "Also the first layer of the engineered cover.", "R-805 / A.7.3 [C]"),
    ("WP-03", "INTEGRAL CRYSTALLINE WATERPROOFING ADMIXTURE",
     "In the concrete. The membrane is not the only line of defence.",
     "master A.5 / R-805 [C]"),
    ("WP-04", "INTERNAL WET-AREA TANKING UNDER THE FINISH",
     "Beneath F-02 and behind W-02 in every wet area, turned up 150 and "
     "dressed to every gully and pipe sleeve.",
     "Wet areas identified from master A.3 and the DRAINAGE package", "[A]"),
    ("WP-05", "TWO WATERSTOPS AT EVERY CONSTRUCTION JOINT",
     "R-804.", "R-805 [C]"),
]

# =========================================================== room schedule
# no, name, level, area m2, F, S, W, C, D, WP, wet, special, remarks
ROOMS = [
    ("U-01", "EMERGENCY STORES / ESC 1", -6.100, 14.50, "F-01", "S-01",
     "W-01", "C-01", "D-04", "WP-01/03", False,
     "1000 L potable tank; ESC 1 collar 1400 dia clear",
     "Falls 1:100 to the spine. Keep 750 clear of the ESC opening edge"),
    ("U-02", "LAVATORY + MEDICAL", -6.100, 9.00, "F-02", "S-01", "W-02",
     "C-01", "D-04", "WP-01/03/04", True,
     "Lavatory 1800 x 2000 + medical 1800 x 3000 [C master A.3]",
     "WET AREA. Falls 1:80 to GY-02. Sealed-cassette toilets - nothing is "
     "discharged in protective mode"),
    ("U-03", "OPS ROOM & HAZARD PLOTTING", -6.100, 17.50, "F-01", "S-01",
     "W-01 + W-04", "C-01", "D-04", "WP-01/03", False,
     "*** EMP ZONE 2 ENCLOSURE - specialist, see W-04 ***",
     "Falls 1:100. The Zone 2 room's finish is subordinate to its shielding"),
    ("U-04", "BERTHING - 9 BERTHS", -6.100, 9.00, "F-01", "S-01", "W-01",
     "C-01", "D-04", "WP-01/03", False,
     "3 x 3-tier bunks. Highest occupant density in the shelter",
     "Falls 1:100. Bunk fixings CAST IN - see note on fixings"),
    ("U-05", "CBRN PLANT + SUMP", -6.100, 7.80, "F-02", "S-01", "W-02",
     "C-01", "D-05", "WP-01/03/04", True,
     "Two NBC filter trains, CO2/O2 plant, dehumidifier, clean sump",
     "WET AREA. Falls 1:80 direct to the sump. 110 mm clear at the sides of "
     "each train - do not thicken the wall finish here"),
    ("U-06", "DECON AIRLOCK - 3 STAGE", -6.100, 10.00, "F-02", "S-01",
     "W-02", "C-01", "D-01/D-05", "WP-01/03/04", True,
     "Stages 2000x2000, 2000x1500, 2000x1500 [C master A.3]",
     "WET AREA, AND THE DIRTIEST SURFACE IN THE SHELTER. Falls 1:80 to the "
     "SEGREGATED gullies. 50 upstand at W5 and at blast door 1"),
    ("U-07", "STAIR SHAFT", -6.100, 14.00, "F-03", "S-02", "W-03", "C-02",
     "D-01", "WP-01/03", False,
     "MAIN STAIRCASE - FROZEN GEOMETRY. See the stair finish schedule",
     "Master A.5 designates these faces a WET / DIRTY ZONE (30 cover). "
     "OUTSIDE the gas-tight envelope"),
    ("U-08", "GENERATOR / SERVICES / ESC 2", -6.100, 15.00, "F-04", "S-02",
     "W-03", "C-02", "D-01", "WP-01/03", False,
     "15 kVA generator; 1000 L decon effluent tank; ESC 2",
     "GREY ZONE. Bunded plinth under the generator. Falls to GY-09, which "
     "has NO DESTINATION DEFINED - DRAINAGE DR-F5"),
    ("G-01", "COVERED STAIRWELL - TOP LANDING", 0.000, 2.25, "F-06", "S-03",
     "W-05", "C-03", "D-03", "WP-06", False,
     "1500 x 1500 at grade. Entry door 1000 x 2100",
     "EXTERNAL. 300 channel + grating across the full 1500 width at the "
     "threshold; ground falls away 1:50 for 2000"),
    ("G-02", "COVERED STAIRWELL - FLIGHT", None, 4.95, "F-06", "S-03",
     "W-05", "C-03", "-", "WP-06", False,
     "12R @ 166.6667 / 300, 1500 wide, waist 250 [C master A.4.7]",
     "EXTERNAL, semi-exposed. Non-slip essential - this is the only entry "
     "route. Soffit follows the flight at 2200 clear"),
    ("G-03", "COVERED STAIRWELL - PLATFORM", -2.000, 2.25, "F-06", "S-03",
     "W-05", "C-03", "D-02", "WP-06", True,
     "1500 x 1500 at (-)2.000. Gully GY-10 to the 1.0 m3 sump",
     "*** C16 - the roof over this platform is UNRESOLVED, 250 or 500. Shown "
     "at 250. The finish does not depend on the ruling; the drip at the "
     "junction does ***"),
    ("G-04", "HEADHOUSE", -2.000, 11.15, "F-05", "S-02", "W-05", "C-02",
     "D-02", "WP-06", True,
     "11.15 m2 usable [C Rev F ground plan]. Equipment drop / PPE store. "
     "Hose-down point",
     "Floor IS the top of the 900 pressure slab - NOT a separate slab. "
     "Confirmed 1:80 fall to GY-11, which goes to an EXTERNAL soakaway and "
     "NEVER to the clean sump"),
    ("G-05", "HEADHOUSE - STAIR VOID EDGE", -2.000, None, "F-05", "S-02",
     "W-05", "-", "-", "WP-06", False,
     "Opening in the pressure slab 2800 x 3160, 1100 guarding to the edge "
     "[C Rev F ground plan, NBC 2016 Part 4]",
     "Guarding finish: galvanised or coated steel, 1100 high. NOT a finish "
     "decision - it is a means-of-escape requirement"),
]

WP_EXTRA = ("WP-06", "EXTERNAL-GRADE ROOF WATERPROOFING AND PROTECTION",
            "Headhouse and covered stairwell roofs stand proud of the berm; "
            "membrane and protection screed [C Rev F section C-C]", "[C]")

# ============================================================ stair finishes
# element, main staircase (U-07), entry stairwell (G-02), class
STAIRS = [
    ("GEOMETRY", "24R @ 170.8333 / 280, 3 flights x 8, total rise 4100, "
     "1200 wide, 200 well, 200 waist, headroom 2533  *** FROZEN ***",
     "12R @ 166.6667 / 300, 1500 wide, 250 waist, 11 goings x 300 = 3300",
     "[C]"),
    ("TREAD", "F-03 non-slip decontaminable, laid to the confirmed 280 going "
     "with no build-up at the nosing",
     "F-06 in-situ concrete, non-slip", "[A]"),
    ("RISER", "F-03 returned up the riser, coved to the tread. No open riser",
     "F-06, closed riser", "[A]"),
    ("NOSING", "CAST-IN non-slip nosing, contrasting. NOT an applied strip - "
     "an applied nosing changes the going and the going is FROZEN",
     "Integral cast nosing", "[A]"),
    ("LANDING", "F-03 to L1 (-)4.7333, L2 (-)3.3667 and the arrival landing "
     "(-)6.100, which is the mat surface",
     "F-06 to the top landing 0.000 and the platform (-)2.000", "[A]"),
    ("SOFFIT / WAIST", "C-02 sealed, on the 200 waist",
     "C-03 external grade, on the 250 waist, at 2200 clear", "[A]"),
    ("STRINGER / SIDE", "W-03 sealed fair-face RC on the shaft walls",
     "W-05 external grade on the 250 RC walls", "[A]"),
    ("WALL", "W-03 to full height of the shaft", "W-05", "[A]"),
    ("HANDRAIL", "Galvanised or stainless, continuous, fixed to CAST-IN "
     "sockets only. HEIGHT AND CONTINUITY TO NBC 2016 PART 4 - not a finish "
     "decision",
     "As the main staircase", "[C] requirement / [A] material"),
    ("GUARDING", "1100 to the stair void edge in the headhouse [C]",
     "Not applicable - the stairwell is enclosed by its own 250 walls",
     "[C]"),
]

# ========================================================== the four rules
RULES = [
    ("R1", "NO SUSPENDED CEILING, NO DRY LINING, NO BOXING-IN AND NO CAVITY "
     "OF ANY KIND ANYWHERE IN THE GAS-TIGHT ENVELOPE.",
     "Three independent confirmed reasons: the HVAC package requires every "
     "duct inspectable along its whole length, including the raw-air duct "
     "that is the only barrier between the clean zone and unfiltered air "
     "(HV-F2); the DRAINAGE package requires the same of every pipe and trap; "
     "and a void is a contamination trap that cannot be decontaminated. "
     "Every wall, floor and soffit finish in this schedule is applied DIRECT "
     "to the concrete."),
    ("R2", "NO FIXING MAY BE DRILLED INTO THE TANKED ENVELOPE. CAST-IN "
     "SOCKETS AND CAST-IN FRAMES ONLY.",
     "The internal cover is 40 mm and the bar spacing is 150 in both curtains "
     "as an EMP requirement (master A.5); the tanking membrane and the "
     "integral crystalline admixture are the waterproofing (R-805); and the "
     "reinforcement cage is the EMP shield. A drilled anchor risks all three. "
     "Bunk frames, handrails, cable trays, duct supports and door frames are "
     "all CAST IN."),
    ("R3", "THE FLOOR FINISH IS PART OF THE DRAINAGE DESIGN, NOT A SEPARATE "
     "DECISION.",
     "The falls, the screed thickness and the 25-78 mm build-up are set in "
     "DRAINAGE calculation D.15 and are constrained by the 1.0 kPa mat SIDL "
     "allowance (finding DR-F4, referred to the structural engineer). "
     "A heavier finish spends an allowance that is already exceeded."),
    ("R4", "EVERY JUNCTION IN A WET OR CLEAN AREA IS COVED, NOT BUTTED.",
     "Floor to wall, wall to soffit, and around every gully and pipe sleeve. "
     "A butt joint at the floor is exactly where contaminant collects and it "
     "is the one place a hose cannot reach."),
]

# ===================================================== what is NOT specified
NOT_SPECIFIED = [
    ("Product, manufacturer and system for every F, S, W and C code",
     "No finish specification exists anywhere in the project", "[N]"),
    ("Finish thicknesses, other than the screed set by the drainage falls",
     "Not derivable from anything in the project", "[N]"),
    ("Colours, gloss levels and light reflectance values",
     "No architectural specification exists", "[N]"),
    ("Fire ratings of finishes and surface spread of flame",
     "NBC 2016 Part 4 is in the Part G register for means of escape and "
     "guarding only; no fire strategy for finishes exists in the project",
     "[N]"),
    ("Slip resistance values (PTV / R rating)",
     "No criterion is stated anywhere. F-03 and F-06 carry the REQUIREMENT, "
     "not a number", "[N]"),
    ("Chemical resistance schedule against the decontaminant actually to be "
     "used", "The decontaminant is not identified anywhere in the project",
     "[N]"),
    ("EMP Zone 2 enclosure specification",
     "Master K.3 confirms the REQUIREMENT and that a welded steel room is the "
     "answer; the specification is a specialist scope and is not in the "
     "project", "[C] requirement / [N] specification"),
    ("Blast door leaf finish",
     "Proprietary, vendor-tested. Do not overcoat a tested assembly", "[N]"),
    ("Door in W5 - size, position and finish",
     "W5 is confirmed as fire and gas-tight but NO DOOR IS SCHEDULED IN IT "
     "anywhere in the project, yet the decon airlock must have a clean-side "
     "exit", "[U]"),
]
