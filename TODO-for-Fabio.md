# TODO for Fabio

1. Jyväskylä PhD title: bio says "Mathematical Information Technology", CV says "Computing and Mathematical Sciences". Site uses the bio's.
2. CV says "8 PhD students" at Swansea but lists 7 PhD + 1 MSc by Res (5 first-supervisor PhD, 2 second). I used the list; please confirm.
3. Project pages: descriptions, outputs and DOIs are not yet filled in; I only used funder, year, role and amount from the CV. Grant-to-project mapping is inferred from slide logos: please confirm.
4. CV "2027"-style future dates and Honorary fellowship ended 23/08/2026: check.
5. PRIVACY: the new CV PDF lists student names. Do not upload it as assets/pdf/CV.pdf without removing that section.
6. Add student names only with written consent.

7. Alumni names are listed publicly (`_data/alumni.yml`).

8. Publications:
   - Please upload with `_bibliography/papers.bib` and check the build log. I could not run Jekyll, so the `-q @*[section=...]` queries on the Publications page are untested.
   - Both theses are in `papers.bib` (DMU title as you gave it, DOI 10.13140/2.1.3248.5447; Jyväskylä details from the JYX record).
   - J49 (generative AI in secondary education) has no authors in the CV: it shows as "Caraffini, Fabio and others". Please supply them.
   - P29, P30, P31 (ACM) and P11 (Springer) have no venue in the CV; they show the publisher only.
   - Typos fixed silently from the CV: Shengxyang to Shengxiang, Colreavy-Donelly/Donnely to Colreavy-Donnelly, Sturat to Stuart, Morder to Morden, "datase" to "dataset", and "Lorenzo Iacca" (P8) to "Giovanni Iacca". Please confirm P8.
   - "Jixianga Cheng" and "Gexianga Zhang" (J10, P8) look like typos for Jixiang and Gexiang. I left them as in the CV.
   - Hongying Zan is written "Zan Hongying" and "Hongying Zan" in the CV. The site uses Zan as the family name.
   - Under review: ICASSP 2026 (R4) and the Zenodo "September 2026" date look out of step with today's date. R9 was removed and R8 moved to Accepted.
   - The duplicate "Structural bias ... extended results" entry was replaced by the Mendeley DEOB entry you supplied.
9. Software page: GitHub links for SOS and the IEEE branch repo are guessed from the repo names; please check them.
10. Run `python3 bin/add_dois.py` locally to fill DOIs; I could not test it against Crossref from here.
11. Co-author ORCIDs are not in `_data/coauthors.yml` (only yours); add them once checked.
