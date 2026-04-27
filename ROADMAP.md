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

- `browser-use-security`
  Focus: browser automation, computer-use flows, DOM injection, session token exposure, and confirmation bypass in UI-driven agents.
  Status: planned, unowned.
  Starter deliverables: one subskill extending `tool-use-execution-security`, one fixture set for DOM or page-content injection, and one example trust-boundary diagram.

- `remote-mcp-security`
  Focus: remote MCP server trust, connector authorization, tool discovery scoping, and data exfiltration through third-party capability servers.
  Status: planned, unowned.
  Starter deliverables: one base skill covering server allowlisting, connector scoping, and tool result validation.

- `fine-tuning-and-eval-data-security`
  Focus: fine-tuning corpus hygiene, evaluation-set leakage, benchmark contamination, labeling trust, and reuse of production data in model improvement loops.
  Status: planned, unowned.
  Starter deliverables: one base skill and one reference note covering dataset provenance, retention, and poisoning checks.

### Tooling Investments

- `red-team-scripts`
  Focus: runnable attack and mitigation demos, starting with prompt-injection bypasses and regression fixtures.
  Status: planned, unowned.
  Starter deliverables: a script contract, a small runner that loads `tests/adversarial-fixtures/*.json`, and one end-to-end example.

## Currently Unowned Surfaces

- Public-incident-backed indirect prompt injection case library
- Dedicated multimodal red-team fixture corpus
- Model backdoor evaluation automation
- Runnable red team automation beyond static fixtures

## Contribution Guidance

- If you add a planned skill, move it from `Planned Skills` to `Shipped`.
- If you partially cover an unowned surface in an existing skill, note the gap explicitly and keep the roadmap entry until the surface has a dedicated owner.
- If a roadmap item depends on public incidents or external references, add citations in the skill draft before treating the guidance as complete.
- If you pick up `red-team-scripts`, follow the interface documented in [red-team-scripts/README.md](red-team-scripts/README.md).
