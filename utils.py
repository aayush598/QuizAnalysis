def calculate_percentage(value, total):
    """Calculate percentage correctly, preventing division by zero."""
    return round((value / total) * 100, 2) if total else 0
