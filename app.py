import os
import re
from fastapi import FastAPI, HTTPException, Request
import requests

app = FastAPI(title="LLM Security Guardrail Proxy")

# Patterns for Prompt Injections & PII
PROMPT_INJECTION_PATTERNS = [
    r"ignore previous instructions",
    r"system prompt",
    r"you are now in developer mode",
    r"bypass restriction"
]

PII_REGEX = {
    "SSN": r"\b\d{3}-\d{2}-\d{4}\b",
    "EMAIL": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
}

def inspect_prompt(prompt: str):
    for pattern in PROMPT_INJECTION_PATTERNS:
        if re.search(pattern, prompt, re.IGNORECASE):
            return False, f"Blocked: Potential prompt injection detected ('{pattern}')"
    return True, "Passed"

def mask_pii(text: str) -> str:
    for pii_type, regex in PII_REGEX.items():
        text = re.sub(regex, f"[{pii_type}_REDACTED]", text)
    return text

@app.post("/v1/chat")
async def handle_request(request: Request):
    data = await request.json()
    user_prompt = data.get("prompt", "")

    # 1. Inspect for Prompt Injection
    is_safe, message = inspect_prompt(user_prompt)
    if not is_safe:
        raise HTTPException(status_code=400, detail={"status": "REJECTED", "reason": message})

    # 2. Redact PII
    sanitized_prompt = mask_pii(user_prompt)

    # 3. Output Payload (Forward to Model/SIEM)
    return {
        "status": "APPROVED",
        "sanitized_prompt": sanitized_prompt,
        "action": "Forwarded to downstream LLM and logged to Splunk/Sentinel"
    }
