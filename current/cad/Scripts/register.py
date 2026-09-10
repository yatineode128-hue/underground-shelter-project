# Drawing register for the ten Rev F architectural drawings.
# Filenames are NOT changed - the master (Part E.2) and every project document
# cite them, and the brief requires the existing DXF to stay at its own name and
# location.  The drawing NUMBER lives in the title block and in the index, which
# carries the filename alongside it.
REG = [
 # file, number, title, subtitle, scale, scale_note, sheet_of, sheet
 ("1_Underground_Level_Plan.dxf", "A-101", "UNDERGROUND LEVEL PLAN",
  "FLOOR (-)6.100 - BAYS 1 TO 8, ESCAPE SHAFTS, STAIR SHAFT", 50,
  "1:50 AT A1", "1 OF 10", "A1"),
 ("2_Ground_Plan_Headhouse_Berm.dxf", "A-102", "GROUND LEVEL PLAN - HEADHOUSE AND BERM",
  "GRADE 0.000 - HEADHOUSE, COVERED STAIRWELL, ENGINEERED COVER", 50,
  "1:50 AT A1", "2 OF 10", "A1"),
 ("3_Sentry_Post_Ground_Floor_Plan.dxf", "A-103", "SENTRY POST - GROUND FLOOR PLAN",
  "SEPARATE STRUCTURE - NOT BLAST DESIGNED", 50, "1:50 AT A1", "3 OF 10", "A1"),
 ("4_Sentry_Post_First_Floor_Plan.dxf", "A-104", "SENTRY POST - FIRST FLOOR PLAN",
  "ARMOURED VISION PANELS - NOT BLAST DESIGNED", 50, "1:50 AT A1", "4 OF 10", "A1"),
 ("6_Sentry_Post_Framing_Plan.dxf", "A-105", "SENTRY POST - FRAMING PLAN",
  "SLAB S1, BEAMS B1/B2, COLUMNS C1 - REV F INPUT GEOMETRY", 50,
  "1:50 AT A1", "5 OF 10", "A1"),
 ("1_Staircase_Section.dxf", "A-201", "SECTION A-A - MAIN STAIRCASE",
  "BAY 7 - 24R AT 170.8333 / 280, THREE FLIGHTS.  GEOMETRY FROZEN", 50,
  "1:50 AT A1", "6 OF 10", "A1"),
 ("2_Side_Section_with_Stairs.dxf", "A-202", "SECTION X-X - SIDE SECTION WITH STAIRS",
  "LONGITUDINAL THROUGH THE BOX, ENTRY AND ENGINEERED COVER", 50,
  "1:50 AT A1", "7 OF 10", "A1"),
 ("3_Headhouse_Section_Cutaway.dxf", "A-203", "SECTION B-B - HEADHOUSE CUTAWAY",
  "CUT AT Z = 2800 - HEADHOUSE WALLS, ROOF AND ENTRY", 50,
  "1:50 AT A1", "8 OF 10", "A1"),
 ("5_Entry_Headhouse_Stair_Section.dxf", "A-204", "SECTION C-C - COVERED ENTRY STAIRWELL",
  "TRUE SECTION ON Z = 6750 - 12R AT 166.667 / 300, ROOF 250", 50,
  "1:50 AT A1", "9 OF 10", "A1"),
 # A-301: the drawing is 880 mm wide at 1:50, so it CANNOT be plotted on A1.
 # The stated scale is kept (it governs measurement); the sheet size is
 # corrected to A0, which is the demonstrably wrong half of "1:50 AT A1".
 ("5_Front_Elevation.dxf", "A-301", "FRONT ELEVATION",
  "SHELTER, HEADHOUSE, BERM AND SENTRY POST - 44 m OVERALL", 50,
  "1:50 AT A0", "10 OF 10", "A0"),
]
SIZES = {"A1": (841.0, 594.0), "A0": (1189.0, 841.0)}
