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

- [ ] The system distinguishes proposals from accepted canonical intent.
- [ ] Broad work is split into traceable bounded packets.
- [ ] Implementation cannot start until approval, authorization, and pre-implementation validation are satisfied.
- [ ] Docs, tests, and failure evidence precede implementation source changes where required.
- [ ] Runtime evidence and final claims are evidence-backed.
- [ ] Critical truth comes only from human decisions, deterministic observations, backend verification of required claims, or auditable artifacts.
