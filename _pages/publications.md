---
layout: page
permalink: /publications/
title: publications
description: Journal articles, conference papers, chapters, editorials, theses and open data. Generated from a BibTeX master file.
nav: true
nav_order: 2
---

Author ORCID: [0000-0001-9199-7368](https://orcid.org/0000-0001-9199-7368) · [Google Scholar](https://scholar.google.com/citations?user=pQqpUNEAAAAJ) · [Scopus](https://www.scopus.com/authid/detail.uri?authorId=55173601900) · [Web of Science](https://www.webofscience.com/wos/author/record/AAE-2809-2019)

{% include bib_search.liquid %}

## 1. Journal articles

<div class="publications">

{% bibliography -q @*[section=journal] %}

</div>

## 2. Peer-reviewed conference proceedings

<div class="publications">

{% bibliography -q @*[section=conference] %}

</div>

## 3. Book chapters

<div class="publications">

{% bibliography -q @*[section=chapter] %}

</div>

## 4. Editorials

<div class="publications">

{% bibliography -q @*[section=editorial] %}

</div>

## 5. Edited books

<div class="publications">

{% bibliography -q @*[section=edited] %}

</div>

## 6. PhD theses

<div class="publications">

{% bibliography -q @*[section=thesis] %}

</div>

## 7. Accepted (DOI not yet available)

<ol>
  {% for p in site.data.in_progress.accepted %}
    <li>{{ p.authors }}. <em>{{ p.title }}</em>. {{ p.venue }}.</li>
  {% endfor %}
</ol>

## 8. Under review

<ol>
  {% for p in site.data.in_progress.under_review %}
    <li>{{ p.authors }}. <em>{{ p.title }}</em>. {{ p.venue }}.</li>
  {% endfor %}
</ol>

Software and datasets with DOIs are on the [Software & Data]({{ '/software/' | relative_url }}) page.
