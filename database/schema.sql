-- =====================================
-- CAREER NAVIGATOR DATABASE SCHEMA
-- =====================================

CREATE DATABASE IF NOT EXISTS career_navigator;

USE career_navigator;

-- =====================================
-- ANALYST JOBS TABLE
-- =====================================

DROP TABLE IF EXISTS analyst_jobs;

CREATE TABLE analyst_jobs (
    id INT AUTO_INCREMENT PRIMARY KEY,

    job_title VARCHAR(255),
    salary_estimate VARCHAR(255),

    job_description LONGTEXT,

    company_name VARCHAR(255),

    location VARCHAR(255),

    industry VARCHAR(255),

    sector VARCHAR(255),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- SALARY JOBS TABLE
-- =====================================

DROP TABLE IF EXISTS salary_jobs;

CREATE TABLE salary_jobs (
    id INT AUTO_INCREMENT PRIMARY KEY,

    work_year INT,

    experience_level VARCHAR(10),

    employment_type VARCHAR(10),

    job_title VARCHAR(255),

    salary_usd FLOAT,

    remote_ratio INT,

    company_location VARCHAR(20),

    company_size VARCHAR(10),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- SKILLS TABLE
-- =====================================

DROP TABLE IF EXISTS skills;

CREATE TABLE skills (
    skill_id INT AUTO_INCREMENT PRIMARY KEY,

    skill_name VARCHAR(100) UNIQUE
);

-- =====================================
-- JOB SKILLS TABLE
-- =====================================

DROP TABLE IF EXISTS job_skills;

CREATE TABLE job_skills (
    id INT AUTO_INCREMENT PRIMARY KEY,

    job_id INT,

    skill_id INT,

    FOREIGN KEY (job_id)
        REFERENCES analyst_jobs(id)
        ON DELETE CASCADE,

    FOREIGN KEY (skill_id)
        REFERENCES skills(skill_id)
        ON DELETE CASCADE
);

-- =====================================
-- RESUME ANALYSIS TABLE
-- =====================================

DROP TABLE IF EXISTS resume_analysis;

CREATE TABLE resume_analysis (
    analysis_id INT AUTO_INCREMENT PRIMARY KEY,

    resume_name VARCHAR(255),

    detected_skills TEXT,

    missing_skills TEXT,

    match_score FLOAT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- USEFUL INDEXES
-- =====================================

CREATE INDEX idx_job_title
ON analyst_jobs(job_title);

CREATE INDEX idx_location
ON analyst_jobs(location);

CREATE INDEX idx_company
ON analyst_jobs(company_name);

CREATE INDEX idx_salary_job_title
ON salary_jobs(job_title);

CREATE INDEX idx_company_location
ON salary_jobs(company_location);