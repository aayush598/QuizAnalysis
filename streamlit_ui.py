import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_loader import load_json
from analysis import analyze_historical_performance, analyze_quiz_submission, analyze_current_quiz
from insights import get_gemini_insights
import config
import requests

# FastAPI Base URL (Change to your Render API URL after deployment)
API_BASE_URL = "https://quizanalysis.onrender.com/"


# Analyze data
historical_analysis = requests.get(f"{API_BASE_URL}/performance/historical").json()
submission_analysis = requests.get(f"{API_BASE_URL}/performance/submission").json()
current_quiz_analysis = requests.get(f"{API_BASE_URL}/performance/current").json()

# Streamlit UI
st.set_page_config(page_title="Student Performance Analysis", layout="wide")

st.title("📊 Student Performance Dashboard")

st.subheader("🔹 Latest Quiz Performance")
st.write(f"**Topic:** {submission_analysis.get('topic', 'N/A')}")
st.write(f"**Score:** {submission_analysis.get('score', 0)}")
st.write(f"**Accuracy:** {submission_analysis.get('accuracy', 0)}%")

st.subheader("🔹 Historical Performance Summary")
st.write(f"**Overall Accuracy:** {historical_analysis['overall_accuracy']}%")

st.subheader("🔹 Comparison with Current Quiz")
st.write(f"**Latest Quiz Accuracy:** {current_quiz_analysis['accuracy']}%")
st.write(f"**Total Questions:** {current_quiz_analysis['total_questions']}")
st.write(f"**Correctly Answered:** {current_quiz_analysis['correct_count']}")

# Topic-wise performance
st.subheader("🔹 Topic Performance")
df_topics = pd.DataFrame.from_dict(historical_analysis["topic_performance"], orient="index")
df_topics = df_topics.rename(columns={"avg_accuracy": "Accuracy (%)", "attempts": "Attempts"})
st.dataframe(df_topics)

# AI-Powered Insights
st.subheader("🤖 AI-Powered Insights & Recommendations")
if st.button("Generate Insights with AI"):
    prompt = (
        f"Analyze the student's performance. "
        f"Latest Quiz: {current_quiz_analysis}. "
        f"Past Performance: {historical_analysis}. "
        f"Submission Data: {submission_analysis}. "
        f"Provide personalized study recommendations."
    )
    with st.spinner("Generating AI Insights... Please wait ⏳"):
        ai_insights = get_gemini_insights(prompt)

    st.write(ai_insights)