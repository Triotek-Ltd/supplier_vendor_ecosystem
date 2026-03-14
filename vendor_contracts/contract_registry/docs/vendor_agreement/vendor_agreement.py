"""Doc runtime hooks for vendor_agreement."""

class DocRuntime:
    doc_key = "vendor_agreement"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'activate', 'renew', 'archive']
