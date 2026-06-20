# Spec Guard Agentic Governance Requirements

Status: Draft implementation specification, version 66-v4  
Audience: implementation agents, maintainers, test authors  
Purpose: define a complete, testable governance system for agent-driven software development.

---

<a id="us-00-source"></a>
## 0. Implementation Discipline

> Derived user story: [US-00: Implementation discipline](user-stories/00-implementation-discipline.md)

Implementation must be test-first.

For each required behavior:

1. Write or update tests first.
2. Run tests and observe the expected failure.
3. Implement the smallest production change that satisfies the tests.
4. Re-run targeted tests.
5. Re-run full validation before packaging or release.

If this document is ambiguous in a way that prevents implementation, stop and ask. Do not invent hidden requirements.

This document must be sufficient for an implementation agent to build Spec Guard without relying on undocumented behavior.

---

<a id="us-01-source"></a>
## 1. Objective

> Derived user story: [US-01: Governance objective and critical truth](user-stories/01-governance-objective.md)

Spec Guard governs agent-driven software development by ensuring that:

- human intent is explicitly captured,
- frontend-agent proposals remain proposals until accepted through the proper gate,
- human-approved content is canonical intent,
- broad work is split into traceable bounded packets,
- implementation starts only after approval, authorization, and pre-implementation validation,
- required docs, tests, and failure evidence precede implementation source changes,
- source/mockup/design-derived ACs are visible with source evidence before approval,
- runtime evidence and final claims are evidence-backed,
- CLI, MCP, Pi, viewer, and generated agent-harness integrations expose the same governed workflow.

Critical truth must come from:

- explicit human decisions,
- deterministic observations,
- backend verification of required semantic frontend-agent claims,
- auditable artifacts.

Frontend-agent claims alone are never critical truth.

---

<a id="us-02-source"></a>
## 2. Authority Model

> Derived user story: [US-02: Authority model](user-stories/02-authority-model.md)

Every governed question must route to exactly one qualified authority. Mixed questions must be split.

| Question type | Authority |
|---|---|
| Product intent, platform, architecture, AC approval, Work Packet approval, implementation authorization, runtime baseline acceptance, Plan-vs-single decision, Plan approval | Human |
| Ordinary drafting before approval | Frontend agent, later reviewed through human gates |
| Files, paths, commands, timestamps, diffs, schemas, lifecycle, hashes, config, recorded decisions | Deterministic kernel |
| Required semantic checks of frontend-agent claims that do not mutate or judge human intent | Backend verifier |

### 2.1 Human authority

The human is the sole authority for:

- product/platform type,
- architecture choice,
- desired product behavior,
- acceptance criteria approval,
- Work Packet approval,
- implementation authorization,
- runtime baseline acceptance,
- Plan-vs-single-packet choice,
- Plan approval,
- source/mockup/design interpretation as represented in approved ACs.

Once approved, human intent is canonical until changed through a recorded human decision. Neither the frontend agent nor backend verifier may judge whether approved intent is correct, complete, optimal, advisable, or high quality.

### 2.2 Frontend-agent authority

The frontend agent may draft or propose:

- goals,
- desired outcomes,
- in-scope and out-of-scope lists,
- users/actors,
- edge cases,
- open questions,
- acceptance criteria,
- platform options,
- architecture options,
- source-derived ACs with source/evidence,
- Plan slices,
- implementation summaries,
- review summaries,
- final response drafts.

These are proposals or claims until accepted by the appropriate human gate or validated as evidence-backed claims.

### 2.3 Deterministic kernel authority

The deterministic kernel owns:

- action registry,
- top-level artifact storage,
- embedded record storage inside artifacts,
- schema validation,
- lifecycle transitions,
- human gate recording,
- runtime baseline validation,
- packet change baseline capture,
- changed-file computation,
- path and glob validation,
- command execution records,
- docs/test/failure-first ordering checks,
- review snapshot hash computation,
- approval invalidation,
- verifier response schema validation,
- CLI/MCP parity,
- viewer data,
- migration.

Observable facts must be checked deterministically.

### 2.4 Backend verifier authority

The backend verifier checks required semantic frontend-agent claims listed in section 13. It must not:

- create or alter product intent,
- approve or reject work,
- authorize implementation,
- choose platform or architecture,
- judge human-approved ACs, scope, platform, architecture, docs requirement, Plan slices, or source interpretation.

A verifier response that attempts to judge human-approved intent is invalid and cannot satisfy a gate.

---

<a id="us-03-source"></a>
## 3. Choice, Gate, and Prompt Semantics

> Derived user story: [US-03: Choice, gate, and prompt semantics](user-stories/03-choice-gate-prompt-semantics.md)

All governed choices shown to the human must be numbered. Governed decision, approval, authorization, acceptance, and final intent state mutates only from a numbered human selection. Draft artifacts, audit records, command results, evidence records, configuration, and deterministic validation records may mutate through their registered actions without being human decisions unless this specification explicitly requires a human gate.

Prompt proposal actions may persist pending prompt/audit records as audit-only records, but they must not record a governed decision or mutate decision state before the human selects a number. Any structured data needed to later record a decision must be included in the prompt record, not reconstructed from frontend-agent prose.

Discuss is always non-mutating.

### 3.1 Non-binary semantic choices

Non-binary semantic choices must include:

- relevant numbered options,
- `Something else`,
- `Discuss`,
- custom prose support.

Non-binary semantic choices include:

- product/platform type,
- architecture.

If the human chooses Something else or discussion produces a custom decision, custom prose alone is not final. The frontend agent must re-present it as a numbered confirmation:

1. Use `<decision>` as the proposed `<choice>`
2. Do not use this decision
3. Discuss

Only option 1 records the decision. For custom confirmation prompts, option 2 records no HumanDecision and leaves the prior choice unset; if the workflow needs a block or decline, it must use the relevant binary gate. Option 3 records no mutation.

Spec Guard validates prompt shape, not semantic clarity of free-form human prose. If the response is unclear, the frontend agent continues discussion until coherent, then re-presents the coherent choice as numbered confirmation.

### 3.2 Binary gates

Binary gates tie directly to Spec Guard state and must never become non-binary prompts.

Binary gates must be:

1. Yes
2. No
3. Discuss

If the human selects Discuss, the frontend agent may discuss, but later resolution must re-present the same Yes/No/Discuss gate. Discussion-derived text must not replace Yes and must not become a custom gate option.

Only numbered Yes mutates the gated state. Numbered No records decline or blocks as specified by the gate and records a HumanDecision with `approved_fields: []` unless the action is specified as audit-only. Discuss records no governed mutation and must not create a HumanDecision; implementations may record audit-only prompt/answer records for Discuss.

Binary gates include:

- runtime baseline acceptance,
- AC approval,
- Work Packet approval,
- implementation authorization,
- Plan approval.

### 3.3 Fixed binary decisions

Fixed binary decisions have two domain outcomes plus Discuss:

1. First domain outcome
2. Second domain outcome
3. Discuss

They must not include Something else or custom prose support. Selecting option 1 or option 2 records a HumanDecision for the fixed decision. Discuss mutates nothing, creates no HumanDecision, and later re-presents the same fixed decision.

Fixed binary decisions include:

- Plan-vs-single-packet choice.

---

<a id="us-04-source"></a>
## 4. Decision Binding and Review Snapshots

> Derived user story: [US-04: Decision binding and review snapshots](user-stories/04-decision-binding-review-snapshots.md)

This section is normative for every human decision that accepts, approves, authorizes, or records governed intent.

### 4.1 Review snapshot

A review snapshot is the exact structured content shown to the human for a decision.

A review snapshot must:

- include all fields the human is deciding on,
- exclude volatile fields not part of the decision, such as transient diagnostics timestamps and command output buffers,
- include enough rendered context for the human-readable viewer and agent session to match the same decision surface,
- have a deterministic hash and revision.

A snapshot producer must hash the named snapshot payload schema, not the physical artifact file. Top-level common fields, audit logs, decision history, evidence, backend verifications, command outputs, and diagnostics are excluded unless the named payload schema includes them.

Canonical serialization rules:

1. Recursively sort object keys by Unicode code point order over key strings.
2. Preserve array order, except arrays explicitly defined as canonical sets.
3. Use UTF-8 JSON without insignificant whitespace.
4. Encode absent optional fields as absent, not null, unless null is semantically meaningful.
5. Timestamps in canonical payloads must be UTC RFC 3339 strings with millisecond precision and `Z` suffix.
6. Numbers in canonical payloads must be integers unless a schema explicitly permits another numeric form.
7. Hash canonical bytes with SHA-256 and encode the digest as lowercase hexadecimal without a prefix.

### 4.2 Snapshot categories and revision semantics

Spec Guard supports three snapshot categories.

#### Ephemeral review snapshot

An ephemeral review snapshot is produced by a non-mutating review action and is not stored as an artifact.

Its `snapshot_revision` is a deterministic string, not an integer. The exact format is:

`ephemeral:<source_refs_hash>:<payload_hash>`

where `source_refs_hash` is the SHA-256 hash of the canonical `source_artifact_refs` array, and `payload_hash` is the SHA-256 hash of the canonical snapshot payload. Direct-payload snapshots with no source artifact may use an empty `source_artifact_refs` array; in that case `source_refs_hash` is the hash of an empty canonical array.

Staleness is detected by comparing the submitted snapshot hash, submitted source artifact references, resolvability of referenced immutable revisions, and submitted decision payload. Review-bound decision actions using ephemeral snapshots must submit the `source_artifact_refs` returned by the snapshot producer. A newer SourceArtifact revision does not stale a decision bound to an older immutable revision; staleness occurs when the referenced revision no longer resolves, its content hash differs, or the current governed artifact revision referenced by the snapshot producer no longer matches.

For a mutating approval action, current artifact revision staleness is checked immediately before applying that action's mutation. The revision increment caused by recording the approving decision, accepted state, authorization, or lifecycle event does not make the just-recorded decision stale. If the action returns a post-mutation reference, that reference names the post-mutation revision explicitly, while the review snapshot remains bound to the pre-mutation payload revision it reviewed.

#### Persisted review snapshot

A persisted review snapshot is stored for audit/replay. Persisting a review snapshot is an audit mutation only. It must not approve, reject, authorize, create product work, change intent, or advance lifecycle state.

Its `snapshot_revision` is a deterministic string with format:

`persisted:<audit_revision>`

where `audit_revision` is a monotonic audit sequence scoped to the owning artifact or standalone audit log named by the persisted snapshot record. Audit revisions are separate from governed top-level artifact revisions and must not affect approval staleness.

#### Batch review snapshot

A batch review snapshot is a persisted review snapshot required for Plan batch proceed. It contains canonical proposed child payloads and child-specific review hashes before child Work Packet artifacts are created. Its `snapshot_revision` uses the same `persisted:<audit_revision>` format, where `audit_revision` is the batch snapshot audit sequence and not the governed Plan revision.

### 4.3 Review snapshot producers

Every review-bound gate must have a snapshot producer before the human decision is recorded.

Required snapshot producers:

| Gate | Snapshot producer | Snapshot category | Decision action |
|---|---|---|---|
| Runtime baseline acceptance | `baseline.review` | ephemeral | `baseline.accept` |
| AC approval | `work.ac.review` | ephemeral | `work.ac.approve` |
| Work Packet approval | `work.packet.review` | ephemeral | `work.approve` |
| Implementation authorization | `work.authorization.review` | ephemeral | `work.authorize` |
| Plan approval | `plan.propose` | ephemeral | `plan.approve` |
| Plan batch proceed | `plan.batch_snapshot.create` | persisted batch audit record | `plan.batch_proceed` |

The required pattern is:

1. A snapshot producer renders the exact decision payload and returns snapshot hash/revision.
2. The frontend agent presents that exact payload to the human.
3. The decision action submits selected number, raw response, exact prompt, human confirmation, and the relevant snapshot hash/revision.
4. Spec Guard validates that the submitted payload or current artifact content hashes to the supplied snapshot hash before mutating governed state.
5. Stale or mismatched snapshot hashes block governed mutation.

Snapshot producers may return compact summaries and full payloads. Approval actions must not depend on frontend-agent summaries when validating snapshot hashes.

Snapshot producer payloads and source refs are deterministic:

| Producer | Snapshot payload schema | Source artifact refs |
|---|---|---|
| `baseline.review` | `BaselineReviewSnapshotPayload`: `/stack`, `/commands`, `/configuration`, `/dependency_modes`, `/diff_policy`, `/validation` | canonical ref `{ "artifact_type": "runtime_baseline", "id": null, "revision": baseline.revision }` |
| `work.ac.review` | `AcReviewSnapshotPayload`: work id, work revision when present, reviewed AC payload | WorkPacket ref when a WorkPacket exists, plus canonical SourceArtifactRefs declared by source-derived AC SourceEvidence in the reviewed payload |
| `work.packet.review` | `WorkPacketReviewSnapshotPayload`: work id/revision, title, parent_plan_id, plan_slice_id, intent, acceptance_criteria, docs policy/none_required_reason/not_applicable_reason, allowed_globs, platform, architecture, classification, runtime_baseline_ref | WorkPacket ref, referenced runtime baseline artifact ref, and canonical SourceArtifactRefs declared by source-derived AC SourceEvidence |
| `work.authorization.review` | `AuthorizationReviewSnapshotPayload` | WorkPacket ref, referenced runtime baseline artifact ref, and SourceArtifactRefs already present in the approved packet review surface |
| `plan.propose` | `PlanProposalPayload` | Source refs declared in the PlanProposalPayload, plus source WorkPacket ref when `PlanProposalPayload.source_work_id` is non-null |
| `plan.batch_snapshot.create` | `BatchReviewSnapshotPayload` | refs derived by section 11.4 |

Decision ids/hashes embedded in payloads are not SourceArtifactRefs unless the decision is stored as a standalone top-level artifact. Built-in artifact refs must use the artifact's stored canonical `artifact_type`, `id`, and `revision`. SourceArtifactRefs in these arrays are canonical sets using the ordering rules in Appendix A.

Non-batch snapshot producers are ephemeral-only. If an implementation wants to retain one for audit/replay, it must persist it through a separate audit-only snapshot persistence action that does not change governed state. Persisting a non-batch snapshot must not be required for normal gate operation.

Non-batch persisted review snapshots live in a ReviewSnapshot audit log. The log may be embedded in the owning artifact or stored as standalone ReviewSnapshot records, but every record must have an `audit_revision` scoped to that log and must be resolvable later by producer action id, snapshot hash, and snapshot revision.

Ephemeral snapshot payloads may still be copied into immutable decision records when the approved-field root is not otherwise durable. This copy is decision payload storage, not a persisted `ReviewSnapshot` artifact, and it exists so audit and invalidation can compare later state against the exact approved payload. When stored in a HumanDecision, `approved_payload_revision` must be `payload:<approved_payload_hash>` and `reviewed_payload_revision` must be `payload:<reviewed_payload_hash>`.

### 4.4 Approved fields

Every approval/acceptance/authorization decision record must include `approved_fields`.

For standard gates, Spec Guard derives `approved_fields` deterministically from `decision_type`; frontend agents do not supply them. Custom decision actions must either use a registered decision type with a known field set or provide an explicit approved field set that deterministic validation accepts.

Standard approved field sets are canonical JSON pointer sets relative to the listed root payload:

| Decision type | Approved-field root payload | Approved JSON pointer set |
|---|---|---|
| `runtime_baseline_acceptance` | RuntimeBaseline artifact | `/stack`, `/commands`, `/configuration`, `/dependency_modes`, `/diff_policy`, `/validation` |
| `plan_vs_single` | PlanVsSingleDecisionPayload stored in HumanDecision.approved_payload | `/work_id`, `/selected_option`, `/presented_ac_payload`, `/presented_ac_payload_hash`, `/presented_ac_refs` |
| `platform_choice` | PlatformChoiceDecisionPayload stored in HumanDecision.approved_payload | `/work_id`, `/choice`, `/custom_response` |
| `architecture_choice` | ArchitectureChoiceDecisionPayload stored in HumanDecision.approved_payload | `/work_id`, `/choice`, `/custom_response`, `/option_details` |
| `ac_approval` | WorkPacket artifact | `/acceptance_criteria` |
| `work_packet_approval` | WorkPacket artifact | `/title`, `/parent_plan_id`, `/plan_slice_id`, `/intent`, `/acceptance_criteria`, `/docs/policy`, `/docs/none_required_reason`, `/docs/not_applicable_reason`, `/scope/allowed_globs`, `/platform`, `/architecture`, `/classification`, `/runtime_baseline_ref` |
| `implementation_authorization` | AuthorizationReviewSnapshotPayload stored in HumanDecision.approved_payload | `/id`, `/approved_packet_snapshot_hash`, `/approved_packet_snapshot_revision`, `/allowed_globs`, `/runtime_baseline_ref`, `/change_baseline_capture_plan` |
| `batch_ac_approval` | ProposedWorkPacketPayload stored through the parent BatchReviewSnapshot child payload | `/acceptance_criteria` |
| `batch_work_packet_approval` | ProposedWorkPacketPayload stored through the parent BatchReviewSnapshot child payload | `/title`, `/parent_plan_id`, `/plan_slice_id`, `/intent`, `/acceptance_criteria`, `/docs/policy`, `/docs/none_required_reason`, `/docs/not_applicable_reason`, `/scope/allowed_globs`, `/platform`, `/architecture`, `/classification`, `/runtime_baseline_ref` |
| `batch_child_implementation_authorization` | ProposedAuthorizationReviewSnapshotPayload stored in HumanDecision.approved_payload | `/plan_slice_id`, `/proposed_child_id`, `/expected_created_work_packet_revision`, `/proposed_packet_snapshot_hash`, `/proposed_packet_snapshot_revision`, `/allowed_globs`, `/runtime_baseline_ref`, `/change_baseline_capture_plan` |
| `plan_approval` | PlanProposalPayload | `/title`, `/goal`, `/source_work_id`, `/product_context`, `/summary`, `/slices` |
| `plan_batch_proceed` | BatchProceedSelectionPayload stored in BatchProceedRecord.selection | `/selected_option`, `/batch_snapshot_hash`, `/batch_snapshot_revision`, `/proposed_children_payload_hash`, `/children` |

Approved JSON pointers must be exact canonical paths in the named root payload. Wildcards, prose fragments, nonexistent schema paths, and frontend-only labels are not valid approved-field entries.

When a final approving/selecting decision has an approved-field root payload that is not a durable top-level artifact path, Spec Guard must persist the canonical approved payload, payload hash, and payload revision in an immutable record named by the root payload. For `implementation_authorization`, that record is the authorization HumanDecision. For `plan_batch_proceed`, that record is the Plan's BatchProceedRecord selection payload. Invalidation compares the stored approved payload with the current deterministically reconstructed payload or with the stored batch proceed selection payload as applicable. Decline, block, and Discuss paths do not create approved payloads.

`plan_batch_proceed`, `batch_ac_approval`, and `batch_work_packet_approval` are the only standard decision types whose approved-field root is stored in a sibling record rather than duplicated into the HumanDecision. The batch proceed HumanDecision must record `approved_payload_ref` pointing to the BatchProceedRecord selection hash and revision. Batch child AC and Work Packet approval HumanDecisions must record `approved_payload_ref` pointing to the exact ProposedWorkPacketPayload stored in the BatchReviewSnapshot child payload; approved pointers remain relative to that ProposedWorkPacketPayload root. These decisions must not duplicate full approved payloads unless an implementation also keeps the referenced sibling payload as canonical.

Plan approval approved fields are rooted in the reviewed PlanProposalPayload. The Plan approval HumanDecision is not part of that reviewed payload and must not be nested under `/plan_proposal`.

For Work Packet approval, `/docs/requirements` and `/scope/deviations` are review context unless explicitly added to an approved-field set by a future decision type. Changing them does not by itself invalidate Work Packet approval, but may affect readiness, docs validation, allowed-globs diagnostics, or review completion.

For implementation authorization, `/change_baseline_capture_plan` approves the baseline capture method and metadata shown before authorization. It does not approve the later captured `PacketChangeBaseline` contents, which are recorded atomically with authorization after capture succeeds.

Changing an approved path invalidates that decision and all dependent decisions.

Dependency invalidation rules:

- Changing AC-approved paths invalidates Work Packet approval, implementation authorization, pre-implementation validation, review completion, and final claim validation for that packet.
- Changing Work-Packet-approved paths invalidates implementation authorization, pre-implementation validation, review completion, and final claim validation for that packet.
- Changing runtime baseline accepted paths invalidates packet approvals and authorizations that reference that baseline revision.
- Generic updates must not change Plan-approved paths. If a future registered Plan amendment action changes Plan-approved paths, it invalidates batch snapshots, child creation eligibility, batch approvals, and batch authorizations derived from that Plan and must record a new Plan approval decision before the Plan is treated as approved again.
- Superseding a human decision invalidates downstream decisions that depend on the superseded decision unless the new decision explicitly re-approves the same canonical path set and snapshot content.

Status effects of invalidation:

- Invalidating AC approval moves a packet to `pending_ac_approval` unless archived/deferred.
- Invalidating Work Packet approval moves a packet to `pending_packet_approval` after AC approval remains valid, or `pending_ac_approval` if AC approval is also invalid.
- Invalidating implementation authorization removes implementation-ready state and moves the packet to `approved` when packet approval remains valid.
- Invalidating pre-implementation validation after implementation has started moves the packet to `blocked` with diagnostics requiring human resolution or a new packet.
- Invalidating approval after `review_complete` marks review completion stale and moves the packet to `blocked` with diagnostics requiring renewed approval and review completion.

### 4.5 Human decision record

Every human decision record that records an approving, accepting, authorizing, selecting, declining, or blocking numbered choice must include:

- id,
- decision type,
- prompt id,
- exact prompt text,
- raw response,
- selected number,
- normalized decision,
- approved fields,
- review snapshot hash and revision when review-bound,
- source artifact references returned by the snapshot producer when review-bound,
- approved payload, approved payload hash, and approved payload revision when the decision approves/selects a final numbered option and the approved-field root is not otherwise durable, except for `plan_batch_proceed`,
- approved payload reference when the decision type is `plan_batch_proceed`, pointing to the canonical BatchProceedRecord selection payload,
- reviewed payload, reviewed payload hash, and reviewed payload revision when a declined or blocked review-bound decision retains the rejected surface for audit,
- custom response if any,
- supersedes decision id if applicable,
- superseded by decision id if applicable,
- source interface,
- at timestamp.

Human decision records are append-only and substance-immutable after creation. Spec Guard must not expose actions that patch the substance of a recorded human decision. Corrections or changes must be represented by a new decision that supersedes the prior decision.

The only permitted update to an existing HumanDecision is metadata-only linkage: setting `superseded_by_decision_id` after a later superseding decision is recorded, or archive metadata that hides a decision from default views. Metadata-only linkage must not change prompt text, raw response, selected number, normalized decision, approved fields, approved payload, snapshot fields, or source interface.

No/decline/block decisions must use `approved_fields: []` unless a registered decision type explicitly defines non-approval fields being selected. They do not require `approved_payload`, even when the corresponding Yes/selection decision type would use a non-durable approved-field root. If the reviewed but rejected payload is retained, it must be stored as `reviewed_payload`, not `approved_payload`. Discuss selections must not create HumanDecision records. If Discuss is audited, it must be recorded as a ChoiceAnswer or audit record with no governed decision state mutation.

If a human selects Yes but deterministic validation or an atomic side effect fails before the governed gate can be satisfied, Spec Guard must not record the approving HumanDecision. It may record an audit-only GateAttempt/ChoiceAnswer with the raw response, prompt, selected number, diagnostics, and failed action. The governed state remains at the prior lifecycle/status except for diagnostics and audit records.

### 4.6 Authorization review snapshot

`work.authorization.review` produces the authorization review snapshot. `work.authorize.review_snapshot_hash` refers to this authorization snapshot, not the Work Packet approval snapshot.

The authorization snapshot payload must include:

- Work Packet id,
- current Work Packet revision,
- approved packet snapshot hash and revision,
- authorization-ready diagnostics,
- allowed globs,
- runtime baseline reference,
- packet change baseline capture plan,
- expected file category policy,
- implementation boundary summary.

One authorization snapshot hash is sufficient because the approved packet snapshot hash is embedded in the authorization snapshot payload.

On numbered Yes, `work.authorize` must store the exact canonical AuthorizationReviewSnapshotPayload in the authorization HumanDecision as `approved_payload`, along with `approved_payload_hash` and `approved_payload_revision`. Later authorization staleness and invalidation must recompute the authorization review payload from current durable state and compare the approved JSON pointer paths against this stored payload.

### 4.7 Batch review snapshot

A Plan batch proceed decision must bind to a batch review snapshot.

The batch review snapshot must exist before the human selects a batch proceed option. It contains the proposed child packet approval surfaces even though child Work Packet artifacts may not yet exist.

A batch review snapshot must include:

- Plan id,
- governed Plan revision,
- approved Plan proposal hash and revision,
- source artifact references used to bind the batch decision,
- proposed children payload hash and snapshot revision,
- batch prompt text,
- available batch options,
- for each proposed child:
  - Plan slice id,
  - proposed child id,
  - expected created Work Packet revision,
  - canonical ProposedWorkPacketPayload,
  - full proposed child AC review snapshot payload and rendered summary,
  - full child packet review snapshot payload and rendered summary,
  - full proposed child authorization review snapshot payload and rendered summary when batch-authorization-eligible,
  - whether the child contains source-derived ACs,
  - batch approval eligibility,
  - batch authorization eligibility,
  - ineligibility diagnostics,
  - readiness diagnostics for AC approval, packet approval, and batch authorization,
  - child-specific snapshot hashes and revisions derived from the proposed payload.

Child-specific batch snapshot revisions must use this exact deterministic format:

`batch-child:<batch_audit_revision>:<proposed_child_id>:<producer_action_id>:<payload_hash>`

where `batch_audit_revision` is the persisted batch snapshot audit revision, `proposed_child_id` is the id in the proposed child payload, `producer_action_id` is `work.ac.review`, `work.packet.review`, or `work.authorization.review`, and `payload_hash` is the hash of the child-specific snapshot payload. Proposed child ids used in this revision format must match `^[A-Za-z0-9._-]+$` and must not contain `:`. Spec Guard must reject proposed child ids that cannot be serialized unambiguously in this format. The `proposed_child_id` must equal `plan_slice_id`; alternate child id mappings are not supported by this specification.

When a batch action creates child artifacts and records approvals, each child decision stores:

- parent batch snapshot hash and revision,
- child-specific AC snapshot hash and revision when ACs are batch-approved,
- child-specific packet snapshot hash and revision when packet is batch-approved,
- child-specific proposed authorization snapshot hash and revision when authorization is batch-recorded,
- approved fields derived for that child decision.

Batch proceed options 3 and 4 are explicit exceptions to the ordinary per-packet binary prompt shape, not to the authority model. The single numbered batch prompt is the human gate for each displayed eligible child approval/authorization it requests. For every child approval or authorization recorded by batch proceed, Spec Guard must create a child HumanDecision with `source_interface: "batch"`, `selected_number` equal to the batch option, `prompt_text` equal to the batch prompt, `parent_batch_snapshot_hash` and `parent_batch_snapshot_revision` populated, `review_snapshot_hash` and `review_snapshot_revision` set to that child's AC, packet, or authorization snapshot, and `source_artifact_refs` set to the canonical union of the parent BatchReviewSnapshot `source_artifact_refs` and that child entry's `source_artifact_refs`. These child decisions use decision types `batch_ac_approval`, `batch_work_packet_approval`, and `batch_child_implementation_authorization`; they are not presented as separate Yes/No prompts. Batch child AC and Work Packet approval decisions must set `approved_payload_ref` to the child's canonical ProposedWorkPacketPayload inside the BatchReviewSnapshot using an ApprovedPayloadRef with record type `batch_review_snapshot`, payload pointer `/children/<index>/proposed_work_payload`, and that ProposedWorkPacketPayload hash/revision. Their approved-field pointers are evaluated relative to that ProposedWorkPacketPayload, not relative to AcReviewSnapshotPayload or ProposedWorkPacketReviewSnapshotPayload wrappers.

Batch AC approval and batch Work Packet approval are valid only if the created child's approval-relevant payload exactly matches the `ProposedWorkPacketPayload` projection used to compute the child AC and packet review snapshots, and the created child revision matches the `expected_created_work_packet_revision` recorded for that child in the batch snapshot. Generated, audit, runtime, evidence, lifecycle-history, diagnostic, and timestamp fields are excluded from this equality check unless explicitly included in `ProposedWorkPacketPayload`. If the created child approval-relevant payload or expected revision differs, Spec Guard must create the child without batch approval and report diagnostics.

Batch equality projections:

- AC batch approval compares `ProposedWorkPacketPayload.acceptance_criteria` to the created WorkPacket `/acceptance_criteria`.
- Work Packet batch approval compares `ProposedWorkPacketPayload` fields `title`, `parent_plan_id`, `plan_slice_id`, `classification`, `intent`, `acceptance_criteria`, `docs.policy`, `docs.none_required_reason`, `docs.not_applicable_reason`, `scope.allowed_globs`, `platform`, `architecture`, and `runtime_baseline_ref` to the corresponding created WorkPacket fields.
- Batch authorization compares `ProposedWorkPacketPayload.id`, `parent_plan_id`, `plan_slice_id`, `scope.allowed_globs`, and `runtime_baseline_ref`, plus the proposed packet snapshot hash/revision and authorization review fields, to the created WorkPacket and captured authorization record.

`docs.requirements` and `scope.deviations` are present in `ProposedWorkPacketPayload` for child creation and review context, but they are not part of Work Packet batch approval unless also represented in the approved-field set for that decision type.

A proposed child authorization snapshot is valid only inside a persisted batch review snapshot. It uses `ProposedAuthorizationReviewSnapshotPayload`, not `AuthorizationReviewSnapshotPayload`, because the child Work Packet artifact does not exist yet. It is computed from the proposed child `ProposedWorkPacketPayload`, expected created Work Packet revision, the proposed child packet snapshot hash, accepted runtime baseline reference, allowed globs, batch-authorization-ready diagnostics, and packet change baseline capture plan. The expected created Work Packet revision is `1`. When the child artifact is created by batch proceed, Spec Guard records authorization against the created child only if the created child's authorization projection exactly matches the `ProposedWorkPacketPayload` authorization projection used by the proposed authorization snapshot and the created child revision matches the expected revision. The batch child authorization HumanDecision must use decision type `batch_child_implementation_authorization` and store the exact canonical ProposedAuthorizationReviewSnapshotPayload as `approved_payload`, with its payload hash and revision.

Batch child mutation sequence is normative: create child WorkPacket at revision 1, compare the created child's approval-relevant projections against the batch snapshot payload, record batch AC approval in a later child revision when applicable, record batch Work Packet approval in a later child revision when applicable, then capture PacketChangeBaseline and record authorization in a later child revision when applicable. Child decisions must store the child revision observed at the moment that decision is recorded in `HumanDecision.target_artifact_revision`. The `expected_created_work_packet_revision` check applies only to the newly created child before approval/authorization mutations.

This allows option 4 to create, approve, and authorize eligible children in one action without losing per-child approval binding. The batch action must reject stale batch snapshot hashes.

Source-derived ACs are never batch-approved or batch-authorized. A child containing source-derived ACs may be created by a batch action, but its AC approval, Work Packet approval, and authorization must proceed through the normal per-child gates.

---

<a id="us-05-source"></a>
## 5. Artifact and Record Model

> Derived user story: [US-05: Artifact and record model](user-stories/05-artifact-record-model.md)

Spec Guard distinguishes top-level artifacts from embedded records.

### 5.1 Top-level artifacts

Top-level artifacts are independently stored JSON documents. They must include:

- `artifact_type`,
- `schema_version`,
- `id` except singletons,
- `revision`,
- `created_at`,
- `updated_at`,
- diagnostics where applicable.

Top-level artifacts include:

- config,
- runtime baseline,
- Work Packet,
- Plan,
- SourceArtifact records,
- standalone decision artifacts when used,
- CommandResult records when stored separately,
- verifier configuration when stored separately.

A newly created top-level artifact starts at governed `revision: 1`. A governed mutating write to a top-level artifact increments `revision` and updates governed `updated_at`. Audit-only writes, including persisted review snapshots and prompt audit records, must not increment the governed `revision` or governed `updated_at` used for approval staleness. Audit-only records have their own `created_at`/audit sequencing. If an implementation stores audit records physically inside a top-level artifact file, it must maintain separate audit sequencing and must not make the governed artifact revision stale solely because an audit record was appended.

Every top-level artifact revision has a governed content hash: `sha256_lower_hex(canonical_json(governed_projection))`. The governed projection is the artifact JSON at that revision after removing audit-only appendices, physical-storage metadata, and fields whose schema explicitly says they are excluded from that artifact's hash, but retaining governed timestamps, revision, status, decisions, lifecycle, evidence, and diagnostics unless a named snapshot payload excludes them. Revision storage must persist this hash with the immutable revision record. Non-SourceArtifact SourceArtifactRefs to Spec Guard artifacts resolve by artifact type/id/revision to this governed content hash.

Any artifact revision referenced by SourceArtifactRef, review snapshot source refs, approval records, or staleness checks must be revision-addressable after later writes. Implementations may store full historical snapshots or immutable content-addressed revision records, but they must be able to resolve the exact referenced revision and its hash-relevant canonical content. When audit-only records are physically stored inside an artifact file, the governed artifact content hash/projection must exclude those audit appendices; physical file hashes must not be used as governed revision hashes unless the storage format separates audit data.

### 5.2 Embedded records

Embedded records live inside top-level artifacts unless an implementation explicitly stores them as top-level artifacts too. Embedded records do not need top-level artifact common fields unless persisted independently.

Every HumanDecision must be retained in a durable append-only decision log. The decision log may be embedded in the owning artifact or stored as standalone decision artifacts. Decisions that do not yet have an owning artifact, such as declined Plan approvals that create no Plan, must be stored as standalone decision artifacts or in a project-level decision log. Convenience current-decision slots may reference or copy the active decision, but those slots are not the durability mechanism. Changing an active slot must not delete or overwrite prior decisions in the decision log.

Every CommandResult must be retained in durable storage addressable by `command_result_ref`. CommandResults may be embedded in the related Work Packet, embedded in the runtime baseline for baseline validation commands, or stored as standalone CommandResult records. Evidence records reference CommandResults; they do not own or overwrite them.

Embedded records include:

- HumanDecision,
- EvidenceRecord,
- PacketChangeBaseline,
- BackendVerification,
- BatchReviewSnapshot,
- BatchProceedRecord,
- ReviewSnapshot,
- ChoicePrompt,
- ChoiceAnswer,
- ProductContext,
- CommandResult,
- DocsRequirement,
- AcceptanceCriterion,
- LifecycleEvent,
- Claim,
- VerifierFinding.

Embedded record schemas are defined in Appendix A.

---

<a id="us-06-source"></a>
## 6. Runtime Baseline and Packet Change Baseline

> Derived user story: [US-06: Runtime and packet change baselines](user-stories/06-runtime-and-change-baselines.md)

### 6.1 Runtime baseline

The runtime baseline is a human-accepted runtime/build/test/project-environment baseline. It is not a repository snapshot and is not a diff base.

Purpose:

- make environment readiness explicit,
- prevent fake or placeholder project commands,
- ensure Plan batch acceleration is not blocked by missing environment readiness.

Runtime baseline status enum:

- `draft`,
- `accepted`,
- `blocked`.

The runtime baseline must capture:

- stack,
- commands,
- configuration assumptions,
- dependency modes,
- diff policy,
- validation results,
- acceptance record when accepted,
- blocker record when blocked.

Commands must distinguish, when applicable:

- test,
- build,
- production runtime smoke,
- development runtime.

If a project requires both frontend and backend for development, the development command must be one documented command or orchestrated entry point that starts the required full development runtime, or a concrete not-applicable reason must be recorded.

Baseline acceptance requires:

1. numbered human Yes on the baseline acceptance gate,
2. a runtime baseline review snapshot hash and revision shown to the human,
3. deterministic validation success,
4. required commands or concrete not-applicable reasons,
5. no placeholder, version-only, or Spec Guard self-check command used as project validation.

Deterministic runtime baseline validation requires every non-null configured command in `commands.test`, `commands.build`, `commands.runtime_production`, and `commands.runtime_development` to be a CommandSpec and to have a current RuntimeBaseline `validation.command_results` entry whose `command_spec` is canonically equal, whose purpose matches (`test`, `build`, `runtime_production`, or `runtime_development`), whose `related_runtime_baseline_ref` is null during draft validation, and whose status is `passed`. For multiple matching CommandResults, the current result is the one with the greatest `finished_at` timestamp; ties are broken by lexicographically greatest CommandResult `id`. Older matching results are audit history and do not satisfy or fail current validation. A null command is valid only when the corresponding concrete not-applicable reason field is non-empty. CommandResults with status `failed`, `timed_out`, or `skipped`, placeholder/version-only/self-check command specs, missing command results, command purpose mismatches, stale command specs, or null commands without not-applicable reasons block baseline acceptance.

If deterministic validation fails after human Yes, acceptance is not recorded. The baseline remains draft or blocked with diagnostics.

If the human selects numbered No on the runtime baseline acceptance gate, `baseline.accept` records a `runtime_baseline_acceptance` HumanDecision with `approved_fields: []`, no approved payload, the reviewed snapshot hash, revision, and source refs required by the action contract, and normalized decision `no`. It appends that decision to runtime baseline decision history, sets baseline status to `blocked`, records a Blocker with reason `human_declined_baseline_acceptance`, and does not create a RuntimeBaselineRef. Discuss records no HumanDecision and no status change.

Accepted baseline changes invalidate acceptance and require the same Yes/No/Discuss acceptance gate again. When `baseline.update` changes any accepted approved path, Spec Guard sets RuntimeBaseline status to `draft`, clears the current `acceptance` convenience slot, keeps decision history append-only, records invalidation diagnostics, and marks every RuntimeBaselineRef to the prior accepted revision stale for dependent packet approval/authorization checks.

`RuntimeBaselineRef.revision` is the accepted RuntimeBaseline artifact revision after the acceptance write completes. `baseline.accept` validates the reviewed pre-acceptance payload against the submitted snapshot hash, records the acceptance HumanDecision with that snapshot hash, writes acceptance state, increments the RuntimeBaseline revision, and returns the accepted revision for references. Later staleness checks compare packet refs against this accepted revision and acceptance decision.

Runtime baseline acceptance must not be batch-approved.

### 6.2 Packet change baseline

The packet change baseline is the file/diff baseline for one Work Packet. It is distinct from the runtime baseline.

It is captured at implementation authorization time and is used to:

- compute changed files,
- enforce allowed globs,
- prove implementation source did not change before failure-first evidence,
- support review traceability.

Modes:

- `vcs`: record commit/tree identifier and working tree status,
- `manifest`: record a file manifest when VCS metadata is unavailable.

Packet change baseline mode is selected deterministically from `Config.change_baseline_policy.mode`. `vcs` requires supported VCS metadata and blocks if unavailable. `manifest` always uses manifest capture. `auto` uses `vcs` when supported VCS metadata is present at or above the project root and otherwise uses `manifest`. The minimum required VCS implementation is Git. Other VCS systems are optional, but if supported they must provide equivalent commit/tree, dirty tracked path, and untracked path data. Authorization actions do not accept caller-supplied baseline mode; they use this selected mode.

At authorization, Spec Guard must capture:

- mode,
- captured timestamp,
- WorkPacket governed content hash/revision,
- allowed globs,
- ignored path rules,
- VCS commit/tree and dirty state, or manifest hash and file entries.

The captured WorkPacket artifact hash is the governed content hash of the WorkPacket at the recorded `artifact_revision`, excluding the `change_baseline.artifact_hash` field itself and excluding audit-only appendices. It includes the other PacketChangeBaseline fields committed atomically with authorization.

Authorization commit uses a deterministic prepare/commit algorithm. Spec Guard first constructs the complete post-authorization WorkPacket projection at `next_revision`, including the authorization HumanDecision and PacketChangeBaseline with all fields populated except `artifact_hash`. It computes `artifact_hash` over that projection while excluding only `change_baseline.artifact_hash` and audit-only appendices, writes the computed hash into `change_baseline.artifact_hash`, then commits that exact projection as `artifact_revision = next_revision`. If the final committed projection excluding `artifact_hash` does not hash to the stored value, authorization is invalid and must be rolled back or marked failed before any authorization decision is exposed.

If VCS exists and the working tree has uncommitted `implementation_source`, `runtime_product_configuration`, or `other_unexpected` changes before authorization, authorization must block unless the human resolves the dirty state before authorization. Dirty files categorized as `docs`, `tests`, or `spec_guard_artifact_evidence` may exist before authorization, but their pre-authorization status and content hashes are captured into the packet baseline as pre-existing state and do not count as packet evidence unless re-recorded after authorization. Spec Guard must not silently absorb pre-existing product/source/runtime configuration changes into the packet.

Changed files are computed from packet change baseline to current state:

- VCS mode: diff baseline commit/tree plus working tree and untracked files, adjusted by stored dirty/untracked baseline entries. For Git, capture `HEAD` commit, `HEAD` tree, and repository-relative dirty/untracked entries from porcelain status with NUL separation. Rename entries are normalized to the new repository-relative path with status `renamed`. Deleted entries keep the deleted path. Untracked paths are captured exactly as repository-relative paths. For every allowed pre-authorization dirty/untracked docs/tests/evidence path, capture size and content hash; later changed-file computation treats that captured content hash as the baseline for that path so pre-existing dirty content is not counted as a packet change unless it changes after authorization.
- Manifest mode: compare current manifest to captured manifest.

Changed files must be classified by the canonical `ChangeFileCategory` enum in Appendix C.

---

<a id="us-07-source"></a>
## 7. Work Packet, Plan, and Classification

> Derived user story: [US-07: Work packets, plans, and classification](user-stories/07-work-packet-plan-classification.md)

### 7.1 Work Packet

A Work Packet is bounded implementable work.

Work Packet lifecycle status enum:

- `draft`,
- `pending_ac_approval`,
- `pending_packet_approval`,
- `approved`,
- `authorized`,
- `preimplementation_validated`,
- `implementation_active`,
- `implemented`,
- `review_complete`,
- `blocked`,
- `deferred`,
- `archived`.

A Work Packet must support:

- title,
- classification,
- parent Plan reference and Plan slice reference when applicable,
- intent fields,
- ACs,
- source/evidence metadata for source-derived ACs,
- docs policy,
- allowed file globs,
- platform choice,
- architecture decision references,
- runtime baseline reference,
- packet change baseline,
- lifecycle approvals and authorization,
- evidence,
- backend verification records,
- review traceability,
- final claim audit.

`work.intake` creates a valid draft Work Packet from an IntakeRequest and classification. It must reject parent Plan ids or Plan slice ids; Plan children must be created only through `plan.child.create` or `plan.batch_proceed`. IntakeRequest must include `title` and `goal`. Initial defaults are deterministic: `intent.goal` is `request.goal`; optional intent arrays are empty; `acceptance_criteria` is empty unless supplied; docs policy is `required` for API/contract-surface and `operational_document` classifications and `none_required` otherwise unless supplied with a classification-compatible policy. Classification-compatible supplied policies are: API/contract-surface requires `required`; `operational_document` requires `required`; other classifications allow `required`, `changed`, `none_required`, or `not_applicable`. If supplied docs policy is `not_applicable`, `request.docs_not_applicable_reason` must be non-empty and is copied to `docs.not_applicable_reason`; if supplied docs policy is `none_required`, `docs.none_required_reason` is set from `request.docs_none_required_reason` when supplied or to `classification_default_none_required`; otherwise docs reason fields are null unless later set by a docs action. There is no separate docs-policy strictness ordering. Docs requirements/records are empty; `scope.allowed_globs` and deviations are empty unless supplied; platform/architecture requiredness fields are computed by sections 8.1 and 8.2; `runtime_baseline_ref`, `change_baseline`, decisions, evidence, backend verifications, claims, and review fields are initialized empty/null/false according to Appendix A.

Rules:

- Goal and ACs are required before AC approval.
- AC approval is required before Work Packet approval except for explicit eligible Plan-child batch approval of non-source-derived ACs.
- Work Packet approval is required before implementation authorization.
- Implementation authorization and packet change baseline capture are one atomic governed action; PacketChangeBaseline capture must succeed before the authorization HumanDecision is recorded.
- Pre-implementation validation is required before implementation source changes.
- Approval is invalidated when approved title, parent Plan linkage, Plan slice linkage, intent, ACs, source evidence, approved scope fields such as allowed globs, classification, docs policy, platform, architecture, or runtime baseline reference changes. Scope deviations and docs requirements are review context unless included in an approved-field set.
- Generic update actions must not silently change approved fields. If an update touches approved fields, Spec Guard must either reject it as a protected approved-field update or apply it and deterministically invalidate every dependent approval/authorization with diagnostics and next actions. The action result must list every invalidated decision.
- `plan.update` must reject changes to Plan-approved fields. Because there is no persisted draft Plan state, an approved Plan cannot be moved back to draft by mutation. Changing approved Plan intent requires a new Plan or a registered Plan amendment action with its own review snapshot and Plan approval decision.

Core Work Packet status transitions:

| Action/outcome | Status effect |
|---|---|
| `work.intake` | creates `draft` |
| `work.intent.draft` with at least one AC and required draft intent fields present | `pending_ac_approval` |
| `work.intent.draft` without ACs or with missing required draft intent fields | `draft` |
| `work.ac.approve` Yes | `pending_packet_approval` unless packet approval is already batch-recorded |
| `work.ac.approve` No | `blocked` with decline diagnostics |
| `work.approve` Yes | `approved` |
| `work.approve` No | `blocked` with decline diagnostics |
| `work.authorize` Yes and baseline capture succeeds | `authorized` |
| `work.authorize` No | remains `approved` with authorization-declined diagnostics |
| `work.authorize` failed PacketChangeBaseline capture | remains `approved` with baseline-capture diagnostics and no authorization decision |
| `work.preimplementation.validate` success | `preimplementation_validated` |
| `work.implementation.start` after preimplementation validation | `implementation_active` |
| `work.implementation.complete` after implementation evidence is recorded | `implemented` until `work.review.complete` |
| `work.review.complete` success | `review_complete` |
| archive action | `archived` |

Validation actions may update diagnostics without changing status unless listed above. A failed validation leaves the prior lifecycle status unchanged and records blocking diagnostics and next actions.

### 7.2 Plan

A Plan coordinates broad work and is not implementable.

Plan status enum:

- `approved`,
- `children_created`,
- `in_progress`,
- `complete`,
- `blocked`,
- `archived`.

A Plan must include:

- id,
- title,
- goal,
- approved Plan proposal record,
- child Work Packet references,
- product/platform context,
- status,
- diagnostics.

A Plan never authorizes implementation. Only child Work Packets can be authorized.

Plan proposals are non-mutating until approved. Therefore there is no persisted proposal-only Plan status and no valid persisted draft Plan. A Plan artifact is created only by Plan approval and must have an approval decision when created.

`plan.update` may mutate only non-approved operational metadata: status among non-archival runtime statuses, diagnostics, child_work_ids after validated child creation, and archive metadata through archive actions. It must reject changes to title, goal, product_context, plan_proposal, approval, and any Plan-approved path.

Core Plan status transitions:

| Action/outcome | Status effect |
|---|---|
| `plan.approve` Yes | creates Plan with `approved` |
| `plan.approve` No | creates no Plan; stores standalone decline decision/audit |
| `plan.child.create` creates first child | `children_created`; created child starts `pending_ac_approval` when ACs exist and no batch approvals are recorded, otherwise `draft` |
| `plan.batch_proceed` option 2/3/4 creates one or more children | `children_created` or `in_progress` when any child is authorized/active |
| child Work Packet starts implementation | `in_progress` |
| all non-archived child Work Packets reach `review_complete` | `complete` |
| blocking diagnostics prevent child creation or progress | `blocked` |
| `plan.archive` | `archived` |

### 7.3 Classification enum

Each Work Packet must have exactly one classification:

- `reusable_api`: reusable public API, SDK, library API, or stable callable contract,
- `rest_api`: route, endpoint, service boundary, or network API,
- `reusable_ui`: reusable UI component, UI package, public props/events/slots/styling/accessibility contract, or importable UI surface,
- `one_off_application_ui`: application-specific UI behavior that is not reusable,
- `direct_behavior`: non-API product behavior, scripts, internal behavior, or localized implementation behavior,
- `operational_document`: documentation or operational content as the primary deliverable,
- `bugfix`: correction of reported behavior.

The frontend agent proposes classification. `work.intake` must receive a valid classification; there is no draft/unknown classification value and no implicit default. The deterministic kernel validates enum membership. The human may override classification before AC approval or during Work Packet approval discussion. The backend verifier must not judge classification quality.

### 7.4 API/contract-surface packets

These classifications are always API/contract-surface:

- `reusable_api`,
- `rest_api`,
- `reusable_ui`.

API/contract-surface packets always require human-facing docs. The human cannot override this requirement to `none_required`, `not_applicable`, or `changed`.

Required chain:

approved ACs → human-facing docs → tests → proven failure → implementation source changes.

### 7.5 Non-API packets and docs policy

All other classifications follow the non-API chain unless docs policy requires docs.

`operational_document` packets are documentation-primary packets. Their docs/content policy must be `required`. They may have tests and failure-first evidence marked not applicable only when the approved scope changes documentation/operational content and does not change product behavior, runtime behavior, API behavior, schema, persistence, or shipped application code. If an operational-document packet changes product behavior, it must be reclassified or follow the applicable product validation chain.

Docs policy values:

- `required`: docs must exist and be linked to approved ACs before pre-implementation validation passes,
- `changed`: docs are not required before pre-implementation validation, but docs must be updated and a `docs_updated` claim must pass backend verification before review completion,
- `none_required`: docs are not required and `docs.none_required_reason` records why,
- `not_applicable`: docs do not apply and `docs.not_applicable_reason` records why.

For API/contract-surface packets, docs policy must be `required`.

For `operational_document` packets, docs/content policy must be `required`; `none_required` and `not_applicable` are invalid.

For other non-API packets, the frontend agent proposes docs policy, deterministic validation checks it, and the human may override it before approval.

When docs are required, Spec Guard must validate:

- docs path is inside project,
- docs exist,
- docs link to approved AC IDs,
- required backend verification for docs-to-AC mapping passed.

When docs policy is `required` or `changed`, when docs policy changes during the packet lifecycle, or when docs files are changed, Spec Guard must require a registered `docs_updated` claim and passed backend verification for that claim before review completion. For `required` docs, this requirement is in addition to docs existence and docs-to-AC mapping checks. For `changed` docs, the requirement is unconditional before review completion and is not based on a later semantic judgment about whether documented behavior changed.

Documentation itself must never be the target of retained tests. Tests must validate product behavior, API behavior, runtime behavior, or other approved non-document behavior. Spec Guard must not require or accept retained tests that assert documentation text, formatting, files, headings, examples, or links as governed evidence. Temporary scripts or tests that an agent uses to aid documentation work are permitted only if removed before review completion.

---

<a id="us-08-source"></a>
## 8. Product Platform and Architecture

> Derived user story: [US-08: Product platform and architecture decisions](user-stories/08-platform-architecture-decisions.md)

### 8.1 Product platform

Platform requiredness is deterministic. A Work Packet's `platform.required` is true for every packet except `operational_document` packets whose approved scope changes only documentation/operational content and packets whose platform is inherited from an approved parent Plan `product_context.platform_decision_id` or an accepted RuntimeBaseline `stack.product_platform`. When `platform.required` is false, `platform.not_required_reason` must record the deterministic basis. When true, packet approval readiness requires `platform.decision_id` to reference a recorded `platform_choice` HumanDecision.

The frontend agent must present a relevant numbered option list based on request, repository context, and observable facts.

Prompt requirements:

- numbered platform options,
- Something else,
- Discuss,
- custom prose support.

Custom platform text is captured as human text after numbered confirmation. Spec Guard must not map custom platform text to a hard-coded equivalent after confirmation.

A platform choice must record a HumanDecision with decision type `platform_choice`. `work.choice.propose` must store each final platform option with a structured payload sufficient to construct PlatformChoiceDecisionPayload. `work.choice.answer` or `work.choice.confirm_custom` must store a canonical PlatformChoiceDecisionPayload in `approved_payload` and update the Work Packet platform decision reference. Discuss and unconfirmed custom prose create no HumanDecision.

Plan approval does not create platform choices. `PlanProposalPayload.product_context.platform_decision_id` may only copy an already recorded platform HumanDecision id, and `platform_choice` is traceability text for that decision. If a Plan child requires a platform choice and no platform decision id is present, the child is not eligible for batch approval or authorization until the platform gate records the decision on that child.

Batch approval must not choose platform.

### 8.2 Architecture

When architecture affects implementation, persistence, runtime, deployment, API boundaries, or test strategy, Spec Guard must require human architecture review.

Architecture requiredness is deterministic from structured WorkPacket fields, not prose. `architecture.required` is true for API/contract-surface classifications and whenever `work.intent.draft` or `work.update` sets `architecture.required: true` with a non-empty `required_reason`. It is false for documentation-only `operational_document` packets and may be false for localized direct behavior/bugfix/one-off UI packets only when `architecture.not_required_reason` records the deterministic basis. Packet approval readiness requires at least one architecture decision id when `architecture.required` is true.

Each architecture option must include:

- label,
- description,
- benefits,
- costs/tradeoffs,
- downstream constraints or lock-in where relevant.

The prompt must include Something else and Discuss. Custom architecture requires numbered confirmation.

Architecture decisions are durable decision artifacts linked to affected Work Packets. `work.choice.propose` must store each architecture option with its label, description, benefits, costs/tradeoffs, and downstream constraints in a structured option payload. An architecture choice must record a HumanDecision with decision type `architecture_choice`. `work.choice.answer` or `work.choice.confirm_custom` must store a canonical ArchitectureChoiceDecisionPayload in `approved_payload` and update the affected Work Packet architecture decision references. Discuss and unconfirmed custom prose create no HumanDecision.

Plan approval does not create architecture choices. `PlanProposalPayload.product_context.architecture_decision_ids` may only copy already recorded architecture HumanDecision ids. If a Plan child requires architecture review and no architecture decision id is present, the child is not eligible for batch approval or authorization until the architecture gate records the decision on that child.

Batch approval must not choose architecture.

The backend verifier must not judge architecture quality.

---

<a id="us-09-source"></a>
## 9. Intent and AC Approval

> Derived user story: [US-09: Intent, source-derived ACs, and AC approval](user-stories/09-intent-ac-source-evidence.md)

### 9.1 Drafted intent

For any prompt requiring repository mutation, the frontend agent should draft:

- goal,
- desired outcomes,
- in scope,
- out of scope,
- users/actors if relevant,
- edge cases if relevant,
- open questions if any,
- ACs.

Required fields for moving from `draft` to `pending_ac_approval` are exactly: non-empty `title`, non-empty `intent.goal`, and at least one AcceptanceCriterion. Desired outcomes, in-scope, out-of-scope, users/actors, edge cases, and open questions are optional relevance-based arrays and may be empty.

Spec Guard should not prompt separately for every non-AC intent field by default.

Generated fields must not contain placeholders, `undefined`, or process boilerplate.

### 9.2 Source-derived ACs

When ACs are derived from source, mockup, design, screenshot, PDF, UI artifact, user story, or other interpreted material:

- they must be included in the displayed AC list,
- each source-derived AC must show source/evidence,
- the review surface must clearly mark which ACs are source-derived,
- the human approves them through the same AC approval gate as all other ACs,
- source-derived ACs are never batch-approved or batch-authorized,
- any packet containing source-derived ACs may be batch-created only and must then use normal per-child AC approval, Work Packet approval, and authorization gates,
- there is no separate one-AC-at-a-time source-derived approval flow,
- there is no custom feature-status prompt.

Yes on AC approval approves the displayed AC list, including displayed source-derived ACs and their source/evidence. Discuss allows in-session refinement and then re-presents the AC approval gate.

Spec Guard must not infer canonical source-derived ACs without human approval.

### 9.3 Source artifact registration

Source material used for source-derived ACs must be represented by a resolvable SourceArtifactRef. Arbitrary source material may be registered as a SourceArtifact regardless of file type, extension, media type, or artifact kind. Spec Guard must not maintain a closed list of acceptable source kinds.

A SourceArtifact revision must be immutable and content-addressed. SourceArtifact registration must capture bytes or a deterministic descriptor plus content hash sufficient to identify and review the material later. Hash-only registration is invalid unless the descriptor includes a deterministic retrieval mechanism and enough metadata for the reviewed material to be presented again. Every SourceArtifact revision must include an immutable `content_ref` or descriptor retrieval mechanism that allows the reviewed material or deterministic descriptor to be re-presented. A source that cannot be assigned a stable id, immutable revision, and content hash cannot satisfy source-derived AC evidence.

`source_artifact.register` creates revision 1 for new source material. `source_artifact.update` creates a new immutable revision and must not alter prior revisions. `source_artifact.get` resolves a SourceArtifactRef and verifies the referenced content hash. SourceArtifactRefs used in approved source-derived ACs must resolve at review time and at later staleness checks.

SourceArtifactRef may also refer to other immutable Spec Guard top-level artifacts by their canonical `artifact_type`, `id`, and `revision`. Built-in artifact refs must use the exact `artifact_type` stored on the artifact.

`source_artifact.register` and `source_artifact.update` accept exactly one of captured bytes or descriptor input. For captured bytes, callers provide `content_bytes_base64`; Spec Guard decodes base64, computes SHA-256 over the decoded bytes, stores the bytes in immutable blob storage, sets `content_ref` to that blob reference, and stores `descriptor: null`. For descriptor input, callers provide `descriptor`; Spec Guard canonicalizes the descriptor JSON, computes SHA-256 over the canonical descriptor bytes unless `content_hash` is supplied and matches that canonical hash, stores the descriptor as immutable content, and sets `content_ref` to the descriptor record. Hash-only input without bytes or descriptor is invalid. On update, absent metadata fields inherit the prior revision; `locator: null` explicitly clears the locator; `kind` and `label` cannot be null.

### 9.4 AC review snapshot and approval gate

For a single Work Packet path, AC approval is mandatory and separate from Work Packet approval.

The `work.ac.review` action renders a non-mutating AC review snapshot. It accepts an optional `proposed_ac_payload`. If omitted, it renders the current packet AC proposal. If supplied, it renders and hashes that supplied in-session refined payload without writing it to any artifact. The snapshot includes the complete AC payload being reviewed, source/evidence for source-derived ACs, snapshot hash, and snapshot revision. During Discuss, refinement remains in the agent session and does not write artifacts. When the human is ready to answer Yes or No, the approval action submits the exact reviewed AC payload with its hash and revision.

`work.ac.approve` must validate the supplied review snapshot hash against `AcReviewSnapshotPayload`, not against the raw AC array alone. It constructs `AcReviewSnapshotPayload` with `work_id` equal to the action `id`, `work_packet_revision` equal to the current pre-mutation WorkPacket revision, and `acceptance_criteria` equal to `reviewed_ac_payload`, canonicalizes it, and compares that hash to `review_snapshot_hash`. On numbered Yes, Spec Guard atomically writes the AC payload as canonical and records AC approval. On numbered No, Spec Guard records decline or blocks as appropriate without approving the AC payload. On Discuss, the action records no mutation and should not be called to persist refinements.

AC approval prompt:

`Do you approve these acceptance criteria as currently drafted?`

1. Yes
2. No
3. Discuss

Rules:

- Yes records AC approval bound to the displayed AC review snapshot hash.
- No records decline or blocks as appropriate.
- Discuss records no mutation.
- During Discuss, the frontend agent may refine ACs in the agent session only.
- Intermediate AC refinements during Discuss must not mutate canonical ACs, approval state, decline state, or artifact hashes.
- After refinement, the frontend agent must re-present the current proposed ACs through the same Yes/No/Discuss gate.
- The loop resolves only through numbered Yes or numbered No.

AC changes after approval invalidate AC approval and any dependent Work Packet approval.

The backend verifier must not judge whether approved ACs are correct or complete.

---

<a id="us-10-source"></a>
## 10. Single Packet Approval and Authorization

> Derived user story: [US-10: Single packet approval and authorization](user-stories/10-single-packet-approval-authorization.md)

### 10.1 Single Work Packet path

If work is not under an approved Plan batch flow, Spec Guard must use sequential gates:

1. AC approval gate.
2. Work Packet approval gate.
3. Implementation authorization gate.

No combined AC+packet approval gate is allowed for a single Work Packet path.

### 10.2 Readiness levels

#### AC-approval-ready

A packet is AC-approval-ready when:

- goal exists,
- at least one AC exists,
- source-derived ACs include source/evidence,
- AC review snapshot can be rendered,
- no AC-approval-blocking diagnostics exist.

#### Packet-approval-ready

A packet is packet-approval-ready when:

- ACs are approved, except for eligible Plan-child batch approval where the same batch selection explicitly approves displayed non-source-derived ACs,
- the packet contains no unapproved source-derived ACs,
- runtime baseline is accepted,
- classification is valid,
- docs policy is valid,
- allowed file globs are present,
- required platform choice is recorded,
- required architecture choice is recorded,
- no required human decision is pending,
- no packet-approval-blocking diagnostics exist.

#### Authorization-ready

A packet is authorization-ready when:

- packet is approved at current review snapshot hash,
- runtime baseline remains accepted,
- approval is not stale,
- allowed scope is known,
- parent Plan relationship is valid when applicable,
- packet change baseline can be captured,
- no authorization-blocking diagnostics exist.

#### Batch-authorization-ready

A proposed Plan child is batch-authorization-ready before artifact creation when:

- the proposed child payload is included in a persisted batch review snapshot,
- the proposed child contains no source-derived ACs,
- the proposed child is batch packet-approval eligible,
- the proposed child packet review snapshot is present,
- the proposed child authorization review snapshot is present,
- runtime baseline remains accepted,
- allowed scope is known in the proposed child payload,
- packet change baseline capture is expected to succeed after child artifact creation,
- no batch-authorization-blocking diagnostics exist.

Batch authorization readiness is evaluated against the proposed child payload and child snapshot bindings. It is not the same as normal authorization-ready, which applies to an existing Work Packet artifact.

#### Implementation-ready

A packet is implementation-ready when:

- authorization is recorded,
- packet change baseline is captured,
- pre-implementation validation passes,
- required pre-implementation docs/tests/failure-first chain is complete: required docs exist and are linked, retained test files exist when tests are required, and failure-first evidence is recorded; passing-test evidence is not required until review completion,
- required backend verification for pre-implementation has passed, excluding `docs_updated` verification that section 12.8 explicitly permits to remain pending until review completion,
- no implementation-blocking diagnostics exist.

Implementation source changes must not occur before implementation-ready state.

### 10.3 Work Packet approval gate

Prompt:

`Do you approve this Work Packet as shown?`

1. Yes
2. No
3. Discuss

Yes records packet approval bound to the displayed packet review snapshot hash. No records decline or blocks as appropriate. Discuss records no mutation and later re-presents the same gate.

### 10.4 Implementation authorization gate

Prompt:

`Do you authorize implementation for this Work Packet?`

1. Yes
2. No
3. Discuss

Yes records authorization, captures packet change baseline, and binds authorization to the authorization review snapshot hash. The authorization review snapshot must include the approved packet snapshot hash and revision. No records decline or blocks as appropriate. Discuss records no mutation and later re-presents the same gate.

Authorization permits the agent to perform pre-implementation validation work. It does not permit implementation source changes until pre-implementation validation passes.

---

<a id="us-11-source"></a>
## 11. Plan Lifecycle and Batch Acceleration

> Derived user story: [US-11: Plan lifecycle and batch acceleration](user-stories/11-plan-lifecycle-batch-acceleration.md)

### 11.1 Plan-vs-single fixed decision

Before asking whether work should be a single packet or a Plan, the frontend agent must present relevant ACs unless already in a valid Plan flow.

Prompt:

1. Single packet is sufficient
2. Create a Plan
3. Discuss

Option 1 records single-packet decision and leaves the source Work Packet active. Option 2 records Plan decision, sets the source Work Packet to `deferred` with diagnostics pointing to the Plan flow, and later Plan approval records `source_work_id` on the Plan. If Plan approval is declined or no Plan is created, Spec Guard restores the source Work Packet to its pre-deferral status and records diagnostics linking the declined Plan attempt. Option 3 mutates nothing, creates no HumanDecision, and re-prompts later. No Something else/custom option is allowed.

The decision must be recorded through `work.plan_choice.answer`. It must not be recorded through generic `decision.create`, because option 2 has the side effect of deferring the source Work Packet. The recorded HumanDecision must store a canonical PlanVsSingleDecisionPayload in `approved_payload` with the work id, selected option, the exact AC payload presented before the decision, and its hash. `presented_ac_refs` are traceability aids and are not sufficient without the presented payload/hash.

### 11.2 Non-mutating Plan proposal

After the human selects Plan, the frontend agent proposes a Plan containing child slices and metadata. `plan.propose` is non-mutating and accepts the full `plan_proposal_payload`: title, goal, product context, source/request context, source evidence summary when relevant, and slices. It returns a proposed Plan review snapshot for that exact payload. It does not create a Plan and does not create children. Every slice `proposed_id` must match `^[A-Za-z0-9._-]+$`; `plan.propose` and `plan.approve` must reject Plan proposals with proposed ids that cannot be used safely in batch child snapshot revisions. Every Plan slice must include at least one full AcceptanceCriterion payload. Any Plan slice containing source-derived ACs must include full AC payloads, not only AC ids, and each source-derived AC must include SourceEvidence with non-empty canonical `source_artifact_refs` and `evidence_hash`.

### 11.3 Plan approval

The Plan proposal is shown to the human with:

1. Yes
2. No
3. Discuss

The `plan.approve` shared action submits the same `plan_proposal_payload` with selected number, raw response, prompt, human confirmation, review snapshot hash, and review snapshot revision. Spec Guard validates that the submitted payload hashes to the supplied snapshot hash. `source_work_id` is part of PlanProposalPayload; any top-level `source_work_id` action input must equal the payload field. Numbered Yes records Plan approval and creates a non-implementable Plan containing the approved slices, `source_work_id`, and metadata.

Plan approval does not create child Work Packets. The created Plan stores the approved PlanProposalPayload as `plan_proposal` and stores the Plan approval HumanDecision outside `plan_proposal`.

Numbered No records a standalone decline HumanDecision or project-level decision-log entry and creates no Plan. Discuss records no mutation and later re-presents the same gate for the current or revised proposal.

After Plan approval, batch proceed or one-at-a-time child creation creates child Work Packets from the approved Plan.

One-at-a-time child creation uses `plan.child.create`. The action must reference the approved Plan id, the approved Plan proposal hash/snapshot revision, a `plan_slice_id` from the approved Plan, and the proposed child payload. Spec Guard must validate that the child payload corresponds to the approved Plan slice before creating the Work Packet. `proposed_child_id` must equal `plan_slice_id`; alternate child id mappings are not supported by this specification.

Child payload correspondence requires exact match between `plan_slice_id` and an approved Plan slice `proposed_id`, requires `proposed_work_payload.id` to equal `plan_slice_id`, and requires exact match for title, goal, classification, docs policy, allowed globs, source-derived flag, source evidence summary, and full AcceptanceCriterion payloads recorded in the approved Plan proposal. Desired outcomes, in-scope, out-of-scope, users/actors, edge cases, and open questions in ProposedWorkPacketPayload must exactly match the corresponding approved Plan slice arrays. Platform and architecture may be copied from approved Plan product context only when that context contains prior platform/architecture HumanDecision ids; otherwise they must remain unset until the child records its own platform/architecture decisions. `runtime_baseline_ref` may be null at create-only child creation time; any non-null runtime baseline ref must reference an accepted baseline, and packet approval or authorization readiness requires an accepted runtime baseline ref. `docs.requirements` and `scope.deviations` may be carried as child review context but are not Plan-slice correspondence fields unless explicitly present in the approved Plan slice. The created WorkPacket must durably store `parent_plan_id` and `plan_slice_id`. Implementations must not create a child with broader scope, different classification, different docs policy, or additional ACs through `plan.child.create`; such changes require Plan amendment or a separate Work Packet approval path.

The backend verifier must not judge whether the Plan proposal is good, complete, or optimal.

### 11.4 Batch proceed for Plan children

Plan slices are high-level coordination metadata. Before a batch proceed decision, `plan.batch_snapshot.create` must receive a `proposed_children_payload` that expands approved Plan slices into proposed child Work Packet payloads. Each proposed child entry must include `plan_slice_id`, `proposed_child_id`, `expected_created_work_packet_revision`, canonical `proposed_work_payload`, and caller-proposed readiness diagnostics. `plan.batch_snapshot.create` must recompute readiness and eligibility through the deterministic kernel, replace caller-proposed readiness fields with kernel-computed values in the persisted BatchReviewSnapshot, and reject only when the proposed child payload itself is invalid; caller readiness diagnostics are hints and are not trusted facts. `plan_slice_id` must match an approved Plan slice `proposed_id`, `proposed_child_id` must equal `plan_slice_id`, `proposed_work_payload.id` must equal `proposed_child_id`, and `proposed_work_payload.title` must match the approved Plan slice title. Optional shorthand mirror fields may be supplied for readability and validation, but `proposed_work_payload` is the canonical source for hashing, snapshotting, equality, and child creation. `proposed_children_payload_hash` is the hash of canonical ProposedChildrenPayload, and `proposed_children_payload_snapshot_revision` is exactly `payload:<proposed_children_payload_hash>`.

Batch child correspondence must enforce the same approved Plan slice constraints as `plan.child.create`: title, goal, classification, docs policy, allowed globs, source-derived flag, source evidence summary, and full AcceptanceCriterion payloads must match the approved Plan slice. `plan.batch_snapshot.create` must reject a proposed child that broadens scope, changes classification, changes docs policy, changes source-derived status, changes source evidence summary, adds ACs, or otherwise fails correspondence with the approved Plan slice.

`plan.batch_snapshot.create` derives `source_artifact_refs` deterministically as a canonical set. The set is the union of: the approved Plan artifact ref, top-level `proposed_children_payload.source_artifact_refs`, each proposed child's provenance refs, and each proposed source-derived AC SourceEvidence `source_artifact_refs`. The approved Plan artifact ref is exactly `{ "artifact_type": "plan", "id": <plan.id>, "revision": <plan.revision> }`. Duplicate refs are removed by exact tuple identity `(artifact_type, id, revision)`. The resulting array is sorted by Unicode code point order over the canonical UTF-8 strings for `artifact_type`, then `id` with null before strings, then numeric `revision`; locale collation must not be used. Snapshot hashing must use this canonical array.

Snapshot-level source refs are review-surface bindings for immediate validation and replay. At snapshot creation and decision validation, every listed ref must resolve and any supplied content hash must match. Later approval invalidation treats only refs that also appear in approved source-derived AC SourceEvidence as governed source dependencies. Top-level and child-level provenance-only refs becoming unavailable after approval create replay diagnostics but do not stale AC approval, Work Packet approval, Plan approval, or batch decisions by themselves.

A proposed child has a governed source dependency only when a source-derived AC SourceEvidence record includes that SourceArtifactRef. Child-level and top-level source refs in ProposedChildrenPayload are provenance-only unless also present on SourceEvidence for a source-derived AC. Spec Guard must not infer dependencies from free-form descriptions, paths, filenames, media types, extensions, or prose. Source-derived AC SourceEvidence must declare at least one SourceArtifactRef. If source-derived AC evidence omits required refs, declared refs cannot be canonicalized, or declared refs do not resolve to immutable SourceArtifact revisions or other known immutable top-level artifact revisions, the action must reject the batch snapshot request with diagnostics.

Spec Guard must not restrict source-derived evidence to a finite list of file types, extensions, media types, or artifact kinds. Source evidence kinds and source artifact kinds are open strings. Deterministic validation checks that refs are registered or otherwise resolvable, canonicalized, hashable, review-visible, and approval-bound; it does not validate whether the kind or file type is acceptable source material.

`plan.batch_snapshot.create` persists a batch review snapshot as an audit-only mutation. It does not create children, approve ACs, approve Work Packets, authorize implementation, change Plan intent, or increment the governed Plan revision. A BatchReviewSnapshot's `plan_revision` is the governed Plan revision of the approved Plan content, not an audit storage sequence. Its `snapshot_hash` is computed over `BatchReviewSnapshotPayload`, which excludes the enclosing record's `id`, `snapshot_hash`, `snapshot_revision`, `audit_revision`, `created_at`, and nested child `ReviewSnapshot` records; this prevents circular or volatile hashing.

The `plan.batch_proceed` shared action records the human's batch proceed selection after Plan approval for selected options 1 through 4. For option 5 Discuss, it records no HumanDecision, creates no BatchProceedRecord, and performs no mutation. Before creating children, approvals, authorizations, or baselines for options 1 through 4, the action must construct and validate a canonical `BatchProceedSelectionPayload` from the selected option and persisted batch snapshot. If this preflight validation fails, the action must perform no child mutation and record no HumanDecision or BatchProceedRecord. The human decision approves only this pre-decision selection payload. After preflight succeeds, per-child execution may partially fail. The action must then construct a separate canonical `BatchProceedResult` containing created child ids, approval results, authorization results, packet change baseline refs, and diagnostics for every proposed child, including failed or skipped child operations. It must store both records in a Plan `BatchProceedRecord` together with their hashes/revisions and the human decision, even when some child operations failed after earlier child mutations succeeded. It must not roll back already committed successful child mutations unless the implementation provides a real transaction that rolls back all child and Plan writes. `selection_revision` must be `batch-selection:<batch_snapshot_revision>:<selection_hash>`. `result_revision` must be `batch-result:<batch_snapshot_revision>:<result_hash>`. The `plan_batch_proceed` approved fields are JSON pointers into the stored `BatchProceedSelectionPayload`, not the post-action result.

The `plan_batch_proceed` HumanDecision must populate `review_snapshot_hash` and `review_snapshot_revision` with the batch snapshot hash and revision, must populate `parent_batch_snapshot_hash` and `parent_batch_snapshot_revision` with the same values, must copy `source_artifact_refs` from the BatchReviewSnapshot, must set `approved_payload_ref` to the BatchProceedRecord selection hash and revision, and must leave `approved_payload`, `approved_payload_hash`, and `approved_payload_revision` null unless an implementation intentionally duplicates the selection payload in addition to keeping the BatchProceedRecord as canonical.

Batch proceed prompt after child suggestions:

1. Work through one child slice at a time
2. Create all suggested child slices, then stop for review
3. Create all suggested child slices and approve eligible displayed non-source-derived child ACs and Work Packets
4. Create all suggested child slices, approve eligible displayed non-source-derived child ACs and Work Packets, and authorize eligible child Work Packets
5. Discuss

Rules:

- Option 1 records a BatchProceedRecord and HumanDecision for the selected one-at-a-time path, creates no children, records no child AC approval, records no Work Packet approval, records no authorization, and returns `plan.child.create` as the next action. Its BatchProceedSelectionPayload must include each proposed child with `selected_for_creation: false`, `requested_ac_batch_approval: false`, `requested_packet_batch_approval: false`, and `requested_batch_authorization: false`. Its BatchProceedResult must include one row for each proposed child with `created_work_packet_id: null`, approval and authorization booleans false, `packet_change_baseline_ref: null`, and diagnostics empty or informational.
- Option 2 creates children only. Its BatchProceedSelectionPayload must include every proposed child with `selected_for_creation: true`, `requested_ac_batch_approval: false`, `requested_packet_batch_approval: false`, and `requested_batch_authorization: false`. Created children start `pending_ac_approval` when ACs exist and no batch approvals are recorded, including all source-derived children.
- Option 3 creates all suggested child Work Packets and approves only children packet-approval-ready under batch rules. Its BatchProceedSelectionPayload must include every proposed child with `selected_for_creation: true`; for each child, `requested_ac_batch_approval` and `requested_packet_batch_approval` are true only when `batch_approval_eligible` and readiness diagnostics are clean, and false otherwise; `requested_batch_authorization` is always false. Children with batch AC and packet approval recorded start `approved`; created children without both approvals start `pending_ac_approval`.
- Option 4 creates all suggested child Work Packets, approves children packet-approval-ready under batch rules, and authorizes only children batch-authorization-ready. Its BatchProceedSelectionPayload must include every proposed child with `selected_for_creation: true`; for each child, `requested_ac_batch_approval` and `requested_packet_batch_approval` are true when `batch_approval_eligible` and readiness diagnostics are clean, and false otherwise; `requested_batch_authorization` is true only when `batch_authorization_eligible` and readiness diagnostics are clean, and false otherwise. Children with authorization recorded start `authorized`; children with approvals but no authorization start `approved`; other created children start `pending_ac_approval`.
- In BatchProceedSelectionPayload, child `ac_snapshot_hash`/`ac_snapshot_revision` are populated only when `requested_ac_batch_approval` is true; `packet_snapshot_hash`/`packet_snapshot_revision` are populated only when `requested_packet_batch_approval` is true; and `authorization_snapshot_hash`/`authorization_snapshot_revision` are populated only when `requested_batch_authorization` is true. All unrequested, ineligible, unavailable, or option-1/option-2 child snapshot fields are null.
- For every child authorized by option 4, Spec Guard must capture and store that child's PacketChangeBaseline atomically with the child authorization decision.
- If PacketChangeBaseline capture is blocked for a child, that child must not be authorized. The batch result may partially succeed for other eligible children, but it must report per-child authorization failure diagnostics and next actions.
- Option 5 mutates nothing.
- Runtime baseline must be accepted before options 3 or 4 can be selected as mutating options. Batch proceed prompt numbering is fixed: options 1 through 5 always keep their numbers. If the baseline is not accepted, options 3 and 4 must be shown as unavailable diagnostics under their fixed numbers; selecting an unavailable option records no HumanDecision and returns blocking diagnostics.
- Batch review must display each affected child packet's ACs, source-derived AC evidence, scope, classification, docs policy, allowed globs, platform, architecture, and diagnostics from the persisted batch review snapshot.
- Batch approval and batch authorization must exclude any child containing source-derived ACs.
- Batch must not choose platform, architecture, runtime baseline acceptance, Plan-vs-single, or Plan approval.
- Batch must not skip deterministic gates or required backend verification.
- Batch approvals and authorizations must bind per child according to section 4.7.

---

<a id="us-12-source"></a>
## 12. Implementation Boundary and Pre-Implementation Validation

> Derived user story: [US-12: Implementation boundary and pre-implementation validation](user-stories/12-preimplementation-validation-boundaries.md)

### 12.1 File categories

Spec Guard must classify changed paths into the canonical `ChangeFileCategory` enum using `Config.path_policy`.

`Config.path_policy` contains ordered glob arrays for `spec_guard_artifact_evidence`, `docs`, `tests`, `implementation_source`, `runtime_product_configuration`, `generated_build_output`, and `ignored_paths`. The deterministic classifier normalizes each repository-relative path, rejects paths outside the project, ignores paths matching `ignored_paths`, then assigns the first matching category in this fixed precedence: `spec_guard_artifact_evidence`, `docs`, `tests`, `runtime_product_configuration`, `implementation_source`, `generated_build_output`. If no category glob matches, the category is `other_unexpected`. Category globs are project-relative and use the same glob engine as allowed-globs validation.

Implementation source includes files that affect product behavior, public API, runtime behavior, UI behavior, business logic, persistence, integration behavior, or shipped assets. For ordering gates, `runtime_product_configuration` is always treated as implementation-like and pre-failure changes to it block pre-implementation validation; Spec Guard does not make semantic behavior-impact judgments to relax this rule.

### 12.2 Allowed pre-implementation changes

Before implementation-ready state, allowed changes are limited to:

- Spec Guard artifacts/evidence,
- required docs,
- tests intended to fail against missing approved behavior.

Required governed docs, tests, and failure-first evidence for a packet must be recorded after packet change baseline capture to count for that packet's validation chain. Pre-authorization docs/tests may exist, but they are treated as pre-existing project state unless re-recorded with evidence after authorization; they must not disappear from review traceability by being silently absorbed into the packet baseline.

Implementation source changes before proven failure-first evidence must block pre-implementation validation.

Docs, test failure, test pass, and runtime evidence records must include a file state snapshot captured by Spec Guard during the evidence action. The snapshot must be sufficient to compare changed files against the packet change baseline and prove whether implementation source had changed before failure-first evidence. Evidence without the required file state snapshot cannot satisfy pre-implementation or review gates.

Command-backed evidence must reference a kernel-created CommandResult from `command.run`. Frontend agents must not supply exit codes, command status, command timestamps, or command output as trusted facts. Evidence actions may accept paths, related AC IDs, summaries, and claim text from the frontend agent, but command, exit code, timing, status, and output references used as governed evidence must come from the deterministic kernel.

CommandResult status derivation is deterministic: a spawned process that exits with code `0` before timeout is `passed`; a spawned process that exits with any non-zero code is `failed`; spawn errors, missing executables, permission errors, and signal termination are `failed` with `exit_code: null` and a populated error message; timeout is `timed_out`; and `skipped` may be recorded only for a deterministic precondition skip requested by `command.run`. Evidence status is derived from CommandResult status as follows: `passed` maps to evidence `passed`; `failed` maps to evidence `failed`; `timed_out` maps to evidence `inconclusive`; `skipped` maps to evidence `inconclusive`. CommandResults with `exit_code: null`, spawn errors, missing executables, permission errors, signal termination, `timed_out`, or `skipped` cannot satisfy required failure-first, passing-test, or runtime evidence gates.

CommandResult purpose compatibility:

| Evidence action/type | Allowed CommandResult purpose |
|---|---|
| `work.evidence.failure` with failure-first role | `test` |
| `work.evidence.pass` with passing-test role | `test` |
| `work.evidence.runtime` production | `runtime_production` |
| `work.evidence.runtime` development | `runtime_development` |
| Runtime baseline validation evidence | `test`, `build`, `runtime_production`, `runtime_development` as applicable |

`work.evidence.runtime.mode` values are exactly `production` and `development`. Mode `production` requires CommandResult purpose `runtime_production` and creates EvidenceRecord type `runtime_production`. Mode `development` requires CommandResult purpose `runtime_development` and creates EvidenceRecord type `runtime_development`.

Evidence actions must reject a CommandResult whose purpose is incompatible with the evidence type. Build commands may be recorded as CommandResults for baseline or review context, but they do not satisfy behavior test failure/pass evidence unless separately paired with compatible test evidence.

Frontend agents must not supply file state snapshots as trusted inputs. They may supply paths and summaries, but Spec Guard must capture VCS or manifest state itself before committing the evidence record.

`work.implementation.complete` must register at least one `implementation_summary` claim from its submitted summary and implementation file list. Review completion cannot pass until that claim is validated or superseded through `work.claims.create`/`work.claims.validate` with evidence-backed final claims.

### 12.3 Test cleanup and side-effect rules

Tests must be cleanup-safe.

Retained tests must not test documentation text, documentation formatting, documentation files, headings, examples, or links. Documentation itself is never governed by retained tests. Deterministic retained-doc-test detection is byte/string based and language-independent: a retained test is flagged when its path also matches a docs glob, when its path matches `Config.path_policy.docs_test_manifests`, or when its UTF-8-decoded content contains an exact normalized docs/content path token from docs evidence/path policy together with one of these case-sensitive operation tokens in the same file: `readFile`, `readFileSync`, `open`, `openSync`, `import`, `require`, `fetch`, `assert`, `expect`, `should`, `toContain`, `toMatch`. A retained test is also flagged when it contains exact known docs heading/link/example tokens captured in docs EvidenceRecords and any assertion token from the list above. Non-UTF-8 test files or suspected documentation-targeting behavior not caught by these deterministic rules require backend verification of a `retained_test_not_docs` claim before review completion.

Passing or failing test evidence must not leave persistent artifacts, generated files, database tables, database rows, external resources, orphan processes, modified runtime state, or other side effects unless those changes are explicitly approved as part of the product change.

Any temporary artifacts/resources created during tests must be cleaned up by the test or test harness. Database-backed tests must isolate state and clean up records, tables, rows, indexes, queues, buckets, messages, or external resources they create unless the approved AC explicitly requires persistent seed/schema changes.

Cleanup verification is recorded through `work.evidence.cleanup`. For test/runtime commands with non-empty `resource_categories`, `command.run` must capture configured cleanup observer before-observations immediately before spawning the command and after-observations immediately after command completion/timeout/termination, and store them on the CommandResult. Checked resource categories may be requested by the caller, but before/after observations and side-effect status must be kernel-captured, command-backed, or derived from deterministic evidence records. Caller-supplied cleanup summaries are claims only and cannot establish cleanup truth. Cleanup records must store checked resource categories, kernel-captured before/after observations or CommandResult refs, side-effect status derived by the kernel, related command/evidence refs, and any remaining cleanup actions.

Built-in cleanup observers are `files` and `processes`. The `files` observer records a manifest of project-relative paths, sizes, mtimes, and content hashes under allowed temp/output/resource paths before and after the command; comparison rule `no_new_resources` passes only when no unapproved new or modified paths remain. The `processes` observer records child process ids, command lines, and start times for processes spawned by the command process tree; it passes only when no spawned process remains alive after cleanup. Other resource categories such as databases, queues, buckets, services, or external resources require configured command-backed observers in `Config.cleanup_observers`. A cleanup observer must define resource category, identity fields, before command or deterministic capture method, after command or deterministic capture method, and comparison rule. Cleanup applicability is determined only from structured `resource_categories` fields on CleanupEvidence, NotApplicableEvidence, EvidenceRecord cleanup records, failure/pass/runtime evidence records, and final claims; free-text summaries and reasons are not parsed. Failure, pass, and runtime evidence actions may receive `resource_categories` from the caller as claimed affected resource categories; Spec Guard stores them as structured claims and uses exact string equality for cleanup applicability. Cleanup evidence must provide the checked `resource_categories` explicitly, and configured observers decide whether those categories are clean. Without a configured observer, a non-file/process resource category can be marked cleanup not applicable only when no structured record lists that exact resource category string. If any approved or deterministic record lists the category and no observer exists, cleanup is blocked with diagnostics requiring observer configuration or human-approved scope change.

When tests or failure-first evidence are not applicable, the not-applicable decision is recorded through `work.evidence.not_applicable`. It must identify the evidence type being marked not applicable, the reason, the classification/policy that permits it, and the approved ACs or scope it applies to. Evidence type `tests` is a single deterministic not-applicable record that covers both retained passing tests and failure-first test evidence; otherwise implementations may record separate `test_failure` and `test_pass` not-applicable records.

`work.evidence.not_applicable` must not bypass evidence gates by assertion alone. It can record tests or failure-first not applicable only when deterministic eligibility is established by classification, approved docs/content policy, and the validation chain in this specification. It can record `implementation_files` not applicable only when changed-file classification since PacketChangeBaseline contains no `implementation_source` or `runtime_product_configuration` files and the packet classification/policy is documentation/content-only. Human confirmation alone must not make tests or failure-first evidence not applicable for product/API/runtime behavior packets. Human confirmation may be required to record awareness of an eligible not-applicable decision, but it cannot override deterministic ineligibility.

Review completion must block when tests leave behind unapproved files, data, processes, external resources, or runtime state.

### 12.4 Allowed-globs enforcement

Allowed globs apply to product-scope changed files:

- docs,
- tests,
- implementation source,
- runtime/product configuration,
- generated build output when tracked or submitted as evidence.

Spec Guard artifact/evidence paths are exempt from allowed-globs blocking, but they must still be tracked and audited.

Path and glob semantics are deterministic:

- Paths are normalized to repository-relative POSIX-style paths using `/` separators.
- Absolute paths and paths containing `..` after normalization are invalid as governed paths.
- Symlink paths are resolved for classification; changes through symlinks are attributed to the resolved repository-relative path when inside the project, and rejected when they resolve outside the project.
- Case sensitivity follows the packet change baseline mode: VCS mode uses the VCS-reported path identity; manifest mode records exact path strings and treats them as case-sensitive.
- Glob matching uses `/` separators, `*` for a single path segment fragment, `**` for zero or more path segments, and `?` for one character within a segment.
- Negated globs are not supported unless a future schema explicitly adds them.
- Glob patterns are repository-relative and must not be absolute or contain `..` after normalization.

Other/unexpected files are never silently allowed. They require diagnostics and explicit resolution.

### 12.5 API/contract-surface validation chain

For `reusable_api`, `rest_api`, and `reusable_ui`:

approved ACs → human-facing docs → tests → proven failure → implementation source changes.

Deterministic checks must validate:

- AC approval exists,
- docs exist and are linked to approved AC IDs,
- docs were recorded before behavior tests that claim to validate the documented contract,
- tests exist and are real test paths,
- retained tests do not test documentation files or documentation text,
- failure evidence exists,
- command result is recorded,
- implementation source did not change before failure-first evidence,
- product-scope changed files are within allowed globs.

Required backend verification for the full API/contract-surface chain must pass for:

- docs-to-AC mapping,
- docs-updated semantic claim when docs are added, changed, or required by policy,
- behavior-tests-to-documented-contract mapping,
- failure evidence semantic claim when the failure is used to prove missing approved behavior.

For pre-implementation validation, docs existence, docs-to-AC mapping, behavior-test mapping, and failure-evidence requirements above must already be satisfied, but `docs_updated` follows section 12.8 and may remain pending until review completion.

### 12.6 Non-API validation chains

For non-API packets with docs policy `required`:

approved ACs → human-facing docs → tests → proven failure → implementation source changes.

For non-API packets without required docs:

approved ACs → tests → proven failure → implementation source changes.

Deterministic checks must validate:

- AC approval exists,
- required docs exist when docs policy is `required`,
- required docs are linked to approved AC IDs when docs policy is `required`,
- required docs were recorded before behavior tests that claim to validate the documented contract,
- tests exist and are real test paths,
- retained tests do not test documentation files or documentation text,
- failure evidence exists,
- command result is recorded,
- implementation source did not change before failure-first evidence,
- product-scope changed files are within allowed globs.

Required backend verification for the full non-API chain must pass for:

- docs-to-AC mapping when docs policy is `required`,
- docs-updated semantic claim when docs policy is `required`, docs policy is `changed`, docs policy changed during the packet lifecycle, or docs files changed,
- behavior-tests-to-documented-contract mapping when docs policy is `required`,
- tests-to-AC mapping,
- failure evidence semantic claim when the failure is used to prove missing approved behavior.

For pre-implementation validation, docs existence, docs-to-AC mapping when required, behavior-test mapping when required, tests-to-AC mapping, and failure-evidence requirements above must already be satisfied, but `docs_updated` follows section 12.8 and may remain pending until review completion.

### 12.7 Operational-document validation chain

For `operational_document` packets that do not change product behavior:

approved ACs → documentation/content changes → review validation.

Deterministic checks must validate:

- AC approval exists,
- docs/content paths are inside project,
- docs/content files exist,
- changed files are limited to approved docs/content paths and Spec Guard artifacts/evidence,
- test/failure-first not-applicable reason is recorded,
- no retained tests were added for documentation text/files,
- no implementation source changed.

Required backend verification must pass for:

- docs/content-to-AC mapping,
- docs-updated semantic claim.

If an operational-document packet changes product behavior, runtime behavior, API behavior, schema, persistence, or shipped application code, this documentation-only chain is invalid.

### 12.8 Docs-updated gate wiring

Spec Guard must require a registered `docs_updated` claim and passed backend verification before review completion when any of these conditions are true:

- docs policy is `required`,
- docs policy is `changed`,
- docs policy changed after Work Packet approval,
- docs/content files changed in the packet diff,
- docs evidence was added or updated.

For docs policy `required`, pre-implementation validation must also require docs existence, docs-to-AC traceability, and any required docs-to-AC backend verification before implementation source changes. The `docs_updated` claim may pass at pre-implementation time or later, but review completion must block until it passes.

For docs policy `changed`, docs evidence identifying the updated docs/content paths must exist before review completion. The docs do not need to precede tests unless another rule requires that ordering, but the `docs_updated` claim must pass before review completion.

---

<a id="us-13-source"></a>
## 13. Backend Verifier

> Derived user story: [US-13: Backend verifier](user-stories/13-backend-verifier.md)

### 13.1 Adapter modes

Spec Guard must support:

1. Disabled.
2. Local command adapter.
3. HTTP endpoint adapter, optional unless implemented and exposed.
4. Provider/model adapter, optional unless implemented and exposed.
5. Test fixture adapter for Spec Guard's own tests only.

The local command adapter is the minimum required executable adapter. The first required concrete local command adapter is the Pi headless RPC command adapter.

If an adapter mode is selectable/configurable, it must actually execute verification tasks and pass health checks. Spec Guard must not collect HTTP or provider/model configuration as usable when that adapter cannot be invoked.

Required semantic verification blocks if no healthy executable adapter is configured.

### 13.2 Claim registration

Required backend verification operates on registered claims. Spec Guard must create or derive stable claim IDs before calling the verifier. The WorkPacket top-level `claims` array is the canonical claim registry for packet-scoped claims; `review.claims` is only the review/final subset or references into that registry.

Claim registration rules:

- Docs evidence actions register docs-to-AC mapping claims when docs are required.
- Docs evidence actions register docs-updated semantic claims when docs are required, docs policy is `changed`, docs policy changes, docs evidence is added or updated, or docs files are changed.
- `work.docs.add`, `work.docs.update`, and docs-policy changes through `work.update` must register or update stable pending `docs_updated` claims for affected docs/ACs.
- `work.preimplementation.validate`, `work.review.validate`, and `work.review.complete` must deterministically detect docs/content file changes and docs policy triggers. If a required `docs_updated` claim is missing, mutating actions may register a stable pending claim; non-mutating actions must return the derived pending claim data and a blocking next action. Direct docs/content file changes without docs evidence do not satisfy docs-updated requirements.
- Test failure/pass evidence actions register tests-to-AC claims and, when docs are required, behavior-tests-to-documented-contract claims.
- Failure evidence actions register failure-evidence semantic claims when failure-first evidence is required.
- Runtime evidence actions register runtime claims for any semantic runtime assertion beyond exact command/path/status existence.
- Review submission records register implementation summary claims.
- Final claim validation registers final user-facing claims, including whether each is presented as verified or explicitly unverified.

Registered claims must include claim id, text, claim type, related AC IDs, related docs IDs when applicable, and evidence refs. `work.backend.verify` must reject unknown claim IDs.

### 13.3 Verification requirement matrix

| Claim or fact | Backend verification |
|---|---|
| Docs-to-AC mapping for API/contract-surface packets | Required |
| Behavior-tests-to-documented-contract mapping for API/contract-surface packets | Required |
| Docs-to-AC mapping for non-API docs-required packets | Required |
| Behavior-tests-to-documented-contract mapping for non-API docs-required packets | Required |
| Tests-to-AC mapping for non-API packets | Required when tests are required |
| Failure evidence semantic claim used to prove missing approved behavior | Required when failure-first evidence is required |
| Retained test is not documentation-targeting (`retained_test_not_docs`) | Required when retained-doc-test detection is inconclusive |
| Runtime claim beyond exact command/path/status existence | Required |
| Final user-facing claim presented as verified/completed | Required |
| Final user-facing claim explicitly marked unverified | No semantic support verification; deterministic label validation required |
| Implementation summary claim | Required for review completion |
| Docs-updated semantic claim | Required when docs are required or changed |
| File existence | Never; deterministic |
| Path safety | Never; deterministic |
| Changed-file list | Never; deterministic |
| Command exit code/status existence | Never; deterministic |
| Package script existence | Never; deterministic |
| Approval hash freshness | Never; deterministic |
| Human-approved intent quality/completeness/correctness | Never; prohibited |

Behavior-tests-to-documented-contract verification means semantic verification that retained behavior tests exercise the product/API/runtime contract described by the docs. It never means testing documentation files, documentation text, headings, links, formatting, examples, or other documentation content directly.

Optional advisory verification may exist, but optional verification must not block or pass gates unless a requirement in this table applies.

### 13.4 Configuration and health

Init or verifier config asks:

1. Configure backend verifier now
2. Leave disabled for now
3. Discuss

Only executable adapters may be presented as normal choices.

Command adapter config must collect:

- adapter kind,
- command,
- arguments,
- working directory behavior,
- timeout,
- environment/secret setup confirmation,
- provider/model fields when the adapter kind manages a model process.

The required first command adapter kind is `pi_headless_rpc`. It manages a local Pi RPC child process and defaults to:

```bash
pi --mode rpc --no-session --no-tools --provider openai-codex --model gpt-5.4-mini
```

The default provider/model is `openai-codex` / `gpt-5.4-mini`. Implementations must allow provider/model override. A non-thinking authenticated model such as `github-copilot` / `gpt-4.1` may be configured, but the adapter must work with thinking-capable models by filtering RPC events rather than relying on model choice.

Implemented HTTP adapter config must collect:

- endpoint,
- auth mechanism or credential environment variable names,
- timeout,
- data-sharing policy.

Implemented provider/model adapter config must collect:

- provider name,
- model name,
- credential environment variable name,
- timeout,
- data-sharing policy.

Secrets must not be stored directly.

Health check sends a minimal verification task and validates response shape. Health failure blocks required semantic verification.

Local command adapter protocol is normative:

1. Spec Guard executes the configured command with configured arguments and working directory.
2. The verifier task is written as one UTF-8 JSON object to stdin, followed by LF.
3. The adapter writes exactly one UTF-8 JSON verifier response object to stdout. Additional stdout after the first complete JSON object is invalid.
4. Stderr is diagnostic-only and must not be parsed as verifier output.
5. Exit code `0` means a response was produced and must still pass schema validation. Non-zero exit code means adapter failure and no gate is satisfied, even if stdout contains JSON.
6. Timeout terminates the adapter process, records verifier health failure for that run, and satisfies no gate.
7. The task JSON must include task id, schema version, submitted claim ids/text, deterministic evidence refs, human-approved refs, and prohibited judgment rules. The response JSON must use the schema in section 13.5.

Pi headless RPC command adapter protocol is normative for adapter kind `pi_headless_rpc`:

1. Start Pi as a managed child process with `pi --mode rpc --no-session --no-tools --provider <provider> --model <model>`.
2. Default `provider` is `openai-codex`; default `model` is `gpt-5.4-mini`.
3. Record process metadata under Spec Guard runtime storage and expose deterministic start/status/prompt/stop lifecycle controls.
4. Accept one prompt at a time. Concurrent prompts must fail with a deterministic busy error.
5. Send prompts to Pi RPC as strict JSONL using LF framing: `{ "type": "prompt", "message": "..." }`.
6. Collect only `message_update` events where `assistantMessageEvent.type` is `text_delta`; concatenate their `delta` strings until `agent_end`.
7. Ignore and never expose `thinking_start`, `thinking_delta`, `thinking_end`, encrypted thinking signatures, partial thinking content, raw event streams, or tool events in adapter output.
8. Return a compact JSON envelope with adapter id, Pi provider/model, final text, optional parsed JSON, diagnostics, and no hidden reasoning.
9. Health check sends a minimal prompt such as `Reply with only the answer, no explanation: 1+1?` and expects final text `2` before `agent_end`.
10. The adapter is advisory verification infrastructure only; it must not bypass Spec Guard human gates, deterministic checks, or approval semantics.

### 13.5 Task and response constraints

Verifier task input must separate:

- claim IDs and claim text,
- deterministic evidence,
- human-approved references as immutable constraints,
- prohibited judgment rules.

Verifier response must include:

- task id,
- schema version,
- status: `passed`, `failed`, or `inconclusive`,
- findings,
- verified claim IDs,
- unverified claim IDs,
- contradicted claim IDs,
- `prohibited_human_intent_judgment_detected` boolean.

Each finding must target one of:

- `agent_claim`,
- `evidence_mapping`,
- `deterministic_reference`,
- `human_approved_reference`.

A finding targeting `human_approved_reference` is valid only when it says an agent claim conflicts with, exceeds, or lacks support from that reference. It is invalid if it judges the human-approved reference itself as correct, incorrect, complete, incomplete, good, bad, advisable, or inadvisable.

Verifier status semantics are deterministic:

- `passed` means every submitted claim id is in `verified_claim_ids`, `unverified_claim_ids` and `contradicted_claim_ids` are empty, and no finding has severity `error`.
- `failed` means at least one submitted claim id is in `contradicted_claim_ids`, or an error finding reports that a required claim is false or unsupported by the provided deterministic evidence.
- `inconclusive` means at least one submitted claim id is in `unverified_claim_ids` and no submitted claim id is contradicted.

Verifier findings are structured for deterministic validation. The kernel must not parse free-text `message` to infer prohibited judgment. Instead, it validates `finding_kind`, `target_type`, and `prohibited_human_intent_judgment`: a finding targeting `human_approved_reference` is valid only with finding kind `claim_conflicts_with_reference`, `claim_exceeds_reference`, or `claim_unsupported_by_reference`; any finding kind `prohibited_human_intent_judgment` or boolean `prohibited_human_intent_judgment: true` makes the response invalid.

The deterministic kernel must mark a verifier response invalid when:

- required fields are missing,
- verified/unverified/contradicted claim ID sets are not pairwise disjoint,
- for `passed`, `failed`, or `inconclusive` responses, the union of verified, unverified, and contradicted claim IDs is not exactly the submitted claim ID set,
- invalid responses include verified, unverified, or contradicted claim IDs outside the submitted set,
- a claim is omitted from all three sets on a non-invalid response,
- an inconclusive claim is not listed in `unverified_claim_ids`,
- findings judge human-approved intent,
- response attempts to approve, reject, defer, change, or reinterpret human intent.

Invalid verifier responses do not satisfy gates. Appendix A defines the normative `VerifierTask` and `VerifierResponse` JSON object shapes for local command, HTTP, provider/model, and test-fixture adapters.

---

<a id="us-14-source"></a>
## 14. Runtime, Review, and Final Claims

> Derived user story: [US-14: Runtime evidence, review completion, and final claims](user-stories/14-runtime-review-final-claims.md)

### 14.1 Runtime evidence

Runtime evidence must distinguish:

- production runtime evidence,
- development runtime evidence.

Production claims require production evidence.

Development/HMR/full-stack development claims require development evidence for exact command and validated paths. If work requires frontend and backend processes for development use, evidence must show one documented command or orchestrated entry point starts the full required development runtime.

### 14.2 Review completion

Review completion requires, when applicable to the packet classification and evidence policy:

- implementation files, or an approved/not-applicable reason for documentation-only or other no-implementation paths,
- test files, or deterministic not-applicable evidence where tests are permitted to be not applicable,
- changed files from packet change baseline,
- AC verification,
- docs status,
- feature/source evidence status,
- cleanup status,
- test cleanup verification showing no unapproved files, database tables/rows, external resources, processes, or runtime state were left behind,
- runtime evidence where applicable,
- required backend verification records,
- final claim audit.

Review cannot complete while required traceability is empty or unsupported.

AC verification at review completion means each approved AC is either linked to passing governed evidence, linked to an approved deterministic not-applicable evidence record where not-applicable is permitted, or explicitly reported as unsupported so review completion blocks. For behavior/API/runtime ACs, evidence must include kernel-created command results and required backend verification. For operational-document documentation-only ACs, evidence must include docs/content records and required docs/content-to-AC verification.

### 14.3 Final claims

Final user-facing claims must be supported by recorded evidence or explicitly marked unverified.

Claims presented as verified, completed, implemented, working, tested, or validated require backend verification against evidence and approved references used only as immutable constraints.

Claims explicitly marked unverified do not require semantic support verification, but deterministic validation must ensure they are clearly labeled as unverified and are not used to satisfy review completion, AC verification, runtime validation, or implementation success. A final response may include unverified claims only as caveats or limitations.

The verifier must not criticize or reinterpret approved human intent.

---

<a id="us-15-source"></a>
## 15. CLI and MCP Requirements

> Derived user story: [US-15: CLI and MCP parity](user-stories/15-cli-mcp-requirements.md)

### 15.1 Shared action result

Every action result must match Appendix B:

- `ok`,
- `action_id`,
- `data`,
- `diagnostics`,
- `mutations`,
- `next_actions`,
- `summary`.

### 15.2 CLI

All shared actions must be available through CLI unless explicitly bootstrap-only.

CLI commands must not require agents to inspect Spec Guard source to discover valid workflow parameters.

`npx spec-guard init` is the normal bootstrap command and must optimize for human readability. On successful `init` with no explicit machine-readable flag, stdout must be plain text, not JSON. The plain text success output must include at least:

- that Spec Guard initialized successfully,
- artifact root path,
- generated MCP/client/Pi config file paths,
- immediate next steps for Pi reload/restart and MCP client reload,
- the recommended first tool calls such as status/quickstart.

`init` must still support an explicit machine-readable mode, such as `--json`, that returns the standard shared action result JSON for automation. Failed `init` attempts may return structured JSON diagnostics or clear plain-text diagnostics, but success with the default `npx spec-guard init` path must not require agents or humans to parse JSON.

### 15.3 MCP

Every non-bootstrap, non-local-runtime shared workflow action must have an MCP tool. MCP does not need an init command.

CLI-only exceptions are allowed for bootstrap actions and local runtime server actions:

- `init` is CLI-only bootstrap for creating local configuration and generated harness files.
- `serve.viewer` is CLI-only local runtime server startup.

CLI and MCP must call the shared core/action registry directly. MCP must not shell out to CLI, spawn CLI subprocesses, parse CLI output, or depend on CLI command behavior as its implementation path.

MCP tools must:

- use complete input schemas,
- return compact output by default,
- support full artifact opt-in,
- include next actions and suggested inputs sufficient for agents,
- expose verifier and baseline status through status/quickstart,
- describe the action in terms an agent can use without inspecting source,
- explicitly remind agents that human-gated actions require actual human confirmation fields,
- make the status/quickstart tools obvious as the first tools to call.

MCP tool names must be deterministic: `spec_guard_` plus action id with dots replaced by underscores.

The MCP server startup path generated by init must invoke the shared core directly. It must be a direct stdio server command, not a wrapper that shells out to ordinary CLI workflow commands or parses CLI output.

---

<a id="us-16-source"></a>
## 16. Agent Harness Configuration

> Derived user story: [US-16: Agent harness configuration](user-stories/16-agent-harness-configuration.md)

`spec-guard init` must generate best-effort agent and MCP configuration files in the project, not only in an internal artifact directory. The generated files must make MCP/Pi use obvious to agents and humans immediately after `npx spec-guard init`.

Required generated/support artifacts:

- generic project MCP config at `.mcp.json`,
- Claude Code project config/snippet compatible with `.mcp.json`,
- Claude Desktop snippet in the artifact harness directory for copy/paste when project-local config is unsupported,
- Cursor project config at `.cursor/mcp.json`,
- VS Code config at `.vscode/mcp.json` where supported,
- Cline config at `.cline/mcp.json` and `.cline/cline_mcp_settings.json` where supported,
- Roo config at `.roo/mcp.json` and `.roo/roo_mcp_settings.json` where supported,
- Windsurf config at `.windsurf/mcp.json` and `.windsurf/mcp_config.json` where supported,
- generic stdio snippets for other MCP clients where supported,
- project-local Pi extension at `.pi/extensions/spec-guard.ts`,
- Pi extension descriptor or snippet in the artifact harness directory,
- project-visible agent guide such as `SPEC_GUARD_AGENT_GUIDE.md`,
- MCP README/quickstart,
- client support matrix.

The project-local Pi extension is required. It must be placed at `.pi/extensions/spec-guard.ts` so Pi auto-discovers it on startup or `/reload`. It must register direct `spec_guard_*` tools for the shared workflow actions and must call the shared core/action registry directly rather than shelling out to CLI. Its tool descriptions or prompt guidelines must direct agents to use Spec Guard tools directly, call status/quickstart first, and provide actual human confirmation fields for human-gated actions.

The generated Pi extension must satisfy Pi's actual extension module contract. It must default-export a synchronous or asynchronous factory function accepting Pi's `ExtensionAPI` object, for example `export default function (pi: ExtensionAPI) { ... }`. The module must not be a tools-only export, a named-export-only module, or a file that requires an undocumented wrapper to load. Tool registration must happen from inside the default factory by calling `pi.registerTool(...)` for each direct `spec_guard_*` tool. The generated file must be loadable from `.pi/extensions/spec-guard.ts` by Pi's normal project-local extension discovery and reload path without a separate build step beyond Pi's documented TypeScript extension loading.

`init` tests must prove generated Pi extension loadability, not only text content. At minimum, tests must generate `.pi/extensions/spec-guard.ts`, load or import it through the same TypeScript execution path used for Pi extensions or an equivalent test loader, assert that the module's default export is a function, invoke that function with a minimal mock `ExtensionAPI`, and assert that expected `spec_guard_*` tools are registered. If a real Pi extension loader test is available in the environment, it is preferred and must assert that Pi does not report `Extension does not export a valid factory function`.

Generated guidance must state:

- use Spec Guard tools directly,
- do not substitute CLI for MCP except bootstrap/init guidance,
- do not inspect Spec Guard package/source internals for workflow parameters,
- human-confirmed fields require actual human responses,
- human-approved content is canonical intent,
- Discuss is non-mutating,
- binary gates remain Yes/No/Discuss after discussion,
- fixed binary decisions record option 1 or 2 only,
- non-binary custom choices require numbered confirmation,
- single packets use sequential AC, packet approval, and authorization gates,
- Plan batch approval applies only to eligible child packets,
- documentation itself is never tested and retained docs tests must be removed,
- tests must clean up files, data, processes, external resources, and runtime state,
- semantic agent claims require backend verification as specified.

---

<a id="us-17-source"></a>
## 17. Viewer Requirements

> Derived user story: [US-17: Viewer requirements](user-stories/17-viewer-requirements.md)

The viewer must be a real web application for artifact review and governance insight.

The viewer must use Mantine for styling, layout, and interaction states. The primary dashboard and review pages must be built from Mantine components or project-local wrappers around Mantine components, including dashboard shell/layout, metric cards, badges, tables/lists, buttons/links, and status colors. The viewer must not be an unstyled/plain HTML surface.

The viewer must be modeled after industry-standard dashboard patterns: an overview-first dashboard, a responsive metric-card grid, clear hierarchy, scannable labels and numbers, consistent spacing and typography, status badges, action-oriented visual emphasis, and drill-down navigation from summary metrics to the underlying records.

`serve.viewer` is a local runtime server action, not a URL formatter. It must create an actual HTTP server bound to the requested host and port, serve viewer routes over HTTP, and keep the CLI process alive until the server is explicitly closed or the process receives a termination signal such as Ctrl-C/SIGINT/SIGTERM. It must not print `Viewer running at ...` unless the server is listening successfully. If binding fails, it must return or print diagnostics and exit non-zero. Implementations may return a server handle from the internal `viewer.serve()` API, but the CLI command must await or otherwise retain that handle so the process does not exit immediately.

The viewer must read through the same shared core/artifact store used by CLI, MCP, and Pi. Viewer data must be derived from persisted Spec Guard artifacts under the configured artifact root, not from viewer-only fixtures, hard-coded empty objects, generated labels, or fake in-memory state except in explicitly isolated unit tests. After a workflow action persists or mutates an artifact, refreshing the viewer or calling the viewer summary action must reflect the persisted state.

The dashboard must show persisted artifact-derived metric cards for:

- total artifacts,
- total artifacts by artifact type,
- artifact counts by type/status,
- the number of artifacts in each workflow/lifecycle stage,
- pending human gates,
- blocked packets,
- runtime baseline status,
- verifier health,
- validation failures,
- runtime evidence status,
- final claim support status.

Each dashboard metric card that displays a count must be clickable. Activating a card must open or navigate to a filtered list of the exact artifacts represented by that count. The filtered list must show artifact identifiers, artifact type, lifecycle/status, pending action if any, last updated/revision where available, and a link to the artifact detail/review page. The number of rows in the filtered list must reconcile with the clicked card count, subject only to explicit pagination with a visible total count.

Metric cards for artifacts or states requiring user action, including pending human gates, blocked packets, stale approvals, verifier failures, validation failures, missing evidence, or review-ready items, must be visually distinct from passive informational cards. The distinction must use Mantine-supported styling such as color, variant, icon, badge, border, or callout treatment, and must remain visible without relying on color alone.

The dashboard summary data used by the viewer must also be available through a shared-core read path suitable for tests and agents. `config.check` must return more than `{ artifact_root, ok }`: it must include a persisted-artifact governance summary with at least total artifacts, artifact counts by type/status, lifecycle distribution, workflow-stage distribution, pending gates, blocked packets, baseline status, verifier health, validation failures, runtime evidence status, and final claim support status. These fields must be computed from real persisted artifacts. For example, after `work.intake` creates a draft Work Packet, `config.check` and the viewer dashboard must report the Work Packet in total artifacts, artifact counts, and lifecycle/workflow-stage distribution without requiring a fake viewer core.

Artifacts awaiting human gates must have human-readable review pages. Formatted JSON must not be the primary review surface.

Work Packet pages must show:

- status and lifecycle,
- goal and intent fields,
- ACs with source/evidence markers,
- AC approval state,
- platform choice,
- architecture decisions,
- classification and docs policy,
- allowed globs,
- runtime baseline status,
- packet change baseline,
- docs requirements,
- backend verification status/findings,
- pre-implementation validation status,
- failure/pass/runtime evidence,
- implementation/test files,
- changed files,
- final claim validation,
- diagnostics,
- next human decision,
- review snapshot hash.

Plan pages must show:

- Plan status,
- approved Plan proposal,
- child creation status,
- batch review snapshot when pending,
- per-child readiness,
- per-child approval/authorization binding.

Approval must bind to the hash shown in the viewer.

The viewer must clearly distinguish:

- human-approved intent,
- frontend-agent proposals,
- backend-verified claims,
- deterministic evidence.

---

<a id="us-18-source"></a>
## 18. Diagnostics

> Derived user story: [US-18: Diagnostics](user-stories/18-diagnostics.md)

Required diagnostic categories:

- missing Something else for non-binary semantic choice,
- missing Discuss option,
- custom non-binary choice awaiting numbered confirmation,
- binary gate discussion must re-prompt Yes/No/Discuss,
- fixed binary decision includes Something else/custom option,
- AC approval required,
- AC review snapshot missing or stale,
- AC reviewed payload hash mismatch,
- AC refinement attempted artifact mutation,
- source-derived AC missing source/evidence,
- batch attempted to approve source-derived AC,
- runtime baseline missing,
- runtime baseline not accepted,
- runtime baseline validation failed,
- runtime baseline acceptance stale,
- packet change baseline missing,
- dirty implementation source at authorization,
- changed files outside allowed globs,
- implementation source changed before failure-first evidence,
- classification invalid,
- docs policy invalid,
- update touched approved fields and invalidated approvals,
- protected approved-field update rejected,
- API/contract-surface docs policy not required,
- docs required but missing,
- docs-to-AC verification required,
- docs-updated verification required,
- behavior-tests-to-documented-contract verification required,
- tests-to-AC verification required,
- retained docs test detected,
- test cleanup side effect detected,
- operational-document not-applicable validation missing,
- not-applicable evidence lacks deterministic eligibility,
- operational-document docs policy invalid,
- failure evidence semantic verification required,
- verifier disabled,
- verifier adapter unavailable,
- verifier misconfigured,
- verifier health check failed,
- verifier response invalid,
- verifier attempted to judge human-approved intent,
- required backend verification claim missing or unregistered,
- Plan-vs-single choice required,
- Plan approval required,
- Plan proposal payload hash mismatch,
- Plan approval attempted to create children directly,
- review snapshot producer output missing,
- snapshot payload mismatch,
- stale source revision for ephemeral snapshot,
- batch review snapshot missing or stale,
- batch source artifact refs missing or not derivable,
- batch audit revision missing,
- batch proposed children payload mismatch,
- batch child snapshot binding missing,
- batch child snapshot revision invalid,
- batch proceed approved post-action result field,
- batch proceed approved payload reference missing,
- ambiguous proposed child id in batch snapshot revision,
- batch child created payload mismatch,
- batch child approval-relevant payload mismatch,
- batch child expected revision missing,
- Plan proposed child id invalid for batch snapshot revision,
- batch child Plan slice mapping missing or invalid,
- batch child Plan slice correspondence mismatch,
- batch child title correspondence mismatch,
- batch child source evidence summary mismatch,
- batch child source artifact refs missing or inconsistent,
- source artifact refs not in canonical order,
- source artifact ref unresolved,
- source artifact content hash mismatch,
- source-derived AC SourceEvidence refs missing,
- source evidence hash mismatch,
- batch child proposed WorkPacket payload missing,
- batch child change baseline capture failed,
- proposed authorization snapshot payload invalid,
- authorization snapshot missing approved packet hash,
- approved fields missing,
- approved payload missing for registered decision type,
- declined decision incorrectly supplied approved payload,
- decision mutation prohibited,
- Plan approved-field update rejected,
- ready child packet preconditions missing,
- Work Packet approval missing,
- implementation authorization missing,
- pre-implementation validation required,
- review traceability missing,
- command result missing for command-backed evidence,
- command result execution context missing,
- command result status incompatible with evidence type,
- command result purpose incompatible with evidence type,
- caller-supplied command status rejected,
- final claim unsupported,
- approval hash stale,
- CLI/MCP parity missing.

---

<a id="us-19-source"></a>
## 19. Tests First Plan

> Derived user story: [US-19: Tests-first coverage plan](user-stories/19-tests-first-plan.md)

Tests must cover these behaviors before implementation.

### 19.1 Choice and authority

- Human-owned decisions route to human gates.
- Discuss mutates nothing and creates no HumanDecision.
- Numbered No records decline/block decisions with empty approved fields and no approved payload.
- Binary gates remain Yes/No/Discuss after discussion.
- Fixed binary decisions have exactly two outcomes plus Discuss.
- Non-binary custom choices require numbered confirmation.
- Backend verifier cannot approve, reject, or judge human intent.

### 19.2 Decision binding

- Every review-bound gate has a non-mutating snapshot producer.
- Review snapshot hash is deterministic.
- Human decisions record approved fields.
- Standard actions derive approved fields by decision type.
- Supersession backlink updates are metadata-only and do not alter decision substance.
- Durable decision histories retain superseded Work Packet and Plan decisions.
- Plan-vs-single, platform, and architecture choices have registered decision types and approved payloads for final selections.
- Unconfirmed custom choices and Discuss do not record final platform or architecture decisions.
- Registered decision types rooted in HumanDecision.approved_payload require canonical approved payloads on final selecting decisions.
- Authorization decisions store the canonical AuthorizationReviewSnapshotPayload as approved payload for later invalidation.
- Plan approval approved fields are rooted in PlanProposalPayload and do not include the Plan approval decision itself.
- Changing an approved field invalidates dependent approvals.
- Generic update actions reject protected approved-field changes or list deterministic approval invalidations.
- Batch proceed stores batch snapshot, pre-decision BatchProceedSelectionPayload, post-action BatchProceedResult, and per-child snapshot bindings.
- Batch proceed approved fields bind only to pre-decision selection fields and not post-action result fields.
- Batch proceed HumanDecision uses approved_payload_ref to reference BatchProceedRecord selection payload rather than requiring duplicated approved payload.
- Batch proceed HumanDecision stores review snapshot fields, parent batch snapshot fields, and source artifact refs from the persisted BatchReviewSnapshot.
- Batch proceed option 1 records a one-at-a-time BatchProceedRecord with per-proposed-child result rows containing null/false result fields.
- Persisting a batch snapshot is an audit-only mutation and does not mutate governed state or increment governed Plan revision.
- Persisted snapshots and batch snapshots use audit revisions separate from governed artifact revisions.
- Non-batch persisted snapshots are created only through audit-only snapshot persistence, not normal review producers.
- Stale batch snapshot blocks batch mutation.
- Ephemeral snapshots become stale when source artifact revisions no longer match.

### 19.3 AC and approval flow

- Single Work Packet path requires AC approval before Work Packet approval.
- Single Work Packet path has no combined AC+packet gate.
- AC Discuss refinement writes no artifacts until Yes or No.
- `work.ac.review` can hash a supplied refined AC payload without mutating artifacts.
- `work.ac.approve` rejects reviewed AC payloads that do not match the supplied snapshot hash.
- Source-derived ACs are displayed with source/evidence and approved through the AC gate.
- Source-derived ACs are excluded from Plan batch approval and batch authorization.
- Plan batch approval can approve only explicitly displayed eligible non-source-derived child ACs/packets.
- Source-derived children have nullable batch authorization hashes and are excluded from batch authorization.
- Plan proposal slice ids and proposed child ids reject values that cannot be used in batch child snapshot revisions.
- Batch snapshots store expected created Work Packet revision for every proposed child, independent of authorization eligibility.
- ProposedChildrenPayload contains the canonical ProposedWorkPacketPayload used for child snapshots and optional shorthand fields are validation mirrors only.
- Proposed child payload equality excludes generated, audit, runtime, evidence, diagnostic, lifecycle-history, and timestamp fields.
- BatchReviewSnapshot source artifact refs are derived from the approved Plan, proposed children payload refs, and AC SourceEvidence refs.
- Batch child correspondence enforces the same approved Plan slice constraints as one-at-a-time child creation.
- Proposed children explicitly map to approved Plan slices through plan_slice_id and created WorkPackets durably store plan_slice_id.
- WorkPacket and ProposedWorkPacketPayload include canonical title for Plan child correspondence.
- ProposedWorkPacketPayload carries source evidence summary for exact Plan-slice string comparison when applicable.
- Source-derived AC evidence uses structured SourceArtifactRefs and source evidence hashes rather than free-form summary matching.
- SourceArtifactRef arrays are canonicalized by tuple identity and deterministic ordering before hashing.
- SourceArtifact registration creates immutable, content-addressed revisions that SourceArtifactRefs can resolve.
- Source evidence kinds and source artifact types are open strings and are not restricted to a finite list of file types.
- Batch AC/packet approvals require exact created-child approval-relevant payload and revision match against the ProposedWorkPacketPayload projection used for snapshots.
- Proposed child authorization snapshots use ProposedAuthorizationReviewSnapshotPayload with expected created revision semantics.
- Child-specific batch snapshot revisions use the exact batch-child revision format and reject ambiguous proposed child ids.
- Batch proceed result records child snapshot hashes and revisions for approvals/authorizations actually recorded.
- Non-batch Plan children use sequential gates.
- Plan proposals do not create draft Plan artifacts; Plan artifacts are created only by Plan approval.
- `plan.update` rejects changes to Plan-approved fields unless a registered Plan amendment flow exists.

### 19.4 Runtime and change baselines

- Runtime baseline acceptance requires human Yes and deterministic validation.
- Runtime baseline is not used as diff base.
- Packet change baseline is captured at authorization.
- VCS and manifest modes compute changed files.
- Dirty implementation source at authorization blocks unless resolved.
- Implementation source before failure-first blocks validation.

### 19.5 Classification and docs

- Classification enum is enforced.
- `reusable_api`, `rest_api`, and `reusable_ui` always require docs policy `required`.
- Human cannot override docs away for API/contract-surface packets.
- Non-API docs policies behave as specified.
- Non-API packets with docs policy `required` follow docs before tests before failure evidence before implementation.
- Operational-document packets require docs/content policy `required`.
- Operational-document packets can mark tests/failure-first not applicable only when no product behavior changes.
- Documentation itself is never tested; retained docs tests block review.
- Docs-updated claims are required and passed before review completion when docs are required, docs policy is `changed`, docs files changed, or docs policy changed.
- Docs policy `changed` requires docs-updated verification before review completion without a later semantic documented-behavior-changed judgment.
- Direct docs/content file changes without docs evidence register or expose missing docs-updated claims and block review.

### 19.6 Backend verification

- Required verification matrix is enforced.
- Disabled/misconfigured verifier blocks required semantic checks.
- Command adapter is executable and health-checkable.
- Optional adapters are not selectable unless executable.
- Invalid verifier responses do not satisfy gates.
- Human-intent judgments in verifier findings are invalid.

### 19.7 Pre-implementation and review

- API/contract-surface chain enforces docs before tests before failure evidence before implementation.
- Non-API docs-required chain enforces docs before tests before failure evidence before implementation.
- Non-API docs-not-required chain enforces tests before failure evidence before implementation.
- Operational-document docs-only chain enforces docs/content validation and no product source changes.
- Failure evidence semantic verification is required when failure is used to prove missing approved behavior.
- Allowed globs apply to product-scope files and exempt Spec Guard artifacts/evidence from blocking.
- Approval and authorization can occur before docs/tests/failure-first.
- Implementation source cannot change until implementation-ready.
- Tests must clean up files, database tables/rows, external resources, processes, and runtime state.
- Command-backed evidence references kernel-created CommandResult records and never trusts caller-supplied exit codes or command status.
- CommandResult records include execution context and durable storage references.
- Evidence actions map timed out and skipped command results to inconclusive and do not use them to satisfy required evidence gates.
- Evidence actions reject CommandResults with incompatible purpose.
- Review requires traceability, cleanup verification, and required backend verification.
- Cleanup evidence action records checked resources and side-effect status.
- Not-applicable evidence action records tests/failure-first not-applicable reasons only with deterministic eligibility. Human confirmation, when collected, only acknowledges the eligible determination.
- Batch authorization readiness is evaluated against proposed child payloads and snapshot bindings.
- Batch authorization captures PacketChangeBaseline per authorized child or leaves that child unauthorized with diagnostics.
- Final claims require support or explicit unverified labeling; unverified claims cannot satisfy review completion.

### 19.8 CLI/MCP/viewer

- Every shared workflow action has CLI and MCP mapping unless bootstrap-only or local-runtime-only.
- Human-gated actions require selected number, raw response, decision prompt, and human confirmation.
- Review-bound approval actions require review snapshot hash, revision, and source artifact refs when using ephemeral snapshots.
- `work.plan_choice.answer` records the registered Plan-vs-single fixed decision.
- `plan.propose` hashes a complete Plan proposal payload.
- `plan.approve` rejects Plan proposal payloads that do not match the supplied snapshot hash.
- Plan approval and batch proceed have concrete shared actions.
- `command.run` creates deterministic CommandResult records used by command-backed evidence.
- `plan.batch_snapshot.create` requires proposed children payload and records only an audit snapshot.
- `plan.child.create` creates one child only when tied to an approved Plan proposal/slice and matching child constraints, with proposed_child_id equal to plan_slice_id.
- Evidence actions register or reference stable claims for required backend verification.
- Human decisions cannot be patched; supersession is append-only.
- MCP calls shared core directly and never shells out to CLI.
- `npx spec-guard init` successful default output is plain text, includes generated file paths and next steps, and is not parseable as JSON.
- `npx spec-guard init --json` returns the standard shared action result JSON.
- Init writes project-visible MCP configs for generic/Claude, Cursor, VS Code, Cline, Roo, and Windsurf clients.
- Init writes `.pi/extensions/spec-guard.ts`, and Pi discovers direct `spec_guard_*` tools after startup or `/reload`.
- The generated Pi extension module is loadable by Pi's factory contract: importing/loading the generated file yields a default-exported factory function, invoking the factory with a mock or real `ExtensionAPI` registers expected `spec_guard_*` tools, and no tools-only or named-export-only extension is accepted.
- Generated MCP/Pi tool descriptions make status/quickstart and human-gated fields obvious without source inspection.
- Action result schema is consistent.
- `serve.viewer` starts a real listening HTTP server on the requested host/port, returns a successful HTTP response for the dashboard, and keeps the CLI process/server alive until explicitly terminated.
- Viewer renders human-readable approval pages with hashes.
- Viewer uses Mantine components/theme or Mantine-backed project wrappers for dashboard/review layout, cards, badges, tables/lists, buttons/links, and action states.
- Viewer dashboard follows industry-standard dashboard layout patterns with an overview-first responsive metric-card grid, clear status hierarchy, and drill-down navigation.
- Viewer dashboard exposes full artifact metric cards for total artifacts, totals by artifact type, counts by type/status, workflow-stage counts, baseline, verifier, pending gates, blocked state, validation failures, runtime evidence, and final claim support.
- Each dashboard count card is clickable and opens a filtered artifact list whose visible total/row count matches the card count, with artifact identifiers, type, status/stage, pending action where applicable, and detail/review links.
- Cards requiring user action are visually distinct from passive informational cards using Mantine-supported non-color-only emphasis.
- Viewer dashboard and `config.check` derive their summary from persisted artifacts: a test must create a real artifact through a shared workflow action such as `work.intake`, then assert total artifact counts, artifact counts by type, lifecycle/workflow-stage counts, and pending-gate summary changes without using fake viewer data.

---

<a id="us-20-source"></a>
## 20. Migration

> Derived user story: [US-20: Migration](user-stories/20-migration.md)

When reading existing artifacts, Spec Guard must:

- migrate known synonymous fields into canonical fields,
- preserve raw legacy values where useful,
- reject future writes that omit required canonical fields,
- warn on boilerplate generated scope without silently deleting it,
- reconstruct parent/child links when possible,
- leave optional intent fields empty unless drafted,
- never fabricate human decisions,
- never fabricate backend verification records,
- invalidate approvals when migration changes approved semantics.

Migration must not create verifier records that judge human-approved content.

---

<a id="us-21-source"></a>
## 21. Non-Goals

> Derived user story: [US-21: Non-goals and boundaries](user-stories/21-non-goals.md)

This specification does not require:

- prompting every non-AC intent field separately,
- making users/actors/edge-cases mandatory,
- letting backend verifier generate product scope,
- letting backend verifier make decisions,
- using backend verifier to judge approved human intent,
- using backend verifier for Plan-vs-single or Plan approval,
- replacing deterministic validation with model judgment,
- choosing a single model vendor,
- storing secrets directly,
- exposing Spec Guard internals to frontend agents.

---

<a id="us-22-source"></a>
## 22. Success Criteria

> Derived user story: [US-22: Redesign success criteria](user-stories/22-success-criteria.md)

The redesign succeeds when:

1. An implementation agent can implement from this document alone.
2. Every governed question routes to the correct authority.
3. Human-approved intent is canonical and not judged by the backend verifier.
4. Choice, binary gate, and fixed binary decision semantics are consistent.
5. Approval records bind to review snapshots and approved fields.
6. Single packets use sequential AC approval, packet approval, and authorization gates.
7. Plan child batch acceleration is explicit, per-child bound, and limited to eligible children.
8. Runtime baseline and packet change baseline are distinct and operational.
9. Implementation boundary is enforceable.
10. API/contract-surface docs are always required for reusable API, REST API, and reusable UI work.
11. Backend verification requirements are deterministic.
12. Artifact schemas, embedded record schemas, hashes, action inputs, CLI, and MCP contracts are concrete enough to implement.
13. Viewer supports human-readable review and governance insight.

---

<a id="us-23-source"></a>
# Appendix A. Normative Schemas

> Derived user story: [US-23: Normative schemas](user-stories/23-normative-schemas.md)

The schemas below are normative field contracts. Implementations may add fields only if they do not weaken required behavior.

## A.1 Common top-level artifact fields

```json
{
  "artifact_type": "string",
  "schema_version": "integer",
  "id": "string | absent for singleton",
  "revision": "integer",
  "created_at": "timestamp",
  "updated_at": "timestamp",
  "diagnostics": "Diagnostic[]"
}
```

## A.2 Diagnostic

```json
{
  "code": "string",
  "severity": "error | warning | info",
  "message": "string",
  "field_path": "string | null",
  "gate": "string | null",
  "fix": "string | null"
}
```

## A.3 HumanDecision embedded record

```json
{
  "id": "string",
  "decision_type": "string",
  "prompt_id": "string",
  "prompt_text": "string",
  "raw_response": "string",
  "selected_number": "integer",
  "normalized_decision": "string",
  "approved_fields": "string[]",
  "custom_response": "string | null",
  "supersedes_decision_id": "string | null",
  "superseded_by_decision_id": "string | null; metadata-only backlink may be filled after supersession",
  "review_snapshot_hash": "string | null",
  "review_snapshot_revision": "string | null",
  "source_artifact_refs": "SourceArtifactRef[]",
  "approved_payload_hash": "string | null; required for final approving/selecting decisions when approved-field root is not otherwise durable except plan_batch_proceed",
  "approved_payload_revision": "string | null; required for final approving/selecting decisions when approved-field root is not otherwise durable except plan_batch_proceed",
  "approved_payload": "object | null; required for final approving/selecting decisions when approved-field root is not otherwise durable except plan_batch_proceed",
  "approved_payload_ref": "ApprovedPayloadRef | null; required for plan_batch_proceed and batch child AC/packet approvals when the approved payload is stored in a sibling batch record",
  "reviewed_payload_hash": "string | null; optional audit copy for declined/blocked review-bound decisions",
  "reviewed_payload_revision": "string | null; optional audit copy for declined/blocked review-bound decisions",
  "reviewed_payload": "object | null; optional audit copy for declined/blocked review-bound decisions",
  "target_artifact_revision": "integer | null; required for batch child decisions and records the created child revision observed when the decision was recorded",
  "parent_batch_snapshot_hash": "string | null",
  "parent_batch_snapshot_revision": "string | null",
  "source_interface": "string",
  "human_confirmed": "boolean",
  "at": "timestamp"
}
```

## A.4 Config top-level artifact

```json
{
  "artifact_type": "config",
  "schema_version": 1,
  "revision": "integer",
  "created_at": "timestamp",
  "updated_at": "timestamp",
  "project_id": "string",
  "artifact_root": "string",
  "project_root": "string",
  "command_execution": {
    "default_mode": "argv | shell",
    "configured_shell": "string | null",
    "default_timeout_ms": "integer",
    "env_policy": "inherit | clean | configured"
  },
  "path_policy": "PathPolicy",
  "change_baseline_policy": "ChangeBaselinePolicy",
  "cleanup_observers": "CleanupObserver[]",
  "diagnostics": "Diagnostic[]"
}
```

PathPolicy:

```json
{
  "spec_guard_artifact_evidence": "string[]",
  "docs": "string[]",
  "tests": "string[]",
  "implementation_source": "string[]",
  "runtime_product_configuration": "string[]",
  "generated_build_output": "string[]",
  "docs_test_manifests": "string[]",
  "ignored_paths": "string[]"
}
```

ChangeBaselinePolicy:

```json
{
  "mode": "auto | vcs | manifest"
}
```

CleanupObserver:

```json
{
  "resource_category": "string",
  "identity_fields": "string[]",
  "before_command_spec": "CommandSpec | null",
  "after_command_spec": "CommandSpec | null",
  "deterministic_capture": "files | processes | null",
  "comparison_rule": "exact_match | no_new_resources | custom_command_exit_zero"
}
```

## A.5 VerifierConfig top-level artifact

```json
{
  "artifact_type": "verifier_config",
  "schema_version": 1,
  "revision": "integer",
  "created_at": "timestamp",
  "updated_at": "timestamp",
  "mode": "disabled | local_command | http | provider_model | test_fixture",
  "adapter_config": "object; shape determined by mode and section 13.4",
  "health": {
    "status": "healthy | unhealthy | unknown",
    "checked_at": "timestamp | null",
    "diagnostics": "Diagnostic[]"
  },
  "diagnostics": "Diagnostic[]"
}
```

## A.6 RuntimeBaseline top-level artifact

```json
{
  "artifact_type": "runtime_baseline",
  "schema_version": 1,
  "revision": "integer",
  "created_at": "timestamp",
  "updated_at": "timestamp",
  "status": "draft | accepted | blocked",
  "stack": {
    "product_platform": "string | null",
    "runtime": "string | null",
    "language": "string | null",
    "package_manager": "string | null",
    "framework": "string | null",
    "build_tool": "string | null",
    "architecture": "string | null"
  },
  "commands": {
    "test": "CommandSpec | null",
    "test_not_applicable_reason": "string | null",
    "build": "CommandSpec | null",
    "build_not_applicable_reason": "string | null",
    "runtime_production": "CommandSpec | null",
    "runtime_production_not_applicable_reason": "string | null",
    "runtime_development": "CommandSpec | null",
    "runtime_development_not_applicable_reason": "string | null"
  },
  "configuration": {
    "environment_strategy": "string | null",
    "required_env_vars": "string[]",
    "greenfield_scaffold": "boolean"
  },
  "dependency_modes": {
    "install_mode": "string | null",
    "external_services": "string | null"
  },
  "diff_policy": {
    "dependency_changes_require_approval": "boolean",
    "include_untracked": "boolean"
  },
  "validation": {
    "command_results": "CommandResult[]",
    "diagnostics": "Diagnostic[]"
  },
  "acceptance": "HumanDecision | null; current active acceptance convenience slot; non-null only when status is accepted",
  "decision_history": "HumanDecision[]; append-only durable decision log for runtime baseline decisions",
  "blocker": "Blocker | null; non-null only when status is blocked"
}
```

## A.7 PacketChangeBaseline embedded record

```json
{
  "mode": "vcs | manifest",
  "captured_at": "timestamp",
  "work_id": "string",
  "artifact_revision": "integer; WorkPacket revision immediately after authorization decision and PacketChangeBaseline storage are atomically committed",
  "artifact_hash": "string; governed WorkPacket content hash at artifact_revision excluding change_baseline.artifact_hash and audit-only appendices",
  "review_snapshot_hash": "string",
  "allowed_globs": "string[]",
  "ignored_paths": "string[]",
  "vcs": "VcsChangeBaseline | null; required when mode is vcs and absent/null otherwise",
  "manifest": "ManifestChangeBaseline | null; required when mode is manifest and absent/null otherwise"
}
```

VcsChangeBaseline:

```json
{
  "system": "string",
  "commit": "string | null",
  "tree": "string | null",
  "dirty_files": "string[]",
  "untracked_files": "string[]",
  "preauthorization_dirty_entries": "PreauthorizationDirtyEntry[]; allowed dirty docs/tests/evidence baseline entries"
}
```

ManifestChangeBaseline:

```json
{
  "manifest_hash": "string",
  "files": [
    { "path": "string", "size": "integer", "mtime": "timestamp", "content_hash": "string" }
  ]
}
```

## A.8 WorkPacket top-level artifact

```json
{
  "artifact_type": "work_packet",
  "schema_version": 1,
  "id": "string",
  "revision": "integer",
  "created_at": "timestamp",
  "updated_at": "timestamp",
  "status": "WorkStatus",
  "title": "string",
  "classification": "WorkClassification",
  "parent_plan_id": "string | null",
  "plan_slice_id": "string | null; required when parent_plan_id is non-null",
  "intent": {
    "goal": "string",
    "desired_outcomes": "string[]",
    "in_scope": "string[]",
    "out_of_scope": "string[]",
    "users_actors": "string[]",
    "edge_cases": "string[]",
    "open_questions": "string[]"
  },
  "acceptance_criteria": "AcceptanceCriterion[]",
  "docs": {
    "policy": "required | changed | none_required | not_applicable",
    "none_required_reason": "string | null; required when policy is none_required",
    "not_applicable_reason": "string | null",
    "requirements": "DocsRequirement[]",
    "records": "EvidenceRecord[]"
  },
  "scope": {
    "allowed_globs": "string[]",
    "deviations": "string[]"
  },
  "platform": {
    "required": "boolean",
    "choice": "string | null",
    "decision_id": "string | null",
    "not_required_reason": "string | null"
  },
  "architecture": {
    "required": "boolean",
    "required_reason": "string | null",
    "not_required_reason": "string | null",
    "decision_ids": "string[]"
  },
  "runtime_baseline_ref": "RuntimeBaselineRef | null; required for packet approval readiness and may be null in draft",
  "change_baseline": "PacketChangeBaseline | null",
  "lifecycle": {
    "ac_approval": "HumanDecision | null; current active decision convenience slot",
    "packet_approval": "HumanDecision | null; current active decision convenience slot",
    "authorization": "HumanDecision | null; current active decision convenience slot",
    "history": "LifecycleEvent[]"
  },
  "decision_history": "HumanDecision[]; append-only durable decision log for this Work Packet",
  "evidence": "EvidenceRecord[]",
  "claims": "Claim[]; canonical claim registry for this Work Packet",
  "backend_verifications": "BackendVerification[]",
  "review": {
    "implementation_files": "string[]",
    "test_files": "string[]",
    "changed_files": "ChangedFile[]",
    "ac_verification": "object",
    "claims": "Claim[]; review/final claim subset copied or referenced from top-level claims registry",
    "complete": "boolean"
  },
  "diagnostics": "Diagnostic[]"
}
```

## A.9 Plan top-level artifact

```json
{
  "artifact_type": "plan",
  "schema_version": 1,
  "id": "string",
  "title": "string",
  "revision": "integer",
  "created_at": "timestamp",
  "updated_at": "timestamp",
  "status": "PlanStatus",
  "implements": false,
  "goal": "string",
  "source_work_id": "string | null",
  "product_context": {
    "platform_choice": "string | null",
    "platform_decision_id": "string | null",
    "architecture_decision_ids": "string[]",
    "source_request_summary": "string | null",
    "source_evidence_summary": "string | null"
  },
  "plan_proposal": {
    "title": "string",
    "goal": "string",
    "source_work_id": "string | null; same value as Plan.source_work_id",
    "product_context": "ProductContext",
    "summary": "string",
    "source_artifact_refs": "SourceArtifactRef[]; same canonical array approved in PlanProposalPayload",
    "slices": [
      {
        "proposed_id": "string; must match ^[A-Za-z0-9._-]+$",
        "title": "string",
        "goal": "string",
        "desired_outcomes": "string[]",
        "in_scope": "string[]",
        "out_of_scope": "string[]",
        "users_actors": "string[]",
        "edge_cases": "string[]",
        "open_questions": "string[]",
        "ac_ids": "string[]; derived from acceptance_criteria ids and must match them",
        "acceptance_criteria": "AcceptanceCriterion[]; full payloads required for every Plan slice",
        "classification": "WorkClassification",
        "docs_policy": "DocsPolicy",
        "docs_none_required_reason": "string | null; required when docs_policy is none_required",
        "docs_not_applicable_reason": "string | null; required when docs_policy is not_applicable",
        "allowed_globs": "string[]",
        "contains_source_derived_acs": "boolean",
        "source_evidence_summary": "string | null"
      }
    ]
  },
  "approval": "HumanDecision; current active Plan approval convenience slot",
  "decision_history": "HumanDecision[]; append-only durable decision log for this Plan",
  "batch_review_snapshots": "BatchReviewSnapshot[]; audit-only records that do not increment governed Plan revision",
  "batch_proceed_records": "BatchProceedRecord[]; batch decision records that do not alter approved Plan proposal fields",
  "child_work_ids": "string[]",
  "diagnostics": "Diagnostic[]"
}
```

## A.10 EvidenceRecord embedded record

```json
{
  "id": "string",
  "type": "docs | test_failure | test_pass | runtime_production | runtime_development | cleanup | not_applicable | review_trace | final_claim_support",
  "created_at": "timestamp",
  "command": "string | null; derived from CommandResult for command-backed evidence",
  "exit_code": "integer | null; derived from CommandResult for command-backed evidence",
  "status": "passed | failed | inconclusive | not_applicable; derived from CommandResult for command-backed evidence",
  "paths": "string[]",
  "related_ac_ids": "string[]",
  "related_doc_ids": "string[]",
  "resource_categories": "string[]; structured cleanup/runtime resource category strings, empty when not applicable",
  "command_result_ref": "string | null; required for test_failure, test_pass, runtime_production, and runtime_development",
  "evidence_role": "docs | behavior_test | failure_first | passing_test | runtime | cleanup | not_applicable | review",
  "file_state_snapshot": "FileStateSnapshot | null; kernel-captured at evidence action time",
  "summary": "string",
  "output_ref": "string | null",
  "docs_content_tokens": "DocsContentTokens | null; populated for docs EvidenceRecords",
  "cleanup": "CleanupEvidence | null",
  "not_applicable": "NotApplicableEvidence | null",
  "source_interface": "string"
}
```

## A.11 BackendVerification embedded record

```json
{
  "id": "string",
  "task_id": "string",
  "verifier_schema_version": "integer",
  "task_type": "string",
  "adapter": { "mode": "string", "metadata": "object" },
  "claims": "Claim[]",
  "evidence_refs": "string[]",
  "human_approved_refs": "object[]",
  "schema_status": "valid | invalid",
  "status": "passed | failed | inconclusive | invalid",
  "findings": "VerifierFinding[]",
  "verified_claim_ids": "string[]",
  "unverified_claim_ids": "string[]",
  "contradicted_claim_ids": "string[]",
  "prohibited_human_intent_judgment_detected": "boolean",
  "input_hash": "string",
  "result_hash": "string",
  "created_at": "timestamp"
}
```

## A.12 BatchReviewSnapshot embedded record

```json
{
  "id": "string",
  "plan_id": "string",
  "plan_revision": "integer",
  "plan_proposal_hash": "string",
  "plan_proposal_snapshot_revision": "string",
  "source_artifact_refs": "SourceArtifactRef[]; includes the approved Plan revision and any source artifacts used to produce proposed children",
  "proposed_children_payload": "ProposedChildrenPayload",
  "proposed_children_payload_hash": "string",
  "proposed_children_payload_snapshot_revision": "string",
  "prompt_text": "string",
  "options": "string[]",
  "snapshot_hash": "string",
  "snapshot_revision": "string",
  "audit_revision": "integer; monotonic audit sequence used in snapshot_revision and separate from Plan revision",
  "created_at": "timestamp",
  "children": [
    {
      "plan_slice_id": "string; must match an approved Plan slice proposed_id",
      "proposed_child_id": "string; must match ^[A-Za-z0-9._-]+$ and equal plan_slice_id",
      "expected_created_work_packet_revision": "integer",
      "proposed_work_payload": "ProposedWorkPacketPayload",
      "proposed_work_payload_hash": "string",
      "proposed_work_payload_revision": "string; exactly payload:<proposed_work_payload_hash>",
      "contains_source_derived_acs": "boolean",
      "source_artifact_refs": "SourceArtifactRef[]; child-level snapshot provenance refs plus AC SourceEvidence refs",
      "ac_review_snapshot": "ReviewSnapshot",
      "packet_review_snapshot": "ReviewSnapshot",
      "authorization_review_snapshot": "ReviewSnapshot | null; non-null only when batch_authorization_eligible is true and payload is ProposedAuthorizationReviewSnapshotPayload",
      "ac_snapshot_hash": "string",
      "ac_snapshot_revision": "string",
      "packet_snapshot_hash": "string",
      "packet_snapshot_revision": "string",
      "authorization_snapshot_hash": "string | null; non-null only when batch_authorization_eligible is true",
      "authorization_snapshot_revision": "string | null; non-null only when batch_authorization_eligible is true",
      "batch_approval_eligible": "boolean",
      "batch_authorization_eligible": "boolean",
      "ineligibility_reasons": "string[]",
      "readiness": {
        "ac_approval_ready": "boolean",
        "packet_approval_ready": "boolean",
        "batch_authorization_ready": "boolean",
        "diagnostics": "Diagnostic[]"
      }
    }
  ]
}
```

## A.13 Supporting embedded types

SourceArtifact top-level or standalone record:

```json
{
  "artifact_type": "source_artifact",
  "schema_version": 1,
  "id": "string",
  "revision": "integer",
  "created_at": "timestamp",
  "updated_at": "timestamp",
  "kind": "string; open string, not a closed enum",
  "label": "string",
  "locator": "string | null; path, URI, design id, or human-readable locator when applicable",
  "content_ref": "string; immutable blob/store reference or descriptor reference used to re-present reviewed material",
  "content_hash": "string; SHA-256 over captured bytes or canonical descriptor bytes",
  "descriptor": "object | null; deterministic metadata and retrieval details for descriptor material, null for captured bytes",
  "captured_at": "timestamp",
  "source_interface": "string",
  "diagnostics": "Diagnostic[]"
}
```

A SourceArtifact revision is immutable. Updating source material creates a new revision with a new `content_hash`; prior revisions remain addressable for staleness checks.

SourceArtifactRegisterInput:

```json
{
  "kind": "string",
  "label": "string",
  "locator": "string | null",
  "content_bytes_base64": "string | null; mutually exclusive with descriptor",
  "descriptor": "object | null; mutually exclusive with content_bytes_base64",
  "content_hash": "string | null; optional for descriptor and must match canonical descriptor hash when supplied",
  "source_interface": "string"
}
```

SourceArtifactUpdateInput:

```json
{
  "id": "string",
  "kind": "string | absent; absent inherits prior revision",
  "label": "string | absent; absent inherits prior revision",
  "locator": "string | null | absent; absent inherits prior revision, null clears",
  "content_bytes_base64": "string | null; mutually exclusive with descriptor",
  "descriptor": "object | null; mutually exclusive with content_bytes_base64",
  "content_hash": "string | null; optional for descriptor and must match canonical descriptor hash when supplied",
  "source_interface": "string"
}
```

SourceArtifactRef:

```json
{
  "artifact_type": "string; open string, not a closed enum; use source_artifact for SourceArtifact records and exact artifact_type for built-in Spec Guard artifacts",
  "id": "string | null",
  "revision": "integer",
  "content_hash": "string; required when artifact_type is source_artifact and absent otherwise"
}
```

For non-`source_artifact` refs, `content_hash` must be absent, not null. SourceArtifactRef arrays used in hashes or snapshot binding are canonical sets. Duplicate refs are removed by exact tuple identity `(artifact_type, id, revision)`, and duplicates with conflicting `content_hash` are invalid. Canonical order is Unicode code point order over canonical UTF-8 strings for `artifact_type`, then `id` with null before strings, then numeric `revision`. Locale collation must not be used. Spec Guard must not restrict `artifact_type` by file type, extension, media type, or source kind.

ApprovedPayloadRef:

```json
{
  "record_type": "batch_proceed_record | batch_review_snapshot | other",
  "record_id": "string",
  "payload_field": "string; e.g. selection",
  "payload_pointer": "string; canonical JSON pointer to payload root when payload_field is not sufficient",
  "payload_hash": "string",
  "payload_revision": "string"
}
```

BaselineReviewSnapshotPayload:

```json
{
  "stack": "RuntimeBaseline.stack",
  "commands": "RuntimeBaseline.commands",
  "configuration": "RuntimeBaseline.configuration",
  "dependency_modes": "RuntimeBaseline.dependency_modes",
  "diff_policy": "RuntimeBaseline.diff_policy",
  "validation": "RuntimeBaseline.validation"
}
```

AcReviewSnapshotPayload:

```json
{
  "work_id": "string | null",
  "work_packet_revision": "integer | null",
  "acceptance_criteria": "AcceptanceCriterion[]"
}
```

WorkPacketReviewSnapshotPayload:

```json
{
  "id": "string",
  "work_packet_revision": "integer",
  "title": "string",
  "parent_plan_id": "string | null",
  "plan_slice_id": "string | null",
  "intent": "WorkPacket.intent",
  "acceptance_criteria": "AcceptanceCriterion[]",
  "docs": {
    "policy": "DocsPolicy",
    "none_required_reason": "string | null",
    "not_applicable_reason": "string | null"
  },
  "scope": {
    "allowed_globs": "string[]"
  },
  "platform": "WorkPacket.platform",
  "architecture": "WorkPacket.architecture",
  "classification": "WorkClassification",
  "runtime_baseline_ref": "RuntimeBaselineRef"
}
```

ProposedAcReviewSnapshotPayload:

```json
{
  "proposed_child_id": "string",
  "expected_created_work_packet_revision": "integer; always 1 for batch-created children",
  "acceptance_criteria": "AcceptanceCriterion[]"
}
```

Batch child AC review snapshots use `ProposedAcReviewSnapshotPayload` because no WorkPacket revision exists yet. After child creation, the created WorkPacket acceptance criteria must exactly match this payload before batch AC approval can be recorded.

ProposedWorkPacketReviewSnapshotPayload:

```json
{
  "proposed_child_id": "string",
  "expected_created_work_packet_revision": "integer; always 1 for batch-created children",
  "proposed_work_payload": "ProposedWorkPacketPayload"
}
```

Batch child packet review snapshots use `ProposedWorkPacketReviewSnapshotPayload` because no WorkPacket revision exists yet. After child creation, the expected created revision must be 1 before batch child approval or authorization can be recorded.

BatchReviewSnapshotPayload:

```json
{
  "plan_id": "string",
  "plan_revision": "integer",
  "plan_proposal_hash": "string",
  "plan_proposal_snapshot_revision": "string",
  "source_artifact_refs": "SourceArtifactRef[]",
  "proposed_children_payload": "ProposedChildrenPayload",
  "proposed_children_payload_hash": "string",
  "proposed_children_payload_snapshot_revision": "string",
  "prompt_text": "string",
  "options": "string[]",
  "children": "BatchReviewSnapshotChildPayload[]"
}
```

BatchReviewSnapshotChildPayload:

```json
{
  "plan_slice_id": "string",
  "proposed_child_id": "string",
  "expected_created_work_packet_revision": "integer",
  "proposed_work_payload": "ProposedWorkPacketPayload",
  "proposed_work_payload_hash": "string",
  "proposed_work_payload_revision": "string; exactly payload:<proposed_work_payload_hash>",
  "contains_source_derived_acs": "boolean",
  "source_artifact_refs": "SourceArtifactRef[]",
  "ac_review_payload": "ProposedAcReviewSnapshotPayload",
  "ac_rendered_summary": "string",
  "ac_snapshot_hash": "string",
  "ac_snapshot_revision": "string",
  "packet_review_payload": "ProposedWorkPacketReviewSnapshotPayload",
  "packet_rendered_summary": "string",
  "packet_snapshot_hash": "string",
  "packet_snapshot_revision": "string",
  "authorization_review_payload": "ProposedAuthorizationReviewSnapshotPayload | null",
  "authorization_rendered_summary": "string | null",
  "authorization_snapshot_hash": "string | null",
  "authorization_snapshot_revision": "string | null",
  "batch_approval_eligible": "boolean",
  "batch_authorization_eligible": "boolean",
  "ineligibility_reasons": "string[]",
  "readiness": {
    "ac_approval_ready": "boolean",
    "packet_approval_ready": "boolean",
    "batch_authorization_ready": "boolean",
    "diagnostics": "Diagnostic[]"
  }
}
```

`BatchReviewSnapshotPayload` is the canonical hash root for a BatchReviewSnapshot. It excludes BatchReviewSnapshot `id`, `snapshot_hash`, `snapshot_revision`, `audit_revision`, `created_at`, and nested `ReviewSnapshot` wrapper records. The batch hash root includes the child review payloads, rendered summaries, hashes, revisions, eligibility flags, source refs, proposed work payload, and readiness data through `BatchReviewSnapshotChildPayload`.

ChangeBaselineCapturePlan:

```json
{
  "mode": "vcs | manifest",
  "capture_action": "authorize | batch_authorize",
  "work_id": "string | null",
  "proposed_child_id": "string | null",
  "allowed_globs": "string[]",
  "ignored_paths": "string[]",
  "vcs_required": "boolean",
  "manifest_includes": "string[]",
  "dirty_state_policy": "block_unapproved_product_changes"
}
```

ExpectedFileCategoryPolicy:

```json
{
  "path_policy_revision": "integer",
  "allowed_globs": "string[]",
  "ignored_paths": "string[]",
  "allowed_preimplementation_categories": "ChangeFileCategory[]",
  "implementation_categories": "ChangeFileCategory[]",
  "unexpected_category": "other_unexpected"
}
```

`change_baseline_capture_plan` and `expected_file_category_policy` are constructed by the deterministic kernel from Config.path_policy, packet allowed globs, selected baseline mode, and current WorkPacket/proposed child identity. Callers may not supply unvalidated object shapes for these fields.

AuthorizationReviewSnapshotPayload:

```json
{
  "id": "string",
  "work_packet_revision": "integer",
  "approved_packet_snapshot_hash": "string",
  "approved_packet_snapshot_revision": "string",
  "authorization_ready_diagnostics": "Diagnostic[]",
  "allowed_globs": "string[]",
  "runtime_baseline_ref": "RuntimeBaselineRef",
  "change_baseline_capture_plan": "ChangeBaselineCapturePlan",
  "expected_file_category_policy": "ExpectedFileCategoryPolicy",
  "implementation_boundary_summary": "string"
}
```

ProposedAuthorizationReviewSnapshotPayload:

```json
{
  "plan_slice_id": "string; must match an approved Plan slice proposed_id",
  "proposed_child_id": "string; must match ^[A-Za-z0-9._-]+$ and equal plan_slice_id",
  "expected_created_work_packet_revision": "integer",
  "proposed_packet_snapshot_hash": "string",
  "proposed_packet_snapshot_revision": "string",
  "authorization_ready_diagnostics": "Diagnostic[]",
  "allowed_globs": "string[]",
  "runtime_baseline_ref": "RuntimeBaselineRef",
  "change_baseline_capture_plan": "ChangeBaselineCapturePlan",
  "expected_file_category_policy": "ExpectedFileCategoryPolicy",
  "implementation_boundary_summary": "string"
}
```

BatchProceedSelectionPayload:

```json
{
  "plan_id": "string",
  "selected_option": "integer",
  "batch_snapshot_hash": "string",
  "batch_snapshot_revision": "string",
  "proposed_children_payload_hash": "string",
  "children": [
    {
      "plan_slice_id": "string; must match an approved Plan slice proposed_id",
      "proposed_child_id": "string; must match ^[A-Za-z0-9._-]+$ and equal plan_slice_id",
      "selected_for_creation": "boolean",
      "requested_ac_batch_approval": "boolean",
      "requested_packet_batch_approval": "boolean",
      "requested_batch_authorization": "boolean",
      "ac_snapshot_hash": "string | null",
      "ac_snapshot_revision": "string | null",
      "packet_snapshot_hash": "string | null",
      "packet_snapshot_revision": "string | null",
      "authorization_snapshot_hash": "string | null",
      "authorization_snapshot_revision": "string | null"
    }
  ]
}
```

BatchProceedResult:

```json
{
  "plan_id": "string",
  "batch_proceed_record_id": "string",
  "children": [
    {
      "plan_slice_id": "string; must match an approved Plan slice proposed_id",
      "proposed_child_id": "string; must match ^[A-Za-z0-9._-]+$ and equal plan_slice_id",
      "created_work_packet_id": "string | null",
      "ac_batch_approved": "boolean",
      "packet_batch_approved": "boolean",
      "batch_authorized": "boolean",
      "ac_snapshot_hash": "string | null",
      "ac_snapshot_revision": "string | null",
      "packet_snapshot_hash": "string | null",
      "packet_snapshot_revision": "string | null",
      "authorization_snapshot_hash": "string | null",
      "authorization_snapshot_revision": "string | null",
      "packet_change_baseline_ref": "string | null",
      "diagnostics": "Diagnostic[]"
    }
  ]
}
```

BatchProceedRecord:

```json
{
  "id": "string",
  "plan_id": "string",
  "decision": "HumanDecision",
  "selection": "BatchProceedSelectionPayload",
  "selection_hash": "string",
  "selection_revision": "string",
  "result": "BatchProceedResult",
  "result_hash": "string",
  "result_revision": "string",
  "batch_snapshot_hash": "string",
  "batch_snapshot_revision": "string",
  "created_at": "timestamp"
}
```

VerifierTask:

```json
{
  "task_id": "string",
  "schema_version": "integer",
  "task_type": "docs_mapping | docs_updated | tests_mapping | documented_contract_mapping | failure_evidence | retained_test_not_docs | runtime | final | other",
  "claims": "Claim[]; submitted claim ids/text",
  "evidence_refs": "string[]; deterministic EvidenceRecord or CommandResult refs",
  "deterministic_references": [
    { "ref_type": "string", "id": "string", "hash": "string | null", "revision": "string | integer | null" }
  ],
  "human_approved_refs": [
    { "decision_id": "string", "decision_type": "string", "approved_fields": "string[]", "payload_hash": "string | null", "payload_revision": "string | null" }
  ],
  "prohibited_judgment_rules": "string[]",
  "instructions": "string"
}
```

VerifierResponse:

```json
{
  "task_id": "string",
  "schema_version": "integer",
  "status": "passed | failed | inconclusive",
  "findings": "VerifierFinding[]",
  "verified_claim_ids": "string[]",
  "unverified_claim_ids": "string[]",
  "contradicted_claim_ids": "string[]",
  "prohibited_human_intent_judgment_detected": "boolean"
}
```

VerifierConfigUpdateInput:

```json
{
  "mode": "disabled | local_command | http | provider_model | test_fixture",
  "adapter_config": "LocalCommandAdapterConfig | HttpAdapterConfig | ProviderModelAdapterConfig | TestFixtureAdapterConfig | null"
}
```

LocalCommandAdapterConfig:

```json
{
  "adapter_kind": "generic_command | pi_headless_rpc",
  "command_spec": "CommandSpec | null; required for generic_command and derived for pi_headless_rpc",
  "pi": "PiHeadlessRpcAdapterConfig | null; required when adapter_kind is pi_headless_rpc",
  "health_timeout_ms": "integer"
}
```

PiHeadlessRpcAdapterConfig:

```json
{
  "provider": "string; default openai-codex",
  "model": "string; default gpt-5.4-mini",
  "no_session": true,
  "no_tools": true,
  "runtime_dir": "string | null; defaults to Spec Guard runtime storage",
  "prompt_timeout_ms": "integer",
  "busy_policy": "reject",
  "output_mode": "text_only | json_from_text",
  "suppress_thinking_events": true
}
```

HttpAdapterConfig:

```json
{
  "endpoint": "string",
  "auth_env_var": "string | null",
  "timeout_ms": "integer",
  "data_sharing_policy": "string"
}
```

ProviderModelAdapterConfig:

```json
{
  "provider": "string",
  "model": "string",
  "credential_env_var": "string | null",
  "timeout_ms": "integer",
  "data_sharing_policy": "string"
}
```

TestFixtureAdapterConfig:

```json
{
  "fixture_name": "string",
  "allowed_in_production": false
}
```

WorkIntentDraftInput:

```json
{
  "title": "string | absent",
  "goal": "string | absent",
  "desired_outcomes": "string[] | absent",
  "in_scope": "string[] | absent",
  "out_of_scope": "string[] | absent",
  "users_actors": "string[] | absent",
  "edge_cases": "string[] | absent",
  "open_questions": "string[] | absent",
  "acceptance_criteria": "AcceptanceCriterion[] | absent",
  "docs_policy": "DocsPolicy | absent",
  "docs_none_required_reason": "string | absent",
  "docs_not_applicable_reason": "string | absent",
  "allowed_globs": "string[] | absent",
  "architecture": "object with WorkPacket architecture shape | absent"
}
```

ChoicePromptOption is the object type used inside `ChoicePrompt.options`.

ReviewSnapshot:

```json
{
  "id": "string",
  "category": "ephemeral | persisted | batch",
  "producer_action_id": "string",
  "snapshot_hash": "string",
  "snapshot_revision": "string",
  "audit_revision": "integer | null; required when category is persisted or batch and absent/null otherwise",
  "source_artifact_refs": "SourceArtifactRef[]",
  "payload": "object; one of BaselineReviewSnapshotPayload, AcReviewSnapshotPayload, ProposedAcReviewSnapshotPayload, WorkPacketReviewSnapshotPayload, ProposedWorkPacketReviewSnapshotPayload, AuthorizationReviewSnapshotPayload, PlanProposalPayload, BatchReviewSnapshotPayload, or ProposedAuthorizationReviewSnapshotPayload",
  "rendered_summary": "string",
  "created_at": "timestamp"
}
```

ChoicePrompt:

```json
{
  "id": "string",
  "choice_type": "string",
  "prompt_text": "string",
  "options": [
    {
      "number": "integer",
      "label": "string",
      "kind": "standard | something_else | discuss | custom_confirmation",
      "payload": "object | null; structured option data needed to construct a registered decision payload",
      "architecture_option_details": "object | null; required for architecture standard/custom confirmation options",
      "custom_confirmation_value": "string | null; required for custom_confirmation options"
    }
  ],
  "status": "pending | answered | superseded",
  "custom_confirmation_required": "boolean",
  "created_at": "timestamp"
}
```

ChoiceAnswer:

```json
{
  "choice_id": "string",
  "selected_number": "integer",
  "raw_response": "string",
  "normalized_decision": "string",
  "human_confirmed": "boolean",
  "created_at": "timestamp"
}
```

IntakeRequest:

```json
{
  "title": "string",
  "goal": "string",
  "acceptance_criteria": "AcceptanceCriterion[] | absent",
  "desired_outcomes": "string[] | absent",
  "in_scope": "string[] | absent",
  "out_of_scope": "string[] | absent",
  "users_actors": "string[] | absent",
  "edge_cases": "string[] | absent",
  "open_questions": "string[] | absent",
  "docs_policy": "DocsPolicy | absent",
  "docs_none_required_reason": "string | absent",
  "docs_not_applicable_reason": "string | absent; required when docs_policy is not_applicable",
  "allowed_globs": "string[] | absent"
}
```

ProductContext:

```json
{
  "platform_choice": "string | null",
  "platform_decision_id": "string | null",
  "architecture_decision_ids": "string[]",
  "source_request_summary": "string | null",
  "source_evidence_summary": "string | null"
}
```

PlanVsSingleDecisionPayload:

```json
{
  "work_id": "string",
  "selected_option": "integer; 1 or 2",
  "presented_ac_payload": "AcceptanceCriterion[]",
  "presented_ac_payload_hash": "string",
  "presented_ac_refs": "string[]; derived from presented_ac_payload ids"
}
```

PlatformChoiceDecisionPayload:

```json
{
  "work_id": "string",
  "choice": "string",
  "custom_response": "string | null"
}
```

ArchitectureChoiceDecisionPayload:

```json
{
  "work_id": "string",
  "choice": "string",
  "custom_response": "string | null",
  "option_details": {
    "label": "string",
    "description": "string",
    "benefits": "string[]",
    "costs_tradeoffs": "string[]",
    "downstream_constraints": "string[]"
  }
}
```

PlanProposalPayload:

```json
{
  "title": "string",
  "goal": "string",
  "source_work_id": "string | null",
  "product_context": "ProductContext",
  "summary": "string",
  "source_artifact_refs": "SourceArtifactRef[]; optional source refs used by plan.propose snapshot binding",
  "slices": [
    {
      "proposed_id": "string; must match ^[A-Za-z0-9._-]+$",
      "title": "string",
      "goal": "string",
      "desired_outcomes": "string[]",
      "in_scope": "string[]",
      "out_of_scope": "string[]",
      "users_actors": "string[]",
      "edge_cases": "string[]",
      "open_questions": "string[]",
      "ac_ids": "string[]; derived from acceptance_criteria ids and must match them",
      "acceptance_criteria": "AcceptanceCriterion[]; full payloads required for every Plan slice",
      "classification": "WorkClassification",
      "docs_policy": "DocsPolicy",
      "docs_none_required_reason": "string | null; required when docs_policy is none_required",
      "docs_not_applicable_reason": "string | null; required when docs_policy is not_applicable",
      "allowed_globs": "string[]",
      "contains_source_derived_acs": "boolean",
      "source_evidence_summary": "string | null"
    }
  ]
}
```

ProposedWorkPacketPayload:

```json
{
  "id": "string; proposed WorkPacket id to create; must equal proposed_child_id",
  "title": "string",
  "parent_plan_id": "string",
  "plan_slice_id": "string; must match an approved Plan slice proposed_id",
  "classification": "WorkClassification",
  "intent": {
    "goal": "string",
    "desired_outcomes": "string[]",
    "in_scope": "string[]",
    "out_of_scope": "string[]",
    "users_actors": "string[]",
    "edge_cases": "string[]",
    "open_questions": "string[]"
  },
  "acceptance_criteria": "AcceptanceCriterion[]",
  "docs": {
    "policy": "DocsPolicy",
    "none_required_reason": "string | null; required when policy is none_required",
    "not_applicable_reason": "string | null",
    "requirements": "DocsRequirement[]"
  },
  "scope": {
    "allowed_globs": "string[]",
    "deviations": "string[]"
  },
  "platform": {
    "required": "boolean",
    "choice": "string | null",
    "decision_id": "string | null",
    "not_required_reason": "string | null"
  },
  "architecture": {
    "required": "boolean",
    "required_reason": "string | null",
    "not_required_reason": "string | null",
    "decision_ids": "string[]"
  },
  "runtime_baseline_ref": "RuntimeBaselineRef | null",
  "source_evidence_summary": "string | null; required when the approved Plan slice has source_evidence_summary or child ACs are source-derived"
}
```

When a Plan slice docs policy is `not_applicable`, ProposedWorkPacketPayload.docs.not_applicable_reason must equal the Plan slice `docs_not_applicable_reason`.

`ProposedWorkPacketPayload` is the canonical proposed child equality and hash root. It intentionally excludes `artifact_type`, `schema_version`, `revision`, `created_at`, `updated_at`, `status`, lifecycle records, decision history, evidence, backend verification records, review records, change baseline, diagnostics, command results, and other generated/audit/runtime fields. When a child WorkPacket is created, Spec Guard compares the corresponding approval-relevant paths in the created WorkPacket against this payload.

`source_evidence_summary` comparison is deterministic string equality against the approved Plan slice `source_evidence_summary`. Source-derived AC evidence is not compared by free-form summary prose; it is compared through each AC's structured SourceEvidence records, their source artifact refs, and their source evidence hashes. `ProposedWorkPacketPayload` does not carry non-AC source dependencies as approval-relevant child fields; governed source-derived child dependencies must be represented on source-derived AC SourceEvidence records.

ProposedChildrenPayload:

```json
{
  "plan_id": "string",
  "source_artifact_refs": "SourceArtifactRef[]; optional top-level refs used to derive BatchReviewSnapshot.source_artifact_refs in addition to the approved Plan ref; child-level and AC-level refs are also included",
  "children": [
    {
      "plan_slice_id": "string; must match an approved Plan slice proposed_id",
      "proposed_child_id": "string; must match ^[A-Za-z0-9._-]+$ and equal plan_slice_id",
      "expected_created_work_packet_revision": "integer",
      "proposed_work_payload": "ProposedWorkPacketPayload",
      "title": "string; optional shorthand, must match the approved Plan slice title when present",
      "goal": "string; optional shorthand, must match proposed_work_payload.intent.goal when present",
      "acceptance_criteria": "AcceptanceCriterion[]; optional shorthand, must match proposed_work_payload.acceptance_criteria when present",
      "contains_source_derived_acs": "boolean; optional shorthand, must match proposed_work_payload.acceptance_criteria",
      "scope": "object; optional shorthand, must match proposed_work_payload.scope",
      "classification": "WorkClassification; optional shorthand, must match proposed_work_payload.classification",
      "docs_policy": "DocsPolicy; optional shorthand, must match proposed_work_payload.docs.policy",
      "allowed_globs": "string[]; optional shorthand, must match proposed_work_payload.scope.allowed_globs",
      "source_evidence_summary": "string | null; optional shorthand, must exactly equal proposed_work_payload.source_evidence_summary when present",
      "source_artifact_refs": "SourceArtifactRef[]; optional child-level snapshot provenance refs; governed source-derived AC dependencies must still be declared on SourceEvidence records",
      "platform": "object with WorkPacket platform shape; optional shorthand, must match proposed_work_payload.platform",
      "architecture": "object with WorkPacket architecture shape; optional shorthand, must match proposed_work_payload.architecture",
      "readiness_diagnostics": "Diagnostic[]"
    }
  ]
}
```

`proposed_work_payload` is the canonical payload for hashing, review snapshots, batch approvals, and child creation. Shorthand fields are optional validation aids and must not conflict with `proposed_work_payload`. `ProposedChildrenPayload` hashes include `plan_id`, top-level `source_artifact_refs`, each child's ids, expected revision, canonical `proposed_work_payload`, child source refs, and readiness diagnostics; optional shorthand mirror fields are excluded from the hash and never affect approval binding. When BatchReviewSnapshotPayload embeds `proposed_children_payload`, snapshot hashing uses this same shorthand-excluded canonical projection, while the stored audit record may retain shorthand mirrors for readability.

DocsContentTokens:

```json
{
  "paths": "string[]; normalized docs/content paths",
  "headings": "string[]; exact heading text without markup prefix",
  "links": "string[]; exact link targets or URLs",
  "examples": "string[]; exact fenced code block bodies or example snippets selected by docs evidence action"
}
```

Docs actions extract `paths` from supplied docs paths, `headings` from markdown-style heading lines beginning with one or more `#` characters, `links` from markdown link targets and plain URLs, and `examples` from fenced code blocks. Other formats may populate only paths unless a deterministic parser is configured. These tokens are the only docs heading/link/example tokens used by retained-doc-test detection.

Blocker:

```json
{
  "reason": "string",
  "owner": "string | null",
  "next_action": "string | null",
  "at": "timestamp"
}
```

CleanupEvidence:

```json
{
  "checked_resources": "string[]",
  "resource_categories": "string[]; exact structured categories checked or declared not applicable",
  "before_observations": "object; kernel-captured or command-backed",
  "after_observations": "object; kernel-captured or command-backed",
  "side_effect_status": "none | cleaned | remaining_unapproved_side_effects; derived by kernel",
  "related_evidence_refs": "string[]",
  "remaining_cleanup_actions": "string[]"
}
```

NotApplicableEvidence:

```json
{
  "evidence_type": "tests | test_failure | test_pass | runtime_production | runtime_development | cleanup | implementation_files",
  "resource_categories": "string[]; required and non-empty when evidence_type is cleanup, empty otherwise",
  "reason": "string",
  "applies_to_ac_ids": "string[]",
  "classification_policy_context": "string"
}
```

CommandSpec:

```json
{
  "mode": "argv | shell",
  "argv": "string[]; required when mode is argv",
  "shell_command": "string | null; required when mode is shell",
  "working_directory": "string",
  "timeout_ms": "integer | null",
  "env_mode": "inherit | clean | configured",
  "env_overrides_ref": "string | null"
}
```

`argv` mode executes without a shell and is preferred for governed evidence. `shell` mode executes through the configured project shell recorded in config; shell quoting is interpreted only by that configured shell. Working directory must be project-relative or an approved absolute project root. Placeholder/version-only/self-check command rejection is deterministic. A command with purpose `test`, `build`, `runtime_production`, or `runtime_development` cannot satisfy governed validation when its normalized CommandSpec matches any invalid placeholder pattern: executable basename `echo`, `printf`, `true`, `false`, `pwd`, or `whoami`; a single executable with only version/help flags such as `--version`, `-v`, `-V`, `version`, `--help`, or `help`; shell commands consisting only of those forms or `exit <code>`; or executable basename `spec-guard`, `pi`, or the current Spec Guard binary with arguments that only inspect Spec Guard state. These commands may still be recorded as CommandResults with purpose `other`, but they cannot satisfy baseline, evidence, or review gates.

CommandResult:

```json
{
  "id": "string",
  "storage_ref": "string; durable CommandResult record location or id",
  "command": "string; display form derived from command_spec",
  "command_spec": "CommandSpec",
  "purpose": "test | build | runtime_production | runtime_development | verifier_health | other",
  "working_directory": "string",
  "timeout_ms": "integer | null",
  "env_mode": "string | null",
  "related_work_id": "string | null",
  "related_runtime_baseline_ref": "RuntimeBaselineRef | null",
  "related_runtime_baseline_draft_revision": "integer | null",
  "exit_code": "integer | null",
  "started_at": "timestamp",
  "finished_at": "timestamp | null",
  "duration_ms": "integer | null",
  "status": "passed | failed | timed_out | skipped",
  "skip_reason": "string | null; required when status is skipped",
  "skip_precondition": "string | null; deterministic precondition that caused the skip",
  "error_message": "string | null; required when command could not spawn, was terminated by signal, or failed without exit code",
  "output_ref": "string | null",
  "output_excerpt": "string | null",
  "resource_categories": "string[]",
  "cleanup_observations": "CleanupCommandObservations | null",
  "source_interface": "string"
}
```

CommandResult records are durable embedded records or standalone records referenced by `storage_ref`. They must be retrievable by `command_result_ref` from EvidenceRecord.

DocsRequirement:

```json
{
  "id": "string",
  "path": "string",
  "related_ac_ids": "string[]",
  "required_before": "tests | review_completion",
  "status": "missing | present | updated | not_applicable"
}
```

LifecycleEvent:

```json
{
  "at": "timestamp",
  "from_status": "string | null",
  "to_status": "string",
  "reason": "string",
  "decision_id": "string | null",
  "source_interface": "string"
}
```

Claim:

```json
{
  "id": "string",
  "text": "string",
  "claim_type": "docs_mapping | docs_updated | tests_mapping | documented_contract_mapping | failure_evidence | retained_test_not_docs | runtime | implementation_summary | final | other",
  "related_ac_ids": "string[]",
  "related_doc_ids": "string[]",
  "evidence_refs": "string[]",
  "resource_categories": "string[]; structured cleanup/runtime resource category strings, empty when not applicable",
  "presentation": "verified | unverified | not_applicable"
}
```

VerifierFinding:

```json
{
  "id": "string",
  "finding_kind": "claim_conflicts_with_reference | claim_exceeds_reference | claim_unsupported_by_reference | evidence_missing | schema_error | prohibited_human_intent_judgment | other",
  "target_type": "agent_claim | evidence_mapping | deterministic_reference | human_approved_reference",
  "target_id": "string",
  "severity": "error | warning | info",
  "message": "string",
  "prohibited_human_intent_judgment": "boolean"
}
```

AcceptanceCriterion:

```json
{
  "id": "string",
  "text": "string",
  "source": "human | frontend_agent | source_derived",
  "source_evidence": "SourceEvidence | null; required when source is source_derived and optional otherwise"
}
```

AcceptanceCriterion ids must be unique within a WorkPacket `acceptance_criteria` array and within each Plan slice `acceptance_criteria` array. Plan slices must include full AcceptanceCriterion payloads for every AC. `ac_ids` are derived traceability mirrors and must exactly match the ids in `acceptance_criteria`. Source-derived ACs must include SourceEvidence with non-empty canonical `source_artifact_refs` and `evidence_hash`.

SourceEvidence:

```json
{
  "kind": "string; open string, not a closed enum",
  "reference": "string",
  "description": "string",
  "source_artifact_refs": "SourceArtifactRef[]; non-empty when attached to a source-derived AC",
  "evidence_hash": "string; hash of canonical SourceEvidence fields excluding evidence_hash and including canonical source_artifact_refs"
}
```

A SourceEvidence record depends on exactly the artifacts listed in `source_artifact_refs`. Deterministic dependency validation uses these refs and `evidence_hash`; it must not infer dependencies from free-form `description` text. Spec Guard must not restrict `kind`, `reference`, or referenced material by a finite list of file types, extensions, media types, or artifact kinds.

RuntimeBaselineRef:

```json
{
  "artifact_type": "runtime_baseline",
  "id": "string | null; null for singleton runtime baseline",
  "revision": "integer",
  "accepted_at": "timestamp",
  "acceptance_decision_id": "string",
  "acceptance_snapshot_hash": "string",
  "acceptance_snapshot_revision": "string"
}
```

FileStateSnapshot:

```json
{
  "captured_at": "timestamp",
  "mode": "vcs | manifest",
  "vcs_commit": "string | null",
  "manifest_hash": "string | null",
  "changed_files_since_packet_baseline": "ChangedFile[]"
}
```

PreauthorizationDirtyEntry:

```json
{
  "path": "string",
  "status": "added | modified | deleted | renamed | untracked",
  "size": "integer | null; null for deleted",
  "content_hash": "string | null; null for deleted"
}
```

CleanupCommandObservations:

```json
{
  "resource_categories": "string[]",
  "before_observations": "object",
  "after_observations": "object",
  "observer_diagnostics": "Diagnostic[]"
}
```

ChangedFile:

```json
{
  "path": "string",
  "category": "ChangeFileCategory",
  "status": "added | modified | deleted | renamed | untracked",
  "allowed_by_globs": "boolean"
}
```

---

<a id="us-24-source"></a>
# Appendix B. Shared Action Contracts

> Derived user story: [US-24: Shared action contracts](user-stories/24-shared-action-contracts.md)

## B.1 Shared action result

```json
{
  "ok": "boolean",
  "action_id": "string",
  "data": "object",
  "diagnostics": "Diagnostic[]",
  "mutations": [
    { "artifact": "string", "operation": "create | update | audit_record | supersede | archive_metadata | none", "paths": "string[]", "summary": "string" }
  ],
  "next_actions": [
    { "action_id": "string", "cli": "string | null", "mcp": "string | null", "reason": "string", "suggested_input": "object | null" }
  ],
  "summary": "string"
}
```

## B.2 Required actions

Each action has the same input schema for CLI and MCP when both interfaces are supported. CLI bootstrap-only and CLI local-runtime-only actions have no MCP tool requirement.

All `patch` inputs use RFC 6902 JSON Patch arrays with operations `add`, `replace`, and `remove` only. Each operation must include `op` and `path`; `add` and `replace` must include `value`. Paths are canonical JSON pointers. Before applying a patch, Spec Guard must compute the affected paths, reject nonexistent paths for `replace`/`remove`, reject type-invalid values, and run approved-field impact detection against the exact affected path set.

The `Mutates` column uses `yes` for governed state mutation, `no` for no mutation, and `audit_only` for persisted review/audit records that do not change governed state.

| Action id | MCP tool | Mutates | Required inputs | Optional inputs |
|---|---|---:|---|---|
| `init` | none | yes | none | project id, artifact root, json output flag |
| `config.get` | `spec_guard_config_get` | no | none | include_full |
| `config.update` | `spec_guard_config_update` | yes | patch | confirm unsafe host |
| `config.check` | `spec_guard_config_check` | no | none | none; returns config validation plus persisted-artifact governance summary used by viewer dashboard |
| `verifier.config.get` | `spec_guard_verifier_config_get` | no | none | none |
| `verifier.config.update` | `spec_guard_verifier_config_update` | yes | VerifierConfigUpdateInput | human confirmation fields |
| `verifier.health_check` | `spec_guard_verifier_health_check` | yes | none | include_full |
| `baseline.init` | `spec_guard_baseline_init` | yes | none | draft baseline fields |
| `baseline.update` | `spec_guard_baseline_update` | yes | patch | source work id, human runtime confirmation |
| `baseline.review` | `spec_guard_baseline_review` | no | none | include_full |
| `baseline.accept` | `spec_guard_baseline_accept` | yes | selected_number, raw_response, decision_prompt, human_confirmed, review_snapshot_hash, review_snapshot_revision, source_artifact_refs | actor |
| `baseline.block` | `spec_guard_baseline_block` | yes | reason | owner, next_action |
| `baseline.check` | `spec_guard_baseline_check` | no | none | include_full |
| `source_artifact.register` | `spec_guard_source_artifact_register` | yes | SourceArtifactRegisterInput | none |
| `source_artifact.get` | `spec_guard_source_artifact_get` | no | id | revision, include_full |
| `source_artifact.list` | `spec_guard_source_artifact_list` | no | none | filters |
| `source_artifact.update` | `spec_guard_source_artifact_update` | yes | SourceArtifactUpdateInput | none |
| `plan.propose` | `spec_guard_plan_propose` | no | plan_proposal_payload | source_work_id, include_full |
| `plan.approve` | `spec_guard_plan_approve` | yes | plan_proposal_payload, selected_number, raw_response, decision_prompt, human_confirmed, review_snapshot_hash, review_snapshot_revision, source_artifact_refs | source_work_id, plan id |
| `plan.batch_snapshot.create` | `spec_guard_plan_batch_snapshot_create` | audit_only | plan_id, proposed_children_payload | include_full |
| `plan.batch_proceed` | `spec_guard_plan_batch_proceed` | yes | plan_id, batch_snapshot_hash, batch_snapshot_revision, selected_number, raw_response, decision_prompt, human_confirmed | none |
| `plan.child.create` | `spec_guard_plan_child_create` | yes | plan_id, plan_proposal_hash, plan_proposal_snapshot_revision, plan_slice_id, proposed_work_payload | none |
| `plan.list` | `spec_guard_plan_list` | no | none | include archived |
| `plan.get` | `spec_guard_plan_get` | no | id | include_full |
| `plan.update` | `spec_guard_plan_update` | yes | id, patch | none |
| `plan.archive` | `spec_guard_plan_archive` | yes | id | reason |
| `decision.create` | `spec_guard_decision_create` | yes | decision_type, decision_prompt, selected_number, raw_response, human_confirmed | custom_response, approved_payload, reviewed_payload, review_snapshot_hash, review_snapshot_revision, source_artifact_refs, approved_fields required for custom/unregistered decision types |
| `decision.list` | `spec_guard_decision_list` | no | none | filters |
| `decision.get` | `spec_guard_decision_get` | no | id | include_full |
| `decision.supersede` | `spec_guard_decision_supersede` | yes | prior_decision_id, decision_type, decision_prompt, selected_number, raw_response, human_confirmed | custom_response, approved_payload, reviewed_payload, review_snapshot_hash, review_snapshot_revision, source_artifact_refs, approved_fields for custom/unregistered decision types |
| `decision.archive_metadata` | `spec_guard_decision_archive_metadata` | yes | id, reason | none |
| `review_snapshot.persist` | `spec_guard_review_snapshot_persist` | audit_only | producer_action_id, source_snapshot_hash, source_snapshot_revision, source_artifact_refs, payload | rendered_summary; returns persisted snapshot_hash and persisted_snapshot_revision |
| `work.intake` | `spec_guard_work_intake` | yes | request, classification | id |
| `work.intent.draft` | `spec_guard_work_intent_draft` | yes | work id, WorkIntentDraftInput | none |
| `work.list` | `spec_guard_work_list` | no | none | filters |
| `work.get` | `spec_guard_work_get` | no | id | include_full |
| `work.update` | `spec_guard_work_update` | yes | id, patch | none |
| `work.check` | `spec_guard_work_check` | no | id | gate |
| `work.next` | `spec_guard_work_next` | no | id | include_full |
| `work.plan_choice.answer` | `spec_guard_work_plan_choice_answer` | yes | id, selected_number, raw_response, decision_prompt, human_confirmed, presented_ac_payload, presented_ac_payload_hash | presented_ac_refs |
| `work.choice.propose` | `spec_guard_work_choice_propose` | audit_only | id, choice_type, prompt, ChoicePromptOption[] | none |
| `work.choice.answer` | `spec_guard_work_choice_answer` | yes | id, choice_id, selected_number, raw_response, decision_prompt, human_confirmed | none |
| `work.choice.confirm_custom` | `spec_guard_work_choice_confirm_custom` | yes | id, choice_id, selected_number, raw_response, decision_prompt, human_confirmed | none |
| `work.ac.review` | `spec_guard_work_ac_review` | no | id | proposed_ac_payload, include_source_evidence |
| `work.ac.approve` | `spec_guard_work_ac_approve` | yes | id, reviewed_ac_payload, selected_number, raw_response, decision_prompt, human_confirmed, review_snapshot_hash, review_snapshot_revision, source_artifact_refs | none |
| `work.coverage.propose` | `spec_guard_work_coverage_propose` | no | id | source refs; renders coverage/source-evidence suggestions only and never records approval |
| `work.backend.verify` | `spec_guard_work_backend_verify` | yes | id, task_type, claim_ids | adapter override if allowed |
| `work.preimplementation.validate` | `spec_guard_work_preimplementation_validate` | yes | id | include_full |
| `work.implementation.start` | `spec_guard_work_implementation_start` | yes | id | none |
| `work.implementation.complete` | `spec_guard_work_implementation_complete` | yes | id, summary | implementation files, test files |
| `work.split` | `spec_guard_work_split` | no | id | include_full |
| `work.packet.review` | `spec_guard_work_packet_review` | no | id | include_full |
| `work.approve` | `spec_guard_work_approve` | yes | id, selected_number, raw_response, decision_prompt, human_confirmed, review_snapshot_hash, review_snapshot_revision, source_artifact_refs | none |
| `work.authorization.review` | `spec_guard_work_authorization_review` | no | id | include_full |
| `work.authorize` | `spec_guard_work_authorize` | yes | id, selected_number, raw_response, decision_prompt, human_confirmed, review_snapshot_hash, review_snapshot_revision, source_artifact_refs | none |
| `command.run` | `spec_guard_command_run` | yes | command_spec, purpose | related work id, related runtime baseline ref, related runtime baseline draft revision, resource_categories, skip_reason, skip_precondition |
| `work.evidence.failure` | `spec_guard_work_evidence_failure` | yes | id, command_result_ref, paths, related_ac_ids, evidence_role, summary | related_doc_ids, resource_categories |
| `work.evidence.pass` | `spec_guard_work_evidence_pass` | yes | id, command_result_ref, paths, related_ac_ids, evidence_role, summary | related_doc_ids, resource_categories |
| `work.evidence.runtime` | `spec_guard_work_evidence_runtime` | yes | id, mode, command_result_ref, paths, related_ac_ids, summary | related_doc_ids, resource_categories |
| `work.evidence.cleanup` | `spec_guard_work_evidence_cleanup` | yes | id, checked_resources, resource_categories, related_evidence_refs | before_command_result_refs, after_command_result_refs, remaining_cleanup_actions, caller_summary |
| `work.evidence.not_applicable` | `spec_guard_work_evidence_not_applicable` | yes | id, evidence_type, reason, applies_to_ac_ids, classification_policy_context | resource_categories for cleanup, selected_number/raw_response/decision_prompt/human_confirmed only to acknowledge an already-eligible not-applicable determination |
| `work.docs.add` | `spec_guard_work_docs_add` | yes | id, paths, related_ac_ids | summary, related_doc_ids |
| `work.docs.update` | `spec_guard_work_docs_update` | yes | id, paths, related_ac_ids | summary, related_doc_ids |
| `work.docs.none` | `spec_guard_work_docs_none` | yes | id, reason | human decision ref |
| `work.review.validate` | `spec_guard_work_review_validate` | no | id | include_full |
| `work.review.complete` | `spec_guard_work_review_complete` | yes | id | final claim refs |
| `work.claims.create` | `spec_guard_work_claims_create` | yes | id, Claim[] | none |
| `work.claims.validate` | `spec_guard_work_claims_validate` | yes | id, Claim[] | none |
| `work.claims.audit` | `spec_guard_work_claims_audit` | no | id | include_full |
| `validate.active` | `spec_guard_validate_active` | no | none | include archived |
| `validate.parity` | `spec_guard_validate_parity` | no | none | none |
| `mcp.quickstart` | `spec_guard_mcp_quickstart` | no | none | compact |
| `mcp.status` | `spec_guard_mcp_status` | no | none | include_full |
| `serve.viewer` | none | no | host, port | open browser; CLI-only local runtime action; starts a real listening long-running HTTP server and must not exit immediately after printing URL |

For `init`, the shared core action result remains the standard Appendix B.1 object internally. The CLI presentation layer is the exception: successful `npx spec-guard init` without a JSON flag must render a plain-text success summary instead of printing the raw action result JSON. `npx spec-guard init --json` or an equivalent explicit machine-readable mode must print the standard JSON result.

`command.run` executes a CommandSpec through the deterministic kernel and stores a CommandResult. It is the normal way to create command-backed governed evidence. When `related_runtime_baseline_ref` or `related_runtime_baseline_draft_revision` is supplied, Spec Guard must append the kernel-created CommandResult to the matching RuntimeBaseline `validation.command_results`; callers must not submit baseline validation CommandResults through `baseline.update`. `skipped` CommandResults may be created only when `command.run` is asked to record a deterministic precondition skip, such as a missing optional command with a recorded not-applicable reason; skipped results cannot satisfy required evidence gates. `work.docs.add` and `work.docs.update` create docs EvidenceRecords, populate `docs_content_tokens`, and must capture `file_state_snapshot` as kernel state during the action. Docs, failure, pass, and runtime evidence actions must capture and store `file_state_snapshot` as kernel state during the action. That snapshot is never a trusted caller input. Failure, pass, and runtime evidence actions must reference a kernel-created CommandResult and must derive command, exit code, status, timestamps, and output refs from that CommandResult rather than caller-supplied facts.

`work.split` is non-mutating analysis that returns proposed Plan or child packet suggestions and must not create artifacts or decisions. `work.coverage.propose` is non-mutating analysis that returns source/coverage suggestions and must not record approval. `work.docs.none` may set docs policy to `none_required` only when classification and docs rules allow it, must store the reason in `docs.none_required_reason`, and must reject API/contract-surface and operational-document packets. `work.claims.validate` validates supplied claims against schemas, required evidence refs, duplicate ids, and prohibited human-intent judgment references; it stores valid claims or diagnostics but does not mark verifier results passed.

## B.3 Human-gated action requirements

These actions must reject missing human confirmation:

- `baseline.accept`,
- `work.plan_choice.answer`,
- `work.choice.answer`,
- `work.choice.confirm_custom`,
- `work.ac.approve`,
- `work.approve`,
- `work.authorize`,
- `plan.approve`,
- `plan.batch_proceed`,
- decision actions that record human choices.

Human-gated actions must require and record `selected_number`, `raw_response`, `decision_prompt`, and `human_confirmed`. If the caller does not supply `prompt_id`, the action must deterministically generate one as `prompt:<action_id>:<sha256_lower_hex(canonical decision_prompt)>` and store it in the HumanDecision. Human-gated approval actions that bind to a review surface must also require and record `review_snapshot_hash`, `review_snapshot_revision`, and `source_artifact_refs`, or for batch proceed `batch_snapshot_hash` and `batch_snapshot_revision` with `source_artifact_refs` copied from the persisted BatchReviewSnapshot. `work.plan_choice.answer` must record decision type `plan_vs_single` only for selected option 1 or 2; option 3 Discuss creates no HumanDecision. `work.choice.answer` and `work.choice.confirm_custom` must record registered HumanDecision types for platform and architecture only when the selected option is a final confirmed platform or architecture choice. Discuss and unconfirmed custom prose must create no HumanDecision. `plan.batch_proceed` must store the canonical BatchProceedSelectionPayload and BatchProceedResult in a BatchProceedRecord on the Plan only for selected options 1 through 4; option 5 Discuss creates no HumanDecision and no BatchProceedRecord.

Generic `decision.create` and `decision.supersede` must not be used for standard workflow gate or choice decision types that have side effects: runtime baseline acceptance, Plan-vs-single, platform choice, architecture choice, AC approval, Work Packet approval, implementation authorization, Plan approval, and Plan batch proceed. Those decisions must use their specialized actions so required artifact writes, baseline capture, child creation, approvals, and authorizations occur atomically. Generic decision actions are allowed only for non-review-bound decisions or custom/unregistered decision types whose effects are limited to recording the decision. For any registered decision type whose approved-field root is `HumanDecision.approved_payload`, specialized decision actions must require enough input to construct and validate the canonical `approved_payload` when the selected option records a final approving/selecting decision. Decline, block, and Discuss paths must not require `approved_payload`.

Standard actions derive `approved_fields` from decision type. Custom decision actions must record explicit approved fields or use a registered decision type.

Generic update actions must validate approved-field impact. `work.update` must reject protected approved-field mutations or apply the mutation with deterministic invalidation of every dependent approval/authorization listed in the action result. `plan.update` must reject Plan-approved-field mutations unless a registered Plan amendment action exists; it must not silently invalidate Plan approval into an undefined non-approved state.

`work.evidence.not_applicable` must reject deterministic ineligibility. Human confirmation may acknowledge an eligible not-applicable determination, but must not create eligibility.

---

<a id="us-25-source"></a>
# Appendix C. Enums

> Derived user story: [US-25: Normative enums](user-stories/25-normative-enums.md)

## C.1 WorkClassification

- `reusable_api`
- `rest_api`
- `reusable_ui`
- `one_off_application_ui`
- `direct_behavior`
- `operational_document`
- `bugfix`

## C.2 WorkStatus

- `draft`
- `pending_ac_approval`
- `pending_packet_approval`
- `approved`
- `authorized`
- `preimplementation_validated`
- `implementation_active`
- `implemented`
- `review_complete`
- `blocked`
- `deferred`
- `archived`

## C.3 PlanStatus

- `approved`
- `children_created`
- `in_progress`
- `complete`
- `blocked`
- `archived`

## C.4 VerificationStatus

- `passed`
- `failed`
- `inconclusive`
- `invalid`

## C.5 EvidenceStatus

- `passed`
- `failed`
- `inconclusive`
- `not_applicable`

## C.6 DocsPolicy

- `required`
- `changed`
- `none_required`
- `not_applicable`

## C.7 ChangeFileCategory

- `spec_guard_artifact_evidence`
- `docs`
- `tests`
- `implementation_source`
- `runtime_product_configuration`
- `generated_build_output`
- `other_unexpected`
