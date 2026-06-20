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

<!-- Expanded from agentic-redesign.md to provide behavior-level coverage. -->

- [ ] AC-20-001: When reading existing artifacts, Spec Guard must:
- [ ] AC-20-002: reject future writes that omit required canonical fields,
- [ ] AC-20-003: never fabricate human decisions,
- [ ] AC-20-004: never fabricate backend verification records,
- [ ] AC-20-005: Migration must not create verifier records that judge human-approved content.
- [ ] AC-20-006: Enumerated item is supported/enforced: migrate known synonymous fields into canonical fields,
- [ ] AC-20-007: Enumerated item is supported/enforced: preserve raw legacy values where useful,
- [ ] AC-20-008: Enumerated item is supported/enforced: reject future writes that omit required canonical fields,
- [ ] AC-20-009: Enumerated item is supported/enforced: warn on boilerplate generated scope without silently deleting it,
- [ ] AC-20-010: Enumerated item is supported/enforced: reconstruct parent/child links when possible,
- [ ] AC-20-011: Enumerated item is supported/enforced: leave optional intent fields empty unless drafted,
- [ ] AC-20-012: Enumerated item is supported/enforced: never fabricate human decisions,
- [ ] AC-20-013: Enumerated item is supported/enforced: never fabricate backend verification records,
- [ ] AC-20-014: Enumerated item is supported/enforced: invalidate approvals when migration changes approved semantics.
