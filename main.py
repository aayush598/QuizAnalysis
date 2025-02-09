import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_loader import load_json
from analysis import analyze_historical_performance
from insights import get_gemini_insights
import config

# Load data
historical_data = load_json(config.HISTORICAL_QUIZ_LINK,from_link=True)

# Analyze student performance
performance = analyze_historical_performance(historical_data)

# Streamlit UI
st.set_page_config(page_title="Student Performance Analysis", layout="wide")

st.title("📊 Student Performance Dashboard")

# Overall performance summary
st.subheader("📌 Performance Overview")
st.write(f"**Overall Accuracy:** {performance['overall_accuracy']:.2f}%")

# Topic-wise performance
st.subheader("📌 Topic Performance")
df_topics = pd.DataFrame.from_dict(performance["topic_performance"], orient="index")
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
    prompt = f"Analyze the following student performance data: {performance}. Provide personalized recommendations for improvement."
    # Show loading spinner while waiting for API response
    with st.spinner("Generating AI Insights... Please wait ⏳"):
        ai_insights = get_gemini_insights(prompt)

    # Display AI insights
    st.write(ai_insights)
