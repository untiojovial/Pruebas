import certifi, asyncio, json, os, subprocess, sys, hashlib
certifi.where = lambda: '/root/.ccr/ca-bundle.crt'
import edge_tts
os.chdir(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, '.')
from script3 import SCENES, VOICE, clean
def hkey(text):
    v, r, p = VOICE; return hashlib.sha1(f'{v}|{r}|{p}|{text}'.encode()).hexdigest()[:12]
async def one(text):
    key = hkey(text); mp3 = f'audh/{key}.mp3'; js = f'audh/{key}.json'
    if os.path.exists(js) and os.path.getsize(mp3) > 0: return
    v, r, p = VOICE
    for attempt in range(5):
        try:
            c = edge_tts.Communicate(text, v, rate=r, pitch=p, boundary='WordBoundary'); words = []
            with open(mp3, 'wb') as f:
                async for ch in c.stream():
                    if ch['type'] == 'audio': f.write(ch['data'])
                    elif ch['type'] == 'WordBoundary': words.append((ch['offset'] / 1e7, ch['duration'] / 1e7, ch['text']))
            json.dump(words, open(js, 'w'), ensure_ascii=False); return
        except Exception as e:
            print('retry', key, e); await asyncio.sleep(2 * (attempt + 1))
async def main():
    for s in SCENES:
        for k, text, src in s['segs']: await one(clean(text))
asyncio.run(main())
tot = 0
for s in SCENES:
    for k, text, src in s['segs']:
        key = hkey(clean(text))
        if not os.path.exists(f'audh/{key}.wav'):
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'audh/{key}.mp3', '-ar', '48000', '-ac', '1', f'audh/{key}.wav'])
        tot += float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f'audh/{key}.wav'], capture_output=True, text=True).stdout)
print('total seconds', round(tot, 1), 'min', round(tot / 60, 2))
