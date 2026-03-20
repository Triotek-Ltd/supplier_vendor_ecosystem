"""Relation service seed for supplier_onboarding_case."""

from __future__ import annotations

from core.services.relation_resolution import RelationResolutionService


DOC_ID = "supplier_onboarding_case"
RELATED_DOCS = [{'doc_id': 'supplier_capability_profile', 'relation_type': 'related', 'show_in_related_panel': True}, {'doc_id': 'supplier_compliance_record', 'relation_type': 'related', 'show_in_related_panel': True}, {'doc_id': 'supplier_profile', 'relation_type': 'related', 'show_in_related_panel': True}]
FETCH_RULES = [{'source_field': 'related_supplier_capability_profile', 'doc_id': 'supplier_capability_profile', 'mode': 'context'}, {'source_field': 'related_supplier_compliance_record', 'doc_id': 'supplier_compliance_record', 'mode': 'context'}, {'source_field': 'related_supplier_profile', 'doc_id': 'supplier_profile', 'mode': 'context'}]

BORROWED_FIELDS = [{'description': 'supplier identity from ecosystem or operations supplier records where linked'}, {'field_id': 'related_supplier_capability_profile', 'doc_id': 'supplier_capability_profile', 'description': 'Borrow context from supplier_capability_profile through related_supplier_capability_profile.'}, {'field_id': 'related_supplier_compliance_record', 'doc_id': 'supplier_compliance_record', 'description': 'Borrow context from supplier_compliance_record through related_supplier_compliance_record.'}, {'field_id': 'related_supplier_profile', 'doc_id': 'supplier_profile', 'description': 'Borrow context from supplier_profile through related_supplier_profile.'}]

class RelationService:
    def _bridge(self, context: dict | None = None) -> RelationResolutionService | None:
        viewset = (context or {}).get("viewset")
        return RelationResolutionService(viewset) if viewset is not None else None

    def resolve_create_relations(self, payload: dict, context: dict | None = None) -> dict:
        bridge = self._bridge(context)
        return bridge.resolve_create_relations(payload) if bridge else {"data": payload}

    def resolve_update_relations(self, instance, payload: dict, context: dict | None = None) -> dict:
        bridge = self._bridge(context)
        return bridge.resolve_update_relations(instance, payload) if bridge else {"data": payload}

    def shape_retrieve_data(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        bridge = self._bridge(context)
        return bridge.serialize_related(instance, serialized_data) if bridge else serialized_data

    def related_targets(self) -> list:
        return RELATED_DOCS

    def borrowed_field_notes(self) -> list:
        return [item.get("description") for item in BORROWED_FIELDS if isinstance(item, dict)]

    def relation_profile(self) -> dict:
        return {
            "related_docs": self.related_targets(),
            "borrowed_fields": self.borrowed_field_notes(),
            "fetch_rule_count": len(FETCH_RULES),
        }
