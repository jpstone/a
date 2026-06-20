# US-19: Tests-first coverage plan

Derived from: [19. Tests First Plan](../agentic-redesign-references.md#us-19-source)

## Problem

The redesign needs explicit test coverage areas so implementation can be validated across authority, decisions, evidence, integrations, and migration.

## User story

As a test author, I want tests-first coverage plan implemented, so that the redesign needs explicit test coverage areas so implementation can be validated across authority, decisions, evidence, integrations, and migration.

## In scope

- Define test coverage for choice/authority, decision binding, AC/approval flow, baselines, classification/docs, backend verification, pre-implementation/review, and CLI/MCP/viewer.
- Use the coverage plan to drive test-first implementation.

## Out of scope

- Treating the listed coverage as optional guidance.
- Implementing production features before their required tests exist.

## Acceptance criteria

- [ ] Tests cover choice and authority semantics.
- [ ] Tests cover review snapshots, approved fields, decisions, and invalidation.
- [ ] Tests cover AC approval, packet approval, authorization, Plans, and batch behavior.
- [ ] Tests cover runtime and packet change baselines.
- [ ] Tests cover classification/docs and validation chains.
- [ ] Tests cover backend verifier, pre-implementation, review, final claims, CLI/MCP/viewer, and migration.
