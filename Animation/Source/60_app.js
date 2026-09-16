/* ===========================================================================
   AN1 — APPLICATION
   Render loop, annotation projection, and the presenter's controls.
   =========================================================================== */

let PROG, PROG_PT, PROG_FULL, AIRPATH = null;
let MESH = {}, PTS = {}, SND = new Sound();
let T = 0, PLAYING = false, LAST = 0, SPEED = 1, UIHIDDEN = false;
/* Adaptive render scale. The scene is small (about 112 000 triangles) but a
   presentation laptop may have no usable GPU at all, and a smooth 6 minutes
   at three-quarter resolution beats a stuttering one at full. The scale
   settles within a second or two and is quantised so the change is not
   visible as a continuous crawl. Press Q to override. */
const SCALES = [1.0, 0.85, 0.7, 0.6, 0.5, 0.4];
let scaleIx = 0, scaleAuto = true, frameAvg = 16.7;
let lastStepPlayed = -1;

/* lighting: one low sun from the west-south-west and a hemisphere ambient.
   Restrained, overcast-clear, no lens flare and no golden-hour theatrics. */
const SUN  = V3.norm(V3.c(-0.42, -0.30, 0.68));
const SKY  = V3.c(0.300, 0.330, 0.375);
const GND  = V3.c(0.150, 0.132, 0.112);
const FOGC = V3.c(0.480, 0.545, 0.650);   // linear; gammas to a light haze
const SKY_HI = V3.c(0.560, 0.625, 0.710), SKY_LO = V3.c(0.760, 0.775, 0.780);

function initGL(){
  canvas = document.getElementById('c');
  gl = canvas.getContext('webgl2', {antialias:true, alpha:false, powerPreference:'high-performance'});
  if(!gl){ document.getElementById('err').style.display='block'; return false; }
  PROG      = compile(VS_SURF, FS_SURF);
  PROG_PT   = compile(VS_PT,   FS_PT);
  PROG_FULL = compile(VS_FULL, FS_FULL);
  gl.enable(gl.DEPTH_TEST);
  gl.enable(gl.CULL_FACE);
  gl.cullFace(gl.BACK);
  return true;
}

function buildAll(){
  MESH.terrain   = buildTerrain();
  MESH.berm      = buildBerm();
  MESH.strata    = buildStrata();
  MESH.backfill  = buildBackfill();
  MESH.cover     = buildCover();
  MESH.box       = buildBox();
  MESH.shafts    = buildShafts();
  MESH.stairs    = buildStairs();
  MESH.headhouse = buildHeadhouse();
  MESH.entry     = buildEntry();
  MESH.sentry    = buildSentry();
  MESH.fitout    = buildFitout();
  MESH.grass     = buildGrass();
  MESH.arrow     = buildArrow();
  MESH.envelope  = buildEnvelope();
  MESH.zone2     = buildZone2Hi();
  MESH.torso     = figureTorso(1);
  MESH.seated    = figureSeated(1);
  MESH.leg       = figureLeg(1);
  MESH.arm       = figureArm(1);
  PTS.dust = new Points(3200);
  PTS.air  = new Points(600);
  PTS.emp  = new Points(1800);
  PTS.fire = new Points(64);
  STATIONS = occupantStations();
}
let STATIONS = [];

/* ---- draw helpers ------------------------------------------------------ */
function setSurfCommon(VP, eye, s){
  gl.useProgram(PROG);
  gl.uniformMatrix4fv(PROG.u.uVP, false, VP);
  gl.uniform3fv(PROG.u.uSun, SUN);
  gl.uniform3fv(PROG.u.uEye, eye);
  const dip = 1 - (s.lightDip||0)*0.55;
  gl.uniform3f(PROG.u.uSky, SKY[0]*dip, SKY[1]*dip, SKY[2]*dip);
  gl.uniform3fv(PROG.u.uGnd, GND);
  gl.uniform3fv(PROG.u.uFogCol, FOGC);
  gl.uniform1f(PROG.u.uFog, 0.0050);
  gl.uniform3f(PROG.u.uTintCol, 0.55, 0.62, 0.78);
  gl.uniform1f(PROG.u.uTint, 0);
  gl.uniform1f(PROG.u.uGhost, 0);
  gl.uniform1f(PROG.u.uAlpha, 1);
  /* `discard` defeats early-Z, so the clip branch is only switched on while
     the section is actually open - which is most of the middle of the film
     and none of the opening or the hero shot */
  gl.uniform1f(PROG.u.uClipOn, s.clipY > SITE.y0 ? 1 : 0);
  /* section: discard everything south of clipY. Second plane parked. */
  gl.uniform4f(PROG.u.uClipA, 0, -1, 0, s.clipY);
  gl.uniform4f(PROG.u.uClipB, 0, 0, 0, -1e9);
}
function drawMesh(m, M, alpha, ghost, tint){
  if(!m) return;
  gl.uniformMatrix4fv(PROG.u.uM, false, M || M4.ident());
  gl.uniform1f(PROG.u.uAlpha, alpha===undefined?1:alpha);
  gl.uniform1f(PROG.u.uGhost, ghost?1:0);
  gl.uniform1f(PROG.u.uTint, tint||0);
  m.draw();
}

/* a standing or seated figure, with the leg rig */
function drawFigure(p, yaw, seated, swing, scale){
  const sc = scale||1;
  const base = M4.mul(M4.trans(p), M4.rotZ(yaw));
  if(seated){ drawMesh(MESH.seated, base); return; }
  drawMesh(MESH.torso, base);
  const hipZ = 0.90*sc, shZ = 1.33*sc;
  for(const side of [-1, 1]){
    const a = swing ? Math.sin(swing + (side>0?0:Math.PI)) * 0.42 : 0;
    const hip = M4.mul(M4.mul(base, M4.trans(V3.c(0, side*0.095*sc, hipZ))), M4.rotY(-a));
    drawMesh(MESH.leg, hip);
    const sh = M4.mul(M4.mul(base, M4.trans(V3.c(0, side*0.215*sc, shZ))), M4.rotY(a*0.75));
    drawMesh(MESH.arm, sh);
  }
}

/* ---- frame ------------------------------------------------------------- */
function frame(now){
  requestAnimationFrame(frame);
  const dt = LAST ? Math.min((now-LAST)/1000, 0.1) : 0;
  LAST = now;
  if(PLAYING){
    T += dt*SPEED;
    if(T >= DURATION){ T = DURATION; PLAYING = false; setPlayIcon(); }
  }
  const s = stateAt(T);

  /* resize, with the adaptive scale applied */
  if(dt > 0) frameAvg = frameAvg*0.9 + dt*1000*0.1;
  if(scaleAuto && PLAYING){
    if(frameAvg > 34 && scaleIx < SCALES.length-1){ scaleIx++; frameAvg = 16.7; }
    else if(frameAvg < 15 && scaleIx > 0){ scaleIx--; frameAvg = 24; }
  }
  const dpr = Math.min(window.devicePixelRatio||1, 2) * SCALES[scaleIx];
  const w = Math.max(2, Math.floor(canvas.clientWidth*dpr)),
        h = Math.max(2, Math.floor(canvas.clientHeight*dpr));
  if(canvas.width!==w || canvas.height!==h){ canvas.width=w; canvas.height=h; }
  gl.viewport(0,0,canvas.width,canvas.height);

  /* camera. The shake is the only non-smooth motion in the piece and it
     lasts 3.4 s; it is the shock felt inside, not a camera style.        */
  let eye = s.pos, tgt = s.tgt;
  if(s.shake){
    eye = V3.add(eye, V3.c(s.shake*0.6, s.shake*0.35, s.shake));
    tgt = V3.add(tgt, V3.c(0, 0, s.shake*0.5));
  }
  const asp = canvas.width/Math.max(canvas.height,1);
  const P = M4.persp(s.fov, asp, 0.08, 7000);
  const VP = M4.mul(P, M4.look(eye, tgt, V3.c(0,0,1)));

  /* --- sky ------------------------------------------------------------- */
  gl.depthMask(false); gl.disable(gl.DEPTH_TEST); gl.disable(gl.BLEND);
  gl.useProgram(PROG_FULL);
  gl.uniform1f(PROG_FULL.u.uGrad, 1);
  gl.uniform3fv(PROG_FULL.u.uCol,  SKY_HI);
  gl.uniform3fv(PROG_FULL.u.uCol2, SKY_LO);
  gl.uniform1f(PROG_FULL.u.uA, 1); gl.uniform1f(PROG_FULL.u.uVig, 0);
  gl.uniform1f(PROG_FULL.u.uScan, 0); gl.uniform1f(PROG_FULL.u.uTime, T);
  gl.drawArrays(gl.TRIANGLES,0,3);
  gl.enable(gl.DEPTH_TEST); gl.depthMask(true);
  gl.clear(gl.DEPTH_BUFFER_BIT);

  /* --- opaque fabric ---------------------------------------------------- */
  setSurfCommon(VP, eye, s);
  const gh = s.ghost > 0.02;
  drawMesh(MESH.strata);
  drawMesh(MESH.backfill);
  drawMesh(MESH.box);
  drawMesh(MESH.shafts);
  drawMesh(MESH.stairs);
  drawMesh(MESH.headhouse);
  drawMesh(MESH.entry);
  drawMesh(MESH.fitout);
  /* the sentry post. As the front passes it, it is drawn progressively
     lost in the blast environment - dimmed and dust-washed. No cracking,
     no collapse mechanics, no failure label (brief section 11).          */
  if(s.sentryDamage > 0){
    gl.uniform3f(PROG.u.uTintCol, 0.46, 0.43, 0.40);
    drawMesh(MESH.sentry, null, 1, false, s.sentryDamage*0.72);
    gl.uniform3f(PROG.u.uTintCol, 0.55, 0.62, 0.78);
  } else drawMesh(MESH.sentry);
  /* grass, bent whole-field by the blast wind */
  gl.disable(gl.CULL_FACE);
  drawMesh(MESH.grass, M4.shear(BLAST_DIR[0]*s.wind*0.85, BLAST_DIR[1]*s.wind*0.85));
  gl.enable(gl.CULL_FACE);

  /* ground and cover: ghosted through the transition, then sectioned */
  if(gh){
    gl.enable(gl.BLEND); gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);
    gl.depthMask(false);
    drawMesh(MESH.terrain, null, 1, true);
    drawMesh(MESH.berm,    null, 1, true);
    drawMesh(MESH.cover,   null, 1, true);
    gl.depthMask(true); gl.disable(gl.BLEND);
  } else {
    drawMesh(MESH.terrain);
    drawMesh(MESH.berm);
    drawMesh(MESH.cover);
  }

  /* --- figures ---------------------------------------------------------- */
  if(s.soldierVisible && (T > 18)){
    const wk = s.walk;
    drawFigure(wk.p, wk.yaw, false, wk.moving ? wk.swing : 0);
    /* footstep audio, forward play only */
    if(PLAYING && SPEED > 0 && wk.moving && wk.step !== lastStepPlayed && wk.step > 0){
      lastStepPlayed = wk.step; SND.step();
    }
    if(!wk.moving) lastStepPlayed = -1;
  }
  if(s.interiorLit > 0.05){
    for(const st of STATIONS){
      const idle = Math.sin(T*0.7 + st.p[0]*3.1)*0.03;
      drawFigure(V3.c(st.p[0], st.p[1], st.p[2]), st.yaw + idle, st.seated, 0);
    }
  }

  /* --- load path arrows -------------------------------------------------- */
  gl.enable(gl.BLEND); gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);
  gl.disable(gl.CULL_FACE);
  gl.uniform1f(PROG.u.uClipOn, 0);          // arrows are annotation, never sectioned
  const arrows = loadPathArrows();
  for(const a of arrows){
    const amt = s.arrowStage[a.stage];
    if(amt <= 0.02) continue;
    const grow = easeInOut(clamp(amt,0,1));
    drawMesh(MESH.arrow, M4.dirTo(a.from, a.dir, a.len*grow, 1.0), amt);
  }
  gl.enable(gl.CULL_FACE);
  gl.uniform1f(PROG.u.uClipOn, s.clipY > SITE.y0 ? 1 : 0);
  /* --- restrained BIM highlights ---------------------------------------- */
  gl.depthMask(false);
  if(s.envelope > 0.02) drawMesh(MESH.envelope, null, s.envelope*0.16);
  if(s.zone2Hi  > 0.02) drawMesh(MESH.zone2,    null, s.zone2Hi*0.22);
  gl.depthMask(true);
  gl.disable(gl.BLEND);

  /* --- particles --------------------------------------------------------- */
  gl.useProgram(PROG_PT);
  gl.uniformMatrix4fv(PROG_PT.u.uVP, false, VP);
  gl.uniform3fv(PROG_PT.u.uEye, eye);
  gl.uniform1f(PROG_PT.u.uPx, canvas.height*0.55);
  gl.enable(gl.BLEND); gl.depthMask(false);

  /* dust and the blast front */
  gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);
  PTS.dust.reset();
  if(s.frontOn) blastFront(PTS.dust, s.front, eye);
  if(s.dust > 0.01) settlingDust(PTS.dust, Math.max(T-104,0), s.dust, [16, 2, 0]);
  PTS.dust.flush();
  gl.uniform3f(PROG_PT.u.uCa, 0.415, 0.372, 0.320);
  gl.uniform3f(PROG_PT.u.uCb, 0.700, 0.672, 0.612);
  PTS.dust.draw();

  /* the fireball, additive, on the horizon */
  if(s.fireball > 0.01){
    gl.blendFunc(gl.SRC_ALPHA, gl.ONE);
    PTS.fire.reset();
    const R = PROJ.narrative.blastRange;
    const bx = 11 + s.burstDir[0]*R, by = 3.1 + s.burstDir[1]*R;
    for(let i=0;i<26;i++){
      const h = hash(i*3.3);
      PTS.fire.add(bx + (h-0.5)*120, by + (hash(i*7.1)-0.5)*120, 70 + h*150,
                   9000 + h*7000, s.fireball*(0.30+h*0.35), h, 0);
    }
    PTS.fire.flush();
    gl.uniform3f(PROG_PT.u.uCa, 1.00, 0.86, 0.58);
    gl.uniform3f(PROG_PT.u.uCb, 0.98, 0.46, 0.20);
    PTS.fire.draw();
  }

  /* CBRN airflow */
  if(s.airOn > 0.02){
    gl.blendFunc(gl.SRC_ALPHA, gl.ONE);
    PTS.air.reset();
    airflowParticles(PTS.air, AIRPATH, T, s.airHead, 210, s.contaminated);
    PTS.air.flush();
    gl.uniform3f(PROG_PT.u.uCa, 0.72, 0.50, 0.30);   // contaminated outside air
    gl.uniform3f(PROG_PT.u.uCb, 0.40, 0.78, 0.82);   // filtered, into the envelope
    PTS.air.draw();
  }

  /* EMP field */
  if(s.empOn && s.empR > 0){
    gl.blendFunc(gl.SRC_ALPHA, gl.ONE);
    PTS.emp.reset();
    empField(PTS.emp, T, [11, 3.1], s.empR);
    PTS.emp.flush();
    gl.uniform3f(PROG_PT.u.uCa, 0.38, 0.58, 0.86);
    gl.uniform3f(PROG_PT.u.uCb, 0.80, 0.86, 0.96);
    PTS.emp.draw();
  }
  gl.depthMask(true); gl.disable(gl.BLEND);

  /* --- overlay: flash, EMP wash, fades ----------------------------------- */
  const ov = [];
  if(s.flash    > 0.002) ov.push([[1,0.97,0.92], Math.min(s.flash*0.92,0.95), 0]);
  if(s.empWash  > 0.002) ov.push([[0.70,0.80,0.95], s.empWash*0.22, s.empWash]);
  if(s.fadeIn   > 0.002) ov.push([[0,0,0], s.fadeIn, 0]);
  if(s.fadeOut  > 0.002) ov.push([[0,0,0], s.fadeOut, 0]);
  if(ov.length){
    gl.disable(gl.DEPTH_TEST); gl.enable(gl.BLEND);
    gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);
    gl.useProgram(PROG_FULL);
    gl.uniform1f(PROG_FULL.u.uGrad, 0);
    gl.uniform1f(PROG_FULL.u.uVig, 0.55);
    gl.uniform1f(PROG_FULL.u.uTime, T);
    for(const [c,a,sc] of ov){
      gl.uniform3f(PROG_FULL.u.uCol, c[0],c[1],c[2]);
      gl.uniform1f(PROG_FULL.u.uA, a);
      gl.uniform1f(PROG_FULL.u.uScan, sc);
      gl.drawArrays(gl.TRIANGLES,0,3);
    }
    gl.disable(gl.BLEND); gl.enable(gl.DEPTH_TEST);
  }

  updateHUD(s, VP);
}
/* AIRPATH is resolved in start(), once PROJ and the bay table are live */

/* ---- annotations, projected from their 3D anchors ---------------------- */
const noteEls = [];
function buildNotes(){
  const layer = document.getElementById('notes');
  ANNOT.forEach((a,i)=>{
    const el = document.createElement('div');
    el.className = 'note';
    el.innerHTML = '<span class="lead"></span><b>'+a.head+'</b>'+(a.sub?'<i>'+a.sub+'</i>':'');
    layer.appendChild(el);
    noteEls.push(el);
  });
}
function project(p, VP, w, h){
  const x = p[0]*VP[0] + p[1]*VP[4] + p[2]*VP[8]  + VP[12];
  const y = p[0]*VP[1] + p[1]*VP[5] + p[2]*VP[9]  + VP[13];
  const z = p[0]*VP[2] + p[1]*VP[6] + p[2]*VP[10] + VP[14];
  const ww= p[0]*VP[3] + p[1]*VP[7] + p[2]*VP[11] + VP[15];
  if(ww <= 0.001) return null;
  return { x:(x/ww*0.5+0.5)*w, y:(1-(y/ww*0.5+0.5))*h, z:z/ww };
}
function updateHUD(s, VP){
  const w = canvas.clientWidth, h = canvas.clientHeight;
  ANNOT.forEach((a,i)=>{
    const el = noteEls[i];
    /* fade in as the camera approaches, hold, fade out - never freeze */
    const inA  = smoothstep(a.t0, a.t0+0.8, T);
    const outA = 1 - smoothstep(a.t1-0.9, a.t1, T);
    let vis = inA*outA;
    if(vis <= 0.01){ if(el.style.opacity!=='0'){ el.style.opacity='0'; el.style.visibility='hidden'; } return; }
    const q = project(V3.c(...a.anchor), VP, w, h);
    if(!q || q.z <= 0 || q.x<-260 || q.x>w+260 || q.y<-160 || q.y>h+160){
      el.style.opacity='0'; el.style.visibility='hidden'; return;
    }
    el.style.visibility='visible';
    el.style.opacity = (vis*(UIHIDDEN?1:1)).toFixed(3);
    el.style.transform = 'translate('+Math.round(clamp(q.x,8,w-8))+'px,'+Math.round(clamp(q.y,8,h-8))+'px)';
  });
  /* the standing caveat */
  const cav = document.getElementById('caveat');
  const cv = smoothstep(CAVEAT.t0, CAVEAT.t0+1, T) * (1-smoothstep(CAVEAT.t1-1.2, CAVEAT.t1, T));
  cav.style.opacity = cv.toFixed(3);
  /* transport */
  if(!UIHIDDEN){
    document.getElementById('bar').style.width = (T/DURATION*100).toFixed(2)+'%';
    document.getElementById('tc').textContent = fmt(T)+' / '+fmt(DURATION);
    const b = s.beat;
    document.getElementById('beat').textContent = b[0];
    document.getElementById('beatsub').textContent = b[3];
    document.getElementById('qual').textContent =
      (scaleAuto ? 'Auto ' : 'Fixed ') + Math.round(SCALES[scaleIx]*100) + '%';
  }
  SND.update(s, T, PLAYING);
}
const fmt = t => Math.floor(t/60)+':'+String(Math.floor(t%60)).padStart(2,'0');

/* ---- controls ---------------------------------------------------------- */
function setPlayIcon(){ document.getElementById('play').textContent = PLAYING ? '❚❚' : '▶'; }
function seek(t){ T = clamp(t, 0, DURATION); lastStepPlayed = -1; }
function wireUI(){
  document.getElementById('play').onclick = ()=>{ PLAYING=!PLAYING; setPlayIcon(); };
  const track = document.getElementById('track');
  const scrub = e =>{
    const r = track.getBoundingClientRect();
    seek(clamp((e.clientX-r.left)/r.width,0,1)*DURATION);
  };
  let dragging=false;
  track.addEventListener('pointerdown', e=>{ dragging=true; track.setPointerCapture(e.pointerId); scrub(e); });
  track.addEventListener('pointermove', e=>{ if(dragging) scrub(e); });
  track.addEventListener('pointerup',   e=>{ dragging=false; });
  /* chapter list */
  const ch = document.getElementById('chapters');
  BEATS.forEach(b=>{
    const d = document.createElement('button');
    d.textContent = b[0];
    d.title = b[3]+'  ·  '+fmt(b[1]);
    d.onclick = ()=>{ seek(b[1]); };
    ch.appendChild(d);
  });
  addEventListener('keydown', e=>{
    if(e.code==='Space'){ e.preventDefault(); PLAYING=!PLAYING; setPlayIcon(); }
    else if(e.code==='ArrowRight') seek(T+5);
    else if(e.code==='ArrowLeft')  seek(T-5);
    else if(e.key==='h'||e.key==='H'){ UIHIDDEN=!UIHIDDEN; document.body.classList.toggle('bare', UIHIDDEN); }
    else if(e.key==='m'||e.key==='M'){ SND.on=!SND.on; document.getElementById('snd').textContent = SND.on?'♪':'✕'; }
    else if(e.key==='f'||e.key==='F'){
      if(document.fullscreenElement) document.exitFullscreen();
      else document.documentElement.requestFullscreen();
    }
    else if(e.key==='0'){ seek(0); }
    else if(e.key==='q'||e.key==='Q'){ cycleQuality(); }
  });
  document.getElementById('qual').onclick = cycleQuality;
  document.getElementById('snd').onclick = ()=>{
    SND.on=!SND.on; document.getElementById('snd').textContent = SND.on?'♪':'✕';
  };
  document.getElementById('hide').onclick = ()=>{
    UIHIDDEN=!UIHIDDEN; document.body.classList.toggle('bare', UIHIDDEN);
  };
}

/* Auto, then each fixed step, then back to auto */
function cycleQuality(){
  if(scaleAuto){ scaleAuto = false; scaleIx = 0; }
  else if(scaleIx < SCALES.length-1){ scaleIx++; }
  else { scaleAuto = true; scaleIx = 0; }
}

function start(){
  if(!initGL()) return;
  buildAll();
  /* airPath() is resolved here, once PROJ and the bay table are live */
  AIRPATH = airPath();
  buildNotes();
  wireUI();
  /* fill the derived figures into the opening plate */
  document.getElementById('derived').textContent =
    PROJ.narrative.steps + ' steps  ·  ' + (PROJ.narrative.pace/1000).toFixed(3) +
    ' m pace  ·  ' + (PROJ.narrative.walkLen/1000).toFixed(2) + ' m walked';
  document.getElementById('gate').addEventListener('click', ()=>{
    SND.init();
    if(SND.ac && SND.ac.state==='suspended') SND.ac.resume();
    document.getElementById('gate').classList.add('gone');
    PLAYING = true; setPlayIcon();
  });
  setPlayIcon();
  requestAnimationFrame(frame);
}
