from fastapi import APIRouter
import json, os, random
from datetime import datetime, timedelta

router = APIRouter(prefix="/api/fraud", tags=["Fraud & Integrity Monitor"])

DATA_PATH = os.path.join("backend", "mock_data", "fraud_events.json")

def load_data():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# -------------------------------------------------------------------

@router.get("/alerts")
async def get_fraud_alerts():
    """Return top 50 recent fraud events with severity levels."""
    data = load_data()
    if not data:
        return {"error": "No fraud events found"}

    # Sort by timestamp (newest first)
    data_sorted = sorted(data, key=lambda x: x.get("timestamp", ""), reverse=True)[:50]

    total = len(data)
    high = sum(1 for e in data if e["severity"] == "High")
    med = sum(1 for e in data if e["severity"] == "Medium")
    low = sum(1 for e in data if e["severity"] == "Low")

    insight_en = (
        f"{total} events analyzed — {high} high-risk cases detected. "
        f"Most common issue: {random.choice(['Tab Switch', 'Mic Muted', 'Inactivity'])}."
    )
    insight_ar = (
        f"تم تحليل {total} حدثًا — تم اكتشاف {high} حالة عالية الخطورة. "
        f"أكثر المشكلات شيوعًا: {random.choice(['تبديل التبويب', 'إيقاف الميكروفون', 'الخمول'])}"
    )

    return {
        "total_events": total,
        "high_risk": high,
        "medium_risk": med,
        "low_risk": low,
        "recent_alerts": data_sorted,
        "insight_en": insight_en,
        "insight_ar": insight_ar
    }

# -------------------------------------------------------------------

@router.get("/candidate/{candidate_name}")
async def get_candidate_events(candidate_name: str):
    """Return all integrity events for a specific candidate."""
    data = load_data()
    candidate_events = [e for e in data if candidate_name.lower() in e["candidate"].lower()]
    if not candidate_events:
        return {"candidate": candidate_name, "events": [], "message": "No events logged."}
    return {
        "candidate": candidate_name,
        "total_events": len(candidate_events),
        "events": candidate_events
    }

# -------------------------------------------------------------------

@router.post("/event")
async def log_event(candidate: str, event_type: str, severity: str = "Low"):
    """Log a new simulated fraud event (demo purpose)."""
    event = {
        "event_id": f"FM-{random.randint(1000,9999)}",
        "candidate": candidate,
        "event_type": event_type,
        "severity": severity,
        "timestamp": datetime.utcnow().isoformat()
    }

    # Append to mock_data file
    data = load_data()
    data.append(event)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return {"message": "Event logged successfully", "event": event}
