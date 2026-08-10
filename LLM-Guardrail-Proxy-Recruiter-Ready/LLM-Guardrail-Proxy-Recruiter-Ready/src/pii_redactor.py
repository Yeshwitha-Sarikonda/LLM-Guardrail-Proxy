import re

PATTERNS = {
    "ssn": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "credit_card": re.compile(r"\b(?:\d[ -]*?){13,16}\b"),
    "api_key": re.compile(r"\b(?:sk|api|key)[-_]?[A-Za-z0-9]{12,}\b", re.IGNORECASE),
    "ipv4": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
}

MASKS = {
    "ssn": "***-**-****",
    "email": "[REDACTED_EMAIL]",
    "credit_card": "[REDACTED_CARD]",
    "api_key": "[REDACTED_SECRET]",
    "ipv4": "[REDACTED_IP]",
}

def redact_sensitive_data(text: str, redact_ips: bool = False) -> tuple[str, list[str]]:
    redacted = text
    found = []
    for kind, pattern in PATTERNS.items():
        if kind == "ipv4" and not redact_ips:
            continue
        if pattern.search(redacted):
            found.append(kind)
            redacted = pattern.sub(MASKS[kind], redacted)
    return redacted, sorted(set(found))
