# US-25: Normative enums

Derived from: [Appendix C. Enums](../agentic-redesign-references.md#us-25-source)

## Problem

Shared enums must be fixed and consistent so validation, lifecycle, classification, evidence, docs policy, and changed-file category checks agree across components.

## User story

As a type-system implementer, I want normative enums implemented, so that shared enums must be fixed and consistent so validation, lifecycle, classification, evidence, docs policy, and changed-file category checks agree across components.

## In scope

- Implement WorkClassification, WorkStatus, PlanStatus, VerificationStatus, EvidenceStatus, DocsPolicy, and ChangeFileCategory.
- Use enum values consistently in schemas, actions, diagnostics, and viewer data.

## Out of scope

- Ad hoc string statuses not listed in the normative enums.
- Interface-specific enum aliases that break schema/action parity.

## Acceptance criteria

- [ ] All enum values from Appendix C are supported exactly.
- [ ] Schema and action validation rejects unsupported enum values.
- [ ] Lifecycle and readiness checks use the normative status enums.
- [ ] File-change classification uses the normative ChangeFileCategory values.
- [ ] Viewer/CLI/MCP render enum values without changing their stored canonical representation.
