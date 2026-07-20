// ==UserScript==
// @name         SkynetChat Auto Capture (para engenharia reversa)
// @namespace    http://tampermonkey.net
// @version      0.2
// @description  Captura automaticamente mensagens do chat skynetchat.net
// @author       Hermes
// @match        https://skynetchat.net/*
// @grant        GM_xmlhttpRequest
// @grant        unsafeWindow
// @connect      localhost
// ==/UserScript==

(function() {
    'use strict';

    const TARGET_API = 'http://localhost:8765/capture'; // mude se quiser

    function log(msg, data) {
        const ts = new Date().toLocaleTimeString();
        console.log(`%c[SKYNET ${ts}] ${msg}`, 'color:#0f0', data || '');
    }

    // 1. Intercepta fetch nativo
    const origFetch = window.fetch;
    window.fetch = async function(...args) {
        const [url, options] = args;
        const method = (options && options.method) || 'GET';

        if (typeof url === 'string' && (url.includes('api') || url.includes('chat') || url.includes('message') || url.includes('stream'))) {
            log(`FETCH ${method} ${url}`, options && options.body ? JSON.parse(options.body) : null);
        }

        const res = await origFetch.apply(this, args);

        if (typeof url === 'string' && (url.includes('api') || url.includes('chat') || url.includes('stream'))) {
            try {
                const clone = res.clone();
                const text = await clone.text();
                if (text.length > 10) {
                    log(`RESPONSE ${url}`, text.substring(0, 600));
                }
            } catch(e) {}
        }
        return res;
    };

    // 2. Intercepta WebSocket (se o site usar)
    const OrigWS = window.WebSocket;
    window.WebSocket = function(url, protocols) {
        log('WEBSOCKET CONNECT', url);
        const ws = new OrigWS(url, protocols);

        const origSend = ws.send;
        ws.send = function(data) {
            log('WS SEND', data);
            return origSend.apply(this, arguments);
        };

        ws.addEventListener('message', (ev) => {
            log('WS MESSAGE', ev.data);
        });

        return ws;
    };

    // 3. MutationObserver no DOM (captura o que aparece na tela)
    const observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
            mutation.addedNodes.forEach((node) => {
                if (node.nodeType === 1) {
                    const text = (node.innerText || node.textContent || '').trim();
                    if (text.length > 15 && text.length < 5000) {
                        // filtra ruído
                        if (!/^(enviar|loading|pensando|digite sua mensagem|...)$/i.test(text)) {
                            log('DOM TEXT', text);
                            // Envia para sua API local (descomente se quiser)
                            // GM_xmlhttpRequest({
                            //     method: "POST",
                            //     url: TARGET_API,
                            //     data: JSON.stringify({text, ts: Date.now()}),
                            //     headers: {"Content-Type": "application/json"}
                            // });
                        }
                    }
                }
            });
        });
    });

    if (document.body) {
        observer.observe(document.body, { childList: true, subtree: true });
    }

    log('Capturador ativado. Abra o console do navegador (F12).');

})();
