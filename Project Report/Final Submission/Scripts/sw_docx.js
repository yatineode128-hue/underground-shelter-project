/*
 * sw_docx.js -- builds the editable Word version of the report from the
 * layout file written by sw_export.py.
 *
 *   python3 Scripts/sw_export.py BUILD
 *   NODE_PATH=$(npm root -g) node Scripts/sw_docx.js BUILD/report.json OUT.docx
 *
 * Format as the CME project report instructions (Appx 'C'): A4; margins left
 * 37.5, right, top and bottom 25 mm; Times New Roman 12 at 1.5 lines; page
 * headings 14 bold; chapter number and name 12 capital bold; titles 12 bold in
 * sentence case; figure names below and table titles above, 12 point; page
 * number centred at the foot.  The contents, figure and table lists are Word
 * fields filled from TC entries: Word refreshes them (and their page numbers)
 * when fields are updated, and it is asked to do so on opening.
 */
const fs = require("fs");
const d = require("docx");
const {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell,
  WidthType, BorderStyle, ShadingType, AlignmentType, TabStopType, Footer,
  PageNumber, NumberFormat, TableOfContents, SimpleField, PageBorderDisplay,
  PageBorderOffsetFrom, VerticalAlign, HeightRule, TableLayoutType,
  SectionType, LeaderType,
} = d;

const [, , jsonPath, outPath] = process.argv;
const R = JSON.parse(fs.readFileSync(jsonPath, "utf8"));
const P = R.page;
const FONT = "Times New Roman";
const TW = 56.6929;                         // twips per mm
const tw = (mm) => Math.round(mm * TW);
const px = (mm) => Math.round((mm / 25.4) * 96);
const TEXT_W = tw(P.text_w);
const LINE15 = 360;                          // 1.5 lines
const NONE = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const NOB = { top: NONE, bottom: NONE, left: NONE, right: NONE };
const THIN = { style: BorderStyle.SINGLE, size: 4, color: "404040" };
const ALIGN = { L: AlignmentType.LEFT, C: AlignmentType.CENTER,
  R: AlignmentType.RIGHT };

// ------------------------------------------------------------------ runs
function mkRuns(runs, o = {}) {
  const out = [];
  for (const r of runs || []) {
    if (r.br) { out.push(new TextRun({ text: "", break: 1 })); continue; }
    out.push(new TextRun({
      text: r.t, font: FONT, size: Math.round((o.size || 12) * 2),
      bold: !!(r.b || o.bold), italics: !!r.i, underline: r.u ? {} : undefined,
      subScript: !!r.sub, superScript: !!r.sup,
    }));
  }
  return out;
}
const plain = (text, o = {}) => mkRuns([{ t: text }], o);
const cleanTC = (s) => s.replace(/"/g, "'");
const tc = (text, id) => new SimpleField(`TC "${cleanTC(text)}" \\f ${id} \\l 1`);

function img(path, wmm, hmm) {
  const type = path.endsWith(".jpg") ? "jpg" : "png";
  return new ImageRun({ type, data: fs.readFileSync(path),
    transformation: { width: px(wmm), height: px(hmm) } });
}

const body = (children, o = {}) => new Paragraph({
  children, alignment: o.align || AlignmentType.JUSTIFIED,
  spacing: { line: o.line || LINE15, lineRule: "auto",
    before: o.before || 0, after: o.after === undefined ? 120 : o.after },
  indent: o.indent, tabStops: o.tabStops, keepNext: o.keepNext,
  pageBreakBefore: o.pageBreakBefore, border: o.border,
});
const centre = (children, o = {}) =>
  body(children, Object.assign({ align: AlignmentType.CENTER }, o));
const spacer = (mm) => new Paragraph({ children: [],
  spacing: { before: 0, after: 0, line: Math.max(tw(mm), 20),
    lineRule: "exact" } });

// ------------------------------------------------------------------ tables
function cell(children, o = {}) {
  return new TableCell({
    children, width: { size: o.w, type: WidthType.DXA },
    columnSpan: o.span, borders: o.borders || NOB,
    shading: o.fill ? { type: ShadingType.CLEAR, color: "auto",
      fill: o.fill } : undefined,
    margins: o.margins || { top: 30, bottom: 30, left: 64, right: 64 },
    verticalAlign: o.valign || VerticalAlign.TOP,
  });
}
const cellPara = (children, o = {}) => new Paragraph({ children,
  alignment: o.align || AlignmentType.LEFT,
  spacing: { line: 240, lineRule: "auto", before: 0, after: 0 },
  keepNext: o.keepNext });

function dataTable(t) {
  const ws = t.widths.map(tw);
  const total = ws.reduce((a, b) => a + b, 0);
  const ncol = ws.length;
  const rows = t.rows.map((r, ri) => {
    const head = t.header && ri === 0;
    const allB = { top: THIN, bottom: THIN, left: THIN, right: THIN };
    if (t.groups.includes(ri)) {
      return new TableRow({ cantSplit: true, children: [cell(
        [cellPara(mkRuns(r[0], { size: t.font, bold: true }))],
        { w: total, span: ncol, borders: allB, fill: P.group_bg })] });
    }
    return new TableRow({ cantSplit: true, tableHeader: head,
      children: r.map((c, ci) => cell([cellPara(
        mkRuns(c, { size: t.font, bold: head }),
        { align: head ? AlignmentType.CENTER : ALIGN[t.align[ci]] })],
      { w: ws[ci], borders: allB, fill: head ? P.head_bg : undefined })) });
  });
  return new Table({ rows, columnWidths: ws, layout: TableLayoutType.FIXED,
    width: { size: total, type: WidthType.DXA },
    alignment: AlignmentType.CENTER });
}

function plainTable(rows, widths, o = {}) {
  const total = widths.reduce((a, b) => a + b, 0);
  return new Table({ rows, columnWidths: widths,
    layout: TableLayoutType.FIXED, width: { size: total, type: WidthType.DXA },
    alignment: o.align || AlignmentType.CENTER, indent: o.indent,
    borders: { top: NONE, bottom: NONE, left: NONE, right: NONE,
      insideHorizontal: NONE, insideVertical: NONE } });
}

// ------------------------------------------------------------------ lists
function listField(entries, id, title) {
  const kids = entries.map((e) => new Paragraph({
    children: [...plain(e.text, { bold: id === "C" }), new TextRun({
      text: "\t" + e.page, font: FONT, size: 24, bold: false })],
    tabStops: [{ type: TabStopType.RIGHT, position: TEXT_W,
      leader: LeaderType ? LeaderType.DOT : "dot" }],
    indent: { right: 400 },
    spacing: { line: 276, lineRule: "auto", after: 40 } }));
  return new TableOfContents(title, { tcFieldIdentifier: id,
    contentChildren: kids });
}

// ------------------------------------------------------------------ build
const sections = [];
let cur = null;
function newSection(kind) {
  cur = { kind, children: [] };
  sections.push(cur);
}
const push = (...x) => cur.children.push(...x);
let pendingBreak = false;         // next heading starts a new page

newSection("cover");
for (const it of R.items) {
  switch (it.t) {
    case "cover":
      for (const p of it.parts) {
        if (p.k === "space") push(spacer(p.mm));
        else if (p.k === "line") push(centre(mkRuns(p.runs,
          { size: p.size, bold: p.bold }), { line: 276, after: 0 }));
        else if (p.k === "figure") push(centre([img(p.path, p.w, p.h)],
          { line: 240, after: 0 }));
        else if (p.k === "names") {
          const w = Math.round(TEXT_W / 2);
          const n = Math.max(...p.cols.map((c) => c.length));
          const rows = [];
          for (let i = 0; i < n; i++) {
            rows.push(new TableRow({ children: p.cols.map((c) => cell(
              [cellPara(plain(c[i] || "", { size: 12 }),
                { align: AlignmentType.CENTER })], { w,
                margins: { top: 0, bottom: 20, left: 0, right: 0 } })) }));
          }
          push(plainTable(rows, p.cols.map(() => w)));
        }
      }
      break;
    case "front":
      if (it.first) newSection("front");
      push(centre([...mkRuns([{ t: it.title, u: true }],
        { size: 14, bold: true }), ...(it.toc ? [tc(it.toc, "C")] : [])],
      { line: 276, after: 160, pageBreakBefore: !it.first }));
      break;
    case "chapter":
      if (it.first) newSection("main");
      push(centre([...plain(it.label, { bold: true }), tc(it.toc, "C")],
        { line: 276, after: 40, pageBreakBefore: !it.first, keepNext: true }));
      push(centre(plain(it.title, { bold: true }),
        { line: 276, after: 40, keepNext: true }));
      if (it.sub) push(centre(plain(it.sub, { bold: true }),
        { line: 276, after: 280, keepNext: true }));
      break;
    case "head":
      push(body(mkRuns(it.runs, { bold: true }),
        { align: AlignmentType.LEFT, before: 120, keepNext: true }));
      break;
    case "para": {
      const kids = [...plain(it.num, { bold: !!it.title }),
        new TextRun({ text: "\t", font: FONT, size: 24 })];
      if (it.title) kids.push(...plain(it.title + ". ", { bold: true }));
      kids.push(...mkRuns(it.runs));
      push(body(kids, { indent: { left: tw(it.ind) },
        tabStops: [{ type: TabStopType.LEFT, position: tw(it.tab) }] }));
      break;
    }
    case "text":
      push(it.centre ? centre(mkRuns(it.runs))
        : body(mkRuns(it.runs), { indent: { left: tw(it.ind) } }));
      break;
    case "table":
      if (it.caption) push(centre([...plain(it.caption, { bold: true }),
        tc(it.caption, "T")], { line: 276, before: 80, after: 80,
        keepNext: true }));
      push(dataTable(it), spacer(3));
      break;
    case "calc": {
      const w = TEXT_W - tw(it.ind);
      const a = Math.round(w * 0.74);
      const b = w - a;
      const rows = it.rows.map((r) => {
        const L = mkRuns(r.a, { bold: r.bold });
        const Rr = mkRuns(r.b, { bold: r.bold });
        if (!r.b.length) return new TableRow({ children: [cell(
          [cellPara(L)], { w: a + b, span: 2 })] });
        return new TableRow({ children: [cell([cellPara(L)], { w: a }),
          cell([cellPara(Rr, { align: AlignmentType.RIGHT })], { w: b })] });
      });
      push(plainTable(rows, [a, b], { align: AlignmentType.LEFT,
        indent: { size: tw(it.ind), type: WidthType.DXA } }), spacer(2));
      break;
    }
    case "figure":
      push(centre([img(it.path, it.w, it.h)],
        { line: 240, before: 60, after: 40, keepNext: true }));
      push(centre([...plain(it.caption, { bold: true }), tc(it.caption, "F")],
        { line: 276, after: 180 }));
      break;
    case "grid": {
      const cw = Math.floor(TEXT_W / it.cols);
      const iw = P.text_w / it.cols - 4;
      const rows = [];
      for (let i = 0; i < it.cells.length; i += it.cols) {
        const grp = it.cells.slice(i, i + it.cols);
        rows.push(grp);
      }
      for (const grp of rows) {
        const r = new TableRow({ cantSplit: true, children: grp.map((c) => {
          const dims = c.dims;
          return cell([
            cellPara([img(c.path, iw, iw * dims[1] / dims[0])],
              { align: AlignmentType.CENTER, keepNext: true }),
            cellPara(plain(c.label, { size: 10 }),
              { align: AlignmentType.CENTER, keepNext: true })],
          { w: cw, margins: { top: 40, bottom: 120, left: 60, right: 60 },
            valign: VerticalAlign.BOTTOM });
        }) });
        push(plainTable([r], grp.map(() => cw)));
      }
      push(centre([...plain(it.caption, { bold: true }), tc(it.caption, "F")],
        { line: 276, before: 60, after: 180 }));
      break;
    }
    case "image":
      push(centre([img(it.path, it.w, it.h)], { line: 240, after: 60 }));
      break;
    case "cols": {
      const w = Math.floor(TEXT_W / it.cols.length);
      const r = new TableRow({ children: it.cols.map((c) => cell(
        c.map((ln, k) => cellPara(mkRuns(ln, { bold: k === 0 }))),
        { w, margins: { top: 0, bottom: 0, left: 120, right: 60 } })) });
      push(plainTable([r], it.cols.map(() => w)), spacer(3));
      break;
    }
    case "right": {
      const ind = Math.round(TEXT_W * 0.58);
      it.lines.forEach((ln, k) => push(body(mkRuns(ln), {
        align: AlignmentType.LEFT, line: 276, after: 0,
        indent: { left: ind }, before: k === 0 && it.rule ? 60 : 0,
        border: k === 0 && it.rule ? { top: { style: BorderStyle.SINGLE,
          size: 6, color: "000000", space: 4 } } : undefined })));
      push(spacer(3));
      break;
    }
    case "sigs": {
      let slots = it.slots;
      if (slots.length === 1) slots = [[""], [""], slots[0]];
      const gap = tw(6);
      const w = Math.floor((TEXT_W - 2 * gap) / 3);
      const widths = [w, gap, w, gap, w];
      const rows = [];
      for (let i = 0; i < slots.length; i += 3) {
        const g = slots.slice(i, i + 3);
        while (g.length < 3) g.push([""]);
        rows.push(new TableRow({ height: { value: tw(13),
          rule: HeightRule.EXACT }, children: widths.map((x) =>
          cell([cellPara([])], { w: x })) }));
        const kids = [];
        g.forEach((s, j) => {
          const named = s[0] !== "";
          const lines = s.filter((x) => x);
          kids.push(cell(lines.map((ln) => cellPara(plain(ln, { size: 11 }),
            { align: AlignmentType.CENTER })), { w,
            borders: named ? { top: { style: BorderStyle.SINGLE, size: 6,
              color: "000000" }, bottom: NONE, left: NONE, right: NONE }
              : NOB }));
          if (j < 2) kids.push(cell([cellPara([])], { w: gap }));
        });
        rows.push(new TableRow({ children: kids }));
      }
      push(plainTable(rows, widths));
      break;
    }
    case "examiners": {
      const ws = [0.34, 0.36, 0.30].map((f) => Math.round(TEXT_W * f));
      const line = { top: NONE, left: NONE, right: NONE,
        bottom: { style: BorderStyle.SINGLE, size: 6, color: "000000" } };
      const mk = (a, h, bold, lined) => new TableRow({
        height: { value: tw(h), rule: HeightRule.EXACT },
        children: [cell([cellPara(plain(a[0], { bold }))],
          { w: ws[0], valign: VerticalAlign.BOTTOM }),
        cell([cellPara(plain(a[1], { bold }))], { w: ws[1],
          valign: VerticalAlign.BOTTOM, borders: lined ? line : NOB }),
        cell([cellPara(plain(a[2], { bold }))], { w: ws[2],
          valign: VerticalAlign.BOTTOM, borders: lined ? line : NOB })] });
      push(plainTable([mk(["Examiners", "Name", "Signatures"], 8, true, false),
        mk(["1.   External Examiner", "", ""], 12, false, true),
        mk(["2.   Guide", "", ""], 12, false, true)], ws), spacer(3));
      break;
    }
    case "vspace":
      push(spacer(it.mm));
      break;
    case "pagebreak":
      pendingBreak = true;
      break;
    case "toc":
      push(listField(it.entries, "C", "Contents"));
      break;
    case "lof":
      push(listField(it.entries, "F", "List of figures"));
      break;
    case "lot":
      push(listField(it.entries, "T", "List of tables"));
      break;
    default:
      throw new Error("unknown item " + it.t);
  }
}

// ------------------------------------------------------------------ document
const margin = { top: tw(P.top), bottom: tw(P.bottom), left: tw(P.left),
  right: tw(P.right), footer: tw(10), header: tw(10) };
const footer = () => ({ default: new Footer({ children: [new Paragraph({
  alignment: AlignmentType.CENTER, children: [new TextRun({
    children: [PageNumber.CURRENT], font: FONT, size: 24 })] })] }) });
const red = { style: BorderStyle.DOUBLE, size: 12, color: "C8171C", space: 24 };

const doc = new Document({
  creator: "Syndicate 01",
  title: "CBRN Hardened Underground Ops Room - Project Report",
  features: { updateFields: true },
  styles: { default: { document: {
    run: { font: FONT, size: 24 },
    paragraph: { spacing: { line: LINE15, lineRule: "auto",
      after: 120 } } } } },
  sections: sections.map((s) => ({
    properties: {
      type: SectionType.NEXT_PAGE,
      page: Object.assign({ margin },
        s.kind === "cover" ? { borders: {
          pageBorders: { display: PageBorderDisplay.ALL_PAGES,
            offsetFrom: PageBorderOffsetFrom.PAGE },
          pageBorderTop: red, pageBorderBottom: red, pageBorderLeft: red,
          pageBorderRight: red } }
          : { pageNumbers: { start: 1, formatType: s.kind === "front"
            ? NumberFormat.LOWER_ROMAN : NumberFormat.DECIMAL } }),
    },
    footers: s.kind === "cover" ? undefined : footer(),
    children: s.children,
  })),
});

// every drawing gets its own docPr id (docx-js numbers them all 1)
Packer.toBuffer(doc).then(async (buf) => {
  const JSZip = require("jszip");
  const zip = await JSZip.loadAsync(buf);
  let xml = await zip.file("word/document.xml").async("string");
  let n = 0;
  xml = xml.replace(/<wp:docPr id="\d+"/g, () => `<wp:docPr id="${++n}"`);
  zip.file("word/document.xml", xml);
  const out = await zip.generateAsync({ type: "nodebuffer",
    compression: "DEFLATE" });
  fs.writeFileSync(outPath, out);
  console.log("written", outPath, out.length, "bytes,", n, "drawings");
});
