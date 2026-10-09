def analyze_context(text: str):
    """
    Analyze the context and intent of a user message.
    """

    text_lower = text.lower()

    result = {
        "original_text": text,
        "length": len(text),
        "contains_instruction": False,
        "contains_sensitive_request": False,
        "context_category": "NORMAL"
    }

    # Instruction-related phrases
    instruction_words = [
        "ignore previous instructions",
        "ignore all previous instructions",
        "ignore your instructions",
        "forget previous instructions",
        "follow these instructions",
        "system prompt",
        "developer message"
    ]

    for word in instruction_words:
        if word in text_lower:
            result["contains_instruction"] = True
            break

    # Sensitive information
    sensitive_words = [
        "password",
        "secret",
        "api key",
        "apikey",
        "token",
        "private key",
        "access key",
        "login credentials",
        "credentials",
        "authentication key",
        "confidential information",
        "confidential data",
        "reveal confidential",
        "personal information",
        "private information",
        "sensitive information",
        "reveal secret",
        "reveal password",
        "steal credentials"
    ]

    for word in sensitive_words:
        if word in text_lower:
            result["contains_sensitive_request"] = True
            result["context_category"] = "SENSITIVE_REQUEST"
            break

    # Security-related context
    security_words = [
        "bypass security",
        "bypass authentication",
        "bypass restrictions",
        "hack",
        "exploit",
        "unauthorized access"
    ]

    for word in security_words:
        if word in text_lower:
            result["context_category"] = "SECURITY_RISK"
            break

    # Instruction manipulation
    if result["contains_instruction"]:
        result["context_category"] = "INSTRUCTION_MANIPULATION"

    return result