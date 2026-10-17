"""Admin Batches page template."""

ADMIN_BATCHES_PAGE = r"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Batches · Admin · 𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚</title>
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
.btn.primary{background:linear-gradient(135deg,#5c8dff,#7c5cff);color:#fff;border:0}
.wrap{max-width:1000px;margin:0 auto;padding:24px 20px 60px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:14px;margin-bottom:24px}
.stat{background:#0e1218;border:1px solid #1e2630;border-radius:14px;padding:18px;text-align:center}
.stat .n{font-size:28px;font-weight:800;color:#5c8dff;line-height:1.1;margin-bottom:4px}
.stat .l{font-size:11px;color:#7c8697;text-transform:uppercase;letter-spacing:.6px;font-weight:600}
.search-wrap{margin-bottom:16px}
.search-wrap input{width:100%;padding:14px 16px;background:#0e1218;border:1px solid #1e2630;color:#e6e9ee;border-radius:12px;font:inherit;font-size:14px;outline:none}
.search-wrap input:focus{border-color:#5c8dff}
.batch-card{background:#0e1218;border:1px solid #1e2630;border-radius:14px;margin-bottom:12px;overflow:hidden}
.b-head{padding:16px 20px;display:flex;justify-content:space-between;align-items:center;cursor:pointer;gap:12px;user-select:none}
.b-head:hover{background:rgba(255,255,255,.02)}
.b-title{font-size:15px;font-weight:700;color:#dfe6f0;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.b-badge{padding:4px 10px;border-radius:8px;font-size:12px;font-weight:700;background:rgba(92,141,255,.15);color:#5c8dff;border:1px solid rgba(92,141,255,.3);flex-shrink:0}
.b-arrow{color:#7c8697;transition:transform .2s}
.batch-card.open .b-arrow{transform:rotate(90deg);color:#5c8dff}
.b-body{display:none;border-top:1px solid #1e2630;background:#07090c;padding:8px 0}
.batch-card.open .b-body{display:block}
.tok-row{display:flex;justify-content:space-between;align-items:center;padding:12px 20px;border-bottom:1px solid rgba(255,255,255,.03);gap:10px;flex-wrap:wrap}
.tok-row:hover{background:rgba(255,255,255,.02)}
.tok-email{font-size:13px;color:#dfe6f0;word-break:break-all;flex:1;min-width:200px}
.tok-email .em-label{font-size:10px;color:#7c8697;font-weight:700;text-transform:uppercase;margin-right:6px;letter-spacing:.4px}
.tok-stat{font-size:10px;padding:2px 8px;border-radius:6px;background:#141a22;color:#7c8697;font-weight:600}
.empty{padding:40px 20px;text-align:center;color:#7c8697;font-size:13px}
</style></head><body>
<div class="header">
  <div class="hd">
    <img src="https://i.ibb.co/GQvZNJ5x/file-00000000a2d082088bb8b30c95b7d8b9.png" alt="logo">
    <h1>𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚 · Batches</h1>
  </div>
  <div class="nav">
    <a href="/admin" class="btn">← Admin</a>
    <a href="/" class="btn">↗ Site</a>
    <button class="btn" onclick="reload()">🔄 Refresh</button>
  </div>
</div>

<div class="wrap">
  <div class="stats">
    <div class="stat"><div class="n" id="s-total">0</div><div class="l">Total Batches</div></div>
    <div class="stat"><div class="n" id="s-tokens">0</div><div class="l">Total Tokens</div></div>
    <div class="stat"><div class="n" id="s-avg">0</div><div class="l">Avg Tokens / Batch</div></div>
  </div>

  <div class="search-wrap">
    <input id="search" placeholder="🔍 Search batch or email..." oninput="render()">
  </div>

  <div id="list"><div class="empty">loading…</div></div>
</div>

<script>
var BATCHES = [];

async function reload() {
  document.getElementById('list').innerHTML = '<div class="empty">loading…</div>';
  try {
    const r = await fetch('/api/admin/batches-stats');
    const j = await r.json();
    if (j.error) {
      document.getElementById('list').innerHTML = '<div class="empty" style="color:#ff7a7a">'+j.error+'</div>';
      return;
    }
    BATCHES = j.batches || [];
    document.getElementById('s-total').textContent = BATCHES.length;
    document.getElementById('s-tokens').textContent = j.total_tokens || 0;
    document.getElementById('s-avg').textContent = BATCHES.length ? Math.round(j.total_tokens / BATCHES.length * 10) / 10 : 0;
    render();
  } catch (e) {
    document.getElementById('list').innerHTML = '<div class="empty" style="color:#ff7a7a">error: '+e.message+'</div>';
  }
}

function render() {
  const q = document.getElementById('search').value.trim().toLowerCase();
  const list = document.getElementById('list');

  const filtered = BATCHES.map(b => {
    const tokens = (b.users || []).filter(u => !q || u.email.toLowerCase().includes(q));
    return { ...b, filteredUsers: tokens };
  }).filter(b => {
    if (!q) return true;
    return b.title.toLowerCase().includes(q) || b.filteredUsers.length > 0;
  });

  if (!filtered.length) {
    list.innerHTML = '<div class="empty">No batches match your search.</div>';
    return;
  }

  list.innerHTML = filtered.map((b, idx) => {
    const users = q ? b.filteredUsers : (b.users || []);
    const rows = users.map(u => `
      <div class="tok-row">
        <div class="tok-email"><span class="em-label">Email</span>${u.email}</div>
        <div class="tok-stat">${u.label || 'token'}</div>
      </div>
    `).join('') || '<div class="empty">No tokens for this batch</div>';

    return `
      <div class="batch-card ${q ? 'open' : ''}" id="bcard-${idx}">
        <div class="b-head" onclick="toggleCard(${idx})">
          <div class="b-title">${b.title}</div>
          <span class="b-badge">${users.length} token${users.length !== 1 ? 's' : ''}</span>
          <span class="b-arrow">▶</span>
        </div>
        <div class="b-body">${rows}</div>
      </div>
    `;
  }).join('');
}

function toggleCard(idx) {
  const card = document.getElementById('bcard-' + idx);
  if (card) card.classList.toggle('open');
}

reload();
</script>
</body></html>"""
