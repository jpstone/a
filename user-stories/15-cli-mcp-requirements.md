# US-15: CLI and MCP parity

Derived from: [15. CLI and MCP Requirements](../agentic-redesign-references.md#us-15-source)

## Problem

CLI and MCP integrations must expose the same governed actions and result contracts so agents and users see consistent behavior.

## User story

As a tooling user, I want cli and mcp parity implemented, so that cLI and MCP integrations must expose the same governed actions and result contracts so agents and users see consistent behavior.

## In scope

- Define shared action result.
- Expose required CLI behavior.
- Expose required MCP behavior.
- Maintain action contract parity across interfaces.

## Out of scope

- Interface-specific governance shortcuts.
- Different validation semantics between CLI and MCP.

## Acceptance criteria

- [ ] All actions return the shared action result shape.
- [ ] CLI commands expose the required governed workflow actions and diagnostics.
- [ ] MCP tools expose the required governed workflow actions and diagnostics.
- [ ] CLI and MCP apply the same validation, lifecycle, snapshot, and authority rules.
- [ ] Errors and diagnostics are represented consistently enough for agent consumption.
