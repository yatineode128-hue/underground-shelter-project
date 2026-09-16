# Animation — AN1

**The deliverable:** [`Output/AN1_UNDERGROUND_CBRN_OPS_ROOM.html`](Output/AN1_UNDERGROUND_CBRN_OPS_ROOM.html)

Open it in any current browser and press **Begin**. It needs WebGL 2 and nothing else — no
internet, no install, no player, no plug-in. Copy that one file to a USB stick and it works.

| | |
|---|---|
| Running time | **6 min 22 s**, one continuous camera journey, 21 beats |
| Technique | Real-time WebGL 2, hand-written, rendered live |
| Dependencies | **None** |
| Design values moved | **NONE** — see `master/MASTER_PROJECT_STATE.md` H.42 |

## Keys

`Space` play/pause · `←` `→` 5 s · `0` restart · `F` full screen ·
**`H` hide the interface — press this before recording** · `M` sound · `Q` render quality

The chapter buttons jump to any of the 21 beats. Use them when an examiner asks to see the
load path or EMP Zone 2 again.

## Recording it to a video file

Full screen (`F`) → hide the interface (`H`) → restart (`0`), then capture with OBS Studio,
the Windows Game Bar (`Win`+`G`) or QuickTime. Let it run the full 6 min 22 s; it fades to
black on its own.

If the machine is slow, press `Q` before recording and pin a fixed render scale — an even
70 % records better than an adaptive scale that steps mid-shot.

## Rendering it to MP4

```
Animation/Scripts/an1_record_all.sh              # 1280x720, 30 fps
Animation/Scripts/an1_record_all.sh 1920 1080 30 # 1080p
```

Writes `Output/AN1_UNDERGROUND_CBRN_OPS_ROOM.mp4` (H.264, silent). Needs
Playwright and an ffmpeg built with libx264 — `pip install imageio-ffmpeg`
supplies one.

**The video is a build artefact and is not tracked in git** — it is regenerable
from the committed sources, and at 60–100 MB it would bloat every clone.

It is rendered **frame by frame, deterministically**: frame *i* is
`stateAt(i / fps)`, not a wall-clock screen capture, so the output plays at a
true 30 fps no matter how slowly the machine produced it, and is identical on
every run. **One worker, not several** — with no GPU a single headless Chromium
already drives SwiftShader at ~350 % CPU and saturates four cores; four workers
measured *slower* than one. Budget roughly 95 minutes for 720p30 on a CPU-only
box, minutes on a machine with a real GPU.

> **Prefer the HTML at the presentation.** The MP4 is a fixed 6:22 recording;
> the page lets you pause on the load path, jump back to EMP Zone 2 when an
> examiner asks, and fills any projector without re-rendering. Keep the MP4 as
> the fallback for a machine you do not control.

## Rebuilding it

```
python3 Animation/Scripts/an1_build.py
```

`Source/*.js` are the sources. **`Output/` is a build artefact — never edit it by hand.**
Start with `Source/00_data.js`: it holds every project value with its evidence tag, and it is
a transcription of master Parts A and B. Nothing may change there that has not changed in the
master first.

## Read this before changing anything

[`Documentation/ANIMATION_DESIGN_BASIS.md`](Documentation/ANIMATION_DESIGN_BASIS.md) — the full
value register with sources and evidence classes, the shot list, what the animation
deliberately does **not** show, and findings `AN1-F1…F7` with open items `AN1-V1…V8`.
