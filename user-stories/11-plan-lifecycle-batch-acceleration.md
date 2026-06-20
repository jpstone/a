# US-11: Plan lifecycle and batch acceleration

Derived from: [11. Plan Lifecycle and Batch Acceleration](../agentic-redesign-references.md#us-11-source)

## Problem

Broad work needs an explicit plan-vs-single decision and safe batch acceleration for eligible child packets without losing per-child governance.

## User story

As a plan approver, I want plan lifecycle and batch acceleration implemented, so that broad work needs an explicit plan-vs-single decision and safe batch acceleration for eligible child packets without losing per-child governance.

## In scope

- Record Plan-vs-single fixed binary decision.
- Generate non-mutating Plan proposals.
- Approve Plans through snapshot-bound gate.
- Create/proceed with Plan children through batch options and batch review snapshot.
- Record child approvals/authorizations from batch where eligible.

## Out of scope

- Using backend verifier for Plan-vs-single or Plan approval.
- Batch-approving source-derived AC children.
- Creating child approvals when proposed and created payloads differ.

## Acceptance criteria

<!-- Expanded from agentic-redesign.md to provide behavior-level coverage. -->

- [ ] AC-11-001: Before asking whether work should be a single packet or a Plan, the frontend agent must present relevant ACs unless already in a valid Plan flow.
- [ ] AC-11-002: Create a Plan
- [ ] AC-11-003: Option 1 records single-packet decision and leaves the source Work Packet active.
- [ ] AC-11-004: Option 2 records Plan decision, sets the source Work Packet to `deferred` with diagnostics pointing to the Plan flow, and later Plan approval records `source_work_id` on the Plan.
- [ ] AC-11-005: If Plan approval is declined or no Plan is created, Spec Guard restores the source Work Packet to its pre-deferral status
- [ ] AC-11-006: records diagnostics linking the declined Plan attempt.
- [ ] AC-11-007: Option 3 mutates nothing, creates no HumanDecision, and re-prompts later.
- [ ] AC-11-008: No Something else/custom option is allowed.
- [ ] AC-11-009: The decision must be recorded through `work.plan_choice.answer`.
- [ ] AC-11-010: It must not be recorded through generic `decision.create`, because option 2 has the side effect of deferring the source Work Packet.
- [ ] AC-11-011: The recorded HumanDecision must store a canonical PlanVsSingleDecisionPayload in `approved_payload` with the work id, selected option, the exact AC payload presented before the decision, and its hash.
- [ ] AC-11-012: It returns a proposed Plan review snapshot for that exact payload.
- [ ] AC-11-013: It does not create a Plan
- [ ] AC-11-014: does not create children.
- [ ] AC-11-015: Every slice `proposed_id` must match `^[A-Za-z0-9._-]+$`
- [ ] AC-11-016: `plan.propose` and `plan.approve` must reject Plan proposals with proposed ids that cannot be used safely in batch child snapshot revisions.
- [ ] AC-11-017: Every Plan slice must include at least one full AcceptanceCriterion payload.
- [ ] AC-11-018: Any Plan slice containing source-derived ACs must include full AC payloads, not only AC ids, and each source-derived AC must include SourceEvidence with non-empty canonical `source_artifact_refs` and `evidence_hash`.
- [ ] AC-11-019: The Plan proposal is shown to the human with:
- [ ] AC-11-020: Spec Guard validates that the submitted payload hashes to the supplied snapshot hash.
- [ ] AC-11-021: any top-level `source_work_id` action input must equal the payload field.
- [ ] AC-11-022: Numbered Yes records Plan approval
- [ ] AC-11-023: creates a non-implementable Plan containing the approved slices, `source_work_id`, and metadata.
- [ ] AC-11-024: Plan approval does not create child Work Packets.
- [ ] AC-11-025: The created Plan stores the approved PlanProposalPayload as `plan_proposal`
- [ ] AC-11-026: stores the Plan approval HumanDecision outside `plan_proposal`.
- [ ] AC-11-027: Numbered No records a standalone decline HumanDecision or project-level decision-log entry
- [ ] AC-11-028: creates no Plan.
- [ ] AC-11-029: Discuss records no mutation and later re-presents the same gate for the current or revised proposal.
- [ ] AC-11-030: After Plan approval, batch proceed or one-at-a-time child creation creates child Work Packets from the approved Plan.
- [ ] AC-11-031: One-at-a-time child creation uses `plan.child.create`.
- [ ] AC-11-032: The action must reference the approved Plan id, the approved Plan proposal hash/snapshot revision, a `plan_slice_id` from the approved Plan, and the proposed child payload.
- [ ] AC-11-033: Spec Guard must validate that the child payload corresponds to the approved Plan slice before creating the Work Packet.
- [ ] AC-11-034: `proposed_child_id` must equal `plan_slice_id`
- [ ] AC-11-035: alternate child id mappings are not supported by this specification.
- [ ] AC-11-036: Child payload correspondence requires exact match between `plan_slice_id` and an approved Plan slice `proposed_id`, requires `proposed_work_payload.id` to equal `plan_slice_id`,
- [ ] AC-11-037: requires exact match for title, goal, classification, docs policy, allowed globs, source-derived flag, source evidence summary, and full AcceptanceCriterion payloads recorded in the approved Plan proposal.
- [ ] AC-11-038: Desired outcomes, in-scope, out-of-scope, users/actors, edge cases, and open questions in ProposedWorkPacketPayload must exactly match the corresponding approved Plan slice arrays.
- [ ] AC-11-039: Platform and architecture may be copied from approved Plan product context only when that context contains prior platform/architecture HumanDecision ids
- [ ] AC-11-040: otherwise they must remain unset until the child records its own platform/architecture decisions.
- [ ] AC-11-041: `runtime_baseline_ref` may be null at create-only child creation time
- [ ] AC-11-042: any non-null runtime baseline ref must reference an accepted baseline, and packet approval or authorization readiness requires an accepted runtime baseline ref.
- [ ] AC-11-043: The created WorkPacket must durably store `parent_plan_id` and `plan_slice_id`.
- [ ] AC-11-044: Implementations must not create a child with broader scope, different classification, different docs policy, or additional ACs through `plan.child.create`
- [ ] AC-11-045: such changes require Plan amendment or a separate Work Packet approval path.
- [ ] AC-11-046: The backend verifier must not judge whether the Plan proposal is good, complete, or optimal.
- [ ] AC-11-047: Before a batch proceed decision, `plan.batch_snapshot.create` must receive a `proposed_children_payload` that expands approved Plan slices into proposed child Work Packet payloads.
- [ ] AC-11-048: Each proposed child entry must include `plan_slice_id`, `proposed_child_id`, `expected_created_work_packet_revision`, canonical `proposed_work_payload`, and caller-proposed readiness diagnostics.
- [ ] AC-11-049: `plan.batch_snapshot.create` must recompute readiness and eligibility through the deterministic kernel, replace caller-proposed readiness fields with kernel-computed values in the persisted BatchReviewSnapshot,
- [ ] AC-11-050: reject only when the proposed child payload itself is invalid
- [ ] AC-11-051: `plan_slice_id` must match an approved Plan slice `proposed_id`, `proposed_child_id` must equal `plan_slice_id`, `proposed_work_payload.id` must equal `proposed_child_id`, and `proposed_work_payload.title` must match the approved Plan slice title.
- [ ] AC-11-052: Batch child correspondence must enforce the same approved Plan slice constraints as `plan.child.create`: title, goal, classification, docs policy, allowed globs, source-derived flag, source evidence summary, and full AcceptanceCriterion payloads must match the approved Plan slice.
- [ ] AC-11-053: `plan.batch_snapshot.create` must reject a proposed child that broadens scope, changes classification, changes docs policy, changes source-derived status, changes source evidence summary, adds ACs, or otherwise fails correspondence with the approved Plan slice.
- [ ] AC-11-054: `plan.batch_snapshot.create` derives `source_artifact_refs` deterministically as a canonical set.
- [ ] AC-11-055: The set is the union of: the approved Plan artifact ref, top-level `proposed_children_payload.source_artifact_refs`, each proposed child's provenance refs, and each proposed source-derived AC SourceEvidence `source_artifact_refs`.
- [ ] AC-11-056: Duplicate refs are removed by exact tuple identity `(artifact_type, id, revision)`.
- [ ] AC-11-057: `plan.batch_snapshot.create` must apply Appendix A canonical SourceArtifactRef ordering when deriving source artifact refs.
- [ ] AC-11-058: Snapshot hashing must use this canonical array.
- [ ] AC-11-059: At snapshot creation and decision validation, every listed ref must resolve and any supplied content hash must match.
- [ ] AC-11-060: Later approval invalidation treats only refs that also appear in approved source-derived AC SourceEvidence as governed source dependencies.
- [ ] AC-11-061: Top-level and child-level provenance-only refs becoming unavailable after approval create replay diagnostics but do not stale AC approval, Work Packet approval, Plan approval, or batch decisions by themselves.
- [ ] AC-11-062: A proposed child has a governed source dependency only when a source-derived AC SourceEvidence record includes that SourceArtifactRef.
- [ ] AC-11-063: Child-level and top-level source refs in ProposedChildrenPayload are provenance-only unless also present on SourceEvidence for a source-derived AC.
- [ ] AC-11-064: Spec Guard must not infer dependencies from free-form descriptions, paths, filenames, media types, extensions, or prose.
- [ ] AC-11-065: Source-derived AC SourceEvidence must declare at least one SourceArtifactRef.
- [ ] AC-11-066: If source-derived AC evidence omits required refs, declared refs cannot be canonicalized, or declared refs do not resolve to immutable SourceArtifact revisions or other known immutable top-level artifact revisions, the action must reject the batch snapshot request with diagnostics.
- [ ] AC-11-067: Spec Guard must not restrict source-derived evidence to a finite list of file types, extensions, media types, or artifact kinds.
- [ ] AC-11-068: it does not validate whether the kind or file type is acceptable source material.
- [ ] AC-11-069: `plan.batch_snapshot.create` persists a batch review snapshot as an audit-only mutation.
- [ ] AC-11-070: It does not create children, approve ACs, approve Work Packets, authorize implementation, change Plan intent, or increment the governed Plan revision.
- [ ] AC-11-071: Its `snapshot_hash` is computed over `BatchReviewSnapshotPayload`, which excludes the enclosing record's `id`, `snapshot_hash`, `snapshot_revision`, `audit_revision`, `created_at`, and nested child `ReviewSnapshot` records
- [ ] AC-11-072: this prevents circular or volatile hashing.
- [ ] AC-11-073: The `plan.batch_proceed` shared action records the human's batch proceed selection after Plan approval for selected options 1 through 4.
- [ ] AC-11-074: For option 5 Discuss, it records no HumanDecision, creates no BatchProceedRecord, and performs no mutation.
- [ ] AC-11-075: Before creating children, approvals, authorizations, or baselines for options 1 through 4, the action must construct
- [ ] AC-11-076: validate a canonical `BatchProceedSelectionPayload` from the selected option and persisted batch snapshot.
- [ ] AC-11-077: If this preflight validation fails, the action must perform no child mutation
- [ ] AC-11-078: record no HumanDecision or BatchProceedRecord.
- [ ] AC-11-079: The human decision approves only this pre-decision selection payload.
- [ ] AC-11-080: The action must then construct a separate canonical `BatchProceedResult` containing created child ids, approval results, authorization results, packet change baseline refs, and diagnostics for every proposed child, including failed or skipped child operations.
- [ ] AC-11-081: It must store both records in a Plan `BatchProceedRecord` together with their hashes/revisions and the human decision, even when some child operations failed after earlier child mutations succeeded.
- [ ] AC-11-082: It must not roll back already committed successful child mutations unless the implementation provides a real transaction that rolls back all child and Plan writes.
- [ ] AC-11-083: `selection_revision` must be `batch-selection:<batch_snapshot_revision>:<selection_hash>`.
- [ ] AC-11-084: `result_revision` must be `batch-result:<batch_snapshot_revision>:<result_hash>`.
- [ ] AC-11-085: The `plan_batch_proceed` approved fields are JSON pointers into the stored `BatchProceedSelectionPayload`, not the post-action result.
- [ ] AC-11-086: The `plan_batch_proceed` HumanDecision must populate `review_snapshot_hash` and `review_snapshot_revision` with the batch snapshot hash and revision, must populate `parent_batch_snapshot_hash` and `parent_batch_snapshot_revision` with the same values, must copy `source_artifact_refs` from the BatchReviewSnapshot, must set `approved_payload_ref` to the BatchProceedRecord selection hash and revision,
- [ ] AC-11-087: must leave `approved_payload`, `approved_payload_hash`, and `approved_payload_revision` null unless an implementation intentionally duplicates the selection payload in addition to keeping the BatchProceedRecord as canonical.
- [ ] AC-11-088: Create all suggested child slices, then stop for review
- [ ] AC-11-089: Create all suggested child slices and approve eligible displayed non-source-derived child ACs and Work Packets
- [ ] AC-11-090: Create all suggested child slices, approve eligible displayed non-source-derived child ACs and Work Packets, and authorize eligible child Work Packets
- [ ] AC-11-091: Option 1 records a BatchProceedRecord and HumanDecision for the selected one-at-a-time path, creates no children, records no child AC approval, records no Work Packet approval, records no authorization,
- [ ] AC-11-092: returns `plan.child.create` as the next action.
- [ ] AC-11-093: Its BatchProceedSelectionPayload must include each proposed child with `selected_for_creation: false`, `requested_ac_batch_approval: false`, `requested_packet_batch_approval: false`, and `requested_batch_authorization: false`.
- [ ] AC-11-094: Its BatchProceedResult must include one row for each proposed child with `created_work_packet_id: null`, approval and authorization booleans false, `packet_change_baseline_ref: null`, and diagnostics empty or informational.
- [ ] AC-11-095: Option 2 creates children only.
- [ ] AC-11-096: Its BatchProceedSelectionPayload must include every proposed child with `selected_for_creation: true`, `requested_ac_batch_approval: false`, `requested_packet_batch_approval: false`, and `requested_batch_authorization: false`.
- [ ] AC-11-097: Created children start `pending_ac_approval` when ACs exist and no batch approvals are recorded, including all source-derived children.
- [ ] AC-11-098: Option 3 creates all suggested child Work Packets and approves only children packet-approval-ready under batch rules.
- [ ] AC-11-099: Its BatchProceedSelectionPayload must include every proposed child with `selected_for_creation: true`
- [ ] AC-11-100: for each child, `requested_ac_batch_approval` and `requested_packet_batch_approval` are true only when `batch_approval_eligible` and readiness diagnostics are clean, and false otherwise
- [ ] AC-11-101: Children with batch AC and packet approval recorded start `approved`
- [ ] AC-11-102: created children without both approvals start `pending_ac_approval`.
- [ ] AC-11-103: Option 4 creates all suggested child Work Packets, approves children packet-approval-ready under batch rules, and authorizes only children batch-authorization-ready.
- [ ] AC-11-104: `requested_batch_authorization` is true only when `batch_authorization_eligible` and readiness diagnostics are clean, and false otherwise.
- [ ] AC-11-105: Children with authorization recorded start `authorized`
- [ ] AC-11-106: children with approvals but no authorization start `approved`
- [ ] AC-11-107: other created children start `pending_ac_approval`.
- [ ] AC-11-108: In BatchProceedSelectionPayload, child `ac_snapshot_hash`/`ac_snapshot_revision` are populated only when `requested_ac_batch_approval` is true
- [ ] AC-11-109: `packet_snapshot_hash`/`packet_snapshot_revision` are populated only when `requested_packet_batch_approval` is true
- [ ] AC-11-110: and `authorization_snapshot_hash`/`authorization_snapshot_revision` are populated only when `requested_batch_authorization` is true.
- [ ] AC-11-111: For every child authorized by option 4, Spec Guard must capture
- [ ] AC-11-112: store that child's PacketChangeBaseline atomically with the child authorization decision.
- [ ] AC-11-113: If PacketChangeBaseline capture is blocked for a child, that child must not be authorized.
- [ ] AC-11-114: The batch result may partially succeed for other eligible children, but it must report per-child authorization failure diagnostics and next actions.
- [ ] AC-11-115: Runtime baseline must be accepted before options 3 or 4 can be selected as mutating options.
- [ ] AC-11-116: Batch proceed prompt numbering is fixed: options 1 through 5 always keep their numbers.
- [ ] AC-11-117: If the baseline is not accepted, options 3 and 4 must be shown as unavailable diagnostics under their fixed numbers
- [ ] AC-11-118: selecting an unavailable option records no HumanDecision
- [ ] AC-11-119: returns blocking diagnostics.
- [ ] AC-11-120: Batch review must display each affected child packet's ACs, source-derived AC evidence, scope, classification, docs policy, allowed globs, platform, architecture, and diagnostics from the persisted batch review snapshot.
- [ ] AC-11-121: Batch approval and batch authorization must exclude any child containing source-derived ACs.
- [ ] AC-11-122: Batch must not choose platform, architecture, runtime baseline acceptance, Plan-vs-single, or Plan approval.
- [ ] AC-11-123: Batch must not skip deterministic gates or required backend verification.
- [ ] AC-11-124: Batch approvals and authorizations must bind per child according to section 4.7.
- [ ] AC-11-125: Ordered requirement is supported/enforced: Single packet is sufficient
- [ ] AC-11-126: Ordered requirement is supported/enforced: Create a Plan
- [ ] AC-11-127: Ordered requirement is supported/enforced: Discuss
- [ ] AC-11-128: Ordered requirement is supported/enforced: Yes
- [ ] AC-11-129: Ordered requirement is supported/enforced: No
- [ ] AC-11-130: Ordered requirement is supported/enforced: Work through one child slice at a time
- [ ] AC-11-131: Ordered requirement is supported/enforced: Create all suggested child slices, then stop for review
- [ ] AC-11-132: Ordered requirement is supported/enforced: Create all suggested child slices and approve eligible displayed non-source-derived child ACs and Work Packets
- [ ] AC-11-133: Ordered requirement is supported/enforced: Create all suggested child slices, approve eligible displayed non-source-derived child ACs and Work Packets, and authorize eligible child Work Packets
- [ ] AC-11-134: Enumerated item is supported/enforced: Option 1 records a BatchProceedRecord and HumanDecision for the selected one-at-a-time path, creates no children, records no child AC approval, records no Work Packet approval, records no authorization, and returns `plan.child.create` as the next action. Its BatchProceedSelectionPayload must include each proposed child with `selected_for_creation: false`, `requested_ac_batch_approval: false`, `requested_packet_batch_approval: false`, and `requested_batch_authorization: false`. Its BatchProceedResult must include one row for each proposed child with `created_work_packet_id: null`, approval and authorization booleans false, `packet_change_baseline_ref: null`, and diagnostics empty or informational.
- [ ] AC-11-135: Enumerated item is supported/enforced: Option 2 creates children only. Its BatchProceedSelectionPayload must include every proposed child with `selected_for_creation: true`, `requested_ac_batch_approval: false`, `requested_packet_batch_approval: false`, and `requested_batch_authorization: false`. Created children start `pending_ac_approval` when ACs exist and no batch approvals are recorded, including all source-derived children.
- [ ] AC-11-136: Enumerated item is supported/enforced: Option 3 creates all suggested child Work Packets and approves only children packet-approval-ready under batch rules. Its BatchProceedSelectionPayload must include every proposed child with `selected_for_creation: true`; for each child, `requested_ac_batch_approval` and `requested_packet_batch_approval` are true only when `batch_approval_eligible` and readiness diagnostics are clean, and false otherwise; `requested_batch_authorization` is always false. Children with batch AC and packet approval recorded start `approved`; created children without both approvals start `pending_ac_approval`.
- [ ] AC-11-137: Enumerated item is supported/enforced: Option 4 creates all suggested child Work Packets, approves children packet-approval-ready under batch rules, and authorizes only children batch-authorization-ready. Its BatchProceedSelectionPayload must include every proposed child with `selected_for_creation: true`; for each child, `requested_ac_batch_approval` and `requested_packet_batch_approval` are true when `batch_approval_eligible` and readiness diagnostics are clean, and false otherwise; `requested_batch_authorization` is true only when `batch_authorization_eligible` and readiness diagnostics are clean, and false otherwise. Children with authorization recorded start `authorized`; children with approvals but no authorization start `approved`; other created children start `pending_ac_approval`.
- [ ] AC-11-138: Enumerated item is supported/enforced: In BatchProceedSelectionPayload, child `ac_snapshot_hash`/`ac_snapshot_revision` are populated only when `requested_ac_batch_approval` is true; `packet_snapshot_hash`/`packet_snapshot_revision` are populated only when `requested_packet_batch_approval` is true; and `authorization_snapshot_hash`/`authorization_snapshot_revision` are populated only when `requested_batch_authorization` is true. All unrequested, ineligible, unavailable, or option-1/option-2 child snapshot fields are null.
- [ ] AC-11-139: Enumerated item is supported/enforced: For every child authorized by option 4, Spec Guard must capture and store that child's PacketChangeBaseline atomically with the child authorization decision.
- [ ] AC-11-140: Enumerated item is supported/enforced: If PacketChangeBaseline capture is blocked for a child, that child must not be authorized. The batch result may partially succeed for other eligible children, but it must report per-child authorization failure diagnostics and next actions.
- [ ] AC-11-141: Enumerated item is supported/enforced: Option 5 mutates nothing.
- [ ] AC-11-142: Enumerated item is supported/enforced: Runtime baseline must be accepted before options 3 or 4 can be selected as mutating options. Batch proceed prompt numbering is fixed: options 1 through 5 always keep their numbers. If the baseline is not accepted, options 3 and 4 must be shown as unavailable diagnostics under their fixed numbers; selecting an unavailable option records no HumanDecision and returns blocking diagnostics.
- [ ] AC-11-143: Enumerated item is supported/enforced: Batch review must display each affected child packet's ACs, source-derived AC evidence, scope, classification, docs policy, allowed globs, platform, architecture, and diagnostics from the persisted batch review snapshot.
- [ ] AC-11-144: Enumerated item is supported/enforced: Batch approval and batch authorization must exclude any child containing source-derived ACs.
- [ ] AC-11-145: Enumerated item is supported/enforced: Batch must not choose platform, architecture, runtime baseline acceptance, Plan-vs-single, or Plan approval.
- [ ] AC-11-146: Enumerated item is supported/enforced: Batch must not skip deterministic gates or required backend verification.
- [ ] AC-11-147: Enumerated item is supported/enforced: Batch approvals and authorizations must bind per child according to section 4.7.
