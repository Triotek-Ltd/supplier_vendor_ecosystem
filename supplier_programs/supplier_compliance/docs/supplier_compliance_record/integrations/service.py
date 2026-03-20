"""Integration-service seed for supplier_compliance_record."""

from __future__ import annotations


DOC_ID = "supplier_compliance_record"
INTEGRATION_RULES = {'external_refs': [{'field_id': 'supplier_reference', 'kind': 'supplier', 'label': 'Supplier Reference'}], 'sync_rules': []}

class IntegrationService:
    def sync_rules(self) -> list:
        return INTEGRATION_RULES.get("sync_rules", [])

    def integration_profile(self) -> dict:
        return {'external_sync_enabled': True, 'tracks_external_refs': True}
