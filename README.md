# 🚀 Data Science Career Navigator

An end-to-end Data Science Career Guidance Platform built using Python, MySQL, Machine Learning, NLP, and Streamlit.

This project helps aspiring Data Analysts and Data Scientists:

* Understand job market trends
* Analyze salary expectations
* Identify skill gaps
* Compare resumes against job descriptions
* Discover suitable job opportunities

---

# 📌 Features

## 📊 Job Market Insights Dashboard

Analyze real-world job market trends using Data Analyst job postings.

### Insights Included

* Top Hiring Locations
* Most Common Job Titles
* Top Industries Hiring
* Salary Distribution
* Salary by Experience Level
* Remote Work Trends

---

## 💰 Salary Predictor

Machine Learning model that predicts annual salary based on:

* Experience Level
* Employment Type
* Company Size
* Remote Work Percentage

### Output

Estimated Salary in USD.

---

## 📄 Resume vs Job Description Analyzer

Upload your resume and compare it against a target job description.

### Features

* Resume Skill Extraction
* Job Description Skill Extraction
* Skill Matching
* Match Score Calculation
* Missing Skill Detection

---

## 🎯 Skill Gap Analysis

Identify skills required by the target job that are missing from your resume.

### Example

Required Skills:

* Python
* SQL
* Power BI
* Tableau

Resume Skills:

* Python
* SQL

Missing Skills:

* Power BI
* Tableau

---

## 📚 Learning Recommendations

Get personalized recommendations based on missing skills.

Example:

* Learn Power BI Dashboards
* Learn Tableau Visualization
* Learn AWS Fundamentals

---

## 💼 Job Recommendation Engine

Recommends suitable jobs based on skills extracted from your resume.

### Output

* Recommended Job Roles
* Company Names
* Match Percentages

---

# 🛠️ Tech Stack

## Programming

* Python

## Data Analysis

* Pandas
* NumPy

## Database

* MySQL
* SQLAlchemy

## Machine Learning

* Scikit-Learn
* Joblib

## NLP & Skill Matching

* Custom Skill Extraction Engine
* Skill Alias Matching

## Visualization

* Plotly

## Frontend

* Streamlit

## Development

* VS Code
* Git
* GitHub

---

# 🗄️ Database Design

## analyst_jobs

Stores job posting information.

| Column          |
| --------------- |
| job_id          |
| job_title       |
| salary_estimate |
| job_description |
| company_name    |
| location        |
| industry        |
| sector          |

---

## salary_jobs

Stores salary data.

| Column           |
| ---------------- |
| salary_id        |
| work_year        |
| experience_level |
| employment_type  |
| job_title        |
| salary_usd       |
| remote_ratio     |
| company_location |
| company_size     |

---

## skills

Stores unique extracted skills.

| Column     |
| ---------- |
| skill_id   |
| skill_name |

---

## job_skills

Maps jobs to skills.

| Column   |
| -------- |
| job_id   |
| skill_id |

---

# 📂 Project Structure

```text
career-navigator/
│
├── app/
│   │
│   ├── pages/
│   │   ├── 1_Skill_Gap.py
│   │   ├── 2_Salary_Predictor.py
│   │   └── 3_Job_Insights.py
│   │
│   ├── __init__.py
│   ├── Home.py
│   ├── style.css
│   └── utils.py
│
├── data/
│   │
│   ├── processed/
│   │   ├── clean_data_analyst.csv
│   │   └── clean_ds_salaries.csv
│   │
│   └── raw/
│       ├── DataAnalyst.csv
│       └── ds_salaries.csv
│
├── database/
│   ├── mysql_connection.py
│   └── schema.sql
│
├── models/
│   └── salary_model.pkl
│
├── notebooks/
│   └── eda.ipynb
│
├── src/
│   │
│   ├── data_ingestion/
│   │   └── load_mysql.py
│   │
│   ├── ml/
│   │   ├── predict_salary.py
│   │   └── train_salary_model.py
│   │
│   ├── preprocessing/
│   │   └── clean_data.py
│   │
│   ├── recommendation/
│   │   ├── job_recommender.py
│   │   ├── skill_gap.py
│   │   └── test_skill_gap.py
│   │
│   ├── skill_extraction/
│   │   ├── extract_skills.py
│   │   ├── populate_skills.py
│   │   └── skills.py
│   │
│   ├── __init__.py
│   └── check_data.py
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/your-username/career-navigator.git

cd career-navigator
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create:

```text
.env
```

Example:

```env
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_NAME=career_navigator
DB_PORT=port_number
```

---

## Run Streamlit Application

```bash
streamlit run app/Home.py
```

---

# 📈 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Model Training
5. Salary Prediction
6. Model Serialization using Joblib

---

# 🔍 Resume Analysis Workflow

```text
Resume
     +
Job Description
     ↓
Skill Extraction
     ↓
Skill Matching
     ↓
Gap Analysis
     ↓
Learning Recommendations
     ↓
Job Recommendations
```

---

# 📊 Datasets Used

### Data Analyst Job Listings

Contains:

* Job Titles
* Companies
* Industries
* Locations
* Salary Estimates
* Job Descriptions

### Data Science Salaries

Contains:

* Experience Level
* Employment Type
* Company Size
* Salary Information
* Remote Work Information

---

# 🚀 Future Enhancements

* Resume Parsing using NLP Models
* DOCX Resume Support
* GPT-powered Resume Feedback
* Course Recommendations
* Interview Question Generator
* Real-Time Job Scraping
* Cloud Deployment (AWS / Azure)

---

# 👨‍💻 Author

### Nagabhooshan



