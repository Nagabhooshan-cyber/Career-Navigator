import sys
import os
import streamlit as st
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
from app.utils import local_css

st.set_page_config(
    page_title="Career Navigator",
    page_icon="🚀",
    layout="wide"
)

local_css("app/style.css")
# ==========================================
# ADD PROJECT ROOT TO PYTHON PATH
# ==========================================

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

if project_root not in sys.path:
    sys.path.insert(0, project_root)

# ==========================================
# IMPORTS
# ==========================================

import pdfplumber
import pandas as pd

from src.recommendation.skill_gap import analyze_skill_gap
from src.recommendation.job_recommender import recommend_jobs
from src.skill_extraction.extract_skills import extract_skills

# ==========================================
# PAGE TITLE
# ==========================================

st.title("📄 Resume vs Job Description Analyzer")

st.info("""
Upload your resume and paste a Job Description.

The system will:

✅ Extract Resume Skills

✅ Extract Job Description Skills

✅ Calculate Match Score

✅ Identify Missing Skills

✅ Suggest Learning Areas

✅ Recommend Suitable Jobs
""")

# ==========================================
# RESUME UPLOAD
# ==========================================

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# ==========================================
# JOB DESCRIPTION INPUT
# ==========================================

job_description = st.text_area(
    "Paste Job Description",
    height=250
)

# ==========================================
# ANALYZE BUTTON
# ==========================================

if st.button("🚀 Analyze Resume"):

    if uploaded_file is None:

        st.error(
            "Please upload a resume PDF."
        )

    elif not job_description.strip():

        st.error(
            "Please paste a Job Description."
        )

    else:

        # ==================================
        # READ RESUME PDF
        # ==================================

        resume_text = ""

        try:

            with pdfplumber.open(
                uploaded_file
            ) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:
                        resume_text += page_text

        except Exception as e:

            st.error(
                f"Error reading PDF: {e}"
            )

            st.stop()

        # ==================================
        # EXTRACT JD SKILLS
        # ==================================

        jd_skills = extract_skills(
            job_description
        )

        # ==================================
        # ANALYZE SKILL GAP
        # ==================================

        result = analyze_skill_gap(
            resume_text,
            jd_skills
        )

        score = result["match_score"]

        # ==================================
        # MATCH SCORE
        # ==================================

        st.subheader("🎯 Match Score")

        st.progress(
            int(score)
        )

        if score >= 80:

            st.success(
                f"Excellent Match ({score}%)"
            )

        elif score >= 60:

            st.warning(
                f"Good Match ({score}%)"
            )

        else:

            st.error(
                f"Low Match ({score}%)"
            )

        st.divider()

        # ==================================
        # MATCHED & MISSING SKILLS
        # ==================================

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "✅ Matching Skills"
            )

            if result["matched_skills"]:

                for skill in result[
                    "matched_skills"
                ]:

                    st.success(
                        skill.title()
                    )

            else:

                st.warning(
                    "No matching skills found."
                )

        with col2:

            st.subheader(
                "❌ Missing Skills"
            )

            if result["missing_skills"]:

                for skill in result[
                    "missing_skills"
                ]:

                    st.error(
                        skill.title()
                    )

            else:

                st.success(
                    "No missing skills."
                )

        st.divider()

        # ==================================
        # LEARNING RECOMMENDATIONS
        # ==================================

        st.subheader(
            "📚 Learning Recommendations"
        )

        missing_skills = result["missing_skills"]

        if missing_skills:

            for skill in missing_skills:

                st.info(
                    f"Learn {skill.title()}"
                )

        else:

            st.success(
                "No recommendations needed."
            )

        st.divider()

        # ==================================
        # RESUME SKILLS
        # ==================================

        st.subheader(
            "🧠 Skills Detected in Resume"
        )

        if result["resume_skills"]:

            st.write(
                sorted(
                    result[
                        "resume_skills"
                    ]
                )
            )

        else:

            st.warning(
                "No skills detected."
            )

        st.divider()

        # ==================================
        # JOB RECOMMENDATIONS
        # ==================================

        st.subheader(
            "💼 Recommended Jobs"
        )

        jobs_df = pd.read_csv(
            "data/processed/clean_data_analyst.csv"
        )

        recommendations = recommend_jobs(
            resume_text,
            jobs_df
        )

        if recommendations:

            for job in recommendations:

                with st.expander(
                    f"{job['job_title']} ({job['match_score']}%)"
                ):

                    st.write(
                        f"Company: {job['company']}"
                    )

                    st.progress(
                        int(
                            job[
                                "match_score"
                            ]
                        )
                    )

        else:

            st.warning(
                "No suitable jobs found."
            )