# US-00: Implementation discipline

Derived from: [0. Implementation Discipline](../agentic-redesign-references.md#us-00-source)

## Problem

Spec Guard needs a predictable test-first implementation workflow so agents do not invent behavior or ship unvalidated changes.

## User story

As a implementation agent, I want implementation discipline implemented, so that spec Guard needs a predictable test-first implementation workflow so agents do not invent behavior or ship unvalidated changes.

## In scope

- Require tests to be written or updated before production behavior changes.
- Require targeted and full validation around implementation work.
- Require agents to stop and ask when the specification is ambiguous.

## Out of scope

- Defining the complete test suite contents for every later story.
- Allowing speculative implementation when required behavior is unclear.

## Acceptance criteria

- [ ] For every required behavior, tests are written or updated before production changes are made.
- [ ] Agents run tests and observe an expected failure before implementing behavior.
- [ ] Agents implement the smallest production change needed, then re-run targeted tests.
- [ ] Agents re-run full validation before packaging or release.
- [ ] Ambiguities that block implementation cause the agent to stop and ask instead of inventing hidden requirements.
