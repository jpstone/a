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

<!-- Expanded from agentic-redesign.md to provide behavior-level coverage. -->

- [ ] AC-09-001: For any prompt requiring repository mutation, the frontend agent should draft:
- [ ] AC-09-002: Required fields for moving from `draft` to `pending_ac_approval` are exactly: non-empty `title`, non-empty `intent.goal`, and at least one AcceptanceCriterion.
- [ ] AC-09-003: Spec Guard should not prompt separately for every non-AC intent field by default.
- [ ] AC-09-004: Generated fields must not contain placeholders, `undefined`, or process boilerplate.
- [ ] AC-09-005: When ACs are derived from source, mockup, design, screenshot, PDF, UI artifact, user story, or other interpreted material:
- [ ] AC-09-006: they must be included in the displayed AC list,
- [ ] AC-09-007: each source-derived AC must show source/evidence,
- [ ] AC-09-008: the review surface must clearly mark which ACs are source-derived,
- [ ] AC-09-009: source-derived ACs are never batch-approved or batch-authorized,
- [ ] AC-09-010: any packet containing source-derived ACs may be batch-created only
- [ ] AC-09-011: must then use normal per-child AC approval, Work Packet approval, and authorization gates,
- [ ] AC-09-012: there is no separate one-AC-at-a-time source-derived approval flow,
- [ ] AC-09-013: Yes on AC approval approves the displayed AC list, including displayed source-derived ACs and their source/evidence.
- [ ] AC-09-014: Spec Guard must not infer canonical source-derived ACs without human approval.
- [ ] AC-09-015: Source material used for source-derived ACs must be represented by a resolvable SourceArtifactRef.
- [ ] AC-09-016: Spec Guard must not maintain a closed list of acceptable source kinds.
- [ ] AC-09-017: A SourceArtifact revision must be immutable and content-addressed.
- [ ] AC-09-018: SourceArtifact registration must capture bytes or a deterministic descriptor plus content hash sufficient to identify and review the material later.
- [ ] AC-09-019: Hash-only registration is invalid unless the descriptor includes a deterministic retrieval mechanism and enough metadata for the reviewed material to be presented again.
- [ ] AC-09-020: Every SourceArtifact revision must include an immutable `content_ref` or descriptor retrieval mechanism that allows the reviewed material or deterministic descriptor to be re-presented.
- [ ] AC-09-021: A source that cannot be assigned a stable id, immutable revision, and content hash cannot satisfy source-derived AC evidence.
- [ ] AC-09-022: `source_artifact.register` creates revision 1 for new source material.
- [ ] AC-09-023: `source_artifact.update` creates a new immutable revision
- [ ] AC-09-024: must not alter prior revisions.
- [ ] AC-09-025: SourceArtifactRefs used in approved source-derived ACs must resolve at review time and at later staleness checks.
- [ ] AC-09-026: Built-in artifact refs must use the exact `artifact_type` stored on the artifact.
- [ ] AC-09-027: `source_artifact.register` and `source_artifact.update` accept exactly one of captured bytes or descriptor input.
- [ ] AC-09-028: For captured bytes, callers provide `content_bytes_base64`
- [ ] AC-09-029: Spec Guard decodes base64, computes SHA-256 over the decoded bytes, stores the bytes in immutable blob storage, sets `content_ref` to that blob reference,
- [ ] AC-09-030: stores `descriptor: null`.
- [ ] AC-09-031: Spec Guard canonicalizes the descriptor JSON, computes SHA-256 over the canonical descriptor bytes unless `content_hash` is supplied and matches that canonical hash, stores the descriptor as immutable content,
- [ ] AC-09-032: sets `content_ref` to the descriptor record.
- [ ] AC-09-033: Hash-only input without bytes or descriptor is invalid.
- [ ] AC-09-034: On update, absent metadata fields inherit the prior revision
- [ ] AC-09-035: `locator: null` explicitly clears the locator
- [ ] AC-09-036: The snapshot includes the complete AC payload being reviewed, source/evidence for source-derived ACs, snapshot hash, and snapshot revision.
- [ ] AC-09-037: `work.ac.approve` must validate the supplied review snapshot hash against `AcReviewSnapshotPayload`, not against the raw AC array alone.
- [ ] AC-09-038: compares that hash to `review_snapshot_hash`.
- [ ] AC-09-039: records AC approval.
- [ ] AC-09-040: On numbered No, Spec Guard records decline or blocks as appropriate without approving the AC payload.
- [ ] AC-09-041: On Discuss, the action records no mutation and should not be called to persist refinements.
- [ ] AC-09-042: Yes records AC approval bound to the displayed AC review snapshot hash.
- [ ] AC-09-043: No records decline or blocks as appropriate.
- [ ] AC-09-044: Discuss records no mutation.
- [ ] AC-09-045: During Discuss, the frontend agent may refine ACs in the agent session only.
- [ ] AC-09-046: Intermediate AC refinements during Discuss must not mutate canonical ACs, approval state, decline state, or artifact hashes.
- [ ] AC-09-047: After refinement, the frontend agent must re-present the current proposed ACs through the same Yes/No/Discuss gate.
- [ ] AC-09-048: The loop resolves only through numbered Yes or numbered No.
- [ ] AC-09-049: The backend verifier must not judge whether approved ACs are correct or complete.
- [ ] AC-09-050: Enumerated item is supported/enforced: goal,
- [ ] AC-09-051: Enumerated item is supported/enforced: desired outcomes,
- [ ] AC-09-052: Enumerated item is supported/enforced: in scope,
- [ ] AC-09-053: Enumerated item is supported/enforced: out of scope,
- [ ] AC-09-054: Enumerated item is supported/enforced: users/actors if relevant,
- [ ] AC-09-055: Enumerated item is supported/enforced: edge cases if relevant,
- [ ] AC-09-056: Enumerated item is supported/enforced: open questions if any,
- [ ] AC-09-057: Enumerated item is supported/enforced: ACs.
- [ ] AC-09-058: Enumerated item is supported/enforced: they must be included in the displayed AC list,
- [ ] AC-09-059: Enumerated item is supported/enforced: each source-derived AC must show source/evidence,
- [ ] AC-09-060: Enumerated item is supported/enforced: the review surface must clearly mark which ACs are source-derived,
- [ ] AC-09-061: Enumerated item is supported/enforced: the human approves them through the same AC approval gate as all other ACs,
- [ ] AC-09-062: Enumerated item is supported/enforced: source-derived ACs are never batch-approved or batch-authorized,
- [ ] AC-09-063: Enumerated item is supported/enforced: any packet containing source-derived ACs may be batch-created only and must then use normal per-child AC approval, Work Packet approval, and authorization gates,
- [ ] AC-09-064: Enumerated item is supported/enforced: there is no separate one-AC-at-a-time source-derived approval flow,
- [ ] AC-09-065: Enumerated item is supported/enforced: there is no custom feature-status prompt.
- [ ] AC-09-066: Ordered requirement is supported/enforced: Yes
- [ ] AC-09-067: Ordered requirement is supported/enforced: No
- [ ] AC-09-068: Ordered requirement is supported/enforced: Discuss
- [ ] AC-09-069: Enumerated item is supported/enforced: Yes records AC approval bound to the displayed AC review snapshot hash.
- [ ] AC-09-070: Enumerated item is supported/enforced: No records decline or blocks as appropriate.
- [ ] AC-09-071: Enumerated item is supported/enforced: Discuss records no mutation.
- [ ] AC-09-072: Enumerated item is supported/enforced: During Discuss, the frontend agent may refine ACs in the agent session only.
- [ ] AC-09-073: Enumerated item is supported/enforced: Intermediate AC refinements during Discuss must not mutate canonical ACs, approval state, decline state, or artifact hashes.
- [ ] AC-09-074: Enumerated item is supported/enforced: After refinement, the frontend agent must re-present the current proposed ACs through the same Yes/No/Discuss gate.
- [ ] AC-09-075: Enumerated item is supported/enforced: The loop resolves only through numbered Yes or numbered No.
