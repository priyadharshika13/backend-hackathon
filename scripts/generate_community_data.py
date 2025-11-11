"""
======================================================================
 StaffTract.AI – Community Workforce Data Generator (v3)
 Author  : StaffTract.AI Crew
 Purpose : Creates a large-scale mock dataset for workforce analytics.
           Generates 10,000 records across 13 Saudi regions and compiles
           a regional summary with quarterly growth trend averages.
 Outputs :
   - backend/mock_data/community_data.json
   - backend/mock_data/community_region_summary.json
======================================================================
"""

import json
import os
import random
from collections import defaultdict
from faker import Faker

# -------------------------------------------------------------------
# Initialize Faker for generating realistic organization names
# -------------------------------------------------------------------
fake = Faker()

# -------------------------------------------------------------------
# Regions & industries used for diversity across the dataset
# -------------------------------------------------------------------
REGIONS = [
    "Riyadh", "Makkah", "Eastern Province", "Madinah", "Qassim",
    "Asir", "Tabuk", "Hail", "Jazan", "Najran",
    "Al-Bahah", "Northern Borders", "Al-Jouf"
]

INDUSTRIES = [
    "Construction", "Healthcare", "Education", "Hospitality",
    "Finance", "IT & Software", "Retail", "Logistics",
    "Manufacturing", "Energy", "Agriculture", "Tourism", "Government"
]

# -------------------------------------------------------------------
# Output file locations
# -------------------------------------------------------------------
OUTPUT_MAIN = os.path.join("backend", "mock_data", "community_data.json")
OUTPUT_SUMMARY = os.path.join("backend", "mock_data", "community_region_summary.json")
os.makedirs(os.path.dirname(OUTPUT_MAIN), exist_ok=True)

# -------------------------------------------------------------------
# Generate 10,000 organization-level data points
# -------------------------------------------------------------------
def generate_dataset(total_records: int = 10000):
    """
    Generate a detailed community workforce dataset.
    Each record represents one organization within a Saudi region.
    """
    data = []
    for _ in range(total_records):
        region = random.choice(REGIONS)
        industry = random.choice(INDUSTRIES)
        organization = fake.company()

        # Basic workforce composition
        total_workers = random.randint(500, 10000)
        saudi_workers = int(total_workers * random.uniform(0.3, 0.75))
        expat_workers = total_workers - saudi_workers
        saudization_rate = round((saudi_workers / total_workers) * 100, 2)

        # Quarterly growth trend (Q1–Q3)
        growth_trend_q = [round(random.uniform(1.0, 5.0), 2) for _ in range(3)]
        avg_growth_trend = round(sum(growth_trend_q) / 3, 2)

        data.append({
            "region": region,
            "industry": industry,
            "organization": organization,
            "total_workers": total_workers,
            "saudi_workers": saudi_workers,
            "expat_workers": expat_workers,
            "saudization_rate": saudization_rate,
            "growth_trend_q": growth_trend_q,
            "avg_growth_trend": avg_growth_trend
        })

    return data

# -------------------------------------------------------------------
# Aggregate data by region to create a concise overview file
# -------------------------------------------------------------------
def generate_region_summary(dataset):
    """
    Summarize the dataset by region, calculating total counts
    and average quarterly growth trends.
    """
    aggregates = defaultdict(lambda: {
        "total_workers": 0,
        "saudi_workers": 0,
        "expat_workers": 0,
        "growth_q_sum": [0, 0, 0],
        "count": 0
    })

    for entry in dataset:
        region = entry["region"]
        aggregates[region]["total_workers"] += entry["total_workers"]
        aggregates[region]["saudi_workers"] += entry["saudi_workers"]
        aggregates[region]["expat_workers"] += entry["expat_workers"]
        for i in range(3):
            aggregates[region]["growth_q_sum"][i] += entry["growth_trend_q"][i]
        aggregates[region]["count"] += 1

    summary = []
    for region, values in aggregates.items():
        count = values["count"]
        q_avg = [round(q / count, 2) for q in values["growth_q_sum"]]
        total = values["total_workers"]
        saudi = values["saudi_workers"]
        expat = values["expat_workers"]
        rate = round((saudi / total) * 100, 2)

        summary.append({
            "region": region,
            "total_workers": total,
            "saudi_workers": saudi,
            "expat_workers": expat,
            "saudization_rate": rate,
            "growth_trend_q": q_avg,
            "avg_growth_trend": round(sum(q_avg) / 3, 2)
        })

    return summary

# -------------------------------------------------------------------
# Entry point
# -------------------------------------------------------------------
if __name__ == "__main__":
    print("Generating 10,000-record community dataset with quarterly trends...")
    dataset = generate_dataset()
    summary = generate_region_summary(dataset)

    with open(OUTPUT_MAIN, "w", encoding="utf-8") as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)

    with open(OUTPUT_SUMMARY, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(f" Main dataset saved → {OUTPUT_MAIN}")
    print(f" Regional summary saved → {OUTPUT_SUMMARY}")
    print(f" Total Records: {len(dataset)}")
    print(f" Regions Summarized: {len(summary)}")
