# SKYNETchat OpenAI-Compatible API Proxy

Proxy que transforma a API interna do [skynetchat.net](https://skynetchat.net) em uma API compatível com OpenAI.

## Instalação

```bash
cd /Users/cleitonmouraloura/TEIA/skynet-proxy
pip3 install fastapi "uvicorn[standard]" httpx
```

## Configuração do Cookie

O skynetchat.net usa cookies HttpOnly para autenticação. Você precisa extrair seus cookies:

### Opção 1: Extração automática

```bash
python3 get_cookies.py
```

### Opção 2: Extração manual

1. Abra https://skynetchat.net e faça login
2. F12 → Application → Storage → Cookies → https://skynetchat.net
3. Copie todos os cookies no formato `nome=valor; nome2=valor2`

Depois:
```bash
export SKYNET_COOKIE="seus_cookies_aqui"
```

## Uso

### Iniciar o servidor

```bash
python3 server.py
# Servidor roda em http://localhost:8080
```

### Exemplo: chamada simples

```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "skynet",
    "messages": [{"role": "user", "content": "Ola, tudo bem?"}]
  }'
```

### Exemplo: streaming

```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "skynet",
    "messages": [{"role": "user", "content": "Explique o SUS em 3 linhas"}],
    "stream": true
  }'
```

### Usar com qualquer client OpenAI (Python)

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8080/v1",
    api_key="skynet-proxy"
)

response = client.chat.completions.create(
    model="skynet",
    messages=[{"role": "user", "content": "Ola!"}]
)
print(response.choices[0].message.content)
```

### Usar com LibreChat, ChatBox, etc

- **API Base URL:** `http://localhost:8080/v1`
- **API Key:** qualquer valor (ou o cookie)
- **Model:** `skynet`

## Como funciona

```
Client OpenAI ──→ Proxy (:8080) ──→ skynetchat.net/api/chat-V3
  /v1/chat/                          (com cookie HttpOnly)
  completions                        SSE: text-delta, step-delta, finish
                                     ↓
                  ←── Transforma SSE para formato OpenAI ←──
```

### Formato interno do skynetchat

**Request (POST /api/chat-V3):**
```json
{
  "id": "abc123",
  "messages": [
    {
      "id": "user-123",
      "role": "user",
      "parts": [{"type": "text", "text": "Olá!"}]
    }
  ],
  "trigger": "submit-message"
}
```

**Response (text/event-stream):**
```
data: {"type":"start","messageId":"..."}
data: {"type":"thinking-meta","summaryTitle":"..."}
data: {"type":"step-start","stepId":"...","stepType":"thinking"}
data: {"type":"step-delta","stepId":"...","delta":"pensando..."}
data: {"type":"step-end","stepId":"..."}
data: {"type":"thinking-complete","totalSteps":1}
data: {"type":"text-start","id":"..."}
data: {"type":"text-delta","id":"...","delta":"texto da resposta"}
data: {"type":"text-end","id":"..."}
data: {"type":"follow-ups","questions":["..."]}
data: {"type":"finish"}
```

O proxy extrai apenas os eventos `text-delta` (resposta real) e ignora o resto.

## Endpoints disponíveis

| Endpoint | Método | Descrição |
|----------|--------|-----------|
| `/v1/chat/completions` | POST | Chat completions (OpenAI format) |
| `/v1/models` | GET | Lista de modelos |
| `/health` | GET | Status do proxy |

## Alternativa de cookie via header

Em vez de usar variável de ambiente, você pode passar o cookie em cada request:

```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "X-Skynet-Cookie: cookie_name=cookie_value" \
  -d '{"model":"skynet","messages":[{"role":"user","content":"Ola!"}]}'
```

Ou como Bearer token:

```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Authorization: Bearer cookie_name=cookie_value" \
  -H "Content-Type: application/json" \
  -d '{"model":"skynet","messages":[{"role":"user","content":"Ola!"}]}'
```

## Arquivos

- `server.py` — Servidor proxy (FastAPI)
- `get_cookies.py` — Extrator de cookies automático
- `README.md` — Esta documentação
