"""
build_all.py  --  regenerate the ENTIRE Structural CAD package from source.

    python3 "Structural CAD/Scripts/build_all.py"

Runs, in order:
    verify_partB.py      recompute every master Part B value used here
    make_schedules.py    write every bar bending schedule from rebar_data.py
    g00 .. g08           write all 30 R-series DXF sheets
    qa_crosscheck.py     mark / schedule / drawing cross-check
    validate_dxf.py      structural validation of every DXF

Nothing in the package is hand-edited.  Change a dimension in sc_proj.py or a
bar in rebar_data.py and re-run this script: the calculations, the schedules,
the bar-mark annotation and the drawings all move together.

REQUIREMENT: ezdxf (pip install ezdxf).  matplotlib is needed only for the
optional visual QA renderer render_qa.py.
"""
import os, sys, subprocess, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

STEPS = [
    ("verify_partB.py", "recompute master Part B"),
    ("make_schedules.py", "write bar bending schedules"),
    ("g00_general.py", "R-001 .. R-004  general"),
    ("g01_foundations.py", "R-101 .. R-103  foundations"),
    ("g02_walls.py", "R-201 .. R-205  walls"),
    ("g03_roof.py", "R-301 .. R-304  roof slab"),
    ("g04_beams.py", "R-401 .. R-402  beam-type elements"),
    ("g06_stairs.py", "R-601 .. R-604  stairs"),
    ("g07_headhouse.py", "R-701 .. R-703  headhouse and entrance"),
    ("g08_typical.py", "R-801 .. R-805  typical details"),
    ("qa_crosscheck.py", "mark / schedule / drawing cross-check"),
    ("validate_dxf.py", "DXF validation"),
]


def main():
    t0 = time.time()
    fails = []
    for script, desc in STEPS:
        print(f"\n=== {script:<22} {desc}")
        r = subprocess.run([sys.executable, os.path.join(HERE, script)],
                           cwd=HERE, capture_output=True, text=True)
        tail = [l for l in r.stdout.strip().splitlines() if l.strip()][-4:]
        for l in tail:
            print("   ", l)
        if r.returncode != 0:
            fails.append(script)
            print("    *** NON-ZERO EXIT ***")
            if r.stderr.strip():
                print("   ", r.stderr.strip().splitlines()[-3:])
    print("\n" + "=" * 70)
    print(f"BUILD COMPLETE in {time.time()-t0:.1f} s")
    if fails:
        print("STEPS REPORTING A PROBLEM:", fails)
    else:
        print("ALL STEPS CLEAN")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
