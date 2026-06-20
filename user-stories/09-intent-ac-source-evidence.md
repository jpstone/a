# US-09: Intent, source-derived ACs, and AC approval

Derived from: [9. Intent and AC Approval](../agentic-redesign-references.md#us-09-source)

## Problem

Acceptance criteria need explicit review and source evidence so approved implementation expectations are human-owned and traceable.

## User story

As a acceptance criteria approver, I want intent, source-derived acs, and ac approval implemented, so that acceptance criteria need explicit review and source evidence so approved implementation expectations are human-owned and traceable.

## In scope

- Draft intent fields and acceptance criteria.
- Represent source/mockup/design-derived ACs with source evidence.
- Register source artifacts immutably.
- Produce AC review snapshots and enforce AC approval gate.

## Out of scope

- Treating source-derived interpretation as approved without human AC approval.
- Approving ACs from unverifiable or unregistered source evidence.
- Letting backend verifier judge approved source interpretation.

## Acceptance criteria

- [ ] Drafted intent remains proposal until approved through gates.
- [ ] Source-derived ACs include required source/evidence metadata.
- [ ] Source artifacts are registered with immutable content identity and refs.
- [ ] AC review snapshot includes reviewed AC payload and source refs.
- [ ] AC approval uses Yes/No/Discuss binary gate and records approved_fields for acceptance_criteria only.
- [ ] Source-derived ACs must be visible with evidence before approval.
