# US-14: Runtime evidence, review completion, and final claims

Derived from: [14. Runtime, Review, and Final Claims](../agentic-redesign-references.md#us-14-source)

## Problem

Implemented work needs runtime evidence, review completion, and final claims that are backed by recorded artifacts instead of unsupported summaries.

## User story

As a reviewer, I want runtime evidence, review completion, and final claims implemented, so that implemented work needs runtime evidence, review completion, and final claims that are backed by recorded artifacts instead of unsupported summaries.

## In scope

- Record runtime evidence.
- Complete review only when required checks and evidence are valid.
- Validate final claims against evidence and governed state.

## Out of scope

- Final responses that claim unrecorded tests or behavior.
- Review completion when approvals or pre-implementation validation are stale.

## Acceptance criteria

<!-- Expanded from agentic-redesign.md to provide behavior-level coverage. -->

- [ ] AC-14-001: Runtime evidence must distinguish:
- [ ] AC-14-002: Production claims require production evidence.
- [ ] AC-14-003: Development/HMR/full-stack development claims require development evidence for exact command and validated paths.
- [ ] AC-14-004: If work requires frontend and backend processes for development use, evidence must show one documented command or orchestrated entry point starts the full required development runtime.
- [ ] AC-14-005: Review completion requires, when applicable to the packet classification and evidence policy:
- [ ] AC-14-006: implementation files, or an approved/not-applicable reason for documentation-only or other no-implementation paths,
- [ ] AC-14-007: required backend verification records,
- [ ] AC-14-008: Review cannot complete while required traceability is empty or unsupported.
- [ ] AC-14-009: AC verification at review completion means each approved AC is either linked to passing governed evidence, linked to an approved deterministic not-applicable evidence record where not-applicable is permitted, or explicitly reported as unsupported so review completion blocks.
- [ ] AC-14-010: For behavior/API/runtime ACs, evidence must include kernel-created command results and required backend verification.
- [ ] AC-14-011: For operational-document documentation-only ACs, evidence must include docs/content records and required docs/content-to-AC verification.
- [ ] AC-14-012: Final user-facing claims must be supported by recorded evidence or explicitly marked unverified.
- [ ] AC-14-013: Claims presented as verified, completed, implemented, working, tested, or validated require backend verification against evidence and approved references used only as immutable constraints.
- [ ] AC-14-014: Claims explicitly marked unverified do not require semantic support verification, but deterministic validation must ensure they are clearly labeled as unverified
- [ ] AC-14-015: are not used to satisfy review completion, AC verification, runtime validation, or implementation success.
- [ ] AC-14-016: A final response may include unverified claims only as caveats or limitations.
- [ ] AC-14-017: The verifier must not criticize or reinterpret approved human intent.
- [ ] AC-14-018: Enumerated item is supported/enforced: production runtime evidence,
- [ ] AC-14-019: Enumerated item is supported/enforced: development runtime evidence.
- [ ] AC-14-020: Enumerated item is supported/enforced: implementation files, or an approved/not-applicable reason for documentation-only or other no-implementation paths,
- [ ] AC-14-021: Enumerated item is supported/enforced: test files, or deterministic not-applicable evidence where tests are permitted to be not applicable,
- [ ] AC-14-022: Enumerated item is supported/enforced: changed files from packet change baseline,
- [ ] AC-14-023: Enumerated item is supported/enforced: AC verification,
- [ ] AC-14-024: Enumerated item is supported/enforced: docs status,
- [ ] AC-14-025: Enumerated item is supported/enforced: feature/source evidence status,
- [ ] AC-14-026: Enumerated item is supported/enforced: cleanup status,
- [ ] AC-14-027: Enumerated item is supported/enforced: test cleanup verification showing no unapproved files, database tables/rows, external resources, processes, or runtime state were left behind,
- [ ] AC-14-028: Enumerated item is supported/enforced: runtime evidence where applicable,
- [ ] AC-14-029: Enumerated item is supported/enforced: required backend verification records,
- [ ] AC-14-030: Enumerated item is supported/enforced: final claim audit.
