
import re


INJECTION_PATTERNS = [
    r"ignore (all )?(previous|prior|above) instructions",
    r"reveal (the )?(system prompt|secret|api key|password)",
    r"bypass (all )?(security|restrictions|permissions)",
    r"disregard (all )?(previous|prior) instructions",
]

SENSITIVE_PATTERNS = {
    "API_KEY": r"\b(?:sk-[A-Za-z0-9_-]{12,}|AKIA[A-Z0-9]{16})\b",
    "PASSWORD": r"\b(password|passcode|login credentials)\b",
    "FINANCIAL": r"\b(salary|payroll|bank account|credit card)\b",
    "CONFIDENTIAL": r"\b(confidential|secret document|internal only)\b",
    "PERSONAL_DATA": r"\b(passport number|personal address|social security number)\b",
}


def analyze_security(query: str, identity_verified: bool) -> dict:
    injection = any(
        re.search(pattern, query, re.IGNORECASE)
        for pattern in INJECTION_PATTERNS
    )

    categories = [
        category
        for category, pattern in SENSITIVE_PATTERNS.items()
        if re.search(pattern, query, re.IGNORECASE)
    ]

    score = 10
    reasons = []

    if not identity_verified:
        score += 40
        reasons.append("Identity could not be verified")

    if categories:
        score += 30
        reasons.append("Sensitive information pattern detected")

    if injection:
        score += 50
        reasons.append("Possible prompt injection detected")

    score = min(score, 100)

    if score >= 80:
        threat_level = "CRITICAL"
    elif score >= 60:
        threat_level = "HIGH"
    elif score >= 30:
        threat_level = "MEDIUM"
    else:
        threat_level = "LOW"

    if not reasons:
        reasons.append("No configured threat patterns detected")

    return {
        "sensitive": bool(categories),
        "sensitive_type": categories,
        "prompt_injection": injection,
        "risk_score": score,
        "threat_level": threat_level,
        "reasons": reasons,
    }
