# J8 notes (counter-arguments and scholarship)

**Searched.** Qur'an and tafsir through the quran.com API (Sahih International; Arabic from `text_uthmani_simple`; Ibn Kathir Arabic = resource 14, Ibn Kathir Abridged English = resource 169). Ibn Ishaq through the Guillaume OUP Karachi 1987 PDF on archive.org (551 pp., text layer; printed pages from the "Page N" headers; Wuestenfeld numbers in parentheses, as Guillaume's introduction states). Watt, *Muhammad at Medina* (1956) from archive.org PDF. Maududi, *Al Jihad fil Islam* (Rafatullah Shah tr.) from islamicstudies.info PDF. Shaltut, *Min tawjihat al-Islam*, from archive.org OCR text. Gospels from bible-api.com (WEB).

**Negative results (not quoted).** Firestone, Cook, Bonner, Peters, Donner, Brown and Emerick: archive.org returns 401/403 (restricted lending copies) or 503 on repeated tries. Abduh/Rida, *Tafsir al-Manar* vol. 2: the scan has no text layer and the OCR is unusable. I checked PDF pages 166-193 by eye; they reach 2:186-189 and 2:187 but not 2:190. Ghamidi: not reached. Greek NT not read.

**Double-check.**
1. Guillaume page = printed page. The `page_file_pdf_page` value is the PDF page index (e.g. printed 212 = PDF 147). Most passages show no Wuestenfeld number inside them.
2. Guillaume and Watt English is normalised: soft hyphens removed, OCR line-break hyphens joined, footnote call numbers and Watt's italic asterisks removed.
3. Shaltut Arabic (J8-36) is OCR text, not checked against the page image; status PARTLY.
4. Ibn Kathir 2:256 (J8-15) is Arabic only; no English was read, so status PARTLY.
5. Arabic in J8-01 to J8-13 is the quran.com simplified Uthmani text without diacritics; use tanzil.net for full tashkeel.
6. bible-api.com is not on the allowed-source list; swap for an allowed source if needed.
7. The Ibn Kathir Abridged translator is unnamed in the API; the brief's Darussalam attribution is unverified.
8. The Maududi Qur'an rendering inside the book is unattributed; the quoted English is Maududi's text, not a Qur'an translation.
9. Verses 2:193 and 2:217 are contested. Ibn Kathir (J8-14) and Maududi (J8-34) read them defensively; the abrogation in J8-15 reads them as offensive.
10. Blank `date` fields: the source gives none.
