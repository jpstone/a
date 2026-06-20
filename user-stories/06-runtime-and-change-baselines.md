# US-06: Runtime and packet change baselines

Derived from: [6. Runtime Baseline and Packet Change Baseline](../agentic-redesign-references.md#us-06-source)

## Problem

Environment readiness and file-change baselines must be explicit and separate so implementation starts only from accepted runtime assumptions and traceable diff state.

## User story

As a implementation authorizer, I want runtime and packet change baselines implemented, so that environment readiness and file-change baselines must be explicit and separate so implementation starts only from accepted runtime assumptions and traceable diff state.

## In scope

- Capture and accept a runtime/build/test/project-environment baseline.
- Validate baseline commands and not-applicable reasons deterministically.
- Capture packet change baseline at authorization.
- Support VCS and manifest baseline modes.
- Compute and classify changed files from the packet baseline.

## Out of scope

- Treating runtime baseline as repository diff base.
- Accepting placeholder, version-only, or Spec Guard self-check commands as project validation.
- Silently absorbing pre-existing product/source/runtime configuration changes into a packet baseline.

## Acceptance criteria

<!-- Expanded from agentic-redesign.md to provide behavior-level coverage. -->

- [ ] AC-06-001: prevent fake or placeholder project commands,
- [ ] AC-06-002: ensure Plan batch acceleration is not blocked by missing environment readiness.
- [ ] AC-06-003: `blocked`.
- [ ] AC-06-004: The runtime baseline must capture:
- [ ] AC-06-005: acceptance record when accepted,
- [ ] AC-06-006: blocker record when blocked.
- [ ] AC-06-007: Commands must distinguish, when applicable:
- [ ] AC-06-008: If a project requires both frontend and backend for development, the development command must be one documented command or orchestrated entry point that starts the required full development runtime, or a concrete not-applicable reason must be recorded.
- [ ] AC-06-009: Baseline acceptance requires:
- [ ] AC-06-010: a runtime baseline review snapshot hash and revision shown to the human,
- [ ] AC-06-011: required commands or concrete not-applicable reasons,
- [ ] AC-06-012: no placeholder, version-only, or Spec Guard self-check command used as project validation.
- [ ] AC-06-013: Deterministic runtime baseline validation requires every non-null configured command in `commands.test`, `commands.build`, `commands.runtime_production`, and `commands.runtime_development` to be a CommandSpec and to have a current RuntimeBaseline `validation.command_results` entry whose `command_spec` is canonically equal, whose purpose matches (`test`, `build`, `runtime_production`, or `runtime_development`), whose `related_runtime_baseline_ref` is null during draft validation, and whose status is `passed`.
- [ ] AC-06-014: A null command is valid only when the corresponding concrete not-applicable reason field is non-empty.
- [ ] AC-06-015: CommandResults with status `failed`, `timed_out`, or `skipped`, placeholder/version-only/self-check command specs, missing command results, command purpose mismatches, stale command specs, or null commands without not-applicable reasons block baseline acceptance.
- [ ] AC-06-016: If deterministic validation fails after human Yes, acceptance is not recorded.
- [ ] AC-06-017: The baseline remains draft or blocked with diagnostics.
- [ ] AC-06-018: If the human selects numbered No on the runtime baseline acceptance gate, `baseline.accept` records a `runtime_baseline_acceptance` HumanDecision with `approved_fields: []`, no approved payload, the reviewed snapshot hash, revision, and source refs required by the action contract, and normalized decision `no`.
- [ ] AC-06-019: It appends that decision to runtime baseline decision history, sets baseline status to `blocked`, records a Blocker with reason `human_declined_baseline_acceptance`,
- [ ] AC-06-020: does not create a RuntimeBaselineRef.
- [ ] AC-06-021: Discuss records no HumanDecision and no status change.
- [ ] AC-06-022: require the same Yes/No/Discuss acceptance gate again.
- [ ] AC-06-023: When `baseline.update` changes any accepted approved path, Spec Guard sets RuntimeBaseline status to `draft`, clears the current `acceptance` convenience slot, keeps decision history append-only, records invalidation diagnostics,
- [ ] AC-06-024: marks every RuntimeBaselineRef to the prior accepted revision stale for dependent packet approval/authorization checks.
- [ ] AC-06-025: `baseline.accept` validates the reviewed pre-acceptance payload against the submitted snapshot hash, records the acceptance HumanDecision with that snapshot hash, writes acceptance state, increments the RuntimeBaseline revision,
- [ ] AC-06-026: returns the accepted revision for references.
- [ ] AC-06-027: Later staleness checks compare packet refs against this accepted revision and acceptance decision.
- [ ] AC-06-028: Runtime baseline acceptance must not be batch-approved.
- [ ] AC-06-029: It is captured at implementation authorization time
- [ ] AC-06-030: is used to:
- [ ] AC-06-031: compute changed files,
- [ ] AC-06-032: enforce allowed globs,
- [ ] AC-06-033: support review traceability.
- [ ] AC-06-034: `vcs`: record commit/tree identifier and working tree status,
- [ ] AC-06-035: `manifest`: record a file manifest when VCS metadata is unavailable.
- [ ] AC-06-036: `vcs` requires supported VCS metadata
- [ ] AC-06-037: blocks if unavailable.
- [ ] AC-06-038: `manifest` always uses manifest capture.
- [ ] AC-06-039: `auto` uses `vcs` when supported VCS metadata is present at or above the project root and otherwise uses `manifest`.
- [ ] AC-06-040: The minimum required VCS implementation is Git.
- [ ] AC-06-041: Other VCS systems are optional, but if supported they must provide equivalent commit/tree, dirty tracked path, and untracked path data.
- [ ] AC-06-042: they use this selected mode.
- [ ] AC-06-043: At authorization, Spec Guard must capture:
- [ ] AC-06-044: captured timestamp,
- [ ] AC-06-045: allowed globs,
- [ ] AC-06-046: The captured WorkPacket artifact hash is the governed content hash of the WorkPacket at the recorded `artifact_revision`, excluding the `change_baseline.artifact_hash` field itself and excluding audit-only appendices.
- [ ] AC-06-047: It includes the other PacketChangeBaseline fields committed atomically with authorization.
- [ ] AC-06-048: Authorization commit uses a deterministic prepare/commit algorithm.
- [ ] AC-06-049: It computes `artifact_hash` over that projection while excluding only `change_baseline.artifact_hash` and audit-only appendices, writes the computed hash into `change_baseline.artifact_hash`, then commits that exact projection as `artifact_revision = next_revision`.
- [ ] AC-06-050: If the final committed projection excluding `artifact_hash` does not hash to the stored value, authorization is invalid
- [ ] AC-06-051: must be rolled back or marked failed before any authorization decision is exposed.
- [ ] AC-06-052: If VCS exists and the working tree has uncommitted `implementation_source`, `runtime_product_configuration`, or `other_unexpected` changes before authorization, authorization must block unless the human resolves the dirty state before authorization.
- [ ] AC-06-053: Dirty files categorized as `docs`, `tests`, or `spec_guard_artifact_evidence` may exist before authorization, but their pre-authorization status and content hashes are captured into the packet baseline as pre-existing state
- [ ] AC-06-054: do not count as packet evidence unless re-recorded after authorization.
- [ ] AC-06-055: Spec Guard must not silently absorb pre-existing product/source/runtime configuration changes into the packet.
- [ ] AC-06-056: Changed files are computed from packet change baseline to current state:
- [ ] AC-06-057: VCS mode: diff baseline commit/tree plus working tree and untracked files, adjusted by stored dirty/untracked baseline entries.
- [ ] AC-06-058: For Git, capture `HEAD` commit, `HEAD` tree, and repository-relative dirty/untracked entries from porcelain status with NUL separation.
- [ ] AC-06-059: Deleted entries keep the deleted path.
- [ ] AC-06-060: Untracked paths are captured exactly as repository-relative paths.
- [ ] AC-06-061: For every allowed pre-authorization dirty/untracked docs/tests/evidence path, capture size and content hash
- [ ] AC-06-062: later changed-file computation treats that captured content hash as the baseline for that path so pre-existing dirty content is not counted as a packet change unless it changes after authorization.
- [ ] AC-06-063: Manifest mode: compare current manifest to captured manifest.
- [ ] AC-06-064: Changed files must be classified by the canonical `ChangeFileCategory` enum in Appendix C.
- [ ] AC-06-065: Enumerated item is supported/enforced: make environment readiness explicit,
- [ ] AC-06-066: Enumerated item is supported/enforced: prevent fake or placeholder project commands,
- [ ] AC-06-067: Enumerated item is supported/enforced: ensure Plan batch acceleration is not blocked by missing environment readiness.
- [ ] AC-06-068: Enumerated item is supported/enforced: `draft`,
- [ ] AC-06-069: Enumerated item is supported/enforced: `accepted`,
- [ ] AC-06-070: Enumerated item is supported/enforced: `blocked`.
- [ ] AC-06-071: Enumerated item is supported/enforced: stack,
- [ ] AC-06-072: Enumerated item is supported/enforced: commands,
- [ ] AC-06-073: Enumerated item is supported/enforced: configuration assumptions,
- [ ] AC-06-074: Enumerated item is supported/enforced: dependency modes,
- [ ] AC-06-075: Enumerated item is supported/enforced: diff policy,
- [ ] AC-06-076: Enumerated item is supported/enforced: validation results,
- [ ] AC-06-077: Enumerated item is supported/enforced: acceptance record when accepted,
- [ ] AC-06-078: Enumerated item is supported/enforced: blocker record when blocked.
- [ ] AC-06-079: Enumerated item is supported/enforced: test,
- [ ] AC-06-080: Enumerated item is supported/enforced: build,
- [ ] AC-06-081: Enumerated item is supported/enforced: production runtime smoke,
- [ ] AC-06-082: Enumerated item is supported/enforced: development runtime.
- [ ] AC-06-083: Ordered requirement is supported/enforced: numbered human Yes on the baseline acceptance gate,
- [ ] AC-06-084: Ordered requirement is supported/enforced: a runtime baseline review snapshot hash and revision shown to the human,
- [ ] AC-06-085: Ordered requirement is supported/enforced: deterministic validation success,
- [ ] AC-06-086: Ordered requirement is supported/enforced: required commands or concrete not-applicable reasons,
- [ ] AC-06-087: Ordered requirement is supported/enforced: no placeholder, version-only, or Spec Guard self-check command used as project validation.
- [ ] AC-06-088: Enumerated item is supported/enforced: compute changed files,
- [ ] AC-06-089: Enumerated item is supported/enforced: enforce allowed globs,
- [ ] AC-06-090: Enumerated item is supported/enforced: prove implementation source did not change before failure-first evidence,
- [ ] AC-06-091: Enumerated item is supported/enforced: support review traceability.
- [ ] AC-06-092: Enumerated item is supported/enforced: `vcs`: record commit/tree identifier and working tree status,
- [ ] AC-06-093: Enumerated item is supported/enforced: `manifest`: record a file manifest when VCS metadata is unavailable.
- [ ] AC-06-094: Enumerated item is supported/enforced: mode,
- [ ] AC-06-095: Enumerated item is supported/enforced: captured timestamp,
- [ ] AC-06-096: Enumerated item is supported/enforced: WorkPacket governed content hash/revision,
- [ ] AC-06-097: Enumerated item is supported/enforced: allowed globs,
- [ ] AC-06-098: Enumerated item is supported/enforced: ignored path rules,
- [ ] AC-06-099: Enumerated item is supported/enforced: VCS commit/tree and dirty state, or manifest hash and file entries.
- [ ] AC-06-100: Enumerated item is supported/enforced: VCS mode: diff baseline commit/tree plus working tree and untracked files, adjusted by stored dirty/untracked baseline entries. For Git, capture `HEAD` commit, `HEAD` tree, and repository-relative dirty/untracked entries from porcelain status with NUL separation. Rename entries are normalized to the new repository-relative path with status `renamed`. Deleted entries keep the deleted path. Untracked paths are captured exactly as repository-relative paths. For every allowed pre-authorization dirty/untracked docs/tests/evidence path, capture size and content hash; later changed-file computation treats that captured content hash as the baseline for that path so pre-existing dirty content is not counted as a packet change unless it changes after authorization.
- [ ] AC-06-101: Enumerated item is supported/enforced: Manifest mode: compare current manifest to captured manifest.
