"""
fn_build_all.py  --  rebuild the whole Schedule of Finishes package.
    python3 fn_build_all.py
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DR = os.path.abspath(os.path.join(HERE, "..", "..", "Drainage", "Scripts"))

if __name__ == "__main__":
    for s in ("fn_schedules.py", "fn_sheets.py"):
        print(f"\n=== {s} " + "=" * (60 - len(s)))
        r = subprocess.run([sys.executable, os.path.join(HERE, s)], cwd=HERE,
                           capture_output=True, text=True)
        print("\n".join([l for l in r.stdout.strip().split("\n") if l][-8:]))
        if r.returncode:
            print(r.stderr[-2000:])
            sys.exit(1)
    print("\n=== validation " + "=" * 52)
    subprocess.run([sys.executable, os.path.join(DR, "mep_validate.py"),
                    os.path.abspath(os.path.join(HERE, "..", "DXF"))], cwd=HERE)
