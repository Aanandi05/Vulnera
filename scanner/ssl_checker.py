import ssl
import socket
from urllib.parse import urlparse
from datetime import datetime

def check_ssl_cert(target_url):
    print("[~] Checking SSL certificate...")
    parsed = urlparse(target_url)
    host = parsed.hostname
    port = 443  # default HTTPS port

    context = ssl.create_default_context()
    ssl_info = {}

    try:
        with socket.create_connection((host, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()

                ssl_info["issuer"] = dict(x[0] for x in cert["issuer"])
                ssl_info["subject"] = dict(x[0] for x in cert["subject"])
                ssl_info["valid_from"] = cert["notBefore"]
                ssl_info["valid_until"] = cert["notAfter"]

                # Check expiry
                expire_date = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")
                days_left = (expire_date - datetime.utcnow()).days
                ssl_info["days_until_expiry"] = days_left

                print(f"[+] SSL Certificate is valid, expires in {days_left} days.")

    except Exception as e:
        print(f"[!] SSL certificate check failed: {e}")
        ssl_info["error"] = str(e)

    return ssl_info
