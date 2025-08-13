import requests

def test_http_methods(target_url):
    print("[~] Testing allowed HTTP methods...")
    methods_to_test = ["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "TRACE", "PATCH"]
    allowed_methods = []

    try:
        for method in methods_to_test:
            response = requests.request(method, target_url, timeout=5)
            # Status code < 400 usually means the method is accepted or processed
            if response.status_code < 400:
                print(f"[+] Method allowed: {method} (Status: {response.status_code})")
                allowed_methods.append(method)
            else:
                print(f"[-] Method not allowed: {method} (Status: {response.status_code})")
    except requests.RequestException as e:
        print(f"[!] Error testing HTTP methods: {e}")

    return allowed_methods
