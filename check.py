import os, re, sys, requests

# pune aici linkul de la cautarea "iphone 17" de pe bsgmag
URL = "https://bsgmag.ro/catalog/q/Apple%20IPhone%2017"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
html = requests.get(URL, headers=headers, timeout=30).text

if re.search(r"Telefon\s+Apple\s+iPhone\s+17(?!\s*(Pro|Plus|Air|e\b))", html, re.IGNORECASE):
    msg = f"iPhone 17 a apărut pe bsgmag: {URL}"
    print(msg)
    hook = os.getenv("DISCORD_WEBHOOK")
    if hook:
        requests.post(hook, json={"content": msg}, timeout=30)
    sys.exit(1)
else:
    print("Nu există încă.")
