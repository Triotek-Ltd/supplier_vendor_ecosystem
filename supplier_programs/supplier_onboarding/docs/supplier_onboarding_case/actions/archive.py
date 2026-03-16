"""Action handler seed for supplier_onboarding_case:archive."""

from __future__ import annotations


DOC_ID = "supplier_onboarding_case"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['opened', 'in_review', 'approved', 'rejected'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['supplier_capability_profile', 'supplier_compliance_record', 'supplier_profile'], 'borrowed_fields': ['supplier identity from ecosystem or operations supplier records where linked'], 'inferred_roles': ['compliance officer', 'procurement officer', 'case owner']}, 'actors': ['compliance officer', 'procurement officer', 'case owner'], 'action_actors': {'create': ['compliance officer'], 'assign': ['compliance officer'], 'review': ['procurement officer'], 'approve': ['compliance officer'], 'reject': ['compliance officer'], 'close': ['case owner'], 'archive': ['case owner']}}

def handle_archive(payload: dict, context: dict | None = None) -> dict:
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
