"""Executable specification for US-20: Migration."""

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
    {'name': 'when_reading_existing_artifacts_spec_guard_must', 'statement': 'When reading existing artifacts, Spec Guard must:', 'target': 'When reading existing artifacts, Spec Guard must:', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'reject_future_writes_that_omit_required_canonical_fields', 'statement': 'reject future writes that omit required canonical fields,', 'target': 'reject future writes that omit required canonical fields', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'never_fabricate_human_decisions', 'statement': 'never fabricate human decisions,', 'target': 'never fabricate human decisions', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'never_fabricate_backend_verification_records', 'statement': 'never fabricate backend verification records,', 'target': 'never fabricate backend verification records', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'migration_must_not_create_verifier_records_that_judge_human_approved_content', 'statement': 'Migration must not create verifier records that judge human-approved content.', 'target': 'Migration must not create verifier records that judge human-approved content', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_migrate_known_synonymous_fields_into_canonical_field', 'statement': 'Enumerated item is supported/enforced: migrate known synonymous fields into canonical fields,', 'target': 'migrate known synonymous fields into canonical fields', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_preserve_raw_legacy_values_where_useful', 'statement': 'Enumerated item is supported/enforced: preserve raw legacy values where useful,', 'target': 'preserve raw legacy values where useful', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_reject_future_writes_that_omit_required_canonical_fi', 'statement': 'Enumerated item is supported/enforced: reject future writes that omit required canonical fields,', 'target': 'reject future writes that omit required canonical fields', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_warn_on_boilerplate_generated_scope_without_silently', 'statement': 'Enumerated item is supported/enforced: warn on boilerplate generated scope without silently deleting it,', 'target': 'warn on boilerplate generated scope without silently deleting it', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_reconstruct_parent_child_links_when_possible', 'statement': 'Enumerated item is supported/enforced: reconstruct parent/child links when possible,', 'target': 'reconstruct parent/child links when possible', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_leave_optional_intent_fields_empty_unless_drafted', 'statement': 'Enumerated item is supported/enforced: leave optional intent fields empty unless drafted,', 'target': 'leave optional intent fields empty unless drafted', 'authority': 'Authority.FRONTEND_AGENT', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_never_fabricate_human_decisions', 'statement': 'Enumerated item is supported/enforced: never fabricate human decisions,', 'target': 'never fabricate human decisions', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_never_fabricate_backend_verification_records', 'statement': 'Enumerated item is supported/enforced: never fabricate backend verification records,', 'target': 'never fabricate backend verification records', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_invalidate_approvals_when_migration_changes_approved', 'statement': 'Enumerated item is supported/enforced: invalidate approvals when migration changes approved semantics.', 'target': 'invalidate approvals when migration changes approved semantics', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True}
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
