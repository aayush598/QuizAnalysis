import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables using os.getenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
CURRENT_QUIZ_FILE = os.getenv("CURRENT_QUIZ_FILE")
HISTORICAL_QUIZ_FILE = os.getenv("HISTORICAL_QUIZ_FILE")
QUIZ_SUBMISSION_FILE = os.getenv("QUIZ_SUBMISSION_FILE")

CURRENT_QUIZ_LINK = os.getenv("CURRENT_QUIZ_LINK")
HISTORICAL_QUIZ_LINK = os.getenv("HISTORICAL_QUIZ_LINK")
QUIZ_SUBMISSION_LINK = os.getenv("QUIZ_SUBMISSION_LINK")
