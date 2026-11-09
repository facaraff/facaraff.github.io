---
layout: page
permalink: /publications/
title: publications
description: Journal articles, conference papers, chapters, editorials, theses and open data. Generated from a BibTeX master file.
nav: true
nav_order: 2
toc:
  sidebar: left
---

Author ORCID: [0000-0001-9199-7368](https://orcid.org/0000-0001-9199-7368) · [Google Scholar](https://scholar.google.com/citations?user=pQqpUNEAAAAJ) · [Scopus](https://www.scopus.com/authid/detail.uri?authorId=55173601900) · [Web of Science](https://www.webofscience.com/wos/author/record/AAE-2809-2019) · [Cronfa](https://cronfa.swansea.ac.uk/Search/Results?lookfor=fabio+caraffini&type=AllFields&sort=year)

{% include bib_search.liquid %}

## Journal articles

<div class="publications">

{% bibliography -q @*[section=journal] %}

</div>

## Peer-reviewed conference proceedings

<div class="publications">

{% bibliography -q @*[section=conference] %}

</div>

## Book chapters

<div class="publications">

{% bibliography -q @*[section=chapter] %}

</div>

## Editorials

<div class="publications">

{% bibliography -q @*[section=editorial] %}

</div>

## Edited books

<div class="publications">

{% bibliography -q @*[section=edited] %}

</div>

## PhD theses

<div class="publications">

{% bibliography -q @*[section=thesis] %}

</div>

## Accepted (DOI not yet available)

<ol>
  {% for p in site.data.in_progress.accepted %}
    <li>{{ p.authors }}. <em>{{ p.title }}</em>. {{ p.venue }}.</li>
  {% endfor %}
</ol>

## Under review

<ol>
  {% for p in site.data.in_progress.under_review %}
    <li>{{ p.authors }}. <em>{{ p.title }}</em>. {{ p.venue }}.</li>
  {% endfor %}
</ol>

Software and datasets with DOIs are on the [Software & Data]({{ '/software/' | relative_url }}) page.
