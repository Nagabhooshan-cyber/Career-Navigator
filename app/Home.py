import streamlit as st

st.set_page_config(
    page_title="Career Navigator",
    page_icon="🚀",
    layout="wide"
)

# ==========================================
# TITLE
# ==========================================

st.title("🚀 Career Navigator")

st.markdown("""
Your AI-powered platform for:

* 📊 Job Market Insights
* 💰 Salary Prediction
* 📄 Resume Analysis
* 🎯 Skill Gap Detection
* 💼 Job Recommendations
""")

st.divider()

# ==========================================
# KPI SECTION
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📋 Jobs Analyzed",
        "2,253"
    )

with col2:
    st.metric(
        "💰 Salary Records",
        "607"
    )

with col3:
    st.metric(
        "🧠 Skills Tracked",
        "28+"
    )

with col4:
    st.metric(
        "📈 Features",
        "5"
    )

st.divider()

# ==========================================
# FEATURES
# ==========================================

st.header("🚀 Explore Features")

col1, col2 = st.columns(2)

with col1:

    st.page_link(
        "pages/3_Job_Insights.py",
        label="📊 Job Market Insights",
        icon="📊"
    )

    st.write("""
    Explore:
    - Top Hiring Locations
    - Salary Trends
    - Industries Hiring
    - Remote Work Statistics
    """)

    st.page_link(
        "pages/2_Salary_Predictor.py",
        label="💰 Salary Predictor",
        icon="💰"
    )

    st.write("""
    Predict salaries using:
    - Experience Level
    - Employment Type
    - Company Size
    - Remote Work %
    """)

with col2:

    st.page_link(
        "pages/1_Skill_Gap.py",
        label="📄 Resume Analyzer",
        icon="📄"
    )

    st.write("""
    Analyze:
    - Resume Skills
    - JD Skills
    - Match Score
    - Missing Skills
    """)

    st.page_link(
        "pages/1_Skill_Gap.py",
        label="💼 Job Recommendations",
        icon="💼"
    )

    st.write("""
    Get:
    - Recommended Roles
    - Match Scores
    - Career Suggestions
    """)

st.divider()

# ==========================================
# PROJECT WORKFLOW
# ==========================================

st.header("⚙️ How It Works")

st.code("""
Resume
    +
Job Description
    ↓
Skill Extraction
    ↓
Skill Gap Analysis
    ↓
Learning Recommendations
    ↓
Job Recommendations
""", language="text")

st.divider()

# ==========================================
# TECH STACK
# ==========================================

st.header("🛠️ Technology Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:
    st.success("Python")

with tech2:
    st.success("MySQL")

with tech3:
    st.success("Machine Learning")

with tech4:
    st.success("Streamlit")

st.divider()

# ==========================================
# FOOTER
# ==========================================

st.caption(
    "Built with Python, SQL, Machine Learning and Streamlit."
)