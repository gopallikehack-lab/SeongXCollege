"""Admin dashboard page."""

ADMIN_PAGE = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Admin · 𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚</title>
<link rel="icon" href="https://i.ibb.co/GQvZNJ5x/file-00000000a2d082088bb8b30c95b7d8b9.png">
<style>
body{margin:0;min-height:100vh;background:#07090c;color:#e6e9ee;font:14px -apple-system,monospace}
.header{padding:20px 24px;background:linear-gradient(180deg,#141a22,#0a0e14);border-bottom:1px solid #1e2630;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px}
.header .hd{display:flex;align-items:center;gap:12px}
.header img{width:40px;height:40px;border-radius:10px;background:#000;border:1px solid #1e2630}
h1{margin:0;font-size:18px;background:linear-gradient(90deg,#5c8dff,#7c5cff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.nav{display:flex;gap:8px}
.btn{padding:10px 16px;background:#141a22;border:1px solid #1e2630;color:#e6e9ee;border-radius:9px;font:inherit;font-weight:600;font-size:12.5px;cursor:pointer;min-height:40px;display:inline-flex;align-items:center;text-decoration:none}
.btn:hover{border-color:#5c8dff;color:#5c8dff}
.btn.danger:hover{border-color:#ff5c5c;color:#ff5c5c}
.wrap{max-width:900px;margin:0 auto;padding:24px 20px 60px}
.card{background:#0e1218;border:1px solid #1e2630;border-radius:14px;padding:24px;margin-bottom:20px}
.card h2{margin:0 0 16px;font-size:16px}
label{display:block;font-size:11px;color:#7c8697;text-transform:uppercase;letter-spacing:.6px;margin:12px 0 6px;font-weight:600}
input,textarea{width:100%;padding:12px 14px;background:#07090c;border:1px solid #1e2630;color:#e6e9ee;font:inherit;border-radius:10px;min-height:46px;box-sizing:border-box}
textarea{font:12px monospace;min-height:80px}
input:focus,textarea:focus{outline:none;border-color:#5c8dff}
.btn-primary{margin-top:14px;padding:12px 22px;background:linear-gradient(90deg,#5c8dff,#7c5cff);color:#fff;border:0;border-radius:10px;font:inherit;font-weight:700;cursor:pointer;min-height:46px;font-size:14px}
.row{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:14px;background:#07090c;border:1px solid #1e2630;border-radius:10px;margin-bottom:10px;flex-wrap:wrap}
.info{display:flex;flex-direction:column;gap:4px;min-width:0;flex:1}
.em{color:#dfe6f0;font-weight:600;word-break:break-all;font-size:13px}
.lb{color:#7c8697;font-size:11.5px}
.tk{color:#9fb8ff;font:11px monospace;word-break:break-all}
.token-status{padding:4px 10px;border-radius:12px;font-size:11px;font-weight:600}
.token-ok{background:rgba(46,204,113,.1);color:#2ecc71;border:1px solid rgba(46,204,113,.3)}
.token-warn{background:rgba(246,183,60,.1);color:#f6b73c;border:1px solid rgba(246,183,60,.3)}
.token-bad{background:rgba(255,92,92,.1);color:#ff5c5c;border:1px solid rgba(255,92,92,.3)}
.msg{margin-top:12px;padding:11px 14px;border-radius:8px;font-size:12.5px;display:none}
.msg.show{display:block}
.msg.ok{background:rgba(46,204,113,.1);color:#2ecc71}
.msg.err{background:rgba(255,92,92,.1);color:#ff8b8b}
.help{padding:14px;background:#07090c;border-radius:10px;font-size:12px;color:#7c8697;line-height:1.7;margin-top:12px}
.help code{background:#141a22;padding:2px 6px;border-radius:4px;color:#9fb8ff;font-size:11px}
</style></head><body>
<div class="header">
  <div class="hd">
    <img src="https://i.ibb.co/GQvZNJ5x/file-00000000a2d082088bb8b30c95b7d8b9.png" alt="logo">
    <h1>𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚 · Admin</h1>
  </div>
  <div class="nav">
    <a href="/" class="btn">← Site</a>
    <a href="https://t.me/SeongEraStudy" target="_blank" class="btn">📢 Channel</a>
    <button class="btn danger" onclick="logout()">Logout</button>
  </div>
</div>
<div class="wrap">
  <div class="card">
    <h2>Add Account</h2>
    <form id="add-form">
      <label>Email</label>
      <input name="email" type="email" required>
      <label>Access Token</label>
      <textarea name="token" required placeholder="paste access_token here"></textarea>
      <label>Label (optional)</label>
      <input name="label" type="text" placeholder="e.g. Main">
      <button type="submit" class="btn-primary">Add Account</button>
      <div id="add-msg" class="msg"></div>
    </form>
    <div class="help">
      <b>How to get the token:</b><br>
      1. Log in to <code>apnacollege.in</code><br>
      2. DevTools → Application → Cookies → <code>www.apnacollege.in</code><br>
      3. Copy <code>lw_tokens</code> → extract only <code>access_token</code> value<br>
      4. Paste. Valid <b>7 days</b>.
    </div>
  </div>
  <div class="card">
  <h2>Site Status</h2>
  <div class="row" style="justify-content:space-between;align-items:center">
    <div class="info">
      <span class="em">Maintenance mode</span>
      <span class="lb">When ON, everyone except admin sees a maintenance page.</span>
    </div>
    <div style="display:flex;gap:10px;align-items:center">
      <span id="maint-status" class="token-status token-ok">off</span>
      <button class="btn" id="maint-toggle" onclick="toggleMaint()">Turn ON</button>
    </div>
  </div>
  <div id="maint-msg" class="msg"></div>
</div>
  <div class="card">
    <h2>Accounts (<span id="count">0</span>)</h2>
    <div id="list"></div>
    <div style="margin-top:14px;display:flex;gap:10px;flex-wrap:wrap">
      <button class="btn" onclick="testAll()">Test All</button>
      <button class="btn" onclick="reload()">Refresh</button>
      <button class="btn" onclick="clearCache()">Clear Batch Cache</button>
    </div>
    <div id="test-msg" class="msg"></div>
  </div>
</div>
<script>
async function reload(){
  const r=await fetch('/api/admin/accounts');
  const j=await r.json();
  const list=document.getElementById('list');
  const accts=j.accounts||[];
  document.getElementById('count').textContent=accts.length;
  if(!accts.length){list.innerHTML='<p style="color:#7c8697">No accounts.</p>';return;}
  list.innerHTML=accts.map(a=>`
    <div class="row">
      <div class="info">
        <span class="em">${a.display}</span>
        <span class="lb">${a.label||''} · ${a.added_ago||''}</span>
        <span class="tk">${a.token_prefix||''}…</span>
      </div>
      <span class="token-status ${a.status_class}">${a.status_text}</span>
      <button class="btn danger" onclick="removeAcct('${a.email}')">Remove</button>
    </div>`).join('');
}
async function addAcct(e){
  e.preventDefault();
  const f=e.target;
  const r=await fetch('/api/admin/accounts',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email:f.email.value,token:f.token.value,label:f.label.value})});
  const j=await r.json();
  const msg=document.getElementById('add-msg');
  msg.textContent=j.error||(j.ok?'added ✓':'');
  msg.className='msg show '+(j.ok?'ok':'err');
  if(j.ok){f.reset();reload();}
}
async function removeAcct(email){
  if(!confirm('Remove '+email+'?'))return;
  await fetch('/api/admin/accounts',{method:'DELETE',headers:{'Content-Type':'application/json'},body:JSON.stringify({email})});
  reload();
}
async function testAll(){
  const msg=document.getElementById('test-msg');
  msg.textContent='testing…';msg.className='msg show';
  const r=await fetch('/api/admin/test');
  const j=await r.json();
  msg.textContent=(j.results||[]).map(x=>`${x.email}: ${x.ok?'✓':'✗ '+x.error}`).join(' · ');
  msg.className='msg show '+(j.results&&j.results.every(x=>x.ok)?'ok':'err');
}
async function clearCache(){await fetch('/api/admin/clear_batch_cache');alert('cache cleared');}
async function logout(){await fetch('/logout',{method:'POST'});location.href='/';}
document.getElementById('add-form').addEventListener('submit',addAcct);
reload();
</script></body></html>"""
