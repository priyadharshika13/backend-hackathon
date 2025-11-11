# -------------------------------------------------------------
# StaffTract.AI – Build & Launch Script
# -------------------------------------------------------------
# Generates all mock datasets, then launches FastAPI backend
# -------------------------------------------------------------

Write-Host "`n  Running Full Mock Data Generator..." -ForegroundColor Cyan
python backend/scripts/run_all_mockdata.py

Write-Host "`n  Launching StaffTract.AI Backend..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "uvicorn backend.app.main:app --reload --port 8000"

Write-Host "`n All Systems Ready. Backend running on http://127.0.0.1:8000" -ForegroundColor Green
