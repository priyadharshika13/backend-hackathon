from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.modules import (
    recruitment_copilot,
    workforce_optimizer,
    performance_eval,
    community_planner,
    fraud_monitor,
    ai_insights,
)

app = FastAPI(title="StaffTract.AI Backend", version="1.0")

# Allow CORS for frontend (Vercel + Codespaces + localhost)
origins = [
    "http://localhost:5173",
    "https://stafftract-ai.vercel.app",
    "https://roshn-hackathon-stafftract-crew-okb19guz-geetha-k-ss-projects.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers registration (ensures /api/* consistency)
app.include_router(recruitment_copilot.router)
app.include_router(workforce_optimizer.router)
app.include_router(performance_eval.router)
app.include_router(community_planner.router)
app.include_router(fraud_monitor.router)
app.include_router(ai_insights.router)

@app.get("/")
async def root():
    return {"message": "Welcome to StaffTract.AI Backend"}

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "service": "backend", "version": "1.0"}
