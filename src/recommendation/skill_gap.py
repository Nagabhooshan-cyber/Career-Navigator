from src.skill_extraction.extract_skills import extract_skills

def analyze_skill_gap(
    resume_text,
    market_skills
):

    resume_skills = set(
        extract_skills(resume_text)
    )

    market_skills = set(
        skill.lower()
        for skill in market_skills
    )

    matched_skills = (
        resume_skills &
        market_skills
    )

    missing_skills = (
        market_skills -
        resume_skills
    )

    match_score = 0

    if len(market_skills) > 0:

        match_score = (
            len(matched_skills)
            /
            len(market_skills)
        ) * 100

    return {
        "resume_skills": list(resume_skills),
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills),
        "match_score": round(match_score, 2)
    }