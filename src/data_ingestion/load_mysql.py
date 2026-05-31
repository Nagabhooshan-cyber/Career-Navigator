import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from urllib.parse import quote_plus

# =====================================
# LOAD ENV VARIABLES
# =====================================

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")

# =====================================
# DATABASE CONNECTION
# =====================================

encoded_password = quote_plus(DB_PASSWORD)

engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# =====================================
# LOAD DATA ANALYST DATASET
# =====================================

print("\nLoading DataAnalyst dataset...")

analyst = pd.read_csv(
    "data/processed/clean_data_analyst.csv"
)

analyst = analyst[
    [
        "Job Title",
        "Salary Estimate",
        "Job Description",
        "Company Name",
        "Location",
        "Industry",
        "Sector"
    ]
]

analyst.columns = [
    "job_title",
    "salary_estimate",
    "job_description",
    "company_name",
    "location",
    "industry",
    "sector"
]

analyst.to_sql(
    "analyst_jobs",
    engine,
    if_exists="append",
    index=False
)

print(f"Loaded {len(analyst)} rows into analyst_jobs")

# =====================================
# LOAD SALARY DATASET
# =====================================

print("\nLoading ds_salaries dataset...")

salary = pd.read_csv(
    "data/processed/clean_ds_salaries.csv"
)

salary = salary[
    [
        "work_year",
        "experience_level",
        "employment_type",
        "job_title",
        "salary_in_usd",
        "remote_ratio",
        "company_location",
        "company_size"
    ]
]

salary.columns = [
    "work_year",
    "experience_level",
    "employment_type",
    "job_title",
    "salary_usd",
    "remote_ratio",
    "company_location",
    "company_size"
]

salary.to_sql(
    "salary_jobs",
    engine,
    if_exists="append",
    index=False
)

print(f"Loaded {len(salary)} rows into salary_jobs")

# =====================================
# VERIFY COUNTS
# =====================================

with engine.connect() as conn:

    analyst_count = conn.execute(
        text("SELECT COUNT(*) FROM analyst_jobs")
    ).scalar()

    salary_count = conn.execute(
        text("SELECT COUNT(*) FROM salary_jobs")
    ).scalar()

print("\n=====================================")
print("LOAD COMPLETED")
print("=====================================")

print(f"analyst_jobs rows : {analyst_count}")
print(f"salary_jobs rows  : {salary_count}")