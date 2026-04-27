---
name: model-supply-chain-security
description: Review a model acquisition and deployment pipeline for poisoned base models, unsafe fine-tunes, trojaned adapters, unverifiable provenance, weak artifact integrity, and overtrust in third-party model documentation.
last_reviewed: 2026-04-27
---

# Model Supply Chain Security

Use this skill when the system depends on third-party base models, hosted model APIs, fine-tuned checkpoints, adapters, quantized variants, or internally trained derivatives. The model artifact itself is part of the trusted computing base and deserves dedicated review.

## Control Lens

- Validate: I check every piece of data coming into the system, including model artifacts, adapter weights, tokenizer files, evaluation baselines, and vendor metadata.
- Scope: I define and enforce the boundaries of which model artifacts are approved for which environments, tasks, and data classes.
- Isolate: I ensure that if a model artifact is poisoned, backdoored, or low-trust, the failure is contained to a limited environment and cannot silently become the default for production workloads.
- Enforce: I use deterministic code and release controls such as allowlisted artifact sources, checksums, signed manifests, gated deployment, and evaluation thresholds before a model becomes runnable.

## MSC.1 Model Provenance and Integrity

Skill: Artifact trust verification.

Check:
- Every deployed model artifact must have a traceable source, version, and integrity record.
- Teams must not rely on a model card or vendor description alone as proof of safety or fitness.

Action:
- Maintain an approved model registry with exact artifact digests, release source, owner, and intended use.
- Verify checksums or signatures before loading model weights, adapters, tokenizers, and auxiliary files.
- Separate experimental, staging, and production model registries so unreviewed artifacts cannot drift into production.
- Record which application version used which model artifact for incident response and rollback.

## MSC.2 Backdoor and Trojan Exposure Review

Skill: Behavioral gatekeeping before deployment.

Check:
- Fine-tuned, instruction-tuned, or vendor-provided models must be tested for hidden triggers, unsafe refusal drift, and task-specific backdoor behavior before promotion.
- Model swaps must not bypass evaluation simply because the API surface remains the same.

Action:
- Run evaluation suites that include trigger-style prompts, refusal checks, and representative abuse cases for the target workload.
- Compare candidate model behavior against a known-good baseline for safety-critical tasks and tool-calling paths.
- Gate production rollout on deterministic pass criteria rather than ad hoc human impressions.
- Restrict sensitive workloads to approved model families and require explicit review for new vendors or new fine-tunes.

Minimum Output:
- Model inventory with provenance, digest, owner, and deployment environment
- Promotion workflow from candidate to production
- Safety and backdoor evaluation coverage
- Rollback path for compromised or low-trust model artifacts

Failure Modes:
- A poisoned fine-tune inherits production trust because it matches the expected API
- Tokenizer, adapter, or sidecar artifact changes behavior without triggering review
- Third-party model documentation is treated as evidence of safety
- Emergency model swaps bypass regression and security evaluation

## References

- Read [system-infrastructure-security/SKILL.md](../system-infrastructure-security/SKILL.md) for runtime and deployment guardrails.
- Read [core-llm-prompt-security/SKILL.md](../core-llm-prompt-security/SKILL.md) for behavior-level validation after model selection.
- For severity wording, read [severity-and-reporting.md](../../references/severity-and-reporting.md).
