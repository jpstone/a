"""Executable specification for US-02: Authority model."""

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
    {'name': 'every_governed_question_must_route_to_exactly_one_qualified_authority', 'statement': 'Every governed question must route to exactly one qualified authority.', 'target': 'Every governed question must route to exactly one qualified authority', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'mixed_questions_must_be_split', 'statement': 'Mixed questions must be split.', 'target': 'Mixed questions must be split', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'once_approved_human_intent_is_canonical_until_changed_through_a_recorded_human_decision', 'statement': 'Once approved, human intent is canonical until changed through a recorded human decision.', 'target': 'Once approved, human intent is canonical until changed through a recorded human decision', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'source_derived_acs_with_source_evidence', 'statement': 'source-derived ACs with source/evidence,', 'target': 'source-derived ACs with source/evidence', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'embedded_record_storage_inside_artifacts', 'statement': 'embedded record storage inside artifacts,', 'target': 'embedded record storage inside artifacts', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'packet_change_baseline_capture', 'statement': 'packet change baseline capture,', 'target': 'packet change baseline capture', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'command_execution_records', 'statement': 'command execution records,', 'target': 'command execution records', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'observable_facts_must_be_checked_deterministically', 'statement': 'Observable facts must be checked deterministically.', 'target': 'Observable facts must be checked deterministically', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'the_backend_verifier_checks_required_semantic_frontend_agent_claims_listed_in_section_13', 'statement': 'The backend verifier checks required semantic frontend-agent claims listed in section 13.', 'target': 'The backend verifier checks required semantic frontend-agent claims listed in section 13', 'authority': 'Authority.BACKEND_VERIFIER', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'it_must_not', 'statement': 'It must not:', 'target': 'It must not:', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'create_or_alter_product_intent', 'statement': 'create or alter product intent,', 'target': 'create or alter product intent', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'approve_or_reject_work', 'statement': 'approve or reject work,', 'target': 'approve or reject work', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_product_platform_type', 'statement': 'Enumerated item is supported/enforced: product/platform type,', 'target': 'product/platform type', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_architecture_choice', 'statement': 'Enumerated item is supported/enforced: architecture choice,', 'target': 'architecture choice', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_desired_product_behavior', 'statement': 'Enumerated item is supported/enforced: desired product behavior,', 'target': 'desired product behavior', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_acceptance_criteria_approval', 'statement': 'Enumerated item is supported/enforced: acceptance criteria approval,', 'target': 'acceptance criteria approval', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_work_packet_approval', 'statement': 'Enumerated item is supported/enforced: Work Packet approval,', 'target': 'Work Packet approval', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_implementation_authorization', 'statement': 'Enumerated item is supported/enforced: implementation authorization,', 'target': 'implementation authorization', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_runtime_baseline_acceptance', 'statement': 'Enumerated item is supported/enforced: runtime baseline acceptance,', 'target': 'runtime baseline acceptance', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_plan_vs_single_packet_choice', 'statement': 'Enumerated item is supported/enforced: Plan-vs-single-packet choice,', 'target': 'Plan-vs-single-packet choice', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_plan_approval', 'statement': 'Enumerated item is supported/enforced: Plan approval,', 'target': 'Plan approval', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_source_mockup_design_interpretation_as_represented_i', 'statement': 'Enumerated item is supported/enforced: source/mockup/design interpretation as represented in approved ACs.', 'target': 'source/mockup/design interpretation as represented in approved ACs', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_goals', 'statement': 'Enumerated item is supported/enforced: goals,', 'target': 'goals', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_desired_outcomes', 'statement': 'Enumerated item is supported/enforced: desired outcomes,', 'target': 'desired outcomes', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_in_scope_and_out_of_scope_lists', 'statement': 'Enumerated item is supported/enforced: in-scope and out-of-scope lists,', 'target': 'in-scope and out-of-scope lists', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_users_actors', 'statement': 'Enumerated item is supported/enforced: users/actors,', 'target': 'users/actors', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_edge_cases', 'statement': 'Enumerated item is supported/enforced: edge cases,', 'target': 'edge cases', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_open_questions', 'statement': 'Enumerated item is supported/enforced: open questions,', 'target': 'open questions', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_acceptance_criteria', 'statement': 'Enumerated item is supported/enforced: acceptance criteria,', 'target': 'acceptance criteria', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_platform_options', 'statement': 'Enumerated item is supported/enforced: platform options,', 'target': 'platform options', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_architecture_options', 'statement': 'Enumerated item is supported/enforced: architecture options,', 'target': 'architecture options', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_source_derived_acs_with_source_evidence', 'statement': 'Enumerated item is supported/enforced: source-derived ACs with source/evidence,', 'target': 'source-derived ACs with source/evidence', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_plan_slices', 'statement': 'Enumerated item is supported/enforced: Plan slices,', 'target': 'Plan slices', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_implementation_summaries', 'statement': 'Enumerated item is supported/enforced: implementation summaries,', 'target': 'implementation summaries', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_review_summaries', 'statement': 'Enumerated item is supported/enforced: review summaries,', 'target': 'review summaries', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_final_response_drafts', 'statement': 'Enumerated item is supported/enforced: final response drafts.', 'target': 'final response drafts', 'authority': 'Authority.FRONTEND_AGENT', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_action_registry', 'statement': 'Enumerated item is supported/enforced: action registry,', 'target': 'action registry', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_top_level_artifact_storage', 'statement': 'Enumerated item is supported/enforced: top-level artifact storage,', 'target': 'top-level artifact storage', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_embedded_record_storage_inside_artifacts', 'statement': 'Enumerated item is supported/enforced: embedded record storage inside artifacts,', 'target': 'embedded record storage inside artifacts', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_schema_validation', 'statement': 'Enumerated item is supported/enforced: schema validation,', 'target': 'schema validation', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_lifecycle_transitions', 'statement': 'Enumerated item is supported/enforced: lifecycle transitions,', 'target': 'lifecycle transitions', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_human_gate_recording', 'statement': 'Enumerated item is supported/enforced: human gate recording,', 'target': 'human gate recording', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_runtime_baseline_validation', 'statement': 'Enumerated item is supported/enforced: runtime baseline validation,', 'target': 'runtime baseline validation', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_packet_change_baseline_capture', 'statement': 'Enumerated item is supported/enforced: packet change baseline capture,', 'target': 'packet change baseline capture', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_changed_file_computation', 'statement': 'Enumerated item is supported/enforced: changed-file computation,', 'target': 'changed-file computation', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_path_and_glob_validation', 'statement': 'Enumerated item is supported/enforced: path and glob validation,', 'target': 'path and glob validation', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_command_execution_records', 'statement': 'Enumerated item is supported/enforced: command execution records,', 'target': 'command execution records', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_docs_test_failure_first_ordering_checks', 'statement': 'Enumerated item is supported/enforced: docs/test/failure-first ordering checks,', 'target': 'docs/test/failure-first ordering checks', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_review_snapshot_hash_computation', 'statement': 'Enumerated item is supported/enforced: review snapshot hash computation,', 'target': 'review snapshot hash computation', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_approval_invalidation', 'statement': 'Enumerated item is supported/enforced: approval invalidation,', 'target': 'approval invalidation', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_verifier_response_schema_validation', 'statement': 'Enumerated item is supported/enforced: verifier response schema validation,', 'target': 'verifier response schema validation', 'authority': 'Authority.BACKEND_VERIFIER', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_cli_mcp_parity', 'statement': 'Enumerated item is supported/enforced: CLI/MCP parity,', 'target': 'CLI/MCP parity', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_viewer_data', 'statement': 'Enumerated item is supported/enforced: viewer data,', 'target': 'viewer data', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_migration', 'statement': 'Enumerated item is supported/enforced: migration.', 'target': 'migration', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_create_or_alter_product_intent', 'statement': 'Enumerated item is supported/enforced: create or alter product intent,', 'target': 'create or alter product intent', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_approve_or_reject_work', 'statement': 'Enumerated item is supported/enforced: approve or reject work,', 'target': 'approve or reject work', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_authorize_implementation', 'statement': 'Enumerated item is supported/enforced: authorize implementation,', 'target': 'authorize implementation', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_choose_platform_or_architecture', 'statement': 'Enumerated item is supported/enforced: choose platform or architecture,', 'target': 'choose platform or architecture', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_judge_human_approved_acs_scope_platform_architecture', 'statement': 'Enumerated item is supported/enforced: judge human-approved ACs, scope, platform, architecture, docs requirement, Plan slices, or source interpretation.', 'target': 'judge human-approved ACs, scope, platform, architecture, docs requirement, Plan slices, or source interpretation', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'table_row_is_implemented_question_type_product_intent_platform_architecture_ac_approval_wo', 'statement': 'Table row is implemented: Question type: Product intent, platform, architecture, AC approval, Work Packet approval, implementation authorization, runtime baseline acceptance, Plan-vs-single decision, Plan approval; Authority: Human', 'target': 'Question type: Product intent, platform, architecture, AC approval, Work Packet approval, implementation authorization, runtime baseline acceptance, Plan-vs-sin', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'table_row_is_implemented_question_type_ordinary_drafting_before_approval_authority_fronten', 'statement': 'Table row is implemented: Question type: Ordinary drafting before approval; Authority: Frontend agent, later reviewed through human gates', 'target': 'Question type: Ordinary drafting before approval; Authority: Frontend agent, later reviewed through human gates', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'table_row_is_implemented_question_type_files_paths_commands_timestamps_diffs_schemas_lifec', 'statement': 'Table row is implemented: Question type: Files, paths, commands, timestamps, diffs, schemas, lifecycle, hashes, config, recorded decisions; Authority: Deterministic kernel', 'target': 'Question type: Files, paths, commands, timestamps, diffs, schemas, lifecycle, hashes, config, recorded decisions; Authority: Deterministic kernel', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'table_row_is_implemented_question_type_required_semantic_checks_of_frontend_agent_claims_t', 'statement': 'Table row is implemented: Question type: Required semantic checks of frontend-agent claims that do not mutate or judge human intent; Authority: Backend verifier', 'target': 'Question type: Required semantic checks of frontend-agent claims that do not mutate or judge human intent; Authority: Backend verifier', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True}
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
