"""Executable specification for US-22: Redesign success criteria."""

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
    {'name': 'approval_records_bind_to_review_snapshots_and_approved_fields', 'statement': 'Approval records bind to review snapshots and approved fields.', 'target': 'Approval records bind to review snapshots and approved fields', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'single_packets_use_sequential_ac_approval_packet_approval_and_authorization_gates', 'statement': 'Single packets use sequential AC approval, packet approval, and authorization gates.', 'target': 'Single packets use sequential AC approval, packet approval, and authorization gates', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'api_contract_surface_docs_are_always_required_for_reusable_api_rest_api_and_reusable_ui_wo', 'statement': 'API/contract-surface docs are always required for reusable API, REST API, and reusable UI work.', 'target': 'API/contract-surface docs are always required for reusable API, REST API, and reusable UI work', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'artifact_schemas_embedded_record_schemas_hashes_action_inputs_cli_and_mcp_contracts_are_co', 'statement': 'Artifact schemas, embedded record schemas, hashes, action inputs, CLI, and MCP contracts are concrete enough to implement.', 'target': 'Artifact schemas, embedded record schemas, hashes, action inputs, CLI, and MCP contracts are concrete enough to implement', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'viewer_supports_human_readable_review_and_governance_insight', 'statement': 'Viewer supports human-readable review and governance insight.', 'target': 'Viewer supports human-readable review and governance insight', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'ordered_requirement_is_supported_enforced_an_implementation_agent_can_implement_from_this', 'statement': 'Ordered requirement is supported/enforced: An implementation agent can implement from this document alone.', 'target': 'Ordered requirement is supported/enforced: An implementation agent can implement from this document alone', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'ordered_requirement_is_supported_enforced_every_governed_question_routes_to_the_correct_au', 'statement': 'Ordered requirement is supported/enforced: Every governed question routes to the correct authority.', 'target': 'Ordered requirement is supported/enforced: Every governed question routes to the correct authority', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'ordered_requirement_is_supported_enforced_human_approved_intent_is_canonical_and_not_judge', 'statement': 'Ordered requirement is supported/enforced: Human-approved intent is canonical and not judged by the backend verifier.', 'target': 'Ordered requirement is supported/enforced: Human-approved intent is canonical and not judged by the backend verifier', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'ordered_requirement_is_supported_enforced_choice_binary_gate_and_fixed_binary_decision_sem', 'statement': 'Ordered requirement is supported/enforced: Choice, binary gate, and fixed binary decision semantics are consistent.', 'target': 'Ordered requirement is supported/enforced: Choice, binary gate, and fixed binary decision semantics are consistent', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'ordered_requirement_is_supported_enforced_approval_records_bind_to_review_snapshots_and_ap', 'statement': 'Ordered requirement is supported/enforced: Approval records bind to review snapshots and approved fields.', 'target': 'Ordered requirement is supported/enforced: Approval records bind to review snapshots and approved fields', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'ordered_requirement_is_supported_enforced_single_packets_use_sequential_ac_approval_packet', 'statement': 'Ordered requirement is supported/enforced: Single packets use sequential AC approval, packet approval, and authorization gates.', 'target': 'Ordered requirement is supported/enforced: Single packets use sequential AC approval, packet approval, and authorization gates', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'ordered_requirement_is_supported_enforced_plan_child_batch_acceleration_is_explicit_per_ch', 'statement': 'Ordered requirement is supported/enforced: Plan child batch acceleration is explicit, per-child bound, and limited to eligible children.', 'target': 'Ordered requirement is supported/enforced: Plan child batch acceleration is explicit, per-child bound, and limited to eligible children', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'ordered_requirement_is_supported_enforced_runtime_baseline_and_packet_change_baseline_are', 'statement': 'Ordered requirement is supported/enforced: Runtime baseline and packet change baseline are distinct and operational.', 'target': 'Ordered requirement is supported/enforced: Runtime baseline and packet change baseline are distinct and operational', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'ordered_requirement_is_supported_enforced_implementation_boundary_is_enforceable', 'statement': 'Ordered requirement is supported/enforced: Implementation boundary is enforceable.', 'target': 'Ordered requirement is supported/enforced: Implementation boundary is enforceable', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'ordered_requirement_is_supported_enforced_api_contract_surface_docs_are_always_required_fo', 'statement': 'Ordered requirement is supported/enforced: API/contract-surface docs are always required for reusable API, REST API, and reusable UI work.', 'target': 'Ordered requirement is supported/enforced: API/contract-surface docs are always required for reusable API, REST API, and reusable UI work', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'ordered_requirement_is_supported_enforced_backend_verification_requirements_are_determinis', 'statement': 'Ordered requirement is supported/enforced: Backend verification requirements are deterministic.', 'target': 'Ordered requirement is supported/enforced: Backend verification requirements are deterministic', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'ordered_requirement_is_supported_enforced_artifact_schemas_embedded_record_schemas_hashes', 'statement': 'Ordered requirement is supported/enforced: Artifact schemas, embedded record schemas, hashes, action inputs, CLI, and MCP contracts are concrete enough to implement.', 'target': 'Ordered requirement is supported/enforced: Artifact schemas, embedded record schemas, hashes, action inputs, CLI, and MCP contracts are concrete enough to imple', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'ordered_requirement_is_supported_enforced_viewer_supports_human_readable_review_and_govern', 'statement': 'Ordered requirement is supported/enforced: Viewer supports human-readable review and governance insight.', 'target': 'Ordered requirement is supported/enforced: Viewer supports human-readable review and governance insight', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True}
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
