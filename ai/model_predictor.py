import joblib
import numpy as np

def extract_features(scan_result):
    # Extract binary features for AI prediction
    open_ports = scan_result.get("open_ports", [])
    headers_missing = scan_result.get("http_headers", {}).get("missing", [])
    methods = scan_result.get("http_methods", [])

    features = {
        "open_port_21": int(21 in open_ports),
        "open_port_22": int(22 in open_ports),
        "open_port_80": int(80 in open_ports),
        "missing_csp": int("Content-Security-Policy" in headers_missing),
        "missing_hsts": int("Strict-Transport-Security" in headers_missing),
        "missing_xfo": int("X-Frame-Options" in headers_missing),
        "put_allowed": int("PUT" in methods),
        "trace_allowed": int("TRACE" in methods),
    }

    return np.array([list(features.values())]), features  # model_input, feature_names

def predict_risk(scan_result, model_path="ai/risk_model.pkl"):
    try:
        model = joblib.load(model_path)
        model_input, features_used = extract_features(scan_result)
        prediction = model.predict(model_input)[0]
        probability = max(model.predict_proba(model_input)[0])

        print(f"[+] Risk Prediction: {prediction} ({round(probability * 100, 2)}% confidence)")
        return {
            "risk_level": prediction,
            "confidence": round(probability, 2),
            "features_used": features_used
        }

    except Exception as e:
        print(f"[!] Prediction failed: {e}")
        return {
            "risk_level": "UNKNOWN",
            "confidence": 0.0,
            "features_used": {}
        }
