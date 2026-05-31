import pandas as pd
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import OneHotEncoder

from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import (
    train_test_split
)

from sklearn.metrics import (
    mean_absolute_error,
    r2_score
)

# ----------------------------------

df = pd.read_csv(
    "data/processed/clean_ds_salaries.csv"
)

# ----------------------------------

features = [
    "experience_level",
    "employment_type",
    "company_size",
    "remote_ratio"
]

target = "salary_in_usd"

X = df[features]

y = df[target]

# ----------------------------------

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
)

# ----------------------------------

categorical_features = [
    "experience_level",
    "employment_type",
    "company_size"
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(
                handle_unknown="ignore"
            ),
            categorical_features
        )
    ],
    remainder="passthrough"
)

# ----------------------------------

model = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),
        (
            "model",
            RandomForestRegressor(
                n_estimators=200,
                random_state=42
            )
        )
    ]
)

# ----------------------------------

model.fit(
    X_train,
    y_train
)

# ----------------------------------

predictions = model.predict(
    X_test
)

# ----------------------------------

mae = mean_absolute_error(
    y_test,
    predictions
)

r2 = r2_score(
    y_test,
    predictions
)

print("\nModel Performance")
print("-" * 30)

print(
    f"MAE : ${mae:,.2f}"
)

print(
    f"R²  : {r2:.3f}"
)

# ----------------------------------

joblib.dump(
    model,
    "models/salary_model.pkl"
)

print(
    "\nModel Saved Successfully"
)