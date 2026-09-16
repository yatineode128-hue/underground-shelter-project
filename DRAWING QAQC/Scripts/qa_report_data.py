"""qa_report_data.py - collect the drawing index and the QA metrics from the
DXF files themselves, so the index and the report cannot drift from the files.
"""
import os, sys, glob, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
import ezdxf, ezdxf.bbox                       # noqa: E402
import dxfqa, modelqa, panelclash              # noqa: E402

# the same "hard" layer set the de-clash tool uses, so the report and the tool
# can never disagree about what counts as a clash
sys.path.insert(0, os.path.join(ROOT, "current", "cad", "Scripts"))
from declash import SOLID as HARD_LAYERS      # noqa: E402

DISCIPLINE = [
    ("Structural CAD/DXF/", "STRUCTURAL - reinforcement"),
    # MEP010 / MEP011 share the folder and the frame with STR006...STR009 but
    # are services sheets, so they are matched by filename prefix FIRST
    ("Presentation Sheets/DXF/MEP", "MEP - A2 presentation sheets"),
    ("Presentation Sheets/DXF/", "STRUCTURAL - A2 presentation sheets"),
    ("Drainage/DXF/",       "DRAINAGE"),
    ("Drainage/Handout/",   "DRAINAGE - handout"),
    ("HVAC/DXF/",           "HVAC"),
    ("HVAC/Handout/",       "HVAC - handout"),
    ("Schedule of Finishes/DXF/", "ARCHITECTURAL - finishes"),
    ("Fire and Life Safety/DXF/", "FIRE AND LIFE SAFETY"),
    ("Site and Concealment/DXF/", "SITE AND CONCEALMENT"),
    ("EMP Protection/DXF/",  "EMP PROTECTION"),
    ("Electrical/DXF/",      "ELECTRICAL"),
    ("Site Selection and Geotechnical/DXF/", "SITE SELECTION AND GEOTECHNICAL"),
    ("current/cad/",        "ARCHITECTURAL / GENERAL - Rev F"),
]

# the ten Rev F drawings carry their number in the title block, not the filename
from register_map import REVF_NUMBERS   # noqa: E402


def sheet_size(doc, scale=1.0):
    """The Rev F drawings are drawn in model millimetres, so their sheet is the
    paper size multiplied by the plot scale."""
    b = ezdxf.bbox.extents(doc.modelspace(), fast=True)
    w = (b.extmax.x - b.extmin.x) / scale
    h = (b.extmax.y - b.extmin.y) / scale
    # The A2 presentation series (ARCH001.. / STR006..) follows the Revit sheet
    # frame: the border is INSET from the page edge at 27, 19.1 -> 567, 400.9, so
    # the drawn extents are 540 x 381.8, not the 594 x 420 page.
    for nm, (sw, sh) in (("A1", (841, 594)), ("A0", (1189, 841)),
                         ("A2", (594, 420)), ("A2", (540, 381.8)),
                         ("A4", (297, 210))):
        if abs(w - sw) < 3 and abs(h - sh) < 3:
            return nm
    return f"{w:.0f} x {h:.0f}"


def scale_of(doc):
    best = None
    for e in doc.modelspace().query("TEXT"):
        t = e.dxf.text
        if re.search(r"SCALE", t, re.I):
            m = re.search(r"(1\s*:\s*[\d.]+|AS NOTED|NOT TO SCALE|AS SHOWN)", t, re.I)
            if m and (best is None or len(t) < len(best)):
                best = m.group(1)
    return best or "-"


TITLE_OVERRIDE = {
    # S-06 carries its title in its own title block, not in a top strip
    "S-06": "UNDERGROUND PLAN - SERVICES AND DRAINAGE",
    # the A2 presentation sheets carry their title in the Revit-style title
    # block, stacked over five lines, so there is no single text to read
    "STR006": "STRUCTURAL REINFORCEMENT DETAILING - ROOF SLAB AND MAT FOUNDATION",
    "STR007": "STRUCTURAL REINFORCEMENT DETAILING - 600 SHEAR WALL AND MAIN STAIRCASE",
    "STR008": "STRUCTURAL REINFORCEMENT DETAILING OF SENTRY POST - BEAMS AND COLUMN",
    "STR009": "STRUCTURAL REINFORCEMENT DETAILING OF SENTRY POST - FOOTING AND SLAB",
    "MEP010": "HVAC AND EMP ZONE LAYOUT PLANS - UNDERGROUND LEVEL",
    "MEP011": "SEPTIC TANK, SOAK PIT AND SUMP PIT - PLANS, SECTIONS AND SCHEDULES",
}


def title_of(doc, number):
    if number in TITLE_OVERRIDE:
        return TITLE_OVERRIDE[number]
    for e in doc.modelspace().query("TEXT"):
        t = e.dxf.text.strip()
        if t.startswith(number + " "):
            return t[len(number):].strip()
    # A4 handouts and S-06 carry their title as the largest text on the sheet
    best = None
    for e in doc.modelspace().query("TEXT"):
        t = e.dxf.text.strip()
        if len(t) < 8:
            continue
        if best is None or e.dxf.height > best[0]:
            best = (e.dxf.height, t)
    return best[1] if best else "-"


def collect():
    rows = []
    for f in sorted(glob.glob(os.path.join(ROOT, "**", "*.dxf"), recursive=True)):
        rel = os.path.relpath(f, ROOT).replace(os.sep, "/")
        if rel.startswith(".git"):
            continue
        disc = next((d for p, d in DISCIPLINE if rel.startswith(p)), "OTHER")
        base = os.path.basename(rel)
        if rel.startswith("current/cad/"):
            num = REVF_NUMBERS.get(base, "S-06")
        else:
            num = base.split("_")[0]
        doc = ezdxf.readfile(f)
        plot = 50.0 if (rel.startswith("current/cad/") and base != "06_Underground_Plan_Services_Sump_BlastValves.dxf") else 1.0
        a = dxfqa.audit(f)
        m = modelqa.analyse(f)
        hard = len([c for c in m["text_over_geometry"]
                    if c[2] >= 3 and any(l in HARD_LAYERS for l in c[3])])
        pc = 0 if rel.startswith("current/cad/") else len(panelclash.analyse(f)[1])
        rows.append(dict(file=rel, base=base, number=num, discipline=disc,
                         title=title_of(doc, num), scale=scale_of(doc),
                         size=sheet_size(doc, plot), texts=a["n_text"],
                         overlap=len(a["issues"].get("text_overlap", [])),
                         over_geom=hard, geom_in_panel=pc))
    return rows


if __name__ == "__main__":
    rows = collect()
    json.dump(rows, open(os.path.join(HERE, "..", "qa_index.json"), "w"), indent=1)
    print(f"collected {len(rows)} drawings")
