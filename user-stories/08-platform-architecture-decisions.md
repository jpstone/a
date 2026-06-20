# US-08: Product platform and architecture decisions

Derived from: [8. Product Platform and Architecture](../agentic-redesign-references.md#us-08-source)

## Problem

Platform and architecture choices need human-owned numbered decisions so later packet work uses explicit product context.

## User story

As a product decision maker, I want product platform and architecture decisions implemented, so that platform and architecture choices need human-owned numbered decisions so later packet work uses explicit product context.

## In scope

- Capture product platform through non-binary semantic choice.
- Capture architecture through non-binary semantic choice.
- Allow custom choices only after numbered confirmation.
- Record choices in decision history and bind to work where applicable.

## Out of scope

- Letting agents infer final platform or architecture without human selection.
- Using backend verifier to choose or judge platform/architecture.

## Acceptance criteria

- [ ] Platform prompts present numbered options, Something else, and Discuss.
- [ ] Architecture prompts present numbered options, Something else, and Discuss.
- [ ] Custom platform or architecture prose is re-presented as numbered confirmation before recording.
- [ ] Only the numbered confirming option records the decision.
- [ ] Recorded choices are available to downstream Work Packet review and readiness checks.
