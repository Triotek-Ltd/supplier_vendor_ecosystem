"""Doc runtime hooks for supplier_capability_profile."""

class DocRuntime:
    doc_key = "supplier_capability_profile"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'archive']
