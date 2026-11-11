---
layout: page
permalink: /talks/
title: Talks
description: Invited talks and tutorials, with slides where available.
nav: true
nav_order: 9
---

<ul>
  {% for t in site.data.talks %}
    <li>
      <strong>{{ t.title }}</strong>, {{ t.event }}, {{ t.place }} ({{ t.date }})
      {% if t.slides %}
        <a href="{{ '/assets/pdf/talks/' | append: t.slides | relative_url }}">Slides (PDF)</a>
      {% endif %}
    </li>
  {% endfor %}
</ul>
