import re

def check_prompt_injection(prompt: str):
    patterns = [
        r"ignore\s+previous\s+instructions",
        r"bypass\s+security",
        r"reveal\s+(system|hidden)\s+prompt",
        r"act\s+as\s+.*without\s+restriction",
    ]

    for pattern in patterns:
        if re.search(pattern, prompt.lower()):
            return True
    return False


def check_sensitive_data(response: str):
    patterns = [
        r"api[_-]?key",
        r"password",
        r"secret",
        r"token",
        r"\b\d{4}-\d{4}-\d{4}-\d{4}\b",  # credit card pattern
    ]

    for pattern in patterns:
        if re.search(pattern, response.lower()):
            return True
    return False