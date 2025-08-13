import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

def train_model():
    print("[~] Loading dataset...")
    df = pd.read_csv("C:/Users/aanan/PycharmProjects/Vulnera/ai/sample_dataset.csv")


    X = df.drop("risk_label", axis=1)
    y = df["risk_label"]

    print("[~] Training RandomForest model...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    print("[+] Classification Report:")
    print(classification_report(y_test, y_pred))

    model_path = "ai/risk_model.pkl"
    # Ensure directory exists before saving
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(clf, model_path)
    print(f"[+] Model saved to {model_path}")



    # Save model directly inside ai/ folder
    model_path = os.path.join(os.path.dirname(__file__), "risk_model.pkl")
    joblib.dump(clf, model_path)

    # Confirm it's saved
    print(f"[+] Model saved to: {os.path.abspath(model_path)}")
    if os.path.isfile(model_path):
        print("[✓] Confirmed: Model file exists.")
    else:
        print("[✗] ERROR: File not found after saving!")

    # Absolute path debug
    full_path = os.path.abspath(model_path)
    print(f"[+] Model saved to: {full_path}")

    # Confirm if the file really exists
    if os.path.isfile(full_path):
        print("[✓] Confirmed: Model file exists.")
    else:
        print("[✗] ERROR: File not found after saving!")


if __name__ == "__main__":
    train_model()
