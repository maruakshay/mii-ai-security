---
name: langchain-rag-security
description: Review a LangChain retrieval augmented generation stack for document poisoning, retriever scope failures, insecure chain composition, weak citation grounding, metadata filter bypass, and leakage from callbacks, memory, or intermediate steps.
---

# LangChain RAG Security

Use this skill when the target system uses LangChain retrievers, chains, agents, memory, or callback handlers in a RAG flow. This skill narrows the base `rag-security` controls to concrete LangChain review points.

## Framework Focus

- `Retriever`, `VectorStoreRetriever`, and hybrid retriever configuration
- `ConversationalRetrievalChain`, `RetrievalQA`, LCEL graphs, and custom chain composition
- Document loaders, text splitters, embeddings, vector stores, rerankers, and callback handlers
- Memory, chat history injection, intermediate steps, and tracing outputs

## 2.1 Source Grounding And Hallucination Mitigation In LangChain

Skill: Citation verification, retriever validation, and chain-boundary review.

Check:
- Every factual claim must be traceable to the retrieved `Document` objects that were actually passed into the answering prompt.
- Chains must not answer from prior chat history, memory, or agent scratchpad when the configured mode is supposed to be grounded only in retrieval.

Action:
- Inspect how retrieved documents are transformed before prompt assembly and confirm citations survive template rendering.
- Verify emitted citations against the exact `Document` objects returned by the retriever instead of trusting citation-shaped model output.
- Verify `k`, score thresholds, metadata filters, and reranker settings do not over-broaden context.
- Ensure callback handlers and tracing do not hide when the final answer used documents outside the intended retriever result set.
- If retrieval confidence is weak, require a fallback response instead of speculative completion.

Failure Modes:
- `chat_history` or memory silently overrides retrieved evidence
- Custom prompt templates omit document provenance
- Intermediate chain steps mix tool output and retrieved context without trust labels

## 2.2 Data Leakage Prevention In LangChain

Skill: Scoped retrieval and sensitive-context masking.

Check:
- Vector store queries must respect tenant, project, document class, and sensitivity filters before any `Document` objects are returned.
- Retrieved content must be screened for PII or secrets before insertion into the final LangChain prompt.

Action:
- Review metadata filter construction for every vector store backend and verify user scope is enforced server-side, not only in prompt text.
- Confirm document loaders and splitters preserve provenance and sensitivity metadata across chunking.
- Mask PII in retrieved chunks before they enter `combine_documents` or equivalent synthesis logic.
- Treat callback logs, LangSmith traces, and debugging views as sensitive stores; store identifiers, policy outcomes, and redacted summaries by default instead of raw prompts or raw document text.

Minimum Output:
- LangChain RAG dataflow from loader to final chain output
- Filter, citation, and confidence controls by component
- Memory and callback leakage risks
- Required fixes for retriever scoping, masking, and grounded fallback

## References

- Read the base [rag-security/SKILL.md](../rag-security/SKILL.md) first for the shared control model.
- For leakage deep-dives, read [data-leakage-prevention/SKILL.md](../data-leakage-prevention/SKILL.md).
- For general framework notes, read [languages-and-frameworks.md](../../references/languages-and-frameworks.md).
