# Test Patterns

Use this reference when converting a review into repeatable tests.

## Prompt Security Tests

- Indirect prompt injection in retrieved or uploaded content
- System prompt extraction attempts
- Role confusion and instruction shadowing
- Output format breaking to escape downstream validators

## RAG Security Tests

- Malicious document insertion into the index
- Metadata filter bypass
- Cross-tenant retrieval by identifier guessing
- Retrieval of stale or deleted records

## Data Leakage Tests

- Secret extraction from prompts, logs, traces, and memory
- PII exposure across sessions or tenants
- Training or evaluation dataset leakage
- Model output containing hidden internal context

## Tool Security Tests

- Unsafe argument passing to shell, SQL, HTTP, or file tools
- Privilege escalation through tool chaining
- Confirmation bypass for destructive actions
- Sandbox escape attempts through generated code

## Infrastructure Tests

- Overexposed admin endpoints
- Missing egress restrictions
- Unsafe dependency or model artifact loading
- Weak secret rotation and environment isolation
