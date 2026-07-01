from __future__ import annotations

import json
from dataclasses import asdict

from .schemas import ExtractionResult


def to_markdown_table(result: ExtractionResult) -> str:
    lines = [
        "| Field | Exists | Extracted Content |",
        "| --- | --- | --- |",
    ]
    for record in result.records:
        value = record.value.replace("\n", "<br>")
        lines.append(f"| {record.field} | {record.exists} | {value} |")
    return "\n".join(lines)


def to_json(result: ExtractionResult) -> str:
    payload = {
        "scenario": result.scenario.value,
        "records": [asdict(record) for record in result.records],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)
