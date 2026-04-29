# mii-ai-security

[![npm version](https://img.shields.io/npm/v/miii-security)](https://www.npmjs.com/package/miii-security)
[![npm downloads](https://img.shields.io/npm/dm/miii-security)](https://www.npmjs.com/package/miii-security)
[![GitHub](https://img.shields.io/github/stars/maruakshay/mii-ai-security?style=social)](https://github.com/maruakshay/mii-ai-security)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Security-focused `SKILL.md` packs for reviewing and hardening LLM systems.

Each skill is a self-contained review guide: a first principle, an attack mental model, a control lens table, named controls with Check/Action/Failure Mode sections, and a Quick Win. Fetch one, apply it to a codebase or design, ship the finding.

## Quick Start

Install via npm: [`miii-security`](https://www.npmjs.com/package/miii-security) · Source: [`maruakshay/mii-ai-security`](https://github.com/maruakshay/mii-ai-security)

```bash
# Add a skill to your project (copies to .claude/skills/<name>/SKILL.md)
npx miii-security add rag-security

# List all available skills
npx miii-security list

# Print a skill to stdout
npx miii-security show fine-tuning-security
```

## What's In Scope

41 skills across seven buckets:

| Bucket | Count | Coverage |
|---|---|---|
| Base | 4 | Prompts, RAG, tools, system infrastructure |
| Companion | 11 | Memory, governance, leakage, agentic trust, multimodal, model supply chain, indirect injection, fine-tuning, embedding attacks |
| Framework | 13 | LangChain, LlamaIndex, Haystack, DSPy, Semantic Kernel, OpenAI APIs, AutoGen, CrewAI, llamafile, Ollama, LiteLLM, Guardrails AI, NeMo Guardrails |
| Attack surface | 5 | Red-teaming, jailbreak taxonomy, adversarial robustness, model inversion, federated learning |
| Infra/ops | 5 | MLOps pipelines, GPU infrastructure, model serving, containers, secrets detection |
| Compliance/governance | 4 | Audit logging, red team programs, third-party model risk, AI privacy/PII |
| Test & reference | — | Adversarial fixtures, severity guidance, OWASP/MITRE mappings |

## Skill List

**Base**
- `core-llm-prompt-security`
- `rag-security`
- `tool-use-execution-security`
- `system-infrastructure-security`

**Companion**
- `data-leakage-prevention`
- `agentic-trust-boundaries`
- `memory-security`
- `model-supply-chain-security`
- `indirect-prompt-injection`
- `multimodal-security`
- `ai-governance-and-incident-response`
- `fine-tuning-security`
- `embedding-attack-security`

**Framework subskills**
- `langchain-rag-security`
- `llamaindex-rag-security`
- `haystack-rag-security`
- `dspy-program-security`
- `semantic-kernel-tool-security`
- `openai-responses-tool-file-security`
- `openai-assistants-legacy-security`
- `autogen-multiagent-security`
- `crewai-agent-security`
- `llamafile-local-model-security`
- `ollama-security`
- `litellm-proxy-security`
- `guardrails-ai-security`
- `nemo-guardrails-security`

**Attack surface**
- `prompt-injection-red-teaming`
- `jailbreak-taxonomy`
- `adversarial-robustness`
- `model-inversion-membership-inference`
- `federated-learning-security`

**Infra/ops**
- `mlops-pipeline-security`
- `gpu-infrastructure-security`
- `model-serving-security`
- `container-ai-workload-security`
- `secrets-in-prompts-detection`

**Compliance/governance**
- `ai-audit-logging`
- `ai-red-team-program`
- `third-party-model-risk`
- `ai-privacy-pii-compliance`

## Recommended Starting Points

New to AI security review — start here:

- `core-llm-prompt-security` — prompt injection and output validation
- `rag-security` — retrieval poisoning and boundary enforcement
- `tool-use-execution-security` — agent tool call authorization
- `ai-governance-and-incident-response` — enterprise ops baseline

Add framework depth:

- `langchain-rag-security`, `llamaindex-rag-security`, `haystack-rag-security`
- `autogen-multiagent-security`, `crewai-agent-security`
- `ollama-security`, `litellm-proxy-security`
- `guardrails-ai-security`, `nemo-guardrails-security`

Running a red team exercise:

- `prompt-injection-red-teaming` — methodology and CI integration
- `jailbreak-taxonomy` — technique catalog and detection signatures
- `adversarial-robustness` — input normalization and classifier hardening

Privacy and compliance review:

- `ai-privacy-pii-compliance` — GDPR/CCPA, DPIAs, data subject rights
- `ai-audit-logging` — tamper-proof event logging schema
- `third-party-model-risk` — vendor DPA, behavioral monitoring, fallback

## Repository Layout

```text
skills/                      41 SKILL.md files, one directory each
references/                  severity-and-reporting, test-patterns, framework-mappings
tests/adversarial-fixtures/  12 JSON fixtures for prompt injection variants
red-team-scripts/
scripts/validate_repo.py     manifest consistency and fixture checker
skills.json                  machine-readable skill index
```

## Repo Guarantees

- `skills.json` is the machine-readable index — every skill registered with controls and severity
- every skill has `last_reviewed` frontmatter
- every control has a severity (`critical`, `high`, `medium`, `low`)
- `python3 scripts/validate_repo.py` validates all 41 skills and fixtures

## Key Docs

- [CONTRIBUTING.md](CONTRIBUTING.md): how to add or classify a skill
- [ROADMAP.md](ROADMAP.md): what is shipped and what is planned
- [references/framework-mappings.md](references/framework-mappings.md): OWASP LLM Top 10 and MITRE ATLAS crosswalk
- [references/test-patterns.md](references/test-patterns.md): repeatable attack categories

## License

Released under the [MIT License](LICENSE).
