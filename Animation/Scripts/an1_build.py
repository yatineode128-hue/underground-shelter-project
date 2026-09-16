#!/usr/bin/env python3
"""
AN1 build — assemble the animation sources into ONE self-contained HTML file.

The output has NO external dependency of any kind: no CDN, no font download,
no network at run time. It plays from a USB stick in a hall with no internet,
which is the only property that matters on the day.

    python3 Animation/Scripts/an1_build.py

Re-run after ANY change to Animation/Source/. Never edit the Output/ file by
hand — it is a build artefact and will be overwritten.
"""
import pathlib, re, sys, datetime

ROOT   = pathlib.Path(__file__).resolve().parents[1]
SRC    = ROOT / "Source"
OUT    = ROOT / "Output" / "AN1_UNDERGROUND_CBRN_OPS_ROOM.html"
# A second, body-only variant for publishing as a Claude Artifact, whose host
# supplies the document skeleton itself. Same animation, same sources; the only
# difference is the wrapper and the phone safe-area inset on the fixed bar.
ART    = ROOT / "Output" / "AN1_ARTIFACT.html"

ORDER = ["00_data.js", "10_engine.js", "20_facility.js", "25_fitout.js",
         "30_effects.js", "40_timeline.js", "50_audio.js", "60_app.js"]


def duration_from_source(text):
    """Read the last beat's end time out of the timeline, so the plate and
    the design basis can never drift from the animation itself."""
    beats = re.findall(r"\['([^']+)',\s*([0-9.]+),\s*([0-9.]+),", text)
    if not beats:
        sys.exit("an1_build: could not read the beat table from 40_timeline.js")
    return float(beats[-1][2]), beats


def caveat_from_data(text):
    m = re.search(r"caveat:\s*'([^']+)'", text)
    return m.group(1) if m else ""


def main():
    missing = [f for f in ORDER if not (SRC / f).exists()]
    if missing:
        sys.exit("an1_build: missing source file(s): " + ", ".join(missing))

    parts, total = [], 0
    for name in ORDER:
        body = (SRC / name).read_text(encoding="utf-8")
        total += len(body)
        parts.append("/* ==== %s ==== */\n%s" % (name, body))
    bundle = "\n\n".join(parts)

    tl = (SRC / "40_timeline.js").read_text(encoding="utf-8")
    dur, beats = duration_from_source(tl)
    mins, secs = int(dur // 60), int(dur % 60)
    dur_str = "%d min %02d s" % (mins, secs)

    tmpl = (SRC / "index_template.html").read_text(encoding="utf-8")
    html = (tmpl
            .replace("__SOURCES__", bundle)
            .replace("__DURATION__", dur_str)
            .replace("__CAVEAT__", caveat_from_data(
                (SRC / "00_data.js").read_text(encoding="utf-8"))))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")

    # ---- the Artifact variant -------------------------------------------
    # The Artifact host wraps the file in its own <!doctype>/<head>/<body>,
    # so the fragment must carry only <title>, <style> and the body content.
    frag = html
    frag = frag[frag.index("<title>"):]
    frag = frag.replace("</head>\n<body>", "", 1)
    frag = frag.replace("</body>\n</html>", "", 1).rstrip() + "\n"
    # the host pads :root by the safe-area insets; a bar fixed to the bottom
    # stays at 0 and adds the inset to its OWN padding
    frag = frag.replace("padding:30px 22px 15px;",
                        "padding:30px 22px calc(15px + env(safe-area-inset-bottom, 0px));")
    if "<html" in frag or "<!DOCTYPE" in frag.upper():
        sys.exit("an1_build: artifact fragment still carries a document wrapper")
    ART.write_text(frag, encoding="utf-8")

    kb = len(html.encode("utf-8")) / 1024
    print("an1_build: wrote %s" % OUT.relative_to(ROOT.parent))
    print("           wrote %s  (Artifact fragment, %.0f kB)" %
          (ART.relative_to(ROOT.parent), len(frag.encode("utf-8")) / 1024))
    print("           %d sources, %.0f kB of JavaScript, %.0f kB total" %
          (len(ORDER), total / 1024, kb))
    print("           %d beats, running time %s (%.0f s)" % (len(beats), dur_str, dur))
    print("           zero external dependencies")
    for name, t0, t1 in beats:
        print("             %6.1f - %6.1f   %s" % (float(t0), float(t1), name))


if __name__ == "__main__":
    main()
