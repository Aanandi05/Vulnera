import json
import os
from datetime import datetime

def generate_report(data, format="json"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_name = f"vulnera_report_{timestamp}.{format}"
    report_path = os.path.join("reports", report_name)

    if format == "json":
        try:
            with open(report_path, "w") as f:
                json.dump(data, f, indent=4)
            print(f"[+] JSON report saved as: {report_path}")
        except Exception as e:
            print(f"[!] Error writing JSON report: {e}")

    elif format == "html":
        try:
            html_content = "<html><body><h2>Vulnera Scan Report</h2><pre>{}</pre></body></html>".format(
                json.dumps(data, indent=4).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            )
            with open(report_path, "w") as f:
                f.write(html_content)
            print(f"[+] HTML report saved as: {report_path}")
        except Exception as e:
            print(f"[!] Error writing HTML report: {e}")
