
# SleepX AI - Ultra Premium Streamlit Dashboard

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(
    page_title="Sleep Health Analysis",
    page_icon="🧠",
    layout="wide"
)

# =========================================================
# LOAD CSS
# =========================================================

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

local_css("style.css")

# =========================================================
# LOAD DATA
# =========================================================

df = pd.read_csv("sleep.csv")

# =========================================================
# DATA CLEANING
# =========================================================

df.drop_duplicates(inplace=True)

# =========================================================
# FEATURE ENGINEERING
# =========================================================

# Sleep Efficiency

df["Sleep_Efficiency"] = (
    df["deep_sleep_percentage"] +
    df["rem_percentage"]
) / 2

# Lifestyle Risk Score

df["Lifestyle_Risk_Score"] = (
    df["stress_score"] * 0.5 +
    df["screen_time_before_bed_mins"] * 0.02 +
    df["alcohol_units_before_bed"] * 2
)

# Wellness Score

df["Wellness_Score"] = (
    df["sleep_quality_score"] * 0.4 +
    df["exercise_day"] * 0.3 +
    df["cognitive_performance_score"] * 0.3
)

# Sleep Category

conditions = [
    df["sleep_quality_score"] >= 8,

    (df["sleep_quality_score"] >= 5) &
    (df["sleep_quality_score"] < 8),

    df["sleep_quality_score"] < 5
]

choices = [
    "Excellent",
    "Average",
    "Poor"
]

df["Sleep_Category"] = np.select(
    conditions,
    choices,
    default="Unknown"
)

# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.title(" Dashboard Filters")

gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["gender"].unique(),
    default=df["gender"].unique()
)

occupation = st.sidebar.multiselect(
    "Select Occupation",
    options=df["occupation"].unique(),
    default=df["occupation"].unique()
)

sleep_category = st.sidebar.multiselect(
    "Select Sleep Category",
    options=df["Sleep_Category"].unique(),
    default=df["Sleep_Category"].unique()
)

# =========================================================
# FILTER DATA
# =========================================================

filtered_df = df[
    (df["gender"].isin(gender)) &
    (df["occupation"].isin(occupation)) &
    (df["Sleep_Category"].isin(sleep_category))
]

# =========================================================
# TITLE
# =========================================================

st.title("Sleep health Analysis")

st.markdown("""
## Smart Sleep & Lifestyle Analytics Platform

Analyze:
- Sleep Quality
- Stress Levels
- Wellness Scores
- Lifestyle Risks
- Cognitive Performance

using powerful data analytics and visualization.
""")

# =========================================================
# KPI CARDS
# =========================================================

st.subheader(" Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    " Avg Sleep Duration",
    round(filtered_df["sleep_duration_hrs"].mean(), 2)
)

col2.metric(
    " Avg Stress Score",
    round(filtered_df["stress_score"].mean(), 2)
)

col3.metric(
    " Avg Cognitive Score",
    round(filtered_df["cognitive_performance_score"].mean(), 2)
)

col4.metric(
    " Avg Wellness Score",
    round(filtered_df["Wellness_Score"].mean(), 2)
)

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3 = st.tabs([
    " EDA Analysis",
    " Insights",
    " Advanced Analytics"
])

# =========================================================
# TAB 1 - EDA
# =========================================================

with tab1:

    # =====================================================
    # SLEEP QUALITY DISTRIBUTION
    # =====================================================

    st.subheader(" Sleep Quality Distribution")

    fig1, ax1 = plt.subplots(figsize=(10,5))

    sns.histplot(
        filtered_df["sleep_quality_score"],
        bins=20,
        kde=True,
        color="skyblue",
        ax=ax1
    )

    ax1.set_title("Distribution of Sleep Quality Scores")

    st.pyplot(fig1)

    # =====================================================
    # STRESS DISTRIBUTION
    # =====================================================

    st.subheader(" Stress Score Distribution")

    fig2, ax2 = plt.subplots(figsize=(10,5))

    sns.histplot(
        filtered_df["stress_score"],
        bins=20,
        kde=True,
        color="red",
        ax=ax2
    )

    ax2.set_title("Stress Score Distribution")

    st.pyplot(fig2)

    # =====================================================
    # SCREEN TIME DISTRIBUTION
    # =====================================================

    st.subheader(" Screen Time Before Bed")

    fig3, ax3 = plt.subplots(figsize=(12,6))

    sns.histplot(
        filtered_df["screen_time_before_bed_mins"],
        bins=30,
        kde=True,
        color="purple",
        ax=ax3
    )

    ax3.set_title("Screen Time Before Bed Analysis")

    st.pyplot(fig3)

    # =====================================================
    # BAR CHART
    # =====================================================

    st.subheader(" Average Sleep Duration by Occupation")

    fig4, ax4 = plt.subplots(figsize=(15,6))

    avg_sleep = filtered_df.groupby("occupation")[
        "sleep_duration_hrs"
    ].mean().sort_values()

    avg_sleep.plot(
        kind="bar",
        ax=ax4
    )

    ax4.set_title("Average Sleep Duration by Occupation")

    plt.xticks(rotation=45)

    st.pyplot(fig4)

    # =====================================================
    # PIE CHART
    # =====================================================

    st.subheader("Sleep Disorder Risk Percentage")

    risk_counts = filtered_df["sleep_disorder_risk"].value_counts()

    fig5, ax5 = plt.subplots(figsize=(8,8))

    ax5.pie(
        risk_counts,
        labels=risk_counts.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax5.set_title("Sleep Disorder Risk Distribution")

    st.pyplot(fig5)

# =========================================================
# TAB 2 - INSIGHTS
# =========================================================

with tab2:

    # =====================================================
    # STRESS VS SLEEP QUALITY
    # =====================================================

    st.subheader(" Stress vs Sleep Quality")

    fig6, ax6 = plt.subplots(figsize=(10,6))

    sns.scatterplot(
        x="stress_score",
        y="sleep_quality_score",
        hue="gender",
        data=filtered_df,
        ax=ax6
    )

    ax6.set_title("Stress vs Sleep Quality")

    st.pyplot(fig6)

    # =====================================================
    # EXERCISE VS SLEEP QUALITY
    # =====================================================

    st.subheader("Physical Activity vs Sleep Quality")

    # Average sleep quality by exercise
    exercise_sleep = filtered_df.groupby(
        "exercise_day"
    )["sleep_quality_score"].mean()

    # Create figure
    fig7, ax7 = plt.subplots(figsize=(10,6))

    # Line chart
    exercise_sleep.plot(
        kind="line",marker="o",linewidth=3,markersize=10,ax=ax7
    )

    # Custom labels
    ax7.set_xticks([0, 1])
    ax7.set_xticklabels(["No Exercise", "Exercise"])

    # Titles
    ax7.set_title("Exercise Impact on Sleep")

    ax7.set_xlabel("Exercise Habit")
    ax7.set_ylabel("Average Sleep Quality Score")

    # Grid
    ax7.grid(True)

    # Show chart
    st.pyplot(fig7)

    # =====================================================
    # GENDER WISE STRESS
    # =====================================================

    st.subheader(" Gender Wise Stress Levels")

    fig8, ax8 = plt.subplots(figsize=(8,5))

    sns.boxplot(
        x="gender",
        y="stress_score",
        data=filtered_df,
        palette="Set2",
        ax=ax8
    )

    ax8.set_title("Stress Distribution by Gender")

    st.pyplot(fig8)

    # =====================================================
    # BAR CHART - WELLNESS SCORE
    # =====================================================

    st.subheader("Wellness Score by Gender")

    fig9, ax9 = plt.subplots(figsize=(8,5))

    sns.barplot(
        x="gender",
        y="Wellness_Score",
        data=filtered_df,
        palette="coolwarm",
        ax=ax9
    )

    ax9.set_title("Average Wellness Score by Gender")

    st.pyplot(fig9)

    # =====================================================
    # COUNT PLOT
    # =====================================================

    st.subheader(" Sleep Category Count")

    fig10, ax10 = plt.subplots(figsize=(8,5))

    sns.countplot(
        x="Sleep_Category",
        data=filtered_df,
        palette="viridis",
        ax=ax10
    )

    ax10.set_title("Sleep Category Distribution")

    st.pyplot(fig10)

# =========================================================
# TAB 3 - ADVANCED ANALYTICS
# =========================================================

with tab3:

    # =====================================================
    # CORRELATION HEATMAP
    # =====================================================

    st.subheader(" Correlation Heatmap")

    fig11, ax11 = plt.subplots(figsize=(14,8))

    corr = filtered_df.select_dtypes(include=np.number).corr()

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        linewidths=0.5,
        ax=ax11
    )

    ax11.set_title("Feature Correlation Matrix")

    st.pyplot(fig11)

    # =====================================================
    # VIOLIN PLOT
    # =====================================================

    st.subheader(" Stress Density by Sleep Disorder Risk")

    fig12, ax12 = plt.subplots(figsize=(12,6))

    sns.violinplot(
        x="sleep_disorder_risk",
        y="stress_score",
        data=filtered_df,
        palette="magma",
        ax=ax12
    )

    ax12.set_title("Stress Density Across Sleep Disorder Risk")

    st.pyplot(fig12)

    # =====================================================
    # LINE CHART
    # =====================================================

    st.subheader("Sleep Quality Trend with Age")

    age_sleep = filtered_df.groupby("age")[
        "sleep_quality_score"
    ].mean()

    fig13, ax13 = plt.subplots(figsize=(12,5))

    age_sleep.plot(
        kind="line",
        marker="o",
        ax=ax13
    )

    ax13.set_title("Sleep Quality Trend by Age")

    st.pyplot(fig13)

    # =====================================================
    # PAIRPLOT
    # =====================================================

    st.subheader(" Feature Relationship Analysis")

    selected_cols = filtered_df[
        [
            "sleep_quality_score",
            "stress_score",
            "exercise_day",
            "Wellness_Score"
        ]
    ]

    pairplot = sns.pairplot(selected_cols)

    st.pyplot(pairplot)

    # =====================================================
    # BOXPLOT
    # =====================================================

    st.subheader(" Stress Distribution Across Sleep Disorder Risk")

    fig14, ax14 = plt.subplots(figsize=(12,6))

    sns.boxplot(
        x="sleep_disorder_risk",
        y="stress_score",
        data=filtered_df,
        palette="Set2",
        ax=ax14
    )

    ax14.set_title("Stress Distribution Across Sleep Disorder Risk")

    st.pyplot(fig14)

    # =====================================================
    # OCCUPATION VS STRESS
    # =====================================================

    st.subheader("Occupation Wise Stress Analysis")

    occupation_stress = filtered_df.groupby(
        "occupation"
    )["stress_score"].mean().sort_values(ascending=False)

    fig15, ax15 = plt.subplots(figsize=(14,6))

    occupation_stress.plot(kind="bar",
    color="red",
    ax=ax15)

    ax15.set_title("Average Stress Score by Occupation")

    ax15.set_xlabel("Occupation")
    ax15.set_ylabel("Average Stress Score")

    plt.xticks(rotation=45)

    st.pyplot(fig15)



    # =====================================================
    # SLEEP VS COGNITIVE PERFORMANCE
    # =====================================================

    st.subheader("Sleep Quality vs Cognitive Performance")

    fig16, ax16 = plt.subplots(figsize=(10,6))

    sns.scatterplot(
        x="sleep_quality_score",y="cognitive_performance_score",hue="gender",data=filtered_df,
        ax=ax16
    )

    ax16.set_title("Impact of Sleep Quality on Brain Performance")

    st.pyplot(fig16)
# =========================================================
# DATASET PREVIEW
# =========================================================

st.subheader("Dataset Preview")

st.dataframe(filtered_df.head(20))

# =========================================================
# INSIGHTS SECTION
# =========================================================

st.subheader(" Key Insights")

st.markdown("""
 Higher stress levels are associated with poor sleep quality.

 Excessive screen time before bed negatively impacts sleep efficiency.

Physically active users generally experience better sleep quality.

 Severe sleep disorder groups show consistently high stress levels.

 Wellness scores improve with better lifestyle habits.

 Sleep quality tends to decline with increasing stress and poor routines.
""")

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown("""
### Developed Using:
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit

###  SleepX AI — Intelligent Sleep Analytics Platform
""")