---
name: llamaindex-rag-security
description: Review a LlamaIndex retrieval augmented generation stack for ingestion poisoning, node metadata loss, retriever scope failures, insecure query-engine composition, weak source attribution, and leakage through storage, memory, or observability layers.
last_reviewed: 2026-04-27
---

# LlamaIndex RAG Security

Use this skill when the target system uses LlamaIndex for ingestion, indexing, retrieval, query engines, agents, or postprocessing. This skill narrows the base `rag-security` controls to concrete LlamaIndex review points.

## Framework Focus

- Readers, parsers, node creation, embeddings, index construction, and storage context
- `RetrieverQueryEngine`, router query engines, agents, response synthesizers, and postprocessors
- Metadata filters, node references, citation support, memory, and observability paths

## Control Lens

- Validate: I check every piece of data coming into the system, including parsed nodes, metadata, storage context contents, retriever output, postprocessor changes, and synthesized response inputs.
- Scope: I define and enforce the boundaries of the LLM's knowledge and actions by limiting which nodes, indexes, query engines, and metadata scopes can contribute to an answer.
- Isolate: I ensure that if the LLM fails or is attacked, the failure is contained and cannot spread from poisoned nodes, broad query routing, or memory leakage into unrestricted access to the core system or data store.
- Enforce: I use deterministic code such as metadata validation, citation mapping, deletion checks, and schema-validated response handling instead of trusting the model or synthesizer to preserve boundaries on its own.

## 2.1 Source Grounding And Hallucination Mitigation In LlamaIndex

Skill: Node-level provenance verification and grounded synthesis review.

Check:
- Every factual claim must be tied back to the retrieved nodes actually selected by the retriever and synthesizer.
- Query engines must not produce answers from generic model prior knowledge when the requested mode is documentation-grounded.

Action:
- Inspect whether node metadata, source IDs, page references, and document provenance survive parsing and chunking.
- Review retriever and postprocessor configuration to confirm low-quality or cross-scope nodes are dropped before synthesis.
- Verify citation-enabled response paths still reference the exact nodes used after reranking or response condensation, and validate that mapping server-side.
- If the retrieved nodes are too weak or contradictory, require a documented refusal path instead of speculative output.

Failure Modes:
- Node parsing strips the metadata needed for citation and access control
- Router query engines send questions to a broad engine that ignores document scope
- Response synthesizers compress away the provenance needed for auditability

## 2.2 Data Leakage Prevention In LlamaIndex

Skill: Scoped node retrieval and masking before synthesis.

Check:
- Metadata filters must enforce tenant and document scope before nodes are returned from the index.
- Sensitive fields must be redacted before nodes are passed into synthesis, summarization, or agent tools.

Action:
- Review ingestion pipelines to confirm sensitive metadata is preserved, not dropped, during node parsing.
- Verify deletion, document refresh, and reindexing behavior so stale or quarantined nodes cannot be retrieved.
- Apply masking to node text and metadata before response synthesis or agent handoff.
- Treat storage context, cache layers, and observability integrations as potential leakage paths requiring separate access control.

Minimum Output:
- LlamaIndex ingestion and query-engine trust map
- Provenance and citation control points
- Filter, deletion, and masking gaps
- Required fixes for node metadata integrity and scoped synthesis

## References

- Read the base [rag-security/SKILL.md](../rag-security/SKILL.md) first for the shared control model.
- For leakage deep-dives, read [data-leakage-prevention/SKILL.md](../data-leakage-prevention/SKILL.md).
- For general framework notes, read [languages-and-frameworks.md](../../references/languages-and-frameworks.md).
