# Contributing

This repository is useful only if the guidance stays correct, small, and reusable.

## What To Contribute

- New base skills for missing AI security surfaces
- Framework subskills tied to a real framework or SDK
- Corrections to unsafe, vague, or outdated guidance
- Better validation, examples, and automation around the skills

## Contribution Rules

- Keep `SKILL.md` files focused and composable
- Prefer portable security controls before framework detail
- Every framework subskill must extend an existing base skill
- Cross-cutting non-framework skills may be added as companion skills when they support multiple bases or represent a standalone operational surface
- Do not add filler docs inside skill folders
- If a control can cause insecure implementations, rewrite it or remove it

## Skill Taxonomy

- Base skills define portable controls for a primary attack surface such as prompts, RAG, tools, or infrastructure.
- Companion skills cover cross-cutting or operational surfaces that do not fit cleanly under a single base skill. Examples include memory, governance, and data leakage.
- Framework subskills must extend exactly one base skill and should narrow that base to a concrete framework or provider surface.

## How To Place A New Skill

- If the skill is framework-specific, add it as a framework subskill and use `extends`.
- If the skill is cross-cutting across multiple bases, add it as a companion skill and use `supports`.
- If the skill introduces a new portable attack surface with controls that are not already captured by an existing base, add a new base skill.
- If you are unsure whether a new skill should be a base or companion skill, document the trust boundary it owns and choose the smallest category that keeps the controls reusable.

Examples:

- `browser-use-security` could extend `tool-use-execution-security` if it is narrowly about tool-driven UI actions.
- `memory-security` is a companion skill because it intersects retrieval, prompts, agents, and governance.
- `ai-governance-and-incident-response` is a companion skill because it governs releases, approvals, audit, and incident handling across the whole system.

## Pull Request Checklist

- Add or update the relevant `SKILL.md`
- Update `skills.json` when adding a skill
- Update `last_reviewed` metadata for any modified skill
- Update control severity metadata in `skills.json` when adding or changing controls
- Add or refresh adversarial fixtures when prompt-injection guidance changes
- Run `python3 scripts/validate_repo.py`
- Verify `./scripts/fetch-skill.sh <skill-id>` works
- Explain the concrete threat model or attack surface the change addresses

## Style

- Use explicit `Skill`, `Check`, and `Action` sections
- Prefer concrete controls over general advice
- Call out failure modes when misuse is plausible
- Treat incorrect guidance as a security bug, not a documentation nit
