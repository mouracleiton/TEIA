# Formas de Capturar Texto do Chat Automaticamente - skynetchat.net

## Resumo Rápido (Recomendação)

**Melhor caminho atual:**  
**Playwright + interceptação de rede + observação do DOM**

Por quê?
- O site é SvelteKit (SPA)
- Usa Cloudflare Turnstile
- Provavelmente usa `fetch` + streaming (vimos "stream" no bundle)
- Playwright consegue lidar com tudo isso de forma relativamente estável

---

## Ranking de Métodos (Praticidade × Robustez)

| Posição | Método                        | Dificuldade | Robustez | Velocidade | Recomendado para |
|---------|-------------------------------|-------------|----------|------------|------------------|
| 1       | Playwright (network + DOM)    | Média       | Alta     | Boa        | Produção / API   |
| 2       | Tampermonkey / Userscript     | Baixa       | Média    | Excelente  | Prototipagem     |
| 3       | mitmproxy (proxy)             | Alta        | Muito Alta | Boa      | Engenharia reversa profunda |
| 4       | CDP direto (pychrome etc)     | Média-Alta  | Alta     | Boa        | Avançado         |
| 5       | Browser Extension             | Média       | Alta     | Boa        | Uso diário       |
| 6       | Reverse dos chunks JS         | Baixa       | Baixa    | Rápida     | Descoberta inicial |
| 7       | Selenium                      | Média       | Média    | Lenta      | Evitar           |
| 8       | OCR + Screenshot              | Alta        | Baixa    | Lenta      | Último recurso   |

---

## 1. Playwright (Método Recomendado)

### Vantagens
- Intercepta todas as requisições (fetch + WebSocket)
- Pode ler o DOM em tempo real
- Consegue lidar com Turnstile (com algumas técnicas)
- Fácil de transformar em API depois

### Como começar

```bash
# Instalar
pip install playwright
playwright install chromium
```

### Script básico para capturar tudo

```python
# capture_skynet.py
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # headless=True depois
        context = await browser.new_context()
        page = await context.new_page()

        # === CAPTURA DE REDE ===
        async def log_response(response):
            url = response.url
            if any(x in url.lower() for x in ['api', 'chat', 'message', 'stream', 'conversation']):
                print(f"[NET] {response.status} {response.request.method} {url}")
                try:
                    body = await response.text()
                    if len(body) > 10:
                        print(f"       Body: {body[:500]}...")
                except:
                    pass

        page.on("response", log_response)

        # === CAPTURA DE WEBSOCKET (se existir) ===
        page.on("websocket", lambda ws: print(f"[WS] {ws.url}"))

        # === OBSERVAR DOM (MutationObserver) ===
        await page.add_init_script("""
            const observer = new MutationObserver(mutations => {
                for (const m of mutations) {
                    for (const node of m.addedNodes) {
                        if (node.nodeType === 1) {
                            const text = node.innerText || node.textContent || '';
                            if (text.length > 5 && text.length < 2000) {
                                console.log('[DOM]', text.trim().slice(0, 300));
                            }
                        }
                    }
                }
            });
            observer.observe(document.body, { childList: true, subtree: true });
        """)

        await page.goto("https://skynetchat.net")
        
        print("\n>>> Abra a página, faça uma conversa e observe o terminal.\n")
        print(">>> Pressione ENTER aqui quando quiser fechar...")
        input()
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
```

Execute:
```bash
python capture_skynet.py
```

### O que observar
- Quais URLs são chamadas quando você envia uma mensagem
- Se aparece `stream` ou `text/event-stream`
- Onde o texto da resposta aparece no DOM (classes, ids)

---

## 2. Tampermonkey (Mais Fácil para Começar)

1. Instale a extensão Tampermonkey no Chrome
2. Crie um novo script com:

```javascript
// ==UserScript==
// @name         Skynet Chat Capture
// @match        https://skynetchat.net/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    const observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
            mutation.addedNodes.forEach((node) => {
                if (node.nodeType === 1) {
                    const text = (node.innerText || '').trim();
                    if (text.length > 10 && text.length < 3000) {
                        console.log('%c[SKYNET CAPTURE]', 'color: lime', text);
                        // Aqui você pode fazer fetch para sua API local
                    }
                }
            });
        });
    });

    observer.observe(document.body, { childList: true, subtree: true });

    console.log('%c[SKYNET] Capturador de chat ativado', 'color: cyan');
})();
```

Abra o console do navegador para ver o texto saindo.

---

## 3. mitmproxy (Mais Poderoso)

```bash
pip install mitmproxy
mitmproxy -s capture_skynet.py   # ou use o modo interativo
```

Você intercepta **tudo** (HTTP + WebSocket) em tempo real.  
É excelente para descobrir o protocolo real.

Desvantagem: precisa instalar certificado SSL no sistema.

---

## 4. Descoberta Rápida Manual (Faça Agora)

Antes de programar:

1. Abra https://skynetchat.net
2. Pressione **F12** → aba **Network**
3. Marque "Preserve log"
4. Faça uma conversa completa
5. Filtre por:
   - `fetch`
   - `api`
   - `chat`
   - `stream`
   - `message`

Me manda print ou lista das requisições que aparecem (principalmente as que retornam texto longo).

Isso já vai revelar:
- Se é polling
- Se é streaming (SSE)
- Se é WebSocket
- O endpoint exato

---

## 5. Reverse Engineering dos Chunks (Já fizemos um pouco)

O site tem vários arquivos:
- `https://skynetchat.net/_app/immutable/chunks/DxXxoVL-.js` (tem "stream", "message", "fetch")

Você pode baixar todos os chunks e procurar por:
- URLs de API
- Formato do body das mensagens
- Como o streaming é feito

---

## Próximos Passos Recomendados

1. **Agora**: Faça a captura manual com DevTools (Network) e me envie os resultados.
2. Instale Playwright e rode o script acima.
3. Com os endpoints descobertos, criamos o wrapper OpenAI-compatible.

Quer que eu gere agora:
- A. Script Playwright mais avançado (com salvamento em arquivo + streaming detection)
- B. Um userscript mais completo
- C. Um script de mitmproxy

Me fala qual você quer implementar primeiro.
