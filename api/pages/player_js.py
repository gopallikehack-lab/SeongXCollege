"""Player + assessment frontend JS (injected into MAIN_PAGE)."""

PLAYER_JS = r"""
(function(){
'use strict';

/* ===== inline svg icons ===== */
var ICON_PATHS = {
  arrowleft:'<line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/>',
  chevleft:'<polyline points="15 18 9 12 15 6"/>',
  chevright:'<polyline points="9 18 15 12 9 6"/>',
  x:'<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>',
  check:'<polyline points="20 6 9 17 4 12"/>',
  refresh:'<polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/>',
  play:'<polygon points="5 3 19 12 5 21 5 3"/>',
  pause:'<rect x="6" y="4" width="4" height="16" rx="1"/><rect x="14" y="4" width="4" height="16" rx="1"/>',
  replay:'<polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"/>',
  prev:'<polygon points="19 20 9 12 19 4 19 20"/><line x1="5" y1="19" x2="5" y2="5"/>',
  next:'<polygon points="5 4 15 12 5 20 5 4"/><line x1="19" y1="5" x2="19" y2="19"/>',
  vol:'<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/>',
  mute:'<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/>',
  gear:'<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/>',
  fs:'<path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/>',
  exitfs:'<path d="M8 3v3a2 2 0 0 1-2 2H3m18 0h-3a2 2 0 0 1-2-2V3m0 18v-3a2 2 0 0 1 2-2h3M3 16h3a2 2 0 0 1 2 2v3"/>',
  list:'<line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/>',
  dl:'<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>',
  link:'<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>',
  clock:'<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
  video:'<polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2"/>',
  file:'<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/>',
  clipboard:'<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/><path d="M9 12h6"/><path d="M9 16h6"/>',
  youtube:'<path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.42a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.42 8.6.42 8.6.42s6.88 0 8.6-.42a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"/><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"/>',
  package:'<path d="M16.5 9.4 7.5 4.21"/><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/>',
  embed:'<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>',
  help:'<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
  book:'<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>'
};
function icon(n,s){s=s||20;var p=ICON_PATHS[n]||ICON_PATHS.book;return '<svg xmlns="http://www.w3.org/2000/svg" width="'+s+'" height="'+s+'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'+p+'</svg>';}
function unitTypeIcon(t){t=(t||'').toLowerCase();if(t==='ivideo')return 'video';if(t==='pdf')return 'file';if(t==='assessmentv2'||t==='assessment')return 'clipboard';if(t==='youtube')return 'youtube';if(t==='scorm')return 'package';if(t==='embed')return 'embed';if(t==='url')return 'link';if(t==='quizformal'||t==='selfassessment')return 'help';return 'book';}

/* ===== themes ===== */
var THEMES = [
  {id:"default",name:"Midnight",accent:"#5c8dff",accent2:"#7c5cff"},
  {id:"dracula",name:"Dracula",accent:"#bd93f9",accent2:"#ff79c6"},
  {id:"rose",name:"Rose",accent:"#ff5c8d",accent2:"#c45cff"},
  {id:"green",name:"Forest",accent:"#2ecc71",accent2:"#13b6a3"},
  {id:"amber",name:"Amber",accent:"#f6b73c",accent2:"#ff8a4c"},
  {id:"crimson",name:"Crimson",accent:"#ff5c5c",accent2:"#b35cff"},
  {id:"cyber",name:"Cyber",accent:"#00d4ff",accent2:"#7c5cff"},
  {id:"mono",name:"Mono",accent:"#e6e9ee",accent2:"#9fb8ff"},
  {id:"sunset",name:"Sunset",accent:"#ff7c5c",accent2:"#ff5cbd"},
  {id:"nord",name:"Nord",accent:"#88c0d0",accent2:"#b48ead"},
  {id:"day",name:"Day",accent:"#3b6dff",accent2:"#7c5cff"}
];
var curTheme = localStorage.getItem("theme") || "default";
document.documentElement.setAttribute("data-theme", curTheme);
function renderThemePicker(){
  var grid=document.getElementById('theme-grid');if(!grid)return;
  var h='';
  for(var i=0;i<THEMES.length;i++){
    var t=THEMES[i];var isCur=t.id===curTheme;
    h+='<div class="theme-swatch'+(isCur?' cur':'')+'" data-tid="'+t.id+'"><span class="dot" style="background:linear-gradient(135deg,'+t.accent+','+t.accent2+')"></span><span>'+t.name+'</span></div>';
  }
  grid.innerHTML=h;
  grid.querySelectorAll('.theme-swatch').forEach(function(el){
    el.addEventListener('click',function(){
      curTheme=el.dataset.tid;
      document.documentElement.setAttribute("data-theme",curTheme);
      localStorage.setItem("theme",curTheme);
      renderThemePicker();closeThemePicker();
    });
  });
}
window.toggleThemePicker=function(){var p=document.getElementById('theme-picker');if(!p)return;p.classList.toggle('open');if(p.classList.contains('open'))renderThemePicker();};
function closeThemePicker(){var p=document.getElementById('theme-picker');if(p)p.classList.remove('open');}
document.addEventListener('click',function(e){var p=document.getElementById('theme-picker');if(!p||!p.classList.contains('open'))return;var b=document.querySelector('.icon-btn[title="Themes"]');if(p.contains(e.target)||(b&&b.contains(e.target)))return;p.classList.remove('open');});

/* ===== utils ===== */
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
function g(id){return document.getElementById(id);}
function hashCode(s){var h=0;for(var i=0;i<(s||'').length;i++){h=((h<<5)-h)+s.charCodeAt(i);h|=0;}return Math.abs(h);}
var PALETTES=[['#5c8dff','#7c5cff'],['#ff5c8d','#c45cff'],['#2ecc71','#13b6a3'],['#f6b73c','#ff8a4c'],['#ff5c5c','#b35cff'],['#00d4ff','#7c5cff'],['#ff7c5c','#ff5cbd'],['#9d5cff','#5c8dff']];
function pickGradient(l){return PALETTES[hashCode(l||'?')%PALETTES.length];}
function initials(l){var p=(l||'?').trim().split(/\s+/);if(p.length===1)return p[0].slice(0,2).toUpperCase();return (p[0].charAt(0)+p[1].charAt(0)).toUpperCase();}
function showPage(name){var pages=document.querySelectorAll('.page');for(var i=0;i<pages.length;i++)pages[i].classList.remove('active');var el=document.getElementById('page-'+name);if(el)el.classList.add('active');var items=document.querySelectorAll('.drawer-item[data-page]');for(var j=0;j<items.length;j++)items[j].classList.remove('active');var act=document.querySelector('.drawer-item[data-page="'+name+'"]');if(act)act.classList.add('active');}
window.goPage=function(name){showPage(name);closeDrawer();};
window.openDrawer=function(){g('drawer').classList.add('open');g('drawer-bg').classList.add('open');};
window.closeDrawer=function(){g('drawer').classList.remove('open');g('drawer-bg').classList.remove('open');};

/* ===== state ===== */
var BATCHES=[],ACTIVE=null,FLAT=[],CURRENT=null,CURRENT_INFO=null,HLS=null,VIDEO=null,CURRENT_VARIANTS={};
var UI_T=null,LP_T=null,TAP_T=null,seekReset=null,seekSide=null,seekAcc=0,ripT=null,lastTapT=0,lastTapSide=null;
var CUR_SPEED=1,VOL=1,MUTED=false,QSEL=-1,QPREF=0,MENU_VIEW=null,SCRUB=false,HOLDING=false;
var DT_STEP=10;
var SPEEDS=[0.5,0.75,1,1.25,1.5,2];

/* ===== batch list ===== */
function renderBatches(){
  var grid=g('batch-grid');if(!grid)return;
  var q=(g('batch-search').value||'').toLowerCase();
  grid.innerHTML='';
  var filtered=BATCHES.filter(function(b){return !q||(b.label||'').toLowerCase().indexOf(q)!==-1;});
  if(!filtered.length){grid.innerHTML='<div style="padding:24px;color:var(--muted);text-align:center;grid-column:1/-1">'+(BATCHES.length?'No batches match.':'No batches available.')+'</div>';return;}
  for(var i=0;i<filtered.length;i++){
    (function(b){
      var gr=pickGradient(b.label);
      var thumb,thumbStyle;
      if(b.image){thumb='<img src="'+esc(b.image)+'" alt="" loading="lazy">';thumbStyle='';}
      else{thumb='<div class="pattern"></div><div class="mono">'+esc(initials(b.label))+'</div>';thumbStyle=' style="background:linear-gradient(135deg,'+gr[0]+','+gr[1]+')"';}
      var card=document.createElement('div');card.className='batch-card';
      card.innerHTML='<div class="thumb"'+thumbStyle+'>'+thumb+'</div>'
        +'<div class="meta"><span class="t">'+esc(b.label)+'</span><span class="s">tap to open</span></div>'
        +'<button class="study-btn">▶ Study</button>';
      var go=function(){openBatch(b.titleId,b.label);};
      card.querySelector('.thumb').addEventListener('click',go);
      card.querySelector('.study-btn').addEventListener('click',go);
      grid.appendChild(card);
    })(filtered[i]);
  }
}

/* ===== viewer ===== */
window.openBatch=function(titleId,label){
  ACTIVE=titleId;
  g('viewer-title').textContent=label;
  g('sections-title').textContent=label;
  g('search').value='';
  g('toc').innerHTML='<div style="padding:20px;color:var(--muted)">loading sections…</div>';
  g('player-wrap').innerHTML='<div class="player-empty"><svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg><h2 class="brand-gradient">Pick a lecture</h2><p>Open the playlist with the list button.</p></div>';
  g('nowplaying').textContent='';
  destroyPlayer();
  showPage('viewer');
  fetch('/api/sections/'+encodeURIComponent(titleId)).then(function(r){return r.json();}).then(function(j){
    if(!j||!j.sections){g('toc').innerHTML='<div style="padding:20px;color:#ff7a7a">'+esc((j&&j.error)||'failed')+'</div>';return;}
    window._sections=j.sections;
    renderTOC();
    if(window.innerWidth>900)g('sections-overlay').classList.add('open');
  }).catch(function(e){g('toc').innerHTML='<div style="padding:20px;color:#ff7a7a">error: '+esc(e.message||e)+'</div>';});
};
window.closeBatch=function(){destroyPlayer();ACTIVE=null;g('sections-overlay').classList.remove('open');showPage('batches');};
window.toggleSections=function(){g('sections-overlay').classList.toggle('open');};

function renderTOC(){
  var toc=g('toc');if(!toc)return;
  toc.innerHTML='';FLAT=[];
  var q=(g('search').value||'').toLowerCase();
  var sections=window._sections||[];
  for(var si=0;si<sections.length;si++){
    var sec=sections[si];
    var units=sec.units.filter(function(u){return !q||((u.title||'').toLowerCase().indexOf(q)!==-1);});
    if(q&&units.length===0)continue;
    var open=(q!==''||si===0)?' open':'';
    var secDiv=document.createElement('div');secDiv.className='toc-sec';
    var head=document.createElement('div');head.className='toc-head'+open;
    head.innerHTML='<div class="toc-num">'+(si+1)+'</div>'
      +'<div class="toc-info"><div class="toc-title">'+esc(sec.title)+'</div>'
      +'<div class="toc-sub">'+units.length+' / '+sec.units.length+' units</div></div>'
      +'<div class="toc-arrow">'+icon('chevright',18)+'</div>';
    var body=document.createElement('div');body.className='toc-body'+open;
    head.onclick=(function(h,b){return function(){h.classList.toggle('open');b.classList.toggle('open');};})(head,body);
    for(var ui=0;ui<units.length;ui++){
      var u=units[ui];var idx=FLAT.length;
      FLAT.push({unit:u,sectionTitle:sec.title});
      var typeKey=(u.type||'').replace(/[^a-zA-Z0-9]/g,'')||'unit';
      var uDiv=document.createElement('div');uDiv.className='toc-unit';uDiv.dataset.idx=idx;
      uDiv.innerHTML='<div class="t">'+esc(u.title||u.id)+'</div><span class="type '+esc(typeKey)+'">'+icon(unitTypeIcon(u.type),13)+'<span>'+esc(u.type||'')+'</span></span>';
      (function(i){uDiv.onclick=function(){playUnit(i);};})(idx);
      body.appendChild(uDiv);
    }
    secDiv.appendChild(head);secDiv.appendChild(body);toc.appendChild(secDiv);
  }
}

/* ===== unit playback ===== */
function playUnit(idx){
  if(idx<0||idx>=FLAT.length)return;
  CURRENT=idx;var item=FLAT[idx];var u=item.unit;
  var units=document.querySelectorAll('.toc-unit.active');
  for(var i=0;i<units.length;i++)units[i].classList.remove('active');
  var el=document.querySelector('.toc-unit[data-idx="'+idx+'"]');
  if(el){el.classList.add('active');el.scrollIntoView({block:'nearest',behavior:'smooth'});}
  g('nowplaying').textContent=u.title||'';
  setStatus('loading…');
  destroyPlayer();
  fetch('/api/video/'+encodeURIComponent(ACTIVE)+'/'+encodeURIComponent(u.id)).then(function(r){return r.json();}).then(function(j){
    CURRENT_INFO=j;
    if(j.error){g('player-wrap').innerHTML='<div class="player-empty"><p>error: '+esc(j.error)+'</p></div>';setStatus('error','status err');return;}
    if(j.type==='wistia'&&j.sourceid){playWistia(j.sourceid);}
    else if(j.type==='pdf'){playPdf(ACTIVE,u.id);}
    else if(j.type==='assessment'){playAssessment(ACTIVE,u.id,false);}
    else{g('player-wrap').innerHTML='<div class="player-empty"><p>unsupported: '+esc(j.type||'?')+'</p></div>';}
    if(window.innerWidth<=900)g('sections-overlay').classList.remove('open');
  }).catch(function(e){g('player-wrap').innerHTML='<div class="player-empty"><p>error: '+esc(e.message||e)+'</p></div>';});
}
function destroyPlayer(){
  clearTimeout(UI_T);clearTimeout(LP_T);clearTimeout(TAP_T);clearTimeout(seekReset);clearTimeout(ripT);
  seekSide=null;seekAcc=0;MENU_VIEW=null;SCRUB=false;HOLDING=false;
  if(HLS){try{HLS.destroy();}catch(e){}HLS=null;}
  if(VIDEO){try{VIDEO.pause();}catch(e){}VIDEO=null;}
  if(window._asTimer){clearInterval(window._asTimer);window._asTimer=null;}
}

/* ===== player ===== */
function setStatus(t,c){var s=g('status');if(!s)return;s.textContent=t;s.className=c||'status';}
function on(id,fn){var el=g(id);if(el)el.addEventListener('click',fn);}

function buildPlayerUI(){
  var title=(CURRENT!=null&&FLAT[CURRENT])?(FLAT[CURRENT].unit.title||''):'';
  g('player-wrap').innerHTML=
  '<div class="yt show" id="yt">'+
    '<video id="v" playsinline webkit-playsinline preload="metadata"></video>'+
    '<div class="yt-gl" id="yt-gl"></div>'+
    '<div class="yt-logo brand-gradient">SeongEra</div>'+
    '<div class="yt-rip l" id="yt-rl"><div class="in">'+icon('replay',34)+'<span id="yt-rlt">10 seconds</span></div></div>'+
    '<div class="yt-rip r" id="yt-rr"><div class="in">'+icon('replay',34)+'<span id="yt-rrt">10 seconds</span></div></div>'+
    '<div class="yt-2x" id="yt-2x">▶▶ 2× speed</div>'+
    '<div class="yt-spin" id="yt-spin"></div>'+
    '<div class="yt-top" id="yt-top"><div class="yt-title" id="yt-title">'+esc(title)+'</div></div>'+
    '<div class="yt-center" id="yt-center">'+
      '<button class="yt-sb" id="yt-prev" title="Previous">'+icon('prev',30)+'</button>'+
      '<button class="yt-big" id="yt-big" title="Play / Pause">'+icon('play',44)+'</button>'+
      '<button class="yt-sb" id="yt-next" title="Next">'+icon('next',30)+'</button>'+
    '</div>'+
    '<div class="yt-bottom" id="yt-bottom">'+
      '<div class="yt-pb" id="yt-pb"><div class="yt-track"><div class="yt-buf" id="yt-buf"></div><div class="yt-fill" id="yt-fill"></div><div class="yt-knob" id="yt-knob"></div></div><div class="yt-tip" id="yt-tip">0:00</div></div>'+
      '<div class="yt-row">'+
        '<div class="yt-l">'+
          '<button class="yb yt-hide-sm" id="yt-pp" title="Play / Pause">'+icon('play',26)+'</button>'+
          '<span class="yt-volwrap"><button class="yb yt-hide-sm" id="yt-mute" title="Mute">'+icon('vol',26)+'</button><input class="yt-vol" id="yt-vol" type="range" min="0" max="1" step="0.05" value="1"></span>'+
          '<span class="yt-time" id="yt-time">0:00 / 0:00</span>'+
        '</div>'+
        '<div class="yt-r">'+
          '<button class="yb" id="yt-list" title="Playlist">'+icon('list',26)+'</button>'+
          '<button class="yb" id="yt-dl" title="Download">'+icon('dl',26)+'</button>'+
          '<button class="yb" id="yt-lk" title="m3u8 link">'+icon('link',26)+'</button>'+
          '<button class="yb" id="yt-set" title="Settings">'+icon('gear',26)+'</button>'+
          '<button class="yb" id="yt-fs" title="Fullscreen">'+icon(fsEl()?'exitfs':'fs',26)+'</button>'+
        '</div>'+
      '</div>'+
    '</div>'+
    '<div class="yt-menu" id="yt-menu"></div>'+
  '</div>';
  bindUI();syncNav();
}
function bindUI(){
  var y=g('yt');if(!y)return;
  y.addEventListener('mousemove',showUI);
  ['yt-top','yt-bottom','yt-center'].forEach(function(zid){var z=g(zid);if(z)z.addEventListener('pointerdown',function(e){e.stopPropagation();showUI();});});
  on('yt-big',function(e){e.stopPropagation();window.togglePlay();});
  on('yt-pp',function(e){e.stopPropagation();window.togglePlay();});
  on('yt-prev',function(e){e.stopPropagation();window.playPrev();});
  on('yt-next',function(e){e.stopPropagation();window.playNext();});
  on('yt-mute',function(e){e.stopPropagation();window.toggleMute();});
  on('yt-list',function(e){e.stopPropagation();window.toggleSections();});
  on('yt-dl',function(e){e.stopPropagation();window.openDownload();});
  on('yt-lk',function(e){e.stopPropagation();window.openLink();});
  on('yt-set',function(e){e.stopPropagation();if(MENU_VIEW)closeMenu();else openMenu('main');});
  on('yt-fs',function(e){e.stopPropagation();window.toggleFS();});
  var vv=g('yt-vol');if(vv)vv.addEventListener('input',function(e){e.stopPropagation();if(!VIDEO)return;var v=parseFloat(this.value);VIDEO.volume=v;VIDEO.muted=(v===0);});
  var mm=g('yt-menu');if(mm)mm.addEventListener('click',function(e){
    e.stopPropagation();
    var t=e.target;
    while(t&&t!==this&&!(t.dataset&&(t.dataset.go||t.dataset.q!==undefined||t.dataset.s!==undefined)))t=t.parentNode;
    if(!t||t===this)return;
    if(t.dataset.go){MENU_VIEW=t.dataset.go;renderMenu();return;}
    if(t.dataset.q!==undefined){setQuality(t.dataset.q);closeMenu();return;}
    if(t.dataset.s!==undefined){window.setSpeed(t.dataset.s);closeMenu();}
  });
  bindProgress();bindGestures();
}
function bindVideo(){
  var v=VIDEO;
  v.addEventListener('timeupdate',updateTime);
  v.addEventListener('progress',updateTime);
  v.addEventListener('durationchange',updateTime);
  v.addEventListener('loadedmetadata',function(){if(!HOLDING)v.playbackRate=CUR_SPEED;updateTime();});
  v.addEventListener('play',function(){syncPlay();showUI();});
  v.addEventListener('pause',function(){
  if(!VIDEO)return;
  syncPlay(); showUI(); setStatus('paused');
  // after 5s of pause, hide the UI (until user moves mouse / taps)
  clearTimeout(UI_T);
  UI_T=setTimeout(hideUI, 5000);
});
  v.addEventListener('playing',function(){if(!VIDEO)return;setBuf(false);syncPlay();setStatus(playingLabel(),'status ok');showUI();});
  v.addEventListener('waiting',function(){if(!VIDEO)return;setBuf(true);setStatus('buffering…');});
  v.addEventListener('canplay',function(){setBuf(false);});
  v.addEventListener('seeked',function(){setBuf(false);});
  v.addEventListener('ended',function(){syncPlay();showUI();});
  v.addEventListener('volumechange',syncVol);
  v.addEventListener('error',function(){if(!VIDEO)return;setBuf(false);setStatus('video error','status err');});
function playingLabel(){if(HLS&&HLS.levels&&HLS.currentLevel>=0&&HLS.levels[HLS.currentLevel]&&HLS.levels[HLS.currentLevel].height)return 'playing · '+HLS.levels[HLS.currentLevel].height+'p';return 'playing';}
function setBuf(on){var y=g('yt'),s=g('yt-spin');if(!y||!s)return;y.classList.toggle('buf',on);s.classList.toggle('on',on);}
function syncPlay(){if(!VIDEO||!g('yt-big'))return;var playing=!VIDEO.paused&&!VIDEO.ended;var nm=VIDEO.ended?'replay':(playing?'pause':'play');g('yt-big').innerHTML=icon(nm,44);g('yt-pp').innerHTML=icon(nm,26);var y=g('yt');if(y)y.classList.toggle('yt-paused',!playing);}
function syncNav(){var p=g('yt-prev'),n=g('yt-next');if(!p||!n)return;p.disabled=!(CURRENT!=null&&CURRENT>0);n.disabled=!(CURRENT!=null&&CURRENT<FLAT.length-1);}
function syncVol(){if(!VIDEO||!g('yt-mute'))return;MUTED=VIDEO.muted;if(!VIDEO.muted&&VIDEO.volume>0)VOL=VIDEO.volume;var eff=VIDEO.muted?0:VIDEO.volume;g('yt-mute').innerHTML=icon(eff===0?'mute':'vol',26);var s=g('yt-vol');if(!s)return;s.value=eff;var p=Math.round(eff*100);s.style.background='linear-gradient(90deg,#fff '+p+'%,rgba(255,255,255,.3) '+p+'%)';}
function showUI(){
  var y=g('yt');if(!y)return;
  y.classList.add('show');
  clearTimeout(UI_T);
  // hide after 3.2s if playing, or after 5s if paused
  if(VIDEO&&!SCRUB&&!MENU_VIEW&&!HOLDING){
    UI_T=setTimeout(hideUI, VIDEO.paused ? 5000 : 3200);
  }
}
function hideUI(){
  var y=g('yt');if(!y)return;
  if(SCRUB||MENU_VIEW)return;   // don't hide while scrubbing or menu is open
  y.classList.remove('show');
}
function dur(){var d=VIDEO&&VIDEO.duration;return (d&&isFinite(d))?d:0;}
function setProg(pct){var f=g('yt-fill'),k=g('yt-knob');if(!f)return;f.style.width=pct+'%';k.style.left=pct+'%';}
function updateTime(){
  if(!VIDEO||!g('yt-time'))return;
  var cur=VIDEO.currentTime||0,d=dur();
  if(!SCRUB){g('yt-time').textContent=fmt(cur)+' / '+fmt(d);setProg(d?Math.min(100,cur/d*100):0);}
  var b=VIDEO.buffered;
  if(d&&b&&b.length){var end=b.end(b.length-1);for(var i=0;i<b.length;i++){if(b.start(i)<=cur+0.5&&b.end(i)>=cur){end=b.end(i);break;}}g('yt-buf').style.width=Math.min(100,end/d*100)+'%';}
}
function fmt(s){s=Math.floor(s||0);if(!isFinite(s))s=0;var h=Math.floor(s/3600),m=Math.floor((s%3600)/60),r=s%60;if(h)return h+':'+(m<10?'0':'')+m+':'+(r<10?'0':'')+r;return m+':'+(r<10?'0':'')+r;}
function bindProgress(){
  var pb=g('yt-pb'),tip=g('yt-tip');if(!pb||!tip)return;
  function pos(e){var r=pb.getBoundingClientRect();return Math.max(0,Math.min(1,(e.clientX-r.left)/r.width));}
  function showTip(p){var w=pb.getBoundingClientRect().width;var x=Math.max(26,Math.min(w-26,p*w));tip.style.left=x+'px';tip.textContent=fmt(p*dur());tip.style.opacity='1';}
  function scrub(e){var p=pos(e),d=dur();setProg(p*100);g('yt-time').textContent=fmt(p*d)+' / '+fmt(d);showTip(p);}
  pb.addEventListener('pointerdown',function(e){if(!VIDEO||!dur())return;e.stopPropagation();SCRUB=true;pb.classList.add('drag');try{pb.setPointerCapture(e.pointerId);}catch(x){}scrub(e);showUI();});
  pb.addEventListener('pointermove',function(e){if(!dur())return;if(SCRUB)scrub(e);else showTip(pos(e));});
  function finish(e,apply){if(!SCRUB)return;SCRUB=false;pb.classList.remove('drag');tip.style.opacity='0';if(apply&&VIDEO&&dur()){VIDEO.currentTime=pos(e)*dur();}updateTime();showUI();}
  pb.addEventListener('pointerup',function(e){finish(e,true);});
  pb.addEventListener('pointercancel',function(e){finish(e,false);});
  pb.addEventListener('pointerleave',function(){if(!SCRUB)tip.style.opacity='0';});
}
function qualityLabel(){if(!HLS||!HLS.levels||!HLS.levels.length)return 'Auto';if(QSEL===-1){var l=HLS.levels[HLS.currentLevel];return 'Auto'+(l&&l.height?' ('+l.height+'p)':'');}var l2=HLS.levels[QSEL];return l2&&l2.height?l2.height+'p':'L'+QSEL;}
function openMenu(v){MENU_VIEW=v;renderMenu();var m=g('yt-menu');if(m)m.classList.add('open');showUI();}
function closeMenu(){MENU_VIEW=null;var m=g('yt-menu');if(m)m.classList.remove('open');showUI();}
function renderMenu(){
  var m=g('yt-menu');if(!m)return;var h='';
  if(MENU_VIEW==='main'){
    h+='<div class="mi" data-go="quality"><span>Quality</span><span class="v">'+esc(qualityLabel())+' ›</span></div>';
    h+='<div class="mi" data-go="speed"><span>Speed</span><span class="v">'+(CUR_SPEED===1?'Normal':CUR_SPEED+'×')+' ›</span></div>';
  }else if(MENU_VIEW==='quality'){
    h+='<div class="mh" data-go="main">‹ Quality</div>';
    var lv=[];if(HLS&&HLS.levels){for(var i=0;i<HLS.levels.length;i++){lv.push({i:i,h:HLS.levels[i].height||0});}}
    lv.sort(function(a,b){return b.h-a.h;});
    for(var j=0;j<lv.length;j++){h+='<div class="mi'+(QSEL===lv[j].i?' sel':'')+'" data-q="'+lv[j].i+'"><span>'+(QSEL===lv[j].i?'✓ ':'')+(lv[j].h?lv[j].h+'p':'L'+lv[j].i)+'</span></div>';}
    h+='<div class="mi'+(QSEL===-1?' sel':'')+'" data-q="auto"><span>'+(QSEL===-1?'✓ ':'')+'Auto</span></div>';
  }else if(MENU_VIEW==='speed'){
    h+='<div class="mh" data-go="main">‹ Speed</div>';
    for(var k=0;k<SPEEDS.length;k++){var sp=SPEEDS[k];h+='<div class="mi'+(CUR_SPEED===sp?' sel':'')+'" data-s="'+sp+'"><span>'+(CUR_SPEED===sp?'✓ ':'')+(sp===1?'Normal':sp+'×')+'</span></div>';}
  }
  m.innerHTML=h;
}
function setQuality(v){if(v==='auto'){QSEL=-1;QPREF=0;}else{QSEL=parseInt(v,10);var l=HLS&&HLS.levels&&HLS.levels[QSEL];QPREF=l?(l.height||0):0;}if(HLS)HLS.currentLevel=QSEL;}
window.setSpeed=function(v){CUR_SPEED=parseFloat(v)||1;if(VIDEO&&!HOLDING)VIDEO.playbackRate=CUR_SPEED;};

function bindGestures(){
  var gl=g('yt-gl');if(!gl)return;
  var down=false,holding=false,moved=false,sx=0,sy=0,isTouch=false;
  function sideOf(e){var r=gl.getBoundingClientRect();var x=(e.clientX-r.left)/r.width;return x<0.35?'l':(x>0.65?'r':'c');}
  gl.addEventListener('contextmenu',function(e){e.preventDefault();});
  gl.addEventListener('pointerdown',function(e){if(e.pointerType==='mouse'&&e.button!==0)return;isTouch=(e.pointerType==='touch'||e.pointerType==='pen');down=true;holding=false;moved=false;sx=e.clientX;sy=e.clientY;clearTimeout(LP_T);if(isTouch){LP_T=setTimeout(function(){if(!down||moved||!VIDEO||VIDEO.paused||MENU_VIEW)return;holding=true;startHold();},450);}});
  gl.addEventListener('pointermove',function(e){if(e.pointerType==='mouse')showUI();if(down&&!holding&&(Math.abs(e.clientX-sx)>12||Math.abs(e.clientY-sy)>12)){moved=true;clearTimeout(LP_T);}});
  function end(e,cancel){if(!down)return;down=false;clearTimeout(LP_T);if(holding){holding=false;stopHold();return;}if(cancel||moved)return;onTap(sideOf(e),isTouch);}
  gl.addEventListener('pointerup',function(e){end(e,false);});
  gl.addEventListener('pointercancel',function(e){end(e,true);});
  gl.addEventListener('pointerleave',function(e){if(down&&holding)end(e,true);});
}
function startHold(){if(!VIDEO)return;HOLDING=true;VIDEO.playbackRate=2;var b=g('yt-2x');if(b)b.classList.add('on');var y=g('yt');if(y)y.classList.remove('show');clearTimeout(UI_T);try{if(navigator.vibrate)navigator.vibrate(15);}catch(e){}}
function stopHold(){HOLDING=false;if(VIDEO)VIDEO.playbackRate=CUR_SPEED;var b=g('yt-2x');if(b)b.classList.remove('on');}
function onTap(side,isTouch){
  if(MENU_VIEW){closeMenu();return;}
  var now=Date.now();
  if(seekSide&&side===seekSide&&side!=='c'){doSeek(side);return;}
  if(now-lastTapT<280&&lastTapSide===side){clearTimeout(TAP_T);lastTapT=0;if(side==='c'){if(isTouch){showUI();}else{window.toggleFS();}}else{doSeek(side);}return;}
  lastTapT=now;lastTapSide=side;clearTimeout(TAP_T);
  TAP_T=setTimeout(function(){singleTap(isTouch);},280);
}
function singleTap(isTouch){if(isTouch){var y=g('yt');if(!y)return;if(!y.classList.contains('show')){showUI();}else{clearTimeout(UI_T);if(VIDEO&&!VIDEO.paused)UI_T=setTimeout(hideUI,3200);}return;}window.togglePlay();showUI();}
function doSeek(side){
  if(!VIDEO||!dur())return;
  var dir=side==='l'?-1:1;
  if(seekSide!==side)seekAcc=0;
  seekSide=side;seekAcc+=DT_STEP;
  VIDEO.currentTime=Math.max(0,Math.min(dur(),(VIDEO.currentTime||0)+dir*DT_STEP));
  showRipple(side,seekAcc);
  clearTimeout(seekReset);
  seekReset=setTimeout(function(){seekSide=null;seekAcc=0;},700);
  updateTime();
}
function showRipple(side,acc){
  var l=g('yt-rl'),r=g('yt-rr');if(!l||!r)return;
  var el=side==='l'?l:r,other=side==='l'?r:l;
  other.classList.remove('on');
  g(side==='l'?'yt-rlt':'yt-rrt').textContent=acc+' seconds';
  el.classList.add('on');
  clearTimeout(ripT);
  ripT=setTimeout(function(){el.classList.remove('on');},650);
}

/* ===== wistia ===== */
function playWistia(sourceid){
  var master='https://fast.wistia.com/embed/medias/'+sourceid+'.m3u8';
  buildPlayerUI();
  VIDEO=g('v');
  VIDEO.volume=VOL;VIDEO.muted=MUTED;VIDEO.playbackRate=CUR_SPEED;QSEL=-1;
  bindVideo();syncVol();syncPlay();setBuf(true);
  fetch('/api/variants/'+encodeURIComponent(sourceid)).then(function(r){return r.json();}).then(function(j){CURRENT_VARIANTS=(j&&j.variants)||{};}).catch(function(){CURRENT_VARIANTS={};});
  if(window.Hls&&Hls.isSupported()){
    HLS=new Hls({capLevelToPlayerSize:false,startLevel:-1,autoStartLoad:true,maxBufferLength:60});
    HLS.loadSource(master);HLS.attachMedia(VIDEO);
    HLS.on(Hls.Events.MANIFEST_PARSED,function(e,data){if(QPREF){for(var i=0;i<data.levels.length;i++){if(data.levels[i].height===QPREF){QSEL=i;HLS.currentLevel=i;break;}}}if(MENU_VIEW)renderMenu();VIDEO.play().catch(function(){});});
    HLS.on(Hls.Events.LEVEL_SWITCHED,function(e,data){var lvl=HLS.levels[data.level];if(lvl)setStatus('playing · '+(lvl.height||'?')+'p','status ok');if(MENU_VIEW)renderMenu();});
    HLS.on(Hls.Events.ERROR,function(e,d){if(!d||!d.fatal)return;if(d.type===Hls.ErrorTypes.NETWORK_ERROR){setStatus('network error · retrying','status err');try{HLS.startLoad();}catch(x){}}else if(d.type===Hls.ErrorTypes.MEDIA_ERROR){try{HLS.recoverMediaError();}catch(x){}}else{setBuf(false);setStatus('playback error','status err');}});
  }else if(VIDEO.canPlayType('application/vnd.apple.mpegurl')){VIDEO.src=master;VIDEO.play().catch(function(){});}
  setStatus('playing','status ok');
  attachAutoNext();
}
function attachAutoNext(){
  if(!VIDEO)return;
  VIDEO.addEventListener('ended',function(){if(CURRENT!=null&&CURRENT<FLAT.length-1){setStatus('auto-playing next…');playUnit(CURRENT+1);}});
}

/* ===== pdf ===== */
function playPdf(titleId,unitId){
  g('player-wrap').innerHTML='<div class="player-empty">loading PDF…</div>';
  fetch('/api/pdf/'+encodeURIComponent(titleId)+'/'+encodeURIComponent(unitId)).then(function(r){return r.json();}).then(function(info){
    if(info.error){g('player-wrap').innerHTML='<div class="player-empty"><p>PDF error: '+esc(info.error)+'</p></div>';return;}
    window._pdfInfo=info;
    g('player-wrap').innerHTML='<div class="pdf-viewer"><div class="pdf-toolbar"><span class="name">'+icon('file',20)+' '+esc(info.display||info.filename)+'</span><div class="pdf-actions"><a href="'+esc(info.redirectUrl)+'" download="'+esc(info.filename)+'" target="_blank" class="primary">'+icon('dl',16)+' download</a><button onclick="pdfCopyUrl(this)">'+icon('link',16)+' copy</button><button onclick="pdfNewTab()">↗ new tab</button></div></div><iframe class="pdf-frame" src="'+esc(info.redirectUrl)+'"></iframe></div>';
    setStatus('pdf','status ok');
  });
}
window.pdfNewTab=function(){if(window._pdfInfo&&window._pdfInfo.redirectUrl)window.open(window._pdfInfo.redirectUrl,'_blank');};
window.pdfCopyUrl=function(btn){var item=FLAT[CURRENT];fetch('/api/pdf/'+encodeURIComponent(ACTIVE)+'/'+encodeURIComponent(item.unit.id)).then(function(r){return r.json();}).then(function(info){if(info.redirectUrl){navigator.clipboard.writeText(info.redirectUrl);var o=btn.textContent;btn.textContent='✓';setTimeout(function(){btn.textContent=o;},1200);}});};

/* ===== controls ===== */
window.togglePlay=function(){if(!VIDEO)return;if(VIDEO.paused||VIDEO.ended){var p=VIDEO.play();if(p&&p.catch)p.catch(function(){});}else VIDEO.pause();};
window.toggleMute=function(){if(VIDEO){VIDEO.muted=!VIDEO.muted;if(!VIDEO.muted&&VIDEO.volume===0)VIDEO.volume=VOL||1;}};
window.playNext=function(){if(CURRENT!=null&&CURRENT<FLAT.length-1)playUnit(CURRENT+1);};
window.playPrev=function(){if(CURRENT!=null&&CURRENT>0)playUnit(CURRENT-1);};
function fsEl(){return document.fullscreenElement||document.webkitFullscreenElement;}
function leaveFS(){if(fsEl()){if(document.exitFullscreen)document.exitFullscreen();else if(document.webkitExitFullscreen)document.webkitExitFullscreen();}}
window.toggleFS=function(){
  var w=g('player-wrap');
  if(!fsEl()){
    var p=null;
    if(w.requestFullscreen)p=w.requestFullscreen();
    else if(w.webkitRequestFullscreen)p=w.webkitRequestFullscreen();
    else if(w.msRequestFullscreen)p=w.msRequestFullscreen();
    else if(VIDEO&&VIDEO.webkitEnterFullscreen){VIDEO.webkitEnterFullscreen();return;}
    if(p&&p.then)p.then(function(){try{if(window.innerWidth<=900&&screen.orientation&&screen.orientation.lock)screen.orientation.lock('landscape').catch(function(){});}catch(e){}}).catch(function(){});
  }else leaveFS();
};
function onFsChange(){var b=g('yt-fs');if(b)b.innerHTML=icon(fsEl()?'exitfs':'fs',26);if(!fsEl()){try{if(screen.orientation&&screen.orientation.unlock)screen.orientation.unlock();}catch(e){}}}
document.addEventListener('fullscreenchange',onFsChange);
document.addEventListener('webkitfullscreenchange',onFsChange);

/* ===== download / link modals ===== */
window.openDownload=function(){
  if(!CURRENT_INFO)return;
  if(CURRENT_INFO.type==='pdf'){var a=document.querySelector('.pdf-actions a.primary');if(a)a.click();return;}
  if(CURRENT_INFO.type==='assessment'){alert('assessment has no download');return;}
  var box=g('dl-variants');box.innerHTML='';
  var items=Object.entries(CURRENT_VARIANTS).sort(function(a,b){return parseInt(b[0])-parseInt(a[0]);});
  if(!items.length){box.innerHTML='<p style="color:var(--muted)">no variants</p>';g('modal-dl').classList.add('open');return;}
  for(var i=0;i<items.length;i++){var q=items[i][0],url=items[i][1];var el=document.createElement('div');el.className='variant';el.innerHTML='<div style="display:flex;justify-content:space-between;align-items:center;gap:10px"><span class="name">'+esc(q)+'</span><button data-url="'+esc(url)+'" data-q="'+esc(q)+'" class="dlbtn">download</button></div>';box.appendChild(el);}
  var btns=box.querySelectorAll('.dlbtn');for(var j=0;j<btns.length;j++){(function(b){b.onclick=function(){browserHlsDownload(b.dataset.url,(CURRENT_INFO.title||'video'),b.dataset.q);};})(btns[j]);}
  g('modal-dl').classList.add('open');
};
function browserHlsDownload(masterUrl,title,quality){
  closeModal('modal-dl');
  var status=g('status');status.textContent='download starting…';
  fetch(masterUrl).then(function(r){return r.text();}).then(function(m){
    var lines=m.split(/\r?\n/);var base=masterUrl.substring(0,masterUrl.lastIndexOf('/')+1);var segs=[];
    for(var i=0;i<lines.length;i++){var t=lines[i].trim();if(!t||t.charAt(0)==='#')continue;var abs=t;if(t.indexOf('http')!==0){if(t.charAt(0)==='/')abs=(new URL(masterUrl)).origin+t;else abs=base+t;}segs.push(abs);}
    if(!segs.length)throw new Error('no segments');
    var buffers=[];var done=0;var cursor=0;
    function worker(){var i=cursor++;if(i>=segs.length)return Promise.resolve();return fetch(segs[i]).then(function(r){return r.arrayBuffer();}).then(function(buf){buffers[i]=buf;}).catch(function(){buffers[i]=new Uint8Array(0);}).then(function(){done++;status.textContent='fetching '+done+'/'+segs.length;return worker();});}
    var workers=[];for(var w=0;w<6;w++)workers.push(worker());
    return Promise.all(workers).then(function(){
      status.textContent='assembling…';
      var total=0;for(var i=0;i<buffers.length;i++)total+=buffers[i].byteLength;
      var out=new Uint8Array(total);var off=0;
      for(var i=0;i<buffers.length;i++){out.set(new Uint8Array(buffers[i]),off);off+=buffers[i].byteLength;}
      var blob=new Blob([out],{type:'video/mp2t'});var url=URL.createObjectURL(blob);
      var a=document.createElement('a');a.href=url;a.download=(title.replace(/[\\/:*?"<>|]/g,'_').slice(0,80))+'_'+quality+'.ts';
      document.body.appendChild(a);a.click();document.body.removeChild(a);
      setTimeout(function(){URL.revokeObjectURL(url);},60000);
      status.textContent='✓ downloaded';status.className='status ok';
    });
  }).catch(function(e){status.textContent='error: '+e.message;status.className='status err';});
}
window.openLink=function(){
  if(!CURRENT_INFO||!CURRENT_INFO.sourceid){alert('no video loaded');return;}
  var master='https://fast.wistia.com/embed/medias/'+CURRENT_INFO.sourceid+'.m3u8';
  g('link-master').value=master;
  var box=g('link-variants');box.innerHTML='<p style="color:var(--muted);font-size:12px">loading…</p>';
  fetch('/api/variants/'+encodeURIComponent(CURRENT_INFO.sourceid)).then(function(r){return r.json();}).then(function(j){
    CURRENT_VARIANTS=(j&&j.variants)||{};
    var items=Object.entries(CURRENT_VARIANTS).sort(function(a,b){return parseInt(b[0])-parseInt(a[0]);});
    if(!items.length){box.innerHTML='<p style="color:var(--muted);font-size:12px">no variants</p>';}
    else{box.innerHTML='';for(var i=0;i<items.length;i++){var q=items[i][0],url=items[i][1];var el=document.createElement('div');el.className='variant';el.innerHTML='<div style="display:flex;justify-content:space-between;align-items:center;gap:10px;margin-bottom:8px"><span class="name">'+esc(q)+'</span><button data-url="'+esc(url)+'" class="copybtn">copy</button></div><input value="'+esc(url)+'" readonly onclick="this.select()" style="font:11px monospace">';box.appendChild(el);}
      var btns=box.querySelectorAll('.copybtn');for(var j=0;j<btns.length;j++){(function(b){b.onclick=function(){copyText(b.dataset.url,b);};})(btns[j]);}}
    g('modal-link').classList.add('open');
  });
};
function copyText(t,btn){navigator.clipboard.writeText(t).then(function(){var o=btn.textContent;btn.textContent='✓';setTimeout(function(){btn.textContent=o;},1200);}).catch(function(){var ta=document.createElement('textarea');ta.value=t;document.body.appendChild(ta);ta.select();document.execCommand('copy');document.body.removeChild(ta);var o=btn.textContent;btn.textContent='✓';setTimeout(function(){btn.textContent=o;},1200);});}
window.closeModal=function(id){g(id).classList.remove('open');};
window.copyField=function(id,btn){var el=g(id);el.select();el.setSelectionRange(0,99999);navigator.clipboard.writeText(el.value).then(function(){var o=btn.textContent;btn.textContent='copied!';setTimeout(function(){btn.textContent=o;},1200);});};
window.copyUpi=function(btn){var id=g('upi-id').textContent.trim();navigator.clipboard.writeText(id).then(function(){var o=btn.textContent;btn.textContent='✓ copied';setTimeout(function(){btn.textContent=o;},1200);});};
document.querySelectorAll('.modal').forEach(function(m){m.addEventListener('click',function(e){if(e.target===m)m.classList.remove('open');});});

document.addEventListener('keydown',function(e){
  if(e.target.tagName==='INPUT'||e.target.tagName==='SELECT'||e.target.tagName==='TEXTAREA')return;
  var k=e.key;
  if(k==='/'){e.preventDefault();if(g('page-viewer').classList.contains('active'))g('search').focus();else g('batch-search').focus();return;}
  if(!VIDEO)return;
  if(k===' '||k==='k'||k==='K'){e.preventDefault();togglePlay();showUI();}
  else if(k==='ArrowRight'||k==='l'||k==='L'){e.preventDefault();doSeek('r');showUI();}
  else if(k==='ArrowLeft'||k==='j'||k==='J'){e.preventDefault();doSeek('l');showUI();}
  else if(k==='ArrowUp'){e.preventDefault();VIDEO.muted=false;VIDEO.volume=Math.min(1,VIDEO.volume+0.05);showUI();}
  else if(k==='ArrowDown'){e.preventDefault();VIDEO.volume=Math.max(0,VIDEO.volume-0.05);showUI();}
  else if(k==='f'||k==='F')toggleFS();
  else if(k==='n'||k==='N')playNext();
  else if(k==='p'||k==='P')playPrev();
  else if(k==='m'||k==='M'){VIDEO.muted=!VIDEO.muted;showUI();}
  else if(k==='Escape'&&g('sections-overlay').classList.contains('open'))g('sections-overlay').classList.remove('open');
});

/* ===== assessment ===== */
var AS={state:null,titleId:null,unitId:null,submissionId:null,answers:{},order:[],blockMap:{},curIdx:0,total:0,submitted:false};
function asWidgetsHtml(desc){
  if(!desc)return '';
  var w=desc.widgets;if(!w&&Array.isArray(desc))w=desc;if(!w)return desc.html||desc.text||'';
  var out=[];
  for(var i=0;i<w.length;i++){var x=w[i];if(!x)continue;if(typeof x==='string'){out.push(x);continue;}var t=x.type||'',p=x.properties||{};if((t==='text'||t==='html')&&p.html)out.push(p.html);else if(t==='spacer')out.push('<div style="height:'+(p.height||12)+'px"></div>');else if(t==='image'){var u=p.url||p.src;if(u)out.push('<img src="'+esc(u)+'" style="max-width:100%;border-radius:8px">');}else if(p.html)out.push(p.html);}
  return out.join('');
}
function asBlockHtml(b){if(!b)return '';var bd=b.blockData||b.data||{};var h=asWidgetsHtml(bd.description);if(!h&&typeof bd.description==='string')h=bd.description;return h;}
function asOptHtml(o){if(!o)return '';var d=o.description||{};var h=asWidgetsHtml(d);if(!h&&typeof d==='string')h=d;return h||esc(o.id||'');}

function playAssessment(titleId,unitId,forceRetake){
  AS.state=null;AS.titleId=titleId;AS.unitId=unitId;AS.answers={};AS.order=[];AS.blockMap={};AS.curIdx=0;AS.total=0;AS.submitted=false;
  g('player-wrap').innerHTML='<div class="as-loading"><div class="sp"></div><div>loading assessment…</div></div>';
  setStatus('assessment');
  var url='/api/assessment/'+encodeURIComponent(titleId)+'/'+encodeURIComponent(unitId);
  if(forceRetake)url+='?retake=1';
  fetch(url).then(function(r){return r.json();}).then(function(j){
    try{
      if(j.error){g('player-wrap').innerHTML='<div class="as-err">'+esc(j.error)+'</div>';setStatus('error','status err');return;}
      AS.state=j;
      var a=j.assessment||{};var sub=j.latestSubmission||j.submission||{};
      AS.submissionId=sub.id||null;
      (sub.answers||[]).forEach(function(e){var id=e.answer&&e.answer.id;if(id)AS.answers[e.blockId]=id;});
      (a.sections||[]).forEach(function(sec){(sec.blocks||[]).forEach(function(b){AS.blockMap[b.id]=b;AS.order.push(b.id);});});
      AS.total=AS.order.length;
      if(sub.status==='submitted'){AS.submitted=true;renderAssessmentReview();}
      else{renderAssessment();}
    }catch(err){g('player-wrap').innerHTML='<div class="as-err">parse error: '+esc(err.message||err)+'</div>';}
  }).catch(function(e){g('player-wrap').innerHTML='<div class="as-err">'+esc(e.message||e)+'</div>';});
}
function asAnsweredCount(){var n=0;for(var k in AS.answers)if(AS.answers[k])n++;return n;}
function renderAssessment(){
  try{
    var a=AS.state.assessment||{};var curIdx=AS.curIdx;var bid=AS.order[curIdx];var b=AS.blockMap[bid];
    if(!b){renderAssessmentReview();return;}
    var bd=b.blockData||b.data||{};var qHtml=asBlockHtml(b);
    if(!qHtml||!qHtml.trim()){
      g('player-wrap').innerHTML='<div class="as-coming"><div class="as-icon">'+icon('clock',36)+'</div><h2>Coming Soon</h2><p>This test isn\'t available yet. The question content hasn\'t been published. Please check back later.</p></div>';
      setStatus('coming soon');return;
    }
    var opts=bd.options||[];var curAns=AS.answers[bid];var optsHtml='';
    for(var i=0;i<opts.length;i++){var o=opts[i];var sel=curAns===o.id?' sel':'';optsHtml+='<div class="as-opt'+sel+'" data-opt="'+esc(o.id)+'"><div class="as-radio"></div><div class="as-opt-body">'+asOptHtml(o)+'</div></div>';}
    if(bd.hasOptionOther){var otherSel=curAns&&curAns.indexOf('other:')===0?' sel':'';optsHtml+='<div class="as-opt'+otherSel+'" data-opt="other"><div class="as-radio"></div><div class="as-opt-body"><span>Other</span><input type="text" placeholder="your answer…" id="as-other-input" value="'+(otherSel?esc(curAns.slice(6)):'')+'"></div></div>';}
    var answered=asAnsweredCount();var pct=AS.total?Math.round(answered/AS.total*100):0;
    var html='<div class="as-wrap"><div class="as-inner">'
      +'<div class="as-head"><h1>'+esc(a.title||'Assessment')+'</h1><div class="as-sub">Question '+(curIdx+1)+' of '+AS.total+' · '+answered+' answered</div><div class="as-progress"><div style="width:'+pct+'%"></div></div></div>'
      +'<div class="as-q"><div class="as-q-num">Question '+(curIdx+1)+' / '+AS.total+'</div><div class="as-q-text">'+qHtml+'</div><div class="as-opts">'+optsHtml+'</div></div>'
      +'<div class="as-actions">'
      +'<button class="as-btn" id="as-prev" '+(curIdx===0?'disabled':'')+'>'+icon('chevleft',18)+' Prev</button>'
      +'<div style="display:flex;gap:10px">'
      +'<button class="as-btn" id="as-save">'+icon('check',18)+' Save</button>'
      +(curIdx<AS.total-1?'<button class="as-btn primary" id="as-next">Next '+icon('chevright',18)+'</button>':'<button class="as-btn danger" id="as-submit">Submit</button>')
      +'</div></div></div></div>';
    g('player-wrap').innerHTML=html;
    setStatus('assessment · Q'+(curIdx+1),'status ok');
    var optEls=g('player-wrap').querySelectorAll('.as-opt');
    for(var k=0;k<optEls.length;k++){(function(el){el.addEventListener('click',function(e){if(e.target&&e.target.tagName==='INPUT')return;var val=el.dataset.opt;if(val==='other'){var inp=g('as-other-input');AS.answers[bid]='other:'+(inp?inp.value:'');}else{AS.answers[bid]=val;}renderAssessment();});})(optEls[k]);}
    var oi=g('as-other-input');if(oi){oi.addEventListener('input',function(){AS.answers[bid]='other:'+this.value;});oi.addEventListener('click',function(e){e.stopPropagation();});}
    on('as-prev',function(){AS.curIdx=Math.max(0,AS.curIdx-1);renderAssessment();});
    var nx=g('as-next');if(nx)nx.addEventListener('click',function(){autosave();AS.curIdx=Math.min(AS.total-1,AS.curIdx+1);renderAssessment();});
    var sv=g('as-save');if(sv)sv.addEventListener('click',function(){autosave();});
    var sb=g('as-submit');if(sb)sb.addEventListener('click',submitAssessment);
  }catch(e){g('player-wrap').innerHTML='<div class="as-err">render error: '+esc(e.message||e)+'</div>';}
}
function asAnswersArray(){var arr=[];for(var bid in AS.answers){var v=AS.answers[bid];if(!v)continue;if(v.indexOf('other:')===0)arr.push({blockId:bid,answer:{text:v.slice(6)}});else arr.push({blockId:bid,answer:{id:v}});}return arr;}
function autosave(){if(!AS.submissionId||AS.submitted)return;var body={submission_id:AS.submissionId,answers:asAnswersArray()};fetch('/api/assessment/save/'+encodeURIComponent(AS.titleId)+'/'+encodeURIComponent(AS.unitId),{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}).then(function(r){return r.json();}).then(function(j){if(j.success||j.updated)setStatus('saved ✓','status ok');else setStatus('save failed','status err');}).catch(function(){});}
function submitAssessment(){
  if(!AS.submissionId)return;
  var unanswered=AS.total-asAnsweredCount();
  if(unanswered>0){if(!confirm('You have '+unanswered+' unanswered question'+(unanswered>1?'s':'')+'. Submit anyway?'))return;}
  setStatus('submitting…');
  var body={submission_id:AS.submissionId,answers:asAnswersArray()};
  fetch('/api/assessment/submit/'+encodeURIComponent(AS.titleId)+'/'+encodeURIComponent(AS.unitId),{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)})
    .then(function(r){return r.json();})
    .then(function(j){
      if(j.error||(j.errors&&j.errors.length)){
        var msg=(j.errors&&j.errors[0]&&j.errors[0].message)||j.error||'submit failed';
        setStatus(msg,'status err');
        if(String(msg).indexOf('already_submitted')!==-1){return fetch('/api/assessment/'+encodeURIComponent(AS.titleId)+'/'+encodeURIComponent(AS.unitId)).then(function(r){return r.json();}).then(function(fresh){AS.state=fresh;AS.submitted=true;renderAssessmentReview();});}
        return;
      }
      AS.submitted=true;
      return fetch('/api/assessment/'+encodeURIComponent(AS.titleId)+'/'+encodeURIComponent(AS.unitId)).then(function(r){return r.json();}).then(function(fresh){AS.state=fresh;renderAssessmentReview();});
    })
    .catch(function(e){setStatus('submit error','status err');});
}
function buildGradeMap(){
  var gg={};
  var fb=AS.state.feedback||[];
  for(var fi=0;fi<fb.length;fi++){var blocks=(fb[fi].blocks)||[];for(var bi=0;bi<blocks.length;bi++){var blk=blocks[bi];if(!blk||!blk.id)continue;gg[blk.id]={grade:blk.grade,blockMaxScore:blk.blockMaxScore,correct:(blk.grade!==null&&blk.grade!==undefined)?(blk.grade>0):null};}}
  var sub=AS.state.latestSubmission||AS.state.submission||{};
  (sub.answers||[]).forEach(function(a){if(!a||!a.blockId)return;var e=gg[a.blockId]||{};if(a.correct!==undefined&&a.correct!==null)e.correct=a.correct;if(a.correctAnswer&&a.correctAnswer.id)e.correctAnswer=a.correctAnswer.id;if(a.grade!==undefined&&a.grade!==null)e.grade=a.grade;gg[a.blockId]=e;});
  return gg;
}
function pieSvg(correct,wrong,neutral){
  var total=correct+wrong+neutral;if(!total)total=1;var r=50,c=2*Math.PI*r;var okLen=(correct/total)*c;var noLen=(wrong/total)*c;
  return '<svg width="120" height="120" viewBox="0 0 120 120">'
    +'<circle cx="60" cy="60" r="'+r+'" fill="none" stroke="rgba(124,134,151,.2)" stroke-width="14"/>'
    +(correct>0?'<circle cx="60" cy="60" r="'+r+'" fill="none" stroke="#2ecc71" stroke-width="14" stroke-dasharray="'+okLen+' '+c+'"/>':'')
    +(wrong>0?'<circle cx="60" cy="60" r="'+r+'" fill="none" stroke="#ff5c5c" stroke-width="14" stroke-dasharray="'+noLen+' '+c+'" stroke-dashoffset="'+(-okLen)+'"/>':'')
    +(neutral>0?'<circle cx="60" cy="60" r="'+r+'" fill="none" stroke="rgba(124,134,151,.6)" stroke-width="14" stroke-dasharray="'+((neutral/total)*c)+' '+c+'" stroke-dashoffset="'+(-(okLen+noLen))+'"/>':'')
    +'</svg>';
}
function renderAssessmentReview(){
  try{
    var a=AS.state.assessment||{};var sub=AS.state.latestSubmission||AS.state.submission||{};var title=a.title||'Assessment';
    var grades=buildGradeMap();var correct=0,wrong=0,neutral=0;
    for(var qi=0;qi<AS.order.length;qi++){var gg=grades[AS.order[qi]];if(!gg||gg.correct===null||gg.correct===undefined)neutral++;else if(gg.correct)correct++;else wrong++;}
    var pct=AS.total?Math.round(correct/AS.total*100):0;
    var html='<div class="as-wrap"><div class="as-inner">';
    html+='<div class="as-head"><h1>'+esc(title)+'</h1><div class="as-sub">✓ Submitted'+(sub.submittedTimestamp?' · '+new Date(sub.submittedTimestamp*1000).toLocaleString():'')+'</div></div>';
    html+='<div class="as-score-card">';
    html+='<div class="as-pie">'+pieSvg(correct,wrong,neutral)+'<div class="c"><div class="pct">'+pct+'%</div><div class="lbl">score</div></div></div>';
    html+='<div class="as-score-info"><div class="big">'+correct+' / '+AS.total+'</div><div class="sub">correct</div><div class="legend"><div class="row"><span class="dot ok"></span><span>'+correct+' correct</span></div><div class="row"><span class="dot no"></span><span>'+wrong+' wrong</span></div>'+(neutral>0?'<div class="row"><span class="dot neutral"></span><span>'+neutral+' ungraded</span></div>':'')+'</div></div></div>';
    for(var qi2=0;qi2<AS.order.length;qi2++){
      var bid=AS.order[qi2];var b=AS.blockMap[bid];if(!b)continue;
      var bd=b.blockData||b.data||{};var opts=bd.options||[];var userAns=AS.answers[bid];var gg2=grades[bid];
      var correctId=(gg2&&gg2.correctAnswer)||null;
      var qHtml=asBlockHtml(b)||'<em style="color:var(--muted)">(empty)</em>';
      var optsHtml='';
      for(var oi=0;oi<opts.length;oi++){var o=opts[oi];var cls='as-opt',tag='';if(userAns===o.id){if(gg2&&gg2.correct===true){cls+=' correct';tag='<span class="as-tag ok">✓</span>';}else if(gg2&&gg2.correct===false){cls+=' wrong';tag='<span class="as-tag no">✗</span>';}}else if(correctId&&o.id===correctId){cls+=' correct';tag='<span class="as-tag ok">✓ answer</span>';}optsHtml+='<div class="'+cls+'"><div class="as-radio"></div><div class="as-opt-body">'+asOptHtml(o)+'</div>'+tag+'</div>';}
      html+='<div class="as-review"><div class="as-q-num">Question '+(qi2+1)+' / '+AS.total+'</div><div class="as-q-text">'+qHtml+'</div><div class="as-opts">'+optsHtml+'</div></div>';
    }
    html+='<div class="as-actions"><button class="as-btn" id="as-back-btn">'+icon('arrowleft',18)+' Back</button><div style="display:flex;gap:10px"><button class="as-btn" id="as-refresh-btn">'+icon('refresh',18)+' Refresh</button><button class="as-btn primary" id="as-retake-btn">Retake</button></div></div>';
    html+='</div></div>';
    g('player-wrap').innerHTML=html;
    setStatus('assessment · submitted','status ok');
    on('as-back-btn',function(){closeBatch();});
    on('as-refresh-btn',function(){playAssessment(AS.titleId,AS.unitId,false);});
    on('as-retake-btn',function(){if(confirm('Start a new attempt?'))playAssessment(AS.titleId,AS.unitId,true);});
  }catch(e){g('player-wrap').innerHTML='<div class="as-err">review error: '+esc(e.message||e)+'</div>';}
}

/* ===== bootstrap ===== */
g('search').addEventListener('input',renderTOC);
g('batch-search').addEventListener('input',renderBatches);
renderThemePicker();
function loadAll(){var grid=g('batch-grid');if(!grid)return;grid.innerHTML='<div style="padding:24px;color:var(--muted);text-align:center;grid-column:1/-1">loading…</div>';fetch('/api/batches').then(function(r){return r.json();}).then(function(j){BATCHES=(j&&j.batches)||[];renderBatches();}).catch(function(e){grid.innerHTML='<div style="padding:24px;color:#ff7a7a;text-align:center;grid-column:1/-1">error: '+esc(e.message||e)+'</div>';});}
function loadLiveStats(){
  var el=g('total-batches');if(!el)return;
  fetch('/api/live/stats').then(function(r){return r.json();}).then(function(j){
    el.textContent = (j&&typeof j.total==='number') ? j.total : '—';
  }).catch(function(){el.textContent='—';});
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',function(){loadAll();loadLiveStats();});
else {loadAll();loadLiveStats();}

})();
"""
