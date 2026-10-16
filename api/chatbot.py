"""SEONG AI — server-side proxy to the iceyyy.dev LLM endpoint."""
import json

import requests as plain_requests
from flask import Blueprint, jsonify, request

chat_bp = Blueprint("chatbot", __name__)

# ============================================================
#   API CONFIG  —  baked in, not env
# ============================================================
API_URL   = "https://api.iceyyy.dev/v1/messages"
API_KEY   = "sk-ice-93j0ib5etqf32a4qwjh09vx7ruap0yp9ghim0p54j8906x8k"
MODELS    = ["deepseek-v4-pro", "mimo-v2.5-pro", "glm-5.3-flash"]
TIMEOUT   = 60
MAX_TOK   = 2048
# ============================================================

SYSTEM_PROMPT = (
    "You are SEONG AI — the official AI assistant of the SeongEraStudy platform. "
    "Your job is to help students with their doubts: coding, DSA, math, aptitude, "
    "physics, chemistry, and any subject they are learning on SeongEraStudy. "
    "You are friendly, direct, and clear. Use short paragraphs and simple language. "
    "For code questions, always give working code and briefly explain it. "
    "For math/aptitude, show the steps, not just the answer. "
    "If you don't know something, say so honestly. "
    "You were created by 𝑮𝒊𝒖𝒎 𝑺𝒆𝒐𝒏𝒈 𝑱𝒆𝒆 for the students of SeongEraStudy. "
    "Do not mention any other AI providers or companies."
)


def _call_model(model, messages):
    try:
        r = plain_requests.post(
            API_URL,
            headers={
                "x-api-key": API_KEY,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
            json={
                "model": model,
                "max_tokens": MAX_TOK,
                "system": SYSTEM_PROMPT,
                "messages": messages,
            },
            timeout=TIMEOUT,
        )
        if r.status_code != 200:
            return None, f"status {r.status_code}: {r.text[:200]}"
        d = r.json()
        text = ""
        try:
            for block in (d.get("content") or []):
                if block.get("type") == "text":
                    text += block.get("text", "")
        except Exception:
            pass
        if not text:
            return None, "empty response"
        return text, None
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"


@chat_bp.route("/api/chat", methods=["POST"])
def api_chat():
    body = request.get_json(silent=True) or {}
    messages = body.get("messages") or []
    if not isinstance(messages, list) or not messages:
        return jsonify(ok=False, error="messages required")

    # sanitize: keep only role + content, cap history at 20
    clean = []
    for m in messages[-20:]:
        if not isinstance(m, dict):
            continue
        role = m.get("role")
        content = m.get("content")
        if role in ("user", "assistant") and isinstance(content, str):
            clean.append({"role": role, "content": content})
    if not clean or clean[-1]["role"] != "user":
        return jsonify(ok=False, error="last message must be from user")

    last_error = None
    for model in MODELS:
        text, err = _call_model(model, clean)
        if text:
            return jsonify(ok=True, reply=text, model=model)
        last_error = err
        print(f"[chat] {model} failed: {err}")

    return jsonify(ok=False, error=f"all models failed: {last_error}")
