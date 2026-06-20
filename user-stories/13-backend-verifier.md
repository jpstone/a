# US-13: Backend verifier

Derived from: [13. Backend Verifier](../agentic-redesign-references.md#us-13-source)

## Problem

Required semantic frontend-agent claims need backend verification while preserving human authority and deterministic-kernel ownership.

## User story

As a verification integrator, I want backend verifier implemented, so that required semantic frontend-agent claims need backend verification while preserving human authority and deterministic-kernel ownership.

## In scope

- Support adapter modes.
- Register frontend-agent claims.
- Enforce verification requirement matrix.
- Manage verifier configuration and health.
- Constrain verifier task and response schemas.

## Out of scope

- Verifier mutating product intent or lifecycle decisions.
- Verifier approving/rejecting work or judging human-approved ACs/scope/platform/architecture.
- Replacing deterministic validation with model judgment.

## Acceptance criteria

<!-- Expanded from agentic-redesign.md to provide behavior-level coverage. -->

- [ ] AC-13-001: Spec Guard must support:
- [ ] AC-13-002: HTTP endpoint adapter, optional unless implemented and exposed.
- [ ] AC-13-003: Provider/model adapter, optional unless implemented and exposed.
- [ ] AC-13-004: Test fixture adapter for Spec Guard's own tests only.
- [ ] AC-13-005: The local command adapter is the minimum required executable adapter.
- [ ] AC-13-006: The first required concrete local command adapter is the Pi headless RPC command adapter.
- [ ] AC-13-007: If an adapter mode is selectable/configurable, it must actually execute verification tasks and pass health checks.
- [ ] AC-13-008: Spec Guard must not collect HTTP or provider/model configuration as usable when that adapter cannot be invoked.
- [ ] AC-13-009: Required semantic verification blocks if no healthy executable adapter is configured.
- [ ] AC-13-010: Required backend verification operates on registered claims.
- [ ] AC-13-011: Spec Guard must create or derive stable claim IDs before calling the verifier.
- [ ] AC-13-012: `review.claims` is only the review/final subset or references into that registry.
- [ ] AC-13-013: Docs evidence actions register docs-to-AC mapping claims when docs are required.
- [ ] AC-13-014: Docs evidence actions register docs-updated semantic claims when docs are required, docs policy is `changed`, docs policy changes, docs evidence is added or updated, or docs files are changed.
- [ ] AC-13-015: `work.docs.add`, `work.docs.update`, and docs-policy changes through `work.update` must register or update stable pending `docs_updated` claims for affected docs/ACs.
- [ ] AC-13-016: `work.preimplementation.validate`, `work.review.validate`, and `work.review.complete` must deterministically detect docs/content file changes and docs policy triggers.
- [ ] AC-13-017: If a required `docs_updated` claim is missing, mutating actions may register a stable pending claim
- [ ] AC-13-018: non-mutating actions must return the derived pending claim data and a blocking next action.
- [ ] AC-13-019: Direct docs/content file changes without docs evidence do not satisfy docs-updated requirements.
- [ ] AC-13-020: Test failure/pass evidence actions register tests-to-AC claims and, when docs are required, behavior-tests-to-documented-contract claims.
- [ ] AC-13-021: Failure evidence actions register failure-evidence semantic claims when failure-first evidence is required.
- [ ] AC-13-022: Review submission records register implementation summary claims.
- [ ] AC-13-023: Registered claims must include claim id, text, claim type, related AC IDs, related docs IDs when applicable, and evidence refs.
- [ ] AC-13-024: `work.backend.verify` must reject unknown claim IDs.
- [ ] AC-13-025: Behavior-tests-to-documented-contract verification means semantic verification that retained behavior tests exercise the product/API/runtime contract described by the docs.
- [ ] AC-13-026: It never means testing documentation files, documentation text, headings, links, formatting, examples, or other documentation content directly.
- [ ] AC-13-027: Optional advisory verification may exist, but optional verification must not block or pass gates unless a requirement in this table applies.
- [ ] AC-13-028: Only executable adapters may be presented as normal choices.
- [ ] AC-13-029: Command adapter config must collect:
- [ ] AC-13-030: The required first command adapter kind is `pi_headless_rpc`.
- [ ] AC-13-031: Implementations must allow provider/model override.
- [ ] AC-13-032: A non-thinking authenticated model such as `github-copilot` / `gpt-4.1` may be configured, but the adapter must work with thinking-capable models by filtering RPC events rather than relying on model choice.
- [ ] AC-13-033: Implemented HTTP adapter config must collect:
- [ ] AC-13-034: Implemented provider/model adapter config must collect:
- [ ] AC-13-035: Secrets must not be stored directly.
- [ ] AC-13-036: validates response shape.
- [ ] AC-13-037: Health failure blocks required semantic verification.
- [ ] AC-13-038: Stderr is diagnostic-only
- [ ] AC-13-039: must not be parsed as verifier output.
- [ ] AC-13-040: must still pass schema validation.
- [ ] AC-13-041: Timeout terminates the adapter process, records verifier health failure for that run, and satisfies no gate.
- [ ] AC-13-042: The task JSON must include task id, schema version, submitted claim ids/text, deterministic evidence refs, human-approved refs, and prohibited judgment rules.
- [ ] AC-13-043: The response JSON must use the schema in section 13.5.
- [ ] AC-13-044: Start Pi as a managed child process with `pi --mode rpc --no-session --no-tools --provider <provider> --model <model>`.
- [ ] AC-13-045: Record process metadata under Spec Guard runtime storage
- [ ] AC-13-046: expose deterministic start/status/prompt/stop lifecycle controls.
- [ ] AC-13-047: Concurrent prompts must fail with a deterministic busy error.
- [ ] AC-13-048: Collect only `message_update` events where `assistantMessageEvent.type` is `text_delta`
- [ ] AC-13-049: Ignore and never expose `thinking_start`, `thinking_delta`, `thinking_end`, encrypted thinking signatures, partial thinking content, raw event streams, or tool events in adapter output.
- [ ] AC-13-050: Return a compact JSON envelope with adapter id, Pi provider/model, final text, optional parsed JSON, diagnostics, and no hidden reasoning.
- [ ] AC-13-051: Health check sends a minimal prompt such as `Reply with only the answer, no explanation: 1+1?` and expects final text `2` before `agent_end`.
- [ ] AC-13-052: The adapter is advisory verification infrastructure only
- [ ] AC-13-053: it must not bypass Spec Guard human gates, deterministic checks, or approval semantics.
- [ ] AC-13-054: Verifier task input must separate:
- [ ] AC-13-055: Verifier response must include:
- [ ] AC-13-056: Each finding must target one of:
- [ ] AC-13-057: A finding targeting `human_approved_reference` is valid only when it says an agent claim conflicts with, exceeds, or lacks support from that reference.
- [ ] AC-13-058: `failed` means at least one submitted claim id is in `contradicted_claim_ids`, or an error finding reports that a required claim is false or unsupported by the provided deterministic evidence.
- [ ] AC-13-059: The kernel must not parse free-text `message` to infer prohibited judgment.
- [ ] AC-13-060: Instead, it validates `finding_kind`, `target_type`, and `prohibited_human_intent_judgment`: a finding targeting `human_approved_reference` is valid only with finding kind `claim_conflicts_with_reference`, `claim_exceeds_reference`, or `claim_unsupported_by_reference`
- [ ] AC-13-061: The deterministic kernel must mark a verifier response invalid when:
- [ ] AC-13-062: required fields are missing,
- [ ] AC-13-063: verified/unverified/contradicted claim ID sets are not pairwise disjoint,
- [ ] AC-13-064: for `passed`, `failed`, or `inconclusive` responses, the union of verified, unverified, and contradicted claim IDs is not exactly the submitted claim ID set,
- [ ] AC-13-065: invalid responses include verified, unverified, or contradicted claim IDs outside the submitted set,
- [ ] AC-13-066: a claim is omitted from all three sets on a non-invalid response,
- [ ] AC-13-067: response attempts to approve, reject, defer, change, or reinterpret human intent.
- [ ] AC-13-068: Ordered requirement is supported/enforced: Disabled.
- [ ] AC-13-069: Ordered requirement is supported/enforced: Local command adapter.
- [ ] AC-13-070: Ordered requirement is supported/enforced: HTTP endpoint adapter, optional unless implemented and exposed.
- [ ] AC-13-071: Ordered requirement is supported/enforced: Provider/model adapter, optional unless implemented and exposed.
- [ ] AC-13-072: Ordered requirement is supported/enforced: Test fixture adapter for Spec Guard's own tests only.
- [ ] AC-13-073: Enumerated item is supported/enforced: Docs evidence actions register docs-to-AC mapping claims when docs are required.
- [ ] AC-13-074: Enumerated item is supported/enforced: Docs evidence actions register docs-updated semantic claims when docs are required, docs policy is `changed`, docs policy changes, docs evidence is added or updated, or docs files are changed.
- [ ] AC-13-075: Enumerated item is supported/enforced: `work.docs.add`, `work.docs.update`, and docs-policy changes through `work.update` must register or update stable pending `docs_updated` claims for affected docs/ACs.
- [ ] AC-13-076: Enumerated item is supported/enforced: `work.preimplementation.validate`, `work.review.validate`, and `work.review.complete` must deterministically detect docs/content file changes and docs policy triggers. If a required `docs_updated` claim is missing, mutating actions may register a stable pending claim; non-mutating actions must return the derived pending claim data and a blocking next action. Direct docs/content file changes without docs evidence do not satisfy docs-updated requirements.
- [ ] AC-13-077: Enumerated item is supported/enforced: Test failure/pass evidence actions register tests-to-AC claims and, when docs are required, behavior-tests-to-documented-contract claims.
- [ ] AC-13-078: Enumerated item is supported/enforced: Failure evidence actions register failure-evidence semantic claims when failure-first evidence is required.
- [ ] AC-13-079: Enumerated item is supported/enforced: Runtime evidence actions register runtime claims for any semantic runtime assertion beyond exact command/path/status existence.
- [ ] AC-13-080: Enumerated item is supported/enforced: Review submission records register implementation summary claims.
- [ ] AC-13-081: Enumerated item is supported/enforced: Final claim validation registers final user-facing claims, including whether each is presented as verified or explicitly unverified.
- [ ] AC-13-082: Ordered requirement is supported/enforced: Configure backend verifier now
- [ ] AC-13-083: Ordered requirement is supported/enforced: Leave disabled for now
- [ ] AC-13-084: Ordered requirement is supported/enforced: Discuss
- [ ] AC-13-085: Enumerated item is supported/enforced: adapter kind,
- [ ] AC-13-086: Enumerated item is supported/enforced: command,
- [ ] AC-13-087: Enumerated item is supported/enforced: arguments,
- [ ] AC-13-088: Enumerated item is supported/enforced: working directory behavior,
- [ ] AC-13-089: Enumerated item is supported/enforced: timeout,
- [ ] AC-13-090: Enumerated item is supported/enforced: environment/secret setup confirmation,
- [ ] AC-13-091: Enumerated item is supported/enforced: provider/model fields when the adapter kind manages a model process.
- [ ] AC-13-092: Enumerated item is supported/enforced: endpoint,
- [ ] AC-13-093: Enumerated item is supported/enforced: auth mechanism or credential environment variable names,
- [ ] AC-13-094: Enumerated item is supported/enforced: data-sharing policy.
- [ ] AC-13-095: Enumerated item is supported/enforced: provider name,
- [ ] AC-13-096: Enumerated item is supported/enforced: model name,
- [ ] AC-13-097: Enumerated item is supported/enforced: credential environment variable name,
- [ ] AC-13-098: Ordered requirement is supported/enforced: Spec Guard executes the configured command with configured arguments and working directory.
- [ ] AC-13-099: Ordered requirement is supported/enforced: The verifier task is written as one UTF-8 JSON object to stdin, followed by LF.
- [ ] AC-13-100: Ordered requirement is supported/enforced: The adapter writes exactly one UTF-8 JSON verifier response object to stdout. Additional stdout after the first complete JSON object is invalid.
- [ ] AC-13-101: Ordered requirement is supported/enforced: Stderr is diagnostic-only and must not be parsed as verifier output.
- [ ] AC-13-102: Ordered requirement is supported/enforced: Exit code `0` means a response was produced and must still pass schema validation. Non-zero exit code means adapter failure and no gate is satisfied, even if stdout contains JSON.
- [ ] AC-13-103: Ordered requirement is supported/enforced: Timeout terminates the adapter process, records verifier health failure for that run, and satisfies no gate.
- [ ] AC-13-104: Ordered requirement is supported/enforced: The task JSON must include task id, schema version, submitted claim ids/text, deterministic evidence refs, human-approved refs, and prohibited judgment rules. The response JSON must use the schema in section 13.5.
- [ ] AC-13-105: Ordered requirement is supported/enforced: Start Pi as a managed child process with `pi --mode rpc --no-session --no-tools --provider <provider> --model <model>`.
- [ ] AC-13-106: Ordered requirement is supported/enforced: Default `provider` is `openai-codex`; default `model` is `gpt-5.4-mini`.
- [ ] AC-13-107: Ordered requirement is supported/enforced: Record process metadata under Spec Guard runtime storage and expose deterministic start/status/prompt/stop lifecycle controls.
- [ ] AC-13-108: Ordered requirement is supported/enforced: Accept one prompt at a time. Concurrent prompts must fail with a deterministic busy error.
- [ ] AC-13-109: Ordered requirement is supported/enforced: Send prompts to Pi RPC as strict JSONL using LF framing: `{ "type": "prompt", "message": "..." }`.
- [ ] AC-13-110: Ordered requirement is supported/enforced: Collect only `message_update` events where `assistantMessageEvent.type` is `text_delta`; concatenate their `delta` strings until `agent_end`.
- [ ] AC-13-111: Ordered requirement is supported/enforced: Ignore and never expose `thinking_start`, `thinking_delta`, `thinking_end`, encrypted thinking signatures, partial thinking content, raw event streams, or tool events in adapter output.
- [ ] AC-13-112: Ordered requirement is supported/enforced: Return a compact JSON envelope with adapter id, Pi provider/model, final text, optional parsed JSON, diagnostics, and no hidden reasoning.
- [ ] AC-13-113: Ordered requirement is supported/enforced: Health check sends a minimal prompt such as `Reply with only the answer, no explanation: 1+1?` and expects final text `2` before `agent_end`.
- [ ] AC-13-114: Ordered requirement is supported/enforced: The adapter is advisory verification infrastructure only; it must not bypass Spec Guard human gates, deterministic checks, or approval semantics.
- [ ] AC-13-115: Enumerated item is supported/enforced: claim IDs and claim text,
- [ ] AC-13-116: Enumerated item is supported/enforced: deterministic evidence,
- [ ] AC-13-117: Enumerated item is supported/enforced: human-approved references as immutable constraints,
- [ ] AC-13-118: Enumerated item is supported/enforced: prohibited judgment rules.
- [ ] AC-13-119: Enumerated item is supported/enforced: task id,
- [ ] AC-13-120: Enumerated item is supported/enforced: schema version,
- [ ] AC-13-121: Enumerated item is supported/enforced: status: `passed`, `failed`, or `inconclusive`,
- [ ] AC-13-122: Enumerated item is supported/enforced: findings,
- [ ] AC-13-123: Enumerated item is supported/enforced: verified claim IDs,
- [ ] AC-13-124: Enumerated item is supported/enforced: unverified claim IDs,
- [ ] AC-13-125: Enumerated item is supported/enforced: contradicted claim IDs,
- [ ] AC-13-126: Enumerated item is supported/enforced: `prohibited_human_intent_judgment_detected` boolean.
- [ ] AC-13-127: Enumerated item is supported/enforced: `agent_claim`,
- [ ] AC-13-128: Enumerated item is supported/enforced: `evidence_mapping`,
- [ ] AC-13-129: Enumerated item is supported/enforced: `deterministic_reference`,
- [ ] AC-13-130: Enumerated item is supported/enforced: `human_approved_reference`.
- [ ] AC-13-131: Enumerated item is supported/enforced: `passed` means every submitted claim id is in `verified_claim_ids`, `unverified_claim_ids` and `contradicted_claim_ids` are empty, and no finding has severity `error`.
- [ ] AC-13-132: Enumerated item is supported/enforced: `failed` means at least one submitted claim id is in `contradicted_claim_ids`, or an error finding reports that a required claim is false or unsupported by the provided deterministic evidence.
- [ ] AC-13-133: Enumerated item is supported/enforced: `inconclusive` means at least one submitted claim id is in `unverified_claim_ids` and no submitted claim id is contradicted.
- [ ] AC-13-134: Enumerated item is supported/enforced: required fields are missing,
- [ ] AC-13-135: Enumerated item is supported/enforced: verified/unverified/contradicted claim ID sets are not pairwise disjoint,
- [ ] AC-13-136: Enumerated item is supported/enforced: for `passed`, `failed`, or `inconclusive` responses, the union of verified, unverified, and contradicted claim IDs is not exactly the submitted claim ID set,
- [ ] AC-13-137: Enumerated item is supported/enforced: invalid responses include verified, unverified, or contradicted claim IDs outside the submitted set,
- [ ] AC-13-138: Enumerated item is supported/enforced: a claim is omitted from all three sets on a non-invalid response,
- [ ] AC-13-139: Enumerated item is supported/enforced: an inconclusive claim is not listed in `unverified_claim_ids`,
- [ ] AC-13-140: Enumerated item is supported/enforced: findings judge human-approved intent,
- [ ] AC-13-141: Enumerated item is supported/enforced: response attempts to approve, reject, defer, change, or reinterpret human intent.
- [ ] AC-13-142: Table row is implemented: Claim or fact: Docs-to-AC mapping for API/contract-surface packets; Backend verification: Required
- [ ] AC-13-143: Table row is implemented: Claim or fact: Behavior-tests-to-documented-contract mapping for API/contract-surface packets; Backend verification: Required
- [ ] AC-13-144: Table row is implemented: Claim or fact: Docs-to-AC mapping for non-API docs-required packets; Backend verification: Required
- [ ] AC-13-145: Table row is implemented: Claim or fact: Behavior-tests-to-documented-contract mapping for non-API docs-required packets; Backend verification: Required
- [ ] AC-13-146: Table row is implemented: Claim or fact: Tests-to-AC mapping for non-API packets; Backend verification: Required when tests are required
- [ ] AC-13-147: Table row is implemented: Claim or fact: Failure evidence semantic claim used to prove missing approved behavior; Backend verification: Required when failure-first evidence is required
- [ ] AC-13-148: Table row is implemented: Claim or fact: Retained test is not documentation-targeting (`retained_test_not_docs`); Backend verification: Required when retained-doc-test detection is inconclusive
- [ ] AC-13-149: Table row is implemented: Claim or fact: Runtime claim beyond exact command/path/status existence; Backend verification: Required
- [ ] AC-13-150: Table row is implemented: Claim or fact: Final user-facing claim presented as verified/completed; Backend verification: Required
- [ ] AC-13-151: Table row is implemented: Claim or fact: Final user-facing claim explicitly marked unverified; Backend verification: No semantic support verification; deterministic label validation required
- [ ] AC-13-152: Table row is implemented: Claim or fact: Implementation summary claim; Backend verification: Required for review completion
- [ ] AC-13-153: Table row is implemented: Claim or fact: Docs-updated semantic claim; Backend verification: Required when docs are required or changed
- [ ] AC-13-154: Table row is implemented: Claim or fact: File existence; Backend verification: Never; deterministic
- [ ] AC-13-155: Table row is implemented: Claim or fact: Path safety; Backend verification: Never; deterministic
- [ ] AC-13-156: Table row is implemented: Claim or fact: Changed-file list; Backend verification: Never; deterministic
- [ ] AC-13-157: Table row is implemented: Claim or fact: Command exit code/status existence; Backend verification: Never; deterministic
- [ ] AC-13-158: Table row is implemented: Claim or fact: Package script existence; Backend verification: Never; deterministic
- [ ] AC-13-159: Table row is implemented: Claim or fact: Approval hash freshness; Backend verification: Never; deterministic
- [ ] AC-13-160: Table row is implemented: Claim or fact: Human-approved intent quality/completeness/correctness; Backend verification: Never; prohibited
