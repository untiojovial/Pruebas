import base64, sys, pathlib
B = pathlib.Path(sys.argv[1]); html = (B/'informe.html').read_text(encoding='utf8')
def face(fam, f, w='normal', st='normal'):
    return "@font-face{font-family:'%s';src:url(data:font/ttf;base64,%s) format('truetype');font-weight:%s;font-style:%s;}" % (fam, base64.b64encode((B/'fonts'/f).read_bytes()).decode(), w, st)
fonts = face('Amiri','Amiri-Regular.ttf') + face('Amiri','Amiri-Bold.ttf','700') + face('Lora','Lora[wght].ttf','400 700') + face('Lora','Lora-Italic[wght].ttf','400 700','italic')
(B/'informe_build.html').write_text(html.replace('/*FONTS*/', fonts), encoding='utf8')
