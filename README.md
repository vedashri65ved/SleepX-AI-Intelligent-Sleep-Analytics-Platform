#  SleepX AI - Intelligent Sleep Analytics Platform

##  Overview

SleepX AI is a data analytics dashboard developed using Python, Pandas, NumPy, Streamlit, Matplotlib, and Seaborn. The platform analyzes sleep health, lifestyle habits, stress levels, and cognitive performance to provide meaningful insights through interactive visualizations and analytics.

The project demonstrates Data Cleaning, Feature Engineering, Exploratory Data Analysis (EDA), and Dashboard Development using real-world sleep health data.

---

##  Features

### Data Processing

* Data Cleaning using Pandas
* Duplicate Record Removal
* Feature Engineering
* Data Filtering and Segmentation

### Analytics Features

* Sleep Efficiency Calculation
* Lifestyle Risk Score Analysis
* Wellness Score Calculation
* Sleep Category Classification
* Correlation Analysis
* Statistical Insights

### Interactive Dashboard

* Dynamic Sidebar Filters
* KPI Metrics Dashboard
* EDA Visualizations
* Advanced Analytics Section
* Dataset Preview
* Interactive Charts

---

## 🛠️ Technologies Used

| Technology | Purpose                      |
| ---------- | ---------------------------- |
| Python     | Programming Language         |
| Pandas     | Data Manipulation & Analysis |
| NumPy      | Numerical Computation        |
| Streamlit  | Dashboard Development        |
| Matplotlib | Data Visualization           |
| Seaborn    | Statistical Visualization    |

---

## Feature Engineering

### Sleep Efficiency

Measures overall sleep effectiveness using Deep Sleep and REM Sleep percentages.

```python
df["Sleep_Efficiency"] = (
    df["deep_sleep_percentage"] +
    df["rem_percentage"]
) / 2
```

### Lifestyle Risk Score

Evaluates lifestyle-related risks affecting sleep quality.

```python
df["Lifestyle_Risk_Score"] = (
    df["stress_score"] * 0.5 +
    df["screen_time_before_bed_mins"] * 0.02 +
    df["alcohol_units_before_bed"] * 2
)
```

### Wellness Score

Calculates overall wellness based on sleep quality, exercise habits, and cognitive performance.

```python
df["Wellness_Score"] = (
    df["sleep_quality_score"] * 0.4 +
    df["exercise_day"] * 0.3 +
    df["cognitive_performance_score"] * 0.3
)
```

---

##  Dashboard Sections

### 1️. EDA Analysis

* Sleep Quality Distribution
* Stress Score Distribution
* Screen Time Analysis
* Average Sleep Duration by Occupation
* Sleep Disorder Risk Distribution

### 2️. Insights Dashboard

* Stress vs Sleep Quality
* Exercise Impact on Sleep
* Gender-wise Stress Analysis
* Wellness Score by Gender
* Sleep Category Distribution

### 3️.Advanced Analytics

* Correlation Heatmap
* Violin Plot Analysis
* Sleep Quality Trend by Age
* Feature Relationship Pairplot
* Occupation-wise Stress Analysis
* Sleep Quality vs Cognitive Performance

---

##  Key Insights

* Higher stress levels are associated with poor sleep quality.
* Excessive screen time before bed negatively impacts sleep efficiency.
* Regular physical activity improves sleep quality.
* Higher wellness scores indicate healthier lifestyle habits.
* Sleep quality significantly affects cognitive performance.
* Sleep disorders are often linked with increased stress levels.

---

##  Project Objectives

* Analyze sleep health patterns.
* Identify factors affecting sleep quality.
* Evaluate wellness and lifestyle risks.
* Generate actionable insights from sleep data.
* Build an interactive analytics dashboard.

---

## Skills Demonstrated

* Data Cleaning
* Data Visualization
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Dashboard Development
* Statistical Analysis
* Python Programming
* Business Insight Generation

---
