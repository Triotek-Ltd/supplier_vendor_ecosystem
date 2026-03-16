"""Action handler seed for supplier_compliance_record:create."""

from __future__ import annotations


DOC_ID = "supplier_compliance_record"
ACTION_ID = "create"
ACTION_RULE = {'allowed_in_states': ['active', 'expired'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['supplier_onboarding_case', 'supplier_capability_profile', 'vendor_review'], 'borrowed_fields': ['supplier identity', 'capabilities from linked records'], 'inferred_roles': ['compliance officer', 'procurement officer', 'case owner']}, 'actors': ['compliance officer', 'procurement officer', 'case owner'], 'action_actors': {'create': ['compliance officer'], 'review': ['procurement officer'], 'archive': ['case owner']}}

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
