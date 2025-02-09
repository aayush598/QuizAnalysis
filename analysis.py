def analyze_historical_performance(data):
    """Analyze historical quiz trends for accuracy, speed, and difficulty level."""
    if not data:
        return {}

    topic_performance = {}
    overall_accuracy = []
    difficulty_breakdown = {"Easy": 0, "Medium": 0, "Hard": 0}

    for quiz in data:
        topic = quiz["quiz"]["topic"]
        accuracy = float(quiz["accuracy"].strip(" %"))  # Convert string accuracy to float
        total_questions = quiz["total_questions"]

        overall_accuracy.append(accuracy)

        # Track topic-wise performance
        if topic not in topic_performance:
            topic_performance[topic] = {"attempts": 0, "total_accuracy": 0}

        topic_performance[topic]["attempts"] += 1
        topic_performance[topic]["total_accuracy"] += accuracy

        # Difficulty breakdown (Based on question ID ranges)
        for q_id in quiz["response_map"]:
            if q_id in range(1, 34):  
                difficulty_breakdown["Easy"] += 1
            elif q_id in range(34, 67):  
                difficulty_breakdown["Medium"] += 1
            else:  
                difficulty_breakdown["Hard"] += 1

    # Fix: Properly calculate average accuracy
    for topic, stats in topic_performance.items():
        topic_performance[topic]["avg_accuracy"] = round(stats["total_accuracy"] / stats["attempts"], 2)  # Correct avg formula

    return {
        "overall_accuracy": round(sum(overall_accuracy) / len(overall_accuracy), 2),  # Fix: Average of all quiz accuracies
        "topic_performance": topic_performance,
        "difficulty_breakdown": difficulty_breakdown
    }
