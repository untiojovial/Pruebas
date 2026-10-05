// Usage: node cap.js specs.json [id ...]
const { chromium } = require('playwright');
const { install } = require('./fetchroute');
const fs = require('fs');

const HL_CSS = `
::highlight(ctx){background-color:rgba(255,236,120,.55);}
::highlight(key){background-color:rgba(255,170,0,.85);color:#000;}
::highlight(alt){background-color:rgba(120,200,255,.6);color:#000;}
`;

async function capture(ctx, spec) {
  const p = await ctx.newPage();
  await p.goto(spec.url, { waitUntil: 'load', timeout: 120000 });
  await p.waitForTimeout(1200);
  const fonts = await p.evaluate(() => document.fonts.ready.then(() => [...document.fonts].map(f => f.family + ':' + f.status)));
  const bad = fonts.filter(f => /error/.test(f));
  if (bad.length) console.log(spec.id, 'FONT ERRORS', bad.join(', '));
  if (process.env.DEBUG) console.log(fonts.join(', '));
  if (spec.css) await p.addStyleTag({ content: spec.css });
  await p.addStyleTag({ content: HL_CSS });
  const res = await p.evaluate((spec) => {
    const DIA = /[ؐ-ًؚ-ٰٟۖ-ۭـ‌-‏]/;
    const MAP = { 'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ٱ': 'ا', 'ى': 'ي', 'ة': 'ه', 'ؤ': 'و', 'ئ': 'ي' };
    const isLetter = (c) => /[\p{L}\p{N}]/u.test(c);
    function normStr(s) {
      let o = '';
      for (const c0 of s) { if (DIA.test(c0)) continue; const c = MAP[c0] || c0; if (isLetter(c)) o += c; else if (!o.endsWith(' ')) o += ' '; }
      return o.trim();
    }
    // build index of visible text nodes
    const H = []; const M = [];
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    let n;
    const push = (ch, node, off) => { H.push(ch); M.push([node, off]); };
    while ((n = walker.nextNode())) {
      const el = n.parentElement; if (!el) continue;
      if (/^(SCRIPT|STYLE|NOSCRIPT|OPTION|SELECT)$/.test(el.tagName)) continue;
      if (!el.getClientRects().length) continue;
      const cs = getComputedStyle(el); if (cs.visibility === 'hidden') continue;
      const v = n.nodeValue;
      if (H.length && H[H.length - 1] !== ' ') push(' ', n, 0);
      for (let i = 0; i < v.length; i++) {
        const c0 = v[i]; if (DIA.test(c0)) continue; const c = MAP[c0] || c0;
        if (isLetter(c)) push(c, n, i); else if (H.length && H[H.length - 1] !== ' ') push(' ', n, i);
      }
    }
    const HS = H.join('');
    function find(phrase, from = 0, to = HS.length) {
      const N = normStr(phrase); const i = HS.indexOf(N, from);
      if (i < 0 || i + N.length > to) return null;
      const [sn, so] = M[i]; const [en, eo] = M[i + N.length - 1];
      const r = document.createRange(); r.setStart(sn, so); r.setEnd(en, eo + 1);
      return { r, i, j: i + N.length };
    }
    const hl = { ctx: [], key: [], alt: [] }; const segs = []; const errors = [];
    let cursor = 0;
    for (const s of spec.segments) {
      const a = find(s.from, cursor); if (!a) { errors.push('from not found: ' + s.from); continue; }
      const b = find(s.to, a.i); if (!b) { errors.push('to not found: ' + s.to); continue; }
      const r = document.createRange(); r.setStart(a.r.startContainer, a.r.startOffset); r.setEnd(b.r.endContainer, b.r.endOffset);
      hl.ctx.push(r); (window.__R = window.__R || []).push(r);
      for (const k of (s.keys || [])) { const f = find(k, a.i, b.j); if (f) hl.key.push(f.r); else errors.push('key not found: ' + k); }
      for (const k of (s.alts || [])) { const f = find(k, a.i, b.j); if (f) hl.alt.push(f.r); else errors.push('alt not found: ' + k); }
      // container: nearest ancestor block with decent width
      let c = r.commonAncestorContainer; if (c.nodeType === 3) c = c.parentElement;
      while (c && c.getBoundingClientRect().width < (spec.minW || 500)) c = c.parentElement;
      (window.__C = window.__C || []).push(c);
      segs.push(1);
      cursor = b.j;
    }
    for (const k of Object.keys(hl)) if (hl[k].length) CSS.highlights.set(k, new Highlight(...hl[k]));
    for (const r of (window.__R || [])) {
      let e = r.startContainer.nodeType === 3 ? r.startContainer.parentElement : r.startContainer;
      while (e && e !== document.body) {
        const cs = getComputedStyle(e);
        if (/auto|scroll|hidden/.test(cs.overflowY) && e.scrollHeight > e.clientHeight + 5) {
          e.style.setProperty('max-height', 'none', 'important'); e.style.setProperty('height', 'auto', 'important'); e.style.setProperty('overflow', 'visible', 'important');
        }
        e = e.parentElement;
      }
    }
    for (const e of document.querySelectorAll('*')) { const p = getComputedStyle(e).position; if ((p === 'fixed' || p === 'sticky') && e.getBoundingClientRect().height < 250 && !e.contains(window.__R[0].startContainer)) e.style.setProperty('visibility', 'hidden', 'important'); }
    let title = null;
    if (spec.titleSel) {
      let t = document.querySelector(spec.titleSel);
      if (t && spec.titleUp) for (let i = 0; i < spec.titleUp; i++) t = t.parentElement;
      if (t) { window.__T = t; title = 1; }
    }
    return { segs, errors, title };
  }, spec);
  if (res.errors.length) console.log(spec.id, 'ERRORS', res.errors);
  if (process.env.DEBUG) console.log(JSON.stringify(res));
  const files = [];
  const padX = 14, padY = spec.padY ?? 3;
  for (let i = 0; i < res.segs.length; i++) {
    const geo = (i) => p.evaluate((i) => {
      const r = window.__R[i], c = window.__C[i];
      const rects = [...r.getClientRects()].filter(x => x.width > 0 && x.height > 0);
      const top = Math.min(...rects.map(x => x.top)), bottom = Math.max(...rects.map(x => x.bottom));
      const cr = c.getBoundingClientRect();
      return { x: cr.left, w: cr.width, y: top, h: bottom - top, sy: scrollY };
    }, i);
    await p.evaluate((i) => { const r = window.__R[i]; const se = r.startContainer.nodeType === 3 ? r.startContainer.parentElement : r.startContainer; se.scrollIntoView({ block: 'start' }); window.scrollBy(0, -60); }, i);
    await p.waitForTimeout(200);
    let g = await geo(i);
    const vp = p.viewportSize();
    if (g.y < 0 || g.y + g.h + 40 > vp.height) {
      await p.evaluate(() => window.scrollTo(0, 0));
      const g0 = await geo(i);
      await p.setViewportSize({ width: vp.width, height: Math.min(14000, Math.ceil(g0.y + g0.h + 200)) });
      await p.waitForTimeout(500);
      await p.evaluate(() => window.scrollTo(0, 0));
      g = await geo(i);
    }
    await p.waitForTimeout(300);
    const clip = { x: Math.max(0, g.x - padX), y: Math.max(0, g.y - padY), width: g.w + 2 * padX, height: g.h + 2 * padY };
    if (process.env.DEBUG) { console.log('clip', JSON.stringify(clip)); await p.screenshot({ path: `raw/${spec.id}_debug.png` }); }
    const f = `raw/${spec.id}_seg${i + 1}.png`;
    await p.screenshot({ path: f, clip });
    files.push(f);
  }
  let tf = null;
  if (res.title) {
    tf = `raw/${spec.id}_title.png`;
    const t = await p.evaluate(() => { window.__T.scrollIntoView({ block: 'center' }); const r = window.__T.getBoundingClientRect(); return { x: r.left, y: r.top, width: r.width, height: r.height }; });
    await p.waitForTimeout(200);
    await p.screenshot({ path: tf, clip: t });
  }
  await p.close();
  return { segs: files, title: tf, errors: res.errors };
}

(async () => {
  const specs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const only = process.argv.slice(3);
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1200, height: 2600 }, deviceScaleFactor: 2, locale: 'ar' });
  await install(ctx);
  const out = fs.existsSync('raw/manifest.json') ? JSON.parse(fs.readFileSync('raw/manifest.json')) : {};
  for (const s of specs) {
    if (only.length && !only.includes(s.id)) continue;
    try { out[s.id] = await capture(ctx, s); console.log(s.id, 'ok', out[s.id].segs.length, 'segs'); }
    catch (e) { console.log(s.id, 'FAIL', e.message.split('\n')[0]); }
    fs.writeFileSync('raw/manifest.json', JSON.stringify(out, null, 1));
  }
  await b.close();
})();
