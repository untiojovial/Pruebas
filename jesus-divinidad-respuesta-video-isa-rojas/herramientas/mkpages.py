# -*- coding: utf-8 -*-
import sys
sys.path.insert(0,'/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/jd')
import hlpage
JD='/tmp/claude-0/-home-user-Pruebas/978f574d-1019-54bc-bb45-9f4fddd102bb/scratchpad/jd'
BLUE=(120,190,255)
jobs = {
 'bauckham_p12': (f'{JD}/J4/dl/mosher_marshall_2018_monotheism_complexities.pdf', 37, [
    "Paul must mean that Jesus Christ was not some created assistant to God but himself belonged eternally to the unique identity of the one God."]),
 'bauckham_p13': (f'{JD}/J4/dl/mosher_marshall_2018_monotheism_complexities.pdf', 38, [
    "Worship of Jesus did not infringe Jewish monotheism, because Jesus himself belonged to the unique identity of the one and only God.",
    "Paul never or hardly ever uses the word “God” of Jesus, but the word “god” is actually rather ambiguous and could be taken to mean that Jesus was a second god. It is much more significant that Paul can take texts referring to YHWH as references to Jesus."]),
 'brown_p565': (f'{JD}/J8/dl/brown_does_NT_call_jesus_God_TS1965.pdf', 21, [
    "This is the clearest example in the New Testament of the use of “God” for Jesus,",
    "The question that forms the title of this article must be answered in the affirmative. In three clear instances and in five instances that have a certain probability Jesus is called God in the New Testament."]),
 'brown_p566': (f'{JD}/J8/dl/brown_does_NT_call_jesus_God_TS1965.pdf', 22, [
    "“Jesus is Lord” was evidently a popular confessional formula in New Testament times, and in this formula Christians gave Jesus the title kyrios which was the standard LXX translation for YHWH.",
    ("Jesus is never called God in the Synoptic Gospels, and a passage like Mk 10:18 would seem to preclude the possibility that Jesus used the title of himself. Even the fourth Gospel never portrays Jesus as saying specifically that he is God.", BLUE)]),
 'schafer_p5': (f'{JD}/J7/dl/schafer_princeton_sample.pdf', 7, [
    "The elevation of Jesus of Nazareth as the firstborn before all creation, the God incarnate, Son of God, Son of Man, the Messiah: all these basic Christological premises are not pagan or other kinds of aberrations; they are rooted in Second Temple Judaism, regardless of their specifically Christian character."]),
}
for k,(pdf,n,ph) in jobs.items():
    miss = hlpage.render(pdf,n,ph,f'{JD}/pg/{k}_f.png',dpi=150,focus=(260,200,150)); hlpage.render(pdf,n,ph,f'{JD}/pg/{k}.png',dpi=150)
    print(k,'missing:',miss)

jobs2 = {
 'hurtado_p8': (f'{JD}/J5/dl/christology-nidb.pdf', 8, [
    "It seems, in fact, that Jesus was ascribed the eschatological role and attributes of Yahweh."]),
 'hurtado_p11': (f'{JD}/J5/dl/christology-nidb.pdf', 11, [
    "The unambiguous instances are in John 1:1 and 20:28."]),
}
for k,(pdf,n,ph) in jobs2.items():
    miss = hlpage.render(pdf,n,ph,f'{JD}/pg/{k}_f.png',dpi=140,focus=(260,200,150)); hlpage.render(pdf,n,ph,f'{JD}/pg/{k}.png',dpi=140)
    print(k,'missing:',miss)
