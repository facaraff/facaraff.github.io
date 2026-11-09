# Maintenance guide

All edits are made on the `master` branch (GitHub: open the file, click the pencil icon, then "Commit changes"). The "Deploy site" action rebuilds the site in about two minutes. Never edit `gh-pages`.

## Add a publication

Open `_bibliography/papers.bib` and copy an existing entry of the same kind. Keep:

- `abbr`: the label (J57 for the next journal article, P50 for the next conference paper, and so on).
- `section`: one of `journal`, `conference`, `chapter`, `editorial`, `edited`, `thesis`, `software`, `data`.
- `doi`: add `doi = {...}` and a DOI button appears.

Optional fields that add buttons: `pdf`, `code`, `slides`, `poster`, `html`, `arxiv`.

## Fill in missing DOIs (so every reference is clickable)

Entries with a `doi` get a DOI button; theses and datasets already have one. For the rest, run on your own computer (it needs internet):

```
python3 bin/add_dois.py          # dry run, prints proposed DOIs
python3 bin/add_dois.py --write  # saves the matches into papers.bib
```

It only accepts near-exact title matches, but skim the list before committing. For anything not matched, add `doi = {...}` or `html = {https://...}` by hand.

## Link co-author names

Edit `_data/coauthors.yml`: add the co-author's family name (lower case), the name variants used in `papers.bib`, and their ORCID or homepage URL. Their name then becomes a link in every entry. Only add URLs you have checked.

## Add a newly published paper

Only published papers (with a DOI) are listed. Add an entry to `_bibliography/papers.bib` with `section`, `abbr`, `themes` and `doi`, then run `python3 bin/make_stats.py`.

## Add a project

Add a block to `_data/projects.yml` (title, funder, amount, role, year, summary). To add links, add a `links:` list of `label` and `url` pairs to the project; they appear under its summary.

## Add a student, alumnus or incoming student

Edit `_data/students.yml` (current and incoming, anonymous) or `_data/alumni.yml` (completed PhDs, with name). Do not add names of current students without their written consent.

## Add a talk or its slides

Edit `_data/talks.yml` and add a block (title, event, place, date). To link slides, upload the PDF to `assets/pdf/talks/` (a subfolder next to the CV in `assets/pdf/`) and set `slides:` to the file name, for example `slides: ecta2023-structural-bias.pdf`. A "Slides (PDF)" link then appears next to that talk. Remove private or third-party material from slides first, because the repo is public.

## Replace the CV PDF

Upload the new file to `assets/pdf/CV.pdf`, replacing the old one. Remove private information (such as student names) first, because the repo is public.

## Edit the homepage text

Edit `_pages/about.md`. The text below the second `---` line is the body.

## Add or change a social link

Edit `_data/socials.yml`. Built-in keys include `github_username`, `linkedin_username`, `orcid_id`, `scholar_userid`; any other entry needs `logo`, `title` and `url`.

## Add a software repository or dataset (citable)

Add an `@misc` entry to `_bibliography/papers.bib` with `section = {software}` (code) or `section = {data}` (datasets), a `year`, and either a `doi` (Zenodo, Mendeley Data, Figshare) or `code = {https://github.com/...}`. It appears on the Software & Data page, with a BibTeX button so others can cite it. To get a DOI for a GitHub repository, archive it with Zenodo: Zenodo, GitHub, switch the repo on, then publish a release.

## Supervision (People page)

Everything on the People page comes from one file, `_data/supervision.yml`. Add one block per student: `level`, `role` (`first` or `second`; second also covers external supervision), `status` (`current` or `completed`), `institution`, and optionally `name`, `start` (for example January 2027), `year`, `title` and `url` (thesis or DOI link). The counts, the per-institution breakdown and the lists update by themselves. Leave out `name` for anyone who has not agreed to be named: they are still counted and listed as "PhD student". Keep completed entries newest first.

## "Research at a glance" on the About page

The theme tags, the publications-per-year chart and the activity tiles are drawn from data files:

- `_data/publication_stats.yml` is generated from `papers.bib`. After you add or change a paper, run `python3 bin/make_stats.py` (it needs no internet) and commit the result, or ask me in the Project chat to regenerate it. Tag each new paper with `themes = {opt, health}` in `papers.bib`; the theme ids are in `_data/research_themes.yml`. The script lists any papers without a `themes` field.
- `_data/research_themes.yml` holds the theme names and short descriptions. Edit it to rename or add themes.
- `_data/activity.yml` holds two hand-kept numbers: journals as Associate Editor and grants secured.
- The student, supervision and talk tiles count `_data/supervision.yml` and `_data/talks.yml` by themselves.
