# -*- coding: utf-8 -*-
# Pack Trinidad–María (T). Cada sección añade sus specs.
import urllib.parse as _up, json
WS = "https://ar.wikisource.org/wiki/"
WSCSS = "html,body,*{scroll-behavior:auto!important} html body div.mw-parser-output div.soura-block.quran-KFGQPC, html body div.mw-parser-output div.soura-block.quran-KFGQPC *{font-family:'Amiri',serif!important;font-size:27px!important;line-height:2.4!important} #mw-head,#mw-panel,.vector-header-container,.vector-column-start,.mw-footer{display:none!important}"
def ws(i, sura, segs): return web(i, WS + _up.quote('سورة_' + sura), segs, css=WSCSS, minW=500)

# s1 — el Corán
add(
 ws('TQ1', 'المائدة', [sg('لقد كفر الذين قالوا ان الله هو المسيح ابن مريم قل فمن يملك', 'ومن في الارض جميعا',
     ['ان اراد ان يهلك المسيح ابن مريم وامه'])]),
 ws('TQ2', 'المائدة', [sg('لقد كفر الذين قالوا ان الله هو المسيح ابن مريم وقال المسيح', 'ثم انظر اني يوفكون',
     ['لقد كفر الذين قالوا ان الله ثالث ثلثه', 'ما المسيح ابن مريم الا رسول', 'وامه صديقه كانا ياكلان الطعام'],
     ['اعبدوا الله ربي وربكم'])]),
 ws('TQ3', 'المائدة', [sg('واذ قال الله يعيسي ابن مريم', 'انت علي كل شيء شهيد',
     ['ءانت قلت للناس اتخذوني وامي الهين من دون الله'],
     ['ما قلت لهم الا'])]),
 ws('TQ4', 'النساء', [sg('ياهل الكتب لا تغلوا في دينكم ولا تقولوا', 'وكفي بالله وكيلا',
     ['وكلمته القيه', 'ولا تقولوا ثلثه انتهوا خيرا لكم', 'سبحنه ان يكون له ولد'])]),
 ws('TQ5', 'الأنعام', [sg('وجعلوا لله شرك', 'وهو بكل شيء عليم',
     ['اني يكون له ولد ولم تكن له صحبه'])]),
 ws('TQ6', 'الجن', [sg('وانه تعلي جد ربنا', 'ما اتخذ صحبه ولا ولدا', ['ما اتخذ صحبه ولا ولدا'])]),
 ws('TQ7', 'التوبة', [sg('وقالت اليهود عزير ابن الله', 'سبحنه عما يشركون',
     ['اتخذوا احبارهم ورهبنهم اربابا من دون الله والمسيح ابن مريم'])]),
)

# ---- secciones 2–5: specs generadas desde los passages.json de las búsquedas ----
REC = {}
for _d in ('T1', 'T2', 'T3', 'T4'):
    for _p in json.load(open(f'{HP}/{_d}/passages.json')):
        REC[_p['id']] = _p
OCRCSS = "html,body,*{scroll-behavior:auto!important} pre{white-space:pre-wrap!important;font-size:19px!important;line-height:1.6!important;max-width:1100px}"
OCRAR = OCRCSS + " pre{direction:rtl!important;text-align:right!important;unicode-bidi:plaintext!important;font-family:'Amiri',serif!important;font-size:22px!important}"
def P(pid, keys=None, alts=(), drop=(), css=None, **kw):
    r = REC[pid]; u = r['url']
    ks = [k for i, k in enumerate(keys if keys is not None else r['keys']) if i not in drop]
    seg = [sg(r['from_'], r['to'], ks, alts)]
    if u.startswith(S): return sh(pid, u[len(S):], seg, **kw)
    if css is None: css = OCRCSS if u.endswith('.txt') else 'html,body,*{scroll-behavior:auto!important}'
    return web(pid, u, seg, css=css, **kw)

# s2 — comentaristas
add(P('T1-03'), P('T1-01'), P('T1-02'),
    P('T1-07'), P('T1-08'),
    P('T1-06', alts=['وزوجًا متتبَّعة بينهما'], keys=REC['T1-06']['keys'][:1] + ['الإله القديم جوهر واحد يعم ثلاثة أقانيم: أبًا والدًا غير مولود، وابنًا مولودًا غير والد،']),
    P('T1-09'), P('T1-10'),
    P('T1-11', keys=REC['T1-11']['keys'][:1] + REC['T1-11']['keys'][2:], alts=[REC['T1-11']['keys'][1]]),
    P('T1-12', keys=[], alts=REC['T1-12']['keys']),
    P('T1-15'), P('T1-16', keys=REC['T1-16']['keys'][:2], alts=[REC['T1-16']['keys'][2]]), P('T1-17', keys=[], alts=REC['T1-17']['keys']),
    P('T1-18', keys=[], alts=REC['T1-18']['keys']),
    P('T1-13', keys=[], alts=REC['T1-13']['keys']), P('T1-14'),
    P('T1-19'),
    P('T1-20', keys=[], alts=REC['T1-20']['keys']), P('T1-21'),
    P('T1-22'), P('T1-23', keys=[], alts=REC['T1-23']['keys']), P('T1-24'),
    P('T1-25', keys=[], alts=REC['T1-25']['keys']), P('T1-26'),
    P('T1-27', keys=REC['T1-27']['keys'][:1], alts=REC['T1-27']['keys'][1:]),
    P('T1-28', keys=[], alts=REC['T1-28']['keys']), P('T1-29'),
    P('T1-36'), P('T1-37', keys=[], alts=REC['T1-37']['keys']), P('T1-38'),
    P('T1-30', keys=REC['T1-30']['keys'][1:], alts=REC['T1-30']['keys'][:1]), P('T1-31'), P('T1-32'),
    P('T1-33'), P('T1-34', keys=[], alts=REC['T1-34']['keys']), P('T1-35'),
    P('T1-39'), P('T1-40'),
    P('T1-41'), P('T1-43', keys=REC['T1-43']['keys'][1:], alts=REC['T1-43']['keys'][:1] + ['واتفقوا على أن اتحاد اللاهوت بالمسيح دون مريم']), P('T1-42'),
)
# s3 — relatos, heresiógrafos, historiadores
_y = [s for s in json.load(open('rspecs.json')) if s['id'] == 'rYq3'][0]
_y = json.loads(json.dumps(_y)); _y['id'] = 'tYq3'; _y['segments'][0]['keys'] = ['فمنها قول من قال إن المسيح وأمه كانا الهين'] + _y['segments'][0]['keys']
add(_y)
add(P('T4-29'),
    P('T2-22'), P('T2-23'),
    P('T2-02', drop=(0,)),
    P('T2-38', keys=[], alts=REC['T2-38']['keys']),
    P('T2-24'), P('T2-25'), P('T2-26'),
    P('T2-04', keys=REC['T2-04']['keys'][:1], alts=REC['T2-04']['keys'][1:2]), P('T2-05', keys=REC['T2-05']['keys'][:1], alts=REC['T2-05']['keys'][1:]),
    P('T2-10', keys=[], alts=REC['T2-10']['keys']), P('T2-11', keys=[], alts=REC['T2-11']['keys']),
    P('T2-12', keys=REC['T2-12']['keys'][2:], alts=REC['T2-12']['keys'][:2]), P('T2-13'), P('T2-14', keys=REC['T2-14']['keys'][:1], alts=REC['T2-14']['keys'][1:]),
    P('T2-17'), P('T2-18'), P('T2-19'),
    P('T2-20'), P('T2-21'),
    P('T2-27'),
    P('T2-01', drop=(2,)),
    P('T2-29'), P('T2-30'),
    P('T2-36'), P('T2-37'),
    P('T2-34'), P('T2-35'),
    P('T4-24'), P('T4-25'),
)
# s4 — coliridianos
add(*[P(f'T3-0{i}') for i in range(1, 10)], P('T3-10'), P('T3-11'), P('T3-12'), P('T3-13'), P('T3-14'), P('T3-15'),
    )
# s5 — la cadena de Sayf
add(P('T4-05'), P('T4-07'), P('T4-08'), P('T4-09'), P('T4-10'), P('T4-11'), P('T4-16'), P('T4-17'), P('T4-12'), P('T4-13'), P('T4-15'))
