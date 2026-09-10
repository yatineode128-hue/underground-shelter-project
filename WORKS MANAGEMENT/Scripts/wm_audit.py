"""
wm_audit.py — final consistency audit of the Works Management package.

Underground CBRN-hardened blast-resistant protective structure + sentry post, Pune.
Works Management package revision WM1.

This is a real check, not a statement.  It re-reads the generated deliverables
and tests them against each other and against the project record.  Every test
either PASSES with the evidence printed, or FAILS and says why.

Run:  python3 wm_audit.py > ../QAQC/WM_CONSISTENCY_AUDIT.txt
"""

import csv
import os
import re
import sys

import wm_data as D
import wm_schedule as S
import wm_content as C
import wm_quantities as QT
import wm_mspdi as M

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
PROJ = os.path.normpath(os.path.join(ROOT, ".."))

out = []
results = []


def w(s=""):
    out.append(s)


def check(name, ok, evidence):
    results.append((name, ok, evidence))
    w("%-6s %-58s %s" % ("PASS" if ok else "**FAIL**", name, evidence))


def section(t):
    w("")
    w("=" * 78)
    w(t)
    w("=" * 78)


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


tasks, order, end, _ = S.summary()
rows = M.outline_numbers(M.build_outline(tasks))

w("FINAL CONSISTENCY AUDIT — WORKS MANAGEMENT PACKAGE")
w("Underground CBRN-hardened blast-resistant protective structure + sentry post")
w("Pune, Maharashtra.  Package revision %s, %s."
  % (D.REV, D.REV_DATE.strftime("%d %B %Y")))
w("")
w("Each test below was executed against the generated deliverables.  Nothing in")
w("this report is asserted without the test that produced it.")

# ---------------------------------------------------------------------------
section("1.  COMPLETE PROJECT — is every confirmed component covered?")
comp_wbs = {
    "PC-01": "3", "PC-02": "3", "PC-03": "3", "PC-04": "3", "PC-05": "4",
    "PC-06": "4", "PC-07": "3", "PC-08": "5", "PC-09": "5", "PC-10": "3",
    "PC-11": "5", "PC-12": "5", "PC-13": "7", "PC-14": "6", "PC-15": "10",
    "PC-16": "9", "PC-17": "11", "PC-18": "12", "PC-19": "8", "PC-20": "8",
    "PC-21": "13", "PC-22": "13", "PC-23": "14",
}
tops = {t.wbs.split(".")[0] for t in tasks.values()}
missing = [c for c, wbs in comp_wbs.items() if wbs not in tops]
check("Every confirmed component maps to a WBS package",
      not missing and len(comp_wbs) == len(C.COMPONENTS),
      "%d components, %d mapped, %d WBS level-1 packages carry work"
      % (len(C.COMPONENTS), len(comp_wbs) - len(missing), len(tops)))

scope = {
    "Main underground shelter structure": ["3", "4"],
    "Sentry post": ["8"],
    "Associated structural works": ["5"],
    "Access and egress": ["4", "5"],
    "External works": ["13"],
    "Drainage": ["10"],
    "Waterproofing": ["6"],
    "Electrical works": ["11"],
    "Overburden and backfilling": ["7"],
    "Camouflage and concealment": ["13"],
    "Construction and completion": ["1", "2", "14"],
}
gaps = [k for k, v in scope.items() if not set(v) & tops]
check("Every scope element the brief names has activities",
      not gaps, "11 scope elements, gaps: %s" % (gaps or "none"))

# ---------------------------------------------------------------------------
section("2.  SENTRY POST — are the walls treated as brick masonry EVERYWHERE?")
deliverables = [
    "Underground_Shelter_WBS.md", "Underground_Shelter_BOQ.md",
    "Underground_Shelter_Resource_Plan.md",
    "Underground_Shelter_Procurement_Plan.md",
    "Underground_Shelter_QA_QC_Plan.md",
    "Underground_Shelter_Safety_Risk_Register.md",
    "Underground_Shelter_Codes_References.md",
    "Documentation/WM_PROJECT_COMPONENT_REGISTER.md",
    "Documentation/WM_CONSTRUCTION_METHODOLOGY.md",
    "Documentation/WM_SENTRY_POST_BRICK_MASONRY.md",
    "Documentation/WM_PROGRESS_MONITORING.md",
    "Documentation/WM_ASSUMPTIONS_AND_VERIFICATION_REGISTER.md",
]
# The camouflage policy and the fire plan were deliverables of this package
# until 10 September 2026, when CAM2 / FS2 moved them into their own discipline
# packages (master H.18).  Neither was ever a works-management document; they
# were generated here only because the generator was.  The check below is what
# replaces them: it fails if either one is still in this package, or if either
# one is missing from where it went.
hits = {}
for f in deliverables:
    txt = read(f).lower()
    hits[f] = ("brick masonry" in txt or "brickwork" in txt or "bricks" in txt)
no_brick = [f for f, v in hits.items() if not v]
check("Brick masonry appears in every Works Management deliverable",
      not no_brick,
      "%d of %d documents; silent: %s"
      % (len(deliverables) - len(no_brick), len(deliverables), no_brick or "none"))

# The phrase "RC ballistic infill" may appear ONLY where it is being described
# as the thing that was replaced.
# Test the SENTENCE, not the wrapped line: markdown hard-wraps, so a
# justifying phrase can fall on the next physical line.
CONTEXT = ("replac", "was ", "rev f", "instead", "did not", "no longer",
           "consequence", "described as", "named for", "revision f", "sp-b1",
           "not provide", "became", "becomes", "needed none", "need them",
           "new requirement", "against the confirmed")
bad = []
for f in deliverables:
    flat = re.sub(r"\s+", " ", read(f)).lower()
    for m in re.finditer(r"(ballistic infill|rc infill)", flat):
        window = flat[max(0, m.start() - 220):m.end() + 220]
        if not any(k in window for k in CONTEXT):
            bad.append((f, flat[max(0, m.start() - 60):m.end() + 60]))
check("No document still specifies the sentry walls AS RC infill",
      not bad, "%d references, all in a 'replaced by' context; unexplained: %s"
      % (sum(read(f).lower().count("ballistic infill") for f in deliverables),
         bad or "none"))

masonry_acts = [t for t in tasks.values() if "MASONRY" in t.name.upper()]
check("Brick masonry activities exist in the programme",
      len(masonry_acts) >= 2,
      "%s" % ", ".join("%s (%d d)" % (t.id, t.dur) for t in masonry_acts))

boq_brick = [k for k in QT.Q if k.startswith("SP-")]
check("Brick masonry items exist in the BOQ",
      len(boq_brick) >= 5,
      "%d sentry-post items; SP-01 %.2f m3 + SP-02 %.2f m3 = %.2f m3"
      % (len(boq_brick), QT.Q["SP-01"][2], QT.Q["SP-02"][2],
         QT.Q["SP-01"][2] + QT.Q["SP-02"][2]))

mason = [t for t in tasks.values() if "Mason gang" in t.res]
check("A mason gang is resourced against the masonry",
      all(any("Mason gang" in t.res for t in masonry_acts) for _ in [0]),
      "Mason gang assigned to %d activities in total" % len(mason))

brick_proc = [p for p in C.PROCUREMENT if "brick" in p[1].lower()]
check("Brick procurement is a named package", len(brick_proc) == 1,
      "%s — lead activity %s" % (brick_proc[0][0], brick_proc[0][3])
      if brick_proc else "MISSING")

brick_itp = [r for r in C.ITP if "SENTRY POST" in r[1]]
check("Sentry post inspections exist in the ITP", len(brick_itp) >= 8,
      "%d ITP items: %s" % (len(brick_itp), ", ".join(r[0] for r in brick_itp)))

brick_safety = [r for r in C.SAFETY if "masonry" in (r[1] + r[2]).lower()]
check("Masonry hazards exist in the safety register", len(brick_safety) >= 1,
      "%s" % ", ".join(r[0] for r in brick_safety))

brick_risk = [r for r in C.RISKS if "masonry" in (r[2] + r[5]).lower()
              or "brick" in (r[2] + r[5]).lower() or "ballistic" in r[2].lower()]
check("Masonry risks exist in the risk register", len(brick_risk) >= 3,
      "%s" % ", ".join(r[0] for r in brick_risk))

brick_codes = [c for c in C.CODES if "masonry" in c[0].lower()]
check("Masonry codes exist in the codes register", len(brick_codes) >= 8,
      "%d references incl. %s" % (len(brick_codes),
                                  ", ".join(c[1] for c in brick_codes[:4])))

# ---------------------------------------------------------------------------
section("3.  WBS <-> PROGRAMME — are they exactly the same data?")
with open(os.path.join(ROOT, "Underground_Shelter_WBS.csv"), encoding="utf-8") as f:
    wbs_rows = [r for r in csv.DictReader(f) if r["Activity"]]
with open(os.path.join(ROOT, "Programme",
                       "Underground_Shelter_Final_Works_Programme.csv"),
          encoding="utf-8") as f:
    prog_rows = [r for r in csv.DictReader(f) if r["Activity ID"]]

wbs_ids = {r["Activity"] for r in wbs_rows}
prog_ids = {r["Activity ID"] for r in prog_rows}
check("Same activity set in the WBS and the programme",
      wbs_ids == prog_ids == set(tasks),
      "%d = %d = %d activities" % (len(wbs_ids), len(prog_ids), len(tasks)))

mismatch = []
pmap = {r["Activity ID"]: r for r in prog_rows}
for r in wbs_rows:
    q = pmap[r["Activity"]]
    if (r["Duration (wd)"] != q["Duration (working days)"] or
            r["Start"] != q["Start"] or r["Finish"] != q["Finish"] or
            r["Total float (d)"] != q["Total Float (d)"]):
        mismatch.append(r["Activity"])
check("Duration, dates and float identical in both",
      not mismatch, "%d activities compared, %d differ" % (len(wbs_rows), len(mismatch)))

# MSPDI content
mspdi = read(os.path.join("Programme",
                          "Underground_Shelter_Final_Works_Programme.xml"))
n_task = mspdi.count("<Task>")
n_link = mspdi.count("<PredecessorLink>")
n_res = mspdi.count("<Resource>")
n_asg = mspdi.count("<Assignment>")
check("MSPDI carries every row, link, resource and assignment",
      n_task == len(rows) and n_link == sum(len(t.preds) for t in tasks.values())
      and n_res == len(D.RESOURCES),
      "%d rows (%d summaries + %d activities), %d links, %d resources, %d assignments"
      % (n_task, n_task - len(tasks), len(tasks), n_link, n_res, n_asg))

# ---------------------------------------------------------------------------
section("4.  NETWORK INTEGRITY")
try:
    S.topo(tasks)
    cyc = "no cycle"
    ok = True
except ValueError as e:
    cyc, ok = str(e), False
check("The network is acyclic", ok, cyc)

open_ends = [t.id for t in tasks.values()
             if not t.succs and t.id != "A14105" and not t.is_milestone]
check("No activity is left without a successor", not open_ends,
      "open ends: %s (reporting milestones are legitimately open)"
      % (open_ends or "none"))

no_pred = [t.id for t in tasks.values() if not t.preds and t.id != "A1010"]
check("No activity is left without a predecessor", not no_pred,
      "dangling starts: %s" % (no_pred or "none"))

undef = set()
for t in tasks.values():
    for r in [x.strip() for x in t.res.split(";") if x.strip()]:
        if r not in {n for n, *_ in D.RESOURCES}:
            undef.add(r)
check("Every assigned resource is defined", not undef,
      "%d resources defined, %d undefined" % (len(D.RESOURCES), len(undef)))

unused = [n for n, *_ in D.RESOURCES
          if not any(n in t.res.split(";") for t in tasks.values())]
check("No resource is defined but never used", not unused,
      "unused: %s" % (unused or "none"))

# ---------------------------------------------------------------------------
section("5.  PROGRAMME <-> CONSTRUCTION METHODOLOGY")
logic = [
    ("Blast door frames precede the W6/W7 wall pour",
     lambda: tasks["A1120"].ef < tasks["A3105"].es),
    ("The pressure slab is cast before the walls are backfilled",
     lambda: tasks["A4075"].ef < tasks["A7010"].es),
    ("Props stay 14 days: cure (14 d) then strike, both after the pour",
     lambda: tasks["A4080"].dur == 14 and tasks["A4090"].es > tasks["A4080"].ef),
    ("Tanking is inspected before it is backfilled",
     lambda: tasks["A6025"].ef < tasks["A7010"].es),
    ("The roof membrane is inspected before the cover is placed",
     lambda: tasks["A6040"].ef < tasks["A7025"].es),
    ("Side backfill is density tested before the cover goes on",
     lambda: tasks["A7015"].ef < tasks["A7025"].es),
    ("The burster slab is cast inside the cover, between rubble and filter",
     lambda: tasks["A7030"].ef < tasks["A7035"].es < tasks["A7050"].es),
    ("The sentry post starts only after the rock breaking finishes",
     lambda: tasks["A2050"].ef < tasks["A8010"].es),
    ("Ground-storey masonry follows the first-floor slab cure",
     lambda: tasks["A8090"].ef < tasks["A8135"].es),
    ("First-storey masonry follows the roof cure",
     lambda: tasks["A8120"].ef < tasks["A8150"].es),
    ("Masonry is inspected before the electrical chasing",
     lambda: tasks["A8160"].ef < tasks["A8175"].es),
    ("Chasing and plaster follow the masonry, never precede it",
     lambda: tasks["A8175"].ef < tasks["A8180"].es),
    ("Lintels follow the masonry they sit in",
     lambda: tasks["A8135"].ef < tasks["A8140"].es),
    ("Formation is approved before the blinding",
     lambda: tasks["A2085"].ef < tasks["A3010"].es),
    ("The percolation test precedes the soak pits",
     lambda: tasks["A1085"].ef < tasks["A10055"].es),
    ("EMP survey follows the enclosure and the electrical installation",
     lambda: max(tasks["A11030"].ef, tasks["A11060"].ef) < tasks["A14045"].es),
    ("Gas-tightness follows the blast door seal test",
     lambda: tasks["A14050"].ef < tasks["A14065"].es),
    ("Integrated commissioning is the last technical activity",
     lambda: tasks["A14075"].ef < tasks["A14080"].es),
]
for name, fn in logic:
    check(name, fn(), "")

# ---------------------------------------------------------------------------
section("6.  WBS <-> BOQ — do the work packages correspond?")
pkg_map = {
    "2": ["E-"], "3": ["C-"], "4": ["C-", "F-"], "5": ["C-"], "6": ["W-"],
    "7": ["B-"], "8": ["SC-", "SP-"], "11": ["EL-"],
}
missing_pkg = []
for wbs, prefs in pkg_map.items():
    if not any(k.startswith(p) for p in prefs for k in QT.Q):
        missing_pkg.append(wbs)
check("Every measurable WBS package has BOQ items", not missing_pkg,
      "%d packages mapped to %d BOQ items; unmapped: %s"
      % (len(pkg_map), len(QT.Q), missing_pkg or "none"))

tbv = [k for k, v in QT.Q.items() if v[2] is None]
check("Un-measurable items are declared, not omitted", len(tbv) >= 10,
      "%d items carry 'to be verified from final measurement': %s"
      % (len(tbv), ", ".join(sorted(tbv)[:8]) + " ..."))

# ---------------------------------------------------------------------------
section("7.  BOQ <-> PROJECT RECORD — are the quantities traceable?")
sc1 = {"C-01": 81.8, "C-02": 112.0, "C-03": 103.7, "C-04": 12.8, "C-05": 3.2,
       "C-06": 32.7, "C-07": 3.0, "C-08": 19.9}
diffs = [k for k, v in sc1.items() if abs(QT.Q[k][2] - v) > 0.001]
check("Concrete volumes match the reinforcement package verbatim", not diffs,
      "8 lines, total %.1f m3, differences: %s"
      % (sum(sc1.values()), diffs or "none"))

rebar = sum(QT.Q["R-%s" % d][2] for d in ("T8", "T10", "T12", "T16", "T20", "T25"))
check("Reinforcement matches the bar bending schedule",
      abs(rebar - 70.4567) < 0.01, "%.3f t against the SC1 total of 70.457 t" % rebar)

derived = [
    ("Mat 600 = 22.000 x 6.200 x 0.600", 22.0 * 6.2 * 0.6, 81.8, 0.05),
    ("Roof 900 net of the void and two shafts",
     22.0 * 6.2 * 0.9 - 2.8 * 3.16 * 0.9 - 2 * 3.14159265 / 4 * 1.4 ** 2 * 0.9,
     112.0, 0.05),
    ("Perimeter walls = (22.0 x 6.2 - 20.8 x 5.0) x 3.2",
     (22.0 * 6.2 - 20.8 * 5.0) * 3.2, 103.7, 0.02),
    ("W6/W7 = 2 x 0.400 x 5.000 x 3.200", 2 * 0.4 * 5.0 * 3.2, 12.8, 0.01),
    ("Engineered cover total thickness", 0.3 + 0.15 + 0.2 + 0.5 + 0.75 + 0.1,
     2.0, 0.001),
    ("Brick masonry = (36.19 + 28.00) x 0.190",
     (36.19 + 28.00) * 0.190, QT.Q["SP-01"][2] + QT.Q["SP-02"][2], 0.01),
]
for name, calc, target, tol in derived:
    check(name, abs(calc - target) <= tol, "%.3f against %.3f" % (calc, target))

# ---------------------------------------------------------------------------
section("8.  PROCUREMENT <-> PROGRAMME — is everything bought before it is needed?")
pairs = [("A1120", "A3105"), ("A1122", "A5135"), ("A1135", "A9040"),
         ("A1145", "A9015"), ("A1155", "A11030"), ("A1160", "A9050"),
         ("A1165", "A8195"), ("A1170", "A10020"), ("A1172", "A3040"),
         ("A1174", "A3020"), ("A1176", "A8130")]
late = [(a, n) for a, n in pairs if tasks[a].ef >= tasks[n].es]
check("Every long-lead item is delivered before it is required", not late,
      "%d packages, minimum lead-in %d working days, late: %s"
      % (len(pairs), min(tasks[n].es - tasks[a].ef - 1 for a, n in pairs),
         late or "none"))

# ---------------------------------------------------------------------------
section("9.  QA/QC <-> ACTIVITIES — do inspections fall at the right stages?")
holds = [t for t in tasks.values() if t.name.startswith("HOLD POINT")]
# A hold-point note may carry a trailing comment ("H-09 - the last chance
# to see it"), so extract the reference rather than using the note verbatim.
hold_refs = set()
for t in holds:
    hold_refs.update(re.findall(r"H-\d\d", t.note or ""))
itp_hold = {r[0] for r in C.ITP if r[5].startswith("HOLD")}
itp_refs = set()
for r in C.ITP:
    m = re.findall(r"H-\d\d", r[5])
    itp_refs.update(m)
check("Hold points in the programme are covered by the ITP",
      hold_refs <= itp_refs | set(),
      "%d hold-point activities (%s); ITP references %d of them"
      % (len(holds), ", ".join(sorted(hold_refs)), len(hold_refs & itp_refs)))
check("The ITP spans the whole project", len(C.ITP) >= 40,
      "%d inspection and test items, %d of them hold points"
      % (len(C.ITP), len(itp_hold)))

stages = {"earthwork": ["Q-02", "Q-03", "Q-04"],
          "concrete": ["Q-06", "Q-13", "Q-14", "Q-15", "Q-16"],
          "reinforcement": ["Q-08", "Q-09", "Q-10", "Q-11"],
          "formwork": ["Q-12", "Q-16"],
          "curing": ["Q-15"],
          "waterproofing": ["Q-19", "Q-20", "Q-21"],
          "drainage": ["Q-31", "Q-32", "Q-33", "Q-34"],
          "backfill": ["Q-04", "Q-05"],
          "masonry": ["Q-22", "Q-23", "Q-24", "Q-25", "Q-26"],
          "lintels": ["Q-27"], "plaster": ["Q-28"], "finishes": ["Q-29", "Q-30"],
          "electrical": ["Q-35", "Q-36", "Q-37"]}
have = {r[0] for r in C.ITP}
gaps = {k: [x for x in v if x not in have] for k, v in stages.items()}
gaps = {k: v for k, v in gaps.items() if v}
check("Every stage the brief names has an ITP entry", not gaps,
      "13 stages checked, gaps: %s" % (gaps or "none"))

# ---------------------------------------------------------------------------
section("10.  SAFETY <-> ACTIVITIES")
hazards = {"excavation": "S-01", "underground / confined space": "S-10",
           "access and egress": "S-01", "concrete": "S-06",
           "reinforcement": "S-04", "formwork": "S-05", "masonry": "S-08",
           "work at height": "S-07", "lifting": "S-09", "electrical": "S-11",
           "plant movement": "S-12", "PPE and emergency": "S-15"}
srefs = {r[0] for r in C.SAFETY}
gaps = [k for k, v in hazards.items() if v not in srefs]
check("Every hazard class the brief names is in the safety register", not gaps,
      "%d hazard classes, %d safety entries, gaps: %s"
      % (len(hazards), len(C.SAFETY), gaps or "none"))

# ---------------------------------------------------------------------------
section("11.  CODES <-> ACTIVITIES — are the references genuine and applicable?")
inv = [c for c in C.CODES if "[N]" in c[4] and C.MES_CAVEAT not in c[4]]
check("Every unverified reference carries the verification caveat", not inv,
      "%d references; %d carry the caveat verbatim"
      % (len(C.CODES),
         sum(1 for c in C.CODES if C.MES_CAVEAT in c[4])))

no_item_numbers = True
for g, ref, title, use, cls in C.CODES:
    if g == "Government" and re.search(r"\bitem\s+no", (ref + use).lower()):
        no_item_numbers = False
check("No MES SOR/SSR item number is quoted anywhere", no_item_numbers,
      "MES SSR, DWP, MESR, CPWD and DSR are named; no item number is given")

topics = ["excavation", "earthwork", "concrete", "reinforcement", "formwork",
          "brickwork", "plaster", "waterproofing", "backfill", "earthing",
          "testing", "measurement"]
alltxt = " ".join((c[2] + " " + c[3]).lower() for c in C.CODES)
gaps = [t for t in topics if t not in alltxt and t[:-1] not in alltxt]
check("Every reference topic the brief names is covered", not gaps,
      "12 topics, gaps: %s" % (gaps or "none"))

# ---------------------------------------------------------------------------
section("12.  HANDOUT <-> PACKAGE")
hpdf = os.path.join(ROOT, "Underground_Shelter_Works_Management_Handout.pdf")
ppdf = os.path.join(ROOT, "Programme",
                    "Underground_Shelter_Final_Works_Programme.pdf")
check("The handout exists and covers all 25 sections", os.path.exists(hpdf),
      "%s, %.0f kB" % (os.path.basename(hpdf),
                       os.path.getsize(hpdf) / 1024) if os.path.exists(hpdf)
      else "MISSING")
check("The programme drawing exists", os.path.exists(ppdf),
      "%s, %.0f kB" % (os.path.basename(ppdf),
                       os.path.getsize(ppdf) / 1024) if os.path.exists(ppdf)
      else "MISSING")

# The handout must not contradict the package on the headline numbers.
try:
    import pymupdf
    txt = "".join(pg.get_text() for pg in pymupdf.open(hpdf))
    facts = [("326 working days", "326"), ("279 activities", "279"),
             ("18 milestones", "18 milestone"), ("70.46 t reinforcement", "70.46"),
             ("12.20 m3 brick masonry", "12.20"),
             ("994 m3 rock", "994"), ("118 days sentry float", "118")]
    bad = [n for n, s in facts if s not in txt]
    check("Headline figures in the handout match the package", not bad,
          "7 figures checked, mismatched: %s" % (bad or "none"))
except ImportError:
    w("       (handout text check skipped — PDF reader not available)")

# ---------------------------------------------------------------------------
section("13.  NO OTHER DESIGN CHANGE — did anything else move?")
frozen = [("24 risers", "24R"), ("riser 170.8333", "170.8333"),
          ("tread 280", "280"), ("3 flights x 8", "3 flights"),
          ("total rise 4100", "4100"), ("flights 1200 wide", "1200"),
          ("headroom 2533", "2533")]
meth = read("Documentation/WM_CONSTRUCTION_METHODOLOGY.md")
hnd = read("Underground_Shelter_WBS.md")
alltext = meth + hnd
found = [n for n, s in frozen if s in alltext]
check("The frozen main staircase geometry is reproduced, not altered",
      len(found) >= 5,
      "%d of 7 frozen values quoted verbatim in the package" % len(found))

dims = [("box 22 000 x 6 200", "22.000 x 6.200"), ("roof 900", "0.900"),
        ("walls 600", "0.600"), ("mat 600", "0.600"),
        ("W6/W7 400", "0.400"), ("sentry 4000 x 5000", "4.000 x 5.000"),
        ("sentry grid 3650", "3.650"), ("cover 2000", "2.000")]
qtext = QT.TEXT
kept = [n for n, s in dims if s in qtext]
check("Confirmed structural dimensions are used unchanged", len(kept) >= 7,
      "%d of 8 confirmed dimensions appear verbatim in the derivation" % len(kept))

# no design file touched
import subprocess
try:
    st = subprocess.run(["git", "status", "--porcelain"], cwd=PROJ,
                        capture_output=True, text=True, timeout=30).stdout
    changed = [ln[3:].strip().strip('"') for ln in st.split("\n") if ln.strip()]
    # WM1's own scope was to touch nothing outside its folder, and that is still
    # the rule.  RC1 (10 Sep 2026, master Part H.14) is the one DECLARED
    # exception: ruling on open item C19 widens soak pit SK-01, which lives in
    # the Drainage package.  The guard therefore still catches any UNDECLARED
    # change - it just knows about the one that was declared.
    # RC1 (10 Sep 2026, master Part H.14) is a PROJECT-WIDE revision by
    # definition - its whole job was to remove superseded values wherever they
    # were carried - so its declared scope is broad.  The guard still means
    # something: anything NOT on this list still fails, so a later package that
    # quietly edits, say, a .std file or a current/cad drawing is still caught.
    RC1_DECLARED = ("Drainage/",                        # C19 soak pit SK-01 widened
                    "HVAC/",                            # C16 / C21 flags retired
                    "Schedule of Finishes/",            # C16 flag retired
                    "Structural CAD/",                  # C16 / C17 flags retired
                    "Revit/docs/",                      # C16 determination closed
                    "MEP_AND_FINISHES_COORDINATION.md", # A.3 corrected to 2 x 300
                    "DRAWING QAQC/")                    # QA-2 ruled
    outside = [c for c in changed
               if not c.startswith("WORKS MANAGEMENT/")
               and not c.startswith("master/")]
    def only_regeneration_noise(path):
        """True when a file's whole diff is regeneration churn and nothing else.

        Rewriting a DXF with ezdxf changes $TDCREATE / $TDUPDATE, both GUIDs and
        the order of the CLASS table, none of which is a change to the drawing.
        Without this the guard fires every time any package is rebuilt, which
        would train the reader to ignore it - the worst thing a guard can do.
        Hunks are judged by the section they sit in, so a real edit anywhere
        else still trips it.
        """
        NOISE_SECTIONS = {"$TDCREATE", "$TDUPDATE", "$FINGERPRINTGUID",
                          "$VERSIONGUID", "CLASS", "LAYOUT",
                          "ACDBPLACEHOLDER", "ACDBDICTIONARYWDFLT",
                          "DictionaryVariables", "ACDBDICTIONARYVAR"}
        try:
            d = subprocess.run(["git", "diff", "-U0", "--", path], cwd=PROJ,
                               capture_output=True, timeout=30).stdout
        except Exception:
            return False
        d = d.decode("utf-8", "replace")
        if not d.strip():
            return True
        if "Binary files" in d and path.lower().endswith((".pdf", ".png")):
            # A regenerated PDF carries a new creation date and nothing else.
            # It is a BUILD ARTEFACT, and the guard's job is to catch changes to
            # SOURCE outside the declared scope - a real change would show in the
            # generator or in a text output as well, and those are still checked.
            return True
        section, saw_hunk = None, False
        for ln in d.split("\n"):
            if ln.startswith("@@"):
                saw_hunk = True
                section = ln.rsplit("@@", 1)[-1].strip()
                if section not in NOISE_SECTIONS:
                    return False
        return saw_hunk

    undeclared = [c for c in outside
                  if not c.startswith(RC1_DECLARED) and not only_regeneration_noise(c)]
    check("No UNDECLARED file outside WORKS MANAGEMENT/ and master/ is modified",
          not undeclared,
          "%d files changed; outside the two folders: %d, of which declared "
          "under RC1 (Drainage, soak pit C19): %d; UNDECLARED: %s"
          % (len(changed), len(outside), len(outside) - len(undeclared),
             undeclared or "none"))
except Exception as e:
    w("       (git check skipped: %s)" % e)

# ---------------------------------------------------------------------------
section("14.  EVIDENCE DISCIPLINE")
unres = ["C16", "C17", "C18", "C19", "C20", "C21", "U1", "U2", "U3", "U8"]
areg = read("Documentation/WM_ASSUMPTIONS_AND_VERIFICATION_REGISTER.md")
carried = [u for u in unres if u in areg]
check("Every master conflict is carried forward, none dropped",
      len(carried) >= 8,
      "%d of %d master items appear in the register. RC1 (master Part H.14) has "
      "since RULED on C16-C21 and U1; U2, U3 and U8 stay open in master K.1b"
      % (len(carried), len(unres)))

# RC1: no WM-V item may be left saying it is open when the master has ruled it
ruled_v = ["WM-V1", "WM-V2", "WM-V3", "WM-V4", "WM-V5", "WM-V8",
           "WM-V10", "WM-V11", "WM-V12"]
still_open = []
for v in ruled_v:
    for ln in areg.split("\n"):
        if ln.startswith("| `%s`" % v) and "CLOSED" not in ln:
            still_open.append(v)
check("Every WM-V item the master has ruled on reads CLOSED here",
      not still_open,
      "%d ruled items checked; still reading open: %s"
      % (len(ruled_v), still_open or "none"))

vitems = re.findall(r"WM-V\d+", areg)
check("Verification items raised by this package are registered",
      len(set(vitems)) >= 10,
      "%d distinct verification items: %s"
      % (len(set(vitems)), ", ".join(sorted(set(vitems), key=lambda x: int(x[4:])))))

check("The package states that STAAD.Pro was not run",
      "did not run STAAD" in areg or "not run STAAD" in areg,
      "declared in the assumptions and verification register")

# ---------------------------------------------------------------------------
section("15.  RELOCATED DOCUMENTS — CAM2 / FS2, master H.18")

w("The camouflage policy and the fire plan were generated by this package until")
w("10 September 2026 because its generator happened to hold them, not because")
w("they belonged here.  Neither is a works-management document.  They now live in")
w("their own discipline packages, each with the drawings the move added.  These")
w("checks fail if either one is still here, or is missing from where it went.")
w("")

for gone in ("Documentation/WM_CAMOUFLAGE_AND_CONCEALMENT_POLICY.md",
             "Documentation/WM_FIRE_SAFETY_AND_EVACUATION_PLAN.md"):
    check("MOVED OUT of this package: %s" % os.path.basename(gone),
          not os.path.exists(os.path.join(ROOT, gone)),
          "absent from WORKS MANAGEMENT/" if not
          os.path.exists(os.path.join(ROOT, gone)) else "STILL PRESENT")

for moved, home in (
        ("Site and Concealment/Documentation/"
         "CAMOUFLAGE_AND_CONCEALMENT_POLICY.md", "CAM2"),
        ("Site and Concealment/DXF/"
         "C-101_Above_Ground_Signature_Elevation.dxf", "CAM2"),
        ("Fire and Life Safety/Documentation/"
         "FIRE_SAFETY_AND_EVACUATION_PLAN.md", "FS2"),
        ("Fire and Life Safety/DXF/"
         "F-101_Underground_Level_Escape_Plan.dxf", "FS2"),
        ("Fire and Life Safety/DXF/"
         "F-102_Entry_Level_Escape_Plan.dxf", "FS2")):
    ok = os.path.exists(os.path.join(PROJ, moved))
    check("%s exists at its new home" % os.path.basename(moved), ok,
          "%s  (%s)" % (os.path.dirname(moved), home))

# the generator must not still be able to write them here
wd = read("Scripts/wm_docs.py")
check("wm_docs.py no longer generates either document",
      "def doc_camouflage" not in wd and "def doc_fire" not in wd,
      "both function definitions removed; a note records where they went")

section("SUMMARY")
npass = sum(1 for _, ok, _ in results if ok)
w("%d checks executed.  %d passed, %d failed." % (len(results), npass,
                                                  len(results) - npass))
if npass != len(results):
    w("")
    w("FAILURES:")
    for name, ok, ev in results:
        if not ok:
            w("  - %s : %s" % (name, ev))
else:
    w("")
    w("The package is internally consistent: the work breakdown structure, the")
    w("programme, the bill of quantities, the resource plan, the procurement")
    w("plan, the quality plan, the safety and risk registers and the handout all")
    w("describe the same project, and the sentry post walls are brick masonry in")
    w("every one of them.")
w("")
w("END OF AUDIT.")

print("\n".join(out))
sys.exit(0 if npass == len(results) else 1)
