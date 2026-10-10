// Renderiza bloques de texto (p. ej. resúmenes de la API de CORE) a PNG con resaltado: node textcap.js
const { chromium } = require('playwright');
const fs = require('fs');
const BLOCKS = {
 'X-mon': { w: 1100, segs: [
  `<p><span class="c">El género literario de Qisas al-anbiya' recopila toda una suerte de narraciones de naturaleza religiosa, sacadas unas del propio acervo musulmán y otras -bajo una amplia gama de matices- que responden a un substrato literario religioso propio del entorno en que nace el Islam:</span> <span class="c">dentro de este último bloque se encuadra el relato de la conversión de Saulo, cuyo estilo y género literario responden a la técnica utilizada por los evangelistas, lo que nos lleva a pensar que <span class="k">esta narración</span> -<span class="a">acompañada de interpolaciones, glosas y omisiones de clara procedencia musulmana</span>- <span class="k">debía ser un relato que corría entre la comunidad cristiana de Damasco</span> y que, <span class="a">tras una sutil reelaboración musulmana</span>, fue recogida por Ibn Katir e incorporada a su obra.</span></p>`
 ]},
};
const CSS = `body{margin:0;background:#fff;font-family:'Georgia','Times New Roman',serif;color:#111}
.box{padding:22px 26px;font-size:27px;line-height:1.6;background:#fff}
.c{background:rgba(255,236,120,.55)} .k{background:rgba(255,170,0,.85)} .a{background:rgba(120,200,255,.6)}
p{margin:0}`;
(async () => {
  const b = await chromium.launch();
  const m = JSON.parse(fs.readFileSync('rawt/manifest.json', 'utf8'));
  for (const [id, blk] of Object.entries(BLOCKS)) {
    const files = [];
    for (let i = 0; i < blk.segs.length; i++) {
      const p = await b.newPage({ viewport: { width: blk.w, height: 400 }, deviceScaleFactor: 2 });
      await p.setContent(`<style>${CSS}</style><div class="box" id="x">${blk.segs[i]}</div>`);
      const f = `rawt/${id}_seg${i + 1}.png`;
      await (await p.$('#x')).screenshot({ path: f });
      files.push(f); await p.close();
    }
    m[id] = { segs: files, title: null, errors: [] };
  }
  fs.writeFileSync('rawt/manifest.json', JSON.stringify(m, null, 1));
  await b.close();
})();
