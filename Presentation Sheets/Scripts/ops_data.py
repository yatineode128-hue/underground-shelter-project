"""
ops_data.py  --  every value that FLS012 (SHEET 12, fire and life safety) and
WMS013 (SHEET 13, works management) draw or print.

SOURCES, in order of authority
    master/MASTER_PROJECT_STATE.md  A.3, A.4.3 - A.4.9 (and the RC4 ruling on
                                    the escape-shaft ladders), H.15 (WM3)
    Fire and Life Safety/Scripts/fs_data.py   the escape-route geometry and
                                              distances, all computed from
                                              mep_proj, not typed
    Drainage/Scripts/mep_proj.py              the reconciled geometry
    WORKS MANAGEMENT/Cost/REVISED_*_RC1.csv   the WM3 revised bill and cost
                                              summary, read at build time
    WORKS MANAGEMENT/Programme/REVISED_MASTER_CONSTRUCTION_SCHEDULE_R1.csv

WHICH WORKS MANAGEMENT REVISION.  SHEET 13 presents **WM3**, the revised owner
package of master H.15, whose final project cost is Rs 2,97,90,913.  It is NOT
WM4, the later bill priced from the Maharashtra SSR 2022-23, whose total is a
different figure on a different basis.  Nothing is re-derived here: every
amount, quantity, date and duration is read from the WM3 output files.

THE LADDER.  fs_data still carries FS-6 / FS-V7 as "no ladder specified".  That
was superseded by the RC4 ruling of 11 September 2026 (master A.4.9 and H.28):
ladder only, fall-arrest deferred.  SHEET 12 therefore draws and schedules the
RULED ladder and does not reproduce the superseded finding text.

MAIN STAIRCASE IS FROZEN and is read from mep_proj.STAIR.  Route R1 uses it and
changes nothing about it.
"""
import csv
import os

import fs_data as F
import mep_proj as P

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
WM = os.path.join(ROOT, "WORKS MANAGEMENT")

IDENTITY = [
    "UNDERGROUND CBRN-HARDENED",
    "BLAST-RESISTANT PROTECTIVE",
    "STRUCTURE + SENTRY POST",
    "PUNE, MAHARASHTRA",
]
PROJECT_LINES = ["CBRN HARDENED", "UG OPS ROOM"]
DATE = "18 SEP 2026"
DRAWN = "SYN 01"
CHECKED = "DR IR CHAUDHARI"

# ===================================================== SHEET 12  geometry
BOX, INTR = P.BOX, P.INT
BAYS, IW, PARTITIONS = P.BAYS, P.IW, P.PARTITIONS
PART_DOOR_Y, BLAST_DOOR = P.PART_DOOR_Y, P.BLAST_DOOR
ESC, ESC_CLEAR_D, ESC_COLLAR_OD = P.ESC, P.ESC_CLEAR_D, P.ESC_COLLAR_OD
VOID, PAD, STAIR = P.VOID, P.PAD, P.STAIR
HH, HH_DOOR, ASW = P.HH, P.HH_DOOR, P.ASW
L_FLOOR, L_SLAB_TOP, L_ROOF_SOF = (P.LVL["floor"], P.LVL["slab_top"],
                                   P.LVL["roof_soffit"])

SPINE_Y = F.SPINE_Y                  # 2950, the centre of the 900 door gaps
BDOOR_Y = F.BDOOR_Y                  # 1200, the blast-door centreline
R1 = F.R1_SPINE + F.R1_W5[1:] + F.R1_TO_DOOR[1:] + F.R1_STAIR[1:]
R2 = F.R2
R3 = F.R3
R3_FROM_BD2 = F.R3_FROM_BD2
ENTRY_ROUTE = F.ENTRY_ROUTE
TRAVEL_R1, TRAVEL_R2, TRAVEL_R3 = F.TRAVEL_R1, F.TRAVEL_R2, F.TRAVEL_R3
CLIMB_R1, CLIMB_R2, CLIMB_R3 = F.CLIMB_R1, F.CLIMB_R2, F.CLIMB_R3
TRAVEL_ENTRY = F.TRAVEL_ENTRY
SPINE_LEN = F.SPINE_LEN

# ---- escape-route schedule.  Kept to five columns so that every cell fits
# the 178 mm schedule column at the package's 1.70 mm text floor.
ESCAPE_ROUTES = [
    ["R1", "PRIMARY - MAIN STAIR", f"{TRAVEL_R1:.1f} m", f"{CLIMB_R1:.3f} m",
     "BAY 7 SHAFT, HEADHOUSE, THEN 12R TO THE ENTRY DOOR AT GRADE"],
    ["R2", "ESCAPE SHAFT ESC 1", f"{TRAVEL_R2:.2f} m", f"{CLIMB_R2:.3f} m",
     "BAY 1, (2050, 2050), 1400 DIA. HEAD +0.150"],
    ["R3", "ESCAPE SHAFT ESC 2", f"{TRAVEL_R3:.2f} m", f"{CLIMB_R3:.3f} m",
     "BAY 8, (19900, 2050), 1400 DIA. HEAD +0.700"],
    f"R1 USES THE MAIN STAIRCASE:  {STAIR['risers']}R AT "
    f"{STAIR['riser']:.4f},  TREAD {STAIR['tread']:.0f},  "
    f"{STAIR['flights']} FLIGHTS OF {STAIR['per_flight']},  TOTAL RISE "
    f"{STAIR['total_rise']:.0f},  WIDTH {STAIR['width']:.0f},  HEADROOM "
    f"{STAIR['headroom']:.0f}",
]

EMERGENCE = [
    ["R1", "ENTRY DOOR, COVERED STAIRWELL", "1000 x 2100", "0.000",
     "OPENS OUTWARD. OUTSIDE THE BOUNDARY"],
    ["R2", "ESC 1 HEAD, BAY 1", "1400 DIA", "+0.150",
     "6.250 m CLIMB ON THE LADDER"],
    ["R3", "ESC 2 HEAD, BAY 8", "1400 DIA", "+0.700",
     "6.800 m CLIMB ON THE LADDER"],
]

# ---- the evacuation decision rule, as drawn on view 4
DECISION = [
    ["BAY 8, GENERATOR", "R1;  R2 IF THE SPINE IS SMOKE-LOGGED",
     "BLAST DOOR 2 SHUT.  DO NOT USE R3"],
    ["BAYS 1 TO 6, OCCUPIED", "R1 IF BAY 7 IS CLEAR",
     "OTHERWISE R2 FROM THE WEST, R3 FROM THE EAST"],
    ["BAY 7, STAIR SHAFT", "R2 OR R3",
     "BOTH BLAST DOORS SHUT.  R1 IS THE FIRE"],
    ["HEADHOUSE OR STAIRWELL", "R2 OR R3", "R1'S SURFACE END IS BLOCKED"],
]


# ---- the escape-shaft ladder, as ruled by RC4 (master A.4.9 / H.28)
LADDER = [
    ["RUNGS", "20 DIA GALVANISED MS", "400 CLEAR WIDTH",
     "EQUAL PITCH WITHIN EACH SHAFT"],
    ["PITCH, ESC 1", "297.6 mm", "21 SPACES", "6.250 m CLIMB"],
    ["PITCH, ESC 2", "295.7 mm", "23 SPACES", "6.800 m CLIMB"],
    ["STRINGERS", "2 No. 50 x 10 GALVANISED FLAT", "-",
     "CAST-IN LUGS TO THE 250 COLLAR AND THE ROOF-SLAB BORE"],
    ["BRACKETS", "EXPANSION ANCHORED", "1.5 m CENTRES",
     "OVER THE LOWER 3.200 m"],
    ["CLEARANCES", "200 OR MORE BEHIND THE RUNG",
     "750 OR MORE CLIMBING SPACE IN FRONT", "GRAB RAILS 1100 ABOVE THE HEAD"],
]

# ---- fire compartments, from the plan's own findings, stated as fact
COMPARTMENTS = [
    ["C1", "BAYS 1 - 6, THE OCCUPIED ZONE  (U-01 TO U-06)",
     "ONE SMOKE COMPARTMENT; THE FOUR W8 GAPS ARE PERMANENT"],
    ["C2", "BAY 7, THE STAIR SHAFT  (U-07)",
     "BOUNDED BY BLAST DOOR 1 IN W6 AND BLAST DOOR 2 IN W7"],
    ["C3", "BAY 8, GENERATOR AND ESC 2  (U-08)",
     "THE LIKELIEST FIRE LOAD IN THE SHELTER; ESC 2 IS INSIDE IT"],
    "BLAST DOORS 1 AND 2 ARE THE ONLY REAL BARRIERS BETWEEN THE THREE "
    "COMPARTMENTS.  W5 IS DESIGNATED FIRE AND GAS-TIGHT.",
]

# ===================================================== SHEET 13  works mgmt
def _rows(path):
    with open(os.path.join(WM, path), newline="") as fh:
        return [r for r in csv.reader(fh) if r]


def _money(v):
    """Indian grouping, the convention the owner's own estimate uses."""
    n = int(round(float(v)))
    s = str(n)
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    out = []
    while len(head) > 2:
        out.insert(0, head[-2:])
        head = head[:-2]
    if head:
        out.insert(0, head)
    return ",".join(out) + "," + tail


_COST = _rows("Cost/REVISED_COST_SUMMARY_RC1.csv")[1:]
COST_SUMMARY = [[r[0], r[1], _money(r[2])] for r in _COST]
FINAL_COST = _money(_COST[-1][2])
BASIC_COST = _money(_COST[0][2])

_BOQ = _rows("Cost/REVISED_BOQ_PRICED_RC1.csv")[1:]
_ITEMS = [r for r in _BOQ if len(r) > 8 and r[1]]


def _part_totals():
    out, seen = [], []
    for r in _ITEMS:
        if r[0] not in seen:
            seen.append(r[0])
    for p in seen:
        rs = [r for r in _ITEMS if r[0] == p]
        tot = sum(float(r[8]) for r in rs)
        out.append((p, len(rs), tot))
    return out


PART_TOTALS = _part_totals()
PART_SUMMARY = [[p.replace("PART ", "").split(" - ")[0],
                 p.split(" - ", 1)[1] if " - " in p else p,
                 str(n), _money(t)] for p, n, t in PART_TOTALS]

def _short(desc, n=62):
    """The bill's own description, trimmed to the column without inventing
    words.  Nothing is reworded; a long description is cut at a word break and
    marked, and the full text stays in the bill itself."""
    d = " ".join(desc.split())
    if len(d) <= n:
        return d
    cut = d[:n].rsplit(" ", 1)[0]
    return cut + " ..."


def _rate(r):
    """The bill's rate, or '-' where the bill carries no rate for the line."""
    v = r[5].strip()
    return v if v and v.replace(".", "").isdigit() else "-"


def _amount(r):
    v = float(r[8] or 0)
    return _money(v) if v else "NOT PRICED"


# The whole measured bill, 38 items under the five part headings.  Each part
# heading is a full-width band carrying its own item count and total.
BOQ_ITEMS = []
for _p, _n, _tot in PART_TOTALS:
    BOQ_ITEMS.append(f"{_p}          {_n} ITEMS          "
                     f"Rs {_money(_tot)}")
    for _r in (x for x in _ITEMS if x[0] == _p):
        BOQ_ITEMS.append([_r[1], _short(_r[2]), _r[3], _r[4], _rate(_r),
                          _amount(_r)])

PRINCIPAL_ITEMS = [
    [_short(r[2], 58), r[3], r[4], _money(r[8])]
    for r in sorted(_ITEMS, key=lambda r: -float(r[8]))[:12]
]

_PROG = _rows("Programme/REVISED_MASTER_CONSTRUCTION_SCHEDULE_R1.csv")[1:]
PROG = {r[0]: r for r in _PROG}
PROG_START, PROG_FINISH = PROG["1"][3], PROG["1"][4]
PROG_DAYS = PROG["1"][2]

# the bars drawn on the programme chart: the four top-level phases and the
# sub-summaries the owner's own outline carries under them
GANTT_IDS = ["1", "2", "6", "11", "14", "27", "28", "42", "52", "55", "68",
             "81", "86", "87", "92", "99", "112", "125"]
GANTT = [(PROG[i][1], PROG[i][2], PROG[i][3], PROG[i][4]) for i in GANTT_IDS]

MILESTONES = [[PROG[i][1][:54], PROG[i][2], PROG[i][3], PROG[i][4]]
              for i in ("2", "6", "27", "86")]

# The programme as a table: the master line, the four phases and the
# sub-summaries the owner's own outline carries under them.
PHASE_IDS = {"1", "2", "6", "27", "86"}
PROGRAMME_ROWS = [
    [i,
     (PROG[i][1] if i in PHASE_IDS else "    " + PROG[i][1])[:58],
     PROG[i][2].replace(" days", "").strip(), PROG[i][3], PROG[i][4]]
    for i in GANTT_IDS
]
PROGRAMME_ROWS[0][1] = "MASTER CONSTRUCTION SCHEDULE"

# what WM3 applied, from master H.15 -- stated as what the bill now contains
WM3_APPLIED = [
    ["BURSTER SLAB", "200 THK M30", "38.40 m3",
     "REDUCED FROM 300 THK M35 AND 57.60 m3"],
    ["SENTRY POST", "RC FRAME ONLY", "-",
     "THE BRICK INFILL IS MEASURED SEPARATELY AS BRICKWORK"],
    ["ESCAPE SHAFT COLLARS", "250 RC, OD 1900", "6.285 m3",
     "ADDED AS A MEASURED LINE"],
    ["GENERATOR", "15 kVA", "1 No.", "ADDED AS A VISIBLE LINE"],
    ["CONCRETE TOTAL", "-", "467.59 m3", "= THE SUM OF ITS OWN LINES"],
    ["PROGRAMME WORDING", "13 ACTIVITIES", "-",
     "2.0 m COVER, 900 SLAB AND THE POST-M1 BOX SIZE"],
]
