from src.pii_redactor import redact_sensitive_data

def test_ssn_redaction():
    redacted, types = redact_sensitive_data("SSN is 111-22-3333")
    assert "***-**-****" in redacted
    assert "ssn" in types

def test_email_redaction():
    redacted, types = redact_sensitive_data("Email analyst@example.com")
    assert "[REDACTED_EMAIL]" in redacted
    assert "email" in types
