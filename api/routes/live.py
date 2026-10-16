"""Live stats routes — total batches across all accounts."""
from flask import Blueprint, jsonify

from ..apna import get_batches_cached
from ..store import STORE


live_bp = Blueprint("live", __name__)


@live_bp.route("/api/live/stats")
def api_live_stats():
    seen = {}
    for acct in STORE.get_accounts():
        try:
            for b in get_batches_cached(acct):
                tid = b.get("titleId")
                if tid and tid not in seen:
                    seen[tid] = {
                        "titleId": tid,
                        "label": b.get("label", tid),
                        "image": b.get("image", ""),
                    }
        except Exception:
            continue
    return jsonify(total=len(seen), batches=list(seen.values()))
