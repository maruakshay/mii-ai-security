---
name: system-infrastructure-security
description: Review the system and infrastructure around an AI application for secret handling, network exposure, runtime isolation, model and dependency supply chain risk, weak observability controls, and deployment misconfiguration across cloud and self-hosted environments.
last_reviewed: 2026-04-27
---

# System And Infrastructure Security

Use this skill when the risk is in the runtime, deployment, network, identity, supply chain, or operational controls surrounding the AI system. These controls are not LLM-specific, but they determine whether the application is defensible in production.

## Control Lens

- Validate: I check every piece of data coming into the system, including requests, identities, network traffic, dependency sources, audit events, and configuration changes.
- Scope: I define and enforce the boundaries of the LLM's knowledge and actions by constraining network paths, service identities, runtime permissions, and observability access.
- Isolate: I ensure that if the LLM fails or is attacked, the failure is contained and cannot move laterally into core infrastructure, secrets, or primary data stores.
- Enforce: I use deterministic code and platform controls such as IAM policy, admission rules, schema-checked config, and structured audit validation instead of relying on prompt policy or operator intent.

## 4.1 Rate Limiting And Throttling

Skill: Denial of service prevention.

Check:
- Limit the number of requests per user or IP address over a rolling time window.

Action:
- Implement rate limiters at the API gateway or edge layer to prevent brute-force attempts, runaway agent loops, unexpected cost spikes, and avoidable outages.
- Distinguish between interactive, batch, admin, and tool-execution traffic so one class cannot starve the rest.

## 4.2 Logging And Auditing (The Black Box)

Skill: Non-repudiation.

Check:
- Every significant event must be logged, including successful calls, failed calls, prompt injection attempts, and data access.

Action:
- Log a structured, redacted audit trail for the full sequence: user request metadata, prompt template identifier or hash, retrieval document identifiers, output policy result, tool or user action, and authorization outcome.
- Record tool calls, authorization decisions, rate-limit events, and data-access outcomes.
- Do not log raw prompts, raw retrieved chunks, or raw outputs by default when they can contain secrets, PII, or proprietary content.
- Protect logs as sensitive data stores and apply redaction, access control, and retention limits.

Minimum Output:
- Rate-limit policy by endpoint and actor type
- Audit trail coverage map
- Sensitive log fields requiring redaction or masking
- Gaps that would block incident response, debugging, or compliance review

Best Practice:
- Logs must be detailed enough for reconstruction but not so raw that they become a new leakage channel.
- Pair logging with retention, access control, and tamper-evidence requirements.

## References

- For stack-specific review notes, read [languages-and-frameworks.md](../../references/languages-and-frameworks.md).
- For severity wording, read [severity-and-reporting.md](../../references/severity-and-reporting.md).
- For repeatable attack cases, read [test-patterns.md](../../references/test-patterns.md).
- For deeper leakage controls in observability and storage, read [data-leakage-prevention/SKILL.md](../data-leakage-prevention/SKILL.md).
