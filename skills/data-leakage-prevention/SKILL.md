---
name: data-leakage-prevention
description: Review an AI system for leakage of secrets, PII, tenant data, hidden prompts, embeddings, logs, traces, memory, evaluation sets, and training artifacts across languages, frameworks, and deployment models.
---

# Data Leakage Prevention

Use this skill as a companion deep-dive when leakage risk spans prompts, retrieval, memory, logging, analytics, training, or infrastructure. It expands the `Gatekeeper` control from RAG and the auditing constraints from system security.

## Core Leakage Controls

Skill:
- Access control, data minimization, masking, and retention enforcement.

Check:
- The system must only collect, retrieve, or expose data that matches the user's explicit scope and authorization.
- Sensitive data must be masked or redacted before it reaches prompts, logs, traces, exports, or analytics sinks.

Action:
- Inventory secrets, PII, source code, internal prompts, business documents, and regulated records.
- Trace every copy path across preprocessing, prompts, retrieval, caches, vector stores, logs, traces, analytics, memory, exports, and training datasets.
- Apply PII masking before retrieved chunks or tool results are added to prompts.
- Enforce tenant isolation for memory, retrieval state, caches, and observability views.
- Sanitize evaluation and fine-tuning datasets before reuse.

What To Look For:
- Secrets hardcoded in prompts, examples, config, or tool outputs
- PII exposed through logging, tracing, analytics, or prompt replay
- Cross-session or cross-tenant memory bleed
- Embeddings or summaries exposing data beyond intended access
- Evaluation or fine-tuning datasets built from production data without sanitization
- Hidden prompts or internal documents reflected back to users

Minimum Output:
- Sensitive data inventory
- Leakage paths by component
- Unauthorized visibility matrix
- Remediations covering redaction, access control, retention, and egress

Failure Modes:
- Scoped retrieval succeeds but unmasked chunks still disclose PII to the model
- Logs capture raw prompts, context, or tool output without redaction
- Memory, caches, or analytics create cross-tenant visibility
- Training or evaluation reuse turns production data into a long-lived leak

Mitigation Bias:
- Minimize collection and persistence
- Redact before storage, not after exposure
- Isolate tenant memory and retrieval state
- Treat observability pipelines as production data processors

## References

- For stack-specific review notes, read [languages-and-frameworks.md](../../references/languages-and-frameworks.md).
- For severity wording, read [severity-and-reporting.md](../../references/severity-and-reporting.md).
- For repeatable attack cases, read [test-patterns.md](../../references/test-patterns.md).
