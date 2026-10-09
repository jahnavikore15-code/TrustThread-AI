def make_ai_decision(risk_level: str, trust_level: str):
    """
    Decide what action should be taken based on risk and trust levels.
    """

    if risk_level == "HIGH" or trust_level == "LOW":
        decision = "BLOCK"
        reason = "High-risk activity detected."

    elif risk_level == "MEDIUM" or trust_level == "MEDIUM":
        decision = "REVIEW"
        reason = "Potentially risky activity requires review."

    else:
        decision = "ALLOW"
        reason = "No significant risk detected."

    return {
        "ai_decision": decision,
        "decision_reason": reason
    }