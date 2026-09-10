"""wm3_revised_owner_package.py — Works Management revision WM3.

Produces a REVISED version of the project owner's own BOQ, cost estimate and
master construction schedule, with the RC1 rulings applied (master Part H.14,
K.1c and WM_RECONCILIATION_REGISTER.md §9).

WHY THIS IS A SEPARATE FILE AND NOT AN EDIT
-------------------------------------------
`USER_SOURCE/` holds the owner's four files exactly as supplied and MUST stay
that way — it is the evidence every published figure is traced back to.  This
script reads those files, applies only what RC1 actually ruled, and writes the
result alongside as clearly-marked REVISED documents.  Both versions therefore
exist side by side and the difference between them is auditable.

WHAT IS APPLIED, AND WHAT IS DELIBERATELY NOT
---------------------------------------------
Applied — each one is a ruling with its basis in master K.1c:
  R-1   burster slab 300 mm M35 -> 200 mm M30  (thickness and grade only)
  R-6   "Sentry Post RCC Frame & Infill" -> RC frame; brick measured separately
  R-7   escape shaft collars ESC 1 / ESC 2 added - they were missing
  R-8   the 15 kVA generator added as a visible line - it was missing
  R-13  concrete total = the sum of its own lines
  R-14  final cost = the sum of its own cost heads
  R-2   programme: "4m Soil Overburdon" -> the ruled 2.0 m engineered cover
  R-3   programme: "1000 mm Thk" slab -> the ruled 900 mm
  R-4   programme: "Lift Shear Wall" -> there is no lift in this project
  R-5   programme title: the pre-M1 "(21.6 x 6.8)" -> "(22.0 x 6.2)"

NOT applied, on purpose:
  * No RATE is invented.  Where a line needs a price the project does not
    contain, it is carried at zero with DATA REQUIRED against it, so the gap is
    visible in the bill instead of silent.
  * No LABOUR figure is invented for a new line.
  * The burster-slab REINFORCEMENT is NOT silently changed.  T12 @ 150 both
    ways is 11.84 kg/m2 whatever the slab thickness, so the thickness ruling
    does not touch it; the owner's 2.89 t over their own implied area is a
    separate question and is flagged [REVIEW], not overwritten.
  * The owner's plan AREA for the cover is theirs and is left alone.  RC1 ruled
    on thickness and grade, not on area.
"""
import csv, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
WM   = os.path.abspath(os.path.join(HERE, ".."))
SRC  = os.path.join(WM, "USER_SOURCE")
XLSX = os.path.join(SRC, "Underground_CBRN_Ops_Room_BOQ_Estimate.xlsx")
OUT  = os.path.join(WM, "Cost")
PROG = os.path.join(WM, "Programme")

# --- RC1 rulings, as data ---------------------------------------------------
BURSTER_WAS_T, BURSTER_NOW_T = 0.300, 0.200          # R-1 thickness
BURSTER_WAS_G, BURSTER_NOW_G = "M35", "M30"          # R-1 grade
ESC_VOL   = 6.285          # R-7, WM1 item C-12: ESC 1 + ESC 2 collars, 250 RC, OD 1900
M35_RATE  = 8640           # the owner's own M35 casting rate
GEN_KVA   = 15             # R-8, master A.3 - Bay 8

REV_NOTE = ("RC1 REVISION, 10-09-2026 — master Part H.14 / K.1c and "
            "WM_RECONCILIATION_REGISTER.md section 9")


def num(v):
    if isinstance(v, (int, float)):
        return float(v)
    t = re.sub(r"[^\d.\-]", "", str(v))
    return float(t) if t not in ("", "-", ".") else None


def load():
    import openpyxl
    wb = openpyxl.load_workbook(XLSX, data_only=True)
    out = {}
    for ws in wb.worksheets:
        rows = []
        for r in ws.iter_rows(values_only=True):
            cells = ["" if c is None else c for c in r]
            if any(str(c).strip() for c in cells):
                rows.append(list(cells))
        out[ws.title] = rows
    return out


# ---------------------------------------------------------------- take-off
def revise_takeoff(rows):
    """Sheet 1: apply R-1 to the burster line, R-6 to the sentry line, and
    R-13 to the total.  Everything else is the owner's, untouched."""
    changes = []
    for r in rows:
        c0 = str(r[0]).strip()
        if c0 == "1.10":                                   # burster slab
            was_q = num(r[3])
            r[1] = ("Sacrificial RC Burster Slab in 2 m Soil Overburden "
                    "(200 mm — RC1 R-1, was 300 mm)")
            r[2] = BURSTER_NOW_G
            r[3] = round(was_q * BURSTER_NOW_T / BURSTER_WAS_T, 2)
            changes.append(("1.10 burster slab",
                            f"{BURSTER_WAS_G} {was_q:.2f} m3 at 300 mm",
                            f"{BURSTER_NOW_G} {r[3]:.2f} m3 at 200 mm"))
        if c0 == "1.11":                                   # sentry post
            r[1] = ("Detached Sentry Post — RC FRAME ONLY (footings, plinth, "
                    "columns, beams, slabs). Brick infill measured as "
                    "brickwork — RC1 R-6")
            changes.append(("1.11 sentry post", "'RCC Frame & Infill'",
                            "RC frame only; brick infill separate"))
    # R-7 - the escape shaft collars the bill did not have
    i = next(n for n, r in enumerate(rows) if str(r[0]).strip() == "1.11")
    rows.insert(i + 1, ["1.12",
                        "Escape shaft collars ESC 1 and ESC 2, 250 RC, OD 1900 "
                        "— ADDED BY RC1 R-7, missing from the bill", "M35",
                        ESC_VOL, "m³", "", "", ""])
    changes.append(("1.12 escape shaft collars", "not in the bill",
                    f"ADDED, {ESC_VOL:.3f} m3 M35"))
    # R-13 - the total is the sum of its own lines
    lines = [num(r[3]) for r in rows
             if re.fullmatch(r"1\.\d+", str(r[0]).strip()) and num(r[3]) is not None]
    for r in rows:
        if "TOTAL CONCRETE" in str(r[1]).upper():
            was = num(r[3])
            r[3] = round(sum(lines), 2)
            r[1] = "TOTAL CONCRETE QUANTITY  (sum of the lines above — RC1 R-13)"
            changes.append(("Total concrete", f"stated {was:.2f} m3",
                            f"{r[3]:.2f} m3, the sum of its own {len(lines)} lines"))
    return rows, changes


# ------------------------------------------------------------- priced BOQ
def revise_priced(rows):
    changes, sub_idx = [], []
    for n, r in enumerate(rows):
        desc = str(r[2]) if len(r) > 2 else ""
        if "Concrete Burster Slab" in desc:                # R-1
            was_q, rate = num(r[4]), num(r[5])
            was_mat, was_tot = num(r[6]), num(r[8])
            was_lab = was_tot - was_mat
            q = round(was_q * BURSTER_NOW_T / BURSTER_WAS_T, 2)
            mat = round(q * rate)
            lab = round(was_lab * BURSTER_NOW_T / BURSTER_WAS_T)
            r[2] = ("Engineered burster slab (200 mm M30 — RC1 R-1, was 300 mm "
                    "M35). Rate carried from the owner's own bill; a grade "
                    "change may warrant a rate review [REVIEW]")
            r[4], r[6], r[8] = q, mat, mat + lab
            r[7] = f"{r[7]}  — scaled with the quantity"
            changes.append(("Part III burster slab",
                            f"{was_q:.2f} m3, Rs {was_tot:,.0f}",
                            f"{q:.2f} m3, Rs {mat+lab:,.0f}"))
        if "Sentry Post RCC Frame" in desc:                # R-6
            r[2] = ("Sentry post RC frame — brick infill measured as brickwork "
                    "(RC1 R-6)")
        if "Burster Slab Mesh" in desc:                    # R-12, flagged only
            r[2] = (str(r[2]) + "  [REVIEW — RC1 R-12: T12 @ 150 B/W is "
                    "11.84 kg/m2 whatever the slab thickness, so the R-1 "
                    "thickness ruling does NOT change this line. The owner's "
                    "tonnage over their own plan area implies about 15 kg/m2; "
                    "that is a separate question and is NOT overwritten here]")
        if len(r) > 7 and str(r[7]).strip().upper() == "SUBTOTAL":
            sub_idx.append(n)

    # R-7 and R-8 - the two real omissions, made visible
    p3 = sub_idx[2]
    rows.insert(p3, ["PART III - SUPERSTRUCTURE & STRUCTURAL RCC", 11,
                     "Escape shaft collars ESC 1 and ESC 2, 250 RC, OD 1900 — "
                     "ADDED BY RC1 R-7", "Cum", ESC_VOL, M35_RATE,
                     round(ESC_VOL * M35_RATE),
                     "[DATA REQUIRED — labour not priced here; no figure for it "
                     "exists in the project and none is invented]",
                     round(ESC_VOL * M35_RATE)])
    changes.append(("Part III escape shaft collars", "not in the bill",
                    f"ADDED, {ESC_VOL:.3f} m3, material Rs "
                    f"{ESC_VOL*M35_RATE:,.0f}, labour DATA REQUIRED"))
    sub_idx = [n + 1 if n >= p3 else n for n in sub_idx]

    p5 = sub_idx[4] + 1
    rows.insert(p5, ["PART V - CBRN, EMP, CLOSURES & ANCILLARY SERVICES", 11,
                     f"Standby generator {GEN_KVA} kVA in Bay 8, with fuel "
                     "system, exhaust and acoustic treatment — ADDED BY RC1 "
                     "R-8. The bill prices the 2 600 m3/h combustion and "
                     "cooling air path through BV-4/BV-5 but not the machine",
                     "Set", 1,
                     "[DATA REQUIRED — vendor quotation. NO RATE IS INVENTED]",
                     0, "[DATA REQUIRED]", 0])
    changes.append(("Part V standby generator", "not in the bill",
                    "ADDED as a visible line, carried at ZERO — "
                    "DATA REQUIRED, no rate invented"))

    # recompute the five part subtotals from their own lines
    part_of, totals = {}, {}
    for r in rows:
        p = str(r[0]).strip()
        if p.startswith("PART ") and len(r) > 8 and num(r[8]) is not None:
            totals[p] = totals.get(p, 0.0) + num(r[8])
    order = [p for p in dict.fromkeys(str(r[0]).strip() for r in rows)
             if p.startswith("PART ")]
    k = 0
    for r in rows:
        if len(r) > 7 and str(r[7]).strip().upper() == "SUBTOTAL":
            was = num(r[8])
            r[8] = round(totals[order[k]])
            if abs(was - r[8]) > 0.5:
                changes.append((f"{order[k][:14]} subtotal",
                                f"Rs {was:,.0f}", f"Rs {r[8]:,.0f}"))
            k += 1
    return rows, changes, [round(totals[p]) for p in order]


# ------------------------------------------------------------ cost summary
def revise_summary(rows, basic):
    changes, heads = [], []
    for r in rows:
        name = str(r[0]).strip()
        if not name or name.lower().startswith("cost head"):
            continue
        if "FINAL PROJECT COST" in name.upper():
            continue
        if "basic" in name.lower():
            was = num(r[2]); r[2] = basic
            if abs(was - basic) > 0.5:
                changes.append(("Total basic cost", f"Rs {was:,.0f}",
                                f"Rs {basic:,.0f}, the sum of the five parts"))
            heads.append(basic); continue
        m = re.match(r"\s*([\d.]+)\s*%", str(r[1]))
        if m:
            was = num(r[2]); r[2] = round(basic * float(m.group(1)) / 100.0)
            heads.append(r[2])
            if abs(was - r[2]) > 0.5:
                changes.append((name[:34], f"Rs {was:,.0f}", f"Rs {r[2]:,.0f}"))
    for r in rows:
        if "FINAL PROJECT COST" in str(r[0]).upper():
            was = num(r[2]); r[2] = round(sum(heads))
            changes.append(("FINAL PROJECT COST", f"stated Rs {was:,.0f}",
                            f"Rs {r[2]:,.0f}, the sum of its own cost heads "
                            f"(RC1 R-14 closed a Rs 1,00,000 gap)"))
    return rows, changes, round(sum(heads))


# ------------------------------------------------------------- programme
def revise_programme():
    """R-2, R-3, R-4, R-5 — stale wording in the owner's own schedule."""
    src = os.path.join(PROG, "USER_MASTER_CONSTRUCTION_SCHEDULE_R0.csv")
    rows = list(csv.reader(open(src, encoding="utf-8")))
    hdr, body = rows[0], rows[1:]
    subs = [
        (r"\(21\.6 x 6\.8\)", "(22.0 x 6.2)", "R-5"),
        (r"4m Soil Overburdon", "2m Engineered Cover", "R-2"),
        (r"4m Soil Overburden",  "2m Engineered Cover", "R-2"),
        (r"1000\s*mm Thk", "900 mm Thk", "R-3"),
        (r"\(1000 mm Thk\)", "(900 mm Thk)", "R-3"),
        (r"Column, Staircase & Lift Shear Wall", "Column & Staircase Shear Wall", "R-4"),
    ]
    changes, out = [], []
    for r in body:
        name, hit = r[1], []
        for pat, rep, ref in subs:
            if re.search(pat, name):
                name = re.sub(pat, rep, name); hit.append(ref)
        if hit:
            changes.append((r[0], r[1], name, "+".join(sorted(set(hit)))))
        out.append([r[0], name] + r[2:])
    return hdr, out, changes


# ----------------------------------------------------------------- output
def w_csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        csv.writer(fh).writerows(rows)
    print("   written", os.path.relpath(path, WM))


def write_xlsx(book, path):
    import openpyxl
    from openpyxl.styles import Font, Alignment
    wb = openpyxl.Workbook(); wb.remove(wb.active)
    for title, rows in book.items():
        ws = wb.create_sheet(title[:31])
        for r in rows:
            ws.append(r)
        for col in ws.columns:
            w = max((len(str(c.value)) for c in col if c.value is not None),
                    default=8)
            ws.column_dimensions[col[0].column_letter].width = min(max(w + 2, 10), 72)
        for c in ws[1]:
            c.font = Font(bold=True)
        ws.freeze_panes = "A2"
        for row in ws.iter_rows():
            for c in row:
                c.alignment = Alignment(vertical="top", wrap_text=True)
    wb.save(path)
    print("   written", os.path.relpath(path, WM))


def md_table(rows):
    w = max(len(r) for r in rows)
    rows = [list(r) + [""] * (w - len(r)) for r in rows]
    keep = [c for c in range(w) if any(str(r[c]).strip() for r in rows)]
    rows = [[r[c] for c in keep] for r in rows]
    def f(v):
        if isinstance(v, float):
            return f"{v:,.2f}".rstrip("0").rstrip(".") if v % 1 else f"{v:,.0f}"
        return str(v).replace("|", "\\|")
    out = ["| " + " | ".join(f(c) for c in rows[0]) + " |",
           "|" + "|".join(["---"] * len(keep)) + "|"]
    for r in rows[1:]:
        out.append("| " + " | ".join(f(c) for c in r) + " |")
    return "\n".join(out)


def main():
    book = load()
    t_rows, t_ch = revise_takeoff([list(r) for r in book["BOQ & Estimate"]])
    p_rows, p_ch, subs = revise_priced([list(r) for r in book["Detailed BOQ"]])
    s_rows, s_ch, final = revise_summary([list(r) for r in book["Cost Summary"]],
                                         sum(subs))
    hdr, prog, pr_ch = revise_programme()

    os.makedirs(OUT, exist_ok=True)
    revised = {"BOQ & Estimate": t_rows, "Detailed BOQ": p_rows,
               "Cost Summary": s_rows}
    write_xlsx(revised, os.path.join(
        OUT, "REVISED_Underground_CBRN_Ops_Room_BOQ_Estimate_RC1.xlsx"))
    for title, fname in (("BOQ & Estimate", "REVISED_BOQ_TAKEOFF_RC1.csv"),
                         ("Detailed BOQ",   "REVISED_BOQ_PRICED_RC1.csv"),
                         ("Cost Summary",   "REVISED_COST_SUMMARY_RC1.csv")):
        w_csv(os.path.join(OUT, fname), revised[title])
    w_csv(os.path.join(PROG, "REVISED_MASTER_CONSTRUCTION_SCHEDULE_R1.csv"),
          [hdr] + prog)

    # --- the markdown record, with the before/after of every change
    L = ["<!-- GENERATED by WORKS MANAGEMENT/Scripts/wm3_revised_owner_package.py",
         "     from USER_SOURCE/.  Do not edit by hand. -->",
         "",
         "# REVISED BILL OF QUANTITIES AND COST ESTIMATE — RC1 RULINGS APPLIED",
         "## Underground CBRN-hardened Ops Room, Pune — Works Management revision WM3",
         "",
         f"**{REV_NOTE}**", "",
         "> **This is the project owner's own estimate with the RC1 rulings applied, and",
         "> nothing else.** The originals stay untouched in `USER_SOURCE/`, and the",
         "> as-supplied version stays published in `Cost/USER_BOQ_*`. Both versions",
         "> therefore exist",
         "> side by side and every difference between them is listed below.",
         "",
         "> **No rate was invented.** Where a line needs a price the project does not",
         "> contain, it is carried at **zero with DATA REQUIRED against it**, so the gap is",
         "> visible in the bill instead of silent. **The final cost below is therefore a",
         "> LOWER BOUND** until the generator is priced.",
         "", "---", "",
         "## What changed, line by line", "",
         "| Item | Was | Now |", "|---|---|---|"]
    for a, b, c in t_ch + p_ch + s_ch:
        L.append(f"| {a} | {b} | {c} |")
    L += ["", "## Programme wording corrected", "",
          "| ID | Was | Now | Ruling |", "|---|---|---|---|"]
    for i, was, now, ref in pr_ch:
        L.append(f"| {i} | {was} | {now} | **{ref}** |")
    L += ["", "---", ""]
    for title in ("BOQ & Estimate", "Detailed BOQ", "Cost Summary"):
        L += [f"## {title} — REVISED", "", md_table(revised[title]), "", "---", ""]
    path = os.path.join(OUT, "REVISED_BOQ_AND_COST_ESTIMATE_RC1.md")
    open(path, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("   written", os.path.relpath(path, WM))
    print(f"\n   {len(t_ch+p_ch+s_ch)} bill changes, {len(pr_ch)} programme "
          f"activities reworded")
    print(f"   REVISED FINAL PROJECT COST  Rs {final:,.0f}  "
          f"(a LOWER BOUND - the generator is unpriced)")
    return final


if __name__ == "__main__":
    main()
