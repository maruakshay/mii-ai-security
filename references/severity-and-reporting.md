# Severity And Reporting

Use this reference to normalize findings across skills.

## Severity Guide

- Critical: direct unauthorized action, tenant breakout, privileged secret disclosure, or remote execution with weak preconditions.
- High: reliable prompt injection, data exfiltration path, policy bypass, or unsafe tool execution requiring moderate preconditions.
- Medium: partial context poisoning, missing validation, overbroad permissions, or leakage limited by compensating controls.
- Low: hardening gap, weak observability, incomplete documentation, or control drift without clear exploit evidence.

## Minimum Finding Format

- Title
- Severity
- Affected component
- Preconditions
- Exploit path
- Impact
- Evidence
- Recommended fix
- Residual risk

## Evidence Expectations

- Include the exact trust boundary crossed.
- Name the vulnerable prompt, retriever, tool, connector, API, or infrastructure component.
- Prefer concrete attack steps over generic warnings.

## Operational Finding Hints

- Treat missing rollback for model or guardrail changes as at least `High` when production impact is plausible.
- Treat audit-log gaps that block forensic reconstruction or regulated review as at least `High`.
- Treat unsafe agent-to-agent privilege spread or unbounded tool autonomy as `Critical` when they can trigger direct actions.
- Treat unmanaged memory persistence as `High` or `Critical` depending on whether it can create durable cross-session influence.
