# US-24: Shared action contracts

Derived from: [Appendix B. Shared Action Contracts](../agentic-redesign-references.md#us-24-source)

## Problem

All interfaces need shared action result and action contracts so CLI, MCP, Pi, and harness integrations invoke the same governed workflow.

## User story

As a API implementer, I want shared action contracts implemented, so that all interfaces need shared action result and action contracts so CLI, MCP, Pi, and harness integrations invoke the same governed workflow.

## In scope

- Define shared action result.
- Define required actions and human-gated action requirements.
- Validate inputs, outputs, lifecycle effects, and diagnostics consistently.

## Out of scope

- Interface-specific action behavior that changes governance semantics.
- Actions that bypass required snapshot, approval, authorization, or evidence checks.

## Acceptance criteria

- [ ] Shared action result fields are returned consistently.
- [ ] Required actions exist with the specified input/output and mutation semantics.
- [ ] Human-gated actions enforce prompt, selected number, raw response, snapshot hash/revision, and source-ref requirements.
- [ ] Action contracts are reusable by CLI, MCP, Pi, viewer, and generated harness integrations.
- [ ] Invalid action inputs return structured diagnostics without illegal state mutation.
