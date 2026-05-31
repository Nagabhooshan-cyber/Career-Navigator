import streamlit as st
import pandas as pd
import sys
import os

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

if project_root not in sys.path:
    sys.path.insert(0, project_root)

from app.utils import local_css
import joblib
from app.utils import local_css

st.set_page_config(
    page_title="Career Navigator",
    page_icon="🚀",
    layout="wide"
)

local_css("app/style.css")
# ==========================================
# PAGE CONFIG
# ==========================================

st.title("💰 Salary Predictor")

st.info("""
This salary predictor is trained on real Data Science job salary data.

Factors considered:
• Experience Level
• Job Type
• Company Size
• Work From Home Percentage

The prediction represents the estimated annual salary in USD.
""")

# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load(
    "models/salary_model.pkl"
)

# ==========================================
# USER FRIENDLY MAPPINGS
# ==========================================

experience_display = {
    "Entry Level (0-2 Years)": "EN",
    "Mid Level (2-5 Years)": "MI",
    "Senior Level (5-10 Years)": "SE",
    "Executive / Director": "EX"
}

employment_display = {
    "Full Time": "FT",
    "Part Time": "PT",
    "Contract": "CT",
    "Freelance": "FL"
}

company_size_display = {
    "Small Company (< 50 Employees)": "S",
    "Medium Company (50-250 Employees)": "M",
    "Large Company (250+ Employees)": "L"
}

# ==========================================
# INPUTS
# ==========================================

experience_label = st.selectbox(
    "👨‍💻 Your Experience",
    list(experience_display.keys()),
    help="Select your current experience level."
)

employment_label = st.selectbox(
    "💼 Job Type",
    list(employment_display.keys()),
    help="Select the type of employment."
)

company_size_label = st.selectbox(
    "🏢 Target Company Size",
    list(company_size_display.keys()),
    help="Choose the approximate size of the company."
)

remote_ratio = st.slider(
    "🏠 Work From Home Percentage",
    min_value=0,
    max_value=100,
    value=100,
    help="""
0 = Fully On-site

50 = Hybrid

100 = Fully Remote
"""
)

# ==========================================
# CONVERT TO MODEL VALUES
# ==========================================

experience = experience_display[
    experience_label
]

employment = employment_display[
    employment_label
]

company_size = company_size_display[
    company_size_label
]

# ==========================================
# PREDICT BUTTON
# ==========================================

if st.button(
    "🚀 Predict Salary",
    use_container_width=True
):

    sample = pd.DataFrame({
        "experience_level": [experience],
        "employment_type": [employment],
        "company_size": [company_size],
        "remote_ratio": [remote_ratio]
    })

    prediction = model.predict(
        sample
    )[0]

    st.success(
        f"💵 Estimated Salary: ${prediction:,.0f} per year"
    )

    st.markdown("---")

    st.subheader("Prediction Summary")

    st.write(
        f"**Experience Level:** {experience_label}"
    )

    st.write(
        f"**Employment Type:** {employment_label}"
    )

    st.write(
        f"**Company Size:** {company_size_label}"
    )

    st.write(
        f"**Work From Home:** {remote_ratio}%"
    )

    st.write(
        f"**Predicted Annual Salary:** ${prediction:,.0f}"
    )

# ==========================================
# EXPLANATION
# ==========================================

with st.expander(
    "ℹ️ What do these terms mean?"
):

    st.markdown("""
### Experience Levels

- **Entry Level (EN)** → 0-2 years
- **Mid Level (MI)** → 2-5 years
- **Senior Level (SE)** → 5-10 years
- **Executive (EX)** → Director, Head, VP

### Employment Types

- **Full Time** → Permanent role
- **Part Time** → Reduced working hours
- **Contract** → Fixed-term project work
- **Freelance** → Independent contractor

### Company Size

- **Small** → Less than 50 employees
- **Medium** → 50-250 employees
- **Large** → More than 250 employees

### Work From Home %

- **0%** → Fully office-based
- **50%** → Hybrid
- **100%** → Fully remote
""")