# US-04: Decision binding and review snapshots

Derived from: [4. Decision Binding and Review Snapshots](../agentic-redesign-references.md#us-04-source)

## Problem

Approvals and authorizations must bind to the exact reviewed content so later changes, stale reviews, and unsupported decisions are detectable.

## User story

As a governance auditor, I want decision binding and review snapshots implemented, so that approvals and authorizations must bind to the exact reviewed content so later changes, stale reviews, and unsupported decisions are detectable.

## In scope

- Define review snapshots and canonical hashing.
- Support ephemeral, persisted, and batch snapshot categories.
- Require snapshot producers for review-bound gates.
- Define approved fields and invalidation dependencies.
- Define immutable HumanDecision records.
- Bind authorization and batch decisions to exact payloads.

## Out of scope

- Using frontend summaries to validate snapshot hashes.
- Mutating decision substance after recording.
- Approving stale or mismatched review payloads.
- Batch-approving source-derived ACs.

## Acceptance criteria

- [ ] Every review-bound gate has a snapshot producer before recording the human decision.
- [ ] Snapshot payloads use deterministic canonical serialization and SHA-256 hashes.
- [ ] Approval actions validate submitted snapshot hash/revision/source refs before mutating governed state.
- [ ] Approved fields are derived from registered decision type and stored as canonical JSON pointers.
- [ ] Changing approved paths invalidates dependent decisions and lifecycle readiness as specified.
- [ ] HumanDecision records are append-only and substance-immutable.
- [ ] Authorization and batch review snapshots include the required payloads, refs, hashes, and child-decision bindings.
