/* ===========================================================================
   AN1 — INTERIOR FIT-OUT AND FIGURES
   Bay contents are exactly master A.3's bay schedule and nothing else.
   Where a bay's contents are listed but not dimensioned, the item is drawn
   as a plain block at the listed position — never detailed into something
   the project has not specified.
   =========================================================================== */

/* rotations the figure rig needs (the fabric only ever needs Z) */
/* Swing is about the local Y axis: after base = translate * rotZ(yaw),
   local +X is the direction of travel, so a rotation about Y swings the
   limb FORWARD and BACK. Rotating about X splayed the legs sideways. */
M4.rotY = a => { const c=Math.cos(a), s=Math.sin(a), o=M4.ident();
  o[0]=c; o[2]=-s; o[8]=s; o[10]=c; return o; };
M4.rotZ = a => { const c=Math.cos(a), s=Math.sin(a), o=M4.ident();
  o[0]=c; o[1]=s; o[4]=-s; o[5]=c; return o; };
M4.trans = t => { const o=M4.ident(); o[12]=t[0]; o[13]=t[1]; o[14]=t[2]; return o; };

const FLOOR = PROJ.lvl.floor;

function buildFitout(){
  const B = new Builder();
  const bay = n => PROJ.bays.find(b=>b.n===n);
  const F = FLOOR;

  /* --- BAY 1 STORES: 1000 L potable tank + shelving ------------------- */
  {
    const b = bay(1);
    B.cyl((b.x0+900)*MM, 1.5, F, F+1.45, 0.55, MAT.steelLt, 18);
    B.disc((b.x0+900)*MM, 1.5, F+1.45, 0.55, MAT.steelLt, 18);
    for(let i=0;i<4;i++)
      B.mm(b.x0+150, 3800, b.x1-150, 4400, F+0.35+i*0.52, F+0.39+i*0.52, MAT.steel);
    B.mm(b.x0+150, 4500, b.x0+1400, 5400, F, F+0.9, MAT.bunk);
  }

  /* --- BAY 2 WC / MED: lavatory 1800x2000 + medical 1800x3000 --------- */
  {
    const b = bay(2);
    B.mm(b.x0, 2600, b.x1, 2710, F, F+2.4, MAT.concDark);      // the divider
    /* SN-03 SEALED-CASSETTE CHEMICAL TOILET — no discharge, master 16.6  */
    B.mm(b.x0+520, 900, b.x0+1160, 1560, F, F+0.42, MAT.steelLt);
    B.mm(b.x0+520, 1300, b.x0+1160, 1560, F+0.42, F+0.86, MAT.steelLt);
    B.mm(b.x0+300, 2100, b.x0+800, 2450, F+0.78, F+0.86, MAT.steelLt);   // basin
    /* medical: examination bunk */
    B.mm(b.x0+300, 3000, b.x1-300, 5000, F+0.50, F+0.62, MAT.bunk);
  }

  /* --- BAY 3 OPS ROOM: plotting + the EMP Zone 2 enclosure ------------ */
  {
    const b = bay(3), Z = PROJ.emp.zone2Encl;
    /* ops desks along the south wall, hazard plotting table in the middle */
    B.mm(b.x0+200, 750, b.x1-200, 1500, F+0.68, F+0.76, MAT.bunk);
    for(const x of [b.x0+500, b.x0+1600, b.x0+2700])
      B.mm(x, 900, x+560, 1450, F+0.76, F+1.22, MAT.steel);   // consoles
    B.mm(b.x0+900, 2400, b.x0+2600, 3600, F+0.86, F+0.94, MAT.bunk);
    for(const [dx,dy] of [[900,2400],[2540,2400],[900,3540],[2540,3540]])
      B.mm(b.x0+dx, dy, b.x0+dx+60, dy+60, F, F+0.86, MAT.steel);
    /* EMP ZONE 2 — welded steel enclosure, 2400 x 1600 x 2200 external.
       The only surface in this project that delivers 80 dB. */
    const zx = b.x0 + 520, zy = 3900;
    B.mm(zx, zy, zx+Z.l, zy+Z.w, F, F+Z.h*MM, MAT.z2);
    B.mm(zx-40, zy-40, zx+Z.l+40, zy+Z.w+40, F+Z.h*MM, F+Z.h*MM+0.05, MAT.steel);
    /* the RF door leaf and its knife-edge frame, read as a recessed panel */
    B.mm(zx+Z.l-0.04/MM, zy+260, zx+Z.l, zy+Z.w-260, F+0.05, F+2.05, MAT.steelLt);
  }

  /* --- BAY 4 BERTHING: 3 x 3-tier bunks, 9 berths --------------------- */
  {
    const b = bay(4);
    for(let s=0;s<3;s++){
      const y0 = 700 + s*1600;
      for(let t=0;t<3;t++){
        const z = F + 0.42 + t*0.72;
        B.mm(b.x0+180, y0, b.x1-180, y0+750, z, z+0.10, MAT.bunk);
      }
      for(const dx of [180, (b.x1-b.x0)-240])
        for(const dy of [0, 690]){
          B.mm(b.x0+dx, y0+dy, b.x0+dx+60, y0+dy+60, F, F+2.02, MAT.steel);
        }
    }
  }

  /* --- BAY 5 CBRN PLANT: 2 x 300 m3/h trains, CO2/O2, sump ------------ */
  {
    const b = bay(5), tw = PROJ.cbrn.trainWidth;
    /* each train is 1450 wide in a 1560 clear bay - 110 mm at the sides,
       so both run ALONG the bay. Master 9.1 / HV-F3. */
    for(let i=0;i<PROJ.cbrn.trains;i++){
      const y0 = 800 + i*1900;
      B.mm(b.x0+55, y0, b.x0+55+tw, y0+1500, F, F+1.95, MAT.steel);
      B.mm(b.x0+55, y0+120, b.x0+55+tw, y0+430, F+0.30, F+1.70, MAT.steelLt);  // HEPA cassette
      B.mm(b.x0+55, y0+560, b.x0+55+tw, y0+880, F+0.30, F+1.70, MAT.z2);       // carbon
    }
    /* CO2 scrubber / O2 store: 2 x 50 L at 150 bar */
    for(const dy of [4500, 4900])
      B.cyl((b.x0+400)*MM, dy*MM, F, F+1.42, 0.13, MAT.steelLt, 14);
    B.mm(b.x0+800, 4400, b.x1-100, 5350, F, F+1.10, MAT.steel);   // dehumidifier
    /* SU-01 clean sump: a 1500 x 1500 opening in the mat, invert (-)7.600.
       DR-A2-V1 records that nothing in the project specifies its cover, so
       it is drawn OPEN with its edge trimmed - not closed with an invented lid. */
    B.mm(b.x0+30, 2600, b.x0+1530, 4100, PROJ.lvl.sumpInvert, F, MAT.concWet);
  }

  /* --- BAY 6 DECON AIRLOCK: 3 stages, 2000x2000 / 2000x1500 / 2000x1500 */
  {
    const b = bay(6);
    for(const y of [2600, 4100]){
      B.mm(b.x0, y, b.x1, y+110, F, F+2.10, MAT.concDark);        // stage divider
      B.mm(b.x0+400, y, b.x0+1300, y+110, F, F+2.10, [0,0,0]);     // the pass-through
    }
    B.mm(b.x0+120, 700, b.x0+520, 2400, F, F+0.06, MAT.steelLt);   // grating, stage 1
  }

  /* --- BAY 8 GENERATOR (grey zone): GEN-1 15 kVA + 250 L day tank ----- */
  {
    const b = bay(8);
    B.mm(b.x0+300, 900, b.x0+2400, 2500, F, F+0.22, MAT.concWet);  // plinth
    B.mm(b.x0+380, 980, b.x0+2320, 2420, F+0.22, F+1.34, MAT.steel);
    B.cyl((b.x0+700)*MM, 1.7, F+1.34, F+1.66, 0.30, MAT.steelLt, 14);
    /* EL-V2 / RC5: a 250 L day tank inside bay 8, fill and vent routed up
       the EXISTING SH-2 bore - no new envelope penetration is created. */
    B.mm(b.x0+2600, 900, b.x1-200, 1700, F, F+0.95, MAT.steelLt);
    /* main LV board */
    B.mm(b.x0+300, 4900, b.x0+1900, 5150, F+0.30, F+2.10, MAT.steel);
  }
  return B.build();
}

/* ---------------------------------------------------------------------- */
/* FIGURES                                                                 */
/* Generic, low-detail, no identifiable likeness (brief section 7).        */
/* Built once in local coordinates about the feet, then instanced.         */
/* ---------------------------------------------------------------------- */
function figureTorso(scale){
  const B = new Builder(), s = scale||1;
  const c = MAT.cloth, sk = MAT.skin;
  B.box(-0.17*s,-0.10*s,0.84*s, 0.17*s,0.10*s,1.38*s, c);          // torso
  B.box(-0.20*s,-0.11*s,1.20*s, 0.20*s,0.11*s,1.40*s, c);          // shoulders
  B.box(-0.075*s,-0.075*s,1.40*s, 0.075*s,0.075*s,1.52*s, sk);     // neck + head
  B.box(-0.095*s,-0.095*s,1.50*s, 0.095*s,0.095*s,1.70*s, sk);
  B.box(-0.105*s,-0.105*s,1.655*s, 0.105*s,0.105*s,1.72*s, c);     // headgear
  return B.build();
}
function figureArm(scale,side){
  const B = new Builder(), s = scale||1;
  B.box(-0.055*s,-0.055*s,-0.52*s, 0.055*s,0.055*s,0.02*s, MAT.cloth);
  return B.build();
}
function figureLeg(scale){
  const B = new Builder(), s = scale||1;
  B.box(-0.070*s,-0.070*s,-0.84*s, 0.070*s,0.070*s,0.02*s, MAT.cloth);
  B.box(-0.075*s,-0.115*s,-0.90*s, 0.075*s,0.065*s,-0.80*s, [0.14,0.13,0.12]);  // boot
  return B.build();
}
/* seated variant for the ops consoles */
function figureSeated(scale){
  const B = new Builder(), s = scale||1;
  B.box(-0.17*s,-0.10*s,0.44*s, 0.17*s,0.10*s,0.98*s, MAT.cloth);
  B.box(-0.20*s,-0.11*s,0.80*s, 0.20*s,0.11*s,1.00*s, MAT.cloth);
  B.box(-0.095*s,-0.095*s,1.10*s, 0.095*s,0.095*s,1.30*s, MAT.skin);
  B.box(-0.075*s,-0.075*s,1.00*s, 0.075*s,0.075*s,1.12*s, MAT.skin);
  B.box(-0.15*s,-0.34*s,0.36*s, 0.15*s,-0.06*s,0.46*s, MAT.cloth);   // thighs
  B.box(-0.15*s,-0.38*s,-0.02*s, 0.15*s,-0.26*s,0.40*s, MAT.cloth);  // shins
  return B.build();
}

/* The nine. Positions are inside the bays master A.3 assigns them to, and
   the count is master A.1's confirmed occupancy — nine, not a chosen number. */
function occupantStations(){
  const b = n => PROJ.bays.find(x=>x.n===n);
  const B3 = b(3), B4 = b(4), B5 = b(5), B1 = b(1), B8 = b(8);
  return [
    /* Bay 3 OPS ROOM — four: three at consoles, one at the plotting table */
    { p:[(B3.x0+780)*MM, 1.95, FLOOR], yaw:-Math.PI/2, seated:true,  bay:3 },
    { p:[(B3.x0+1880)*MM, 1.95, FLOOR], yaw:-Math.PI/2, seated:true,  bay:3 },
    { p:[(B3.x0+2980)*MM, 1.95, FLOOR], yaw:-Math.PI/2, seated:true,  bay:3 },
    { p:[(B3.x0+1750)*MM, 2.10, FLOOR], yaw: Math.PI/2, seated:false, bay:3 },
    /* Bay 4 BERTHING — two off watch */
    { p:[(B4.x0+900)*MM, 1.30, FLOOR], yaw: 0.4, seated:false, bay:4 },
    { p:[(B4.x0+900)*MM, 4.20, FLOOR], yaw:-2.2, seated:false, bay:4 },
    /* Bay 5 CBRN PLANT — one at the filter trains */
    { p:[(B5.x0+1250)*MM, 2.05, FLOOR], yaw: Math.PI, seated:false, bay:5 },
    /* Bay 1 STORES — one */
    { p:[(B1.x0+1250)*MM, 4.05, FLOOR], yaw:-0.9, seated:false, bay:1 },
    /* Bay 8 GENERATOR, the grey zone — one */
    { p:[(B8.x0+2100)*MM, 3.30, FLOOR], yaw: 2.6, seated:false, bay:8 }
  ];
}
