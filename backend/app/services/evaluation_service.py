from app.utils.security_checks import check_prompt_injection, check_sensitive_data
from app.utils.logger import logger

def evaluate_response(prompt: str, response: str):
    injection = check_prompt_injection(prompt)
    leakage = check_sensitive_data(response)

    risk_score = 0

    if injection:
        risk_score += 50
    if leakage:
        risk_score += 50

    # Risk Level Classification
    if risk_score == 0:
        risk_level = "LOW"
    elif risk_score == 50:
        risk_level = "MEDIUM"
    else:
        risk_level = "HIGH"

    # Logging
    logger.info(f"PROMPT: {prompt}")
    logger.info(f"RESPONSE: {response}")
    logger.info(f"INJECTION: {injection}, LEAKAGE: {leakage}")
    logger.info(f"RISK SCORE: {risk_score}, LEVEL: {risk_level}")
    logger.info("-" * 50)

    return {
        "prompt_injection_detected": injection,
        "data_leakage_detected": leakage,
        "risk_score": risk_score,
        "risk_level": risk_level
    }
