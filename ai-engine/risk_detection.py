
def detect_risk(text: str, context_result: dict, injection_result: dict):
    """
    Detect risk using prompt injection, sensitive requests,
    and security-related context.
    """

    risk_score = 0
    reasons = []

    # Detect prompt injection
    if injection_result.get("is_prompt_injection"):
        risk_score += 50
        reasons.append("Prompt injection detected")

    # Detect requests for sensitive information
    if context_result.get("contains_sensitive_request"):
        risk_score += 30
        reasons.append("Sensitive information requested")

    # Detect security-related activity
    if context_result.get("context_category") == "SECURITY_RISK":
        risk_score += 40
        reasons.append("Security-related activity detected")

    # Keep the risk score between 0 and 100
    risk_score = min(risk_score, 100)

    # Determine risk level
    if risk_score >= 70:
        risk_level = "HIGH"
    elif risk_score >= 30:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "risk_reasons": reasons
    }