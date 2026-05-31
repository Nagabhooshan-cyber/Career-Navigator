from src.skill_extraction.skills import SKILL_ALIASES


def extract_skills(text):

    if not text:
        return []

    text = str(text).lower()

    found_skills = []

    for skill, aliases in SKILL_ALIASES.items():

        for alias in aliases:

            if alias.lower() in text:

                found_skills.append(skill)
                break

    return sorted(
        list(
            set(found_skills)
        )
    )