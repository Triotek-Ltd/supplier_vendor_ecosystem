"""Doc runtime hooks for vendor_portal_account."""

class DocRuntime:
    doc_key = "vendor_portal_account"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'provision', 'activate', 'suspend', 'archive']
