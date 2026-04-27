# Languages And Frameworks

Use this reference when the assessment needs stack-specific examples or attack surfaces.

## Languages

- Python: inspect agent loops, template rendering, unsafe deserialization, notebook execution, subprocess wrappers, and broad SDK usage.
- JavaScript/TypeScript: inspect tool routers, server actions, untrusted prompt composition, eval-like behavior, browser extensions, and SSR boundaries.
- Java/Kotlin: inspect orchestration layers, HTTP clients, prompt builders, policy enforcement, and enterprise connector boundaries.
- Go: inspect CLI wrappers, RPC boundaries, shell bridging, retrieval middleware, and secret handling in config structs.
- Rust: inspect sandbox boundaries, plugin execution, command wrappers, and explicit capability grants.
- C#: inspect Semantic Kernel planners, plugin registration, connector permissions, and tenant isolation paths.
- Ruby: inspect Rails controllers, background jobs, prompt templates, and shell/database bridge code.

## Frameworks

- LangChain: review retrievers, tools, memory, callback handlers, output parsers, and chain composition.
- LlamaIndex: review document ingestion, node parsers, retrievers, query engines, metadata filters, and postprocessors.
- Semantic Kernel: review plugin imports, planner behavior, function calling, memory connectors, and policy hooks.
- Haystack: review pipelines, routers, retrievers, document stores, and evaluators.
- DSPy: review optimizer datasets, prompt programs, tool wrappers, and evaluation leakage.
- OpenAI Responses API: review hosted tools, file search, conversation state, function calling, and tool-loop controls.
- OpenAI Assistants API: review legacy threads, runs, attachments, and migration risk for deprecated integrations.
- Custom SDK implementations: map inputs, prompts, model calls, tools, outputs, storage, and audit logs.

## Related Skills

- Prompt and output boundaries: `core-llm-prompt-security`, `indirect-prompt-injection`, `multimodal-security`
- Retrieval and context scoping: `rag-security`, `langchain-rag-security`, `llamaindex-rag-security`, `haystack-rag-security`
- Tooling and agent execution: `tool-use-execution-security`, `semantic-kernel-tool-security`, `openai-responses-tool-file-security`, `openai-assistants-legacy-security`, `agentic-trust-boundaries`
- Program and optimization safety: `dspy-program-security`, `memory-security`
- Operations and governance: `system-infrastructure-security`, `model-supply-chain-security`, `ai-governance-and-incident-response`

## Portable Review Questions

- Where is untrusted content first accepted?
- Where is it transformed into model-visible context?
- Where can the model trigger actions?
- What data can cross tenant or trust boundaries?
- What controls fail closed versus fail open?
