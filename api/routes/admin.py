"""Admin routes."""
import secrets
import time

from flask import Blueprint, jsonify, make_response, redirect, render_template_string, request

from ..apna import ApnaSession, clear_batch_cache
from ..config import ADMIN_CODE, ADMIN_COOKIE, ADMIN_TTL
from ..pages import ADMIN_PAGE, LOGIN_PAGE
from ..store import STORE


admin_bp = Blueprint("admin", __name__)


def _current_admin():
    tok = request.cookies.get(ADMIN_COOKIE)
    if not tok:
        return False
    return STORE.cache_get(f"admin:{tok}") == "1"


def _require_admin(f):
    from functools import wraps
    @wraps(f)
    def wrap(*a, **kw):
        if not _current_admin():
            return jsonify(error="admin required"), 401
        return f(*a, **kw)
    return wrap


@admin_bp.route("/admin", methods=["GET", "POST"])
def admin_route():
    if request.method == "GET":
        if _current_admin():
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


@admin_bp.route("/logout", methods=["POST", "GET"])
def logout():
    tok = request.cookies.get(ADMIN_COOKIE)
    if tok:
        STORE.cache_set(f"admin:{tok}", "0", ttl=10)
    resp = make_response(redirect("/"))
    resp.delete_cookie(ADMIN_COOKIE)
    return resp


@admin_bp.route("/api/admin/accounts", methods=["GET", "POST", "DELETE"])
@_require_admin
def admin_accounts():
    if request.method == "GET":
        out = []
        for a in STORE.get_accounts():
            e = a["email"]; u, _, d = e.partition("@")
            masked = (u[:2] + "*" * max(3, len(u)-4) + u[-2:]) + "@" + d if len(u) > 4 else u[:1] + "*" * (len(u)-1) + "@" + d
            tok = a.get("token", "") or ""
            try:
                added_ts = time.mktime(time.strptime(a["added_at"][:19], "%Y-%m-%dT%H:%M:%S")) if isinstance(a.get("added_at"), str) else a.get("added_at", time.time())
                updated_ts = time.mktime(time.strptime(a["token_updated_at"][:19], "%Y-%m-%dT%H:%M:%S")) if isinstance(a.get("token_updated_at"), str) else a.get("token_updated_at", time.time())
            except Exception:
                added_ts = updated_ts = time.time()
            age = time.time() - updated_ts
            if age > 7 * 24 * 3600:
                cls, txt = "token-bad", "expired"
            elif age > 6 * 24 * 3600:
                cls, txt = "token-warn", "expiring soon"
            else:
                cls, txt = "token-ok", f"valid · {int((7*24*3600-age)/3600)}h left"
            out.append({
                "email": e, "display": masked, "label": a.get("label", ""),
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
        clear_batch_cache()
        return jsonify(ok=True)
    if request.method == "DELETE":
        b = request.get_json(silent=True) or {}
        email = b.get("email", "")
        ok = STORE.remove_account(email)
        clear_batch_cache()
        return jsonify(ok=ok)


@admin_bp.route("/api/admin/accounts/bulk", methods=["POST"])
@_require_admin
def admin_accounts_bulk():
    body = request.get_json(silent=True) or {}
    accounts = body.get("accounts") or []
    if not isinstance(accounts, list):
        return jsonify(error="accounts must be a list")

    added, exists, failed = [], [], []
    existing_emails = {a["email"].lower() for a in STORE.get_accounts()}

    for item in accounts:
        email = (item.get("email") or "").strip().lower()
        token = (item.get("token") or "").strip()
        label = item.get("label") or ""
        if not email or not token:
            failed.append({"email": email or "?", "reason": "missing email or token"})
            continue
        if email in existing_emails:
            exists.append(email)
            continue

        s = ApnaSession(email, token)
        ok, detail = s.verify()
        if not ok:
            failed.append({"email": email, "reason": f"invalid token: {detail}"})
            continue

        ok2, msg = STORE.add_account(email, token, label)
        if ok2:
            added.append(email)
            existing_emails.add(email)
        else:
            failed.append({"email": email, "reason": msg})

    if added:
        clear_batch_cache()

    return jsonify(
        ok=True,
        added=added,
        exists=exists,
        failed=failed,
        total_added=len(added),
        total_exists=len(exists),
        total_failed=len(failed),
    )


@admin_bp.route("/api/admin/accounts/bulk_delete", methods=["POST"])
@_require_admin
def admin_accounts_bulk_delete():
    """Bulk remove accounts. If emails list is empty -> delete ALL."""
    body = request.get_json(silent=True) or {}
    emails = body.get("emails") or []
    delete_all = bool(body.get("all"))

    if delete_all:
        existing = [a["email"] for a in STORE.get_accounts()]
        removed = []
        for e in existing:
            if STORE.remove_account(e):
                removed.append(e)
        clear_batch_cache()
        return jsonify(ok=True, removed=removed, total=len(removed))

    if not isinstance(emails, list) or not emails:
        return jsonify(error="emails required")

    removed, failed = [], []
    for e in emails:
        if STORE.remove_account(e):
            removed.append(e)
        else:
            failed.append(e)
    if removed:
        clear_batch_cache()
    return jsonify(ok=True, removed=removed, failed=failed, total=len(removed))


@admin_bp.route("/api/admin/test")
@_require_admin
def admin_test():
    results = []
    for acct in STORE.get_accounts():
        s = ApnaSession(acct["email"], acct.get("token", ""))
        ok, detail = s.verify()
        results.append({"email": acct["email"], "ok": ok, "error": None if ok else detail})
    return jsonify(results=results)


@admin_bp.route("/api/admin/clear_batch_cache")
@_require_admin
def admin_clear_batch_cache():
    clear_batch_cache()
    return jsonify(ok=True)


@admin_bp.route("/api/admin/maintenance", methods=["GET", "POST"])
@_require_admin
def admin_maintenance():
    from .maintenance import is_on, set_on
    if request.method == "GET":
        return jsonify(on=is_on())
    body = request.get_json(silent=True) or {}
    on = bool(body.get("on"))
    ok = set_on(on)
    return jsonify(ok=ok, on=on)
