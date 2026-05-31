import pandas as pd

# ---------------------------
# Data Analyst Dataset
# ---------------------------

analyst = pd.read_csv("data/raw/DataAnalyst.csv")

analyst.drop(columns=["Unnamed: 0"], inplace=True)

analyst.drop_duplicates(inplace=True)

analyst["Company Name"] = analyst["Company Name"].fillna("Unknown")

analyst.to_csv(
    "data/processed/clean_data_analyst.csv",
    index=False
)

print("DataAnalyst cleaned")


# ---------------------------
# Salary Dataset
# ---------------------------

salary = pd.read_csv("data/raw/ds_salaries.csv")

salary.drop(columns=["Unnamed: 0"], inplace=True)

salary.drop_duplicates(inplace=True)

salary.to_csv(
    "data/processed/clean_ds_salaries.csv",
    index=False
)

print("Salary dataset cleaned")