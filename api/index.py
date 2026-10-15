#!/usr/bin/env python3
"""
SeongEra_Study — ApnaCollege multi-batch streaming player
Made By @Seong_Era · t.me/Seong_Era
Vercel + Supabase edition.
"""

import json
import os
import re
import secrets
import time
import urllib.parse
from functools import wraps

from flask import Flask, jsonify, make_response, redirect, render_template_string, request

try:
    from curl_cffi import requests as http
    HAVE_CFFI = True
except ImportError:
    import requests as http
    HAVE_CFFI = False

import requests as plain_requests


BASE = "https://www.apnacollege.in"
IMPERSONATE = "chrome124"
TIMEOUT = 25
ADMIN_COOKIE = "se_admin"
TOKEN_TTL = 60 * 60 * 24 * 7
ADMIN_TTL = 60 * 60 * 4
BRAND = "SeongEra_Study 📚✏"
TG_LINK = "https://t.me/Seong_Era"

ADMIN_CODE = os.environ.get("ADMIN_CODE", "12345678")
SUPABASE_URL = (os.environ.get("SUPABASE_URL") or "").rstrip("/")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY") or ""


class SupabaseStore:
    def __init__(self):
        self.url = SUPABASE_URL
        self.key = SUPABASE_KEY
        self.enabled = bool(self.url and self.key)
        self._mem_accounts = []
        self._mem_cache = {}

    def _headers(self, prefer="return=minimal"):
        return {
            "apikey": self.key,
            "Authorization": f"Bearer {self.key}",
            "Content-Type": "application/json",
            "Prefer": prefer,
        }

    def get_accounts(self):
        if not self.enabled:
            return self._mem_accounts
        try:
            r = plain_requests.get(
                f"{self.url}/rest/v1/accounts?select=*&order=added_at.desc",
                headers=self._headers(), timeout=10)
            if r.status_code == 200:
                return r.json()
            print(f"[!] supabase get_accounts status {r.status_code}: {r.text[:200]}")
        except Exception as e:
            print(f"[!] supabase get_accounts: {e}")
        return []

    def add_account(self, email, token, label=""):
        if not self.enabled:
            self._mem_accounts.append({
                "email": email, "token": token, "label": label,
                "added_at": time.time(), "token_updated_at": time.time(),
            })
            return True, "added"
        try:
            r = plain_requests.post(
                f"{self.url}/rest/v1/accounts",
                headers=self._headers(),
                json={"email": email.lower(), "token": token, "label": label},
                timeout=10)
            if r.status_code in (200, 201):
                return True, "added"
            if r.status_code == 409 or "duplicate" in (r.text or "").lower():
                return False, "account already exists"
            return False, f"supabase {r.status_code}: {r.text[:200]}"
        except Exception as e:
            return False, f"{type(e).__name__}: {e}"

    def remove_account(self, email):
        if not self.enabled:
            self._mem_accounts = [a for a in self._mem_accounts
                                  if a.get("email","").lower() != email.lower()]
            return True
        try:
            r = plain_requests.delete(
                f"{self.url}/rest/v1/accounts?email=eq.{urllib.parse.quote(email.lower())}",
                headers=self._headers(), timeout=10)
            return r.status_code in (200, 204)
        except Exception:
            return False

    def cache_get(self, key):
        if not self.enabled:
            v = self._mem_cache.get(key)
            if v and v.get("expires_at", 0) > time.time():
                return v["value"]
            return None
        try:
            r = plain_requests.get(
                f"{self.url}/rest/v1/cache?key=eq.{urllib.parse.quote(key)}&select=value,expires_at",
                headers=self._headers(), timeout=10)
            if r.status_code == 200:
                rows = r.json()
                if rows and rows[0].get("value"):
                    return rows[0]["value"]
        except Exception:
            pass
        return None

    def cache_set(self, key, value, ttl=TOKEN_TTL):
        if not self.enabled:
            self._mem_cache[key] = {"value": value, "expires_at": time.time()+ttl}
            return
        try:
            headers = self._headers(prefer="resolution=merge-duplicates")
            plain_requests.post(
                f"{self.url}/rest/v1/cache",
                headers=headers,
                json={"key": key, "value": value,
                      "expires_at": time.strftime("%Y-%m-%dT%H:%M:%S+00:00",
                                                  time.gmtime(time.time()+ttl))},
                timeout=10)
        except Exception:
            pass


STORE = SupabaseStore()


class ApnaSession:
    def __init__(self, email, token):
        self.email = email.lower()
        self.token = token
        self.s = http.Session(impersonate=IMPERSONATE) if HAVE_CFFI else http.Session()
        cookie_val = urllib.parse.quote(json.dumps({
            "access_token": token, "token_type": "Bearer", "expires_in": TOKEN_TTL,
        }))
        self.s.cookies.set("lw_tokens", cookie_val, domain="www.apnacollege.in")

    def h(self, referer=None):
        return {"Accept":"application/json","Content-Type":"application/json",
                "Origin": BASE, "Referer": referer or f"{BASE}/start",
                "token": self.token or ""}

    def verify(self):
        try:
            r = self.s.get(f"{BASE}/api/user/me", headers=self.h(), timeout=TIMEOUT)
            if r.status_code != 200:
                return False, f"status {r.status_code}"
            if '"username"' not in (r.text or ""):
                return False, "no username"
            return True, "ok"
        except Exception as e:
            return False, f"{type(e).__name__}"

    def fetch_batches(self):
        body = {
            "type": "course",
            "access": "public,private-enroll,soon,view-locked",
            "excludeNotEnrolledPrivateProductsForAdmin": "true",
            "fields": "title,titleId,settings,progress,access,type",
            "owned": "true",
            "sortFields": [{"sortField":"lastVisited","direction":"desc"}],
            "offset": "0", "itemsPerPage": "100", "paginationType": "offset",
        }
        try:
            r = self.s.post(f"{BASE}/api/learner/products", json=body,
                            headers=self.h(), timeout=TIMEOUT)
            d = r.json()
        except Exception:
            return []
        out = []
        for c in d.get("data", []):
            tid, ttl = c.get("titleId"), c.get("title")
            if tid and ttl:
                out.append({"titleId": tid, "label": ttl})
        return out

    def fetch_curriculum(self, titleId):
        cache_key = f"curric:{self.email}:{titleId}"
        cached = STORE.cache_get(cache_key)
        if cached:
            try:
                return json.loads(cached)
            except Exception:
                pass
        try:
            r = self.s.get(f"{BASE}/api/course/{titleId}?contents&path-player",
                           headers=self.h(f"{BASE}/path-player?courseid={titleId}"),
                           timeout=TIMEOUT)
            if r.status_code != 200:
                return None
            d = r.json()
            try:
                compact = {
                    "id": d.get("course",{}).get("id"),
                    "titleId": d.get("course",{}).get("titleId"),
                    "title": d.get("course",{}).get("title"),
                    "sections": d.get("course",{}).get("sections",{}),
                    "objects": d.get("course",{}).get("objects",{}),
                }
                STORE.cache_set(cache_key, json.dumps(compact), ttl=TOKEN_TTL)
            except Exception:
                pass
            return d
        except Exception:
            return None

    def course_internal_id(self, titleId):
        d = self.fetch_curriculum(titleId)
        if not d: return None
        return (d.get("course") or {}).get("id") or d.get("id")

    def fetch_video(self, titleId, unit_id):
        cid = self.course_internal_id(titleId)
        if not cid: return {"error": "no course id"}
        try:
            r = self.s.get(f"{BASE}/api/video/{cid}/{unit_id}",
                headers=self.h(f"{BASE}/path-player?courseid={titleId}&unit={unit_id}Unit"),
                timeout=TIMEOUT)
            if r.status_code != 200:
                return {"error": f"status {r.status_code}"}
            j = r.json()
        except Exception as e:
            return {"error": f"{type(e).__name__}"}
        v = j.get("video") or {}
        if not v and not j.get("success", True):
            fname, disp = self.get_pdf_filename(titleId, unit_id)
            if fname:
                return {"unit_id": unit_id, "title": disp or fname,
                        "type": "pdf", "pdf": fname, "batch": titleId}
        return {
            "unit_id": unit_id,
            "title": v.get("title"),
            "type": v.get("type"),
            "sourceid": v.get("sourceid"),
            "duration": v.get("duration"),
            "vimeo": v.get("vimeoid"),
            "batch": titleId,
        }

    def get_pdf_filename(self, titleId, unit_id):
        d = self.fetch_curriculum(titleId)
        if not d: return (None, None)
        objs = ((d.get("course") or {}).get("objects")) or d.get("objects") or {}
        obj = objs.get(unit_id)
        if not obj: return (None, None)
        data = obj.get("data") or {}
        raw = data.get("pdf") or ""
        fname = raw.split("/", 1)[1] if "/" in raw else raw
        disp = data.get("pdf_name") or obj.get("title") or fname
        return (fname, disp) if fname else (None, None)

    def pdf_redirect(self, titleId, unit_id):
        fname, disp = self.get_pdf_filename(titleId, unit_id)
        if not fname: return {"error": "no pdf in curriculum"}
        try:
            r = self.s.get(f"{BASE}/api/unlock/pdf/{urllib.parse.quote(fname)}",
                params={"courseid": titleId, "unitId": unit_id, "json": ""},
                headers=self.h(f"{BASE}/path-player?courseid={titleId}&unit={unit_id}Unit"),
                timeout=TIMEOUT)
            j = r.json()
        except Exception as e:
            return {"error": f"{type(e).__name__}"}
        url = j.get("redirectUrl")
        if not url: return {"error": "no redirect"}
        return {"redirectUrl": url, "filename": fname, "display": disp}

    def wistia_variants(self, sourceid):
        try:
            r = self.s.get(f"https://fast.wistia.com/embed/medias/{sourceid}.m3u8",
                           timeout=TIMEOUT)
            if r.status_code != 200: return {}
            out = {}
            lines = r.text.splitlines()
            for i, line in enumerate(lines):
                if line.startswith("#EXT-X-STREAM-INF"):
                    m = re.search(r'NAME="([^"]+)"', line)
                    key = m.group(1) if m else f"v{i}"
                    for j in range(i+1, len(lines)):
                        u = lines[j].strip()
                        if u and not u.startswith("#"):
                            if u.startswith("/"):
                                u = f"https://embed-cloudfront.wistia.com{u}"
                            out[key] = u
                            break
            return out
        except Exception:
            return {}


app = Flask(__name__)


def current_admin():
    tok = request.cookies.get(ADMIN_COOKIE)
    if not tok:
        return False
    return STORE.cache_get(f"admin:{tok}") == "1"


def require_admin(f):
    @wraps(f)
    def wrap(*a, **kw):
        if not current_admin():
            return jsonify(error="admin required"), 401
        return f(*a, **kw)
    return wrap


# ================= MAIN PAGE =================
MAIN_PAGE = """<!DOCTYPE html>
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
.site-header{display:flex;justify-content:space-between;align-items:center;padding:12px 18px;background:linear-gradient(180deg,rgba(20,26,34,.6),rgba(10,14,20,.9));border-bottom:1px solid var(--line);flex-shrink:0;flex-wrap:wrap;gap:12px}
.site-brand h1{margin:0;font-size:18px;font-weight:700}
.tg-link{font-size:11px;color:var(--muted);display:inline-block;margin-top:3px}
.site-actions{display:flex;gap:8px;align-items:center}
.btn-nav{padding:9px 15px;background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:9px;font:inherit;font-weight:600;font-size:12.5px;cursor:pointer;min-height:38px;display:inline-flex;align-items:center}
.theme-btn{padding:8px 12px;background:var(--panel2);border:1px solid var(--line);border-radius:9px;cursor:pointer;font-size:16px;min-height:38px}
.tabs{display:flex;gap:8px;padding:12px 18px;overflow-x:auto;background:rgba(10,14,20,.7);border-bottom:1px solid var(--line);flex-shrink:0;scrollbar-width:none;min-height:64px;align-items:center}
.tabs::-webkit-scrollbar{display:none}
.tabs-loading{color:var(--muted);font-size:12px;padding:8px 4px}
.tab{padding:10px 16px;background:transparent;border:1px solid var(--line);color:var(--muted);border-radius:10px;font:inherit;font-weight:600;font-size:12.5px;cursor:pointer;white-space:nowrap;flex-shrink:0;min-height:40px}
.tab:hover{color:var(--txt);border-color:var(--accent)}
.tab.active{color:#fff;background:linear-gradient(90deg,var(--accent),var(--accent2));border-color:transparent}
.tab .badge{font-size:10.5px;background:rgba(0,0,0,.25);padding:2px 7px;border-radius:10px;font-weight:600;margin-left:6px}
.body{flex:1;display:flex;overflow:hidden;min-height:0;position:relative}
.sidebar{width:360px;min-width:360px;background:var(--panel);border-right:1px solid var(--line);display:flex;flex-direction:column;transition:transform .22s ease}
.search{padding:12px 14px;border-bottom:1px solid var(--line);flex-shrink:0}
.search input{width:100%;padding:12px 14px;background:var(--bg);border:1px solid var(--line);color:var(--txt);font:inherit;border-radius:10px;min-height:var(--tap);font-size:14px}
.toc{flex:1;overflow-y:auto;padding-bottom:40px}
.sec{border-bottom:1px solid var(--line)}
.sec-head{padding:14px 16px;cursor:pointer;display:flex;justify-content:space-between;gap:10px;align-items:center;font-weight:600;font-size:13px;color:#c8d0dd;min-height:var(--tap)}
.sec-head.open{background:var(--panel2);color:var(--accent)}
.sec-head .left{flex:1;display:flex;gap:10px;align-items:center;overflow:hidden}
.sec-head .t{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sec-head .cnt{color:var(--muted);font-size:11px;background:var(--panel2);padding:2px 8px;border-radius:10px}
.copy-btn{background:transparent;border:1px solid var(--line);color:var(--muted);border-radius:6px;padding:5px 8px;font-size:11px;cursor:pointer;min-width:32px;min-height:32px;display:inline-flex;align-items:center;justify-content:center}
.copy-btn.copied{border-color:var(--good);color:var(--good)}
.sec-body{display:none;background:rgba(0,0,0,.15)}
.sec-body.open{display:block}
.unit{padding:12px 16px 12px 26px;cursor:pointer;font-size:13px;color:#a8b3c2;border-left:3px solid transparent;display:flex;justify-content:space-between;gap:10px;align-items:center;min-height:var(--tap)}
.unit:hover{background:var(--panel2);color:var(--txt)}
.unit.active{background:linear-gradient(90deg,rgba(92,141,255,.12),transparent);color:var(--accent);border-left-color:var(--accent)}
.unit .u-left{flex:1;display:flex;gap:8px;align-items:center;overflow:hidden}
.unit .u-left .t{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.unit .right{display:flex;gap:6px;align-items:center}
.unit .type{padding:2px 8px;border-radius:8px;font-size:10px;background:var(--panel2);color:var(--muted);font-weight:600;text-transform:uppercase}
.main{flex:1;display:flex;flex-direction:column;overflow:hidden;min-width:0}
.topbar{display:flex;justify-content:space-between;gap:12px;align-items:center;padding:12px 18px;background:var(--panel);border-bottom:1px solid var(--line)}
.topbar .title{font-size:14px;font-weight:600;color:#dfe6f0;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.topbar .nav{display:flex;gap:6px}
.topbar button{padding:9px 14px;background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:9px;cursor:pointer;font:inherit;font-weight:600;min-height:38px;font-size:14px;min-width:44px}
.mobile-toggle{display:none}
.player-wrap{flex:1;background:#000;display:flex;align-items:center;justify-content:center;position:relative;min-height:0;overflow:hidden}
.player-empty{color:var(--muted);text-align:center;padding:32px;max-width:560px;line-height:1.8}
.player-empty h2{font-size:26px;margin:0 0 16px;font-weight:800}
.player-wrap video{width:100%;height:100%;background:#000;object-fit:contain}
.controls{background:var(--panel);border-top:1px solid var(--line);padding:12px 16px;flex-shrink:0}
.ctr-row{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.controls button{background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:9px;padding:8px;cursor:pointer;min-height:var(--tap);min-width:var(--tap);font-size:15px;display:inline-flex;align-items:center;justify-content:center}
.controls .time{font-size:12px;color:var(--muted);min-width:104px;text-align:center}
.seekbar{flex:1;height:8px;background:var(--panel2);border-radius:4px;position:relative;cursor:pointer;min-width:100px}
.seekbar .filled{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--accent),var(--accent2));width:0%}
.seekbar .knob{position:absolute;top:50%;left:0;width:16px;height:16px;border-radius:50%;background:#fff;transform:translate(-50%,-50%)}
.controls select{background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:9px;padding:8px 10px;font:inherit;font-size:13px;min-height:var(--tap)}
.bottombar{padding:10px 18px;background:var(--panel);border-top:1px solid var(--line);flex-shrink:0;font-size:11.5px;color:var(--muted)}
.status{padding:4px 11px;background:var(--panel2);border-radius:12px;color:var(--accent);border:1px solid rgba(92,141,255,.2);font-size:11.5px;font-weight:600}
.status.ok{color:var(--good)}
.status.err{color:#ff7a7a}
.pdf-viewer{width:100%;height:100%;display:flex;flex-direction:column;background:#0a0a0a}
.pdf-toolbar{padding:10px 16px;background:var(--panel2);border-bottom:1px solid var(--line);display:flex;justify-content:space-between;gap:12px;align-items:center;flex-wrap:wrap}
.pdf-toolbar .name{color:#dfe6f0;font-weight:600;font-size:13px;flex:1;min-width:120px}
.pdf-actions{display:flex;gap:8px;flex-wrap:wrap}
.pdf-actions a,.pdf-actions button{padding:9px 14px;background:var(--panel2);color:var(--txt);border:1px solid var(--line);border-radius:9px;font:inherit;font-weight:600;font-size:12.5px;cursor:pointer;min-height:38px;display:inline-flex;align-items:center;gap:6px;text-decoration:none}
.pdf-actions .primary{background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border-color:transparent}
.pdf-frame{flex:1;border:0;background:#fff}
.modal{position:fixed;inset:0;background:rgba(0,0,0,.8);backdrop-filter:blur(6px);display:none;align-items:center;justify-content:center;z-index:999;padding:16px}
.modal.open{display:flex}
.modal .box{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:24px;max-width:600px;width:100%;max-height:90vh;overflow-y:auto}
.modal h2{margin:0 0 6px;font-size:17px}
.modal .sub{color:var(--muted);font-size:12px;margin-bottom:16px}
.modal input{width:100%;padding:12px 14px;background:var(--bg);border:1px solid var(--line);color:var(--accent);font:12px monospace;border-radius:10px;margin-bottom:10px;box-sizing:border-box}
.modal .variant{padding:12px 14px;background:var(--bg);border:1px solid var(--line);border-radius:10px;margin-bottom:8px}
.modal .variant .name{font-weight:600;font-size:13px}
.modal .variant button{padding:10px 16px;background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:8px;cursor:pointer;font:inherit;font-size:12.5px;font-weight:600;min-height:40px}
.modal .close{float:right;background:transparent;border:0;color:var(--muted);font-size:26px;cursor:pointer;min-width:44px;min-height:44px}
@media (max-width:900px){
  .sidebar{position:absolute;top:0;left:0;bottom:0;width:85vw;max-width:340px;z-index:15;transform:translateX(-100%);box-shadow:12px 0 40px rgba(0,0,0,.6)}
  .sidebar.open{transform:translateX(0)}
  .mobile-toggle{display:inline-flex}
}
</style></head><body>
<div style="height:100vh;height:100dvh;display:flex;flex-direction:column">
  <header class="site-header">
    <div class="site-brand">
      <h1 class="brand-gradient">SeongEra_Study 📚✏</h1>
      <a class="tg-link" href="https://t.me/Seong_Era" target="_blank">Telegram · t.me/Seong_Era</a>
    </div>
    <div class="site-actions">
      <button class="theme-btn" onclick="cycleTheme()">🎨</button>
      <a href="/admin" class="btn-nav">Admin</a>
    </div>
  </header>
  <div class="tabs" id="tabs"><div class="tabs-loading">loading batches…</div></div>
  <div class="body">
    <aside class="sidebar" id="sidebar">
      <div class="search"><input id="search" placeholder="search units…"></div>
      <div class="toc" id="toc"></div>
    </aside>
    <main class="main">
      <div class="topbar">
        <button class="mobile-toggle btn-nav" onclick="toggleSidebar()">☰</button>
        <div class="title" id="unit-title">Welcome</div>
        <div class="nav"><button onclick="playPrev()">‹</button><button onclick="playNext()">›</button></div>
      </div>
      <div class="player-wrap" id="player-wrap">
        <div class="player-empty">
          <h2 class="brand-gradient">SeongEra_Study</h2>
          <p>Pick a batch above, then a lecture.</p>
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
      <div class="bottombar"><span class="status" id="status">ready</span></div>
    </main>
  </div>
</div>
<div class="modal" id="modal-dl"><div class="box"><button class="close" onclick="closeModal('modal-dl')">×</button><h2>Download</h2><div class="sub">Downloads directly to your device</div><div class="variants" id="dl-variants"></div></div></div>
<div class="modal" id="modal-link"><div class="box"><button class="close" onclick="closeModal('modal-link')">×</button><h2>Direct m3u8 links</h2><div class="sub">Paste into VLC, mpv, yt-dlp</div><input id="link-master" readonly onclick="this.select()"><button onclick="copyField('link-master',this)" style="padding:12px 18px;background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border:0;border-radius:10px;font:inherit;font-weight:600;cursor:pointer;margin-bottom:16px;width:100%">copy master</button><div class="variants" id="link-variants"></div></div></div>
<script src="https://cdn.jsdelivr.net/npm/hls.js@1"></script>
<script>
console.log('[SE] main script loaded');
let BATCHES=[],ACTIVE=null,FLAT=[],CURRENT=null,CURRENT_INFO=null,HLS=null,VIDEO=null,CURRENT_VARIANTS={};
const THEMES=["default","rose","green","amber","crimson","cyber","mono","sunset"];
let curTheme=localStorage.getItem("theme")||"default";
document.documentElement.setAttribute("data-theme",curTheme);
function cycleTheme(){let i=THEMES.indexOf(curTheme);i=(i+1)%THEMES.length;curTheme=THEMES[i];document.documentElement.setAttribute("data-theme",curTheme);localStorage.setItem("theme",curTheme);}
function esc(s){return String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]))}
async function loadAll(){
  console.log('[SE] loadAll start');
  const tabs=document.getElementById('tabs');
  tabs.innerHTML='<div class="tabs-loading">loading batches…</div>';
  try{
    const r=await fetch('/api/batches');
    console.log('[SE] /api/batches status:', r.status);
    const j=await r.json();
    console.log('[SE] /api/batches response:', j);
    BATCHES=j.batches||[];
    console.log('[SE] batches count:', BATCHES.length);
    if(!BATCHES.length){
      tabs.innerHTML='<div class="tabs-loading">no batches — add accounts in /admin</div>';
      document.getElementById('toc').innerHTML='<div style="padding:24px;color:var(--muted);text-align:center">No batches. Add tokens in /admin.</div>';
      return;
    }
    renderTabs();
    console.log('[SE] tabs rendered, selecting first batch:', BATCHES[0].titleId);
    selectBatch(BATCHES[0].titleId);
  }catch(e){
    console.error('[SE] loadAll error:', e);
    tabs.innerHTML=`<div class="tabs-loading" style="color:#ff7a7a">error: ${esc(e.message||String(e))}</div>`;
  }
}
function renderTabs(){
  const tabs=document.getElementById('tabs');
  tabs.innerHTML='';
  for(const b of BATCHES){
    const t=document.createElement('button');
    t.className='tab'+(ACTIVE===b.titleId?' active':'');
    t.textContent=b.label;
    t.onclick=()=>selectBatch(b.titleId);
    tabs.appendChild(t);
  }
}
async function selectBatch(titleId){
  console.log('[SE] selectBatch:', titleId);
  ACTIVE=titleId;renderTabs();
  document.getElementById('search').value='';
  document.getElementById('toc').innerHTML='<div style="padding:24px;color:var(--muted)">loading…</div>';
  try{
    const r=await fetch(`/api/sections/${titleId}`);
    const j=await r.json();
    console.log('[SE] sections response:', j);
    if(!j.sections){
      document.getElementById('toc').innerHTML=`<div style="padding:24px;color:#ff7a7a">${esc(j.error||'failed')}</div>`;
      return;
    }
    window._sections=j.sections;
    renderTOC();
  }catch(e){
    console.error('[SE] selectBatch error:', e);
    document.getElementById('toc').innerHTML=`<div style="padding:24px;color:#ff7a7a">error: ${esc(e.message||String(e))}</div>`;
  }
}
function renderTOC(){
  const toc=document.getElementById('toc');toc.innerHTML='';FLAT=[];
  const q=document.getElementById('search').value.toLowerCase();
  for(const sec of (window._sections||[])){
    const units=sec.units.filter(u=>!q||(u.title||'').toLowerCase().includes(q));
    if(q&&units.length===0)continue;
    const secDiv=document.createElement('div');secDiv.className='sec';
    const head=document.createElement('div');head.className='sec-head'+(q?' open':'');
    const st=esc(sec.title).replace(/'/g,"\\'");
    head.innerHTML=`<div class="left"><span class="t">${esc(sec.title)}</span></div><span class="cnt">${sec.units.length}</span><button class="copy-btn" onclick="event.stopPropagation();copyTitle(this,'${st}')">📋</button>`;
    head.onclick=()=>{head.classList.toggle('open');body.classList.toggle('open');};
    const body=document.createElement('div');body.className='sec-body'+(q?' open':'');
    for(const u of units){
      const idx=FLAT.length;FLAT.push({unit:u,sectionTitle:sec.title});
      const uDiv=document.createElement('div');uDiv.className='unit';uDiv.dataset.idx=idx;
      const st2=esc(u.title||u.id).replace(/'/g,"\\'");
      uDiv.innerHTML=`<div class="u-left"><span class="t">${esc(u.title||u.id)}</span></div><span class="right"><span class="type ${u.type}">${u.type}</span><button class="copy-btn" onclick="event.stopPropagation();copyTitle(this,'${st2}')">📋</button></span>`;
      uDiv.onclick=()=>playUnit(idx);body.appendChild(uDiv);
    }
    secDiv.appendChild(head);secDiv.appendChild(body);toc.appendChild(secDiv);
  }
  console.log('[SE] TOC rendered, total units:', FLAT.length);
}
function copyTitle(btn,title){navigator.clipboard.writeText(title).then(()=>{const o=btn.textContent;btn.textContent='✓';btn.classList.add('copied');setTimeout(()=>{btn.textContent=o;btn.classList.remove('copied');},1000);});}
async function playUnit(idx){
  if(idx<0||idx>=FLAT.length)return;CURRENT=idx;
  const item=FLAT[idx];const u=item.unit;
  document.querySelectorAll('.unit.active').forEach(el=>el.classList.remove('active'));
  const el=document.querySelector(`.unit[data-idx="${idx}"]`);
  if(el){el.classList.add('active');el.scrollIntoView({block:'nearest',behavior:'smooth'});}
  document.getElementById('unit-title').textContent=u.title;
  document.getElementById('status').textContent='loading…';document.getElementById('status').className='status';
  document.getElementById('controls').style.display='none';destroyPlayer();
  const r=await fetch(`/api/video/${ACTIVE}/${u.id}`);const j=await r.json();CURRENT_INFO=j;
  if(j.error){document.getElementById('player-wrap').innerHTML=`<div class="player-empty"><p>error: ${esc(j.error)}</p></div>`;document.getElementById('status').textContent='error';document.getElementById('status').className='status err';return;}
  if(j.type==='wistia'&&j.sourceid)await playWistia(j.sourceid);
  else if(j.type==='pdf')await playPdf(ACTIVE,u.id);
  else document.getElementById('player-wrap').innerHTML=`<div class="player-empty"><p>unsupported: ${esc(j.type||'?')}</p></div>`;
  if(window.innerWidth<=900)document.getElementById('sidebar').classList.remove('open');
}
function destroyPlayer(){if(HLS){try{HLS.destroy();}catch(e){}HLS=null;}if(VIDEO){try{VIDEO.pause();}catch(e){}VIDEO=null;}}
async function playWistia(sourceid){const master=`https://fast.wistia.com/embed/medias/${sourceid}.m3u8`;document.getElementById('player-wrap').innerHTML='<video id="v" playsinline preload="metadata"></video>';VIDEO=document.getElementById('v');document.getElementById('controls').style.display='block';try{const r=await fetch(`/api/variants/${sourceid}`);const j=await r.json();CURRENT_VARIANTS=j.variants||{};}catch(e){CURRENT_VARIANTS={};}if(window.Hls&&Hls.isSupported()){HLS=new Hls({capLevelToPlayerSize:false,startLevel:-1,autoStartLoad:true,maxBufferLength:60});HLS.loadSource(master);HLS.attachMedia(VIDEO);HLS.on(Hls.Events.MANIFEST_PARSED,(e,data)=>{const sel=document.getElementById('quality');sel.innerHTML='<option value="auto">auto</option>';data.levels.forEach((lvl,i)=>{const o=document.createElement('option');o.value=i;o.textContent=lvl.height?`${lvl.height}p`:`L${i}`;sel.appendChild(o);});VIDEO.play().catch(()=>{});});HLS.on(Hls.Events.LEVEL_SWITCHED,(e,data)=>{const lvl=HLS.levels[data.level];if(lvl){document.getElementById('status').textContent=`playing · ${lvl.height||'?'}p`;document.getElementById('status').className='status ok';}});}else if(VIDEO.canPlayType('application/vnd.apple.mpegurl')){VIDEO.src=master;VIDEO.play().catch(()=>{});}VIDEO.addEventListener('timeupdate',updateTime);VIDEO.addEventListener('loadedmetadata',updateTime);VIDEO.addEventListener('play',()=>document.getElementById('btn-play').textContent='❚❚');VIDEO.addEventListener('pause',()=>document.getElementById('btn-play').textContent='▶');VIDEO.addEventListener('click',togglePlay);document.getElementById('status').textContent='playing';}
async function playPdf(titleId,unitId){document.getElementById('player-wrap').innerHTML='<div class="player-empty">loading PDF…</div>';let info;try{const r=await fetch(`/api/pdf/${titleId}/${unitId}`);info=await r.json();}catch(e){return;}if(info.error){document.getElementById('player-wrap').innerHTML=`<div class="player-empty"><p>PDF error: ${esc(info.error)}</p></div>`;return;}window._pdfInfo=info;document.getElementById('player-wrap').innerHTML=`<div class="pdf-viewer"><div class="pdf-toolbar"><span class="name">📄 ${esc(info.display||info.filename)}</span><div class="pdf-actions"><a href="${esc(info.redirectUrl)}" download="${esc(info.filename)}" target="_blank" class="primary">⬇ download</a><button onclick="pdfCopyUrl(this)">🔗 copy</button><button onclick="pdfNewTab()">↗ new tab</button></div></div><iframe class="pdf-frame" src="${esc(info.redirectUrl)}"></iframe></div>`;document.getElementById('status').textContent='pdf';document.getElementById('status').className='status ok';}
function pdfNewTab(){if(window._pdfInfo&&window._pdfInfo.redirectUrl)window.open(window._pdfInfo.redirectUrl,'_blank');}
async function pdfCopyUrl(btn){const item=FLAT[CURRENT];try{const r=await fetch(`/api/pdf/${ACTIVE}/${item.unit.id}`);const info=await r.json();if(info.redirectUrl){await navigator.clipboard.writeText(info.redirectUrl);const o=btn.textContent;btn.textContent='✓';setTimeout(()=>btn.textContent=o,1200);}}catch(e){}}
function updateTime(){if(!VIDEO)return;const cur=VIDEO.currentTime||0,dur=VIDEO.duration||0;document.getElementById('time').textContent=fmt(cur)+' / '+fmt(dur);const pct=dur?(cur/dur)*100:0;document.getElementById('seek-filled').style.width=pct+'%';document.getElementById('seek-knob').style.left=pct+'%';}
function fmt(s){s=Math.floor(s||0);const h=Math.floor(s/3600),m=Math.floor((s%3600)/60),r=s%60;return h?`${h}:${String(m).padStart(2,'0')}:${String(r).padStart(2,'0')}`:`${m}:${String(r).padStart(2,'0')}`;}
function togglePlay(){if(VIDEO)VIDEO.paused?VIDEO.play():VIDEO.pause();}
function skip(n){if(VIDEO)VIDEO.currentTime+=n;}
function seekClick(e){if(!VIDEO)return;const r=e.currentTarget.getBoundingClientRect();VIDEO.currentTime=((e.clientX-r.left)/r.width)*(VIDEO.duration||0);}
function setSpeed(v){if(VIDEO)VIDEO.playbackRate=parseFloat(v);}
function onQualityChange(v){if(HLS)HLS.currentLevel=(v==='auto')?-1:parseInt(v,10);}
function toggleFS(){const w=document.getElementById('player-wrap');if(!document.fullscreenElement)w.requestFullscreen();else document.exitFullscreen();}
function playNext(){if(CURRENT!=null&&CURRENT<FLAT.length-1)playUnit(CURRENT+1);}
function playPrev(){if(CURRENT!=null&&CURRENT>0)playUnit(CURRENT-1);}
function toggleSidebar(){document.getElementById('sidebar').classList.toggle('open');}
function openDownload(){if(!CURRENT_INFO)return;if(CURRENT_INFO.type==='pdf'){const a=document.querySelector('.pdf-actions a.primary');if(a)a.click();return;}const box=document.getElementById('dl-variants');box.innerHTML='';const items=Object.entries(CURRENT_VARIANTS).sort((a,b)=>parseInt(b[0])-parseInt(a[0]));if(!items.length){box.innerHTML='<p style="color:var(--muted)">no variants</p>';document.getElementById('modal-dl').classList.add('open');return;}const best=document.createElement('div');best.className='variant';best.style.borderColor='var(--accent)';best.innerHTML=`<div style="display:flex;justify-content:space-between;align-items:center;gap:10px"><span class="name">Best available</span><button onclick="browserHlsDownload('${esc(items[0][1])}','${esc((CURRENT_INFO.title||'video').replace(/'/g,''))}','${esc(items[0][0])}')" style="background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border-color:transparent">download</button></div>`;box.appendChild(best);for(const [q,url] of items){const el=document.createElement('div');el.className='variant';el.innerHTML=`<div style="display:flex;justify-content:space-between;align-items:center;gap:10px"><span class="name">${esc(q)}</span><button onclick="browserHlsDownload('${esc(url)}','${esc((CURRENT_INFO.title||'video').replace(/'/g,''))}','${esc(q)}')">download</button></div>`;box.appendChild(el);}document.getElementById('modal-dl').classList.add('open');}
async function browserHlsDownload(masterUrl,title,quality){closeModal('modal-dl');const status=document.getElementById('status');status.textContent='download starting…';try{const m=await fetch(masterUrl).then(r=>r.text());const lines=m.split(/\r?\n/);const base=masterUrl.substring(0,masterUrl.lastIndexOf('/')+1);const segs=[];for(const line of lines){const t=line.trim();if(!t||t.startsWith('#'))continue;let abs=t;if(!t.startsWith('http')){abs=t.startsWith('/')?(new URL(masterUrl)).origin+t:base+t;}segs.push(abs);}if(!segs.length)throw new Error('no segments');const buffers=[];let done=0,cursor=0;async function worker(){while(true){const i=cursor++;if(i>=segs.length)return;try{buffers[i]=await fetch(segs[i]).then(r=>r.arrayBuffer());}catch(e){buffers[i]=new Uint8Array(0);}done++;status.textContent=`fetching ${done}/${segs.length}`;}}await Promise.all(Array.from({length:6},worker));status.textContent='assembling…';const total=buffers.reduce((a,b)=>a+b.byteLength,0);const out=new Uint8Array(total);let off=0;for(const b of buffers){out.set(new Uint8Array(b),off);off+=b.byteLength;}const blob=new Blob([out],{type:'video/mp2t'});const url=URL.createObjectURL(blob);const a=document.createElement('a');a.href=url;a.download=`${title.replace(/[\\/:*?"<>|]/g,'_').slice(0,80)}_${quality}.ts`;document.body.appendChild(a);a.click();document.body.removeChild(a);setTimeout(()=>URL.revokeObjectURL(url),60000);status.textContent='✓ downloaded';status.className='status ok';}catch(e){status.textContent='error: '+e.message;status.className='status err';}}
async function openLink(){if(!CURRENT_INFO||!CURRENT_INFO.sourceid){alert('no video loaded');return;}const master=`https://fast.wistia.com/embed/medias/${CURRENT_INFO.sourceid}.m3u8`;document.getElementById('link-master').value=master;const box=document.getElementById('link-variants');box.innerHTML='<p style="color:var(--muted);font-size:12px">loading…</p>';if(!Object.keys(CURRENT_VARIANTS).length){try{const r=await fetch(`/api/variants/${CURRENT_INFO.sourceid}`);const j=await r.json();CURRENT_VARIANTS=j.variants||{};}catch(e){}}const items=Object.entries(CURRENT_VARIANTS).sort((a,b)=>parseInt(b[0])-parseInt(a[0]));if(!items.length){box.innerHTML='<p style="color:var(--muted);font-size:12px">no variants</p>';}else{box.innerHTML='';for(const [q,url] of items){const el=document.createElement('div');el.className='variant';el.innerHTML=`<div style="display:flex;justify-content:space-between;align-items:center;gap:10px;margin-bottom:8px"><span class="name">${esc(q)}</span><button onclick="copyText('${esc(url)}',this)">copy</button></div><input value="${esc(url)}" readonly onclick="this.select()" style="font:11px monospace">`;box.appendChild(el);}}document.getElementById('modal-link').classList.add('open');}
function copyText(t,btn){navigator.clipboard.writeText(t).then(()=>{const o=btn.textContent;btn.textContent='✓';setTimeout(()=>btn.textContent=o,1200);}).catch(()=>{const ta=document.createElement('textarea');ta.value=t;document.body.appendChild(ta);ta.select();document.execCommand('copy');document.body.removeChild(ta);const o=btn.textContent;btn.textContent='✓';setTimeout(()=>btn.textContent=o,1200);});}
function closeModal(id){document.getElementById(id).classList.remove('open');}
function copyField(id,btn){const el=document.getElementById(id);el.select();el.setSelectionRange(0,99999);navigator.clipboard.writeText(el.value).then(()=>{const o=btn.textContent;btn.textContent='copied!';setTimeout(()=>btn.textContent=o,1200);});}
document.querySelectorAll('.modal').forEach(m=>{m.addEventListener('click',e=>{if(e.target===m)m.classList.remove('open');});});
document.addEventListener('keydown',e=>{if(e.target.tagName==='INPUT'||e.target.tagName==='SELECT')return;const k=e.key;if(k==='/'){e.preventDefault();document.getElementById('search').focus();return;}if(!VIDEO)return;if(k===' '){e.preventDefault();togglePlay();}else if(k==='ArrowRight')VIDEO.currentTime+=5;else if(k==='ArrowLeft')VIDEO.currentTime-=5;else if(k==='f'||k==='F')toggleFS();});
document.getElementById('search').addEventListener('input',renderTOC);
window.addEventListener('DOMContentLoaded',()=>{console.log('[SE] DOMContentLoaded, calling loadAll');loadAll();});
if(document.readyState!=='loading'){console.log('[SE] DOM already ready, calling loadAll now');loadAll();}
</script></body></html>"""


LOGIN_PAGE = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Admin · SeongEra_Study</title>
<style>
body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;background:#07090c;color:#e6e9ee;font:14px -apple-system,monospace;padding:20px}
.card{background:#0e1218;border:1px solid #1e2630;border-radius:16px;padding:32px 28px;width:100%;max-width:420px;box-shadow:0 24px 60px rgba(0,0,0,.55)}
h1{margin:0 0 6px;font-size:22px;text-align:center;background:linear-gradient(90deg,#5c8dff,#7c5cff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.sub{color:#7c8697;font-size:11.5px;text-align:center;margin-bottom:26px}
label{display:block;font-size:11px;color:#7c8697;text-transform:uppercase;letter-spacing:.6px;margin:16px 0 6px;font-weight:600}
input{width:100%;padding:13px 14px;background:#07090c;border:1px solid #1e2630;color:#e6e9ee;font:inherit;border-radius:10px;min-height:48px;font-size:15px;letter-spacing:3px;text-align:center;box-sizing:border-box}
input:focus{outline:none;border-color:#5c8dff}
button{margin-top:22px;width:100%;padding:15px;background:linear-gradient(90deg,#5c8dff,#7c5cff);color:#fff;border:0;border-radius:10px;font:inherit;font-weight:700;cursor:pointer;min-height:50px;font-size:15px}
.err{margin-top:16px;padding:12px 14px;background:rgba(255,92,92,.1);border:1px solid rgba(255,92,92,.3);border-radius:8px;color:#ff8b8b;font-size:12.5px}
.foot{margin-top:22px;text-align:center;color:#7c8697;font-size:11px}
</style></head><body>
<form class="card" method="POST" action="/admin">
  <h1>SeongEra_Study 📚✏</h1>
  <p class="sub">Admin · Made By @Seong_Era</p>
  <label>Admin Code</label>
  <input type="password" name="code" required autofocus autocomplete="off" inputmode="numeric" maxlength="8" pattern="[0-9]{8}" placeholder="••••••••">
  {% if error %}<div class="err">{{ error }}</div>{% endif %}
  <button type="submit">Unlock</button>
  <div class="foot">Telegram · <a href="https://t.me/Seong_Era" target="_blank" style="color:#5c8dff">t.me/Seong_Era</a></div>
</form></body></html>"""


ADMIN_PAGE = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Admin · SeongEra_Study</title>
<style>
body{margin:0;min-height:100vh;background:#07090c;color:#e6e9ee;font:14px -apple-system,monospace}
.header{padding:20px 24px;background:linear-gradient(180deg,#141a22,#0a0e14);border-bottom:1px solid #1e2630;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px}
h1{margin:0;font-size:18px;background:linear-gradient(90deg,#5c8dff,#7c5cff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.nav{display:flex;gap:8px}
.btn{padding:10px 16px;background:#141a22;border:1px solid #1e2630;color:#e6e9ee;border-radius:9px;font:inherit;font-weight:600;font-size:12.5px;cursor:pointer;min-height:40px;display:inline-flex;align-items:center;text-decoration:none}
.btn:hover{border-color:#5c8dff;color:#5c8dff}
.btn.danger:hover{border-color:#ff5c5c;color:#ff5c5c}
.wrap{max-width:900px;margin:0 auto;padding:24px 20px 60px}
.card{background:#0e1218;border:1px solid #1e2630;border-radius:14px;padding:24px;margin-bottom:20px}
.card h2{margin:0 0 16px;font-size:16px;display:flex;align-items:center;gap:10px}
.card h2::before{content:'';width:4px;height:16px;background:linear-gradient(180deg,#5c8dff,#7c5cff);border-radius:2px}
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
.help b{color:#5c8dff}
.help code{background:#141a22;padding:2px 6px;border-radius:4px;color:#9fb8ff;font-size:11px}
</style></head><body>
<div class="header">
  <h1>SeongEra_Study 📚✏ · Admin</h1>
  <div class="nav">
    <a href="/" class="btn">← Site</a>
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
      3. Copy <code>lw_tokens</code> → extract only the <code>access_token</code> value<br>
      4. Paste here. Valid <b>7 days</b>.
    </div>
  </div>
  <div class="card">
    <h2>Accounts (<span id="count">0</span>)</h2>
    <div id="list"></div>
    <div style="margin-top:14px;display:flex;gap:10px;flex-wrap:wrap">
      <button class="btn" onclick="testAll()">Test All</button>
      <button class="btn" onclick="reload()">Refresh</button>
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
async function logout(){await fetch('/logout',{method:'POST'});location.href='/';}
document.getElementById('add-form').addEventListener('submit',addAcct);
reload();
</script></body></html>"""


# ============ ROUTES ============
@app.route("/")
def index():
    return render_template_string(MAIN_PAGE)


@app.route("/admin", methods=["GET", "POST"])
def admin_route():
    if request.method == "GET":
        if current_admin():
            return render_template_string(ADMIN_PAGE)
        return render_template_string(LOGIN_PAGE, error="")
    code = (request.form.get("code") or "").strip()
    if code != ADMIN_CODE:
        return render_template_string(LOGIN_PAGE, error="Invalid code")
    token = secrets.token_urlsafe(24)
    STORE.cache_set(f"admin:{token}", "1", ttl=ADMIN_TTL)
    resp = make_response(redirect("/admin"))
    resp.set_cookie(ADMIN_COOKIE, token, httponly=True, samesite="Lax", max_age=ADMIN_TTL)
    return resp


@app.route("/logout", methods=["POST", "GET"])
def logout():
    tok = request.cookies.get(ADMIN_COOKIE)
    if tok:
        STORE.cache_set(f"admin:{tok}", "0", ttl=10)
    resp = make_response(redirect("/"))
    resp.delete_cookie(ADMIN_COOKIE)
    return resp


@app.route("/api/batches")
def api_batches():
    seen = {}
    for acct in STORE.get_accounts():
        s = ApnaSession(acct["email"], acct.get("token",""))
        for b in s.fetch_batches():
            tid = b["titleId"]
            if tid not in seen:
                seen[tid] = {"titleId": tid, "label": b["label"]}
    return jsonify(batches=list(seen.values()))


@app.route("/api/sections/<titleId>")
def api_sections(titleId):
    for acct in STORE.get_accounts():
        s = ApnaSession(acct["email"], acct.get("token",""))
        if any(b["titleId"] == titleId for b in s.fetch_batches()):
            d = s.fetch_curriculum(titleId)
            if d:
                secs = (d.get("course") or {}).get("sections") or d.get("sections") or {}
                out = []
                for sid, sec in secs.items():
                    out.append({
                        "id": sid, "title": sec.get("title", sid),
                        "units": [{"id": u.get("id"), "title": u.get("unitTitle",""), "type": u.get("type","")} for u in sec.get("learningPath", [])],
                    })
                return jsonify(sections=out)
    return jsonify(error="no access"), 404


@app.route("/api/video/<titleId>/<unit_id>")
def api_video(titleId, unit_id):
    for acct in STORE.get_accounts():
        s = ApnaSession(acct["email"], acct.get("token",""))
        if any(b["titleId"] == titleId for b in s.fetch_batches()):
            return jsonify(s.fetch_video(titleId, unit_id))
    return jsonify(error="no access"), 404


@app.route("/api/pdf/<titleId>/<unit_id>")
def api_pdf(titleId, unit_id):
    for acct in STORE.get_accounts():
        s = ApnaSession(acct["email"], acct.get("token",""))
        if any(b["titleId"] == titleId for b in s.fetch_batches()):
            return jsonify(s.pdf_redirect(titleId, unit_id))
    return jsonify(error="no access"), 404


@app.route("/api/variants/<sourceid>")
def api_variants(sourceid):
    accts = STORE.get_accounts()
    if accts:
        s = ApnaSession(accts[0]["email"], accts[0].get("token",""))
        return jsonify(variants=s.wistia_variants(sourceid))
    return jsonify(variants={})


@app.route("/api/admin/accounts", methods=["GET", "POST", "DELETE"])
@require_admin
def admin_accounts():
    if request.method == "GET":
        out = []
        for a in STORE.get_accounts():
            e = a["email"]; u, _, d = e.partition("@")
            masked = (u[:2] + "*" * max(3, len(u)-4) + u[-2:]) + "@" + d if len(u)>4 else u[:1] + "*"*(len(u)-1) + "@" + d
            tok = a.get("token","") or ""
            try:
                added_ts = time.mktime(time.strptime(a["added_at"][:19], "%Y-%m-%dT%H:%M:%S")) if isinstance(a.get("added_at"), str) else a.get("added_at", time.time())
                updated_ts = time.mktime(time.strptime(a["token_updated_at"][:19], "%Y-%m-%dT%H:%M:%S")) if isinstance(a.get("token_updated_at"), str) else a.get("token_updated_at", time.time())
            except Exception:
                added_ts = updated_ts = time.time()
            age = time.time() - updated_ts
            if age > 7*24*3600: cls, txt = "token-bad", "expired"
            elif age > 6*24*3600: cls, txt = "token-warn", "expiring soon"
            else: cls, txt = "token-ok", f"valid · {int((7*24*3600-age)/3600)}h left"
            out.append({
                "email": e, "display": masked, "label": a.get("label",""),
                "token_prefix": tok[:16],
                "added_ago": f"{int((time.time()-added_ts)/3600)}h ago",
                "status_class": cls, "status_text": txt,
            })
        return jsonify(accounts=out)
    if request.method == "POST":
        b = request.get_json(silent=True) or {}
        email = (b.get("email") or "").strip()
        token = (b.get("token") or "").strip()
        label = b.get("label") or ""
        if not email or not token:
            return jsonify(error="email and token required")
        s = ApnaSession(email, token)
        ok, detail = s.verify()
        if not ok:
            return jsonify(error=f"token invalid: {detail}")
        ok2, msg = STORE.add_account(email, token, label)
        if not ok2:
            return jsonify(error=msg)
        return jsonify(ok=True)
    if request.method == "DELETE":
        b = request.get_json(silent=True) or {}
        return jsonify(ok=STORE.remove_account(b.get("email","")))


@app.route("/api/admin/test")
@require_admin
def admin_test():
    results = []
    for acct in STORE.get_accounts():
        s = ApnaSession(acct["email"], acct.get("token",""))
        ok, detail = s.verify()
        results.append({"email": acct["email"], "ok": ok, "error": None if ok else detail})
    return jsonify(results=results)


@app.route("/api/debug")
def debug():
    return jsonify({
        "have_cffi": HAVE_CFFI,
        "supabase_enabled": STORE.enabled,
        "supabase_url_set": bool(SUPABASE_URL),
        "supabase_key_set": bool(SUPABASE_KEY),
        "admin_code_set": bool(os.environ.get("ADMIN_CODE")),
        "accounts_count": len(STORE.get_accounts()),
        "python_version": __import__("sys").version.split()[0],
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002, debug=True)
