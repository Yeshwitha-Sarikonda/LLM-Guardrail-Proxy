from src.risk_engine import calculate_risk

def test_high_risk_combination():
    score, _ = calculate_risk(
        ["instruction_override", "system_prompt_exfiltration"],
        ["api_key"],
    )
    assert score == 100

def test_safe_request():
    score, _ = calculate_risk([], [])
    assert score == 0
