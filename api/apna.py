"""ApnaCollege API client."""
import json
import re
import urllib.parse

try:
    from curl_cffi import requests as http
    HAVE_CFFI = True
except ImportError:
    import requests as http
    HAVE_CFFI = False

from .config import (
    BASE, IMPERSONATE, TIMEOUT, TOKEN_TTL, BATCH_CACHE_TTL,
)
from .store import STORE


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
        return {"Accept": "application/json", "Content-Type": "application/json",
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

    def fetch_image_map(self):
        """Parse /start page HTML for batch cover images."""
        try:
            r = self.s.get(f"{BASE}/start",
                headers={
                    "Accept": "text/html,application/xhtml+xml",
                    "Origin": BASE,
                    "Referer": f"{BASE}/start",
                    "token": self.token or "",
                },
                timeout=TIMEOUT)
            if r.status_code != 200:
                print(f"[!] image_map status {r.status_code}")
                return {}
            m = re.search(r'var SITE_AFFILIATES=(\{.*?\});', r.text, re.DOTALL)
            if not m:
                print("[!] SITE_AFFILIATES not found")
                return {}
            data = json.loads(m.group(1))
            out = {}
            for p in data.get("products-migration-v4", []) or []:
                tid = p.get("titleId")
                img = p.get("image")
                if tid and img:
                    out[tid] = img
            print(f"[+] image_map {self.email}: {len(out)} images")
            return out
        except Exception as e:
            print(f"[!] fetch_image_map: {type(e).__name__}: {e}")
            return {}

    def fetch_batches(self):
        body = {
            "type": "course",
            "access": "public,private-enroll,soon,view-locked",
            "excludeNotEnrolledPrivateProductsForAdmin": "true",
            "fields": "title,titleId,courseImage,image,settings,progress,access,type",
            "owned": "true",
            "sortFields": [{"sortField": "lastVisited", "direction": "desc"}],
            "offset": "0", "itemsPerPage": "100", "paginationType": "offset",
        }
        try:
            r = self.s.post(f"{BASE}/api/learner/products", json=body,
                            headers=self.h(), timeout=TIMEOUT)
            d = r.json()
        except Exception as e:
            print(f"[!] fetch_batches {self.email}: {type(e).__name__}")
            return []

        data = d.get("data") or []
        image_map = self.fetch_image_map()

        out = []
        for c in data:
            tid, ttl = c.get("titleId"), c.get("title")
            if not tid or not ttl:
                continue
            img = ""
            if tid in image_map:
                img = image_map[tid]
            else:
                ci = c.get("courseImage") or c.get("image") or {}
                if isinstance(ci, dict):
                    img = ci.get("url") or ci.get("src") or ""
                elif isinstance(ci, str):
                    img = ci
                if img and "course-default-img" in img:
                    img = ""
            out.append({"titleId": tid, "label": ttl, "image": img})
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
                    "id": d.get("course", {}).get("id"),
                    "titleId": d.get("course", {}).get("titleId"),
                    "title": d.get("course", {}).get("title"),
                    "sections": d.get("course", {}).get("sections", {}),
                    "objects": d.get("course", {}).get("objects", {}),
                }
                STORE.cache_set(cache_key, json.dumps(compact), ttl=TOKEN_TTL)
            except Exception:
                pass
            return d
        except Exception:
            return None

    def course_internal_id(self, titleId):
        d = self.fetch_curriculum(titleId)
        if not d:
            return None
        return (d.get("course") or {}).get("id") or d.get("id")

    def fetch_video(self, titleId, unit_id):
        cid = self.course_internal_id(titleId)
        if not cid:
            return {"error": "no course id"}
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
            # check for assessmentV2 fallback
            a = self._assessment_meta(titleId, unit_id)
            if a:
                return a
        if v.get("type") == "wistia":
            return {
                "unit_id": unit_id,
                "title": v.get("title"),
                "type": "wistia",
                "sourceid": v.get("sourceid"),
                "duration": v.get("duration"),
                "batch": titleId,
            }
        # video endpoint returned nothing useful — try assessment
        a = self._assessment_meta(titleId, unit_id)
        if a:
            return a
        return {
            "unit_id": unit_id,
            "title": v.get("title"),
            "type": v.get("type"),
            "sourceid": v.get("sourceid"),
            "duration": v.get("duration"),
            "vimeo": v.get("vimeoid"),
            "batch": titleId,
        }

    def _assessment_meta(self, title_id, unit_id):
        """Look up assessmentV2 metadata from curriculum objects map."""
        d = self.fetch_curriculum(title_id)
        if not d:
            return None
        objs = ((d.get("course") or {}).get("objects")) or d.get("objects") or {}
        obj = objs.get(unit_id)
        if not obj:
            return None
        otype = obj.get("objectType") or ""
        if otype != "assessmentV2":
            return None
        data = obj.get("data") or {}
        return {
            "unit_id": unit_id,
            "title": obj.get("title") or "Assessment",
            "type": "assessment",
            "assessment_id": data.get("assessmentId"),
            "batch": title_id,
        }

    # ---------- assessment endpoints ----------

    def fetch_assessment_state(self, title_id, unit_id):
        """GET /api/assessment/state?sourceType=unit&objectId=<unitId>"""
        try:
            r = self.s.get(f"{BASE}/api/assessment/state",
                params={"sourceType": "unit", "objectId": unit_id},
                headers=self.h(f"{BASE}/path-player?courseid={title_id}&unit={unit_id}Unit"),
                timeout=TIMEOUT)
            if r.status_code != 200:
                return {"error": f"status {r.status_code}"}
            j = r.json()
            if not j.get("success", True):
                errs = j.get("errors") or []
                msg = errs[0].get("message") if errs and isinstance(errs[0], dict) else "assessment error"
                return {"error": msg}
            return j
        except Exception as e:
            return {"error": f"{type(e).__name__}: {e}"}

    def save_assessment(self, submission_id, title_id, unit_id, answers,
                        status="begun"):
        """PATCH /api/assessment/submission/<id>"""
        body = {"answers": answers, "status": status}
        try:
            r = self.s.patch(
                f"{BASE}/api/assessment/submission/{submission_id}",
                json=body,
                headers=self.h(f"{BASE}/path-player?courseid={title_id}&unit={unit_id}Unit"),
                timeout=TIMEOUT)
            if r.status_code != 200:
                return {"error": f"status {r.status_code}", "body": r.text[:400]}
            return r.json()
        except Exception as e:
            return {"error": f"{type(e).__name__}: {e}"}

    def submit_assessment(self, submission_id, title_id, unit_id, answers):
        """Submit — same PATCH but status=submitted."""
        return self.save_assessment(submission_id, title_id, unit_id,
                                    answers, status="submitted")

    # ---------- pdf ----------

    def get_pdf_filename(self, titleId, unit_id):
        d = self.fetch_curriculum(titleId)
        if not d:
            return (None, None)
        objs = ((d.get("course") or {}).get("objects")) or d.get("objects") or {}
        obj = objs.get(unit_id)
        if not obj:
            return (None, None)
        data = obj.get("data") or {}
        raw = data.get("pdf") or ""
        fname = raw.split("/", 1)[1] if "/" in raw else raw
        disp = data.get("pdf_name") or obj.get("title") or fname
        return (fname, disp) if fname else (None, None)

    def pdf_redirect(self, titleId, unit_id):
        fname, disp = self.get_pdf_filename(titleId, unit_id)
        if not fname:
            return {"error": "no pdf in curriculum"}
        try:
            r = self.s.get(f"{BASE}/api/unlock/pdf/{urllib.parse.quote(fname)}",
                params={"courseid": titleId, "unitId": unit_id, "json": ""},
                headers=self.h(f"{BASE}/path-player?courseid={titleId}&unit={unit_id}Unit"),
                timeout=TIMEOUT)
            j = r.json()
        except Exception as e:
            return {"error": f"{type(e).__name__}"}
        url = j.get("redirectUrl")
        if not url:
            return {"error": "no redirect"}
        return {"redirectUrl": url, "filename": fname, "display": disp}

    # ---------- wistia ----------

    def wistia_variants(self, sourceid):
        try:
            r = self.s.get(f"https://fast.wistia.com/embed/medias/{sourceid}.m3u8",
                           timeout=TIMEOUT)
            if r.status_code != 200:
                return {}
            out = {}
            lines = r.text.splitlines()
            for i, line in enumerate(lines):
                if line.startswith("#EXT-X-STREAM-INF"):
                    m = re.search(r'NAME="([^"]+)"', line)
                    key = m.group(1) if m else f"v{i}"
                    for j in range(i + 1, len(lines)):
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
_BATCH_CACHE_TTL_LOCAL = BATCH_CACHE_TTL


def get_batches_cached(acct):
    email = (acct.get("email") or "").lower()
    if not email:
        return []
    import time as _t
    now = _t.time()
    cached = _BATCH_CACHE.get(email)
    if cached and now - cached[0] < _BATCH_CACHE_TTL_LOCAL:
        return cached[1]
    try:
        s = ApnaSession(acct["email"], acct.get("token", ""))
        batches = s.fetch_batches()
        if batches:
            _BATCH_CACHE[email] = (now, batches)
        return batches if batches else (cached[1] if cached else [])
    except Exception:
        return cached[1] if cached else []


def find_session_for(titleId):
    for acct in STORE.get_accounts():
        batches = get_batches_cached(acct)
        if any(b.get("titleId") == titleId for b in batches):
            return ApnaSession(acct["email"], acct.get("token", ""))
    return None


def clear_batch_cache():
    _BATCH_CACHE.clear()
