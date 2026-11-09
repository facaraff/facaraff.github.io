---
layout: page
permalink: /software/
title: software & data
description: Citable software repositories and open datasets, generated from the BibTeX master file.
nav: true
nav_order: 4
---

<style>
  .pubnav { font-size: 0.95rem; margin: 0 0 1.5rem; }
  .pubnav a { display: inline-block; margin: 0 1.1rem 0.3rem 0; color: var(--global-text-color); border-bottom: 1px solid var(--global-divider-color); }
  .pubnav a:hover { color: var(--global-theme-color); border-bottom-color: var(--global-theme-color); text-decoration: none; }
  h2[id] { scroll-margin-top: 5rem; }
</style>

<nav class="pubnav" aria-label="Page sections">
  <a href="#software">Software and code</a>
  <a href="#datasets">Datasets and materials</a>
  <a href="#repositories">Other repositories</a>
</nav>

## Software and code {#software}

<div class="publications">

{% bibliography -q @*[section=software] %}

</div>

## Datasets and supplementary materials {#datasets}

<div class="publications">

{% bibliography -q @*[section=data] %}

</div>

## Other repositories {#repositories}

- Figshare: [current account](https://figshare.com/authors/Fabio_Caraffini/820869) and [De Montfort University archive](https://figshare.dmu.ac.uk/authors/Fabio_Caraffini/6657968).
- GitHub: [facaraff](https://github.com/facaraff).
