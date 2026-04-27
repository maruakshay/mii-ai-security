# Framework Mappings

Use this reference to translate repository skills into the control language that enterprise security and risk teams already use.

This crosswalk is directional, not canonical. OWASP and MITRE evolve over time, and some skills span multiple risks or techniques.

## Skill Crosswalk

| Skill ID | OWASP LLM Top 10 Alignment | MITRE ATLAS Alignment |
| --- | --- | --- |
| `core-llm-prompt-security` | `LLM01 Prompt Injection`, `LLM02 Insecure Output Handling` | Prompt injection, guardrail bypass, unsafe downstream execution |
| `indirect-prompt-injection` | `LLM01 Prompt Injection`, `LLM06 Sensitive Information Disclosure` | Prompt injection from external sources, indirect prompt injection flows |
| `rag-security` | `LLM06 Sensitive Information Disclosure`, `LLM09 Overreliance` | Prompt injection through retrieved data, data poisoning, scope bypass |
| `data-leakage-prevention` | `LLM06 Sensitive Information Disclosure` | Exfiltration and unauthorized disclosure pathways |
| `tool-use-execution-security` | `LLM02 Insecure Output Handling`, `LLM07 Insecure Plugin Design`, `LLM08 Excessive Agency` | Unsafe action execution, privilege escalation, exfiltration via tool or API use |
| `agentic-trust-boundaries` | `LLM07 Insecure Plugin Design`, `LLM08 Excessive Agency` | Prompt injection across agents, trust transitivity, chained action escalation |
| `memory-security` | `LLM01 Prompt Injection`, `LLM06 Sensitive Information Disclosure`, `LLM08 Excessive Agency` | Persistent poisoning, cross-session influence, mis-scoped retrieval from memory |
| `multimodal-security` | `LLM01 Prompt Injection`, `LLM06 Sensitive Information Disclosure` | Prompt injection through multimedia or OCR-derived content |
| `model-supply-chain-security` | `LLM03 Training Data Poisoning`, `LLM05 Supply Chain Vulnerabilities`, `LLM10 Model Theft` | Poison training data, model exposure, model theft or inference-based extraction |
| `system-infrastructure-security` | `LLM04 Model Denial of Service`, `LLM05 Supply Chain Vulnerabilities` | Resource exhaustion, access-control drift, model or environment exposure |
| `ai-governance-and-incident-response` | `LLM05 Supply Chain Vulnerabilities`, `LLM08 Excessive Agency`, `LLM09 Overreliance` | Detection, containment, rollback, and forensic reconstruction after AI incidents |
| `dspy-program-security` | `LLM01 Prompt Injection`, `LLM02 Insecure Output Handling`, `LLM09 Overreliance` | Poisoned optimization data, unsafe wrapper execution, evaluation contamination |
| `haystack-rag-security` | `LLM06 Sensitive Information Disclosure`, `LLM09 Overreliance` | Retrieved-context poisoning, pipeline branch expansion, store-scope bypass |
| `langchain-rag-security` | `LLM06 Sensitive Information Disclosure`, `LLM07 Insecure Plugin Design`, `LLM09 Overreliance` | Prompt injection via chains or memory, unsafe tool or retriever composition |
| `llamaindex-rag-security` | `LLM06 Sensitive Information Disclosure`, `LLM09 Overreliance` | Node poisoning, metadata loss, query-engine scope drift |
| `semantic-kernel-tool-security` | `LLM07 Insecure Plugin Design`, `LLM08 Excessive Agency` | Plugin abuse, planner escalation, unsafe connector invocation |
| `openai-responses-tool-file-security` | `LLM07 Insecure Plugin Design`, `LLM08 Excessive Agency`, `LLM06 Sensitive Information Disclosure` | Hosted-tool misuse, file-search scope failures, unsafe state carryover |
| `openai-assistants-legacy-security` | `LLM07 Insecure Plugin Design`, `LLM08 Excessive Agency`, `LLM06 Sensitive Information Disclosure` | Thread or run state leakage, hosted-tool misuse, attachment scope failures |

## Notes

- Use this document for governance conversations, audit packaging, and control rationales.
- If a formal compliance deliverable depends on exact framework wording, re-validate the mapping against the current official OWASP and MITRE publications.
