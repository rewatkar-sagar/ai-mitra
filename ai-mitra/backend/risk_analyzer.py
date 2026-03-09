def calculate_risk(score):

    if score == 0:
        return "Low"

    elif score <= 2:
        return "Medium"

    else:
        return "High"