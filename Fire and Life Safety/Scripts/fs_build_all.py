"""fs_build_all.py  --  rebuild the whole FIRE AND LIFE SAFETY package.

    python3 fs_build_all.py

Writes the plan, the route schedule, both A1 drawings and the validation
report.  Every number in all four comes from fs_data.py, which computes them
from the confirmed project geometry in Drainage/Scripts/mep_proj.py.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
SHARED = os.path.normpath(os.path.join(ROOT, "..", "Drainage", "Scripts"))


def main():
    sys.path.insert(0, HERE)
    import fs_docs
    import fs_schedules
    import fs_sheets
    fs_docs.main()
    fs_schedules.main()
    fs_sheets.main()

    os.makedirs(os.path.join(ROOT, "QAQC"), exist_ok=True)
    rep = os.path.join(ROOT, "QAQC", "FS_DRAWING_VALIDATION.txt")
    r = subprocess.run([sys.executable,
                        os.path.join(SHARED, "mep_validate.py"),
                        os.path.join(ROOT, "DXF")],
                       capture_output=True, text=True)
    with open(rep, "w", encoding="utf-8") as f:
        f.write("FIRE AND LIFE SAFETY  -  DXF VALIDATION  -  revision FS2\n")
        f.write("Produced by Drainage/Scripts/mep_validate.py, the same "
                "validator used by the\nDRAINAGE, HVAC and SCHEDULE OF "
                "FINISHES packages.  11 checks per file.\n")
        f.write("=" * 78 + "\n\n")
        f.write(r.stdout)
        if r.stderr:
            f.write("\nSTDERR\n" + r.stderr)
    print("validation written:", os.path.relpath(rep, ROOT))
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
