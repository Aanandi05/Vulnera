import socket
from urllib.parse import urlparse

def scan_ports(target_url):
    parsed = urlparse(target_url)
    host = parsed.hostname
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]
    open_ports = []

    print("[~] Scanning common ports...")

    for port in common_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"[+] Port {port} is open")
                open_ports.append(port)
            sock.close()
        except socket.gaierror:
            print("[-] Hostname could not be resolved.")
            break
        except socket.error:
            print("[-] Couldn't connect to server.")
            break

    return open_ports

