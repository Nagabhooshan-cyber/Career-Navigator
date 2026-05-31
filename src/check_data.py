import pandas as pd

print("=" * 50)
print("DATA ANALYST DATASET")
print("=" * 50)

df1 = pd.read_csv("data/raw/DataAnalyst.csv")

print(df1.head())
print("\nColumns:")
print(df1.columns.tolist())

print("\nShape:")
print(df1.shape)

print("\nMissing Values:")
print(df1.isnull().sum())



print("\n\n" + "=" * 50)
print("SALARY DATASET")
print("=" * 50)

df2 = pd.read_csv("data/raw/ds_salaries.csv")

print(df2.head())
print("\nColumns:")
print(df2.columns.tolist())

print("\nShape:")
print(df2.shape)

print("\nMissing Values:")
print(df2.isnull().sum())