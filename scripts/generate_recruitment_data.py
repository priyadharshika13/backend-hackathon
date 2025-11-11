"""
StaffTract.AI – Recruitment Data Generator
------------------------------------------
Generates 10 000 realistic bilingual candidate profiles
across 500 job roles for hackathon or demo use.

Output:
    backend/mock_data/recruitment_data.json
"""

import json, os, random
from faker import Faker

# -------------------------------------------------------------------
fake_en = Faker("en")
fake_ar = Faker("ar_SA")

OUTPUT_PATH = os.path.join("backend", "mock_data", "recruitment_data.json")

# -------------------------------------------------------------------
# 500 diverse roles drawn from Vision 2030 domains
roles = [
    # IT & Digital
    "Software Engineer","AI Specialist","Data Scientist","Cybersecurity Analyst","DevOps Engineer",
    "Cloud Architect","Full-Stack Developer","Mobile App Developer","UI/UX Designer","Game Developer",
    # Engineering & Manufacturing
    "Civil Engineer","Mechanical Engineer","Electrical Engineer","HVAC Technician","Auto Mechanic",
    "Industrial Engineer","Project Manager","Safety Officer","Quality Inspector","Fabrication Technician",
    # Healthcare & Science
    "Doctor","Nurse","Pharmacist","Surgeon","Biomedical Scientist","Lab Technician","Research Scientist",
    "Environmental Scientist","Chemist","Biochemist","Radiologist","Dentist","Veterinarian",
    # Education & Academia
    "Teacher","Professor","Curriculum Designer","Education Technologist","Training Coordinator",
    # Business & Finance
    "Accountant","Auditor","Financial Analyst","Procurement Officer","HR Specialist","Operations Manager",
    "Business Consultant","Bank Officer","Economist","Compliance Officer",
    # Agriculture & Environment
    "Agronomist","Farm Technician","Hydroponic Operator","Food Scientist","Sustainability Consultant",
    # Creative & Design
    "Architect","Interior Designer","Graphic Designer","Fashion Technologist","Animator","Photographer",
    "Video Editor","Product Designer","Industrial Designer",
    # Construction & Logistics
    "Site Supervisor","Quantity Surveyor","Construction Foreman","Truck Driver","Logistics Coordinator",
    # Energy & Oil
    "Petroleum Engineer","Renewable Energy Specialist","Solar Technician","Geologist","Energy Analyst",
    # Tourism & Hospitality
    "Hotel Manager","Chef","Tour Guide","Travel Consultant","Front Desk Officer",
    # Admin & Services
    "Office Administrator","Receptionist","Customer Service Rep","Secretary","Payroll Officer",
    # Security, Law, Public Services
    "Legal Advisor","Security Analyst","Public Relations Officer","Government Relations Specialist",
    # (Fill to ~500 by repeating category variants)
]

# Expand to ~500 unique titles
while len(roles) < 500:
    roles.append(random.choice(roles) + f" {random.randint(1,9)}")

# -------------------------------------------------------------------
def generate_candidate(idx: int):
    """Return a realistic bilingual candidate record."""
    name_en = fake_en.name()
    name_ar = fake_ar.name()
    position = random.choice(roles)
    exp = random.randint(0, 25)
    skills = random.sample([
        "Python","Java","React","Machine Learning","AutoCAD","Finance","Leadership",
        "Communication","Negotiation","Electrical Systems","Data Analysis","Teamwork",
        "Project Planning","Customer Service","Creativity","Problem Solving","Research",
        "Sustainability","Teaching","Healthcare"
    ], k=3)

    # weighted AI scoring
    tech = random.randint(55, 100)
    comm = random.randint(55, 100)
    attitude = random.randint(55, 100)
    teamwork = random.randint(55, 100)
    overall = round((0.3*tech)+(0.25*comm)+(0.25*attitude)+(0.2*teamwork), 2)

    # decision rules
    if overall >= 80:
        decision = "Shortlisted"
    elif overall >= 65:
        decision = "Waitlisted"
    else:
        decision = "Rejected"

    # bilingual feedback
    fb_en_templates = [
        "Strong technical foundation with good collaboration.",
        "Excellent communicator and fast learner.",
        "Reliable professional with adaptive mindset.",
        "Shows leadership and teamwork in complex environments.",
        "Analytical thinker with growth potential."
    ]
    fb_ar_templates = [
        "أساس تقني قوي وقدرة جيدة على التعاون.",
        "متواصل ممتاز وسريع التعلم.",
        "محترف موثوق يتمتع بعقلية مرنة.",
        "يُظهر قيادة وروح عمل جماعي في بيئات معقدة.",
        "مفكر تحليلي يتمتع بإمكانيات عالية للنمو."
    ]
    i = random.randint(0, 4)

    return {
        "id": idx,
        "name": name_en,
        "arabic_name": name_ar,
        "position": position,
        "experience_years": exp,
        "skills": skills,
        "technical_score": tech,
        "communication_score": comm,
        "attitude_score": attitude,
        "teamwork_score": teamwork,
        "ai_overall_score": overall,
        "ai_feedback_en": fb_en_templates[i],
        "ai_feedback_ar": fb_ar_templates[i],
        "decision": decision,
        "fraud_flag": random.random() < 0.02
    }

# -------------------------------------------------------------------
def main(total=10000):
    Faker.seed(2025)
    print(f"Generating {total} recruitment records ...")
    data = [generate_candidate(i+1) for i in range(total)]
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f" Created: {OUTPUT_PATH}  ({total} records)")

# -------------------------------------------------------------------
if __name__ == "__main__":
    main()
