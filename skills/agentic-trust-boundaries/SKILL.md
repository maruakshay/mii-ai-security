---
name: agentic-trust-boundaries
description: Review a multi-agent or orchestrated AI system for agent-to-agent prompt injection, trust transitivity failures, planner-to-worker privilege spread, unsafe delegation, and cross-agent action escalation.
last_reviewed: 2026-04-27
---

# Agentic Trust Boundaries

Use this skill when one model delegates to another model, when planners coordinate workers, or when multiple agents exchange prompts, summaries, tool outputs, or memory. In these systems, the output of one agent becomes the untrusted input of another.

## Control Lens

- Validate: I check every piece of data coming into the system, including delegation payloads, planner summaries, worker results, cross-agent memory, and approval state.
- Scope: I define and enforce the boundaries of each agent's knowledge and actions so no downstream agent inherits broader privileges or context than it was explicitly granted.
- Isolate: I ensure that if one agent is prompt-injected or fails, the compromise is contained to that agent's scope and cannot automatically spread to sibling agents, orchestrators, or core systems.
- Enforce: I use deterministic code such as typed handoff schemas, explicit allowlists, approval gates, and policy checks to validate every cross-agent message and action request.

## ATB.1 Agent-to-Agent Trust Separation

Skill: Delegation boundary hardening.

Check:
- Outputs from one agent must never be treated as trusted instructions by another agent without relabeling and validation.
- Orchestrators must distinguish between trusted control metadata and untrusted task content in every handoff.

Action:
- Define a typed handoff contract for every agent boundary, including task, allowed tools, allowed data sources, and expected output shape.
- Strip or neutralize instruction-shaped text from worker output before it is inserted into another agent's prompt.
- Pass only the minimum required context to each sub-agent instead of full transcripts or broad planner state.
- Record which agent produced each intermediate artifact so trust boundaries remain auditable.

## ATB.2 Cross-Agent Action Containment

Skill: Privilege and blast-radius containment.

Check:
- A lower-trust agent must not be able to trigger privileged tools or approvals indirectly through a higher-trust orchestrator.
- Agent chaining must not create implicit trust transitivity where one approved step unlocks unrelated follow-on actions.

Action:
- Bind tool permissions to the receiving agent identity, not just to the overall workflow.
- Require deterministic re-authorization when a worker proposes a sensitive action, even if the planner already approved the broader task.
- Use separate credentials, memory stores, and execution sandboxes per agent role.
- Terminate or quarantine workflows when an agent produces policy-bypass attempts, unexplained delegation, or instruction-bearing output.

Minimum Output:
- Agent graph with trust levels, handoff edges, and tool permissions
- Cross-agent message schema and validation path
- Privilege inheritance and approval escalation risks
- Containment requirements for compromised planner or worker agents

Failure Modes:
- Planner summaries contain hidden instructions that silently steer worker agents
- Worker output is re-ingested as trusted policy or tool-routing logic
- One agent's broad permissions implicitly authorize sibling or downstream agents
- Shared credentials or shared memory collapse agent isolation

## References

- Read the base [tool-use-execution-security/SKILL.md](../tool-use-execution-security/SKILL.md) for tool-level authorization and sandbox controls.
- Read [core-llm-prompt-security/SKILL.md](../core-llm-prompt-security/SKILL.md) for instruction-boundary and output-validation controls.
- For severity wording, read [severity-and-reporting.md](../../references/severity-and-reporting.md).
