#!/usr/bin/env python3
"""
Capturador automático para skynetchat.net
Uso: python capture_skynet.py

Instale antes:
    pip install playwright
    playwright install chromium
"""
import asyncio
import json
from datetime import datetime
from pathlib import Path
from playwright.async_api import async_playwright

LOG_FILE = Path("skynet_captures.log")

async def main():
    LOG_FILE.touch(exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,   # Mude para True quando quiser rodar escondido
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        )
        page = await context.new_page()

        print("[*] Iniciando captura em https://skynetchat.net")
        print("[*] Faça uma conversa normal na página que abrir.")
        print("[*] Tudo que for capturado vai aparecer aqui e também em skynet_captures.log\n")

        # 1. Captura de respostas de rede (fetch / api calls)
        async def on_response(response):
            url = response.url
            method = response.request.method
            status = response.status

            interesting = any(k in url.lower() for k in [
                "api", "chat", "message", "stream", "conversation", "generate", "completion"
            ])

            if interesting or "skynetchat" in url:
                line = f"\n[NET {datetime.now().strftime('%H:%M:%S')}] {status} {method} {url}"
                print(line)
                LOG_FILE.write_text(LOG_FILE.read_text() + line + "\n", encoding="utf-8")

                try:
                    content_type = response.headers.get("content-type", "")
                    if "json" in content_type or "text" in content_type:
                        body = await response.text()
                        if body and len(body) > 5:
                            preview = body[:800].replace("\n", " ")
                            print(f"     └─ Body: {preview}")
                            LOG_FILE.write_text(
                                LOG_FILE.read_text() + f"     Body: {preview}\n",
                                encoding="utf-8"
                            )
                except Exception as e:
                    pass

        page.on("response", on_response)

        # 2. Captura de WebSocket (se o site usar)
        def on_ws(ws):
            msg = f"\n[WS  {datetime.now().strftime('%H:%M:%S')}] {ws.url}"
            print(msg)
            LOG_FILE.write_text(LOG_FILE.read_text() + msg + "\n", encoding="utf-8")

            ws.on("framereceived", lambda frame: (
                print(f"     [WS-IN]  {str(frame)[:300]}") if frame else None
            ))
            ws.on("framesent", lambda frame: (
                print(f"     [WS-OUT] {str(frame)[:300]}") if frame else None
            ))

        page.on("websocket", on_ws)

        # 3. Observa mudanças no DOM (texto que aparece na tela)
        await page.add_init_script("""
            (() => {
                const observer = new MutationObserver((mutations) => {
                    for (const mutation of mutations) {
                        for (const node of mutation.addedNodes) {
                            if (node.nodeType === 1) {
                                const text = (node.innerText || node.textContent || '').trim();
                                if (text.length > 8 && text.length < 4000) {
                                    // Evita capturar coisas muito genéricas
                                    if (!/^(loading|enviar|enviando|pensando|...)$/i.test(text)) {
                                        const ts = new Date().toLocaleTimeString();
                                        console.log(`[DOM ${ts}] ${text}`);
                                    }
                                }
                            }
                        }
                    }
                });
                if (document.body) {
                    observer.observe(document.body, { childList: true, subtree: true });
                }
            })();
        """)

        # 4. Também escuta console.log do navegador
        page.on("console", lambda msg: (
            print(f"[CONSOLE] {msg.text}") if "DOM" in msg.text or "SKYNET" in msg.text.upper() else None
        ))

        await page.goto("https://skynetchat.net", wait_until="networkidle")

        print("\n" + "="*60)
        print("PÁGINA ABERTA. Faça sua conversa agora.")
        print("Pressione ENTER no terminal quando quiser parar a captura.")
        print("="*60 + "\n")

        # Mantém aberto até o usuário apertar enter
        await asyncio.get_event_loop().run_in_executor(None, input)

        await browser.close()
        print(f"\n[*] Captura finalizada. Logs salvos em: {LOG_FILE.absolute()}")

if __name__ == "__main__":
    asyncio.run(main())
