# Architecture

The project uses a small agent pipeline that can be swapped from mock extraction to real LLM extraction.

## Components

| Component | File | Responsibility |
| --- | --- | --- |
| Scenario registry | `src/crm_ci_agent/schemas.py` | Defines supported CRM scenarios and field schemas. |
| Prompt builder | `src/crm_ci_agent/prompts.py` | Builds evidence-grounded extraction prompts. |
| OCR placeholder | `src/crm_ci_agent/ocr.py` | Reads public transcript files and represents future OCR integration. |
| Agent | `src/crm_ci_agent/agent.py` | Routes scenario and source text to an extractor. |
| Exporters | `src/crm_ci_agent/exporters.py` | Converts structured results to Markdown and JSON. |
| CLI | `src/crm_ci_agent/cli.py` | Provides a command-line demo interface. |

## Data Flow

1. A user selects one of the six supported CRM scenarios.
2. The screenshot is converted to source text by OCR, a vision model, or manual transcript.
3. The agent loads the matching schema from the registry.
4. The extraction prompt instructs the LLM to use evidence only.
5. Output is normalized into `field`, `exists`, and `value`.
6. Exporters generate Markdown and JSON.

## Production Extension

For production usage, implement an extractor with the same interface as `DeterministicMockExtractor`:

```python
class LlmExtractor:
    def extract(self, scenario: Scenario, source_text: str) -> ExtractionResult:
        ...
```

Recommended production additions:

- OCR or multimodal model integration.
- JSON schema validation.
- Evidence spans for each extracted field.
- Confidence scoring.
- Human review queue for low-confidence records.
- Batch processing for competitor monitoring.
