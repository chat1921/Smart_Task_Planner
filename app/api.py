# app/api.py
import os
import json
import google.generativeai as genai
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
from pathlib import Path

# Load Environment
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Configure AI
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# --- Data Models ---
class Task(BaseModel):
    id: int
    title: str
    description: str
    duration: str

class GoalPlan(BaseModel):
    goal: str
    tasks: List[Task]

class GoalRequest(BaseModel):
    goal_text: str
    current_plan_context: Optional[str] = None # New field for modification

# --- The Logic ---
def generate_goal_plan(user_goal: str, context: str = None) -> GoalPlan:
    try:
        # We check if this is a "New Goal" or a "Refinement"
        if context:
            base_prompt = f"""
            You are a Senior Project Manager.
            The user wants to MODIFY an existing plan based on this instruction: "{user_goal}".
            
            Here is the context/original goal: "{context}".
            
            Regenerate the full plan incorporating this change.
            """
        else:
            base_prompt = f"""
            You are a Senior Project Manager.
            Create a highly structured, concise execution plan for: "{user_goal}".
            """

        # Strict Formatting Rules
        final_prompt = base_prompt + """
        
        STRICT RULES:
        1. Generate exactly 5 to 7 high-impact tasks (keep it brief).
        2. Task Titles must be action-oriented (e.g., "Draft Business Plan").
        3. Descriptions must be extremely short (Max 15 words).
        4. Return ONLY valid JSON matching this schema:
        {
            "goal": "Refined Goal Title",
            "tasks": [
                { "id": 1, "title": "string", "description": "string", "duration": "string" }
            ]
        }
        """

        model = genai.GenerativeModel('gemini-2.0-flash', generation_config={"response_mime_type": "application/json"})
        response = model.generate_content(final_prompt)
        return json.loads(response.text)

    except Exception as e:
        print(f"❌ Error: {e}")
        return None