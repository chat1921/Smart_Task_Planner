import sqlite3
import json
from datetime import datetime

DB_NAME = "plans.db"

def init_db():
    """Creates the database table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            goal TEXT NOT NULL,
            tasks_json TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_plan_to_db(goal: str, tasks: list):
    """Saves a new goal and its tasks to the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # We convert the list of tasks to a JSON string to store it easily
    tasks_str = json.dumps(tasks)
    cursor.execute('INSERT INTO plans (goal, tasks_json) VALUES (?, ?)', (goal, tasks_str))
    conn.commit()
    conn.close()

def get_all_plans():
    """Fetches all saved plans from the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT id, goal, created_at FROM plans ORDER BY created_at DESC')
    rows = cursor.fetchall()
    conn.close()
    
    # Convert to a nice list of dictionaries
    plans = [{"id": row[0], "goal": row[1], "date": row[2]} for row in rows]
    return plans

def get_plan_by_id(plan_id: int):
    """Fetches a specific plan's details."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT goal, tasks_json FROM plans WHERE id = ?', (plan_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return {"goal": row[0], "tasks": json.loads(row[1])}
    return None