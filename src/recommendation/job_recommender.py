import pandas as pd

from src.skill_extraction.extract_skills import (
    extract_skills
)

def recommend_jobs(
    resume_text,
    jobs_df,
    top_n=5
):

    resume_skills = set(
        extract_skills(resume_text)
    )

    recommendations = []

    for _, row in jobs_df.iterrows():

        jd_skills = set(
            extract_skills(
                row["Job Description"]
            )
        )

        if len(jd_skills) == 0:
            continue

        score = (
            len(
                resume_skills &
                jd_skills
            )
            /
            len(jd_skills)
        ) * 100

        recommendations.append({
            "job_title":
                row["Job Title"],

            "company":
                row["Company Name"],

            "match_score":
                round(score, 2)
        })

    recommendations = sorted(
        recommendations,
        key=lambda x:
        x["match_score"],
        reverse=True
    )

    return recommendations[:top_n]