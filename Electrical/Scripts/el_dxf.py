"""el_dxf.py  --  A1 sheet library for the ELECTRICAL AND POWER package.

Subclasses the shared MEP sheet library exactly as the EMP package does, and
uses the three class attributes FS2 / CAM2 added (SCOPE_NOTE, TB_SCOPE, DATE)
rather than restating the title block.  Nothing in any shared library is
modified.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "Drainage", "Scripts"))
sys.path.insert(0, _HERE)

import mep_dxf as M                                        # noqa: E402
import el_proj as P                                        # noqa: E402

vw, TXT = M.vw, M.TXT
IN_L, IN_B, IN_R, IN_T = M.IN_L, M.IN_B, M.IN_R, M.IN_T

EL_LAYERS = {
    "E-SOURCE":  (2, 50, "Sources - mains, generator, battery"),
    "E-BOARD":   (3, 50, "Distribution boards"),
    "E-CABLE":   (7, 35, "Sub-mains and final circuits"),
    "E-DC":      (5, 35, "DC and essential distribution"),
    "E-LOAD":    (4, 30, "Loads"),
    "E-PROT":    (6, 30, "Protective devices, changeover, PCI"),
    "E-FLAGE":   (1, 35, "Open items and findings"),
}


class Sheet(M.Sheet):
    """One A1 Electrical sheet."""

    SCOPE_NOTE = "SENTRY POST EXCLUDED FROM THIS PACKAGE"
    TB_SCOPE = f"ELECTRICAL {P.REV}  -  SENTRY POST NOT IN THIS PACKAGE"
    DATE = P.PACKAGE_DATE

    def __init__(self, number, title, subtitle="", flags=(), sheet_of=""):
        super().__init__(number, title, subtitle=subtitle, package=P.PACKAGE,
                         rev=P.REV, status=P.STATUS, flags=flags,
                         sheet_of=sheet_of)
        for name, (col, lw, desc) in EL_LAYERS.items():
            ly = self.doc.layers.add(name)
            ly.color, ly.lineweight, ly.description = col, lw, desc

    def sheet_header(self, extra=None):
        self.text(f"{P.PACKAGE} PACKAGE", (IN_L + 2, IN_T - 7.5),
                  TXT["sheet_title"], "M-TITLE")
        self.text(f"{self.number}   {self.title}", (IN_L + 2, IN_T - 14.5),
                  TXT["detail_label"], "M-TITLE")
        self.line((IN_L, IN_T - 17.5), (IN_R, IN_T - 17.5), "M-TITLE")
        self.text(self.SCOPE_NOTE, (IN_R - 2, IN_T - 7.0), TXT["note"],
                  "M-FLAG", "RIGHT")
        self.text("BASIC DESIGN - STOPS AT BOARD LEVEL - PENDING ENGINEERING "
                  "VERIFICATION", (IN_R - 2, IN_T - 13.5), TXT["small"],
                  "M-FLAG", "RIGHT")
        if self.flags:
            self.text("OPEN ITEMS ON THIS SHEET:  " + "   ".join(self.flags),
                      (IN_L + 2, IN_T - 22.5), TXT["small"], "M-FLAG")
        if extra:
            self.text(extra, (IN_L + 2, IN_T - 27.0), TXT["small"], "M-TEXT")


def evidence_key(sh, x, y, w=222.0):
    return sh.panel(x, y, w, "EVIDENCE CLASS - APPLIED TO EVERY VALUE ON THIS "
                    "SHEET", [
        "[C] CONFIRMED      master, a Rev F drawing, S-06, or the owner's own",
        "                   Works Management documents, which govern",
        "[R] RECONSTRUCTED  computed here from confirmed values",
        "[D] DERIVED        an engineering result computed by this package",
        "[A] ASSUMED        an engineering selection - confirm before construction",
        "[U] UNRESOLVED     the project holds two positions, or none",
        "[N] NOT AVAILABLE  no source exists anywhere in the project",
    ], h=2.0, lead=3.4)
