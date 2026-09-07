"""
wm_mspdi.py — writes the master programme as a Microsoft Project file.

Underground CBRN-hardened blast-resistant protective structure + sentry post, Pune.
Works Management package revision WM1.

FORMAT — READ THIS BEFORE ASKING WHY THERE IS NO .mpp
-----------------------------------------------------
Microsoft Project's native .mpp is an undocumented binary (OLE2 compound
document) format.  It can only be written by Microsoft Project itself.  The
industry-standard library for Project files, MPXJ, READS .mpp but its writer
supports only JSON, MPX, MSPDI, Planner, PMXML, XER and SDEF — this was
verified in this environment against mpxj 16.7.0
(org.mpxj.writer.FileFormat has no MPP member).

This package therefore writes **MSPDI** — the Microsoft Project Data
Interchange schema, Microsoft's own published XML format for Project.  It is
not a substitute or an approximation: it is a first-class Project file that
carries the full WBS, durations, links with lags, calendar, constraints,
resources, assignments, milestones and notes.

To obtain the .mpp:
    File > Open > Underground_Shelter_Final_Works_Programme.xml
    File > Save As > Project (*.mpp)
Everything below is preserved and the file remains fully editable.

A CSV task list is written alongside for import into any other planning tool.
"""

import csv
import os
from datetime import datetime
from xml.sax.saxutils import escape

import wm_data as D
import wm_schedule as S

MIN_PER_DAY = 480          # 08:00-12:00 + 13:00-17:00
MIN_PER_WEEK = 6 * 480     # six-day working week
DAYS_PER_MONTH = 26

HOLIDAY_NAMES = {
    (1, 26): "Republic Day",
    (5, 1): "Maharashtra Day / Labour Day",
    (8, 15): "Independence Day",
    (10, 2): "Gandhi Jayanti",
    (12, 25): "Christmas Day",
}

# MSPDI expresses duration-valued integer fields (LinkLag, TotalSlack,
# FreeSlack) in TENTHS OF A MINUTE.  Verified by reading the file back
# with MPXJ and comparing against the CPM result.
TENTHS = 10

LINK_TYPE = {"FF": 0, "FS": 1, "SF": 2, "SS": 3}


def dt_start(i):
    return S.CAL.day(i).strftime("%Y-%m-%dT08:00:00")


def dt_finish(i):
    return S.CAL.day(i).strftime("%Y-%m-%dT17:00:00")


def dur(days):
    return "PT%dH0M0S" % (days * 8)


def build_outline(tasks):
    """
    Interleave WBS summary rows with their leaf activities, in outline order.
    Returns a list of dicts ready for emission, and assigns sequential UIDs.
    """
    roll = S.wbs_rollup(tasks)
    by_wbs = {}
    for t in sorted(tasks.values(), key=lambda x: x.uid):
        by_wbs.setdefault(t.wbs, []).append(t)

    rows = []
    uid = 1
    for code, title in D.WBS:
        if code not in roll:
            continue
        es, ef = roll[code]
        rows.append(dict(uid=uid, kind="summary", wbs=code, name=title,
                         level=len(code.split(".")), es=es, ef=ef,
                         dur=ef - es + 1, note=""))
        uid += 1
        for t in by_wbs.get(code, []):
            rows.append(dict(uid=uid, kind="task", wbs=code, task=t,
                             name=t.name, level=len(code.split(".")) + 1,
                             es=t.es, ef=t.ef, dur=t.dur, note=t.note))
            t.uid = uid
            uid += 1
    return rows


def outline_numbers(rows):
    """Microsoft Project OutlineNumber, e.g. 3.2.4 — derived from row order."""
    counters = {}
    stack = []
    for r in rows:
        lvl = r["level"]
        stack = stack[:lvl - 1]
        key = tuple(stack)
        counters[key] = counters.get(key, 0) + 1
        # reset deeper counters
        for k in [k for k in counters if len(k) >= lvl and k[:lvl - 1] == key and k != key]:
            del counters[k]
        stack = list(key) + [counters[key]]
        r["outline"] = ".".join(str(x) for x in stack)
    return rows


def write_mspdi(path, tasks):
    rows = outline_numbers(build_outline(tasks))
    res_uid = {name: i + 1 for i, (name, *_r) in enumerate(D.RESOURCES)}
    end = max(t.ef for t in tasks.values())

    o = []
    a = o.append
    a('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>')
    a('<Project xmlns="http://schemas.microsoft.com/project">')
    a('  <SaveVersion>14</SaveVersion>')
    a('  <Name>Underground_Shelter_Final_Works_Programme.xml</Name>')
    a('  <Title>%s</Title>' % escape(
        "%s — %s (Rev %s)" % (D.PROJECT["title"], D.PROJECT["programme_title"], D.REV)))
    a('  <Subject>Works Management — complete project including the sentry post</Subject>')
    a('  <Company>B.E. Civil Engineering final-semester project</Company>')
    a('  <Manager>Project Manager</Manager>')
    a('  <CreationDate>%s</CreationDate>' % D.REV_DATE.strftime("%Y-%m-%dT08:00:00"))
    a('  <ScheduleFromStart>1</ScheduleFromStart>')
    a('  <StartDate>%s</StartDate>' % dt_start(0))
    a('  <FinishDate>%s</FinishDate>' % dt_finish(end))
    a('  <CalendarUID>1</CalendarUID>')
    a('  <DefaultStartTime>08:00:00</DefaultStartTime>')
    a('  <DefaultFinishTime>17:00:00</DefaultFinishTime>')
    a('  <MinutesPerDay>%d</MinutesPerDay>' % MIN_PER_DAY)
    a('  <MinutesPerWeek>%d</MinutesPerWeek>' % MIN_PER_WEEK)
    a('  <DaysPerMonth>%d</DaysPerMonth>' % DAYS_PER_MONTH)
    a('  <DefaultTaskType>0</DefaultTaskType>')
    a('  <DefaultFixedCostAccrual>3</DefaultFixedCostAccrual>')
    a('  <DurationFormat>7</DurationFormat>')
    a('  <WorkFormat>2</WorkFormat>')
    a('  <NewTasksAreManual>0</NewTasksAreManual>')
    a('  <NewTaskStartDate>0</NewTaskStartDate>')
    a('  <SpreadPercentComplete>0</SpreadPercentComplete>')
    a('  <CurrencySymbol>Rs.</CurrencySymbol>')
    a('  <CurrencyCode>INR</CurrencyCode>')
    a('  <CurrencyDigits>2</CurrencyDigits>')
    a('  <WeekStartDay>1</WeekStartDay>')
    a('  <CriticalSlackLimit>0</CriticalSlackLimit>')
    a('  <HonorConstraints>1</HonorConstraints>')

    # ---- calendar --------------------------------------------------------
    a('  <Calendars>')
    a('    <Calendar>')
    a('      <UID>1</UID>')
    a('      <Name>Site 6-day week (Mon-Sat)</Name>')
    a('      <IsBaseCalendar>1</IsBaseCalendar>')
    a('      <BaseCalendarUID>-1</BaseCalendarUID>')
    a('      <WeekDays>')
    # DayType 1=Sunday .. 7=Saturday
    for dt in range(1, 8):
        working = 0 if dt == 1 else 1
        a('        <WeekDay>')
        a('          <DayType>%d</DayType>' % dt)
        a('          <DayWorking>%d</DayWorking>' % working)
        if working:
            a('          <WorkingTimes>')
            a('            <WorkingTime><FromTime>08:00:00</FromTime>'
              '<ToTime>12:00:00</ToTime></WorkingTime>')
            a('            <WorkingTime><FromTime>13:00:00</FromTime>'
              '<ToTime>17:00:00</ToTime></WorkingTime>')
            a('          </WorkingTimes>')
        a('        </WeekDay>')
    a('      </WeekDays>')
    a('      <Exceptions>')
    for hd in sorted(S.CAL.holidays):
        if not (D.PROJECT["start"] <= hd <= S.CAL.day(end)):
            continue
        a('        <Exception>')
        a('          <EnteredByOccurrences>0</EnteredByOccurrences>')
        a('          <TimePeriod>')
        a('            <FromDate>%sT00:00:00</FromDate>' % hd.isoformat())
        a('            <ToDate>%sT23:59:00</ToDate>' % hd.isoformat())
        a('          </TimePeriod>')
        a('          <Occurrences>1</Occurrences>')
        a('          <Name>%s</Name>' % escape(HOLIDAY_NAMES[(hd.month, hd.day)]))
        a('          <Type>1</Type>')
        a('          <DayWorking>0</DayWorking>')
        a('        </Exception>')
    a('      </Exceptions>')
    a('    </Calendar>')
    a('  </Calendars>')

    # ---- tasks -----------------------------------------------------------
    a('  <Tasks>')
    for r in rows:
        summary = r["kind"] == "summary"
        t = r.get("task")
        ms = (not summary) and t.is_milestone
        a('    <Task>')
        a('      <UID>%d</UID>' % r["uid"])
        a('      <ID>%d</ID>' % r["uid"])
        nm = r["name"] if summary else "%s  %s" % (t.id, r["name"])
        a('      <Name>%s</Name>' % escape(nm))
        a('      <Active>1</Active>')
        a('      <Manual>0</Manual>')
        a('      <Type>0</Type>')                 # fixed units
        a('      <IsNull>0</IsNull>')
        a('      <WBS>%s</WBS>' % escape(r["wbs"] if summary else
                                         "%s.%s" % (r["wbs"], t.id)))
        a('      <OutlineNumber>%s</OutlineNumber>' % r["outline"])
        a('      <OutlineLevel>%d</OutlineLevel>' % r["level"])
        a('      <Priority>500</Priority>')
        a('      <Start>%s</Start>' % dt_start(r["es"]))
        a('      <Finish>%s</Finish>' % (dt_start(r["es"]) if ms else dt_finish(r["ef"])))
        a('      <Duration>%s</Duration>' % dur(0 if ms else max(r["dur"], 0)))
        a('      <DurationFormat>7</DurationFormat>')
        a('      <Milestone>%d</Milestone>' % (1 if ms else 0))
        a('      <Summary>%d</Summary>' % (1 if summary else 0))
        a('      <Critical>%d</Critical>' % (0 if summary else (1 if t.tf == 0 else 0)))
        a('      <Rollup>1</Rollup>')
        a('      <ConstraintType>0</ConstraintType>')     # As Soon As Possible
        a('      <EffortDriven>0</EffortDriven>')
        a('      <FixedCostAccrual>3</FixedCostAccrual>')
        a('      <PercentComplete>0</PercentComplete>')
        a('      <CalendarUID>1</CalendarUID>')
        if not summary:
            a('      <TotalSlack>%d</TotalSlack>' % (t.tf * MIN_PER_DAY * 10))
            a('      <FreeSlack>%d</FreeSlack>' % (t.ff * MIN_PER_DAY * 10))
            note = t.note
            if note:
                a('      <Notes>%s</Notes>' % escape(note))
            for pid, typ, lag in t.preds:
                p = tasks[pid]
                a('      <PredecessorLink>')
                a('        <PredecessorUID>%d</PredecessorUID>' % p.uid)
                a('        <Type>%d</Type>' % LINK_TYPE[typ])
                a('        <CrossProject>0</CrossProject>')
                a('        <LinkLag>%d</LinkLag>' % (lag * MIN_PER_DAY * 10))
                a('        <LagFormat>7</LagFormat>')
                a('      </PredecessorLink>')
        a('    </Task>')
    a('  </Tasks>')

    # ---- resources -------------------------------------------------------
    a('  <Resources>')
    for i, (name, group, comp, peak, note) in enumerate(D.RESOURCES):
        a('    <Resource>')
        a('      <UID>%d</UID>' % (i + 1))
        a('      <ID>%d</ID>' % (i + 1))
        a('      <Name>%s</Name>' % escape(name))
        a('      <Type>1</Type>')                  # work resource
        a('      <IsNull>0</IsNull>')
        a('      <Group>%s</Group>' % escape(group))
        a('      <MaxUnits>%.2f</MaxUnits>' % float(peak))
        a('      <CalendarUID>1</CalendarUID>')
        a('      <Notes>%s</Notes>' % escape("%s. %s" % (comp, note)))
        a('    </Resource>')
    a('  </Resources>')

    # ---- assignments -----------------------------------------------------
    a('  <Assignments>')
    auid = 1
    for r in rows:
        if r["kind"] != "task":
            continue
        t = r["task"]
        if not t.res:
            continue
        for rn in [x.strip() for x in t.res.split(";") if x.strip()]:
            if rn not in res_uid:
                raise ValueError("%s uses an undefined resource %r" % (t.id, rn))
            a('    <Assignment>')
            a('      <UID>%d</UID>' % auid)
            a('      <TaskUID>%d</TaskUID>' % t.uid)
            a('      <ResourceUID>%d</ResourceUID>' % res_uid[rn])
            a('      <Units>1.00</Units>')
            a('      <Start>%s</Start>' % dt_start(t.es))
            a('      <Finish>%s</Finish>' % dt_finish(t.ef))
            a('      <Work>%s</Work>' % dur(max(t.dur, 0)))
            a('      <PercentWorkComplete>0</PercentWorkComplete>')
            a('    </Assignment>')
            auid += 1
    a('  </Assignments>')
    a('</Project>')

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(o) + "\n")
    return rows


def write_csv(path, tasks, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        wcsv = csv.writer(f)
        wcsv.writerow(["Outline", "WBS", "Activity ID", "Task Name",
                       "Duration (working days)", "Start", "Finish",
                       "Predecessors", "Total Float (d)", "Free Float (d)",
                       "Critical", "Resources", "Note"])
        for r in rows:
            if r["kind"] == "summary":
                wcsv.writerow([r["outline"], r["wbs"], "", r["name"],
                               r["dur"], S.dstr(r["es"]), S.dstr(r["ef"]),
                               "", "", "", "", "", "SUMMARY"])
            else:
                t = r["task"]
                preds = ",".join(
                    "%s%s%s" % (p, "" if ty == "FS" else ty,
                                ("%+d" % lg) if lg else "")
                    for p, ty, lg in t.preds)
                wcsv.writerow([r["outline"], r["wbs"], t.id, r["name"],
                               t.dur, S.dstr(t.es), S.dstr(t.ef), preds,
                               t.tf, t.ff, "YES" if t.tf == 0 else "",
                               t.res, t.note])


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "..", "Programme")
    tasks, order, end, lines = S.summary()
    rows = write_mspdi(os.path.join(
        out, "Underground_Shelter_Final_Works_Programme.xml"), tasks)
    write_csv(os.path.join(
        out, "Underground_Shelter_Final_Works_Programme.csv"), tasks, rows)
    print("\n".join(lines))
    print("MSPDI rows (incl. summaries): %d" % len(rows))
