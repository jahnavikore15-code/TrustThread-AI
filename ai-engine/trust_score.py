def calculate_trust_score(risk_score: int):
    """
    Calculate a trust score based on the detected risk score.
    """

    trust_score = 100 - risk_score

    if trust_score < 0:
        trust_score = 0

    if trust_score >= 80:
        trust_level = "HIGH"
    elif trust_score >= 50:
        trust_level = "MEDIUM"
    else:
        trust_level = "LOW"

    return {
        "trust_score": trust_score,
        "trust_level": trust_level
    }