"""Executable specification for US-01: Governance objective and critical truth."""

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
    {'name': 'human_intent_is_explicitly_captured', 'statement': 'human intent is explicitly captured,', 'target': 'human intent is explicitly captured', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'implementation_starts_only_after_approval_authorization_and_pre_implementation_validation', 'statement': 'implementation starts only after approval, authorization, and pre-implementation validation,', 'target': 'implementation starts only after approval, authorization, and pre-implementation validation', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'required_docs_tests_and_failure_evidence_precede_implementation_source_changes', 'statement': 'required docs, tests, and failure evidence precede implementation source changes,', 'target': 'required docs, tests, and failure evidence precede implementation source changes', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'source_mockup_design_derived_acs_are_visible_with_source_evidence_before_approval', 'statement': 'source/mockup/design-derived ACs are visible with source evidence before approval,', 'target': 'source/mockup/design-derived ACs are visible with source evidence before approval', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'cli_mcp_pi_viewer_and_generated_agent_harness_integrations_expose_the_same_governed_workfl', 'statement': 'CLI, MCP, Pi, viewer, and generated agent-harness integrations expose the same governed workflow.', 'target': 'CLI, MCP, Pi, viewer, and generated agent-harness integrations expose the same governed workflow', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'critical_truth_must_come_from', 'statement': 'Critical truth must come from:', 'target': 'Critical truth must come from:', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'backend_verification_of_required_semantic_frontend_agent_claims', 'statement': 'backend verification of required semantic frontend-agent claims,', 'target': 'backend verification of required semantic frontend-agent claims', 'authority': 'Authority.BACKEND_VERIFIER', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'frontend_agent_claims_alone_are_never_critical_truth', 'statement': 'Frontend-agent claims alone are never critical truth.', 'target': 'Frontend-agent claims alone are never critical truth', 'authority': 'Authority.FRONTEND_AGENT', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_human_intent_is_explicitly_captured', 'statement': 'Enumerated item is supported/enforced: human intent is explicitly captured,', 'target': 'human intent is explicitly captured', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_frontend_agent_proposals_remain_proposals_until_acce', 'statement': 'Enumerated item is supported/enforced: frontend-agent proposals remain proposals until accepted through the proper gate,', 'target': 'frontend-agent proposals remain proposals until accepted through the proper gate', 'authority': 'Authority.FRONTEND_AGENT', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_human_approved_content_is_canonical_intent', 'statement': 'Enumerated item is supported/enforced: human-approved content is canonical intent,', 'target': 'human-approved content is canonical intent', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_broad_work_is_split_into_traceable_bounded_packets', 'statement': 'Enumerated item is supported/enforced: broad work is split into traceable bounded packets,', 'target': 'broad work is split into traceable bounded packets', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_implementation_starts_only_after_approval_authorizat', 'statement': 'Enumerated item is supported/enforced: implementation starts only after approval, authorization, and pre-implementation validation,', 'target': 'implementation starts only after approval, authorization, and pre-implementation validation', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_required_docs_tests_and_failure_evidence_precede_imp', 'statement': 'Enumerated item is supported/enforced: required docs, tests, and failure evidence precede implementation source changes,', 'target': 'required docs, tests, and failure evidence precede implementation source changes', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_source_mockup_design_derived_acs_are_visible_with_so', 'statement': 'Enumerated item is supported/enforced: source/mockup/design-derived ACs are visible with source evidence before approval,', 'target': 'source/mockup/design-derived ACs are visible with source evidence before approval', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_runtime_evidence_and_final_claims_are_evidence_backe', 'statement': 'Enumerated item is supported/enforced: runtime evidence and final claims are evidence-backed,', 'target': 'runtime evidence and final claims are evidence-backed', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_cli_mcp_pi_viewer_and_generated_agent_harness_integr', 'statement': 'Enumerated item is supported/enforced: CLI, MCP, Pi, viewer, and generated agent-harness integrations expose the same governed workflow.', 'target': 'CLI, MCP, Pi, viewer, and generated agent-harness integrations expose the same governed workflow', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_explicit_human_decisions', 'statement': 'Enumerated item is supported/enforced: explicit human decisions,', 'target': 'explicit human decisions', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_deterministic_observations', 'statement': 'Enumerated item is supported/enforced: deterministic observations,', 'target': 'deterministic observations', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_backend_verification_of_required_semantic_frontend_a', 'statement': 'Enumerated item is supported/enforced: backend verification of required semantic frontend-agent claims,', 'target': 'backend verification of required semantic frontend-agent claims', 'authority': 'Authority.BACKEND_VERIFIER', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_auditable_artifacts', 'statement': 'Enumerated item is supported/enforced: auditable artifacts.', 'target': 'auditable artifacts', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True}
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
