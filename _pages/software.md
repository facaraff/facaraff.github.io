---
layout: page
permalink: /software/
title: software & data
description: Citable software repositories and open datasets, generated from the BibTeX master file.
nav: true
nav_order: 4
---

<style>
  .pubnav { font-size: 0.9rem; margin: 0 0 1.5rem; }
  .pubnav a { display: inline-block; margin: 0 0.9rem 0.3rem 0; color: var(--global-text-color); border-bottom: 1px solid transparent; }
  .pubnav a:hover { color: var(--global-theme-color); border-bottom-color: var(--global-theme-color); text-decoration: none; }
  h2[id] { scroll-margin-top: 5rem; }
  @media (min-width: 1250px) {
    .pubnav { position: fixed; top: 9rem; left: max(1rem, calc(50% - 760px)); width: 11rem; margin: 0; }
    .pubnav a { display: block; margin: 0 0 0.55rem; padding-left: 0.6rem; border-left: 2px solid var(--global-divider-color); border-bottom: 0; }
    .pubnav a:hover { border-left-color: var(--global-theme-color); }
  }
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
