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

<!-- Expanded from agentic-redesign.md to provide behavior-level coverage. -->

- [ ] AC-18-001: Required diagnostic categories:
- [ ] AC-18-002: binary gate discussion must re-prompt Yes/No/Discuss,
- [ ] AC-18-003: fixed binary decision includes Something else/custom option,
- [ ] AC-18-004: AC approval required,
- [ ] AC-18-005: source-derived AC missing source/evidence,
- [ ] AC-18-006: batch attempted to approve source-derived AC,
- [ ] AC-18-007: changed files outside allowed globs,
- [ ] AC-18-008: update touched approved fields and invalidated approvals,
- [ ] AC-18-009: protected approved-field update rejected,
- [ ] AC-18-010: API/contract-surface docs policy not required,
- [ ] AC-18-011: docs required but missing,
- [ ] AC-18-012: docs-to-AC verification required,
- [ ] AC-18-013: docs-updated verification required,
- [ ] AC-18-014: behavior-tests-to-documented-contract verification required,
- [ ] AC-18-015: tests-to-AC verification required,
- [ ] AC-18-016: retained docs test detected,
- [ ] AC-18-017: failure evidence semantic verification required,
- [ ] AC-18-018: required backend verification claim missing or unregistered,
- [ ] AC-18-019: Plan-vs-single choice required,
- [ ] AC-18-020: Plan approval required,
- [ ] AC-18-021: Plan approval attempted to create children directly,
- [ ] AC-18-022: batch child created payload mismatch,
- [ ] AC-18-023: source-derived AC SourceEvidence refs missing,
- [ ] AC-18-024: batch child change baseline capture failed,
- [ ] AC-18-025: Plan approved-field update rejected,
- [ ] AC-18-026: pre-implementation validation required,
- [ ] AC-18-027: caller-supplied command status rejected,
- [ ] AC-18-028: Enumerated item is supported/enforced: missing Something else for non-binary semantic choice,
- [ ] AC-18-029: Enumerated item is supported/enforced: missing Discuss option,
- [ ] AC-18-030: Enumerated item is supported/enforced: custom non-binary choice awaiting numbered confirmation,
- [ ] AC-18-031: Enumerated item is supported/enforced: binary gate discussion must re-prompt Yes/No/Discuss,
- [ ] AC-18-032: Enumerated item is supported/enforced: fixed binary decision includes Something else/custom option,
- [ ] AC-18-033: Enumerated item is supported/enforced: AC approval required,
- [ ] AC-18-034: Enumerated item is supported/enforced: AC review snapshot missing or stale,
- [ ] AC-18-035: Enumerated item is supported/enforced: AC reviewed payload hash mismatch,
- [ ] AC-18-036: Enumerated item is supported/enforced: AC refinement attempted artifact mutation,
- [ ] AC-18-037: Enumerated item is supported/enforced: source-derived AC missing source/evidence,
- [ ] AC-18-038: Enumerated item is supported/enforced: batch attempted to approve source-derived AC,
- [ ] AC-18-039: Enumerated item is supported/enforced: runtime baseline missing,
- [ ] AC-18-040: Enumerated item is supported/enforced: runtime baseline not accepted,
- [ ] AC-18-041: Enumerated item is supported/enforced: runtime baseline validation failed,
- [ ] AC-18-042: Enumerated item is supported/enforced: runtime baseline acceptance stale,
- [ ] AC-18-043: Enumerated item is supported/enforced: packet change baseline missing,
- [ ] AC-18-044: Enumerated item is supported/enforced: dirty implementation source at authorization,
- [ ] AC-18-045: Enumerated item is supported/enforced: changed files outside allowed globs,
- [ ] AC-18-046: Enumerated item is supported/enforced: implementation source changed before failure-first evidence,
- [ ] AC-18-047: Enumerated item is supported/enforced: classification invalid,
- [ ] AC-18-048: Enumerated item is supported/enforced: docs policy invalid,
- [ ] AC-18-049: Enumerated item is supported/enforced: update touched approved fields and invalidated approvals,
- [ ] AC-18-050: Enumerated item is supported/enforced: protected approved-field update rejected,
- [ ] AC-18-051: Enumerated item is supported/enforced: API/contract-surface docs policy not required,
- [ ] AC-18-052: Enumerated item is supported/enforced: docs required but missing,
- [ ] AC-18-053: Enumerated item is supported/enforced: docs-to-AC verification required,
- [ ] AC-18-054: Enumerated item is supported/enforced: docs-updated verification required,
- [ ] AC-18-055: Enumerated item is supported/enforced: behavior-tests-to-documented-contract verification required,
- [ ] AC-18-056: Enumerated item is supported/enforced: tests-to-AC verification required,
- [ ] AC-18-057: Enumerated item is supported/enforced: retained docs test detected,
- [ ] AC-18-058: Enumerated item is supported/enforced: test cleanup side effect detected,
- [ ] AC-18-059: Enumerated item is supported/enforced: operational-document not-applicable validation missing,
- [ ] AC-18-060: Enumerated item is supported/enforced: not-applicable evidence lacks deterministic eligibility,
- [ ] AC-18-061: Enumerated item is supported/enforced: operational-document docs policy invalid,
- [ ] AC-18-062: Enumerated item is supported/enforced: failure evidence semantic verification required,
- [ ] AC-18-063: Enumerated item is supported/enforced: verifier disabled,
- [ ] AC-18-064: Enumerated item is supported/enforced: verifier adapter unavailable,
- [ ] AC-18-065: Enumerated item is supported/enforced: verifier misconfigured,
- [ ] AC-18-066: Enumerated item is supported/enforced: verifier health check failed,
- [ ] AC-18-067: Enumerated item is supported/enforced: verifier response invalid,
- [ ] AC-18-068: Enumerated item is supported/enforced: verifier attempted to judge human-approved intent,
- [ ] AC-18-069: Enumerated item is supported/enforced: required backend verification claim missing or unregistered,
- [ ] AC-18-070: Enumerated item is supported/enforced: Plan-vs-single choice required,
- [ ] AC-18-071: Enumerated item is supported/enforced: Plan approval required,
- [ ] AC-18-072: Enumerated item is supported/enforced: Plan proposal payload hash mismatch,
- [ ] AC-18-073: Enumerated item is supported/enforced: Plan approval attempted to create children directly,
- [ ] AC-18-074: Enumerated item is supported/enforced: review snapshot producer output missing,
- [ ] AC-18-075: Enumerated item is supported/enforced: snapshot payload mismatch,
- [ ] AC-18-076: Enumerated item is supported/enforced: stale source revision for ephemeral snapshot,
- [ ] AC-18-077: Enumerated item is supported/enforced: batch review snapshot missing or stale,
- [ ] AC-18-078: Enumerated item is supported/enforced: batch source artifact refs missing or not derivable,
- [ ] AC-18-079: Enumerated item is supported/enforced: batch audit revision missing,
- [ ] AC-18-080: Enumerated item is supported/enforced: batch proposed children payload mismatch,
- [ ] AC-18-081: Enumerated item is supported/enforced: batch child snapshot binding missing,
- [ ] AC-18-082: Enumerated item is supported/enforced: batch child snapshot revision invalid,
- [ ] AC-18-083: Enumerated item is supported/enforced: batch proceed approved post-action result field,
- [ ] AC-18-084: Enumerated item is supported/enforced: batch proceed approved payload reference missing,
- [ ] AC-18-085: Enumerated item is supported/enforced: ambiguous proposed child id in batch snapshot revision,
- [ ] AC-18-086: Enumerated item is supported/enforced: batch child created payload mismatch,
- [ ] AC-18-087: Enumerated item is supported/enforced: batch child approval-relevant payload mismatch,
- [ ] AC-18-088: Enumerated item is supported/enforced: batch child expected revision missing,
- [ ] AC-18-089: Enumerated item is supported/enforced: Plan proposed child id invalid for batch snapshot revision,
- [ ] AC-18-090: Enumerated item is supported/enforced: batch child Plan slice mapping missing or invalid,
- [ ] AC-18-091: Enumerated item is supported/enforced: batch child Plan slice correspondence mismatch,
- [ ] AC-18-092: Enumerated item is supported/enforced: batch child title correspondence mismatch,
- [ ] AC-18-093: Enumerated item is supported/enforced: batch child source evidence summary mismatch,
- [ ] AC-18-094: Enumerated item is supported/enforced: batch child source artifact refs missing or inconsistent,
- [ ] AC-18-095: Enumerated item is supported/enforced: source artifact refs not in canonical order,
- [ ] AC-18-096: Enumerated item is supported/enforced: source artifact ref unresolved,
- [ ] AC-18-097: Enumerated item is supported/enforced: source artifact content hash mismatch,
- [ ] AC-18-098: Enumerated item is supported/enforced: source-derived AC SourceEvidence refs missing,
- [ ] AC-18-099: Enumerated item is supported/enforced: source evidence hash mismatch,
- [ ] AC-18-100: Enumerated item is supported/enforced: batch child proposed WorkPacket payload missing,
- [ ] AC-18-101: Enumerated item is supported/enforced: batch child change baseline capture failed,
- [ ] AC-18-102: Enumerated item is supported/enforced: proposed authorization snapshot payload invalid,
- [ ] AC-18-103: Enumerated item is supported/enforced: authorization snapshot missing approved packet hash,
- [ ] AC-18-104: Enumerated item is supported/enforced: approved fields missing,
- [ ] AC-18-105: Enumerated item is supported/enforced: approved payload missing for registered decision type,
- [ ] AC-18-106: Enumerated item is supported/enforced: declined decision incorrectly supplied approved payload,
- [ ] AC-18-107: Enumerated item is supported/enforced: decision mutation prohibited,
- [ ] AC-18-108: Enumerated item is supported/enforced: Plan approved-field update rejected,
- [ ] AC-18-109: Enumerated item is supported/enforced: ready child packet preconditions missing,
- [ ] AC-18-110: Enumerated item is supported/enforced: Work Packet approval missing,
- [ ] AC-18-111: Enumerated item is supported/enforced: implementation authorization missing,
- [ ] AC-18-112: Enumerated item is supported/enforced: pre-implementation validation required,
- [ ] AC-18-113: Enumerated item is supported/enforced: review traceability missing,
- [ ] AC-18-114: Enumerated item is supported/enforced: command result missing for command-backed evidence,
- [ ] AC-18-115: Enumerated item is supported/enforced: command result execution context missing,
- [ ] AC-18-116: Enumerated item is supported/enforced: command result status incompatible with evidence type,
- [ ] AC-18-117: Enumerated item is supported/enforced: command result purpose incompatible with evidence type,
- [ ] AC-18-118: Enumerated item is supported/enforced: caller-supplied command status rejected,
- [ ] AC-18-119: Enumerated item is supported/enforced: final claim unsupported,
- [ ] AC-18-120: Enumerated item is supported/enforced: approval hash stale,
- [ ] AC-18-121: Enumerated item is supported/enforced: CLI/MCP parity missing.
