import re

RULES = {
    "instruction_override": [
        r"ignore\s+(all\s+)?previous\s+instructions",
        r"disregard\s+(all\s+)?previous\s+instructions",
        r"forget\s+(all\s+)?previous\s+instructions",
    ],
    "system_prompt_exfiltration": [
        r"reveal\s+(the\s+)?system\s+prompt",
        r"show\s+(me\s+)?(the\s+)?system\s+prompt",
        r"print\s+(the\s+)?hidden\s+instructions",
    ],
    "policy_bypass": [
        r"bypass\s+(the\s+)?(safety|security|policy)",
        r"disable\s+(the\s+)?guardrails",
        r"jailbreak",
    ],
    "role_override": [
        r"you\s+are\s+now\s+developer\s+mode",
        r"act\s+as\s+an?\s+unrestricted",
        r"pretend\s+you\s+have\s+no\s+rules",
    ],
    "encoded_payload_hint": [
        r"base64",
        r"decode\s+this",
        r"hex\s+encoded",
    ],
}

def detect_prompt_injection(prompt: str) -> list[str]:
    text = prompt.lower()
    hits = []
    for rule, patterns in RULES.items():
        if any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns):
            hits.append(rule)
    return sorted(set(hits))
