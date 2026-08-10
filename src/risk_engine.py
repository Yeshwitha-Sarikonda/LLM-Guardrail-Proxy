RULE_WEIGHTS = {
    "instruction_override": 35,
    "system_prompt_exfiltration": 40,
    "policy_bypass": 35,
    "role_override": 30,
    "encoded_payload_hint": 15,
}

PII_WEIGHTS = {
    "ssn": 30,
    "credit_card": 30,
    "api_key": 35,
    "email": 8,
    "ipv4": 5,
}

def calculate_risk(triggered_rules: list[str], sensitive_types: list[str]) -> tuple[int, list[str]]:
    reasons = []
    score = 0
    for rule in triggered_rules:
        value = RULE_WEIGHTS.get(rule, 10)
        score += value
        reasons.append(f"{rule}: +{value}")
    for item in sensitive_types:
        value = PII_WEIGHTS.get(item, 5)
        score += value
        reasons.append(f"sensitive_{item}: +{value}")
    return min(score, 100), reasons
