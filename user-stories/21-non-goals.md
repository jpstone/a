# US-21: Non-goals and boundaries

Derived from: [21. Non-Goals](../agentic-redesign-references.md#us-21-source)

## Problem

The redesign needs explicit boundaries so implementers do not add authority, prompting, verifier, or storage requirements that the governance model rejects.

## User story

As a scope owner, I want non-goals and boundaries implemented, so that the redesign needs explicit boundaries so implementers do not add authority, prompting, verifier, or storage requirements that the governance model rejects.

## In scope

- Document features and behaviors explicitly not required.
- Use non-goals to reject scope creep and incorrect implementations.

## Out of scope

- Prompting every non-AC intent field separately.
- Letting backend verifier generate or judge product scope/intent.
- Replacing deterministic validation with model judgment.
- Choosing one model vendor or storing secrets directly.

## Acceptance criteria

- [ ] Implementation does not require every non-AC intent field to be separately prompted.
- [ ] Backend verifier cannot generate product scope, make decisions, or judge approved human intent.
- [ ] Deterministic validation is not replaced by model judgment.
- [ ] The design remains model-vendor-neutral.
- [ ] Secrets are not stored directly in Spec Guard artifacts/config.
