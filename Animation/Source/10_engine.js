/* ===========================================================================
   AN1 — ENGINE
   A small dependency-free WebGL2 renderer. Written rather than imported so
   the finished animation is ONE self-contained file that runs from a USB
   stick in a hall with no internet. Z-up, right-handed, matching the
   project's own coordinate system (master A.4.1) so that every coordinate in
   00_data.js goes into the scene unconverted.
   =========================================================================== */

/* ---- math ------------------------------------------------------------- */
const V3 = {
  c:(x,y,z)=>new Float32Array([x,y,z]),
  add:(a,b)=>V3.c(a[0]+b[0],a[1]+b[1],a[2]+b[2]),
  sub:(a,b)=>V3.c(a[0]-b[0],a[1]-b[1],a[2]-b[2]),
  mul:(a,s)=>V3.c(a[0]*s,a[1]*s,a[2]*s),
  dot:(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],
  len:a=>Math.hypot(a[0],a[1],a[2]),
  norm:a=>{const l=V3.len(a)||1;return V3.c(a[0]/l,a[1]/l,a[2]/l);},
  cross:(a,b)=>V3.c(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]),
  lerp:(a,b,t)=>V3.c(a[0]+(b[0]-a[0])*t,a[1]+(b[1]-a[1])*t,a[2]+(b[2]-a[2])*t),
  dist:(a,b)=>Math.hypot(a[0]-b[0],a[1]-b[1],a[2]-b[2])
};

const M4 = {
  ident:()=>new Float32Array([1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1]),
  mul(a,b){
    const o=new Float32Array(16);
    for(let i=0;i<4;i++)for(let j=0;j<4;j++){
      let s=0; for(let k=0;k<4;k++) s+=a[k*4+j]*b[i*4+k];
      o[i*4+j]=s;
    }
    return o;
  },
  persp(fovy,asp,n,f){
    const t=1/Math.tan(fovy*0.5), o=new Float32Array(16);
    o[0]=t/asp; o[5]=t; o[10]=(f+n)/(n-f); o[11]=-1; o[14]=2*f*n/(n-f);
    return o;
  },
  /* Z-up look-at */
  look(eye,tgt,up){
    const f=V3.norm(V3.sub(tgt,eye));
    let s=V3.cross(f,up);
    if(V3.len(s)<1e-6) s=V3.cross(f,V3.c(0,1,0));   // guard: looking straight up/down
    s=V3.norm(s);
    const u=V3.cross(s,f), o=new Float32Array(16);
    o[0]=s[0];o[4]=s[1];o[8]=s[2];
    o[1]=u[0];o[5]=u[1];o[9]=u[2];
    o[2]=-f[0];o[6]=-f[1];o[10]=-f[2];
    o[12]=-V3.dot(s,eye); o[13]=-V3.dot(u,eye); o[14]=V3.dot(f,eye);
    o[15]=1; return o;
  },
  trs(t,rz,s){
    const c=Math.cos(rz), n=Math.sin(rz), o=M4.ident();
    o[0]=c*s[0]; o[1]=n*s[0];
    o[4]=-n*s[1]; o[5]=c*s[1];
    o[10]=s[2];
    o[12]=t[0]; o[13]=t[1]; o[14]=t[2];
    return o;
  }
};

/* scalar helpers */
const clamp=(v,a,b)=>v<a?a:v>b?b:v;
const lerp =(a,b,t)=>a+(b-a)*t;
const smoothstep=(e0,e1,x)=>{const t=clamp((x-e0)/(e1-e0||1e-9),0,1);return t*t*(3-2*t);};
const easeInOut=t=>t<0.5?2*t*t:1-Math.pow(-2*t+2,2)/2;
/* the pacing curve used by every camera move: slow in, slow out, no snap */
const easeCam=t=>{t=clamp(t,0,1); return t*t*t*(t*(t*6-15)+10);};
const invLerp=(a,b,v)=>(v-a)/(b-a||1e-9);
/* deterministic noise so every playback is identical */
function hash(n){ const s=Math.sin(n)*43758.5453; return s-Math.floor(s); }

/* Catmull-Rom through a point list — the camera never cuts, so every
   position and target is a point on one of these splines. */
function catmull(pts,t){
  const n=pts.length-1, i=clamp(Math.floor(t*n),0,n-1), f=t*n-i;
  const p0=pts[Math.max(i-1,0)], p1=pts[i], p2=pts[i+1], p3=pts[Math.min(i+2,n)];
  const f2=f*f, f3=f2*f, o=new Float32Array(3);
  for(let k=0;k<3;k++){
    o[k]=0.5*((2*p1[k])+(-p0[k]+p2[k])*f+
              (2*p0[k]-5*p1[k]+4*p2[k]-p3[k])*f2+
              (-p0[k]+3*p1[k]-3*p2[k]+p3[k])*f3);
  }
  return o;
}

/* ---- GL --------------------------------------------------------------- */
let gl=null, canvas=null;

function compile(vs,fs){
  const p=gl.createProgram();
  for(const [src,type] of [[vs,gl.VERTEX_SHADER],[fs,gl.FRAGMENT_SHADER]]){
    const s=gl.createShader(type);
    gl.shaderSource(s,src); gl.compileShader(s);
    if(!gl.getShaderParameter(s,gl.COMPILE_STATUS))
      throw new Error((type===gl.VERTEX_SHADER?'VS: ':'FS: ')+gl.getShaderInfoLog(s));
    gl.attachShader(p,s);
  }
  gl.linkProgram(p);
  if(!gl.getProgramParameter(p,gl.LINK_STATUS)) throw new Error('link: '+gl.getProgramInfoLog(p));
  p.u=new Proxy({},{get:(c,k)=>(k in c?c[k]:(c[k]=gl.getUniformLocation(p,k)))});
  return p;
}

/* A mesh is positions + normals + a per-vertex material tint and an
   "ao" term baked at build time. Indexed, one VAO each. */
class Mesh {
  constructor(pos,nrm,col,ao,idx){
    this.count=idx.length;
    this.vao=gl.createVertexArray();
    gl.bindVertexArray(this.vao);
    const buf=(data,loc,size)=>{
      const b=gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER,b);
      gl.bufferData(gl.ARRAY_BUFFER,data,gl.STATIC_DRAW);
      gl.enableVertexAttribArray(loc);
      gl.vertexAttribPointer(loc,size,gl.FLOAT,false,0,0);
    };
    buf(new Float32Array(pos),0,3);
    buf(new Float32Array(nrm),1,3);
    buf(new Float32Array(col),2,3);
    buf(new Float32Array(ao),3,1);
    const ib=gl.createBuffer();
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER,ib);
    gl.bufferData(gl.ELEMENT_ARRAY_BUFFER,new Uint32Array(idx),gl.STATIC_DRAW);
    gl.bindVertexArray(null);
  }
  draw(){ gl.bindVertexArray(this.vao); gl.drawElements(gl.TRIANGLES,this.count,gl.UNSIGNED_INT,0); }
}

/* Geometry accumulator. Everything in the scene is built into one of these,
   then uploaded once. Groups let the timeline switch whole assemblies on
   and off (e.g. the cover layers become a section when the camera descends). */
class Builder {
  constructor(){ this.pos=[];this.nrm=[];this.col=[];this.ao=[];this.idx=[];this.n=0; }
  tri(a,b,c,nr,cl,ao){
    for(const v of [a,b,c]){ this.pos.push(v[0],v[1],v[2]); this.nrm.push(nr[0],nr[1],nr[2]);
      this.col.push(cl[0],cl[1],cl[2]); this.ao.push(ao); }
    this.idx.push(this.n,this.n+1,this.n+2); this.n+=3;
  }
  /* explicit-normal quad: used where the geometric normal is horizontal
     (grass blades) and would otherwise read black under a high sun */
  quadN(a,b,c,d,nr,cl,ao){
    this.tri(a,b,c,nr,cl,ao); this.tri(a,c,d,nr,cl,ao);
  }
  quad(a,b,c,d,cl,ao,flip){
    let nr=V3.norm(V3.cross(V3.sub(b,a),V3.sub(d,a)));
    if(flip) nr=V3.mul(nr,-1);
    this.tri(a,b,c,nr,cl,ao); this.tri(a,c,d,nr,cl,ao);
  }
  /* axis-aligned box from two corners, in PROJECT METRES.
     faces: optional 6-bool [+x,-x,+y,-y,+z,-z] to omit hidden faces      */
  box(x0,y0,z0,x1,y1,z1,cl,faces){
    const f=faces||[1,1,1,1,1,1];
    const P=(x,y,z)=>V3.c(x,y,z);
    const A=[x0,x1],B=[y0,y1],C=[z0,z1];
    /* top gets the most light, undersides the least — a cheap, stable AO */
    if(f[4]) this.quad(P(A[0],B[0],C[1]),P(A[1],B[0],C[1]),P(A[1],B[1],C[1]),P(A[0],B[1],C[1]),cl,1.00);
    if(f[5]) this.quad(P(A[0],B[1],C[0]),P(A[1],B[1],C[0]),P(A[1],B[0],C[0]),P(A[0],B[0],C[0]),cl,0.45);
    if(f[0]) this.quad(P(A[1],B[0],C[0]),P(A[1],B[1],C[0]),P(A[1],B[1],C[1]),P(A[1],B[0],C[1]),cl,0.80);
    if(f[1]) this.quad(P(A[0],B[1],C[0]),P(A[0],B[0],C[0]),P(A[0],B[0],C[1]),P(A[0],B[1],C[1]),cl,0.72);
    if(f[2]) this.quad(P(A[1],B[1],C[0]),P(A[0],B[1],C[0]),P(A[0],B[1],C[1]),P(A[1],B[1],C[1]),cl,0.86);
    if(f[3]) this.quad(P(A[0],B[0],C[0]),P(A[1],B[0],C[0]),P(A[1],B[0],C[1]),P(A[0],B[0],C[1]),cl,0.66);
  }
  /* box in PROJECT MILLIMETRES with a level pair in metres */
  mm(x0,y0,x1,y1,z0,z1,cl,faces){
    this.box(x0*MM,y0*MM,z0,x1*MM,y1*MM,z1,cl,faces);
  }
  cyl(cx,cy,z0,z1,r,cl,seg,inner){
    seg=seg||24;
    for(let i=0;i<seg;i++){
      const a0=i/seg*Math.PI*2, a1=(i+1)/seg*Math.PI*2;
      const p0=V3.c(cx+Math.cos(a0)*r, cy+Math.sin(a0)*r, z0);
      const p1=V3.c(cx+Math.cos(a1)*r, cy+Math.sin(a1)*r, z0);
      const p2=V3.c(cx+Math.cos(a1)*r, cy+Math.sin(a1)*r, z1);
      const p3=V3.c(cx+Math.cos(a0)*r, cy+Math.sin(a0)*r, z1);
      if(inner) this.quad(p1,p0,p3,p2,cl,0.55); else this.quad(p0,p1,p2,p3,cl,0.78);
    }
  }
  disc(cx,cy,z,r,cl,seg,down){
    seg=seg||24;
    const nr=V3.c(0,0,down?-1:1), c=V3.c(cx,cy,z);
    for(let i=0;i<seg;i++){
      const a0=i/seg*Math.PI*2, a1=(i+1)/seg*Math.PI*2;
      const p0=V3.c(cx+Math.cos(a0)*r, cy+Math.sin(a0)*r, z);
      const p1=V3.c(cx+Math.cos(a1)*r, cy+Math.sin(a1)*r, z);
      if(down) this.tri(c,p1,p0,nr,cl,0.5); else this.tri(c,p0,p1,nr,cl,0.95);
    }
  }
  build(){ return new Mesh(this.pos,this.nrm,this.col,this.ao,this.idx); }
  get empty(){ return this.n===0; }
}

/* ---- shaders ----------------------------------------------------------- */
/* One surface shader for the whole scene. Two section planes let the
   camera cut the ground open without swapping models — the engineering
   cutaway in the brief is a clip, not a different scene.                  */
const VS_SURF = `#version 300 es
layout(location=0) in vec3 aPos;
layout(location=1) in vec3 aNrm;
layout(location=2) in vec3 aCol;
layout(location=3) in float aAo;
uniform mat4 uVP, uM;
out vec3 vN, vC, vW; out float vAo;
void main(){
  vec4 w = uM * vec4(aPos,1.0);
  vW = w.xyz;
  vN = mat3(uM) * aNrm;
  vC = aCol; vAo = aAo;
  gl_Position = uVP * w;
}`;

const FS_SURF = `#version 300 es
precision highp float;
in vec3 vN, vC, vW; in float vAo;
uniform vec3 uSun, uEye, uSky, uGnd, uFogCol;
uniform float uFog, uAlpha, uGhost, uTint;
uniform vec3 uTintCol;
/* section planes: xyz = normal, w = d.  Fragment is cut where dot(n,p)+d > 0 */
uniform vec4 uClipA, uClipB;
uniform float uClipOn;
out vec4 frag;
void main(){
  if(uClipOn > 0.5){
    if(dot(uClipA.xyz, vW) + uClipA.w > 0.0) discard;
    if(dot(uClipB.xyz, vW) + uClipB.w > 0.0) discard;
  }
  vec3 N = normalize(vN);
  float d = max(dot(N, uSun), 0.0);
  /* hemisphere ambient: sky above, bounced ground below */
  float h = N.z * 0.5 + 0.5;
  vec3 amb = mix(uGnd, uSky, h);
  vec3 V = normalize(uEye - vW);
  vec3 H = normalize(V + uSun);
  float spec = pow(max(dot(N,H),0.0), 42.0) * 0.16;
  /* vC is authored as the surface's INTENDED sRGB appearance in full light,
     so it is linearised here and gamma-encoded again at the end. A fully
     lit face then renders at exactly the colour the palette names, which
     is the only way a restrained palette stays predictable. */
  vec3 alb = pow(max(vC, 0.0), vec3(2.2));
  vec3 col = alb * (amb * vAo + d) + spec;
  col = mix(col, pow(uTintCol, vec3(2.2)), uTint);
  float dist = length(uEye - vW);
  /* exp2 fog: the near field stays clean and only the far plot fades, so
     the horizon is haze rather than the edge of the model */
  float fd = dist * uFog;
  col = mix(col, uFogCol, 1.0 - exp(-fd * fd));
  /* ghosting is how the ground turns semi-transparent for the cutaway */
  float a = uAlpha;
  if(uGhost > 0.5){
    float rim = 1.0 - abs(dot(N, V));
    col = mix(col, uFogCol * 1.2, 0.30);
    a *= 0.20 + rim * 0.55;
  }
  frag = vec4(pow(max(col, 0.0), vec3(1.0/2.2)), a);
}`;

/* Points: every particle system in the animation — dust, airflow, EMP,
   grass tips, the blast front — is one instanced point buffer.           */
const VS_PT = `#version 300 es
layout(location=0) in vec3 aPos;
layout(location=1) in vec4 aData;   // x = size, y = alpha, zw = colour ramp t, kind
uniform mat4 uVP; uniform vec3 uEye; uniform float uPx;
out float vA; out float vT; out float vK;
void main(){
  vec4 p = uVP * vec4(aPos,1.0);
  gl_Position = p;
  float d = max(length(uEye - aPos), 0.6);
  gl_PointSize = clamp(aData.x * uPx / d, 1.0, 190.0);
  vA = aData.y; vT = aData.z; vK = aData.w;
}`;

const FS_PT = `#version 300 es
precision highp float;
in float vA; in float vT; in float vK;
uniform vec3 uCa, uCb;
out vec4 frag;
void main(){
  vec2 q = gl_PointCoord * 2.0 - 1.0;
  float r = dot(q,q);
  if(r > 1.0) discard;
  float soft = 1.0 - r;
  vec3 c = mix(uCa, uCb, vT);
  /* kind 1 = hard-edged engineering marker, kind 0 = soft atmospheric */
  float a = vA * (vK > 0.5 ? smoothstep(0.0, 0.25, soft) : soft * soft);
  frag = vec4(c, a);
}`;

/* Full-screen overlay: the flash, the fade, the EMP wash. One triangle. */
const VS_FULL = `#version 300 es
const vec2 P[3] = vec2[3](vec2(-1.,-1.), vec2(3.,-1.), vec2(-1.,3.));
out vec2 vUv;
void main(){ vec2 p = P[gl_VertexID]; vUv = p * 0.5 + 0.5; gl_Position = vec4(p,0.,1.); }`;

const FS_FULL = `#version 300 es
precision highp float;
in vec2 vUv; out vec4 frag;
uniform vec3 uCol, uCol2; uniform float uA, uVig, uScan, uTime, uGrad;
void main(){
  float a = uA;
  vec2 d = vUv - 0.5;
  if(uGrad > 0.5){
    /* sky: a single restrained vertical gradient, no sun disc, no clouds */
    vec3 sky = mix(uCol2, uCol, pow(clamp(vUv.y,0.0,1.0), 0.75));
    frag = vec4(sky, 1.0);
    return;
  }
  a *= mix(1.0, 1.0 - dot(d,d) * 1.7, uVig);
  /* uScan is the EMP wash only — a faint horizontal disturbance, no flicker */
  if(uScan > 0.001){
    float s = sin((vUv.y * 320.0) + uTime * 26.0) * 0.5 + 0.5;
    a += s * uScan * 0.16;
  }
  frag = vec4(uCol, clamp(a, 0.0, 1.0));
}`;

/* A particle system with a CPU-side buffer re-uploaded each frame. Counts
   here are small (a few thousand) so this is comfortably fast and keeps
   every effect fully deterministic and scrubbable. */
class Points {
  constructor(max){
    this.max=max; this.n=0;
    this.pos=new Float32Array(max*3); this.dat=new Float32Array(max*4);
    this.vao=gl.createVertexArray(); gl.bindVertexArray(this.vao);
    this.bp=gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER,this.bp);
    gl.bufferData(gl.ARRAY_BUFFER,this.pos.byteLength,gl.DYNAMIC_DRAW);
    gl.enableVertexAttribArray(0); gl.vertexAttribPointer(0,3,gl.FLOAT,false,0,0);
    this.bd=gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER,this.bd);
    gl.bufferData(gl.ARRAY_BUFFER,this.dat.byteLength,gl.DYNAMIC_DRAW);
    gl.enableVertexAttribArray(1); gl.vertexAttribPointer(1,4,gl.FLOAT,false,0,0);
    gl.bindVertexArray(null);
  }
  reset(){ this.n=0; }
  add(x,y,z,size,alpha,t,kind){
    if(this.n>=this.max||alpha<=0.002) return;
    const i=this.n++;
    this.pos[i*3]=x; this.pos[i*3+1]=y; this.pos[i*3+2]=z;
    this.dat[i*4]=size; this.dat[i*4+1]=alpha; this.dat[i*4+2]=t; this.dat[i*4+3]=kind||0;
  }
  flush(){
    if(!this.n) return;
    gl.bindBuffer(gl.ARRAY_BUFFER,this.bp);
    gl.bufferSubData(gl.ARRAY_BUFFER,0,this.pos,0,this.n*3);
    gl.bindBuffer(gl.ARRAY_BUFFER,this.bd);
    gl.bufferSubData(gl.ARRAY_BUFFER,0,this.dat,0,this.n*4);
  }
  draw(){ if(!this.n) return; gl.bindVertexArray(this.vao); gl.drawArrays(gl.POINTS,0,this.n); }
}
