"""Public routes."""
from flask import Blueprint, jsonify, render_template_string

from ..apna import (
    ApnaSession, get_batches_cached, find_session_for,
)
from ..config import UPI_ID, QR_IMAGE
from ..pages import MAIN_PAGE
from ..store import STORE


public_bp = Blueprint("public", __name__)


@public_bp.route("/")
def index():
    html = (MAIN_PAGE
            .replace("__UPI_ID__", UPI_ID)
            .replace("__QR_IMAGE__", QR_IMAGE))
    return render_template_string(html)


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
