# J2 notes: killings of critics and poets

**Searched.** sunnah.com returned Cloudflare 403 to curl, so hadith texts come from the fawazahmed0/hadith-api JSON via jsDelivr (eng-bukhari = Muhsin Khan and eng-muslim = Abdul Hamid Siddiqui per metadata; the Abu Dawud and Arabic editions list no translator or edition). Guillaume: archive.org GuillaumeATheLifeOfMuhammad, saved as dl/guillaume.pdf (431 pp, OCR text layer). PDF page n = printed pp. 2(n-24) and 2(n-24)+1. Key lines were checked on page images (pdftoppm, 130 dpi) for PDF 178, 207, 208, 265, 299, 322, 361, 362. Ibn Sa'd: archive.org "tabqaatibnsaadarabic" djvu OCR (dl/sad_ar.txt); English Bewley vol. VIII (dl/sad_v8.txt) has no 'Asma' bint Marwan or Abu 'Afak entry.

**Normalisation.** Arabic was matched ignoring harakat; invisible RLM/LRM marks were removed. Harakat are kept where the source has them.

**Negative or partial results.**
- Muslim "1801" (brief) is not confirmed. In the dataset, hadithnumber 1801 is a different hadith (Ibn 'Abbas, night prayer, book 6 hadith 229). The Ka'b hadith there is 4664 (book 32, Jihad, hadith 146).
- Ibn Sa'd English: no entry found for 'Asma' or Abu 'Afak. Ibn Sa'd Arabic OCR is noisy (e.g. "يَقَثْل" for يقتل); verify against a scan.
- Ka'b b. Zuhayr pardon (J2-18) is OCR only.
- Not checked: Ibn Hisham Arabic (Wustenfeld), al-Waqidi Maghazi (Ibn Sa'd cites it at p. 174 for Abu 'Afak), al-Tabari Leiden.

**Double-check before publishing.**
1. Bukhari and Abu Dawud numbers are the dataset's; confirm against sunnah.com (blocked from here).
2. Abu Dawud 2686 grading: Albani and Muhyi al-Din hasan sahih, Shu'ayb sahih, Zubair 'Ali Za'i da'if. The isnad runs through Ibrahim (al-Nakha'i) and Masruq.
3. J2-04 is labelled killing of critic on its content, not on the Abdul Baqi number.
4. J2-08 (Ibn Sunayna) is a general order to kill any Jew, not limited to critics.
5. Wustenfeld margin numbers were read from page images.

