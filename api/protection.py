"""Cloudflare Turnstile gate — protection page + verification route."""
import secrets
import urllib.parse

import requests as plain_requests
from flask import Blueprint, jsonify, redirect, request

from .config import BASE, TIMEOUT
from .store import STORE

# ============================================================
#   TURNSTILE KEYS  —  paste your real keys here
# ============================================================
TURNSTILE_SITE_KEY   = "0x4AAAAAAFYknbdvZc3cInpx"
TURNSTILE_SECRET_KEY = "0x4AAAAAAFYknSDQkm5oAl0PmaPIhSb1BgE"
# ============================================================

VERIFY_COOKIE = "se_verified"
VERIFY_TTL    = 60 * 60 * 24 * 30      # 30 days
VERIFY_URL    = "https://challenges.cloudflare.com/turnstile/v0/siteverify"

protection_bp = Blueprint("protection", __name__)


# ---------- cookie helpers ----------

def _verified():
    tok = request.cookies.get(VERIFY_COOKIE)
    if not tok:
        return False
    try:
        return STORE.cache_get(f"se_verified:{tok}") == "1"
    except Exception:
        return False


def _mark_verified(tok):
    try:
        STORE.cache_set(f"se_verified:{tok}", "1", ttl=VERIFY_TTL)
    except Exception:
        pass


# ---------- verification call to Cloudflare ----------

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


# ---------- public route the frontend calls ----------

@protection_bp.route("/api/verify", methods=["POST"])
def api_verify():
    body = request.get_json(silent=True) or {}
    token = (body.get("token") or "").strip()
    if not token:
        return jsonify(ok=False, error="missing token")

    ip = request.headers.get("x-forwarded-for", "").split(",")[0].strip() or request.remote_addr
    result = _siteverify(token, ip)

    if not result.get("success"):
        return jsonify(ok=False, error="challenge failed", detail=result.get("error-codes", []))

    tok = secrets.token_urlsafe(24)
    _mark_verified(tok)
    resp = jsonify(ok=True)
    resp.set_cookie(
        VERIFY_COOKIE, tok,
        max_age=VERIFY_TTL,
        httponly=True,
        samesite="Lax",
        secure=True,
    )
    return resp
