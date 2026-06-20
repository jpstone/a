# US-03: Choice, gate, and prompt semantics

Derived from: [3. Choice, Gate, and Prompt Semantics](../agentic-redesign-references.md#us-03-source)

## Problem

Human-facing governance prompts need consistent numbered semantics so only explicit numbered choices mutate decision state.

## User story

As a human reviewer, I want choice, gate, and prompt semantics implemented, so that human-facing governance prompts need consistent numbered semantics so only explicit numbered choices mutate decision state.

## In scope

- Require numbered choices for governed decisions.
- Define non-binary semantic choices with Something else and Discuss.
- Define binary gates as Yes/No/Discuss only.
- Define fixed binary decisions with two domain outcomes plus Discuss.
- Ensure prompt proposals and Discuss are non-mutating.

## Out of scope

- Free-form final governed decisions without numbered confirmation.
- Turning binary gates into custom semantic prompts.
- Recording Discuss as a HumanDecision.

## Acceptance criteria

<!-- Expanded from agentic-redesign.md to provide behavior-level coverage. -->

- [ ] AC-03-001: All governed choices shown to the human must be numbered.
- [ ] AC-03-002: Governed decision, approval, authorization, acceptance, and final intent state mutates only from a numbered human selection.
- [ ] AC-03-003: Draft artifacts, audit records, command results, evidence records, configuration, and deterministic validation records may mutate through their registered actions without being human decisions unless this specification explicitly requires a human gate.
- [ ] AC-03-004: Prompt proposal actions may persist pending prompt/audit records as audit-only records, but they must not record a governed decision or mutate decision state before the human selects a number.
- [ ] AC-03-005: Any structured data needed to later record a decision must be included in the prompt record, not reconstructed from frontend-agent prose.
- [ ] AC-03-006: Non-binary semantic choices must include:
- [ ] AC-03-007: custom prose support.
- [ ] AC-03-008: Non-binary semantic choices include:
- [ ] AC-03-009: The frontend agent must re-present it as a numbered confirmation:
- [ ] AC-03-010: Use `<decision>` as the proposed `<choice>`
- [ ] AC-03-011: Do not use this decision
- [ ] AC-03-012: Only option 1 records the decision.
- [ ] AC-03-013: For custom confirmation prompts, option 2 records no HumanDecision and leaves the prior choice unset
- [ ] AC-03-014: if the workflow needs a block or decline, it must use the relevant binary gate.
- [ ] AC-03-015: Option 3 records no mutation.
- [ ] AC-03-016: Spec Guard validates prompt shape, not semantic clarity of free-form human prose.
- [ ] AC-03-017: must never become non-binary prompts.
- [ ] AC-03-018: Binary gates must be:
- [ ] AC-03-019: If the human selects Discuss, the frontend agent may discuss, but later resolution must re-present the same Yes/No/Discuss gate.
- [ ] AC-03-020: Discussion-derived text must not replace Yes
- [ ] AC-03-021: must not become a custom gate option.
- [ ] AC-03-022: Only numbered Yes mutates the gated state.
- [ ] AC-03-023: Numbered No records decline or blocks as specified by the gate
- [ ] AC-03-024: records a HumanDecision with `approved_fields: []` unless the action is specified as audit-only.
- [ ] AC-03-025: Discuss records no governed mutation
- [ ] AC-03-026: must not create a HumanDecision
- [ ] AC-03-027: implementations may record audit-only prompt/answer records for Discuss.
- [ ] AC-03-028: Binary gates include:
- [ ] AC-03-029: They must not include Something else or custom prose support.
- [ ] AC-03-030: Selecting option 1 or option 2 records a HumanDecision for the fixed decision.
- [ ] AC-03-031: Discuss mutates nothing, creates no HumanDecision, and later re-presents the same fixed decision.
- [ ] AC-03-032: Fixed binary decisions include:
- [ ] AC-03-033: Enumerated item is supported/enforced: relevant numbered options,
- [ ] AC-03-034: Enumerated item is supported/enforced: `Something else`,
- [ ] AC-03-035: Enumerated item is supported/enforced: `Discuss`,
- [ ] AC-03-036: Enumerated item is supported/enforced: custom prose support.
- [ ] AC-03-037: Enumerated item is supported/enforced: product/platform type,
- [ ] AC-03-038: Enumerated item is supported/enforced: architecture.
- [ ] AC-03-039: Ordered requirement is supported/enforced: Use `<decision>` as the proposed `<choice>`
- [ ] AC-03-040: Ordered requirement is supported/enforced: Do not use this decision
- [ ] AC-03-041: Ordered requirement is supported/enforced: Discuss
- [ ] AC-03-042: Ordered requirement is supported/enforced: Yes
- [ ] AC-03-043: Ordered requirement is supported/enforced: No
- [ ] AC-03-044: Enumerated item is supported/enforced: runtime baseline acceptance,
- [ ] AC-03-045: Enumerated item is supported/enforced: AC approval,
- [ ] AC-03-046: Enumerated item is supported/enforced: Work Packet approval,
- [ ] AC-03-047: Enumerated item is supported/enforced: implementation authorization,
- [ ] AC-03-048: Enumerated item is supported/enforced: Plan approval.
- [ ] AC-03-049: Ordered requirement is supported/enforced: First domain outcome
- [ ] AC-03-050: Ordered requirement is supported/enforced: Second domain outcome
- [ ] AC-03-051: Enumerated item is supported/enforced: Plan-vs-single-packet choice.
