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

<!-- Expanded from agentic-redesign.md to provide behavior-level coverage. -->

- [ ] AC-05-001: Spec Guard distinguishes top-level artifacts from embedded records.
- [ ] AC-05-002: Top-level artifacts are independently stored JSON documents.
- [ ] AC-05-003: They must include:
- [ ] AC-05-004: Top-level artifacts include:
- [ ] AC-05-005: SourceArtifact records,
- [ ] AC-05-006: standalone decision artifacts when used,
- [ ] AC-05-007: CommandResult records when stored separately,
- [ ] AC-05-008: verifier configuration when stored separately.
- [ ] AC-05-009: A newly created top-level artifact starts at governed `revision: 1`.
- [ ] AC-05-010: A governed mutating write to a top-level artifact increments `revision`
- [ ] AC-05-011: updates governed `updated_at`.
- [ ] AC-05-012: Audit-only writes, including persisted review snapshots and prompt audit records, must not increment the governed `revision` or governed `updated_at` used for approval staleness.
- [ ] AC-05-013: Audit-only records have their own `created_at`/audit sequencing.
- [ ] AC-05-014: If an implementation stores audit records physically inside a top-level artifact file, it must maintain separate audit sequencing
- [ ] AC-05-015: must not make the governed artifact revision stale solely because an audit record was appended.
- [ ] AC-05-016: The governed projection is the artifact JSON at that revision after removing audit-only appendices, physical-storage metadata, and fields whose schema explicitly says they are excluded from that artifact's hash, but retaining governed timestamps, revision, status, decisions, lifecycle, evidence, and diagnostics unless a named snapshot payload excludes them.
- [ ] AC-05-017: Revision storage must persist this hash with the immutable revision record.
- [ ] AC-05-018: Any artifact revision referenced by SourceArtifactRef, review snapshot source refs, approval records, or staleness checks must be revision-addressable after later writes.
- [ ] AC-05-019: Implementations may store full historical snapshots or immutable content-addressed revision records, but they must be able to resolve the exact referenced revision and its hash-relevant canonical content.
- [ ] AC-05-020: When audit-only records are physically stored inside an artifact file, the governed artifact content hash/projection must exclude those audit appendices
- [ ] AC-05-021: physical file hashes must not be used as governed revision hashes unless the storage format separates audit data.
- [ ] AC-05-022: Embedded records live inside top-level artifacts unless an implementation explicitly stores them as top-level artifacts too.
- [ ] AC-05-023: Embedded records do not need top-level artifact common fields unless persisted independently.
- [ ] AC-05-024: Every HumanDecision must be retained in a durable append-only decision log.
- [ ] AC-05-025: The decision log may be embedded in the owning artifact or stored as standalone decision artifacts.
- [ ] AC-05-026: Decisions that do not yet have an owning artifact, such as declined Plan approvals that create no Plan, must be stored as standalone decision artifacts or in a project-level decision log.
- [ ] AC-05-027: Changing an active slot must not delete or overwrite prior decisions in the decision log.
- [ ] AC-05-028: Every CommandResult must be retained in durable storage addressable by `command_result_ref`.
- [ ] AC-05-029: CommandResults may be embedded in the related Work Packet, embedded in the runtime baseline for baseline validation commands, or stored as standalone CommandResult records.
- [ ] AC-05-030: Evidence records reference CommandResults
- [ ] AC-05-031: Embedded records include:
- [ ] AC-05-032: Embedded record schemas are defined in Appendix A.
- [ ] AC-05-033: Enumerated item is supported/enforced: `artifact_type`,
- [ ] AC-05-034: Enumerated item is supported/enforced: `schema_version`,
- [ ] AC-05-035: Enumerated item is supported/enforced: `id` except singletons,
- [ ] AC-05-036: Enumerated item is supported/enforced: `revision`,
- [ ] AC-05-037: Enumerated item is supported/enforced: `created_at`,
- [ ] AC-05-038: Enumerated item is supported/enforced: `updated_at`,
- [ ] AC-05-039: Enumerated item is supported/enforced: diagnostics where applicable.
- [ ] AC-05-040: Enumerated item is supported/enforced: config,
- [ ] AC-05-041: Enumerated item is supported/enforced: runtime baseline,
- [ ] AC-05-042: Enumerated item is supported/enforced: Work Packet,
- [ ] AC-05-043: Enumerated item is supported/enforced: Plan,
- [ ] AC-05-044: Enumerated item is supported/enforced: SourceArtifact records,
- [ ] AC-05-045: Enumerated item is supported/enforced: standalone decision artifacts when used,
- [ ] AC-05-046: Enumerated item is supported/enforced: CommandResult records when stored separately,
- [ ] AC-05-047: Enumerated item is supported/enforced: verifier configuration when stored separately.
- [ ] AC-05-048: Enumerated item is supported/enforced: HumanDecision,
- [ ] AC-05-049: Enumerated item is supported/enforced: EvidenceRecord,
- [ ] AC-05-050: Enumerated item is supported/enforced: PacketChangeBaseline,
- [ ] AC-05-051: Enumerated item is supported/enforced: BackendVerification,
- [ ] AC-05-052: Enumerated item is supported/enforced: BatchReviewSnapshot,
- [ ] AC-05-053: Enumerated item is supported/enforced: BatchProceedRecord,
- [ ] AC-05-054: Enumerated item is supported/enforced: ReviewSnapshot,
- [ ] AC-05-055: Enumerated item is supported/enforced: ChoicePrompt,
- [ ] AC-05-056: Enumerated item is supported/enforced: ChoiceAnswer,
- [ ] AC-05-057: Enumerated item is supported/enforced: ProductContext,
- [ ] AC-05-058: Enumerated item is supported/enforced: CommandResult,
- [ ] AC-05-059: Enumerated item is supported/enforced: DocsRequirement,
- [ ] AC-05-060: Enumerated item is supported/enforced: AcceptanceCriterion,
- [ ] AC-05-061: Enumerated item is supported/enforced: LifecycleEvent,
- [ ] AC-05-062: Enumerated item is supported/enforced: Claim,
- [ ] AC-05-063: Enumerated item is supported/enforced: VerifierFinding.
