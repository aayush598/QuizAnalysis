import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_loader import load_json
from analysis import analyze_historical_performance, analyze_quiz_submission, analyze_current_quiz
from insights import get_gemini_insights
import config



# Load all three datasets
historical_data = load_json(config.HISTORICAL_QUIZ_LINK, from_link=True)
quiz_submission = load_json(config.QUIZ_SUBMISSION_LINK, from_link=True)
current_quiz = load_json(config.CURRENT_QUIZ_LINK, from_link=True)

# Analyze data
historical_analysis = analyze_historical_performance(historical_data)
submission_analysis = analyze_quiz_submission(quiz_submission)
current_quiz_analysis = analyze_current_quiz(current_quiz)

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

# Visualization
st.subheader("📊 Accuracy Trend")

fig, ax = plt.subplots(figsize=(5, 3))  # Reduce the figure size
sns.lineplot(
    x=range(1, len(historical_data) + 1),
    y=[float(q["accuracy"].strip(" %")) for q in historical_data],
    marker="o",
    linestyle="-",
    color="blue"
)
ax.set_xlabel("Quiz Attempt", fontsize=10)
ax.set_ylabel("Accuracy (%)", fontsize=10)
ax.set_title("Accuracy Trend Over Time", fontsize=12)
ax.tick_params(axis='both', labelsize=8)

st.pyplot(fig, use_container_width=False)  # Prevent auto-scaling

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