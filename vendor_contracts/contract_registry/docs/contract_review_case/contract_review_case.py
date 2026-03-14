"""Doc runtime hooks for contract_review_case."""

class DocRuntime:
    doc_key = "contract_review_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'review', 'amend', 'renew', 'close', 'archive']
