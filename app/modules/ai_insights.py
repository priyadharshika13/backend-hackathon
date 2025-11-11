from fastapi import APIRouter
import json, os, random, statistics

router = APIRouter(prefix="/api/insights", tags=["AI Insight Generator"])
BASE_PATH = os.path.join("backend", "mock_data")

# ------------------------------------------------------------
def load_json(file_name):
    """Helper to safely load a JSON file."""
    path = os.path.join(BASE_PATH, file_name)
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# ------------------------------------------------------------
@router.get("/generate")
async def generate_insight():
    """Generate bilingual AI insights based on available data sources."""
    recruitment = load_json("recruitment_data.json")
    workforce = load_json("workforce_data.json")
    performance = load_json("performance_data.json")
    community = load_json("community_data.json")
    insights_pool = load_json("insights_data.json")

    # --- RECRUITMENT TRENDS ---
    total_candidates = len(recruitment)
    shortlisted = sum(1 for c in recruitment if c.get("result") == "Shortlisted")
    rejection_rate = round(((total_candidates - shortlisted) / total_candidates) * 100, 2) if total_candidates else 0
    top_roles = [c.get("role_applied", "General") for c in recruitment]
    common_role = max(set(top_roles), key=top_roles.count) if top_roles else "General"

    # --- WORKFORCE TRENDS ---
    saudization_rates = [r.get("saudization_rate", r.get("saudization_%", 0)) for r in workforce if r]
    avg_saudization = round(statistics.mean(saudization_rates), 2) if saudization_rates else 0

    # --- PERFORMANCE ANALYTICS ---
    perf_scores = [p.get("overall_score", 0) for p in performance if p.get("overall_score") is not None]
    avg_perf = round(statistics.mean(perf_scores), 2) if perf_scores else 0
    high_perf = sum(1 for p in performance if p.get("overall_score", 0) > 85)

    # --- COMMUNITY INSIGHTS ---
    regions = [c.get("region") for c in community if c.get("region")]
    top_region = max(set(regions), key=regions.count) if regions else "Riyadh"

    # --- AI-STYLE ENGLISH INSIGHTS ---
    insight_en = random.choice([
        f"Across {len(regions)} regions, average Saudization stands at {avg_saudization}%. {top_region} leads in localization efforts.",
        f"Average employee performance is {avg_perf}%, with {high_perf} high-performing employees identified this quarter.",
        f"Hiring focus shifted toward {common_role}, while overall rejection rate remains {rejection_rate}%.",
        f"Saudization and performance metrics indicate steady workforce growth of {random.randint(3,7)}% quarter-over-quarter."
    ])

    # --- AI-STYLE ARABIC INSIGHTS ---
    insight_ar = random.choice([
        f"في {len(regions)} منطقة، يبلغ متوسط التوطين {avg_saudization}٪، وتتصدّر منطقة {top_region} جهود التوطين.",
        f"متوسط أداء الموظفين هو {avg_perf}٪، مع {high_perf} موظفًا عالي الأداء تم تحديدهم هذا الربع.",
        f"تركز التوظيف مؤخرًا على وظيفة {common_role}، بينما تبلغ نسبة الرفض الإجمالية {rejection_rate}٪.",
        f"تشير مؤشرات التوطين والأداء إلى نمو مستقر في القوى العاملة بنسبة {random.randint(3,7)}٪ مقارنة بالربع السابق."
    ])

    # --- OPTIONAL INSIGHT POOL MERGE (insights_data.json) ---
    if insights_pool:
        extra_en = [i["text"] for i in insights_pool if i.get("language", "").lower().startswith("eng")]
        extra_ar = [i["text"] for i in insights_pool if i.get("language", "").lower().startswith("arab")]
        if extra_en and random.random() > 0.5:
            insight_en = random.choice(extra_en)
        if extra_ar and random.random() > 0.5:
            insight_ar = random.choice(extra_ar)

    return {
        "summary": {
            "total_candidates": total_candidates,
            "shortlisted": shortlisted,
            "rejection_rate_%": rejection_rate,
            "average_saudization_%": avg_saudization,
            "average_performance_%": avg_perf,
            "top_region": top_region
        },
        "insight_en": insight_en,
        "insight_ar": insight_ar
    }

# ------------------------------------------------------------
@router.get("/random")
async def random_motivational():
    """Return a random bilingual motivational message for dashboards."""
    messages_en = [
        "Great progress! Keep building a smarter, more inclusive workforce.",
        "AI metrics show upward growth — consistency is the new excellence.",
        "Localization and innovation go hand-in-hand toward Vision 2030."
    ]
    messages_ar = [
        "تقدّم رائع! استمر في بناء قوة عاملة أذكى وأكثر شمولًا.",
        "تُظهر مؤشرات الذكاء الاصطناعي نموًا إيجابيًا — الاستمرارية هي التميز الجديد.",
        "التوطين والابتكار يسيران جنبًا إلى جنب نحو رؤية 2030."
    ]

    return {
        "message_en": random.choice(messages_en),
        "message_ar": random.choice(messages_ar)
    }
