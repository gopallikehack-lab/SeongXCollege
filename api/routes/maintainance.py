"""Maintenance mode blueprint — global on/off toggle stored in Supabase cache."""
from flask import Blueprint, jsonify, request

from ..store import STORE

maintenance_bp = Blueprint("maintenance", __name__)

_MAINT_KEY = "site:maintenance"


def is_on():
    try:
        v = STORE.cache_get(_MAINT_KEY)
        return v == "1"
    except Exception:
        return False


def set_on(on: bool):
    try:
        STORE.cache_set(_MAINT_KEY, "1" if on else "0", ttl=60 * 60 * 24 * 365)
        return True
    except Exception:
        return False
