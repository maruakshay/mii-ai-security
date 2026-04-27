# mii-ai-security

Security-focused `SKILL.md` packs for reviewing and hardening LLM systems.

This repo is meant to be simple to use:

- fetch a skill
- apply its checks to a codebase or design
- use the references, fixtures, and validator to keep contributions consistent

## What’s In Scope

The repository currently ships 18 skills across four buckets:

- Base skills: prompts, RAG, tools, and system infrastructure
- Companion skills: memory, governance, leakage, agentic trust boundaries, multimodal, model supply chain, and indirect prompt injection
- Framework subskills: LangChain, LlamaIndex, Haystack, DSPy, Semantic Kernel, and OpenAI-hosted APIs
- Test and reference material: adversarial fixtures, severity guidance, framework notes, and OWASP or MITRE-aligned mappings

## Quick Start

List skills:

```bash
./scripts/list-skills.sh
```

Fetch a skill:

```bash
./scripts/fetch-skill.sh rag-security
```

Validate the repo:

```bash
python3 scripts/validate_repo.py
```

## Recommended Starting Points

- Prompt and input security: `core-llm-prompt-security`
- Retrieval security: `rag-security`
- Tool and agent execution: `tool-use-execution-security`
- Enterprise operations: `ai-governance-and-incident-response`

Then add framework depth as needed:

- `langchain-rag-security`
- `llamaindex-rag-security`
- `haystack-rag-security`
- `dspy-program-security`
- `semantic-kernel-tool-security`
- `openai-responses-tool-file-security`

## Repository Layout

```text
skills/
references/
tests/adversarial-fixtures/
red-team-scripts/
scripts/
skills.json
ROADMAP.md
```

## Key Docs

- [CONTRIBUTING.md](CONTRIBUTING.md): how to add or classify a skill
- [ROADMAP.md](ROADMAP.md): what is shipped and what is still unowned
- [references/framework-mappings.md](references/framework-mappings.md): directional OWASP LLM and MITRE ATLAS crosswalk
- [references/test-patterns.md](references/test-patterns.md): repeatable attack categories

## Repo Guarantees

- `skills.json` is the machine-readable index for automation
- every skill has `last_reviewed` metadata
- every listed control has a severity
- `python3 scripts/validate_repo.py` checks manifest consistency and adversarial fixtures

## License

Released under the [MIT License](LICENSE).
