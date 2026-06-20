"""Executable specification for US-21: Non-goals and boundaries."""

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
    {'name': 'this_specification_does_not_require', 'statement': 'This specification does not require:', 'target': 'This specification does not require:', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_prompting_every_non_ac_intent_field_separately', 'statement': 'Enumerated item is supported/enforced: prompting every non-AC intent field separately,', 'target': 'prompting every non-AC intent field separately', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_making_users_actors_edge_cases_mandatory', 'statement': 'Enumerated item is supported/enforced: making users/actors/edge-cases mandatory,', 'target': 'making users/actors/edge-cases mandatory', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_letting_backend_verifier_generate_product_scope', 'statement': 'Enumerated item is supported/enforced: letting backend verifier generate product scope,', 'target': 'letting backend verifier generate product scope', 'authority': 'Authority.BACKEND_VERIFIER', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_letting_backend_verifier_make_decisions', 'statement': 'Enumerated item is supported/enforced: letting backend verifier make decisions,', 'target': 'letting backend verifier make decisions', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_using_backend_verifier_to_judge_approved_human_inten', 'statement': 'Enumerated item is supported/enforced: using backend verifier to judge approved human intent,', 'target': 'using backend verifier to judge approved human intent', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_using_backend_verifier_for_plan_vs_single_or_plan_ap', 'statement': 'Enumerated item is supported/enforced: using backend verifier for Plan-vs-single or Plan approval,', 'target': 'using backend verifier for Plan-vs-single or Plan approval', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_replacing_deterministic_validation_with_model_judgme', 'statement': 'Enumerated item is supported/enforced: replacing deterministic validation with model judgment,', 'target': 'replacing deterministic validation with model judgment', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_choosing_a_single_model_vendor', 'statement': 'Enumerated item is supported/enforced: choosing a single model vendor,', 'target': 'choosing a single model vendor', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_storing_secrets_directly', 'statement': 'Enumerated item is supported/enforced: storing secrets directly,', 'target': 'storing secrets directly', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_exposing_spec_guard_internals_to_frontend_agents', 'statement': 'Enumerated item is supported/enforced: exposing Spec Guard internals to frontend agents.', 'target': 'exposing Spec Guard internals to frontend agents', 'authority': 'Authority.FRONTEND_AGENT', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True}
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
