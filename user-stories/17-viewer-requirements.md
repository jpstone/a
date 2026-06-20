# US-17: Viewer requirements

Derived from: [17. Viewer Requirements](../agentic-redesign-references.md#us-17-source)

## Problem

Humans need a viewer that makes governed state, review surfaces, decisions, diagnostics, and evidence understandable without changing authority rules.

## User story

As a human reviewer, I want viewer requirements implemented, so that humans need a viewer that makes governed state, review surfaces, decisions, diagnostics, and evidence understandable without changing authority rules.

## In scope

- Display work packets, plans, baselines, decisions, snapshots, evidence, diagnostics, and readiness.
- Support human-readable review surfaces matching agent prompts.
- Expose invalidation and traceability information.

## Out of scope

- Using viewer display as a separate source of truth from stored artifacts.
- Letting viewer edits bypass registered actions or gates.

## Acceptance criteria

<!-- Expanded from agentic-redesign.md to provide behavior-level coverage. -->

- [ ] AC-17-001: The viewer must be a real web application for artifact review and governance insight.
- [ ] AC-17-002: The viewer must use Mantine for styling, layout, and interaction states.
- [ ] AC-17-003: The primary dashboard and review pages must be built from Mantine components or project-local wrappers around Mantine components, including dashboard shell/layout, metric cards, badges, tables/lists, buttons/links, and status colors.
- [ ] AC-17-004: The viewer must not be an unstyled/plain HTML surface.
- [ ] AC-17-005: The viewer must be modeled after industry-standard dashboard patterns: an overview-first dashboard, a responsive metric-card grid, clear hierarchy, scannable labels and numbers, consistent spacing and typography, status badges, action-oriented visual emphasis, and drill-down navigation from summary metrics to the underlying records.
- [ ] AC-17-006: It must create an actual HTTP server bound to the requested host and port, serve viewer routes over HTTP,
- [ ] AC-17-007: keep the CLI process alive until the server is explicitly closed or the process receives a termination signal such as Ctrl-C/SIGINT/SIGTERM.
- [ ] AC-17-008: It must not print `Viewer running at ...` unless the server is listening successfully.
- [ ] AC-17-009: If binding fails, it must return or print diagnostics and exit non-zero.
- [ ] AC-17-010: Implementations may return a server handle from the internal `viewer.serve()` API, but the CLI command must await or otherwise retain that handle so the process does not exit immediately.
- [ ] AC-17-011: The viewer must read through the same shared core/artifact store used by CLI, MCP, and Pi.
- [ ] AC-17-012: Viewer data must be derived from persisted Spec Guard artifacts under the configured artifact root, not from viewer-only fixtures, hard-coded empty objects, generated labels, or fake in-memory state except in explicitly isolated unit tests.
- [ ] AC-17-013: After a workflow action persists or mutates an artifact, refreshing the viewer or calling the viewer summary action must reflect the persisted state.
- [ ] AC-17-014: The dashboard must show persisted artifact-derived metric cards for:
- [ ] AC-17-015: blocked packets,
- [ ] AC-17-016: final claim support status.
- [ ] AC-17-017: Each dashboard metric card that displays a count must be clickable.
- [ ] AC-17-018: Activating a card must open or navigate to a filtered list of the exact artifacts represented by that count.
- [ ] AC-17-019: The filtered list must show artifact identifiers, artifact type, lifecycle/status, pending action if any, last updated/revision where available, and a link to the artifact detail/review page.
- [ ] AC-17-020: The number of rows in the filtered list must reconcile with the clicked card count, subject only to explicit pagination with a visible total count.
- [ ] AC-17-021: Metric cards for artifacts or states requiring user action, including pending human gates, blocked packets, stale approvals, verifier failures, validation failures, missing evidence, or review-ready items, must be visually distinct from passive informational cards.
- [ ] AC-17-022: The distinction must use Mantine-supported styling such as color, variant, icon, badge, border, or callout treatment,
- [ ] AC-17-023: must remain visible without relying on color alone.
- [ ] AC-17-024: The dashboard summary data used by the viewer must also be available through a shared-core read path suitable for tests and agents.
- [ ] AC-17-025: `config.check` must return more than `{ artifact_root, ok }`: it must include a persisted-artifact governance summary with at least total artifacts, artifact counts by type/status, lifecycle distribution, workflow-stage distribution, pending gates, blocked packets, baseline status, verifier health, validation failures, runtime evidence status, and final claim support status.
- [ ] AC-17-026: These fields must be computed from real persisted artifacts.
- [ ] AC-17-027: For example, after `work.intake` creates a draft Work Packet, `config.check` and the viewer dashboard must report the Work Packet in total artifacts, artifact counts, and lifecycle/workflow-stage distribution without requiring a fake viewer core.
- [ ] AC-17-028: Artifacts awaiting human gates must have human-readable review pages.
- [ ] AC-17-029: Formatted JSON must not be the primary review surface.
- [ ] AC-17-030: Work Packet pages must show:
- [ ] AC-17-031: allowed globs,
- [ ] AC-17-032: Plan pages must show:
- [ ] AC-17-033: Approval must bind to the hash shown in the viewer.
- [ ] AC-17-034: The viewer must clearly distinguish:
- [ ] AC-17-035: Enumerated item is supported/enforced: total artifacts,
- [ ] AC-17-036: Enumerated item is supported/enforced: total artifacts by artifact type,
- [ ] AC-17-037: Enumerated item is supported/enforced: artifact counts by type/status,
- [ ] AC-17-038: Enumerated item is supported/enforced: the number of artifacts in each workflow/lifecycle stage,
- [ ] AC-17-039: Enumerated item is supported/enforced: pending human gates,
- [ ] AC-17-040: Enumerated item is supported/enforced: blocked packets,
- [ ] AC-17-041: Enumerated item is supported/enforced: runtime baseline status,
- [ ] AC-17-042: Enumerated item is supported/enforced: verifier health,
- [ ] AC-17-043: Enumerated item is supported/enforced: validation failures,
- [ ] AC-17-044: Enumerated item is supported/enforced: runtime evidence status,
- [ ] AC-17-045: Enumerated item is supported/enforced: final claim support status.
- [ ] AC-17-046: Enumerated item is supported/enforced: status and lifecycle,
- [ ] AC-17-047: Enumerated item is supported/enforced: goal and intent fields,
- [ ] AC-17-048: Enumerated item is supported/enforced: ACs with source/evidence markers,
- [ ] AC-17-049: Enumerated item is supported/enforced: AC approval state,
- [ ] AC-17-050: Enumerated item is supported/enforced: platform choice,
- [ ] AC-17-051: Enumerated item is supported/enforced: architecture decisions,
- [ ] AC-17-052: Enumerated item is supported/enforced: classification and docs policy,
- [ ] AC-17-053: Enumerated item is supported/enforced: allowed globs,
- [ ] AC-17-054: Enumerated item is supported/enforced: packet change baseline,
- [ ] AC-17-055: Enumerated item is supported/enforced: docs requirements,
- [ ] AC-17-056: Enumerated item is supported/enforced: backend verification status/findings,
- [ ] AC-17-057: Enumerated item is supported/enforced: pre-implementation validation status,
- [ ] AC-17-058: Enumerated item is supported/enforced: failure/pass/runtime evidence,
- [ ] AC-17-059: Enumerated item is supported/enforced: implementation/test files,
- [ ] AC-17-060: Enumerated item is supported/enforced: changed files,
- [ ] AC-17-061: Enumerated item is supported/enforced: final claim validation,
- [ ] AC-17-062: Enumerated item is supported/enforced: diagnostics,
- [ ] AC-17-063: Enumerated item is supported/enforced: next human decision,
- [ ] AC-17-064: Enumerated item is supported/enforced: review snapshot hash.
- [ ] AC-17-065: Enumerated item is supported/enforced: Plan status,
- [ ] AC-17-066: Enumerated item is supported/enforced: approved Plan proposal,
- [ ] AC-17-067: Enumerated item is supported/enforced: child creation status,
- [ ] AC-17-068: Enumerated item is supported/enforced: batch review snapshot when pending,
- [ ] AC-17-069: Enumerated item is supported/enforced: per-child readiness,
- [ ] AC-17-070: Enumerated item is supported/enforced: per-child approval/authorization binding.
- [ ] AC-17-071: Enumerated item is supported/enforced: human-approved intent,
- [ ] AC-17-072: Enumerated item is supported/enforced: frontend-agent proposals,
- [ ] AC-17-073: Enumerated item is supported/enforced: backend-verified claims,
- [ ] AC-17-074: Enumerated item is supported/enforced: deterministic evidence.
