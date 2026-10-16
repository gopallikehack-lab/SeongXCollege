"""MAIN_PAGE — HTML shell + CSS + JS."""
from .player_css import PLAYER_CSS
from .player_js import PLAYER_JS

_MAIN_HTML = r"""<!DOCTYPE html>
<html lang="en" data-theme="default">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚</title>
<link rel="icon" href="https://i.ibb.co/GQvZNJ5x/file-00000000a2d082088bb8b30c95b7d8b9.png">
<style>
:root{--bg:#07090c;--panel:#0e1218;--panel2:#141a22;--line:#1e2630;--txt:#e6e9ee;--muted:#7c8697;--accent:#5c8dff;--accent2:#7c5cff;--good:#2ecc71;--warn:#f6b73c}
[data-theme="dracula"]{--bg:#1e1f29;--panel:#282a36;--panel2:#343746;--line:#44475a;--txt:#f8f8f2;--muted:#a0a4b8;--accent:#bd93f9;--accent2:#ff79c6;--good:#50fa7b;--warn:#f1fa8c}
[data-theme="rose"]{--bg:#0c070b;--panel:#160d13;--panel2:#221420;--line:#2e1a2a;--txt:#f2e6ee;--muted:#a08290;--accent:#ff5c8d;--accent2:#c45cff;--good:#2ecc71;--warn:#f6b73c}
[data-theme="green"]{--bg:#060d09;--panel:#0d1a12;--panel2:#152622;--line:#1e3a2a;--txt:#dff0e4;--muted:#7e9a86;--accent:#2ecc71;--accent2:#13b6a3;--good:#2ecc71;--warn:#f6b73c}
[data-theme="amber"]{--bg:#0d0a06;--panel:#1a140a;--panel2:#2a2010;--line:#3a2c16;--txt:#f0e6d6;--muted:#9a8a6a;--accent:#f6b73c;--accent2:#ff8a4c;--good:#2ecc71;--warn:#f6b73c}
[data-theme="crimson"]{--bg:#0c0606;--panel:#1a0d0d;--panel2:#2a1414;--line:#3a1c1c;--txt:#f2e0e0;--muted:#9a7474;--accent:#ff5c5c;--accent2:#b35cff;--good:#2ecc71;--warn:#f6b73c}
[data-theme="cyber"]{--bg:#05080d;--panel:#0b1219;--panel2:#122030;--line:#1e3247;--txt:#dff2ff;--muted:#6a91b3;--accent:#00d4ff;--accent2:#7c5cff;--good:#00ffaa;--warn:#ffcc33}
[data-theme="mono"]{--bg:#050505;--panel:#101010;--panel2:#1a1a1a;--line:#262626;--txt:#e6e6e6;--muted:#7c7c7c;--accent:#e6e9ee;--accent2:#9fb8ff;--good:#8fd08f;--warn:#d0b06a}
[data-theme="sunset"]{--bg:#0d0608;--panel:#1a0f13;--panel2:#2a1820;--line:#3a2028;--txt:#f2e0e6;--muted:#a08090;--accent:#ff7c5c;--accent2:#ff5cbd;--good:#2ecc71;--warn:#f6b73c}
[data-theme="day"]{--bg:#f5f6f9;--panel:#ffffff;--panel2:#eef0f5;--line:#dde1e8;--txt:#1a1d24;--muted:#6a7280;--accent:#3b6dff;--accent2:#7c5cff;--good:#16a34a;--warn:#d97706}
[data-theme="nord"]{--bg:#2e3440;--panel:#3b4252;--panel2:#434c5e;--line:#4c566a;--txt:#eceff4;--muted:#a1abc0;--accent:#88c0d0;--accent2:#b48ead;--good:#a3be8c;--warn:#ebcb8b}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{margin:0;height:100%;background:var(--bg);color:var(--txt);font:14px/1.5 -apple-system,"SF Mono",ui-monospace,monospace;overflow:hidden}
button,select,input{font-family:inherit;-webkit-appearance:none;appearance:none}
a{color:var(--accent);text-decoration:none}
.brand-gradient{background:linear-gradient(90deg,var(--accent),var(--accent2) 60%,#b35cff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.topnav{display:flex;align-items:center;gap:10px;padding:10px 16px;background:linear-gradient(180deg,rgba(20,26,34,.5),rgba(10,14,20,.9));border-bottom:1px solid var(--line);flex-shrink:0;position:relative;z-index:20}
[data-theme="day"] .topnav{background:linear-gradient(180deg,#ffffff,#f5f6f9)}
.menu-btn{padding:8px 10px;background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:9px;cursor:pointer;min-width:44px;min-height:44px;display:inline-flex;align-items:center;justify-content:center}
.menu-btn:hover{border-color:var(--accent);color:var(--accent)}
.brand{flex:1;min-width:0;display:flex;align-items:center;gap:10px}
.brand-logo{width:34px;height:34px;border-radius:9px;object-fit:cover;border:1px solid var(--line);background:#000;flex-shrink:0}
.brand-text{min-width:0;display:flex;flex-direction:column;justify-content:center}
.brand-title{margin:0;font-size:15px;font-weight:800;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;letter-spacing:.3px;line-height:1.15}
.brand-sub{font-size:10px;color:var(--muted);display:block;margin-top:1px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-weight:600}
.brand-sub a{color:var(--accent);font-weight:700}
.theme-btn{padding:8px;background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:9px;cursor:pointer;min-width:44px;min-height:44px;display:inline-flex;align-items:center;justify-content:center}
.theme-btn:hover{border-color:var(--accent);color:var(--accent)}
.drawer-bg{position:fixed;inset:0;background:rgba(0,0,0,.65);backdrop-filter:blur(4px);z-index:200;opacity:0;pointer-events:none;transition:opacity .22s}
.drawer-bg.open{opacity:1;pointer-events:auto}
.drawer{position:fixed;top:0;left:0;bottom:0;width:280px;max-width:85vw;background:var(--panel);border-right:1px solid var(--line);z-index:201;transform:translateX(-100%);transition:transform .22s;display:flex;flex-direction:column;overflow-y:auto}
.drawer.open{transform:translateX(0)}
.drawer-head{padding:18px;border-bottom:1px solid var(--line);background:linear-gradient(180deg,rgba(92,141,255,.08),transparent);display:flex;align-items:center;gap:12px}
.drawer-head img{width:44px;height:44px;border-radius:11px;border:1px solid var(--line);background:#000}
.drawer-head .info{min-width:0;flex:1}
.drawer-head h2{margin:0;font-size:15px;font-weight:800;letter-spacing:.3px;line-height:1.15;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.drawer-head .tg{font-size:11px;color:var(--muted);display:block;margin-top:3px}
.drawer-head .tg a{color:var(--accent);font-weight:700}
.drawer-item{display:flex;align-items:center;gap:12px;padding:14px 18px;cursor:pointer;color:var(--txt);border-left:3px solid transparent;font-weight:600;font-size:13.5px;text-decoration:none}
.drawer-item.active{background:linear-gradient(90deg,rgba(92,141,255,.12),transparent);border-left-color:var(--accent);color:var(--accent)}
.drawer-item svg{flex-shrink:0}
.drawer-foot{margin-top:auto;padding:16px 18px;font-size:10.5px;color:var(--muted);border-top:1px solid var(--line);line-height:1.6}
.drawer-foot a{color:var(--accent)}
.content{flex:1;display:flex;flex-direction:column;overflow:hidden;min-height:0;position:relative}
.page{display:none;flex:1;overflow-y:auto;padding:16px}
.page.active{display:block}
.hero{display:flex;align-items:center;gap:14px;padding:16px;margin:4px 0 6px;background:linear-gradient(135deg,rgba(92,141,255,.12),rgba(124,92,255,.06) 60%,transparent);border:1px solid var(--line);border-radius:16px;position:relative;overflow:hidden}
[data-theme="day"] .hero{background:linear-gradient(135deg,rgba(59,109,255,.08),rgba(124,92,255,.04) 60%,transparent)}
.hero img{width:52px;height:52px;border-radius:12px;background:#fff;border:1px solid var(--line);object-fit:contain;flex-shrink:0}
.hero .h-text{min-width:0;flex:1}
.hero .h-title{font-size:16px;font-weight:800;letter-spacing:.4px;line-height:1.2}
.hero .h-sub{font-size:11.5px;color:var(--muted);margin-top:2px}
.hero .h-sub a{color:var(--accent);font-weight:700}
.search-wrap{padding:10px 0;position:sticky;top:0;background:var(--bg);z-index:5}
.search-wrap input{width:100%;padding:12px 14px;background:var(--panel);border:1px solid var(--line);color:var(--txt);font:inherit;border-radius:10px;min-height:46px;font-size:14px}

/* NEW batch layout */
.batch-list{display:flex;flex-direction:column;gap:14px;padding-bottom:40px}
@media (min-width:800px){.batch-list{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr))}}
.bcard{display:flex;gap:14px;align-items:center;background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:12px;transition:all .2s cubic-bezier(.22,.9,.28,1);cursor:pointer;position:relative;overflow:hidden}
.bcard:hover{border-color:var(--accent);transform:translateY(-1px);box-shadow:0 12px 32px rgba(0,0,0,.35)}
.bcard-img-wrap{width:140px;height:90px;border-radius:11px;flex-shrink:0;position:relative;overflow:hidden;background:#000;border:1px solid rgba(255,255,255,.05)}
[data-theme="day"] .bcard-img-wrap{border-color:rgba(0,0,0,.08)}
.bcard-img-wrap img{width:100%;height:100%;object-fit:cover;display:block}
.bcard-img-wrap.fallback{display:flex;align-items:center;justify-content:center}
.bcard-img-wrap.fallback .mono{font-size:32px;font-weight:800;color:#fff;text-shadow:0 3px 12px rgba(0,0,0,.5);letter-spacing:2px}
.bcard-body{flex:1;min-width:0;display:flex;flex-direction:column;gap:5px}
.bcard-title{font-size:15px;font-weight:700;color:var(--txt);line-height:1.25}
.bcard-meta{font-size:11.5px;color:var(--muted);display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.bcard-meta .chip{padding:2px 8px;border-radius:6px;background:var(--panel2);border:1px solid var(--line);font-weight:600;font-size:10.5px;text-transform:uppercase;letter-spacing:.4px}
.bcard-prog{margin-top:6px;height:4px;background:rgba(255,255,255,.08);border-radius:3px;overflow:hidden}
[data-theme="day"] .bcard-prog{background:rgba(0,0,0,.06)}
.bcard-prog > div{height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));width:0}
.bcard-arrow{color:var(--muted);padding-right:6px;transition:transform .2s}
.bcard:hover .bcard-arrow{color:var(--accent);transform:translateX(3px)}

/* viewer */
.viewer{display:flex;flex-direction:column;height:100%;min-height:0}
.viewer-head{display:flex;align-items:center;gap:10px;padding:10px 16px;background:var(--panel);border-bottom:1px solid var(--line);flex-shrink:0}
.viewer-head .back{padding:8px 10px;background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:8px;cursor:pointer;min-height:40px;min-width:40px;display:inline-flex;align-items:center;justify-content:center}
.viewer-head .back:hover{border-color:var(--accent);color:var(--accent)}
.viewer-head .title{font-size:14px;font-weight:600;color:var(--txt);flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.player-main{flex:1;display:flex;flex-direction:column;overflow:hidden;min-height:0;position:relative}
.player-wrap{flex:1;background:#000;display:flex;align-items:center;justify-content:center;position:relative;min-height:0;overflow:hidden;cursor:pointer}
.player-empty{color:var(--muted);text-align:center;padding:32px;max-width:560px;line-height:1.8}
.player-empty h2{font-size:26px;margin:0 0 16px;font-weight:800}
.player-wrap video{width:100%;height:100%;background:#000;object-fit:contain}
.player-wrap iframe{width:100%;height:100%;border:0;background:#fff}
.controls{background:var(--panel);border-top:1px solid var(--line);padding:10px 14px;flex-shrink:0}
.bottombar{padding:8px 14px;background:var(--panel);border-top:1px solid var(--line);flex-shrink:0;font-size:11.5px;color:var(--muted);display:flex;justify-content:space-between;gap:10px}
.status{padding:3px 10px;background:var(--panel2);border-radius:12px;color:var(--accent);font-weight:600;font-size:11px}
.status.ok{color:var(--good)}
.status.err{color:#ff7a7a}

/* pdf viewer */
.pdf-viewer{width:100%;height:100%;display:flex;flex-direction:column;background:#0a0a0a}
.pdf-toolbar{padding:10px 14px;background:var(--panel2);border-bottom:1px solid var(--line);display:flex;justify-content:space-between;gap:10px;align-items:center;flex-wrap:wrap}
.pdf-toolbar .name{color:var(--txt);font-weight:600;font-size:12.5px;flex:1;min-width:100px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.pdf-actions{display:flex;gap:6px;flex-wrap:wrap}
.pdf-actions a,.pdf-actions button{padding:8px 12px;background:var(--panel2);color:var(--txt);border:1px solid var(--line);border-radius:8px;font:inherit;font-weight:600;font-size:12px;cursor:pointer;min-height:38px;display:inline-flex;align-items:center;gap:5px;text-decoration:none}
.pdf-actions .primary{background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border-color:transparent}
.pdf-frame{flex:1;border:0;background:#fff}

/* cards for about/request/etc */
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:22px;margin-bottom:14px}
.card h2{margin:0 0 12px;font-size:16px;font-weight:700;color:var(--txt);display:flex;align-items:center;gap:10px}
.card p{color:var(--muted);line-height:1.7;margin:8px 0;font-size:13.5px}
.card p b{color:var(--txt)}
.card .btn-row{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}
.btn-link{display:inline-flex;align-items:center;gap:8px;padding:11px 18px;background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border-radius:10px;font-weight:600;font-size:13px;text-decoration:none;min-height:46px}
.btn-ghost{display:inline-flex;align-items:center;gap:8px;padding:11px 18px;background:var(--panel2);color:var(--txt);border:1px solid var(--line);border-radius:10px;font-weight:600;font-size:13px;text-decoration:none;min-height:46px}
.qr-img{width:min(100%,320px);border-radius:14px;border:1px solid var(--line);margin:14px auto 0;display:block;background:#fff;padding:12px}
.upi-box{background:var(--bg);border:1px solid var(--line);border-radius:10px;padding:14px;display:flex;justify-content:space-between;gap:10px;align-items:center;margin-top:14px;flex-wrap:wrap}
.upi-box .id{font:13px monospace;color:var(--accent);word-break:break-all;flex:1;min-width:120px}
.upi-box button{padding:10px 16px;background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border:0;border-radius:9px;font:inherit;font-weight:600;font-size:12.5px;cursor:pointer;min-height:40px}
.dev-hero{text-align:center;padding:20px;background:linear-gradient(180deg,rgba(92,141,255,.1),transparent);border-radius:14px;margin-bottom:14px}
.dev-hero .avatar{width:96px;height:96px;border-radius:50%;background:linear-gradient(135deg,var(--accent),var(--accent2));display:inline-flex;align-items:center;justify-content:center;font-size:42px;font-weight:800;color:#fff;margin-bottom:14px}
.dev-hero h2{margin:0 0 6px;font-size:20px;color:var(--txt)}
.dev-hero .tag{color:var(--muted);font-size:12.5px}

/* modals */
.modal{position:fixed;inset:0;background:rgba(0,0,0,.82);backdrop-filter:blur(8px);display:none;align-items:center;justify-content:center;z-index:999;padding:16px}
.modal.open{display:flex}
.modal .box{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:22px;max-width:600px;width:100%;max-height:90vh;overflow-y:auto}
.modal h2{margin:0 0 6px;font-size:17px}
.modal .sub{color:var(--muted);font-size:12px;margin-bottom:16px}
.modal input{width:100%;padding:12px 14px;background:var(--bg);border:1px solid var(--line);color:var(--accent);font:12px monospace;border-radius:10px;margin-bottom:10px;box-sizing:border-box}
.modal .variant{padding:12px 14px;background:var(--bg);border:1px solid var(--line);border-radius:10px;margin-bottom:8px}
.modal .variant .name{font-weight:600;font-size:13px}
.modal .variant button{padding:10px 16px;background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:8px;cursor:pointer;font:inherit;font-size:12.5px;font-weight:600;min-height:40px}
.modal .close{float:right;background:transparent;border:0;color:var(--muted);font-size:26px;cursor:pointer;min-width:44px;min-height:44px}

/* theme picker */
.theme-picker{position:fixed;top:58px;right:14px;z-index:300;background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:12px;box-shadow:0 24px 60px rgba(0,0,0,.7);display:none;min-width:280px;max-width:92vw}
.theme-picker.open{display:block}
.theme-picker h4{margin:0 0 10px;font-size:12px;text-transform:uppercase;letter-spacing:.8px;color:var(--muted);font-weight:700}
.theme-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:8px}
.theme-swatch{display:flex;align-items:center;gap:10px;padding:10px 12px;background:var(--panel2);border:1px solid var(--line);border-radius:10px;cursor:pointer;font-size:12.5px;font-weight:600;color:var(--txt);transition:all .15s}
.theme-swatch:hover{border-color:var(--accent);transform:translateY(-1px)}
.theme-swatch.cur{border-color:var(--accent);background:rgba(92,141,255,.08)}
.theme-swatch .dot{width:20px;height:20px;border-radius:50%;flex-shrink:0;border:1px solid rgba(255,255,255,.15)}

@media (max-width:900px){.sections-overlay{width:88vw}}
</style>
</head>
<body>
<div style="height:100vh;height:100dvh;display:flex;flex-direction:column">
  <div class="topnav">
    <button class="menu-btn" onclick="openDrawer()" id="menu-btn" title="Menu"></button>
    <div class="brand">
      <img class="brand-logo" src="https://i.ibb.co/GQvZNJ5x/file-00000000a2d082088bb8b30c95b7d8b9.png" alt="logo">
      <div class="brand-text">
        <h1 class="brand-title brand-gradient">𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚</h1>
        <span class="brand-sub">📚 Free Study · <a href="https://t.me/SeongEraStudy" target="_blank">t.me/SeongEraStudy</a></span>
      </div>
    </div>
    <button class="theme-btn" onclick="toggleThemePicker()" id="palette-btn" title="Themes"></button>
  </div>

  <div class="theme-picker" id="theme-picker">
    <h4>Themes</h4>
    <div class="theme-grid" id="theme-grid"></div>
  </div>

  <div class="drawer-bg" id="drawer-bg" onclick="closeDrawer()"></div>
  <div class="drawer" id="drawer">
    <div class="drawer-head">
      <img src="https://i.ibb.co/GQvZNJ5x/file-00000000a2d082088bb8b30c95b7d8b9.png" alt="logo">
      <div class="info">
        <h2 class="brand-gradient">𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚</h2>
        <span class="tg">📚 Free study · Made By <a href="https://t.me/Seong_Era" target="_blank">@Seong_Era</a></span>
      </div>
    </div>
    <div class="drawer-item active" data-page="batches" onclick="goPage('batches')"><span class="ico" data-icon="book"></span><span>All Batches</span></div>
    <div class="drawer-item" data-page="request" onclick="goPage('request')"><span class="ico" data-icon="plus"></span><span>Request a Batch</span></div>
    <a class="drawer-item" href="https://t.me/SeongEraStudy" target="_blank"><span class="ico" data-icon="message"></span><span>Join Telegram</span></a>
    <div class="drawer-item" data-page="contact" onclick="goPage('contact')"><span class="ico" data-icon="mail"></span><span>Contact Us</span></div>
    <div class="drawer-item" data-page="donate" onclick="goPage('donate')"><span class="ico" data-icon="heart"></span><span>Donate</span></div>
    <div class="drawer-item" data-page="developer" onclick="goPage('developer')"><span class="ico" data-icon="code"></span><span>Developer Info</span></div>
    <div class="drawer-foot">Made By <a href="https://t.me/Seong_Era" target="_blank">@Seong_Era</a><br>Channel: <a href="https://t.me/SeongEraStudy" target="_blank">t.me/SeongEraStudy</a></div>
  </div>

  <div class="content">
    <div class="page active" id="page-batches">
      <div class="hero">
        <img src="https://i.ibb.co/7d6VkR0g/apna-college-icon-filled-256.png" alt="Apna College">
        <div class="h-text">
          <div class="h-title brand-gradient">𝐀𝐩𝐧𝐚 𝐂𝐨𝐥𝐥𝐞𝐠𝐞</div>
          <div class="h-sub">All batches · Free forever · <a href="https://t.me/SeongEraStudy" target="_blank">t.me/SeongEraStudy</a></div>
        </div>
      </div>
      <div class="search-wrap"><input id="batch-search" placeholder="🔍 Search batches…"></div>
      <div class="batch-list" id="batch-list"><div style="padding:24px;color:var(--muted);text-align:center">loading…</div></div>
    </div>

    <div class="page" id="page-viewer">
      <div class="viewer">
        <div class="viewer-head">
          <button class="back" onclick="closeBatch()" data-icon="arrow-left"></button>
          <button class="back" onclick="toggleSections()" data-icon="list" title="playlist"></button>
          <div class="title" id="viewer-title">Batch</div>
        </div>
        <div class="player-main">
          <div class="player-wrap" id="player-wrap">
            <div class="player-empty">
              <h2 class="brand-gradient">Pick a lecture</h2>
              <p>Open the playlist panel with the list icon to browse lectures.</p>
            </div>
          </div>
          <div class="controls" id="controls" style="display:none"></div>
          <div class="bottombar">
            <span class="status" id="status">ready</span>
            <span id="nowplaying"></span>
          </div>
        </div>
      </div>
    </div>

    <div class="page" id="page-request"><div class="card"><h2><span data-icon="plus"></span> Request a Batch</h2><p>Want a new batch added? Message me on Telegram with the batch name or link.</p><div class="btn-row"><a class="btn-link" href="https://t.me/Seong_Era" target="_blank">💬 Message @Seong_Era</a><a class="btn-ghost" href="https://t.me/SeongEraStudy" target="_blank">📢 Join Channel</a></div></div></div>

    <div class="page" id="page-contact">
      <div class="card"><h2><span data-icon="mail"></span> Contact Us</h2><p>Any issue or feedback — reach out on Telegram.</p><div class="btn-row"><a class="btn-link" href="https://t.me/Seong_Era" target="_blank">💬 @Seong_Era</a><a class="btn-ghost" href="https://t.me/SeongEraStudy" target="_blank">📢 Study Channel</a></div></div>
      <div class="card"><h2>Common stuff</h2><p><b>Video won't load:</b> reload.</p><p><b>Wrong quality:</b> pick a lower resolution.</p><p><b>Download:</b> hit the download icon in the player.</p></div>
    </div>

    <div class="page" id="page-donate">
      <div class="card"><h2><span data-icon="heart"></span> Support 𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚</h2><p>If this helped you, even a small amount keeps it alive for everyone.</p><p><b>Thank you for the support — it means a lot. 🙏</b></p><img class="qr-img" src="__QR_IMAGE__" alt="UPI QR"><div class="upi-box"><span class="id" id="upi-id">__UPI_ID__</span><button onclick="copyUpi(this)">📋 copy UPI ID</button></div><p style="margin-top:16px;color:var(--warn);font-weight:600">📸 After donation, kindly send the payment screenshot to the owner on Telegram.</p><div class="btn-row"><a class="btn-link" href="https://t.me/SeongEra" target="_blank">💬 Send Screenshot</a></div></div>
      <div class="card"><h2>Where it goes</h2><p>• Server + domain costs</p><p>• New batches, more lectures</p><p>• Keeping it free for everyone</p></div>
    </div>

    <div class="page" id="page-developer">
      <div class="dev-hero"><div class="avatar">GP</div><h2 class="brand-gradient">Gopal Parmar</h2><div class="tag">Reverse Engineer · Developer · Bug Bounty Hunter</div></div>
      <div class="card"><h2><span data-icon="code"></span> Developer Info</h2><p><b>Name:</b> Gopal Parmar</p><p><b>Skills:</b> Reverse Engineering · Coding · Exploiting · Bug Bounty</p><p><b>Age:</b> Why?? you want to know 🥹🥸🥲</p><p><b>State:</b> Rajasthan 🫶❤️‍🩹</p><p><b>Telegram:</b> <a href="https://t.me/SeongEra">@SeongEra</a></p><div class="btn-row"><a class="btn-link" href="https://t.me/SeongEra" target="_blank">💬 Message @SeongEra</a><a class="btn-ghost" href="https://t.me/SeongEraStudy" target="_blank">📢 Study Channel</a></div></div>
      <div class="card"><h2>About the project</h2><p>𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚 is a free study platform built for students. No ads, no paywall, no signup.</p><p style="color:var(--muted);font-size:12px">Made with care in Rajasthan.</p></div>
    </div>
  </div>
</div>

<div class="sections-overlay" id="sections-overlay">
  <div class="sections-head">
    <img src="https://i.ibb.co/GQvZNJ5x/file-00000000a2d082088bb8b30c95b7d8b9.png" alt="logo" style="width:28px;height:28px;border-radius:8px;background:#000;border:1px solid var(--line)">
    <h3 id="sections-title">Sections</h3>
    <button class="close-sec" onclick="toggleSections()" data-icon="x"></button>
  </div>
  <div class="search2"><input id="search" placeholder="search units…"></div>
  <div class="toc" id="toc"></div>
</div>

<div class="modal" id="modal-dl"><div class="box"><button class="close" onclick="closeModal('modal-dl')">×</button><h2>Download</h2><div class="sub">Downloads directly to your device</div><div class="variants" id="dl-variants"></div></div></div>
<div class="modal" id="modal-link"><div class="box"><button class="close" onclick="closeModal('modal-link')">×</button><h2>Direct m3u8 links</h2><div class="sub">Paste into VLC, mpv, yt-dlp</div><input id="link-master" readonly onclick="this.select()"><button onclick="copyField('link-master',this)" style="padding:12px 18px;background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border:0;border-radius:10px;font:inherit;font-weight:600;cursor:pointer;margin-bottom:16px;width:100%">copy master</button><div class="variants" id="link-variants"></div></div></div>

<script src="https://cdn.jsdelivr.net/npm/hls.js@1"></script>
<script>
__PLAYER_JS__
</script>
</body></html>"""

MAIN_PAGE = _MAIN_HTML.replace("__PLAYER_CSS__", PLAYER_CSS).replace("__PLAYER_JS__", PLAYER_JS)
