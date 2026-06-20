# US-14: Runtime evidence, review completion, and final claims

Derived from: [14. Runtime, Review, and Final Claims](../agentic-redesign-references.md#us-14-source)

## Problem

Implemented work needs runtime evidence, review completion, and final claims that are backed by recorded artifacts instead of unsupported summaries.

## User story

As a reviewer, I want runtime evidence, review completion, and final claims implemented, so that implemented work needs runtime evidence, review completion, and final claims that are backed by recorded artifacts instead of unsupported summaries.

## In scope

- Record runtime evidence.
- Complete review only when required checks and evidence are valid.
- Validate final claims against evidence and governed state.

## Out of scope

- Final responses that claim unrecorded tests or behavior.
- Review completion when approvals or pre-implementation validation are stale.

## Acceptance criteria

- [ ] Runtime evidence records command results and required metadata.
- [ ] Review completion requires valid approvals, authorization, validation, changed-file checks, evidence, and backend verification where required.
- [ ] Final claims are registered and checked against available evidence.
- [ ] Unsupported or stale claims are diagnosed and cannot satisfy final claim validation.
- [ ] Review completion becomes stale when dependent approvals are invalidated.
