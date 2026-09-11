"""sg_dxf.py  --  A1 sheet library for the SITE SELECTION AND GEOTECHNICAL
package.

Subclasses the shared MEP sheet library exactly as the EMP and ELECTRICAL
packages do, and uses the three class attributes FS2 / CAM2 added
(SCOPE_NOTE, TB_SCOPE, DATE) rather than restating the title block.
NOTHING IN ANY SHARED LIBRARY IS MODIFIED, so DRAINAGE, HVAC, SCHEDULE OF
FINISHES, FIRE AND LIFE SAFETY, SITE AND CONCEALMENT, EMP PROTECTION and
ELECTRICAL all regenerate byte for byte unchanged.

One departure from the other packages, and it is deliberate: the scope note
says the sentry post IS included.  Footing F1 bears on in-situ basalt at
(-)2.000 and that is a geotechnical statement, so it appears on SG-201.  No
sentry post STRUCTURAL value is touched by this package.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "Drainage", "Scripts"))
sys.path.insert(0, _HERE)

import mep_dxf as M                                        # noqa: E402
import sg_proj as P                                        # noqa: E402

vw, TXT = M.vw, M.TXT
IN_L, IN_B, IN_R, IN_T = M.IN_L, M.IN_B, M.IN_R, M.IN_T

SG_LAYERS = {
    "G-TOPSOIL":  (30, 25, "Black cotton soil - CH, very high swell"),
    "G-MURRUM":   (42, 25, "Murrum - GM / GP / SC"),
    "G-BROKEN":   (33, 25, "Disintegrated broken basalt"),
    "G-ROCK":     (8,  30, "Sound basalt"),
    "G-NODATA":   (1,  35, "BELOW THE INVESTIGATION - NO DATA EXISTS"),
    "G-WATER":    (4,  35, "Design groundwater table - ASSUMED"),
    "G-STRUCT":   (7,  50, "Structure, for comparison only"),
    "G-LOG":      (7,  35, "Trial pit log outline"),
    "G-SETTING":  (5,  35, "Site setting diagram - NOT a site plan"),
    "G-FLAGG":    (1,  35, "Open items and findings"),
}

# stratum key: (name, layer, hatch pattern, scale, angle)
STRATA = {
    "CH":     ("BLACK COTTON - CH", "G-TOPSOIL", "ANSI37", 1.1, 0.0),
    "MURRUM": ("MURRUM - GM/GP/SC", "G-MURRUM", "EARTH", 0.8, 0.0),
    "BROKEN": ("BROKEN BASALT", "G-BROKEN", "GRAVEL", 0.5, 0.0),
    "ROCK":   ("SOUND BASALT", "G-ROCK", "ANSI31", 1.4, 0.0),
    "NODATA": ("NO DATA", "G-NODATA", "ANSI31", 5.0, 90.0),
}


def classify(kind):
    """Map a report stratum description to a STRATA key."""
    k = kind.upper()
    if "CLAY" in k or "CH" in k:
        return "CH"
    if "MURRUM" in k:
        return "MURRUM"
    if "BROKEN" in k:
        return "BROKEN"
    return "ROCK"


class Sheet(M.Sheet):
    """One A1 Site Selection and Geotechnical sheet."""

    SCOPE_NOTE = "SENTRY POST INCLUDED - GROUND ONLY, NO STRUCTURAL VALUE"
    TB_SCOPE = f"SITE AND GEOTECHNICAL {P.REV}  -  GROUND ONLY"
    DATE = P.PACKAGE_DATE

    def __init__(self, number, title, subtitle="", flags=(), sheet_of=""):
        super().__init__(number, title, subtitle=subtitle, package=P.PACKAGE,
                         rev=P.REV, status=P.STATUS, flags=list(flags),
                         sheet_of=sheet_of)
        for name, (col, lw, desc) in SG_LAYERS.items():
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
        self.text("THIS PACKAGE RESOLVES NOTHING - IT RECORDS PROVENANCE AND "
                  "QUANTIFIES MARGIN", (IN_R - 2, IN_T - 13.5), TXT["small"],
                  "M-FLAG", "RIGHT")
        if self.flags:
            self.text("OPEN ITEMS ON THIS SHEET:  " + "   ".join(self.flags),
                      (IN_L + 2, IN_T - 22.5), TXT["small"], "M-FLAG")
        if extra:
            self.text(extra, (IN_L + 2, IN_T - 27.0), TXT["small"], "M-TEXT")

    # ------------------------------------------------------------ helpers
    def stratum(self, x0, x1, y0, y1, key, label=None, h=1.8):
        """One hatched stratum band between two paper levels."""
        name, layer, pat, sc, ang = STRATA[key]
        pts = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        self.hatch_pat(pts, pat, sc, ang, layer)
        self.pline(pts, layer, close=True)
        if label:
            self.text(label, (x1 + 2.0, (y0 + y1) / 2.0 - h / 2.0), h,
                      layer)
        return (y0 + y1) / 2.0

    def lvl(self, x, y, txt, layer="M-LEVEL", h=1.8, align="LEFT"):
        """A level tick and its label, drawn at a paper point."""
        self.line((x - 3.0, y), (x + 3.0, y), layer)
        self.pline([(x, y), (x - 1.6, y + 2.4), (x + 1.6, y + 2.4)],
                   layer, close=True)
        self.text(txt, (x + 4.5 if align == "LEFT" else x - 4.5, y + 0.8),
                  h, layer, "LEFT" if align == "LEFT" else "RIGHT")


def evidence_key(sh, x, y, w=230.0):
    return sh.panel(x, y, w,
                    "EVIDENCE CLASS - APPLIED TO EVERY VALUE ON THIS SHEET",
                    [f"{t} {n:<14} {d}" for t, n, d in P.EVIDENCE],
                    h=2.0, lead=3.4)
