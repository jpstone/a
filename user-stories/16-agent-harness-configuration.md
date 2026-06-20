# US-16: Agent harness configuration

Derived from: [16. Agent Harness Configuration](../agentic-redesign-references.md#us-16-source)

## Problem

Generated agent harnesses need configuration that instructs agents to use governed workflows consistently across supported environments.

## User story

As a agent harness maintainer, I want agent harness configuration implemented, so that generated agent harnesses need configuration that instructs agents to use governed workflows consistently across supported environments.

## In scope

- Generate or maintain harness configuration artifacts.
- Include governance instructions for prompts, approvals, authorization, evidence, validation, and final claims.
- Support configured integrations without weakening governance.

## Out of scope

- Letting harness instructions bypass Spec Guard gates.
- Embedding secrets directly in generated configuration.

## Acceptance criteria

<!-- Expanded from agentic-redesign.md to provide behavior-level coverage. -->

- [ ] AC-16-001: `spec-guard init` must generate best-effort agent and MCP configuration files in the project, not only in an internal artifact directory.
- [ ] AC-16-002: The generated files must make MCP/Pi use obvious to agents and humans immediately after `npx spec-guard init`.
- [ ] AC-16-003: Required generated/support artifacts:
- [ ] AC-16-004: VS Code config at `.vscode/mcp.json` where supported,
- [ ] AC-16-005: Cline config at `.cline/mcp.json` and `.cline/cline_mcp_settings.json` where supported,
- [ ] AC-16-006: Roo config at `.roo/mcp.json` and `.roo/roo_mcp_settings.json` where supported,
- [ ] AC-16-007: Windsurf config at `.windsurf/mcp.json` and `.windsurf/mcp_config.json` where supported,
- [ ] AC-16-008: generic stdio snippets for other MCP clients where supported,
- [ ] AC-16-009: client support matrix.
- [ ] AC-16-010: The project-local Pi extension is required.
- [ ] AC-16-011: It must be placed at `.pi/extensions/spec-guard.ts` so Pi auto-discovers it on startup or `/reload`.
- [ ] AC-16-012: It must register direct `spec_guard_*` tools for the shared workflow actions
- [ ] AC-16-013: must call the shared core/action registry directly rather than shelling out to CLI.
- [ ] AC-16-014: Its tool descriptions or prompt guidelines must direct agents to use Spec Guard tools directly, call status/quickstart first, and provide actual human confirmation fields for human-gated actions.
- [ ] AC-16-015: The generated Pi extension must satisfy Pi's actual extension module contract.
- [ ] AC-16-016: It must default-export a synchronous or asynchronous factory function accepting Pi's `ExtensionAPI` object, for example `export default function (pi: ExtensionAPI) { ...
- [ ] AC-16-017: The module must not be a tools-only export, a named-export-only module, or a file that requires an undocumented wrapper to load.
- [ ] AC-16-018: Tool registration must happen from inside the default factory by calling `pi.registerTool(...)` for each direct `spec_guard_*` tool.
- [ ] AC-16-019: The generated file must be loadable from `.pi/extensions/spec-guard.ts` by Pi's normal project-local extension discovery and reload path without a separate build step beyond Pi's documented TypeScript extension loading.
- [ ] AC-16-020: `init` tests must prove generated Pi extension loadability, not only text content.
- [ ] AC-16-021: At minimum, tests must generate `.pi/extensions/spec-guard.ts`, load or import it through the same TypeScript execution path used for Pi extensions or an equivalent test loader, assert that the module's default export is a function, invoke that function with a minimal mock `ExtensionAPI`, and assert that expected `spec_guard_*` tools are registered.
- [ ] AC-16-022: must assert that Pi does not report `Extension does not export a valid factory function`.
- [ ] AC-16-023: Generated guidance must state:
- [ ] AC-16-024: use Spec Guard tools directly,
- [ ] AC-16-025: human-confirmed fields require actual human responses,
- [ ] AC-16-026: fixed binary decisions record option 1 or 2 only,
- [ ] AC-16-027: non-binary custom choices require numbered confirmation,
- [ ] AC-16-028: single packets use sequential AC, packet approval, and authorization gates,
- [ ] AC-16-029: Plan batch approval applies only to eligible child packets,
- [ ] AC-16-030: documentation itself is never tested and retained docs tests must be removed,
- [ ] AC-16-031: tests must clean up files, data, processes, external resources, and runtime state,
- [ ] AC-16-032: semantic agent claims require backend verification as specified.
- [ ] AC-16-033: Enumerated item is supported/enforced: generic project MCP config at `.mcp.json`,
- [ ] AC-16-034: Enumerated item is supported/enforced: Claude Code project config/snippet compatible with `.mcp.json`,
- [ ] AC-16-035: Enumerated item is supported/enforced: Claude Desktop snippet in the artifact harness directory for copy/paste when project-local config is unsupported,
- [ ] AC-16-036: Enumerated item is supported/enforced: Cursor project config at `.cursor/mcp.json`,
- [ ] AC-16-037: Enumerated item is supported/enforced: VS Code config at `.vscode/mcp.json` where supported,
- [ ] AC-16-038: Enumerated item is supported/enforced: Cline config at `.cline/mcp.json` and `.cline/cline_mcp_settings.json` where supported,
- [ ] AC-16-039: Enumerated item is supported/enforced: Roo config at `.roo/mcp.json` and `.roo/roo_mcp_settings.json` where supported,
- [ ] AC-16-040: Enumerated item is supported/enforced: Windsurf config at `.windsurf/mcp.json` and `.windsurf/mcp_config.json` where supported,
- [ ] AC-16-041: Enumerated item is supported/enforced: generic stdio snippets for other MCP clients where supported,
- [ ] AC-16-042: Enumerated item is supported/enforced: project-local Pi extension at `.pi/extensions/spec-guard.ts`,
- [ ] AC-16-043: Enumerated item is supported/enforced: Pi extension descriptor or snippet in the artifact harness directory,
- [ ] AC-16-044: Enumerated item is supported/enforced: project-visible agent guide such as `SPEC_GUARD_AGENT_GUIDE.md`,
- [ ] AC-16-045: Enumerated item is supported/enforced: MCP README/quickstart,
- [ ] AC-16-046: Enumerated item is supported/enforced: client support matrix.
- [ ] AC-16-047: Enumerated item is supported/enforced: use Spec Guard tools directly,
- [ ] AC-16-048: Enumerated item is supported/enforced: do not substitute CLI for MCP except bootstrap/init guidance,
- [ ] AC-16-049: Enumerated item is supported/enforced: do not inspect Spec Guard package/source internals for workflow parameters,
- [ ] AC-16-050: Enumerated item is supported/enforced: human-confirmed fields require actual human responses,
- [ ] AC-16-051: Enumerated item is supported/enforced: human-approved content is canonical intent,
- [ ] AC-16-052: Enumerated item is supported/enforced: Discuss is non-mutating,
- [ ] AC-16-053: Enumerated item is supported/enforced: binary gates remain Yes/No/Discuss after discussion,
- [ ] AC-16-054: Enumerated item is supported/enforced: fixed binary decisions record option 1 or 2 only,
- [ ] AC-16-055: Enumerated item is supported/enforced: non-binary custom choices require numbered confirmation,
- [ ] AC-16-056: Enumerated item is supported/enforced: single packets use sequential AC, packet approval, and authorization gates,
- [ ] AC-16-057: Enumerated item is supported/enforced: Plan batch approval applies only to eligible child packets,
- [ ] AC-16-058: Enumerated item is supported/enforced: documentation itself is never tested and retained docs tests must be removed,
- [ ] AC-16-059: Enumerated item is supported/enforced: tests must clean up files, data, processes, external resources, and runtime state,
- [ ] AC-16-060: Enumerated item is supported/enforced: semantic agent claims require backend verification as specified.
