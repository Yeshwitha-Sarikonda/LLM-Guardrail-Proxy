from pydantic import BaseModel, Field

class InspectRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=20000)
    source: str = "demo-client"

class InspectionResult(BaseModel):
    decision: str
    risk_score: int
    triggered_rules: list[str]
    redacted_prompt: str
    owasp_controls: list[str]
    event_id: str
