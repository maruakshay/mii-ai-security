---
name: ai-governance-and-incident-response
description: Review an AI system for weak model version control, missing rollback plans, unsafe guardrail change workflows, inadequate regulated audit trails, and incident response gaps specific to LLM and agentic failures.
last_reviewed: 2026-04-27
---

# AI Governance And Incident Response

Use this skill when the challenge is operational control in production: model release management, guardrail changes, audit readiness, or incident handling. This is the layer where many enterprise programs stall because the technical controls exist, but the operating model around them does not.

## Control Lens

- Validate: I check every piece of data coming into the system, including model release metadata, prompt and policy changes, exception approvals, audit events, and incident records.
- Scope: I define and enforce the boundaries of who can change models, prompts, guardrails, tools, and data access policies, and which environments those changes may reach.
- Isolate: I ensure that if a release, guardrail update, or model regression fails, the failure is contained through staged rollout, rollback, and environment separation rather than becoming a fleet-wide outage or security incident.
- Enforce: I use deterministic code and process controls such as signed release records, approval workflows, immutable audit trails, and incident runbooks instead of relying on tribal knowledge or informal coordination.

## GOV.1 Model and Guardrail Change Governance

Skill: Release, approval, and rollback discipline.

Check:
- Every model version, prompt template, guardrail rule, and tool policy change must be versioned, reviewable, and reversible.
- Production changes must require explicit approval aligned to risk, especially for model swaps, tool exposure, or policy relaxations.

Action:
- Track model IDs, prompt versions, policy bundles, and tool configurations as versioned assets tied to releases.
- Require peer review or formal approval for guardrail, model, and tool-policy changes before promotion to production.
- Define staged rollout and rollback procedures so teams can revert to a known-good model or policy set quickly.
- Record change rationale, approver, test evidence, and affected environments for each release.

## GOV.2 AI Incident Response and Regulated Audit Readiness

Skill: Production forensics and response readiness.

Check:
- The organization must have AI-specific incident playbooks for prompt injection, data leakage, unsafe tool execution, model regression, and memory poisoning.
- Audit trails must support forensic reconstruction and regulated review without exposing raw sensitive content unnecessarily.

Action:
- Define incident runbooks that specify triage, containment, rollback, communication, evidence preservation, and post-incident review for common AI failure modes.
- Log the minimum structured evidence needed for reconstruction: model version, prompt or policy version, retrieval source IDs, tool decisions, authorization outcomes, and user or tenant context.
- Apply retention, access control, tamper evidence, and redaction rules to logs used for regulated or high-assurance environments.
- Exercise the playbooks with tabletop or replay-based drills so teams can contain AI incidents under time pressure.

Minimum Output:
- Release inventory for models, prompts, policies, and tool configurations
- Approval workflow and rollback path for high-risk changes
- Audit-log field requirements and retention constraints
- Incident playbooks for the top AI-specific failure modes

Failure Modes:
- Teams cannot tell which model or guardrail version produced a bad outcome
- Prompt or policy changes reach production without approval or rollback readiness
- Audit logs are too sparse for forensics or too raw for compliance and privacy requirements
- Incident response plans assume generic web outages and ignore AI-specific containment steps

## References

- Read [system-infrastructure-security/SKILL.md](../system-infrastructure-security/SKILL.md) for base logging and runtime controls.
- Read [model-supply-chain-security/SKILL.md](../model-supply-chain-security/SKILL.md) for model provenance and promotion controls.
- For severity wording, read [severity-and-reporting.md](../../references/severity-and-reporting.md).
