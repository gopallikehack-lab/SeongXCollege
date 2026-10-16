"""SEONG AI — floating widget markup + logic + voice input."""

CHATBOT_HTML = r"""
<!-- SEONG AI floating chat -->
<div id="sa-launcher" class="sa-launcher" title="SEONG AI">
  <img src="https://i.8upload.com/thumbnail/d252db6ffe117d55/6240190351691944107-120.jpg" alt="SEONG AI">
  <span class="sa-dot"></span>
</div>

<div id="sa-toast" class="sa-toast">
  <div class="sa-toast-text">Heyy 👋 Can I help you?</div>
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

  <div class="sa-voice-hint" id="sa-voice-hint">
    <span>🎤</span>
    <span>Listening… speak now</span>
  </div>

  <div class="sa-foot">
    <button id="sa-mic" class="sa-mic" title="Voice input">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>
    </button>
    <textarea id="sa-input" class="sa-input" rows="1" placeholder="Ask your doubt…"></textarea>
    <button id="sa-send" class="sa-send" title="Send">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 2 11 13"/><path d="M22 2l-7 20-4-9-9-4z"/></svg>
    </button>
  </div>
</div>

<style>
/* ===== launcher ===== */
.sa-launcher{position:fixed;left:22px;bottom:22px;width:78px;height:78px;border-radius:50%;cursor:grab;z-index:9000;background:#0e1218;border:3px solid rgba(92,141,255,.6);box-shadow:0 16px 46px rgba(0,0,0,.6),0 0 0 0 rgba(92,141,255,.35);display:flex;align-items:center;justify-content:center;overflow:visible;animation:sa-pulse 2.6s ease-in-out infinite;user-select:none;touch-action:none}
.sa-launcher.dragging{cursor:grabbing;animation:none}
.sa-launcher img{width:100%;height:100%;border-radius:50%;object-fit:cover;pointer-events:none;display:block;background:#000}
.sa-launcher .sa-dot{position:absolute;left:3px;bottom:3px;width:15px;height:15px;border-radius:50%;background:#2ecc71;border:2px solid #0e1218;box-shadow:0 0 10px #2ecc71}
@keyframes sa-pulse{0%,100%{box-shadow:0 16px 46px rgba(0,0,0,.6),0 0 0 0 rgba(92,141,255,.4)}50%{box-shadow:0 16px 46px rgba(0,0,0,.6),0 0 0 18px rgba(92,141,255,0)}}

/* ===== greeting toast ===== */
.sa-toast{position:fixed;left:110px;bottom:44px;z-index:8999;padding:11px 16px;background:linear-gradient(135deg,rgba(92,141,255,.18),rgba(124,92,255,.1));border:1px solid rgba(92,141,255,.35);border-radius:14px;color:var(--txt);font-size:13.5px;font-weight:600;backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);box-shadow:0 14px 40px rgba(0,0,0,.55);opacity:0;transform:translateX(-10px) scale(.95);pointer-events:none;transition:opacity .35s cubic-bezier(.22,.9,.28,1),transform .35s cubic-bezier(.22,.9,.28,1);white-space:nowrap;max-width:calc(100vw - 140px);overflow:hidden;text-overflow:ellipsis}
.sa-toast.show{opacity:1;transform:translateX(0) scale(1)}
.sa-toast::after{content:"";position:absolute;left:-8px;bottom:14px;width:0;height:0;border:8px solid transparent;border-right-color:rgba(92,141,255,.35);border-left:0}
.sa-toast-text{background:linear-gradient(90deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
@media (max-width:520px){
  .sa-toast{left:96px;bottom:34px;font-size:12.5px;padding:10px 14px;max-width:calc(100vw - 120px)}
}

/* ===== panel ===== */
.sa-panel{position:fixed;left:22px;bottom:112px;width:min(410px,92vw);height:min(620px,78vh);z-index:9001;background:var(--panel);border:1px solid var(--line);border-radius:20px;overflow:hidden;display:none;flex-direction:column;box-shadow:0 30px 80px rgba(0,0,0,.7);animation:sa-in .22s cubic-bezier(.22,.9,.28,1)}
.sa-panel.open{display:flex}
@keyframes sa-in{from{opacity:0;transform:translateY(10px) scale(.97)}to{opacity:1;transform:translateY(0) scale(1)}}
.sa-head{display:flex;align-items:center;gap:12px;padding:14px;background:linear-gradient(135deg,rgba(92,141,255,.18),rgba(124,92,255,.06) 60%,transparent);border-bottom:1px solid var(--line);flex-shrink:0}
.sa-ava{width:50px;height:50px;border-radius:50%;object-fit:cover;border:2px solid rgba(92,141,255,.5);background:#000;flex-shrink:0;display:block}
.sa-head-info{flex:1;min-width:0}
.sa-title{font-size:16px;font-weight:800;letter-spacing:.3px;background:linear-gradient(90deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.sa-sub{font-size:10.5px;color:var(--muted);margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-weight:600}
.sa-close{background:transparent;border:1px solid var(--line);color:var(--muted);width:36px;height:36px;border-radius:10px;cursor:pointer;font-size:20px;line-height:1;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0}
.sa-close:hover{color:var(--accent);border-color:var(--accent)}

/* ===== model strip ===== */
.sa-models{display:flex;gap:6px;padding:9px 10px;background:var(--panel);border-bottom:1px solid var(--line);overflow-x:auto;flex-shrink:0;scrollbar-width:none}
.sa-models::-webkit-scrollbar{display:none}
.sa-model{padding:7px 12px;border-radius:9px;background:var(--panel2);border:1px solid var(--line);color:var(--txt);font-size:11.5px;font-weight:600;cursor:pointer;white-space:nowrap;flex-shrink:0;display:inline-flex;align-items:center;gap:5px;transition:all .15s}
.sa-model:hover{border-color:var(--accent)}
.sa-model.sel{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border-color:transparent}
.sa-model .sa-tag{font-size:8.5px;opacity:.75;font-weight:700;letter-spacing:.3px}

/* ===== body ===== */
.sa-body{flex:1;overflow-y:auto;padding:16px 14px;display:flex;flex-direction:column;gap:12px;background:var(--bg)}
.sa-msg{display:flex;flex-direction:column;max-width:88%}
.sa-msg.sa-user{align-self:flex-end;align-items:flex-end}
.sa-msg.sa-bot{align-self:flex-start;align-items:flex-start}
.sa-bubble{padding:11px 14px;border-radius:14px;font-size:13.5px;line-height:1.7;white-space:pre-wrap;word-wrap:break-word;overflow-wrap:anywhere}
.sa-bot .sa-bubble{background:var(--panel2);color:var(--txt);border:1px solid var(--line);border-bottom-left-radius:5px}
.sa-user .sa-bubble{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border-bottom-right-radius:5px}
.sa-bubble b{font-weight:800;color:#fff}
.sa-bubble i{font-style:italic;opacity:.95}
.sa-bubble code{background:rgba(0,0,0,.45);padding:2px 6px;border-radius:5px;font:12px monospace;color:#8fd0ff}
.sa-bubble pre{background:rgba(0,0,0,.5);padding:10px 12px;border-radius:8px;margin:8px 0;overflow-x:auto;font:12px/1.5 monospace;color:#c9e4ff;border:1px solid rgba(255,255,255,.06)}
.sa-bubble pre code{background:none;padding:0;color:inherit}
.sa-bubble ul{margin:6px 0;padding-left:20px}
.sa-bubble li{margin:3px 0}
.sa-model-tag{font-size:9.5px;color:var(--muted);margin-top:5px;text-transform:uppercase;letter-spacing:.6px;font-weight:700}
.sa-typing{display:inline-flex;gap:4px;align-items:center;padding:11px 14px}
.sa-typing i{width:6px;height:6px;border-radius:50%;background:var(--muted);display:inline-block;animation:sa-bnc 1.2s ease-in-out infinite}
.sa-typing i:nth-child(2){animation-delay:.15s}
.sa-typing i:nth-child(3){animation-delay:.3s}
@keyframes sa-bnc{0%,80%,100%{opacity:.35;transform:translateY(0)}40%{opacity:1;transform:translateY(-4px)}}
.sa-err{align-self:flex-start;max-width:88%;padding:10px 12px;background:rgba(255,92,92,.1);border:1px solid rgba(255,92,92,.25);border-radius:10px;color:#ff8b8b;font-size:12px;font-family:monospace;white-space:pre-wrap;word-break:break-word}

/* ===== voice hint ===== */
.sa-voice-hint{display:none;align-items:center;justify-content:center;gap:8px;padding:10px 14px;background:linear-gradient(135deg,rgba(255,92,92,.14),rgba(179,92,255,.1));border-top:1px solid rgba(255,92,92,.3);color:#ffb0b0;font-size:12.5px;font-weight:600;flex-shrink:0;animation:sa-in .2s}
.sa-voice-hint.on{display:flex}
.sa-voice-hint span:first-child{font-size:16px;animation:sa-mic-pulse 1.1s ease-in-out infinite}
@keyframes sa-mic-pulse{0%,100%{transform:scale(1);opacity:.85}50%{transform:scale(1.22);opacity:1}}

/* ===== foot ===== */
.sa-foot{display:flex;gap:8px;padding:10px 12px;border-top:1px solid var(--line);background:var(--panel);flex-shrink:0;align-items:flex-end}
.sa-mic{width:48px;height:48px;flex-shrink:0;border:1px solid var(--line);background:var(--panel2);color:var(--txt);border-radius:12px;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;transition:all .15s}
.sa-mic:hover{border-color:var(--accent);color:var(--accent)}
.sa-mic.rec{background:linear-gradient(135deg,#ff5c5c,#b35cff);color:#fff;border-color:transparent;animation:sa-rec 1.1s ease-in-out infinite}
@keyframes sa-rec{0%,100%{box-shadow:0 0 0 0 rgba(255,92,92,.55)}50%{box-shadow:0 0 0 12px rgba(255,92,92,0)}}
.sa-mic svg{width:22px;height:22px}
.sa-input{flex:1;resize:none;padding:12px 14px;background:var(--bg);border:1px solid var(--line);color:var(--txt);font:inherit;font-size:13.5px;border-radius:12px;outline:none;max-height:120px;min-height:48px;line-height:1.45}
.sa-input:focus{border-color:var(--accent)}
.sa-send{width:48px;height:48px;flex-shrink:0;border:0;border-radius:12px;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;transition:filter .15s}
.sa-send:hover{filter:brightness(1.1)}
.sa-send:disabled{opacity:.5;cursor:not-allowed}
.sa-send svg{width:20px;height:20px}

@media (max-width:520px){
  .sa-launcher{left:16px;bottom:16px;width:70px;height:70px}
  .sa-panel{left:8px;right:8px;bottom:96px;width:auto;height:min(640px,80vh)}
}
</style>

<script>
(function(){
  var launcher = document.getElementById('sa-launcher');
  var panel    = document.getElementById('sa-panel');
  var body     = document.getElementById('sa-body');
  var input    = document.getElementById('sa-input');
  var sendBtn  = document.getElementById('sa-send');
  var micBtn   = document.getElementById('sa-mic');
  var modelsBar= document.getElementById('sa-models');
  var voiceHint= document.getElementById('sa-voice-hint');
  var toast    = document.getElementById('sa-toast');

  var history  = [];
  var busy     = false;
  var curModel = null;
  var MODELS   = [];
  var DEF      = null;

  /* ============ GREETING TOAST ============ */
  (function showGreeting(){
    // only once per session
    var KEY = 'sa_greet_shown';
    var done = false;
    try{ done = sessionStorage.getItem(KEY) === '1'; }catch(e){}
    if(done) return;
    try{ sessionStorage.setItem(KEY, '1'); }catch(e){}
    setTimeout(function(){
      toast.classList.add('show');
      setTimeout(function(){
        toast.classList.remove('show');
      }, 3600);   // visible for ~3.6s
    }, 900);      // 0.9s after page load
  })();

  /* ============ DRAG ============ */
  var drag = {active:false, moved:false, sx:0, sy:0, ox:0, oy:0, ptr:null};
  var POS_KEY = 'sa_launcher_pos';
  function applyPos(p){ if(!p)return; launcher.style.left=p.x+'px'; launcher.style.top=p.y+'px'; launcher.style.bottom='auto'; launcher.style.right='auto'; }
  function savePos(p){ try{localStorage.setItem(POS_KEY, JSON.stringify(p));}catch(e){} }
  function loadPos(){ try{var s=localStorage.getItem(POS_KEY); return s?JSON.parse(s):null;}catch(e){return null;} }
  function clampPos(x,y){ var w=launcher.offsetWidth||78, h=launcher.offsetHeight||78; return {x:Math.max(0,Math.min(window.innerWidth-w,x)), y:Math.max(0,Math.min(window.innerHeight-h,y))}; }
  var saved = loadPos(); if(saved){ var c=clampPos(saved.x,saved.y); applyPos(c); }

  launcher.addEventListener('pointerdown', function(e){
    if(e.button!==undefined && e.button!==0) return;
    drag.active=true; drag.moved=false;
    drag.sx=e.clientX; drag.sy=e.clientY;
    var r=launcher.getBoundingClientRect();
    drag.ox=e.clientX-r.left; drag.oy=e.clientY-r.top;
    launcher.classList.add('dragging');
    try{launcher.setPointerCapture(e.pointerId);}catch(x){}
    drag.ptr=e.pointerId;
  });
  launcher.addEventListener('pointermove', function(e){
    if(!drag.active) return;
    var dx=e.clientX-drag.sx, dy=e.clientY-drag.sy;
    if(Math.abs(dx)>4||Math.abs(dy)>4) drag.moved=true;
    if(!drag.moved) return;
    applyPos(clampPos(e.clientX-drag.ox, e.clientY-drag.oy));
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
  window.addEventListener('resize', function(){ var r=launcher.getBoundingClientRect(); var c=clampPos(r.left,r.top); applyPos(c); savePos(c); });

  /* ============ OPEN / CLOSE ============ */
  window.saClose = function(){ panel.classList.remove('open'); stopVoice(); };
  function saToggle(){
    // hide toast on open
    toast.classList.remove('show');
    panel.classList.toggle('open');
    if(panel.classList.contains('open')) setTimeout(function(){ input.focus(); }, 80);
  }
  window.saToggle = saToggle;

  /* ============ MODELS ============ */
  function renderModels(){
    modelsBar.innerHTML = MODELS.map(function(m){
      var cls = 'sa-model' + (m.id===curModel ? ' sel' : '');
      return '<div class="'+cls+'" data-id="'+m.id+'">'+m.name+' <span class="sa-tag">'+m.tag+'</span></div>';
    }).join('');
    modelsBar.querySelectorAll('.sa-model').forEach(function(el){
      el.addEventListener('click', function(){ curModel = el.dataset.id; renderModels(); });
    });
  }
  function loadModels(){
    fetch('/api/chat/models')
      .then(function(r){ return r.json(); })
      .then(function(j){
        MODELS = j.models || [];
        DEF = j.default || (MODELS[0] && MODELS[0].id);
        curModel = DEF;
        renderModels();
      })
      .catch(function(){ MODELS=[]; });
  }

  /* ============ MARKDOWN → HTML ============ */
  function escapeHtml(s){
    return String(s==null?'':s).replace(/[&<>]/g, function(c){
      return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c];
    });
  }
  function renderMarkdown(text){
    if(!text) return '';
    var s = escapeHtml(text);
    var blocks = [];
    s = s.replace(/```([\s\S]*?)```/g, function(_, code){
      var idx = blocks.length;
      blocks.push('<pre><code>' + code.trim() + '</code></pre>');
      return '\u0000CB' + idx + '\u0000';
    });
    s = s.replace(/`([^`\n]+?)`/g, function(_, c){ return '<code>' + c + '</code>'; });
    s = s.replace(/\*\*([^*\n]+?)\*\*/g, '<b>$1</b>');
    s = s.replace(/(^|[^*])\*([^*\n]+?)\*(?!\*)/g, '$1<i>$2</i>');
    s = s.replace(/^\s*[-*]\s+(.+)$/gm, '• $1');
    s = s.replace(/\n/g, '<br>');
    s = s.replace(/\u0000CB(\d+)\u0000/g, function(_, i){ return blocks[+i]; });
    return s;
  }

  function addMsg(role, text, model){
    var wrap = document.createElement('div');
    wrap.className = 'sa-msg sa-' + (role==='user' ? 'user' : 'bot');
    var bubble = document.createElement('div');
    bubble.className = 'sa-bubble';
    if(role==='user'){ bubble.textContent = text; }
    else{ bubble.innerHTML = renderMarkdown(text); }
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

  /* ============ SEND ============ */
  function doSend(){
    if(busy) return;
    var text = (input.value||'').trim();
    if(!text) return;
    stopVoice();
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
  }
  window.saSend = doSend;
  sendBtn.addEventListener('click', doSend);

  input.addEventListener('keydown', function(e){
    if(e.key==='Enter' && !e.shiftKey){ e.preventDefault(); doSend(); }
  });
  input.addEventListener('input', function(){
    this.style.height='auto';
    this.style.height = Math.min(120, this.scrollHeight) + 'px';
  });

  /* ============ VOICE INPUT ============ */
  var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  var recog = null;
  var recording = false;
  var baseText = '';

  function setRecUI(on){
    recording = on;
    if(on){ micBtn.classList.add('rec'); voiceHint.classList.add('on'); }
    else  { micBtn.classList.remove('rec'); voiceHint.classList.remove('on'); }
  }
  function buildRecognizer(){
    if(!SR) return null;
    var r = new SR();
    r.continuous = true;
    r.interimResults = true;
    r.lang = 'en-IN';
    r.maxAlternatives = 1;

    r.onstart = function(){ setRecUI(true); };
    r.onresult = function(e){
      var finalTxt = '';
      var interimTxt = '';
      for(var i=e.resultIndex; i<e.results.length; i++){
        var res = e.results[i];
        if(res.isFinal) finalTxt += res[0].transcript;
        else interimTxt += res[0].transcript;
      }
      var combined = (baseText + ' ' + finalTxt + ' ' + interimTxt).replace(/\s+/g,' ').trim();
      input.value = combined;
      input.style.height='auto';
      input.style.height = Math.min(120, input.scrollHeight) + 'px';
      body.scrollTop = body.scrollHeight;
    };
    r.onerror = function(e){
      setRecUI(false);
      if(e.error === 'not-allowed' || e.error === 'service-not-allowed'){
        addError('microphone permission denied');
      } else if(e.error === 'no-speech' || e.error === 'aborted'){
        // silent
      } else {
        addError('voice: ' + e.error);
      }
    };
    r.onend = function(){ setRecUI(false); input.focus(); };
    return r;
  }
  function startVoice(){
    if(!SR){ addError('voice input not supported on this browser — try Chrome / Edge / Kiwi'); return; }
    if(recording) return;
    recog = buildRecognizer();
    baseText = input.value.trim();
    try{ recog.start(); }
    catch(e){ setRecUI(false); addError('could not start microphone: ' + (e.message||e)); }
  }
  function stopVoice(){
    if(!recog || !recording) return;
    try{ recog.stop(); }catch(e){}
    setRecUI(false);
  }
  function toggleVoice(){ if(recording) stopVoice(); else startVoice(); }

  if(SR){ micBtn.addEventListener('click', toggleVoice); }
  else{ micBtn.style.display = 'none'; }

  /* ============ INIT ============ */
  loadModels();
})();
</script>
"""
