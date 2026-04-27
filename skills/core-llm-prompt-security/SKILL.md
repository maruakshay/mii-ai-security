---
name: core-llm-prompt-security
description: Review the core prompt layer of an LLM application for prompt injection, jailbreaks, system prompt exposure, weak guardrails, unsafe output handling, and trust-boundary failures across any language or framework.
last_reviewed: 2026-04-27
---

# Core LLM Prompt Security

Use this skill when the main risk is in prompt construction, model instruction hierarchy, or output handling. This section hardens the input and output streams of the LLM itself.

## Control Lens

- Validate: I check every piece of data coming into the system, including user text, chat history, retrieved content, uploaded files, tool output, and prior model output.
- Scope: I define and enforce the boundaries of the LLM's knowledge and actions by separating trusted instructions from untrusted context and limiting what external context can influence the prompt.
- Isolate: I ensure that if the LLM fails or is attacked, the failure is contained and cannot directly reach core services, privileged tools, or sensitive data paths.
- Enforce: I use deterministic code such as Pydantic, JSON schema validation, and strict parsers to validate model output and downstream actions instead of trusting generated format or intent.

## 1.1 Prompt Injection Defense (The Guard Rail)

Skill: Contextual separation and input sanitization.

Check:
- All user inputs must be separated from system prompts using unique delimiters such as `---USER_INPUT---`.
- Untrusted content from files, chat history, tools, or retrieval must never be merged into trusted instructions without labeling.

Action:
- Implement a preprocessing layer that scans user input for system-prompt override phrases such as `Ignore previous instructions` or `As a developer, you can`.
- If suspicious control text is detected, flag and sanitize the input or reject the request.
- Maintain a prompt map showing where trusted instructions, user content, retrieved content, and tool outputs enter the final prompt.

Best Practice:
- Never trust the input; treat it as potentially malicious code.
- Assume indirect prompt injection can arrive through uploaded files, URLs, email, retrieved chunks, or prior model/tool output.

## 1.2 Output Validation And Guardrails (The Filter)

Skill: Schema enforcement and toxic content filtering.

Check:
- Every LLM output must pass through a final validation step before it is shown to a user or forwarded to another system.

Action:
- Schema enforcement: when the output must be JSON or another fixed structure, validate it with a strict parser such as Pydantic or an equivalent typed schema validator.
- Content filtering: pass the output through a secondary safety layer to check for toxic, hateful, or illegal content before display or execution.
- Treat all model output as untrusted if it is consumed by renderers, tools, SQL, shell, or code execution paths.

Minimum Output:
- Prompt boundary map with delimiters used
- Injection triggers and sanitization rules
- Output validation path and schema failure handling
- Guardrail gaps that still fail open

Failure Modes:
- User text can override the system or developer prompt
- Model output bypasses validation and reaches downstream code directly
- Safety policy exists only in prompt text and is not enforced by code

## References

- For stack-specific review notes, read [languages-and-frameworks.md](../../references/languages-and-frameworks.md).
- For severity wording, read [severity-and-reporting.md](../../references/severity-and-reporting.md).
- For repeatable attack cases, read [test-patterns.md](../../references/test-patterns.md).
