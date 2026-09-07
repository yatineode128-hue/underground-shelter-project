"""
wm_build_all.py — rebuild every Works Management deliverable from source.

Underground CBRN-hardened blast-resistant protective structure + sentry post, Pune.
Works Management package revision WM1.

Edit wm_data.py (programme and resources) or wm_content.py (methodology, ITP,
safety, risk, procurement, codes) and run this script.  Everything downstream
moves together: the WBS, the BOQ, the plans, the registers, the Microsoft
Project file, the programme drawing and the handout are all generated, so they
cannot drift apart.

Order matters: quantities feed the BOQ, the schedule feeds the programme
files, and the audit runs last against the finished deliverables.

    python3 wm_build_all.py
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))

STEPS = [
    ("Quantity derivation", "wm_quantities.py",
     os.path.join(ROOT, "Schedules", "BOQ_QUANTITY_DERIVATION.txt")),
    ("Critical-path calculation", "wm_schedule.py",
     os.path.join(ROOT, "Schedules", "WM_CPM_OUTPUT.txt")),
    ("Microsoft Project file and task list", "wm_mspdi.py", None),
    ("Programme drawing", "wm_programme_pdf.py", None),
    ("Documents, schedules and registers", "wm_docs.py", None),
    ("Works Management handout", "wm_handout_pdf.py", None),
    ("Final consistency audit", "wm_audit.py",
     os.path.join(ROOT, "QAQC", "WM_CONSISTENCY_AUDIT.txt")),
]


def main():
    for d in ("Schedules", "QAQC", "Documentation", "Programme"):
        os.makedirs(os.path.join(ROOT, d), exist_ok=True)
    failed = 0
    for name, script, redirect in STEPS:
        sys.stdout.write("%-42s" % name)
        sys.stdout.flush()
        r = subprocess.run([sys.executable, script], cwd=HERE,
                           capture_output=True, text=True)
        if redirect:
            with open(redirect, "w", encoding="utf-8") as f:
                f.write(r.stdout)
            tail = os.path.relpath(redirect, ROOT)
        else:
            tail = (r.stdout.strip().split("\n") or [""])[-1]
        if r.returncode != 0:
            failed += 1
            print("FAILED")
            print(r.stdout[-2000:])
            print(r.stderr[-2000:])
        else:
            print("ok   %s" % tail)
    print()
    print("BUILD COMPLETE" if not failed else "BUILD FINISHED WITH %d FAILURE(S)"
          % failed)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
