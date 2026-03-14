"""Doc runtime hooks for partner_issue_case."""

class DocRuntime:
    doc_key = "partner_issue_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'triage', 'resolve', 'escalate', 'close', 'archive']
