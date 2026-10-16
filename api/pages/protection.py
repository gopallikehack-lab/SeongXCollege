"""Protection page template (glassmorphism + Turnstile)."""

from ..protection import TURNSTILE_SITE_KEY


PROTECTION_PAGE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Verifying… · 𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚</title>
<link rel="icon" href="https://i.ibb.co/GQvZNJ5x/file-00000000a2d082088bb8b30c95b7d8b9.png">
<script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>
<style>
:root{
  --accent:#5c8dff;--accent2:#7c5cff;--txt:#eaf0ff;--muted:#a9b6d0;
}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{height:100%}
body{
  margin:0;font:15px/1.5 -apple-system,"SF Mono",ui-monospace,monospace;
  color:var(--txt);overflow:hidden;
  background:
    radial-gradient(ellipse at 20% 10%, #1b2b5e 0%, transparent 55%),
    radial-gradient(ellipse at 85% 90%, #2a1a4d 0%, transparent 55%),
    linear-gradient(135deg,#0a0f1e 0%,#070a15 55%,#050812 100%);
  min-height:100vh;
  display:flex;align-items:center;justify-content:center;padding:24px;
  position:relative;
}
/* floating blobs */
body::before,body::after{content:"";position:fixed;pointer-events:none;border-radius:50%;filter:blur(90px);opacity:.55;z-index:0}
body::before{width:420px;height:420px;left:-140px;top:-140px;background:linear-gradient(135deg,#5c8dff,#b35cff);animation:float1 16s ease-in-out infinite}
body::after{width:380px;height:380px;right:-140px;bottom:-140px;background:linear-gradient(135deg,#7c5cff,#00d4ff);animation:float2 18s ease-in-out infinite}
@keyframes float1{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(40px,30px) scale(1.08)}}
@keyframes float2{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(-40px,-30px) scale(1.1)}}

.card{
  position:relative;z-index:1;
  width:100%;max-width:440px;
  padding:40px 30px 34px;
  border-radius:22px;
  background:rgba(255,255,255,.06);
  border:1px solid rgba(255,255,255,.14);
  backdrop-filter:blur(22px) saturate(150%);
  -webkit-backdrop-filter:blur(22px) saturate(150%);
  box-shadow:
    0 24px 70px rgba(0,0,0,.55),
    inset 0 1px 0 rgba(255,255,255,.16);
  text-align:center;
  animation:enter .5s cubic-bezier(.22,.9,.28,1);
}
@keyframes enter{from{opacity:0;transform:translateY(14px) scale(.97)}to{opacity:1;transform:translateY(0) scale(1)}}
.card::before{content:"";position:absolute;inset:0;border-radius:22px;padding:1px;background:linear-gradient(135deg,rgba(255,255,255,.35),rgba(255,255,255,0));-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none}

.shield{
  width:74px;height:74px;border-radius:50%;margin:0 auto 20px;
  display:flex;align-items:center;justify-content:center;
  background:linear-gradient(135deg,rgba(92,141,255,.25),rgba(179,92,255,.18));
  border:1px solid rgba(255,255,255,.18);
  box-shadow:0 12px 40px rgba(92,141,255,.4), inset 0 1px 0 rgba(255,255,255,.2);
  font-size:34px;
  animation:pulse 2.6s ease-in-out infinite;
}
@keyframes pulse{
  0%,100%{box-shadow:0 12px 40px rgba(92,141,255,.4), inset 0 1px 0 rgba(255,255,255,.2), 0 0 0 0 rgba(92,141,255,.35)}
  50%{box-shadow:0 12px 40px rgba(92,141,255,.6), inset 0 1px 0 rgba(255,255,255,.2), 0 0 0 18px rgba(92,141,255,0)}
}

h1{margin:0 0 8px;font-size:20px;font-weight:800;letter-spacing:.4px;background:linear-gradient(90deg,#fff,#a9c3ff 60%,#c79dff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.sub{margin:0 0 26px;color:var(--muted);font-size:13px;line-height:1.65}

.cf-widget{
  display:flex;justify-content:center;align-items:center;
  min-height:70px;margin-bottom:22px;
  padding:8px;border-radius:14px;
  background:rgba(255,255,255,.04);
  border:1px solid rgba(255,255,255,.08);
}

.status{
  display:inline-flex;align-items:center;gap:8px;
  padding:8px 14px;border-radius:10px;
  font-size:12.5px;color:var(--muted);
  background:rgba(255,255,255,.05);
  border:1px solid rgba(255,255,255,.08);
  transition:all .25s ease;
}
.status .dot{width:8px;height:8px;border-radius:50%;background:#5c8dff;box-shadow:0 0 10px #5c8dff}
.status.waiting .dot{animation:blink 1.2s ease-in-out infinite}
@keyframes blink{0%,100%{opacity:.35}50%{opacity:1}}
.status.ok{color:#7be0a8;background:rgba(46,204,113,.12);border-color:rgba(46,204,113,.3)}
.status.ok .dot{background:#2ecc71;box-shadow:0 0 10px #2ecc71}
.status.err{color:#ff8b8b;background:rgba(255,92,92,.12);border-color:rgba(255,92,92,.3)}
.status.err .dot{background:#ff5c5c;box-shadow:0 0 10px #ff5c5c}

.foot{margin-top:22px;font-size:11px;color:var(--muted);line-height:1.7}
.foot a{color:#9fb8ff;text-decoration:none}
.foot a:hover{text-decoration:underline}

@media (max-width:480px){
  .card{padding:32px 22px 26px;border-radius:20px}
  h1{font-size:18px}
  .shield{width:64px;height:64px;font-size:30px}
}
</style>
</head>
<body>

<div class="card">
  <div class="shield">🛡️</div>
  <h1>SeongEraStudy Protection</h1>
  <p class="sub">Quick security check to keep the site clean and bot-free.<br>This takes a second.</p>

  <div class="cf-widget">
    <div class="cf-turnstile"
         data-sitekey="__SITE_KEY__"
         data-callback="onTurnstileSuccess"
         data-error-callback="onTurnstileError"
         data-expired-callback="onTurnstileExpired"
         data-theme="dark"
         data-size="normal"
         data-appearance="always"></div>
  </div>

  <div class="status waiting" id="status">
    <span class="dot"></span>
    <span id="status-text">waiting for verification…</span>
  </div>

  <div class="foot">
    Protected by Cloudflare Turnstile · <a href="https://t.me/SeongEraStudy" target="_blank">@SeongEraStudy</a>
  </div>
</div>

<script>
function setStatus(kind, text){
  var s = document.getElementById('status');
  s.className = 'status ' + kind;
  document.getElementById('status-text').textContent = text;
}

function onTurnstileSuccess(token){
  setStatus('ok', 'verified · entering…');
  fetch('/api/verify', {
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body: JSON.stringify({token: token}),
  })
  .then(function(r){ return r.json(); })
  .then(function(j){
    if(j && j.ok){
      setTimeout(function(){ location.href = '/'; }, 400);
    } else {
      setStatus('err', 'verification failed — retry');
      if(window.turnstile) try{ turnstile.reset(); }catch(e){}
    }
  })
  .catch(function(){
    setStatus('err', 'network error — retry');
    if(window.turnstile) try{ turnstile.reset(); }catch(e){}
  });
}
function onTurnstileError(){
  setStatus('err', 'challenge error — refresh page');
}
function onTurnstileExpired(){
  setStatus('waiting', 'challenge expired — retry');
}
</script>

</body>
</html>""".replace("__SITE_KEY__", TURNSTILE_SITE_KEY)
