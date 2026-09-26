"""
sw_case.py -- sentence case for titles, headings, captions and table heads,
as the CME project report format (Appx 'C', para 2) requires.

Only the first word keeps its capital.  A word also keeps it when it is an
acronym or code (two or more capitals, or any digit: CBRN, IS, W6, M35,
STAAD.Pro, D-05), a proper noun (KEEP), a month, or a reference word followed
by its number or letter (Zone 2, Part I, Appendix A, Chapter 3, Table 2.1).
"""

import re

KEEP = {
    "Pune", "Maharashtra", "India", "Indian", "Deccan", "Revit",
    "AutoCAD", "Excel", "Glasstone", "Dolan", "Biggs", "Jaky", "Schelkunoff",
    "Portland", "Syndicate", "Pa", "No", "Rs", "Celsius", "Fahrenheit",
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
    "Nov", "Dec",
}
REF = {"Zone", "Part", "Appendix", "Chapter", "Table", "Fig", "Sheet",
       "Annex", "Grade", "Type", "Class", "Stage", "Mode", "Phase"}
# multi-word proper names kept as written
PHRASES = ["CBRN Hardened Underground Ops Room", "College of Military "
           "Engineering", "Indian Standards", "Deccan Trap", "MS Project",
           "MS Excel", "Autodesk Revit", "National Building Code"]
_NEXT_REF = re.compile(r"^(\d|[IVX]+\b|[A-Z]\b|[A-Z]\.\d)")


def _keep(word):
    core = re.sub(r"^[^\w]+|[^\w.]+$", "", word)
    if not core:
        return True
    if any(ch.isdigit() for ch in core):
        return True
    if sum(1 for ch in core if ch.isupper()) >= 2:
        return True
    if len(core) == 1 and core.isupper():
        return True                   # a variable or grid letter: X, Z, E
    return core in KEEP


def _lower(seg):
    """Lower-case one word segment unless it must keep its capital."""
    if _keep(seg):
        return seg
    m = re.search(r"[A-Za-z]", seg)
    if not m or not seg[m.start()].isupper():
        return seg
    i = m.start()
    return seg[:i] + seg[i].lower() + seg[i + 1:]


def _word(w, first):
    """Hyphenated or slashed words are treated segment by segment; the first
    word of the title keeps the capital of its first segment only."""
    parts = re.split(r"([-/])", w)
    out = []
    for k, p in enumerate(parts):
        if p in ("-", "/") or (first and k == 0):
            out.append(p)
        else:
            out.append(_lower(p))
    return "".join(out)


def sentence(s):
    if not s or not re.search(r"[a-z]", s):
        return s                      # empty, or all capitals: leave alone
    # protect <sub>/<sup> markup and whole proper phrases
    hold = {}

    def stash(m):
        key = "\x00%d\x00" % len(hold)
        hold[key] = m.group(0)
        return key
    t = re.sub(r"<(sub|sup)>.*?</\1>", stash, s)
    for ph in PHRASES:
        t = re.sub(re.escape(ph), stash, t)
    words = t.split(" ")
    out, first = [], True
    for i, w in enumerate(words):
        if not w or w.startswith("\x00"):
            out.append(w)
            first = first and not w
            continue
        nxt = words[i + 1] if i + 1 < len(words) else ""
        core = re.sub(r"^[^\w]+", "", w)
        if not first and core.rstrip(",.:;") in REF and _NEXT_REF.match(nxt):
            out.append(w)
        else:
            out.append(_word(w, first))
        first = False
    t = " ".join(out)
    for key, val in hold.items():
        t = t.replace(key, val)
    return t
