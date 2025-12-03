# app/main.py
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional, List, Any
from contextlib import asynccontextmanager

from app.api import generate_goal_plan
from app.database import init_db, save_plan_to_db, get_all_plans, get_plan_by_id

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="AI Goal Planner", lifespan=lifespan)
templates = Jinja2Templates(directory="app/templates")

# Updated Request Model
class GoalRequest(BaseModel):
    goal_text: str
    current_plan_context: Optional[str] = None 

# --- Routes ---
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/generate")
async def generate_plan_api(request: GoalRequest):
    # Pass both the goal (or instruction) and the context (if modifying)
    plan = generate_goal_plan(request.goal_text, request.current_plan_context)
    
    if not plan:
        raise HTTPException(status_code=500, detail="AI generation failed")
    
    # Save only if it's a fresh plan (optional decision, but keeps DB clean)
    if not request.current_plan_context:
        save_plan_to_db(plan['goal'], plan['tasks'])
    
    return plan

@app.get("/api/history")
async def get_history():
    return get_all_plans()

@app.get("/api/history/{plan_id}")
async def get_archived_plan(plan_id: int):
    return get_plan_by_id(plan_id)