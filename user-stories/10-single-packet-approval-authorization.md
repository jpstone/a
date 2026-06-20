# US-10: Single packet approval and authorization

Derived from: [10. Single Packet Approval and Authorization](../agentic-redesign-references.md#us-10-source)

## Problem

A single Work Packet needs a sequential path from AC approval to packet approval to implementation authorization, with readiness checks at each step.

## User story

As a packet approver, I want single packet approval and authorization implemented, so that a single Work Packet needs a sequential path from AC approval to packet approval to implementation authorization, with readiness checks at each step.

## In scope

- Define single-packet path.
- Define readiness levels for AC approval, packet approval, authorization, batch authorization, and implementation.
- Enforce Work Packet approval gate.
- Enforce implementation authorization gate.

## Out of scope

- Starting implementation before authorization and pre-implementation validation.
- Skipping AC approval before packet approval.
- Authorizing stale or unapproved packet content.

## Acceptance criteria

<!-- Expanded from agentic-redesign.md to provide behavior-level coverage. -->

- [ ] AC-10-001: If work is not under an approved Plan batch flow, Spec Guard must use sequential gates:
- [ ] AC-10-002: No combined AC+packet approval gate is allowed for a single Work Packet path.
- [ ] AC-10-003: source-derived ACs include source/evidence,
- [ ] AC-10-004: no AC-approval-blocking diagnostics exist.
- [ ] AC-10-005: ACs are approved, except for eligible Plan-child batch approval where the same batch selection explicitly approves displayed non-source-derived ACs,
- [ ] AC-10-006: the packet contains no unapproved source-derived ACs,
- [ ] AC-10-007: allowed file globs are present,
- [ ] AC-10-008: required platform choice is recorded,
- [ ] AC-10-009: required architecture choice is recorded,
- [ ] AC-10-010: no required human decision is pending,
- [ ] AC-10-011: no packet-approval-blocking diagnostics exist.
- [ ] AC-10-012: allowed scope is known,
- [ ] AC-10-013: packet change baseline can be captured,
- [ ] AC-10-014: no authorization-blocking diagnostics exist.
- [ ] AC-10-015: the proposed child payload is included in a persisted batch review snapshot,
- [ ] AC-10-016: the proposed child contains no source-derived ACs,
- [ ] AC-10-017: allowed scope is known in the proposed child payload,
- [ ] AC-10-018: packet change baseline capture is expected to succeed after child artifact creation,
- [ ] AC-10-019: no batch-authorization-blocking diagnostics exist.
- [ ] AC-10-020: authorization is recorded,
- [ ] AC-10-021: packet change baseline is captured,
- [ ] AC-10-022: required pre-implementation docs/tests/failure-first chain is complete: required docs exist
- [ ] AC-10-023: are linked, retained test files exist when tests are required, and failure-first evidence is recorded
- [ ] AC-10-024: passing-test evidence is not required until review completion,
- [ ] AC-10-025: required backend verification for pre-implementation has passed, excluding `docs_updated` verification that section 12.8 explicitly permits to remain pending until review completion,
- [ ] AC-10-026: no implementation-blocking diagnostics exist.
- [ ] AC-10-027: Implementation source changes must not occur before implementation-ready state.
- [ ] AC-10-028: `Do you approve this Work Packet as shown?`
- [ ] AC-10-029: Yes records packet approval bound to the displayed packet review snapshot hash.
- [ ] AC-10-030: No records decline or blocks as appropriate.
- [ ] AC-10-031: Discuss records no mutation and later re-presents the same gate.
- [ ] AC-10-032: Yes records authorization, captures packet change baseline, and binds authorization to the authorization review snapshot hash.
- [ ] AC-10-033: The authorization review snapshot must include the approved packet snapshot hash and revision.
- [ ] AC-10-034: Ordered requirement is supported/enforced: AC approval gate.
- [ ] AC-10-035: Ordered requirement is supported/enforced: Work Packet approval gate.
- [ ] AC-10-036: Ordered requirement is supported/enforced: Implementation authorization gate.
- [ ] AC-10-037: Enumerated item is supported/enforced: goal exists,
- [ ] AC-10-038: Enumerated item is supported/enforced: at least one AC exists,
- [ ] AC-10-039: Enumerated item is supported/enforced: source-derived ACs include source/evidence,
- [ ] AC-10-040: Enumerated item is supported/enforced: AC review snapshot can be rendered,
- [ ] AC-10-041: Enumerated item is supported/enforced: no AC-approval-blocking diagnostics exist.
- [ ] AC-10-042: Enumerated item is supported/enforced: ACs are approved, except for eligible Plan-child batch approval where the same batch selection explicitly approves displayed non-source-derived ACs,
- [ ] AC-10-043: Enumerated item is supported/enforced: the packet contains no unapproved source-derived ACs,
- [ ] AC-10-044: Enumerated item is supported/enforced: runtime baseline is accepted,
- [ ] AC-10-045: Enumerated item is supported/enforced: classification is valid,
- [ ] AC-10-046: Enumerated item is supported/enforced: docs policy is valid,
- [ ] AC-10-047: Enumerated item is supported/enforced: allowed file globs are present,
- [ ] AC-10-048: Enumerated item is supported/enforced: required platform choice is recorded,
- [ ] AC-10-049: Enumerated item is supported/enforced: required architecture choice is recorded,
- [ ] AC-10-050: Enumerated item is supported/enforced: no required human decision is pending,
- [ ] AC-10-051: Enumerated item is supported/enforced: no packet-approval-blocking diagnostics exist.
- [ ] AC-10-052: Enumerated item is supported/enforced: packet is approved at current review snapshot hash,
- [ ] AC-10-053: Enumerated item is supported/enforced: runtime baseline remains accepted,
- [ ] AC-10-054: Enumerated item is supported/enforced: approval is not stale,
- [ ] AC-10-055: Enumerated item is supported/enforced: allowed scope is known,
- [ ] AC-10-056: Enumerated item is supported/enforced: parent Plan relationship is valid when applicable,
- [ ] AC-10-057: Enumerated item is supported/enforced: packet change baseline can be captured,
- [ ] AC-10-058: Enumerated item is supported/enforced: no authorization-blocking diagnostics exist.
- [ ] AC-10-059: Enumerated item is supported/enforced: the proposed child payload is included in a persisted batch review snapshot,
- [ ] AC-10-060: Enumerated item is supported/enforced: the proposed child contains no source-derived ACs,
- [ ] AC-10-061: Enumerated item is supported/enforced: the proposed child is batch packet-approval eligible,
- [ ] AC-10-062: Enumerated item is supported/enforced: the proposed child packet review snapshot is present,
- [ ] AC-10-063: Enumerated item is supported/enforced: the proposed child authorization review snapshot is present,
- [ ] AC-10-064: Enumerated item is supported/enforced: allowed scope is known in the proposed child payload,
- [ ] AC-10-065: Enumerated item is supported/enforced: packet change baseline capture is expected to succeed after child artifact creation,
- [ ] AC-10-066: Enumerated item is supported/enforced: no batch-authorization-blocking diagnostics exist.
- [ ] AC-10-067: Enumerated item is supported/enforced: authorization is recorded,
- [ ] AC-10-068: Enumerated item is supported/enforced: packet change baseline is captured,
- [ ] AC-10-069: Enumerated item is supported/enforced: pre-implementation validation passes,
- [ ] AC-10-070: Enumerated item is supported/enforced: required pre-implementation docs/tests/failure-first chain is complete: required docs exist and are linked, retained test files exist when tests are required, and failure-first evidence is recorded; passing-test evidence is not required until review completion,
- [ ] AC-10-071: Enumerated item is supported/enforced: required backend verification for pre-implementation has passed, excluding `docs_updated` verification that section 12.8 explicitly permits to remain pending until review completion,
- [ ] AC-10-072: Enumerated item is supported/enforced: no implementation-blocking diagnostics exist.
- [ ] AC-10-073: Ordered requirement is supported/enforced: Yes
- [ ] AC-10-074: Ordered requirement is supported/enforced: No
- [ ] AC-10-075: Ordered requirement is supported/enforced: Discuss
