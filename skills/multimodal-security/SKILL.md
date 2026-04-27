---
name: multimodal-security
description: Review a multimodal AI system for adversarial images, OCR prompt injection, hidden text, typographic attacks, unsafe visual grounding, and vision-to-action trust-boundary failures.
last_reviewed: 2026-04-27
---

# Multimodal Security

Use this skill when the system accepts images, screenshots, PDFs, scanned forms, diagrams, or other visual inputs that influence reasoning or actions. Visual content creates new injection and evasion paths that text-only controls do not fully cover.

## Control Lens

- Validate: I check every piece of data coming into the system, including images, OCR text, embedded metadata, extracted captions, and any model-produced visual interpretation.
- Scope: I define and enforce the boundaries of what visual input is allowed to influence, which extracted text is trusted as evidence, and whether visual content can ever trigger tools or sensitive decisions.
- Isolate: I ensure that if a visual input contains hidden or adversarial instructions, the failure is contained to a labeled untrusted context and cannot directly reach privileged tools, memory, or core data stores.
- Enforce: I use deterministic code such as file-type checks, OCR review pipelines, output schemas, and policy gates instead of trusting raw multimodal model interpretation.

## MM.1 Image and OCR Input Validation

Skill: Visual-input hardening.

Check:
- Uploaded images and extracted OCR text must be treated as untrusted input regardless of source.
- The system must account for hidden text, typographic manipulation, overlays, and misleading OCR output.

Action:
- Validate file type, size, dimensions, and preprocessing path before images enter the model pipeline.
- Separate raw image storage from OCR text and preserve provenance linking between them.
- Flag inputs where OCR text contains instruction-like phrases, policy overrides, or action requests.
- Require manual review or a safer fallback path when extracted content is low-confidence or visually ambiguous.

## MM.2 Multimodal Instruction Boundary Enforcement

Skill: Vision-to-action containment.

Check:
- Content seen in an image must not directly authorize tool calls, approvals, or identity assumptions.
- Visual grounding must remain evidence-oriented rather than instruction-oriented.

Action:
- Treat OCR and caption output exactly like other untrusted retrieved content when assembling prompts.
- Require deterministic validation before any action based on image-derived data, especially identity, payment, or access-control decisions.
- Prevent screenshots, diagrams, or embedded text from mutating system prompt behavior or long-term memory directly.
- Log when visual content attempts to influence tools, memory, or policy decisions.

Minimum Output:
- Multimodal intake map covering upload, preprocessing, OCR, reasoning, and action paths
- Validation controls for image artifacts and OCR text
- Vision-to-tool and vision-to-memory containment strategy
- Known ambiguity and fallback requirements

Failure Modes:
- Hidden text in an image injects instructions into the prompt
- OCR errors create false approvals, identities, or commands
- The model treats diagrams or screenshots as trusted policy rather than untrusted evidence
- Visual content silently reaches tools or memory without deterministic validation

## References

- Read [core-llm-prompt-security/SKILL.md](../core-llm-prompt-security/SKILL.md) for trust-boundary and output-validation controls.
- Read [data-leakage-prevention/SKILL.md](../data-leakage-prevention/SKILL.md) for image-derived sensitive data handling.
- For severity wording, read [severity-and-reporting.md](../../references/severity-and-reporting.md).
