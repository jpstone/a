"""Executable specification for US-14: Runtime evidence, review completion, and final claims."""

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
    {'name': 'runtime_evidence_must_distinguish', 'statement': 'Runtime evidence must distinguish:', 'target': 'Runtime evidence must distinguish:', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'production_claims_require_production_evidence', 'statement': 'Production claims require production evidence.', 'target': 'Production claims require production evidence', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'development_hmr_full_stack_development_claims_require_development_evidence_for_exact_comma', 'statement': 'Development/HMR/full-stack development claims require development evidence for exact command and validated paths.', 'target': 'Development/HMR/full-stack development claims require development evidence for exact command and validated paths', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'if_work_requires_frontend_and_backend_processes_for_development_use_evidence_must_show_one', 'statement': 'If work requires frontend and backend processes for development use, evidence must show one documented command or orchestrated entry point starts the full required development runtime.', 'target': 'If work requires frontend and backend processes for development use, evidence must show one documented command or orchestrated entry point starts the full requi', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'review_completion_requires_when_applicable_to_the_packet_classification_and_evidence_polic', 'statement': 'Review completion requires, when applicable to the packet classification and evidence policy:', 'target': 'Review completion requires, when applicable to the packet classification and evidence policy:', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'implementation_files_or_an_approved_not_applicable_reason_for_documentation_only_or_other', 'statement': 'implementation files, or an approved/not-applicable reason for documentation-only or other no-implementation paths,', 'target': 'implementation files, or an approved/not-applicable reason for documentation-only or other no-implementation paths', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'required_backend_verification_records', 'statement': 'required backend verification records,', 'target': 'required backend verification records', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'review_cannot_complete_while_required_traceability_is_empty_or_unsupported', 'statement': 'Review cannot complete while required traceability is empty or unsupported.', 'target': 'Review cannot complete while required traceability is empty or unsupported', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'ac_verification_at_review_completion_means_each_approved_ac_is_either_linked_to_passing_go', 'statement': 'AC verification at review completion means each approved AC is either linked to passing governed evidence, linked to an approved deterministic not-applicable evidence record where not-applicable is permitted, or explicitly reported as unsupported so review completion blocks.', 'target': 'AC verification at review completion means each approved AC is either linked to passing governed evidence, linked to an approved deterministic not-applicable ev', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'for_behavior_api_runtime_acs_evidence_must_include_kernel_created_command_results_and_requ', 'statement': 'For behavior/API/runtime ACs, evidence must include kernel-created command results and required backend verification.', 'target': 'For behavior/API/runtime ACs, evidence must include kernel-created command results and required backend verification', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'for_operational_document_documentation_only_acs_evidence_must_include_docs_content_records', 'statement': 'For operational-document documentation-only ACs, evidence must include docs/content records and required docs/content-to-AC verification.', 'target': 'For operational-document documentation-only ACs, evidence must include docs/content records and required docs/content-to-AC verification', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'final_user_facing_claims_must_be_supported_by_recorded_evidence_or_explicitly_marked_unver', 'statement': 'Final user-facing claims must be supported by recorded evidence or explicitly marked unverified.', 'target': 'Final user-facing claims must be supported by recorded evidence or explicitly marked unverified', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'claims_presented_as_verified_completed_implemented_working_tested_or_validated_require_bac', 'statement': 'Claims presented as verified, completed, implemented, working, tested, or validated require backend verification against evidence and approved references used only as immutable constraints.', 'target': 'Claims presented as verified, completed, implemented, working, tested, or validated require backend verification against evidence and approved references used o', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'claims_explicitly_marked_unverified_do_not_require_semantic_support_verification_but_deter', 'statement': 'Claims explicitly marked unverified do not require semantic support verification, but deterministic validation must ensure they are clearly labeled as unverified', 'target': 'Claims explicitly marked unverified do not require semantic support verification, but deterministic validation must ensure they are clearly labeled as unverifie', 'authority': 'Authority.BACKEND_VERIFIER', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'are_not_used_to_satisfy_review_completion_ac_verification_runtime_validation_or_implementa', 'statement': 'are not used to satisfy review completion, AC verification, runtime validation, or implementation success.', 'target': 'are not used to satisfy review completion, AC verification, runtime validation, or implementation success', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'a_final_response_may_include_unverified_claims_only_as_caveats_or_limitations', 'statement': 'A final response may include unverified claims only as caveats or limitations.', 'target': 'A final response may include unverified claims only as caveats or limitations', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'the_verifier_must_not_criticize_or_reinterpret_approved_human_intent', 'statement': 'The verifier must not criticize or reinterpret approved human intent.', 'target': 'The verifier must not criticize or reinterpret approved human intent', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_production_runtime_evidence', 'statement': 'Enumerated item is supported/enforced: production runtime evidence,', 'target': 'production runtime evidence', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_development_runtime_evidence', 'statement': 'Enumerated item is supported/enforced: development runtime evidence.', 'target': 'development runtime evidence', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_implementation_files_or_an_approved_not_applicable_r', 'statement': 'Enumerated item is supported/enforced: implementation files, or an approved/not-applicable reason for documentation-only or other no-implementation paths,', 'target': 'implementation files, or an approved/not-applicable reason for documentation-only or other no-implementation paths', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_test_files_or_deterministic_not_applicable_evidence', 'statement': 'Enumerated item is supported/enforced: test files, or deterministic not-applicable evidence where tests are permitted to be not applicable,', 'target': 'test files, or deterministic not-applicable evidence where tests are permitted to be not applicable', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_changed_files_from_packet_change_baseline', 'statement': 'Enumerated item is supported/enforced: changed files from packet change baseline,', 'target': 'changed files from packet change baseline', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_ac_verification', 'statement': 'Enumerated item is supported/enforced: AC verification,', 'target': 'AC verification', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_docs_status', 'statement': 'Enumerated item is supported/enforced: docs status,', 'target': 'docs status', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_feature_source_evidence_status', 'statement': 'Enumerated item is supported/enforced: feature/source evidence status,', 'target': 'feature/source evidence status', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_cleanup_status', 'statement': 'Enumerated item is supported/enforced: cleanup status,', 'target': 'cleanup status', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_test_cleanup_verification_showing_no_unapproved_file', 'statement': 'Enumerated item is supported/enforced: test cleanup verification showing no unapproved files, database tables/rows, external resources, processes, or runtime state were left behind,', 'target': 'test cleanup verification showing no unapproved files, database tables/rows, external resources, processes, or runtime state were left behind', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_runtime_evidence_where_applicable', 'statement': 'Enumerated item is supported/enforced: runtime evidence where applicable,', 'target': 'runtime evidence where applicable', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_required_backend_verification_records', 'statement': 'Enumerated item is supported/enforced: required backend verification records,', 'target': 'required backend verification records', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_final_claim_audit', 'statement': 'Enumerated item is supported/enforced: final claim audit.', 'target': 'final claim audit', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True}
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
