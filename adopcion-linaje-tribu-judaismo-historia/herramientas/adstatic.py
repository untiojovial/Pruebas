# -*- coding: utf-8 -*-
# Diapositivas generales: AD00 (presentación), AD00b/AD00c (índice de las 34 pruebas) y AD99 (fuentes y licencias)
import sys, os, shutil
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/ad')
import adcards
from adcards import E, TAGNAME, SCOPE, PACK, OUT, page, chips
import adspec
from PIL import Image
os.makedirs(OUT + '/img', exist_ok=True)
im = Image.open('/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/ad/A2/dl/img_rembrandt_jacob_blessing_joseph_sons.jpg').convert('RGB')
im.thumbnail((1000, 1000)); im.save(OUT + '/img/rembrandt.jpg', quality=90)
CARDS = adspec.CARDS
GROUPS = [('A', 'Adopción y herencia tribal: Efraín y Manasés y otros casos', 'AD01–AD09, AD13–AD15, AD19, AD34'),
          ('B', 'Principio rabínico: «como si lo hubiera engendrado»', 'AD10–AD12'),
          ('E', 'Levirato y filiación legal: el nombre y la heredad del muerto', 'AD16–AD20, AD33'),
          ('C', 'Incorporación a una tribu o a un linaje', 'AD21–AD23'),
          ('G', 'Historia: derecho antiguo (Babilonia, Atenas, Roma)', 'AD24–AD31'),
          ('J', 'Jesús, José y David: Mateo, Africano y Agustín', 'AD32–AD34')]
n = {g: sum(1 for c in CARDS if g in c['tags']) for g, _, _ in GROUPS}
rows = ''.join(f'<tr><td><span class="tg tg{g}">{E(TAGNAME[g])}</span></td><td>{E(t)}</td><td style="white-space:nowrap">{E(r)}</td><td style="text-align:center;font-weight:700">{n[g]}</td></tr>' for g, t, r in GROUPS)
body = f'''<div style="display:grid;grid-template-columns:430px 1fr;gap:22px;align-items:start">
<div><img src="img/rembrandt.jpg" style="width:100%;border-radius:10px;border:1px solid #cfd6e2"><div style="font-size:13px;color:#566079;margin-top:6px;line-height:1.4">Rembrandt, «Jacob bendice a los hijos de José» (1656). Wikimedia Commons, «Rembrandt - Jacob Blessing the Children of Joseph - WGA19117.jpg», dominio público.</div></div>
<div>
<div class="ans"><b>La pregunta.</b> ¿Atribuían el judaísmo antiguo y la historia del derecho familia, nombre, herencia, linaje o tribu a quien era adoptado o tenido por hijo por ley? Este pack recoge <b>34 pruebas</b>: del Tanaj, los targumim, el Talmud y el Midrás, de Josefo, de leyes y autores de Babilonia, Atenas y Roma, y de dos textos cristianos antiguos sobre José y la genealogía de Jesús. Cada una tiene su <b>texto original</b> y su <b>traducción al español</b> con «qué demuestra».</div>
<div class="pn" style="margin-bottom:12px"><h4>Cómo leer las tarjetas</h4><p style="font-size:17.5px;line-height:1.5">Amarillo = pasaje citado; naranja = frase clave. Etiqueta de alcance: <b>Texto directo</b> (el texto mismo habla de un adoptado o hijo legal), <b>Institución análoga</b> (levirato, crianza, incorporación) y <b>Contexto histórico</b>.</p></div>
</div></div>
<table class="v" style="margin-top:10px"><tr><th>Grupo</th><th>Contenido</th><th>Tarjetas</th><th>N.º</th></tr>{rows}</table>
<div class="pn" style="margin-top:12px"><h4>Selección</h4><p style="font-size:17px;line-height:1.5">Es una <b>selección de textos favorables</b>, cada uno comprobado contra la página de la que procede; no recoge los textos que apuntan en otro sentido. Las limitaciones y los textos en contra que encontraron los investigadores están en el README del repositorio.</p></div>'''
page(OUT, 'AD00_es', 'AD00', 'Adopción, linaje y tribu', 'Resumen en español',
     'Adopción, linaje y tribu: lo que dicen el judaísmo y la historia',
     'Ocho investigadores buscaron las fuentes; cada texto mostrado lo comprobé contra su página de origen.', body,
     'Traducciones al español mías. Fechas aproximadas.<br>' + PACK, head_cls='alt')

def idx(fname, cid, kind, part):
    tr = ''
    for c in part:
        sc = f'<span class="sc">{E(SCOPE[c["scope"]])}</span>'
        tg = ''.join(f'<span class="tg tg{x}">{E(TAGNAME[x])}</span>' for x in c['tags'])
        tr += f'<tr><td class="who">{c["id"]}</td><td>{E(c["title"])}</td><td>{tg}</td><td>{sc}</td></tr>'
    body = f'<table class="v"><tr><th style="width:70px">Código</th><th>Fuente y qué dice</th><th style="width:250px">Grupo</th><th style="width:170px">Alcance</th></tr>{tr}</table>'
    page(OUT, fname, cid, 'Índice de pruebas', kind, 'Índice de las 34 pruebas' + f' ({part[0]["id"]}–{part[-1]["id"]})',
         'Cada prueba tiene una diapositiva con el texto original y otra con la traducción al español.', body,
         'Cada código ADxx corresponde a ADxx_or.png (original) y ADxx_es.png (español).<br>' + PACK, head_cls='alt')
idx('AD00b_es', 'AD00b', 'Resumen en español', CARDS[:17])
idx('AD00c_es', 'AD00c', 'Resumen en español', CARDS[17:])

body = '''<div class="two">
<div class="pn"><h4>Qué leí y cómo se comprobó</h4><ul class="l" style="font-size:17.5px">
<li>Ocho investigadores (modelo pequeño, uno por tema) buscaron los textos; <b>comprobé yo</b>, con un script, que cada texto mostrado (hebreo, arameo, griego, latín o inglés) aparece letra por letra en la página de la que procede.</li>
<li>Hebreo: <i>Miqra according to the Masorah</i> y Talmud de Wikisource (ed. Vilna) vía Sefaria (CC BY-SA); Rashi, targumim y Tanjumá (Sefaria, dominio público).</li>
<li>Griego y latín: Perseids, The Latin Library; Mateo: SBLGNT (CC BY 4.0).</li>
<li>Traducciones inglesas de dominio público: JPS 1917, Whiston (Josefo), King (Hammurabi), Moyle (Justiniano), Church y Brodribb (Tácito), Thomson (Suetonio), McGiffert y Schaff (NPNF), Etheridge (targumim).</li>
</ul></div>
<div class="pn"><h4>Límites y derechos</h4><ul class="l" style="font-size:17.5px">
<li><b>Traducciones al español mías.</b> Del Talmud y de los textos hebreos y arameos traduje directamente del original; del resto, desde el original cuando se muestra y con la traducción inglesa como apoyo.</li>
<li><b>Solo leí en inglés</b> a Josefo, Hammurabi, Africano y Agustín (griego, acadio y latín no consultados).</li>
<li>Los <b>Loeb de 1927</b> (Iseo, Gelio) son de dominio público en EE. UU. desde 2023 por su fecha; las páginas de origen no declaran licencia.</li>
<li><b>Fechas aproximadas</b> (convencionales); no las verifiqué una a una.</li>
<li>Es una <b>selección de textos favorables</b>; los textos en sentido contrario y las limitaciones de cada fuente están en el README.</li>
</ul></div></div>'''
page(OUT, 'AD99_es', 'AD99', 'Fuentes, licencias y límites', 'Resumen en español',
     'Fuentes leídas, licencias y límites',
     'Resumen del método y de los derechos de los textos mostrados.', body,
     'Textos citados en extractos breves, con su fuente. Sefaria: https://www.sefaria.org · Perseids: https://cts.perseids.org · The Latin Library · Project Gutenberg · New Advent · Avalon Project.<br>' + PACK, head_cls='alt')
print('adstatic ok')
