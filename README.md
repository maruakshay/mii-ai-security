# mii-ai-security

Open-source `SKILL.md` packs for teaching and operationalizing AI security across prompts, retrieval, tool execution, and governance.

This repository is built around one objective: help developers think like attackers, design like defenders, and ship LLM systems with controls that hold up in production.

## Why This Repo Exists

AI security guidance is often either too abstract to implement or too tied to one framework to reuse. `mii-ai-security` is intended to bridge that gap with practical security skills, reusable review checklists, and framework-aware hardening guidance.

The repo provides:

- foundational security skills for LLM applications
- framework-specific subskills for real stacks such as LangChain, LlamaIndex, Haystack, DSPy, Semantic Kernel, and OpenAI-hosted APIs
- dedicated skills for high-severity agentic surfaces such as multi-agent delegation, memory, indirect injection, and model supply chain risk
- a machine-readable index for automation and CI workflows, including control severity and review-date metadata
- lightweight scripts for fetching and validating skills
- canonical adversarial prompt-injection fixtures for repeatable testing

## The Five Pillars

### Pillar 1: Foundational Concepts and Threat Modeling

Goal: teach developers how to think like an attacker.

Skills covered:

- Attack surface mapping across API calls, RAG retrieval, system prompts, user input, and tool execution
- Threat modeling for LLM systems using adapted patterns such as STRIDE with AI-specific categories like prompt tampering
- Blast radius analysis so teams understand how a single weakness can become data leakage, privilege misuse, or unauthorized actions

Mapped skills:

- `core-llm-prompt-security`
- `system-infrastructure-security`

### Pillar 2: Input and Context Hardening

Goal: treat the prompt and all external inputs as untrusted code.

Skills covered:

- Input sanitization layers to catch obvious attack keywords, obfuscation, and structure-breaking payloads
- Instruction separation so user content cannot rewrite or mutate the system prompt
- Contextual guardrails that detect bypass attempts or self-modification requests
- Defense in depth using deterministic code controls instead of trusting the model to police itself

Mapped skills:

- `core-llm-prompt-security`
- `data-leakage-prevention`

### Pillar 3: Data Integrity and Context Management

Goal: ensure retrieved data is trustworthy, relevant, and properly scoped.

Skills covered:

- Source validation for retrieved documents, including provenance and freshness checks
- Access control enforcement before retrieval using RBAC or ABAC
- Data poisoning detection during ingestion into vector stores and retrieval pipelines
- Prompt grounding that requires citations and explicit abstention when context is insufficient

Mapped skills:

- `rag-security`
- `langchain-rag-security`
- `llamaindex-rag-security`

### Pillar 4: Execution Isolation and Structured Output

Goal: control what the model can do with the information it receives.

Skills covered:

- Principle of least privilege for tool access and execution environments
- Sandboxing of code execution, API invocation, and function-calling pathways
- Output schema enforcement with strict validation instead of trusting raw model JSON
- Input and output validation before any model-suggested action is executed
- Safe fallbacks when output is formally valid but still semantically unsafe

Mapped skills:

- `tool-use-execution-security`
- `semantic-kernel-tool-security`
- `agentic-trust-boundaries`

### Pillar 5: Testing, Monitoring, and Governance

Goal: make AI security continuous rather than a one-time review.

Skills covered:

- Red teaming with adversarial prompts, encoding tricks, structural evasions, and policy bypass attempts
- Observability for prompts, retrieved chunks, tool calls, outputs, and incidents
- Guardrail management with version control, peer review, and explicit change control
- Model versioning, promotion, and rollback procedures
- Approval workflows for guardrail and policy changes
- Audit-log requirements for regulated or high-assurance environments
- AI-specific incident response playbooks for prompt injection, leakage, unsafe actions, and model regressions

Mapped skills:

- `system-infrastructure-security`
- `data-leakage-prevention`
- `ai-governance-and-incident-response`
- `memory-security`
- `model-supply-chain-security`
- `multimodal-security`

## High-Severity Agentic Surfaces

The repository also covers attack surfaces that tend to become critical once systems move from single-model chat flows to agentic orchestration:

- `agentic-trust-boundaries`: multi-agent orchestration, trust transitivity, and agent-to-agent prompt injection
- `memory-security`: persistent memory poisoning, episodic memory stores, and long-term cross-session influence
- `model-supply-chain-security`: model provenance, fine-tune backdoors, poisoned model artifacts, and third-party trust
- `indirect-prompt-injection`: instructions arriving through documents, web pages, email, and API responses
- `multimodal-security`: adversarial images, OCR confusion, typographic attacks, and hidden visual instructions

## What You Get

Each skill is a focused `SKILL.md` with:

- clear `Skill`, `Check`, and `Action` sections
- failure modes and minimum expected outputs
- references for severity, testing, and cross-language review
- controls that can be reused across languages and deployment models
- a `last_reviewed` date in both frontmatter and `skills.json`

## Skill Map

| Skill ID | Focus |
| --- | --- |
| `core-llm-prompt-security` | Prompt injection defense, instruction separation, guardrails, output validation |
| `rag-security` | Grounding, retrieval scoping, citation discipline, source trust |
| `tool-use-execution-security` | Function authorization, schema validation, sandboxing, least privilege |
| `system-infrastructure-security` | Logging, auditing, throttling, runtime hardening, operational controls |
| `data-leakage-prevention` | Redaction, tenant isolation, retention, egress and observability leakage controls |
| `agentic-trust-boundaries` | Multi-agent trust separation, delegation safety, cross-agent containment |
| `memory-security` | Memory poisoning, retention, retrieval scope, persistent influence containment |
| `model-supply-chain-security` | Model provenance, backdoors, trojans, third-party model trust |
| `indirect-prompt-injection` | Untrusted content ingestion from documents, web, email, and APIs |
| `multimodal-security` | Vision/OCR trust boundaries, hidden text, adversarial image handling |
| `ai-governance-and-incident-response` | Model versioning, rollback, change approval, regulated audit logging, AI incident response |
| `dspy-program-security` | DSPy signature, optimizer, evaluation, and tool-wrapper hardening |
| `haystack-rag-security` | Haystack pipeline, router, retriever, and document-store controls |
| `langchain-rag-security` | LangChain-specific RAG attack surface and mitigations |
| `llamaindex-rag-security` | LlamaIndex-specific retrieval and context security controls |
| `semantic-kernel-tool-security` | Semantic Kernel plugin and tool execution hardening |
| `openai-responses-tool-file-security` | OpenAI Responses API tool-calling, file-search, and conversation-state hardening |
| `openai-assistants-legacy-security` | Legacy Assistants API thread, run, tool, and attachment isolation review |

## Quick Start

List available skills:

```bash
./scripts/list-skills.sh
```

Fetch a skill:

```bash
./scripts/fetch-skill.sh rag-security
```

Validate the repository:

```bash
python3 scripts/validate_repo.py
```

This validates:

- `skills.json` structure, control severity metadata, and `last_reviewed` dates
- `SKILL.md` frontmatter consistency
- adversarial fixture structure in `tests/adversarial-fixtures/`

Inspect the machine-readable index:

```bash
cat skills.json
```

## Example Learning Path

Start with the foundational controls, then move deeper into retrieval and execution risk.

```bash
./scripts/fetch-skill.sh core-llm-prompt-security
./scripts/fetch-skill.sh rag-security
./scripts/fetch-skill.sh tool-use-execution-security
```

Then add framework-specific depth where needed:

```bash
./scripts/fetch-skill.sh dspy-program-security
./scripts/fetch-skill.sh haystack-rag-security
./scripts/fetch-skill.sh langchain-rag-security
./scripts/fetch-skill.sh semantic-kernel-tool-security
./scripts/fetch-skill.sh openai-responses-tool-file-security
```

For agentic systems, add the dedicated high-severity surfaces early:

```bash
./scripts/fetch-skill.sh agentic-trust-boundaries
./scripts/fetch-skill.sh memory-security
./scripts/fetch-skill.sh indirect-prompt-injection
```

For enterprise production rollouts, add governance and operations controls:

```bash
./scripts/fetch-skill.sh ai-governance-and-incident-response
./scripts/fetch-skill.sh system-infrastructure-security
```

## Repository Layout

```text
skills/
  agentic-trust-boundaries/
  core-llm-prompt-security/
  rag-security/
  data-leakage-prevention/
  ai-governance-and-incident-response/
  dspy-program-security/
  haystack-rag-security/
  indirect-prompt-injection/
  memory-security/
  model-supply-chain-security/
  multimodal-security/
  openai-assistants-legacy-security/
  openai-responses-tool-file-security/
  tool-use-execution-security/
  system-infrastructure-security/
  langchain-rag-security/
  llamaindex-rag-security/
  semantic-kernel-tool-security/
references/
  languages-and-frameworks.md
  severity-and-reporting.md
  test-patterns.md
scripts/
  fetch-skill.sh
  list-skills.sh
  validate_repo.py
tests/
  adversarial-fixtures/
    *.json
skills.json
ROADMAP.md
```

## Design Principles

- Threat-model first, framework second
- Treat prompts and retrieved context as untrusted input
- Treat agent outputs, memories, and model artifacts as untrusted inputs too
- Use deterministic controls around model behavior
- Reduce blast radius through isolation and validation
- Make testing, monitoring, and governance part of the default workflow
- Treat model releases, prompt changes, and incident playbooks as security-controlled assets

## Scope

The skills are written to support:

- Python, JavaScript/TypeScript, Java, Go, Rust, C#, Ruby, and Kotlin
- LangChain, LlamaIndex, Semantic Kernel, Haystack, DSPy, OpenAI-hosted APIs, custom agent stacks, and direct SDK usage
- API, web, worker, batch, and self-hosted deployment patterns

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a PR. New skills should stay focused, composable, and tied to a concrete attack surface or operational control.

## Roadmap

Read [ROADMAP.md](ROADMAP.md) for planned skills, unowned attack surfaces, and larger investments that are not yet implemented in the repository.

## Security

If you find incorrect or unsafe guidance in this repository, report it through [SECURITY.md](SECURITY.md). Unsafe security guidance is treated as a security issue.

## License

Released under the [MIT License](LICENSE).
