# Recortes en alta resolución (frases resaltadas con hl.py)
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hl import render
G = '../jq/J2/dl/guillaume.pdf'; D7 = '../jq/J7/dl/'; D6 = '../jq/J6/dl/'
jobs = [
 (G,167,['will kill them in the sacred month,','attack them. Then they encouraged each other, and decided to kill as','with an arrow and killed him,'],'g_nakhla.jpg'),
 (G,168,['Quraysh caravan containing their property. Go out to attack it, perhaps','God will give it as a prey.'],'g_badr.jpg'),
 (G,207,['Who will rid me of','I will kill him.'],'g_kab1.jpg'),
 (G,208,['Smite the enemy of God!','Kill any Jew that falls into your power.'],'g_kab2.jpg'),
 (G,256,['judgement that the men should be killed, the property divided, and the','trenches in it. Then he sent for them and struck off their heads in those','trenches as they were brought out to him in batches.'],'g_qurayza.jpg'),
 (G,279,['apostle raided a people he waited until the morning. If he heard a call to','prayer he held back; if he did not hear it he attacked.','Khaybar is destroyed.'],'g_khaybar.jpg'),
 (G,299,["be killed even if they were found beneath the curtains of the Ka'ba."],'g_mecca.jpg'),
 (G,325,['orders to prepare to raid the Byzantines.','The apostle ordered his companions to prepare to raid the Byzantines at'],'g_tabuk.jpg'),
 (G,361,["ea WIt tl:llS rascal for me?' whereupo","Take that Abu Afak m spite of your age!'"],'g_abuafak.jpg'),
 (G,362,["Who will rid me of Marwan's daughter?",'You have helped God and His apostle'],'g_asma.jpg'),
 (D7+'Bukhari_1997_vol1.pdf',67,['ordered (by Allah) to fight against the people','till they testify that La ilaha illallah, wa anna'],'b25.jpg'),
 (D7+'Bukhari_1997_vol3.pdf',414,['had (suddenly) attacked','Ban! Mualiq (without warning while they','were heedless) and their cattle were being','watered at the places of water. Their fighting','men were killed and their women and','children were taken as captives;'],'b2541.jpg'),
 (D7+'Bukhari_1997_vol5.pdf',222,['said "Who will',"kill Ka'b bin Al-Ashraf who has hurt Allah",'and His Messenger?" Thereupon',"Allah's Messenger! Would you like that I kill",'him?" The Prophet ij said, "Yes."',"me to say a thing (i.e., to deceive Ka'b) .\""],'b4037.jpg'),
 (D7+'IbnKathir_vol4_text.pdf',403,['This honorable Ayah was revealed with the order to fight the','People of the Book,','commanded His Messenger gj to fight the People of the','Scriptures, Jews and Christians, on the ninth year of Hijrah,','and he prepared his army to fight the Romans'],'ik929.jpg'),
 (D7+'IbnKathir_vol4_text.pdf',374,['do not wait until you find them. Rather, seek and besiege','them in their areas and forts,','This way, they will have no choice,','but to die or embrace Islam,'],'ik95.jpg'),
 (D7+'IbnKathir_vol4_text.pdf',375,['This honorable Ayah (9:5) was called the Ayah of the Sword,','about which Ad-Dahhftk bin Muzahim said, “It abrogated every','agreement of peace between the Prophet','and any idolator,','every treaty, and every term."'],'ik95b.jpg'),
 (D6+'reliance_traveller.pdf',620,['makes war upon Jews, Christians, and Zoroastrians','until they become Muslim or else pay the non-Muslim poll tax'],'rel98.jpg'),
 (D6+'reliance_traveller.pdf',621,['The caliph fights all other peoples until they become Muslim'],'rel99.jpg'),
 ('../jq/J8/dl/watt1956.pdf',253,['The words of the pledge of war speak of defensive action only;','What happened was that the first expeditions were offensive','expeditions from Medina in the hope of ambushing a Meccan caravan.','As these expeditions, even that to Badr, were razzias,'],'watt231.jpg'),
]
os.makedirs('pgh', exist_ok=True)
for pdf, p, ph, o in jobs:
    render(pdf, p, ph, 'pgh/' + o, dpi=300 if pdf == G else 260, pad=460, width=2200)
