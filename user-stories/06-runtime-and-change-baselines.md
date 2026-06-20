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

- [ ] Runtime baseline status supports draft, accepted, and blocked.
- [ ] Baseline acceptance requires numbered Yes, review snapshot, deterministic validation success, required commands or concrete N/A reasons, and no placeholder validation commands.
- [ ] A human No blocks baseline acceptance and records an appropriate decision.
- [ ] Accepted baseline approved-path changes invalidate acceptance and dependent packet refs.
- [ ] Authorization captures packet change baseline using configured policy and blocks disallowed dirty source/config changes.
- [ ] Changed files are computed against the captured packet baseline and classified by ChangeFileCategory.
