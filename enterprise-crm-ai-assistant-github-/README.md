# Enterprise CRM AI Assistant

A public, mock-data reimplementation of a CRM competitive intelligence agent. The project demonstrates how an LLM-powered workflow can extract structured CRM information from screenshots, route the task to a scenario-specific schema, and return consistent Markdown and JSON outputs.

The repository is designed for portfolio and learning purposes. It does not include confidential company information, customer data, or real brand-sensitive material.

## Project Overview

Enterprise CRM teams often need to review competitor CRM touchpoints such as membership pages, member-day campaigns, customer lifecycle messages, and benefits pages. Manual extraction is slow and inconsistent.

This project provides a lightweight AI assistant pattern:

1. Select a CRM scenario type.
2. Convert screenshot content into text through an OCR placeholder.
3. Route the text to the matching extraction schema.
4. Extract only evidence-backed fields.
5. Output a Markdown table and JSON payload.

If a field cannot be confirmed from the input, the assistant returns `Not Mentioned` instead of guessing.

## Features

- Scenario-based schema routing for six CRM intelligence use cases.
- Prompt templates for evidence-grounded structured extraction.
- OCR placeholder for screenshot-to-text workflows.
- Unified Markdown table and JSON output.
- Mock sample inputs and outputs suitable for public GitHub sharing.
- Deterministic demo extractor that runs without an LLM API key.
- Optional extension point for OpenAI, Azure OpenAI, or other LLM providers.

## Use Cases

- Competitive CRM program tracking
- Membership benefit benchmarking
- Member-day campaign analysis
- Lifecycle communication audit
- Prospect-to-customer conversion offer analysis
- CRM prompt engineering portfolio demo

## Supported CRM Scenarios

| ID | Scenario |
| --- | --- |
| `membership_tier_benefits` | Membership Tier Benefits |
| `member_day_campaign` | Member Day Campaign |
| `existing_customer_communication_benefits` | Existing Customer Communication & Benefits |
| `prospect_communication_benefits` | Prospect Communication & Benefits |
| `prospect_new_existing_member_benefits` | Prospect/New/Existing Member Benefits |
| `new_customer_communication_benefits` | New Customer Communication & Benefits |

## Architecture

```text
crm-competitive-intelligence-agent/
├── README.md
├── requirements.txt
├── .gitignore
├── docs/
│   ├── architecture.md
│   ├── demo_workflow.md
│   └── prompt_design.md
├── examples/
│   ├── input/
│   │   └── membership_tier_benefits.md
│   ├── output/
│   │   ├── membership_tier_benefits.json
│   │   └── membership_tier_benefits_table.md
│   ├── sample_inputs/
│   │   ├── member_day_campaign.txt
│   │   ├── membership_tier_benefits.txt
│   │   └── screenshot_descriptions.md
│   ├── sample_ocr_text/
│   │   └── membership_tier_benefits.txt
│   └── sample_outputs/
│       ├── member_day_campaign.json
│       └── member_day_campaign.md
└── src/
    ├── crm_ci_agent/
    │   ├── __init__.py
    │   ├── agent.py
    │   ├── cli.py
    │   ├── exporters.py
    │   ├── ocr.py
    │   ├── prompts.py
    │   └── schemas.py
    └── run_demo.py
```

## Workflow

```text
Screenshot or screenshot description
        |
        v
OCR placeholder / manual transcript
        |
        v
Scenario selector
        |
        v
Extraction schema router
        |
        v
LLM extraction prompt
        |
        v
Validation and normalization
        |
        v
Markdown table + JSON output
```

## Prompt Design

The extraction prompt follows four principles:

- Use the selected scenario schema only.
- Fill every field with `exists` and `value`.
- Use `Not Mentioned` when the source does not provide explicit evidence.
- Do not infer from industry knowledge, CRM norms, or prior campaigns.

Example instruction:

```text
You are a CRM competitive intelligence extraction assistant.
Extract only information explicitly supported by the provided source text.
If a field cannot be verified, return "Not Mentioned".
Do not infer, summarize, or add recommendations.
```

Full prompt examples are available in [docs/prompt_design.md](docs/prompt_design.md).
The demo workflow is available in [docs/demo_workflow.md](docs/demo_workflow.md).
Mock screenshot descriptions are available in [examples/sample_inputs/screenshot_descriptions.md](examples/sample_inputs/screenshot_descriptions.md).

## Complete Mock Demo Case

### Membership Tier Benefits

This demo uses anonymized mock OCR text reconstructed from public-style loyalty program screenshots.

The source case represents 6 fictional screenshots from a loyalty program mini app page. The screenshots are not included. The mock OCR text covers membership enrollment rules, tier upgrade rules, points rules, birthday benefits, tier benefits, upgrade gifts, and points arrival rules.

Anonymized naming:

- Brand: `Brand A`
- Loyalty program: `Brand A Loyalty Program`
- Channel: `Official Mini Program`

Demo files:

| File | Purpose |
| --- | --- |
| [examples/input/membership_tier_benefits.md](examples/input/membership_tier_benefits.md) | Demo case description and input setup |
| [examples/sample_ocr_text/membership_tier_benefits.txt](examples/sample_ocr_text/membership_tier_benefits.txt) | Mock OCR extracted text |
| [examples/output/membership_tier_benefits_table.md](examples/output/membership_tier_benefits_table.md) | Structured Markdown table output |
| [examples/output/membership_tier_benefits.json](examples/output/membership_tier_benefits.json) | Structured JSON output |

This case demonstrates LLM-based structured extraction, prompt engineering, schema-driven output, and CRM competitive intelligence automation. It is a personal reimplementation / mock demo and does not represent a company project.

## Example Output

### Markdown

| Field | Exists | Extracted Content |
| --- | --- | --- |
| Campaign Channel | Yes | App membership center banner |
| Campaign Theme | Yes | Monthly Member Day |
| Start Date | Yes | 2026-05-20 |
| End Date | Yes | 2026-05-22 |
| Store Visit Gift | Yes | Complimentary mini gift after in-store check-in |
| Points Multiplier | Yes | 2x points for eligible purchases |
| MGM Referral | Not Mentioned | Not Mentioned |

### JSON

```json
{
  "scenario": "member_day_campaign",
  "records": [
    {
      "field": "Campaign Channel",
      "exists": "Yes",
      "value": "App membership center banner"
    },
    {
      "field": "MGM Referral",
      "exists": "Not Mentioned",
      "value": "Not Mentioned"
    }
  ]
}
```

## How to Run

Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the demo:

```bash
python src/run_demo.py \
  --scenario member_day_campaign \
  --input examples/sample_inputs/member_day_campaign.txt \
  --format both
```

Run as a module:

```bash
PYTHONPATH=src python -m crm_ci_agent.cli \
  --scenario membership_tier_benefits \
  --input examples/sample_inputs/membership_tier_benefits.txt \
  --format markdown
```

## Tech Stack

- Python
- Prompt engineering
- OCR placeholder
- LLM-ready extraction interface
- Pydantic-style structured data pattern
- Markdown and JSON exporters

## Extending the Project

To connect a real LLM provider, replace `DeterministicMockExtractor` in `src/crm_ci_agent/agent.py` with a provider implementation that sends:

- selected scenario
- schema field list
- source transcript
- extraction prompt

The provider should return the same `ExtractionResult` structure so exporters remain unchanged.

## Disclaimer

This is a personal reimplementation with mock data and does not contain confidential company information, private customer data, internal documents, or real brand-sensitive information. All examples are fictional and designed only to demonstrate LLM Agent, prompt engineering, structured extraction, and CRM competitive intelligence automation concepts.
