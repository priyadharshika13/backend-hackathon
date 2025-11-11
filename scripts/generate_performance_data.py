"""
StaffTract.AI – Performance Evaluation Data Generator (v1)
------------------------------------------------------------
Generates:
  - performance_data.json → Employee-level KPIs & AI feedback
Links each employee to a company from:
  backend/mock_data/company_list.json
"""

import json, os, random
from faker import Faker

BASE_PATH = os.path.join("backend", "mock_data")
os.makedirs(BASE_PATH, exist_ok=True)

fake = Faker()
fake_ar = Faker("ar_SA")

def load_companies():
    """Load shared company names from workforce dataset."""
    path = os.path.join(BASE_PATH, "company_list.json")
    if not os.path.exists(path):
        print("⚠️ company_list.json not found! Run generate_workforce_data.py first.")
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_performance_data(companies, total_employees=10000):
    """Generate realistic employee-level KPI data linked to companies."""
    departments = [
        "IT","HR","Operations","Finance","Design","Construction","Procurement",
        "Marketing","Customer Support","Engineering","Legal","Quality Assurance",
        "R&D","Administration"
    ]

    feedback_en = [
        "Consistent performer with strong attention to detail.",
        "Shows leadership potential; excellent team collaboration.",
        "Improvement needed in time management and goal focus.",
        "Highly adaptable, thrives in cross-functional projects.",
        "Strong technical foundation with innovative mindset."
    ]
    feedback_ar = [
        "موظف متميز يتمتع بدقة عالية في الأداء.",
        "يبدي قدرة قيادية ممتازة ويتعاون بشكل رائع مع الفريق.",
        "يحتاج إلى تحسين في إدارة الوقت والتركيز على الأهداف.",
        "مرن للغاية ويبدع في المشاريع المشتركة بين الأقسام.",
        "يمتلك أساسًا فنيًا قويًا وعقلية مبتكرة."
    ]

    data = []
    for _ in range(total_employees):
        company = random.choice(companies)
        dept = random.choice(departments)
        attendance = random.randint(60, 100)
        productivity = random.randint(50, 100)
        teamwork = random.randint(60, 100)
        learning = random.randint(50, 100)
        overall = round((attendance + productivity + teamwork + learning) / 4, 2)

        data.append({
            "employee_id": f"E{random.randint(10000,99999)}",
            "name": fake.name(),
            "arabic_name": fake_ar.name(),
            "company": company,
            "department": dept,
            "attendance_score": attendance,
            "productivity_score": productivity,
            "teamwork_score": teamwork,
            "learning_score": learning,
            "overall_score": overall,
            "ai_feedback_en": random.choice(feedback_en),
            "ai_feedback_ar": random.choice(feedback_ar),
            "promotion_recommendation": random.choice(["Yes", "No"]),
            "salary_increase_%": random.choice([0, 3, 5, 7, 10]),
            "year": random.choice([2023, 2024, 2025])
        })
    return data

def main():
    print("Generating performance evaluation dataset...")
    companies = load_companies()
    if not companies:
        print("⚠️ No company data found. Run generate_workforce_data.py first.")
        return
    performance_data = generate_performance_data(companies)
    path = os.path.join(BASE_PATH, "performance_data.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(performance_data, f, ensure_ascii=False, indent=2)
    print(f"✅ performance_data.json created with {len(performance_data)} employee records.")
    print("Linked to companies from workforce_data.json")

if __name__ == "__main__":
    main()
