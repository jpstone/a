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

- [ ] Every governed question routes to exactly one qualified authority.
- [ ] Mixed questions are split before resolution.
- [ ] Human decisions remain canonical until changed through a recorded human decision.
- [ ] Frontend-agent outputs are treated as proposals or claims unless accepted or validated by the proper mechanism.
- [ ] Deterministic kernel owns schema, storage, lifecycle, path, command, evidence-ordering, hash, CLI/MCP, viewer, and migration facts.
- [ ] Verifier responses that judge human-approved intent are invalid for satisfying gates.
