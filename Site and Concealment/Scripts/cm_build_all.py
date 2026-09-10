"""cm_build_all.py  --  rebuild the whole SITE AND CONCEALMENT package.

    python3 cm_build_all.py

Writes the policy, the drawing and the validation report.  The signature
inventory in all three comes from cm_data.py, which reads the confirmed
geometry out of Drainage/Scripts/mep_proj.py and the sentry post out of master
A.4.1, so no height or size on the drawing can disagree with the policy.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
SHARED = os.path.normpath(os.path.join(ROOT, "..", "Drainage", "Scripts"))


def main():
    sys.path.insert(0, HERE)
    import cm_docs
    import cm_sheets
    cm_docs.main()
    cm_sheets.main()

    os.makedirs(os.path.join(ROOT, "QAQC"), exist_ok=True)
    rep = os.path.join(ROOT, "QAQC", "CM_DRAWING_VALIDATION.txt")
    r = subprocess.run([sys.executable,
                        os.path.join(SHARED, "mep_validate.py"),
                        os.path.join(ROOT, "DXF")],
                       capture_output=True, text=True)
    with open(rep, "w", encoding="utf-8") as f:
        f.write("SITE AND CONCEALMENT  -  DXF VALIDATION  -  revision CAM2\n")
        f.write("Produced by Drainage/Scripts/mep_validate.py, the same "
                "validator used by the\nDRAINAGE, HVAC, SCHEDULE OF FINISHES "
                "and FIRE AND LIFE SAFETY packages.\n")
        f.write("=" * 78 + "\n\n")
        f.write(r.stdout)
        if r.stderr:
            f.write("\nSTDERR\n" + r.stderr)
    print("validation written:", os.path.relpath(rep, ROOT))
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
