from datetime import datetime, timezone
import json
import uuid
from pathlib import Path

def build_security_event(source: str, decision: str, risk_score: int,
                         triggered_rules: list[str], sensitive_types: list[str]) -> dict:
    return {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event_type": "llm_guardrail_inspection",
        "source": source,
        "decision": decision,
        "risk_score": risk_score,
        "triggered_rules": triggered_rules,
        "sensitive_types": sensitive_types,
    }

def append_jsonl(event: dict, path: str = "security-events.jsonl") -> None:
    with Path(path).open("a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")
