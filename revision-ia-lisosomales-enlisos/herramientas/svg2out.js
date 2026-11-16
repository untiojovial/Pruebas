// Convierte un SVG en PDF vectorial y PNG con Chromium.  Uso: node svg2out.js figura.svg ANCHO ALTO
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const [svgPath, w, h] = [process.argv[2], +process.argv[3], +process.argv[4]];
  const base = svgPath.replace(/\.svg$/, '');
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
  const p = await ctx.newPage();
  await p.setContent(`<html><body style="margin:0">${fs.readFileSync(svgPath, 'utf8')}</body></html>`);
  await p.screenshot({ path: base + '.png', clip: { x: 0, y: 0, width: w, height: h } });
  await p.pdf({ path: base + '.pdf', width: w + 'px', height: h + 'px', printBackground: true, pageRanges: '1' });
  await b.close();
})();
