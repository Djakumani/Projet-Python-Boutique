import os
import socket
import subprocess
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright


BASE_DIR = Path(__file__).resolve().parent.parent
SCREENSHOTS_DIR = BASE_DIR / "docs" / "screenshots"
HOST = "127.0.0.1"
PORT = 8000


def wait_for_server(host: str, port: int, timeout: float = 20.0) -> None:
    deadline = time.time() + timeout
    while time.time() < deadline:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            if sock.connect_ex((host, port)) == 0:
                return
        time.sleep(0.5)
    raise RuntimeError("Le serveur Django n'a pas demarre a temps.")


def main() -> None:
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

    env = os.environ.copy()
    env.setdefault("PYTHONIOENCODING", "utf-8")

    server = subprocess.Popen(
        [sys.executable, "manage.py", "runserver", f"{HOST}:{PORT}", "--noreload"],
        cwd=BASE_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        env=env,
    )

    try:
        wait_for_server(HOST, PORT)
        base_url = f"http://{HOST}:{PORT}"

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1440, "height": 1200})

            page.goto(f"{base_url}/login/", wait_until="networkidle")
            page.screenshot(path=str(SCREENSHOTS_DIR / "01-login-page.png"), full_page=True)

            page.fill('input[name="username"]', "client1")
            page.fill('input[name="password"]', "client123")
            page.click('button[type="submit"]')
            page.wait_for_load_state("networkidle")
            page.goto(f"{base_url}/collection/", wait_until="networkidle")
            page.screenshot(path=str(SCREENSHOTS_DIR / "02-catalogue-client.png"), full_page=True)

            stock_text = page.locator(".product-card-stock").first.inner_text()
            page.locator("a.btn.btn-primary").first.click()
            page.wait_for_load_state("networkidle")
            page.screenshot(path=str(SCREENSHOTS_DIR / "03-achat-page.png"), full_page=True)

            page.fill('input[name="quantite"]', "1")
            page.click('button[type="submit"]')
            page.wait_for_load_state("networkidle")
            page.screenshot(path=str(SCREENSHOTS_DIR / "04-stock-apres-achat.png"), full_page=True)

            page.goto(f"{base_url}/login/", wait_until="networkidle")
            page.fill('input[name="username"]', "admin")
            page.fill('input[name="password"]', "admin123")
            page.click('button[type="submit"]')
            page.wait_for_load_state("networkidle")
            page.goto(f"{base_url}/gestion/", wait_until="networkidle")
            page.screenshot(path=str(SCREENSHOTS_DIR / "05-gestion-admin.png"), full_page=True)

            with open(SCREENSHOTS_DIR / "notes.txt", "w", encoding="utf-8") as fh:
                fh.write("Stock visible avant achat (premiere carte): " + stock_text + "\n")
                fh.write("Captures generees automatiquement depuis le serveur local.\n")

            browser.close()
    finally:
        server.terminate()
        try:
            server.wait(timeout=10)
        except subprocess.TimeoutExpired:
            server.kill()


if __name__ == "__main__":
    main()
