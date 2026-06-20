# US-05: Artifact and record model

Derived from: [5. Artifact and Record Model](../agentic-redesign-references.md#us-05-source)

## Problem

Governed artifacts and embedded records need durable revisioning and hashing so references, decisions, evidence, and audit logs remain replayable.

## User story

As a storage implementer, I want artifact and record model implemented, so that governed artifacts and embedded records need durable revisioning and hashing so references, decisions, evidence, and audit logs remain replayable.

## In scope

- Define common top-level artifact fields.
- Separate governed revisions from audit-only writes.
- Persist immutable revision-addressable content hashes.
- Retain HumanDecision and CommandResult logs durably.
- Define embedded records and optional standalone storage.

## Out of scope

- Letting audit-only appends stale governed approvals.
- Using physical file hashes as governed hashes when audit appendices are mixed in.
- Overwriting or deleting prior decisions through convenience current slots.

## Acceptance criteria

- [ ] Top-level artifacts include artifact type, schema version, revision, timestamps, and diagnostics where applicable.
- [ ] Governed mutating writes increment artifact revision and governed updated_at.
- [ ] Audit-only writes use separate sequencing and do not increment governed revision.
- [ ] Referenced artifact revisions remain resolvable after later writes.
- [ ] HumanDecision logs are append-only and durable.
- [ ] CommandResults are retained in durable storage addressable by command_result_ref.
