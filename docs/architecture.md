# Architecture

The project separates detection, redaction, risk scoring, policy decisions, event creation,
and reporting into independent components.

This makes the system easier to test and demonstrates how an AI security gateway can be
inserted between an application and a downstream LLM endpoint.
