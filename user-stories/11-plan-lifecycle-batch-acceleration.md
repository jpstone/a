# US-11: Plan lifecycle and batch acceleration

Derived from: [11. Plan Lifecycle and Batch Acceleration](../agentic-redesign-references.md#us-11-source)

## Problem

Broad work needs an explicit plan-vs-single decision and safe batch acceleration for eligible child packets without losing per-child governance.

## User story

As a plan approver, I want plan lifecycle and batch acceleration implemented, so that broad work needs an explicit plan-vs-single decision and safe batch acceleration for eligible child packets without losing per-child governance.

## In scope

- Record Plan-vs-single fixed binary decision.
- Generate non-mutating Plan proposals.
- Approve Plans through snapshot-bound gate.
- Create/proceed with Plan children through batch options and batch review snapshot.
- Record child approvals/authorizations from batch where eligible.

## Out of scope

- Using backend verifier for Plan-vs-single or Plan approval.
- Batch-approving source-derived AC children.
- Creating child approvals when proposed and created payloads differ.

## Acceptance criteria

- [ ] Plan-vs-single prompt has two domain outcomes plus Discuss and no Something else.
- [ ] Plan proposal action is non-mutating and produces the reviewed Plan proposal payload.
- [ ] Plan approval binds to the Plan proposal snapshot.
- [ ] Batch proceed requires a persisted batch review snapshot before human selection.
- [ ] Batch options record per-child decisions with child-specific hashes/revisions/source refs.
- [ ] Source-derived AC children are not batch-approved or batch-authorized.
- [ ] Stale batch snapshots or mismatched child projections block batch approvals/authorizations.
