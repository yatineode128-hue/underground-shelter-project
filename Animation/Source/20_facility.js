/* ===========================================================================
   AN1 — FACILITY GEOMETRY
   Every dimension below is read from PROJ (00_data.js), which is itself a
   transcription of master Parts A and B. No dimension is written twice and
   none is invented here.
   =========================================================================== */

const L = PROJ.lvl, BX = PROJ.box;

/* Restrained palette. Concrete reads as concrete, soil as soil, rock as
   rock — brief section 29. No glowing colours anywhere in the fabric. */
const MAT = {
  conc:     [0.780,0.772,0.742],   // M35 fair-faced, formwork marked
  concDark: [0.620,0.614,0.592],   // soffits and buried faces
  concWet:  [0.690,0.688,0.668],   // mat and blinding
  blind:    [0.700,0.686,0.652],   // M15 PCC
  steel:    [0.452,0.474,0.496],   // plant and frames
  steelLt:  [0.600,0.615,0.628],
  door:     [0.500,0.516,0.500],   // blast doors
  z2:       [0.628,0.608,0.560],   // welded steel EMP enclosure
  basalt:   [0.336,0.330,0.356],   // Deccan trap
  redbole:  [0.436,0.306,0.248],   // the flow-contact seam - the named hazard
  cotton:   [0.286,0.258,0.226],   // black cotton, CH, FSI 60-65 %
  murrum:   [0.582,0.442,0.296],
  backfill: [0.540,0.462,0.352],
  turf:     [0.412,0.462,0.296],
  turfDry:  [0.556,0.548,0.382],
  cloth:    [0.402,0.428,0.348],   // generic olive field clothing
  skin:     [0.612,0.500,0.418],
  bunk:     [0.540,0.528,0.492],
  glassZ2:  [0.460,0.520,0.548]
};

/* --- the excavation: box + 1000 working space each side (WM-V9 / RC6) --- */
const EXC = { x0:-1.0, x1:23.0, y0:-1.0, y1:7.2 };
/* --- the modelled ground block that the section cuts through ------------ */
const SITE = { x0:-34, x1:64, y0:-30, y1:38 };
/* the wider plot, meshed coarsely, so the ground reaches the fog and the
   viewer never sees the edge of the model */
const FAR  = { x0:-420, x1:450, y0:-420, y1:420 };

/* Berm: graded 1.5:1 against the headhouse and the entry stairwell walls,
   up to +0.900 (master A.4.6, A.4.7). Everywhere else the site is at grade,
   crowned and falling 1:50 away (A.4.3). */
function bermH(x,y){
  const run = L.hhRoofTop * PROJ.headhouse.bermSlope;     // 0.900 x 1.5 = 1.35 m
  let h = 0;
  const rects = [
    [PROJ.headhouse.ext.x0*MM, PROJ.headhouse.ext.y0*MM, PROJ.headhouse.ext.x1*MM, PROJ.headhouse.ext.y1*MM],
    [PROJ.entry.ext.x0*MM,     PROJ.entry.ext.y0*MM,     PROJ.entry.ext.x1*MM,     PROJ.entry.ext.y1*MM]
  ];
  for(const [a,b,c,d] of rects){
    const dx = Math.max(a-x, 0, x-c), dy = Math.max(b-y, 0, y-d);
    const dist = Math.hypot(dx,dy);
    h = Math.max(h, L.hhRoofTop * clamp(1 - dist/run, 0, 1));
  }
  return h;
}
/* Grade is a FINISHED, PREPARED site level: master A.4.3 records 0.000,
   "crowned, falls 1:50 away". The near plot therefore stays within a few
   centimetres of datum and is CLAMPED so it can never sink below the top of
   the strata cap at STRATA_TOP - if it did, the black cotton band would
   render over the ground and hide it. */
const STRATA_TOP = -0.140;
function groundZ(x,y){
  const b = bermH(x,y);
  if(b > 0.001) return b;
  const cy = PROJ.bursterFall.crownY*MM;
  let z = -Math.abs(y-cy)/PROJ.bursterFall.grade;          // the 1:50 crown
  z += (hash(x*0.13)+hash(y*0.17)-1.0) * 0.045;            // surface irregularity
  return clamp(z, STRATA_TOP + 0.030, 0.10);
}
/* Beyond the prepared plot the ground is ordinary country, falling gently
   away. It starts exactly where the near plot ends, so the two meet without
   a step. */
function farZ(x,y){
  const dx = Math.max(SITE.x0-x, 0, x-SITE.x1), dy = Math.max(SITE.y0-y, 0, y-SITE.y1);
  const d = Math.hypot(dx,dy);
  return -0.15 - d*0.006 + (hash(x*0.031)+hash(y*0.037)-1.0) * Math.min(d*0.022, 1.30);
}

/* ---------------------------------------------------------------------- */
/* 1. TERRAIN                                                              */
/* ---------------------------------------------------------------------- */
function buildTerrain(){
  const B = new Builder();
  /* --- the wider plot, coarse, running out to the fog -------------------
     Meshed as four rectangles fitted around the near plot rather than a grid
     with the middle punched out, because a punched grid leaves a ring of
     dropped cells wherever a cell only PARTLY overlaps - and that ring shows
     as a gap of sky along the horizon. */
  const rings = [
    { x0:FAR.x0,  x1:FAR.x1,  y0:FAR.y0,  y1:SITE.y0 },
    { x0:FAR.x0,  x1:FAR.x1,  y0:SITE.y1, y1:FAR.y1  },
    { x0:FAR.x0,  x1:SITE.x0, y0:SITE.y0, y1:SITE.y1 },
    { x0:SITE.x1, x1:FAR.x1,  y0:SITE.y0, y1:SITE.y1 }
  ];
  for(const r of rings){
    const nx = Math.max(2, Math.round((r.x1-r.x0)/16)), ny = Math.max(2, Math.round((r.y1-r.y0)/16));
    const sx = (r.x1-r.x0)/nx, sy = (r.y1-r.y0)/ny;
    for(let i=0;i<nx;i++) for(let j=0;j<ny;j++){
      const x0=r.x0+i*sx, x1=x0+sx, y0=r.y0+j*sy, y1=y0+sy;
      const c = V3.lerp(MAT.turf, MAT.turfDry, hash(x0*0.7+y0*1.9));
      B.quad(V3.c(x0,y0,farZ(x0,y0)), V3.c(x1,y0,farZ(x1,y0)),
             V3.c(x1,y1,farZ(x1,y1)), V3.c(x0,y1,farZ(x0,y1)), c, 0.95);
    }
  }
  /* --- the near plot, fine, carrying the crown and the berm ------------- */
  const N = 150, gx = (SITE.x1-SITE.x0)/N, gy = (SITE.y1-SITE.y0)/N;
  const inExc = (x,y) => x>EXC.x0-gx && x<EXC.x1+gx && y>EXC.y0-gy && y<EXC.y1+gy;
  for(let i=0;i<N;i++) for(let j=0;j<N;j++){
    const x0=SITE.x0+i*gx, x1=x0+gx, y0=SITE.y0+j*gy, y1=y0+gy;
    const mx=(x0+x1)/2, my=(y0+y1)/2;
    /* the excavation footprint is surfaced by the engineered cover and the
       berm, not by natural ground - leave the hole for them to fill */
    if(inExc(mx,my) && bermH(mx,my) < 0.005) continue;
    const p00=V3.c(x0,y0,groundZ(x0,y0)), p10=V3.c(x1,y0,groundZ(x1,y0)),
          p11=V3.c(x1,y1,groundZ(x1,y1)), p01=V3.c(x0,y1,groundZ(x0,y1));
    const r = Math.hypot(mx-11,my-3.1);
    /* drier, more worn ground close to the works; turf further out */
    const t = clamp(smoothstep(3, 30, r) * 0.75 + hash(i*7.3+j*3.1)*0.25, 0, 1);
    const c = V3.lerp(MAT.turfDry, MAT.turf, t);
    B.quad(p00,p10,p11,p01,c, 0.88 + hash(i*2.7+j*5.9)*0.12);
  }
  return B.build();
}

/* THE BERM.
   Graded 1.5:1 against all four headhouse walls and against the entry
   stairwell walls, up to +0.900 (master A.4.6 / A.4.7). It sits ON the
   engineered cover, which is why it is meshed separately from both: the
   cover is six flat layers below grade, the berm is the earth above it. */
function buildBerm(){
  const B = new Builder();
  const pad = 2.0;
  const x0 = Math.min(PROJ.headhouse.ext.x0, PROJ.entry.ext.x0)*MM - pad;
  const x1 = Math.max(PROJ.headhouse.ext.x1, PROJ.entry.ext.x1)*MM + pad;
  const y0 = Math.min(PROJ.headhouse.ext.y0, PROJ.entry.ext.y0)*MM - pad;
  const y1 = Math.max(PROJ.headhouse.ext.y1, PROJ.entry.ext.y1)*MM + pad;
  const N = 96, gx = (x1-x0)/N, gy = (y1-y0)/N;
  for(let i=0;i<N;i++) for(let j=0;j<N;j++){
    const ax=x0+i*gx, bx=ax+gx, ay=y0+j*gy, by=ay+gy;
    const h = [bermH(ax,ay), bermH(bx,ay), bermH(bx,by), bermH(ax,by)];
    if(Math.max(...h) < 0.004) continue;
    const c = V3.lerp(MAT.turfDry, MAT.turf, clamp(Math.max(...h)/0.9, 0, 1));
    B.quad(V3.c(ax,ay,h[0]), V3.c(bx,ay,h[1]), V3.c(bx,by,h[2]), V3.c(ax,by,h[3]),
           c, 0.90 + hash(i*3.3+j*5.1)*0.10);
  }
  return B.build();
}

/* ---------------------------------------------------------------------- */
/* 2. STRATA — what the section exposes                                    */
/*    Black cotton cap, rockhead band, Deccan basalt with red-bole seams.  */
/*    Every one of these is [ASSUMED] in master A.6 and is labelled so.    */
/* ---------------------------------------------------------------------- */
function buildStrata(){
  const B = new Builder();
  /* a stratum, drawn as four blocks around the excavation void so the
     box interior is never buried by ground that should not be there */
  const band = (z0,z1,col)=>{
    B.box(SITE.x0,SITE.y0,z0, SITE.x1,EXC.y0,z1, col);
    B.box(SITE.x0,EXC.y1,z0, SITE.x1,SITE.y1,z1, col);
    B.box(SITE.x0,EXC.y0,z0, EXC.x0,EXC.y1,z1, col);
    B.box(EXC.x1,EXC.y0,z0, SITE.x1,EXC.y1,z1, col);
  };
  band(L.rockheadHi, STRATA_TOP, MAT.cotton);   // black cotton / murrum cap  [A]
  band(L.rockheadLo, L.rockheadHi, MAT.murrum);  // rockhead band 1.5 to 2.0   [A]
  band(-11.5,        L.rockheadLo, MAT.basalt);  // Deccan trap                [A]
  /* red-bole / vesicular seams at flow contacts. Drawn thin and few: they
     are the hazard the master names, not a decorative stripe. */
  for(const z of [-3.35, -5.10, -7.55]){
    band(z-0.050, z+0.050, MAT.redbole);
  }
  /* founding horizon: the basalt the mat actually sits on, drawn under the
     excavation so the load path has somewhere to end */
  B.box(EXC.x0,EXC.y0,-11.5, EXC.x1,EXC.y1,L.formation, MAT.basalt);
  B.box(EXC.x0,EXC.y0,-7.600, EXC.x1,EXC.y1,-7.500, MAT.redbole);
  return B.build();
}

/* backfill between the box faces and the excavation faces */
function buildBackfill(){
  const B = new Builder();
  const bx1 = BX.lenExt*MM, by1 = BX.widExt*MM;
  B.box(EXC.x0,EXC.y0,L.formation, EXC.x1,0,        0, MAT.backfill);
  B.box(EXC.x0,by1,   L.formation, EXC.x1,EXC.y1,   0, MAT.backfill);
  B.box(EXC.x0,0,     L.formation, 0,     by1,      0, MAT.backfill);
  B.box(bx1,  0,      L.formation, EXC.x1,by1,      0, MAT.backfill);
  return B.build();
}

/* ---------------------------------------------------------------------- */
/* 3. ENGINEERED COVER — the six layers of master A.7.3                    */
/*    2000 total. 39.15 kPa of layers + a declared 1.50 allowance = 40.65. */
/* ---------------------------------------------------------------------- */
function buildCover(){
  const B = new Builder();
  const runs = [
    /* west of the headhouse, stopping clear of the entry stairwell strip */
    { x0:EXC.x0, x1:PROJ.headhouse.ext.x0*MM, y0:EXC.y0, y1:PROJ.entry.ext.y0*MM },
    /* east of the headhouse */
    { x0:PROJ.headhouse.ext.x1*MM, x1:EXC.x1, y0:EXC.y0, y1:EXC.y1 }
  ];
  let z = L.grade;                                   // build downwards from grade
  PROJ.coverLayers.forEach((ly,i)=>{
    const t = ly.t*MM, zTop = z, zBot = z - t;
    for(const r of runs) B.box(r.x0,r.y0,zBot, r.x1,r.y1,zTop, ly.col);
    z = zBot;
  });
  /* the strip under the entry stairwell is ordinary backfill (A.4.7: the
     stairwell sits on a stepped RC raft on compacted fill) */
  B.box(EXC.x0,PROJ.entry.ext.y0*MM,L.roofTop, PROJ.headhouse.ext.x0*MM,EXC.y1,0, MAT.backfill);

  /* TURF CAP over the whole excavation footprint.
     The works are CONCEALED - the cover's own top layer is 300 topsoil/turf
     and CAM2 is a camouflage policy - so the finished ground must read as
     continuous, not as a green rectangle inside a construction patch. The
     cap carries the same colour variation the surrounding terrain does, and
     is 2 mm thick so it never shows in the section.                        */
  const CN = 44, cx = (EXC.x1-EXC.x0)/CN, cy = (EXC.y1-EXC.y0)/CN;
  for(let i=0;i<CN;i++) for(let j=0;j<CN;j++){
    const x0=EXC.x0+i*cx, x1=x0+cx, y0=EXC.y0+j*cy, y1=y0+cy;
    const mx=(x0+x1)/2, my=(y0+y1)/2;
    if(bermH(mx,my) > 0.005) continue;                 // the berm surfaces this
    const r = Math.hypot(mx-11,my-3.1);
    const t = clamp(smoothstep(3, 30, r)*0.75 + hash(i*7.3+j*3.1)*0.25, 0, 1);
    const col = V3.lerp(MAT.turfDry, MAT.turf, t);
    B.box(x0,y0,0.002, x1,y1,0.006, col, [0,0,0,0,1,0]);
  }
  return B.build();
}

/* ---------------------------------------------------------------------- */
/* 4. THE BOX — mat, perimeter walls, pressure slab, internal walls        */
/* ---------------------------------------------------------------------- */
function buildBox(){
  const B = new Builder();
  const X1 = BX.lenExt, Y1 = BX.widExt, t = BX.wallPerim;

  /* blinding and mat */
  B.mm(0,0,X1,Y1, L.formation, L.matUnder, MAT.blind);
  B.mm(0,0,X1,Y1, L.matUnder,  L.floor,    MAT.concWet);

  /* perimeter walls, 600 thk, floor to roof soffit */
  B.mm(0,0,       X1,t,        L.floor, L.roofSoffit, MAT.conc);   // south W1
  B.mm(0,Y1-t,    X1,Y1,       L.floor, L.roofSoffit, MAT.conc);   // north W2
  B.mm(0,t,       t, Y1-t,     L.floor, L.roofSoffit, MAT.conc);   // west  W3
  B.mm(X1-t,t,    X1,Y1-t,     L.floor, L.roofSoffit, MAT.conc);   // east  W4

  /* pressure slab, 900 thk, with the stair void (A.4.4) and the two
     escape-shaft openings (A.4.5) left out of it */
  const v = PROJ.stair.voidS;
  const slabRun = (x0,x1)=>B.mm(x0,0,x1,Y1, L.roofSoffit, L.roofTop, MAT.conc);
  slabRun(0, v.x0);
  slabRun(v.x1, X1);
  /* the band beside the void: the cantilever pad survives north of it */
  B.mm(v.x0,v.y1, v.x1,Y1, L.roofSoffit, L.roofTop, MAT.conc);
  B.mm(v.x0,0,    v.x1,v.y0, L.roofSoffit, L.roofTop, MAT.conc);

  /* internal walls. W6 and W7 are 400 (Modification M1) and are the
     protective boundary; each carries a blast-door opening Y 600-1800. */
  for(const w of PROJ.walls){
    const isBd = (w.mark==='W6'||w.mark==='W7');
    if(isBd){
      const d = PROJ.blastDoors.find(b=>b.wallX===w.x0);
      B.mm(w.x0,t, w.x1,d.y0, L.floor, L.roofSoffit, MAT.conc);
      B.mm(w.x0,d.y1, w.x1,Y1-t, L.floor, L.roofSoffit, MAT.conc);
      B.mm(w.x0,d.y0, w.x1,d.y1, L.floor+d.h*MM, L.roofSoffit, MAT.conc);   // over-door
      /* the blast door leaf itself, 1200 x 2100, >= 7 bar */
      B.mm(w.x0+40,d.y0, w.x1-40,d.y1, L.floor, L.floor+d.h*MM, MAT.door);
    } else if(w.mark==='W5'){
      B.mm(w.x0,t, w.x1,Y1-t, L.floor, L.roofSoffit, MAT.conc);
    } else {
      const g = PROJ.doorGap;
      B.mm(w.x0,t, w.x1,g.y0, L.floor, L.roofSoffit, MAT.conc);
      B.mm(w.x0,g.y1, w.x1,Y1-t, L.floor, L.roofSoffit, MAT.conc);
      B.mm(w.x0,g.y0, w.x1,g.y1, L.floor+2.100, L.roofSoffit, MAT.conc);
    }
  }
  return B.build();
}

/* ---------------------------------------------------------------------- */
/* 5. ESCAPE SHAFTS — 1400 dia, 250 RC collar, OD 1900                     */
/* ---------------------------------------------------------------------- */
function buildShafts(){
  const B = new Builder();
  for(const s of PROJ.escShafts){
    const cx=s.cx*MM, cy=s.cy*MM, ri=s.dia*MM/2, ro=s.od*MM/2;
    B.cyl(cx,cy,L.roofSoffit,L.grade, ro, MAT.concDark, 28);        // collar outside
    B.cyl(cx,cy,L.roofSoffit,L.grade, ri, MAT.concDark, 28, true);  // bore inside
    /* the head hatch at grade (RC5: designed structurally) */
    B.disc(cx,cy,L.grade+0.09, ro*1.06, MAT.door, 28);
    B.cyl(cx,cy,L.grade,L.grade+0.09, ro*1.06, MAT.door, 28);
  }
  return B.build();
}

/* ---------------------------------------------------------------------- */
/* 6. MAIN STAIRCASE — FROZEN geometry (CLAUDE.md).                        */
/*    24R at 170.8333, tread 280, 3 flights x 8, total rise 4100.          */
/* ---------------------------------------------------------------------- */
function buildStairs(){
  const B = new Builder();
  const S = PROJ.stair, r = S.riser*MM, g = S.tread*MM, w = S.width*MM;
  /* one flight of 8 risers, drawn as real treads and risers */
  const flight = (x0, yStart, dir, zStart)=>{
    for(let i=0;i<S.perFlight;i++){
      const z0 = zStart + i*r, z1 = z0 + r;
      const y0 = yStart + dir*i*g, y1 = y0 + dir*g;
      const ya = Math.min(y0,y1), yb = Math.max(y0,y1);
      B.box(x0, ya, z0, x0+w, yb, z1, MAT.conc);          // the step block
    }
  };
  const A = S.flightA.x0*MM, Bf = S.flightB.x0*MM;
  /* flight 1: arrival (-6.100) up to L1 (-4.7333), running north  */
  flight(A, S.arrival.y1*MM, +1, L.floor);
  /* landing L1 */
  B.mm(S.shaft.x0,S.L1.y0, S.shaft.x1,S.L1.y1, S.L1.z-0.25, S.L1.z, MAT.conc);
  /* flight 2: L1 up to L2, running south on flight B */
  flight(Bf, S.L1.y0*MM, -1, S.L1.z);
  /* landing L2, stacked over the arrival landing */
  B.mm(S.shaft.x0,S.L2.y0, S.shaft.x1,S.L2.y1, S.L2.z-0.25, S.L2.z, MAT.conc);
  /* flight 3: L2 up to the headhouse floor (-2.000), running north on A */
  flight(A, S.L2.y1*MM, +1, S.L2.z);
  /* store under landing L1 */
  B.mm(S.shaft.x0,4960, S.shaft.x1,S.shaft.y1, L.floor, L.floor+2.0, MAT.concDark);
  /* the 200 well between the flights, left open — drawn only as the
     edge of the two flights, which is what a well is */
  return B.build();
}

/* ---------------------------------------------------------------------- */
/* 7. HEADHOUSE — 4800 x 5800 external, walls 400, roof 500, top +0.900    */
/* ---------------------------------------------------------------------- */
function buildHeadhouse(){
  const B = new Builder();
  const H = PROJ.headhouse, e=H.ext, n=H.int;
  const z0 = L.roofTop, z1 = L.hhSoffit, z2 = L.hhRoofTop;
  const d = H.innerDoor;
  /* HW1 south, HW2 north (with the inner security door), HW3 west, HW4 east */
  B.mm(e.x0,e.y0, e.x1,n.y0, z0,z1, MAT.conc);
  B.mm(e.x0,n.y1, d.x0,e.y1, z0,z1, MAT.conc);
  B.mm(d.x1,n.y1, e.x1,e.y1, z0,z1, MAT.conc);
  B.mm(d.x0,n.y1, d.x1,e.y1, z0+d.h*MM, z1, MAT.conc);        // over the door
  B.mm(e.x0,n.y0, n.x0,n.y1, z0,z1, MAT.conc);                 // HW3 west
  B.mm(n.x1,n.y0, e.x1,n.y1, z0,z1, MAT.conc);                 // HW4 east
  /* roof 500, over everything except the stair void it shares with the box */
  const v = PROJ.stair.voidS;
  B.mm(e.x0,e.y0, e.x1,v.y0, z1,z2, MAT.conc);
  B.mm(e.x0,v.y1, e.x1,e.y1, z1,z2, MAT.conc);
  B.mm(e.x0,v.y0, v.x0,v.y1, z1,z2, MAT.conc);
  B.mm(v.x1,v.y0, e.x1,v.y1, z1,z2, MAT.conc);
  return B.build();
}

/* ---------------------------------------------------------------------- */
/* 8. COVERED ENTRY STAIRWELL — DECLARED EXPENDABLE (master A.2)           */
/*    12R at 166.6667, going 300, roof 250 raking, platform at (-)2.000    */
/* ---------------------------------------------------------------------- */
function buildEntry(){
  const B = new Builder();
  const E = PROJ.entry, e=E.ext, n=E.int, w=E.wall;
  const fl = E.flight, r = fl.rise*MM, g = fl.going*MM;
  const zAt = x => {                       // soffit datum follows the walking line
    if(x <= fl.x0*MM) return L.grade;
    if(x >= E.platform.x0*MM) return E.platform.z;
    return L.grade - (x - fl.x0*MM)/ (fl.going*MM) * r;
  };
  /* top landing and platform */
  B.mm(E.topLanding.x0,n.y0, E.topLanding.x1,n.y1, -0.25, 0, MAT.conc);
  B.mm(E.platform.x0,n.y0, E.platform.x1,n.y1, E.platform.z-0.25, E.platform.z, MAT.conc);
  /* the 12 steps */
  for(let i=0;i<fl.risers;i++){
    const x0 = fl.x0*MM + i*g, z1 = L.grade - i*r;
    B.box(x0,n.y0*MM, z1-r-0.25, x0+g,n.y1*MM, z1-r, MAT.conc);
    B.box(x0,n.y0*MM, z1-r, x0+g,n.y1*MM, z1, MAT.conc);
  }
  /* side walls 250, following the rake, plus headwall and east wall */
  const seg = 34;
  for(let i=0;i<seg;i++){
    const x0 = n.x0*MM + (e.x1-n.x0)*MM*i/seg, x1 = n.x0*MM + (e.x1-n.x0)*MM*(i+1)/seg;
    const zb = Math.min(zAt(x0),zAt(x1)) - 0.45;
    const zt = Math.max(zAt(x0),zAt(x1)) + E.soffitOverFlight*MM + E.roof*MM;
    B.box(x0,e.y0*MM,zb, x1,n.y0*MM,zt, MAT.conc);
    B.box(x0,n.y1*MM,zb, x1,e.y1*MM,zt, MAT.conc);
    /* raking roof, 250, staying 250 over the platform (RC1 ruling C16) */
    B.box(x0,e.y0*MM, zt-E.roof*MM, x1,e.y1*MM, zt, MAT.conc);
  }
  /* headwall with the 1000 x 2100 entry door at grade, opening outward.
     Built as three pieces AROUND the opening - the opening is absence of
     concrete, not a dark box inside it. */
  const dz  = L.grade + E.door.h*MM;
  const dcy = (n.y0+n.y1)/2, dy0 = dcy - E.door.w/2, dy1 = dcy + E.door.w/2;
  B.mm(e.x0,e.y0, n.x0,dy0,  -0.45, L.grade + 2.45, MAT.conc);
  B.mm(e.x0,dy1,  n.x0,e.y1, -0.45, L.grade + 2.45, MAT.conc);
  B.mm(e.x0,dy0,  n.x0,dy1,  dz,    L.grade + 2.45, MAT.conc);
  B.mm(e.x0,dy0,  n.x0,dy1,  -0.45, L.grade,        MAT.conc);
  /* 300 channel + grating across the full 1500 width, X 8950-9250 */
  B.mm(8950,n.y0, 9250,n.y1, -0.30, L.grade, MAT.steel);
  return B.build();
}

/* ---------------------------------------------------------------------- */
/* 9. SENTRY POST — a separate two-storey RC framed building.              */
/*    NOT blast designed. Declared expendable. Its own footings on rock.   */
/* ---------------------------------------------------------------------- */
function buildSentry(){
  const B = new Builder();
  const S = PROJ.sentry, st = S.site;
  const ox = st.x0, oy = st.y0;                    // post local origin, mm
  const cs = S.col, half = cs/2;
  const cols = [[S.gridA,S.grid1],[S.gridB,S.grid1],[S.gridA,S.grid2],[S.gridB,S.grid2]];
  const P = (lx,ly)=>[ox+lx, oy+ly];

  /* footings F1 1500 x 1500 x 600 on in-situ basalt at (-)2.000 */
  for(const [lx,ly] of cols){
    const [x,y] = P(lx,ly);
    B.mm(x-S.ftg.l/2, y-S.ftg.w/2, x+S.ftg.l/2, y+S.ftg.w/2,
         S.ftg.z, S.ftg.z + S.ftg.d*MM, MAT.concWet);
    B.mm(x-half, y-half, x+half, y+half, S.ftg.z+S.ftg.d*MM, S.plinth.z, MAT.conc);
  }
  /* columns C1 350 x 350, both storeys */
  for(const [lx,ly] of cols){
    const [x,y] = P(lx,ly);
    B.mm(x-half,y-half, x+half,y+half, S.plinth.z, L.sentryRoof, MAT.conc);
  }
  /* plinth beams, then B1/B2 at each floor, then the 150 slabs */
  const beamRing = (zTop)=>{
    const b = S.beam.b, d = S.beam.d, z0 = zTop - d*MM;
    for(const g1 of [S.grid1,S.grid2]){            // B1 spanning A-B, in X
      const [xa,y] = P(S.gridA,g1), [xb] = P(S.gridB,g1);
      B.mm(xa,y-b/2, xb,y+b/2, z0, zTop, MAT.conc);
    }
    for(const gA of [S.gridA,S.gridB]){            // B2 spanning 1-2, in Y
      const [x,y1] = P(gA,S.grid1), [,y2] = P(gA,S.grid2);
      B.mm(x-b/2,y1, x+b/2,y2, z0, zTop, MAT.conc);
    }
  };
  B.mm(ox+S.gridA, oy+S.grid1-S.plinth.b/2, ox+S.gridB, oy+S.grid1+S.plinth.b/2,
       S.plinth.z-S.plinth.d*MM, S.plinth.z, MAT.conc);
  B.mm(ox+S.gridA, oy+S.grid2-S.plinth.b/2, ox+S.gridB, oy+S.grid2+S.plinth.b/2,
       S.plinth.z-S.plinth.d*MM, S.plinth.z, MAT.conc);
  beamRing(L.sentryFF); beamRing(L.sentryRoof);
  for(const z of [L.sentryFF, L.sentryRoof]){
    B.mm(ox, oy, ox+S.ext.l, oy+S.ext.w, z, z + S.slab*MM, MAT.conc);
  }
  /* ground storey: 200 RC ballistic infill panels, full height */
  const inf = S.infillGF;
  const gfz0 = S.plinth.z, gfz1 = L.sentryFF - S.beam.d*MM;
  const dW = S.door;
  B.mm(ox,oy, ox+S.ext.l, oy+inf, gfz0,gfz1, MAT.concDark);                 // south
  B.mm(ox,oy+S.ext.w-inf, ox+S.ext.l, oy+S.ext.w, gfz0,gfz1, MAT.concDark); // north
  B.mm(ox,oy+inf, ox+inf, oy+S.ext.w-inf, gfz0,gfz1, MAT.concDark);         // west
  /* east face carries D1, 900 */
  const dy0 = oy + S.ext.w/2 - dW/2, dy1 = dy0 + dW;
  B.mm(ox+S.ext.l-inf, oy+inf, ox+S.ext.l, dy0, gfz0,gfz1, MAT.concDark);
  B.mm(ox+S.ext.l-inf, dy1, ox+S.ext.l, oy+S.ext.w-inf, gfz0,gfz1, MAT.concDark);
  B.mm(ox+S.ext.l-inf, dy0, ox+S.ext.l, dy1, gfz0+2.100, gfz1, MAT.concDark);
  /* first storey: armoured vision panels 1200 wide, piers between */
  const ffz0 = L.sentryFF + S.slab*MM, ffz1 = L.sentryRoof - S.beam.d*MM;
  const sill = ffz0 + 0.95, head = sill + 0.85;
  const pierRun = (x0,y0,x1,y1,along)=>{
    const span = along==='x' ? x1-x0 : y1-y0;
    const nP = Math.max(2, Math.round(span/(S.visionPanel*1.9)));
    for(let i=0;i<=nP;i++){
      const f = i/nP, pw = 260;
      if(along==='x'){ const px = x0 + f*(span) - pw/2;
        B.mm(clamp(px,x0,x1-pw), y0, clamp(px+pw,x0+pw,x1), y1, ffz0, ffz1, MAT.concDark); }
      else { const py = y0 + f*(span) - pw/2;
        B.mm(x0, clamp(py,y0,y1-pw), x1, clamp(py+pw,y0+pw,y1), ffz0, ffz1, MAT.concDark); }
    }
    /* spandrel below the vision band and the head above it */
    B.mm(x0,y0,x1,y1, ffz0, sill, MAT.concDark);
    B.mm(x0,y0,x1,y1, head, ffz1, MAT.concDark);
    B.mm(x0, y0, x1, y1, sill, head, MAT.steel);   // the armoured panel itself
  };
  pierRun(ox, oy, ox+S.ext.l, oy+inf, 'x');
  pierRun(ox, oy+S.ext.w-inf, ox+S.ext.l, oy+S.ext.w, 'x');
  pierRun(ox, oy+inf, ox+inf, oy+S.ext.w-inf, 'y');
  pierRun(ox+S.ext.l-inf, oy+inf, ox+S.ext.l, oy+S.ext.w-inf, 'y');
  /* parapet to +7.000 */
  const pz0 = L.sentryRoof + S.slab*MM;
  for(const [a,b,c,d] of [[ox,oy,ox+S.ext.l,oy+150],[ox,oy+S.ext.w-150,ox+S.ext.l,oy+S.ext.w],
                          [ox,oy,ox+150,oy+S.ext.w],[ox+S.ext.l-150,oy,ox+S.ext.l,oy+S.ext.w]])
    B.mm(a,b,c,d, pz0, L.sentryPar, MAT.conc);
  /* external spiral stair, 1000 R, 250 dia central pole */
  const sx = (ox+S.ext.l+S.spiral.r+250)*MM, sy = (oy+S.ext.w*0.5)*MM;
  B.cyl(sx,sy, S.plinth.z, L.sentryRoof, S.spiral.pole*MM/2, MAT.steel, 14);
  const turns = 22;
  for(let i=0;i<turns;i++){
    const a0 = i/turns*Math.PI*3.0, a1=(i+1)/turns*Math.PI*3.0;
    const z = S.plinth.z + (L.sentryFF-S.plinth.z)*i/turns;
    const ri = S.spiral.pole*MM/2, ro = S.spiral.r*MM;
    B.quad(V3.c(sx+Math.cos(a0)*ri, sy+Math.sin(a0)*ri, z),
           V3.c(sx+Math.cos(a0)*ro, sy+Math.sin(a0)*ro, z),
           V3.c(sx+Math.cos(a1)*ro, sy+Math.sin(a1)*ro, z),
           V3.c(sx+Math.cos(a1)*ri, sy+Math.sin(a1)*ri, z), MAT.steelLt, 0.95);
  }
  return B.build();
}
