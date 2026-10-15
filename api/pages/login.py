"""Admin login page."""

LOGIN_PAGE = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Admin · 𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚</title>
<link rel="icon" href="https://i.ibb.co/GQvZNJ5x/file-00000000a2d082088bb8b30c95b7d8b9.png">
<style>
body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;background:#07090c;color:#e6e9ee;font:14px -apple-system,monospace;padding:20px}
.card{background:#0e1218;border:1px solid #1e2630;border-radius:16px;padding:32px 28px;width:100%;max-width:420px;box-shadow:0 24px 60px rgba(0,0,0,.55)}
.logo{width:64px;height:64px;border-radius:14px;display:block;margin:0 auto 14px;background:#000;border:1px solid #1e2630}
h1{margin:0 0 6px;font-size:22px;text-align:center;background:linear-gradient(90deg,#5c8dff,#7c5cff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.sub{color:#7c8697;font-size:11.5px;text-align:center;margin-bottom:26px}
.sub a{color:#5c8dff;text-decoration:none}
label{display:block;font-size:11px;color:#7c8697;text-transform:uppercase;letter-spacing:.6px;margin:16px 0 6px;font-weight:600}
input{width:100%;padding:13px 14px;background:#07090c;border:1px solid #1e2630;color:#e6e9ee;font:inherit;border-radius:10px;min-height:48px;font-size:15px;letter-spacing:3px;text-align:center;box-sizing:border-box}
input:focus{outline:none;border-color:#5c8dff}
button{margin-top:22px;width:100%;padding:15px;background:linear-gradient(90deg,#5c8dff,#7c5cff);color:#fff;border:0;border-radius:10px;font:inherit;font-weight:700;cursor:pointer;min-height:50px;font-size:15px}
.err{margin-top:16px;padding:12px 14px;background:rgba(255,92,92,.1);border:1px solid rgba(255,92,92,.3);border-radius:8px;color:#ff8b8b;font-size:12.5px}
.foot{margin-top:22px;text-align:center;color:#7c8697;font-size:11px}
</style></head><body>
<form class="card" method="POST" action="/admin">
  <img class="logo" src="https://i.ibb.co/GQvZNJ5x/file-00000000a2d082088bb8b30c95b7d8b9.png" alt="logo">
  <h1>𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚</h1>
  <p class="sub">Admin · <a href="https://t.me/SeongEraStudy" target="_blank">t.me/SeongEraStudy</a></p>
  <label>Admin Code</label>
  <input type="password" name="code" required autofocus autocomplete="off" inputmode="numeric" maxlength="8" pattern="[0-9]{8}" placeholder="••••••••">
  {% if error %}<div class="err">{{ error }}</div>{% endif %}
  <button type="submit">Unlock</button>
</form></body></html>"""
