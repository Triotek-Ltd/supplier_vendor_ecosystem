"""Doc runtime hooks for collaboration_request."""

class DocRuntime:
    doc_key = "collaboration_request"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'accept', 'complete', 'cancel', 'archive']
