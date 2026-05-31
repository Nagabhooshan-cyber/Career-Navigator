import pandas as pd
import joblib

model = joblib.load(
    "models/salary_model.pkl"
)

sample = pd.DataFrame({
    "experience_level": ["SE"],
    "employment_type": ["FT"],
    "company_size": ["L"],
    "remote_ratio": [100]
})

prediction = model.predict(
    sample
)

print(
    f"Predicted Salary: ${prediction[0]:,.2f}"
)