# US-17: Viewer requirements

Derived from: [17. Viewer Requirements](../agentic-redesign-references.md#us-17-source)

## Problem

Humans need a viewer that makes governed state, review surfaces, decisions, diagnostics, and evidence understandable without changing authority rules.

## User story

As a human reviewer, I want viewer requirements implemented, so that humans need a viewer that makes governed state, review surfaces, decisions, diagnostics, and evidence understandable without changing authority rules.

## In scope

- Display work packets, plans, baselines, decisions, snapshots, evidence, diagnostics, and readiness.
- Support human-readable review surfaces matching agent prompts.
- Expose invalidation and traceability information.

## Out of scope

- Using viewer display as a separate source of truth from stored artifacts.
- Letting viewer edits bypass registered actions or gates.

## Acceptance criteria

- [ ] Viewer displays current lifecycle/readiness for packets, plans, and baselines.
- [ ] Viewer can show decision surfaces equivalent to governed review snapshots.
- [ ] Viewer shows approval, authorization, invalidation, evidence, backend verification, changed files, and diagnostics.
- [ ] Viewer distinguishes proposals, accepted intent, stale approvals, and blocked states.
- [ ] Viewer data is derived from deterministic artifacts and action results.
