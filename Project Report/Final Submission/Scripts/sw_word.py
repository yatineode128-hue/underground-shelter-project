"""
sw_word.py -- builds the editable Word version of the report.

    python3 "Project Report/Final Submission/Scripts/sw_word.py"

Runs sw_export.py into a temporary folder and sw_docx.js (Node, with the
`docx` package installed globally: npm install -g docx) on the result, and
writes CBRN_Hardened_Underground_Ops_Room_Project_Report.docx next to the PDF.
"""

import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.abspath(os.path.join(HERE, ".."))
OUT = os.path.join(PKG, "CBRN_Hardened_Underground_Ops_Room_Project_Report.docx")


def main():
    tmp = tempfile.mkdtemp(prefix="sw_word_")
    try:
        subprocess.check_call([sys.executable,
                               os.path.join(HERE, "sw_export.py"), tmp])
        root = subprocess.check_output(["npm", "root", "-g"],
                                       text=True).strip()
        env = dict(os.environ, NODE_PATH=os.pathsep.join(
            [root, os.path.join(root, "docx", "node_modules")]))
        subprocess.check_call(["node", os.path.join(HERE, "sw_docx.js"),
                               os.path.join(tmp, "report.json"), OUT],
                              env=env)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
