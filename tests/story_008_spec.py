"""Executable specification for US-08: Product platform and architecture decisions."""

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
    {'name': 'a_work_packet_s_platform_required_is_true_for_every_packet_except_operational_document_pac', 'statement': "A Work Packet's `platform.required` is true for every packet except `operational_document` packets whose approved scope changes only documentation/operational content and packets whose platform is inherited from an approved parent Plan `product_context.platform_decision_id` or an accepted RuntimeBaseline `stack.product_platform`.", 'target': "A Work Packet's `platform.required` is true for every packet except `operational_document` packets whose approved scope changes only documentation/operational c", 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'when_platform_required_is_false_platform_not_required_reason_must_record_the_deterministic', 'statement': 'When `platform.required` is false, `platform.not_required_reason` must record the deterministic basis.', 'target': 'When `platform.required` is false, `platform.not_required_reason` must record the deterministic basis', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'when_true_packet_approval_readiness_requires_platform_decision_id_to_reference_a_recorded', 'statement': 'When true, packet approval readiness requires `platform.decision_id` to reference a recorded `platform_choice` HumanDecision.', 'target': 'When true, packet approval readiness requires `platform.decision_id` to reference a recorded `platform_choice` HumanDecision', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'the_frontend_agent_must_present_a_relevant_numbered_option_list_based_on_request_repositor', 'statement': 'The frontend agent must present a relevant numbered option list based on request, repository context, and observable facts.', 'target': 'The frontend agent must present a relevant numbered option list based on request, repository context, and observable facts', 'authority': 'Authority.FRONTEND_AGENT', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'custom_prose_support', 'statement': 'custom prose support.', 'target': 'custom prose support', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'custom_platform_text_is_captured_as_human_text_after_numbered_confirmation', 'statement': 'Custom platform text is captured as human text after numbered confirmation.', 'target': 'Custom platform text is captured as human text after numbered confirmation', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'spec_guard_must_not_map_custom_platform_text_to_a_hard_coded_equivalent_after_confirmation', 'statement': 'Spec Guard must not map custom platform text to a hard-coded equivalent after confirmation.', 'target': 'Spec Guard must not map custom platform text to a hard-coded equivalent after confirmation', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'a_platform_choice_must_record_a_humandecision_with_decision_type_platform_choice', 'statement': 'A platform choice must record a HumanDecision with decision type `platform_choice`.', 'target': 'A platform choice must record a HumanDecision with decision type `platform_choice`', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'work_choice_propose_must_store_each_final_platform_option_with_a_structured_payload_suffic', 'statement': '`work.choice.propose` must store each final platform option with a structured payload sufficient to construct PlatformChoiceDecisionPayload.', 'target': '`work.choice.propose` must store each final platform option with a structured payload sufficient to construct PlatformChoiceDecisionPayload', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'work_choice_answer_or_work_choice_confirm_custom_must_store_a_canonical_platformchoicedeci', 'statement': '`work.choice.answer` or `work.choice.confirm_custom` must store a canonical PlatformChoiceDecisionPayload in `approved_payload`', 'target': '`work.choice.answer` or `work.choice.confirm_custom` must store a canonical PlatformChoiceDecisionPayload in `approved_payload`', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'update_the_work_packet_platform_decision_reference', 'statement': 'update the Work Packet platform decision reference.', 'target': 'update the Work Packet platform decision reference', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'discuss_and_unconfirmed_custom_prose_create_no_humandecision', 'statement': 'Discuss and unconfirmed custom prose create no HumanDecision.', 'target': 'Discuss and unconfirmed custom prose create no HumanDecision', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'plan_approval_does_not_create_platform_choices', 'statement': 'Plan approval does not create platform choices.', 'target': 'Plan approval does not create platform choices', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'planproposalpayload_product_context_platform_decision_id_may_only_copy_an_already_recorded', 'statement': '`PlanProposalPayload.product_context.platform_decision_id` may only copy an already recorded platform HumanDecision id, and `platform_choice` is traceability text for that decision.', 'target': '`PlanProposalPayload.product_context.platform_decision_id` may only copy an already recorded platform HumanDecision id, and `platform_choice` is traceability te', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'if_a_plan_child_requires_a_platform_choice_and_no_platform_decision_id_is_present_the_chil', 'statement': 'If a Plan child requires a platform choice and no platform decision id is present, the child is not eligible for batch approval or authorization until the platform gate records the decision on that child.', 'target': 'If a Plan child requires a platform choice and no platform decision id is present, the child is not eligible for batch approval or authorization until the platf', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'batch_approval_must_not_choose_platform', 'statement': 'Batch approval must not choose platform.', 'target': 'Batch approval must not choose platform', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'when_architecture_affects_implementation_persistence_runtime_deployment_api_boundaries_or', 'statement': 'When architecture affects implementation, persistence, runtime, deployment, API boundaries, or test strategy, Spec Guard must require human architecture review.', 'target': 'When architecture affects implementation, persistence, runtime, deployment, API boundaries, or test strategy, Spec Guard must require human architecture review', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'architecture_required_is_true_for_api_contract_surface_classifications_and_whenever_work_i', 'statement': '`architecture.required` is true for API/contract-surface classifications and whenever `work.intent.draft` or `work.update` sets `architecture.required: true` with a non-empty `required_reason`.', 'target': '`architecture.required` is true for API/contract-surface classifications and whenever `work.intent.draft` or `work.update` sets `architecture.required: true` wi', 'authority': 'Authority.FRONTEND_AGENT', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'it_is_false_for_documentation_only_operational_document_packets_and_may_be_false_for_local', 'statement': 'It is false for documentation-only `operational_document` packets and may be false for localized direct behavior/bugfix/one-off UI packets only when `architecture.not_required_reason` records the deterministic basis.', 'target': 'It is false for documentation-only `operational_document` packets and may be false for localized direct behavior/bugfix/one-off UI packets only when `architectu', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'packet_approval_readiness_requires_at_least_one_architecture_decision_id_when_architecture', 'statement': 'Packet approval readiness requires at least one architecture decision id when `architecture.required` is true.', 'target': 'Packet approval readiness requires at least one architecture decision id when `architecture.required` is true', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'each_architecture_option_must_include', 'statement': 'Each architecture option must include:', 'target': 'Each architecture option must include:', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'the_prompt_must_include_something_else_and_discuss', 'statement': 'The prompt must include Something else and Discuss.', 'target': 'The prompt must include Something else and Discuss', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'custom_architecture_requires_numbered_confirmation', 'statement': 'Custom architecture requires numbered confirmation.', 'target': 'Custom architecture requires numbered confirmation', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'work_choice_propose_must_store_each_architecture_option_with_its_label_description_benefit', 'statement': '`work.choice.propose` must store each architecture option with its label, description, benefits, costs/tradeoffs, and downstream constraints in a structured option payload.', 'target': '`work.choice.propose` must store each architecture option with its label, description, benefits, costs/tradeoffs, and downstream constraints in a structured opt', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'an_architecture_choice_must_record_a_humandecision_with_decision_type_architecture_choice', 'statement': 'An architecture choice must record a HumanDecision with decision type `architecture_choice`.', 'target': 'An architecture choice must record a HumanDecision with decision type `architecture_choice`', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'work_choice_answer_or_work_choice_confirm_custom_must_store_a_canonical_architecturechoice', 'statement': '`work.choice.answer` or `work.choice.confirm_custom` must store a canonical ArchitectureChoiceDecisionPayload in `approved_payload`', 'target': '`work.choice.answer` or `work.choice.confirm_custom` must store a canonical ArchitectureChoiceDecisionPayload in `approved_payload`', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'update_the_affected_work_packet_architecture_decision_references', 'statement': 'update the affected Work Packet architecture decision references.', 'target': 'update the affected Work Packet architecture decision references', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': False},
    {'name': 'plan_approval_does_not_create_architecture_choices', 'statement': 'Plan approval does not create architecture choices.', 'target': 'Plan approval does not create architecture choices', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'planproposalpayload_product_context_architecture_decision_ids_may_only_copy_already_record', 'statement': '`PlanProposalPayload.product_context.architecture_decision_ids` may only copy already recorded architecture HumanDecision ids.', 'target': '`PlanProposalPayload.product_context.architecture_decision_ids` may only copy already recorded architecture HumanDecision ids', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.OBSERVABLE', 'blocking': True},
    {'name': 'if_a_plan_child_requires_architecture_review_and_no_architecture_decision_id_is_present_th', 'statement': 'If a Plan child requires architecture review and no architecture decision id is present, the child is not eligible for batch approval or authorization until the architecture gate records the decision on that child.', 'target': 'If a Plan child requires architecture review and no architecture decision id is present, the child is not eligible for batch approval or authorization until the', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.YES', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'batch_approval_must_not_choose_architecture', 'statement': 'Batch approval must not choose architecture.', 'target': 'Batch approval must not choose architecture', 'authority': 'Authority.HUMAN', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'the_backend_verifier_must_not_judge_architecture_quality', 'statement': 'The backend verifier must not judge architecture quality.', 'target': 'The backend verifier must not judge architecture quality', 'authority': 'Authority.BACKEND_VERIFIER', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.BLOCKING', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_numbered_platform_options', 'statement': 'Enumerated item is supported/enforced: numbered platform options,', 'target': 'numbered platform options', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_something_else', 'statement': 'Enumerated item is supported/enforced: Something else,', 'target': 'Something else', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_discuss', 'statement': 'Enumerated item is supported/enforced: Discuss,', 'target': 'Discuss', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_custom_prose_support', 'statement': 'Enumerated item is supported/enforced: custom prose support.', 'target': 'custom prose support', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_label', 'statement': 'Enumerated item is supported/enforced: label,', 'target': 'label', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_description', 'statement': 'Enumerated item is supported/enforced: description,', 'target': 'description', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_benefits', 'statement': 'Enumerated item is supported/enforced: benefits,', 'target': 'benefits', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_costs_tradeoffs', 'statement': 'Enumerated item is supported/enforced: costs/tradeoffs,', 'target': 'costs/tradeoffs', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True},
    {'name': 'enumerated_item_is_supported_enforced_downstream_constraints_or_lock_in_where_relevant', 'statement': 'Enumerated item is supported/enforced: downstream constraints or lock-in where relevant.', 'target': 'downstream constraints or lock-in where relevant', 'authority': 'Authority.DETERMINISTIC_KERNEL', 'mutation': 'MutationMode.NO', 'level': 'EnforcementLevel.REQUIRED', 'blocking': True}
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
