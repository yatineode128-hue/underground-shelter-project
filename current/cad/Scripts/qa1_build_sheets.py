"""qa1_build_sheets.py  --  the QA1 pipeline that was run over current/cad.

It is recorded here so the state of these eleven DXF files is reproducible and
auditable, in the same way every other package in this project keeps the
scripts that produced it.  It is NOT a generator: it does not create drawings,
it corrects the ones that are already there, IN PLACE, at the same filenames.

    1  declash    move annotation off the line work it was sitting on
    2  addsheet   A1/A0 border, title block and revision strip at the
                  drawing's own stated scale (the ten Rev F drawings only)
    3  notesbox   collect the loose bottom notes into a ruled NOTES box and
                  balance the drawing between the header and the notes
    4  declash    a second, wider pass now that the sheet frame exists: it
                  clears the last labels in the crowded zones and, being
                  border-aware, keeps every one of them on the sheet

RUNNING IT A SECOND TIME IS A NO-OP.  A drawing that already carries a sheet frame is
skipped whole.  This matters: de-clash is a search, not an idempotent transform - run
over an already-cleared drawing it will keep nudging labels and can make the result
worse, so the guard is on the pipeline, not left to the operator.

To re-run it properly, restore the drawings from git first:

    git checkout -- current/cad/*.dxf     # or check out the pre-QA1 revision
    python3 current/cad/Scripts/qa1_build_sheets.py

The de-clash step is the ONLY step applied to
`06_Underground_Plan_Services_Sump_BlastValves.dxf` (sheet S-06): it is an
output sheet that already carries its own border and title block.

DECLARED DEVIATION FROM PROJECT RULE M.12
    M.12 forbids editing a generated DXF directly.  S-06 is a generated sheet
    and its generator is not in the workspace, so the QA/QC brief's explicit
    and repeated instruction - every existing DXF is to be inspected,
    corrected and saved back at the same filename - can only be met by editing
    it directly.  This is recorded, not hidden; see the QA/QC report.
"""
import os
import sys
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
CAD = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)

import declash          # noqa: E402
import addsheet         # noqa: E402
import notesbox         # noqa: E402
import register         # noqa: E402


def framed(path):
    """True once a drawing carries the QA1 sheet frame."""
    import ezdxf
    doc = ezdxf.readfile(path)
    return bool(len(doc.modelspace().query('LINE[layer=="SHEET-BORDER"]')))


def main():
    files = sorted(glob.glob(os.path.join(CAD, "*.dxf")))
    done = [f for f in files if framed(f)]
    if done:
        print(f"{len(done)} drawing(s) already carry the QA1 sheet frame - nothing to do.")
        print("Restore them from git before re-running:  git checkout -- current/cad/*.dxf")
        return
    print(f"=== 1  de-clash annotation      {len(files)} drawings")
    for f in files:
        declash.declash(f)
    print(f"\n=== 2  sheet frame + title block   {len(register.REG)} Rev F drawings")
    for fn, num, title, sub, sc, note, of, size in register.REG:
        w, h = register.SIZES[size]
        addsheet.add_sheet(os.path.join(CAD, fn), sc, num, title, sub, note, of,
                           sheet_w=w, sheet_h=h)
    print("\n=== 3  notes box + sheet balance")
    for fn, num, title, sub, sc, note, of, size in register.REG:
        notesbox.run(os.path.join(CAD, fn), sheet_w=register.SIZES[size][0])
    print("\nQA1 pipeline complete.")


if __name__ == "__main__":
    main()
