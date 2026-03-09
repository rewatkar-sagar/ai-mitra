def analyze_text(user_text):
    # Simple analysis logic
    words = user_text.lower()

    stress_keywords = ["sad", "depressed", "lonely", "tired", "hopeless"]

    score = 0
    for word in stress_keywords:
        if word in words:
            score += 1

    return score