def fraud_check(text):

    scam_words = [
        "winner",
        "lottery",
        "click link",
        "urgent",
        "otp",
        "bank",
        "investment",
        "free money"
    ]

    score = 0

    for word in scam_words:
        if word in text.lower():
            score += 1

    if score >= 3:
        return "High Scam Risk"
    elif score >= 1:
        return "Suspicious"
    else:
        return "Low Risk"