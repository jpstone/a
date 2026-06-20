# US-00: Implementation discipline

Derived from: [0. Implementation Discipline](../agentic-redesign-references.md#us-00-source)

## Problem

Spec Guard needs a predictable test-first implementation workflow so agents do not invent behavior or ship unvalidated changes.

## User story

As a implementation agent, I want implementation discipline implemented, so that spec Guard needs a predictable test-first implementation workflow so agents do not invent behavior or ship unvalidated changes.

## In scope

- Require tests to be written or updated before production behavior changes.
- Require targeted and full validation around implementation work.
- Require agents to stop and ask when the specification is ambiguous.

## Out of scope

- Defining the complete test suite contents for every later story.
- Allowing speculative implementation when required behavior is unclear.

## Acceptance criteria

<!-- Expanded from agentic-redesign.md to provide behavior-level coverage. -->

- [ ] AC-00-001: Implementation must be test-first.
- [ ] AC-00-002: For each required behavior:
- [ ] AC-00-003: Write or update tests first.
- [ ] AC-00-004: If this document is ambiguous in a way that prevents implementation, stop and ask.
- [ ] AC-00-005: This document must be sufficient for an implementation agent to build Spec Guard without relying on undocumented behavior.
- [ ] AC-00-006: Ordered requirement is supported/enforced: Write or update tests first.
- [ ] AC-00-007: Ordered requirement is supported/enforced: Run tests and observe the expected failure.
- [ ] AC-00-008: Ordered requirement is supported/enforced: Implement the smallest production change that satisfies the tests.
- [ ] AC-00-009: Ordered requirement is supported/enforced: Re-run targeted tests.
- [ ] AC-00-010: Ordered requirement is supported/enforced: Re-run full validation before packaging or release.
