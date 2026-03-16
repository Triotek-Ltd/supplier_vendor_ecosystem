"""Action handler seed for vendor_portal_account:provision."""

from __future__ import annotations


DOC_ID = "vendor_portal_account"
ACTION_ID = "provision"
ACTION_RULE = {'allowed_in_states': ['requested', 'provisioned', 'active', 'suspended'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['collaboration_request', 'partner_issue_case', 'supplier_capability_profile'], 'borrowed_fields': ['vendor identity from linked partner/profile records'], 'inferred_roles': ['procurement officer', 'case owner']}, 'actors': ['procurement officer', 'case owner'], 'action_actors': {'create': ['procurement officer'], 'activate': ['case owner'], 'archive': ['case owner']}}

def handle_provision(payload: dict, context: dict | None = None) -> dict:
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
