# ============================================================
# PlacementCoach Pro — Streamlit Web App
# AI Career Coach for Engineering Placement Preparation
# Author: Jannat Garg | BPIT Delhi
# Kaggle x Google AI Agents Intensive 2026
# ============================================================

import streamlit as st
import json

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="PlacementCoach Pro",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .tool-card {
        background: #f8f9fa;
        border-left: 4px solid #667eea;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    .score-high   { color: #28a745; font-size: 2rem; font-weight: bold; }
    .score-medium { color: #ffc107; font-size: 2rem; font-weight: bold; }
    .score-low    { color: #dc3545; font-size: 2rem; font-weight: bold; }
    .priority-critical { border-left: 4px solid #dc3545; background: #fff5f5; padding: 0.8rem; border-radius: 6px; margin: 0.3rem 0; }
    .priority-high     { border-left: 4px solid #fd7e14; background: #fff8f0; padding: 0.8rem; border-radius: 6px; margin: 0.3rem 0; }
    .priority-medium   { border-left: 4px solid #ffc107; background: #fffdf0; padding: 0.8rem; border-radius: 6px; margin: 0.3rem 0; }
    .round-badge {
        background: #667eea;
        color: white;
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        font-size: 0.8rem;
        margin-right: 0.5rem;
    }
    .memory-box {
        background: #e8f4fd;
        border: 1px solid #bee3f8;
        padding: 0.8rem;
        border-radius: 8px;
        font-family: monospace;
        font-size: 0.85rem;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        padding: 8px 20px;
        border-radius: 8px 8px 0 0;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# KNOWLEDGE BASE
# ============================================================

COMPANY_DATABASE = {
    "google": {
        "full_name": "Google / Alphabet",
        "roles": ["Software Engineer", "ML Engineer", "Data Scientist"],
        "interview_rounds": [
            "Online Assessment (90 min — LeetCode Hard level)",
            "Technical Phone Screen (45 min — DSA + System Design basics)",
            "Onsite Round 1: Coding (LeetCode Medium-Hard)",
            "Onsite Round 2: Coding (LeetCode Medium-Hard)",
            "Onsite Round 3: System Design",
            "Onsite Round 4: Behavioral (Googleyness)",
            "Hiring Committee Review"
        ],
        "primary_focus": ["Data Structures", "Algorithms", "System Design", "ML Fundamentals"],
        "difficulty": "Very High",
        "avg_ctc": "Rs.40-80 LPA",
        "prep_months": 6,
        "tips": [
            "Think aloud always — process matters more than the answer",
            "Googleyness tests collaboration and intellectual humility",
            "ML roles require fundamentals depth, not just library knowledge"
        ]
    },
    "amazon": {
        "full_name": "Amazon / AWS",
        "roles": ["SDE-1", "SDE-2", "Applied Scientist", "ML Engineer"],
        "interview_rounds": [
            "Online Assessment (2 coding + work simulation — 105 min)",
            "Phone Screen (1 coding + 2 Leadership Principles stories)",
            "Loop Round 1: Coding — LeetCode Medium",
            "Loop Round 2: System Design",
            "Loop Round 3: Leadership Principles deep dive",
            "Loop Round 4: Bar Raiser (wildcard)",
            "Loop Round 5: Hiring Manager"
        ],
        "primary_focus": ["Leadership Principles (16 LPs)", "DSA", "System Design"],
        "difficulty": "High",
        "avg_ctc": "Rs.35-55 LPA",
        "prep_months": 4,
        "tips": [
            "Every round can pivot to a Leadership Principle — prepare 32+ STAR stories",
            "Bar Raiser protects the hiring bar — they can come from any team",
            "Ownership and Customer Obsession are weighted most heavily"
        ]
    },
    "microsoft": {
        "full_name": "Microsoft",
        "roles": ["SWE", "Data Scientist", "ML Engineer"],
        "interview_rounds": [
            "Online Assessment (2 coding problems — 60 min)",
            "Technical Screen (1 problem + discussion)",
            "Interview Round 1: Problem Solving",
            "Interview Round 2: Problem Solving + Design",
            "Interview Round 3: Behavioral + Culture"
        ],
        "primary_focus": ["Problem Solving", "Communication", "Growth Mindset"],
        "difficulty": "High",
        "avg_ctc": "Rs.35-60 LPA",
        "prep_months": 3,
        "tips": [
            "Communication matters as much as technical skill",
            "Show genuine curiosity — ask thoughtful questions back",
            "Growth Mindset: show willingness to learn from mistakes"
        ]
    },
    "flipkart": {
        "full_name": "Flipkart (Walmart subsidiary)",
        "roles": ["SDE-1", "Data Scientist", "ML Engineer"],
        "interview_rounds": [
            "Online Assessment (3 coding + MCQs — 90 min)",
            "Technical Round 1: DSA focus",
            "Technical Round 2: DSA + System Design",
            "Technical Round 3: Low-Level Design",
            "Managerial + HR Round"
        ],
        "primary_focus": ["DSA", "System Design", "Low-Level Design"],
        "difficulty": "High",
        "avg_ctc": "Rs.20-40 LPA",
        "prep_months": 3,
        "tips": [
            "Strong Low-Level Design rounds — practice class diagrams",
            "E-commerce system design is a frequent topic",
            "Good stepping stone to larger product companies"
        ]
    },
    "startup": {
        "full_name": "AI/ML Startups (General)",
        "roles": ["ML Engineer", "Data Scientist", "AI Engineer"],
        "interview_rounds": [
            "Take-home Assignment (3-7 days — build something real)",
            "Technical Discussion (walk through your assignment)",
            "Culture Fit / Founder Interview",
            "Optional: Pair Programming Session"
        ],
        "primary_focus": ["Practical skills", "GitHub portfolio", "Project depth"],
        "difficulty": "Medium",
        "avg_ctc": "Rs.8-25 LPA",
        "prep_months": 1,
        "tips": [
            "Projects beat degrees — show what you can build NOW",
            "A deployed Streamlit app > 10 Coursera certificates",
            "GitHub daily commits signal a serious developer"
        ]
    },
    "infosys": {
        "full_name": "Infosys",
        "roles": ["Systems Engineer", "Data Scientist", "AI Analyst"],
        "interview_rounds": [
            "InfyTQ Platform Assessment (aptitude + coding)",
            "Technical Interview (basic DSA + CS fundamentals)",
            "HR Interview"
        ],
        "primary_focus": ["Aptitude", "Basic Coding", "Communication"],
        "difficulty": "Low-Medium",
        "avg_ctc": "Rs.3.6-8 LPA",
        "prep_months": 1,
        "tips": [
            "HackerRank Python Basic + SQL Basic badges help you stand out",
            "Communication matters as much as coding here",
            "Strong training programs — good first job"
        ]
    }
}

MOCK_QUESTIONS = {
    "ml": [
        {"q": "What is the difference between supervised and unsupervised learning?",
         "hint": "Think: do you have labeled output (y) or not?",
         "framework": "Supervised = labeled data to predict output (spam, house prices). "
                      "Unsupervised = no labels, find patterns (clustering, PCA).",
         "follow_up": "Which would you use for customer segmentation?"},
        {"q": "Explain overfitting and underfitting. How do you detect and fix each?",
         "hint": "Think about the training vs validation performance gap.",
         "framework": "Overfit: high train, low val -> regularization, dropout, more data. "
                      "Underfit: low on both -> more features, complex model.",
         "follow_up": "What is the bias-variance tradeoff?"},
        {"q": "Why do we split data into train, validation, and test sets?",
         "hint": "What is each set's specific purpose in the ML workflow?",
         "framework": "Train: model learns. Val: hyperparameter tuning. "
                      "Test: final unbiased evaluation — touch only once!",
         "follow_up": "What is data leakage?"}
    ],
    "dsa": [
        {"q": "Find two numbers in an array that sum to a target. What is the optimal approach?",
         "hint": "Can you store something while iterating to avoid O(n2) brute force?",
         "framework": "HashMap: for each num, check if (target-num) exists. "
                      "O(n) time, O(n) space. LeetCode #1 Two Sum.",
         "follow_up": "Can you solve it in O(1) space if the array is sorted?"},
        {"q": "Find the maximum subarray sum including arrays with negative numbers.",
         "hint": "Kadane's Algorithm — what happens when the running sum goes negative?",
         "framework": "Track current_sum and max_sum. Reset current_sum to 0 when negative. "
                      "O(n) time, O(1) space. LeetCode #53.",
         "follow_up": "How would you also return the subarray itself?"}
    ],
    "behavioral": [
        {"q": "Tell me about yourself.",
         "hint": "Past to Present to Future formula. Keep to 90 seconds.",
         "framework": "PAST: degree + focus area. PRESENT: current project + certifications. "
                      "FUTURE: what you want to contribute at this company.",
         "follow_up": "Do not recite your resume — tell a story with momentum."},
        {"q": "Describe a challenging project and how you overcame obstacles.",
         "hint": "Use STAR: Situation, Task, Action, Result.",
         "framework": "SITUATION: context. TASK: your role. "
                      "ACTION: exact steps. RESULT: quantified impact.",
         "follow_up": "Always end with a Result — most candidates forget this."}
    ],
    "system_design": [
        {"q": "Design a URL shortener like bit.ly.",
         "hint": "Start with requirements and scale before jumping to solutions.",
         "framework": "Requirements -> API design -> DB schema -> hashing strategy -> "
                      "scale with cache and CDN.",
         "follow_up": "How would you handle 100x more traffic?"}
    ]
}

# ============================================================
# TOOL FUNCTIONS (same logic as notebook)
# ============================================================

def evaluate_resume(skills, projects, deployed, internships, cgpa, certs, github, kaggle):
    scores = {}
    feedback = []

    skill_score = min(len(skills) * 2, 20)
    scores["Skills"] = (skill_score, 20)
    if len(skills) < 5:
        feedback.append({"priority": "HIGH", "area": "Skills",
            "action": f"Add {5-len(skills)} more skills. Target: SQL, LangChain, FastAPI, Git."})

    proj_score = min(projects * 5, 15) + min(deployed * 5, 10)
    scores["Projects"] = (proj_score, 25)
    if projects < 2:
        feedback.append({"priority": "CRITICAL", "area": "Projects",
            "action": "Build 2 projects minimum — Churn Prediction and RAG Chatbot are great starts."})
    elif deployed == 0:
        feedback.append({"priority": "HIGH", "area": "Deployment",
            "action": "Deploy 1 project on Streamlit Cloud. A live URL is 10x more impactful."})

    intern_score = min(internships * 10, 20)
    scores["Internship"] = (intern_score, 20)
    if internships == 0:
        feedback.append({"priority": "CRITICAL", "area": "Internship",
            "action": "Apply on Internshala and AngelList this week."})

    cgpa_score = min(int((cgpa / 10) * 15), 15)
    scores["CGPA"] = (cgpa_score, 15)
    if cgpa < 7.0:
        feedback.append({"priority": "MEDIUM", "area": "CGPA",
            "action": f"CGPA {cgpa} may not pass cutoffs (7.5+). Compensate with stronger projects."})

    cert_score = min(len(certs) * 3, 10)
    scores["Certifications"] = (cert_score, 10)
    if len(certs) == 0:
        feedback.append({"priority": "MEDIUM", "area": "Certifications",
            "action": "Get Kaggle Python cert (free, 5 hrs) + HackerRank Python Basic badge."})

    presence_score = (5 if github else 0) + (5 if kaggle else 0)
    scores["Online Presence"] = (presence_score, 10)
    if not github:
        feedback.append({"priority": "HIGH", "area": "GitHub",
            "action": "Commit daily. A 60-day streak signals a serious developer."})

    total = sum(v[0] for v in scores.values())
    priority_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2}
    feedback.sort(key=lambda x: priority_order.get(x["priority"], 3))

    return total, scores, feedback


def get_study_plan(company, days, hours_per_day, weak_areas):
    total = days * hours_per_day
    is_product = company in ["google", "amazon", "microsoft", "flipkart"]

    if is_product:
        alloc = {"DSA Practice": 0.50, "ML/Domain Skills": 0.25,
                 "Projects": 0.15, "Mock Interviews": 0.10}
    else:
        alloc = {"DSA Practice": 0.20, "ML/Domain Skills": 0.40,
                 "Projects": 0.30, "Mock Interviews": 0.10}

    weeks = []
    for w in range(1, min(days // 7 + 1, 7)):
        if w <= 2:   phase, focus = "Foundation",     "Arrays, Strings, HashMaps (LeetCode Easy)"
        elif w <= 4: phase, focus = "Core Skills",    "Trees, Graphs, DP (LeetCode Medium)"
        elif w <= 6: phase, focus = "Advanced",       "System Design + Mixed LeetCode"
        else:        phase, focus = "Interview Prep", "Company-specific + Mock Interviews"
        weeks.append({"week": w, "phase": phase, "focus": focus,
                      "hours": round(hours_per_day * 7, 1)})

    return {
        "total_hours": total,
        "allocation": {k: (int(total * v), f"{int(v*100)}%") for k, v in alloc.items()},
        "weeks": weeks,
        "milestones": [
            f"Week 1: Complete Kaggle Python certificate",
            f"Week 2: Earn HackerRank Python Basic badge",
            f"Week 3: Build and deploy first ML project",
            f"Week 4: Apply to {COMPANY_DATABASE.get(company, COMPANY_DATABASE['startup'])['full_name']}",
            f"Week 6: 50 LeetCode problems solved",
            f"Week 8: Full mock interviews — ready to apply"
        ]
    }

# ============================================================
# SIDEBAR — STUDENT PROFILE
# ============================================================

with st.sidebar:
    st.markdown("## Student Profile")
    st.markdown("*Fill your details — the coach personalizes everything to you*")
    st.divider()

    name  = st.text_input("Your Name", value="Jannat Garg")
    college = st.text_input("College", value="BPIT Delhi")
    cgpa  = st.slider("CGPA (out of 10)", 5.0, 10.0, 7.8, 0.1)
    year  = st.selectbox("Year", ["1st", "2nd", "3rd", "Final Year"], index=3)

    st.markdown("**Skills**")
    skills_input = st.text_area("Skills (comma separated)",
                                value="Python, ML, scikit-learn, SQL, LangChain, Gemini API")
    skills = [s.strip() for s in skills_input.split(",") if s.strip()]

    st.markdown("**Projects & Experience**")
    projects   = st.number_input("Total Projects Built", 0, 20, 2)
    deployed   = st.number_input("Projects Deployed/Live", 0, 20, 0)
    internships = st.number_input("Internships", 0, 10, 1)

    st.markdown("**Certifications**")
    certs_input = st.text_area("Certifications (comma separated)",
                               value="Google AI Certificate, Kaggle Python Certificate")
    certs = [c.strip() for c in certs_input.split(",") if c.strip()]

    st.markdown("**Online Presence**")
    github_active = st.checkbox("GitHub — active commits", value=True)
    kaggle_active = st.checkbox("Kaggle — active notebooks", value=True)

    st.divider()
    st.markdown("**Target Company**")
    company = st.selectbox("Target Company",
                           ["amazon", "google", "microsoft", "flipkart", "startup", "infosys"],
                           index=0)
    days = st.slider("Days Until Placement Season", 7, 180, 45)
    hours_day = st.slider("Study Hours Per Day", 1.0, 10.0, 5.0, 0.5)

    weak_input = st.multiselect("Weak Areas",
                                ["DSA", "System Design", "ML Theory", "Behavioral", "Low-Level Design"],
                                default=["DSA", "System Design"])

# ============================================================
# MAIN HEADER
# ============================================================

st.markdown("""
<div class="main-header">
    <h1>PlacementCoach Pro</h1>
    <p>Your AI Career Coach for Engineering Placements</p>
    <p><em>Built for Kaggle x Google AI Agents Intensive 2026 | Track: Agents for Good</em></p>
</div>
""", unsafe_allow_html=True)

# Agent memory display
st.markdown("**Agent Memory (updates as you change your profile)**")
st.markdown(f"""
<div class="memory-box">
student_profile = {{<br>
&nbsp;&nbsp;name: "{name}",&nbsp;&nbsp;college: "{college}",&nbsp;&nbsp;cgpa: {cgpa},<br>
&nbsp;&nbsp;skills: {skills[:4]}...,&nbsp;&nbsp;projects: {projects},&nbsp;&nbsp;deployed: {deployed},<br>
&nbsp;&nbsp;internships: {internships},&nbsp;&nbsp;target: "{company}",&nbsp;&nbsp;prep_days: {days}<br>
}}
</div>
""", unsafe_allow_html=True)

st.divider()

# ============================================================
# TABS — 5 TOOLS
# ============================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Resume Evaluator",
    "Company Patterns",
    "Study Plan",
    "Mock Interview",
    "Job Search"
])

# ---- TAB 1: RESUME EVALUATOR ----
with tab1:
    st.markdown("### Resume Strength Evaluator")
    st.markdown("*Tool: `evaluate_resume_strength()` — scores your profile 0 to 100*")

    total, scores, feedback = evaluate_resume(
        skills, projects, deployed, internships, cgpa, certs,
        github_active, kaggle_active
    )

    col1, col2 = st.columns([1, 2])
    with col1:
        css_class = "score-high" if total >= 70 else ("score-medium" if total >= 45 else "score-low")
        level = "STRONG" if total >= 80 else ("GOOD" if total >= 60 else ("AVERAGE" if total >= 40 else "BUILDING"))
        st.markdown(f'<p class="{css_class}">{total}/100</p>', unsafe_allow_html=True)
        st.markdown(f"**Level:** {level}")
        st.progress(total / 100)

    with col2:
        st.markdown("**Score Breakdown**")
        for area, (score, max_score) in scores.items():
            pct = score / max_score
            color = "green" if pct >= 0.7 else ("orange" if pct >= 0.4 else "red")
            st.markdown(f"`{area}` — {score}/{max_score}")
            st.progress(pct)

    st.divider()
    st.markdown("**Prioritized Action Items**")
    if not feedback:
        st.success("Your profile looks strong! Focus on deploying your projects.")
    else:
        for fb in feedback:
            p = fb['priority']
            css = "priority-critical" if p == "CRITICAL" else ("priority-high" if p == "HIGH" else "priority-medium")
            icon = "🔴" if p == "CRITICAL" else ("🟡" if p == "HIGH" else "🟢")
            st.markdown(f"""
            <div class="{css}">
                <strong>{icon} [{p}] {fb['area']}</strong><br>
                {fb['action']}
            </div>
            """, unsafe_allow_html=True)

# ---- TAB 2: COMPANY PATTERNS ----
with tab2:
    st.markdown("### Company Interview Pattern")
    st.markdown(f"*Tool: `get_company_interview_pattern('{company}')` — fetches real interview data*")

    if company in COMPANY_DATABASE:
        d = COMPANY_DATABASE[company]
        col1, col2, col3 = st.columns(3)
        col1.metric("Difficulty", d["difficulty"])
        col2.metric("Avg CTC India", d["avg_ctc"])
        col3.metric("Prep Time", f"{d['prep_months']} months")

        st.markdown(f"**Roles Available:** {', '.join(d['roles'])}")
        st.markdown(f"**Primary Focus:** {', '.join(d['primary_focus'])}")

        st.divider()
        st.markdown("**Interview Rounds**")
        for i, rd in enumerate(d["interview_rounds"], 1):
            st.markdown(f"""
            <span class="round-badge">Round {i}</span> {rd}
            """, unsafe_allow_html=True)

        st.divider()
        st.markdown("**Pro Tips from People Who Got In**")
        for tip in d["tips"]:
            st.info(f"💡 {tip}")

# ---- TAB 3: STUDY PLAN ----
with tab3:
    st.markdown("### Personalized Study Plan")
    st.markdown(f"*Tool: `generate_study_plan('{company}', {days} days, {hours_day} hrs/day)*")

    plan = get_study_plan(company, days, hours_day, weak_input)

    col1, col2 = st.columns(2)
    col1.metric("Total Study Hours", f"{plan['total_hours']} hrs")
    col2.metric("Weeks Available", f"{days // 7} weeks")

    st.divider()
    st.markdown("**Time Allocation**")
    cols = st.columns(4)
    for i, (area, (hrs, pct)) in enumerate(plan["allocation"].items()):
        cols[i].metric(area, f"{hrs} hrs", pct)

    st.divider()
    st.markdown("**Weekly Breakdown**")
    for week in plan["weeks"]:
        with st.expander(f"Week {week['week']} — {week['phase']} ({week['hours']} hrs)"):
            st.markdown(f"**Focus:** {week['focus']}")

    st.divider()
    st.markdown("**Key Milestones**")
    for m in plan["milestones"]:
        st.markdown(f"- {m}")

    st.divider()
    st.markdown("**Recommended Daily Routine**")
    st.markdown("""
    | Time | Activity |
    |------|----------|
    | 6 AM – 9 AM | LeetCode DSA (peak focus hours) |
    | 2 PM – 4 PM | ML courses and project building |
    | 6 PM – 8 PM | Kaggle notebooks and theory revision |
    | 9 PM – 10 PM | HackerRank practice and company research |
    """)

# ---- TAB 4: MOCK INTERVIEW ----
with tab4:
    st.markdown("### Mock Interview Practice")
    st.markdown("*Tool: `get_mock_interview_questions()` — adaptive questions with hints*")

    col1, col2 = st.columns(2)
    domain     = col1.selectbox("Domain", ["ml", "dsa", "behavioral", "system_design"])
    difficulty = col2.selectbox("Difficulty", ["beginner", "intermediate"])

    questions = MOCK_QUESTIONS.get(domain, MOCK_QUESTIONS["ml"])

    for i, q in enumerate(questions, 1):
        with st.expander(f"Q{i}: {q['q']}", expanded=(i == 1)):
            st.markdown(f"**Hint:** {q['hint']}")
            st.markdown(f"**Answer Framework:**")
            st.info(q['framework'])
            if q.get('follow_up'):
                st.warning(f"**Likely Follow-up:** {q['follow_up']}")

    st.divider()
    st.markdown("**Interview Tips**")
    tips = [
        "Think aloud — interviewers want to see your process, not just the answer",
        "Clarify requirements before diving into a solution",
        "Start with brute force, then optimize",
        "Test your solution with edge cases before declaring done"
    ]
    for tip in tips:
        st.markdown(f"- {tip}")

# ---- TAB 5: JOB SEARCH ----
with tab5:
    st.markdown("### Job Search Strategy")
    st.markdown("*Tool: `search_job_openings()` — platforms and application strategy*")

    platforms = [
        {"name": "LinkedIn",           "url": "linkedin.com/jobs",
         "strategy": f"Set job alert: '{company.title()} Engineer Fresher India'. Apply within 24h of posting."},
        {"name": "Naukri",             "url": "naukri.com",
         "strategy": "Best for Indian companies. Upload resume and set profile to Active."},
        {"name": "Internshala",        "url": "internshala.com",
         "strategy": "Best for internships — many convert to full-time offers."},
        {"name": "AngelList/Wellfound","url": "wellfound.com",
         "strategy": "Best for AI startups — many don't post on Naukri or LinkedIn."},
        {"name": "Company Career Pages","url": "Direct",
         "strategy": "Google Careers, Amazon Jobs — direct applications get fastest responses."}
    ]

    for p in platforms:
        with st.expander(f"{p['name']} — {p['url']}"):
            st.markdown(p["strategy"])

    st.divider()
    st.markdown("**Resume Keywords to Include**")
    keywords = ["Python", "Machine Learning", "Deep Learning", "NLP",
                "TensorFlow", "PyTorch", "Scikit-learn", "Pandas", "SQL",
                "LangChain", "RAG", "LLM", "Gemini API", "HuggingFace",
                "FastAPI", "Streamlit", "Git", "Docker"]
    st.markdown(" ".join([f"`{k}`" for k in keywords]))

    st.divider()
    st.markdown("**Immediate Actions This Week**")
    actions = [
        f"Update LinkedIn headline: '{company.title()} Engineer | Python | Open to Work'",
        "Set LinkedIn Open to Work (private — visible to recruiters only)",
        "Connect with 5 ML engineers at target companies this week",
        "Apply to 3 companies today — don't wait for a perfect resume"
    ]
    for a in actions:
        st.markdown(f"- {a}")

# ============================================================
# FOOTER
# ============================================================

st.divider()
st.markdown("""
**PlacementCoach Pro** | Built for Kaggle x Google AI Agents Intensive 2026 | Track: Agents for Good  
Author: Jannat Garg | BPIT Delhi | [github.com/jannatgarg2005](https://github.com/jannatgarg2005) | [kaggle.com/jannatgarg](https://www.kaggle.com/jannatgarg)

*Democratizing career coaching for 1.5M+ engineering students in India*
""")