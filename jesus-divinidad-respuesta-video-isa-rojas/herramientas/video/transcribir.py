from faster_whisper import WhisperModel
import sys
m = WhisperModel('large-v3', device='cpu', compute_type='int8')
segs, info = m.transcribe('audio.wav', language='es', vad_filter=True, beam_size=5)
out = []
for s in segs:
    out.append(f'[{s.start:7.1f} - {s.end:7.1f}] {s.text.strip()}')
    print(out[-1], flush=True)
open('transcripcion.txt', 'w', encoding='utf-8').write('\n'.join(out))
