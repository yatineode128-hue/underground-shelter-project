"""
wm4_owner_compare.py — the project owner's own priced bill, re-rated at SSR 2022-23.

Works Management revision WM4.

The owner supplied a priced bill (WM2, master H.13) and RC1 revised it (WM3,
master H.15).  Those rates came from the owner, not from any published schedule:
master H.15 records "No cost was re-estimated, no rate was checked against a
market or a schedule of rates."  This module does exactly that check, line by
line, against the SSR the owner has now supplied.

NOTHING IN THE OWNER'S BILL IS EDITED.  Their quantities and their rates are
reproduced as given; the SSR rate sits beside them.  Where the SSR has no item,
the row says so and no figure is invented.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from wm4_ssr_library import SSR
from wm4_bill import DERIVED

# (part, owner description, unit, qty, owner rate, ssr item, ssr rate, note)
# ssr rate None  -> not comparable / not in the SSR
INC = "INCLUDED IN THE SSR CONCRETE RATE"

COMPARE = [
 ("I", "Confirmatory soil and rock core boreholes", "No", 4, 50000, "—", None,
  "Not comparable.  The SSR's site-investigation items are road trial pits, "
  "not cored boreholes"),
 ("I", "Site clearance, grubbing and setting out", "m2", 1800, 44.8, "21.33",
  SSR["21.33"]["completed"], "SSR clearance is a labour-only item at Rs 7/m2"),
 ("I", "Mass excavation in basalt / murum (~6.8 m)", "m3", 1539, 850, "21.20",
  SSR["21.20"]["completed"],
  "SSR 21.20, hard rock by chiselling, BEFORE the Section B depth increases "
  "of +20 % and +30 % that a 6.8 m excavation attracts.  The owner's single "
  "blended Rs 850 covers both murum and basalt"),
 ("I", "Surface dressing and anti-termite treatment", "m2", 320, 180, "21.22",
  SSR["21.22"]["completed"], "IS 6313 Part II, bottom and sides of excavation"),

 ("II", "Formwork for mat raft and bay 5 sump", "m2", 125, 410, "—", None, INC),
 ("II", "PCC 1:3:6 levelling bed (100 mm)", "m3", 17.17, 5500, "24.01",
  SSR["24.01"]["completed"],
  "The SSR's consumption table gives 1:3:6 and M-10 the same 4.40 bags/m3.  "
  "The project's own bill (C-09 / C-10) specifies M15, which is 24.04 at "
  "Rs 6 359 — the two bills differ on the blinding grade"),
 ("II", "Monolithic mat raft casting (M35)", "m3", 81.84, 8640, "25.17",
  SSR["25.17"]["completed"], "Raft foundations, M-35.  Formwork inside both rates"),
 ("II", "Pre-applied waterproofing membrane + screed", "m2", 280, 950,
  "51.114 + 51.115", SSR["51.114"]["completed"] + SSR["51.115"]["completed"],
  "Polymeric HMHDPE membrane plus the SSR's 20 mm protective screed"),
 ("II", "Dual swelling hydrophilic kicker waterstops", "m", 68, 650, "—", None,
  "NOT IN THE SSR — no waterstop item exists in the schedule"),

 ("III", "Formwork for 600 mm shear walls (3.2 m ht)", "m2", 480, 580, "—",
  None, INC),
 ("III", "Casting 600 mm perimeter and shear walls (M35)", "m3", 132.61, 8640,
  "26.19 der.", DERIVED["PARDI_M35"],
  "R.C.C. pardi (wall) uplifted M25 -> M35.  THE LARGEST SINGLE RATE GAP IN "
  "THE BILL: wall formwork is what the SSR item is dear for"),
 ("III", "Formwork and staging for 900 mm pressure slab", "m2", 145, 650, "—",
  None, INC),
 ("III", "Casting 900 mm pressure roof slab (M35)", "m3", 114.72, 8640,
  "25.76", SSR["25.76"]["completed"], "R.C.C. slabs and landings, M-35"),
 ("III", "Internal dog-leg staircase RCC", "m3", 4.8, 9200, "26.26 der.",
  DERIVED["WAIST_M35"], "Waist slab and steps, uplifted M25 -> M35"),
 ("III", "Headhouse structure (400 mm wall / 500 mm roof)", "m3", 28.56, 8640,
  "26.19 der. / 25.76", None,
  "Two SSR items apply — walls at the derived pardi rate, roof at 25.76.  "
  "The owner bills them as one line, so no single SSR rate can stand against "
  "it.  The project's own bill splits them at C-06.1 / C-06.2"),
 ("III", "Approach stairwell RC box (250 mm RC)", "m3", 18.2, 8640,
  "26.19 der.", DERIVED["PARDI_M35"], "Priced at the wall rate, as C-08"),
 ("III", "Engineered burster slab (200 mm M30 — RC1 R-1)", "m3", 38.4, 8200,
  "25.15", SSR["25.15"]["completed"],
  "Ground-supported slab on the rubble layer, so the M-30 raft item.  RC1 "
  "flagged this rate [REVIEW] after the grade changed; the SSR answers it"),
 ("III", "Sentry post RC frame — brick infill measured as brickwork (RC1 R-6)",
  "m3", 18.6, 8500, "25.15 / 25.35 / 25.54 / 25.74", None,
  "Four SSR items apply to a frame — footings, columns, beams, slabs — at "
  "Rs 7 471 to Rs 14 299.  The project's own bill splits them at SC-01 to "
  "SC-07.  One blended rate cannot be checked against one SSR rate"),
 ("III", "110 mm internal brick partition walls", "m2", 95, 920, "27.06",
  SSR["27.06"]["completed"],
  "Half-brick thick wall in CM 1:4 with hoop-iron reinforcement.  NOTE: the "
  "project's own W8 partitions (C-14) are 110 REINFORCED CONCRETE with A252 "
  "mesh both faces, not brick — the two bills describe different work"),
 ("III", "Escape shaft collars ESC 1 and ESC 2, 250 RC, OD 1900 (RC1 R-7)",
  "m3", 6.285, 8640, "26.19 der.", DERIVED["PARDI_M35"], "As C-12"),

 ("IV", "Pressure roof slab rebar (T25 / T12)", "t", 23.22, 78000, "26.33",
  SSR["26.33"]["completed"], "TMT Fe-500 fixed in position"),
 ("IV", "Perimeter and shear wall rebar (T16 / T20)", "t", 17.85, 78000,
  "26.33", SSR["26.33"]["completed"], "As above"),
 ("IV", "Mat raft and haunch diagonal rebar", "t", 13.14, 78000, "26.33",
  SSR["26.33"]["completed"], "As above"),
 ("IV", "Headhouse, approach and staircase steel", "t", 6.76, 78000, "26.33",
  SSR["26.33"]["completed"], "As above"),
 ("IV", "Burster slab mesh (T12 @ 150 B/W)", "t", 2.89, 78000, "26.33",
  SSR["26.33"]["completed"],
  "The RC1 [REVIEW] on this line is a QUANTITY question and the SSR does not "
  "touch it — only the rate is compared here"),
 ("IV", "Sentry post structural rebar", "t", 3.93, 78000, "26.33",
  SSR["26.33"]["completed"], "As above"),
 ("IV", "EMP welding at 4th node and bonding straps", "item", 1, 380000, "—",
  None, "NOT IN THE SSR"),

 ("V", "Blast doors 1 and 2 (>= 7 bar, rebound-rated)", "set", 2, 1250000, "—",
  None, "NOT IN THE SSR"),
 ("V", "Emergency exit hatches (900 clear, 621 kPa)", "set", 2, 450000, "—",
  None, "NOT IN THE SSR"),
 ("V", "Fast-acting blast valves BV-1 to BV-3 (DN100)", "set", 3, 160000, "—",
  None, "NOT IN THE SSR"),
 ("V", "Generator blast valves BV-4 and BV-5 (DN350)", "set", 2, 320000, "—",
  None, "NOT IN THE SSR"),
 ("V", "NBC collective protection trains (2 x 300 m3/h)", "set", 2, 1850000,
  "—", None, "NOT IN THE SSR"),
 ("V", "Sealed Zone-2 welded EMP enclosure (3 x 3 x 2.4 m)", "item", 1, 850000,
  "—", None, "NOT IN THE SSR"),
 ("V", "Layerwise engineered fill and basalt rubble berm", "m3", 620, 420,
  "21.37 / 21.38", SSR["21.37"]["completed"],
  "Compared at the engineered-fill item 21.37.  The rubble part of the same "
  "owner line is 21.38 at Rs 1 382"),
 ("V", "Submersible sump pumps + effluent piping + septic", "set", 1, 420000,
  "—", None, "NOT IN THE SSR in this form"),
 ("V", "Sand-faced internal plaster, punning and painting", "m2", 720, 180,
  "32.04 + 32.15 + 36.12",
  SSR["32.04"]["completed"] + SSR["32.15"]["completed"] + SSR["36.12"]["completed"],
  "Three SSR items make up this one owner line: 12 mm internal plaster CM 1:4 "
  "(Rs 278) + neeru finish, which is what punning is (Rs 65) + two coats of "
  "plastic emulsion (Rs 80) = Rs 423"),
 ("V", "Testing, commissioning and envelope leakage test", "item", 1, 250000,
  "—", None, "NOT IN THE SSR"),
]
