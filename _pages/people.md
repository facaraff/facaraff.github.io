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

<ul>
  {% for s in cur %}
    {% if s.title %}
      <li>{{ s.title }} <em>({{ s.level }}, {{ s.role }} supervisor)</em></li>
    {% endif %}
  {% endfor %}
</ul>

## Joining January 2027

- **{{ inc.size }}** PhD students, as first supervisor

<ul>
  {% for s in inc %}
    {% if s.title %}
      <li>{{ s.title }} <em>(PhD, {{ s.role }} supervisor)</em></li>
    {% endif %}
  {% endfor %}
</ul>

## Alumni (completed PhDs)

<ul>
  {% for a in site.data.alumni %}
    <li>
      <strong>{{ a.name }}</strong>{% if a.date != nil %}, {{ a.date }}{% endif %}, {{ a.institution }}
      {% if a.thesis %}<br><em>{{ a.thesis }}</em>{% endif %}
      {% if a.url %} <a href="{{ a.url }}">e-thesis</a>{% endif %}
    </li>
  {% endfor %}
</ul>

**{{ site.data.alumni.size }}** PhDs completed as first supervisor.

## External supervision

Invited external supervisor of 1 MSc student (Leiden University), 2 PhD students (Pontifical Xavierian University), 2 PhD students (De Montfort University) and 2 PhD students (University of Limerick, ongoing).

Individual student profiles will appear here once each student has agreed to be listed.

Interested in a PhD? Please [get in touch](mailto:fabio.caraffini@swansea.ac.uk) with a short research proposal and CV.
