import requests

def brute_force_dirs(target_url):
    print("[~] Starting directory brute-force...")

    wordlist = [
        "admin", "login", "dashboard", "config", "uploads", "includes",
        "server-status", ".git", ".env", "backup", "api", "test", "private"
    ]

    found_dirs = []

    for word in wordlist:
        url = f"{target_url.rstrip('/')}/{word}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"[+] Found: {url} (200 OK)")
                found_dirs.append(url)
            elif response.status_code == 403:
                print(f"[!] Forbidden but exists: {url} (403)")
                found_dirs.append(url + " (403)")
        except requests.RequestException:
            continue

    return found_dirs
