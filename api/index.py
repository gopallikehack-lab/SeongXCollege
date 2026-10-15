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
TG_LINK = "https://t.me/SeongEraStudy"
TG_ADMIN = "https://t.me/SeongEra"
UPI_ID = "gopal92008@fam"
DONATE_QR = "https://i.ibb.co/1Ghndgcb/IMG-20261015-162405-562.jpg"

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
            print(f"[!] supabase get status {r.status_code}: {r.text[:200]}")
        except Exception as e:
            print(f"[!] supabase get: {e}")
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
            "fields": "title,titleId,courseImage,image,settings,progress,access,type",
            "owned": "true",
            "sortFields": [{"sortField":"lastVisited","direction":"desc"}],
            "offset": "0", "itemsPerPage": "100", "paginationType": "offset",
        }
        try:
            r = self.s.post(f"{BASE}/api/learner/products", json=body,
                            headers=self.h(), timeout=TIMEOUT)
            d = r.json()
        except Exception as e:
            print(f"[!] fetch_batches {self.email}: {type(e).__name__}")
            return []
        out = []
        for c in d.get("data", []):
            tid, ttl = c.get("titleId"), c.get("title")
            if not tid or not ttl:
                continue
            img = ""
            ci = c.get("courseImage") or c.get("image") or {}
            if isinstance(ci, dict):
                img = ci.get("url") or ci.get("src") or ""
            elif isinstance(ci, str):
                img = ci
            out.append({"titleId": tid, "label": ttl, "image": img})
        return out

    def fetch_course_image(self, titleId):
        """Fetch just the cover image from the course endpoint."""
        try:
            r = self.s.get(f"{BASE}/api/course/{titleId}?contents&path-player",
                           headers=self.h(f"{BASE}/path-player?courseid={titleId}"),
                           timeout=TIMEOUT)
            if r.status_code != 200:
                return ""
            d = r.json()
            ci = (d.get("course") or {}).get("courseImage") or {}
            if isinstance(ci, dict):
                return ci.get("url") or ""
            if isinstance(ci, str):
                return ci
        except Exception:
            pass
        return ""

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


# ---- batch cache ----
_BATCH_CACHE = {}
_BATCH_CACHE_TTL = 300


def _get_batches_cached(acct):
    email = (acct.get("email") or "").lower()
    if not email:
        return []
    now = time.time()
    cached = _BATCH_CACHE.get(email)
    if cached and now - cached[0] < _BATCH_CACHE_TTL:
        return cached[1]
    try:
        s = ApnaSession(acct["email"], acct.get("token",""))
        batches = s.fetch_batches()
        # if any batch lacks an image, try fetching from course endpoint
        for b in batches:
            if not b.get("image"):
                img = s.fetch_course_image(b["titleId"])
                if img:
                    b["image"] = img
        _BATCH_CACHE[email] = (now, batches)
        return batches
    except Exception:
        return cached[1] if cached else []


def _find_session_for(titleId):
    for acct in STORE.get_accounts():
        batches = _get_batches_cached(acct)
        if any(b.get("titleId") == titleId for b in batches):
            return ApnaSession(acct["email"], acct.get("token",""))
    return None


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


# ============================================================
# MAIN PAGE
# ============================================================
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

/* top nav */
.topnav{display:flex;align-items:center;gap:10px;padding:12px 16px;background:linear-gradient(180deg,rgba(20,26,34,.6),rgba(10,14,20,.9));border-bottom:1px solid var(--line);flex-shrink:0;position:relative;z-index:100}
.menu-btn{padding:8px 12px;background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:9px;cursor:pointer;font-size:18px;min-width:44px;min-height:44px;display:inline-flex;align-items:center;justify-content:center}
.brand{flex:1;min-width:0}
.brand h1{margin:0;font-size:16px;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.brand .sub{font-size:10.5px;color:var(--muted);display:block;margin-top:2px}
.nav-right{display:flex;gap:6px}
.theme-btn{padding:8px 12px;background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:9px;cursor:pointer;font-size:16px;min-width:44px;min-height:44px}

/* drawer */
.drawer-bg{position:fixed;inset:0;background:rgba(0,0,0,.65);backdrop-filter:blur(4px);z-index:200;opacity:0;pointer-events:none;transition:opacity .22s}
.drawer-bg.open{opacity:1;pointer-events:auto}
.drawer{position:fixed;top:0;left:0;bottom:0;width:280px;max-width:85vw;background:var(--panel);border-right:1px solid var(--line);z-index:201;transform:translateX(-100%);transition:transform .22s;display:flex;flex-direction:column;overflow-y:auto}
.drawer.open{transform:translateX(0)}
.drawer-head{padding:20px 18px;border-bottom:1px solid var(--line);background:linear-gradient(180deg,rgba(92,141,255,.08),transparent)}
.drawer-head h2{margin:0;font-size:17px;font-weight:700}
.drawer-head .tg{font-size:11.5px;color:var(--muted);display:block;margin-top:4px}
.drawer-item{display:flex;align-items:center;gap:12px;padding:14px 18px;cursor:pointer;color:var(--txt);border-left:3px solid transparent;font-weight:600;font-size:13.5px;transition:all .12s;text-decoration:none}
.drawer-item:hover{background:var(--panel2)}
.drawer-item.active{background:linear-gradient(90deg,rgba(92,141,255,.12),transparent);border-left-color:var(--accent);color:var(--accent)}
.drawer-item .ico{font-size:18px;width:24px;text-align:center}
.drawer-foot{margin-top:auto;padding:16px 18px;font-size:10.5px;color:var(--muted);border-top:1px solid var(--line);line-height:1.6}

/* content area */
.content{flex:1;display:flex;flex-direction:column;overflow:hidden;min-height:0;position:relative}
.page{display:none;flex:1;overflow-y:auto;padding:16px}
.page.active{display:block}

/* batches grid */
.search-wrap{padding:12px 0;position:sticky;top:0;background:var(--bg);z-index:5}
.search-wrap input{width:100%;padding:12px 14px;background:var(--panel);border:1px solid var(--line);color:var(--txt);font:inherit;border-radius:10px;min-height:46px;font-size:14px}
.search-wrap input:focus{outline:none;border-color:var(--accent)}
.batch-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:14px;padding-bottom:40px}
@media (min-width:700px){.batch-grid{grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:16px}}
.batch-card{background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden;cursor:pointer;transition:all .15s;display:flex;flex-direction:column}
.batch-card:active{transform:scale(.98)}
.batch-card:hover{border-color:var(--accent)}
.batch-card .thumb{aspect-ratio:16/9;background:linear-gradient(135deg,var(--accent),var(--accent2));position:relative;overflow:hidden}
.batch-card .thumb img{width:100%;height:100%;object-fit:cover;display:block}
.batch-card .thumb .fallback{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:800;color:#fff;text-shadow:0 2px 8px rgba(0,0,0,.4)}
.batch-card .meta{padding:12px 14px;flex:1;display:flex;flex-direction:column;gap:4px;min-width:0}
.batch-card .meta .t{color:#dfe6f0;font-weight:600;font-size:13.5px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.batch-card .meta .s{color:var(--muted);font-size:11px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}

/* player view */
.viewer{display:flex;flex-direction:column;flex:1;min-height:0}
.viewer.hidden{display:none}
.viewer-head{display:flex;align-items:center;gap:10px;padding:10px 16px;background:var(--panel);border-bottom:1px solid var(--line);flex-shrink:0}
.viewer-head .back{padding:8px 12px;background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:8px;cursor:pointer;font-size:14px;min-height:40px;min-width:40px}
.viewer-head .title{font-size:14px;font-weight:600;color:#dfe6f0;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.viewer-body{flex:1;display:flex;overflow:hidden;min-height:0;position:relative}
.sidebar{width:340px;min-width:340px;background:var(--panel);border-right:1px solid var(--line);display:flex;flex-direction:column;transition:transform .22s ease}
.search2{padding:10px 12px;border-bottom:1px solid var(--line);flex-shrink:0}
.search2 input{width:100%;padding:10px 12px;background:var(--bg);border:1px solid var(--line);color:var(--txt);font:inherit;border-radius:9px;min-height:42px;font-size:13.5px}
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
.unit .right{display:flex;gap:6px;align-items:center;flex-shrink:0}
.unit .type{padding:2px 8px;border-radius:8px;font-size:10px;background:var(--panel2);color:var(--muted);font-weight:600;text-transform:uppercase}

.player-main{flex:1;display:flex;flex-direction:column;overflow:hidden;min-width:0}
.player-wrap{flex:1;background:#000;display:flex;align-items:center;justify-content:center;position:relative;min-height:0;overflow:hidden}
.player-empty{color:var(--muted);text-align:center;padding:32px;max-width:560px;line-height:1.8}
.player-empty h2{font-size:24px;margin:0 0 16px;font-weight:800}
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
.bottombar{padding:8px 14px;background:var(--panel);border-top:1px solid var(--line);flex-shrink:0;font-size:11.5px;color:var(--muted)}
.status{padding:3px 10px;background:var(--panel2);border-radius:12px;color:var(--accent);font-weight:600;font-size:11px}
.status.ok{color:var(--good)}
.status.err{color:#ff7a7a}
.pdf-viewer{width:100%;height:100%;display:flex;flex-direction:column;background:#0a0a0a}
.pdf-toolbar{padding:10px 14px;background:var(--panel2);border-bottom:1px solid var(--line);display:flex;justify-content:space-between;gap:10px;align-items:center;flex-wrap:wrap}
.pdf-toolbar .name{color:#dfe6f0;font-weight:600;font-size:12.5px;flex:1;min-width:100px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.pdf-actions{display:flex;gap:6px;flex-wrap:wrap}
.pdf-actions a,.pdf-actions button{padding:8px 12px;background:var(--panel2);color:var(--txt);border:1px solid var(--line);border-radius:8px;font:inherit;font-weight:600;font-size:12px;cursor:pointer;min-height:38px;display:inline-flex;align-items:center;gap:5px;text-decoration:none}
.pdf-actions .primary{background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border-color:transparent}
.pdf-frame{flex:1;border:0;background:#fff}

/* generic page cards */
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

/* modal */
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
@media (max-width:900px){
  .sidebar{position:absolute;top:0;left:0;bottom:0;width:85vw;max-width:340px;z-index:15;transform:translateX(-100%);box-shadow:12px 0 40px rgba(0,0,0,.6)}
  .sidebar.open{transform:translateX(0)}
}
</style>
</head>
<body>
<div style="height:100vh;height:100dvh;display:flex;flex-direction:column">

  <!-- top nav -->
  <div class="topnav">
    <button class="menu-btn" onclick="openDrawer()">☰</button>
    <div class="brand">
      <h1 class="brand-gradient">SeongEra_Study 📚✏</h1>
      <span class="sub">t.me/SeongEraStudy</span>
    </div>
    <div class="nav-right">
      <button class="theme-btn" onclick="cycleTheme()">🎨</button>
    </div>
  </div>

  <!-- drawer -->
  <div class="drawer-bg" id="drawer-bg" onclick="closeDrawer()"></div>
  <div class="drawer" id="drawer">
    <div class="drawer-head">
      <h2 class="brand-gradient">SeongEra_Study</h2>
      <span class="tg">📚 Study free · Made By @Seong_Era</span>
    </div>
    <div class="drawer-item active" data-page="batches" onclick="goPage('batches')">
      <span class="ico">📚</span><span>Batches</span>
    </div>
    <div class="drawer-item" data-page="enroll" onclick="goPage('enroll')">
      <span class="ico">➕</span><span>Enroll Batch</span>
    </div>
    <a class="drawer-item" href="https://t.me/SeongEraStudy" target="_blank">
      <span class="ico">💬</span><span>Join Telegram</span>
    </a>
    <div class="drawer-item" data-page="contact" onclick="goPage('contact')">
      <span class="ico">📩</span><span>Contact Us</span>
    </div>
    <div class="drawer-item" data-page="donate" onclick="goPage('donate')">
      <span class="ico">❤️</span><span>Donate</span>
    </div>
    <div class="drawer-foot">
      Made By @Seong_Era<br>
      Support: t.me/Seong_Era
    </div>
  </div>

  <!-- content -->
  <div class="content">

    <!-- PAGE: Batches -->
    <div class="page active" id="page-batches">
      <div class="search-wrap">
        <input id="batch-search" placeholder="🔍 Search batches…">
      </div>
      <div class="batch-grid" id="batch-grid">
        <div style="padding:24px;color:var(--muted);text-align:center;grid-column:1/-1">loading…</div>
      </div>
    </div>

    <!-- PAGE: Viewer (batch opened) -->
    <div class="page" id="page-viewer">
      <div class="viewer">
        <div class="viewer-head">
          <button class="back" onclick="closeBatch()">←</button>
          <div class="title" id="viewer-title">Batch</div>
          <button class="back" onclick="toggleSidebar()">☰</button>
        </div>
        <div class="viewer-body">
          <aside class="sidebar" id="sidebar">
            <div class="search2"><input id="search" placeholder="search units…"></div>
            <div class="toc" id="toc"></div>
          </aside>
          <div class="player-main">
            <div class="player-wrap" id="player-wrap">
              <div class="player-empty">
                <h2 class="brand-gradient">Pick a lecture</h2>
                <p>Select a unit from the sidebar.</p>
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
          </div>
        </div>
      </div>
    </div>

    <!-- PAGE: Enroll -->
    <div class="page" id="page-enroll">
      <div class="card">
        <h2>➕ Enroll / Request a Batch</h2>
        <p>Want a new batch added to <b>SeongEra_Study</b>? Just message me on Telegram with the batch name or link. I add batches manually — as soon as it's live, it'll show up in your Batches tab.</p>
        <div class="btn-row">
          <a class="btn-link" href="https://t.me/Seong_Era" target="_blank">💬 Message @Seong_Era</a>
          <a class="btn-ghost" href="https://t.me/SeongEraStudy" target="_blank">📢 Join Channel</a>
        </div>
      </div>
      <div class="card">
        <h2>What I need from you</h2>
        <p>• Batch name (e.g. <i>Alpha Plus — DSA</i>)</p>
        <p>• Direct link on ApnaCollege if you have it</p>
        <p>• Why you need it (optional, just curious)</p>
        <p style="color:var(--muted);font-size:12px;margin-top:14px">I don't need your ApnaCollege password or any personal account info. Just the batch details.</p>
      </div>
    </div>

    <!-- PAGE: Contact -->
    <div class="page" id="page-contact">
      <div class="card">
        <h2>📩 Contact Us</h2>
        <p>Any issue — playback errors, missing lecture, wrong PDF, or just feedback — reach out. I reply as fast as I can.</p>
        <div class="btn-row">
          <a class="btn-link" href="https://t.me/Seong_Era" target="_blank">💬 @Seong_Era (Personal)</a>
          <a class="btn-ghost" href="https://t.me/SeongEraStudy" target="_blank">📢 Study Channel</a>
        </div>
      </div>
      <div class="card">
        <h2>Common stuff people ask about</h2>
        <p><b>Video won't load:</b> reload the page. If still broken, message me the batch name + lecture title.</p>
        <p><b>Wrong quality or lag:</b> tap the quality dropdown in the player and pick a lower resolution.</p>
        <p><b>Download:</b> hit the ⬇ button in the player. It saves a <code>.ts</code> file — VLC and MX Player play it perfectly.</p>
        <p><b>New batch request:</b> use the Enroll page.</p>
        <p><b>Support / donation:</b> check the Donate page. Anything helps.</p>
      </div>
      <div class="card">
        <h2>Feedback & Discussion</h2>
        <p>Want to suggest a feature, share a trick, or discuss study plans? Message me directly — I read everything.</p>
        <div class="btn-row">
          <a class="btn-link" href="https://t.me/Seong_Era" target="_blank">💬 Open Chat</a>
        </div>
      </div>
    </div>

    <!-- PAGE: Donate -->
    <div class="page" id="page-donate">
      <div class="card">
        <h2>❤️ Support SeongEra_Study</h2>
        <p>Running this takes time and server cost. If it's helped you, even a small amount keeps it alive and free for everyone.</p>
        <p><b>Thank you for the support — it means a lot. 🙏</b></p>
        <img class="qr-img" src="https://i.ibb.co/1Ghndgcb/IMG-20261015-162405-562.jpg" alt="UPI QR">
        <div class="upi-box">
          <span class="id" id="upi-id">__UPI_ID__</span>
          <button onclick="copyUpi(this)">📋 copy UPI ID</button>
        </div>
        <p style="color:var(--muted);font-size:11.5px;margin-top:12px">Scan the QR with any UPI app (GPay / PhonePe / Paytm / BHIM) — or copy the UPI ID.</p>
      </div>
      <div class="card">
        <h2>Where the money goes</h2>
        <p>• Server + domain costs</p>
        <p>• New batches, more lectures</p>
        <p>• Keeping it free for everyone — no ads, no paywall</p>
        <div class="btn-row">
          <a class="btn-ghost" href="https://t.me/Seong_Era" target="_blank">💬 Say hi on Telegram</a>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- modals -->
<div class="modal" id="modal-dl"><div class="box"><button class="close" onclick="closeModal('modal-dl')">×</button><h2>Download</h2><div class="sub">Downloads directly to your device</div><div class="variants" id="dl-variants"></div></div></div>
<div class="modal" id="modal-link"><div class="box"><button class="close" onclick="closeModal('modal-link')">×</button><h2>Direct m3u8 links</h2><div class="sub">Paste into VLC, mpv, yt-dlp</div><input id="link-master" readonly onclick="this.select()"><button onclick="copyField('link-master',this)" style="padding:12px 18px;background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border:0;border-radius:10px;font:inherit;font-weight:600;cursor:pointer;margin-bottom:16px;width:100%">copy master</button><div class="variants" id="link-variants"></div></div></div>

<script src="https://cdn.jsdelivr.net/npm/hls.js@1"></script>
<script>
(function(){
'use strict';
console.log('[SE] script start');
var BATCHES=[],ACTIVE=null,FLAT=[],CURRENT=null,CURRENT_INFO=null,HLS=null,VIDEO=null,CURRENT_VARIANTS={};
var THEMES=["default","rose","green","amber","crimson","cyber","mono","sunset"];
var curTheme=localStorage.getItem("theme")||"default";
document.documentElement.setAttribute("data-theme",curTheme);

window.cycleTheme=function(){
  var i=THEMES.indexOf(curTheme);i=(i+1)%THEMES.length;curTheme=THEMES[i];
  document.documentElement.setAttribute("data-theme",curTheme);
  localStorage.setItem("theme",curTheme);
};

function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}

function showPage(name){
  var pages=document.querySelectorAll('.page');
  for(var i=0;i<pages.length;i++) pages[i].classList.remove('active');
  var el=document.getElementById('page-'+name);
  if(el) el.classList.add('active');
  var items=document.querySelectorAll('.drawer-item[data-page]');
  for(var j=0;j<items.length;j++) items[j].classList.remove('active');
  var act=document.querySelector('.drawer-item[data-page="'+name+'"]');
  if(act) act.classList.add('active');
}
window.goPage=function(name){ showPage(name); closeDrawer(); };

window.openDrawer=function(){ document.getElementById('drawer').classList.add('open'); document.getElementById('drawer-bg').classList.add('open'); };
window.closeDrawer=function(){ document.getElementById('drawer').classList.remove('open'); document.getElementById('drawer-bg').classList.remove('open'); };

function renderBatches(){
  var grid=document.getElementById('batch-grid');
  var q=(document.getElementById('batch-search').value||'').toLowerCase();
  grid.innerHTML='';
  var filtered=BATCHES.filter(function(b){ return !q || (b.label||'').toLowerCase().indexOf(q)!==-1; });
  if(!filtered.length){
    grid.innerHTML='<div style="padding:24px;color:var(--muted);text-align:center;grid-column:1/-1">'+(BATCHES.length?'No batches match your search.':'No batches available.')+'</div>';
    return;
  }
  for(var i=0;i<filtered.length;i++){
    (function(b){
      var card=document.createElement('div');
      card.className='batch-card';
      var initials=(b.label||'?').split(/\s+/).map(function(w){return w.charAt(0);}).join('').slice(0,2).toUpperCase();
      var thumbInner = b.image
        ? '<img src="'+esc(b.image)+'" onerror="this.style.display=\\'none\\';this.nextSibling.style.display=\\'flex\\';" alt=""><div class="fallback" style="display:none">'+esc(initials)+'</div>'
        : '<div class="fallback">'+esc(initials)+'</div>';
      card.innerHTML='<div class="thumb">'+thumbInner+'</div><div class="meta"><span class="t">'+esc(b.label)+'</span><span class="s">tap to open</span></div>';
      card.onclick=function(){ openBatch(b.titleId, b.label); };
      grid.appendChild(card);
    })(filtered[i]);
  }
}

window.openBatch=function(titleId, label){
  ACTIVE=titleId;
  document.getElementById('viewer-title').textContent=label;
  document.getElementById('search').value='';
  document.getElementById('toc').innerHTML='<div style="padding:20px;color:var(--muted)">loading sections…</div>';
  document.getElementById('player-wrap').innerHTML='<div class="player-empty"><h2 class="brand-gradient">Pick a lecture</h2><p>Select a unit from the sidebar.</p></div>';
  document.getElementById('controls').style.display='none';
  destroyPlayer();
  showPage('viewer');
  fetch('/api/sections/'+encodeURIComponent(titleId))
    .then(function(r){return r.json();})
    .then(function(j){
      if(!j||!j.sections){
        document.getElementById('toc').innerHTML='<div style="padding:20px;color:#ff7a7a">'+esc((j&&j.error)||'failed')+'</div>';
        return;
      }
      window._sections=j.sections;
      renderTOC();
    })
    .catch(function(e){
      document.getElementById('toc').innerHTML='<div style="padding:20px;color:#ff7a7a">error: '+esc(e.message||e)+'</div>';
    });
};

window.closeBatch=function(){
  destroyPlayer();
  ACTIVE=null;
  showPage('batches');
};

window.toggleSidebar=function(){ document.getElementById('sidebar').classList.toggle('open'); };

function renderTOC(){
  var toc=document.getElementById('toc');
  toc.innerHTML='';FLAT=[];
  var q=(document.getElementById('search').value||'').toLowerCase();
  var sections=window._sections||[];
  for(var si=0;si<sections.length;si++){
    var sec=sections[si];
    var units=sec.units.filter(function(u){ return !q || ((u.title||'').toLowerCase().indexOf(q)!==-1); });
    if(q && units.length===0) continue;
    var secDiv=document.createElement('div');secDiv.className='sec';
    var head=document.createElement('div');head.className='sec-head'+(q?' open':'');
    head.innerHTML='<div class="left"><span class="t">'+esc(sec.title)+'</span></div><span class="cnt">'+sec.units.length+'</span>';
    var body=document.createElement('div');body.className='sec-body'+(q?' open':'');
    head.onclick=(function(h,b){return function(){h.classList.toggle('open');b.classList.toggle('open');};})(head,body);
    for(var ui=0;ui<units.length;ui++){
      var u=units[ui];
      var idx=FLAT.length;
      FLAT.push({unit:u,sectionTitle:sec.title});
      var uDiv=document.createElement('div');uDiv.className='unit';uDiv.dataset.idx=idx;
      uDiv.innerHTML='<div class="u-left"><span class="t">'+esc(u.title||u.id)+'</span></div><span class="right"><span class="type '+esc(u.type||'')+'">'+esc(u.type||'')+'</span></span>';
      (function(i){uDiv.onclick=function(){playUnit(i);};})(idx);
      body.appendChild(uDiv);
    }
    secDiv.appendChild(head);secDiv.appendChild(body);toc.appendChild(secDiv);
  }
}

function playUnit(idx){
  if(idx<0||idx>=FLAT.length) return;
  CURRENT=idx;
  var item=FLAT[idx];var u=item.unit;
  var units=document.querySelectorAll('.unit.active');
  for(var i=0;i<units.length;i++) units[i].classList.remove('active');
  var el=document.querySelector('.unit[data-idx="'+idx+'"]');
  if(el){el.classList.add('active');el.scrollIntoView({block:'nearest',behavior:'smooth'});}
  document.getElementById('status').textContent='loading…';
  document.getElementById('status').className='status';
  document.getElementById('controls').style.display='none';
  destroyPlayer();
  fetch('/api/video/'+encodeURIComponent(ACTIVE)+'/'+encodeURIComponent(u.id))
    .then(function(r){return r.json();})
    .then(function(j){
      CURRENT_INFO=j;
      if(j.error){
        document.getElementById('player-wrap').innerHTML='<div class="player-empty"><p>error: '+esc(j.error)+'</p></div>';
        document.getElementById('status').textContent='error';
        document.getElementById('status').className='status err';
        return;
      }
      if(j.type==='wistia'&&j.sourceid){playWistia(j.sourceid);}
      else if(j.type==='pdf'){playPdf(ACTIVE,u.id);}
      else{document.getElementById('player-wrap').innerHTML='<div class="player-empty"><p>unsupported: '+esc(j.type||'?')+'</p></div>';}
      if(window.innerWidth<=900) document.getElementById('sidebar').classList.remove('open');
    })
    .catch(function(e){
      document.getElementById('player-wrap').innerHTML='<div class="player-empty"><p>error: '+esc(e.message||e)+'</p></div>';
    });
}

function destroyPlayer(){
  if(HLS){try{HLS.destroy();}catch(e){}HLS=null;}
  if(VIDEO){try{VIDEO.pause();}catch(e){}VIDEO=null;}
}

function playWistia(sourceid){
  var master='https://fast.wistia.com/embed/medias/'+sourceid+'.m3u8';
  document.getElementById('player-wrap').innerHTML='<video id="v" playsinline preload="metadata"></video>';
  VIDEO=document.getElementById('v');
  document.getElementById('controls').style.display='block';
  fetch('/api/variants/'+encodeURIComponent(sourceid))
    .then(function(r){return r.json();})
    .then(function(j){CURRENT_VARIANTS=(j&&j.variants)||{};})
    .catch(function(){CURRENT_VARIANTS={};});
  if(window.Hls&&Hls.isSupported()){
    HLS=new Hls({capLevelToPlayerSize:false,startLevel:-1,autoStartLoad:true,maxBufferLength:60});
    HLS.loadSource(master);HLS.attachMedia(VIDEO);
    HLS.on(Hls.Events.MANIFEST_PARSED,function(e,data){
      var sel=document.getElementById('quality');sel.innerHTML='<option value="auto">auto</option>';
      for(var i=0;i<data.levels.length;i++){
        var lvl=data.levels[i];
        var o=document.createElement('option');o.value=i;
        o.textContent=lvl.height?(lvl.height+'p'):('L'+i);
        sel.appendChild(o);
      }
      VIDEO.play().catch(function(){});
    });
    HLS.on(Hls.Events.LEVEL_SWITCHED,function(e,data){
      var lvl=HLS.levels[data.level];
      if(lvl){document.getElementById('status').textContent='playing · '+(lvl.height||'?')+'p';document.getElementById('status').className='status ok';}
    });
  } else if(VIDEO.canPlayType('application/vnd.apple.mpegurl')){
    VIDEO.src=master;VIDEO.play().catch(function(){});
  }
  VIDEO.addEventListener('timeupdate',updateTime);
  VIDEO.addEventListener('loadedmetadata',updateTime);
  VIDEO.addEventListener('play',function(){document.getElementById('btn-play').textContent='❚❚';});
  VIDEO.addEventListener('pause',function(){document.getElementById('btn-play').textContent='▶';});
  VIDEO.addEventListener('click',togglePlay);
  document.getElementById('status').textContent='playing';
}

function playPdf(titleId,unitId){
  document.getElementById('player-wrap').innerHTML='<div class="player-empty">loading PDF…</div>';
  fetch('/api/pdf/'+encodeURIComponent(titleId)+'/'+encodeURIComponent(unitId))
    .then(function(r){return r.json();})
    .then(function(info){
      if(info.error){document.getElementById('player-wrap').innerHTML='<div class="player-empty"><p>PDF error: '+esc(info.error)+'</p></div>';return;}
      window._pdfInfo=info;
      document.getElementById('player-wrap').innerHTML='<div class="pdf-viewer"><div class="pdf-toolbar"><span class="name">📄 '+esc(info.display||info.filename)+'</span><div class="pdf-actions"><a href="'+esc(info.redirectUrl)+'" download="'+esc(info.filename)+'" target="_blank" class="primary">⬇ download</a><button onclick="pdfCopyUrl(this)">🔗 copy</button><button onclick="pdfNewTab()">↗ new tab</button></div></div><iframe class="pdf-frame" src="'+esc(info.redirectUrl)+'"></iframe></div>';
      document.getElementById('status').textContent='pdf';
      document.getElementById('status').className='status ok';
    })
    .catch(function(e){document.getElementById('player-wrap').innerHTML='<div class="player-empty"><p>PDF error: '+esc(e.message||e)+'</p></div>';});
}
window.pdfNewTab=function(){ if(window._pdfInfo&&window._pdfInfo.redirectUrl) window.open(window._pdfInfo.redirectUrl,'_blank'); };
window.pdfCopyUrl=function(btn){
  var item=FLAT[CURRENT];
  fetch('/api/pdf/'+encodeURIComponent(ACTIVE)+'/'+encodeURIComponent(item.unit.id))
    .then(function(r){return r.json();})
    .then(function(info){
      if(info.redirectUrl){
        navigator.clipboard.writeText(info.redirectUrl);
        var o=btn.textContent;btn.textContent='✓';
        setTimeout(function(){btn.textContent=o;},1200);
      }
    });
};

function updateTime(){
  if(!VIDEO) return;
  var cur=VIDEO.currentTime||0, dur=VIDEO.duration||0;
  document.getElementById('time').textContent=fmt(cur)+' / '+fmt(dur);
  var pct=dur?(cur/dur)*100:0;
  document.getElementById('seek-filled').style.width=pct+'%';
  document.getElementById('seek-knob').style.left=pct+'%';
}
function fmt(s){
  s=Math.floor(s||0);
  var h=Math.floor(s/3600),m=Math.floor((s%3600)/60),r=s%60;
  if(h) return h+':'+(m<10?'0':'')+m+':'+(r<10?'0':'')+r;
  return m+':'+(r<10?'0':'')+r;
}
window.togglePlay=function(){if(VIDEO){VIDEO.paused?VIDEO.play():VIDEO.pause();}};
window.skip=function(n){if(VIDEO)VIDEO.currentTime+=n;};
window.seekClick=function(e){if(!VIDEO)return;var r=e.currentTarget.getBoundingClientRect();VIDEO.currentTime=((e.clientX-r.left)/r.width)*(VIDEO.duration||0);};
window.setSpeed=function(v){if(VIDEO)VIDEO.playbackRate=parseFloat(v);};
window.onQualityChange=function(v){if(HLS)HLS.currentLevel=(v==='auto')?-1:parseInt(v,10);};
window.toggleFS=function(){var w=document.getElementById('player-wrap');if(!document.fullscreenElement)w.requestFullscreen();else document.exitFullscreen();};
window.playNext=function(){if(CURRENT!=null&&CURRENT<FLAT.length-1)playUnit(CURRENT+1);};
window.playPrev=function(){if(CURRENT!=null&&CURRENT>0)playUnit(CURRENT-1);};

window.openDownload=function(){
  if(!CURRENT_INFO) return;
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
  for(var j=0;j<btns.length;j++){
    (function(b){
      b.onclick=function(){browserHlsDownload(b.dataset.url,(CURRENT_INFO.title||'video'),b.dataset.q);};
    })(btns[j]);
  }
  document.getElementById('modal-dl').classList.add('open');
};

function browserHlsDownload(masterUrl,title,quality){
  closeModal('modal-dl');
  var status=document.getElementById('status');
  status.textContent='download starting…';
  fetch(masterUrl).then(function(r){return r.text();}).then(function(m){
    var lines=m.split(/\r?\n/);
    var base=masterUrl.substring(0,masterUrl.lastIndexOf('/')+1);
    var segs=[];
    for(var i=0;i<lines.length;i++){
      var t=lines[i].trim();
      if(!t||t.charAt(0)==='#') continue;
      var abs=t;
      if(t.indexOf('http')!==0){ if(t.charAt(0)==='/') abs=(new URL(masterUrl)).origin+t; else abs=base+t; }
      segs.push(abs);
    }
    if(!segs.length) throw new Error('no segments');
    var buffers=[]; var done=0; var cursor=0;
    function worker(){
      var i=cursor++;
      if(i>=segs.length) return Promise.resolve();
      return fetch(segs[i]).then(function(r){return r.arrayBuffer();})
        .then(function(buf){buffers[i]=buf;}).catch(function(){buffers[i]=new Uint8Array(0);})
        .then(function(){done++;status.textContent='fetching '+done+'/'+segs.length;return worker();});
    }
    var workers=[]; for(var w=0;w<6;w++) workers.push(worker());
    return Promise.all(workers).then(function(){
      status.textContent='assembling…';
      var total=0; for(var i=0;i<buffers.length;i++) total+=buffers[i].byteLength;
      var out=new Uint8Array(total); var off=0;
      for(var i=0;i<buffers.length;i++){ out.set(new Uint8Array(buffers[i]),off); off+=buffers[i].byteLength; }
      var blob=new Blob([out],{type:'video/mp2t'});
      var url=URL.createObjectURL(blob);
      var a=document.createElement('a'); a.href=url;
      a.download=(title.replace(/[\\/:*?"<>|]/g,'_').slice(0,80))+'_'+quality+'.ts';
      document.body.appendChild(a);a.click();document.body.removeChild(a);
      setTimeout(function(){URL.revokeObjectURL(url);},60000);
      status.textContent='✓ downloaded'; status.className='status ok';
    });
  }).catch(function(e){status.textContent='error: '+e.message;status.className='status err';});
}

window.openLink=function(){
  if(!CURRENT_INFO||!CURRENT_INFO.sourceid){alert('no video loaded');return;}
  var master='https://fast.wistia.com/embed/medias/'+CURRENT_INFO.sourceid+'.m3u8';
  document.getElementById('link-master').value=master;
  var box=document.getElementById('link-variants'); box.innerHTML='<p style="color:var(--muted);font-size:12px">loading…</p>';
  fetch('/api/variants/'+encodeURIComponent(CURRENT_INFO.sourceid))
    .then(function(r){return r.json();})
    .then(function(j){
      CURRENT_VARIANTS=(j&&j.variants)||{};
      var items=Object.entries(CURRENT_VARIANTS).sort(function(a,b){return parseInt(b[0])-parseInt(a[0]);});
      if(!items.length){ box.innerHTML='<p style="color:var(--muted);font-size:12px">no variants</p>'; }
      else {
        box.innerHTML='';
        for(var i=0;i<items.length;i++){
          var q=items[i][0],url=items[i][1];
          var el=document.createElement('div');el.className='variant';
          el.innerHTML='<div style="display:flex;justify-content:space-between;align-items:center;gap:10px;margin-bottom:8px"><span class="name">'+esc(q)+'</span><button data-url="'+esc(url)+'" class="copybtn">copy</button></div><input value="'+esc(url)+'" readonly onclick="this.select()" style="font:11px monospace">';
          box.appendChild(el);
        }
        var btns=box.querySelectorAll('.copybtn');
        for(var j=0;j<btns.length;j++){ (function(b){b.onclick=function(){copyText(b.dataset.url,b);};})(btns[j]); }
      }
      document.getElementById('modal-link').classList.add('open');
    });
};

function copyText(t,btn){
  navigator.clipboard.writeText(t).then(function(){var o=btn.textContent;btn.textContent='✓';setTimeout(function(){btn.textContent=o;},1200);})
    .catch(function(){var ta=document.createElement('textarea');ta.value=t;document.body.appendChild(ta);ta.select();document.execCommand('copy');document.body.removeChild(ta);var o=btn.textContent;btn.textContent='✓';setTimeout(function(){btn.textContent=o;},1200);});
}
window.closeModal=function(id){document.getElementById(id).classList.remove('open');};
window.copyField=function(id,btn){
  var el=document.getElementById(id);el.select();el.setSelectionRange(0,99999);
  navigator.clipboard.writeText(el.value).then(function(){var o=btn.textContent;btn.textContent='copied!';setTimeout(function(){btn.textContent=o;},1200);});
};
window.copyUpi=function(btn){
  var id=document.getElementById('upi-id').textContent.trim();
  navigator.clipboard.writeText(id).then(function(){var o=btn.textContent;btn.textContent='✓ copied';setTimeout(function(){btn.textContent=o;},1200);});
};

var modals=document.querySelectorAll('.modal');
for(var mi=0;mi<modals.length;mi++){ (function(m){m.addEventListener('click',function(e){if(e.target===m)m.classList.remove('open');});})(modals[mi]); }

document.addEventListener('keydown',function(e){
  if(e.target.tagName==='INPUT'||e.target.tagName==='SELECT') return;
  var k=e.key;
  if(k==='/'){e.preventDefault();if(document.getElementById('page-viewer').classList.contains('active'))document.getElementById('search').focus();else document.getElementById('batch-search').focus();return;}
  if(!VIDEO) return;
  if(k===' '){e.preventDefault();togglePlay();}
  else if(k==='ArrowRight')VIDEO.currentTime+=5;
  else if(k==='ArrowLeft')VIDEO.currentTime-=5;
  else if(k==='f'||k==='F')toggleFS();
});

document.getElementById('search').addEventListener('input',renderTOC);
document.getElementById('batch-search').addEventListener('input',renderBatches);

function loadAll(){
  console.log('[SE] loading batches');
  var grid=document.getElementById('batch-grid');
  grid.innerHTML='<div style="padding:24px;color:var(--muted);text-align:center;grid-column:1/-1">loading…</div>';
  fetch('/api/batches')
    .then(function(r){return r.json();})
    .then(function(j){
      console.log('[SE] batches', j);
      BATCHES=(j&&j.batches)||[];
      renderBatches();
    })
    .catch(function(e){
      grid.innerHTML='<div style="padding:24px;color:#ff7a7a;text-align:center;grid-column:1/-1">error: '+esc(e.message||e)+'</div>';
    });
}

if(document.readyState==='loading'){ document.addEventListener('DOMContentLoaded',loadAll); } else { loadAll(); }
})();
</script>
</body></html>"""


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
async function clearCache(){
  await fetch('/api/admin/clear_batch_cache');
  alert('cache cleared');
}
async function logout(){await fetch('/logout',{method:'POST'});location.href='/';}
document.getElementById('add-form').addEventListener('submit',addAcct);
reload();
</script></body></html>"""


# ============ ROUTES ============
@app.route("/")
def index():
    html = MAIN_PAGE.replace("__UPI_ID__", UPI_ID)
    return render_template_string(html)


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
        for b in _get_batches_cached(acct):
            tid = b.get("titleId")
            if tid and tid not in seen:
                seen[tid] = {"titleId": tid, "label": b.get("label", tid), "image": b.get("image","")}
    return jsonify(batches=list(seen.values()))


@app.route("/api/sections/<titleId>")
def api_sections(titleId):
    s = _find_session_for(titleId)
    if not s:
        return jsonify(error="no account has access to this batch"), 404
    d = s.fetch_curriculum(titleId)
    if not d:
        return jsonify(error="failed to load curriculum"), 500
    secs = (d.get("course") or {}).get("sections") or d.get("sections") or {}
    out = []
    for sid, sec in secs.items():
        out.append({
            "id": sid,
            "title": sec.get("title", sid),
            "units": [{"id": u.get("id"), "title": u.get("unitTitle",""), "type": u.get("type","")} for u in sec.get("learningPath", [])],
        })
    return jsonify(sections=out)


@app.route("/api/video/<titleId>/<unit_id>")
def api_video(titleId, unit_id):
    s = _find_session_for(titleId)
    if not s:
        return jsonify(error="no account has access"), 404
    return jsonify(s.fetch_video(titleId, unit_id))


@app.route("/api/pdf/<titleId>/<unit_id>")
def api_pdf(titleId, unit_id):
    s = _find_session_for(titleId)
    if not s:
        return jsonify(error="no account has access"), 404
    return jsonify(s.pdf_redirect(titleId, unit_id))


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
        _BATCH_CACHE.pop(email.lower(), None)
        return jsonify(ok=True)
    if request.method == "DELETE":
        b = request.get_json(silent=True) or {}
        email = b.get("email","")
        ok = STORE.remove_account(email)
        _BATCH_CACHE.pop(email.lower(), None)
        return jsonify(ok=ok)


@app.route("/api/admin/test")
@require_admin
def admin_test():
    results = []
    for acct in STORE.get_accounts():
        s = ApnaSession(acct["email"], acct.get("token",""))
        ok, detail = s.verify()
        results.append({"email": acct["email"], "ok": ok, "error": None if ok else detail})
    return jsonify(results=results)


@app.route("/api/admin/clear_batch_cache")
@require_admin
def admin_clear_batch_cache():
    _BATCH_CACHE.clear()
    return jsonify(ok=True)


@app.route("/api/debug")
def debug():
    return jsonify({
        "have_cffi": HAVE_CFFI,
        "supabase_enabled": STORE.enabled,
        "admin_code_set": bool(os.environ.get("ADMIN_CODE")),
        "accounts_count": len(STORE.get_accounts()),
        "python_version": __import__("sys").version.split()[0],
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002, debug=True)
