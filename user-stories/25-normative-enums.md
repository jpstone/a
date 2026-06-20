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

<!-- Expanded from agentic-redesign.md to provide behavior-level coverage. -->

- [ ] AC-25-001: Enum `WorkClassification` is implemented as a fixed normative enum.
- [ ] AC-25-002: Enum `WorkClassification` includes value `reusable_api`.
- [ ] AC-25-003: Enum `WorkClassification` includes value `rest_api`.
- [ ] AC-25-004: Enum `WorkClassification` includes value `reusable_ui`.
- [ ] AC-25-005: Enum `WorkClassification` includes value `one_off_application_ui`.
- [ ] AC-25-006: Enum `WorkClassification` includes value `direct_behavior`.
- [ ] AC-25-007: Enum `WorkClassification` includes value `operational_document`.
- [ ] AC-25-008: Enum `WorkClassification` includes value `bugfix`.
- [ ] AC-25-009: Enum `WorkStatus` is implemented as a fixed normative enum.
- [ ] AC-25-010: Enum `WorkStatus` includes value `draft`.
- [ ] AC-25-011: Enum `WorkStatus` includes value `pending_ac_approval`.
- [ ] AC-25-012: Enum `WorkStatus` includes value `pending_packet_approval`.
- [ ] AC-25-013: Enum `WorkStatus` includes value `approved`.
- [ ] AC-25-014: Enum `WorkStatus` includes value `authorized`.
- [ ] AC-25-015: Enum `WorkStatus` includes value `preimplementation_validated`.
- [ ] AC-25-016: Enum `WorkStatus` includes value `implementation_active`.
- [ ] AC-25-017: Enum `WorkStatus` includes value `implemented`.
- [ ] AC-25-018: Enum `WorkStatus` includes value `review_complete`.
- [ ] AC-25-019: Enum `WorkStatus` includes value `blocked`.
- [ ] AC-25-020: Enum `WorkStatus` includes value `deferred`.
- [ ] AC-25-021: Enum `WorkStatus` includes value `archived`.
- [ ] AC-25-022: Enum `PlanStatus` is implemented as a fixed normative enum.
- [ ] AC-25-023: Enum `PlanStatus` includes value `approved`.
- [ ] AC-25-024: Enum `PlanStatus` includes value `children_created`.
- [ ] AC-25-025: Enum `PlanStatus` includes value `in_progress`.
- [ ] AC-25-026: Enum `PlanStatus` includes value `complete`.
- [ ] AC-25-027: Enum `PlanStatus` includes value `blocked`.
- [ ] AC-25-028: Enum `PlanStatus` includes value `archived`.
- [ ] AC-25-029: Enum `VerificationStatus` is implemented as a fixed normative enum.
- [ ] AC-25-030: Enum `VerificationStatus` includes value `passed`.
- [ ] AC-25-031: Enum `VerificationStatus` includes value `failed`.
- [ ] AC-25-032: Enum `VerificationStatus` includes value `inconclusive`.
- [ ] AC-25-033: Enum `VerificationStatus` includes value `invalid`.
- [ ] AC-25-034: Enum `EvidenceStatus` is implemented as a fixed normative enum.
- [ ] AC-25-035: Enum `EvidenceStatus` includes value `passed`.
- [ ] AC-25-036: Enum `EvidenceStatus` includes value `failed`.
- [ ] AC-25-037: Enum `EvidenceStatus` includes value `inconclusive`.
- [ ] AC-25-038: Enum `EvidenceStatus` includes value `not_applicable`.
- [ ] AC-25-039: Enum `DocsPolicy` is implemented as a fixed normative enum.
- [ ] AC-25-040: Enum `DocsPolicy` includes value `required`.
- [ ] AC-25-041: Enum `DocsPolicy` includes value `changed`.
- [ ] AC-25-042: Enum `DocsPolicy` includes value `none_required`.
- [ ] AC-25-043: Enum `DocsPolicy` includes value `not_applicable`.
- [ ] AC-25-044: Enum `ChangeFileCategory` is implemented as a fixed normative enum.
- [ ] AC-25-045: Enum `ChangeFileCategory` includes value `spec_guard_artifact_evidence`.
- [ ] AC-25-046: Enum `ChangeFileCategory` includes value `docs`.
- [ ] AC-25-047: Enum `ChangeFileCategory` includes value `tests`.
- [ ] AC-25-048: Enum `ChangeFileCategory` includes value `implementation_source`.
- [ ] AC-25-049: Enum `ChangeFileCategory` includes value `runtime_product_configuration`.
- [ ] AC-25-050: Enum `ChangeFileCategory` includes value `generated_build_output`.
- [ ] AC-25-051: Enum `ChangeFileCategory` includes value `other_unexpected`.
- [ ] AC-25-052: `blocked`
- [ ] AC-25-053: `required`
- [ ] AC-25-054: Enumerated item is supported/enforced: `reusable_api`
- [ ] AC-25-055: Enumerated item is supported/enforced: `rest_api`
- [ ] AC-25-056: Enumerated item is supported/enforced: `reusable_ui`
- [ ] AC-25-057: Enumerated item is supported/enforced: `one_off_application_ui`
- [ ] AC-25-058: Enumerated item is supported/enforced: `direct_behavior`
- [ ] AC-25-059: Enumerated item is supported/enforced: `operational_document`
- [ ] AC-25-060: Enumerated item is supported/enforced: `bugfix`
- [ ] AC-25-061: Enumerated item is supported/enforced: `draft`
- [ ] AC-25-062: Enumerated item is supported/enforced: `pending_ac_approval`
- [ ] AC-25-063: Enumerated item is supported/enforced: `pending_packet_approval`
- [ ] AC-25-064: Enumerated item is supported/enforced: `approved`
- [ ] AC-25-065: Enumerated item is supported/enforced: `authorized`
- [ ] AC-25-066: Enumerated item is supported/enforced: `preimplementation_validated`
- [ ] AC-25-067: Enumerated item is supported/enforced: `implementation_active`
- [ ] AC-25-068: Enumerated item is supported/enforced: `implemented`
- [ ] AC-25-069: Enumerated item is supported/enforced: `review_complete`
- [ ] AC-25-070: Enumerated item is supported/enforced: `blocked`
- [ ] AC-25-071: Enumerated item is supported/enforced: `deferred`
- [ ] AC-25-072: Enumerated item is supported/enforced: `archived`
- [ ] AC-25-073: Enumerated item is supported/enforced: `children_created`
- [ ] AC-25-074: Enumerated item is supported/enforced: `in_progress`
- [ ] AC-25-075: Enumerated item is supported/enforced: `complete`
- [ ] AC-25-076: Enumerated item is supported/enforced: `passed`
- [ ] AC-25-077: Enumerated item is supported/enforced: `failed`
- [ ] AC-25-078: Enumerated item is supported/enforced: `inconclusive`
- [ ] AC-25-079: Enumerated item is supported/enforced: `invalid`
- [ ] AC-25-080: Enumerated item is supported/enforced: `not_applicable`
- [ ] AC-25-081: Enumerated item is supported/enforced: `required`
- [ ] AC-25-082: Enumerated item is supported/enforced: `changed`
- [ ] AC-25-083: Enumerated item is supported/enforced: `none_required`
- [ ] AC-25-084: Enumerated item is supported/enforced: `spec_guard_artifact_evidence`
- [ ] AC-25-085: Enumerated item is supported/enforced: `docs`
- [ ] AC-25-086: Enumerated item is supported/enforced: `tests`
- [ ] AC-25-087: Enumerated item is supported/enforced: `implementation_source`
- [ ] AC-25-088: Enumerated item is supported/enforced: `runtime_product_configuration`
- [ ] AC-25-089: Enumerated item is supported/enforced: `generated_build_output`
- [ ] AC-25-090: Enumerated item is supported/enforced: `other_unexpected`
