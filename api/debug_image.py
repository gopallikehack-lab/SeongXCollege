"""Debug image map fetching."""
import json
import re

from flask import jsonify

from .apna import ApnaSession
from .config import BASE, TIMEOUT
from .store import STORE


def register(app):
    @app.route("/api/debug_image")
    def debug_image():
        accts = STORE.get_accounts()
        if not accts:
            return jsonify(error="no accounts")
        acct = accts[0]
        s = ApnaSession(acct["email"], acct.get("token",""))
        result = {"email": acct["email"]}
        try:
            r = s.s.get(f"{BASE}/start",
                headers={"Accept":"text/html,application/xhtml+xml",
                         "Origin": BASE, "Referer": f"{BASE}/start",
                         "token": s.token or ""},
                timeout=TIMEOUT)
            result["status"] = r.status_code
            result["size"] = len(r.text)
            result["has_site_affiliates"] = "SITE_AFFILIATES" in r.text
            result["body_head"] = r.text[:300]
            m = re.search(r'var SITE_AFFILIATES=(\{.*?\});', r.text, re.DOTALL)
            if m:
                try:
                    data = json.loads(m.group(1))
                    prods = data.get("products-migration-v4", []) or []
                    result["products_count"] = len(prods)
                    result["products"] = [
                        {"titleId": p.get("titleId"), "image": p.get("image")}
                        for p in prods
                    ]
                except Exception as e:
                    result["json_error"] = str(e)
            else:
                result["regex_match"] = False
        except Exception as e:
            result["error"] = f"{type(e).__name__}: {e}"
        return jsonify(result)
