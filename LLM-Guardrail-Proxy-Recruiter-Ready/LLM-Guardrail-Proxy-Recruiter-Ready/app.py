from fastapi import FastAPI
from src.models import InspectRequest, InspectionResult
from src.inspector import inspect_prompt
from src.security_event import append_jsonl

app = FastAPI(
    title="LLM Guardrail Proxy",
    description="Portfolio AI-security proxy for prompt inspection and security event generation.",
    version="1.0.0",
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/v1/inspect", response_model=InspectionResult)
def inspect(request: InspectRequest):
    result = inspect_prompt(request.prompt, request.source)
    event = result["event"]
    append_jsonl(event)
    return InspectionResult(
        decision=event["decision"],
        risk_score=event["risk_score"],
        triggered_rules=event["triggered_rules"],
        redacted_prompt=result["redacted_prompt"],
        owasp_controls=result["owasp_controls"],
        event_id=event["event_id"],
    )
