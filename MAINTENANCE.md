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

## Move a paper from "under review" to "accepted" or "published"

Edit `_data/in_progress.yml`. When it has a DOI, delete it from there and add it to `papers.bib`.

## Add a project

Add a block to `_data/projects.yml` (title, funder, amount, role, year, summary).

## Add a student, alumnus or incoming student

Edit `_data/students.yml` (current and incoming, anonymous) or `_data/alumni.yml` (completed PhDs, with name). Do not add names of current students without their written consent.

## Add a talk

Add a line to `_pages/talks.md`. Put the slides PDF in `assets/pdf/` and link to it with `/assets/pdf/<file>.pdf`.

## Replace the CV PDF

Upload the new file to `assets/pdf/CV.pdf`, replacing the old one. Remove private information (such as student names) first, because the repo is public.

## Edit the homepage text

Edit `_pages/about.md`. The text below the second `---` line is the body.

## Add or change a social link

Edit `_data/socials.yml`. Built-in keys include `github_username`, `linkedin_username`, `orcid_id`, `scholar_userid`; any other entry needs `logo`, `title` and `url`.

## Add a software repository or dataset (citable)

Add an `@misc` entry to `_bibliography/papers.bib` with `section = {software}` (code) or `section = {data}` (datasets), a `year`, and either a `doi` (Zenodo, Mendeley Data, Figshare) or `code = {https://github.com/...}`. It appears on the Software & Data page, with a BibTeX button so others can cite it. To get a DOI for a GitHub repository, archive it with Zenodo: Zenodo, GitHub, switch the repo on, then publish a release.

## Supervision counts and titles

The counts on the People page are computed from `_data/students.yml` (current and incoming) and `_data/alumni.yml` (completed), so just add or edit entries. Fill in `title:` for a student to list their project title (anonymous). For alumni, add `thesis:` (title) and `url:` (link to the e-thesis) and a link appears.
