import os

BLOCK_THRESHOLD = int(os.getenv("BLOCK_THRESHOLD", "80"))
REVIEW_THRESHOLD = int(os.getenv("REVIEW_THRESHOLD", "45"))
REDACT_IPS = os.getenv("REDACT_IPS", "false").lower() == "true"
