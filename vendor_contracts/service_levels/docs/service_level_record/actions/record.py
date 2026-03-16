"""Action handler seed for service_level_record:record."""

from __future__ import annotations


DOC_ID = "service_level_record"
ACTION_ID = "record"
ACTION_RULE = {'allowed_in_states': ['active', 'reviewed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['vendor_agreement', 'contract_review_case', 'vendor_review'], 'borrowed_fields': ['SLA targets', 'vendor identity from vendor_agreement'], 'inferred_roles': ['compliance officer', 'procurement officer', 'case owner']}, 'actors': ['compliance officer', 'procurement officer', 'case owner'], 'action_actors': {'record': ['compliance officer'], 'review': ['procurement officer'], 'archive': ['case owner']}}

def handle_record(payload: dict, context: dict | None = None) -> dict:
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
