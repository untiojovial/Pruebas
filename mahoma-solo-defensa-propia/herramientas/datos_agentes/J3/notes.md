# J3 notes: hadith on offensive fighting and calling to Islam

## Searched
- sunnah.com: 403 to curl and to WebFetch (checked for muslim:1731). No text was read from sunnah.com itself.
- Texts were read from the jsDelivr copy of fawazahmed0/hadith-api (`ara-bukhari`, `eng-bukhari`, `ara-muslim`, `eng-muslim`, `ara-abudawud`, `eng-abudawud`), saved in `dl/`.
- Muslim texts were cross-checked against AhmedBaset/hadith-json `muslim.json` (saved as `dl/ahmed-muslim.json`). Arabic and English matched for 1730, 1731, 1767, 1910, 1551.06 and the 21/22 texts.
- Arabic over 120 words is a verbatim window of the matn. English is the full mirror text.

## Numbering
- Bukhari: mirror `hadithnumber` equals sunnah numbering (25, 392, 2541, etc.). Mirror in-book refs are given in `page`.
- Muslim: mirror `hadithnumber` is sequential and differs from standard numbering. Standard numbers were taken from the mirror's `arabicnumber`: 124=20, 125/126/127=21.01/21.02/21.03, 129=22, 4519=1730.01, 4594=1767.01, 4931=1910, 3967=1551.06.
- Muslim 1731: mirror 4521 and 4522 have no `arabicnumber`. They are two transmission lines of the same matn, and the number 1731 was inferred from content. Check on sunnah.com.

## Negative results and limits
- No sunnah.com grading per hadith. Bukhari and Muslim are marked sahih at collection level only. Abu Dawud 2484 has grades from the mirror.
- No translator is named in any mirror JSON. English translators are unknown; `translator` is blank for all items. Confirm attribution on sunnah.com before quoting.
- Muslim 1767 is "I will expel the Jews and Christians from the Arabian Peninsula", not a jizya passage. The Hijaz expulsion (Muslim 1551.06, Khaybar context) is recorded separately as J3-21.
- Muslim 1730 has Nafi' writing that inviting enemies before fighting was required "in the early days of Islam". Record it as a source-internal qualifier.
- No PDFs were used, so `page_file` is null for all items.

## Double-check
1. All sunnah.com URLs in `url`, from a browser, with the Arabic and English shown there.
2. Translator names for the English (Bukhari and Muslim).
3. Muslim 1731 numbering and the two-line structure.
4. Muslim 21.01 to 21.03 sub-numbering on sunnah.com.
5. Abu Dawud 2484 grading.
