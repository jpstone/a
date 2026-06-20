# US-23: Normative schemas

Derived from: [Appendix A. Normative Schemas](../agentic-redesign-references.md#us-23-source)

## Problem

Implementations need concrete field contracts for artifacts and embedded records so storage, validation, APIs, and viewers interoperate.

## User story

As a schema implementer, I want normative schemas implemented, so that implementations need concrete field contracts for artifacts and embedded records so storage, validation, APIs, and viewers interoperate.

## In scope

- Define common top-level fields, diagnostics, HumanDecision, Config, VerifierConfig, RuntimeBaseline, PacketChangeBaseline, WorkPacket, Plan, EvidenceRecord, BackendVerification, BatchReviewSnapshot, and supporting embedded types.
- Validate required fields and allowed shapes.

## Out of scope

- Adding fields that weaken required behavior.
- Treating schemas as examples instead of normative contracts.

## Acceptance criteria

- [ ] Each normative schema is implemented with required field names, types, enums, and nullability.
- [ ] Schema validation rejects records that violate normative field contracts.
- [ ] Implementations may add fields only when they do not weaken required behavior.
- [ ] Schema support is sufficient for snapshot hashing, artifact refs, decisions, evidence, verifier records, batch records, and viewer data.
