def calculate_risk(text):
    """
    Temporary placeholder for Member 4.
    Returns a dummy dictionary so the Flask app can run and Member 2 can test the AI Engine.
    """
    return {
        "rule_based_risk": "Pending",
        "flagged_words": []
    }

def calculate_risk(score):

    if score == 0:
        return "Low"

    elif score <= 2:
        return "Medium"

    else:
        return "High"

