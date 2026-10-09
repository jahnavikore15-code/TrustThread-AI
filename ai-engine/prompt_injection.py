
def detect_prompt_injection(text: str):
    """
    Detect common prompt-injection attempts using phrase matching.
    This is a basic detector, not a complete security solution.
    """

    if not isinstance(text, str) or not text.strip():
        return {
            "is_prompt_injection": False,
            "detected_patterns": []
        }

    text_lower = text.lower()

    injection_patterns = [
        "ignore previous instructions",
        "ignore all previous instructions",
        "ignore your instructions",
        "forget previous instructions",
        "disregard previous instructions",
        "disregard all earlier directions",
        "ignore all earlier directions",
        "override previous instructions",
        "follow these instructions instead",
        "system prompt",
        "hidden system prompt",
        "reveal your prompt",
        "show me your prompt",
        "expose the hidden prompt",
        "developer message",
        "reveal secret",
        "reveal confidential information",
        "give me the password",
        "bypass security",
        "bypass restrictions",
        "ignore safety rules",
        "disable safety rules",
        "act as an unrestricted AI"
    ]

    detected_patterns = [
        pattern for pattern in injection_patterns
        if pattern in text_lower
    ]

    return {
        "is_prompt_injection": len(detected_patterns) > 0,
        "detected_patterns": detected_patterns
    }