const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1300, height: 900 }, deviceScaleFactor: 1.25 });
  const files = process.argv.slice(2).length ? process.argv.slice(2) : fs.readdirSync("wcards").filter(f => f.endsWith('.html')).map(f => 'wcards/' + f);
  for (const f of files) {
    await p.goto('file://' + path.resolve(f));
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(150);
    await p.locator('.card').screenshot({ path: f.replace('.html', '.png') });
    console.log('rendered', f);
  }
  await b.close();
})();
