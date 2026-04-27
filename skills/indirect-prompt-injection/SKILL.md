---
name: indirect-prompt-injection
description: Review an AI system for prompt injection delivered through retrieved documents, web pages, emails, tickets, code repositories, API responses, or tool output rather than directly from the end user.
last_reviewed: 2026-04-27
---

# Indirect Prompt Injection

Use this skill when the model processes untrusted external content such as web pages, files, email, support tickets, API responses, or tool output. In these systems, the dangerous instruction often arrives through the content the system chose to fetch, not through the visible user prompt.

## Control Lens

- Validate: I check every piece of data coming into the system, especially externally fetched or retrieved content, before it is allowed to influence prompts, tool routing, or memory.
- Scope: I define and enforce the boundaries of what external content may influence model reasoning, what can be cited as evidence, and what can trigger downstream actions.
- Isolate: I ensure that if fetched content contains malicious instructions, the compromise is contained to a labeled untrusted context and cannot directly drive tools, memory, or privileged actions.
- Enforce: I use deterministic code such as source filters, content labeling, action guards, and structured validation to neutralize attacker instructions embedded in retrieved data.

## IPI.1 Untrusted Content Labeling and Filtering

Skill: External-content trust separation.

Check:
- Content fetched from the web, documents, email, or APIs must always be marked as untrusted data rather than trusted instructions.
- The system must detect obvious instruction-bearing patterns, hidden directives, or formatting tricks before prompt assembly.

Action:
- Label each external content block with source, trust level, and allowed use before inserting it into the prompt.
- Filter for known instruction patterns, delimiter breakouts, role claims, approval claims, and tool-routing directives.
- Preserve source boundaries so one retrieved item cannot silently blend into system or developer instructions.
- Prefer extraction or summarization pipelines that remove executable-style instructions from retrieved content before model consumption.

## IPI.2 Retrieved Instruction Neutralization

Skill: Action-safe grounding.

Check:
- External content must never be allowed to authorize a tool call, policy change, or memory write by itself.
- Retrieval and browsing flows must fail closed when the content is suspicious, contradictory, or irrelevant to the user's task.

Action:
- Require server-side policy checks before any action that was suggested by retrieved content or tool output.
- Separate informational retrieval from action-enabling workflows so evidence can inform an answer without directly controlling execution.
- Block retrieved text from writing to durable memory or agent state unless it passes explicit validation.
- Log which source introduced a suspicious instruction so defenders can trace the injection path.

Minimum Output:
- External-content intake map by source type
- Labeling, filtering, and prompt-boundary controls
- Action-guard path for content-driven tool or memory changes
- High-risk fetch surfaces and fail-closed behavior

Failure Modes:
- A web page or document injects instructions that override the agent's intended task
- Tool output is re-used as trusted orchestration state
- External content writes persistent memory or approval state without validation
- Retrieval and browsing are merged with action execution in a single trust domain

## References

- Read [core-llm-prompt-security/SKILL.md](../core-llm-prompt-security/SKILL.md) for base injection defenses.
- Read [rag-security/SKILL.md](../rag-security/SKILL.md) for source-grounding and scoped-retrieval controls.
- For repeatable attack cases, read [test-patterns.md](../../references/test-patterns.md).
