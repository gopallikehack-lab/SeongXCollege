"""Cloudflare Turnstile gate — protection page + verification route."""
import json
import secrets
import time

import requests as plain_requests
from flask import Blueprint, jsonify, request

from .store import STORE

# ============================================================
#   TURNSTILE KEYS
# ============================================================
TURNSTILE_SITE_KEY   = "0x4AAAAAAFYknbdvZc3cInpx"
TURNSTILE_SECRET_KEY = "0x4AAAAAAFYknSDQkm5oAl0PmaPIhSb1BgE"
# ============================================================

VERIFY_COOKIE   = "se_verified"
VERIFY_COOKIE_TTL = 60 * 60              # cookie itself lives 1 hour
VERIFY_CACHE_TTL  = 60 * 60              # server-side record lives 1 hour
VERIFY_URL      = "https://challenges.cloudflare.com/turnstile/v0/siteverify"

protection_bp = Blueprint("protection", __name__)


def _verified():
    """Return True only if the user has a valid cookie AND it's under 1 hour old."""
    tok = request.cookies.get(VERIFY_COOKIE)
    if not tok:
        return False
    try:
        raw = STORE.cache_get(f"se_verified:{tok}")
        if not raw:
            return False
        # stored as JSON: {"at": <unix_ts>}
        try:
            data = json.loads(raw)
            ts = float(data.get("at", 0))
        except Exception:
            ts = float(raw)
        age = time.time() - ts
        if age < 0 or age > VERIFY_CACHE_TTL:
            return False
        return True
    except Exception:
        return False


def _mark_verified(tok):
    try:
        STORE.cache_set(
            f"se_verified:{tok}",
            json.dumps({"at": time.time()}),
            ttl=VERIFY_CACHE_TTL,
        )
    except Exception:
        pass


def _siteverify(token, ip):
    try:
        r = plain_requests.post(
            VERIFY_URL,
            data={
                "secret":   TURNSTILE_SECRET_KEY,
                "response": token,
                "remoteip": ip,
            },
            timeout=10,
        )
        return r.json()
    except Exception as e:
        return {"success": False, "error-codes": [f"network:{e}"]}


@protection_bp.route("/api/verify", methods=["POST"])
def api_verify():
    body = request.get_json(silent=True) or {}
    token = (body.get("token") or "").strip()
    if not token:
        return jsonify(ok=False, error="missing token")

    ip = (request.headers.get("x-forwarded-for", "").split(",")[0].strip()
          or request.remote_addr)
    result = _siteverify(token, ip)

    if not result.get("success"):
        return jsonify(ok=False, error="challenge failed",
                       detail=result.get("error-codes", []))

    tok = secrets.token_urlsafe(24)
    _mark_verified(tok)
    resp = jsonify(ok=True)
    resp.set_cookie(
        VERIFY_COOKIE, tok,
        max_age=VERIFY_COOKIE_TTL,
        httponly=True,
        samesite="Lax",
        secure=True,
    )
    return resp
