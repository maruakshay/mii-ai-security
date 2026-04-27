---
name: semantic-kernel-tool-security
description: Review a Semantic Kernel agent or planner for unauthorized plugin execution, unsafe function routing, excessive connector permissions, missing argument validation, insecure memory use, and weak sandboxing around code or action execution.
last_reviewed: 2026-04-27
---

# Semantic Kernel Tool Security

Use this skill when the target system uses Semantic Kernel plugins, planners, function calling, memory connectors, or agent orchestration. This skill narrows the base `tool-use-execution-security` controls to concrete Semantic Kernel review points.

## Framework Focus

- Native and prompt-based plugins, function registration, and plugin exposure rules
- Planners, automatic function calling, kernel arguments, filters, and memory connectors
- Connectors to files, HTTP APIs, databases, enterprise systems, and code execution surfaces

## Control Lens

- Validate: I check every piece of data coming into the system, including `KernelArguments`, planner output, plugin parameters, connector responses, and any model-proposed action.
- Scope: I define and enforce the boundaries of the LLM's knowledge and actions by limiting registered plugins, connector permissions, planner reach, and environment-specific function exposure.
- Isolate: I ensure that if the LLM fails or is attacked, the failure is contained and cannot escape from Semantic Kernel plugins or connectors into the host, core system, or sensitive data stores.
- Enforce: I use deterministic code such as typed plugin contracts, JSON schema validation, policy filters, and explicit allowlists to validate Semantic Kernel output and invocation paths before execution.

## 3.1 Function Calling Authorization In Semantic Kernel

Skill: Least privilege plugin exposure and policy enforcement.

Check:
- The kernel must not expose plugins or functions beyond the current user's role, task scope, and environment boundary.
- Planner or auto-invocation behavior must not reach admin or mutating functions without explicit authorization.

Action:
- Map each user role to an explicit allowlist of Semantic Kernel plugins and functions.
- Validate `KernelArguments` and plugin parameters against typed schemas and business policy before invocation.
- Review planner configuration to confirm it cannot discover or call internal-only plugins through broad kernel registration.
- Separate read-only plugins from mutating plugins and require durable confirmation for destructive operations.

Failure Modes:
- Auto function calling reaches internal plugins that were registered for convenience
- Plugin outputs are trusted as instructions and fed back into the kernel loop
- Connector credentials inherit ambient privileges far broader than the user scope

## 3.2 Output Execution Sandboxing In Semantic Kernel

Skill: Isolation and connector containment.

Check:
- Any plugin that executes code, queries databases, manipulates files, or calls sensitive APIs must run inside the approved isolation boundary.

Action:
- Place code, shell, and database execution behind sandboxed or brokered plugins rather than direct host access.
- Restrict network egress, filesystem scope, runtime identity, and execution time for high-risk plugins.
- Log every plugin invocation, policy decision, and denied call without exposing raw secrets in the logs.
- Ensure memory connectors and planners cannot be used as side channels to bypass plugin restrictions.

Minimum Output:
- Semantic Kernel plugin inventory with role mapping
- Planner and auto-function-call exposure risks
- Argument validation and isolation controls
- Required fixes for connector permissions, logging, and sandbox boundaries

## References

- Read the base [tool-use-execution-security/SKILL.md](../tool-use-execution-security/SKILL.md) first for the shared control model.
- For leakage concerns in logs or memory, read [data-leakage-prevention/SKILL.md](../data-leakage-prevention/SKILL.md).
- For general framework notes, read [languages-and-frameworks.md](../../references/languages-and-frameworks.md).
