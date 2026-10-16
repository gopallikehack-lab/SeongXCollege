"""Maintenance page template."""

MAINTENANCE_PAGE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Maintenance · 𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚</title>
<link rel="icon" href="https://i.ibb.co/GQvZNJ5x/file-00000000a2d082088bb8b30c95b7d8b9.png">
<style>
:root{--bg:#07090c;--panel:#0e1218;--line:#1e2630;--txt:#e6e9ee;--muted:#7c8697;--accent:#5c8dff;--accent2:#7c5cff}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{margin:0;min-height:100vh;background:var(--bg);color:var(--txt);font:14px/1.6 -apple-system,"SF Mono",ui-monospace,monospace;overflow-x:hidden}
body{display:flex;align-items:center;justify-content:center;padding:24px;position:relative}
body::before{content:"";position:fixed;inset:0;background:radial-gradient(circle at 20% 20%,rgba(92,141,255,.12),transparent 45%),radial-gradient(circle at 80% 80%,rgba(124,92,255,.1),transparent 45%);pointer-events:none;z-index:0}
.wrap{position:relative;z-index:1;max-width:560px;width:100%;text-align:center}
.logo{width:72px;height:72px;border-radius:18px;border:1px solid var(--line);background:#000;object-fit:cover;display:block;margin:0 auto 22px;box-shadow:0 12px 40px rgba(0,0,0,.55)}
.title{font-size:26px;font-weight:800;letter-spacing:.4px;line-height:1.2;background:linear-gradient(90deg,var(--accent),var(--accent2) 60%,#b35cff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin:0 0 10px}
.sub{color:var(--muted);font-size:13.5px;margin:0 0 28px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:26px 22px;margin-bottom:18px;box-shadow:0 24px 60px rgba(0,0,0,.5)}
.card h2{margin:0 0 10px;font-size:15px;color:#dfe6f0;font-weight:700}
.card p{margin:0;color:var(--muted);font-size:13px;line-height:1.7}
.gear{display:inline-block;font-size:52px;line-height:1;margin-bottom:14px;animation:spin 4s linear infinite;transform-origin:50% 55%}
@keyframes spin{to{transform:rotate(360deg)}}
.bar{height:6px;background:var(--line);border-radius:3px;margin-top:20px;overflow:hidden;position:relative}
.bar > div{position:absolute;top:0;left:0;bottom:0;width:30%;background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:3px;animation:slide 1.6s ease-in-out infinite}
@keyframes slide{0%{left:-30%}100%{left:100%}}
.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 22px;background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border-radius:10px;font:inherit;font-weight:700;font-size:13.5px;text-decoration:none;min-height:48px;box-shadow:0 8px 24px rgba(92,141,255,.28);border:0;cursor:pointer}
.btn:hover{filter:brightness(1.1)}
.btn.ghost{background:var(--panel);border:1px solid var(--line);color:var(--txt);box-shadow:none}
.btn.ghost:hover{border-color:var(--accent)}
.btn-row{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:18px}
.foot{margin-top:24px;font-size:11px;color:var(--muted)}
.foot a{color:var(--accent);text-decoration:none}
</style>
</head>
<body>
<div class="wrap">
  <img class="logo" src="https://i.ibb.co/GQvZNJ5x/file-00000000a2d082088bb8b30c95b7d8b9.png" alt="">
  <h1 class="title">We'll be right back</h1>
  <p class="sub">𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚 is under maintenance right now.</p>

  <div class="card">
    <div class="gear">⚙️</div>
    <h2>Updating things behind the scenes</h2>
    <p>The site is being refreshed with new batches, better performance and cleaner UI. Come back in a bit — everything will be ready soon.</p>
    <div class="bar"><div></div></div>
    <div class="btn-row">
      <a class="btn" href="https://t.me/SeongEraStudy" target="_blank">📢 Get updates on Telegram</a>
      <a class="btn ghost" href="javascript:location.reload()">↻ Retry</a>
    </div>
  </div>

  <div class="foot">
    Made By <a href="https://t.me/Seong_Era" target="_blank">@Seong_Era</a> ·
    <a href="https://t.me/SeongEraStudy" target="_blank">t.me/SeongEraStudy</a>
  </div>
</div>
</body>
</html>"""
