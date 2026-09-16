/* ===========================================================================
   AN1 — PROJECT DATA MODULE
   Underground CBRN-hardened blast-resistant protective structure + sentry post
   Pune, Maharashtra.

   EVERY value below is transcribed from an authoritative project source.
   Evidence tags follow the master's own legend:
       C = CONFIRMED   R = RECONSTRUCTED   A = ASSUMED
       U = UNRESOLVED  N = NOT AVAILABLE   D = DERIVED by a named package
       V = VISUAL-ONLY, this animation's own narrative choice, carries no
           engineering weight and is declared as such in the design basis.

   SOURCE OF TRUTH: master/MASTER_PROJECT_STATE.md Parts A, B, F, L.
   Nothing here may be changed without changing the master first.

   COORDINATE SYSTEM — master A.4.1, used verbatim so every number below can
   be checked against the drawings without conversion:
       ORIGIN = south-west EXTERNAL corner of the underground box, at grade
       X = east   (along the length, 0 .. 22000)
       Y = north  (across the width, 0 .. 6200)
       Z = level, metres relative to finished grade 0.000, negative downwards
   Geometry is authored in MILLIMETRES and divided by 1000 at build time,
   exactly as the DXF toolchain does.
   =========================================================================== */

const MM = 0.001;                      // millimetres -> scene metres

const PROJ = {

  identity: {
    title:      'UNDERGROUND CBRN-HARDENED OPERATIONS ROOM',           // C
    subtitle:   'Blast-resistant protective structure with sentry post', // C
    location:   'Pune, Maharashtra',                                    // C
    tagline:    'NINE PEOPLE. NINETY-SIX HOURS. TWO METRES OF EARTH.',  // C - project flier
    objective:  'Protect 9 occupants for 96 h against a nuclear air-blast ' +
                'design basis threat with CBRN, EMP and fallout hardening', // C - master A.1
    archRev:    'Rev F',            // C
    strRev:     'Phase 2 Rev A + M1' // C
  },

  /* ---- A.4.2 MAIN BOX -------------------------------------------------- */
  box: {
    lenExt:     22000,   // C  master A.4.2 (was 21600 pre-M1)
    widExt:      6200,   // C
    lenInt:     20800,   // C
    widInt:      5000,   // C  clear span of the roof - do not widen
    wallPerim:    600,   // C
    roofSlab:     900,   // C  the pressure slab, governing element (B.4)
    mat:          600,   // C
    pcc:          100,   // C  M15 blinding
    clearHt:     3200,   // C
    cover:       2000    // C  engineered cover over roof, layered
  },

  /* ---- A.4.3 LEVEL SCHEDULE (metres) ----------------------------------- */
  lvl: {
    grade:        0.000,   // C  finished site level, crowned, falls 1:50 away
    roofTop:     -2.000,   // C  top of pressure slab = headhouse floor level
    roofSoffit:  -2.900,   // C
    floor:       -6.100,   // C  internal floor / top of mat
    matUnder:    -6.700,   // C
    formation:   -6.800,   // C  underside of PCC
    gwt:         -2.000,   // A  design groundwater table (monsoon) - THE most
                           //    important number the site investigation must confirm
    rockheadHi:  -1.500,   // A  master A.6; SG1 measured 0.9-1.5 m at three locations
    rockheadLo:  -2.000,   // A
    stairL1:     -4.7333,  // C  8 risers up from floor
    stairL2:     -3.3667,  // C  16 risers up from floor
    hhSoffit:     0.400,   // C
    hhRoofTop:    0.900,   // C  no earth cover; berm graded to this level
    entryRoofHd:  2.450,   // C  master A.4.3  (Revit set prints 3400 - see AN1-F2)
    sentryGF:     0.450,   // C  = base of the STAAD model
    sentryFF:     3.650,   // C
    sentryRoof:   6.700,   // C
    sentryPar:    7.000,   // C
    sumpInvert:  -7.600    // C
  },

  /* ---- A.3 BAY SCHEDULE (post-M1) -------------------------------------- */
  /* name strings are the project flier's own bay legend                     */
  bays: [
    { n:1, x0:  600, x1: 3500, w:2900, name:'STORES',      // C
      use:'Emergency stores, 1000 L potable tank, ESC 1' },
    { n:2, x0: 3610, x1: 5410, w:1800, name:'WC / MED',    // C
      use:'Lavatory (1800x2000) + medical (1800x3000)' },
    { n:3, x0: 5520, x1: 9020, w:3500, name:'OPS ROOM',    // C
      use:'Ops room & hazard plotting; EMP Zone 2 enclosure' },
    { n:4, x0: 9130, x1:10930, w:1800, name:'BERTHING',    // C
      use:'3 x 3-tier bunks, 9 berths' },
    { n:5, x0:11040, x1:12600, w:1560, name:'CBRN PLANT',  // C
      use:'2 x 300 m3/h filter trains, CO2/O2, dehumidifier, sump' },
    { n:6, x0:12800, x1:14800, w:2000, name:'DECON',       // C
      use:'Decon airlock, 3 stages (2000x2000, 2000x1500, 2000x1500)' },
    { n:7, x0:15200, x1:18000, w:2800, name:'STAIR',       // C  shifted +200 by M1
      use:'Stair shaft' },
    { n:8, x0:18400, x1:21400, w:3000, name:'GENERATOR',   // C  grey zone
      use:'Generator 15 kVA, ESC 2 at X 19900' }
  ],

  /* ---- A.3 INTERNAL WALLS ---------------------------------------------- */
  walls: [
    { mark:'W8', x0: 3500, x1: 3610, t:110 },  // C  door gap Y 2500-3400
    { mark:'W8', x0: 5410, x1: 5520, t:110 },  // C
    { mark:'W8', x0: 9020, x1: 9130, t:110 },  // C
    { mark:'W8', x0:10930, x1:11040, t:110 },  // C
    { mark:'W5', x0:12600, x1:12800, t:200 },  // C  fire + gas-tight only
    { mark:'W6', x0:14800, x1:15200, t:400 },  // C  MOD M1, was 200. PROTECTIVE BOUNDARY
    { mark:'W7', x0:18000, x1:18400, t:400 }   // C  MOD M1, was 200. PROTECTIVE BOUNDARY
  ],
  doorGap: { y0:2500, y1:3400 },               // C  900 door gap in each W8

  /* ---- A.2 / A.4.9 PROTECTIVE BOUNDARY --------------------------------- */
  blastDoors: [
    { mark:'BLAST DOOR 1', wallX:14800, t:400, y0:600, y1:1800,   // C  W6
      w:1200, h:2100, rating:'7 bar', into:'Bay 6' },
    { mark:'BLAST DOOR 2', wallX:18000, t:400, y0:600, y1:1800,   // C  W7
      w:1200, h:2100, rating:'7 bar', into:'Bay 8' }
  ],

  /* ---- A.4.5 ESCAPE SHAFTS --------------------------------------------- */
  escShafts: [
    { mark:'ESC 1', cx: 2050, cy:2050, dia:1400, collar:250, od:1900 }, // C
    { mark:'ESC 2', cx:19900, cy:2050, dia:1400, collar:250, od:1900 }  // C  +400 by M1
  ],

  /* ---- A.4.4 STAIR SHAFT, VOID AND PAD (post-M1) ------------------------ */
  stair: {
    shaft:   { x0:15200, x1:18000, y0: 600, y1:5600 },   // C  2800 x 5000
    voidS:   { x0:15200, x1:18000, y0: 600, y1:3760 },   // C  2800 x 3160 in the slab
    pad:     { x0:15200, x1:18000, y0:3760, y1:5600 },   // C  cantilever pad 1840
    flightA: { x0:15300, x1:16500 },                     // C  flights 1 and 3, 1200 wide
    well:    { x0:16500, x1:16700 },                     // C  200
    flightB: { x0:16700, x1:17900 },                     // C  flight 2, 1200 wide
    L1:      { z:-4.7333, y0:3760, y1:4960 },            // C
    L2:      { z:-3.3667, y0: 600, y1:1800 },            // C
    arrival: { z:-6.100,  y0: 600, y1:1800 },            // C  = the mat surface
    /* FROZEN - CLAUDE.md. Never change without an explicit new instruction. */
    risers: 24, riser: 170.8333, tread: 280,             // C
    flights: 3, perFlight: 8, totalRise: 4100, headroom: 2533, width: 1200 // C
  },

  /* ---- A.4.6 HEADHOUSE (shifted +200 by M1) ----------------------------- */
  headhouse: {
    ext: { x0:13600, x1:18400, y0: 200, y1:6000 },  // C  4800 x 5800
    int: { x0:14000, x1:18000, y0: 600, y1:5600 },  // C  4000 x 5000
    wall: 400, roof: 500,                            // C
    innerDoor: { x0:14450, x1:15350, w:900, h:2100, wall:'HW2 north' }, // C not blast rated
    bermSlope: 1.5                                   // C  1.5:1 to +0.900
  },

  /* ---- A.4.7 COVERED ENTRY STAIRWELL (Rev F, +200 by M1) ---------------- */
  entry: {
    ext: { x0: 9250, x1:16050, y0:5750, y1:7750 },  // C  6800 x 2000
    int: { x0: 9500, x1:15800, y0:6000, y1:7500 },  // C  6300 x 1500
    wall: 250, roof: 250,                            // C  RC1 ruling C16: stays 250 over the platform
    topLanding: { x0: 9500, x1:11000, z:0.000, t:250 },        // C
    flight:     { x0:11000, x1:14300, risers:12, rise:166.6667, going:300, waist:250 }, // C
    platform:   { x0:14300, x1:15800, z:-2.000, t:250 },       // C  1500 x 1500
    door: { x0:9250, x1:9500, w:1000, h:2100 },      // C  at grade in the headwall, opens outward
    soffitOverFlight: 2200                            // C
  },

  /* ---- A.4.8 SENTRY POST ------------------------------------------------ */
  sentry: {
    site: { x0:32000, x1:36000, y0:600, y1:5600 },  // A  U4 - EAST position adopted by RC4.
                                                    //    A drawing convention, not a survey coordinate.
    ext: { l:4000, w:5000 }, int: { l:3600, w:4600 },// C
    gridA: 175, gridB: 3825, grid1: 175, grid2: 4825,// C  local to the post
    colGridX: 3650, colGridY: 4650,                  // C  c/c
    col: 350,                                        // C  C1 350 x 350, 4 No., both storeys
    beam: { b:250, d:450 },                          // C  B1 and B2
    slab: 150,                                       // C  S1 two-way
    plinth: { b:250, d:400, z:0.450 },               // C
    ftg: { l:1500, w:1500, d:600, z:-2.000 },        // C  F1 on in-situ basalt
    infillGF: 200,                                   // C  RC ballistic panels
    visionPanel: 1200,                               // C  first storey armoured vision panels
    spiral: { r:1000, pole:250 },                    // C  external
    door: 900,                                       // C  D1
    standoffRule: '>= 10 m clear of the shelter excavation', // C
    standoffToBoxFace: 10.00,   // C  X 32000 less box face X 22000
    standoffToExcav:    9.00,   // C  RC4-F3: excavation face with 1000 working space is at X 23000
    blastDesigned: false        // C  NOT blast designed - declared expendable
  },

  /* ---- A.7.1 BLAST ------------------------------------------------------ */
  blast: {
    dbt:     'nuclear air-blast',    // C
    pso:      344.7,                 // C  kPa = 50 psi
    psoPsi:   50,                    // C
    tdMin:    0.13, tdMax: 1.33,     // C  positive phase, s
    pr:       1366,                  // C  reflected pressure, kPa
    q:        282,                   // C  dynamic pressure, kPa
    mu:       5,                     // C  ductility ratio, moderate repairable damage
    dlf:      1.111,                 // C  mu/(mu-0.5) = 5/4.5
    design:   383,                   // C  344.7 x 1.111, applied to roof AND walls (Ka = 1.0)
    roofT:    13.4,                  // C  natural period, ms -> td/T 10..100 -> QUASI-STATIC
    comb103:  448.15,                // C  total roof load, A.7.4
    lateralAtFloor: 83.2,            // C  earth + water at (-)6.100, kPa
    lateralGrad: 15.41,              // C  K0.gamma' + gamma_w, kPa/m (9.81 of it is water)
    uplift:   46.11,                 // C  hydrostatic on mat, kPa; 6289 kN over 136.4 m2
    sbc:      3240,                  // A  presumptive, IS 1904:1986 Table 1, hard rock
    falloutPF: 2200,                 // C  against a requirement of ~1000
    caveat:   'IS 4991:1968 excludes nuclear explosions - used for its loading rules only' // C
  },

  /* ---- A.7.3 ENGINEERED COVER BUILD-UP, top to bottom ------------------- */
  /* Six layers, 2000 total, 39.15 kPa + a declared 1.50 allowance = 40.65   */
  coverLayers: [
    { t:300, name:'TOPSOIL / TURF',        kpa:5.40,  fn:'Concealment, erosion, sheds rain', col:[0.28,0.31,0.19] },
    { t:150, name:'GRANULAR FILTER',       kpa:2.85,  fn:'Stops fines clogging',             col:[0.62,0.58,0.48] },
    { t:200, name:'RC BURSTER SLAB M30',   kpa:5.00,  fn:'Breaks up a penetrating item',     col:[0.60,0.60,0.58] },
    { t:500, name:'CRUSHED BASALT RUBBLE', kpa:8.50,  fn:'Scatters burster energy',          col:[0.34,0.33,0.33] },
    { t:750, name:'COMPACTED FILL 95% MDD',kpa:15.00, fn:'Radiation mass',                   col:[0.45,0.37,0.26] },
    { t:100, name:'PROTECTION SCREED',     kpa:2.40,  fn:'Protects waterproofing',           col:[0.55,0.54,0.52] }
  ],
  coverTotal: { t:2000, sum:39.15, allowance:1.50, design:40.65 }, // C  RC1 ruling C17
  bursterFall: { grade:50, crownY:3100, dropAtEdge:62 },           // C  BS1: 1:50 crossfall

  /* ---- A.5 MATERIALS ---------------------------------------------------- */
  materials: {
    concrete: 'M35 (box) / M30 (burster slab) / M15 (blinding)',  // C
    steel:    'Fe500D',                                            // C
    codes:    'IS 456:2000 - IS 4991:1968 - IS 13920 - IS 10262:2019', // C
    fckDyn:   43.75,   // C  1.25 x 35, BLAST CASE ONLY, IS 4991 Cl 10.3.1
    fyDyn:    625      // C  1.25 x 500
  },

  /* ---- GEOLOGY, master A.6 + SG1 ---------------------------------------- */
  geology: {
    ground:   'Deccan basalt (trap), with red-bole / vesicular seams at flow contacts', // A
    surface:  'BLACK COTTON, CH, free swell index 60-65%',  // C  SG1, top band of the IS 1498 scale
    rockhead: '0.9 - 1.5 m measured at three locations',    // C  SG1
    hazard:   'The hazard is not the basalt - it is the flow contacts', // C
    gammaBulk: 20, gammaSat: 21, K0: 0.50, phi: 30          // A
  },

  /* ---- 9.1 HVAC AND CBRN ------------------------------------------------ */
  cbrn: {
    envelope:   'Bays 1-6',                    // C  gas-tight
    envArea:    67.80, envVol: 216.96,         // C  m2 / m3
    cleanArea:  57.80, cleanVol: 184.96,       // R  envelope less the 10.0 m2 airlock
    trains:     2, trainDuty: 300,             // C  m3/h each, HEPA H14 + activated carbon
    trainWidth: 1450,                          // C  in a 1560 clear bay - 110 mm at the sides
    hepa:       'HEPA H14 (EN 1822, >= 99.995 % at MPPS) + activated carbon', // C
    femaReq:    264.3,                         // C  FEMA 453, 0.25 cfm/ft2
    leakage:    32.5,                          // R  0.15 vol/h = 10.8 % of one train
    ventSurv:   45, ventWork: 135,             // C  5x9 and 15x9 m3/h
    co2Time:    9.9,                           // C  h to 1.0 % CO2, airlock shut
    purge:      12.8,                          // C  min for 5 x 64 m3 at 300 m3/h
    o2store:    15,                            // C  m3 (2 x 50 L at 150 bar) = 80 h
    overpressLo: 50, overpressHi: 100,         // C  Pa
    scrubber:   75,                            // C  m3/h CO2 scrubber loop (RC7)
    closedLimit: 48,                           // C  h - set by the soda lime, not by power
    valves: [                                  // C  five blast valves
      { mark:'BV-1', dn:100 }, { mark:'BV-2', dn:100 }, { mark:'BV-3', dn:100 },
      { mark:'BV-4', dn:350 }, { mark:'BV-5', dn:350 }
    ],
    valveNote: 'All five shut at the shock; BV-4/BV-5 REOPEN for GEN-1 (RC2). 48 h' // C
  },

  /* ---- 17 ELECTRICAL ---------------------------------------------------- */
  power: {
    gen: 'GEN-1, 15 kVA, Bay 8',   // C
    genLoad: 7.360, genPct: 49,    // C  kVA against 15 kVA
    essential: 1.283,              // C  kW essential load
    battery: '149 Ah, 48 V',       // C  Case A confirmed by RC2
    dayTank: 250,                  // C  L nominal, bay 8, fill+vent up the EXISTING SH-2 bore
    earthing: '5 ohm',             // C
    duration: 96                   // C  h
  },

  /* ---- 19 EMP ----------------------------------------------------------- */
  emp: {
    /* The three-zone model is DERIVED BY EM1 and ADOPTED by owner ruling RC2. */
    zones: [
      { z:'EMP ZONE 0', extent:'Everything above grade', perf:'No attenuation credited' }, // D
      { z:'EMP ZONE 1', extent:'The buried box - the rebar cage',
        perf:'A genuine low-frequency measure. NOT a MIL-STD boundary and not to be credited as one' }, // D
      { z:'EMP ZONE 2', extent:'Welded steel enclosure, Bay 3',
        perf:'80 dB across the band - the only surface in this project that delivers it' }   // D
    ],
    zone2Encl: { l:2400, w:1600, h:2200 },  // A  EM1 designs it at 2400 x 1600 x 2200 external
    zone2dB: 80,                             // C  the design rule: full 80 dB standing alone
    zone2Load: 1.50,                         // A  kW allowance, Z-01, sub-board DB-Z2
    rebarSpacing: 150,                       // C  a deliberate EMP decision, 99.99 dB at the cage's band
    verifyCode: 'IEEE Std 299'               // C  shielding effectiveness survey
  },

  /* ---- 16 WATER, SEWAGE, SANITATION ------------------------------------- */
  sanitation: {
    mark: 'SN-03',                                        // C
    fixture: 'SEALED-CASSETTE CHEMICAL TOILET',           // C
    room: 'U-02 lavatory, Bay 2',                         // C
    discharge: 'NO DISCHARGE',                            // C
    rule: 'In protective mode the shelter is sealed and uses sealed-cassette ' +
          'chemical toilets - nothing is discharged at all',   // C
    peacetime: 'Septic tank ST-01 -> foul soak pit SK-01, peacetime use ONLY', // C
    sumpStore: 3375, sumpIn: 400, sumpDays: 8             // C  L store, L/day, days with no power
  },

  /* ---- OCCUPANCY -------------------------------------------------------- */
  occupancy: { n: 9, hours: 96, berths: 9, bunks: '3 x 3-tier' }, // C

  /* ---- COST ------------------------------------------------------------- */
  cost: { estimate: '2.98 cr', protectiveContent: 70 },  // C  project flier, SSR 2022-23

  /* =======================================================================
     ANIMATION-ONLY NARRATIVE VALUES — class [V].
     These carry NO engineering weight. They exist so the camera has
     somewhere to stand and the soldier has somewhere to walk. They are
     declared in ANIMATION_DESIGN_BASIS.md section 4 and must never be
     quoted back into the engineering record.
     ======================================================================= */
  narrative: {
    steps: 56,              // V  the presenter's requirement, not a project value
    /* The pace is DERIVED, not chosen: the walked route is fixed by the two
       real endpoints (the sentry post door D1 and the entry stairwell door at
       X 9250) and the ground between them, and the pace is that route's
       measured length divided by 56. Printed on screen at the 56th step. */
    pace: null,             // V  derived at build time, mm per footfall
    walkLen: null,          // V  derived at build time, mm
    cadence: 0.95,          // V  s per footfall
    blastAzimuth: 115,      // V  degrees, BEARING TO THE BURST from north, clockwise.
                            //    East-south-east, so the wave crosses the sentry post
                            //    BEFORE the shelter - the only ordering the stand-off
                            //    argument allows. Checked: FC_SENTRY -29.50 < FC_BOX -8.66
    blastRange: 2400,       // V  m to the burst - far enough that it reads as a distant event
    siteRadius: 130         // V  m of modelled terrain around the origin
  }
};

/* Convenience: bay centre in scene metres */
function bayCentreX(b){ return (b.x0 + b.x1) * 0.5 * MM; }
