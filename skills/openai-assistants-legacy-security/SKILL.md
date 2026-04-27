---
name: openai-assistants-legacy-security
description: Review a legacy OpenAI Assistants API integration for unsafe thread and run reuse, attachment scope failures, hosted tool exposure, and migration risk to newer interfaces.
last_reviewed: 2026-04-27
---

# OpenAI Assistants Legacy Security

Use this skill when the target system still relies on the legacy OpenAI Assistants API with assistants, threads, runs, attachments, or hosted tools. This skill exists for inherited integrations that have not yet migrated to newer interfaces.

## Framework Focus

- Assistants, threads, runs, and message attachments
- Hosted tools, function calling, and file-backed workflows
- Thread reuse, run orchestration, and assistant-level instructions

## Control Lens

- Validate: I check every piece of data coming into the system, including assistant instructions, thread history, file attachments, tool arguments, and run outputs.
- Scope: I define and enforce the boundaries of which assistants, threads, files, and tools are available to each user and task.
- Isolate: I ensure that if one run, thread, or attachment becomes poisoned or mis-scoped, the failure is contained and cannot leak across assistants, users, or later runs.
- Enforce: I use deterministic code such as attachment authorization, strict tool validation, thread isolation, and migration-safe wrappers instead of trusting legacy defaults.

## 3.1 Legacy Assistant Tool and File Exposure Review

Skill: Hosted tool and attachment hardening.

Check:
- Assistants must not be configured with broader tool or file access than required for the current workflow.
- File attachments must be authorized per user and per thread before they are made available to a run.

Action:
- Inventory assistant definitions, enabled tools, and attached files for each workflow.
- Validate attachment ownership and intended scope before creating or executing runs.
- Separate assistants that need read-only retrieval from those that can trigger mutating actions.
- Treat tool outputs and retrieved file content as untrusted when fed back into later thread messages.

## 3.2 Thread, Run, and Attachment Isolation In Assistants API

Skill: Legacy state containment.

Check:
- Threads must not be reused across users, unrelated tasks, or trust domains.
- Run outputs and thread history must not carry hidden approvals or unsafe tool context into subsequent runs.

Action:
- Bind threads to a single user and workflow scope.
- Validate all function-call outputs and file-derived content before acting on them outside the API.
- Audit migration plans so legacy assumptions about threads, runs, and attachments do not persist unnoticed in successor integrations.
- Prefer wrappers that normalize legacy run output into deterministic application-side state before downstream use.

Minimum Output:
- Assistant, thread, run, and attachment inventory
- Tool and file authorization path
- Thread-reuse and state-carryover risks
- Migration blockers that keep risky legacy behavior in production

## References

- Read the base [tool-use-execution-security/SKILL.md](../tool-use-execution-security/SKILL.md) first for the shared control model.
- Read [data-leakage-prevention/SKILL.md](../data-leakage-prevention/SKILL.md) for attachment and observability leakage controls.
- For general framework notes, read [languages-and-frameworks.md](../../references/languages-and-frameworks.md).
