# US-02: Authority model

Derived from: [2. Authority Model](../agentic-redesign-references.md#us-02-source)

## Problem

Governed questions must route to the correct authority so human intent, deterministic facts, frontend drafting, and backend semantic verification do not overwrite each other.

## User story

As a Spec Guard integrator, I want authority model implemented, so that governed questions must route to the correct authority so human intent, deterministic facts, frontend drafting, and backend semantic verification do not overwrite each other.

## In scope

- Classify governed questions by qualified authority.
- Split mixed questions before asking or validating them.
- Preserve human authority over product intent, approvals, authorization, and plan decisions.
- Limit frontend agents to drafts, proposals, and claims until gates validate them.
- Assign deterministic facts and lifecycle enforcement to the deterministic kernel.
- Constrain backend verification to required semantic checks that do not judge human intent.

## Out of scope

- Letting backend verifier create or alter product intent.
- Letting deterministic checks decide product desirability or correctness.
- Letting frontend-agent prose become critical truth without a gate.

## Acceptance criteria

<!-- Expanded from agentic-redesign.md to provide behavior-level coverage. -->

- [ ] AC-02-001: Every governed question must route to exactly one qualified authority.
- [ ] AC-02-002: Mixed questions must be split.
- [ ] AC-02-003: Once approved, human intent is canonical until changed through a recorded human decision.
- [ ] AC-02-004: source-derived ACs with source/evidence,
- [ ] AC-02-005: embedded record storage inside artifacts,
- [ ] AC-02-006: packet change baseline capture,
- [ ] AC-02-007: command execution records,
- [ ] AC-02-008: Observable facts must be checked deterministically.
- [ ] AC-02-009: The backend verifier checks required semantic frontend-agent claims listed in section 13.
- [ ] AC-02-010: It must not:
- [ ] AC-02-011: create or alter product intent,
- [ ] AC-02-012: approve or reject work,
- [ ] AC-02-013: Enumerated item is supported/enforced: product/platform type,
- [ ] AC-02-014: Enumerated item is supported/enforced: architecture choice,
- [ ] AC-02-015: Enumerated item is supported/enforced: desired product behavior,
- [ ] AC-02-016: Enumerated item is supported/enforced: acceptance criteria approval,
- [ ] AC-02-017: Enumerated item is supported/enforced: Work Packet approval,
- [ ] AC-02-018: Enumerated item is supported/enforced: implementation authorization,
- [ ] AC-02-019: Enumerated item is supported/enforced: runtime baseline acceptance,
- [ ] AC-02-020: Enumerated item is supported/enforced: Plan-vs-single-packet choice,
- [ ] AC-02-021: Enumerated item is supported/enforced: Plan approval,
- [ ] AC-02-022: Enumerated item is supported/enforced: source/mockup/design interpretation as represented in approved ACs.
- [ ] AC-02-023: Enumerated item is supported/enforced: goals,
- [ ] AC-02-024: Enumerated item is supported/enforced: desired outcomes,
- [ ] AC-02-025: Enumerated item is supported/enforced: in-scope and out-of-scope lists,
- [ ] AC-02-026: Enumerated item is supported/enforced: users/actors,
- [ ] AC-02-027: Enumerated item is supported/enforced: edge cases,
- [ ] AC-02-028: Enumerated item is supported/enforced: open questions,
- [ ] AC-02-029: Enumerated item is supported/enforced: acceptance criteria,
- [ ] AC-02-030: Enumerated item is supported/enforced: platform options,
- [ ] AC-02-031: Enumerated item is supported/enforced: architecture options,
- [ ] AC-02-032: Enumerated item is supported/enforced: source-derived ACs with source/evidence,
- [ ] AC-02-033: Enumerated item is supported/enforced: Plan slices,
- [ ] AC-02-034: Enumerated item is supported/enforced: implementation summaries,
- [ ] AC-02-035: Enumerated item is supported/enforced: review summaries,
- [ ] AC-02-036: Enumerated item is supported/enforced: final response drafts.
- [ ] AC-02-037: Enumerated item is supported/enforced: action registry,
- [ ] AC-02-038: Enumerated item is supported/enforced: top-level artifact storage,
- [ ] AC-02-039: Enumerated item is supported/enforced: embedded record storage inside artifacts,
- [ ] AC-02-040: Enumerated item is supported/enforced: schema validation,
- [ ] AC-02-041: Enumerated item is supported/enforced: lifecycle transitions,
- [ ] AC-02-042: Enumerated item is supported/enforced: human gate recording,
- [ ] AC-02-043: Enumerated item is supported/enforced: runtime baseline validation,
- [ ] AC-02-044: Enumerated item is supported/enforced: packet change baseline capture,
- [ ] AC-02-045: Enumerated item is supported/enforced: changed-file computation,
- [ ] AC-02-046: Enumerated item is supported/enforced: path and glob validation,
- [ ] AC-02-047: Enumerated item is supported/enforced: command execution records,
- [ ] AC-02-048: Enumerated item is supported/enforced: docs/test/failure-first ordering checks,
- [ ] AC-02-049: Enumerated item is supported/enforced: review snapshot hash computation,
- [ ] AC-02-050: Enumerated item is supported/enforced: approval invalidation,
- [ ] AC-02-051: Enumerated item is supported/enforced: verifier response schema validation,
- [ ] AC-02-052: Enumerated item is supported/enforced: CLI/MCP parity,
- [ ] AC-02-053: Enumerated item is supported/enforced: viewer data,
- [ ] AC-02-054: Enumerated item is supported/enforced: migration.
- [ ] AC-02-055: Enumerated item is supported/enforced: create or alter product intent,
- [ ] AC-02-056: Enumerated item is supported/enforced: approve or reject work,
- [ ] AC-02-057: Enumerated item is supported/enforced: authorize implementation,
- [ ] AC-02-058: Enumerated item is supported/enforced: choose platform or architecture,
- [ ] AC-02-059: Enumerated item is supported/enforced: judge human-approved ACs, scope, platform, architecture, docs requirement, Plan slices, or source interpretation.
- [ ] AC-02-060: Table row is implemented: Question type: Product intent, platform, architecture, AC approval, Work Packet approval, implementation authorization, runtime baseline acceptance, Plan-vs-single decision, Plan approval; Authority: Human
- [ ] AC-02-061: Table row is implemented: Question type: Ordinary drafting before approval; Authority: Frontend agent, later reviewed through human gates
- [ ] AC-02-062: Table row is implemented: Question type: Files, paths, commands, timestamps, diffs, schemas, lifecycle, hashes, config, recorded decisions; Authority: Deterministic kernel
- [ ] AC-02-063: Table row is implemented: Question type: Required semantic checks of frontend-agent claims that do not mutate or judge human intent; Authority: Backend verifier
