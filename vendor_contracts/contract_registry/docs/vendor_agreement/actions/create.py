"""Action handler seed for vendor_agreement:create."""

from __future__ import annotations


DOC_ID = "vendor_agreement"
ACTION_ID = "create"
ACTION_RULE = {'allowed_in_states': ['draft', 'approved', 'active', 'expired', 'renewed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['service_level_record', 'contract_review_case', 'vendor_contract'], 'borrowed_fields': ['supplier identity', 'capability context from supplier_capability_profile'], 'inferred_roles': ['compliance officer', 'procurement officer', 'case owner']}, 'actors': ['compliance officer', 'procurement officer', 'case owner'], 'action_actors': {'create': ['compliance officer'], 'review': ['procurement officer'], 'approve': ['compliance officer'], 'activate': ['case owner'], 'archive': ['case owner']}}

def handle_create(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = ACTION_RULE.get("transitions_to")
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
