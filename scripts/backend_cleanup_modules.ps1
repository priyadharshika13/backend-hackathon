# =====================================================================
#  StaffTract.AI – MVP Version (Roshn 2025 Edition)
#  Backend Cleanup + Module Initialization Script
#  Author: StaffTract Crew (Geetha K S, Dr. Abdullah Alshamer, Dr. Saravanan Pandiaraj)
# =====================================================================

echo "------------------------------------------------------"
echo "Starting Backend Cleanup and Module Setup for Hackathon"
echo "------------------------------------------------------"

# --- STEP 1 : Clean existing clutter ---
cd "D:\Geetha\Hackathon_Roshn_2025"

# Remove old, unused files
Remove-Item *.sql, *.db, *.exe, *.bat, *.html, TODO.md -Force -ErrorAction SilentlyContinue
Remove-Item auto_commit_push_* -Force -ErrorAction SilentlyContinue
Remove-Item db_health_* -Force -ErrorAction SilentlyContinue
Remove-Item env.backend -Force -ErrorAction SilentlyContinue
Get-ChildItem -Recurse -Include __pycache__, .pytest_cache, .mypy_cache | Remove-Item -Recurse -Force

echo "Cleanup complete – keeping only essential backend structure."

# --- STEP 2 : Ensure folders exist ---
$backendPath = "backend\app\modules"
if (!(Test-Path $backendPath)) {
    New-Item -ItemType Directory -Force -Path $backendPath | Out-Null
}
if (!(Test-Path "backend\mock_data")) {
    New-Item -ItemType Directory -Force -Path "backend\mock_data" | Out-Null
}

# --- STEP 3 : Create 6 backend modules ---
echo "Creating 6 backend modules..."

# 1. Recruitment Copilot
$content1 = @"
from fastapi import APIRouter
import json, os

router = APIRouter(prefix=`"/api/recruitment`", tags=[`"Recruitment Copilot`"])

@router.get(`"/sample_candidates`")
async def get_candidates():
    path = os.path.join(`"backend`", `"mock_data`", `"recruitment_data.json`")
    with open(path, `"r`", encoding=`"utf-8`") as f:
        data = json.load(f)
    return {`"module`": `"Recruitment Copilot`", `"data`": data[:5]}

@router.get(`"/ai_score`")
async def ai_score():
    return {`"candidate`": `"Fatimah A.`", `"ai_score`": 88, `"result`": `"Shortlisted`"}
"@
$content1 | Out-File "$backendPath\recruitment_copilot.py" -Encoding utf8

# 2. Workforce Optimization
$content2 = @"
from fastapi import APIRouter
import json, os

router = APIRouter(prefix=`"/api/workforce`", tags=[`"Workforce Optimization`"])

@router.get(`"/summary`")
async def workforce_summary():
    path = os.path.join(`"backend`", `"mock_data`", `"workforce_data.json`")
    with open(path, `"r`", encoding=`"utf-8`") as f:
        data = json.load(f)
    return {`"saudization_summary`": data[:3]}

@router.get(`"/predict`")
async def predict_nitaqat():
    return {`"company`": `"Roshn Projects`", `"saudization_rate`": 64, `"category`": `"Green`"}
"@
$content2 | Out-File "$backendPath\workforce_optimization.py" -Encoding utf8

# 3. Fraud & Integrity Monitor
$content3 = @"
from fastapi import APIRouter
import json, os

router = APIRouter(prefix=`"/api/fraud`", tags=[`"Fraud Monitor`"])

@router.post(`"/event`")
async def log_event():
    return {`"status`": `"Fraud event logged`", `"event_id`": `"FM-1023`"}

@router.get(`"/alerts`")
async def get_alerts():
    path = os.path.join(`"backend`", `"mock_data`", `"fraud_events.json`")
    with open(path, `"r`", encoding=`"utf-8`") as f:
        data = json.load(f)
    return {`"alerts`": data[:3]}
"@
$content3 | Out-File "$backendPath\fraud_monitor.py" -Encoding utf8

# 4. Community Workforce Planner
$content4 = @"
from fastapi import APIRouter
import json, os

router = APIRouter(prefix=`"/api/community`", tags=[`"Community Planner`"])

@router.get(`"/overview`")
async def overview():
    path = os.path.join(`"backend`", `"mock_data`", `"community_data.json`")
    with open(path, `"r`", encoding=`"utf-8`") as f:
        data = json.load(f)
    return {`"overview`": data}

@router.get(`"/region/{region_name}`")
async def region_detail(region_name: str):
    return {`"region`": region_name, `"saudi_workers`": 240, `"expat_workers`": 80, `"growth`": `"8%`"}
"@
$content4 | Out-File "$backendPath\community_planner.py" -Encoding utf8

# 5. AI Insight Generator
$content5 = @"
from fastapi import APIRouter
import random

router = APIRouter(prefix=`"/api/insights`", tags=[`"AI Insights`"])

insights = [
    {`'language`': `'English`', `'text`': `'AI analysis shows a 12% growth in Saudi hires this quarter.`'},
    {`'language`': `'Arabic`', `'text`': `'تحليل القوى العاملة يظهر زيادة بنسبة 12٪ في التوظيف الوطني.`'}
]

@router.get(`"/generate`")
async def generate_insight():
    return random.choice(insights)
"@
$content5 | Out-File "$backendPath\ai_insights.py" -Encoding utf8

# 6. Performance Evaluation
$content6 = @"
from fastapi import APIRouter
import json, os

router = APIRouter(prefix=`"/api/performance`", tags=[`"Performance Evaluation`"])

@router.get(`"/summary`")
async def summary():
    path = os.path.join(`"backend`", `"mock_data`", `"performance_data.json`")
    with open(path, `"r`", encoding=`"utf-8`") as f:
        data = json.load(f)
    return {`"performance_overview`": data[:3]}

@router.get(`"/employee/{id}`")
async def employee_score(id: str):
    return {`"employee_id`": id, `"score`": 89, `"remarks`": `"Consistent performer`"}
"@
$content6 | Out-File "$backendPath\performance_eval.py" -Encoding utf8

echo "Backend module creation complete."

# --- STEP 4 : Confirm file creation ---
Get-ChildItem "$backendPath" | Select Name, LastWriteTime

echo ""
echo "------------------------------------------------------"
echo "Backend is clean and ready for hackathon development."
echo "Run 'uvicorn app.main:app --reload' to test all routes."
echo "------------------------------------------------------"
