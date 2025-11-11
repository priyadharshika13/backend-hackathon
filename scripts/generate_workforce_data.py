"""
StaffTract.AI – Workforce Optimizer Data Generator (v1)
--------------------------------------------------------
Generates:
  - workforce_data.json  → Company-level Saudization & growth analytics
Linked with:
  - generate_performance_data.py (uses same company list)
"""

import json, os, random
from faker import Faker

# Base output directory
BASE_PATH = os.path.join("backend", "mock_data")
os.makedirs(BASE_PATH, exist_ok=True)

fake = Faker()

def generate_companies(total=500):
    """Generate unique company names for cross-linking with performance data."""
    companies = [fake.company() for _ in range(total)]
    with open(os.path.join(BASE_PATH, "company_list.json"), "w", encoding="utf-8") as f:
        json.dump(companies, f, ensure_ascii=False, indent=2)
    return companies

def generate_workforce_data(companies):
    """Generate company-level Saudization and growth metrics."""
    data = []
    for company in companies:
        total_workers = random.randint(50, 2000)
        saudization = random.randint(15, 95)
        saudi = int(saudization / 100 * total_workers)
        expats = total_workers - saudi
        growth = round(random.uniform(0.5, 6.0), 2)
        category = (
            "Platinum" if saudization > 70 else
            "Green" if saudization > 50 else
            "Yellow" if saudization > 30 else
            "Red"
        )
        region = random.choice([
            "Riyadh", "Jeddah", "Dammam", "Mecca", "Medina",
            "Tabuk", "Abha", "Yanbu", "Al Khobar", "Taif"
        ])
        data.append({
            "company": company,
            "region": region,
            "total_workers": total_workers,
            "saudi_workers": saudi,
            "expat_workers": expats,
            "saudization_%": saudization,
            "category": category,
            "growth": growth
        })
    return data

def main():
    print("Generating workforce optimizer dataset...")
    companies = generate_companies(500)
    workforce_data = generate_workforce_data(companies)
    path = os.path.join(BASE_PATH, "workforce_data.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(workforce_data, f, ensure_ascii=False, indent=2)
    print(f"✅ workforce_data.json created with {len(workforce_data)} records.")
    print("✅ company_list.json created for performance linkage.")

if __name__ == "__main__":
    main()
