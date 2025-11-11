from fastapi import APIRouter, UploadFile, File
import json, os

router = APIRouter(prefix="/api/recruitment", tags=["Recruitment AI Copilot"])
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(_file_)))
DATA_PATH = os.path.join(BASE_DIR, "mock_data", "recruitment_summary.json")

def load_data():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

@router.get("/summary")
async def get_recruitment_summary():
    return load_data()

@router.get("/candidates")
async def get_candidates():
    path = os.path.join(BASE_DIR, "mock_data", "candidates.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# --- NEW ENDPOINT FOR AI RESUME ANALYSIS ---
@router.post("/analyze_resume")
async def analyze_resume(file: UploadFile = File(...)):
    """
    Analyzes an uploaded resume file and returns a mock AI match score and feedback.
    """
    # In a real application, you would:
    # 1. Save the file temporarily or stream its content.
    # 2. Call an external AI/NLP service (e.g., Google Gemini, Azure, AWS).
    # 3. Process the results.

    # Mock Analysis Logic
    filename = file.filename or "uploaded_resume.pdf"
    
    # Simulate an AI score based on the filename (or real logic here)
    if "data scientist" in filename.lower():
        match_score = 92
    elif "manager" in filename.lower():
        match_score = 78
    else:
        match_score = 65 # Default score

    # Mock Feedback (English and Arabic)
    feedback_en = f"Excellent match for the role! Focus on quantifying achievements for a perfect score."
    feedback_ar = f"تطابق ممتاز للدور! ركز على تحديد الإنجازات كمياً للحصول على درجة كاملة."

    return {
        "filename": filename,
        "match_score": match_score,
        "feedback_en": feedback_en,
        "feedback_ar": feedback_ar
    }
# ---------------------------------------------
