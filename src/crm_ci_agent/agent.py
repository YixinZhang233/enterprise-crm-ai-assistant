from __future__ import annotations

import re

from .prompts import build_extraction_prompt
from .schemas import (
    NOT_MENTIONED,
    ExtractionRecord,
    ExtractionResult,
    Scenario,
    get_schema,
)


class DeterministicMockExtractor:
    """Demo extractor that fills schema fields from simple public mock text.

    This keeps the repository runnable without API keys. Replace this class
    with an LLM provider for real screenshot extraction.
    """

    def extract(self, scenario: Scenario, source_text: str) -> ExtractionResult:
        schema = get_schema(scenario)
        records = []
        for field in schema:
            value = self._find_value(field.name, source_text)
            exists = "Yes" if value != NOT_MENTIONED else NOT_MENTIONED
            records.append(ExtractionRecord(field=field.name, exists=exists, value=value))
        return ExtractionResult(scenario=scenario, records=records)

    @staticmethod
    def _find_value(field_name: str, source_text: str) -> str:
        patterns = [
            rf"^{re.escape(field_name)}\s*:\s*(.+)$",
            rf"^- {re.escape(field_name)}\s*:\s*(.+)$",
        ]
        for pattern in patterns:
            match = re.search(pattern, source_text, flags=re.IGNORECASE | re.MULTILINE)
            if match:
                value = match.group(1).strip()
                return value if value else NOT_MENTIONED
        return NOT_MENTIONED


class CrmCompetitiveIntelligenceAgent:
    def __init__(self, extractor: DeterministicMockExtractor | None = None) -> None:
        self.extractor = extractor or DeterministicMockExtractor()

    def build_prompt(self, scenario: Scenario, source_text: str) -> str:
        return build_extraction_prompt(scenario, get_schema(scenario), source_text)

    def run(self, scenario: Scenario, source_text: str) -> ExtractionResult:
        return self.extractor.extract(scenario, source_text)
