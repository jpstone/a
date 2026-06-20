# US-01: Governance objective and critical truth

Derived from: [1. Objective](../agentic-redesign-references.md#us-01-source)

## Problem

Agent-driven development needs governed truth sources so proposals, approvals, runtime evidence, and final claims remain auditable and consistent across integrations.

## User story

As a project maintainer, I want governance objective and critical truth implemented, so that agent-driven development needs governed truth sources so proposals, approvals, runtime evidence, and final claims remain auditable and consistent across integrations.

## In scope

- Capture human intent explicitly.
- Keep frontend-agent proposals non-canonical until accepted through a gate.
- Make human-approved content canonical until changed by recorded decision.
- Require traceable bounded work, approval, authorization, pre-implementation validation, evidence, and final claim support.
- Expose the same governed workflow through CLI, MCP, Pi, viewer, and generated harnesses.

## Out of scope

- Treating frontend-agent claims alone as critical truth.
- Using undocumented behavior as a source of governance truth.

## Acceptance criteria

<!-- Expanded from agentic-redesign.md to provide behavior-level coverage. -->

- [ ] AC-01-001: human intent is explicitly captured,
- [ ] AC-01-002: implementation starts only after approval, authorization, and pre-implementation validation,
- [ ] AC-01-003: required docs, tests, and failure evidence precede implementation source changes,
- [ ] AC-01-004: source/mockup/design-derived ACs are visible with source evidence before approval,
- [ ] AC-01-005: CLI, MCP, Pi, viewer, and generated agent-harness integrations expose the same governed workflow.
- [ ] AC-01-006: Critical truth must come from:
- [ ] AC-01-007: backend verification of required semantic frontend-agent claims,
- [ ] AC-01-008: Frontend-agent claims alone are never critical truth.
- [ ] AC-01-009: Enumerated item is supported/enforced: human intent is explicitly captured,
- [ ] AC-01-010: Enumerated item is supported/enforced: frontend-agent proposals remain proposals until accepted through the proper gate,
- [ ] AC-01-011: Enumerated item is supported/enforced: human-approved content is canonical intent,
- [ ] AC-01-012: Enumerated item is supported/enforced: broad work is split into traceable bounded packets,
- [ ] AC-01-013: Enumerated item is supported/enforced: implementation starts only after approval, authorization, and pre-implementation validation,
- [ ] AC-01-014: Enumerated item is supported/enforced: required docs, tests, and failure evidence precede implementation source changes,
- [ ] AC-01-015: Enumerated item is supported/enforced: source/mockup/design-derived ACs are visible with source evidence before approval,
- [ ] AC-01-016: Enumerated item is supported/enforced: runtime evidence and final claims are evidence-backed,
- [ ] AC-01-017: Enumerated item is supported/enforced: CLI, MCP, Pi, viewer, and generated agent-harness integrations expose the same governed workflow.
- [ ] AC-01-018: Enumerated item is supported/enforced: explicit human decisions,
- [ ] AC-01-019: Enumerated item is supported/enforced: deterministic observations,
- [ ] AC-01-020: Enumerated item is supported/enforced: backend verification of required semantic frontend-agent claims,
- [ ] AC-01-021: Enumerated item is supported/enforced: auditable artifacts.
