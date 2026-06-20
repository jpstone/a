"""Executable specification for US-15: CLI and MCP parity."""

import pytest

from spec_guard.contracts import GovernanceContract, GovernanceControl
from spec_guard.enums import Authority, EnforcementLevel, MutationMode


AUTHORITY_VALUES = {
    "Authority.HUMAN": Authority.HUMAN,
    "Authority.BACKEND_VERIFIER": Authority.BACKEND_VERIFIER,
    "Authority.FRONTEND_AGENT": Authority.FRONTEND_AGENT,
    "Authority.DETERMINISTIC_KERNEL": Authority.DETERMINISTIC_KERNEL,
}

MUTATION_VALUES = {
    "MutationMode.YES": MutationMode.YES,
    "MutationMode.NO": MutationMode.NO,
    "MutationMode.AUDIT_ONLY": MutationMode.AUDIT_ONLY,
}

ENFORCEMENT_VALUES = {
    "EnforcementLevel.BLOCKING": EnforcementLevel.BLOCKING,
    "EnforcementLevel.REQUIRED": EnforcementLevel.REQUIRED,
    "EnforcementLevel.OBSERVABLE": EnforcementLevel.OBSERVABLE,
}

CONTROLS = [
    {'name': 'every_action_result_must_match_appendix_b', 'statement': 'Every action result must match Appendix B:', 'target': 'Every action result must match Appendix B:', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'all_shared_actions_must_be_available_through_cli_unless_explicitly_bootstrap_only', 'statement': 'All shared actions must be available through CLI unless explicitly bootstrap-only.', 'target': 'All shared actions must be available through CLI unless explicitly bootstrap-only', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'cli_commands_must_not_require_agents_to_inspect_spec_guard_source_to_discover_valid_workfl', 'statement': 'CLI commands must not require agents to inspect Spec Guard source to discover valid workflow parameters.', 'target': 'CLI commands must not require agents to inspect Spec Guard source to discover valid workflow parameters', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'must_optimize_for_human_readability', 'statement': 'must optimize for human readability.', 'target': 'must optimize for human readability', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'on_successful_init_with_no_explicit_machine_readable_flag_stdout_must_be_plain_text_not_js', 'statement': 'On successful `init` with no explicit machine-readable flag, stdout must be plain text, not JSON.', 'target': 'On successful `init` with no explicit machine-readable flag, stdout must be plain text, not JSON', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'the_plain_text_success_output_must_include_at_least', 'statement': 'The plain text success output must include at least:', 'target': 'The plain text success output must include at least:', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'the_recommended_first_tool_calls_such_as_status_quickstart', 'statement': 'the recommended first tool calls such as status/quickstart.', 'target': 'the recommended first tool calls such as status/quickstart', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'init_must_still_support_an_explicit_machine_readable_mode_such_as_json_that_returns_the_st', 'statement': '`init` must still support an explicit machine-readable mode, such as `--json`, that returns the standard shared action result JSON for automation.', 'target': '`init` must still support an explicit machine-readable mode, such as `--json`, that returns the standard shared action result JSON for automation', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'failed_init_attempts_may_return_structured_json_diagnostics_or_clear_plain_text_diagnostic', 'statement': 'Failed `init` attempts may return structured JSON diagnostics or clear plain-text diagnostics, but success with the default `npx spec-guard init` path must not require agents or humans to parse JSON.', 'target': 'Failed `init` attempts may return structured JSON diagnostics or clear plain-text diagnostics, but success with the default `npx spec-guard init` path must not ', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'every_non_bootstrap_non_local_runtime_shared_workflow_action_must_have_an_mcp_tool', 'statement': 'Every non-bootstrap, non-local-runtime shared workflow action must have an MCP tool.', 'target': 'Every non-bootstrap, non-local-runtime shared workflow action must have an MCP tool', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'cli_only_exceptions_are_allowed_for_bootstrap_actions_and_local_runtime_server_actions', 'statement': 'CLI-only exceptions are allowed for bootstrap actions and local runtime server actions:', 'target': 'CLI-only exceptions are allowed for bootstrap actions and local runtime server actions:', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'init_is_cli_only_bootstrap_for_creating_local_configuration_and_generated_harness_files', 'statement': '`init` is CLI-only bootstrap for creating local configuration and generated harness files.', 'target': '`init` is CLI-only bootstrap for creating local configuration and generated harness files', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'serve_viewer_is_cli_only_local_runtime_server_startup', 'statement': '`serve.viewer` is CLI-only local runtime server startup.', 'target': '`serve.viewer` is CLI-only local runtime server startup', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'cli_and_mcp_must_call_the_shared_core_action_registry_directly', 'statement': 'CLI and MCP must call the shared core/action registry directly.', 'target': 'CLI and MCP must call the shared core/action registry directly', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'mcp_must_not_shell_out_to_cli_spawn_cli_subprocesses_parse_cli_output_or_depend_on_cli_com', 'statement': 'MCP must not shell out to CLI, spawn CLI subprocesses, parse CLI output, or depend on CLI command behavior as its implementation path.', 'target': 'MCP must not shell out to CLI, spawn CLI subprocesses, parse CLI output, or depend on CLI command behavior as its implementation path', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'mcp_tools_must', 'statement': 'MCP tools must:', 'target': 'MCP tools must:', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'use_complete_input_schemas', 'statement': 'use complete input schemas,', 'target': 'use complete input schemas', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'return_compact_output_by_default', 'statement': 'return compact output by default,', 'target': 'return compact output by default', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'support_full_artifact_opt_in', 'statement': 'support full artifact opt-in,', 'target': 'support full artifact opt-in', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'include_next_actions_and_suggested_inputs_sufficient_for_agents', 'statement': 'include next actions and suggested inputs sufficient for agents,', 'target': 'include next actions and suggested inputs sufficient for agents', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'expose_verifier_and_baseline_status_through_status_quickstart', 'statement': 'expose verifier and baseline status through status/quickstart,', 'target': 'expose verifier and baseline status through status/quickstart', 'authority': 'Authority.BACKEND_VERIFIER', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'describe_the_action_in_terms_an_agent_can_use_without_inspecting_source', 'statement': 'describe the action in terms an agent can use without inspecting source,', 'target': 'describe the action in terms an agent can use without inspecting source', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'explicitly_remind_agents_that_human_gated_actions_require_actual_human_confirmation_fields', 'statement': 'explicitly remind agents that human-gated actions require actual human confirmation fields,', 'target': 'explicitly remind agents that human-gated actions require actual human confirmation fields', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'make_the_status_quickstart_tools_obvious_as_the_first_tools_to_call', 'statement': 'make the status/quickstart tools obvious as the first tools to call.', 'target': 'make the status/quickstart tools obvious as the first tools to call', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'mcp_tool_names_must_be_deterministic_spec_guard_plus_action_id_with_dots_replaced_by_under', 'statement': 'MCP tool names must be deterministic: `spec_guard_` plus action id with dots replaced by underscores.', 'target': 'MCP tool names must be deterministic: `spec_guard_` plus action id with dots replaced by underscores', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'the_mcp_server_startup_path_generated_by_init_must_invoke_the_shared_core_directly', 'statement': 'The MCP server startup path generated by init must invoke the shared core directly.', 'target': 'The MCP server startup path generated by init must invoke the shared core directly', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'it_must_be_a_direct_stdio_server_command_not_a_wrapper_that_shells_out_to_ordinary_cli_wor', 'statement': 'It must be a direct stdio server command, not a wrapper that shells out to ordinary CLI workflow commands or parses CLI output.', 'target': 'It must be a direct stdio server command, not a wrapper that shells out to ordinary CLI workflow commands or parses CLI output', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_ok', 'statement': 'Enumerated item is supported/enforced: `ok`,', 'target': '`ok`', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_action_id', 'statement': 'Enumerated item is supported/enforced: `action_id`,', 'target': '`action_id`', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_data', 'statement': 'Enumerated item is supported/enforced: `data`,', 'target': '`data`', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_diagnostics', 'statement': 'Enumerated item is supported/enforced: `diagnostics`,', 'target': '`diagnostics`', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_mutations', 'statement': 'Enumerated item is supported/enforced: `mutations`,', 'target': '`mutations`', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_next_actions', 'statement': 'Enumerated item is supported/enforced: `next_actions`,', 'target': '`next_actions`', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_summary', 'statement': 'Enumerated item is supported/enforced: `summary`.', 'target': '`summary`', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_that_spec_guard_initialized_successfully', 'statement': 'Enumerated item is supported/enforced: that Spec Guard initialized successfully,', 'target': 'that Spec Guard initialized successfully', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_artifact_root_path', 'statement': 'Enumerated item is supported/enforced: artifact root path,', 'target': 'artifact root path', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_generated_mcp_client_pi_config_file_paths', 'statement': 'Enumerated item is supported/enforced: generated MCP/client/Pi config file paths,', 'target': 'generated MCP/client/Pi config file paths', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_immediate_next_steps_for_pi_reload_restart_and_mcp_c', 'statement': 'Enumerated item is supported/enforced: immediate next steps for Pi reload/restart and MCP client reload,', 'target': 'immediate next steps for Pi reload/restart and MCP client reload', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_the_recommended_first_tool_calls_such_as_status_quic', 'statement': 'Enumerated item is supported/enforced: the recommended first tool calls such as status/quickstart.', 'target': 'the recommended first tool calls such as status/quickstart', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_init_is_cli_only_bootstrap_for_creating_local_config', 'statement': 'Enumerated item is supported/enforced: `init` is CLI-only bootstrap for creating local configuration and generated harness files.', 'target': '`init` is CLI-only bootstrap for creating local configuration and generated harness files', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_serve_viewer_is_cli_only_local_runtime_server_startu', 'statement': 'Enumerated item is supported/enforced: `serve.viewer` is CLI-only local runtime server startup.', 'target': '`serve.viewer` is CLI-only local runtime server startup', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_use_complete_input_schemas', 'statement': 'Enumerated item is supported/enforced: use complete input schemas,', 'target': 'use complete input schemas', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_return_compact_output_by_default', 'statement': 'Enumerated item is supported/enforced: return compact output by default,', 'target': 'return compact output by default', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_support_full_artifact_opt_in', 'statement': 'Enumerated item is supported/enforced: support full artifact opt-in,', 'target': 'support full artifact opt-in', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_include_next_actions_and_suggested_inputs_sufficient', 'statement': 'Enumerated item is supported/enforced: include next actions and suggested inputs sufficient for agents,', 'target': 'include next actions and suggested inputs sufficient for agents', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_expose_verifier_and_baseline_status_through_status_q', 'statement': 'Enumerated item is supported/enforced: expose verifier and baseline status through status/quickstart,', 'target': 'expose verifier and baseline status through status/quickstart', 'authority': 'Authority.BACKEND_VERIFIER', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_describe_the_action_in_terms_an_agent_can_use_withou', 'statement': 'Enumerated item is supported/enforced: describe the action in terms an agent can use without inspecting source,', 'target': 'describe the action in terms an agent can use without inspecting source', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_explicitly_remind_agents_that_human_gated_actions_re', 'statement': 'Enumerated item is supported/enforced: explicitly remind agents that human-gated actions require actual human confirmation fields,', 'target': 'explicitly remind agents that human-gated actions require actual human confirmation fields', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_make_the_status_quickstart_tools_obvious_as_the_firs', 'statement': 'Enumerated item is supported/enforced: make the status/quickstart tools obvious as the first tools to call.', 'target': 'make the status/quickstart tools obvious as the first tools to call', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True}
]


@pytest.mark.parametrize("expected", CONTROLS, ids=[item["name"] for item in CONTROLS])
def test_governance_control_is_registered_with_concrete_enforcement(expected):
    contract = GovernanceContract.default()

    actual = contract.control(expected["name"])

    assert isinstance(actual, GovernanceControl)
    assert actual.name == expected["name"]
    assert actual.statement == expected["statement"]
    assert actual.target == expected["target"]
    assert actual.authority is AUTHORITY_VALUES[expected["authority"]]
    assert actual.mutation_mode is MUTATION_VALUES[expected["mutation"]]
    assert actual.enforcement_level is ENFORCEMENT_VALUES[expected["level"]]
    assert actual.blocks_noncompliant_workflow is expected["blocking"]
    assert actual.enforced is True


def test_workflow_rejects_execution_when_any_registered_blocking_control_fails():
    contract = GovernanceContract.default()
    blocking_controls = [item["name"] for item in CONTROLS if item["blocking"]]

    result = contract.evaluate_workflow_controls(
        operation="implementation_source_change",
        actor="agent",
        satisfied_controls=[],
        candidate_controls=blocking_controls,
    )

    assert result.allowed is False
    assert result.blocked_control_names == blocking_controls
    assert all(diagnostic.severity == "error" for diagnostic in result.diagnostics)
