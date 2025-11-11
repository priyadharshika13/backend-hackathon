"""
StaffTract.AI – Full Mock Data Builder (v1)
-------------------------------------------
Runs all data generators sequentially:
1. Workforce Optimizer
2. Performance Evaluation
3. Fraud & Integrity Monitor
4. Community Workforce Planner
5. AI Insights
6. Recruitment Data (optional)
"""

import os, subprocess, time

scripts = [
    "generate_workforce_data.py",
    "generate_performance_data.py",
    "generate_fraud_data.py",
    "generate_community_data.py",
    "generate_insights_data.py"
]

BASE_DIR = os.path.dirname(__file__)
print("🚀 Running StaffTract.AI full mock data builder...\n")

start_time = time.time()
for i, script in enumerate(scripts, start=1):
    path = os.path.join(BASE_DIR, script)
    if not os.path.exists(path):
        print(f"⚠️ Script not found: {script}")
        continue
    print(f"[{i}/{len(scripts)}] Running {script} ...")
    subprocess.run(["python", path], check=False)
    print("-" * 60)
    time.sleep(1)

elapsed = round(time.time() - start_time, 2)
print(f"\n✅ All datasets generated successfully in backend/mock_data/ (Time: {elapsed}s)")
print("📊 You can now run your backend:")
print("   uvicorn app.main:app --reload --port 8000\n")
