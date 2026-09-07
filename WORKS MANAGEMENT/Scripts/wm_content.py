"""
wm_content.py — engineering content for the Works Management deliverables.

Underground CBRN-hardened blast-resistant protective structure + sentry post, Pune.
Works Management package revision WM1.

Holds the project component register, construction methodology, inspection and
test plan, safety register, risk register, procurement schedule, codes register
and progress-monitoring system.  Rendered into documents by wm_docs.py and into
the handout by wm_handout_pdf.py.

Rule observed throughout: no IS clause number, MES item number, SOR/SSR
reference, specification number or document title is invented.  Where an exact
MES reference cannot be verified from the material available, the entry says
so in those words.
"""

MES_CAVEAT = ("To be verified against the applicable MES SOR/SSR/specification "
              "edition.")

# ===========================================================================
# 1  PROJECT COMPONENT REGISTER
# ===========================================================================
# (ref, component, description, source, class, in_wm_scope)
COMPONENTS = [
    ("PC-01", "Main underground box — mat foundation",
     "600 thk M35 mat on 100 M15 blinding, u/s (-)6.700, on in-situ Deccan "
     "basalt. T16 @ 150 EF EW with a T12 @ 250 x 250 link grid. 84 % utilised "
     "— the most highly worked foundation element.", "master A.4.2, B.3, F.1", "[C]", True),
    ("PC-02", "Main underground box — perimeter walls W1–W4",
     "600 thk M35, 3.200 clear height, T16 @ 150 EF EW with T12 closed links "
     "@ 200. Designed for 383 kPa blast on the walls as well as the roof "
     "(K_a = 1.0) plus a 15.41 kPa/m earth-and-water gradient.",
     "master A.4.2, B.1, F.1", "[C]", True),
    ("PC-03", "Main underground box — protective walls W6 and W7",
     "400 thk M35 at X 14800–15200 and 18000–18400. These two walls, with the "
     "mat, the perimeter walls, the pressure slab and blast doors 1 and 2, ARE "
     "the protective boundary. T20 @ 150 EF EW, T12 4L @ 200.",
     "master A.3, B.2, F.1", "[C]", True),
    ("PC-04", "Main underground box — wall W5 and partitions W8",
     "W5 200 thk at X 12600–12800, fire and gas-tight only, no pressure "
     "differential. Four W8 partitions at 110 thk with A252 mesh both faces, "
     "each with a 900 door gap at Y 2500–3400. Non-structural.",
     "master A.3, F.1", "[C]", True),
    ("PC-05", "Main underground box — pressure (roof) slab",
     "900 thk M35, top (-)2.000, soffit (-)2.900, spanning ONE WAY across the "
     "5.000 internal width. T25 @ 150 EF EW. Total design load 448.15 kPa "
     "under COMB 103. THE GOVERNING ELEMENT of the whole structure.",
     "master A.4.2, A.7.4, B.4, F.1", "[C]", True),
    ("PC-06", "Roof openings — stair void and escape shafts",
     "Stair void 2800 x 3160 at X 15200–18000, Y 600–3760; two 1400 dia escape "
     "openings. Slab locally thickened 900 to 1200 with 6-T25 and 5-T25 trimmer "
     "bands and 4-T25 diagonal bars at the re-entrant corners.",
     "master A.4.4, A.4.5, B.4.1, F.1", "[C]", True),
    ("PC-07", "Sump pit SU-01",
     "1500 x 1500 x 1500 clear, invert (-)7.600, base slab (-)8.000, walls 300 "
     "and base 400, cast monolithic with the mat with the membrane dressed "
     "around the pit. Conflict C18 (300 vs 400 base) is OPEN; 400 held.",
     "master F.1, Drainage DR1", "[C]/[U]", True),
    ("PC-08", "Escape shafts ESC 1 and ESC 2",
     "1400 dia clear, 250 RC collar, OD 1900. ESC 1 at (2050, 2050) with its "
     "head at +0.150; ESC 2 at (19900, 2050) with its head at +0.700. The 750 "
     "clearance rule means a bay must be at least 2900 wide to hold one.",
     "master A.4.5", "[C]", True),
    ("PC-09", "Blast doors 1 and 2",
     "1200 x 2100, 7 bar, gas-tight, rebound rated, in W6 and W7 at Y 600–1800, "
     "level (-)6.100. Vendor item. The cast-in frame is welded to the "
     "reinforcement cage for EMP continuity. Jambs 4-T20 each face; header "
     "400 x 1100 with 4-T20 top and bottom.", "master A.2, F.1", "[C]/[N]", True),
    ("PC-10", "Main staircase — FROZEN",
     "Bay 7. 24 risers at 170.8333, tread 280, three flights of eight, total "
     "rise 4100, flights 1200 wide, waist 200, headroom 2533. Inside the "
     "protective envelope but NOT a blast element — designed to IS 456 with "
     "normal partial factors. Geometry is frozen and is not touched by this "
     "package.", "master A.4.4, B.5; frozen by project instruction", "[C]", True),
    ("PC-11", "Entry headhouse",
     "External 4800 x 5800 sitting on the pressure slab; walls 400, roof 500, "
     "top +0.900, NO earth cover. HW3 has no wall beneath it and loads the "
     "pressure slab as a line load. Walls designed for 383 kPa on either face "
     "(conflict C10). Roof at 90 % utilisation.",
     "master A.4.6, B.7, F.3", "[C]", True),
    ("PC-12", "Covered entry stairwell",
     "External 6800 x 2000, walls 250, 12 risers at 166.6667 with 300 going, "
     "waist 250, platform 1500 x 1500 at (-)2.000, stepped raft 300 with a "
     "MOVEMENT JOINT at the headhouse. Outside the protective boundary and "
     "DECLARED EXPENDABLE.", "master A.4.7, B.6, F.2", "[C]", True),
    ("PC-13", "Engineered cover / overburden",
     "2000 layered = 40.65 kPa in six layers: 100 protection screed, 750 "
     "compacted fill at 95 % MDD, 500 crushed basalt rubble, 200 M30 burster "
     "slab, 150 granular filter, 300 topsoil and turf. The second metre is "
     "bought entirely for prompt neutron and gamma attenuation.",
     "master A.7.3", "[C]", True),
    ("PC-14", "Waterproofing system WP-01 to WP-06",
     "Continuous external tank on the blinding, up the walls and over the roof; "
     "100 protection screed; integral crystalline admixture in the concrete; "
     "internal wet-area tanking; two waterstops at every construction joint; "
     "external-grade roofing to the headhouse and stairwell.",
     "Schedule of Finishes FN1, R-805", "[C]", True),
    ("PC-15", "Drainage and sanitary installation",
     "Clean sump SU-01 with duty, standby AND hand pumps; segregated "
     "decontamination effluent to tank TK-01 (tanker only, never to the clean "
     "sump); stairwell sump SU-02; septic tank ST-01; soak pits SK-01 to SK-04; "
     "gullies, drains, chambers and the threshold channel.",
     "Drainage DR1", "[C]", True),
    ("PC-16", "HVAC and CBRN plant",
     "Two 300 m³/h NBC filter trains in true N+1 (louvre, blast valve, G4/F7 "
     "pre-filter, H14 HEPA, ASZM-TEDA carbon, fan with hand crank); CO2 "
     "scrubber; oxygen store; dehumidifier; five blast valves; fresh-air shaft "
     "SH-1 and generator air shaft SH-2; generator GEN-1 15 kVA in bay 8.",
     "HVAC HV1", "[C]", True),
    ("PC-17", "Electrical and EMP installation",
     "Supply, distribution, lighting, small power, emergency lighting, "
     "generator changeover, earthing to a 5 ohm target, EMP Zone 2 shielded "
     "enclosure in bay 3, EMP straps at every construction joint, and EMP "
     "protection at every service penetration. THE SCOPE IS CONFIRMED BUT NO "
     "ELECTRICAL DESIGN PACKAGE EXISTS — every quantity is [N].",
     "master A.3, G; MIL-STD-188-125-1", "[C] scope / [N] design", True),
    ("PC-18", "Internal finishes",
     "Thirteen spaces. Every finish is a PERFORMANCE REQUIREMENT — "
     "decontaminable, non-dusting, joint-free within a room, no suspended "
     "ceiling and no boxing-in anywhere in the gas-tight envelope. The product "
     "that satisfies each requirement is deliberately left open.",
     "Schedule of Finishes FN1", "[C] requirement / [N] product", True),
    ("PC-19", "SENTRY POST — RC frame",
     "Separate two-storey RC framed building, at least 10 m clear of the "
     "shelter excavation, on its own footings on in-situ basalt at (-)2.000. "
     "F1 1500 x 1500 x 600 x 4; C1 350 x 350 x 4 both storeys; B1/B2 250 x 450; "
     "S1 150 two-way at both levels; PB 250 x 400 at +0.450; external spiral "
     "stair. M30 / Fe500, ductile detailing to IS 13920. NOT BLAST DESIGNED — a "
     "recorded decision.", "master A.4.8, B.8, F.4", "[C]", True),
    ("PC-20", "SENTRY POST — BRICK MASONRY WALLS  (design change SP-B1)",
     "Infill walls between the columns, both storeys, 190 thk one-brick "
     "modular brickwork in CM 1:6 within the confirmed 200 structural zone. "
     "REPLACES the 200 RC ballistic infill panels of Rev F. Ground storey has "
     "door D1 900 and window W1 1200; first storey has eight armoured vision "
     "panels 1200 wide and door D1. Lintels are a NEW requirement created by "
     "this change.", "SP-B1, this package; geometry from Rev F drawings 3, 4, 6",
     "[C] instruction / [D] quantities", True),
    ("PC-21", "External works, berm and site restoration",
     "Berm graded 1.5:1 to +0.900 against the headhouse and covered stairwell; "
     "site crowned with 1:50 falls away from the structure; surface water "
     "drainage; access route and hardstanding; removal of temporary works. NO "
     "SITE PLAN OR GROUND MODEL EXISTS, so extents are indicative.",
     "master A.4.6, A.4.7; Drainage DR1 open item D3", "[C] intent / [N] extent", True),
    ("PC-22", "Camouflage and concealment",
     "The 300 topsoil and turf layer at the top of the engineered cover is the "
     "only concealment element the project confirms; its stated function is "
     "'concealment, erosion, sheds rain'. Any further measure — spoil dressing, "
     "screening, track discipline, planting regime — is planned as work but has "
     "no specification in the project.", "master A.7.3", "[C] layer / [N] regime", True),
    ("PC-23", "Testing, commissioning and handover",
     "Cube results, NDT, watertightness, drainage tests, electrical tests, "
     "earth resistance, EMP shielding effectiveness survey to IEEE Std 299, "
     "blast door functional and seal tests, escape shaft functional test, "
     "CBRN commissioning, gas-tightness and overpressure test, generator load "
     "test, integrated protective-mode commissioning, training and handover.",
     "master G; this package", "[C]", True),
]

NOT_COMPONENTS = [
    ("Lift / lift shaft", "The supplied R0 schedule contains 'Column, Staircase "
     "& Lift Shear Wall' activities. THERE IS NO LIFT ANYWHERE IN THIS PROJECT. "
     "Those activities are generic building boilerplate and have been removed."),
    ("Second grade slab over 4 m of overburden", "The R0 schedule programmes a "
     "'2nd Slab (Ground Lvl) Grade Slab' over '4m Soil Overburdon'. The current "
     "design has a SINGLE 900 pressure slab at (-)2.000 under 2000 of layered "
     "engineered cover containing a 200 M30 burster slab. The 4 m arrangement is "
     "a superseded revision."),
    ("1000 mm roof slab", "The R0 schedule calls the roof '1st Slab (1000 mm "
     "Thk)'. The confirmed thickness is 900."),
    ("Structural RC columns in the shelter", "None exists. The box is a wall-and-"
     "slab structure; master B.3 declares punching shear NOT APPLICABLE for the "
     "same reason, and Structural CAD SC1 records that drawing a column sheet "
     "would be fabrication."),
    ("Dado / wall tiling in the shelter", "The R0 schedule programmes wall tiles. "
     "The Schedule of Finishes states the opposite for the gas-tight envelope: "
     "'NO joints, NO tiles, NO grout — grout lines are a decontamination "
     "failure'. Tiling is therefore not programmed inside the envelope."),
    ("Suspended ceilings and gypsum punning in the shelter", "The R0 schedule "
     "programmes gypsum punning to ceilings. FN1 forbids any suspended ceiling "
     "or boxing-in in the gas-tight envelope for three confirmed reasons: duct "
     "inspectability, pipe inspectability and contamination trapping."),
]

# ===========================================================================
# 2  CONSTRUCTION METHODOLOGY
# ===========================================================================
METHODOLOGY = [
    ("M1", "Site establishment and setting out", [
        "The site is a military installation, so the boundary, gate and access "
        "control are established before any other activity and workforce "
        "security clearance runs in parallel with mobilisation.",
        "Setting out uses the project's own coordinate system (master A.4.1): "
        "origin at the south-west external corner of the box at ground level, X "
        "east 0 to 22000, Y north 0 to 6200, levels in metres relative to "
        "finished grade 0.000. Two permanent benchmarks are established outside "
        "the excavation influence zone and checked independently.",
        "The sentry post is set out from the same grid but its site position is "
        "ASSUMED in the project — no coordinate for it exists. The only "
        "confirmed constraint is that it stands at least 10 m clear of the "
        "shelter excavation. That distance is set out and recorded before any "
        "excavation begins.",
        "Temporary water supply is sized on curing demand, not domestic demand. "
        "About 1060 m² of formed concrete face requires continuous curing for up "
        "to 14 days at a time.",
    ]),
    ("M2", "Excavation", [
        "Topsoil is stripped 150 deep and STOCKPILED, not carted away: the same "
        "material returns as the 300 concealment layer at the top of the "
        "engineered cover.",
        "Excavation is 6.800 m deep over a 24.000 x 8.200 envelope, which "
        "includes 1.000 m of working space outside the external wall face. That "
        "working space is not optional — the external tanking membrane and its "
        "protection are applied from outside the structure.",
        "Only the top 1.5 to 2.0 m is soil; below rockhead the material is "
        "Deccan basalt. Rock is removed by HYDRAULIC BREAKER, not by blasting. "
        "The sentry post founds on the same rock within 10 m, the site is "
        "operational, and controlled blasting would require a vibration regime "
        "the project has not specified.",
        "The single most important instruction to the excavation gang concerns "
        "the flow contacts. Master A.6 is explicit: the hazard is not the basalt "
        "but the red-bole and vesicular seams between flows. A single red-bole "
        "seam under the mat produces the differential-support case that SIZES "
        "the mat. Every seam exposed at formation is over-excavated and replaced "
        "with M15 lean concrete before the formation is approved.",
        "The formation is a HOLD POINT. It is trimmed, cleaned of all loose "
        "rock, inspected for seams and approved by the Engineer before the "
        "blinding is placed.",
    ]),
    ("M3", "Dewatering", [
        "The design groundwater table is (-)2.000 in the monsoon and is ASSUMED "
        "— the master calls it the single most important number the site "
        "investigation must confirm. Of the 15.41 kPa/m lateral gradient on the "
        "walls, 9.81 is water and only 5.60 is soil.",
        "Construction dewatering runs continuously from the start of the deep "
        "excavation until the side backfill is complete, with a standby pump and "
        "an independent power source. Groundwater monitoring during the monsoon "
        "is programmed as a critical-path activity precisely because the answer "
        "changes the dewatering, the tanking and the flotation check.",
        "Discharge is to the surface water system away from the excavation, "
        "through a settlement facility. Silt-laden discharge into the soak pits "
        "would destroy their percolation capacity before they are commissioned.",
    ]),
    ("M4", "Blinding, tanking and the mat", [
        "100 M15 blinding is placed over the whole formation, projecting 100 "
        "beyond the mat, to give a clean surface for the membrane.",
        "The external tanking WP-01 is a CONTINUOUS TANK: horizontal on the "
        "blinding, turned up the external wall faces, and lapped to the roof "
        "membrane. It is inspected and signed off before it is covered, because "
        "after that it can never be seen again.",
        "The mat is cast in a single continuous pour of about 85 m³ including "
        "the sump pit, which is cast monolithic with it and has the membrane "
        "dressed around it.",
        "Wall starter bars are set with a 900 horizontal leg into the mat and a "
        "50 phi lap above a 150 kicker. Getting the starters wrong at this stage "
        "is the most expensive error available on the job.",
        "Curing is 14 days continuous. The mat is a 600 mass section in M35 and "
        "is 84 % utilised.",
    ]),
    ("M5", "Walls", [
        "The 3.200 m wall height is cast in two lifts of 1.600 m. Vertical "
        "construction joints are formed at about 6 m centres; at every joint the "
        "reinforcement is FULLY CONTINUOUS and two waterstops plus a welded "
        "copper or galvanised EMP strap are installed. A construction joint in a "
        "protective structure is simultaneously a water path, a gas path and an "
        "EMP discontinuity, and all three have to be closed.",
        "There is no movement joint anywhere inside the protective envelope. The "
        "only movement joint on the project is where the covered stairwell raft "
        "meets the headhouse — outside the boundary, in the structure that is "
        "declared expendable.",
        "Bar spacing is 150 both curtains throughout. This is an EMP requirement "
        "and is stricter than IS 456 — it is not a strength requirement and must "
        "not be relaxed on site to ease congestion.",
        "The blast door frames are set, aligned and WELDED TO THE CAGE in W6 and "
        "W7 before those walls are poured. This is why the doors are ordered on "
        "day one: a 75-day frame lead time sits directly upstream of the wall "
        "concrete, and a late frame stops the wall.",
        "500 x 500 haunches with diagonal T20 @ 150 are formed at every "
        "wall–mat and wall–roof junction.",
    ]),
    ("M6", "Pressure slab", [
        "The pressure slab is the governing element: 900 thk, T25 @ 150 each "
        "face each way, 20.5 t of reinforcement, carrying 448.15 kPa. It spans "
        "ONE WAY across the 5.000 internal width, which is the single fact that "
        "makes lengthening the box cheap and widening it expensive.",
        "Falsework carries 104 m² of deck at 3.200 m height and is designed and "
        "checked as temporary works.",
        "Reinforcement is fixed in a fixed order: bottom curtain, opening "
        "trimmers, escape shaft collar bands, local thickenings, links, top "
        "curtain, haunches. The opening details are not incidental — the stair "
        "void carries 6-T25 top and bottom with 4-T25 diagonal bars at each "
        "re-entrant corner, and each shaft carries 5-T25 on every side, face and "
        "direction with the slab thickened 900 to 1200 over a 600 annulus.",
        "IS 4991 Cl. 10.3.1.1 allows NO dynamic increase on shear. That is why "
        "the end 1500 of the slab carries four-legged T12 links at 250 that a "
        "static design would not need, and it is the most commonly misapplied "
        "rule in blast design.",
        "The slab is cast in a single continuous pour of 112 m³. Curing is 14 "
        "days. Props remain 14 days — IS 456 Table 11, props to a slab spanning "
        "over 4.5 m. This span is 5.000 m clear. Those 19 days sit on the "
        "critical path and cannot be argued away.",
    ]),
    ("M7", "Entry structures and escape shafts", [
        "The headhouse is built off the top of the pressure slab, its floor "
        "being the slab surface at (-)2.000. Wall HW4 aligns exactly with W7 "
        "after modification M1; HW3 has no wall beneath it and loads the slab as "
        "a line load, which the slab was checked for.",
        "The headhouse roof is 500 thk at 90 % utilisation — the most highly "
        "worked element in the project. Its reinforcement inspection is a hold "
        "point attended by the structural consultant.",
        "The covered entry stairwell is built on a stepped raft on compacted "
        "fill, with the movement joint at the headhouse. It is outside the "
        "protective boundary and is DECLARED EXPENDABLE; it is built to IS 456 "
        "with normal partial factors and is not blast rated.",
        "The escape shaft collars are 250 RC, OD 1900, rising from the roof slab "
        "to +0.150 at ESC 1 and +0.700 at ESC 2. They are built before the "
        "engineered cover so that the cover is placed against a finished collar, "
        "not around a partly built one.",
    ]),
    ("M8", "Backfill, engineered cover and overburden", [
        "The walls are NOT backfilled until the pressure slab is cast and cured. "
        "A 3.2 m wall carrying an 83.2 kPa gradient at its base needs the roof "
        "as its prop; backfilling earlier means designing and installing "
        "temporary propping to do the same job worse.",
        "Side backfill is placed in 250 layers compacted to 95 % MDD and tested "
        "in situ before the cover goes on.",
        "The engineered cover is a designed six-layer structure, not a filling "
        "operation, and it is built from the bottom up in the reverse of the "
        "order given in master A.7.3: 100 protection screed over the membrane, "
        "750 compacted engineered fill at 95 % MDD (the radiation mass), 500 "
        "crushed basalt rubble at 25–75 mm (which scatters burster energy), the "
        "200 M30 burster slab reinforced T12 @ 150 both ways (which breaks up a "
        "penetrating item), 150 granular filter (which stops fines clogging the "
        "rubble) and 300 topsoil and turf (concealment and erosion control).",
        "The 500 rubble layer is won from the site's own rock excavation and "
        "crushed on site. About 994 m³ of basalt is excavated and only about 51 "
        "m³ of rubble is needed, so the layer costs haulage and crushing and "
        "nothing else. This is the largest single saving available on the job.",
        "The cover does not extend over the headhouse, which has no earth cover, "
        "nor over the two escape shaft heads.",
        "The completed build-up is verified against master A.7.3 — the design "
        "load of 40.65 kPa on the roof depends on those six layers being the "
        "thicknesses and materials stated.",
    ]),
    ("M9", "Sentry post — frame", [
        "The sentry post is an independent structure and is deliberately NOT "
        "started until the main rock breaking is finished. No green concrete "
        "stands within 10 m of a hydraulic breaker.",
        "Footings F1 found on in-situ basalt at (-)2.000; the founding stratum is "
        "a hold point in the same way as the main formation.",
        "Columns, beams and slabs are detailed to IS 13920 for Zone III. The "
        "detail that most often gets lost on site is the column confinement: "
        "T10 hoops with a cross-tie each way at 85 c/c over 500 mm from EVERY "
        "joint face, top and bottom, AND THROUGH THE JOINT.",
        "Slab S1 carries corner torsion reinforcement — T8 @ 200 in FOUR LAYERS "
        "over 700 x 700 at all four corners (IS 456 Annex D-1.8). It is a small "
        "quantity of steel that is routinely omitted and should not be.",
        "Beam B2 is reinforced 3-T20 rather than 5-T16 because five T16 bars "
        "need 256 mm of width in a 250 mm beam. That check is recorded in the "
        "master and is exactly the kind of item that becomes a site query if it "
        "is skipped.",
    ]),
    ("M10", "Sentry post — BRICK MASONRY WALLS (design change SP-B1)", [
        "See the dedicated methodology section — this is the only design change "
        "carried by the Works Management package.",
    ]),
    ("M11", "Services", [
        "Builder's work — sleeves, ducts and penetrations — is coordinated with "
        "the reinforcement and is a predecessor to the wall inspection hold "
        "point. Cutting a penetration afterwards through a 600 wall at 150 bar "
        "spacing both curtains is not a repair, it is a defect.",
        "Every duct and every pipe in the gas-tight envelope must remain "
        "inspectable along its whole length. That is why there is no suspended "
        "ceiling and no boxing-in anywhere in bays 1 to 6.",
        "The decontamination effluent system is physically segregated from the "
        "clean sump and is never connected to it. Effluent goes to tank TK-01 "
        "for tanker removal.",
        "The rising main from the clean sump carries four devices in series "
        "inside the envelope: isolation valve, gas-tight non-return valve, blast "
        "check valve and a 75 deep-seal trap. Each closes a different failure "
        "path.",
        "The EMP works are structural as much as electrical: straps welded at "
        "every construction joint, the blast door frames welded to the cage, "
        "protection at every service penetration, and a welded steel Zone 2 room "
        "in bay 3 because the reinforcement cage on its own gives 0 dB at 1 GHz.",
    ]),
    ("M12", "Finishes", [
        "Every finish in this project is specified as a PERFORMANCE REQUIREMENT "
        "and the product is deliberately left open. The requirements come from "
        "the decontamination duty, the gas-tight envelope, the EMP requirement "
        "and the wet areas.",
        "Floors are laid to falls, joint-free within a room, and coved into the "
        "skirting in one piece. In the wet areas — bays 2, 5 and 6 — the finish "
        "is fully impervious and coved 150 up every wall in a single piece, with "
        "no tiles and no grout, because a grout line is a decontamination "
        "failure.",
        "Wall finishes are applied direct to the concrete. There is no cavity, "
        "no dry lining and no batten anywhere in the envelope: a lined cavity is "
        "a contamination trap that cannot be decontaminated or inspected.",
    ]),
    ("M13", "External works and concealment", [
        "The berm is graded 1.5:1 to +0.900 against the headhouse and covered "
        "stairwell, and the site is crowned with 1:50 falls away from the "
        "structure.",
        "Turf over the cover is the confirmed concealment measure. Anything "
        "beyond it — spoil dressing, screening, planting regime, track "
        "discipline — is programmed as work but has no specification in the "
        "project, and the extent must be confirmed before it is priced.",
        "Site restoration removes the temporary works, the haul road and the "
        "dewatering installation, and reinstates the ground so that the finished "
        "site reads as ground, which is the point of the whole exercise.",
    ]),
    ("M14", "Testing, commissioning and handover", [
        "Structural verification is by 28-day cube results supported by "
        "ultrasonic pulse velocity and rebound hammer testing.",
        "The protective systems are tested in a fixed order because each depends "
        "on the one before: EMP shielding effectiveness survey, blast door "
        "functional and seal test, then the gas-tightness and overpressure test "
        "of bays 1 to 6, then CBRN filter train commissioning, then integrated "
        "protective-mode operation.",
        "Two claims must never be made, and are not made here. A static "
        "analysis gives the DEMAND on a blast structure; it is not proof of "
        "blast resistance — the non-linear support-rotation check is Phase 3 "
        "work. And flotation can never be read off a model whose springs take "
        "tension; it is a hand check.",
        "Handover includes as-built drawings, O&M manuals, all test "
        "certificates, and operator training on the CBRN plant, the pumps, the "
        "generator, the blast doors and the escape shafts.",
    ]),
]

# ===========================================================================
# 3  SENTRY POST BRICK MASONRY METHODOLOGY — design change SP-B1
# ===========================================================================
BRICK_METHOD = {
    "decision": (
        "The sentry post walls are BRICK MASONRY. This replaces the '200 RC "
        "BALLISTIC INFILL PANELS' shown on Rev F drawings 3, 4 and 6 and "
        "described in master A.4.8. It is the only design change carried by this "
        "Works Management package and it is recorded as reference SP-B1."),
    "consequence": (
        "Two consequences follow and are recorded rather than buried. First, "
        "brick masonry does not provide the ballistic protection that the Rev F "
        "panels were named for; the change removes a stated protective function "
        "from the sentry post, which is already a structure the project declares "
        "NOT blast designed and expendable. Second, the openings now need "
        "lintels, which the RC panels did not, and no lintel design exists "
        "anywhere in the project. Both are carried into the verification "
        "register for the designer to close."),
    "geometry": [
        ("Wall run per storey", "15.200 m",
         "4.000 - 2 x 0.350 = 3.300 on the north and south walls, 5.000 - 2 x "
         "0.350 = 4.300 on the east and west walls, two of each"),
        ("Panel height", "2.600 m",
         "the project's own confirmed figure — master A.7.7 gives the infill "
         "load as 13.000 kN/m = 0.200 x 2.600 x 25, verified"),
        ("Structural zone", "200 mm",
         "unchanged from Rev F; the columns' outer faces are flush with the wall"),
        ("Brickwork thickness", "190 mm",
         "one brick thick in modular bricks to IS 1077 (190 x 90 x 90), built "
         "inside the 200 zone with the residual 10 mm taken up at the internal "
         "face in the plaster, so the confirmed 4000 x 5000 external envelope "
         "and the column faces are preserved exactly"),
        ("Ground storey openings", "D1 900 wide; W1 1200 wide",
         "D1 in the west wall at Y 1000–1900; W1 in the east wall at Y 1900–3100 "
         "— both read from the Rev F drawing"),
        ("First storey openings", "8 vision panels 1200 wide; D1 900",
         "two panels per face on all four faces; the door lies within the west "
         "panel on the drawing, and the overlap is a verification item"),
        ("Quantity", "12.20 m³ / 64.19 m² face",
         "6.88 m³ ground storey, 5.32 m³ first storey, net of openings"),
        ("Materials", "~6 400 bricks; 15 bags cement; 3.0 m³ sand",
         "modular bricks class 10 to IS 1077 with 5 % breakage; CM 1:6"),
    ],
    "method": [
        "SOURCE APPROVAL AND TESTING. Bricks are procured against IS 1077 as "
        "class designation 10 (10 N/mm² minimum average compressive strength). "
        "Samples are drawn to IS 5454 and tested to IS 3495 for compressive "
        "strength, water absorption, efflorescence and warpage before any brick "
        "is laid. On a military structure the source is approved once and not "
        "changed without retesting.",
        "STACKING AND WETTING. Bricks are stacked to IS 4082 clear of the "
        "working area and are thoroughly soaked before laying so that they do "
        "not draw water out of the mortar. Dry bricks in a CM 1:6 bed are the "
        "most common cause of weak masonry on Indian sites.",
        "MORTAR. Cement mortar 1:6 by volume for the general walling, prepared "
        "and used to IS 2250, with sand to IS 2116. Mortar is used within 30 "
        "minutes of mixing and is never re-tempered. Gauge boxes are used — "
        "proportioning by shovel is not accepted.",
        "BOND AND COURSING. English bond, one brick thick. Joints are 10 mm and "
        "are fully filled — bed, cross and vertical. Every fourth course is "
        "checked for level and every panel is checked for plumb. Courses are "
        "kept level and no part of the wall is raised more than one metre above "
        "another in a day's work.",
        "INTERFACE WITH THE FRAME. The masonry is an INFILL between RC columns "
        "and under RC beams. It is not a load-bearing wall and must not be built "
        "tight to the beam soffit in one operation: the top course is left down "
        "and is wedged and packed after the panel below has taken its initial "
        "shrinkage, so that the panel does not attract load from the frame it "
        "was not designed to carry.",
        "TIES TO THE COLUMNS. The masonry is tied to the columns so that the "
        "panel is restrained out of plane. The tie detail does not exist in the "
        "project and is carried as a verification item; until it is designed, "
        "the assumption for planning is starter bars or proprietary ties at "
        "every fourth course.",
        "SEISMIC NOTE — NOT RESOLVED HERE. Master A.7.8 records that the sentry "
        "post uses R = 3.0 precisely BECAUSE the infill is not separated from "
        "the frame, and B.8 designs to V_b = 73.18 kN. Substituting brick "
        "masonry at about 20 kN/m³ for 200 RC at 25 kN/m³ reduces the infill "
        "line load from 13.000 kN/m to roughly 9.9 kN/m and therefore reduces "
        "the seismic weight, which points the existing design in the "
        "conservative direction. That is a direction, not a verification. The "
        "structural discipline must re-run the check; this package does not.",
        "LINTELS. RC lintels are required over D1, W1 and the eight vision "
        "panels. Bearing is taken as 200 each end for planning. NO LINTEL DESIGN "
        "EXISTS IN THE PROJECT — section, reinforcement and bearing are to be "
        "designed before the openings are built, and the 200 x 150 section used "
        "for the estimate is for quantity only.",
        "CURING. Masonry is kept damp for at least seven days. Chases for "
        "electrical conduit are CUT, not hammered, and never cut into a course "
        "until the masonry has cured.",
        "TOLERANCES AND INSPECTION. Line, level, plumb and joint thickness are "
        "inspected at a hold point at the end of each storey before plaster. "
        "Plumb over the 2.600 storey height and joint thickness are the two "
        "measurements that decide whether the plaster can be held to its stated "
        "thickness.",
    ],
}

# ===========================================================================
# 4  INSPECTION AND TEST PLAN
# ===========================================================================
# (ref, work, stage, requirement, reference, type, record)
ITP = [
    # --- earthworks
    ("Q-01", "Site setting out", "Before excavation",
     "Position, orientation and level against the master A.4.1 grid; independent "
     "check. Sentry post at least 10 m clear of the excavation.",
     "master A.4.1, A.2", "WITNESS", "Setting-out record and check certificate"),
    ("Q-02", "Excavation", "During",
     "Line, level and stability of the faces; edge protection in place; "
     "dewatering operating.", "IS 3764", "SURVEILLANCE", "Daily excavation record"),
    ("Q-03", "Formation", "Before blinding",
     "Formation level (-)6.800; loose rock removed; red-bole and vesicular seams "
     "identified, over-excavated and replaced with M15. Founding stratum "
     "confirmed as in-situ basalt. The same check applies to the sentry post "
     "footings at (-)2.000 (H-11).", "master A.6", "HOLD (H-01, H-11)",
     "Formation approval certificate with a seam map"),
    ("Q-04", "Backfill and engineered fill", "Each layer",
     "Layer thickness not exceeding 250; in-situ dry density at least 95 % MDD.",
     "IS 2720 (Part 8) for MDD; IS 2720 (Part 28) sand replacement",
     "TEST", "Field density test sheets, one set per layer per 100 m²"),
    ("Q-05", "Engineered cover build-up", "On completion",
     "Six layers reproduced at the thicknesses and materials of master A.7.3, "
     "totalling 2000 and 40.65 kPa.", "master A.7.3", "HOLD",
     "Cover verification record with layer levels"),
    # --- concrete
    ("Q-06", "Concrete mix", "Before first pour",
     "Trial mix and design for M35 (box) and M30 (sentry). Minimum cement 340 "
     "kg/m³ and w/c not more than 0.45 for M35 very severe exposure. Integral "
     "crystalline waterproofing admixture.",
     "IS 456 Table 5; IS 10262; IS 2645", "HOLD", "Approved mix design"),
    ("Q-07", "Cement, aggregate and water", "Each delivery / source",
     "Cement to IS 269 or IS 1489 (Part 1) with test certificates; aggregate to "
     "IS 383 tested to IS 2386; water to IS 456 Cl. 5.4.",
     "IS 269, IS 383, IS 2386, IS 456 Cl. 5.4", "TEST", "Material test register"),
    ("Q-08", "Reinforcement", "Each consignment",
     "Fe500D to IS 1786 for the box; Fe500 for the sentry post. Mill "
     "certificates plus independent tensile and bend tests per lot.",
     "IS 1786", "TEST", "Mill certificates and independent test reports"),
    ("Q-09", "Reinforcement fixing — mat", "Before pour",
     "Bar size, spacing 150 both curtains, laps 50 phi staggered so not more "
     "than 50 % are spliced at a section, cover 75 to the blinding and 50 to "
     "formed faces, chairs and spacers, wall starters with a 900 leg.",
     "IS 456 Cl. 26.2, 26.4.2, Table 16; master A.5, F.1", "HOLD (H-03)",
     "Pre-pour reinforcement checklist countersigned by the structural consultant"),
    ("Q-10", "Reinforcement fixing — walls", "Before each lift",
     "As Q-09 plus blast door jamb bars 4-T20 each face, header cage, haunch "
     "diagonals, and the blast door frame set, aligned and WELDED TO THE CAGE.",
     "master F.1", "HOLD (H-04, H-05, H-07)",
     "Pre-pour checklist and frame alignment record. H-07 is the headhouse walls, "
     "which carry the same 383 kPa either-face requirement"),
    ("Q-11", "Reinforcement fixing — pressure slab", "Before pour",
     "T25 @ 150 EF EW; opening trimmers 6-T25 and 5-T25; 4-T25 diagonals at the "
     "re-entrant corners; local thickenings 900 to 1200; four-legged T12 links "
     "@ 250 in the end 1500; HW3 band 4-T25 top and bottom; all cast-in items.",
     "master B.4, B.4.1, F.1", "HOLD (H-06, H-08)",
     "Pre-pour checklist countersigned by the structural consultant. H-08 is the "
     "headhouse roof, the most highly worked element at 90 % utilisation"),
    ("Q-12", "Formwork and falsework", "Before pour",
     "Line, level, plumb, camber, tightness and cleanliness; falsework designed "
     "and checked as temporary works.", "IS 456 Cl. 11; IS 14687", "HOLD",
     "Formwork release note; falsework design check"),
    ("Q-13", "Concrete placing", "During pour",
     "Slump on every load; placing and compaction; no cold joint in a "
     "continuous pour; temperature control on the 900 slab and 600 mat.",
     "IS 456 Cl. 13; IS 1199", "SURVEILLANCE", "Pour card per pour"),
    ("Q-14", "Concrete strength", "7 and 28 days",
     "Cube sampling and testing; acceptance to IS 456 Cl. 15 and 16.",
     "IS 516; IS 456 Cl. 15, 16", "TEST", "Cube test certificates"),
    ("Q-15", "Curing", "After each pour",
     "Continuous moist curing: 14 days for the mat, the pressure slab and the "
     "headhouse roof; 7 days minimum elsewhere.", "IS 456 Cl. 13.5", "SURVEILLANCE",
     "Curing register"),
    ("Q-16", "Formwork striking", "Before striking",
     "Vertical faces after 16–24 h; props to slabs spanning over 4.5 m after 14 "
     "days. The pressure slab spans 5.000 clear.", "IS 456 Cl. 11.3 Table 11",
     "HOLD", "Striking permit signed by the site engineer"),
    ("Q-17", "Construction joints", "At each joint",
     "Surface prepared; reinforcement fully continuous; TWO waterstops and a "
     "welded EMP strap installed before the next pour.",
     "IS 456 Cl. 13.4; master F.1", "HOLD",
     "Joint record with photographs of the strap and waterstops"),
    ("Q-18", "Hardened concrete — NDT", "After 28 days",
     "Ultrasonic pulse velocity and rebound hammer on a sampling basis, "
     "concentrating on the pressure slab and the protective walls.",
     "IS 13311 (Part 1) and (Part 2)", "TEST", "NDT report"),
    # --- waterproofing
    ("Q-19", "Tanking — substrate", "Before application",
     "Substrate sound, clean, dry and free of laitance; fillets formed at all "
     "internal angles.", "IS 3067", "WITNESS", "Substrate acceptance record"),
    ("Q-20", "Tanking — horizontal and vertical", "Before covering",
     "Continuity, laps, terminations, upstands and dressing to every "
     "penetration; protection layer in place before backfilling.",
     "IS 3067; FN1 WP-01/WP-02", "HOLD (H-02, H-09, H-10)",
     "Tanking inspection certificate with photographic record"),
    ("Q-21", "Watertightness", "After completion",
     "Visual inspection of the whole internal envelope for damp and seepage "
     "after the first monsoon exposure or a flood test where practicable.",
     "IS 6494 principles", "WITNESS", "Watertightness inspection report"),
    # --- sentry post masonry
    ("Q-21A", "SENTRY POST — RC footings and frame reinforcement",
     "Before each pour",
     "Bar size, spacing, cover 50 to footings / 40 to columns / 30 to beams and "
     "slabs; column starters 8-T16; IS 13920 detailing — T10 confining hoops "
     "with a cross-tie each way @ 85 over 500 from every joint face AND through "
     "the joint; slab corner torsion steel T8 @ 200 in four layers over 700 x "
     "700 at all four corners.",
     "IS 456; IS 13920 Cl. 7.4, 8.1, 8.2; IS 456 Annex D-1.8; master F.4",
     "HOLD (H-12, H-13, H-14)",
     "Pre-pour reinforcement checklist countersigned by the structural consultant"),
    ("Q-22", "SENTRY POST — brick source", "Before order",
     "Class designation 10 modular bricks; sampling to IS 5454; testing to "
     "IS 3495 for compressive strength, water absorption, efflorescence and "
     "warpage. Dimensional tolerance check on the 190 x 90 x 90 size.",
     "IS 1077; IS 3495; IS 5454", "HOLD", "Brick test report and source approval"),
    ("Q-23", "SENTRY POST — masonry mortar", "Each batch",
     "CM 1:6 by volume using gauge boxes; sand to IS 2116; used within 30 "
     "minutes; never re-tempered. Mortar cube tests on a sampling basis.",
     "IS 2250; IS 2116", "TEST", "Mortar register and cube results"),
    ("Q-24", "SENTRY POST — masonry workmanship", "Each storey",
     "English bond one brick thick; 10 mm joints fully filled bed, cross and "
     "vertical; bricks thoroughly soaked before laying; not more than 1 m of "
     "lift above adjacent work in a day.", "IS 2212", "SURVEILLANCE",
     "Daily masonry record"),
    ("Q-25", "SENTRY POST — line, level, plumb and joints", "End of each storey",
     "Plumb over the 2.600 storey height; level every fourth course; joint "
     "thickness 10 mm nominal; panel dimensions against the 190 thickness "
     "inside the 200 structural zone.", "IS 2212; IS 1905", "HOLD (H-15, H-16)",
     "Masonry inspection record with measured plumb and joint thickness"),
    ("Q-26", "SENTRY POST — infill / frame interface", "Before plaster",
     "Top course wedged and packed only after the panel has taken its initial "
     "shrinkage; ties to the columns installed at the specified spacing.",
     "IS 1905; SP-B1", "HOLD", "Interface inspection record"),
    ("Q-27", "SENTRY POST — lintels", "Before and after casting",
     "Approved lintel design in place before the opening is built; section, "
     "reinforcement, bearing 200 minimum each end, and curing.",
     "IS 456; design NOT YET ISSUED", "HOLD", "Lintel inspection record"),
    ("Q-28", "SENTRY POST — plaster", "Before and after",
     "Surface prepared and raked; thickness, true to line and level; cured "
     "seven days; no hollowness on tapping.", "IS 1661", "WITNESS",
     "Plaster inspection record"),
    ("Q-29", "SENTRY POST — flooring and finishes", "On completion",
     "Level, falls, finish and freedom from cracking.", "IS 2571 for in-situ "
     "cement concrete flooring", "WITNESS", "Finish inspection record"),
    ("Q-30", "SENTRY POST — painting", "Each coat",
     "Surface preparation, primer and coats; adhesion.",
     "IS 2395 (Part 1)", "WITNESS", "Painting record"),
    # --- services
    ("Q-31", "Drainage — pipes and chambers", "Before covering",
     "Line, level, gradient, jointing; water or air test; rodding access at "
     "every change of direction.", "IS 1742 principles; Drainage DR1",
     "HOLD", "Drainage test certificate"),
    ("Q-32", "Sump and pumps", "On commissioning",
     "Duty and standby pump performance; auto-alternation; level switch "
     "settings at start +900, stop +300 and high alarm +1200 above the invert; "
     "hand pump PU-03 proved independently of power.", "Drainage DR1",
     "TEST", "Pump commissioning record"),
    ("Q-33", "Soak pits", "Before construction",
     "PERCOLATION TEST IS MANDATORY and must precede construction; SK-01 is "
     "already 2.3 % short of its own stated requirement (conflict C19, OPEN).",
     "IS 2470 (Part 2) Cl. 4", "HOLD", "Percolation test report"),
    ("Q-34", "Septic tank", "On completion",
     "Capacity, baffle at two-thirds of the length, inlet and outlet tees, "
     "50 cowled vent at least 2 m above grade; watertightness.",
     "IS 2470 (Part 1) Cl. 6.2, 6.3, 6.5, 6.6, 6.9, Table 1", "WITNESS",
     "Septic tank inspection record"),
    ("Q-35", "Electrical installation", "On completion",
     "Insulation resistance, continuity, polarity, protective device "
     "operation.", "IS 732", "TEST", "Electrical test certificate"),
    ("Q-36", "Earthing", "On completion",
     "Earth electrode resistance against the 5 ohm target; bonding continuity "
     "to all metalwork.", "IS 3043; IEEE 142", "TEST", "Earth resistance test report"),
    ("Q-37", "EMP shielding", "After enclosure and all penetrations",
     "Shielding effectiveness survey, 80 dB over 10 kHz to 1 GHz.",
     "IEEE Std 299; MIL-STD-188-125-1 §5.4, §5.5, §5.7.2.1, §5.7.4.1, §5.7.6",
     "TEST", "Shielding effectiveness survey report"),
    ("Q-38", "Blast doors", "On installation",
     "Alignment, seal compression, operation, and the vendor's rating "
     "documentation. The tested assembly is NOT overcoated.",
     "Vendor specification; FN1 D-01", "HOLD", "Door installation and seal test record"),
    ("Q-39", "Gas-tightness and overpressure", "After doors and finishes",
     "Envelope leakage of bays 1 to 6 (67.8 m² floor, 217.0 m³ volume) and "
     "overpressure hold with the filter trains running.",
     "FEMA 453 principles; project protective requirement", "TEST",
     "Gas-tightness and overpressure test report"),
    ("Q-40", "CBRN filter trains", "On commissioning",
     "Airflow, filter seating, in-place leak test of the H14 HEPA stage, carbon "
     "bed condition, hand-crank operation of each fan.",
     "EN 1822 for the HEPA classification; HVAC HV1", "TEST",
     "Filter train commissioning report"),
    ("Q-41", "Generator", "On commissioning",
     "Load test, changeover proving, exhaust and combustion air path, bunding.",
     "HVAC HV1", "TEST", "Generator commissioning report"),
    ("Q-42", "Integrated protective mode", "Before handover",
     "Whole-system operation in protective mode: doors closed, blast valves "
     "set, filter trains running, overpressure maintained, drainage isolated.",
     "This package", "HOLD", "Integrated commissioning report"),
]

# ===========================================================================
# 5  SAFETY MANAGEMENT
# ===========================================================================
# (ref, activity, hazard, control, reference)
SAFETY = [
    ("S-01", "Deep excavation, 6.8 m",
     "Collapse of the soil zone above rockhead; fall of persons and plant into "
     "the excavation; fall of material from the edge.",
     "Battered or supported faces designed as temporary works before excavation "
     "starts; edge protection, barriers and signage installed as the excavation "
     "deepens; spoil and plant kept back from the edge; access by fixed ladders "
     "in protected bays; daily inspection by a competent person after rain.",
     "IS 3764"),
    ("S-02", "Rock breaking",
     "Flying fragments; noise; hand-arm and whole-body vibration; damage to "
     "adjacent structures.",
     "Hydraulic breaking only, no blasting; exclusion zone around the rig; eye "
     "and hearing protection mandatory; vibration exposure monitored; a "
     "minimum 10 m separation from the sentry post founding level maintained.",
     "IS 3764; IS 5121 for safety in erection — " + MES_CAVEAT),
    ("S-03", "Working in the excavation",
     "Water accumulation; oxygen deficiency in a deep sump; entrapment.",
     "Continuous dewatering with standby; the sump pit at (-)8.100 is treated as "
     "a CONFINED SPACE with permit, gas testing, ventilation, a standby person "
     "and rescue arrangements.", "IS 3764; permit-to-work system"),
    ("S-04", "Reinforcement handling and fixing",
     "Cuts and puncture from projecting bars; manual handling injuries; crush "
     "injuries during unloading.",
     "Bar caps on all projecting verticals; mechanical unloading; gloves and "
     "safety footwear; bar-bending machines guarded; the reinforcement yard laid "
     "out so that bars are not carried over other trades.",
     "IS 7969; IS 4082 for stacking"),
    ("S-05", "Formwork and falsework",
     "Collapse of falsework under the 112 m³ pressure slab pour; falls from the "
     "deck at 3.200 m; falling components during striking.",
     "Falsework designed, checked and inspected before every pour; a striking "
     "permit signed only against the IS 456 Table 11 periods; edge protection to "
     "the deck; exclusion zone below during striking.",
     "IS 14687; IS 456 Cl. 11.3; IS 3696 (Part 1)"),
    ("S-06", "Concrete placing",
     "Cement burns and dermatitis; eye injury; pump line whip; entanglement "
     "with vibrators; night work fatigue on continuous pours.",
     "Gloves, eye protection and barrier cream; pump lines restrained and "
     "pressure-tested; a briefed pour team with defined rest breaks; lighting "
     "designed for the continuous pours.", "IS 7969"),
    ("S-07", "Work at height — headhouse, sentry post, scaffolding",
     "Falls from the scaffold and from the slab edges; falling tools and "
     "materials.",
     "Scaffold erected, altered and dismantled only by trained scaffolders and "
     "tagged before use; full guard-rail, mid-rail and toe-board; harness where "
     "edge protection cannot be provided; toe-boards and debris netting.",
     "IS 3696 (Part 1) and (Part 2); IS 4014 (Part 2)"),
    ("S-08", "SENTRY POST — brick masonry",
     "Falls from the masonry scaffold at first-storey level; collapse of a "
     "freshly built panel; manual handling of bricks and mortar; silica dust "
     "from cutting; eye injury from mortar splash and from chasing.",
     "Independent tied scaffold with a proper working platform, never a "
     "trestle on a slab edge; no more than 1 m of lift above adjacent work in a "
     "day, and temporary propping of a free-standing panel; mechanical hoisting "
     "of bricks above ground level rather than throwing; wet cutting or on-tool "
     "extraction and RPE for dust; eye protection for laying, cutting and "
     "chasing; the top course wedged only from a proper platform.",
     "IS 2212 for the work itself; IS 3696 (Part 1); IS 7969"),
    ("S-09", "Lifting operations",
     "Load failure during the lift of the blast door leaves, the filter trains, "
     "the EMP enclosure and the spiral stair.",
     "Lift plan for every significant lift; certified crane, operator and "
     "tackle; exclusion zone; no lifting over occupied areas; wind limit set "
     "for the crane.", "IS 3696 (Part 1); " + MES_CAVEAT),
    ("S-10", "Confined space — sump, escape shafts, ducts",
     "Oxygen deficiency; toxic atmosphere; entrapment in a 1400 dia shaft.",
     "Permit to work, gas testing before and during entry, forced ventilation, "
     "harness and retrieval line, standby person, and a rehearsed rescue plan. "
     "The 1400 dia escape shafts are entered only under permit.",
     "Permit-to-work system; " + MES_CAVEAT),
    ("S-11", "Electrical works",
     "Electric shock; arc flash; working live.",
     "All work dead unless a live-working permit is issued; lock-off and tag; "
     "residual current protection on all site supplies; only competent "
     "electricians; the generator changeover proved before energisation.",
     "IS 732; IS 5216 (Part 1); IS 3043"),
    ("S-12", "Plant movement and haulage",
     "Struck by excavator, tipper or roller; reversing incidents; interaction "
     "with pedestrians on a constrained site.",
     "Segregated pedestrian routes; banksman for all reversing; reversing "
     "alarms and cameras; a one-way haul route; speed limit; daily plant "
     "inspection.", "IS 7969; " + MES_CAVEAT),
    ("S-13", "Waterproofing and coatings",
     "Solvent vapour in the confined internal envelope; fire; skin and "
     "respiratory sensitisation.",
     "Forced ventilation during application in the closed envelope; no hot work "
     "adjacent; appropriate RPE and gloves; material safety data sheets held on "
     "site for every product; a fire watch where hot-applied systems are used.",
     "Product safety data; " + MES_CAVEAT),
    ("S-14", "Backfill and cover placement",
     "Plant overturning on the berm slope; crushing between plant and the "
     "structure; damage to the tanking membrane by plant tracking.",
     "Compaction plant kept off the membrane until the 100 protection screed is "
     "cured; slope gradients controlled; banksman during placement adjacent to "
     "the structure.", "IS 7969"),
    ("S-15", "Site-wide",
     "General site hazards; emergency in a deep excavation or a confined space.",
     "Site induction for every person; PPE as a minimum standard — helmet, "
     "safety footwear, high-visibility clothing, eye protection; first-aid post "
     "and trained first-aiders; documented emergency plan with rescue from "
     "height and from confined space; emergency contact list and assembly point; "
     "weekly safety walk and monthly safety committee.",
     "IS 13416 (Parts 1 to 5); CPWD Safety Code; " + MES_CAVEAT),
]

# ===========================================================================
# 6  RISK REGISTER
# ===========================================================================
# (ref, category, risk, L, I, response, owner)
RISKS = [
    ("R-01", "Ground",
     "Groundwater is higher than the ASSUMED (-)2.000. Water is nearly "
     "two-thirds of the 15.41 kPa/m lateral gradient, so the walls, the "
     "flotation check and the dewatering all move.",
     "M", "H",
     "Monsoon monitoring (A1080) is deliberately on the critical path and must "
     "close before the excavation support is designed. If the level is higher, "
     "the design is referred back before excavation, not after.",
     "Project Manager / Designer"),
    ("R-02", "Ground",
     "Red-bole or vesicular seams found under the mat. A single seam produces "
     "the differential-support case that sizes the mat.",
     "H", "H",
     "Confirmatory boreholes before excavation; every seam exposed at formation "
     "is over-excavated and replaced with M15; formation approval is a hold "
     "point with a seam map. Provisional quantity carried for replacement "
     "concrete.", "Site Engineer (Civil)"),
    ("R-03", "Ground",
     "Rock excavation quantity exceeds the estimate because rockhead is "
     "shallower than the mean assumed.",
     "M", "M",
     "The BOQ gives the quantity at both bounds — 944 to 1043 m³ — so the range "
     "is priced, not discovered. Roughly one extra day on the excavation.",
     "Planning Engineer"),
    ("R-04", "Procurement",
     "Blast door FRAMES arrive late. The frames must be welded into the W6 and "
     "W7 cages before those walls are poured, so a late frame stops the wall and "
     "the whole downstream structure.",
     "M", "H",
     "Ordered on day one with a 75-day lead time and 19 days of float; "
     "manufacturing progress reported monthly; the frame is a separate delivery "
     "from the leaf so it is not delayed by leaf testing. This is the single "
     "largest procurement risk on the job.", "Project Manager"),
    ("R-05", "Procurement",
     "CBRN filter trains, blast valves or the EMP enclosure arrive late.",
     "M", "M",
     "All ordered at mobilisation; each carries over 100 days of float; the "
     "installation activities sit after the structure is complete so a slip is "
     "absorbed rather than propagated.", "Project Manager"),
    ("R-06", "Design",
     "Conflict C21 — the CBRN filter duty is stated as 2 x 250 m³/h in master "
     "A.3 and as 300 m³/h in nine places on sheet S-06, and 250 fails S-06's own "
     "264 m³/h criterion. UNRESOLVED.",
     "H", "M",
     "Must be ruled on BEFORE the filter trains are ordered — the enquiry "
     "activity is programmed before order placement for exactly this reason. "
     "Escalated to the designer at mobilisation.", "Designer"),
    ("R-07", "Design",
     "Conflict C16 — the roof/platform junction, 250 against 500. UNRESOLVED in "
     "the master and not resolved by this package.",
     "M", "M",
     "Affects the covered entry stairwell roof, which carries float. Ruling "
     "required before A5105. Raised in the verification register.", "Designer"),
    ("R-08", "Design",
     "No electrical design package exists. The scope is confirmed but no "
     "circuit, cable, luminaire, distribution board or earth-electrode schedule "
     "does.",
     "H", "H",
     "Every electrical quantity is declared 'to be verified from final "
     "measurement'. The electrical design must be issued before A11025; the "
     "programme allows for it but cannot absorb an indefinite delay. Raised at "
     "mobilisation as the largest single information gap.", "Designer"),
    ("R-09", "Design",
     "SENTRY POST BRICK MASONRY (SP-B1) — no lintel design exists, no wall tie "
     "detail exists, and the seismic weight of the frame changes when RC infill "
     "becomes brickwork.",
     "H", "M",
     "Lintel and tie design requested before A8135; the seismic re-check is "
     "referred to the structural discipline. The change reduces the infill line "
     "load from 13.000 to about 9.9 kN/m, which points the existing V_b = 73.18 "
     "kN in the conservative direction — but that is a direction, not a "
     "verification.", "Designer / Structural Consultant"),
    ("R-10", "Design",
     "The Rev F panels are described as BALLISTIC infill. Brick masonry does "
     "not give the same ballistic protection.",
     "H", "M",
     "Recorded as a consequence of the instructed change so that the decision is "
     "visible. If ballistic performance is required it must be reinstated by "
     "another means; this package does not assume it has been.",
     "Project Manager / Client"),
    ("R-11", "Design",
     "No site plan or ground model exists. The berm volume, access route, "
     "hardstanding, several drainage runs and the soakaway positions cannot be "
     "determined.",
     "H", "M",
     "All affected items carried as 'to be verified from final measurement'. A "
     "site plan is requested at mobilisation; the external works sit at the end "
     "of the programme, which buys time but not an unlimited amount.",
     "Designer"),
    ("R-12", "Construction",
     "The 112 m³ continuous pressure slab pour cannot be completed without a "
     "cold joint — plant breakdown, supply interruption or weather.",
     "M", "H",
     "Standby pump and standby transit mixers arranged; the pour is planned as "
     "a single shift with defined fallback joint positions agreed with the "
     "designer IN ADVANCE, complete with waterstop and EMP strap details, so "
     "that an unplanned stop does not become an unplanned detail.",
     "Site Engineer (Civil)"),
    ("R-13", "Construction",
     "Reinforcement congestion at 150 spacing both curtains prevents proper "
     "compaction, particularly at the haunches, trimmer bands and blast door "
     "jambs.",
     "M", "H",
     "The 150 spacing is an EMP requirement and must NOT be relaxed on site. "
     "Mock-up of the most congested zone before the pour; mix designed for "
     "workability at 0.45 w/c; small-diameter vibrators and a rehearsed placing "
     "sequence.", "Site Engineer (Civil) / QA/QC Engineer"),
    ("R-14", "Construction",
     "Damage to the external tanking membrane during backfilling.",
     "M", "H",
     "Protection board or screed applied and inspected before any backfill; a "
     "hold point at the vertical tanking specifically because it can never be "
     "seen again; compaction plant kept off the membrane until the protection "
     "screed has cured.", "QA/QC Engineer"),
    ("R-15", "Construction",
     "SENTRY POST masonry quality — plumb, joint filling and the interface with "
     "the frame.",
     "M", "M",
     "Bricks soaked before laying; gauge boxes for mortar; hold point on line, "
     "level, plumb and joint thickness at each storey; the top course wedged "
     "only after initial shrinkage so the panel does not attract frame load.",
     "QA/QC Engineer"),
    ("R-16", "Materials",
     "Brick supply — availability of class 10 modular bricks to IS 1077 of "
     "consistent size and strength.",
     "M", "L",
     "Source approved and tested BEFORE order (A1176 precedes A8130); the whole "
     "requirement is only about 6 400 bricks, so a single approved batch covers "
     "the job. Changing source mid-job requires retesting.", "Storekeeper / QA/QC"),
    ("R-17", "Materials",
     "Cement or reinforcement supply interruption during a continuous pour "
     "period.",
     "M", "M",
     "Reinforcement ordered at 77.3 t including wastage with mill certificates; "
     "cement stocked to cover the largest pour plus a margin; stacking to "
     "IS 4082 to prevent deterioration.", "Storekeeper"),
    ("R-18", "Weather",
     "Monsoon — Pune, June to September. Deep excavation, tanking and cover "
     "placement are all weather sensitive.",
     "H", "M",
     "Sequenced so that the deep excavation (Dec–Jan) and the external tanking "
     "are out of the monsoon; surface water cut-off drains installed before "
     "excavation; productivity allowances inside the affected durations rather "
     "than an artificial non-working calendar.", "Planning Engineer"),
    ("R-19", "Programme",
     "Festival holidays are not in the calendar because their dates move.",
     "H", "L",
     "A 10-working-day contingency activity (A14098) sits before handover for "
     "exactly this purpose. It is stated, not hidden inside durations.",
     "Planning Engineer"),
    ("R-20", "Programme",
     "The 14-day prop period on the pressure slab is questioned on site and "
     "props are struck early.",
     "L", "H",
     "IS 456 Table 11 is explicit for a slab spanning over 4.5 m; this one "
     "spans 5.000 m clear. Striking requires a signed permit. The 19 days are "
     "in the baseline and are not available for compression.",
     "Site Engineer (Civil)"),
    ("R-21", "Quality",
     "Percolation test fails — likely on basalt — and the soak pits cannot "
     "work. SK-01 is already 2.3 % short of its own stated requirement "
     "(conflict C19, OPEN).",
     "H", "M",
     "The percolation test is programmed early (A1085) and is a hold point "
     "before the soak pits are built. If it fails, an alternative disposal "
     "route is a design decision, not a site one, and the programme flags it "
     "early enough to be taken.", "Designer"),
    ("R-22", "Testing",
     "EMP shielding effectiveness survey fails to reach 80 dB.",
     "M", "H",
     "The rebar cage alone gives 0 dB at 1 GHz — the master says so. The answer "
     "is the welded steel Zone 2 room plus disciplined penetration protection "
     "and joint straps, all of which are inspected as they are built rather "
     "than tested for the first time at the end.",
     "Specialist subcontractor / QA/QC"),
    ("R-23", "Testing",
     "Gas-tightness and overpressure test fails.",
     "M", "H",
     "Every penetration through the envelope is recorded and sealed as built; "
     "the blast door seals are proved before the envelope test; the test is "
     "programmed with rectification time and float ahead of handover.",
     "Site Engineer (Services)"),
    ("R-24", "Interface",
     "Damage to the completed sentry post by main-works traffic during the "
     "remaining eight months of the programme.",
     "M", "L",
     "The sentry post carries 118 days of float and is deliberately started "
     "only after the rock breaking finishes, which shortens its exposure. Its "
     "surround and apron are built at the end with the external works.",
     "Site Engineer (Civil)"),
    ("R-25", "Access",
     "Constrained site access on an operational military installation; "
     "restricted working hours or short-notice closures.",
     "M", "M",
     "Access control established first; deliveries booked; the programme uses a "
     "six-day week which leaves Sunday available for recovery without overtime "
     "premium on the critical path.", "Project Manager"),
]

# ===========================================================================
# 7  PROCUREMENT
# ===========================================================================
# (ref, package, key requirement, lead activity, needed by, note)
PROCUREMENT = [
    ("P-01", "Blast doors 1 and 2 — leaves and cast-in frames",
     "1200 x 2100, 7 bar, gas-tight, rebound rated. Vendor item; master F.1 "
     "records the leaf, frame and anchorage as NOT AVAILABLE.",
     "A1110 / A1115", "Frames at A3105 (walls W6/W7); leaves at A5135",
     "THE critical procurement. Frames are a separate, earlier delivery than "
     "the leaves so that the wall pour is not held by leaf testing."),
    ("P-02", "CBRN filter trains AHU-1 and AHU-2",
     "300 m³/h each, true N+1. Louvre, blast valve, G4/F7 pre-filter, EN 1822 "
     "H14 HEPA, ASZM-TEDA carbon, fan with electric drive AND hand crank.",
     "A1130", "A9040",
     "Conflict C21 (250 vs 300 m³/h) MUST be ruled on before the order is "
     "placed. Fan static pressure is not derivable — select on DIRTY filter "
     "figures, not clean."),
    ("P-03", "Blast valves, 5 No., and sleeves",
     "Sizes and sleeve details are on sheet S-06 and are NOT in master Part B.",
     "A1140", "A9015 (sleeves cast in) / A9035",
     "Sleeves are needed at the wall and slab pours, well before the valves."),
    ("P-04", "EMP Zone 2 shielded enclosure",
     "Welded steel room in bay 3; 80 dB over 10 kHz to 1 GHz; effectiveness "
     "verified to IEEE Std 299.",
     "A1150", "A11030",
     "Specialist. The reinforcement cage gives 0 dB at 1 GHz, so this is the "
     "whole EMP answer, not a supplement to it."),
    ("P-05", "Generator, 15 kVA", "Bay 8 grey zone; 2600 m³/h combustion and "
     "cooling air through BV-4 and BV-5; heat rejection into bay 8 not stated.",
     "A1160", "A9050", "Delivered before the shafts are closed."),
    ("P-06", "Armoured vision panels, 8 No.",
     "1200 wide, first storey of the sentry post. Specification does not exist "
     "in the project.",
     "A1165", "A8195",
     "Specification must be issued before the enquiry can be meaningful."),
    ("P-07", "Submersible pumps and drainage plant",
     "PU-01/PU-02 1.5 L/s duty and standby with auto-alternation; PU-03 hand "
     "pump; PU-04/PU-05 2 L/s for the stairwell sump.",
     "A1170", "A10020 / A10035",
     "The hand pump is the third line of defence and is independent of power — "
     "it is not an optional extra."),
    ("P-08", "Reinforcement, Fe500D and Fe500",
     "77.3 t including 5 % wastage: 70.46 t for the shelter and entry "
     "structures, 1.22 t for the burster slab, 1.97 t for the sentry post. Mill "
     "certificates required.",
     "A1172", "A3040 (mat, first fixing)",
     "Cut and bend to the fabricator's approved bar bending schedule; bend "
     "deductions to BS 8666 Table 3 are the fabricator's."),
    ("P-09", "Waterproofing system",
     "Continuous external tanking, protection layer, integral crystalline "
     "admixture, internal wet-area tanking, waterstops and EMP straps. FN1 "
     "leaves the product deliberately open — it specifies performance.",
     "A1174", "A3020 (horizontal tanking under the mat)",
     "Needed EARLY: the horizontal tanking is the first thing that happens "
     "after the blinding."),
    ("P-10", "SENTRY POST — modular bricks to IS 1077",
     "Class designation 10, 190 x 90 x 90, about 6 400 No. including 5 % "
     "breakage. Sampled to IS 5454 and tested to IS 3495 before order.",
     "A1176", "A8135",
     "DESIGN CHANGE SP-B1. Source approved once and not changed without "
     "retesting. A single approved batch covers the whole requirement."),
    ("P-11", "Cement",
     "About 194 t (3 900 bags): OPC 43 grade to IS 269 or PPC to IS 1489 "
     "(Part 1). M35 requires at least 340 kg/m³ and w/c not more than 0.45.",
     "With A1050", "A3010 onward",
     "Stacked to IS 4082. Quantity is a LOWER BOUND — the trial mix to IS 10262 "
     "fixes the real content."),
    ("P-12", "Aggregate, coarse and fine",
     "About 829 t to IS 383, tested to IS 2386. Masonry sand to IS 2116; "
     "plaster sand to IS 1542.",
     "With A1050", "A3010 onward", "Source-tested before first use."),
    ("P-13", "Formwork and falsework",
     "About 1 058 m² of contact area; 104 m² of deck at 3.200 m height with "
     "props to remain 14 days.",
     "With A1060", "A3060 onward",
     "Falsework designed and checked as temporary works to IS 14687."),
    ("P-14", "Electrical materials and equipment",
     "Cables, distribution board, luminaires, emergency lighting, earthing "
     "conductors and electrodes, EMP penetration protection.",
     "Not yet possible", "A11025 onward",
     "*** NO ELECTRICAL DESIGN PACKAGE EXISTS. Quantities are 'to be verified "
     "from final measurement' and no enquiry can be issued until the design is "
     "produced. ***"),
    ("P-15", "Internal finishes",
     "Sealed power-floated and seamless coved wet-area floor finishes, coved "
     "skirtings, sealed washable wall and soffit coatings, doors and "
     "ironmongery.",
     "After FN1 product selection", "A12020 onward",
     "FN1 specifies PERFORMANCE, not products. Each product must be approved "
     "against its stated requirement before order."),
    ("P-16", "Drainage materials",
     "DN100 drains and DN50 rising mains, gullies, chambers, gratings, the "
     "gas-tight NRV, blast check valve and deep-seal traps, septic tank and "
     "soak pit fill.",
     "With A1170", "A10010 onward",
     "Several pipe lengths are NOT DETERMINABLE without a site plan."),
]

# ===========================================================================
# 8  CODES, STANDARDS AND SPECIFICATIONS
# ===========================================================================
# (group, reference, title/scope, used for, class)
CODES = [
    # --- structural design, carried from master Part G (already verified there)
    ("Structural design", "IS 456:2000",
     "Plain and reinforced concrete — code of practice",
     "All RC design and construction; Cl. 11.3 Table 11 formwork striking; "
     "Cl. 13.4 construction joints; Cl. 13.5 curing; Cl. 15 and 16 acceptance; "
     "Cl. 26.2 development and laps; Cl. 26.4.2 and Table 16 cover; Table 5 "
     "exposure, minimum cement and w/c.", "[C] master Part G"),
    ("Structural design", "IS 1786:2008",
     "High strength deformed steel bars and wires for concrete reinforcement",
     "Fe500D for the shelter, Fe500 for the sentry post.", "[C] master Part G"),
    ("Structural design", "IS 13920:2016",
     "Ductile design and detailing of reinforced concrete structures subjected "
     "to seismic forces", "Sentry post frame detailing, Zone III.",
     "[C] master Part G"),
    ("Structural design", "IS 1893 (Part 1):2016",
     "Criteria for earthquake resistant design of structures — general "
     "provisions and buildings", "Seismic design of the sentry post and the box.",
     "[C] master Part G"),
    ("Structural design", "IS 875 (Parts 1, 2, 3, 5)",
     "Code of practice for design loads (other than earthquake)",
     "Dead loads and unit weights; imposed loads; wind on the sentry post; load "
     "combinations.", "[C] master Part G"),
    ("Structural design", "IS 3370 (Parts 1 and 2):2021",
     "Concrete structures for the storage of liquids",
     "Crack width limit 0.2 mm and surface-zone steel.", "[C] master Part G"),
    ("Structural design", "IS 4991:1968",
     "Criteria for blast resistant design of structures for explosions above "
     "ground",
     "Blast loading rules and dynamic material strengths ONLY. Cl. 1.1 "
     "EXPLICITLY EXCLUDES NUCLEAR and that exclusion is quoted in every "
     "deliverable. Cl. 10.3.1.1 — NO dynamic increase on shear.",
     "[C] master Part G"),
    ("Structural design", "SP 34:1987",
     "Handbook on concrete reinforcement and detailing",
     "Shape codes; Cl. 5.5 opening-corner detailing.", "[C] master Part G"),
    ("Structural design", "SP 16:1980", "Design aids for reinforced concrete",
     "Column interaction charts, cross-checked against first-principles "
     "calculation.", "[C] master Part G"),
    ("Structural design", "BS 8666", "Scheduling, dimensioning, bending and "
     "cutting of steel reinforcement for concrete",
     "Bar shape codes and bend deductions in all bar bending schedules, used "
     "alongside SP 34.", "[C] master Part G"),
    ("Structural design", "IS 1904:1986",
     "Design and construction of foundations in soils — general requirements",
     "Presumptive bearing capacity, Table 1, hard rock 3240 kPa.",
     "[C] master Part G"),
    ("Structural design", "IS 12070:1987",
     "Design and construction of shallow foundations on rocks",
     "Settlement on sound basalt.", "[C] master Part G"),
    # --- construction, materials and workmanship
    ("Materials", "IS 269:2015", "Ordinary Portland Cement — specification",
     "Cement for all concrete, mortar and plaster.", "[C]"),
    ("Materials", "IS 1489 (Part 1):1991",
     "Portland pozzolana cement — fly ash based", "Alternative binder if approved.",
     "[C]"),
    ("Materials", "IS 383:2016",
     "Coarse and fine aggregate for concrete — specification",
     "All concrete aggregate.", "[C]"),
    ("Materials", "IS 2386 (Parts 1 to 8):1963",
     "Methods of test for aggregates for concrete", "Aggregate acceptance testing.",
     "[C]"),
    ("Materials", "IS 2116:1980", "Sand for masonry mortars — specification",
     "SENTRY POST brick masonry mortar.", "[C]"),
    ("Materials", "IS 1542:1992", "Sand for plaster — specification",
     "Sentry post internal and external plaster.", "[C]"),
    ("Materials", "IS 2645:2003",
     "Integral waterproofing compounds for cement mortar and concrete",
     "The integral crystalline admixture required by master A.5.", "[C]"),
    ("Materials", "IS 4031", "Methods of physical tests for hydraulic cement",
     "Cement acceptance testing. Multi-part standard — cite the relevant part "
     "for each test.", "[C]"),
    ("Construction", "IS 10262:2019",
     "Concrete mix proportioning — guidelines",
     "Trial mix design for M35 and M30.", "[C]"),
    ("Construction", "IS 1199", "Fresh concrete — methods of sampling, testing "
     "and analysis", "Slump and sampling at the pour. Multi-part; confirm the "
     "current part and edition before citing a clause.", "[C] / edition to confirm"),
    ("Construction", "IS 516", "Hardened concrete — methods of test",
     "Cube compressive strength. Confirm the current part and edition before "
     "citing a clause.", "[C] / edition to confirm"),
    ("Construction", "IS 13311 (Parts 1 and 2):1992",
     "Non-destructive testing of concrete — ultrasonic pulse velocity; rebound "
     "hammer", "NDT of the pressure slab and protective walls.", "[C]"),
    ("Construction", "IS 14687:1999",
     "Falsework for concrete structures — guidelines",
     "Falsework to the pressure slab soffit at 3.200 m.", "[C]"),
    ("Construction", "IS 9077:1979",
     "Corrosion protection of steel reinforcement in RB and RCC construction",
     "Reinforcement protection in a very severe exposure environment.", "[C]"),
    ("Construction", "IS 2720 (Part 8):1983",
     "Methods of test for soils — determination of water content–dry density "
     "relation using heavy compaction",
     "MDD for the backfill and the engineered cover.", "[C]"),
    ("Construction", "IS 2720 (Part 28):1974",
     "Methods of test for soils — determination of dry density of soils "
     "in place by the sand replacement method",
     "Field density testing of every compacted layer.", "[C]"),
    # --- masonry — the design change
    ("SENTRY POST masonry", "IS 1077:1992",
     "Common burnt clay building bricks — specification",
     "Class designation 10 modular bricks, 190 x 90 x 90, for the sentry post "
     "walls. DESIGN CHANGE SP-B1.", "[C]"),
    ("SENTRY POST masonry", "IS 2212:1991", "Code of practice for brickwork",
     "Laying, bond, joint filling, soaking, lift heights and curing.", "[C]"),
    ("SENTRY POST masonry", "IS 1905:1987",
     "Code of practice for structural use of unreinforced masonry",
     "Infill panel proportions, slenderness and the frame interface.", "[C]"),
    ("SENTRY POST masonry", "IS 2250:1981",
     "Code of practice for preparation and use of masonry mortars",
     "CM 1:6 preparation, gauge boxes, working time.", "[C]"),
    ("SENTRY POST masonry", "IS 3495 (Parts 1 to 4):1992",
     "Methods of tests of burnt clay building bricks — compressive strength, "
     "water absorption, efflorescence, warpage",
     "Brick acceptance testing before order and on delivery.", "[C]"),
    ("SENTRY POST masonry", "IS 5454:1978",
     "Method for sampling of clay building bricks",
     "Sample size and selection for the IS 3495 tests.", "[C]"),
    ("SENTRY POST masonry", "IS 1661:1972",
     "Code of practice for application of cement and cement-lime plaster "
     "finishes", "Sentry post internal and external plaster.", "[C]"),
    ("SENTRY POST masonry", "IS 2395 (Part 1):1994",
     "Code of practice for painting concrete, masonry and plaster surfaces",
     "Sentry post painting.", "[C]"),
    ("SENTRY POST masonry", "IS 2571:1970",
     "Code of practice for laying in-situ cement concrete flooring",
     "Sentry post flooring.", "[C]"),
    # --- waterproofing and drainage
    ("Waterproofing", "IS 3067:1988",
     "Code of practice for general design details and preparatory work for "
     "damp-proofing and waterproofing of buildings",
     "Substrate preparation, fillets, terminations for WP-01.", "[C]"),
    ("Waterproofing", "IS 6494:1988",
     "Code of practice for waterproofing of underground water reservoirs and "
     "swimming pools",
     "Principles applied to the buried envelope and the sump pit.", "[C]"),
    ("Drainage", "IS 2470 (Part 1):1985",
     "Code of practice for installation of septic tanks — design criteria and "
     "construction",
     "Septic tank ST-01; Cl. 6.2, 6.3, 6.5, 6.6, 6.9 and Table 1.",
     "[C] master Part G"),
    ("Drainage", "IS 2470 (Part 2):1985",
     "Code of practice for installation of septic tanks — secondary treatment "
     "and disposal",
     "Cl. 4 — the PERCOLATION TEST IS MANDATORY before the soak pits are built.",
     "[C] master Part G"),
    # --- services
    ("Electrical", "IS 732:2019",
     "Code of practice for electrical wiring installations",
     "Wiring, distribution and testing.", "[C]"),
    ("Electrical", "IS 3043:2018", "Code of practice for earthing",
     "Earthing installation and the 5 ohm target.", "[C] master Part G"),
    ("Electrical", "IEEE 142", "Recommended practice for grounding of "
     "industrial and commercial power systems",
     "Earthing target, cited alongside IS 3043.", "[C] master Part G"),
    ("Electrical", "IS 694:2010",
     "PVC insulated cables for working voltages up to and including 1100 V",
     "Final circuit cabling.", "[C]"),
    ("Electrical", "IS 1554 (Part 1):1988",
     "PVC insulated (heavy duty) electric cables for working voltages up to "
     "and including 1100 V", "Sub-mains and generator cabling.", "[C]"),
    ("Electrical", "IS 3646 (Part 1):1992",
     "Code of practice for interior illumination",
     "Internal lighting levels.", "[C]"),
    ("Protective", "MIL-STD-188-125-1",
     "High-altitude electromagnetic pulse protection for ground-based C4I "
     "facilities",
     "EMP requirement: 80 dB over 10 kHz to 1 GHz; §5.4 access, §5.5 waveguide "
     "below cutoff, §5.7.2.1 power PCI, §5.7.4.1 fibre, §5.7.6 RF.",
     "[C] master Part G"),
    ("Protective", "IEEE Std 299",
     "Standard method for measuring the effectiveness of electromagnetic "
     "shielding enclosures", "The shielding effectiveness survey at handover.",
     "[C] master Part G"),
    ("Protective", "EN 1822", "High efficiency air filters (EPA, HEPA and ULPA)",
     "H14 classification of the CBRN filter train HEPA stage.",
     "[C] master Part G"),
    ("Protective", "FEMA 453", "Safe rooms and shelters",
     "Shelter ventilation criteria and carbon adsorber performance.",
     "[C] master Part G"),
    ("Protective", "UFC 3-340-02",
     "Structures to resist the effects of accidental explosions",
     "Cited AS US criteria: §4-27 opening trimmers, §4-30 direct shear.",
     "[C] master Part G"),
    # --- safety
    ("Safety", "IS 3764:1992", "Code of safety for excavation work",
     "The 6.8 m deep excavation and its edge protection.", "[C]"),
    ("Safety", "IS 3696 (Part 1):1987", "Safety code for scaffolds and ladders "
     "— scaffolds", "Masonry, plaster and slab-edge scaffolding.", "[C]"),
    ("Safety", "IS 3696 (Part 2):1991", "Safety code for scaffolds and ladders "
     "— ladders", "Access into the excavation and to working platforms.", "[C]"),
    ("Safety", "IS 4014 (Part 2):1967",
     "Code of practice for steel tubular scaffolding — safety regulations",
     "Erection, alteration and dismantling of tubular scaffold.", "[C]"),
    ("Safety", "IS 7969:1975",
     "Safety code for handling and storage of building materials",
     "Reinforcement, brick, cement and aggregate handling.", "[C]"),
    ("Safety", "IS 4082:1996",
     "Recommendations on stacking and storage of construction materials and "
     "components at site", "Site stacking discipline.", "[C]"),
    ("Safety", "IS 13416 (Parts 1 to 5)",
     "Recommendations for preventive measures against hazards at work places",
     "General site safety, falling material, fire and excavation.", "[C]"),
    ("Safety", "IS 5216 (Part 1):1982",
     "Guide for safety procedures and practices in electrical work",
     "Electrical safety and permit-to-work.", "[C]"),
    ("Life safety", "NBC 2016 Part 4", "Fire and life safety",
     "Stair geometry, 1100 guarding and means of escape.", "[C] master Part G"),
    # --- measurement and government specifications
    ("Measurement", "IS 1200 (Part 1):1992",
     "Methods of measurement of building and civil engineering works — "
     "earthwork", "Measurement of excavation, filling and disposal.", "[C]"),
    ("Measurement", "IS 1200 (Part 2):1974",
     "Methods of measurement — concrete works", "Measurement of all concrete.",
     "[C]"),
    ("Measurement", "IS 1200 (Part 3):1976",
     "Methods of measurement — brickwork",
     "SENTRY POST brick masonry, measured at its actual 190 thickness.", "[C]"),
    ("Measurement", "IS 1200 (Part 5):1982",
     "Methods of measurement — formwork", "Formwork contact area.", "[C]"),
    ("Measurement", "IS 1200 (Part 12):1976",
     "Methods of measurement — plastering and pointing",
     "Sentry post plaster.", "[C]"),
    ("Measurement", "IS 1200 (Part 13):1994",
     "Methods of measurement — whitewashing, colour washing, distempering and "
     "painting of buildings", "Painting.", "[C] / edition to confirm"),
    ("Government", "MES Standard Schedule of Rates (SSR), Part I — Rates and "
     "Part II — Specifications",
     "The Military Engineer Services schedule governing measurement, "
     "specification and rates for Service works.",
     "Measurement conventions, specification clauses and rates for every item "
     "of this BOQ. NO ITEM NUMBER IS QUOTED because none could be verified "
     "from the material available.", "[N] — " + MES_CAVEAT),
    ("Government", "Defence Works Procedure (DWP)",
     "The procedure governing the sanction, execution and acceptance of "
     "defence works.",
     "Approvals, sanction stages, acceptance of works and handover to the "
     "user Service.", "[N] — edition and clause " + MES_CAVEAT),
    ("Government", "MES Regulations (MESR)",
     "Standing regulations of the Military Engineer Services.",
     "Contract administration, measurement, and the Engineer's authority.",
     "[N] — edition and clause " + MES_CAVEAT),
    ("Government", "CPWD Specifications 2019, Volumes 1 and 2",
     "Central Public Works Department specifications for building works.",
     "Workmanship clauses for earthwork, concrete, brickwork, plaster, "
     "flooring and painting where the MES SSR defers to them.",
     "[C] document exists / [N] clause numbers — " + MES_CAVEAT),
    ("Government", "CPWD Works Manual",
     "Central Public Works Department procedure for the execution of works.",
     "Quality control, measurement books and inspection procedure.",
     "[C] document exists / [N] clause numbers — " + MES_CAVEAT),
    ("Government", "Delhi Schedule of Rates (DSR)",
     "CPWD schedule of rates used as a comparator where an MES SSR item is "
     "not available.",
     "Rate comparison only. NO ITEM NUMBER IS QUOTED.",
     "[N] — " + MES_CAVEAT),
]

# ===========================================================================
# 9  PROGRESS MONITORING
# ===========================================================================
PROGRESS = {
    "baseline": [
        "The baseline is the WM1 programme: 279 activities, 326 working days, "
        "2 November 2026 to 20 November 2027, with 18 milestones and 75 "
        "activities at zero total float.",
        "The baseline is frozen at the start of construction. It is re-baselined "
        "only on a formal instruction — a change of scope, an extension of time "
        "or a design change — and every re-baseline keeps the previous version. "
        "A programme that is quietly re-drawn each month measures nothing.",
        "Progress is reported against the baseline, never against the last "
        "revision of the programme.",
    ],
    "measurement": [
        "Physical progress is measured by QUANTITY, not by opinion. Each "
        "activity is linked to a BOQ item, so 'wall reinforcement 60 % complete' "
        "means 14.8 of 24.7 tonnes fixed and can be verified from the "
        "measurement book.",
        "Earned value is computed on quantity: earned = quantity placed x BOQ "
        "rate. Schedule performance index and cost performance index are "
        "reported monthly for the project and for each of the three reporting "
        "streams.",
        "Milestones are binary. A milestone is either achieved on its date or it "
        "is not; there is no percentage against a milestone.",
    ],
    "streams": [
        ("Stream A — Underground shelter",
         "WBS 2 to 7 and 12. Excavation, substructure, pressure slab, entry "
         "structures, waterproofing, cover and internal finishes.",
         "Measured on m³ of excavation and concrete, tonnes of reinforcement, "
         "m² of formwork and tanking, and m³ of cover."),
        ("Stream B — Sentry post",
         "WBS 8. Frame, BRICK MASONRY WALLS, lintels, spiral stair, finishes "
         "and electrical.",
         "Measured on m³ of concrete, m³ and m² of brick masonry, and m² of "
         "plaster and painting. Reported separately because it is an "
         "independent structure with 118 days of float."),
        ("Stream C — Services and external works",
         "WBS 9, 10, 11 and 13. HVAC and CBRN, drainage, electrical and EMP, "
         "external works and concealment.",
         "Measured on installed lengths and items. Several quantities are 'to "
         "be verified from final measurement', so this stream is reported on "
         "activity completion until the design gaps close."),
    ],
    "cycle": [
        ("Daily", "Site diary; labour and plant returns; concrete pour cards; "
         "weather; any stoppage and its cause."),
        ("Weekly", "Progress against the three-week look-ahead; quantities "
         "placed; hold points cleared and outstanding; a short-interval "
         "programme for the coming week issued every Saturday."),
        ("Fortnightly", "Rolling three-week look-ahead reissued, showing the "
         "activities starting and finishing, the resources needed, the "
         "materials required on site and the inspections due."),
        ("Monthly", "Updated programme with actual start, actual finish and "
         "remaining duration on every activity; recalculated critical path; "
         "float erosion report; earned value for each stream and for the "
         "project; milestone status; a delay register with cause, effect and "
         "recovery proposal; the top ten risks reviewed."),
    ],
    "delay": [
        "Every delay is recorded when it happens, with its cause, the activities "
        "affected and its effect on the critical path — not reconstructed at the "
        "end of the job.",
        "Float erosion is tracked explicitly. An activity is flagged when its "
        "total float falls below ten working days, whether or not it is "
        "critical, because a chain that is quietly consuming float is the "
        "warning that arrives before a delay does.",
        "Recovery is proposed in the same report as the delay: resequencing "
        "first, then additional resource, then additional shifts. Compressing "
        "the 14-day prop period on the pressure slab is not an available "
        "recovery measure and must not be offered as one.",
    ],
    "corrective": [
        "Sentry post float — 118 days — is the natural place to absorb labour "
        "redeployment when the main works are held up, and the natural place to "
        "take labour from when the main works need to catch up.",
        "The long-lead procurement chain has no recovery available once a "
        "delivery is late. It is therefore managed by monitoring the vendor, not "
        "by planning to recover: monthly manufacturing progress reports for the "
        "blast doors, filter trains, blast valves and the EMP enclosure.",
        "Where an information gap is the cause — the electrical design, the site "
        "plan, the lintel design, conflicts C16 and C21 — the corrective action "
        "is escalation to the designer with a stated date by which the "
        "information is needed. Those dates are computed from the programme and "
        "issued at mobilisation, not requested when the activity is due to "
        "start.",
    ],
}
