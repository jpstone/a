# US-20: Migration

Derived from: [20. Migration](../agentic-redesign-references.md#us-20-source)

## Problem

Existing Spec Guard artifacts need safe migration into the redesigned schemas and lifecycle without losing auditability.

## User story

As a existing project maintainer, I want migration implemented, so that existing Spec Guard artifacts need safe migration into the redesigned schemas and lifecycle without losing auditability.

## In scope

- Migrate existing artifacts and decisions where possible.
- Preserve historical audit data.
- Mark missing or unverifiable required fields with diagnostics.
- Require renewed approval where redesigned approval binding cannot be reconstructed.

## Out of scope

- Silently treating legacy approvals as valid when required snapshot/field binding is absent.
- Discarding historical decisions or evidence during migration.

## Acceptance criteria

- [ ] Migration reads legacy artifacts and writes redesigned schema-compatible artifacts.
- [ ] Historical decisions/evidence are preserved or referenced.
- [ ] Missing required redesigned fields produce diagnostics.
- [ ] Approvals that cannot be proven against required snapshots/fields are marked stale or require renewed gates.
- [ ] Migration results are visible through normal action results and viewer data.
