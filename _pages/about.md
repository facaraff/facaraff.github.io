---
layout: about
title: about
permalink: /
subtitle: Associate Professor in Artificial Intelligence · Swansea University, UK

selected_papers: false
social: true

announcements:
  enabled: false
latest_posts:
  enabled: false
---

I currently serve as an Associate Professor of Artificial Intelligence at Swansea University, where my work centres on fundamental research in optimisation and machine learning alongside their applications to interdisciplinary problems.

My academic background includes a Ph.D. in Mathematical Information Technology from the University of Jyväskylä, Finland (2016), preceded by a Ph.D. in Computer Science from De Montfort University, U.K. (2014). Earlier, I earned an M.Sc. in Telecommunications Engineering (2011) and a B.Sc. in Electronics Engineering (2008), both from the University of Perugia, Italy.

I am the founding counsellor of the Swansea IEEE Student Branch and the _Foundation and Methods for Modelling, Data Science and AI_ theme lead within the [Zienkiewicz Institute](https://zienkiewicz.institute/).

**Contact:** Room 219 (second floor), Computational Foundry, Bay Campus, Swansea University.

<style>
.social .contact-icons{font-size:3rem!important}
.social .contact-icons a,.social .contact-icons a i{font-size:inherit!important}
.rv{margin-top:2rem}
.rv h3{margin-bottom:.75rem}
.rv h4{font-size:1rem;margin:1.25rem 0 .5rem}
.rv-cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(13.5rem,1fr));gap:.7rem}
.rv-card{display:grid;align-content:start;grid-template-columns:auto 1fr;gap:.2rem .7rem;align-items:center;padding:.8rem .9rem;border:1px solid var(--global-divider-color);border-left:4px solid hsl(var(--h) 55% 50%);border-radius:.6rem;color:var(--global-text-color);background:var(--global-card-bg-color,transparent);transition:transform .15s,box-shadow .15s}
.rv-card:hover{transform:translateY(-2px);box-shadow:0 4px 14px rgba(0,0,0,.12);text-decoration:none;color:var(--global-text-color)}
.rv-ic{width:2.4rem;height:2.4rem;border-radius:50%;background:hsl(var(--h) 55% 50%);color:#fff;display:flex;align-items:center;justify-content:center;font-size:1.05rem}
.rv-n{justify-self:end;font-size:1.6rem;font-weight:600;line-height:1;color:hsl(var(--h) 55% 50%)}
.rv-l{grid-column:1/-1;font-weight:600;line-height:1.3;margin-top:.3rem}
.rv-d{grid-column:1/-1;font-size:.8rem;color:var(--global-text-color-light);line-height:1.35}
.rv-bar{grid-column:1/-1;height:5px;border-radius:3px;background:var(--global-divider-color);margin-top:.4rem;overflow:hidden}
.rv-bar span{display:block;height:100%;background:hsl(var(--h) 55% 50%);border-radius:3px}
.rv-bars{display:flex;align-items:flex-end;gap:3px;height:150px;border-bottom:1px solid var(--global-divider-color)}
.rv-col{flex:1;min-width:0;height:100%;display:flex;flex-direction:column;justify-content:flex-end}
.rv-seg{width:100%}
.rv-seg.j{background:var(--global-theme-color)}
.rv-seg.c{background:var(--global-theme-color);opacity:.55}
.rv-seg.o{background:var(--global-text-color);opacity:.3}
.rv-years{display:flex;gap:3px;font-size:.7rem;color:var(--global-text-color-light)}
.rv-years span{flex:1;min-width:0;text-align:center}
.rv-legend{font-size:.8rem;color:var(--global-text-color-light);margin-top:.4rem}
.rv-legend i{display:inline-block;width:.7rem;height:.7rem;margin:0 .25rem 0 .75rem;vertical-align:middle}
.rv-legend i:first-child{margin-left:0}
.rv-tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(7.5rem,1fr));gap:.6rem}
.rv-tile{border:1px solid var(--global-divider-color);border-radius:.5rem;padding:.6rem .7rem;text-align:center}
.rv-tile b{display:block;font-size:1.6rem;line-height:1.2;color:var(--global-theme-color)}
.rv-tile span{font-size:.8rem;color:var(--global-text-color-light)}
@media (max-width:576px){.rv-years span:nth-child(even){visibility:hidden}}
</style>

{% assign st = site.data.publication_stats %}
{% assign maxc = st.themes | map: "count" | sort | last %}
{% assign maxy = 1 %}
{% for y in st.years %}{% assign tot = y.journal | plus: y.conference | plus: y.other %}{% if tot > maxy %}{% assign maxy = tot %}{% endif %}{% endfor %}
{% assign cur = site.data.supervision | where: "status", "current" %}
{% assign done = site.data.supervision | where: "status", "completed" %}

<div class="rv">
<h3>Research at a glance</h3>
<h4>Research themes</h4>
<div class="rv-cards">
{% for th in site.data.research_themes %}{% assign c = st.themes | where: "id", th.id | first %}<a class="rv-card" href="{{ '/publications/' | relative_url }}" style="--h:{{ th.hue }}" title="{{ c.count }} papers"><span class="rv-ic"><i class="fa-solid {{ th.icon }}" aria-hidden="true"></i></span><span class="rv-n">{{ c.count }}</span><span class="rv-l">{{ th.label }}</span><span class="rv-d">{{ th.blurb }}</span><span class="rv-bar"><span style="width:{{ c.count | times: 100.0 | divided_by: maxc }}%"></span></span></a>
{% endfor %}
</div>
<h4>Publications per year</h4>
<div class="rv-bars" role="img" aria-label="Bar chart of {{ st.total }} publications by year, split into journal articles, conference papers and other outputs">
{% for y in st.years %}{% assign tot = y.journal | plus: y.conference | plus: y.other %}<div class="rv-col" title="{{ y.year }}: {{ y.journal }} journal, {{ y.conference }} conference, {{ y.other }} other"><div class="rv-seg o" style="height:{{ y.other | times: 100.0 | divided_by: maxy }}%"></div><div class="rv-seg c" style="height:{{ y.conference | times: 100.0 | divided_by: maxy }}%"></div><div class="rv-seg j" style="height:{{ y.journal | times: 100.0 | divided_by: maxy }}%"></div></div>
{% endfor %}
</div>
<div class="rv-years">
{% for y in st.years %}<span>{{ y.year | slice: 2, 2 }}</span>{% endfor %}
</div>
<div class="rv-legend"><i class="rv-seg j"></i>Journal<i class="rv-seg c"></i>Conference<i class="rv-seg o"></i>Other (chapters, editorials)</div>
<h4>Activity</h4>
<div class="rv-tiles">
<div class="rv-tile"><b>{{ st.total }}</b><span>publications</span></div>
<div class="rv-tile"><b>{{ site.data.activity.associate_editor }}</b><span>journals as Associate Editor</span></div>
<div class="rv-tile"><b>{{ site.data.activity.grants_secured }}</b><span>grants secured</span></div>
<div class="rv-tile"><b>{{ cur.size }}</b><span>current and incoming students</span></div>
<div class="rv-tile"><b>{{ done.size }}</b><span>completed supervisions</span></div>
<div class="rv-tile"><b>{{ site.data.talks.size }}</b><span>invited talks</span></div>
</div>
</div>
<script>
document.addEventListener("DOMContentLoaded",function(){var s=document.querySelector(".social"),r=document.querySelector(".rv");if(s&&r){s.insertAdjacentElement("afterend",r);}});
</script>