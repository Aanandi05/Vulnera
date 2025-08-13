import requests

def check_headers(target_url):
    print("[~] Checking HTTP security headers...")
    try:
        response = requests.get(target_url, timeout=5)
        headers = response.headers

        required_headers = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "X-XSS-Protection",
            "Referrer-Policy",
            "Permissions-Policy"
        ]

        missing = []
        for header in required_headers:
            if header not in headers:
                print(f"[-] Missing header: {header}")
                missing.append(header)
            else:
                print(f"[+] Present header: {header}")

        return {
            "present": {h: headers[h] for h in required_headers if h in headers},
            "missing": missing
        }

    except requests.RequestException as e:
        print(f"[!] Error during header check: {e}")
        return {
            "present": {},
            "missing": required_headers
        }
