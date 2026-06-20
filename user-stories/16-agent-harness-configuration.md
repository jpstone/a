# US-16: Agent harness configuration

Derived from: [16. Agent Harness Configuration](../agentic-redesign-references.md#us-16-source)

## Problem

Generated agent harnesses need configuration that instructs agents to use governed workflows consistently across supported environments.

## User story

As a agent harness maintainer, I want agent harness configuration implemented, so that generated agent harnesses need configuration that instructs agents to use governed workflows consistently across supported environments.

## In scope

- Generate or maintain harness configuration artifacts.
- Include governance instructions for prompts, approvals, authorization, evidence, validation, and final claims.
- Support configured integrations without weakening governance.

## Out of scope

- Letting harness instructions bypass Spec Guard gates.
- Embedding secrets directly in generated configuration.

## Acceptance criteria

- [ ] Harness configuration includes required Spec Guard workflow instructions.
- [ ] Agents are instructed to use numbered human gates for governed choices.
- [ ] Agents are instructed not to implement before authorization and pre-implementation validation.
- [ ] Evidence, verifier, review, and final-claim expectations are included.
- [ ] Generated configuration is compatible with supported CLI/MCP/Pi workflows.
