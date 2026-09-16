/* ===========================================================================
   AN1 — EFFECTS AND SYSTEMS VISUALISATION

   RULE OBSERVED THROUGHOUT THIS FILE (brief sections 13 and 31):
   nothing here is an analysis result. No stress contour, no displacement,
   no utilisation and no failure mode is drawn anywhere. The load path is
   CONCEPTUAL - it shows WHERE the load goes, never HOW MUCH arrives.
   The only numbers that ever appear on screen are the ones already printed
   in the master as design INPUTS.
   =========================================================================== */

/* direction-aligned transform for arrows and streamers */
M4.dirTo = function(from, dir, len, rad){
  const d = V3.norm(dir);
  let up = Math.abs(d[2]) > 0.98 ? V3.c(1,0,0) : V3.c(0,0,1);
  const s = V3.norm(V3.cross(up, d)), u = V3.cross(d, s);
  const o = M4.ident();
  o[0]=s[0]*rad; o[1]=s[1]*rad; o[2]=s[2]*rad;
  o[4]=u[0]*rad; o[5]=u[1]*rad; o[6]=u[2]*rad;
  o[8]=d[0]*len; o[9]=d[1]*len; o[10]=d[2]*len;
  o[12]=from[0]; o[13]=from[1]; o[14]=from[2];
  return o;
};
/* shear used to bend the grass field in the blast wind */
M4.shear = function(sx, sy){
  const o = M4.ident(); o[8]=sx; o[9]=sy; return o;
};

/* ---------------------------------------------------------------------- */
/* GRASS — the environmental read-out for the blast wind.                  */
/* Authored rooted at z = 0 and bent whole-field by a shear, so the        */
/* response is uniform and directional, as a pressure front's would be.    */
/* ---------------------------------------------------------------------- */
function buildGrass(){
  const B = new Builder();
  const N = 11000;
  const UP = V3.norm(V3.c(0, 0, 1));
  for(let i=0;i<N;i++){
    const u = hash(i*1.37), v = hash(i*2.91), w = hash(i*4.11);
    /* concentrated along the approach the camera actually travels */
    const x = lerp(-16, 46, u) + (v-0.5)*4.0;
    const y = lerp(-10, 18, v) + (u-0.5)*4.0;
    const gz = groundZ(x,y);
    if(bermH(x,y) > 0.02 && w < 0.45) continue;      // thinner on the berm
    const h = 0.09 + w*0.15, a = hash(i*5.7)*Math.PI;
    const bw = 0.022;
    const dx = Math.cos(a)*bw, dy = Math.sin(a)*bw;
    const c = V3.lerp(MAT.turf, MAT.turfDry, hash(i*7.3)*0.8);
    /* the geometric normal of a blade is horizontal and would read black
       under a high sun, so the blade is lit as if it faced the sky */
    B.quadN(V3.c(x-dx,y-dy,gz), V3.c(x+dx,y+dy,gz),
            V3.c(x+dx*0.35,y+dy*0.35,gz+h), V3.c(x-dx*0.35,y-dy*0.35,gz+h),
            UP, c, 0.96);
  }
  return B.build();
}

/* ---------------------------------------------------------------------- */
/* ARROWS — the structural load path, and nothing more.                    */
/* ---------------------------------------------------------------------- */
function buildArrow(){
  const B = new Builder();
  const c = [0.92,0.62,0.22];                      // one restrained accent, used only here
  const sh = 0.30, r = 0.16;
  /* shaft 0 -> 0.68 of unit length, head 0.68 -> 1.0 */
  for(let i=0;i<10;i++){
    const a0=i/10*Math.PI*2, a1=(i+1)/10*Math.PI*2;
    const p=(a,z,rr)=>V3.c(Math.cos(a)*rr, Math.sin(a)*rr, z);
    B.quad(p(a0,0,r*sh), p(a1,0,r*sh), p(a1,0.68,r*sh), p(a0,0.68,r*sh), c, 0.95);
    B.tri(p(a0,0.68,r), p(a1,0.68,r), V3.c(0,0,1.0), V3.c(0,0,1), c, 1.0);
    B.tri(V3.c(0,0,0.68), p(a1,0.68,r), p(a0,0.68,r), V3.c(0,0,-1), c, 0.7);
  }
  return B.build();
}

/* The load path, stated once, in the order the brief asks for:
   BLAST PRESSURE -> ROOF/PRESSURE SLAB -> RC WALLS -> MAT -> FOUNDING STRATUM.
   Plus the lateral case on the buried walls, which master A.7.2 confirms.  */
function loadPathArrows(){
  const a = [], X = PROJ.box.lenExt*MM, Y = PROJ.box.widExt*MM, L = PROJ.lvl;
  /* 1. blast on to the roof: down on to the pressure slab */
  for(let i=0;i<7;i++){
    const x = lerp(1.6, 13.0, i/6);
    a.push({ stage:0, from:V3.c(x, 1.55, L.grade+1.85), dir:V3.c(0,0,-1), len:1.80 });
  }
  /* 2. roof into the walls: the slab spans the 5000 clear and delivers to
        the 600 perimeter walls */
  for(const x of [3.2, 7.6, 11.4]){
    a.push({ stage:1, from:V3.c(x, 0.30, L.roofSoffit-0.35), dir:V3.c(0,0,-1), len:1.5 });
  }
  /* 3. down the walls */
  for(const x of [3.2, 7.6, 11.4]){
    a.push({ stage:2, from:V3.c(x, 0.30, L.roofSoffit-0.55), dir:V3.c(0,0,-1), len:2.2 });
  }
  /* 4. walls into the mat */
  for(const x of [3.2, 7.6, 11.4]){
    a.push({ stage:3, from:V3.c(x, 0.30, L.floor-0.12), dir:V3.c(0,0,-1), len:0.75 });
  }
  /* 5. mat into the founding stratum */
  for(const x of [2.4, 6.0, 9.6, 13.0]){
    a.push({ stage:4, from:V3.c(x, 1.6, L.matUnder-0.15), dir:V3.c(0,0,-1), len:1.0 });
  }
  /* 6. the lateral case: earth + water on the buried wall, 83.2 kPa at floor.
        Drawn as a gradient - short at the soffit, long at the base - because
        that is what a 15.41 kPa/m gradient is. */
  for(let i=0;i<6;i++){
    const z = lerp(L.roofSoffit-0.25, L.floor+0.3, i/5);
    const f = invLerp(L.roofSoffit, L.floor, z);
    a.push({ stage:5, from:V3.c(5.0, -1.70, z), dir:V3.c(0,1,0), len:0.75+f*0.95 });
  }
  return a;
}

/* ---------------------------------------------------------------------- */
/* AIRFLOW — the CBRN path, as a route through real rooms.                 */
/* Contaminated outside air -> intake -> blast valve -> bay 5 filter        */
/* trains -> clean air into the envelope held at +50 to +100 Pa.            */
/* ---------------------------------------------------------------------- */
function airPath(){
  const b5 = PROJ.bays.find(b=>b.n===5), F = PROJ.lvl.floor;
  /* SH-1 is the intake shaft head; master locates the two shafts 25.30 m
     apart at opposite ends of the box (SG2 / RC8). The intake is drawn at
     the west end, which is the end SH-1 serves. */
  return [
    V3.c(-2.6, 2.2, 4.2), V3.c(-0.9, 2.2, 1.9), V3.c(-0.30, 2.2, -0.6),
    V3.c(-0.30, 2.2, -2.45),                                    // down past the boundary
    V3.c( 0.55, 2.2, -3.30),                                    // through the wall
    V3.c( 2.60, 1.30, -4.25), V3.c( 6.00, 1.15, -4.70),
    V3.c( 9.60, 2.20, -4.90), V3.c((b5.x0+780)*MM, 2.95, F+1.30), // in at the door line
    V3.c((b5.x0+780)*MM, 3.90, F+1.30),                          // through train 1
    V3.c((b5.x0+780)*MM, 5.05, F+1.30),                          // through train 2
    V3.c((b5.x0+300)*MM, 5.30, F+1.60),
    V3.c( 9.00, 4.40, F+1.90), V3.c( 6.00, 4.10, F+2.10),
    V3.c( 3.00, 3.40, F+2.15), V3.c( 1.20, 2.60, F+1.70)         // out into the envelope
  ];
}
/* the point on a polyline at parameter u in [0,1], by arc length */
function polyAt(pts, u){
  let total=0; const seg=[];
  for(let i=0;i<pts.length-1;i++){ const d=V3.dist(pts[i],pts[i+1]); seg.push(d); total+=d; }
  let want = clamp(u,0,1)*total;
  for(let i=0;i<seg.length;i++){
    if(want <= seg[i] || i===seg.length-1)
      return V3.lerp(pts[i], pts[i+1], clamp(want/(seg[i]||1),0,1));
    want -= seg[i];
  }
  return pts[pts.length-1];
}

/* ---------------------------------------------------------------------- */
/* PROTECTED VOLUME — bays 1 to 6, the gas-tight envelope.                 */
/* A restrained BIM highlight. No red box, no "SAFE" label (brief 15).     */
/* ---------------------------------------------------------------------- */
function buildEnvelope(){
  const B = new Builder();
  const b1 = PROJ.bays.find(b=>b.n===1), b6 = PROJ.bays.find(b=>b.n===6);
  const c = [0.40,0.66,0.72];
  B.mm(b1.x0, 600, b6.x1, 5600, PROJ.lvl.floor+0.01, PROJ.lvl.roofSoffit-0.01, c);
  return B.build();
}
/* the EMP Zone 2 enclosure, highlighted on its own at the end */
function buildZone2Hi(){
  const B = new Builder(), Z = PROJ.emp.zone2Encl;
  const b3 = PROJ.bays.find(b=>b.n===3);
  const zx = b3.x0 + 520, zy = 4200;
  B.mm(zx-70, zy-70, zx+Z.l+70, zy+Z.w+70,
       PROJ.lvl.floor, PROJ.lvl.floor+Z.h*MM+0.10, [0.52,0.60,0.46]);
  return B.build();
}

/* ---------------------------------------------------------------------- */
/* PARTICLE DRIVERS                                                        */
/* Every one is a pure function of time, so scrubbing the timeline gives    */
/* exactly the frame that plays. Nothing accumulates.                      */
/* ---------------------------------------------------------------------- */

/* THE BLAST FRONT.
   At 2400 m range the wavefront over a 100 m plot is planar to within a
   few centimetres, so it is drawn as a plane sweeping the site rather than
   as a ring. `s` is the front's position along the direction of travel.
   TRAVEL IS SLOWED FOR LEGIBILITY and the animation says so on screen:
   no arrival time, no propagation velocity and no decay is implied. */
const BLAST_DIR = (function(){
  /* azimuth is the compass BEARING TO THE BURST, measured from north (+Y)
     clockwise. The wave travels the opposite way. The burst sits east-
     south-east, so the front crosses the SENTRY POST before the shelter:
     that ordering is the whole stand-off argument and it is not negotiable. */
  const a = PROJ.narrative.blastAzimuth * Math.PI/180;
  return V3.norm(V3.c(-Math.sin(a), -Math.cos(a), 0));
})();
const frontCoord = (x,y) => x*BLAST_DIR[0] + y*BLAST_DIR[1];
/* front coordinates of the two things that matter, for the timeline */
const FC_SENTRY = frontCoord((PROJ.sentry.site.x0+PROJ.sentry.site.x1)*0.5*MM,
                             (PROJ.sentry.site.y0+PROJ.sentry.site.y1)*0.5*MM);
const FC_BOX    = frontCoord(PROJ.box.lenExt*0.5*MM, PROJ.box.widExt*0.5*MM);

function blastFront(pts, s, camPos){
  const perp = V3.c(-BLAST_DIR[1], BLAST_DIR[0], 0);
  const N = 1100;
  for(let i=0;i<N;i++){
    const along = (hash(i*3.1)-0.5)*3.4;                 // thickness of the front
    const across = (hash(i*1.7)-0.5)*150;                // width across the plot
    const h = hash(i*7.7);
    const x = BLAST_DIR[0]*(s+along) + perp[0]*across;
    const y = BLAST_DIR[1]*(s+along) + perp[1]*across;
    if(x<SITE.x0-14||x>SITE.x1+14||y<SITE.y0-14||y>SITE.y1+14) continue;
    const z = groundZ(x,y) + h*h*9.0 + 0.15;
    const fade = clamp(1.0 - Math.abs(along)/2.0, 0, 1);
    pts.add(x, y, z, 130 + h*230, fade*0.40, clamp(h,0,1), 0);
  }
  /* the dust the front drags along behind it */
  const D = 850;
  for(let i=0;i<D;i++){
    const lag = 1.5 + hash(i*5.3)*26.0;
    const across = (hash(i*2.9)-0.5)*150;
    const x = BLAST_DIR[0]*(s-lag) + perp[0]*across + (hash(i*2.2)-0.5)*4;
    const y = BLAST_DIR[1]*(s-lag) + perp[1]*across + (hash(i*6.6)-0.5)*4;
    if(x<SITE.x0-14||x>SITE.x1+14||y<SITE.y0-14||y>SITE.y1+14) continue;
    const h = hash(i*9.1);
    pts.add(x, y, groundZ(x,y) + h*4.0 + 0.1, 170 + h*300,
            clamp(1 - lag/28, 0, 1) * 0.26, 0.25 + h*0.5, 0);
  }
}

/* settling dust, used after the event and in the return to the surface */
function settlingDust(pts, t, amount, centre){
  if(amount <= 0.001) return;
  const N = 620;
  for(let i=0;i<N;i++){
    const a = hash(i*1.9)*Math.PI*2, r = 4 + hash(i*3.7)*46;
    const x = centre[0] + Math.cos(a)*r, y = centre[1] + Math.sin(a)*r;
    const h0 = hash(i*8.3);
    const drift = t*0.35 + hash(i*4.4)*10;
    const z = groundZ(x,y) + 0.2 + h0*5.5 * Math.exp(-t*0.035);
    pts.add(x + Math.sin(drift)*1.3, y + Math.cos(drift*0.7)*1.1, z,
            140 + h0*180, amount * (0.05 + h0*0.09), 0.30 + h0*0.4, 0);
  }
}

/* airflow: discrete marker particles walking the CBRN route, so the eye
   can follow ONE parcel of air the whole way through the plant */
function airflowParticles(pts, path, t, headU, density, contaminated){
  const N = density||260;
  for(let i=0;i<N;i++){
    const phase = (i/N + t*0.055) % 1;
    if(phase > headU) continue;
    const p = polyAt(path, phase);
    const j = (hash(i*2.3)-0.5)*0.30, k = (hash(i*5.1)-0.5)*0.30;
    /* colour ramp t: 0 = contaminated outside air, 1 = filtered */
    const filtered = phase > 0.62 ? 1 : 0;
    const ramp = filtered ? 1.0 : (contaminated ? 0.0 : 0.45);
    /* seen from a corridor a metre away, not from across a hall: additive
       blending saturates fast, so these are small and faint. The air must
       read as a stream of markers, not as a light source. */
    pts.add(p[0]+j, p[1]+k, p[2]+(hash(i*7.9)-0.5)*0.22,
            22 + hash(i*3.3)*14, 0.20, ramp, 1);
  }
}

/* EMP: a field, not an explosion. A directional wavefront that passes
   through the site, drawn as a thin advancing shell. */
function empField(pts, t, originXY, radius){
  if(radius <= 0) return;
  const N = 1500;
  for(let i=0;i<N;i++){
    const u = hash(i*1.13), v = hash(i*3.71);
    const th = u*Math.PI*2, ph = Math.acos(clamp(v*1.4-0.15,-1,1));
    const rr = radius + (hash(i*5.17)-0.5)*1.4;
    const x = originXY[0] + Math.sin(ph)*Math.cos(th)*rr;
    const y = originXY[1] + Math.sin(ph)*Math.sin(th)*rr;
    const z = Math.max(groundZ(x,y), Math.cos(ph)*rr*0.55 + 3.0);
    if(x<SITE.x0-20||x>SITE.x1+20||y<SITE.y0-20||y>SITE.y1+20) continue;
    pts.add(x, y, z, 22 + hash(i*8.8)*18, 0.30, 0.5 + hash(i*2.2)*0.5, 1);
  }
}
