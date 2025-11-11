import os

expected_modules = {
    "ai_insights.py",
    "community_planner.py",
    "fraud_monitor.py",
    "performance_eval.py",
    "recruitment_copilot.py",
    "workforce_optimizer.py"
}

modules_dir = os.path.join("backend", "app", "modules")
existing = set(os.listdir(modules_dir))

print("\n🔍 MVP Structure Verification\n")

missing = expected_modules - existing
extra = existing - expected_modules

if not missing and not extra:
    print("✅ All 6 core hackathon modules are present and clean.")
else:
    if missing:
        print(f"❌ Missing: {', '.join(missing)}")
    if extra:
        print(f"⚠️ Extra: {', '.join(extra)}")

print("\nStructure check complete.\n")
