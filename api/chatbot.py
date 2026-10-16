"""SEONG AI — server-side proxy to aihubmix.com with model fallback."""
import json

import requests as plain_requests
from flask import Blueprint, jsonify, request

chat_bp = Blueprint("chatbot", __name__)

# ============================================================
#   API CONFIG
# ============================================================
API_URL = "https://aihubmix.com/v1/chat/completions"
API_KEY = "sk-kxbD9ARI00KDOjo4F3A5Ca376d134e289c7d0c904664B48b"
TIMEOUT = 90
MAX_TOK = 4096

# Fallback order — first one tried first. If it fails, next.
MODEL_CHAIN = [
    "coding-glm-5.3-flash-free",     # glm-5.3-flash  · fast, solid
    "xiaomi-mimo-v2.6-pro-free",     # mimo-v2.6-pro  · reasoning + voice
    "kimi-for-coding-free",          # kimi · long context
    "minimax-m2.7-free",             # minimax m2.7
    "ling-3.0-flash-free",           # ling 3.0 flash
    "dots-3-note-preview-free",      # dots 3 note preview
]

# models the widget exposes in the picker (order = display order)
MODEL_LIST = [
    {"id": "coding-glm-5.3-flash-free",  "name": "GLM 5.3 Flash",   "tag": "fast · coding"},
    {"id": "xiaomi-mimo-v2.6-pro-free",  "name": "MiMo V2.6 Pro",   "tag": "reasoning · voice"},
    {"id": "kimi-for-coding-free",       "name": "Kimi for Coding", "tag": "long context"},
    {"id": "minimax-m2.7-free",          "name": "MiniMax M2.7",    "tag": "balanced"},
    {"id": "ling-3.0-flash-free",        "name": "Ling 3.0 Flash",  "tag": "flash"},
    {"id": "dots-3-note-preview-free",   "name": "Dots 3 Note",     "tag": "preview"},
]
DEFAULT_MODEL = "coding-glm-5.3-flash-free"
# ============================================================

SYSTEM_PROMPT = (
    "You are SEONG AI — the official AI assistant of the SeongEraStudy platform. "
    "Your job is to help students with their doubts: coding, DSA, math, aptitude, "
    "physics, chemistry, and any subject they study on SeongEraStudy. "
    "Be friendly, direct, and clear. Use short paragraphs and simple language. "
    "For code questions, always give working code and briefly explain it. "
    "For math, show the steps, not just the answer. "
    "If you don't know something, say so honestly. "
    "You were created by 𝑮𝒊𝒖𝒎 𝑺𝒆𝒐𝒏𝒈 𝑱𝒆𝒆 for the students of SeongEraStudy. "
    "Do not mention any other AI providers or companies."
)


def _call_model(model_id, messages):
    payload = {
        "model": model_id,
        "messages": [{"role": "system", "content": SYSTEM_PROMPT}] + messages,
        "max_tokens": MAX_TOK,
        "stream": False,
    }
    try:
        r = plain_requests.post(
            API_URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=TIMEOUT,
        )
        if r.status_code != 200:
            return None, f"status {r.status_code}: {r.text[:200]}"
        d = r.json()
        choices = d.get("choices") or []
        if not choices:
            return None, f"no choices: {r.text[:200]}"
        text = (choices[0].get("message") or {}).get("content") or ""
        if not text:
            return None, "empty content"
        return text, None
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"


def _sanitize(messages):
    clean = []
    for m in messages[-20:]:
        if not isinstance(m, dict):
            continue
        role = m.get("role")
        content = m.get("content")
        if role in ("user", "assistant") and isinstance(content, str):
            clean.append({"role": role, "content": content})
    return clean


@chat_bp.route("/api/chat/models")
def api_chat_models():
    return jsonify(models=MODEL_LIST, default=DEFAULT_MODEL)


@chat_bp.route("/api/chat", methods=["POST"])
def api_chat():
    body = request.get_json(silent=True) or {}
    messages = body.get("messages") or []
    chosen = body.get("model") or DEFAULT_MODEL

    if not isinstance(messages, list) or not messages:
        return jsonify(ok=False, error="messages required")

    clean = _sanitize(messages)
    if not clean or clean[-1]["role"] != "user":
        return jsonify(ok=False, error="last message must be from user")

    valid_ids = {m["id"] for m in MODEL_LIST}
    if chosen not in valid_ids:
        chosen = DEFAULT_MODEL

    # try chosen first, then the rest of the chain in order
    order = [chosen] + [m for m in MODEL_CHAIN if m != chosen]

    last_error = None
    for model in order:
        text, err = _call_model(model, clean)
        if text:
            return jsonify(ok=True, reply=text, model=model)
        last_error = err
        print(f"[chat] {model} failed: {err}")

    return jsonify(ok=False, error=f"all models failed: {last_error}")
