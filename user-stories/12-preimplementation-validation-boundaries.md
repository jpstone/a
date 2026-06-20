# US-12: Implementation boundary and pre-implementation validation

Derived from: [12. Implementation Boundary and Pre-Implementation Validation](../agentic-redesign-references.md#us-12-source)

## Problem

Spec Guard must prevent implementation source changes before required docs, tests, and failure-first evidence are established.

## User story

As a implementation agent, I want implementation boundary and pre-implementation validation implemented, so that spec Guard must prevent implementation source changes before required docs, tests, and failure-first evidence are established.

## In scope

- Classify file categories.
- Define allowed pre-implementation changes.
- Enforce docs/test/failure-first ordering.
- Handle test cleanup and side effects.
- Enforce allowed globs.
- Define validation chains for API, non-API, and operational-document packets.
- Wire docs-updated gate behavior.

## Out of scope

- Allowing implementation_source changes before required validation evidence.
- Counting pre-existing dirty docs/tests/evidence as packet evidence without re-recording.
- Permitting changes outside allowed globs without diagnostics.

## Acceptance criteria

<!-- Expanded from agentic-redesign.md to provide behavior-level coverage. -->

- [ ] AC-12-001: Spec Guard must classify changed paths into the canonical `ChangeFileCategory` enum using `Config.path_policy`.
- [ ] AC-12-002: The deterministic classifier normalizes each repository-relative path, rejects paths outside the project, ignores paths matching `ignored_paths`, then assigns the first matching category in this fixed precedence: `spec_guard_artifact_evidence`, `docs`, `tests`, `runtime_product_configuration`, `implementation_source`, `generated_build_output`.
- [ ] AC-12-003: use the same glob engine as allowed-globs validation.
- [ ] AC-12-004: Implementation source includes files that affect product behavior, public API, runtime behavior, UI behavior, business logic, persistence, integration behavior, or shipped assets.
- [ ] AC-12-005: For ordering gates, `runtime_product_configuration` is always treated as implementation-like and pre-failure changes to it block pre-implementation validation
- [ ] AC-12-006: Before implementation-ready state, allowed changes are limited to:
- [ ] AC-12-007: required docs,
- [ ] AC-12-008: Required governed docs, tests, and failure-first evidence for a packet must be recorded after packet change baseline capture to count for that packet's validation chain.
- [ ] AC-12-009: Pre-authorization docs/tests may exist, but they are treated as pre-existing project state unless re-recorded with evidence after authorization
- [ ] AC-12-010: they must not disappear from review traceability by being silently absorbed into the packet baseline.
- [ ] AC-12-011: Implementation source changes before proven failure-first evidence must block pre-implementation validation.
- [ ] AC-12-012: Docs, test failure, test pass, and runtime evidence records must include a file state snapshot captured by Spec Guard during the evidence action.
- [ ] AC-12-013: The snapshot must be sufficient to compare changed files against the packet change baseline and prove whether implementation source had changed before failure-first evidence.
- [ ] AC-12-014: Evidence without the required file state snapshot cannot satisfy pre-implementation or review gates.
- [ ] AC-12-015: Command-backed evidence must reference a kernel-created CommandResult from `command.run`.
- [ ] AC-12-016: Frontend agents must not supply exit codes, command status, command timestamps, or command output as trusted facts.
- [ ] AC-12-017: Evidence actions may accept paths, related AC IDs, summaries, and claim text from the frontend agent, but command, exit code, timing, status, and output references used as governed evidence must come from the deterministic kernel.
- [ ] AC-12-018: and `skipped` may be recorded only for a deterministic precondition skip requested by `command.run`.
- [ ] AC-12-019: Evidence status is derived from CommandResult status as follows: `passed` maps to evidence `passed`
- [ ] AC-12-020: CommandResults with `exit_code: null`, spawn errors, missing executables, permission errors, signal termination, `timed_out`, or `skipped` cannot satisfy required failure-first, passing-test, or runtime evidence gates.
- [ ] AC-12-021: Mode `production` requires CommandResult purpose `runtime_production`
- [ ] AC-12-022: creates EvidenceRecord type `runtime_production`.
- [ ] AC-12-023: Mode `development` requires CommandResult purpose `runtime_development`
- [ ] AC-12-024: creates EvidenceRecord type `runtime_development`.
- [ ] AC-12-025: Evidence actions must reject a CommandResult whose purpose is incompatible with the evidence type.
- [ ] AC-12-026: Build commands may be recorded as CommandResults for baseline or review context, but they do not satisfy behavior test failure/pass evidence unless separately paired with compatible test evidence.
- [ ] AC-12-027: Frontend agents must not supply file state snapshots as trusted inputs.
- [ ] AC-12-028: They may supply paths and summaries, but Spec Guard must capture VCS or manifest state itself before committing the evidence record.
- [ ] AC-12-029: `work.implementation.complete` must register at least one `implementation_summary` claim from its submitted summary and implementation file list.
- [ ] AC-12-030: Review completion cannot pass until that claim is validated or superseded through `work.claims.create`/`work.claims.validate` with evidence-backed final claims.
- [ ] AC-12-031: Tests must be cleanup-safe.
- [ ] AC-12-032: Retained tests must not test documentation text, documentation formatting, documentation files, headings, examples, or links.
- [ ] AC-12-033: Documentation itself is never governed by retained tests.
- [ ] AC-12-034: Deterministic retained-doc-test detection is byte/string based and language-independent: a retained test is flagged when its path also matches a docs glob, when its path matches `Config.path_policy.docs_test_manifests`, or when its UTF-8-decoded content contains an exact normalized docs/content path token from docs evidence/path policy together with one of these case-sensitive operation tokens in the same file: `readFile`, `readFileSync`, `open`, `openSync`, `import`, `require`, `fetch`, `assert`, `expect`, `should`, `toContain`, `toMatch`.
- [ ] AC-12-035: A retained test is also flagged when it contains exact known docs heading/link/example tokens captured in docs EvidenceRecords and any assertion token from the list above.
- [ ] AC-12-036: Non-UTF-8 test files or suspected documentation-targeting behavior not caught by these deterministic rules require backend verification of a `retained_test_not_docs` claim before review completion.
- [ ] AC-12-037: Passing or failing test evidence must not leave persistent artifacts, generated files, database tables, database rows, external resources, orphan processes, modified runtime state, or other side effects unless those changes are explicitly approved as part of the product change.
- [ ] AC-12-038: Any temporary artifacts/resources created during tests must be cleaned up by the test or test harness.
- [ ] AC-12-039: Database-backed tests must isolate state and clean up records, tables, rows, indexes, queues, buckets, messages, or external resources they create unless the approved AC explicitly requires persistent seed/schema changes.
- [ ] AC-12-040: Cleanup verification is recorded through `work.evidence.cleanup`.
- [ ] AC-12-041: For test/runtime commands with non-empty `resource_categories`, `command.run` must capture configured cleanup observer before-observations immediately before spawning the command and after-observations immediately after command completion/timeout/termination,
- [ ] AC-12-042: store them on the CommandResult.
- [ ] AC-12-043: Checked resource categories may be requested by the caller, but before/after observations and side-effect status must be kernel-captured, command-backed, or derived from deterministic evidence records.
- [ ] AC-12-044: Caller-supplied cleanup summaries are claims only and cannot establish cleanup truth.
- [ ] AC-12-045: Cleanup records must store checked resource categories, kernel-captured before/after observations or CommandResult refs, side-effect status derived by the kernel, related command/evidence refs, and any remaining cleanup actions.
- [ ] AC-12-046: The `files` observer records a manifest of project-relative paths, sizes, mtimes, and content hashes under allowed temp/output/resource paths before and after the command
- [ ] AC-12-047: comparison rule `no_new_resources` passes only when no unapproved new or modified paths remain.
- [ ] AC-12-048: The `processes` observer records child process ids, command lines,
- [ ] AC-12-049: start times for processes spawned by the command process tree
- [ ] AC-12-050: it passes only when no spawned process remains alive after cleanup.
- [ ] AC-12-051: Other resource categories such as databases, queues, buckets, services, or external resources require configured command-backed observers in `Config.cleanup_observers`.
- [ ] AC-12-052: A cleanup observer must define resource category, identity fields, before command or deterministic capture method, after command or deterministic capture method, and comparison rule.
- [ ] AC-12-053: Cleanup applicability is determined only from structured `resource_categories` fields on CleanupEvidence, NotApplicableEvidence, EvidenceRecord cleanup records, failure/pass/runtime evidence records, and final claims
- [ ] AC-12-054: Spec Guard stores them as structured claims
- [ ] AC-12-055: uses exact string equality for cleanup applicability.
- [ ] AC-12-056: Cleanup evidence must provide the checked `resource_categories` explicitly, and configured observers decide whether those categories are clean.
- [ ] AC-12-057: Without a configured observer, a non-file/process resource category can be marked cleanup not applicable only when no structured record lists that exact resource category string.
- [ ] AC-12-058: If any approved or deterministic record lists the category and no observer exists, cleanup is blocked with diagnostics requiring observer configuration or human-approved scope change.
- [ ] AC-12-059: When tests or failure-first evidence are not applicable, the not-applicable decision is recorded through `work.evidence.not_applicable`.
- [ ] AC-12-060: It must identify the evidence type being marked not applicable, the reason, the classification/policy that permits it, and the approved ACs or scope it applies to.
- [ ] AC-12-061: Evidence type `tests` is a single deterministic not-applicable record that covers both retained passing tests and failure-first test evidence
- [ ] AC-12-062: otherwise implementations may record separate `test_failure` and `test_pass` not-applicable records.
- [ ] AC-12-063: `work.evidence.not_applicable` must not bypass evidence gates by assertion alone.
- [ ] AC-12-064: It can record tests or failure-first not applicable only when deterministic eligibility is established by classification, approved docs/content policy, and the validation chain in this specification.
- [ ] AC-12-065: It can record `implementation_files` not applicable only when changed-file classification since PacketChangeBaseline contains no `implementation_source` or `runtime_product_configuration` files and the packet classification/policy is documentation/content-only.
- [ ] AC-12-066: Human confirmation alone must not make tests or failure-first evidence not applicable for product/API/runtime behavior packets.
- [ ] AC-12-067: Human confirmation may be required to record awareness of an eligible not-applicable decision, but it cannot override deterministic ineligibility.
- [ ] AC-12-068: Review completion must block when tests leave behind unapproved files, data, processes, external resources, or runtime state.
- [ ] AC-12-069: Allowed globs apply to product-scope changed files:
- [ ] AC-12-070: Spec Guard artifact/evidence paths are exempt from allowed-globs blocking, but they must still be tracked and audited.
- [ ] AC-12-071: changes through symlinks are attributed to the resolved repository-relative path when inside the project, and rejected when they resolve outside the project.
- [ ] AC-12-072: Case sensitivity follows the packet change baseline mode: VCS mode uses the VCS-reported path identity
- [ ] AC-12-073: manifest mode records exact path strings and treats them as case-sensitive.
- [ ] AC-12-074: Glob matching uses `/` separators, `*` for a single path segment fragment, `**` for zero or more path segments, and `?` for one character within a segment.
- [ ] AC-12-075: Negated globs are not supported unless a future schema explicitly adds them.
- [ ] AC-12-076: must not be absolute or contain `..` after normalization.
- [ ] AC-12-077: Other/unexpected files are never silently allowed.
- [ ] AC-12-078: They require diagnostics and explicit resolution.
- [ ] AC-12-079: Deterministic checks must validate:
- [ ] AC-12-080: docs were recorded before behavior tests that claim to validate the documented contract,
- [ ] AC-12-081: retained tests do not test documentation files or documentation text,
- [ ] AC-12-082: command result is recorded,
- [ ] AC-12-083: product-scope changed files are within allowed globs.
- [ ] AC-12-084: Required backend verification for the full API/contract-surface chain must pass for:
- [ ] AC-12-085: docs-updated semantic claim when docs are added, changed, or required by policy,
- [ ] AC-12-086: failure evidence semantic claim when the failure is used to prove missing approved behavior.
- [ ] AC-12-087: For pre-implementation validation, docs existence, docs-to-AC mapping, behavior-test mapping, and failure-evidence requirements above must already be satisfied, but `docs_updated` follows section 12.8 and may remain pending until review completion.
- [ ] AC-12-088: For non-API packets with docs policy `required`:
- [ ] AC-12-089: For non-API packets without required docs:
- [ ] AC-12-090: required docs exist when docs policy is `required`,
- [ ] AC-12-091: required docs are linked to approved AC IDs when docs policy is `required`,
- [ ] AC-12-092: required docs were recorded before behavior tests that claim to validate the documented contract,
- [ ] AC-12-093: Required backend verification for the full non-API chain must pass for:
- [ ] AC-12-094: docs-to-AC mapping when docs policy is `required`,
- [ ] AC-12-095: docs-updated semantic claim when docs policy is `required`, docs policy is `changed`, docs policy changed during the packet lifecycle, or docs files changed,
- [ ] AC-12-096: behavior-tests-to-documented-contract mapping when docs policy is `required`,
- [ ] AC-12-097: For pre-implementation validation, docs existence, docs-to-AC mapping when required, behavior-test mapping when required, tests-to-AC mapping, and failure-evidence requirements above must already be satisfied, but `docs_updated` follows section 12.8 and may remain pending until review completion.
- [ ] AC-12-098: test/failure-first not-applicable reason is recorded,
- [ ] AC-12-099: no retained tests were added for documentation text/files,
- [ ] AC-12-100: Required backend verification must pass for:
- [ ] AC-12-101: docs-updated semantic claim.
- [ ] AC-12-102: If an operational-document packet changes product behavior, runtime behavior, API behavior, schema, persistence, or shipped application code, this documentation-only chain is invalid.
- [ ] AC-12-103: Spec Guard must require a registered `docs_updated` claim and passed backend verification before review completion when any of these conditions are true:
- [ ] AC-12-104: docs policy is `required`,
- [ ] AC-12-105: docs evidence was added or updated.
- [ ] AC-12-106: For docs policy `required`, pre-implementation validation must also require docs existence, docs-to-AC traceability, and any required docs-to-AC backend verification before implementation source changes.
- [ ] AC-12-107: The `docs_updated` claim may pass at pre-implementation time or later, but review completion must block until it passes.
- [ ] AC-12-108: For docs policy `changed`, docs evidence identifying the updated docs/content paths must exist before review completion.
- [ ] AC-12-109: The docs do not need to precede tests unless another rule requires that ordering, but the `docs_updated` claim must pass before review completion.
- [ ] AC-12-110: Enumerated item is supported/enforced: Spec Guard artifacts/evidence,
- [ ] AC-12-111: Enumerated item is supported/enforced: required docs,
- [ ] AC-12-112: Enumerated item is supported/enforced: tests intended to fail against missing approved behavior.
- [ ] AC-12-113: Enumerated item is supported/enforced: docs,
- [ ] AC-12-114: Enumerated item is supported/enforced: tests,
- [ ] AC-12-115: Enumerated item is supported/enforced: implementation source,
- [ ] AC-12-116: Enumerated item is supported/enforced: runtime/product configuration,
- [ ] AC-12-117: Enumerated item is supported/enforced: generated build output when tracked or submitted as evidence.
- [ ] AC-12-118: Enumerated item is supported/enforced: Paths are normalized to repository-relative POSIX-style paths using `/` separators.
- [ ] AC-12-119: Enumerated item is supported/enforced: Absolute paths and paths containing `..` after normalization are invalid as governed paths.
- [ ] AC-12-120: Enumerated item is supported/enforced: Symlink paths are resolved for classification; changes through symlinks are attributed to the resolved repository-relative path when inside the project, and rejected when they resolve outside the project.
- [ ] AC-12-121: Enumerated item is supported/enforced: Case sensitivity follows the packet change baseline mode: VCS mode uses the VCS-reported path identity; manifest mode records exact path strings and treats them as case-sensitive.
- [ ] AC-12-122: Enumerated item is supported/enforced: Glob matching uses `/` separators, `*` for a single path segment fragment, `**` for zero or more path segments, and `?` for one character within a segment.
- [ ] AC-12-123: Enumerated item is supported/enforced: Negated globs are not supported unless a future schema explicitly adds them.
- [ ] AC-12-124: Enumerated item is supported/enforced: Glob patterns are repository-relative and must not be absolute or contain `..` after normalization.
- [ ] AC-12-125: Enumerated item is supported/enforced: AC approval exists,
- [ ] AC-12-126: Enumerated item is supported/enforced: docs exist and are linked to approved AC IDs,
- [ ] AC-12-127: Enumerated item is supported/enforced: docs were recorded before behavior tests that claim to validate the documented contract,
- [ ] AC-12-128: Enumerated item is supported/enforced: tests exist and are real test paths,
- [ ] AC-12-129: Enumerated item is supported/enforced: retained tests do not test documentation files or documentation text,
- [ ] AC-12-130: Enumerated item is supported/enforced: failure evidence exists,
- [ ] AC-12-131: Enumerated item is supported/enforced: command result is recorded,
- [ ] AC-12-132: Enumerated item is supported/enforced: implementation source did not change before failure-first evidence,
- [ ] AC-12-133: Enumerated item is supported/enforced: product-scope changed files are within allowed globs.
- [ ] AC-12-134: Enumerated item is supported/enforced: docs-to-AC mapping,
- [ ] AC-12-135: Enumerated item is supported/enforced: docs-updated semantic claim when docs are added, changed, or required by policy,
- [ ] AC-12-136: Enumerated item is supported/enforced: behavior-tests-to-documented-contract mapping,
- [ ] AC-12-137: Enumerated item is supported/enforced: failure evidence semantic claim when the failure is used to prove missing approved behavior.
- [ ] AC-12-138: Enumerated item is supported/enforced: required docs exist when docs policy is `required`,
- [ ] AC-12-139: Enumerated item is supported/enforced: required docs are linked to approved AC IDs when docs policy is `required`,
- [ ] AC-12-140: Enumerated item is supported/enforced: required docs were recorded before behavior tests that claim to validate the documented contract,
- [ ] AC-12-141: Enumerated item is supported/enforced: docs-to-AC mapping when docs policy is `required`,
- [ ] AC-12-142: Enumerated item is supported/enforced: docs-updated semantic claim when docs policy is `required`, docs policy is `changed`, docs policy changed during the packet lifecycle, or docs files changed,
- [ ] AC-12-143: Enumerated item is supported/enforced: behavior-tests-to-documented-contract mapping when docs policy is `required`,
- [ ] AC-12-144: Enumerated item is supported/enforced: tests-to-AC mapping,
- [ ] AC-12-145: Enumerated item is supported/enforced: docs/content paths are inside project,
- [ ] AC-12-146: Enumerated item is supported/enforced: docs/content files exist,
- [ ] AC-12-147: Enumerated item is supported/enforced: changed files are limited to approved docs/content paths and Spec Guard artifacts/evidence,
- [ ] AC-12-148: Enumerated item is supported/enforced: test/failure-first not-applicable reason is recorded,
- [ ] AC-12-149: Enumerated item is supported/enforced: no retained tests were added for documentation text/files,
- [ ] AC-12-150: Enumerated item is supported/enforced: no implementation source changed.
- [ ] AC-12-151: Enumerated item is supported/enforced: docs/content-to-AC mapping,
- [ ] AC-12-152: Enumerated item is supported/enforced: docs-updated semantic claim.
- [ ] AC-12-153: Enumerated item is supported/enforced: docs policy is `required`,
- [ ] AC-12-154: Enumerated item is supported/enforced: docs policy is `changed`,
- [ ] AC-12-155: Enumerated item is supported/enforced: docs policy changed after Work Packet approval,
- [ ] AC-12-156: Enumerated item is supported/enforced: docs/content files changed in the packet diff,
- [ ] AC-12-157: Enumerated item is supported/enforced: docs evidence was added or updated.
- [ ] AC-12-158: Table row is implemented: Evidence action/type: `work.evidence.failure` with failure-first role; Allowed CommandResult purpose: `test`
- [ ] AC-12-159: Table row is implemented: Evidence action/type: `work.evidence.pass` with passing-test role; Allowed CommandResult purpose: `test`
- [ ] AC-12-160: Table row is implemented: Evidence action/type: `work.evidence.runtime` production; Allowed CommandResult purpose: `runtime_production`
- [ ] AC-12-161: Table row is implemented: Evidence action/type: `work.evidence.runtime` development; Allowed CommandResult purpose: `runtime_development`
- [ ] AC-12-162: Table row is implemented: Evidence action/type: Runtime baseline validation evidence; Allowed CommandResult purpose: `test`, `build`, `runtime_production`, `runtime_development` as applicable
