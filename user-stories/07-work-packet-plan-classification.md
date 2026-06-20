# US-07: Work packets, plans, and classification

Derived from: [7. Work Packet, Plan, and Classification](../agentic-redesign-references.md#us-07-source)

## Problem

Spec Guard needs bounded work packets, multi-slice plans, and classification rules to keep implementation scope explicit and enforceable.

## User story

As a work planner, I want work packets, plans, and classification implemented, so that spec Guard needs bounded work packets, multi-slice plans, and classification rules to keep implementation scope explicit and enforceable.

## In scope

- Define Work Packet lifecycle states and required packet content.
- Define Plan content and statuses.
- Define work classification enum and docs requirements by classification.
- Handle API/contract-surface and non-API packet policies.

## Out of scope

- Implementing unbounded work without packet scope.
- Skipping required API/contract docs for reusable/API/contract-surface work.
- Using docs policy to weaken classification requirements.

## Acceptance criteria

- [ ] Work Packets support the specified lifecycle status enum.
- [ ] Work Packets store title, classification, intent, ACs, evidence, docs policy, allowed globs, platform, architecture, runtime baseline, approvals, authorization, and review traceability.
- [ ] Plans support proposed, approved, in_progress, completed, blocked, deferred, and archived states.
- [ ] Classification determines required docs and validation chains.
- [ ] API/contract-surface packets require appropriate docs and tests.
- [ ] Non-API packets may use none_required/not_applicable policies only with concrete reasons where allowed.
