"""Render the self-contained interactive HTML dashboard.

Design constraints this file honours:

* **Self-contained.** The snapshot is embedded as a JSON island, so the page
  works identically from ``file://``, from GitHub Pages, or from a zip. No CDN,
  no fetch, no build step, no runtime dependency.
* **Charts are hand-drawn SVG.** No chart library - which is also why the page
  has zero supply chain.
* **Dark by default** (the brief prefers it) with a light theme that is *stepped
  for its own surface*, not an inverted copy.
* **Every chart has a table twin.** Colour never carries meaning alone; the
  tooltip enhances, it never gates.
"""

from __future__ import annotations

import json

PLACEHOLDER = "__PULSE_DATA__"


def render(snapshot: dict) -> str:
    payload = json.dumps(snapshot, separators=(",", ":"))
    payload = payload.replace("</", "<\\/")  # never break out of the script tag
    return TEMPLATE.replace(PLACEHOLDER, payload)


TEMPLATE = r"""<!doctype html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Solana Ecosystem Pulse</title>
<meta name="description" content="An auto-updating dashboard for the state of the Solana ecosystem - network, validators, economics and anomalies, from keyless public data.">
<style>
:root{
  color-scheme: dark;
  --page:#0d0d0d; --surface:#1a1a19; --surface-2:#211f1f;
  --ink:#ffffff; --ink-2:#c3c2b7; --muted:#898781;
  --grid:#2c2c2a; --axis:#383835; --hairline:rgba(255,255,255,.10);
  --s1:#3987e5; --s2:#d95926; --s3:#199e70; --s4:#c98500;
  --good:#0ca30c; --warning:#fab219; --serious:#ec835a; --critical:#d03b3b;
  --up:#0ca30c; --down:#d03b3b;
  --radius:14px;
  --font: system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
}
html[data-theme="light"]{
  color-scheme: light;
  --page:#f9f9f7; --surface:#fcfcfb; --surface-2:#f2f1ed;
  --ink:#0b0b0b; --ink-2:#52514e; --muted:#898781;
  --grid:#e1e0d9; --axis:#c3c2b7; --hairline:rgba(11,11,11,.10);
  --s1:#2a78d6; --s2:#eb6834; --s3:#1baf7a; --s4:#eda100;
  --up:#006300; --down:#d03b3b;
}
*{box-sizing:border-box}
body{margin:0;background:var(--page);color:var(--ink);font-family:var(--font);
     font-size:15px;line-height:1.55;-webkit-font-smoothing:antialiased}
a{color:var(--s1)}
.wrap{max-width:1280px;margin:0 auto;padding:28px 20px 80px}
header.top{display:flex;flex-wrap:wrap;gap:16px;align-items:flex-start;justify-content:space-between;
           padding-bottom:20px;border-bottom:1px solid var(--hairline);margin-bottom:26px}
.brand h1{font-size:22px;margin:0 0 4px;letter-spacing:-.01em;font-weight:650}
.brand p{margin:0;color:var(--ink-2);font-size:13.5px;max-width:60ch}
.meta{color:var(--muted);font-size:12.5px;margin-top:8px;font-variant-numeric:tabular-nums}
.controls{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
button,select{font:inherit;font-size:13px;color:var(--ink-2);background:var(--surface);
       border:1px solid var(--hairline);border-radius:8px;padding:7px 12px;cursor:pointer;
       transition:background .12s ease,color .12s ease}
button:hover,select:hover{background:var(--surface-2);color:var(--ink)}
button:focus-visible,select:focus-visible,[tabindex]:focus-visible{outline:2px solid var(--s1);outline-offset:2px}
button[aria-pressed="true"]{background:var(--s1);border-color:var(--s1);color:#fff}
.filterbar{display:flex;flex-wrap:wrap;gap:14px;align-items:center;justify-content:space-between;
           background:var(--surface);border:1px solid var(--hairline);border-radius:var(--radius);
           padding:12px 16px;margin-bottom:26px}
.filterbar .group{display:flex;gap:8px;align-items:center}
.filterbar .lbl{font-size:12px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}

/* ---- status banner ---- */
.status{display:flex;gap:14px;align-items:flex-start;border:1px solid var(--hairline);
        border-radius:var(--radius);padding:16px 18px;background:var(--surface);margin-bottom:26px}
.status .dot{width:12px;height:12px;border-radius:50%;margin-top:6px;flex:none}
.status h2{margin:0 0 2px;font-size:16px;font-weight:620}
.status p{margin:0;color:var(--ink-2);font-size:13.5px}
.sev-good{background:var(--good)} .sev-warning{background:var(--warning)}
.sev-serious{background:var(--serious)} .sev-critical{background:var(--critical)}

/* ---- hero + tiles ---- */
.hero{background:var(--surface);border:1px solid var(--hairline);border-radius:var(--radius);
      padding:22px 24px;margin-bottom:16px;display:flex;flex-wrap:wrap;gap:26px;align-items:flex-end;
      justify-content:space-between}
.hero .lab{font-size:12.5px;text-transform:uppercase;letter-spacing:.07em;color:var(--muted);margin-bottom:4px}
.hero .val{font-size:clamp(40px,7vw,60px);font-weight:660;line-height:1;letter-spacing:-.02em}
.hero .sub{color:var(--ink-2);font-size:13.5px;margin-top:8px}
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(184px,1fr));gap:12px;margin-bottom:26px}
.tile{background:var(--surface);border:1px solid var(--hairline);border-radius:12px;padding:14px 16px}
.tile .lab{font-size:11.5px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.tile .val{font-size:24px;font-weight:620;margin-top:5px;letter-spacing:-.01em}
.tile .sub{font-size:12.5px;color:var(--ink-2);margin-top:3px}
.delta{font-size:12.5px;font-weight:600}
.delta.up{color:var(--up)} .delta.down{color:var(--down)} .delta.flat{color:var(--muted)}
.meter{height:6px;border-radius:3px;background:var(--grid);margin-top:9px;overflow:hidden}
.meter i{display:block;height:100%;background:var(--s1);border-radius:3px}

/* ---- cards / charts ---- */
h2.section{font-size:13px;text-transform:uppercase;letter-spacing:.09em;color:var(--muted);
           margin:34px 0 12px;font-weight:600}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(420px,1fr));gap:16px;align-items:start}
.card{background:var(--surface);border:1px solid var(--hairline);border-radius:var(--radius);
      padding:18px 18px 12px;min-width:0}
.card header{display:flex;justify-content:space-between;align-items:flex-start;gap:12px;margin-bottom:2px}
.card h3{margin:0;font-size:15px;font-weight:620}
.card .cap{margin:2px 0 12px;color:var(--ink-2);font-size:12.5px}
.card .chart{position:relative;width:100%}
.card svg{display:block;width:100%;overflow:visible}
.legend{display:flex;flex-wrap:wrap;gap:14px;margin:2px 0 8px}
.legend span{display:inline-flex;align-items:center;gap:7px;font-size:12.5px;color:var(--ink-2)}
.legend i{width:16px;height:2px;border-radius:1px;display:block}
.legend i.box{width:11px;height:11px;border-radius:3px}
.tbl-toggle{font-size:12px;padding:5px 10px}
table{width:100%;border-collapse:collapse;font-size:12.5px;font-variant-numeric:tabular-nums;margin-top:6px}
th,td{text-align:right;padding:6px 8px;border-bottom:1px solid var(--hairline);white-space:nowrap}
th:first-child,td:first-child{text-align:left}
th{color:var(--muted);font-weight:600;font-size:11.5px;text-transform:uppercase;letter-spacing:.05em}
.scroll{overflow-x:auto;max-height:340px;overflow-y:auto}
.tblwrap{overflow-x:auto;max-width:100%}
.hidden{display:none}
.tip{position:absolute;pointer-events:none;background:var(--surface-2);border:1px solid var(--hairline);
     border-radius:9px;padding:9px 11px;font-size:12.5px;box-shadow:0 8px 26px rgba(0,0,0,.35);
     min-width:140px;z-index:5;opacity:0;transition:opacity .1s ease}
.tip .t{color:var(--muted);font-size:11.5px;margin-bottom:5px}
.tip .row{display:flex;align-items:center;gap:8px;justify-content:space-between}
.tip .row .k{display:flex;align-items:center;gap:7px;color:var(--ink-2)}
.tip .row .k i{width:14px;height:2px;border-radius:1px;display:block}
.tip .row .v{font-weight:640;color:var(--ink);font-variant-numeric:tabular-nums}

/* ---- findings ---- */
.findings{display:grid;gap:10px;align-items:start}
.finding{display:flex;gap:12px;align-items:flex-start;background:var(--surface);
         border:1px solid var(--hairline);border-left-width:3px;border-radius:10px;padding:13px 15px}
.finding.critical{border-left-color:var(--critical)} .finding.serious{border-left-color:var(--serious)}
.finding.warning{border-left-color:var(--warning)} .finding.info{border-left-color:var(--s1)}
.finding .ico{flex:none;width:20px;height:20px;margin-top:1px}
.finding h4{margin:0 0 3px;font-size:13.5px;font-weight:620}
.finding p{margin:0;color:var(--ink-2);font-size:12.5px}
.chip{display:inline-block;font-size:10.5px;text-transform:uppercase;letter-spacing:.06em;
      border:1px solid var(--hairline);border-radius:999px;padding:1px 8px;color:var(--muted);margin-left:8px}

/* ---- lists ---- */
.news{display:grid;gap:14px}
.news a{font-weight:600;text-decoration:none;font-size:14px}
.news a:hover{text-decoration:underline}
.news .when{color:var(--muted);font-size:12px;font-variant-numeric:tabular-nums}
.news p{margin:3px 0 0;color:var(--ink-2);font-size:12.5px}
footer{margin-top:46px;padding-top:20px;border-top:1px solid var(--hairline);
       color:var(--muted);font-size:12.5px}
footer code{background:var(--surface);padding:2px 6px;border-radius:5px;color:var(--ink-2)}
.srcs{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:8px;margin-top:12px}
.src{display:flex;align-items:center;gap:8px;font-size:12px;color:var(--ink-2)}
.src .pip{width:8px;height:8px;border-radius:50%;flex:none}
@media (max-width:760px){ .grid{grid-template-columns:1fr} .wrap{padding:18px 14px 60px} }
@media print{ body{background:#fff} .controls,.tbl-toggle{display:none} }
</style>
</head>
<body>
<div class="wrap">
  <header class="top">
    <div class="brand">
      <h1>Solana Ecosystem Pulse</h1>
      <p>An auto-updating picture of the Solana network, its validators, its economy and anything currently
         out of the ordinary &mdash; assembled entirely from public, keyless data sources.</p>
      <div class="meta" id="meta"></div>
    </div>
    <div class="controls">
      <button id="themeBtn" type="button" aria-label="Toggle colour theme">Light theme</button>
      <a href="./data/latest.json" download style="text-decoration:none"><button type="button">Download JSON</button></a>
    </div>
  </header>

  <div class="filterbar">
    <div class="group">
      <span class="lbl">Time range</span>
      <div class="group" id="rangeBtns" role="group" aria-label="Time range for the historical charts">
        <button type="button" data-days="30">30d</button>
        <button type="button" data-days="90" aria-pressed="true">90d</button>
        <button type="button" data-days="180">180d</button>
        <button type="button" data-days="0">All</button>
      </div>
    </div>
    <div class="group">
      <span class="lbl">Scopes every historical chart below</span>
    </div>
  </div>

  <div class="status" id="status"></div>

  <div class="hero" id="hero"></div>
  <div class="tiles" id="tiles"></div>

  <h2 class="section">Anomaly detection</h2>
  <div class="findings" id="findings"></div>

  <h2 class="section">Economics</h2>
  <div class="grid" id="econ"></div>

  <h2 class="section">Network &amp; validators</h2>
  <div class="grid" id="net"></div>

  <h2 class="section">Ecosystem</h2>
  <div class="grid" id="eco"></div>

  <h2 class="section">News, releases &amp; upcoming upgrades</h2>
  <div class="grid" id="news"></div>

  <footer>
    <div id="footmeta"></div>
    <div class="srcs" id="srcs"></div>
  </footer>
</div>

<script type="application/json" id="pulse-data">__PULSE_DATA__</script>
<script>
(function(){
"use strict";
var D = JSON.parse(document.getElementById('pulse-data').textContent);
var RANGE_DAYS = 90;
var charts = [];

/* ------------------------------------------------------------------ utils */
function el(tag, cls, text){ var n=document.createElement(tag); if(cls) n.className=cls;
  if(text!==undefined && text!==null) n.textContent=String(text); return n; }
function dig(o, path){ var c=o; var p=path.split('.');
  for(var i=0;i<p.length;i++){ if(c===null||c===undefined||typeof c!=='object') return null; c=c[p[i]]; }
  return (c===undefined)?null:c; }
function isNum(v){ return typeof v==='number' && isFinite(v); }
function cssVar(name){ return getComputedStyle(document.documentElement).getPropertyValue(name).trim(); }

function usd(v, dp){
  if(!isNum(v)) return 'n/a';
  var a=Math.abs(v), u=[[1e12,'T'],[1e9,'B'],[1e6,'M'],[1e3,'K']];
  for(var i=0;i<u.length;i++){ if(a>=u[i][0]) return '$'+(v/u[i][0]).toFixed(2)+u[i][1]; }
  return '$'+v.toFixed(dp===undefined?2:dp);
}
function compact(v){
  if(!isNum(v)) return 'n/a';
  var a=Math.abs(v), u=[[1e12,'T'],[1e9,'B'],[1e6,'M'],[1e3,'K']];
  for(var i=0;i<u.length;i++){ if(a>=u[i][0]) return (v/u[i][0]).toFixed(a/u[i][0]>=100?0:1)+u[i][1]; }
  return v.toFixed(Math.abs(v)<10?1:0);
}
function num(v, dp){ return isNum(v) ? v.toLocaleString('en-US',{minimumFractionDigits:dp||0,maximumFractionDigits:dp||0}) : 'n/a'; }
function pct(v, dp){ return isNum(v) ? v.toFixed(dp===undefined?2:dp)+'%' : 'n/a'; }
function signedPct(v, dp){ return isNum(v) ? (v>=0?'+':'')+v.toFixed(dp===undefined?2:dp)+'%' : 'n/a'; }
function day(ts){ var d=new Date(ts*1000);
  return d.toLocaleDateString('en-US',{month:'short',day:'numeric',timeZone:'UTC'}); }
function dayYear(ts){ var d=new Date(ts*1000);
  return d.toLocaleDateString('en-US',{year:'numeric',month:'short',day:'numeric',timeZone:'UTC'}); }
function clockUTC(ts){ var d=new Date(ts*1000);
  return d.toISOString().slice(11,16)+' UTC'; }
/* x labels for the per-minute performance charts, whose x axis is a sample index */
function minsAgo(i, total){ var m=Math.round(total-1-i); return m<=0 ? 'now' : ('-'+m+' min'); }

function deltaEl(v, dp){
  var s = el('span','delta '+(!isNum(v)?'flat':(v>0?'up':(v<0?'down':'flat'))));
  s.textContent = isNum(v) ? (v>0?'▲ ':(v<0?'▼ ':'')) + Math.abs(v).toFixed(dp===undefined?2:dp)+'%' : '';
  return s;
}
function trim(points){
  if(!points || !points.length) return [];
  if(!RANGE_DAYS) return points;
  var cut = points[points.length-1].t - RANGE_DAYS*86400;
  var out = points.filter(function(p){ return p.t >= cut; });
  return out.length>1 ? out : points.slice(-2);
}

/* --------------------------------------------------------------- svg core */
var NS='http://www.w3.org/2000/svg';
function svgEl(tag, attrs){ var n=document.createElementNS(NS,tag);
  for(var k in attrs){ if(attrs[k]!==null && attrs[k]!==undefined) n.setAttribute(k,attrs[k]); } return n; }

function niceTicks(min, max, count){
  if(min===max){ max = min===0 ? 1 : min*1.1; }
  var span=(max-min)/Math.max(1,count), mag=Math.pow(10,Math.floor(Math.log(span)/Math.LN10)),
      norm=span/mag, step;
  step = norm<1.5?1:(norm<3?2:(norm<7?5:10));
  step*=mag;
  var ticks=[], t=Math.ceil(min/step)*step;
  for(; t<=max+step*0.001; t+=step){ ticks.push(Math.round(t/step)*step); }
  return ticks;
}

/* Line / area chart. spec:
   {series:[{name,color,points:[{t,v}]}], zero:bool, area:bool, fmt:fn, yfmt:fn} */
function drawLine(host, spec){
  host.textContent='';
  var W = host.clientWidth || 560, H = spec.height || 230;
  var compactMode = (spec.height || 230) < 140;
  var padL = compactMode ? 44 : 58, padR = 16, padT = 12, padB = compactMode ? 22 : 30;
  var series = spec.series.filter(function(s){ return s.points && s.points.length>1; });
  if(!series.length){ host.appendChild(el('p','cap','No data available for this range.')); return; }

  var allT=[], allV=[];
  series.forEach(function(s){ s.points.forEach(function(p){ allT.push(p.t); allV.push(p.v); }); });
  var t0=Math.min.apply(null,allT), t1=Math.max.apply(null,allT);
  var vMin=Math.min.apply(null,allV), vMax=Math.max.apply(null,allV);
  if(spec.zero){ vMin = Math.min(0, vMin); }
  else { var pad=(vMax-vMin)*0.12 || Math.abs(vMax)*0.05 || 1; vMin-=pad; vMax+=pad; }
  if(vMax===vMin) vMax = vMin+1;

  var x=function(t){ return padL + (t1===t0?0:(t-t0)/(t1-t0))*(W-padL-padR); };
  var y=function(v){ return padT + (1-(v-vMin)/(vMax-vMin))*(H-padT-padB); };

  var svg = svgEl('svg',{viewBox:'0 0 '+W+' '+H, width:W, height:H, role:'img',
                         'aria-label':spec.aria || 'line chart'});
  var grid=cssVar('--grid'), axis=cssVar('--axis'), muted=cssVar('--muted');

  var yTickCount = (H-padT-padB) < 90 ? 2 : ((H-padT-padB) < 150 ? 3 : 4);
  niceTicks(vMin,vMax,yTickCount).forEach(function(v){
    if(v<vMin||v>vMax) return;
    svg.appendChild(svgEl('line',{x1:padL,x2:W-padR,y1:y(v).toFixed(1),y2:y(v).toFixed(1),
                                  stroke:grid,'stroke-width':1}));
    var tx=svgEl('text',{x:padL-9,y:y(v)+4,'text-anchor':'end',fill:muted,'font-size':11,
                         'font-family':'inherit','font-variant-numeric':'tabular-nums'});
    tx.textContent=(spec.yfmt||compact)(v); svg.appendChild(tx);
  });
  svg.appendChild(svgEl('line',{x1:padL,x2:W-padR,y1:H-padB,y2:H-padB,stroke:axis,'stroke-width':1}));

  var nTicks = compactMode ? 2 : (W<430?3:4);
  for(var i=0;i<=nTicks;i++){
    var tt=t0+(t1-t0)*i/nTicks;
    var lx=svgEl('text',{x:x(tt),y:H-padB+(compactMode?14:18),
                         'text-anchor':i===0?'start':(i===nTicks?'end':'middle'),
                         fill:muted,'font-size':compactMode?10:11,'font-family':'inherit'});
    lx.textContent=(spec.xfmt||day)(tt); svg.appendChild(lx);
  }

  series.forEach(function(s){
    var d='', a='';
    s.points.forEach(function(p,i){
      var px=x(p.t).toFixed(2), py=y(p.v).toFixed(2);
      d += (i?'L':'M')+px+' '+py; a += (i?'L':'M')+px+' '+py;
    });
    if(spec.area && spec.zero && series.length===1){
      a += 'L'+x(s.points[s.points.length-1].t).toFixed(2)+' '+y(Math.max(0,vMin)).toFixed(2)
        +  'L'+x(s.points[0].t).toFixed(2)+' '+y(Math.max(0,vMin)).toFixed(2)+'Z';
      svg.appendChild(svgEl('path',{d:a,fill:s.color,'fill-opacity':0.10,stroke:'none'}));
    }
    svg.appendChild(svgEl('path',{d:d,fill:'none',stroke:s.color,'stroke-width':2,
                                  'stroke-linejoin':'round','stroke-linecap':'round'}));
    var last=s.points[s.points.length-1];
    svg.appendChild(svgEl('circle',{cx:x(last.t),cy:y(last.v),r:4.5,fill:s.color,
                                    stroke:cssVar('--surface'),'stroke-width':2}));
  });

  /* direct end-label for the single-series case */
  if(series.length===1){
    var lp=series[0].points[series[0].points.length-1];
    var lbl=svgEl('text',{x:Math.min(W-padR, x(lp.t)+9),y:y(lp.v)-9,'text-anchor':'end',
                          fill:cssVar('--ink'),'font-size':12,'font-weight':620,'font-family':'inherit'});
    lbl.textContent=(spec.fmt||compact)(lp.v); svg.appendChild(lbl);
  }

  var cross = svgEl('line',{x1:0,x2:0,y1:padT,y2:H-padB,stroke:axis,'stroke-width':1,opacity:0});
  svg.appendChild(cross);
  var dots = series.map(function(s){
    var c=svgEl('circle',{r:4.5,fill:s.color,stroke:cssVar('--surface'),'stroke-width':2,opacity:0});
    svg.appendChild(c); return c;
  });
  host.appendChild(svg);

  var tip = el('div','tip'); host.appendChild(tip);
  function hide(){ tip.style.opacity=0; cross.setAttribute('opacity',0);
                   dots.forEach(function(d){ d.setAttribute('opacity',0); }); }
  function move(ev){
    var r=svg.getBoundingClientRect();
    var px=(ev.clientX!==undefined?ev.clientX:0)-r.left;
    var tt=t0+(t1-t0)*Math.max(0,Math.min(1,(px-padL)/(W-padL-padR)));
    cross.setAttribute('opacity',1);
    tip.textContent='';
    var head=el('div','t'); var shown=null;
    series.forEach(function(s,i){
      var best=s.points[0], bd=Infinity;
      s.points.forEach(function(p){ var dd=Math.abs(p.t-tt); if(dd<bd){ bd=dd; best=p; } });
      shown=best;
      cross.setAttribute('x1',x(best.t)); cross.setAttribute('x2',x(best.t));
      dots[i].setAttribute('cx',x(best.t)); dots[i].setAttribute('cy',y(best.v));
      dots[i].setAttribute('opacity',1);
      var row=el('div','row'); var k=el('div','k'); var key=el('i');
      key.style.background=s.color; key.style.width='14px'; key.style.height='2px';
      k.appendChild(key); k.appendChild(el('span',null,s.name));
      var v=el('div','v',(spec.fmt||compact)(best.v));
      row.appendChild(k); row.appendChild(v); tip.appendChild(row);
      if(i===0){ head.textContent = spec.timeLabel? spec.timeLabel(best) : dayYear(best.t); }
    });
    tip.insertBefore(head, tip.firstChild);
    tip.style.opacity=1;
    var tw=tip.offsetWidth, left=x(shown.t)+14;
    if(left+tw>W) left=x(shown.t)-tw-14;
    tip.style.left=Math.max(0,left)+'px';
    tip.style.top=(padT+6)+'px';
  }
  svg.addEventListener('pointermove',move);
  svg.addEventListener('pointerleave',hide);
  svg.setAttribute('tabindex','0');
  svg.addEventListener('focus',function(){
    var r=svg.getBoundingClientRect(); move({clientX:r.left+W-40});
  });
  svg.addEventListener('blur',hide);
}

/* Bar chart. spec:{items:[{label,value,sub}], horizontal, color, fmt, height} */
function drawBars(host, spec){
  host.textContent='';
  var items=spec.items||[];
  if(!items.length){ host.appendChild(el('p','cap','No data available.')); return; }
  var W=host.clientWidth||560;
  var color=spec.color||cssVar('--s1');
  var surface=cssVar('--surface'), muted=cssVar('--muted'), grid=cssVar('--grid');
  var maxV=Math.max.apply(null,items.map(function(i){ return Math.abs(i.value)||0; }))||1;

  if(spec.horizontal){
    var rowH=Math.min(30, Math.max(22, 300/items.length)), gap=6;
    var labW=Math.min(160, Math.max(88, W*0.28));
    var valW=74;
    var H=items.length*(rowH+gap)+8;
    var svg=svgEl('svg',{viewBox:'0 0 '+W+' '+H,width:W,height:H,role:'img','aria-label':spec.aria||'bar chart'});
    items.forEach(function(it,i){
      var y=i*(rowH+gap)+4, bh=Math.min(20,rowH-6);
      var full=W-labW-valW-8;
      var w=Math.max(2,(Math.abs(it.value)/maxV)*full);
      var lt=svgEl('text',{x:0,y:y+bh/2+4,fill:cssVar('--ink-2'),'font-size':12,'font-family':'inherit'});
      lt.textContent=it.label; svg.appendChild(lt);
      var g=svgEl('g',{}); g.setAttribute('tabindex','0');
      var track=svgEl('rect',{x:labW,y:y-3,width:full,height:bh+6,fill:'transparent'});
      g.appendChild(track);
      g.appendChild(svgEl('rect',{x:labW,y:y,width:w,height:bh,rx:4,ry:4,fill:color}));
      /* square the baseline end so growth reads from a single origin */
      g.appendChild(svgEl('rect',{x:labW,y:y,width:Math.min(4,w),height:bh,fill:color}));
      var vt=svgEl('text',{x:W,y:y+bh/2+4,'text-anchor':'end',fill:cssVar('--ink'),'font-size':12,
                           'font-weight':600,'font-family':'inherit','font-variant-numeric':'tabular-nums'});
      vt.textContent=(spec.fmt||compact)(it.value); svg.appendChild(vt);
      g.addEventListener('pointerenter',function(){ show(it,labW+w,y); });
      g.addEventListener('focus',function(){ show(it,labW+w,y); });
      g.addEventListener('pointerleave',hideTip); g.addEventListener('blur',hideTip);
      svg.appendChild(g); svg.appendChild(vt);
    });
    host.appendChild(svg);
  } else {
    var H=spec.height||210, padL=52, padR=8, padT=10, padB=34;
    var svgc=svgEl('svg',{viewBox:'0 0 '+W+' '+H,width:W,height:H,role:'img','aria-label':spec.aria||'column chart'});
    niceTicks(0,maxV,3).forEach(function(v){
      var yy=padT+(1-v/maxV)*(H-padT-padB);
      svgc.appendChild(svgEl('line',{x1:padL,x2:W-padR,y1:yy.toFixed(1),y2:yy.toFixed(1),stroke:grid,'stroke-width':1}));
      var t=svgEl('text',{x:padL-9,y:yy+4,'text-anchor':'end',fill:muted,'font-size':11,'font-family':'inherit'});
      t.textContent=(spec.yfmt||spec.fmt||compact)(v); svgc.appendChild(t);
    });
    svgc.appendChild(svgEl('line',{x1:padL,x2:W-padR,y1:H-padB,y2:H-padB,stroke:cssVar('--axis'),'stroke-width':1}));
    var band=(W-padL-padR)/items.length, bw=Math.max(1,Math.min(24,band-2));
    items.forEach(function(it,i){
      var h=Math.max(1,(Math.abs(it.value)/maxV)*(H-padT-padB));
      var xx=padL+i*band+(band-bw)/2, yy=H-padB-h;
      var g=svgEl('g',{}); g.setAttribute('tabindex','-1');
      g.appendChild(svgEl('rect',{x:padL+i*band,y:padT,width:band,height:H-padT-padB,fill:'transparent'}));
      g.appendChild(svgEl('rect',{x:xx,y:yy,width:bw,height:h,rx:Math.min(4,bw/2),ry:Math.min(4,bw/2),fill:color}));
      if(h>4) g.appendChild(svgEl('rect',{x:xx,y:H-padB-Math.min(4,h),width:bw,height:Math.min(4,h),fill:color}));
      g.addEventListener('pointerenter',function(){ show(it,xx+bw/2,yy); });
      g.addEventListener('pointerleave',hideTip);
      svgc.appendChild(g);
      if(items.length<=14 || i%Math.ceil(items.length/6)===0){
        var lx=svgEl('text',{x:xx+bw/2,y:H-padB+16,'text-anchor':'middle',fill:muted,'font-size':11,
                             'font-family':'inherit'});
        lx.textContent=it.label; svgc.appendChild(lx);
      }
    });
    host.appendChild(svgc);
  }

  var tip=el('div','tip'); host.appendChild(tip);
  function show(it, px, py){
    tip.textContent='';
    tip.appendChild(el('div','t', it.tipLabel||it.label));
    var row=el('div','row'); var k=el('div','k');
    var key=el('i'); key.style.background=color; key.style.width='11px'; key.style.height='11px';
    key.style.borderRadius='3px'; k.appendChild(key); k.appendChild(el('span',null,spec.valueName||'Value'));
    row.appendChild(k); row.appendChild(el('div','v',(spec.fmt||compact)(it.value)));
    tip.appendChild(row);
    if(it.sub){ var s=el('div','t',it.sub); s.style.marginTop='5px'; s.style.marginBottom='0'; tip.appendChild(s); }
    tip.style.opacity=1;
    var tw=tip.offsetWidth, left=px+12; if(left+tw>host.clientWidth) left=px-tw-12;
    tip.style.left=Math.max(0,left)+'px'; tip.style.top=Math.max(0,py-10)+'px';
  }
  function hideTip(){ tip.style.opacity=0; }
}

/* ------------------------------------------------------------- card maker */
function card(parent, title, caption, opts){
  var c=el('div','card');
  var h=el('header');
  var box=el('div');
  box.appendChild(el('h3',null,title));
  h.appendChild(box);
  var btn=el('button','tbl-toggle','Table'); btn.type='button'; btn.setAttribute('aria-pressed','false');
  h.appendChild(btn);
  c.appendChild(h);
  if(caption) c.appendChild(el('p','cap',caption));
  if(opts && opts.legend){
    var lg=el('div','legend');
    opts.legend.forEach(function(s){
      var sp=el('span'); var i=el('i', s.box?'box':null); i.style.background=s.color;
      sp.appendChild(i); sp.appendChild(el('span',null,s.name)); lg.appendChild(sp);
    });
    c.appendChild(lg);
  }
  var chart=el('div','chart'); c.appendChild(chart);
  var tblWrap=el('div','scroll hidden'); c.appendChild(tblWrap);
  btn.addEventListener('click',function(){
    var on = tblWrap.classList.toggle('hidden')===false;
    btn.setAttribute('aria-pressed', on?'true':'false');
    btn.textContent = on?'Chart':'Table';
    chart.classList.toggle('hidden', on);
    if(on && opts && opts.table){ tblWrap.textContent=''; tblWrap.appendChild(opts.table()); }
  });
  parent.appendChild(c);
  return {chart:chart, tableWrap:tblWrap};
}

function makeTable(cols, rows){
  var t=el('table'); var thead=el('thead'); var tr=el('tr');
  cols.forEach(function(c){ tr.appendChild(el('th',null,c)); });
  thead.appendChild(tr); t.appendChild(thead);
  var tb=el('tbody');
  rows.forEach(function(r){ var row=el('tr');
    r.forEach(function(v){ row.appendChild(el('td',null,v)); }); tb.appendChild(row); });
  t.appendChild(tb);
  var wrap=el('div','tblwrap'); wrap.appendChild(t); return wrap;
}

function register(host, fn){ charts.push({host:host, fn:fn}); fn(); }
function redrawAll(){ charts.forEach(function(c){ if(c.host.isConnected) c.fn(); }); }

/* =========================================================== BUILD THE PAGE */
var market=D.market||{}, tvl=dig(D,'defi.tvl')||{}, protos=dig(D,'defi.protocols')||{},
    stables=D.stablecoins||{}, dex=D.dex||{}, rev=D.rev||{}, perf=dig(D,'network.performance')||{},
    epoch=dig(D,'network.epoch')||{}, val=D.validators||{}, fees=D.fees||{}, derived=D.derived||{},
    anom=D.anomalies||{}, activity=D.activity||{};

/* meta */
(function(){
  var m=document.getElementById('meta');
  m.textContent='Generated '+D.generated_at+'  ·  schema '+D.schema_version
    +'  ·  '+dig(D,'collection.sources.ok')+'/'+dig(D,'collection.sources.calls')
    +' source calls OK  ·  '+dig(D,'collection.duration_secs')+'s';
})();

/* status banner */
(function(){
  var s=document.getElementById('status');
  var dot=el('div','dot sev-'+(anom.status||'good')); s.appendChild(dot);
  var box=el('div');
  box.appendChild(el('h2',null,anom.headline||'Status unknown'));
  var c=anom.counts||{};
  box.appendChild(el('p',null,
    (anom.rules_evaluated||0)+' rules evaluated · '
    +(c.critical||0)+' critical, '+(c.serious||0)+' serious, '+(c.warning||0)+' warning, '+(c.info||0)+' info'
    +' · '+(anom.history_runs_available||0)+' historical runs in the local archive'));
  s.appendChild(box);
})();

/* hero + tiles */
(function(){
  var hero=document.getElementById('hero');
  var left=el('div');
  left.appendChild(el('div','lab','Total value locked on Solana'));
  var v=el('div','val', usd(tvl.tvl_usd)); left.appendChild(v);
  var sub=el('div','sub');
  sub.appendChild(document.createTextNode('24h '));
  sub.appendChild(deltaEl(tvl.change_1d_pct));
  sub.appendChild(document.createTextNode('   ·   7d '));
  sub.appendChild(deltaEl(tvl.change_7d_pct));
  sub.appendChild(document.createTextNode('   ·   rank #'+(tvl.chain_rank_by_tvl||'?')
    +' of '+num(tvl.chains_tracked)+' chains · '+pct(tvl.share_of_all_chain_tvl_pct,1)+' of all chain TVL'));
  left.appendChild(sub);
  hero.appendChild(left);

  var right=el('div'); right.style.minWidth='260px'; right.style.flex='1'; right.style.maxWidth='420px';
  right.appendChild(el('div','lab','TVL, last 90 days'));
  var spark=el('div','chart'); right.appendChild(spark); hero.appendChild(right);
  register(spark, function(){
    drawLine(spark,{height:96, zero:true, area:true, fmt:usd, yfmt:compact,
      series:[{name:'TVL', color:cssVar('--s1'), points:(tvl.history||[]).slice(-90)}]});
  });

  var tiles=document.getElementById('tiles');
  function tile(lab, value, subNode, meterPct){
    var t=el('div','tile');
    t.appendChild(el('div','lab',lab));
    t.appendChild(el('div','val',value));
    if(subNode){ var s=el('div','sub'); if(typeof subNode==='string') s.textContent=subNode; else s.appendChild(subNode); t.appendChild(s); }
    if(isNum(meterPct)){ var m=el('div','meter'); var i=el('i'); i.style.width=Math.max(0,Math.min(100,meterPct))+'%';
      m.appendChild(i); t.appendChild(m); }
    tiles.appendChild(t);
  }
  function withDelta(prefix, v){ var s=el('span'); if(prefix) s.appendChild(document.createTextNode(prefix+' '));
    s.appendChild(deltaEl(v)); return s; }

  tile('SOL price', usd(market.price_usd, 2), withDelta('24h', market.change_24h_pct));
  tile('Market cap', usd(market.market_cap_usd), 'Rank #'+(market.market_cap_rank||'?')
    +' · vol/cap '+pct(market.volume_to_mcap_pct,1));
  tile('Stablecoin supply', usd(stables.supply_usd), withDelta('7d', stables.change_7d_pct));
  tile('DEX volume 24h', usd(dex.total_24h), withDelta('24h', dex.change_1d_pct));
  tile('Chain fees 24h (REV)', usd(dig(D,'rev.fees.total_24h')), withDelta('24h', dig(D,'rev.fees.change_1d_pct')));
  tile('Non-vote TPS', num(perf.tps_non_vote_avg,0), 'Total '+num(perf.tps_avg,0)
    +' · peak '+num(perf.tps_peak,0));
  tile('Slot time', num(perf.slot_time_ms_avg,0)+' ms', 'Target 400 ms · worst '
    +num(perf.slot_time_ms_max,0)+' ms');
  tile('Validators', num(val.active_count), num(val.delinquent_count)+' delinquent · '
    +pct(val.delinquent_stake_pct,2)+' of stake');
  tile('Nakamoto coefficient', num(val.nakamoto_coefficient), 'Top 10 hold '+pct(val.top10_stake_pct,1));
  tile('Stake rate', pct(derived.stake_rate_pct,1), usd(derived.staked_value_usd)+' staked', derived.stake_rate_pct);
  tile('Epoch '+(epoch.epoch===null?'?':epoch.epoch), pct(epoch.progress_pct,1),
       num(epoch.slots_remaining)+' slots remaining', epoch.progress_pct);
  tile('Tokenised assets', usd(dig(D,'defi.protocols.tokenized_assets.tvl_usd')),
       pct(dig(D,'defi.protocols.tokenized_assets.share_of_solana_tvl_pct'),3)+' of chain TVL');
})();

/* findings */
(function(){
  var host=document.getElementById('findings');
  var list=anom.findings||[];
  if(!list.length){
    var ok=el('div','finding info');
    ok.appendChild(icon('good'));
    var b=el('div'); b.appendChild(el('h4',null,'No anomalies detected'));
    b.appendChild(el('p',null,'All threshold rules passed and no tracked metric exceeded its z-score band.'));
    ok.appendChild(b); host.appendChild(ok); return;
  }
  list.forEach(function(f){
    var n=el('div','finding '+f.severity);
    n.appendChild(icon(f.severity));
    var b=el('div');
    var h=el('h4'); h.appendChild(document.createTextNode(f.title));
    var chip=el('span','chip', f.severity+' · '+f.engine); h.appendChild(chip);
    b.appendChild(h); b.appendChild(el('p',null,f.detail));
    n.appendChild(b); host.appendChild(n);
  });
  function _unused(){}
})();

function icon(sev){
  var c={good:'--good',info:'--s1',warning:'--warning',serious:'--serious',critical:'--critical'}[sev]||'--s1';
  var s=svgEl('svg',{viewBox:'0 0 20 20',width:20,height:20,'aria-hidden':'true'});
  s.setAttribute('class','ico');
  var col=cssVar(c);
  if(sev==='critical'||sev==='serious'||sev==='warning'){
    s.appendChild(svgEl('path',{d:'M10 2.6 18.2 17H1.8Z',fill:'none',stroke:col,'stroke-width':1.8,'stroke-linejoin':'round'}));
    s.appendChild(svgEl('path',{d:'M10 7.6v4.2',stroke:col,'stroke-width':1.8,'stroke-linecap':'round'}));
    s.appendChild(svgEl('circle',{cx:10,cy:14.4,r:1,fill:col}));
  } else if(sev==='good'){
    s.appendChild(svgEl('circle',{cx:10,cy:10,r:7.6,fill:'none',stroke:col,'stroke-width':1.8}));
    s.appendChild(svgEl('path',{d:'M6.6 10.2 9 12.6 13.6 7.8',fill:'none',stroke:col,'stroke-width':1.8,
                                'stroke-linecap':'round','stroke-linejoin':'round'}));
  } else {
    s.appendChild(svgEl('circle',{cx:10,cy:10,r:7.6,fill:'none',stroke:col,'stroke-width':1.8}));
    s.appendChild(svgEl('path',{d:'M10 9v4.6',stroke:col,'stroke-width':1.8,'stroke-linecap':'round'}));
    s.appendChild(svgEl('circle',{cx:10,cy:6.4,r:1,fill:col}));
  }
  return s;
}

/* ------------------------------------------------------------- ECONOMICS */
(function(){
  var host=document.getElementById('econ');

  var c1=card(host,'Total value locked','DeFiLlama chain TVL for Solana. Axis starts at zero.',{
    table:function(){ return makeTable(['Date','TVL (USD)'],
      trim(tvl.history||[]).slice().reverse().map(function(p){ return [dayYear(p.t), usd(p.v)]; })); }});
  register(c1.chart,function(){ drawLine(c1.chart,{zero:true,area:true,fmt:usd,aria:'Solana total value locked over time',
    series:[{name:'TVL',color:cssVar('--s1'),points:trim(tvl.history||[])}]}); });

  var c2=card(host,'SOL price','Daily close in USD. Axis is padded to the range, not zero-based.',{
    table:function(){ return makeTable(['Date','Price (USD)'],
      trim(market.price_history||[]).slice().reverse().map(function(p){ return [dayYear(p.t), '$'+p.v.toFixed(2)]; })); }});
  register(c2.chart,function(){ drawLine(c2.chart,{zero:false,fmt:function(v){return '$'+v.toFixed(2);},
    yfmt:function(v){return '$'+compact(v);},aria:'SOL price over time',
    series:[{name:'SOL',color:cssVar('--s1'),points:trim(market.price_history||[])}]}); });

  var c3=card(host,'Stablecoin supply on Solana','Total circulating stablecoin value bridged to or issued on Solana.',{
    table:function(){ return makeTable(['Date','Supply (USD)'],
      trim(stables.history||[]).slice().reverse().map(function(p){ return [dayYear(p.t), usd(p.v)]; })); }});
  register(c3.chart,function(){ drawLine(c3.chart,{zero:true,area:true,fmt:usd,aria:'Stablecoin supply over time',
    series:[{name:'Stablecoins',color:cssVar('--s1'),points:trim(stables.history||[])}]}); });

  var c4=card(host,'DEX volume, daily','Aggregate spot DEX volume across '+num(dex.protocols_tracked)+' Solana venues.',{
    table:function(){ return makeTable(['Date','Volume (USD)'],
      trim(dex.history||[]).slice().reverse().map(function(p){ return [dayYear(p.t), usd(p.v)]; })); }});
  register(c4.chart,function(){ drawBars(c4.chart,{items:trim(dex.history||[]).map(function(p){
      return {label:day(p.t), tipLabel:dayYear(p.t), value:p.v}; }),
      fmt:usd, valueName:'Volume', color:cssVar('--s1'), aria:'Daily DEX volume'}); });

  var c5=card(host,'Chain fees, daily (REV)', (rev.definition||''),{
    table:function(){ return makeTable(['Date','Fees (USD)'],
      trim(dig(D,'rev.fees.history')||[]).slice().reverse().map(function(p){ return [dayYear(p.t), usd(p.v)]; })); }});
  register(c5.chart,function(){ drawBars(c5.chart,{items:trim(dig(D,'rev.fees.history')||[]).map(function(p){
      return {label:day(p.t), tipLabel:dayYear(p.t), value:p.v}; }),
      fmt:usd, valueName:'Fees', color:cssVar('--s1'), aria:'Daily chain fees'}); });

  var dv=[];
  if(isNum(derived.tvl_to_mcap_pct)) dv.push(['TVL / market cap', pct(derived.tvl_to_mcap_pct)]);
  if(isNum(derived.stablecoins_per_tvl_dollar)) dv.push(['Stablecoin supply per $1 of DeFi TVL', '$'+derived.stablecoins_per_tvl_dollar.toFixed(2)]);
  if(isNum(derived.dex_volume_to_tvl_ratio)) dv.push(['DEX volume / TVL (daily turnover)', derived.dex_volume_to_tvl_ratio.toFixed(3)+'x']);
  if(isNum(derived.annualised_fees_to_mcap_pct)) dv.push(['Annualised fees / market cap', pct(derived.annualised_fees_to_mcap_pct)]);
  if(isNum(derived.fee_per_user_transaction_usd)) dv.push(['Chain fees per user transaction (all protocol fees)', '$'+derived.fee_per_user_transaction_usd.toFixed(6)]);
  if(isNum(derived.estimated_daily_user_transactions)) dv.push(['Estimated daily user transactions', num(derived.estimated_daily_user_transactions)]);
  if(isNum(derived.modelled_typical_fee_usd)) dv.push(['Modelled 200k-CU transaction cost', '$'+derived.modelled_typical_fee_usd.toFixed(6)]);
  if(isNum(derived.staked_value_usd)) dv.push(['Value of staked SOL', usd(derived.staked_value_usd)]);
  if(dv.length){
    var cd=el('div','card');
    var hh=el('header'); var bx=el('div'); bx.appendChild(el('h3',null,'Cross-source ratios'));
    hh.appendChild(bx); cd.appendChild(hh);
    cd.appendChild(el('p','cap','Figures that only exist because two independent sources were collected in the same run.'));
    if(protos.tvl_sum_note){ var pn=el('p','cap', 'Note on TVL: '+protos.tvl_sum_note); cd.appendChild(pn); }
    cd.appendChild(makeTable(['Ratio','Value'], dv));
    host.appendChild(cd);
  }
})();

/* -------------------------------------------------- NETWORK & VALIDATORS */
(function(){
  var host=document.getElementById('net');
  var s=(perf.series||[]);
  var total=s.map(function(p,i){ return {t:i, v:p.tps}; });
  var nonvote=s.filter(function(p){ return p.tps_non_vote!==null; }).map(function(p,i){ return {t:i, v:p.tps_non_vote}; });
  var c1=card(host,'Throughput, last '+(perf.window_minutes||0)+' minutes',
    'One point per 60-second performance sample from getRecentPerformanceSamples. Newest on the right.',{
    legend:[{name:'All transactions',color:cssVar('--s1')},{name:'Non-vote (user) transactions',color:cssVar('--s2')}],
    table:function(){ return makeTable(['Sample','Slot','TPS (all)','TPS (non-vote)','Slot time (ms)'],
      s.slice().reverse().map(function(p,i){ return [String(s.length-i), num(p.slot), num(p.tps,1),
        num(p.tps_non_vote,1), num(p.slot_time_ms,1)]; })); }});
  register(c1.chart,function(){
    drawLine(c1.chart,{zero:true,fmt:function(v){return num(v,0)+' TPS';},yfmt:function(v){return compact(v);},
      aria:'Transactions per second over the last hour',
      timeLabel:function(p){ return minsAgo(p.t, s.length)+' · sample '+(p.t+1)+' of '+s.length; },
      xfmt:function(v){ return minsAgo(v, s.length); },
      series:[{name:'All transactions',color:cssVar('--s1'),points:total},
              {name:'Non-vote (user)',color:cssVar('--s2'),points:nonvote}]});
  });

  var slot=s.filter(function(p){ return p.slot_time_ms!==null; }).map(function(p,i){ return {t:i, v:p.slot_time_ms}; });
  var c2=card(host,'Slot time, last '+(perf.window_minutes||0)+' minutes','Milliseconds per slot. Solana targets 400 ms.',{
    table:function(){ return makeTable(['Sample','Slot time (ms)'],
      slot.slice().reverse().map(function(p){ return [String(p.t+1), num(p.v,1)]; })); }});
  register(c2.chart,function(){
    drawLine(c2.chart,{zero:true,area:true,fmt:function(v){return num(v,0)+' ms';},yfmt:function(v){return num(v,0);},
      aria:'Slot time over the last hour',
      timeLabel:function(p){ return minsAgo(p.t, slot.length)+' · sample '+(p.t+1)+' of '+slot.length; },
      xfmt:function(v){ return minsAgo(v, slot.length); },
      series:[{name:'Slot time',color:cssVar('--s1'),points:slot}]});
  });

  var tops=(val.top_validators||[]).slice(0,10);
  var c3=card(host,'Top validators by stake','Active stake per vote account. Identifiers are truncated; full keys in the table.',{
    table:function(){ return makeTable(['Vote account','Stake (SOL)','Share','Commission'],
      (val.top_validators||[]).map(function(v){ return [v.vote_pubkey, num(v.stake_sol), pct(v.stake_pct,3), v.commission+'%']; })); }});
  register(c3.chart,function(){
    drawBars(c3.chart,{horizontal:true, color:cssVar('--s1'), valueName:'Stake (SOL)',
      fmt:function(v){ return compact(v)+' SOL'; }, aria:'Top validators by stake',
      items:tops.map(function(v){ return {label:v.vote_pubkey.slice(0,6)+'…'+v.vote_pubkey.slice(-4),
        tipLabel:v.vote_pubkey, value:v.stake_sol, sub:pct(v.stake_pct,3)+' of stake · '+v.commission+'% commission'}; })});
  });

  var dist=dig(D,'validators.commission.distribution')||[];
  var c4=card(host,'Validator commission distribution','How many validators charge what. Buckets are ordered, so this is one colour.',{
    table:function(){ return makeTable(['Commission','Validators'], dist.map(function(d){ return [d.bucket, num(d.count)]; })); }});
  register(c4.chart,function(){
    drawBars(c4.chart,{items:dist.map(function(d){ return {label:d.bucket, value:d.count}; }),
      fmt:function(v){ return num(v)+' validators'; }, yfmt:function(v){ return num(v); },
      valueName:'Validators', color:cssVar('--s1'), aria:'Validator commission distribution'});
  });

  /* RPC + supply detail card */
  var cd=el('div','card');
  var hh=el('header'); var bx=el('div'); bx.appendChild(el('h3',null,'Network detail'));
  hh.appendChild(bx); cd.appendChild(hh);
  cd.appendChild(el('p','cap','Straight from JSON-RPC on the endpoint that answered first.'));
  var rows=[
    ['Epoch', num(epoch.epoch)+'  ('+pct(epoch.progress_pct,1)+' complete)'],
    ['Absolute slot', num(dig(D,'network.absolute_slot'))],
    ['Block height', num(dig(D,'network.block_height'))],
    ['Agave version', String(dig(D,'network.version.solana_core')||'n/a')],
    ['Feature set', num(dig(D,'network.version.feature_set'))],
    ['Inflation (annualised)', pct(dig(D,'network.inflation.total_pct'),3)],
    ['Total stake', num(val.total_stake_sol)+' SOL'],
    ['Circulating supply', dig(D,'supply.available') ? num(dig(D,'supply.circulating_sol'))+' SOL' : 'unavailable this run'],
    ['Base fee', num(fees.base_fee_lamports)+' lamports'],
    ['Median priority fee', num(fees.priority_fee_micro_lamports_median,2)+' µlamports/CU'],
    ['Slots carrying a priority fee', pct(fees.slots_with_priority_fee_pct,1)]
  ];
  if(activity.available){
    rows.push(['Unique fee payers per block (sampled)', num(activity.unique_fee_payers_per_block_avg,1)]);
    rows.push(['Blocks sampled', num(activity.blocks_sampled)]);
  }
  cd.appendChild(makeTable(['Metric','Value'], rows));
  var health=dig(D,'network.rpc_health')||{};
  if(Object.keys(health).length){
    cd.appendChild(el('p','cap','Public RPC endpoints probed this run:'));
    var srow=el('div','srcs');
    Object.keys(health).forEach(function(h){
      var d=el('div','src'); var pip=el('span','pip');
      pip.style.background = health[h].healthy ? cssVar('--good') : cssVar('--critical');
      d.appendChild(pip); d.appendChild(el('span',null,h+' · '+health[h].latency_ms+' ms'));
      srow.appendChild(d);
    });
    cd.appendChild(srow);
  }
  document.getElementById('net').appendChild(cd);
})();

/* ------------------------------------------------------------- ECOSYSTEM */
(function(){
  var host=document.getElementById('eco');
  var top=(protos.top||[]).slice(0,10);
  var c1=card(host,'Top protocols by TVL','Value locked per protocol on Solana. Nominal categories, so a single colour.',{
    table:function(){ return makeTable(['Protocol','Category','TVL','1d','7d'],
      (protos.top||[]).map(function(p){ return [p.name, p.category, usd(p.tvl_usd),
        signedPct(p.change_1d_pct,1), signedPct(p.change_7d_pct,1)]; })); }});
  register(c1.chart,function(){
    drawBars(c1.chart,{horizontal:true,color:cssVar('--s1'),valueName:'TVL',fmt:usd,aria:'Top Solana protocols by TVL',
      items:top.map(function(p){ return {label:p.name, value:p.tvl_usd,
        sub:p.category+' · 24h '+signedPct(p.change_1d_pct,1)}; })});
  });

  var cats=(protos.categories||[]).slice(0,8);
  var c2=card(host,'TVL by category','Where the locked value sits. Shares are of tracked Solana TVL.',{
    table:function(){ return makeTable(['Category','TVL','Share'],
      cats.map(function(c){ return [c.category, usd(c.tvl_usd), pct(c.share_pct)]; })); }});
  register(c2.chart,function(){
    drawBars(c2.chart,{horizontal:true,color:cssVar('--s1'),valueName:'TVL',fmt:usd,aria:'Solana TVL by category',
      items:cats.map(function(c){ return {label:c.category, value:c.tvl_usd, sub:pct(c.share_pct)+' of tracked TVL'}; })});
  });

  var pegs=(stables.breakdown||[]);
  if(pegs.length){
    var c3=card(host,'Stablecoins by peg','Circulating value on Solana, split by what each token tracks.',{
      table:function(){ return makeTable(['Peg','Supply'], pegs.map(function(p){ return [p.peg, usd(p.supply_usd)]; })); }});
    register(c3.chart,function(){
      drawBars(c3.chart,{horizontal:true,color:cssVar('--s1'),valueName:'Supply',fmt:usd,aria:'Stablecoins by peg',
        items:pegs.map(function(p){ return {label:p.peg, value:p.supply_usd}; })});
    });
  }

  var ta=dig(D,'defi.protocols.tokenized_assets')||{};
  if((ta.protocols||[]).length){
    var c4=card(host,'Tokenised assets & equities','Real-world-asset protocols on Solana, by locked value.',{
      table:function(){ return makeTable(['Protocol','Category','TVL'],
        (ta.protocols||[]).map(function(p){ return [p.name, p.category, usd(p.tvl_usd)]; })); }});
    register(c4.chart,function(){
      drawBars(c4.chart,{horizontal:true,color:cssVar('--s1'),valueName:'TVL',fmt:usd,aria:'Tokenised asset protocols',
        items:(ta.protocols||[]).map(function(p){ return {label:p.name, value:p.tvl_usd, sub:p.category}; })});
    });
    var note=el('div','card');
    note.appendChild(el('h3',null,'What this number is'));
    note.appendChild(el('p','cap', ta.note||''));
    if(activity.available){
      note.appendChild(el('h3',null,'Address activity'));
      note.appendChild(el('p','cap', activity.note||''));
      note.appendChild(makeTable(['Slot','Transactions','Unique fee payers'],
        (activity.samples||[]).map(function(s){ return [num(s.slot), num(s.transactions), num(s.unique_fee_payers)]; })));
    }
    host.appendChild(note);
  }

  var d=D.deltas||{};
  if(d.available && d.windows){
    Object.keys(d.windows).forEach(function(k){
      var w=d.windows[k];
      var cd=el('div','card');
      cd.appendChild(el('h3',null,'Change over '+k));
      cd.appendChild(el('p','cap','Against this project’s own archived run at '+w.reference_time+'.'));
      cd.appendChild(makeTable(['Metric','Then','Now','Change'],
        Object.keys(w.metrics).map(function(m){ var x=w.metrics[m];
          return [x.label, num(x.previous,2), num(x.current,2), signedPct(x.change_pct)]; })));
      host.appendChild(cd);
    });
  }
})();

/* ------------------------------------------------------------------ NEWS */
(function(){
  var host=document.getElementById('news');
  function listCard(title, cap, items, render){
    if(!items || !items.length) return;
    var c=el('div','card');
    c.appendChild(el('h3',null,title));
    c.appendChild(el('p','cap',cap));
    var box=el('div','news');
    items.forEach(function(it){ box.appendChild(render(it)); });
    c.appendChild(box); host.appendChild(c);
  }
  listCard('Solana Foundation news','From solana.com/news/rss.xml.', (dig(D,'news.solana_foundation.items')||[]).slice(0,5),
    function(it){ var d=el('div'); var a=el('a',null,it.title); a.href=it.url; a.rel='noopener'; a.target='_blank';
      d.appendChild(a); d.appendChild(el('div','when', it.published||''));
      if(it.summary) d.appendChild(el('p',null,it.summary)); return d; });

  listCard('Validator client releases','GitHub releases for anza-xyz/agave — what validators are being asked to run.',
    (dig(D,'news.releases.releases')||[]).slice(0,5),
    function(r){ var d=el('div'); var a=el('a',null,r.tag+(r.prerelease?'  (pre-release)':'  (stable)'));
      a.href=r.url; a.rel='noopener'; a.target='_blank'; d.appendChild(a);
      d.appendChild(el('div','when',(r.published||'').slice(0,10))); return d; });

  listCard('Open SIMD proposals','Live from the solana-improvement-documents pull-request queue.',
    (dig(D,'news.simds.open_proposals')||[]).slice(0,8),
    function(s){ var d=el('div'); var a=el('a',null,(s.simd?s.simd+': ':'')+s.title);
      a.href=s.url; a.rel='noopener'; a.target='_blank'; d.appendChild(a);
      d.appendChild(el('div','when','updated '+(s.updated||'').slice(0,10))); return d; });

  var road=dig(D,'news.roadmap')||{};
  if((road.milestones||[]).length){
    var c=el('div','card');
    c.appendChild(el('h3',null,'Tracked upgrade milestones'));
    c.appendChild(el('p','cap','Curated list — no machine-readable feed publishes these. Last reviewed '
      +(road.last_reviewed||'unknown')+'.'));
    c.appendChild(makeTable(['Milestone','Status','What it changes'],
      road.milestones.map(function(m){ return [m.name, m.status, m.summary]; })));
    host.appendChild(c);
  }
})();

/* ---------------------------------------------------------------- FOOTER */
(function(){
  var f=document.getElementById('footmeta');
  var srcs=dig(D,'collection.sources')||{};
  f.textContent='Built by solana-ecosystem-pulse. Python standard library only — no installed packages, '
    +'no API keys, no runtime JavaScript dependencies. This run made '+(srcs.calls||0)+' HTTP calls ('
    +(srcs.ok||0)+' OK, '+(srcs.failed||0)+' failed).';
  var names={}; (srcs.detail||[]).forEach(function(e){
    var key=e.name.split('@')[0];
    if(!(key in names)) names[key]=true;
    if(!e.ok) names[key]=false;
  });
  var host=document.getElementById('srcs');
  Object.keys(names).sort().forEach(function(k){
    var d=el('div','src'); var pip=el('span','pip');
    pip.style.background = names[k] ? cssVar('--good') : cssVar('--warning');
    d.appendChild(pip); d.appendChild(el('span',null,k)); host.appendChild(d);
  });
})();

/* -------------------------------------------------------------- CONTROLS */
document.getElementById('themeBtn').addEventListener('click',function(){
  var next = document.documentElement.getAttribute('data-theme')==='dark' ? 'light':'dark';
  document.documentElement.setAttribute('data-theme',next);
  this.textContent = next==='dark' ? 'Light theme' : 'Dark theme';
  try{ localStorage.setItem('pulse-theme',next); }catch(e){}
  redrawAll();
});
try{ var saved=localStorage.getItem('pulse-theme');
  if(saved){ document.documentElement.setAttribute('data-theme',saved);
    document.getElementById('themeBtn').textContent = saved==='dark'?'Light theme':'Dark theme'; }
  else if(window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches){
    document.documentElement.setAttribute('data-theme','light');
    document.getElementById('themeBtn').textContent='Dark theme';
  }
}catch(e){}

document.getElementById('rangeBtns').addEventListener('click',function(ev){
  var b=ev.target.closest('button'); if(!b) return;
  RANGE_DAYS = parseInt(b.getAttribute('data-days'),10)||0;
  Array.prototype.forEach.call(this.querySelectorAll('button'),function(x){
    x.setAttribute('aria-pressed', x===b ? 'true':'false'); });
  redrawAll();
});

var rt; window.addEventListener('resize',function(){ clearTimeout(rt); rt=setTimeout(redrawAll,140); });
redrawAll();
})();
</script>
</body>
</html>
"""
