# Interview Walkthrough

## Problem
LLM-integrated applications can receive malicious or sensitive prompts before those requests reach the model.

## What I built
A defensive Python/FastAPI guardrail proxy that:
1. inspects prompts,
2. detects common prompt-injection patterns,
3. redacts sensitive data,
4. calculates risk,
5. applies allow/review/block policy,
6. generates structured security events,
7. creates incident reports.

## What I would improve for production
- semantic classifier rather than regex-only detection
- model-specific output filtering
- authentication and authorization
- distributed rate limiting
- durable event pipeline
- Splunk/Sentinel production connector
- continuous evaluation dataset
- false-positive measurement

## Honest limitations
This portfolio version uses synthetic examples and deterministic security rules.
