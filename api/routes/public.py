"""Public routes."""
from flask import Blueprint, jsonify, redirect, render_template_string, request

from ..apna import (
    ApnaSession, get_batches_cached, find_session_for,
)
from ..config import UPI_ID, QR_IMAGE, ADMIN_COOKIE
from ..pages import MAIN_PAGE
from ..pages.maintenance import MAINTENANCE_PAGE
from ..pages.protection import PROTECTION_PAGE
from ..protection import _verified
from ..routes.maintenance import is_on as maint_on
from ..store import STORE


public_bp = Blueprint("public", __name__)


@public_bp.route("/favicon.ico")
def favicon():
    return redirect(
        "https://i.ibb.co/GQvZNJ5x/file-00000000a2d082088bb8b30c95b7d8b9.png",
        code=302,
    )


def _is_admin():
    tok = request.cookies.get(ADMIN_COOKIE)
    if not tok:
        return False
    try:
        return STORE.cache_get(f"admin:{tok}") == "1"
    except Exception:
        return False


@public_bp.route("/")
def index():
    if _is_admin():
        html = (MAIN_PAGE
                .replace("__UPI_ID__", UPI_ID)
                .replace("__QR_IMAGE__", QR_IMAGE))
        return render_template_string(html)

    if not _verified():
        return render_template_string(PROTECTION_PAGE)

    if maint_on():
        return render_template_string(MAINTENANCE_PAGE)

    html = (MAIN_PAGE
            .replace("__UPI_ID__", UPI_ID)
            .replace("__QR_IMAGE__", QR_IMAGE))
    return render_template_string(html)
    
  from ..pages.certificate import CERTIFICATE_PAGE

@public_bp.route("/certificate")
def certificate():
    course = request.args.get("course", "Unknown Course")
    name = request.args.get("name", "Student")
    html = (CERTIFICATE_PAGE
            .replace("__COURSE_NAME__", course)
            .replace("__USER_NAME__", name))
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
                    "image": b.get("image", ""),
                    "progress": b.get("progress", 0),
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
                {"id": u.get("id"), "title": u.get("unitTitle", ""), "type": u.get("type", "")}
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
        s = ApnaSession(accts[0]["email"], accts[0].get("token", ""))
        return jsonify(variants=s.wistia_variants(sourceid))
    return jsonify(variants={})


# ---------- batch info ----------

@public_bp.route("/api/batch-info/<titleId>")
def api_batch_info(titleId):
    s = find_session_for(titleId)
    if not s:
        return jsonify(error="no account has access"), 404
    info = s.fetch_course_info(titleId)
    if not info:
        return jsonify(error="failed to fetch info"), 500
    return jsonify(info)


# ---------- assessment ----------

@public_bp.route("/api/assessment/<titleId>/<unit_id>")
def api_assessment_state(titleId, unit_id):
    s = find_session_for(titleId)
    if not s:
        return jsonify(error="no account has access"), 404
    force = request.args.get("retake") == "1"
    return jsonify(s.fetch_assessment_state(titleId, unit_id, force_new=force))


@public_bp.route("/api/assessment/save/<titleId>/<unit_id>", methods=["POST"])
def api_assessment_save(titleId, unit_id):
    s = find_session_for(titleId)
    if not s:
        return jsonify(error="no account has access"), 404
    body = request.get_json(silent=True) or {}
    sub_id = body.get("submission_id")
    answers = body.get("answers") or []
    if not sub_id:
        return jsonify(error="submission_id required")
    return jsonify(s.save_assessment(sub_id, titleId, unit_id, answers, status="begun"))


@public_bp.route("/api/assessment/submit/<titleId>/<unit_id>", methods=["POST"])
def api_assessment_submit(titleId, unit_id):
    s = find_session_for(titleId)
    if not s:
        return jsonify(error="no account has access"), 404
    body = request.get_json(silent=True) or {}
    sub_id = body.get("submission_id")
    answers = body.get("answers") or []
    if not sub_id:
        return jsonify(error="submission_id required")
    return jsonify(s.submit_assessment(sub_id, titleId, unit_id, answers))
