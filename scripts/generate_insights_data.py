"""
StaffTract.AI – AI Insights Data Generator (v1)
------------------------------------------------
Generates:
  - insights_data.json → Bilingual AI-style dashboard summaries
Combines trends from workforce, performance, and recruitment data.
"""

import json, os, random

BASE_PATH = os.path.join("backend", "mock_data")
os.makedirs(BASE_PATH, exist_ok=True)

def generate_insights(total=3000):
    english_templates = [
        "AI analysis shows {percent}% improvement in Saudization this quarter.",
        "Employee satisfaction increased by {percent}%.",
        "Performance KPIs improved by {percent}% across all departments.",
        "Fraud alerts reduced by {percent}% since last audit.",
        "Recruitment efficiency improved by {percent}% in {region}.",
        "Regional growth in community workforce reached {percent}% this quarter."
    ]
    arabic_templates = [
        "تحليل الذكاء الاصطناعي يُظهر تحسنًا بنسبة {percent}٪ في السعودة هذا الربع.",
        "زاد رضا الموظفين بنسبة {percent}٪.",
        "تحسنت مؤشرات الأداء بنسبة {percent}٪ في جميع الأقسام.",
        "انخفضت التنبيهات الاحتيالية بنسبة {percent}٪ منذ المراجعة الأخيرة.",
        "تحسنت كفاءة التوظيف بنسبة {percent}٪ في {region}.",
        "وصل نمو القوى العاملة المجتمعية إلى {percent}٪ هذا الربع."
    ]
    regions = ["Riyadh","Jeddah","Dammam","Mecca","Medina","Abha","Tabuk","Yanbu","Taif","Al Khobar"]

    data = []
    for _ in range(total):
        percent = random.randint(3, 25)
        region = random.choice(regions)
        template = random.choice(english_templates + arabic_templates)
        text = template.format(percent=percent, region=region)
        lang = "Arabic" if "٪" in text else "English"
        category = random.choice(["Recruitment","Performance","Community","Workforce","Fraud","General"])
        data.append({
            "language": lang,
            "category": category,
            "text": text,
            "impact_score": round(random.uniform(0.5, 1.0), 2)
        })
    return data

def main():
    print("Generating AI Insights bilingual dataset ...")
    data = generate_insights()
    path = os.path.join(BASE_PATH, "insights_data.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ insights_data.json created with {len(data)} records.")

if __name__ == "__main__":
    main()
