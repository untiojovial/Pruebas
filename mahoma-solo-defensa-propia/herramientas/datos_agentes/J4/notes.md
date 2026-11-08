# J4 notes: Qur'an and tafsir

## Searched
- Qur'an 9:5, 9:29, 9:123, 9:73, 8:39, 8:12, 8:60, 2:216, 2:190-193, 2:217, 47:4, 48:16, 22:39-40: Arabic (text_uthmani), Saheeh International and Hilali-Khan from quran.com API v4. All 17 verses read.
- Tafsir via quran.com API v4 (ids 14 Ibn Kathir Arabic, 169 Ibn Kathir abridged English, 15 al-Tabari, 90 al-Qurtubi, 94 al-Baghawi). The API names no printed edition or page.
- Jalalayn: Arabic from tafsir.app/jalalayn (edition not named); English 9:5 from quranx.com.
- All 33 distinct passage URLs return HTTP 200.

## Negative or limited results
- Ali "four swords" report (Ibn Kathir 9:5): absent from the English abridged; Ibn Kathir doubts part of it.
- Al-Qurtubi 9:5 does not say "every verse of pardon". It says "every verse ... mentioning turning away and patience with the enemies' harm" (item 22).
- Jalalayn 2:190 on tafsir.app stops mid-sentence. quranx has no English for 2:190-191 (404).
- altafsir.com returns no ayah text in server HTML (loaded by script); KSU site has no Jalalayn.
- No Darussalam abridged scan on archive.org. tafsir-ibn-kathir-eng (113 MB, commercial upload) exceeds 80 MB and was not downloaded. dl/ is empty, so page_file is null everywhere; use the listed URLs for captures.
- sunnah.com returns 403 to curl; not needed here.

## Double-check
- Printed edition and page numbers for Ibn Kathir (AR and EN), Baghawi and Jalalayn. Only Qurtubi ([ص: 13] to [ص: 330], volume unstated) and Tabari (vol. 3 p. 571 marker) carry markers.
- Translator and edition of the tafsir.app Arabic and the quranx English.
- In-book numbers for hadiths cited inside Ibn Kathir (Ibn Umar on 2:193; Makkah sanctity on 2:190; Buraydah on 2:190). None verified.
- "Pact of Umar" (item 27): quoted from Ibn Kathir; chain unchecked, authenticity contested.
- The brief's "Muhsin Khan" is the Bukhari translator; the Qur'an uses Hilali-Khan (quran.com id 203), with Saheeh International as the English field.
- 9:29 (Tabuk): Ibn Kathir ties it to Tabuk; Baghawi also reports a Kalbi view that it concerns Qurayza and al-Nadir.
