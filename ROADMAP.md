# Roadmap

This roadmap tracks what is already covered, what is planned, and which security surfaces are currently unowned in `mii-ai-security`.

## Shipped

- `agentic-trust-boundaries`
- `ai-governance-and-incident-response`
- `core-llm-prompt-security`
- `indirect-prompt-injection`
- `rag-security`
- `memory-security`
- `model-supply-chain-security`
- `multimodal-security`
- `tool-use-execution-security`
- `system-infrastructure-security`
- `data-leakage-prevention`
- `dspy-program-security`
- `haystack-rag-security`
- `langchain-rag-security`
- `llamaindex-rag-security`
- `openai-assistants-legacy-security`
- `openai-responses-tool-file-security`
- `semantic-kernel-tool-security`

## Planned Skills

### High Priority

### Tooling Investments

- `red-team-scripts`
  Focus: runnable attack and mitigation demos, starting with prompt-injection bypasses and regression fixtures.
  Status: planned, unowned.

## Currently Unowned Surfaces

- Public-incident-backed indirect prompt injection case library
- Dedicated multimodal red-team fixture corpus
- Model backdoor evaluation automation
- Runnable red team automation beyond static fixtures

## Contribution Guidance

- If you add a planned skill, move it from `Planned Skills` to `Shipped`.
- If you partially cover an unowned surface in an existing skill, note the gap explicitly and keep the roadmap entry until the surface has a dedicated owner.
- If a roadmap item depends on public incidents or external references, add citations in the skill draft before treating the guidance as complete.
