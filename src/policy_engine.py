from config import BLOCK_THRESHOLD, REVIEW_THRESHOLD

def decide(risk_score: int) -> str:
    if risk_score >= BLOCK_THRESHOLD:
        return "block"
    if risk_score >= REVIEW_THRESHOLD:
        return "review"
    return "allow"
