# US-13: Backend verifier

Derived from: [13. Backend Verifier](../agentic-redesign-references.md#us-13-source)

## Problem

Required semantic frontend-agent claims need backend verification while preserving human authority and deterministic-kernel ownership.

## User story

As a verification integrator, I want backend verifier implemented, so that required semantic frontend-agent claims need backend verification while preserving human authority and deterministic-kernel ownership.

## In scope

- Support adapter modes.
- Register frontend-agent claims.
- Enforce verification requirement matrix.
- Manage verifier configuration and health.
- Constrain verifier task and response schemas.

## Out of scope

- Verifier mutating product intent or lifecycle decisions.
- Verifier approving/rejecting work or judging human-approved ACs/scope/platform/architecture.
- Replacing deterministic validation with model judgment.

## Acceptance criteria

- [ ] Configured verifier adapter modes behave as specified.
- [ ] Claims are registered with required metadata before verification.
- [ ] Verification is required exactly where the matrix requires it.
- [ ] Verifier health and configuration diagnostics are exposed.
- [ ] Verifier task payloads and responses follow the required schemas and constraints.
- [ ] Responses that exceed verifier authority or judge human-approved intent are invalid.
