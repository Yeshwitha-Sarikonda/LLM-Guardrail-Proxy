CONTROL_MAP = {
    "instruction_override": "LLM Prompt Injection",
    "system_prompt_exfiltration": "LLM Prompt Injection",
    "policy_bypass": "LLM Prompt Injection / Excessive Agency",
    "role_override": "LLM Prompt Injection",
    "encoded_payload_hint": "LLM Prompt Injection",
    "ssn": "Sensitive Information Disclosure",
    "credit_card": "Sensitive Information Disclosure",
    "api_key": "Sensitive Information Disclosure",
    "email": "Sensitive Information Disclosure",
    "ipv4": "Sensitive Information Disclosure",
}

def map_owasp(triggered_rules: list[str], sensitive_types: list[str]) -> list[str]:
    items = triggered_rules + sensitive_types
    return sorted(set(CONTROL_MAP[x] for x in items if x in CONTROL_MAP))
