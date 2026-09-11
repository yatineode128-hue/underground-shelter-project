"""
em_build_all.py  --  rebuild the entire EMP PROTECTION package (revision EM1).

    python3 em_build_all.py

Runs, in order:
    em_calc.py        every derivation -> Calculations/EMP_CALC_OUTPUT.txt
    em_schedules.py   five schedules   -> Schedules/*.md and *.csv
    em_sheets.py      six A1 drawings  -> DXF/EM-*.dxf

Then validates every drawing with the project's own shared validator,
Drainage/Scripts/mep_validate.py.

NOTHING IN ANY SHARED LIBRARY IS MODIFIED by this package.  Drainage, HVAC
and Schedule of Finishes regenerate byte-identically after it exists.

The Documentation/*.md files are written prose, not generated - but every
figure in them comes from EMP_CALC_OUTPUT.txt.
"""
import os
import sys
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))


def run(script):
    print(f"\n=== {script} " + "=" * (60 - len(script)))
    r = subprocess.run([sys.executable, os.path.join(HERE, script)],
                       cwd=HERE)
    if r.returncode:
        sys.exit(f"FAILED: {script}")


if __name__ == "__main__":
    run("em_calc.py")
    run("em_schedules.py")
    run("em_sheets.py")
    print("\n=== validation " + "=" * 53)
    sys.path.insert(0, os.path.join(ROOT, "Drainage", "Scripts"))
    import mep_validate                                   # noqa: E402
    rc, _ = mep_validate.run([os.path.join(HERE, "..", "DXF")])
    sys.exit(rc)
