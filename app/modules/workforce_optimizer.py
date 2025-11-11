from fastapi import APIRouter
import json, os

router = APIRouter(prefix="/api/workforce", tags=["Workforce Optimizer"])
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(BASE_DIR, "mock_data", "workforce_data.json")

def load_data():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

@router.get("/overview")
async def get_workforce_overview():
    return load_data()

@router.get("/summary")
async def get_workforce_summary():
    data = load_data()
    if not data:
        return {"message": "No workforce data available"}
    # Calculate summary stats
    total_employees = sum(emp.get("total_workers", 0) for emp in data)
    total_saudi = sum(emp.get("saudi_workers", 0) for emp in data)
    saudization_rate = (total_saudi / total_employees * 100) if total_employees > 0 else 0
    organization_avg_saudization = saudization_rate  # Simplified
    return {
        "total_employees": total_employees,
        "saudization_rate": round(saudization_rate, 2),
        "organization_avg_saudization": round(organization_avg_saudization, 2)
    }
