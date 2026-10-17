"""Wakeup route for Vercel Cron to prevent cold starts."""
from flask import Blueprint, jsonify
from ..apna import get_batches_cached
from ..store import STORE

wakeup_bp = Blueprint("wakeup", __name__)

@wakeup_bp.route("/api/wakeup")
def api_wakeup():
    # Fetch first account's batches to keep the server warm and cache fresh
    accts = STORE.get_accounts()
    if accts:
        get_batches_cached(accts[0])
    return jsonify(ok=True, msg="warm")
