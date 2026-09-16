/* ===========================================================================
   AN1 — TIMELINE
   ONE continuous camera journey. There is no cut anywhere in this file.
   Camera position and target are sampled from a single smoothed track that
   runs from t = 0 to t = DURATION; the only override is the soldier-follow
   during the walk, and that is cross-faded in and out so the track never
   jumps. Every effect is a pure function of t, so the scrub bar lands on
   exactly the frame that plays.
   =========================================================================== */

/* ---- the soldier's route ---------------------------------------------- */
/* Both endpoints are real: D1 on the sentry post's east face (master A.4.8)
   and the 1000 x 2100 entry door at grade in the stairwell headwall at
   X 9250 (master A.4.7). The ground between them is open plot, so the route
   is this animation's own [V] choice - declared in the design basis - and
   the PACE is then derived from it, not assumed.                           */
const WALK = (function(){
  const S = PROJ.sentry.site;
  const ex = (S.x1)*MM, cy = (S.y0+S.y1)*0.5*MM;
  const pts = [
    V3.c(ex+0.90, cy,     0), V3.c(ex+2.60, cy+3.10, 0), V3.c(ex+0.20, cy+6.70, 0),
    V3.c(29.50,  11.60,   0), V3.c(21.50,  12.20, 0), V3.c(15.00,  11.40, 0),
    V3.c(11.40,   9.60,   0), V3.c(10.00,   7.60, 0), V3.c( 9.78,   6.78, 0)
  ];
  let len = 0;
  for(let i=0;i<pts.length-1;i++) len += Math.hypot(pts[i+1][0]-pts[i][0], pts[i+1][1]-pts[i][1]);
  return { pts, len, pace: len / PROJ.narrative.steps };
})();
PROJ.narrative.walkLen = Math.round(WALK.len*1000);
PROJ.narrative.pace    = Math.round(WALK.pace*1000);

/* The heading must be taken from a WINDOW of the route, not from the current
   segment. Segment direction changes in one step at every waypoint, and the
   follow camera sits 4.2 m behind and 1.5 m to the side of it, so a corner
   used to teleport the camera several metres between frames - a cut, and the
   one thing this animation may not contain. Measured before the fix: a peak
   camera speed of 138 m/s at t = 43.1 s. Sampling ahead and behind turns each
   corner into a three-metre arc, and taking the heading as a VECTOR rather
   than an angle also removes the atan2 wrap. */
const HEAD_WIN = 1.5;                                   // metres each side
function headingAt(d){
  const a = walkAt(Math.min(d + HEAD_WIN, WALK.len)).p;
  const b = walkAt(Math.max(d - HEAD_WIN, 0)).p;
  const v = V3.c(a[0]-b[0], a[1]-b[1], 0);
  return V3.len(v) < 1e-5 ? V3.c(1,0,0) : V3.norm(v);
}

/* position and heading at a distance d along the route */
function walkAt(d){
  d = clamp(d, 0, WALK.len);
  let acc = 0;
  for(let i=0;i<WALK.pts.length-1;i++){
    const a = WALK.pts[i], b = WALK.pts[i+1];
    const seg = Math.hypot(b[0]-a[0], b[1]-a[1]);
    if(acc + seg >= d || i === WALK.pts.length-2){
      const f = clamp((d-acc)/(seg||1), 0, 1);
      const x = lerp(a[0],b[0],f), y = lerp(a[1],b[1],f);
      return { p: V3.c(x, y, groundZ(x,y)), yaw: Math.atan2(b[1]-a[1], b[0]-a[0]) };
    }
    acc += seg;
  }
  const e = WALK.pts[WALK.pts.length-1];
  return { p: V3.c(e[0],e[1],groundZ(e[0],e[1])), yaw: Math.PI };
}

/* ---- beat table -------------------------------------------------------- */
/* Times are seconds. Each beat's end IS the next beat's start; there is no
   gap and no overlap, which is what makes the journey continuous.          */
const BEATS = [
  ['SITE',              0,   20, 'The plot, the berm, the stand-off'],
  ['SENTRY POST',      20,   36, 'The exposed outer element'],
  ['56 STEPS',         36,   85, 'The walk to the entry'],
  ['BLAST',            85,  100, 'Design basis threat'],
  ['BLAST WAVE',      100,  117, 'Source to project'],
  ['STAND-OFF',       117,  129, 'Expendability by design'],
  ['CUTAWAY',         129,  147, 'Into the ground'],
  ['ENGINEERED COVER',147,  162, 'Six layers, 2 000'],
  ['LOAD PATH',       162,  187, 'Slab to wall to mat to rock'],
  ['PROTECTED VOLUME',187,  199, 'Bays 1 to 6'],
  ['INTERIOR',        199,  216, 'Through the boundary'],
  ['OCCUPANTS',       216,  231, 'Nine, at work'],
  ['CBRN AIRFLOW',    231,  257, 'Intake to filtration to envelope'],
  ['CLOSED MODE',     257,  270, 'Sealed'],
  ['ESSENTIAL POWER', 270,  287, 'GEN-1 and the essential board'],
  ['SANITATION',      287,  298, 'Nothing is discharged'],
  ['EMP',             298,  314, 'A field, not an explosion'],
  ['EMP ZONE 2',      314,  330, '80 dB, standing alone'],
  ['INTEGRATION',     330,  342, 'Continuity of operations'],
  ['RETURN',          342,  360, 'Back to the surface'],
  ['SITE, AFTER',     360,  382, 'The project, whole']
];
const DURATION = BEATS[BEATS.length-1][2];
const beatAt = t => { for(const b of BEATS) if(t >= b[1] && t < b[2]) return b; return BEATS[BEATS.length-1]; };

/* ---- camera keys ------------------------------------------------------- */
/* pos and tgt in scene metres. Deliberately dense through the transitions
   so the smoothing pass has real curvature to work with.                   */
const CAM = [
  /* SITE — a high oblique that establishes terrain, berm, headhouse, entry
     and the sentry post in one frame, then descends                        */
  [  0, [ -26,  -46,  42], [ 14,   3,  -1]],
  [  7, [  -8,  -40,  31], [ 15,   3,  -1]],
  [ 14, [  14,  -34,  20], [ 22,   3,   0]],
  /* SENTRY POST — the camera comes down to standing height beside it       */
  [ 20, [  28,  -22,  12], [ 33,   3,   2]],
  [ 27, [  40,  -11,   5.4],[ 35,   3,   3]],
  [ 33, [  42.5,  1.5,  2.6],[ 36,   3.1, 2.0]],
  [ 36, [  41.0,  3.0,  2.1],[ 37.2, 3.1, 1.2]],
  /* 56 STEPS — procedural follow takes over here; these keys only have to
     put the track in the right neighbourhood for the cross-fade            */
  [ 60, [  24.0, 16.0,  3.4],[ 22.0,11.5, 1.0]],
  [ 85, [   7.0, 10.6,  2.6],[ 10.0, 7.2, 1.0]],
  /* BLAST — the camera turns to the burst on the east-south-east horizon   */
  [ 90, [   6.4,  9.8,  2.9],[ 26.0,-6.0, 3.6]],
  [ 96, [   6.0,  8.6,  4.6],[ 34.0,-9.0, 4.4]],
  [100, [   5.0,  4.0,  9.0],[ 30.0,-6.0, 4.0]],
  /* BLAST WAVE — rise and pull back so source, wave and project are one
     frame. This is the shot that makes the stand-off legible.              */
  [108, [  -3.0, -14.0, 20.0],[ 24.0, 2.0, 2.0]],
  [117, [  -1.0, -20.0, 17.0],[ 30.0, 3.0, 3.0]],
  /* STAND-OFF — hold on the post as the environment overwhelms it          */
  [123, [  20.0, -17.0, 11.0],[ 34.0, 3.0, 3.4]],
  [129, [  16.0, -14.0,  8.0],[ 20.0, 3.0, 0.5]],
  /* CUTAWAY — follow the pressure to the berm and descend through it       */
  [136, [   6.0, -12.0,  6.0],[ 11.0, 3.0,-1.5]],
  [142, [   2.0, -11.0,  1.6],[ 10.0, 3.0,-3.0]],
  [147, [   0.5, -12.6,  1.0],[ 7.0, 3.0,-2.6]],
  /* ENGINEERED COVER — a slow lateral dolly across the six layers          */
  [153, [   3.0,  -8.6,  1.1],[ 4.2, 0.7,-0.95]],
  [162, [   9.6,  -8.4,  1.0],[10.8, 0.7,-1.10]],
  /* LOAD PATH — pull back to hold the whole section, then track down it    */
  [170, [   6.0, -17.5,  0.6],[ 8.0, 1.5,-3.2]],
  [178, [   4.5, -16.5, -1.6],[ 6.0, 1.5,-4.2]],
  [187, [   8.0, -15.0, -3.4],[ 9.0, 1.5,-5.4]],
  /* PROTECTED VOLUME — the envelope, seen whole from outside the section   */
  [193, [   5.0, -16.0, -2.0],[ 9.0, 1.5,-4.2]],
  [199, [   1.0, -10.0, -3.4],[ 6.0, 2.0,-4.5]],
  /* INTERIOR — through the cut face and level out in the ops room.
     FROM HERE TO THE END OF THE BOX, EVERY SIGHT LINE AND EVERY TRAVERSE IS
     ROUTED THROUGH A REAL OPENING. The W8 partitions carry a 900 door gap at
     Y 2500-3400 (master A.3), so longitudinal travel and longitudinal views
     both run on Y ~ 2.90; W6 and W7 carry the blast doors at Y 600-1800
     (A.4.9), so the traverse into bay 8 drops to Y ~ 1.3 to pass through
     them. A camera that sights a partition instead of its doorway just
     renders a grey wall, which is what the first cut of this sequence did. */
  [205, [   3.6,  -3.40, -4.20],[  6.6, 2.60,-4.70]],
  [211, [   5.35,  1.90, -4.28],[  8.0, 2.55,-4.82]],
  [216, [   5.80,  3.05, -4.42],[  8.6, 2.25,-4.88]],
  /* OCCUPANTS — the consoles, then the plotting table, then east           */
  [221, [   6.45,  3.45, -4.40],[  9.0, 2.15,-4.92]],
  [226, [   7.55,  3.15, -4.45],[ 10.4, 2.92,-4.95]],
  [231, [   9.50,  2.95, -4.55],[ 11.6, 2.92,-4.90]],
  /* CBRN AIRFLOW — west to the intake down the axis, then follow the air   */
  [237, [   6.0,   2.92, -4.00],[  1.6, 2.90,-4.20]],
  [243, [   2.25,  2.90, -4.28],[  5.8, 2.75,-4.72]],
  [250, [   8.0,   2.92, -4.45],[ 11.2, 2.70,-4.85]],
  [257, [  10.5,   2.92, -4.50],[ 12.2, 2.40,-4.90]],
  /* CLOSED MODE — bay 5 is 1560 clear and the trains leave 110 mm a side,
     so it is read from the bay 4 doorway. There is nowhere to stand in it,
     and that is the point HV-F3 makes.                                     */
  [264, [  10.7,   2.85, -4.40],[ 11.9, 2.30,-4.90]],
  [270, [  11.0,   2.60, -4.35],[ 12.4, 2.10,-4.85]],
  /* ESSENTIAL POWER — east through BLAST DOOR 1, the stair well, BLAST
     DOOR 2, into bay 8                                                     */
  [277, [  14.0,   1.60, -4.80],[ 16.6, 1.25,-5.05]],
  [283, [  16.6,   1.25, -4.85],[ 19.4, 1.35,-5.05]],
  [287, [  19.4,   1.90, -4.70],[ 20.6, 2.60,-5.05]],
  /* SANITATION — back west through both blast doors, then up on to the
     door line and into bay 2                                               */
  [291, [  17.0,   1.30, -4.85],[ 14.2, 1.40,-5.00]],
  [294, [  13.2,   2.10, -4.75],[ 10.6, 2.70,-4.95]],
  [296, [   5.9,   2.90, -4.62],[  4.9, 2.60,-4.95]],
  [298, [   4.95,  2.55, -4.68],[  4.45,1.30,-5.18]],
  /* EMP — out through the cut to watch the field arrive, still continuous  */
  [304, [   3.4,  -6.0,  -1.60],[  7.0, 2.60,-3.20]],
  [309, [   4.0, -11.0,   3.40],[ 12.0, 3.00,-1.00]],
  [314, [   4.6,  -8.0,  -1.20],[  7.2, 3.00,-3.60]],
  /* ZONE 2 — down on to the welded steel enclosure in bay 3                */
  [321, [   5.2,  -1.40, -4.00],[  6.6, 3.90,-5.00]],
  [330, [   6.6,   1.30, -4.50],[  6.7, 4.30,-5.20]],
  /* INTEGRATION — the long axial view down the whole envelope, straight
     through every doorway, with everything running                         */
  [336, [   8.6,   2.87, -4.40],[  4.5, 2.90,-4.85]],
  [342, [  10.8,   2.90, -4.35],[  4.0, 2.90,-4.85]],
  /* RETURN — reverse the journey: roof, cover, berm, surface               */
  [348, [  12.0,  -6.0, -3.2],[  8.0,3.0,-4.0]],
  [354, [  10.0, -13.0,  1.0],[  9.0,3.0,-2.0]],
  [360, [   6.0, -21.0,  9.0],[ 12.0,3.0,-0.5]],
  /* SITE, AFTER — the hero three-quarter, matching the Revit side profile  */
  [368, [  -6.0, -31.0, 17.0],[ 16.0,3.0, 0.0]],
  [375, [ -18.0, -40.0, 25.0],[ 18.0,3.0, 0.0]],
  [382, [ -30.0, -52.0, 34.0],[ 18.0,3.0, 0.0]]
];

/* ---- build one smoothed, continuously-moving track --------------------- */
/* Linear resample at 30 Hz, then repeated binomial smoothing. This gives
   continuous velocity (no stop-start at keys) and cannot overshoot, which
   a Catmull-Rom through the same keys would. */
const TRACK = (function(){
  const HZ = 30, n = Math.ceil(DURATION*HZ)+1;
  const pos = new Array(n), tgt = new Array(n);
  for(let i=0;i<n;i++){
    const t = i/HZ;
    let k = 0;
    while(k < CAM.length-2 && CAM[k+1][0] <= t) k++;
    const a = CAM[k], b = CAM[Math.min(k+1, CAM.length-1)];
    const f = easeCam(clamp(invLerp(a[0], b[0], t), 0, 1));
    pos[i] = V3.lerp(V3.c(...a[1]), V3.c(...b[1]), f);
    tgt[i] = V3.lerp(V3.c(...a[2]), V3.c(...b[2]), f);
  }
  const smooth = arr => {
    for(let pass=0; pass<26; pass++){
      const o = arr.map(v=>V3.c(v[0],v[1],v[2]));
      for(let i=1;i<arr.length-1;i++)
        arr[i] = V3.add(V3.mul(o[i],0.5), V3.mul(V3.add(o[i-1],o[i+1]),0.25));
    }
  };
  smooth(pos); smooth(tgt);
  return { HZ, n, pos, tgt };
})();
function trackAt(t){
  const x = clamp(t,0,DURATION)*TRACK.HZ, i = Math.min(Math.floor(x), TRACK.n-2), f = x-i;
  return { pos: V3.lerp(TRACK.pos[i], TRACK.pos[i+1], f),
           tgt: V3.lerp(TRACK.tgt[i], TRACK.tgt[i+1], f) };
}

/* ---- the walk ---------------------------------------------------------- */
const WALK_T0 = 39.0;                                   // first footfall
const CADENCE = 0.75;                                   // s per footfall  [V]
const WALK_T1 = WALK_T0 + PROJ.narrative.steps*CADENCE; // 39 + 42.0 = 81.0
function walkState(t){
  const raw = (t - WALK_T0)/CADENCE;
  const stepF = clamp(raw, 0, PROJ.narrative.steps);
  const step  = Math.min(Math.floor(stepF)+ (raw>0?1:0), PROJ.narrative.steps);
  const d     = clamp(stepF,0,PROJ.narrative.steps) * WALK.pace;
  const w     = walkAt(d);
  const h     = headingAt(d);
  /* the swing phase that puts a foot down on every whole step */
  const ph    = (stepF - Math.floor(stepF)) * Math.PI * 2;
  const moving = t > WALK_T0-1.2 && t < WALK_T1+0.35;
  return { p:w.p, yaw:Math.atan2(h[1],h[0]), dir:h, step, stepF,
           swing: moving ? ph : 0, moving, done: t >= WALK_T1 };
}

/* ---- the whole animation state at time t ------------------------------- */
function stateAt(t){
  const s = {};
  const tk = trackAt(t);
  s.pos = tk.pos; s.tgt = tk.tgt;
  /* 47 degrees outside; the box is 5 000 clear and 3 200 high, and a normal
     lens in a room that size sees a wall. The interior beats open up to 64
     degrees and ease back on the way out. */
  const wide = smoothstep(203, 213, t) * (1 - smoothstep(340, 350, t));
  s.fov = lerp(47, 64, wide) * Math.PI/180;

  /* --- soldier follow, cross-faded so the track never jumps ------------ */
  const wk = walkState(t);
  s.walk = wk;
  s.soldierVisible = t < 132;                 /* he goes inside; he is not
                                                 shown in the blast environment */
  const blend = smoothstep(36.0, 40.5, t) * (1 - smoothstep(80.0, 85.5, t));
  if(blend > 0.001){
    const back = 4.2, side = 1.5, up = 1.95;
    const fx = wk.dir[0], fy = wk.dir[1];
    const follow = V3.c(wk.p[0] - fx*back - fy*side,
                        wk.p[1] - fy*back + fx*side,
                        wk.p[2] + up + Math.sin(wk.stepF*Math.PI)*0.012);
    const look = V3.c(wk.p[0] + fx*1.6, wk.p[1] + fy*1.6, wk.p[2] + 1.15);
    s.pos = V3.lerp(s.pos, follow, blend);
    s.tgt = V3.lerp(s.tgt, look,   blend);
  }

  /* --- the blast ------------------------------------------------------- */
  /* front position sweeps the plot. Travel is SLOWED FOR LEGIBILITY and
     the animation says so; no velocity or arrival time is implied.        */
  const T_FLASH = 92.0;
  s.flash = t < T_FLASH ? 0 : Math.exp(-(t-T_FLASH)*2.6) * smoothstep(T_FLASH, T_FLASH+0.12, t);
  s.fireball = clamp(smoothstep(T_FLASH, T_FLASH+0.25, t) * (1-smoothstep(T_FLASH+3.0, T_FLASH+11.0, t)), 0, 1);
  s.burstDir = V3.mul(BLAST_DIR, -1);
  const sweep = invLerp(97.0, 128.0, t);
  s.front   = t < 97 ? -1e9 : lerp(-78, 52, clamp(sweep,0,1.35));
  s.frontOn = t > 96.5 && t < 150;
  /* wind shear on the grass: builds as the front passes, then decays       */
  const dFront = s.front - frontCoord(11, 3.1);
  s.wind = clamp(Math.exp(-Math.abs(dFront)/22) * smoothstep(97, 101, t), 0, 1) * 1.0;
  s.sentryHit = s.front > FC_SENTRY;
  s.sentryDamage = clamp(invLerp(FC_SENTRY, FC_SENTRY+11, s.front), 0, 1);
  /* dust peaks with the event, then settles to a residual haze that clears
     over the closing minute - brief section 33, "dust settles" */
  const dustPeak  = smoothstep(104, 116, t) * (1 - smoothstep(128, 172, t));
  const dustResid = smoothstep(120, 140, t) * (1 - smoothstep(338, 378, t)*0.80) * 0.22;
  s.dust = clamp(dustPeak + dustResid, 0, 1);

  /* --- ground transparency, then the engineering section ---------------
     ONE section, opened once and closed once. The plane sits at Y = 0.620,
     the inner face of the 600 south perimeter wall, so the cut removes the
     ground and that one wall and leaves everything else standing: bays,
     north wall, roof slab and mat all read in true section, exactly as
     A-203 SECTION XX draws them. The camera then flies INSIDE the same
     section rather than needing a second model.                          */
  s.ghost = smoothstep(130, 139, t) * (1 - smoothstep(143, 152, t))
          + smoothstep(344, 350, t) * (1 - smoothstep(354, 360, t));
  const SECT_OFF = -35.0, SECT_ON = 0.620;
  s.clipY = lerp(SECT_OFF, SECT_ON, smoothstep(134, 149, t));
  s.clipY = lerp(s.clipY, SECT_OFF, smoothstep(346, 358, t));
  s.clip  = 1;

  /* --- load path ------------------------------------------------------- */
  /* six stages, revealed in order, each held while the next arrives       */
  s.arrowStage = [];
  const stageT = [[165,172],[169,176],[173,180],[177,184],[180,188],[183,191]];
  for(let i=0;i<6;i++){
    const [a,b] = stageT[i];
    s.arrowStage[i] = smoothstep(a, a+2.2, t) * (1 - smoothstep(196, 201, t));
  }
  s.pressureOnRoof = smoothstep(163, 168, t) * (1 - smoothstep(196, 200, t));

  /* --- highlights ------------------------------------------------------ */
  s.envelope = smoothstep(188, 192, t) * (1 - smoothstep(203, 208, t));
  s.zone2Hi  = smoothstep(319, 323, t) * (1 - smoothstep(338, 344, t));

  /* --- interior -------------------------------------------------------- */
  s.interiorLit = smoothstep(196, 206, t);
  /* the shock, felt inside: a slight vibration and a brief light dip.
     No panic, no falling objects, no casualties (brief section 17).       */
  const shockT = 219.0;
  s.shake = t > shockT && t < shockT+3.4
          ? Math.exp(-(t-shockT)*1.5) * Math.sin((t-shockT)*46) * 0.020 : 0;
  s.lightDip = t > shockT && t < shockT+2.6
          ? Math.exp(-(t-shockT)*2.2) * 0.38 : 0;

  /* --- CBRN ------------------------------------------------------------ */
  s.airOn   = smoothstep(233, 238, t) * (1 - smoothstep(288, 294, t));
  s.airHead = clamp(invLerp(236, 256, t), 0, 1);
  s.contaminated = t < 268;
  s.closedMode   = t > 258;
  s.valvesShut   = smoothstep(258, 262, t);

  /* --- power ----------------------------------------------------------- */
  s.powerOn = smoothstep(272, 277, t) * (1 - smoothstep(292, 297, t));

  /* --- EMP ------------------------------------------------------------- */
  const T_EMP = 302.0;
  s.empOn  = t > T_EMP && t < 336;
  s.empR   = s.empOn ? (t - T_EMP) * 26.0 : -1;
  s.empWash= t > T_EMP && t < T_EMP+7
           ? Math.exp(-(t-T_EMP-0.6)*0.8) * 0.5 * smoothstep(T_EMP, T_EMP+0.4, t) : 0;
  s.zoneReveal = [ smoothstep(304,307,t)*(1-smoothstep(316,320,t)),
                   smoothstep(309,312,t)*(1-smoothstep(320,324,t)),
                   smoothstep(318,321,t)*(1-smoothstep(338,343,t)) ];

  /* --- overall --------------------------------------------------------- */
  s.fadeIn  = 1 - smoothstep(0, 2.2, t);
  s.fadeOut = smoothstep(DURATION-6.0, DURATION-0.4, t);
  s.beat = beatAt(t);
  return s;
}

/* ---- annotations -------------------------------------------------------
   Small, anchored, specific, and gone before they become a caption. Every
   figure below is printed somewhere in the master or the project flier;
   nothing here is rounded, recomputed or invented, and no value tagged
   [ASSUMED] is shown without saying so.
   ---------------------------------------------------------------------- */
const NOTE = (t0,t1,anchor,head,sub,cls) => ({t0,t1,anchor,head,sub,cls:cls||''});
const ANNOT = [
  /* staggered so no two are on screen together at the same screen position;
     the stairwell note has been moved to where the soldier actually reaches
     it, which is the moment it means something                             */
  NOTE(  4.0, 11.5, [11, 3.1, 0.4],   'UNDERGROUND CBRN-HARDENED OPERATIONS ROOM', 'Pune, Maharashtra'),
  NOTE( 12.5, 18.5, [ 6, 1.5, 0.1],   'ENGINEERED COVER', '2 000 layered, over a 900 pressure slab'),
  NOTE( 19.0, 25.5, [16, 3.1, 0.9],   'HEADHOUSE', 'Roof +0.900, no earth cover'),
  NOTE( 24.0, 30.0, [34, 3.1, 7.0],   'SENTRY POST', 'Two-storey RC frame - NOT blast designed'),
  NOTE( 28.5, 34.0, [34, 3.1, 0.45],  'STAND-OFF', '10.00 m to the box face - 9.00 m to the excavation'),
  NOTE( 31.0, 36.5, [34, 3.1,-1.7],   'FOOTINGS ON IN-SITU BASALT', 'F1 1500 x 1500 x 600 at (-)2.000'),
  NOTE( 72.0, 81.0, [10.4,6.75,2.0],  'COVERED ENTRY STAIRWELL', 'Declared expendable'),

  NOTE( 88,  97, [30,-9.0, 6.0],   'DESIGN BASIS THREAT', 'Nuclear air-blast - p so 344.7 kPa (50 psi)'),
  NOTE( 99, 110, [22, 0.0, 5.0],   'BLAST FRONT', 'Travel slowed for legibility'),
  NOTE(120, 129, [34, 3.1, 4.0],   'EXPENDABLE OUTER ELEMENT', 'Stand-off is the protection, not the post'),

  /* the six layers are named ONE AT A TIME, top to bottom, each held about
     three seconds with a short handover - six labels on screen together is
     a caption, which is exactly what the brief forbids                     */
  NOTE(149.0,152.2, [ 3.0, 0.62,-0.15],'TOPSOIL / TURF  300', 'Concealment, erosion, sheds rain'),
  NOTE(151.8,155.0, [ 4.4, 0.62,-0.38],'GRANULAR FILTER  150', 'Stops fines clogging'),
  NOTE(154.6,157.8, [ 6.0, 0.62,-0.60],'RC BURSTER SLAB M30  200', 'Breaks up a penetrating item - laid to a 1:50 crossfall'),
  NOTE(157.4,160.6, [ 7.6, 0.62,-0.95],'CRUSHED BASALT RUBBLE  500', 'Scatters burster energy'),
  NOTE(160.2,163.4, [ 9.2, 0.62,-1.58],'COMPACTED FILL 95% MDD  750', 'Radiation mass - the second metre buys neutron and gamma'),
  NOTE(163.0,166.2, [10.6, 0.62,-1.95],'PROTECTION SCREED  100', '2 000 total - 40.65 kPa'),

  NOTE(164, 174, [ 6.0, 1.0, 1.6], 'DESIGN BLAST PRESSURE  383 kPa', '344.7 x DLF 1.111 - roof AND walls'),
  NOTE(170, 179, [ 4.0, 1.0,-2.45],'PRESSURE SLAB  900', 'The governing element'),
  NOTE(174, 183, [ 0.3, 1.0,-4.50],'RC WALL  600', 'Blast 383 kPa acting on either face'),
  NOTE(178, 187, [ 4.0, 1.4,-6.40],'MAT  600', 'Hydrostatic uplift 46.11 kPa, compensated'),
  NOTE(182, 191, [ 7.0, 1.4,-7.30],'FOUNDING STRATUM', 'Deccan basalt - rockhead ASSUMED, not proved'),
  NOTE(180, 189, [ 5.0,-1.6,-5.10],'EARTH + WATER  83.2 kPa', 'At floor level - two-thirds of it is water'),

  NOTE(189, 199, [ 6.5, 3.0,-4.4], 'GAS-TIGHT ENVELOPE - BAYS 1 to 6', '67.80 m2 - 216.96 m3'),
  NOTE(193, 201, [14.8, 1.2,-5.0], 'BLAST DOOR 1', '1200 x 2100 - >= 7 bar - the protective boundary'),
  NOTE(208, 216, [ 8.0, 3.0,-4.9], 'OPS ROOM - BAY 3', 'Internal clear height 3 200'),
  NOTE(219, 229, [10.2, 2.0,-4.9], 'NINE OCCUPANTS - 96 HOURS', 'The external event, felt as a tremor'),

  NOTE(236, 245, [-1.2, 2.2, 1.2], 'AIR INTAKE', 'Blast valve at the boundary - all five shut at the shock'),
  NOTE(244, 254, [11.9, 2.4,-4.3], 'CBRN FILTRATION  2 x 300 m3/h', 'HEPA H14 + activated carbon - true N+1'),
  NOTE(250, 258, [ 6.0, 3.6,-4.3], 'ENVELOPE HELD AT +50 to +100 Pa', 'Clean air, outward leakage'),
  NOTE(260, 269, [12.0, 2.0,-4.4], 'CBRN CLOSED MODE', '48 h - the limit is the soda lime, not the power'),

  NOTE(275, 285, [19.9, 1.8,-5.1], 'GEN-1  15 kVA  BAY 8', '7.360 kVA connected - 49 %'),
  NOTE(280, 289, [19.9, 3.4,-4.6], 'ESSENTIAL LOAD  1.283 kW', 'Battery 149 Ah, 48 V'),
  NOTE(292, 299, [ 4.45,1.3,-5.2], 'SN-03 SEALED-CASSETTE CHEMICAL TOILET', 'NO DISCHARGE in protective mode'),

  NOTE(303, 311, [12.0, 3.0, 6.0], 'EMP ZONE 0', 'Everything above grade - no attenuation credited'),
  NOTE(309, 318, [ 9.0, 3.0,-2.4], 'EMP ZONE 1 - THE BURIED BOX', 'A genuine low-frequency measure. Not a MIL-STD boundary'),
  NOTE(320, 333, [ 6.7, 5.0,-3.9], 'EMP ZONE 2  -  80 dB', 'Welded steel enclosure, bay 3. Designed standing alone'),
  NOTE(334, 343, [ 8.0, 3.0,-4.6], 'CONTINUITY OF OPERATIONS', 'Structure + air + power + sanitation + EMP'),

  NOTE(366, 378, [14.0, 3.1, 1.0], '22.0 x 6.2 m EXTERNAL - 8 BAYS', 'Roof 900 - mat 600 - walls 600'),
  NOTE(371, 381, [11.0, 3.1,-0.2], 'NINE PEOPLE. NINETY-SIX HOURS. TWO METRES OF EARTH.', '')
];

/* the one standing caveat, shown while the blast is on screen. It is on
   the project's own flier and it belongs on any animation of this threat. */
const CAVEAT = { t0: 86, t1: 131, text: PROJ.blast.caveat };
