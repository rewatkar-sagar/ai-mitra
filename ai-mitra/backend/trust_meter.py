def trust_meter(text):

    length = len(text)

    if length > 100:
        confidence = 85
    elif length > 60:
        confidence = 70
    elif length > 20:
        confidence = 60
    else:
        confidence = 50

    return confidence