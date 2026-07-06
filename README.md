# PlacementCoach Pro 🎯
### AI Agent for Campus Placement Preparation | Kaggle × Google AI Agents Intensive 2026

[![Kaggle](https://img.shields.io/badge/Kaggle-Notebook-20BEFF?style=for-the-badge&logo=kaggle)](https://www.kaggle.com/jannatgarg)
[![Google Gemini](https://img.shields.io/badge/Gemini_API-1.5_Flash-4285F4?style=for-the-badge&logo=google)](https://aistudio.google.com)
[![Track](https://img.shields.io/badge/Track-Agents_for_Good-green?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)]()

---

## 🚨 The Problem

Every year, **1.5 million+ engineering graduates** in India compete for a fraction of AI/ML roles.

Most students face this exact situation:
- ❌ Don't know which companies match their profile
- ❌ Don't know what to study or in what order
- ❌ Can't afford ₹50,000+ career counselling sessions
- ❌ Get generic advice that doesn't consider their specific background
- ❌ No personalized mock interview practice

**I am one of these students.** I'm Jannat Garg, final-year B.Tech CSE at BPIT Delhi. I built the solution I needed.

---

## 💡 The Solution: PlacementCoach Pro

An intelligent **multi-agent AI system** that acts as a personal career coach — available 24/7, completely free, and fully personalized to each student.

### Why Agents (not just a chatbot)?

| Feature | Regular Chatbot | PlacementCoach Pro |
|---------|----------------|-------------------|
| Memory | Forgets each turn | ✅ Remembers your full profile |
| Actions | Only talks | ✅ Fetches company data, scores resume |
| Personalization | Generic responses | ✅ Adapts to YOUR profile |
| Tools | None | ✅ 5 specialized tools |
| Error handling | Crashes | ✅ Graceful degradation |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Student (User)                    │
└───────────────────────┬─────────────────────────────┘
                        │ natural language input
                        ▼
┌─────────────────────────────────────────────────────┐
│           PlacementCoach Pro Agent                   │
│         (Gemini 1.5 Flash + System Instructions)    │
│                                                     │
│  Memory Store: student_profile {}                   │
│  • name, college, cgpa, skills, projects            │
│  • target_companies, certifications                 │
│  • Persists across ALL conversation turns           │
└──────────────────┬──────────────────────────────────┘
                   │ Automatic Function Calling
          ┌────────┼────────────────────┐
          ▼        ▼                    ▼
    ┌──────────┐ ┌──────────────┐ ┌────────────────┐
    │ Company  │ │   Resume     │ │   Study Plan   │
    │ Pattern  │ │  Evaluator   │ │  Generator     │
    │  Tool    │ │    Tool      │ │    Tool        │
    └──────────┘ └──────────────┘ └────────────────┘
          ▼        ▼                    ▼
    ┌──────────┐ ┌──────────────┐
    │  Mock    │ │  Job Search  │
    │Interview │ │  Strategy    │
    │   Tool   │ │    Tool      │
    └──────────┘ └──────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────┐
│         Personalized Response to Student             │
└─────────────────────────────────────────────────────┘
```

---

## 🔧 Tools Built (Function Calling)

| Tool | Purpose | Input | Output |
|------|---------|-------|--------|
| `get_company_interview_pattern()` | Fetch interview rounds, focus areas, pro tips | company name | Structured interview data |
| `evaluate_resume_strength()` | Score resume 0-100 with prioritized feedback | skills, projects, CGPA, etc. | Score + action items |
| `generate_study_plan()` | Create week-by-week preparation schedule | target company, days, hours | Complete study roadmap |
| `get_mock_interview_questions()` | Adaptive DSA/ML/behavioral questions | role, difficulty, domain | Questions + hints + frameworks |
| `search_job_openings()` | Job search strategy and platform recommendations | role, experience level | Strategy + platforms + tips |

---

## 🛠️ Technologies Used

- **Gemini 1.5 Flash** — Core LLM powering the agent
- **Google AI Python SDK** (`google-generativeai`) — API integration
- **Function Calling** — Automatic tool use by the agent
- **Kaggle Secrets** — Secure API key management (no hardcoded keys)
- **Python** — Agent architecture, tools, memory management

---

## 🚀 Setup Instructions

### Prerequisites
- Kaggle account (phone verified)
- Google AI Studio API key (free at [aistudio.google.com](https://aistudio.google.com))

### Run on Kaggle (Recommended — Zero Setup)

1. **Open the Kaggle notebook:** [Link to your notebook]
2. **Add your API key:**
   - Click `Add-ons` → `Secrets`
   - Add secret: Name = `GEMINI_API_KEY`, Value = your key
   - Toggle `Notebook has access` → ON
3. **Run all cells:** `Session` → `Run All`
4. Watch PlacementCoach Pro in action!

### Run Locally

```bash
# Clone the repository
git clone https://github.com/jannatgarg2005/kaggle-google-ai-agent
cd kaggle-google-ai-agent

# Install dependencies
pip install google-generativeai

# Set your API key
export GEMINI_API_KEY="your-api-key-here"

# Run the agent
python placementcoach_capstone.py
```

> ⚠️ **Security Note:** Never hardcode API keys. Always use environment variables or secure secret managers.

---

## 📊 Course Concepts Demonstrated

| Concept | Implementation |
|---------|---------------|
| ✅ Gemini API | `genai.GenerativeModel("gemini-1.5-flash")` |
| ✅ Function Calling | 5 custom tools with typed inputs/outputs |
| ✅ Automatic Function Calling | `enable_automatic_function_calling=True` |
| ✅ Multi-turn Memory | `student_profile` dict persists across session |
| ✅ System Instructions | Personality, behavior rules, response format |
| ✅ Error Handling | Quota limits, invalid API keys, bad inputs |
| ✅ Structured Output | JSON responses from all tools |
| ✅ Safe Key Management | Kaggle Secrets + environment variables |

---

## 🌍 Social Impact (Agents for Good)

**Who this helps:**
- 1.5M+ engineering graduates in India annually
- Students from tier-2/tier-3 colleges without campus placement support
- First-generation college students with no industry connections
- Students who cannot afford career counselling (₹50,000+ per session)

**What it replaces:**
- Expensive career coaches
- Generic YouTube "how to get placed" videos
- One-size-fits-all preparation guides

**What makes it unique:**
- Fully personalized to each student's profile
- Free and accessible to anyone with internet
- Available 24/7 — no appointment needed
- Scales infinitely — one agent, millions of students

---

## 👩‍💻 About the Author

**Jannat Garg**
Final Year B.Tech CSE | BPIT, New Delhi | AI/ML Engineer in the making

- 🔗 GitHub: [github.com/jannatgarg2005](https://github.com/jannatgarg2005)
- 🔗 Kaggle: [kaggle.com/jannatgarg](https://www.kaggle.com/jannatgarg)
- 🔗 LinkedIn: [linkedin.com/in/jannat-garg-1699a3366](https://www.linkedin.com/in/jannat-garg-1699a3366)

*"I built the tool I wish existed when I started my placement preparation."*

---

## 📄 License

MIT License — Free to use, modify, and distribute with attribution.
