const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + path.resolve(process.argv[2]), { waitUntil: 'load' }); await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: process.argv[3], format: 'A4', printBackground: true, displayHeaderFooter: true,
    headerTemplate: '<div></div>', footerTemplate: '<div style="font-size:8px;color:#777;width:100%;text-align:center;font-family:serif">Mahoma y los ídolos antes de la revelación · <span class="pageNumber"></span>/<span class="totalPages"></span></div>',
    margin: { top: '18mm', bottom: '18mm', left: '17mm', right: '17mm' } }); await b.close(); })();
