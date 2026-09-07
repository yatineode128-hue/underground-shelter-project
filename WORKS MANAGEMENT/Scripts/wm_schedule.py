"""
wm_schedule.py — calendar and critical-path calculation.

Underground CBRN-hardened blast-resistant protective structure + sentry post, Pune.
Works Management package revision WM1.

Implements the working calendar defined in wm_data.py and a full CPM pass
(forward, backward, total float, free float, critical path) over the activity
network, supporting FS, SS, FF and SF links with positive and negative lags,
exactly as Microsoft Project does.

The result is the single set of dates used by the MSPDI programme file, the
programme PDF and the handout.  Nothing is scheduled by hand.
"""

from datetime import date, timedelta
import re

import wm_data as D


# ---------------------------------------------------------------------------
# CALENDAR
# ---------------------------------------------------------------------------
class Calendar:
    """Six-day working week with date-certain national holidays."""

    def __init__(self):
        self.holidays = set()
        for y in D.HOLIDAY_YEARS:
            for m, dd in D.FIXED_HOLIDAYS_MMDD:
                self.holidays.add(date(y, m, dd))
        self._fwd = {}     # working-day index -> date
        self._rev = {}     # date -> working-day index
        self._build(D.PROJECT["start"], 2200)

    def is_working(self, d):
        return d.weekday() in D.WORKING_DAYS and d not in self.holidays

    def _build(self, start, n):
        d = start
        while not self.is_working(d):
            d += timedelta(days=1)
        i = 0
        while i < n:
            if self.is_working(d):
                self._fwd[i] = d
                self._rev[d] = i
                i += 1
            d += timedelta(days=1)

    def day(self, i):
        """Date of working-day index i (0 = project start)."""
        return self._fwd[i]

    def index(self, d):
        return self._rev[d]

    def working_days_between(self, d1, d2):
        return self._rev[d2] - self._rev[d1]


CAL = Calendar()


# ---------------------------------------------------------------------------
# NETWORK
# ---------------------------------------------------------------------------
LINK_RE = re.compile(r"^([A-Za-z0-9]+?)(FS|SS|FF|SF)?([+-]\d+)?$")


def parse_preds(s):
    """'A3090SS+6,A3100' -> [('A3090','SS',6), ('A3100','FS',0)]"""
    out = []
    for part in [p.strip() for p in s.split(",") if p.strip()]:
        m = LINK_RE.match(part)
        if not m:
            raise ValueError("bad predecessor %r" % part)
        pid, typ, lag = m.group(1), m.group(2) or "FS", int(m.group(3) or 0)
        out.append((pid, typ, lag))
    return out


class Task:
    __slots__ = ("id", "wbs", "name", "dur", "preds", "res", "note",
                 "es", "ef", "ls", "lf", "tf", "ff", "succs", "uid")

    def __init__(self, row, uid):
        (self.id, self.wbs, self.name, self.dur, preds, self.res,
         self.note) = row
        self.preds = parse_preds(preds)
        self.uid = uid
        self.es = self.ef = self.ls = self.lf = None
        self.tf = self.ff = None
        self.succs = []

    # In working-day indices.  ES = first working day; EF = last working day.
    # A zero-duration milestone has EF = ES - 1 conceptually; we keep EF = ES
    # and flag it, matching Microsoft Project's presentation of a milestone as
    # a single instant on its start date.
    @property
    def is_milestone(self):
        return self.dur == 0


def build():
    tasks = {}
    for i, row in enumerate(D.A):
        t = Task(row, i + 1)
        if t.id in tasks:
            raise ValueError("duplicate activity id %s" % t.id)
        tasks[t.id] = t
    for t in tasks.values():
        for pid, typ, lag in t.preds:
            if pid not in tasks:
                raise ValueError("%s references unknown predecessor %s" % (t.id, pid))
            tasks[pid].succs.append((t.id, typ, lag))
    return tasks


def topo(tasks):
    """Topological order; raises on a cycle."""
    indeg = {k: len(v.preds) for k, v in tasks.items()}
    ready = [k for k, v in indeg.items() if v == 0]
    order = []
    while ready:
        k = ready.pop(0)
        order.append(k)
        for sid, _, _ in tasks[k].succs:
            indeg[sid] -= 1
            if indeg[sid] == 0:
                ready.append(sid)
    if len(order) != len(tasks):
        stuck = [k for k, v in indeg.items() if v > 0]
        raise ValueError("cycle in the network, involving: %s" % ", ".join(sorted(stuck)))
    return order


def forward(tasks, order):
    for k in order:
        t = tasks[k]
        es = 0
        for pid, typ, lag in t.preds:
            p = tasks[pid]
            pdur = max(p.dur, 0)
            if typ == "FS":
                cand = p.ef + 1 + lag if pdur else p.es + lag
            elif typ == "SS":
                cand = p.es + lag
            elif typ == "FF":
                cand = (p.ef + lag) - max(t.dur - 1, 0)
                if pdur == 0:
                    cand = (p.es + lag) - max(t.dur - 1, 0)
            elif typ == "SF":
                cand = (p.es + lag) - max(t.dur - 1, 0)
            else:
                raise ValueError(typ)
            es = max(es, cand)
        t.es = max(es, 0)
        t.ef = t.es + max(t.dur - 1, 0) if t.dur else t.es


def backward(tasks, order, project_end):
    for k in reversed(order):
        t = tasks[k]
        if not t.succs:
            t.lf = project_end
        else:
            lf = None
            for sid, typ, lag in t.succs:
                s = tasks[sid]
                if typ == "FS":
                    cand = s.ls - 1 - lag if t.dur else s.ls - lag
                elif typ == "SS":
                    cand = (s.ls - lag) + max(t.dur - 1, 0)
                elif typ == "FF":
                    cand = s.lf - lag
                elif typ == "SF":
                    cand = (s.lf - lag) + max(t.dur - 1, 0)
                lf = cand if lf is None else min(lf, cand)
            t.lf = lf
        t.ls = t.lf - max(t.dur - 1, 0) if t.dur else t.lf
        t.tf = t.ls - t.es


def free_float(tasks):
    for t in tasks.values():
        if not t.succs:
            t.ff = t.tf
            continue
        ff = None
        for sid, typ, lag in t.succs:
            s = tasks[sid]
            if typ == "FS":
                cand = s.es - 1 - lag - t.ef if t.dur else s.es - lag - t.es
            elif typ == "SS":
                cand = (s.es - lag) - t.es
            elif typ == "FF":
                cand = (s.ef - lag) - t.ef
            elif typ == "SF":
                cand = (s.ef - lag) - t.es
            ff = cand if ff is None else min(ff, cand)
        t.ff = max(0, ff)


def schedule():
    tasks = build()
    order = topo(tasks)
    forward(tasks, order)
    end = max(t.ef for t in tasks.values())
    backward(tasks, order, end)
    free_float(tasks)
    return tasks, order, end


# ---------------------------------------------------------------------------
# WBS ROLL-UP
# ---------------------------------------------------------------------------
def wbs_rollup(tasks):
    """Return {wbs_code: (es, ef)} for every WBS node, rolled up from leaves."""
    roll = {}
    for t in tasks.values():
        parts = t.wbs.split(".")
        for i in range(len(parts)):
            code = ".".join(parts[:i + 1])
            es, ef = roll.get(code, (10 ** 9, -1))
            roll[code] = (min(es, t.es), max(ef, t.ef))
    return roll


def dstr(i):
    return CAL.day(i).strftime("%d-%m-%y")


def summary():
    tasks, order, end = schedule()
    crit = [t for t in tasks.values() if t.tf == 0]
    lines = []
    lines.append("Project start   : %s" % CAL.day(0).strftime("%A %d %B %Y"))
    lines.append("Project finish  : %s" % CAL.day(end).strftime("%A %d %B %Y"))
    lines.append("Working days    : %d" % (end + 1))
    lines.append("Calendar days   : %d" % ((CAL.day(end) - CAL.day(0)).days + 1))
    lines.append("Activities      : %d  (of which %d milestones)"
                 % (len(tasks), sum(1 for t in tasks.values() if t.is_milestone)))
    lines.append("Critical (TF=0) : %d activities" % len(crit))
    return tasks, order, end, lines


if __name__ == "__main__":
    tasks, order, end, lines = summary()
    print("\n".join(lines))
    print()
    print("CRITICAL PATH")
    print("%-8s %-6s %-64s %4s %-9s %-9s %5s" %
          ("ID", "WBS", "ACTIVITY", "DUR", "START", "FINISH", "TF"))
    for t in sorted((x for x in tasks.values() if x.tf == 0), key=lambda x: (x.es, x.uid)):
        print("%-8s %-6s %-64s %4d %-9s %-9s %5d" %
              (t.id, t.wbs, t.name[:64], t.dur, dstr(t.es), dstr(t.ef), t.tf))
    print()
    print("MILESTONE DATES")
    for mid, aid, name in D.MILESTONES:
        t = tasks[aid]
        print("  %-5s %-9s %-56s %s%s" %
              (mid, aid, name[:56], dstr(t.es),
               "   <- CRITICAL" if t.tf == 0 else "   float %d d" % t.tf))
