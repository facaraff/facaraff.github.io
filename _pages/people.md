---
layout: page
permalink: /people/
title: people
description: Research group and postgraduate supervision.
nav: true
nav_order: 7
---

{% assign cur = site.data.students | where: "status", "current" %}
{% assign inc = site.data.students | where: "status", "incoming" %}
{% assign phd1 = cur | where: "level", "PhD" | where: "role", "first" %}
{% assign phd2 = cur | where: "level", "PhD" | where: "role", "second" %}
{% assign msc = cur | where: "level", "MSc by Research" %}

## Current postgraduate researchers

- **{{ phd1.size }}** PhD students, as first supervisor (Swansea University)
- **{{ phd2.size }}** PhD students, as second supervisor (Swansea University)
- **{{ msc.size }}** MSc by Research student (Swansea University)

## Joining January 2027

- **{{ inc.size }}** PhD students, as first supervisor

## Alumni (completed PhDs)

<ul>
  {% for a in site.data.alumni %}
    <li><strong>{{ a.name }}</strong>{% if a.date != nil %}, {{ a.date }}{% endif %}, {{ a.institution }}</li>
  {% endfor %}
</ul>

Five PhDs were completed at De Montfort University, UK, and one at Pontifical Xavierian University, Colombia.

## External supervision

Invited external supervisor of 1 MSc student (Leiden University), 2 PhD students (Pontifical Xavierian University), 2 PhD students (De Montfort University) and 2 PhD students (University of Limerick, ongoing).

Individual student profiles will appear here once each student has agreed to be listed.

Interested in a PhD? Please [get in touch](mailto:fabio.caraffini@swansea.ac.uk) with a short research proposal and CV.
