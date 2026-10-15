MAIN_PAGE = r"""<!DOCTYPE html>
<html lang="en" data-theme="default">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>SeongEra_Study 📚✏</title>
<style>
:root{--bg:#07090c;--panel:#0e1218;--panel2:#141a22;--line:#1e2630;--txt:#e6e9ee;--muted:#7c8697;--accent:#5c8dff;--accent2:#7c5cff;--good:#2ecc71;--warn:#f6b73c;--tap:44px}
[data-theme="rose"]{--accent:#ff5c8d;--accent2:#c45cff;--bg:#0c070b;--panel:#160d13;--panel2:#221420}
[data-theme="green"]{--accent:#2ecc71;--accent2:#13b6a3;--bg:#060d09;--panel:#0d1a12;--panel2:#152622}
[data-theme="amber"]{--accent:#f6b73c;--accent2:#ff8a4c;--bg:#0d0a06;--panel:#1a140a;--panel2:#2a2010}
[data-theme="crimson"]{--accent:#ff5c5c;--accent2:#b35cff;--bg:#0c0606;--panel:#1a0d0d;--panel2:#2a1414}
[data-theme="cyber"]{--accent:#00d4ff;--accent2:#7c5cff;--bg:#05080d;--panel:#0b1219;--panel2:#122030}
[data-theme="mono"]{--accent:#e6e9ee;--accent2:#9fb8ff;--bg:#050505;--panel:#101010;--panel2:#1a1a1a}
[data-theme="sunset"]{--accent:#ff7c5c;--accent2:#ff5cbd;--bg:#0d0608;--panel:#1a0f13;--panel2:#2a1820}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{margin:0;height:100%;background:var(--bg);color:var(--txt);font:14px/1.5 -apple-system,"SF Mono",ui-monospace,monospace;overflow:hidden}
button,select,input{font-family:inherit;-webkit-appearance:none;appearance:none}
a{color:var(--accent);text-decoration:none}
.brand-gradient{background:linear-gradient(90deg,var(--accent),var(--accent2) 60%,#b35cff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.topnav{display:flex;align-items:center;gap:10px;padding:12px 16px;background:linear-gradient(180deg,rgba(20,26,34,.6),rgba(10,14,20,.9));border-bottom:1px solid var(--line);flex-shrink:0}
.menu-btn{padding:8px 12px;background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:9px;cursor:pointer;font-size:18px;min-width:44px;min-height:44px;display:inline-flex;align-items:center;justify-content:center}
.brand{flex:1;min-width:0}
.brand h1{margin:0;font-size:16px;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.brand .sub{font-size:10.5px;color:var(--muted);display:block;margin-top:2px}
.theme-btn{padding:8px 12px;background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:9px;cursor:pointer;font-size:16px;min-width:44px;min-height:44px}
.drawer-bg{position:fixed;inset:0;background:rgba(0,0,0,.65);backdrop-filter:blur(4px);z-index:200;opacity:0;pointer-events:none;transition:opacity .22s}
.drawer-bg.open{opacity:1;pointer-events:auto}
.drawer{position:fixed;top:0;left:0;bottom:0;width:280px;max-width:85vw;background:var(--panel);border-right:1px solid var(--line);z-index:201;transform:translateX(-100%);transition:transform .22s;display:flex;flex-direction:column;overflow-y:auto}
.drawer.open{transform:translateX(0)}
.drawer-head{padding:20px 18px;border-bottom:1px solid var(--line);background:linear-gradient(180deg,rgba(92,141,255,.08),transparent)}
.drawer-head h2{margin:0;font-size:17px;font-weight:700}
.drawer-head .tg{font-size:11.5px;color:var(--muted);display:block;margin-top:4px}
.drawer-item{display:flex;align-items:center;gap:12px;padding:14px 18px;cursor:pointer;color:var(--txt);border-left:3px solid transparent;font-weight:600;font-size:13.5px;text-decoration:none}
.drawer-item.active{background:linear-gradient(90deg,rgba(92,141,255,.12),transparent);border-left-color:var(--accent);color:var(--accent)}
.drawer-item .ico{font-size:18px;width:24px;text-align:center}
.drawer-item .badge{background:var(--accent);color:#fff;font-size:10.5px;padding:1px 7px;border-radius:10px;margin-left:auto}
.drawer-foot{margin-top:auto;padding:16px 18px;font-size:10.5px;color:var(--muted);border-top:1px solid var(--line);line-height:1.6}
.content{flex:1;display:flex;flex-direction:column;overflow:hidden;min-height:0;position:relative}
.page{display:none;flex:1;overflow-y:auto;padding:16px}
.page.active{display:block}
.search-wrap{padding:12px 0;position:sticky;top:0;background:var(--bg);z-index:5}
.search-wrap input{width:100%;padding:12px 14px;background:var(--panel);border:1px solid var(--line);color:var(--txt);font:inherit;border-radius:10px;min-height:46px;font-size:14px}
.batch-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:14px;padding-bottom:40px}
@media (min-width:700px){.batch-grid{grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:16px}}
.batch-card{background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden;display:flex;flex-direction:column;transition:all .15s}
.batch-card:hover{border-color:var(--accent);transform:translateY(-2px)}
.batch-card .thumb{aspect-ratio:16/9;background:var(--panel2);position:relative;overflow:hidden;cursor:pointer}
.batch-card .thumb img{width:100%;height:100%;object-fit:cover;display:block}
.batch-card .thumb .pattern{position:absolute;inset:0;background-image:radial-gradient(circle at 20% 20%,rgba(255,255,255,.15) 0,transparent 40%),radial-gradient(circle at 80% 80%,rgba(255,255,255,.1) 0,transparent 40%)}
.batch-card .thumb .mono{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:52px;font-weight:800;color:#fff;text-shadow:0 3px 12px rgba(0,0,0,.35);letter-spacing:2px}
.batch-card .badge-enrolled{position:absolute;top:8px;right:8px;background:var(--good);color:#fff;font-size:10.5px;font-weight:700;padding:4px 9px;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,.3)}
.batch-card .meta{padding:10px 12px 6px;flex:1;display:flex;flex-direction:column;gap:3px;min-width:0}
.batch-card .meta .t{color:#dfe6f0;font-weight:600;font-size:13.5px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.batch-card .meta .s{color:var(--muted);font-size:11px}
.batch-card .actions{display:flex;gap:8px;padding:6px 12px 12px}
.batch-card .actions button{flex:1;padding:9px 8px;border-radius:9px;border:1px solid var(--line);font:inherit;font-weight:600;font-size:12.5px;cursor:pointer;min-height:40px;transition:all .12s;background:var(--panel2);color:var(--txt)}
.batch-card .actions .study{background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border-color:transparent}
.batch-card .actions .study:hover{filter:brightness(1.1)}
.batch-card .actions .enroll{background:var(--panel2);color:var(--txt)}
.batch-card .actions .enroll:hover{border-color:var(--accent);color:var(--accent)}
.batch-card .actions .enroll.on{background:rgba(46,204,113,.1);color:var(--good);border-color:rgba(46,204,113,.4)}

/* viewer */
.viewer{display:flex;flex-direction:column;height:100%;min-height:0}
.viewer-head{display:flex;align-items:center;gap:10px;padding:10px 16px;background:var(--panel);border-bottom:1px solid var(--line);flex-shrink:0}
.viewer-head .back{padding:8px 12px;background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:8px;cursor:pointer;font-size:14px;min-height:40px;min-width:40px}
.viewer-head .title{font-size:14px;font-weight:600;color:#dfe6f0;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.viewer-head .enroll-mini{padding:8px 14px;background:rgba(46,204,113,.1);color:var(--good);border:1px solid rgba(46,204,113,.4);border-radius:8px;cursor:pointer;font:inherit;font-weight:600;font-size:12.5px;min-height:40px}
.viewer-head .enroll-mini.off{background:var(--panel2);color:var(--txt);border-color:var(--line)}
.viewer-head .enroll-mini.off:hover{border-color:var(--good);color:var(--good)}
.player-main{flex:1;display:flex;flex-direction:column;overflow:hidden;min-height:0;position:relative}
.player-wrap{flex:1;background:#000;display:flex;align-items:center;justify-content:center;position:relative;min-height:0;overflow:hidden}
.player-empty{color:var(--muted);text-align:center;padding:32px;max-width:560px;line-height:1.8}
.player-empty h2{font-size:26px;margin:0 0 16px;font-weight:800}
.player-wrap video{width:100%;height:100%;background:#000;object-fit:contain}
.player-wrap iframe{width:100%;height:100%;border:0;background:#fff}
.controls{background:var(--panel);border-top:1px solid var(--line);padding:10px 14px;flex-shrink:0}
.ctr-row{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.controls button{background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:9px;padding:8px;cursor:pointer;min-height:44px;min-width:44px;font-size:15px;display:inline-flex;align-items:center;justify-content:center}
.controls .time{font-size:12px;color:var(--muted);min-width:100px;text-align:center}
.seekbar{flex:1;height:8px;background:var(--panel2);border-radius:4px;position:relative;cursor:pointer;min-width:100px}
.seekbar .filled{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--accent),var(--accent2));width:0%}
.seekbar .knob{position:absolute;top:50%;left:0;width:16px;height:16px;border-radius:50%;background:#fff;transform:translate(-50%,-50%)}
.controls select{background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:9px;padding:8px 10px;font:inherit;font-size:13px;min-height:44px}
.bottombar{padding:8px 14px;background:var(--panel);border-top:1px solid var(--line);flex-shrink:0;font-size:11.5px;color:var(--muted);display:flex;justify-content:space-between;gap:10px}
.status{padding:3px 10px;background:var(--panel2);border-radius:12px;color:var(--accent);font-weight:600;font-size:11px}
.status.ok{color:var(--good)}
.status.err{color:#ff7a7a}
.sections-overlay{position:fixed;top:0;left:0;bottom:0;width:340px;max-width:85vw;background:var(--panel);border-right:1px solid var(--line);z-index:250;transform:translateX(-100%);transition:transform .22s ease;display:flex;flex-direction:column;box-shadow:16px 0 40px rgba(0,0,0,.5)}
.sections-overlay.open{transform:translateX(0)}
.sections-overlay .sections-head{padding:14px 16px;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;align-items:center;flex-shrink:0}
.sections-overlay .sections-head h3{margin:0;font-size:14px;color:#dfe6f0}
.sections-overlay .close-sec{background:transparent;border:0;color:var(--muted);font-size:22px;cursor:pointer;padding:0 6px;min-width:40px;min-height:40px}
.sections-overlay .search2{padding:10px 12px;border-bottom:1px solid var(--line);flex-shrink:0}
.sections-overlay .search2 input{width:100%;padding:10px 12px;background:var(--bg);border:1px solid var(--line);color:var(--txt);font:inherit;border-radius:9px;min-height:42px;font-size:13.5px}
.toc{flex:1;overflow-y:auto;padding-bottom:40px}
.sec{border-bottom:1px solid var(--line)}
.sec-head{padding:13px 16px;cursor:pointer;display:flex;justify-content:space-between;gap:10px;align-items:center;font-weight:600;font-size:13px;color:#c8d0dd;min-height:44px}
.sec-head.open{background:var(--panel2);color:var(--accent)}
.sec-head .left{flex:1;display:flex;gap:10px;align-items:center;overflow:hidden}
.sec-head .t{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sec-head .cnt{color:var(--muted);font-size:11px;background:var(--panel2);padding:2px 8px;border-radius:10px}
.sec-body{display:none;background:rgba(0,0,0,.15)}
.sec-body.open{display:block}
.unit{padding:11px 16px 11px 24px;cursor:pointer;font-size:13px;color:#a8b3c2;border-left:3px solid transparent;display:flex;justify-content:space-between;gap:10px;align-items:center;min-height:44px}
.unit.active{background:linear-gradient(90deg,rgba(92,141,255,.12),transparent);color:var(--accent);border-left-color:var(--accent)}
.unit .u-left{flex:1;display:flex;gap:8px;align-items:center;overflow:hidden}
.unit .u-left .t{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.unit .type{padding:2px 8px;border-radius:8px;font-size:10px;background:var(--panel2);color:var(--muted);font-weight:600;text-transform:uppercase;flex-shrink:0}
.pdf-viewer{width:100%;height:100%;display:flex;flex-direction:column;background:#0a0a0a}
.pdf-toolbar{padding:10px 14px;background:var(--panel2);border-bottom:1px solid var(--line);display:flex;justify-content:space-between;gap:10px;align-items:center;flex-wrap:wrap}
.pdf-toolbar .name{color:#dfe6f0;font-weight:600;font-size:12.5px;flex:1;min-width:100px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.pdf-actions{display:flex;gap:6px;flex-wrap:wrap}
.pdf-actions a,.pdf-actions button{padding:8px 12px;background:var(--panel2);color:var(--txt);border:1px solid var(--line);border-radius:8px;font:inherit;font-weight:600;font-size:12px;cursor:pointer;min-height:38px;display:inline-flex;align-items:center;gap:5px;text-decoration:none}
.pdf-actions .primary{background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border-color:transparent}
.pdf-frame{flex:1;border:0;background:#fff}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:22px;margin-bottom:14px}
.card h2{margin:0 0 12px;font-size:16px;font-weight:700;color:#dfe6f0}
.card p{color:#c8d0dd;line-height:1.7;margin:8px 0;font-size:13.5px}
.card .btn-row{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}
.btn-link{display:inline-flex;align-items:center;gap:8px;padding:11px 18px;background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border-radius:10px;font-weight:600;font-size:13px;text-decoration:none;min-height:46px}
.btn-ghost{display:inline-flex;align-items:center;gap:8px;padding:11px 18px;background:var(--panel2);color:var(--txt);border:1px solid var(--line);border-radius:10px;font-weight:600;font-size:13px;text-decoration:none;min-height:46px}
.qr-img{width:min(100%,320px);border-radius:14px;border:1px solid var(--line);margin:14px auto 0;display:block;background:#fff;padding:12px}
.upi-box{background:var(--bg);border:1px solid var(--line);border-radius:10px;padding:14px;display:flex;justify-content:space-between;gap:10px;align-items:center;margin-top:14px;flex-wrap:wrap}
.upi-box .id{font:13px monospace;color:var(--accent);word-break:break-all;flex:1;min-width:120px}
.upi-box button{padding:10px 16px;background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border:0;border-radius:9px;font:inherit;font-weight:600;font-size:12.5px;cursor:pointer;min-height:40px}
.modal{position:fixed;inset:0;background:rgba(0,0,0,.8);backdrop-filter:blur(6px);display:none;align-items:center;justify-content:center;z-index:999;padding:16px}
.modal.open{display:flex}
.modal .box{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:22px;max-width:600px;width:100%;max-height:90vh;overflow-y:auto}
.modal h2{margin:0 0 6px;font-size:17px}
.modal .sub{color:var(--muted);font-size:12px;margin-bottom:16px}
.modal input{width:100%;padding:12px 14px;background:var(--bg);border:1px solid var(--line);color:var(--accent);font:12px monospace;border-radius:10px;margin-bottom:10px;box-sizing:border-box}
.modal .variant{padding:12px 14px;background:var(--bg);border:1px solid var(--line);border-radius:10px;margin-bottom:8px}
.modal .variant .name{font-weight:600;font-size:13px}
.modal .variant button{padding:10px 16px;background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:8px;cursor:pointer;font:inherit;font-size:12.5px;font-weight:600;min-height:40px}
.modal .close{float:right;background:transparent;border:0;color:var(--muted);font-size:26px;cursor:pointer;min-width:44px;min-height:44px}
.empty-state{text-align:center;padding:60px 20px;color:var(--muted)}
.empty-state h2{font-size:20px;color:#dfe6f0;margin:0 0 12px}
.empty-state p{max-width:400px;margin:0 auto;line-height:1.7}
@media (max-width:900px){
  .content{padding:0}
  .sections-overlay{width:88vw}
}
</style>
</head>
<body>
<div style="height:100vh;height:100dvh;display:flex;flex-direction:column">
  <div class="topnav">
    <button class="menu-btn" onclick="openDrawer()">☰</button>
    <div class="brand">
      <h1 class="brand-gradient">SeongEra_Study 📚✏</h1>
      <span class="sub">t.me/SeongEraStudy</span>
    </div>
    <button class="theme-btn" onclick="cycleTheme()">🎨</button>
  </div>

  <div class="drawer-bg" id="drawer-bg" onclick="closeDrawer()"></div>
  <div class="drawer" id="drawer">
    <div class="drawer-head">
      <h2 class="brand-gradient">SeongEra_Study</h2>
      <span class="tg">📚 Study free · Made By @Seong_Era</span>
    </div>
    <div class="drawer-item active" data-page="batches" onclick="goPage('batches')"><span class="ico">📚</span><span>All Batches</span></div>
    <div class="drawer-item" data-page="enrolled" onclick="goPage('enrolled')"><span class="ico">⭐</span><span>My Enrolled</span><span class="badge" id="enrolled-badge">0</span></div>
    <div class="drawer-item" data-page="enroll" onclick="goPage('enroll')"><span class="ico">➕</span><span>Request a Batch</span></div>
    <a class="drawer-item" href="https://t.me/SeongEraStudy" target="_blank"><span class="ico">💬</span><span>Join Telegram</span></a>
    <div class="drawer-item" data-page="contact" onclick="goPage('contact')"><span class="ico">📩</span><span>Contact Us</span></div>
    <div class="drawer-item" data-page="donate" onclick="goPage('donate')"><span class="ico">❤️</span><span>Donate</span></div>
    <div class="drawer-foot">Made By @Seong_Era<br>Support: t.me/Seong_Era</div>
  </div>

  <div class="content">
    <div class="page active" id="page-batches">
      <div class="search-wrap">
        <input id="batch-search" placeholder="🔍 Search batches…">
      </div>
      <div class="batch-grid" id="batch-grid">
        <div style="padding:24px;color:var(--muted);text-align:center;grid-column:1/-1">loading…</div>
      </div>
    </div>

    <div class="page" id="page-enrolled">
      <div class="search-wrap">
        <input id="enrolled-search" placeholder="🔍 Search enrolled…">
      </div>
      <div class="batch-grid" id="enrolled-grid"></div>
    </div>

    <div class="page" id="page-viewer">
      <div class="viewer">
        <div class="viewer-head">
          <button class="back" onclick="closeBatch()">←</button>
          <button class="back" onclick="toggleSections()" title="sections">☰</button>
          <div class="title" id="viewer-title">Batch</div>
          <button class="enroll-mini off" id="viewer-enroll" onclick="toggleEnrollCurrent()">☆ Enroll</button>
        </div>
        <div class="player-main">
          <div class="player-wrap" id="player-wrap">
            <div class="player-empty">
              <h2 class="brand-gradient">Pick a lecture</h2>
              <p>Open the sections panel with ☰ to browse lectures.</p>
            </div>
          </div>
          <div class="controls" id="controls" style="display:none">
            <div class="ctr-row">
              <button id="btn-play" onclick="togglePlay()">▶</button>
              <span class="time" id="time">0:00 / 0:00</span>
              <div class="seekbar" id="seek" onclick="seekClick(event)"><div class="filled" id="seek-filled"></div><div class="knob" id="seek-knob"></div></div>
              <button onclick="skip(-10)">⟲</button><button onclick="skip(10)">⟳</button>
              <select id="speed" onchange="setSpeed(this.value)"><option value="0.5">0.5×</option><option value="0.75">0.75×</option><option value="1" selected>1×</option><option value="1.25">1.25×</option><option value="1.5">1.5×</option><option value="2">2×</option></select>
              <select id="quality" onchange="onQualityChange(this.value)"><option value="auto">auto</option></select>
              <button onclick="openDownload()">⬇</button><button onclick="openLink()">🔗</button><button onclick="toggleFS()">⛶</button>
            </div>
          </div>
          <div class="bottombar">
            <span class="status" id="status">ready</span>
            <span id="nowplaying"></span>
          </div>
        </div>
      </div>
    </div>

    <div class="page" id="page-enroll">
      <div class="card">
        <h2>➕ Request a Batch</h2>
        <p>Want a new batch added to <b>SeongEra_Study</b>? Message me on Telegram with the batch name or link.</p>
        <div class="btn-row">
          <a class="btn-link" href="https://t.me/Seong_Era" target="_blank">💬 Message @Seong_Era</a>
          <a class="btn-ghost" href="https://t.me/SeongEraStudy" target="_blank">📢 Join Channel</a>
        </div>
      </div>
    </div>

    <div class="page" id="page-contact">
      <div class="card">
        <h2>📩 Contact Us</h2>
        <p>Any issue or feedback — reach out on Telegram.</p>
        <div class="btn-row">
          <a class="btn-link" href="https://t.me/Seong_Era" target="_blank">💬 @Seong_Era (Personal)</a>
          <a class="btn-ghost" href="https://t.me/SeongEraStudy" target="_blank">📢 Study Channel</a>
        </div>
      </div>
      <div class="card">
        <h2>Common stuff</h2>
        <p><b>Video won't load:</b> reload. Still broken? Message me the batch + lecture name.</p>
        <p><b>Wrong quality or lag:</b> pick a lower resolution.</p>
        <p><b>Download:</b> hit ⬇ in the player. Saves a .ts file — VLC plays it fine.</p>
        <p><b>New batch:</b> use the Request page.</p>
      </div>
    </div>

    <div class="page" id="page-donate">
      <div class="card">
        <h2>❤️ Support SeongEra_Study</h2>
        <p>If this helped you, even a small amount keeps it alive for everyone.</p>
        <p><b>Thank you for the support — it means a lot. 🙏</b></p>
        <img class="qr-img" src="__QR_IMAGE__" alt="UPI QR">
        <div class="upi-box">
          <span class="id" id="upi-id">__UPI_ID__</span>
          <button onclick="copyUpi(this)">📋 copy UPI ID</button>
        </div>
      </div>
      <div class="card">
        <h2>Where it goes</h2>
        <p>• Server + domain costs</p>
        <p>• New batches, more lectures</p>
        <p>• Keeping it free for everyone</p>
      </div>
    </div>
  </div>
</div>

<div class="sections-overlay" id="sections-overlay">
  <div class="sections-head">
    <h3 id="sections-title">Sections</h3>
    <button class="close-sec" onclick="toggleSections()">✕</button>
  </div>
  <div class="search2"><input id="search" placeholder="search units…"></div>
  <div class="toc" id="toc"></div>
</div>

<div class="modal" id="modal-dl"><div class="box"><button class="close" onclick="closeModal('modal-dl')">×</button><h2>Download</h2><div class="sub">Downloads directly to your device</div><div class="variants" id="dl-variants"></div></div></div>
<div class="modal" id="modal-link"><div class="box"><button class="close" onclick="closeModal('modal-link')">×</button><h2>Direct m3u8 links</h2><div class="sub">Paste into VLC, mpv, yt-dlp</div><input id="link-master" readonly onclick="this.select()"><button onclick="copyField('link-master',this)" style="padding:12px 18px;background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border:0;border-radius:10px;font:inherit;font-weight:600;cursor:pointer;margin-bottom:16px;width:100%">copy master</button><div class="variants" id="link-variants"></div></div></div>

<script src="https://cdn.jsdelivr.net/npm/hls.js@1"></script>
<script>
(function(){
'use strict';
var BATCHES=[],ACTIVE=null,FLAT=[],CURRENT=null,CURRENT_INFO=null,HLS=null,VIDEO=null,CURRENT_VARIANTS={};
var ENROLLED=[];
var THEMES=["default","rose","green","amber","crimson","cyber","mono","sunset"];
var curTheme=localStorage.getItem("theme")||"default";
document.documentElement.setAttribute("data-theme",curTheme);
var PALETTES=[['#5c8dff','#7c5cff'],['#ff5c8d','#c45cff'],['#2ecc71','#13b6a3'],['#f6b73c','#ff8a4c'],['#ff5c5c','#b35cff'],['#00d4ff','#7c5cff'],['#ff7c5c','#ff5cbd'],['#9d5cff','#5c8dff'],['#00b894','#00cec9'],['#fdcb6e','#e17055'],['#e84393','#fd79a8'],['#6c5ce7','#a29bfe']];
window.cycleTheme=function(){var i=THEMES.indexOf(curTheme);i=(i+1)%THEMES.length;curTheme=THEMES[i];document.documentElement.setAttribute("data-theme",curTheme);localStorage.setItem("theme",curTheme);};
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
function hashCode(s){var h=0;for(var i=0;i<s.length;i++){h=((h<<5)-h)+s.charCodeAt(i);h|=0;}return Math.abs(h);}
function pickGradient(l){return PALETTES[hashCode(l||'?')%PALETTES.length];}
function initials(l){var p=(l||'?').trim().split(/\s+/);if(p.length===1)return p[0].slice(0,2).toUpperCase();return (p[0].charAt(0)+p[1].charAt(0)).toUpperCase();}
function showPage(name){var pages=document.querySelectorAll('.page');for(var i=0;i<pages.length;i++)pages[i].classList.remove('active');var el=document.getElementById('page-'+name);if(el)el.classList.add('active');var items=document.querySelectorAll('.drawer-item[data-page]');for(var j=0;j<items.length;j++)items[j].classList.remove('active');var act=document.querySelector('.drawer-item[data-page="'+name+'"]');if(act)act.classList.add('active');}
window.goPage=function(name){showPage(name);closeDrawer();if(name==='enrolled')renderEnrolled();};
window.openDrawer=function(){document.getElementById('drawer').classList.add('open');document.getElementById('drawer-bg').classList.add('open');};
window.closeDrawer=function(){document.getElementById('drawer').classList.remove('open');document.getElementById('drawer-bg').classList.remove('open');};

// ---- enroll ----
function updateEnrollBadge(){document.getElementById('enrolled-badge').textContent=ENROLLED.length;}
function isEnrolled(tid){return ENROLLED.indexOf(tid)!==-1;}
window.toggleEnroll=function(tid,btn){
  var isOn=isEnrolled(tid);
  var method=isOn?'DELETE':'POST';
  fetch('/api/enroll',{method:method,headers:{'Content-Type':'application/json'},body:JSON.stringify({titleId:tid})})
    .then(function(r){return r.json();})
    .then(function(j){
      if(j.ok){ENROLLED=j.enrolled||[];updateEnrollBadge();renderBatches();renderEnrolled();updateViewerEnrollBtn();}
    });
};
window.toggleEnrollCurrent=function(){if(ACTIVE)toggleEnroll(ACTIVE);};
function updateViewerEnrollBtn(){var b=document.getElementById('viewer-enroll');if(!b||!ACTIVE)return;var on=isEnrolled(ACTIVE);b.textContent=on?'✓ Enrolled':'☆ Enroll';b.className='enroll-mini'+(on?'':' off');}

// ---- batches ----
function renderBatchCard(b){
  var card=document.createElement('div');card.className='batch-card';
  var hasImg=b.image&&b.image.indexOf('course-default-img')===-1;
  var g=pickGradient(b.label),ini=initials(b.label);
  var thumb;
  if(hasImg){thumb='<img src="'+esc(b.image)+'" alt="">';}
  else{thumb='<div class="pattern"></div><div class="mono">'+esc(ini)+'</div>';}
  var thumbStyle=hasImg?'':' style="background:linear-gradient(135deg,'+g[0]+','+g[1]+')"';
  var enrolledBadge=isEnrolled(b.titleId)?'<div class="badge-enrolled">⭐ Enrolled</div>':'';
  var enrollBtn=isEnrolled(b.titleId)?'<button class="enroll on" data-act="enroll" data-tid="'+esc(b.titleId)+'">✓ Enrolled</button>':'<button class="enroll" data-act="enroll" data-tid="'+esc(b.titleId)+'">☆ Enroll</button>';
  card.innerHTML=
    '<div class="thumb"'+thumbStyle+' data-act="study" data-tid="'+esc(b.titleId)+'" data-label="'+esc(b.label)+'">'+thumb+enrolledBadge+'</div>'+
    '<div class="meta"><span class="t">'+esc(b.label)+'</span><span class="s">tap study to open</span></div>'+
    '<div class="actions">'+
      '<button class="study" data-act="study" data-tid="'+esc(b.titleId)+'" data-label="'+esc(b.label)+'">▶ Study</button>'+
      enrollBtn+
    '</div>';
  return card;
}
function renderBatches(){
  var grid=document.getElementById('batch-grid');
  var q=(document.getElementById('batch-search').value||'').toLowerCase();
  grid.innerHTML='';
  var filtered=BATCHES.filter(function(b){return !q||(b.label||'').toLowerCase().indexOf(q)!==-1;});
  if(!filtered.length){grid.innerHTML='<div style="padding:24px;color:var(--muted);text-align:center;grid-column:1/-1">'+(BATCHES.length?'No batches match.':'No batches available.')+'</div>';return;}
  for(var i=0;i<filtered.length;i++){grid.appendChild(renderBatchCard(filtered[i]));}
}
function renderEnrolled(){
  var grid=document.getElementById('enrolled-grid');
  var q=(document.getElementById('enrolled-search').value||'').toLowerCase();
  grid.innerHTML='';
  var filtered=BATCHES.filter(function(b){return isEnrolled(b.titleId)&&(!q||(b.label||'').toLowerCase().indexOf(q)!==-1);});
  if(!filtered.length){grid.innerHTML='<div class="empty-state" style="grid-column:1/-1"><h2>No enrolled batches yet</h2><p>Click "☆ Enroll" on any batch to save it here.</p></div>';return;}
  for(var i=0;i<filtered.length;i++){grid.appendChild(renderBatchCard(filtered[i]));}
}

document.addEventListener('click',function(e){
  var t=e.target;
  var act=t.dataset&&t.dataset.act;
  if(!act)return;
  if(act==='study'){openBatch(t.dataset.tid,t.dataset.label);}
  else if(act==='enroll'){toggleEnroll(t.dataset.tid,t);}
});

// ---- viewer ----
window.openBatch=function(titleId,label){
  ACTIVE=titleId;
  document.getElementById('viewer-title').textContent=label;
  document.getElementById('sections-title').textContent=label;
  document.getElementById('search').value='';
  document.getElementById('toc').innerHTML='<div style="padding:20px;color:var(--muted)">loading sections…</div>';
  document.getElementById('player-wrap').innerHTML='<div class="player-empty"><h2 class="brand-gradient">Pick a lecture</h2><p>Open the sections panel with ☰ to browse lectures.</p></div>';
  document.getElementById('controls').style.display='none';
  destroyPlayer();
  updateViewerEnrollBtn();
  showPage('viewer');
  fetch('/api/sections/'+encodeURIComponent(titleId)).then(function(r){return r.json();}).then(function(j){
    if(!j||!j.sections){document.getElementById('toc').innerHTML='<div style="padding:20px;color:#ff7a7a">'+esc((j&&j.error)||'failed')+'</div>';return;}
    window._sections=j.sections;renderTOC();
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
  if(el)el.classList.add('active');
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
    else{document.getElementById('player-wrap').innerHTML='<div class="player-empty"><p>unsupported: '+esc(j.type||'?')+'</p></div>';}
    if(window.innerWidth<=900)document.getElementById('sections-overlay').classList.remove('open');
  }).catch(function(e){document.getElementById('player-wrap').innerHTML='<div class="player-empty"><p>error: '+esc(e.message||e)+'</p></div>';});
}
function destroyPlayer(){if(HLS){try{HLS.destroy();}catch(e){}HLS=null;}if(VIDEO){try{VIDEO.pause();}catch(e){}VIDEO=null;}}

function playWistia(sourceid){
  var master='https://fast.wistia.com/embed/medias/'+sourceid+'.m3u8';
  document.getElementById('player-wrap').innerHTML='<video id="v" playsinline preload="metadata"></video>';
  VIDEO=document.getElementById('v');
  document.getElementById('controls').style.display='block';
  fetch('/api/variants/'+encodeURIComponent(sourceid)).then(function(r){return r.json();}).then(function(j){CURRENT_VARIANTS=(j&&j.variants)||{};}).catch(function(){CURRENT_VARIANTS={};});
  if(window.Hls&&Hls.isSupported()){
    HLS=new Hls({capLevelToPlayerSize:false,startLevel:-1,autoStartLoad:true,maxBufferLength:60});
    HLS.loadSource(master);HLS.attachMedia(VIDEO);
    HLS.on(Hls.Events.MANIFEST_PARSED,function(e,data){
      var sel=document.getElementById('quality');sel.innerHTML='<option value="auto">auto</option>';
      for(var i=0;i<data.levels.length;i++){var lvl=data.levels[i];var o=document.createElement('option');o.value=i;o.textContent=lvl.height?(lvl.height+'p'):('L'+i);sel.appendChild(o);}
      VIDEO.play().catch(function(){});
    });
    HLS.on(Hls.Events.LEVEL_SWITCHED,function(e,data){var lvl=HLS.levels[data.level];if(lvl){document.getElementById('status').textContent='playing · '+(lvl.height||'?')+'p';document.getElementById('status').className='status ok';}});
  }else if(VIDEO.canPlayType('application/vnd.apple.mpegurl')){VIDEO.src=master;VIDEO.play().catch(function(){});}
  VIDEO.addEventListener('timeupdate',updateTime);
  VIDEO.addEventListener('loadedmetadata',updateTime);
  VIDEO.addEventListener('play',function(){document.getElementById('btn-play').textContent='❚❚';});
  VIDEO.addEventListener('pause',function(){document.getElementById('btn-play').textContent='▶';});
  VIDEO.addEventListener('click',togglePlay);
  document.getElementById('status').textContent='playing';
}

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

function updateTime(){if(!VIDEO)return;var cur=VIDEO.currentTime||0,dur=VIDEO.duration||0;document.getElementById('time').textContent=fmt(cur)+' / '+fmt(dur);var pct=dur?(cur/dur)*100:0;document.getElementById('seek-filled').style.width=pct+'%';document.getElementById('seek-knob').style.left=pct+'%';}
function fmt(s){s=Math.floor(s||0);var h=Math.floor(s/3600),m=Math.floor((s%3600)/60),r=s%60;if(h)return h+':'+(m<10?'0':'')+m+':'+(r<10?'0':'')+r;return m+':'+(r<10?'0':'')+r;}
window.togglePlay=function(){if(VIDEO){VIDEO.paused?VIDEO.play():VIDEO.pause();}};
window.skip=function(n){if(VIDEO)VIDEO.currentTime+=n;};
window.seekClick=function(e){if(!VIDEO)return;var r=e.currentTarget.getBoundingClientRect();VIDEO.currentTime=((e.clientX-r.left)/r.width)*(VIDEO.duration||0);};
window.setSpeed=function(v){if(VIDEO)VIDEO.playbackRate=parseFloat(v);};
window.onQualityChange=function(v){if(HLS)HLS.currentLevel=(v==='auto')?-1:parseInt(v,10);};
window.toggleFS=function(){var w=document.getElementById('player-wrap');if(!document.fullscreenElement)w.requestFullscreen();else document.exitFullscreen();};
window.openDownload=function(){
  if(!CURRENT_INFO)return;
  if(CURRENT_INFO.type==='pdf'){var a=document.querySelector('.pdf-actions a.primary');if(a)a.click();return;}
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
document.addEventListener('keydown',function(e){if(e.target.tagName==='INPUT'||e.target.tagName==='SELECT')return;var k=e.key;if(k==='/'){e.preventDefault();if(document.getElementById('page-viewer').classList.contains('active'))document.getElementById('search').focus();else document.getElementById('batch-search').focus();return;}if(!VIDEO)return;if(k===' '){e.preventDefault();togglePlay();}else if(k==='ArrowRight')VIDEO.currentTime+=5;else if(k==='ArrowLeft')VIDEO.currentTime-=5;else if(k==='f'||k==='F')toggleFS();});
document.getElementById('search').addEventListener('input',renderTOC);
document.getElementById('batch-search').addEventListener('input',renderBatches);
document.getElementById('enrolled-search').addEventListener('input',renderEnrolled);

function loadAll(){
  fetch('/api/enroll').then(function(r){return r.json();}).then(function(j){ENROLLED=(j&&j.enrolled)||[];updateEnrollBadge();});
  var grid=document.getElementById('batch-grid');
  grid.innerHTML='<div style="padding:24px;color:var(--muted);text-align:center;grid-column:1/-1">loading…</div>';
  fetch('/api/batches').then(function(r){return r.json();}).then(function(j){
    BATCHES=(j&&j.batches)||[];renderBatches();
  }).catch(function(e){grid.innerHTML='<div style="padding:24px;color:#ff7a7a;text-align:center;grid-column:1/-1">error: '+esc(e.message||e)+'</div>';});
}
if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',loadAll);}else{loadAll();}
})();
</script>
</body></html>"""
