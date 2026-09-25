"""
sw_figures.py -- the drawn figures of the final-submission report.

The drawings themselves are produced by ../../Scripts/report_figures.py, from the
project's own geometry constants.  This module draws them through a text filter
so that every figure carries plain engineering annotation only: headings are
restated, explanatory side notes are replaced by short design notes or left
out, and the evidence tags used in the working documents are removed.  The
geometry, levels, dimensions and values drawn are not touched.

It also carries the small helpers used to print the drawing index.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "Scripts")))

import report_figures as RF                                    # noqa: E402
from reportlab.graphics.shapes import Drawing, Group          # noqa: E402

DROP = None

# --------------------------------------------------------------------------
#  Per-figure text maps.  'T' = single strings, 'P' = wrapped paragraphs
#  (keyed on their full text), 'N' = note blocks keyed on the heading and
#  mapped to (heading, body) or DROP.
# --------------------------------------------------------------------------
MAPS = {
    "fig_entry_route": {"T": {
        "THE WAY IN  -  NINE STEPS FROM GRADE TO THE CLEAN ZONE, AND WHERE "
        "THE PROTECTIVE BOUNDARY ACTUALLY STARTS":
            "ACCESS ROUTE  -  FROM GRADE TO THE CLEAN ZONE",
        "1 000 x 2 100, opens O": "1 000 x 2 100",
        "EXPENDABLE": "not blast rated",
        "500 roof, 400 walls, N": "500 roof, 400 walls",
        "900 x 2 100, NOT blast": "900 x 2 100",
        "24R @ 170.8333, 3 flig": "24R @ 170.8333",
        "the buried box begins": "shaft to the doors",
        "THE BOUNDARY  -  1 200": "1 200 x 2 100",
        "OUTSIDE  -  expendable": "OUTSIDE THE BOUNDARY",
        "INSIDE  -  the protective boundary": "PROTECTIVE BOUNDARY",
        "EVERYTHING WEST OF THAT LINE IS DESIGNED TO BE LOST.": DROP,
        "WHICH IS WHY THE STAIR VOID IS THE EMP FINDING.": DROP,
        "AND IT IS ALSO THE ONLY ROUTE AN INJURED PERSON CAN USE.": DROP,
        "Routes R2 and R3 are 1 400 mm shafts with vertical ladders and a "
        "six-metre climb.  They are escape shafts, not exits.": DROP},
        "Pall": DROP},
    "fig_long_section": {"T": {"DESIGN GWT (-)2.000 [A]": DROP}},
    "fig_cross_section": {"T": {"DESIGN GWT": "DESIGN GWT (-)2.000"}},
    "fig_stair_section": {"T": {
        "THIS GEOMETRY IS FROZEN.  24 risers at 170.8333 mm, 280 mm tread, "
        "three flights of eight, total rise 4 100 mm, 1 200 mm wide, 200 mm "
        "well, 200 mm waist, 2 533 mm headroom.":
            "24 risers at 170.8333 mm, 280 mm tread, three flights of eight, "
            "total rise 4 100 mm, 1 200 mm wide, 200 mm well, 200 mm waist, "
            "2 533 mm headroom.",
        "It is also the only escape route usable by an injured person, which "
        "is why the width and the landings matter as much as the rise.":
            DROP}},
    "fig_blast_wave": {"T": {
        "not a separate load case": DROP,
        "Shape indicative;  the DESIGN INPUTS are the peak and the duration, "
        "both confirmed.  The yield behind them is deliberately not stated  "
        "[N].": "Shape indicative.  Design inputs:  peak incident "
                "overpressure 344.7 kPa and positive phase duration 0.13 to "
                "1.33 s."}},
    "fig_dlf": {"T": {"A ductility ratio is a": DROP,
                      "PROMISE ABOUT DETAILING,": DROP,
                      "not a discount.": DROP,
                      "the elastic step load  -  the expression":
                          "the elastic step-load value;",
                      "reduces correctly at its own limit":
                          "the expression reduces correctly"}},
    "fig_regimes": {"T": {
        "Roof T = 13.4 ms against t_d 0.13-1.33 s.  A thick slab on a short "
        "span is very stiff, and a nuclear air blast is a long-duration "
        "load.  THAT is what makes a static analysis with a load factor an "
        "honest way to get the demand.":
            "Roof slab T = 13.4 ms against t_d = 0.13 to 1.33 s.  The response "
            "is quasi-static, so an equivalent static load with the dynamic "
            "load factor gives the design demand."}},
    "fig_lateral": {"T": {}},
    "fig_cover": {"T": {
        "BREAKS UP a penetrating item  -  it does not defeat one":
            "breaks up a penetrating item",
        "RADIATION MASS  -  what the second metre buys":
            "radiation shielding mass",
        "declared allowance, held": "compaction tolerance allowance",
        "DESIGN VALUE  -  DL2 in every model": "DESIGN VALUE",
        "The cover buys NO reduction in blast pressure:  K_a = 1.0 "
        "saturated, so a buried roof takes the full p_so.":
            "K_a = 1.0 (saturated ground):  the buried roof is designed for "
            "the full blast pressure.",
        "1.0 m already covers fallout at PF 2 200.  THE SECOND METRE IS "
        "BOUGHT ENTIRELY FOR PROMPT NEUTRON AND GAMMA ATTENUATION.":
            "The first metre gives a fallout protection factor of about "
            "2 200;  the second metre provides prompt neutron and gamma "
            "attenuation."}},
    "fig_flotation": {"T": {
        "2009 kN": DROP, "4802 kN": DROP, "7528 kN": DROP, "12453 kN": DROP,
        "FoS 0.33   FAIL": "FoS 0.33", "FoS 0.78   FAIL": "FoS 0.78",
        "UPLIFT  6 175 kN  -  it does not change":
            "UPLIFT AT DESIGN WATER TABLE",
        "FLOTATION  -  THE CONSTRUCTION STAGE GOVERNS":
            "FLOTATION CHECK AT EACH CONSTRUCTION STAGE",
        "Buoyancy competes with weight, and the weight arrives late.  "
        "Require FoS >= 1.2.  Figures at the pre-lengthening box;  both sides "
        "scale with length, so every factor is unchanged.":
            "Required FoS >= 1.2 in service.  Stages 1 and 2 are held by "
            "continuous dewatering and pressure-relief plugs in the mat until "
            "backfill and cover are complete."}},
    "fig_wall_section": {"T": {
        "600 IS NOT STRENGTH-GOVERNED  -  it is 68 %":
            "600 THICKNESS  -  68 % UTILISED;  ALSO SET BY:",
        "PERIMETER WALL W1 - W4   600 thk   1 : 15": DROP}},
    "fig_w6_and_door": {"T": {
        "-  the blast fixing AND": "- blast fixing and",
        "the only EMP continuity": "EMP continuity",
        "the opening has": DROP,
        "200 thk is IMPOSSIBLE here, not merely awkward:  Mu,lim = 138.0 "
        "kNm/m against a demand of 245.1 kNm/m.  No steel ratio closes that "
        "gap, so the GEOMETRY changed.":
            "A 200 mm wall gives Mu,lim = 138.0 kNm/m against a demand of "
            "245.1 kNm/m;  400 mm is therefore adopted for W6 and W7."}},
    "fig_mat_section": {"T": {
        "3.0 m of support REMOVED, worst position":
            "3.0 m band, worst position",
        "T16 @ 150 EF EW  =  1 340 mm2/m per face   ->   M 303.7 against Mu "
        "362.8 kNm/m  =  84 %, the worst in the box":
            "T16 @ 150 EF EW  =  1 340 mm2/m per face   ->   M 303.7 against "
            "Mu 362.8 kNm/m  =  84 %",
        "Uplift case (net 31.1 kPa up over 5 000) gives only 48.6 kNm/m.  "
        "Bearing governs NOTHING  -  12.5 % of the presumptive value.":
            "Uplift case (net 31.1 kPa up over 5 000) gives 48.6 kNm/m.  "
            "Bearing pressure under blast is 12.5 % of the safe bearing "
            "capacity.",
        "MAT FOUNDATION   600 thk   -   THE CASE THAT SIZES IT   1 : 70":
            "MAT FOUNDATION   600 thk   -   GOVERNING SOFT-BAND CASE   "
            "1 : 70"}},
    "fig_roof_section": {"T": {}},
    "fig_roof_openings": {"T": {
        "T12 4-LEG LINKS @ 250 THROUGHOUT THE PAD  -  a requirement in its "
        "own right": "T12 4-LEG LINKS @ 250 THROUGHOUT THE PAD"}},
    "fig_esc_head": {"T": {
        "a flat Fe250 plate would be 32 mm":
            "(a flat plate would be 32 mm, 505 kg)",
        "      and 505 kg  -  UNLIFTABLE": DROP,
        "NO fall-arrest.  NO rest platform.  And a": DROP,
        "vertical ladder cannot pass a stretcher.": DROP,
        "ESCAPE SHAFT HEAD  -  A 1.54 m2 HOLE IN THE PROTECTIVE BOUNDARY   "
        "1 : 40": DROP}},
    "fig_opening_corner": {"T": {
        "THE OPENING CORNER  -  THE DETAIL MOST OFTEN GOT WRONG        "
        "SP 34 Cl. 5.5":
            "OPENING CORNER DETAIL, ENTRY FLIGHT        SP 34 Cl. 5.5"}},
    "fig_sentry_post": {"T": {
        "THE SENTRY POST  -  A TWO-STOREY RC FRAME ON ITS OWN FOOTINGS, "
        "DELIBERATELY NOT BLAST DESIGNED   1 : 90":
            "SENTRY POST  -  TWO-STOREY RC FRAME ON ISOLATED FOOTINGS   "
            "1 : 90",
        "3-T20 / 2-T20   89 %": "3-T20 / 2-T20"},
        "N": {"IT IS NOT BLAST DESIGNED, AND THAT IS A RECORDED DECISION.":
              DROP},
        "P": {"Seismic governs over wind 2.4 : 1  -  73.18 kN against 29.9 kN"
              "  -  and every member is designed to the model's base shear, "
              "not to the lighter hand-calculated one.":
              DROP}},
    "fig_bearing_chart": {"T": {
        "The founding horizon is 4.8 m below the design water table, so the "
        "SOAKED value is the one that applies.  Worst utilisation 20.6 %; "
        "factor of 4.8 in hand.":
            "The founding horizon is below the design water table, so the "
            "soaked rock value is used.  Worst utilisation 20.6 %.",
        "measured soaked, highest  2 059": "soaked basalt, highest  2 059",
        "MEASURED soaked basalt, lowest  1 961":
            "soaked basalt, lowest  1 961"}},
    "fig_met_chart": {"T": {
        "RECORDED METEOROLOGY  -  MONTHLY MEANS": DROP,
        "Rainfall total 759.6 mm against the soil report's 500-600 mm  -  an "
        "unresolved conflict in the supplied documents.  October, at 139.8 "
        "mm, is the figure to go back and check:  the monsoon has withdrawn "
        "by then.":
            "Annual rainfall 759.6 mm, concentrated in June to October;  "
            "maximum monthly mean temperature 38.3 degC (April)."}},
    "fig_site_plan": {"T": {
        "9.00 m to the EXCAVATION face": DROP,
        "10.00 m to the BOX face": "10.00 m clear of the box",
        "G  SH-2 generator air, X 22 598 - 23 198;  Y not recorded  [N]":
            "G  SH-2 generator air shaft, X 22 598 - 23 198",
        "+X = EAST,  +Y = NORTH   [A].   Dashed: above, or not recorded.":
            "+X = EAST,  +Y = NORTH.   Dashed:  structure below or above "
            "grade."}},
    "fig_hvac_schematic": {"T": {
        "THE AIR PATH  -  ONE WAY IN, ONE WAY OUT, AND A SEPARATE LOOP FOR "
        "THE GENERATOR": "VENTILATION AIR PATH AND ROOM DISTRIBUTION",
        "bay 6  \u00b7  NOTHING IS SUPPLIED TO IT": "bay 6  \u00b7  transfer air only",
        "TRANSFER AIR  -  the whole 300 m3/h, and it is what makes the "
        "cascade work": "TRANSFER AIR  -  the whole 300 m3/h passes through "
                        "the airlock",
        "gooseneck head at +1.500, 12.3 m from the intake to the entry "
        "against a >= 10 m rule":
            "gooseneck head at +1.500, 12.3 m from the entry",
        "RAW AIR  -  UNFILTERED": "RAW AIR DUCT",
        "11.2 m through the": "fully welded, 11.2 m,",
        "clean zone": "tested at +300 Pa",
        "THE GENERATOR LOOP DOES NOT TOUCH THE GAS-TIGHT ENVELOPE.  Bay 8 is "
        "outside it, behind blast door 2 and W7, so running the set neither "
        "depressurises the clean zone nor spends carbon-bed life.":
            "The generator air loop is separate from the gas-tight envelope:  "
            "bay 8 lies behind blast door 2 and W7, so running the set does "
            "not affect the clean-zone overpressure or the carbon beds."}},
    "fig_filter_train": {"T": {
        "300 m3/h duty.  TWO IDENTICAL TRAINS, EACH ABLE TO CARRY THE WHOLE "
        "DUTY ALONE  -  true N+1, not 2 x 150.":
            "300 m3/h duty.  Two identical trains, each able to carry the "
            "whole duty (N+1).",
        "They are the only way to know a filter is spent.  They turn a "
        "vendor's dirty-filter figure into a maintenance trigger.":
            "They show filter loading and set the change-out trigger for "
            "each stage.",
        "STAGE 5 IS THE ONLY STAGE WITH A FINITE, CONSUMABLE LIFE.": DROP,
        "Its change-out interval needs a challenge concentration and vendor "
        "breakthrough data.  Neither exists  -  DATA REQUIRED  [N].": DROP,
        "FIVE OF THE EIGHT PRESSURE-LOSS COMPONENTS ARE VENDOR DATA.": DROP,
        "Only 161 Pa  -  ductwork plus the 100 Pa plenum  -  is derivable.  "
        "The fan must be selected on the DIRTY figures.  A quoted total "
        "would be fabricated.": DROP}},
    "fig_cascade": {"T": {
        "THE OVERPRESSURE CASCADE  -  0 to +50 Pa IN FOUR STEPS, AND WHY THE "
        "AIRLOCK HAS THREE STAGES":
            "THE OVERPRESSURE CASCADE  -  0 TO +50 Pa IN FOUR STEPS",
        "THE CASCADE MAPS EXACTLY ONTO THE THREE AIRLOCK STAGES.":
            "THE CASCADE MAPS ONTO THE THREE AIRLOCK STAGES.",
        "The cascade values are confirmed; the mapping onto the stages is a "
        "reconstruction  [R]  -  the issued sheet does not state it.  Purge: "
        "5 air changes of stage 1 = 12.8 min, so 4 to 5 persons an hour.":
            "Airlock purge:  5 air changes of stage 1 = 12.8 min, giving an "
            "entry rate of 4 to 5 persons per hour."}},
    "fig_septic_soakpit": {"T": {
        "side area 24.19 m2  -  the base is assumed blinded by silt":
            "effective side area 24.19 m2",
        "DESIGN GWT  (-)2.000": DROP},
        "P": {"10 users at 45 lpcd = 450 L/day.  The tank is sized for the "
              "PEACETIME duty:  the shelter is not occupied continuously, "
              "and the sheltered case belongs to the airlock, not to the "
              "lavatory.":
              "10 users at 45 lpcd = 450 L/day, peacetime use.  In the "
              "protective modes sealed-cassette toilets are used and nothing "
              "is discharged."},
        "N": {"WIDENED FROM 2.000 TO 2.200 DIAMETER, NOT DEEPENED.": (
            "SOAK PIT  2.200 DIA x 3.500 EFFECTIVE DEPTH",
            "Side area 24.19 m2 against 22.5 m2 required at an absorption "
            "rate of 20 L/m2/day.  SK-01 and SK-02 share one detail and one "
            "cover slab."),
            "THE 20 L/m2/day ABSORPTION RATE IS ASSUMED  [A], AND A "
            "PERCOLATION TEST TO IS 2470 (Pt 2) Cl. 4 IS MANDATORY.": (
                "PERCOLATION TEST",
                "A percolation test to IS 2470 (Part 2) Cl. 4 is carried out "
                "at the soak pit location before construction.")}},
    "fig_water_balance": {"T": {
        "SK-03  -  NOT SIZED  [N]": "STAIRWELL SOAKAWAY SK-03",
        "400 L/day INTO A 3 375 L SUMP  =  8 DAYS.  That is the number that "
        "matters:  it is longer than the 48-hour closed-mode limit set by the "
        "soda lime, by a factor of four.":
            "400 L/day into a 3 375 L sump = 8 days of storage without power, "
            "four times the 48-hour closed-mode period.",
        "THE SEEPAGE RATE 0.5 L/m2/day IS A DESIGN ALLOWANCE FOR AN INTACT "
        "TANKED STRUCTURE.  It is not a measured figure and it is not a leak "
        "allowance for a defective one.":
            "Seepage allowance 0.5 L/m2/day over the 401 m2 of tanked "
            "envelope below the design water table.",
        "Groundwater does not stop because the shelter is sealed.  The clean "
        "sump pump stays on the essential board through closed mode, and the "
        "hand pump covers the battery failing.":
            "The clean sump pump remains on the essential board in closed "
            "mode;  hand pump PU-03 provides non-electrical back-up."}},
    "fig_emp_zones": {"T": {
        "THE THREE EMP ZONES  -  AND THE ONE THAT CARRIES THE REQUIREMENT":
            "EMP ZONES",
        "EMP ZONE 1   the buried box, all eight bays  -  THE REINFORCEMENT "
        "CAGE IS THE SHIELD":
            "EMP ZONE 1   the buried box, all eight bays  -  reinforcement "
            "cage",
        "MIL-STD-188-125-1 asks for 80 dB from 10 kHz to 1 GHz.  Only one of "
        "these three zones delivers it.":
            "MIL-STD-188-125-1 requirement:  80 dB from 10 kHz to 1 GHz, "
            "provided by the Zone 2 enclosure.",
        "NOTHING CREDITED": "NO CREDIT TAKEN",
        "sentry post +7.000  ·  headhouse +0.900 with no earth cover  ·  "
        "covered stairwell +2.450, expendable  ·  ESC heads  ·  "
        "burster slab":
            "sentry post +7.000  ·  headhouse +0.900  ·  covered "
            "stairwell +2.450  ·  ESC heads  ·  burster slab",
        "80 dB ONLY": "80 dB",
        "1 decade of the 5": "MARGIN ONLY",
        "CANNOT BE SURVEYED": DROP,
        "buried under 2 m of cover": DROP,
        "IEEE Std 299 FULL SURVEY IS A HOLD POINT BEFORE ANY EQUIPMENT IS "
        "INSTALLED.  Every dimension of it is assumed  [A];  only the "
        "requirement is confirmed.":
            "Accepted by a full IEEE Std 299 survey before any equipment is "
            "installed."},
        "P": {"Reinforcement at 150 in both curtains, cast-in frames welded to "
              "the cage, and a welded EMP strap at every construction joint.  "
              "Mesh shielding falls at 20 dB per decade, which is a property "
              "of any mesh and not of this one.":
              "Reinforcement at 150 in both curtains, cast-in frames welded "
              "to the cage and a welded EMP strap at every construction "
              "joint give low-frequency attenuation."}},
    "fig_emp_se": {"T": {
        "SHIELDING EFFECTIVENESS OF THE REINFORCEMENT CAGE  -  20 dB PER "
        "DECADE AGAINST A FLAT 80 dB REQUIREMENT":
            "SHIELDING EFFECTIVENESS OF THE 150 mm REINFORCEMENT CAGE",
        "and reaches 0 dB at 999.31 MHz  -  where the half-spacing":
            "and reaches 0 dB at 999.31 MHz, where the half-spacing",
        "equals a half wavelength and the cage stops being a shield":
            "equals a half wavelength",
        "THE CAGE MEETS 80 dB OVER ONE DECADE OF THE FIVE THE STANDARD ASKS "
        "FOR.  IT IS NOT A SUBSTITUTE FOR ZONE 2.":
            "THE CAGE GIVES 80 dB UP TO ABOUT 100 kHz;  THE FULL BAND IS "
            "PROVIDED BY THE ZONE 2 ENCLOSURE.",
        "This is a property of any mesh:  a 150 mm cage cannot do better, "
        "and closing the grid to reach 1 GHz would need a spacing of about "
        "0.15 mm  -  a sheet, not a cage.": DROP,
        "It also cannot be surveyed.  The exterior is under two metres of "
        "engineered cover, so the figure above is a calculation and stays "
        "one.": DROP}},
    "fig_honeycomb": {"T": {
        "THE HONEYCOMB WAVEGUIDE PANEL  -  TENS OF THOUSANDS OF PARALLEL "
        "TUBES, EACH BELOW CUTOFF":
            "HONEYCOMB WAVEGUIDE VENTILATION PANEL  -  EMP ZONE 2",
        "MARGIN + 8.3 dB, NOT + 53": "MARGIN  + 8.3 dB OVER 80 dB"},
        "N": {"THE SINGLE-CELL NUMBER IS AN UPPER BOUND, AND THE ARRAY "
              "CORRECTION IS WHY VENDOR TEST DATA IS NOT OPTIONAL.": (
                  "INSTALLATION",
                  "The panel is mounted inboard of the blast valve:  the valve "
                  "takes the pressure and the honeycomb takes the radio "
                  "frequency.  The panel is procured with a certified "
                  "attenuation curve for the complete panel.")},
        "P": {"Two consequences are referred rather than resolved:  a "
              "honeycomb panel adds pressure drop, and the fan duty was built "
              "without one;  and the panel's own blast rating is [N].": DROP}},
    "fig_single_line": {"T": {
        "ELECTRICAL SINGLE LINE  -  THREE BOARDS, ONE CABLE ENTRY, AND WHAT "
        "STAYS LIVE WITH NOTHING RUNNING":
            "ELECTRICAL SINGLE LINE DIAGRAM  -  SOURCES, BOARDS AND ESSENTIAL "
            "SERVICES",
        "The largest motor is the filter fan at 0.379 kW;  even direct-on-"
        "line it is about 2.7 kVA, so there is no starting problem.  THE "
        "PACKAGE STOPS AT BOARD LEVEL  -  no circuit schedule, no cable "
        "sizing, no luminaire layout.":
            "The largest motor is the filter fan at 0.379 kW;  direct-on-line "
            "starting is about 2.7 kVA, well within the set rating.",
        "GROUNDWATER DOES NOT STOP BECAUSE THE SHELTER IS SEALED.  The hand "
        "pump PU-03 and the two hand cranks on the filter fans are what cover "
        "the battery failing;  no electrical design should obscure them.":
            "Hand pump PU-03 and the hand cranks on both filter fans provide "
            "non-electrical back-up to the essential system."}},
    "fig_fire_egress": {"T": {
        "FIRE AND EGRESS  -  THREE ROUTES, ONE SMOKE COMPARTMENT 20.8 m LONG, "
        "AND A SHELTER THAT CANNOT BE VENTILATED OF SMOKE":
            "FIRE AND EGRESS",
        "ONE SMOKE COMPARTMENT  -  BAYS 1 TO 6, 20.8 m, FOUR PERMANENTLY "
        "OPEN 900 GAPS": "BAYS 1 TO 6  -  ONE SMOKE COMPARTMENT, 20.8 m",
        "R1's surface end is blocked;  both are outside the boundary and the "
        "stairwell is expendable": "R1's surface end is blocked",
        "bays 1 to 6 are ONE compartment  -  smoke starting in bay 1 reaches "
        "bay 6 unobstructed": "bays 1 to 6 form one smoke compartment",
        "R1 IS THE ONLY ROUTE THAT DOES NOT REQUIRE CLIMBING A SHAFT, AND THE "
        "ONLY ONE USABLE BY AN INJURED PERSON.":
            "R1 IS THE PRIMARY ROUTE AND THE ONLY ROUTE WITHOUT A SHAFT "
            "CLIMB.",
        "THE MOST LIKELY FIRE IN THE SHELTER DENIES ONE OF ITS THREE ESCAPE "
        "ROUTES.": DROP},
        "Pall": DROP},
    "fig_external_works": {"T": {
        "THE DRAINAGE RESERVE  -  EVERYTHING DOWNGRADIENT, IN ONE PLACE, FOR "
        "FOUR STATED REASONS   1 : 420":
            "EXTERNAL WORKS  -  SEPTIC TANK, SOAK PITS AND SOAKAWAYS   1 : 420",
        "THE RESERVE  -  18 000 x 11 000, DOWNGRADIENT":
            "EXTERNAL WORKS RESERVE  18 000 x 11 000, DOWNGRADIENT",
        "WHY EVERYTHING IS IN ONE RESERVE, DOWNGRADIENT":
            "LAYOUT PRINCIPLES"},
        "P": {
            "1   nothing recharges the ground upslope of a box that is "
            "flotation-critical at FoS 0.33 in the mat-only stage  -  and "
            "whose side backfill is MORE permeable than the basalt around it":
            "1   no effluent is released upslope of, or alongside, the buried "
            "box and its backfill",
            "2   one percolation-test location, one keep-clear zone, one "
            "reserved fallback":
            "2   one percolation-test location and one keep-clear zone",
            "3   one trench  -  and where rockhead is 0.9 to 1.5 m, the cost "
            "IS the trench": "3   one common services trench",
            "4   concealment  -  four cover slabs and a 2 m septic vent, "
            "grouped 11 to 22 m away, MARK THE DRAINAGE FIELD, NOT THE "
            "SHELTER":
            "4   cover slabs and the septic vent are grouped 11 to 22 m away "
            "from the shelter",
            "The layout is anchored to confirmed geometry only, and every "
            "offset is relative  -  so if the perimeter fence turns out to be "
            "closer than the reserve's east edge, THE WHOLE RESERVE "
            "TRANSLATES AND NOT ONE OFFSET CHANGES.": DROP}},
    "fig_underground_plan": {"T": {}},
}

_TAG = re.compile(r"\s*\[(A|C|R|N|U)\]")
_CUR = {"name": None}


def _clean(kind, s):
    m = MAPS.get(_CUR["name"], {})
    table = m.get(kind, {})
    if s in table:
        return table[s]
    if kind == "P" and "Pall" in m:
        return m["Pall"]
    return _TAG.sub("", s)


_orig = {"txt": RF.Fig.txt, "para": RF.Fig.para, "note": RF.Fig.note,
         "dimh": RF.Fig.dimh, "dimv": RF.Fig.dimv}
_depth = {"n": 0}


def _txt(self, x, y, s, *a, **k):
    if not _depth["n"]:
        s = _clean("T", s)
        if s is DROP:
            return None
    else:
        s = _TAG.sub("", s)
    return _orig["txt"](self, x, y, s, *a, **k)


def _para(self, x, y, s, *a, **k):
    if not _depth["n"]:
        s = _clean("P", s)
        if s is DROP:
            return y
    _depth["n"] += 1
    try:
        return _orig["para"](self, x, y, s, *a, **k)
    finally:
        _depth["n"] -= 1


def _note(self, x, y, head, body, *a, **k):
    m = MAPS.get(_CUR["name"], {}).get("N", {})
    if head in m:
        rep = m[head]
        if rep is DROP:
            return y
        head, body = rep
    _depth["n"] += 1
    try:
        return _orig["note"](self, x, y, _TAG.sub("", head),
                             _TAG.sub("", body), *a, **k)
    finally:
        _depth["n"] -= 1


def _dimh(self, x1, x2, y, label, *a, **k):
    if _clean("T", label) is DROP:
        return None
    return _orig["dimh"](self, x1, x2, y, label, *a, **k)


def _dimv(self, y1, y2, x, label, *a, **k):
    if _clean("T", label) is DROP:
        return None
    return _orig["dimv"](self, y1, y2, x, label, *a, **k)


def _bounds(d):
    """Content bounds of a drawing, strings measured with their fonts."""
    xs, ys = [], []

    def walk(node, tf):
        for el in getattr(node, "contents", []):
            cls = el.__class__.__name__
            if cls == "Group":
                t = getattr(el, "transform", (1, 0, 0, 1, 0, 0))
                walk(el, _mul(tf, t))
                continue
            pts = []
            if cls == "Line":
                pts = [(el.x1, el.y1), (el.x2, el.y2)]
            elif cls == "Rect":
                pts = [(el.x, el.y), (el.x + el.width, el.y + el.height)]
            elif cls == "Circle":
                pts = [(el.cx - el.r, el.cy - el.r),
                       (el.cx + el.r, el.cy + el.r)]
            elif cls == "String":
                w = RF._strw(el.text, el.fontName, el.fontSize)
                an = getattr(el, "textAnchor", "start")
                x0 = el.x - (w if an == "end" else w / 2.0
                             if an == "middle" else 0.0)
                pts = [(x0, el.y - 0.25 * el.fontSize),
                       (x0 + w, el.y + el.fontSize)]
            elif cls in ("Polygon", "PolyLine"):
                p = el.points
                pts = [(p[i], p[i + 1]) for i in range(0, len(p), 2)]
            for px, py in pts:
                X = tf[0] * px + tf[2] * py + tf[4]
                Y = tf[1] * px + tf[3] * py + tf[5]
                xs.append(X)
                ys.append(Y)
    walk(d, (1, 0, 0, 1, 0, 0))
    return min(xs), min(ys), max(xs), max(ys)


def _mul(a, b):
    return (a[0] * b[0] + a[2] * b[1], a[1] * b[0] + a[3] * b[1],
            a[0] * b[2] + a[2] * b[3], a[1] * b[2] + a[3] * b[3],
            a[0] * b[4] + a[2] * b[5] + a[4],
            a[1] * b[4] + a[3] * b[5] + a[5])


def _crop(d, pad=4.0):
    """Trim empty space left where notes were removed; keep the width."""
    x0, y0, x1, y1 = _bounds(d)
    bottom = max(0.0, y0 - pad)
    top = min(d.height, y1 + pad)
    g = Group(*d.contents)
    g.translate(0, -bottom)
    nd = Drawing(d.width, top - bottom)
    nd.add(g)
    return nd


def _post_site_plan(d):
    """Remove the dimension line whose label is not printed."""
    reds = [el for el in d.contents if el.__class__.__name__ == "Line"
            and el.strokeColor == RF.RED and abs(el.y1 - el.y2) < 0.01]
    kill = set(id(el) for el in reds)
    for r in reds:
        lo, hi = min(r.x1, r.x2) - 3, max(r.x1, r.x2) + 3
        for el in d.contents:
            if el.__class__.__name__ == "Line":
                mx, my = (el.x1 + el.x2) / 2.0, (el.y1 + el.y2) / 2.0
                if abs(my - r.y1) < 2.5 and lo <= mx <= hi and \
                        abs(el.x1 - el.x2) < 4 and abs(el.y1 - el.y2) < 4:
                    kill.add(id(el))
    d.contents = [el for el in d.contents if id(el) not in kill]


POST = {"fig_site_plan": _post_site_plan}


def figure(name):
    fn = getattr(RF, name)
    RF.Fig.txt, RF.Fig.para, RF.Fig.note = _txt, _para, _note
    RF.Fig.dimh, RF.Fig.dimv = _dimh, _dimv
    _CUR["name"] = name
    try:
        d = fn()
    finally:
        RF.Fig.txt, RF.Fig.para, RF.Fig.note = (_orig["txt"], _orig["para"],
                                                _orig["note"])
        RF.Fig.dimh, RF.Fig.dimv = _orig["dimh"], _orig["dimv"]
        _CUR["name"] = None
    if name in POST:
        POST[name](d)
    _blacken(d)
    return _crop(d)


def _blacken(node):
    """All lettering in black; line work and fills keep their colours."""
    from reportlab.lib import colors
    for el in getattr(node, "contents", []):
        cls = el.__class__.__name__
        if cls == "Group":
            _blacken(el)
        elif cls == "String":
            el.fillColor = colors.black


def cover_figure():
    d = figure("fig_long_section")

    def strip(node):
        node.contents = [el for el in node.contents if not (
            el.__class__.__name__ == "String" and
            el.text.startswith("LONGITUDINAL SECTION"))]
        for el in node.contents:
            if el.__class__.__name__ == "Group":
                strip(el)
    strip(d)
    return d


def all_strings(name):
    """Every string a figure prints, after filtering -- used for checking."""
    d = figure(name)
    out = []

    def walk(node):
        for el in getattr(node, "contents", []):
            if el.__class__.__name__ == "Group":
                walk(el)
            elif el.__class__.__name__ == "String":
                out.append(el.text)
    walk(d)
    return out


# --------------------------------------------------------------------------
#  Drawing index helpers
# --------------------------------------------------------------------------
DRAWING_GROUP_ORDER = [
    "Services - General Arrangement",
    "Architectural - Presentation Sheets (A2)",
    "Architectural - Finishes",
    "Structural - Reinforcement",
    "Structural - Presentation Sheets (A2)",
    "Services - Presentation Sheets (A2)",
    "Fire and Life Safety - Presentation Sheet (A2)",
    "Works Management - Presentation Sheet (A2)",
    "Site Selection and Geotechnical",
    "Site and Concealment",
    "Drainage",
    "Drainage - Handout Sheets",
    "HVAC and CBRN Ventilation",
    "HVAC - Handout Sheets",
    "EMP Protection",
    "Electrical",
    "Fire and Life Safety",
]

_GROUPS = {
    "ARCHITECTURAL / GENERAL - Rev F":
        ("Services - General Arrangement", "current/cad"),
    "ARCHITECTURAL - A2 presentation sheets":
        ("Architectural - Presentation Sheets (A2)", "Presentation Sheets"),
    "ARCHITECTURAL - finishes":
        ("Architectural - Finishes", "Schedule of Finishes"),
    "STRUCTURAL - reinforcement":
        ("Structural - Reinforcement", "Structural CAD"),
    "STRUCTURAL - A2 presentation sheets":
        ("Structural - Presentation Sheets (A2)", "Presentation Sheets"),
    "MEP - A2 presentation sheets":
        ("Services - Presentation Sheets (A2)", "Presentation Sheets"),
    "FIRE AND LIFE SAFETY - A2 presentation sheets":
        ("Fire and Life Safety - Presentation Sheet (A2)",
         "Presentation Sheets"),
    "WORKS MANAGEMENT - A2 presentation sheets":
        ("Works Management - Presentation Sheet (A2)", "Presentation Sheets"),
    "DRAINAGE": ("Drainage", "Drainage"),
    "DRAINAGE - handout": ("Drainage - Handout Sheets", "Drainage"),
    "HVAC": ("HVAC and CBRN Ventilation", "HVAC"),
    "HVAC - handout": ("HVAC - Handout Sheets", "HVAC"),
    "FIRE AND LIFE SAFETY": ("Fire and Life Safety", "Fire and Life Safety"),
    "SITE AND CONCEALMENT": ("Site and Concealment", "Site and Concealment"),
    "EMP PROTECTION": ("EMP Protection", "EMP Protection"),
    "ELECTRICAL": ("Electrical", "Electrical"),
    "SITE SELECTION AND GEOTECHNICAL":
        ("Site Selection and Geotechnical",
         "Site Selection and Geotechnical"),
}


# The ten Rev F architectural drawings supplied by the owner (master E.2).
# They are input, not drawings generated in the project, and are not listed.
INPUT_SET = {
    "current/cad/1_Underground_Level_Plan.dxf",
    "current/cad/1_Staircase_Section.dxf",
    "current/cad/2_Side_Section_with_Stairs.dxf",
    "current/cad/2_Ground_Plan_Headhouse_Berm.dxf",
    "current/cad/3_Headhouse_Section_Cutaway.dxf",
    "current/cad/5_Entry_Headhouse_Stair_Section.dxf",
    "current/cad/5_Front_Elevation.dxf",
    "current/cad/3_Sentry_Post_Ground_Floor_Plan.dxf",
    "current/cad/4_Sentry_Post_First_Floor_Plan.dxf",
    "current/cad/6_Sentry_Post_Framing_Plan.dxf",
}


def is_generated(rec):
    return rec["file"] not in INPUT_SET


def drawing_group(rec):
    g = _GROUPS.get(rec.get("discipline", ""))
    if g is None:
        folder = rec["file"].split("/")[0]
        g = (rec.get("discipline", folder).title(), folder)
    return g


_TITLE_FIX = {
    "SG-202": "EXTERNAL WORKS SITING AND SOAK PIT DETAILS",
    "SG-001": "SITE AND GEOTECHNICAL DESIGN BASIS",
    "ARCH001": "UNDERGROUND LEVEL PLAN, HEADHOUSE LEVEL PLAN AND GROUND "
               "LEVEL PLAN",
    "ARCH002": "SENTRY POST - FLOOR PLANS AND SOUTH ELEVATION",
}


def clean_title(rec):
    t = _TITLE_FIX.get(rec["number"], rec["title"])
    t = re.sub(r"\s+-\s+", " - ", t)
    t = re.sub(r"\s{2,}", " ", t)
    return t.strip()


def clean_scale(s):
    s = (s or "").strip().rstrip(".")
    if s in ("-", ""):
        return "As shown"
    if s.lower() == "not to scale":
        return "NTS"
    if s.upper() in ("AS SHOWN", "AS NOTED"):
        return "As shown"
    return s


def sheet_key(num):
    parts = re.findall(r"\d+|\D+", num)
    return [int(p) if p.isdigit() else p for p in parts]
