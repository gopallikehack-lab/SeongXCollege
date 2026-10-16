"""SEONG AI — floating widget markup + logic + voice input."""

CHATBOT_HTML = r"""
<!-- SEONG AI floating chat -->
<div id="sa-launcher" class="sa-launcher" title="SEONG AI">
  <img src="https://i.8upload.com/thumbnail/d252db6ffe117d55/6240190351691944107-120.jpg" alt="SEONG AI">
  <span class="sa-dot"></span>
</div>

<div id="sa-panel" class="sa-panel">
  <div class="sa-head">
    <img class="sa-ava" src="https://i.8upload.com/thumbnail/d252db6ffe117d55/6240190351691944107-120.jpg" alt="">
    <div class="sa-head-info">
      <div class="sa-title">SEONG AI</div>
      <div class="sa-sub">SeongEraStudy Platform · Share Your Doubt!</div>
    </div>
    <button class="sa-close" onclick="saClose()" title="Close">×</button>
  </div>

  <div class="sa-models" id="sa-models"></div>

  <div class="sa-body" id="sa-body">
    <div class="sa-msg sa-bot">
      <div class="sa-bubble">Hi 👋 I'm <b>SEONG AI</b>, the SeongEraStudy assistant.<br>Ask me anything — coding, DSA, math, aptitude. Share your doubt!</div>
    </div>
  </div>

  <div class="sa-foot">
    <button id="sa-mic" class="sa-mic" title="Voice input" onclick="saVoice()">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>
    </button>
    <textarea id="sa-input" class="sa-input" rows="1" placeholder="Ask your doubt…"></textarea>
    <button id="sa-send" class="sa-send" title="Send" onclick="saSend()">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 2 11 13"/><path d="M22 2l-7 20-4-9-9-4z"/></svg>
    </button>
  </div>
</div>

<style>
.sa-launcher{position:fixed;left:20px;bottom:20px;width:62px;height:62px;border-radius:50%;cursor:grab;z-index:9000;background:#0e1218;border:2px solid rgba(92,141,255,.55);box-shadow:0 14px 40px rgba(0,0,0,.55),0 0 0 0 rgba(92,141,255,.35);display:flex;align-items:center;justify-content:center;overflow:visible;animation:sa-pulse 2.6s ease-in-out infinite;user-select:none;touch-action:none}
.sa-launcher.dragging{cursor:grabbing;animation:none}
.sa-launcher img{width:100%;height:100%;border-radius:50%;object-fit:cover;pointer-events:none;display:block;background:#000}
.sa-launcher .sa-dot{position:absolute;right:2px;top:2px;width:13px;height:13px;border-radius:50%;background:#2ecc71;border:2px solid #0e1218;box-shadow:0 0 8px #2ecc71}
@keyframes sa-pulse{0%,100%{box-shadow:0 14px 40px rgba(0,0,0,.55),0 0 0 0 rgba(92,141,255,.35)}50%{box-shadow:0 14px 40px rgba(0,0,0,.55),0 0 0 14px rgba(92,141,255,0)}}

.sa-panel{position:fixed;left:20px;bottom:94px;width:min(400px,92vw);height:min(600px,76vh);z-index:9001;background:var(--panel);border:1px solid var(--line);border-radius:20px;overflow:hidden;display:none;flex-direction:column;box-shadow:0 30px 80px rgba(0,0,0,.65);animation:sa-in .22s cubic-bezier(.22,.9,.28,1)}
.sa-panel.open{display:flex}
@keyframes sa-in{from{opacity:0;transform:translateY(10px) scale(.97)}to{opacity:1;transform:translateY(0) scale(1)}}
.sa-head{display:flex;align-items:center;gap:12px;padding:13px 14px;background:linear-gradient(135deg,rgba(92,141,255,.16),rgba(124,92,255,.06) 60%,transparent);border-bottom:1px solid var(--line);flex-shrink:0}
.sa-ava{width:44px;height:44px;border-radius:50%;object-fit:cover;border:2px solid rgba(92,141,255,.5);background:#000;flex-shrink:0;display:block}
.sa-head-info{flex:1;min-width:0}
.sa-title{font-size:15px;font-weight:800;letter-spacing:.3px;background:linear-gradient(90deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.sa-sub{font-size:10.5px;color:var(--muted);margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-weight:600}
.sa-close{background:transparent;border:1px solid var(--line);color:var(--muted);width:34px;height:34px;border-radius:9px;cursor:pointer;font-size:20px;line-height:1;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0}
.sa-close:hover{color:var(--accent);border-color:var(--accent)}

.sa-models{display:flex;gap:6px;padding:8px 10px;background:var(--panel);border-bottom:1px solid var(--line);overflow-x:auto;flex-shrink:0;scrollbar-width:none}
.sa-models::-webkit-scrollbar{display:none}
.sa-model{padding:6px 11px;border-radius:8px;background:var(--panel2);border:1px solid var(--line);color:var(--txt);font-size:11px;font-weight:600;cursor:pointer;white-space:nowrap;flex-shrink:0;display:inline-flex;align-items:center;gap:5px;transition:all .15s}
.sa-model:hover{border-color:var(--accent)}
.sa-model.sel{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border-color:transparent}
.sa-model .sa-tag{font-size:8.5px;opacity:.7;font-weight:700;letter-spacing:.3px}

.sa-body{flex:1;overflow-y:auto;padding:16px 14px;display:flex;flex-direction:column;gap:12px;background:var(--bg)}
.sa-msg{display:flex;flex-direction:column;max-width:88%}
.sa-msg.sa-user{align-self:flex-end;align-items:flex-end}
.sa-msg.sa-bot{align-self:flex-start;align-items:flex-start}
.sa-bubble{padding:11px 14px;border-radius:14px;font-size:13.5px;line-height:1.65;white-space:pre-wrap;word-wrap:break-word;overflow-wrap:anywhere}
.sa-bot .sa-bubble{background:var(--panel2);color:var(--txt);border:1px solid var(--line);border-bottom-left-radius:5px}
.sa-user .sa-bubble{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border-bottom-right-radius:5px}
.sa-bubble b{font-weight:700}
.sa-bubble code{background:rgba(0,0,0,.35);padding:2px 6px;border-radius:5px;font:12px monospace}
.sa-model-tag{font-size:9.5px;color:var(--muted);margin-top:4px;text-transform:uppercase;letter-spacing:.6px;font-weight:700}
.sa-typing{display:inline-flex;gap:4px;align-items:center;padding:11px 14px}
.sa-typing i{width:6px;height:6px;border-radius:50%;background:var(--muted);display:inline-block;animation:sa-bnc 1.2s ease-in-out infinite}
.sa-typing i:nth-child(2){animation-delay:.15s}
.sa-typing i:nth-child(3){animation-delay:.3s}
@keyframes sa-bnc{0%,80%,100%{opacity:.35;transform:translateY(0)}40%{opacity:1;transform:translateY(-4px)}}
.sa-err{align-self:flex-start;max-width:88%;padding:10px 12px;background:rgba(255,92,92,.1);border:1px solid rgba(255,92,92,.25);border-radius:10px;color:#ff8b8b;font-size:12px;font-family:monospace;white-space:pre-wrap;word-break:break-word}

.sa-foot{display:flex;gap:8px;padding:10px 12px;border-top:1px solid var(--line);background:var(--panel);flex-shrink:0;align-items:flex-end}
.sa-mic{width:46px;height:46px;flex-shrink:0;border:1px solid var(--line);background:var(--panel2);color:var(--txt);border-radius:11px;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;transition:all .15s}
.sa-mic:hover{border-color:var(--accent);color:var(--accent)}
.sa-mic.rec{background:linear-gradient(135deg,#ff5c5c,#b35cff);color:#fff;border-color:transparent;animation:sa-rec 1s ease-in-out infinite}
@keyframes sa-rec{0%,100%{box-shadow:0 0 0 0 rgba(255,92,92,.5)}50%{box-shadow:0 0 0 10px rgba(255,92,92,0)}}
.sa-mic svg{width:20px;height:20px}
.sa-input{flex:1;resize:none;padding:11px 13px;background:var(--bg);border:1px solid var(--line);color:var(--txt);font:inherit;font-size:13.5px;border-radius:11px;outline:none;max-height:120px;min-height:44px;line-height:1.4}
.sa-input:focus{border-color:var(--accent)}
.sa-send{width:46px;height:46px;flex-shrink:0;border:0;border-radius:11px;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;transition:filter .15s}
.sa-send:hover{filter:brightness(1.1)}
.sa-send:disabled{opacity:.5;cursor:not-allowed}
.sa-send svg{width:20px;height:20px}
@media (max-width:520px){
  .sa-launcher{left:14px;bottom:14px;width:58px;height:58px}
  .sa-panel{left:8px;right:8px;bottom:82px;width:auto;height:min(620px,78vh)}
}
</style>

<script>
(function(){
  var launcher = document.getElementById('sa-launcher');
  var panel = document.getElementById('sa-panel');
  var body = document.getElementById('sa-body');
  var input = document.getElementById('sa-input');
  var sendBtn = document.getElementById('sa-send');
  var micBtn = document.getElementById('sa-mic');
  var modelsBar = document.getElementById('sa-models');
  var history = [];
  var busy = false;
  var curModel = null;
  var MODELS = [];
  var DEF = null;

  /* ---------- drag ---------- */
  var drag = {active:false, moved:false, sx:0, sy:0, ox:0, oy:0, ptr:null};
  var POS_KEY = 'sa_launcher_pos';
  function applyPos(p){ if(!p)return; launcher.style.left=p.x+'px'; launcher.style.top=p.y+'px'; launcher.style.bottom='auto'; launcher.style.right='auto'; }
  function savePos(p){ try{localStorage.setItem(POS_KEY, JSON.stringify(p));}catch(e){} }
  function loadPos(){ try{var s=localStorage.getItem(POS_KEY); return s?JSON.parse(s):null;}catch(e){return null;} }
  function clamp(x,y){ var w=launcher.offsetWidth||62, h=launcher.offsetHeight||62; return {x:Math.max(0,Math.min(window.innerWidth-w,x)), y:Math.max(0,Math.min(window.innerHeight-h,y))}; }
  var saved=loadPos(); if(saved){ var c=clamp(saved.x,saved.y); applyPos(c); }

  launcher.addEventListener('pointerdown', function(e){
    if(e.button!==undefined && e.button!==0) return;
    drag.active=true; drag.moved=false;
    drag.sx=e.clientX; drag.sy=e.clientY;
    var r=launcher.getBoundingClientRect();
    drag.ox=e.clientX-r.left; drag.oy=e.clientY-r.top;
    launcher.classList.add('dragging');
    try{launcher.setPointerCapture(e.pointerId);}catch(x){}
    drag.ptr=e.pointerId; e.preventDefault();
  });
  launcher.addEventListener('pointermove', function(e){
    if(!drag.active) return;
    var dx=e.clientX-drag.sx, dy=e.clientY-drag.sy;
    if(Math.abs(dx)>4||Math.abs(dy)>4) drag.moved=true;
    if(!drag.moved) return;
    var p=clamp(e.clientX-drag.ox, e.clientY-drag.oy);
    applyPos(p);
  });
  function endDrag(e){
    if(!drag.active) return;
    drag.active=false;
    launcher.classList.remove('dragging');
    try{launcher.releasePointerCapture(drag.ptr);}catch(x){}
    var r=launcher.getBoundingClientRect();
    savePos({x:r.left, y:r.top});
    if(!drag.moved){ saToggle(); }
  }
  launcher.addEventListener('pointerup', endDrag);
  launcher.addEventListener('pointercancel', endDrag);
  window.addEventListener('resize', function(){ var r=launcher.getBoundingClientRect(); var c=clamp(r.left,r.top); applyPos(c); savePos(c); });

  /* ---------- open/close ---------- */
  window.saClose = function(){ panel.classList.remove('open'); };
  function saToggle(){ panel.classList.toggle('open'); if(panel.classList.contains('open')) setTimeout(function(){input.focus();}, 60); }
  window.saToggle = saToggle;

  /* ---------- models bar ---------- */
  function renderModels(){
    modelsBar.innerHTML = MODELS.map(function(m){
      var cls = 'sa-model' + (m.id===curModel ? ' sel' : '');
      return '<div class="'+cls+'" data-id="'+m.id+'">'+m.name+' <span class="sa-tag">'+m.tag+'</span></div>';
    }).join('');
    modelsBar.querySelectorAll('.sa-model').forEach(function(el){
      el.addEventListener('click', function(){
        curModel = el.dataset.id;
        renderModels();
      });
    });
  }
  function loadModels(){
    fetch('/api/chat/models').then(function(r){return r.json();}).then(function(j){
      MODELS = j.models || [];
      DEF = j.default || (MODELS[0] && MODELS[0].id);
      curModel = DEF;
      renderModels();
    }).catch(function(){ MODELS = []; });
  }

  /* ---------- voice input (Web Speech API) ---------- */
  var recog = null;
  var recording = false;
  function hasSpeech(){ return ('webkitSpeechRecognition' in window) || ('SpeechRecognition' in window); }
  function setupRecog(){
    if(!hasSpeech()) return null;
    var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    var r = new SR();
    r.continuous = false;
    r.interimResults = true;
    r.lang = 'en-IN';
    r.onresult = function(e){
      var txt = '';
      for(var i=e.resultIndex; i<e.results.length; i++){
        txt += e.results[i][0].transcript;
      }
      input.value = txt;
      input.style.height='auto';
      input.style.height = Math.min(120, input.scrollHeight) + 'px';
    };
    r.onend = function(){ recording=false; micBtn.classList.remove('rec'); };
    r.onerror = function(e){ recording=false; micBtn.classList.remove('rec'); };
    return r;
  }
  if(hasSpeech()){
    recog = setupRecog();
  } else {
    micBtn.style.display = 'none';
  }
  window.saVoice = function(){
    if(!recog){ alert('Voice input not supported on this browser'); return; }
    if(recording){ try{recog.stop();}catch(e){} recording=false; micBtn.classList.remove('rec'); return; }
    try{ recog.start(); recording=true; micBtn.classList.add('rec'); }catch(e){ recording=false; micBtn.classList.remove('rec'); }
  };

  /* ---------- chat ---------- */
  function esc(s){ return String(s==null?'':s).replace(/[&<>]/g, function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c];}); }
  function addMsg(role, text, model){
    var wrap = document.createElement('div');
    wrap.className = 'sa-msg sa-' + (role==='user' ? 'user' : 'bot');
    var bubble = document.createElement('div');
    bubble.className = 'sa-bubble';
    bubble.innerHTML = esc(text).replace(/\n/g,'<br>');
    wrap.appendChild(bubble);
    if(model){
      var mt = document.createElement('div');
      mt.className = 'sa-model-tag';
      mt.textContent = 'via ' + model;
      wrap.appendChild(mt);
    }
    body.appendChild(wrap);
    body.scrollTop = body.scrollHeight;
    return wrap;
  }
  function addTyping(){
    var wrap = document.createElement('div');
    wrap.className = 'sa-msg sa-bot';
    wrap.innerHTML = '<div class="sa-bubble sa-typing"><i></i><i></i><i></i></div>';
    body.appendChild(wrap);
    body.scrollTop = body.scrollHeight;
    return wrap;
  }
  function addError(text){
    var wrap = document.createElement('div');
    wrap.className = 'sa-err';
    wrap.textContent = '⚠️ ' + text;
    body.appendChild(wrap);
    body.scrollTop = body.scrollHeight;
  }

  window.saSend = function(){
    if(busy) return;
    var text = (input.value||'').trim();
    if(!text) return;
    addMsg('user', text);
    history.push({role:'user', content:text});
    input.value='';
    input.style.height='auto';
    busy = true; sendBtn.disabled = true;
    var t = addTyping();
    fetch('/api/chat', {
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body: JSON.stringify({messages: history, model: curModel}),
    })
    .then(function(r){ return r.json(); })
    .then(function(j){
      t.remove();
      if(j && j.ok){
        addMsg('bot', j.reply, j.model);
        history.push({role:'assistant', content:j.reply});
      } else {
        addError((j && j.error) || 'something went wrong');
      }
    })
    .catch(function(e){
      t.remove();
      addError('network: ' + (e.message||e));
    })
    .then(function(){
      busy = false; sendBtn.disabled = false; input.focus();
    });
  };

  input.addEventListener('keydown', function(e){
    if(e.key==='Enter' && !e.shiftKey){ e.preventDefault(); window.saSend(); }
  });
  input.addEventListener('input', function(){
    this.style.height='auto';
    this.style.height = Math.min(120, this.scrollHeight) + 'px';
  });

  loadModels();
})();
</script>
"""
