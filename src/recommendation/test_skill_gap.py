from skill_gap import analyze_skill_gap

resume_text = """
I have experience in Python,
SQL, Pandas and Excel.
"""

market_skills = [
    "Python",
    "SQL",
    "Excel",
    "Power BI",
    "Tableau",
    "AWS"
]

result = analyze_skill_gap(
    resume_text,
    market_skills
)

print(result)