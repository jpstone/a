"""Executable specification for US-03: Choice, gate, and prompt semantics."""

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
    {'name': 'all_governed_choices_shown_to_the_human_must_be_numbered', 'statement': 'All governed choices shown to the human must be numbered.', 'target': 'All governed choices shown to the human must be numbered', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'governed_decision_approval_authorization_acceptance_and_final_intent_state_mutates_only_fr', 'statement': 'Governed decision, approval, authorization, acceptance, and final intent state mutates only from a numbered human selection.', 'target': 'Governed decision, approval, authorization, acceptance, and final intent state mutates only from a numbered human selection', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'draft_artifacts_audit_records_command_results_evidence_records_configuration_and_determini', 'statement': 'Draft artifacts, audit records, command results, evidence records, configuration, and deterministic validation records may mutate through their registered actions without being human decisions unless this specification explicitly requires a human gate.', 'target': 'Draft artifacts, audit records, command results, evidence records, configuration, and deterministic validation records may mutate through their registered actio', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'prompt_proposal_actions_may_persist_pending_prompt_audit_records_as_audit_only_records_but', 'statement': 'Prompt proposal actions may persist pending prompt/audit records as audit-only records, but they must not record a governed decision or mutate decision state before the human selects a number.', 'target': 'Prompt proposal actions may persist pending prompt/audit records as audit-only records, but they must not record a governed decision or mutate decision state be', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.AUDIT_ONLY', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'any_structured_data_needed_to_later_record_a_decision_must_be_included_in_the_prompt_recor', 'statement': 'Any structured data needed to later record a decision must be included in the prompt record, not reconstructed from frontend-agent prose.', 'target': 'Any structured data needed to later record a decision must be included in the prompt record, not reconstructed from frontend-agent prose', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'non_binary_semantic_choices_must_include', 'statement': 'Non-binary semantic choices must include:', 'target': 'Non-binary semantic choices must include:', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'custom_prose_support', 'statement': 'custom prose support.', 'target': 'custom prose support', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'non_binary_semantic_choices_include', 'statement': 'Non-binary semantic choices include:', 'target': 'Non-binary semantic choices include:', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'the_frontend_agent_must_re_present_it_as_a_numbered_confirmation', 'statement': 'The frontend agent must re-present it as a numbered confirmation:', 'target': 'The frontend agent must re-present it as a numbered confirmation:', 'authority': 'Authority.FRONTEND_AGENT', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'use_decision_as_the_proposed_choice', 'statement': 'Use `<decision>` as the proposed `<choice>`', 'target': 'Use `<decision>` as the proposed `<choice>`', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'do_not_use_this_decision', 'statement': 'Do not use this decision', 'target': 'Do not use this decision', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'only_option_1_records_the_decision', 'statement': 'Only option 1 records the decision.', 'target': 'Only option 1 records the decision', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'for_custom_confirmation_prompts_option_2_records_no_humandecision_and_leaves_the_prior_cho', 'statement': 'For custom confirmation prompts, option 2 records no HumanDecision and leaves the prior choice unset', 'target': 'For custom confirmation prompts, option 2 records no HumanDecision and leaves the prior choice unset', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'if_the_workflow_needs_a_block_or_decline_it_must_use_the_relevant_binary_gate', 'statement': 'if the workflow needs a block or decline, it must use the relevant binary gate.', 'target': 'if the workflow needs a block or decline, it must use the relevant binary gate', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'option_3_records_no_mutation', 'statement': 'Option 3 records no mutation.', 'target': 'Option 3 records no mutation', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'spec_guard_validates_prompt_shape_not_semantic_clarity_of_free_form_human_prose', 'statement': 'Spec Guard validates prompt shape, not semantic clarity of free-form human prose.', 'target': 'Spec Guard validates prompt shape, not semantic clarity of free-form human prose', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'must_never_become_non_binary_prompts', 'statement': 'must never become non-binary prompts.', 'target': 'must never become non-binary prompts', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'binary_gates_must_be', 'statement': 'Binary gates must be:', 'target': 'Binary gates must be:', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'if_the_human_selects_discuss_the_frontend_agent_may_discuss_but_later_resolution_must_re_p', 'statement': 'If the human selects Discuss, the frontend agent may discuss, but later resolution must re-present the same Yes/No/Discuss gate.', 'target': 'If the human selects Discuss, the frontend agent may discuss, but later resolution must re-present the same Yes/No/Discuss gate', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'discussion_derived_text_must_not_replace_yes', 'statement': 'Discussion-derived text must not replace Yes', 'target': 'Discussion-derived text must not replace Yes', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'must_not_become_a_custom_gate_option', 'statement': 'must not become a custom gate option.', 'target': 'must not become a custom gate option', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'only_numbered_yes_mutates_the_gated_state', 'statement': 'Only numbered Yes mutates the gated state.', 'target': 'Only numbered Yes mutates the gated state', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'numbered_no_records_decline_or_blocks_as_specified_by_the_gate', 'statement': 'Numbered No records decline or blocks as specified by the gate', 'target': 'Numbered No records decline or blocks as specified by the gate', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'records_a_humandecision_with_approved_fields_unless_the_action_is_specified_as_audit_only', 'statement': 'records a HumanDecision with `approved_fields: []` unless the action is specified as audit-only.', 'target': 'records a HumanDecision with `approved_fields: []` unless the action is specified as audit-only', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.AUDIT_ONLY', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'discuss_records_no_governed_mutation', 'statement': 'Discuss records no governed mutation', 'target': 'Discuss records no governed mutation', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'must_not_create_a_humandecision', 'statement': 'must not create a HumanDecision', 'target': 'must not create a HumanDecision', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'implementations_may_record_audit_only_prompt_answer_records_for_discuss', 'statement': 'implementations may record audit-only prompt/answer records for Discuss.', 'target': 'implementations may record audit-only prompt/answer records for Discuss', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.AUDIT_ONLY', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'binary_gates_include', 'statement': 'Binary gates include:', 'target': 'Binary gates include:', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'they_must_not_include_something_else_or_custom_prose_support', 'statement': 'They must not include Something else or custom prose support.', 'target': 'They must not include Something else or custom prose support', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'selecting_option_1_or_option_2_records_a_humandecision_for_the_fixed_decision', 'statement': 'Selecting option 1 or option 2 records a HumanDecision for the fixed decision.', 'target': 'Selecting option 1 or option 2 records a HumanDecision for the fixed decision', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'discuss_mutates_nothing_creates_no_humandecision_and_later_re_presents_the_same_fixed_deci', 'statement': 'Discuss mutates nothing, creates no HumanDecision, and later re-presents the same fixed decision.', 'target': 'Discuss mutates nothing, creates no HumanDecision, and later re-presents the same fixed decision', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'fixed_binary_decisions_include', 'statement': 'Fixed binary decisions include:', 'target': 'Fixed binary decisions include:', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'enumerated_item_is_supported_enforced_relevant_numbered_options', 'statement': 'Enumerated item is supported/enforced: relevant numbered options,', 'target': 'relevant numbered options', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_something_else', 'statement': 'Enumerated item is supported/enforced: `Something else`,', 'target': '`Something else`', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_discuss', 'statement': 'Enumerated item is supported/enforced: `Discuss`,', 'target': '`Discuss`', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_custom_prose_support', 'statement': 'Enumerated item is supported/enforced: custom prose support.', 'target': 'custom prose support', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_product_platform_type', 'statement': 'Enumerated item is supported/enforced: product/platform type,', 'target': 'product/platform type', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_architecture', 'statement': 'Enumerated item is supported/enforced: architecture.', 'target': 'architecture', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'ordered_requirement_is_supported_enforced_use_decision_as_the_proposed_choice', 'statement': 'Ordered requirement is supported/enforced: Use `<decision>` as the proposed `<choice>`', 'target': 'Ordered requirement is supported/enforced: Use `<decision>` as the proposed `<choice>`', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'ordered_requirement_is_supported_enforced_do_not_use_this_decision', 'statement': 'Ordered requirement is supported/enforced: Do not use this decision', 'target': 'Ordered requirement is supported/enforced: Do not use this decision', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'ordered_requirement_is_supported_enforced_discuss', 'statement': 'Ordered requirement is supported/enforced: Discuss', 'target': 'Ordered requirement is supported/enforced: Discuss', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'ordered_requirement_is_supported_enforced_yes', 'statement': 'Ordered requirement is supported/enforced: Yes', 'target': 'Ordered requirement is supported/enforced: Yes', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'ordered_requirement_is_supported_enforced_no', 'statement': 'Ordered requirement is supported/enforced: No', 'target': 'Ordered requirement is supported/enforced: No', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_runtime_baseline_acceptance', 'statement': 'Enumerated item is supported/enforced: runtime baseline acceptance,', 'target': 'runtime baseline acceptance', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_ac_approval', 'statement': 'Enumerated item is supported/enforced: AC approval,', 'target': 'AC approval', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_work_packet_approval', 'statement': 'Enumerated item is supported/enforced: Work Packet approval,', 'target': 'Work Packet approval', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_implementation_authorization', 'statement': 'Enumerated item is supported/enforced: implementation authorization,', 'target': 'implementation authorization', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_plan_approval', 'statement': 'Enumerated item is supported/enforced: Plan approval.', 'target': 'Plan approval', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'ordered_requirement_is_supported_enforced_first_domain_outcome', 'statement': 'Ordered requirement is supported/enforced: First domain outcome', 'target': 'Ordered requirement is supported/enforced: First domain outcome', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'ordered_requirement_is_supported_enforced_second_domain_outcome', 'statement': 'Ordered requirement is supported/enforced: Second domain outcome', 'target': 'Ordered requirement is supported/enforced: Second domain outcome', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_plan_vs_single_packet_choice', 'statement': 'Enumerated item is supported/enforced: Plan-vs-single-packet choice.', 'target': 'Plan-vs-single-packet choice', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True}
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
