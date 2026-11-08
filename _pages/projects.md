---
layout: page
title: projects
permalink: /projects/
description: Funded research projects.
nav: true
nav_order: 3
---

{% for p in site.data.projects %}

### {{ p.title }}

{{ p.funder }} · {{ p.year }} · {{ p.role }} · {{ p.amount }}{% if p.partner %} · Partner: {{ p.partner }}{% endif %}

{{ p.summary }}

{% endfor %}

Further funding is listed on the [CV]({{ '/cv/' | relative_url }}).
