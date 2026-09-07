"""
hv_build_all.py  --  rebuild the whole HVAC package from source.
    python3 hv_build_all.py
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DR = os.path.abspath(os.path.join(HERE, "..", "..", "Drainage", "Scripts"))
STEPS = ["hv_calc.py", "hv_schedules.py", "hv_sheets.py", "hv_handout.py"]

if __name__ == "__main__":
    for s in STEPS:
        print(f"\n=== {s} " + "=" * (60 - len(s)))
        r = subprocess.run([sys.executable, os.path.join(HERE, s)], cwd=HERE,
                           capture_output=True, text=True)
        print("\n".join([l for l in r.stdout.strip().split("\n") if l][-6:]))
        if r.returncode:
            print(r.stderr[-2000:])
            sys.exit(1)
    print("\n=== validation " + "=" * 52)
    for d in ("DXF", "Handout"):
        subprocess.run([sys.executable, os.path.join(DR, "mep_validate.py"),
                        os.path.abspath(os.path.join(HERE, "..", d))], cwd=HERE)
