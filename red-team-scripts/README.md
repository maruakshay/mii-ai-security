# Red Team Scripts

This directory is the starter home for runnable attack and regression scripts.

The goal is not to replace `tests/adversarial-fixtures/`. The goal is to turn those fixtures into executable checks that teams can run against a live integration, a local wrapper, or a staging environment.

## Expected Interface

Every runnable red-team script should:

1. Load one or more fixtures from `tests/adversarial-fixtures/*.json`.
2. Send the fixture payload to a target adapter that represents the system under test.
3. Record the observed behavior in a structured result.
4. Exit non-zero when the system violates the expected behavior.

## Minimum Output Contract

Each script should emit machine-readable results containing:

- `fixture_id`
- `target`
- `result`
- `observed_behavior`
- `expected_behavior`
- `notes`

## Suggested Layout

```text
red-team-scripts/
  README.md
  adapters/
  examples/
```

## First Deliverables

- A minimal runner that iterates over `tests/adversarial-fixtures/*.json`
- One adapter contract for sending prompts to a target system
- One example script that demonstrates pass or fail behavior end to end

## Scope Guardrails

- Do not hardcode secrets, API keys, or tenant data in scripts.
- Treat all captured results as potentially sensitive.
- Keep the canonical attack corpus in `tests/adversarial-fixtures/`; do not create a second fixture source inside `red-team-scripts/`.
- Write captured results only to an ignored local path or external artifact store, not to a checked-in repository directory.
- Keep the first scripts deterministic and fixture-driven before adding autonomous attack logic.
