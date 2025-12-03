Copy this entire block and replace the text in your README.md file.
Markdown

# 🚀 Smart_Task_Planner- Advanced Goal Architect

![Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)
![Stack](https://img.shields.io/badge/FastAPI-Tailwind-blue?style=flat-square)
![AI](https://img.shields.io/badge/Powered%20By-Gemini%202.0-orange?style=flat-square)

**NexPlan AI** is an intelligent task orchestration system that transforms vague user goals into structured, timeline-based execution plans. Unlike simple to-do lists, NexPlan uses **LLM Reasoning (Google Gemini 2.0)** to understand context, estimate duration, and logically sequence dependencies.

---

## ✨ Advanced Features

| Feature | Description |
| :--- | :--- |
| 🧠 **Context-Aware AI** | Utilizes **Google Gemini 2.0 Flash** for logical task breakdown and timeline estimation. |
| 🔄 **Conversational Refinement** | **Interactive Mode:** Users can "chat" with the plan to tweak timelines or add missing steps (e.g., *"Make it shorter"*, *"Add budget steps"*). |
| 💾 **Persistent Memory** | **SQLite Database** integration automatically archives projects, allowing instant retrieval of past strategies. |
| 🎨 **Glassmorphism UI** | A premium, dark-mode aesthetic built with Tailwind CSS, featuring staggered animations and responsive design. |
| ⚡ **Real-time Feedback** | Low-latency generation with visual loading states and error handling. |

---

## 🛠️ Technical Stack

* **Backend:** Python (FastAPI), Pydantic (Data Validation)
* **Frontend:** Vanilla JS (ES6+), Tailwind CSS (via CDN), FontAwesome
* **Database:** SQLite (Embedded, Zero-config)
* **AI Engine:** Google Generative AI (Gemini 2.0 Flash)

---

## 🚀 Installation & Setup Guide

Follow these steps to run the project locally.

### 1. Clone the Repository
Open your terminal and run:
```bash
git clone [https://github.com/chat1921/Smart_Task_Planner.git](https://github.com/chat1921/Smart_Task_Planner.git)
cd Smart_Task_Planner

 2. Set up Virtual Environment

It is recommended to use a virtual environment to keep dependencies clean.

    Windows:
    Bash

python -m venv venv
venv\Scripts\activate

Mac / Linux:
Bash:

    python3 -m venv venv
    source venv/bin/activate

3. Install Dependencies
Bash:

pip install -r requirements.txt

4. Configure Environment Variables

    Create a file named .env in the root folder.

    Open it and add your Google Gemini API Key (Get it from Google AI Studio):
    Code snippet

    GEMINI_API_KEY=your_actual_api_key_here

5. Run the Application

Start the backend server:
Bash:

uvicorn app.main:app --reload

6. Access the App

Open your browser and visit: http://127.0.0.1:8000


📂 Project Structure

Smart_Task_Planner/
├── app/
│   ├── main.py          # FastAPI Server & Routes
│   ├── api.py           # AI Logic (Gemini Integration)
│   ├── database.py      # SQLite Database Manager
│   └── templates/
│       └── index.html   # Advanced Dashboard UI
├── requirements.txt     # Python Dependencies
├── .env                 # API Keys (Excluded from Git)
└── README.md            # Documentation

