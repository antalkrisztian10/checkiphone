import os, re, sys, requests

URL = "https://bsgmag.ro/catalog/q/Apple%20IPhone%2017"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
html = requests.get(URL, headers=headers, timeout=30).text

# TEST: prinde iPhone 17 Pro Max, care exista sigur in pagina
if re.search(r"Telefon\s+Apple\s+iPhone\s+17\s+Pro\s+Max", html, re.IGNORECASE):
    msg = f"iPhone 17 a apărut pe bsgmag: {URL}"
    print(msg)
    hook = os.getenv("DISCORD_WEBHOOK")
    print("Webhook setat:", bool(hook))
    if hook:
        r = requests.post(hook, json={"content": msg}, timeout=30)
        print("Discord:", r.status_code, r.text)
    sys.exit(1)
else:
    print("Nu există încă.")
