def calculate_risk(score):

    # Low risk
    if score == 0:
        return "Low"

    # Medium risk
    elif score <= 2:
        return "Medium"

    # High risk
    else:
        return "High"