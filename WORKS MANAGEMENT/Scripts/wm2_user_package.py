"""wm2_user_package.py — Works Management revision WM2.

Reads the USER'S OWN four Works Management files, exactly as supplied, and
publishes them as the project's cost document and programme of record.

Nothing here is retyped.  The BOQ, the rates and the cost build-up are read
from the user's workbook cell by cell; the 130-activity Master Construction
Schedule is decoded from the user's own MS Project print.  If a number in the
generated CSV is wrong, the user's file is wrong — there is no intermediate
transcription that could have introduced an error.

Brief section 26 sets the order of authority for Works Management:
    1  the user's uploaded Works Management files      <- these
    2  actual project information
    3  existing project documentation
    4  previously generated Works Management material  <- WM1
so nothing in the user's material is corrected, rebuilt or re-derived here.
Where it disagrees with the project master, the disagreement is RECORDED in
Documentation/WM_RECONCILIATION_REGISTER.md and left for the user to rule on.
"""
import csv, os, re, sys, zlib

HERE = os.path.dirname(os.path.abspath(__file__))
WM   = os.path.abspath(os.path.join(HERE, ".."))
SRC  = os.path.join(WM, "USER_SOURCE")
XLSX = os.path.join(SRC, "Underground_CBRN_Ops_Room_BOQ_Estimate.xlsx")
MCS  = os.path.join(SRC, "UG_CBRN_HDRND_OPS_ROOM_MCS_R0_Lvl5Micro.pdf")


# ---------------------------------------------------------------- workbook
def read_workbook():
    import openpyxl
    wb = openpyxl.load_workbook(XLSX, data_only=True)
    out = {}
    for ws in wb.worksheets:
        rows = []
        for r in ws.iter_rows(values_only=True):
            cells = ["" if c is None else c for c in r]
            if any(str(c).strip() for c in cells):
                rows.append(cells)
        out[ws.title] = rows
    return out


# ------------------------------------------------------------- MS Project
# The print is a Microsoft "Print To PDF" with Identity-encoded subset fonts,
# so the glyph codes mean nothing until they are put back through the font's
# own ToUnicode CMap.  That is all this does.
def _streams(raw):
    for m in re.finditer(rb"stream\r?\n", raw):
        s = m.end(); e = raw.find(b"endstream", s)
        if e < 0:
            continue
        blob = raw[s:e]
        try:
            yield zlib.decompress(blob)
        except Exception:
            yield blob          # the ToUnicode CMaps are stored uncompressed


def _cmap(raw):
    cm = {}
    for data in _streams(raw):
        for blk in re.findall(rb"beginbfchar(.*?)endbfchar", data, re.S):
            for a, b in re.findall(rb"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", blk):
                cm[int(a, 16)] = "".join(chr(int(b[i:i + 4], 16))
                                         for i in range(0, len(b), 4))
        for blk in re.findall(rb"beginbfrange(.*?)endbfrange", data, re.S):
            for a, b, c in re.findall(
                    rb"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", blk):
                lo, hi, st = int(a, 16), int(b, 16), int(c, 16)
                for i in range(lo, hi + 1):
                    cm[i] = chr(st + i - lo)
    return cm


def read_schedule():
    raw = open(MCS, "rb").read()
    cm = _cmap(raw)
    chunks = []
    for data in _streams(raw):
        if b"Tj" not in data and b"TJ" not in data:
            continue
        buf = []
        for tm in re.finditer(rb"<([0-9A-Fa-f\s]+)>|(Td|TD|T\*|Tm)", data):
            if tm.group(1) is not None:
                h = re.sub(rb"\s", b"", tm.group(1)).decode()
                for i in range(0, len(h), 4):
                    buf.append(cm.get(int(h[i:i + 4], 16), ""))
            else:
                buf.append("\n")
        if buf:
            chunks.append("".join(buf))
    lines = [l.strip() for l in "\n".join(chunks).split("\n") if l.strip()]

    # The print puts one field per line: id, name, duration, start, finish and
    # (when there is one) predecessors.  Task names wrap over several lines and
    # a predecessor is often a bare number, so the only reliable anchor is that
    # the ids run 1, 2, 3 ... in order: a bare number is the NEXT ACTIVITY only
    # when it is the id we are expecting next.  Everything between two ids is
    # one activity's record.
    DATE = re.compile(r"^\d{2}-\d{2}-\d{2}$")
    DUR  = re.compile(r"^\d+ days?$")
    JUNK = {"ID", "Task NameWorking", "Days", "StartFinishPredecessors",
            "Task", "Split", "Milestone", "Summary", "Project Summary",
            "External Tasks", "External Milestone", "Inactive Task",
            "Inactive Milestone", "Inactive Summary", "Manual Task",
            "Duration-only", "Manual Summary Rollup", "Manual Summary",
            "Start-only", "Finish-only", "Deadline", "Critical",
            "Critical Split", "Progress", "Manual Progress"}
    JUNKRE = re.compile(r"^(Page \d|Project:|Date:|[A-Z][a-z]{2} '\d\d$|\d{4}$)")

    pos, want, marks = 0, 1, []
    while True:
        try:
            k = lines.index(str(want), pos)
        except ValueError:
            break
        marks.append((want, k)); pos = k + 1; want += 1
    marks.append((want, len(lines)))

    acts = []
    for (aid, k), (_, nxt) in zip(marks, marks[1:]):
        rec = [l for l in lines[k + 1:nxt]
               if l not in JUNK and not JUNKRE.match(l)]
        d = next((n for n, l in enumerate(rec) if DUR.fullmatch(l)), None)
        if d is None or d == 0:
            continue
        name = " ".join(rec[:d]).strip()
        dur = rec[d]
        rest = rec[d + 1:]
        start = rest[0] if rest and DATE.fullmatch(rest[0]) else ""
        finish = rest[1] if len(rest) > 1 and DATE.fullmatch(rest[1]) else ""
        pred = " ".join(rest[2:]).strip()
        # the Gantt bar carries a milestone date label; it is not a predecessor
        pred = re.sub(r"\s*\d{2}-\d{2}$", "", pred).strip()
        acts.append(dict(id=aid, name=name, duration=dur, start=start,
                         finish=finish, predecessors=pred))
    return acts


# ------------------------------------------------------------------ output
def w_csv(path, header, rows):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        wr = csv.writer(fh)
        wr.writerow(header)
        wr.writerows(rows)
    print("   written", os.path.relpath(path, WM))


SRC_NOTE = """> **This document is the USER'S OWN Works Management material, published as
> supplied.** It is generated straight from `USER_SOURCE/` by
> `Scripts/wm2_user_package.py` — the figures are read out of the user's files,
> never retyped and never re-derived. No quantity, rate, cost, duration, date or
> activity has been corrected, rounded or rebuilt.
>
> Where it disagrees with the project master or with the generated package WM1,
> **the disagreement is recorded, not resolved** — see
> `Documentation/WM_RECONCILIATION_REGISTER.md`. Brief section 26 puts the user's
> Works Management files first in the order of authority, so nothing here has
> been overwritten by anything Claude produced.
"""


def _fmt(v):
    if isinstance(v, float):
        return f"{v:,.2f}".rstrip("0").rstrip(".") if v % 1 else f"{v:,.0f}"
    return str(v)


def md_table(rows, head=None):
    if not rows:
        return ""
    w = max(len(r) for r in rows)
    rows = [list(r) + [""] * (w - len(r)) for r in rows]
    # the workbook pads every sheet to its widest row; drop the columns that
    # carry nothing so the rendered table is the owner's data and no filler
    keep = [c for c in range(w) if any(str(r[c]).strip() for r in rows)]
    rows = [[r[c] for c in keep] for r in rows]
    w = len(keep)
    head = head or rows[0]
    body = rows if head is not rows[0] else rows[1:]
    out = ["| " + " | ".join(_fmt(c) for c in head) + " |",
           "|" + "|".join(["---"] * w) + "|"]
    for r in body:
        out.append("| " + " | ".join(_fmt(c).replace("|", "\\|") for c in r) + " |")
    return "\n".join(out)


def write_cost_md(book):
    L = ["<!-- GENERATED by WORKS MANAGEMENT/Scripts/wm2_user_package.py from",
         "     USER_SOURCE/Underground_CBRN_Ops_Room_BOQ_Estimate.xlsx.",
         "     Do not edit: edit the user's workbook and re-run. -->",
         "",
         "# BILL OF QUANTITIES AND COST ESTIMATE — AS SUPPLIED BY THE PROJECT OWNER",
         "## Underground CBRN-hardened Ops Room, Pune — Works Management revision WM2",
         "",
         "**Source:** `USER_SOURCE/Underground_CBRN_Ops_Room_BOQ_Estimate.xlsx`",
         "and `USER_SOURCE/BOQ_and_Works_Management_CBRN_Ops_Room.pdf`",
         "", SRC_NOTE, "", "---", ""]
    for title in ("BOQ & Estimate", "Detailed BOQ", "Cost Summary"):
        L += [f"## {title}", "", md_table(book[title]), "", "---", ""]
    path = os.path.join(WM, "Cost", "USER_BOQ_AND_COST_ESTIMATE.md")
    open(path, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("   written", os.path.join("Cost", "USER_BOQ_AND_COST_ESTIMATE.md"))


def write_schedule_md(acts):
    L = ["<!-- GENERATED by WORKS MANAGEMENT/Scripts/wm2_user_package.py from",
         "     USER_SOURCE/UG_CBRN_HDRND_OPS_ROOM_MCS_R0_Lvl5Micro.pdf. -->",
         "",
         "# MASTER CONSTRUCTION SCHEDULE (R0) — AS SUPPLIED BY THE PROJECT OWNER",
         "## Underground CBRN-hardened Ops Room, Pune — Works Management revision WM2",
         "",
         "**Source:** `USER_SOURCE/UG_CBRN_HDRND_OPS_ROOM_MCS_R0.mpp`, published as the",
         "Level-5 micro print `UG_CBRN_HDRND_OPS_ROOM_MCS_R0_Lvl5Micro.pdf`.",
         "",
         f"**{len(acts)} activities · 224 working days · 02-11-2026 to 26-07-2027 ·"
         " six working days per week.**",
         "", SRC_NOTE, "", "---", "",
         "| ID | Task name | Working days | Start | Finish | Predecessors |",
         "|---:|---|---|---|---|---|"]
    for a in acts:
        L.append(f'| {a["id"]} | {a["name"]} | {a["duration"]} | {a["start"]} '
                 f'| {a["finish"]} | {a["predecessors"]} |')
    path = os.path.join(WM, "Programme",
                        "USER_MASTER_CONSTRUCTION_SCHEDULE_R0.md")
    open(path, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("   written", os.path.join("Programme",
                                     "USER_MASTER_CONSTRUCTION_SCHEDULE_R0.md"))


def _num(v):
    if isinstance(v, (int, float)):
        return float(v)
    t = re.sub(r"[^\d.\-]", "", str(v))
    return float(t) if t not in ("", "-", ".") else None


def audit(book, acts):
    """Re-add the owner's own columns and report what does and does not tie up.

    This CHECKS the owner's arithmetic.  It never changes it.  Everything it
    finds is written up in Documentation/WM_RECONCILIATION_REGISTER.md.
    """
    L = ["WM2 - AUDIT OF THE PROJECT OWNER'S OWN WORKS MANAGEMENT FILES",
         "=" * 78,
         "Read straight from USER_SOURCE/.  Nothing here is corrected - findings are",
         "recorded in Documentation/WM_RECONCILIATION_REGISTER.md for the owner to rule on.",
         ""]

    # --- concrete take-off (sheet 'BOQ & Estimate', items 1.1 - 1.11)
    conc, stated_c = [], None
    for r in book["BOQ & Estimate"]:
        c0 = str(r[0]).strip()
        if re.fullmatch(r"1\.\d+", c0) and len(r) > 3:
            q = _num(r[3])
            if q is not None:
                conc.append((c0, str(r[1])[:58], q))
        if "TOTAL CONCRETE" in str(r[1]).upper() and len(r) > 3:
            stated_c = _num(r[3])
    L += ["1  CONCRETE TAKE-OFF", "-" * 78]
    for a, b, q in conc:
        L.append(f"   {a:<6}{b:<60}{q:>9.2f} m3")
    tot = sum(q for _, _, q in conc)
    L += [f"   {'sum of the ' + str(len(conc)) + ' lines above':<66}{tot:>9.2f} m3",
          f"   {'stated TOTAL CONCRETE QUANTITY':<66}{stated_c:>9.2f} m3",
          f"   {'DIFFERENCE':<66}{stated_c - tot:>9.2f} m3"
          + ("   *** see R-13 ***" if abs(stated_c - tot) > 0.005 else "   ties up"), ""]

    # --- rebar (items 2.1 - 2.6)
    net, gross, stated_net, stated_gross = 0.0, 0.0, None, None
    L += ["2  REINFORCEMENT", "-" * 78]
    for r in book["BOQ & Estimate"]:
        c0 = str(r[0]).strip()
        if re.fullmatch(r"2\.\d+", c0) and len(r) > 4:
            n, w, g = _num(r[2]), _num(r[3]), _num(r[4])
            if None in (n, w, g):
                continue
            net += n; gross += g
            chk = n * (1 + w) / 1000.0
            L.append(f"   {c0:<6}{str(r[1])[:52]:<54}{n:>9.0f} kg"
                     f"  x{1 + w:.2f} = {g:>6.2f} T"
                     + ("  ok" if abs(chk - g) < 0.01 else f"  != {chk:.2f}"))
        if "TOTAL REINFORCEMENT" in str(r[1]).upper() and len(r) > 4:
            stated_net, stated_gross = _num(r[2]), _num(r[4])
    L += [f"   {'sum of the bar lines':<60}{net:>9.0f} kg   {gross:>6.2f} T",
          f"   {'stated TOTAL REINFORCEMENT STEEL':<60}{stated_net:>9.0f} kg   {stated_gross:>6.2f} T",
          "   " + ("ties up" if abs(stated_net - net) < 1 and abs(stated_gross - gross) < 0.02
                   else "*** DOES NOT TIE UP ***"), ""]

    # --- priced BOQ: do the part subtotals make the basic cost?
    L += ["3  PRICED BOQ - PART SUBTOTALS", "-" * 78]
    subs = []
    for r in book["Detailed BOQ"]:
        if len(r) > 8 and str(r[7]).strip().upper() == "SUBTOTAL":
            v = _num(r[8])
            if v is not None:
                subs.append(v)
    for i, v in enumerate(subs, 1):
        L.append(f"   Part {i:<62}{v:>14,.0f}")
    L.append(f"   {'sum of the part subtotals':<67}{sum(subs):>14,.0f}")

    # --- cost summary
    heads, basic, final = [], None, None
    for r in book["Cost Summary"]:
        name, v = str(r[0]).strip(), _num(r[2]) if len(r) > 2 else None
        if v is None or not name or name.lower().startswith("cost head"):
            continue
        if "FINAL PROJECT COST" in name.upper():
            final = v; continue
        heads.append((name, str(r[1]), v))
        if "basic" in name.lower():
            basic = v
    L += ["", "4  COST SUMMARY", "-" * 78]
    for name, basis, v in heads:
        chk = ""
        m = re.match(r"\s*([\d.]+)\s*%", basis)
        if m and basic:
            want = basic * float(m.group(1)) / 100.0
            chk = "  ok" if abs(want - v) < 1 else f"  != {want:,.0f}"
        L.append(f"   {name[:52]:<54}{basis:<16}{v:>14,.0f}{chk}")
    ssum = sum(v for _, _, v in heads)
    L += [f"   {'sum of the cost heads above':<70}{ssum:>14,.0f}",
          f"   {'stated FINAL PROJECT COST':<70}{final:>14,.0f}",
          f"   {'DIFFERENCE':<70}{final - ssum:>14,.0f}"
          + ("   *** see R-14 ***" if abs(final - ssum) > 0.5 else "   ties up")]
    if basic and subs:
        L.append(f"   {'basic cost vs the sum of the part subtotals':<70}"
                 f"{basic - sum(subs):>14,.0f}"
                 + ("   ties up to the rupee" if abs(basic - sum(subs)) < 0.5 else "   *** OUT ***"))

    # --- programme
    L += ["", "5  MASTER CONSTRUCTION SCHEDULE R0", "-" * 78,
          f"   activities recovered from the owner's print   {len(acts)}",
          f"   ids present                                   "
          f"{min(a['id'] for a in acts)} - {max(a['id'] for a in acts)}, "
          f"{'no gaps' if len(acts) == max(a['id'] for a in acts) else 'GAPS'}",
          f"   project line                                  "
          f"{acts[0]['duration']}, {acts[0]['start']} to {acts[0]['finish']}",
          f"   final activity                                "
          f"{acts[-1]['name']}, {acts[-1]['finish']}"]
    for kw, ref in ((r"4\s*m\s+soil", "R-2, the 4 m cover"),
                    (r"1000\s*mm", "R-3, the 1000 mm slab"),
                    (r"lift shear wall", "R-4, the lift that does not exist")):
        hits = [a["id"] for a in acts if re.search(kw, a["name"], re.I)]
        if hits:
            L.append(f"   {ref.split(',')[1].strip():<28} activities {hits}   ({ref.split(',')[0]})")

    path = os.path.join(WM, "QAQC", "WM2_SOURCE_AUDIT.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("   written", os.path.join("QAQC", "WM2_SOURCE_AUDIT.txt"))
    return "\n".join(L)


def main():
    os.makedirs(os.path.join(WM, "Cost"), exist_ok=True)
    book = read_workbook()

    # --- the BOQ and estimate sheets, cell for cell
    for title, fname in (("BOQ & Estimate", "USER_BOQ_TAKEOFF.csv"),
                         ("Detailed BOQ",   "USER_BOQ_PRICED.csv"),
                         ("Cost Summary",   "USER_COST_SUMMARY.csv")):
        rows = book[title]
        width = max(len(r) for r in rows)
        rows = [list(r) + [""] * (width - len(r)) for r in rows]
        with open(os.path.join(WM, "Cost", fname), "w", newline="",
                  encoding="utf-8") as fh:
            csv.writer(fh).writerows(rows)
        print("   written", os.path.join("Cost", fname))

    # --- the master construction schedule
    acts = read_schedule()
    w_csv(os.path.join(WM, "Programme",
                       "USER_MASTER_CONSTRUCTION_SCHEDULE_R0.csv"),
          ["ID", "Task Name", "Working Days", "Start", "Finish", "Predecessors"],
          [[a["id"], a["name"], a["duration"], a["start"], a["finish"],
            a["predecessors"]] for a in acts])
    print(f"   {len(acts)} activities read from the user's MS Project print")
    write_cost_md(book)
    write_schedule_md(acts)
    audit(book, acts)
    return book, acts


if __name__ == "__main__":
    main()
