"""Player + assessment frontend JS (injected into MAIN_PAGE)."""

PLAYER_JS = r"""
(function(){
'use strict';
var BATCHES=[],ACTIVE=null,FLAT=[],CURRENT=null,CURRENT_INFO=null,HLS=null,VIDEO=null,CURRENT_VARIANTS={};
var UI_T=null,LP_T=null,TAP_T=null,seekReset=null,seekSide=null,seekAcc=0,ripT=null,lastTapT=0,lastTapSide=null,lastPtr='mouse';
var CUR_SPEED=1,VOL=1,MUTED=false,QSEL=-1,QPREF=0,MENU_VIEW=null,SCRUB=false,HOLDING=false;
var DT_STEP=10;
var SPEEDS=[0.5,0.75,1,1.25,1.5,2];
var THEMES=["default","rose","green","amber","crimson","cyber","mono","sunset"];
var curTheme=localStorage.getItem("theme")||"default";
document.documentElement.setAttribute("data-theme",curTheme);
var PALETTES=[['#5c8dff','#7c5cff'],['#ff5c8d','#c45cff'],['#2ecc71','#13b6a3'],['#f6b73c','#ff8a4c'],['#ff5c5c','#b35cff'],['#00d4ff','#7c5cff'],['#ff7c5c','#ff5cbd'],['#9d5cff','#5c8dff'],['#00b894','#00cec9'],['#fdcb6e','#e17055'],['#e84393','#fd79a8'],['#6c5ce7','#a29bfe']];
window.cycleTheme=function(){var i=THEMES.indexOf(curTheme);i=(i+1)%THEMES.length;curTheme=THEMES[i];document.documentElement.setAttribute("data-theme",curTheme);localStorage.setItem("theme",curTheme);};
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
function g(id){return document.getElementById(id);}
function hashCode(s){var h=0;for(var i=0;i<s.length;i++){h=((h<<5)-h)+s.charCodeAt(i);h|=0;}return Math.abs(h);}
function pickGradient(l){return PALETTES[hashCode(l||'?')%PALETTES.length];}
function initials(l){var p=(l||'?').trim().split(/\s+/);if(p.length===1)return p[0].slice(0,2).toUpperCase();return (p[0].charAt(0)+p[1].charAt(0)).toUpperCase();}
function showPage(name){var pages=document.querySelectorAll('.page');for(var i=0;i<pages.length;i++)pages[i].classList.remove('active');var el=document.getElementById('page-'+name);if(el)el.classList.add('active');var items=document.querySelectorAll('.drawer-item[data-page]');for(var j=0;j<items.length;j++)items[j].classList.remove('active');var act=document.querySelector('.drawer-item[data-page="'+name+'"]');if(act)act.classList.add('active');}
window.goPage=function(name){showPage(name);closeDrawer();};
window.openDrawer=function(){document.getElementById('drawer').classList.add('open');document.getElementById('drawer-bg').classList.add('open');};
window.closeDrawer=function(){document.getElementById('drawer').classList.remove('open');document.getElementById('drawer-bg').classList.remove('open');};

function renderBatches(){
  var grid=document.getElementById('batch-grid');
  var q=(document.getElementById('batch-search').value||'').toLowerCase();
  grid.innerHTML='';
  var filtered=BATCHES.filter(function(b){return !q||(b.label||'').toLowerCase().indexOf(q)!==-1;});
  if(!filtered.length){grid.innerHTML='<div style="padding:24px;color:var(--muted);text-align:center;grid-column:1/-1">'+(BATCHES.length?'No batches match.':'No batches available.')+'</div>';return;}
  for(var i=0;i<filtered.length;i++){
    (function(b){
      var card=document.createElement('div');card.className='batch-card';
      var hasImg=b.image&&b.image.indexOf('course-default-img')===-1;
      var gr=pickGradient(b.label),ini=initials(b.label);
      var thumb,thumbStyle;
      if(hasImg){thumb='<img src="'+esc(b.image)+'" alt="">';thumbStyle='';}
      else{thumb='<div class="pattern"></div><div class="mono">'+esc(ini)+'</div>';thumbStyle=' style="background:linear-gradient(135deg,'+gr[0]+','+gr[1]+')"';}
      card.innerHTML=
        '<div class="thumb"'+thumbStyle+' data-tid="'+esc(b.titleId)+'" data-label="'+esc(b.label)+'">'+thumb+'</div>'+
        '<div class="meta"><span class="t">'+esc(b.label)+'</span><span class="s">tap to open</span></div>'+
        '<button class="study-btn" data-tid="'+esc(b.titleId)+'" data-label="'+esc(b.label)+'">▶ Study</button>';
      grid.appendChild(card);
    })(filtered[i]);
  }
}
document.addEventListener('click',function(e){
  var t=e.target;
  if(t.dataset&&t.dataset.tid){openBatch(t.dataset.tid,t.dataset.label);}
});

window.openBatch=function(titleId,label){
  ACTIVE=titleId;
  document.getElementById('viewer-title').textContent=label;
  document.getElementById('sections-title').textContent=label;
  document.getElementById('search').value='';
  document.getElementById('toc').innerHTML='<div style="padding:20px;color:var(--muted)">loading sections…</div>';
  document.getElementById('player-wrap').innerHTML='<div class="player-empty"><h2 class="brand-gradient">Pick a lecture</h2><p>Open playlist panel with ☰</p></div>';
  document.getElementById('controls').style.display='none';
  document.getElementById('nowplaying').textContent='';
  destroyPlayer();
  showPage('viewer');
  fetch('/api/sections/'+encodeURIComponent(titleId)).then(function(r){return r.json();}).then(function(j){
    if(!j||!j.sections){document.getElementById('toc').innerHTML='<div style="padding:20px;color:#ff7a7a">'+esc((j&&j.error)||'failed')+'</div>';return;}
    window._sections=j.sections;
    renderTOC();
    if(window.innerWidth>900)document.getElementById('sections-overlay').classList.add('open');
  }).catch(function(e){document.getElementById('toc').innerHTML='<div style="padding:20px;color:#ff7a7a">error: '+esc(e.message||e)+'</div>';});
};
window.closeBatch=function(){destroyPlayer();ACTIVE=null;document.getElementById('sections-overlay').classList.remove('open');showPage('batches');};
window.toggleSections=function(){document.getElementById('sections-overlay').classList.toggle('open');};

function renderTOC(){
  var toc=document.getElementById('toc');toc.innerHTML='';FLAT=[];
  var q=(document.getElementById('search').value||'').toLowerCase();
  var sections=window._sections||[];
  for(var si=0;si<sections.length;si++){
    var sec=sections[si];
    var units=sec.units.filter(function(u){return !q||((u.title||'').toLowerCase().indexOf(q)!==-1);});
    if(q&&units.length===0)continue;
    var secDiv=document.createElement('div');secDiv.className='sec';
    var head=document.createElement('div');head.className='sec-head'+(q?' open':'');
    head.innerHTML='<div class="left"><span class="t">'+esc(sec.title)+'</span></div><span class="cnt">'+sec.units.length+'</span>';
    var body=document.createElement('div');body.className='sec-body'+(q?' open':'');
    head.onclick=(function(h,b){return function(){h.classList.toggle('open');b.classList.toggle('open');};})(head,body);
    for(var ui=0;ui<units.length;ui++){
      var u=units[ui];var idx=FLAT.length;
      FLAT.push({unit:u,sectionTitle:sec.title});
      var uDiv=document.createElement('div');uDiv.className='unit';uDiv.dataset.idx=idx;
      uDiv.innerHTML='<div class="u-left"><span class="t">'+esc(u.title||u.id)+'</span></div><span class="type '+esc(u.type||'')+'">'+esc(u.type||'')+'</span>';
      (function(i){uDiv.onclick=function(){playUnit(i);};})(idx);
      body.appendChild(uDiv);
    }
    secDiv.appendChild(head);secDiv.appendChild(body);toc.appendChild(secDiv);
  }
}

function playUnit(idx){
  if(idx<0||idx>=FLAT.length)return;
  CURRENT=idx;var item=FLAT[idx];var u=item.unit;
  var units=document.querySelectorAll('.unit.active');
  for(var i=0;i<units.length;i++)units[i].classList.remove('active');
  var el=document.querySelector('.unit[data-idx="'+idx+'"]');
  if(el){el.classList.add('active');el.scrollIntoView({block:'nearest',behavior:'smooth'});}
  document.getElementById('nowplaying').textContent=u.title||'';
  document.getElementById('status').textContent='loading…';
  document.getElementById('status').className='status';
  document.getElementById('controls').style.display='none';
  destroyPlayer();
  fetch('/api/video/'+encodeURIComponent(ACTIVE)+'/'+encodeURIComponent(u.id)).then(function(r){return r.json();}).then(function(j){
    CURRENT_INFO=j;
    if(j.error){document.getElementById('player-wrap').innerHTML='<div class="player-empty"><p>error: '+esc(j.error)+'</p></div>';document.getElementById('status').textContent='error';document.getElementById('status').className='status err';return;}
    if(j.type==='wistia'&&j.sourceid){playWistia(j.sourceid);}
    else if(j.type==='pdf'){playPdf(ACTIVE,u.id);}
    else if(j.type==='assessment'){playAssessment(ACTIVE,u.id,j);}
    else{document.getElementById('player-wrap').innerHTML='<div class="player-empty"><p>unsupported: '+esc(j.type||'?')+'</p></div>';}
    if(window.innerWidth<=900)document.getElementById('sections-overlay').classList.remove('open');
  }).catch(function(e){document.getElementById('player-wrap').innerHTML='<div class="player-empty"><p>error: '+esc(e.message||e)+'</p></div>';});
}
function destroyPlayer(){
  clearTimeout(UI_T);clearTimeout(LP_T);clearTimeout(TAP_T);clearTimeout(seekReset);clearTimeout(ripT);
  seekSide=null;seekAcc=0;MENU_VIEW=null;SCRUB=false;HOLDING=false;
  if(HLS){try{HLS.destroy();}catch(e){}HLS=null;}
  if(VIDEO){try{VIDEO.pause();}catch(e){}VIDEO=null;}
  if(window._asTimer){clearInterval(window._asTimer);window._asTimer=null;}
}

/* ================= YouTube-style player ================= */
var IC={
  play:'M8 5v14l11-7z',
  pause:'M6 19h4V5H6v14zm8-14v14h4V5h-4z',
  replay:'M12 5V1L7 6l5 5V7c3.31 0 6 2.69 6 6s-2.69 6-6 6-6-2.69-6-6H4c0 4.42 3.58 8 8 8s8-3.58 8-8-3.58-8-8-8z',
  prev:'M6 6h2v12H6zm3.5 6l8.5 6V6z',
  next:'M6 18l8.5-6L6 6v12zM16 6v12h2V6h-2z',
  vol:'M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02z',
  mute:'M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3L3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4L9.91 6.09 12 8.18V4z',
  gear:'M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58a.49.49 0 0 0 .12-.61l-1.92-3.32a.488.488 0 0 0-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54a.484.484 0 0 0-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58a.49.49 0 0 0-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z',
  fs:'M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z',
  exitfs:'M5 16h3v3h2v-5H5v2zm3-8H5v2h5V5H8v3zm6 11h2v-3h3v-2h-5v5zm2-11V5h-2v5h5V8h-3z',
  list:'M3 13h2v-2H3v2zm0 4h2v-2H3v2zm0-8h2V7H3v2zm4 4h14v-2H7v2zm0 4h14v-2H7v2zM7 7v2h14V7H7z',
  dl:'M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z',
  link:'M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z'
};
function ic(n,s){s=s||24;return '<svg viewBox="0 0 24 24" width="'+s+'" height="'+s+'" fill="currentColor"><path d="'+IC[n]+'"/></svg>';}
function setStatus(t,c){var s=g('status');if(!s)return;s.textContent=t;s.className=c||'status';}

function buildPlayerUI(){
  var title=(CURRENT!=null&&FLAT[CURRENT])?(FLAT[CURRENT].unit.title||''):'';
  g('player-wrap').innerHTML=
  '<div class="yt show" id="yt">'+
    '<video id="v" playsinline webkit-playsinline preload="metadata"></video>'+
    '<div class="yt-gl" id="yt-gl"></div>'+
    '<div class="yt-logo brand-gradient">SeongEra</div>'+
    '<div class="yt-rip l" id="yt-rl"><div class="in"><span class="ar">'+ic('replay',30)+'</span><span id="yt-rlt">10 seconds</span></div></div>'+
    '<div class="yt-rip r" id="yt-rr"><div class="in"><span class="ar flip">'+ic('replay',30)+'</span><span id="yt-rrt">10 seconds</span></div></div>'+
    '<div class="yt-2x" id="yt-2x">▶▶ 2× speed</div>'+
    '<div class="yt-spin" id="yt-spin"></div>'+
    '<div class="yt-top" id="yt-top"><div class="yt-title" id="yt-title">'+esc(title)+'</div></div>'+
    '<div class="yt-center" id="yt-center">'+
      '<button class="yt-sb" id="yt-prev" title="Previous lecture">'+ic('prev',28)+'</button>'+
      '<button class="yt-big" id="yt-big" title="Play / Pause">'+ic('play',40)+'</button>'+
      '<button class="yt-sb" id="yt-next" title="Next lecture">'+ic('next',28)+'</button>'+
    '</div>'+
    '<div class="yt-bottom" id="yt-bottom">'+
      '<div class="yt-pb" id="yt-pb"><div class="yt-track"><div class="yt-buf" id="yt-buf"></div><div class="yt-fill" id="yt-fill"></div><div class="yt-knob" id="yt-knob"></div></div><div class="yt-tip" id="yt-tip">0:00</div></div>'+
      '<div class="yt-row">'+
        '<div class="yt-l">'+
          '<button class="yb yt-hide-sm" id="yt-pp" title="Play / Pause">'+ic('play')+'</button>'+
          '<span class="yt-volwrap"><button class="yb yt-hide-sm" id="yt-mute" title="Mute">'+ic('vol')+'</button><input class="yt-vol" id="yt-vol" type="range" min="0" max="1" step="0.05" value="1"></span>'+
          '<span class="yt-time" id="yt-time">0:00 / 0:00</span>'+
        '</div>'+
        '<div class="yt-r">'+
          '<button class="yb" id="yt-list" title="Playlist">'+ic('list')+'</button>'+
          '<button class="yb" id="yt-dl" title="Download">'+ic('dl')+'</button>'+
          '<button class="yb" id="yt-lk" title="Get m3u8 link">'+ic('link')+'</button>'+
          '<button class="yb" id="yt-set" title="Settings">'+ic('gear')+'</button>'+
          '<button class="yb" id="yt-fs" title="Fullscreen">'+ic(fsEl()?'exitfs':'fs')+'</button>'+
        '</div>'+
      '</div>'+
    '</div>'+
    '<div class="yt-menu" id="yt-menu"></div>'+
  '</div>';
  bindUI();
  syncNav();
}

function on(id,fn){var el=g(id);if(el)el.addEventListener('click',fn);}
function bindUI(){
  var y=g('yt');
  if(!y)return;
  y.addEventListener('mousemove',showUI);
  var zones=['yt-top','yt-bottom','yt-center'];
  for(var i=0;i<zones.length;i++){var z=g(zones[i]);if(z)z.addEventListener('pointerdown',function(e){e.stopPropagation();showUI();});}
  on('yt-big',function(e){e.stopPropagation();window.togglePlay();});
  on('yt-pp',function(e){e.stopPropagation();window.togglePlay();});
  on('yt-prev',function(e){e.stopPropagation();window.playPrev();});
  on('yt-next',function(e){e.stopPropagation();window.playNext();});
  on('yt-mute',function(e){e.stopPropagation();window.toggleMute();});
  on('yt-list',function(e){e.stopPropagation();leaveFS();window.toggleSections();});
  on('yt-dl',function(e){e.stopPropagation();leaveFS();window.openDownload();});
  on('yt-lk',function(e){e.stopPropagation();leaveFS();window.openLink();});
  on('yt-set',function(e){e.stopPropagation();if(MENU_VIEW)closeMenu();else openMenu('main');});
  on('yt-fs',function(e){e.stopPropagation();window.toggleFS();});
  var vv=g('yt-vol'); if(vv) vv.addEventListener('input',function(e){e.stopPropagation();if(!VIDEO)return;var v=parseFloat(this.value);VIDEO.volume=v;VIDEO.muted=(v===0);});
  var mm=g('yt-menu'); if(mm) mm.addEventListener('click',function(e){
    e.stopPropagation();
    var t=e.target;
    while(t&&t!==this&&!(t.dataset&&(t.dataset.go||t.dataset.q!==undefined||t.dataset.s!==undefined)))t=t.parentNode;
    if(!t||t===this)return;
    if(t.dataset.go){MENU_VIEW=t.dataset.go;renderMenu();return;}
    if(t.dataset.q!==undefined){setQuality(t.dataset.q);closeMenu();return;}
    if(t.dataset.s!==undefined){window.setSpeed(t.dataset.s);closeMenu();}
  });
  bindProgress();
  bindGestures();
}

function bindVideo(){
  var v=VIDEO;
  v.addEventListener('timeupdate',updateTime);
  v.addEventListener('progress',updateTime);
  v.addEventListener('durationchange',updateTime);
  v.addEventListener('loadedmetadata',function(){if(!HOLDING)v.playbackRate=CUR_SPEED;updateTime();});
  v.addEventListener('play',function(){syncPlay();showUI();});
  v.addEventListener('pause',function(){if(!VIDEO)return;syncPlay();showUI();setStatus('paused','status');});
  v.addEventListener('playing',function(){if(!VIDEO)return;setBuf(false);syncPlay();setStatus(playingLabel(),'status ok');showUI();});
  v.addEventListener('waiting',function(){if(!VIDEO)return;setBuf(true);setStatus('buffering…','status');});
  v.addEventListener('canplay',function(){setBuf(false);});
  v.addEventListener('seeked',function(){setBuf(false);});
  v.addEventListener('ended',function(){syncPlay();showUI();});
  v.addEventListener('volumechange',syncVol);
  v.addEventListener('error',function(){if(!VIDEO)return;setBuf(false);setStatus('video error','status err');});
}
function playingLabel(){
  if(HLS&&HLS.levels&&HLS.currentLevel>=0&&HLS.levels[HLS.currentLevel]&&HLS.levels[HLS.currentLevel].height)return 'playing · '+HLS.levels[HLS.currentLevel].height+'p';
  return 'playing';
}
function setBuf(on){var y=g('yt'),s=g('yt-spin');if(!y||!s)return;y.classList.toggle('buf',on);s.classList.toggle('on',on);}
function syncPlay(){
  if(!VIDEO||!g('yt-big'))return;
  var playing=!VIDEO.paused&&!VIDEO.ended;
  var n=VIDEO.ended?'replay':(playing?'pause':'play');
  g('yt-big').innerHTML=ic(n,40);
  g('yt-pp').innerHTML=ic(n);
  var y=g('yt');
  if(y)y.classList.toggle('yt-paused',!playing);
}
function syncNav(){
  var p=g('yt-prev'),n=g('yt-next');if(!p||!n)return;
  p.disabled=!(CURRENT!=null&&CURRENT>0);
  n.disabled=!(CURRENT!=null&&CURRENT<FLAT.length-1);
}
function syncVol(){
  if(!VIDEO||!g('yt-mute'))return;
  MUTED=VIDEO.muted;
  if(!VIDEO.muted&&VIDEO.volume>0)VOL=VIDEO.volume;
  var eff=VIDEO.muted?0:VIDEO.volume;
  g('yt-mute').innerHTML=ic(eff===0?'mute':'vol');
  var s=g('yt-vol');if(!s)return;s.value=eff;
  var p=Math.round(eff*100);
  s.style.background='linear-gradient(90deg,#fff '+p+'%,rgba(255,255,255,.3) '+p+'%)';
}
function showUI(){
  var y=g('yt');if(!y)return;
  y.classList.add('show');
  clearTimeout(UI_T);
  if(VIDEO&&!VIDEO.paused&&!SCRUB&&!MENU_VIEW&&!HOLDING){UI_T=setTimeout(hideUI,3200);}
}
function hideUI(){
  var y=g('yt');
  if(!y||!VIDEO||VIDEO.paused||SCRUB||MENU_VIEW)return;
  y.classList.remove('show');
}
function dur(){var d=VIDEO&&VIDEO.duration;return (d&&isFinite(d))?d:0;}
function setProg(pct){var f=g('yt-fill'),k=g('yt-knob');if(!f)return;f.style.width=pct+'%';k.style.left=pct+'%';}
function updateTime(){
  if(!VIDEO||!g('yt-time'))return;
  var cur=VIDEO.currentTime||0,d=dur();
  if(!SCRUB){
    g('yt-time').textContent=fmt(cur)+' / '+fmt(d);
    setProg(d?Math.min(100,cur/d*100):0);
  }
  var b=VIDEO.buffered;
  if(d&&b&&b.length){
    var end=b.end(b.length-1);
    for(var i=0;i<b.length;i++){if(b.start(i)<=cur+0.5&&b.end(i)>=cur){end=b.end(i);break;}}
    g('yt-buf').style.width=Math.min(100,end/d*100)+'%';
  }
}
function fmt(s){s=Math.floor(s||0);if(!isFinite(s))s=0;var h=Math.floor(s/3600),m=Math.floor((s%3600)/60),r=s%60;if(h)return h+':'+(m<10?'0':'')+m+':'+(r<10?'0':'')+r;return m+':'+(r<10?'0':'')+r;}
function bindProgress(){
  var pb=g('yt-pb'),tip=g('yt-tip');if(!pb||!tip)return;
  function pos(e){var r=pb.getBoundingClientRect();return Math.max(0,Math.min(1,(e.clientX-r.left)/r.width));}
  function showTip(p){
    var w=pb.getBoundingClientRect().width;
    var x=Math.max(26,Math.min(w-26,p*w));
    tip.style.left=x+'px';tip.textContent=fmt(p*dur());tip.style.opacity='1';
  }
  function scrub(e){
    var p=pos(e),d=dur();
    setProg(p*100);
    g('yt-time').textContent=fmt(p*d)+' / '+fmt(d);
    showTip(p);
  }
  pb.addEventListener('pointerdown',function(e){
    if(!VIDEO||!dur())return;
    e.stopPropagation();
    SCRUB=true;pb.classList.add('drag');
    try{pb.setPointerCapture(e.pointerId);}catch(x){}
    scrub(e);showUI();
  });
  pb.addEventListener('pointermove',function(e){
    if(!dur())return;
    if(SCRUB)scrub(e);else showTip(pos(e));
  });
  function finish(e,apply){
    if(!SCRUB)return;
    SCRUB=false;pb.classList.remove('drag');tip.style.opacity='0';
    if(apply&&VIDEO&&dur()){VIDEO.currentTime=pos(e)*dur();}
    updateTime();showUI();
  }
  pb.addEventListener('pointerup',function(e){finish(e,true);});
  pb.addEventListener('pointercancel',function(e){finish(e,false);});
  pb.addEventListener('pointerleave',function(){if(!SCRUB)tip.style.opacity='0';});
}

function qualityLabel(){
  if(!HLS||!HLS.levels||!HLS.levels.length)return 'Auto';
  if(QSEL===-1){var l=HLS.levels[HLS.currentLevel];return 'Auto'+(l&&l.height?' ('+l.height+'p)':'');}
  var l2=HLS.levels[QSEL];return l2&&l2.height?l2.height+'p':'L'+QSEL;
}
function openMenu(view){MENU_VIEW=view;renderMenu();var m=g('yt-menu');if(m)m.classList.add('open');showUI();}
function closeMenu(){MENU_VIEW=null;var m=g('yt-menu');if(m)m.classList.remove('open');showUI();}
function renderMenu(){
  var m=g('yt-menu');if(!m)return;
  var h='';
  if(MENU_VIEW==='main'){
    h+='<div class="mi" data-go="quality"><span>Quality</span><span class="v">'+esc(qualityLabel())+' ›</span></div>';
    h+='<div class="mi" data-go="speed"><span>Playback speed</span><span class="v">'+(CUR_SPEED===1?'Normal':CUR_SPEED+'×')+' ›</span></div>';
  }else if(MENU_VIEW==='quality'){
    h+='<div class="mh" data-go="main">‹ Quality</div>';
    var lv=[];
    if(HLS&&HLS.levels){for(var i=0;i<HLS.levels.length;i++){lv.push({i:i,h:HLS.levels[i].height||0});}}
    lv.sort(function(a,b){return b.h-a.h;});
    for(var j=0;j<lv.length;j++){
      h+='<div class="mi'+(QSEL===lv[j].i?' sel':'')+'" data-q="'+lv[j].i+'"><span>'+(QSEL===lv[j].i?'✓ ':'')+(lv[j].h?lv[j].h+'p':'L'+lv[j].i)+'</span></div>';
    }
    h+='<div class="mi'+(QSEL===-1?' sel':'')+'" data-q="auto"><span>'+(QSEL===-1?'✓ ':'')+'Auto</span></div>';
  }else if(MENU_VIEW==='speed'){
    h+='<div class="mh" data-go="main">‹ Playback speed</div>';
    for(var k=0;k<SPEEDS.length;k++){
      var sp=SPEEDS[k];
      h+='<div class="mi'+(CUR_SPEED===sp?' sel':'')+'" data-s="'+sp+'"><span>'+(CUR_SPEED===sp?'✓ ':'')+(sp===1?'Normal':sp+'×')+'</span></div>';
    }
  }
  m.innerHTML=h;
}
function setQuality(v){
  if(v==='auto'){QSEL=-1;QPREF=0;}
  else{QSEL=parseInt(v,10);var l=HLS&&HLS.levels&&HLS.levels[QSEL];QPREF=l?(l.height||0):0;}
  if(HLS)HLS.currentLevel=QSEL;
}
window.onQualityChange=function(v){setQuality(v);};
window.setSpeed=function(v){CUR_SPEED=parseFloat(v)||1;if(VIDEO&&!HOLDING)VIDEO.playbackRate=CUR_SPEED;};

function bindGestures(){
  var gl=g('yt-gl');if(!gl)return;
  var down=false,holding=false,moved=false,sx=0,sy=0;
  var isTouch=false;
  function sideOf(e){var r=gl.getBoundingClientRect();var x=(e.clientX-r.left)/r.width;return x<0.35?'l':(x>0.65?'r':'c');}
  gl.addEventListener('contextmenu',function(e){e.preventDefault();});
  gl.addEventListener('pointerdown',function(e){
    if(e.pointerType==='mouse'&&e.button!==0)return;
    lastPtr=e.pointerType||'mouse';
    isTouch=(e.pointerType==='touch'||e.pointerType==='pen');
    down=true;holding=false;moved=false;sx=e.clientX;sy=e.clientY;
    clearTimeout(LP_T);
    if(isTouch){
      LP_T=setTimeout(function(){
        if(!down||moved||!VIDEO||VIDEO.paused||MENU_VIEW)return;
        holding=true;startHold();
      },450);
    }
  });
  gl.addEventListener('pointermove',function(e){
    if(e.pointerType==='mouse')showUI();
    if(down&&!holding&&(Math.abs(e.clientX-sx)>12||Math.abs(e.clientY-sy)>12)){moved=true;clearTimeout(LP_T);}
  });
  function end(e,cancel){
    if(!down)return;
    down=false;clearTimeout(LP_T);
    if(holding){holding=false;stopHold();return;}
    if(cancel||moved)return;
    onTap(sideOf(e),isTouch);
  }
  gl.addEventListener('pointerup',function(e){end(e,false);});
  gl.addEventListener('pointercancel',function(e){end(e,true);});
  gl.addEventListener('pointerleave',function(e){if(down&&holding)end(e,true);});
}
function startHold(){
  if(!VIDEO)return;
  HOLDING=true;VIDEO.playbackRate=2;
  var b=g('yt-2x');if(b)b.classList.add('on');
  var y=g('yt');if(y)y.classList.remove('show');
  clearTimeout(UI_T);
  try{if(navigator.vibrate)navigator.vibrate(15);}catch(e){}
}
function stopHold(){
  HOLDING=false;
  if(VIDEO)VIDEO.playbackRate=CUR_SPEED;
  var b=g('yt-2x');if(b)b.classList.remove('on');
}
function onTap(side,isTouch){
  if(MENU_VIEW){closeMenu();return;}
  var now=Date.now();
  if(seekSide&&side===seekSide&&side!=='c'){doSeek(side);return;}
  if(now-lastTapT<280&&lastTapSide===side){
    clearTimeout(TAP_T);lastTapT=0;
    if(side==='c'){
      if(isTouch){showUI();}else{window.toggleFS();}
    }else{doSeek(side);}
    return;
  }
  lastTapT=now;lastTapSide=side;
  clearTimeout(TAP_T);
  TAP_T=setTimeout(function(){singleTap(isTouch);},280);
}
function singleTap(isTouch){
  if(isTouch){
    var y=g('yt');
    if(!y)return;
    if(!y.classList.contains('show')){showUI();}
    else{clearTimeout(UI_T);if(VIDEO&&!VIDEO.paused)UI_T=setTimeout(hideUI,3200);}
    return;
  }
  window.togglePlay();
  showUI();
}
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

/* ================= video loading ================= */
function playWistia(sourceid){
  var master='https://fast.wistia.com/embed/medias/'+sourceid+'.m3u8';
  buildPlayerUI();
  VIDEO=g('v');
  VIDEO.volume=VOL;VIDEO.muted=MUTED;VIDEO.playbackRate=CUR_SPEED;
  QSEL=-1;
  bindVideo();
  syncVol();syncPlay();
  setBuf(true);
  fetch('/api/variants/'+encodeURIComponent(sourceid)).then(function(r){return r.json();}).then(function(j){CURRENT_VARIANTS=(j&&j.variants)||{};}).catch(function(){CURRENT_VARIANTS={};});
  if(window.Hls&&Hls.isSupported()){
    HLS=new Hls({capLevelToPlayerSize:false,startLevel:-1,autoStartLoad:true,maxBufferLength:60});
    HLS.loadSource(master);HLS.attachMedia(VIDEO);
    HLS.on(Hls.Events.MANIFEST_PARSED,function(e,data){
      if(QPREF){
        for(var i=0;i<data.levels.length;i++){if(data.levels[i].height===QPREF){QSEL=i;HLS.currentLevel=i;break;}}
      }
      if(MENU_VIEW)renderMenu();
      VIDEO.play().catch(function(){});
    });
    HLS.on(Hls.Events.LEVEL_SWITCHED,function(e,data){
      var lvl=HLS.levels[data.level];
      if(lvl){setStatus('playing · '+(lvl.height||'?')+'p','status ok');}
      if(MENU_VIEW)renderMenu();
    });
    HLS.on(Hls.Events.ERROR,function(e,d){
      if(!d||!d.fatal)return;
      if(d.type===Hls.ErrorTypes.NETWORK_ERROR){setStatus('network error · retrying','status err');try{HLS.startLoad();}catch(x){}}
      else if(d.type===Hls.ErrorTypes.MEDIA_ERROR){try{HLS.recoverMediaError();}catch(x){}}
      else{setBuf(false);setStatus('playback error','status err');}
    });
  }else if(VIDEO.canPlayType('application/vnd.apple.mpegurl')){VIDEO.src=master;VIDEO.play().catch(function(){});}
  document.getElementById('status').textContent='playing';
  attachAutoNext();
}

function attachAutoNext(){
  if(!VIDEO) return;
  VIDEO.addEventListener('ended', function(){
    if(CURRENT != null && CURRENT < FLAT.length - 1){
      document.getElementById('status').textContent='auto-playing next…';
      playUnit(CURRENT + 1);
    }
  });
}

/* ================= assessment player ================= */
var AS = { state:null, titleId:null, unitId:null, submissionId:null,
           answers:{}, order:[], blockMap:{}, curIdx:0, total:0, submitted:false };

// bulletproof extractor — tries every known shape, logs nothing if it works
function _asWidgetsToHtml(desc){
  if(!desc)return '';
  // desc could be {widgets:[...]} or a list directly or {html:...}
  var widgets = desc.widgets;
  if(!widgets && Array.isArray(desc)) widgets = desc;
  if(!widgets) return desc.html || desc.text || '';
  var parts=[];
  for(var i=0;i<widgets.length;i++){
    var w=widgets[i];
    if(!w)continue;
    if(typeof w==='string'){parts.push(w);continue;}
    var t=w.type||'';
    var p=w.properties||{};
    if(t==='text'&&p.html){parts.push(p.html);}
    else if(t==='html'&&p.html){parts.push(p.html);}
    else if(t==='spacer'){var hh=(p.height||12);parts.push('<div style="height:'+hh+'px"></div>');}
    else if(t==='image'){var u=p.url||p.src;if(u)parts.push('<img src="'+esc(u)+'" style="max-width:100%;border-radius:8px">');}
    else if(t==='button'&&p.buttonLabel){parts.push('<span>'+p.buttonLabel+'</span>');}
    else if(p.html){parts.push(p.html);}
  }
  return parts.join('');
}

function asWidgetHtml(widgets){
  return _asWidgetsToHtml({widgets:widgets});
}

function extractBlockHtml(block){
  if(!block)return '(empty block)';
  var bd=block.blockData||block.data||{};
  var desc=bd.description||{};
  var html=_asWidgetsToHtml(desc);
  if(!html && typeof desc==='string') html=desc;
  if(!html) html='<em style="color:#7c8697">(no text in this block)</em>';
  return html;
}

function extractOptionHtml(option){
  if(!option)return '';
  var d=option.description||{};
  var html=_asWidgetsToHtml(d);
  if(!html && typeof d==='string') html=d;
  return html || esc(option.id||'');
}

function playAssessment(titleId,unitId,info){
  AS.state=null;AS.titleId=titleId;AS.unitId=unitId;AS.answers={};
  AS.order=[];AS.blockMap={};AS.curIdx=0;AS.total=0;AS.submitted=false;
  g('player-wrap').innerHTML='<div class="as-loading"><div class="sp"></div><div>loading assessment…</div></div>';
  setStatus('assessment','status');
  fetch('/api/assessment/'+encodeURIComponent(titleId)+'/'+encodeURIComponent(unitId))
    .then(function(r){return r.json();})
    .then(function(j){
      try{
        if(j.error){g('player-wrap').innerHTML='<div class="as-err">'+esc(j.error)+'</div>';setStatus('error','status err');return;}
        AS.state=j;
        var a=j.assessment||{};
        var sub=j.latestSubmission||j.submission||{};
        AS.submissionId=sub.id||null;
        var pre=(sub.answers||[]);
        for(var i=0;i<pre.length;i++){
          var e=pre[i];
          var id=e.answer&&e.answer.id;
          if(id)AS.answers[e.blockId]=id;
        }
        var secs=a.sections||[];
        for(var si=0;si<secs.length;si++){
          var blocks=secs[si].blocks||[];
          for(var bi=0;bi<blocks.length;bi++){
            var b=blocks[bi];
            AS.blockMap[b.id]=b;
            AS.order.push(b.id);
          }
        }
        AS.total=AS.order.length;
        if(sub.status==='submitted'){AS.submitted=true;renderAssessmentReview();}
        else{renderAssessment();}
      }catch(err){
        console.error('playAssessment parse error',err);
        g('player-wrap').innerHTML='<div class="as-err">parse error: '+esc(err.message||err)+'</div>';
      }
    })
    .catch(function(e){
      console.error('playAssessment fetch error',e);
      g('player-wrap').innerHTML='<div class="as-err">'+esc(e.message||e)+'</div>';
    });
}

function asAnsweredCount(){var n=0;for(var k in AS.answers)if(AS.answers[k])n++;return n;}

function renderAssessment(){
  try{
    var a=AS.state.assessment||{};
    var title=a.title||'Assessment';
    var curIdx=AS.curIdx;
    var blockId=AS.order[curIdx];
    var block=AS.blockMap[blockId];
    if(!block){renderAssessmentReview();return;}
    var bd=block.blockData||block.data||{};
    var qHtml=extractBlockHtml(block);
    var opts=bd.options||[];
    var optsHtml='';
    var curAns=AS.answers[blockId];
    for(var i=0;i<opts.length;i++){
      var o=opts[i];
      var oHtml=extractOptionHtml(o);
      var sel=curAns===o.id?' sel':'';
      optsHtml+='<div class="as-opt'+sel+'" data-opt="'+esc(o.id)+'"><div class="as-radio"></div><div class="as-opt-body">'+oHtml+'</div></div>';
    }
    if(bd.hasOptionOther){
      var otherSel=curAns&&curAns.indexOf('other:')===0?' sel':'';
      optsHtml+='<div class="as-opt'+otherSel+'" data-opt="other"><div class="as-radio"></div><div class="as-opt-body"><span>Other</span><input type="text" placeholder="your answer…" id="as-other-input" value="'+(otherSel?esc(curAns.slice(6)):'')+'"></div></div>';
    }
    var answered=asAnsweredCount();
    var pct=AS.total?Math.round(answered/AS.total*100):0;
    var html=
      '<div class="as-wrap"><div class="as-inner">'+
        '<div class="as-head">'+
          '<div style="flex:1;min-width:0"><h1>'+esc(title)+'</h1>'+
            '<div class="as-sub">Question '+(curIdx+1)+' of '+AS.total+' · '+answered+' answered</div>'+
            '<div class="as-progress"><div style="width:'+pct+'%"></div></div>'+
          '</div>'+
        '</div>'+
        '<div class="as-q">'+
          '<div class="as-q-num">Question '+(curIdx+1)+' / '+AS.total+'</div>'+
          '<div class="as-q-text">'+qHtml+'</div>'+
          '<div class="as-opts">'+optsHtml+'</div>'+
        '</div>'+
        '<div class="as-actions">'+
          '<button class="as-btn" id="as-prev" '+(curIdx===0?'disabled':'')+'>← Prev</button>'+
          '<div style="display:flex;gap:10px">'+
            '<button class="as-btn primary" id="as-save">Save</button>'+
            (curIdx<AS.total-1
              ? '<button class="as-btn primary" id="as-next">Next →</button>'
              : '<button class="as-btn danger" id="as-submit">Submit</button>')+
          '</div>'+
        '</div>'+
      '</div></div>';
    g('player-wrap').innerHTML=html;
    setStatus('assessment · Q'+(curIdx+1),'status ok');
    var optEls=g('player-wrap').querySelectorAll('.as-opt');
    for(var k=0;k<optEls.length;k++){
      (function(el){
        el.addEventListener('click',function(e){
          if(e.target&&e.target.tagName==='INPUT')return;
          var val=el.dataset.opt;
          if(val==='other'){
            var inp=g('as-other-input');
            AS.answers[blockId]='other:'+(inp?inp.value:'');
          }else{
            AS.answers[blockId]=val;
          }
          renderAssessment();
        });
      })(optEls[k]);
    }
    var oi=g('as-other-input');
    if(oi){
      oi.addEventListener('input',function(){AS.answers[blockId]='other:'+this.value;});
      oi.addEventListener('click',function(e){e.stopPropagation();});
    }
    on('as-prev',function(){AS.curIdx=Math.max(0,AS.curIdx-1);renderAssessment();});
    var nx=g('as-next');if(nx)nx.addEventListener('click',function(){autosave();AS.curIdx=Math.min(AS.total-1,AS.curIdx+1);renderAssessment();});
    var sv=g('as-save');if(sv)sv.addEventListener('click',function(){autosave();});
    var sb=g('as-submit');if(sb)sb.addEventListener('click',submitAssessment);
  }catch(e){
    console.error('renderAssessment error',e);
    g('player-wrap').innerHTML='<div class="as-err">render error: '+esc(e.message||e)+'</div>';
  }
}

function asAnswersArray(){
  var arr=[];
  for(var bid in AS.answers){
    var v=AS.answers[bid];
    if(!v)continue;
    if(v.indexOf('other:')===0){
      arr.push({blockId:bid, answer:{text:v.slice(6)}});
    }else{
      arr.push({blockId:bid, answer:{id:v}});
    }
  }
  return arr;
}

function autosave(){
  if(!AS.submissionId||AS.submitted)return;
  var body={submission_id:AS.submissionId, answers:asAnswersArray()};
  fetch('/api/assessment/save/'+encodeURIComponent(AS.titleId)+'/'+encodeURIComponent(AS.unitId),
    {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)})
    .then(function(r){return r.json();})
    .then(function(j){if(j.success||j.updated)setStatus('saved ✓','status ok');})
    .catch(function(){});
}

function submitAssessment(){
  if(!AS.submissionId)return;
  var unanswered=AS.total-asAnsweredCount();
  if(unanswered>0){
    if(!confirm('You have '+unanswered+' unanswered question'+(unanswered>1?'s':'')+'. Submit anyway?'))return;
  }
  setStatus('submitting…','status');
  var body={submission_id:AS.submissionId, answers:asAnswersArray()};
  fetch('/api/assessment/submit/'+encodeURIComponent(AS.titleId)+'/'+encodeURIComponent(AS.unitId),
    {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)})
    .then(function(r){return r.json();})
    .then(function(j){
      if(j.error){setStatus('submit failed: '+j.error,'status err');return;}
      AS.submitted=true;
      return fetch('/api/assessment/'+encodeURIComponent(AS.titleId)+'/'+encodeURIComponent(AS.unitId))
        .then(function(r){return r.json();})
        .then(function(fresh){
          AS.state=fresh;
          renderAssessmentReview();
        });
    })
    .catch(function(e){setStatus('submit error','status err');});
}

function renderAssessmentReview(){
  try{
    var a=AS.state.assessment||{};
    var sub=AS.state.latestSubmission||{};
    var title=a.title||'Assessment';
    var grades={};
    var correctCount=0, gradedCount=0;
    var subAnswers=sub.answers||[];
    for(var i=0;i<subAnswers.length;i++){
      var e=subAnswers[i];
      grades[e.blockId]=e;
      if(e.graded){gradedCount++; if(e.correct)correctCount++;}
    }
    var html='<div class="as-wrap"><div class="as-inner">';
    html+='<div class="as-head"><div style="flex:1;min-width:0"><h1>'+esc(title)+'</h1><div class="as-sub">✓ Submitted · reviewed</div></div></div>';
    if(gradedCount>0){
      var pct=Math.round(correctCount/gradedCount*100);
      html+='<div class="as-score-card"><div class="num">'+correctCount+' / '+gradedCount+'</div><div class="lbl">'+pct+'% correct</div></div>';
    }else{
      html+='<div class="as-score-card"><div class="num">✓</div><div class="lbl">Submitted</div></div>';
    }
    for(var qi=0;qi<AS.order.length;qi++){
      var bid=AS.order[qi];
      var block=AS.blockMap[bid];
      if(!block)continue;
      var bd=block.blockData||block.data||{};
      var qHtml=extractBlockHtml(block);
      var opts=bd.options||[];
      var userAns=AS.answers[bid];
      var grade=grades[bid];
      var correctOptId=null;
      if(grade&&grade.correctAnswer&&grade.correctAnswer.id)correctOptId=grade.correctAnswer.id;
      var optsHtml='';
      for(var oi=0;oi<opts.length;oi++){
        var o=opts[oi];
        var oHtml=extractOptionHtml(o);
        var cls='as-opt';
        var tag='';
        if(userAns===o.id){
          if(grade&&grade.correct){cls+=' correct';tag='<span class="as-tag ok">✓ correct</span>';}
          else if(grade&&!grade.correct){cls+=' wrong';tag='<span class="as-tag no">✗ wrong</span>';}
        }else if(correctOptId&&o.id===correctOptId){
          cls+=' correct';tag='<span class="as-tag ok">✓ answer</span>';
        }
        optsHtml+='<div class="'+cls+'"><div class="as-radio"></div><div class="as-opt-body">'+oHtml+'</div>'+tag+'</div>';
      }
      html+='<div class="as-review"><div class="as-q-num">Question '+(qi+1)+' / '+AS.total+'</div><div class="as-q-text">'+qHtml+'</div><div class="as-opts">'+optsHtml+'</div></div>';
    }
    html+='<div class="as-actions"><button class="as-btn" id="as-back">← Back</button><button class="as-btn primary" id="as-retake">Retake</button></div>';
    html+='</div></div>';
    g('player-wrap').innerHTML=html;
    setStatus('assessment · submitted','status ok');
    on('as-back',function(){toggleSections();});
    on('as-retake',function(){playAssessment(AS.titleId,AS.unitId);});
  }catch(e){
    console.error('renderAssessmentReview error',e);
    g('player-wrap').innerHTML='<div class="as-err">review error: '+esc(e.message||e)+'</div>';
  }
}
/* ================= end assessment ================= */

function playPdf(titleId,unitId){
  document.getElementById('player-wrap').innerHTML='<div class="player-empty">loading PDF…</div>';
  fetch('/api/pdf/'+encodeURIComponent(titleId)+'/'+encodeURIComponent(unitId)).then(function(r){return r.json();}).then(function(info){
    if(info.error){document.getElementById('player-wrap').innerHTML='<div class="player-empty"><p>PDF error: '+esc(info.error)+'</p></div>';return;}
    window._pdfInfo=info;
    document.getElementById('player-wrap').innerHTML='<div class="pdf-viewer"><div class="pdf-toolbar"><span class="name">📄 '+esc(info.display||info.filename)+'</span><div class="pdf-actions"><a href="'+esc(info.redirectUrl)+'" download="'+esc(info.filename)+'" target="_blank" class="primary">⬇ download</a><button onclick="pdfCopyUrl(this)">🔗 copy</button><button onclick="pdfNewTab()">↗ new tab</button></div></div><iframe class="pdf-frame" src="'+esc(info.redirectUrl)+'"></iframe></div>';
    document.getElementById('status').textContent='pdf';document.getElementById('status').className='status ok';
  });
}
window.pdfNewTab=function(){if(window._pdfInfo&&window._pdfInfo.redirectUrl)window.open(window._pdfInfo.redirectUrl,'_blank');};
window.pdfCopyUrl=function(btn){var item=FLAT[CURRENT];fetch('/api/pdf/'+encodeURIComponent(ACTIVE)+'/'+encodeURIComponent(item.unit.id)).then(function(r){return r.json();}).then(function(info){if(info.redirectUrl){navigator.clipboard.writeText(info.redirectUrl);var o=btn.textContent;btn.textContent='✓';setTimeout(function(){btn.textContent=o;},1200);}});};

window.togglePlay=function(){
  if(!VIDEO)return;
  if(VIDEO.paused||VIDEO.ended){var p=VIDEO.play();if(p&&p.catch)p.catch(function(){});}
  else VIDEO.pause();
};
window.toggleMute=function(){if(VIDEO){VIDEO.muted=!VIDEO.muted;if(!VIDEO.muted&&VIDEO.volume===0)VIDEO.volume=VOL||1;}};
window.playNext=function(){if(CURRENT!=null&&CURRENT<FLAT.length-1)playUnit(CURRENT+1);};
window.playPrev=function(){if(CURRENT!=null&&CURRENT>0)playUnit(CURRENT-1);};

function fsEl(){return document.fullscreenElement||document.webkitFullscreenElement;}
function leaveFS(){
  if(fsEl()){
    if(document.exitFullscreen)document.exitFullscreen();
    else if(document.webkitExitFullscreen)document.webkitExitFullscreen();
  }
}
window.toggleFS=function(){
  var w=document.getElementById('player-wrap');
  if(!fsEl()){
    var p=null;
    if(w.requestFullscreen)p=w.requestFullscreen();
    else if(w.webkitRequestFullscreen)p=w.webkitRequestFullscreen();
    else if(w.msRequestFullscreen)p=w.msRequestFullscreen();
    else if(VIDEO&&VIDEO.webkitEnterFullscreen){VIDEO.webkitEnterFullscreen();return;}
    if(p&&p.then){
      p.then(function(){
        try{if(window.innerWidth<=900&&screen.orientation&&screen.orientation.lock){screen.orientation.lock('landscape').catch(function(){});}}catch(e){}
      }).catch(function(){});
    }
  }else{
    leaveFS();
  }
};
function onFsChange(){
  var b=g('yt-fs');if(b)b.innerHTML=ic(fsEl()?'exitfs':'fs');
  if(!fsEl()){try{if(screen.orientation&&screen.orientation.unlock)screen.orientation.unlock();}catch(e){}}
}
document.addEventListener('fullscreenchange',onFsChange);
document.addEventListener('webkitfullscreenchange',onFsChange);

window.openDownload=function(){
  if(!CURRENT_INFO)return;
  if(CURRENT_INFO.type==='pdf'){var a=document.querySelector('.pdf-actions a.primary');if(a)a.click();return;}
  if(CURRENT_INFO.type==='assessment'){alert('assessment has no download');return;}
  var box=document.getElementById('dl-variants');box.innerHTML='';
  var items=Object.entries(CURRENT_VARIANTS).sort(function(a,b){return parseInt(b[0])-parseInt(a[0]);});
  if(!items.length){box.innerHTML='<p style="color:var(--muted)">no variants</p>';document.getElementById('modal-dl').classList.add('open');return;}
  for(var i=0;i<items.length;i++){
    var q=items[i][0],url=items[i][1];
    var el=document.createElement('div');el.className='variant';
    el.innerHTML='<div style="display:flex;justify-content:space-between;align-items:center;gap:10px"><span class="name">'+esc(q)+'</span><button data-url="'+esc(url)+'" data-q="'+esc(q)+'" class="dlbtn">download</button></div>';
    box.appendChild(el);
  }
  var btns=box.querySelectorAll('.dlbtn');
  for(var j=0;j<btns.length;j++){(function(b){b.onclick=function(){browserHlsDownload(b.dataset.url,(CURRENT_INFO.title||'video'),b.dataset.q);};})(btns[j]);}
  document.getElementById('modal-dl').classList.add('open');
};
function browserHlsDownload(masterUrl,title,quality){
  closeModal('modal-dl');
  var status=document.getElementById('status');status.textContent='download starting…';
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
  document.getElementById('link-master').value=master;
  var box=document.getElementById('link-variants');box.innerHTML='<p style="color:var(--muted);font-size:12px">loading…</p>';
  fetch('/api/variants/'+encodeURIComponent(CURRENT_INFO.sourceid)).then(function(r){return r.json();}).then(function(j){
    CURRENT_VARIANTS=(j&&j.variants)||{};
    var items=Object.entries(CURRENT_VARIANTS).sort(function(a,b){return parseInt(b[0])-parseInt(a[0]);});
    if(!items.length){box.innerHTML='<p style="color:var(--muted);font-size:12px">no variants</p>';}
    else{box.innerHTML='';for(var i=0;i<items.length;i++){var q=items[i][0],url=items[i][1];var el=document.createElement('div');el.className='variant';el.innerHTML='<div style="display:flex;justify-content:space-between;align-items:center;gap:10px;margin-bottom:8px"><span class="name">'+esc(q)+'</span><button data-url="'+esc(url)+'" class="copybtn">copy</button></div><input value="'+esc(url)+'" readonly onclick="this.select()" style="font:11px monospace">';box.appendChild(el);}
      var btns=box.querySelectorAll('.copybtn');for(var j=0;j<btns.length;j++){(function(b){b.onclick=function(){copyText(b.dataset.url,b);};})(btns[j]);}}
    document.getElementById('modal-link').classList.add('open');
  });
};
function copyText(t,btn){navigator.clipboard.writeText(t).then(function(){var o=btn.textContent;btn.textContent='✓';setTimeout(function(){btn.textContent=o;},1200);}).catch(function(){var ta=document.createElement('textarea');ta.value=t;document.body.appendChild(ta);ta.select();document.execCommand('copy');document.body.removeChild(ta);var o=btn.textContent;btn.textContent='✓';setTimeout(function(){btn.textContent=o;},1200);});}
window.closeModal=function(id){document.getElementById(id).classList.remove('open');};
window.copyField=function(id,btn){var el=document.getElementById(id);el.select();el.setSelectionRange(0,99999);navigator.clipboard.writeText(el.value).then(function(){var o=btn.textContent;btn.textContent='copied!';setTimeout(function(){btn.textContent=o;},1200);});};
window.copyUpi=function(btn){var id=document.getElementById('upi-id').textContent.trim();navigator.clipboard.writeText(id).then(function(){var o=btn.textContent;btn.textContent='✓ copied';setTimeout(function(){btn.textContent=o;},1200);});};
var modals=document.querySelectorAll('.modal');for(var mi=0;mi<modals.length;mi++){(function(m){m.addEventListener('click',function(e){if(e.target===m)m.classList.remove('open');});})(modals[mi]);}
document.addEventListener('keydown',function(e){
  if(e.target.tagName==='INPUT'||e.target.tagName==='SELECT'||e.target.tagName==='TEXTAREA')return;
  var k=e.key;
  if(k==='/'){e.preventDefault();if(document.getElementById('page-viewer').classList.contains('active'))document.getElementById('search').focus();else document.getElementById('batch-search').focus();return;}
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
  else if(k==='Escape'&&document.getElementById('sections-overlay').classList.contains('open')){document.getElementById('sections-overlay').classList.remove('open');}
});
document.getElementById('search').addEventListener('input',renderTOC);
document.getElementById('batch-search').addEventListener('input',renderBatches);
function loadAll(){
  var grid=document.getElementById('batch-grid');
  grid.innerHTML='<div style="padding:24px;color:var(--muted);text-align:center;grid-column:1/-1">loading…</div>';
  fetch('/api/batches').then(function(r){return r.json();}).then(function(j){
    BATCHES=(j&&j.batches)||[];renderBatches();
  }).catch(function(e){grid.innerHTML='<div style="padding:24px;color:#ff7a7a;text-align:center;grid-column:1/-1">error: '+esc(e.message||e)+'</div>';});
}
if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',loadAll);}else{loadAll();}
})();
"""
