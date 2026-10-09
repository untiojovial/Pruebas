const { execFile } = require('child_process');
const fs = require('fs'), os = require('os'), path = require('path');
let n = 0;
function curl(url) {
  return new Promise((res) => {
    const hdr = path.join(os.tmpdir(), `h${process.pid}_${n++}.txt`);
    execFile('curl', ['-sS', '-L', '-A', 'Mozilla/5.0 (X11; Linux x86_64) Chrome/140', '--max-time', '40', '-D', hdr, url],
      { encoding: 'buffer', maxBuffer: 64 * 1024 * 1024 }, (err, stdout) => {
        let ct = 'application/octet-stream', status = 200;
        try {
          const h = fs.readFileSync(hdr, 'latin1'); fs.unlinkSync(hdr);
          const blocks = h.trim().split(/\r?\n\r?\n/); const last = blocks[blocks.length - 1];
          const m = last.match(/^content-type:\s*(.+)$/im); if (m) ct = m[1].trim();
          const s = last.match(/^HTTP\/\S+\s+(\d+)/); if (s) status = +s[1];
        } catch (e) {}
        res({ ok: !err, body: stdout, ct, status });
      });
  });
}
async function curlRetry(u) { let r; for (let k = 0; k < 4; k++) { r = await curl(u); if (r.ok && r.status < 500) return r; await new Promise(z => setTimeout(z, 1500 * (k + 1))); } return r; }
async function install(ctx, allow = ['document', 'stylesheet', 'font', 'image']) {
  await ctx.route('**/*', async (route) => {
    const req = route.request();
    const u = req.url();
    if (u.startsWith('data:') || u.startsWith('file:')) return route.continue();
    const host = (() => { try { return new URL(u).hostname; } catch (e) { return ''; } })();
    const jsOk = process.env.ALLOWJS && host.endsWith(process.env.ALLOWJS) && ['script', 'xhr', 'fetch'].includes(req.resourceType());
    if (!allow.includes(req.resourceType()) && !jsOk) return route.abort();
    const r = await curlRetry(u);
    if (!r.ok) return route.abort();
    return route.fulfill({ status: r.status, contentType: r.ct, body: r.body });
  });
}
module.exports = { install, curl };
