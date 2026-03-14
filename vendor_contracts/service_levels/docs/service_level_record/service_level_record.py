"""Doc runtime hooks for service_level_record."""

class DocRuntime:
    doc_key = "service_level_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'archive']
