"""
====================================================================
 StaffTract.AI – Community Data Auto-Repair Script
 Author  : StaffTract.AI Crew
 Purpose : Fix inconsistencies in community_data.json and
           community_region_summary.json to resolve 500 errors.
====================================================================
"""

import json, os, random
from statistics import mean

DATA_PATH = os.path.join("backend", "mock_data", "community_data.json")
SUMMARY_PATH = os.path.join("backend", "mock_data", "community_region_summary.json")

def load_json(path):
    if not os.path.exists(path):
        print(f"⚠️ File not found: {path}")
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ Cleaned and saved: {path} ({len(data)} records)")

def clean_community_data(data):
    """Fix numeric inconsistencies and missing fields."""
    cleaned = []
    for record in data:
        try:
            region = record.get("region", "Unknown")
            total = int(record.get("total_workers", 0))
            saudi = int(record.get("saudi_workers", 0))
            expat = int(record.get("expat_workers", total - saudi))
            if total <= 0:
                continue  # skip invalid
            if saudi > total:
                saudi = int(total * random.uniform(0.3, 0.8))
            expat = total - saudi
            saudization_rate = round((saudi / total) * 100, 2)
            growth_q = record.get("growth_trend_q", [random.uniform(1.0, 5.0) for _ in range(3)])
            growth_q = [round(float(x), 2) for x in growth_q]
            avg_growth = round(mean(growth_q), 2)
            cleaned.append({
                "region": region,
                "industry": record.get("industry", "General"),
                "organization": record.get("organization", "Unknown"),
                "total_workers": total,
                "saudi_workers": saudi,
                "expat_workers": expat,
                "saudization_rate": saudization_rate,
                "growth_trend_q": growth_q,
                "avg_growth_trend": avg_growth
            })
        except Exception:
            continue
    return cleaned

def clean_summary_data(data):
    """Recalculate averages in region summary."""
    for region in data:
        total = region.get("total_workers", 0)
        saudi = region.get("saudi_workers", 0)
        if total > 0:
            region["expat_workers"] = total - saudi
            region["saudization_rate"] = round((saudi / total) * 100, 2)
        else:
            region["saudization_rate"] = 0
        growth_q = region.get("growth_trend_q", [2.0, 3.0, 4.0])
        region["growth_trend_q"] = [round(float(x), 2) for x in growth_q]
        region["avg_growth_trend"] = round(mean(region["growth_trend_q"]), 2)
    return data

if __name__ == "__main__":
    print("🧹 Running StaffTract.AI community data auto-repair...")

    community = load_json(DATA_PATH)
    summary = load_json(SUMMARY_PATH)

    if community:
        fixed_community = clean_community_data(community)
        save_json(DATA_PATH, fixed_community)

    if summary:
        fixed_summary = clean_summary_data(summary)
        save_json(SUMMARY_PATH, fixed_summary)

    print("\n🎯 Repair complete. Try restarting your backend now:")
    print("   python -m uvicorn app.main:app --reload --port 8000")
