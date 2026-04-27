---
name: dspy-program-security
description: Review a DSPy application for unsafe signature design, optimizer dataset leakage, prompt-program boundary failures, weak typed output enforcement, and insecure tool-wrapper behavior.
last_reviewed: 2026-04-27
---

# DSPy Program Security

Use this skill when the target system uses DSPy signatures, modules, optimizers, teleprompters, evaluators, or tool wrappers. DSPy introduces security risk not only in prompts, but also in how training examples, compiled programs, and typed outputs shape future model behavior.

## Framework Focus

- `Signature` definitions, modules, adapters, and prompt-program composition
- Optimizers and teleprompters, including training and evaluation example sets
- Tool wrappers, retrieval modules, and evaluation pipelines

## Control Lens

- Validate: I check every piece of data coming into the system, including optimizer datasets, compiled prompts, module inputs, evaluator examples, and tool-wrapper arguments.
- Scope: I define and enforce the boundaries of what each DSPy module can see, what examples can influence optimization, and which tools or retrieval paths are available to the program.
- Isolate: I ensure that if a DSPy module is prompt-injected or an optimizer dataset is poisoned, the failure is contained and cannot silently propagate into compiled programs or privileged tool execution.
- Enforce: I use deterministic code such as typed signatures, schema validation, curated optimizer datasets, and explicit tool policies to constrain DSPy behavior.

## 1.1 Prompt Program and Optimizer Boundary Review In DSPy

Skill: Dataset and program-boundary hardening.

Check:
- Optimizer or teleprompter datasets must not contain instruction-bearing or sensitive production content that can poison the compiled program.
- Module composition must preserve the distinction between trusted program instructions and untrusted task data.

Action:
- Review how examples are sourced, sanitized, and approved before DSPy optimization or compilation.
- Keep evaluation and optimization datasets separate from live user content unless explicit validation and redaction are applied.
- Verify compiled prompts and program traces to confirm untrusted example text does not become hidden control logic.
- Scope retrieval modules and subprogram context to the minimum needed for each signature.

## 1.2 Typed Output and Tool Wrapper Enforcement In DSPy

Skill: Typed execution and wrapper controls.

Check:
- DSPy outputs that drive code, tools, or business logic must be validated outside the model.
- Tool wrappers and retrieval adapters must not widen permissions beyond the intended module scope.

Action:
- Enforce typed output parsing for every module whose output is consumed by code or other modules.
- Validate tool-wrapper arguments and return values before they are re-ingested into the DSPy program.
- Restrict module-specific tool access instead of exposing a broad global tool set.
- Log optimizer choices, module traces, and policy failures without leaking sensitive example content.

Minimum Output:
- DSPy program graph with modules, optimizers, evaluators, and tool wrappers
- Dataset sourcing and poisoning controls
- Typed output and wrapper validation path
- Privilege and leakage risks across compiled programs

## References

- Read the base [core-llm-prompt-security/SKILL.md](../core-llm-prompt-security/SKILL.md) first for shared prompt and output controls.
- Read [tool-use-execution-security/SKILL.md](../tool-use-execution-security/SKILL.md) for wrapper and action-policy hardening.
- For general framework notes, read [languages-and-frameworks.md](../../references/languages-and-frameworks.md).
