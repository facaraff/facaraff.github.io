#!/usr/bin/env python3
"""Look up missing DOIs in _bibliography/papers.bib using the Crossref API.

Usage (run on your own computer, it needs internet access):
    python3 bin/add_dois.py            # dry run: prints proposed DOIs
    python3 bin/add_dois.py --write    # writes accepted matches into papers.bib

Only entries WITHOUT a doi field are looked up, and only when the Crossref title
matches the BibTeX title almost exactly. Always skim the report before committing.
Set CROSSREF_MAILTO=you@example.org to use Crossref's polite pool (optional).
"""
import difflib, json, os, re, sys, time, urllib.parse, urllib.request

BIB = os.path.join(os.path.dirname(__file__), "..", "_bibliography", "papers.bib")
SECTIONS = {"journal", "conference", "chapter", "editorial"}


def norm(s):
    s = re.sub(r"\\&", "and", s)
    s = re.sub(r"[{}\\$]", "", s)
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def lookup(title, mailto):
    q = {"query.bibliographic": title, "rows": "3", "select": "DOI,title"}
    if mailto:
        q["mailto"] = mailto
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(q)
    with urllib.request.urlopen(url, timeout=30) as r:
        items = json.load(r)["message"]["items"]
    best = None
    for it in items:
        for t in it.get("title", []):
            ratio = difflib.SequenceMatcher(None, norm(title), norm(t)).ratio()
            if not best or ratio > best[0]:
                best = (ratio, it["DOI"], t)
    return best


def main():
    write = "--write" in sys.argv
    mailto = os.environ.get("CROSSREF_MAILTO", "")
    text = open(BIB, encoding="utf-8").read()
    parts = re.split(r"(?m)^(?=@\w+\{)", text)
    out, found, missed = [], 0, []
    for part in parts:
        m = re.match(r"@\w+\{([^,]+),", part)
        sec = re.search(r"section\s*=\s*\{(\w+)\}", part)
        if not m or not sec or sec.group(1) not in SECTIONS or re.search(r"(?m)^\s*doi\s*=", part):
            out.append(part)
            continue
        tm = re.search(r"title\s*=\s*\{\{?(.*?)\}?\},?\s*$", part, re.M)
        if not tm:
            out.append(part)
            continue
        title = tm.group(1)
        try:
            best = lookup(title, mailto)
        except Exception as e:  # network or API problem: leave the entry alone
            print("ERROR", m.group(1), e)
            out.append(part)
            continue
        time.sleep(0.3)
        if best and best[0] >= 0.95:
            found += 1
            print(f"OK   {m.group(1):28} {best[1]}  ({best[0]:.2f})")
            part = re.sub(r"(?m)^(\s*abbr\s*=)", f"  doi = {{{best[1]}}},\n\\1", part, count=1)
        else:
            missed.append(m.group(1))
            print(f"MISS {m.group(1):28} best={best[1] if best else None} ({best[0]:.2f})" if best else f"MISS {m.group(1)}")
        out.append(part)
    print(f"\n{found} DOIs found, {len(missed)} not matched.")
    if write:
        open(BIB, "w", encoding="utf-8").write("".join(out))
        print("papers.bib updated.")
    else:
        print("Dry run: use --write to update papers.bib.")


if __name__ == "__main__":
    main()
