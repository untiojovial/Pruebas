// Usage: node webshot.js config.json   (config: [{url, vw, shots:[{out, marks:[{t, c}], ctx:[phrases whose blocks define the clip], pad}]}])
const { chromium } = require('/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/caps/node_modules/playwright');
const fs = require('fs');
const cfg = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
(async () => {
  const proxy = process.env.HTTPS_PROXY; const opts = { headless: true };
  if (proxy) { const u = new URL(proxy); opts.proxy = { server: `${u.protocol}//${u.host}`, username: decodeURIComponent(u.username), password: decodeURIComponent(u.password) }; }
  const b = await chromium.launch(opts);
  for (const page of cfg) {
    const ctx = await b.newContext({ ignoreHTTPSErrors: true, viewport: { width: page.vw || 1000, height: 1500 }, deviceScaleFactor: 1.5 });
    const p = await ctx.newPage();
    let ok = false; for (let t = 0; t < 4 && !ok; t++) { try { await p.goto(page.url, { waitUntil: 'domcontentloaded', timeout: 90000 }); ok = true; } catch (e) { console.log('retry', t, e.message.slice(0, 60)); await new Promise(r => setTimeout(r, 4000 * (t + 1))); } }
    if (!ok) { console.log('PAGE FAIL', page.url); await ctx.close(); continue; }
    await p.waitForTimeout(2500);
    // remove sticky/cookie overlays
    await p.addStyleTag({ content: 'header, nav, .cookie, [class*=cookie], [id*=cookie], [class*=banner], [class*=popup], [class*=modal], [class*=newsletter], [class*=subscribe]{display:none !important} *{scroll-behavior:auto !important}' });
    let si = 0; for (const shot of page.shots) { si++;
      const res = await p.evaluate(({ marks, ctxp, si }) => {
        const norm = s => s.replace(/[‘’ʼ]/g, "'").replace(/[“”]/g, '"').replace(/ /g, ' ').replace(/\s+/g, ' ');
        const blocks = Array.from(document.querySelectorAll('p,li,blockquote,h1,h2,h3,h4,figcaption,dd,div'))
          .filter(e => !Array.from(e.children).some(c => ['P','LI','BLOCKQUOTE','DIV','H1','H2','H3','H4'].includes(c.tagName)));
        const found = [];
        const missing = [];
        function markIn(el, phrase, color) {
          const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
          const nodes = []; let n; while ((n = walker.nextNode())) nodes.push(n);
          let raw = ''; const starts = [];
          for (const nd of nodes) { starts.push(raw.length); raw += nd.nodeValue; }
          // normalized string with mapping
          let ns = ''; const map = [];
          let prevSpace = false;
          for (let i = 0; i < raw.length; i++) {
            let ch = raw[i];
            if (/[‘’ʼ]/.test(ch)) ch = "'"; else if (/[“”]/.test(ch)) ch = '"'; else if (ch === ' ') ch = ' ';
            if (/\s/.test(ch)) { if (prevSpace) continue; ch = ' '; prevSpace = true; } else prevSpace = false;
            ns += ch; map.push(i);
          }
          const target = norm(phrase).trim();
          const idx = ns.indexOf(target);
          if (idx < 0) return false;
          const rs = map[idx], re = map[idx + target.length - 1] + 1;
          // wrap overlapping nodes
          for (let k = nodes.length - 1; k >= 0; k--) {
            const nd = nodes[k]; const s0 = starts[k], e0 = s0 + nd.nodeValue.length;
            const a = Math.max(rs, s0), z = Math.min(re, e0);
            if (a >= z) continue;
            const range = document.createRange(); range.setStart(nd, a - s0); range.setEnd(nd, z - s0);
            const m = document.createElement('mark'); m.style.cssText = `background:${color};color:#111;padding:0 1px;text-decoration:underline;text-decoration-color:#e07a00;text-decoration-thickness:2px;text-underline-offset:3px`;
            m.dataset.s = String(si); range.surroundContents(m);
          }
          return true;
        }
        for (const m of marks) {
          const target = norm(m.t).trim();
          const el = blocks.find(e => norm(e.textContent).includes(target));
          if (!el) { missing.push(m.t.slice(0, 50)); continue; }
          markIn(el, m.t, m.c || '#ffe066');
          found.push(el);
        }
        const ctxEls = [];
        for (const t of ctxp) {
          const target = norm(t).trim();
          const el = blocks.find(e => norm(e.textContent).includes(target));
          if (el) ctxEls.push(el); else missing.push('ctx:' + t.slice(0, 40));
        }
        const marksEls = Array.from(document.querySelectorAll('mark'));
        if (!found.length) return { missing };
        const first = marksEls.find(m => m.dataset.s === String(si));
        if (!first) return { missing };
        first.scrollIntoView({ block: 'center' });
        return { missing, ok: true };
      }, { marks: shot.marks || [], ctxp: shot.ctx || [], si });
      if (!res.ok) { console.log('SHOT FAIL', shot.out, JSON.stringify(res.missing)); continue; }
      await p.waitForTimeout(300);
      const box = await p.evaluate((si) => {
        const rs = Array.from(document.querySelectorAll('mark')).filter(m => m.dataset.s === String(si)).map(m => m.getBoundingClientRect()).filter(r => r.height > 0 && r.top > -2000 && r.top < 3000);
        let x0 = 1e9, y0 = 1e9, x1 = 0, y1 = 0;
        for (const r of rs) { x0 = Math.min(x0, r.left); y0 = Math.min(y0, r.top); x1 = Math.max(x1, r.right); y1 = Math.max(y1, r.bottom); }
        return [x0, y0, x1, y1, window.innerWidth, window.innerHeight];
      }, si);
      const padY = shot.padY || 90, padX = shot.padX || 60;
      let [x0, y0, x1, y1, iw, ih] = box;
      x0 = Math.max(0, x0 - padX); x1 = Math.min(iw, x1 + padX); y0 = Math.max(0, y0 - padY); y1 = Math.min(ih, y1 + padY);
      await p.screenshot({ path: shot.out, clip: { x: x0, y: y0, width: x1 - x0, height: y1 - y0 } });
      console.log('shot', shot.out, 'missing:', JSON.stringify(res.missing));
    }
    await ctx.close();
  }
  await b.close();
})().catch(e => { console.error('ERR', e.message); process.exit(1); });
