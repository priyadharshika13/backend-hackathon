Write-Host " Launching StaffTract.AI Backend..." -ForegroundColor Cyan
cd backend
python -m uvicorn app.main:app --reload --port 8000
