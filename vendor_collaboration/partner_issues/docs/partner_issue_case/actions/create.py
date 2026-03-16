"""Action handler seed for partner_issue_case:create."""

from __future__ import annotations


DOC_ID = "partner_issue_case"
ACTION_ID = "create"
ACTION_RULE = {'allowed_in_states': ['opened', 'triaged', 'in_progress', 'resolved', 'escalated'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['vendor_portal_account', 'collaboration_request', 'contract_review_case', 'delivery_exception_case'], 'borrowed_fields': ['vendor', 'contract context from linked records'], 'inferred_roles': ['compliance officer', 'procurement officer', 'operations coordinator', 'case owner']}, 'actors': ['compliance officer', 'procurement officer', 'operations coordinator', 'case owner'], 'action_actors': {'create': ['compliance officer'], 'assign': ['compliance officer'], 'close': ['case owner'], 'archive': ['case owner']}}

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
