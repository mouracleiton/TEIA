#!/usr/bin/env python3
"""
SKYNETchat OpenAI-Compatible API Proxy v2.2
==========================================
Transforma a API interna do skynetchat.net em uma API compatível com OpenAI.

COMO USAR:
  1. Extraia seus cookies do skynetchat.net (veja get_cookies.py)
  2. export SKYNET_COOKIE="cookie_string_aqui"
     (ou SKYNET_BASE se precisar de mirror/fork)
  3. python3 server.py

ENDPOINTS:
  POST /v1/chat/completions    -> Chat completions (streaming + não-streaming)
  GET  /v1/models              -> Lista de modelos
  GET  /health                 -> Health check

TESTE:
  curl http://localhost:8080/v1/chat/completions \\
    -H "Content-Type: application/json" \\
    -d '{"model":"skynet","messages":[{"role":"user","content":"Ola!"}]}'
"""

import os
import json
import time
import uuid
import traceback
import httpx
from pathlib import Path
from typing import Optional
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse

app = FastAPI(title="SKYNETchat OpenAI Proxy", version="2.2.0")

# Config via env (override para testes / mirrors)
SKYNET_BASE = os.environ.get("SKYNET_BASE", "https://skynetchat.net").rstrip("/")
SKYNET_CHAT = f"{SKYNET_BASE}/api/chat-V3"

# Cookie sources in priority order:
# 1. env var SKYNET_COOKIE
# 2. .skynet_cookie file next to server.py (absolute resolved)
# 3. fallback empty
_COOKIE_FILE = Path(__file__).resolve().parent / ".skynet_cookie"


def _load_cookie() -> str:
    env = os.environ.get("SKYNET_COOKIE", "")
    if env:
        return env
    if _COOKIE_FILE.exists():
        return _COOKIE_FILE.read_text().strip()
    # Also check common hermes location as last resort
    hermes_cookie = Path.home() / ".hermes" / ".skynet_cookie"
    if hermes_cookie.exists():
        return hermes_cookie.read_text().strip()
    return ""


SKYNET_COOKIE = _load_cookie()


def get_headers(extra_cookie: str = "") -> dict:
    """Retorna headers necessários para o skynetchat."""
    cookie = extra_cookie or SKYNET_COOKIE
    headers = {
        "accept": "*/*",
        "accept-language": "pt-BR,pt;q=0.9,en;q=0.8",
        "content-type": "application/json",
        "origin": SKYNET_BASE,
        "referer": f"{SKYNET_BASE}/",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/150.0.0.0 Safari/537.36",
    }
    if cookie:
        headers["cookie"] = cookie
    return headers


def openai_to_skynet(messages: list) -> dict:
    """
    Converte formato OpenAI messages -> formato SKYNETchat.

    OpenAI:
      [{"role": "user", "content": "texto"}]

    SKYNET:
      {"id": "...", "messages": [{"id": "...", "role": "user",
       "parts": [{"type": "text", "text": "..."}]}], "trigger": "submit-message"}
    """
    skynet_messages = []
    for msg in messages:
        content = msg.get("content", "")
        if isinstance(content, list):
            text_parts = []
            for part in content:
                if isinstance(part, dict) and part.get("type") == "text":
                    text_parts.append(part.get("text", ""))
                elif isinstance(part, str):
                    text_parts.append(part)
            content = "\n".join(text_parts)

        skynet_messages.append({
            "id": f"{msg.get('role', 'user')}-{int(time.time() * 1000)}",
            "role": msg.get("role", "user"),
            "parts": [{"type": "text", "text": content}]
        })

    return {
        "id": uuid.uuid4().hex[:16],
        "messages": skynet_messages,
        "trigger": "submit-message"
    }


def parse_sse_line(line: str) -> Optional[dict]:
    """Parse uma linha SSE do skynetchat."""
    line = line.strip()
    if not line or not line.startswith("data: "):
        return None
    try:
        return json.loads(line[6:])
    except json.JSONDecodeError:
        return None


def extract_cookie_from_request(request: Request) -> str:
    """
    Extrai cookie de 3 fontes possíveis:
    1. Header Authorization: Bearer ***
    2. Header X-Skynet-Cookie: <cookie>
    3. Variável de ambiente SKYNET_COOKIE
    """
    custom = request.headers.get("x-skynet-cookie", "")
    if custom:
        return custom

    auth = request.headers.get("authorization", "")
    if auth.startswith("Bearer ") and not auth.startswith("Bearer sk-"):
        return auth[7:]

    return SKYNET_COOKIE


def _error_chunk(message: str, code: str = "upstream_error") -> str:
    """Helper para gerar chunk de erro OpenAI-compatible."""
    payload = {
        "error": {
            "message": message,
            "type": "proxy_error" if "connect" in message.lower() or "unreach" in message.lower() else "upstream_error",
            "code": code,
        }
    }
    return f"data: {json.dumps(payload)}\n\ndata: [DONE]\n\n"


async def stream_openai_response(skynet_payload: dict, model: str, cookie: str):
    """
    Faz POST para /api/chat-V3 e transforma o SSE stream do skynetchat
    no formato SSE do OpenAI.
    Com tratamento robusto de erros de conexão.
    """
    created = int(time.time())
    chat_id = f"chatcmpl-{uuid.uuid4().hex[:24]}"

    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(120.0)) as client:
            async with client.stream(
                "POST", SKYNET_CHAT,
                json=skynet_payload,
                headers=get_headers(cookie)
            ) as response:

                if response.status_code != 200:
                    error_body = await response.aread()
                    error_detail = error_body.decode("utf-8", errors="replace")[:500]
                    yield _error_chunk(
                        f"SKYNETchat returned {response.status_code}: {error_detail}",
                        str(response.status_code)
                    )
                    return

                # Primeiro chunk (role)
                first_chunk = {
                    "id": chat_id,
                    "object": "chat.completion.chunk",
                    "created": created,
                    "model": model,
                    "choices": [{
                        "index": 0,
                        "delta": {"role": "assistant"},
                        "finish_reason": None
                    }]
                }
                yield f"data: {json.dumps(first_chunk)}\n\n"

                buffer = ""
                async for chunk in response.aiter_text():
                    buffer += chunk
                    while "\n" in buffer:
                        line, buffer = buffer.split("\n", 1)
                        event = parse_sse_line(line)
                        if event is None:
                            continue

                        event_type = event.get("type")
                        if event_type == "text-delta":
                            delta_text = event.get("delta", "")
                            if delta_text:
                                openai_chunk = {
                                    "id": chat_id,
                                    "object": "chat.completion.chunk",
                                    "created": created,
                                    "model": model,
                                    "choices": [{
                                        "index": 0,
                                        "delta": {"content": delta_text},
                                        "finish_reason": None
                                    }]
                                }
                                yield f"data: {json.dumps(openai_chunk)}\n\n"

                        elif event_type == "finish":
                            done_chunk = {
                                "id": chat_id,
                                "object": "chat.completion.chunk",
                                "created": created,
                                "model": model,
                                "choices": [{
                                    "index": 0,
                                    "delta": {},
                                    "finish_reason": "stop"
                                }]
                            }
                            yield f"data: {json.dumps(done_chunk)}\n\n"
                            yield "data: [DONE]\n\n"

    except httpx.RequestError as e:
        # ConnectError, Timeout, etc.
        err_msg = f"Failed to reach {SKYNET_CHAT}: {type(e).__name__} - {e}"
        print(f"[SKYNET-PROXY ERROR] {err_msg}")
        yield _error_chunk(err_msg, "connection_failed")
    except Exception as e:
        err_msg = f"Unexpected proxy error: {type(e).__name__}: {e}"
        print(f"[SKYNET-PROXY ERROR] {err_msg}")
        traceback.print_exc()
        yield _error_chunk(err_msg, "internal_error")


async def collect_full_response(skynet_payload: dict, cookie: str) -> str:
    """Faz POST e coleta resposta completa (não-streaming). Com tratamento de erro."""
    full_text = ""

    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(120.0)) as client:
            async with client.stream(
                "POST", SKYNET_CHAT,
                json=skynet_payload,
                headers=get_headers(cookie)
            ) as response:

                if response.status_code != 200:
                    error_body = await response.aread()
                    raise HTTPException(
                        status_code=response.status_code,
                        detail=f"SKYNETchat error: {error_body.decode('utf-8', errors='replace')[:300]}"
                    )

                buffer = ""
                async for chunk in response.aiter_text():
                    buffer += chunk
                    while "\n" in buffer:
                        line, buffer = buffer.split("\n", 1)
                        event = parse_sse_line(line)
                        if event is None:
                            continue
                        if event.get("type") == "text-delta":
                            full_text += event.get("delta", "")

    except httpx.RequestError as e:
        raise HTTPException(
            status_code=502,
            detail=f"Proxy failed to connect to upstream ({SKYNET_CHAT}): {type(e).__name__} {e}"
        )

    return full_text


# ============================================================
# ENDPOINTS
# ============================================================

@app.get("/health")
async def health():
    has_cookie = bool(SKYNET_COOKIE)
    return {
        "status": "ok",
        "service": "skynet-openai-proxy",
        "version": "2.2.0",
        "upstream": SKYNET_CHAT,
        "cookie_configured": has_cookie,
        "cookie_len": len(SKYNET_COOKIE) if has_cookie else 0,
        "hint": "Set SKYNET_COOKIE env var or pass X-Skynet-Cookie header" if not has_cookie else None
    }


@app.get("/v1/models")
async def list_models():
    return {
        "object": "list",
        "data": [{
            "id": "skynet",
            "object": "model",
            "created": 1700000000,
            "owned_by": "skynetchat.net"
        }]
    }


@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    body = await request.json()

    model = body.get("model", "skynet")
    messages = body.get("messages", [])
    stream = body.get("stream", False)

    if not messages:
        raise HTTPException(status_code=400, detail="messages is required")

    # Extrair cookie (env var, header X-Skynet-Cookie, ou Authorization)
    cookie = extract_cookie_from_request(request)

    if not cookie:
        raise HTTPException(
            status_code=401,
            detail="No cookie configured. Set SKYNET_COOKIE env var, "
                   "pass X-Skynet-Cookie header, or use Authorization: Bearer *** "
                   "Run get_cookies.py to extract your cookie."
        )

    skynet_payload = openai_to_skynet(messages)

    if stream:
        return StreamingResponse(
            stream_openai_response(skynet_payload, model, cookie),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no",
            }
        )
    else:
        full_text = await collect_full_response(skynet_payload, cookie)
        return JSONResponse({
            "id": f"chatcmpl-{uuid.uuid4().hex[:24]}",
            "object": "chat.completion",
            "created": int(time.time()),
            "model": model,
            "choices": [{
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": full_text
                },
                "finish_reason": "stop"
            }],
            "usage": {
                "prompt_tokens": -1,
                "completion_tokens": -1,
                "total_tokens": -1
            }
        })


if __name__ == "__main__":
    import uvicorn
    print("=" * 55)
    print(" SKYNETchat OpenAI Proxy v2.2")
    print("=" * 55)
    print()
    print(" Endpoints:")
    print("   POST /v1/chat/completions")
    print("   GET  /v1/models")
    print("   GET  /health")
    print()
    print(f" Cookie configurado: {'SIM' if SKYNET_COOKIE else 'NAO'} (len={len(SKYNET_COOKIE)})")
    print(f" Upstream target: {SKYNET_CHAT}")
    if not SKYNET_COOKIE:
        print()
        print(" ! AVISO: Sem cookie, as chamadas vao falhar (401).")
        print(" ! Para configurar:")
        print(" !   1. python3 get_cookies.py")
        print(" !   2. export SKYNET_COOKIE=\"...\"")
        print(" ! Ou passe header: X-Skynet-Cookie: ...")
    print()
    print(" Base URL (para OpenAI clients): http://localhost:8080/v1")
    print(" Dica: export SKYNET_BASE=https://... para mudar o upstream")
    print("=" * 55)
    uvicorn.run(app, host="0.0.0.0", port=8080)
