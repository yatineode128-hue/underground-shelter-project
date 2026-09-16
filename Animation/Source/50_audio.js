/* ===========================================================================
   AN1 — SOUNDSCAPE
   One continuous bed, synthesised in the browser. No music, no war-film
   score, no heroic cues (brief section 32). Every layer is a gain driven
   from the same state object the picture is driven from, so the sound
   follows the scrub bar exactly as the image does.
   =========================================================================== */
class Sound {
  constructor(){ this.ok=false; this.on=true; }
  init(){
    if(this.ok) return;
    const AC = window.AudioContext || window.webkitAudioContext;
    if(!AC) return;
    const ac = this.ac = new AC();
    this.master = ac.createGain(); this.master.gain.value = 0.0;
    this.master.connect(ac.destination);

    /* one noise buffer, shared by every noise layer */
    const len = ac.sampleRate * 4;
    const buf = ac.createBuffer(1, len, ac.sampleRate);
    const d = buf.getChannelData(0);
    let last = 0;
    for(let i=0;i<len;i++){                       // brown-ish noise, less hiss
      const w = Math.random()*2-1;
      last = (last + 0.021*w) / 1.021; d[i] = last*3.2;
    }
    this.buf = buf;

    const noise = (type, freq, q, gain)=>{
      const src = ac.createBufferSource(); src.buffer = buf; src.loop = true;
      const f = ac.createBiquadFilter(); f.type = type; f.frequency.value = freq;
      if(q) f.Q.value = q;
      const g = ac.createGain(); g.gain.value = gain||0;
      src.connect(f); f.connect(g); g.connect(this.master); src.start();
      return { g, f, src };
    };
    const tone = (type, freq, gain)=>{
      const o = ac.createOscillator(); o.type = type; o.frequency.value = freq;
      const g = ac.createGain(); g.gain.value = gain||0;
      o.connect(g); g.connect(this.master); o.start();
      return { o, g };
    };

    /* OUTSIDE */
    this.wind   = noise('bandpass', 520, 0.6, 0);      // open ground, wind in grass
    this.gust   = noise('bandpass', 190, 0.8, 0);
    /* BLAST — low-frequency pressure, rushing air, deep rumble */
    this.rumble = noise('lowpass', 62, 1.1, 0);
    this.rush   = noise('highpass', 380, 0.5, 0);
    this.sub    = tone('sine', 24, 0);
    /* UNDERGROUND — muffled exterior, ventilation, electrical, generator */
    this.muffle = noise('lowpass', 105, 0.8, 0);
    this.vent   = noise('bandpass', 310, 1.4, 0);
    this.fan    = noise('bandpass', 760, 2.2, 0);
    this.hum    = tone('sine', 50, 0);                 // 50 Hz, the Indian mains
    this.hum2   = tone('sine', 100, 0);
    this.gen    = tone('sawtooth', 31, 0);
    /* EMP — a tonal artefact, not an explosion */
    this.emp    = tone('triangle', 1180, 0);
    this.empLo  = tone('sine', 196, 0);
    this.ok = true;
  }
  /* footfalls are events, so they are scheduled rather than driven */
  step(){
    if(!this.ok || !this.on) return;
    const ac = this.ac, t = ac.currentTime;
    const src = ac.createBufferSource(); src.buffer = this.buf;
    src.playbackRate.value = 0.8 + Math.random()*0.25;
    const f = ac.createBiquadFilter(); f.type='bandpass'; f.frequency.value = 240; f.Q.value = 1.1;
    const g = ac.createGain();
    g.gain.setValueAtTime(0.0001, t);
    g.gain.linearRampToValueAtTime(0.055, t+0.008);
    g.gain.exponentialRampToValueAtTime(0.0001, t+0.19);
    src.connect(f); f.connect(g); g.connect(this.master);
    src.start(t, Math.random()*3); src.stop(t+0.22);
  }
  set(p, v, t){ if(p) p.gain.setTargetAtTime(Math.max(v,0.0001), this.ac.currentTime, t||0.12); }
  update(s, tNow, playing){
    if(!this.ok) return;
    const m = (this.on && playing) ? 0.85 : 0.0;
    this.master.gain.setTargetAtTime(m, this.ac.currentTime, 0.25);
    if(!playing) return;
    const inside = clamp(s.interiorLit, 0, 1);
    const out    = 1 - inside;
    /* outside */
    this.set(this.wind.g, out * (0.030 + s.wind*0.16));
    this.set(this.gust.g, out * (0.012 + s.wind*0.26));
    /* blast */
    this.set(this.rumble.g, (s.frontOn ? 0.30 : 0.0) * (0.35 + s.wind) * (0.55+out*0.45), 0.35);
    this.set(this.rush.g,   out * s.wind * 0.10, 0.20);
    this.set(this.sub.g,    s.flash*0.30 + (s.frontOn ? s.wind*0.20 : 0), 0.30);
    /* underground */
    this.set(this.muffle.g, inside * (0.045 + (s.frontOn?0.10:0)));
    this.set(this.vent.g,   inside * (0.022 + s.airOn*0.050));
    this.set(this.fan.g,    inside * s.airOn * 0.030);
    this.set(this.hum.g,    inside * 0.022 * (1 - s.lightDip));
    this.set(this.hum2.g,   inside * 0.009 * (1 - s.lightDip));
    this.set(this.gen.g,    inside * s.powerOn * 0.040);
    /* EMP */
    this.set(this.emp.g,   (s.empWash>0 ? 0.016 : 0) + (s.zone2Hi*0.006), 0.18);
    this.set(this.empLo.g, (s.empWash>0 ? 0.020 : 0), 0.18);
    if(this.emp) this.emp.o.frequency.setTargetAtTime(
      1180 - (s.empWash||0)*520, this.ac.currentTime, 0.4);
  }
}
