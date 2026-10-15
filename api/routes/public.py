"""Public routes."""
import base64
import hashlib
import hmac
import json

from flask import Blueprint, jsonify, make_response, render_template_string, request

from ..apna import (
    ApnaSession, get_batches_cached, find_session_for,
)
from ..config import UPI_ID, QR_IMAGE, SECRET_KEY, ENROLL_COOKIE, ENROLL_TTL
from ..pages import MAIN_PAGE
from ..store import STORE


public_bp = Blueprint("public", __name__)


# ---------- enrolled cookie helpers ----------
def _sign(value: str) -> str:
    """HMAC-SHA256 signature (hex) of the value."""
    return hmac.new(SECRET_KEY.encode(), value.encode(), hashlib.sha256).hexdigest()


def _encode_enrolled(ids: list[str]) -> str:
    """Pack the list into 'b64.signature' string."""
    raw = ",".join(ids).encode()
    b64 = base64.urlsafe_b64encode(raw).decode().rstrip("=")
    return f"{b64}.{_sign(b64)[:32]}"


def _decode_enrolled(cookie_val: str) -> list[str]:
    """Verify and unpack. Returns [] if invalid."""
    if not cookie_val or "." not in cookie_val:
        return []
    try:
        b64, sig = cookie_val.rsplit(".", 1)
        expected = _sign(b64)[:32]
        if not hmac.compare_digest(sig, expected):
            return []
        # add padding
        pad = "=" * (-len(b64) % 4)
        raw = base64.urlsafe_b64decode(b64 + pad).decode()
        if not raw:
            return []
        return [x for x in raw.split(",") if x]
    except Exception:
        return []


def _current_enrolled() -> list[str]:
    return _decode_enrolled(request.cookies.get(ENROLL_COOKIE, ""))


# ---------- pages ----------
@public_bp.route("/")
def index():
    html = (MAIN_PAGE
            .replace("__UPI_ID__", UPI_ID)
            .replace("__QR_IMAGE__", QR_IMAGE))
    return render_template_string(html)


# ---------- batches ----------
@public_bp.route("/api/batches")
def api_batches():
    seen = {}
    for acct in STORE.get_accounts():
        for b in get_batches_cached(acct):
            tid = b.get("titleId")
            if tid and tid not in seen:
                seen[tid] = {
                    "titleId": tid,
                    "label": b.get("label", tid),
                    "image": b.get("image", "")
                }
    return jsonify(batches=list(seen.values()))


# ---------- enroll ----------
@public_bp.route("/api/enroll", methods=["GET", "POST", "DELETE"])
def api_enroll():
    enrolled = _current_enrolled()
    if request.method == "GET":
        return jsonify(enrolled=enrolled)

    body = request.get_json(silent=True) or {}
    title_id = (body.get("titleId") or "").strip()
    if not title_id:
        return jsonify(error="titleId required"), 400

    if request.method == "POST":
        if title_id not in enrolled:
            enrolled.append(title_id)
    elif request.method == "DELETE":
        enrolled = [x for x in enrolled if x != title_id]

    cookie_val = _encode_enrolled(enrolled)
    resp = make_response(jsonify(ok=True, enrolled=enrolled))
    resp.set_cookie(
        ENROLL_COOKIE, cookie_val,
        max_age=ENROLL_TTL,
        httponly=False,   # JS needs to read this to update the UI
        samesite="Lax",
        secure=request.is_secure,
    )
    return resp


# ---------- sections / video / pdf ----------
@public_bp.route("/api/sections/<titleId>")
def api_sections(titleId):
    s = find_session_for(titleId)
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
            "units": [
                {"id": u.get("id"), "title": u.get("unitTitle",""), "type": u.get("type","")}
                for u in sec.get("learningPath", [])
            ],
        })
    return jsonify(sections=out)


@public_bp.route("/api/video/<titleId>/<unit_id>")
def api_video(titleId, unit_id):
    s = find_session_for(titleId)
    if not s:
        return jsonify(error="no account has access"), 404
    return jsonify(s.fetch_video(titleId, unit_id))


@public_bp.route("/api/pdf/<titleId>/<unit_id>")
def api_pdf(titleId, unit_id):
    s = find_session_for(titleId)
    if not s:
        return jsonify(error="no account has access"), 404
    return jsonify(s.pdf_redirect(titleId, unit_id))


@public_bp.route("/api/variants/<sourceid>")
def api_variants(sourceid):
    accts = STORE.get_accounts()
    if accts:
        s = ApnaSession(accts[0]["email"], accts[0].get("token",""))
        return jsonify(variants=s.wistia_variants(sourceid))
    return jsonify(variants={})
