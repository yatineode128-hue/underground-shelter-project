/* ===========================================================================
   AN1 — FRAME RECORDER (one worker)

   Renders a contiguous slice of the animation DETERMINISTICALLY and pipes the
   frames straight into ffmpeg. Every frame is `stateAt(i / fps)`, so the
   result is frame-exact and identical on every run no matter how slow the
   renderer is — a wall-clock screen capture of a software-rasterised page
   would stutter and drop frames, and this cannot.

   Nothing is written to disk but the output segment: the JPEGs go down a pipe.

   Driven by an1_record_all.sh, which splits the film across several workers
   and concatenates the segments. Run directly for one slice:

     node Animation/Scripts/an1_record.js \
       w=1280 h=720 fps=30 from=0 to=300 out=seg0.mp4 ffmpeg=/path/to/ffmpeg

   Requires Playwright and an ffmpeg built with libx264.
   =========================================================================== */
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');

const A    = Object.fromEntries(process.argv.slice(2).map(s => s.split('=')));
const W    = +A.w   || 1280;
const H    = +A.h   || 720;
const FPS  = +A.fps || 30;
const FROM = +A.from || 0;
const TO   = +A.to;
const OUT  = A.out;
const ID   = A.id || '0';
const FF   = A.ffmpeg || 'ffmpeg';
const PAGE = A.page || path.resolve(__dirname, '..', 'Output',
                                    'AN1_UNDERGROUND_CBRN_OPS_ROOM.html');

if (!TO || !OUT) {
  console.error('an1_record: need to=<frame> and out=<file.mp4>');
  process.exit(2);
}

(async () => {
  const ff = spawn(FF, ['-y', '-hide_banner', '-loglevel', 'error',
    '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
    '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20',
    '-pix_fmt', 'yuv420p', '-movflags', '+faststart', OUT]);
  ff.stderr.on('data', d => process.stderr.write(`[ff${ID}] ${d}`));
  const ffDone = new Promise(res => ff.on('close', res));

  const browser = await chromium.launch({ args: [
    '--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader',
    '--hide-scrollbars', '--mute-audio', '--disable-dev-shm-usage'] });
  const pg = await browser.newPage({ viewport: { width: W, height: H },
                                     deviceScaleFactor: 1 });
  const errs = [];
  pg.on('pageerror', e => errs.push(e.message));

  await pg.goto('file://' + PAGE, { waitUntil: 'load' });
  await pg.waitForTimeout(2500);
  await pg.click('#gate .cta');
  await pg.waitForTimeout(600);

  await pg.evaluate(() => {
    /* Take the animation off its own clock, pin full render scale, hide the
       transport — and STOP THE rAF LOOP RE-ARMING. Left running, the page
       keeps rendering between captures and burns most of the CPU on frames
       nobody records. From here each frame is drawn exactly once, on demand. */
    PLAYING = false; SPEED = 0;
    scaleAuto = false; scaleIx = 0;
    UIHIDDEN = true; document.body.classList.add('bare');
    if (window.SND) SND.on = false;
    window.requestAnimationFrame = () => 0;
  });
  await pg.waitForTimeout(400);

  const t0 = Date.now();
  let n = 0;
  for (let i = FROM; i < TO; i++) {
    await pg.evaluate(tt => { T = tt; frame(performance.now()); }, i / FPS);
    const buf = await pg.screenshot({ type: 'jpeg', quality: 92, timeout: 180000 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    n++;
    if (n % 50 === 0 || i === TO - 1) {
      const el = (Date.now() - t0) / 1000;
      const rate = n / el, left = (TO - 1 - i) / rate;
      console.log(`[w${ID}] ${n}/${TO - FROM}  ${rate.toFixed(2)} fps  ` +
                  `elapsed ${(el / 60).toFixed(1)}m  eta ${(left / 60).toFixed(1)}m`);
    }
  }

  ff.stdin.end();
  await browser.close();
  await ffDone;
  console.log(`[w${ID}] DONE ${TO - FROM} frames -> ${OUT}` +
              (errs.length ? `  ERRORS: ${errs.join(' | ')}` : ''));
})();
