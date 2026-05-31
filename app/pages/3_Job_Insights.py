import streamlit as st
import pandas as pd
import plotly.express as px
from app.utils import local_css
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
st.set_page_config(
    page_title="Career Navigator",
    page_icon="🚀",
    layout="wide"
)

local_css("app/style.css")
# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Job Insights",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

analyst = pd.read_csv(
    "data/processed/clean_data_analyst.csv"
)

salary = pd.read_csv(
    "data/processed/clean_ds_salaries.csv"
)

# ==========================================
# TITLE
# ==========================================

st.title("📊 Job Market Insights Dashboard")

st.markdown("""
Explore hiring trends, salaries, industries,
and job market demand using real-world data.
""")

# ==========================================
# KPI SECTION
# ==========================================

total_jobs = len(analyst)

avg_salary = int(
    salary["salary_in_usd"].mean()
)

top_location = (
    analyst["Location"]
    .value_counts()
    .idxmax()
)

top_job = (
    analyst["Job Title"]
    .value_counts()
    .idxmax()
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📋 Total Jobs",
        f"{total_jobs:,}"
    )

with col2:
    st.metric(
        "💰 Average Salary",
        f"${avg_salary:,}"
    )

with col3:
    st.metric(
        "📍 Top Location",
        top_location
    )

with col4:
    st.metric(
        "💼 Top Job Role",
        top_job
    )

st.divider()

# ==========================================
# TOP LOCATIONS
# ==========================================

st.subheader(
    "📍 Top Hiring Locations"
)

top_locations = (
    analyst["Location"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_locations.columns = [
    "Location",
    "Jobs"
]

fig = px.bar(
    top_locations,
    x="Location",
    y="Jobs",
    title="Top 10 Hiring Locations"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# TOP JOB TITLES
# ==========================================

st.subheader(
    "💼 Most Common Job Titles"
)

top_jobs = (
    analyst["Job Title"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_jobs.columns = [
    "Job Title",
    "Count"
]

fig = px.bar(
    top_jobs,
    x="Job Title",
    y="Count",
    title="Top 10 Job Titles"
)

fig.update_layout(
    xaxis_tickangle=-45
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# TOP INDUSTRIES
# ==========================================

st.subheader(
    "🏭 Top Industries Hiring"
)

top_industries = (
    analyst["Industry"]
    .dropna()
    .value_counts()
    .head(10)
    .reset_index()
)

top_industries.columns = [
    "Industry",
    "Count"
]

fig = px.bar(
    top_industries,
    x="Industry",
    y="Count",
    title="Top Industries Hiring Data Professionals"
)

fig.update_layout(
    xaxis_tickangle=-45
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# SALARY DISTRIBUTION
# ==========================================

st.subheader(
    "💰 Salary Distribution"
)

fig = px.histogram(
    salary,
    x="salary_in_usd",
    nbins=30,
    title="Salary Distribution (USD)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# SALARY BY EXPERIENCE
# ==========================================

st.subheader(
    "📈 Average Salary by Experience Level"
)

experience_map = {
    "EN": "Entry",
    "MI": "Mid",
    "SE": "Senior",
    "EX": "Executive"
}

salary["experience_name"] = (
    salary["experience_level"]
    .map(experience_map)
)

order = [
    "Entry",
    "Mid",
    "Senior",
    "Executive"
]

exp_salary = (
    salary.groupby(
        "experience_name"
    )["salary_in_usd"]
    .mean()
    .reset_index()
)

exp_salary["experience_name"] = pd.Categorical(
    exp_salary["experience_name"],
    categories=order,
    ordered=True
)

exp_salary = exp_salary.sort_values(
    "experience_name"
)

fig = px.bar(
    exp_salary,
    x="experience_name",
    y="salary_in_usd",
    title="Average Salary by Experience"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# REMOTE WORK
# ==========================================

st.subheader(
    "🏠 Remote Work Distribution"
)

remote = (
    salary["remote_ratio"]
    .value_counts()
    .reset_index()
)

remote.columns = [
    "Remote %",
    "Count"
]

fig = px.pie(
    remote,
    names="Remote %",
    values="Count",
    title="Remote Work Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# DATA PREVIEW
# ==========================================

with st.expander(
    "🔍 View Raw Job Data"
):
    st.dataframe(
        analyst.head(20)
    )