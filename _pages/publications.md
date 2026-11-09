---
layout: page
permalink: /publications/
title: publications
description: Journal articles, conference papers, chapters, editorials, theses and open data. Generated from a BibTeX master file.
nav: true
nav_order: 2
---

Author ORCID: [0000-0001-9199-7368](https://orcid.org/0000-0001-9199-7368) · [Google Scholar](https://scholar.google.com/citations?user=pQqpUNEAAAAJ) · [Scopus](https://www.scopus.com/authid/detail.uri?authorId=55173601900) · [Web of Science](https://www.webofscience.com/wos/author/record/AAE-2809-2019) · [Cronfa](https://cronfa.swansea.ac.uk/Search/Results?lookfor=fabio+caraffini&type=AllFields&sort=year)

{% include bib_search.liquid %}

<style>
  .pubnav { font-size: 0.95rem; margin: 0 0 1.5rem; }
  .pubnav a { display: inline-block; margin: 0 1.1rem 0.3rem 0; color: var(--global-text-color); border-bottom: 1px solid var(--global-divider-color); }
  .pubnav a:hover { color: var(--global-theme-color); border-bottom-color: var(--global-theme-color); text-decoration: none; }
  h2[id] { scroll-margin-top: 5rem; }
</style>

<nav class="pubnav" aria-label="Publication sections">
  <a href="#journal">Journal articles</a>
  <a href="#conference">Conference papers</a>
  <a href="#chapters">Book chapters</a>
  <a href="#editorials">Editorials</a>
  <a href="#edited">Edited books</a>
  <a href="#theses">PhD theses</a>
</nav>

<script>
  document.querySelectorAll(".pubnav a").forEach(function (a) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      var el = document.getElementById(a.getAttribute("href").slice(1));
      if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });
</script>

## Journal articles {#journal}

<div class="publications">

{% bibliography -q @*[section=journal] %}

</div>

## Peer-reviewed conference proceedings {#conference}

<div class="publications">

{% bibliography -q @*[section=conference] %}

</div>

## Book chapters {#chapters}

<div class="publications">

{% bibliography -q @*[section=chapter] %}

</div>

## Editorials {#editorials}

<div class="publications">

{% bibliography -q @*[section=editorial] %}

</div>

## Edited books {#edited}

<div class="publications">

{% bibliography -q @*[section=edited] %}

</div>

## PhD theses {#theses}

<div class="publications">

{% bibliography -q @*[section=thesis] %}

</div>

Software and datasets with DOIs are on the [Software & Data]({{ '/software/' | relative_url }}) page.
