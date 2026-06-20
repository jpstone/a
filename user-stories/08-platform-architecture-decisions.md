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

<!-- Expanded from agentic-redesign.md to provide behavior-level coverage. -->

- [ ] AC-08-001: A Work Packet's `platform.required` is true for every packet except `operational_document` packets whose approved scope changes only documentation/operational content and packets whose platform is inherited from an approved parent Plan `product_context.platform_decision_id` or an accepted RuntimeBaseline `stack.product_platform`.
- [ ] AC-08-002: When `platform.required` is false, `platform.not_required_reason` must record the deterministic basis.
- [ ] AC-08-003: When true, packet approval readiness requires `platform.decision_id` to reference a recorded `platform_choice` HumanDecision.
- [ ] AC-08-004: The frontend agent must present a relevant numbered option list based on request, repository context, and observable facts.
- [ ] AC-08-005: custom prose support.
- [ ] AC-08-006: Custom platform text is captured as human text after numbered confirmation.
- [ ] AC-08-007: Spec Guard must not map custom platform text to a hard-coded equivalent after confirmation.
- [ ] AC-08-008: A platform choice must record a HumanDecision with decision type `platform_choice`.
- [ ] AC-08-009: `work.choice.propose` must store each final platform option with a structured payload sufficient to construct PlatformChoiceDecisionPayload.
- [ ] AC-08-010: `work.choice.answer` or `work.choice.confirm_custom` must store a canonical PlatformChoiceDecisionPayload in `approved_payload`
- [ ] AC-08-011: update the Work Packet platform decision reference.
- [ ] AC-08-012: Discuss and unconfirmed custom prose create no HumanDecision.
- [ ] AC-08-013: Plan approval does not create platform choices.
- [ ] AC-08-014: `PlanProposalPayload.product_context.platform_decision_id` may only copy an already recorded platform HumanDecision id, and `platform_choice` is traceability text for that decision.
- [ ] AC-08-015: If a Plan child requires a platform choice and no platform decision id is present, the child is not eligible for batch approval or authorization until the platform gate records the decision on that child.
- [ ] AC-08-016: Batch approval must not choose platform.
- [ ] AC-08-017: When architecture affects implementation, persistence, runtime, deployment, API boundaries, or test strategy, Spec Guard must require human architecture review.
- [ ] AC-08-018: `architecture.required` is true for API/contract-surface classifications and whenever `work.intent.draft` or `work.update` sets `architecture.required: true` with a non-empty `required_reason`.
- [ ] AC-08-019: It is false for documentation-only `operational_document` packets and may be false for localized direct behavior/bugfix/one-off UI packets only when `architecture.not_required_reason` records the deterministic basis.
- [ ] AC-08-020: Packet approval readiness requires at least one architecture decision id when `architecture.required` is true.
- [ ] AC-08-021: Each architecture option must include:
- [ ] AC-08-022: The prompt must include Something else and Discuss.
- [ ] AC-08-023: Custom architecture requires numbered confirmation.
- [ ] AC-08-024: `work.choice.propose` must store each architecture option with its label, description, benefits, costs/tradeoffs, and downstream constraints in a structured option payload.
- [ ] AC-08-025: An architecture choice must record a HumanDecision with decision type `architecture_choice`.
- [ ] AC-08-026: `work.choice.answer` or `work.choice.confirm_custom` must store a canonical ArchitectureChoiceDecisionPayload in `approved_payload`
- [ ] AC-08-027: update the affected Work Packet architecture decision references.
- [ ] AC-08-028: Plan approval does not create architecture choices.
- [ ] AC-08-029: `PlanProposalPayload.product_context.architecture_decision_ids` may only copy already recorded architecture HumanDecision ids.
- [ ] AC-08-030: If a Plan child requires architecture review and no architecture decision id is present, the child is not eligible for batch approval or authorization until the architecture gate records the decision on that child.
- [ ] AC-08-031: Batch approval must not choose architecture.
- [ ] AC-08-032: The backend verifier must not judge architecture quality.
- [ ] AC-08-033: Enumerated item is supported/enforced: numbered platform options,
- [ ] AC-08-034: Enumerated item is supported/enforced: Something else,
- [ ] AC-08-035: Enumerated item is supported/enforced: Discuss,
- [ ] AC-08-036: Enumerated item is supported/enforced: custom prose support.
- [ ] AC-08-037: Enumerated item is supported/enforced: label,
- [ ] AC-08-038: Enumerated item is supported/enforced: description,
- [ ] AC-08-039: Enumerated item is supported/enforced: benefits,
- [ ] AC-08-040: Enumerated item is supported/enforced: costs/tradeoffs,
- [ ] AC-08-041: Enumerated item is supported/enforced: downstream constraints or lock-in where relevant.
