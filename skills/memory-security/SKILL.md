---
name: memory-security
description: Review an AI system for persistent memory poisoning, unsafe episodic or long-term memory writes, retrieval scope failures, stale or undeletable memory state, and cross-session influence over future model behavior.
last_reviewed: 2026-04-27
---

# Memory Security

Use this skill when the application stores conversational memory, episodic state, summaries, vectorized memories, task history, or user-specific long-term context. Memory turns a one-turn prompt injection into a persistence attack surface.

## Control Lens

- Validate: I check every piece of data coming into the system before it is written to memory, retrieved from memory, or merged into a future prompt.
- Scope: I define and enforce the boundaries of which users, sessions, tenants, and agent roles can read or write specific memory stores.
- Isolate: I ensure that if one memory item is poisoned or mis-scoped, the failure is contained and cannot persistently influence unrelated users, agents, or future sessions.
- Enforce: I use deterministic code such as memory write policies, typed memory records, retrieval filters, and deletion workflows rather than trusting the model to curate its own memory safely.

## MEM.1 Memory Write Validation

Skill: Safe persistence controls.

Check:
- The system must not write attacker-controlled instructions, secrets, or unverifiable claims into long-term memory without validation.
- Memory write rules must distinguish durable preferences from transient task content and malicious policy-shaped text.

Action:
- Apply a write gate that classifies candidate memory as preference, fact, task state, or rejectable content before persistence.
- Reject or quarantine instruction-bearing text such as future behavior directives, approval claims, or tool-routing suggestions.
- Attach provenance, timestamp, owner, and sensitivity metadata to every memory record.
- Require deterministic size, retention, and overwrite rules so memory cannot grow into an opaque policy channel.

## MEM.2 Persistent Influence Containment

Skill: Memory retrieval hardening and cleanup.

Check:
- Retrieved memory must be scoped to the current user, task, and agent role before it affects prompt assembly.
- Operators must be able to expire, delete, or quarantine poisoned or stale memory records.

Action:
- Enforce read filters on memory retrieval using tenant, user, session, agent, and sensitivity boundaries.
- Limit how many memory items can influence a prompt and require explicit labels showing memory provenance.
- Maintain deletion and reindex workflows so poisoned memory can be removed from live retrieval paths.
- Audit high-impact memory reads and writes, especially when memories affect tool use, approvals, or identity assumptions.

Minimum Output:
- Memory architecture map covering write paths, stores, retrieval, and deletion
- Write-validation and retrieval-scope controls
- Persistence and poisoning scenarios with cleanup strategy
- Cross-session and cross-agent isolation gaps

Failure Modes:
- A single malicious turn writes persistent instructions that shape many future sessions
- Old or quarantined memory remains retrievable through caches, summaries, or embeddings
- Shared memory causes cross-user or cross-agent influence
- The model decides what to remember without external policy checks

## References

- Read [data-leakage-prevention/SKILL.md](../data-leakage-prevention/SKILL.md) for retention, redaction, and tenant-isolation controls.
- Read [rag-security/SKILL.md](../rag-security/SKILL.md) for scoped retrieval and provenance handling.
- For severity wording, read [severity-and-reporting.md](../../references/severity-and-reporting.md).
