---
layout: page
permalink: /people/
title: People
description: Research group and postgraduate supervision.
nav: true
nav_order: 7
toc:
  sidebar: left
---

{% assign cur = site.data.supervision | where: "status", "current" %}
{% assign done = site.data.supervision | where: "status", "completed" %}
{% assign cur_phd = cur | where: "level", "PhD" %}
{% assign cur_first = cur_phd | where: "role", "first" %}
{% assign cur_second = cur_phd | where: "role", "second" %}
{% assign cur_msc = cur | where: "level", "MSc by Research" %}
{% assign cur_taught = cur | where: "level", "MSc" %}
{% assign cur_inst = cur | group_by: "institution" %}
{% assign done_phd = done | where: "level", "PhD" %}
{% assign done_first = done_phd | where: "role", "first" %}
{% assign done_second = done_phd | where: "role", "second" %}
{% assign done_msc = done | where: "level", "MSc by Research" %}
{% assign done_taught = done | where: "level", "MSc" %}
{% assign done_inst = done | group_by: "institution" %}

<p><small class="text-muted"><em>Note: where a name is missing, I have not yet sought consent to display it. These students are still included in the counts.</em></small></p>

## Current postgraduate researchers

**{{ cur.size }}** current and incoming students.

- **{{ cur_first.size }}** PhD students as first supervisor
- **{{ cur_second.size }}** PhD students as second supervisor
- **{{ cur_msc.size }}** MSc (by research) students
{% if cur_taught.size > 0 %}- **{{ cur_taught.size }}** MSc (taught) dissertation students
{% endif %}

By institution:
{% for g in cur_inst %}{{ g.name }}: **{{ g.items.size }}**{% unless forloop.last %} · {% endunless %}{% endfor %}

<ul>
  {% for p in cur %}
    <li>
      {% if p.name %}<strong>{{ p.name }}</strong>, {{ p.level }}{% else %}<strong>{{ p.level }} student</strong>{% endif %}
      · {{ p.role }} supervisor · {{ p.institution }}{% if p.start %} · starts {{ p.start }}{% endif %}
      {% if p.title %}<br><em>{{ p.title }}</em>{% endif %}
      {% if p.url %} <a href="{{ p.url }}">link</a>{% endif %}
    </li>
  {% endfor %}
</ul>

## Alumni (completed)

**{{ done.size }}** completed supervisions.

- **{{ done_first.size }}** PhDs as first supervisor
- **{{ done_second.size }}** PhDs as second supervisor
- **{{ done_msc.size }}** MSc (by research) students
{% if done_taught.size > 0 %}- **{{ done_taught.size }}** MSc (taught) dissertation students
{% endif %}

By institution:
{% for g in done_inst %}{{ g.name }}: **{{ g.items.size }}**{% unless forloop.last %} · {% endunless %}{% endfor %}

<ul>
  {% for p in done %}
    <li>
      {% if p.name %}<strong>{{ p.name }}</strong>, {{ p.level }}{% else %}<strong>{{ p.level }} student</strong>{% endif %}
      · {{ p.role }} supervisor · {{ p.institution }}{% if p.year %} · {{ p.year }}{% endif %}
      {% if p.title %}<br><em>{{ p.title }}</em>{% endif %}
      {% if p.url %} <a href="{{ p.url }}">thesis</a>{% endif %}
    </li>
  {% endfor %}
</ul>

Interested in a PhD? Please [get in touch](mailto:fabio.caraffini@swansea.ac.uk) with a short research proposal and CV.
