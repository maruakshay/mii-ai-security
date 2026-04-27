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
- Do not add filler docs inside skill folders
- If a control can cause insecure implementations, rewrite it or remove it

## Pull Request Checklist

- Add or update the relevant `SKILL.md`
- Update `skills.json` when adding a skill
- Run `python3 scripts/validate_repo.py`
- Verify `./scripts/fetch-skill.sh <skill-id>` works
- Explain the concrete threat model or attack surface the change addresses

## Style

- Use explicit `Skill`, `Check`, and `Action` sections
- Prefer concrete controls over general advice
- Call out failure modes when misuse is plausible
- Treat incorrect guidance as a security bug, not a documentation nit
