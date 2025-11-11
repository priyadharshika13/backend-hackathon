from fastapi import APIRouter
import json, os

router = APIRouter(prefix="/api/performance", tags=["Performance Evaluation"])
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(BASE_DIR, "mock_data", "performance_data.json")

def load_data():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

@router.get("/summary")
async def get_performance_summary():
    return load_data()
