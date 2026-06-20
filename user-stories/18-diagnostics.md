# US-18: Diagnostics

Derived from: [18. Diagnostics](../agentic-redesign-references.md#us-18-source)

## Problem

Governance failures need structured, actionable diagnostics so humans and agents can resolve blocked states without guessing.

## User story

As a agent operator, I want diagnostics implemented, so that governance failures need structured, actionable diagnostics so humans and agents can resolve blocked states without guessing.

## In scope

- Define diagnostic shape and severities.
- Emit diagnostics for readiness, validation, staleness, authority, snapshot, evidence, verifier, path, and lifecycle failures.
- Attach diagnostics to relevant artifacts/action results.

## Out of scope

- Silent failures.
- Unstructured prose-only errors when machine-readable diagnostics are required.

## Acceptance criteria

- [ ] Diagnostics include code, severity, message, field path, gate, and fix where applicable.
- [ ] Failed gates and validations return actionable diagnostics.
- [ ] Diagnostics identify stale approvals, snapshot mismatches, missing evidence, invalid verifier responses, disallowed file changes, and lifecycle blockers.
- [ ] Diagnostics are visible through CLI, MCP, viewer, and artifact state where applicable.
