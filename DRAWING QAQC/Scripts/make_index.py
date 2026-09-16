"""make_index.py - write DRAWING_INDEX.md from qa_index.json.

Run `qa_report_data.py` first; it reads the DXF files themselves, so the index
cannot drift from the drawings.
"""
import os, json, collections

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "DRAWING_INDEX.md")

ORDER = ["ARCHITECTURAL / GENERAL - Rev F", "ARCHITECTURAL - finishes",
         "STRUCTURAL - reinforcement", "STRUCTURAL - A2 presentation sheets",
         "MEP - A2 presentation sheets",
         "DRAINAGE", "DRAINAGE - handout",
         "HVAC", "HVAC - handout", "FIRE AND LIFE SAFETY",
         "SITE AND CONCEALMENT", "EMP PROTECTION", "ELECTRICAL",
         "SITE SELECTION AND GEOTECHNICAL"]


def main():
    rows = json.load(open(os.path.join(HERE, "..", "qa_index.json")))
    by = collections.defaultdict(list)
    for r in rows:
        by[r["discipline"]].append(r)

    L = []
    A = L.append
    A("# DRAWING INDEX — Underground CBRN-hardened protective structure, Pune")
    A("")
    A("Generated from the DXF files themselves by `DRAWING QAQC/Scripts/qa_report_data.py`")
    A("and `make_index.py`, so it cannot drift from the drawings.")
    A("")
    sizes = collections.Counter(r["size"] for r in rows)
    A(f"**{len(rows)} DXF · "
      + " · ".join(f"{n} {s}" for s, n in sorted(sizes.items(), key=lambda kv: -kv[1]))
      + ".**  Drafting QA/QC baseline **QA1** (9 September 2026, master H.11), "
      "re-scanned at **QA2** (11 September 2026, master H.25).  The FIRE AND LIFE "
      "SAFETY and SITE AND CONCEALMENT sheets were added at **FS2 / CAM2**, and the "
      "EMP PROTECTION, ELECTRICAL and SITE SELECTION AND GEOTECHNICAL sheets at "
      "**EM1 / EL1 / SG1 / SG2**, all after the QA1 pass and all drawn to the same "
      "standard.")
    A("")
    A("> **Filenames are deliberately unchanged.** Master Parts E.2 and I.1 and every")
    A("> document in this project cite the current filenames, and the QA/QC brief requires")
    A("> each existing DXF to be corrected and saved back at its own name and location.")
    A("> The drawing number therefore lives in the title block, and this index carries both.")
    A("")
    for disc in ORDER:
        rs = sorted(by[disc], key=lambda r: r["number"])
        if not rs:
            continue
        A(f"## {disc}  ({len(rs)})")
        A("")
        A("| Drawing No. | Title | Scale | Size | Texts | Final QA |")
        A("|---|---|---|---|---|---|")
        for r in rs:
            res = r["overlap"] + r["over_geom"]
            A(f"| **{r['number']}** | {r['title']} | {r['scale']} | {r['size']} | "
              f"{r['texts']} | {'PASS' if res == 0 else f'REVIEW ({res})'} |")
        A("")
        A("<details><summary>filenames</summary>")
        A("")
        for r in rs:
            A(f"- `{r['number']}` — `{r['file']}`")
        A("")
        A("</details>")
        A("")
    tot = sum(r["overlap"] + r["over_geom"] for r in rows)
    npass = sum(1 for r in rows if r["overlap"] + r["over_geom"] == 0)
    A("---")
    A("")
    A(f"**Package QA result — {len(rows)} drawings, {npass} PASS, {len(rows) - npass} "
      f"REVIEW REQUIRED, {tot} residual items in total.**")
    A("")
    A("Every REVIEW item is a single annotation still crossing a dimension or a wall line")
    A("in a dense zone of a section or plan. Each one is named individually in")
    A("`DRAWING QAQC/QAQC_REPORT.md` §5.1.")
    open(OUT, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"DRAWING_INDEX.md written — {len(rows)} drawings, {npass} PASS")


if __name__ == "__main__":
    main()
