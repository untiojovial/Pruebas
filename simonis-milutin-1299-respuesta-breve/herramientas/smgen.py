# -*- coding: utf-8 -*-
# Simonis & Milutin: six short English slides (SM01-SM06)
import sys, os
SM = '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/sm'
sys.path.insert(0, '/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/hb')
import hbcss
from hbcss import E, marks, page
hbcss.CSS += """
.qb{border-left:5px solid #fca311;background:#fbf8ee;padding:10px 16px;margin:9px 0;font-family:'Bitstream Charter','DejaVu Serif',serif;font-size:16.5px;line-height:1.5;color:#1b2333;border-radius:0 7px 7px 0}
.qb mark.k{background:#ffd36b}
.pnh{font-size:13px;letter-spacing:.07em;text-transform:uppercase;color:#3b4660;font-weight:700;margin-bottom:2px}
.pns{font-size:14px;color:#566079;margin-bottom:6px;line-height:1.35}
.rd{border-left:6px solid #14213d;background:#eef1f8;padding:12px 20px;border-radius:0 8px 8px 0;font-size:17px;line-height:1.5;margin-top:14px}
.rd ol{margin:4px 0 0 20px}.rd li{margin:3px 0}
table.v td.g{font-family:'FreeSerif','DejaVu Serif',serif;font-size:16.5px;line-height:1.45;color:#1b2333}
table.v td.en{font-size:15px;line-height:1.45}
table.v td.en .tk{display:block;margin-top:4px;font-weight:700;color:#14213d;font-size:14px}
table.v td.src{font-size:14px;line-height:1.4;color:#2f3a52}
.st-ok{color:#1d7a4f;font-weight:700}.st-no{color:#b44a2f;font-weight:700}.st-md{color:#9a6a00;font-weight:700}
.sy2{border:1px solid #d6dbe4;border-radius:10px;overflow:hidden;margin-bottom:10px}
.sy2 .t{background:#14213d;color:#fff;font-weight:700;font-size:14px;padding:5px 14px;letter-spacing:.05em;text-transform:uppercase}
.sy2 .b{padding:9px 16px;font-size:16.5px;line-height:1.48;background:#fff}
"""
OUT = SM + '/smcards'
PACK = 'Simonis and Milutin (1299): a short reply to two book pages'
KIND = 'Short reply'

# ------------------------------------------------------------------ SM01
body = '''<div class="ans"><b>The marriage is a documented fact and needs no denial.</b> But the very pages shown say it <mark class="k">violated Church rules</mark>, and that the court had to get round the objection with <mark class="k">a clever loophole</mark>. Byzantine law set minimum marriage ages (Justinian: 12 for girls, 14 for boys; Ecloga: 13 and 15), and Gregoras says Simonis was to be raised in Milutin’s household <mark class="k">until the customary time of marriage</mark>. The Church’s eventual concession was a political climb-down by rulers and clergy, a fair criticism of them, not a Christian rule that five-year-olds may marry. Only one chronicler, Gregoras, reports abuse, at age eight, and he does not date it to the wedding.</div>
<div class="two">
<div class="pn"><h4>What the sources do establish</h4><ul class="l" style="font-size:16.5px">
<li>Simonis was five when offered (Gregoras; Pachymeres: <i>not yet past her sixth year</i>); Milutin was in his forties (Gregoras: forty) or, per Kaldellis, fifty.</li>
<li>The Church objected (Fine: <i>too young</i> and a fourth marriage); Pachymeres lists her immaturity among the obstacles and says the patriarch was bypassed.</li>
<li>It was overridden for a peace treaty: the argument <i>at least officially satisfied the Church</i> (Fine).</li>
<li>Milutin is venerated as a saint (OCA, 30 October).</li>
<li>Gregoras: intercourse when she was eight, injuring her womb.</li>
</ul></div>
<div class="pn"><h4>What they do not establish</h4><ul class="l" style="font-size:16.5px">
<li><b>That Orthodox teaching prescribed or allowed child marriage.</b> Law and canons set higher ages, and both authors say the marriage broke Church rules.</li>
<li><b>That anyone argued a five-year-old could properly be wed.</b> The loophole answers only the fourth-marriage objection; for her age the plan was to wait.</li>
<li><b>That abuse happened “immediately”</b> (Kaldellis, citing <i>some sources</i>). The only source I found is Gregoras: age eight, no date for the wedding.</li>
</ul></div></div>
<div class="rd" style="margin-top:14px"><b>Fair concessions.</b> The Church did give way, and Milutin was later made a saint; “the Church rejected it completely” would be too strong. The claim that survives is narrower: this was a rulers’ act, not a doctrine. Details, sources and limits in SM02–SM06.</div>'''
page(OUT, 'SM01', 'SM01', 'Simonis & Milutin', KIND,
     'Simonis and Milutin, 1299: what the two pages prove, and what they don’t',
     'Reply to Kaldellis, A Cabinet of Byzantine Curiosities (Oxford UP), p. 12, and Fine, The Late Medieval Balkans (Univ. of Michigan Press), p. 222', body,
     PACK + '<br>Quotations in the highlighted phrases are from the photographed pages, transcribed by me.', head_cls='alt')

# ------------------------------------------------------------------ SM02
body = '''<div class="two">
<div><div class="pnh">Kaldellis, <i>A Cabinet of Byzantine Curiosities</i>, p. 12</div>
<div class="pns">Oxford UP; a popular book of “strange tales and surprising facts”. The photographed passage is a single paragraph.</div>
<div class="qb">She was five years old and Milutin was fifty, but the real problem was that he had already married three times, so this would be his fourth, which <mark class="k">violated Church rules</mark>. The court came up with <mark class="k">a clever loophole</mark>: as wife #1 had been alive when Milutin took wives #2 and #3, the latter had not been real wives after all. But wife #1 had died in the meantime, which meant that Milutin was now free to marry Simonis as wife #2.</div>
<div class="qb">The question of her age was apparently not important. <mark class="k">According to some sources</mark>, Milutin immediately consummated the marriage, leaving Simonis unable to bear children.</div></div>
<div><div class="pnh">Fine, <i>The Late Medieval Balkans</i>, p. 222</div>
<div class="pns">University of Michigan Press; a scholarly survey of the period.</div>
<div class="qb">The only available bride fitting the bill was Andronicus’ five-year-old daughter Simonida. So, Andronicus offered her to Milutin. At this point the negotiations, already threatened by serious opposition in Serbia, acquired <mark class="k">strong resistance from the Byzantine Church</mark>.</div>
<div class="qb">… the Byzantine Church felt the proposed marriage between Simonida and Milutin <mark class="k">violated Church canons</mark>. Not only was she too young, but fourth marriages were completely forbidden by the Church, and she was about to become Milutin’s fourth wife. The Byzantine court eventually overcame this objection with <mark class="k">an elegant piece of sophistry</mark>. Since Milutin’s first wife had been alive at the time he contracted marriages two and three, those two marriages were in fact not marriages at all. However, now in 1299, since by then wife number one had died, Simonida could go to Serbia and become the second wife of the lonely widower. <mark class="k">This reasoning at least officially satisfied the Church</mark>, so the marriage was carried out and the peace concluded.</div></div></div>
<div class="rd"><b>Read closely.</b><ol>
<li>Both authors call it a breach of Church rules or canons. On the central point the photos support the reply, not the attack.</li>
<li>The “loophole” answers only the fourth-marriage objection. Neither page reports an argument that a five-year-old could properly be married.</li>
<li>They differ on age: Fine lists <i>too young</i> among the Church’s objections; Kaldellis says it was <i>apparently not important</i>, to the court.</li>
<li>“Immediately” is Kaldellis’ wording of what <i>some sources</i> say; his endnote is not in the photo. The only source I found for any consummation is Gregoras (SM03).</li></ol></div>'''
page(OUT, 'SM02', 'SM02', 'Simonis & Milutin', KIND,
     'The two pages, transcribed',
     'Highlighted passages as in the photos; words marked in orange are the ones that matter', body,
     PACK + '<br>Transcribed by me from the photos you sent (the photos carry a TikTok watermark). Fine’s 1987 first edition and its later reprint are not distinguished here.', head_cls='alt')

# ------------------------------------------------------------------ SM03
R = [
 ('<b>Pachymeres</b> (contemporary; d. c. 1310), <i>De Andronico Palaeologo</i>, Bonn ed. II, <b>p. 273</b>',
  'ζῶσα γὰρ ἡ προτέρα τὰς ἐπιγενομένας παρανόμους ἀπήλεγχεν … ἡ προτέρα τεθνηκυῖα ἠκούετο … τῶν ἐν τῷ μεταξὺ ὡς νόθων ἀπηλλοτριωμένων',
  'For while the first wife lived she showed the later ones to be unlawful … it was reported that the first had died … the ones in between being set aside as illegitimate.<span class="tk">→ The “loophole”, in a contemporary’s words.</span>'),
 ('<b>Pachymeres</b>, Bonn II, <b>p. 275</b> (§31)',
  'ἦν οὖν πάνυ ἀστεῖον τοῦτο τὸ θυγάτριον, οὔπω τὸν ἕκτον παραλλάττον ἐνιαυτόν',
  'This little daughter was very charming, not yet past her sixth year.<span class="tk">→ Her age when the match was made.</span>'),
 ('<b>Pachymeres</b>, Bonn II, <b>pp. 279–280</b>',
  'ἥ τ᾽ ἀφηλικίωσις τῆς νεάνιδος … οὔτ᾽ ἐκοινοῦτο τῷ πατριάρχῃ τὴν πρᾶξιν … πατριάρχης δ᾽ αὖθις ὑβριοπαθῶν ἴσως ὑπερφρονούμενος',
  '… the girl’s immaturity [one of the obstacles the emperor weighed] … nor did he consult the patriarch about the affair … and the patriarch, in turn, felt insulted, perhaps at being disregarded.<span class="tk">→ The patriarch was bypassed, not persuaded.</span>'),
 ('<b>Gregoras</b> (mid-14th c.), <i>Historia</i> VI.9, Bonn I, <b>p. 203</b>',
  'πέμπτον τῆς ἡλικίας ἀγούσης ἔτος, ἵν᾽ ὑπ᾽ ἐκείνῳ λαβόντι τρέφοιτο, μέχρις ἂν ἐς τὸν νομιζόμενον ἔλθῃ τοῦ γάμου χρόνον κἄπειτα εἴη σύζυγος αὐτῷ',
  '… in her fifth year, so that, taken in by him, she might be raised until she reached the customary time of marriage, and then be his wife.<span class="tk">→ The formal plan was to wait. No “twelve” is named.</span>'),
 ('<b>Gregoras</b>, VII.5, Bonn I, <b>p. 243</b>',
  'τῇ μὲν γὰρ θυγατρὶ ὀκταετεῖ πλέον ἢ τετταρακον[…]της ὁ Κράλης μιγεὶς βλαβῆναι τὴν ταύτης πέπραχε μήτραν, ὡς μηδὲ γονὴν ἐξ ἐκείνης ἔτι δύνασθαι γίγνεσθαι',
  'For the Kral, more than forty years old, having had intercourse with the eight-year-old daughter, brought it about that her womb was injured, so that no offspring could any longer come from her.<span class="tk">→ The abuse allegation: age eight, no date given for the wedding.</span>'),
]
tr = ''.join(f'<tr><td class="src">{a}</td><td class="g">{E(g)}</td><td class="en">{e}</td></tr>' for a, g, e in R)
body = f'''<table class="v" style="table-layout:fixed"><tr><th style="width:190px">Source</th><th style="width:470px">Greek (Bonn edition, page image)</th><th>English (my translation)</th></tr>{tr}</table>
<div class="rd"><b>Weight and discrepancies.</b> Pachymeres is a contemporary and, in the pages read, says nothing of intercourse or injury. Gregoras wrote decades later and is the only source I found for the abuse. He also calls her an infant (<span class="gr" style="font-size:17px">βρέφος</span>, p. 204) when she left for Serbia and gives Milutin’s age as forty, “about five years older” than the emperor, not fifty. Neither discrepancy excuses the marriage; both are worth knowing before quoting Kaldellis’ round figures.</div>'''
page(OUT, 'SM03', 'SM03', 'Simonis & Milutin', KIND,
     'What the fourteenth-century chroniclers actually say',
     'Pachymeres and Gregoras, Greek text with my translation; the lines in the table were read on the page images', body,
     PACK + '<br>Pachymeres, <i>De Michaele et Andronico Palaeologis</i>, ed. I. Bekker, vol. 2 (Bonn, 1835); Gregoras, <i>Byzantina historia</i>, ed. Schopen–Bekker, vol. 1 (Bonn, 1829); scans on archive.org. The smudge in the p. 243 line hides two letters of “forty”.', head_cls='alt')

# ------------------------------------------------------------------ SM04
T = [
 ('Justinian, <i>Institutes</i> 1.22 pr.', 'Puberty in males “immediately on the completion of the fourteenth year”; females “fit for marriage after completing their twelfth year”.', 'Sandars transl. (1876)', '<span class="st-ok">Verified.</span> The guide cited 1.10, which gives no number.'),
 ('<i>Digest</i> 23.2.4 (Pomponius)', 'A girl married under twelve becomes a lawful wife only once she has completed twelve years with her husband.', 'Latin text; my translation', '<span class="st-ok">Verified.</span> Note: this tolerated a child bride in the husband’s house but made twelve the threshold.'),
 ('<i>Digest</i> 23.1.14 (Modestinus)', 'Betrothal is valid if neither party is younger than seven.', 'Latin text; my translation', '<span class="st-ok">Verified.</span> Simonis (five) was below it; whether later Byzantine codes kept the rule, not checked.'),
 ('<i>Ecloga</i> (726), tit. II', '“for a man at fifteen and for a woman at thirteen years of age”.', 'Freshfield (1926), via Fordham; Greek in Zachariä (1852)', '<span class="st-ok">Verified</span> in both.'),
 ('<i>Prochiron</i> (c. 870)', 'Marriage ages: not read. Its marriage title is, per the 1895 concordance, taken from the Ecloga (15/13); tit. VI.1 uses 14/12 for minors’ wills.', 'Brandileone–Puntoni (1895)', '<span class="st-no">Not confirmed.</span> The guide’s “12/14” is not in what I could read.'),
 ('Milaš, <i>Orthodox Church Law</i> §181', '“The Church adopted these years [14 and 12] for marriage, and made them law through several synodal decisions.”', 'English text on a web site', '<span class="st-md">As stated by Milaš.</span> His cite “Prochiron IV, 2” points to a chapter on dowry.'),
 ('Meyendorff, <i>Dumbarton Oaks Papers</i> 44 (1990), p. 103', '“The minimum age for marriage was fixed … to fourteen for men and twelve for women, but diplomatic requirements sometimes made this rule flexible.” And: Milutin married Simonis “when she was only five (1299)”.', 'DOP 44, p. 103', '<span class="st-ok">Verified.</span> An Orthodox scholar concedes the flexibility.'),
 ('Tome of Union (920): fourth marriage', '“Totally forbidding a fourth marriage”, with strict limits on a third.', 'Meyendorff, DOP 44, p. 102', '<span class="st-md">Secondary;</span> the Greek Tome was not read.'),
]
tr = ''.join(f'<tr><td class="src"><b>{a}</b></td><td class="en" style="font-size:14.5px">{b}</td><td class="src">{c}</td><td class="src">{d}</td></tr>' for a, b, c, d in T)
body = f'''<table class="v" style="table-layout:fixed"><tr><th style="width:200px">Rule</th><th>What it says</th><th style="width:185px">Source</th><th style="width:255px">Check</th></tr>{tr}</table>
<div class="rd"><b>Reading.</b> Every age rule I could read puts the minimum for marriage at twelve or thirteen for girls; five was below all of them, and below the Digest’s betrothal minimum. The practice bent for diplomacy, as Meyendorff admits: that is the <i>political concession</i> point, not a doctrine. I found no Orthodox canon or council citing the Simonis marriage as a precedent (a negative result from a limited search).</div>'''
page(OUT, 'SM04', 'SM04', 'Simonis & Milutin', KIND,
     'What Byzantine law and the canons say about age',
     'Checked against the texts; where the pasted guide was wrong or I could not confirm, it says so', body,
     PACK + '<br>Institutes: gutenberg.org/ebooks/5983. Digest 23: thelatinlibrary.com. Ecloga: sourcebooks.web.fordham.edu/source/byz-marr726.asp and archive.org (eclogaleonisetc00linggoog). Milaš: royalarchives.org. Meyendorff: archive.org (DOP44_07_Meyendorff).', head_cls='alt')

# ------------------------------------------------------------------ SM05
body = '''<div class="two">
<div>
<div class="sy2"><div class="t">Milutin the saint</div><div class="b">
<p>The OCA commemorates St Stephen Milutin on 30 October and says his relics were found incorrupt. Its short life does not mention the marriages, which proves nothing either way.</p>
<p style="margin-top:6px">OrthodoxWiki: <i>“Saints are not thought of as either perfect or infallible.”</i> (A reference wiki, not a synodal text.)</p>
<p style="margin-top:6px"><b>So:</b> veneration does not make every act of the saint a precept. But a defence that says the Church rejected him entirely would also be wrong.</p></div></div>
<div class="sy2"><div class="t">The syllogism</div><div class="b">
<p><b>P1.</b> To show that a religion prescribes or permits a conduct, it is not enough that one of its rulers or members practised it.</p>
<p style="margin-top:6px"><b>P2.</b> Simonis’ marriage was arranged by Christian rulers against the age minima of Byzantine law and over Church objections (Fine; Pachymeres); it was not an ordinary application of the marriage rules.</p>
<p style="margin-top:6px"><b>C.</b> So the case does not show that Orthodox Christianity prescribed or approved marrying five-year-olds. It does show rulers and clergy who gave way.</p></div></div>
</div>
<div>
<div class="sy2"><div class="t">If it is turned on Aisha</div><div class="b">
<p>The distinction is between <b>a ruler’s act</b> and <b>a normative precedent</b>. To compare fairly, ask what authority each tradition gives the act and how its jurists read it:</p>
<p style="margin-top:8px"><b>Ibn Hazm</b> (d. 1064), <i>al-Muhalla</i>, q. 1826: <i>“The proof that a father may marry off his young virgin daughter is Abu Bakr’s marriage of the Prophet to Aisha when she was six … whoever claims it was exclusive is not heeded.”</i></p>
<p style="margin-top:8px"><b>Ibn Shubruma</b> (d. 8th c., as reported by Ibn Hazm): a father may not marry off a young daughter until she reaches puberty and consents; Aisha’s case was <i>particular to the Prophet</i>.</p>
<p style="margin-top:8px">So the Aisha precedent was itself debated as law inside Islam. For Simonis I found no Orthodox text that does this.</p></div></div>
<div class="rd" style="margin-top:0"><b>Two cautions.</b><ol>
<li>“Others did it too” shows nothing about right or wrong, in either direction.</li>
<li>The Aisha question stands on its own evidence; this slide only shows why the two cases are not the same kind of case.</li></ol></div>
</div></div>'''
page(OUT, 'SM05', 'SM05', 'Simonis & Milutin', KIND,
     'A saint’s act is not a precept, and the Aisha comparison',
     'The logic of the reply, with its limits', body,
     PACK + '<br>OCA: oca.org/saints/lives/2017/10/30/103118-saint-stephen-milutin-of-serbia. OrthodoxWiki, “Saint”. Ibn Hazm, <i>al-Muhalla</i> vol. 9, pp. 38–40 (OpenITI Shamela0000767; page numbers deduced from the OpenITI markers). Translations mine.', head_cls='alt')

# ------------------------------------------------------------------ SM06
body = '''<div class="two">
<div class="pn"><h4>Corrections to the guide pasted with the photos</h4><ul class="l" style="font-size:15.5px;line-height:1.45">
<li><b>Justinian’s ages</b> are in <i>Inst.</i> 1.22 pr. and <i>Dig.</i> 23.2.4, not <i>Inst.</i> 1.10.</li>
<li><b>Prochiron “12/14”</b>: not confirmed; its marriage title seems to come from the Ecloga (15/13).</li>
<li><b>“Wait until twelve”</b> is not in Gregoras: he says <i>the customary time of marriage</i>. (The Digest does give twelve.)</li>
<li><b>“Immediately”</b> (Kaldellis): Gregoras gives age eight and no date for the wedding.</li>
<li><b>Milutin “fifty”</b>: Gregoras says forty, about five years older than the emperor.</li>
<li><b>“Fourth wife”</b>: sources disagree on Simonis’ rank; I would not cite a number.</li>
<li><b>Milaš</b> cites Prochiron IV,2 for the ages, but that chapter is on dowry.</li>
<li><b>Patriarch</b>: Pachymeres says he was not consulted and took offence. That Failler (1990) says the conflict continued after the ceremony, and that Kosmas resigned over it, I could not verify.</li>
</ul></div>
<div class="pn"><h4>Not verified, and limits</h4><ul class="l" style="font-size:15.5px;line-height:1.45">
<li><b>Fine p. 222 and Kaldellis p. 12</b>: read only from your photos; Kaldellis’ endnote is not visible.</li>
<li><b>Not obtained</b>: Georgievska-Shine (1993) and Failler (1990) (not found / PDF refused); Lascaratos &amp; Poulakou-Rebelakou (2000), abstract only: premature marriages used to cover rape, even in imperial families; it does not name Simonis.</li>
<li><b>Not read</b>: Prochiron title II, the Greek of the Tome of Union, Danilo II’s <i>Life of Milutin</i>, Metochites’ own account.</li>
<li><b>Negative result</b>: no Orthodox text found citing Simonis as precedent (weak OCR search).</li>
<li><b>Greek</b>: lines in SM03 read on Bonn page images (pp. 203–204, 243, 273, 275, 279–280, 285); translations mine. Pachymeres’ book number is ambiguous in the scans (running heads “L. III” and “L. IV”), so I cite pages.</li>
<li><b>Web sources</b> (OCA, OrthodoxWiki, Wikipedia, a Serbian state portal) are secondary; Milutin’s death is dated 1320 or 1321 depending on the source.</li>
<li>Four small AI research agents gathered the material in parallel; I re-read the key page images myself.</li>
</ul></div></div>
<div class="rd" style="margin-top:12px"><b>Bottom line.</b> The accusation has solid historical ground against particular rulers and against institutions that gave way. It is not evidence that Orthodox Christianity taught the conduct as a moral or religious norm. Do not dispute the books’ authenticity: they are real and relevant.</div>'''
page(OUT, 'SM06', 'SM06', 'Simonis & Milutin', KIND,
     'What was checked, what was corrected, what could not be',
     'An honest account of the method and its limits', body,
     PACK + '<br>Page images: archive.org items nicephorigregor00bekkgoog and georgiipachymer00pousgoog (Google scans of the Bonn editions).', head_cls='alt')
print('smgen ok')
