# Test Patterns

Use this reference when converting a review into repeatable tests.

## Prompt Security Tests

- Indirect prompt injection in retrieved or uploaded content
- System prompt extraction attempts
- Role confusion and instruction shadowing
- Output format breaking to escape downstream validators
Related skills: `core-llm-prompt-security`, `indirect-prompt-injection`

## RAG Security Tests

- Malicious document insertion into the index
- Metadata filter bypass
- Cross-tenant retrieval by identifier guessing
- Retrieval of stale or deleted records
Related skills: `rag-security`, `langchain-rag-security`, `llamaindex-rag-security`, `haystack-rag-security`

## Data Leakage Tests

- Secret extraction from prompts, logs, traces, and memory
- PII exposure across sessions or tenants
- Training or evaluation dataset leakage
- Model output containing hidden internal context
Related skills: `data-leakage-prevention`, `memory-security`, `ai-governance-and-incident-response`

## Tool Security Tests

- Unsafe argument passing to shell, SQL, HTTP, or file tools
- Privilege escalation through tool chaining
- Confirmation bypass for destructive actions
- Sandbox escape attempts through generated code
Related skills: `tool-use-execution-security`, `semantic-kernel-tool-security`, `openai-responses-tool-file-security`, `openai-assistants-legacy-security`, `agentic-trust-boundaries`

## Agentic And Memory Tests

- Agent-to-agent prompt injection through planner summaries or worker output
- Cross-agent privilege inheritance through shared approvals or credentials
- Persistent memory poisoning that influences future sessions
- Deletion failures where quarantined memory remains retrievable
Related skills: `agentic-trust-boundaries`, `memory-security`

## Model And Supply Chain Tests

- Poisoned fine-tune or adapter promotion into production
- Trigger-style backdoor prompts in pre-release evaluation
- Model swap without rollback metadata or approval trail
- Inference API exposure or model artifact exfiltration path
Related skills: `model-supply-chain-security`, `ai-governance-and-incident-response`

## Multimodal Tests

- Hidden text or OCR-based instruction injection in images or PDFs
- Typographic attacks that alter extracted meaning
- Vision-to-tool action requests derived from screenshots or diagrams
- Image-derived PII or secrets leaking into logs or downstream prompts
Related skills: `multimodal-security`

## Governance And Response Tests

- Guardrail rule changes merged without approval evidence
- Missing rollback path for model or prompt regressions
- Audit logs too sparse for incident reconstruction
- Incident playbooks not exercised for prompt injection or unsafe tool use
Related skills: `ai-governance-and-incident-response`, `system-infrastructure-security`

## Infrastructure Tests

- Overexposed admin endpoints
- Missing egress restrictions
- Unsafe dependency or model artifact loading
- Weak secret rotation and environment isolation
