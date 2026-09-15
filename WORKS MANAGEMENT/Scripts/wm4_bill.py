"""
wm4_bill.py — the Works Management bill of quantities priced at SSR 2022-23.

Underground CBRN-hardened blast-resistant protective structure + sentry post, Pune.
Works Management package revision WM4 · 15 September 2026.

WHAT THIS IS.  WM1 (7 Sep 2026, master H.10) measured the whole project as 90
items in 10 sections and DELIBERATELY carried no rate, because no rate could be
sourced: master I/Part G records "Rates come from the MES SSR.  No item number
could be verified from the material available."  The project owner has now
supplied the Government of Maharashtra PWD STATE SCHEDULE OF RATES 2022-23.
WM4 prices the WM1 bill from it.

THE THREE TIERS.  Every line lands in exactly one:

  PRICED         the SSR publishes an item that matches the specified work, or
                 a rate derived from a published item by the SSR's OWN stated
                 method (the cement-consumption rule for a higher grade, the
                 depth and floor-lift increases of Section B).
  PRICED [A]     priced on an assumption this package states in the open —
                 a substituted specification, or a band the SSR leaves to the
                 Superintending Engineer.  Carried in the total, and listed
                 separately so it can be lifted out.
  NOT PRICED     the project has no specification, or the SSR has no item.
                 NO RATE IS INVENTED.  Section B of the SSR General Notes is
                 explicit about what happens instead: "The items for which
                 rates are not included in State Schedule of Rates, the rates
                 shall be approved by concerned Superintending Engineer, PWD."

NOTHING IN THE DESIGN IS CHANGED BY THIS REVISION.  No dimension, load, bar,
level, thickness or QUANTITY moves.  The main staircase is untouched.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from wm4_ssr_library import (SSR, MATERIAL, CEMENT_BAGS, DEPTH_INCREASE,
                             FLOOR_LIFT, grade_uplift, ON_COST)

R = lambda x: round(x + 1e-9, 2)        # money and areas
Q = lambda x: round(x + 1e-9, 3)        # volumes, so a split sums back exactly


# ===========================================================================
#  DERIVED RATES — every one shown with its arithmetic
# ===========================================================================

DERIVED = {}
_deriv_log = []


def derive(key, value, working):
    DERIVED[key] = R(value)
    _deriv_log.append((key, R(value), working))
    return DERIVED[key]


# --- concrete grades the SSR does not publish for that member family --------
_p25 = SSR["26.19"]["completed"]          # R.C.C. pardi (wall), M-25
derive("PARDI_M35", _p25 + grade_uplift("M25", "M35"),
       "SSR 26.19 R.C.C. pardi M-25 = %d.  Highest grade published for this "
       "item is M-25; the box is M-35.  General Notes Section B: derive by "
       "adding the difference in standard cement consumption.  "
       "(8.25 - 7.50) bags x 50 kg x Rs 6.00/kg x %.4f on-cost = %.2f.  "
       "%d + %.2f = %.2f /m3"
       % (_p25, ON_COST, grade_uplift("M25", "M35"), _p25,
          grade_uplift("M25", "M35"), _p25 + grade_uplift("M25", "M35")))

derive("PARDI_M30", _p25 + grade_uplift("M25", "M30"),
       "SSR 26.19 R.C.C. pardi M-25 = %d.  Sentry post parapet is M-30.  "
       "(8.00 - 7.50) bags x 50 kg x Rs 6.00/kg x %.4f = %.2f.  "
       "%d + %.2f = %.2f /m3"
       % (_p25, ON_COST, grade_uplift("M25", "M30"), _p25,
          grade_uplift("M25", "M30"), _p25 + grade_uplift("M25", "M30")))

_w25 = SSR["26.26"]["completed"]          # waist slab and steps, M-25
derive("WAIST_M35", _w25 + grade_uplift("M25", "M35"),
       "SSR 26.26 R.C.C. waist slab and steps of staircases M-25 = %d.  "
       "Highest grade published for this item is M-25; the main staircase is "
       "M-35.  (8.25 - 7.50) bags x 50 kg x Rs 6.00/kg x %.4f = %.2f.  "
       "%d + %.2f = %.2f /m3"
       % (_w25, ON_COST, grade_uplift("M25", "M35"), _w25,
          grade_uplift("M25", "M35"), _w25 + grade_uplift("M25", "M35")))

# --- excavation depth bands, SSR General Notes Section B --------------------
_rock = SSR["21.20"]["completed"]
derive("ROCK_0_3", _rock, "SSR 21.20 hard rock by chiselling / wedging / line "
       "drilling, mechanical = %d.  Depth below 3.0 m: no increase" % _rock)
derive("ROCK_3_45", _rock * 1.20,
       "SSR 21.20 = %d x 1.20.  Section B: '3.0 m to 4.50 m depth add 20 %%'" % _rock)
derive("ROCK_45_6", _rock * 1.30,
       "SSR 21.20 = %d x 1.30.  Section B: '4.5 m to 6.0 m depth add 30 %%'" % _rock)
derive("ROCK_6_PLUS", _rock * 1.30,
       "SSR 21.20 = %d x 1.30.  [A] Section B stops at 6.0 m: 'Depth beyond "
       "6.0 m - extra percent to be decided by concerned Superintending "
       "Engineer'.  NO PERCENTAGE IS INVENTED HERE.  The 4.5-6.0 m band's "
       "30 %% is carried on as a DECLARED LOWER BOUND so the line is not left "
       "blank; the true figure can only be higher.  Open item WM4-V1" % _rock)

# --- floor lift, SSR General Notes Section B --------------------------------
for _k, _base in (("M30_SLAB", SSR["25.74"]["completed"]),
                  ("M30_BEAM", SSR["25.54"]["completed"])):
    derive(_k + "_FF", _base * (1 + FLOOR_LIFT["first"]),
           "SSR %s = %d x 1.01.  Section B floor lift: 'First floor 1 %%'"
           % ({"M30_SLAB": "25.74", "M30_BEAM": "25.54"}[_k], _base))
derive("PARDI_M30_FF", DERIVED["PARDI_M30"] * (1 + FLOOR_LIFT["first"]),
       "Derived M-30 pardi %.2f x 1.01 (first floor lift 1 %%)" % DERIVED["PARDI_M30"])
derive("BRICK_FF", SSR["27.05"]["completed"] * (1 + FLOOR_LIFT["first"]),
       "SSR 27.05 = %d x 1.01 (first floor lift 1 %%)" % SSR["27.05"]["completed"])

# --- composite finishes -----------------------------------------------------
derive("MEMBRANE_PROT", SSR["51.114"]["completed"] + SSR["51.115"]["completed"],
       "SSR 51.114 membrane %d + SSR 51.115 20 mm protective screed %d = %d /m2.  "
       "WP-06 is specified as external-grade membrane PLUS protection"
       % (SSR["51.114"]["completed"], SSR["51.115"]["completed"],
          SSR["51.114"]["completed"] + SSR["51.115"]["completed"]))


# ===========================================================================
#  THE BILL
# ===========================================================================
# (code, description, unit, qty, ssr_item, rate, tier, note)
#   tier: "P" priced · "A" priced on a stated assumption · "N" not priced
# A rate of None with tier "X" means the work is INCLUDED in another line's
# composite rate and must not be paid twice.

P, A, N, X = "P", "A", "N", "X"

BILL = []


def b(section, code, desc, unit, qty, item, rate, tier, note):
    BILL.append(dict(section=section, code=code, desc=desc, unit=unit, qty=qty,
                     ssr=item, rate=rate, tier=tier, note=note,
                     amount=None if (rate is None or qty is None)
                     else R(qty * rate)))


# --- the excavation depth model, reproducing the WM1 quantities -------------
EXC_AREA = 1338.24 / 6.800                 # 196.80 m2, back-figured from WM1 E-02
ROCKHEAD = 1.750                           # mean, master / SG1


SEC_A = "A · SITE PREPARATION AND EARTHWORKS"

b(SEC_A, "E-01", "Site clearance and grubbing, shelter area", "m2", 618.8,
  "21.33", SSR["21.33"]["completed"], P,
  "Clearance only.  The 150 topsoil strip is measured and priced at E-01a")
b(SEC_A, "E-01a", "Topsoil stripped 150 thk and stockpiled for re-use in the "
  "concealment layer", "m3", 92.82, "21.02", SSR["21.02"]["completed"], P,
  "Excavation in soil, lift <= 1.5 m, mechanical.  Stacking within 50 m is "
  "inside the SSR rate, which is exactly what stockpiling for re-use is")
b(SEC_A, "E-02", "Bulk excavation, main shelter, 0.000 to (-)6.800, all strata "
  "— SUM OF THE SIX DEPTH BANDS BELOW", "m3", 1338.24, "—", None, X,
  "Measured at E-02.1 to E-02.6.  Plan area %.2f m2 = 1338.24 / 6.800" % EXC_AREA)
b(SEC_A, "E-02.1", "  0.000 to (-)1.500, soil / weathered overburden", "m3",
  Q(EXC_AREA * 1.500), "21.02", SSR["21.02"]["completed"], P,
  "Lift <= 1.5 m.  Reproduces the WM1 lower bound of 295.2 m3 exactly")
b(SEC_A, "E-02.2", "  (-)1.500 to (-)1.750, soil to mean rockhead", "m3",
  Q(EXC_AREA * 0.250), "21.04", SSR["21.04"]["completed"], P,
  "Lift 1.5 to 3.0 m.  E-02.1 + E-02.2 = 344.4 m3 = WM1 item E-02a exactly")
b(SEC_A, "E-02.3", "  (-)1.750 to (-)3.000, Deccan basalt", "m3",
  Q(EXC_AREA * 1.250), "21.20", DERIVED["ROCK_0_3"], P,
  "BY HYDRAULIC BREAKER, NOT BLASTING — WM_CONSTRUCTION_METHODOLOGY.md and "
  "risk S-02.  SSR 21.20 is the schedule's non-blasting rock item; the three "
  "blasting items 21.17 / 21.18 / 21.19 do not apply to this project")
b(SEC_A, "E-02.4", "  (-)3.000 to (-)4.500, Deccan basalt", "m3",
  Q(EXC_AREA * 1.500), "21.20", DERIVED["ROCK_3_45"], P,
  "SSR 21.20 + 20 % depth increase, General Notes Section B")
b(SEC_A, "E-02.5", "  (-)4.500 to (-)6.000, Deccan basalt", "m3",
  Q(EXC_AREA * 1.500), "21.20", DERIVED["ROCK_45_6"], P,
  "SSR 21.20 + 30 % depth increase, General Notes Section B")
b(SEC_A, "E-02.6", "  (-)6.000 to (-)6.800, Deccan basalt", "m3",
  Q(EXC_AREA * 0.800), "21.20", DERIVED["ROCK_6_PLUS"], A,
  "[A] BEYOND THE SSR's LAST DEFINED BAND.  Priced at the 4.5-6.0 m band's "
  "+30 % as a declared LOWER BOUND.  Section B leaves the percentage to the "
  "Superintending Engineer.  OPEN ITEM WM4-V1")
b(SEC_A, "E-02a", "  of which excavation in soil / weathered overburden", "m3",
  344.4, "—", None, X, "Memorandum.  Priced at E-02.1 and E-02.2")
b(SEC_A, "E-02b", "  of which excavation in rock (Deccan basalt)", "m3", 993.84,
  "—", None, X, "Memorandum.  Priced at E-02.3 to E-02.6")
b(SEC_A, "E-03", "Excavation in rock for sump pit SU-01, below general formation",
  "m3", 9.477, "21.20", DERIVED["ROCK_6_PLUS"], A,
  "[A] Below (-)6.800, so beyond the SSR's last defined depth band.  Same "
  "lower bound and the same open item as E-02.6 — WM4-V1")
b(SEC_A, "E-04", "Excavation for the covered entry stairwell, outside the box "
  "envelope, 0.000 to (-)2.000", "m3", 19.096, "21.04",
  SSR["21.04"]["completed"], A,
  "[A] Priced wholly as soil at the 1.5-3.0 m lift.  The strata split is not "
  "derivable from the project record; SG1 puts a CH clay horizon here to "
  "1.0 m.  If basalt is met below the mean rockhead the 21.20 rate applies "
  "to that part")
b(SEC_A, "E-05.1", "Excavation, sentry post footings F1, 4 No.: 0.000 to "
  "(-)1.500, soil", "m3", Q(4 * 2.100 ** 2 * 1.500), "21.02",
  SSR["21.02"]["completed"], P,
  "Pits 2.100 sq (0.300 working space) x 2.100 deep — wm_quantities.py 1.6")
b(SEC_A, "E-05.2", "  (-)1.500 to (-)1.750, soil", "m3", Q(4 * 2.100 ** 2 * 0.250),
  "21.04", SSR["21.04"]["completed"], P, "Lift 1.5 to 3.0 m")
b(SEC_A, "E-05.3", "  (-)1.750 to (-)2.100, Deccan basalt", "m3",
  Q(4 * 2.100 ** 2 * 0.350), "21.20", DERIVED["ROCK_0_3"], P,
  "F1 founds on in-situ basalt at (-)2.000.  Depth under 3.0 m: no increase.  "
  "E-05.1 + E-05.2 + E-05.3 = 37.044 m3 = WM1 item E-05 exactly")
b(SEC_A, "E-06", "Filling in compacted granular fill under the sentry post "
  "ground floor", "m3", 7.452, "21.37", SSR["21.37"]["completed"], P,
  "Contractor's material, 15-20 cm layers, watered and compacted")
b(SEC_A, "E-07", "Side backfill in selected granular fill, 250 layers to 95 % MDD",
  "m3", 289.92, "21.37", SSR["21.37"]["completed"], P,
  "SSR layers are 15-20 cm against the specified 250 — the specification is "
  "TIGHTER than the schedule, so the SSR rate is not understated on that count")
b(SEC_A, "E-08", "Surplus excavated material — re-use on site as engineered "
  "fill / crushed rubble, remainder to spoil", "m3", 1113.937, "—", None, X,
  "INCLUDED.  Every SSR excavation item already carries removal to 50 m "
  "beyond the building area and stacking as directed.  Lead beyond 50 m is "
  "payable under SSR Statement C-1 transportation charges and CANNOT be "
  "quantified — no site plan and no spoil destination exists (Drainage D3)")
b(SEC_A, "E-09", "Preconstructional antitermite treatment to the bottom surface "
  "and sides of the excavation, IS 6313 Part II", "m2", None, "21.22",
  SSR["21.22"]["completed"], N,
  "NOT IN THE WM1 BILL and no quantity exists.  Listed because the owner's "
  "own RC1 bill carries a 320 m2 anti-termite line and the SSR has an item "
  "for it.  Rate shown for information; NOT in the total")

SEC_B = "B · MAIN UNDERGROUND SHELTER — CONCRETE"

b(SEC_B, "C-01", "Mat 600 (M35)", "m3", 81.8, "25.17", SSR["25.17"]["completed"], P,
  "SSR 25.17 names raft foundations explicitly.  Formwork IS IN THE RATE")
b(SEC_B, "C-02", "Pressure slab 900, net of openings (M35)", "m3", 112.0,
  "25.76", SSR["25.76"]["completed"], P, "R.C.C. slabs and landings, M-35")
b(SEC_B, "C-03", "Perimeter walls 600 (M35)", "m3", 103.7, "26.19 der.",
  DERIVED["PARDI_M35"], P,
  "R.C.C. pardi (wall) of required thickness, grade-uplifted M25 -> M35 by "
  "the SSR's own cement-consumption rule")
b(SEC_B, "C-04", "Walls W6 / W7 400 (M35)", "m3", 12.8, "26.19 der.",
  DERIVED["PARDI_M35"], P, "As C-03")
b(SEC_B, "C-05", "Wall W5 200 (M35)", "m3", 3.2, "26.19 der.",
  DERIVED["PARDI_M35"], P, "As C-03")
b(SEC_B, "C-06.1", "Headhouse walls 400 (M35)", "m3", 18.8, "26.19 der.",
  DERIVED["PARDI_M35"], P,
  "WM1 item C-06 is walls + roof at 32.7 m3.  Split pro rata from its own "
  "derivation: walls (4.800 x 5.800 - 4.000 x 5.000) x 2.400 = 18.816, roof "
  "4.800 x 5.800 x 0.500 = 13.920, total 32.736.  No quantity is changed")
b(SEC_B, "C-06.2", "Headhouse roof 500 (M35)", "m3", 13.9, "25.76",
  SSR["25.76"]["completed"], P, "Same split as C-06.1")
b(SEC_B, "C-07", "Main staircase, waist and landings (M35)", "m3", 3.0,
  "26.26 der.", DERIVED["WAIST_M35"], P,
  "R.C.C. waist slab and steps of staircases, grade-uplifted M25 -> M35.  "
  "THE STAIRCASE GEOMETRY IS FROZEN AND IS NOT TOUCHED — 24 risers, "
  "170.8333 riser, 280 tread, 3 flights x 8, 4 100 total rise")
b(SEC_B, "C-08", "Entry stairwell: walls, roof, raft, flight, landings (M35)",
  "m3", 19.9, "26.19 der.", DERIVED["PARDI_M35"], A,
  "[A] A composite accepted whole from SC1 — no volume split by member exists.  "
  "Priced entirely at the WALL rate, which is the DEAREST of the M-35 family, "
  "so the line cannot be understated by the choice.  83.0 of the 110.9 m2 of "
  "its formwork is wall face, so walls do govern")
b(SEC_B, "C-09", "Blinding / PCC M15, 100 thk under the mat", "m3", 14.208,
  "24.04", SSR["24.04"]["completed"], P, "M15 for foundation and bedding")
b(SEC_B, "C-10", "Blinding / PCC M15, 100 thk, sump pit, footings F1 and "
  "stairwell raft", "m3", 3.045, "24.04", SSR["24.04"]["completed"], P, "As C-09")
b(SEC_B, "C-11", "Sump pit SU-01 walls 300 and base 400 below the mat soffit (M35)",
  "m3", 3.708, "26.19 der.", DERIVED["PARDI_M35"], A,
  "[A] Walls and base measured together in WM1.  Priced at the wall rate "
  "throughout — the dearer of the two applicable rates")
b(SEC_B, "C-12", "Escape shaft collars ESC 1 and ESC 2, 250 RC, OD 1900 (M35)",
  "m3", 6.285, "26.19 der.", DERIVED["PARDI_M35"], P,
  "Circular 250 walls.  The SSR has no curved-formwork item; 26.19 is "
  "'of required thickness' and is the closest published item")
b(SEC_B, "C-13", "Local thickenings of the pressure slab 900 -> 1200 at openings "
  "(M35)", "m3", 3.331, "25.76", SSR["25.76"]["completed"], P, "Slab work")
b(SEC_B, "C-14", "Internal partitions W8, 4 No., 110 thk, non-structural (M35)",
  "m3", 6.208, "26.19 der.", DERIVED["PARDI_M35"], A,
  "[A] W8 is non-structural with A252 mesh both faces; the project states NO "
  "GRADE and WM1 measured it as M35 with the rest of the box (tagged [A] "
  "there).  That tag is carried, not resolved")

SEC_C = "C · REINFORCEMENT — ALL WORKS"

_reb = [("R-T8", "Reinforcement T8 Fe500D, shelter and entry structures", 0.006),
        ("R-T10", "Reinforcement T10 Fe500D, shelter and entry structures", 0.063),
        ("R-T12", "Reinforcement T12 Fe500D, shelter and entry structures", 20.318),
        ("R-T16", "Reinforcement T16 Fe500D, shelter and entry structures", 23.707),
        ("R-T20", "Reinforcement T20 Fe500D, shelter and entry structures", 10.923),
        ("R-T25", "Reinforcement T25 Fe500D, shelter and entry structures", 15.439),
        ("R-BS", "Reinforcement T12 Fe500 to the burster slab (M30)", 1.218),
        ("R-S8", "Reinforcement T8 Fe500, sentry post", 0.645),
        ("R-S10", "Reinforcement T10 Fe500, sentry post", 0.245),
        ("R-S12", "Reinforcement T12 Fe500, sentry post", 0.19),
        ("R-S16", "Reinforcement T16 Fe500, sentry post", 0.624),
        ("R-S20", "Reinforcement T20 Fe500, sentry post", 0.269)]
for _c, _d, _q in _reb:
    b(SEC_C, _c, _d, "t", _q, "26.33", SSR["26.33"]["completed"], P,
      "TMT Fe-500, cut, bent, hooked, tied and FIXED IN POSITION.  The SSR "
      "measures the fixed weight, which is the net weight scheduled here")
b(SEC_C, "R-ORD", "Reinforcement ORDER quantity, all works, incl. 5 % wastage",
  "t", 77.33, "—", None, X,
  "PROCUREMENT MEMORANDUM, NOT A PAYABLE ITEM.  SSR 26.33 is paid on the "
  "weight fixed in position — 73.647 t, the sum of the twelve lines above.  "
  "77.33 / 1.05 = 73.648, so the two figures agree exactly.  Wastage is "
  "inside the SSR rate and must not be paid a second time")

SEC_D = "D · FORMWORK AND FALSEWORK"

b(SEC_D, "F-01", "Formwork, shelter and entry structures, contact area", "m2",
  1057.743, "—", None, X,
  "INCLUDED IN EVERY CONCRETE RATE ABOVE.  SSR items 24.04, 25.15, 25.17, "
  "25.35, 25.54, 25.74, 25.76, 26.19 and 26.26 each read 'including STEEL "
  "CENTERING, FORMWORK, cover blocks'.  Paying F-01 separately would pay for "
  "the same formwork twice.  The quantity stands as a measured control figure")
b(SEC_D, "F-02", "Falsework to the pressure slab soffit, 3.200 m height, props "
  "to remain 14 days (IS 456 Table 11)", "m2", 104.0, "—", None, X,
  "INCLUDED, as F-01.  The 14-day prop period remains a PROGRAMME driver "
  "even though it is not a separately payable item")

SEC_E = "E · ENGINEERED COVER, OVERBURDEN AND CONCEALMENT"

b(SEC_E, "B-screed", "Protection screed 100 over the membrane (cover layer 1)",
  "m3", 10.289, "24.04", SSR["24.04"]["completed"], P,
  "M15 bedding concrete.  THIS IS THE SAME WORK AS ITEM W-05, which is "
  "measured in m2 — 102.889 x 0.100 = 10.289.  Paid here ONCE")
b(SEC_E, "B-fill", "Compacted engineered fill @ 95 % MDD", "m3", 77.167,
  "21.37", SSR["21.37"]["completed"], P, "As E-07")
b(SEC_E, "B-rubble", "Crushed basalt rubble 25-75 mm", "m3", 51.445, "21.38",
  SSR["21.38"]["completed"], P,
  "Trap rubble stone soling, hand packed and compacted.  SEE THE CREDIT LINE "
  "BELOW — this material is to be won from the project's own rock excavation")
b(SEC_E, "B-rubble-cr", "  CREDIT if the rubble is won on site and crushed, as "
  "the quantity derivation directs", "m3", 51.445, "21.38", None, X,
  "MEMORANDUM, NOT DEDUCTED.  994 m3 of basalt comes out of E-02b against "
  "51.4 m3 needed.  The SSR labour component of 21.38 is Rs 432 against the "
  "completed Rs 1 382, so winning it on site is worth about "
  "51.445 x (1382 - 432) = Rs 48 873, and removes 51 m3 of import AND 51 m3 "
  "of cart-away.  Left in the bill at the full SSR rate because the crushing "
  "plant is not in the project record")
b(SEC_E, "B-burster", "RC burster slab M30, T12 @ 150 B/W, 200 thk", "m3",
  20.578, "25.15", SSR["25.15"]["completed"], P,
  "Ground-supported: it is cast on the 500 crushed-rubble layer, and its own "
  "formwork measure is EDGE ONLY, 11.3 m2.  So the raft item 25.15 governs, "
  "not the suspended-slab item 25.74 (M-30, Rs 14 299)")
b(SEC_E, "B-filter", "Granular filter, 150 thk", "m3", 15.433, "21.39",
  SSR["21.39"]["completed"], A,
  "[A] SSR 21.39 sand filling is the nearest published item and carries the "
  "condition 'to be executed with prior approval of the Superintending "
  "Engineer'.  The project specifies no filter grading — no gradation is "
  "invented here")
b(SEC_E, "B-concealment", "Topsoil / turf — concealment and erosion, 300 thk",
  "m3", 30.867, "21.36", SSR["21.36"]["completed"], P,
  "Filling with APPROVED EXCAVATED MATERIAL, watered and compacted — exactly "
  "the 92.82 m3 stripped and stockpiled at E-01a, of which 30.867 is used.  "
  "TURFING ITSELF IS NOT IN THE SSR: the schedule directs Parks and Gardens "
  "wing rates for that, which this project does not hold")
b(SEC_E, "B-berm", "Berm forming and grading, 1.5:1 to +0.900 against the "
  "headhouse and covered stairwell", "m3", None, "21.36", None, N,
  "NOT PRICED.  NO QUANTITY EXISTS — no site plan and no ground model is in "
  "the project (Drainage open item D3).  A rate is available (SSR 21.36, "
  "Rs 120/m3) the moment a quantity does")
b(SEC_E, "B-camo", "Camouflage and concealment measures beyond the 300 topsoil "
  "/ turf layer", "item", None, "—", None, N,
  "NOT PRICED and NOT IN THE SSR.  No concealment specification exists in "
  "the project.  SSR General Notes Section B: rates not in the schedule are "
  "to be approved by the Superintending Engineer")

SEC_F = "F · WATERPROOFING"

b(SEC_F, "W-01", "WP-01 tanking, horizontal on blinding under the mat", "m2",
  142.08, "51.114", SSR["51.114"]["completed"], A,
  "[A] SPECIFICATION SUBSTITUTION.  WP-01 is a continuous external tanking "
  "MEMBRANE (FINISH_LEGEND).  SSR 51.114 is a five-layer polymeric membrane "
  "on a 90 micron HMHDPE core — the material matches; the SSR describes it "
  "applied to roof and parapet, not below grade.  The SSR's own below-grade "
  "item, 31.12, is a rough shahabad BOX treatment at Rs 1 286 — a different "
  "specification, carried in the workbook as the alternative")
b(SEC_F, "W-02", "WP-01 tanking, vertical to external wall faces, (-)6.700 to "
  "(-)2.000", "m2", 265.08, "51.114", SSR["51.114"]["completed"], A,
  "[A] As W-01.  SSR alternative for vertical basement faces is 31.13, "
  "Rs 1 338")
b(SEC_F, "W-03", "WP-01 tanking, roof membrane, net of the void and shafts",
  "m2", 121.881, "51.114", SSR["51.114"]["completed"], A, "[A] As W-01")
b(SEC_F, "W-04", "WP-01 upstands, fillets and dressing to openings and "
  "penetrations", "m2", 37.145, "51.114", SSR["51.114"]["completed"], A,
  "[A] As W-01")
b(SEC_F, "W-05", "WP-02 protection screed 100 over the roof membrane (also "
  "cover layer 1)", "m2", 102.889, "—", None, X,
  "THE SAME WORK AS B-screed, measured in m2 instead of m3.  Paid once, at "
  "B-screed.  102.889 x 0.100 = 10.289 m3")
b(SEC_F, "W-06", "WP-06 headhouse and stairwell roofs, external grade + "
  "protection", "m2", 41.44, "51.114 + 51.115", DERIVED["MEMBRANE_PROT"], A,
  "[A] Membrane plus the SSR's own 20 mm mechanical protective layer")
b(SEC_F, "W-08", "WP-04 internal wet-area tanking, floors", "m2", 26.8,
  "31.09", SSR["31.09"]["completed"], A,
  "[A] Acrylic polymer modified cement-based coating with fibre glass mesh — "
  "the SSR's tanking-under-finish item.  WP-04 names no product")
b(SEC_F, "W-09", "WP-04 internal wet-area tanking, walls, 2.000 high", "m2",
  81.44, "31.09", SSR["31.09"]["completed"], A, "[A] As W-08")
b(SEC_F, "W-10", "Waterstops, 2 No. at every construction joint (WP-05), "
  "~6 m centres", "m", 109.76, "—", None, N,
  "NOT PRICED.  THE SSR HAS NO WATERSTOP ITEM ANYWHERE IN 624 PAGES — "
  "searched for waterstop, water stop, water bar and PVC water bar.  "
  "Section B: the rate is to be approved by the Superintending Engineer.  "
  "The joint positions are also not fixed in the project ([A] in WM1)")

SEC_G = "G · SENTRY POST — CONCRETE AND FRAME  (M30)"

b(SEC_G, "SC-01", "Sentry post: Footings F1, 4 No., 1500 x 1500 x 600", "m3",
  5.4, "25.15", SSR["25.15"]["completed"], P, "M-30 foundations and footings")
b(SEC_G, "SC-02", "Sentry post: Columns C1, 4 No., 350 x 350, (-)1.400 to +6.700",
  "m3", 3.969, "25.35", SSR["25.35"]["completed"], P,
  "M-30 columns.  No floor lift applied — a column is cast in one pour from "
  "its base")
b(SEC_G, "SC-03", "Sentry post: Plinth beam PB 250 x 400, 15.200 m clear", "m3",
  1.52, "25.54", SSR["25.54"]["completed"], P, "M-30 beams, ground level")
b(SEC_G, "SC-04.1", "Sentry post: Beams B1 / B2 250 x 450, first-floor level",
  "m3", 1.14, "25.54", DERIVED["M30_BEAM_FF"], P,
  "Half of WM1 item SC-04 (2.28 m3 at two levels).  +1 % first-floor lift")
b(SEC_G, "SC-04.2", "Sentry post: Beams B1 / B2 250 x 450, roof level", "m3",
  1.14, "25.54", DERIVED["M30_BEAM_FF"], P, "The other half.  +1 % floor lift")
b(SEC_G, "SC-05", "Sentry post: Slab S1 150, first floor, 4.000 x 5.000", "m3",
  3.0, "25.74", DERIVED["M30_SLAB_FF"], P, "M-30 slabs, +1 % first-floor lift")
b(SEC_G, "SC-06", "Sentry post: Slab S1 150, roof, 4.600 x 5.600 incl. the 300 "
  "projection", "m3", 3.864, "25.74", DERIVED["M30_SLAB_FF"], P,
  "M-30 slabs, +1 % floor lift.  The SSR table runs ground / first / second / "
  "third / fourth; the roof of a G+1 is read as the first-floor band")
b(SEC_G, "SC-07", "Sentry post: Parapet 300 high x 150 thk over the roof "
  "projection", "m3", 0.918, "26.19 der.", DERIVED["PARDI_M30_FF"], A,
  "[A] Pardi grade-uplifted M25 -> M30, +1 % floor lift.  The 150 thickness "
  "is [A] in WM1 and that tag is carried, not resolved")
b(SEC_G, "SC-08", "Sentry post ground floor slab on grade — PROVISIONAL, not "
  "designed", "m2", 16.56, "—", None, N,
  "NOT PRICED.  Thickness and specification are to be confirmed — WM1 tags "
  "this [N] and no rate can be chosen without them")
b(SEC_G, "SC-09", "Sentry post: blinding / PCC M15 100 thk under F1, 4 No.",
  "m3", 1.156, "24.04", SSR["24.04"]["completed"], P, "As C-09")
b(SEC_G, "SC-10", "Sentry post: external spiral stair, 1000 R, 250 dia central "
  "pole", "item", 1, "—", None, N,
  "NOT PRICED.  THE SSR HAS NO SPIRAL STAIR ITEM, and the fabrication detail "
  "is not in the project record.  SSR 40.06, SS 304 handrail at "
  "Rs 1 220/m, is the only related published item and cannot stand for the "
  "stair.  Section B: Superintending Engineer to approve the rate")

SEC_H = "H · SENTRY POST — BRICK MASONRY AND FINISHES  (design change SP-B1)"

b(SEC_H, "SP-01", "Brick masonry, ground storey, 190 thk in a 200 zone, CM 1:6, "
  "incl. scaffolding", "m3", 6.876, "27.05", SSR["27.05"]["completed"], A,
  "[A] Mortar CM 1:6 and location (superstructure) match SSR 27.05 exactly.  "
  "SP-B1 specifies modular bricks CLASS 10 to IS 1077.  THE SSR PUBLISHES NO "
  "FIRST-CLASS ITEM FOR SUPERSTRUCTURE WALLS AT ALL — chapter 27 offers "
  "first class only in plinth (27.02) and in pillars (27.08, 27.09) — so "
  "27.05 is the only published superstructure brick wall item and it governs "
  "whatever class the bricks are.  The SSR's first / second class is a "
  "workmanship grading and does not map onto IS 1077 strength classes.  "
  "OPEN ITEM WM4-V2")
b(SEC_H, "SP-02", "Brick masonry, first storey, 190 thk in a 200 zone, CM 1:6, "
  "incl. scaffolding", "m3", 5.32, "27.05", DERIVED["BRICK_FF"], A,
  "[A] As SP-01, +1 % first-floor lift")
b(SEC_H, "SP-03", "Modular burnt clay bricks class 10 to IS 1077, delivered",
  "No.", 6402.952, "—", None, X,
  "INCLUDED in SP-01 / SP-02 — SSR 27.05 is a composite supply-and-lay rate.  "
  "SSR general material rate for II class brick is Rs 8.50 each, so this "
  "quantity carries about Rs 54 425 of material INSIDE the masonry rate")
b(SEC_H, "SP-04", "Cement for masonry mortar CM 1:6", "bag", 14.458, "—", None, X,
  "INCLUDED in SP-01 / SP-02.  SSR general rate Rs 6 000 / M.T. = Rs 300 / bag")
b(SEC_H, "SP-05", "Sand for masonry mortar, to IS 2116", "m3", 3.012, "—", None, X,
  "INCLUDED in SP-01 / SP-02.  SSR general rate, crushed sand, Rs 1 200 / m3")
b(SEC_H, "SP-06", "RC lintels over openings, 200 x 150 — PROVISIONAL section",
  "m3", 0.51, "25.54", SSR["25.54"]["completed"], A,
  "[A] M-30 beams and lintels.  THE SECTION IS SUPERSEDED: design revision "
  "SP-B2 (master A.4.8 / H.12) designs lintel L1 at 190 x 150, and "
  "WM_RECONCILIATION_REGISTER section 6 records that this bill line still "
  "measures the superseded 200 x 150.  WM4 does NOT re-measure it — the "
  "quantity is WM1's and stays WM1's.  OPEN ITEM WM4-V3")
b(SEC_H, "SP-07", "Internal cement plaster 12 mm, CM 1:4", "m2", 125.15,
  "32.04", SSR["32.04"]["completed"], P,
  "Thickness, mortar and location all match the SSR item exactly.  WM1's "
  "description says 'sand faced'; sand facing is an EXTERNAL finish in the "
  "SSR (32.11) and 12 mm internal CM 1:4 is 32.04.  Priced as internal")
b(SEC_H, "SP-08", "External cement plaster 15 mm, two coat", "m2", 97.39,
  "32.11", SSR["32.11"]["completed"], P,
  "SSR 32.11 sand faced external: 15 mm base coat in CM 1:4 plus a finishing "
  "coat — the specified two-coat 15 mm work exactly")
b(SEC_H, "SP-09", "Flooring, ground and first floor, 3.600 x 4.600 each", "m2",
  33.12, "33.24", None, N,
  "NOT PRICED.  NO FLOORING SPECIFICATION EXISTS IN THE PROJECT (WM1 tags it "
  "[N]).  For information only, and NOT in the total: SSR 33.24 matt ceramic "
  "300 x 300 is Rs 1 182 / m2, which would be Rs 39 147")
b(SEC_H, "SP-10.1", "Painting, INTERNAL — plastic emulsion, two coats", "m2",
  125.15, "36.12", SSR["36.12"]["completed"], A,
  "[A] WM1 item SP-10 is one 222.54 m2 line for internal and external "
  "together.  It splits EXACTLY on the two plaster areas — 125.15 + 97.39 = "
  "222.54 — so the split is arithmetic, not judgement.  The paint SYSTEM is "
  "assumed: WM1 records the specification as not in the project")
b(SEC_H, "SP-10.2", "Painting, EXTERNAL — exterior acrylic emulsion, two coats",
  "m2", 97.39, "35.25", SSR["35.25"]["completed"], A, "[A] As SP-10.1")
b(SEC_H, "SP-11", "Door D1 900 x 2100, 2 No. (ground and first floor)", "m2",
  R(2 * 0.900 * 2.100), "39.10", SSR["39.10"]["completed"], A,
  "[A] SHUTTER ONLY — the SSR bills the frame as a separate item and no "
  "frame specification exists.  The door TYPE is not in the project either; "
  "a 32 mm commercial flush shutter is assumed.  Height 2100 is [A] in WM1")
b(SEC_H, "SP-12", "Window W1 1200 wide, ground storey, 1 No.", "No.", 1,
  "39.50", None, N,
  "NOT PRICED.  THE HEIGHT IS NOT STATED ANYWHERE IN THE PROJECT ([N] in "
  "WM1), so there is no area to price.  SSR 39.50 aluminium openable window "
  "is Rs 5 700 / m2 when a height exists")
b(SEC_H, "SP-13", "Armoured vision panels 1200 wide, 8 No., first storey — "
  "SPECIALIST", "No.", 8, "—", None, N,
  "NOT PRICED and NOT IN THE SSR.  An armoured vision panel is not a "
  "schedule item.  Specification is not in the project either")

SEC_I = "I · ELECTRICAL AND EMP INSTALLATION"

for _c, _d in [
        ("EL-01", "Conduits, boxes and concealed work, cast into RC — builder's work"),
        ("EL-02", "Cabling, distribution board and final circuits"),
        ("EL-03", "EMP Zone 2 shielded enclosure, bay 3 — SPECIALIST"),
        ("EL-04", "Earthing installation, 5 ohm target, IS 3043"),
        ("EL-05", "Lighting, small power and emergency lighting"),
        ("EL-06", "Generator connection, changeover and protection"),
        ("EL-07", "EMP protection to every service penetration (power PCI, "
                  "waveguide-below-cutoff, fibre)")]:
    b(SEC_I, _c, _d, "item", None, "—", None, N,
      "NOT PRICED.  NO ELECTRICAL DESIGN PACKAGE EXISTS — no quantity, and "
      "for EL-03 and EL-07 no SSR item either.  The SSR's water-supply and "
      "sanitary chapters 41-43 hold no EMP or shielding item of any kind")

SEC_J = "J · PRINCIPAL MATERIALS — PROCUREMENT VOLUMES"

b(SEC_J, "M-01", "Cement, OPC 43 grade to IS 269, all works", "t", 194.169,
  "—", None, X,
  "PROCUREMENT MEMORANDUM, NOT A PAYABLE ITEM — cement is inside every "
  "composite rate above.  At the SSR general rate of Rs 6 000 / M.T. this "
  "volume carries Rs 1 165 014 of cement INSIDE those rates")
b(SEC_J, "M-02", "Coarse and fine aggregate to IS 383, all concrete", "t",
  828.661, "—", None, X,
  "PROCUREMENT MEMORANDUM.  Inside the composite rates.  SSR general rates: "
  "20 mm aggregate Rs 1 050 / m3, crushed sand Rs 1 200 / m3")
b(SEC_J, "M-03", "Water for concrete, mortar and curing — site supply", "item",
  None, "—", None, X,
  "PROCUREMENT MEMORANDUM.  Curing and watering are inside every SSR item.  "
  "SSR general rate for water is Rs 213 / 1 000 litre")

SEC_K = "K · ITEMS ADDED BY OWNER RULING RC4 (master H.28)"

b(SEC_K, "RC4-01", "Strip expansive CH horizon to 1.000 m below existing ground "
  "under and 1.000 m beyond the entry stairwell stepped raft, cart away and "
  "dispose", "m3", 8.0, "21.02", SSR["21.02"]["completed"], P,
  "RC4 recorded this as '[A] NOT PRICED' because no rate existed.  A RATE "
  "NOW EXISTS.  The QUANTITY tag stays [R] and the ruling is untouched — "
  "only the rate column is filled")
b(SEC_K, "RC4-02", "Supply and place free-draining granular replacement fill, "
  "FSI <= 20 % to IS 2720 Pt XL, in 200 mm layers compacted to >= 95 % MDD, "
  "incl. 50 mm sand blinding", "m3", 8.0, "21.37", SSR["21.37"]["completed"], P,
  "As RC4-01.  SSR 21.37 is filling with contractor's material in 15-20 cm "
  "layers, watered and compacted — the specified work, at a TIGHTER layer "
  "thickness than the schedule assumes")

SEC_L = "L · PROTECTIVE PLANT, CLOSURES AND SERVICES — OUTSIDE THE SSR"

for _c, _d, _u, _q in [
        ("Z-01", "Blast Doors 1 and 2, >= 7 bar, rebound-rated", "set", 2),
        ("Z-02", "Emergency exit hatches, 900 clear, 621 kPa", "set", 2),
        ("Z-03", "Fast-acting blast valves BV-1 to BV-3 (DN100)", "set", 3),
        ("Z-04", "Generator blast valves BV-4 and BV-5 (DN350)", "set", 2),
        ("Z-05", "NBC collective protection trains, 2 x 300 m3/h", "set", 2),
        ("Z-06", "Sealed Zone-2 welded EMP enclosure, 3 x 3 x 2.4 m", "item", 1),
        ("Z-07", "Submersible sump pumps, effluent piping and septic", "set", 1),
        ("Z-08", "Standby generator 15 kVA in bay 8, fuel system, exhaust and "
                 "acoustic treatment", "set", 1),
        ("Z-09", "Testing, commissioning and envelope leakage test", "item", 1)]:
    b(SEC_L, _c, _d, _u, _q, "—", None, N,
      "NOT IN THE WM1 BILL AND NOT IN THE SSR.  Recorded here so the estimate "
      "is honest about its boundary: the owner's own bill (Cost/USER_BOQ_*, "
      "Cost/REVISED_BOQ_*_RC1) prices these from vendor figures.  SSR General "
      "Notes Section B: 'The items for which rates are not included in State "
      "Schedule of Rates, the rates shall be approved by concerned "
      "Superintending Engineer, PWD'")


SECTIONS = [SEC_A, SEC_B, SEC_C, SEC_D, SEC_E, SEC_F, SEC_G, SEC_H, SEC_I,
            SEC_J, SEC_K, SEC_L]


# ===========================================================================
#  RECAPITULATION
# ===========================================================================

def totals():
    t = {"P": 0.0, "A": 0.0}
    for r in BILL:
        if r["tier"] in t and r["amount"]:
            t[r["tier"]] += r["amount"]
    t["ITEMS"] = t["P"] + t["A"]
    return t


# Recapitulation heads.  The first block is the SSR's OWN Section B; the second
# is the project owner's provision structure, carried from their RC1 estimate
# and clearly separated because it is NOT part of the schedule of rates.
#   (head, basis, percent or None, source)
RECAP_SSR = [
    ("Total of items — SSR 2022-23 completed rates, excluding GST",
     "sum of the priced bill", None, "this bill"),
    ("Insurance of project / work facility",
     "1.00 % — work value above Rs 25.00 lakh", 0.0100,
     "SSR General Notes Section B (i) A"),
    ("Labour insurance",
     "1.00 % — work value above Rs 25.00 lakh", 0.0100,
     "SSR General Notes Section B (i) B"),
    ("Material testing charges",
     "SSR chapter 18, Testing Charges and Frequency of Test", None,
     "NOT QUANTIFIED — the test schedule is priced per test and the "
     "frequencies depend on delivered lot sizes"),
    ("GST on works contract", "18 % [A]", 0.18,
     "SSR requires a separate provision in the recapitulation sheet but does "
     "NOT fix the rate.  18 % is the standard works-contract rate and is "
     "tagged [A].  Change the one parameter cell to test another rate"),
]

RECAP_OWNER = [
    ("Contingencies", 0.03),
    ("Water and electricity provisions", 0.01),
    ("Specialist CBRN / EMP and engineering consultant", 0.06),
    ("Site supervision and quality assurance", 0.02),
    ("Statutory clearances and liaisoning", 0.01),
]

NOT_ADDED = [
    ("Contractor's overhead", 0.10,
     "ALREADY INSIDE EVERY SSR COMPLETED RATE.  General Notes: 'For labour "
     "amenities and all other overhead charges, 10 % provision is considered "
     "in Rate Abstract'"),
    ("Contractor's profit", 0.10,
     "ALREADY INSIDE EVERY SSR COMPLETED RATE.  General Notes: 'In addition, "
     "10 % provision for Contractor's Profit is also considered separately'"),
    ("Labour cess", 0.01,
     "ALREADY INSIDE EVERY SSR COMPLETED RATE.  General Notes, Govt. Circular "
     "SSR-1090/CR-6453/PLN-3 dt. 14.07.1993: 'Labour Cess at 1 % has been "
     "considered separately in Rate Abstracts'"),
]
