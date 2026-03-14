"""Doc runtime hooks for supplier_compliance_record."""

class DocRuntime:
    doc_key = "supplier_compliance_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'renew', 'expire', 'archive']
