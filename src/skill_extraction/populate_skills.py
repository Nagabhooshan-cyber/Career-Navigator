import os
import pandas as pd

from dotenv import load_dotenv
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from extract_skills import extract_skills
from skills import SKILLS

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")



encoded_password = quote_plus(DB_PASSWORD)

engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


print("Reading jobs...")

jobs = pd.read_sql(
    """
    SELECT id,
           job_description
    FROM analyst_jobs
    """,
    engine
)

all_skills = set()

job_skill_rows = []

for _, row in jobs.iterrows():

    job_id = row["id"]

    skills_found = extract_skills(
        row["job_description"]
    )

    for skill in skills_found:

        all_skills.add(skill)

        job_skill_rows.append(
            {
                "job_id": job_id,
                "skill_name": skill
            }
        )

print(f"Found {len(all_skills)} unique skills")

# --------------------
# skills table
# --------------------

skills_df = pd.DataFrame(
    {"skill_name": sorted(all_skills)}
)

skills_df.to_sql(
    "skills",
    engine,
    if_exists="append",
    index=False
)

print("Skills table populated")

# --------------------
# mapping
# --------------------

skill_lookup = pd.read_sql(
    """
    SELECT skill_id,
           skill_name
    FROM skills
    """,
    engine
)

mapping = dict(
    zip(
        skill_lookup["skill_name"],
        skill_lookup["skill_id"]
    )
)

job_skills_df = pd.DataFrame(
    job_skill_rows
)

job_skills_df["skill_id"] = (
    job_skills_df["skill_name"]
    .map(mapping)
)

job_skills_df = job_skills_df[
    [
        "job_id",
        "skill_id"
    ]
]

job_skills_df.to_sql(
    "job_skills",
    engine,
    if_exists="append",
    index=False
)

print("job_skills populated")

print("DONE")