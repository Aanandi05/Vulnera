import argparse
import os
from scanner.port_scanner import scan_ports
from scanner.header_checker import check_headers
from scanner.method_tester import test_http_methods
from scanner.ssl_checker import check_ssl_cert
from scanner.dir_bruteforce import brute_force_dirs
from reports.report_generator import generate_report
from ai.model_predictor import predict_risk


def main():
    parser = argparse.ArgumentParser(description="Vulnera - AI-Powered Web Vulnerability Scanner")
    parser.add_argument("--url", help="Target website URL (e.g., https://example.com)")
    parser.add_argument("--report", choices=["pdf"], default="pdf", help="Output report format")  # Always PDF
    args = parser.parse_args()

    # Ask interactively if URL not provided
    if not args.url:
        args.url = input("Enter target website URL: ").strip()

    target_url = args.url

    # Basic scans
    ports = scan_ports(target_url)
    headers = check_headers(target_url)
    methods = test_http_methods(target_url)
    ssl_info = check_ssl_cert(target_url)
    exposed_dirs = brute_force_dirs(target_url)

    # Collate all results
    scan_result = {
        "url": target_url,
        "open_ports": ports,
        "http_headers": headers,
        "http_methods": methods,
        "ssl_info": ssl_info,
        "exposed_directories": exposed_dirs,
    }

    # Predict risk using AI model
    risk = predict_risk(scan_result)
    scan_result["ai_risk_prediction"] = risk

    # Report output
    report_path = generate_report(scan_result, format=args.report)

    print(f"\n[+] PDF Report generated: {os.path.abspath(report_path)}")


if __name__ == "__main__":
    main()
