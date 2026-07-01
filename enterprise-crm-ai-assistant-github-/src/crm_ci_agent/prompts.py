from __future__ import annotations

from .schemas import FieldSpec, Scenario


SYSTEM_PROMPT = """You are a CRM competitive intelligence extraction assistant.
Extract only information explicitly supported by the provided source text.
If a field cannot be verified, return "Not Mentioned".
Do not infer, summarize, recommend actions, or use prior industry knowledge.
Return every schema field with an existence flag and extracted content."""


def build_extraction_prompt(scenario: Scenario, schema: list[FieldSpec], source_text: str) -> str:
    fields = "\n".join(f"- {field.name}: {field.description}" for field in schema)
    return f"""{SYSTEM_PROMPT}

Scenario:
{scenario.value}

Schema fields:
{fields}

Output contract:
- For each field, return:
  - field
  - exists: one of "Yes", "No", "Not Mentioned"
  - value: exact extracted content or "Not Mentioned"
- Use "No" only when the source explicitly says the item does not exist.
- Use "Not Mentioned" when the source does not provide enough evidence.

Source text:
{source_text}
"""
