# US-12: Implementation boundary and pre-implementation validation

Derived from: [12. Implementation Boundary and Pre-Implementation Validation](../agentic-redesign-references.md#us-12-source)

## Problem

Spec Guard must prevent implementation source changes before required docs, tests, and failure-first evidence are established.

## User story

As a implementation agent, I want implementation boundary and pre-implementation validation implemented, so that spec Guard must prevent implementation source changes before required docs, tests, and failure-first evidence are established.

## In scope

- Classify file categories.
- Define allowed pre-implementation changes.
- Enforce docs/test/failure-first ordering.
- Handle test cleanup and side effects.
- Enforce allowed globs.
- Define validation chains for API, non-API, and operational-document packets.
- Wire docs-updated gate behavior.

## Out of scope

- Allowing implementation_source changes before required validation evidence.
- Counting pre-existing dirty docs/tests/evidence as packet evidence without re-recording.
- Permitting changes outside allowed globs without diagnostics.

## Acceptance criteria

- [ ] Files are classified by canonical file categories.
- [ ] Pre-implementation validation blocks implementation source changes until required docs/tests/failure evidence conditions are met.
- [ ] Test cleanup and side-effect rules prevent false failure-first evidence.
- [ ] Allowed-globs enforcement detects and reports out-of-scope changes.
- [ ] API/contract-surface packets use the required docs and validation chain.
- [ ] Non-API and operational-document packets use their specified validation chains.
- [ ] Docs-updated gate wiring reflects docs policy and classification.
