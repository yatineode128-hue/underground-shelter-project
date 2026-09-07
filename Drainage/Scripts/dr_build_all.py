"""
dr_build_all.py  --  rebuild the whole DRAINAGE package from source.

    python3 dr_build_all.py

Runs, in order:
    dr_calc.py        the calculations          -> ../Calculations/
    dr_schedules.py   every schedule            -> ../Schedules/
    d00_general.py    D-001, D-002              -> ../DXF/
    d01_plans.py      D-101 to D-203            -> ../DXF/
    d02_details.py    D-204 to D-305            -> ../DXF/
    dr_handout.py     the two-page handout      -> ../Handout/
    mep_validate.py   validation of every DXF
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
STEPS = ["dr_calc.py", "dr_schedules.py", "d00_general.py", "d01_plans.py",
         "d02_details.py", "dr_handout.py"]

if __name__ == "__main__":
    for s in STEPS:
        print(f"\n=== {s} " + "=" * (60 - len(s)))
        r = subprocess.run([sys.executable, os.path.join(HERE, s)],
                           cwd=HERE, capture_output=True, text=True)
        tail = [ln for ln in r.stdout.strip().split("\n") if ln][-6:]
        print("\n".join(tail))
        if r.returncode:
            print(r.stderr[-2000:])
            sys.exit(1)
    print("\n=== validation " + "=" * 52)
    for d in ("DXF", "Handout"):
        subprocess.run([sys.executable, os.path.join(HERE, "mep_validate.py"),
                        os.path.abspath(os.path.join(HERE, "..", d))], cwd=HERE)
