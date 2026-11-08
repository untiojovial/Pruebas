# J7 notes: page scans

## Searched
- archive.org (search and metadata API) for every listed edition. PDFs are in dl/ (about 150 MB). Each was checked with pdfinfo and pdftotext.
- Guillaume: GuillaumeLifeOfMuhammad.pdf (Karachi 1955, 431 pages, two-page spreads, header numbers) and Guillaume_1987_OUP.pdf (551 pages, "Page NNN" markers; none for pp. 240-339). Both use the 1955 pagination.
- Bukhari (Muhsin Khan, Darussalam 1997) vols 1, 3, 4, 5: hadith 25, 2541, 2977, 4037 located and text-checked.
- Ibn Kathir (Mubarakpuri abridged, Darussalam 2000) vol. 4 _text.pdf: 9:5 and 9:29 located (printed = PDF + 2).
- Muslim vol. 2 (Khattab translation): [1731] located.
- Ibn Hisham Arabic (Yedali upload) vols 1-2 text layers.

## Negative results
- sunnah.com: 403 to curl and WebFetch (bukhari:25, 4037, muslim:1731). Clean URLs are in passages.json. A jsDelivr hadith mirror gave English texts; it is not an allowed source, used only to cross-check.
- Muslim 1731 in the available English edition (Khattab) is Aisha on the Prophet sleeping before dawn, not a war hadith. The Abdul Hamid Siddiqi translation was not found.
- Rosenthal Muqaddimah vol. 1 (Pantheon 1958): restricted (401). The open PDF is vol. 2.
- Wustenfeld 1858 (bub_gb_GH8pAAAAYAAJ, bub_gb_ZH8pAAAAYAAJ): no PDF, no Arabic text layer, images only (tar 93-101 MB, not downloaded).
- Bukhari Arabic-English 1997 single file: restricted (401).
- Muhsin Khan PDFs have no Arabic text layer; no Arabic is copied.

## Double-check
- Guillaume pages 280-290 and 300-310: PDF pages inferred from headers and the TOC, not read. Render before use.
- Guillaume 1955 spreads: header-mapped only. The 1987 markers are more reliable where present.
- Ibn Kathir 9:29 English is OCR-broken; check against the printed page.
- Yedali Ibn Hisham: edition unidentified, Arabic OCR noisy; no Arabic copied.
- Replace Muslim 1731 with the intended hadith number.
