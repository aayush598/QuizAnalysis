from utils import calculate_percentage

def analyze_quiz_submission(data):
    """Analyze the most recent quiz submission."""
    if not data:
        return {}

    return {
        "topic": data["quiz"]["topic"],
        "score": data["score"],
        "accuracy": float(data["accuracy"].strip(" %")),
        "correct_answers": data["correct_answers"],
        "incorrect_answers": data["incorrect_answers"],
    }

def analyze_current_quiz(data):
    """Analyze the latest quiz attempt."""
    if not data or "quiz" not in data or "questions" not in data["quiz"]:
        return {}

    total_questions = len(data["quiz"]["questions"])
    
    # Fix: Iterate through options list to find correct ones
    correct_count = sum(
        1 for q in data["quiz"]["questions"]
        if any(option["is_correct"] for option in q["options"])
    )
    
    accuracy = calculate_percentage(correct_count, total_questions)

    return {
        "topic": data["quiz"]["topic"],
        "total_questions": total_questions,
        "correct_count": correct_count,
        "accuracy": accuracy,
    }
def analyze_historical_performance(data):
    """Analyze past quiz trends to identify strengths & weaknesses."""
    if not data:
        return {}

    topic_performance = {}
    overall_accuracy = []

    for quiz in data:
        topic = quiz["quiz"]["topic"]
        accuracy = float(quiz["accuracy"].strip(" %"))
        
        overall_accuracy.append(accuracy)

        if topic not in topic_performance:
            topic_performance[topic] = {"attempts": 0, "total_accuracy": 0}

        topic_performance[topic]["attempts"] += 1
        topic_performance[topic]["total_accuracy"] += accuracy

    for topic, stats in topic_performance.items():
        stats["avg_accuracy"] = round(stats["total_accuracy"] / stats["attempts"], 2)

    return {
        "overall_accuracy": round(sum(overall_accuracy) / len(overall_accuracy), 2),
        "topic_performance": topic_performance
    }
