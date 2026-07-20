#!/usr/bin/env python3
"""
Extrator de cookies do skynetchat.net
======================================
Abre o Chrome (com seu perfil), captura os cookies HttpOnly
e salva em arquivo para usar com o proxy.

USO:
  python3 get_cookies.py

Salva o cookie em:
  - /Users/cleitonmouraloura/TEIA/skynet-proxy/.skynet_cookie
  - Imprime o comando export para você copiar/colar
"""

import subprocess
import sys
import os
from pathlib import Path

COOKIE_FILE = Path(__file__).parent / ".skynet_cookie"


def get_cookies_from_safari():
    """Tenta extrair cookies do Safari via javascript."""
    try:
        script = '''
        tell application "Safari"
            if (count of windows) = 0 then
                make new document
            end if
            set URL of document 1 to "https://skynetchat.net"
            delay 3
            do JavaScript "document.cookie" in document 1
        end tell
        '''
        result = subprocess.run(
            ["osascript", "-e", script],
            capture_output=True, text=True, timeout=15
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"  Erro Safari: {e}")
        return None


def get_cookies_from_chrome_applescript():
    """Tenta extrair cookies do Chrome via AppleScript (cookies não-HttpOnly)."""
    try:
        script = '''
        tell application "Google Chrome"
            if (count of windows) = 0 then
                make new window
                set URL of active tab of window 1 to "https://skynetchat.net"
                delay 4
            end if
            set found to false
            repeat with w in windows
                repeat with t in tabs of w
                    if URL of t contains "skynetchat" then
                        set found to true
                        exit repeat
                    end if
                end repeat
            end repeat
            if not found then
                tell window 1
                    set URL of active tab to "https://skynetchat.net"
                    delay 4
                end tell
            end if
            execute active tab of window 1 javascript "document.cookie"
        end tell
        '''
        result = subprocess.run(
            ["osascript", "-e", script],
            capture_output=True, text=True, timeout=15
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"  Erro Chrome: {e}")
        return None


def get_cookies_from_chrome_db():
    """
    Extrai cookies HttpOnly diretamente do banco de dados do Chrome.
    Requer Chrome fechado (ou faz cópia).
    """
    import sqlite3
    import shutil
    import tempfile

    cookie_db_paths = [
        Path.home() / "Library/Application Support/Google/Chrome/Default/Cookies",
        Path.home() / "Library/Application Support/Google/Chrome/Profile 1/Cookies",
        Path.home() / "Library/Application Support/Google/Chrome/Profile 2/Cookies",
    ]

    for db_path in cookie_db_paths:
        if not db_path.exists():
            continue

        # Copia o DB (Chrome pode ter lock)
        with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
            tmp_path = tmp.name

        try:
            shutil.copy2(str(db_path), tmp_path)
        except Exception:
            continue

        try:
            conn = sqlite3.connect(tmp_path)
            cursor = conn.cursor()
            cursor.execute("""
                SELECT host_key, name, value, encrypted_value
                FROM cookies
                WHERE host_key LIKE '%skynetchat%'
            """)

            cookies = []
            for row in cursor.fetchall():
                host, name, value, encrypted = row
                if value:
                    cookies.append(f"{name}={value}")
                # Se encrypted, precisaríamos descriptografar com keychain (complexo)

            conn.close()
            os.unlink(tmp_path)

            if cookies:
                return "; ".join(cookies)

        except Exception as e:
            print(f"  Erro lendo DB do Chrome: {e}")
            try:
                os.unlink(tmp_path)
            except:
                pass

    return None


def get_cookies_manual():
    """Instruções manuais como fallback."""
    print("\n" + "=" * 55)
    print(" EXTRAÇÃO MANUAL DE COOKIES")
    print("=" * 55)
    print()
    print("1. Abra https://skynetchat.net no Chrome/Safari")
    print("2. Faça login normalmente")
    print("3. Abra DevTools (F12)")
    print("4. Vá em Application > Storage > Cookies")
    print("5. Selecione https://skynetchat.net")
    print("6. Copie TODOS os cookies no formato:")
    print("   nome1=valor1; nome2=valor2; ...")
    print()
    print("7. Cole aqui:")
    cookie = input("   > ").strip()
    return cookie if cookie else None


def main():
    print("=" * 55)
    print(" Extrator de Cookies - skynetchat.net")
    print("=" * 55)
    print()

    # Tentar métodos em ordem
    methods = [
        ("Chrome (AppleScript)", get_cookies_from_chrome_applescript),
        ("Chrome (Database)", get_cookies_from_chrome_db),
        ("Safari (AppleScript)", get_cookies_from_safari),
    ]

    for name, method in methods:
        print(f"Tentando: {name}...")
        result = method()
        if result and len(result) > 10:
            print(f"  SUCESSO! Cookie obtido ({len(result)} chars)")
            # Salvar
            COOKIE_FILE.write_text(result)
            print(f"\nCookie salvo em: {COOKIE_FILE}")
            print(f"\nPara usar com o proxy:")
            print(f'  export SKYNET_COOKIE="{result}"')
            print(f"  python3 server.py")
            return result
        else:
            print(f"  Sem sucesso.")

    # Fallback manual
    print("\nTodos os métodos automáticos falharam.")
    result = get_cookies_manual()
    if result:
        COOKIE_FILE.write_text(result)
        print(f"\nCookie salvo em: {COOKIE_FILE}")
        print(f'export SKYNET_COOKIE="{result}"')
        return result

    print("\nFalha ao obter cookies.")
    return None


if __name__ == "__main__":
    main()
