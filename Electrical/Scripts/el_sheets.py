"""el_sheets.py  --  E-001, the single line diagram.  One sheet, on purpose."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import el_dxf as X                                          # noqa: E402
import el_proj as P                                         # noqa: E402
import el_calc as K                                         # noqa: E402

OUT = os.path.abspath(os.path.join(HERE, "..", "DXF"))
NOTE, LEAD = 2.4, 4.3
CA = 14.0
TOP = 552.0


def box(sh, x, y, w, h, label, sub="", layer="E-BOARD", hb=2.8):
    sh.rect(x, y, x + w, y + h, layer)
    sh.text(label, (x + w / 2.0, y + h - hb - 2.0), hb, layer, "CENTER")
    if sub:
        sh.text(sub, (x + w / 2.0, y + 2.4), 1.9, "M-TEXT", "CENTER")


def e001():
    tot = K.connected_kw()
    kva = tot / P.PF_SYSTEM
    ess = K.essential_kw()
    ah_a, kwh_a = K.battery_ah(P.CASE_A_H)
    ah_b, kwh_b = K.battery_ah(P.CASE_B_H)

    sh = X.Sheet("E-001", "SINGLE LINE DIAGRAM - SOURCES, BOARDS AND "
                 "ESSENTIAL SERVICES",
                 "BASIC ELECTRICAL DESIGN - THREE BOARDS, ONE CABLE ENTRY, "
                 "ONE BATTERY",
                 flags=("EL-V3", "EL-V4", "EM-V3"), sheet_of="1 OF 1")

    # ---------------- sources row
    box(sh, 40, 470, 92, 34, "MAINS", "METER PANEL  [C] OWNER'S PROGRAMME 123",
        "E-SOURCE")
    sh.text("CAPACITY [N]  EL-V4", (86, 462), 1.9, "M-FLAG", "CENTER")
    box(sh, 168, 470, 92, 34, "GEN-1", f"{P.GEN_KVA:.0f} kVA  BAY 8  [C] A.3",
        "E-SOURCE")
    sh.text(f"LOADED {kva/P.GEN_KVA*100:.0f} %  -  AMPLY SIZED  [D]", (214, 462),
            1.9, "M-TEXT", "CENTER")

    # changeover
    sh.line((86, 470), (86, 440), "E-CABLE")
    sh.line((214, 470), (214, 440), "E-CABLE")
    box(sh, 104, 420, 92, 20, "CHANGEOVER", "", "E-PROT", 2.4)
    sh.line((86, 440), (104, 440), "E-CABLE")
    sh.line((196, 440), (214, 440), "E-CABLE")

    # ---------------- DB-M
    sh.line((150, 420), (150, 396), "E-CABLE")
    box(sh, 60, 362, 180, 34, "DB-M   MAIN LV BOARD",
        "BAY 8 - GREY ZONE - OUTSIDE THE GAS-TIGHT ENVELOPE", "E-BOARD")
    for x, lab in ((80, "P-01"), (118, "U-02"), (156, "G-01"), (206, "B-01")):
        sh.line((x, 362), (x, 346), "E-CABLE")
        sh.text(lab, (x, 341), 1.9, "E-LOAD", "CENTER")

    # battery + inverter
    sh.line((206, 341), (206, 322), "E-DC")
    box(sh, 152, 288, 108, 34, "BATTERY + INVERTER",
        f"{P.V_DC:.0f} V DC   {ah_a:.0f} Ah   CASE A  [A]", "E-SOURCE")
    sh.text("*** EL-V1 - IF CASE B IS RIGHT THIS IS", (206, 281), 1.9,
            "E-FLAGE", "CENTER")
    sh.text(f"{ah_b/ah_a:.0f}x TOO SMALL:  {ah_b:.0f} Ah, {kwh_b*1000/P.WH_PER_KG/1000:.1f} t ***",
            (206, 275), 1.9, "E-FLAGE", "CENTER")

    # ---------------- DB-E
    sh.line((100, 362), (100, 250), "E-CABLE")
    sh.line((152, 305), (100, 305), "E-DC")
    sh.text("ESSENTIAL FEED ON LOSS OF BOTH SOURCES", (104, 308), 1.9, "E-DC")
    box(sh, 40, 216, 180, 34, "DB-E   ESSENTIAL BOARD",
        "BAY 5 - INSIDE THE GAS-TIGHT ENVELOPE", "E-BOARD")
    for x, lab in ((58, "L-01"), (92, "L-02"), (126, "F-01"),
                   (160, "D-01"), (198, "U-01")):
        sh.line((x, 216), (x, 200), "E-CABLE")
        sh.text(lab, (x, 195), 1.9, "E-LOAD", "CENTER")
    sh.line((176, 216), (176, 206), "E-CABLE")
    sh.text("S-01", (176, 189), 1.9, "E-LOAD", "CENTER")

    # ---------------- DB-Z2 through the PCI
    sh.line((220, 233), (286, 233), "E-CABLE")
    box(sh, 286, 219, 46, 28, "PCI", "5.7.2.1", "E-PROT", 2.4)
    sh.text("EM1 PoE-3", (309, 212), 1.9, "M-TEXT", "CENTER")
    sh.line((332, 233), (372, 233), "E-CABLE")
    box(sh, 372, 200, 130, 66, "DB-Z2", "EMP ZONE 2 SUB-BOARD, BAY 3",
        "E-BOARD")
    sh.text("Z-01   OPS / COMMS", (437, 228), 2.0, "E-LOAD", "CENTER")
    sh.text(f"{[r[3] for r in K.rows() if r[0]=='Z-01'][0]:.2f} kW ALLOWANCE  [A]",
            (437, 221), 1.9, "M-FLAG", "CENTER")
    sh.text("NOT A SCHEDULE - EL-V3 / EM-V2", (437, 214), 1.9, "M-FLAG",
            "CENTER")
    sh.rect(364, 192, 510, 274, "E-PROT")
    sh.text("EMP ZONE 2 SHIELDED ENCLOSURE  -  80 dB  [A] EM1", (437, 277),
            2.0, "E-PROT", "CENTER")
    sh.text("SIGNAL CROSSES AS FIBRE ONLY - 5.7.4.1, EM1 PoE-4", (437, 185),
            1.9, "M-TEXT", "CENTER")

    # ---------------- cable entry note
    sh.rect(40, 150, 332, 176, "E-CABLE")
    sh.text("ONE CABLE ENTRY.  Every conductor crossing the protective "
            "envelope uses the SERVICE ENTRY", (46, 168), 2.0, "M-TEXT")
    sh.text("PLATE - the project's single services penetration [C].  PCI on "
            "power, FIBRE on signal.", (46, 162), 2.0, "M-TEXT")
    sh.text("THIS PACKAGE CREATES NO NEW PENETRATION.  Its level and size "
            "remain [N].", (46, 155), 2.0, "M-FLAG")

    sh.view_title((40.0, 530.0), "V1",
                  "SINGLE LINE DIAGRAM", "NOT TO SCALE")

    # ---------------- right-hand column
    sh.panel_column(540.0, TOP, 122.0, 290.0, [
        ("THE LOAD, AND THE GENERATOR CHECK", [
            f"Connected load            {tot:7.3f} kW",
            f"at power factor {P.PF_SYSTEM}       {kva:7.3f} kVA",
            f"GEN-1  [C] master A.3    {P.GEN_KVA:7.3f} kVA",
            f"UTILISATION               {kva/P.GEN_KVA*100:6.1f} %",
            f"SPARE                     {P.GEN_KVA-kva:7.3f} kVA",
            "",
            "THE CONFIRMED 15 kVA IS ABOUT TWICE THE CONNECTED",
            "DEMAND, and 49 % sits in the healthy loading band for",
            "a diesel set.  THE PROJECT'S OWN FIGURE NEEDS NO",
            f"CHANGE.  Largest motor is the filter fan at {K.fan_kw():.3f} kW;",
            f"even a DOL start is about {K.fan_kw()*6/P.PF_SYSTEM:.1f} kVA.  NO STARTING",
            "PROBLEM.  [D]",
        ]),
        ("EL-V1  -  RULED.  THE GENERATOR MAY RUN IN MODE 3", [
            "*** RULED YES - RC2, 11 Sep 2026, master H.21. ***",
            "All five valves shut at the shock and hold 1.3 s;",
            "BV-4 AND BV-5 ARE THEN REOPENED FOR GEN-1.  Bay 8 is",
            "outside the gas-tight envelope, so the clean zone is",
            "unaffected.  HV1's mode 3 row is amended to match.",
            "CASE A CONFIRMED - no number changes, only the class.",
            "",
            "The question, kept because the size of the",
            "consequence is why it needed a ruling:",
            "   MODE 3  'ALL FIVE BLAST VALVES SHUT.  48 h limit'",
            "   MODE 5  'BV-4 AND BV-5 OPEN ... bay 8 only - does",
            "            NOT touch the gas-tight envelope', and",
            "           'Mode 5 is INDEPENDENT of modes 1-4'",
            "BV-4/BV-5 are two of the five.  BOTH COULD NOT HOLD",
            "DURING MODE 3, and the project held no position.",
            "",
            f"   CASE A   {P.CASE_A_H:.0f} h   {ah_a:6.0f} Ah   {kwh_a*1000/P.WH_PER_KG:5.0f} kg   a CABINET   <- RULED",
            f"   Case B  {P.CASE_B_H:.0f} h   {ah_b:6.0f} Ah   {kwh_b*1000/P.WH_PER_KG:5.0f} kg   a ROOM      historical",
            "",
            f"{ah_b/ah_a:.0f}x APART.  Case B needed {kwh_b*1000/P.WH_PER_KG*9.81/1000/P.FLOOR_LL_KPA:.1f} m2 of floor just to stay",
            f"inside the {P.FLOOR_LL_KPA:.0f} kPa floor live load  [C] A.7.2 - AND BAY 5",
            "IS ALREADY 80 % OCCUPIED (CO-3).  That is why it was",
            "put to the owner rather than assumed.  [D]",
            "",
            "CONSEQUENCE, RECORDED NOT RESOLVED:  reopening BV-4",
            "and BV-5 leaves two DN350 bores open post-attack -",
            "the two EM1 showed FAIL BOTH EMP CRITERIA.  SHARPENS",
            "EM-V3 without deciding it.",
        ]),
        ("WHAT THIS PACKAGE UNBLOCKS", [
            "FS-V2  'No fire detection, alarm, emergency lighting or",
            "       suppression exists anywhere.  FOLLOWS THE MISSING",
            "       ELECTRICAL DESIGN.'  ->  S-01 and L-02 now exist on",
            "       the essential board, on the battery.  THE ELECTRICAL",
            "       BLOCKER IS GONE.  The head layout and zoning remain",
            "       fire engineering.  ADVANCED, NOT CLOSED.",
            "EM-V2  EMP Zone 2 dimensions awaited an equipment schedule.",
            "       Z-01 gives a 1.50 kW ALLOWANCE and a sub-board, so the",
            "       enclosure now has a BASIS instead of nothing.  It is",
            "       still an allowance.  ADVANCED, NOT CLOSED.",
            "FS-V4  Generator fuel unspecified  ->  this package puts the",
            f"       first number on it: about {int(round(K.connected_kw()*P.MISSION_H*P.SFC_L_PER_KWH/10.0)*10)} L for a 96 h run  [A].",
            "       A bounded estimate, not a specification.",
            "HVAC P11  'distribution, UPS and battery autonomy are an",
            "       ELECTRICAL scope item, not designed here'  ->  DESIGNED.",
            "13 GAPS  'no electrical design package exists' was the",
            "       LARGEST.  A BASIC one now does.  The detailed design",
            "       still does not - EL-V5.",
        ]),
        ("WHAT NEEDS NO ELECTRICITY AT ALL  -  AND IS CONFIRMED", [
            "HAND CRANK on both filter fans   [C] HVAC schedule",
            "HAND PUMP PU-03                  [C] S-06",
            "",
            "These are the real last line, the project already has",
            "them, and NO ELECTRICAL DESIGN SHOULD OBSCURE THEM. [D]",
            "",
            "Groundwater does not stop because the shelter is",
            "sealed - the clean sump pump stays on the essential",
            f"board through mode 3.  Essential total {ess:.3f} kW.",
        ]),
    ], gap=8.0)

    X.evidence_key(sh, CA, 140.0, 290.0)
    sh.panel(320.0, 140.0, 200.0, "WHAT THIS SHEET DOES NOT SHOW", [
        "NO circuit schedule, NO cable sizing, NO luminaire or",
        "socket layout, NO protection or discrimination study.",
        "It stops at BOARD LEVEL on purpose - EL-V5.  A fault",
        "level cannot be computed until the incoming supply",
        "capacity exists, and that is [N] - EL-V4.",
        "",
        "NO BOQ QUANTITY, RATE, DATE OR FLOAT IS CHANGED.",
        "The owner's Works Management package governs.",
    ], h=NOTE, lead=LEAD)

    sh.finish(scale="NOT TO SCALE", sheet_of="1 OF 1")
    return sh


def build():
    os.makedirs(OUT, exist_ok=True)
    sh = e001()
    sh.save(os.path.join(OUT, "E-001_Single_Line_Diagram.dxf"))
    print("  E-001_Single_Line_Diagram.dxf")


if __name__ == "__main__":
    print("EL1 drawing:")
    build()
