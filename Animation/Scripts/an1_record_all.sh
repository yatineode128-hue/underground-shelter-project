#!/usr/bin/env bash
# ===========================================================================
# AN1 — render the whole animation to a single MP4.
#
# Splits the film across N parallel workers, each rendering a contiguous slice
# deterministically (frame i is stateAt(i/fps), never wall-clock) and piping
# straight into its own ffmpeg. The segments are then concatenated without
# re-encoding, so the joins are exact and cost nothing.
#
#   Animation/Scripts/an1_record_all.sh [width] [height] [fps] [workers] [out]
#
# Defaults: 1280 720 30 1 Animation/Output/AN1_UNDERGROUND_CBRN_OPS_ROOM.mp4
#
# Needs Playwright and an ffmpeg with libx264.
#
# WHY ONE WORKER BY DEFAULT. With no GPU the page renders on SwiftShader, and
# a SINGLE browser instance already runs at about 350 % CPU -- it saturates
# four cores by itself. Measured here: one worker 1.16 fps; four workers, load
# average 13-16 and a LOWER total rate. Raise the worker count only on a box
# with cores to spare. With a real GPU this render is minutes, not hours.
# ===========================================================================
set -euo pipefail

W=${1:-1280}
H=${2:-720}
FPS=${3:-30}
N=${4:-1}

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(dirname "$HERE")"
OUT=${5:-"$ROOT/Output/AN1_UNDERGROUND_CBRN_OPS_ROOM.mp4"}
WORK="${TMPDIR:-/tmp}/an1_render_$$"
mkdir -p "$WORK"
trap 'rm -rf "$WORK"' EXIT

FF=${FFMPEG:-$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())" 2>/dev/null || command -v ffmpeg)}
[ -x "$FF" ] || { echo "an1_record_all: no ffmpeg with libx264 found" >&2; exit 1; }

# the running time is read out of the timeline, so the video can never be a
# different length from the animation
DUR=$(grep -oE "\['SITE, AFTER', *[0-9.]+, *[0-9.]+" "$ROOT/Source/40_timeline.js" \
      | grep -oE "[0-9.]+$")
TOTAL=$(python3 -c "import math;print(math.ceil($DUR*$FPS))")

echo "an1_record_all: ${W}x${H} @ ${FPS} fps, ${DUR}s = ${TOTAL} frames, ${N} workers"
echo "                ffmpeg: $FF"
echo "                out:    $OUT"

pids=()
for ((i=0; i<N; i++)); do
  FROM=$(( TOTAL * i / N ))
  TO=$(( TOTAL * (i+1) / N ))
  NODE_PATH=${NODE_PATH:-/opt/node22/lib/node_modules} \
  node "$HERE/an1_record.js" \
      w=$W h=$H fps=$FPS from=$FROM to=$TO id=$i ffmpeg="$FF" \
      out="$WORK/seg$i.mp4" &
  pids+=($!)
done
for p in "${pids[@]}"; do wait "$p"; done

: > "$WORK/list.txt"
for ((i=0; i<N; i++)); do
  [ -s "$WORK/seg$i.mp4" ] || { echo "an1_record_all: segment $i is missing" >&2; exit 1; }
  echo "file '$WORK/seg$i.mp4'" >> "$WORK/list.txt"
done

"$FF" -y -hide_banner -loglevel error -f concat -safe 0 -i "$WORK/list.txt" \
      -c copy -movflags +faststart "$OUT"

echo "an1_record_all: wrote $OUT"
"$FF" -hide_banner -i "$OUT" 2>&1 | grep -E "Duration|Stream" || true
ls -la "$OUT"
