"""SEONG AI — floating chat widget markup + logic, injected into MAIN_PAGE."""

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

  <div class="sa-body" id="sa-body">
    <div class="sa-msg sa-bot">
      <div class="sa-bubble">Hi 👋 I'm <b>SEONG AI</b>, the SeongEraStudy assistant.<br>Ask me anything — coding, DSA, math, aptitude. Share your doubt!</div>
    </div>
  </div>

  <div class="sa-foot">
    <textarea id="sa-input" class="sa-input" rows="1" placeholder="Ask your doubt…"></textarea>
    <button id="sa-send" class="sa-send" title="Send" onclick="saSend()">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 2 11 13"/><path d="M22 2l-7 20-4-9-9-4z"/></svg>
    </button>
  </div>
</div>

<style>
.sa-launcher{position:fixed;left:20px;bottom:20px;width:60px;height:60px;border-radius:50%;cursor:grab;z-index:9000;background:#0e1218;border:2px solid rgba(92,141,255,.55);box-shadow:0 14px 40px rgba(0,0,0,.55),0 0 0 0 rgba(92,141,255,.35);display:flex;align-items:center;justify-content:center;overflow:visible;animation:sa-pulse 2.6s ease-in-out infinite;user-select:none;touch-action:none}
.sa-launcher.dragging{cursor:grabbing;animation:none}
.sa-launcher img{width:100%;height:100%;border-radius:50%;object-fit:cover;pointer-events:none;display:block;background:#000}
.sa-launcher .sa-dot{position:absolute;right:2px;top:2px;width:12px;height:12px;border-radius:50%;background:#2ecc71;border:2px solid #0e1218;box-shadow:0 0 8px #2ecc71}
@keyframes sa-pulse{0%,100%{box-shadow:0 14px 40px rgba(0,0,0,.55),0 0 0 0 rgba(92,141,255,.35)}50%{box-shadow:0 14px 40px rgba(0,0,0,.55),0 0 0 14px rgba(92,141,255,0)}}

.sa-panel{position:fixed;left:20px;bottom:92px;width:min(380px,92vw);height:min(540px,72vh);z-index:9001;background:var(--panel);border:1px solid var(--line);border-radius:18px;overflow:hidden;display:none;flex-direction:column;box-shadow:0 30px 80px rgba(0,0,0,.65);animation:sa-in .22s cubic-bezier(.22,.9,.28,1)}
.sa-panel.open{display:flex}
@keyframes sa-in{from{opacity:0;transform:translateY(10px) scale(.97)}to{opacity:1;transform:translateY(0) scale(1)}}
.sa-head{display:flex;align-items:center;gap:12px;padding:12px 14px;background:linear-gradient(135deg,rgba(92,141,255,.16),rgba(124,92,255,.06) 60%,transparent);border-bottom:1px solid var(--line);flex-shrink:0}
.sa-ava{width:42px;height:42px;border-radius:50%;object-fit:cover;border:2px solid rgba(92,141,255,.5);background:#000;flex-shrink:0;display:block}
.sa-head-info{flex:1;min-width:0}
.sa-title{font-size:14.5px;font-weight:800;letter-spacing:.3px;background:linear-gradient(90deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.sa-sub{font-size:10.5px;color:var(--muted);margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-weight:600}
.sa-close{background:transparent;border:1px solid var(--line);color:var(--muted);width:34px;height:34px;border-radius:9px;cursor:pointer;font-size:20px;line-height:1;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0}
.sa-close:hover{color:var(--accent);border-color:var(--accent)}
.sa-body{flex:1;overflow-y:auto;padding:16px 14px;display:flex;flex-direction:column;gap:12px;background:var(--bg)}
.sa-msg{display:flex;flex-direction:column;max-width:86%}
.sa-msg.sa-user{align-self:flex-end;align-items:flex-end}
.sa-msg.sa-bot{align-self:flex-start;align-items:flex-start}
.sa-bubble{padding:11px 14px;border-radius:14px;font-size:13.5px;line-height:1.6;white-space:pre-wrap;word-wrap:break-word}
.sa-bot .sa-bubble{background:var(--panel2);color:var(--txt);border:1px solid var(--line);border-bottom-left-radius:5px}
.sa-user .sa-bubble{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border-bottom-right-radius:5px}
.sa-bubble b{font-weight:700}
.sa-bubble code{background:rgba(0,0,0,.35);padding:2px 6px;border-radius:5px;font:12px monospace}
.sa-typing{display:inline-flex;gap:4px;align-items:center;padding:10px 14px}
.sa-typing i{width:6px;height:6px;border-radius:50%;background:var(--muted);display:inline-block;animation:sa-bounce 1.2s ease-in-out infinite}
.sa-typing i:nth-child(2){animation-delay:.15s}
.sa-typing i:nth-child(3){animation-delay:.3s}
@keyframes sa-bounce{0%,80%,100%{opacity:.35;transform:translateY(0)}40%{opacity:1;transform:translateY(-4px)}}
.sa-foot{display:flex;gap:8px;padding:10px 12px;border-top:1px solid var(--line);background:var(--panel);flex-shrink:0;align-items:flex-end}
.sa-input{flex:1;resize:none;padding:11px 13px;background:var(--bg);border:1px solid var(--line);color:var(--txt);font:inherit;font-size:13.5px;border-radius:11px;outline:none;max-height:120px;min-height:44px;line-height:1.4}
.sa-input:focus{border-color:var(--accent)}
.sa-send{width:46px;height:46px;flex-shrink:0;border:0;border-radius:11px;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;cursor:pointer;display:inline-flex;align-items:center;justify-content:center}
.sa-send:hover{filter:brightness(1.1)}
.sa-send:disabled{opacity:.5;cursor:not-allowed}
.sa-send svg{width:20px;height:20px}
@media (max-width:520px){
  .sa-launcher{left:14px;bottom:14px;width:56px;height:56px}
  .sa-panel{left:8px;right:8px;bottom:80px;width:auto;height:min(560px,74vh)}
}
</style>

<script>
(function(){
  var launcher = document.getElementById('sa-launcher');
  var panel = document.getElementById('sa-panel');
  var body = document.getElementById('sa-body');
  var input = document.getElementById('sa-input');
  var sendBtn = document.getElementById('sa-send');
  var history = [];
  var busy = false;

  /* ---------- draggable ---------- */
  var drag = {active:false, moved:false, sx:0, sy:0, ox:0, oy:0, ptr:null};
  var POS_KEY = 'sa_launcher_pos';

  function applyPos(p){
    if(!p) return;
    launcher.style.left = p.x + 'px';
    launcher.style.top  = p.y + 'px';
    launcher.style.bottom = 'auto';
    launcher.style.right  = 'auto';
  }
  function savePos(p){
    try{ localStorage.setItem(POS_KEY, JSON.stringify(p)); }catch(e){}
  }
  function loadPos(){
    try{
      var s = localStorage.getItem(POS_KEY);
      if(s) return JSON.parse(s);
    }catch(e){}
    return null;
  }
  // clamp so it never goes off screen
  function clamp(x,y){
    var w = launcher.offsetWidth||60;
    var h = launcher.offsetHeight||60;
    var maxX = window.innerWidth - w;
    var maxY = window.innerHeight - h;
    return {x: Math.max(0,Math.min(maxX,x)), y: Math.max(0,Math.min(maxY,y))};
  }
  var saved = loadPos();
  if(saved){ var c = clamp(saved.x, saved.y); applyPos(c); }

  launcher.addEventListener('pointerdown', function(e){
    if(e.button!==undefined && e.button!==0) return;
    drag.active = true; drag.moved = false;
    drag.sx = e.clientX; drag.sy = e.clientY;
    var r = launcher.getBoundingClientRect();
    drag.ox = e.clientX - r.left;
    drag.oy = e.clientY - r.top;
    launcher.classList.add('dragging');
    try{ launcher.setPointerCapture(e.pointerId); }catch(x){}
    drag.ptr = e.pointerId;
    e.preventDefault();
  });
  launcher.addEventListener('pointermove', function(e){
    if(!drag.active) return;
    var dx = e.clientX - drag.sx;
    var dy = e.clientY - drag.sy;
    if(Math.abs(dx)>4 || Math.abs(dy)>4) drag.moved = true;
    if(!drag.moved) return;
    var p = clamp(e.clientX - drag.ox, e.clientY - drag.oy);
    applyPos(p);
  });
  function endDrag(e){
    if(!drag.active) return;
    drag.active = false;
    launcher.classList.remove('dragging');
    try{ launcher.releasePointerCapture(drag.ptr); }catch(x){}
    var r = launcher.getBoundingClientRect();
    savePos({x:r.left, y:r.top});
    if(!drag.moved){ saToggle(); }
  }
  launcher.addEventListener('pointerup', endDrag);
  launcher.addEventListener('pointercancel', endDrag);

  /* re-clamp on resize */
  window.addEventListener('resize', function(){
    var r = launcher.getBoundingClientRect();
    var c = clamp(r.left, r.top);
    applyPos(c); savePos(c);
  });

  /* ---------- open/close ---------- */
  window.saClose = function(){ panel.classList.remove('open'); };
  function saToggle(){ panel.classList.toggle('open'); if(panel.classList.contains('open')) setTimeout(function(){ input.focus(); }, 60); }
  window.saToggle = saToggle;

  /* ---------- chat ---------- */
  function esc(s){ return String(s==null?'':s).replace(/[&<>]/g, function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c];}); }
  function addMsg(role, text){
    var wrap = document.createElement('div');
    wrap.className = 'sa-msg sa-' + (role==='user' ? 'user' : 'bot');
    var bubble = document.createElement('div');
    bubble.className = 'sa-bubble';
    bubble.innerHTML = esc(text).replace(/\n/g,'<br>');
    wrap.appendChild(bubble);
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
      body: JSON.stringify({messages: history}),
    })
    .then(function(r){ return r.json(); })
    .then(function(j){
      t.remove();
      if(j && j.ok){
        addMsg('bot', j.reply);
        history.push({role:'assistant', content:j.reply});
      } else {
        addMsg('bot', '⚠️ Sorry, something went wrong. Try again in a moment.');
      }
    })
    .catch(function(){
      t.remove();
      addMsg('bot', '⚠️ Network error. Check your connection and try again.');
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
})();
</script>
"""
