---
name: rag-security
description: Review a retrieval augmented generation system for ingestion poisoning, retrieval boundary failures, insecure chunking and metadata handling, document trust confusion, and cross-tenant or stale-context exposure across any language or framework.
---

# Retrieval Augmented Generation Security

Use this skill when the system indexes content, performs retrieval, or grounds model responses on external knowledge. This section addresses vulnerabilities introduced by vector stores, databases, and external corpora.

## 2.1 Source Grounding And Hallucination Mitigation

Skill: Citation verification and confidence scoring.

Check:
- Every factual claim made by the LLM must be directly traceable to a retrieved document chunk.
- The system must detect when retrieval quality is too weak to support a grounded answer.

Action:
- Citation mandate: require the LLM to emit citations in the response format, for example `[Source: Doc_A, p. 3]`.
- Server-side verification: validate every emitted citation against the actual retrieved chunk set and reject citations that do not map to the retrieved evidence.
- Confidence scoring: implement a score that penalizes answers when retrieved chunks are highly disparate, low relevance, stale, or contradictory.
- If grounding fails, the required response is: `I cannot answer this question with the provided documentation.`

Failure Mode:
- If the answer cannot be grounded to retrieved evidence, do not allow the model to improvise.
- Do not treat citation-shaped text as proof of grounding unless the application verifies it against the retrieved source set.

## 2.2 Data Leakage Prevention (The Gatekeeper)

Skill: Access control and data masking.

Check:
- The system must only retrieve data relevant to the user's explicit query scope.
- Retrieved source chunks must be screened for PII and other restricted data before they are exposed to the model.

Action:
- Query rewriting: before querying the vector store, rewrite the request into precise scoped filters such as `user_department=HR` or `document_type=Policy`.
- PII masking: implement a final masking layer that redacts or masks PII in retrieved chunks before they are passed to the LLM.
- Enforce authorization at retrieval time and again when assembling the prompt context.

Minimum Output:
- RAG dataflow with ingestion, indexing, retrieval, reranking, and prompt assembly boundaries
- Citation and confidence policy
- Query-scoping and masking controls
- Clear fallback behavior when grounding or scope enforcement fails

Best Practice:
- Preserve provenance and sensitivity metadata through the full pipeline.
- Treat uploaded and indexed documents as untrusted until validated and attributed.

## References

- For stack-specific review notes, read [languages-and-frameworks.md](../../references/languages-and-frameworks.md).
- For severity wording, read [severity-and-reporting.md](../../references/severity-and-reporting.md).
- For repeatable attack cases, read [test-patterns.md](../../references/test-patterns.md).
- For deeper leakage controls outside retrieval, read [data-leakage-prevention/SKILL.md](../data-leakage-prevention/SKILL.md).
