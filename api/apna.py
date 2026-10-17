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

SITE_ID = "62a6cd5e1e9e2fbf212d608d"
IMAGE_BASE = f"https://lwfiles.mycourse.app/{SITE_ID}-public"


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

    @staticmethod
    def _build_image_url(path):
        if not path:
            return ""
        if isinstance(path, str) and path.startswith("http"):
            return path
        if not path.startswith("/"):
            path = "/" + path
        return IMAGE_BASE + path

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

        out = []
        for c in (d.get("data") or []):
            tid, ttl = c.get("titleId"), c.get("title")
            if not tid or not ttl:
                continue
            st = c.get("settings") or {}
            img = self._build_image_url(st.get("image"))
            prog = c.get("progress") or {}
            pct = prog.get("percentage") if isinstance(prog, dict) else 0
            out.append({
                "titleId": tid,
                "label": ttl,
                "image": img,
                "bgcolor": st.get("bgcolor") or "",
                "progress": pct or 0,
            })
        return out

    def fetch_course_info(self, titleId):
        """Compact info about a course — title, subtitle, poster, and curriculum counts."""
        cache_key = f"cinfo:{titleId}"
        cached = STORE.cache_get(cache_key)
        if cached:
            try:
                return json.loads(cached)
            except Exception:
                pass
        try:
            r = self.s.get(f"{BASE}/api/course/{titleId}",
                           headers=self.h(f"{BASE}/path-player?courseid={titleId}"),
                           timeout=TIMEOUT)
            if r.status_code != 200:
                return None
            d = r.json()
            c = d.get("course") or d

            img = ""
            ci = c.get("courseImage") or {}
            if isinstance(ci, dict):
                img = ci.get("url") or ci.get("uncompressedUrl") or ""
            elif isinstance(ci, str):
                img = ci
            if img and "course-default-img" in img:
                img = ""

            sections = c.get("sections") or {}
            objects = c.get("objects") or {}
            sec_count = len(sections)
            unit_count = 0
            type_counts = {}
            for _sid, sec in sections.items():
                for u in (sec.get("learningPath") or []):
                    unit_count += 1
                    t = (u.get("type") or "unknown").lower()
                    type_counts[t] = type_counts.get(t, 0) + 1
            if not unit_count and objects:
                unit_count = len(objects)
                for u in objects.values():
                    t = (u.get("objectType") or "unknown").lower()
                    type_counts[t] = type_counts.get(t, 0) + 1

            info = {
                "titleId": titleId,
                "title": c.get("title") or titleId,
                "subtitle": c.get("keywords") or "",
                "image": img,
                "price": c.get("price"),
                "status": c.get("status"),
                "sections": sec_count,
                "units": unit_count,
                "types": type_counts,
            }
            try:
                STORE.cache_set(cache_key, json.dumps(info), ttl=TOKEN_TTL)
            except Exception:
                pass
            return info
        except Exception as e:
            print(f"[!] course_info {titleId}: {type(e).__name__}: {e}")
            return None

    @staticmethod
    def _patch_assessment_titles(sections, objects):
        if not sections or not objects:
            return
        for _sid, _sec in sections.items():
            for _u in (_sec.get("learningPath") or []):
                if (_u.get("type") or "") == "assessmentV2":
                    _obj = objects.get(_u.get("id")) or {}
                    _real = _obj.get("title")
                    if _real and _real != "Untitled":
                        _u["unitTitle"] = _real

    def fetch_curriculum(self, titleId):
        cache_key = f"curric:v4:{self.email}:{titleId}"
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
                sections = d.get("course", {}).get("sections", {}) or {}
                objects = d.get("course", {}).get("objects", {}) or {}
                self._patch_assessment_titles(sections, objects)
                compact = {
                    "id": d.get("course", {}).get("id"),
                    "titleId": d.get("course", {}).get("titleId"),
                    "title": d.get("course", {}).get("title"),
                    "sections": sections,
                    "objects": objects,
                }
                STORE.cache_set(cache_key, json.dumps(compact), ttl=TOKEN_TTL)
            except Exception as _e:
                print(f"[!] curriculum compact failed: {_e}")
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
        a = self._assessment_meta(titleId, unit_id)
        if a:
            return a
        
        # Check if it's a certificate
        d = self.fetch_curriculum(titleId)
        if d:
            objs = ((d.get("course") or {}).get("objects")) or d.get("objects") or {}
            obj = objs.get(unit_id)
            if obj and (obj.get("objectType") == "certificateV2"):
                return {
                    "unit_id": unit_id,
                    "title": obj.get("title") or "Certificate",
                    "type": "certificate",
                    "batch": titleId
                }

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
        if v.get("type") == "wistia":
            return {
                "unit_id": unit_id,
                "title": v.get("title"),
                "type": "wistia",
                "sourceid": v.get("sourceid"),
                "duration": v.get("duration"),
                "batch": titleId,
            }
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
        d = self.fetch_curriculum(title_id)
        if not d:
            return None
        objs = ((d.get("course") or {}).get("objects")) or d.get("objects") or {}
        obj = objs.get(unit_id)
        if not obj:
            return None
        if (obj.get("objectType") or "") != "assessmentV2":
            return None
        data = obj.get("data") or {}
        return {
            "unit_id": unit_id,
            "title": obj.get("title") or "Assessment",
            "type": "assessment",
            "assessment_id": data.get("assessmentId"),
            "batch": title_id,
        }

    # ---------- assessment ----------

    def fetch_assessment_state(self, title_id, unit_id, force_new=False):
        ref = f"{BASE}/path-player?courseid={title_id}&unit={unit_id}Unit"

        if force_new:
            try:
                ri = self.s.post(f"{BASE}/api/assessment/submission/init",
                    json={"sourceType": "unit", "objectId": unit_id,
                          "courseTitleId": title_id},
                    headers=self.h(ref), timeout=TIMEOUT)
                if ri.status_code == 200:
                    ji = ri.json()
                    if ji.get("assessment"):
                        return ji
            except Exception as e:
                print(f"[!] force init: {e}")

        try:
            r = self.s.get(f"{BASE}/api/assessment/state",
                params={"sourceType": "unit", "objectId": unit_id},
                headers=self.h(ref), timeout=TIMEOUT)
            if r.status_code != 200:
                return {"error": f"status {r.status_code}"}
            j = r.json()
            if not j.get("success", True):
                errs = j.get("errors") or []
                msg = errs[0].get("message") if errs and isinstance(errs[0], dict) else "assessment error"
                return {"error": msg}

            needs_init = False
            secs = ((j.get("assessment") or {}).get("sections")) or []
            for sec in secs:
                for blk in (sec.get("blocks") or []):
                    if "blockData" not in blk:
                        needs_init = True
                        break
                if needs_init:
                    break
            has_sub = bool(j.get("latestSubmission"))

            if needs_init and not has_sub:
                try:
                    ri = self.s.post(f"{BASE}/api/assessment/submission/init",
                        json={"sourceType": "unit", "objectId": unit_id,
                              "courseTitleId": title_id},
                        headers=self.h(ref), timeout=TIMEOUT)
                    if ri.status_code == 200:
                        ji = ri.json()
                        if ji.get("success", True) and ji.get("assessment"):
                            return ji
                except Exception:
                    pass

            return j
        except Exception as e:
            return {"error": f"{type(e).__name__}: {e}"}

    def save_assessment(self, submission_id, title_id, unit_id, answers,
                        status="begun"):
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
    cache_key = f"batches:{email}"

    # 1. Check local memory cache (instant)
    cached = _BATCH_CACHE.get(email)
    if cached and now - cached[0] < _BATCH_CACHE_TTL_LOCAL:
        return cached[1]

    # 2. Check Supabase cache (fast, survives cold starts)
    db_cached = STORE.cache_get(cache_key)
    if db_cached:
        try:
            data = json.loads(db_cached)
            if data.get("ts", 0) + BATCH_CACHE_TTL > now:
                _BATCH_CACHE[email] = (data["ts"], data["batches"])
                return data["batches"]
        except Exception:
            pass

    # 3. Fetch fresh from ApnaCollege
    try:
        s = ApnaSession(acct["email"], acct.get("token", ""))
        batches = s.fetch_batches()
        if batches:
            _BATCH_CACHE[email] = (now, batches)
            # Save to Supabase
            try:
                STORE.cache_set(cache_key, json.dumps({"ts": now, "batches": batches}), ttl=BATCH_CACHE_TTL)
            except Exception:
                pass
            return batches
        # If failed, return whatever cache we had
        return (cached[1] if cached else [])
    except Exception:
        return (cached[1] if cached else [])


def find_session_for(titleId):
    for acct in STORE.get_accounts():
        batches = get_batches_cached(acct)
        if any(b.get("titleId") == titleId for b in batches):
            s = ApnaSession(acct["email"], acct.get("token", ""))
            
            # TEST if this account works before returning it
            cid = s.course_internal_id(titleId)
            if cid:
                return s
            else:
                print(f"[!] Token dead for {acct['email']} on {titleId}, rotating to next user...")
                continue # Try the next account
                
    return None


def clear_batch_cache():
    _BATCH_CACHE.clear()
