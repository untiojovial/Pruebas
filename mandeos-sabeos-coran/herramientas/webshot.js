const { chromium } = require('playwright');
const jobs = JSON.parse(process.argv[2]);
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({viewport:{width:760,height:1300}, deviceScaleFactor:2, locale:'en-US', userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'});
  for (const j of jobs) {
    const p = await ctx.newPage();
    try {
      await p.goto(j.url,{timeout:60000, waitUntil:'networkidle'}).catch(()=>{});
      await p.waitForTimeout(2500);
      const box = await p.evaluate((subs) => {
        let first=null;
        for (const sub of subs) {
          const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
          let n;
          while((n=w.nextNode())){
            const i=n.nodeValue.indexOf(sub);
            if(i>=0){
              const r=document.createRange(); r.setStart(n,i); r.setEnd(n,i+sub.length);
              const m=document.createElement('mark'); m.style.background='#ffe066'; m.style.boxShadow='0 3px 0 #d9822b';
              try{ r.surroundContents(m);}catch(e){}
              if(!first) first=m; break;
            }
          }
        }
        if(!first) return null;
        first.scrollIntoView({block:'center'});
        const el = first.closest('div,section,article,p') || first;
        const rr=first.getBoundingClientRect();
        return {y:rr.top, h:rr.height};
      }, j.subs);
      await p.waitForTimeout(600);
      if (!box) { console.log(j.out,'NOT FOUND'); }
      const y0 = box ? Math.max(0, box.y - (j.above||420)) : 0;
      await p.screenshot({path:j.out, clip:{x:0,y:y0,width:760,height:Math.min(1300-y0, j.h||900)}});
      console.log(j.out, box ? 'ok' : 'no-mark');
    } catch(e){ console.log(j.out,'ERR',e.message.slice(0,120)); }
    await p.close();
  }
  await b.close();
})();
