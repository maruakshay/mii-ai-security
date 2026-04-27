---
name: tool-use-execution-security
description: Review an agentic AI system for insecure tool calling, unsafe code or shell execution, excessive permissions, confirmation bypass, argument injection, sandbox escape risk, and action-policy failures across languages and frameworks.
---

# Tool Use And Execution Security

Use this skill when the model can call functions, access APIs, execute code, manipulate files, browse, or take external actions. This section applies to agentic systems with tool or function calling.

## 3.1 Function Calling Authorization (The Permission Slip)

Skill: Least privilege principle.

Check:
- The LLM must not be allowed to call functions it is not explicitly permitted to use for the current user context.

Action:
- Role-based access control: map user roles such as `Basic User` or `Admin` to a predefined list of callable functions.
- Validate every function argument against both the tool schema and the user's scope before execution.
- Never execute a function call based solely on the LLM's output.

## 3.2 Output Execution Sandboxing (The Sandbox)

Skill: Isolation and resource limitation.

Check:
- Any external code execution, shell execution, or database query execution must happen in a completely isolated environment.

Action:
- Use containerization or sandboxed execution libraries so a malicious function call cannot affect the host system.
- Restrict filesystem access, outbound network access, CPU, memory, and execution time to the defined scope.
- Separate read-only tools from mutating tools and require confirmation for destructive actions.

Minimum Output:
- Tool inventory with role mapping and privileges
- Parameter validation and policy enforcement path
- Isolation model for shell, code, SQL, file, and HTTP tools
- Known escape, chaining, or confirmation-bypass scenarios

Failure Modes:
- Internal-only tools are reachable from external prompts
- Tool output is fed back into the prompt loop as trusted instructions
- Ambient credentials or broad service accounts turn minor prompt abuse into high-impact compromise

## References

- For stack-specific review notes, read [languages-and-frameworks.md](../../references/languages-and-frameworks.md).
- For severity wording, read [severity-and-reporting.md](../../references/severity-and-reporting.md).
- For repeatable attack cases, read [test-patterns.md](../../references/test-patterns.md).
