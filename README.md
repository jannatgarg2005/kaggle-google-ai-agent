# PlacementCoach Pro
**AI Career Coach Agent for Engineering Placement Preparation**

[![Live App](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://kaggle-app-ai-agent-uxi2imzmcnxc7r88bj7q4n.streamlit.app/)
[![Kaggle Notebook](https://img.shields.io/badge/Kaggle-Notebook-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/jannatgarg)
[![Gemini API](https://img.shields.io/badge/Gemini_2.0-Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://aistudio.google.com)
[![Track](https://img.shields.io/badge/Track-Agents_for_Good-2ea44f?style=for-the-badge)](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](https://opensource.org/licenses/MIT)

**Competition:** AI Agents: Intensive Vibe Coding Capstone Project — Kaggle x Google 2026  
**Author:** Jannat Garg | B.Tech CSE, BPIT New Delhi  
**GitHub:** [github.com/jannatgarg2005](https://github.com/jannatgarg2005) | **LinkedIn:** [jannat-garg-1699a3366](https://www.linkedin.com/in/jannat-garg-1699a3366)

---

## The Problem

Every year, **1.5 million+ engineering graduates** in India compete for a fraction of AI/ML roles.

Most students face this:
- Do not know which companies match their profile
- Do not know what to study or in what order
- Cannot afford Rs.50,000+ career counselling sessions
- Get generic advice that ignores their specific background
- Have no personalized mock interview practice

**I am one of these students.** I built the tool I needed.

---

## The Solution: PlacementCoach Pro

An intelligent **multi-tool AI agent** that acts as a personal career coach — available 24/7, completely free, and personalized to each student.

### Why Agents and Not Just a Chatbot?

| Feature | Regular Chatbot | PlacementCoach Pro |
|---------|----------------|--------------------|
| Memory | Forgets each turn | Remembers full student profile |
| Actions | Only talks | Fetches company data, scores resume |
| Personalization | Generic | Adapts to YOUR specific profile |
| Tools | None | 5 specialized tools |
| Error handling | Crashes | Graceful retry logic |

---

## Live Demo and Deployment

| Link | Description |
|------|-------------|
| [Live Streamlit App](https://kaggle-app-ai-agent-uxi2imzmcnxc7r88bj7q4n.streamlit.app/) | Interactive web app — try your own profile |
| [Kaggle Notebook](https://www.kaggle.com/jannatgarg) | Full agent code with all 5 tools | 
| [Demo Video](https://loom.com) | 3-minute walkthrough of the agent | 
| [GitHub Repo](https://github.com/jannatgarg2005/kaggle-google-ai-agent) | Full source code and README |

> **REPLACE** the Streamlit, Kaggle notebook, and Loom links above with your real URLs after deployment.

### Two Ways to Run This

**Option 1 — Live Streamlit App (Recommended for judges)**  
Visit [placementcoach.streamlit.app](https://kaggle-app-ai-agent-uxi2imzmcnxc7r88bj7q4n.streamlit.app/) — enter your own profile and get personalized results instantly. No setup required.

**Option 2 — Kaggle Notebook**  
Open the notebook, click Copy and Edit, add your Gemini API key in Secrets, and click Run All.

---

## Architecture

```
Student Input (natural language)
        |
        v
+-----------------------------------------------+
|         PlacementCoach Pro Agent              |
|      Gemini 2.0 Flash + System Instructions   |
|                                               |
|  student_profile {}  <-- MEMORY               |
|  Updates every turn, persists full session    |
+-----------------------------------------------+
        |
        | Automatic Function Calling
        |
   +---------+-----------+-----------+----------+
   |         |           |           |          |
   v         v           v           v          v
Tool 1    Tool 2      Tool 3      Tool 4     Tool 5
Resume    Company     Study       Mock       Job
Scorer    Pattern     Plan        Interview  Search
          Fetcher     Generator   Questions  Strategy
   |         |           |           |          |
   v         v           v           v          v
        Personalized Response to Student
```

---

## Tools Built (Function Calling)

| Tool | Purpose | Output |
|------|---------|--------|
| `evaluate_resume_strength()` | Scores resume 0-100 with ranked feedback | Score + priority action items |
| `get_company_interview_pattern()` | Fetches interview rounds per company | Rounds, CTC, pro tips |
| `generate_study_plan()` | Creates week-by-week prep schedule | Timeline + daily routine |
| `get_mock_interview_questions()` | Adaptive questions with hints | Questions + answer frameworks |
| `search_job_openings()` | Job search strategy by role | Platforms + immediate steps |

---

## Course Concepts Demonstrated

| Concept | Implementation |
|---------|---------------|
| Gemini API | gemini-2.0-flash via google-generativeai SDK |
| Function Calling | 5 custom typed tools with structured JSON output |
| Automatic Function Calling | enable_automatic_function_calling=True |
| Multi-turn Stateful Memory | student_profile dict updates every conversation turn |
| System Instructions | Agent personality, behavior rules, response format |
| Error Handling | Retry logic with exponential backoff for rate limits |
| Safe Key Management | Kaggle Secrets only — no hardcoded API keys |

---

## Setup and Run

### Option 1 — Run on Kaggle (Recommended, Zero Setup)

1. Open the Kaggle Notebook — REPLACE WITH YOUR NOTEBOOK URL
2. Click **Copy and Edit**
3. Add your Gemini API key:
   - Click **Add-ons** then **Secrets**
   - Name: `GEMINI_API_KEY` | Value: your key from [aistudio.google.com](https://aistudio.google.com/app/apikey)
   - Toggle **Notebook has access** to ON
4. Click **Run All**

### Option 2 — Run Locally

```bash
# Clone the repository
git clone https://github.com/jannatgarg2005/kaggle-google-ai-agent
cd kaggle-google-ai-agent

# Install dependencies
pip install google-generativeai

# Set your API key (never hardcode it)
export GEMINI_API_KEY="your-api-key-here"

# Run the agent
python placementcoach_capstone.py
```

---

## What the Demo Shows

```
PART 1: Direct Tool Execution (no API quota needed)
  Tool 1: Resume scored 68/100 for student profile
  Tool 2: Amazon 7 interview rounds with pro tips
  Tool 3: 45-day study plan with time allocation breakdown
  Tool 4: 3 ML questions with hints and answer frameworks
  Tool 5: Top job platforms with application strategy

PART 2: Multi-turn Stateful Conversation (3 turns)
  Turn 1: Student shares profile -> agent evaluates resume
  Turn 2: Student targets Amazon -> agent fetches rounds + builds plan
  Turn 3: Student asks for questions -> agent gives mock interview set

  Key: Agent remembers CGPA, college, and targets across ALL turns
  without being re-told. This is multi-turn stateful memory.

PART 3: Session Report
  Summary of student profile captured and all concepts shown
```

---

## Social Impact (Agents for Good)

**Who this helps:**
- 1.5M+ engineering graduates in India annually
- Students from tier-2 and tier-3 colleges without placement cell support
- First-generation college students with no industry connections
- Students who cannot afford Rs.50,000+ per career coaching session

**What it replaces:**
- Expensive career coaches
- Generic one-size-fits-all prep guides
- Unstructured YouTube advice

---

## Project Structure

```
kaggle-google-ai-agent/
    app.py                        Streamlit web app (live deployment)
    placementcoach_capstone.py    Kaggle notebook code (all 6 cells)
    requirements.txt              Python dependencies for Streamlit Cloud
    README.md                     This file
    .gitignore                    Excludes API keys and cache files
```

---

## Author

**Jannat Garg**  
Final Year B.Tech CSE | BPIT New Delhi | AI/ML Engineer

- GitHub: [github.com/jannatgarg2005](https://github.com/jannatgarg2005)
- Kaggle: [kaggle.com/jannatgarg](https://www.kaggle.com/jannatgarg)
- LinkedIn: [jannat-garg-1699a3366](https://www.linkedin.com/in/jannat-garg-1699a3366)
- Email: jannatgarg2005@gmail.com

*"I built the tool I wish existed when I started my placement preparation."*

---

## License

MIT License. Free to use, modify, and distribute with attribution.
