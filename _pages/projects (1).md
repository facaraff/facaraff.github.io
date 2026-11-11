---
layout: page
title: Projects
permalink: /projects/
description: Funded research projects.
nav: true
nav_order: 3
toc:
  sidebar: left
---

{% for p in site.data.projects %}

### {{ p.title }}

{{ p.funder }} · {{ p.year }} · {{ p.role }} · {{ p.amount }}{% if p.partner %} · Partner: {{ p.partner }}{% endif %}

{{ p.summary }}

{% if p.links %}<p>{% for l in p.links %}<a href="{{ l.url }}">{{ l.label }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}</p>{% endif %}

{% endfor %}

Further funding is listed on the [CV]({{ '/cv/' | relative_url }}).
