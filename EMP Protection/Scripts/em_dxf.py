"""
em_dxf.py  --  A1 sheet library for the EMP PROTECTION package.

It re-uses the shared MEP sheet library (Drainage/Scripts/mep_dxf.py), which
itself subclasses the structural sheet library (Structural CAD/Scripts/
sc_dxflib.py).  So an EMP sheet carries the SAME border, title block, text
heights, dimension styles and drawing conventions as the issued R-series
reinforcement drawings and the D / M / A-6xx services drawings.

NOTHING IN THE SHARED LIBRARIES IS MODIFIED.  Drainage, HVAC and Schedule of
Finishes regenerate byte-identically after this package exists.  Only the
package name, the revision, the date and an added EMP layer group are re-cut,
by subclassing.

    A1, 841 x 594 mm, drawn in PAPER MILLIMETRES, plot 1:1
    AutoCAD 2010 (AC1024) ASCII DXF, $INSUNITS = 4 (millimetres)
"""
import os
import sys
import math

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "Drainage", "Scripts"))
sys.path.insert(0, _HERE)

import mep_dxf as M                                        # noqa: E402
import mep_proj as MP                                      # noqa: E402
import mep_views as MV                                     # noqa: E402
import em_proj as P                                        # noqa: E402

vw = M.vw
TXT = M.TXT
IN_L, IN_B, IN_R, IN_T = M.IN_L, M.IN_B, M.IN_R, M.IN_T
TB_X, TB_Y, TB_W, TB_H = M.TB_X, M.TB_Y, M.TB_W, M.TB_H

# EMP-specific layers, added on top of the shared MEP set
EM_LAYERS = {
    "E-ZONE0":    (8,  18, "EMP Zone 0 - unprotected, above grade"),
    "E-ZONE1":    (4,  30, "EMP Zone 1 - the reinforcement cage"),
    "E-ZONE2":    (3,  50, "EMP Zone 2 - the 80 dB shielded enclosure"),
    "E-SHIELD":   (2,  35, "Shielded surfaces, plates, honeycomb, liners"),
    "E-BOND":     (6,  30, "Bonding straps, earth, cage continuity"),
    "E-PENET":    (5,  30, "Envelope penetrations - treated"),
    "E-APERTURE": (1,  35, "Apertures that FAIL - findings"),
    "E-CHART":    (7,  18, "Chart axes, curves and gridlines"),
    "E-CHART-HI": (1,  35, "Chart requirement line and fail region"),
}


class Sheet(M.Sheet):
    """One A1 EMP Protection sheet.

    FS2 / CAM2 (10.09.26) turned the scope note, the title-block scope line and
    the issue date into class attributes on the shared Sheet, precisely so a new
    package need not restate the whole title block to change them.  EM1 uses
    those hooks.  It previously carried its own copy of `titleblock()`, which
    worked but froze the EMP sheets at one revision of the house standard; that
    copy is gone and the house method is inherited again.
    """

    SCOPE_NOTE = "SENTRY POST EXCLUDED FROM THIS PACKAGE"
    TB_SCOPE = f"EMP PROTECTION {P.REV}  -  SENTRY POST NOT IN THIS PACKAGE"
    DATE = P.PACKAGE_DATE

    def __init__(self, number, title, subtitle="", flags=(), sheet_of=""):
        super().__init__(number, title, subtitle=subtitle,
                         package=P.PACKAGE, rev=P.REV, status=P.STATUS,
                         flags=flags, sheet_of=sheet_of)
        for name, (col, lw, desc) in EM_LAYERS.items():
            ly = self.doc.layers.add(name)
            ly.color = col
            ly.lineweight = lw
            ly.description = desc

    # ------------------------------------------------------------ header
    def sheet_header(self, extra=None):
        self.text(f"{P.PACKAGE} PACKAGE", (IN_L + 2, IN_T - 7.5),
                  TXT["sheet_title"], "M-TITLE")
        self.text(f"{self.number}   {self.title}", (IN_L + 2, IN_T - 14.5),
                  TXT["detail_label"], "M-TITLE")
        self.line((IN_L, IN_T - 17.5), (IN_R, IN_T - 17.5), "M-TITLE")
        self.text(self.SCOPE_NOTE,
                  (IN_R - 2, IN_T - 7.0), TXT["note"], "M-FLAG", "RIGHT")
        self.text("NO DESIGN VALUE IS CHANGED BY THIS PACKAGE - "
                  "PENDING ENGINEERING VERIFICATION",
                  (IN_R - 2, IN_T - 13.5), TXT["small"], "M-FLAG", "RIGHT")
        if self.flags:
            self.text("OPEN ITEMS ON THIS SHEET:  " + "   ".join(self.flags),
                      (IN_L + 2, IN_T - 22.5), TXT["small"], "M-FLAG")
        if extra:
            self.text(extra, (IN_L + 2, IN_T - 27.0), TXT["small"], "M-TEXT")



def evidence_key(sh, x, y, w=168):
    return sh.panel(x, y, w, "EVIDENCE CLASS - APPLIED TO EVERY VALUE ON THIS "
                    "SHEET", [
        "[C] CONFIRMED      traceable to the master, a Rev F drawing or S-06",
        "[R] RECONSTRUCTED  computed here from confirmed values; arithmetic shown",
        "[D] DERIVED        an engineering result computed by this package",
        "[A] ASSUMED        an engineering selection - confirm before construction",
        "[U] UNRESOLVED     the project holds no single position",
        "[N] NOT AVAILABLE  no source exists anywhere in the project - DATA REQUIRED",
    ], h=2.0, lead=3.4)


def zone_key(sh, x, y, w=168):
    return sh.panel(x, y, w, "EMP ZONE KEY   -   'EMP ZONE' IS NOT 'ZONE'", [
        "EMP ZONE 0   above grade.  NO ATTENUATION CREDITED.",
        "EMP ZONE 1   the buried box, all 8 bays.  The rebar cage at 150.",
        "             100 dB at 10 kHz falling 20 dB/decade to 0 dB at 999 MHz.",
        "             NOT A MIL-STD-188-125-1 SHIELD.  NOT TO BE CREDITED AS ONE.",
        "EMP ZONE 2   welded steel enclosure, bay 3.  80 dB, 10 kHz - 1 GHz,",
        "             STANDING ALONE.  THE ONLY EMP SHIELD IN THIS PROJECT.",
        "",
        "*** DRAINAGE AND FINISHES ALREADY USE 'ZONE 1/2/3' FOR CLEANLINESS.",
        "    THE PREFIX 'EMP' IS MANDATORY EVERYWHERE IN THIS PROJECT. ***",
    ], h=2.0, lead=3.4)
