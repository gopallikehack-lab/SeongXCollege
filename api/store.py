"""Supabase-backed store."""
import json
import time
import urllib.parse

import requests as plain_requests

from .config import SUPABASE_URL, SUPABASE_KEY, TOKEN_TTL


class SupabaseStore:
    def __init__(self):
        self.url = SUPABASE_URL
        self.key = SUPABASE_KEY
        self.enabled = bool(self.url and self.key)
        self._mem_accounts = []
        self._mem_cache = {}

    def _headers(self, prefer="return=minimal"):
        return {
            "apikey": self.key,
            "Authorization": f"Bearer {self.key}",
            "Content-Type": "application/json",
            "Prefer": prefer,
        }

    def get_accounts(self):
        if not self.enabled:
            return self._mem_accounts
        try:
            r = plain_requests.get(
                f"{self.url}/rest/v1/accounts?select=*&order=added_at.desc",
                headers=self._headers(), timeout=10)
            if r.status_code == 200:
                return r.json()
            print(f"[!] supabase get {r.status_code}: {r.text[:200]}")
        except Exception as e:
            print(f"[!] supabase get: {e}")
        return []

    def add_account(self, email, token, label=""):
        if not self.enabled:
            self._mem_accounts.append({
                "email": email, "token": token, "label": label,
                "added_at": time.time(), "token_updated_at": time.time(),
            })
            return True, "added"
        try:
            r = plain_requests.post(
                f"{self.url}/rest/v1/accounts",
                headers=self._headers(),
                json={"email": email.lower(), "token": token, "label": label},
                timeout=10)
            if r.status_code in (200, 201):
                return True, "added"
            if r.status_code == 409 or "duplicate" in (r.text or "").lower():
                return False, "account already exists"
            return False, f"supabase {r.status_code}: {r.text[:200]}"
        except Exception as e:
            return False, f"{type(e).__name__}: {e}"

    def remove_account(self, email):
        if not self.enabled:
            self._mem_accounts = [a for a in self._mem_accounts
                                  if a.get("email","").lower() != email.lower()]
            return True
        try:
            r = plain_requests.delete(
                f"{self.url}/rest/v1/accounts?email=eq.{urllib.parse.quote(email.lower())}",
                headers=self._headers(), timeout=10)
            return r.status_code in (200, 204)
        except Exception:
            return False

    def cache_get(self, key):
        if not self.enabled:
            v = self._mem_cache.get(key)
            if v and v.get("expires_at", 0) > time.time():
                return v["value"]
            return None
        try:
            r = plain_requests.get(
                f"{self.url}/rest/v1/cache?key=eq.{urllib.parse.quote(key)}&select=value,expires_at",
                headers=self._headers(), timeout=10)
            if r.status_code == 200:
                rows = r.json()
                if rows and rows[0].get("value"):
                    return rows[0]["value"]
        except Exception:
            pass
        return None

    def cache_set(self, key, value, ttl=TOKEN_TTL):
        if not self.enabled:
            self._mem_cache[key] = {"value": value, "expires_at": time.time()+ttl}
            return
        try:
            headers = self._headers(prefer="resolution=merge-duplicates")
            plain_requests.post(
                f"{self.url}/rest/v1/cache",
                headers=headers,
                json={"key": key, "value": value,
                      "expires_at": time.strftime("%Y-%m-%dT%H:%M:%S+00:00",
                                                  time.gmtime(time.time()+ttl))},
                timeout=10)
        except Exception:
            pass


STORE = SupabaseStore()
