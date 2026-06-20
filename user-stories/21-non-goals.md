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

<!-- Expanded from agentic-redesign.md to provide behavior-level coverage. -->

- [ ] AC-21-001: This specification does not require:
- [ ] AC-21-002: Enumerated item is supported/enforced: prompting every non-AC intent field separately,
- [ ] AC-21-003: Enumerated item is supported/enforced: making users/actors/edge-cases mandatory,
- [ ] AC-21-004: Enumerated item is supported/enforced: letting backend verifier generate product scope,
- [ ] AC-21-005: Enumerated item is supported/enforced: letting backend verifier make decisions,
- [ ] AC-21-006: Enumerated item is supported/enforced: using backend verifier to judge approved human intent,
- [ ] AC-21-007: Enumerated item is supported/enforced: using backend verifier for Plan-vs-single or Plan approval,
- [ ] AC-21-008: Enumerated item is supported/enforced: replacing deterministic validation with model judgment,
- [ ] AC-21-009: Enumerated item is supported/enforced: choosing a single model vendor,
- [ ] AC-21-010: Enumerated item is supported/enforced: storing secrets directly,
- [ ] AC-21-011: Enumerated item is supported/enforced: exposing Spec Guard internals to frontend agents.
