from config import REDACT_IPS
from src.prompt_detector import detect_prompt_injection
from src.pii_redactor import redact_sensitive_data
from src.risk_engine import calculate_risk
from src.policy_engine import decide
from src.owasp_mapping import map_owasp
from src.security_event import build_security_event

def inspect_prompt(prompt: str, source: str = "demo-client") -> dict:
    rules = detect_prompt_injection(prompt)
    redacted, sensitive_types = redact_sensitive_data(prompt, redact_ips=REDACT_IPS)
    score, reasons = calculate_risk(rules, sensitive_types)
    decision = decide(score)
    owasp = map_owasp(rules, sensitive_types)
    event = build_security_event(source, decision, score, rules, sensitive_types)
    return {
        "event": event,
        "redacted_prompt": redacted,
        "risk_reasons": reasons,
        "owasp_controls": owasp,
    }
