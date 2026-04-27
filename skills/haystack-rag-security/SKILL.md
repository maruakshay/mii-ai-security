---
name: haystack-rag-security
description: Review a Haystack retrieval pipeline for router scope failures, insecure document-store access, weak grounding, metadata-filter bypass, and leakage through pipeline components or evaluators.
last_reviewed: 2026-04-27
---

# Haystack RAG Security

Use this skill when the target system uses Haystack pipelines, routers, retrievers, document stores, generators, or evaluators in a RAG workflow. This skill narrows the base `rag-security` controls to concrete Haystack review points.

## Framework Focus

- Pipelines, routers, retrievers, rankers, generators, and evaluators
- Document stores, metadata filters, ingestion, and update paths
- Pipeline component wiring, intermediate outputs, and observability

## Control Lens

- Validate: I check every piece of data coming into the system, including documents, metadata filters, router decisions, retrieved documents, and generator inputs.
- Scope: I define and enforce the boundaries of which document-store records, pipelines, and components can influence a response for a given user or task.
- Isolate: I ensure that if one pipeline branch is poisoned or over-broad, the failure is contained and cannot silently expose unrelated stores, components, or data domains.
- Enforce: I use deterministic code such as document-store filters, pipeline validation, citation checks, and typed component contracts to constrain Haystack behavior.

## 2.1 Source Grounding and Pipeline Boundary Review In Haystack

Skill: Pipeline-level grounding and provenance review.

Check:
- Every factual answer must be traceable to the retrieved documents actually passed through the Haystack pipeline.
- Routers and pipeline branches must not broaden trust boundaries or allow generator-only answers when the mode is supposed to be grounded.

Action:
- Inspect component wiring to confirm retrieved document provenance survives through ranking and generation.
- Verify router logic cannot send queries to broader or less-trusted branches without explicit policy.
- Validate that evaluators and debugging outputs do not mask when answers lack grounded evidence.
- Require a refusal or fallback response when retrieval confidence is weak or contradictory.

## 2.2 Scoped Retrieval and Store Isolation In Haystack

Skill: Document-store and filter hardening.

Check:
- Document-store access must enforce tenant, sensitivity, and collection scope before retrieval results are returned to the pipeline.
- Retrieved documents must be masked or filtered before they reach the generator when they contain restricted content.

Action:
- Review document-store filter construction and ensure it is enforced server-side.
- Preserve provenance and sensitivity metadata across ingestion, updates, and reindexing.
- Prevent pipeline components from reading broad stores when a narrower collection was intended.
- Treat evaluator datasets, traces, and intermediate pipeline state as sensitive stores requiring separate controls.

Minimum Output:
- Haystack pipeline and document-store trust map
- Router and branch-expansion risks
- Filter, provenance, and masking controls
- Required fixes for scoped retrieval and grounded generation

## References

- Read the base [rag-security/SKILL.md](../rag-security/SKILL.md) first for the shared control model.
- For leakage deep-dives, read [data-leakage-prevention/SKILL.md](../data-leakage-prevention/SKILL.md).
- For general framework notes, read [languages-and-frameworks.md](../../references/languages-and-frameworks.md).
