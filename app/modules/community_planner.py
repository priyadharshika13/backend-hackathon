from fastapi import APIRouter
import json, os

router = APIRouter(prefix="/api/community", tags=["Community Planner"])
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(BASE_DIR, "mock_data", "community_data.json")

@router.get("/summary")
async def get_community_summary():
    """Return community planning data."""
    if not os.path.exists(DATA_PATH):
        return {"error": "Community data not found"}
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

@router.get("/overview")
async def get_community_overview():
    """Return community overview data."""
    if not os.path.exists(DATA_PATH):
        return {"error": "Community data not found"}
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
