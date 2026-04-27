---
name: openai-responses-tool-file-security
description: Review an OpenAI Responses API integration for unsafe hosted-tool exposure, file-search scope failures, function-calling validation gaps, and conversation-state or tool-loop escalation.
last_reviewed: 2026-04-27
---

# OpenAI Responses Tool And File Security

Use this skill when the target system uses the OpenAI Responses API with built-in tools, function calling, file search, uploaded files, or conversation state. This skill narrows the base `tool-use-execution-security` controls to OpenAI-hosted tool and file surfaces.

## Framework Focus

- `responses.create`, conversation state, and `previous_response_id`
- Built-in tools such as file search and other hosted tools
- Custom function calling, `tool_choice`, `max_tool_calls`, and structured tool arguments
- Uploaded files, vector stores, and file-backed retrieval

## Control Lens

- Validate: I check every piece of data coming into the system, including uploaded files, vector-store contents, tool arguments, response items, and tool outputs returned through the API.
- Scope: I define and enforce the boundaries of which files, vector stores, tools, and conversation state can be attached to a response for a given user or task.
- Isolate: I ensure that if the model misuses a hosted tool or returns unsafe tool-call output, the failure is contained and cannot directly widen file access, trigger unsupported actions, or poison future responses.
- Enforce: I use deterministic code such as JSON schema validation, response-item parsing, file authorization checks, and explicit tool configuration to constrain the integration.

## 3.1 Hosted Tool Invocation and File Scope Review In Responses API

Skill: Built-in tool and file-scope hardening.

Check:
- Response requests must not attach files, vector stores, or hosted tools beyond the current user's authorization scope.
- Built-in tool access must be explicitly configured and limited to the task rather than left broadly enabled by default.

Action:
- Map which tools are enabled on each response path and why, including file search and custom functions.
- Validate file and vector-store ownership before attaching them to a response request.
- Restrict `tool_choice` and related configuration so sensitive tools are only available where necessary.
- Treat tool outputs and retrieved file snippets as untrusted content when re-inserting them into later prompts or workflows.

## 3.2 Conversation State and Tool Loop Containment In Responses API

Skill: Stateful loop and output validation.

Check:
- Conversation state must not silently carry forward unsafe assumptions, approvals, or file context into unrelated tasks.
- Model-produced function calls or tool loops must be validated in application code before execution.

Action:
- Bound how conversation state is reused across users, sessions, and tasks.
- Validate every function call argument against a strict schema before executing custom code.
- Set explicit limits on tool-loop behavior and handle repeated or unexpected calls as policy failures.
- Parse response items deterministically instead of trusting raw text or inferred structure.

Minimum Output:
- Responses API request map with tools, files, vector stores, and state reuse
- Authorization path for file and tool attachment
- Schema-validation and tool-loop controls
- Containment requirements for unsafe response items or repeated tool calls

## References

- Read the base [tool-use-execution-security/SKILL.md](../tool-use-execution-security/SKILL.md) first for the shared control model.
- Read [rag-security/SKILL.md](../rag-security/SKILL.md) when file search is used as hosted retrieval.
- For general framework notes, read [languages-and-frameworks.md](../../references/languages-and-frameworks.md).
