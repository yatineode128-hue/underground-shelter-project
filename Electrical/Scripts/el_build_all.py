"""
el_build_all.py  --  rebuild the ELECTRICAL AND POWER package (revision EL1).

    python3 el_build_all.py

Runs el_calc.py, el_schedules.py and el_sheets.py, then validates the drawing
with the project's own shared validator.  Nothing in any shared library is
modified: el_dxf.py subclasses mep_dxf.py and uses the SCOPE_NOTE / TB_SCOPE /
DATE hooks FS2 / CAM2 added.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))


def run(script):
    print(f"\n=== {script} " + "=" * (58 - len(script)))
    if subprocess.run([sys.executable, os.path.join(HERE, script)],
                      cwd=HERE).returncode:
        sys.exit(f"FAILED: {script}")


if __name__ == "__main__":
    run("el_calc.py")
    run("el_schedules.py")
    run("el_sheets.py")
    print("\n=== validation " + "=" * 51)
    sys.path.insert(0, os.path.join(ROOT, "Drainage", "Scripts"))
    import mep_validate                                   # noqa: E402
    sys.exit(mep_validate.run([os.path.join(HERE, "..", "DXF")])[0])
