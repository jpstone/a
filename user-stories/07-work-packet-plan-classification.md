# US-07: Work packets, plans, and classification

Derived from: [7. Work Packet, Plan, and Classification](../agentic-redesign-references.md#us-07-source)

## Problem

Spec Guard needs bounded work packets, multi-slice plans, and classification rules to keep implementation scope explicit and enforceable.

## User story

As a work planner, I want work packets, plans, and classification implemented, so that spec Guard needs bounded work packets, multi-slice plans, and classification rules to keep implementation scope explicit and enforceable.

## In scope

- Define Work Packet lifecycle states and required packet content.
- Define Plan content and statuses.
- Define work classification enum and docs requirements by classification.
- Handle API/contract-surface and non-API packet policies.

## Out of scope

- Implementing unbounded work without packet scope.
- Skipping required API/contract docs for reusable/API/contract-surface work.
- Using docs policy to weaken classification requirements.

## Acceptance criteria

<!-- Expanded from agentic-redesign.md to provide behavior-level coverage. -->

- [ ] AC-07-001: `blocked`,
- [ ] AC-07-002: A Work Packet must support:
- [ ] AC-07-003: source/evidence metadata for source-derived ACs,
- [ ] AC-07-004: allowed file globs,
- [ ] AC-07-005: backend verification records,
- [ ] AC-07-006: `work.intake` creates a valid draft Work Packet from an IntakeRequest and classification.
- [ ] AC-07-007: It must reject parent Plan ids or Plan slice ids
- [ ] AC-07-008: Plan children must be created only through `plan.child.create` or `plan.batch_proceed`.
- [ ] AC-07-009: IntakeRequest must include `title` and `goal`.
- [ ] AC-07-010: docs policy is `required` for API/contract-surface and `operational_document` classifications and `none_required` otherwise unless supplied with a classification-compatible policy.
- [ ] AC-07-011: Classification-compatible supplied policies are: API/contract-surface requires `required`
- [ ] AC-07-012: `operational_document` requires `required`
- [ ] AC-07-013: other classifications allow `required`, `changed`, `none_required`, or `not_applicable`.
- [ ] AC-07-014: If supplied docs policy is `not_applicable`, `request.docs_not_applicable_reason` must be non-empty
- [ ] AC-07-015: if supplied docs policy is `none_required`, `docs.none_required_reason` is set from `request.docs_none_required_reason` when supplied or to `classification_default_none_required`
- [ ] AC-07-016: otherwise docs reason fields are null unless later set by a docs action.
- [ ] AC-07-017: Docs requirements/records are empty
- [ ] AC-07-018: platform/architecture requiredness fields are computed by sections 8.1 and 8.2
- [ ] AC-07-019: Goal and ACs are required before AC approval.
- [ ] AC-07-020: AC approval is required before Work Packet approval except for explicit eligible Plan-child batch approval of non-source-derived ACs.
- [ ] AC-07-021: Work Packet approval is required before implementation authorization.
- [ ] AC-07-022: Implementation authorization and packet change baseline capture are one atomic governed action
- [ ] AC-07-023: PacketChangeBaseline capture must succeed before the authorization HumanDecision is recorded.
- [ ] AC-07-024: Pre-implementation validation is required before implementation source changes.
- [ ] AC-07-025: Approval is invalidated when approved title, parent Plan linkage, Plan slice linkage, intent, ACs, source evidence, approved scope fields such as allowed globs, classification, docs policy, platform, architecture, or runtime baseline reference changes.
- [ ] AC-07-026: Scope deviations and docs requirements are review context unless included in an approved-field set.
- [ ] AC-07-027: Generic update actions must not silently change approved fields.
- [ ] AC-07-028: If an update touches approved fields, Spec Guard must either reject it as a protected approved-field update or apply it and deterministically invalidate every dependent approval/authorization with diagnostics and next actions.
- [ ] AC-07-029: The action result must list every invalidated decision.
- [ ] AC-07-030: `plan.update` must reject changes to Plan-approved fields.
- [ ] AC-07-031: Because there is no persisted draft Plan state, an approved Plan cannot be moved back to draft by mutation.
- [ ] AC-07-032: Changing approved Plan intent requires a new Plan or a registered Plan amendment action with its own review snapshot and Plan approval decision.
- [ ] AC-07-033: Validation actions may update diagnostics without changing status unless listed above.
- [ ] AC-07-034: records blocking diagnostics and next actions.
- [ ] AC-07-035: A Plan must include:
- [ ] AC-07-036: approved Plan proposal record,
- [ ] AC-07-037: A Plan never authorizes implementation.
- [ ] AC-07-038: Only child Work Packets can be authorized.
- [ ] AC-07-039: Therefore there is no persisted proposal-only Plan status and no valid persisted draft Plan.
- [ ] AC-07-040: A Plan artifact is created only by Plan approval
- [ ] AC-07-041: must have an approval decision when created.
- [ ] AC-07-042: `plan.update` may mutate only non-approved operational metadata: status among non-archival runtime statuses, diagnostics, child_work_ids after validated child creation, and archive metadata through archive actions.
- [ ] AC-07-043: It must reject changes to title, goal, product_context, plan_proposal, approval, and any Plan-approved path.
- [ ] AC-07-044: Each Work Packet must have exactly one classification:
- [ ] AC-07-045: `work.intake` must receive a valid classification
- [ ] AC-07-046: The deterministic kernel validates enum membership.
- [ ] AC-07-047: The backend verifier must not judge classification quality.
- [ ] AC-07-048: API/contract-surface packets always require human-facing docs.
- [ ] AC-07-049: Required chain:
- [ ] AC-07-050: All other classifications follow the non-API chain unless docs policy requires docs.
- [ ] AC-07-051: Their docs/content policy must be `required`.
- [ ] AC-07-052: They may have tests and failure-first evidence marked not applicable only when the approved scope changes documentation/operational content
- [ ] AC-07-053: If an operational-document packet changes product behavior, it must be reclassified or follow the applicable product validation chain.
- [ ] AC-07-054: `required`: docs must exist and be linked to approved ACs before pre-implementation validation passes,
- [ ] AC-07-055: `changed`: docs are not required before pre-implementation validation, but docs must be updated and a `docs_updated` claim must pass backend verification before review completion,
- [ ] AC-07-056: `none_required`: docs are not required and `docs.none_required_reason` records why,
- [ ] AC-07-057: `not_applicable`: docs do not apply and `docs.not_applicable_reason` records why.
- [ ] AC-07-058: For API/contract-surface packets, docs policy must be `required`.
- [ ] AC-07-059: For `operational_document` packets, docs/content policy must be `required`
- [ ] AC-07-060: When docs are required, Spec Guard must validate:
- [ ] AC-07-061: required backend verification for docs-to-AC mapping passed.
- [ ] AC-07-062: When docs policy is `required` or `changed`, when docs policy changes during the packet lifecycle, or when docs files are changed, Spec Guard must require a registered `docs_updated` claim and passed backend verification for that claim before review completion.
- [ ] AC-07-063: For `required` docs, this requirement is in addition to docs existence and docs-to-AC mapping checks.
- [ ] AC-07-064: Documentation itself must never be the target of retained tests.
- [ ] AC-07-065: Tests must validate product behavior, API behavior, runtime behavior, or other approved non-document behavior.
- [ ] AC-07-066: Spec Guard must not require or accept retained tests that assert documentation text, formatting, files, headings, examples, or links as governed evidence.
- [ ] AC-07-067: Temporary scripts or tests that an agent uses to aid documentation work are permitted only if removed before review completion.
- [ ] AC-07-068: Enumerated item is supported/enforced: `draft`,
- [ ] AC-07-069: Enumerated item is supported/enforced: `pending_ac_approval`,
- [ ] AC-07-070: Enumerated item is supported/enforced: `pending_packet_approval`,
- [ ] AC-07-071: Enumerated item is supported/enforced: `approved`,
- [ ] AC-07-072: Enumerated item is supported/enforced: `authorized`,
- [ ] AC-07-073: Enumerated item is supported/enforced: `preimplementation_validated`,
- [ ] AC-07-074: Enumerated item is supported/enforced: `implementation_active`,
- [ ] AC-07-075: Enumerated item is supported/enforced: `implemented`,
- [ ] AC-07-076: Enumerated item is supported/enforced: `review_complete`,
- [ ] AC-07-077: Enumerated item is supported/enforced: `blocked`,
- [ ] AC-07-078: Enumerated item is supported/enforced: `deferred`,
- [ ] AC-07-079: Enumerated item is supported/enforced: `archived`.
- [ ] AC-07-080: Enumerated item is supported/enforced: title,
- [ ] AC-07-081: Enumerated item is supported/enforced: classification,
- [ ] AC-07-082: Enumerated item is supported/enforced: parent Plan reference and Plan slice reference when applicable,
- [ ] AC-07-083: Enumerated item is supported/enforced: intent fields,
- [ ] AC-07-084: Enumerated item is supported/enforced: ACs,
- [ ] AC-07-085: Enumerated item is supported/enforced: source/evidence metadata for source-derived ACs,
- [ ] AC-07-086: Enumerated item is supported/enforced: docs policy,
- [ ] AC-07-087: Enumerated item is supported/enforced: allowed file globs,
- [ ] AC-07-088: Enumerated item is supported/enforced: platform choice,
- [ ] AC-07-089: Enumerated item is supported/enforced: architecture decision references,
- [ ] AC-07-090: Enumerated item is supported/enforced: runtime baseline reference,
- [ ] AC-07-091: Enumerated item is supported/enforced: packet change baseline,
- [ ] AC-07-092: Enumerated item is supported/enforced: lifecycle approvals and authorization,
- [ ] AC-07-093: Enumerated item is supported/enforced: evidence,
- [ ] AC-07-094: Enumerated item is supported/enforced: backend verification records,
- [ ] AC-07-095: Enumerated item is supported/enforced: review traceability,
- [ ] AC-07-096: Enumerated item is supported/enforced: final claim audit.
- [ ] AC-07-097: Enumerated item is supported/enforced: Goal and ACs are required before AC approval.
- [ ] AC-07-098: Enumerated item is supported/enforced: AC approval is required before Work Packet approval except for explicit eligible Plan-child batch approval of non-source-derived ACs.
- [ ] AC-07-099: Enumerated item is supported/enforced: Work Packet approval is required before implementation authorization.
- [ ] AC-07-100: Enumerated item is supported/enforced: Implementation authorization and packet change baseline capture are one atomic governed action; PacketChangeBaseline capture must succeed before the authorization HumanDecision is recorded.
- [ ] AC-07-101: Enumerated item is supported/enforced: Pre-implementation validation is required before implementation source changes.
- [ ] AC-07-102: Enumerated item is supported/enforced: Approval is invalidated when approved title, parent Plan linkage, Plan slice linkage, intent, ACs, source evidence, approved scope fields such as allowed globs, classification, docs policy, platform, architecture, or runtime baseline reference changes. Scope deviations and docs requirements are review context unless included in an approved-field set.
- [ ] AC-07-103: Enumerated item is supported/enforced: Generic update actions must not silently change approved fields. If an update touches approved fields, Spec Guard must either reject it as a protected approved-field update or apply it and deterministically invalidate every dependent approval/authorization with diagnostics and next actions. The action result must list every invalidated decision.
- [ ] AC-07-104: Enumerated item is supported/enforced: `plan.update` must reject changes to Plan-approved fields. Because there is no persisted draft Plan state, an approved Plan cannot be moved back to draft by mutation. Changing approved Plan intent requires a new Plan or a registered Plan amendment action with its own review snapshot and Plan approval decision.
- [ ] AC-07-105: Enumerated item is supported/enforced: `children_created`,
- [ ] AC-07-106: Enumerated item is supported/enforced: `in_progress`,
- [ ] AC-07-107: Enumerated item is supported/enforced: `complete`,
- [ ] AC-07-108: Enumerated item is supported/enforced: id,
- [ ] AC-07-109: Enumerated item is supported/enforced: goal,
- [ ] AC-07-110: Enumerated item is supported/enforced: approved Plan proposal record,
- [ ] AC-07-111: Enumerated item is supported/enforced: child Work Packet references,
- [ ] AC-07-112: Enumerated item is supported/enforced: product/platform context,
- [ ] AC-07-113: Enumerated item is supported/enforced: status,
- [ ] AC-07-114: Enumerated item is supported/enforced: diagnostics.
- [ ] AC-07-115: Enumerated item is supported/enforced: `reusable_api`: reusable public API, SDK, library API, or stable callable contract,
- [ ] AC-07-116: Enumerated item is supported/enforced: `rest_api`: route, endpoint, service boundary, or network API,
- [ ] AC-07-117: Enumerated item is supported/enforced: `reusable_ui`: reusable UI component, UI package, public props/events/slots/styling/accessibility contract, or importable UI surface,
- [ ] AC-07-118: Enumerated item is supported/enforced: `one_off_application_ui`: application-specific UI behavior that is not reusable,
- [ ] AC-07-119: Enumerated item is supported/enforced: `direct_behavior`: non-API product behavior, scripts, internal behavior, or localized implementation behavior,
- [ ] AC-07-120: Enumerated item is supported/enforced: `operational_document`: documentation or operational content as the primary deliverable,
- [ ] AC-07-121: Enumerated item is supported/enforced: `bugfix`: correction of reported behavior.
- [ ] AC-07-122: Enumerated item is supported/enforced: `reusable_api`,
- [ ] AC-07-123: Enumerated item is supported/enforced: `rest_api`,
- [ ] AC-07-124: Enumerated item is supported/enforced: `reusable_ui`.
- [ ] AC-07-125: Enumerated item is supported/enforced: `required`: docs must exist and be linked to approved ACs before pre-implementation validation passes,
- [ ] AC-07-126: Enumerated item is supported/enforced: `changed`: docs are not required before pre-implementation validation, but docs must be updated and a `docs_updated` claim must pass backend verification before review completion,
- [ ] AC-07-127: Enumerated item is supported/enforced: `none_required`: docs are not required and `docs.none_required_reason` records why,
- [ ] AC-07-128: Enumerated item is supported/enforced: `not_applicable`: docs do not apply and `docs.not_applicable_reason` records why.
- [ ] AC-07-129: Enumerated item is supported/enforced: docs path is inside project,
- [ ] AC-07-130: Enumerated item is supported/enforced: docs exist,
- [ ] AC-07-131: Enumerated item is supported/enforced: docs link to approved AC IDs,
- [ ] AC-07-132: Enumerated item is supported/enforced: required backend verification for docs-to-AC mapping passed.
- [ ] AC-07-133: Table row is implemented: Action/outcome: `work.intake`; Status effect: creates `draft`
- [ ] AC-07-134: Table row is implemented: Action/outcome: `work.intent.draft` with at least one AC and required draft intent fields present; Status effect: `pending_ac_approval`
- [ ] AC-07-135: Table row is implemented: Action/outcome: `work.intent.draft` without ACs or with missing required draft intent fields; Status effect: `draft`
- [ ] AC-07-136: Table row is implemented: Action/outcome: `work.ac.approve` Yes; Status effect: `pending_packet_approval` unless packet approval is already batch-recorded
- [ ] AC-07-137: Table row is implemented: Action/outcome: `work.ac.approve` No; Status effect: `blocked` with decline diagnostics
- [ ] AC-07-138: Table row is implemented: Action/outcome: `work.approve` Yes; Status effect: `approved`
- [ ] AC-07-139: Table row is implemented: Action/outcome: `work.approve` No; Status effect: `blocked` with decline diagnostics
- [ ] AC-07-140: Table row is implemented: Action/outcome: `work.authorize` Yes and baseline capture succeeds; Status effect: `authorized`
- [ ] AC-07-141: Table row is implemented: Action/outcome: `work.authorize` No; Status effect: remains `approved` with authorization-declined diagnostics
- [ ] AC-07-142: Table row is implemented: Action/outcome: `work.authorize` failed PacketChangeBaseline capture; Status effect: remains `approved` with baseline-capture diagnostics and no authorization decision
- [ ] AC-07-143: Table row is implemented: Action/outcome: `work.preimplementation.validate` success; Status effect: `preimplementation_validated`
- [ ] AC-07-144: Table row is implemented: Action/outcome: `work.implementation.start` after preimplementation validation; Status effect: `implementation_active`
- [ ] AC-07-145: Table row is implemented: Action/outcome: `work.implementation.complete` after implementation evidence is recorded; Status effect: `implemented` until `work.review.complete`
- [ ] AC-07-146: Table row is implemented: Action/outcome: `work.review.complete` success; Status effect: `review_complete`
- [ ] AC-07-147: Table row is implemented: Action/outcome: archive action; Status effect: `archived`
- [ ] AC-07-148: Table row is implemented: Action/outcome: `plan.approve` Yes; Status effect: creates Plan with `approved`
- [ ] AC-07-149: Table row is implemented: Action/outcome: `plan.approve` No; Status effect: creates no Plan; stores standalone decline decision/audit
- [ ] AC-07-150: Table row is implemented: Action/outcome: `plan.child.create` creates first child; Status effect: `children_created`; created child starts `pending_ac_approval` when ACs exist and no batch approvals are recorded, otherwise `draft`
- [ ] AC-07-151: Table row is implemented: Action/outcome: `plan.batch_proceed` option 2/3/4 creates one or more children; Status effect: `children_created` or `in_progress` when any child is authorized/active
- [ ] AC-07-152: Table row is implemented: Action/outcome: child Work Packet starts implementation; Status effect: `in_progress`
- [ ] AC-07-153: Table row is implemented: Action/outcome: all non-archived child Work Packets reach `review_complete`; Status effect: `complete`
- [ ] AC-07-154: Table row is implemented: Action/outcome: blocking diagnostics prevent child creation or progress; Status effect: `blocked`
- [ ] AC-07-155: Table row is implemented: Action/outcome: `plan.archive`; Status effect: `archived`
