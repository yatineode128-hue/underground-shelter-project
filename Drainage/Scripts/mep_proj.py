"""
mep_proj.py  --  shared constants for the DRAINAGE, HVAC and SCHEDULE OF
FINISHES packages.

ONE definition of each value.  Every entry carries its source and its evidence
class, using the master's own legend:

    [C] CONFIRMED      traceable to the master or to a Rev F / S-06 drawing
    [R] RECONSTRUCTED  computed here from confirmed values, arithmetic shown
    [A] ASSUMED        an engineering selection made by THIS package
    [U] UNRESOLVED     competing values exist, or the input does not exist
    [N] NOT AVAILABLE  no source exists anywhere in the project

SOURCE OF TRUTH, in order:
    master/MASTER_PROJECT_STATE.md  Parts A.2-A.7, B.3, B.6, E.3, F.1, G, K
    current/cad/06_Underground_Plan_Services_Sump_BlastValves.dxf   (sheet S-06)
    current/cad/1_Underground_Level_Plan.dxf        (GA plan, Rev F + M1)
    current/cad/2_Ground_Plan_Headhouse_Berm.dxf    (ground plan, Rev F + M1)
    current/cad/5_Entry_Headhouse_Stair_Section.dxf (section C-C, Rev F)
    Structural CAD/DXF/Typical_Details/R-805_Waterproofing_Structural_Interface.dxf

SENTRY POST: OUT OF SCOPE.  No sentry post constant appears in this file and no
sentry post element appears in any drawing, schedule or calculation produced by
these three packages.  Historical sentry post information elsewhere in the
project is left untouched.

MAIN STAIRCASE: FROZEN.  24R @ 170.8333 / 280, 3 flights x 8, total rise 4100.
Nothing in these packages changes it; the finishes package annotates it only.
"""

# --------------------------------------------------------------- identity
PACKAGE_DATE = "05.09.2026"
PROJECT = "UNDERGROUND CBRN-HARDENED BLAST-RESISTANT PROTECTIVE STRUCTURE"
LOCATION = "PUNE, MAHARASHTRA"
GEOM_REV = "GEOMETRY REV F + M1"
STATUS = "FOR REVIEW - NOT FOR CONSTRUCTION"

REV = dict(drainage="DR1", hvac="HV1", finishes="FN1")

# ------------------------------------------------------- geometry  [C] A.4
BOX = dict(x0=0, x1=22000, y0=0, y1=6200)          # external
INT = dict(x0=600, x1=21400, y0=600, y1=5600)      # internal clear
T_WALL, T_ROOF, T_MAT, T_PCC = 600, 900, 600, 100
H_CLEAR = 3200                                     # internal clear height

LVL = dict(grade=0.000, slab_top=-2.000, roof_soffit=-2.900, floor=-6.100,
           mat_soffit=-6.700, formation=-6.800, gwt=-2.000,
           L1=-4.7333, L2=-3.3667,
           hh_soffit=+0.400, hh_top=+0.900,
           asw_head=+2.450, asw_soffit=+2.200,
           sump_invert=-7.600, sump_base=-8.000,
           esc1_head=+0.150, esc2_head=+0.700)

# bay no, x0, x1, clear width, room number, room name        [C] A.3 + GA plan
BAYS = [(1, 600, 3500, 2900, "U-01", "EMERGENCY STORES / ESC 1"),
        (2, 3610, 5410, 1800, "U-02", "LAVATORY + MEDICAL"),
        (3, 5520, 9020, 3500, "U-03", "OPS ROOM & HAZARD PLOTTING"),
        (4, 9130, 10930, 1800, "U-04", "BERTHING - 9 BERTHS"),
        (5, 11040, 12600, 1560, "U-05", "CBRN PLANT + SUMP"),
        (6, 12800, 14800, 2000, "U-06", "DECON AIRLOCK - 3 STAGE"),
        (7, 15200, 18000, 2800, "U-07", "STAIR SHAFT"),
        (8, 18400, 21400, 3000, "U-08", "GENERATOR / SERVICES")]

IW = [("W5", 12600, 12800, 200), ("W6", 14800, 15200, 400),
      ("W7", 18000, 18400, 400)]
PARTITIONS = [(3500, 3610), (5410, 5520), (9020, 9130), (10930, 11040)]
T_PART = 110
PART_DOOR_Y = (2500, 3400)                          # 900 clear gap

# Bay 2 sub-division  [C] A.3 "Lavatory (1800x2000) + medical (1800x3000)"
LAV = dict(x0=3610, x1=5410, depth=2000)            # 1800 x 2000
MED = dict(x0=3610, x1=5410, depth=3000)            # 1800 x 3000

# Bay 6 decon airlock stages  [C] A.3 "(2000x2000, 2000x1500, 2000x1500)"
DECON_STAGES = [("S1", 2000, 2000), ("S2", 2000, 1500), ("S3", 2000, 1500)]

BLAST_DOOR = dict(w=1200, h=2100, y0=600, y1=1800)  # W6 / W7, 7 bar  [C]
ESC = [("ESC 1", 2050, 2050, +0.150), ("ESC 2", 19900, 2050, +0.700)]
ESC_CLEAR_D, ESC_COLLAR_T, ESC_COLLAR_OD = 1400, 250, 1900

VOID = dict(x0=15200, x1=18000, y0=600, y1=3760)    # opening in pressure slab
PAD = dict(x0=15200, x1=18000, y0=3760, y1=5600)    # cantilever pad

# main staircase -- FROZEN, annotated only              [C] A.4.4 / CLAUDE.md
STAIR = dict(risers=24, riser=170.8333, tread=280, flights=3, per_flight=8,
             total_rise=4100, width=1200, well=200, waist=200, headroom=2533,
             fltA=(15300, 16500), wellx=(16500, 16700), fltB=(16700, 17900),
             L1_y=(3760, 4960), L2_y=(600, 1800), arrival_y=(600, 1800),
             store_y=(4960, 5600))

HH = dict(x0=13600, x1=18400, y0=200, y1=6000,      # headhouse external
          ix0=14000, ix1=18000, iy0=600, iy1=5600,  # internal
          t_wall=400, t_roof=500, clear_h=2400, usable_m2=11.15)
HH_DOOR = dict(x0=14450, x1=15350, w=900, h=2100, wall="HW2")

ASW = dict(x0=9250, x1=16050, y0=5750, y1=7750,     # covered stairwell ext.
           ix0=9500, ix1=15800, iy0=6000, iy1=7500,
           t_wall=250, t_roof=250, t_raft=300,
           top_landing=(9500, 11000), flight=(11000, 14300),
           platform=(14300, 15800), risers=12, riser=166.6667, going=300,
           waist=250, width=1500, door=(1000, 2100),
           channel=(8950, 9250), channel_w=300)

BERM = dict(slope="1.5:1", top=+0.900, toe_run=1350, fall_at_door="1:50",
            fall_run=2000)

# ------------------------------------------------ services, confirmed [C]
# Every value below is read from sheet S-06 or from a Rev F drawing note.
SUMP = dict(l=1500, b=1500, d=1500, volume_m3=3.375,
            invert=-7.600, base=-8.000, t_wall=300, t_base=400,
            pumps=2, duty_ls=1.5, arrangement="DUTY / STANDBY AUTO-ALTERNATING",
            hand_pump=True, start=900, stop=300, alarm=1200,
            reinf="T16 @ 150 EF EW", trimmers="4-T20 EACH FACE / SIDE")
# C18: F.1 and the A.4.3 levels give base 400; S-06 text says 300.  400 HELD.

DISCHARGE_TRAIN = ["ISOLATION VALVE", "GAS-TIGHT NON-RETURN VALVE",
                   "BLAST CHECK VALVE", "DEEP-SEAL TRAP"]   # in series, [C]

DECON_TANK = dict(volume_l=1000, disposal="TANKER ONLY - NEVER TO CLEAN SUMP")
POTABLE_TANK = dict(volume_l=1000, bay=1)

SEPTIC = dict(l=1.50, b=0.75, liquid_depth=1.00, freeboard=0.300,
              overall_depth=1.30, capacity_l=1125, required_l=1050,
              users=10, q_lpcd=45, flow_lpd=450,
              detention_l=450, sludge_l=600, lb_ratio=2.0,
              compartments=2, baffle="AT 2/3 L", vent="50 COWLED, >= 2 m ABOVE GRADE")

SOAKPIT = dict(dia=2.0, effective_depth=3.5, side_area_m2=22.0,
               required_m2=22.5, absorption_lm2d=20,
               fill="40-80 mm BRICKBAT / STONE, 300 SAND AT TOP, RC COVER SLAB",
               offsets=">= 15 m FROM ANY WELL, >= 5 m FROM THE SEPTIC TANK, "
                       ">= 2 m FROM ANY BUILDING")

ASW_SUMP = dict(volume_m3=1.0, duty_ls=2.0, arrangement="DUTY + STANDBY",
                rising_main="NON-RETURN VALVE ON THE RISING MAIN",
                fill_time_h=32, discharge="OWN SOAKAWAY")

# design flows, sheet S-06 "DRAINAGE AND WASTE - DESIGN FLOWS"        [C]
# (item, flow, capacity/store, discharges to)
DESIGN_FLOWS = [
    ("Structural seepage  0.5 L/m2/day x 401 m2", "200 L/day", "sump 3375 L",
     "storm soakaway"),
    ("Condensate + washdown", "200 L/day", "= 8 days store", "storm soakaway"),
    ("Decon effluent, airlock stages 1 + 2", "on use", "1000 L tank",
     "TANKER ONLY"),
    ("Foul, peacetime, 10 users x 45 lpcd", "450 L/day", "septic 1.125 m3",
     "soak pit"),
    ("Stairwell / approach surface water", "0.10 L/s", "1.0 m3 sump",
     "own soakaway")]

SEEPAGE = dict(rate_lm2d=0.5, wetted_area_m2=401.0, flow_lpd=200.0)   # [C]/[A8]
RAIN_INTENSITY = 50.0        # mm/h  [C] drawing 5 note 1, Rev F
REV_E_PIT_AREA = 7.2         # m2    [C] drawing 5 note 1 (superseded catchment)

# ------------------------------------------------------ ventilation  [C]
VENT = dict(occupants=9, endurance_h=96,
            survival_pp=5, working_pp=15,
            survival_total=45, working_total=135,
            fema_rate="0.25 cfm/ft2", clean_zone_m2=57.8, fema_total=264,
            design_m3h=300, trains=2, redundancy="TRUE N+1",
            envelope_m2=67.8, envelope_m3=217.0,
            leak_rate="<= 0.15 vol/h at +300 Pa", leak_m3h=32.5,
            overpressure="+50 to +100 Pa",
            cascade="0 -> +10 -> +20 -> +35 -> +50 Pa",
            closed_volume_m3=185.0, co2_pp=0.02, co2_total=0.18,
            co2_limit_pct=1.0, closed_hours=9.9,
            soda_lime_kgd=20, soda_lime_48h=40,
            o2_m3d=4.5, o2_cyl="2 x 50 L AT 150 bar (15 m3)",
            purge_stage_m3=12.8, purge_changes=5, purge_m3=64,
            purge_min=13, entry_rate="4-5 PERSONS PER HOUR")

FILTER_TRAIN = [("WEATHER LOUVRE", "SAND + DEBRIS TRAP"),
                ("BLAST VALVE", "< 2 ms CLOSE, HOLDS 1.3 s"),
                ("PRE-FILTER", "G4 / F7"),
                ("HEPA", "EN 1822 H14, 99.995 % MPPS"),
                ("CARBON", "ASZM-TEDA, 300 000 mg.min/m3"),
                ("FAN", "+ HAND CRANK"),
                ("PLENUM", "+50 to +100 Pa")]

# tag, size, serves, flow m3/h, velocity, design pressure, force on disc   [C]
BLAST_VALVES = [
    ("BV-1", "DN100", "FRESH AIR TRAIN 1", 300, "10.6 m/s", "383 kPa RECESSED", "3.0 kN"),
    ("BV-2", "DN100", "FRESH AIR TRAIN 2", 300, "10.6 m/s", "383 kPa RECESSED", "3.0 kN"),
    ("BV-3", "DN100", "EXHAUST + OPRV", 300, "10.6 m/s", "383 kPa RECESSED", "3.0 kN"),
    ("BV-4", "DN350", "GENERATOR INTAKE", 2600, "7.5 m/s", "383 kPa RECESSED", "36.8 kN"),
    ("BV-5", "DN350", "GENERATOR EXHAUST", 2600, "7.5 m/s", "383 kPa RECESSED", "36.8 kN")]

SHAFTS = dict(fresh_air="600 x 600, GOOSENECK +1.500",
              generator="600 x 600",
              intake_to_entry_m=12.3, intake_min_m=10.0)

GENSET = dict(rating_kva=15, bay=8, zone="GREY", air_m3h=2600)

SERVICE_ENTRY = ("SERVICE ENTRY PLATE - THE ONLY PENETRATION OF THE ENVELOPE. "
                 "MCT FRAME WITH EMP MODULES + SLEEVED PIPES + SUMP RISING MAIN")

# ------------------------------------------------ waterproofing  [C] R-805
WP = dict(concrete="M35, w/c <= 0.45, cement >= 340 kg/m3",
          admixture="INTEGRAL CRYSTALLINE WATERPROOFING ADMIXTURE",
          tanking="TANKING MEMBRANE ON THE BLINDING, TURNED UP THE EXTERNAL "
                  "FACE AND LAPPED TO THE ROOF MEMBRANE - A CONTINUOUS TANK",
          screed="100 PROTECTION SCREED OVER THE ROOF MEMBRANE; ALSO THE FIRST "
                 "LAYER OF THE ENGINEERED COVER",
          joints="TWO WATERSTOPS AT EVERY CONSTRUCTION JOINT - R-804",
          crack="IS 3370 CRACK CONTROL 0.2 mm, 0.35 % SURFACE-ZONE STEEL OVER "
                "A 250 mm ZONE",
          cover="NO COVER IS REDUCED FOR WATERPROOFING")

COVER_BUILDUP = [("TOPSOIL / TURF", 300, 18, 5.40, "CONCEALMENT, EROSION, SHEDS RAIN"),
                 ("GRANULAR FILTER", 150, 19, 2.85, "STOPS FINES CLOGGING"),
                 ("RC BURSTER SLAB M30", 200, 25, 5.00,
                  "BREAKS UP A PENETRATING ITEM - LAID TO 1:50 CROSSFALL, BS1"),
                 ("CRUSHED BASALT RUBBLE 25-75", 500, 17, 8.50, "SCATTERS BURSTER ENERGY"),
                 ("COMPACTED FILL @ 95 % MDD", 750, 20, 15.00, "RADIATION MASS"),
                 ("PROTECTION SCREED", 100, 24, 2.40, "PROTECTS WATERPROOFING")]

# ------------------------------------------------------------ open items
OPEN_ITEMS = {
    "C16": "ROOF / PLATFORM JUNCTION - UNRESOLVED. A.4.7 says the roof over the "
           "platform becomes the 500 headhouse roof; B.6 / A.7.6 / F.2 design, "
           "load and register 250. NOT RESOLVED BY THIS PACKAGE. Rainwater "
           "falling on the junction and the position of the platform gully "
           "depend on it - see the QA/QC report.",
    "A2":  "DESIGN GWT (-)2.000 IS [ASSUMED]. Monsoon monitoring required. "
           "Governs the seepage rate the sump is sized on.",
    "A7":  "SOAK-PIT ABSORPTION 20 L/m2/day IS [ASSUMED]. A PERCOLATION TEST "
           "TO IS 2470 (Pt 2) Cl. 4 IS MANDATORY BEFORE CONSTRUCTION. Deccan "
           "basalt drains badly; if the test returns less, switch to a "
           "dispersion trench (Cl. 5) or a sealed holding tank.",
    "A8":  "STRUCTURAL SEEPAGE 0.5 L/m2/day IS [ASSUMED]. Packer permeability "
           "tests required. Sets the 8.4-day sump store.",
    "D1":  "RAINFALL INTENSITY 50 mm/h is the only intensity stated anywhere in "
           "the project (Rev F drawing 5 note 1). NO return period, duration or "
           "IDF source is recorded. VERIFY against IMD Pune data before "
           "construction.",
    "D2":  "PEACETIME FOUL DRAINAGE ROUTE FROM THE BAY 2 LAVATORY IS NOT "
           "DEFINED ANYWHERE IN THE PROJECT. S-06 records cassette toilets in "
           "protective mode and a peacetime septic tank sized for 10 users, but "
           "no connection between the two. ENGINEER TO CONFIRM.",
    "D3":  "FINAL DISCHARGE OF THE STORM SOAKAWAY AND THE SOAK PIT IS TO GROUND "
           "ON SITE. NO MUNICIPAL SEWER OR STORM CONNECTION EXISTS ANYWHERE IN "
           "THE PROJECT and no site boundary, contour or outfall level is "
           "recorded. DATA REQUIRED.",
    "M2":  "NO CODE DOCUMENT is in the workspace. Clause numbers are cited only "
           "from the verified master Part G register; codes outside that "
           "register are cited BY TITLE ONLY and flagged.",
}

# codes already in the master Part G register that these packages rely on
CODES_IN_REGISTER = [
    ("IS 456:2000", "RC design, cover, crack control"),
    ("IS 875 (Part 2):1987", "Imposed loads"),
    ("IS 1904:1986", "Presumptive bearing capacity"),
    ("IS 2470 (Part 1):1985", "Septic tank - Cl. 6.2, 6.3, 6.5, 6.6, 6.9, Table 1"),
    ("IS 2470 (Part 2):1985", "Soak pit / dispersion - Cl. 4, Cl. 5"),
    ("IS 3370 (Parts 1, 2):2021", "Liquid-retaining crack control"),
    ("IS 4991:1968", "Blast rules - Cl. 6.2.1 recessing, Cl. 7.2 buried surfaces"),
    ("NBC 2016 Part 4", "Fire and life safety, guarding, means of escape"),
    ("FEMA 453", "Shelter ventilation - 0.25 cfm/ft2, carbon adsorber"),
    ("EN 1822", "HEPA classification H14"),
    ("MIL-STD-188-125-1", "EMP - penetration treatment"),
]

# codes NOT in the register - cited by title only, clause numbers NOT quoted
CODES_BY_TITLE_ONLY = [
    ("IS 1742:1983", "Building drainage - code of practice"),
    ("IS 5329:1969", "Sanitary pipework above ground"),
    ("IS 2065:1983", "Water supply in buildings"),
    ("NBC 2016 Part 9", "Plumbing services"),
    ("IS 3103:1975", "Industrial ventilation"),
    ("ISHRAE / ASHRAE handbooks", "Ventilation and duct design practice"),
]


def bay(no):
    for b in BAYS:
        if b[0] == no:
            return b
    raise KeyError(no)


def bay_area(no):
    """Clear floor area of a bay, m2, on the 5000 internal width."""
    return bay(no)[3] * (INT["y1"] - INT["y0"]) / 1e6


def bay_volume(no):
    return bay_area(no) * H_CLEAR / 1000.0
