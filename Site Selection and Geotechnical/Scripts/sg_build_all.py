"""
sg_build_all.py  --  rebuild the SITE SELECTION AND GEOTECHNICAL package
(revisions SG1 + SG2).

    python3 sg_build_all.py

Runs the SG1 modules then the SG2 modules, then validates all five drawings with the project's own shared validator and writes the
validation report into QAQC/.

NOTHING IN ANY SHARED LIBRARY IS MODIFIED.  sg_dxf.py subclasses
Drainage/Scripts/mep_dxf.py and uses the SCOPE_NOTE / TB_SCOPE / DATE hooks
FS2 / CAM2 added, exactly as the EMP and ELECTRICAL packages do, so DRAINAGE,
HVAC, SCHEDULE OF FINISHES, FIRE AND LIFE SAFETY, SITE AND CONCEALMENT, EMP
PROTECTION and ELECTRICAL all regenerate byte for byte unchanged.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.abspath(os.path.join(HERE, ".."))
ROOT = os.path.abspath(os.path.join(PKG, ".."))
SHARED = os.path.join(ROOT, "Drainage", "Scripts")


def run(script):
    print(f"\n=== {script} " + "=" * (58 - len(script)))
    if subprocess.run([sys.executable, os.path.join(HERE, script)],
                      cwd=HERE).returncode:
        sys.exit(f"FAILED: {script}")


def main():
    run("sg_calc.py")          # SG1 - the geotechnical calculation
    run("sg_schedules.py")     # SG1 - five schedules
    run("sg_docs.py")          # SG1 - the section, README, drawing index
    run("sg_sheets.py")        # SG1 - SG-001, SG-101, SG-201
    run("sg_site_calc.py")     # SG2 - the siting calculation
    run("sg_site_docs.py")     # SG2 - the layout section + four schedules
    run("sg_site_sheets.py")   # SG2 - SG-102, SG-202

    print("\n=== validation " + "=" * 51)
    r = subprocess.run([sys.executable,
                        os.path.join(SHARED, "mep_validate.py"),
                        os.path.join(PKG, "DXF")],
                       capture_output=True, text=True)
    os.makedirs(os.path.join(PKG, "QAQC"), exist_ok=True)
    rep = os.path.join(PKG, "QAQC", "SG_DRAWING_VALIDATION.txt")
    with open(rep, "w", encoding="utf-8") as f:
        f.write("SITE SELECTION AND GEOTECHNICAL  -  DXF VALIDATION  -  "
                "revision SG1\n")
        f.write("Produced by Drainage/Scripts/mep_validate.py, the same "
                "validator used by the\nDRAINAGE, HVAC, SCHEDULE OF "
                "FINISHES, FIRE AND LIFE SAFETY, SITE AND CONCEALMENT,\n"
                "EMP PROTECTION and ELECTRICAL packages.\n")
        f.write("=" * 78 + "\n\n")
        f.write(r.stdout)
        if r.stderr:
            f.write("\nSTDERR\n" + r.stderr)
    print(r.stdout)
    print("validation written:", os.path.relpath(rep, PKG))
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
