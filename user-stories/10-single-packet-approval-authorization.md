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

- [ ] Single-packet flow follows AC approval, packet approval, and implementation authorization gates.
- [ ] AC-approval-ready, packet-approval-ready, authorization-ready, batch-authorization-ready, and implementation-ready diagnostics are computed as specified.
- [ ] Work Packet approval binds to a packet review snapshot.
- [ ] Implementation authorization binds to an authorization review snapshot and captures packet change baseline.
- [ ] Authorization fails when deterministic readiness checks fail.
- [ ] Implementation-ready requires valid approvals, authorization, runtime baseline, packet baseline, and no stale invalidation.
