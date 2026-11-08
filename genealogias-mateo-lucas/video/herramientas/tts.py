import certifi, asyncio, json, os, subprocess, sys
certifi.where = lambda: '/root/.ccr/ca-bundle.crt'
import edge_tts
sys.path.insert(0,'.')
from script import SCENES, VOICES
os.makedirs('aud',exist_ok=True)
async def one(key,spk,text):
    mp3=f'aud/{key}.mp3'; js=f'aud/{key}.json'
    if os.path.exists(js) and os.path.getsize(mp3)>0: return
    v,r,p=VOICES[spk]
    for attempt in range(4):
        try:
            c=edge_tts.Communicate(text,v,rate=r,pitch=p,boundary='WordBoundary')
            words=[]
            with open(mp3,'wb') as f:
                async for ch in c.stream():
                    if ch['type']=='audio': f.write(ch['data'])
                    elif ch['type']=='WordBoundary': words.append((ch['offset']/1e7,ch['duration']/1e7,ch['text']))
            json.dump(words,open(js,'w'),ensure_ascii=False); return
        except Exception as e:
            print('retry',key,e); await asyncio.sleep(2*(attempt+1))
async def main():
    for si,s in enumerate(SCENES):
        for gi,(spk,text) in enumerate(s['segs']):
            await one(f'{si:02d}_{gi}',spk,text)
asyncio.run(main())
tot=0
for f in sorted(os.listdir('aud')):
    if f.endswith('.mp3'):
        subprocess.run(['ffmpeg','-y','-loglevel','error','-i','aud/'+f,'-ar','48000','-ac','1','aud/'+f[:-4]+'.wav'])
        d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0','aud/'+f[:-4]+'.wav'],capture_output=True,text=True).stdout)
        tot+=d
print('total seconds',round(tot,1),'min',round(tot/60,2))
