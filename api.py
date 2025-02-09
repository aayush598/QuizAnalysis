from fastapi import FastAPI
from data_loader import load_json
from analysis import analyze_historical_performance, analyze_quiz_submission, analyze_current_quiz
from insights import get_gemini_insights
import config

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Student Performance API 🚀"}

@app.get("/performance/historical")
def get_historical_performance():
    """Fetch and analyze historical quiz performance."""
    historical_data = load_json(config.HISTORICAL_QUIZ_LINK, from_link=True)
    if not historical_data:
        return {"error": "No historical data found"}
    return analyze_historical_performance(historical_data)

@app.get("/performance/current")
def get_current_quiz_performance():
    """Fetch and analyze the latest quiz."""
    current_quiz_data = load_json(config.CURRENT_QUIZ_LINK, from_file=True)
    if not current_quiz_data:
        return {"error": "No current quiz data found"}
    return analyze_current_quiz(current_quiz_data)

@app.get("/performance/submission")
def get_quiz_submission():
    """Fetch and analyze the most recent quiz submission."""
    submission_data = load_json(config.QUIZ_SUBMISSION_LINK, from_file=True)
    if not submission_data:
        return {"error": "No submission data found"}
    return analyze_quiz_submission(submission_data)

@app.get("/insights/ai")
def generate_ai_insights():
    """Generate AI-powered insights using Google Gemini API."""
    prompt = "Analyze the student's latest quiz and historical performance. Provide improvement strategies."
    insights = get_gemini_insights(prompt)
    if insights:
        return {"insights": insights}
    return {"error": "Failed to generate insights"}