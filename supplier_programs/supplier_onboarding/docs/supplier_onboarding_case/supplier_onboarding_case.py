"""Doc runtime hooks for supplier_onboarding_case."""

class DocRuntime:
    doc_key = "supplier_onboarding_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'review', 'approve', 'reject', 'close', 'archive']
