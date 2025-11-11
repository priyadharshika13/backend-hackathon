"""
StaffTract.AI – Fraud & Integrity Monitor Data Generator (v1)
--------------------------------------------------------------
Generates:
  - fraud_events.json → Simulated online test / interview integrity logs
"""

import json, os, random
from faker import Faker
from datetime import datetime, timedelta

BASE_PATH = os.path.join("backend", "mock_data")
os.makedirs(BASE_PATH, exist_ok=True)

fake = Faker()

def generate_fraud_data(total=6000):
    """Generate realistic fraud/integrity monitoring events."""
    event_types = [
        "Tab Switch Detected",
        "Mic Muted During Interview",
        "Inactivity Timeout",
        "Multiple Voices Detected",
        "Unauthorized App Opened",
        "Camera Blocked",
        "Screen Share Disabled",
        "High Background Noise"
    ]
    severities = ["Low", "Medium", "High"]
    data = []
    for _ in range(total):
        candidate = fake.name()
        event_type = random.choice(event_types)
        timestamp = datetime.now() - timedelta(minutes=random.randint(1, 600))
        data.append({
            "event_id": f"FM-{random.randint(1000,9999)}",
            "candidate": candidate,
            "event_type": event_type,
            "severity": random.choice(severities),
            "timestamp": timestamp.isoformat(),
            "notes": random.choice([
                "User switched tabs multiple times.",
                "Microphone muted for over 2 minutes.",
                "Detected potential background voice.",
                "Browser minimized unexpectedly.",
                "High noise level detected near candidate."
            ])
        })
    return data

def main():
    print("Generating fraud & integrity monitor data ...")
    data = generate_fraud_data()
    path = os.path.join(BASE_PATH, "fraud_events.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ fraud_events.json created with {len(data)} records.")

if __name__ == "__main__":
    main()
